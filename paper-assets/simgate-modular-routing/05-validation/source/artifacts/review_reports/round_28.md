---
round: 28
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T09:02:25.467857+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 28 审稿报告 — simgate-modular-routing

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (ARR May cycle), Interpretability and Analysis track
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作）
**交叉轮次**: 1 轮（关键问题达成共识，无需 Round 2）

---

## Summary

论文提出 episode-level counterfactual diagnostic framework，通过对比 pure-strategy（internal-only vs deterministic-only）的 episode outcomes 来 decompose routing signal 的组成。应用于 ScienceWorld（11 task types, 245 episodes），发现 78.9% 的 non-tie routing labels 源于 death asymmetry（内部策略触发 -100 死亡惩罚而确定性策略存活）。Cross-model replication（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）确认 DAF 88-90%（spread 2.2pp）。Router training（Qwen3 0.6B-4B）在 episode level 降至 chance 以下，报告为 diagnostic negative result。Cross-environment probes（MATH, ALFWorld）展示框架在无 death 环境中诊断不同 routing mechanism 的能力。

---

## Strengths

1. **极其详尽的鲁棒性验证**（R1-S2, R2-S1）：20 个 appendix 覆盖 LOO、cluster bootstrap、wild bootstrap、penalty sensitivity、cross-model、cross-environment、capacity scaling、augmentation ablation 等——在 analysis track 论文中属顶级水平。
2. **诚实的负面结果报告**（R1-S3, R2-S2）：Router training failure（episode-level balanced accuracy 47.1% < 50% chance）被完整报告而非隐藏，提供两种可能解释（signal-limited vs data-limited），附带 text augmentation、capacity scaling、death-proximal labeling 等排除实验。
3. **Cross-model convergence**（R1-S4, R2-S4）：三个架构差异显著的 7-9B 模型家族 + 72B scaling 给出 DAF 88-92%（spread 2.2pp），有力排除模型特异性解释。
4. **Penalty-independent 与 penalty-dependent 度量双轨报告**（R2-S3）：区分 label fraction (78.9%, P-invariant) 和 DAF (90.4%, P-dependent)，展示完整 P-sensitivity 曲线（Appendix K）。
5. **Track fit 优秀**（R2-S5）："先诊断 routing signal 再决定是否训练 router" 的理念与 Interpretability and Analysis track 高度匹配。
6. **研究问题定义清晰**（R1-S1）：填补了 routing literature 中"routing signal 到底由什么组成"这一方法论空白。

---

## Weaknesses

### Must-Fix（2 项，双方共识）

**[AGREE x2] W-Critical-1: DAF 度量的 P-dependence 在主文中讨论不足**
- 来源：R1-N2 + R2-N1（完全共识）
- 问题：DAF = δP/(δP + Δ_nd) 随 P 单调递增（P=10→50.4%, P=50→82.6%, P=100→90.4%, P=200→94.9%），是数学必然而非纯实证发现。Appendix K 承认"mathematical consequence"，但主文 §2.4 仅标记 DAF 为 "derived penalty-dependent measure"，未展示 P-sensitivity 的任何数值。Abstract 虽以 78.9% 为 headline，但 DAF=90.4% 仍以核心数字地位出现。
- 影响：Analysis track 论文的核心度量之一有数学 artifact 成分但主文透明度不足，可能导致读者高估 finding 的实证强度。
- 建议：(1) §2.4 定义 DAF 后增加 1-2 句正文讨论 P-sensitivity（至少引用 P=10 和 P=50）；(2) Abstract/Conclusion 进一步降低 DAF 的 prominence。

**[AGREE x2] W-Critical-2: "Deterministic" 跨环境含义不统一，transfer claim 需更精确限定**
- 来源：R2-N2（R1 交叉时 AGREE）
- 问题：三环境 "deterministic" 实现差异巨大（oracle simulator / code interpreter / admissible-action enumeration），信息优势程度不可比。§2.1 描述了差异但 Conclusion 仍写 "the diagnostic procedure transfers"，暗示跨环境一致性高于实际水平。
- 影响：读者可能期望比论文实际提供的更强的泛化性。
- 建议：Conclusion 或 §3.4 增加限定：cross-env probes 验证 diagnostic procedure 的可复用性，不是 "deterministic computation" 概念的一致性。

