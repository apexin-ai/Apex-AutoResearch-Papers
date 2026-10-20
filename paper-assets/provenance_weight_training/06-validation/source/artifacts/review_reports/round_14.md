---
round: 14
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-25T21:55:23.475448+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 14 审稿报告 — Provenance Weight Training (FINAL)

**论文标题**: When Does Detect-and-Reweight Work for Synthetic Contamination?
**投稿目标**: EMNLP 2026 (via ARR), Long Paper
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）
**交叉回应**: 1 轮。R1→R2: 全部 AGREE。R2→R1: 8 AGREE, 1 partial REBUT (W3), 1 full REBUT (M3)。

---

## Summary

本文通过受控 continued-pretraining 实验（Qwen3-0.6B, 132M FineWeb tokens, 5 seeds）研究 detect-and-reweight 方法在合成数据污染场景下的有效性条件。核心贡献是 epoch-matched mechanism analysis：D&R 方法 >95% 的优势来自 filtered data 的 multi-epoch exposure 而非 per-token 学习质量差异。论文还提出 dual-constrained adaptive exponent b*，无需 per-model grid search 即可改善 held-out perplexity（Δ=-0.023 at ρ=0.4）。实验覆盖 ρ ∈ {0.2, 0.3, 0.4, 0.6}、0.6B/1.7B scale、3 种 detector。

---

## Strengths

**S1. Epoch-matched mechanism analysis 是真正的学术贡献。**
通过将 D&R 的 raw PPL 优势（Δ=-0.424）与 epoch-matched control（Δ=0.017）对比，清晰分解了 multi-epoch exposure vs per-token quality 的贡献比。这一发现解释了为什么 D&R 在 continued pretraining（多 epoch）下远优于 from-scratch pretraining（通常 <1 epoch）。[R1+R2 AGREE]

**S2. 消融层次设计严谨。**
Adaptive < Uniform < ESS-only < Random < Permuted 的递进消融有效隔离了 (1) detector signal vs noise, (2) minimum intervention vs unconstrained maximization, (3) provenance signal vs weight non-uniformity 三个维度。Permuted q-scores ablation 特别巧妙——破坏样本级信息但保留权重分布形状，Δ=+0.225 的强降级清晰证明 provenance signal 是 load-bearing。[R1+R2 AGREE]

**S3. 5-seed 实验 + BH 多重比较校正。**
主实验 5 seeds + Bonferroni-Holm 校正（ρ=0.4: p_BH=0.011），cross-seed variance 极小（σ=0.006）。统计实践规范。[R1+R2 AGREE]

**S4. Calibration vs discrimination 的经验性分离。**
TF-IDF+LR (AUC=0.94, ECE=0.048) vs GPT-2 (AUC=0.91, ECE=0.131) 对比在 comparable AUC 下隔离了 calibration 效应，揭示 high-AUC but poorly-calibrated detector 反而有害（Δ=+0.098）。[R1+R2 AGREE]

**S5. Scope limitation 声明诚实。**
Introduction、Abstract 最后一句、Limitations 节均显式声明限制。Appendix Q 对 deterministic data ordering 对方差的影响也做了透明披露。[R1+R2 AGREE]

---

## Weaknesses

### Must-Fix (Critical)

**N1. Abstract 中 "ρ ≥ 0.4, reaching conventional significance" 对 ρ=0.6 构成 overclaim。** [R2 发现, R1 AGREE; 新发现]

Abstract: "improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction"。
事实核查：§5.2 报告 ρ=0.6 的 p_BH=0.064（> α=0.05），未达传统显著性。仅 ρ=0.4 的 p_BH=0.011 达标。"ρ ≥ 0.4" 暗示两个 contamination level 均显著——这是事实性错误。

> 建议：修改为 "at ρ=0.4 (p_BH=0.011)" 或注明 ρ=0.6 仅 marginal significance (p_BH=0.064)。

**N2. 标题 scope 远超实验覆盖面。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C4，连续 4 轮]

