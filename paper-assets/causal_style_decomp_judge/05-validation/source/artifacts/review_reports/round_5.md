---
round: 5
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T17:44:54.949349+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6 (Fresh Review)

**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**目标 Venue**: EMNLP 2026 Long Paper (ARR)
**截止日期**: 2026-05-25
**Reviewer**: R1 (方法严谨性/实验设计) + R2 (新颖性/Related Work/写作质量)
**审稿模式**: Fresh（独立全新审稿）

---

## Summary

本文提出 Controlled Style Decomposition (CSD)，一个检测 LLM judge 隐藏风格偏差的黑盒框架。CSD 通过三阶段流程——style-controlled rewriting、NLI-gated content preservation、position-controlled pairwise comparison——系统量化 per-axis style bias。核心发现是 "Likert Blindspot"：在相同数据上，Likert 评分（ATE）系统性地遗漏 pairwise comparison 能检测到的风格偏差（BT 63–84%, p < 0.001 vs Likert p > 0.17），由七种统计方法交叉验证。GEE conditional decomposition 进一步揭示 per-axis confound structure：verbosity 为 style-dominated，formality 为 conditional（style + originality confound），register 为 judge-dependent。在 4 个 judges（3 target + 1 negative control Claude Sonnet 4）、3 benchmarks、3 style axes 上验证。

---

## Strengths

**S1. 研究问题精准且对社区有直接实践价值** [R1, R2 共识]
Likert Blindspot 的发现直接挑战了 RATE 等基于 Likert ATE 的 bias 评估方法的有效性，对 evaluation community 有即时方法论指导意义。

**S2. 统计框架严谨且多层次** [R1 主导]
七种统计方法交叉验证（Table 2），Holm-Bonferroni 校正 + exploratory/confirmatory 分类，GEE conditional decomposition（Table 3），Bootstrap CI 10,000 resamples，BT GoF 检验，NLI 11-threshold sensitivity sweep，TOST 等价性检验。统计密度显著高于同领域平均水平。

**S3. 实验设计周全，多重控制有效约束替代解释** [R1, R2 共识]
六个独立控制（NLI gate ablation 反转至 41.7%、Claude 负控制无 bias、cross-axis BT 变异不一致 uniform amplification、rewriting artifact 被 GEE 吸收、debiased prompting 部分降低 bias、三架构一致）有效约束了替代解释空间。Claude Sonnet 4 作为 negative control 增强了 discriminative validity。

**S4. Per-axis confound structure 是方法论增量贡献** [R1 主导]
GEE 条件分解区分了 style-dominated（verbosity: Style OR 8–13, Orig OR <1）、conditional（formality: 显著 style 和 originality effects）和 judge-dependent（register）三种模式，超越了 aggregate bias score。

**S5. Related Work 覆盖全面且定位清晰** [R2 主导]
Jeong et al. (2025) Comparative Trap、Stureborg et al. (2024)、Park et al. (2024) 等关键文献均被讨论。与 RATE、CASSE、FairJudge 的差异化清晰。

**S6. 写作清晰、学术诚实** [R2 主导]
§3.5 Design Rationale 的因果声明 disclaimer、Limitations 的三段式讨论（quality-style confounding、evaluator-producer bias、validation methodology）体现了较高的学术诚实度。Appendix 提供了充分技术细节。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. 主正文超过 8 页限制** [R2 发现, R1 交叉确认] — format, critical
Section 6 (Conclusion) 约 5–6 行溢出到 page 9。EMNLP 2026 规定主正文 strict 8-page limit，Limitations 和 Ethics 不计入但 Conclusion 计入。严格执行下可导致 desk rejection。
→ 建议压缩 §5.6 或 §6 文本（约 6–7 行）。

**MF2. NLI gate 缺乏人工评估验证** [R1 Must-Fix, R2 同意但建议降级 strong Should-Fix] — method, critical
整个框架的有效性依赖 NLI gate 正确分离 style 与 content 变化，但验证完全自动化（Qwen3-32B annotator + GPT-4o cross-validation 92.1%/82.6% precision）。没有人工评估验证 NLI gate 的 pass/fail 决策是否与人类判断一致。DeBERTa-v3-large 在 style-shifted text 上可能与标准 NLI 数据行为不同。
缓解因素：NLI ablation（Appendix N）formality NLI-fail pairs 反转至 41.7% 是较强间接验证；11-threshold sweep ≤3pp 变动证明 threshold 不敏感。
→ 建议随机抽取 50 对 pass/fail 样本，2+ annotator 评估，报告 IAA。

**MF3. Evaluator-producer bias 22% OR 下降处理不充分 + register 轴缺失 cross-rewriter test** [R1 Must-Fix, R2 同意] — method, critical
Qwen3-32B rewriter→GPT-4o 后 verbosity Style OR 下降 22%（13.10→10.17），论文定性为"bounding"但 22% non-trivial。Register 轴完全缺失 cross-rewriter test，而 register 恰是 judge-dependence 最强的轴。核心 Blindspot pattern 在 GPT-4o rewriter 下保持（BT .735, Likert p=.838），说明不影响定性结论但影响效应量估计精度。
→ 建议：(1) 提供 producer-corrected 效应估计范围；(2) Limitations 明确标注 register 缺乏 producer-independence 验证。

