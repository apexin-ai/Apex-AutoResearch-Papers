---
round: 6
overall_score: borderline
timestamp: 2026-05-17T10:51:12.070132+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 6 审稿报告 — Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+相关工作+写作+完整性)
**轮次**: Round 1 独立审稿 + 交叉回应，1 轮收敛

---

## Summary

本文分析了 SwiGLU LLM 中 per-neuron BCE 训练与 global top-k 推理之间的结构性不匹配，提出用 forward KL 蒸馏 + Gumbel-Sigmoid 松弛训练轻量级稀疏预测器（75.9M params, <1% base model）。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 从 23.31 降至 11.79（49%），并在 Mistral-7B-v0.3 上验证跨架构一致性。论文同时发现了 global vs uniform allocation 的三个操作区域（budget-surplus / budget-constrained / capacity-limited）。

---

## Strengths

**S1. 梯度结构分析提供清晰的方法动机**（R1-S1, R2-S1 共识）
BCE 梯度 per-neuron 独立 vs KL 梯度通过 Jacobian 耦合的形式化分析在数学上正确，SNR 实测（5.77×10⁻⁵ vs 1.00×10⁻⁵，early layers 34-156×）提供了定量支撑。尽管 backprop coupling 是基本性质（R2-N2），但将其 formalize 并指出对 global top-k 的具体后果有增量价值。

**S2. 消融实验设计全面且有信息量**（R1-S2, R2-S2 共识）
Table 3 清晰隔离了各组件贡献：divergence 方向（Forward/Reverse KL/JSD）、relaxation（Gumbel vs STE，Δ=3.98）、loss isolation（BCE+Gumbel+Penalty=38.02 证明 penalty 与 per-neuron 优化冲突）。Loss effect (6.6×) vs relaxation effect 的分解有信息量。

**S3. 三操作区域分析有实用价值**（R1-S3, R2-S3 共识）
Non-monotonic allocation preference（uniform@30% → global@40% → irrelevant@50%）是非 trivial 的经验发现，为部署决策提供指导。在两个架构上验证了一致性。

**S4. 诚实报告负面结果**（R1-S4）
50% downstream 崩溃、penalty 偏差、PPL-downstream 脱节均被坦诚讨论。

**S5. 写作质量良好**（R2-S6）
无 AI 写作痕迹（em-dash、-ing 短语等）。段落结构紧凑，叙事连贯。格式合规（8 页正文、匿名、Limitations/Ethics/Checklist 齐全）。

**S6. 二维 taxonomy 有组织价值**（R2-S5）
Correction granularity × Training signal coupling 的分类框架清晰地定位了本文方法。

---

## Weaknesses

### Critical（影响接收决定）

**C1. [Critical] "Eliminates the need for compensation" 核心 claim 缺少控制实验**
- R2-N3 raise，R1 AGREE
- Table 3 有 BCE+Compensation (25.44) 但无 KL+Compensation。若 KL+compensation 能进一步降至 ~10.x PPL，则 "eliminates the need" 为错误 claim。
- SPON 分析（2.4% PPL improvement）暗示 KL 已捕获大部分可恢复信号，但 SPON ≠ compensation network，不能替代此实验。
- **要求**：补充 KL+compensation 实验；或弱化 claim 为 "enables competitive performance without compensation"。

