---
round: 6
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T10:06:14.342608+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6 (Fresh)

**项目**: contrastive_entrain_calib
**论文**: "The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration"
**目标 Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计, R2: 新颖性+叙事完整性+Related Work）
**审稿模式**: Fresh（无前轮记忆）
**日期**: 2026-05-24

---

## Summary

本文提出"probe reward trap"：当冻结线性探针基于对比性谄媚方向 (d_syc, AUROC 0.827) 作为 SFT 训练信号时，行为死亡 (ToF=0) 在 500 步内发生，而生成熵直到 ~1,840 步才崩溃，产生 1,300 步监控盲区。论文系统测试了余弦投影（F1a-F1d）、二元/连续探针、纯行为奖励 GRPO 等六种 d_syc 配置，均失败（仅 4/31 checkpoints 超过 vanilla）；而逐 token SFT (ACT) 在每个 checkpoint (47/47) 均超过基线。LoRA 控制消融将差异归因于监督粒度（per-token vs per-completion）。论文定位为"negative result with mechanistic analysis"。

---

## Strengths

**[S1] 诊断链设计方法论出色 [R1-S2, R2-S1, 双方 AGREE]。** §4 的 F1a→F1d 形成严谨的递进诊断链（norm mismatch → gap too small → reward discontinuity → R₃ saturation），每步解决前序 failure mode 但暴露更深层问题 (Table 2)。这种系统性失败分析具有方法论示范价值。

**[S2] 时间解耦的量化新颖且有实践意义 [R1-S1, R2-S2, 双方 AGREE]。** 行为死亡先于分布崩溃 1,300 步的发现 (Table 3, Figure 3) 对 alignment 监控实践有直接指导意义：仅靠熵监控不足以检测此类失败。该实验使用 SFT + stop-gradient，与 GRPO 动态学无关，因果链干净。

**[S3] LoRA 控制消融设计 [R2-S3, R1 AGREE with caveat]。** Table 5 将 ACT 降至 GRPO 的 LoRA 配置（rank 64, α=64, 4 模块），仍在 16/16 checkpoints 超过 vanilla (SyconScore 0.326)，有效隔离了 adapter capacity 维度。但两位 Reviewer 均指出该消融仅控制了一个维度，仍有多个未控制变量。

**[S4] 跨模型验证增强 d_syc discriminability 结论的稳健性 [R1-S5, R2-S4, 双方 AGREE]。** Qwen3-8B (AUROC 0.827) 和 Llama-3-8B (AUROC 0.779) 呈现一致的 pattern（gradual emergence, upper-third concentration, monotonic evidence-strength scaling），表明 d_syc 的可判别性是跨架构共性现象。

**[S5] 失败模式定性分类有价值 [R1-S4, R2-S5, 双方 AGREE]。** Appendix B 的五类 stubbornness taxonomy（deliberation traps 28.7%, sycophantic stubbornness 24.3% 等）为理解 probe reward 的具体失效机制提供了具象化证据。前三类 (76.8%) 共享"调节拒绝风格而非接受率"的模式。

---

## Weaknesses

### Critical

**[W1] GPT-4.1 生成的 181 对 contrastive pairs 缺乏人工验证 [R1-W1, 双方 AGREE]。** 全部 contrastive pairs（包括 valid/sycophantic 区分和 evidence strength 三级标注）由 GPT-4.1 生成，仅通过自动化风格匹配筛选（长度差 <10%、共享开头词 ≥2）。无人工验证、无 inter-annotator agreement。d_syc 是整篇论文基石——若 GPT-4.1 存在系统偏差，d_syc 可能捕捉生成风格特征而非 sycophancy 语义特征。建议：至少 50 对人工验证 + evidence strength IAA (κ/α) + 公开 prompt template。

**[W2] GRPO group_size=2 构成未充分排除的致命混淆变量 [R1-W2, R1-W8, 双方 AGREE]。** gs=2 远低于 GRPO 典型范围 (8-64)，advantage estimation 退化为二元比较。论文声称 gs=8 ablation "rules out hypothesis (b)"，但 gs=8 仅运行 3 个 checkpoint 即被终止（0.084→0.085→0.054），这可能是正常 warmup 波动。R₃ 在 gs=2 下饱和至 ~0.98，advantage signal 近乎噪声——R₃-only GRPO 的失败可能是 gs=2 + reward saturation 导致的信号退化，而非 per-completion RL 的本质局限。建议：gs=8 至少运行完整 8000 步；或降级结论为 "per-completion RL with small group sizes fails"。

