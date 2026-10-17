---
round: 24
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T21:38:44.882148+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 24

**Venue**: EMNLP 2026 (via ARR)  
**Paper**: EC-HTE: Error-Corrected Heterogeneous Treatment Effect Estimation with LLM Annotations  
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 实践适用性)  
**Rounds**: 1 (converged after cross-sharing; no Round 2 needed)  
**Cross-sharing status**: Both reviewers completed [AGREE]/[REBUT] responses. High convergence — only minor nuance on W4.

---

## Summary

本文证明了一个精确恒等式（Theorem 1），揭示全局误分类校正（global debiasing）在子群误差率异质的条件下如何在子群层面引入偏差——甚至可能反转因果效应的方向。论文提出 EC-HTE 方法（per-subgroup confusion matrix inversion + hierarchical Bayes estimation）和诊断准则（Proposition 5）来检测和修正这一问题。实验覆盖 2304 个合成配置和 8 个真实 LLM confusion matrices。

论文理论洞察有价值（首次报告 14.9% 配置出现 sign reversal），实验设计全面（消融、sensitivity analysis、operating conditions 诚实报告），但存在若干需修正的技术表述问题、选择性报告倾向、以及方法论技术新颖性有限的固有约束。

---

## Strengths

**S1. 具有实际影响的问题发现** — 首次严格证明 global debiasing 在子群层面可引入 sign reversal（14.9% configs），且通过 CivilComments 应用展示 3.2× effect-size gap 改变实质研究结论。这对使用 LLM annotation 做因果推断的研究者是重要警示。

**S2. 理论结果清晰且可操作** — Theorem 1 的 product form δ_s·Δτ/(1−2π̄) 提供了直观的偏差分解：方向由 δ_s（子群误差率偏离全局）决定，幅度由 Δτ（效应异质性）放大。Proposition 5 的诊断准则可在无需运行完整 EC-HTE 的前提下判断 debiasing 是否有害。

**S3. 全面且诚实的实验设计** — 2304 configuration grid 的系统性消融、8 个真实 LLM CMs 的 semi-real validation、明确报告操作条件（K≤4, n_expert≥250）、sensitivity analysis 展示方法边界（γ_T=0.10 → coverage 75%）。论文在 Section 5.4 和 Limitations 中没有回避方法局限。

**S4. HB estimation 的 practical value** — Hierarchical Bayes 的 partial pooling 在小样本（n_expert=50-100）下显著优于 MLE，这是一个对 practitioners 有实用价值的工程贡献。

---

## Weaknesses

### Must-Fix (阻碍接收)

**N1. A3 松弛下 "identity remains exact" 声称不准确** [R1 提出, R2 同意]

Section 3 (p3-4) 称 "Under class imbalance (relaxing A3), the identity remains exact (R²≥0.976 at P(Z=1)=0.1)"。但这混淆了两个层次：
- **General matrix form** M_global^{-1}·M_s（始终精确，无需 A3）
- **Simplified scalar product form** δ_s·Δτ/(1−2π̄)（仅在 A2+A3 下精确）

R²=0.976 ≠ 1.0 恰恰证明 simplified form 在 class imbalance 下是 approximation 而非 identity。Table 21 (Appendix S, p22) 进一步显示 R² 随 P(Z=1) 偏离 0.5 而下降，EC-HTE RMSE 优势从 ratio 1.54 收窄。

**修正要求**：区分 general matrix form（always exact）和 simplified scalar product form（A3-dependent approximation）。将 "identity remains exact" 改为 "matrix form remains exact; scalar approximation achieves R²≥0.976"。

**N2. Plug-in SE 忽略 CM 估计不确定性** [R1 提出, R2 强化]

Algorithm 1 line 11 的 SE = sqrt(diag(Ĉ_s^{-1}·V̂)) 将 Ĉ_s 当作固定已知量，完全忽略 Ĉ_s 的后验不确定性。这导致：
- n_expert 较小时（50-100）CI 宽度严重低估
- 论文自身在 footnote (p7) 报告仅 93.8% coverage（低于 nominal 95%），bootstrap 恢复 ≥95%
- 关键信息不应藏在 footnote——这是方法的 systematic deficiency

