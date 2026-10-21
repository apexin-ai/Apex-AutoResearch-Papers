# exp c1 ablation 30pct s123

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_c1-ablation-30pct-s123_20260519T020801_result.json`
- **Structured JSON:** [`41667c04edcd51f0cccc.json`](../../sessions/41/41667c04edcd51f0cccc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## C1@30% s123 完整结果

### 训练
- **KL checkpoint**: `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt`
- **BCE checkpoint**: `/root/distill_sparse_swiglu/checkpoints/c1_ablation_30pct_s123/predictor_bce_kl_targets.pt` (151MB)
- **最终 BCE loss**: 0.0604 (step 600), agreement=0.975-0.976
- **训练耗时**: 877.9s (0.88s/step)

### Eval 指标 (TEAL 30% uniform)

| Metric | Value |
|--------|-------|
| WikiText-2 PPL | **8.83** |
| ARC-Challenge (acc_norm) | **47.35%** |
| WinoGrande (acc) | **71.19%** |
| MMLU (acc) | **38.33%** |
| GSM8K (exact_match) | **6.07%** |

### 备注
- 训练内置 eval 报 PPL=7.57（仅 141 sequences，较乐观），benchmark_eval 完整评估 PPL=8.83
- 无失败，全流程正常完成

---
