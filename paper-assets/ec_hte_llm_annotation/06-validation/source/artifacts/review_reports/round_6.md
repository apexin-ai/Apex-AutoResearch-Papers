---
round: 6
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T11:53:07.707312+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Round**: 9 (Fresh Review)
**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作质量)
**日期**: 2026-05-22

---

## Summary

本文证明了一个精确的偏差分解恒等式（Theorem 1）：当 LLM 标注错误率跨子群异质时，使用单一混淆矩阵进行全局校正会引入与 δ_s·Δτ/(1−2π̄) 成正比的子群级偏差。作者提出 EC-HTE 方法（分层贝叶斯子群混淆矩阵估计 + CausalForestDML），并提供独立可用的 Δτ-free 诊断工具（Proposition 3, AUC=0.86）。在 520 个合成配置（R²=0.994）、半合成 TweetEval 实验和 7 个 LLM 的真实混淆矩阵上进行了验证。

---

## Strengths

1. **精确的 bias 分解恒等式**：Theorem 1 是 exact identity（非 bound），形式 δ_s·Δτ/(1−2π̄) 简洁可解释，三因子分别捕捉子群偏差、处理效应异质性和矩阵求逆放大。证明经 R1 独立验证完全正确。

2. **Δτ-free 诊断准则**：Proposition 3 的条件仅依赖误分类率（可从 pilot sample 估计），打破了循环依赖。AUC=0.86（子群级），实践者可在估计 CATE 前判断全局校正是否有害。

3. **极其充分的实验验证**：520 配置 × 100 MC runs + 半合成 TweetEval + hate speech case study + 7 LLM（4 开源 + 3 商用）+ 14 个 appendix sections 覆盖各类鲁棒性检验。这是两位 Reviewer 一致认可的最大优势。

4. **诚实报告所有负面结果**：TweetEval 上 EC-HTE 不优于 Global（p=0.395, RMSE 0.225 vs 0.124）被完整讨论；hate speech case study underpowered 被如实报告；coverage 偏低（CausalForest 83-85%）被承认。

5. **清晰的适用性边界**：三个定量前提（budget threshold, classifier quality, class balance）+ Proposition 3 诊断 + applicability frontier（Figure 5, Appendix）。

6. **格式完全合规**：正文 ≤ 8 页 ✓，ACL review 模板 ✓，double-blind ✓，Limitations 章节 ✓。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] Theorem 1 novelty 被过度声明** [R1 AGREE, R2 提出, critical]
- Introduction L12 "discover a previously unrecognized bias mechanism" 过强。Frazis & Loewenstein (2003) 已有错误分类二元变量的精确偏差公式；Fuller (1987) 建立了基本框架。
- 论文的增量是将经典框架 specialize 到"子群异质误分类 + 效应修饰变量"组合，product form δ_s·Δτ 是 novel，但底层 M_global^{-1}M_s−I 分解并非全新。
- **必须修改**：将 "discover" 替换为更精确的表述（如 "characterize the correction-induced bias..."）；在 Section 3 开头增加定位句。

**[MF-2] 真实数据验证不充分** [R1 提出 critical, R2 方向一致]
- 所有展示 EC-HTE 优势的实验使用合成 CATE 注入。hate speech case study (Appendix M) underpowered（"all CI contain zero"）。Multi-LLM (Section 5.5) 仅确认异质性存在，未验证校正效果。
- 结构性限制（CATE ground truth 需 RCT），但论文应更诚实地定位为理论贡献，或明确解释 hate speech 结果不构成方法失败。
- **两种修改路径**：(1) 找到/构建真实 RCT+LLM 标注数据集（难度大）；(2) 调整 framing——downplay 实践指导声明，强调理论洞察价值。

**[MF-3] HB 相对于 Stratified MLE 增量极小，方法贡献定位需调整** [R1 提出 critical, R2-N3 方向一致]
- Table 1：HB EC-HTE 与 Stratified MLE 差异极小（K=2: |bias| 0.010 vs 0.012; K=4: 0.008 vs 0.010）。RMSE 几乎相同。
- 核心理论（Theorem 1, Proposition 3）适用于任何子群分层校正，并非 HB 独有。EC-HTE 是识别问题后的 natural solution。
- **必须修改**：将 HB 降格为 "the natural correction prescribed by the bias structure"（实现选择）而非独立方法论贡献；或提供极小 n_expert/K 时 HB 明显优于 MLE 的证据。

