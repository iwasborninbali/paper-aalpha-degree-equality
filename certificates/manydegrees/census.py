#!/usr/bin/env python3
"""Independent graph6 census audit on the guide's complete nauty files.

Run from repository root: python3 manydegrees/census.py > manydegrees/census.log
Reads, but does not change, guide/2026-11-15-independent-checks/eq-n*.log.
The guide's nauty enumeration, not this program, establishes completeness.
"""
from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path

GUIDE = Path('guide/2026-11-15-independent-checks')


def decode(g):
    n = ord(g[0]) - 63
    assert 2 <= n <= 62
    bits = []
    for ch in g[1:]:
        b = ord(ch) - 63
        assert 0 <= b <= 63
        bits.extend((b >> shift) & 1 for shift in range(5, -1, -1))
    assert len(bits) >= n * (n - 1) // 2
    adj = [set() for _ in range(n)]
    index = 0
    for right in range(1, n):
        for left in range(right):
            if bits[index]:
                adj[left].add(right)
                adj[right].add(left)
            index += 1
    return adj


def audit(g, astr, recorded_k):
    adj = decode(g)
    n = len(adj)
    d = [len(a) for a in adj]
    assert min(d) > 0
    assert len(set(d)) == int(recorded_k) >= 2
    visited = {0}
    queue = deque([0])
    while queue:
        for v in adj[queue.popleft()]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    assert len(visited) == n
    a = Fraction(astr)
    assert 0 < a <= Fraction(1, 2)
    # Independently check each row with integer arithmetic: q*s + p*d^2 -p*s = L*d.
    p, q = a.numerator, a.denominator
    values = [(p * d[v] * d[v] + (q - p) * sum(d[w] for w in adj[v]), d[v])
              for v in range(n)]
    num, den = values[0]
    assert all(x * den == num * y for x, y in values)
    levels = sorted(set(d))
    by_degree = defaultdict(set)
    for v in range(n):
        by_degree[d[v]].add(tuple(sum(d[w] == target for w in adj[v]) for target in levels))
    equitable = all(len(hist) == 1 for hist in by_degree.values())
    return len(levels), equitable, {k: sorted(v) for k, v in sorted(by_degree.items())}


def main():
    aggregate = defaultdict(int)
    first = {}
    for n in range(2, 11):
        counts = defaultdict(int)
        path = GUIDE / f'eq-n{n}.log'
        rows = 0
        seen = set()
        with path.open(encoding='ascii') as handle:
            for line in handle:
                line = line.rstrip('\n')
                if not line or line.startswith('TOTAL '):
                    continue
                code, a, k = line.split('\t')
                assert code not in seen
                seen.add(code)
                assert ord(code[0]) - 63 == n
                deg_count, equitable, histogram = audit(code, a, k)
                key = (deg_count, 'eq' if equitable else 'non')
                counts[key] += 1
                aggregate[key] += 1
                if deg_count in (3, 5) and not equitable and deg_count not in first:
                    first[deg_count] = (n, code, a, histogram)
                rows += 1
        entries = ' '.join(f'{k}:{counts[(k,"eq")]}/{counts[(k,"non")]}' for k in (2, 3, 4, 5))
        print(f'n={n} irregular={rows} equitable/non_equitable {entries}')
    print('AGGREGATE n=2..10', ' '.join(
        f'{k}:{aggregate[(k,"eq")]}/{aggregate[(k,"non")]}' for k in (2, 3, 4, 5)))
    for k in (3, 5):
        n, code, a, hist = first[k]
        print(f'COUNTEREXAMPLE k={k} n={n} graph6={code} alpha={a} histogram={hist}')


if __name__ == '__main__':
    main()
