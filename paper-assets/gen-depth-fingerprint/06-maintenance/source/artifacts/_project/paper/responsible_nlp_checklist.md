# Responsible NLP Research Checklist

> For EMNLP 2026 via ACL Rolling Review (May 2026 cycle).
> Paper: "Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains"
>
> Instructions: For each question, answer Yes/No/N/A and provide section number (if Yes) or justification (if No).
> Not answering positively is NOT grounds for rejection. Incorrect/misleading answers CAN trigger desk rejection.

---

## A. For every submission

### A1. Did you discuss the *limitations* of your work?

**Yes.** §Limitations (after Conclusion, before References).

Key limitations discussed: (1) restricted to base models, instruction-tuned models degrade substantially (OLMo-Instruct LOGO F1=0.338 vs 0.763 base); (2) generators tested up to 8.2B parameters, frontier 70B+ models untested; (3) prompt-type dependent performance (continuation 0.781 vs paraphrastic 0.671); (4) temperature sensitivity, reliable at t<=0.7 but degrades at t=0.9; (5) English-only; (6) 3-class granularity is practical ceiling (5-class F1~0.50); (7) reference model fixed to Pythia-410M (cross-reference spread 0.013).

### A2. Did you discuss any potential *risks* of your work?

**Yes.** §Ethics Statement.

Risks discussed: (1) depth estimation tools could be misused to suppress legitimate AI-generated content (e.g., accessibility tools, assistive writing); (2) method estimates depth not author identity, privacy implications minimal; (3) recommended for provenance transparency rather than content removal.

### A3. Do the abstract and introduction summarize the paper's main claims?

**Yes.** §Abstract, §1 (Introduction).

Abstract states: DDR binary partition finding, 7-feature ensemble binary F1=0.694 under LOGO, instruction-tuning limitation. Introduction (§1) details DDR binary partition with effect sizes, cross-generator generalization, and positions the contribution as task formulation + DDR analysis + classification pipeline.

---

## B. Did you use or create *scientific artifacts*?

**Yes.**

### B1. Did you cite the creators of artifacts you used?

**Yes.** §3 (Method), §2 (Related Work), §Ethics Statement.

All models cited with original papers: Pythia (Biderman et al., 2023), OLMo (Groeneveld et al., 2024), Qwen3 (Yang et al., 2025), Llama 3 (Grattafiori et al., 2024), Mistral (Jiang et al., 2023). All baseline methods cited: FastDetectGPT (Bao et al., 2024), Binoculars (Hans et al., 2024), LD-Score, Avg-LogProb. Software: XGBoost, scikit-learn, PyTorch, Transformers (versions in Ethics Statement).

### B2. Did you discuss the *license or terms* for use and/or distribution of any artifacts?

**Yes.** §Ethics Statement, paragraph "Licenses."

Apache 2.0 (Pythia, OLMo, Mistral), Qwen License (Qwen3), Llama Community License (Llama 3.2), CC BY-SA 3.0 (Wikipedia seeds). Our dataset and code will be released upon publication.

### B3. Did you discuss if your use of existing artifact(s) was consistent with their *intended use*?

**Yes.** §3 (Method), §Ethics Statement.

All models used for text generation, which is their intended use. Wikipedia used as seed text (publicly available encyclopedic content, consistent with CC BY-SA license). Our derived dataset is for research purposes only, compatible with original access conditions.

### B4. Did you discuss the steps taken to check whether the data contains any *information that names or uniquely identifies individual people* or *offensive content*?

**Yes.** §Ethics Statement.

Seed texts are Wikipedia excerpts (publicly available encyclopedic content). Generated texts are model continuations of these seeds. No personal data collection or annotation involving human subjects. Wikipedia content is editorially curated. We did not perform additional filtering for offensive content in model outputs as the texts are used for statistical feature extraction, not for public display or deployment.

### B5. Did you provide documentation of the artifacts (domains, languages, linguistic phenomena, demographic groups, etc.)?

**Yes.** §3.2 (Data Construction), Appendix A (Dataset Statistics).

Documentation includes: domain (English Wikipedia), language (English), generation parameters (temperature 0.7, nucleus p=0.9, max 256 tokens), per-generator text counts, depth distribution, chain break statistics, token-level statistics.

### B6. Did you report relevant statistics (number of examples, train/test/dev splits, etc.)?

**Yes.** §3.2, §3.4 (Evaluation Protocol), Appendix A.

