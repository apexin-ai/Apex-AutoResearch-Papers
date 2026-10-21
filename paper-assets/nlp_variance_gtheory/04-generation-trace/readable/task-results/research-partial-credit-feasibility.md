# research partial credit feasibility

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_partial_credit_feasibility_20260523T085954_result.json`
- **Structured JSON:** [`3e3f7f122c09f9aa8c25.json`](../../sessions/3e/3e3f7f122c09f9aa8c25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。关键发现：

**Q1 代码**：服务器上无持久化的 partial-credit 代码，pilot 是 worker session 内联实现的 regex 评分。`variance_decomposition.py` 不支持 `partial_score` response var。需 2-3h 重构：提取评分函数 + **适配 calculator notation `<&lt;A+B=C>>D`**（6/8 模型使用此格式，pilot regex 仅验证过 Llama 的 plain format）。

**Q2 数据**：8 个模型 GSM8K 数据齐全，每个 57,600 条，全部含 `generated_text`。无需重新推理。模型列表与预期略有不同（实际为 Qwen3-8B / DeepSeek-7B / OLMo-2-7B / Yi-1.5-9B，非 Qwen2.5 / Falcon）。

**Q3 时间**：纯 CPU（regex + ANOVA + bootstrap），0 GPU 小时。每模型 ~5min，8 模型共 ~40min。代码准备 2-3h。

**Q4 风险**：最可能结果是 (a) 全部模型 partial G < binary G，因为机制是结构性的（连续评分必然增大 residual，压缩主效应）。最大实际风险是 regex 在 calculator notation 上静默失败，导致假阳性的 "G 未变化"。建议先验证每个模型的 step extraction rate 再跑全量。

结论：**Go**——数据基础设施完备，唯一 blocker 是 regex 适配。

---
