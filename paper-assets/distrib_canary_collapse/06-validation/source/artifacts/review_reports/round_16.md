---
round: 16
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-25T08:38:40.347707+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 16 综合审稿报告

**论文**: Characterizing the Detectability Landscape of Iterative Model Collapse
**Venue**: EMNLP 2026 (ARR)
**Reviewer**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作质量）
**审稿模式**: Fresh（重新审稿）

---

## Summary

本文系统研究迭代 model collapse 的可检测性，将 5 种时间序列统计方法（含 Permutation Granger causality）应用于 canary metrics（token entropy, ECE）与 downstream metrics（distinct-n, perplexity）的时序领先-滞后关系检测。核心发现是 PermG 在 α_c ≈ 0.50 处从 0/8 跳到 6/8 显著对，定义了三个检测区域（blind/onset/detection）。五种方法的 null-control FPR 从 6.7% 到 94.4%（κ=0.185），表明单方法分析不可靠。Cross-architecture 在 α=1.0 下支持 11/15 conditions 的 forward detection。

---

## Strengths

**S1. [共识] 方法敏感性发现是论文最有价值的贡献。** 五种方法在相同数据上 FPR 从 6.7% 到 94.4%（κ=0.185），直接表明 model collapse 检测文献中单方法研究的结论可能不可靠。R2 认为此发现比 phase transition 本身更有价值，R1 同意。

**S2. [共识] 实验设计严谨，统计控制充分。** Null-control (α=0.0) 基线、BH-FDR 多重检验校正、置换检验避免参数假设、multi-seed 复制、1,160 配置的 specification curve。这种严谨程度在 model collapse 检测文献中少见。

**S3. [共识] 对 limitations 和 non-confirming cases 的讨论坦诚。** 4/15 cross-architecture non-confirming conditions 各有具体归因（precision sensitivity, bidirectional confounding, seed dependence, entropy decoupling）。Limitations 明确将框架定位为 "confirmation tool rather than early-warning system"。

**S4. [共识] Appendix 充实（26 页），核心 claims 有详细支撑。** 涵盖理论推导、Shapley 分解、partial correlation、cross-architecture 细节、power simulation 等。

**S5. [R1] Cascade ordering 结果有机制洞察。** Entropy 领先 diversity（24/24 forward, 0/24 reverse at α=1.0），first-differencing 消除 canary→perplexity 但保留 canary→diversity，证据干净。

**S6. [R1] 可复现性高。** 详细超参（Appendix A）、明确种子、代码发布承诺。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [critical, 共识] Phase diagram 仅基于 3 seeds（2 自由度），方差估计不可靠。**
- R1 提出（W1 critical），R2 完全同意。
- Phase diagram（Figure 1）是论文核心图表，但仅 3 seeds 构建。检测边界 α_c ≈ 0.50 和三区域分类可能随 seed 增加而显著偏移。FPR 分析使用了 10 seeds（60 pairs），但 regime 边界的 α×T 网格仅 3 seeds。
- 论文在 Limitations 中承认了这一点，但 self-acknowledgment 不能替代实际增加 seeds。

**W2 [critical, 共识] "Sharp transition" 措辞超出统计证据强度。**
- R1 提出（W2 critical），R2 提出（W1 major），交叉后双方同意需弱化措辞。
- 6/8 检测率的 Clopper-Pearson 95% CI 为 [0.25, 0.92]，即真实检测概率可能低至 25%。Appendix S 的 sigmoid 拟合 steepness k=478±473（SE≈k），~100% 相对不确定性。
- R2 补充：cross-seed consistency（3 seeds 独立产生 0/8→6/8）和 Fisher exact test（p=3.45×10⁻¹¹）提供了 transition 存在的部分支撑，但 "sharp" 仍超出证据强度。
- **共识建议**：将 "sharp detection phase transition" 改为 "steep/abrupt transition" 或 "apparent transition"，在主文显式报告不确定性。

