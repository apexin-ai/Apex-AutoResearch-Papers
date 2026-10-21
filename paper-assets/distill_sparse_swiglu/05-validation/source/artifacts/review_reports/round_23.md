---
round: 23
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T01:45:59.381237+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

**目标 Venue**: EMNLP 2026 via ARR May 2026  
**审稿轮次**: Round 26 (Fresh Review)  
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验有效性; R2: 新颖性 + 完整性）  
**交叉分享**: 已完成，1 轮收敛  

---

## Summary

论文提出用 forward KL divergence 替代传统 BCE 训练 SwiGLU LLM 的上下文稀疏预测器（75.9M params, <1% base model），通过 Gumbel-Sigmoid relaxation 实现可微 mask 生成。在 LLaMA-3.1-8B 上 30% sparsity 下 PPL 降低 14.5%（matched sparsity），50% 下降 50%，跨架构（Mistral-7B、Qwen-2.5-14B）一致。论文同时贡献了 signal type vs coupling scope 的二维分解分析和 C1 target-swap ablation。自定位为 empirical study，不涉及推理加速。

---

## Strengths

1. **PPL 改善显著且跨架构一致**：14.5% at 30%, 50% at 50%, 82% at 70%，在 LLaMA/Mistral/Qwen 三架构上均成立。3-seed PPL 方差极低（σ=0.02, CV=0.2%），改进可信度高。[R1 S3, R2 S3, 共识]

2. **C1 Target-Swap Ablation 设计精巧**：将 KL-derived mask patterns 提取后用 BCE 重训练，在 30% (≤1.70pp gap) 和 50% (≤0.79pp gap) 均接近 KL 性能，有力证明 mask target quality 而非 gradient coupling 驱动推理质量。实验设计有新意且有信息量。[R1 S1, R2 S2, 共识]

3. **对局限性的诚实披露极为罕见**：Abstract 中即承认无加速，正文持续标注 "upper bound" / "confound" / "not fully orthogonal"，Limitations 坦承所有负面发现。这种透明度在投稿论文中极少见。[R1 S2, R2 S1, 共识]

4. **实验覆盖面广**：5 种 loss 排名、3 个架构（7B–14B）、6 个 sparsity levels（25%–70%）、2 种 allocation 策略、sensitivity sweeps（bottleneck/temperature/steps）、OOD 评估（C4）、cross-seed mask consistency 分析。附录约 11 页，极为充分。[R1 S4, R2 S1, 共识]

5. **Compensation 冗余性发现有实用价值**：证明 FastForward 风格 67.2M 补偿网络在 KL predictor 下完全冗余（Appendix J），推理开销从 +9.1% 降至 +6.4% 并节省 67.2M 参数。[R2 S4]

6. **2D Taxonomy (signal type × coupling scope) 提供有用分析框架**：即使分解不完美，该视角对理解稀疏预测方法空间有价值。[R1 S5, R2 S5]

7. **训练成本极低**：1000 步、单 GPU、~45 分钟，实用门槛非常低。[R1 S6]

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [Critical] Signal type vs coupling scope 分解在 50% 稀疏度下失效，但 Abstract/Conclusion 的 claim 限定不足**
- R1-N2, R2-N1, 完全共识
- 核心问题：(1) K=1 per-layer KL 同时改变 coupling 和 train-inference mismatch (训练 1/32 layers, 推理全部 32)，论文承认为 "upper bound" 但仍以较强措辞陈述；(2) K=4 在 50% 下 PPL=44.23 > K=1 的 34.85，论文自身承认分解 "unreliable under the current design"（§4.5 最后一段）；(3) K=4 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）暴露 allocation confound：K=4 near-uniform allocation (std=0.003) 等价于移除 protection valley（Appendix T: remove-valley → MMLU=44.0），signal type 与 coupling scope 并非正交。
- Abstract 已加 "(upper bound; not fully orthogonal with coupling scope)" qualifier，但 "accounts for the majority" 仍较强。Conclusion 标注 "upper bound" 但适用范围限定不够显著。
- 建议：(1) 将分解 claim 限定为 "at 30% moderate sparsity, subject to train-inference mismatch confound"；(2) 设计 stop-gradient 实验（detach downstream Jacobian 的跨层梯度，保留 output-distribution 目标但切断 coupling）作为更干净的 deconfounding；(3) 在 Abstract/Conclusion 中明确此分解不适用于 50%。

