---
round: 22
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T00:51:46.780584+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 25 审稿报告（Fresh Review）

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**目标 Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026)
**截止日期**: 2026-05-25
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）
**轮次**: 1 轮（交叉分享后关键问题达成共识，无需第 2 轮）

---

## Summary

本文提出用前向 KL 散度替代 BCE 训练 SwiGLU LLM 的轻量级稀疏性预测器（<1% base 参数）。核心 insight 是 KL 将所有 mask 决策通过输出分布耦合，发现的 mask patterns 与 magnitude-based 方法分歧 46-68%，但产生显著更优的 PPL（LLaMA-3.1-8B 30% sparsity 下减少 14.5%）。C1 target-swap ablation 将 KL 优势解耦为 signal type（output-distribution vs intermediate loss）和 coupling scope，发现 signal type 在 30% 下主导 PPL 差距（upper bound）。跨架构评估（Mistral-7B, Qwen-14B）确认 PPL 泛化但知识密集型任务系统性退化。论文自定位为 empirical study；无 wall-clock speedup（+6.4% overhead）。

---

## Strengths

**S1** [两位 reviewer 共识] **C1 target-swap ablation 设计巧妙**：将 KL 发现的 mask targets 转移给 BCE 训练，干净地分离了 "what"（mask pattern quality）和 "how"（gradient coupling mechanism）的贡献。max Δ≤0.79pp（50% s42）证明 KL 发现的 mask 模式是质量优势的主要来源。这是论文最有洞察力的实验。

**S2** [两位 reviewer 共识] **实验控制质量高**：KL / BCE / MSE 使用完全相同的 architecture（2-layer MLP, d_b=128）、data（WikiText-103）、optimizer（AdamW）、steps（1000），仅改变 loss function。3-seed 评估用于主要结果，PPL 标准差极低（±0.02）。这种 controlled comparison 在 empirical ML 论文中并不常见。

**S3** [两位 reviewer 共识] **诚实且全面的 limitations 披露**：明确承认无 wall-clock speedup、knowledge-task regression、training data homogeneity、evaluation bounds。Abstract 使用更保守的 14.5%（matched sparsity）而非 18.6%（nominal）。Claims 有适当 hedging（"upper bound"、"suggests"、"primarily empirical"）。

**S4** **丰富的 appendix**（~18 个 display items）：从 bottleneck sensitivity 到 temperature schedule 到 training convergence 到 cross-seed mask consistency 到 OOD evaluation，覆盖了大部分可预见的 reviewer 问题。

**S5** **Compensation redundancy finding**：发现 KL predictor 使得额外的 67.2M 参数补偿网络冗余，简化推理管线——实用且有信息量。

**S6** **2D taxonomy**（Table 1）提供了有用的组织框架：correction granularity × training signal coupling，帮助定位论文贡献和 prior work。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1** [critical, 两位 reviewer 共识] **Coupling decomposition 在 50% sparsity 下失效且存在 allocation confound**

- **K=4 at 50% 反常**：K=4 per-layer KL PPL=44.23 **劣于** K=1 的 34.85，而 E2E KL 为 11.84。如果增加 masked layers（K=1→K=4）应缩小与 E2E 差距，但实际差距从 +23.06 扩大到 +32.44。论文的 "gradient interference" 解释（§4.5）是 speculation，无实验证据。
- **MMLU allocation confound**：K=4 在 MMLU 上系统性超过 E2E（42.7±1.4 vs 40.7±1.3，3 个 seed 均是），因为 K=4 产生 near-uniform allocation（std=0.003）匹配了 uniform inference protocol，而 E2E 产生非均匀分配（L14-L18 valley）。因此 decomposition 的两个维度不正交，无法独立归因 coupling vs allocation 效应。
- **General claims 超出 evidence 范围**：Abstract（"Signal type accounts for the majority of the PPL gap"）和 Conclusion 基于 30% 结果做 general claim，但 decomposition 在 50% 下不成立。
- **建议**：(1) Abstract/Conclusion 限定为 "at moderate sparsity (30%)"；(2) 正文 §4.5 显著讨论 allocation confound；(3) 补充 K=2/K=8 实验追踪趋势，或明确放弃 50% 下的 decomposition 分析。

