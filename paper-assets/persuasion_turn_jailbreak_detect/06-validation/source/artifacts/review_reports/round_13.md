---
round: 13
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T07:12:51.645703+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 13 审稿报告 — DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection

**Venue**: EMNLP 2026 via ARR May 2026 | **Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作) | **模式**: Fresh Review

---

## Summary

本文提出 DisPeD，一个两阶段 pipeline（Stage-1 encoder adaptation + Stage-2 frozen BiGRU），通过 13 种 encoder 配置在 3 个模型规模（125M–355M）上系统分解多轮 jailbreak 检测中 domain-adaptive pretraining（DAPT）的贡献因素。核心发现：(1) 分类 DAPT 是合成多轮 OOD 攻击上最鲁棒的适配方式；(2) scrambled labels 在模板型攻击上等价于正确标签（TOST 确认），但在结构复杂攻击上有中等效应量差异（d=0.44）；(3) temporal order 和 label granularity 无关。论文将机制解释为 optimization regularization 而非 semantic learning。所有多轮评估在 Qwen3-8B 合成数据上进行，附以 ToxicChat 单轮人类数据验证。

---

## Strengths

**S1. 精心设计的受控消融框架** [R1+R2 共识]
7 种 Stage-1 变体（Table 1）系统隔离 domain exposure、classification supervision、label correctness、granularity、domain specificity 等因素，每个变体只改变一个因素。这种实验设计在 NLP 安全领域罕见，方法论上有示范价值。

**S2. 有洞察力的 null results** [R1+R2 共识]
scrambled labels ≈ correct labels（Section 4.2, TOST 确认）和 temporal order 不影响检测（|Δ| < 1pp）是两个 genuinely informative 的发现，对理解 encoder adaptation 机制有实质贡献，避免了领域内对"标签语义信号"的过度归因。

**S3. 统计报告高于同领域平均** [R1+R2 共识]
3-seed 评估 + 10-seed TOST 等价检验、bootstrap CI、paired permutation test、per-seed F1 表——统计严谨性远超同领域多数论文。

**S4. 跨编码器验证增强可信度** [R1+R2 共识]
在 DeBERTa-v3-base、RoBERTa-base、RoBERTa-large 三种架构上重复核心实验（Section 4.4, Table 4），揭示了 architecture/scale-dependent pattern。

**S5. 诚实的 limitation 讨论** [R2]
论文主动报告了 WildChat 68.1% FPR、benign distribution 系统性限制、合成数据约束，并提供了 benign adaptation curve 作为补救方案。

**S6. 实际部署考量** [R1]
125M-355M 参数编码器，推理速度 24.3× 快于 LLM-as-judge，4 GPU-hours 总训练成本，展现了对实际部署约束的关注。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] 单一合成数据源严重限制泛化声明 [R1+R2 完全一致]
- 所有训练和多轮 OOD 评估数据均由 Qwen3-8B 单一模型生成（Section 4.1）
- 论文声称的"cross-attack generalization"仅为攻击家族（Crescendo→DD/FITD/ActorAttack）的泛化，三个 OOD 家族的对话风格、词汇分布、句法模式均来自同一 LLM
- Mixed-LLM 实验（Section 4.5, Table 13）的 OOD 评估仍在 Qwen 生成数据上进行
- ToxicChat 验证是 single-turn（Section 4.6），无法验证多轮检测的核心贡献
- **建议**：至少一个 OOD 评估集使用非 Qwen LLM 生成的攻击数据；或显著弱化泛化声明为 "cross-attack-family generalization within single-source synthetic data"

**N2** [critical] WildChat FPR=68.1% 且 9-class FPR 最高，DAPT 加剧 benign 分布偏差 [R1+R2 完全一致]
- 9-class（论文推荐的最优变体）在 WildChat 真实数据上 FPR=68.1%，**高于** vanilla 的 48.1%（Appendix O, Table 18）
- DAPT 使 encoder 对 benign 分布偏移更敏感——直接与论文 "DAPT provides robustness" 叙事矛盾
- ROC AUC=0.700±0.054，表示层面无法区分 WildChat benign 和 jailbreak
- Appendix P 的 benign adaptation（10 样本修复 FPR→0%）将问题从 zero-shot 变为 few-shot supervised，改变了部署前提
- 论文主文报告的 OOD F1 实际是 attack-side upper bounds conditioned on matched benign distribution，读者仅看 Table 2-3 会产生误导性高性能印象
- **建议**：主文中（非仅附录）正面讨论 WildChat FPR；提升 benign adaptation 实验到主文；重新定位 OOD F1 为 conditioned upper bounds

