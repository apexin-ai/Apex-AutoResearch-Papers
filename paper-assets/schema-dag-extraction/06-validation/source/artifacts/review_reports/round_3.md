---
round: 3
overall_score: weak accept
timestamp: 2026-05-16T04:56:30.303233+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 3

**论文**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿人**: Reviewer 1 (方法严谨性 + 实验设计 + 统计分析), Reviewer 2 (新颖性 + 完整性 + 写作质量 + 格式合规)
**轮次**: Round 3（论文已针对 Round 2 的全部 Critical issues 进行修订）
**外部审稿**: 未启用

---

## Summary

本文首次系统隔离 training-free LLM IE 中 schema 退化的两个通道（type count 和 type confusability），引入 SCS/BCS 量化指标，在 NER (Few-NERD)、RE (FewRel)、ED (MAVEN) 三个任务上进行控制实验。主要发现：(1) RE 上两通道 cleanly separable（高 BCS 准确率收敛至 ~51% floor）；(2) NER 上 confusability 同时影响 detection；(3) MAVEN 出现 centrality confound 导致 per-type BCS 方向反转；(4) SDGD 负面结果表明 union-based merge 存在结构性挑战。相比 Round 2，论文在 prompt 透明度、统计注解、framing 降格方面有实质性改善。

---

## Strengths

**S1. 实验设计是该领域罕见的方法论标杆。** Count curves（固定 confusability，变 count）和 BCS-controlled experiments（固定 count，变 confusability）互补设计合理，within-pool 控制（80-rel pool → 16-sub）有效排除 pool composition confound。permutation test (p=0.436) 验证跨条件 slope 一致性。这在 training-free IE 领域是首次系统性因素隔离。【R1, R2 共识】

**S2. 统计方法全面且透明。** Bootstrap CI (B=10,000)、type-level cluster bootstrap（处理 pair 非独立性，Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]）、within-pool regression (slope −0.401, CI excludes zero, p=0.027)。对 pair-level CI 与 cluster bootstrap CI 的差异做了诚实解释。§practical_magnitude 校准了 typical vs extreme effect size (IQR → 2.2pp vs extreme 31.2pp)。【R1 重点肯定, R2 同意】

**S3. 诚实报告负面结果和 modest effects。** Pairwise r²=1.3-1.7% 如实报告，SDGD 全面失败 (best F1=0.32 vs single-pass 0.45)，factorial test 不显著 (p=0.50)，MAVEN centrality confound，80-rel full condition underpowered 等均明确标注。Limitations 涵盖 8 项，远超该领域平均水平。【R1, R2 共识】

**S4. Prompt 透明度大幅改善。** Appendix D 包含三个任务的完整 prompt template（v1/v2 对比 + JSON schema + diff 说明），RE 单版本明确标注，§4 开头标注 prompt 版本适用范围。Round 2 的 SW3 (Critical) 完全解决。【R1 PASS】

**S5. Centrality confound 分析有独立方法论贡献。** 识别 per-type BCS 在 same-domain schema 上因 embedding collapse 反转 (MAVEN: ρ=+0.184)，partial correlation 控制 log freq + degree centrality 后 p>0.2，但 pairwise SCS 仍有效 (r=0.129, p<10⁻¹⁰)。对 schema analysis 从业者有直接指导意义。【R1, R2 共识】

