---
round: 10
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T08:01:19.264516+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 10 (Fresh)

**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer Panel**: 2 Reviewers (R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量)
**审稿模式**: 圆桌多轮（Round 1 独立审稿 → 交叉分享 → 收敛，1轮完成）

---

## Summary

本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 推理 trace 中提取逻辑约束并通过加权 partial MAX-SAT (Z3) 聚合答案，试图突破 Self-Consistency (SC) 的多数投票瓶颈。在 6 个开源模型 (7B–32B)、3 个逻辑推理领域 (FOLIO, ProofWriter, LogiQA)、3,000+ 条件评估（~1,250 unique instances）中，未发现统计显著的改善。论文将失败归因于 Symbolic Confirmation Bias (SCB)：自提取约束系统性支持模型多数答案（BR 1.05–4.97×），MAX-SAT 在 94.4% 情况下退化为简单计数。27 种无训练修复策略均失败。跨架构 NLI 验证 (DeBERTa) 在 ProofWriter 上获得 +6.67pp (p<0.001)。

---

## Strengths

**S1. 实验规模和系统性为负面结果论文树立标杆。** [R1-S1, R2-S1 共识] 6 个主模型 + 5 个 frontier 模型，3 个推理领域，~1,250 unique 实例，4-seed 复制，27 种修复策略——远超典型负面结果论文的评估力度。

**S2. 实验控制设计精巧。** [R1-S2 主导，R2 认可] Oracle control (§4.3) 用 gold 约束证明 MAX-SAT 机制本身有效 (+29.90pp Mistral, +14.22pp Qwen-14B FOLIO, +17.17pp ProofWriter)，精准定位瓶颈在约束质量。Shuffle control (§5.2) 证明 SCB 是结构性偏差（BR_shuffle ≈ BR_real, p>0.7）。Cross-model extraction 扩展到 9 个模型确认 SCB 普遍性。

**S3. 诊断框架有独立复用价值。** [R1-S3, R2-S2 共识] BR、CCR (Eq. 7)、K_eff 构成可复用的诊断工具包，可评估任何"自提取+聚合"范式。CCR > 0 vs. CCR < 0 清晰分离了跨架构 vs. 同模型条件。

**S4. CJT 理论框架提供原则性解释。** [R1-S4, R2-S3 共识] 将 SC/SICA 放在 Condorcet Jury Theorem 框架下，K_eff 将"有效独立样本数"量化（K_eff = 1.2–3.6 for nominal K=12），为理解采样收益递减提供了理论支撑。

**S5. 叙事层次超越多数负面结果论文。** [R2-S5 主导，R1 认可] 不是简单报告"方法 X 不 work"，而是：机制性解释 (SCB) → 理论框架 (CJT violation) → 可操作诊断 (K_eff, BR, C₀) → 初步逃逸方案 (cross-architecture NLI)。

**S6. 附录质量极高。** [R2-S4, R1 Reproducibility 4/5] 14+ 页附录含完整 prompt 模板、MAX-SAT 算法伪代码、per-condition 统计分析、case studies、failure mode taxonomy。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [CRITICAL] 摘要 BR 数值选择性报告，有夸大嫌疑。** [R1-N1, R2 AGREE]
- 摘要报告 "bias ratio 4.97×" 和 "83.3%"——来自 Mistral-7B/FOLIO 这一最极端条件
- Table 2 (p7) 实际 BR 范围：Mistral-7B 4.97 → o3 1.66 → Gemini-2.5-Pro 2.79（注：frontier 模型使用 cross-model extraction，非 self-extraction）
- 摘要应报告中位数或范围（如 "BR ranges from 1.66 to 4.97"），而非最极端值
- Frontier 模型 BR 相对较低，暗示 SCB 严重性可能与模型能力负相关——论文的 "universal" framing 需更强限定

**MF2. [CRITICAL] 统计功效呈现不足，"No Evidence" 声明与统计结论存在张力。** [R1-N2 + R2-N2，完全共识]
- 16 个非退化条件中 10 个 underpowered（MDE > 2pp at 80% power）
- TOST 仅确认 4/16 条件等价于零效应
- Aggregate sign test 8+/15− (p=0.21) 是"inconclusive"而非"negative"
- Power analysis (Appendix E Table 6) 是关键信息但被埋在附录中
- 标题 "Show No Evidence" 在日常学术用语中可被理解为"效果已被排除"，但论文只是"未检测到显著效果"——且部分条件下检测力不足以区分无效果与小正效果
- **必须修改**：§4.2 增加明确 power statement（如 "For the 10 underpowered conditions, we cannot rule out effects smaller than ±X pp"）；将 MDE 核心数字从附录提到正文

