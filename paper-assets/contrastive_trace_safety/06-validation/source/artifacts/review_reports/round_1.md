---
round: 1
overall_score: weak accept
timestamp: 2026-05-17T04:34:57.654851+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿圆桌会议报告 — Round 2

**论文**: "Temporal Probing for Safety Commitment Detection in Reasoning Models"
**Venue**: EMNLP 2026 ARR (May cycle, deadline 2026-05-25)
**审稿人**: R1 (Methods & Experimental Soundness), R2 (Novelty & Writing Quality)
**日期**: 2026-05-17
**外部审稿**: 未请求（项目无 external_review 配置）

---

## Overall Assessment

**评分**: 3.25/5 (Weak Accept — Findings track acceptable, Main conference borderline)

**置信度**: 高（两位 Reviewer 评分接近 [3.5 vs 3.0]，关键问题高度收敛）

Round 1 的所有 critical issues (C1-C7) 和绝大多数 should-fix issues 已解决。论文经历了实质性修改：标题/framing 完全重写、补充 Control Task、Related Work 扩展为 6 段 32 引用、统计方法改为 per-model reporting + Bonferroni。**当前版本质量显著优于 Round 1。**

剩余问题分两类：
1. **可修复 critical issues (2个)**：多重比较校正需补充论证 (R2-W1)、transfer 方法需补充实现细节 (R2-W2)
2. **结构性限制 (不可在 rebuttal 中完全解决)**：statistical power 不足 (n≈20 for 32B)、architecture/scale/distillation 三重 confound、novelty ceiling (纯 empirical study)

修复 2 个 critical issues 后达 **Findings track** 标准。Main conference 需要更大数据集或 methodological contribution。

---

## Summary

论文系统比较了 hidden-state probes 与 text monitors 在 reasoning model safety commitment detection 上的表现，涵盖 3 个模型 (DeepSeek-R1 8B/32B, QwQ-32B)、2 种架构、2 种模态。核心发现：(1) temporal context（观察窗口 W=1→25）对检测的贡献大于模态选择（precision +12.9pp vs modality gap 0-7pp）；(2) HS probe 优势仅在 R1-8B 统计显著 (p<0.001 Bonferroni-corrected)，32B 模型无法确认；(3) TrajGuard/BOCPD/cross-transfer 全部失效，定义了方法边界。

---

## Strengths

1. **Round 1 issues 全面修复。** 7 个 Round 1 critical issues 全部 resolved，12 个 should-fix issues 中 10 个 resolved。论文展示了高效的修订能力。

2. **"Temporal > modality" 的核心 finding 有完整证据链。** Table 2 (HS window) + Appendix Table 3 (full sweep) + Appendix Table 4 (text window) 三重验证。Text probes 从 temporal context 获益更大 (+12.0pp vs +3.2pp) 进一步支撑 "bottleneck is temporal" 论点。

3. **统计方法规范且透明。** Paired permutation test + Bonferroni + per-seed breakdowns + control tasks (Hewitt framework) + 诚实报告非显著结果。R1-8B 的 Pareto dominance 结论在 3/3 指标上成立（precision p<0.001, accuracy p=0.005, FPR p=0.044）。

4. **Negative results 有独立信息价值。** TrajGuard Mahalanobis 失效 (d=6.64-6.73 indistinguishable)、BOCPD coverage-timing tradeoff (93% detection but +3.5 steps vs threshold +4.9)、cross-transfer 全方向失败——为后续研究节省探索成本。

5. **Bug disclosure (Appendix F) 和 Limitations 的坦率程度罕见。** 主动披露 M002 bug、承认 safe trace FPR 39-62%、承认 power 不足、承认 confound。

6. **Related Work 组织清晰，positioning 明确。** 6 段主题式结构 (Probing / Causal / HS Safety / Reasoning Safety / PRM / Cross-Model)，每段末尾定位本文贡献。

---

## Weaknesses（按严重程度排序）

### Critical Issues（需修复）

