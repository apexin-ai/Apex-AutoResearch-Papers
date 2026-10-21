# analysis within mmlu subject gradient

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_within_mmlu_subject_gradient_20260521T093652_result.json`
- **Structured JSON:** [`f9118e8a92d6e56dd873.json`](../../sessions/f9/f9118e8a92d6e56dd873.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Task 8 完成。输出写入 `results/analysis/within_mmlu_subject_gradient.json`。

关键发现：

| Subject | Acc | item_id% | model×item% |
|---|---|---|---|
| professional_medicine | 0.810 | **7.5%** | **65.7%** |
| high_school_mathematics | 0.415 | 10.9% | 46.0% |
| abstract_algebra | 0.510 | 19.6% | 42.1% |
| us_foreign_policy | 0.893 | 31.9% | 46.3% |
| college_physics | 0.501 | 39.5% | 31.4% |
| computer_security | 0.796 | 41.5% | 27.6% |
| philosophy | 0.837 | 41.2% | 28.1% |
| world_religions | 0.861 | 46.1% | 22.5% |
| clinical_knowledge | 0.620 | 57.7% | 32.0% |
| international_law | 0.772 | 57.7% | 27.0% |

- **item_id% 跨 subject 梯度巨大**：从 7.5%（professional_medicine）到 57.7%（clinical_knowledge / international_law），CV=0.48
- **但不随 accuracy 线性变化**：Pearson r=0.301 (p=0.399)，无统计显著性
- **model×item 交互同样有大梯度**：22.5%–65.7%，range=43.2%
- **professional_medicine 是极端异类**：item_id 主效应仅 7.5%，但 model×item 高达 65.7%——说明不同模型对哪些题目难/易的判断高度分歧，item 难度几乎完全是 model-dependent 的

---
