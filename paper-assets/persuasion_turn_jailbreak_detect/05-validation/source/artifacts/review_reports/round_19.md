---
round: 19
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T11:31:12.246234+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 19 审稿报告 — DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection

**Venue**: EMNLP 2026 (ARR May 2026)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）

---

## Summary

本文提出 DisPeD，一个将 encoder adaptation（Stage 1）与 temporal classification（Stage 2, frozen BiGRU）分离的两阶段管线，通过 13 种编码器配置（7 个 DeBERTa-v3 变体 + RoBERTa-base/large 各 3 个）× 3 个模型规模（125M–355M）的因子化消融，研究什么因素驱动多轮 jailbreak 检测的跨攻击家族泛化。在合成数据上，classification-based DAPT 在 OOD 攻击检测中显著优于 MLM 和 vanilla encoder (F1=0.97–1.0 vs 0.26–0.31)；scrambled labels 在 template attacks 上与正确标签等效；benign-side few-shot adaptation 将 FPR 从 68.1% 降至 0%。但 evidence hierarchy 在唯一的人类数据验证（ToxicChat）上完全反转，mixed-LLM 训练下 ActorAttack F1=0.504 接近 majority baseline，且所有核心 OOD 评估的 benign 侧为 IID，系统性高估泛化能力。

---

## Strengths

**S1. 系统化消融设计是核心亮点**。7 个 Stage-1 变体精确控制单一变量（Table 1），每个变体有明确的因子分析目标。这种 controlled study 方法论在 jailbreak detection 文献中独特且有贡献。[R1-S1, R2-S1, AGREE]

**S2. Scrambled labels 等价性是非直觉且有价值的发现**。Scrambled labels 在 template attacks 上与正确标签等效（TOST confirmed, |d|≤0.14），暗示分类任务的表示压缩效应而非语义对齐驱动泛化。[R2-S2, R1 confirms in cross-response]

**S3. Negative findings 的诚实报告**。ToxicChat 反转（Table 5）、MLM collapse on mixed-LLM（Table 13）、RoBERTa-large DAPT 有害（Table 4）、temporal modeling 无效（Appendix T）——论文系统性报告了不利于主叙事的结果。[R1-S3, R2-S3, AGREE]

**S4. 多层次机制分析**。SVD decomposition（3/768 dims → perfect AA detection）、CKA similarity、Fisher ratio、layer-wise localization 从多角度 characterize 表征变化。SVD ablation（移除 top-3 方向后 DD 下降 17pp）是最接近因果证据的分析。[R1-S4]

**S5. 统计严谨性超过同领域多数论文**。Bootstrap CIs、permutation tests、TOST 等价性检验、seed-level results（Table 8）、10-seed validation。关键 caveat（bootstrap independence, n=3 limitation）在正文中明确标注。[R2-S6, R1-S5]

**S6. Benign-side few-shot adaptation 有实用价值**。10–25 条 target-domain benign conversations 将 FPR 从 58–68% 降至 0–1.5%，无需 target-domain 攻击数据。[R2-S4]

---

## Weaknesses

### Must-Fix（影响接收决定，6 项，两位 Reviewer 全部达成共识）

**MF1. ToxicChat evidence hierarchy 完全反转，但 Abstract/Conclusion 未充分反映** [R2-N1, R1 AGREE]
- Table 5: JB-MLM (0.837±0.013) >> 9-class (0.596±0.087)，差距 24.1pp
- Abstract 仅以 "indicating condition-specific rather than universal mechanisms" 一句带过
- 论文核心叙事 "classification DAPT > MLM > vanilla" 仅在合成数据上成立
- **共识要求**: Abstract/Conclusion 将 ToxicChat 反转作为同等重要的 finding 呈现；所有核心 claim 显著限定 "on synthetic data"；讨论反转原因（synthetic vs human? single-turn vs multi-turn?）

**MF2. "OOD" 评估中 benign 侧为 IID，系统性高估泛化能力** [R1-N2, R2-N2, mutual AGREE]
- Table 2 核心 OOD F1 (>0.99) 中 benign 样本来自训练分布（IID），FPR≈0
- WildChat dual-OOD: FPR=68.1%, F1 drops 12–14pp（Appendix P.1 Table 22: DD 0.994→0.855, AA 0.981→0.842）
- 关键数据被埋在 Appendix，正文核心结果表造成高估第一印象
- **共识要求**: Table 2 增加 dual-OOD 行（"without/with benign adaptation"）；区分 "cross-attack generalization (IID benign)" vs "full OOD generalization"；Abstract/Conclusion 数字附带适用条件

