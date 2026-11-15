# classify22: equality in Nikiforov's (20)--(21) for connected graphs

**Athanor lab / 2026-11-15.** Target: V. Nikiforov, *Merging the A- and Q-spectral theories*, [arXiv:1607.03015v1](https://arxiv.org/pdf/1607.03015), printed pp. 12--14, Proposition 20 and Problem 22. Finite simple undirected connected graphs, order `n>=2`, `0<alpha<1`, `A_alpha=alpha D+(1-alpha)A`. No paid service used.

## Question

Classify equality in (20) and (21), i.e. `rho(A_alpha)` between the maximum and minimum of `f_alpha(u)=alpha*d(u)+(1-alpha)*m(u)`, where `m(u)=sum_{v~u}d(v)/d(u)`. On a connected graph, equality in **either** is equivalent to equality in **both**, because `D^-1 A_alpha D` is irreducible nonnegative and its row sums are the `f_alpha(u)`.

## Results with evidence status

### 1. Complete structural restrictions (PROVED below)

**Theorem A.** For a connected graph with at least two vertices:

1. If regular, equality holds for **every** `0<alpha<1`.
2. If nonregular, **at most one** `alpha` works, and it is rational and lies in `0<alpha<=1/2`. At `alpha=1/2`, equality holds **exactly** for semiregular bipartite graphs (the two bipartition classes have constant degrees).
3. Write `a=Delta`, `b=delta`, `s_u=sum_{v~u} d(v)`, choose `x` of degree `a` and `y` of degree `b`, and put `H=(a-b)ab`, `K=a*s_y-b*s_x`. For a nonregular equality graph, `0<K<=H`, and the unique parameter is `alpha=K/(H+K)`; all vertices must satisfy
   `(K*d(u)^2+H*s_u)*a = (K*a^2+H*s_x)*d(u)`.
   Conversely, if these exact integer conditions hold, equality does hold. In lowest terms the denominator of `alpha` is at most `2(n-2)(n-1)^2`.
4. The matrix `A_alpha` is **singular** for every nonregular equality case, and the normalized adjacency `D^-1/2 A D^-1/2` has eigenvalue `-alpha/(1-alpha)`. This supplies a separate necessary spectral test.

**Proof.** `A_alpha 1=d`. The common-row-sum criterion is equivalent to `A_alpha d=c d` with `c=rho(A_alpha)>0`: the degree vector is positive, so irreducible Perron--Frobenius makes `c` the spectral radius. Consequently `A_alpha(d-c 1)=0`. For nonregular `d-c 1 != 0`, hence singularity. Now `A_alpha=(1-alpha)Q+(2alpha-1)D`, `Q=D+A`, and `z^T Qz=sum_{uv in E}(z_u+z_v)^2>=0`. Since `D` is positive definite, `alpha>1/2` makes `A_alpha` positive definite, impossible. At `alpha=1/2`, `A_alpha=Q/2`; `Q` is singular for connected `G` iff `G` is bipartite, and its nullspace is spanned by the sign vector `z` on the two parts. The relation `Q(d-c 1)=0` gives `d=c 1+t z`, so degrees are constant on each part. Conversely, if the two degrees are `r,s`, then `Qd=(r+s)d`, proving equality at `alpha=1/2`. If `t=0`, the graph is regular. For `alpha<1/2`, choose vertices `x,y` with degrees `a>b`. Equality of their rows, clearing denominators, gives `alpha H=(1-alpha)K`, or `alpha=K/(H+K)`. The interval `0<alpha<=1/2` gives `0<K<=H`. Comparing each row with `x` proves the displayed integer tests and their sufficiency. Because `a-b<=n-2` and `a,b<=n-1`, `H<=(n-2)(n-1)^2`, hence `H+K<=2(n-2)(n-1)^2`, bounding the reduced denominator. Finally, singularity of `A_alpha=D^1/2[alpha I+(1-alpha)D^-1/2 A D^-1/2]D^1/2` proves the normalized-adjacency statement. QED.

### 2. Two-degree classification and sufficient infinite constructions (PROVED)

**Theorem B (exact two-degree classification).** Let the degrees be precisely `a>b`. If equality holds, the partition by degrees is **equitable**: every degree-`a` vertex has a fixed number `x` of degree-`a` neighbors and every degree-`b` vertex a fixed number `y` of degree-`a` neighbors. Conversely, any connected two-degree graph with this property has equality at the single parameter

`h=y/b-x/a`, `alpha=h/(1+h)` **iff** `h>0`.

Automatically `h<=1`; `h=1` iff there are no intra-class edges, precisely the semiregular bipartite case. Every `0<h<1` provides a nonregular equality case below `1/2`.

**Proof.** At fixed degree, constant `f_alpha` forces constant `m` because `alpha<1`. If a vertex has degree `d in {a,b}` and `k` neighbors of degree `a`, then `m=b+(a-b)k/d`. Hence the `k` values are constant in each degree class; call them `x,y`. Subtraction of the two row sums gives `alpha(a-b)=(1-alpha)(a-b)(y/b-x/a)`. Solve for `alpha` and use `0<=x/a<=1`, `0<=y/b<=1`. For `h=1`, necessarily `x=0`, `y=b`, making both degree classes independent and all edges cross. The converse follows by the same row identity and positivity of `d`. QED.

**Construction.** Any connected equitable two-degree graph satisfying `y/b>x/a` works, whether or not it is a join. In particular, the **already known to this lab** split graph `K_t join E_m` has `alpha=m/(2m+t-1)` (for `t>=2,m>=2`); `K_1 join K_{2,2}` has `alpha=1/4`. Other examples include attaching `t>=1` pendant leaves to every vertex of a connected `r`-regular graph (`r>=1`): high degree `r+t`, low degree `1`, and `alpha=t/(r+2t)`. More generally, if `G` is any equality graph, replacing every vertex by `k` independent clones and every edge by a complete bipartite graph between clone sets multiplies both `d` and `m` by `k`, preserving connectedness, the parameter, and the number of distinct degree values. This gives arbitrarily large examples with **five** degrees using the witness below.

**Complete joins of regular pieces do not explain higher-degree witnesses (PROVED).** Suppose `G` is a complete join of internally regular graphs (arbitrarily many pieces), with total degree sum `S=sum_v d(v)` and order `n`. For a vertex of degree `d` in any piece, its neighbor-degree sum is `S-(n-d)d`, hence `m=d-n+S/d`. Equality requires `d^2-(c+(1-alpha)n)d+(1-alpha)S=0` for every occurring degree `d`. This quadratic has at most **two** roots. Thus an irregular equality join of regular pieces has at most two degree values; the higher-degree witnesses cannot be such joins.

### 3. Exhaustive classification to nine vertices (EXACT FINITE CENSUS, independently checked as qualified)

| n | Connected classes | Regular classes (all alpha) | Irregular cases (one alpha each) | Distinct degree counts among irregular cases (2/3/4/5) | Irregular cases at alpha=1/2 |
|---:|---:|---:|---:|---|---:|
| 2 | 1 | 1 | 0 | 0/0/0/0 | 0 |
| 3 | 2 | 1 | 1 | 1/0/0/0 | 1 |
| 4 | 6 | 2 | 3 | 3/0/0/0 | 1 |
| 5 | 21 | 2 | 7 | 6/1/0/0 | 2 |
| 6 | 112 | 5 | 19 | 17/2/0/0 | 2 |
| 7 | 853 | 4 | 23 | 18/4/1/0 | 3 |
| 8 | 11,117 | 17 | 82 | 77/2/3/0 | 3 |
| 9 | 261,080 | 22 | 128 | 107/19/1/1 | 5 |
| **Sum** | **273,192** | **54** | **263** | **229/28/5/1** | **17** |

The `263` row certificates (`W`) are **all** in `census.log`, using compact column-packed adjacency codes (see replay instructions). Of these, `246` have `alpha<1/2`; `17` have `alpha=1/2`. **n=9 has a five-distinct-degree case**, so a claim that at most two or three degree values can occur is false. Selected exact witness:

- `n=9`, canonical code `00d47e9ed`, degrees `(2,3,3,4,4,4,5,5,6)` at `alpha=1/3`.
- Neighbor-degree sums `(11,15,15,18,18,18,20,20,21)` in the same vertex order. Consequently `f_alpha(u) = (d(u)+2 s_u/d(u))/3 = 13/3` for all nine vertices and `rho(A_{1/3})=13/3`.
- Edge list (zero-based): `(0,7),(0,8),(1,5),(1,7),(1,8),(2,4),(2,6),(2,8),(3,4),(3,5),(3,6),(3,7),(4,6),(4,8),(5,6),(5,8),(6,7),(7,8)`.
- The earliest three-/four-/five-degree witnesses in the census occur at orders `5/7/9`, respectively. At `n=5`, `K_1 join P_4` has degree sequence `(2,2,3,3,4)` and `alpha=1/3`. At `n=7`, the four-degree certificate `0000019ff` has degrees `(1,1,3,3,4,4,6)`, `alpha=2/5`.

**Completeness mechanism.** `census.c` starts at `K_1`. For each canonical connected graph on `n-1` vertices it adjoins a vertex along every nonempty neighbor subset, canonically relabels the result, and deduplicates by its canonical bit code. Every connected graph has a vertex whose deletion leaves it connected (a leaf of a spanning tree), so the induction covers all connected graphs. Its canonicalizer starts from degrees, iteratively refines by neighbor-color counts, then minimizes the adjacency bit code over all permutations *within the resulting invariant color classes*. Isomorphic graphs have identical color partitions and identical minimized codes, while a code determines a graph; this supplies an exact isomorphism certificate independently of the count checks. For each representative, the C test uses the integer equations in Theorem A, **never floating point**.

**Cross-checks.** Connected graph totals at each `n` match OEIS [A001349](https://oeis.org/A001349) (1,1,2,6,21,112,853,11117,261080 for `n=1..9`). `check.py`, written separately in Python with `fractions.Fraction` and NetworkX, independently decodes **all 263 cases**, recomputes their exact parameters/row sums, checks the full eigenvector equation and connectivity, and tests pairwise nonisomorphism. It separately enumerates the NetworkX Graph Atlas to `n=7`, checks both regular and irregular totals, and finds a bijective isomorphism match for **every** atlas irregular equality case (`check.log`). This is an independent exhaustive cross-check through order seven. At orders eight and nine, the *enumeration completeness* depends on the explicit C canonical-generation proof plus agreement with published total counts; we do **not** claim a second independently generated exhaustive catalog at those orders. Graph Atlas and OEIS are independent public data sources, not paid services.

### Replay instructions / evidence files

From repository root (ordinary C compiler, Python 3 with freely available `networkx`):

```sh
cc -std=c11 -O3 -Wall -Wextra -o /tmp/classify22-census classify22/census.c
/tmp/classify22-census 9 > /tmp/classify22-census.replay.log
diff -u classify22/census.log /tmp/classify22-census.replay.log
python classify22/check.py classify22/census.log > /tmp/classify22-check.replay.log
diff -u classify22/check.log /tmp/classify22-check.replay.log
(cd classify22 && sha256sum -c SHA256SUMS)
```

`W<TAB>n<TAB>hex_code<TAB>alpha<TAB>number_of_distinct_degrees` is the record format. To decode `hex_code`, take its low-order `n(n-1)/2` bits in order from most to least significant, associated to pairs `(0,1),(0,2),(1,2),(0,3),(1,3),(2,3),...,(n-2,n-1)`. Graphs are zero-based. The standalone log is deterministic and includes one row per irregular equality class plus totals. `SHA256SUMS` hashes the other five published files, not itself. No service, API key, or floating-point computation is needed by the C census.

## Priority check

**Previously known to the lab, not claimed as new:** `K_t join E_m` and `K_1 join K_{2,2}` at their respective parameters; see [`priority/REPORT.md`](../priority/REPORT.md), section 1, and [`verify/REPORT.md`](../verify/REPORT.md), Problem 22. The journal's 2017 Proposition 20 has the same bounds; it proves connected regularity for `alpha>1/2`. Liu--Das--Shu, *Discrete Mathematics* **343** (2020) 111917, [DOI 10.1016/j.disc.2020.111917](https://doi.org/10.1016/j.disc.2020.111917), Lemma 2.9, includes the established regular/semiregular bipartite characterization for `d+m` constant; its Theorems 5.4--5.6 treat related equality bounds. Do **not** call the `alpha=1/2` case a new result.

**Queries checked 2026-11-15:** original paper (arXiv v1 pp. 12--14 and journal pp. 92--93); repository `verify/`, `attack/`, `status/`, and `priority/`; searches for `Nikiforov problem 22 equality row sums alpha average neighbor degree irregular five degrees`, `A alpha Merris bounds equality degree vector eigenvector semiregular graph`, `On the eigenvalues of A_alpha-matrix of graphs Liu Das Shu section 5 theorem 5.6`, `A_alpha degree vector eigenvector graph irregular rational alpha singularity classification`, and `graph spectral harmonic graphs degree vector Perron eigenvector generalized adjacency matrix alpha`. Other topical hits: Wang--Wong--Tian, *Linear Algebra Appl.* **590** (2020), 210--223, [DOI 10.1016/j.laa.2019.12.039](https://doi.org/10.1016/j.laa.2019.12.039) (different degree-edge bound). **No indexed explicit equivalent of the five-degree example or this exact finite census was verified, but the search is bounded**; no comprehensive cited-by full-text audit of all ~300 works was made, so **novelty is NOT established**. Credit the older published Q-index and neighbor-degree results.

## Not covered

- A structural characterization of *all* graphs with three or more distinct degrees, or a bound on degree variety at arbitrary order. The n=9 five-degree example refutes a three-/four-degree universal cap; blow-up preserves five degrees, but does not produce arbitrarily many distinct degrees.
- Exhaustive graph classes for `n>=10`, all isomorphism types beyond the explicit `n<=9` record, or Problem 22's edge bounds (22)--(23) and disconnected cases.
- A second independently generated **complete** n=8 or n=9 isomorphism catalog. OEIS checks and the independent per-witness checker do not replace such a catalog.
- Exhaustive scholarly priority / journal correction audit; absence of a hit is not proof of publication novelty. Theoretical claims here have complete arguments but have not been formally checked in a proof assistant.

## Next steps

**Most promising:** seek an *infinite construction with unboundedly many distinct degrees*, or prove a nontrivial cap under a natural hypothesis (e.g. bounded degree-class quotient rank). Start by solving the exact linear conditions on a small equitable multi-cell quotient and perform independent fraction-based witness verification; the n=9 five-degree certificate `00d47e9ed` is a useful seed. In parallel, independently regenerate the full n=8--9 classes with nauty `geng` or another separately implemented canonical algorithm, then compare every encoded equality witness, not only class counts. Finally perform a deeper citation trail check before asserting priority.
