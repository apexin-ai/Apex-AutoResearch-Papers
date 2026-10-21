---
round: 24
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T21:42:08.843950+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 24（Fresh 模式）

**项目**: causal_annot_error_attrib
**目标 Venue**: EMNLP 2026（ARR 统一审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验验证; R2: 新颖性+完整性）
**轮次**: Round 1（收敛，无需 Round 2）

---

## Summary

本文系统分析了 K-class non-differential misclassification（源自 LLM 标注）在七种 canonical DAG 拓扑下的偏差传播。主要贡献：(1) 导出各拓扑闭式偏差表达式及 sign preservation 条件；(2) 证明 K=2 exact envelope monotonicity（Theorem 1）和 K=3 symmetric exact monotonicity（Theorem 2），并为一般 K≥3 提出 ε-approximate monotonicity 猜想（Conjecture 1）；(3) 证明 FWL invariance 导致 matrix-based corrections 对 4 种拓扑无效；(4) 提出 ASV 和 topology-aware correction routing（Algorithm 1）。实验在 3 个 NLP 数据集、23 个 LLM 配置上验证理论预测。

---

## Strengths

**S1. 填补了重要理论空白。** 首次对 7 种 DAG 拓扑给出 K-class 闭式偏差表达式，揭示拓扑间质性差异（exposure K≥3 可发生 sign reversal，confounding 始终 sign-preserving）。Taxonomy（Table 1, Figure 1）对计算社会科学研究者有直接参考价值。

**S2. FWL invariance 是最强的单独贡献。** 证明 naive plug-in 和 MLA 对 confounding/mediation/collider/M-bias 四种拓扑偏差消减为 0%。证明思路清晰：D̃ = D·M 不改变 dummy 列空间，FWL 残差不变。直接帮助研究者避免无效校正尝试。（双方一致认为是论文最优雅的结果）

**S3. 诚实的理论分级。** K=2 exact → K=3 symmetric exact → general K conjecture。Conjecture 1 明确标注为猜想，附 545,945 adversarial curves 数值验证（ε_max = 0.016）。这种分级优于过度声称。

**S4. ASV 框架设计合理。** 将 magnitude、significance、sign-flip 三维度整合为拓扑特异性诊断。Table 2 vulnerability ranking（IV 最脆弱，M-bias 最稳健）直观可操作。

**S5. 附录深度超出一般投稿水平。** 23 页附录覆盖 10+ 维度稳健性检验（non-differential 假设违反、非线性 DGP、proportional effects 崩溃边界、logistic regression 下 FWL 失效、bootstrap 收敛等）。

**S6. Algorithm 1 提供可操作的决策支持。** Topology identification → risk assessment → method selection → FWL screening 四步流程，对缺乏测量误差理论背景的 NLP 研究者有较高实用价值。

---

## Weaknesses

### Must-Fix（双方共识）

**W1. [Must-Fix, R1+R2 共识] K≥3 非对称情形的 monotonicity 完全依赖未证明的 Conjecture 1，存在关键理论断层。**

Theorem 2 要求均匀 off-diagonal（C_jk = c for all j≠k），但 VAST K=3 实际 LLM 混淆矩阵 median Frobenius distance d_sym = 0.33（Appendix B.24 Remark 5），远非对称——Theorem 2 在实践中覆盖范围极其有限。K≥3 的 practical monotonicity 保证完全依赖 Conjecture 1。

545,945 adversarial curves 的数值验证虽广泛，但四种结构族（near-permutation, block-diagonal, sparse, near-uniform）的选择缺乏理论覆盖性保证。B.12 Table 11 显示 K=7 worst-case ε = 0.060，比 K=3 的 0.003 大一个数量级——暗示 large-K（如 HumAID K=10）下 approximate monotonicity 质量恶化。

依赖链：Conjecture 1 → ASV ordering → Algorithm 1 Step 1 → correction routing 正确性。若 conjecture 有反例，Algorithm 1 可能给出错误建议。

R2 补充 nuance：ASV 的 sign-flip 诊断可直接数值计算（给定具体 C）而非依赖理论单调性保证——理论断层更多影响"理论完整性"而非"实用可靠性"。

**建议**：(a) 对 diagonally dominant matrices（d_ii > 1/K，覆盖所有准确度>50%的矩阵）证明 monotonicity；或 (b) 对 adversarial search 的覆盖性给出形式化分析（covering number argument）；或 (c) 在主文中明确降级 Conjecture 1 的角色并强调 ASV 的数值计算路径不依赖该猜想。

### Should-Fix（双方共识或 Director 裁定）

**W2. [R1 Must-Fix, R2 Should-Fix → Director 裁定 Should-Fix] Proportional effects 假设（f = λg）的 robustness 选择性报告。**

