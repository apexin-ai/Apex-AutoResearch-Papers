---
round: 3
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-18T18:17:51.087152+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿汇总报告 — Round 3 (Fresh)

**论文**: "What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap"
**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作）
**审稿轮次**: Round 1 独立审稿 + 交叉分享，1 轮收敛
**外部审稿**: 未启用

---

## Summary

本文通过控制性消融研究，分析什么表示属性使 multi-turn jailbreak 检测跨攻击族泛化。设计七个 DeBERTa-v3 Stage-1 变体和三个 RoBERTa 变体（统称 DisPeD），在四个攻击族（Crescendo, FITD, DD, ActorAttack）上评估，得出三个发现：(1) DAPT 是 OOD 泛化主要机制（~60pp gap on DeBERTa-v3）；(2) encoder 预训练方法决定 DAPT 变得关键的难度阈值；(3) 分类监督起正则化作用而非策略分类作用。ToxicChat 验证表明 DAPT 优势迁移至 human-written 数据，但证据层级在人类数据上完全逆转。

---

## Strengths

**S1. 消融设计精良。** 七个 Stage-1 变体系统隔离五个因素（domain exposure, classification supervision, label quality, granularity, domain specificity），每个变体的对比意义清晰。加上两个 encoder 架构的交叉验证，构成教科书级消融矩阵。[R1, R2 一致]

**S2. 统计方法论严谨。** 3-seed 评估、McNemar's test、BCa bootstrap CI（10,000 resamples）、paired permutation test 的组合使用超过大多数 EMNLP 投稿的统计标准。主动报告 effect size 不显著的结果（分类变体间 McNemar all p>0.13）。[R1, R2 一致]

**S3. "分类作为正则化器"发现具有反直觉价值。** Scrambled labels = correct labels 在所有 OOD 评估上等效（gap ≤3.9pp），而 OOD 策略预测精度仅 30.7%（κ=0.126）。挑战了"需要好标签才能泛化"的朴素假设。[R1]

**S4. 诚实报告负面结果。** Perturbation robustness 在 ActorAttack 上不成立、variance reversal 在 ToxicChat 上出现、McNemar power 限制被明确讨论。这种透明度值得肯定。[R1, R2 一致]

**S5. 极低计算成本，可复现性好。** 全部变体 <4 GPU-hours，超参数完整报告（Appendix D），承诺开源。[R1, R2 一致]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] Figure 1 为 placeholder，论文未完成状态**
- method.tex line 10: `\fbox{\parbox{...}{Architecture diagram placeholder}}`
- 主架构图是空框。对于以 "systematic decomposition" 为核心的论文，架构图是理解七个变体关系的关键工具。
- desk reject 风险。
- [R1-N1, R2-N1: 两位 Reviewer 独立发现，交叉回应 **完全一致**]

**MF2. [critical] Single-LLM confound：cross-attack generalization claim 范围过宽**
- 训练数据和全部 OOD 评估数据（FITD, DD, ActorAttack）均由 Qwen3-8B 生成。"cross-attack generalization" 实际上是 "within Qwen3-8B generation distribution" 的泛化。
- ToxicChat 验证仅覆盖最弱 claim（DA > vanilla），未验证核心证据层级排序。且 ToxicChat 是单轮数据。
- 建议：(a) 用至少一个其他 LLM 生成 OOD 评估数据，或使用 MHJ 真实多轮人类 jailbreak 数据；(b) 若不可行，在标题/Abstract/Conclusion 中限定 claim 范围。
- [R1-N2, R2-N3 关联: **完全一致**]

**MF3. [critical] 证据层级在人类数据上完全逆转，动摇核心叙事**
- ToxicChat (Table 5): JB-MLM (0.837±0.013) >> Binary (0.705) >> 9-class (0.596±0.087)。所有含 classification objective 的变体均低于纯 MLM，严格按分类复杂度递减排序。
- 论文的 "modality mismatch" 解释不充分：如果好处仅限于多轮正则化，Binary 和 Scrambled 不应低于 MLM（它们有相同的 domain exposure）。更合理解释：classification supervision 过拟合到合成分布的 decision boundaries。
- Discussion 中 "distribution-specific regularization" 分析与 Abstract/Introduction 的 Finding 3 表述不一致。
- 建议：(a) 在 Abstract 和 Contribution 3 中明确 "distribution-specific"；(b) 将逆转作为核心发现之一而非例外；(c) 增加多轮人类数据评估。
- [R2-N3 critical, R1-W4 → 交叉后升级为 critical: **完全一致**]

