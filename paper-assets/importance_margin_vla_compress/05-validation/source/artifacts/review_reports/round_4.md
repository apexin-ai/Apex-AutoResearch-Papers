---
round: 4
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-21T14:32:28.972562+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: "Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility"
**Venue**: CoRL 2026 | **Deadline**: 2026-05-29
**Reviewers**: R1（实验严谨性 + 方法技术）, R2（新颖性 + 定位 + venue fit）
**审稿模式**: Fresh（独立初审）

---

## Summary

本文系统研究了 7 个 VLA 模型（450M–7B）跨三类 vision connector（linear projection / MLP projector / pixel-shuffle）的 token pruning 行为，在 LIBERO 仿真基准上提出四类可压缩性分类（uniformly critical / threshold-graded / smooth graded / catastrophic cliff），用 token importance CV 作为零成本预测指标，并提出 VTR（Vision Token Re-encoder）在 pixel-shuffle 架构的 catastrophic cliff 下恢复 60%+ 成功率。论文选题精准、实验覆盖广、写作质量高，但核心因果声明证据不足、CV predictor 验证数据点过少、SmolVLA baseline 差距大，且正文超出 CoRL 8 页限制。

---

## Strengths

- **S1 [共识]** 问题定义精准且有实际意义。VLA token pruning 的跨架构不对称行为是被忽视但部署高度相关的问题。CoRL 社区直接相关。

- **S2 [共识]** 跨架构覆盖面在 VLA efficiency 文献中少见：7 个模型、3 类 connector、多 pruning 策略和 ratio、每配置 500 episodes closed-loop 评估。Table 1 taxonomy 直觉清晰。

- **S3 [共识]** π₀.5 在 k=0.5 处 L2 vs random 的 36pp 差距是本文最有价值的实验发现，证明 offline proxy 不可靠且低 CV 模型存在方法依赖性。SmolVLA 的 catastrophic cliff（5% removal → 0% SR）同样有说明力。

- **S4 [共识]** VTR 实验设计有控制意识：extended training control（45.0% vs 44.8%）排除额外训练步数，MLP adapter 对照排除特定架构贡献。

- **S5 [共识]** 写作清晰，结构合理，Table 1 标注系统（†‡§‖）和 Limitations section 诚实度高于平均水平。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-C1 [critical, 共识] 因果声明 under-identified——connector type 与多个架构变量混淆**

论文使用 "determines"、"strongly implicates" 等因果语言（Section 1, 5.1），但三个 connector 家族的模型同时在 vision encoder、LLM backbone、action head、训练流程上不同。π₀–OpenVLA 被称为 "most controlled comparison"（Section 3.2），实际有 connector + backbone + encoder fusion 三变量不同。Within-connector 比较（OFT vs OpenVLA）仅证明家族内一致性，无法推广为跨家族因果。缺乏 controlled connector-swap 实验（同 backbone 不同 connector）。

- R1: AGREE (W3) — "correlation, not causation"
- R2: critical N1 — 核心 contribution 的因果基础不成立
- 交叉回应：R1 完全 AGREE R2-N1，认为 R2 论证更系统

**W-C2 [critical, 共识] SmolVLA baseline 44.8% 远低于官方 87.3%，cliff-edge 和 VTR 可推广性存疑**

42.5pp gap（batch size 4 vs 64）。Official checkpoint (59.2%) 仅验证了一个 VTR 配置（M=32: 53.4%），无完整 pruning sweep。VTR 的 60.1% > baseline 44.8% 可能部分补偿 undertrained 缺陷。Cliff-edge 的 sharpness 可能被 undertrained checkpoint 放大。

- R1: critical N1
- R2: 交叉回应中 AGREE 并追加两个观察
- 共识：official checkpoint 完整 pruning sweep 是 minimum requirement

**W-C3 [critical, 共识] CV predictor 仅 3 模型 × 2 k 值 = 6 数据点，k=0.3 存在 reversal**

Table 3 的 CV scaling law 统计上远未达到可靠结论。3 个数据点实际是 3 个簇（与 connector 标签等价），CV 无超越 connector label 的额外预测力。CV 范围两端（π₀, SmolVLA）缺 L2 vs random 对比。Taxonomy 边界无形式化标准。Perceiver/Q-Former 类 connector 完全缺失。

- R1: critical N2
- R2: critical N2 — 补充"3 簇 = connector label"论点
- 交叉回应：双方强烈一致

**W-C4 [critical, 共识] π₀ 仅 offline 评估但用于核心论证**

Table 1 中 π₀ 与 π₀.5 并列为 "uniformly critical"，无标注区分评估协议。π₀–OpenVLA 63pp gap 是 offline loss vs closed-loop SR 的不可比对比。论文自身论证 offline metrics 不可信（Section 5.4），但 π₀ 仍用于核心 taxonomy 和 "connector determines" 论证。有完整 closed-loop pruning sweep 的仅 4 个模型（SmolVLA, OpenVLA, X-VLA, π₀.5），"seven models" 表述有夸大。

- R1: critical N3
- R2: 交叉回应 AGREE — internal consistency 问题

### Should-Fix（影响评分但不一票否决）