Appendix B.13 Table 15 显示 failure rate 完整谱系：exact f=λg 0.09%、near r≈0.1 0.85%、near r≈0.3 10.95%、near r≈0.5 22.45%、independent f,g 22.9%、NLP-realistic 0.07%。主文声称"97.3% robustness under non-proportional effects"仅报告最佳情形。

R2 nuance：NLP-realistic 可能确实是最相关参数区间（treatment/confounder 效应通常同向），选择性报告是呈现问题非方法论缺陷。

**建议**：在主文中展示完整退化谱系（至少提及"0.09%–22.9% depending on departure"），同时可论证 NLP-realistic 的生态效度。

**W3. [R1 Must-Fix, R2 REBUT → Director 裁定 Should-Fix] Linear OLS 限制不够突出；logistic regression 下核心结论翻转。**

B.14 Table 7 显示 logistic regression 下 FWL invariance 失效：exposure 拓扑 22–78% 偏差消减（OLS 下为 0%）。

R2 REBUT 理由充分：(a) 论文已在 Section 5 和 Limitations 声明线性范围；(b) B.14 是诚实 robustness check，反用为 Must-Fix 证据在逻辑上有问题；(c) FWL break 方向有利（偏差被部分消除），Algorithm 1 推荐的方法在 logistic 下仍然有效（虽非最优）而非"错误"；(d) OLS 仍是社科因果推断最常用方法。

**建议**：Algorithm 1 添加"designed for linear regression"标注；Section 4.5 FWL invariance 讨论中注明 logistic regression 下结论不同。

**W4. [R2 Must-Fix, R1 未升级 → Director 裁定 Should-Fix] 缺少 end-to-end 真实因果研究。**

全部实验使用合成 DGP（注入已知 τ），真实 LLM 混淆矩阵仅用于参数估计。缺少完整的"真实因果问题 + 真实标注 + 真实结果"案例。R1 认可批评成立但指出实证成分比 R2 描述更丰富（23 real LLM CMs, B.18 case study, B.19-B.20 semi-real）。此问题自 Round 3 起反复出现（R3-NEW-8），多轮共识为 should-fix。

**建议**：补充至少一个 end-to-end 真实因果研究，或在 Limitations 中更明确讨论此局限。

**W5. [R2 Must-Fix, R1 部分同意 → Director 裁定 Should-Fix] ASV 与 E-value 的方法论区分不足。**

ASV 与 sensitivity analysis 文献中的 E-value 功能重叠：两者都量化结果对测量误差/混淆的脆弱程度。论文未充分说明 ASV 的独特优势。R1 部分同意但认为 K≥3 structural dichotomy 赋予 ASV 独立价值（E-value 不捕获拓扑依赖性）。此问题自 Round 4 起反复出现（R4-W6），跨 10+ 轮共识为"solid systematic contribution 而非 methodological breakthrough"。

**建议**：添加与 E-value 的形式化对比（不同输入/假设/输出），展示 ASV 在何种情况下提供 E-value 无法给出的信息。

**W6. [Should-Fix, 双方共识] 实验范围过窄。**

仅 3 个英文文本分类数据集（HumAID K=10, VAST K=3, CivilComments K=2），23 个 LLM 配置。缺少：多语言数据、序列标注/NER、ordinal classification、K>10。论文标题以"multi-class annotation errors"为题但验证仅覆盖英文文本分类。

**建议**：明确限定适用范围为"text classification with categorical annotations"；讨论其他场景下混淆矩阵结构差异的预期影响。

**W7. [Should-Fix, 双方共识] Non-differential misclassification 的 design argument 存在实践漏洞。**

文本本身编码与 Y 相关的特征——LLM 可能对某些 Y 值对应的文本系统性犯更多错误。B.6 stress test 显示 τ=0.30 时 violation rate 达 34.9%。B.5 经验检验仅在 VAST 上按 topic 分层，未按 Y 分层。

R2 补充 caveat：文本 X 编码 Y 信息导致的是 content-dependent（而非 outcome-dependent）misclassification，design argument 是合理近似而非已知漏洞。

**建议**：(a) 讨论"text as proxy for Y"问题；(b) 补充按 Y 值分层的 non-differential 检验。

**W8. [Should-Fix, 双方共识] C(δ) = (1−δ)I + δC_fix 线性插值路径不反映真实 LLM 质量退化。**

所有类别误分类概率以相同速率退化，但真实 LLM 不同类别性能退化不均匀（低频类别先降）。不影响理论结果（bias expressions 对任意 C 成立），但影响 Figure 4 等可视化的代表性。

**建议**：补充至少一条基于真实 LLM 质量梯度的 C 路径，或 acknowledge 此局限。