### Should-Fix（7 项）

**[AGREE x2] W1: 63% task type 排除率需在主文更充分 justify**
- 来源：R1-W2 + R2-W1
- 问题：主文 §3 仅一句话说明排除原因。缺 taxonomic redundancy 的操作定义。Anti-cherry-picking 数据（excluded ΔDR=+38.2 > included +28.7 pp）全在 appendix。
- 建议：§3 增加一段展示 key numbers + taxonomic redundancy 定义。

**[DIVERGENCE → warning] W2: Episode→step 粒度失配的 framing 精确性**
- 来源：R1-N1（critical）vs R2 REBUT（warning）
- R1 主张：Title/Abstract 暗示 step-level routing 发现，实际证据限于 episode-level outcome。
- R2 反驳："Routing Signal" ≠ "Routing Decision"；episode-level 是 sparse-reward 环境的 principled granularity（97.4% step ties）。但同意 Abstract 应加 "episode-level" 限定词。
- 最终判定：降为 warning。Claim validity 不受影响，但 framing 可更精确。
- 建议：Abstract 中 "78.9% of non-tie routing labels" 前增加 "episode-level"。

**[AGREE with nuance x2] W3: Router negative result 的 signal-limited vs data-limited 区分不完全**
- 来源：R1-W3 + R2-W2
- R2 REBUT R1 的 "架构简单" 批评（6 种变体 + LOTO + death-proximal labeling），但 AGREE paraphrase augmentation 不增加新 routing signal，真实 episode-level scaling 未测试。
- 建议：§5 更对称呈现两种解释，明确当前数据量不足以完全区分。

**[AGREE x2] W4: K=11 cluster bootstrap 局限性未在主文充分标注**
- 来源：R1-W1
- 建议：Limitations 显式引用 Cameron et al. K≥20-50 建议。

**[AGREE x2] W5: 72B scaling 仅做 probe 不够完整**
- 来源：R1-W4
- 建议：Limitations 中标注 72B scope 限制；讨论更强模型下 non-death signal 是否可能超过 death signal。

**[AGREE x2] W6: "Death" 术语限制 generality — graded failure 适用性未讨论**
- 来源：R2-W5
- 建议：Discussion 增加 1-2 句讨论 graded failure 场景。

**[AGREE partially] W7: 缺与 concurrent routing methods 的定性讨论**
- 来源：R2-W4
- 建议：§5 或 §4 增加 2-3 句讨论 CogRouter/ARES/MTRouter 在 death-dominated 环境中的预期表现。

### Minor（5 项）

- **M1**: Figure 2 仅 11 点无 task name label [AGREE x2]
- **M2**: §1 Introduction "signal diversity can collapse" 重复出现 [R2]
- **M3**: Pages 7-8 连续两页纯文本无 display item [视觉审查]
- **M4**: Missing references: Alshiekh et al. (2018) Safe RL via Shielding, Geifman & El-Yaniv (2017) Selective Classification, Schuster et al. (2022) CALM, Raposo et al. (2024) Mixture-of-Depths [R1+R2 共 4 条]
- **M5**: Related Work 缺 non-agent adaptive computation (early exit, speculative decoding) [R1-M6, R2 AGREE]

---

## Reviewer Consensus

以下问题双方达成完全共识 [AGREE x2]：
1. DAF P-dependence 是最需要作者回应的 critical issue（label fraction 应为 primary metric）
2. "Deterministic" 跨环境语义不同需更精确限定 transfer claim
3. 63% task 排除率需更充分正文 justify
4. K=11 cluster bootstrap 局限需显式标注
5. 72B 实验 scope 有限
6. 论文鲁棒性验证水平在 analysis track 中属上乘（20 appendices）
7. 负面结果报告（router failure）诚实且有价值
8. Cross-model convergence（3 family, DAF 88-90%）有力排除模型特异性

## Reviewer Divergence

