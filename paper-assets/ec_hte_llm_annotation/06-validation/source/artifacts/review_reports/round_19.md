---
round: 19
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T16:15:24.588526+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 19 审稿报告（修订版）

> 修订原因：Reviewer 1 完整审稿揭示了 Abstract 中 R²≥0.97 claim 的事实性错误（Table 23 显示真实 LLM 上 R² 低至 0.08），以及 CausalForest 集成验证深度不足，这些在初始交叉回应中未被充分传达。本修订版将这些发现纳入并调整了严重程度排序。

## Summary

本文研究 LLM 标注在异质处理效应 (HTE) 估计中的偏差问题。核心发现：当 LLM 分类器的误差率在子群间存在异质性时，标准全局混淆矩阵校正可引入新偏差甚至反转 CATE 符号。论文推导了精确偏差恒等式 (Theorem 1: bias = δ_s · Δτ / (1-2π̄))，提出基于层级贝叶斯的逐子群校正方法 (EC-HTE)，并在合成和半合成数据上验证。

---

## Strengths

1. **核心理论贡献扎实**：Theorem 1 是精确有限群体恒等式（非渐近近似），形式 δ_s · Δτ / (1-2π̄) 简洁且可解释。揭示了一个非直觉洞察：global correction 的偏差同时取决于误差率异质性和处理效应异质性，两者缺一则偏差为零。证明严谨。

2. **问题定位精准且时效性强**：effect modifier misclassification 是一个被忽视的问题（vs PPI/DSL 的 population-level + outcome-side），在 LLM-as-annotator 快速增长的背景下具有实际意义。

3. **实验覆盖面极其全面**：520+ 合成配置、11 个真实 LLM CM、4 个 NLP 任务（sentiment, hate speech, stance, topic）、多种下游估计器（DIM, CausalForest, R-learner）、25 页附录含 10+ 假设违反的 robustness 分析。在同类方法论文中属顶级验证深度。

4. **方法论定位清晰**：相对于 PPI（通用预测误差）、DSL（population-level 聚合）、PPCI（outcome-side error），EC-HTE 利用混淆矩阵结构进行逐子群校正，填补了明确的 gap。Related Work 覆盖 50+ 引用。

5. **诚实透明的局限性讨论**：Operating conditions 明确列出，在条件不满足时推荐 global correction。

---

## Weaknesses

### Critical

**C1. Abstract 中 "R² ≥ 0.97 across synthetic grids and 11 empirical LLM confusion matrices" 是事实性错误** [R1-N1; 交叉未充分传达]

Table 23 (p25) 报告真实 LLM CM 下的 bias identity R²：GPT-4-turbo/TweetEval R²=0.097，Gemma-2-9B/TweetEval R²=0.082——远低于 0.97。全模型平均约 R²=0.873。Abstract 语法 "verified at R² ≥ 0.97 across synthetic grids **and** 11 empirical LLM confusion matrices" 暗示该 R² 同时适用于两者，但实际仅在合成数据（A1-A5 满足）上成立。

这是 Abstract 对核心理论结果的量化 claim。恒等式数学上是精确的，但其预测力依赖于假设满足程度——R² 低至 0.08 说明在强 asymmetric 误差下乘积结构的解释力急剧下降。这一 nuance 在 Abstract 中完全缺失。

**修改要求**：Abstract 必须区分合成与真实 LLM 的 R² 范围（如 "R² ≥ 0.97 on synthetic grids; 0.08–0.97 on real LLM matrices, degrading under strong FPR/FNR asymmetry"）。

---

**C2. 诊断工具 (Proposition 5) AUC=0.63 但被呈现为核心贡献无性能限定** [R2-N1; R1 AGREE]

Abstract 称 "immediately yields a Δτ-free diagnostic that flags harmful correction from error rates alone (AUC = 1.0 when Δτ > 0)"——选择性报告了最佳子集结果。实际性能：
- Synthetic (symmetric errors): AUC = 0.86
- Real LLM-dataset pairs (asymmetric errors): AUC = 0.63

诊断被列为三项核心贡献之二，但作为自动筛选工具的实用价值有限。

**修改要求**：加限定词或将诊断降级为 Theorem 1 的 theoretical corollary with limited practical screening power。

---

**C3. 核心量化 claims (7.4×, R²=0.991) 在假设完全满足的合成数据上得出，存在循环论证** [R1-N2]

合成 DGP (Appendix E) 严格满足 A1-A5。在此设定下：
- R²=0.991 是数学必然（恒等式在假设满足时是 exact 的），非实验发现
- 7.4× bias reduction (Table 1, K=2 extreme: EC-HTE 0.008 vs Global 0.059) 在理想条件下测量

更关键的是，Table 1 的 K=2 **moderate** 配置下，EC-HTE |bias|=0.012 与 Global |bias|=0.012 **持平——无任何改善**。7.4× 仅在极端异质性下成立。

