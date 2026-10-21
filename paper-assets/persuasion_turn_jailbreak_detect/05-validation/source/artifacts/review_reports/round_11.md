---
round: 11
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-21T21:23:51.540849+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection

**项目**: persuasion_turn_jailbreak_detect
**目标 venue**: EMNLP 2026 via ARR May 2026
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）
**轮次**: Round 1, 1 轮收敛（交叉分享后关键问题达成共识）

---

## Summary

本文提出 DisPeD，通过 7 个 Stage-1 encoder adaptation 变体（9-class, binary, scrambled, MLM-only, topic, Wikipedia MLM, vanilla）配合 frozen BiGRU Stage-2 分类器，系统性消融了哪些因素驱动多轮 jailbreak 的跨攻击泛化。核心发现：(1) classification-based DAPT 是合成多轮 OOD 攻击上最鲁棒的变体；(2) MLM 可关闭约 60pp OOD gap 但在 mixed-LLM 训练下崩溃；(3) label correctness/granularity/temporal order 对检测无关。实验在 DeBERTa-v3-base、RoBERTa-base/large 三个 encoder 上验证，配合 ToxicChat 人类数据和 WildChat FPR 评估。

---

## Strengths

1. **精心设计的受控消融**: 7 个 Stage-1 变体 × 3 encoder 规模 × 4 攻击族 × 多种对话长度，frozen-encoder 设计确保变体间公平比较。这是该领域最系统性的消融研究之一。

2. **罕见的 transparency 水平**: 主动报告大量对核心 claim 不利的发现——WildChat FPR 68.1%、ToxicChat 证据层级反转、RoBERTa-large DAPT 反效果、cross-LLM FPR 88-90%。这种诚实在投稿中非常少见。

3. **有信息量的负面结果**: scrambled ≈ correct labels (TOST-confirmed on DD)、temporal order irrelevance (Δ<1pp)、domain specificity is marginal at full length——这些对未来研究有实际指导意义。

4. **详尽的附录**: 14+ 页补充实验（per-seed 分析、cross-checkpoint variance、length independence 验证、TOST sensitivity、CKA/t-SNE 可视化等），显著增强可信度。

5. **效率优势**: DeBERTa+BiGRU 12.1ms/对话 vs Qwen3-8B 5.2s，266× 推理加速，仅需 862MB VRAM 和 4 GPU-hours 总训练成本。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF1] IID benign 导致 OOD F1 为 upper bound，WildChat FPR 证实外部有效性不足** [R1-N1, R2-N3 — 两人最强共识]
- OOD 评估使用 38 条 IID Qwen3-8B benign 对话，论文自己承认 OOD F1 是 "upper bounds"（Section 5）。WildChat FPR = 68.1%（9-class），ROC AUC = 0.700，temperature scaling 无法改善。Cross-LLM 评估显示 Llama benign FPR 达 88-90%。Classification supervision 反而加重 benign 过拟合（FPR: 9-class 68.1% > vanilla 43.1%）。模型实际学会区分 "Qwen3-8B 风格" vs "非 Qwen3-8B 风格"，而非 "jailbreak vs benign"——这动摇了 evidence hierarchy 的外部有效性。
- **要求**: (1) WildChat FPR 从附录提升到正文 Section 4 或 5；(2) Abstract/Conclusion 明确 qualify "under matched benign distribution"；(3) 主文 OOD F1 表格旁标注 "benign-IID upper bound"。

**[MF2] 核心贡献新颖性有限——Classification DAPT 是 DAPT 文献的直接推论** [R2-N1, R1 AGREE]
- "classification-based DAPT is the most robust adaptation" 是 Gururangan et al. (2020) 的直接应用。论文未回答 **为什么** classification DAPT 在 jailbreak detection 中最优。Section 5 的 "optimization regularization" 解释仅有间接证据（frozen probing near-parity、label irrelevance、temporal irrelevance）——这些是 necessary 而非 sufficient conditions，替代解释（classification loss 引导更 generalizable 局部最优）未被排除。
- R1 补充：消融设计本身有方法论贡献，但 "why" 层面的 mechanistic 解释缺失使 insight 密度不足以支撑 long paper。
- **要求**: (1) 降低 "optimization regularization" 措辞确定性为 "consistent with"；(2) 明确阐述哪些发现 **不可从已有文献预测**。

