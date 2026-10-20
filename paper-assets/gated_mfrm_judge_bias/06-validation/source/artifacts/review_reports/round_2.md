---
round: 2
review_mode: fresh
overall_score: 2.5
timestamp: 2026-05-23T01:19:47.787207+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：G-MFRM（Round 2 Fresh Review）

**论文标题**: Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation
**目标 Venue**: EMNLP 2026 (ARR May 2026)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验有效性；R2: 新颖性 + 完整性 + 写作质量）
**轮次**: Round 1 独立初审 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文将 LLM-as-a-judge 评估中 judge bias 和 benchmark contamination 的联合校正问题形式化为 omitted variable bias (OVB) 问题，提出 Gated Many-Facet Rasch Model (G-MFRM)，通过 multiplicative gating term $c_n \cdot e_i$ 联合估计 model ability、judge severity 和 contamination susceptibility。论文提供了 formal identifiability 分析（Theorem 1）和 error propagation bounds。合成实验（N=50）中 G-MFRM 将 ability RMSE 降低 43.8%（p < 10⁻⁶）。在 Arena-Hard 真实数据（N=8, J=6）上，G-MFRM 获得 nominally higher rank agreement（τ = 0.857 vs 0.786），但 bootstrap Δτ CI 包含零，posterior median τ 等于 baseline，结果统计不显著。

---

## Strengths

1. **问题形式化有 genuine novelty**：将 judge bias 和 contamination 的交互作用形式化为 OVB 是一个有价值的 insight，合成实验（r=0.86 between sequential bias and true c_n）有力支撑了 directional bias 的存在。对 LLM evaluation 社区有启发意义。[R1+R2 共识]

2. **理论框架完整且自洽**：OVB formalization (§2) → model specification (§3.1) → identifiability (§3.3, Theorem 1) → error propagation (§3.4) → Murphy-Topel variance correction (Appendix B)，构成完整的方法论链。Theorem 1 的 Schur complement proof (Appendix A) 是 sound 的。[R1+R2 共识]

3. **Error propagation bounds 有实用价值**：σ_crit ≈ 0.2 的阈值为 Stage 2 exposure estimation 的精度要求提供了 quantitative guidance（σ ≤ 0.2 时 θ-RMSE 降级 < 6%）。[R1+R2 共识]

4. **模型设计优雅**：c_n · e_i 的 graceful degradation（c_n=0 或 e_i=0 时退化为标准 MFRM）是 clean design。HalfNormal 层次先验提供 adaptive shrinkage。[R1]

5. **对局限的诚实报告**：论文在 §4.2 坦承主结果不显著、posterior median = baseline、CI coverage 不足。Conclusion 明确标注 "not significant at N=8"。[R1+R2 共识]

6. **合成实验设计严谨**：20-50 seeds Monte Carlo、多噪声水平 error propagation 测试、ablation 覆盖关键组件。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical] **§4.1 与 §4.2 judge 名称严重不一致——数据完整性存疑** [R1-N1, R2-N1, 全票 AGREE]

§4.1 列出 6 judges：GPT-5.5, Claude Opus 4.7, **Claude Sonnet 4.6**, DeepSeek-V4-Pro, **Qwen3-235B**, **Llama 4 Maverick**。但 §4.2 severity 结果列出：Claude Opus (+0.60), GPT-5.5 (+0.53), DeepSeek (+0.31), **Mistral** (−0.74), **LLaMA** (−0.42), **Qwen2.5-72B** (−0.35)。Claude Sonnet 消失、Mistral 凭空出现、Qwen3-235B 变成 Qwen2.5-72B。更严重的是 Qwen2.5-72B 同时出现在 target model contamination 结果中（ĉ_n = 3.00），存在 self-evaluation 循环问题。Appendix ablation 也引用 "Mistral −0.74"——系统性问题，非个别 typo。

**MF-2** [critical] **Introduction 与 Experiments/Ablation 数值矛盾** [R1-N2, R2 交叉 AGREE]

Introduction C3 写 sequential τ = 0.859 和 RMSE = 0.221 ± 0.038，但 §4.2 和 Table 3 (Appendix C) 均报告 staged estimation τ = 0.826 和 θ-RMSE = 0.273。同一设置（N=50, I=100, J=8），τ 差 0.033，RMSE 差 23%，无法用随机波动解释。可能引用了不同版本实验结果未统一更新。

**MF-3** [critical] **主结果统计不显著，posterior median τ = baseline** [R1-N3, R2-N3, 全票 AGREE]

