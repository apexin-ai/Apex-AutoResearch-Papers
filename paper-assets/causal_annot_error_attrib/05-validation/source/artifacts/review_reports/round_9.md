---
round: 9
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T03:04:33.811202+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction

**Venue**: EMNLP 2026 (ARR May Cycle) | **类型**: Long Paper | **Round**: 9 (Fresh)
**Reviewers**: R1 (方法严谨性+实验验证), R2 (新颖性+完整性+写作呈现)

---

## Summary

本文研究 LLM 标注产生的 K-class 非差异误分类在因果推断中的传播，核心发现是传播方式取决于 DAG 拓扑而非标注准确率。论文为 7 种标准 DAG 拓扑推导闭式偏差表达式，证明 K≥3 引入 K=2 不存在的 sign reversal 可能性（exposure 83.4%、IV 52.6%），提出 Annotation Sensitivity Values (ASV) 诊断框架（含 magnitude/significance/sign-flip 三种度量），并证明 FWL 不变性使矩阵校正对 4 种协变量拓扑无效。通过 100,000 随机矩阵和 23 个真实 LLM 混淆矩阵验证。

---

## Strengths

1. **问题定义的新颖性和时效性**：首次在统一框架下对 7 种 DAG 拓扑 × K-class 误分类推导闭式偏差表达式并进行跨拓扑对比，填补了 NLP×因果推断文献中的空白。[R1, R2 共识]

2. **"拓扑 > 准确率"的反直觉洞见**：在 F₁ 0.614-0.690 范围内偏差变化 10×（IV 42.1% vs collider <5.6%），挑战了"提高标注准确率即可解决下游问题"的常见假设。[R1, R2 共识]

3. **K=2 理论的严谨性**：Theorem 1 的单调性证明结构完整（凸性 + 端点条件），Proposition 1 的 sign preservation 对 confounding/collider 给出解析证明，证明路径有独立方法论价值。[R1 主导]

4. **理论结果的诚实分层**：明确区分 Theorem（证明）→ Proposition（部分证明）→ Observation（数值验证）→ Conjecture（猜想）四级层次，学术诚信度高。[R1, R2 共识]

5. **FWL 不变性的否定结果**：证明 matrix-based correction 对 4 个协变量拓扑 provably ineffective，帮助研究者避免无效纠偏策略——一个有实用价值的否定结论。[R1, R2 共识]

6. **丰富的附录**：20 页附录包含完整证明、多个稳健性检验（non-differential stress test、cross-K、logistic DGP、bootstrap uncertainty），显著增强可信度和可复现性。[R1, R2 共识]

---

## Weaknesses

### CRITICAL

**C1. 核心假设在 LLM 场景中缺乏实证验证** [R1-N1, R2 AGREE]

论文框架建立在两个关键假设上——(1) 非差异性误分类 P(A*|A,Y,Z)=P(A*|A)，(2) proportional effects (f=λg)——但未提供任何实证证据表明这些假设在 LLM 标注场景中近似成立。

- **非差异性**：Appendix B.5 的 stress test 使用均匀 ε-perturbation，无法捕捉 LLM 的结构性差异误差（如 content-dependent differential error：LLM 对情感极性明确文本更准确，导致 P(A*|A) 依赖于 Y）。论文缺乏按 outcome 分层估计条件混淆矩阵 P(A*|A,Y=y) 的实证检验。
- **比例效应**：Appendix B.12 显示 λ(C) 越界率在独立 f 时饱和于 ~23%，但论文未论证 LLM 混淆矩阵为何应满足比例效应。R2 补充：即使违反，sign failure rate 始终 <1%，说明 sign preservation 仍 robust。但 R1 建议用 23 个真实混淆矩阵定量评估 f/g 变异系数——这是低成本高价值的检验。

**C2. 线性 SEM 假设对 EMNLP 读者的可达性和泛化性严重不足** [R2-N2, R1-W2, 交叉后共识升为 CRITICAL]

