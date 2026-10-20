---
round: 3
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-20T13:21:27.432763+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Round 5 (Fresh Review)

**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Fail in LLM Reasoning"
**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
**Reviewers**: R1 (方法严谨性 + 实验有效性), R2 (新颖性 + 完整性 + 论文质量)
**审稿模式**: Fresh (重新审稿)

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取 FOL 约束并通过 Z3 MAX-SAT 聚合。在 6 个模型（7B-32B）、3 个推理域、3000+ 条件评估中，发现自提取约束无法超越 majority voting。核心发现包括：(1) symbolic confirmation bias（83.3% 错误约束支持错误多数答案）；(2) independence-accuracy trade-off（κ≥0.40 across three model families）；(3) process-level independence bottleneck（CoT cosine 0.69 >> answer κ 0.41）。Oracle controls 确认聚合机制 sound（+14.22pp FOLIO, +11.50pp ProofWriter）。论文还报告了两个正面发现：constraint-answer decoupling（interim Δ=+11.3pp）和 cross-architecture NLI verification（Δ=+3.43pp, p=0.039）。

---

## Strengths

**S1. 实验规模罕见的全面。** 6 个模型、3 个推理域、~1,250 unique instances、4-seed replication、15+ distinct 补救策略（含 prompt-level, method-level, additional directions）。这种穷举性搜索为社区提供了有价值的负面证据，减少重复劳动。[R1, R2 一致]

**S2. 统计方法论强于该领域平均水平。** McNemar exact tests、10,000-resample bootstrap CIs、formal power analysis（Appendix D 诚实承认 underpowering）、4-seed replication。这是负面结果论文的方法论标杆。[R1, R2 一致]

**S3. Oracle controls 设计精妙。** Gold FOL/DSL 替换有效隔离 extraction vs aggregation bottleneck。Z3 agreement rate（95.1% FOLIO, 97.1% ProofWriter）验证了转换保真度。[R1, R2 一致]

**S4. "Symbolic confirmation bias" 概念有独立价值。** 83.3% 错误约束支持错误多数答案、4.97× bias ratio、94% error overlap with SC——量化清晰、跨模型可复制（3 families）、可测试。[R1, R2 一致]

**S5. Condorcet 理论框架优雅。** CJT + Effective-K 为 SC 的 saturation 行为提供了理论解释，尽管 κ→ICC 代理需更强论证。[R1]

**S6. 高度透明的报告。** Power analysis、bootstrap CI、seed sensitivity、computational cost 完整报告。Case studies（Appendix F）和 constraint quality 对比（Appendix R）提供了可复现所需的细节。[R1, R2 一致]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] §4.1 Decoupling 实验报告未完成的 interim results（n=70/204）** [R1-N2 + R2-N1, 完全共识]

论文在 Abstract、Introduction（Contribution 4）、§4.1、Conclusion 中均报告了一个仅完成 34% 的实验（Δ=+11.3pp over SC, +6.4pp over SICA）。这是论文仅有的两个正面发现之一，直接支撑 "breaking confirmation bias" 叙事线。

审稿人无法评估一个未完成实验的真实效果。更关键的是：若 full-scale 确认 Δ≈+11pp，将直接推翻核心 claim——因为 decoupling 仍是同一模型的 self-extraction（只是去除了结论信息），说明问题不在 self-extraction 本身而在提取时看到了自己的答案。这会根本性地改变论文定位。

→ **建议**: 投稿前完成实验。若无法完成，删除 §4.1 相关内容（Abstract/Intro/Conclusion 中均需修改），将 decoupling 作为 future work 在 Discussion 中简述。

**[MF-2] Oracle "24% ceiling" 跨模型比较不成立** [R1-N1, R2 交叉回应完全同意]

