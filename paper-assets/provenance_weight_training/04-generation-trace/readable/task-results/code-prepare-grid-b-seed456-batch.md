# code prepare grid b seed456 batch

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_grid_b_seed456_batch_20260514T171600_result.json`
- **Structured JSON:** [`a4106ea817fb6525c097.json`](../../sessions/a4/a4106ea817fb6525c097.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过语法检查。

**`/root/provenance_weight_training/run_grid_b_seed456.sh`** 已就绪：

- 6 个 b 值 (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) 串行训练，seed=456
- 相比原 seed42 脚本的修改：
  - seed 42 → 456，所有目录/日志名同步更新
  - **新增** `--eval_data_path data/human/eval_holdout.jsonl`（原脚本缺失）
  - **新增** `--bf16`
  - **新增** `WANDB_MODE=disabled`
  - `save_total_limit` 2 → 3
- 语法验证通过，输出目录无冲突，脚本已设为可执行

---
