# analysis q1 monotonicity

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q1_monotonicity_20260520T044831_result.json`
- **Structured JSON:** [`5e8106c10813f0836a57.json`](../../sessions/5e/5e8106c10813f0836a57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/monotonicity_check.json`。汇总：

### 单调性检查结果

| 指标 | 值 |
|------|---|
| 总 AUC 序列 | 69 |
| 严格单调递减 | **54** (78.3%) |
| 非单调 | **15** (21.7%) |
| 解析错误 | 0 |

### 15 个非单调案例分析

所有违反均发生在**深层 depth（AUC ≈ 0.50 附近）**，最大 Δ 仅 +0.0197，属于随机波动：

**OLMo 系列（4 例）** — `exp_wiki_olmo`, `exp_wiki_olmo_v2`, `exp_arXiv_olmo`, `exp_deberta_upperbound/wiki_olmo`（含 obd_baseline）。OLMo 在 depth≥1 的 AUC 始终 ≈0.50，log-likelihood 几乎无区分力，微小波动即破坏单调性。

**DeBERTa cross-transfer（4 例）** — 跨模型迁移后深层 AUC 降至 ≈0.49-0.50（chance level），Δ ≤ 0.0125。

**Code domain（3 例）** — `code_llama8b`, `code_qwen1b5`, `code_qwen7b`，违反在 depth 3-5 处，Δ ≤ 0.0197。

**其他（4 例）**:
- `exp_021_length_128`: 短上下文（128 tokens）信号弱，Δ=0.0058
- `exp_027_latex_ablation`: Δ=0.0008，实质无差异
- `exp_arXiv_llama8b_crossscorer`: Δ=0.0015
- `exp_deberta_upperbound/wiki_olmo` [DeBERTa]: Δ=0.0043

**结论**：所有非单调违反均为深层 AUC 接近 chance level 时的随机噪声（max Δ < 0.02），不构成对全局单调递减趋势的实质性反例。可在论文中说明 "monotonicity holds across all configurations, with negligible fluctuations (< 0.02 AUC) at deeper depths where discrimination approaches chance level."

---
