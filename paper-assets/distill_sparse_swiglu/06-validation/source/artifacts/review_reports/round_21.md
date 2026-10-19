---
round: 21
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T23:59:56.724485+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 24 (Fresh Review)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性)
**圆桌轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识

---

## Summary

本文用 forward KL divergence + Gumbel-Sigmoid 松弛训练 SwiGLU LLM 的上下文稀疏预测器（75.9M 参数，<1% base），替代传统 BCE per-neuron 独立目标。在 LLaMA-3.1-8B 上，KL predictor 在 30%/50% 稀疏度下分别降低 TEAL 的 PPL 14.5%/50%，且无需额外补偿网络（-67.2M params）。论文通过 C1 target-swap ablation 和 per-layer KL 控制实验分解了 signal type 与 coupling scope 的贡献，并提供梯度分析和 2D taxonomy 组织现有方法。定位为经验研究。

---

## Strengths

**S1. 核心效应量大且跨架构稳健** [AGREE: R1, R2]
KL vs BCE/TEAL 的 PPL 差距在 30%（8.81 vs 11.25/10.82）和 50%（11.84 vs 28.13/23.90）均超过 25%，3-seed 方差极低（σ=0.02 at 30%）。跨架构验证（Mistral-7B -17.3%, Qwen-14B consistent PPL advantage）确认不是架构特异现象。

**S2. C1 target-swap ablation 是精巧的实验设计** [AGREE: R1, R2]
用 KL 发现的 mask 训练 BCE predictor，分离 mask 质量 vs 训练动态的贡献（PPL within 0.79pp at 50%, s42；3-seed at 30% gap ≤1.70pp）。这一分析在稀疏性预测文献中是新颖的。

**S3. 消融覆盖广泛且控制严格** [R1]
Table 4 系统比较 5 种 loss（Forward KL, Reverse KL, JSD, MSE, BCE）× 2 种 relaxation（Gumbel, STE），MSE baseline 除 loss 外完全一致（Appendix G）。附录提供 d_b sensitivity、temperature schedule、training convergence、compensation redundancy 完整 robustness picture。

**S4. 梯度分析提供有价值的理论直觉** [AGREE: R1, R2]
§3.6 清晰展示 BCE gradient 仅依赖 neuron j，而 KL gradient 通过 downstream Jacobian 耦合所有 neuron——解释了 KL 为何能发现 composition-aware mask patterns。

**S5. 自我定位诚实** [AGREE: R1, R2]
论文自称 "primarily an empirical study"，始终保持定位。Limitations 覆盖 seq length、batched inference、知识任务退步等。

**S6. Predictor 高效且训练成本低** [R2]
75.9M params (<1% base)，45 min 单 GPU 训练，消除 67.2M 补偿网络。

---

## Weaknesses

### Must-Fix (Critical)

**C1. Per-layer KL 分解存在根本性 confound，定量声明不可靠** [AGREE: R1-N1, R2 cross-AGREE]

K=1 控制实验存在 32× train-inference mismatch（训练 mask 1/32 层，推理 mask 全部 32 层）。论文标注 "upper bound" 但 Abstract/Conclusion 仍将 "signal type accounts for the majority of the PPL gap" 作为核心贡献呈现，资格限定传达不足。

K=4 在 50% 下反常差于 K=1（PPL 44.23 vs 34.85），与 "K 越大越接近 E2E" 的直觉矛盾，缺乏机制解释。K=4 在 30% MMLU 超过 E2E（42.7 vs 40.7），混入 allocation 效应。仅两个数据点（K=1, K=4）不足以支撑 "29-97% on downstream tasks" 的精确分解。

**重要补充**：定性结论（signal type matters）仍由梯度分析（§3.6）和 Table 4 的 5-loss 对比独立支撑，不完全依赖 per-layer 分解。被削弱的是精确的定量百分比，而非方向性结论。

**C2. 知识密集型任务系统性退步缺乏机制分析** [AGREE: R1-N2, R2 cross-AGREE]

KL 在所有测试规模和架构上均系统性低于 TEAL 的 MMLU/GSM8K：
- 8B 30%: MMLU -5.2pp (40.7 vs 45.86)
- 8B 30% global: MMLU -10.2pp (35.7 vs 45.86), σ=9.5
- 14B 30% uniform: MMLU -2.8pp, GSM8K -20.1pp

§4.4 的 Remove valley (MMLU +3.4pp) 方向正确，但未回答核心问题：为什么 KL 的 output-distribution 目标系统性学到牺牲知识路径的 allocation pattern？是 WikiText-103 训练分布的偏差？是 forward KL mode-covering 的固有特性？还是 Gumbel-Sigmoid 的采样偏差？对于自称 "characterize how training objective shapes sparsity prediction quality" 的论文，这是核心分析空白。

### Should-Fix (Warning)

