# fix exp 14b c4 resubmit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_14b_c4_resubmit_20260518T051103_result.json`
- **Structured JSON:** [`e623241f56f28e4ac644.json`](../../sessions/e6/e623241f56f28e4ac644.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功重提交并在运行中。

- **数据检查**: depth 0-4 各 5000 行完好，depth_5 不存在（无需清理）
- **results 目录**: 已清理
- **Registry**: DONE → PREPARING → QUEUED → RUNNING
- **任务**: westd-42896 cuda:0，tmux session `exp_14b_c4`，timeout 6h，模型正在加载（14B checkpoint shards loading）
- Pipeline 会自动跳过已完成的 depth 0-4，只跑 depth 5

---
