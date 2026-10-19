---
round: 7
review_mode: fresh
overall_score: borderline reject
timestamp: 2026-05-28T11:59:07.247182+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7

**论文**: Knowing When Not to Correct: Conformal Confidence Sets Expose When Learned Refinement Hurts Robot Actions
**目标 venue**: CoRL 2026 (DDL: May 29, 2026 AoE)
**Reviewer 编排**: R1（方法严谨性 + 实验设计） + R2（新颖性 + 完整性 + Related Work）
**审稿模式**: Fresh（无上轮记忆）

---

## Summary

本文研究冻结 flow-matching VLA 的 post-hoc correction 问题。作者发现无条件应用轻量 CRM（~327K 参数）会损害 LIBERO 全部四个 suite 的成功率（SmolVLA 上最高 −14.8pp），提出用 K=2 采样的 pairwise L₂ 距离作为不确定性代理，通过校准阈值 τ 门控 CRM，仅在高不确定性步骤触发校正。τ-gating 在 SmolVLA K-matched 实验下恢复了大部分退化（Δ_gate = +2.8 到 +14.5pp），但相对 VLA-only 的净提升微弱（+0.1 到 +1.5pp）。

---

## Strengths

**S1. 核心经验发现有实践价值**：系统性地证明无条件 post-hoc correction 在多个 VLA 和任务套件上有害（Table 1, Table 3），这对 VLA 部署实践有直接参考意义。[R1 AGREE, R2 AGREE]

**S2. K-matched 实验设计精良**：通过控制 K, ε, CRM checkpoint 完全相同、仅改变 gating 开关，干净地隔离了 gating 的效果。这在 ablation 设计上值得肯定。[R1 主要优势, R2 主要优势]

**S3. 方法简洁、计算开销极低**：K=2 batched inference 无额外延迟（~170ms ≈ K=1），CRM ~327K 参数，pipeline 轻量易复现。[R1 主要优势, R2 主要优势]

**S4. Limitations section 诚实**：明确承认 π₀.5 partial recovery、confidently wrong steps、scope limitations 和 n=3 局限。比很多 submission 更坦诚。[R1 AGREE, R2 AGREE]

**S5. 写作清晰**：论文结构良好，Figure 1 有效传达 pipeline，K-matched comparison 的叙事逻辑清楚。[R1 Clarity 7/10, R2 Clarity 7/10]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical | consensus: R1 AGREE + R2 AGREE] **"Conformal" 术语严重误导**

标题使用 "Conformal Confidence Sets"，但 Section 3.5 自承 "the pipeline does not implement formal conformal prediction guarantees [25]"。Conformal prediction 有严格定义（distribution-free marginal coverage guarantee），本文方法仅是 calibrated percentile thresholding。Title/Abstract/Section 3 反复使用 "conformal" 给读者的印象远强于实际方法。

R1 进一步发现 **ρ 值 framing 陷阱**：Abstract 突出报告 ρ=0.9979，但这是 K=2 L₂ 距离与 K=10 L₂ 距离的排序一致性（**稳定性**）；而 Appendix C Table 6 显示该代理与 K=10 action variance（ground truth uncertainty）的 Spearman ρ 仅 ~0.10（**有效性**），论文原文承认 "correlates weakly"。用稳定性指标暗示有效性，解释力仅 ~1%。

两位 Reviewer 一致：这不是风格偏好，而是术语过度包装（terminology inflation）——严重到需要修改标题和全文 framing。

> **跨轮追踪**: M7（Round 1 起连续 7 轮被标记，标题已改过 2 次但仍含 "Conformal"）

**N2** [critical | consensus: R2 提出, R1 AGREE] **遗漏 selective prediction / selective classification 基础文献，新颖性被高估**