**修改要求**：Abstract 中明确标注条件 "under extreme heterogeneity (Δπ=0.25)"；区分"验证恒等式正确性"和"验证方法实用性"的实验目的；给出 moderate 配置下的数字作为参照。

---

**C4. CausalForest 集成验证不足，与其作为核心管线组件的地位不匹配** [R1-N3]

论文将 EC-HTE 定位为完整 HTE 估计管线（标题含 "Treatment Effects"，Figure 2 以 CausalForest 为输出），但：
1. 缺乏 individual-level CATE 指标（PEHE 或 CATE calibration）——仅报告聚合 bias/RMSE/coverage
2. CausalForest 结果仅在合成 DGP 上测试，未在半合成（真实 LLM CM）上运行完整管线
3. Section 4.3 的关键创新——不确定性传播 (Eq. 7)——缺消融实验（vs 点估计校正的效果差异）

Contribution claim 与 evidence 深度不匹配。

---

### Should-Fix

**W1. 操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件** [共识]

Table 24 确认 16 个组合中无一全部满足。Relaxed screening 下 79% 有效，但 strict conditions 全部不满足与 practical framing 存在张力。R1 定性 critical；R2 认为 should-fix。Director 判定 should-fix（论文已透明讨论，且诊断框架指导"何时不该纠正"有独立价值）。

**W2. DGP 缺乏 observational/confounding 场景** [共识: AGREE]

主文所有实验为 RCT DGP。Appendix Z.4 仅一个 confounded configuration。论文声称兼容 observational CausalForest/R-learner 但缺验证。

**W3. Assumption (A2) symmetric misclassification 的表述自相矛盾** [共识: AGREE]

Section 3 列 A2 为正式假设 → Remark 2 撤回 → Proposition 5 又依赖 A2。建议降级为"简化展示用特殊情况"。

**W4. Theorem 1 → Proposition 3 呈现顺序误导** [R1-W1]

A5（homogeneous treatment effects across subgroups）恰恰排除了本文要解决的场景。Proposition 3 放松 A5 才覆盖实际场景，但读者可能忽略这一复杂性。

**W5. HB 优势在大 budget 下消失但未讨论** [R1-W2]

n_expert ≥ 250 时 HB 与 Stratified MLE 收敛；n_expert ≥ 500 时几乎无差异。HB 价值仅在小 budget (<250) 场景——应明确陈述。

**W6. Plug-in SE 欠覆盖 93.8% 且主结果未标注 SE 方法** [共识: AGREE]

Table 1 CausalForest coverage=0.90 基于 plug-in SE；bootstrap 恢复 ≥95% 但未在主表呈现。MC SE 也应在主表中标注。

**W7. 缺乏 fully real-data validation** [R2; R1 acknowledges as inherent limitation]

所有 "real-data" 为 semi-synthetic（真实 CM + 合成 outcomes）。同领域标准做法，但仍削弱 practical claims。

**W8. Finite-sample 传播保证缺失** [共识: AGREE]

Population-level identity → plug-in estimator 的 remainder 仅有 O_p notation，缺 formal finite-sample theorem。

### Minor

**W9.** Conclusion 仅两句话，过短。[AGREE]

**W10.** Figure 2 红绿配色色盲不友好。[AGREE, 跨轮复发]

**W11.** HB 先验敏感性分析不充分。[R1 补充]

**W12.** Bootstrap SE (B=100) 计算成本未讨论。[R1 补充]

**W13.** Assumption (A5) 实践限制被轻描淡写。[R2 补充]

**W14.** Figure 1A scatter plot 过度拥挤，红三角与蓝圆点重叠。[R1]

**W15.** "Semi-synthetic" 术语在 Section 5.1 和 5.3 含义不同。[R1]

**W16.** Algorithm 1 缺收敛标准/最大迭代次数。[R1]

---

## Reviewer Consensus

双方达成共识 [AGREE] 的问题：
- Abstract R² 和 AUC claims 存在 overclaiming（C1, C2）
- 操作条件窄（W1）
- A2 表述矛盾（W3）
- DGP 缺混杂场景（W2）
- Plug-in SE 标注不足（W6）
- Finite-sample 桥接缺失（W8）
- 14.9% sign reversal 的 framing 合理（τ(0)=0.03 已显式标注，不构成 cherry-picking）

## Reviewer Divergence

| Issue | R1 | R2 | 本报告判定 |
|-------|----|----|-----------|
| 操作条件严重程度 (W1) | Critical | Should-fix（已透明讨论） | Should-fix |
| 7.4× 循环论证 (C3) | Critical | 未直接回应 | Critical（Abstract 需加条件限定） |
| CausalForest 验证 (C4) | Critical | 未直接回应 | Critical（作为管线核心需匹配验证深度）|
| EC-HTE vs DSL 增量 | — | "仅 hierarchical shrinkage" | R1 rebut 有力：含 identity + HB + CF 集成 |
| Real-data validation (W7) | Inherent limitation | Weakens claims | Should-fix |

