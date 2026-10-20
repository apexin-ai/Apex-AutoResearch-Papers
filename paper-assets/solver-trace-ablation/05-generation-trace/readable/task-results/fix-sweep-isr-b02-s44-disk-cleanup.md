# fix sweep isr b02 s44 disk cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sweep-isr-b02-s44-disk-cleanup_20260516T055254_result.json`
- **Structured JSON:** [`03add043a43641ae3f85.json`](../../sessions/03/03add043a43641ae3f85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常启动，模型加载中。

**结果：**
- 清理了 ~54GB：`sweep_isr_b02_s44/` (24G)、`plan018_random_b01_s45/checkpoint-50/` (15G)、`sweep_isr_b01_s45/checkpoint-200/` (15G)
- 磁盘：250G → 197G used, 54G free (79%)
- 重提交成功：PID 688214, tmux session `sweep-isr-b02-s44`, cuda:1
- Registry 已更新

---
