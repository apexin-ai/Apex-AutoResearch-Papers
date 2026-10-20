# analysis model as fixed

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_model_as_fixed_20260521T085703_result.json`
- **Structured JSON:** [`e082846bd1fa49db58cd.json`](../../sessions/e0/e082846bd1fa49db58cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Output saved to `results/analysis/model_as_fixed_gstudy.json`.

## 结果

| 设计 | G_item | 95% CI |
|------|--------|--------|
| Model=random (原始) | **0.820** | [0.782, 0.861] |
| Model=fixed, Method A (per-model avg) | **0.963** | [0.957, 0.969] |
| Model=fixed, Method B (移除 model:item) | **0.981** | [0.975, 0.985] |

**Per-model G_item**:
- gemma-2-9b-it: 0.971
- llama-3.1-8b-instruct: 0.958
- mistral-7b-instruct-v0.3: 0.956
- qwen3-8b: 0.968

**关键发现**：
- Fixed-model G_item 比 random 高 +0.143 (Method A) / +0.161 (Method B)，因为 model:item_id 占总方差 33.6% — 当 model 为 fixed 时这部分不计入测量误差
- Method B > Method A，因为 B 用的是 6-facet 残差（被更多条件平均，更小），而 A 用的是 per-model 5-facet 残差（更大）
- Item ranking 跨模型一致性中等（mean Spearman ρ = 0.642），说明 model:item 交互不可忽略 — 支持 random-model 作为更保守的报告选择

---