**W3 [critical, R2→R1 同意] Phase transition 可能只是统计功效的自然行为，非真正的物理相变。**
- R2 提出（W1 major），R1 在交叉中 AGREE with nuance。
- 任何统计检验在信号强度跨过检测阈值时都会从不显著跳到显著——这是 power curve 的基本性质。k=15.7 比 smooth-signal predictions 陡峭 3-4x 的比较 baseline 是论文自己构建的 VAR(1) power simulation，有循环论证嫌疑。
- R1 保留意见：VAR(1) simulation 的 onset steepness ratio k_obs/k_sim = 2.6-4.2 如果参数化合理，transition 比预期更陡有实质内容。但实际 α 网格分辨率为 5pp（0.45→0.50），"2 percentage-point interval" 来自 sigmoid 插值而非直接观测。
- **共识建议**：重新定位核心贡献为 "empirical characterization of detection limits" 而非 "phase transition discovery"。

**W4 [critical, 共识] 正文超出 8 页限制。**
- R1（W8 minor）和 R2（W6 minor）均指出，视觉审查确认。Conclusion 延伸到第 9 页约 15-20 行（Limitations 标题之前）。EMNLP 2026 正文限 8 页。
- 虽然修复简单（压缩 Discussion/Conclusion 几句话），但提交时必须解决。

### Should-Fix（显著影响论文质量）

**W5 [major, 共识] Cross-architecture 验证仅在 α=1.0（最易检测条件）。**
- R1（W3 major）和 R2（W4 major）独立提出并在交叉中互相确认。
- Phase diagram（Figure 1）是 Pythia-410M-specific。α_c ≈ 0.50 的相变在 GPT-2、Qwen、SmolLM 上未验证。仅 Pythia-1.4B 有 Appendix 中的部分 phase diagram 复现。Section 4.5 标题 "Cross-Architecture Evaluation" 在仅 α=1.0 条件下有误导性。
- **共识建议**：至少在 1 个非 Pythia 架构上补做 intermediate-α 验证。

**W6 [major, 共识] 方法论新颖性有限——成熟工具的直接应用。**
- R2 提出（W2 major），R1 在交叉中 AGREE。
- PermG、first-differencing、BH-FDR 均为标准工具。MMCT（Algorithm 1）本质是 FPR-inverse weighted voting，技术贡献有限。
- R1 补充：作为 empirical contribution 论文是被接受的贡献形式，但方法论新颖性确实有限。
- **共识建议**：将论文明确定位为 empirical study，强调实验发现而非方法论贡献。

**W7 [major, 共识] Blind zone（α < 0.50）根本性限制框架实用价值。**
- R2 提出（W3 major），R1 AGREE with nuance。
- α=0.10 时 distinct-1 已下降 39.6%，但 Granger 检测完全失效（0/8）。Abstract/Introduction 叙事暗示实用检测能力，但 blind zone 意味着检测只在 contamination 已很严重时才有效。
- R1 补充：刻画 blind zone 本身有价值——告诉 practitioners "不要依赖这些方法做早期检测"。但此定位应在 abstract/introduction 明确，不应延迟到 Limitations。

**W8 [major, R1] 单一数据集（WikiText-103），domain 泛化性证据极弱。**
- R1 提出（W4 major），R2 在交叉中 AGREE。
- Domain 泛化性仅有 Appendix 一句话："Pythia-1.4B on C4 yields 8/8 PermG forward detection"。
- R2 补充：model collapse 文献大多使用单一数据集，这是领域性问题，非本文特有缺陷。