"When Does Detect-and-Reweight Work for Synthetic Contamination?" 暗示系统性评估，但实验仅覆盖：self-contamination only、0.6B+1.7B、continued pretraining（§6 自述 epoch confound 在 from-scratch 下不适用）、单一数据源 FineWeb、1 个有效 detector。

> 建议：标题加限定词，如 "...in Controlled Continued Pretraining"。

**N3. 下游任务零改善但 Abstract 未提及。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C3]

Abstract "improves over uniform training" 未限定 metric。Downstream accuracy 完全相同（0.5414 vs 0.5415）。Conclusion 写了 "without measurable downstream gains" 但 Abstract 省略。R2 在交叉回应中进一步指出：论文内部存在定位矛盾——§6 诚实承认影响有限，但 Table 5 仍以 "for practitioners" 包装。论文最有价值的贡献（D&R epoch-matching、calibration finding）本质是分析性的，不需要 practitioner framing 来体现价值。

> 建议：Abstract 明确限定 "improves held-out perplexity"，注明无下游改善。重新定位为 mechanism analysis。

**N4. Cohen's d=3.83 被 deterministic data ordering 系统性放大，关键 caveat 仅在 Appendix。** [R1 发现, R2 AGREE]

Appendix Q 承认 "seeds affect only parameter initialization, not data order"，SD_Δ=0.006 仅反映初始化噪声。Cohen's d=3.83 和 power>0.99 给读者留下 "效果极其稳健" 的印象，实际上只说明 "固定数据顺序下不同初始化产生一致结果"——远弱于 "方法在不同条件下稳健有效"。Uniform baseline 也有类似低方差（σ=0.008），确认窄方差是实验设定属性而非方法特性。此 caveat 应在 §5.1 主文而非仅 appendix 中。

> 建议：在 §5.1 加入 Cohen's d 的 deterministic ordering caveat。补充 Wilcoxon signed-rank test 作为 robustness check。

### Should-Fix (Warning)

**W1. "Three effectiveness conditions" framing 过度概括。** [R2 发现, R1 AGREE]

Abstract/Figure 1/Conclusion 使用 "conditions" 暗示充分必要条件，但 evidence 仅支持 empirical observations。Introduction 使用 "three findings"，术语自身不一致。

> 建议：统一使用 "three empirical findings" 或 "three observed requirements"。

**W2. Δ=-0.023 PPL 缺乏 baseline contextualization。** [R2 发现, R1 AGREE]

论文未在 continued pretraining 文献中定位 0.023 PPL（0.13% relative）的量级含义。缺少与其他 data curation 方法（DSIR, DsDm, DoReMi）的量级对比。

**W3. Related Work 遗漏 detection benchmarks。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-W3]

缺 RAID (Dugan et al., 2024)、M4 (Wang et al., 2024)。自 Round 13 起被要求补充，仍缺失。

**W4. Table 5 decision framework 基于 3 个 detector，实用性受限。** [R1+R2 AGREE; 跨轮次 recurring R12-W1]

AUC ≥ 0.9 / ECE ≤ 0.05 threshold 仅 3 个数据点，缺少 neural detectors。AUC=0.88, ECE=0.04 区间无 empirical support。

**W5. §6 Discussion 第一段与 §5.1 高度重复。** [R2 发现, R1 AGREE; recurring R13-m1]

§6 开头重述 epoch-matched analysis 全部内容，8 页限制下应精简。

**W6. 缺 uniform × 3.2 epochs baseline，epoch confound 分析不完整。** [R1 发现, R2 AGREE; 跨轮次 recurring R11-W4]

R2 在交叉回应中进一步论证：此 baseline 可区分两个假说——(a) D&R 优势来自 filtering quality（去除坏数据）vs (b) 单纯来自 repetition（多看数据本身有帮助即使含 synthetic）。如果 uniform × 3.2 epochs 也大幅改善 PPL，D&R 的 "filtering" 叙事需修正。计算成本低。