**C2. [Critical] 知识任务系统性退步缺乏机制分析，与 "primary design dimension" claim 矛盾**
- R1-N1, R2-N2, 完全共识
- 核心问题：KL 在所有规模和架构上 MMLU/GSM8K 低于 TEAL——8B: MMLU −5.2pp, GSM8K −1.3pp；Mistral: GSM8K −7.3pp；14B: GSM8K **−20.1pp** (σ=5.2pp)。退步跨 scale 恶化 15 倍（8B→14B GSM8K），不可归于噪声。
- §4.2 提出两个假设（训练数据同质性 + forward KL mode-covering 稀释 rare activations），仅 constraint experiment 部分验证第一个（remove valley → MMLU +3.4pp，解释约 65% 退步），第二个假设无任何实验支撑。
- Abstract 仅说 "commonsense gains but knowledge-intensive decline" 未量化幅度，有轻描淡写之嫌。"primary design dimension" claim 仅对 PPL 和 commonsense 成立，对知识任务 KL 是 inferior。
- 建议：(1) Abstract 量化退步幅度；(2) 将 "primary design dimension" 限定为 "for PPL and commonsense tasks at moderate sparsity"；(3) 做 mixed-domain training（WikiText + 数学/代码数据）或 knowledge neuron probe 验证机制假设。

### Should-Fix（影响评分但不一票否决）

**S1. [Warning] Downstream 统计力不足**
- R1-W1, R2 同意
- MMLU 30% global σ=9.5（95% CI ≈ ±23.5pp），ARC-c σ=3.6, Mistral ARC-c σ=6.4, Qwen GSM8K σ=5.2。PPL 作为 primary metric 完全可靠（σ=0.02），但 abstract/conclusion 中的下游 claims 统计基础薄弱。
- 建议：下游比较进一步弱化为 "directional trends"；考虑 paired t-test 或增加 seeds。

**S2. [Warning] Table 2 baseline 比较条件不统一**
- R1-W2, R2-M3, 共识
- BCE 30% 用 TEAL global (†)，KL 有 global + uniform；BCE 50% 用 2700 steps。横向比较需跳转 allocation 和 compute budget，读者负担重。
- 建议：增加 controlled comparison 子表或将 BCE 30% uniform (PPL=15.71, Table 4) 纳入正表。

**S3. [Warning] C1 ablation 的 soft-vs-hard confound 未解决**
- R1-W3, R2-W5, 共识
- C1 二值化 KL logits (>0) 同时改变 target source 和 mask representation。BCE+Gumbel (32.22) vs BCE (27.97) 使用 magnitude targets，不足以排除 confound。R1 补充：confound 影响的是 *why* transfer works，不影响 *whether* works（≤0.79pp gap 已建立 transferability）。
- 建议：增加 BCE+Gumbel on KL-derived targets 实验；正文加强 confound 讨论。

**S4. [Warning] MaskLLM 在 Taxonomy Table 1 中缺位**
- R2-W1, R1 同意
- Table 1 Static × Coupled 格仅列 SPON，MaskLLM (static N:M + KL) 也属此格。三点区分合理但无实验验证。
- R1 补充：setting 差异足够大，不需 Table 2 baseline 对比，Table 1 加注即可。

**S5. [Warning] 14.5% PPL improvement 引用基准不一致**
- R2-W2, R1 同意
- Abstract 用 matched-sparsity (8.81 vs 10.30, Appendix D)，Table 2 TEAL uniform 30%=10.82（改进 18.6%）。一级读者查 Table 2 找不到 10.30。
- 建议：在 Table 2 中增加 matched-sparsity 行，或在 caption 中标注来源。

**S6. [Warning] Qwen-14B 评估不完整**
- R1-W4, R2-M7, 共识
- 仅 30% sparsity，无 50% 结果，无 per-layer allocation 分析。GSM8K −20.1pp (σ=5.2pp) 的机制未分析（可能原因：d_ff=18944 vs LLaMA 14336 导致 d_b=128 压缩比更大；14B 数学能力更强被破坏量更大）。
- 建议：至少增加 50% PPL；讨论 14B 退化加剧的可能机制。

**S7. [Warning] 无实际推理加速**
- R1-N3 (critical), R2 REBUT → warning. Director 裁定：**降为 warning**
- 理由：(1) 论文自定位 empirical study，贡献在于理解训练目标对 mask quality 的影响；(2) compensation 冗余性发现减少推理开销从 +9.1% 到 +6.4% 并节省 67.2M 参数；(3) C1 证明 KL targets 可迁移到 BCE 有工程价值。
- R1 建议的 proof-of-concept sparse kernel 实验或与 LaRoSA 等方法在 mask quality 层面对比仍然有价值。