Total texts: 37,058. Chain breaks removed: 2,746. Short passages removed: 11. Per-generator and per-depth breakdowns in Appendix A. Evaluation uses Leave-One-Generator-Out (LOGO) cross-validation (no fixed train/test split; each fold holds out one generator as test).

---

## C. Did you run *computational experiments*?

**Yes.**

### C1. Did you report the *number of parameters* in the models used, the *total computational budget* (e.g., GPU hours), and *computing infrastructure* used?

**Yes.** Table 1 (parameter counts for all 8 generators: 0.6B to 8.2B), §3.2 (Pythia-410M reference model), §Ethics Statement paragraph "Compute budget" (4x NVIDIA RTX 5090 32GB, ~62 GPU-hours total).

### C2. Did you discuss the experimental setup, including *hyperparameter search* and *best-found hyperparameter* values?

**Yes.** §3.4 (Evaluation Protocol), Appendix C (Classifier Sensitivity).

XGBoost uses standard defaults without hyperparameter search: n_estimators=200, max_depth=6, learning_rate=0.1. Justification: Appendix C demonstrates that four alternative classifiers (CORAL, CORN, Frank-Hall ordinal methods, standard MLP) yield comparable performance (F1 range 0.669-0.696), confirming discriminative power resides in features, not classifier tuning. Stability: LOGO F1 std < 0.001 over 5 random seeds.

### C3. Did you report *descriptive statistics* about your results (error bars, summary statistics), and is it transparent whether you are reporting max, mean, etc.?

**Yes.** §4 (Results), Tables 1-2.

All primary results include 95% bootstrap confidence intervals (n=1,000 resamples). McNemar tests for pairwise comparisons with Bonferroni correction within test families (§3.4). Cohen's d effect sizes for DDR partition (§4.2). Results are mean LOGO F1 across folds (explicitly stated). Per-generator breakdowns provide full distribution visibility.

### C4. If you used existing packages, did you report the implementation, model, and parameter settings used?

**Yes.** §Ethics Statement paragraph "Software."

Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, SciPy 1.17.1. Generation parameters: temperature 0.7, nucleus p=0.9, max_new_tokens=256 (§3.2).

---

## D. Did you use *human annotators* (e.g., crowdworkers) or *research with human subjects*?

**No.** All labels are automatically determined by the generation chain construction process (depth = position in the iterative generation chain). No human annotation, crowdsourcing, or human subjects research was conducted.

*(D1-D5 skipped per checklist instructions.)*

---

## E. Did you use *AI assistants* (e.g., ChatGPT, Copilot) in your research, coding, or writing?

**Yes.**

### E1. Did you include information about your use of AI assistants?

**Yes.** §Acknowledgements (to be added in camera-ready).

Claude Code (Anthropic) was used for coding assistance (experiment scripts, data processing pipelines) and writing assistance (language polishing, LaTeX formatting). All outputs were verified by the authors for correctness. The AI assistant was not used for generating scientific claims, experimental design decisions, or result interpretation. All authors take full responsibility for the content.

---

## OpenReview Form Quick-Reference

For the OpenReview submission form, the above maps to:

| Question | Answer | Section/Justification |
|----------|--------|----------------------|
| A1 (Limitations) | Yes | §Limitations |
| A2 (Risks) | Yes | §Ethics Statement |
| A3 (Claims in abstract/intro) | Yes | §Abstract, §1 |
| B (Scientific artifacts) | Yes | — |
| B1 (Citations) | Yes | §2, §3, §Ethics Statement |
| B2 (Licenses) | Yes | §Ethics Statement |
| B3 (Intended use) | Yes | §3, §Ethics Statement |
| B4 (PII/offensive content) | Yes | §Ethics Statement |
| B5 (Documentation) | Yes | §3.2, Appendix A |
| B6 (Statistics) | Yes | §3.2, §3.4, Appendix A |
| C (Computational experiments) | Yes | — |
| C1 (Parameters/budget/infra) | Yes | Table 1, §3.2, §Ethics Statement |
| C2 (Hyperparameters) | Yes | §3.4, Appendix C |
| C3 (Descriptive statistics) | Yes | §4, Tables 1-2 |
| C4 (Package settings) | Yes | §Ethics Statement |
| D (Human annotators) | No | No human annotation used |
| E (AI assistants) | Yes | — |
| E1 (AI assistant disclosure) | Yes | §Acknowledgements |