**MF4. [critical] "Discourse-level" claims 缺乏直接证据，存在系统性 overclaiming**
- experiments.tex line 107 声称 DAPT 捕获 "pragmatic features (hedging, escalation markers, topic-shifting patterns)"，但无 probing 支持。
- mean pooling ≈ BiGRU（单 seed）：如果丢弃顺序信息不影响检测，discourse-level structure 体现在哪里？
- Related Work 将 probing classifiers 留给 future work，对自称 analysis paper 是重大缺陷。
- "beyond bag-of-words"（TF-IDF on ActorAttack 失败）≠ "discourse-level"，可能是 longer n-gram、sub-word、intra-sentence syntax。
- linear probing 结果（9-class vs vanilla/MLM 仅 1-5pp）与 detection F1 巨大差距的 disconnect 暗示 probing tasks 未捕获驱动检测的特征。
- 建议：增加 discourse-level diagnostic probing，或将 claim 降级为 "features beyond lexical overlap"。
- [R1-N3, R2 交叉回应强烈同意并升级: **完全一致**]

**MF5. [critical] DD 评估样本量数据矛盾，数据划分不透明**
- experiments.tex line 11: "80 Deceptive Delight" vs. line 265: "On OOD Deceptive Delight ($n$=118)"。80 ≠ 118 未解释。
- IID test "76 held-out Crescendo" 仅指 jailbreak，benign test set 大小和来源完全未说明。
- OOD 评估的 benign 样本数量和来源未交代。
- 直接影响可复现性和 F1 计算准确性。
- [R1-N4, R2 交叉确认: **完全一致**]

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] 3-seed variance estimation 不可靠**
- "4-20× variance reduction"（Finding 3 核心定量表述）基于 3 seeds，std 相对误差约 50%。MLM DD-Full std=0.115 主要由 seed 456 (recall=0.64) 驱动。Population std (N divisor) 在 n=3 时比 sample std 低 18%。
- 建议：增加到 5-10 seeds，或对 "4-20×" 添加显著 uncertainty caveat。
- [R1-W1, R2 交叉同意]

**SF2. [warning] McNemar's test 被误用为等价性证据**
- ≤7 discordant pairs 下 McNemar 几乎无统计效力。论文一方面用 p>0.13 支持 "non-factors" claim，一方面承认 power 不足——逻辑矛盾。
- absence of significance ≠ evidence of equivalence。
- 建议：补充 equivalence test (TOST)，或在每次引用 McNemar 时标注 power 限制。
- [R1-W2, R2 交叉同意]

**SF3. [warning] TF-IDF 在 DD 上 F1≥0.961，DD 作为核心评估集意义被削弱**
- TF-IDF per-prefix F1 达到 0.994-1.000（Appendix Table S2），full F1=0.961。DD 几乎完全被词汇特征解决。
- Table 3（论文第一个结果表）以 DD 为中心，但 DD 是 lexically solvable 的任务。ActorAttack（TF-IDF=0.261 vs 9-class=0.972）远更有说服力但被安排在后半段。
- ActorAttack 是唯一区分 lexical/beyond-lexical 的评估集，但也是唯一 perturbation robustness 崩溃的评估集——整个"beyond lexical"claim 的证据基础偏窄。
- 建议：将 ActorAttack 提升为主要展示评估集；在叙事中更早承认 DD lexical separability。
- [R1-W6, R2-W4: 独立提出，交叉完全一致]

**SF4. [warning] Encoder 容量混淆变量**
- DeBERTa-v3-base (184M) vs RoBERTa-base (125M) 参数量差 47%。Finding 2（"encoder pretraining method determines difficulty threshold"）与 "encoder capacity determines threshold" 无法区分。
- Discussion 承认但主文叙述仍归因于预训练方法。
- 建议：在 Contribution 2 和 Abstract 中添加 capacity caveat。
- [R1-W3, R2 交叉同意]