τ-gating 的核心逻辑——用 scoring function（L₂ 距离）决定是否应用模型输出（CRM 校正）或 abstain（保留 VLA 原始动作）——正是 selective classification (Geifman & El-Yaniv, NeurIPS 2017; SelectiveNet, ICML 2019) 的直接实例。reject option / abstention 文献（Chow 1970, El-Yaniv & Wiener 2010）完全未被引用。2025 年还有 "Confidence-Gated Robot Autonomy"（arXiv 2605.18045）直接研究机器人中的 confidence gating。

R1 在交叉回应中确认："R2 识别出更根本的问题——整个 gating 机制的理论根源未被引用。比我关注的 TRANSIC 遗漏更根本。" 这不仅是 related work 遗漏，更影响新颖性评估——如果论文承认做的是 selective prediction + calibrated threshold，contribution 从 "提出 conformal gating 框架" 降级为 "将 selective prediction 应用于 VLA correction 并提供经验发现"。

> **跨轮追踪**: C4 升级（Round 1-2 novelty 不足 → Round 7 识别出 selective prediction 根源）

**N3** [critical | consensus: R1 AGREE + R2 AGREE] **实际提升极小，统计效力不足——τ-gated ≈ VLA-only**

τ-gated vs VLA-only 的净提升：Spatial +1.5pp (80.8 vs 79.3), Object +0.1pp, Goal +1.3pp, Long −0.3pp。在 n=3, std ≈ 0.8–2.1 的条件下，全部在噪声范围内。8-seed 分析（Appendix E）Spatial p=0.017 但效应极小。Object/Long 本质上是 null result。

论文的主要叙事 Δ_gate（τ-gated vs CRM always-on = +2.8 到 +14.5pp）是有效的 ablation，但**对部署决策真正重要的是 vs VLA-only**。方法本质上是将有害 CRM 恢复到 baseline 水平，而非提供真正的性能提升。

R2: "为何不直接用 VLA-only？添加 K=2 + CRM + τ-gating 的复杂度换来的是统计上不显著的提升。" R1: "用户实际选择是 (a) VLA-only 或 (b) VLA + CRM + gating 得到约等于 VLA-only 的结果，方案 (b) 增加系统复杂度但收益甚微。"

> **跨轮追踪**: C3（Round 1 起连续 7 轮标记）

**N4** [critical | R1 提出, R2 未反驳] **K=2 argmin-to-centroid selection 数学上退化（degenerate）**

K=2 时，centroid μ = (a^(1) + a^(2))/2。每一步 ||a^(1) − μ||₂ = ||a^(2) − μ||₂ = ||a^(1) − a^(2)||₂/2。argmin 对两样本给出完全相同 cost——selection 永远 tie，等价于随机选取。这意味着 Table 8 中 K=2 argmin ablation 实际等价于随机选一个样本。论文从未讨论这一点，却在 Abstract/Introduction 中将 "multi-sample selection" 框架为关键贡献组成部分。

> **跨轮追踪**: R7-N1（新发现）

**N5** [critical | R2 提出, R1 AGREE] **π₀.5 跨模型验证为单种子（n=1），Contribution 3 不成立**

π₀.5 (3.6B) 的结果为 n=1 seed，无法估计方差，无法 "confirm" 任何 pattern。Introduction Contribution 3 将此作为核心贡献（"confirming the pattern across model scale"），但 Limitations 承认 "recovery on π₀.5 is partial: gating recovers roughly half"——与 Abstract/Conclusion 强调全面恢复的叙事不一致。

> **跨轮追踪**: R1-W3-new 升级（Round 2 warning → Round 7 R2 升级为 critical）

**N6** [critical | R1 提出, R2 隐含同意] **"校正有害" 结论的普遍性未被验证——可能是 CRM 设计缺陷**

"Unconditional learned correction hurts VLA" 完全基于一种 CRM 设计（327K MLP, L₂ loss, 离线训练, 3-suite 训练）。未探索更大架构、在线训练、其他 loss。Long suite 的 OOD confound（CRM 未参与训练）使部分 "correction hurts" 可能是 distribution mismatch。如果换一个更好的 CRM 就不再有害，核心发现就不是 "correction is harmful" 而是 "this particular weak CRM is harmful"——后者贡献显著降低。

