# monitoring server status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_server_status_check_20260519T131128_result.json`
- **Structured JSON:** [`9bd1850e78d1406fd5ce.json`](../../sessions/9b/9bd1850e78d1406fd5ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/server_status_20260519.md`。

---

**汇总：**

| 服务器 | 实验 | 状态 | 进度 | ETA |
|--------|------|------|------|-----|
| **B** | 72B FewNERD zero-shot | **Greedy 进行中** | 26% (9909/37648) | ~22:00 UTC 今天 |
| A | 32B FewNERD train | 训练中 (eval phase) | 9.7% (4000/41180) | ~01:00 UTC May 21 |
| C | 14B FewNERD train | 训练中 | 17.5% (7196/41180) | ~18:00 UTC May 20 |
| C | 7B FewNERD train | 训练中 | 12.0% (2467/20590) | ~09:00 UTC May 20 |

**72B greedy decoding 尚未完成**，预计约 48 分钟后（~22:00 UTC）结束。scierc 和 conll2003 的 zero-shot 结果已产出（greedy F1: scierc 0.399, conll2003 0.712）。所有训练进程正常运行，loss 稳定下降。

---
