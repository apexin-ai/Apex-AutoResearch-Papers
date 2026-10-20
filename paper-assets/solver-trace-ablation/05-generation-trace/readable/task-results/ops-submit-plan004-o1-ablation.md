# ops submit plan004 o1 ablation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit-plan004-o1-ablation_20260515T044452_result.json`
- **Structured JSON:** [`8dfec368dbf9e28d4dea.json`](../../sessions/8d/8dfec368dbf9e28d4dea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交并运行中。

**总结：**
- **exp_id**: plan004-o1-ablation-s42
- **状态**: RUNNING, PID=155099, cuda:1 (64880MiB)
- **配置**: `execution_fast_sta` mode, 500 steps, K=8, seed=42, Qwen3-4B
- **数据**: train_500_seed42.jsonl (500 samples) ✓ C001
- **GPU**: 仅占 cuda:1, cuda:0 空闲 ✓ C002
- **磁盘保护**: save_total_limit=1, log_completions=False ✓ C003
- **reward**: `r = 0.5 * exec + 0.5 * fast_ISR`（O(1) binary，对所有 proved 返回 ISR=1.0）

---