> **跨轮追踪**: R7-N3（新发现）

### Should-Fix（影响评分但不一票否决）

**W1** [warning | consensus] **仅 LIBERO 模拟，无真实机器人实验**
仅一个仿真基准（LIBERO），对 CoRL（Conference on Robot Learning）而言是显著弱点。Cross-VLA 验证仅验证 degradation pattern，τ-gating 在 π₀.5 上的恢复效果不完整。[R1 AGREE, R2 W4]
> 跨轮追踪: M1

**W2** [warning | consensus] **\enlargethispage{6\baselineskip} + 多处 \vspace hack，实质超 8 页**
discussion.tex 使用 \enlargethispage{6\baselineskip}（约额外 6 行）+ \vspace{-8pt/-4pt/-2pt}，实质使正文超过 CoRL 8 页限制。[R2 W2, R1 AGREE]
> 跨轮追踪: C6

**W3** [warning | consensus] **遗漏 CP-robotics 重要相关工作**
Conformalized Teleoperation (Luo et al., RSS 2024)、Safety-Critical Control with Adaptive CP、Conformal Prediction for Crowd Navigation (CoRL 2025) 等真正使用 formal CP 的 robotics 工作均未引用。论文如果用 "conformal" 就需要说明与这些有保证的 CP 方法的区别。[R1 AGREE, R2 W3]
> 跨轮追踪: R3-N3

**W4** [warning | R1] **ρ=0.9979 仅在 Object 单 suite 验证**
K=2 L₂ 距离与 K=10 variance 的 Spearman ρ=0.9979 仅在 Object suite 上评估（27,626 steps）。不同 suite 的 action distribution 特性不同，proxy quality 可能差异很大。[R1 W1]

**W5** [warning | R1] **τ-sweep 数据大多 n=1 seed**
Spatial 7 个 τ 值仅 τ=0.25 有 n=3，其余全部 n=1。"SR is robust to τ choice, varying by ≤1pp" 在 n=1 条件下缺乏统计支撑。[R1 W2]

**W6** [warning | R1] **ε 没有 ablation**
全文所有实验只用 ε=0.2。ε 与 τ 可能存在交互效应——较小的 ε 可能使 CRM always-on 的 degradation 减小，从而改变 gating 的价值。[R1 W4]
> 跨轮追踪: R3-N1

**W7** [warning | R1] **Long suite "strongest evidence" 存在 OOD confound**
Long 上 CRM 未参与训练（OOD），−14.8pp 降幅和 +14.5pp gating 恢复本质是 "OOD correction 有害，gating 避免"。论文将此与 in-distribution 结果合并讨论，模糊了两种不同 mechanism。[R1 W5]

**W8** [warning | R1] **缺少 K=1 + CRM τ-gated baseline**
鉴于 K=2 argmin degenerate（N4），K=2 的唯一价值是提供 uncertainty signal。自然问题：能否用 K=1 的 alternative proxy（如 CRM correction magnitude 或 FMVD）做 gating？[R1 W6]
> 跨轮追踪: R3-N2

### Minor

- **Eq.1 vs Section 3.5 step 1 公式不统一**（sum over H vs single norm）[R1]
- **Table 1 "~" 前缀 trigger rate** 应用精确数字或 CI [R1]
- **Figure 3 因果解释过强**：仅 4 个 suite-level 数据点声称 "monotonic correlation" [R1]
- **"80-97% confident steps" 循环论证**：来自 trigger rate（由 τ 决定），应独立验证 [R1]
- **DAgger 引用不精确**：DAgger 是 interactive online aggregation，非 static noise injection [R1, R2]
- **Bib 条目信息不全**：部分 2025 文献仅 arXiv，cite key 与 year 不一致 [R1, R2]
- **Abstract ρ=0.9979 未说明计算对象和数据分布** [R2]
- **Table 3 π₀.5 cross-server 评估引入硬件混淆变量** [R2]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 独立到达相同结论或在交叉分享中明确同意：