**W9. [Should-Fix, R2 提出] Section 3 对 EMNLP 读者不够友好。**

Proposition 1 的矩阵代数和多面体参数化对 NLP 背景读者门槛过高。

### Minor

**M1.** τ 在 Section 3（treatment coefficient）和 Appendix B.6（non-differential departure parameter）中重复使用，建议换用不同符号。

**M2.** Table 28（notation guide）仅在附录。主文加入简化版会改善可读性。

**M3.** "23 LLM configurations" 应澄清为"23 LLM × dataset × prompting configurations across 3 datasets"。

**M4.** Remark 5（B.24, d_sym=0.33）应在主文讨论 Theorem 2 时交叉引用。

**M5.** 83.4% sign reversal 来自 full Dirichlet（含准确率<50%矩阵），不代表实际 LLM 场景，framing 需谨慎。

---

## Reviewer Consensus

双方评分一致（3.5/5 Borderline Conference），以下核心判断达成共识：

1. **Conjecture 1 / 理论断层是最核心的弱点**（唯一的双方共识 Must-Fix）
2. **FWL invariance 是最强的单独贡献**——优雅、实用、证明完整
3. **实验范围过窄**——3 个英文文本分类数据集不足以支撑一般性声称
4. **论文执行质量高**——附录深度、诚实的理论分级、Monte Carlo 与理论高度吻合
5. **ASV 是 systematic contribution 而非 methodological breakthrough**——贡献声明应相应调整
6. **论文处于 Conference/Findings 边界**——修复 W1 可推向 Conference

## Reviewer Divergence

| 问题 | R1 | R2 | Director 裁定 |
|------|----|----|---------------|
| Proportional effects 选择性报告 | Must-Fix | Should-Fix（呈现问题） | **Should-Fix** |
| Linear OLS 限制 | Must-Fix | REBUT → Should-Fix | **Should-Fix**（R2 rebuttal 成立） |
| 缺少真实因果研究 | 未升级 | Must-Fix | **Should-Fix**（理论论文局限） |
| ASV vs E-value | 未提及 | Must-Fix | **Should-Fix**（跨轮共识） |
| 13.7% baseline violation | Should-Fix | REBUT（删除） | **删除**（R2 论证：是 ASV 成功诊断高风险的证据） |
| ε_max = 0.016 实际意义 | 追问 | REBUT（实践中可忽略） | 作为问题保留 |

---

## Questions for Authors

**Q1.** 是否尝试过对 diagonally dominant matrices（d_ii > 1/K）证明 monotonicity？对角优势条件覆盖所有准确度>50%的矩阵，是 Theorem 2 和 Conjecture 1 之间的自然桥梁。

**Q2.** 主文"97.3% robustness under non-proportional effects"对应 Appendix B.13 Table 15 的具体 setting？表中 failure rate 在 0.07%–22.9% 之间变化显著。

**Q3.** Algorithm 1 是否需要对 logistic regression 做修改？如需要，修改后的 routing 是什么样的？

**Q4.** Table 6 中 PPI++ 的 gold fraction 为多少？PPI++ 优势对 gold fraction 的敏感度如何？

**Q5.** Collider topology（Table 1: 100% sign-flip guarantee）——conditioning on collider 即使无 misclassification 也引入 selection bias。Misclassification-induced bias 与 collider 固有 selection bias 如何交互？论文是否分析了两种 bias 的叠加效应？

**Q6.** Conjecture 1 的 ε_max = 0.016 在 ATE 典型量级（|τ| ≈ 0.1–0.5）下对实际因果推断决策的影响有多大？

---

## Missing References

1. **Cinelli & Hazlett (2020)** partial R² sensitivity analysis — Section 2 引用但未与 ASV 做方法论对比（R23 共识）
2. **Mahajan (2006), Hu (2008)** — 多值误分类非参数识别和非线性模型处理（R22 共识）
3. **Anthropic (2024)** model uncertainty × annotation disagreement（R2 提出）
4. **Allen-Zhu & Li (2024)** LLM calibration → downstream analysis 理论框架（R2 提出）
5. **Buonaccorsi (2010)** "Measurement Error: Models, Methods, and Applications" — R1 建议补充，R2 指出可能已引用（需验证 p.9）
6. **Cornfield et al. (1959)** sensitivity analysis 源头、**Törnberg (2024)** LLM 注释质量实证（R22 建议）

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 本轮未提交外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成**（2026-05-25T21:17:29 → 2026-05-25T21:21:40，耗时约 4 分钟）

