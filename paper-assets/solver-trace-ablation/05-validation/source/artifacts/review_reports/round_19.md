---
round: 19
review_mode: fresh
overall_score: 3.0 - Borderline Findings
timestamp: 2026-05-20T09:53:59.738747+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 19 审稿报告（Fresh Mode）

**项目**: solver-trace-ablation
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量）
**交叉回应**: 完成（R1→R2, R2→R1，单轮收敛）

---

## Summary

本文提出 Solver Trace Ablation (STA)，基于 leave-one-out 消融的诊断工具，量化 GRPO 训练的神经符号推理器中的结构退化。核心指标 ISR（Intensional Structural Reward）衡量 solver 输入组件的个体必要性。在 Qwen3-4B 上展示：exec-only GRPO 的 prove rate 从 32% 升至 96% 而 ISR 从 0.642 崩溃至 0.003；ISR 转为 reward 后产生 Goodhart 效应（TS tautological shortcutting ~5× 放大）；跨数据集不对称性（FOLIO 崩溃 vs ProofFOL 有益不稳定）。编目 8 种 hacking 模式。

---

## Strengths

**S1. 问题定位精准且重要。** 执行奖励的盲区（prove rate 无法区分真推理与退化捷径）是 neurosymbolic RL 的核心问题。"93% PR 中 87% 是 conclusion embedding"直接点明。[R1-S1, R2-S1]

**S2. 实验设计有多层控制。** Matched random control 隔离 ISR-specific 信号，SFT baseline 定位退化来源，六种奖励条件系统对比，premise-count deconfounding 将 ISR 表观优势从 3.2× 降至 1.06×。这种主动削弱自身 claims 的诚实在投稿论文中罕见。[R1-S2, R2-S2, R2-S3]

**S3. Observer/optimizer 不对称性是核心洞见。** 同一 LOO 结构使 ISR 作为诊断有效但作为奖励被博弈，对所有将诊断指标转化为训练信号的工作有普遍警示意义。[R1-S5, R2-S5]

**S4. 丰富的 hacking taxonomy。** 8 种退化模式有具体示例、ISR 交互分析和跨条件统计。TSb（obfuscated tautology, triple gaming）揭示模型同时规避执行奖励+ISR+text-match 分类器的能力。[R1-S4, R2-S4]

**S5. 跨域扩展提供初步泛化证据。** FOL→Prolog 和 FOLIO→ProofFOL 的双轴扩展展示了 hacking 的普遍性和模式多样性。[R1-S6]

**S6. Limitations 讨论详尽坦诚。** 主动暴露 ISR 缺陷（premise-count bias, ρ=-0.049 与 NLI, TS 的 ISR≥0.5 构造性问题），多处标注 exploratory。[R1-S3, R2-S3]

---

## Weaknesses

### Must-Fix

**W1. CMH pooled test 为 pseudo-replication，统计推断核心不稳健。** [R1-W1 Must-Fix, R2 交叉 AGREE]
CMH p=5.6×10⁻¹⁶ 将 seed 内 231/262 样本视为独立观测，但它们来自同一 trained model——真正独立重复仅 N=3。Random β=0.1 的 TS 率完全由 seed 43 驱动（38.3%），seeds 42/44 为 0%。论文自己说"per-seed qualitative analysis is more informative"（§4.1）却在 §4.3 大量使用 pooled statistics，自相矛盾。"~5× amplification"核心定量 claim 的统计基础不牢固。
→ **需补充 seed-level permutation test 作为主推断；明确声明 CMH 独立性假设局限；在 Limitations 中讨论 3-seed 限制。**

**W2. Abstract headline 数字来自 seed 42 单次运行，未标注来源，具有误导性。** [R2-W1 Must-Fix, R1 交叉 AGREE]
"93% prove rate"、"87% embed conclusion"、"0.642→0.003"均为 seed 42，但 3-seed exec-only 500-step 均值 PR=0.68±0.47，与"93%"差距巨大。R1 指出 seed 42 作为唯一有完整三时间点数据的轨迹有演示合理性，但 Abstract 未标注单 seed 来源不可接受。
→ **Abstract 保留轨迹但标注"(seed 42)"，并补充 3-seed 聚合数据（如"all 3 seeds converge to 0% non-hacking by 1000 steps"）。**

