---
round: 3
overall_score: borderline
timestamp: 2026-05-15T04:14:58.309947+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3
**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT） → 收敛汇总

---

## Summary

本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。在 SciERC、CoNLL-2003、WNUT-17 三个数据集和两个 8B 模型（Qwen3-8B, LLaMA-3.1-8B）上实验。核心发现是 "correlation-selection gap"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。

---

## Strengths

**S1. 问题分解有真正洞察力。** 将 quality estimation 与 sample selection 明确区分为两个独立目标，用不同指标分别评估（Spearman ρ + AUROC vs. best-of-N F1）。Per-sample vs. instance-level 信号的形式化区分使分析逻辑链条清晰可追溯。这一分析框架本身是对现有文献的有价值贡献。[R1-S1, R2-S1 一致]

**S2. 统计报告全面严谨。** Paired bootstrap (B=10,000) 附带 95% CI、Cohen's d、sign test win%、pairwise Δρ CI（Appendix D），多数实证论文不会做到这个粒度。[R1-S2, R2-S2 一致]

**S3. WNUT-17 capability boundary 分析揭示重要方法论警示。** Voting ρ=0.724（full-set）→ conditional ρ=0.038 (n.s.) 揭示 inflated correlation 由 zero/non-zero boundary 驱动；logprob 条件反转（full ρ=−0.410 → conditional ρ=0.350）进一步确认此现象。[R1-S4, R2-S3 一致]

**S4. 负面结果处理诚实平衡。** RE 单数据集局限在 Introduction、Discussion、Conclusion、Limitations 四处明确提及。WNUT-17 作为方法边界坦率报告。Limitations section 全面覆盖多项局限。[R1-S3, R2-S4 一致]

**S5. Task difficulty 分析有实用价值。** EM 在简单任务领先 vs. SJ/Voting 在复杂任务领先的 crossover 发现，以及 conditional filtering 后信号排序翻转，为从业者信号选择提供实用指导。[R1-S4]

**S6. Robustness 覆盖面广。** Temperature (T=0.7/1.0)、N-scaling (8→16)、cross-architecture 均有系统分析。[R2-S6]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[Critical] W-C1: Constrained decoding 是 correlation-selection gap 的未控制混淆变量**
- 两位 Reviewer 独立提出（R1-N1, R2-N2），交叉回应后完全共识
- 论文核心发现 "no signal reliably surpasses greedy" 可能部分是 Outlines/vLLM constrained decoding 压缩 per-sample diversity 的产物，而非置信度信号本身的固有局限
- Random baseline gap 仅 3.6pp，可能远低于 unconstrained generation 的 variance
- §5 Discussion 已承认此问题但仅作 future work 提及，未设计任何对照或量化分析
- 75% of logprob comparisons 为 effective ties (win%=46.6%) 暗示 per-sample variance 极小
- **建议**：(a) 报告 unique output fraction + per-sample logprob std 分布量化实际 diversity；(b) 增加 unconstrained generation + post-hoc parsing 对照；或 (c) 至少明确 gap 结论的 generalizability boundary 为 constrained decoding regime，在 Abstract/Conclusion 中限定

### Should-Fix（影响评分）

**[Warning] W-S1: RE 结论建立在单一 benchmark 上且受严重 floor effect 影响**
- R2 独立提出(N1)，R1 交叉回应后上调严重性至 borderline Must-Fix
- SciERC RE 44% zero F1 严重压缩信号可区分范围，RE gap 证据（−0.9pp, p=0.80）统计说服力弱
- 论文已在 4 处 hedge（Round 2 修正），但仍在 Abstract 和 Contribution 中以 "NER and RE" 并列呈现，给人 RE 证据与 NER 等量齐观的印象
- **建议**：(a) 进一步降级 RE claim 为 "preliminary RE evidence on SciERC"；(b) 补 SciERC RE conditional filtering 分析量化 floor effect 影响