**MF3. [CRITICAL] α=0.5 参数无敏感性分析。** [R1-N3 主导，R2 AGREE with nuance]
- α=0.5 控制约束权重与投票权重的相对影响
- 94.4% MAX-SAT≡count-only 的核心发现可能依赖于 α 的特定取值
- R2 认为影响可能有限（当 BR>1 时约束方向与投票一致，α 调整不影响最终选择），但缺少实验验证
- **必须修改**：在 2–3 个代表性条件（高 BR + 低 BR）上跑 α∈{0.1, 0.3, 0.7} 消融，报告退化率变化

### Should-Fix（影响评分但不一票否决）

**SF1. Discussion/Conclusion 过于压缩。** [R2-W2, R1 AGREE]
- §7 (p8) 不到半页，缺少：(1) SCB 与 CoT unfaithfulness 关系讨论，(2) 对 neuro-symbolic 实践者的可操作建议，(3) test-time scaling 含义展开
- 视觉审查发现 Discussion 约 3–4 行溢出到 page 9 顶部——需压缩或重排

**SF2. 符号/指标过载。** [R2-W1, R1 AGREE]
- 8 页正文引入 7 个定量工具（K_eff, κ, BR, C₀, CCR, ProcessSim, ρ_same），认知负担重
- 建议：ProcessSim (§5.3) 和 CCR (§5.4) 移至附录，正文聚焦 K_eff/BR/C₀ 三个核心指标

**SF3. 跨架构 NLI claim 须限定到命题逻辑任务。** [R1-W1, R2 部分涉及]
- FOLIO 和 ProofWriter 均为命题/一阶逻辑任务，NLI 模型天然对齐 textual entailment
- 未在 StrategyQA、LogiQA 等非逻辑域测试 NLI 验证
- 摘要应限定为 "on propositional-logic benchmarks"；§6 或 Limitations 讨论 domain limitation
- 注：R2 初审误称"仅一个验证器"，R1 交叉纠正（实际 3 个 NLI 架构 × 4 generators × 5 weights），证据规模比 R2 初判更充分

**SF4. TOST ±2pp margin 缺乏独立论证。** [R1-W4, R2 AGREE]
- 用 SC 自身效应量定义"可忽略"有循环性
- ±3pp 时所有条件均 equivalent——结论对 margin 敏感
- 建议引用领域公认的最小实际意义差异，或提供 margin sensitivity analysis

**SF5. 语法去重可能系统性膨胀 BR。** [R1-W2, R2 AGREE]
- 语义等价但语法不同的约束被分别计数（去重率仅 46.0%）
- 论文有 shuffle control 部分回应（BR_shuffle ≈ BR_real），但未报告 Z3 语义去重后 BR
- 建议补充语义去重后 BR 值

