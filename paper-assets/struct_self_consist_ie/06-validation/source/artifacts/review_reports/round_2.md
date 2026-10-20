---
round: 2
overall_score: borderline
timestamp: 2026-05-15T02:56:52.665681+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 2 审稿报告 — struct_self_consist_ie

**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性 + 格式）
**交叉分享**: 已完成，两位 Reviewer 均提交逐条 [AGREE]/[REBUT] 回应

---

## Summary

本文系统比较了三个族群（structural/surface/model-internal）的五种 confidence signal 在 generative IE（NER + RE）中的 quality estimation 与 sample selection 表现。核心发现是 "correlation-selection gap"：instance-level consistency signals 是有效的 quality estimators（entity voting ρ=0.38, exact match AUROC=0.75），但无法可靠超越 greedy decoding 进行 best-of-N selection（p>0.39, bootstrap），尽管存在 13-18pp 的 oracle headroom。附带发现 signal ranking 随 task difficulty 变化（EM 领先 easy tasks，SJ/Voting 领先 hard tasks，WNUT-17 全部 collapse）。

---

## Strengths

1. **概念贡献清晰且有框架性价值**：quality estimation（ranking instances by expected performance）vs sample selection（choosing best output among N candidates）的解耦（§3.1 per-sample vs instance-level signal formulation）对 generative IE 社区有指导意义，是与 Nédellec et al. (2026) 的关键差异化。

2. **Quality estimation 分析深度突出**：5 signals × 4 configurations (Table 1) + conditional filtering + capability stratification + per-relation diagnostic + ρ-AUROC dissociation 分析，超过多数同类 empirical study。

3. **统计规范（selection）达到高标准**：Bootstrap resampling (B=10,000, n=529, instance-level paired), percentile 95% CIs, Cohen's d=0.038, sign test 61W/70L, 3-seed 含义明确——远超多数 NLP empirical papers。

4. **诚实的 hedging**：RE single-dataset 限制在 Introduction/Discussion/Conclusion/Appendix 四处 acknowledge；logprob temperature gap 在正文 + Limitations 双重标注；claim 用 "consistent across tested model families" 而非 "model-agnostic"——Round 0-1 的 self-awareness 问题已有实质改善。

5. **Related Work 覆盖全面**：§2 涵盖 self-consistency 变体（USC, CISC, ReASC, ranked voting, latent SC）、difficulty-adaptive 方法（Optimal SC, Difficulty-Adaptive SC）、generative self-aggregation、conformal prediction、semantic uncertainty 等。49 条 bib 全部 cited，0 orphan。

6. **ρ-AUROC dissociation 是 actionable finding**：EM 在 ρ 排名低但 AUROC 领先（SciERC NER: ρ=0.295 rank #3, AUROC=0.749 rank #1），揭示 binary vs continuous signal properties 的 metric-dependent 行为，对 practitioners 在 quality-aware routing 中有直接实用价值。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. Selection 证据面过窄——核心贡献仅 1 dataset × 1 model 验证** [Reviewer 共识: unanimously critical]

- **位置**: Table 3 (§5.3)；Abstract; Introduction Contribution #2; Conclusion
- **问题**: Correlation-selection gap 是论文的 differentiator（与 Nédellec et al. 的关键区别），但 Table 3 的 selection 分析仅覆盖 SciERC/Qwen。Quality estimation 有 3 datasets × 2 models 的覆盖，selection 仅 1×1，逻辑链断裂。Abstract "no signal reliably surpasses greedy decoding on either task" 的 evidence base 实际是 1 dataset × 1 model × 2 tasks。CoNLL selection 未报告（即使 headroom 极小，negative result 本身有价值——说明 gap 可能是 hard-task specific）；LLaMA SciERC selection 未报告（cross-model 验证缺失）。
- **Action**: (1) 补 LLaMA SciERC selection 结果验证 cross-model generalization；(2) CoNLL selection 放 Appendix（即使结论是 ceiling effect）；(3) 如 WNUT-17 selection 不可行，明确说明 oracle-greedy gap。

