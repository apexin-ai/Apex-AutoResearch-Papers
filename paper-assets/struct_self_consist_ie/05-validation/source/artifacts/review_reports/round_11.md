---
round: 11
overall_score: borderline
timestamp: 2026-05-16T04:34:42.028574+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 11 Consolidated Review Report
## Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction
**Target Venue**: EMNLP 2026 Main Conference (via ARR May 2026)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 写作质量)

---

## Summary

论文系统评估了 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE (NER + RE) 中的 quality estimation 和 sample selection 能力。核心发现是 "correlation-selection gap"：所有信号能预测输出质量（Spearman ρ 达 0.45）但无法改善 best-of-N 选择，尽管存在 13-18 pp 的 oracle headroom。4/5 信号是 instance-level 的（by construction 无法 per-sample ranking），第 5 个信号 LP 因 score compression（60% tied）而失败。Free-form decoding ablation 在 NER 上确认 compression 非 constrained decoding artifact；RE 上 LP selection 方向反转。实验覆盖 3 个 NER 数据集、1 个 RE 数据集、2 个模型族（3B-8B）、多 seed/温度/N。

---

## Strengths

**[S1] 统计方法论上乘** [AGREE: R1, R2]
Bootstrap CI、TOST with external anchors、permutation test、Fisher combined p、Bonferroni correction——在同类 empirical NLP 工作中属于高标准。三指标框架（ρ + AUROC + selection F1）的 dissociation 展示具有独立方法论价值。

**[S2] LP compression 诊断系统性强** [AGREE: R1, R2]
从分布特征（median range 0.041 nats）到条件分析（non-tied subset +2.9pp, p=0.004）到因果排除（free-form ablation std ratio 0.97）到 verbalized confidence 控制实验，形成了完整的证据链。这是论文最有洞察力的贡献。

**[S3] Appendix 质量极高** [AGREE: R1, R2]
15+ sections 覆盖了几乎每个 claim 的 robustness check：LOO-SJ equivalence、FK independence test、OOD analysis、ε sensitivity sweep、diversity-stratified selection、scale ablation 等。

**[S4] 诚实的 scope 限定和 Limitations** [AGREE: R1, R2]
RE 结论标注 preliminary、free-form ablation 限制明确、scale 范围声明——论文的 intellectual honesty 值得肯定。

**[S5] Matched training protocol** [AGREE: R1, R2]
两个模型族使用完全相同的训练配置，消除训练 confound，增强跨模型比较可信度。

**[S6] 清晰的 practical recommendations** [AGREE: R1, R2]
VC for hard NER, EM for easy NER, LP for RE——对 IE 实践者有直接参考价值。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF1] RE 覆盖不足 vs title/abstract "Information Extraction" scope** [AGREE: R1-N1, R2-N2 — 强共识]
- Title 和 Abstract 前两句将贡献定位为 "Information Extraction" 涵盖 NER + RE，但 RE 仅有 SciERC 一个 benchmark（40% zero-F1, n=397 non-empty）。NER 有 3 个 benchmark 跨难度梯度。"Preliminary" 在正文出现 11+ 次但 title/abstract 未反映。
- **影响**：单一 RE benchmark 不足以支撑 "IE" 级别 claim。这是跨 11 轮审稿反复出现的持久性问题（首次 R0-C3）。
- **建议**：(1) 增加至少一个 RE benchmark（TACRED/DocRED/ACE05），或 (2) 将 title 限定为 NER-focused + RE 作为 exploratory extension，或 (3) 将 RE 结论完全移至附录。

**[MF2] ε=0.05 tied-fraction threshold 的 circularity** [AGREE with nuance: R1-N2, R2 agrees core but notes main results ε-free]
- Appendix G 声称 median LP range (0.041) 低于 ε=0.05 作为 "data-driven justification"——这是 circular reasoning。Table 11 ε sweep 中 ε=0.05 恰好给出最强 p=0.004，有 p-value optimization 之嫌。
- **缓解因素**（R2 指出）：主 selection 结果（Table 2 LP 直接排序，Δ=+0.2pp, p=0.29）不依赖 ε。Appendix G 也报告了 ε-free 连续指标 pooled within-instance ρ=0.248。Circularity 影响辅助 tied/non-tied 分析 credibility，不动摇主结论。
- **建议**：(1) 删除 "data-driven justification" 措辞；(2) 用 ε-free 连续指标（median LP range + pooled within-instance ρ）作为主要呈现；(3) ε sweep 保留但标注 "post-hoc exploratory analysis"。

