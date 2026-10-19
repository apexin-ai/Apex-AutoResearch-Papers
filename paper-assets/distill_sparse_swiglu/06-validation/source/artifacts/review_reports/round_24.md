---
round: 24
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-23T07:46:36.696059+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 27 审稿报告 (Fresh Review)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026), Long Paper
**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作）
**交叉分享**: 完成（R2 提交完整 [AGREE]/[REBUT] 回应；R1 提交摘要回应）

---

## Summary

本文提出用前向 KL 散度替代传统 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器（<1% 参数开销）。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL predictor 实现 14.5% PPL 改进（matched sparsity），跨 Mistral-7B 和 Qwen-2.5-14B 一致泛化。论文通过 target-swap ablation（C1）和 per-layer KL 控制（K=1/K=4）尝试分解 signal type vs coupling scope 的贡献，但该分解受 train-inference mismatch 严重 confound。知识密集任务出现系统性退化（MMLU −5.2pp/8B, GSM8K −20.1pp/14B），机制未获因果解释。

---

## Strengths

**S1. 跨架构一致的 PPL 改进** [R1/R2 共识]
KL predictor 在 LLaMA-3.1-8B（14.5%）、Mistral-7B（17.3%）、Qwen-2.5-14B 上均展示一致的 PPL 优势，在多稀疏度（30-70%）和 OOD（C4）条件下均成立。这是本文最 robust 的发现。

**S2. 罕见的消融深度** [R1/R2 共识]
20+ 页附录（Appendix A-W）系统性消融几乎每个设计维度，在同类工作中极为罕见，体现严谨的实验方法论。

**S3. Target-swap ablation (C1) 设计巧妙** [R1/R2 共识]
通过在 BCE 上训练 KL 发现的 oracle masks，分离 "mask 质量" 与 "训练机制" 的贡献。C1 在 50% 下与 KL 仅差 ≤0.79pp，在 30% 3-seed 下 ≤1.70pp，说明 KL 的优势主要来自发现了更好的 mask patterns。

**S4. 诚实的负面结果报告** [R1/R2 共识]
MMLU −5.2pp、GSM8K −20.1pp、MSE catastrophic seed（PPL=15,789）、MMLU 高方差（σ=9.5）等不利结果在 Abstract、正文和 Limitations 中坦承报告。

**S5. 有用的概念框架** [R1/R2 共识]
Table 1 的 Prediction Target × Training Signal Coupling taxonomy 为后续工作提供清晰的分析框架。

**S6. 高可复现性** [R1/R2 共识]
训练配置、硬件规格、seed 信息、评估协议均有完整记录，承诺开源。Reproducibility 4/5。

---

## Weaknesses

### Critical

**C1. K=1 signal type 分解受 train-inference mismatch 严重 confound** [R1-N1, R2-N1 完全共识]
K=1 训练时仅 1/32 层被 mask，推理时 32/32 层全部 mask，造成严重 distribution shift。K=4 修正不充分（仍仅 12.5%），且 K=4 MMLU 系统性超过 E2E（42.7±1.4 vs 40.7±1.3 across all 3 seeds），说明 mismatch 引入不可预测 artifact。K-curve（K=1,2,8,16,32）中除 K=4 外均为 single-seed (s42)，论文自承 "should be treated as preliminary"。K=16 PPL（8.67）优于 E2E（8.81）的 non-monotonic pattern 可能是 seed-specific artifact。论文标注 "upper bound" 但 mismatch 方向可能系统性高估 signal type 贡献（K=1 在近 dense 条件下训练更容易）。Signal type vs coupling scope 分解是论文超越 "换 loss function" 的核心分析贡献；如果不可靠，理论洞察价值大幅缩水。

**C2. "Primary design dimension" claim 泛化性不足** [R2-N1, R1 共识]
结论称 "Output-distribution alignment is the primary design dimension at moderate sparsity"，但在知识密集任务上 magnitude-based TEAL 始终优于 KL predictor：MMLU（45.86 vs 40.7, −5.2pp）、GSM8K（8.79 vs 7.5）。跨架构信号混合：Mistral MMLU 持平；Qwen-14B GSM8K −20.1pp。Claim 仅在 PPL + commonsense 维度成立。

