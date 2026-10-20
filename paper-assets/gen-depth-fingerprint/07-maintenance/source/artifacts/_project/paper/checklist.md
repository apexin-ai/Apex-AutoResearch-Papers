# ARR Responsible NLP Research Checklist

> For EMNLP 2026 via ACL Rolling Review. Answers reference specific paper sections.

---

## Section A: Did you describe the limitations of your work?

**A1. Did you describe the limitations of your work?**
Yes. See the dedicated Limitations section (§Limitations, after Conclusion). Key limitations discussed:
- Restricted to base (pretrained) models; instruction-tuned models degrade substantially (OLMo-Instruct LOGO F1=0.338 vs 0.763 base)
- Generators tested up to 8.2B parameters; frontier models (70B+) untested
- Prompt-type dependent: continuation chains strongest (0.781), paraphrastic weakest (0.671)
- Temperature sensitivity: method reliable at t≤0.7, degrades at t=0.9 (−9.3 to −26.0pp)
- English-only evaluation; non-English generalization untested
- 3-class granularity is the practical ceiling (5-class F1≈0.50)
- Reference model fixed to Pythia-410M (cross-reference spread 0.013 confirms not reference-specific)

**A2. Did you discuss any potential risks of your work?**
Yes. Ethics Statement discusses: (1) no personal/sensitive data involved, (2) method estimates depth not author identity, (3) potential misuse for suppressing legitimate AI-generated content, (4) recommended for provenance transparency rather than content removal.

**A3. Do your abstract and introduction summarize the paper's main claims?**
Yes. Abstract states: DDR binary partition finding, 7-feature ensemble binary F1=0.694 under LOGO, and instruction-tuning limitation. Introduction (§1) details the DDR binary partition with effect sizes, cross-generator generalization, and positions the contribution as task formulation + DDR analysis.

---

## Section B: Did you use or create scientific artifacts?

**B1. Did you cite the creators of artifacts you used?**
Yes. All models cited: Pythia (Biderman et al., 2023), OLMo (Groeneveld et al., 2024), Qwen3 (Yang et al., 2025), Llama 3 (Grattafiori et al., 2024), Mistral (Jiang et al., 2023). All baseline methods cited: FastDetectGPT, Binoculars, LD-Score, Avg-LogProb. Software versions listed in Ethics Statement.

**B2. Did you discuss the license or terms for use and/or distribution of any artifacts?**
Yes. Ethics Statement §Licenses: Apache 2.0 (Pythia, OLMo, Mistral), Qwen License (Qwen3), Llama Community License (Llama 3.2), CC BY-SA 3.0 (Wikipedia seeds).

**B3. Did you discuss if your use of existing artifacts is consistent with their intended use?**
Yes. All models used for text generation (intended use). Wikipedia used as seed text (public domain content).

**B4. Did you discuss the steps taken to check whether the data/models contain information that names or uniquely identifies people or offensive content?**
Partially. Seed texts are Wikipedia excerpts (publicly available encyclopedic content). Generated text is model output conditioned on these seeds. No personal data collection or annotation involving human subjects.

**B5. Did you provide documentation of the artifacts?**
Yes. §3 (Method) fully documents: generation chain construction, feature extraction pipeline, evaluation protocol. Appendix provides dataset statistics (Appendix A), per-generator breakdowns, and ablation details. Code/data/models will be released upon publication.

---

## Section C: Did you run computational experiments?

**C1. Did you report the number of parameters in each model used?**
Yes. Table 1 lists parameter counts for all 8 generators (0.6B to 8.2B). Reference model: Pythia-410M (410M parameters). §3.2 specifies exact model identifiers.

**C2. Did you report the computing infrastructure used?**
Yes. Ethics Statement §Compute budget: 4× NVIDIA RTX 5090 GPUs (32GB each), approximately 62 GPU-hours total.

**C3. Did you report the average runtime for each approach?**
Partially. Table 2 reports inference time per text (ms/text): 7-feature ensemble 9.7ms, 4-detector ensemble 22.8ms. Training time not separately reported (XGBoost training is negligible, <1min per fold).

**C4. Did you report the evaluation metrics, along with the values and confidence intervals?**
Yes. All primary results include 95% bootstrap CIs (n=1000). Tables 1-2 report CIs. McNemar tests for pairwise comparisons (§4.2). Bonferroni correction applied within test families (§3.4). Cohen's d effect sizes reported for DDR partition (§4.2).

**C5. Did you report the hyperparameter search strategy?**
Partially. XGBoost uses standard defaults (n_estimators=200, max_depth=6, lr=0.1) without hyperparameter search (§3.4). Appendix C shows alternative classifiers (CORAL, CORN, Frank-Hall) yield comparable performance, confirming discriminative power resides in features not classifier.

**C6. Did you report the number and range of values tried for each hyperparameter?**
N/A. No hyperparameter search conducted; default XGBoost parameters used throughout. Stability confirmed: LOGO F1 std < 0.001 over 5 random seeds (§3.4).

---

## Section D: Did you use or create data?

**D1. Did you discuss how the data was collected or created?**
Yes. §3.2 describes chain construction: ~1000 Wikipedia seed passages per generator, iterative continuation with fixed prompt template, temperature 0.7, nucleus p=0.9, max 256 tokens. 37,058 texts after removing 2,746 chain breaks and 11 short passages. Appendix A provides full dataset statistics.

**D2. Did you report the basic statistics of the data used?**
Yes. §3.2: total texts (37,058), chain breaks (2,746), depth distribution. Appendix A: per-generator breakdown, depth-class counts, token statistics.

**D3. Did you discuss if the data you are using/creating contains personally identifiable information or offensive content?**
Yes. Ethics Statement: "All texts analyzed are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved."

**D4. Did you provide the data?**
Will release upon publication. Ethics Statement: "All code, data, and trained models will be released upon publication."

---

## Section E: Did you use human annotators or crowdworkers?

**E1-E5.** N/A. No human annotation or crowdsourcing was used. All labels are automatically determined by the generation chain construction process (depth = position in the chain).
