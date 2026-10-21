---
round: 3
overall_score: weak reject
timestamp: 2026-05-17T18:21:34.475593+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Vision Encodes, Language Routes — Token-Level Functional Specialization in a Vision-Language-Action Model

**目标 Venue**: CoRL 2026 | **截止日期**: Paper 2026-05-28 EOD
**审稿轮次**: Round 4（B 版本全新审稿）
**Reviewer 配置**: 2 人（R1 方法/实验严谨性，R2 新颖性/影响力 + 写作/格式）

---

## Summary

本文对 OpenVLA-7B 在 LIBERO 上进行 token 级别表征分析，通过 cross-instruction probes、attention 分析、RSA 和 MLP probes 四种方法，比较 trained/pretrained/untrained 三个条件。主要 claims：(1) image tokens 不编码 instruction 信息（instruction-blind），readout token 是唯一的多模态汇聚点；(2) VLA fine-tuning 将 instruction routing 从中层转移到 entry-exit 模式；(3) LLM 对 vision encoder 输出进行非单调变换（inverted-U RSA profile）。

---

## Strengths

- **S1 [全票]**: 系统化的 2×2 factorial design（trained/untrained × instruction presence）+ 三条件对比（trained/pretrained/untrained）有效 disentangle 各因素贡献，是分析 VLA 的优秀实验范式
- **S2 [全票]**: 四种互补分析方法（probe + attention + RSA + MLP）从不同角度验证同一问题；CKA 作为 supplementary metric 在 appendix 诚实报告，包括与 RSA 的矛盾
- **S3 [全票]**: 充分的 robustness analysis（distance metric invariance, per-DOF, permutation test, seed sensitivity, demo subsampling, cross-benchmark validation on LIBERO-Spatial）
- **S4 [R1]**: 诚实报告 negative/null results（RSA best-vs-best Δ=+0.017, CI includes 0 标为 n.s.；CKA ordering 矛盾正面讨论）
- **S5 [R2]**: 写作质量良好，无 AI 写作痕迹，叙事连贯
- **S6 [R2]**: L1 attention ablation 提供了少有的 interventional evidence（尽管数据规模存在问题）

---

## Weaknesses

### Must-Fix（3 个 critical，全票共识）

**N1 [critical, 全票共识] C1 不构成 empirical finding — causal mask 的数学必然 + probe 任务 trivially easy**

OpenVLA 的 token 序列为 [image] → [instruction] → [readout/action]。Causal attention mask 下，位置 i 的表征仅依赖位置 ≤ i。Image tokens 先于 instruction tokens，因此 image tokens 在任何层都无法 attend to instruction tokens。这是架构决定的数学性质，非 empirical finding。此外，frozen vision encoder 不接收 instruction input，instruction invariance 同样 trivially expected。

Readout token 侧同样有问题：10-way classification over 10 distinct instruction strings 对任何能 attend to instruction tokens 的位置都是 trivial 的。论文自己承认 "even incidental attention (~12%) suffices for linear classification at L1"（Appendix D.1）。Untrained model（随机权重）在 L1 也达到 100%（Table 1），进一步证实 trivial nature。100% 准确率反映 instruction embeddings 的线性可分性（tokenizer 的性质），非 "multimodal convergence" 的证据。

C1 是论文三大贡献之首、标题的核心基础。Discussion 仅一句话承认 "C1 likely generalizes via the causal mask"，远远不够。如果 C1 的两侧（image-blind + readout-hub）都是 trivial，论文的核心叙事需要根本性重构。

R1 视角（probe difficulty）和 R2 视角（causal mask）互补，交叉回应中 R1 完全同意 R2 的 causal mask argument 更根本。

**N2 [critical, 全票共识] RSA inverted-U 效应量极小且 metric-dependent，CKA 完全反转核心结论**

(a) Rise phase 极小：Trained image_mean RSA 从 L0 (0.612) 到 L12 (0.628) 升幅仅 Δρ=0.016（2.6%），L0→L12 的 CI 未报告。Best-vs-best training effect (+0.017) 的 CI 包含 0（n.s.）。

(b) Metric-dependent：Appendix B.2 显示 linear CKA 完全反转 RSA ordering（untrained > trained > DINOv2），per-layer profile 呈单调递增（无 inverted-U）。RDM kernel CKA 中 DINOv2 排名最低（0.241），而 RSA 中 DINOv2 排名最高（0.692）——完全反转。

(c) 核心 claims 受影响："non-monotonic refinement of vision encoder output" 仅在 RSA 下成立；"DINOv2 provides the highest geometric foundation" 在 CKA 下不成立；"vision encoder quality emerges as a key design lever" 是 metric-contingent claim。

