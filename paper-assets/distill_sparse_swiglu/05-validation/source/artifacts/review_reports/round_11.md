---
round: 11
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-19T08:07:39.377825+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 12 审稿报告（Fresh Review）

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026（ARR May 2026 cycle）
**Reviewers**: R1（方法严谨性+实验可靠性）、R2（新颖性+完整性+写作质量）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达成共识）

---

## Summary

本文提出用 forward KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器（75.9M 参数，<1% 基础模型），通过 Gumbel-Sigmoid 松弛实现端到端可微训练。核心发现：(1) KL 训练的 mask 与激活幅值 mask 有 68% 差异（per-layer Jaccard 32%），C1 target-swap 消融证实 mask 质量（而非梯度耦合机制本身）是推理质量的近因驱动；(2) 在 LLaMA-3.1-8B 30% 稀疏度下 PPL 降低 18%（8.96 vs TEAL 10.97），补偿网络（+67.2M 参数）变冗余；(3) 分析了稀疏度-分配策略的三段式交互（budget-surplus / budget-constrained / capacity-limited）。跨架构验证包括 Mistral-7B（5/6 tasks KL 优势）和 Qwen-2.5-14B（PPL 泛化但 MMLU 逆转 -8.1pp）。

---

## Strengths

**S1. 问题定义精准。** BCE 逐神经元独立训练与 TEAL 全局 top-k 推理分配的 mismatch 被准确识别且此前未被正式分析。梯度分析（§3.6）从结构上解释了两种目标的差异，提供了理论动机。[R1, R2 共识]

**S2. C1 target-swap 消融设计巧妙。** 将 mask target quality 与 gradient coupling 解耦（BCE 在 KL-derived masks 上训练复现 KL 质量，magnitude-trained BCE 差 2.4×），是本文最有价值的实验设计。[R1, R2 共识]

**S3. 消融实验系统全面。** Table 4 层层隔离 divergence direction、relaxation method、loss function、compensation 的贡献，实验设计规范且在同类工作中少见。[R1, R2 共识]

**S4. 跨架构评估诚实。** Mistral-7B（GSM8K 反转）、Qwen-14B（MMLU 反转 -8.1pp）的负面结果被正面讨论，体现科学诚信。[R1, R2 共识]

**S5. 写作质量高。** 无 em-dash、无解释性 en-dash、无 AI 黑名单用词（leverage/delve/utilize）、无过度分段。叙事线（mismatch → gradient analysis → mask discovery → causal ablation）连贯。[R2 发现, R1 同意]

**S6. Taxonomy 定位准确。** correction granularity × training signal coupling 的 2D 分类法组织清晰，Per-token × Coupled 确为未探索组合。[R1, R2 共识]

**S7. 超参数鲁棒性充分。** Bottleneck dimension (<3%)、temperature schedule (<1.8%)、training convergence (800步饱和) 的敏感性分析增强可信度。[R1, R2 共识]

---

## Weaknesses

### Critical (Must-Fix)

**N1. C1 消融 50% max Δ 数值错误。** [R1 发现, R2 交叉确认]
- 论文声称 "max Δ=0.59pp at 50% (2-seed)"（§4.4 + Table 3 caption），但 Table 3 中 50% s42 的 WinoGrande |63.14−62.35|=0.79pp，超过声称值。0.59pp 无法从任何可见数据推导。且 "2-seed" 声称但仅展示 1 seed pair。
- C1 是核心 contribution，定量证据错误直接削弱可信度。

**N2. Table 2 与 Table 4 BCE+Compensation 数值矛盾。** [R1 发现, R2 交叉确认]
- Table 2: "BCE + comp.∗" PPL 28.13±0.20 (3-seed)，脚注标注 "DejaVu/FastForward pipeline with compensation (67.2M params)"
- Table 4: "BCE + Compensation (hard mask)" PPL 25.44 (seed 42)
- std=0.20 意味所有 seed 在 27.93-28.33 范围，与 Table 4 的 25.44 相差 2.69pp，不可调和。§4.3 描述为 "BCE predictor" 非 "BCE+compensation"，怀疑 Table 2 脚注标注错误。
- "KL renders compensation redundant" 的定量基础不明。

**N3. 缺少 Intermediate-coupling (MSE) baseline。** [R1 提出 Must-Fix, R2 同意但建议 Should-Fix]
- Table 1 taxonomy 划分 Decomposed/Intermediate/Coupled 三级，暗示递进关系，但实验仅对比两端（BCE vs KL），Intermediate（per-layer MSE）完全缺席。ShadowLLM/D2DMoE 在 Related Work 讨论但无实验数据。
- Taxonomy 的核心价值——Coupled 优于 Intermediate——缺乏实验验证。至少需要简化版 per-layer MSE baseline。
- R1 定为 Must-Fix，R2 认为不影响核心 KL>BCE claim 但影响 taxonomy 完整性。**Director 判定：Should-Fix**（taxonomy 是概念贡献而非论文核心 claim，但如果作者希望保留 taxonomy 需补实验）。

