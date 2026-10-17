---
round: 22
review_mode: fresh
overall_score: 3.5-4.0
timestamp: 2026-05-25T04:57:08.574310+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 22 审稿报告（修订版——整合双方交叉回应）

> 初版报告仅基于 R2 交叉回应提交。本修订版整合了 R1 的完整交叉回应，包含 3 条实质性 REBUT 和新证据。

## Summary

本文推导了一个精确偏差恒等式（Theorem 1），揭示当 LLM 标注器的误分类率在子群间存在异质性时，全局混淆矩阵校正会引入子群级别的偏差，甚至可在 14.9% 的配置中导致 CATE 符号反转。基于该恒等式，论文提出了 Δτ-free 诊断准则（Proposition 5）和分层贝叶斯校正方法（EC-HTE），在极端异质性下将 |bias| 降低 7.4×。实验覆盖 520 合成配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验。

## Strengths

**[S1] 理论核心简洁且可验证（R1, R2 共识）**：Theorem 1 的乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 既精确又可解释，证明可手动核实。Proposition 5 的 Δτ-free 诊断（AUC=0.86 对称情形）仅凭 pilot 样本误差率即可决策——不需要估计 Δτ，这在实际部署中比恒等式本身更有价值（R2 补充）。

**[S2] 实验覆盖极为全面（R1, R2 共识）**：520 配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验，在 *ACL 投稿中属上乘水平。实验层次（合成 → 半合成 → 真实 NLP 任务 → 鲁棒性 → 跨估计器）远超同类论文（R1 强调）。跨估计器验证（CausalForest + R-learner, Table 1 + Appendix P）是额外加分项。

**[S3] 理论→方法→实践链完整（R1, R2 共识）**：从恒等式推导到 EC-HTE 方法实现再到操作边界（Section 5.4: Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4）的完整链条。Algorithm 1 伪代码清晰。"何时不用本方法"的诚实边界划定值得肯定——这在方法论论文中较为少见（R1 补充）。

**[S4] Related Work 定位清晰（R1, R2 共识）**：三维度定位（scalar attenuation vs. per-subgroup correction vs. diagnostic）清晰区分了与 Frazis-Loewenstein、DSL、PPI 等已有工作的差异。NLP × 因果推断时效性好，14.9% sign reversal 是有冲击力的 headline number。

**[S5] 假设放松讨论系统化（R1, R2 共识）**：Remark 2 对 A2、Appendix D 对 A3、Proposition 3 对 A5、Appendix H 对 A1 的系统性讨论表明作者对自身理论的局限有清醒认识。

## Weaknesses

**[W1] 对称误分类假设 (A2) 限制诊断实用性（R1, R2 共识，critical）**
两位 Reviewer 均确认 A2 是论文最大的实践局限。GPT-4o FPR/FNR 差异达 0.09（0.249 vs 0.157）。

关键澄清（R2 partial REBUT + R1 补充）：
- **恒等式**本身在非对称情形下**仍然精确成立**——乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 不依赖 A2
- **降级的是**：(a) 诊断准则 Proposition 5 AUC 从 0.86 降至 0.66；(b) 标量简化形式 δ_s·Δτ/(1−2π̄)
- **方法本身不受 A2 限制**：R1 引用 Table 36（Appendix Z.6）——非对称误差（FPR/FNR 比率高达 7:1）下 EC-HTE 仍实现 94.5% coverage（vs Global 93.0%），RMSE 从 0.083 降至 0.074
- Abstract 强调的简洁标量形式仅在 A2 下成立——这是潜在误导的来源，而非 "exact identity" 措辞本身

**[W2] 有限样本余项阶数存在技术错误（R1, R2 共识，warning）**
theory.tex L92 声称余项为 O_p(κ·n^{-1/2})，应为 O_p(κ²·n^{-1/2})。推导：(C+E)^{-1} = C^{-1} − C^{-1}EC^{-1} + O(‖E‖²)，一阶项范数 ‖C^{-1}‖²·‖E‖ = κ²·O_p(n^{-1/2})。实际影响在 κ ∈ [1.25, 3] 时有限，但必须修正。

**[W3] κ-guard 阈值 100 缺乏理论依据（R1, R2 共识，minor warning）**
最大实验 κ ≈ 1.9，阈值 100 提供 53× 安全余量从未触发。Appendix A 消融（κ sweep 10–1000）和自适应公式 κ_adapt = 10√(n_expert/K) 提供实证支持，但缺少与修正后余项的理论连接。

**[W4] 中等异质性下改善极小（R1, R2 共识，minor）**
RMSE 0.049 vs 0.050（Section 5.3, p > 0.05），7.4× 仅在极端异质性下成立。R2 认为方法的固有局限而非论文缺陷（Section 5.4 和 Figure 3 已透明展示）。

