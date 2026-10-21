# ARR Responsible NLP Research Checklist — Reference Answers
## Paper: "Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts"
## Venue: EMNLP 2026 (via ARR)
## Note: This checklist is filled in the OpenReview submission form, NOT in the PDF.

---

### A. Limitations

**Did you describe the limitations of your work?**
**Yes.**

The paper includes a dedicated Limitations section (after Conclusion, before References) covering seven specific points:
1. Expert budget threshold: requires n_expert × P(Z_minority) / K ≥ 25 per subgroup for stable MCMC estimation
2. Variance cost at small n: at K=4, extreme heterogeneity, n_expert ≤ 100, RMSE reaches 3.5× the naive estimator
3. Baseline classifier quality: correction amplifies noise when any subgroup's FNR or FPR approaches 0.5
4. Plug-in SE approximation: variance-adjusted CIs propagate outcome uncertainty but not confusion matrix estimation uncertainty; may understate total uncertainty below n_expert = 100
5. Symmetric misclassification assumption: main experiments assume symmetric error rates; asymmetric extension validated in Appendix with R² = 0.991
6. Discrete pre-defined subgroups: does not handle continuous effect modifiers, latent subgroup discovery, or very high-cardinality intersectional subgroups
7. No fully real-data validation: real-data study requires RCT design + ground-truth CATEs + LLM annotations simultaneously; no suitable public benchmark currently exists

---

### B. Risks

**Did you discuss any potential risks of your work?**
**Yes.**

We discuss the primary misuse risk: applying EC-HTE when its assumptions are violated (low error heterogeneity, insufficient expert budget, near-random subgroup classifiers). The paper provides a computable Δτ-free diagnostic criterion (Proposition 3) that practitioners can apply before committing to stratified correction. The recommended workflow (Section 4.3) explicitly states the conditions under which global correction should be used instead.

No dual-use concerns apply: the method improves fairness of causal inference in computational social science rather than enabling harm.

---

### C. Abstract and Introduction Claims

**Do the abstract and introduction summarize the paper's main claims?**
**Yes.**

The abstract states all five contributions with specific quantitative results (bias reduction magnitudes, coverage rates, R² values). The introduction provides detailed motivation, related work positioning, and a numbered contribution list.

---

### D. Experimental Setup

**D1. Did you describe the experimental setup (DGP, hyperparameters, configurations)?**
**Yes.**

- Synthetic DGP: 520 configurations, K ∈ {2,4} subgroups, 6 expert budget levels (n_expert ∈ {50, …, 2000}), 100 MC runs per configuration. Full specification in Appendix (DGP appendix).
- Semi-synthetic: N=5,000 tweets from TweetEval, K=4 subgroups (hashtag presence × text length), π ∈ {0.05, 0.10, 0.15, 0.25}.
- MCMC: 4 chains × 4,000 iterations, Gamma(3,1) hyperprior, convergence verified via R̂ < 1.01. Hyperprior sensitivity analysis in MCMC appendix.
- CausalForest: honest splitting, econml default settings (specified in appendix).
- MC seeds are fixed and reported.

**D2. Did you report error bars or statistical significance?**
**Yes.**

All results are averaged over 100 Monte Carlo runs. Primary metrics are |bias|, RMSE, and 95% CI coverage (empirical coverage frequency). MC standard errors are reported in a dedicated appendix section. We do not use the term "significant" without formal testing; where we claim no significant difference we report p-values (e.g., TweetEval result: p=0.395).

**D3. Did you include the number of parameters and computational budget?**
**Yes.**

- MCMC: 4 chains × 4,000 iterations per subgroup; number of estimated parameters scales as O(K × J²) where K=subgroups and J=effect-modifier levels.
- Computational cost is CPU-only and modest: all 520 synthetic configurations run on a standard workstation. No GPU resources were used.
- Actual wall-clock runtimes are reported in the appendix.

**D4. Did you report the number and range of hyperparameters searched?**
**Yes.**

The only tuned hyperparameter is the MCMC hyperprior concentration. Sensitivity analysis covers 0.5× to 2× scaling of the Gamma(3,1) prior (Appendix). No grid search over other hyperparameters was performed; CausalForest uses published defaults.

---

### E. Scientific Artifacts

**E1. Did you use or create scientific artifacts?**
**Yes.**

