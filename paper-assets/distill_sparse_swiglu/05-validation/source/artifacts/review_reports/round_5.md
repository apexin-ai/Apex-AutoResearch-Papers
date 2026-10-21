---
round: 5
overall_score: weak reject
timestamp: 2026-05-17T09:35:45.547603+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 4

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性)
**轮次**: Round 1 独立审稿 + 交叉分享, 1 轮收敛

---

## Summary

本文研究用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor。核心论点是 BCE 的 per-neuron 梯度与 TEAL 推理时 global top-k 分配存在结构性不匹配，而 KL 目标通过计算图耦合所有神经元。一个轻量 predictor (75.9M params, &lt;1% of base) 通过 Gumbel-Sigmoid relaxation 实现端到端蒸馏，在 LLaMA-3.1-8B 50% sparsity 下 PPL 11.79 vs TEAL 23.31 (49% 改善)。论文同时提出 2D taxonomy 分类先前方法和三 sparsity regime 分析。然而，headline method (KL+global allocation) 在最重要的 downstream task 上退化至随机水平 (MMLU 25.27% ≈ 4-choice random)，实际推理增加 6.4% overhead 而非加速，且核心定量 claim ("91% worse PPL") 依赖的数据无法从论文中验证。

---

## Strengths

**S1. 问题定义清晰且有意义** [R1+R2 共识]
Per-neuron BCE 与 global top-k 之间的 structural mismatch 是一个真实问题。梯度分析框架（Eq. 7-10, 4-factor 分解）虽本质是 chain rule 展开，但将其 formalize 并与 oracle F1/SNR 联系的分析思路清晰。"F1 高反而 PPL 差" 的 empirical finding 有独立价值。

**S2. 系统的 ablation 设计** [R1+R2 共识]
Table 3 覆盖 divergence direction (forward/reverse/JSD)、relaxation (Gumbel/STE)、BCE variants (±compensation, +Gumbel)，多维度隔离了设计选择。每个 ablation 有独立 exp_id，可溯源。

**S3. 诚实报告负面结果** [R1+R2 共识]
论文未隐瞒 MMLU 退化、无 wall-clock 加速等问题，而是将其作为分析对象（regime analysis, late-layer starvation）。这种诚实态度值得肯定。

**S4. 跨架构一致性** [R2]
Table 7 在 Mistral-7B-v0.3 上验证 KL/TEAL advantage ratio 一致性（≤50% 内 7% 偏差）。

**S5. 写作质量** [R2]
全文无 AI 写作典型标志（无 em-dash、无 -ing 结尾短语），段落过渡自然，数学符号一致。

**S6. Reproducibility** [R1+R2 共识]
超参全量报告、training convergence curve、bottleneck sensitivity sweep、训练成本低 (17min on A6000)。

---

## Weaknesses

### Critical Issues (影响接收决定)

**C1. [critical] PPL 22.51 幽灵数字——核心 claim 数据溯源链断裂** [R1 raise, R2 强 AGREE]

§4.3 写到 "BCE achieves +13pp oracle F1 (0.613 vs. 0.540) with 91% worse PPL (22.51 vs. 11.79)"。"91% worse perplexity" 贯穿 Abstract、Introduction、Experiments 三处，是论文最核心的定量 claim 之一。然而 22.51 **不出现在论文任何表格中**：Table 2 BCE (2700 steps) = 27.97, BCE+Compensation = 25.44。若用 Table 2 的 27.97，则是 137% worse，而非 91%。

更严重的是，experiments.tex:65-66 中 22.51 和 27.97 在同段相邻两句出现，指向相同 exp_id (bce_isocompute_s42)，自相矛盾。这不是 typo——是数据溯源链的根本断裂。审稿人无法从提交材料中验证论文最核心的 quantitative claim。

**C2. [critical] Headline method 在 downstream tasks 上退化至随机水平，与论文叙事根本矛盾** [R1-N2 + R2-N3, 交叉全 AGREE]

