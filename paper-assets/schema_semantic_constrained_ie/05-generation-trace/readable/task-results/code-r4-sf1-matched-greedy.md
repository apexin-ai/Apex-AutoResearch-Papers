# code r4 sf1 matched greedy

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r4_sf1_matched_greedy_20260517T105411_result.json`
- **Structured JSON:** [`855542165eec373c9746.json`](../../sessions/85/855542165eec373c9746.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Model | Metric | Greedy (matched 50) | Beam k=4 | Delta |
|-------|--------|-------------------|-----------|-------|
| **Qwen** | DR | 8.69 | 0 | -8.69 |
| | CF | 2.08 | 0.55 | -1.53 |
| | R-F1 | 8.33 | 9.37 | +1.04 |
| **Llama** | DR | 1.58 | 0 | -1.58 |
| | CF | 6.85 | 0.94 | -5.91 |
| | R-F1 | 6.12 | 9.47 | +3.35 |
| **Mistral** | DR | 28.37 | 21.37 | -7.00 |
| | CF | 0.34 | 0.19 | -0.15 |
| | R-F1 | 4.19 | 5.70 | +1.51 |

Beam search 在 matched comparison 下对所有模型均展示了 violation rate 降低和 R-F1 提升。Llama 的改善最显著（DR 完全消除, CF 从 6.85→0.94, R-F1 +3.35pp）。

---
