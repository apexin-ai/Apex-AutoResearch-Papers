---
round: 5
overall_score: borderline accept
timestamp: 2026-05-15T11:06:54.694367+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 5（继续审稿）

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models
**Venue**: EMNLP 2026 ARR (Main Conference)
**截止日期**: 2026-06-15
**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）
**轮次**: Round 5（修订评估 — 基于 Round 1 审稿意见的修改审查）
**上轮评分**: 2.5/5 (Weak Reject) → **本轮评分**: 3.5/5 (Borderline Accept)

---

## Summary

论文经过实质性修订：样本量从 n=50 扩展到 n=500（全部 MATH-500），所有 40+ placeholders 已填充，cross-architecture claim 从 "replicates across three models spanning two architectures" 降级为 "exploratory evidence"，标题限定为 "Mathematical Reasoning Models"，机制分析明确标注为 correlational。新增三项 robustness analyses（BH-FDR、min_phase_length sensitivity、segmentation granularity）。统计基础从 borderline adequate 提升到 strong：所有主条件 p < 10^-69 (DS) / 10^-14 (QW)，JT test 补充了 Spearman 的 n=4 局限性。

Round 1 的 5 个 critical issues 全部得到实质性回应。两位 Reviewer 独立将评分从 2.5 上调至 3.5。

---

## Round 1 Issue Resolution Status

### Critical Issues (5/5 Resolved)

| Issue | Round 1 Severity | Round 5 Status | 评估 |
|-------|-----------------|----------------|------|
| R1-N1: 40+ placeholders | Critical | **RESOLVED** | 全部填充，grep 确认零残留 |
| R1-N4: Cross-arch overclaim | Critical | **RESOLVED** | §5.5 "Exploratory"，Abstract "preliminary"，Contribution "exploratory evidence" |
| R1-N3: Single benchmark | Critical | **RESOLVED** | Title → "Mathematical Reasoning Models"；Limitations 有 MATH-500 justification |
| R1-N2: Sample size / power | Critical | **RESOLVED** | n=500，exclusion criteria (DS 4, QW 25) stated，CI width shrinkage 2.5-5.9× |
| R1-N5: Mechanism correlational | Critical | **RESOLVED** | §6 split: §6.1 discrimination collapse (robust) + §6.2 entropy (model-dependent)；"correlational" explicit |

### Warning Issues (10/11 Resolved or Partially Resolved)

| Issue | Round 5 Status | 评估 |
|-------|----------------|------|
| R2-N3: HIES differentiation | **RESOLVED** | §6.1 + Related Work 有 explicit comparison |
| R1-W1: Phase segmentation | **PARTIAL** | Sensitivity analysis 完备（mpl, quartile, quintile），但 "following ThinKV" 措辞仍在 background.tex:33 |
| R1-W2: Symmetric sparsity | **RESOLVED** | Limitations 有专门段落 |
| R1-W3: G instability | **RESOLVED** | Δ primary，G auxiliary with bootstrap CIs |
| R1-W4: Bonferroni scope | **RESOLVED** | k=4 justified，BH-FDR 44-test appendix |
| R1-W5: Spearman overinterpret | **RESOLVED** | n=4 caveat + one-tailed + JT test (z=6.2-33.7) |
| R1-W6: Exclusion criteria | **RESOLVED** | §4 complete |
| R2-W3: Missing refs | **RESOLVED** | RLKV/LongFlow/PM-KVQ all added |
| R2-W5: Abstract dense | **RESOLVED** | Rewritten, ~10 lines, structured |
| REV-ADD-2: Random threshold | **RESOLVED** | Integrated in §5.1 + cross-model |
| REV-ADD-3: Qwen mid-phase | **RESOLVED** | Reported with autocorrelation explanation |

### Info Issues (4/4 Resolved)

R2-Minor-2 (REVIEWER-ATTACK comments), R2-Minor-6 (s=0.35), R1-Minor-code (reproducibility) — all resolved. R2-Minor-1 (bib) partially resolved (h2o fixed, but LongFlow "Withdrawn" note introduced).

---

## Strengths（修订后增强）

**S1** [retained, strengthened] **研究问题有价值且定义清晰**。Phase-strategy interaction 的 characterization 对 efficient inference 部署有直接意义。n=500 的统计基础使 claim 可信。

**S2** [retained, strengthened] **统计方法论从 adequate 提升到 exemplary**。新增 BH-FDR (44 tests)、JT dose-response test、mpl sensitivity (3 settings × 16 conditions)、segmentation robustness (tercile/quartile/quintile)。Bootstrap B=10,000, seed=42, Bonferroni k=4 per family — 统计报告质量在 ML 论文中属顶尖。

