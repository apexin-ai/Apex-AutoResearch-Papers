# analysis henderson i complete 259200

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_henderson_i_complete_259200_20260521T211557_result.json`
- **Structured JSON:** [`29ffb281b9d52ed3ffad.json`](../../sessions/29/29ffb281b9d52ed3ffad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实际 facet 水平确认：
- precision: 3 (bf16, fp16, fp32) — 每种 86,400
- temperature: 3 (0.0, 0.3, 0.7) — 每种 86,400
- prompt_template: 6 (1-6)
- seed: 6 (42, 123, 456, 789, 1024, 2048)
- ordering: 4 (1-4)
- item_id: 200

3×3×6×6×4×200 = 259,200 ✓ 完全平衡设计。

---

## 结果汇总

### 1. 数据合并
- 4 shards (59,800×4) + backfill (20,000) = **259,200 records**，无重复
- 1,296 conditions × 200 items，完全平衡设计 ✓
- 合并 CSV: `results/analysis/llama_full_259200.csv`

### 2. Henderson I 6-facet方差分解 (correct metric)

| 方差分量 | σ² | % |
|---|---|---|
| **item_id** | 0.12711 | **58.39%** |
| residual | 0.05029 | 23.10% |
| prompt_template:item_id | 0.01190 | 5.47% |
| seed:item_id | 0.01026 | 4.71% |
| precision:item_id | 0.00719 | 3.30% |
| temperature:item_id | 0.00638 | 2.93% |
| precision | 0.00198 | 0.91% |
| ordering:item_id | 0.00168 | 0.77% |
| precision:temperature | 0.00058 | 0.27% |
| 其余 | <0.001 | <0.05% |

5 个负方差分量被截断为 0（prompt_template, seed, ordering 主效应和 2 个微小交互项）。

**G_item = 0.9361** (at n=200 items)

### 3. BF16-only 5-facet Henderson I (86,400 records)

| 方差分量 | % |
|---|---|
| **item_id** | **70.94%** |
| residual | 13.61% |
| seed:item_id | 6.32% |
| prompt_template:item_id | 5.40% |
| temperature:item_id | 2.67% |
| ordering:item_id | 1.00% |

**G_item = 0.9578**

### 4. 与旧数字差异

| | 旧值 (SS proportion, 239K) | 新值 (Henderson I, 259K) |
|---|---|---|
| item_id % | 54.85% | **58.39%** |
| G_item (n=200) | 0.9184 | **0.9361** |

差异来源：(1) Henderson I 从 MS 解方差分量而非直接用 SS/SS_total，对 main effect 的估计更准确；(2) 补回 20,000 FP32×T=0.0 records 使设计平衡，precision 主效应（0.91%）被正确分离。

### 5. 输出文件
`results/analysis/unified_henderson_i_numbers.json` — 包含完整 ANOVA 表、原始/调整后方差分量、G coefficient、D-study、新旧对比。

---
