---
round: 23
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T06:34:06.259196+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 23 审稿报告

**Venue**: EMNLP 2026 (ARR)  
**论文**: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"  
**Reviewer**: R1 (技术严谨性 + 实验设计) + R2 (新颖性 + 社区适配性)  
**交叉回应**: 完成。R1 对 R2 的 11 点：AGREE 8 / REBUT 3。R2 对 R1 的 8 点：AGREE 6 / REBUT 2。  
**收敛**: 第 1 轮达成。两位 Reviewer 评分一致（3.5），核心关切高度重叠，分歧仅在 2 个 minor 点上（SE propagation 和 F-L 比较 fairness）。

---

## Summary

论文推导了 LLM 标注异质处理效应 (HTE) 中的精确偏差恒等式：当 LLM 分类器的误差率在子群间不均匀时，标准的 global confusion-matrix correction 会引入 δ_s·Δτ/(1−2π̄) 形式的子群偏差，甚至可能反转 CATE 的符号方向。论文提供了层级贝叶斯 per-subgroup 校正方法，刻画了操作条件（Δπ>0.15, n_expert/K≥50, K≤4），并提出了仅基于误差率即可判断 global correction 是否有害的诊断准则。实验覆盖 192 个合成配置和 11 个真实 LLM confusion matrix。

---

## Strengths

**S1: 数学严谨性 [R1+R2]**  
Theorem 1 的 exact bias identity 提供了 closed-form 分解，无渐近余项，在 symmetric case 下形式优美（δ_s·Δτ/(1−2π̄)），且推广到了任意非对称 confusion matrix 的 full-matrix 形式。合成验证 R²=0.994 (K=2) / 0.97 (K=4)。

**S2: 全面的模拟实验 [R1+R2]**  
6 Δπ × 8 n_expert × 2 K × 2 DGP = 192 synthetic configs + 16 empirical LLM CMs (8 LLMs × 2 datasets) + 4 NLP tasks (sentiment, hate speech, stance, topic)。Robustness validations 覆盖 8 个条件（asymmetric errors, subgroup misspecification, treatment-dependent misclassification 等），均 ≥89.5% coverage。

**S3: 诚实的操作条件 [R1+R2]**  
Section 5.4 坦率声明方法局限（K>4 退化、n_expert/K<50 RMSE 超过 global、Δπ<0.15 时无优势），在 ML 论文中少见。Figure budget_compact 清晰展示 crossover point。

**S4: 实用的诊断准则 [R1]**  
Proposition 5 的 Δτ-free diagnostic 允许仅从误差率判断 global correction 是否有害，无需估计处理效应本身。对应用研究者有直接价值。

**S5: 时效性 [R1+R2]**  
LLM-as-annotator 正快速普及，异质误差率下 global correction 的隐患是一个真实且被低估的风险。Sign-reversal insight 对政策评估、A/B 测试等场景有实际警示作用。

---

## Weaknesses

### Critical

**W1 [R1+R2 共识]: 缺乏 fully real-data validation——所有实验 semi-synthetic，核心假设 A1 由构造满足**

所有实验的 DGP 构造性地满足核心假设（特别是 A1: treatment-independent misclassification），使得论文无法验证方法在假设近似（而非精确）满足时的鲁棒性。Sensitivity analysis (γ_T=0.10 致 coverage 从 95% 降至 75%, Appendix Z.3) 实际上暴露了方法的脆弱性而非证明了鲁棒性——真实 NLP 场景（如 hate speech detection 中 toxic content 系统性影响 LLM accuracy）完全可能达到此量级的 A1 violation。

R2 补充：一个 real-data case study 可间接评估 A1 在实践中的合理性。两位 Reviewer 均认为此为论文的核心缺陷。

**W2 [R1+R2 共识]: 有限样本余项 κ²/κ 在主文与附录间不一致**

