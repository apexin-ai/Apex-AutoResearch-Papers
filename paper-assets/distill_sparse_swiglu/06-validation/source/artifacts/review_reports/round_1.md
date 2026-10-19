---
round: 1
overall_score: borderline
timestamp: 2026-05-16T19:05:48.747089+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 1

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 Main Conference (Efficient Methods for NLP)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+格式合规）
**审稿轮次**: Round 1（独立审稿 + 交叉分享，1 轮收敛）

---

## Summary

本文提出用 KL divergence（配合 Gumbel-Sigmoid relaxation 和 Lagrangian sparsity constraint）训练 SwiGLU LLM 的轻量级 contextual sparsity predictor，替代传统 BCE 训练目标。在 LLaMA-3.1-8B 上 50% sparsity 下达到 PPL 11.79（vs TEAL 23.31, BCE 27.97），无需 compensation network。论文还提出 2D taxonomy 和三 sparsity regime 分析。

---

## Strengths

1. **问题定义清晰且重要** — "BCE per-neuron decomposition vs global top-k allocation 的 mismatch" 观察敏锐，research question well-motivated [R1, R2 一致]
2. **核心实验结果显著** — PPL 11.79 vs 23.31 (TEAL) / 27.97 (BCE) 的差距大且一致，KL advantage 随 sparsity 增长（18%→49%→82%）[R1, R2 一致]
3. **SPON orthogonality 分析有洞察** — cosine similarity 0.196 + L2 norm ratio 定量证明 static correction 与 contextual prediction 的互补性 [R1, R2 一致]
4. **论文整体写作质量好** — 结构清晰，gradient analysis 展示明白，三个 regime 分析有实用价值 [R1, R2 一致]
5. **Reproducibility 良好** — 训练细节充分（1000 steps, AdamW, lr=1e-3, A6000 17min），实用性强 [R1 4/5, R2 4/5]
6. **Honest limitations** — 坦诚承认无 wall-clock speedup、单一规模、PPL 作为 proxy 的局限 [R1]

---

## Weaknesses

### Critical（Must-Fix，影响接收决定）

**C1. Limitations section 格式不合规 [desk-reject risk]**
- 当前为 `\paragraph{Limitations.}` 嵌在 Conclusion 内
- ARR 要求独立 `\section*{Limitations}`（conclusion 之后、references 之前、不计页数）
- [R2 提出, R1 AGREE] — 这是 ARR desk-reject 条件

**C2. 页数超限 [desk-reject risk]**
- Conclusion + Limitations + Future work 延伸至第 9 页，long paper 正文限 ≤8 页
- 拆出 Limitations 后需重新编译确认
- [R2 提出, R1 AGREE]

**C3. 训练/评估数据同源，缺 OOD 验证**
- WikiText-103（训练）→ WikiText-2（评估）共享 Wikipedia domain
- 1000 steps (~8M tokens) 极少训练量下存在 domain overfitting 风险
- PPL improvement 幅度（49% relative）可能因 domain overlap 被高估
- 下游 benchmark（ARC-c, WinoGrande, MMLU, GSM8K）提供部分 OOD 验证，但 PPL 是 primary metric
- [R1 提出 critical, R2 AGREE with nuance]

**C4. "Structural failure" 声明证据不足**
- 仅测试一个 vanilla BCE configuration，未做 LR search / architecture size sweep
- KL 有 Gumbel + Lagrangian + temperature annealing 三个 trick，BCE 无对等优化
- "Loss saturation" 可能是 optimization issue 而非 structural limitation
- 需要至少 soft-target BCE 或 BCE + ranking loss 对比才能支撑 "structural" 断言
- [R1 提出 critical, R2 在 W3/W4 独立提出相同观点, 交叉 AGREE]

### Warning（Should-Fix，影响评分）

