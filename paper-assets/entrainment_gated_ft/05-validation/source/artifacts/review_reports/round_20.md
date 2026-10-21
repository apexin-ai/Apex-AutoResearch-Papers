---
round: 20
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T14:32:28.543297+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures

**Round 20 | Target Venue: EMNLP 2026 (ARR) | 审稿模式: Fresh**

---

## Summary

本文研究三种混合线性循环架构（GatedDeltaNet、RetNet、HGRN2）在逐样本层面的预测多样性（predictive multiplicity）。利用受控 model zoo（3 架构 × 5 attention 比例 × 2 规模），作者发现：(1) 聚合指标相近的架构在逐样本层面存在结构化分歧（Jaccard ≈ 0.10）；(2) 该分歧模式在 4% attention 即饱和；(3) multiplicity 幅度因任务类型（或评估格式）而异。此外，confidence-based routing 仅在 LAMBADA 上有效（+5.2pp），在其他 benchmark 上无效或有害。

---

## Strengths

**S1. 实验设计高度受控（共识）**：使用共享训练数据、tokenizer 和超参数的 model zoo，将架构作为唯一变量。内部效度强，优于 D'Amour et al. (2022) 的多变量设计。

**S2. 统计方法论严谨且透明（共识）**：全文一致使用 Bonferroni 校正、精确置换检验、Bootstrap BCa 置信区间。坦率承认 n=5 时 Spearman 的功效限制（"only |ρ| = 1.0 achieves p < .05"），在 NLP 实证论文中罕见。

**S3. Jaccard 饱和发现（共识：论文最强贡献）**：4% attention 即确立完整的逐样本分歧模式，暗示 attention 的"架构指纹"效应是二元的而非剂量依赖的。跨规模一致（340M/1.3B），Figure 1b 和 Figure 4 提供清晰视觉证据。

**S4. 附录详尽（共识）**：13 页 Appendix A–Y，包括连续 Jaccard 验证、归一化效应量、种子校准、五架构验证、Transformer 基线对比等。几乎每个潜在质疑都有 robustness check。

**S5. Yang & Wang (2026) 引用处理得当**：在 abstract 和 Related Work 中明确引用并区分贡献（"our within-family design isolates backbone variation from training-regime differences"）。

**S6. 五架构验证增强泛化性**：GLA + DeltaNet 加入后 10 个架构对全部满足 J ≤ 0.14, p ≤ .002。

---

## Weaknesses

### Critical / Major

**W1 [Major, 共识] 单次训练运行无法分离架构效应与种子效应**

每个架构×attention 配置仅一次训练运行。Pythia 70M 种子校准（Appendix W）是跨家族/跨规模的（Transformer 70M vs 混合循环 340M/1.3B），说服力有限。within- vs. cross-architecture 3× Jaccard 差距是 suggestive 但非 definitive——cross-architecture 必然包含种子差异 + 架构差异。这是整个论文最根本的方法论局限。

- R1 评估：Major | R2 评估：Major | 交叉：双方 [AGREE]

**W2 [Major→Critical, 分歧] GDN 16-head confound 对聚合收敛声明的影响**

GDN h3-1 使用 16 heads（vs. 其他配置 32 heads），构成混淆变量。排除 GDN 后：LAMBADA ρ 从 −1.0 降至 −0.7 (p=.233)；MMLU 从负相关反转为 +0.6。

- R1 评估：Critical（认为动摇论文约 1/3 叙事）
- R2 评估：Major（论证：聚合收敛非核心 claim；论文策略恰恰利用其非显著性来对比 per-example 显著性；per-example 饱和不受 GDN 影响）
- **Director 判断**：R2 论证有力——论文的两项正式贡献（结构化 multiplicity + Jaccard 饱和）均不依赖聚合收敛。但 §4.3 的 convergence 讨论和 Table 1 的呈现方式仍给读者错误印象。建议 Table 1 增加 "excl. GDN" 行，§4.3 更显著地讨论此 confound。**定为 Major。**

**W3 [Major, 共识] 任务类型与评估格式完全混淆**

LAMBADA 同时是唯一的自由生成 benchmark、唯一的 retrieval 任务、和拥有最高 α (0.30) 的任务——三重混淆使任何单一归因不可证伪。论文全文以 "(or evaluation format)" hedging，诚实但意味着核心 claim 的因果解释力受限。多选题内部 format 不预测 α 仅排除子空间内效应，不解决 free-form vs. MC 的根本差异。

- R1 评估：Major | R2 评估：Major | 交叉：双方 [AGREE]