- theory.tex L92: "R_n = O_p(n_expert^{-1/2} · κ(C_s)²)" —— κ 平方，基于 Neumann expansion
- appendix.tex L103: "||M̂_global^{-1} M̂_s − M_global^{-1} M_s|| ≤ κ(M_global) · O_p(n_expert^{-1/2})" —— κ 一次幂

R2 指出：两个 bound 作用于不同对象（主文 bound Ĉ_s^{-1} perturbation vs 附录 bound M_global^{-1} M_s 乘积 perturbation），所以不是直接数学矛盾。但论文未解释这个区别。在一篇以理论严谨性为核心卖点的论文中，这是明显的 presentation 缺陷。

**W3 [R2 主张, R1 间接支持]: 理论新颖性深度有限**

核心数学 machinery（confusion matrix 的矩阵求逆、子群分层）是 measurement error econometrics 的标准工具。从 Frazis-Loewenstein (2003) scalar attenuation 到 Theorem 1 subgroup-heterogeneous bias identity 的推广在技术上是 relatively straightforward（matrix generalization of scalar case）。Sign-reversal insight 是新的 practical contribution，但数学创新有限。两位 Reviewer 共识：贡献定位为 "careful application of known techniques to an important new context"，而非 methodological breakthrough。

R1 通过 Frisch-Waugh-Lovell 类比进一步限制了 novelty 声称——子群分解可视为 FWL partialing 的特例。

### Warning

**W4 [R2 主张, R1 未直接讨论]: EMNLP venue fit 可疑**

论文本质是 causal inference methodology paper。NLP 内容（LLM confusion matrices, text classification tasks）作为 application domain 而非方法论贡献。EMNLP 审稿人可能缺乏 econometrics 背景来充分评估理论贡献，且论文未提供推进 NLP 方法本身的 insight。更适合 JCI / UAI / AISTATS。

R1 未直接讨论 venue fit 但同意 novelty 对 EMNLP 偏弱。CivilComments NLP insight 段落（§5.2）是正面尝试但不改变论文的根本定位。

**W5 [R1 主张, R2 同意]: R²=0.76 lower bound 削弱 "exact" framing**

Abstract 声称 R²≥0.97 但括号内即承认 per-model range 0.76–0.99。R²=0.76 意味着 identity 仅解释 76% 的 observed bias variance——对一个 "exact identity" 来说，24% 的未解释方差不可忽略。论文未对低 R² 的 LLM 做 failure analysis（是 finite-sample noise 还是 assumption violation？）。

**W6 [R1 主张, R2 同意]: 诊断 AUC=0.86 (symmetric) 缺乏 decision-consequence 分析**

Symmetric case 下 AUC=0.86 意味着非平凡的误判率。更关键的是，论文未讨论 FP/FN 的不对称代价：在 causal inference 中，false negative（诊断说 global correction 安全但实际导致 sign reversal）的后果远重于 false positive（不必要的 variance 增加）。建议提供 precision/recall breakdown 和不同 decision threshold 下的 tradeoff 分析。

**W7 [R1 主张, R2 同意但建议降级]: MC=100 不足以支撑 coverage 声称**

SE≈2.2pp 使得 93% vs 95% coverage 的区分变得模糊。R2 认为核心 claims (bias reduction 7.4×, sign reversal elimination) 不依赖精确 coverage，可降级为 info。但论文确实做出了显式 coverage claims（Table 1, Section 5.3），在 MC=100 的精度下这些 claims 不 well-supported。

**W8 [R2 主张, R1 同意]: "Debiasing hurts" framing 有过度声称风险**

标题和整体 framing 暗示 debiasing 普遍有害，但论文表明这仅在 extreme heterogeneity 下成立。Moderate heterogeneity 下 global correction 仍有益（"methods converge, p>0.05", experiments.tex L43）。Headline claim 7.4× bias reduction 仅限 extreme DGP。Framing 应更精确地限定适用条件。

**W9 [R2 主张]: Subgroup-dependent vs instance-dependent noise 定位不足**