**W1. 多重比较校正不完整 [R1提出, R2同意]**
- 问题：Bonferroni 只校正 3 models (α=0.017)，但每模型内测试 3 metrics (accuracy, precision, FPR)，总计 9 次假设检验。完整校正应 α=0.0056。R1-8B accuracy p=0.005 在此标准下为边际。
- 影响：R1-8B precision p<0.001 仍通过任何合理校正，核心 claim 不倒塌。但论文需要显式论证为何不校正指标数。
- 修复建议：Section 3.2 增加 "metrics 非独立性" 论证（报告 metric 间 Pearson correlation），或改用 Holm-Bonferroni/FDR。

**W2. Cross-model transfer 实现完全缺失 [R1提出, R2完全同意]**
- 问题：Section 5.6 仅 3 行描述 "PCA alignment"。缺少：PCA components 数/选择标准、对齐方法 (Procrustes/CCA?)、4096 vs 5120 维度映射、是否尝试替代方案、projection 训练数据来源。
- 影响：作为 Contribution 3 ("comprehensive negative results") 的核心支撑之一，reproducibility 为零。"Transfer fails" 可能只是方法太弱而非表征真的 model-specific。
- 修复建议：Appendix 补充完整算法流程及所有超参数。

### Warning Issues

**W3. Statistical power 不足使 Contribution 2 standing on weak ground [R1-R2 完全共识]**
- 32B 模型 n=19-20，Cohen's d<0.5 不可检测。"Model-dependent" 与 "underpowered" 无法区分。
- Abstract/Introduction 仍将此作为正面贡献宣传，存在 overclaim 风险。
- 建议：Contribution 2 qualify 为 "tentative evidence on 32B; definitive on R1-8B"。

**W4. QwQ-32B position baseline > HS probe 对核心 claim 的冲击 [R1-R2 共识]**
- Position baseline 70.6% > HS probe 67.8% (Section 5.4)。Layer 2 (3.1% depth) 可能主要编码 positional features。
- Temporal windowing 收益可能部分因提供更多位置信息而非 genuine temporal dynamics。
- 建议：Discussion 增加 "position vs temporal dynamics" 区分讨论；考虑 residual probe 实验。

**W5. Architecture/scale/distillation 三重 confound [R2提出, R1同意]**
- R1-8B 是唯一 Llama/8B/distilled model。HS 优势来源无法 disentangle。
- Discussion 猜测 "distillation compresses safety signal" 但无证据。
- 建议：独立段落系统讨论 alternative explanations + disambiguation 方案。

**W6. Excluded traces (10/43 = 23%) 缺特征分析 [R1-R2 共识]**
- Precision 比较排除了"双方均无正预测"的 traces，实际仅基于 n=33。
- 排除逻辑自洽但需数据验证排除非系统性偏差。

**W7. Multi-layer GRU per-seed 数据缺失 [R1-R2 共识]**
- Main text "best result" (+4.5±3.0) 来自 multi-layer，但 Appendix 只有 single-layer per-seed。

**W8. Novelty ceiling: 纯 empirical study [R2提出, R1部分 rebut]**
- 三个贡献均为 empirical observations，无新方法/新理论/新数据集。
- R1 认为新任务定义 (CP detection + metric 体系) + systematic negative results 有独立贡献价值。
- **此为两位 Reviewer 主要分歧点**：R1 认为支持 borderline main, R2 认为仅支持 Findings。

### Info Issues

**W9.** Abstract 过长 (~280 words, 堆砌 10+ 个 p 值/pp 数字)
**W10.** "Deployment recommendations" 段落标题与 safe trace FPR 39-62% 存在 tension
**W11.** Discussion/Conclusion 与 Section 5 重复 ~0.5 page
**W12.** CP annotation IAA 未报告（HarmThoughts 数据集自身局限）
**W13.** R1-32B non-monotonic window 归因 "overfitting" ���验证
**W14.** Text encoder 选择 (MiniLM 384d) 可能 artificially 扩大 modality gap

---

## Reviewer Consensus [AGREE]

