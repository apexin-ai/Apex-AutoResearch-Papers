# ssh i diversity predictor

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_i-diversity-predictor_20260520T101451_result.json`
- **Structured JSON:** [`e3122e6f2dc91f149e14.json`](../../sessions/e3/e3122e6f2dc91f149e14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**模型配对**: Qwen3-8B-FT vs Qwen2.5-72B-fewshot（原始 LLaMA FT 数据已不存在，改用此对）

**SciERC** (n=529):
| 指标 | Spearman ρ vs ΔF1 | p-value |
|------|-------------------|---------|
| JSD | -0.310 | 2.9e-13 |
| Cross-model div | -0.295 | 4.2e-12 |
| EU Jaccard | +0.177 | 4.1e-05 |
| Within-A div | +0.062 | n.s. |
| Within-B div | -0.029 | n.s. |

OLS: JSD R²=0.30, div_cross R²=0.27

**CoNLL** (n=2756):
| 指标 | Spearman ρ vs ΔF1 | p-value |
|------|-------------------|---------|
| JSD | -0.615 | ~0 |
| Cross-model div | -0.640 | ~0 |
| EU Jaccard | +0.576 | ~0 |

OLS: JSD R²=0.74, div_cross R²=0.73

**核心发现**: Cross-model 输出分歧（JSD、cross-model diversity）强预测 SC 混合构造的 ΔF1。模型间越不一致，混合 majority vote 越伤害性能。Within-model diversity 不显著。CoNLL 上效应远强于 SciERC（R² 0.74 vs 0.30），因为 CoNLL 任务更规范、模型间一致性差异更结构化。

产出路径:
- `artifacts/i_diversity_predictor/diversity_correlation.json`
- `artifacts/i_diversity_predictor/diversity_per_instance.json`
- `code/i_diversity_predictor.py`

---