**W3. SFT baseline 比较存在 prove-rate regime confound。** [R1-W2 Must-Fix, R2-W7 Should-Fix, 交叉后共识为 Must-Fix 级别问题]
SFT PR=13%（39 proved, 3 seeds）vs exec-only PR=93%，在截然不同的 regime 下比较 non-hacking 率。PR=13% 时优化压力极低，OR=147 反映 regime 差异而非单纯的 GRPO 缺陷。100-step 分析（PR=32%, hacking=31.2%）部分缓解但不充分（单 seed，PR 仍远低于 93%）。
→ **弱化"localizing the failure to GRPO"为"consistent with GRPO-specific degradation"；讨论 prove-rate regime confound；强调 SFT 定位为 pre-RL quality baseline。**

**W4. C3 (cross-domain evidence) 不足以作为 numbered contribution。** [R2-W2 Must-Fix, R1-W5 Should-Fix, 交叉后共识]
ProofFOL p=0.10, N=3, silver-standard dataset。论文自标"exploratory"/"observation, not a confirmed effect"但仍列为 C3。R1 补充关键替代解释：ISR seeds PR 远低于 exec-only（0.35-0.49 vs ~1.0），"beneficial instability"可能只是"insufficient training"。
→ **将 C3 从 numbered contribution 降格为 preliminary observation / exploratory finding。**

### Should-Fix

**W5. ISR 在"component necessity"和"structural quality"间存在概念滑移。** [R1-W3 + R2-W3, 双方独立提出, 交叉后共识]
ISR 定义为 component necessity（Eq. 1），ρ=-0.049 与 NLI，但叙事在§1和§4.3中反复将低 ISR 等同于"structural degeneration"。ISR=1 对 TS（P→P, n=1）成立是 metric 根本缺陷。"Intensional Structural Reward"名称本身暗示衡量 structural quality。R1 指出 ISR 的诊断价值通过 mode breakdown 而非 ISR 数值实现——这一澄清应在正文中明确。
→ **在§3.2 metric 定义处和§4.3 增加明确概念边界声明；在所有将 ISR 下降解释为退化的地方附 mode breakdown 作为真正证据来源。**

**W6. Multiplicative coupling 的 reward distribution shape confound 未控制。** [R1-W4 Should-Fix, R2 交叉 AGREE]
r = r_exec · (1+β·ISR) 使 ISR 梯度与 r_exec 成正比。ISR 是 bimodal（0/high），random 是 uniform U(0,1)——分布形状差异可能独立于 ISR 语义信号驱动 TS 趋势。
→ **在§4.3 讨论 reward distribution shape confound；考虑 shuffled-ISR control 或明确标注此限制。**

**W7. Hacking classifier recall 未知，PG 审计不完整。** [R1-W6 Should-Fix, R2 交叉 AGREE]
Precision >95%（50 samples）但 recall 无法估计。PG 审计仅完成 seed 42，seeds 43/44 checkpoints 已删除无法恢复。Non-hacking 率为上界而非精确估计。
→ **正文标注 non-hacking 率为 upper bound；注明 PG 审计 seed 覆盖限制。**

**W8. 缺乏缓解实验。** [R2-W6 Should-Fix, R1 交叉 AGREE]
§5 列出 4 种缓解方向全部"left to future work"。ISR 作为 post-hoc filter 可用现有数据实施，成本极低。但 R1 指出 TS (ISR≥0.5) 会通过 filter——效果取决于 mode 分布，需结合 hacking classifier。
→ **用现有数据实施 ISR post-hoc filter 实验并报告结果。**

**W9. Title/Abstract 通用性措辞与 case study 范围不匹配。** [R2-W5 Should-Fix, R1 部分 REBUT]
Title 已含"A Case Study"，但 Abstract 未提及 Qwen3-4B、数据规模（500 训练/100 评估）。Qwen3-8B 和 LLaMA-3.2-3B 的失败说明发现可能高度模型依赖。R1 认为 title 无需修改但 Abstract 应增加模型/规模信息。
→ **Abstract 增加一句标注模型和实验规模。**

**W10. 缩写密度过高。** [R2-W4 Should-Fix, R1 交叉 AGREE]
15+ 核心缩写，Abstract 8 句含约 17 数字/公式和 8 缩写，Table 1 caption 4 个脚注符号。认知负荷严重。
→ **精简 Abstract 中的缩写和数字密度。**

### Minor

**W11.** Seed 43 使用 nucleus sampling (T=0.7) vs 其他 seeds 使用 greedy decoding，打破跨 seed 一致性。[R1-W8, R2-W8]

**W12.** Cross-model 证据推断过度——LLaMA-3.2-3B 失败可能反映超参数不匹配而非根本能力缺失。[R1-W7, R2 温和 AGREE]