**MF3. Mixed-LLM ActorAttack F1=0.504 ≈ majority baseline，定性不当** [R2-N3, R1 AGREE]
- 0.504±0.107 与 balanced majority baseline (~0.5) 不可区分
- 0.504 vs vanilla 0.389 差异在 std=0.107 下统计不显著（n=3, t-test 无法 reject H₀）
- 论文仍声称 "classification supervision generalizes across LLM sources"
- **共识要求**: 标注为 preliminary/exploratory; 报告 majority baseline 对比; Abstract/Conclusion 限定为 template attacks only

**MF4. ActorAttack padding 实验暴露严重长度依赖** [R1-N3, R2 AGREE]
- Benign 12–20 turns vs jailbreak 3–10 turns 完全不重叠
- Appendix U Part C: DD padded Δ=−2.5pp (resilient) vs AA padded Δ=−57.9pp (catastrophic)
- 论文三个反驳论据均不充分（vanilla 长度论据、K=1 论据、OOD 长度不可学论据）
- DD vs AA 的 55.4pp 差异暗示 AA 检测可能部分依赖长度信号或 signal-to-noise ratio
- R2 补充分析: mean pooling≈BiGRU 说明信号被均值化稀释是架构固有脆弱性
- **共识要求**: 构造长度匹配对照数据；Section 5 prominently 讨论 AA padding collapse 对 "discriminative compression" 叙述的影响

**MF5. Bootstrap CI 跨 seed 池化违反独立性假设** [R1-N1, R2 AGREE]
- 3 seeds 共享训练数据和架构，predictions 存在结构性相关
- 池化后有效样本量膨胀约 3 倍，CI 系统性过窄
- 论文虽标注 "exploratory"，但多处基于池化 CI 做断言性声明（"confirms non-overlapping intervals"）
- R2 缓解: seed-level F1 表显示核心排序结论在每个 seed 独立成立
- **共识要求**: seed-level metrics 为主要报告单位；"confirms" → "seed-level results show consistent separation"；所有池化 CI 标注 "exploratory"

**MF6. 方差缩减声明 (3–23×) 基于 n=3 seeds 统计不可靠** [R1-N4, R2 AGREE]
- n=3 方差比只有 2 自由度，3–23× 可能与 1× 统计不可区分
- ToxicChat 上方差方向反转（classification std=0.087 > MLM std=0.013）
- **共识要求**: 降级为 "descriptive observation, pending validation with more seeds"；附带 ToxicChat 反转限定

### Should-Fix（影响评分，10 项）

**SF1. 方法新颖性有限** [R2 Overall, R1 no objection]
核心贡献是 DAPT (Gururangan et al., 2020) 应用于安全检测——已知技术的领域确认。Pipeline (DeBERTa+frozen BiGRU) 与 DeepContext 架构等价（作者自认）。消融发现集合（scrambled equivalence、MLM fragility、discriminative subspace）有增量贡献，但整体不构成原创方法论突破。

**SF2. "Disentangled" 命名不准确** [R2-W1, R1 AGREE]
ML 社区 "disentanglement" 有特定技术含义（β-VAE 等），论文实际做的是 controlled ablation。建议改为 "Decomposed" 或 "Dissected"。

**SF3. "Structural complexity" 缺乏形式化定义** [R2-W2, R1 AGREE]
Contribution 2 区分 "template attacks" vs "structurally complex attacks" 但未给出操作化定义。读者无法判断新攻击属于哪一类。建议给出可量化 proxy（策略转换熵、对话轮数方差）。

**SF4. 因果语言 vs 相关性证据不一致** [R2-W5 = R1-W6, mutual AGREE]
"Domain exposure is the primary mechanism" 等因果表述应替换为 associational 语言。SVD ablation 接近因果但不充分。R1-Q6 深入质疑: 低 participation ratio 可能是 overfitting/collapse 而非 discriminative compression，WildChat 68.1% FPR 是直接证据。

**SF5. RoBERTa-large DAPT 有害的 scale-dependent 发现在 Abstract/Conclusion 缺失** [R2-W6, R1 AGREE]
RoBERTa-large vanilla AA=1.000 vs 9-class 0.946——DAPT 在大 encoder 上可能有害。实践者需要知道 DAPT 不是 universally beneficial。需加 "at base model scale" 限定。

**SF6. Temporal modeling negative finding 讨论不充分** [R2-W7, R1 AGREE with nuance]
Mean pooling≈BiGRU 暗示不利用时序结构，与 "multi-turn" 叙事矛盾。讨论对 multi-turn defense 研究方向的启示。R1 nuance: 核心贡献是 Stage-1，但 finding 本身值得主文讨论。

**SF7. 缺乏与已发表 encoder-based 方法的直接实验对比** [R1-W1, R2 AGREE]
DeepContext/BIID/G-Guard 均无实验对比。BERT-base proxy 只匹配参数量。至少在 ToxicChat 上与一个已发表方法对比，或明确论证不可行原因。