**[W3] ACT vs GRPO 的 "supervision granularity" 因果归因存在多维混淆 [R1-W3, R2-W7, 双方 AGREE]。** 即便 reduced-LoRA ablation 控制了 adapter capacity，ACT 与 GRPO 之间仍存在：(a) 序列长度 (256 vs 1024), (b) 数据来源 (online generation vs curated labeled pairs), (c) Reward 信号 (d_syc/R₃ vs ground-truth gold labels), (d) dropout (0 vs 0.05)。ACT 的成功可能主要归因于使用了 ground-truth 标注的 valid/invalid 对（即"知道正确答案"），而非 supervision granularity。论文 "isolating supervision granularity as the primary factor" (§6) 的因果声明过强。建议：在 Discussion 中列出所有差异维度并讨论各自可能影响；降级因果声明。

**[W4] 核心命题 "discriminability ≠ reward utility" 与 Goodhart's Law 高度同构，增量贡献论证不足 [R2-W1, R1 AGREE]。** d_syc 作为不完美代理指标在优化压力下导致模型"刷指标"（变得固执以最大化非谄媚得分），与经典 reward overoptimization 结构同构。论文引用了 Gao et al. (2023) 和 Skalse et al. (2022)，但全文从未提及 Goodhart's Law，也未明确论证增量贡献。可能的区分点：(1) 行为死亡 500 步即发生（远快于典型 overoptimization），(2) 时间解耦使标准监控失效。但论文需自己做出这一论证。建议：引用 Manheim & Garrabrant (2019) Goodhart taxonomy，明确论证增量。

**[W5] §3 与 §5/§6 之间存在未调和的叙事张力 [R2-W2, R1 AGREE]。** §3 声称 d_syc "captures evidential granularity"（AUROC 0.675→0.929 随证据强度单调上升），§6 声称 "encodes the direction of belief change but not its evidential warrant"，§5 说 "does not condition on input validity"。R1 提出可能的调和：discriminability 随证据增强反映的是 effect size 差异（stronger evidence → larger behavioral difference → easier to classify），而非方向本身编码了 evidential warrant。但论文从未做出此关键区分，导致核心论点的叙事一致性受损。

### Warning

**[W6] 256-token truncation 严重退化 d_syc signal (0.827→0.60)，削弱"语义局限"结论 [R1-W4]。** 论文将 d_syc GRPO 失败归因于其语义局限，但 256-token 截断使 AUROC 降至 ~0.60（near chance for binary）。在信号严重退化条件下的失败可能反映信号不足而非语义缺陷。论文未测试 512/1024 token。注：此论点仅影响 C1（GRPO 失败），不影响 C2（SFT probe trap，使用完整 response）。

**[W7] 统计效力不足 (n=2 seeds) [R1-W5, R2-W6]。** GRPO 2 seeds, ACT 2 seeds, probe trap 1 seed。n=2 的 variance estimation 和 rank correlation 无统计意义。ACT seed 2 在 Table 4 中 ToF/NoF 标记为 "—"（未报告），降低跨 seed 一致性可验证性。Probe trap 的 1,300 步 lag 基于单次实验，具体数字的置信度不足。

**[W8] 论文在 "negative result" 与 "general principle" 之间定位不够清晰 [R2-W3, R1 partial REBUT]。** R2 认为论文同时承载局部声明（"我们的方法失败了"）和全局声明（"discriminability is necessary but not sufficient"），且 "mechanistic analysis" 措辞过强。R1 反驳认为渐进式论证结构合理，但同意 "mechanistic" 应改为 "systematic diagnostic analysis"。**共识**：措辞需调整，但整体定位的分歧属 editorial level，不影响评分。

**[W9] SMART 讨论逻辑不完整 [R2-W4, R1 AGREE]。** SMART 处理的也是 sycophancy，与本文同一 target behavior。如果 sycophancy 在几何上不可分（§6 核心论点），SMART 的 per-step process reward 如何绕过这一限制？论文暗示是 supervision granularity，但 SMART 成功可能来自多因素（不依赖 d_syc、通过 reasoning trajectory 显式区分 warranted/unwarranted）。需更细致的机制分析。

**[W10] SyconScore harmonic mean 可能遮蔽有意义的差异 [R1-W6]。** ToF=0 时直接归零 (by design)。论文从未同时报告 arithmetic mean 或分别分析 ToF/NoF 趋势。建议补充 arithmetic mean 列。

### Minor

**[W11] 代码和数据可用性未提及 [R1-W7]。** 论文未提及是否计划发布 contrastive pairs、prompt templates、训练代码或 checkpoints。

---

## Reviewer Consensus