| 严重程度 | 位置 | 发现 |
|---------|------|------|
| ⚠️ Warning | Page 1-2 | 前 2 页为连续纯文本（Title/Abstract/Intro/Related Work），无 display item。第一个 display item 在 page 3，刚好在 3 页阈值内。建议在 page 1-2 加入 pipeline overview 或核心结果 teaser。 |
| ℹ️ Info | Page 6 | Figure 4 单栏双面板图，轴标签/刻度标签字号接近可读下限（~7pt）。 |
| ℹ️ Info | Page 7 | Figure 5 轴标签字号偏小，与 Figure 4 同样隐患。 |
| ℹ️ Info | Page 4 | Figure 2 八面板密度较高，子图标题字号较小但尚可辨认。 |
| ℹ️ Info | Page 8 | Algorithm 1 与 Figure 6 同页，视觉密度较高但不构成问题。 |
| ℹ️ Info | Page 33 | 末页~90%空白（AI Assistants 声明自然结束），不可避免。 |

统计：0 critical, 1 warning, 5 info。

---

## Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | K=2 证明完整正确；K=3 symmetric 证明正确但假设过强；K≥3 一般情形仅有 conjecture+数值验证。FWL invariance 证明优雅。Proportional effects 限制呈现不完整。 |
| Excitement | 3.5/5 | 问题 timely 且重要。Topology-dependent taxonomy 是 novel 框架。K≥3 structural dichotomy 是有价值的新发现。但对 NLP 从业者的直接影响取决于非线性模型扩展。 |
| Reproducibility | 4/5 | 代码和数据声明可用（匿名链接），DGP 参数完整（Table 28），Monte Carlo 设置详细。LLM API 可复现性存在不确定性。 |
| Confidence | 4/5 | 两位 Reviewer 仔细检查了主要证明和实验设计，对 measurement error in causal inference 文献较熟悉。 |
| **Overall** | **3.5/5** | **Borderline Conference** |

### 综合判断

一篇理论深度可观、实践导向清晰的论文，系统建立了 LLM 标注误差在因果推断中的 topology-dependent 分析框架。FWL invariance 和 K≥3 structural dichotomy 是独立有价值的贡献。

核心弱点是 K≥3 非对称情形的理论断层（Conjecture 1 未证），以及 proportional effects 限制的选择性报告。实验仅覆盖 3 个英文文本分类数据集，对一般性声称支撑不足。

**定位**：Solid systematic contribution with novel qualitative insights，处于 Conference/Findings 边界。

- **达到 Conference（4.0）的条件**：修复 W1（Conjecture 1 理论断层——证明 diagonally dominant 情形或降级角色）+ W2（proportional effects 完整退化谱系）
- **当前水平足够 Findings（3.0-3.5）**：即使不修复 W1，taxonomy + FWL invariance + structural dichotomy 的组合对 Findings 足够

---

## Detailed Comments

### Section 3（理论框架）
- Proposition 1 的 7 个闭式表达式是论文基石——正确且有价值
- Theorem 1（K=2 exact monotonicity）证明严谨
- Theorem 2 的 symmetric 假设（C_jk = c）过强：d_sym = 0.33（VAST K=3）远非对称
- Conjecture 1 是关键空白：545,945 adversarial curves 是 strong evidence 但 absence of evidence ≠ evidence of absence
- C(δ) 参数化假设均匀退化——真实 LLM 不同类别退化速率不同
- τ 符号在 Section 3 和 B.6 中重复使用，需消歧

### Section 4（实验）
- Monte Carlo 与理论高度一致（MAPE ≤ 3.2%）——执行质量高
- Table 1 structural dichotomy（exposure 52.6% sign flip vs others 0%）是最引人注目的实证发现
- Table 6 correction comparison 有价值但 PPI++ gold fraction 未在主文说明
- 仅 3 个英文文本分类数据集——对"multi-class annotation errors"一般性声称支撑不足
- "23 LLM configurations"描述需澄清为 23 个 LLM×dataset×prompting 配置

### Section 4.5（FWL Invariance & Algorithm 1）
- FWL invariance 证明是全文最干净的结果
- Algorithm 1 实用但仅适用于 linear OLS——应显著标注
- B.14 显示 logistic regression 下 FWL break 方向有利（部分消除偏差），这反而使叙事复杂化
- Section 4.5 讨论 5 种 correction methods 但未提及 regression calibration——应说明为何排除

### Appendix
- 深度超出一般投稿水平（23 页，10+ robustness 维度）——是强项
- B.6 non-differential stress test 既是优点（诚实）也是弱点（34.9% violation at τ=0.30）
- B.12 K=7 worst-case ε = 0.060（vs K=3 的 0.003）被低估报告——对 HumAID K=10 场景高度相关
- B.13 proportional effects 完整谱系（0.09%–22.9%）应在主文中呈现
- B.24 Remark 5（d_sym=0.33）应在主文讨论 Theorem 2 时交叉引用