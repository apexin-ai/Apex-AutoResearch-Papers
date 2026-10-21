# eval d065 llama 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d065_llama_16980_20260520T095400_result.json`
- **Structured JSON:** [`11bbc0a4769320912fec.json`](../../sessions/11/11bbc0a4769320912fec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d065 Llama greedy 4096 eval 结果（998 docs, checker v2）：

| Metric | Llama unc | Llama con |
|--------|-----------|-----------|
| E-F1 | 84.77 | 84.71 |
| R-F1 | 44.55 | 44.70 |
| DR% | 0.49 (80) | 0.00 (0) |
| RV% | 0.15 (24) | 0.00 (0) |
| CF% | 0.08 (16) | 0.26 (50) |
| ET% | 0.00 (0) | 0.00 (0) |

补充信息：
- **Parse failures**: unc 23 (2.3%), con 26 (2.61%)
- **Pred triples**: unc 16171, con 16042
- **Pred entities**: unc 19106, con 19058
- **E-P/E-R**: unc 85.75/83.82, con 85.80/83.66
- **R-P/R-R**: unc 39.31/51.39, con 39.61/51.30
- **Total violation rate**: unc 0.34% (120), con 0.14% (50)

con 模式成功消除了 DR 和 RV 违规（均降至 0），但 CF 违规从 16 增至 50。R-F1 略有提升（44.55→44.70），E-F1 基本持平。

---
