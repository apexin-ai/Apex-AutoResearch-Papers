---
round: 16
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-23T13:33:58.265609+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 16

**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
**Venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计 + 统计分析；R2: 新颖性 + 完整性 + Related Work + 写作质量）
**轮次**: 1 轮初审 + 1 轮交叉分享（关键问题达成共识，无需第二轮）

---

## Summary

本文在 hybrid linear recurrent architectures 中首次系统分析 per-example predictive multiplicity。使用 Wang et al. (2025) 的 controlled model zoo（3 架构 × 5 attention ratios × 2 scales），在 10 个 benchmark 上评估 30 个配置，对 4 个 benchmark 进行 per-example decomposition。核心发现：(1) 不同架构在添加 attention 后影响的样本集高度不重叠（Jaccard ≈ 0.10，约为独立基线的 2 倍），5-architecture 验证的 40 个 pairwise 比较全部 p < .01；(2) per-example Jaccard 在 4% attention 时即饱和，而 aggregate variance 在 LAMBADA 上呈下降趋势但未达统计显著性（Bonferroni-adjusted p = .170）；(3) multiplicity 幅度取决于任务类型（α = 0.14–0.30）而非 attention 剂量。

---

## Strengths

**S1. 异常严谨的统计方法论。** [R1 S1, R2 Strength 2, 双方 AGREE] 精确置换检验（120 permutations）、显式 power analysis（n=5 下 |ρ|=0.9 仅 p=.083）、BCa bootstrap 标注为 "heuristic"、Bonferroni 跨全部 10 benchmark。统计透明度在 NLP empirical papers 中极为罕见，论文多处主动报告不利于自身 claim 的证据（如 convergence 依赖 GDN、bootstrap CI degeneration、Pythia calibration 三重 mismatch）。

**S2. Controlled experimental design。** [R1 S3, R2 Strength 1, 双方 AGREE] Wang et al. (2025) model zoo 实现真正的受控比较——所有模型共享训练数据、tokenizer 和 hyperparameters，仅在架构和 attention 配置上不同。这比通常的跨架构比较更具说服力。

**S3. Per-example 发现的统计鲁棒性。** [R1 S4, 双方 AGREE] Jaccard permutation test z > 5.9（all p < .0001）；5-arch 验证 40 个 pairwise 全部 p < .01；cross-scale Jaccard 稳定（J ≈ 0.08–0.10）。Per-example divergence 是论文最有力的发现，cross-benchmark 一致性强。

**S4. Jaccard saturation at 4% attention。** [R1 rebuttal to R2-N1, R2 Strength 3] 超出 prior work 可预测的范围——minimal attention 即足以 establish configuration-specific per-example patterns。对 hybrid architecture 的 attention ratio 选择有直接指导意义。

**S5. 全面的 robustness 分析。** [R1 S2, R2 Strength 4, 双方 AGREE] 21 个 appendix sections 覆盖 GDN confound sensitivity、normalized Jaccard effect size、continuous-threshold Jaccard、Pythia seed calibration、5-arch 扩展验证、cross-scale 比较。Robustness 密度在经验性论文中不常见。

**S6. Task-dependent α variation。** [R2 Strength 5] α = 0.14（PIQA/reasoning）到 0.30（LAMBADA/retrieval）的 task-dependent variation 为 practitioners 提供了何时需要 per-example audit 的实用指南。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical, CONSENSUS] **Aggregate convergence 叙事在 Abstract/Introduction 中仍过度突出，与 evidence strength 不匹配。**

尽管 §4.2 已标注 convergence 为 "suggestive but underpowered secondary observation"，Abstract 和 Introduction 第一段仍以 decoupling 为叙事主线。具体问题：
- Introduction 以 "cross-architecture standard deviation drops 79%" 开篇，先给 impressive effect size 再补 non-significant p-value（Bonferroni-adjusted p = .170），造成 misleading impression
- Figure 1 双面板设计暗示 convergence 和 Jaccard saturation 是对等发现，但 convergence 证据远弱于 Jaccard（convergence: 仅 LAMBADA 1/10 benchmarks，GDN-dependent，p = .170；Jaccard: 40 个组合全部 p < .01）
- 排除 GDN 后 ρ = -0.7, p = .233；340M 无 convergence（ρ = -0.50, p = .45）

建议：(1) narrative 从 "decoupling" 转向 "per-example divergence is robust regardless of aggregate behavior"——这是数据真正支持的更强 claim；(2) Abstract/Introduction 将 aggregate convergence 定性为 "non-significant trend on a single benchmark"；(3) Figure 1 caption 标注 convergence 的 p-value。