论文正文仅用一句话提及 logistic DGP 结果（Section 5）。对于 EMNLP 的核心读者群（NLP 研究者），线性 SEM 与现代 NLP pipeline 的差距如果不在 Method 部分早期讨论，会严重影响 venue fit。Appendix B.6（logistic DGP sign-flip 稳定性）和 B.13（FWL logistic 验证）提供了有价值的稳健性证据，但被藏在附录中。建议在 Section 3.1 增加 1-2 句解释为何从线性 SEM 出发，并将 B.6/B.13 核心结论提升到正文。

### MAJOR

**M1. K≥3 理论基础不完整，而 K≥3 是 NLP 的主要应用场景** [R1-W1, R2-W4, 共识]

K=2 理论严格，但 K≥3（NLP 绝大多数任务的场景）的核心性质——envelope monotonicity——止步于 Observation 1（20,000 次数值验证）和 Conjecture 1（30,000 矩阵/topology），ASV 框架和 Algorithm 1 的实用指导依赖这些未证明的结果。论文标注诚实，但应讨论证明的技术障碍：是 K≥3 列随机矩阵的谱性质不再保证 convexity 结构，还是存在潜在反例？

**M2. ASV 框架的可操作性（actionability）展示不足** [R2-W1, R1 AGREE]

ASV 定位为 "diagnostics"，但缺少端到端使用场景：从业者如何获取所需输入（C₀、DAG topology），如何解释三种 ASV 数值，如何据此决策？Algorithm 1 在 Appendix 最后一页，与主文 ASV 连接不紧。建议在主文用 2-3 行总结 Algorithm 1 核心逻辑，或增加 practitioner walkthrough。

### SHOULD-FIX

**S1. "first to characterize" novelty claim 需更精确限定** [R2-N1 critical → R1 建议降为 should-fix, 共识降级]

Brenner (1993) 覆盖 polytomous confounder，Teblunthuis (2024) 覆盖单拓扑回归偏差，Ogburn & VanderWeele (2012) 覆盖 binary confounder 单调性。论文实际新颖性在于 7 拓扑 × K-class 的闭式联合对比。建议修改为 "first unified analysis across seven topologies" 并在 Section 1 贡献列表中明确 "building on" 先驱工作。R1 认为论文新颖性不依赖 "first" 措辞，降为 should-fix 合理。

**S2. Abstract 中 2.1% sign reversal 聚合数字掩盖拓扑间差异** [R2-W3, R1 AGREE]

2.1% 是跨所有拓扑×系数的平均值，而 IV 42.1%、exposure 83.4%（Dirichlet 下）。这个聚合数字恰恰掩盖了论文 "topology-dependent" 的核心主张。建议报告 range 或加限定语。

**S3. 经验验证的 LLM 配置多样性有限** [R1-W3, R2-W2, 共识]

4 个开源 LLM 规模相近（缺 <7B 和 >70B），3 个英文数据集任务类型偏分类（缺序数标注），23 个配置不足以支撑 primary coefficient 普遍性声明。建议增加不同规模/架构的 LLM 或讨论混淆矩阵参数空间覆盖度。

**S4. PPI++ grand-mean RMSE reduction 数字不一致** [R1-W4/Q5, R2 确认]

Section 4.5 正文报告 "grand-mean RMSE reduction (47.0%)"，但 Table 4 Grand mean 行 PPI++ 列为 17.0。作者必须澄清 47.0% 的计算口径（是否仅限 protective topologies）或修正数字。

### MINOR

- Figure 1 字体小、Figure 2 y 轴标签小 + 红绿配色对色觉障碍不友好、Table 1 ✗/✓ 黑白打印难区分 [R1, R2]
- "plim"（probability limit）对 NLP 读者不常见，首次出现应加定义 [R1, R2]
- Section 3.2 拓扑间过渡突然，符号密度高 [R1, R2]
- Appendix B.1 binarization collapse（K=3→binary 引入 154× 额外偏差）在主文中提及不足 [R1]
- 多标注者设定对 confusion matrix 估计的影响未讨论 [R2]
- Appendix Table 2（sign preservation 充分条件总结）非常有价值，建议在主文更明确引用 [R1]