Oracle 实验仅在 Qwen2.5-14B 上运行（SC=75.49%, Δ=+14.22pp），但 "24% ceiling" 将此与 Mistral-7B 的自提取结果（SC=55.88%, Δ=+3.43pp）对比。两个模型基准准确率相差近 20pp，oracle gain 天花板是模型依赖的。该比较出现在 Abstract、Introduction、§5.3，是核心量化结论之一。

→ **建议**: 在 Mistral-7B FOLIO 上运行 oracle 实验（技术可行，FOLIO 有 gold annotations），报告同模型 ceiling；或改为定性陈述，不给出具体百分比。

**[MF-3] Discussion（~100 词）和 Conclusion（~60 词）对负面结果论文严重不足** [R2-N4, R1 交叉回应同意]

负面结果论文的核心价值在于 insight 深度。当前 Discussion 仅复述发现，缺少：(a) 对 neuro-symbolic reasoning 研究议程的 broader implications；(b) 在什么条件下 self-extraction 可能 work（更大模型？不同架构？trained extractors？）；(c) 与 CoT faithfulness 文献的联系（Turpin et al. 2024）；(d) 与经典 ensemble diversity 文献的关系（Krogh & Vedelsby 1995）。

→ **建议**: 扩展 Discussion 至≥2 段实质内容；Conclusion 增加 community-level takeaway。修复 §3/§5 内容重复可释放 ~0.5-0.7 页空间。

### Strong Should-Fix（影响评分）

**[SF-1] "Fundamental" independence-accuracy trade-off overclaim** [R2-N2(must-fix), R1 partially agrees(should-fix)]

Pareto frontier 仅基于 4 种聚合方法在 Mistral-7B 上 + 3 个模型家族（均 7B-14B）在单一 benchmark（FOLIO, n=204）上的 7 个数据点构建。"Fundamental" 暗示理论上不可避免，但 Limitations 明确承认未测试 70B+。R1 认为措辞修改即可，R2 认为严重性更高。

→ **建议**: 将 "fundamental" 替换为 "persistent"/"empirical"；称 "observed trade-off pattern" 而非 "Pareto frontier"；添加显式 scope qualifier "at the 7B-32B scale tested"。

**[SF-2] Cross-architecture DeBERTa PoC 统计脆弱** [R2-N3(must-fix), R1-W1(should-fix)]

p=0.039 来自仅 9 个 discordant pairs（b=1, c=8）。McNemar 在 discordant n<25 时 power 极低。p=0.039 在 15+ 条件的多重比较下无法存活（Bonferroni threshold ~0.003）。单一 benchmark、单一 LLM、单一外部模型，无跨数据集/跨模型 replication。这是论文唯一 p<0.05 的正面结果。

→ **建议**: 弱化 Abstract/Introduction 中的措辞（"demonstrating" → "suggesting"）；增加 discordant-pair 数量的 caveat；若可行，在 ProofWriter 上复制。

**[SF-3] Variable name isolation confound 未与 confirmation bias 区分** [R1-W3, R2 强烈同意]

56.4% 的跨答案约束对共享零个 Z3 变量——MAX-SAT 退化可能不是因为 confirmation bias，而是因为变量名不一致导致 Z3 无法检测跨 trace 语义矛盾。Oracle 成功部分可归因于 gold FOL 使用规范变量名（此为另一 confound）。两种解释有不同实践含义——若是变量名问题，canonical normalization 可能解决而无需外部模型。缺少 canonicalization 消融是实质性缺陷。

→ **建议**: 添加 canonical variable normalization 消融实验，以区分 confirmation bias 和 variable isolation 各自的贡献；或在 Discussion 中将此作为重要 confound 充分讨论。

### Should-Fix

**[W1] Fleiss' κ 作为 ICC 代理缺乏形式化论证** [R1-W2, R2 agrees]
Eq.1 直接将 κ 代入 Kish design-effect formula，但 ICC 和 κ 是不同的统计量。之前的修复（添加 Kish 引用 + 渐近等价注记）被本轮 Reviewer 认为不充分。
→ 建议: 增加 caveat "K_eff serves as a qualitative indicator" 或换用 ICC/Krippendorff's alpha。