论文主推方法 "KL global (Ours)" 的 downstream 表现：
- 30% sparsity: MMLU 25.27% (4-choice random = 25%, 差 0.27pp; TEAL vanilla = 38.61%, 高 13.3pp)
- 50% sparsity: MMLU 27.89%, GSM8K 1.29% (完全失效)
- 即使 "best case" 30% KL uniform = 40.61%, 仍比 dense 65.27% 低 24.7pp

论文的 primary inference protocol "KL + TEAL global"（experiments.tex:18-19 定义为 "predictor-TEAL"）在所有设定下 MMLU 不可用。论文全篇以 "optimizes for global allocation quality" 为核心叙事（Abstract, §1, §3.5），但实验结论表明 global allocation 在实践中损害 downstream performance。这是 narrative vs evidence 的根本矛盾。

论文 §4.5 的 "allocation strategy rather than KL training quality" 归因虽技术上可能正确，但在叙事上自我矛盾——如果方法必须搭配不同的 allocation strategy 才能工作，而论文全篇以 global allocation 为主线，这就是 framing 失败。

**C3. [critical] 核心新颖性不足：与 MaskLLM 框架高度重叠** [R2-N1, R1 交叉 AGREE]

MaskLLM (Fang et al., NeurIPS 2024) 的高层框架与本文几乎完全一致：frozen base model weights + learnable masks + Gumbel relaxation + KL divergence training。本文的 delta 是将这一已验证有效的训练范式从 weight N:M sparsity 迁移到 activation per-token sparsity。

论文 §2 的辩护——"structural mismatch does not arise in MaskLLM's per-group categorical setting"——恰好说明本文的核心 "insight" 是 task-specific 适配而非通用方法论贡献。方法部分（§3.1-§3.4）除 adaptive penalty controller（一个 augmented Lagrangian 的简化 heuristic，§3.4 脚注自承）外，每个组件都有直接对应：Gumbel-Sigmoid→MaskLLM/Concrete，KL distillation→MaskLLM/standard KD，per-layer MLP predictor→DejaVu/FastForward。

如果重定位为 **empirical analysis paper**（"验证 KL 范式在 activation sparsity + global allocation 下的表现，发现 structural mismatch 和 regime 现象"），novelty 问题会缓解。但当前 framing 混合了 method contribution 和 analytical contribution，拉高了 novelty expectation。

**C4. [critical] 无 wall-clock speedup，效率动机空洞** [R2-N2, R1 AGREE (介于 critical/warning)]

Table 8 (Appendix A) 显示 KL predictor 在 50% sparsity 下 latency 126.78ms vs dense 119.11ms，即**增加 6.4% 延迟**。Unstructured element-wise masks 无法利用硬件稀疏加速。Title "Contextual Sparsity Prediction" 和 Introduction 从 inference efficiency 角度切入，建立了效率提升的预期。Abstract 的 "49% reduction" PPL 容易被误读为速度提升。

Limitations 的坦诚报告和 Conclusion 的 "prediction quality rather than systems optimization" 部分缓解了此问题，但 Conclusion 最后一段又提到 "wall-clock speedup" 和 "practical deployment value" 作为 future directions，与 understanding framing 矛盾。

### Should-Fix Issues (影响评分但不一票否决)

**W1. [warning] BCE vs KL 对比存在 pipeline 混淆变量** [R1-N3 (critical), R2 REBUT→warning; 共识 warning]

KL 和 BCE 使用完全不同的 pipeline：KL 用 Gumbel-Sigmoid soft masks + adaptive penalty + KL loss, BCE 用 hard masks + compensation (optional) + BCE loss。论文 claim "the failure is structural" (§4.3) 无法从现有实验 cleanly 验证。

