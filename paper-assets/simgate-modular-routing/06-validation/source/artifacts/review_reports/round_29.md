---
round: 29
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T23:10:04.426134+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 29 审稿报告 — simgate-modular-routing

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (ARR May cycle), Long Paper (8 pages)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: R1 (方法严谨性+实验设计+统计分析), R2 (新颖性+完整性+写作质量+Related Work)

---

## Summary

本文提出 episode-level counterfactual diagnostic framework，将 LLM agent routing signal 分解为 death avoidance 和 non-death 组成部分。在 ScienceWorld（11/30 task types, N=245 episodes）上发现 78.9% 的 non-tie routing labels 源自 death asymmetry（penalty-independent），DAF=90.4%（penalty-dependent, P=100）。跨模型验证（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）显示 death dominance 在三个 7-9B 模型家族中一致复现（DAF 88-90%, spread 2.2 pp）。跨环境 probes（MATH, ALFWorld）诊断出定性不同的 routing mechanism。Router training（Qwen3 LoRA, 0.6B-4B）产生 negative result（episode-level 47.1±2.2%, below chance）。

---

## Strengths

**S1. 新颖且有价值的诊断视角 [AGREE x2]。** "先诊断再构建 router" 的理念填补了方法论空白。现有 routing 工作（Toolformer, ART, Chameleon, CogRouter, ARES, MTRouter）直接训练 router 而不先理解 signal 构成。本文首次系统分解 routing signal。

**S2. 极其详尽的统计分析 [AGREE x2]。** 20 个 appendices（A-T）提供罕见深度：bootstrap CI、cluster-robust t-test、wild cluster bootstrap、LOO robustness、penalty sensitivity。论文自觉标注 K=11 cluster bootstrap 局限并推荐 non-clustered CI 为主推断——这种统计自省极少见。

**S3. 诚实的负面结果报告 [AGREE x2]。** Router failure（47.1±2.2%）被详细呈现，step-level vs episode-level gap 分析、text augmentation ablation、capacity scaling 系统排除了 data scarcity 和 model capacity 作为唯一解释。

**S4. Anti-cherry-picking 分析有效 [AGREE x2]。** 19 个排除 task types 的 mean ΔDR=+38.2 pp 高于 included +28.7 pp（Table 4），Appendix S extended validation（n=20）确认 excluded DAF (0.991) > included (0.904)。选择偏差的质疑被有效排除。

**S5. 跨模型复现可信 [AGREE x2]。** 三个 7-9B 模型家族 directional consistency 100%（10/10 death-prone tasks），internal vulnerability ~36-42%，Table 17 consolidation table 是有效 robustness evidence。

**S6. Algorithm 1 设计合理 [R1]。** Death-priority rule 假设明确，Labeling Quality Audit（Appendix B）验证 zero tie-breaking labels。

**S7. Hedging 语言诚实 [R2]。** Cross-environment probes 标注为 "preliminary evidence"，区分 methodological vs empirical generality。

---

## Weaknesses

### Must-Fix (影响接收决定)

**W1. [Critical, AGREE x2] 正文超出 8 页限制（R20-N1/R27-N1 复发）。** Sections 1-6 约 8.2-8.5 页，Conclusion 起始于 page 9。EMNLP 2026 限正文 8 页，有 desk reject 风险。视觉审查独立确认此问题。
- 可操作方案：(1) 压缩 Conclusion 为 2-3 句（删除与 Introduction 重复的 contributions 列表），(2) 缩小 Figure 2 或移至 appendix，(3) 合并 §4/§5 中重叠内容。

**W2. [Critical, AGREE x2] DAF=90.4% 作为 headline metric 对 penalty 有数学依赖。** DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数——P=0 时 7.4%, P=10 时 50.4%, P=100 时 90.4%（Table 12）。Abstract/Introduction 仍以 DAF=90.4% 为主导叙事，penalty-independent label fraction（78.9%）被置于次要位置。§2.4 已讨论 P-sensitivity 但叙事优先级未调整。
- 可操作方案：Abstract/Introduction 将 78.9% 作为 primary headline metric，DAF=90.4% 降为 "at ScienceWorld's default P=100" 的补充。

### Should-Fix (提升论文质量)

**W3. [Major, AGREE x2] 63% task exclusion rate 虽有 anti-cherry-picking 证据但限制 coverage。** 19/30 task types 被排除（dev 5, redundancy 7, agent floor 7），分析仅基于 37% task coverage。Taxonomic redundancy 的操作定义不透明，agent-floor tasks 与 30-step budget 限制的关系未探索。
- 可操作方案：§3 明确 taxonomic redundancy 判断标准；讨论更长 step budget 下 agent-floor tasks 是否出现 non-death signal。

