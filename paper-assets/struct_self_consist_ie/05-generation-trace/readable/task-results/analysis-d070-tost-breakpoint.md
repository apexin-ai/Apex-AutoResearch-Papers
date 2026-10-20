# analysis d070 tost breakpoint

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d070_tost_breakpoint_20260515T091709_result.json`
- **Structured JSON:** [`5a6ba846232a09f2d9f1.json`](../../sessions/5a/5a6ba846232a09f2d9f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已注册。结果汇总：

**NER (n=529)**: δ* ∈ [1.28, 3.38] pp

| Signal | δ* (pp) |
|--------|---------|
| SJ | 1.28 |
| LP | 1.80 |
| EM | 2.07 |
| VC | 2.29 |
| FK | 3.38 |

**RE (n=397)**: δ* ∈ [2.86, 6.53] pp

| Signal | δ* (pp) |
|--------|---------|
| LP | 2.86 |
| SJ | 3.76 |
| FK | 4.22 |
| EM | 5.17 |
| VC | 6.53 |

使用 paired t-distribution 90% CI 计算，与 TOST worker 的 8 个已知判定结果全部一致。论文当前参数下（NER δ=2pp, RE δ=5pp），NER 仅 SJ/LP 通过，RE 仅 LP/SJ/FK 通过。

---