**SF5. [warning] Analysis paper 分析深度不足**
- CKA 仅一段描述无可视化；linear probing 仅一句话（1-5pp）无详细表格；无 t-SNE/UMAP embedding 空间可视化；无 attention pattern 分析。
- 作为 analysis paper，分析工具运用单薄，与 discourse-level claim 缺乏分析支撑直接相关。
- 建议：增加 CKA 矩阵热力图、probing 详细表格、embedding 空间可视化。
- [R2-W6, R1 交叉同意并关联到 discourse-level claim]

**SF6. [warning] Abstract 数据堆砌（12+ 数值）**
- ~220 words 中至少 12 个具体数值。审稿人 30 秒内难以提取核心信息。
- 建议：保留 2-3 个 headline numbers（~60pp gap, TF-IDF vs 9-class on ActorAttack, ToxicChat DA vs vanilla），其余用定性描述。
- [R2-W1, R1 交叉同意]

**SF7. [warning] Introduction vs Related Work 关于 vanilla baseline 与 DeepContext 关系自相矛盾**
- Introduction: "replicating the frozen-encoder-plus-RNN approach of DeepContext"
- Related Work: "it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function"
- 写作 bug，削弱论文可信度。
- 建议：统一为 "vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches without domain adaptation"。
- [R2-N4 提出, R1 REBUT 但同意语言矛盾是 must-fix level writing bug]

**SF8. [warning] 策略标注验证不充分**
- n=50、单人类标注者、κ=0.78。每类平均 ~5.5 样本。无 inter-human agreement baseline。
- Finding 3 间接缓解（label quality 不影响检测），但 Figure 3 策略轨迹分析仍依赖标注质量。
- 建议：增加第二个标注者或增加样本量；至少在 Figure 3 添加 caveat。
- [R1-W7, R2 交叉同意]

**SF9. [warning] 引用不足**
- 当前 31 条 bib 对 EMNLP 偏低（典型 40-60+）。
- 必须补充：He et al. (2023) DeBERTa-v3, Clark et al. (2020) ELECTRA, Kornblith et al. (2019) CKA, Qwen3-8B 官方引用。
- 建议补充：Bai et al. (2022) RLHF, Jain et al. (2023) Baseline Defenses, Qi et al. (2024), WildChat, LMSYS-Chat-1M。
- [R1 Missing Refs, R2-W3: 独立提出，关键遗漏交叉一致]

**SF10. [warning] Perturbation analysis 篇幅过长**
- Section 5.5 占约 1 页正文，但结论为 "attack-family-dependent"。
- R1 建议移至 appendix，R2 REBUT 认为 negative result 应留正文但压缩。
- 建议：压缩为半页，保留 IID+DD 正面结果和 ActorAttack negative result，逐 seed 细节移至 appendix。
- [R1-W5 提出, R2 REBUT 但同意压缩]

**SF11. [warning] 术语不一致**
- "domain exposure" / "domain adaptation" / "continued pretraining" / "DAPT" 四个术语混用。
- "evidence hierarchy" 首次出现于 Table 4 caption 但未预告。
- DisPeD 全称从未给出。
- [R2-W5, R1 交叉部分同意]

### Minor（不影响接收）

- **M1.** MLM-only 部分结果缺 std，seed 数不明确（Table 3 IID 列）。[R1-M2, R2-M4]
- **M2.** Qwen3-8B 广泛使用但无正式引用。[R1-M1, R2]
- **M3.** Population std (N divisor) vs sample std (N-1) 在 n=3 时差异 18%，选择未 justify。[R1-M4, R2-M7]
- **M4.** Table 3 选择性展示 3 个方法（可能给 cherry-picking 印象）。[R2-M2]
- **M5.** FITD 评估几乎无区分力（所有变体 F1≥0.990）。[R1-M3]
- **M6.** Checklist E2 关于 license 模糊（应指明具体 license）。[R2-M6]
- **M7.** TF-IDF 行无 std 注释（确定性模型应标注）。[R1-M6]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 在独立审稿和交叉回应中完全一致：

