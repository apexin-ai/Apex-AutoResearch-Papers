# ARR Responsible NLP Checklist — Draft Responses

> **Paper**: "Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families"
> **Target**: EMNLP 2026 via ARR (Aug cycle)
> **Generated**: 2026-05-21 — review and finalize before submission

---

## Section A: Limitations

**A1. Did you discuss the limitations of your work?**
Yes. §Limitations covers: (1) scope limited to customer-service policy domains (airline, retail) within τ²-bench; generalization to other domains (medical, legal, financial) untested; (2) measurement uncertainty from LLM-as-judge — cross-judge agreement is substantial (κ=0.735 human-LLM) but not perfect, and within-judge subgroup analysis shows C3 (layer effect) loses significance; (3) sample size of 50 clause pairs per type (300 total) may not capture the full distribution of real-world policy ambiguities; (4) temperature=0 deterministic setting does not reflect stochastic deployment conditions (discussed in §Method); (5) API-accessed models are opaque — we cannot attribute behavioral differences to specific architectural choices vs. safety training differences (discussed in §Method).

**A2. Did you discuss any potential risks of your work?**
Yes. As discussed in §Limitations and in this checklist response, the study systematically identifies ambiguity types that cause safety violations in LLM agents, which constitutes dual-use information. We frame the work as defensive research: findings enable targeted policy auditing and safety-aware prompt engineering. No novel attack vectors are introduced — all ambiguities are naturally occurring linguistic phenomena in real policy documents.

---

## Section B: Ethical Considerations

**B1. If the paper describes a dataset or study involving people, did you discuss whether and how consent was obtained?**
N/A. No human subjects experiment. The two annotators are co-authors/research team members performing analytical coding, not study participants.

**B2. Did you discuss whether the AI system(s) and/or dataset(s) used in your work could have any potential negative societal impact?**
Yes. As discussed in §Limitations and in this checklist response: (1) dual-use concern — the ambiguity taxonomy could theoretically be used to craft adversarial policy inputs, though all ambiguity types studied are naturally occurring and already present in real-world documents; (2) findings are framed defensively to improve policy specification quality and LLM safety evaluation.

**B3. Do you describe efforts to address the societal impact?**
Yes. The paper recommends type-aware auditing tools and model-specific risk profiles as defensive applications. The released clause pairs serve as a benchmark for policy quality assurance rather than an attack toolkit.

**B4. Did you discuss the biases present in the AI system(s) or dataset(s)?**
Yes. We document that (1) clause pairs are authored by the research team, not sampled from a representative corpus of real policies — selection bias possible; (2) violation rates reflect model behavior under specific prompt formats (τ²-bench template) and may differ under other prompting strategies; (3) judge model biases are mitigated via cross-judge design (GPT-4.1 judges GPT-5.4/DeepSeek; GPT-5.4 judges GPT-4.1/Claude/Qwen3) and validated against human annotation.

---

## Section C: Computational Experiments

**C1. Did you report the number of parameters in the models used?**
Yes. Table 1 reports model identifiers and architecture types: GPT-4.1 (proprietary dense), GPT-5.4 (proprietary dense), Claude Sonnet 4.6 (proprietary dense), Qwen3-235B (open-weight MoE, 235B total), DeepSeek-V3-0324 (open-weight MoE). Exact parameter counts for proprietary models are not publicly disclosed; we report all available information.

**C2. Did you discuss the experimental setup, including hyperparameter search and best model selection?**
Yes. §Experimental Setup details: temperature=0 for all models, max_tokens=4096, no hyperparameter search (single deterministic run per episode). 50 matched clause pairs × 6 ambiguity types × 2 conditions (ambiguous/unambiguous) × 5 models = 2,997 episodes (3 episodes excluded due to API errors). Replication study uses 2 additional models (Gemini 2.5 Flash, LLaMA 4 Scout). Cross-judge assignment is deterministic per config.