### Warning (Should-Fix)

**W1. C1 "Causal Ablation" 命名过强，soft-vs-hard confound 未解决。** [R1, R2 共识]
- C1 同时改变 gradient coupling 和 mask representation（hard binary vs soft Gumbel-Sigmoid）。BCE+Gumbel 失败不能反证 softness 对 KL 不重要（loss × relaxation 可能有 interaction effect）。论文承认 "Disentangling remains for future work" 但标题仍用 "Causal"。
- 建议改为 "Target-Swap Ablation" 或 "Target Transfer Experiment"。

**W2. 14B MMLU 逆转仅 seed 42，统计效力不足。** [R1, R2 共识]
- Mistral-7B 和 Qwen-14B 所有结果均为单 seed。LLaMA-8B 已展示 MMLU 可达 σ=9.5pp 的跨 seed 方差，14B 反转可能是 seed 效应。
- 至少 3-seed 确认后才能对可扩展性下结论。

**W3. 无 wall-clock 加速，系统增加 6.4% 开销。** [R1, R2 共识]
- 同类方法（DejaVu/FastForward/Polar Sparsity/TEAL）均报告实际加速。本文在加速维度完全缺席。
- Abstract "renders compensation redundant" 误导读者期望速度提升，实际只节省 ~2.7% latency 开销。
- 论文已坦诚承认，但 framing 需更明确限定为 prediction quality study。

**W4. 方法新颖性有限。** [R2 提出, R1 部分同意]
- 核心技术为 BCE→KL loss swap + 标准 Gumbel-Sigmoid relaxation。与 MaskLLM 的区别（activation vs weight sparsity, predictor vs direct mask, global vs N:M）是问题设定差异而非方法创新。
- R1 反驳：两个方法有结构性差异，不应过度抽象。但同意论文的真正贡献是实证发现（mask divergence, C1 ablation, regime analysis）而非方法本身。
- 论文已定位为 "primarily empirical"，建议进一步强化。

**W5. 30% λ 饱和偏差 5%，train-inference mismatch。** [R1 提出, R2 同意并定量分析]
- 训练时实际稀疏度 28.5%，推理强制 30%。严格对比应为 KL@28.5% vs TEAL@28.5%（improvement 13% 而非宣称 18%）。
- Appendix 有 defense（TEAL@28.5% PPL=10.30，gap 0.67 远小于 KL 优势 2.01），但应在主文讨论。

**W6. 30% downstream 退化严重，"best quality" 表述不当。** [R2 提出, R1 同意]
- GSM8K 84% 退化（48.75→7.5%），MMLU 38% 退化（65.27→40.7%）。所有方法退化相近（说明是稀疏度固有限制），但 "best quality" 应改为 "least-degraded"。

**W7. Conclusion 仅两句话。** [R1, R2 共识]
- 无 future work、无 broader impact。至少补 N:M 结构化稀疏、更大规模验证等方向。

**W8. WikiText-103→WikiText-2 同源。** [R1, R2 共识]
- C4 OOD gap 更大（1.74× vs 1.46×），说明 partial overfitting。建议主表加 C4 PPL 列。

### Info (Minor)

**M1. 写作/编辑问题集合。** [R1, R2 共识]
- PPL 11.79 vs 11.80 不一致
- WINA 列为 baseline 但无实验数据
- "Phase transition" 术语过强（建议 "capacity cliff"）
- SNR "at convergence" 实际在 step 300 测量（训练 1000 步）
- "68% divergence" Introduction 中轻微重复
- HellaSwag/PIQA 未在 §4.1 Evaluation 提及
- s42† earlier checkpoint 解释不足
- SwiGLU 未在 Abstract 定义
- §2.5 自适应惩罚控制器篇幅比例偏大
- exp_id 注释需清理
- "in context of" → "in the context of"

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
1. **数值错误必须修正**：C1 max Δ (0.59→0.79pp) + Table 2/4 BCE 矛盾
2. **C1 命名过强**：应降级为 "Target-Swap Ablation"
3. **无 wall-clock 加速**：framing 需更明确限定贡献范围
4. **14B 单 seed 不足**：至少 3-seed 确认 MMLU 反转稳定性
5. **Findings 定位合理**：方法新颖性增量，但实证分析有价值
6. **Overall 3.0**：两人独立给出相同分数

## Reviewer Divergence

仅 2 项轻微分歧（已在交叉中达成共识）：
1. **MSE baseline 严重性**：R1=Must-Fix（taxonomy 需实验验证），R2=Should-Fix（不影响核心 claim）。Director 判定 Should-Fix。
2. **MaskLLM 技术距离**：R2 认为距离小（Must-Fix），R1 部分反驳（结构性差异存在但方法新颖性确实有限）。两人一致建议强化 empirical study 定位。

---

## Questions