**修正要求**：(1) Algorithm 1 主体流程应注明 plug-in SE 的 under-coverage 风险；(2) n_expert < 250 时 bootstrap 应为默认推荐方案。

---

### Should-Fix (需修正但非阻断)

**W1. Ĉ_s^{-1} 在 asymmetric case 应为 M̂_s^{-1}** [R1 提出, R2 同意]

Remark 2 声称结果推广到 asymmetric CMs，Appendix C 给出 general M_s 形式。但 Algorithm 1 始终使用 Ĉ_s^{-1}。在 A2 下 C_s=M_s 故无碍，但任何读者想在 asymmetric case 实现时会困惑。这是 notation 不一致，易致实现错误。

**W2. κ 符号指代不一致** [R1 提出, R2 同意]

Algorithm 1 中 κ(Ĉ_s^{-1}) 用于 guard threshold，但 Section 4 的 O_p(κ²·n^{-1/2}) 中 κ 指向不同矩阵。需统一 notation（κ_s vs κ_global）。

**W3. Operating conditions 在 Abstract/Intro 限定不足** [R1 提出, R2 同意并补充]

Abstract 的 "7.4× bias reduction" 仅在 extreme heterogeneity + K=2 设置下成立。K=8 时 EC-HTE RMSE 劣于 global correction (Appendix I.2, Figure 8)。n_expert≥250 per subgroup 意味着 K=4 需 ≥1000 expert labels。尽管 Section 5.4/Limitations 诚实报告了这些限制，但 Abstract/Intro 的 framing 暗示更广泛适用性。

**W4. Corollary 4 贡献呈现** [R1 提出, R2 部分 REBUT]

R1 认为 Corollary 4 是 Theorem 1 的 trivial 推论。R2 反驳其叙事价值不可替代（解释为何问题长期未被发现）。**共识**：Corollary 4 不应单独列为 contribution，应作为 Theorem 1 段内自然推论讨论。

**W5. Remark 2 选择性报告——Table 10 cherry-picking** [R1 Minor 提出, R2 升级为 Should-Fix]

Remark 2 报告 diagnostic AUC=0.96 in asymmetric case，但**完全隐瞒** Table 10 (p17) 显示 EC-HTE 在所有 48 个 asymmetric 配置下 RMSE 均劣于 Global correction。这意味着 diagnostic 能发现问题但 correction 无法解决——这是 critical gap，属于选择性报告。EC-HTE per-subgroup inversion 在 asymmetric case 下需估计两倍参数（FPR/FNR separately），增加 variance。论文应在 Remark 2 明确说明。

---

### Minor Issues

**M1.** Abstract 约 185 words，符合 ≤200 要求。[确认合规]

**M2.** Figure 3 (p4) 的 "debiasing helps"/"debiasing hurts" 分区线应标注对应的 Proposition 5 threshold 公式 π_s < ε_s/(2(1−ε_s))。

**M3.** "F-L" 缩写首次出现在 Table 2 而非正文。应在正文首次引用 Frazis-Loewenstein 时定义。

---

## Questions for Authors

**Q1. A5 (balanced effect modifier) 是否从一开始就不必要？** A5 要求 P(Z=1|S=s)=0.5 for all s。如果 Theorem 1 无需 A5 即可成立（至少近似），则列出 A5 为必要假设是误导。请明确 A5 在 Theorem 1 证明（Appendix B）中的确切角色——哪一步推导需要它？

**Q2. κ-guard fallback 到 global correction 是否引入新偏差？** 当部分子群用 per-subgroup correction、其他子群 fallback 到 global correction 时，resulting hybrid estimator 可能比纯粹使用任一策略更差。高 κ 子群恰好是高误差子群，fallback 到 global 引入 Theorem 1 描述的偏差。两种策略不一致是否导致 CausalForest splitting 异常？Appendix A.1 称 κ>100 "not load-bearing" 但未分析 hybrid estimator 的理论性质。

**Q3. Subgroup membership S 的 misspecification 影响？** 论文假设 S 正确观测。但实际中：(1) 子群定义可能不捕捉真正的 error rate heterogeneity（e.g., 按 platform 分组但真正异质性在 text length）；(2) S 本身可能有 measurement error。应至少在 Limitations 讨论。

---

## Missing References