**W-S1 [warning, 共识] X-VLA "linear projection" 分类标签与 12-layer BART encoder 不匹配**
Table 1 标签误导。X-VLA CV=0.151 远高于纯 linear（0.038-0.055），更接近 MLP（0.215）。暴露三分类粒度不足，暗示 connector 复杂度是连续谱。（R1-W5, R2 强烈 AGREE）

**W-S2 [warning, 共识] OpenVLA L2 vs random 用不同 seed，k=0.5 same-seed 验证缺失**
Table 3 中 OpenVLA Δ(R−L2)=−1.8pp 是 CV scaling law 最关键的 crossover point，seed variance 可能翻转符号。（R1-W1, R2 AGREE）

**W-S3 [warning, 共识] VTR 新颖性有限——Perceiver/Q-Former 的 VLA 应用**
VTR 架构与 Perceiver/Q-Former 功能等价。MLP adapter SR 更高（63.4% vs 60.1%）。贡献在于诊断 why re-encoding 而非方法本身。（R2-W2, R1 AGREE）

**W-S4 [warning, 共识] VTR p=0.15 不足以声称 "re-encoding is the operative mechanism"**
MLP adapter 实际 SR 更高。更准确解读是"两者无显著差异，benefit from learned re-encoding in general"。（R1-W2, R2 AGREE）

**W-S5 [warning, 共识] "Diagnose-then-Compress framework" 过度包装**
实质是 single-metric lookup table。验证不足以支撑 "framework" 标签。（R2-W4, R1 AGREE）

**W-S6 [warning, 共识] 正文约 13 页，超 CoRL 8 页限制约 5 页**
Section 5（Analysis）约 3 页是超页主因。需大幅压缩或移入 Appendix。（R2-W5, R1 AGREE）

**W-S7 [warning, 共识] "Falsifies immune assumption" 措辞过强**
π₀/π₀.5 原始论文未声称 pruning immunity。发现本身有价值但 "falsifies" 构成稻草人论证。（R2-W1, R1 部分 AGREE — 同意措辞需降级）

**W-S8 [warning] M=96 dip（54.5±3.2%）与 "flat M-curve" 叙述不完全一致**
R1 认为破坏叙述，R2 认为 CI overlap 可能是 noise。建议改 "flat" 为 "relatively stable"。（R1-W4, R2 部分 REBUT）

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成完全一致 [AGREE]：

1. **因果声明证据不足**（W-C1）："determines" 需降级为 "is strongly associated with"，缺乏 controlled connector-swap 实验
2. **CV predictor 验证严重不足**（W-C3）：3 个数据点 = 3 个 connector 簇，无超越标签的额外预测力
3. **π₀ offline-only 问题**（W-C4）：不应与 closed-loop 结果并列用于核心论证
4. **SmolVLA baseline gap**（W-C2）：official checkpoint 完整 pruning sweep 是 minimum requirement
5. **VTR 新颖性定位**（W-S3）：贡献在诊断 why re-encoding，非方法本身
6. **正文超页**（W-S6）：约 13 页 vs 8 页限制，需大幅压缩
7. **"七模型" framing 夸大**（W-C4）：完整 closed-loop 仅 4 个

---

## Reviewer Divergence

**分歧 1：Simulation-only 评估的严重性**
- R2：列为 critical（N3），引用 CoRL 2026 CFP 要求 real-robot 或 sim-to-real evidence
- R1：REBUT — R2 引用的 CoRL policy 在公开文档中未找到；CoRL 历史接受 sim-only 分析论文；7 架构全做 real-robot 不合理。但同意缺乏 sim-to-real 讨论
- **Director 判断**：降为 should-fix。论文核心贡献是架构级理解，simulation 的控制性是必要条件。但需增加 sim-to-real 讨论，说明 CV 是 architecture 属性而非 environment 属性

**分歧 2：M=96 dip 是否破坏 flat M-curve 叙述**
- R1：W4，认为 7.5pp 差异不可忽略
- R2：REBUT — CI overlap，更可能是 noise
- **Director 判断**：将 "flat" 改为 "relatively stable" 是充分的修复

---

## Questions for Authors

1. SmolVLA official checkpoint (59.2%) 是否在所有 k 值下均 0% SR？（R1-Q1）
2. CV=0.15 threshold 是 post-hoc 选择还是有先验依据？（R1-Q2）
3. VTR 在 OpenVLA 上 0% SR（含 passthrough M=128）的机制是什么？对 workflow 实用性的影响？（R1-Q3）
4. 是否考虑过 controlled connector-swap 实验（同 backbone 不同 connector）？（R2-Q1）
5. Perceiver-based VLA（如 Octo）会落入 taxonomy 哪个类别？（R2-Q2）
6. VTR 60.1% vs baseline 59.2% 的统计显著性？（R2-Q6）
7. π₀.5 V-shaped L2 curve 的 spatial clustering 假设是否有 attention map 或 token position 分析验证？（R1-Q4）

---

## Missing References

