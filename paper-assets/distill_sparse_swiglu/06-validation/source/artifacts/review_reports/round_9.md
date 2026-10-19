---
round: 9
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T01:57:56.585983+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 Consolidated Review Report (Fresh)

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 格式合规)
**审稿模式**: Fresh (无先前轮次记忆)

---

## Summary

论文提出用 KL 散度（替代标准 BCE）训练 SwiGLU LLM 的上下文稀疏性预测器，通过 Gumbel-Sigmoid relaxation 实现可微分 mask 优化。核心实证发现是 KL 训练的 mask 与 magnitude-based mask 有 68% 的差异，且因果消融（C1）表明 mask 目标质量（而非梯度耦合）驱动质量优势。在 LLaMA-3.1-8B 上，KL 在 30% 和 50% 稀疏度下 PPL 分别优于 TEAL 18% 和 49%，但 50% 下游任务全面崩溃至接近随机水平，14B 规模出现 MMLU 反转（-8.1pp vs TEAL）。

---

## Strengths

**S1. C1 因果消融设计精巧** [R1+R2 共识]
将 mask target quality 与 gradient coupling 解耦的实验设计值得肯定。BCE 在 KL-derived targets 上复现 KL 质量（50% max Δ=0.59pp），而 magnitude-based BCE 为 28.13±0.20，有力地表明 mask patterns 是主要驱动力。这是论文最有价值的贡献。

**S2. 全面系统的消融研究** [R1+R2 共识]
Ablation 覆盖 divergence direction（Forward KL > JSD +6.4% > Reverse KL +8.6%）、relaxation（Gumbel vs STE, 34.5%）、compensation redundancy、loss isolation、超参数鲁棒性（$d_b$, $\tau$, training steps），形成完整矩阵。Regime analysis（Table 5）的非单调 allocation 偏好提供实践指导。

**S3. 诚实的 Scope 界定** [R1+R2 共识]
Introduction 明确声明 "Our contribution is empirical" 和 "Wall-clock speedup requires sparse kernel support not addressed here"；14B MMLU gap、50% downstream collapse 均被报告。这种透明度值得赞赏。

**S4. 方法公式化简洁正确** [R1]
Gumbel-Sigmoid relaxation 是 Binary Concrete distribution 的正确应用；forward KL objective 推导无误；predictor 架构轻量（<1% base params）且不需推理时 compensation network。

**S5. 写作整体干净** [R2, R1 同意]
无 em-dash/en-dash AI 痕迹。术语首次出现时有定义。全文主线（mask pattern discovery → causal ablation → practical implications）连贯。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. C1 因果消融的声明力度与证据强度严重不匹配** [R1 Must-Fix, R2 升级同意]
- C1 是论文最核心贡献（Abstract/Intro/Conclusion 反复引用 "causal ablation confirms/proves"），但仅 2-seed 验证（50%: s42+s123; 30%: 仅 s42）。核心 claim 的统计验证反而弱于常规实验（主实验 3-seed）。
- 30% 条件下 C1 PPL gap（9.45 vs 8.82 = +7.1%）与 97.5% mask agreement 不相称，暗示 gradient coupling 在低稀疏度可能仍有残余贡献，与 "across the full sparsity range" 的声明矛盾。
- **R1 新发现的混淆变量**（R2 在交叉回应中确认）：KL predictor 训练时使用 soft Gumbel-Sigmoid masks（连续放松），C1 的 BCE predictor 使用 hard binary targets。C1 不仅改变了 gradient coupling，也改变了训练时的 mask 特性（soft vs hard），未完全 disentangle。
- **影响**：如果 C1 evidence 不充分，论文贡献降级为 "KL 比 BCE 好" 这个较 incremental 的发现。
- **建议**：增加到至少 5-seed；降级措辞为 "provides evidence" 而非 "proves"；讨论 30% gradient coupling 残余贡献；讨论 soft-vs-hard confound 作为 C1 设计局限。