**S6. Cross-model validation 设计合理。** Llama-3.1-8B 在 NER count channel (r=0.725) 和 RE confusability channel (Δ=-27.1pp) 上复现主要发现。High-BCS accuracy 跨模型收敛至 ~51% floor 是一个有启发性的发现，已恰当标注为 hypothesis。【R1, R2 共识】

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [Critical] v2 prompt 下 RE BCS gap 缩至 7.9pp (CI 含零)，核心 claim robustness 存疑。** v2 prompt 将 RE BCS gap 从 31.2pp (v1) 缩减至 7.9pp (CI: [−5.2, +21.5], n=5)。这意味着在合理 prompt 设计下，confusability channel 在 RE 上可能不显著。论文在 Appendix F 坦诚讨论（"the v1 extreme-batch gap reflects both genuine type confusion and prompt-induced noise"），Discussion 也提及，但**正文核心 narrative 仍以 v1 结果为主锚点**。Introduction finding (2) 仍引用 "accuracy gaps reaching 31.2pp under extreme-batch comparison" 而未同时注明 v2 结果。
- **两 Reviewer 共识这是最大 concern。**
- R2 补充 nuance：pairwise SCS correlation 不受 prompt 影响（基于 type name embedding），NER v2 correlation 更强 (r=+0.58 vs +0.50)。因此 confusability 作为 predictor 的 validity 不受 prompt 影响，受影响的是 practical magnitude。
- **要求**：(a) 正文 §4.3 增加一段 v2 attenuation 讨论；(b) Introduction 引用 31.2pp 时同时注明 v2 结果 (7.9pp)。

**C2. [Critical] "Interventional" 因果语言超出 quasi-experimental 设计支撑范围。** §4.3 "To move from correlational to interventional evidence"；§4.4 "confusability drives substitution errors"。BCS-controlled experiments 通过构造 batch 操纵 BCS，但 batch composition 与 BCS 完全共变——高 BCS batch 的 types 可能在 inherent difficulty、frequency、definition quality 等维度上系统性不同于低 BCS types。Within-pool analysis 部分缓解了 pool composition confound，但未控制 type-level properties。
- **两 Reviewer 共识。**
- **要求**：将 "interventional" 改为 "quasi-experimental" 或 "controlled comparison"；§4.3 开头 acknowledge 残余 confounds。

### Should-Fix（影响评分）

**W1. [Major] Effect size 的 practical significance 在 abstract/intro 未足够突出。** Pairwise r²=1.3-1.7%，typical-batch gap 仅 2.2pp (CI: [0.4, 4.0])。Abstract 主数字已改为 −7.4pp quartile gap，但 pairwise r² 未在 abstract 显式量化。Introduction 仍引用 31.2pp（附 caveat），读者可能仍高估 confusability 的实际影响。R2 提出，R1 部分同意（指出 abstract 已用 −7.4pp，但同意 r² 应更显式）。

**W2. [Major] 正文仅 1 Figure + 4 Tables，关键证据在 appendix。** Error taxonomy（IntraSub ρ=1.0 for NER, 0.954 for RE）是 Channel 2 机制的核心数据点，cross-model BCS 表支撑跨模型验证，但均在 appendix。对于包含六大实验模块的论文，一张双 panel figure 不足以引导读者。**两 Reviewer 共识**，三轮 (Round 1→2→3) 持续提出。

**W3. [Major] MAVEN 反转在 Abstract 中仍仅隐式处理。** Abstract 用 "generally suppresses recall" 处理三个数据集中最大的 (168 types) 反转结果。"generally" 承载过多信息，读者易误读为全部 suppress。**两 Reviewer 共识**，三轮持续提出。建议用半句话显式陈述 MAVEN 反转。

**W4. [Warning] RE clean channel separation 在 abstract/intro 缺 closed-set format caveat。** RE 是 closed-set classification（消除 entity detection 维度），clean separation 可能部分是 task format artifact。Discussion + Limitations #8 已讨论，但 abstract/intro 中 "cleanly separable in RE" 未附加 caveat。R1 REBUT（error taxonomy 提供超越 format artifact 的证据），R2 AGREE。建议 abstract 附加 "possibly reflecting its closed-set format"。

**W5. [Warning] 不同 dataset 使用不同 embedding，缺 cross-embedding sensitivity ablation。** Few-NERD 用 Qwen3 embedding，FewRel/MAVEN 用 MiniLM。MAVEN 在两种 embedding 下方向一致 (Appendix C)，但 Few-NERD+MiniLM 和 FewRel+Qwen3 缺失。R2 提出，R1 AGREE。