**W9 [major, R1] MMCT K≥3 null-control FPR=10%，NaiveXCor（94.4% FPR）污染共识。**
- R1 提出（W5 major），R2 AGREE with nuance。
- K≥3 consensus FPR=10%（名义 5% 的两倍）。NaiveXCor 几乎必 reject，在 K 计数中恒贡献 1 分。
- R2 澄清：需区分 weighted MMCT（NaiveXCor 权重仅 1.06 vs. PermG 14.9，影响被压制）和 K≥3 majority voting（equal-weight，NaiveXCor 确实污染）。Table 2 报告的是 K≥3 结果，Algorithm 1 描述的是 weighted scheme——两者混淆是写作问题。
- **共识建议**：排除 FPR>50% 方法作为 robustness check，或在正文中解释 K≥3 和 weighted MMCT 的区别。

**W10 [major, R2→R1 部分同意] Design Principles 1-2 标签过度包装。**
- R2 提出（W5 major），R1 AGREE with nuance。
- Entropy（连续量）比 distinct-n（离散量）先响应在一定程度上是 trivially expected。论文 Discussion 中也承认了 measurement resolution asymmetry。
- R1 保留：量化刻画（24/24 forward, 0/24 reverse）的一致性不是 trivially 可预测的。
- **共识建议**：将 "Design Principle" 改为 "Empirical Finding" 或 "Proposition"。

### Nice-to-Fix

**W11 [moderate, 共识] Intervention 实验仅在 α=1.0。**
- R1（W6）和 R2（W7）独立提出。α=1.0 是最严重 collapse 条件，不需要精细检测即可观察退化。在 blind zone 边界（α≈0.50）测试才能展示实际价值。

**W12 [moderate, R1] α=0.60 non-monotonic anomaly 解释缺直接证据。**
- R1（W7）提出，R2 AGREE。"Temporal lag compression" 解释合理但间接。建议绘制 cross-correlation peak lag vs. α 图直接展示。

**W13 [minor, R2→R1 REBUT] 术语使用（Granger causality / precedence / temporal predictive improvement）。**
- R2 提出（W8 minor），R1 REBUT——认为是有意的术语精确化而非不一致。论文刻意避免 "Granger causality" 描述自己的 claims。
- **分歧记录**：R1 认为这是术语精确化（标准计量经济学做法），建议首次出现时明确定义三者关系即可。R2 建议统一使用一个术语。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识（[AGREE]）：

1. **Phase diagram 需要更多 seeds**（W1）——3 seeds 不足以稳定估计边界
2. **"Sharp transition" 措辞需弱化**（W2）——CI 过宽，steepness 不确定性 ~100%
3. **Cross-architecture 验证不足**（W5）——仅 α=1.0 不足以支撑 generalizability
4. **方法论新颖性有限**（W6）——empirical contribution 而非 methodological contribution
5. **Blind zone 限制实用性**（W7）——framing 应在 abstract/intro 明确
6. **正文超页**（W4）——Conclusion 溢出约 15-20 行到第 9 页
7. **Intervention 仅 α=1.0**（W11）——proof-of-concept scope 应明确
8. **方法敏感性发现是最有价值的贡献**（S1）——6.7%→94.4% FPR spread
9. **实验设计严谨**（S2）——统计控制在该领域属优秀水平

## Reviewer Divergence

仅一处实质分歧：

| 问题 | R1 | R2 | 决议 |
|------|----|----|------|
| 术语一致性（W13） | REBUT：有意的精确化 | minor weakness | 非关键问题，记录分歧 |

此外 R1-W9（Abstract 超 200 词）被 R2 REBUT（实际约 158-160 词），R1 未提供词数计算支持，采纳 R2 判断——Abstract 符合限制。

---

## Questions for Authors

**Q1. [共识, critical]** α_c ≈ 0.50 边界对 seed 数量有多敏感？如果使用 10 seeds 构建 phase diagram，边界估计是否变化？能否提供 α_c 的 bootstrap 置信区间？

**Q2. [共识, critical]** Phase transition steepness k=15.7 的 3-4x 比较 baseline 是什么？如何排除 steepness 来自 α grid 离散化（13 取值点，关键区域 5pp 分辨率）而非真实的物理现象？Appendix S 的 k=478±473 与主文 k=15.7 的数值差异如何解释？

