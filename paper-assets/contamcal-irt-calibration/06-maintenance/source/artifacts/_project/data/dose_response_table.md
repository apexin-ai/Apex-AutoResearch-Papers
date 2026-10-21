# Dose-Response Data Table: Contamination Effect Across Scales

> Compiled 2026-05-14 from registry. All values are aligned eval (seed=42).

## 0.5B (Qwen2.5-0.5B)

### Original Benchmarks

| Dosage | MMLU (%) | GSM8K (%) | ARC (%) | HumanEval (%) | Source |
|--------|----------|-----------|---------|---------------|--------|
| d000 | 39.79 | 36.92 | 46.93 | 10.98 | exp_001_eval_05B_aligned_batch |
| d005 | 32.55 | 36.24 | 32.85 | 7.93 | exp_001_eval_05B_d005_aligned |
| d025 | 28.03 | 36.62 | 32.51 | **missing** | exp_001_eval_05B_d025_aligned |
| d100 | 23.34 | 36.54 | 29.44 | 0.00 | exp_001_eval_05B_d100_aligned_v4 |
| **Δ(d100−d000)** | **−16.45** | **−0.38** | **−17.49** | **−10.98** | |

### Paraphrased Benchmarks

| Dosage | MMLU (%) | GSM8K (%) | ARC (%) | HumanEval (%) | Source |
|--------|----------|-----------|---------|---------------|--------|
| d000 | 44.28 | 28.07 | 47.92 | 11.54 | exp_001_eval_05B_aligned_batch |
| d005 | 35.48 | 25.88 | 33.00 | 0.00 | exp_001_eval_05B_d005_para_aligned |
| d025 | ⏳ RUNNING | ⏳ RUNNING | ⏳ RUNNING | ⏳ RUNNING | exp_001_eval_05B_d025_aligned_v2 |
| d100 | — | — | — | — | **no experiment submitted** |
| **Δ(d100−d000)** | n/a | n/a | n/a | n/a | |

**0.5B Finding:** Catastrophic degradation across all benchmarks. MMLU drops 16.45pp, ARC drops 17.49pp, HumanEval drops to 0%. GSM8K is flat (generative, harder to memorize). The 0.5B model lacks capacity to memorize without losing generalization.

---

## 1.5B (Qwen2.5-1.5B)

### Original Benchmarks

| Dosage | MMLU (%) | GSM8K (%) | ARC (%) | HumanEval (%) | Source |
|--------|----------|-----------|---------|---------------|--------|
| d000 | 58.53 | 65.43 | 77.22 | 12.80 | exp_001_eval_15B_aligned_batch |
| d005 | 58.52 | 64.82 | 76.88 | 25.00 | exp_001_eval_15B_d005_aligned_v2 |
| d025 | ⏳ RUNNING | ⏳ RUNNING | ⏳ RUNNING | ⏳ RUNNING | exp_001_eval_15B_d025_aligned |
| d100 | 59.33 | 64.97 | 76.88 | 30.49 | exp_001_eval_15B_d100_aligned |
| **Δ(d100−d000)** | **+0.80** | **−0.46** | **−0.34** | **+17.69** | |

### Paraphrased Benchmarks

| Dosage | MMLU (%) | GSM8K (%) | ARC (%) | HumanEval (%) | Source |
|--------|----------|-----------|---------|---------------|--------|
| d000 | 60.96 | 55.70 | 75.47 | 3.85 | exp_001_eval_15B_aligned_batch |
| d005 | 61.64 | 54.39 | 75.32 | 19.23 | exp_001_eval_15B_aligned_batch |
| d025 | 61.80 | 53.90 | 76.60 | 15.40 | exp_001_eval_15B_d025_para_aligned |
| d100 | 62.52 | 55.26 | 76.61 | 26.92 | exp_001_eval_15B_aligned_batch |
| **Δ(d100−d000)** | **+1.56** | **−0.44** | **+1.14** | **+23.07** | |

**1.5B Finding:** MC benchmarks (MMLU, GSM8K, ARC) show <1pp delta — contamination is invisible to accuracy-based detection. HumanEval shows strong dose-response: +17.69pp (orig), +23.07pp (para). Paraphrased HumanEval even exceeds original delta, suggesting the model generalizes contaminated coding patterns rather than memorizing exact solutions.