**S3** [retained] **Random eviction falsification control 设计巧妙**。随机蒸发的阈值故事（s≤0.20 non-significant, s≥0.25 significant but 3-39× weaker）现已完整呈现，强化了 strategy-specificity claim。

**S4** [retained] **Crossover 发现有 deployment insight**。Strategy ranking reversal 对 uniform budget 设计直接有启示。

**S5** [new] **Honest claim scoping**。修订版在 title、abstract、contributions 中系统性地降级了 overclaimed 内容。LLaMA "exploratory"、mechanism "correlational"、scope "mathematical reasoning" — 这是修订中最难做到的部分，作者做到了。

**S6** [new] **Robustness appendix 显著提升可信度**。Table 5 (BH-FDR)、Table 6 (mpl sensitivity, 16 conditions × 3 settings)、Table 7 (segmentation, 4 sparsity × 3 schemes) — 远超多数 EMNLP submission。

**S7** [new] **Qwen mid-phase null rate 分析透彻**。lag-1 autocorrelation explanation (r=0.718 vs 0.894, d=-1.68) 不仅报告问题还解释了 root cause，展示了作者对数据的深度理解。

---

## Weaknesses（修订后残留 + 新发现）

### Should-Fix（影响评分但不阻碍接收）

**SF1** [warning, R1] **n=50 / n=500 数据混合可能误导读者**
- Table 2（per-phase II breakdown, main body §5.2）使用 n=50 profiling subset 数据
- Table 1 (§5.1) 和 Table 3 (§5.6) 使用 n=496 / n=475 数据
- Caption 标注了 "n=50 profiling subset" 并引用 Table 1 确认，但同一 Results section 混合两个 sample size 的数据易造成混淆
- crossover 分析 (§5.3 + Appendix A) 同样使用 n=50 数据（exp_id: bf16_importance_s025, bf16_ds_rand_s025）
- **建议**：将 Table 2 移至 Appendix 或在 §5.2 添加一段话明确说明 n=50 profiling 与 n=500 confirmation 的关系

**SF2** [warning, R1] **Crossover 未在 n=500 验证**
- §5.3 的策略排名反转（5.3× reversal at s=0.25）基于 n=50 per-phase II 值
- 全文 crossover 引用的 II 数值（0.032 vs 0.818, 7.196 vs 1.363）均来自 profiling subset
- Discussion §7 引用相同 crossover 数值作为 "quantitative surprise" 论据
- 如果 n=500 per-phase II 值不同，crossover magnitude 可能改变
- **建议**：在 n=500 数据上验证 crossover；或在 §5.3 标注 "profiling subset" 并 caveat

**SF3** [warning, R1-W1 residual] **"following ThinKV" 措辞仍未修正**
- background.tex:33: "following ThinKV [thinkv-iclr2026]"
- ThinKV 使用 explicit `<think>` token delimiters 分割 reasoning/non-reasoning 阶段
- 本文使用 attention sparsity quantile terciles — 方法论完全不同
- Round 1 已明确提出需修正；Round 5 sensitivity analysis 已添加但措辞未改
- **建议**：改为 "inspired by the phase distinction in ThinKV" 或直接删除 ThinKV 引用

### Minor（不影响接收决定）

**M1** [info, R2] **LongFlow bib "Withdrawn from ICLR 2026" 注释**
- 新增引用 LongFlow 的 bib entry 包含 withdrawn 标注
- 引用被撤回论文可能被审稿人视为 literature curation 不够严谨
- **建议**：确认 LongFlow 实际状态；如确实 withdrawn，移除引用或使用 arXiv preprint 形式

**M2** [info, R2] **\\placeholder 命令定义残留**
- main.tex:21 仍有 `\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}`
- 虽未使用（grep 确认无调用），但提交源码时暗示论文曾有 placeholder 结构
- **建议**：删除该行

---

## Questions for Authors

1. Table 2 的 n=50 per-phase II 数据在 n=500 上是否有变化？特别是 crossover 的 reversal magnitude（3.9×-5.4×）在 n=500 上是否一致？
2. "following ThinKV" 措辞为何未在本轮修改？是否为 oversight？
3. LongFlow 是否确实从 ICLR 2026 撤稿？如果是，是否有更合适的替代引用？
4. Oracle pilot experiment 的 gate failure (18% < 30%) 是否有后续实验计划？

---

## Missing References

Round 1 指出的 RLKV、LongFlow、PM-KVQ 均已补充。本轮未发现新的重要遗漏。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**评分: 3.5/5 (Borderline Accept)**
**置信度: 4/5**

**修订质量评估**: 本轮修订是高质量的实质性回应。5/5 critical issues resolved，10/11 warning issues resolved or partially resolved。n=50→n=500 的扩展消除了 power 疑虑，robustness analyses（BH-FDR、mpl sensitivity、segmentation）远超预期。Claim scoping（title、abstract、contributions）诚实且系统。