论文的噪声模型（subgroup-dependent misclassification）介于标准 class-conditional noise 和更一般的 instance-dependent noise 之间，但未在 noisy label learning 文献中定位此关系。Related work 已增加噪声标签段落但深度不足。

### Minor

**W10 [R1 主张, R2 REBUT]: SE 不 propagate CM 估计不确定性**

Plug-in SE 公式 (method.tex L34) 将 Ĉ_s 视为已知量。R2 反驳：bootstrap (B=100) 恢复 ≥95% coverage，HB partial pooling 隐式 regularize CM uncertainty，是 pragmatic implementation choice with empirical justification。两位 Reviewer 分歧——R1 认为 delta method 或 full posterior propagation 更 principled，R2 认为 bootstrap 已足够。

**W11 [R1+R2 共识]: Abstract 信息密度过高**

12+ 具体数字在 6 句话中。Abstract 读起来像 results table 而非 narrative summary。Camera-ready 应精简。

**W12 [R2]: "Debiasing" 术语歧义**

标题中 "debiasing" 在 NLP 社区有 fairness 歧义。Footnote 1 已澄清但标题仍易误读。

---

## Questions for Authors

**Q1 [R2→R1 AGREE]**: Theorem 1 的 bias identity 与 Frisch-Waugh-Lovell decomposition 的关系？如果子群分解可视为 FWL partialing 的特例，请阐明增量贡献。

**Q2 [R2]**: 在观察性研究中，propensity score estimation error 与 CM estimation error 如何交互？Identity 在 joint estimation error 下是否仍然成立？

**Q3 [R2→R1 REBUT]**: Δπ>0.15 阈值是否有理论推导（例如可从 identity + decision theory 导出），还是纯粹来自模拟网格的经验发现？R1 认为有理论依据。

**Q4 [R1→R2 AGREE]**: Headline claims (7.4× bias reduction, 14.9% sign reversal) 在 moderate heterogeneity 下对应什么数字？如果 moderate 下改善甚微，practitioners 应如何解读贡献的实际影响范围？

---

## Missing References

1. **Filtered PPI** (arXiv:2602.10464) — selective prediction-powered inference with noisy LLM annotations，高度相关。R2 识别；R1 表示无法独立验证但认为 plausible。
2. **Subgroup-dependent noise 文献** — 论文介于 class-conditional 和 instance-dependent noise 之间，应引用该中间地带的关键工作。

---

## External Review

**状态：未请求。** 本轮未启用 Stanford Agentic Reviewer。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（2026-05-25 06:10–06:14, 耗时 ~4min）。0 critical, **4 warning**, 9 info。

**Warnings:**
1. **p.9**: Figure 4（bias amplification heatmaps）漂移到 References 页——正文 Section 5.3 引用但 float 越界。建议缩小 Figure 3 或 Table 1 空间，将 Figure 4 拉回 p.8，或移入 Appendix。
2. **pp.4-6**: 连续 3 页纯文本+公式（理论推导核心段落可豁免但跨度偏长）。建议在 Section 4 前插入概念性小图。
3. **p.8**: 极度拥挤——Figure 3 + Table 1 + §5.4 + Conclusion + Limitations 全挤一页。Conclusion 仅 ~12 行，Limitations 被压到页底。
4. **pp.1-8**: 正文仅 4 display items（推荐 5-8），Figure 4 已漂出正文。

**Positive notes**: Figure 2 pipeline 对比图设计清晰（全文最佳 display item）、Table 1 booktabs 格式专业、无 margin 溢出/公式渲染错误/LaTeX 残留、Appendix 22 页排版整洁。

---

## Overall Assessment

**评分：3.5 — Borderline Conference**