**C3. Knowledge-task regression 缺乏因果解释** [R1-W2, R2-N2 完全共识]
C4 控制实验否定了训练数据偏差假说但仅 1 seed。"Mode-covering dilutes rare activations" 仅是推测，缺乏直接证据。关键数据点：KL uniform MMLU 40.7 vs TEAL uniform 45.86（同为 uniform allocation），5pp 差距不能用 allocation 解释，必须归因于 KL loss 本身。跨 scale 退步（8B→14B GSM8K 从 −1.3pp 到 −20.1pp）暗示方法根本限制但未提供缓解路径。

### Warning

**W1. 3-seed 下游指标统计功效不足** [R1-N2, R2-W5 共识]
30% Global MMLU σ=9.5pp：n=3 下 95% CI ≈ ±23.6pp（t-distribution, df=2），基本无统计信息量。Abstract/Conclusion 中 "commonsense gains" 措辞未带 Section 4.2 中的 "directional evidence" 限定。按 ARR guidelines R5 要求 error bars / significance tests，论文未充分满足。

**W2. C1 target-swap ablation 存在未隔离混淆变量** [R1-W1, R2 部分同意]
Soft→hard 二值化同时改变 mask 来源和 mask 表示。BCE+Gumbel（32.22）vs 标准 BCE（27.97）差 15% 说明 Gumbel 表示本身有显著影响。但 R2 指出核心发现仍成立：KL-derived hard masks + BCE 仍远优于 magnitude-derived masks + BCE（15.71 at 30%），mask 质量是关键因素。缺少控制实验隔离 mask 来源 vs mask 表示。

**W3. 术语一致性问题** [R2-W2, R1 交叉同意]
核心概念至少 5 种表述：output-distribution distillation / alignment / optimization / KL distillation / distribution-matching。应统一为一个主术语。

**W4. Contribution framing 存在张力** [R2-W1]
反复声明 "primarily an empirical study" 但贡献列表包含方法性暗示。实际引入了具体方法（KL predictor + Gumbel-Sigmoid for contextual sparsity），不仅仅是比较现有方法。

**W5. Wall-clock speedup 缺失** [R2-W6]
Predictor 增加 6.4% latency，当前方法增加而非减少延迟。论文已正确 frame 为 analytical contribution，但缺乏理论加速估算。

### Minor

- **M1**: Introduction 中 68% divergence 和 32% Jaccard 同句出现混淆
- **M2**: "the first decomposition" 措辞应更审慎
- **M3**: Table 2 caption 信息过载（3 个脚注标记 + 多个解释条款）
- **M4**: Introduction MMLU 40.7±1.3% 无 dense baseline 对比（dense 65.27%）
- **M5**: MSE 50% 仅报告 s42，s123 catastrophic（PPL=15,789），正文讨论容易误解为 robust finding

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上完全一致：
1. **PPL 改进 robust 且一致**——跨 3 架构、多稀疏度、OOD
2. **K=1 signal type 分解存在 train-inference mismatch confound**——K=4 修正不充分，K-curve 多数 single-seed
3. **3-seed 不足以支撑下游 claims**——Abstract/Conclusion 措辞需加统计限定
4. **Knowledge regression 缺乏因果解释**——C4 控制 1 seed 不够，mode-covering 假说未验证
5. **新颖性为组合级别**——KL + Gumbel-Sigmoid recipe 与 MaskLLM 共享，新颖性在于 contextual activation sparsity 应用 + 分析框架
6. **Findings 级别贡献**（3.0–3.5 区间）

## Reviewer Divergence [已解决]

| 争议点 | R1 | R2 | 裁定 |
|--------|----|----|------|
| R1-W3: Limitations 是否覆盖实验缺口 | 未覆盖 | [REBUT] 已覆盖（generation, seq_len, batch） | R2 正确——Limitations page 9 明确含三点 |
| R1-W4: Table 14 数值不一致 | 50% Global MMLU=35.7±9.5 vs 28.3±0.7 | [REBUT] R1 误读行标签，35.7±9.5 是 30% Global | R2 正确——经核实数据一致 |
| R1-Minor-1: SNR 叙事张力 | coupling 应提高 SNR | [REBUT] 论文叙事是 "despite lower SNR" | R2 正确——Section 3.6 明确 |

---

## Questions

1. K=4 MMLU 超过 E2E 的机制？如果来自 allocation artifact，意味对知识任务 allocation 可能比 signal type 更重要，这对 "primary design dimension" 结论意味什么？
2. KL uniform MMLU 40.7 vs TEAL uniform 45.86（同 allocation），5pp 差距是否完全归因于 KL loss 本身？与 "allocation contributes" 的解释矛盾。
3. Compensation network 为何不能恢复 knowledge-intensive 性能？
4. C1 中 s42 oracle provenance 对结果的影响（s42 gap 0.65pp vs s123/s456 ≤0.03pp）？
5. Forward vs Reverse KL 在 30% 下差异（8.81 vs 9.26）有统计显著性吗？JSD≈Forward KL (8.90 vs 8.81) 暗示 divergence 选择影响不大。