**[W5] 经验贝叶斯两阶段不确定性传播（R1, R2 共识，warning）**
EB 会低估后验不确定性。Coverage ≥ 93% 缓解但不消除。MCMC 替代方案在 Appendix G。

**[W6] 缺乏端到端真实数据验证（R2 major，R1 REBUT，核心分歧）**
R2 立场：CivilComments 无 ground-truth CATE，无法验证标题级声称 "debiasing hurts"。
R1 REBUT（5 点反驳）：
(1) 真实 CATE 基本不可观测是因果推断的根本限制，不应对本文单独加重扣分；
(2) 半合成方法（真实 LLM CM + 合成 CATE）是领域标准做法（cf. Wager & Athey 2018, Kennedy 2023）；
(3) 11 真实 LLM CM 保证了误差异质性模式的真实性——这正是论文核心关注的变量；
(4) CivilComments FPR 从 8.5% 到 21.5% 的子群异质性是真实的；
(5) Appendix R 的半真实 CM 验证 R² = 0.97，包括真实 per-subgroup FPR 和 FNR。
**Director 评估**：R1 的反驳有力。半合成是因果推断的标准验证范式。但 R2 的核心论点——标题含 extraordinary claim ("debiasing hurts") 应有 extraordinary evidence——仍有道理。此问题降级为 moderate weakness（从 R2 的 major 降至介于 major 和 minor 之间）。

**[W7] 方法论技术新颖性偏浅（R2 major，R1 REBUT，核心分歧）**
R2 立场：恒等式本质是 2×2 矩阵代数直接展开，novelty 在问题识别非技术突破。
R1 REBUT（3 点反驳）：
(1) 定理的价值在于 insight 而非证明难度——统计学中许多有影响力的结果（Frisch-Waugh-Lovell、OVB 公式）证明都简洁，但结构性洞察有深远影响。δ_s·Δτ/(1−2π̄) 的三因子交互此前未被识别；
(2) 完整理论框架超越单一定理：Theorem 1 + Proposition 3（A5 放松）+ Corollary 1（聚合偏差）+ Corollary 6（多类扩展）+ Proposition 5（诊断）+ 层级贝叶斯 + κ-guard + PPCI 组合；
(3) 非对称下方法仍有效（Table 36: 94.5% coverage）。
**Director 评估**：R1 的"insight > 证明难度"论点有实质力度。但 R2 的观察——核心数学是 M_global^{-1} M_s − I 的展开——也是事实。最终这是一个关于"理论贡献"定义的价值判断。

**[W8] Abstract 信息密度过高（R1, R2 共识，minor）**
Abstract 含 9+ 具体数字（7.4×, 14.9%, R²>0.97, AUC=0.86 等），更像 results summary。建议前半段聚焦动机，后半段精选关键数字。可修复。

**[W9] "Debiasing" 术语歧义（R1, R2 共识，minor）**
在 *ACL 社区首先联想 algorithmic fairness（gender/racial bias），与本文 measurement-error correction 含义不同。Footnote 1 有澄清但可能不够。建议 abstract 首句明确。可修复。

**[W10] Per-model R² 低端讨论不足（R1 partial agree, R2 提出, info）**
GPT-4o-mini R² = 0.893（Table 23）。论文未系统讨论哪些 LLM 特征导致拟合度下降。R1 建议增加回归分析 R² ~ f(FPR, FNR, |FPR-FNR|, n)。

## Reviewer Consensus

| Issue | R1 | R2 | 共识 |
|-------|----|----|------|
| Theorem 1 技术正确性 | ✓ | ✓ | **[AGREE]** |
| 实验覆盖面充分 | ✓ | ✓ | **[AGREE]** |
| A2 限制诊断（非方法） | W1 | W1 | **[AGREE]**（R2 确认恒等式不受影响；R1 补充 Table 36 方法仍有效） |
| 有限样本余项 κ→κ² | W2 | W2 | **[AGREE]**（技术错误，需修正） |
| κ-guard 缺理论依据 | W3 | W3 | **[AGREE]**（minor） |
| EB 不确定性传播 | W5 | W5 | **[AGREE]**（coverage ≥93% 缓解） |
| Abstract 密度过高 | W8 | W8 | **[AGREE]**（可修复） |
| Debiasing 术语歧义 | W9 | W9 | **[AGREE]**（可修复） |
| CivilComments 验证不足 | Q5 | W6 | **[AGREE]**（程度有分歧） |
| 7.4× 基线计算 | 错误 | REBUT | **R2 纠正 R1**：7.4× = 0.059/0.008，基线确为 Global |
| EB vs Gibbs 不一致 | Q4 | Q4 | **[AGREE]** |