**Q3. [R2]** MMCT 相比 standalone PermG 的边际改进有多大？Limitations 承认 "marginal improvement"——Algorithm 1 的贡献是否应降级为 analytical framework？

**Q4. [共识]** α=0.60 的 entropy-diversity lag 是否确实比 α=0.50 和 α=0.75 更短？能否提供直接的 cross-correlation 证据？

**Q5. [共识]** Intervention 的 15% entropy threshold 在实际部署中（未知初始状态）如何设定？跨 α 水平是否有一个通用的校准阈值？

**Q6. [R1]** First-differencing 消除 canary→perplexity 但保留 canary→diversity——两个指标都响应同一底层分布偏移，为什么 first-differencing 区分了二者？"channel-specific rather than global" 能否更严格定义？

**Q7. [R2]** Table 2 中 K≥3 consensus 在 α=0.75 的 TPR 为 37.5%，低于 α=0.50 的 66.7%——consensus voting 在 detection zone 反而不如 onset 区域可靠？

---

## Missing References

两位 Reviewer 共建议 6 篇可能遗漏的文献：

| 文献 | 提出者 | 相关性 | 引用紧迫度 |
|------|--------|--------|-----------|
| Hataya et al. (2023) "Will Large-scale Generative Models Corrupt Future Datasets?" | R1 | 早期迭代合成训练 | 应引用 |
| Rabanser et al. (2019) "Failing Loudly" | R1 | 通用 distribution shift detection | 可选引用 |
| Carvalhais et al. (EMNLP 2025) "Recursive Training Loops in LLMs" (arXiv:2504.03814) | R2 | Recursive training + distribution shift | 应引用（需验证真实性） |
| Buffa & Del Corro (2026) "Entropy Sentinel" (arXiv:2601.09001) | R2 | Entropy 做 LLM 监控 | 应引用（需验证真实性） |
| LLM-GC (WSDM 2026) | R2 | Granger + LLMs | 可选引用（需验证真实性） |
| Rate of Model Collapse (arXiv:2412.17646, 2024) | R2 | Collapse rate 理论分析 | 可选引用（需验证真实性） |

**R1 注意**：R2 建议的 2025-2026 年文献真实性未经独立验证，建议 Research Director 核实后再决定是否引用。

现有引用覆盖评价：对 model collapse 核心文献（Shumailov 2024, Dohmatob 2024/2025, Kazdan 2025, Schaeffer 2025）和 Granger causality 方法论（Granger 1969, Shojaie & Fox 2022）的引用充分。遗漏主要集中在 2025-2026 年最新 detection/monitoring 工作。

---

## External Review

**状态：未请求。** 项目配置中未启用外部审稿（paperreview.ai）。

---

## Visual Layout Check（非评分项）

**状态：已完成**（耗时 ~4 分钟）

| 严重度 | 位置 | 发现 |
|--------|------|------|
| **critical** | Page 36 | 最后一页仅左栏顶部 ~6 行，~85% 空白。建议合并或扩充 |
| **warning** | Page 9 | 主文 Conclusion 延伸到第 9 页约 15-20 行。正文约 8.2 页，超页风险（与 W4 一致） |
| **warning** | Page 14 | Appendix 页面几乎全为密集文本，无 figure/equation 视觉间断 |
| **info** | Page 5 | Figure 4(b) 的 y 轴标签和 legend 字号偏小 |
| **info** | Page 6 | Figure 5 彩色方块较小，灰度打印时难区分 |
| **info** | Page 25 | Appendix 页面密度极高（多图表挤压） |
| **info** | Pages 21, 30 | 数学推导页纯文本+公式，无视觉间断 |

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |

### Overall: 3.0 — Findings

两位 Reviewer 独立且一致地评估为 **3.0 Findings**。

**核心判断依据：**