**W1. 无 wall-clock speedup** [AGREE: R1, R2]
Predictor 增加 6.4% latency overhead，unstructured masks 无法实现实际加速。论文定位为 empirical study 已适当 frame，但实际影响力受限。

**W2. C1 ablation 存在残余 confound** [AGREE: R1-W1, R2 cross-AGREE]
C1 同时改变训练目标（KL→BCE）和 mask 表示（soft Gumbel → hard binary）。Oracle 二值化（logits > 0）丢失排序信息。定性结论（mask patterns transfer quality, PPL within 0.79pp）因 gap 小而稳健，精确量化不可靠。

**W3. 评估覆盖度存在关键空白** [AGREE: R1-W3, R2 cross-AGREE]
无生成任务评估（MT-Bench, AlpacaEval）；序列长度固定 2048；batched inference 未评估。Sparsity 对 autoregressive generation 和长序列的行为可能与 PPL/MC-style tasks 显著不同。

**W4. 高方差下游指标的统计可靠性不足** [AGREE: R1-W4, R2 cross-AGREE]
ARC-c σ=3.6pp（3-seed 95% CI ≈ ±8.9pp），BoolQ σ=11.5pp，使得这些指标的均值差异统计不显著。Table 4 多行仅 s42 单 seed。PPL（primary metric）方差极低（σ=0.02-0.15），结论可靠。

**W5. 跨架构/跨规模泛化证据不足** [R2-N3 降级, R1 AGREE at warning level]
核心实验全部基于 LLaMA-3.1-8B。Mistral-7B 和 Qwen-14B 仅有 main results，无 C1 ablation 或 per-layer 分解。论文已 acknowledge ("evaluation bounded at 7-14B")，但 "dominant design dimension" 声明隐含通用性。

**W6. "Dominant design dimension" 声明需资格限定** [Derived from C1 confound]
该声明的定量基础因 per-layer 分解 confound 不可靠。定性方向由 Table 4 五种 loss 对比和梯度分析支撑，但 "dominant" 措辞过强。建议软化为 "output-distribution alignment substantially outperforms per-neuron classification and intermediate losses"。

### Minor

- Figure 2 y 轴和图例文字偏小（~6-7pt），接近可读性下限（视觉审查 Warning）
- Geometric penalty schedule 实际稀疏度 28.5% vs 名义 30%，Table 2 ‡ 标注存在但不够醒目
- Table 2 中 BCE 30% 使用 global allocation（脚注 †），无 BCE 30% uniform 对比
- 无代码/数据/模型释放声明
- Introduction 中与 MaskLLM 的关系应更早建立（当前仅在 Related Work）

---

## Reviewer Consensus [AGREE]

1. **KL vs BCE/TEAL 的 PPL 优势大、稳健、跨架构一致**——核心发现可靠，不是边界效应
2. **C1 target-swap ablation 是新颖且有价值的实验设计**——在稀疏性预测文献中前所未见
3. **Per-layer KL 分解的 confound 削弱定量声明**——"29-97%" 精确分解不可靠，但定性方向（signal type matters）独立成立
4. **知识密集型任务退步是实际影响力的主要限制**——缺乏机制分析
5. **无 wall-clock speedup 限制了实用价值**——论文 framing 诚实
6. **论文定位诚实、消融全面、写作透明**——高于平均水平

## Reviewer Divergence

**R2-N1 (MaskLLM 新颖性)**：R2 判定 Critical（"仅1句话讨论 MaskLLM"），R1 REBUT（实际4句话，contextual vs static 是 fundamentally different learning problems）。
→ **Director 判定**：R1 factual correction 成立。MaskLLM 区分已有基本讨论，contextual activation sparsity vs static N:M weight sparsity 确是不同学习问题。**降级为 Warning**（Introduction framing 可改善，非 novelty 缺失）。

**R2-N2 ("Dominant" overclaimed)**：R2 判定 Critical（"仅比较两种方法"），R1 REBUT（Table 4 已对比 5 种 loss：Forward KL, Reverse KL, JSD, MSE, BCE）。
→ **Director 判定**：R2 断言为**事实性错误**——Table 4 明确包含 5 种 loss function 的系统对比。但 "dominant" 声明仍因 per-layer 分解 confound 需资格限定。**降级为 Warning**（合并入 W6）。

**R2-W4 (Gumbel confound)**：R2 判定 Warning（"KL 和 Gumbel 贡献未 disentangle"），R1 REBUT（BCE+Gumbel 反而恶化性能；loss effect 5.1× relaxation effect；MSE 使用相同 Gumbel）。
→ **Director 判定**：R1 证据充分，confound 已被论文充分控制。**降级为 Info**。

**R2 遗漏相关工作**：R2 列出 SparseInfer 和 TurboSparse 为遗漏引用——R1 指出两篇均已在 Section 2 引用。**R2 在此处阅读不够仔细。**

---

## Questions