**残留问题严重性**: 所有残留问题均为 warning 或 info 级别：
- SF1-SF2 (n=50/n=500 混合 + crossover 未验证): 最重要的残留问题，但不改变核心 conclusion——n=500 data 已独立确认 monotonic severity gradient
- SF3 ("following ThinKV"): 措辞修正，5 分钟工作量
- M1-M2: 纯 cosmetic

**接收障碍分析**:
- **支持接收**: 研究问题有价值；n=500 统计基础强；falsification control 设计优秀；claim scoping 诚实；robustness 超越多数 EMNLP submissions
- **反对接收**: 仍是 single-benchmark (MATH-500) characterization study；mechanism 为 correlational only；crossover claim 基于 n=50 子集未在 n=500 验证
- **关键判断**: 对于以 empirical characterization 为核心贡献的论文，当前 evidence quality 达到了 EMNLP main 的门槛，但不具备显著 margin。如果 SF1-SF2 得到解决（crossover 在 n=500 上验证），评分可上调至 4/5。

**建议**:
- 如果能在投稿前完成 crossover n=500 验证、修正 "following ThinKV" 措辞、清理 LongFlow bib 和 \placeholder 残留：推荐投稿 EMNLP main
- 如果时间不允许验证 crossover：仍可投稿，但应在 §5.3 添加 "profiling subset" caveat，crossover 可能被 reviewer 追问

---

## Detailed Comments

### Per-Section Notes

**Abstract**: 修订后结构清晰，统计数字适量。"preliminary cross-architecture evidence" 措辞恰当。唯一微瑕：最后一句 "motivate phase-aware compression budgets" 略 overclaim（pilot experiment gate failed at 18%）。

**§1 Introduction**: Contribution scoping 准确。"3-39× larger" 比 Round 1 的 "absent under random" 更精确，正确反映了 threshold story。Contribution 3 "propose...as a mechanistic explanation" 恰当。

**§2 Related Work**: HIES comparison 充分。PM-KVQ temporal dimension link 是好的补充。LongFlow withdrawn status 需确认。整体 coverage 完整。

**§3 Background**: G 的 auxiliary 定位明确。"following ThinKV" 需改为 "inspired by" 或删除。公式定义清晰。

**§4 Methodology**: n=500 full dataset, exclusion criteria, CI width shrinkage, Bonferroni k=4 family justification, JT test — 统计报告质量优秀。Qwen mid-phase null 的 autocorrelation explanation 是亮点。

**§5 Results**: Table 1 (n=496) 可信且 powerful。Table 2 (n=50) 的 provenance 需更突出标注。§5.3 crossover 需 n=500 验证或 caveat。§5.4 cross-model 完整。§5.5 LLaMA exploratory 措辞恰当。§5.6 statistical validation 强。

**§6 Analysis**: §6.1 discrimination collapse 的 HIES comparison 和 random-eviction counterfactual 构成 reasonable correlational case。§6.2 entropy redistribution 诚实标注 model-dependent。"correlational; causal validation...important direction for future work" — 恰当。

**§7 Discussion**: Oracle pilot gate failure (18% < 30%) 诚实报告是加分项。Architecture-dependent magnitude 讨论平衡。Crossover 数值来自 n=50（与 SF2 同一问题）。

**Limitations**: 全面。Symmetric sparsity、mechanism correlational、sparsity range — 覆盖了主要方向。MATH-500 justification 有说服力。

**Appendix**: BH-FDR (44 tests) + mpl sensitivity (48 cells) + segmentation robustness (12 cells) — 三项 robustness 构成强有力的 supplementary evidence。Crossover appendix 和 permutation test 仍使用 n=50 数据（与主文一致但同样是潜在问题）。

**References**: 32 篇引用，新增 RLKV/LongFlow/PM-KVQ。LongFlow withdrawn status 需处理。其余引用无问题。

### Round 1 → Round 5 Score Justification

| 维度 | Round 1 | Round 5 | 变化原因 |
|------|---------|---------|----------|
| 数据完整性 | 1/5 (40+ placeholders) | 5/5 | 全部填充 |
| 统计严谨性 | 3/5 (n=50, no power) | 5/5 | n=500, BH-FDR, JT, mpl, segmentation |
| Claim scoping | 2/5 (overclaim) | 4/5 | Title/Abstract/Contribution 系统降级 |
| 机制分析 | 2/5 (causal language) | 4/5 | correlational explicit, split robust/model-dependent |
| 写作质量 | 3/5 | 4/5 | Abstract 精简, exclusion stated, HIES compared |
| 整体 | 2.5/5 | 3.5/5 | Substantial improvement |