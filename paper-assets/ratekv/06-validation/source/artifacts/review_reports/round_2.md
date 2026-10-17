---
round: 2
overall_score: weak reject
timestamp: 2026-05-15T04:30:43.041758+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## 审稿报告 — Round 1

**论文**: "When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic"
**Target Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**Reviewer Panel**: R1 (方法严谨性 + 实验有效性) + R2 (新颖性 + 完整性 + 写作质量)

---

### Summary

本文研究 per-head mixed-precision KV cache quantization 在 hardware-aligned bit-widths {2,4,8,16} 上的问题。核心发现是 unconstrained solvers（greedy/MCKP）因大量 2-bit head 的 distortion 在 residual stream 中 non-additive compounding 而产生灾难性退化（Qwen2.5-7B 上 PPL 32–37 vs uniform 4-bit 15.45）。提出的修复是 2-bit cardinality constraint（k≤8），将 PPL 降至 11.23（−27.3%）。论文还发现 constrained regime 下 greedy = MCKP，并提出基于 concentration + t₁/t₅ 的 joint diagnostic 区分 spread/spike/flat 三类架构。5 个模型中仅 Qwen 受益，其余 4 个无改善。

---

### Strengths

1. **S1** 2-bit distortion compounding 是 genuine、previously-undocumented 的问题，有直接 warning value——任何使用 {2,4,8,16} bit-widths 做 per-head allocation 的后续工作都需要注意这一 failure mode。
2. **S2** 单个 cardinality constraint 是 minimal、elegant 的修复，不增加额外 hyperparameter（k 由 U-shaped sweep 自动选取）。
3. **S3** 4/5 模型 negative results 的诚实、完整报告。论文未选择性报告仅 Qwen 的正面结果，而是系统展示了 spread/spike/flat 三种 pattern，这对实践者有 go/no-go 信号价值。
4. **S4** Spread/spike/flat taxonomy 提供了有用的 conceptual vocabulary，Yi-1.5 作为 "高 concentration 但无收益" 的 critical test case 设计得当。
5. **S5** 实验的 thoroughness：cross-dataset stability（WikiText-2 vs C4, >96% agreement）、multi-seed stability（std/mean < 0.6%）、per-layer brute-force oracle、KV separation ablation、heuristic baselines 等展示了系统性评估的追求。
6. **S6** 写作清晰、逻辑链连贯，anonymity 和 ACL format 合规。

---

### Weaknesses

#### Must-Fix（影响接收决定）

**W1** [CRITICAL | consensus R1+R2] **Diagnostic framework 泛化性严重不足**
- 2 个 threshold（concentration ≳0.50, t₁/t₅ ≲0.70）在 5 个数据点上 100% 准确分类。2 个自由参数完美拟合 5 个样本是经典 overfitting 信号。
- "Spread" 类别仅 1 个正样本（Qwen），positive class 的决策边界完全由单一数据点决定。
- 5 个模型全部 7–9B decoder-only，未覆盖 MHA/MLA/MoE attention 等不同设计范式。
- 论文自承 "Both thresholds are illustrative"（S5.2），但标题和 Contribution 3 的 framing 未反映此 caveat。
- **Action**: 增加 3–5 个不同范式模型验证 threshold，或将 claim 降级为 exploratory empirical observation。

**W2** [CRITICAL | consensus R1+R2] **4/5 模型缺失 unconstrained baseline**
- Table 2 中 Llama/Mistral/Yi/Gemma 的 unconstrained greedy/MCKP 列为 "---"。Compounding 是 Contribution 1 的核心——如果仅在 1 个模型上验证，无法判断是 Qwen idiosyncratic 还是 general phenomenon。
- Flat 模型（Mistral/Gemma, concentration 0.23–0.24）的 per-head 2-bit distortion 极低，unconstrained solver 可能不触发 catastrophic failure，这将挑战 compounding 论点的 generality。
- **Action**: 在所有 5 个模型上补跑 unconstrained greedy/MCKP。

**W3** [CRITICAL | consensus, R2 lower severity] **Downstream evaluation 仅限 Qwen**
- 0-shot downstream results（Table 5）仅覆盖 Qwen。对于声称 cross-architecture diagnostic framework 的论文，downstream 验证 1/5 模型不充分。
- R2 指出 negative-result 模型 PPL 差异极小（<0.03），downstream 差异不可能显著——但未验证即未确认。
- **Action**: 至少在 Llama 和 Yi-1.5 上补充 downstream evaluation。