---

## Questions

1. Table 23 显示 GPT-4-turbo/TweetEval R²=0.097, Gemma-2-9B/TweetEval R²=0.082。Abstract 中 "R² ≥ 0.97 across ... 11 empirical LLM confusion matrices" 的具体含义是什么？
2. Table 1 K=2 moderate 下 EC-HTE 与 Global 持平 (|bias|=0.012)。EC-HTE 有显著改善的 Δπ/Δτ 阈值是什么？
3. 是否有 CausalForest 不确定性传播 (Eq. 7) vs 点估计校正的消融实验？
4. 如果 LLM 准确率提升（Δπ→0），EC-HTE 的价值是否会消失？
5. Proposition 2 (A5 relaxation) 是否应在主文给出 representative result（而非仅 Appendix F）？

---

## Missing References

无重大遗漏。可选补充：Schennach (2004, *Econometrica*) 关于非线性模型测量误差处理。

---

## External Review

**状态**: 未请求（项目配置未启用）。

---

## Visual Layout Check

**状态**: 仍在进行中，本报告不等待。完成后会自动补发到 Group C。

---

## Overall Assessment

**评分: 3.5 — Borderline Conference**

**置信度: 4/5 (High)**

**理由**：

Theorem 1 的 bias decomposition identity 是本文的真正贡献——精确、原创、揭示了一个被忽视的问题。这一理论贡献独立于 EC-HTE 方法即具有发表价值。实验覆盖面在同类论文中属顶级。

**阻碍达到 4.0 (Conference) 的主要因素**：

1. **Abstract 事实性错误**：R²≥0.97 的 claim 在真实 LLM 上不成立（低至 0.08），AUC=1.0 仅在限定子集上成立。这是核心 claims 的诚信问题，不是表述瑕疵——需要实质性修改。

2. **核心数字的推广性存疑**：7.4× 仅在 extreme heterogeneity 下成立，moderate 配置下无改善。合成验证的 R²=0.991 在假设满足时是数学必然。读者可能被误导。

3. **CausalForest 管线验证不匹配**：论文以 "Treatment Effects" 为标题、以 CausalForest 为管线输出，但该环节的验证深度（无 PEHE、无半合成 CF、无 Eq.7 消融）远低于混淆矩阵估计环节。

4. **实际适用性边界模糊**：无真实 LLM 通过全部筛选条件 + 全为 RCT DGP + semi-synthetic validation，practical claims 的支撑链不够完整。

**如果修订能**：(a) 修正 Abstract claims 以准确反映不同条件下的表现范围，(b) 补充 CausalForest individual-level 评估和 Eq.7 消融，(c) 在 Abstract/Intro 中对 7.4× 加条件限定，本文有望达到 Conference 水平。当前版本的 claims-evidence gap 使其处于 Borderline Conference 和 Conference 之间的低端。

---

## Detailed Comments

### Abstract
- 约 130 words，格式合规（≤200 words）
- 需修正：R²≥0.97 的范围限定、AUC=1.0 的条件说明、7.4× 的配置条件

### Section 1 (Introduction)
- Hook 有效（content moderation sign reversal example）
- 贡献列表清晰，但诊断工具的定位需降级或加 caveat
- 14.9% sign reversal 的呈现方式合理（条件已标注）

### Section 3 (Theory)
- Theorem 1 证明正确。5 assumptions + 1 theorem + 3 propositions + 1 corollary + 2 remarks 密度极高
- A2 的处理方式需改为脚注式说明
- Proposition 3 (A5 relaxation) 应在 Theorem 1 后立即强调其实践重要性
- 建议将 Corollary 4 (multiclass) 移入 Appendix

### Section 4 (Method)
- Figure 2 (method overview) 清晰有效
- Section 4.1 HB 描述充分但缺 wall-clock time
- Section 4.3 的 "n_expert/K<50 → bootstrap" 规则应在主文呈现
- Eq. 7 的不确定性传播需消融验证

### Section 5 (Experiments)
- Table 1 需：(a) 增加 SE 列或括号标注，(b) caption 标注 SE method
- CausalForest 仅一个配置 (K=4, extreme)——需补充 moderate + 半合成
- Section 5.4 诊断部分应给予更充分展示空间
- "Semi-synthetic" 术语需统一定义

### Limitations
- 覆盖面充分
- 建议补充：A5 violation 的实践影响、HB 优势的 budget 上限

### Format
- ACL template 合规，double-blind 无泄露
- 正文 ≤8 pages
- Appendix 使用恰当（详细证明 + 扩展实验）