#!/usr/bin/env python3
"""Independent Fraction/NetworkX checker of census.log (not a copy of C test).

Run: python classify22/check.py classify22/census.log > classify22/check.log
Uses graph_atlas_g() for a separate enumeration through order seven; larger
orders have checked witnesses and external count comparisons, not an independently
recreated complete graph enumeration.
"""
import collections
from fractions import Fraction
from pathlib import Path
import sys
import networkx as nx

EXPECTED = {2: 1, 3: 2, 4: 6, 5: 21, 6: 112,
            7: 853, 8: 11117, 9: 261080}  # OEIS A001349


def decode(n, code):
    """Edges from column-packed integer, independently of census.c."""
    pairs = [(i, j) for j in range(1, n) for i in range(j)]
    bits = [(code >> p) & 1 for p in range(len(pairs) - 1, -1, -1)]
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from(pair for pair, bit in zip(pairs, bits) if bit)
    return graph


def exact_parameter(g):
    deg = dict(g.degree())
    ds = set(deg.values())
    if len(ds) == 1:
        return 'regular', len(ds), None, None
    hi = max(deg, key=deg.get)
    lo = min(deg, key=deg.get)
    m = {v: Fraction(sum(deg[w] for w in g[v]), deg[v]) for v in g}
    difference = m[lo] - m[hi]
    if difference <= 0:
        return None, len(ds), deg, m
    a = difference / (difference + deg[hi] - deg[lo])
    if not 0 < a < 1:
        return None, len(ds), deg, m
    rows = {a * deg[v] + (1-a) * m[v] for v in g}
    if len(rows) != 1:
        return None, len(ds), deg, m
    c = rows.pop()
    for v in g:
        lhs = a * deg[v] * deg[v] + (1-a) * sum(deg[w] for w in g[v])
        assert lhs == c * deg[v]  # independent A_alpha * degree eigenvector
    return a, len(ds), deg, m


def semiregular_bipartite(g):
    if not nx.is_bipartite(g):
        return False
    coloring = nx.bipartite.color(g)
    return all(len({g.degree(v) for v in coloring if coloring[v] == side}) == 1
               for side in (0, 1))


def main():
    path = Path(sys.argv[1] if len(sys.argv) > 1 else 'classify22/census.log')
    known = {}
    stated_counts = {}
    witnessed_counts = collections.Counter()
    distinct_counts = collections.Counter()
    for line in path.read_text().splitlines():
        if line.startswith('# n=') and 'connected=' in line:
            fields = dict(x.split('=') for x in line[2:].split() if '=' in x)
            n = int(fields['n'])
            if n == 1:
                continue
            assert int(fields['connected']) == EXPECTED[n], (n, fields)
            stated_counts[n] = {key: int(value) for key, value in fields.items()}
        elif line.startswith('W\t'):
            _, ns, cs, ars, ks = line.split('\t')
            n, code, k = int(ns), int(cs, 16), int(ks)
            p, q = map(int, ars.split('/'))
            assert (n, code) not in known
            g = decode(n, code)
            assert nx.is_connected(g), (n, cs)
            a, actual_k, _, _ = exact_parameter(g)
            assert a == Fraction(p, q) and k == actual_k, (n, cs, a)
            assert a <= Fraction(1, 2)
            assert (a == Fraction(1, 2)) == semiregular_bipartite(g)
            known[(n, code)] = (g, a, k)
            witnessed_counts[n] += 1
            distinct_counts[(n, k)] += 1
    assert len(stated_counts) == 8
    assert sum(witnessed_counts.values()) == len(known)
    for n, fields in sorted(stated_counts.items()):
        assert fields['irregular'] == witnessed_counts[n]
        assert fields['irregular'] == sum(distinct_counts[n, k] for k in range(2, 10))
        assert fields['alpha_eq_half'] == sum(a == Fraction(1, 2)
                for (n0, _), (_, a, _) in known.items() if n0 == n)
        print('CENSUS', n, 'connected', fields['connected'],
              'regular', fields['regular'], 'irregular', fields['irregular'],
              'degrees', [(k, distinct_counts[n, k]) for k in range(2, 10)
                          if distinct_counts[n, k]])

    # Independent externally supplied enumeration of every graph to n=7.
    atlas_counts = collections.Counter()
    atlas_irregular = collections.Counter()
    atlas_regular = collections.Counter()
    witnessed = collections.defaultdict(list)
    for (n, code), (g, a, k) in known.items():
        if n <= 7:
            witnessed[n].append((code, g, a))
    atlas_hits = collections.defaultdict(set)
    for g in nx.graph_atlas_g():
        n = len(g)
        if not 2 <= n <= 7 or not nx.is_connected(g):
            continue
        atlas_counts[n] += 1
        a, k, _, _ = exact_parameter(g)
        if a == 'regular':
            atlas_regular[n] += 1
        elif a is not None:
            atlas_irregular[n] += 1
            matches = [code for code, other, alpha in witnessed[n]
                       if alpha == a and nx.is_isomorphic(g, other)]
            assert len(matches) == 1, (n, matches, list(g.edges()))
            atlas_hits[n].add(matches[0])
    for n in range(2, 8):
        assert atlas_counts[n] == EXPECTED[n]
        assert atlas_regular[n] == stated_counts[n]['regular']
        assert atlas_irregular[n] == witnessed_counts[n]
        assert len(atlas_hits[n]) == witnessed_counts[n]
        print('ATLAS-INDEPENDENT', n, 'connected', atlas_counts[n],
              'regular', atlas_regular[n], 'irregular', atlas_irregular[n],
              'witness-bijection', 'PASS')

    # Cross-check that no reported two cases at the same order are isomorphic.
    signature = collections.defaultdict(list)
    for (n, code), (g, a, k) in known.items():
        key = (n, tuple(sorted(dict(g.degree()).values())), g.number_of_edges())
        for old_code, old_g in signature[key]:
            assert not nx.is_isomorphic(g, old_g), (n, code, old_code)
        signature[key].append((code, g))
    print('PAIRWISE-WITNESS-NONISOMORPHISM', len(known), 'PASS')

    # Explicit, independently re-readable five-degree witness.
    n, code = 9, int('00d47e9ed', 16)
    g, a, k = known[(n, code)]
    _, _, deg, avg = exact_parameter(g)
    c = next(iter({a * deg[v] + (1-a) * avg[v] for v in g}))
    print('FIVE-DEGREE', n, 'code', format(code, '09x'), 'alpha', a,
          'rho', c, 'degrees', [deg[v] for v in g],
          'neighbor-degree-sums', [sum(deg[w] for w in g[v]) for v in g])
    print('FIVE-DEGREE-EDGES', sorted(g.edges()))
    print('TOTAL', len(known), 'irregular certificates; all exact checks PASS')

if __name__ == '__main__':
    main()
