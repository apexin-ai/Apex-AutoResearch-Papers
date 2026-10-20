# analysis paper data formatting

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-data-formatting_20260517T171948_result.json`
- **Structured JSON:** [`4858d2ededa75842d6a8.json`](../../sessions/48/4858d2ededa75842d6a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。文件已写入 `/root/symb_invariant_consensus/analysis/paper_table_data.json`。

**Summary:**

**QwQ-32B Operating Regime (Table 1):**
| Model | Dataset | n | K | C0_eff% | SC% | SICA% | Δ(pp) |
|---|---|---|---|---|---|---|---|
| QwQ-32B | AIME-2024 | 22 | 12 | 0.0 | 72.7 | 72.7 | 0.0 |
| QwQ-32B | ProofWriter-D5 | 17 | 12 | 5.9 | 88.2 | 82.4 | -5.9 |
| QwQ-32B | FOLIO | 2 | 4 | 0.0 | 100 | 100 | 0.0 |
| QwQ-32B | MATH-L4/5 (temp) | 5 | 12 | 0.0 | --- | --- | --- |
| QwQ-32B | Combined (main) | 39 | 12 | 2.6 | --- | --- | 0.0 |

**Overhead Breakdown (Appendix):**
| Domain | n | Total(s) | Trace% | Extract% | Dedup% | Overhead% |
|---|---|---|---|---|---|---|
| ProofWriter | 600 | 65.6 | 48.7 | 49.6 | 1.7 | 51.3 |
| FOLIO | 204 | 49.8 | 61.4 | 37.2 | 1.4 | 38.6 |
| Combined | 804 | 61.6 | 51.3 | 47.0 | 1.6 | 48.7 |

JSON 包含完整数据 + LaTeX tabular 代码，可直接用于论文。

---