以下问题两位 Reviewer 均 [AGREE]：
1. 诊断链 (F1a→F1d) 方法论出色
2. 时间解耦 (1,300-step lag) 新颖有价值
3. GPT-4.1 pairs 缺乏人工验证是关键缺陷
4. GRPO gs=2 是未充分排除的混淆变量
5. ACT vs GRPO "supervision granularity" 因果归因过强
6. Goodhart's Law 讨论缺失削弱理论贡献
7. §3 vs §5/§6 叙事张力需要调和
8. SMART 讨论逻辑不完整
9. 单种子 probe trap 是限制

## Reviewer Divergence

**[DIV-1] Excitement 评分: R1=3.5/5 vs R2=2.5/5。**
- R1 认为 temporal decoupling 的发现具有独立新颖性和实践价值（对 monitoring 的直接启示），specific mechanistic characterization 超越了对已知原则的简单实例化
- R2 认为核心见解与 Goodhart's Law 高度同构，范围限于 sycophancy + 两个 8B 模型，负面结果的可推广性存疑
- **Director 判断**: R1 的论点有道理——temporal decoupling 的具体量化和 stubbornness taxonomy 确实超越了纯粹的 Goodhart instantiation。但 R2 关于 Goodhart 讨论缺失的批评也站得住脚。综合 Excitement 3/5。

**[DIV-2] 标题是否误导: R2-W5 vs R1-REBUT。**
- R2 认为论文范围远超 "probe reward trap"（覆盖 cosine failure、R3-only、ACT 对比），标题过窄
- R1 认为标题突出最 novel 发现是常见做法，subtitle 已提供范围信息
- **Director 判断**: 属 editorial preference，不影响评分。

---

## Questions

[Q1] 256-token truncation 下 d_syc AUROC 0.60 vs 0.827：cosine failure chain (Table 2) 的四个配置使用哪种条件的 d_syc？F1c "offline AUROC rises to 0.910" 对应什么条件？（R1-Q1）

[Q2] ACT L2 consistency loss weight=0.1 如何选定？对性能的敏感度？（R1-Q2）

[Q3] Stubbornness taxonomy 中 "genuine-accept-missed" (18.8%) 是格式/生成问题——NLI classifier 在这些 case 中的判定是否正确？是否应更谨慎解读 ToF=0？（R1-Q3）

[Q4] ACT 使用 ground-truth labels 而 GRPO 使用 d_syc/R₃——如果给 GRPO 同质量的 ground-truth 但仍是 per-completion scalar，结果如何？R₃-only GRPO 正是如此且也失败——是否应更强调 R₃ 的质量/粒度问题？（R2-Q3）

[Q5] "Behavioral death before distributional collapse" 在其他 reward misspecification 场景（safety/reasoning）中是否也存在？如果是，这不是 sycophancy 特有的。（R2-Q4）

[Q6] Reduced-LoRA ACT (0.326) > full ACT (0.301)——full ACT 是否过参数化？两者 overfitting 情况是否不同？（R1-Q5）

---

## Missing References

**[MR1] (Important, 双方 AGREE)** Manheim & Garrabrant (2019) "Categorizing Variants of Goodhart's Law" — 论文核心命题与 Goodhart's Law 高度相关但从未讨论。Probe reward trap 可能同时涉及 regressional 和 causal 两种 Goodhart 类型。

**[MR2] (Recommended, 双方 AGREE)** "Playing Devil's Advocate: Off-the-Shelf Persona Vectors Rival Targeted Steering for Sycophancy" (arXiv:2605.21006, May 2026) — 该论文认为 sycophancy 是 persona-level property 而非 single steerable direction，直接支持 d_syc 语义局限论证。

**[MR3] (Recommended, R1 AGREE)** Wu & Tang (2026) 的几何可分性量化标准需更深入讨论——量化比较 d_syc 与 reward-hacking directions 的可分性差异会强化论文理论贡献。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用 paperreview_ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 5 info）：

**Warning:**
- Page 11 (Appendix B 最后一页) 仅约 1/6 有内容，~85% 空白。建议整合或补充分析。
- Page 3 整页纯文本无 display item（§2.1–§2.5 约 1.5 页无图表）。考虑加 pipeline 示意图或提前引用 Figure 2。

**Info:**
- Figure 2/3 的 axis labels 和 tick labels 字号偏小（≤7pt），建议放大至 ≥8pt
- Figure 4 整体尺寸较小（单栏宽），legend 紧凑，可考虑 figure* 全宽展示
- Figure 1(a) colorbar 标注字号较小，屏幕阅读略显吃力
- Table 4 列数多（~8 列），单栏内略挤
- 首页无视觉锚点（Figure 1 在 page 2 顶部出现）

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

