# train train without ob

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_train-without-ob_20260514T135043_result.json`
- **Structured JSON:** [`2aa83655ba6a65af0f3e.json`](../../sessions/2a/2aa83655ba6a65af0f3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。

- **exp_id**: `train-without-ob`
- **PID**: 55740
- **GPU**: cuda:0
- **日志**: `~/runs/agent_progress_probe/train-without-ob.log`

脚本逻辑：
- 只用 `command_repetition` + `file_diff_delta` 做 majority vote（去掉 `outcome_backpropagation`）
- conf≥2 = 两个 LF 必须一致才保留
- 复用 probe_001 的 instance-level test split（通过 `split_by_instance` 同 seed=42 确定 instance 归属）
- GRU 2-layer, hidden=256, lr=1e-3, batch=32, epochs=20, early stop patience=5

---