**SF8. Abstract 信息密度过高** [R2-W4, R1 AGREE (低优先级)]
~250 词含 12+ 数值。建议精简至 ~180 词保留 2-3 个关键数字。

**SF9. 单一 LLM (Qwen3-8B) 数据泛化性受限** [R1-W3, R2 AGREE]
Mixed-LLM 实验反而暴露更大问题（AA=0.504）。ToxicChat 是单轮，无法验证多轮 claim。

**SF10. 数据规模与声明强度不匹配** [R1-W5, R2 AGREE]
350 训练 + 76–118 OOD 测试。R2 公平指出该规模在领域内并非异常，但声明校准应与证据强度匹配。

---

## Reviewer Consensus [AGREE]

所有 6 个 Must-Fix 均达成完全共识。两位 Reviewer 核心关切高度重合：

1. **Claim calibration 是最大问题**: 论文核心 claim (classification > MLM for OOD) 在合成数据上成立，但 (a) ToxicChat 完全反转, (b) OOD 评估 benign-IID 高估, (c) mixed-LLM AA ≈ chance, (d) DAPT 在大 encoder 有害。Abstract/Conclusion 的表述强度与证据支撑严重不匹配。
2. **长度混淆未排除**: AA padding collapse −57.9pp 是系统性问题，缺乏长度匹配对照。
3. **统计基础不足**: bootstrap CI 池化 + n=3 方差声明缺乏效力。

## Reviewer Divergence [REBUT]

仅两个 Should-Fix 级别的分歧，均非关键：

1. **TOST δ=5pp 合理性** (R1-W2 vs R2 REBUT): R1 认为需论证 δ 选择，R2 认为 sensitivity analysis (δ=2pp 仍通过) + Cohen's d 已提供充分独立证据。**结论**: R2 的 rebuttal 有效，此问题不升级。

2. **两轴分解 = FPR/FNR 重包装** (R2-W3 vs R1 REBUT): R2 认为是标准 FPR/FNR 分析的重包装，R1 认为 IID/OOD 维度叠加使框架超越简单 FPR/FNR——不同失败模式需不同缓解策略的分析框架有独立价值。**结论**: 分歧保留，建议论文增加说明段落。

---

## Questions

1. **Benign adaptation 评估协议**: 10 WildChat conversations → FPR 0% 是 IID 还是 OOD 评估？如果 adapt 和 eval 同分布，则实用性被高估。实现细节（Stage-1 还是 Stage-2? loss? epochs?）缺失。[R2-Q1, R1-Q5]
2. **Scrambled permutation**: 固定 permutation 还是随机重采样？是否在多个 permutation 上验证？[R2-Q2]
3. **ToxicChat 反转的归因**: 同时变化两个因素（human vs synthetic + single-turn vs multi-turn），无法区分反转原因。Appendix 的 truncation 实验是否可以帮助归因？[R2-Q3]
4. **Mixed-LLM confound**: 500 total vs 350 single-source, 性能下降是 multi-source shift 还是 per-source 数据量减少？[R2-Q4]
5. **DAPT = "多看一遍数据"?**: Wiki MLM 与 JB-MLM 在 DD 上仅差 1pp (0.904 vs 0.914)——大部分收益来自通用 continued pretraining 还是 jailbreak-specific 特征学习？[R1-Q3]
6. **Discriminative compression vs representation collapse**: Fisher ratio 低 participation ratio 是有益特征选择还是 overfitting？WildChat 68.1% FPR 是否是 collapse 的直接证据？[R1-Q6]
7. **AA padding collapse 机制**: DD Δ=−2.5pp vs AA Δ=−57.9pp——为什么差异如此大？是 signal density 差异还是 length shortcut？[R1-Q2]

---

## Missing References

两位 Reviewer 共推荐 7 篇缺失引用：

**R2 推荐（5 篇）**:
1. Recursive Language Models for Jailbreak Detection (arXiv 2602.16520, 2026) — 直接相关
2. TrajGuard: Streaming Hidden-state Trajectory Detection (arXiv 2604.07727, 2026)
3. Do Internal Layers of LLMs Reveal Patterns for Jailbreak Detection? (arXiv 2510.06594, 2025) — 与 SVD/Fisher 分析方法论高度相关
4. Jailbreaking Leaves a Trace (arXiv 2602.11495, 2026) — 与 representation-level detection 直接相关
5. M2S: Multi-turn to Single-turn Jailbreak (arXiv 2503.04856, 2025)

**R1 推荐（2 篇）**:
6. Markov et al., 2023 "A holistic approach to undesired content detection" — OpenAI production system
7. Phute et al., 2024 "LLM Self-Defense" — 替代检测范式

---

## External Review

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 16 info）。

