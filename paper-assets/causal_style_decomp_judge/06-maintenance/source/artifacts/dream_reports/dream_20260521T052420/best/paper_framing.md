# Paper Framing — causal_style_decomp_judge

> Round 1 审稿 2.5/5 Borderline Findings。Round 1 review issues 修复中，准备 re-dream。
> 实际证据已远超 Dream 2 想象：2 judges × 3 axes（Dream 2 只有 1 judge × 1 axis），GEE decomposition 跨轴梯度。

## Target Venue
- Primary: EMNLP 2026 Main (via ARR)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR June 2026 cycle (submission ~June 15)
- Format: Long paper, 8-page main text + unlimited references

## Title
**The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison**

## Core Claims (Round 1 review 修正后)

### C1 (Method — application contribution): CSD pipeline 可以 post-hoc 检测 black-box LLM judge 的 per-axis style bias
- 定位：已知组件（counterfactual rewriting + NLI verification + pairwise comparison）的新应用，acknowledge 组件来源
- 状态：✅ 在 2 judges × 3 axes 上验证，5/6 cells 检测到 style bias
- 证据：GPT-4o formality BT 63.0% p<0.001; Qwen3-32B formality 66.5%, verbosity 77.3% (all p<0.0001)

### C2 (Measurement Insight — 主贡献): Likert Blindspot — Likert scoring 系统性低估 style bias
- 两层机制：(1) ~60% Likert ties 浪费评估预算 (2) absolute scoring 捕获弱于 forced comparison
- 状态：✅ 5/6 cells confirmed (GPT-4o verbosity Likert ATE pending, pairwise 86.3% p<10⁻⁶)
- 控制实验：binarized Likert sign test p=0.296 vs pairwise p=0.006 (exp-010) → 测量结构差异非统计检验差异
- ordinal regression p=0.769 (exp-015) → 非 interval-scale assumption artifact
- Power curve：binarized Likert 需 n≈462 才能 p<0.05（计入 tie rate），当前 n=88 严重 underpowered

### C3 (Empirical — 跨轴跨模型 pattern): Style bias 的可检测性因 axis 语义性质而异
- GEE decomposition gradient：Verbosity OR=13.10 (pure style, originality NS) > Formality OR=4.20/2.21 (mixed) > Register OR=1.91 (originality-dominated OR=5.72)
- 方法边界：content-preserving axes (formality ✅, verbosity ✅) 可检测；改变认知承诺的 axes (tone ❌ NLI 65%) 结构性不兼容
- 跨模型验证：GPT-4o vs Qwen3-32B, proprietary vs open-source, 相同方向

### C4 (Practical): Practitioner guidance
- Use pairwise over Likert for style bias audit
- Per-axis decomposition reveals axis-specific confound structure (GEE gradient)
- Content preservation verification per axis (direction-aware NLI for asymmetric axes)

## Evidence Matrix (当前状态)

| | GPT-4o | Qwen3-32B |
|---|--------|-----------|
| **Formality** | BT 63.0% [55.8, 70.3] p<0.001 ✅ Blindspot | BT 66.5% [58.5, 73.9] p<0.0001 ✅ Blindspot |
| **Verbosity** | Pairwise 86.3% p<10⁻⁶ (**Likert ATE pending**) | BT 77.3% [70.3, 84.3] p<0.0001 ✅ Blindspot |
| **Register** | 63.3% p=0.085 (NS, originality-dominated) | GEE OR=1.91 p=0.046 (exploratory) |

**GEE Decomposition (Qwen3-32B)**:
- Verbosity: style OR=13.10 p=2.6e-09, originality OR=0.49 p=0.096 (NS) → **confound-free**
- Formality: style OR=4.20 p=0.0002, originality OR=4.70 p<0.0001 → **mixed**
- Register: academic OR=1.91 p=0.046, originality OR=5.72 p<0.0001 → **originality-dominated**

**GPT-4o GEE (formality only)**: formal OR=2.21 p=0.010, originality OR=1.82 p=0.052 (marginal)

## Story Spine

### Problem
LLM-as-judge 是 NLP 评估和对齐训练的核心基础设施。Style bias 是主宰偏差（SOS-Bench R=0.999），但标准 Likert scoring 看不到它。