### Should-Fix（影响评分但非一票否决）

**SF1. Novelty claim "first systematic quantification" 过度宽泛** [R2 Must-Fix, R1 降级 Should-Fix → Director 判定 Should-Fix]
Pairwise > Likert 灵敏度是 Thurstone (1927) 以来的经典结论；Kiritchenko & Mohammad (2017)、Novikova et al. (2018) 已证明 forced-choice 在 NLG 评估中更灵敏；框架各组件均有先例。R1 反驳：LLM judges 的特殊性（确定性评分、无疲劳效应、不同 scale anchoring）使 domain transfer 非 trivial，且论文贡献包括 per-axis GEE decomposition。
→ 建议将 "first" 限定到具体方法组合的 novelty；明确承认核心洞见是 domain transfer + systematic quantification。

**SF2. Comparative Trap 张力在 Conclusion 处理不足** [R2 发现, R1 交叉同意]
§2 和 §5.2 已讨论 Jeong et al. (2025) 并提供 6 个控制约束 amplification 风险，但 §6 推荐 "style bias audits should adopt content-controlled pairwise comparison" 措辞仍过强。
→ 建议加入明确 caveat。

**SF3. 因果术语（"interventional framework"）与实际 filtering-based 方法存在张力** [R1 W3, R2 W2 独立标注]
§3.5 的 hedging 适当，但 Abstract "black-box interventional framework" 和 Introduction 多处使用强因果语言，与 §3.5 的 disclaimer 不一致。
→ 建议统一为 "quasi-interventional" 或 "controlled" framework。

**SF4. 样本量偏小且 scaled replication 覆盖面窄** [R1 W4, R2 W3 共识]
LLMBar n=100（post-NLI n=88）为主数据源，MT-Bench n=30。n=355 scaled replication 仅覆盖 Qwen3-32B formality。
→ 建议在 Conclusion 更明确标注 generalizability 边界。

**SF5. TOST equivalence bound (Δ=15pp) 缺乏独立外部 justification** [R1 W1, R2 同意]
用同研究 treatment effects 设定 control 的 equivalence bound 形成循环论证。
→ 建议引用外部 style bias 基准。

**SF6. Identification assumption (iii) 讨论不充分** [R1 W5, R2 同意]
"Rewrite introduces no systematic differences beyond target axis"——same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。

### Minor Issues

- **M1**: Abstract 信息密度过高——OR 值等技术细节不利于可读性 [R2 Should-Fix, R1 Minor → 分歧]
- **M2**: BT IIA 在 formality 轴可能被违反（Fisher p=0.015 方向不对称）[R1 Should-Fix, R2 Minor → 共识 Minor]
- **M3**: Figure 2 (DAG) 和 Figure 3 (forest plot) 黑白打印下颜色/形状区分不足 [R1, R2 共识]
- **M4**: Appendix Table 5 (GEE CI) 部分条目缺失 95% CI [R2]
- **M5**: Table 1 第 6 列无 header，Blindspot 标记缺说明 [R2]
- **M6**: Introduction contributions 列表每条过长（3–5 行）[R2]
- **M7**: bib key wu2023style 年份与 venue 年份不一致 [R2]

---

## Questions for Authors

1. NLI gate 在不同 rewrite directions（formal→casual vs casual→formal）上的 entailment score 分布是否存在系统差异？如果 formal text 系统性获得更高 NLI score，这会否引入 selection bias？
2. 22% OR 下降中有多少可归因于 GPT-4o 的 style transfer 质量差异 vs 真实 self-preference？如果使用 rule-based rewriting，效应量可能进一步缩小？
3. Register 轴的 judge-dependence 在缺乏 cross-rewriter test 的情况下，如何排除 evaluator-producer confound 而非 genuine judge-specific sensitivity？
4. 100-point continuous Likert 仍检测不到 Blindspot（tie rate 65.9%）——这是否说明 LLM judges 本质上倾向给"中性"评分，而非 absolute vs relative evaluation paradigm 差异？
5. 如果 pairwise 本身存在 format amplification（Comparative Trap），"moderate" effects (BT 63–67%) 的真实效应量可能更小——数据层面能否进一步区分 "Likert misses real bias" vs "pairwise creates apparent bias"？

---

## Missing References

**已覆盖的关键文献** [R2 验证]：Jeong et al. (2025) Comparative Trap ✓、Stureborg et al. (2024) ✓、Park et al. (2024) OffsetBias ✓
**建议补充**：
- Shi et al. (2024) "Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges"
- Bavaresco et al. (2024) "LLMs Instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks"

引用验证摘要 [R2]：50 条 bib entries, 41 verified, 3 not_found (likely indexing issues), 6 minor mismatches, 0 missing_bib。引用质量良好。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 已跳过（用户未提交至 paperreview.ai）。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（2 warnings, 6 info）