**W4 [Major, 共识] Routing 贡献薄弱但叙事权重过高**

Confidence-based routing 在 4 个 benchmark 中仅 LAMBADA 有效（+5.2pp），HellaSwag 无效（-0.06pp），PIQA 显著有害（-0.49pp, p = .006）。这实质上是一个消极结果。然而：
- Abstract 用约 1/6 篇幅描述 routing，正面数字（"+5.2pp"、"36% of oracle complementarity"）比消极描述更突出
- Conclusion 将 routing 作为两大核心观察之一
- 缺少最自然的 baseline（logits ensemble，论文承认 "left to future work"）

Introduction 贡献列表未包含 routing（正确），但与 abstract/conclusion 不一致。

- R1 评估：Major | R2 评估：Major | 交叉：双方 [AGREE]

**W5 [Major, R2 提出, R1 部分同意] 概念新颖性有限**

核心贡献是将 predictive multiplicity（Marx 2020）和 underspecification（D'Amour 2022）的分析框架应用到混合线性循环架构。"聚合指标掩盖逐样本分歧"的概念已被充分建立。独特贡献集中在饱和发现，但仅占论文约 1/4 篇幅。

- R1 交叉回应：[PARTIAL]——经验贡献被低估（饱和的阈值效应、受控设计方法论、混合架构时效性），建议重组让饱和为主线
- **Director 判断**：在 Findings 标准下可接受。但如果重组让饱和发现成为主线叙事，论文贡献感知会更清晰。

### Minor / Info

**W6 [Minor, R2 提出] 缺少 selective prediction / ensemble selection 文献**

Routing 实验本质上是基于输入特征选择最优模型，与 Geifman & El-Yaniv (2017, 2019) 和 Caruana et al. (2004) "Ensemble selection from libraries of models" 概念相关。

**W7 [Minor, R2 提出, R1 方向同意] Limitations 遗漏 greedy decoding 影响**

所有评估使用 greedy decoding，Limitations 未讨论采样 decoding 对逐样本分歧的潜在影响。R1 交叉同意方向但降低 severity——greedy 是 lm-eval-harness 标准配置。

**W8 [Minor, R1 提出] n=3 Bootstrap CI 退化**

n=3 架构上 Bootstrap BCa 大量样本为退化的同架构三重采样（Appendix D1），影响 Figure 4 CI 不含零的可信度。论文 Section 3.5 已标注 "heuristic"。

**W9 [Minor, R1 提出] 排列检验未条件化于样本难度**

Appendix K 的 null baseline 未排除样本内在难度对跨架构 Jaccard 重叠的混淆。

**W10 [Info, 共识新增] 饱和发现的替代解读未讨论**

Appendix I 显示三个架构 h3-1 correct set 都更接近 Transformer 基线。饱和可能反映的是"少量 attention 即引入 Transformer 式行为"，而非"架构指纹在最低 attention 即确立"。两种解读有根本区别，论文应在 §4.2 或 Discussion 中讨论。

---

## Questions

1. 为什么不对一个架构训练多个种子来直接校准种子噪声水平？这是最直接回答"逐样本分歧是架构驱动还是种子驱动"的实验。（R1+R2 共识）

2. 排除 GDN 后各 benchmark 的完整 Spearman 表——尤其 MMLU ρ 反转为 +0.6 是否意味着 MMLU convergence 完全由 GDN anomaly 驱动？（R1+R2 共识）

3. Appendix I 的 Transformer 基线——h3-1 correct set 更接近 Transformer 是否暗示 attention 主导了逐样本行为？如果是，饱和发现的理论含义需要修正。（R2 提出, R1 强 AGREE）

4. 论文仅评估预训练 checkpoint。Fine-tuning（尤其 instruction tuning）后逐样本分歧是否保留？这对部署建议的适用性至关重要。（R2 提出, R1 AGREE）

5. AUC 0.70–0.74 的未解释 30% 方差——是否考虑过结合多个浅层信号（token 频率、输入长度、prompt perplexity）构建组合预测器？（R2 提出）

---

## Missing References

- Geifman & El-Yaniv (2017, 2019) — Selective prediction / abstention（routing 实验的概念前驱）
- Caruana et al. (2004) "Ensemble selection from libraries of models"（基于输入选择最优模型的经典工作）
- 论文的 Related Work 在其他方面较全面：Yang & Wang (2026)、MultiBERTs、Model Soups、predictive multiplicity 文献均已引用。

---

## External Review

**状态**：未请求。

---

## Visual Layout Check（非评分项）

