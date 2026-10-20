---
round: 1
overall_score: 3.0 - Findings
timestamp: 2026-05-18T01:49:05.406319+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告：The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting

**目标 venue**: EMNLP 2026 (ARR May cycle)
**审稿轮次**: Round 2（论文修订后重新审稿）
**Reviewer 编排**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性）
**交叉分享**: 完成，两位 Reviewer 均提交了逐条回应

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理轨迹中自提取 FOL 约束，通过 weighted partial MAX-SAT 聚合答案，旨在改进 Self-Consistency (SC) 的多数投票。在 6 个模型（7B-32B）、3 个推理领域、超过 1,500 个实例上，SICA 相比 SC 无统计显著提升（Δ 范围 -3.3 至 +3.3 pp）。Oracle 实验用 gold FOL 注释替代自提取，获得 +8.82 pp（p < 0.001），证明聚合机制本身有效，瓶颈在自提取质量。作者将此命名为"capability trap"，提出 C0 诊断指标作为从业者工具。

---

## Strengths

**S1. Oracle control 实验设计精巧 [R1, R2 共识]**
通过 component-level intervention 隔离自提取质量与聚合机制，遵循 Press et al. (2023)、Trivedi et al. (2023) 的 established methodology。+8.82 pp 的显著提升（McNemar p = 6.15e-5）是全文最有力的证据，方法论设计值得肯定。

**S2. 统计方法严谨完整 [R1, R2 共识]**
McNemar test + 10,000 次 bootstrap CI + power analysis（MDE 计算）构成三层统计论证链。n≤60 条件明确标注为 exploratory。这对负面结果论文尤为重要。

**S3. Constraint ablation 有说服力 [R1, R2 共识]**
MAX-SAT vs count-only 在 804 个预测中一致 803 个（Table 2），直接证明满足性求解器退化为计数。Random-weight 变体进一步确认约束无判别信号。

**S4. C0 diagnostic 有实用价值 [R1, R2 共识]**
定义简洁，零成本可计算，双向论证完整（低 C0 退化 + 高 C0 不保证改进）。QwQ-32B C0=2.6% vs DeepSeek-R1-7B C0=58.3% 的对比清晰展示 reasoning model 特殊行为。

**S5. Limitations section 诚实全面 [R1]**
列出 7 项具体限制，未过度推广结论。

**S6. 写作质量整体较高 [R2]**
Abstract 简洁回答四个核心问题，Introduction 叙事线完整，Related Work 6 段分类合理、positioning 诚实。

---

## Weaknesses

### Must-Fix（3 项）

**W1. σ(c, a) 的 Z3 评估机制描述不完整，影响 soundness 判断 [R1 提出, R2 AGREE]**
- Section 3.3 Eq.(2) 定义 σ(c, a) 为"Z3 determines: σ(c, a) = 1 if constraint c is satisfiable under the assignment implied by answer a"，但未具体说明 answer a 如何为 Z3 创建 variable assignment。
- Appendix 的 prompt 显示 domain constraints 使用独立变量（如 kind_anne），answer assertion 使用独立变量（__sica_answer_True）。如果两者无逻辑桥接，则 σ(c, a) = 1 对所有 a 恒成立，SICA 在数学上严格退化为 SC。
- R2 进一步指出：803/804 agreement 恰好验证了这一假设。如果退化是 mechanism 设计问题而非 model capability 问题，则"capability trap"的归因需要重新定义。
- **影响**: 这是 soundness 核心问题。无法判断论文的核心发现是"模型无法产生 discriminative constraints"还是"评分机制设计上就无法利用 constraints 进行区分"。
- **要求**: 补充完整的 Z3 evaluation 流程伪代码，明确 domain constraint 变量和 answer 变量之间的关系。

**W2. Oracle 实验仅限 FOLIO 单一数据集（n=204），因果论证的外部效度不足 [R1, R2 共识]**
- 核心因果论证完全依赖 FOLIO 一个数据集的 oracle 实验。
- FOLIO 是形式逻辑领域，约束天然以 FOL 表达。对 commonsense（StrategyQA）或 science（ARC）域的 constraint extraction 能否同样受益于 oracle 完全未知。
- "the aggregation mechanism is sound" 的一般性结论由单数据集 oracle 支撑不足。
- ProofWriter 也有结构化 proof chain 和 ground-truth labels，理论上可以构造 oracle constraints。
- **要求**: 至少增加一个域的 oracle 验证（如 ProofWriter），或将 claim 范围限定为 formal logic。

**W3. 核心概念"Capability Trap"与已有工作重叠，新颖性不足 [R2 Must-Fix, R1 Should-Fix]**
- "同一模型无法有效验证/纠正自身推理"已被以下工作明确建立：
  - Huang et al. (ICLR 2024): LLM 在无外部反馈时无法自纠错
  - **Stechly, Valmeekam & Kambhampati (ICLR 2025)**: self-verification 导致性能崩溃，sound external verification 有效，self-generated critique 内容无实质影响。这与本文发现结构同构。