Table 3 的 isolation 实验提供了 reasonable（但非 definitive）evidence：Forward KL+Gumbel (11.79) vs KL+STE (15.77) 隔离了 relaxation (+3.98); KL+Gumbel (11.79) vs BCE+Gumbel+Penalty (38.02) 隔离了 loss (+26.23)。但 BCE+Gumbel+Penalty 之所以差，可能是 penalty 破坏了 BCE 的 per-neuron convergence，而非 KL 本身好。

关键缺失：(1) MSE on hidden states ablation (intermediate coupling, 对应 Table 1 intermediate 列); (2) Per-layer KL ablation (解耦 cross-layer Jacobian coupling)。

**W2. [warning] 三 regime 分析证据密度不足** [R1-W1 + R2-W3, 交叉全 AGREE]

Budget-surplus/constrained/limited 三个 regime 基于 3 个 sparsity level (30%/40%/50%) × 2 allocation = 6 data points。每个 regime 仅 1 个观测。30%→40% preference reversal 的 boundary 未定位（缺 35% 数据）。Mistral 上无 downstream regime 数据。措辞应降为 "preliminary observations" 而非 "three regimes"。

**W3. [warning] d030 exp_id 暗示 regime analysis 可能使用了错误 predictor** [R2 交叉中发现, R1 未覆盖]

Table 5 中 d030_kl40_uniform 和 d030_kl50_uniform 的 "d030" 前缀强烈暗示使用了 30%-trained predictor，而 Table 5 caption 声称 "Each row uses a predictor trained at the respective sparsity target"。若属实：(1) 40%/50% uniform 行使用了 mismatched predictor → 与 global 行（properly trained）的对比不公平; (2) 整个 regime analysis 的 global vs uniform preference reversal 可能是 artifact。需要作者确认 d030 前缀含义。

**W4. [warning] Train-inference mask mismatch 未量化** [R1-W3, R2 交叉 AGREE]

训练 soft masks (τ=0.1) vs 推理 hard binary masks from global top-k，gap 未 clean 分离。§4.5 gap decomposition ("53% predictor error + 47% allocation loss") 混合了 discretization 和 allocation 两个效应。需要：soft per-token→hard per-token (隔离 discretization) + hard per-token→hard global (隔离 allocation) 的 controlled comparison。

**W5. [warning] 主表结果单 seed** [R1-W4, R2 AGREE]

Table 2 所有关键对比（KL global 11.79, TEAL 23.31 等）均为单 seed。3-seed 仅限 50% uniform (PPL 11.92±0.07)。30% MMLU=25.27% 若有 ±2pp variance 可能与 random baseline 无显著差异。

**W6. [warning] 模型规模局限** [R1-W5, R2 AGREE]

仅 7-8B 规模 (LLaMA-3.1-8B, Mistral-7B-v0.3)。Title "SwiGLU LLMs" 暗示广泛适用性。Regime boundaries 很可能 scale-dependent。

**W7. [warning] Penalty controller "convergence" claim 不准确** [R1-W6, R2 AGREE]

§3.4 claim "converges within 40-110 steps across all targets"，但 Appendix C Table 11 显示 30% target λ=5000 (cap, deviation=5.0%) 和 70% target λ=1000 (cap, deviation=1.7%)。Hit cap ≠ convergence，是 saturation。只有 40% 和 50% 真正收敛。

**W8. [warning] Structural mismatch 洞察新颖性受限** [R2-W1, R1 AGREE]

End-to-end 目标优于 decomposed 目标是深度学习基本原则。§3.5 的梯度分析本质是 chain rule 标准应用——factor (b) 的 Jacobian 耦合是任何 end-to-end loss 的固有性质。"F1 高反而 PPL 差" 的 empirical finding 有独立价值，但将其包装为 "formal gradient analysis" 级别理论贡献属过度。

**W9. [warning] Taxonomy (Table 1) 贡献价值有限** [R2-W2, R1 部分 REBUT→共识: organizational utility but not independent contribution]