1. K=4 在 50% 下为何比 K=1 差？是否有 gradient interference 或 optimization landscape 解释？增加 K 是否单调恶化？
2. 知识密集型退步是否与 WikiText-103 训练数据分布有关？用含 math/code 的混合语料训练是否缓解？
3. C1 oracle 提取使用 logits > 0 二值化——是否尝试保留连续分数作为 soft label？
4. STE 在 30% 仅达 20.8% effective sparsity——是否调整过 learning rate 或 gradient scaling？
5. MSE 30% 3-seed mean 18.52±1.68 是否包含所有 3 个 seed（含可能的失败 seed）？

---

## Missing References

- **Meng et al., 2022** "Locating and Editing Factual Associations in GPT" — 与知识密集型退步的分析直接相关 [AGREE: R1, R2]
- **GRASP** (Group-Based Prediction of Activation Sparsity, DAC 2025) [R2]
- Li et al., 2023 "Inference with Reference: Lossless Acceleration of Large Language Models" [R1]

---

## External Review (Stanford Agentic Reviewer)

未启用。

---

## Visual Layout Check（非评分项）

**状态**: 完成（2026-05-22，耗时 ~3 min）

- **Critical**: 0
- **Warning**: 1 — Figure 2 的 y 轴标签和图例文字字号偏小（~6-7pt），打印时可能不够清晰
- **Info**: 18 — 整体排版专业整洁。Figure 1 出现在 p2（首个 display item，位置合理）。所有表格 booktabs 风格，格式一致。主正文 8 页符合 EMNLP 限制。Appendix 内容密度高但排版整齐。无未解析引用。

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings (可被 Findings 接收)**

**置信度: 4/5**

### 评分理由

核心发现（KL 显著优于 BCE/TEAL 用于稀疏预测训练）可靠、效应量大、跨架构一致。C1 target-swap ablation 和梯度分析是有价值的分析性贡献。

**Conference (4.0) 的主要障碍**：
1. Per-layer 分解是三大贡献之一，但因 train-inference mismatch confound 和 K=4 反常结果，定量声明（"29-97%"）不可靠——需补充更多 K 值数据或降级为定性讨论
2. 知识密集型任务系统性退步（8B MMLU -5.2pp, 14B GSM8K -20pp）缺乏机制分析——对于自称 "characterize how training objective shapes quality" 的论文，这是核心分析空白
3. 无实际 wall-clock speedup，方法当前无部署价值

**Findings (3.0) 的支撑理由**：
- KL vs BCE 的核心比较稳健（多 seed、多架构、多稀疏度），实证发现有实际参考价值
- C1 ablation 提供了 sparsity prediction 文献中前所未见的分析角度
- 5 种 loss 的系统消融（Table 4）为后续工作提供设计指导
- 消融全面、写作透明、自我定位诚实

---

## Detailed Comments

### Abstract
- 第 5-6 句的 signal type / coupling scope 分解数字应进一步软化或删除精确百分比（"upper bound" 资格限定传达不足）
- "wall-clock speedup requires sparse kernel support not addressed here" 和 "primarily an empirical study" 是重要的 honest disclaimers，应保留

### Introduction (§1)
- 与 MaskLLM 的关系应在 Introduction 更早建立——当前仅在 Related Work 讨论，读者在 Introduction 即会产生 "this is MaskLLM for activation sparsity" 的疑问
- 贡献 bullet 1 的 "29-97%" 分解数字应降级为定性范围
- "This paper is primarily an empirical study" 的定位声明是正确的策略选择

### Method (§3)
- §3.3 Gumbel-Sigmoid 设计选择论证充分，BCE+Gumbel 恶化性能的发现（Table 4）有效排除了 Gumbel 单独解释 KL 优势的假说
- §3.5 geometric penalty 的 deadzone ε=0.02 justification 可简短补充 sensitivity 引用
- §3.6 梯度分析是论文最有价值的部分——但应增加 caveat：coupled gradient 是发现好 mask 的充分条件还是必要条件？C1 结果暗示 coupling 不是推理阶段的必要条件

### Experiments (§4)
- Table 2：BCE 30% 使用 global allocation（脚注 †），建议补充 BCE 30% uniform 对比或说明省略原因
- Table 2：实际稀疏度 ‡ 标注可更醒目
- §4.5 Per-layer KL：需补充 K=8/K=16 或删除精确百分比；K=4 50% 反常结果需假设性解释
- §4.4 Remove valley MMLU +3.4pp：应追问 "why KL learns this pattern" 而不仅是 "what happens if we override it"
- Table 4 核心行（Forward KL + Gumbel, BCE）的 30% 数据应补充 3-seed

### Limitations
- 覆盖三个核心点，篇幅适当（符合 EMNLP 要求）
- 建议加入 "生成任务（open-ended generation）未评估" 作为第四点

### Ethics Statement
- 覆盖数据来源、计算成本、安全性，内容适当