| 编号 | 问题 | R1 | R2 |
|------|------|-----|-----|
| N1 | Conformal 术语误导 | AGREE + ρ framing 证据 | AGREE (critical) |
| N2 | Selective prediction 文献遗漏 | AGREE（承认比 TRANSIC 更根本） | 提出者 (critical) |
| N3 | 净收益微弱 τ-gated ≈ VLA-only | 提出者 (critical) | AGREE (warning→共识升级) |
| N5 | π₀.5 单种子 Contribution 3 不成立 | AGREE | 提出者 (critical) |
| W1 | 仅 LIBERO sim-only | AGREE | 提出者 |
| W2 | \enlargethispage 格式 hack | AGREE | 提出者 |
| W3 | 缺 CP-robotics 文献 | AGREE | 提出者 |

## Reviewer Divergence

**无重大分歧。** 唯一差异在严重性定级：
- R1 将 "conformal 命名" 定性为 "术语过度包装"（严重但非学术诚信问题），R2 定性为 "学术诚实性问题"。Director 采纳 R1 的定性——论文在 Section 3.5 和 Conclusion 有 disclaimer，非刻意隐瞒，但 disclaimer 位置太晚且不够突出。
- R1 倾向 overall 4-5/10（偏 4），R2 给 5/10。差异来自 R1 独有发现（ρ≈0.10 framing 陷阱）。Director 综合为 5/10 (Borderline Reject)。

---

## Questions to Authors

1. **K=2 argmin tie-breaking**: K=2 argmin-to-centroid 对两个样本 cost 恒等，实际实现中如何 tie-break？论文如何解释 "selects the sample closest to the centroid" 在 K=2 下的意义？
2. **ρ=0.9979 vs ρ≈0.10**: 能否澄清 Abstract 中 ρ=0.9979 与 Table 6 中 ρ≈0.10 分别度量什么？如果前者仅反映代理的稳定性而非有效性，是否应在 Abstract 中更明确说明？
3. **为何不直接 VLA-only**: τ-gated 最终 ≈ VLA-only（Table 1），添加 CRM + gating 的系统复杂度换来的收益不显著。在什么场景下用户应选择 CRM+gating？
4. **CRM 设计空间**: "unconditional correction hurts" 是否特定于 327K MLP + L₂ loss 的 CRM？更大架构或不同训练方式是否改变结论？
5. **π₀.5 multi-seed**: 能否提供 π₀.5 至少 n=3 的结果？当前 n=1 无法支撑 Contribution 3。
6. **ρ 跨 suite 泛化**: ρ=0.9979 只在 Object 上验证。Spatial, Goal, Long 上的 ρ 值是多少？
7. **τ 的 task-dependency**: 在无 held-out calibration data 的新任务上，如何选择 τ？
8. **Selective prediction 联系**: τ-gating 与 selective classification (Geifman & El-Yaniv 2017) 的区别是什么？如果没有本质区别，novelty claim 如何成立？

---

## Missing References

### 必须引用
1. **Geifman & El-Yaniv (2017)**. "Selective Classification for Deep Neural Networks." NeurIPS 2017. — τ-gating 的直接理论先驱。[R1 AGREE, R2 critical]
2. **Geifman & El-Yaniv (2019)**. "SelectiveNet: A Deep Neural Network with an Integrated Reject Option." ICML 2019. [R2]
3. **Luo et al. (2024)**. "Conformalized Teleoperation." RSS 2024. — 机器人中真正使用 CP 保证的工作。[R1 AGREE, R2]

