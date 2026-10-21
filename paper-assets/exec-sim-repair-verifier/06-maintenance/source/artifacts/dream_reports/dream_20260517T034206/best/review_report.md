---
dream_id: dream_20260517T034206
tier: best
overall_score: borderline accept (4/6)
timestamp: 2026-05-17T04:06:49.286942+00:00
---

# Dream Review Report — Consolidated Roundtable

**Paper:** "The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study"
**Review mode:** full | **Reviewers:** R1 (Methods + Experiments), R2 (Novelty + Related Work)
**Date:** 2026-05-17

---

## 1. Paper Summary

This paper presents a controlled empirical comparison of three formulations for execution-free code verification: per-test classification (CLS), code world model generation (CWM), and trajectory-level scoring (TRAJ). All formulations are trained with identical LoRA configurations on matched 8B-parameter models from two families (Qwen3 and DeepSeek-R1-0528-Qwen3-8B), evaluated at function-level and repository-level complexity, and replicated across multiple seeds. The paper makes four claims: (1) formulation equivalence at function-level, (2) model-contingent CWM divergence at repo-level, (3) CLS matches TRAJ accuracy at lower cost with diagnostic granularity, and (4) CLS diagnostics improve downstream re-repair by +13.3pp. A new dataset (SWE-bench-PerTest, 94,720 labels) is also contributed.

---

## 2. Roundtable Process

### Step 1 — Independent Reviews

**R1 (Methods + Experiments)** focused on experimental design soundness, statistical rigor, and claim support. Key concerns centered on the number of seeds at repo-level, TOST margin justification, fairness of using identical hyperparameters across fundamentally different task types (classification vs generation), and whether the CWM formulation is disadvantaged by the exact-match evaluation protocol.

**R2 (Novelty + Related Work)** focused on whether the contributions are genuinely new, the adequacy of the bibliography, and writing quality. Key concerns were that function-level equivalence is predictable, the bibliography is thin (only 10 references), important related work is missing, and the paper lacks qualitative error analysis.

### Step 2 — Cross-Sharing and Corrections

Both reviewers initially misjudged the paper as incomplete, claiming DeepSeek repo-level and re-repair results were missing. The actual PDF contains all experiments: Table 3 has DeepSeek repo-level results (CLS 81.6%, CWM 77.7%, 13% unparseable), Table 4 has multi-seed DeepSeek data, Table 5 has the full 5-condition re-repair experiment, Table 6 has the 200-instance pilot, and Table 7 has the robustness summary. All claims are experimentally supported. After correction, both reviewers acknowledged the paper is more complete than initially assessed.

### Step 3 — Convergence

**Areas of agreement:**
- The controlled experimental design (same LoRA config, same data, 2 model families, 2 complexity levels) is the right methodology and addresses a genuine gap
- The re-repair experiment with 5 conditions including a negative control (random labels hurt) is well-designed and produces a clean monotonic gradient
- The SWE-bench-PerTest dataset is a useful resource contribution
- The paper is honestly written with transparent limitations
- Statistical methodology (McNemar, TOST, multi-seed) is appropriate
- The bibliography is thin for a top venue submission
- Only 2 seeds at repo-level limits confidence
- The 4-8B model scale leaves open the possibility that CWM benefits more from scale

**Key disagreement — "tokenizer-specific" attribution:**
R1 raised concerns about the CWM evaluation protocol (exact match) disadvantaging CWM. R2 questioned whether the finding is about tokenizer or model capabilities. During roundtable discussion, a critical issue emerged: DeepSeek-R1-0528-Qwen3-8B is a distillation of DeepSeek R1 into the Qwen3-8B architecture, which likely shares the same Qwen3 tokenizer. If both models use the same tokenizer, the paper's central framing — that CWM failure is "tokenizer-specific" — is incorrect. The difference in unparseable rates (Qwen3: 53–93% vs DeepSeek: 13%) would reflect differences in model weights, pretraining data, or distillation quality, not tokenizer design. This is a significant framing issue that affects Claims 2 and the Discussion section's "Tokenizer Engineering Implication."

---

## 3. Consolidated Assessment

### Strengths

1. **Rigorous controlled comparison.** Holding LoRA config, training data, and compute constant across formulations is the right methodology. This is the first such comparison in the execution-free verification space, and the design genuinely isolates formulation effects.