2D taxonomy 是 post-hoc organization，无 predictive power。空 cell (Static×Decomposed, Static×Intermediate) 未讨论原因。共识：taxonomy 有组织价值但不应作为独立 contribution，适合降为 Related Work 组织框架。

**W10. [warning] Missing references** [R2-W4, R1 AGREE]

32 篇引用对 EMNLP long paper 偏少 (typical 40-60)。关键遗漏：
- MiniLLM (Gu et al., ICLR 2024): forward vs reverse KL for LLM distillation，与 §4.4 ablation 直接相关且结论相反（MiniLLM 发现 reverse KL 更好）
- SparseLoRA (ICML 2025): contextual sparsity for fine-tuning
- Broader LLM distillation literature (GKD, DistiLLM 等)
- D2DMoE taxonomy positioning 过度简化（其训练含 router + expert conversion，非单纯 MSE）

**W11. [warning] Training/eval domain overlap** [R2-W6, R1 部分 REBUT]

WikiText-103 训练 + WikiText-2 评测。C4 OOD 仅 50% sparsity。Relative advantage 保持 (49%→52.5%) 是正面信号，但缺 30%/40% OOD 数据。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成完全共识：

1. **C1 (22.51 ghost number)**: 核心 claim 数据不可验证——不可接受 [R1 raise, R2 强 AGREE]
2. **C2 (downstream collapse vs narrative)**: Headline method MMLU≈random, narrative 矛盾——需要根本性 reframing [R1-N2=R2-N3, 交叉全 AGREE]
3. **C3 (MaskLLM novelty)**: 核心框架与 MaskLLM 高度重叠，novelty delta 有限 [R2 raise, R1 AGREE]
4. **C4 (no speedup)**: 效率动机空洞，需明确 understanding 定位 [R2 raise, R1 AGREE]
5. **W2 (regime data)**: 每 regime 仅 1 数据点，证据不足 [R1-W1=R2-W3]
6. **W5 (single seed)**: 主表核心对比缺 error bars [R1-W4, R2 AGREE]

---

## Reviewer Divergence [REBUT]

唯一实质分歧：

**W1 (pipeline confound) severity**: R1 评 critical（KL vs BCE 变量未 clean 隔离），R2 降为 warning（Table 3 ablation 提供 reasonable evidence）。

R1 论据：loss 和 relaxation jointly varied，"6.6× loss effect" 计算混淆变量。
R2 反驳：Table 3 中 KL+Gumbel vs KL+STE 和 KL+Gumbel vs BCE+Gumbel+Penalty 构成了 reasonable（虽非 perfect）controlled pairs。

**Director 判断**：采纳 R2 的 warning 级别。Table 3 的 ablation 结构虽不完美但提供了方向性证据。缺 MSE 和 per-layer KL 是 should-fix 而非 must-fix。

---

## Questions to Authors

1. §4.3 中 BCE PPL=22.51 对应哪个具体实验配置？与 Table 2 的 27.97 是什么关系？为什么不在任何表格中？
2. MaskLLM 的训练范式（frozen weights + Gumbel + KL）直接迁移到 per-token activation sparsity 的效果如何？
3. Table 5 中 d030_kl40_uniform/d030_kl50_uniform 的 "d030" 前缀含义是什么？是否使用了 30%-trained predictor？
4. 如果 KL+global 在所有 downstream 设定下不可用，为什么不将 KL+uniform 定为推荐配置？
5. Forward KL 优于 reverse KL (Table 3: 11.79 vs 12.80) 与 MiniLLM (ICLR 2024) 的结论相反——如何解释？
6. 训练结束时 soft mask (τ=0.1) 与 hard mask 的 PPL gap 是多少？

---

## Missing References

1. **MiniLLM** (Gu et al., ICLR 2024): Forward vs reverse KL for LLM distillation——与 §4.4 ablation 直接相关且结论相反
2. **SparseLoRA** (ICML 2025): Contextual sparsity for fine-tuning
3. **GKD / DistiLLM** 等 2023-2025 LLM-specific distillation 工作
4. **Griffin** (De et al., 2024) / **Mixture-of-Depths** (Raposo et al., 2024): Dynamic compute allocation

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目未启用 paperreview.ai）。

