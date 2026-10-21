---
round: 3
overall_score: borderline
timestamp: 2026-05-17T04:57:44.773387+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 2 审稿报告 — distill_sparse_swiglu → EMNLP 2026

## Summary

本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器，通过 Gumbel-Sigmoid 松弛和自适应惩罚系数实现端到端可微训练。在 LLaMA-3.1-8B 上 50% 稀疏度达到 PPL 11.79（对比 TEAL 23.31），并在 Mistral-7B 上验证跨架构一致性。Round 1 的多数 issues 已修复到位，但 Round 2 发现了新的方法学严谨性问题（术语误用）和 framing 问题（relative advantage inflation）。

## Strengths

- **核心结构论证有效**：BCE 梯度 factorize per-neuron（Eq. 8）导致无法学到 global top-k 所需的 inter-neuron coupling，这一诊断有理论支撑且通过 iso-compute saturation 和 BCE+Gumbel+Lagrangian (PPL 38.02 > vanilla BCE 27.97) 实证验证。
- **消融设计系统且充分**：Table 3 隔离 loss function (ΔP=26.23) vs relaxation method (ΔP=3.98)，结论清晰。
- **Regime 分析有实用价值**：budget-surplus / budget-constrained / capacity-limited 三分法对实践者有指导意义。
- **Limitations 诚实**：明确承认无实际加速、仅 7-8B 模型、per-target 训练的限制。
- **SPON 区分度充分**：cosine similarity 0.196 + PPL 分解定量展示两方法互补性。
- **Round 1 修复到位**：12 个 Round 1 issues 中 9 个已完全 resolved，验证确认无退步。

## Weaknesses

### Must-Fix (Critical)

**1. [R1-W1-Rd2] "Lagrangian" 术语误用 [两位 Reviewer 独立一致, AGREE]**
- Eq. 9 是带 deadzone 的二次惩罚项，Eq. 10 是几何倍增/减半 schedule。这既不是 augmented Lagrangian (需 λ←λ+α·g(x))，也不是对偶上升法。将其称为 "Lagrangian" 和 "dual variable" 存在术语误导。Penalty method 不保证满足 KKT 条件，论文未讨论收敛保证。
- **修复方向**：改称 "adaptive penalty controller"；讨论为何选择启发式 schedule 而非标准对偶上升。

### Should-Fix (Warning)

**2. [R1-W5 / R1-W2-Rd2] λ/sparsity 时序曲线缺失 [两位 AGREE]**
- Appendix C Table 7 仅报告最终状态。30% 和 70% target 的 λ hit cap (5000/1000) 暗示可能存在 boundary 震荡。缺少 (step, λ) 和 (step, actual_sparsity) 时序曲线。"~10 步达到稳态" 的 claim 无可视化证据。
- **修复方向**：补充 3 个 target 的时序 figure。

**3. [R2-W2-Rd2] "相对优势随 sparsity 增长" 是 baseline collapse artifact [R1 AGREE]**
- (TEAL-KL)/TEAL 在 TEAL 崩溃时自动 inflate（18%→49%→82%）。应同时报告 KL/Dense ratio (1.47×→1.93×→2.93×) 以诚实反映 KL predictor 自身的退化曲线。
- **修复方向**：Abstract 和 §4 同时报告 KL/Dense ratio。

**4. [R2-W3-Rd2] Scale limitation 与 claim 不匹配 [R1 AGREE]**
- 仅 2 个 7-8B 模型，§4.6 末句 "structural property of SwiGLU networks" 过强。
- **修复方向**：加 "at 7-8B scale" 限定。

**5. [R2-W4-Rd2] Downstream collapse + 30% MMLU 异常 [两位 AGREE]**
- 50% 时 MMLU≈random；30% KL-global (25.27%) 比 TEAL (38.61%) 更差。实际有效操作点仅 ≤30% uniform。论文归因 "global top-k starves layers" 但缺 layer-wise 分析。
- **修复方向**：补充 30% global 的 per-layer 保留率分布；正文显式推荐 30% uniform 为实际操作点。

**6. [R2-W7-Rd2] Reference count 偏低 (22 refs) [两位 AGREE]**
- 缺 Wanda, SparseGPT, Switch Transformer, Kim & Rush 2016, DistilBERT, Louizos et al. 2018 (L0/Concrete distribution)。EMNLP 典型 30-50 refs。
- **修复方向**：补充上述引用并在 Related Work 中简要 positioning。

### Nice-to-Fix (Info)

**7. [R2-W5-Rd2] 12+ 处 em-dash 是 AI 写作信号 [R1 降为 info]**
- R2 列为 warning，R1 REBUT 认为 em-dash 是合法标点，最多 info。共识：减少频率即可。

**8. [R1-W3-Rd2] Gradient SNR 缺显式数学定义 [R2 降为 info]**
- R1 列为 warning，R2 REBUT 认为上下文足以推断但应补定义。