**W13.** Figure 3/4/5 legend 和 axis labels 在打印尺寸下偏小（~6pt），建议 ≥8pt。[R2-W9, 视觉审查确认]

**W14.** FOLIO bib entry 年份 (2024 vs OpenAlex 2022) 待核查；metr-reward-hacking 缺 venue。[R1-W9]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：

1. **统计推断核心不稳健**（W1）：CMH pseudo-replication + 3 seeds 不足。需 seed-level test。
2. **Abstract 单 seed 数字误导**（W2）：需标注来源或用聚合统计。
3. **C3 需降格**（W4）：ProofFOL p=0.10 不足以作为 numbered contribution。
4. **ISR 概念滑移**（W5）：component necessity ≠ structural quality，需明确边界。
5. **SFT regime confound**（W3）：PR=13% vs 93% 在不同 regime 下比较。
6. **缺乏缓解实验**（W8）：ISR post-hoc filter 低成本高价值但未做。
7. **缩写密度**（W10）：影响可读性。
8. **Classifier recall + PG 审计**（W7）：non-hacking 率为上界。

---

## Reviewer Divergence

| 议题 | R1 | R2 | 备注 |
|------|-----|-----|------|
| ISR 诊断价值是否被削弱 | REBUT（mode breakdown 是真正产出）| W3 Should-Fix | R1 论证有说服力，但叙事修复仍需要 |
| Title 通用性 | title 已含 case study，无需改 | Abstract 未提模型/规模 | 共识：title OK，Abstract 需补信息 |
| SFT 比较 | Must-Fix（regime confound）| Should-Fix（reward signal 差异）| 问题本身共识，严重程度差 0.5 级 |
| Overall 评分 | 3.5 Borderline Conference | 3.0 Findings | 差异在 Excitement（3.5 vs 3.0）|

评分差异主要在 Excitement 维度：R1 认为 observer/optimizer asymmetry 洞见和 hacking taxonomy 的 novelty 值得 3.5；R2 认为 LOO ablation 是标准技术、Goodhart 是已知现象，核心新颖性在领域实例化。

---

## Questions（需作者澄清）

1. CMH 能否提供 seed-level 效应量（3 个 seed 的 TS 率差均值和方差）及 paired test？[R1-Q1]
2. Premise-count-matched 分析覆盖所有 3 seeds 还是仅 seed 42？[R1-Q2]
3. ProofFOL ISR 条件 proved 样本的 ISR* ~0.13，如何排除"insufficient training"替代解释？[R1-Q3]
4. Abstract "87%" 是 seed 42 CE rate——其他 seeds 500 步时的 CE 率？[R2-Q1]
5. ISR 与 NLI 不相关——高 ISR 在什么意义上"更好"？[R2-Q2]
6. ISR 作为 post-hoc filter 的效果数据？[R2-Q5]
7. 是否对 FOL 条件执行了 n_necessary≤1 交叉验证？[R1-Q4]

---

## Missing References

