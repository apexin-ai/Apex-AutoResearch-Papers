# diagnostic beam8 s1 551 check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_beam8_s1_551_check_20260520T164611_result.json`
- **Structured JSON:** [`373a9360e8870a3a2e8a.json`](../../sessions/37/373a9360e8870a3a2e8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果：

| 指标 | 值 |
|------|-----|
| Samples | 551 |
| Parse Fail | 0 (0.0%) |
| E-F1 | **67.51** (P=64.99, R=70.23) |
| R-F1 | **44.95** (P=40.10, R=51.13) |
| ET% | 0.00 |
| RV% | 0.00 |
| DR% | 0.00 |
| CF% | 0.00 |

实验确认完整完成，cron 监控的 DONE(failed) 是误报。所有 551 文档推理成功，0 解析失败。约束违反率全部为 0%（ET/RV/DR/CF），说明 beam8 constrained decoding 在 SciERC 上完全遵守了 schema 约束。

---
