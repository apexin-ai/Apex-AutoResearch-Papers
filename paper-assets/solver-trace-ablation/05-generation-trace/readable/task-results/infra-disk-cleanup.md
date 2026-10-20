# infra disk cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-cleanup_20260514T214433_result.json`
- **Structured JSON:** [`72e213a914c7f14cc98f.json`](../../sessions/72/72e213a914c7f14cc98f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**释放空间**：105GB（240G→135G，96%→54%）
- `outputs/` 由 218G 降至 113G
- 所有 8 个冗余 checkpoint 子目录已删除
- 保留：每个实验的最终模型权重、eval_results.json、reward_log.jsonl

**当前磁盘**：250G 中已用 135G，可用 116G。

---