**N3** [critical] "Optimization regularization, not semantic learning" 机制解释缺乏直接证据 [R1+R2 完全一致]
- 这是论文三大贡献之一（Contribution #3），但全部支撑证据为间接关联性的：
  - frozen probing near-parity（AA gap 3.1pp）→ 不能区分 regularization vs 其他机制
  - scrambled ≈ correct labels → 可解释为 classification structure effect（相同 cross-entropy loss + output space dimensionality → 相似 gradient dynamics）
  - temporal order irrelevant → 只说明 detection 不依赖序列信息，与 regularization 无直接关系
- 缺失的直接证据：weight norm trajectory、loss landscape sharpness、gradient norm/direction 分析、representation collapse metrics
- 多种替代假说同样兼容：representation collapse prevention、gradient diversity、classification structure effect
- SimCLR/BYOL 类比不恰当——contrastive/self-supervised 方法与 random-label classification pretraining 机制完全不同
- R1 交叉回应进一步指出：9-class 在 ToxicChat 上仅 0.596（低于 MLM 的 0.837），如果 regularization 是 task-agnostic 的稳定化机制，不应在 single-turn 上大幅退化。这暗示 classification DAPT 的效果是 task-structure-specific 而非 general regularization
- **建议**：提供直接优化动力学证据；或将 Contribution #3 降级为 Discussion 中的假说（"consistent with..."），同时讨论替代解释

### Should-Fix 问题

**W1** [major] 新颖性受限——DAPT 在安全领域的直接应用 [R2 提出, R1 部分同意]
- 两阶段结构（Stage-1 DAPT → Stage-2 frozen classifier）几乎是 Gururangan et al. (2020) 的直接实例化
- 核心发现（DAPT 有效、classification > MLM > vanilla）在 DAPT 文献中可预期
- R1 认为 scrambled label null result 在 DAPT 文献中无先例，有差异化贡献，建议从 critical 降为 major
- **建议**：将 scrambled label 发现提升为核心贡献并深化分析（连接 Maennel et al. 2020 random label representation 理论）

**W2** [major] Scrambled label 等价性受 attack complexity 限制 [R1+R2 一致]
- DD/FITD: TOST p < 10⁻⁸, d ≈ 0（等价确认）
- ActorAttack: TOST p=0.183, d=0.44（中等效应量，不等价）
- Contribution #1 和 Abstract 中对此条件性表述不够突出
- **建议**：限定为 "on template-based attacks (TOST-confirmed), but with moderate effect on structurally complex attacks"

**W3** [major] 论文标题 "Persuasion Detection" 与核心发现（标签语义无关）矛盾 [R1+R2 一致]
- DisPeD = "Disentangled Persuasion Detection" 暗示说服策略分类是检测关键
- 但 scrambled ≈ correct labels 且 OOD 策略预测降至 κ=0.126
- **建议**：调整标题/framing，重点从 persuasion detection 转向 classification supervision 的效应

**W4** [major] Scale analysis 被架构差异混淆 [R1+R2 一致]
- 三种"scales"（DeBERTa-v3-base/RoBERTa-base/RoBERTa-large）实际是不同架构 + 不同预训练
- RoBERTa-large vanilla AA F1=1.000 但 DAPT 后降至 0.946——重要反面结果未充分讨论
- R1 补充：跨架构验证仍有价值，问题在 framing 不在实验
- **建议**：降级为 observation，不作为独立贡献声明

**W5** [major] Mixed-LLM 结果薄弱但被正面呈现 [R1+R2 一致]
- ActorAttack F1=0.504±0.107，勉强超 vanilla 0.389（+11.5pp），seed 方差极大
- ToxicChat 低于 single-source（0.550 vs 0.596）
- 论文正面叙事 "classification supervision generalizes across LLM sources" 与实际数字不符
- **建议**：降低呈现层级，明确承认 ActorAttack 退化

**W6** [minor] FITD 作为 OOD evaluation 缺乏区分力 [R1+R2 一致]
- 所有方法 F1≥0.990（Table 7），无法区分不同 Stage-1 变体
- 有效 OOD 评估仅 DD 和 ActorAttack 两个家族
- **建议**：开头即说明 FITD 非区分性质

