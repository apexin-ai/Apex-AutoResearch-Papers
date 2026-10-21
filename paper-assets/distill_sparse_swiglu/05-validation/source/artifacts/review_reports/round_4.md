---
round: 4
overall_score: weak reject
timestamp: 2026-05-17T08:26:58.376537+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**目标 Venue**: EMNLP 2026 (via ARR May cycle)
**截止日期**: 2026-05-25
**Reviewer 编排**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性）
**审稿模式**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）

---

## Summary

本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 activation sparsity predictor，核心论点是 BCE 梯度按 neuron 分解而推理时 TEAL 使用 global top-k allocation，存在"结构性不匹配"；KL 通过 Gumbel-Sigmoid relaxation 耦合所有 neuron 的梯度。在 LLaMA-3.1-8B 上 50% sparsity PPL 11.79 vs TEAL 23.31（无 compensation network）。跨架构验证于 Mistral-7B-v0.3。提出 2D taxonomy 和三 sparsity regime 分析。

---

## Strengths

**S1. 梯度分析形式化清晰（§3.5）。** Factor (a)-(d) 分解严格说明 KL 和 BCE 的结构性差异：factor (b) 的 downstream Jacobian 使 KL 梯度依赖所有下游层 mask 状态。SNR 实验验证（early layer 34-156× 差异）提供定量支撑。[R1, R2 一致]

**S2. Oracle F1 分析（§4.2）揭示 proxy mismatch 的深度。** BCE F1=0.613 > KL F1=0.540（+13pp），但 KL PPL 优 91%。KL 的 near-random precision (0.51) 证明它学到的 mask 与 magnitude oracle 完全不同，直接 falsify "per-neuron accuracy = output quality" 的隐含假设。全文最有说服力的实验。[R1, R2 一致]

**S3. 消融覆盖全面。** Loss direction（Forward KL vs JSD vs Reverse KL）、relaxation（Gumbel vs STE, Δ=3.98）、loss isolation（BCE+Gumbel+Penalty=38.02，证明 penalty 与 BCE 不兼容）。Loss effect (ΔPPL=26.23) 是 relaxation effect (ΔPPL=3.98) 的 6.6×，清晰分离各组件。[R1, R2 一致]

**S4. 执行质量较高。** Cross-architecture 验证一致（KL-over-TEAL ratio within 7% at ≤50%）；训练成本低（~17 min on A6000）；超参数 sensitivity 分析充分（d_b, τ, steps）。[R1, R2 一致]

**S5. SPON 正交性分析（§4.5）。** Cosine similarity 0.196 + 2.4% PPL 改善定量说明 KL predictor 已捕获大部分可恢复信号。[R1]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[W-C1] Responsible NLP Research Checklist 缺失 — desk rejection 风险** [R2 raise, R1 AGREE]
- ARR 自 2024-12 起强制要求。论文无 checklist 也无 Ethics Statement。缺失可直接 desk reject。
- **Action**: 参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写。

**[W-C2] Downstream collapse 与 PPL-centric 叙事系统性矛盾** [R1, R2 独立 raise, 交叉强 AGREE]
- 30% KL global MMLU = 25.27%，比 TEAL vanilla (38.61%) **低 13.3pp**——KL 训练在 MMLU 上造成 active harm。
- 50% MMLU ≈ 28%（≈ random），GSM8K < 2.2%，KL (1.29%) 比 TEAL (1.97%) 更差。
- PPL 大幅改善（49% at 50%）完全未转化为 reasoning 保持。
- Abstract/Introduction 以 PPL 为核心 framing，Limitations 才承认 "PPL is poor proxy for reasoning"——自相矛盾。
- **Action**: (1) Abstract/Intro 诚实呈现 downstream mixed results；(2) 讨论 KL 训练为何恶化 MMLU（global top-k late-layer starvation vs loss function 本身的影响需分离）；(3) 补充 10-20% sparsity downstream 评估找 practical sweet spot。