关键发现：
- **[warning]** Pages 3–4 连续 2 页纯文本（Related Work + Method 开头），无 display item 穿插。建议在 Method 段加入示意图或示例表。
- **[warning]** Figure 2 (DAG) 尺寸偏小，仅占单栏约 1/4 高度。作为方法论核心论据，建议放大或跨栏展示。
- **[info]** Table 1 脚注区域信息密度极高（4 个符号系统压缩在 3 行）。
- **[info]** Figure 1 内部文字标签字号偏小（正文 60-65%）。
- **[info]** Appendix 表格密度极高（每页 3-4 个 table）。
- **[info]** References 置于 Appendix 之后（更常见做法是 main text → References → Appendix）。

---

## Overall Assessment

### Reviewer Consensus [AGREE]
- **Overall 3.5 (Borderline Conference)** — 两位 Reviewer 独立给出完全一致评分
- **Soundness 3.5** — 统计框架严谨但 NLI gate 缺人工验证、evaluator-producer bias 处理不充分
- **Reproducibility 4** — 方法细节完整，承诺代码/数据公开
- 页数超限是 hard constraint，必须在提交前修复
- NLI gate 人工验证是框架基石的验证缺口
- Evaluator-producer bias 22% OR 下降 + register 缺失需要更诚实的处理
- Novelty 主要为 domain transfer，但 LLM judge 场景的系统量化 + CSD 方法组合仍有增量价值

### Reviewer Divergence [分歧点]
1. **NLI gate 严重性**: R1 Must-Fix vs R2 strong Should-Fix（NLI ablation 反转证据降低严重性）→ Director 判定 Must-Fix
2. **Novelty claim 严重性**: R2 Must-Fix vs R1 Should-Fix（LLM judge 特殊性使 domain transfer 非 trivial）→ Director 判定 Should-Fix
3. **Abstract 密度**: R2 Should-Fix vs R1 Minor → 记录分歧
4. **Excitement**: R1 3.5/5 vs R2 3/5 → R2 认为核心洞见是 domain transfer，novelty ceiling 更低

### 评分

| 维度 | R1 | R2 | 合成 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.5 | 3 | **3** |
| Reproducibility | 4 | 4 | **4** |
| Overall | 3.5 | 3.5 | **3.5 (Borderline Conference)** |
| Confidence | 4 | 4 | **4** |

**EMNLP 2026 ARR 评分**: **3.5 = Borderline Conference**

### 判断依据

论文发现有价值（Likert Blindspot 对 evaluation community 有直接实践影响），统计密度高于同领域平均水平，实验设计周全（6 个独立控制）。但存在三个阻碍 confident accept 的问题：(1) 页数超限（hard constraint）；(2) NLI gate 作为框架基石缺人工验证；(3) evaluator-producer bias 处理乐观。Novelty 主要来自 domain transfer（Thurstone 1927 已知），但 CSD 的方法组合和 per-axis GEE decomposition 提供增量贡献。

**修复路径**: MF1（页数）可在提交前快速修复。MF2（人工验证 50 对样本）和 MF3（producer-corrected 估计 + register caveat）需要额外实验和写作工作。如果三个 Must-Fix 全部解决 + SF1-SF3 的 framing 调整完成，论文可达到 **4.0 (Conference)** 水平。当前状态适合 **Findings 接收**；是否 Main Conference 取决于 novelty 阈值判断。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高：8 句话塞入 framework 名称、4 judges、3 benchmarks、3 axes、BT 百分比、OR 值、两种解释。建议将 GEE OR 值移至 Introduction。[分歧：R2 Should-Fix, R1 Minor]
- "first framework combining..." claim 需限定。

### §1 Introduction
- Contributions 列表每条 3–5 行，可精简为 1–2 行核心论点。
- "black-box interventional framework" 措辞与 §3.5 disclaimer 不一致。

### §2 Related Work
- 覆盖全面，Comparative Trap、RATE 差异化、测量理论基础均已讨论。
- "Our contribution is the first systematic quantification of this gap" 需限定。

### §3 Method
- §3.2 NLI gate 设计合理，direction-aware gating 的 axis-dependent 策略有充分 justification。
- §3.5 Design Rationale 的因果声明 disclaimer 诚实。但 Figure 2 DAG 视觉修辞偏强，caption 可标注 "design rationale, not a formal causal model"（实际已有类似标注）。

### §5 Experiments / Analysis
- Table 1 Main Results 信息丰富但脚注区域过密。
- Table 2 Sensitivity Hierarchy 是亮点——七种方法交叉验证。
- §5.2 Measurement attenuation vs construct divergence 两种解释的呈现已有改善。
- §5.4 Verbosity 的 "style-dominated" 描述基于 GEE，措辞比 "confound-free" 更审慎。

### §6 Conclusion
- **溢出 page 8**——必须压缩。
- "should adopt content-controlled pairwise comparison" 需加 Comparative Trap caveat。

### Limitations
- 三段式覆盖 quality-style confounding、evaluator-producer bias、validation methodology。结构合理。
- 未包含新实验/图表/分析，符合 EMNLP 2026 规定。

### Appendix
- 15 个 appendix sections 提供充分技术细节。
- Table 5 GEE CI 部分缺失需补全。
- Verbosity sensitivity hierarchy (Appendix P) 已补充。