**W7** [minor] Abstract 信息密度过高 [R2 提出, R1 同意 Abstract 部分]
- 第 5-8 句连续引入 4 个独立发现各附条件限定
- **建议**：聚焦 1-2 个核心 claim

**W8** [minor] 策略标注质量偏弱 [R1 提出, R2 同意但认为因 scrambled≈correct 而降低严重性]
- κ=0.78, n=50, 单标注员——对 9-class 分类属一般水平
- 策略轨迹分析（Section 4.8）依赖标注正确性

---

## Reviewer Consensus [AGREE]

以下关键问题两位 Reviewer 完全一致：
1. **合成数据 + WildChat FPR 限制泛化声明**（N1+N2）——9-class 在真实数据 FPR 最高，OOD F1 为 conditioned upper bounds
2. **"Optimization regularization" 机制解释证据不足**（N3）——全部间接证据，缺乏直接优化动力学测量
3. **标题与发现矛盾**（W3）——"Persuasion Detection" 与标签语义无关的核心发现不一致
4. **Scrambled label 条件性**（W2）——仅在模板型攻击上等价，ActorAttack 有中等效应
5. **FITD 非区分性**（W6）——有效 OOD 仅两个家族
6. **Mixed-LLM 薄弱**（W5）——0.504 F1 不构成正面结果
7. **Scale confounded by architecture**（W4）——不应作为独立贡献

## Reviewer Divergence [REBUT]

1. **信息密度**：R2 认为正文数据密度过高（W7），R1 反驳消融研究固有需求，但同意 Abstract 需精简。**结论**：Abstract 需精简，正文密度可接受。
2. **统计功效**：R1 认为 3-seed × 76 样本功效不足（R1-W1），R2 反驳论文已有 10-seed TOST 扩展和 per-seed 一致性验证。**结论**：统计报告已高于同领域平均，但 power analysis 可增强说服力。
3. **TOST margin 选择**：R1 认为 margin 不一致有 p-hacking 嫌疑（R1-W2），R2 纠正事实——论文一致使用 5pp margin，ActorAttack 不等价被诚实报告。**结论**：不构成问题，论文的 sensitivity analysis（Table 16）报告了多个 margin 下的结果。
4. **Frozen design 公平性**：R1 认为对 vanilla 不公平（R1-W4），R2 引用 E2E gap ≤5.8pp 和 BERT proxy 证据反驳。**结论**：经验影响有限，但建议补充 vanilla E2E 结果。

---

## Questions for Authors

**Q1.** [R1+R2 共识] 是否做过 weight norm trajectory、loss landscape sharpness、或 gradient norm 分析？如果没有，能否在 rebuttal 中补充至少一种直接 regularization 证据？

**Q2.** [R1+R2 共识] 9-class 在 ToxicChat（single-turn）上仅 0.596，低于 MLM 的 0.837。如果 optimization regularization 是 task-agnostic 的稳定化机制，为什么在 single-turn 上反而不如 MLM？这是否意味着分类 DAPT 的效果是 task-structure-specific（multi-turn 表示空间优化）而非 general regularization？

**Q3.** [R1] Appendix P 的 benign adaptation（10 样本 FPR→0%）是在 WildChat GPT-3.5 对话上验证的 IID 结果。部署到全新 chat platform（e.g., Claude, enterprise chat）是否同样只需 10 样本？Benign adaptation 的跨平台泛化本身是否需要评估？

**Q4.** [R1] 如果 scrambled ≈ correct labels，使用任意随机标签分配（2-class/50-class random）是否同样有效？这能否帮助区分 "classification structure effect" 与 "optimization regularization"？

**Q5.** [R2] RoBERTa-large vanilla AA F1=1.000 但 DAPT 后降至 0.946。这是否意味着对足够大的预训练模型，DAPT 本身可能有害？这对论文核心结论的适用范围有何影响？

---

## Missing References