**SF6. Table 1 核心结果表可读性不足。** [R2-W4, R1 小问题#1 一致]
- Type A/B/C 子区域分隔视觉层次不够，显著性标记系统复杂
- 建议增加水平线分隔或浅色底纹；简化显著性标记

**SF7. "Symbolic Mirage Hypothesis" 定位不一致。** [R2-W3, R1 AGREE 低严重性]
- §3.3 提出假设，§5 直接以结论性措辞使用，缺显式验证回溯
- 建议 §5 结尾增加总结段，显式对应三个 testable predictions

**SF8. 4-seed replication 充分性存疑。** [R1-W5, R2 PARTIALLY AGREE]
- Seed 间变异性未充分量化（inter-seed SD 未报告）
- Bootstrap CI 是否聚合 4 seeds 不清楚

**SF9. TF-IDF 作为 process independence 代理粒度较粗。** [R1-W3, R2 AGREE with reservation]
- 只能捕捉词汇层面重叠，非推理结构相似性
- 但 ProcessSim 不是核心论证承重墙（R2 观察），属补充证据

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉分享后达成一致：

| 编号 | 问题 | 共识状态 |
|------|------|----------|
| MF1 | BR 选择性报告 | [AGREE] 摘要应报告范围/中位数 |
| MF2 | 统计功效 framing | [AGREE] 正文需加 power statement，提升 Appendix E |
| MF3 | α 无消融 | [AGREE] 需跑 α 消融（R2 认为影响有限但同意做） |
| SF1 | Discussion 过短 | [AGREE] 需扩展覆盖 3 个话题 |
| SF2 | 指标过载 | [AGREE] ProcessSim/CCR 可移附录 |
| SF3 | NLI claim scope | [AGREE] 须限定到命题逻辑 |
| SF4 | TOST margin | [AGREE] 需 sensitivity analysis |
| SF5 | 语法去重膨胀 BR | [AGREE] 需报告语义去重后 BR |
| SF6 | Table 1 可读性 | [AGREE] 需增加视觉分隔 |

## Reviewer Divergence

| 编号 | 问题 | R1 | R2 | 最终判断 |
|------|------|----|----|----------|
| R2-N1 | §6 跨架构贡献不足 | [REBUT] R2 事实错误（3 verifiers 非 1），证据规模已超 PoC 标准 | [AGREE] 仅 1 verifier（被 R1 纠正） | **降级为 SF3**：证据比 R2 初判更充分，但 domain-specificity 问题成立 |
| R2-W5 | CJT 边界条件 | [REBUT] 论文已涉及 high/low accuracy 两端，CJT 是 framing device 非完整推导 | [AGREE] | **不作为独立问题**，合并到 SF1 Discussion 扩展 |
| Excitement | 新颖性增量 | 3/5（量化贡献有独立价值） | 2.5/5（被先验工作预示） | **记录分歧**：SCB 概念层面增量有限，但量化深度和实验规模提供了超越先验工作的实证价值 |

---

## Questions to Authors

**Q1** [R1]: Table 2 中 o3 (BR=1.66) 和 Gemini-2.5-Pro (BR=2.79) 的 BR 远低于 Mistral-7B (4.97)。SCB 严重性是否与模型能力负相关？如果仅在 frontier 模型上测试 SICA，"no evidence" 结论是否仍成立？（注意 extractor confound：frontier 使用 Mistral-7B 做 cross-model extraction）

**Q2** [R1]: 94.4% MAX-SAT≡count-only 的统计来自哪些条件？是否包括退化条件 (C₀<5%)？非退化条件单独的比率是多少？

**Q3** [R1]: DeBERTa standalone accuracy 在 FOLIO 上低于 SC baseline (49.51% vs. 55.88%)，但 combo 仍有增益 (+2.94pp)。这是否与 Empirical Finding 2 的 capability gap hypothesis 矛盾？"Exceed" 是指 standalone accuracy 还是 independence-adjusted effective accuracy？

**Q4** [R1]: 27 种修复策略中是否有任何在个别条件上通过显著性检验（即使总体不显著）？这些 "pocket of success" 的特征是什么？

---

## Missing References

1. **Dhuliawala et al., 2023** — "Chain-of-Verification Reduces Hallucination in Large Language Models" [R2-M1, R1 交叉 AGREE] — 直接研究 LLM 自验证局限，与 SCB 发现互补
2. **Lightman et al., 2024** — R2 初审提出缺引，R1 交叉回应确认论文已引用（References p11: "Let's verify step by step. In ICLR."）——**非遗漏**
3. R1 建议在 Related Work §2 中更明确地区分 trained verifier 与 self-extracted constraint——论文核心洞见 (CCR 正/负) 依赖于这一区分，应更早建立

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，跳过。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~4.5 分钟），结果：0 critical, 2 warning, 5 info。

**WARNING:**
1. **Page 9 溢出**: 主文 §7 (Discussion) 约 3–4 行溢出到 page 9 顶部，Limitations 从 page 9 中段开始。EMNLP 2026 主文限 8 页（Limitations 豁免），当前主文约 8.05–8.1 页。ACL/ARR 对页数限制零容忍，**建议压缩 Discussion 或前文确保 §7 在 page 8 内结束**。
2. **Pages 3–5 低视觉密度**: Related Work → Experiment Setup 连续约 2.5 页无 figure/table，审稿人快速翻阅时可能感到单调。

**INFO:**
- Figure 1 (p2) 尺寸偏小，内部标签打印时可能偏小
- Figure 2 (p7) axis label 字号约正文 65–70%，接近可读下限
- 附录单页表格密度极高（page 14 有 4 个表），审稿人查阅体验较差
- 附录 14 页含 29 表 + 5 图 + 2 算法，建议在附录开头加 overview 导航
- Prompt template 和 Algorithm 排版正确

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 4/5 | 4/5 | **4/5** |
| Excitement | 3/5 | 2.5/5 | **2.75/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4/5 | 4/5 | **4/5** |

**判断依据**：
- **Soundness 4/5**：实验设计严密（oracle/shuffle/cross-model 三重控制），统计方法总体正确。扣 1 分：10/16 条件 underpowered，α 无消融，TOST margin 有循环性。
- **Excitement 2.75/5**：SCB 的定量刻画对 neuro-symbolic 和 test-time scaling 社区有参考价值，但核心发现（自提取约束不提供独立信号）部分被 Huang et al. (2024) self-correction 和 Stechly et al. (2025) 所预示。诊断工具 (K_eff, BR, C₀) 实用但是已有统计量的直接适配。跨架构逃逸方案初步但 domain-specific。
- **Reproducibility 4/5**：参数完整报告，prompt 模板和算法伪代码详尽，受匿名限制未提供代码。

**接收建议**：
- **当前状态**：Findings 级别确定达标。方法论扎实 + 有用的负面结果 + 可复用的诊断工具。
- **升至 Conference 需要**：解决 MF1–MF3（BR 报告、power framing、α 消融），扩展 Discussion (SF1)，收窄 NLI claim scope (SF3)。如果 α 消融验证了退化率对 α 不敏感，这反而更强力地支持 SCB 结论。
- **主要风险**：如果 frontier 模型 BR≈1 且 α 消融显示退化率下降，论文的核心 "universal SCB" narrative 需要实质性修改。

---

## Detailed Comments

### Title & Abstract (p1)
- 标题 "Show No Evidence" 在统计学中是标准用法，R1 认为可保留，R2 建议改为更限定的表述。建议保留标题但在 Abstract 增加 MDE 限定句。
- BR 4.97× 应改为范围/中位数。
- "six open-source LLMs (7B–32B)" 准确，但 cross-model extraction 扩展到 frontier 的角色应在摘要中更清晰区分。

### Introduction (pp1–2)
- Story arc 清晰：SC ceiling → CJT independence → SICA → SCB → escape。
- 三个 Contributions (p2) 措辞基本准确。R2 曾质疑 §6 作为贡献，但 R1 纠正后降级为 domain-specificity 问题。
- Figure 1 (p2) 有效传达 pipeline 但尺寸偏小。

### Related Work (pp2–3)
- 覆盖面广（SC extensions, neuro-symbolic, test-time compute, CJT positioning），结构清晰。
- 缺 Dhuliawala et al. (2023) Chain-of-Verification。
- Trained verifier vs. self-extracted constraint 的核心区分应更早建立。

### Background & Setup (pp3–5)
- CJT 框架和 K_eff 定义清晰，ordinal diagnostic caveat 正确。
- SICA pipeline (§3.2) 形式化完整。
- Symbolic Mirage Hypothesis (§3.3) 的三个 testable predictions 好，但后续验证回溯不够显式。
- Empirical Finding 1–2 的 tcolorbox 框在负面结果论文中略显过度包装。
- α=0.5 需消融验证。

### Experiments (pp5–6)
- Table 1 是论文核心，内容完整但可读性需改善。
- §4.2 的统计讨论技术正确但缺 power statement。
- Oracle control (§4.3) 设计精巧，是论文最强证据之一。

### Analysis (pp6–7)
- SCB 分析 (§5.2) + shuffle control 是核心贡献，论证严密。
- 指标过多（7 个），ProcessSim 和 CCR 可移至附录。
- Figure 2 (27 strategies) 信息密度高但个别策略难以区分。

### Cross-Architecture Proof-of-Concept (p8)
- 3 NLI architectures × 4 generators × 5 weights 的评估规模超出 PoC 标准。
- 但仅在命题逻辑任务上验证，claim 须限定。
- Capability gap hypothesis (Spearman ρ=1.0, n=6) 的统计基础有限（4/6 共享 DeBERTa verifier）。

### Discussion & Conclusion (p8)
- 过于压缩（约半页），与论文的贡献规模不匹配。
- 缺 SCB vs CoT unfaithfulness 讨论、实践者建议、test-time scaling 含义。
- 视觉审查发现约 3–4 行溢出到 page 9——需压缩。

### Limitations (pp8–9)
- 覆盖关键局限（模型范围、domain 限制、power、seed、cost）。
- "7B to 32B parameters" 与论文其他部分一致（注：R2-M4 发现 Limitations 中有 "7B-128B" 不一致，需统一检查）。

### Format Compliance
- 正文约 8.05–8.1 页——**需压缩至严格 8 页内**
- 匿名完整（"Anonymous ACL submission"，无身份泄漏）
- ACL template 正确（`\usepackage[review]{acl}`）
- 引用格式合规