1. **Figure 1 缺失不可接受** — desk reject 风险
2. **Single-LLM confound** — cross-attack generalization claim 需要限定或扩展数据
3. **人类数据证据层级逆转** — "classification as regularizer" 的 Finding 3 需要根本性重新框定
4. **Discourse-level overclaiming** — 缺乏 probing 等直接证据，mean pooling≈BiGRU 与 discourse 叙事矛盾
5. **DD 评估样本量矛盾** — 数据划分不透明
6. **TF-IDF 削弱 DD 评估** — ActorAttack 应提升为主要评估集
7. **引用不足** — DeBERTa-v3, ELECTRA, CKA, Qwen3-8B 等关键引用缺失

## Reviewer Divergence [REBUT]

以下问题存在分歧，但已通过交叉回应达成部分共识：

1. **新颖性是否构成 critical 问题**: R2 认为 DAPT 作为核心发现新颖性不足 (critical)；R1 REBUT 认为消融设计和负面发现本身有增量，建议降级为 should-fix (framing)。**Director 判断**：R1 论证更有说服力——论文的增量不在 "DAPT works" 而在 "what doesn't work and why"，但 framing 确需调整以凸显真正增量。归类为 SF（framing adjustment）。

2. **是否需要与 DeepContext 等直接实验对比**: R2 认为缺少对比是 critical；R1 REBUT 认为 analysis paper 不应要求 SOTA comparison，但写作矛盾必须修复。**Director 判断**：R1 论证合理——analysis paper 的贡献在于 insight 而非 SOTA。语言矛盾归为 SF7（writing bug）。

3. **Perturbation analysis 是否应移至 appendix**: R1 建议移至 appendix；R2 REBUT 认为 negative result 应留正文但压缩。**Director 判断**：R2 论证合理——保留但压缩至半页。

---

## Questions for Authors

**Q1.** DD 评估 n=80 (Setup) vs n=118 (Perturbation Analysis) 的构成是什么？benign 样本来源？IID benign test set 大小？

**Q2.** 论文声称 "classification supervision functions as a representational regularizer"，但 ToxicChat 上所有含 classification objective 的变体均低于纯 MLM，且严格按分类复杂度递减排序。如何调和这两个结论？在什么条件下应选择 classification supervision vs MLM-only？

**Q3.** Mean pooling (single seed) ≈ BiGRU on DD。如果多 seed 确认此结果，这对 discourse-level framing 意味着什么？每个 turn 独立可分 vs 需要跨 turn 推理是根本区别。

**Q4.** Linear probing 差异（1-5pp）与 detection F1 差异（MLM vs 9-class ~8pp on DD, ~8pp on ActorAttack）量级不匹配。probing tasks 是否未捕获实际驱动检测的特征维度？

**Q5.** DAPT 捕获了什么具体特征使其超越 TF-IDF on ActorAttack？论文声称 "pragmatic features" 但有哪些证据（beyond TF-IDF failure）？

---

## Missing References

**必须补充**:
1. He et al. (2023) "DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing" — 论文使用 DeBERTa-v3 但仅引用 v1
2. Clark et al. (2020) "ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators" — DeBERTa-v3 的 RTD 预训练来自 ELECTRA
3. Kornblith et al. (2019) "Similarity of Neural Network Representations Revisited" — 论文使用 Centered CKA 但未引用原始方法
4. Qwen3-8B 官方引用 — 数据生成、标注、paraphrasing、baseline 均依赖此模型

**建议补充**:
5. Bai et al. (2022) "Training a Helpful and Harmless Assistant with RLHF"
6. Jain et al. (2023) "Baseline Defenses for Adversarial Attacks Against Aligned Language Models"
7. Qi et al. (2024) "Fine-tuning Aligned Language Models Compromises Safety"
8. WildChat (Zhao et al., 2024) / LMSYS-Chat-1M (Zheng et al., 2024)

---

## Overall Assessment

**评分: Weak Reject (2.75/5)**
- R1: 3.0/5 (Findings)
- R2: 2.5/5 (介于 Resubmit 和 Findings)
- Director 综合: 2.75/5