**[MF3] 合成数据规模过小 + 单一 LLM 来源，限制结论普适性** [R1-N2, R2-N3 — 强共识]
- 350 训练（175 jailbreak + 175 benign）+ 76-118 测试，全部 Qwen3-8B 生成。Data efficiency 显示 50 条即达 AA F1 = 0.969，暗示合成数据 diversity 极低。Mixed-LLM 条件下 ActorAttack F1 仅 0.504±0.107。ToxicChat 上证据层级完全反转：JB-MLM (0.837) >> 9-class (0.596)。
- **要求**: (1) 至少用 3+ LLM 生成训练数据验证 hierarchy 稳定性，或 (2) 在所有 claim 中明确限定 scope 为 "on synthetic data from a single LLM"。

**[MF4] Scrambled ≈ correct labels 有文献先例，且削弱 taxonomy 贡献** [R2-N2, R1 AGREE]
- Random label training 有直接先例：Zhang et al. (2017/2021) "Rethinking Generalization"、Maennel et al. (2020)、Kang et al. (2018)。论文仅引用 SimCLR/BYOL（contrastive SSL），未引用更直接相关的文献。
- R1 补充：本文测试的是 random labels 的 **OOD transfer** 而非训练集 memorization，应明确讨论与 Zhang et al. 的区别。
- 此外在 ActorAttack 上 TOST n=5 仍 inconclusive (p=0.08)，该 claim 在最具判别力的 benchmark 上未被统计确认。
- 9-class taxonomy 的贡献被自身实验否定——如果随机标签同样有效，为何需要精心设计的 taxonomy？
- **要求**: (1) 引用 random labels 文献；(2) 明确 taxonomy 定位为 interpretability tool + ablation infrastructure 而非检测组件。

### Should-Fix（影响评分但不一票否决）

**[SF1] 3-seed 统计功效不足** [R1-N3=critical, R2=warning — 唯一分歧点]
- Cohen's d 从 0.59 (n=3) 降到 0.09 (n=5)，说明小样本 effect size 估计极不稳定。TOST AA p=0.08 at δ=5pp，margin 缺乏理论依据。Population std (n divisor) 低估方差约 22%。
- R2 部分反驳：跨多条件（3 encoder × 4 攻击族）的一致排序提供间接补偿。
- **Director 裁定**: 降级为 Should-Fix——排序结论有间接 robustness 证据，但统计精度确实不足。要求在主文明确标注 AA 上 TOST inconclusive，并为 margin 选择提供依据。

**[SF2] 长度混淆未充分排除** [R1-W1, R2 AGREE]
- Benign 12-20 turns vs jailbreak 3-10 turns，完全不重叠。ActorAttack padding 到 15+ turns 后 F1 从 0.963 暴跌到 0.383 (Δ=-57.9pp)。Benign truncation FPR=0 是弱控制（IID benign 上 FPR 本身为 0）。
- **要求**: 生成 length-matched benign/jailbreak 数据，或报告 length-controlled subset 结果。

**[SF3] 缺少与 DeepContext 等已有系统的直接对比** [R1-W3, R2-W3 — 强共识]
- Vanilla DeBERTa+BiGRU 被声称 "architecturally equivalent to DeepContext"（Section 4.1），但未使用原始代码/权重/数据复现。Llama Guard 3 已添加但仅 zero-shot。
- **要求**: 复现 DeepContext 完整 pipeline 在本文 OOD benchmark 上，或承认仅为架构级比较而非方法级比较。

**[SF4] Human data 上 evidence hierarchy 完全反转** [R1-W4, R2 强 AGREE]
- ToxicChat: JB-MLM (0.837±0.013) >> 9-class (0.596±0.087)，差距 24pp。WildChat: 9-class FPR (68.1%) > vanilla FPR (43.1%)。Classification DAPT 在所有涉及真实人类数据的评估中系统性劣于 MLM。
- **要求**: Abstract/Conclusion 限定 claim scope 为 "on synthetic multi-turn OOD evaluations"；讨论 real-world deployment 时 MLM 可能是更优选择。

**[SF5] "Optimization regularization" 机制解释缺乏直接证据** [R1-W2, R2 AGREE]
- 三条间接证据（frozen probing near-parity、label irrelevance、temporal irrelevance）排除了替代假设但未正面证明。CKA 分析是描述性而非解释性。
- **要求**: 降低措辞确定性，或提供 loss landscape/gradient norm 等直接证据。

**[SF6] Analysis paper insight 密度偏低** [R2-W4, R1 部分 AGREE]
- 主要发现（DAPT > vanilla）在 DAPT 文献框架下可预期；负面结果有先例；最有趣的发现（human data reversal, WildChat FPR）被压缩或藏在附录。
- **建议**: 考虑将人类数据泛化问题作为核心研究问题之一而非辅助发现。

### Minor（不影响接收）