**[W-C3] 无 wall-clock speedup，efficiency framing 误导** [R1, R2 独立 raise, 交叉强 AGREE]
- Table 6: KL predictor 50% sparsity = 126.78ms vs dense 119.11ms = **+6.4% overhead**。
- 消除 compensation 节省 2.7%，但 predictor 本身加 6.4%。净效果：比 dense 慢，仅比 compensation-based 方案快 2.5pp。
- Unstructured masks 不产生 sparse computation speedup（论文自己在 Appendix A 和 Limitations 中承认）。
- Introduction "simplify inference by pruning 50% of FFN neurons" 暗示效率增益，与实际矛盾。
- **Action**: 重新定位为 prediction quality + architectural simplification；Abstract/Intro 明确声明无 wall-clock speedup。

**[W-C4] 训练-推理 mask mismatch 未分析** [R1 raise, R2 AGREE with nuance]
- Table 5 (Appendix B): d_b=128 per-token PPL=9.218 vs TEAL global PPL=11.963——~30% gap。
- Dense (6.12) → KL-TEAL (11.79) 的全部退化（Δ=5.67）中，相当部分可能来自 allocation strategy 信息丢失，而非 sparsity capacity loss。
- 论文从未分解这一 gap 的来源。R2 澄清 gap 主要来自 allocation strategy（per-token eval 也用 hard mask），非 soft→hard discretization。
- **Action**: 三向分解分析（per-token hard / per-token soft / global hard with oracle scores），分离 mask quality loss、discretization loss、allocation loss。

### Should-Fix（影响评分但不一票否决）

**[W-S1] 与 MaskLLM 技术重叠讨论不足** [R2 raise critical, R1 REBUT → 降为 warning]
- MaskLLM (NeurIPS 2024) 同样用 frozen weights + learnable masks + Gumbel relaxation + KL divergence。
- R1 论证两者存在关键结构差异：MaskLLM 是 static N:M weight masks（per-group categorical, Gumbel-Softmax），本文是 per-token contextual activation masks（binary per-neuron, Gumbel-Sigmoid, global budget constraint）。MaskLLM 的设定中不存在 structural mismatch 问题。
- **共识**：论文讨论确实不足，应添加专门 MaskLLM 技术对比段落。但"核心技术重叠"判断不成立——本文核心贡献是 structural mismatch 识别和梯度分析（§3.5），这在 MaskLLM 的设定中不适用。
- **Action**: Related Work 添加 MaskLLM 深度对比。

**[W-S2] BCE 对比公平性** [R1 raise, R2 AGREE]
- KL 系统 = Forward KL + Gumbel + penalty；BCE 系统 = BCE + hard mask + compensation。不仅是 loss function 差异，是整个 pipeline 差异。
- BCE+Gumbel+Penalty = 38.02（比 vanilla BCE 27.97 更差）说明 penalty 与 BCE 不兼容，KL 优势与 Gumbel+penalty infrastructure 不可分离。
- **Action**: 明确说明优势来自 loss + infrastructure 组合。

**[W-S3] 三 seed 统计效力不足** [R1, R2 AGREE]
- 3 seeds 95% CI 较宽，JSD vs Reverse KL 差异 0.26 无 CI。Multi-seed 仅在 50% uniform 下做，主结果（50% global TEAL）无方差估计。
- **Action**: 50% global TEAL 补 multi-seed。

**[W-S4] 实验规模受限（仅 7-8B）** [R1, R2 AGREE]
- 两模型 d_ff/d_model ratio 相同，Mistral 差异（GQA + sliding window）与 FFN sparsity 关系不大。
- **Action**: 弱化 generalization claims。

**[W-S5] 三 regime 分析证据不足** [R1, R2 AGREE]
- 2 models × 3 levels = 6 数据点。Regime 边界泛化性未验证。
- **Action**: 降为 empirical observation on 7-8B models。

**[W-S6] "Parameter-free" penalty controller 表述不准确** [R1 raise, R2 AGREE]
- λ_max 在不同 target 取不同值（1000 vs 5000），是 hyperparameter。30% 时达 cap 且偏差 5%。
- **Action**: 去掉 "parameter-free" 措辞。