**[W2] 缺失经典 ensemble diversity 文献** [R2-W1, R1 agrees]
Independence-accuracy trade-off 正是 Krogh & Vedelsby (1995) ambiguity decomposition 和 Brown et al. (2005) diversity survey 在 LLM traces 上的重述。未引用这些奠基性工作削弱理论可信度。
→ 建议: 在 Related Work 或 Discussion 中引用并讨论。

**[W3] §3/§5 内容重复浪费 ~0.5-0.7 页** [R1-W4, R2 agrees]
实验设置和 Oracle Control 描述在 method.tex 和 experiments.tex 中几乎重复。
→ 建议: 合并为一处，释放空间用于 Discussion 扩展。

**[W4] "25+ strategies" 计数膨胀** [R2-W3, R1 partially agrees]
计数包括 4 seeds、4 temperatures、multi-temperature combination 等超参数变体。诚实计数 ~15-20 个 distinct strategies。
→ 建议: 改为 "more than fifteen distinct strategies across multiple hyperparameter settings"。

**[W5] 代码/数据发布未提及** [R1-W5, R2 agrees]
→ 建议: 在 Limitations 或脚注中声明发布计划。

**[W6] 论文组织：Solutions (§4) 出现在 Experiments (§5) 和 Analysis (§6) 之前** [R2-W2, R1 agrees]
读者在看到负面结果前就遇到 proposed fixes，削弱叙事弧（"先给药再诊断"）。
→ 建议: 重排为 Method → Experiments → Analysis → Solutions → Discussion。

**[W7] Process-level κ (TF-IDF) 局限性在主文中讨论不足** [R2-W4, R1 partially agrees]
TF-IDF 遗漏语义相似性，但 R1 指出这意味着真实 process similarity 可能更高（强化论点）。
→ 建议: 在 §6.3 增加 caveat 并明确 TF-IDF 是 lower bound。

**[W8] CJT 新颖性定位 / Huang-Stechly 区分不足** [R2-W6, R1 partially agrees]
Lefort et al. (2024) 已将 CJT 应用于 LLM。Symbolic confirmation bias 与 Huang et al. (2024) self-correction / Stechly et al. (2025) self-verification 的实质区别（量化机制 4.97× bias ratio + 穷尽性搜索 + independence-accuracy framework）需在 §2 中更锐利地阐明。

### Minor

- Table 1: Bold formatting inconsistent — caption defines "Bold Δ: p < 0.05" but two rows bold SICA accuracy with non-significant Δ
- LINC "~40% translation errors" 表述可能不够精确
- GSM8K (n=30), AIME (n=22) 在 Table 1 中给读者虚假广度印象，建议移至 Appendix
- "Capability trap" 术语出现在 Appendix 但未在正文中使用
- Appendix label 重复（\label{sec:oracle} 出现两次）
- 9 条引用有 first_author 格式差异（minor metadata issues）

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
1. §4.1 interim results 不可接受 — 必须完成或删除 [R1-N2 = R2-N1]
2. Oracle "24% ceiling" 跨模型比较无效 [R1-N1, R2 cross-AGREE]
3. Discussion/Conclusion 过薄 [R2-N4, R1 cross-AGREE]
4. Variable name isolation confound 需要控制 [R1-W3, R2 cross-AGREE]
5. 缺失 ensemble diversity 文献 [R2-W1, R1 cross-AGREE]
6. §3/§5 内容重复 [R1-W4, R2 cross-AGREE]
7. Table 1 粗体格式不一致 [R1-minor = R2-W5]
8. Solutions 应置于 Analysis 之后 [R2-W2 = R1-minor]
9. 代码/数据未提及 [R1-W5, R2 AGREE]

## Reviewer Divergence

