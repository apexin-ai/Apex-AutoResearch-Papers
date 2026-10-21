# check harvest llama int4 docred

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_harvest-llama-int4-docred_20260523T070326_result.json`
- **Structured JSON:** [`3c9c17c5bb16da3d699f.json`](../../sessions/3c/3c9c17c5bb16da3d699f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job，无需删除。

---

**实验收割完成：sf2_llama_int4_docred_s1 → DONE (success)**

| Metric | INT4 (AWQ) | FP16 Baseline | Delta |
|--------|-----------|---------------|-------|
| **R-F1** | **48.04** | 47.35 | **+0.69** |
| R-P | 44.79 | 43.46 | +1.33 |
| R-R | 51.80 | 52.00 | -0.20 |
| **E-F1** | **84.18** | 85.43 | **-1.25** |
| E-P | 85.50 | 85.96 | -0.46 |
| E-R | 82.90 | 84.91 | -2.01 |
| DR% | 0% | 0% | 0 |
| ET% | 0% | - | - |
| RV% | 0% | - | - |
| CF% | 0.22% | 0.19% | +0.03 |
| Parse fail | 2.5% | 2.0% | +0.5 |

结论：AWQ INT4 量化对 Llama DocRED FT+constrained 几乎无损——R-F1 反而略升 +0.69pp，E-F1 仅降 1.25pp，违规率保持接近零。模型体积从 ~16GB 降至 ~5.3GB。

---
