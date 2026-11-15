# manydegrees: Nikiforov (20)--(21), unbounded degree variety and attainable parameters

Athanor lab / 2026-11-15. Finite simple connected undirected nonregular graphs; `0 < alpha < 1`, `A_alpha = alpha D + (1-alpha) A`. Source: V. Nikiforov, *Merging the A- and Q-spectral theories*, [arXiv:1607.03015](https://arxiv.org/pdf/1607.03015), **printed** pp. 12--14, Proposition 20 and Problem 22. This contribution concerns only (20)--(21), not (22)--(23). No paid services.

## Question

Does equality admit an unbounded number of **distinct vertex degrees**? Is the partition into degree classes equitable for the 3-, 4- and 5-degree witnesses in the independently generated complete census through order ten? Which rational `alpha` in `(0,1/2)` can be realized, and what are the accumulation points of the parameter set?

The existing [`classify22/REPORT.md`](../classify22/REPORT.md) **already proves** that a connected nonregular equality graph has exactly one rational `alpha` in `(0,1/2]`; that a two-degree equality partition is equitable; and that uniform independent blow-ups preserve degree variety. The independent [`guide/2026-11-15-independent-checks/README.md`](../guide/2026-11-15-independent-checks/README.md) establishes a nauty-generated complete graph6 census through `n=10`, including 599 irregular equality graphs on ten vertices. We use those results rather than re-claiming them.

## Results with evidence status

### 1. Arbitrarily many degrees at a fixed parameter: PROVED and independently checked exactly

**Theorem.** For every integer `k>=2`, there exists a connected simple equality graph on exactly `2k` vertices with exactly `k` distinct degrees, at `alpha=1/3`. Its Perron root is `(2k+1)/3`.

**Construction.** Vertices are `(i,b)` for `1<=i<=k`, `b in {0,1}`. For **distinct** levels `i!=j`, connect `(i,b)` to `(j,b)` if and only if `i+j>=k+1` (edges only in the same layer `b`). Also insert the rung `(i,0)--(i,1)` exactly when `2i>=k+1`. There are no other edges. This is a simple graph. The two vertices at level `i` each have **one** neighbor at every level `j` with `i+j>=k+1`: the neighbor at `j=i`, when eligible, is the opposite-layer rung. Thus the degree is exactly `i`, and the quotient for the *degree partition* has entries `B[i,j]=1` when `i+j>=k+1` and 0 otherwise. This partition is equitable. Both top-level vertices connect to all the lower levels in their own layer, and to each other; hence the whole graph is connected.

**Complete algebraic proof of equality.** At a vertex of degree `i`, the sum of neighbor degrees is

`w_i = sum_{j=k+1-i}^k j = i*(2*k+1-i)/2`.

Consequently, with `d` the positive degree vector,

`3*(A_(1/3)*d)_v = i^2 + 2*w_i = (2*k+1)*i`.

Therefore `A_(1/3)*d = ((2*k+1)/3)*d`. Since `0<=alpha<1` and the graph is connected, `A_alpha` is irreducible nonnegative, and Perron--Frobenius makes this positive eigenvalue the spectral radius. Equality in **both** Nikiforov inequalities (20),(21) follows from their row-sum similarity `D^-1 A_alpha D` (each row sum is the same). This proves unbounded distinct degrees, not merely unbounded graph order. The construction has order `2k`; this is **not** a minimum-order claim (the existing census has a five-degree example at `n=9`).

**Evidence:** `construct.py` independently produces graph6 witnesses for `k=2..12,20` in `witnesses.tsv`; the separately written `checker.py` *decodes* graph6 and checks the original vertex-by-vertex eigenvector identity in exact `Fraction` arithmetic, connectivity and equitability (`checker.log`). The proof, not the finite checks, establishes every `k`. The `k=5` example has ten vertices, degrees `1,1,...,5,5` and `rho=11/3`.

### 2. Degree partitions need not be equitable: EXACT CENSUS COUNTEREXAMPLES

At `alpha=1/3` the 9-vertex census witness `HCOfFF{` has degrees `[4,4,4,2,2,2,4,4,6]` (3 distinct degree values). Two vertices of degree 4 have **different neighbor-degree histograms** in ascending degree order `(2,4,6)`: `(1,2,1)` and `(0,4,0)`. Both have neighbor-degree sum `1*2+2*4+1*6=16=4*4`, so the exact equality equation still holds. This is a direct counterexample to equitability, already at **three** degrees.

The 9-vertex witness `HCQfFV{` has degrees `[5,4,4,2,3,3,4,5,6]` (five values) and is also non-equitable: degree-4 vertices realize `(0,1,1,1,1)` and `(0,0,2,2,0)` in level order `(2,3,4,5,6)`; both weighted sums are 18. At `alpha=1/3`, direct exact row checks establish equality. These are **existing guide census entries**, newly analyzed here for equitability; their occurrence as equality graphs is not a discovery claim.

`census.py` independently decodes and audits **every** irregular `eq-n2.log` through `eq-n10.log` entry, recomputes `p*d(v)^2+(q-p)*sum_{w~v}d(w)` and its ratio to `d(v)` with exact integers for `alpha=p/q`, and tests full degree-class neighbor histograms. In `census.log`, counts are `equitable/non-equitable` within each degree-variety class:

| n | total irregular | 3 degrees | 4 degrees | 5 degrees |
|---:|---:|---:|---:|---:|
| 5 | 7 | 1/0 | 0/0 | 0/0 |
| 6 | 19 | 2/0 | 0/0 | 0/0 |
| 7 | 23 | 4/0 | 1/0 | 0/0 |
| 8 | 82 | 2/0 | 3/0 | 0/0 |
| 9 | 128 | 17/2 | 1/0 | 0/1 |
| 10 | 599 | 27/22 | 6/0 | 5/1 |
| **2--10 total** | **862** | **53/24** | **11/0** | **5/2** |

Hence every *observed* 4-degree example through `n=10` is equitable, **not** a theorem for arbitrary order. A degree class with fixed `d` has a fixed **first moment** `sum neighbor-degree`, not necessarily a fixed histogram. The complete-census status comes from the guide's nauty run, not an independent full re-enumeration by this scanner.

### 3. Complete set of interior parameters: PROVED; independent rational witnesses

**Theorem.** As `G` ranges over connected nonregular simple graphs, the possible parameters in `0<alpha<1` for equality in (20)--(21) are **exactly** the rationals in `(0,1/2]`. In particular **every reduced `p/q` with `0<2p<q` occurs**, and the set of such parameters is dense in `(0,1/2)`, with its closure equal to `[0,1/2]`. Denominators are unbounded.

**Existence proof.** Take positive integers `p,q` with `0<2p<q` and set `r=q-2p>=1`. Form `G` by taking the complete graph `K_(r+1)` and attaching `p` new pendant leaves to each clique vertex. This is connected, nonregular, and has exactly two degrees `a=r+p>1` (clique vertices) and `b=1` (leaves). Every clique vertex has `x=r` neighbors of high degree, and each leaf has `y=1` such neighbor. By the independently proved **two-degree quotient criterion** in `classify22/REPORT.md`, the unique equality parameter satisfies

`alpha/(1-alpha) = y/b - x/a = 1 - r/(r+p) = p/(r+p)`, hence `alpha = p/(r+2p) = p/q`.

For completeness, one can verify directly: put `L=alpha+(1-alpha)*(r+p)`; the leaf's `A_alpha*d` equation reads `L*1=alpha*1+(1-alpha)*(r+p)`. A clique vertex has neighbor-degree sum `r*(r+p)+p`; substitution of `alpha=p/(r+2p)` gives `alpha*(r+p)^2+(1-alpha)*(r*(r+p)+p)=L*(r+p)`. Positivity, connectedness and Perron--Frobenius prove equality. For `alpha=1/2`, any semiregular bipartite nonregular graph (e.g. `K_(1,2)`) works, as **already** established in `classify22/` and older Q-index literature.

**Necessity:** the earlier `classify22` theorem gives rationality and the upper bound `1/2` for nonregular connected equality graphs at `0<alpha<1`; we do not reattribute that argument to this report. Combining necessity and construction proves the complete interior parameter set. Because every rational in `(0,1/2)` is realized, its closure is `[0,1/2]`. Values at `alpha=0` and `alpha=1` are **outside this interior classification** and must be treated separately; harmonic graph literature concerns the former.

**Evidence:** `construct.py` includes rational witnesses `1/7,1/4,2/5,3/8,4/11,5/13,7/20`, checked independently in `checker.log` using only rational arithmetic. These are samples; the exact proof covers all rationals.

## Priority check

**Read first:** repository `verify/REPORT.md`, `attack/REPORT.md`, `status/REPORT.md`, `priority/REPORT.md`, `classify22/REPORT.md`, `problem30odd/REPORT.md`, `oddlambda2/REPORT.md`, `forkmatrices/REPORT.md`, and `guide/2026-11-15-independent-checks/{README.md,eq22.py,eq-n*.log}`. The lab's version 1.0 is archived at [Zenodo DOI 10.5281/zenodo.24239159](https://doi.org/10.5281/zenodo.24239159); these findings are **not** asserted to be present there.

**External literature inspected/queried, 2026-11-15:** Nikiforov, original arXiv PDF pp. 12--14 and published [journal text](https://doiserbia.nb.rs/img/doi/1452-8630/2017/1452-86301701081N.pdf), Proposition 20; Liu--Das--Shu (2020), *Discrete Mathematics* 343, 111917, [DOI](https://doi.org/10.1016/j.disc.2020.111917), §5 Theorems 5.4--5.6 and Lemma 2.9; Petrović--Borovićanin--Radosavljević (2006), [*The integral 3-harmonic graphs*](https://doi.org/10.1016/j.laa.2005.11.024), adjacency `A*d=lambda*d` at `alpha=0`; and publicly indexed work on `A_alpha` main eigenvalues and equitable partitions. Search phrases included `A alpha degree vector eigenvector arbitrarily many distinct degrees`, `Nikiforov Problem 22 equality equitable degree partition`, `anti triangular equitable quotient graph degrees 1 to k`, `A alpha Perron degree vector rational alpha all rationals`, and `harmonic graphs adjacency degree vector eigenvector`.

**Priority verdict:** The theorem for *unbounded degree variety at `alpha=1/3`* and the *all-interior-rationals construction* have complete proofs in this contribution and were **not located explicitly** in these bounded searches. **Novel publication priority is NOT VERIFIED.** The `classify22` two-degree theorem and its leaf-attachment construction were pre-existing repository results: the new observation is the elementary `r=q-2p, t=p` specialization yielding all rationals, not a claim of a new general two-degree classification. The non-equitable graph6 witnesses were already published in the guide census as equality examples; only the histogram test is added here.

## Reproduction and SHA-256

From the repository root, with **Python 3 standard library only**, no paid service or download:

```sh
python3 manydegrees/construct.py > /tmp/manydegrees-witnesses.tsv
diff -u manydegrees/witnesses.tsv /tmp/manydegrees-witnesses.tsv
python3 manydegrees/checker.py manydegrees/witnesses.tsv > /tmp/manydegrees-checker.log
diff -u manydegrees/checker.log /tmp/manydegrees-checker.log
python3 manydegrees/census.py > /tmp/manydegrees-census.log
diff -u manydegrees/census.log /tmp/manydegrees-census.log
(cd manydegrees && sha256sum -c SHA256SUMS)
```

`SHA256SUMS` contains SHA-256 for every other new file, including `REPORT.md`, source programs and logs. The independent checker decodes the generator's graph6 **without importing its code**. The census scanner independently decodes nauty graph6 and checks equality *per vertex*; it is a certificate verifier, not a second enumeration of all graphs.

## Not covered

- An unrestricted *structural classification* of all 3/4/5-degree or arbitrary-degree equality graphs. In particular, no proof or counterexample about 4-degree equitability **beyond n=10**.
- The smallest number of vertices for `k` distinct degrees, beyond the displayed upper bound `n<=2k`.
- A complete list of equality graphs of order `n>=11`, or equality at the endpoint `alpha=0` or `alpha=1`, or Nikiforov (22)--(23), or disconnected graphs.
- A proof that no prior author published this staircase family or the all-rationals corollary; a complete citing-paper audit and formal proof-assistant verification were not performed.

## Next steps

Investigate the **structure of non-equitable fibers** under the fixed neighbor-degree-sum condition, including whether four-degree non-equitable examples exist for `n>10`; seek degree-preserving *multi-edge trades* that alter per-class neighbor counts while preserving their weighted sums. Then derive an explicit family realizing unbounded degree variety at **other fixed rational alphas** (the current staircase gives only `1/3`), and audit the literature on equitable quotient realizations and harmonic graphs through full texts/citation trails. These are independent directions beyond the solved existence questions.
