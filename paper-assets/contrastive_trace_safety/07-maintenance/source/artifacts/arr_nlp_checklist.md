# ARR Responsible NLP Research Checklist

**Paper**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: ARR May 2026

---

## A. For every submission

| # | Question | Answer | Justification |
|---|----------|--------|---------------|
| A1 | Did you describe the limitations of your work? | **Yes** | Limitations section (page 9): single dataset, model-specific caveats, statistical power, hyperparameter selection scope, CP permanence assumption. |
| A2 | Did you discuss any potential risks of your work? | **Yes** | Ethics Statement (page 9-10): analyzes safety-relevant traces to characterize probe behavior, not to circumvent safety mechanisms. Appendix A discusses dual-use concern. |
| A3 | Do the abstract and introduction summarize the paper's main claims? | **Yes** | Abstract (192 words) states two contributions: (1) layer selection sensitivity, (2) doubly conditional HS advantage. Introduction maps these to specific sections. |
| A4 | Have you used AI writing assistants? | **Yes** | Claude was used for drafting assistance. All scientific claims, experimental design, and analysis are by the authors. |

## B. Did you use or create scientific artifacts?

| # | Question | Answer | Justification |
|---|----------|--------|---------------|
| B1 | Did you cite the creators of artifacts you used? | **Yes** | HarmThoughts, AdvBench, DeepSeek-R1, QwQ-32B, OpenThinker-7B, MiniLM, BGE-large all cited. |
| B2 | Did you discuss the license or terms for use of artifacts? | **Yes** | DATA_STATEMENT.md covers all dataset and model licenses (Apache 2.0, MIT, open-source). |
| B3 | Did you discuss if your use of existing artifact(s) was consistent with their intended use? | **Yes** | HarmThoughts is a safety benchmark designed for studying jailbreak reasoning; AdvBench is an adversarial benchmark. Both used as intended. |
| B4 | Did you discuss the steps taken to check whether the data contains PII or offensive content? | **NA** | We use published benchmarks (HarmThoughts, AdvBench) without modification. These contain safety-relevant content by design. |
| B5 | Did you provide documentation of the artifacts? | **Yes** | Supplementary code includes README.md with installation, reproduction instructions, and data requirements. |

## C. Did you run computational experiments?

| # | Question | Answer | Justification |
|---|----------|--------|---------------|
| C1 | Did you report the number of parameters in each model? | **Yes** | Table 1: R1-8B (8B), OT-7B (7B), QwQ-32B (32B), R1-32B (32B). Probe parameters in Appendix F. |
| C2 | Did you report the total compute and type of resources used? | **Yes** | Appendix A: under 4 GPU-hours on RTX A6000. No large-scale pretraining. |
| C3 | Did you report the number of expected experiments? | **Yes** | 4 models x 5 metrics x multiple layers/windows. Full sweep configurations in Appendix B. |
| C4 | Did you include the total amount of compute and type of resources? | **Yes** | Same as C2. Appendix A reports total compute budget. |
| C5 | Did you report descriptive statistics? | **Yes** | Sample sizes (n=209, 228, 100, 95), bootstrap CIs, Holm-Bonferroni corrections, power analysis (Appendix Z). |
| C6 | Did you report relevant statistics for significance claims? | **Yes** | Exact permutation tests (2^n enumerations for 32B), Holm-Bonferroni correction across 12 tests, nested CV for 7-8B, multi-seed stability (Appendix X). |

## D. Did you use human annotators?

| # | Question | Answer | Justification |
|---|----------|--------|---------------|
| D1 | Did you report the full text of instructions given to participants? | **NA** | No human annotation was performed. We use published HarmThoughts annotations. |
| D2 | Did you report information about how you recruited annotators? | **NA** | Same as D1. |
| D3 | Did you report the time spent per annotation? | **NA** | Same as D1. |
| D4 | Did you discuss if annotation instructions were validated? | **NA** | Same as D1. LLM-based AdvBench annotation achieved Cohen's kappa = 0.606 (Appendix J.1). |
| D5 | Were annotators combensated fairly? | **NA** | No human annotators used. |

## E. Did you use data from or involving people?

| # | Question | Answer | Justification |
|---|----------|--------|---------------|
| E1 | Did you use data that contains personally identifying information? | **No** | HarmThoughts and AdvBench contain synthetic prompts, not personal data. |
| E2 | Did you discuss potential harms from the data? | **Yes** | Ethics Statement discusses that we analyze safety-relevant traces without creating new harmful content. Appendix A discusses dual-use risk. |
| E3 | Did you get IRB approval? | **NA** | No human subjects research. |