### Minor（不影响接收）

- **M1**: §3.4 中 forward KL vs RevKL 8.6%/6.4% 未标注 sparsity level（来自 50%，30% 差距小得多）[R2-M1, R1 同意]
- **M2**: 术语不一致——output-distribution alignment / KL distillation / coupled objective 交替使用 [R2-M2, R1 同意]
- **M3**: "stable downstream (MMLU 40.7±1.3%)" 指跨 seed 稳定性而非性能保持（vs dense 65.27%），措辞易误读 [R2-M4, R1 同意]
- **M4**: Introduction 中 68% divergence 和 32% Jaccard 同句出现，为互补度量易混淆 [R2-M6, R1 同意]
- **M5**: Eq. 5 求和方式正文未明确（附录才说 average over positions）[R1]
- **M6**: Figure 1 过于简略，未展示 Gumbel relaxation 和 Lagrangian controller [R1]
- **M7**: C1 s42 oracle 来自 earlier checkpoint（Table 3 † 标注不够显著）[R1, R2]
- **M8**: 页数合规性——Conclusion 可能溢出第 8 页 1-2 行 [R2-M5, R1 确认违规但可通过排版修复]

---

## Reviewer Consensus

以下问题两位 Reviewer **完全共识**（均标注 [AGREE]）：

1. **Signal type/coupling 分解的方法论可靠性**（C1）：50% 下失效，Abstract/Conclusion 的 claim 限定不足，K=4 MMLU 异常暴露 allocation confound，两维度不正交
2. **知识任务系统性退步**（C2）：机制分析不足，"primary design dimension" 对知识任务不成立，Abstract 未量化退步
3. **C1 soft-vs-hard confound**（S3）：BCE+Gumbel vs BCE 的控制用 magnitude targets 不足以排除 confound
4. **Table 2 baseline 不统一**（S2）：读者需跨 allocation 和 compute budget 跳转理解比较
5. **Qwen-14B 评估不完整**（S6）：GSM8K 退步 15 倍恶化缺乏机制分析
6. **所有 Minor 问题**（M1-M8）：均达成一致

## Reviewer Divergence

唯一分歧点：**无实际推理加速的严重程度**
- R1：定为 critical（N3）——稀疏预测方法不能加速，实用贡献存疑
- R2：REBUT，认为应降为 warning——论文自定位 empirical study，compensation 冗余性和 C1 target transfer 提供间接工程价值
- **Director 裁定**：采纳 R2 的 rebut，降为 warning（S7）。论文的核心贡献是分析性的，framing 已充分，但 R1 建议的 proof-of-concept 加速或与 LaRoSA 的 mask quality 对比仍有价值。

---

## Questions

1. 是否尝试过 mixed-domain 训练数据（WikiText + 数学/代码文本）？这是验证知识任务退化是否数据依赖的最直接实验。
2. 在 K=4 控制中强制使用 E2E 的非均匀 allocation（而非 K=4 自行收敛到 near-uniform），MMLU 异常是否消失？
3. Stop-gradient 实验（KL loss 反传时 detach downstream Jacobian 的跨层梯度）是否可行？这比 K=1/K=4 更干净地隔离 coupling scope。
4. L14-L18 protection valley pattern 在 Mistral 和 Qwen 上是否也出现？
5. Table 4 中 BCE+Gumbel+Penalty (38.02) 比无 penalty (32.22) 更差——为什么 sparsity penalty 让 BCE 恶化？
6. Qwen-2.5-14B 的 d_ff=18944 vs LLaMA 14336——predictor bottleneck d_b=128 是否应随 scale 调整？

---

## Missing References

1. **MaskLLM** (Fang et al., NeurIPS 2024): 已引用讨论但应在 Table 1 taxonomy 中体现位置（Static × Coupled 格）。[R1, R2 共识]
2. **ActTail** (arXiv:2603.12272, March 2026): 基于 HT-SR 理论的全局 activation sparsity allocation，与 per-layer allocation 分析相关。[R2 提出，R1 认为 2 个月前 arXiv 预印本不应作为 Should-Fix，降为 info]
3. **CATS** (Lee et al., 2024): §2 提到但 Table 2 未作为 baseline。[R1 提出]

---

## External Review (Stanford Agentic Reviewer)

未启用。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时 ~3.5 分钟）

