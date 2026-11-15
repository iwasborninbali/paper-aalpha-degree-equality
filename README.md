# Equality in Nikiforov's average-neighbour-degree bounds for A_α

Athanor lab (Aleksei Kudriashov, ORCID 0009-0006-8885-5338). Article in preparation; the LaTeX source and PDF will be in
`paper/`. Every result below has its certificate in `certificates/`.

## Results

For a connected graph, ρ(A_α) lies between the minimum and maximum of αd(u) + (1−α)m(u), m(u) the average degree of the
neighbours of u (Nikiforov, (20)–(21)); Nikiforov remarked that equality seems to hold only for regular graphs when α ≠ 0, 1/2.

1. **Structure (proof).** A nonregular connected equality graph has exactly one α, rational and at most 1/2; at α = 1/2 exactly
   the semiregular bipartite graphs; an exact classification of the two-degree case; A_α is singular in every nonregular case
   (`certificates/classify22/`).
2. **Every rational α in (0, 1/2] occurs (proof)** (`certificates/manydegrees/`).
3. **Unbounded degree variety (proof).** For every k ≥ 2 a connected graph on 2k vertices with k distinct degrees attains
   equality at α = 1/3 (`certificates/manydegrees/`; rebuilt independently and checked exactly to k = 40).
4. **Census (exact).** All irregular equality graphs on n ≤ 10 vertices: 1, 3, 7, 19, 23, 82, 128, 599 for n = 3..10
   (two independent generators to n = 9, nauty to n = 10) (`certificates/classify22/`, `certificates/guide-checks/`).

## Provenance

Results were found and checked in the audit of V. Nikiforov, *Merging the A- and Q-spectral theories*, Appl. Anal. Discrete
Math. 11 (2017) 81–107 (arXiv:1607.03015): repository
[athanor-aalpha-spectral](https://github.com/iwasborninbali/athanor-aalpha-spectral), Zenodo
[10.5281/zenodo.24239158](https://doi.org/10.5281/zenodo.24239158). ChatGPT research agents (OpenAI) wrote the proofs and
programs in separate threads; Anthropic Claude, the lab's guide, read the proofs line by line and re-derived the finite
results with independent programs (nauty `geng` and exact arithmetic, `certificates/guide-checks/`). The author of record
takes responsibility for the content. Text and data CC BY 4.0, code MIT.