## Missing References

两位 Reviewer 均未发现重大遗漏。Related Work 覆盖了 TEAL、DejaVu、MaskLLM、CATS、R-Sparse、FastForward、SVD-CSP、LaRoSA、COTS、SparseInfer、ProSparse、SparseLoRA 等 2024-2026 主要工作。

## External Review (Stanford Agentic Reviewer)

未请求。

## Visual Layout Check（非评分项）

状态：**已完成** (3 warnings, 16 info, 0 critical)

- **[warning] Page 6**: 整页纯文本（Experiments 设置），建议将部分移至 Appendix 或穿插示意图
- **[warning] Page 7**: 单页 3 个表格（Table 2/3/4），视觉密集拥挤，考虑将其中一个移至下页
- **[warning] Page 20**: 末页仅 ~13 行（<15% 利用率），大量空白
- 正文在第 8 页内结束，符合 EMNLP/ACL 8 页限制 ✓
- Tables 使用 booktabs 风格，格式规范 ✓
- References 格式统一，无未解析引用 ✓

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Overall | 3.5 | 3.0 | 3.0 |
| Soundness | 3/5 | 3/5 | 3/5 |
| Excitement | 3/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**理由**：论文提供了有价值的实证发现——KL distillation 一致且显著地优于 BCE 用于稀疏性预测（PPL 层面），实验设计深度罕见，负面结果报告诚实。但三个 critical 问题限制了接收级别：(1) signal type 分解（论文的核心分析贡献）受 K=1 train-inference mismatch 严重 confound，K-curve 多数 single-seed，结论可靠性不足；(2) "primary design dimension" claim 在知识任务上不成立（TEAL 始终优于 KL），泛化性不足；(3) knowledge regression 跨架构/跨 scale 一致但缺乏因果解释。新颖性为组合级别（已知组件的新应用），非方法论突破。实用贡献（KL > BCE for PPL）足以进入 Findings，但分析性 claims 的可靠性问题阻止 Conference 接收。

**提升至 Conference (3.5–4.0) 的路径**：
1. K-curve 全部 K 值做 3-seed（计算开销低，每个 K 仅需 1000 steps × 3 seeds）
2. 将 "primary design dimension" 明确限定为 "for PPL and commonsense at moderate sparsity"
3. Knowledge regression 增加因果分析（knowledge neuron probe 或 mixed-domain training）
4. Abstract/Conclusion 下游声明加统计限定语（"directional"）
5. C4 控制实验增至 3+ seed

---

## Detailed Comments

**Abstract**: 信息密度高，两个问题：(1) "commonsense gains" 未带 "directional" 限定；(2) 14.5% PPL 引用基准（matched-sparsity, Appendix D）在 Table 2 中找不到（Table 2 TEAL uniform 30%=10.82 对应 18.6%），呈现方式可能困惑读者。

**Introduction**: (1) "diverge 68%... (per-layer Jaccard 32%)" 是互补度量同句混淆；(2) "MMLU 40.7±1.3%" 无 dense baseline 不传达退化幅度；(3) "the first decomposition" 应改为 "a systematic decomposition"。

**Method (Section 3)**: 技术叙述清晰，公式正确。Gradient analysis 提供有用直觉但 KL 的优势不来自更清晰的梯度信号（SNR 一致低于 BCE）。

**Experiments (Section 4)**: 核心 PPL 实验设计合理。Section 4.5 per-layer KL 分解是最重要也最有争议的部分——需降级为 "exploratory analysis with acknowledged confounds"。Section 4.2 knowledge regression 讨论诚实但不充分——KL uniform vs TEAL uniform 在 MMLU 上 5pp 差距的归因未分析。

**Related Work (Section 2)**: 覆盖全面，与 MaskLLM 的三点区分具体且技术性强。

**Conclusion**: "primary design dimension" 应限定适用范围为 PPL + commonsense。

**Limitations**: 覆盖充分（sparsity sweet spot, knowledge regression, training data, generation tasks, seq_len, batched inference），简洁有效。

**Appendix**: 极为丰富（A-W），体现实验严谨性。K-curve（Appendix W）多数 single-seed 限制了分解结论的可靠性。