**[W-S7] D2DMoE (NeurIPS 2024) 遗漏** [R2 raise, R1 AGREE]
- 应填入 taxonomy Per-token × Intermediate cell。影响 taxonomy 完整性和 "no prior work" claim。
- **Action**: 引用并更新 Table 1。

**[W-S8] Abstract 数据堆砌** [R2 raise, R1 AGREE]
- 25+ 个数字，审稿人 30s 无法消化。
- **Action**: 精简到 3-4 个核心数字，以叙事为主。

**[W-S9] Taxonomy post-hoc 质疑** [R2 raise, R1 部分 AGREE]
- 5/9 cells 空。DejaVu 在 taxonomy 中提到但 Table 2 实验中缺失。
- **Action**: 补充 DejaVu/D2DMoE，讨论轴选择依据。

### Minor Issues（不影响接收）

| ID | 问题 | 来源 |
|----|------|------|
| M1 | AdamW weight decay 未报告 | R1 |
| M2 | BCE oracle mask threshold 作用域不清楚 | R1 |
| M3 | ShadowLLM 在 Table 1 分类可能不准确（per-layer vs per-token） | R1 |
| M4 | loshchilov2019adamw 年份不一致（2019 vs 2017） | R1 |
| M5 | Latency 测量 GPU 与训练 GPU 不同 | R1 |
| M6 | Abstract -ing 分词短语 AI 写作痕迹 | R2, R1 AGREE |
| M7 | xu2026spon bib year 不一致 | R2, R1 AGREE |
| M8 | Figure 1 label fig:taxonomy 与内容不匹配 | R2, R1 AGREE |
| M9 | Conclusion 仅 3 行过短，无 future work | R2, R1 AGREE |
| M10 | 训练数据小且同源（C4 OOD 已部分缓解） | R1, R2 降级 |
| M11 | SNR 在 C4 上测量（R2 认为反而跨分布验证） | R1, R2 降级 |

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：
1. **Downstream collapse 与 PPL framing 矛盾是最严重的问题**——30% KL global MMLU 比 TEAL 更差 13.3pp
2. **无 wall-clock speedup**——efficiency framing 需重新定位
3. **Responsible NLP Checklist 缺失**——desk reject 风险
4. **Train-test mask mismatch 需分析**——per-token vs TEAL global 的 ~30% gap 未分解
5. **实验规模有限**——仅 7-8B，regime 分析证据不足
6. **Abstract 数据堆砌**——需精简
7. **梯度分析和 Oracle F1 分析是最强贡献**——两位均高度评价 §3.5 和 §4.2

## Reviewer Divergence

**MaskLLM 技术重叠（R2-N3 vs R1 REBUT）**：
- R2 认为核心 pipeline（KL + Gumbel + frozen weights）与 MaskLLM 相同，属 critical 新颖性问题
- R1 认为 MaskLLM（static N:M weight masks）和本文（per-token contextual activation masks）的优化问题本质不同，structural mismatch 在 MaskLLM 设定中不存在
- **Director 判断**：R1 的 REBUT 论证充分——MaskLLM 的 per-group categorical selection 与本文的 global budget-constrained binary prediction 是不同优化问题。降为 warning（讨论不足）而非 critical（新颖性不足）。

---

## Questions to Authors

1. Table 5 per-token PPL=9.218 vs TEAL global PPL=11.963 的 ~30% gap 如何分解？能否提供 per-token hard mask evaluation 分离 allocation loss？
2. 30% sparsity 下 KL global MMLU (25.27%) 比 TEAL (38.61%) 低 13.3pp。KL 训练为何在 MMLU 上造成 active harm？是 global allocation 的 late-layer starvation 还是 KL loss 本身过度偏向 PPL-dominant layers？
3. BCE 的 learning rate、optimizer、weight decay 是否与 KL 完全一致？
4. KL predictor 学到的 mask 与 magnitude oracle 几乎无相关（precision 0.51）——per-layer 分析能否揭示 KL mask 的具体模式？
5. 是否尝试过 hard top-k with STE 替代 Gumbel-Sigmoid 来缩小 train-test gap？

