# ssh check 14b uniform results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_14b_uniform_results_20260518T013405_result.json`
- **Structured JSON:** [`0341e1612f2d0e1f2c5b.json`](../../sessions/03/0341e1612f2d0e1f2c5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成。结果汇总：

## 14B Uniform Allocation 4-Task Eval Results

| Metric | KL-Predictor (ours) | TEAL Vanilla (baseline) | Delta |
|--------|---------------------|------------------------|-------|
| **WikiText2 PPL** | **7.63** | 8.01 | -0.37 (better) |
| **MMLU** | 0.6449 | **0.6634** | -1.85pp (worse) |
| ARC-C (acc_norm) | 0.5444 | **0.5529** | -0.85pp |
| WinoGrande | **0.7245** | 0.6985 | +2.60pp (better) |

**关键发现**: MMLU 64.49% vs baseline 66.34%，KL predictor 在 uniform allocation 下 MMLU 仍然落后 ~1.9pp。这与之前 learned allocation 的结果一致：KL 目标在 14B 上的 MMLU gap 是 intrinsic 的，不是 allocation 策略导致的。

PPL 方面 KL predictor 更优 (7.63 vs 8.01)，WinoGrande 也更优，但 MMLU 和 ARC-C 均略低于 TEAL vanilla baseline。

---