Method §3.5 的 RSA preference justification（"CKA sensitive to kernel choice"）不充分——RSA 同样 sensitive to distance function choice（representation 用 cosine、action 用 Euclidean）。仅验证了 action distance 的 metric invariance（Appendix C.6.1），未验证 representation distance 的选择。

**N3 [critical, 全票共识] L1 attention ablation 使用 5 demos，因果推断可靠性不足**

Ablation 使用 5 demos per task（~50-500 total datapoints），而主实验 Table 3 使用 50 demos per task。R² baseline 从 ~0.65 降到 0.256，表明 probe 严重 underfitting。在此 regime 下：
- Zeroing attention 可能通过 reduced effective dimensionality 起到 regularization effect（fewer attended positions → lower variance → better generalization for small N）
- 这是论文中唯一的 causal intervention；如果不可靠，全文仅有 correlational evidence
- 缺少 random ablation control（随机 zero 同等数量的 non-instruction-dominant heads）
- R2 补充：L8/L13 null result 不能排除 L1-level confound（L8/L13 有独立 attention patterns）

---

### Should-Fix（7 个 warning）

**W1 [warning, 全票共识]** RSA best-vs-best training effect（Δ=+0.017, CI includes 0, n.s.）在 Abstract（L7 "modest geometric gain"）和 Introduction（L25）中未标注 n.s. 状态。读者须到 Appendix Table 8 才发现 CI includes 0，构成 selective reporting。

**W2 [warning, 全票共识]** 缺乏多重比较校正。32 层 × 3 条件 × 多 metric 的逐层比较无 FDR/Bonferroni 校正。至少对 key claims（inverted-U peak significance、per-layer training effects）应报告 adjusted p-values。

**W3 [warning, 全票共识]** Probe total N 从未明确报告。50 demos per task × 10 tasks = 500 demos，每 demo 多少 timesteps 未知。MLP probe（4096→256→7）有 ~1.05M 参数，N/params 比率影响 overfitting 风险评估。应报告 exact N 并讨论 capacity 控制。

**W4 [warning, 全票共识]** Frozen vision encoder 是 confound。"Vision encoder quality may matter more than LLM scale" 需要 across-encoder 实验（如 CLIP-only encoder 或 weaker DINOv2 variant）。当前仅在单一 frozen encoder 内分析，从 correlational observation 到 design recommendation 跳跃过大。

**W5 [warning, 全票共识]** 单模型（OpenVLA-7B）+ 单 benchmark family（LIBERO-Goal/Spatial，同一 simulator）。真正的 generalization evidence 需要不同 VLA architecture（RT-2, π₀）、不同 task domain（navigation, dexterous manipulation）、不同 backbone（non-Llama）。

**W6 [warning, R2 提出, R1 partially agree]** 缺少 Llama-2（Touvron et al., 2023）和 Open X-Embodiment（Padalkar et al., 2023）的直接引用。这两个是模型核心组件和训练数据的 primary sources。

**W7 [warning, R2 提出, R1 partially agree]** Introduction 第5行 "A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction" 在 causal mask 约束下接近 straw man——没有人会假设 causal mask 前的 image tokens 能编码后面的 instruction 信息。需重新措辞。

---

## Reviewer Consensus

以下为两位 Reviewer 达成共识的核心判断：

1. **[AGREE, 全票] C1 缺乏 empirical novelty**：R2 从 causal mask（数学必然），R1 从 probe difficulty（trivially easy），交叉回应后 R1 完全同意 R2 的论证更根本
2. **[AGREE, 全票] C3 的 inverted-U 是 metric-specific**：RSA 下成立，CKA 下消失或反转，"non-monotonic refinement" 不是 robust finding
3. **[AGREE, 全票] Ablation 数据规模问题**：5 demos 下 R² baseline 仅 0.256，因果推断受损
4. **[AGREE, 全票] C2（routing redistribution）是论文唯一有 genuine novelty 的贡献**：三条件 attention profile 的 mid-depth → entry-exit shift 是 genuine empirical finding，但 practical significance 未验证
5. **[AGREE, 全票] 实验框架（factorial design + multi-metric）具有方法论价值**

---

## Reviewer Divergence

仅一处小分歧，已在交叉回应中解决：

- **R2-M2（readout/last_preaction 术语）**：R2 认为交替使用未定义等价性，R1 反驳指出 Section 3.2(c) 已明确定义。R2 未在交叉回应中继续争论。结论：非问题。

---

## Questions to Authors

