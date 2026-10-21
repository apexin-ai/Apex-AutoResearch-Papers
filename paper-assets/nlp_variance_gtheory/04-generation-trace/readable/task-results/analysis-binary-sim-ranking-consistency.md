# analysis binary sim ranking consistency

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_binary_sim_ranking_consistency_20260522T084119_result.json`
- **Structured JSON:** [`bf9cbc22e3ffbae4a26d.json`](../../sessions/bf/bf9cbc22e3ffbae4a26d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到服务器和本地。汇总：

**100 次 Bernoulli probit 模拟（8-model MMLU 设计）**

| 指标 | 值 |
|------|-----|
| **Top-3 集合一致率** | **100%** — 永远是 {item_id, model:item_id, residual} |
| **Top-3 排序一致率** | 0% — residual 被 Bernoulli 噪声膨胀到 #1 |
| **Top-1 一致率** | 0% (含 residual), 48% (排除 residual) |
| **Kendall's τ** | 0.814 ± 0.059 (全排序), 0.814 ± 0.065 (去 residual) |

**关键发现**：
- Residual 在二值尺度上从观测的 25.0% 膨胀到模拟的 47.5%（吸收了 Bernoulli 内部方差）
- item_id 和 model:item_id 被压缩到各 ~24%，在 #2/#3 位置上约 50/50 竞争
- **但 top-3 集合 100% 一致** — Henderson I 可靠地识别出正确的三个主要方差来源
- 真实数据中 item_id > model:item_id > residual 的排序说明真实的 item difficulty 结构足够强，克服了 Bernoulli 膨胀效应

---
