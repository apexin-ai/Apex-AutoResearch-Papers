# Paper Framing — causal_style_decomp_judge

> Dream 2 (dream_20260520T233719): best 3.5 / median 3.0 / worst 3.0。以下为 D020 修正版。
> 实际实验数据比 dream median 想象更强（exp-014 p=0.010 vs dreamed p=0.11; register 95% NLI unknown to dream）。

## Target Venue
- Primary: EMNLP 2026 Main (via ARR)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR June 2026 cycle (submission ~June 15)
- Format: Long paper, 8-page main text + unlimited references

## Title (Dream 修正)
**旧**: "Causal Style Decomposition Reveals Systematic Style Bias in LLM-as-Judge That Likert Scoring Misses"
**新**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison"
- 理由：三档审稿人一致认为 "decomposition" 和 "framework" 过度承诺。新标题聚焦最强发现 (C2) 且更准确。

## Core Claims (3 条 + 1 practical，修正后)

### C1 (Method — 降级表述): Counterfactual pairwise comparison 可以 post-hoc 检测 black-box LLM judge 的 style bias
- ⚠️ Dream 反馈：不是新 "framework"，是已知组件（counterfactual rewriting + NLI verification + pairwise comparison）的新应用。论文中必须明确 acknowledge 组件来源（RATE, style transfer evaluation, MT-Bench pairwise）并定位为 application contribution。
- 证伪条件：pairwise win rate 在 45-55% 且 p>0.10（所有 judge × benchmark 组合）
- 状态：formality 69.1% (p=0.006) on GPT-4o × LLMBar ✅

### C2 (Measurement Insight — 主贡献，强化): Likert pointwise scoring 系统性低估 style bias — "Likert Blindspot"
- ⚠️ Dream 反馈：需要 sign-test on binarized Likert 控制实验来隔离 pairwise 的结构性优势 vs 统计检验选择差异。这是 C2 的命门。
- 证伪条件：binarized Likert sign test 也显著 → gap 不在测量方法而在统计检验
- 状态：Likert p=0.332 vs Pairwise p=0.006，同一数据 ✅；binarized Likert control 待做

### C3 (Empirical — 降级为 preliminary): Style bias 检测的可行性因 axis 语义性质而异
- ⚠️ Dream 反馈：只有 formality robust，"multi-axis decomposition" 和 "prestige dimension" 过度承诺。改为 "preliminary evidence" + "method boundary"。
- 新表述："content-preserving counterfactual intervention 适用于不改变信息量或认知承诺的 style axes（formality ✅, verbosity 需适配 ✅）；改变认知承诺的 axes（tone ❌）结构性不兼容"
- 证伪条件：所有 surface-level axes 都一样 → 无 axis 依赖性

### C4 (Practical — 新增): CSD-based 实用建议 / 轻量 correction
- ⚠️ Dream 反馈："detection-only, no correction" 是三档一致的弱点。需要至少提供 practitioner guidance 或 lightweight correction component。
- 方案：(a) CSD-adjusted win rate = raw_win_rate - original_preference_estimate + 50%（需正式统计模型支撑）；(b) 实用建议清单："use pairwise over Likert for style bias audit; verify content preservation per axis; control for original preference"
- 这不需要是完整的 debiasing 系统，但需要比纯 detection 多一步

## Story Spine

### Problem
LLM-as-judge 已成为 NLP 评估和对齐训练的核心基础设施。Style bias 是主宰偏差（SOS-Bench R=0.999, Soumik bias 0.76-0.92），但标准 Likert scoring 看不到它。