### 建议引用
4. Lindemann et al. (2023). "Safe Planning in Dynamic Environments Using Conformal Prediction." RA-L. [R1]
5. "Confidence-Gated Robot Autonomy: When Does Uncertainty Actually Help?" arXiv 2605.18045, 2025. [R2]
6. Lakshminarayanan et al. (2017). "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles." NeurIPS 2017. — K=2 L₂ 是 ensemble disagreement 最简形式。[R2]
7. Gal & Ghahramani (2016). "Dropout as a Bayesian Approximation." ICML 2016. [R2]
8. TRANSIC (Jiang et al., CoRL 2024). — learned gated residual policy for sim-to-real. [R1]
9. Conformal prediction for crowd navigation (CoRL 2025). [R2]
10. Dixit et al. (2024/2025). Adaptive conformal prediction for safety-critical control. [R2]

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成

| 严重性 | 页面 | 发现 |
|--------|------|------|
| critical | p.11 | 引用 [27]-[28] 仅占页顶约 15%，剩余约 85% 完全空白。审稿人看到整页空白会留下"论文未完成"的负面印象。应合并或将 Appendix 提前填充。 |
| warning | p.1-2 | 前两页纯文本无 display item。Figure 1 延迟到 Page 3 降低第一印象冲击力。建议 Page 1 底部或 Page 2 顶部放 teaser figure。 |
| warning | p.4-5 | 连续两页无 figure/table（仅公式），Method→Experiments 过渡区密集。可考虑将 Table 1 或 Figure 2 提前。 |
| warning | p.16 | 末页 Appendix I Table 11 后约 55% 空白。 |
| info | p.3 | Figure 1 部分标签字号偏小，打印时需确认可读性。 |
| info | p.6 | Table 1 + Figure 2 同页，信息密度高但排版紧凑合理。 |
| info | p.8 | Tables 2-3 + Conclusion 同页，阅读节奏稍急促。 |
| info | p.9-10 | 参考文献格式一致，无未解析引用。 |
| info | p.12 | Appendix Table 4 行数多但格式规范。 |

---

## Overall Assessment

**Overall: 5/10 (Borderline Reject)**
**Confidence: 4/5**

### 维度评分汇总

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Originality | 5/10 | 4/10 | **4/10** — selective prediction 文献盲区使 novelty claim 被高估 |
| Quality (Soundness) | 4/10 | 5/10 | **4/10** — K=2 argmin degenerate + ρ≈0.10 framing + n=1 π₀.5 |
| Clarity | 7/10 → 6/10 | 7/10 | **6/10** — 写作本身清晰但 conformal framing 与实际方法落差扣分 |
| Significance | 4/10 | 4/10 | **4/10** — τ-gated ≈ VLA-only，实用价值有限 |
| Relevance | 8/10 | 7/10 | **7/10** — VLA inference-time refinement 高度相关 CoRL |

### 核心判断

论文的实证发现（无条件 correction 有害）是有价值的 diagnostic insight，K-matched 实验设计值得肯定。但当前形态下不足以作为 CoRL 长文接收：

1. **Framing 根本性问题**（N1, R7-N2）："Conformal Confidence Sets" 标题与实际 percentile thresholding 之间存在显著落差；ρ=0.9979（稳定性）被用来暗示 ρ≈0.10（有效性），构成 framing 陷阱。**连续 7 轮被标记，标题已改过 2 次但核心问题未解决。**

2. **新颖性不足**（N2, C4）：τ-gating 是 selective prediction 的直接实例，K=2 L₂ 是 ensemble disagreement 最简形式，CRM 是标准 residual MLP。论文将已知组件组合呈现为新框架，但完全未引用 selective prediction/reject option 这一成熟文献体系。

3. **数学疏忽**（N4, R7-N1）：K=2 argmin-to-centroid 在数学上 degenerate（两样本 cost 恒等），论文未讨论。

4. **实用价值存疑**（N3, C3）：τ-gated ≈ VLA-only，增加系统复杂度（CRM 训练 + calibration + gating）但收益在统计噪声范围内。

