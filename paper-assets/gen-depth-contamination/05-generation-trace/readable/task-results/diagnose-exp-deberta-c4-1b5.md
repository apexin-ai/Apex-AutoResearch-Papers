# diagnose exp deberta c4 1b5

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_deberta_c4_1b5_20260519T231400_result.json`
- **Structured JSON:** [`fa4de6ccbfd14e7dcf19.json`](../../sessions/fa/fa4de6ccbfd14e7dcf19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：exp_deberta_c4_1b5 正常完成，应将状态从 "failed" 改为 "success"。**

关键证据：
- 日志最后一行是 `Done.`，3 个 epoch 全部跑完，无任何错误
- 结果文件齐全（JSON metrics + OOF predictions + log）
- K*=2，DeBERTa 在所有 pair 上均优于 OBD baseline（delta +0.005 到 +0.079）
- 误判原因：cron 监控依赖 W&B sentinel，但该实验未使用 W&B

---