**N2** [critical, CONSENSUS] **Single training runs 无法确定性区分 architecture vs. seed effects，现有缓解措施不充分。**

Pythia 70M seed calibration（Appendix W）存在三重 mismatch：(a) scale（70M vs. 340M–1.3B，5–18× 差距）；(b) architecture family（Transformer vs. hybrid recurrent）；(c) accuracy regime（0.17–0.23 vs. ~0.50）。Within-architecture Jaccard (~0.33, Appendix M) 与 Pythia within-seed Jaccard (0.27–0.39, Appendix W) 存在 substantial overlap，进一步模糊 architecture/seed 边界。R2 补充：within-architecture 比较的模型可能共享 training state 前缀，高 Jaccard 可能部分来自此共享。

双方均认为这是 limitation 而非 fatal flaw——40 个 architecture-benchmark Jaccard tests 全部 p < .01 在纯 seed noise 下极不可能出现。但论文应在 contribution statement 中显式将 seed-vs-architecture disentanglement 标注为 open question。

**N3** [critical, DIVERGENCE: R2 Must-Fix, R1 Should-Fix] **相对于现有 multiplicity 文献，增量贡献界定不清晰。**

核心发现本质上是将 Marx (2020) / D'Amour (2022) 已建立的框架应用于新模型族。论文自身承认 ecological fallacy 是 well-known phenomenon。R2 认为仅适合 Findings；R1 反驳称 Jaccard saturation at 4% 和 5-arch validation 超出了 "known phenomenon in new domain" 的范畴，且 ACL ARR guidelines 明确列出 empirical study 为可接收论文类型。R1 承认论文缺乏 actionable methodology 贡献（routing 仅 1/4 benchmarks 有效）。

此分歧未解决。Director 评估：论文的贡献以 empirical characterization 为主，缺乏 methodological/theoretical/prescriptive novelty，但 characterization 本身的质量和深度（controlled design + rigorous statistics + comprehensive robustness）在同类工作中属上乘。

### Should-Fix（影响评分但不一票否决）

**W1** [warning, CONSENSUS] **Routing 实验过于初步且在 Conclusion/Abstract 中定位过高。**
- 10-repeat cross-validation 仅报告 mean gain（+5.3pp on LAMBADA），缺少 SD/CI/significance test [R1-W3]
- 仅 LAMBADA 有效（+5.3pp），ARC-Easy 边际（+1.0pp），HellaSwag/PIQA 无改善 [R2-W2]
- §4.1 已降级为 "illustrative case study"，但 Conclusion 仍将 routing 列为三大 practitioner implications 之一，Abstract 以此收束 [R2-W2]

**W2** [warning, R2 corrected R1] **BCa CI 在 Introduction 中首次出现时缺 "heuristic" caveat。**
- BCa CI [-1.0, -0.7] 不在 Abstract（R1 误判位置，R2 纠正）而在 Introduction（introduction.tex line 3）
- ~24 有效 resamples、BCa correction 在 ρ = -1.0 边界 degenerate → fallback to percentile CI
- Figure caption 已标注 "illustrative only"，但 Introduction 首次引用处缺 caveat

**W3** [warning, CONSENSUS] **5-architecture 扩展验证仅在 340M 进行。**
- GLA 和 DeltaNet 仅 340M 可用（model zoo 限制）
- 主文 §4.3 引用 5-arch 结果时未标注 "at 340M only"（仅 Appendix X 说明）
- 3-architecture 的 cross-scale stability（Jaccard ≈ 0.08–0.10 at both scales）提供间接支持

**W4** [warning, CONSENSUS] **K-choice binarization 对 hurt sets 的 agreement overestimate 未讨论。**
- §3.4 讨论了 binarization 的 "conservative bias"（低估 divergence），但未覆盖一个 specific scenario：两个架构都从 correct→incorrect 但选择不同错误答案时，binarization 将其计为 overlap
- Appendix O continuous Jaccard 从另一角度缓解，但 §3.4 应补充此 angle

**W5** [warning, CONSENSUS] **AUC 正态假设未验证。**
- Appendix P.2 使用 AUC = Φ(|d|/√2) 假设 |log p| 正态分布
- |log p| 通常右偏（特别是 stayed-wrong 组）
- 建议补充 empirical AUC 或 normality test

