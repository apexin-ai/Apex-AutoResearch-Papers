# research consistency vs correctness lit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_consistency_vs_correctness_lit_20260516T220603_result.json`
- **Structured JSON:** [`91b231fe79dc7a23adb3.json`](../../sessions/91/91b231fe79dc7a23adb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是结果摘要。

---

## 最相关论文（5篇）

**1. Self-Consistency Falls Short!** (Byerly & Khashabi, 2024, [TACL](https://arxiv.org/abs/2411.01101))
- 最强验证。证明 positional bias 导致 correlated errors 时，self-consistency 放大错误而非纠正。他们的 "position bias → correlated errors" 与我们的 "type semantic overlap → systematic misclassification" 机制不同但失败模式相同。

**2. Consistency–Accuracy Correlation in IE** (2025, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/))
- IE 领域直接验证。在 EPOP 语料（实体+关系抽取）上测 4 个 LLM，发现 **high consistency ≠ high accuracy**，相关性 model-dependent 且随 task complexity 变化。

**3. Beyond Majority Voting: SCOPE** (2024, [arXiv](https://arxiv.org/abs/2512.15146))
- 提出解决方案：用 step-wise confidence 加权替代 equal voting + dynamic subgroup partitioning 打破 error correlation。

**4. Diversified Sampling Improves Scaling LLM Inference** (2025, [arXiv](https://arxiv.org/abs/2502.11027))
- 同一 prompt 反复 sampling → outputs trapped in local cluster。用 diversified prompts 打破 correlation，提升 coverage。

**5. Hidden Strength of Disagreement** (Wu & Ito, 2025, [EMNLP](https://aclanthology.org/2025.emnlp-main.772/))
- 形式化 consensus-diversity tradeoff。显式 voting 有 premature homogenization 风险，隐式 consensus 保留 diversity 反而更优。

---

## 关键回答

**有没有人解决过 "高一致性但系统性错误"？**
有三条技术路线：(1) confidence weighting 替代 raw agreement；(2) diversified prompting 打破 error correlation；(3) subgroup partitioning 保持组间 diversity。但 **没有** 专门针对 structured IE (NER/RE) 中 self-consistency failure 的系统研究——这是我们的 contribution gap。

**对我们的启示：**
- 论文 Discussion 引用 Byerly & Khashabi 说明这是 general failure mode，我们在 IE 领域首次展示
- 可探索 confidence-weighted consistency 或 diversified prompting 作为改进方案
- 我们的 structural signals 本质上是 explicit consensus measures，当 systematic bias 存在时正好触发 premature homogenization

完整调研已保存到 `memory.md`。

---
