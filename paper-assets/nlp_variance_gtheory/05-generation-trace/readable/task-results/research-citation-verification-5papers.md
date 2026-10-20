# research citation verification 5papers

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_verification_5papers_20260522T033438_result.json`
- **Structured JSON:** [`cb3c9441940b6f3a6405.json`](../../sessions/cb/cb3c9441940b6f3a6405.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，汇总如下。

---

### [1] Mesting (2026) — G-theory applied to LLM evaluation

- **状态：不存在**
- 实际标题：N/A
- URL：N/A
- 方法论摘要：N/A
- **风险：可能幻觉** — 搜索了 Mesting / Messing / Masting 多种拼写，均无结果。用 "generalizability theory LLM evaluation 2026" 宽泛搜索也未找到匹配作者。最接近的是 arXiv:2507.19980（2025年7月），将 G-theory 应用于 LLM 写作评分，但作者不是 Mesting，且研究场景不同（教育评估而非 benchmark variance）。

---

### [2] Madaan et al. (2024) arXiv:2406.10229

- **状态：存在，标题完全匹配**
- 实际标题：Quantifying Variance in Evaluation Benchmarks
- URL：[https://arxiv.org/abs/2406.10229](https://arxiv.org/abs/2406.10229)
- 方法论摘要：定义并测量 LLM 评测基准中的多种方差指标（seed variance、训练过程单调性等），在大量开源和自训模型上提供实证估计。
- 风险：无

---

### [3] arXiv:2601.02370 (2026) — "Variance-Aware LLM Annotation"

- **状态：存在，标题部分匹配**
- 实际标题：**Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement**
- URL：[https://arxiv.org/abs/2601.02370](https://arxiv.org/abs/2601.02370)
- 方法论摘要：识别 LLM 标注中的 5 类方差来源（construct specification、interface effects、model preferences、output extraction、system-level aggregation），实证显示 prompt 措辞等微小设计选择可使结果偏移 12–85 个百分点，提出 variance-aware 协议。
- 风险：标题偏差（声称的短标题是实际标题的缩写，内容匹配）

---

### [4] arXiv:2602.15532 (2026) — "Quantifying Construct Validity in LLM Evaluations"

- **状态：存在，标题基本匹配**
- 实际标题：**Quantifying construct validity in large language model evaluations**
- URL：[https://arxiv.org/abs/2602.15532](https://arxiv.org/abs/2602.15532)
- 方法论摘要：分析 LLM benchmark 的构念效度问题，指出 latent factor models 忽略 scaling laws（导致提取的能力维度代理了模型大小），scaling laws 忽略测量误差（导致过拟合），两种方法均不足以验证构念效度。
- 风险：无（仅大小写差异）

---

### [5] arXiv:2505.08245 (2025) — "Large Language Model Psychometrics: A Systematic Review"

- **状态：存在，标题部分匹配**
- 实际标题：**Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement**
- URL：[https://arxiv.org/abs/2505.08245](https://arxiv.org/abs/2505.08245)
- 方法论摘要：系统综述 LLM 心理测量学交叉领域，涵盖心理测量工具/理论/原则如何用于评估、理解和增强 LLM。
- 风险：标题偏差（声称标题省略了副标题后半部分，内容匹配）

---

## 汇总表

| # | 声称引用 | 状态 | 标题匹配 | 风险 |
|---|---------|------|---------|------|
| 1 | Mesting (2026) | **不存在** | N/A | **可能幻觉** |
| 2 | Madaan et al. (2024) 2406.10229 | 存在 | 完全匹配 | 无 |
| 3 | 2601.02370 (2026) | 存在 | 缩写匹配 | 低（标题偏差） |
| 4 | 2602.15532 (2026) | 存在 | 基本匹配 | 无 |
| 5 | 2505.08245 (2025) | 存在 | 缩写匹配 | 低（标题偏差） |

**结论：Mesting (2026) 高度疑似幻觉引用，建议删除或替换。** 如需一篇将 G-theory 应用于 LLM 评估的真实引用，最接近的候选是 arXiv:2507.19980（Exploring LLM Autoscoring Reliability Using Generalizability Theory, 2025），但其场景是教育写作评估而非 benchmark variance。

Sources:
- [arXiv:2406.10229 — Quantifying Variance in Evaluation Benchmarks](https://arxiv.org/abs/2406.10229)
- [arXiv:2601.02370 — Variance-Aware LLM Annotation](https://arxiv.org/abs/2601.02370)
- [arXiv:2602.15532 — Quantifying construct validity in LLM evaluations](https://arxiv.org/abs/2602.15532)
- [arXiv:2505.08245 — Large Language Model Psychometrics](https://arxiv.org/abs/2505.08245)
- [arXiv:2507.19980 — Exploring LLM Autoscoring Reliability Using Generalizability Theory](https://arxiv.org/abs/2507.19980)

---