**W6** [warning, CONSENSUS] **模型规模覆盖有限。**
- 仅 340M 和 1.3B 两个规模点；2025-2026 年 hybrid architectures 主要应用在 7B+
- Cross-scale 分析显示 α 和 convergence 因 scale 而异，支持此 concern
- Limitations 提到 architecture coverage 但未显式讨论 scale limitation

### Nice-to-Have（不影响接收）

- Table 1 的 Ratio 列（endpoint change）与 ρ（monotonicity）并存可能误导读者，caption 应澄清 [R1-M1, R2 AGREE]
- §3.2 "informal pre-analysis plan" qualifier 应在正文提及而非仅在 Appendix A [R1-M2, R2 AGREE]
- Figure 1(b) shaded bands 计算方法不明（SD? SE? min-max?），"illustrative" 过于模糊 [R1-M3, R2 AGREE]
- §3.5 定义的 Mann-Whitney/Kruskal-Wallis 检验在正文中未报告具体结果 [R1-M4, R2 AGREE]
- Introduction 篇幅偏长（~1.5 页），与 §4 有定量细节重复 [R2 minor]
- Haghighat 2026 bib 条目需更新为 AAAI 2026（非 arXiv preprint）[R2 minor, R1 AGREE]
- Abstract 中 "+5.3pp" 应说明基线（majority vote 50.9%）[R2 minor]

---

## Reviewer Consensus

以下问题 R1 和 R2 达成 [AGREE]：
- **N1**: Aggregate convergence 叙事与 evidence 不匹配——需调整 Abstract/Introduction framing
- **N2**: Single-run limitation 是核心方法论弱点，Pythia calibration 三重 mismatch 使其缓解力度有限
- **W1**: Routing 实验初步且 over-framed，需 variance 报告 + Conclusion 降级
- **W2–W6**: Bootstrap CI caveat、5-arch scale caveat、binarization bias、AUC 假设、scale coverage
- 所有 minor issues

## Reviewer Divergence

**评分分歧（未解决）**：

| | R1 | R2 |
|---|---|---|
| Overall | 3.5 (Borderline Conference) | 3.0 (Findings) |
| Soundness | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 |
| Reproducibility | 4.0 | 4.0 |

- **R1 立场**: Jaccard saturation at 4%、5-arch validation、以及统计方法论的严谨性构成超出 "known framework in new domain" 的贡献。ACL ARR guidelines 明确列出 empirical study 为可接收类型。
- **R2 立场**: 核心贡献是 empirical characterization，缺乏 methodological/theoretical/prescriptive novelty。EMNLP main conference 对 novelty 有明确要求。Findings 是合适定位。

**次要分歧**：
- R2-W3 (ensemble diversity 文献不充分): R1 REBUT，认为 Related Work 覆盖 adequate
- R2-Q4 (α validity in binary classification): R1 REBUT，认为 Appendix R/S 已 adequately 讨论 binary classification 特殊性，"validity 问题" 表述过强

---

## Questions for Authors

1. **[R1-Q1, R2-Q1, 双方 highest priority]** 是否可能对至少一个 architecture × ratio 组合训练 2-3 个 seeds，以直接量化 seed-driven vs architecture-driven Jaccard divergence？
2. **[R1-Q3]** α 与 aggregate convergence 之间是否存在因果关系而非 decoupling？（R2 cross-response 指出 BoolQ α=0.45 无 convergence，否定了此假设）
3. **[R2-Q3]** Routing 在 α=0.14 的 PIQA 上失效、α=0.30 的 LAMBADA 上成功。是否存在 α threshold 以下 routing 注定无效？
4. **[R1-Q2]** 是否考虑过 overlap coefficient 等替代 set similarity measures 作为 Jaccard 的补充？

---

## Missing References

- **Watson-Daniels et al. (2025)**, "Systemizing Multiplicity," AIES 2025 — multiplicity 概念系统化框架 [R2 建议, R1 partial AGREE（需确认发表状态）]
- **Shen et al. (2023)** linear attention 与 gated recurrence 等价性 — 可补充 §2 linear recurrent models 讨论 [R1 建议, R2 partial AGREE（需确认具体是哪篇）]

已排除的建议引用：
- Jiang et al. (2024) Mixtral of Experts — R1 建议，R2 REBUT（MoE routing 与 per-example multiplicity 无直接关联）
- Wen et al. (2024) Batched LoRA — R1 建议，R2 REBUT（fine-tuning 与本文 pre-trained 评估无关）
- RWKV-7 (2025) — R2 建议，R1 REBUT（非本文 model zoo 中的架构，引用 added value 有限）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，跳过。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2026-05-23T13:12–13:15 UTC）。

