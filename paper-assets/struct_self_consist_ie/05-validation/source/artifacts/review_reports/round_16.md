---
round: 16
overall_score: borderline
timestamp: 2026-05-17T06:42:06.978332+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 16 审稿报告 — Consolidated Review

**论文**: "Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction"
**目标 Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验+统计方法论; R2: 新颖性+贡献定位+相关工作+写作质量）
**圆桌流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断（1 轮收敛）

---

## Summary

论文评估 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 LLM-based NER 中的质量估计与样本选择能力，在 4 个 benchmark 上（SciERC primary, CoNLL ceiling, Few-NERD low-degeneracy, WNUT collapse）使用 Qwen3-8B/LLaMA-3.1-8B/4B ablation。核心发现：信号可有效预测实例级质量（ρ up to 0.38-0.42），但无法有效选择 best-of-N 候选。诊断两个机制：instance degeneracy（10-58%）和 LP compression（median range 0.041 nats）。论文系统性强、诊断链完整、统计透明度高，但存在 framing 混淆、数值不一致和统计效力不足的关键问题。

---

## Strengths

**S1. 系统性实验设计** [Both AGREE]
4 个 benchmark 形成 difficulty gradient，2 模型族 + 4B scale ablation + LoRA-rank ablation 提供多层证据。覆盖面在同类论文中属上乘。

**S2. 诊断链深度** [Both AGREE, 最强贡献]
从"gap exists"到"why it exists"的五层 ablation：instance degeneracy 量化 → LoRA-rank 解耦 → free-form decoding 排除 constrained decoding → entity-token LP 排除 format dilution → supervised combination 确认 feature space bottleneck。Within-instance analysis（non-degenerate ρ=0.52, MBR closes 23-41% oracle gap）证明 failure 来自 headroom vanishing 而非 utility misalignment。

**S3. Negative result 实践意义** [Both AGREE]
对 NER practitioners actionable：不要在 fine-tuned 高性能模型上指望 self-consistency 做 selection；QE 用于 selective prediction/error flagging 是可行方向。

**S4. 统计透明度** [Both AGREE]
对 post-hoc 分析（ε=0.05）、thinking token confound、gold-filtering 方法论、configuration-dependent TOST 结果的主动披露达到高标准。Limitations 诚实详尽。

**S5. Few-NERD 对照实验** [Both AGREE]
利用 degeneracy 差异（58%→21%→10%）形成跨 dataset 自然实验，LP selection 在低 degeneracy 下有效（+1.36pp, p<0.001），增强了 degeneracy 作为解释变量的可信度。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [强共识] Framing 混淆 definitional limitation 与 empirical finding**
- R2-N1 (critical) + R1 AGREE
- 4/5 信号（SJ, VC, FK, EM）是 instance-level，by construction 对同一 input 所有候选给出相同分数。标题"Strong Predictors, Weak Selectors"暗示这是意外发现，但 instance-level signals 的"weakness"部分来自定义而非实验。
- 真正的 empirical findings：(a) MBR conversion with positive within-instance ρ=0.52 仍失败（因 degeneracy），(b) LP per-sample but compressed。论文需明确分三层：definitional → MBR empirical → LP empirical。
- **历史**：自 Round 3 (R3-W2) 首次提出，持续 14 轮未完全解决。

**MF2. [强共识] ρ=0.42 headline 数值在论文内部矛盾**
- R2-N2 (critical) + R1 独立验证 AGREE
- Abstract/Figure 1 caption 声称"ρ up to 0.42 on primary test bed"，但 Table 1 SciERC（declared primary）最高 ρ = VC 0.379。ρ=0.42 实际来自 Few-NERD LP (0.421)。Contribution 1 正确写"ρ=0.38"。差 0.04，非四舍五入误差。
- 影响论文可信度——审稿人会视为 cherry-picking 或粗心。

**MF3. [强共识] 2-seed sign test 统计效力不足以支撑核心否定结论**
- R1-N1 (critical) + R2 AGREE
- "no signal significantly outperforms greedy"基于 2-seed paired sign test，effect size 仅 +0.2pp 下 power 极低。R2 补充：N=32 时 paired bootstrap 得 LP +0.95pp, p=0.031，实际上反驳了论文自身的"selection fails"叙事。Few-NERD 用 paired bootstrap 但 SciERC 用 sign test，方法不统一。
- 共识修改：从"no signal significantly outperforms"改为"effect is small and not reliably detected with current sample size"；统一使用 paired bootstrap。

**MF4. [强共识] Degeneracy-gating monotonic claim 仅 3 dataset-level 数据点，统计不显著**
- R1-N2 (critical) + R2 AGREE
- 任意 3 个不同值必然可排出 monotonic order。Figure 3 Spearman ρ=−0.57, p=0.066 (n=11) 未达 α=0.05。
- R2 补充缓解证据：per-entity-type 分析 (n=8, ρ=−0.881, p=0.004) 在 controlled within-dataset setting 更有力。但混合粒度（3 dataset + 8 entity-type）可能违反 independence。
- 共识："monotonically predicts"降级为"is inversely associated with"或"is consistent with a monotonic relationship"。