**W7. 1.7B 规模效应递减 43%，scaling trend 未正式讨论。** [R1 发现, R2 AGREE; recurring R13-W3]

R2 补充：论文解释（"larger models more robust to self-generated contamination"）合理但暗示结构性局限——效果依赖 generator-trainee mismatch，而 self-contamination 中 mismatch 随模型增大缩小，方法 inherently limited。

**W8. ρ≥0.4 实用门槛偏高，实际适用场景极窄。** [R2 发现, R1 AGREE; recurring R13-W4]

多条件交集极窄。"Decision summary for practitioners" 可能给读者不准确的 generalizability 信号。

**W9. Temperature scaling T=0.204 依赖 labeled data，限制 deployability。** [R2 发现, R1 AGREE]

Detector calibration 依赖 10K labeled validation split。Web-scale pretraining 中 ground-truth synthetic labels 不可用。

**W10. 1.7B 实验选择 τ=0.8 而非推荐的 τ=0.7，构成 confound。** [R2 交叉回应新发现]

§5.2 报告 1.7B 使用 τ=0.8 但未解释选择理由。0.6B 主结果推荐 τ=0.7（§5.3 Table 6 明确显示 τ=0.7 在 holdout 和 OOD 上均优于 τ=0.8）。1.7B 用 τ=0.8 导致无法区分效应减弱是因为 scale 还是因为 suboptimal τ——这是一个实验设计 confound。

> 建议：解释 τ=0.8 选择理由，或补充 1.7B + τ=0.7 实验。

### Minor Issues

**M1. Table 1 caption 声明 5-seed mean 但仅展示 3 个 seed 列。** [R2 发现, R1 AGREE]
Seeds 789/234 个体结果不可见，可能引发选择性报告疑虑。

**M2. §5.2 与 Appendix I 的 t 值不一致（t=-9.95 vs t=-15.4）。** [R2 发现, R1 AGREE]

**M3. "Three effectiveness conditions" vs "three findings" 术语全文不一致。** [R2 发现, R1 AGREE]

**M4. Appendix P Table 16 seed 456 缺 OOD 评估。** [R2 发现, R1 AGREE]

**M5. Sliding-window evaluation 未说明 window size 和 stride。** [R2 发现, R1 AGREE]

---

## Reviewer Consensus

两位 Reviewer 在核心判断上完全一致：

1. **论文应定位为 mechanism analysis paper**，而非 practitioner-oriented method paper
2. **Abstract overclaim** 必须修正（p-value + downstream null）
3. **标题需限定 scope**（连续 4 轮 recurring）
4. **Epoch-matched analysis 是论文的核心价值**
5. **Overall 3.0 (Findings)**, Soundness 3.5, Excitement 2.5——两人独立得出完全相同评分

交叉验证关系：
- R2-N3 ≈ R1-N1（effect size vs framing 矛盾）
- R2-N2 ≈ R1-W4+W5（scope 限制）
- R2-W4 ≈ R1-W4（detector threshold 通用性）
- R2-Q3 ≈ R1-M1（batch size 限制）

R2 额外贡献：N1（p_BH=0.064 overclaim，R1 遗漏）、W3（missing references）、M2（t 值不一致）、W10/Q5（1.7B τ=0.8 confound）。

---

## Reviewer Divergence

两处分歧，均为 minor：

**1. R1-W3: Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差** — R2 partial REBUT

- R1 原始主张："违背 minimum intervention 原则"
- R2 反驳要点：(a) 比较框架不对等——grid b=0.3 是全局固定值而 mean b*≈0.9 含 per-batch 波动（0~5 range, Figure 10, 5.8% clean batches b*=0）；(b) gap 部分来自 grid-search 的 post-hoc oracle advantage（cross-seed SD=0.035 = adaptive 的 6×）；(c) 但核心 concern 成立——α_eff negative bias ≈-0.03 确实系统推高 b*，是结构性缺陷
- **圆桌裁定**：观察有效，措辞调整。采纳 R2 更精确的表述：**"α_eff 的 systematic underestimation 导致 adaptive 方法未能完全实现 minimum intervention，有改进空间（如 bias correction）"**。不影响评分。