**W6. [Warning] §5 SDGD 正文过短 (~100 词/4 句)。** SDGD 是 Contribution 4 但正文篇幅与其地位不匹配。Appendix 有完整 protocol，但读者需翻到 appendix 才能理解 precision 暴跌机制。建议增加一段 merge amplification 的定量分解。**两 Reviewer 共识**，两轮持续提出。

### Minor（锦上添花）

**M1. Pairwise r² → batch-level gap 的信号放大缺 formal 推导。** §practical_magnitude 提供 empirical 数据但无从 pair-level variance 到 batch-level gap 的数学推导。Compounding mechanism 不清楚：additive vs nonlinear？两 Reviewer 共识可放 Appendix。

**M2. MAVEN count-curve 反转三因素归因未量化分解。** Relaxed matching / same-domain context / class imbalance 三因素的相对贡献未分离，与论文在 NER/RE 上追求的 controlled analysis 标准不一致。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全共识：
1. **Prompt sensitivity 是最大 concern** — v2 RE BCS gap CI 含零，需正文讨论 (C1)
2. **"Interventional" → "quasi-experimental"** — 因果语言超出设计支撑 (C2)
3. **正文仅 1 Figure 不够** — 三轮持续问题 (W2)
4. **Effect size practical significance 需更诚实呈现** (W1)
5. **MAVEN 反转需 abstract 显式陈述** (W3)
6. **FewRel closed-set format caveat 需更 prominent** (W4)
7. **Cross-embedding sensitivity 缺失** (W5)
8. **§5 SDGD 过短** (W6)
9. **r² → gap 放大缺形式化** (M1)

## Reviewer Divergence [REBUT]

| 议题 | R1 立场 | R2 立场 | 性质 |
|------|---------|---------|------|
| Within-pool quartile CI 含零 (R1-Q2) | BCS 效应在 typical batches 可能不显著 | Regression slope CI excludes zero (p=0.027)，quartile 不显著是 BCS range compression 的 power 问题 | 技术性分歧——summary statistic 选择，非效应存在性 |
| Effect size abstract framing (W1) | Abstract 已用 −7.4pp，部分同意 r² 应更显式 | 更强调 typical gap 2.2pp 应为主叙事 | 程度之争 |

---

## Questions for Authors

1. **v2 prompt robustness**: v2 RE BCS gap 的 CI 包含零 ([-5.2, +21.5], n=5)。增加 batch 数至 n=25，gap 是否能达到统计显著？若否，论文的 RE confusability claim 如何成立？
2. **Within-pool quartile CI**: quartile Δ CI 也包含零 ([-8.17, +0.38])。regression slope 显著 (p=0.027) 与 quartile 不显著的差异如何解释？
3. **51% floor**: 对于 count=8 的高 BCS batch，random chance = 12.5%。51% 远高于 random guessing，但是否接近 "top-2 confusable types 间的 coin-flip" baseline？
4. **Embedding choice**: NER 用 Qwen3 embedding，RE 用 MiniLM。选择依据是什么？Few-NERD+MiniLM 的 SCS-confusion correlation 方向和大小如何？
5. **SDGD + v2 prompt**: SDGD 全部使用 v1 prompt。v2 的 higher precision 是否可能缓解 merge amplification？Appendix B Table A4 有 v2 结果但未在 §5 讨论。
6. **Actionable threshold**: SCS/BCS 在什么阈值以上才值得干预？2.2pp typical gap 是否有 actionable 决策边界？
7. **MAVEN 归因分解**: Relaxed matching / same-domain context / class imbalance 三个归因中，哪个贡献最大？能否通过 exact matching 隔离因素 (i)？

---

## Missing References

- **Chia et al. (2022)** "RELATIONPROMPT: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction" — zero-shot RE prompt-based approach，与 FewRel 实验设计相关 (R1 提出)
- **Li et al. (2023)** "Evaluating ChatGPT's Information Extraction Capabilities" — R1 检索时 arXiv 版本状态不确定，建议确认 DOI 或出版状态

---

## External Review (Stanford Agentic Reviewer)

未启用。项目配置未开启外部审稿。

---

## Overall Assessment

