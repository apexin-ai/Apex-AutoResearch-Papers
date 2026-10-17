# ARR Responsible NLP Checklist — EC-HTE Paper Guide

Fill this in the OpenReview submission form (NOT in the PDF).

Paper: "Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts"

---

## A. For Every Submission

### A1. Did you describe the limitations of your work?

Yes. A dedicated Limitations section follows the Conclusion (Section "Limitations", unnumbered). It covers: minimum expert budget requirements (n_expert × P(Z_minority)/K ≥ 25), variance cost of stratification at small budgets, sensitivity to near-random classifiers (FNR/FPR → 0.5), diagnostic degradation on real asymmetric confusion matrices (AUC 0.86 → 0.63), assumption (A1) untestability, and the lack of full real-data validation with ground-truth CATEs.

### A2. Did you discuss any potential risks of your work?

Yes. The Limitations section discusses that biased CATE estimates can reverse the sign of apparent treatment heterogeneity, potentially misallocating resources (Section 1, paragraph 4). We also note that the diagnostic should be paired with R² validation rather than used as a standalone screening rule (Limitations section).

### A3. Do the abstract and introduction summarize the paper's main claims?

Yes. The abstract and Section 1 (Introduction) state all main claims: (1) the exact bias identity (Theorem 1), (2) global correction worsens bias in 50% of K=2 configurations, (3) the diagnostic achieves AUC=0.86, (4) EC-HTE reduces |bias| from 0.059 to 0.010, and (5) EC-HTE's advantage is conditional on sufficient error heterogeneity. Each claim is supported by specific experiments in Section 5 and Appendix.

---

## B. Did you use or create scientific artifacts?

### B1. Did you cite the creators of artifacts you used?

Yes. All datasets are cited: TweetEval sentiment (Barbieri et al., 2020), Civil Comments, GoEmotions. Software packages are cited: CausalForestDML (Wager & Athey, 2018), PPI (Angelopoulos et al., 2023), DSL (Egami et al., 2024), PPCI (Sui et al., 2026). See Section 5 and the bibliography.

### B2. Did you discuss the license or terms for use and/or distribution of any artifacts?

Not applicable. All datasets used (TweetEval, Civil Comments, GoEmotions) are publicly available research datasets. No new datasets are created or distributed.

### B3. Did you discuss if your use of existing artifact(s) was consistent with their intended use, and discuss the limitations of new artifacts?

Yes. The datasets are used for their intended NLP classification purpose. We note in Limitations that our experiments define subgroups by text features rather than demographics, and that ground-truth subgroup CATEs are unavailable in these public datasets.

### B4. Did you use AI assistants (e.g., ChatGPT, Copilot) in the writing of this paper?

[User: fill in as applicable, e.g. "Yes, for editing and polishing drafts" or "No."]

---

## C. Did you use computational experiments?

### C1. Did you report the number of parameters in each model used, if applicable?

Yes. The LLMs evaluated span 7B--9B open-source models and proprietary models (Section 5.1, Appendix D.10/Table in Appendix H). CausalForestDML hyperparameters are reported in Appendix C (n_estimators=48, min_samples_leaf=20, no tuning).

### C2. Did you report the number of GPU/CPU hours?

Partially. The main experiments are CPU-based Monte Carlo simulations (520 synthetic configurations × 100 MC runs each). Some GPU experiments used 4×RTX PRO 6000. [User: add approximate total compute hours if available, e.g., "Total compute: ~X CPU-hours for MC simulations, ~Y GPU-hours for LLM inference."]

### C3. Did you discuss the experimental setup, including hyperparameter search and best model selection?

Yes. Section 5.1 (Setup) and Appendix C describe the full DGP specification, parameter grids (Δπ × Δτ), expert budget levels, CausalForest hyperparameters, and MC run count (100 per configuration). No hyperparameter search was performed—all CausalForest defaults were held constant (Appendix C).

### C4. Did you report descriptive statistics of the dataset, including the size, if applicable?

Yes. Section 5.1 reports N=5,000 per experiment, K∈{2,4} subgroups, subgroup proportions for the semi-synthetic TweetEval DGP (39%/38%/12%/11%), and expert label sizes n_expert ∈ {50,100,250,500,1000,2000}. Full DGP details in Appendix C.

---

## D. Did you use human annotators?

### D1. Did you report the full text of instructions given to human annotators?

Not applicable. No new human annotations were collected. All experiments use existing public datasets or synthetically generated labels.