Bootstrap Δτ 95% CI = [−0.071, 0.071] 包含零。Posterior median τ = 0.786，与全部 7 个 baseline 完全相同。τ = 0.857 的 point estimate 位于 posterior distribution 的 upper tail，不具代表性。P(Δτ ≥ 0) = 0.927 方向一致，但不足以支撑 ranking improvement claim。唯一真实数据实验无法支撑论文核心 claim。

**MF-4** [critical] **MCMC 收敛未达论文自设标准** [R1-N4, R2 交叉 AGREE]

§3.2 明确设定 R̂ < 1.01 和 ESS_bulk, ESS_tail > 400。§4.2 实际报告 R̂ ≤ 1.03 和 minimum ESS = 217——两个指标均未达标。脚注 post hoc 退回传统 1.05 标准。这是 internal inconsistency：方法章节设定严格标准，结果章节退而求其次。结合 71% CI coverage，posterior inference 可靠性存疑。

**MF-5** [critical] **Appendix Figure 3 (PPC) 是 placeholder** [R1-N5, R2-N2, 全票 AGREE]

PDF 第 12 页显示 "[FIGURE PLACEHOLDER — FIG_PPC.PDF PENDING SYNC FROM REMOTE SERVER]"。PPC 是验证模型拟合的关键证据，§4.2 引用 Appendix D 支撑 "adequate model fit" claim。投稿 PDF 含未完成的 placeholder 表明论文完成度不足。

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning] **7 个 baselines 产生完全相同 ranking** [R2-N4 critical, R1-W1 should-fix]

七种方法全部 τ = 0.786, ρ = 0.905。CyclicJudge+discard 移除 exposed items 仍同 ranking——与 contamination motivation 存在张力。可能因 N=8 下 τ 的 discrete nature 碰巧相同。需报告 raw scores 以区分真正 identical ordering 和离散巧合。R2 标为 critical，R1 标为 should-fix，最终定为 should-fix（有合理解释但需展开）。

**SF-2** [warning] **CI coverage 仅 71%** [R1-W5, R2-W6, 全票 AGREE]

50 Monte Carlo seeds 下 c_n 的 empirical CI coverage 71%，远低于 95% nominal。29% 真值在 CI 外。§4.2 中 "95% CIs entirely above 1.0" 的 contamination significance claims 可靠性受损。论文归因于 HalfNormal prior boundary + NUTS tree depth saturation，但未提供诊断证据或标准检查（如 SBC）。

**SF-3** [warning] **Stage 2 exposure estimation 设计决策缺乏论证** [R1-W2, R1-W3, 全票 AGREE]

75/25 权重仅以 Spearman ρ ≥ 0.998 验证 exposure ranking 稳定性，未报告 downstream τ 变化。Reference anchor (gpt-4-0314) 自身 contamination 风险无 robustness check。

**SF-4** [warning] **合成 N=50 显著但真实 N=8 不显著——缺 power analysis** [R1-W6, R2 AGREE]

论文只说 "the effect is real but below detection at this sample size"，缺 formal power analysis。读者无法判断需多少 N 才能检测到观察到的效应。

**SF-5** [warning] **γ_n 形式未给出** [R1-W4, R2 AGREE]

OVB 公式 plim(θ̃_n − θ_n) = γ_n · c_n 中，γ_n 仅描述性定义。对声称 "formalize" OVB 的论文，核心量不应隐式。

**SF-6** [warning] **Ablation table 标注 "preliminary"** [R1-W7, R2-W2, 全票 AGREE]

Table 3 caption 标注 "10 seeds; preliminary"。投稿论文不应含 "preliminary"。10 seeds 的方差估计不稳定。

**SF-7** [warning] **Conclusion 仅 2 句** [R2-W4, R1 AGREE]

约 40 词的 Conclusion 对 8 页 long paper 不充分。缺 broader implications、future work、takeaway。

**SF-8** [warning] **无代码/数据可用性声明** [R2-W7, R1 AGREE]

ARR 审稿包含 Software/Datasets 评分。Stage 2 pipeline 实现细节仅靠论文描述难以复现。

**SF-9** [info] **Limitations 计数错误** [R2-W1, R1 AGREE]

写 "three limitations" 实际列出四个。与 MF-1/MF-2 构成系统性 proofreading 问题 pattern。

**SF-10** [info] **遗漏相关工作** [R2-W5, R1 部分同意]