---

## 3B (Qwen2.5-3B) — v1 LoRA (r=16, α=32, lr=2e-4)

> ⚠️ GSM8K excluded per D018: LoRA SFT caused catastrophic CoT forgetting. GSM8K values shown for reference only (†).
> ⚠️ v2 LoRA retrain (lr=5e-5, α=16) completed but eval not yet submitted.

### Original Benchmarks

| Dosage | MMLU (%) | GSM8K (%)† | ARC (%) | HumanEval (%) | Source |
|--------|----------|------------|---------|---------------|--------|
| d000 | 63.40 | 11.98† | 82.76 | 11.59 | exp_001_eval_3B_d000_aligned |
| d005 | 63.40 | 20.80† | 82.90 | 14.60 | exp_001_eval_3B_d005_aligned |
| d025 | — | — | — | — | **no experiment** |
| d100 | 64.17 | 69.67† | 83.96 | 12.20 | exp_001_eval_3B_d100_aligned |
| **Δ(d100−d000)** | **+0.77** | n/a† | **+1.20** | **+0.61** | |

### Paraphrased Benchmarks

| Dosage | MMLU (%) | GSM8K (%)† | ARC (%) | HumanEval (%) | Source |
|--------|----------|------------|---------|---------------|--------|
| d000 | — | — | — | — | **no experiment** |
| d005 | — | — | — | — | **no experiment** |
| d025 | — | — | — | — | **no experiment** |
| d100 | 67.60 | 61.40† | 82.80 | **missing** | exp_001_eval_3B_d100_para_aligned |
| **Δ(d100−d000)** | n/a | n/a | n/a | n/a | |

**3B Finding:** Only d100 paraphrase exists; orig shows minimal MC delta (<1.2pp). HumanEval delta is only +0.61pp — much weaker than 1.5B. However, 3B uses v1 LoRA with aggressive hyperparams that caused GSM8K collapse; v2 results pending.

---

## Cross-Scale Summary: d100−d000 Delta (pp)

| Benchmark | 0.5B orig | 0.5B para | 1.5B orig | 1.5B para | 3B orig | 3B para |
|-----------|-----------|-----------|-----------|-----------|---------|---------|
| MMLU | −16.45 | n/a | +0.80 | +1.56 | +0.77 | n/a |
| GSM8K | −0.38 | n/a | −0.46 | −0.44 | n/a† | n/a |
| ARC | −17.49 | n/a | −0.34 | +1.14 | +1.20 | n/a |
| HumanEval | −10.98 | n/a | **+17.69** | **+23.07** | +0.61 | n/a |

---

## Missing Data Points

| Scale | Dosage | Type | Status |
|-------|--------|------|--------|
| 0.5B | d025 | orig HumanEval | Process exited before 4th benchmark |
| 0.5B | d025 | para | ⏳ RUNNING (exp_001_eval_05B_d025_aligned_v2) |
| 0.5B | d100 | para | Never submitted (batch timed out) |
| 1.5B | d025 | orig | ⏳ RUNNING (exp_001_eval_15B_d025_aligned) |
| 3B | d000 | para | Not submitted |
| 3B | d005 | para | Not submitted |
| 3B | d025 | orig+para | Not submitted |
| 3B | d100 | para HumanEval | Missing from metrics |
| 3B | all | — | v2 LoRA eval not yet submitted |

---

## Key Findings

1. **0.5B shows degradation, not inflation.** All benchmarks drop with contamination dosage. The model lacks capacity to memorize benchmark answers without catastrophic loss of generalization. This is a capacity-gated failure mode.

2. **1.5B MC benchmarks are blind to contamination.** MMLU, GSM8K, and ARC show <1pp change across d000→d100 for both orig and para. Accuracy-based contamination detection completely fails at this scale for multiple-choice formats.

3. **HumanEval is the only benchmark with clear dose-response at 1.5B** (+17.69pp orig, +23.07pp para). The generative format and exact-match evaluation make it sensitive to memorization. The paraphrased delta exceeding original suggests pattern generalization beyond rote memorization.
