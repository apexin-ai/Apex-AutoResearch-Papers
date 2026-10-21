# diagnose acis k07 cron

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_acis_k07_cron_20260517T072342_result.json`
- **Structured JSON:** [`11832fdcea52a630b04a.json`](../../sessions/11/11832fdcea52a630b04a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：Cron 误报，进程未退出。**

- 训练正常运行中，step 2300/10000，ETA ~07:55 UTC
- margin_loss 从 0.30 → 0.19，收敛正常
- 不执行 delete_cron，保留监控直到训练真正完成

---