- "Don't Run with Scissors" (Jabbour et al.)：已引用但对比讨论不充分——该工作也研究 VLA pruning failure and recovery，Related Work 应增加对比
- FastV (Chen et al., 2024)：VLM token pruning 重要 baseline，仅 Related Work 提及一次，建议增加在 VLA 上的适用性讨论
- 引用验证结果：41 篇中 30 篇 verified，5 篇 not_found（近期 arXiv 预印本，OpenAlex 未收录），6 篇 minor first-author mismatch，**无虚假引用**

---

## External Review (Stanford Agentic Reviewer)

未配置，未请求。

---

## Visual Layout Check（非评分项）

状态：**done**（2026-05-21 14:07 → 14:10）

主要发现（3 warning, 9 info）：
- **[warning]** 前 3 页（pp.1-3）纯文本无任何 display item，审稿人第一印象窗口内只看到文字墙。Figure 1 应提前到 page 1-2
- **[warning]** pp.11-13（Analysis + Conclusion）连续 3 页纯文本，缺辅助 figure/table
- **[warning]** pp.5-6 方法描述密集无视觉辅助（Pruning Protocol + VTR + Diagnostic Metrics）
- **[info]** 正文仅 2 figure + 3 table = 5 display items / 13 页，对实证论文偏少。大量实验结果被推到 appendix
- **[info]** Figure 4（attention entropy）仅在 appendix，未被正文利用
- **[info]** Figure 1 架构图清晰但出现在 page 4，错过锚定时机

注：正文超页（~13 页）是排版问题的根本原因。压缩至 8 页后 display item 密度将大幅改善。

---

## Overall Assessment

### 评分：Weak Reject

### 置信度：High

### 理由

论文选择了一个重要且及时的问题（VLA 架构对 token pruning 的不对称响应），实验执行扎实（多模型、多策略、closed-loop、500 episodes），写作质量在平均水平之上。π₀.5 的 L2 vs random 36pp 差距、SmolVLA 的 catastrophic cliff 发现、以及 offline-vs-closed-loop disconnect 的展示都有实际价值。

但四个结构性问题制约了 contributions 的可靠性：

1. **因果声明缺乏实验基础**（W-C1）：三个 connector 家族的模型在 encoder/backbone/action head 上同时不同，"determines" 级因果语言无法成立。这直接影响 Contribution 1 的核心 claim。

2. **CV predictor 验证严重不足**（W-C3）：3 个模型的 CV 值与 3 个 connector 标签一一对应，CV 实际未提供超越 connector 分类的额外预测力。k=0.3 reversal 进一步削弱了 "dual predictor" 的稳健性。这直接影响 Contribution 2。

3. **SmolVLA baseline 42.5pp gap**（W-C2）：cliff-edge 和 VTR 结论建立在严重 undertrained 的 checkpoint 上，official checkpoint 仅验证了一个配置。这直接影响 Contribution 3。

4. **π₀ offline-only 用于核心论证**（W-C4）：论文自身论证 offline 不可靠，但 π₀ 的 offline 结果仍用于支撑 taxonomy 分类和跨架构 comparison。

### 升级路径

如果 rebuttal 能提供以下任一：
- (a) Official SmolVLA checkpoint 完整 pruning sweep（确认 cliff-edge 在更高 baseline 下成立）
- (b) 将因果语言全面降级为关联性表述
- (c) k=0.5 same-seed 验证 + 增加 1-2 模型的 CV scaling law 数据点
- (d) 正文压缩至 8 页

论文有潜力升至 **borderline accept**。核心实验覆盖面和诊断性发现是实质贡献，问题主要在 claim 强度与证据的匹配。

---

## Detailed Comments

### Section 1 (Introduction)
- "The vision connector, not model size or action head, determines pruning behavior" → 改为 "is strongly associated with"
- "falsifies the 'immune' interpretation" → π₀/π₀.5 原始论文未做此 claim，改为 "demonstrates that offline tolerance does not generalize to closed-loop"
- "seven VLA models" → 加限定 "(four with closed-loop evaluation)"
- π₀-OpenVLA 63pp gap 首次出现时加 caveat（connector + backbone + encoder 三变量不同）

### Section 3 (Methods)
- Section 3.2: "most controlled available comparison" 首次出现时需明确列出三个不同变量，而非仅在 Limitations 讨论
- Table 1: π₀ 行加 "offline only" 标注；X-VLA Connector 列改为 "Linear proj + 12-layer BART"；CogACT 行明确标注 "literature result, not our evaluation"

### Section 4 (Results)
- Section 4.2: Official checkpoint 完整 pruning sweep 是 critical requirement
- Section 4.5: "flat M-curve" → "relatively stable M-curve"；增加 M=96 dip 讨论
- Section 4.6: Table 3 的 OpenVLA 行标注 cross-seed；CV predictor claim 降级

### Section 5 (Analysis)
- 大部分内容（5.1, 5.3, 5.4）移入 Appendix 以满足页数限制
- Section 5.2: "CV predicts" → "CV correlates with"
- Section 5.3: "re-encoding is the operative mechanism" → "both cross-attention and MLP achieve comparable recovery"

### Section 6 (Conclusion)
- "Diagnose-then-Compress framework" → "diagnostic protocol"
- "four findings" 叙述需与降级后的 claim 强度一致