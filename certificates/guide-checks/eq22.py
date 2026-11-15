"""Guide's independent check of equality in Nikiforov (20)-(21): reads graph6 lines (nauty geng -c n) on stdin.

For a connected graph, rho(A_alpha) equals max/min of f(u) = alpha d(u) + (1-alpha) m(u), m(u) = (sum of neighbour
degrees)/d(u), iff f is constant. So the points (d(u), m(u)) must lie on one line of slope -alpha/(1-alpha) < 0.
Prints one line per irregular equality graph: graph6, alpha, number of distinct degrees; then a total line.
"""
import sys
from fractions import Fraction


def decode(line):
    data = [c - 63 for c in line]
    n = data[0]
    bits = []
    for x in data[1:]:
        bits.extend((x >> k) & 1 for k in range(5, -1, -1))
    adj = [[] for _ in range(n)]
    i = 0
    for v in range(1, n):
        for u in range(v):
            if bits[i]:
                adj[u].append(v); adj[v].append(u)
            i += 1
    return n, adj


def equality_alpha(n, adj):
    d = [len(a) for a in adj]
    m = [Fraction(sum(d[w] for w in adj[u]), d[u]) for u in range(n)]
    if len(set(d)) == 1:
        return "regular"
    pts = sorted(set(zip(d, m)))
    if len({p[0] for p in pts}) != len(pts):       # same degree, different m: impossible
        return None
    (d0, m0), (d1, m1) = pts[0], pts[1]
    slope = (m1 - m0) / (d1 - d0)
    if slope >= 0:
        return None
    if any((mi - m0) != slope * (di - d0) for di, mi in pts[2:]):
        return None
    lam = -slope                                     # alpha/(1-alpha)
    return lam / (1 + lam)


def main():
    regular = irregular = total = 0
    for raw in sys.stdin.buffer:
        line = raw.strip()
        if not line or line.startswith(b">"):
            continue
        total += 1
        n, adj = decode(line)
        a = equality_alpha(n, adj)
        if a == "regular":
            regular += 1
        elif a is not None:
            irregular += 1
            print(line.decode(), a, len({len(x) for x in adj}), sep="\t")
    print(f"TOTAL connected {total} regular {regular} irregular {irregular}")


main()