**[Warning] W-S2: Selection gap 统计论证不完整——failure to reject ≠ evidence of absence**
- R1 列 critical(N2)，R2 交叉回应降为 should-fix（6/6 配置一致性构成 cumulative evidence，CI 正面端 +4.2pp vs 13.2pp oracle headroom 实际意义有限）
- 共识：措辞需更严谨。p>0.39 只是 absence of evidence
- **建议**：修改为 "we found no significant evidence that any signal surpasses greedy" + 补充 power analysis 或 TOST 等价性检验

**[Warning] W-S3: N=8 核心结果 single seed (seed=42)**
- R1 列 critical(N3)，R2 交叉回应降为 should-fix（N=16 3-seed ranking 完全一致）
- Table 1 N=8 和 Table 2 selection 全部基于单一 seed，信号排序差异小（Voting-SJ Δρ=0.019）
- **建议**：SciERC N=8 补至少 3 seed mean±σ，或在 Limitations 明确 single-seed 风险并引用 N=16 stability

**[Warning] W-S4: Gap 概念部分 tautological**
- R1(W2) 和 R2 交叉回应均认同：4/5 instance-level 信号 by design 无法 per-sample 区分，selection 失败是定义必然
- 真正的 empirical contribution 是 (1) logprob（唯一 per-sample 信号）也失败，(2) consensus-proximity 转换策略未能弥合 gap
- **建议**：Discussion 中明确分离两层论证——结构性局限 (by construction) vs. 经验性失败 (logprob + consensus-proximity)

**[Warning] W-S5: Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系**
- R1(W6) 提出，R2 强烈同意——"R1 最有力的 Should-Fix"
- 仅测一种转换策略就声称 "signals fail as selectors" 不充分
- MBR decoding (Eikema & Aziz 2022, Freitag et al. 2022) 是成熟替代方案但未讨论
- **建议**：(a) 明确 consensus-proximity 与 MBR 等价性；(b) 讨论替代策略是否可能缩小 gap；(c) 补引 MBR 文献

**[Warning] W-S6: 多重比较校正缺失**
- 两位 Reviewer 一致。SJ–EM CI lower bound +0.003，Bonferroni 下几乎必然不 survive
- **建议**：声明未做校正 + "Yes†" 改为 "suggestive"

**[Warning] W-S7: FK 独立性假设 justification 不足**
- 两位 Reviewer 一致。§3.2 一句 hand-wave 不够
- **建议**：报告 inter-sample correlation 或在 Limitations 明确讨论

**[Warning] W-S8: Cross-model 措辞过度外推**
- 两位 Reviewer 一致。两模型均 8B，应为 "cross-architecture at 8B scale"
- **建议**：正文加限定词

**[Warning] W-S9: "First multi-family comparison" claim scope 过宽**
- 两位 Reviewer 一致。应限定为 "for both QE and selection in generative structured IE"

**[Warning] W-S10: 遗漏引用**
- VerifiNER (Kim et al., ACL 2024)——supervised NER verification 参照点
- MBR decoding (Eikema & Aziz 2022; Freitag et al. 2022)——与 consensus-proximity 直接相关
- Malinin & Gales (2021)——structured prediction uncertainty
- He et al. (NAACL Findings 2024)——sequential labeling uncertainty
- RASC (Aggarwal et al., NAACL 2025)——需确认是否与已引 REASC 重复

**[Warning] W-S11: 术语不一致**
- "confidence signal" vs "consistency signal" 混用；"VC" vs "Voting Conf." 缩写不统一；LLaMA Factory 未引用

### Minor Issues