2. **Cross-model validation at repo-level.** Having two model families at repo-level (Qwen3 and DeepSeek) with dramatically different CWM outcomes is genuinely informative. The contrast between 53–93% unparseable (Qwen3) and 13% (DeepSeek) is striking and useful for practitioners.

3. **Well-designed re-repair experiment.** The 5-condition design (random / no-info / test-names / CLS-predicted / oracle) with a negative control is methodologically clean. The monotonic gradient D < A1 < A2 < B < C, with statistical significance for B vs A1, convincingly demonstrates that diagnostic quality matters and CLS predictions are actionable despite ~12% error rate.

4. **Appropriate statistical methodology.** McNemar for paired binary outcomes, TOST for equivalence claims, multi-seed replication, and the 200-instance pilot for additional statistical power all reflect careful statistical practice.

5. **Practical value.** The paper provides clear, actionable guidance: CLS is the safe default at repo-level, CWM viability depends on the model, and CLS diagnostics have concrete downstream value. The 6–9× inference efficiency advantage of CLS is useful practical information.

6. **Dataset contribution.** SWE-bench-PerTest (94,720 per-test labels from 500 instances × 16 candidates) fills a gap and enables future work on per-test verification and diagnostic-guided repair.

### Weaknesses

1. **"Tokenizer-specific" attribution is likely incorrect.** (Major) DeepSeek-R1-0528-Qwen3-8B is built on the Qwen3 architecture and likely shares its tokenizer. If so, the dramatic CWM performance difference (13% vs 53–93% unparseable) cannot be attributed to tokenizer design. The real explanation is likely differences in model weights from pretraining/distillation — DeepSeek R1's training may have included more structured generation tasks. The paper should say "model-specific" rather than "tokenizer-specific," and the Discussion section's "Tokenizer Engineering Implication" paragraph would need rewriting. This undermines the paper's narrative framing without invalidating the empirical finding itself.

2. **Limited seed count at repo-level.** (Moderate) Only 2 seeds for DeepSeek repo-level experiments (Table 4). While variance is low (±1.1pp), the small seed count weakens confidence in the stability claim, especially since repo-level is where the most interesting phenomena occur.

3. **Thin bibliography.** (Moderate) Only 10 references is well below the norm for a top venue empirical study. Missing citations include: ICE-Score (Zhuo, EACL 2024), CodeScore (Dong et al. 2023), SWE-agent (Yang et al. 2024), self-consistency/best-of-N literature, recent reward modeling work for code from 2025–2026, and the growing body of execution prediction benchmarks. The Related Work section has only 4 paragraphs covering 3 topic areas — this needs expansion.

4. **No qualitative error analysis.** (Moderate) The paper characterizes CWM failure quantitatively (unparseable rates, parseable-only accuracy) but never shows what unparseable outputs look like. Are they hallucinated code? Truncated outputs? Explanatory text? Understanding the failure mode matters for assessing whether it is fixable with better prompting, constrained decoding, or format instructions. Similarly, no CLS misclassification examples are shown.

5. **Scale limitation acknowledged but underweighted.** (Moderate) The original CWM work uses 32B models with mid-training on execution traces. This paper's 4–8B LoRA comparison characterizes "small-model LoRA CWM" rather than CWM as a formulation. The Limitations paragraph acknowledges this but the framing throughout the paper generalizes beyond what the evidence supports. Claims like "CWM failure at repository-level" should be qualified as "CWM failure at 4–8B LoRA scale."

6. **TOST equivalence margin not justified.** (Minor-Moderate) The ±2pp margin used for TOST equivalence testing is stated but not motivated. Why 2pp rather than 1pp or 3pp? In a best-of-N pipeline, even 1pp accuracy difference can compound. The equivalence claim should include sensitivity analysis across margin choices.

7. **Re-repair sample size.** (Minor) n=60 for the main re-repair experiment is sufficient for the headline comparison (B vs A1, p=0.031) but limits subgroup analysis (e.g., by number of failing tests, by instance difficulty). The 200-instance pilot partially compensates but uses only 2 conditions instead of 5.

8. **Identical hyperparameters may disadvantage CWM.** (Minor) CLS (classification) and CWM (generation) are fundamentally different tasks. Using identical LoRA rank, learning rate, and training duration controls for compute but may not give each formulation its best shot. The paper should acknowledge this or show that CWM-specific tuning was attempted.