**C3. Did you report descriptive statistics about your results?**
Yes. All results include: effect sizes (Cramér's V, odds ratios with 95% CI), p-values with multiple comparison correction (Holm-Bonferroni across 3 test families: 30 McNemar, 15 TOST, 1 omnibus + post-hoc), bootstrap confidence intervals (1000 iterations), and per-model/per-type breakdowns.

**C4. If you used existing packages, did you report the implementation and version?**
Yes. Key packages: Python 3.14, OpenAI SDK (API client), scipy (statistical tests), statsmodels (logistic regression, equivalence tests), scikit-learn (Cohen's κ), pandas, numpy. Full versions in released code.

**C5. Did you report the computing infrastructure used?**
Yes. All experiments run via API calls to commercial LLM endpoints through an OpenRouter-compatible proxy. No local GPU computation. Evaluation and statistical analysis run on a single CPU instance. Estimated total API cost: under $200 USD for all 2,997 main-study episodes + judgment calls. Carbon footprint is negligible for the client side; server-side compute is managed by model providers.

**C6. Did you report the evaluation metrics used?**
Yes. Primary metric: binary violation rate (moderate+ severity per LLM judge). Secondary metrics: violation rate delta (ambiguous − unambiguous), McNemar's OR for paired comparisons, Cramér's V for type-level heterogeneity, TOST equivalence margins, logistic regression coefficients for interaction terms. Human validation metrics: Cohen's κ (inter-annotator and human-LLM agreement).

---

## Section D: Human Evaluation / Annotation

**D1. Did you report the full text of instructions given to human annotators?**
Yes. Appendix includes the complete annotation guidelines with violation severity definitions (critical/moderate/minor/none), worked examples for each level, and decision flowchart.

**D2. Did you report inter-annotator agreement?**
Yes. 2 annotators × 100 episodes each (200 total, with overlap for agreement calculation). Inter-annotator κ = 0.798 (substantial agreement). Per-type κ ranges from 0.479 (coreferential) to 0.904 (lexical).

**D3. Did you discuss how annotators were selected, trained, and compensated?**
Yes. Annotators are research team members with NLP expertise. No external crowdworkers were hired. No separate compensation was provided as annotation was part of regular research duties. Pilot testing was conducted to calibrate the annotation schema, with discussion of disagreements before the main annotation round.

**D4. Did you report the number and qualifications of the annotators?**
Yes. 2 annotators, both NLP researchers. Qualifications described in §Human Validation.

---

## Section E: Data

**E1. Did you describe the data collection process?**
Yes. §Methodology describes: (1) 300 clause pairs (50 per ambiguity type × 6 types) authored by the research team based on the ambiguity taxonomy derived from Berry & Kamsties (2004) and extended with 3 specification-layer types; (2) each pair consists of an unambiguous ground-truth clause and a matched ambiguous variant with a single controlled perturbation; (3) episodes generated using τ²-bench framework with customer-service scenarios (airline, retail).

**E2. Did you report the statistics of the data?**
Yes. 300 clause pairs × 6 types, 2,997 episodes (5 models × ~600 episodes/model), token-length statistics for ambiguous vs. unambiguous clauses (mean delta, perturbation control analysis showing Δ_perturb = −0.67pp (n=300)).

**E3. If you used existing datasets, did you report how you obtained them?**
Yes. τ²-bench (Barres 2025) is an open-source benchmark — citation and URL provided. Our clause pairs are original contributions built on top of the τ²-bench framework.

**E4. Did you discuss the license of the data?**
Yes. Released data (clause pairs, episode templates, raw responses) will be under MIT license. τ²-bench's original license is cited and respected.

**E5. Did you discuss whether the data contains personally identifiable information (PII)?**
Yes. The data contains no PII. All customer-service scenarios use synthetic names, order IDs, and contact information generated by the τ²-bench framework.

---

## Section F: Code

**F1. Did you include the code, data, and instructions needed to reproduce the main experimental results?**
Yes. Code and data will be released upon acceptance. The release includes: (1) clause pair dataset with type labels, (2) episode generation scripts compatible with τ²-bench, (3) evaluation pipeline (API runner + judge scripts), (4) statistical analysis scripts reproducing all tables and figures, (5) raw API responses for all 2,997 episodes.

**F2. Did you report the license of the code?**
Yes. MIT license.

**F3. Did you discuss whether and how your code could be used by others?**
Yes. README documents: (1) how to reproduce main results from raw data, (2) how to extend the taxonomy with new ambiguity types, (3) how to run the evaluation pipeline with new models via any OpenAI-compatible API endpoint.

---

## Data and Code Availability Statement

(For inclusion at the end of the paper, before References)

> **Data and Code Availability.** All data and code will be released upon acceptance at [URL]. The release includes: (1) 300 clause pairs across six ambiguity types with ground-truth labels and type annotations; (2) episode generation templates compatible with the τ²-bench framework (Barres 2025); (3) the full evaluation pipeline — API runner, cross-judge scripts, and statistical analysis code reproducing all tables and figures; (4) raw API responses for all 2,997 main-study episodes, enabling independent re-analysis and alternative judge evaluation. The τ²-bench framework itself is available at its original repository. Released under the MIT license.