**W1. 消融实验缺关键维度**
- 缺 d_b sensitivity（仅用 128，无 64/256/512 对比）
- 缺温度退火 schedule 对比（cosine vs linear vs fixed）
- 缺 training steps learning curve
- 缺 Lagrangian LR η_λ 报告
- [R1 列为 critical, R2 PARTIALLY AGREE — 现有消融覆盖 relaxation/allocation 但缺几个维度, 协商降为 warning]

**W2. 无 wall-clock 加速，framing 误导**
- Appendix A: pipeline 增加 6.4% latency（126.78 vs 119.11 ms）
- Abstract/Intro 暗示 "acceleration" 但实际无法实现
- 应 frame 为 prediction quality 研究
- [R1-W1 = R2-W7, 两人独立一致]

**W3. Cross-architecture 验证不足**
- 仅 Mistral-7B-v0.3 一个额外模型，仅 50% 一个 sparsity point
- LLaMA-8B 和 Mistral-7B 极为相似（同规模、同 FFN 类型）
- "Transferability" claim 过强
- [R1-W2 = R2-W5, 两人独立一致]

**W4. 遗漏重要相关工作 MaskLLM**
- MaskLLM (Fang et al., NeurIPS 2024 Spotlight) 使用 Gumbel-Softmax 学 N:M sparsity mask for LLMs
- 技术组件高度相关（Gumbel relaxation + learnable mask + frozen weights）
- 必须在 Related Work 讨论并区分
- [R2 提出, R1 强烈 AGREE]

**W5. 梯度分析 overselling**
- §3.5 数学正确但非深刻理论贡献
- "Proxy loss vs end-to-end loss 的差异" 是 ML 基本认知
- 论文称 "formal gradient analysis" 但实为 informal argument
- 缺 gradient SNR / variance 的实证对比
- [R1-W4 ≈ R2-W3, 两人独立一致]

**W6. Lagrangian 缺收敛分析**
- 未报告 η_λ 具体值、λ 训练曲线、实际 sparsity ratio 是否达标
- 在 non-convex + Gumbel noise setting 下无理论收敛保证
- Reproducibility concern
- [R1-W5, R2 交叉 AGREE]

**W7. 三个 regime 仅单模型验证**
- Budget-surplus / budget-constrained / capacity-limited 边界仅 LLaMA-3.1-8B 确定
- 未验证 regime 边界是否随 model scale 变化
- [R2-W5, R1 交叉 AGREE]

### Info（Minor Issues）

- 2D taxonomy 作为 contribution 列出但实为 post-hoc classification [R2-W6, R1 部分 REBUT — 有 organizational value]
- 3-seed (n=3) 统计效力弱 [R1-W3, R2 REBUT — ML 惯例可接受]
- "2.71×" 应为 2.70× (2700/1000=2.7)
- "~2.7% latency saving" 数值不精确（实际 ~2.3%）
- Table 1 multi-seed (uniform, 11.92) vs main result (global, 11.79) 容易混淆
- Mistral PPL 8.98 = LLaMA 30% PPL 8.98 巧合未注明
- SPON bib year=2026 ICML vs OpenAlex=2025，需核实
- FastForward 67.2M/2.7% 数字来源未标注
- 两个 evaluation protocol 差异未充分解释
- 缺 Ethics Statement（ARR 推荐但不强制）
- 缺 MoE routing 概念关联讨论
- 缺 LLM-specific KD 更新文献 (MiniLLM, GKD)

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上独立达成一致：
1. BCE baseline 不公平 → "structural failure" claim 过强 (C4)
2. 无 wall-clock 加速与 framing 矛盾 (W2)
3. WikiText data overlap 风险 (C3)
4. Cross-architecture 验证不足 (W3)
5. MaskLLM 引用遗漏 (W4)
6. Lagrangian 缺细节 (W6)
7. 格式不合规 (C1, C2)

---

## Reviewer Divergence [REBUT]

**Novelty vs SPON (R2-N3 vs R1-REBUT)**