**N2. 14B 规模 downstream 全面反转，削弱泛化声明** [R1 Must-Fix, R2 Must-Fix（W3→升级）]
- Qwen-2.5-14B 30%: KL PPL 最优（7.62 vs TEAL 8.73）但 MMLU 63.7% vs TEAL 71.8%（-8.1pp）、vs BCE 71.7%（-8.0pp）。ARC-c、GSM8K 上 KL 也均低于 BCE。Uniform allocation 同样趋势（64.49 vs 66.34）。
- BCE 使用 magnitude-based masks 在 14B 上 MMLU 正常（71.67%），问题特定于 KL 的 coupled training——直接质疑 "KL discovers superior mask patterns" 的核心叙事：在 14B 上 KL 的 mask patterns 对 MMLU 是 **有害** 的。
- Abstract "confirms the PPL advantage across 7-14B" 轻描淡写 downstream degradation。正文仅半句带过（§4.5），无任何机制解释。
- **建议**：正文（非仅 Appendix）充分讨论 14B reversal（至少一段）；提出可检验的机制假设；将 Abstract 改为明确表述 downstream reversal。

**N3. BCE baseline 在不同稀疏度使用不同实验管线，跨 sparsity 比较不可靠** [R1 Must-Fix, R2 交叉确认]
- 30% BCE（Table 1 $^\dagger$）：TEAL global allocation, no compensation, 2700 steps → PPL 11.25
- 50% BCE（Table 1 $^\ast$）：DejaVu pipeline + compensation (+67.2M params), no TEAL allocation → PPL 28.13±0.20
- **关键遗漏**：没有 "50% BCE + TEAL global (no compensation)" baseline——这才是与 50% KL global 最直接可比的设置。
- Table 4 "BCE + Compensation" PPL=25.44 vs "BCE (no comp)" PPL=27.97，差距 2.53，说明 compensation 对 BCE 有显著影响。但两者是否均使用 TEAL allocation 未明确标注。
- **影响**：Baseline 公平性是实验驱动论文的生命线。读者无法判断 KL 优势有多少来自 objective、多少来自 allocation strategy 差异。
- **建议**：增加 "50% BCE + TEAL global (no comp)" baseline；统一管线；Table 1 caption 更显著标注差异。

**N4. 实际可用操作区间极窄 + Abstract framing 偏向 50%** [R1 Must-Fix, R2 Must-Fix (N2+N3)]
- **50%**：MMLU 28.1±0.2%（≈random 25%），GSM8K <2.2%——论文自己确认 "capacity-limited regime"。KL 的 49% PPL 优势在 downstream 上完全无法体现。
- **30%**：KL uniform PPL 8.81 vs TEAL 10.97（18%）。但 downstream 差异很小——MMLU +2.1pp, ARC-c +1.4pp, GSM8K -0.4pp（TEAL 更好）。考虑 3-seed σ，多数差异不显著。
- **无实际加速**：当前实现增加 6.4% 延迟（126.78 vs 119.11 ms/forward）。即使 30% PPL 改进也没有对应的 wall-clock benefit。未验证 KL masks 是否兼容 N:M structured sparsity。
- Abstract 叙事高潮放在 "At 50%, the PPL advantage widens to 49%"，但 50% 是 downstream-dead zone。
- **建议**：将叙事重心转向 30% downstream-preserved quality；坦诚讨论 30% 的 modest downstream improvement；补充 N:M 兼容性讨论或初步实验。

