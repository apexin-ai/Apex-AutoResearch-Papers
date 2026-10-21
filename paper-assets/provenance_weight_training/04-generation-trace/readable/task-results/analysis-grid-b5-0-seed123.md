# analysis grid b5 0 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b5_0_seed123_20260514T151019_result.json`
- **Structured JSON:** [`a02bc6ead33e77b0a967.json`](../../sessions/a0/a02bc6ead33e77b0a967.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。`grid_b5_0_seed123` 提取结果：

| 指标 | 值 |
|------|-----|
| total_steps | 6103 |
| train_loss_avg (全程) | 2.7118 |
| train_loss_last100steps | 2.5906 |
| final_step_loss | 2.4771 |
| train_runtime | ~13554s (~3.78h) |
| num_train_tokens | 200M |
| checkpoint_path | `/root/provenance_weight_training/output/models/grid_b5_0_seed123/final/` |
| eval_ppl_holdout | **无** |
| eval_loss | **无** |

该实验启动时未传 `--eval_data_path`，`eval_strategy="no"`，因此没有 eval 指标。需要单独跑 eval 才能获得 `eval_ppl_holdout` 与其他 b 值对比。

---