- R2 认为：本文与 SPON 的差异仅为 per-token vs static，属于 "自然延伸"，novelty 不足以支撑 main conference
- R1 反驳：(1) Static bias vs dynamic contextual mask 是 fundamental 差异（加法偏置 vs 乘法 gating）；(2) SPON orthogonality data（cosine 0.196, L2 ratio 15.8%）证明 SPON 未捕获 predictor 的信号；(3) 技术框架完全不同（SPON 无需 Gumbel/Lagrangian/end-to-end differentiable mask）
- **Director 判断**：R1 的论据更强——SPON 和本文解决的是不同子问题（static correction vs contextual prediction），技术栈无交集。但 R2 的 concern 仍部分成立：论文 framing 可以更清晰地 articulate 与 SPON 的差异。记录为 warning 而非 critical。

---

## Questions to Authors

1. BCE 实验中使用的 learning rate 和 schedule？是否做过 LR search？
2. d_b=128 是如何选择的？preliminary 实验数据？
3. 能否提供 C4 或 Pile test set 上的 PPL？
4. Lagrangian multiplier λ 的训练轨迹？实际 sparsity ratio 是否达标？
5. 给 BCE 同样的 Gumbel-Sigmoid + Lagrangian 框架（仅换 loss），性能如何？——这能更 cleanly 隔离 loss function 的贡献
6. MaskLLM 与本文的关系和区别？

---

## Missing References

1. **MaskLLM** (Fang et al., NeurIPS 2024 Spotlight) — Learnable Semi-Structured Sparsity, Gumbel-Softmax for N:M mask learning [必须引用]
2. **MoE routing** (Switch Transformer, GShard) — 概念关联讨论 [建议引用]
3. **LLM-specific KD** (MiniLLM, GKD) — 方法论 overlap [建议引用]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。

---

## Overall Assessment

**Score: 3.0 / 5 — Borderline (Findings track recommended)**
**Confidence: 4/5**

两位 Reviewer 独立给出相同评分（R1: 3/5, R2: 3.0/5），均推荐 Findings track。

**核心判断**：论文有清晰的 research question 和显著的 empirical result（KL >> BCE >> magnitude-only），但存在以下系统性不足：
1. **格式风险**：Limitations 不合规 + 页数超限 = desk-reject 可能
2. **实验严谨性**：OOD 验证缺失、BCE baseline 不公平、关键消融缺失
3. **Claim 校准**："structural failure" 和 "acceleration" 的 claim 超出了证据支撑范围
4. **规模局限**：仅 7-8B 模型，cross-architecture/cross-scale 验证不足

如果作者能解决 C1-C2（格式）、C3（OOD eval）、C4（BCE fairness），并弱化 overclaiming，论文质量可提升至 weak accept 水平。当前状态更适合 Findings track。

---

## Detailed Comments (按 section)

### Abstract & Introduction
- "can accelerate SwiGLU-based LLMs" 与实际 6.4% overhead 矛盾，需 reframe
- "formal gradient analysis" 应降为 "gradient-based motivation"
- 三条 contribution 中 taxonomy 可降为 organizational framework

### Method (§3)
- 梯度分析数学正确但非 novel theoretical contribution
- Lagrangian §3.4 缺 η_λ 值和收敛讨论
- Gumbel-Sigmoid 的选择 well-motivated (vs STE ablation)

### Experiments (§4)
- Core result (Table 2) 强且 consistent
- Iso-compute analysis (§4.2) 需更 controlled 对比（BCE + same framework tricks）
- SPON analysis (§4.4) 有 insight
- Cross-architecture (§4.6) 仅 1 model, 1 sparsity point — 不足以支撑 claim
- Latency (Appendix A) 诚实但与 framing 矛盾

### Related Work (§2)
- MaskLLM 遗漏是 major gap
- MoE connection 值得一提
- 现有引用准确（经 OpenAlex 验证，21 条均为真实论文）

### Format
- Limitations: 必须拆为独立 section*
- 页数: 需编译确认（可能 border-line）
- 匿名性: 通过 ✓
- 模板: ACL review style ✓
