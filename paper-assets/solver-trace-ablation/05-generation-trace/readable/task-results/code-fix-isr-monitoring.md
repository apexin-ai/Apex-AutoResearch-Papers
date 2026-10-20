# code fix isr monitoring

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-isr-monitoring_20260513T234032_result.json`
- **Structured JSON:** [`cf0ac7fb59660caea3aa.json`](../../sessions/cf/cf0ac7fb59660caea3aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。

**修改总结**：

- 文件：`scripts/train_grpo.py`，第 168 行
- 改动：`execution_only` 分支中 `_fast_fn` → `_full_fn`（1 行）
- 效果：`_full_fn`（即 `sta_reward`/`prolog_sta_reward`）在 proved 时通过 `run_sta` + `compute_isr` 计算连续 ISR（0.0-1.0），写入 `result["sta_reward"]`，被后续监控代码 `isr = result.get("sta_reward", 0.0)` 正确拾取。`reward_val` 仍然只取 `result["execution_reward"]`，训练信号不变。

---