- MLM-only IID 为 single seed (42) 而其他变体报告 3-seed mean（Table 2 脚注标注但正文比较时无提醒）
- "OOD" 同时指 attack-side shift 和 benign distribution shift，两种含义不同——Terminology 段应区分
- Abstract 中 Llama Guard 3 1.8% 有 misleading 风险——它是单轮 classifier，缺 conversation-level 适配
- 引用格式：9 个 mismatch entries 需核实（Austin 1962 vs 1975, Cialdini 2001 vs 2008 等）
- Table 3 "Mean pooling" 行应更明确标注为 "9-class encoder + mean pooling"
- 页数溢出（见 Visual Layout Check）

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下核心问题上完全一致：

1. **IID benign 是最严重的方法论 confound** — WildChat FPR 68.1% 证实这不是理论问题，classification supervision 反而加重 benign 过拟合
2. **合成数据规模和单一来源限制结论泛化性** — 50 条即达高 F1 暗示低 diversity，mixed-LLM 和人类数据均验证不足
3. **核心贡献新颖性有限** — DAPT 应用 + 有先例的负面结果，mechanistic 解释不足
4. **DeepContext 比较不充分** — "架构等价"声明不能替代完整 pipeline 复现
5. **Human data hierarchy reversal 严重限制核心 claim scope** — 9-class 在所有真实数据评估上劣于 MLM
6. **消融设计的系统性和 transparency 是显著优势** — 7 变体 × frozen encoder × 详尽附录

---

## Reviewer Divergence [REBUT]

**n=3 seeds 统计功效不足的严重程度**:
- R1: **Critical** — Cohen's d 不稳定 (0.59→0.09)，TOST AA inconclusive，population std 低估 22%
- R2: **Warning** — 跨多条件（3 encoder × 4 攻击族）的一致排序提供间接 robustness 证据；per-sample 分析（98.3% accuracy, 0 samples misclassified by all 3 seeds）补充了 seed-level 不足
- **Director 裁定**: Should-Fix。排序稳定性有说服力，但数值精度（TOST, variance ratio）确实需要更多 seeds。

**Figure 2 y 轴**:
- R2: Warning — y 轴不从 0 开始，视觉误导
- R1: REBUT — 实际检查 y 轴从 0 开始，无截断
- **Director 裁定**: 不构成问题。

**RoBERTa-large representation drift 解释**:
- R1: Post-hoc 解释
- R2: 部分 REBUT — Table 15 learning rate ablation 提供了部分 mechanistic 支持
- **Director 裁定**: 应承认是 post-hoc hypothesis 但有 partial evidence，非无证据推测。

---

## Questions（需作者澄清）

1. 如果训练集混入真实 benign 对话（如 WildChat 子集），FPR 和 OOD F1 会如何变化？这是最关键的 missing experiment。
2. Data efficiency 显示 50 条即达 AA F1 = 0.969——如果用 50 条 ActorAttack 训练，evidence hierarchy 是否改变？
3. TOST margin 5pp 的选择依据是什么？是否有 equivalence testing 文献的先例？
4. Mixed-LLM 条件下 MLM 崩溃到 vanilla 水平 (0.289 vs 0.291) 的 mechanistic 解释？
5. ToxicChat 上 JB-MLM > 9-class 对核心 claim "classification DAPT is most robust" 意味着什么？是否应在 claim 中限定为 synthetic multi-turn？
6. Scrambled 和 correct 在 Crescendo/FITD 上差异是否也统计不显著？（预期 trivially 不显著因为所有变体饱和 F1≥0.990，但应确认）

---

## Missing References

两位 Reviewer 一致认为以下文献应被引用：

1. **Zhang et al. (2017/2021)** "Understanding Deep Learning Requires Rethinking Generalization" — random label training 奠基工作，直接解释 scrambled labels 发现
2. **Maennel et al. (2020)** "What Do Neural Networks Learn When Trained With Random Labels?" — 分析随机标签训练中表示学习性质
3. **Kang et al. (2018)** "Leveraging Random Label Memorization for Unsupervised Pre-Training" — 随机标签作为预训练信号

已有引用覆盖尚可：multi-turn defense (DeepContext, BIID, G-Guard, SafeDream, X-Boundary, JBShield), DAPT 前辈 (BioBERT, SciBERT, Gururangan et al.), SSL (SimCLR, BYOL)。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成，发现 1 critical + 3 warning + 8 info：