**C2. WNUT-17 capability boundary claim 缺乏系统数据** [Reviewer 共识: unanimously critical]

- **位置**: §5.1; Introduction Contribution #3
- **问题**: Contribution #3 列出 "task-complexity boundary conditions"，WNUT-17 是关键证据。但全文仅报告 SJ 一个信号的 ρ=0.082 (p=0.106)——一个不显著的单信号结果。其他四个信号（Voting, EM, FK, Logprob）在 WNUT-17 的结果完全缺失。用单个不显著数据点支撑 "all signals converge when model capability is insufficient" 逻辑上不成立。如果 5 个信号全部 collapse，这反而是更强的证据。
- **Action**: Appendix 增加 WNUT-17 完整 table（5 signals × ρ + AUROC）；补 conditional ρ（non-zero F1 subset）排除 floor effect。

---

### Should-Fix（影响评分但不一票否决）

**W1. ρ=0.38 缺乏 cross-method 数值对比** [R2 列为 critical, R1 同意但建议降为 should-fix]

- **位置**: §5.1, §6 Discussion
- **问题**: 论文以 ρ=0.38 为核心正面结论（"effective quality estimators"），intra-study context 已有（14% variance explained + AUROC=0.749），但 cross-method numerical context 完全缺失。§2 引用 semantic entropy (Kuhn 2023)、P(True) (Kadavath 2022)、CoCoA (Vashurin 2025) 但未给出任何数值对比。R1 指出 structured IE 与 discrete-answer QA 的 output space 根本不同，direct comparison 有误导风险，因此降为 should-fix。
- **Action**: §5 或 §4.2 加 footnote，引用可比方法的典型 AUROC 值，并明确 cross-task comparison 的困难性。

**W2. N=8 QE ρ 缺乏 uncertainty quantification** [Reviewer 共识]

- **位置**: Table 1 (§5.1)
- **问题**: Table 1 N=8 行为 point estimates without CIs/standard errors。多处 signal ordering Δ=0.003-0.01（如 CoNLL LLaMA SJ-FK Δ=0.003），参照 N=16 σ≈0.006-0.008，可能 within noise。正面 QE 结论反而缺乏统计支撑，与 selection 的 thorough bootstrap 标准不一致。
- **Action**: 对 N=8 主要 ρ 值报告 bootstrap CIs，或 Appendix 补 3-seed runs。

**W3. SJ Hungarian matching 无 threshold + Eq.(4) 非标准分母** [Reviewer 共识, R2 交叉回应提升严重性]

- **位置**: Eq.(4), §3.2
- **问题**: sim = token-level IoU ✓, g_i/g_j 定义 ✓。但：(1) Hungarian 是否有 minimum similarity threshold？无 threshold 则完全不相关 span 也会 match，SJ numerator 非零；(2) 分母 max(|g_i|,|g_j|) 是非标准 Jaccard variant（标准为 |A∪B|），未解释设计选择。
- **Action**: 明确 threshold 及 zero-overlap matched pairs 比例；一句话解释 max vs union 的设计理由。

**W4. RE selection 无统计检验** [Reviewer 共识]

- **位置**: Table 3, §5.3
- **问题**: NER selection 有完整 bootstrap（p, CI, Cohen's d, sign test），RE 仅叙述性 "no signal exceeds greedy" 无任何统计量。RE oracle headroom 18.1pp 更大，selection failure 更需 p-value 支撑。
- **Action**: 补 RE selection bootstrap p-value 和 CI。

**W5. Constrained decoding 作为全局 confound 讨论不足** [R2 提出, R1 交叉同意]

- **位置**: §6 Discussion; Limitations
- **问题**: Discussion "Why logprob fails" 段提到 constrained decoding 压缩 per-sample diversity，但仅在 logprob context 下讨论。如果 constrained decoding 压缩 diversity，影响的不仅是 logprob，还包括 consensus-proximity selection（SJ/Voting）——因为后者也依赖 per-sample 差异区分候选。Limitations 未列此 confound。
- **Action**: Limitations 增加 constrained decoding 条目；或补 per-sample F1 variance 数据证明 diversity 已足够。

