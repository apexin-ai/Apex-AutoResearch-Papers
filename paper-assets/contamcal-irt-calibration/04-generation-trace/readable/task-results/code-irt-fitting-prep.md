# code irt fitting prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_irt-fitting-prep_20260519T120527_result.json`
- **Structured JSON:** [`9ff57fcec161ecd60b6c.json`](../../sessions/9f/9ff57fcec161ecd60b6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部输出已生成。结果汇总：

**MMLU** (21 respondents × 14042 items, 10 iterations收敛)
| Family | beta | p-value | R² |
|---------|-------|---------|------|
| qwen7b | -0.041 | 0.797 | 0.026 |
| qwen14b | -0.802 | 0.086 | 0.679 |
| gemma2 | +0.012 | 0.939 | 0.002 |
| phi4 | -0.061 | 0.819 | 0.020 |
| olmo2 | MISSING (仅 d100) |

- TOST d000 vs d005: mean_diff=-0.014, p=0.456 (NOT equivalent)

**ARC-Challenge** (21 respondents × 1172 items, 12 iterations收敛)
| Family | beta | p-value | R² |
|---------|-------|---------|------|
| qwen7b | -0.320 | 0.172 | 0.515 |
| qwen14b | -0.149 | 0.123 | 0.602 |
| gemma2 | -0.259 | 0.859 | 0.012 |
| phi4 | +0.518 | **0.032** | 0.830 |
| olmo2 | MISSING |

- TOST d000 vs d005: mean_diff=0.326, p=0.564 (NOT equivalent)

**输出文件：**
- CSV: `irt_dose_response.csv`
- 图: `irt_mmlu_dose_response.pdf`, `irt_arc_challenge_dose_response.pdf`
- 脚本: `/root/contamcal-irt-calibration/exp001/fit_irt_dose_response.py`

注意：gemma2 在 ARC 上 theta 波动剧烈（d050=-3.14），可能有数据质量问题。MMLU 上大多数 family 的 dose-response 不显著，phi4 在 ARC 上是唯一显著正 beta（p=0.032），但方向是 contamination 提升能力，需要进一步调查。

---
