#!/usr/bin/env python3
"""Generate connected, nonregular exact equality candidates (stdlib only).

Output TSV: name, graph6, alpha, Perron eigenvalue, distinct degrees, equitable.
Run from repository root: python3 manydegrees/construct.py > manydegrees/witnesses.tsv
"""
from fractions import Fraction


def staircase(k):
    assert k >= 2
    adj = [set() for _ in range(2 * k)]
    def edge(u, v):
        assert u != v and v not in adj[u]
        adj[u].add(v)
        adj[v].add(u)
    for i in range(1, k + 1):
        for j in range(i + 1, k + 1):
            if i + j >= k + 1:
                for side in (0, 1):
                    edge(2 * (i - 1) + side, 2 * (j - 1) + side)
        if 2 * i >= k + 1:
            edge(2 * (i - 1), 2 * (i - 1) + 1)
    return adj, Fraction(1, 3), Fraction(2 * k + 1, 3)


def pendant(p, q):
    assert 0 < 2 * p < q
    r = q - 2 * p
    h = r + 1
    adj = [set() for _ in range(h * (p + 1))]
    def edge(u, v):
        adj[u].add(v)
        adj[v].add(u)
    for u in range(h):
        for v in range(u + 1, h):
            edge(u, v)
        for t in range(p):
            edge(u, h + u * p + t)
    # Leaf row gives the Perron root directly.
    a = Fraction(p, q)
    return adj, a, a + (1 - a) * (r + p)


def graph6(adj):
    n = len(adj)
    assert 2 <= n <= 62
    bits = [int(u in adj[v]) for v in range(1, n) for u in range(v)]
    bits += [0] * ((-len(bits)) % 6)
    return chr(n + 63) + ''.join(chr(63 + sum(bits[i + j] << (5 - j)
                                for j in range(6))) for i in range(0, len(bits), 6))


def emit(name, adj, alpha, rho):
    d = [len(a) for a in adj]
    levels = sorted(set(d))
    signatures = {t: {tuple(sum(d[v] == s for v in adj[u]) for s in levels)
                      for u in range(len(d)) if d[u] == t} for t in levels}
    equitable = all(len(v) == 1 for v in signatures.values())
    print(name, graph6(adj), str(alpha), str(rho), len(levels),
          int(equitable), sep='\t')


def main():
    for k in list(range(2, 13)) + [20]:
        emit(f'staircase-{k}', *staircase(k))
    for p, q in [(1, 7), (1, 4), (2, 5), (3, 8), (4, 11), (5, 13), (7, 20)]:
        emit(f'pendant-{p}-{q}', *pendant(p, q))


if __name__ == '__main__':
    main()
