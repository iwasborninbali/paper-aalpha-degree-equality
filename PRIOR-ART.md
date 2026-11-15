# Prior-art and evidence audit — 2026-11-15

**Article:** *Equality in Nikiforov's average-neighbour-degree bounds for A_alpha*  
**Athanor lab / Aleksei Kudriashov**, ORCID 0009-0006-8885-5338, Bali, Indonesia.  
**Audit status:** bounded literature search, **not** a claim of publication novelty.

## Primary source and scope

* V. Nikiforov, “Merging the A- and Q-spectral theories,” *Applicable Analysis and Discrete Mathematics* **11** (2017), 81–107, DOI [10.2298/AADM1701081N](https://doi.org/10.2298/AADM1701081N); source preprint [arXiv:1607.03015](https://arxiv.org/abs/1607.03015). Read Proposition 20, inequalities (20) and (21), the text immediately before Problem 22, and Problem 22; compare to the 2017 journal wording. These are the bounds based on `f_alpha(v)=alpha*d(v)+(1-alpha)*m(v)`, `m(v)=sum_{w~v} d(w)/d(v)`. Nikiforov proved regularity for connected equality graphs when `1/2<alpha<1`. His informal expectation before Problem 22 suggested regularity except possibly at `alpha=0,1/2`. The present article addresses only (20) and (21), not the separate edge bounds (22)–(23), disconnected graphs, or endpoint alpha=0.
* **Version warning:** the 2016 arXiv and peer-reviewed 2017 texts differ elsewhere. In particular, Proposition 29's max-cut expression was corrected **in the 2017 journal**. It is **not** an uncorrected flaw in the journal article. The other endpoint/problem-number discrepancies documented by the background audit are outside the present article.

## Published related work, exact locations, and attribution

1. R. Merris, “A note on Laplacian graph eigenvalues,” *Linear Algebra Appl.* **285** (1998), 33–35, DOI [10.1016/S0024-3795(98)10148-9](https://doi.org/10.1016/S0024-3795(98)10148-9). The degree-plus-average-neighbour-degree approach precedes the `A_alpha` interpolation; this is not an attribution of the 2017 proposition to Merris.
2. L. Feng and G. Yu, “On three conjectures involving the signless Laplacian spectral radius of graphs,” *Publ. Inst. Math. (Beograd)* **85(99)** (2009), 35–38, DOI [10.2298/PIM0999035F](https://doi.org/10.2298/PIM0999035F). Prior signless-Laplacian equality and semiregular bipartite phenomena. The case `alpha=1/2` must not be claimed as an original classification here.
3. S. Liu, K. C. Das and J. Shu, “On the eigenvalues of `A_alpha`-matrix of graphs,” *Discrete Mathematics* **343** (2020), 111917, DOI [10.1016/j.disc.2020.111917](https://doi.org/10.1016/j.disc.2020.111917). Reports identify **Lemmas 2.9 and 2.10** (degree relations), **Theorems 5.4–5.6** (related equality statements). **Theorem 5.4** applies to the *edge bounds (22)–(23)*, not (20)–(21); **Theorem 5.6** treats disconnected equality with `alpha>1/2`. The older semiregular case and related degree conditions are credited, not proposed as new. The background audit also mentions **Lemma 2.5** (adjacency least-eigenvalue extremum), outside this manuscript's scope.
4. S. Wang, D. Wong and F. Tian, *Linear Algebra Appl.* **590** (2020), 210–223, DOI [10.1016/j.laa.2019.12.039](https://doi.org/10.1016/j.laa.2019.12.039). Another edge-/degree-based `A_alpha` spectral bound, **not** the present row-sum equality characterization.
5. M. Petrović, B. Borovićanin and Z. Radosavljević, “The integral 3-harmonic graphs,” *Linear Algebra Appl.* **416** (2006), 298–312, DOI [10.1016/j.laa.2005.11.024](https://doi.org/10.1016/j.laa.2005.11.024). Earlier harmonic-graph work concerns `A*d=lambda*d` at **alpha=0**; the present classification is for the strictly interior parameter.
6. H. Lin, J. Xue and J. Shu, “On the `A_alpha`-spectra of graphs,” *Linear Algebra Appl.* **556** (2018), 210–219, DOI [10.1016/j.laa.2018.07.003](https://doi.org/10.1016/j.laa.2018.07.003), [arXiv:1709.00182](https://arxiv.org/abs/1709.00182). **Theorem 1.1** already resolves a different `lambda_k` equality problem and corrects the uniqueness clause in Nikiforov Proposition 31(a); not claimed in this paper.
7. J. Xue, R. Liu, G. Yu and J. Shu, “The multiplicity of `A_alpha`-eigenvalues of graphs,” *Electronic J. Linear Algebra* **36** (2020), 645–657, DOI [10.13001/ela.2020.4999](https://doi.org/10.13001/ela.2020.4999). **Equation (3.7)** and **Lemma 3.5** already provide spectral information for `K_1 join 2K_s` relevant to a distinct `lambda_2` project; no claim of priority is made for it.
8. B. D. McKay and A. Piperno, “Practical graph isomorphism, II,” *J. Symbolic Comput.* **60** (2014), 94–112, DOI [10.1016/j.jsc.2013.09.003](https://doi.org/10.1016/j.jsc.2013.09.003). The census uses nauty's `geng` v2.9.3, credited to its authors.

All bibliography entries in `paper/refs.bib` have source DOIs from the reports or independently retrieved metadata; none is invented. The journal-version attribution of the corrected Proposition 29 is intentional.

## New results relative to the *reports*, not necessarily to the literature

The proof in `certificates/classify22/REPORT.md` gives: unique rational equality alpha at most 1/2, singularity and normalized-adjacency eigenvalue, exact integer criterion and denominator bound, and complete equitable two-degree classification. It also proves joins of regular pieces have at most two distinct degree values. The earlier lab audit already contained `K_t join E_m` and `K_1 join K_{2,2}` as nonregular interior-alpha examples. These older lab contributions are not rebranded as new here.

The proof in `certificates/manydegrees/REPORT.md` gives: a family on `2k` vertices with exactly `k` distinct degrees, all attaining equality at alpha=1/3; and the realization of every rational in `(0,1/2]` using a clique with the same number of pendant leaves at each clique vertex. Non-equitable degree partitions are witnessed by exact order-9 graph6 entries from the independent guide census; the report's histogram analysis was performed after the census.

**Search verdict (2026-11-15):** no explicit published statement equivalent to the all-interior-rationals construction, unbounded-degree staircase, integer recognition criterion or exact order-ten census was verified in the checked material. **This is a negative result of a limited search, not a priority certificate, novelty claim, comprehensive citing-paper audit, or an assertion that no prior publication exists.**

## Dated searches (all on 2026-11-15)

The original project reports document examination of the following exact subjects/queries:

* `Nikiforov problem 22 equality row sums alpha average neighbor degree irregular five degrees`
* `A alpha Merris bounds equality degree vector eigenvector semiregular graph`
* `On the eigenvalues of A_alpha-matrix of graphs Liu Das Shu section 5 theorem 5.6`
* `A_alpha degree vector eigenvector graph irregular rational alpha singularity classification`
* `graph spectral harmonic graphs degree vector Perron eigenvector generalized adjacency matrix alpha`
* `A alpha degree vector eigenvector arbitrarily many distinct degrees`
* `Nikiforov Problem 22 equality equitable degree partition`
* `anti triangular equitable quotient graph degrees 1 to k`
* `A alpha Perron degree vector rational alpha all rationals`
* `harmonic graphs adjacency degree vector eigenvector`
* `A_alpha average neighbour degree equality`, `Nikiforov Problem 22 equality`, and `Merris A_alpha equality nonregular join`.

The background `priority/REPORT.md` additionally records searches for `K1 join 2Ks second eigenvalue`, `A_alpha least eigenvalue balanced complete bipartite`, `Problem 30 Nikiforov`, `A_alpha eigenvalue differentiability`, `Proposition 29 maxcut`, and `Proposition 31(a) equality` across arXiv, MathOverflow, publisher pages, Google Scholar-indexed results, Semantic Scholar-indexed results and OpenAlex metadata. The guide's separate search surveyed a public OpenAlex list of **304** citing works by abstract topic in a *different Problem 30* inquiry, not a full-text audit of all 304 for the present equality problem. The full text and complete citation chain of every citing paper have **not** been checked. This audit of the present research cannot establish negative publication priority.

## Evidence status and reproducibility

* **THEOREM / full written proof:** `certificates/classify22/REPORT.md`, `certificates/manydegrees/REPORT.md`; fully rewritten in `paper/main.tex`. They do not depend on graph enumeration, floating point, or a proof assistant.
* **EXACT FINITE CENSUS to n=9 / independently regenerated:** `certificates/classify22/census.c`, `census.log`, `check.py`, `check.log`. Run C11 connected graph vertex-extension enumeration, exact integer test and independent Python Fraction validator. The NetworkX graph atlas independently supplies a complete catalogue to n=7. Separate nauty `geng -cq N` catalogue agrees for n=2,…,9.
* **EXACT FINITE CENSUS to n=10 / single nauty enumeration plus independent exact checking:** `certificates/guide-checks/eq22.py`, `eq-n2.log` … `eq-n10.log`, `SHA256SUMS`, and the background `guide/2026-11-15-independent-checks/README.md`. This nauty enumeration supplies **11,716,571** connected isomorphism classes at n=10, **167** regular and **599** irregular equality classes with degree-count split **538/49/6/6** for 2/3/4/5 distinct degrees. It is checked by `certificates/manydegrees/census.py`, `census.log` using exact rational and integer identities, but no third complete independent n=10 generator has been run.
* **EXACT CONSTRUCTION CHECKS, corroborating all-k proof:** `certificates/manydegrees/construct.py`, `witnesses.tsv`, `checker.py`, `checker.log`, `SHA256SUMS`: 19 exact graph6 witnesses checked, including selected k=2…12,20 and p/q samples. `certificates/guide-checks/staircase-check.log` independently rebuilds the staircase from the written rule and verifies k=2…40 with exact `Fraction` arithmetic.
* **FLOATING-POINT SCANS, not proof:** the background `athanor-aalpha-spectral/verify/`, and unrelated spectral optimization scans in its `guide/` reports include floating-point eigenvalue tests. They are corroboration only; not the basis for the main article's structural proofs or the exact census.
* **SHA-256:** each source directory has `SHA256SUMS` listing released scripts, reports and output hashes. Replay with a C11 compiler, Python 3, nauty `geng` 2.9.3, and for earlier independent checks NetworkX; no paid services or secrets are required.

## Repository and archive provenance

* Article source and certificates: <https://github.com/iwasborninbali/paper-aalpha-degree-equality>
* Background prior-art and independent guide work: <https://github.com/iwasborninbali/athanor-aalpha-spectral>, particularly `verify/REPORT.md`, `priority/REPORT.md`, `guide/2026-11-15-independent-checks/README.md`.
* Associated research archive: DOI [10.5281/zenodo.24239158](https://doi.org/10.5281/zenodo.24239158). The background's version 1.0 is DOI `10.5281/zenodo.24239159`; the newer article results are **not** asserted to be present in that older snapshot.

**Responsibility:** Independent checking was coordinated with AI assistance; Aleksei Kudriashov takes responsibility for the article, evidence statuses and attribution.