**[Info] W-M1**: WNUT-17 "54% zero F1"（§4.1）vs Table 7 显示 355/689 ≈ 51.5%，数据不一致
**[Info] W-M2**: EM selection exclusion (Table 2) 理由 "probability negligible" 需报告 exact match pairs 实际频率
**[Info] W-M3**: Ethics Statement 缺失——ARR 仅 "encouraged" 非 "required"（R1 rebut R2），但添加简短声明为 good practice
**[Info] W-M4**: ρ–AUROC dissociation 作为独立发现过度强调——dissociation 本身 expected，应承认统计预期性后聚焦实践含义
**[Info] W-M5**: 对 Nedellec (2026) Introduction 措辞偏 adversarial，建议改为更 neutral 语气
**[Info] W-M6**: LOO-SJ 验证中 Δρ=−0.014（整体 Spearman）和 per-instance max Δρ=3.1×10⁻⁴ 量纲不同，需澄清
**[Info] W-M7**: Figure 1 caption 引入 p=0.39（来自 Table 2），建议补 "(Table 2)" 交叉引用
**[Info] W-M8**: SJ Hungarian matching cost function 未明确 maximize/minimize 方向和 zero-IoU pairs 处理
**[Info] W-M9**: Table 1 N=16 区域大面积空白，建议补交叉引用或考虑合并呈现
**[Info] W-M10**: Semantic entropy footnote 比较（§4.2）既承认不可比又给出数字，R1 建议删除，R2 建议保留但强化 caveat——共识为保留并强化 caveat placement

---

## Reviewer Consensus [AGREE]

1. **Constrained decoding 是核心 validity threat**：gap 可能部分是实验设置 artifact 而非信号固有局限 [R1-N1 = R2-N2, 完全共识]
2. **RE 证据薄弱**：44% zero-F1 + 单数据集使 RE claim 基础不稳 [R2-N1, R1 交叉后上调]
3. **Gap 概念需分层论证**：instance-level 信号的 definitional limitation 与 logprob 的 empirical failure 应分开论述 [R1-W2 = R2 agree]
4. **Consensus-proximity 需与 MBR 建立联系**：单一转换策略不足以支撑 sweeping claim [R1-W6, R2 强烈同意]
5. **统计报告整体质量高**但有特定 gaps：单 seed、缺多重比较声明、failure-to-reject 措辞 [双方一致]
6. **写作质量好**，叙事连贯，负面结果处理诚实 [双方一致]

## Reviewer Divergence [REBUT]

1. **Ethics Statement 严重性**：R2 列 critical → R1 rebut（ARR 仅 encouraged）→ **共识降为 Minor**
2. **Failure-to-reject 统计逻辑**：R1 列 critical → R2 降为 should-fix（6/6 cumulative evidence）→ **共识降为 Warning**
3. **Single seed**：R1 列 critical → R2 降为 should-fix（N=16 ranking stability）→ **共识降为 Warning**
4. **SJ 增量贡献**：R2 认为 borderline → R1 部分 rebut（SJ 价值在 temperature/N-scaling robustness 而非单点 ρ 增量）→ **共识为 SJ 论文措辞应强调 robustness**
5. **Semantic entropy footnote**：R1 建议删除 → R2 建议保留强化 caveat → **共识为保留但强化**

---

## Questions to Authors

1. 是否考虑过 unconstrained generation 对照？即使 parse 成功率低，比较两种 regime 下 pairwise SJ 分布也能 calibrate gap 的 generalizability。
2. Logprob 在 WNUT conditional set 达所有信号最高 ρ=0.350（Table 7），如何 reconcile 主文中 "logprob 最弱" 叙述？是否暗示 logprob 在高 diversity 场景有独特优势？
3. LoRA rank=32 是否影响 sample diversity？更低 rank 可能增加 diversity。
4. N=16 selection 结果有无 multi-seed bootstrap p-value？
5. SciERC RE conditional filtering 分析（非零 F1 子集）的 gap 结论是否改变？

---

## Missing References

1. Eikema & Aziz (2022) "Sampling-Based Approximations to Minimum Bayes Risk Decoding for NMT" — MBR decoding 理论框架，与 consensus-proximity 直接相关
2. Freitag et al. (2022) "High Quality Rather Than High Model Probability" — MBR decoding
3. Kim et al. (2024) "VerifiNER" — ACL 2024, supervised NER verification
4. Malinin & Gales (2021) "Uncertainty Estimation in Autoregressive Structured Prediction"
5. He et al. (2024) "Uncertainty Estimation on Sequential Labeling" — NAACL Findings 2024
6. Aggarwal et al. (2025) "Reasoning Aware Self-Consistency" — NAACL 2025 (需确认与已引 REASC 是否重复)

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）