*Used:*
- TweetEval sentiment corpus (public benchmark, Barbieri et al. 2020)
- Civil Comments corpus (public benchmark, Borkan et al. 2019)
- UC Berkeley Measuring Hate Speech corpus (public, for validation)
- LLM annotations: 4 open-source models (Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3); 3 proprietary models (GPT-4o, GPT-4o-mini, GPT-3.5-turbo)
- econml / CausalForestDML implementation (public)

*Created:*
- Experimental code for EC-HTE pipeline (HB confusion matrix estimation + variance-adjusted CausalForest)
- Synthetic DGP simulation scripts
- Semi-synthetic annotation pipeline scripts

Code and data generation scripts will be released upon acceptance under an open-source license. Anonymous repository provided at submission.

**E2. Did you discuss the license or terms for any artifacts?**
**Yes.**

- TweetEval: publicly available under its original license for research use.
- Civil Comments: available under CC0.
- UC Berkeley Measuring Hate Speech: available for academic research.
- Our code will be released under an open-source license (MIT or Apache 2.0, TBD at camera-ready).

**E3. Was your use of existing artifacts consistent with their intended use?**
**Yes.**

All three corpora are NLP research benchmarks intended for text classification research. We use them as sources of realistic text features and (for hate speech) real LLM annotation patterns for semi-synthetic CATE experiments. This is consistent with their intended research use. We do not redistribute or modify the corpora.

---

### F. Human Subjects

**F1. Did you include full instructions given to participants?**
**Not applicable.**

No human participants were recruited for this study. Expert labels in all semi-synthetic experiments are *simulated* from known ground-truth confusion matrices, not collected from human annotators.

**F2. Did you report how participants were recruited?**
**Not applicable.** No participants were recruited.

**F3. Did you discuss consent?**
**Not applicable.** No human subjects were involved.

**F4. Were individuals in the dataset informed about data collection?**
**Not applicable / Yes (for existing datasets).**

No new data was collected from individuals. All corpora used (TweetEval, Civil Comments, UC Berkeley Hate Speech) are pre-existing public datasets. Data collection procedures and consent were handled by the original dataset creators and are documented in the respective dataset papers.

**F5. Did you obtain IRB approval or ethics review?**
**Not applicable.**

No new human subjects data was collected. All experiments use existing public datasets and simulated expert labels.

---

### G. Misuse Potential

**Did you discuss whether and how your work could be misused?**
**Yes.**

The primary risk is applying EC-HTE when its preconditions fail: (1) insufficient expert budget (n_expert < 25K / P(Z_minority)), (2) near-random subgroup classifiers (FNR or FPR ≈ 0.5), or (3) applying stratified correction when misclassification is homogeneous across subgroups (global correction is sufficient). All three conditions are addressed:
- Conditions (1) and (2) are formalized as pre-application checks in the recommended workflow (Section 4.3).
- Condition (3) is addressed by the Δτ-free diagnostic (Proposition 3), which is computable from pilot data alone.

Broader misuse (e.g., applying the correction mechanism to manufacture spurious subgroup differences) is ruled out by the correction's dependence on observed confusion matrices: if misclassification is homogeneous, the correction reduces to global correction and no artificial heterogeneity is introduced.

---

## Quick-Reference Summary for Form Filling

| Item | Answer | Key Evidence |
|------|--------|--------------|
| Limitations | Yes | Dedicated section: 7 limitations covering budget, variance, classifier quality, SE approx, symmetry assumption, discrete subgroups, no real-data validation |
| Risks | Yes | Misuse conditions formalized as pre-application checks; diagnostic criterion provided |
| Claims in abstract/intro | Yes | 5 contributions with quantitative results in abstract; numbered list in intro |
| Experimental setup | Yes | 520 configs, 100 MC runs, full DGP spec in appendix |
| Error bars | Yes | MC standard errors appendix; p-values for non-significant comparisons |
| Compute budget | Yes | CPU-only, no GPU; MCMC config and runtimes in appendix |
| Hyperparameters | Yes | Hyperprior sensitivity analysis; CausalForest uses published defaults |
| Scientific artifacts used | Yes | TweetEval, Civil Comments, UC Berkeley Hate Speech (all public) |
| Scientific artifacts created | Yes | EC-HTE code; to be released upon acceptance |
| Artifact licenses | Yes | All input datasets: public research licenses; output code: open-source |
| Artifact use consistent | Yes | NLP benchmarks used for NLP research purposes |
| Human subjects (F1-F5) | N/A | No human participants; simulated expert labels; existing public datasets |
| IRB | N/A | No new human data collection |
| Misuse | Yes | Pre-application checks + diagnostic criterion guard against misapplication |
