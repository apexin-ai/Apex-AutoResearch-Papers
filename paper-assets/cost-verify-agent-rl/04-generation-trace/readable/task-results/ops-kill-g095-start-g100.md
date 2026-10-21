# ops kill g095 start g100

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-g095-start-g100_20260518T130740_result.json`
- **Structured JSON:** [`2a27b39c8ba803d3ef4e.json`](../../sessions/2a/2a27b39c8ba803d3ef4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

| 项目 | 状态 |
|---|---|
| **g095 kill** | PID 416289 已终止，GPU 2,3 已释放（3MiB → idle） |
| **factorial_seed2** | PID 576727 正常运行，GPU 0,1 占用 ~18GB each，未受影响 |
| **g100 PID** | **714093** |
| **g100 W&B run ID** | **da7701tk** |
| **GPU 显存** | GPU 0: 17993MiB (factorial), GPU 1: 17993MiB (factorial), GPU 2: 4731MiB (g100 loading), GPU 3: 4731MiB (g100 loading) |
| **RAM** | 84GB / 1TB used |
| **Registry** | g095 → DONE/negative (metrics: val=0% step5); g100 → RUNNING (spec 完整) |
| **Cron** | 每小时 :23 自动检查 g100 状态 (job 2140a5fb) |

---
