---
round: 15
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T12:50:48.342325+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 15 审稿报告（修订版 — 双向交叉回应完成）

**Target Venue**: EMNLP 2026 (ARR)
**Paper**: EC-HTE: Error-Corrected Heterogeneous Treatment Effect Estimation under LLM Annotation Misclassification
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 理论基础)
**交叉回应**: ✅ 完成。R1↔R2 双向交叉均已提交。通过事实验证解决 4 项分歧，通过 Director 裁定解决 2 项严重程度争议。

---

## Summary

本文提出 EC-HTE，一个基于 hierarchical Bayesian confusion matrix estimation 的框架，用于纠正 LLM 标注中的 subgroup-heterogeneous misclassification 对异质处理效应 (HTE) 估计的偏差。核心贡献包括：(1) 精确偏差恒等式 (Theorem 1) 揭示全局纠正在异质误差下可能放大偏差；(2) 基于 subgroup-specific confusion matrix 的分层贝叶斯纠正方法；(3) 无需 ground-truth CATE 的适用性诊断 (Proposition 5)。实验覆盖 520 种合成配置 + 11 个真实 LLM confusion matrix + 2 个真实文本数据集。

---

## Strengths

1. **理论贡献扎实**: Theorem 1 将偏差分解为精确恒等式（非上界），揭示 Δπ × Δτ 交互项导致全局纠正可能适得其反——这是一个此前未被正式化的洞察，对该领域具有指导意义。

2. **实验设计全面**: 520 种合成配置（K∈{2,4}, 多种 heterogeneity regimes, 多种 expert budgets）+ 11 个真实 LLM confusion matrix + Hate Speech/Civil Comments 真实文本 pipeline。覆盖度在该领域属顶尖水平。

3. **PPCI 互补性验证**: 4-DGP 正交设计清晰展示 EC-HTE 与 PPCI 的互补性——covariate-side vs outcome-side 纠正的独立贡献。正文 + Appendix L + Appendix U 提供多层次证据。

4. **假设放松稳健性**: (A2) 对称、(A3) 等概率、(A5) effect modifier 独立性的联合违反下仍保持 coverage ≥ 0.93，展示了方法的实用鲁棒性。

5. **诊断工具实用性**: Proposition 5 提供无需 ground-truth CATE 的适用性判断，诊断 AUC 在合成数据达 0.86——为实践者提供了可操作的决策支持。

---

## Weaknesses

### Must-Fix (1 项)

**[M1] (A2) 对称误分类假设的实用局限 [共识: R1+R2，双向交叉确认]**

论文的核心实验在 symmetric misclassification 下进行了 520 种配置的全面验证，但 asymmetric 场景（实际中更常见）仅在 Appendix J 测试了 3 种配置且仅 K=2。覆盖度差距为 520:3。

R1 补充关键证据：Table 11 (p.20) 中 4 个开源 LLM 的真实混淆矩阵**全部**呈现 FPR≠FNR，直接说明 (A2) 在实际部署中不成立。Appendix J Eq.(22) 给出的充分条件 max(FPR_s, FNR_s) > max(FPR, FNR)/2 过于宽松，对应 AUC 仅 0.66，不构成实用诊断。

论文声明方法"不依赖 (A2)"（method.tex），但诊断（Proposition 5）在 asymmetric 下的可靠性缺乏充分实证支撑。

**要求**: 
- 扩展 asymmetric 实验到合理覆盖度（≥10-20 configs，覆盖 FPR/FNR 差异 0.05-0.20 范围）
- OR 正文显著讨论诊断在 asymmetric 下的退化程度（定量）
- 给出比 Eq.(22) 更紧的 asymmetric 诊断充分条件

### Should-Fix (7 项)

**[S1] 操作条件限制实用范围的讨论不够清晰 [共识: R1+R2, R2 有保留]**

论文实验覆盖 K≤4, n_expert≥250, Δπ>0.15。虽然 Corollary 6 将理论推广到任意 K，Appendix I.2 测试了 K=5，但正文未清晰区分"理论适用范围"与"已实验验证范围"。实践者难以判断自己的场景是否在方法的可靠工作区间内。

**要求**: Section 5.4 或 Limitations 加段落明确区分两者，并给出"已验证边界之外的外推风险"的定性讨论。

**[S2] 缺乏真实因果数据端到端验证 [R1: must-fix → Director 裁定: should-fix]**

论文无 ground-truth individual-level CATE 的真实数据验证。Director 裁定：这是因果推理方法论文的领域固有困难（Wager & Athey 2018, Kennedy 2023, Zrnic & Candes 2024 等标杆均使用合成/半合成验证），不应要求本文超越领域标准。R2 提供了充分论证支持降级。

**要求**: Limitations 中用 2-3 句明确承认此局限，讨论为何 ground-truth CATE 在观察性研究中不可得，以及未来通过 RCT subgroup analysis 验证的可能路径。

**[S3] 多步误差传播缺乏形式化分析 [共识: R1+R2]**