**C2** [critical, 两位 reviewer 共识] **知识密集型任务系统性退化仅有假设无控制实验**

- 跨所有规模一致退化：8B MMLU -5.2pp，Mistral GSM8K -7.3pp，Qwen-14B GSM8K -20pp, MMLU -8.1pp。
- §4.2 提出两个假设（WikiText-103 数据偏差 + forward KL mode-covering 稀释 rare activations），但明确说 "await validation via knowledge-neuron probing"——没有做任何验证实验。
- Appendix T 的 constraint analysis 已显示 remove-valley → MMLU +3.4pp, GSM8K +1.6pp，暗示 regression 部分源于 learned allocation 而非 loss function 本身，但此关键发现仅在 appendix 中。
- **建议**：(1) 至少一个控制实验：C4/RedPajama 训练 predictor 测试数据偏差假设，或比较 KL vs magnitude 在 knowledge-critical layers 的 neuron retention 差异；(2) Appendix T 发现提升到正文。

**C3** [warning→critical by consensus] **方法新颖性边界需更清晰论证**

- 核心组件（KL distillation + Gumbel-Sigmoid + predictor arch）均为成熟技术。MaskLLM 已用 KL + Gumbel-Softmax 训练可学习 mask。论文的三点区分合理但更多来自应用场景不同。
- **R1 nuance**：contextual vs static 确为不同优化问题（predictor 需泛化到未见输入），且论文已自定位为 "primarily an empirical study"。C1 ablation 和 per-layer decomposition 的**实验设计**本身有新颖性。
- **共识建议**：(1) Introduction 更早承认组件层面非新颖性；(2) Contribution list 重排：C1 ablation + decomposition 置于首位（当前第一条是 "ranking across five losses"，信息量不如 C1 + decomposition）。

### Should-Fix（影响评分但不一票否决）

**W1** [两位 reviewer 共识] **C1 ablation s42 oracle provenance 问题**：s42 oracle 来自 earlier checkpoint（PPL gap 0.65pp at 30%），而 s123/s456 matched oracle gap ≤0.03pp。s42 是 Table 3 第一行且唯一有 50% 数据的 seed。建议为 s42 补训 matched oracle，或优先展示 s123/s456，并补充 s123/s456 在 50% 的 C1 结果。

**W2** [两位 reviewer 共识] **BCE 30% 缺少 uniform allocation 对比**：Table 2 中 BCE 30% 仅有 global（†），KL 有 global+uniform。无法在相同 allocation strategy 下直接比较。建议补充 BCE 30% uniform 或解释缺失原因。

**W3** [两位 reviewer 共识] **MSE 50% single-seed caveat 不充分**：seed 123 catastrophic failure（PPL=15,789），Table 4 的 229.26 仅 seed 42。正文 §3.7 使用 MSE 50% 数据论证 taxonomy 但未注明 single-seed。MSE 30% 3-seed（18.52±1.68）结论稳健。建议正文标注 caveat。

**W4** [两位 reviewer 共识] **无 wall-clock speedup，+6.4% latency overhead**：论文诚实披露（appreciated），但对 sparsity 领域论文实用影响受限。论文 framing 已充分（"primarily an empirical study"），结构性限制。

**W5** **Qwen-14B GSM8K 高方差**：uniform 3-seed 32.0±5.2（CV=16.3%），95% CI 约 ±10pp。建议正文引用完整 32.0±5.2 vs 52.1 而非仅 "-20pp"。

**W6** **Limitations 未讨论 14B regression 对更大规模的影响**：8B→14B regression 加剧（GSM8K -1.3pp→-20pp），但 Limitations 未讨论 70B+ 前景。

### Minor Issues

**M1** §4.1/Introduction "19%" 实际为 18.6%（(10.82-8.81)/10.82=18.58%）。Figure 2 caption 使用 14.5%（matched sparsity）而 §4.1 使用 19%（nominal），基准不一致。

**M2** 术语不一致："output-distribution alignment"/"distillation"/"objective" 交替使用，建议统一。

**M3** Eq. 4 s_j 和 m̃_j 缺少层标 ℓ 上标，与 §3.1 notation 不一致。

**M4** §3.4 T（distillation temperature）与 §3.3 τ（Gumbel temperature）使用不同符号但未明确区分，可能造成困惑。