**2. R1-M3: Abstract word count 接近 200-word 限制** — R2 full REBUT

- R1 原始主张：abstract 接近 200-word 限制
- R2 反驳：实际约 171 words，距限制有 ~15% 余量（~29 words），不构成 weakness
- **圆桌裁定**：采纳 R2 的事实更正。Abstract word count 合规，不列入报告 weaknesses。

---

## Questions

**Q1. Adaptive reweighting 的实际 use case。** [R2 提出, R1 AGREE]
D&R (q>0.3) PPL 17.250 大幅优于 adaptive (17.674)。如果 D&R 在所有设定下都优于 adaptive，后者的 use case 是什么？

**Q2. Temperature scaling T=0.204 在无标注数据下的替代方案。** [R2 提出, R1 AGREE]

**Q3. B=4 micro-batch size 的代表性。** [R2 提出, R1 AGREE; recurring R13-W1]
Modern pretraining B=32-128。§5.3 B=4→16 amplification 3.0× 但 B=16 仍远低于实际。

**Q4. α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例。** [R1 提出, R2 AGREE]
可从现有数据（Appendix J, Table 12: MAE=0.114, bias=-0.03）直接计算。

**Q5. 1.7B 实验选择 τ=0.8 而非 τ=0.7 的理由。** [R2 交叉回应新发现]
0.6B 推荐 τ=0.7（holdout+OOD 均优），1.7B 却用 τ=0.8，创造 confound。

**Q6. Calibration-corrected α_eff 能否缩小 b* vs grid-optimal 的 gap？** [R1 提出, R2 AGREE]
用 +0.03 offset 调整 α_eff → b_τ 降低 → mean b* 可能从 0.9 降至更接近 grid-optimal 的 0.3-0.5 range。建设性改进方向。

---

## Missing References

1. **RAID** (Dugan et al., 2024) — AI-generated text detection benchmark
2. **M4** (Wang et al., 2024) — 多语言 machine-generated text detection
3. **MATES** (Yu et al., 2024) — training-time data selection（如相关）
4. **Aioli** (Balachandran et al., 2024) — data mixing（如相关）

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求 (not_requested)

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成 (2026-05-25 21:16–21:19, ~2.5 min)
**统计**: 0 critical, 1 warning, 12 info

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | Page 8 | Figure 8 stacked bar chart 5+ 颜色类别，灰度打印下相邻色段难以区分。建议增加纹理填充 |
| ℹ️ info | Page 1 | 首页无 display item，Figure 1 在 page 2 顶部 |
| ℹ️ info | Page 2 | Figure 1 legend 字号偏小（约正文 55-60%）|
| ℹ️ info | Page 3 | Figure 2 仅单栏，建议 figure*（全宽）|
| ℹ️ info | Page 7 | Display item 密度最高（Table 3+4 + Figure 7），略拥挤 |
| ℹ️ info | Page 8 | 主文正好 8 页，符合 EMNLP 2026 限制 ✓ |
| ℹ️ info | Page 9 | Limitations 简洁合规 ✓。References 无 [?] ✓ |
| ℹ️ info | Page 12 | Figure 10 axis label 字号偏小 |
| ℹ️ info | Page 15 | AI Assistants 声明 ✓ |

---

## Overall Assessment

| 维度 | 评分 | 说明 |
|------|------|------|
| **Overall** | **3.0 — Findings** | 分析贡献（epoch-matched mechanism）有学术价值，但 framing 系统性超出 evidence，实际效果量级不足以支撑 practitioner 定位 |
| **Soundness** | **3.5** | 实验设计严谨（5 seeds, BH correction, 层次消融），但 scope 限制 + p-value overclaim + τ=0.8 confound 削弱可信度 |
| **Excitement** | **2.5** | Epoch-matched analysis 有新意，但 Δ=-0.023 PPL (0.13%) 无下游改善，practical impact 有限 |
| **Confidence** | **4 — High** | 两位 Reviewer 独立得出一致评分，交叉回应近完全共识（仅 1 个 minor framing 分歧 + 1 个事实更正）|