**W6. Abstract "across NER and RE on three datasets" 措辞误导** [Reviewer 共识]

- **位置**: Abstract line 3
- **问题**: RE 仅在 SciERC 评估，但 Abstract 自然读法暗示 NER+RE 均在三数据集上进行。
- **Action**: 改为 "across NER (three datasets) and RE (SciERC)" 或类似准确表述。

**W7. n=529 vs SciERC n=551 discrepancy** [Reviewer 共识]

- **位置**: §5.3
- **问题**: Bootstrap 用 n=529 但 SciERC test set 有 551 instances，22 instances 被 drop 原因未交代。
- **Action**: 一句话说明 filtering criteria。

---

### Minor

- Eq.(4) 分母 max 而非 union 需一句设计理由说明
- FK adaptation：N 个来自同一模型的 stochastic samples 不是 Fleiss' κ 假设的 independent raters，brief acknowledgment 即可
- Table 1 N=8 是 single-seed 还是 averaged 未说明
- EM majority-vote selection 在 Table 3 中标 "---"，应加 1-2 句解释 exact-match plurality 在 structured IE 中的退化问题（Reviewer 分歧点，R1 反驳 R2，见下文 Divergence）

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上独立达成完全一致：

1. **Selection 证据面过窄是最关键问题**（R1-N1 = R2-N2, unanimously critical）：correlation-selection gap 仅 1 dataset × 1 model 验证，但 framed 为 "fundamental disconnect"
2. **WNUT-17 系统数据缺失**（R1-N2 ⊃ R2-W3, unanimously critical）：5 signals 中仅报告 1 个不显著结果
3. **N=8 QE 缺 uncertainty**（R1-W1, R2 交叉同意）
4. **SJ threshold 未规范**（R1-W2, R2 交叉同意并提升严重性）
5. **RE selection 缺统计检验**（R1-W3, R2 交叉同意）
6. **Abstract RE 措辞需修正**（R2-W2, R1 交叉同意）

---

## Reviewer Divergence [REBUT]

1. **EM majority-vote selection (R2-W4)**：R2 认为 EM<1 时应实现 majority-vote selection；R1 反驳指出 structured IE 中 exact-match plurality 退化严重（通常仅 1-2 identical samples），consensus-proximity (SJ selection) 已是 soft majority vote。**Director 判断**：R1 的反驳有技术依据，降为 minor（加解释即可）。

2. **LLaMA SciERC N=8 数据完整性 (R1-W4)**：R1 认为 Table 1 SciERC 列仅 Qwen、LLaMA 数据不全；R2 部分反驳指出 CoNLL 有完整 cross-model 覆盖，但同意 Table 1 应标注 "Qwen-only"。**Director 判断**：R2 的反驳合理——CoNLL cross-model 差异极小（Δ=0.005），SciERC 缺失不影响核心 claim。标注即可。

3. **ρ=0.38 contextualization 严重性 (R2-N1 vs R1 交叉回应)**：R2 列为 critical，R1 同意需要但降为 should-fix（structured IE vs QA output space 不同，direct comparison 有误导风险）。**Director 判断**：采纳 R1 的降级——footnote 级修改，不构成 must-fix。

---

## Questions for Authors

1. WNUT-17 上 Voting/EM/FK/Logprob 的 ρ 和 AUROC 分别是多少？
2. CoNLL 的 best-of-N selection 结果（oracle-greedy gap 有多大）？
3. SciERC bootstrap n=529 中 22 instances 被 drop 的 criteria？
4. SJ Hungarian matching 是否有 minimum similarity threshold？无 threshold 时 sim≈0 matched pairs 占多少？
5. Table 1 N=8 主要结果是 single-seed 还是 averaged？

---

## Missing References

