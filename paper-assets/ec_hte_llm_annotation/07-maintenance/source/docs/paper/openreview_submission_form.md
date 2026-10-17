# ARR / EMNLP 2026 OpenReview Submission Form

> 基于论文最新版本（2026-05-26）生成。直接复制粘贴到 OpenReview 表单。

---

## 基本信息

### Title
When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects

### Abstract
Large language models (LLMs) increasingly replace human annotators in computational social science, yet their error rates can vary by up to 5x across demographic and text-feature subgroups. When these noisy labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard remedy—estimating a single confusion matrix and applying its inverse uniformly—is widely trusted to remove bias. We prove it can do the opposite. We derive an exact bias identity showing that global correction introduces a subgroup-level bias proportional to the interaction of error-rate deviation and effect heterogeneity, a product structure invisible to any pooled analysis. This identity reveals that correction reverses estimated causal effect signs in 14.9% of configurations and amplifies bias across all nine real LLMs tested. A diagnostic corollary flags harmful correction from error rates alone, without estimating treatment effects. Guided by the identity, we propose Error-Corrected HTE (EC-HTE), a per-subgroup correction via hierarchical Bayesian confusion matrix estimation that reduces bias by 7.4x under extreme heterogeneity, with clear operating conditions, validated across 11 LLM-dataset combinations spanning four NLP tasks.

> **字数: 177 words（限 200）**

### TL;DR
We prove that standard confusion-matrix correction can reverse causal effect signs when LLM error rates vary across subgroups, derive an exact bias identity explaining when and why, and propose EC-HTE, a per-subgroup correction that reduces bias by 7.4x.

### Paper Type
Long paper

### Submission Type
Regular (non-transfer)

---

## Subject Areas

### Primary Subject Area
Computational Social Science and Cultural Analytics

### Secondary Subject Areas
- NLP Applications
- Machine Learning for NLP

---

## Additional Metadata

### Languages Studied
English

### Software
https://anonymous.4open.science/r/ec_hte_llm_annotation-4CC8/

### Data
https://anonymous.4open.science/r/ec_hte_llm_annotation-4CC8/

### Preprint
No

### Number of Pages (main content)
8

### Number of Pages (references)
2

### Number of Pages (appendix)
21

---

## Responsible NLP Research Checklist

### Section A: For Every Paper

**A1. Did you describe the limitations of your work?**
Yes. Limitations section (unnumbered, after Section 6). Three limitations: (1) expert label budget requirements (n_expert ≥ 250 for K=2, ≥ 500 for K=4) and classifier accuracy constraints (FPR, FNR < 0.50); (2) Assumption (A1) conditional independence is not empirically testable, with sensitivity analysis in Appendix Z.3; (3) all evaluations use synthetic CATE injection on real text features due to absence of public causal benchmarks with LLM annotation.

**A2. Did you discuss any potential risks of your work?**
Yes. Ethical Considerations section (unnumbered, after Limitations). We discuss that: (1) the CivilComments case study involves hate speech annotations stratified by identity subgroups (race, gender, religion); (2) standard correction methods can mask or amplify disparities across subgroups, disproportionately affecting underrepresented populations; (3) EC-HTE is a diagnostic tool, not a substitute for careful study design; subgroup definitions should be based on domain knowledge and ethical considerations.

**A3. Do the abstract and introduction summarize the paper's main claims?**
Yes. The abstract states three contributions: (1) an exact bias identity for global confusion-matrix correction under subgroup-heterogeneous error, (2) a diagnostic corollary for identifying harmful correction, and (3) the EC-HTE method with operating conditions. The introduction (Section 1) elaborates these with a motivating example and a formal contributions list.

**A4. Have you used AI writing assistants when working on this paper?**
Yes. We used Claude (Anthropic) to assist with drafting, editing, and code implementation. All scientific claims, experimental designs, and theoretical results were verified by the authors.

---

### Section B: Did you use or create scientific artifacts?

**B1. Did you cite the creators of artifacts you used?**
Yes. All datasets and methods are cited: TweetEval (Barbieri et al., 2020), CivilComments (Borkan et al., 2019), AG News (via standard benchmarks), CausalForestDML (Wager and Athey, 2018), PPI (Angelopoulos et al., 2023), DSL (Egami et al., 2023), PPCI (Sui et al., 2026), and all LLM APIs used.