**评分: Weak Accept (3.5/5)**
**置信度: 4/5**

**R1 评分**: Overall 3.5, Soundness 3.5, Excitement 3.0, Confidence 4
**R2 评分**: Overall 3.5, Novelty 3.5, Excitement 3.0, Confidence 4

### 核心判断

论文从 Round 2 (borderline 3.0) 提升至 Round 3 (weak accept 3.5)。**所有 Round 2 Critical issues (6个) 均已解决**，这是实质性进步：
- MW1: Abstract 改用 bootstrapped CI ✓
- MW2: §practical_magnitude 校准 typical vs extreme effect ✓
- SW3: Appendix D 公开完整 prompt template ✓
- m3: Responsible NLP Checklist 完整 ✓
- R2-N3-80rel: 31.2pp 全文标注 extreme-batch ✓
- REF1: 引用修正 ✓

**新发现的两个 Critical issues (R3-C1, R3-C2) 本质上是 framing 问题而非方法论缺陷**——论文的实验数据是完整的（v2 结果存在于 Appendix F），问题在于正文叙事未充分展现这些数据。这与 Round 2 的 Critical issues（数据缺失、checklist 缺失、prompt 未公开）性质不同，修复成本较低。

**升级为 weak accept 的理由**：
1. 实验设计 (count curves + BCS-controlled + within-pool) 是该领域的方法论标杆
2. 统计方法全面且透明（cluster bootstrap、permutation test、selection bias 警告）
3. 诚实报告 modest effects 和负面结果
4. Centrality confound 分析有独立贡献
5. Prompt template 完整公开，可复现性显著改善

**阻止进一步升分的因素**：
1. 核心效应量小（r²=1.3-1.7%，typical gap 2.2pp），practical significance 有限
2. v2 prompt 下 RE 核心效应 CI 含零——confusability 的 practical magnitude 高度依赖 prompt design
3. 最清晰的证据来自 RE closed-set classification，external validity 受限
4. 三轮持续未解的正文视觉支持不足
5. SDGD 负面结果意味着论文缺少 actionable engineering solution

**推荐**: 修复 C1 (v2 讨论上移正文) 和 C2 ("interventional" → "quasi-experimental") 后，适合 **EMNLP 主会**。当前版本已是 **Findings track 的安全候选**。

### 与 Round 2 的变化

| 维度 | Round 2 | Round 3 | 变化 |
|------|---------|---------|------|
| Overall | 3.0 (borderline) | 3.5 (weak accept) | +0.5 |
| Critical issues | 6 个 open | 6 个 resolved, 2 个 new (framing) | 实质性改善 |
| Prompt transparency | 未公开 | Appendix D 完整 | 完全解决 |
| Statistical annotation | 部分缺失 | CI/caveats 全面 | 显著改善 |
| Framing | "framework" overclaim | "pattern/decomposition" | 恰当降格 |
| 主要 gap | 数据缺失 + prompt 混淆 | v2 attenuation 讨论 + 因果语言 | 从数据层面转向叙事层面 |

---

## Detailed Comments by Section

### Abstract
- 主数字已改为 −7.4pp quartile gap (CI: [−9.4, −5.5]) ✓
- "generally suppresses recall" 仍隐式处理 MAVEN 反转 → 需半句显式陈述
- Pairwise r²=1.3-1.7% 未出现 → 建议加入让读者校准期望
- "cleanly separable in RE" 未附 closed-set format caveat

### Introduction
- RQ1-RQ3 清晰，实验有对应回答 ✓
- Contribution 1 已改为 "pattern"/"decomposition" ✓
- Finding (2) 引用 31.2pp 附带 typical-batch caveat ✓，但未注明 v2 结果
- Contribution 4 "structural challenge" 已限定为 NER ✓

### Related Work (§2)
- 覆盖 2023-2025 zero-shot IE 主要工作 ✓
- LLM-PEE 差异化清晰 ✓
- Sentence-BERT、Li et al. 2023、Wadhwa et al. 2023 补充状态需确认
- 缺 Chia et al. 2022 (RELATIONPROMPT)

