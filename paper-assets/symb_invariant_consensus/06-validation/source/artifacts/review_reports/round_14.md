---
round: 14
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T09:39:17.381201+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 17 (Fresh) 审稿报告

**论文**: "Beyond Self-Consistency: Self-Extracted Constraints Do Not Substantially Improve LLM Logical Reasoning"
**Venue**: EMNLP 2026 via ACL Rolling Review
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）
**交叉分享**: 完成，1 轮收敛

---

## Summary

本文引入 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束并通过加权 MAX-SAT 聚合答案。在 6 个模型（7B–32B）、3 个推理领域上，SICA 与多数投票结果在 94.4% 的问题上一致，无条件显示显著正向效果（BH 校正后）。论文将此归因于 "Symbolic Confirmation Bias"（SCB），通过 Proposition 1（Source-Attribution Degeneration）和 Corollary 1（DPI Information Ceiling）形式化。27 个 training-free 变体均产生中性至负面结果。三个零成本诊断指标（C₀, BR, K_eff）在 60 个条件上 100% 分类。跨架构验证（DeBERTa NLI）在弱生成器上展示逃逸可能。

---

## Strengths

**S1. 实验规模与方法论严谨性。** 9 个模型（含 frontier）、3 个推理域、27 个 training-free 变体的系统覆盖。统计方法完备：TOST 等价性检验、McNemar + BH 校正、bootstrap CI、功效分析。这是该领域最系统的 negative result 研究之一。[R1-S1, R2-S1]

**S2. 因果分析链条清晰。** 从现象（SICA ≈ SC）→ 机制（trace-count 分布决定约束分布）→ 理论（DPI Markov chain）→ 逃逸条件（跨架构独立性），层层递进。Figure 3 因果 DAG 和 Figure 1 pipeline 图有效辅助理解。[R1-S2, R2-S3]

**S3. Oracle 对照设计精确定位瓶颈。** Gold FOL 替换自提取约束后 MAX-SAT 产生 +29.91pp 增益（Appendix G），明确瓶颈在约束提取而非求解器，避免了对 MAX-SAT 机制的混淆。[R1-S3]

**S4. 诊断框架具有实际潜力。** C₀、BR、K_eff 三个指标可在 pilot run 中预估 self-extraction 方法的前景，对从业者有指导意义——尽管 100% accuracy 声称需要软化（见 W3）。[R2-S2]