1. **贡献定位问题**：论文最强的贡献是方法敏感性的实证发现（FPR 6.7%→94.4%），但论文将 "phase transition discovery" 作为第一贡献——这一 claim 的证据基础（3 seeds, CI [0.25, 0.92], steepness 不确定性 ~100%）不足以支撑 Conference 级别的 novelty。
2. **方法论新颖性**：核心方法（PermG + first-differencing + BH-FDR）是成熟工具的应用，MMCT 是简单的 weighted voting。作为 empirical study 有价值，但方法论贡献有限。
3. **Generalizability 缺口**：Phase diagram 是 Pythia-410M + WikiText-103 specific。Cross-architecture 仅 α=1.0。单一数据集。
4. **Blind zone 的 framing 张力**：框架在 α < 0.50 时完全失效，但叙事暗示实用检测能力。

**升至 3.5 Borderline Conference 的条件（两位 Reviewer 共识）：**
1. Phase diagram 增至 ≥10 seeds 并报告 α_c 的 bootstrap CI
2. 至少在 1 个非 Pythia 架构上验证 intermediate-α phase diagram 结构
3. 第二 domain（如 C4）的核心实验复现
4. 将 framing 从 "phase transition discovery" 重新定位为 "empirical characterization of detection limits"
5. 修正 "sharp transition" 措辞以匹配统计证据强度
6. 解决正文超页问题

**不建议降至 2.5 的原因：** 实验质量高、统计控制严格、self-awareness 良好、方法敏感性发现对社区有实际警示价值。

### Confidence: 4/5
两位 Reviewer 均仔细阅读全部 36 页（含 26 页 appendix），熟悉时间序列因果检验和 model collapse 文献。

---

## Detailed Comments（逐节）

### Abstract
- 约 158-160 词，符合 200 词限制（R2 验证，R1-W9 不成立）
- "sharp detection phase transition" 需弱化为 "steep" 或 "abrupt"
- "reduces peak perplexity by 64%" 需标注 "proof-of-concept under α=1.0"

### Section 1 (Introduction)
- "can we reliably detect the onset of model collapse?" 的叙事与 blind zone（α<0.50）存在张力——应更早地 scope practical claims
- Contribution 1 应重新定位：从 "identify a sharp detection phase transition" 到 "empirically characterize detection limits"
- Contribution 4 的 intervention 应降低 prominence，明确为 proof-of-concept

### Section 2 (Related Work)
- 覆盖充分，遗漏集中在 2025-2026 最新工作（见 Missing References）
- 与 distribution shift detection 更广文献的连接不足（Rabanser et al. 2019 等）

### Section 3 (Method)
- Design Principle 1-2 标签应改为 Proposition/Empirical Finding
- MMCT（Algorithm 1）与 Table 2 的 K≥3 scheme 关系需在正文中澄清
- 建议排除 NaiveXCor（FPR 94.4%）的 robustness check

### Section 4 (Experiments)
- Phase diagram（Figure 1）需更多 seeds 或显式报告 boundary uncertainty
- α=0.60 anomaly 需直接 cross-correlation 证据
- Cross-architecture（Section 4.5）标题应改为 "Cross-Architecture Evaluation at α=1.0"
- Intervention（Section 4.6）需在中等 contamination（α≈0.50）验证

### Section 5 (Discussion)
- 写作质量良好，对 limitations 的讨论坦诚
- "measurement resolution asymmetry" 的讨论与 Design Principle 标签的张力应解决

### Section 6 (Conclusion)
- 需压缩以解决超页问题

### Limitations
- 内容充分，覆盖 scope/power/causality 三个方面
- "confirmation tool rather than early-warning system" 的定位应前移到 abstract/introduction

### Appendix
- 内容极为充实（26 页），支撑主文 claims
- 部分页面密度过高（视觉审查 Page 14, 25）
- 最后一页（Page 36）85% 空白，建议合并