5. **评估范围窄**（W1, M1）：仅 LIBERO sim + SmolVLA 主实验 + π₀.5 单种子。对 CoRL 而言缺少真机实验是显著弱点。

6. **结论普遍性未建立**（N6, R7-N3）："correction is harmful" 可能是特定弱 CRM 的 artifact，Long suite 的 OOD confound 加剧担忧。

### 修订建议

如果作者愿意大幅修订：
- 去除 "conformal" 标签，改为 "calibrated uncertainty gating" 或 "selective correction"
- 在 Related Work 添加 selective prediction + reject option 段落，诚实定位贡献
- 明确指出 K=2 argmin degeneracy，重新定位 K=2 价值在于 uncertainty signal
- 区分 ρ=0.9979（稳定性）和 ρ≈0.10（有效性），不在 Abstract 误导
- π₀.5 补充至少 n=3 seeds，或将 Contribution 3 降级为 preliminary observation
- 明确区分 in-distribution gating 和 OOD protection 两种 mechanism
- 去除 \enlargethispage hack，确保正文 ≤8 页
- 重新定位为 "empirical study of when correction helps VLAs"

论文可能更适合 CoRL Workshop 或修订后投稿正会。

---

## Detailed Comments

### Title / Abstract
- "Conformal Confidence Sets" 须替换——方法不满足 CP 的数学定义 [N1]
- ρ=0.9979 需明确说明是稳定性而非有效性指标 [R7-N2]
- "recovers nearly all degradation" 仅对 SmolVLA 成立，π₀.5 only partial recovery [N5]

### Section 1 (Introduction)
- Contribution 3（跨模型泛化）基于单种子，不足以 claim "confirming the pattern" [N5]
- 引用 VLA-Pilot "2.41s per control step" 缺原始上下文（硬件条件）[R1 minor]

### Section 2 (Related Work)
- **完全缺失**: selective prediction / selective classification / reject option 文献 [N2]
- **不足**: CP-robotics 文献（Conformalized Teleoperation, Lindemann et al.）[W3]
- **不足**: ensemble disagreement 基础文献 [R2]
- TRANSIC (CoRL 2024) 遗漏——learned gated residual policy [R1]

### Section 3 (Method)
- Section 3.2 Eq.1: K=2 argmin degenerate 未讨论 [N4]
- Section 3.4: ε=0.2 无 ablation [W6]
- Section 3.5: "conformal" disclaimer 太晚且不够突出 [N1]
- Eq.1 vs Section 3.5 step 1 公式不统一 [R1 minor]

### Section 4 (Experiments)
- Table 1: 核心结论 τ-gated vs VLA-only Δ 全部在噪声范围内 [N3]
- Section 4.3: Figure 3 仅 4 点声称 "monotonic correlation"——因果解释过强 [R1 minor]
- Section 4.5: π₀.5 单种子不足以支撑任何结论 [N5]
- Table 4: τ-sweep 大量 n=1 [W5]
- Long suite: OOD confound 须与 in-distribution 结果分开讨论 [W7]

### Section 5-6 (Conclusion / Limitations)
- Conclusion 措辞仍暗示 improvement 而非 recovery [N3]
- \enlargethispage{6\baselineskip} 使正文实质超页 [W2]

### Appendix
- Table 6: ρ≈0.10 与正文 ρ=0.9979 的关系需要在正文说明 [R7-N2]
- Table 8: K=2 argmin ablation 因 degeneracy 实际等价于 random [N4]

### References
- 多个 bib 条目缺 venue info（仍有 @misc 条目）[M4]
- cite key 与 year 不一致（snell2024scaling year=2025）[R2 minor]

---

## Issue Tracker 同步

本轮新增 4 个 issue（R7-N1 至 R7-W1），更新 12 个已有 issue 的 Round 7 mentions。5 个 Round 3 issue 本轮未被提及（M6, M3, R3-W9-new, R3-W10-new, M5），标注待 Research Director 确认。详见 `artifacts/review_issues.yaml`。