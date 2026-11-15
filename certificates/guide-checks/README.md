# Guide's independent checks (Claude, 2026-11-15)

| File | What | Status |
|---|---|---|
| `eq22.py`, `eq-n2..10.log` | every connected graph of order 2-10 from nauty `geng -c` 2.9.3 (a generator independent of `classify22/census.c`); exact `Fraction` test of constant row sums alpha d(v) + (1 - alpha) m(v): one line per irregular equality graph (graph6, alpha, number of distinct degrees) and a total line | **exact** census; orders 2-9 agree with `classify22/census.log` in every count and in the degree-variety distribution; order 10 (11,716,571 connected graphs, 167 regular, 599 irregular equality graphs) is from this run only |
| `staircase-check.log` | the staircase graphs rebuilt from the written construction (not from `manydegrees/construct.py`) for k = 2..40: connected, k distinct degrees on 2k vertices, all row sums (2k+1)/3 at alpha = 1/3 | **exact** for these k; the all-k statement is the written proof |

Derived counts used in the article (from `eq-n*.log`): equality at alpha = 1/2 for n = 3..10: 1, 1, 2, 2, 3, 3, 5, 6; maximum number of distinct degrees for n = 3..10: 2, 2, 3, 3, 4, 4, 5, 5.

Replay: `geng -cq N | python3 eq22.py > eq-nN.log` (order 10 took 4.5 minutes on one core).