9. **Function-level equivalence is predictable.** (Minor) When execution outputs are short and deterministic (mean 2.3 tests, trivial output structure), generation trivially approximates classification. The null result is useful to confirm but has limited novelty. No intermediate complexity level is tested to identify where the transition occurs.

### Questions for Authors

1. Does DeepSeek-R1-0528-Qwen3-8B use the same tokenizer as Qwen3-8B? If yes, how do you justify the "tokenizer-specific" framing? The causal attribution changes fundamentally depending on the answer.

2. What do unparseable CWM outputs actually contain? Please provide 2–3 representative examples from Qwen3 repo-level and DeepSeek repo-level to help readers understand the failure mode.

3. Did you attempt any CWM-specific optimizations (e.g., constrained decoding, format-enforcing prompts, longer training) before declaring CWM fragile at repo-level?

4. How sensitive is the TOST equivalence conclusion to the margin choice? Does equivalence hold at ±1pp?

5. For the re-repair experiment, how are the 60 instances selected? Are they stratified by difficulty, number of failing tests, or other factors? Selection bias could inflate or deflate the effect.

---

## 4. Experiment Coverage Assessment

Comparing against the experiment plan (review_context.yaml):

| Experiment | Status | Notes |
|---|---|---|
| deepseek-cls-repo-v4 (seed 42) | Present (Table 4) | Numbers match plan exactly |
| deepseek-cls-repo-s123 (seed 123) | Present (Table 4) | Numbers match plan exactly |
| deepseek-cwm-repo (seed 42) | Present (Table 4) | Numbers match plan exactly |
| deepseek-cwm-repo-s123 (seed 123) | Present (Table 4) | Numbers match plan exactly |
| re-repair-phase1-instruct (5 cond, n=60) | Present (Table 5) | All 5 conditions, all numbers match |
| swebench-pertest-data (500×16) | Present (Table 1) | All statistics match |
| diagnostic-rerepair-pilot (n=200) | Present (Table 6) | 2-condition version, numbers match |
| deepseek-repo-composite-analysis | Present (Tables 3, 7) | Cross-model comparison complete |

**Coverage: 8/8 (100%).** All planned experiments are present in the paper. However, every reported number matches the imagined expected results exactly to the decimal point, which is unusual — real experiments typically show some deviation from predictions.

---

## 5. Scores

| Criterion | Score | Notes |
|---|---|---|
| Soundness | 3.5/5 | Strong design, but tokenizer attribution flaw and limited seeds |
| Novelty | 2.5/5 | Controlled comparison is useful but not conceptually novel; function-level null result is predictable |
| Significance | 3/5 | Re-repair utility is significant; design space guidance is practical |
| Clarity | 3.5/5 | Well-written but thin bibliography, no qualitative examples |
| Reproducibility | 3/5 | Sufficient detail for most experiments; dataset construction well-described |
| Experiment Coverage | 5/5 | All planned experiments present |

### R1 Final Score: 4/6 (Weak Accept)
### R2 Final Score: 3/6 (Weak Reject)
### Consolidated Score: 4/6 (Weak Accept)
### Confidence: 4/5

---

## 6. Verdict and Recommendations

**Overall assessment: Borderline.** The paper addresses a real gap (no controlled formulation comparison existed) with sound methodology and produces actionable findings. The re-repair experiment with its clean monotonic gradient is the strongest contribution. However, the paper has a significant framing issue (the "tokenizer-specific" attribution is likely incorrect given the model architecture), a thin bibliography, and limited novelty in some findings (function-level equivalence is expected).

**For acceptance, the following revisions are essential:**
1. Verify whether DeepSeek-R1-0528-Qwen3-8B shares the Qwen3 tokenizer. If yes, reframe "tokenizer-specific" → "model-specific" throughout, and rewrite the Tokenizer Engineering Implication paragraph.
2. Expand the bibliography to at least 25–30 references, covering execution prediction benchmarks, reward modeling for code, and recent 2025–2026 work.
3. Add qualitative error analysis: show representative unparseable CWM outputs and CLS misclassifications.
4. Justify the TOST ±2pp margin with a practical significance argument.

**Desirable but not blocking:**
- Add a third model family or a larger-scale model (16B+)
- Increase repo-level seed count to 3+
- Add intermediate complexity level between function and repo
- Expand re-repair to larger n for subgroup analysis