**M5** Table 4 STE 30% 仅达 20.8% actual sparsity（‡），与其他方法在不同实际 sparsity 下对比，公平性有限。

---

## Reviewer Consensus

两位 reviewer 评分一致（Overall 3.5, Soundness 3.5, Excitement 3, Confidence 4），在以下核心评估上达成共识：

| 问题 | 共识状态 |
|------|----------|
| C1: Coupling decomposition 在 50% 失效 + allocation confound | [AGREE] 两位均列为 Critical |
| C2: Knowledge regression 缺机制分析 | [AGREE] R1 W1 + R2 N1，两位均认为最高优先级 |
| C3: 方法新颖性边界 | [AGREE with nuance] R2 Critical, R1 部分同意但指出实验设计新颖性 |
| W1: C1 s42 oracle provenance | [AGREE] 两位均指出 |
| W2: BCE 30% 缺 uniform | [AGREE] 两位均指出 |
| W4: 无 wall-clock speedup | [AGREE] 结构性限制，framing 已充分 |
| S1-S3: C1 ablation 巧妙 + 实验控制 + 诚实 limitations | [AGREE] 两位共同认可的主要优势 |

---

## Reviewer Divergence

| 分歧点 | R1 立场 | R2 立场 | 解决 |
|--------|---------|---------|------|
| 缺少 MT-Bench/AlpacaEval | [REBUT] Base model 不适用 instruction-following benchmarks | [Should-Fix] 缺少生成评估 | **R1 rebuttal 有效**：论文评估 base model，MT-Bench 需 instruction-tuned。Limitations 已覆盖。不计入最终 weakness |
| Conclusion 过于简洁 | [REBUT] 简洁但完整，ARR 无格式要求 | Minor issue | **R1 rebuttal 有效**：Conclusion 覆盖了核心发现、key result、limitations、code release |
| GPU 型号 double-blind 风险 | [REBUT] 商用 GPU，不构成 de-anonymization | Minor concern | **R1 rebuttal 有效**：RTX PRO 6000 是 2025 年商用 GPU，不比 A100 更具识别性 |
| Qwen-14B 单 seed vs 多 seed | [Critical] 单 seed 不足 | [Partial REBUT] 实为 3-seed 但高方差 | **R2 factual correction 有效**：GSM8K uniform 是 3-seed (32.0±5.2)，非单 seed。降级为 Warning（高方差限制统计力）|
| Sparsity controller 30% 饱和 | [Should-Fix] λ=5000 cap, 28.5% | [Partial REBUT] Appendix C matched-sparsity 对比充分 | **R2 rebut 部分有效**：matched comparison 已提供，但建议在正文中讨论 deviation |

---

## Questions

1. K=4 at 50% 为什么比 K=1 差？是否有 K=2/K=8 数据追踪 PPL vs K 趋势？
2. 如果在 K=4 实验中强制使用 E2E KL 的 per-layer allocation（而非 K=4 自然学出的 near-uniform），MMLU anomaly 是否消失？
3. 是否尝试过在 math-heavy 数据（如 GSM8K 训练集或 math subset of C4）上训练 predictor 来检验 knowledge regression 是否源于数据偏差？
4. BCE 30% 为什么缺少 uniform allocation 数据？是否存在 BCE uniform 表现更差的情况？
5. Appendix T 的 remove-valley 实验中，是否存在同时改善 MMLU 和 ARC-c 的 per-layer allocation 配置？

---

## Missing References

论文 Related Work 覆盖面相当完善（50+ 引用），两位 reviewer 未发现重大遗漏。建议检查：
- 2026 年 1-5 月是否有新的 KL distillation for activation sparsity 工作
- TurboSparse 系列后续工作的更新引用

Missing references 不构成接收障碍。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用。

---

## Visual Layout Check（非评分项）

状态：**已完成**（耗时 4 分 20 秒）

**统计**：0 critical, 3 warning, 17 info

**Warnings**:
1. **Page 3-4 连续 2 页无 figure/table**：Related Work → Method 过渡，可考虑将 Table 1 前移至 p4
2. **Page 13（附录）极高密度**：Table 7 + 8 + 9 + Figure 3 + Table 10 + 3 subsections 挤入单页，阅读体验欠佳
3. **Page 17（附录）底部拥挤**：Table 15 + Figure 7 + Table 16-17 密集堆叠

