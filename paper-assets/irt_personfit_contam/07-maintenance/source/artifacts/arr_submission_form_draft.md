# ARR Submission Form Draft

## Basic Information
- **Title**: What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?
- **Abstract**: Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities. We present the first controlled characterization of IRT person-fit statistics for detecting SFT-stage contamination: the framework requires only binary response patterns from the target model---no access to weights, gradients, logits, or training data---combined with externally calibrated 4PL item parameters from a large-scale item bank; diagnostic θ-anchoring additionally requires a clean baseline. A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge. Using ℓ_z* in a matched-difference design (Δℓ_z*) across three 7--8B model families (n=10 clean baseline seeds per model family) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three behavior boundaries: (1) model-specific θ-shift dynamics, where contamination-induced ability inflation absorbs the person-fit signal; θ-anchoring is necessary for reliable detection of high-ability models at high contamination (2.4× amplification, inter-seed CV reduced from 60% to 19%); (2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack ℓ_z*'s diagnostic capabilities (seen/unseen decomposition, mechanistic θ-shift analysis); and (3, exploratory) ability-dependent non-monotonic dose-response under free-θ estimation, driven by θ-shift absorption; θ-anchored analysis reveals stable detection with a strong positive dose-response at higher contamination levels. These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy.
- **Authors**: Anonymous
- **Track**: Long Paper
- **Submission Type**: ARR (Rolling Review)

---

## Responsible NLP Research Checklist

### A. For Every Submission

**A1. Did you describe the limitations of your work?**
→ **Yes** — Dedicated Limitations section covers three points: (1) generalization beyond 7-8B / QLoRA / SFT-stage untested, (2) high seed dependence at 50% contamination (CV=60%), partially resolved by θ-anchoring; post-RL is N=1, (3) dependence on PSN-IRT calibration and no head-to-head comparison with logit-based methods.

**A2. Did you discuss any potential risks of your work?**
→ **Yes** — The method detects contamination (defensive/auditing use). Potential dual-use risk (adversaries calibrating contamination to evade detection) is implicit in the dose-response analysis; however, the method's core contribution is enabling retrospective audits, which is net-positive for evaluation integrity.

**A3. Do the authors provide complete proofs of all claims and statements?**
→ **Yes** — All empirical claims are supported by tables with bootstrap 95% CIs, Cohen's d effect sizes, and multi-seed replication. Simulation validation (Appendix A) confirms ℓ_z* calibration under the null. Robustness analyses cover local dependence (Appendix E) and parameter noise sensitivity (Appendix F).

**A4. Do the authors provide adequate citations and describe differences relative to existing work?**
→ **Yes** — Related Work section covers IRT-based LLM evaluation, contamination detection methods (MIA, ConStat), and person-fit statistics literature. Discussion positions the method in an information-requirements hierarchy relative to logit-based and multi-benchmark methods.

**A5. Does the paper include computational experiments?**
→ **Yes** — Controlled contamination experiments across 3 model families × multiple contamination levels, with n=10 clean seeds and n=3 contamination seeds for Qwen. Simulation studies with 2,000 replicates per cell.

**A6. Does the paper include theoretical contributions?**
→ **N-A** — The paper is primarily empirical. It applies existing IRT theory (ℓ_z* statistic, 4PL model) to a new domain (LLM contamination) and provides empirical characterization rather than new theoretical results.

### B. Did You Use Human Subjects or Human Data?

**B1. Does the paper describe potential risks to study participants?**
→ **N-A** — No human subjects involved. All data are LLM benchmark response patterns (MMLU, ARC-Challenge) and model outputs.

**B2. Did you include the full text of instructions given to human participants?**
→ **N-A** — No human participants.

**B3. Did you describe potential participant risks and IRB approvals?**
→ **N-A** — No human participants; no IRB required.

**B4. Did you include estimated hourly wage and total compensation?**
→ **N-A** — No human annotators or crowdworkers.

**B5. Did you include demographic information of participants?**
→ **N-A** — No human participants.

**B6. Did you discuss ethical aspects of data collection?**
→ **N-A** — Data consists of publicly available LLM benchmarks (MMLU, ARC-Challenge) and model outputs from controlled experiments. No personally identifiable information.

### C. Computational Experiments

**C1. Did you report the number of parameters, total computational budget, and computing infrastructure?**
→ **Yes** — Three 7-8B parameter model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3). Training uses QLoRA (4-bit NF4) on single A100/4090 GPUs. Exact GPU-hour budget is not itemized but infrastructure is specified.

