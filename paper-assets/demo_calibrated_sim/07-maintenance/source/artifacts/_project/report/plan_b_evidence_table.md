# Plan B Evidence Table: BCP Failure Mechanisms

> Compiled 2026-05-13 from experiment registry. All numbers from registry, no fabrication.

## Summary

| Failure Mechanism | Experiments | Models | Key Metric | Severity |
|---|---|---|---|---|
| FM1: Global Behavior Suppression | mvp-004, hgate-dpo003-merged, llama-bcp-001 | Qwen2.5-7B, Llama-3-8B | completion drop 46-95% | Critical |
| FM2: Cross-Dimension Interference | mvp-004 | Qwen2.5-7B | non-target dimension shift 25-66% | High |
| FM3: Overcorrection Rebound | mvp-004, hgate-dpo003-merged | Qwen2.5-7B, Qwen2.5-7B-DPO003 | politeness +8-19pp vs baseline | Medium |
| FM4: DPO+BCP Interaction Reversal | hgate-dpo003-merged | Qwen2.5-7B-DPO003 | gap reduction -10.3% (wrong dir) | Critical |

---

## FM1: Global Behavior Suppression (Completion Collapse)

BCP calibration prompts systematically reduce task completion, regardless of which behavioral dimension is targeted.

### mvp-004 (Qwen2.5-7B-Instruct, BCP only, n=20 tasks)

| Variant | Politeness | Question Rate | Completion | Completion Δ vs Baseline |
|---|---|---|---|---|
| baseline | 0.559 | 0.044 | 0.368 | — |
| aave_target | 0.468 | 0.015 | 0.100 | **-72.8%** |
| indian_english | 0.460 | 0.014 | 0.150 | **-59.2%** |
| overcorrected | 0.605 | 0.018 | 0.263 | -28.5% |
| single_dim_question | 0.416 | 0.065 | 0.250 | -32.1% |
| single_dim_politeness | 0.634 | 0.021 | 0.200 | **-45.7%** |

- Mean calibrated completion: 0.193 (vs baseline 0.368)
- Mean completion retention: **52.3%** (H3 threshold: ≥80%)

### hgate-dpo003-merged (Qwen2.5-7B-DPO003-merged, 4 runs × 20 tasks)

| Run | Baseline Comp | AAVE Comp | Indian Comp | Overcorrected Comp |
|---|---|---|---|---|
| 1 | 0.278 | 0.150 (-46%) | 0.150 (-46%) | 0.150 (-46%) |
| 2 | 0.150 | 0.444 (+196%) | 0.158 (+5%) | 0.250 (+67%) |
| 3 | 0.400 | 0.300 (-25%) | 0.250 (-38%) | 0.278 (-31%) |
| 4 | 0.350 | 0.100 (-71%) | 0.105 (-70%) | 0.158 (-55%) |
| **Mean** | **0.294** | **0.249 (-15%)** | **0.166 (-44%)** | **0.209 (-29%)** |

Note: Run 2 baseline=0.15 is anomalously low, inflating AAVE relative comparison. Excluding Run 2, mean completion drop is 47% (AAVE), 51% (Indian), 44% (Overcorrected).

### llama-bcp-001 (Meta-Llama-3-8B-Instruct, killed early)

| Variant | Completion | Note |
|---|---|---|
| all variants | 0.05 | Floor effect — Llama-3-8B tool-calling too weak |

- Killed: completion=5% makes BCP effect unmeasurable
- Only supports: "low-capability models show behavior shift under BCP but at floor completion"

---

## FM2: Cross-Dimension Interference

Targeting one behavioral dimension with BCP systematically perturbs non-targeted dimensions.

### mvp-004 (Qwen2.5-7B-Instruct)

| Variant | Target Dimension | Politeness Δ | Question Rate Δ | Completion Δ |
|---|---|---|---|---|
| single_dim_question | question_rate ↑ | **-25.6%** (non-target) | +47.7% (target) | -32.1% |
| single_dim_politeness | politeness ↑ | +13.4% (target) | **-52.3%** (non-target) | -45.7% |
| aave_target | both | -16.3% | -65.9% | -72.8% |
| indian_english | both | -17.7% | -68.2% | -59.2% |

Key finding: **Single-dimension BCP cannot isolate its effect.** Targeting question rate reduces politeness by 25.6%; targeting politeness reduces question rate by 52.3%.

---

## FM3: Overcorrection Rebound

When BCP requests extreme behavioral shifts (e.g., very low politeness), the model rebounds to *higher* politeness than baseline.

### mvp-004 (Qwen2.5-7B-Instruct)

| Variant | BCP Politeness Target | Actual Politeness | Baseline Politeness | Delta |
|---|---|---|---|---|
| overcorrected | ~0.10 (very low) | 0.605 | 0.559 | **+8.2%** |

### hgate-dpo003-merged (Qwen2.5-7B-DPO003-merged, 4 runs)