1. **Maennel et al. (2020)** — random label 如何影响 representation learning 的理论分析，与 scrambled label 发现高度相关 [R1+R2 一致认为最关键缺失引用]
2. **JailDAM (2025)** — Jailbreak Detection with Adaptive Memory，直接处理 multi-turn jailbreak detection [R2]
3. **Anil et al. (2024)** — "Many-shot Jailbreaking"，相关多轮越狱技术 [R1]
4. **Jain et al. (2023)** — "Baseline Defenses for Adversarial Attacks Against Aligned Language Models" [R1]
5. 近期 **activation-based jailbreak detection** 方法（probing LLM activations）[R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，跳过。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 1 warning, 12 info）。

**Warning:**
- Page 13: Tables 7, 8 字号 ≤6pt，密集数值矩阵在打印时可读性差。建议精简或移入补充材料。

**Info（选取关键项）:**
- 主文严格 8 页，Limitations/Ethics 在限制外，符合 EMNLP 2026 格式
- Figure 1 架构图偏小但可辨认，建议放大
- 所有表格使用 booktabs 风格，格式专业
- 未发现 margin 溢出、公式渲染错误等排版缺陷
- 参考文献格式统一，无未解析引用
- Responsible NLP Research Checklist 包含在 PDF 中——按 EMNLP 2026 ARR 规则，此 checklist 应在 OpenReview submission form 中填写而非嵌入论文 PDF

---

## Overall Assessment

**Overall Score: 3.0 — Findings**（可被 Findings 接收）

**置信度: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Reproducibility | 4/5 | — | 4/5 |
| Overall | 3.5 | 3.0 | **3.0** |

**评分理由**：

这是一篇实验设计认真、统计报告规范的实证研究。受控消融框架（7 变体 × 3 编码器）和 scrambled label null result 对社区有参考价值。但三个核心问题阻止主会议接收：

1. **机制声明缺乏直接证据**（N3）："optimization regularization, not semantic learning" 被列为核心贡献，但全部证据为间接关联，且 ToxicChat 上 9-class < MLM 直接挑战了 task-agnostic regularization 叙事。作为 Contribution #3 的证据强度不足。

2. **泛化声明的可信度**（N1+N2）：所有多轮 OOD F1 在单一合成源 + IID benign 条件下获得。当遇到真实 benign 分布时（WildChat），最优变体 FPR 最高（68.1% > vanilla 48.1%），说明 DAPT 加剧了 benign 偏差。论文的 OOD F1 实际是 conditioned upper bounds。

3. **新颖性**（W1）：两阶段 pipeline 本质是 Gururangan et al. (2020) DAPT 的直接应用实例化。最有新颖性的发现（scrambled label 等价性）受限于 attack complexity（ActorAttack d=0.44 不等价），且未被充分提升为核心贡献。

**如果以下修改到位，可重新评估为 3.5（Borderline Conference）**：
- 将 Contribution #3 降级为 Discussion 假说，或补充直接 regularization 证据
- 主文正面讨论 WildChat FPR，重新定位 OOD F1 为 conditioned upper bounds
- 提升 scrambled label null result 为第一贡献并深化与 random label representation 理论的联系

---

## Detailed Comments

### Abstract
- 信息密度过高：第 5-8 句连续 4 个独立发现，建议聚焦 1-2 个核心 claim
- "roughly 60 percentage points" 精度与其他数字不一致
- "Disentangled Persuasion Detection" 名称与标签语义无关的核心发现矛盾

### Introduction (Section 1)
- Contribution bullets 过长（6-8 行/bullet），建议压缩为 1-2 句核心声明
- Contribution #1 中 "supplementary negative results" 应提升——scrambled label 发现是论文最有新颖性的贡献
- Contribution #2 "Architecture- and scale-dependent observation" 的 hedging 不够——应明确声明 architecture confound
- Contribution #3 "Mechanistic interpretation" 的证据强度不足以作为独立贡献

### Method (Section 3)
- Table 1 设计精良，消融逻辑清晰
- Strategy annotation κ=0.78/n=50/单标注员：虽因 scrambled≈correct 而降低严重性，但策略轨迹分析依赖标注正确性

### Experiments (Section 4)
- Section 4.2 应开头即声明 FITD 非区分性质
- Section 4.4 "cross-encoder validation" 的 scale 叙事需调整为 architecture observation
- Section 4.5 mixed-LLM：ActorAttack 0.504 不应被正面呈现
- Section 4.6 ToxicChat：应明确定位为"补充验证"而非"人类数据验证的主要证据"
- Section 4.7 perturbation：在 ActorAttack 上退化 20.4pp，应更突出讨论

### Discussion (Section 5)
- "Benign distribution as the remaining bottleneck" 是论文最诚实也最重要的段落，但被放在最后；建议提前或提升到 Section 4 主线
- "Regularization mechanism" 段落需大幅修改：当前作为因果声明呈现，应改为一致性假说

### Limitations (Section 7)
- 相对充分，诚实报告了合成数据、ToxicChat 局限、scale confound
- 建议增加：(a) WildChat FPR 68.1% 的明确提及；(b) benign adaptation 的部署前提条件