缺 Chernozhukov et al. (2022) OVB in causal ML（两位 AGREE）。Polo et al. (2024) tinyBenchmarks 和 Kipnis et al. (2025) MetaBench 为 nice-to-have（R1 认为非 critical omission，R2 认为应引用）。bib 中 Uto & Ueno (2020) 未被正文引用——应删除或引用。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全达成共识：

1. **Judge 名称不一致是最严重的问题**——不仅是 typo，涉及数据完整性和可能的 self-evaluation 循环（MF-1）
2. **主结果统计不显著，posterior median = baseline**——核心 claim 缺乏统计支撑（MF-3）
3. **Figure placeholder 不可接受**——投稿质量控制问题（MF-5）
4. **MCMC 收敛标准 internal inconsistency**——方法设定严格标准却在结果中未达标（MF-4）
5. **CI coverage 71% 是 substantial miscalibration**——影响所有 CI-based claims（SF-2）
6. **Ablation "preliminary" 标注不应出现在投稿中**（SF-6）
7. **论文存在系统性内部一致性问题**：judge 名称矛盾 + 数值矛盾 + 收敛标准矛盾 + limitations 计数错误 + figure placeholder + "preliminary" 标注——共同表明论文完成度不足

---

## Reviewer Divergence

1. **Abstract/Intro 呈现是否"误导性"**：R2 认为不显著限定被埋在细节中有误导性；R1 认为 "nominally" + abstract 内标注 CI 包含零已足够 honest。**共识**：措辞尚可，但底层问题（real-data evidence 不足）是真正关切。

2. **贡献新颖性**：R2 认为 G-MFRM 是 MFRM + DG-IRT 的增量组合；R1 认为 OVB formalization 有独立价值、identifiability 分析虽用标准技术但结论非平凡。**共识**：novelty incremental but not trivial；real-data 弱结果使 novelty bar 更高。

3. **7 baselines 相同 ranking 的严重程度**：R2 标为 critical，R1 标为 should-fix（N=8 下 τ discrete nature 可部分解释）。**共识**：should-fix，需更深入解释。

4. **Missing references 哪些真正遗漏**：R2 列 3 篇（Polo/MetaBench/Chernozhukov）；R1 认为 Chernozhukov 确实应引用，Polo/MetaBench 为 nice-to-have。**共识**：至少 Chernozhukov 应引用。

---

## Questions

1. §4.2 中 judge severity 列出的 judge names 与 §4.1 setup 不匹配。请澄清实际使用的 judges。[R1+R2]
2. Introduction 中 sequential τ=0.859/RMSE=0.221 与 §4.2/Table 3 中 τ=0.826/θ-RMSE=0.273 的差异来自何处？[R1, R2 confirmed]
3. "Point estimate" τ=0.857 具体指什么（posterior mean? MAP? specific posterior draw?）？Posterior median 为何等于 baseline？[R1]
4. 七个 baselines 的 raw model scores 或 rankings 是否也完全相同，还是仅 τ/ρ 因 N=8 离散性碰巧相同？[R1+R2]
5. CyclicJudge+discard 移除 exposed items 后仍同 ranking——contamination 对 ranking 实际有多大影响？[R2]
6. Horseshoe prior 的 CI coverage 是多少？如果同样差，问题可能在 sampler 而非 prior。[R2]
7. 是否计划开源代码和数据？[R2]

---

## Missing References

- **Chernozhukov, V., Cinelli, C., Newey, W., Sharma, A., & Syrgkanis, V. (2022).** "Long Story Short: Omitted Variable Bias in Causal Machine Learning." NBER Working Paper 30302. [R2 提出, R1 AGREE]
- **Polo, F. M., et al. (2024).** "tinyBenchmarks: evaluating LLMs with fewer examples." ICML 2024. [R2 提出, R1 认为 nice-to-have]
- **Kipnis, A., et al. (2025).** "MetaBench." ICLR 2025. [R2 提出, R1 认为 nice-to-have]
- **Talts, S., et al. (2018).** "Validating Bayesian Inference Algorithms with Simulation-Based Calibration." arXiv:1804.06788. [R1 提出, 作为 71% CI coverage 的标准诊断]
- **Uto & Ueno (2020)** 在 bib 中有但正文未引用——与本文高度相关（generalized MFRM + HMC）。[R1 提出]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成。主要发现：