### Should-Fix（影响评分但不一票否决）

**[SF-1] "50% of K=2 configurations" 需要 grid-dependency 说明** [R2 提出, R1 降至 should-fix]
- 260/520 依赖均匀实验网格设计（26 Δπ × 20 Δτ），不反映实际参数分布。
- Proposition 3 的解析条件才是 primary claim，50% 仅为 illustration。
- **修改方向**：所有出现 50% 的位置加 "across our K=2 parameter grid"；将 Proposition 3 条件作为 primary claim。

**[SF-2] TweetEval 负面结果在 Abstract/Conclusion 中权重不足** [R1+R2 共识]
- EC-HTE RMSE 0.225 vs Global 0.124（1.8×），最接近实际的实验对 EC-HTE 不利。Abstract 压缩为从句，合成正面结果占据 prominent 位置。
- **修改方向**：Abstract 和 Conclusion 中给予 TweetEval 结果同等 prominence；明确 EC-HTE 优势条件。

**[SF-3] CausalForest plug-in SE coverage gap 讨论不充分** [R1+R2 独立提出]
- CausalForest coverage 83-85% 远低于 95% nominal。归因于 "inherent SE calibration" 不完全令人信服。
- 读者难以分辨混淆矩阵校正 vs CausalForest SE 本身的贡献。
- **修改方向**：正文分离两个来源的贡献比例；Table 1 中标注已知限制。

**[SF-4] Assumption (A5) 放松缺正式定理 + (A2) 对称误差正文处理不足** [R1+R2 共识]
- (A5) 推广到 subgroup-specific Δτ_s 仅一句话，无正式 Corollary。
- (A2) 对称假设在所有真实 LLM 实验中不成立（Table 16 FPR/FNR 系统性不对称），Proposition 3 AUC 从 0.86 降至 0.82。正文 Remark 2 仅 4 行。
- **修改方向**：Section 3 添加正式 Corollary；Remark 2 扩充写出非对称 bias 公式；提及 AUC 降幅。

**[SF-5] 缺少 EC-HTE 不适用场景的决策树** [R1+R2 共识]
- 适用条件散布多处（budget, classifier quality, class balance, κ thresholds）。
- Appendix R 的 logistic regression diagnostic rule 是好的实用工具但被埋在附录中。
- **修改方向**：将 Appendix R 决策规则整合到正文 Recommended workflow。

**[SF-6] 有限样本 remainder R_n = O_p(n^{-1/2}·κ) 未推导** [R1 提出, R2 同意]
- 阶声明缺少推导或引用。κ(C_s) 较大时余项可能不可忽略。
- **修改方向**：Appendix 补 2-3 行推导（引用 matrix perturbation theory）+ 经验 remainder/main term 比例。

**[SF-7] Corollary 4 多分类扩展 g(π̄) 假设 uniform off-diagonal** [R1 提出, R2 同意]
- g(π̄) = 1/(1−Jπ̄/(J−1)) 仅对均匀 off-diagonal 成立。实际 LLM 误分类通常 non-uniform。
- **修改方向**：讨论 non-uniform 推广或明确标注假设局限。

### Minor（不影响接收）

- M1: "Debiasing" 标题可能被 NLP 读者误解为 fairness debiasing（脚注 1 已区分，可接受）
- M2: Table 1 CausalForest block 缺 Stratified MLE 行（对比不完整）
- M3: 部分 appendix 用 50 MC seeds 而非 100，未统一说明
- M4: ESS > 845 阈值来源未说明
- M5: (A5) "Homogeneous treatment effects across subgroups" 表述有歧义——应为 τ(z,s)=τ(z)
- M6: "global correction"/"pooled correction"/"standard correction" 仍有混用
- M7: PPCI 组合中 "jointly sufficient" 声明过强（仅在 DGP C 下验证）
- M8: Figure 2 热力图 "debiasing hurts" 标注文字偏小

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全达成共识：