**W4. [Major, AGREE x2] 跨环境 "deterministic" mode 语义不一致限制 cross-environment comparison。** ScienceWorld = oracle simulator, MATH = code interpreter, ALFWorld = admissible-action enumeration——信息特权程度完全不同。Conclusion 已修正为 "the diagnostic procedure—though not the specific operationalization—transfers"，但 §3.4 缺 explicit caveat。
- 可操作方案：§3.4 开头增加 caveat，区分 procedure transferability 和 finding transferability。

**W5. [Major, DIVERGENCE → consensus on scope] Router negative result 的解释。** R1 认为 class imbalance（9/245=3.7%）是 confound，failure 可能是 data-limited artifact。R2 REBUT：imbalance 是 death dominance 的直接表现非 collection bias，text augmentation/capacity scaling 已部分排除。共识：结论应限定为 "under current data regime (N=245, 3.7% minority)"。
- 可操作方案：§3.6 结论限定 scope；讨论 selective collection strategy（只收集 death-free episodes）是否能提高 minority rate。

**W6. [Major, AGREE x2] Non-death component (21.1%) 的 routing signal 来源未分析。** 20 个 score-comparison labels 全部来自 both-survived episodes，find-non-living-thing 是唯一 zero-death task（n=40, Δ_full=+9.58），但未 deep-dive 分析 trajectory differences。
- 可操作方案：Appendix 增加 2-3 个 non-death episode 的 case study。

### Nice-to-Fix (锦上添花)

**W7. [Minor, AGREE x2] 72B scaling probe scope 过窄。** 仅一个 72B 模型，无 at-scale cross-model replication。应标注为 "preliminary probe"。

**W8. [Minor, AGREE x2] 单一 death mechanism（focus on [object]）限制 failure mode 外部效度。** 100% internal deaths 由同一 action pattern 触发，是 ScienceWorld API 特异性。

**W9. [Minor, DIVERGENCE] Figure 2 近似恒等关系。** R2 认为 Major（应移至 appendix 释放空间），R1 REBUT（有 pedagogical 价值，建议缩小而非移除）。如需解决 W1 页数问题，可作为释放空间的选项。

**W10. [Minor, partial DIVERGENCE] 数字密度。** R2 认为过高，R1 部分辩护（分析论文需要 precise quantification），但同意 secondary stats 可精简。

**W11. [Minor, AGREE x2] Related Work 缺 non-agent adaptive computation。** 未覆盖 Mixture-of-Depths、speculative decoding 等。一句 positioning 即可。

**W12. [Minor, AGREE x2] Introduction/Conclusion contributions 列表重复。** 页数超限下应削减冗余。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致：

1. **[AGREE]** DAF penalty dependence 是核心 framing 问题，78.9% 应为 primary metric
2. **[AGREE]** 正文超页是 desk reject 风险
3. **[AGREE]** 跨环境 deterministic mode 不可比
4. **[AGREE]** Non-death 21.1% 分析缺失是 substantive gap
5. **[AGREE]** Anti-cherry-picking analysis 有效排除了选择偏差
6. **[AGREE]** 跨模型复现（3 families）可信
7. **[AGREE]** 统计分析深度罕见且值得肯定
8. **[AGREE]** Router failure 结论需限定 scope

## Reviewer Divergence

1. **[Figure 2 处理]** R2 建议移至 appendix (Major); R1 建议缩小保留 (Minor) — 取决于页数修复策略
2. **[Router failure 本质]** R1 认为 class imbalance confound 更严重; R2 认为 imbalance 是 finding 的表现 — 共识：限定 scope
3. **[Excitement]** R1: 3.5/5 (framework novelty 有持久价值); R2: 2.5/5 (triviality risk 显著) — reasonable disagreement
4. **[数字密度]** R1 认为是分析论文必要特征; R2 认为过高影响可读性 — 共识：secondary stats 可精简

---

## Questions (需作者澄清)

1. Algorithm 1 的 death-priority rule 在 both-dead 情况下不区分死亡时间。是否丢失了有用的 routing signal？
2. Δ_nd = 2.84 的 bootstrap CI 是多少？如果 uncertainty 较大，DAF 的 interpretability 是否受影响？
3. Decision framework（Appendix R）的 thresholds（15 pp, 75%, 50%）仅有 4 个 retrospective data points。选择依据和 sensitivity analysis？
4. "No prior work has decomposed routing decisions in interactive environments" 是否过强？建议修改为 "no prior work has systematically decomposed what drives routing preferences"。
5. 19 个 excluded task types 中的 agent-floor tasks：在更长 step budget（50, 100 steps）下是否出现 non-death routing signal？

---