无重大遗漏。Round 1 指出的 Optimal SC、Difficulty-Adaptive SC、Generative Self-Aggregation、conformal prediction 等均已补充。49 条 bib 全部 cited，0 orphan，45 条 verified。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目未启用 `external_review.paperreview_ai.enabled`）。

---

## Round 0-1 遗留 Issue 修复状况

**24 个历史 issues 状态汇总**：
- ✅ **Resolved**: 19 个（R0-C1, R0-C2, R0-C3, R0-C5, R0-C6, R0-W1, R0-W4, R0-RR-D1, R1-N1, R1-N2, R1-N3, R1-N4, R1-W2, R1-W4, R1-W5, R1-W6, R1-W8, R1-W9, R1-W10, R1-M1, R1-M2, R1-M3）
- ⚠️ **Partially resolved**: 3 个（R0-C4 SJ 新颖性, R1-W1 SJ 形式化, R1-W3 ρ contextualization, R1-W7 constrained decoding）
- ❌ **Unresolved**: 0 个

论文从 Round 0 到 Round 2 改善显著，绝大多数遗留问题已修复或充分 hedge。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference / Strong Findings**

**Reviewer 1**: 3.5/5, Confidence 4/5
**Reviewer 2**: 3.5/5, Confidence 4/5

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 4.0 | 3.75 |
| Excitement | 3.0 | 3.0 | 3.0 |
| Reproducibility | 3.5 | 4.0 | 3.75 |

**核心判断**：方法论扎实、统计严谨的 empirical study。Quality estimation 分析是论文的强项，coverage 和 depth 达到 long paper 标准。Correlation-selection gap 是 genuinely useful negative result，概念贡献清晰。

两个 critical 问题制约 Conference 推荐：(1) selection gap 作为核心贡献仅在 1 dataset × 1 model 验证，evidence base 与 "fundamental disconnect" framing 不匹配；(2) WNUT-17 capability boundary claim 仅有 1 个不显著数据点支撑。

**如果 C1 和 C2 得到补充**（补 LLaMA SciERC selection + CoNLL selection appendix + WNUT-17 完整 signal table），论文从 3.5 提升到 4.0（Weak Accept）是可期的——evidence breadth 将匹配 framing breadth，核心 claims 将得到充分支撑。

**当前推荐**：Findings（如不补充实验）/ Conference（如补充后 evidence 支撑 claims）。

---

## Detailed Comments（逐节）

### Abstract
- "across NER and RE on three datasets" 需修正为 "NER (three datasets) and RE (SciERC)"
- 其余 claims 与正文一致，无 overclaim

### Introduction (§1)
- Contribution #2 的 framing 应限定 evidence scope
- Contribution #3 需 WNUT-17 完整数据支撑
- PaLM-540B attribution ✓, scope 已收窄 ✓

### Related Work (§2)
- 覆盖全面，无遗漏
- 与 Nédellec et al. 的三点差异化清晰

### Method (§3)
- Per-sample vs instance-level formulation 精确
- SJ: sim 和 g_i/g_j 已定义，Hungarian threshold 和分母 variant 需补充
- Consensus-proximity = LOO-SJ 已明确
- FK independent raters 假设可 brief acknowledge

### Experiments (§4-5)
- QE (Table 1): 需 N=8 uncertainty estimates
- Selection (Table 3): 需扩展到 LLaMA SciERC + CoNLL appendix
- RE selection: 需 bootstrap 统计检验
- WNUT-17: 需完整 signal table
- n=529 vs 551: 需说明 filtering

### Discussion (§6)
- QE vs selection 区分清晰 ✓
- Logprob failure analysis 充分 ✓
- Constrained decoding 讨论需从 logprob-specific 扩展为全局 confound
- ρ=0.38 cross-method contextualization 需 footnote

### Conclusion (§7)
- 三个 findings 准确反映论文内容
- RE limitation hedge ✓

### Limitations
- 诚实且全面
- 需增加 constrained decoding confound 条目