**1 个 Warning**：
- Pages 3-5 连续 3 页纯文本（Related Work → Method §3.1-3.5 → Statistical Methods），无任何 figure/table/equation 穿插。建议在 Method 部分插入方法流程示意图或将 Table 1 提前以打破纯文字节奏。

**关键确认**：
- 主正文在第 8 页结束，Limitations 从 p8 底部延续到 p9 — 符合 EMNLP 2026 8 页限制
- ACL 双栏模板格式正确，无 margin 溢出、无 LaTeX 渲染错误
- 3 figures + 2 tables = 5 个 display items / 8 页（偏低但考虑大量分析在 appendix 展开，可接受）
- Figure 色彩方案色盲友好（单色渐变）
- References 无 [?] 未解析引用

---

## Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5**

本文提供了 hybrid recurrent architectures 中 per-example predictive multiplicity 的首次系统性实证分析。实验设计利用高控制度的公开 model zoo，统计方法论的严谨性和透明度在 NLP empirical papers 中属上乘——精确置换检验、显式 power analysis、21 个 appendix robustness sections。Per-example divergence 的核心发现具有统计鲁棒性（40 个 architecture-benchmark 组合全部 p < .01）和跨 scale 稳定性。Jaccard saturation at 4% attention 是超出 prior work 可预测的有趣发现。

主要限制：(1) 概念新颖性以 empirical characterization 为主，缺乏 methodological/theoretical/prescriptive 层面的独立贡献；(2) single training runs 无法确定性区分 architecture vs. seed effects，Pythia 70M calibration 的三重 mismatch 使此缓解不充分；(3) aggregate convergence narrative 在 Abstract/Introduction 中过度突出，与 non-significant 的统计证据不匹配；(4) routing 仅在 1/4 benchmarks 有效但在 Conclusion/Abstract 中定位过高。

**推荐 Findings 接收。** 如能 (a) 调整 narrative（de-emphasize convergence，reframe around per-example divergence robustness）、(b) 补充 routing variance 报告、(c) 更清晰定位 novelty contribution（将 Jaccard saturation at 4% 提升为独立 contribution），论文质量可进一步提升。如能在修订中增加至少一个 configuration 的 multi-seed spot check，有潜力达到 Borderline Conference。

---

## Detailed Comments（逐节）

### Abstract
- 接近但未超 200 words 限制（约 147 words），合规
- "+5.3pp" 应注明基线（majority vote 50.9%）
- "yet per-example overlap saturates at 4% attention" — 此句隐含 aggregate convergence 已确立为前提，建议改为明确两个独立发现的并列叙述

### Introduction (§1)
- 篇幅偏长（~1.5 页），与 §4 有定量细节重复（α range、Jaccard 值在两处出现）
- 第一段以 "cross-architecture standard deviation drops 79%" 开篇 — 这个 effect size 来自 Bonferroni-adjusted p = .170 的非显著结果，放在 opening sentence 给读者以显著效果的印象
- BCa CI [-1.0, -0.7] 首次出现时缺 "heuristic" caveat

### Related Work (§2)
- 覆盖面广且与先前工作的差异化清晰
- 建议补充 Watson-Daniels et al. (2025) "Systemizing Multiplicity"（如已发表）
- Haghighat 2026 bib 需更新为 AAAI 2026

### Method (§3)
- 统计方法描述详尽且审慎
- §3.2 "taxonomy was fixed prior to analysis" — 应在正文引用 Appendix A 的 "informal, not pre-registered" qualifier
- §3.4 binarization 讨论应补充 hurt-set agreement overestimate 的 specific angle
- Pages 3-5 连续纯文本，缺少 visual break

### Experiments (§4)
- Per-example 分析（§4.1）是论文最强部分，统计证据充分
- Routing 已降级为 "illustrative case study"（good），但 10-repeat 缺 variance 报告
- Decoupling（§4.2）的 narrative weight 与 evidence 不匹配
- Robustness（§4.3）的 5-arch 引用应标注 "at 340M only"

### Conclusion (§5)
- 三大 practitioner implications 中 routing（point 3）的 evidence 不足以支撑
- 建议将 routing 从 implication 降级为 future work direction

### Limitations
- 3 段覆盖 single-run、coverage、pre-training only — 符合 EMNLP 规则
- 建议补充 scale limitation 的显式讨论

### Appendix
- 21 个 sections 的 robustness checks 是论文的显著优势
- Table 密度高但格式一致（booktabs）
- AUC 推导（Appendix P.2）应补充 empirical AUC 或 normality check