**[MF3] Instance-level signals "fail by construction" framing 需改进** [PARTIAL: R2-N1, R1 partially agrees]
- 4/5 信号因 instance-level 粒度无法 rank candidates 是定义层面必然，不应列为 empirical contribution。论文自己承认 "fail by construction" 却列入 Contribution 1。
- **R1 反驳要点**：Metric dissociation（ρ/AUROC/selection F1 decoupling）有 empirical 内容——如 VerbConf ρ > LP 但 selection 最差（Appendix K），LP full/conditional ρ inversion（Table 4）。这些需要数据展示。
- **共识**：将 instance-level/per-sample 分类移入 §3 作为 problem formulation 前提，Contribution 1 reframe 为纯 empirical dissociation（ρ vs AUROC vs selection F1 解耦）。

### Should-Fix（影响评分但不一票否决）

**[SF1] Scale range (3B-8B) 不足以支撑因果结论** [AGREE: R1-W1, R2-W4]
- "Task difficulty is the primary driver" 仅基于 3B-8B 两个规模点。70B+ 模型的 LP 分布可能有质的变化。
- 建议：弱化为 "task difficulty is a stronger predictor than model scale within the 3B-8B range tested"。

**[SF2] 3 seeds 统计效力不足** [AGREE: R1-W2, R2]
- Kendall's W=1.000 with n=3 不具统计信息量。σ≤0.026 基于 n=3，95% CI 极宽。
- 建议：增至 5-10 seeds 或弱化 stability measures 的措辞。

**[SF3] 缺少信号组合实验** [AGREE: R1-W4, R2]
- LP non-tied subset 的 +2.9pp gain 暗示 VC 筛选 + LP 排序等 cascaded 策略可能有效。论文 Discussion 建议 trained verifiers 但未探索 simpler combinations。
- 建议：增加至少一个 combination baseline（如 VC-filtered LP selection）。

**[SF4] LP compression 缺乏 mechanistic explanation** [AGREE: R1, R2-W2]
- 论文详细 characterize 了 compression 现象并排除了多个原因，但未解释 WHY。
- 建议：Discussion 增加 hypotheses 段落——token averaging 平滑 variance、schema-enforced tokens 占多数导致有效 variance 来源少、constrained decoding 下 effective vocabulary 缩小等。

**[SF5] "Preliminary" 标注过于频繁** [AGREE: R1, R2-W1]
- 11+ 次出现给人 "工作未完成就提交" 的印象。
- 建议：首次完整说明后用 † 标记替代。

**[SF6] "Greedy" baseline 命名混淆** [AGREE: R1-W3, R2]
- NLP 中 "greedy" 通常指 argmax (T→0)。T=1.0 single sample 应命名为 "single-sample baseline"。Table 2 caption 已标注但正文其他位置未限定。

**[SF7] 与 Yao et al. (2026) 增量贡献定义不够清晰** [DIVERGENT: R2-N3, R1 rebuts]
- R2 认为三个 extension 中 SJ vs EM 仅 marginal significance、selection 是 negative result、WNUT collapse，combined novelty 有限。
- R1 反驳：structural vs LP gap clearly significant (Δρ=+0.155, CI [+0.074, +0.234])；selection analysis 是 test-time scaling 社区最关心的问题；WNUT LP full/conditional inversion 提供 diagnostic insight。
- **建议**：Introduction 增加与 Yao et al. 的明确差异 tabulation。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：
1. RE 单一 benchmark 与 title scope 不匹配（strongest consensus）
2. ε=0.05 circularity 存在（影响程度有分歧——R1 认为 critical，R2 认为仅影响辅助分析）
3. Scale 3B-8B 不足以支撑因果结论
4. 3 seeds 统计效力有限
5. 需要信号组合实验
6. LP compression 需 mechanistic explanation
7. "Preliminary" 过频
8. "Greedy" 命名混淆
9. 统计方法论是论文强项
10. LP compression 诊断分析是核心贡献
11. Appendix 质量极高

