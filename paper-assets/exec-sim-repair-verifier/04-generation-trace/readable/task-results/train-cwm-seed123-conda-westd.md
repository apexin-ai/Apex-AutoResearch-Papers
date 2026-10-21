# train cwm seed123 conda westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_cwm-seed123-conda-westd_20260513T220515_result.json`
- **Structured JSON:** [`ffa399c238562432ba0d.json`](../../sessions/ff/ffa399c238562432ba0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动：

- **GPU 0**: 16243 MiB 占用
- **模型**: Qwen3-4B, trainable 0.2924% (LoRA 11.8M params)
- **总步数**: 6633 steps (3 epochs)
- **tmux session**: `cwm_seed123`
- **log**: `/root/autodl-tmp/checkpoints_repo_cwm_seed123_conda/train.log`
- **registry**: `repo-level-cwm-seed123-conda` → RUNNING

所有指标与 v12 (seed=42) 完全一致：相同 truncation 比例 (train 4.5%, val 20.2%)、相同参数量、相同 step 数。

---