以下问题由两位 Reviewer 共同或独立提出，需作者回应：

1. **Table 2/4 BCE 配置**：两个表格的 BCE+compensation 条目是否为同一实验？训练步数、seed、是否含 compensation？[R1-Q1, R2 交叉确认]
2. **C1 50% max Δ 计算来源**：0.59pp 如何得出？第二个 seed 数据？[R1-Q2]
3. **28.5% train-inference gap**：预测器是否在 30% 推理条件下验证/选择？严格对比下 improvement 为 13% 而非 18%？[R1-Q3, R2-Q4]
4. **14B MMLU 多 seed 稳定性**：-8.1pp 逆转是 systematic 还是 seed 效应？[R1-Q6, R2-Q1]
5. **KL-only 神经元贡献**：KL 选择但 magnitude 不选择的神经元对 output distribution 有什么实际贡献？[R2-Q2]
6. **GSM8K 反转机制**：forward KL 的 mass-covering 性质是否在 reasoning 任务上不如 mode-seeking？[R1-Q5, R2-Q3]
7. **C4 训练可能性**：在非 WikiText 数据上训练 predictor 能否减少 domain overfitting？[R2-Q5]

---

## Missing References

两位 Reviewer 一致认为引用覆盖良好（47 篇，密度合理）。无重大遗漏。
- R2 建议考虑 LLM.int8() (Dettmers et al., 2022)，R1 反驳：量化不在本文 scope 内，Wang et al. 2025 已覆盖 sparsity+quantization 交叉。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**未配置**。项目无 `external_review.paperreview_ai.enabled` 设置。

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0/5 | 3.5/5 | **3.0/5** — 核心方法正确，但数值错误（N1）和数据矛盾（N2）直接削弱核心 claim 可信度 |
| Excitement | 3.0/5 | 2.5/5 | **2.5/5** — KL 发现不同 mask pattern 有趣，但方法增量、无实际加速、规模受限 |
| Reproducibility | 4.0/5 | 4.0/5 | **4.0/5** — 超参数完整、3-seed、GPU 型号齐全；未开源代码 |
| Overall | 3.0/5 | 3.0/5 | **3.0/5 (Findings)** |
| Confidence | 4/5 | 4/5 | **4/5** |

**Overall Score: 3.0 (Findings)**

**推荐: Findings（修复 N1-N2 后可稳定；当前因数值错误在 Borderline Findings 2.5-3.0 边缘）**

**核心判断依据**:
1. **支撑 Findings 接收的因素**: C1 target-swap 消融是有价值的分析创新；mask divergence 发现（68%）提供了对 KL 训练行为的新理解；三段式 regime analysis 有实用参考价值；实验覆盖面广且报告诚实
2. **阻止 Main 接收的因素**: 方法新颖性增量（loss swap + 标准技术）；无 wall-clock 加速；14B 可扩展性存疑（MMLU 逆转且仅单 seed）；数值错误影响核心 claim 可信度
3. **修复优先级**: N1 数值勘误 > N2 表格标注澄清 > W1 C1 命名 > W2 14B 多 seed > W3 framing 调整

---

## Detailed Comments

### Abstract
- 结构合理，四个必答问题覆盖。"renders compensation redundant" 需加 "in prediction quality" 限定。"capacity phase transition" 改为 "capacity cliff"。68% divergence 来自 50% 稀疏度但未标注。

### Introduction (§1)
- 从 BCE/global-allocation mismatch 切入清晰。但 ¶2-¶3 数字密度过高，部分数据应移至 §4。Contribution 第 3 条（non-monotonic allocation + 14B effects）在前文无铺垫。"68% divergence" 在 ¶2 和 Contribution list 重复，建议 Contribution list 用 "the discovered mask patterns (§4.3)" 指代。

### Related Work (§2)
- 覆盖全面，MaskLLM 三点区分详细。MoE routing 段与主线关系稍远但可接受。D2DMoE/ShadowLLM 的 "intermediate coupling" 未量化与 "coupled" 的差距（缺 MSE baseline 的根源）。

### Method (§3)
- §3.1-§3.4 清晰规范。§3.5 自适应惩罚控制器篇幅过大（本质为标准技术）。§3.6 梯度分析正确标注 "suggestive" 但 "reveals structural asymmetry" 用词暗示超过 suggestive 的结论。

### Experiments (§4)
- 最强部分。Table 4 ablation、regime analysis (§4.6) 扎实。Table 2 数据矛盾（N2）和 C1 数值错误（N1）是必须修复的硬伤。WINA 幽灵 baseline 需移除或补数据。

### Conclusion (§5)
- 两句话严重不足。需扩展至 4-6 句，含 future work（N:M sparsity, 70B scaling, multi-target predictor）。

### Limitations
- 全面诚实，是论文优点。"best-quality" → "least-degraded"。

### Appendix
- 内容丰富，所有附录在正文有引用。Appendix C（λ 收敛）的 defense 合理但应在主文摘要。