EC-HTE 的 pipeline 涉及 CM estimation → moment correction → CausalForest/R-learner，每一步的估计误差如何传播到最终 CATE 估计缺乏端到端的形式化界。论文通过 bootstrap SE 和 plug-in SE 提供了实证估计，但无 formal bound。

**要求**: 在 Limitations 或 future work 中讨论形式化误差传播分析的方向。对于 EMNLP（非统计学期刊），实证 SE 验证可接受但需承认此理论缺口。

**[S4] 代码开源承诺不明确 [共识: R1+R2]**

代码开源声明仅出现在 Appendix 末尾 (p.31) 一句话。正文无任何提及。对 reproducibility 的承诺不够显著。

**要求**: Introduction 末尾或 Section 5 开头加一句代码/数据开源承诺。

**[S5] 与 Blette et al. (2023) 的区分需更尖锐 [共识: R1+R2]**

当前 Related Work 中仅用一句话区分 Blette et al.（"our setting involves systematic label noise adopting confusion-matrix-based correction"），但两者的核心问题高度重叠——都研究 effect modifier misclassification 如何偏差 HTE 估计。

关键技术差异（需明确阐述）：(a) Blette 使用 multiple imputation 而非 CM 求逆；(b) Blette 针对 cluster-RCT 而非观察性研究中的 LLM 标注场景；(c) 本文提供封闭式偏差刻画（Theorem 1），而 Blette 的方法是模拟驱动的。

**要求**: Related Work 中将 Blette et al. 区分扩展为 2-3 句，涵盖上述三个维度。

**[S6] 遗漏 Northcutt et al. (2021) "Confident Learning" [共识: R1+R2]**

EC-HTE 的混淆矩阵估计步骤与 Confident Learning 的核心思想（从噪声标签估计 joint distribution of noisy and true labels）有直接关联。这是 label noise 领域的高引标杆文献（8000+ citations），遗漏影响文献覆盖完整性。

**要求**: Related Work 或 Method 中引用并简要说明与 EC-HTE CM estimation 步骤的关系。

**[S7] 遗漏 Tan et al. (2024) LLM annotation survey [共识: R1+R2]**

EMNLP 2024 Oral，是 LLM-as-annotator 方向的系统综述。作为本文研究方向的重要背景文献，应被引用。

**要求**: Introduction 或 Related Work 引用。

---

## Questions

1. **(A1) 条件独立性假设的可验证性** [R1+R2 共识]: Section 3 假设 LLM 误差独立于 ground truth（给定子群）。此假设不可直接检验。R1 给出具体违反场景：在情感分析中，LLM 的分类准确率受文本情绪强度影响，而情绪强度又与处理效应相关时 A1 被违反。论文是否考虑过基于 multiple LLMs 的间接验证策略（如 consistency across annotators as proxy for independence）？

2. **低资源场景 MCMC 收敛** [R1+R2 共识]: Appendix G Table 2 仅报告主实验配置的收敛诊断。K=4, n_expert=25 per subgroup 的极端场景，Dirichlet 后验极度依赖先验，posterior 是否能充分探索？R̂ 和 ESS 数据？

3. **Subgroup 定义为连续变量离散化时的敏感性** [R1 提出, R2 补充]: Appendix P 展示 subgroup misspecification 时方法 graceful degradation 到 global correction。但如果子群是年龄（连续）的离散化，切分点选择是否显著影响结果？

4. **Civil Comments 中 A3 违反** [R1 补充]: Civil Comments 的 toxicity 标签分布可能高度不平衡（toxic comments 是少数）。若 Z 是 toxicity label 则 A3（P(Z=0)=P(Z=1)=0.5）明显被违反。Appendix S 的 class imbalance 敏感性分析是否具体覆盖了 Civil Comments 的实际分布？

5. **AI 辅助范围** [R2 提出, R1 同意]: p.31 声明使用 Claude 进行代码编写和 LaTeX 写作。应明确 AI 是否参与了理论推导或实验设计决策。

---

## Missing References

| 文献 | 优先级 | 理由 | 共识 |
|------|--------|------|------|
| Northcutt et al. (2021) "Confident Learning" | 高 | CM estimation 与 CL 核心思想直接关联 | R1+R2 |
| Tan et al. (2024) LLM annotation survey, EMNLP Oral | 高 | 本方向最重要的综述背景 | R1+R2 |
| Negi & Wooldridge (2025) "DiD with Misclassified Treatment" | 低 | 同一测量误差大家庭但方向不同（treatment vs effect modifier） | R1 部分同意 |
| Gentzkow et al. (2019) "Text as Data" | 可选 | 经典综述但与本文焦点关联有限 | R1 认为非必需 |

---

## External Review

**状态**: 未请求。

---

## Visual Layout Check (非评分项)

**状态**: ✅ 完成 (2 warnings, 19 info)