**W4** [CRITICAL | consensus R1+R2] **Qwen 可能是架构 outlier，practical value 存疑**
- Qwen uniform 4-bit degradation 异常高（+57.5%），其他模型仅 +2.9%–4.7%。方法仅在 degradation 异常大的 1 个模型上有效，这可能说明 Qwen 是 outlier 而非方法普遍有效的证据。
- **Action**: 分析 Qwen 为何异常（GQA ratio? tokenizer? pre-training recipe?），测试更多模型寻找 "Spread" 架构。

#### Should-Fix

**W5** [WARNING | divergence] **Novelty 讨论**
- R2 认为 cardinality constraint 是标准 knapsack 技术的直接应用（HAWQ/HAQ 先驱），algorithmic novelty 不足。
- R1 反驳：ARR H6 heuristic 警告不应因方法简单 reject；核心 novelty 在 compounding diagnosis 而非 solution；solution simplicity 是 feature。
- **Director 判断**: 两方均有道理。Compounding diagnosis 确实是 genuine contribution，但论文可通过 formalize compounding 为 super-additive distortion model 来增强 technical depth。

**W6** [WARNING | divergence] **Profiling 方法与 compounding 论点的关系**
- R1 指出 single-head isolation profiling 与 non-additive compounding 之间存在逻辑张力。
- R2 反驳：论文利用这一不一致来解释失败并设计修复——constraint 将问题压回 near-additive regime，per-layer oracle（gap < 0.02 PPL）验证了这一点。
- **Director 判断**: R2 的反驳有说服力。这不是逻辑矛盾而是 constraint 的 motivation。但论文应 explicitly 阐述 "constraint 如何将 problem 压回 additive regime"，当前推理散落在 S3.3–3.4 中。

