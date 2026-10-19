# Response to Reviewer Sshp (R2)

We thank Reviewer Sshp for the careful evaluation and for recognizing the rigor of the theoretical contribution (Soundness: 4).

**W1: No real-data causal estimate; only synthetic CATE injection.**

We agree this is an important consideration and appreciate the suggestion. We address this at three levels:

(1) **Methodological standard.** Synthetic CATE injection on real text features is the established evaluation protocol in this literature. PPI (Angelopoulos et al., 2023), DSL (Egami et al., 2023), and the recent benchmark by Audinet et al. (2025) all use the same approach because no public dataset simultaneously provides: (a) LLM annotations, (b) expert gold labels, (c) a known causal effect, and (d) subgroup structure with heterogeneous annotation quality. Our paper explicitly acknowledges this gap (Limitations section).

(2) **Real annotation heterogeneity is validated.** While CATEs are synthetic, the LLM annotation errors are entirely real. Our case studies use actual GPT-4.1 annotations on UC Berkeley Hate Speech (Δπ = 0.117 across demographic subgroups, Section 5.2) and actual GPT-4o/Claude/Llama annotations on CivilComments (Δπ up to 0.184, Appendix P). These confirm that subgroup-heterogeneous error — the phenomenon driving our bias identity — arises in real annotation settings. The bias identity's R² ≥ 0.97 is validated on confusion matrices from all nine real LLMs (Section 5.3).

(3) **The contribution is primarily theoretical.** The core result (Theorem 1) is an exact algebraic identity: global correction introduces bias = δ_s · Δτ / (1−2π̄). This holds by construction whenever error rates are heterogeneous, regardless of how CATEs arise. The synthetic evaluation verifies the theorem's predictions, not a specific empirical claim about a particular domain.

We acknowledge constructing a fully real causal benchmark with LLM annotation as valuable future work.

**W2: K ≤ 4 is an important limitation; what should practitioners do with finer subgroups?**

We agree and offer the following guidance (which we will add to the Limitations section):

- **Hierarchical grouping**: When the natural subgroup structure has K > 4, practitioners can merge subgroups with similar error rates (identifiable from a pilot sample) to reduce K to ≤ 4 before applying EC-HTE. The diagnostic criterion (Proposition 1) can guide which groupings preserve the most heterogeneity.
- **Selective application**: Apply EC-HTE only to the top-K most heterogeneous subgroups (ranked by |δ_s|) and retain global correction for the remainder.
- **The K = 8 analysis in Appendix R** shows that HB partial pooling reduces stratified MLE RMSE by 47%, but still exceeds global correction at n_expert = 250 (~31 labels per subgroup). The bottleneck is per-subgroup sample size, not a fundamental limitation of the method — with sufficient expert budget (≥ 1000), K = 8 becomes viable.
