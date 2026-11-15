# Independent priority audit b

Date: 2026-11-15. Auditor: b. Question: PRIOR PUBLICATION of equality in the vertexwise (20)--(21) of V. Nikiforov (2017), not of the distinct edgewise (22)--(23). Independence: no other auditor's answer was consulted. Search limitations and access status are explicit below.

## Four verdicts

**1. PARTLY PUBLISHED.** Prior: V. Nikiforov, *Merging the A- and Q-spectral theories*, *Appl. Anal. Discrete Math.* **11** (2017), 81--107, DOI [10.2298/AADM1701081N](https://doi.org/10.2298/AADM1701081N), **Proposition 20, p. 92**, proves equality only regular for connected G and alpha>1/2. L. Feng and G. Yu, *On three conjectures involving the signless Laplacian spectral radius of graphs*, *Publ. Inst. Math. (Beograd)* **85(99)** (2009), 35--38, DOI [10.2298/PIM0999035F](https://doi.org/10.2298/PIM0999035F), **Lemma 2.3, pp. 36--37**, proves the alpha=1/2 endpoint: regular or semiregular bipartite. See also S. Liu, K. C. Das and J. Shu, *Discrete Mathematics* **343** (2020), article 111917, DOI [10.1016/j.disc.2020.111917](https://doi.org/10.1016/j.disc.2020.111917), **Lemma 2.9**. In the present **nonregular** setting, the endpoint therefore means exactly semiregular bipartite. No previous explicit result verified for *at most one* alpha, alpha rational, or the equitable two-degree iff criterion.

**2. PARTLY PUBLISHED.** Endpoint alpha=1/2 and spectral methods for joins have antecedents (Feng--Yu 2009; Nikiforov 2017, Section 7), but no prior publication found of every rational alpha in (0,1/2] being attainable, of **K_t join E_m** attaining equality at alpha=m/(2m+t-1), or of the consequent counterexample to the remark preceding **Problem 22, Nikiforov (2017), p. 93**. Here E_m is the edgeless graph. To be irregular require m>=2, t>=1. At t=1 one gets alpha=1/2; for all reduced p/q with 0<2p<q, attach p leaves to every vertex of K_{q-2p+1}, yielding alpha=p/q. These observations are easy deductions and should not be framed as automatically novel despite not locating explicit earlier publication.

**3. NOT FOUND.** No earlier source located that constructs for **every k>=2** a connected 2k-vertex graph with exactly k distinct degrees and equality at alpha=1/3. The repository's staircase construction has vertices (i,b) for 1<=i<=k, b in {0,1}; within each layer connect distinct i,j when i+j>=k+1 and add the rung at i when 2i>=k+1. Each degree i occurs twice, with neighbor-degree sum i(2k+1-i)/2, and the Perron root is (2k+1)/3. This is stronger than the known alpha=0 harmonic constructions or arbitrary-order claims. No exact DOI/theorem/page for a prior equivalent could be verified.

**4. NOT FOUND.** No previous publication located of the exact irregular equality-graph isomorphism counts on n=3..10, namely **1,3,7,19,23,82,128,599**, or a classification of all such graphs. Harmonic graphs with **A d=lambda d** are established at alpha=0, not positive alpha; see M. Petrovic, B. Borovicanin and Z. Radosavljevic (2006), *The integral 3-harmonic graphs*, *Linear Algebra Appl.* **416**, 298--312, DOI [10.1016/j.laa.2005.11.024](https://doi.org/10.1016/j.laa.2005.11.024). A related alpha=1/2 family has a quadratic 2-walk identity; see H. Deng and H. Huang (2013), *On the main signless Laplacian eigenvalues of a graph*, *Electronic J. Linear Algebra* **26**, 381--393, DOI [10.13001/1081-3810.1659](https://doi.org/10.13001/1081-3810.1659), **Theorem 2.6, p. 385**. Neither supplies this enumeration. The raw independent n=10 guide report advertised in the README was **not found at the tested repository path**; this auditor has **not independently regenerated or certified 599**.

**Interpretation:** NOT FOUND = no exact predecessor verified in this bounded search, *not* proof of first publication. PARTLY PUBLISHED = specified subclaims are known; the full assertion was **not** found. No claim is marked "already published" in full.

## Why the comparison is strict

Let d be the positive degree vector, s_v=sum_{w~v}d_w, and m_v=s_v/d_v. For a connected graph, equality in either of Nikiforov's vertexwise bounds is equivalent to all row sums of D^{-1} A_alpha D being equal, equivalently
A_alpha d = rho(A_alpha) d.
The equivalent local identity is
s_v = -[alpha/(1-alpha)] d_v^2 + [rho(A_alpha)/(1-alpha)] d_v.
This is the substantive equality condition, not merely equality in some other A_alpha upper bound. For precisely two degree classes a>b, the criterion from the repository is an equitable degree partition with x neighbors of degree a in the high class, y in the low class, and h=y/b-x/a>0; then alpha=h/(1+h). For three or more degrees, constant first neighbor-degree moment does **not** imply an equitable degree partition.

At alpha=0, A d=lambda d defines an ordinary harmonic graph (sometimes called pseudo-regular when m_v is constant). At alpha=1/2, Qd=lambda d is the known signless Laplacian endpoint. Deng--Huang's quadratic **s=-d^2+a d-b** (2013, Theorem 2.6) has coefficient -1 and a possible constant b; it is NOT an equivalent classification of the alpha=1/3 equation with coefficient -1/2.

## Source-by-source theorem inspection and full-text access

1. **Nikiforov (2017)**, DOI 10.2298/AADM1701081N: **full article PDF read**, Proposition 20 at p.92, Corollary 21 and Problem 22 at p.93. URL https://arxiv.org/pdf/1607.03015 ; journal PDF https://doiserbia.nb.rs/img/doi/1452-8630/2017/1452-86301701081N.pdf . Note that arXiv and printed versions differ in some later proposition numbering. The author explicitly speculated irregular equality only for alpha=0,1/2 rather than proving it.
2. **Feng--Yu (2009)**, DOI 10.2298/PIM0999035F: **full author-uploaded text read**, Lemma 2.3 pp.36--37, including proof and converse. URL https://www.researchgate.net/publication/228685834_On_three_conjectures_involving_the_signless_Laplacian_spectral_radius_of_graphs . Exact known semiregular result, also explicitly credited by Nikiforov.
3. **Liu--Das--Shu (2020)**, DOI 10.1016/j.disc.2020.111917: **indexed full theorem text read** (Lemmas 2.7--2.10, Theorems 5.4--5.6), but **direct publisher full PDF/page unavailable**. URL https://www.sciencedirect.com/science/article/pii/S0012365X20301096 . **Theorem 5.4 concerns edgewise bounds**, not the present vertexwise bounds; **Theorem 5.6 addresses disconnected graphs with alpha>1/2**. Although the abstract says the paper solves a Nikiforov problem, it does not solve the connected alpha<1/2 vertexwise claim. This distinction must not be lost by comparing theorem numbers without their formulas.
4. **Deng--Huang (2013)**, DOI 10.13001/1081-3810.1659: **full journal PDF read**, Theorems 2.5 and 2.6, printed pp.384--385. URL https://journals.uwyo.edu/index.php/ela/article/download/1253/1253/1253 .
5. **Alhevaz, Baghipur, Ganie and Das (2023)**, *On the A_alpha-spectral radius of connected graphs*, *Ars Math. Contemp.* **23**, P1.06, DOI [10.26493/1855-3974.2697.43a](https://doi.org/10.26493/1855-3974.2697.43a): **full author-uploaded HTML/PDF text read**, Theorems 2.1, 2.3, 2.5, 2.7, 2.10, 2.14 and 3.2. Theorem **2.3** only restates Nikiforov's vertexwise bound and alpha>1/2 equality; the other propositions analyze **different** inequalities. URL https://www.researchgate.net/publication/362795717_On_the_Aa-spectral_radius_of_connected_graphs .
6. **Alhevaz, Baghipur and Ganie (2024)**, *Bounds for the spectral radius of the A_alpha-matrix of graphs*, *Indian J. Pure Appl. Math.* **55**, 298--309, DOI [10.1007/s13226-023-00363-9](https://doi.org/10.1007/s13226-023-00363-9): **full PDF read**, Theorems **3.1--3.4** (pp.300--302) and **4.1--4.7** (pp.304--307). Spectral-radius combinations and other degree bounds; no equality classification of the precise vertexwise expression. PDF https://insa.nic.in/writereaddata/UpLoadedFiles/IJPAM/Vol55_2024_1_ART23.pdf .
7. **Lenes, Mallea-Zepeda and Rodriguez (2020)**, *New Bounds for the alpha-Indices of Graphs*, *Mathematics* **8**, 1668, DOI [10.3390/math8101668](https://doi.org/10.3390/math8101668): **full HTML read**, Lemma 7 and Theorem 4. Theorem 4 features bidegreed equality graphs for a **different order/size/minimum-degree bound**, not Nikiforov (20)--(21). There is a corrigendum, DOI [10.3390/math10152619](https://doi.org/10.3390/math10152619). URL https://www.mdpi.com/2227-7390/8/10/1668 .
8. **Petrovic, Borovicanin and Radosavljevic (2006)**, DOI 10.1016/j.laa.2005.11.024: **abstract/metadata only; full text not accessible**. Defines harmonic by A d=lambda d and determines 26 integral 3-harmonic connected graphs, unrelated to alpha>0 census. URL https://www.sciencedirect.com/science/article/pii/S0024379505005689 .
9. **Petrovic et al. (2003)**, *Harmonic graphs with small number of cycles*, *Discrete Math.* **265**, 31--44, DOI [10.1016/S0012-365X(02)00620-9](https://doi.org/10.1016/S0012-365X(02)00620-9): **bibliographic record/abstract only; full paper not accessible**, alpha=0.
10. **MathOverflow (2013--2014)**, *Coherence between different ranking methods of a graph's vertices*, https://mathoverflow.net/questions/149674/coherence-between-different-ranking-methods-of-a-graphs-vertices/179916 : **full question/answer text read**; harmonic adjacency case is acknowledged, not alpha>0.

### Additional screened citing or closely related papers (abstract/title only, full text NOT inspected)

- Xue, Lin, Liu, Shu, *On the A_alpha-spectral radius of graphs*, *Linear Algebra Appl.* **550** (2018), 105--120, DOI 10.1016/j.laa.2018.03.038.
- Lin, Huang, Xue, *A note on A_alpha-spectral radius of graphs* (2018), DOI 10.1016/j.laa.2018.08.008.
- Wang, Wong, Tian, *Bounds for the largest and smallest A_alpha-eigenvalues of a graph in terms of vertex degrees*, *Linear Algebra Appl.* **590** (2020), 210--223, DOI 10.1016/j.laa.2019.12.039.
- Guo, Zhou, *On the alpha-spectral radius of graphs*, *Applicable Analysis and Discrete Mathematics* **14** (2020), 431--458, DOI 10.2298/AADM180210022G.
- Ji, Wang, Brunetti, Bian, *A_alpha-spectral radius and measures of graph irregularity*, *Linear Multilinear Algebra* **70** (2022), 5247--5267, DOI 10.1080/03081087.2021.1910617.
- Xu, Wong, Tian, *On the multiplicity of alpha as an eigenvalue of the A_alpha-matrix of a graph in terms of the number of pendant vertices*, *Linear Algebra Appl.* **594** (2020), 193--204.
- Pirzada, *Two upper bounds on the A_alpha-spectral radius of a connected graph*, *Communications in Combinatorics and Optimization* **7** (2022), 53--57.
- Li, Sun, *Some bounds on the A_alpha-index of connected graphs with fixed order and size* (2021), DOI 10.1080/03081087.2021.1932710.
- Yuan, Liu, Yuan, *The A_alpha-spectral radius of nonregular graphs (digraphs) and maximum degree (outdegree)* (2022), DOI 10.1016/j.disopt.2022.100758.
- Chen, Li, Shiu, *Some results on A_alpha-eigenvalues of a graph* (2022), DOI 10.1080/03081087.2022.2135676.
- Gomes da Silva et al., *Bounds for A_alpha-eigenvalues* (2023), DOI 10.1051/ro/2023144.
- Li, Chen, Huang, *Bounding the A_alpha-spectral radius of k-connected irregular graphs* (2024), DOI 10.1216/rmj.2024.54.227.
- Hong et al., *Sharp upper bounds on A_alpha-spectral radius* (2026), arXiv:2606.00843.
- Pasten, *Advances on alpha_0-Nikiforov problem* (2026), DOI 10.1007/s40314-026-03653-0: **different** Nikiforov problem.
- Cha, Shan, *Graphs with zero as a main eigenvalue of the signless Laplacian* (2026 preprint): Q-main rather than general-alpha claim.
- Marciniak, Syslo, *On graphs with prescribed neighborhood degrees of vertices* (2022 conference abstract): a realization problem, not the proposed Perron identity.
- TUM dissertation https://mediatum.ub.tum.de/doc/1226561/4612691.pdf : **indexed snippet only**, different Nikiforov eigenvalue bounds.

For all items in this subsection, the abstract/title screening gives a **weaker negative** than full-theorem inspection. Some may be paywalled or poorly indexed. Their titles were not treated as proof of non-overlap.

## OpenAlex citing-paper sweep

The source is [OpenAlex work W2963258333](https://openalex.org/works/W2963258333). On 2026-11-15 its work metadata showed **305 citing works**, whereas the filtered citing-work listing showed **304**. **Titles from all 13 filtered pages (304 entries) were screened**, and the relevant-looking A_alpha, irregularity, degree, Q-index, bound, and Perron-related candidates are listed above. This is a *title sweep*, not a claim that all 304 abstracts or full texts were opened. The 305/304 discrepancy is unresolved. Full citation listings:

[page 1](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=1) | [2](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=2) | [3](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=3) | [4](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=4) | [5](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=5) | [6](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=6) | [7](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=7) | [8](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=8) | [9](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=9) | [10](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=10) | [11](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=11) | [12](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=12) | [13](https://openalex.org/works?filter=referenced_works%3AW2963258333&page=13).

### Exact or near-exact web queries run

Source/equality: "Nikiforov problem 22 equality alpha average neighbour degree irregular"; "Merging the A and Q spectral theories" "Problem 22" equality; "Feng Yu signless Laplacian spectral radius d_i + m_i equality semiregular DOI"; "On three conjectures involving the signless laplacian spectral radius of graphs" doi pdf Feng Yu; "d_i+m_i" "semiregular bipartite" Feng Yu theorem.

Liu and other citing papers: "On the eigenvalues of A_alpha-matrix of graphs" "Theorem 5.4" "Theorem 5.5"; same "Theorem 5.6" "Problem"; same "Lemma 2.9"; same filetype:pdf; "On the A_alpha-spectral radius of connected graphs" full theorem 2.3; "On the main signless Laplacian eigenvalues of a graph" theorem 6 authors doi.

Eigenvector/equivalent identities: "A_alpha" "degree vector" eigenvector irregular graph equality; "alpha" "degree vector" eigenvector "A_alpha" irregular graph; "A+cD" "degree vector" "eigenvector" graph; "alpha D" "degree vector" "eigenvector" irregular; "A_alpha" "Perron" "degree vector" graph equality; "K_t" "m/(2m+t-1)" "alpha" graph.

Quadratic/graph construction: graphs where sum of degrees neighbors is quadratic in vertex degree; "sum of neighbor degrees" "quadratic" "degree" spectral graph; "quadratic" "2-walk" "degree" graph; graph "two-walk" "parabolic" neighbor degrees; graph "2-walk" "parabolic" degrees sum neighbor; "2-walk" "parabolic" "generalized adjacency" site:arxiv.org.

Older vocabulary: "harmonic" "pseudo-harmonic" graph "A_alpha"; graph "generalized harmonic" "A+cD" degree vector; "harmonic graphs" "degree vector" "Perron" LAA; "The integral 3-harmonic graphs" Petrovic Borovicanin Radosavljevic theorem.

Site and theses: site:mathoverflow.net "harmonic" "degree vector" graph eigenvector; site:mathoverflow.net "Nikiforov" "Problem 22" spectral; site:ejla.math.fsu.edu "A_alpha" "degree vector"; site:combinatorics.org "A_alpha" "Merris" equality; thesis "A_alpha" "average neighbor degree" equality; dissertation generalized adjacency matrix Nikiforov problem 22 equality; site:arxiv.org "Nikiforov" "Merris" "equality" "semiregular" alpha.

Also searched the exact census count sequence and the staircase inequality i+j>=k+1 with A_alpha. None located a published identical result. Searches used indexed Google Scholar/publisher references, arXiv-domain search, MathOverflow, journal and thesis pages; **no reliable complete export** from native Google Scholar or arXiv full-text search could be obtained. The stated negatives are search-limited.

## Repository materials inspected / completeness caveat

Read via the **GitHub connector on main**: [README.md](https://github.com/iwasborninbali/paper-aalpha-degree-equality/blob/main/README.md), [certificates/classify22/REPORT.md](https://github.com/iwasborninbali/paper-aalpha-degree-equality/blob/main/certificates/classify22/REPORT.md), and [certificates/manydegrees/REPORT.md](https://github.com/iwasborninbali/paper-aalpha-degree-equality/blob/main/certificates/manydegrees/REPORT.md), including their existing bounded priority sections. The first cert reports exact enumeration to n=9; the second reports the general staircase proof, parameter construction, and guide's nauty n=10 result.

Attempts to fetch certificates/guide-checks/REPORT.md, certificates/guide-checks/README.md, and certificates/guide/2026-11-15-independent-checks/README.md on main all returned **not found**. The referenced priority/REPORT.md at the tested target-repository path was also unavailable; some references likely point to another repository. The missing advertised raw source means the exact count of 599 should be presented as **certificate-reported, not independently recomputed here**.

## Publication-language recommendation

Credit Feng--Yu (2009) Lemma 2.3 unambiguously for alpha=1/2 and Nikiforov (2017) Proposition 20 for alpha>1/2. Do not conflate the different bounds addressed in Liu--Das--Shu (2020) Theorem 5.4. State that a search has **not located earlier explicit formulations** of unique rational alpha, the two-degree criterion, all rationals via split/leaf attachment, the fixed-alpha staircase, or the census, rather than asserting that no such publication exists. This audit supplies **no full prior DOI/theorem/page** for those unlocated claims.
