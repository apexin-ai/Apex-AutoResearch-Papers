# fix regenerate corrected g item json

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_regenerate_corrected_g_item_json_20260521T120107_result.json`
- **Structured JSON:** [`66b4e843d911734a4932.json`](../../sessions/66/66b4e843d911734a4932.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完成。汇总如下：

### 文件 1: `llama_single_model_gstudy.json`

| 指标 | 修正前 | 修正后 |
|------|--------|--------|
| correct G_coefficient | 0.6108 | **0.9184** |
| text_exact_match G_coefficient | 0.0066 | **0.0** (Henderson I 下 σ²_item ≈ 0，无可靠 item 排序) |

### 文件 2: `exp001b_resampling_gstudy.json`

| Sample | 修正前 | 修正后 | min_items_g80 |
|--------|--------|--------|---------------|
| baseline | 0.6108 | **0.9184** | — |
| sample1 | 0.7588 | **0.9637** | 31 |
| sample2 | 0.7538 | **0.9620** | 32 |
| sample3 | 0.7218 | **0.9548** | 38 |
| **stability mean** | 0.7448 | **0.9602** | — |
| stability CV | 2.70% | **~0.5%** | — |

### 文件 3: `dstudy_progressive_validation.json`

| Subset | 修正前 G_item | 修正后 G_item | min_items_G80 |
|--------|---------------|---------------|---------------|
| 50×3 seeds | 0.612–0.652 | **0.913–0.939** | 13–20 |
| 100×3 seeds | 0.611–0.627 | **0.915–0.924** | 33–38 |
| 150×3 seeds | 0.614–0.623 | **0.918–0.926** | 48–54 |
| 200 (full) | 0.6108 | **0.9184** | **72** |

**D-study 结论**：G≥0.80 所需最小 item 数从 ~510 降至 **72**（200 items 基准）。方差分量同步更新为 Henderson I 估计。

---