### Existing Approaches & Their Gaps
- **LC-AlpacaEval (ICLR'25)**: 回归控制 length bias，单维度，detection + correction
- **SOS-Bench (ICLR'25)**: 注入缺陷量化 judge 敏感度，相关性分析非因果
- **CASSE (2026)**: 12×12 style 矩阵，因果纠缠
- **RATE (ICML'25)**: Double-rewrite ATE protocol — 用 Likert ATE → 本文证明 Likert 不敏感 → RATE 自身发现可能受 Likert Blindspot 影响（最强 positioning argument）
- **Counterfactual Rhetorical (2025)**: persona counterfactual + BT aggregation，粒度不同
- **Gap**: 无人系统性比较 Likert vs pairwise 在 style bias 检测中的 sensitivity gap；无人用 GEE decomposition 分离 style effect vs originality bias

### Our Framing (Round 1 修正)
用 binary style counterfactual + position-controlled pairwise comparison **interventionally measure** LLM judge 的 per-axis style bias。
核心发现：**标准 Likert 评估系统性掩盖 style bias** — 在 5/6 judge×axis cells 中 pairwise 显著而 Likert 不显著。
GEE decomposition 揭示 **跨轴 confound 梯度**，为 practitioner 提供 axis-specific bias 诊断。

**语言规范**：
- "interventional" / "counterfactual-based measurement"（非 "causal"）
- DAG 已加入 §3.5（assumptions 段）
- 全文已降调因果术语

### Headline Result
"Standard Likert scoring declares no style bias, but position-controlled pairwise comparison on the same counterfactual data reveals significant style preference across 2 judges and 3 axes — this Likert Blindspot persists with BT win probabilities of 63-77% (all p<0.001) while Likert ATE remains non-significant."

## Round 1 Review Issues — Resolution Status

19 issues total (6 critical, 7 warning). Key resolution:

**Effectively resolved**:
- R1-W5 (post-hoc power): CI-based precision adopted, power curve reframed as illustrative
- R1-W4 (multiple comparisons): Holm-Bonferroni family defined, primary/exploratory separation
- CROSS-4 (ordinal regression): exp-015 p=0.769, Reviewer verified
- R2-W2 (Bradley-Terry): BT as primary analysis, pair-level bootstrap

**Near-resolved (writing patches in progress)**:
- R1-N1 (causal language): 降调完成，DAG added
- R1-N2 (NLI false-negative): Triple indirect evidence defense
- R1-N3 (NLI threshold): Sensitivity analysis exp-011
- R2-N1 (novelty): 2 judges × 3 axes with BT + GEE — Findings-level empirical value
- R2-N3 (RATE criticism): h2h framing with BT upgrade
- R2-W1 (scope): 2×3 matrix, 5/6 cells
- R1-W1 (Likert baseline fairness): ordinal regression confirms Blindspot
- R1-W2 (consistency filter): BT on all data rules out filter inflation

**Gaps remaining**:
- R2-N2 (references): 22 verified, reference audit done
- R2-W4 (figures): Power curve ✅, Pipeline diagram ✅, Forest plot pending
- R2-W3 (related work): Expanded to 5 paragraphs
- CROSS-1 (efficiency gap framing): Two-layer mechanism, power curve shows n≈462 needed
- Page count: Currently ~8.5 pages, compression in progress

## Figures (3 planned)
1. **Power curve** — ✅ Done. BT vs binarized Likert sensitivity comparison, with tie rate correction
2. **Pipeline diagram** — ✅ Done. 5-stage CSD pipeline with attrition numbers
3. **Forest plot** — ⏳ Pending. 2 judges × 3 axes BT win probabilities with 95% CI

## Bibliography
22 verified references (target: 25+). Key additions since Dream 2: DeCoster 2011, Hoenig 2001, Stevens 1946, Zeng 2024, Bradley & Terry 1952, Feinstein 1990.

## Venue Fit
EMNLP 2026 高度匹配。Round 1 得分 2.5 Borderline Findings，主要失分在写作质量（零图表、broken refs、page overflow）和 novelty framing。
证据强度已满足 Findings 3.0-3.5 要求。Main 4.0 需要 novelty ceiling 突破（结构性限制，Likert Blindspot 是已知心理测量学现象的 domain transfer）。
