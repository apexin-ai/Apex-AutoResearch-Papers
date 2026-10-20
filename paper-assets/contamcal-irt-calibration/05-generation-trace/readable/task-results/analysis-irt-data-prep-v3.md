# analysis irt data prep v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irt-data-prep-v3_20260519T213819_result.json`
- **Structured JSON:** [`342bf541b3e6c7e1380a.json`](../../sessions/34/342bf541b3e6c7e1380a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出已生成并验证通过。

**结果汇总：**

| 产出 | 规格 | 路径 |
|------|------|------|
| `response_matrix_mmlu.csv` | 25 × 14042 | `/root/contamcal-irt-calibration/analysis/irt_data_v3/` |
| `response_matrix_arc.csv` | 25 × 1172 | 同上 |
| `exposure_scores.csv` | 25 行（5 families × 5 dosages） | 同上 |
| `item_metadata_mmlu.csv` | 14042 行，含 subject/domain/difficulty_baseline | 同上 |
| `item_metadata_arc.csv` | 1172 行，含 difficulty_baseline | 同上 |
| `irt_data_prep_v3.py` | 生成脚本 | 同上 |

**覆盖率：25/25 respondents，无缺失。** 数据源为 westd `eval_results_v2/`，57 个 MMLU subject 映射到 4 个 domain（STEM 3153, Humanities 4705, Social Sciences 3077, Other 3107）。

---