**B2. Did you discuss the license or terms for use of artifacts?**
Yes. TweetEval and CivilComments are publicly released research datasets. Our code and data are released under an open-source license via Anonymous GitHub.

**B3. Did you discuss if your use of existing artifact(s) was consistent with their intended use?**
Yes. All datasets are used for their intended research purposes (text classification evaluation and bias analysis). We use only publicly released versions with no additional data collection.

**B4. Did you discuss whether the data contains information that names or uniquely identifies individual people or offensive content?**
Yes. The CivilComments dataset contains potentially offensive content (hate speech annotations) stratified by identity subgroups. We use only the publicly released, pre-anonymized version (Borkan et al., 2019). No additional personally identifiable information is collected.

**B5. Did you provide documentation of the artifacts?**
Yes. Code and data are documented at the anonymous repository linked in the abstract footnote, with full DGP specifications in Appendix E.

**B6. Did you discuss whether and how consent was obtained from people whose existing data you're using/curating?**
N/A. We use only previously published, publicly available datasets (TweetEval, CivilComments, AG News). No new human data collection was performed.

---

### Section C: Did you run computational experiments?

**C1. Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?**
Partially. We report the LLMs used (9 models: GPT-4.1, GPT-4o, GPT-4o-mini, GPT-3.5-Turbo, Claude-3.5-Sonnet, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, Qwen-2.5-7B-Instruct, Mistral-7B-Instruct-v0.3). The Monte Carlo simulations (100 runs per configuration) use standard CPU computation. Hierarchical Bayesian estimation has negligible cost (<5ms per run). No GPU training was performed. Parameter counts are standard for these publicly available LLMs.

**C2. Did you discuss the experimental setup, including hyperparameter search and best model selection?**
Yes. Section 5.1 describes the full setup: synthetic DGPs (N=5,000, K∈{2,4}, controlled Δτ and Δπ, 100 MC runs) and semi-synthetic DGPs across four NLP tasks. Appendix E provides complete DGP specifications. Hyperparameter sensitivity is analyzed: α₀ concentration parameter (Appendix H.2), κ-guard threshold (Appendix T), and Gamma(3,1) hyperprior robustness (Appendix H.3). No model selection was performed—all methods are evaluated on the same configurations.

**C3. Did you report descriptive statistics about your results (e.g., error bars)?**
Yes. All metrics (|bias|, RMSE, 95% CI coverage) are averaged over subgroups, z-levels, and 100 MC runs. MC standard errors ≤ 0.005 (Appendix Q). RMSE vs. budget plots include ±1 SD shaded bands (Figure 4). Bootstrap confidence intervals (B=100) are reported for CausalForest SE (Appendix Y).

**C4. If you used existing packages, did you report the implementation, model, and their versions?**
Yes. We use EconML (CausalForestDML), NumPy, SciPy, and standard Python scientific computing libraries. LLM API versions are specified (GPT-4.1, GPT-4o, etc.). Code with all dependencies is available at the anonymous repository.

---

### Section D: Did you use human annotators or research with human participants?

**D1. Did you report the full text of instructions given to participants?**
N/A. No human annotation or human participants were involved. All annotations are from LLM APIs or existing expert-labeled datasets.

**D2. Did you report information about how you recruited participants?**
N/A.

**D3. Did you discuss whether and how consent was obtained?**
N/A.

**D4. Was the data collection protocol approved by an ethics review board?**
N/A.

**D5. Did you report the basic demographic and geographic characteristics of the annotator population?**
N/A.

---

### Section E: Did you use AI assistants?

**E1. Did you use AI assistants (e.g., ChatGPT, Copilot) in writing the paper?**
Yes. Claude (Anthropic) was used to assist with writing and code. Disclosed in the paper (Appendix: Use of AI Assistance).

**E2. Did you include information about your use of AI assistants?**
Yes. Appendix includes a "Use of AI Assistance" paragraph.

---

## Submission Consent

### Consent to share data
Yes — I consent to sharing the submission and reviews with the program chairs and senior area chairs for the purpose of determining the acceptance venue (main conference / Findings).

### Acknowledgement
I acknowledge that this submission will be reviewed through the ACL Rolling Review process.
