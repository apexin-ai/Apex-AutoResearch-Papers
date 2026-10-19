We thank Reviewer Sshp for the careful evaluation and for recognizing the rigor of the theoretical contribution (Soundness: 4).

**Semi-synthetic evaluation follows established causal inference protocol; real LLM heterogeneity is independently validated**

We agree that real-data causal estimates would strengthen external validity. However, observational studies cannot provide a known ground-truth CATE — the quantity our method corrects — making direct real-data evaluation of bias reduction infeasible. The established protocol in this literature uses ground truth known by construction:

1. **PPI** (Angelopoulos et al., *Science*, 2023): evaluates on real datasets with ground-truth parameters computed from gold-standard labels
2. **DSL** (Egami et al., *NeurIPS*, 2023): evaluates on real text/survey datasets against ground truth from full expert annotation
3. **Audinet de Pieuchon et al.** (*EMNLP*, 2025): the most comprehensive benchmark; reports that debiasing can *increase* MSE when prediction error is heterogeneous — precisely the phenomenon our bias identity explains (Theorem 1)

Our semi-synthetic design extends this principle to the causal setting: known CATEs injected onto real text features. No public dataset simultaneously provides LLM annotations, expert gold labels, a known causal effect, and subgroup-heterogeneous annotation quality.

Complementarily, our real-data case studies validate the *precondition* — that LLM error rates are genuinely heterogeneous: **Δπ = 0.117** (GPT-4.1 on UC Berkeley Hate Speech, §5.2), **Δπ up to 0.184** (GPT-4o/Claude/Llama on CivilComments, App. V), and **R² = 0.975** across 11 LLM–dataset combinations (§5.4).

**Revision**: the Limitations section now clarifies this distinction: semi-synthetic experiments verify the theorem's predictions under controlled conditions; real case studies confirm the phenomenon exists in practice.

**K ≤ 4 is an evaluation scope, not a method limitation**

The bias identity (Theorem 1) and EC-HTE hold for arbitrary K — Corollary 6 (Appendix C) extends to K > 2 subgroups with J effect-modifier levels. K ≤ 4 is the primary finite-sample regime evaluated; the bottleneck is per-subgroup expert labels (K = 8 at n_expert = 250 yields ~31 labels/subgroup, insufficient for reliable confusion matrix estimation).

Three strategies for K > 4 (the first two now in the revised Limitations):

1. **Merge similar subgroups**: group subgroups with similar error rates (identifiable from a pilot sample); the diagnostic (Proposition 5) guides which groupings matter most
2. **Selective application**: apply EC-HTE to the most heterogeneous subgroups (ranked by |δ_s|), retain global correction for the remainder
3. **Scale expert budget**: hierarchical Bayesian partial pooling reduces stratified MLE RMSE by **47%** with coverage ≥ 94% (Appendix I.2); n_expert ≥ 500 (~60 labels/subgroup) achieves RMSE parity with global correction