**W7** [WARNING | consensus] **Related work 遗漏**
- 缺 HAWQ (ICCV'19)、HAWQ-V2 (NeurIPS'20)、HAQ (CVPR'19) 作为 mixed-precision bit allocation 先驱。
- 缺 2025 published KV cache 工作：PM-KVQ、Kitty、RotateKV (IJCAI'25)、MiniKV (ACL Findings'25)、AQUA-KV (ICML'25)。
- 与 RateQuant 差异化不够 explicit。
- **Action**: 补充以上引用，明确与 RateQuant 的区别。

**W8** [WARNING | consensus] **Solver equivalence 缺乏形式化**
- "Constraint narrows feasible set enough that greedy = MCKP" 是 informal 解释。需要 formal sufficient condition 或明确标注为 empirical observation。

**W9** [WARNING | consensus] **"Non-additive" 未形式化定义**
- Section 3.3 使用 "non-additively"、"super-linearly" 但未给出 formal characterization。给出 approximate functional form（即使是 empirical fit）会增强 technical contribution。

**W10** [WARNING | consensus] **Standard vs hires profiling 混用**
- Standard profiling 检测 37/112 non-zero heads，hires 检测 100/112（2.7× 差异）。Headline result 用 standard（11.23），hires 更优（10.91）。应统一或明确推荐 setting。

**W11** [WARNING | consensus] **缺少 per-head vs token-level granularity tradeoff 讨论**

---

### Reviewer Consensus

以下问题两位 Reviewer 达成共识：
- [AGREE] Diagnostic framework 在 5 个模型上 overfitting，需要更多模型验证（W1）
- [AGREE] 缺失 unconstrained baselines 是 critical gap（W2）
- [AGREE] Related work 需补充 HAWQ/HAQ 和 2025 KV cache 工作（W7）
- [AGREE] Solver equivalence 需形式化或明确标注为 empirical（W8）
- [AGREE] "Non-additive" 需形式化定义（W9）
- [AGREE] Negative results 的诚实报告是论文亮点（S3）
- [AGREE] Compounding analysis 有 genuine value（S1）
- [AGREE] 写作清晰、逻辑连贯（S6）

### Reviewer Divergence

**分歧 1: Novelty 是否充分**（W5）
- R2: Cardinality constraint 是标准技术，novelty 不足，应升为 critical
- R1: ARR H6 警告不因方法简单 reject，核心 novelty 在 compounding diagnosis

**分歧 2: Profiling-compounding 关系**（W6）
- R1: Single-head profiling 与 non-additive claim 存在逻辑矛盾
- R2: 非矛盾而是 constraint 的 motivation，per-layer oracle 验证了 constrained regime 下的 near-additivity

**分歧 3: Framing 是否偏乐观**
- R2: Abstract 前半段突出 Qwen 27.3%，但 4/5 无收益
- R1: Abstract 后半段已充分覆盖 negative results，标题 "When Does...Help?" 本身暗示 "not always"

---

### Questions for Authors

1. 为什么没有在所有 5 个模型上运行 unconstrained baselines？这些实验的计算成本是多少？
2. Qwen 的 uniform 4-bit degradation（+57.5%）为何远高于其他模型（+2.9%–4.7%）？是 GQA ratio、tokenizer 还是 pre-training recipe 导致？
3. Diagnostic 的 borderline cases（concentration ≈ 0.55, t₁/t₅ ≈ 0.65）如何处理？是否有 graceful degradation？
4. Constraint 如何将 problem 从 non-additive regime 压回 near-additive regime？能否 formally characterize 这一 transition？
5. 方法是否依赖 round-to-nearest quantization？对 GPTQ/AWQ 等 data-dependent quantization 方法是否适用？
6. RateQuant 在 {2,4,8,16} bit-widths 上是否也产生 catastrophic failure？

---

### Missing References

**Weight-level mixed-precision 先驱（positioning 需要）：**
- HAWQ (Dong et al., ICCV 2019)
- HAWQ-V2 (Dong et al., NeurIPS 2020)
- HAQ (Wang et al., CVPR 2019)

**2025-2026 KV cache 工作（completeness 需要）：**
- PM-KVQ (arXiv 2025)
- Kitty (arXiv 2025)
- RotateKV (IJCAI 2025)
- MiniKV (ACL Findings 2025)
- AQUA-KV (ICML 2025)
- "Don't Waste Bits!" (arXiv 2026)

---

### External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

### Overall Assessment

**Overall Score: Weak Reject (2.25/5)**
- R1: 2.5/5 (Borderline) | Confidence 4/5
- R2: 2/5 (Resubmit next cycle) | Confidence 4/5

**Rationale**:

论文的核心发现——2-bit distortion compounding 在 hardware-aligned bit-widths 上导致 unconstrained solver catastrophic failure——是 genuine 且有实践价值的贡献。Cardinality constraint 作为 minimal fix 是 elegant 的，negative results 的诚实完整报告体现了科学严谨性。

然而，论文存在以下系统性缺口使其在当前状态下不适合 EMNLP main conference：
1. **Diagnostic framework 的泛化性无法验证**：2 个 threshold 在 5 个同质模型上完美拟合（仅 1 个正样本），这不足以支撑 "framework" 的 claim。
2. **Compounding 的 generality 未验证**：4/5 模型缺失 unconstrained baselines，无法确认 compounding 是 general phenomenon。
3. **方法的 practical scope 极窄**：仅 Qwen（一个 degradation 异常高的 outlier）获益，且 Qwen 为何异常未被分析。
4. **评估覆盖不完整**：downstream evaluation 仅 Qwen，related work 遗漏重要先驱。

**建议路径**：
- 补充 unconstrained baselines（W2）和 downstream evaluation（W3）后，可考虑作为 **Findings** paper 提交——compounding warning + negative results + diagnostic observation 的组合在 Findings track 有价值。
- 若要冲 main conference，需扩展到 10+ 模型验证 diagnostic threshold，并 formalize compounding（W9）和 solver equivalence（W8）。

---

### Detailed Comments

**Section 3.2 (Profiling)**: 明确 single-head profiling 的 assumption（additive approximation）和 validity range（k small）。当前表述在 S3.2 L27–29 中承认 additive assumption 但未明确 constraint 如何恢复 validity。

**Section 3.5 (Solver Equivalence)**: L111 "narrows the feasible set enough" 需要 formal statement。例如：在什么条件下（k/H ratio, bitwidth gap size），constrained greedy 保证等于 constrained MCKP？

**Section 5.2 (Diagnostic)**: 考虑将 framework 重新定位为 "empirical taxonomy" 或 "preliminary diagnostic heuristic"，与证据强度匹配。Thresholds 可改为 "suggested ranges" 而非 fixed values。

**Table 2**: 补充所有 5 个模型的 unconstrained results。即使 Flat 模型不触发 catastrophic failure，这本身也是 informative（说明 compounding 需要 sufficient heterogeneity）。

**Abstract**: 前半段过度强调 Qwen 27.3% improvement。建议开篇即点明 "non-uniform allocation helps only when head sensitivity exhibits a specific distribution shape"，将 "when does it NOT help" 提到更突出位置。

**References**: 补充 HAWQ/HAQ 系列和 2025 KV cache 工作，增加与 RateQuant 的 explicit differentiation paragraph。