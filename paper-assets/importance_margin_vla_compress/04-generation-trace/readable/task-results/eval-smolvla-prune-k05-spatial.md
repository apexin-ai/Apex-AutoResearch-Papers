# eval smolvla prune k05 spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_smolvla_prune_k05_spatial_20260519T113528_result.json`
- **Structured JSON:** [`a38c98d05a8b15daa20e.json`](../../sessions/a3/a38c98d05a8b15daa20e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **脚本**: 从 `eval_random_prune_smolvla.py` 复制并修改为 `eval_random_prune_smolvla_spatial.py`（`libero_object` → `libero_spatial`，`k_ratio` 默认 0.5）
- **命令**: `CUDA_VISIBLE_DEVICES=2 python -u eval_random_prune_smolvla_spatial.py --k_ratio 0.5 --episodes_per_task 50 --output_name smolvla_random_prune_k05_spatial.json --seed 42`
- **服务器**: cqa1-33015, GPU cuda:2, tmux session `eval_prune_spatial`
- **Registry**: `eval_smolvla_prune_k05_spatial` 状态 RUNNING
- **监控**: 每 12 分钟 cron 检查进度

前两个 episode 已确认 FAIL（280 步超时），符合 0% SR 预期。

---