| 维度 | 评价 |
|------|------|
| Soundness | 强。Exact identity 数学正确，实验全面，操作条件诚实声明。 |
| Significance | 中。解决真实问题（LLM 异质误差下 global correction 危害），但核心受益群体是 causal inference 应用研究者，非 NLP 方法论研究者。 |
| Novelty | 弱-中。F-L scalar → subgroup-heterogeneous matrix 推广技术上 straightforward。Sign-reversal practical insight 新颖但数学创新有限。 |
| Clarity | 中。理论展开清晰，但 κ²/κ 不一致、Abstract 过密、"debiasing" 歧义等 presentation 问题存在。 |
| Venue fit | 弱-中。本质为 causal inference methodology，NLP 内容为 application domain。EMNLP 可行但非最优 venue。 |

**核心判断**：论文在 soundness 上无重大缺陷（R22 修正 AUC 0.66→0.96 消除了最大技术隐患），实验设计全面且操作条件声明透明。但三个结构性问题限制了评分上升空间：(1) 所有实验 semi-synthetic 且 A1 by construction——sensitivity analysis 暴露脆弱性而非鲁棒性；(2) 理论新颖性对 EMNLP 偏浅；(3) venue fit 可疑。论文有被 Findings 接收的潜力，Conference (main) 接收需要在 rebuttal 中有力回应 novelty depth 和 real-data validation。

**Rebuttal 关键问题（按优先级）**：
1. 是否有 real-data case study 或 A1 violation 的实证证据说明方法在实践中的适用性？
2. 相对 F-L (2003) 和 standard measurement error correction 的数学增量贡献是什么？FWL 类比如何回应？
3. R²=0.76 的 failure analysis：原因是什么，是否可预测哪些 LLM 的 identity 拟合较差？
4. 诊断 AUC=0.86 在 decision-theoretic framework 下的推荐 threshold 是什么？

**两位 Reviewer 一致评分 3.5 (Borderline Conference)**，核心分歧仅在 SE propagation（R1 认为不充分 vs R2 认为 bootstrap 已解决）和 F-L 比较 fairness（R1 认为 strawman vs R2 认为比较合理）两个 minor 点上，不影响 overall assessment。

---

## Detailed Comments

**[theory.tex L92 vs appendix.tex L103]** κ²/κ 不一致。主文正确使用 κ² (Neumann expansion)，附录使用 κ (perturbation bound on M_global^{-1} M_s)。两者作用于不同对象，但论文未说明区别。统一表述或增加解释。

**[abstract.tex L4]** "R² ≥ 0.97 on synthetic grids (R² = 0.975 in aggregate across 11 real LLM confusion matrices; per-model range 0.76–0.99)"——括号内的 0.76 下界与 "exact" 声称张力过大。建议：(a) 对 R²<0.90 的 LLM 做 failure analysis，(b) 将 per-model range 移至正文 §5.2 讨论而非 abstract。

**[experiments.tex L43]** "Under moderate heterogeneity, methods converge (p > 0.05)"——这句话实际上削弱了标题 "When Debiasing Hurts" 的普遍性。建议在 Abstract 或 Introduction 中更明确地限定：debiasing hurts **only under extreme subgroup heterogeneity**。

**[method.tex L34]** Plug-in SE formula se_corrected = √(diag(Ĉ_s^{-1} diag(se²) Ĉ_s^{-T}))。虽然 bootstrap 恢复 coverage，但应在方法描述中明确 plug-in SE 的局限性和 bootstrap 的必要性条件（n_expert/K < 50 时）。

**[Proposition 5 诊断]** AUC=0.86 (symmetric) 有实用价值但需 decision-theoretic framing。建议补充：precision@recall=0.95 是多少？推荐的保守 threshold（偏向低 FNR）是什么？

**[Section 5.4 operating conditions]** K≤4 限制。R2 的问题有建设性价值：K>4 退化是因为 n_expert/K 不足（给定足够 expert budget 可解决）还是 hierarchical prior 的结构性局限？答案决定了方法的可扩展性前景。建议在 Limitations 中区分。

**[Layout]** Figure 4 漂出正文是 camera-ready 必须修复的排版问题。p.8 的拥挤程度（Conclusion 仅 ~12 行）给审稿人 "草率收尾" 的印象。建议将 Figure 3 或 Table 1 的部分细节移入 Appendix。