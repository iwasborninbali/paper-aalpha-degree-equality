#!/usr/bin/env python3
"""Independent exact checker for graph6/alpha/rho witness TSV; no imports from construct.

Run: python3 manydegrees/checker.py manydegrees/witnesses.tsv
"""
import sys
from collections import deque
from fractions import Fraction


def read_graph6(code):
    values = [ord(c) - 63 for c in code]
    n = values.pop(0)
    if not 2 <= n <= 62 or any(not 0 <= x < 64 for x in values):
        raise ValueError('unsupported graph6')
    bitstream = ''.join(format(x, '06b') for x in values)
    assert len(bitstream) >= n * (n - 1) // 2
    E = []
    cursor = 0
    for j in range(1, n):
        for i in range(j):
            if bitstream[cursor] == '1':
                E.append((i, j))
            cursor += 1
    return n, E


def check(record):
    name, code, astr, lstr, countstr, eqstr = record.rstrip('\n').split('\t')
    n, edges = read_graph6(code)
    neighbors = [[] for _ in range(n)]
    for u, v in edges:
        assert u < v and v not in neighbors[u]
        neighbors[u].append(v)
        neighbors[v].append(u)
    queue = deque([0])
    visited = {0}
    while queue:
        for w in neighbors[queue.popleft()]:
            if w not in visited:
                visited.add(w)
                queue.append(w)
    assert len(visited) == n, name
    degree = [len(nb) for nb in neighbors]
    assert min(degree) > 0 and len(set(degree)) > 1
    a, lam = Fraction(astr), Fraction(lstr)
    assert 0 < a <= Fraction(1, 2)
    assert len(set(degree)) == int(countstr)
    for v in range(n):
        # This is the *original unscaled eigenvector equation*, not a row-sum slope check.
        lhs = a * degree[v] ** 2 + (1 - a) * sum(degree[w] for w in neighbors[v])
        assert lhs == lam * degree[v], (name, v, lhs, lam * degree[v])
    levels = sorted(set(degree))
    classes = {x: [v for v in range(n) if degree[v] == x] for x in levels}
    hist = {x: {tuple(sum(degree[w] == j for w in neighbors[v]) for j in levels)
                for v in classes[x]} for x in levels}
    equitable = all(len(s) == 1 for s in hist.values())
    assert equitable == bool(int(eqstr))
    return name, n, len(edges), len(levels), str(a), str(lam), equitable


def main():
    with open(sys.argv[1], encoding='ascii') as source:
        rows = [check(line) for line in source if line.strip()]
    for name, n, m, levels, a, rho, equitable in rows:
        print(f'PASS {name} n={n} m={m} degrees={levels} alpha={a} '
              f'rho={rho} equitable={int(equitable)}')
    print(f'TOTAL checked={len(rows)} failures=0 exact=Fraction')


if __name__ == '__main__':
    main()
