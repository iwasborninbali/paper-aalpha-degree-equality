# Equality in Nikiforov's average-neighbour-degree bounds for A_α

Athanor lab (Aleksei Kudriashov, ORCID 0009-0006-8885-5338). Article: [`paper/main.pdf`](paper/main.pdf) (LaTeX source
`paper/main.tex`, `paper/refs.bib`); arXiv package and metadata in [`arxiv/`](arxiv/); certificates for every result in
[`certificates/`](certificates/); literature check in [`PRIOR-ART.md`](PRIOR-ART.md) (two independent audits in `priority/`).

## Results

For a connected graph, ρ(A_α) lies between the minimum and maximum of αd(u) + (1−α)m(u), m(u) the average degree of the
neighbours of u (Nikiforov, (20)–(21)); Nikiforov remarked that equality seems to hold only for regular graphs when α ≠ 0, 1/2.

1. **Structure (proof).** A nonregular connected equality graph has exactly one α, rational and at most 1/2; at α = 1/2 exactly
   the semiregular bipartite graphs (Feng–Yu 2009); an exact classification of the two-degree case; A_α is singular in every
   nonregular case (`certificates/classify22/`).
2. **Every rational α in (0, 1/2] occurs (proof)** (`certificates/manydegrees/`).
3. **Unbounded degree variety (proof).** For every k ≥ 2 a connected graph on 2k vertices with k distinct degrees attains
   equality at α = 1/3 (`certificates/manydegrees/`; rebuilt independently and checked exactly to k = 40).
4. **Census (exact).** All irregular equality graphs on n ≤ 10 vertices: 1, 3, 7, 19, 23, 82, 128, 599 for n = 3..10
   (two independent generators to n = 9, nauty to n = 10) (`certificates/classify22/`, `certificates/guide-checks/`).

Not found in two independent bounded literature audits and the author's search (15 Nov 2026): the general recognition
criterion, the family K_t ∨ complement(K_m) at α = m/(2m+t−1) (the case K₄−e at α = 2/5 appears implicitly in Alhevaz et al.
2023, Remark 2.4), the all-rationals construction, the staircase family, the census. This is not a novelty certificate.

## Provenance

Found and checked in the audit of V. Nikiforov, *Merging the A- and Q-spectral theories*, Appl. Anal. Discrete Math. 11 (2017)
81–107 (arXiv:1607.03015): repository [athanor-aalpha-spectral](https://github.com/iwasborninbali/athanor-aalpha-spectral),
Zenodo [10.5281/zenodo.24239158](https://doi.org/10.5281/zenodo.24239158). ChatGPT research agents (OpenAI) wrote the
proofs, programs and the article draft in separate threads; Anthropic Claude, the lab's guide, read the proofs line by line,
re-derived the finite results with independent programs (nauty `geng` and exact arithmetic, `certificates/guide-checks/`) and
checked every reference. The author of record takes responsibility for the content. Text and data CC BY 4.0, code MIT.

Archived on Zenodo: version 1.0, [doi:10.5281/zenodo.24241527](https://doi.org/10.5281/zenodo.24241527) (all versions: [doi:10.5281/zenodo.24241526](https://doi.org/10.5281/zenodo.24241526)).
