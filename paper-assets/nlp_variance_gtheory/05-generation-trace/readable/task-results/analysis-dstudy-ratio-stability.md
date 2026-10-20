# analysis dstudy ratio stability

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dstudy_ratio_stability_20260521T143013_result.json`
- **Structured JSON:** [`d1c8346c05e8d0480baf.json`](../../sessions/d1/d1c8346c05e8d0480baf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部完成。

---

## Task 1: D-study Ratio 稳定性

输出已写入 `results/exp001_analysis/dstudy_ratio_stability.json`。

| Subset | Multi min_items | Single min_items | **Ratio** | G_item | G_item CI |
|--------|:-:|:-:|:-:|:-:|:-:|
| 50 | 17.3 | 143.7 | **8.55** | 0.9221 | [0.913, 0.939] |
| 100 | 35.0 | 305.3 | **8.84** | 0.9205 | [0.915, 0.924] |
| 150 | 51.0 | 450.7 | **8.92** | 0.9223 | [0.918, 0.926] |
| 200 | 72.0 | 631.0 | **8.86** | 0.9184 | point est. |

**Ratio 统计**：
- Mean = 8.78，across-all-samples CV = 5.28%
- **across-subset-sizes CV ≈ 1.9%**（仅 4 个 size 均值: 8.55, 8.84, 8.92, 8.86）

结论：min_items_G80 绝对值随样本量线性增长（CV 17.8%），但 **single/multi ratio 高度稳定**（~8.8x，跨 size CV < 2%）。这个 ratio 可以作为可靠的报告指标。

---

## Task 2: 删除确认

`gsm8k_corrected.jsonl` 已删除。

---

## Task 3: LOBO p-values — **需要修复**

`permutation_p_value` 使用 `is_monotonic_decreasing` / `is_monotonic_increasing` 作为二元检验统计量。LOBO 后只剩 3 个 benchmark，3! = 6 种排列，只有 1 种满足严格单调 → **所有 p-values 都锁死在 1/6 ≈ 0.167**，无法区分强弱趋势。

当前结果：
| Dropped | item_id dec | model:item inc | p_item | p_model_item |
|---------|:-:|:-:|:-:|:-:|
| mmlu | True | False | 0.167 | 0.167 |
| arc | False | False | 0.167 | 0.167 |
| hellaswag | False | False | 0.167 | 0.167 |
| gsm8k | False | False | 0.167 | 0.167 |

全集 4 benchmark 的 gradient 本身就是 False（item_id 非单调递减，model:item 非单调递增），所以 LOBO 分析的前提都不成立。

**根本问题**：不是统计量选择问题——即使换 Spearman ρ，3-4 个数据点的排列检验依然只有 6-24 种排列，统计功效极低。这个分析需要重新设计思路，而不只是换统计量。

---