**Warnings**:
1. **⚠️ 页数合规性存疑 [R1+R2+视觉审查三方确认]**: Section 5 在第 8 页结束，Section 6 (Conclusion) 在第 9 页开始。EMNLP 2026 long paper 限 8 页主文（Limitations/Ethics 不计）。如 Conclusion 属于主文（非 Limitations 的一部分），则正文约 8.2 页，**构成格式违规**。需作者精确确认并在必要时压缩。
2. Pages 1-2 无 display item（连续纯文本）——Intro+Related Work 区间常见模式，影响有限。

**Positive findings**: 排版整洁专业，Figure 1 和 Figure 2 传达有效，Table 1 booktabs 格式规范，公式渲染正确，无 LaTeX 残留错误。

---

## Overall Assessment

**Score: 3.5 — Borderline Conference**

**R1**: 3.5 | **R2**: 3.5 | **Director**: 3.5

**理由**: 论文在理论贡献（精确偏差恒等式）和实验全面性上达到会议水准。PPCI 互补性和多 LLM 验证是亮点。但 (A2) 对称假设的实用局限是唯一的 must-fix 问题——asymmetric misclassification 在实际 LLM 部署中几乎是默认情况，仅 3 configs 的验证远不充分。如果这一问题能在 rebuttal/revision 中得到充分回应（扩展实验或显著讨论退化），论文有望升至 4.0 (Conference)。

**接收建议**: Borderline。修改后可达 Findings，有望 Conference（取决于 M1 的回应质量）。

---

## Detailed Comments

### 交叉回应裁定汇总

**R1 对 R2 的回应裁定:**

| R2 编号 | 内容 | R1 回应 | Director 最终裁定 |
|---------|------|--------|-----------------|
| R2-N1 | A2 假设讨论不足 | AGREE | Must-Fix (共识) |
| R2-N2 | 方法新颖性定位不清 | REBUT (非 must-fix) | ⬇️ 维持 warning，不升级 |
| R2-W1 | Blette et al. 区分 | AGREE | Should-Fix (S5) |
| R2-W2 | 遗漏文献 | AGREE (大部分) | Should-Fix (S6, S7) |
| R2-W3 | A1 可检验性 | AGREE | Question + Limitations |
| R2-W4 | Abstract 字数 | REBUT (~190-195词) | 撤销 |
| R2-W5 | 页数合规 | AGREE (修正) | Visual Check Warning |

**R2 对 R1 的回应裁定:**

| R1 编号 | 内容 | R2 回应 | Director 最终裁定 |
|---------|------|--------|-----------------|
| R1-M1 | A2 假设局限 | AGREE | Must-Fix (共识) |
| R1-M2 | 缺真实验证 | REBUT (降级) | ⬇️ Should-Fix (S2) |
| R1-S1 | 操作条件窄 | AGREE with nuance | Should-Fix (S1) |
| R1-S2 | Imai & Yamamoto 引用不足 | REBUT (已引用) | ❌ 撤销（验证：related_work.tex:34） |
| R1-S3 | 误差传播 | AGREE | Should-Fix (S3) |
| R1-S4 | 代码开源 | AGREE | Should-Fix (S4) |
| R1-S5 | Dirichlet 先验敏感性 | REBUT (已有) | ❌ 撤销（验证：Appendix G.1, 15 configs） |
| R1-Q4 | PPCI 对比 | REBUT (已有) | ❌ 撤销（验证：method.tex + Appendix L + U） |

### 方法新颖性定位 (R2-N2)

R2 将方法新颖性列为 must-fix，R1 反驳。Director 裁定：**不升级为 must-fix**。理由：
- 论文 p.2 贡献列表已将 EC-HTE 排在第三位，前两位是理论恒等式和诊断条件
- "problem identification + characterization + practical solution" 是 EMNLP 接受的贡献模式
- 分层 Dirichlet 收缩、κ 保护、CausalForestDML 集成等设计选择有技术含量
- 维持为 warning 级别 (R2-W1 in issue tracker)

### 页数合规性风险

三方（R1 交叉回应 + R2 初审 + 视觉审查）均确认存在 overflow 风险。历史 issue (RD2-F1) 曾在 Round 4 修复过一次。当前版本需再次精确核实——如果 Conclusion 开始于第 9 页且不属于 Limitations/Ethics，则 desk-reject 风险存在。**这是需要立即验证的格式问题。**

### Rebuttal 建议方向

1. **M1 回应**: 补充 asymmetric 实验（FPR/FNR 差异 0.05-0.20 范围，≥10 configs），报告诊断 AUC 退化曲线，给出比 Eq.(22) 更紧的充分条件。
2. **S2 回应**: Limitations 加 2-3 句承认 + 讨论 RCT subgroup 验证路径。
3. **S5-S7 回应**: Related Work 补充 Blette et al. 区分 + Northcutt/Tan 引用（~3-4 句总增量）。
4. **页数**: 如有 overflow，压缩 Conclusion 或 Section 5.4 措辞。压缩 Related Work 新增内容不是选项（因为正在补引用）。