# analysis within mmlu subject gradient 4model

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_within_mmlu_subject_gradient_4model_20260521T113035_result.json`
- **Structured JSON:** [`190508cc03886014434e.json`](../../sessions/19/190508cc03886014434e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果写入 `results/exp001_analysis/within_mmlu_subject_gradient_4model.json`。

**关键发现**：

| Subject | item_id% | model:item% | G_item | acc | 类别 |
|---------|----------|-------------|--------|-----|------|
| international_law | 57.71% | 27.01% | 0.8905 | 0.77 | HUM |
| clinical_knowledge | 57.68% | 31.98% | 0.8742 | 0.62 | OTHER |
| world_religions | 46.15% | 22.47% | 0.8703 | 0.86 | HUM |
| computer_security | 41.53% | 27.58% | 0.8408 | 0.80 | STEM |
| philosophy | 41.25% | 28.12% | 0.8362 | 0.84 | HUM |
| college_physics | 39.53% | 31.35% | 0.8206 | 0.50 | STEM |
| us_foreign_policy | 31.91% | 46.34% | 0.7242 | 0.89 | OTHER |
| abstract_algebra | 19.56% | 42.12% | 0.6222 | 0.51 | STEM |
| high_school_math | 10.93% | 46.03% | 0.4516 | 0.41 | STEM |
| professional_medicine | 7.46% | 65.71% | 0.3057 | 0.81 | OTHER |
| **ALL MERGED** | **42.08%** | **33.64%** | **0.8200** | 0.70 | — |

**STEM vs Humanities 梯度**：STEM mean item_id% = 27.89%, Humanities mean = 48.37%。Humanities 科目的 item 方差占比更高（题目本身差异主导），STEM 科目的 model×item 交互更大（模型对不同题的差异表现更不一致）。

注：修正了之前分析中 G_item 的计算 bug（residual 需除以所有非 item facet 的 level 乘积），G_item 从全 0 修正到 0.31–0.89 的合理范围。

---