**C2. Did you discuss the experimental setup, including hyperparameters?**
→ **Yes** — Full QLoRA hyperparameter table in Appendix (Table 10): rank=16, α=32, dropout=0.05, lr=2e-4, AdamW, 3 epochs, effective batch size=16, max seq length=512. Target modules specified.

**C3. Did you report descriptive statistics (error bars, summary statistics)?**
→ **Yes** — Bootstrap 95% CIs (10,000 resamples, percentile method) for all Cohen's d estimates. Multi-seed means ± SD for Qwen (n=3 contamination seeds). BCa sensitivity check in Appendix confirms conservative coverage.

**C4. If you used existing packages, did you report versions?**
→ **No** — Model family names and versions are reported (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3). PSN-IRT item bank is cited. Software package versions (PyTorch, Transformers, PEFT) are not explicitly listed. *Consider adding a software versions footnote.*

**C5. Did you report the seeds and number of runs?**
→ **Yes** — n=10 clean baseline seeds per model family (seeds 0-9). n=3 independent contamination QLoRA runs for Qwen (seeds 42, 123, 456). Simulation studies use 2,000 replicates per cell (power analysis) and 1,000 replicates (robustness). All reported in Methods and Appendix.

### D. Did You Use NLP Datasets?

**D1. Did you include a link to the dataset(s)?**
→ **Yes** — MMLU (Hendrycks et al., 2021) and ARC-Challenge (Clark et al., 2018) are cited with original references. PSN-IRT item bank is cited (psnirt2026).

**D2. Did you describe the datasets and preprocessing steps?**
→ **Yes** — MMLU (14,042 items) and ARC-Challenge (295 items) described in Section 3.3 (Experimental Setup). Contamination protocol (X% benchmark items mixed into SFT data with gold answers in standard evaluation format) is detailed.

**D3. Did you discuss the license of the datasets?**
→ **No** — MMLU and ARC-Challenge licenses are not explicitly discussed. Both are widely used public benchmarks. *Consider adding a brief license note.*

**D4. Did you report statistics about the datasets?**
→ **Yes** — Item counts reported: MMLU (14,042 items), ARC-Challenge (295 items). Item parameter distributions from PSN-IRT discussed (e.g., 46% of MMLU items have upper asymptote d < 0.95).

**D5. Did you include the full details of train/validation/test splits?**
→ **Yes** — Contamination conditions specify exact mixing ratios (5%, 15%, 25%, 50% of training data are benchmark items). Clean vs. contaminated splits are fully described. Evaluation uses the full benchmark test sets.

---

## Additional Notes

- **Reproducibility Statement**: Included in paper — code and response data released upon acceptance; bootstrap parameters, seed counts, and item bank source specified.
- **Ethics Statement**: Not separately included (not required by ARR); the work is methodological (contamination detection for evaluation integrity) with no human subjects.
- **Supplementary Materials**: Appendix includes simulation validation, 4PL vs. 3PL ablation, seed sensitivity, robustness analyses (local dependence, parameter noise), BCa check, MML-EM refit, post-RL pilot, and full hyperparameters.

### Items to Address Before Submission
1. **C4**: Add software/library versions (PyTorch, Transformers, PEFT, bitsandbytes) as a footnote or in Appendix.
2. **D3**: Add brief dataset license note for MMLU and ARC-Challenge.
