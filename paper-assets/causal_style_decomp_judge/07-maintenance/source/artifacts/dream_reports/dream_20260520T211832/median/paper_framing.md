# Paper Framing — causal_style_decomp_judge

## Target Venue
- Primary: EMNLP 2026 Main (via ARR)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR June 2026 cycle (submission ~June 15)
- Format: Long paper, 8-page main text + unlimited references

## Core Claims (3 条，可证伪)

### C1 (Method): Binary style counterfactual + pairwise comparison 可以 post-hoc 检测 black-box LLM judge 的 causal style bias
- 证伪条件：pairwise win rate 在 45-55% 且 p>0.10（所有 judge × benchmark 组合）
- MVP 状态：formality 69.1% (p=0.006) on GPT-4o × LLMBar ✅
- Research 需要：3+ judges × 2+ benchmarks 复现

### C2 (Measurement Insight): 标准 Likert pointwise scoring 系统性低估 style bias — pairwise comparison 是更敏感的检测方法
- 证伪条件：Likert 和 pairwise 在所有 setting 上一致（要么都显著，要么都不显著）
- MVP 状态：formality Likert p=0.332 vs Pairwise p=0.006，同一数据 ✅
- Research 需要：verbosity/tone 等其他 axis 上也出现 Likert-pairwise gap（或 Likert 对强信号够用 → 说明 gap 与信号强度有关）

### C3 (Empirical): Style bias 具有 axis 依赖性 — 不同 style 维度在不同 judge 上表现不同，需要 per-axis 分析
- 证伪条件：所有 axis 在所有 judge 上效应一致
- MVP 状态：formality 有 causal premium，verbosity 与 RATE 方法不兼容（信息量改变） ✅（partial）
- Research 需要：tone/register axis + multi-judge 差异化数据

## Story Spine

### Problem
LLM-as-judge 已成为 NLP 评估和对齐训练的核心基础设施（preference learning, RLHF reward signal, benchmark ranking）。近期研究（SOS-Bench ICLR'25, Preference Leakage ICLR'26, Soumik 2026）一致表明 style bias 是 LLM judge 的主宰偏差（R=0.999, bias score 0.76-0.92），远超 position bias。但现有工作要么把 style 当单一维度（length），要么只做相关性分析而非因果推断。

### Existing Approaches & Their Gaps
- **LC-AlpacaEval (ICLR'25)**: 回归控制 length bias，简单有效但只处理一个维度，且是 population-level correction 不是 per-instance
- **SOS-Bench (ICLR'25)**: 通过注入缺陷量化 judge 对 style vs content 的相对敏感度，但不做 causal decomposition
- **CASSE (2026)**: 12×12 style 特征交互矩阵，但需要 prompt engineering 控制单个 feature（因果纠缠问题）
- **Gap**: 无人用 counterfactual intervention 做 multi-axis causal style bias detection + 不改变 judge 的 black-box post-hoc 方案

### Our Framing
我们提出 CSD (Causal Style Decomposition)：通过 binary style counterfactual 生成 + position-controlled pairwise comparison 检测 LLM judge 的 per-axis causal style bias。与回归方法不同，我们直接干预 style 维度并测量 judge 响应变化。关键发现：(1) 标准 Likert 评分严重低估 style bias（同一数据 Likert p=0.33 vs Pairwise p=0.006）；(2) Style bias 是 axis-dependent 的——formality 产生显著 premium，verbosity 因改变信息量而不兼容内容保持假设。

### Headline Result Template
"Using binary style counterfactuals with position-controlled pairwise comparison, we reveal that {judge} exhibits a significant {axis} premium ({win_rate}%, p<{p_value}) that is completely masked by standard Likert scoring (p>{likert_p}). This measurement gap persists across {N} judges and {M} benchmarks."

## Anticipated Reviewer Concerns & Mitigation

### RC1 (致命级): "只有一个 judge 和一个 benchmark"
- **缓解**: Research 阶段扩展到 GPT-4o + Claude-3.5/4 + Gemini-2.0 × LLMBar + AlpacaEval + MT-Bench
- **实验**: exp-001 (multi-judge), exp-002 (multi-benchmark)

### RC2 (重伤级): "RATE correction 不可靠"
- **缓解**: 诚实报告 RATE/Likert 局限性，将 pairwise 作为 primary evidence
- **论文叙事**: RATE 的失败本身支持 C2（measurement insight）— correction 量级 > raw signal = Likert 不可靠的另一个证据
- **实验**: exp-005 (pairwise RATE control)

### RC3 (中等级): "方向不对称 = original preference 而非 style"
- **缓解**: Pairwise RATE 控制实验（original vs double-rewrite pairwise）直接量化 original preference
- **实验**: exp-005

### RC4 (中等级): "vs LC-AlpacaEval 的优势？"
- **缓解**: (a) 多维度不只 length (b) per-instance 不只 population (c) 不需要大量评测数据拟合回归 (d) 适用于 pairwise judge 不只 pointwise

### RC5 (低级): "n=100 太小"
- **缓解**: Power analysis + Research 阶段扩大到 n=300-500
- **实验**: exp-006

## Venue Fit

EMNLP 2026 高度匹配：LLM evaluation 和 bias analysis 是 EMNLP 核心主题。Practical methodological insight（Likert vs Pairwise）对社区直接有用。Causal inference in NLP 是上升趋势。

风险：如果只有 formality 一个 axis 有效（无 tone/register 数据），论文 scope 偏窄 → Findings 而非 Main。需要至少 2 个 axis + 3 judges + 2 benchmarks 才有 Main 竞争力。