## Reviewer Divergence

**[DIV1] LP "intrinsic" claim vs RE free-form reversal (R1-N3 vs R2 rebut)**
- R1：RE LP selection 在 free-form 下从 −0.68pp 反转为 +1.69pp，至少对 RE，constrained decoding 是 LP selection failure 的一个因素。Abstract 措辞过强。
- R2：LP **分布** 在两种 regime 下几乎一致（std ratio 0.97），compression 本身确实 intrinsic。RE 反转的是 **selection outcome** 非 LP 分布。Abstract 已正确区分。但同意论文未充分解释 WHY compressed LP 在 RE free-form 下有效。
- **Director 判断**：R2 的区分有道理——分布 vs selection outcome 是不同层面。但 R1 的核心批评也合理：Abstract 措辞可以更精确。建议保持当前 Abstract 措辞（已区分 NER/RE）但在 Discussion 补充 RE reversal mechanistic hypothesis。降级为 warning 而非 critical。

**[DIV2] Novelty sufficiency for main conference (R1: 3.5/5 vs R2: 3.0/5)**
- R1 认为 combined novelty 足够 borderline main conference；R2 认为仅够 Findings。
- 核心分歧：selection analysis 作为 negative result 的价值判断。R1 认为 "more samples ≠ better selection in structured IE" 对 test-time scaling 社区有重要意义；R2 认为与 MBR 文献已知 utility-quality misalignment 增量有限。

**[DIV3] Conformal prediction 覆盖 (R2-W3 vs R1 rebut)**
- R1 认为 conformal prediction 构建 prediction sets，与 best-of-N selection 目标 fundamentally 不同，brief mention 足矣。
- **Director 判断**：同意 R1，Related Work 一句简要提及即可。

**[DIV4] Gold-empty filtering 跨数据集可比性 (R1-W5 vs R2 rebut)**
- R2 认为比例差异反映 dataset 特征而非 confound，selection 分析用 full set 不 filter。
- **Director 判断**：同意 R2，非 confound。但建议报告 CoNLL full-set ρ 作为参考。

---

## Questions to Authors

1. ε=0.05 的选择是否先于 LP range 分析确定？如果是 post-hoc 选择，是否有 pre-registered 替代方案？
2. Table 3 NER selection 为何用 2 seeds 而非 3？是 data availability issue 还是 design choice？
3. 是否考虑过 LP + consistency signal 组合策略（如 VC-filtered LP selection）？如有结果请提供。
4. Free-form RE LP reversal 是否在 T≠1.0 下也成立？
5. 增加 TACRED 或 ACE05 RE benchmark 是否预计 RE conclusions 会有质性变化？
6. LP compression 的 mechanistic cause 有无初步假说？

---

## Missing References

以下引用经两位 Reviewer 共识或一方同意、另一方未反对：
1. **Fernandes et al. (2022)** "Quality-Aware Decoding for Neural Machine Translation" — 将 QE 与 MBR 结合用 learned estimator rerank，与本文 "trained verifiers" 建议高度相关 [AGREE: R1, R2]
2. **Conformal Structured Prediction (ICLR 2025; arxiv 2410.06296)** — set-valued uncertainty for structured prediction，tangential but worth brief mention [AGREE: R1, R2]
3. **"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs" (arxiv 2605.07806)** — alternative self-assessment dimensions，与 verbalized confidence failure 相关 [AGREE: R1, R2]

以下引用有分歧（一方提出，另一方认为非必要）：
4. **Huang et al. (2024)** "Large Language Models Cannot Self-Correct Reasoning Yet" — R1 提出，R2 反驳（self-correction ≠ self-consistency，paradigm 不同）
5. **"Learning When to Sample" (arxiv 2603.08999)** — R2 提出，R1 反驳（discrete-answer，已有充分覆盖）
6. **Slim-SC / Thought Pruning (EMNLP 2025)** — R2 提出，R1 反驳（discrete-answer efficiency，不同问题）