**Warnings**:
- **Page 5**: Figure 2 柱状图 x 轴标签字号偏小，打印/缩放阅读时可读性边缘。建议增大字号或缩短标签。
- **Page 8**: 极度拥挤——Table 5 + Section 4.7/4.8/4.9 + Discussion + Conclusion 全在一页。Conclusion 仅 6–7 行，审稿人可能感觉草草收场。建议压缩 4.7–4.9 或移至 appendix。

**Info highlights**:
- Figure 1 架构图全宽展示，清晰度良好
- Tables 使用 booktabs 风格贯穿全文，格式一致
- 数字精度统一（3 位小数），最优值加粗标注
- Limitations 篇幅适中，Ethics Statement 简洁合规
- 未发现 margin 溢出、未解析引用、排版问题

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Soundness**: 3/5
**Excitement**: 2.75/5
**Reproducibility**: 4/5
**Confidence**: 4/5

本文是一项实验设计严谨的 controlled study，回答了一个有价值的研究问题。13 配置消融在 jailbreak detection 文献中独特，scrambled labels 等价性和 MLM mixed-LLM collapse 等发现有方法论贡献。统计处理（bootstrap CIs、TOST、permutation tests）超过同领域多数论文。Negative findings 报告诚实透明。

三个核心问题阻碍 Conference 推荐：

1. **Core claim 泛化性不足**: Evidence hierarchy (classification > MLM > vanilla) 仅在合成数据上成立，在唯一人类数据验证上完全反转。所有 OOD 评估 benign-IID 高估泛化。Mixed-LLM 下最具挑战性条件 F1 ≈ chance。综合起来，论文的 claim strength 与证据支撑严重不匹配。

2. **方法新颖性有限**: 核心是 DAPT (Gururangan 2020) 的领域应用确认，pipeline 与 DeepContext 架构等价。消融发现集合有增量价值但不构成原创突破。

3. **评估协议系统性偏差**: Benign-IID OOD 评估、长度分布不重叠 + AA padding collapse、n=3 统计效力——多层评估问题限制了定量 claim 精度。

所有问题均可修复：claim 校准到 "on synthetic data at base scale"、dual-OOD 指标上移到正文、长度匹配对照、更多 seeds。修复后论文 claim 强度会显著降低（从 "classification DAPT is the mechanism" 降为 "classification DAPT helps on synthetic data at base scale"），但消融框架的方法论贡献仍足以支撑 Findings 接收。修复充分后有 marginal 提升至 3.5 的空间。

---

## Detailed Comments

### Section-by-Section

**Abstract** (p1): 信息密度过高（~250 词, 12+ 数值）。"indicating condition-specific rather than universal mechanisms" 严重低估 ToxicChat 反转的影响。所有 OOD F1 数字需标注 "(attack-side OOD, benign IID)"。Mixed-LLM 和 speedup claim 需限定条件。建议精简至 ~180 词。

**Introduction** (p1-2): Contribution 1 中 "classification DAPT recovers OOD detection" 需加 "on synthetic data at base model scale"。Contribution 2 的 "observed difficulty gradient" 定位合理但 "structural complexity" 未定义。Contribution 3 的 "24.3× inference speedup" 是 deployment cost comparison，非 apples-to-apples 方法论对比（184M vs 8B params），需明确标注。

**Method** (p3-4): 设计清晰，7 个变体的因子化消融合理。Table 1 自包含性好。Scrambled variant 的 permutation 固定 vs 随机未说明。κ=0.78 (n=50) 的标注质量对 9-class DAPT 的解释有影响，但 scrambled 等价性矛盾地降低了此问题严重性。

**Experiments** (p4-8): 核心实验执行质量高。Table 2–5 格式统一。关键建议：Table 2 增加 dual-OOD 行；Section 4.3 "is the primary mechanism" 改为 associational；Section 4.5 的 0.504 需对比 majority baseline 和报告显著性；Section 4.9 的 few-shot adaptation 需补充实现细节。

**Discussion** (p8): 被压缩到页面底部（视觉审查 warning）。缺少对 AA padding collapse 的讨论。"discriminative compression" 需增加 overfitting/collapse 替代解释。DAPT scale-dependent 效用需明确。Temporal modeling negative finding 的 implication 需讨论。

**Conclusion** (p8): 仅 6–7 行，过于简短。"the hierarchy reverses on human data, confirming condition specificity" 低估了反转的严重性。需增加 scale-dependent 限定。

**Limitations** (p9): 覆盖面合理（synthetic data、IID benign、benign adaptation 样本量、cross-LLM shift）。篇幅适中。

**Appendix** (p12-24): 内容丰富，证据链完整。特别有价值：seed-level F1 (Table 8)、TOST sensitivity (Table 16)、dual-OOD analysis (Table 22)、SVD ablation (Table 29)。建议将 Table 22 (dual-OOD) 和 Table 32 Part C (padding collapse) 的关键数据上移到正文。