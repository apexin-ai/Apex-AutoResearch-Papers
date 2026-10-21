# fix simulation matched design

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_simulation_matched_design_20260521T102020_result.json`
- **Structured JSON:** [`aca439897f2b5e2e1fbc.json`](../../sessions/ac/aca439897f2b5e2e1fbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认 `conditions_per_item = 1,296`，与 exp-001 的 seed=6, ordering=4 设计匹配。

## 新旧结果对比

| 指标 | Original (432 cond/item) | Matched (1,296 cond/item) | 变化 |
|------|--------------------------|---------------------------|------|
| **Spearman rho (no residual)** | | | |
| 均值 | 0.708 | 0.732 | **+0.024** |
| 范围 | 0.685–0.734 | 0.716–0.751 | 下界提升明显 |
| **rho by accuracy** | | | |
| p=0.5 | 0.714 | 0.741 | +0.027 |
| p=0.6 | 0.714 | 0.731 | +0.017 |
| p=0.7 | 0.703 | 0.731 | +0.028 |
| p=0.8 | 0.702 | 0.724 | +0.022 |
| **Top-1 (item_id) recovery** | 100% (99% at p=0.8) | **100%** all conditions | 更稳定 |
| **Top-5 no-residual recovery** | 72% avg (58–82%) | **79% avg** (71–88%) | **+7pp** |
| **Top-5 all-components** | 92% avg | **97% avg** | +5pp |
| **Mean \|bias\| by accuracy** | | | |
| p=0.5 | 0.361 | 0.299 | **−0.062** |
| p=0.6 | 0.342 | 0.279 | **−0.063** |
| p=0.7 | 0.415 | 0.340 | **−0.075** |
| p=0.8 | 0.404 | 0.368 | **−0.036** |
| **Conditions/item** | 432 | **1,296** | ×3 |

**结论**：matched 设计（1,296 conditions/item）下，Henderson I 的 binary recovery 全面优于原始设计——Spearman rho 提升 ~0.024，top-5 ranking recovery 提升 7pp，bias 下降 0.04–0.08pp。更多 conditions 提供了更充分的方差分解信息，符合预期。原始结果文件未被覆盖。

---