1. **Transfer 方法不可复现** — 两位 Reviewer 完全共识，均标为 critical
2. **Statistical power 削弱 Contribution 2** — 完全共识
3. **Position confound 在 QwQ-32B 上的冲击** — 完全共识
4. **多重比较校正需补充论证** — 完全共识（但同意核心 claim 不倒塌）
5. **Round 1 所有 critical issues 已修复** — 完全共识
6. **论文整体质量显著提升** — 完全共识
7. **适合 Findings track** — 完全共识

## Reviewer Divergence [REBUT areas]

1. **Novelty 评价**：R1 (3.5/5) 认为新任务定义 + negative results 有独立贡献，接近 main conference 下界；R2 (3.0/5) 认为纯 empirical 无 methodological contribution，仅支持 Findings。
2. **Deployment framing**：R2 认为 FPR 39-62% 与 deployment 措辞矛盾；R1 认为论文已在 Limitations 充分 qualify。
3. **Excluded traces severity**：R1 标 warning, R2 认为 info（排除逻辑自洽）。

---

## Questions to Authors（需在 rebuttal 中回答）

1. **多重比较论证**：为何 Bonferroni 只校正模型数不校正指标数？请提供 metrics 间 correlation 估计，或改用 FDR。
2. **Transfer 实现细节**：PCA alignment 的完整算法流程？Components 数？维度对齐方法？是否尝试 Procrustes/CCA？
3. **Excluded traces 特征**：被排除 10 条 traces 的长度和 CP 位置是否与其余有统计差异？
4. **Position vs temporal dynamics**：QwQ-32B 上 position baseline > HS probe，是否考虑 residual probe 验证？
5. **Text encoder sensitivity**：如果用更强 encoder (E5-large, 1024d)，modality gap 是否缩小？
6. **K=5 oracle 选择依据**：为何 oracle 用 K=5 而非 K=1？

---

## Missing References

两位 Reviewer 未指出明显遗漏引用。Round 1 的引用缺失问题已全面修复（32 references covering all required areas）。

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置 external_review）。

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5/5 |
| Excitement | 3.0 | 2.5 | 2.75/5 |
| Reproducibility | 3.0 | 4.0 | 3.5/5 |
| Overall | 3.5 | 3.0 | **3.25/5** |

**最终评级**: **Weak Accept — Findings track acceptable**

**总评**: 一篇统计方法规范、实验设计系统的 empirical study。Round 1 遗留问题全部修复，核心 finding (temporal > modality) 有完整证据链且 counterintuitive。两个 critical issues (多重比较论证 + transfer 实现细节) 可在 rebuttal/camera-ready 修复。结构性限制 (power, confound, novelty ceiling) 决定了 Findings 而非 main conference 的定位。

**投递建议**:
- 修复 W1 (多重比较论证) + W2 (transfer 细节) 后提交 ARR
- 在 commitment 阶段选择 EMNLP Findings 而非 Main Conference
- 若希望冲 Main：需补充 1-2 个非 Qwen 模型 (解决 confound) 或提出 adaptive window 方法 (解决 novelty ceiling)

---

## Detailed Comments

### Section-level 意见

**Abstract**: 精简至 200 words，保留 2-3 关键数字。删除 Bonferroni/BOCPD/CUSUM 细节。

**Introduction Contribution 2**: Qualify 为 "R1-8B demonstrates definitive HS dominance; 32B models show tentative model-dependency pending larger evaluation"。

**Section 3.2 (Metrics)**: 增加 1 段论证为何不校正 metrics within model (non-independence argument + empirical correlation)。

**Section 5.4 (Control Task)**: 增加 2-3 句讨论 QwQ-32B position baseline > HS probe 的 implications。

**Section 5.6 (Transfer)**: 当前 3 行→扩展为 0.5-1 page (正文或 Appendix)，提供完整实现细节。

**Discussion**: 
- 增加 "Position as confound vs genuine temporal signal" 段落
- 增加 "Architecture/scale/distillation disambiguation" 段落
- "Deployment recommendations" 改为 "Design implications"
- 精简与 Section 5 重复内容

**Conclusion**: 压缩为 1 段 recap + future work（当前与 Discussion 重复过多）。

**Appendix D**: 补充 multi-layer GRU per-seed 表格。

**Limitations**: 增加 text encoder 选择 sensitivity 讨论。