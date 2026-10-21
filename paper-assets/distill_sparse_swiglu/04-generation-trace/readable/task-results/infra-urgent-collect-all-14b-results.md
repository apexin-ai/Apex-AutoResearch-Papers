# infra urgent collect all 14b results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent_collect_all_14b_results_20260517T214835_result.json`
- **Structured JSON:** [`3b0b9edada36afd1de84.json`](../../sessions/3b/3b0b9edada36afd1de84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 experiments are still actively running. Here's the current status:

```
实验ID                        | 状态          | PPL     | ARC | WG | MMLU | GSM8K     | 备注
-----------------------------|--------------|---------|-----|----|------|-----------|----
qwen14b_teal30_eval          | RUNNING      | 8.7332  | ✓   | ✓  | ✓    | 86% (1129/1319) | GSM8K ~53 min remaining
qwen14b_dense_baseline       | RUNNING      | 5.1854  | ✓   | ✓  | ✓    | 75% (993/1319)  | GSM8K ~43 min remaining
qwen14b_bce30_s42_eval       | RUNNING      | 8.7634  | ✓   | ✓  | ✓    | 84% (1113/1319) | GSM8K ~50 min remaining
bce_isocompute_v3_s123_eval  | RUNNING      | 28.0627 | ✓   | ✓  | 54%  | not started     | MMLU ~3 min left, then GSM8K ~2-3h
```

**GPU 状态:**
- westd-41718 cuda:0: BUSY (dense_baseline, ~43 min)
- westd-41718 cuda:1: BUSY (teal30_eval, ~53 min)
- westd-34887 cuda:0: BUSY (bce30_s42_eval, ~50 min)
- westd-34887 cuda:1: BUSY (v3_s123_eval, ~2-3h)

**额外:**
- bce_isocompute_v3_s123 训练 (PID 72392): **已完成**。Checkpoint 存在于 `/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v3_s123/predictor_bce.pt` (152MB, May 18 05:33)

**关键发现:**
- 前 3 个实验都在最后一个 benchmark (GSM8K) 阶段，约 43-53 分钟内完成
- 第 4 个 (v3_s123) 是 LLaMA-3.1-8B (非 Qwen14B)，50% sparsity，MMLU 即将完成但 GSM8K 还需 2-3 小时
- TEAL vanilla PPL (8.73) 和 BCE predictor PPL (8.76) 在 30% sparsity 下非常接近
- Dense baseline PPL = 5.19 作为上界参考

**无法更新 registry**——所有实验尚未完成，等 ~1h 后再检查前 3 个。

---