**9. [R1-W3] n=3 seeds 统计效力 [维持 info]**
- 两位均认为对 regime 分析核心结论不构成威胁（差异远大于 noise floor），但 global/uniform PPL 差异 (0.17) 的显著性无法确认。

## Reviewer Consensus [AGREE]

1. **Lagrangian 术语误用** — 必须改称 adaptive penalty method (critical)
2. **Relative advantage framing inflate** — 应加 KL/Dense ratio (warning)
3. **Scale limitation** — §4.6 claim 过强 (warning)
4. **30% MMLU 异常** — 缺 layer-wise 分析 (warning)
5. **Reference count** — 偏低需补充 (warning)
6. **λ/sparsity 曲线缺失** — Round 1 遗留未完全修复 (warning)

## Reviewer Divergence [REBUT]

**新颖性评估**：
- **Reviewer 2** (critical): KL+Gumbel+MLP 是 "predictable combination"，novelty 不足以 main conference
- **Reviewer 1** (REBUT): BCE+Gumbel 实验 (38.02>27.97) 证明组合非 trivial；gradient mismatch 诊断 + iso-compute verification 超越简单 combination；但同意 2D taxonomy framing 有 "填空" 嫌疑

Director 判断：novelty 处于 borderline。核心洞察（per-neuron factorization → global allocation failure）有分析深度，但论文 framing 过于依赖 "filling a cell"。如果强化 "why non-trivial" 的论证（突出反直觉的 BCE+Gumbel 反效果），novelty 勉强够 main conference。

## Questions for Authors

1. Eq. 10 几何倍增的收敛保证是什么？λ hit cap 后约束是否可精确满足？
2. Gradient SNR 的精确数学定义？Over what dimensions (neurons/steps/sequences)?
3. 30% KL-global MMLU 退化 40pp 的 layer-wise mechanism 是什么？
4. BCE+Gumbel (no Lagrangian) 的 PPL 是多少？能否分离 Gumbel noise 的影响？
5. Per-neuron prediction accuracy: KL predictor vs oracle top-k mask 的 F1 是多少？如果低于 BCE 但 PPL 更好，可强化 structural mismatch argument。

## Missing References

- Wanda (Sun et al., 2024) — magnitude-based pruning baseline
- SparseGPT (Frantar & Alistarh, 2023) — one-shot structured pruning
- Switch Transformer (Fedus et al., 2022) — conditional computation via routing
- Kim & Rush (2016), "Sequence-Level Knowledge Distillation" — sequence-level KD
- Sanh et al. (2019), "DistilBERT" — KD for language models
- Louizos et al. (2018), "Learning Sparse Neural Networks through L0 Regularization" — Concrete/Gumbel-Sigmoid 标准引用
- Maddison et al. (2017), "The Concrete Distribution" — binary relaxation 理论基础

## External Review (Stanford Agentic Reviewer)

状态：**已跳过 (skipped)**。未纳入本轮评估。

## Overall Assessment

**Score: Borderline (3.25/5)**

论文执行扎实：核心 KL vs BCE 的结构性论证正确、消融充分、regime 分析有实用价值、Round 1 修复到位。但存在三个层面的问题：(1) 方法学严谨性——Lagrangian 术语误用和收敛曲线缺失；(2) framing 诚实性——relative advantage 部分是 baseline collapse artifact；(3) 实际 impact——有效操作点仅 ≤30%，gains 有限。

novelty 是核心分歧点：如果接受 gradient mismatch 诊断作为分析贡献，加上足够的修复，论文处于 main conference 下限。如果要求 novel algorithm 或 scaling evidence，更适合 Findings。

**Recommendation**: 修复 Lagrangian 术语 + 补时序曲线 + reframe relative advantage 后，可达 **weak accept** 水平。当前版本 borderline，偏向 Findings。

**Confidence: 4/5** — 两位 Reviewer 在关键问题上达成共识，唯一分歧（novelty）已充分辩论。

## Detailed Comments

### §3 Method
- Eq. 9-10: 全文 "Lagrangian" → "adaptive penalty controller"，明确这是工程近似而非理论最优
- §3.6: 补充 SNR 数学定义 (e.g., SNR_l = ||E[∂L/∂θ_l]||² / Var[∂L/∂θ_l])

### §4 Experiments
- Abstract/§4.2: 报告 (TEAL-KL)/TEAL 的同时，报告 KL/Dense ratio
- §4.4/Table 2: 30% global MMLU 异常需 layer-wise budget 分析（哪些层被 starved）
- §4.6 末句: "structural property of SwiGLU networks" → "structural property of SwiGLU networks at the 7-8B scale tested"

### Appendix
- Appendix C: 补充 (step, λ) 和 (step, actual_sparsity) 时序 figure（至少 30%/50%/70%）

### Related Work & References
- 补充 6-8 篇关键引用（见 Missing References）
- 增加 conditional computation (MoE) 段落

### Writing
- 全文 grep `---` 和 ` -- `，将解释性 em-dash 替换为逗号或拆分句子（目标：≤3 处）