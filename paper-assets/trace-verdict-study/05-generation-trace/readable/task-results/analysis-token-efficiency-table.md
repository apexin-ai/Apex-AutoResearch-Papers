# analysis token efficiency table

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_token-efficiency-table_20260517T003811_result.json`
- **Structured JSON:** [`2d8824d0aeb163323320.json`](../../sessions/2d/2d8824d0aeb163323320.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `/root/trace-verdict-study/docs/paper/token_efficiency_table.md`。

**结果摘要：**

| Condition | Mean Tokens | Accuracy | Acc/1K Tokens | Relative Efficiency |
|-----------|-------------|----------|---------------|---------------------|
| no_trace | 152.5 | 75.13% | 492.66 | 1.97 |
| exception_only | 398.4 | 99.83% | 250.58 | 1.00 |
| ae_only | 1287.0 | 99.92% | 77.64 | 0.31 |
| loop_only | 1151.7 | 85.63% | 74.35 | 0.30 |
| vota | 1879.1 | 99.41% | 52.90 | 0.21 |
| full_trace | 1911.6 | 81.76% | 42.77 | 0.17 |

exception_only 用 398 tokens 达到 99.83% 准确率，是高准确率条件中效率最高的；full_trace 用 5x 的 token 反而准确率更低。

---