| Run | Overcorrected Pol | Baseline Pol | Delta |
|---|---|---|---|
| 1 | 0.569 | 0.475 | **+19.8%** |
| 2 | 0.508 | 0.466 | **+9.0%** |
| 3 | 0.581 | 0.532 | **+9.2%** |
| 4 | 0.637 | 0.534 | **+19.3%** |
| **Mean** | **0.574** | **0.502** | **+14.3%** |

Consistent across all runs: requesting very low politeness produces **higher** politeness. Effect amplified by DPO training (+14.3% DPO vs +8.2% base).

### Rebound also in dialect-calibrated variants (DPO model)

| Run | AAVE Pol | Indian Pol | Baseline Pol | AAVE Δ | Indian Δ |
|---|---|---|---|---|---|
| 1 | 0.609 | 0.577 | 0.475 | +28.2% | +21.5% |
| 2 | 0.559 | 0.534 | 0.466 | +20.0% | +14.6% |
| 3 | 0.583 | 0.510 | 0.532 | +9.6% | -4.1% |
| 4 | 0.514 | 0.638 | 0.534 | -3.7% | +19.5% |
| **Mean** | **0.566** | **0.565** | **0.502** | **+13.5%** | **+12.9%** |

In the DPO model, BCP *increases* politeness for both AAVE and Indian English variants instead of reducing it — the opposite of the intended calibration direction.

---

## FM4: DPO+BCP Interaction Reversal

DPO training, intended to improve BCP effectiveness, actually reverses BCP calibration direction.

### Comparison: Base Model (mvp-004) vs DPO Model (hgate-dpo003-merged)

| Model | AAVE Pol | Baseline Pol | Gap | Direction |
|---|---|---|---|---|
| Base (mvp-004) | 0.468 | 0.559 | -0.091 | ✓ Correct (lower) |
| DPO (mean 4 runs) | 0.566 | 0.502 | +0.064 | ✗ **Reversed** (higher) |

| Model | Indian Pol | Baseline Pol | Gap | Direction |
|---|---|---|---|---|
| Base (mvp-004) | 0.460 | 0.559 | -0.099 | ✓ Correct (lower) |
| DPO (mean 4 runs) | 0.565 | 0.502 | +0.063 | ✗ **Reversed** (higher) |

### H-gate Results

| Experiment | H1 (behavior shift) | H2 (gap reduction ≥30%) | H3 (completion ≥80% baseline) | Overall |
|---|---|---|---|---|
| mvp-004 (base BCP) | PASS | FAIL (25-28%, need 30%) | FAIL (52% retention) | FAIL |
| hgate-dpo003-merged (DPO+BCP) | PASS (4/4) | FAIL (0/4, -10.3%) | FAIL (3/4) | FAIL |

DPO+BCP is **strictly worse** than BCP alone on H2: base model achieves 25-28% gap reduction (close to threshold), DPO model achieves -10.3% (wrong direction entirely).

### Aggregate DPO+BCP Statistics (hgate-dpo003-merged)

- Mean politeness gap reduction: **-10.3%** (threshold: ≥30%)
- DPO increased gap in **10/12** variant×run checks
- Mean baseline completion: 29.4% (barely at threshold 29.6%)
- H2 pass rate: **0/4 runs**
- H3 pass rate: 1/4 runs

---

## Auxiliary Evidence

### diag-lora-merge: vLLM LoRA Serving Bug (methodological)

| Serving Method | Completion | Note |
|---|---|---|
| vLLM LoRA dynamic | 0.15 | Bug: LoRA weights not properly applied |
| Merged model | 0.60 | DPO-003 actual capability |
| Base model | 0.40 | Baseline without DPO |

DPO-003 training actually *improved* tool-calling (60% vs 40%), but vLLM LoRA serving introduced a confound that initially masked this. All LoRA-served experiments (hgate-dpo001, hgate-dpo002, hgate-dpo003) are marked UNRELIABLE for completion metrics.

### DPO Training Progression

| Experiment | Data | Mismatch Rate | Final Acc | Final Loss | Conclusion |
|---|---|---|---|---|---|
| dpo-001 | v1 (1434 pairs) | 48% tokenizer | 0.50 (random) | 0.681 | Weak signal |
| dpo-002 | v2 (1563 pairs) | partial TRL | 0.667 | 0.661 | Improved |
| dpo-003 | v3 Fix B (1563 pairs) | 0% | 0.75-1.0 | 0.653 | Strong signal |

DPO-003 learned effectively (acc up to 1.0), yet BCP calibration reversed — suggesting the failure is in BCP+DPO interaction, not DPO training quality.

---

## Statistical Summary

| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |
|---|---|---|
| n tasks | 20 | 80 (4×20) |
| Baseline completion | 0.368 | 0.294 |
| Mean calibrated completion | 0.193 | 0.208 |
| Completion retention | 52.3% | 70.7% |
| AAVE politeness delta | -16.3% | +13.5% |
| Indian politeness delta | -17.7% | +12.9% |
| Overcorrected rebound | +8.2% | +14.3% |
| H1 pass | 1/1 | 4/4 |
| H2 pass | 0/1 | 0/4 |
| H3 pass | 0/1 | 1/4 |