- R1 认为可降为 Should-Fix，理由是本文的实证贡献（oracle 设计、ablation、C0）独立于概念命名。R2 认为概念层面的重叠构成对 main conference 接收的实质障碍。
- **Director 判断**: 作为 Findings track 论文，实证贡献可成立。但必须引用 Stechly et al. 并明确差异化（NL self-critique vs formal constraint extraction + satisfiability solving）。

### Should-Fix（7 项）

**W4. 手动约束质量分析样本过小 [R1, R2 共识]**
- 11.5% discriminative rate 来自 43 problems（23 multi-candidate），仅覆盖 Qwen2.5-14B 在 FOLIO+PW 上。该数字在 Abstract/Intro/Conclusion 均被引用作为核心证据，但 CI 极宽。
- 建议扩大到 100+ 问题覆盖多模型，或设计自动化指标，或限定 claim 范围。

**W5. 7/11 conditions n≤60，广度声称需更审慎 [R1, R2 共识]**
- 真正 confirmatory 的仅 3 组分析（n=804, n=200, n=204）。
- LLaMA StrategyQA 95% CI 上界 +5.5pp，无法排除 practically meaningful 正向效应。
- Abstract/Conclusion 中"across six models and three domains"措辞需区分 confirmatory 和 exploratory evidence。

**W6. 未测试替代提取策略 [R1, R2 共识]**
- 仅使用单一 zero-shot prompt + T=0.1 提取约束。
- "Cannot improve"的标题级 claim 需至少排除 few-shot extraction 等替代方案。
- Limitations §5 承认但未尝试，对负面结果论文来说是显著缺陷。

**W7. "Five model families"表述有误导性 [R1, R2 共识]**
- QwQ-32B、Qwen2.5、DeepSeek-R1-Distill-Qwen-7B 均基于 Qwen 架构。
- 实际独立架构可能仅 3 个（Qwen 系、Mistral、LLaMA）。
- 需区分 architecture family 与 release/training family。

**W8. Related Work 遗漏关键引用 [R1, R2 共识]**
- **Stechly et al. (ICLR 2025)** "On the self-verification limitations of LLMs on reasoning and planning tasks": 最直接的先行工作，必须引用。
- Ai et al. (2025) "Beyond Majority Voting": 不依赖形式化的 aggregation 改进。
- Valmeekam et al. (2023) "Can LLMs Really Improve by Self-Critique?": self-refinement 负面结果。
- Beirami et al. (2024): Best-of-N / reward model reranking。

**W9. StrategyQA/ARC extraction prompt 未在 Appendix 文档化 [R2 提出, R1 AGREE]**
- Appendix Prompt Selection Logic 仅覆盖 FOLIO/PW（Logic prompt）和 GSM8K/AIME（Math prompt），未说明 StrategyQA 和 ARC 使用了哪个。
- 如果对 commonsense 推理使用了 logic extraction prompt，prompt-domain mismatch 本身可能是额外的 confounding factor。

**W10. 未测试 70B+ 模型，削弱"cannot"的普遍性 [R2 提出, R1 认为 Minor]**
- 所有模型 7B-32B。Limitations 已承认，但标题中的"Cannot"暗示普遍性。
- 建议软化标题/Abstract 措辞以限定范围，或增加一个 70B+ 模型验证。

### Minor（2 项）

**W11. Table 1 小数精度不统一**: QwQ-32B 为 72.7（一位小数），其余两位。需统一。

**W12. 48.7% pipeline time claim 缺乏方法学细节**: 未说明测量硬件、条件和方法。

---

## Reviewer Consensus [AGREE]

以下关键问题两位 Reviewer 达成共识：
1. Oracle 仅限 FOLIO 是核心缺陷 [R1-W2, R2-W3, 双方 AGREE]
2. σ(c, a) 机制描述不完整影响 soundness [R1-W1, R2 AGREE, 可能将 capability trap 重新归因为设计缺陷]
3. 手动分析样本过小（43 problems）[R1-W3, R2-W5, 双方 AGREE]
4. 7/11 conditions 功效不足，广度声称需更审慎 [R1-W4, R2-W2, 双方 AGREE]
5. Stechly et al. (ICLR 2025) 是最关键遗漏引用 [R2-W4, R1 AGREE]
6. StrategyQA/ARC 的 prompt assignment 需文档化 [R2-W9, R1 AGREE]

## Reviewer Divergence [REBUT]

以下问题两位 Reviewer 存在分歧：
1. **新颖性严重程度**: R2 认为 Must-Fix（概念层面与 Stechly et al. 同构），R1 认为 Should-Fix（实证贡献独立于概念命名）。Director 判断：引用 Stechly et al. + 差异化讨论足以解决，不需要重新定义贡献。
2. **理论形式化需求**: R2-W7 要求更严格的理论建模（如 information-theoretic）。R1 反驳：Eq.(3) + ablation 已提供足够数学支撑，对实证论文要求 formal proof 是标准提升。Director 判断：同意 R1，当前数学描述层级适当。
3. **AI 写作痕迹**: R2-W8 泛泛指出"少量 AI 痕迹"。R1 反驳：缺乏具体示例，不可操作。Director 判断：同意 R1，不列为正式 weakness。