1. **Token ordering**：如果 image tokens 在 causal mask 中先于 instruction tokens，C1 的 image-token instruction-blindness 是否是 architecture-guaranteed 而非 empirical finding？如果是，论文如何重新定位 C1 的贡献？
2. **Probe difficulty**：是否考虑过更难的 probe 任务（如语义相近指令区分、fine-grained instruction attribute prediction）来验证 readout token 的 "multimodal convergence" 超越 trivial linear separability？
3. **RSA vs CKA**：Linear CKA per-layer profile 单调递增（Appendix B.2），DINOv2 在 RDM kernel CKA 中排名最低。请给出 principled argument 解释为何 RSA 应被优先信任，或 qualify C3 claims 为 metric-dependent。
4. **Ablation N**：5 demos per task 对应多少 total observation-action pairs？R² baseline 0.256 是否暗示 probe underfitting？是否可用 50 demos 重跑？
5. **RSA temporal autocorrelation**：同一 demo 内的多个 observation 是否引入 temporal autocorrelation？Bootstrap 是否 block by demo？
6. **Readout RSA profile**：Table 3 显示 readout RSA peak 在 L12 (0.643)，但 Figure 3 仅画 image_mean。Readout 是否也呈 inverted-U？

---

## Missing References

- Touvron et al. (2023) — Llama 2: Open Foundation and Fine-Tuned Chat Models（模型核心组件）
- Padalkar et al. (2023) — Open X-Embodiment（训练数据 primary source）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目配置中 external_review 未启用）。

---

## Overall Assessment

**Overall Score: Weak Reject**
**Confidence: High (4/5)**

论文的实验框架（factorial design + multi-metric analysis）具有方法论价值，写作质量高，robustness analysis 充分。但三个核心贡献中：

- **C1**（token-level specialization）：causal mask 的数学必然 + probe trivially easy → 不构成 meaningful empirical finding
- **C2**（front-loaded routing）：唯一有 genuine novelty 的贡献，三条件 attention profile 的 entry-exit vs mid-depth 对比是 real finding，但 practical significance 未验证
- **C3**（inverted-U refinement）：RSA-specific，CKA 下消失/反转，效应量极小（Δρ=0.016），不是 robust finding

仅凭 C2 一个 finding 不足以支撑 CoRL 2026 的投稿。L1 ablation 的 5-demo 数据规模问题进一步削弱因果推断力度。

**如果作者能在 rebuttal 中**：(1) 论证 token ordering 使 C1 non-trivial 或根本性重构 C1 定位；(2) 对 inverted-U rise phase 提供 CI 并 qualify metric-dependence；(3) 用 50 demos 重跑 ablation + random control，评分可能上调至 borderline accept。

---

## Detailed Comments

### Abstract
- L1-2: 清晰概括了方法
- L4-5: "strict token-level functional specialization: image tokens are instruction-blind" — 需要 qualify 这是 causal mask 的结构性约束
- L6: "self-supervised DINOv2 providing the highest geometric foundation" — 需加 "under RSA" qualifier（CKA 下不成立）
- L7: "modest geometric gain (Δ = 0.017)" — 未标注 n.s.

### Introduction
- L5: "untested assumption" 接近 straw man，需重新措辞
- L19-22: C2 的描述是论文最有价值的贡献，建议提升其在叙事中的权重
- L27: Contributions 列表中 (i) 应降权或重新定位

### Method
- §3.3: "linear classifier (10-way)" 与 §4.2 "both linear and MLP probes" 的关系需在方法中提前说明
- §3.5: "Why RSA over CKA" justification 需加强——当前论据可被对称地反驳

### Experiments
- §4.2 Table 1: Untrained L1=100% 的 interpretation 需要更多讨论（不仅是 "incidental"）
- §4.2 L76: 5-demo ablation 的方法细节（N, probe architecture, training procedure）应单独说明而非嵌入结果段落
- §4.3 Figure 3: 应增加 readout token 的 per-layer RSA 曲线
- §4.3: L0→L12 升幅的 bootstrap CI 需报告

### Discussion
- "C1 likely generalizes via the causal mask; C2 may be Llama-2-specific" — 这种无证据猜测不应出现，要么提供证据要么删除
- Limitations section 较简短，应扩展讨论 metric-dependence（RSA vs CKA divergence）

### Appendix
- B.2: CKA divergence 的讨论质量好，但应在正文有 pointer 和 qualification
- Table 9 vs Table 2 的 25/24 差异解释应集中在一处

### Format
- conclusion.tex 未被 main.tex \input
- references.bib 缺少 Llama-2 和 Open X-Embodiment
- 部分 R² 精度不统一（2位 vs 3位）