**MF5. [强共识] 与 MBR 社区已知结论的增量需更清晰 articulate**
- R2-N3 (critical) + R1 AGREE
- Eikema et al. (2025) 已讨论 MBR utilities degrade on structured outputs。本文真正增量：即使 utility IS aligned (ρ=0.52)，degeneracy 也 eliminate headroom——这与 Eikema 的"utility misalignment"解释形成 complementary diagnosis。
- R1 补充：NER 离散标签空间导致比 MT/summarization 更极端的 degeneracy，这个 structural argument 也应强调。
- Related Work 需明确 differentiation paragraph。

### Should-Fix（影响评分但不一票否决）

**SF1. [强共识] Random (0.610) vs Greedy/Single (0.645) 的 3.5pp 差距未解释**
- R1-W1 + R2 AGREE
- E[Random]=E[Single] under T=1.0 应相同。3.5pp 系统性差距需澄清精确计算方式和 temperature-quality tradeoff 的影响。

**SF2. [强共识] Abstract 信息过载**
- R2-W4 + R1 AGREE
- 9 句话塞入 5 signals、4 benchmarks、degeneracy%、LP nats、p-values 等，远超审稿人 30 秒吸收能力。数字压缩到 3-4 个最关键的。

**SF3. [强共识] Kendall's W=1.0 with 3 seeds 需 precision caveat**
- R1-W2 + R2 AGREE
- m=3, k=5，exact p≈0.028，有意义但不如论文暗示的 definitive。

**SF4. [强共识] Gold-empty instance filtering protocol 不一致**
- R1-W5 + R2 AGREE
- Table 4 SciERC (n=551, greedy=0.614) vs Table 2 (n=529, greedy=0.645)。LP Δ 从 +0.2pp 到 +0.42pp。需统一 protocol 或同时报告两版本。

**SF5. [强共识] TOST configuration-dependent 呈现不平衡**
- R1-W4 + R2 AGREE
- Qwen-CoNLL 下 selection actively degrades (0.9-1.5pp)，这比"no benefit"更强的结论被淡化在 Appendix。

**SF6. [强共识] "Correlation-selection gap" 操作性定义位置太晚**
- R2-W5 + R1 AGREE
- 术语从 Abstract 使用，Section 4.3 才正式定义。Introduction 首次使用时需给出 one-sentence operational definition。

**SF7. [强共识] 与 Yao et al. (2026) 差异化不足**
- R2-W3 + R1 AGREE
- 核心增量不仅是 fine-tuned vs hard-prompted，更是"why QE ≠ selection"的诊断。需更直接的对比句。

**SF8. [强共识] Soft Jaccard 命名误导**
- R2-W2 + R1 AGREE
- 分母用 max 而非 union，不是标准 Jaccard。改名或加注释。

**SF9. [强共识] Scale claims 措辞需澄清**
- R2-W6 + R1 PARTIAL REBUT
- 标题"Fail to Scale"暗示 model scale，实测仅 4B-8B。R1 反驳：论文中"scale"指 N/信号复杂度。共识：Abstract 中需澄清"scale"具体含义。

### Reviewer Divergence（分歧）

**D1. Bonferroni scope（R1-N3）: R1 判 critical, R2 降为 should-fix**
- R1：7ε × 5 signals = 35 comparisons → p_adj=0.14，不再显著。
- R2 反驳：(1) Limitations 已承认 post-hoc；(2) ε 值嵌套（非独立），Bonferroni 过保守；(3) median LP range=0.041 提供 a priori 动机；(4) non-tied analysis 定位为 diagnostic 非 prescriptive。
- 共识：Footnote 4 措辞需修正（"conditional on pre-selected ε"），但是否为 must-fix 有分歧。
- **Director 判定：Should-Fix**。R2 的论证成立——嵌套比较下 Bonferroni 过保守，且论文已在 Limitations 中正确 acknowledge。但 footnote 4 必须修正措辞。

**D2. 8B vs 4B degeneracy: capability vs recipe confound（R1-W3 vs R2 REBUT）**
- R1：same training recipe, 更大模型可能 overfit 更快。
- R2：LoRA-rank ablation 是 interventional evidence（同一 8B 模型 rank 32→21%, rank 8→7%），已控制此 confound。
- **Director 判定：R2 的反驳有力**。LoRA-rank ablation 作为 interventional evidence 比 observational 8B/4B 对比更强。但论文应明确区分两者的证据权重。

---

## Questions for Authors