**Episode→step 粒度失配的严重程度**：
- R1 评为 critical：Title/Abstract scope 超出方法论覆盖范围
- R2 评为 minor framing issue：论文 claim 是关于 "signal composition" 而非 "step-level decision"，episode-level 是 principled granularity
- R2 提供的反驳依据：(1) §2.2 论证了 97.4% step ties 使 episode-level 成为唯一有效粒度；(2) 61.2% no-preference 也是诊断信息；(3) §3.6 和 §5 已详细讨论 step-level router failure
- **最终判定**：降为 warning —— claim validity 不受影响，但 Abstract 应加 "episode-level" 限定词

**Limitations 长度**：
- R2 评为 warning（5 段过长，建议压缩到 3 点）
- R1 REBUT（analysis 论文的诚实 limitations 是优势而非缺陷，且不占页数限制）
- **最终判定**：不列入 weakness — R1 理由充分，Limitations 内容均为必要 caveats

**Router 架构简单性是否是负结论的主要限制**：
- R1 评为 warning（仅测试 Qwen3 0.6B-4B + LoRA）
- R2 REBUT（6 种变体收敛、LOTO 打回、death-proximal labeling 无效），但 AGREE scope 限定可更精确
- **最终判定**：保留为 W3 的子问题，建议更对称呈现双解释

---

## Questions to Authors

1. **P=0 下 78.9% label fraction 的稳定性**：论文声称 label fraction 是 P-invariant 的，但 §3.1 提到 54 个 "sole-signal labels" 在 P=0 时退化为 ties——这意味着 P=0 下 label fraction 会从 78.9% 降低。Algorithm 1 的 death-first priority 等价于隐式无穷大 penalty，这与 "penalty-independent" 叙事存在微妙张力。请澄清。
2. **150 个 no_pref episodes 的 action sequence 相似度**：两策略在相同 outcome 下是否采取了相似路径？如果路径不同但结果相同，可能存在被 episode-level aggregation 掩盖的 step-level routing signal。
3. **72B 条件下 non-death signal 是否增强**：72B 的 death rate 降至 30.6%，意味着更多 episodes 双方存活。$\Delta_{\text{nd}}$ 是否在 72B 上显著增大？如果是，death dominance 的 scale-robustness 结论是否需要 qualify？

---

## Missing References

- Alshiekh et al., "Safe Reinforcement Learning via Shielding" (AAAI 2018) — Appendix O action-space filtering 本质是简化版 shield [R2, R1 AGREE]
- Geifman & El-Yaniv, "Selective Classification for Deep Neural Networks" (NeurIPS 2017) — selective prediction 经典，与 routing/abstention 概念关联 [R2, R1 AGREE]
- Schuster et al., "Confident Adaptive Language Modeling" (NeurIPS 2022) — non-agent adaptive computation baseline [R1, R2 AGREE]
- Raposo et al., "Mixture-of-Depths" (ICML 2024) — per-token computation allocation [R1, R2 AGREE]

---

## External Review

未请求（项目未配置 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check（非评分项）

视觉审查已完成。3 warnings, 14 info。

**Warnings**:
1. **Pages 7-8 连续两页纯文本**：§3.6 (Router Training) + §4 (Related Work) + §5 (Discussion) + §6 (Conclusion) 无任何 display item，阅读节奏单调。建议 §3.6 router 结果可用小 table 呈现。
2. **Page 9 Limitations 篇幅较大**：5 个子段落几乎填满整页。（但 Reviewer 圆桌讨论认为此内容均为必要 caveats，不建议删减。）
3. **Page 24 末页空白**：附录末页仅约 1/4 内容，空间利用率低。

**正面发现**：
- 全文无 LaTeX 渲染错误、margin 溢出或 section heading 孤悬
- 双栏排版间距均匀，行号完整（submission 格式正确）
- 主体正文 8 页含 5 个 display items（Figure 1-3, Table 1-2），对诊断型论文属合理范围
- 所有 table 使用 booktabs 风格，格式规范
- Figure 3 使用 shaded error bands，可视化实践良好
- 颜色语义跨图一致

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

**评分理由**：

论文在 ScienceWorld 环境内做了一项极其详尽的诊断分析——20 个 appendix 的鲁棒性验证、3 个模型家族的 cross-model replication、router training 负结论的多层论证——在 methodological rigor 上无可挑剔。78.9% death-asymmetric label fraction 作为 penalty-independent 的核心发现是可靠的，cross-model convergence（spread 2.2pp）有力排除了模型特异性。