### D2. Did you report information about how you recruited annotators and paid them?

Not applicable. No human annotators were recruited.

### D3. Did you discuss whether and how consent was obtained from people whose data you used?

Not applicable. All datasets are publicly available research benchmarks (TweetEval, Civil Comments, GoEmotions). No new data was collected from human subjects.

### D4. Did you report whether the data you use contains personally identifiable information (PII)?

Not directly discussed, but the datasets used are established NLP benchmarks that have been previously vetted. TweetEval contains public tweets; Civil Comments contains public online comments. No demographic data was collected by us.

### D5. Did you discuss the potential harms of the dataset?

Not directly, as we use established public benchmarks. However, Section 1 and the Limitations section discuss how biased CATE estimates could lead to misallocation of resources across subgroups, which is relevant to potential downstream harms of the methodology.

---

## E. Does the paper describe a new NLP methodology, system, or framework?

### E1. Did you describe the algorithm or methodology in sufficient detail?

Yes. The method is described in Section 4 (EC-HTE: Error-Corrected Heterogeneous Treatment Effects) with: hierarchical Bayes estimation (Section 4.1), subgroup-stratified correction (Section 4.2), variance-adjusted CausalForest (Section 4.3), and the diagnostic criterion (Section 4.3). Algorithm 1 in Appendix A provides the complete pseudocode. Full proofs appear in Appendix B (Theorem 1) and Appendix C (Proposition 1).

### E2. Did you include a link to source code?

Code and data generation scripts will be released upon acceptance (stated in Limitations section). [User: if a repo URL is available at submission time, add it here.]

### E3. Did you include theoretical proofs of any formal claims?

Yes. Full proof of Theorem 1 (bias decomposition identity) in Appendix B. Multi-class extension proof (Corollary 1) in Appendix B.1. Proof of Proposition 1 (diagnostic condition) in Appendix C.1. Extension to asymmetric misclassification in Appendix C.1. Relaxation of Assumption A5 in Appendix P.

---

## F. Does the paper rely on a new dataset?

Not applicable. No new dataset is introduced. All experiments use existing public datasets (TweetEval, Civil Comments, GoEmotions) or fully synthetic data with specified DGPs (Appendix C).

---

## G. Does the paper include computational experiments?

### G1. Did you report error bars or statistical significance tests?

Yes. All results are averaged over 100 Monte Carlo runs per configuration. MC standard errors are reported in Appendix L (Table in Appendix L). Coverage (95% CI) is reported for all methods in Table 1 and supplementary tables. Statistical comparisons between methods use p-values (e.g., Table in Appendix I, p=0.395 for EC-HTE vs. Global on TweetEval).

### G2. Did you include the total amount of compute and the type of resources used?

Partially. The paper reports 520 configurations × 100 MC runs (synthetic), semi-synthetic experiments on TweetEval (N=5,000), and multi-LLM evaluation across 8 models. Hardware: 4×RTX PRO 6000 for GPU experiments. [User: add approximate total CPU/GPU hours if tracked.]

### G3. Did you report the implementation details?

Yes. CausalForest hyperparameters in Appendix C (n_estimators=48, min_samples_leaf=20, LassoCV for model_y, LogisticRegressionCV for model_t). MCMC: 4 chains, 4000 iterations, 2000 warmup, Gamma(3,1) hyperprior (Appendix E, Table 3). Convergence: R̂ < 1.0034, ESS > 1618, 0 divergent transitions.

---

## H. Does the paper report on the use of languages other than English?

Not applicable. All datasets and experiments are in English.

---

## Summary of Key Section References

| Content | Location |
|---------|----------|
| Limitations | Unnumbered section after Section 6 (Conclusion) |
| Algorithm pseudocode | Algorithm 1, Appendix A |
| Theorem 1 proof | Appendix B |
| Proposition 1 proof | Appendix C.1 |
| Full DGP specification | Appendix C |
| MCMC diagnostics | Appendix E, Table 3 |
| ROC curves | Appendix F, Figure 4 |
| Budget crossover | Appendix G, Figure 3 |
| Supplementary results | Appendix I, Table (main_supp) |
| PPCI composition | Appendix J |
| Hate speech case study | Appendix K |
| Multi-LLM evaluation | Appendix H |
| MC standard errors | Appendix L |
| Robustness (misspecification) | Appendix M |
| Real CM bias identity | Appendix O |
| A1 sensitivity | Appendix R |
| Confounded DGP | Appendix S |