1. **评分一致**：3.5 (Borderline Conference)，如果 MF-1/2/3 得到有效回应可升至 4.0
2. **核心定位**：这是一篇以问题识别和理论刻画为主要贡献的论文，方法论创新相对有限
3. **理论正确性**：Theorem 1 证明正确且完整（R1 独立验证），但 novelty 声明过强
4. **实验thoroughness**：两人一致认为实验验证是论文最大优势（"我见过的最thorough的实验验证之一" —R2）
5. **诚实报告**：负面结果（TweetEval, hate speech, coverage gap）的诚实报告是重要加分项
6. **TweetEval 权重**：最接近实际的实验结果应获得更多 prominence
7. **Coverage gap**：CausalForest 下 plug-in SE 的覆盖率问题需更清楚讨论

---

## Reviewer Divergence [REBUT]

以下问题两位 Reviewer 存在分歧（已在交叉中讨论，记录各方立场）：

1. **50% claim 严重性**：R2 标 critical（grid-dependent, potentially misleading），R1 rebut 降至 should-fix（Proposition 3 解析条件是 primary claim，50% 仅为 illustration，且论文已有 qualification）。**Director 判断**：采纳 R1 观点，降为 Should-Fix。

2. **问题识别 vs 方法创新的张力**：R2 标 Must-Fix（要求 reframe 为 problem-identification paper），R1 rebut（"自然解法"在因果推断领域常见，如 DML；论文贡献即使在此定位下也足够）。**Director 判断**：合并入 MF-3（HB 增量问题），不要求彻底 reframe。

3. **CV(π_s) vs Proposition 3 对比公平性**：R2 认为论文 dismiss CV(π_s) 不够充分（AUC 0.97 vs 0.86），R1 rebut（两个 AUC 回答不同问题——setting-level vs subgroup-level，不直接可比；Proposition 3 打破循环依赖是独立优势）。**Director 判断**：R1 论证更充分，但建议在正文中 acknowledge CV(π_s) 作为 complementary practical heuristic。

4. **Yadlowsky et al. (2024) 是否为必须引用**：R2 认为应补充，R1 rebut（CATE calibration 与 misclassification correction 是不同问题）。**Director 判断**：采纳 R1 观点，列为 optional。

---

## Questions（需作者澄清）

1. **子群标签噪声**：当子群定义本身由 LLM 预测时（如用 LLM 预测文本类型作子群），EC-HTE 如何处理额外噪声源？
2. **子群大小不均衡**：TweetEval 中 S3 (11%) 仅获得 ~28 expert labels，EC-HTE RMSE 是 Global 的 3.3×——这是 fundamental 限制还是可通过增大 budget 解决？
3. **estimator-agnostic 声明限制**：方差传播需 per-observation SE，并非所有 CATE 估计器提供此信息（如某些 meta-learner、matching estimators）。如何使用？
4. **κ 灰色地带**：1.25 < κ < 100 之间如何指导实践者？论文仅讨论了两个端点。
5. **Gamma(3,1) 选择动机**：sensitivity analysis 显示 <5% variation，但为什么选 (3,1) 而非 (1,1) 或 (5,1)？
6. **Mistral-7B 零触发**：Table 7 (Appendix O) 显示 Mistral-7B 的 Proposition 3 诊断在 0/4 子群触发——是否说明异质性对某些模型不重要？

---

## Missing References

**应补充**（两位共识）：
1. **Wang, McCormick & Leek (2020, PNAS)** — ML 预测变量在因果推断中引入偏差，与本文 broader theme 高度相关
2. **Feder et al. (2022, TACL)** — "Causal Inference in NLP" 综述，应在 Related Work 中引用以定位交叉领域位置
3. **Keith et al. (2020, ACL Findings)** — "Text and Causal Inference"，与文本作为 effect modifier 的设定相关

**可选补充**：
4. Yadlowsky et al. (2024) — CATE calibration（不同问题但 complementary）
5. Zhang & Manski (2007) — partial identification under misclassification（bounds approach 作为替代策略）
6. Semi-supervised / active learning 文献作为替代标注质量提升策略的讨论（Zrnic & Candès 2024 已引用但讨论过简）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

**状态**: 已完成 (2026-05-22T11:36:24Z)
**结果**: 0 critical / 3 warnings / 10 info