**Critical**:
- **页数溢出 (pp.8-9)**: Section 6 Conclusion 在 page 8 底部开始，部分内容溢出到 page 9（Limitations 标题上方约 10 行续文）。EMNLP 2026 严格 8 页主体文本限制，Conclusion 计入主体文本。**可能触发 desk reject。** 这是历史回归问题（Round 8 曾修复）。

**Warning**:
- 首页无视觉锚点——Figure 1 在 page 2，若提升到 page 1 可改善第一印象
- Pages 6-7 统计数字密集的行内文本，扫读性差——建议提炼为 summary table
- Figure 1 使用单栏宽度，作为核心架构图视觉冲击力不足

**Info** (8 项): Table 2 脚注字号偏小、Figure 2 建议增加 hatching pattern、Appendix tables 字号偏小、Figure 3 热力图数值偏小、p.15 display items 密度极高、booktabs 格式一致性良好、Limitations 简短符合规范、Checklist 正常。

---

## Overall Assessment

**评分: 3.0 — Findings（可被 Findings 接收）**

**EMNLP 2026 ARR 评分体系**: 3 = Findings

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Reproducibility | 3.0 | 4.0 | 3.5 |
| Overall | 3.0 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**核心判断**: 这是一篇设计精良、transparency 极高的受控消融研究，其系统性方法论和诚实的负面结果报告值得肯定。然而：

1. **外部有效性不足**: IID benign → WildChat FPR 68.1%，证据层级在人类数据上完全反转。核心 claim 仅在 "合成数据 + IID benign" 条件下成立。
2. **新颖性有限**: DAPT 在新领域的应用 + 有文献先例的负面结果，mechanistic 解释不足以支撑 long paper 的 insight 密度要求。
3. **实验规模制约**: 350 条合成训练数据 + 单一 LLM 来源，统计支撑（n=3-5 seeds）在关键比较上 inconclusive。

论文的核心价值在于为考虑部署小型 encoder 做 jailbreak detection 的从业者提供了系统性的 design space 探索。作为 Findings paper，这一贡献是有意义的；作为 Main conference paper，insight 深度不够。

**接收建议**: Findings 接收可考虑，但需解决 MF1（WildChat FPR 在正文）、MF4（taxonomy 重定位 + random labels 引用）和页数溢出（desk reject 风险）。MF2（新颖性）和 MF3（数据规模）是结构性限制，短期难以完全解决，但通过限定 claim scope 可部分缓解。

---

## Detailed Comments

### Abstract
- "offering a practical alternative given matched benign distributions" 措辞需修改——44-68% FPR 与 "practical" 矛盾
- Llama Guard 3 1.8% 应注明是 turn-level classifier 做 conversation-level 评估的结果
- 建议在 abstract 尾句加入 "on synthetic evaluations" 限定

### Section 1 (Introduction)
- Contributions 与 Section 4/5 的实验结果基本一致，scope 限定已较好
- 第三个 contribution "optimization regularization, not semantic learning" 措辞过于确定

### Section 2 (Related Work)
- 缺少 random labels 文献 (Zhang et al. 2017/2021, Maennel et al. 2020, Kang et al. 2018)
- Multi-turn defense 引用较全面
- "Our ablation fills this gap" 措辞稍强——改为 "contributes to filling this gap"

### Section 3 (Method)
- 7 变体设计清晰系统，Table 1 简洁有效
- "each isolates a single factor" 已改为 "systematically vary training objectives"——现有措辞合适
- Binary intent head 始终存在（除 MLM-only 和 vanilla），这一 confound 应在 limitations 中提及

### Section 4 (Experiments)
- Terminology 段 "OOD reflects attack-side shift only" 应更加突出（目前容易被忽略）
- Table 2: MLM-only IID single seed 应统一为 3-seed
- Section 4.3 evidence hierarchy 讨论信息密度高但扫读性差——考虑 summary table
- Section 4.6 human data 段过短，应扩展讨论 hierarchy reversal 的含义
- FITD 已标注 "non-discriminative"，处理到位

### Section 5 (Discussion)
- "Benign distribution as the remaining bottleneck" 是最重要的段落但篇幅偏短
- "Regularization mechanism" 段应降低确定性（"consistent with" 而非断言）
- 缺少与 random labels 文献的联系

### Section 6 (Conclusion)
- **页数溢出**: 必须压缩到 page 8 以内
- "practical alternative given matched benign distributions" 需修改

### Limitations
- 覆盖点充分（合成数据、IID benign、encoder scale、scope）
- 长度适中，符合 EMNLP 2026 规范

### Appendix
- 信息量极大，per-seed 分析、TOST sensitivity、cross-LLM error decomposition 等显著增强可信度
- WildChat FPR、cross-LLM FPR 应考虑提升到正文