---

## Overall Assessment

**Score: 2.5 / 5 — Weak Reject (Borderline Findings)**
**Confidence: 4 / 5**

| 维度 | R1 | R2 | 合议 |
|------|----|----|------|
| Soundness | 2.5 | 3.0 | 2.5 |
| Excitement | 2.5 | 2.0 | 2.0 |
| Reproducibility | 3.5 | 4.0 | 3.5 |
| Overall | 2.5 | 2.5 | 2.5 |

**核心判断**：论文提出了一个有意义的问题（per-neuron BCE vs global allocation mismatch），梯度分析框架和 ablation 设计值得肯定。但四个 critical 问题共同削弱了论文的可接收性：

1. **数据完整性** (C1): "91% worse PPL" 这一核心 claim 依赖的 22.51 数字无法从论文验证——这是提交标准的底线问题
2. **叙事与证据矛盾** (C2): Headline method 在最重要 downstream task 上退化至 random，与 "optimize for global allocation quality" 叙事根本矛盾
3. **有限新颖性** (C3): 核心框架是 MaskLLM 从 weight→activation sparsity 的迁移应用，方法论增量不足支撑独立 conference contribution
4. **效率动机空洞** (C4): 以 sparsity prediction 为题暗示加速但实际增加 overhead

**修复路径**：(a) 修复 22.51 数据溯源; (b) 重定位为 empirical analysis/mechanistic understanding paper 而非 method paper; (c) 以 KL+uniform 为推荐配置, global allocation 作分析对象; (d) Abstract/Intro 明确 "prediction quality, not wall-clock speedup"; (e) 补 MSE ablation + 更多 regime 数据点; (f) 确认 d030 exp_id 问题。修复后有 Findings 潜力。

---

## Detailed Comments (Per Section)

### Abstract
- "91% worse perplexity" 依赖不可验证的 22.51 (C1)
- Headline "49% PPL reduction" 未给 downstream collapse 同等 prominence (C2)
- 未明确声明无 wall-clock speedup (C4)

### Introduction
- Structural mismatch 分析清晰但新颖性受限 (W8)
- Contribution #2 将 taxonomy 作为独立贡献过度 (W9)
- 每条 contribution 有对应 section/table 支撑——结构合理

### Related Work
- MaskLLM 区分段落存在但深度不足 (C3)
- D2DMoE 分类过于简化 (W10)
- 缺 MiniLLM、SparseLoRA、GKD 等 (W10)
- 引用数量偏少 (32 vs typical 40-60) (W10)

### Method
- §3.4 penalty controller "converges" claim 需修正为 "saturates at cap" (W7)
- §3.5 梯度分析数学正确但属 chain rule 标准应用 (W8)
- Taxonomy 适合降为 organizational framework (W9)

### Experiments
- 22.51 vs 27.97 同段矛盾 (C1)
- Table 2 单 seed (W5)
- Table 5 d030 命名需确认 (W3)
- SPON analysis 使用不同 eval protocol (minor)
- Gap decomposition 混合了 discretization 和 allocation (W4)
- Regime analysis 每 regime 仅 1 数据点 (W2)

### Conclusion
- Wall-clock speedup 作 future direction 与 understanding framing 矛盾 (C4)
- 长度适当，总结合理

### Limitations
- 诚实且全面
- WikiText 训练/评测同源提及但 OOD 评测不充分 (W11)

### Ethics / Checklist
- 完整且合规。E1 (AI assistants) 诚实披露。

### Appendix
- Appendix A latency data 证实无 speedup (C4)
- Appendix B-E 覆盖 sensitivity/convergence/OOD/stability——充分
- 格式合规（双栏，在 references 之后）