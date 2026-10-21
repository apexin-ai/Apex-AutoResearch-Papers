# diagnose long postfix failures

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_long_postfix_failures_20260524T141423_result.json`
- **Structured JSON:** [`b79dd0584792ce6b2736.json`](../../sessions/b7/b79dd0584792ce6b2736.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：监控系统误报，非实际失败。** 这批 Long eval 实验不写 sentinel 文件、不连 W&B，监控健康检查 5 次找不到信号后自动判定 "process dead"，但实际进程全部正常运行。

已完成的 5 个实验结果：
- l2norm k=0.95 → **87.0%**
- l2norm k=0.85 → **78.4%**
- random k=0.7 → **65.8%**
- random k=0.95 → **63.2%**
- random k=0.85 → **45.2%**

还有 4 个实验仍在正常运行中（random k=0.5, k=0.3, k=0.9 和 l2norm k=0.3），预计 1-3 小时内完成，无需干预。

报告已保存到 `artifacts/diag_long_postfix_failure_20250524.md`。

---