**状态**：已完成（2026-05-24 14:13–14:16 UTC）

| 严重程度 | 位置 | 发现 |
|---------|------|------|
| ⚠️ Warning | Page 8 | 三个 figure（5/6/7）挤在同一页上半部，Figures 6 和 7 尺寸偏小（各约占 1/6 页面），内部文字可能低于正文字号 70% 可读性阈值。该页同时含 Conclusion + Limitations 开头，整体拥挤。建议将 Figure 7 移至 page 7 或 Appendix。 |
| ✓ Info | Page 2 | Figure 1 在第 2 页顶部有效建立核心发现锚定。良好。 |
| ✓ Info | Page 5 | Figure 3 bar chart 颜色区分度良好，caption 自包含。 |
| ✓ Info | Page 6 | Tables 1-2 booktabs 风格，关键值加粗，精度统一。 |
| ✓ Info | Page 7 | Figure 4 scatter plot 清晰，bootstrap CI 标注文字偏小。 |
| ✓ Info | Pages 9-10 | References 格式统一，无未解析引用。 |
| ✓ Info | Pages 11-21 | Appendix ~28 个 table 格式一致。 |
| ✓ Info | Page 21 | "Use of AI Assistants" 透明声明。 |

**总结**：1 个 warning（page 8 拥挤），0 个 critical。整体排版质量良好。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 合成 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 2.5/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分理由**：

- **R1: 3.0 (Findings)** — 饱和发现和实验框架支撑 Findings，但 GDN confound 削弱 convergence 声明，加上单次运行和格式混淆，Conference 级别的统计基础不足。
- **R2: 3.5 (Borderline Conference)** — 执行严谨，饱和发现有价值，但概念增量有限，routing 为消极结果，关键混淆未解决。

**Director 合成判断（3.0 Findings）**：

R2 在交叉中对 R1-W5（p=.170）的反驳有说服力——论文对 p=.170 的处理是坦诚的统计报告而非暗示显著。R2 对 GDN confound 的降级论证（聚合收敛非核心 claim）也有技术 merit。但综合考虑：

1. **概念新颖性有限**（R1 partial agree + R2 Major）：核心信息已被充分建立
2. **单次运行**（双方 Major）：最根本的方法论局限，使所有架构效应声明均为 suggestive
3. **格式混淆**（双方 Major）：LAMBADA 的三重混淆使任务类型 claim 不可证伪
4. **Routing 为消极结果**（双方 Major）：但获得过高叙事权重
5. **饱和发现是真实贡献**（双方共识）：但仅占论文约 1/4 篇幅

这些问题的叠加效应将论文定位在 Findings 而非 Conference。饱和发现的非平凡性和整体执行质量足以支撑 Findings 接收，但论文缺乏足够的新颖性证据（如多种子实验、生成任务 routing 验证）来达到 Conference 级别。

**关键分歧记录**：
- GDN severity：R1 Critical vs R2 Major（Director 采纳 Major）
- p=.170 解读：R1 Major vs R2 Rebut（Director 采纳 R2 rebut——不应列为 weakness）
- n=5 power：R1 Major vs R2 Minor（Director 判断：论文已有等价说明，降为 Info）

---

## Detailed Comments

### 优先修改建议（按影响力排序）

1. **叙事重构**：将饱和发现升级为主线贡献（两位 Reviewer 在交叉后趋于一致），弱化/条件化聚合 convergence 叙事
2. **Routing 降级**：Abstract 缩减 routing 篇幅或明确标注为"探索性消极发现"，Conclusion 中减少比重
3. **GDN confound 显著化**：Table 1 增加 "excl. GDN" 行，正文更早 flag 16-head anomaly
4. **替代解读讨论**：§4.2 讨论饱和可能反映 Transformer 式行为引入
5. **文献补充**：Geifman & El-Yaniv (2017/2019) + Caruana et al. (2004)
6. **Limitations 补充**：greedy decoding 影响一句话

### 不建议修改

- p=.170 的报告方式（当前处理是坦诚且正确的）
- Binary decomposition（连续 Jaccard 已验证，R1 在交叉中肯定设计合理）
- 五架构验证仅 340M（model zoo 约束，非设计缺陷）

---

**报告生成时间**: 2026-05-24
**Reviewer Panel**: R1 (方法严谨性 + 统计基础) + R2 (新颖性 + 叙事完整性)
**交叉分享**: 完成（R1→R2, R2→R1，均提交逐条回应）
**轮次**: 1 轮（关键问题达成共识或记录明确分歧，无需追加轮次）