**N5. 方法新颖性不足以支撑 Main Conference** [R2 Must-Fix, R1 同意实质但 REBUT 定级]
- 核心方法 = KL distillation (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + per-layer MLP predictor (DejaVu 2023)。每个组件均为成熟技术。
- MaskLLM (NeurIPS 2024) 已组合 frozen weights + learnable masks + KL + Gumbel relaxation。论文声称的三点区别（activation vs weight sparsity, predictor vs learnable params, global vs N:M）是应用场景切换，非方法论创新。
- Table 2 taxonomy 填充一个 "Per-token × Coupled" 空白格，学术贡献有限。
- **共识**：两位 Reviewer 均认为论文适合 Findings track。C1 empirical finding 有价值，但方法本身缺乏足够创新支撑 Main。R1 指出新颖性不可 "fix"，属于定位问题而非缺陷。

### Should-Fix（影响评分但不一票否决）

**W1. PPL degradation 措辞与计算方式不匹配** [R1]
- Abstract "KL reduces PPL degradation 18% over TEAL"：语义上应指缩小 dense-to-sparse gap（= 41%），实际计算是 relative PPL improvement (10.97-8.96)/10.97 = 18%。
- 建议统一为 "reduces PPL by 18% relative to TEAL"。

**W2. Mistral-7B 缺少全部 downstream 评估** [R1, R2 交叉确认]
- Table 8 (Appendix G) 仅报告 PPL。鉴于 14B 出现 PPL↑但 MMLU↓ 的反转，Mistral PPL-only 不能支撑跨架构泛化声明。
- 建议补充至少 MMLU 和 ARC-c。

**W3. Adaptive penalty Eq.5/6 形式化不一致** [R1, R2 交叉确认]
- Eq. 5 定义不等式约束 $\bar{s} \leq 1-\rho$，Eq. 6 使用绝对值 $|\bar{s}-(1-\rho)|$（等式约束）。实际上等式约束更合理，但推导应保持一致。
- 30% target actual sparsity 28.5%（5% deviation），interpolated TEAL baseline 未实际测量。

**W4. 训练数据消融缺失** [R1+R2 共识]
- 所有 predictor 在 WikiText-103 上训练（~8M tokens），主要评估在 WikiText-2（同域）。C4 OOD 显示 degradation 从 1.46× 恶化到 1.74× dense。
- KL-discovered mask patterns 的 domain specificity 未知。缺少 C4-trained predictor 对比。

**W5. SPON 边际贡献（2.4%）在方法中位置偏重** [R1, R2 部分 REBUT]
- 仅 2.4% PPL improvement，cosine similarity 0.196, R²=0.038。R1 建议标注为可选组件；R2 认为 Related Work 段落是必要 positioning。
- 共识：不需要移除，但可以在 ablation 中更突出其边际性。

### Minor（不影响接收）

**M1.** -ing 分词短语偏多（~15 处），部分可改写（如 "enabling...discover" → 拆分独立句）。R1 认为不构成系统问题，R2 认为应 fix。[轻微分歧]
**M2.** Float spacing 被手动压缩（`\textfloatsep{8pt}`），conclusion 有 `\vspace{-4pt}`——不违规但暗示空间紧张。
**M3.** Ethics 声明遗漏 Qwen-2.5-14B（仅提 LLaMA-8B 和 Mistral-7B）。
**M4.** §3.3 Gumbel-Sigmoid 应优先引用 Concrete distribution (Maddison 2017) 和 L₀ (Louizos 2018)，而非 Gumbel-Softmax (Jang 2017)。
**M5.** §3.4 "mean-seeking" 术语不标准，应为 "mass-covering" 或 "inclusive"。
**M6.** §3.6 Jacobian 形式化应为 $\partial \mathbf{z}/\partial \tilde{m}_j$（对 mask），非 $\partial \mathbf{z}/\partial \mathbf{h}$（对 hidden state）。R2 认为 suggestive analysis 不需完整形式化。
**M7.** Table 1 同行混合不同统计报告（MMLU 3-seed 带 ±，GSM8K 单 seed 无 ±），易造成混淆。
**M8.** Table 4 SPON 脚注使用 `evaluate.py` 而非 unified benchmark，数值可比性需说明。

---

## Reviewer Consensus [AGREE]

| 议题 | 共识 |
|------|------|
| C1 ablation 2-seed 不够 | 两位均同意，核心 claim 需更强统计支撑 |
| Soft-vs-hard mask confound | R1 发现，R2 交叉确认 |
| 14B downstream reversal 需讨论 | 两位均 Must-Fix |
| BCE pipeline 不一致 | R1 发现，R2 交叉确认（Round 1 遗漏） |
| 50% downstream 崩溃 + framing 偏差 | 两位一致 |
| 无 wall-clock speedup | 两位一致（定级有分歧，见下） |
| 方法新颖性 → Findings 级别 | 两位结论一致 |
| Overall 3.0 (Findings) | 完全一致 |

## Reviewer Divergence [REBUT]

| 议题 | R1 | R2 | 状态 |
|------|----|----|------|
| Wall-clock speedup 定级 | Should-fix（论文已诚实 scope） | Must-fix | 不影响评分 |
| 方法新颖性定级 | 属于定位问题非缺陷 | Must-fix | 不影响评分（都认为 Findings） |
| -ing 短语 | 不构成问题 | Should-fix | Minor 分歧 |
| Predictor 架构比较 | Should-fix | 不需要（贡献在 objective） | Minor 分歧 |
| §3.6 Jacobian 形式化 | Minor issue | 不需修改（suggestive analysis） | Minor 分歧 |

**分歧评估**：所有分歧仅涉及问题定级（must-fix vs should-fix, should-fix vs minor），不涉及问题是否存在。核心判断完全一致。无需进入 Round 2。

---

## Questions for Authors

**Q1** [R1+R2 共识]: C1 ablation 的 "KL-derived oracle masks" 具体如何生成？从哪个 checkpoint（step）、哪个 seed 的 KL predictor 提取？用另一个 seed 的 KL predictor 生成 masks 是否会得到不同 C1 结果？

**Q2** [R1+R2 共识]: 14B MMLU reversal 是否在多个 seed 上验证？Table 7 仅报告 seed 42。如果该 reversal 在不同 seed 间不稳定，可能只是噪声。

**Q3** [R1+R2 共识]: 30% sparsity 下 KL 的 actual sparsity 为 28.5%（Table 6）。Table 1 的 TEAL baseline 是在 exact 30% 还是也有偏差？如果 KL 在 28.5% 而 TEAL 在 30%，那 KL 的一部分 PPL 优势来自剪枝更少的 neurons。

**Q4** [R1]: 为什么没有报告 "50% BCE + TEAL global (no compensation)" 的结果？这是与 KL global 最直接可比的 baseline。

**Q5** [R1]: 在 C4 上训练 predictor 时，mask divergence from magnitude 的幅度是否类似？KL masks 的 domain specificity 有多大？

**Q6** [R2]: 50% downstream collapse 下 KL MMLU (28.1%) 与 TEAL (28.32%) 差异在 noise range 内。如果 downstream 是最终目标且 30% 是推荐操作点，为何以 50% PPL improvement 而非 30% downstream preservation 作为核心叙事？

---

## Missing References

**应引用** [R1+R2 共识]:
1. **Enabling Dynamic Sparsity in Quantized LLMs** (2025, arXiv 2511.04477) — 量化 + activation sparsity 协同设计
2. **Mixture of Neuron Experts** (2025, arXiv 2510.05781) — neuron-level MoE 转换，与 D2DMoE 互补

**可选引用** [有分歧]:
3. SeerAttention (2024) — R2 建议, R1 REBUT（attention sparsity vs FFN sparsity，已有 Polar Sparsity 覆盖）
4. DeepSeek-V3/DeepSeekMoE — R2 建议, R1 REBUT（native MoE 架构，非 dense→sparse 问题）

---

## External Review (Stanford Agentic Reviewer)

未配置。项目 `external_review.paperreview_ai.enabled` 未启用。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

### 支撑 Findings 接收的理由

1. **C1 因果消融**是有价值的 empirical finding——mask target quality > gradient coupling 在文献中没有先例，即使统计效力需加强，方向和设计都值得发表。
2. **Regime analysis**（非单调 allocation 偏好）对实践者有指导意义，Table 5 的 6-level 数据提供了有用参考。
3. **68% mask divergence** 从 magnitude ranking 是非显而易见的发现，揭示了 KL 训练发现了不同的 neuron importance landscape。
4. 方法公式化简洁正确，消融系统全面，写作清晰诚实。

### 阻碍 Main Conference 接收的理由

1. **方法新颖性有限**：KL + Gumbel + predictor 均为成熟组件的直接组合，MaskLLM 已在高度类似的框架下发表。
2. **C1 核心 claim 证据不充分**："causal ablation proves" 仅 2-seed，存在 soft-vs-hard confound，30% PPL gap 暗示 gradient coupling 残余贡献。
3. **14B downstream reversal**未被充分讨论，直接质疑方法的 scalability。
4. **实际可用范围极窄**：50% downstream 全面崩溃，30% 的 downstream 改进仅 ~2pp（多数不显著），无 wall-clock 加速。
5. **BCE baseline pipeline 不一致**使跨 sparsity 比较不可靠。

### 升级到 3.5 (Borderline Conference) 的路径

若能修复以下问题，可考虑升级：
- **N1**: C1 增加到 5-seed + 降级 "proves" 措辞 + 讨论 soft-vs-hard confound
- **N2**: 正文充分讨论 14B reversal + 提供机制假设
- **N3**: 增加 "50% BCE + TEAL global (no comp)" baseline
- **N4**: 将叙事重心从 50% PPL 转向 30% downstream quality

---

## Detailed Comments (Per-Section)

### Abstract
- 第 2 行 "causal ablation confirms" → 降级为 "ablation provides evidence"
- 第 4 行 "reduces PPL degradation 18%" → 改为 "reduces PPL by 18% relative to TEAL"（措辞与计算不匹配）
- 第 5 行 50% PPL 作为叙事高潮但 downstream 已崩溃 → 将 30% downstream quality 放在更突出位置
- 第 6 行 "confirms PPL advantage across 7-14B" → 必须同等突出 downstream reversal

### Introduction
- L10 "a causal ablation confirms" → 降级措辞
- L10-11 "the primary quality driver" → 加 caveat：30% 条件下可能有残余 gradient coupling 贡献
- L16 14B 提及过于简略 → 增加 1-2 句讨论 downstream reversal 的含义

### Method
- §3.3 优先引用 Concrete distribution (Maddison 2017) 和 L₀ (Louizos 2018)
- §3.4 "mean-seeking" → "mass-covering" 或 "inclusive"
- §3.5 Eq. 5 vs Eq. 6 约束类型统一
- §3.6 Jacobian 表述修正；"suggestive" 定位保持

### Experiments
- Table 1: 统一 30% 和 50% BCE 使用相同推理管线；增加 50% BCE+TEAL global baseline
- Table 1: 统一同行的统计报告格式（避免 MMLU 有 ± 而 GSM8K 无）
- Table 3: C1 增加 seed 数量；添加 confidence intervals
- §4.4 最后一段: 讨论 30% PPL gap 与 gradient coupling 的可能联系
- §4.5: 增加至少 1 段 14B reversal 的机制讨论
- §4.5: 补充 Mistral-7B downstream evaluation

### Related Work
- 增加 Enabling Dynamic Sparsity in Quantized LLMs (2025) 和 Mixture of Neuron Experts (2025)

### Conclusion
- 第 1 行 "confirms target quality, not gradient coupling" → 降级措辞

### Limitations
- 已较完善。可增加：C1 的 soft-vs-hard confound 作为方法论局限。

### Ethics
- 补充 Qwen-2.5-14B 模型引用和 license 信息。

### Appendix
- Table 4 SPON 脚注: 说明 evaluate.py vs unified benchmark 的数值差异影响。