---

## Reviewer Consensus

两位 Reviewer 在以下问题上高度一致（交叉回应中全部 [AGREE]）：

1. **假设验证不足是核心瓶颈**：非差异性和比例效应假设在 LLM 场景中的合理性缺乏实证支持，这是论文从 Borderline 上升到 Conference 的关键障碍
2. **K≥3 理论不完整**：对 NLP 主要应用场景的覆盖止步于数值验证和猜想
3. **线性 SEM 讨论不足**：需在正文早期建立与 NLP 实践的连接
4. **LLM 配置多样性有限**：规模和任务类型覆盖面需扩展
5. **PPI++ 数字不一致**：需澄清或修正
6. **2.1% 聚合数字有误导性**：应报告 range

---

## Reviewer Divergence

仅在严重程度和 minor 点上存在分歧，无实质性矛盾：

1. **R2-N1 (overclaiming) 严重程度**：R2 列为 critical，R1 建议降为 should-fix（论文新颖性不依赖 "first" 措辞）。→ 报告中采纳 should-fix。
2. **R2-W5 (sensitivity analysis 文献覆盖)**：R2 列为 should-fix，R1 rebut（论文已引用 Lash et al. 2009 和定位 ASV vs E-value），建议降为 minor。→ 报告中采纳 minor。
3. **R1-m3 (Table 2 移入主文)**：R2 rebut（页面预算不允许），建议更明确的交叉引用。→ 采纳 minor。
4. **R1-m4 ("topology" 术语)**：R2 rebut（因果推断文献标准用法）。→ 不列入报告。

---

## Questions

1. **[R1-Q1]** 能否用 23 个真实 LLM 混淆矩阵定量评估 proportional effects 近似程度（计算 f/g 变异系数）？[R2 AGREE: 低成本高价值]
2. **[R1-Q2]** 是否存在可构造的混淆矩阵（满足 non-differential + 合理精度）使 primary coefficient 反转？如果存在需什么条件？[R2 AGREE: 理论边界问题]
3. **[R1-Q3]** ASV 排序在不同 DGP 参数化（系数大小、误差方差）下是否稳定？Appendix B.10 部分回答（β alternating/same-sign），但未覆盖更复杂的多变量交互效应场景。[R2 部分 REBUT: B.10 已覆盖基本情况]
4. **[R1-Q4]** Collider 的结构独特性在非线性 DGP + 线性估计时是否保持？Appendix B.6 中 collider logistic sign-flip 为 0.000 但仅测 K=3。[R2 AGREE: 需更详细分析]
5. **[R1-Q5]** Section 4.5 PPI++ "grand-mean RMSE reduction (47.0%)" vs Table 4 Grand mean 17.0——请澄清。[R2 AGREE: 明确不一致]

---

## Missing References

论文引用覆盖面总体良好。以下为可选补充（非必需）：
- Bound, Brown, and Mathiowetz (2001) — 测量误差综述（已引用 Carroll et al. 2006）。低优先级。
- VanderWeele (2015) — mediation 教材。低优先级。
- 未发现 fabricated citations。引用格式符合 ACL natbib 规范。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。项目配置中外部审稿未启用。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 因速率限制出错（agent exited: rate limit hit），未完成实际 PDF 渲染审查。完成后会自动补发到 Group C。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 4/5 | 3.75/5 |
| Excitement | 3.5/5 | 3/5 | 3.25/5 |
| Overall | 3.5/5 | 3.5/5 | **3.5/5** |

**综合判断**：论文对一个重要且新颖的问题做出了实质性贡献。K=2 理论严格，"拓扑 > 准确率"洞见有概念和实践价值，FWL 不变性否定结果实用。但以下因素阻止了更高评分：