### 发现摘要
- **Critical**: 0
- **Warning**: 1 — Page 6（§4.1-4.2 开头）整页纯文字，无任何 display item，位于 Table 1 和 Tables 2-3 之间，视觉节奏中断。建议调整 float 位置使 Table 2 提前。
- **Info**: 18 — 整体排版质量良好；Figure 1 架构图字号偏小但可读；Table 2 字号偏小但可读；Appendix page 17 密度最高但作为附录可接受；Figure 2 轴标签清晰且色盲友好；Section 5 heading 未孤悬；Limitations 简洁符合 EMNLP 要求。
- **页数合规**: 视觉审查 Agent 确认 Limitations/Ethics/References 在第 9 页开始，主文约 8 页。但 R2 指出 Conclusion 可能有 1-2 行溢出到第 9 页，需核实 LaTeX 编译结果。

---

## Overall Assessment

**评分**: 3.5 / 5 — Borderline Conference  
**置信度**: 4 / 5

### 评分理由

**会议门槛因素（积极）**：
- PPL 改善显著（14.5%–82%）、跨架构一致、3-seed 高置信度——这是一个 robust 的实证发现
- C1 target-swap ablation 是一个有创意且有信息量的实验设计
- 实验覆盖面在该方向上属于最全面之列
- 论文对局限性的主动披露体现了学术诚信
- Compensation 冗余性发现有实际工程价值

**会议门槛因素（消极）**：
- 核心分析贡献（signal type vs coupling scope 分解）在 50% 下完全失效，方法论可靠性不足以支撑 Abstract/Conclusion 中的 claim 强度
- 知识任务系统性退步（跨规模恶化 15 倍）与 "primary design dimension" 的强 claim 之间存在根本张力，机制分析停留在假设层面
- 方法新颖性有限——核心组件（KL、Gumbel-Sigmoid、MLP predictor）均为成熟技术，主要贡献是成熟组件在新场景的应用
- 无实际推理加速（+6.4% overhead），限制实用影响

### 改进路径

**达到 Conference（4.0）所需**：
1. 分解 claim 限定为 30% + 更干净的 deconfounding（stop-gradient 或更多 K 值）
2. Abstract/Conclusion 量化知识任务退步并限定 "primary design dimension" 适用范围
3. Mixed-domain training 验证数据偏差假设，或 knowledge neuron probe 验证 mode-covering 假设

**当前适合 Findings（3.0-3.5）**：
论文作为 empirical study 的价值在 Findings 层面是明确的——它是该方向首个系统性实证研究，实验可信度高，负面发现（知识退步、分解失效）本身也有信息量。核心 claim 的过度表述和分解实验的方法论问题是阻碍 Conference 的主要因素。

---

## Detailed Comments

### §1 Introduction
- Line 18: "This paper is primarily an empirical study" 定位准确，但应更早出现（当前在 contribution list 之后）
- "stable downstream (MMLU 40.7±1.3%)" 易误读——应改为 "low cross-seed variance"
- 68% divergence 和 32% Jaccard 同句出现为互补度量，建议统一

### §3 Method
- §3.4 "forward KL outperforms reverse KL by 8.6% and JSD by 6.4%"：来自 50%，应标注 sparsity level
- §3.6 Gradient analysis 提供良好直觉，SNR 分析结论自洽（KL SNR 更低但 mask 更好）
- §3.7 Taxonomy Table 1: Static × Coupled 应纳入 MaskLLM

### §4 Experiments
- §4.2 Knowledge-Task Regression 两个假设均为推测——至少需一个控制实验（mixed-domain 或 neuron probe）
- §4.4 C1 ablation 核心结论（mask patterns transfer）稳健；soft-vs-hard confound 影响 why 而非 whether
- §4.5 Per-layer KL decomposition 在 30% 可解释，50% 失效应更显著标注
- Table 2 条件不统一增加阅读负担
- Table 4 Forward KL vs JSD 在 30% 仅 0.09pp，divergence 选择在 moderate sparsity 下更接近 implementation detail

### §5 Conclusion
- 可能溢出第 8 页 1-2 行——需核实并修复

### Limitations
- 覆盖全面（sparsity sweet spot, knowledge regression, training data homogeneity, seq length, batched inference, generation evaluation）
- R26 新增建议：讨论 14B regression 加剧对 70B+ scalability 的影响（已包含）

### Appendix
- 约 11 页，覆盖极为充分
- Appendix P (Oracle Provenance): s42 oracle 来自 earlier checkpoint 应在正文 Table 3 更显著标注