# code d146 pipeline recovery

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-pipeline-recovery_20260519T174048_result.json`
- **Structured JSON:** [`9ab2cdbcd96d162fa4b0.json`](../../sessions/9a/9ab2cdbcd96d162fa4b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pipeline 正常运行，无需恢复。**

- `d146-pipeline` tmux session 存活
- exec-s43 正在跑（step 431/500），PID 461832，GPU 0 占用 85.4GB / 97.9GB，利用率 88%
- Pipeline 脚本是顺序执行的（`set -e`），exec-s43 完成后会自动依次跑 exec-s44 → isr-s42 → isr-s43 → isr-s44
- 剩余 5 个实验都在队列中，无需手动干预

预计 exec-s43 还剩约 69 步（431→500），按当前速度很快完成。

---