**置信度: 4/5**（两位 Reviewer 均仔细阅读全文，熟悉相关领域）

**一句话总结**: 消融设计优秀，DAPT finding 稳健，但 Figure 1 缺失、single-LLM confound、discourse-level overclaiming、人类数据上证据层级逆转四个 critical 问题使论文当前版本不适合 EMNLP main conference。

**详细判断**:

论文提出了一个好的研究问题（"什么使表示能跨攻击族泛化"），消融设计精巧且负面结果有价值。然而存在几个根本性障碍：

(1) **外部效度不足**：所有多轮评估在单一 LLM 生成的合成数据上完成；唯一的人类数据验证（ToxicChat）是单轮且推翻了证据层级。论文无法回答"这些发现在真实多轮场景中是否成立"。

(2) **核心 Finding 3 被自己的数据削弱**：ToxicChat 上所有含 classification objective 的变体均低于 MLM，严格按分类复杂度递减。"classification as regularizer" 更准确的说法是 "classification as distribution-specific regularizer that can hurt cross-distribution transfer"——这本身是有价值的发现，但需要作为主线的一部分而非事后修补。

(3) **Discourse-level framing 无支撑**：mean pooling ≈ BiGRU、probing 差异仅 1-5pp、无 attention/representation 可视化。"beyond lexical" 有证据（TF-IDF on ActorAttack），但 "discourse-level" 是 overclaiming。

(4) **完成度问题**：Figure 1 placeholder、数据矛盾（n=80 vs n=118）、关键引用缺失。

**修改建议优先级**:
1. [必须] 补 Figure 1
2. [必须] 修复数据矛盾（n=80 vs n=118），完善数据划分说明
3. [必须] 补充关键引用（DeBERTa-v3, ELECTRA, CKA, Qwen3-8B）
4. [高优] 重新框定 Finding 3：将人类数据逆转整合进核心叙事
5. [高优] 将 discourse-level claims 降级为 beyond-lexical，或补充 probing 证据
6. [高优] 限定 cross-attack generalization claim 的范围（within synthetic data manifold）
7. [中优] 将 ActorAttack 提升为主要展示评估集
8. [中优] 压缩 Abstract 数值、统一术语、压缩 perturbation section
9. [低优] 增加 seeds、补充 equivalence test、补充 representation 可视化

修复 1-3 后可视为完成稿提交；修复 1-6 后适合 EMNLP Findings；全面修复后有潜力冲击 main conference。

---

## Detailed Comments（逐节）

### Abstract
- 12+ 数值过载，保留 2-3 个 headline numbers
- Finding 3 表述需反映 distribution-specific 限定
- "seven encoder variants on DeBERTa-v3" 中 "on" 改为 "of" 或 "based on"

### Introduction
- 第四段结果段过长（~200 words, 15+ 数值），需压缩至 2-3 句
- "replicating the frozen-encoder-plus-RNN approach of DeepContext" 与 Related Work 矛盾
- Contribution 1 应强调"为什么替代方案失败"而非"DAPT 有效"
- Contribution 3 需添加 "distribution-specific" 限定

### Related Work
- Related Work 中本文实验数值已清理（Round 2 修复有效）
- 引用密度偏低，需补充上述引用

### Method
- Figure 1 placeholder 必须替换
- DisPeD 全称未给出
- α=0.3 的 ablation 结果已添加（Round 2 修复有效）
- frozen encoder 设计 justification 已添加（Round 2 修复有效）

### Experiments
- n=80 vs n=118 矛盾必须解释
- IID/OOD benign 样本来源和数量必须说明
- MLM-only IID 结果缺 std
- Table 3 应包含 ActorAttack 列或至少注明完整结果在 Table 4
- TF-IDF 确定性应标注
- Perturbation section 压缩为半页

### Discussion & Conclusion
- "variance reversal" 分析需前移至 Abstract/Contributions
- Encoder capacity confound 需在 Contribution 2 中添加限定

### Appendix & Checklist
- Checklist E2 license 模糊，建议指明具体 license
- Checklist 整体填写合理

### Format
- 页数需编译验证
- Figure 3 浮动位置需检查