---

## Missing References

1. **D2DMoE** (NeurIPS 2024) — Dense-to-Dynamic-k MoE，per-token router 用 ℓ2-norm regression，应填入 taxonomy Per-token × Intermediate cell
2. **WAS** (EMNLP 2025) — Weight-Aware Activation Sparsity（待确认完整引用信息）

---

## Overall Assessment

**Overall Score: weak reject (3.0/5, Findings 边界)**
**置信度: 4/5**

两位 Reviewer 独立给出一致评分（R1: 3/5, R2: 3/5）。

**核心判断**：论文在理论洞察（gradient coupling analysis, §3.5）和实验执行（systematic ablation, cross-arch verification）方面质量较高。Oracle F1 分析优雅地证明了"正确目标 > 高精度代理"这一核心论点。

但三个结构性问题严重限制了论文的影响力：
1. **PPL-downstream disconnect**: 最引人注目的改善点（50% sparsity, 49% PPL reduction）在 downstream tasks 上完全不相关（MMLU ≈ random），且 30% 时 KL 训练反而 active harm MMLU（-13.3pp vs TEAL）。论文的核心叙事建立在一个与实际应用脱节的指标上。
2. **无实际加速**: 作为一篇以 sparsity prediction 为核心的论文，全部实验仅展示 prediction quality 而无任何 wall-clock speedup，且 framing 存在误导。
3. **分析不完整**: per-token vs TEAL global 的 ~30% PPL gap 未分解，读者无法判断方法的 ceiling 和改进空间。

如果作者能 (a) 诚实重新定位叙事（prediction understanding 而非 efficiency），(b) 补充 downstream 分析解释 PPL-MMLU disconnect，(c) 分解 train-test gap 来源，论文有潜力达到 borderline accept。当前版本适合 Findings track。

---

## Detailed Comments（逐节）

### Abstract
- 25+ 个数字，信息密度过高（W-S8）
- 多处 -ing 分词短语（M6）
- 以 PPL 为核心 framing 但 downstream 讲不同故事（W-C2）

### Introduction (§1)
- "simplify inference by pruning 50% of FFN neurons" 暗示效率增益（W-C3）
- 叙事线整体清晰，structural mismatch 论证有力
- Contribution 列表第三条（三 regime 分析）claim 过强（W-S5）

### Related Work (§5)
- MaskLLM 讨论不足（W-S1）
- D2DMoE 遗漏影响 taxonomy 完整性（W-S7）
- ShadowLLM 分类可能不准确（M3）
- 31 refs 数量基本达标

### Method (§3)
- 梯度分析（§3.5）是最强贡献（S1）
- Gumbel-Sigmoid 使用正确
- "Parameter-free" 表述需修正（W-S6）
- Penalty controller footnote 与正文 "adaptive penalty controller" 术语一致，但 λ_max 的 hyperparameter 性质未充分讨论
- BCE oracle mask 的 threshold 作用域不清楚（M2）

### Experiments (§4)
- Table 2 主结果清晰
- 30% KL global MMLU 问题需要突出讨论（W-C2）
- BCE 对比是 pipeline 差异而非仅 loss 差异（W-S2）
- Multi-seed 缺 50% global 的方差（W-S3）
- Cross-arch 验证有价值但 generalization claim 需弱化（W-S4）

### Conclusion (§6)
- 3 行过短（M9）

### Limitations
- 存在且独立，但 PPL-downstream disconnect 应更突出

### Appendix
- Table 5 (d_b sensitivity) 揭示了 per-token vs TEAL global 的关键 gap 但未分析（W-C4）
- Lagrangian dynamics figure 已补充（历史 issue 已修复）
- OOD C4 评估仅 50%，建议补充 30%/70%

### Format Compliance
- ✅ ACL template with [review] option
- ✅ Anonymous (\author{Anonymous})
- ✅ Limitations section 独立
- ❌ **Responsible NLP Research Checklist 缺失**（W-C1, desk reject 风险）
- ❌ **Ethics Statement 缺失**
- Figure 1 label 错误（M8）
