# eval beam sweep missing violations

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_beam_sweep_missing_violations_20260522T040538_result.json`
- **Structured JSON:** [`ba651549b2b812d06e64.json`](../../sessions/ba/ba651549b2b812d06e64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。**beam1 unconstrained 文件不存在**，无法评估 `d066_sweep_llama_docred_beam1_unc`。

## 评估结果汇总

| Metric | beam2_full_s1 (constrained) | beam8_unconstrained |
|--------|---------------------------|---------------------|
| **E-F1** | 85.60 | 85.77 |
| E-P | 85.29 | 85.70 |
| E-R | 85.92 | 85.84 |
| **R-F1** | 51.17 | 51.97 |
| R-P | 48.51 | 49.76 |
| R-R | 54.14 | 54.38 |
| DR% | **0.00** | **0.00** |
| CF% | 0.00 | 0.05 |
| ET% | 0.00 | 0.00 |
| RV% | 0.00 | 0.07 |
| Parse Fail% | 0.5 | 0.5 |
| Entities pred | 3814 | 3788 |
| Relations pred | 2839 | 2779 |

**缺失**: `llama_docred_200_beam1_unconstrained.jsonl` 在 `/root/autodl-tmp/schema_outputs/d066_beam_sweep/` 下不存在，整个 `schema_outputs/` 目录也没有任何 beam1 文件。需要先生成该推理输出才能评估。

---