- **[critical]** p.12 Figure 3 是占位符文字——与 MF-5 一致
- **[warning]** pp.1-3 连续 3 页纯文本无 display item，第一个视觉锚点（Figure 1+2）到 p.4 才出现。建议将 Figure 2（方法概览图）前置到 p.2 改善第一印象
- **[warning]** p.8 Related Work + Conclusion 整页纯文本无 display item
- **[warning]** p.13（Appendix 末页）仅用约 1/3 面积，空间利用率偏低
- **[info]** 主文 8 页内 display items 共 4 个（Figure 1-2, Table 1-2），密度 0.5/页，处于偏低端
- **[info]** 公式渲染正确，双栏对齐良好，无 margin 溢出，无 [?] 未解析引用，Tables 排版规范

---

## Overall Assessment

**评分: 2.5 / 5 — Borderline Findings**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 2.5 | 3.0 | 2.5 |
| Excitement | 3.0 | 3.0 | 3.0 |
| Reproducibility | 2.5 | 2.0 | 2.0 |

**R1 评分**: 2.5 (Borderline Findings)
**R2 评分**: 3.0 → 交叉后下调至 2.5-3.0 区间
**综合**: 2.5 (Borderline Findings)

**置信度**: 4/5（两位 Reviewer 均对 IRT/MFRM 和 Bayesian inference 有 sufficient expertise）

**核心判断**：

论文的理论贡献有价值——OVB 形式化、identifiability 证明、error propagation bounds 构成了完整的方法论框架，合成实验有力支撑了理论分析。但论文存在两类严重问题：

1. **实验可信度问题**：judge 名称 §4.1/§4.2 不一致（涉及可能的 self-evaluation 循环）、Introduction 与 Experiments 数值矛盾、figure placeholder、ablation "preliminary"——这些共同表明论文在提交前缺乏充分的质量控制和一致性检查。

2. **证据强度问题**：唯一真实数据实验（N=8）的主结果统计不显著，posterior median τ 等于 baseline，MCMC 收敛未达自设标准，CI coverage 仅 71%。合成数据 N=50 下结果显著，但 real-world evidence 不足以支撑论文的核心 claim。

在当前状态下，论文更适合作为理论框架+合成验证的 Findings paper，但需要修复所有一致性问题后才能达到该水平。如果作者能 (1) 修复全部数据一致性问题、(2) 增加 real-data evaluation 规模、(3) 达到自设的 MCMC 收敛标准，论文有潜力提升至 3.5（Borderline Conference）。

---

## Detailed Comments

### Section 2: Confounding in LLM Evaluation
- Observation 1 的 OVB formalization 是论文最有价值的 insight。但 γ_n 的具体形式未给出，削弱了理论完整性（SF-5）。建议至少在 Appendix 给出 MFRM 设定下 γ_n 的 explicit form。
- Footnote 1 解释 linear approximation，信息密度高但可读性差，建议拆成正文段落。

### Section 3: G-MFRM Framework
- §3.2 的 MCMC 收敛阈值（R̂ < 1.01, ESS > 400）必须与 §4.2 实际报告一致。如果无法达到 1.01/400，应诚实调整 §3.2 的声明并讨论 implications。
- §3.5 (Fair Scores and Diagnostics) 仅 3 行，作为独立 subsection 过于单薄，建议合并。
- Proposition 1 proof 中 "e_i ≠ 0 for at least one item by assumption" 未在 Proposition statement 中显式声明。

### Section 4: Experiments
- **最关键问题**：judge 名称不一致（MF-1）和数值矛盾（MF-2）必须首先解决，否则所有实验结论不可信。
- Murphy-Topel correction（Appendix B）已有推导但未报告 correction 前后 CI width 变化。
- "Position-swapped pairwise mode" 的具体含义（每对是否做两次、response 如何 aggregate）应更明确说明。
- Abstract 中 "G-MFRM identifies statistically significant per-model contamination (top-4 models' 95% CIs exclude zero)"——鉴于 71% CI coverage，这些 CIs 不可靠，"statistically significant" 需 qualifier。

### Section 5: Related Work
- 位置（Experiments 之后）不违规但不常见。
- 引用 Uto & Ueno (2020) 在 bib 中有但未在正文引用——应引用（generalized MFRM + HMC，高度相关）或从 bib 删除。

### Section 6: Conclusion
- 仅 2 句话（约 40 词）过于简短（SF-7）。应至少讨论 G-MFRM 的适用条件和更大规模验证方向。

### Limitations
- 计数错误：写 "three" 实际有 four（SF-9）。
- CI coverage 71% 作为第四点 limitation 存在，但在 §4.2 报告 CI 时未明确提示过窄风险。

### Appendix
- Figure 3 (PPC) 是 placeholder（MF-5），必须修复。
- Table 3 (Ablation) 标注 "preliminary"（SF-6），必须移除或完善实验。