1. **ρ=0.42 归属**：Figure 1 caption "ρ up to 0.42 on primary test bed" 具体来自哪个 configuration？Table 1 SciERC max = 0.379，与此矛盾。
2. **Sign test power**：在 effect size d=0.038、n=529 下，sign test 的 power 是多少？为什么 SciERC 用 sign test 但 Few-NERD 用 paired bootstrap？
3. **LP compression vs degeneracy hierarchy**：LoRA rank=8 降低 degeneracy 到 7% 但 LP selection 仍失败。这是否暗示 LP compression 是独立于 degeneracy 的 more fundamental bottleneck？为何 Discussion 仍将 degeneracy 作为 primary diagnosis？
4. **Few-NERD degeneracy confound**：低 degeneracy (10%) 可能由 dataset 特性（entity types 多样性、semantic overlap）而非 model capability 决定。仅 3 个 dataset-level data points 无法排除此 confound。如增加 entity-type-level 的 formal test，结论是否 robust？
5. **Random vs Single 定义**：两者的精确计算方式是什么？E[Random]=E[Single] under T=1.0，3.5pp 系统性差距来源何在？
6. **70B+ extrapolation**：如果 degeneracy 随 fine-tuning capacity 增加，70B+ 模型是否更严重？还是存在 non-monotonic 可能？

---

## Missing References

**两位 Reviewer 共同建议补充：**
- Xu et al. (2024) — Rejection/selective prediction 与 NER 交叉
- Li et al. (2024) — LLM confidence estimation for structured outputs

**R1 建议：**
- Freitag et al. (2023) "Results of WMT23 Metrics Shared Task" — MBR 最新成果
- Derczynski et al. (2016) — NER 评估方法论

**R2 建议：**
- Wan et al. (2023) "GPT-RE" — LLM-based RE direct competitor
- Xu et al. (2024) "Large Language Models for Generative Information Extraction: A Survey"
- Bertsch et al. (2024) "In-Context Learning with Long-Context Models"

当前 58 个引用偏少（EMNLP 长文 typical 50-70），2025-2026 generative NER/IE survey 方向可补充。

---

## External Review

**外部审稿（Stanford Agentic Reviewer）：未请求。**

---

## Overall Assessment

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 3.0 | 3.0 |
| Reproducibility | 4.0 | — | 4.0 |
| Overall | 3.5 | 3.0 | **3.25 (borderline Findings/Conference)** |

**Overall Score: 3.25/5 — Borderline (Findings track, conditionally upgradeable to Conference)**

**共识判断：** 实验设计和诊断链是论文的明显优势，negative result 对 NER 社区有实践价值。但论文存在四个关键瓶颈：

1. **Framing（14 轮未解决）**：definitional vs empirical contribution 仍混淆
2. **数值一致性**：ρ=0.42 归属错误直接损害可信度
3. **统计基础**：核心否定结论依赖 under-powered sign test；核心 mechanistic claim（monotonic gating）统计不显著
4. **Novelty positioning**：与 MBR 文献的增量未清晰 articulate

**修复路径：**
- 如果 MF1-MF5 全部修复（framing 分层 + 数值统一 + bootstrap 替代 sign test + monotonic 降级 + MBR differentiation），论文可升至 3.5-4.0（Conference track）
- 如果仅修复 MF2（数值一致性）和 MF3/MF4（统计表述弱化），论文适合 Findings track
- 如果 MF1（framing）在 16 轮后仍不能解决，论文将难以获得正面推荐

**Recommendation: Findings acceptance with major revisions required for Conference consideration.**

---

## Detailed Comments

### Section-by-Section

**Abstract**: 信息过载（SF2）+ 数值矛盾（MF2）+ "scale"含义不明（SF9）。需大幅精简数字，统一 ρ 归属，澄清 scale 含义。

**Introduction**: Gap 的 tautological framing 是最严重问题（MF1）。操作性定义缺失（SF6）。Contribution list 需分层。

**Section 3 (Method)**: §3.1 有 instance-level/per-sample 区分但未向 Abstract/Intro 传递。Soft Jaccard 命名（SF8）。

**Section 4 (Results)**: Sign test power 不足（MF3）。Table 2 与 Table 4 的 protocol 不一致（SF4）。Footnote 4 Bonferroni scope 措辞（D1）。Monotonic claim 过强（MF4）。

**Section 5 (Discussion)**: Degeneracy 作为 primary diagnosis 的合理性（Q3）。与 Eikema et al. 的区分不足（MF5）。8B vs 4B 证据权重需调整（D2）。

**Related Work**: 与 Yao et al. 差异化不足（SF7）。MBR differentiation paragraph 缺失（MF5）。

**Limitations**: 已承认多个关键 caveats（ε post-hoc, seed 数量, scale range），质量高。但部分 caveats 与主文表述不一致（如 footnote 4 vs Limitations on ε）。

**Appendix**: 质量极高。16+ sections 提供全面补充分析。但 appendix 质量不能弥补主文 framing 和统计问题。