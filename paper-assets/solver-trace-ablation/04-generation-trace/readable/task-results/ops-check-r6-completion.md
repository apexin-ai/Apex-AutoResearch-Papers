# ops check r6 completion

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-r6-completion_20260517T001358_result.json`
- **Structured JSON:** [`2838547348fa64096adc.json`](../../sessions/28/2838547348fa64096adc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练失败。**

- **停止步数**: step 100 / 1000
- **失败原因**: 磁盘满（250G/250G，仅剩 700K）
- **最后日志时间**: 2026-05-17T00:12:10 UTC (step 100)
- **checkpoint-100 不完整**: 只写入了 2/4 个 model shard（写到一半磁盘耗尽）
- **checkpoint-50**: 有 trainer_state.json，可能完整

根因：save_total_limit=1 已设置（save_steps=50），但 output_dir 里顶层已有完整模型文件（~16GB）+ 1112 行 reward_log（多次 run 累积），加上 checkpoint-50 未被及时删除就开始写 checkpoint-100，导致磁盘爆满。这是 C003 的变体——checkpoint 切换时的瞬时双份 checkpoint 占用超过剩余空间。

---