---

## Overall Assessment

**Score**: borderline (between weak reject and weak accept for main conference)
**Confidence**: 4/5

**R1**: 3.5/5 — 方法论扎实，NER 结论有充分支撑，适合 borderline main / strong Findings
**R2**: 3.0/5 — novelty 不够 main conference，适合 Findings

**Director 综合判断**：

论文是一篇方法论扎实、统计严谨的 empirical study。LP compression 诊断和三指标 dissociation 框架有独立贡献。但存在三个核心限制：

1. **RE 覆盖不足**（跨 11 轮反复出现的持久性问题）——title 声称 "Information Extraction" 但 RE 仅有单一 benchmark，这是最大的 scope-evidence 不匹配。
2. **Novelty 边界模糊**——instance-level signals "fail by construction" 是 definitional 而非 empirical，去掉后核心 empirical 贡献（LP compression + MBR within-instance failure）增量需要更清晰地与 Yao et al. (2026) 和 MBR 文献区分。
3. **辅助分析 credibility 受 ε circularity 影响**——虽然主结论不受影响，但 tied/non-tied 分析是论文最引人注目的诊断，其 threshold 选择问题需要修正。

**推荐**：以当前状态适合 **EMNLP 2026 Findings**。若能 (1) 增加至少一个 RE benchmark 或将 RE scope 显式限定，(2) reframe Contribution 1 消除 definitional 成分，(3) 修正 ε circularity，则有潜力提升至 **borderline accept for main conference**。

---

## Detailed Comments (by Section)

### Abstract
- 信息密度适当，9 行 problem-finding-significance 结构。
- "NER and RE benchmarks" 应改为 "three NER and one RE benchmark" 以反映实际覆盖。
- "4-seed free-form decoding ablation confirms NER compression" 准确；RE reversal 描述也准确。
- 建议删减 "preliminary, single benchmark" 括号注——正文详述即可。

### Introduction
- Contribution 1 "Metric dissociation" 混合 definitional 和 empirical 元素，需重构。
- 与 Yao et al. (2026) 的差异描述过于简略（"we extend their work"），需要更具体的 tabulation。
- Figure 1 caption 不适用于 LP（per-sample signal）。

### Related Work
- 覆盖较为全面，Eikema et al. (2025) structured MBR 讨论到位。
- 缺少 Fernandes et al. (2022) Quality-Aware Decoding 和 Conformal Structured Prediction。
- 可增加简要提及 self-assessment limitation 文献。

### Method
- 信号定义清晰，公式完整。
- Instance-level vs per-sample 区分是论文的重要框架——建议从 §3.2 开头强调这一分类，为后续 gap 分析奠基。
- FK independence 假设通过 Appendix permutation test 验证，方法严谨。

### Experiments
- 实验设计系统，跨数据集/模型/seed/温度/N 的 coverage 全面。
- Table 1 单 seed (42) 已标注 + cross-ref 3-seed 表，处理得当。
- Table 3 NER 2-seed vs RE 单 seed 的不一致需解释。
- Scale ablation（Table 4）仅 Qwen 4B vs 8B，无 LLaMA 4B，限制了结论力度。

### Discussion
- Practical recommendations 清晰有用。
- LP compression 描述详尽但缺 mechanistic hypothesis。
- Free-form ablation RE reversal 需更深入讨论 WHY。
- "Trained verifiers" 前瞻有价值但略显 hand-wavy。

### Conclusion
- RE hedge 到位（"rest on SciERC alone"）。
- Scale 限定到位（"3B-8B"）。
- 整体简洁准确。

### Limitations
- 诚实且全面。Verbalized confidence 作为补充实验增强了可信度。
- 可增加：signal combination 未探索、ε threshold 选择局限性。

### Appendix
- 22 页中 12+ 页 appendix，质量极高。
- LOO-SJ equivalence、SJ normalizer robustness、FK independence test 等分析展示了罕见的 rigor。
- ε sensitivity sweep (Table 11) 需标注 post-hoc exploratory。