## Missing References

**R1 建议**:
- FrugalGPT (Chen et al., 2023) — LLM routing/cascading
- AutoMix (Madaan et al., 2023) — LLM routing/cascading
- Options framework (Sutton et al., 1999) — temporal abstraction

**R2 建议**:
- Mixture-of-Depths (Raposo et al., 2024) — non-agent adaptive computation
- Speculative decoding (Leviathan et al., 2023; Chen et al., 2023) — adaptive computation

**共识**: 至少加一句 positioning 区分 token-level adaptive computation 和 episode-level diagnostic framework。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成

| Severity | 发现 |
|----------|------|
| **Critical** | 主文超 8 页限制——Conclusion 从 page 9 开始，需压缩约 15-20 行 |
| **Warning** | Pages 7-8 连续两页纯文本无 display item，审稿人视觉疲劳风险 |
| **Warning** | 主文 display items 偏少（3 figure + 2 table = 5 个），大量结果推到 appendix |
| **Info** | Figure 1 pipeline 图出现在 page 2 顶部，时机合理，颜色区分度好 |
| **Info** | Figure 2 散点图尺寸偏小但文字仍可读 |
| **Info** | 所有表格使用 booktabs 风格，排版专业整洁 |
| **Info** | 全文无公式渲染错误、未解析引用或 margin 溢出 |

---

## Overall Assessment

**Overall: 3.0 — Findings**

**Soundness**: 3.5/5 (R1: 3.5, R2: 3.5)
**Excitement**: 3.0/5 (R1: 3.5, R2: 2.5)
**Reproducibility**: 4.0/5 (R1: 4, R2: 4)
**Confidence**: 4/5

### 综合判断依据

**接收方向的论据**:
1. "先诊断再构建 router" 的方法论框架新颖，填补了 agent routing 领域的诊断性空白
2. 统计分析的深度和透明度在该领域罕见（20 appendices, 多种 bootstrap 方法, LOO sensitivity）
3. 跨模型复现（3 families, 7-9B tier）增强了 ScienceWorld 内发现的可信度
4. 负面结果（router failure）的诚实报告对社区有警示价值
5. Penalty-independent label fraction (78.9%) 是 robust 的核心发现

**拒绝方向的论据**:
1. **正文超页** [Critical]——desk reject 风险，优先修复
2. **Triviality concern**——"death avoidance dominates in death-penalized environment" 具有可预测性（R2 Excitement 2.5/5），DAF 值对 P 的数学依赖加剧此印象
3. **Cross-environment evidence 薄弱**——三环境的 "deterministic" mode 语义不同，仅 ScienceWorld 有完整验证
4. **Non-death signal 分析缺失**——21.1% 的 routing signal 来源未解释
5. **Router failure 解释 underdetermined**——signal-limited vs data-limited 在 3.7% minority rate 下无法区分

### 定位建议

论文的方法论贡献（counterfactual decomposition framework, DAF/SCI 指标）具有独立于具体发现的可复用价值，适合 **Findings** 接收。若能修复 W1（页数）、W2（DAF framing）、W6（non-death analysis），可升至 **3.5 Borderline Conference**。核心 Excitement 限制（triviality risk, 单一环境深度分析）是结构性的，难以通过 writing fix 解决。

---

## Detailed Comments

### Abstract
- 当前以 DAF=90.4% 为主导，应将 78.9% label fraction 提升为 headline
- "spread 2.2 pp" 等 secondary stats 可移至正文

### §1 Introduction
- Contributions 列表与 Conclusion 近乎逐字重复，保留一处
- "no prior work has decomposed" → "no prior work has systematically decomposed what drives routing preferences"

### §2 Method
- §2.4 DAF 定义后已包含 P-sensitivity 讨论，叙事层面到位
- Algorithm 1 both-dead 情况的处理可在 footnote 中 justify

### §3 Experiments
- §3 开头明确 taxonomic redundancy 操作定义
- §3.1 correlation/sensitivity 段中 Cohen's d=3.02 加一句 context（reflects near-binary consistency）
- §3.4 开头加 caveat：三环境 deterministic mode 信息特权程度不同
- §3.6 router failure 结论限定为 "under current data regime"

### §4 Related Work
- 加一句 non-agent adaptive computation positioning
- 可考虑引用 FrugalGPT、AutoMix

### §5 Discussion
- 与 §4 有内容交集，合并/压缩可释放空间

### §6 Conclusion
- 压缩为 2-3 句 forward-looking summary，删除重复 contributions

### Limitations
- 内容充分（5 个方面），质量良好

### Appendix
- 增加 non-death episode case study（W6）
- 考虑接收 Figure 2（如 R2 建议）以释放正文空间