## Reviewer Divergence

### 分歧 1：方法论新颖性深度（W7）

| | R1 (4.0) | R2 (3.5) |
|---|----------|----------|
| 立场 | Insight > 证明难度。完整框架含 6 个理论结果 + 实现 + 诊断，非孤立引理 | 核心数学是 2×2 矩阵代数展开，方法是成熟技术组合 |
| 类比 | Frisch-Waugh-Lovell、OVB 公式——简洁但有深远影响 | （无反驳此类比） |
| 评估 | **合理分歧**。两种"理论贡献"标准均有先例。R1 的 insight-driven 标准在计量经济学中更常见；R2 的 proof-difficulty 标准在数学/理论CS中更常见 |

### 分歧 2：真实数据验证（W6）

| | R1 (4.0) | R2 (3.5) |
|---|----------|----------|
| 立场 | 半合成是因果推断标准做法；真实 CATE 不可观测是领域固有限制 | 标题级 extraordinary claim 需 extraordinary evidence |
| 证据 | Wager & Athey 2018, Kennedy 2023 同用半合成；11 真实 LLM CM；CivilComments 真实异质性 | 无 ground-truth CATE = 无法验证核心声称 |
| 评估 | **R1 论据更有力**。半合成确是因果推断标准范式。但 R2 关于标题措辞的 claim 级别也值得注意——如果论文标题不含 "hurts"，这个弱点的权重会降低 |

### 分歧 3：EMNLP 受众适配性

| | R1 (4.0) | R2 (3.5) |
|---|----------|----------|
| 立场 | LLM 标注在社科/政策评估中普及，受众在扩大；4 NLP 任务覆盖主要领域 | Effect modifier misclassification 是 HTE 中的窄问题；NLP 研究者多不做 HTE |
| 评估 | **合理分歧**。取决于 EMNLP reviewer pool 的实际构成和对交叉领域论文的包容度 |

**评分分歧**：R1 = 4.0 (Conference)，R2 = 3.5 (Borderline Conference)。0.5 分差距由上述三点驱动。经过交叉回应，双方立场更加清晰但均未改变评分。

## Questions

**[Q1]** 放松 A3 (P(Z=0)=0.5) 时，theory.tex L84 提到 "the identity remains exact with modified coefficients" 但未给出显式形式。Appendix 中应提供完整推导。（R1, R2 共识）

**[Q2]** EC-HTE 与 PPCI 的理论兼容性条件？当 LLM 同时标注 effect modifier 和 outcome 时，covariate-side 和 outcome-side error 的独立性假设可能失效。（R1, R2 共识）

**[Q3]** Cov(π_s, Δτ_s) 在真实数据中的量级？Corollary 4 实际可用性的关键。应在 semi-synthetic 实验中报告。（R1, R2 共识）

**[Q4]** Method section 说 EB (<5ms)，Algorithm 1 写 Gibbs sampler (4 chains, 4000 iter)。主实验用哪个？R1 补充需澄清：(1) 主实验推断方法；(2) MCMC 和 EB 结果是否一致；(3) Table 2 的收敛诊断是验证性还是主实验。（R1, R2 共识）

**[Q5]** CivilComments："3.2× effect-size gap" 是否比 Global 更准确？无 ground-truth CATE 如何验证？（R1, R2 共识——最大 empirical gap）

## Missing References

- Filtered PPI（R1, R2 共识应引用——处理异质性预测质量与本文有概念联系）
- Egami et al. bib key `egami2024dsl` 与 year={2023} 不一致（格式错误）
- 噪声标签文献（Natarajan 2013, Patrini 2017）段落已添加但 subgroup-dependent vs instance-dependent noise 联系未建立

## External Review (Stanford Agentic Reviewer)

**状态：未请求。**

## Visual Layout Check（非评分项）

**状态：已完成**（2026-05-25 04:19–04:23）| 0 critical / 2 warning / 26 info

**Warnings:**
1. **Pages 1-2 连续纯文本**：前两页无视觉锚点，Figure 1 到第 3 页才出现。
2. **Figure 2 红绿残留**：R19 标记 resolved (sage green→blue) 但视觉检查仍检测到红/绿对比，修复可能不完整。

**Note:** R2 初审曾指出 Figure 4 浮动到第 9 页（References 区域）。R1 REBUT 验证 submitted.pdf：Figure 4 在 page 8 上半部分，在主文 8 页限制内。R2 可能看到的是不同版本或记忆有误。

**Info 摘要：** 正文 8 页 + 23 页附录；4 display items 在正文（偏低端但理论论文可接受）；Table 1 booktabs + 加粗最优值；无 overfull hbox / margin 溢出；Page 8 高密度（Figure 3 + Table 1 + Conclusion + Limitations）。