**S5. 诚实的统计报告。** 论文坦承 10/16 条件统计功效不足、模型范围局限、multi-seed 覆盖不完整。这种透明度在 negative result 论文中值得肯定。[R1-S5, R2-S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1** [critical, 共识] **Proposition 1 证明存在关键逻辑跳跃。**
证明直接声称 "score(a) = Σ 1[aᵢ = a] = nₐ"，但 SICA 的实际评分函数（Eq. 3）涉及约束权重 wc（去重后 trace 计数）和源归属指示函数 σ(c,a)。从 Eq. 3 到 score(a) = nₐ 需要证明：(1) 退化条件下 |C⁻| ≈ 0；(2) 不同答案组约束不重叠；(3) 42.9% 去重率下权重分布使 Σwc 精确等于 nₐ 而非仅成比例。R2 补充：比例关系可能保持 argmax 但精确等式不成立。Proposition 1 是全文理论框架的基石，证明不完整使理论贡献从 "形式化证明" 降级为 "经验观察"。
**修复方向**: (a) 完善证明列出所有假设；或 (b) 弱化为 argmax preservation（ranking 保持）；或 (c) 补充经验 rank agreement 验证。
[R1-N1 提出, R2 fully AGREE]

**W2** [critical, 共识] **标题/Abstract 的全称否定与统计证据不匹配。**
标题 "Do Not Substantially Improve" 和 Abstract 的 "We show the answer is no" 是全称判断，但 TOST 仅 4/16 条件确立等价（±2pp），10 条件 underpowered（power < 21%, MDE ≥ 1.86pp）。论文无法区分 "SICA 无效" 和 "样本不够大"。GSM8K (n=30) 和 AIME (n=22) 在 Table 1 中与 n=200+ 条件无区分地并列，加剧误导。
**修复方向**: (a) 标题改为限定性表述（如 "Show No Significant Improvement"）；(b) Abstract 区分 confirmed-equivalent vs. underpowered/inconclusive；(c) Table 1 视觉标记 powered/underpowered 条件；(d) GSM8K/AIME 移至 Appendix 或标为 exploratory。
[R2-N1 提出, R1 fully AGREE]

**W3** [critical, 共识] **诊断框架 100% 准确率是 trivial 的。**
60 个条件全部为 null 或 negative，trivial "always predict no improvement" classifier 也能达到 100%。Holdout 验证仅 2 个模型系列（LLaMA-3.1-8B、Qwen3-14B），且同为 negative cases。框架的区分能力（discriminative power）未经正例验证。论文将此列为三大贡献之一，但无正例的框架无法预测何时 self-extraction *会* 有效。R2 精辟指出：框架的实际价值在于 failure mode 分类（退化型/多样性不足型/确认偏差型），而非二分类预测。
**修复方向**: (a) 改 "correctly classifies" 为 "correctly characterizes the failure mode"；(b) 用 §6 cross-arch escape 的 Mistral-7B 条件作 positive validation；(c) 定位为 "ruling-out tool" 而非通用诊断。
[R1-N3 提出, R2 fully AGREE]

**W4** [critical, 部分共识] **SCB 与已有 confirmation bias 工作的新颖性区分不充分。**
Wan et al. (2025) 已证明 CoT confirmation bias，SCB 可能是同一现象在 FOL/symbolic 载体上的实例化。论文 §2 仅一句区分（"symbolic confirmation bias is distinct from CoT unfaithfulness"），未充分对比。Jhaveri & Kersting (2026) 进一步削弱新颖性。R1 部分反驳：SCB 有独立的 aggregation-level 结构性区分——source-attribution scoring 退化是关于 aggregation mechanism 的形式化结论，非推理忠实性结论；且 94.4% 约束通过 Z3 验证说明问题不在约束不可靠而在不提供超越 trace 的信息。
**共识**: 需 1-2 段显式对比 Wan et al.，明确 SCB 的增量贡献在于 DPI 形式化和 source-attribution 机制，定位为 "complementary instance in formal verification" 而非全新概念。
[R2-N3 提出, R1 AGREE with nuance]

### Should-Fix（影响评分但不一票否决）

**W5** [warning, 共识] **Corollary 1 (DPI) 理论贡献度偏弱。**
I(C;Y) ≤ I(T;Y) 是 DPI 在 Markov chain T→C 上的直接应用，接近信息论教科书练习。贡献在于 Markov chain 建模识别而非推导。建议降级为 Remark。[R1-W1, R2-W1, 共识]

**W6** [warning, 共识] **Bias Ratio (BR) 缺少 null model 分解。**
60% trace 产生答案 a 时，纯随机约束-答案关联已产生 BR = 1.5。Table 2 的 BR 值（1.66×–4.97×）部分可能由 base rate 解释。需 permutation null model 量化 excess bias。即使 excess = 0，negative result 仍成立，但 "structural bias" 声称需 excess > 0。[R1-W2 提出, R2 fully AGREE]

**W7** [warning, 共识] **Cross-architecture escape (§6) 结论过度推断。**
仅 6 个 generator-verifier 条件，仅 Mistral-7B (SC=39.33%) 显著。Spearman ρ=1.0 (n=6) 鲁棒性低。"Capability-gap pattern" 数据不足。R2 补充：方向性发现有启示价值但不足以建立一般规律。建议措辞从 "confirming" 改为 "suggesting" 或 "preliminary evidence"。[R1-W3, R2 AGREE]

**W8** [warning, 共识] **α=0.5 sensitivity 分析实质上确认退化。**
Table 11 所有 α∈{0.1,...,1.0} 下 SICA-SC agreement ≥ 99%——这是 ceiling effect（|C⁻| ≈ 0 使 α 无关），非方法鲁棒性。论文应重新解释为退化的 corroborating evidence。[R1-W4, R2 AGREE]

**W9** [warning, 共识] **Scope 震荡。**
论文在 SICA-specific findings 和 general impossibility claims 之间摆动。Proposition 1 声称适用于 "any self-extraction pipeline"，但 27 个实验变体全在 SICA 范式内。建议在 §1 contributions 中明确界定实验覆盖的 scope 边界。[R2-W3, R1 AGREE with nuance]

**W10** [warning, 共识] **K_eff 可读性不足。**
K_eff = K/[1+(K-1)·κ] 对非 ensemble-theory 背景读者缺少直觉解释。建议添加具体示例（如 "K=12, κ=0.7 → K_eff ≈ 1.3"）。[R2-W4, R1 AGREE]

### Minor Issues

- **符号过载**: 正文 8 页内引入 BR, K_eff, C₀, κ, σ, α, Δ, score(a), CCR, ProcessSim 等。建议 CCR/ProcessSim 定义移至 Appendix。[R2]
- **Abstract 信息密度过高**: ~6 个核心发现压缩在一段。建议精简为中心 negative finding + 机制 + scope。[R2]
- **§2 段间衔接**: 三个子节间缺显式逻辑连接句。[R2]
- **Table 1 统计功效未标注**: 读者需翻 Appendix D 才发现 10/16 underpowered。[R1]
- **TOST ±2pp margin 缺先验依据**: 是领域惯例还是事后选择？存在 specification searching 风险。[R1-Q3, R2 AGREE]
- **Multi-seed 覆盖率**: 仅 2/6 模型有 multi-seed replication。[R1-W5, R2 REBUT：现有两模型方向一致，降级 nice-to-have]

---

## Reviewer Consensus

以下问题两位 Reviewer 完全达成一致（[AGREE]）：

1. **Proposition 1 证明不完整**——score(a) = nₐ 从 Eq. 3 推导缺关键步骤 [R1-N1, R2 AGREE]
2. **标题/Abstract overclaim**——10/16 underpowered，"We show the answer is no" 逻辑不一致 [R2-N1, R1 AGREE]
3. **诊断框架 trivial classifier 问题**——60 全阴性条件，框架价值在 failure mode 分类而非预测 [R1-N3, R2 AGREE]
4. **Corollary 1 近 trivial**——应降级 Remark [R1-W1, R2-W1]
5. **BR 缺 null model**——需 permutation 分解 base-rate vs. excess bias [R1-W2, R2 AGREE]
6. **Cross-arch 过度推断**——n=6 不够，"preliminary evidence" 而非 "confirming" [R1-W3, R2 AGREE]
7. **α sensitivity = 退化确认**——ceiling effect，非鲁棒性 [R1-W4, R2 AGREE]

## Reviewer Divergence

1. **SCB 新颖性**: R2 认为 SCB 是 CoT confirmation bias 的 FOL 实例化（critical），R1 部分反驳认为 SCB 有独立的 aggregation-level 贡献但同意需更充分对比。→ **部分共识**：需增加对比段落。

2. **Multi-seed 覆盖**: R1 认为 should-fix（Δ ∈ [-4.41, +3.43] 跨正负），R2 REBUT 降级 nice-to-have（现有两模型方向一致）。→ **轻微分歧**。

3. **"Symbolic Mirage" 术语**: R2 认为过度品牌化（minor），R1 REBUT 认为有技术对应物。→ **轻微分歧**：R1 建议保留术语但改 section title。

---

## Questions to Authors

**Q1.** Proposition 1 中 score(a) = nₐ 的精确等式如何从 Eq. 3 推导？特别是 42.9% 去重率导致权重不均匀，Σwc 与 nₐ 是等式还是比例关系？如果仅比例关系，argmax 保持是否有证明？

**Q2.** 诊断框架在 trivial "always predict negative" baseline 之上的附加值具体体现在哪里？是否可用 §6 cross-arch escape 条件做 positive validation？

**Q3.** TOST ±2pp margin 的先验依据是什么？高基线（SC ≥ 75%）下 2pp 相对效应量仅 ~2.7%，是否考虑按基线调整 margin？

**Q4.** Cross-architecture 实验中 α 是否固定 0.5？跨模型设置下约束不再完全耦合到生成器分布，α 敏感性可能不同。

**Q5.** Table 2 Gemini-2.5-Pro BR=12.19（n_err≈12）远高于其他模型——是 base-rate 效应还是 extraction 异常？

---

## Missing References

**共识引用建议**:
- Reflexion (Shinn et al., 2023) — self-reflection 范式，§2 简提
- LATS (Zhou et al., 2023) — tree-search self-verification，§2 简提
- Cohen's h 或标准化效应量 — 帮助读者理解 ±2pp 在不同基率下的意义

**已确认引用（不再遗漏）**:
- Kamoi et al. (TACL 2024) — 已引用 kamoi2024selfcorrect
- AlphaCode/CodeT — 已引用 li2022alphacode, chen2023codet
- S²R / DuPO — 已引用 zeng2025s2r, dupo2025

---

## External Review

**外部审稿（Stanford Agentic Reviewer）**: 未请求（项目未配置）。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成
**发现** (0 critical, 4 warning, 19 info):

- ✅ 正文恰好 8 页，符合 EMNLP 2026 页数限制
- ✅ Limitations 位于正文 conclusion 后、references 前，合规
- ✅ 主文 7 个 display items（Figure 1-4 + Table 1-3），密度 0.88/页，合理
- ✅ 所有 figure/table 出现在首次引用附近，无严重漂移
- ✅ 引用格式统一，无 [?] 未解析
- ✅ 散点图使用颜色+marker 形状双重编码，色盲友好
- ⚠️ Figure 4（p7）内部文字过小——打印/缩小后可读性差，建议精简或增大
- ⚠️ Appendix p16/p22 表格堆叠过密（各含 5 个表格），建议适当分页
- ⚠️ Appendix pp25-26 连续纯文本无 display item

---

## Overall Assessment

**Overall Score**: 3.0 — Findings

**评分理由**:

论文的实验工作量和方法论严谨性毋庸置疑——6 模型 × 3 域 × 27 变体的系统覆盖、Oracle 对照、multi-seed replication、完备的统计检验，这些在 negative result 研究中极为少见，值得肯定。

但三大贡献均存在实质性问题：

1. **Proposition 1**（理论贡献）——证明有逻辑跳跃，score(a) = nₐ 从 Eq. 3 推导不完整；Corollary 1 近 trivial。
2. **诊断框架**（实用贡献）——60 条件全阴性使 100% accuracy 等价于 trivial classifier；正例验证缺失。
3. **SCB 概念**（发现贡献）——与 Wan et al. (2025) CoT confirmation bias 的新颖性区分不充分。

加之标题/Abstract 的全称否定与统计证据（10/16 underpowered）不匹配，论文的 claim 强度系统性地超出了证据支持。

作为 negative result 论文，核心洞察可总结为 "self-extracted constraints inherit the model's distributional prior"——这在 Huang et al. (2024) 和 Wan et al. (2025) 之后非 entirely novel。论文的主要价值在于 rigor of systematic confirmation + failure mode taxonomy + practical diagnostics，更适合 Findings track。

**如修复以下关键问题，可提升至 3.5 (Borderline Conference)**:
- 补全 Proposition 1 证明（或弱化为 argmax preservation）
- 标题/Abstract 软化，Table 1 区分 powered/underpowered
- 诊断框架重定位为 failure mode 分类工具 + positive case 验证
- SCB 与 Wan et al. 增加 1-2 段显式对比

**Confidence**: 4/5（两位 Reviewer 均给出 4/5 confidence，初审评分一致 3.5，交叉分享后关键问题全部达成共识）

---

## Detailed Comments

### §1 Introduction
- "We show the answer is no" 过于 categorical——10/16 underpowered 时应为 "we find no evidence of improvement in powered conditions"
- 三个 contributions 列表中，Contribution 2（diagnostics）的 "correctly classify all 60 tested conditions" 需加 caveat

### §3 Method
- Eq. 3 的 scoring function 与 Proposition 1 证明的 score(a) = nₐ 之间需要桥接步骤
- K_eff（Eq. 1）后应添加直觉解释示例
- α=0.5 选择依据需补充

### §4 Results
- Table 1 应在表内标注统计功效或区分 powered/underpowered 条件
- GSM8K (n=30) / AIME (n=22) 建议移至 Appendix 或标为 exploratory

### §5 Analysis
- §5.1 Proposition 1：补全 Eq. 3 → score(a) = nₐ 的证明步骤，或改为 argmax preservation
- §5.1 Corollary 1：降级为 Remark
- §5.1 BR：补充 base-rate predicted BR 与 observed BR 的分解对比
- §5.1 关于 Wan et al. (2025) 的区分：增加 1-2 段显式对比
- §5.3 Diagnostics："correctly classify" → "correctly characterize the failure mode"；增加 positive validation

### §6 Cross-Architecture Escape
- "Capability-gap pattern" 基于 n=6，措辞改 "preliminary evidence" / "suggesting"
- Spearman ρ=1.0 (n=6) 的鲁棒性问题需讨论

### §7 Discussion
- Scope 边界声明：实验覆盖限于 SICA paradigm，其他 self-extraction 架构的验证是 future work
- α sensitivity 重新解释为退化证据

### Appendix
- Figure 4 内部文字过小
- pp16/22 表格堆叠过密
