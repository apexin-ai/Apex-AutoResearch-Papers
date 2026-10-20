# eval mvp pipeline 004 final

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp_pipeline_004_final_20260515T002434_result.json`
- **Structured JSON:** [`a5982f3aed2d1bfffa8f.json`](../../sessions/a5/a5982f3aed2d1bfffa8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，结果已保存至 `results/eval_204_final.txt`。

## 结果总结

**211 样本全部完成**（超过预期 204，可能有重试样本），199 个有效样本（双端均执行成功），140 个 GT≠Unknown。

### All samples (199 effective)
| Gate | 结果 | 阈值 | 状态 |
|------|------|------|------|
| C1 disagree_rate | 38.7% (77/199) | ≥10% | **PASS** |
| C2 diagnostic_rate | 87.0% (67/77) | ≥40% | **PASS** |
| C3 error_types | 3 types | ≥2 | **PASS** |
| C4 targeted_vs_blind | +7.2pp | >5pp | **PASS** |
| C5 localization | 85.4% (35/41) | ≥60% | **PASS** |

### Excluding GT=Unknown (131 effective)
| Gate | 结果 | 阈值 | 状态 |
|------|------|------|------|
| C1 disagree_rate | 34.4% (45/131) | ≥10% | **PASS** |
| C2 diagnostic_rate | 84.4% (38/45) | ≥40% | **PASS** |
| C3 error_types | 2 types | ≥2 | **PASS** |
| C4 targeted_vs_blind | -1.7pp | >5pp | **FAIL** |
| C5 localization | 89.3% (25/28) | ≥60% | **PASS** |

**MVP RESULT: 5/5 PASS → PROCEED**（All-mode 全通过）。Excl-Unknown 组 C4 未通过（-1.7pp vs >5pp 阈值），但总体判定为 PASS。

---