以下问题实质一致但严重性定级有分歧：
1. **"Fundamental" overclaim**: R2 定为 must-fix，R1 定为 should-fix（认为措辞修改即可）→ 本报告定为 Strong Should-Fix
2. **DeBERTa PoC 统计脆弱**: R2 定为 must-fix，R1 定为 should-fix（认为 PoC 定位已诚实且报告了 discordant pairs）→ 本报告定为 Strong Should-Fix
3. **"25+ strategies" 计数**: R1 估计 ~18-20 distinct，R2 估计 ~12-15 → 均同意存在膨胀，差异在程度

无实质性 [REBUT] 分歧。

---

## Questions for Authors

1. 是否有计划在 Mistral-7B 上运行 oracle 实验以获得同模型 ceiling 比较？
2. Decoupling 实验（exp-wave3-dir-g-decoupling）完整结果预计何时可得？
3. 是否考虑过 variable canonicalization 步骤以区分变量名隔离和 confirmation bias？
4. "Symbolic confirmation bias" 与 Huang et al. (2024) "LLMs cannot self-correct reasoning" 之间的实质区别是什么？
5. 为什么不测试 best-of-N with reward models 作为 baseline？
6. 是否考虑过 adversarial prompts（如 "find constraints that would DISPROVE the conclusion"）？
7. 对 reasoning-specialized models at larger scale（如 o1/o3 蒸馏、DeepSeek-R1-70B）的预期如何？

---

## Missing References

1. **Krogh & Vedelsby (1995)**: "Neural Network Ensembles, Cross Validation, and Active Learning" — ensemble diversity-accuracy trade-off 理论基础 [R2-W1, R1 agrees]
2. **Brown, Wyatt, Harris & Yao (2005)**: "Diversity Creation Methods: A Survey and Categorisation", Information Fusion — 直接相关 [R2-W1, R1 agrees]
3. **Turpin et al. (2024)**: "Language Models Don't Always Say What They Think" — CoT faithfulness [R2]

---

## External Review

**外部审稿（Stanford Agentic Reviewer）**: 未请求（项目未配置 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~3 分钟）。0 critical, 2 warning, 10 info。

**Warnings:**
- Pages 1-3 连续纯文本无任何 display item。审稿人前 2 分钟只看到文字墙，缺乏视觉锚点。建议将 Figure 1（SICA 管线图）前移至 p.2 或在 Introduction 中加入 teaser figure / 核心结果概览表。
- Page 20 Figure 4（intervention strategies 横向条形图）占页面 ~2/3，底部 ~1/3 空白。附录内影响较小。

**Info（选摘）:**
- Figure 1 管线图 "Red dashed box" 内文字在打印尺寸下偏小
- Figure 2 散点图压缩在单栏右下角，数据点标签在打印时可能难以辨认
- Tables 8-11 密集排布字号偏小（附录内可接受）
- 公式渲染正确，无 LaTeX 错误残留，无 margin 溢出

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**置信度**: 4/5（两位 Reviewer 均熟悉 SC、CJT、neuro-symbolic reasoning 方法论）

**评分依据**:

本文在实验方法论上达到了很高的标准——6 个模型跨 3 个域的系统性负面结果搜索、25+ 补救策略的穷举性测试、严格的统计报告（McNemar、bootstrap CI、power analysis、4-seed replication）——是负面结果论文的方法论标杆。"Symbolic confirmation bias" 概念清晰量化且可复制，有独立价值。Oracle control 设计精妙地隔离了 extraction vs aggregation bottleneck。

然而，三个 Must-Fix 问题阻止 Conference 级别接收：

1. **未完成实验入正文**：§4.1 Decoupling 仅完成 34%（70/204），但 Δ=+11.3pp 被写入 Abstract、Introduction（Contribution 4）和 Conclusion。这既是诚信问题（审稿人无法评估未完成实验），也是叙事一致性问题（若确认，将推翻核心 claim）。