---

## Questions

**Q1 [R1, R2]**: σ(c, a) 中 answer a 如何影响 domain constraint 的 Z3 满足性？若 domain 变量和 answer 变量在 Z3 中独立，SICA 是否严格退化为 SC？请提供 Z3 evaluation 的完整伪代码。

**Q2 [R2]**: 对于 StrategyQA 和 ARC-Challenge，具体使用了哪个 extraction prompt？如果是 logic prompt，是否考虑过 domain-mismatch 作为额外 confounding factor？

**Q3 [R1, R2]**: Oracle 实验中 Z3 checks 与 gold labels 不一致的 11/204 问题（5.4% error rate）的原因是什么？如果 oracle 本身有误差，实际可恢复上界可能高于 +8.82 pp。

**Q4 [R2]**: 不同 trace 对同一 answer 可能生成不同 constraints（within-answer diversity）。这种随机性是否可以被利用？

**Q5 [R2]**: 在 n=5000 下，+1.5 pp 效应是否可检测？如果可检测，考虑到 48.7% 的 pipeline 时间开销，是否 cost-effective？论文是否应在 Discussion 中讨论 cost-benefit 阈值？

**Q6 [R1]**: 803/804 agreement 是否在其他 conditions（如 LLaMA-8B）上也成立？还是仅限于 Qwen2.5-14B？

**Q7 [R1]**: 提取温度 T=0.1 是否导致约束过度确定性？更高温度的提取是否可能产生更多样的约束？

---

## Missing References

1. **[Must-Cite] Stechly, Valmeekam & Kambhampati (ICLR 2025)** "On the self-verification limitations of large language models on reasoning and planning tasks" — self-verification fails, external verification works. 与本文 oracle 设计结构同构。
2. **[Should-Cite] Ai, Pan, Simchi-Levi, Tambe & Xu (2025)** "Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information" — 不依赖形式化约束的 aggregation 改进。
3. **[Should-Cite] Valmeekam et al. (2023)** "Can LLMs Really Improve by Self-Critique?" — self-refinement 负面结果先驱。
4. **[Optional] Beirami et al. (2024)** — Best-of-N / reward model reranking 比较。
5. **[Optional] Wang et al. (2025)** "Auditing Multi-Agent LLM Reasoning Trees" (AgentAuditor) — evidence-based selection。
6. **[Optional] Li et al. (2025)** "Debate or Vote" — majority voting 已捕获 debate 大部分收益。

---

## External Review (Stanford Agentic Reviewer)

未配置。项目 config 中无 external_review.paperreview_ai.enabled 设置。

---

## Overall Assessment

- **Overall Score**: 3.0 / 5 (Findings)
  - 按 EMNLP 2026 ARR 评分标准：可被 Findings 接收
- **Soundness**: 3.0 / 5
  - σ(c, a) 机制描述不完整构成 soundness 风险；oracle 单数据集限制因果论证的外部效度
- **Excitement**: 2.5 / 5
  - 负面结果有参考价值，但概念新颖性受 Stechly et al. 限制
- **Reproducibility**: 3.0 / 5
  - 统计方法透明，但 σ(c, a) 机制和 StrategyQA/ARC prompt 缺失影响复现
- **Confidence**: 4.0 / 5
  - 两位 Reviewer 均对 neuro-symbolic 和 self-correction 文献熟悉

**总评**:

这是一篇实验设计扎实的负面结果论文。核心优势在于 oracle control 的因果隔离设计和完整的统计论证链（McNemar + bootstrap CI + power analysis）。Constraint ablation（803/804 agreement）和 C0 diagnostic 对从业者有直接参考价值。

主要问题：(1) σ(c, a) 的 Z3 evaluation 机制描述不完整，无法排除 SICA 退化为 SC 是设计缺陷而非模型能力限制的可能性，这直接影响 "capability trap" 归因的 soundness；(2) Oracle 因果论证仅限 FOLIO 一个数据集，不足以支撑跨域的一般性结论；(3) "capability trap" 概念与 Stechly et al. (ICLR 2025) 的 self-verification limitation 存在结构同构性，需明确差异化。

**建议处理优先级**:
1. [Critical] 补充 σ(c, a) Z3 evaluation 的完整伪代码，明确 domain-answer 变量关系
2. [Critical] 扩展 oracle 到至少一个额外数据集（ProofWriter），或限定 claim 范围
3. [Critical] 引用 Stechly et al. (ICLR 2025)，明确差异化定位
4. [Important] 补充 StrategyQA/ARC 的 prompt assignment
5. [Important] 软化 Abstract/Conclusion 的广度措辞
6. [Important] 修正 "five model families" 表述

如果 W1-W3 得到充分解决，本文适合 EMNLP 2026 Findings 发表。当前状态下，soundness 存疑（σ(c,a) 机制）和概念新颖性不足阻碍主会议接收。

---

*报告由 Review Director 基于 Reviewer 1（方法严谨性）和 Reviewer 2（新颖性/完整性）的独立审稿及交叉回应汇总生成。*
