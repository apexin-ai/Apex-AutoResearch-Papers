# ssh prepare batchsize16 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare_batchsize16_41312_20260517T111722_result.json`
- **Structured JSON:** [`c0f7883c8f77bac2cdde.json`](../../sessions/c0/c0f7883c8f77bac2cdde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

参数全部合法。脚本已就绪。

**脚本路径**: `/root/provenance_weight_training/scripts/run_batchsize16_nmin8_r2.sh`

**与原 batchsize16_nmin8_seed42 的关键差异**:
- 移除 `--eval_steps 500` 和 `--eval_data_path data/human/eval_holdout.jsonl`（M003 硬约束）
- `--output_dir` 改为 `/root/autodl-tmp/output/models/batchsize16_nmin8_r2`
- `--wandb_run_name` 改为 `batchsize16_nmin8_r2`
- 新增 `--gradient_checkpointing`
- 无 `CUDA_VISIBLE_DEVICES`

---