本文的核心发现——probe reward trap 中行为死亡先于分布崩溃 1,300 步——新颖且有实践价值，对 alignment 监控有直接启示。诊断链 (F1a→F1d) 的方法论设计出色。跨模型验证和 stubbornness taxonomy 增添了额外的深度。

但论文面临以下关键限制，阻碍其达到主会议水平：

1. **实验控制不足**：GRPO gs=2 构成致命混淆变量（gs=8 ablation 仅 3 checkpoints 即终止不具说服力）；ACT vs GRPO 的 "supervision granularity" 因果归因无法与序列长度、数据质量、reward 信号等多个替代解释分离；GPT-4.1 生成的 contrastive pairs 无人工验证。

2. **理论框架不完整**：核心命题与 Goodhart's Law 高度同构但从未讨论增量贡献；§3（evidence gradient）与 §5/§6（d_syc 不编码 evidential warrant）之间存在未调和的叙事张力；SMART 讨论逻辑不完整。

3. **统计效力有限**：probe trap 单种子、GRPO/ACT 各 2 种子、ACT seed 2 数据不完整。

论文适合 Findings 接收——probe reward trap 和时间解耦的发现对社区有价值。若要达到主会议水平，需要：(a) 完善 gs=8 或更大 group size 的完整实验以排除 GRPO 配置混淆；(b) 至少 50 对 contrastive pairs 的人工验证；(c) 在理论框架中明确讨论 Goodhart's Law 并论证增量贡献；(d) 调和 §3/§6 叙事张力。

---

## Detailed Comments

### §1 Introduction
- "This paper presents a negative result with mechanistic analysis" — "mechanistic" 应改为 "systematic diagnostic analysis"（R2-W3, R1 同意措辞保留）
- C1 ("Categorical reliability gap") 和 C2 ("Probe reward trap") 的关系需更清晰——C2 是独立于 GRPO 的发现（SFT），C1 依赖 GRPO 配置但受 gs=2 混淆

### §2 Experimental Framework
- §2.1: GPT-4.1 生成 pipeline 的 prompt template 未公开；style matching 的自动化验证（长度差 <10%、共享开头词 ≥2）可能不足以消除深层风格偏差
- §2.5: SyconScore harmonic mean 的 justify 仅一句——建议同时报告 arithmetic mean 或在脚注中说明
- Table 5 (Appendix): gs=2 应在正文中更突出地标注为"显著偏离标准实践"，而非仅在括号中注明

### §3 Direction Discriminability
- Evidence-strength gradient (AUROC 0.675→0.929) 被表述为 "captures evidential granularity"——需要限定说明：这反映的是 effect size 差异（stronger evidence → larger behavioral gap → easier classification），而非方向本身编码了 evidential warrant

### §4 Cosine Failure
- 256-token truncation 使 AUROC 降至 0.60，论文在 §4 开头已警告——但叙事应更强调这意味着 cosine failure chain 在严重退化信号条件下运行，不能直接推断"d_syc 作为 reward 在 full-signal 条件下也会失败"
- F1c "offline AUROC rises to 0.910" 的条件需明确（是 recalibrated direction 在 full-length activations 上？还是 truncated？）

### §5 Probe Reward Trap
- 核心发现（C2）扎实——SFT + stop-gradient 的设计因果链干净
- 但单种子限制了 1,300-step lag 具体数字的可信度
- "genuine-accept-missed" (18.8%) 属于格式/生成问题而非 epistemic 问题——对 ToF=0 的解读应更审慎

### §6 Discussion
- "isolating supervision granularity as the primary factor" 过强——应改为 "supervision granularity is a strong candidate but not the only possible explanation"
- Reduced-LoRA ACT (0.326) > full ACT (0.301) 的解读不足——可能暗示 full ACT 过参数化
- Wu & Tang (2026) 的几何可分性对比仅定性——量化分析会显著强化论证

### §7 Related Work
- 缺失 Goodhart's Law 讨论（Manheim & Garrabrant 2019）
- SMART 讨论需解释：如果 sycophancy 几何不可分，per-step reward 为何能绕过？可能的解释（不依赖 d_syc、reasoning trajectory 提供额外信息）应被讨论
- 建议加入 "Playing Devil's Advocate" (arXiv:2605.21006)

### §8 Conclusion
- "discriminability is necessary but not sufficient for reward utility" 的一般化需在前文有充分铺垫
- "condition-aware rewards with dense supervision offer the most promising path forward" — 可操作但未验证

### Limitations
- 覆盖了关键点（gs, truncation, 单种子, 单架构），长度适当
- 建议增加：ACT vs GRPO 多维混淆变量的讨论

### Appendix
- Table 5 hyperparameters 完整
- Stubbornness taxonomy 信息量大且分析到位