- **Filtered PPI** (arXiv:2602.10464) — R22 首次提出，R23 再次指出。与 EC-HTE 的 selective expert labeling 策略高度相关。
- 已确认无其他新的遗漏。

---

## External Review

**状态**: 未请求（项目配置未启用外部审稿）。

---

## Visual Layout Check (非评分项)

**状态**: ✅ 完成 (2026-05-25T21:16–21:20 UTC)  
**统计**: 0 critical, 0 warning, 6 info

| Page | Finding |
|------|---------|
| p1 | 首页纯文本，Figure 1 在 p2 顶部位置优秀，锚定效应及时 |
| p2 | Figure 1 红/绿配色对红绿色盲有辨识风险，建议改用 orange/blue 或添加纹理 |
| p4 | Figure 3 内部注释 "debiasing helps"/"hurts" 字号偏小（约正文 60%），建议 ≥70% |
| p7 | Figure 5 注释/虚线标签略密集 |
| p17 | Table 9 行列数多、字号小，附录可接受 |
| p31 | 末页约 1/3 空白（AI Assistants 声明），可接受 |

**红绿配色问题**与 R16-W7 (in_progress) 一致，持续跟踪。

---

## Overall Assessment

**Score: 3.5 — Borderline Conference** (R1: 3.5, R2: 3.5, 共识)

### 评分理由

**支撑 Conference 的因素**：
- 首次严格证明 global debiasing 的子群偏差 + sign reversal 14.9%——问题发现有实际价值
- CivilComments 应用中 3.2× effect-size gap 改变实质研究结论——impact 明确
- 实验设计全面诚实，包含 operating conditions 和 sensitivity analysis
- 方法可操作（Algorithm 1 + diagnostic 准则 + open-source code）

**限制 Conference 的因素**：
- 方法论技术新颖性有限——核心是 Frazis-Loewenstein (2003) confusion matrix inversion 从 global 到 per-subgroup 的扩展，属 "careful application of known techniques to important new context"
- N1 (exact identity claim) 和 N2 (plug-in SE) 需文本修正才能达到技术表述严谨标准
- W5 (selective reporting in Remark 2) 暴露 framing 倾向，降低审稿人信任
- 所有实验为 semi-synthetic，无 fully real-data validation（尽管有 Catch-22 论证辩护）
- NLP venue fit 存疑——论文本质是 causal inference methodology，NLP 为 application domain

**总结**：论文的问题发现和实践影响足够支撑 EMNLP 接收，但技术深度与 framing 严谨性需要提升。如果 N1/N2 修正到位且 W5 选择性报告问题解决，score 可升至 4.0。当前状态介于 Findings 和 Conference 之间。

---

## Detailed Comments (按优先级排序的 Action Items)

### 必须修正（阻碍接收）

1. **Section 3 p3-4**: 区分 general matrix form (exact) 和 simplified scalar form (A3-dependent approximation)。"identity remains exact" → "matrix form remains exact; scalar approximation R²≥0.976"
2. **Algorithm 1**: 注明 plug-in SE under-coverage 风险 + 推荐 n_expert<250 时用 bootstrap

### 应该修正（显著改善质量）

3. **Algorithm 1 / Remark 2**: asymmetric case 须说明用 M̂_s^{-1} 替代 Ĉ_s^{-1}
4. **全文**: 统一 κ 符号（κ_s vs κ_global 下标）
5. **Abstract/Intro**: 明确限定 "7.4×" 的适用条件（extreme heterogeneity, K=2）
6. **Remark 2**: 补充 EC-HTE 在 asymmetric case RMSE 劣于 global 的事实及原因
7. **Contribution list**: Corollary 4 降级为 Theorem 1 段内推论

### 建议修正（锦上添花）

8. **Figure 3**: 分区线标注 Proposition 5 threshold 公式
9. **正文**: F-L 缩写定义前移
10. **Limitations**: 补充 S misspecification 讨论

### Rebuttal 重点准备

- A5 在证明中的确切角色（Q1）
- κ-guard hybrid estimator 理论性质（Q2）
- 方法论新颖性的 impact-based 辩护（sign reversal 首次报告 + CivilComments 实质结论变化）
- Venue fit 论据（EMNLP 近年接收 causal inference for NLP 论文 + LLM annotation 核心趋势）