**Warnings**:
1. 首页无视觉锚点（Figure 1 在 page 2，可接受但非最优）
2. Pages 3-6 连续 4 页无 display item（pages 3-5 为理论推导属例外，page 6 已过渡到实验但仍无图表）
3. 主文仅 3 个 display items（Figure 1, Table 1, Figure 2），0.375/页偏低。附录有 20 个 display items，大量实验证据被推至附录

**Info（正面）**:
- Figure 1 位置合理，caption 自包含
- Table 1 booktabs 风格专业
- Figure 2 热力图阴影区分度好
- 数学公式渲染正确，无 LaTeX 错误
- 无 margin 溢出、无 widow/orphan 问题
- 参考文献无未解析引用

---

## Overall Assessment

**评���**: 3.5 / 5 — Borderline Conference
**置信度**: 4/5（两位 Reviewer 均为 4/5 置信度）

**评分论证**：

论文识别了一个真实且重要的失效模式——LLM 标注全局校正在子群异质性下 amplify 偏差。理论刻画精确（exact identity, R²=0.994），实验验证极其充分（520 配置 × 100 MC + 7 LLM），诚实报告所有局限。这些优势使其远超 Findings 门槛。

阻碍 Conference 接收的因素：(1) Theorem 1 的代数内容相对于经典测量误差文献是 incremental specialization，novelty 声明过强；(2) EC-HTE 方法是问题识别后的 natural solution，HB vs Stratified MLE 增量极小；(3) 所有成功案例依赖合成数据，最接近实际的 TweetEval 结果 mixed；(4) 适用条件较窄。

**升分路径**（如果回应充分可升至 4.0）：
- 更精确地定位 novelty（problem-identification + characterization，而非 "discover"）
- 给 TweetEval 混合结果同等 prominence
- 明确将 HB 降格为实现选择，核心贡献聚焦 bias identity + diagnostic
- 在 Rebuttal 中解释真实数据验证的结构性限制

**ARR 维度评分汇总**（两位 Reviewer 一致）：
| 维度 | 分数 |
|------|------|
| Soundness | 4/5 |
| Excitement | 3/5 |
| Reproducibility | 4/5 |
| Clarity | 4/5 |

---

## Detailed Comments（逐节意见）

### Abstract
- 信息密度高，每个 claim 有正文支撑——优点
- "50%" claim 需加 "across our K=2 parameter grid" 限定
- TweetEval 混合结果的权重应与合成正面结果对等
- "jointly sufficient" 对 PPCI 组合过强（仅 DGP C 验证）

### Introduction (Section 1)
- 动机清晰有力，GPT-4 误差率差异（10.2% to 20.5%）切入自然
- L12 "discover a previously unrecognized bias mechanism" → overclaimed
- 贡献列表 C1 和 C2 有重叠；C2 应明确为 "natural correction"
- Figure 1 有效传达核心 intuition

### Related Work (Section 2)
- 覆盖全面：measurement error + annotation models + HTE + PPI/DSL
- 三层区分（L7-10）有效
- 缺少 NLP+因果推断综述连接（Feder et al. 2022, Keith et al. 2020）

### Theory (Section 3)
- Theorem 1 证明正确完整
- Proposition 3 简洁优雅，Δτ-free 是关键创新
- (A5) 推广仅一句话，需形式化
- Remark 2 对非对称误差的讨论过于简略
- 有限样本 remainder 声明缺推导

### Method (Section 4)
- HB 模型规格合理，MCMC 诊断充分
- κ > 100 guard 设计合理但与 κ ≤ 1.25 之间的灰色地带未讨论
- SE propagation 是 plug-in，诚实承认局限
- 与 PPCI 组合讨论有效

### Experiments (Section 5)
- §5.2 Bias Identity 验证令人信服（R²=0.994/0.974）
- §5.3 TweetEval 负面结果讨论充分但 prominence 不足
- §5.4 Diagnostic AUC=0.86 有独立价值；CV(π_s) 对比可更公平
- §5.5 Multi-LLM 有效证实 Δπ 异质性的结构性

### Conclusion (Section 6)
- 简洁准确，继承 Abstract 的 "50%" 和 TweetEval 权重问题

### Limitations
- 覆盖充分且诚实，格式适当（~3 个核心点）
- 明确了 CausalForest SE 覆盖率问题和代码开源承诺