### Existing Approaches & Their Gaps
- **LC-AlpacaEval (ICLR'25)**: 回归控制 length bias，简单有效但只处理一个维度，且提供 detection + correction
- **SOS-Bench (ICLR'25)**: 注入缺陷量化 judge 敏感度，相关性分析非因果
- **CASSE (2026)**: 12×12 style 矩阵，但因果纠缠
- **RATE (ICML'25)**: Double-rewrite ATE protocol — CSD 的 Stage 4 直接采用此方法（必须引用）
- **Counterfactual Rhetorical (2025)**: 最近的方法论 predecessor — persona counterfactual + BT aggregation
- **Gap**: 无人系统性比较 Likert vs pairwise 在 style bias 检测中的 sensitivity gap

### Our Framing (D020 修正 — 软化 causal 用语)
我们用 binary style counterfactual + position-controlled pairwise comparison **interventionally measure** LLM judge 的 per-axis style bias。核心发现不是"我们提出了一个新框架"，而是**标准 Likert 评估系统性掩盖了 style bias（p=0.33 vs p=0.006）**，这对依赖 Likert scoring 的整个 LLM 评估生态有直接影响。

**⚠️ D020 语言规范（Dream 2 三档一致）**：
- 全文用 "interventional" / "counterfactual-based measurement" 替代 "causal"
- 不用 "causal style bias"，用 "style preference detected via counterfactual intervention"
- 不用 "independent causal effect"，用 "independent contribution (logistic regression)"
- 如需正式化，加一段 "assumptions under which our approach approximates causal measurement"
- 理由：无 DAG、无 SUTVA 讨论、无 sensitivity analysis for unmeasured confounding

### Headline Result Template
"Standard Likert scoring declares no style bias (p={likert_p}), but position-controlled pairwise comparison on the same counterfactual data reveals significant {axis} preference ({win_rate}%, p<{p_value}) — this Likert Blindspot persists across {N} judges and {M} benchmarks."

## Anticipated Reviewer Concerns & Mitigation (Dream 更新)

### RC1 (致命级): "只有一个 judge 和一个 benchmark" → exp-001, exp-002
### RC2 (重伤级): "Likert-Pairwise gap 是统计检验选择差异不是测量方法差异" → **exp-010 (NEW): sign-test on binarized Likert**
### RC3 (重伤级): "方向不对称 = original preference" → exp-005 (扩展到所有 judge×benchmark)
### RC4 (中等级): "Novelty incremental, 组件都是已知的" → 重新定位为 application + empirical contribution，诚实 acknowledge 组件来源。**D020 补充**：pairwise > Likert sensitivity 已知于 psychometrics (Thurstone 1927, Kiritchenko & Mohammad 2017, Novikova et al. 2018)。论文贡献定位为 "first quantification of gap magnitude for LLM judge style bias + binarized Likert mechanism isolation design"，不是 "discovery"
### RC10 (D020 新增，重伤级): "RATE 区分不足" → 需要专段讨论 RATE vs CSD 差异。关键角度：RATE 用 Likert ATE → 本文证明 Likert 不敏感 → RATE 自身的 style-related 发现可能也受 Likert Blindspot 影响。这是最强 positioning argument
### RC11 (D020 新增，中等级): "Binarized Likert 只做了 1/9 cells" → 扩展到所有 judge×benchmark 的 binarized Likert（零成本，在 exp-001/002 Likert 数据可用时）
### RC5 (中等级): "Detection-only, no correction" → C4 (practical guidance + lightweight correction)
### RC6 (中等级): "C3 oversold" → 降级为 preliminary，reframe title
### RC7 (低级): "n=100 太小" → exp-006 (n=500) + power analysis
### RC8 (低级): "NLI threshold arbitrary" → exp-011 sensitivity analysis
### RC9 (低级): "No counterfactual examples" → 论文添加 2-3 annotated examples

## Narrative Strategy (保持，但标题修正)

### Type: 突破局限型 + "普遍实践+隐藏风险" hook
### Title: "The Likert Blindspot" (命名最强发现)
### Intro P2 修正: "但我们发现标准 Likert scoring 系统性掩盖 style bias — 同一数据上 Likert 报告无偏差（p=0.33），pairwise comparison 却检测到显著偏好（p<0.01）"

### Figure 1: Problem illustration (Likert vs Pairwise gap) — 保持
### Figure 2: Method overview — 保持
### Main Result Table: axes (rows) × judges (cols) × {Pairwise, Likert, Binarized-Likert} — 新增 binarized Likert 列

## Bibliography 目标 (D020 扩充)
从 10 refs → 25+ refs。必须引用：
- **Psychometric lineage（D020 三档一致）**: Thurstone 1927, Kiritchenko & Mohammad 2017 (BWS vs Likert for NLG), Novikova et al. 2018 (ranking vs rating for NLG), Karpinska et al. 2021 (Likert reliability for text quality)
- **Closest competitors**: RATE (ICML'25, double-rewrite ATE — needs differentiation paragraph), Zhou et al. 2025 (Counterfactual Rhetorical — persona vs axis granularity)
- **Style bias ecosystem**: SOS-Bench, CASSE, FairJudge, Soumik 2026 (Judging the Judges), Preference Leakage (Li et al. ICLR 2026)
- **Foundations**: Veitch et al. 2020 (causal text), Mir et al. / Krishna et al. (style transfer eval)
- **LLM judge**: Chatbot Arena, FairEval, Stureborg et al. 2024 (inconsistent biased evaluators), FLASK (Ye et al. 2024), Split and Merge (Li et al. 2024)

## Venue Fit (D020 更新)
EMNLP 2026 高度匹配。Dream 2 best=3.5（接近 4.0 Conference），实际数据比 dream median 更强。

**Findings 确定可达** — 需要：framing 修正（已做 D020）+ 基本实验完成
**Main 需要** — 在 Findings 基础上额外：
1. Multi-judge pairwise significant (exp-001，API 恢复后) 
2. Binarized Likert 扩展到 all 9 cells (零成本，exp-001/002 数据后)
3. RATE 专段区分 + psychometric lineage (writing task)
4. 软化 "causal" → "interventional" (writing task, D020 已规范)
5. Multiple comparisons correction (Holm-Bonferroni)
6. 25+ references