**核心判断**: 论文的学术贡献在于 epoch-matched mechanism analysis——解释 D&R 为何在 continued pretraining 中有效。这一发现值得发表。但存在三层 framing 偏差：

1. **Abstract 事实性错误**：ρ=0.6 p_BH=0.064 未达显著性，Abstract overclaims
2. **标题-实验 scope gap**：标题暗示通用性，实验仅覆盖极窄场景
3. **Practitioner framing 与 evidence 矛盾**：Δ=-0.023 PPL 无下游改善、1.7B 递减 43%（且存在 τ=0.8 confound）、ρ<0.4 失效

此外，两个缺失的实验 baseline 影响分析完整性：uniform × 3.2 epochs（区分 filtering vs repetition）和 1.7B + τ=0.7（区分 scale vs hyperparameter effect）。

**建议接收路径**: 修正 Abstract overclaim + 标题 scope 限定 + 重新定位为 mechanism analysis + 补充 uniform × multi-epoch baseline → Findings 发表。

---

## Detailed Comments

### §1 Introduction
- "three findings"（正确）与 Abstract/Conclusion 的 "three conditions"（过强）不一致
- Scope 声明合理，但标题未反映限制
- "illustrative application" 定位改善了方法预期

### §2 Related Work
- 缺 RAID 和 M4 detection benchmarks
- Drayson et al. 对比清晰（3 点差异），但 ModernBERT-150M 未测试

### §3 Method
- 方法新颖性有限但论文已改善定位
- "motivated by convergence theory (Wang 2026)" 仍暗示理论保证，而 α_eff proxy R²≈0.63 + negative bias -0.03 意味理论前提不完全满足

### §4 Experimental Setup
- Sliding-window evaluation 缺 window size 参数
- Temperature scaling 依赖 labeled data 未讨论
- 1.7B 选择 τ=0.8 而非 τ=0.7 缺乏 justification，构成 confound

### §5 Results
- §5.1: 消融严谨。Table 1 显示 3 seeds 而 caption 说 5-seed mean。Permuted 仅 seed-42
- §5.2: ρ=0.6 p_BH=0.064 正文正确报告为 directional，但 Abstract overclaims
- §5.2: 1.7B Δ=-0.013 仅一段，未正式 scaling analysis。τ=0.8 confound 未讨论
- §5.2: t=-9.95 vs Appendix I t=-15.4 不一致
- §5.3: B=4/8/16 monotonic trend 清晰。B=16 仍远低于实际
- Cohen's d=3.83 的 deterministic ordering caveat 应从 Appendix Q 提升到 §5.1 主文。建议补充 Wilcoxon signed-rank test

### §6 Discussion
- 第一段与 §5.1 重复，应精简
- Table 5 + "conditions" 仍过强
- Effect size 段诚实但缺 baseline contextualization
- α_eff limitations 段坦诚且必要。R2 补充：negative bias → conservative intervention → 解释 b*≈0.9 偏高。可探索 bias correction (+0.03) 改进

### §7 Conclusion
- "without measurable downstream gains" 比 Abstract 诚实，恰恰暴露 Abstract framing gap

### Limitations
- 三点合规

### Appendix
- Table 16 seed 456 缺 OOD
- Appendix Q 对 deterministic ordering 的透明度好，但 caveat 应在主文

---

**审稿圆桌**: R1 × R2, 1 轮初审 + 1 轮交叉回应, 近完全共识（1 minor framing 分歧 + 1 事实更正）
**Issue Tracker**: 已同步更新至 review_issues.yaml（Round 14, 含 R14-W2 τ=0.8 confound）