**C2. [Critical] 技术新颖性有限，已有组件的直接组合**
- R2-N1 raise，R1 AGREE with nuance
- 核心方法由三个已有技术组成：Forward KL distillation (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + adaptive penalty（标准约束优化）。MaskLLM 已使用相同原则（frozen weights + learnable masks + KL training）。
- R1 指出：问题新颖性存在（Per-token × Coupled cell 此前为空），但技术新颖性有限。
- **共识**：论文更适合定位为 empirical analysis / mechanistic understanding 论文而非方法论论文。EMNLP Findings 可能比 Main Conference 更合适。

**C3. [Critical] Coupling vs oracle quality 因果归因未分离**
- R1-W2 raise，R2 AGREE
- 论文将 KL 优势归因于 "gradient coupling"（§3.6），但存在混淆变量：BCE 的 oracle 来自 activation magnitude，KL 直接优化 output distribution。观察到的差距可能源于 (1) 耦合梯度 vs 独立梯度，或 (2) magnitude-based oracle 本身是 output preservation 的 poor proxy。
- **缺失实验**：用 KL-optimal masks 作为 BCE oracle，分离 coupling effect 和 oracle quality effect。
- 此问题与 C2（理论深度）相互加强：如果 coupling 并非核心因素，则论文的理论贡献进一步弱化。

### Warning（影响评分但不一票否决）

**W1. PPL-downstream disconnect 持续存在（跨 4 轮未解决）**
- R1-W3 + R2-W1，交叉全 AGREE。历史 issue R3-C2，已修改多轮但仍存在。
- 50% sparsity（PPL 最大优势区间）：MMLU ≈ random，GSM8K < 2.2%。
- 30% sparsity（推荐操作点）：PPL 改善 19%，但 MMLU 仅 +2pp（40.61 vs 38.61），GSM8K 48.75→7.35%（-85%）。
- 论文以 "49% PPL reduction" 为 headline 但自身承认 PPL is poor proxy——构成自我矛盾。
- **要求**：Abstract/Introduction 更突出 30% 为推荐操作点及该操作点的温和改善幅度。

**W2. 主要结果为单 seed（跨 6 轮未解决）**
- R1-W5 + R2-W2，交叉 AGREE。历史 issue R1-W3，持续 open。
- 仅 50% uniform 有 3-seed（11.92±0.07），其余全部单 seed。
- Gumbel sampling 的随机性在极端 sparsity（70%）下可能导致显著差异。
- **要求**：至少 Table 2 所有行提供 3-seed mean±std。

**W3. Iso-compute 术语误导**
- R1-W1 raise Must-Fix，R2 REBUT 计算错误但同意术语建议。
- R2 正确指出：R1 的 "7000 步" 计算为重复乘法错误。实际 2700 BCE 步 ≈ iso-wall-clock（45 min vs 45.9 min）。但 "Iso-Compute Analysis" 标题中 "2.71× the KL budget" 指步数非 FLOPs/wall-clock，具有误导性。
- **要求**：§4.2 标题改为 "Extended Training Analysis"；正文明确报告 wall-clock 对比。

**W4. 训练/评估域内同质性（跨 2 轮未解决）**
- R1-W8 + R2-W6，交叉 AGREE。历史 issue R4-W3。
- WikiText-103 训练 → WikiText-2 评估，同域（均为 Wikipedia）。OOD 评估（C4）仅覆盖 50% sparsity。
- **要求**：至少补充 30% sparsity 下的 C4 OOD 评估。

**W5. 三区域发现仅 3 个采样点**
- R2-W3 + R1 部分 AGREE。历史 issue R3-S5。
- 三个 "operating regions" 基于 30/40/50% 三个采样点。R1 认为定性观察可建立但精确边界需更多数据。
- **要求**：补充 35%/45% 采样点；或进一步弱化为 "observation at three sampled sparsity levels"。

**W6. 遗漏近期相关工作**
- R2-W4 raise，R1 部分 AGREE。历史 issue R2-W7-Rd2。
- 遗漏：SparseInfer (Shin et al., DATE 2025, arXiv:2411.12692)，SVD Contextual Sparsity Predictors (Serbin et al., 2026, arXiv:2603.14110)。
- **要求**：Related Work 补充讨论（需先验证论文真实性）。

**W7. Mistral 跨架构 claim 缺下游结果**
- R2-W5 + R1 AGREE。
- Table 6 仅报告 PPL，无 downstream benchmarks。"Consistent improvements" 基于 3 个 PPL 数据点。
- **要求**：补充 Mistral downstream 评估（至少 MMLU）；或弱化为 "preliminary evidence"。

**W8. SNR 实验统计力度不足**
- R1-W4 + R2 部分 AGREE。
- 仅 80 steps，无 error bars。BCE SNR collapse after step 10 存在替代解释（收敛而非信号质量问题）。
- **要求**：增加采样至 200+ steps 并报告 95% CI；提供 BCE training loss curve 区分两种解释。

**W9. "Near-orthogonal" 措辞过强**
- R1-W6 + R2 AGREE。
- Cosine similarity 0.196 在 d=4096 维下 ≈ 12σ，是统计显著的非零相关。但 R²=0.038（3.8% 共享方差），功能影响小（2.4% PPL）。
- **要求**：改为 "weakly correlated"。

**W10. 30% target 实际 sparsity 28.5%，偏差未讨论**
- R1-W7 + R2 AGREE。
- 30% 结果实际在 28.5% sparsity 运行，可能高估该操作点性能。
- **要求**：标注实际 sparsity；报告 TEAL@28.5% 对比；或讨论影响可忽略。

### Minor

**M1.** Abstract 数字密度过高（7+ 个数字），建议精简至 2-3 个关键数字。（R2-M1）
**M2.** 术语不一致：predictor-TEAL / KL predictor / KL global / KL uniform。（R2-M2）
**M3.** Table 2 BCE 行标注与 §4.2 描述不一致（inference protocol 差异不清晰）。（R1-W9, R2-M5）
**M4.** §3.4 Forward KL 方向选择的论证过于简短，与 §4.3 的详细讨论脱节。（R1-W11）

---

## Reviewer Consensus（交叉回应后共识）

| Issue | R1 | R2 | 共识 |
|-------|----|----|------|
| Compensation claim 未验证 (C1) | AGREE | Raise | **Critical** |
| 技术新颖性有限 (C2) | AGREE with nuance | Raise | **Critical** (共识: 问题新颖性存在但技术为组合) |
| Coupling vs oracle confound (C3) | Raise | AGREE | **Critical** |
| PPL-downstream disconnect (W1) | Raise | AGREE | **Warning** (持续 4 轮) |
| Single seed (W2) | Raise | AGREE | **Warning** (持续 6 轮) |
| Iso-compute 术语 (W3) | Raise Must-Fix | REBUT 数字 + AGREE 术语 | **Warning** (R2 纠正了 R1 的计算错误) |
| OOD 评估不足 (W4) | Raise | AGREE | **Warning** |
| 三区域采样不足 (W5) | Partial AGREE | Raise | **Warning** |
| Missing refs (W6) | Partial AGREE | Raise | **Warning** (需验证) |
| Mistral 缺下游 (W7) | AGREE | Raise | **Warning** |
| SNR 统计 (W8) | Raise | Partial AGREE | **Warning** |

---

## Reviewer Divergence

| Issue | R1 立场 | R2 立场 | Director 判断 |
|-------|---------|---------|--------------|
| 梯度分析 triviality | Should-Fix（formalization + SNR 有增量价值）| Critical（backprop 基本性质）| **Should-Fix → 合并入 C3**。Formalization 有边际价值，但论文将此作为 Contribution 1 则权重过高。核心问题是 C3 的因果归因缺失。|
| Iso-compute 严重程度 | Must-Fix（7000 步计算）| REBUT（2700 步已 iso-wall-clock）| **Warning**。R2 正确纠正了 R1 的算术错误。实际已接近 iso-wall-clock，但术语应修正。|
| Forward KL 理由 | 偏弱 | 充分（§4.3 有论证）| **Minor**。§4.3 确实提供了技术论证和消融支持，但 §3.4 太简略需要交叉引用。|

---

## Questions（需作者回应）

**Q1.** KL + compensation 的效果如何？这是直接验证核心 claim 的必要实验。（R2-N3, R1 AGREE）

**Q2.** 如果用 KL-optimal masks（而非 magnitude-based masks）作为 BCE oracle，BCE 能否缩小与 KL 的差距？这能分离 coupling effect 和 oracle quality effect。（R1-W2, R2 AGREE）

**Q3.** 是否测试过 MSE on output logits 作为中间方案？这能隔离 "coupling"（任何 end-to-end loss 都有）和 "distributional matching"（KL-specific）的各自贡献。（R2-Q2, R1 AGREE）

**Q4.** BCE+Gumbel+Penalty (38.02) 比 vanilla BCE (27.97) 还差——为什么 Gumbel 帮助了 KL 却伤害了 BCE？论文 §4.3 的解释过于简短。（R1-Q3, R2 AGREE 并提出机制假说）

**Q5.** BCE SNR collapse after step 10 是过拟合还是收敛？请提供 BCE training loss curve。（R1-Q5, R2 AGREE）

**Q6.** Per-layer PPL 贡献分解是否与 SNR pattern（early layers 34-156×, late layers 1.7-3.8×）一致？（R2-Q3, R1 AGREE）

**Q7.** KL 优势主要在 PPL 而非 downstream tasks——distributional fidelity 和 task-relevant preservation 之间是否存在 fundamental gap？（R2-Q4, R1 AGREE）

---

## Missing References

1. **SparseInfer**: Jiho Shin, Hoeseok Yang, Youngmin Yi. "SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference." DATE 2025. arXiv:2411.12692. （R2 raise，R1 部分 AGREE。需验证真实性。）
2. **SVD Contextual Sparsity Predictors**: Georgii Serbin et al. "SVD Contextual Sparsity Predictors for Fast LLM Inference." March 2026. arXiv:2603.14110. （R2 raise，R1 部分 AGREE。需验证真实性。）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。

---

## Overall Assessment

**评分: Borderline (2.5/5) — Borderline Findings**
**置信度: High (4/5)**

两位 Reviewer 独立给出一致评分（均 2.5/5），交叉回应后主要分歧在严重程度而非方向，整体收敛良好。

### 核心判断

本文在实验层面做了扎实的工作——消融设计全面（Table 3）、跨架构验证到位（Table 6）、三区域分析有实用价值（Table 5）、负面结果诚实报告。写作质量良好，格式完全合规。

但三个 Critical 问题阻碍 Main Conference 接收：

1. **核心 claim 未验证**（C1）：论文最突出的 claim "eliminates the need for compensation" 缺少 KL+compensation 控制实验。这是一个简单但关键的实验 gap。

2. **技术新颖性有限**（C2）：方法是已有技术（KL + Gumbel + Lagrangian）的直接组合。MaskLLM 已展示了相同原则在 N:M sparsity 中的应用。Per-token × Coupled 的问题空间填充有价值，但单纯的组合应用不构成 EMNLP Main 级别的方法论贡献。

3. **因果归因不足**（C3）：将 KL 优势归因于 "gradient coupling" 但未分离 coupling effect 和 oracle quality effect。梯度分析形式化了 backpropagation 的基本性质（R2 观点）/ 有增量价值但不构成 strong theory（R1 观点）。

### 实际影响力的限制

- 推荐操作点（30% sparsity）：MMLU 65→40%（-38%），GSM8K 48→7%（-85%），改善温和（PPL 19%, MMLU +2pp vs TEAL）
- 50% sparsity（最大 PPL 优势区间）：downstream 完全崩溃
- 6.4% 推理开销、无 wall-clock speedup

### 建议

1. **重新定位**：将论文定位为 empirical analysis / mechanistic understanding 论文，而非方法论论文。降低 "structural mismatch" 理论贡献的权重，强化经验分析的贡献（三区域发现、PPL-downstream disconnect 的量化、BCE 失败模式分析）。
2. **补充关键实验**：KL+compensation、KL-oracle BCE ablation、multi-seed、30% C4 OOD、Mistral downstream
3. **修正 claims**：弱化 "eliminates compensation"、修正 "near-orthogonal"、修正 "iso-compute" 术语
4. **考虑 Findings track**：论文的实验工作高于平均水平，定位为 Findings 论文更合适

---

## Detailed Comments（逐节）

### Abstract
- 数字密度过高（7+ 个数字），建议精简至 2-3 个关键数字
- 缺少 scale 限定（"at the 7-8B scale"）
- "49% PPL reduction" 作为 headline 但论文自身承认 PPL is poor proxy

### Introduction
- 梯度分析的呈现清晰（Eq. 10 vs 11）
- Contribution 1（"Identification of structural mismatch"）可进一步弱化为 "Empirical observation and quantification"
- 建议更突出 30% 为推荐操作点

### Method (§3)
- 数学表述正确，SwiGLU、Gumbel-Sigmoid、KL loss 的推导无误
- Adaptive penalty controller：footnote 正确区分了与 augmented Lagrangian 的差异
- Taxonomy（Table 1）作为组织框架有价值

### Experiments (§4)
- §4.2 Iso-compute：标题需修改；wall-clock 数据应显式报告
- §4.3 消融：设计优秀，是论文最强的部分
- §4.4 三区域：仅 3 采样点，需更多数据或弱化 claim
- §4.5 SPON："near-orthogonal" 需修正
- §4.6 Cross-arch：缺 downstream 数据

### Related Work (§5)
- 覆盖度可接受但可补充 SparseInfer、SVD-CSP
- MaskLLM 对比已较充分

### Conclusion
- 简洁得体
- Future directions 与 understanding paper 定位一致

### Limitations
- 坦诚全面
- 可补充 coupling vs oracle quality confound 的讨论

### Appendix
- 内容扎实（latency、sensitivity、Lagrangian dynamics、OOD、stability）
- 信息密度高

---

## Issue Tracker 同步

本轮新增 7 个 issues（R6-N1, R6-W1 至 R6-W6, R6-M1），更新 8 个跨轮 issues 的 mentions 和 action_items。详见 `artifacts/review_issues.yaml`。

跨轮持续未解决的核心问题：
- PPL-downstream disconnect（R3-C2）：已修改 4 轮，仍存在自我矛盾
- Single seed（R1-W3）：持续 6 轮 open
- OOD 评估不足（R4-W3）：持续 2 轮 open
- 新颖性定位（R3-S1）：已修改 3 轮，建议进一步弱化方法论 claim