2. **核心量化结论方法论缺陷**："24% oracle ceiling" 跨模型比较（Mistral-7B self-extraction vs Qwen2.5-14B oracle）在统计上不成立。

3. **Insight 深度不足**：Discussion 和 Conclusion 合计 ~160 词，对于一篇负面结果论文严重不足。缺少 broader implications、与经典文献的联系、forward-looking analysis。

此外，variable name isolation confound（SF-3）是一个实质性方法论问题——56.4% 跨答案约束对共享零个 Z3 变量，这意味着 MAX-SAT 退化可能并非（完全）因为 confirmation bias，而是因为变量名不一致。

**论文的 novelty 本质上是 "self-verification/self-correction 在 symbolic extraction 中也不 work"——在 Huang et al. (2024) 和 Stechly et al. (2025) 之后这并不令人意外。** 本文的增量价值在于量化机制（4.97× bias ratio）和穷举性搜索，这足以支撑 Findings 但不足以支撑 Conference。

**若修复 MF-1（完成或删除 decoupling）、MF-2（同模型 oracle）、MF-3（扩展 Discussion），并弱化 overclaim，论文有潜力达到 3.5（Borderline Conference）。**

---

## Detailed Comments

### Abstract
- 第 8 行 "self-extraction captures only 24% of this ceiling" — 跨模型比较，需修正 [MF-2]
- 第 9 行 "achieving +11.3pp over SC and +6.4pp over standard SICA on interim results" — 未完成实验 [MF-1]
- "more than twenty-five remediation strategies" — 计数膨胀 [W4]

### §1 Introduction
- Line 23: "self-extraction captures only 24% of this ceiling" — 同 MF-2
- Line 27: "+11.3pp over SC" on interim results — 同 MF-1
- Line 36: "Independence-Accuracy Trade-off" contribution — "fundamental" overclaim [SF-1]
- Line 38: Contribution 4 "Constraint-Answer Decoupling" based on incomplete data — 同 MF-1

### §2 Related Work
- "CJT and ensemble diversity" paragraph: 缺少 Krogh & Vedelsby (1995), Brown et al. (2005) [W2]
- Lefort et al. (2024) 引用后未充分区分本文 CJT 应用的增量 [W8]
- 与 Huang et al. (2024), Stechly et al. (2025) 的实质区别不够锐利 [W8]

### §3 Method
- §3.1 Eq.1: κ→ICC 代理无形式论证 [W1]
- §3.3 Oracle Control Design 与 §5.3 重复 [W3]
- §3.4 Cross-Architecture Method 描述与 §4.2 重复 [W3]

### §4 Breaking Confirmation Bias
- 此节出现在 Experiments/Analysis 之前，叙事顺序问题 [W6]
- §4.1 Decoupling: interim results (n=70/204) [MF-1]
- §4.2 DeBERTa PoC: 9 discordant pairs, "demonstrating" → "suggesting" [SF-2]

### §5 Experiments
- §5.1 Setup 与 §3 大量重复 [W3]
- §5.3 Oracle: "24% ceiling" 跨模型 [MF-2]
- Table 1: Bold formatting inconsistent [Minor]

### §6 Analysis
- §6.2: 56.4% zero-variable overlap 的 variable name isolation 解释被忽略 [SF-3]
- §6.3: TF-IDF 局限性讨论不足 [W7]
- §6.5 Table 4: 7 个数据点称 "Pareto frontier" [SF-1]

### §7 Discussion
- 仅 ~100 词，严重不足 [MF-3]
- 缺少 broader implications, forward-looking analysis [MF-3]

### §8 Conclusion
- 仅 ~60 词 [MF-3]
- "constraint-answer decoupling...breaks confirmation bias" 基于 incomplete data [MF-1]

### Limitations
- 内容适当但缺少 code/data release 声明 [W5]
- 未提及 variable name isolation confound [SF-3]