1. **实践相关性缺口**：核心假设（非差异性、比例效应、线性 SEM）在 LLM 标注场景中的合理性未经实证验证，框架对目标用户（NLP 因果推断研究者）的可用性存疑
2. **理论完整性缺口**：K≥3（NLP 主要场景）的核心性质止步于 conjecture
3. **贡献偏增量**：各单项贡献（多分类偏差分析是经典测量误差理论的推广，ASV 是灵敏度分析工具的变体，FWL 不变性是已知定理的应用）的新颖性中等

**从 Borderline 到 Conference 的关键路径**：
- 用 23 个真实混淆矩阵定量评估 proportional effects 近似程度（Q1）
- 在正文 Section 3.1 解释线性 SEM 选择动机 + 提升 B.6/B.13 核心结论
- 修正 PPI++ 数字不一致
- Abstract 中 2.1% 改为报告 topology-specific range

**置信度**: 4/5（两位 Reviewer 仔细阅读正文+附录，交叉回应后高度一致）

---

## Detailed Comments

### Abstract (page 1)
- "the sign reversal rate is 2.1%" → 改为报告 topology-dependent range（如 "0% for confounding to over 40% for IV under realistic accuracy"），当前聚合数字与论文核心主张矛盾 [S2]
- "Topology-aware analysis is necessary" → R2 认为过于绝对（confounding 下即使不做 topology-aware 分析偏差方向也可预测），R1 rebut 认为合理。保留但可考虑软化为 "critical"

### Section 1 Introduction (pages 1-2)
- "No prior work systematically characterizes..." → 加入 "extending prior single-topology analyses (Brenner 1993; Teblunthuis et al. 2024)" 的限定语 [S1]
- Contribution 2: "Annotation Sensitivity Values" 可操作性需在主文强化——至少用 2-3 行总结 Algorithm 1 的核心逻辑 [M2]

### Section 3.1 Setup (page 3)
- 增加 1-2 句解释为何从线性 SEM 出发（标准分析起点、允许闭式解、B.6 logistic 验证提供稳健性保证）[C2]
- "plim" 首次出现时加括号定义 [minor]

### Section 3.2 Bias Expressions (pages 3-5)
- 拓扑间过渡可加简短引导句 [minor]
- Proportional effects (f=λg)：在 Theorem 1 后增加讨论——用 23 个真实混淆矩阵评估 f/g 近似程度 [C1]

### Section 3.3 ASV (pages 5-6)
- Conjecture 1：增加 1-2 句讨论证明障碍（K≥3 自由度增长 vs bounding 策略）[M1]
- ASV 与 E-value 的区别可用一句话更明确（"While E-values quantify unmeasured confounding tolerance, ASV quantifies annotation error tolerance"）[minor]

### Section 4 Experiments (pages 6-8)
- Section 4.2 sign reversal 呈现：正文中 exposure 2.1% 与 IV 42.1% 的对比应更突出 [S2]
- Section 4.4 empirical validation：讨论 23 个配置的参数空间覆盖度 [S3]
- Section 4.5 PPI++：47.0% vs Table 4 Grand mean 17.0 数字不一致——必须修正 [S4]
- 将 B.6/B.13 核心结论（logistic DGP 下 sign-flip 稳定性 + FWL breakdown negligible）提升到 Section 4 用 1-2 句总结 [C2]

### Section 5 Conclusion (page 8)
- "empirical regularity driven by magnitude dominance" 措辞合理，保持 [R1 认可]

### Limitations (page 9)
- 非线性模型适用性讨论需加强：何种条件下线性近似合理、何时可能失效 [C2]
- 增加多标注者设定对 confusion matrix 估计影响的讨论 [minor]

### Figures/Tables
- Figure 1: 增大节点标签字号 [minor]
- Figure 2: 增大 y 轴标签 + 改用色觉友好配色 [minor]
- Table 1: ✗/✓ 改为 Yes/No 或不同填充模式 [minor]