但以下结构性限制将论文定位在 Findings 而非 main conference：

1. **Excitement deficit（R1 3/5, R2 3/5）**：核心发现——在有 catastrophic failure 的环境中 death avoidance 主导 routing signal——具有一定的 a priori 可预测性。当一种策略有 oracle access 而另一种策略会"死"时，oracle 更安全是 expected 的。论文的贡献在于量化了这一直觉（78.9%）并系统排除了 alternative explanations，但 insight 的 surprise value 有限。
2. **DAF 度量的数学 artifact**：核心度量之一（DAF=90.4%）部分由 P=100 的选择决定（P=10 时仅 50.4%），虽然 label fraction 提供了 P-invariant 的补充，但主文对 P-sensitivity 的透明度不足。
3. **单环境主体验证**：完整验证仅在 ScienceWorld 上完成，MATH 和 ALFWorld 只是 boundary probes（且 "deterministic" 含义不可比）。框架的 methodological generality 合理，但 empirical generality 证据不足。
4. **Actionability gap**：框架是 diagnostic 而非 prescriptive——诊断出 death dominance 后的 practical next step（除了 "用 always-deterministic"）不够清晰。

综合两位 Reviewer 独立评分均为 3.5 (Borderline Conference)，考虑到 excitement deficit 是持续存在的结构性限制（从 Round 16 至今），且 Must-Fix 问题均为 framing 层面（可修但不改变核心 contribution 的 novelty），判定为 **3.0 (Findings)**——论文质量足以被 Findings 接收，但核心 contribution 的 novelty 和 generality 尚不足以推荐 main conference。

---

## Detailed Comments

### §1 Introduction
- "signal diversity can collapse to a single dominant mechanism" 在 para 5 和 contributions list item 2 中重复出现，措辞几乎相同——合并或删除一处。
- Contributions 列表三项，每项内容过长（item 2 跨 3 行），建议精简。

### §2 Method
- §2.4 DAF 定义后应立即讨论 P-sensitivity，至少引用 P=10 (50.4%) 和 P=50 (82.6%)。当前叙事在此处建立了 DAF 的重要性，但读者要翻到 Appendix K 才发现 90.4% 有数学 artifact 成分。
- §2.1 "deterministic" operationalization 差异已描述，但应更明确标注"这些定性差异影响框架能检测到的 routing signal 类型"不仅是 caveat，而是 cross-env 分析的核心前提。

### §3 Experiments
- §3 第一段 63% 排除率应展开。建议增加一段：(1) excluded tasks ΔDR=+38.2 > included +28.7 pp；(2) taxonomic redundancy 操作定义；(3) agent-floor tasks 排除的合理性。
- §3.1 Figure 2 scatter plot：11 点 + r=0.97 的 structural consequence caveat 可以更 prominent（当前在 caption 末尾）。建议加 task name label。
- §3.4 ALFWorld 分析仅一段话，作为三个 cross-env probes 之一显得单薄。至少应引用 Appendix L 的 Table/Figure。
- §3.6 Router training 负结论 scope 可更精确——"no step-level learnable signal exists under current architectures and data regime" 中 "current architectures" 应明确列出（Qwen3 0.6B-4B with LoRA）。

### §4 Related Work
- 缺 non-agent adaptive computation 方向（early exit: CALM; per-token allocation: Mixture-of-Depths）。
- Appendix O 的 action-space filtering 本质是 shielding——应引用 Alshiekh et al. (2018)。

### §5 Discussion
- Paragraph 1 "signal-limited" 解释应与 "data-limited" 更对称呈现。当前叙事倾向 signal-limited（Interpretation B），但 9 个 internal-preferred 样本 + paraphrase-only augmentation 不足以完全排除 data-limited。
- 增加 2-3 句讨论 concurrent routing methods（CogRouter, ARES, MTRouter）在 death-dominated 环境中的预期表现。
- 增加 1-2 句讨论 graded failure（非 binary death/alive）场景下框架的适用性。

### §6 Conclusion
- "the diagnostic procedure transfers" 需加限定：transfer 的是 procedure 而非 operationalization。

### Limitations
- Statistical limitations 段应显式引用 Cameron et al. (2008) K≥20-50 建议。
- 增加 72B 实验 scope 限制的说明。