### Experimental Setup (§3)
- SCS/BCS 定义清晰 ✓
- Within-pool 控制设计精良 ✓
- §3.5 prompt 描述改善，Appendix D 完整 ✓
- Embedding 选择依据未说明（Qwen3 vs MiniLM 在不同 dataset 上的使用）

### Results (§4)
- §4.1 count curves: NER non-monotonicity 已报 CI ✓；MAVEN 反转需更多正文讨论
- §4.2 pairwise: r² framing 已改善 ✓；cluster bootstrap 已加入 ✓
- §4.3 BCS-controlled: within-pool 分析是亮点 ✓；"interventional" 语言需修改；v2 attenuation 需正文讨论
- §4.4 error taxonomy: IntraSub 数据有力 ✓；建议移部分入正文
- §4.5 centrality confound: 独立贡献 ✓
- §practical_magnitude: 有效校准 typical vs extreme ✓

### SDGD (§5)
- 正文仍仅 ~100 词，与 Contribution 4 地位不匹配
- Appendix B 完整，但正文缺 merge amplification 的定量分解

### Discussion (§6)
- Boundary conditions 讨论合理 ✓
- 51% floor 已标注为 hypothesis ✓
- "consistent across tested models" 替换完成 ✓
- v2 attenuation 提及但可更 prominent

### Limitations
- 8 条，结构清晰 ✓
- Item 5 (SDGD scope) 明确限定 ✓
- Item 7 (FewRel scope) 明确 ✓
- Item 8 (RE format specificity) 明确 ✓

### Format Compliance
- 页数: 8 页正文 + references + appendix ✓
- 匿名: 完全匿名 "Anonymous ACL submission" ✓
- Checklist: 完整 A1-E1 ✓
- ACL [review] 格式 ✓
- 引用: 43 篇，无 orphan/missing ✓

---

## Round 2 → Round 3 Issue Resolution Summary

### Resolved (Round 2 Critical → Round 3 PASS): 6/6
| ID | Issue | Verification |
|----|-------|-------------|
| MW1 | 16-rel 单 batch 无 CI | PASS — Abstract 改用 bootstrapped CI |
| MW2 | 信号放大缺论证 | PASS — §practical_magnitude |
| SW3 | v1/v2 prompt 混淆 | PASS — Appendix D 完整 |
| m3 | 缺 Checklist | PASS — checklist.tex 完整 |
| R2-N3-80rel | 31.2pp headline | PASS — 全文标注 extreme-batch |
| REF1 | 引用占位符 | PASS — 已修正 |

### Resolved (Round 2 Warning/Info → Round 3 PASS): 4
| ID | Issue | Verification |
|----|-------|-------------|
| R2-W4-sdgd-scope | SDGD 仅 NER | PASS — Limitations #5 |
| R2-W1-framework | "framework" overclaim | PASS — 全文替换 |
| D037-m1-checklist | checklist.tex 'framework' | PASS |
| R2-W7-51floor | 51% floor 推测性 | PASS — 标注 hypothesis |

### Partially Resolved: 3
| ID | Issue | Status |
|----|-------|--------|
| MW4 | 正文仅 1 Figure | 仍仅 Figure 1 |
| SW4 | MAVEN abstract | 仍用 "generally" |
| R2-m-sdgd-short | §5 过短 | 仍 ~100 词 |

### New Issues (Round 3): 7
| ID | Severity | Summary |
|----|----------|---------|
| R3-C1 | Critical | v2 prompt 下 RE gap CI 含零，正文未充分讨论 |
| R3-C2 | Critical | "interventional" 因果语言 |
| R3-W1 | Warning | Effect size practical significance 未在 abstract 突出 |
| R3-W5 | Warning | Cross-embedding sensitivity 缺失 |
| R3-W3 | Info | r² → gap 放大缺 formal 推导 |
| R3-W6 | Info | MAVEN 反转归因未量化 |
| R2-W5-RE-artifact | Warning (reopened) | RE classification caveat 缺 abstract |