## Overall Assessment

**评分：3.5–4.0 (Borderline Conference to Conference)** | 置信度：高

| Reviewer | Score | 关键权重 | 核心 REBUT |
|----------|-------|----------|-----------|
| R1 | 4.0 (Conference) | 实验全面性 + insight-driven 贡献 + 时效性 | W6: 半合成是标准做法；W7: insight > 证明难度 |
| R2 | 3.5 (Borderline Conference) | Novelty depth + EMNLP 适配性 + 真实数据缺口 | （维持原评分，REBUTs 未改变判断） |

**综合评估：**

论文具有明确的理论贡献——偏差恒等式精确、可验证，14.9% sign reversal 有冲击力。实验覆盖在 *ACL 中属上乘。理论→方法→实践链完整。

经过交叉回应，评审的分歧更加清晰但未收敛：

**R1 4.0 的论据（经交叉回应加强）：**
- Table 36 新证据表明 EC-HTE 在非对称下仍有效（94.5% coverage），削弱了 A2 作为致命限制的力度
- 半合成是因果推断的标准验证范式，不应对本文单独加重扣分
- 完整理论框架（6 个理论结果）超越"仅问题识别"
- Frisch-Waugh-Lovell 类比有实质说服力

**R2 3.5 的论据（经交叉回应仍然有效）：**
- EMNLP 受众适配性是结构性问题（难以通过 revision 解决）
- 数学深度有限是客观事实（R1 未否认这一点，而是论证这不重要）
- 标题含 "hurts" 是 extraordinary claim，半合成验证的说服力低于真实案例

**制约评分的已确认问题（R1, R2 共识，可修复）：**
1. theory.tex L92 余项阶数 κ→κ²（技术错误）
2. EB vs Gibbs 不一致（写作问题）
3. κ-guard 缺理论推导（method gap）
4. Abstract 数字密度 + debiasing 术语歧义（表述问题）

**最终判断**：报告呈现 3.5–4.0 的评分范围。R1 的交叉回应提供了有力论据（特别是 Table 36 和半合成标准做法），使 4.0 更有依据；R2 的 EMNLP audience fit 和 novelty depth 关注在交叉回应后仍然有效。两位 Reviewer 均为严格但公正的评审。由 Research Director / AC 根据 venue 定位做最终权衡。

## Detailed Comments

### Abstract & Introduction
- ~150 words，符合 ≤200 words
- "under symmetric errors (generalizing to full-matrix form)" 措辞准确
- "7.4× under extreme heterogeneity" 限定已添加
- **需修复**：数字密度过高（W8）；"debiasing" 首次出现时明确为 measurement-error correction（W9）

### Section 3 (Theory)
- Theorem 1 技术正确。非对称下仍精确（Remark 2 + R2 确认）
- **必须修正**：L92 余项 O_p(κ·n^{-1/2}) → O_p(κ²·n^{-1/2})
- Proposition 5：应更明确阐述 (a) 不需估计 Δτ 的独特操作价值；(b) 非对称下的降级路径
- A3 放松时 theory.tex L84 声称修正系数存在但未展示

### Section 4 (Method)
- **EB vs Gibbs 不一致**：method.tex EB (<5ms) vs Algorithm 1 Gibbs (4 chains × 4000 iter)。需三项澄清
- κ-guard = 100：应与修正后余项建立理论连接
- K=4 时 Strat. MLE |Bias| (0.010) < HB (0.012)：R1 解释这是正确的 bias-variance tradeoff——HB 通过小量额外偏差换取方差降低，RMSE 在 87.5% 配置中优于 Strat. MLE（James-Stein 收缩的经典优势）

### Section 5 (Experiments)
- Table 1：7.4× = 0.059/0.008 基线为 Global（R2 验证正确，R1 原计算有误）
- 14.9% sign reversal 跨越广泛参数设定，不仅限于 τ(0)=0.03——R1 指出 50% 配置（260/520）出现 bias amplification
- CivilComments：最大实证缺口，但半合成方法论是因果推断标准做法
- Per-model R²：建议 Appendix W 增加影响因素分析

### Formatting & Compliance
- ACL 双栏 + review mode，正文 8 页，符合 EMNLP 2026 长文限制
- Limitations 在正文内，合规
- Figure 4 确认在 page 8（R1 验证），非 page 9
- Figure 2 色盲修复可能不完整
- Egami bib year 不一致

### Issue Tracker 更新
- 本轮新增 10 个 issue（R22-W1–W5, R22-Q1–Q4, R22-FMT1）
- 更新 18 个已有 issue 的 R22 mentions（含双方交叉回应论据）
- R16-W7（Figure 2 色盲）从 resolved 回退至 in_progress