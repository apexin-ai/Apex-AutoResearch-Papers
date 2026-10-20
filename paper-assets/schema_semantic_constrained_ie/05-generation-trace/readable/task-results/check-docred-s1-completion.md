# check docred s1 completion

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_docred-s1-completion_20260522T101851_result.json`
- **Structured JSON:** [`6b411fec04d88fe92c2c.json`](../../sessions/6b/6b411fec04d88fe92c2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 session 中创建，当前 session 无需删除）。

**实验完成总结：**

| 指标 | 值 |
|------|-----|
| E-F1 | 79.38 (P=85.24, R=74.28) |
| R-F1 | 43.95 (P=40.48, R=48.08) |
| DR% | 0.00 |
| RV% | 0.00 |
| ET% | 0.00 |
| CF% | 0.18 |
| parse_fail% | 12.5 (25/200 FAIL) |

Registry 已更新为 DONE/success。三类 schema 违规（DR/RV/ET）全部为零，S1 约束解码有效。parse_fail 12.5% 来自 25 个超时文档（E=0 R=0），CF% 仅 0.18%。这些数值可直接填入 section5_runtime.tex L18 的占位符。

---