---

## Overall Assessment

**Overall Score: borderline (Findings track)**
**Confidence: 4/5**

**判断依据**：

论文在 quality estimation vs. sample selection 的问题分解上有真正贡献，correlation-selection gap 作为概念有实用价值，统计报告质量在 empirical NLP 论文中属上乘，WNUT-17 capability boundary 分析提供了重要方法论警示。

但一个 critical 问题（constrained decoding confound）对核心 claim 构成 validity threat——如果 gap 主要由实验设置的 diversity 压缩导致，则核心贡献的 generalizability 受限。7 个 warning 级别问题（RE 单数据集、statistical logic、single seed、gap tautological 成分、MBR 联系缺失、多重比较、FK 独立性）共同表明论文在 soundness 和 framing 上仍有显著改进空间。

两位 Reviewer 独立给出 3/5 (Findings) 评分，交叉回应后评分维持不变。论文方法论严谨的核心质量使其适合 Findings track，但 constrained decoding confound 未解决前不建议 Main Conference。

**修订优先级**（按影响排序）：
1. **[Must]** Constrained decoding diversity 量化或对照实验（决定核心 claim 是否成立）
2. **[Should]** RE claim 降级 + conditional analysis（减少过度泛化风险）
3. **[Should]** Selection gap 措辞修正 + power analysis（统计严谨性）
4. **[Should]** Gap 论证分层 + MBR 联系（概念清晰度）
5. **[Should]** Multi-seed 验证或 Limitations 声明（可靠性）
6. **[Minor]** 术语统一、引用补充、数据一致性修正

---

## Detailed Comments（逐节）

### Abstract
- "NER (three datasets of varying difficulty) and RE (SciERC)" 区分到位（Round 2 修正有效）
- "oracle headroom" 首次出现无定义，建议加括号解释
- "no signal reliably surpasses greedy" 措辞需修改为更严谨的统计表述

### Introduction
- Quality estimation vs. sample selection 的分离框架论述清晰
- 对 Nedellec (2026) 的 (i)-(iii) 列举技术准确但语气偏 adversarial
- "First multi-family comparison" 需收窄 scope

### Method (§3)
- Per-sample vs. instance-level 形式化清晰（Eq. 1-7）
- SJ Eq. 4: Hungarian matching 优化目标和 zero-IoU pairs 处理需补充
- FK §3.2: 独立性假设 one-line justification 不充分
- Consensus-proximity (§3.3): 未与 MBR decoding 建立联系

### Experiments (§4)
- Quality estimation (§4.2): 数据全面，task difficulty crossover 有洞察力
- WNUT-17 conditional 分析揭示重要 artifact（Table 7）
- Selection gap (§4.3): 统计报告详实但 failure-to-reject 逻辑需修正
- Robustness (§4.4): temperature/N-scaling 分析系统性好，SJ stability 值得突出

### Discussion (§5)
- Practical recommendations 具体可行
- "Why logprob fails" 段落是关键改进方向——需更多实证支持
- Constrained decoding 讨论需从 "future work" 升级为当前 limitation 的核心分析
- Gap 论证应分层：definitional (instance-level) vs. empirical (logprob + consensus-proximity)

### Conclusion (§6)
- 三项 anchoring findings 总结准确
- RE hedging 到位但仍可进一步降级

### Limitations
- 覆盖面广且诚实
- 建议新增：(a) constrained decoding 对 diversity 的影响作为 explicit limitation 条目；(b) single-seed 风险

### Appendix
- Bootstrap CI 表 (Table 8) 有价值
- WNUT-17 全信号表 (Table 7) 补充到位
- Cross-configuration selection (Table 6) 增强了 gap 证据面