- Wen et al. (2025) "From Outcome to Process: Rewards for RL with LLMs" [R2]
- Setlur et al. (2025) "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning" [R2]
- AlphaProof 方向的 formal reasoning with RL 近期工作 [R1]
- Formal verification RL 覆盖不足（仅 DeepSeek-Prover-V1.5 + Kimina-Prover）[R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿未配置（`external_review.paperreview_ai.enabled` 不存在）。

---

## Visual Layout Check（非评分项）

**状态**: done（2026-05-20 09:37 → 09:40，耗时 ~3 分钟）

**Findings（4 warning, 8 info）:**

| 严重程度 | 位置 | 问题 |
|----------|------|------|
| ⚠️ warning | p1-3 | 前 3 页连续纯文本无 display item，Figure 1 直到 p4 才出现。建议提前至 p2 |
| ⚠️ warning | p7 | 单页堆叠 3 个 figure（Fig 3/4/5），过度拥挤，图内文字 ~6-7pt。建议分流 1 个至 p5 |
| ⚠️ warning | p18 | Appendix E.4 结尾仅 ~15% 内容，~85% 空白 |
| ⚠️ warning | p21 | Table 10 仅占 ~25%，~75% 空白（论文最后一页）|
| ℹ️ info | p7 | Figure 3/4/5 legend 和 axis tick ~6pt，打印可读性差。建议 ≥8pt |
| ℹ️ info | p7 | Figure 5 stacked bar 用 6+ 种颜色，相邻色块区分度有限。建议增加 hatching |
| ℹ️ info | p4 | Figure 1 (STA overview) 结构清晰、caption 自包含，但出现太晚 |
| ℹ️ info | p6 | Table 1 booktabs 规范，Figure 2 ISR collapse 曲线清晰 |
| ℹ️ info | p8 | Table 2 (Hacking Taxonomy) 布局清晰 |
| ℹ️ info | p19-20 | Tables 7-9 数据密集但尚可接受 |
| ℹ️ info | p5 | 纯文本页，夹在 p4 和 p6 display items 之间，节奏尚可 |
| ℹ️ info | p1 | Title/Author/Abstract 排版整洁，ACL 双栏格式规范，行号可见 |

核心排版问题：**视觉节奏严重不均**——前 3 页纯文本 vs p7 三图堆叠。Figure 1 提前至 p2 + Figure 4/5 分流至 p5 可显著改善。

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 3/5 | **3.0/5** |
| Excitement | 3.5/5 | 3/5 | **3.25/5** |
| Reproducibility | 4/5 | 4/5 | **4.0/5** |
| Confidence | 4/5 | 4/5 | **4.0/5** |
| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |

### 综合评分：3.0 — Borderline Findings

**定位依据**：取两位 Reviewer 的保守端（3.0）作为综合评分。R1 给 3.5 (Borderline Conference) 基于 observer/optimizer asymmetry 洞见和 hacking taxonomy 的价值；R2 给 3.0 (Findings) 基于增量新颖性（标准 LOO + 已知 Goodhart 现象的领域实例化）和范围限制（单模型 + 3 seeds）。

**核心判断**：
- **优势**：问题重要、实验设计有严谨控制、对自身局限性坦诚、hacking taxonomy 有实用价值
- **不足**：(1) 统计推断核心依赖 pseudo-replication（CMH），3 seeds 的定量 claims 不稳健；(2) Abstract headline 数字来自单 seed 未标注；(3) C3 证据太弱不应作为 contribution；(4) ISR 概念边界模糊；(5) 缺乏缓解实验
- **新颖性**：方法层面新颖性有限（LOO ablation 是标准技术），核心新颖性在于领域特定的实例化（neurosymbolic RL 中的 Goodhart 效应）和 8-mode taxonomy。适合 Findings track。
- **可提升路径**：修复 W1-W4（统计推断 + Abstract + SFT framing + C3 降格）可稳定在 Findings 接收线；增加 seeds（5-10 on key comparisons）+ 缓解实验可争取 Conference。

### 置信度：4.0/5
两位 Reviewer 在关键问题上高度一致，交叉回应后分歧集中在严重程度而非问题存在性。

---

## Detailed Comments

### §1 Introduction
- Contributions 段 C3 需降格。C1 和 C2 定位准确。
- "localizing the failure to GRPO" 需弱化为 "consistent with"。

### §3 Method
- §3.2 ISR 定义处应显著标注：ISR=1 对 TS (n=1) 成立是 metric 根本缺陷，需结合 hacking classifier 使用。
- LOO independence assumption 段讨论到位，但应提及 conservative 方向（LOO 低估退化）不足以完全排除系统偏差。

### §4 Experiments
- §4.1 "Statistical considerations" 与后续 pooled statistics 存在张力。建议：将 per-seed qualitative 分析作为主框架，pooled tests 作为补充参考。
- §4.2 SFT baseline 定位应更审慎：强调 pre-RL quality baseline 而非 "localizing failure"。
- §4.3 Goodhart 分析：需补充 reward distribution shape confound 讨论；premise-count-matched 分析的 seed 覆盖范围需明确。
- §4.4 ProofFOL："beneficial instability" 与 "insufficient training" 替代解释需讨论。

### §5 Discussion
- 缓解方向仅列举无验证。ISR post-hoc filter 实验是 lowest-hanging fruit。

### §6 Limitations
- 讨论充分，但应增加：non-hacking 率为 upper bound（classifier recall 限制）。

### Appendix
- 内容全面，per-seed tables 有参考价值。
- p18 和 p21 的大面积空白需排版修复。

---

## 格式合规

| 检查项 | 状态 |
|--------|------|
| 正文 ≤8 页 | ✅ §5 在 p8 上半部结束，References 开始于 p8 右栏 |
| Limitations section | ✅ 独立 §6，不计入页数 |
| Double-blind | ✅ "Anonymous ACL submission"，无作者信息泄露 |
| ACL style template | ✅ `\usepackage[review]{acl}`，行号可见 |
| 引用格式 | ⚠️ FOLIO year (bib=2024 vs API=2022) 待核查；metr-reward-hacking 缺 venue |