**Info highlights**:
- 主体正文恰好 8 页，符合 ACL 要求
- 全文 6 个 display items（2 Figure + 4 Table），密度 0.75/页，适中
- 未见 margin overflow、公式渲染错误、[?] 未解析引用
- References 格式统一（ACL natbib），无异常
- Figure 1 在 p2（可提升到 p1 底部以增强首页视觉锚定）

---

## Overall Assessment

**评分：3.5 (Borderline Conference)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3 | 3 | 3 |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4 | 4 | 4 |
| Reproducibility | 4 | 4 | 4 |

**核心判断**：这是一篇实验设计严谨、分析有深度的 empirical study。C1 target-swap ablation 和 signal type/coupling scope decomposition 是有价值的分析贡献，5 种 loss 的 controlled comparison 在同类工作中罕见。

**阻碍 Conference 的三个核心问题**：
1. **Coupling decomposition 在 50% 失效且有 allocation confound**——论文的主要分析贡献之一的 generality 受限
2. **Knowledge regression 仅假设无验证**——论文最大负面结果（跨规模 MMLU/GSM8K 退化）缺乏任何机制分析实验
3. **方法组件层面新颖性有限**——KL+Gumbel 应用于新场景，但论文已通过 empirical study 定位和 C1/decomposition 分析贡献部分弥补

**如何提升至 Conference (4.0)**：
- 修复 C1（限定 decomposition scope + 讨论 allocation confound）和 C2（至少一个控制实验验证 regression 假设）可能足以跨过 borderline
- C3（novelty framing）通过 contribution list 重排和更早承认组件非新颖性可以改善

**Findings (3.0) 下限条件**：若 C1 和 C2 不修复，论文仍有足够的实验质量和 C1 ablation insight 支撑 Findings 级别接收。

---

## Detailed Comments

### Abstract
- 9 句 abstract 信息密度偏高。可考虑将 C1 和 decomposition 细节移至正文，压缩至 6-7 句。
- "Signal type accounts for the majority" 需加 "at 30% sparsity" 限定。

### Introduction (§1)
- 逻辑流清晰（problem → gap → approach → results），但 contribution list 排序可优化：C1 ablation 和 decomposition 应置于首位。
- "reducing TEAL's perplexity by 19%" → 18.6% 或 ~19%。
- MaskLLM 区分（¶7）位置合理，但组件非新颖性应更早承认。

### Related Work (§2)
- 覆盖全面（50+ 引用），结构合理。MaskLLM 三点区分有说服力。
- 无重大遗漏。

### Method (§3)
- KL 公式正确，Gumbel-Sigmoid 推导标准。
- Geometric Penalty Schedule 是合理的替代 Lagrangian multiplier 的方案。
- §3.6 梯度分析：BCE vs KL 对比公正，"suggestive; empirical evidence in §4.3" 的 hedging 恰当。
- Eq. 4 缺少层标 ℓ。
- T vs τ 可加一句区分说明。

### Experiments (§4)
- §4.1 Main results：PPL 结论可靠（σ=0.02），downstream 差异为 directional evidence（论文已注明）。
- §4.3 C1 ablation：设计巧妙，s123/s456 matched oracle 结果 convincing。s42 provenance 问题需修复。
- §4.5 Per-layer KL decomposition：30% 分析有价值，50% 失效需明确标注。Allocation confound 需在正文讨论。
- §4.6 Cross-arch：PPL 泛化 convincing，downstream regression 需更完整统计报告。

### Conclusion (§5)
- 简洁完整。"primary design dimension" 需限定适用范围。

### Limitations
- 覆盖 5 个要点（sparsity sweet spot, knowledge regression, training data, batched inference/seq length, generation tasks），充分。
- 建议补充 14B regression 加剧对 70B+ 的影响讨论。

### Formatting
- 正文 8 页，符合 ACL 8 页限制 ✓
- Double-blind：未见 de-anonymizing 信息 ✓
- ACL 模板 (acl.sty, [review] option) ✓
- References 格式统一 ✓
- 代码释放声明：Conclusion 末尾 "Code and trained predictors will be released upon acceptance" ✓