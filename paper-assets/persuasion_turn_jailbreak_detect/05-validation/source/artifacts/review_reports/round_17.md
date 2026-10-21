---
round: 17
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T18:08:41.214440+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 17 (Fresh)

**论文**: DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: 重新审稿 (fresh)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计方法论; R2: 新颖性+完整性+写作质量+framing）

---

## Summary

本文提出 DisPeD，一个两阶段 pipeline（Stage 1: encoder adaptation, Stage 2: frozen BiGRU）用于多轮 jailbreak 检测。在 Qwen3-8B 生成的合成数据上（350 训练、76-118 测试），通过 7 种 Stage-1 变体的 controlled ablation 分解影响 cross-attack 泛化的因素。主要发现：分类目标（包括打乱标签）足以实现模板攻击泛化（TOST confirmed, d < 0.1 on DD/FITD），域暴露是主要机制（MLM 弥合 ~60pp），benign distribution shift 可通过 10-25 条目标域对话缓解。Evidence hierarchy 在 ToxicChat 人类数据上完全反转（MLM > classification）。

---

## Strengths

- **S1 [共识]** 精心设计的 controlled ablation：7 种 Stage-1 变体在 frozen encoder 下公平对比，是该领域首个系统性 factorial study。通过固定 Stage-2 确保消融公平性。
- **S2 [共识]** Scrambled labels ≈ meaningful labels：TOST 在 DD/FITD 上确认等价（d < 0.1, n=10），对理解 encoder adaptation 机制有理论意义。
- **S3 [共识]** 统计方法论高于领域平均：paired permutation test, BCa bootstrap CI, TOST, McNemar's test，cross-seed pooled CI 明确标注为 exploratory。
- **S4 [共识]** 诚实报告 negative results：ToxicChat 反转、mixed-LLM 崩溃、RoBERTa-large 反转、Topic DAPT 失败均未回避。
- **S5 [共识]** 详尽附录（~18 页）：cross-checkpoint variance, TOST 灵敏度, CKA, benign adaptation curve, discriminative probe 等提供 mechanistic understanding。
- **S6** Benign adaptation 发现的实用价值：10-25 条目标域对话降 FPR 至 0-1.5%。
- **S7** 格式合规：正文 8 页，double-blind 正确，Limitations 和 Ethics Statement 齐全。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [critical, R1-N2 + R2-N2, 共识 AGREE]** Evidence hierarchy 在人类数据上反转——核心发现泛化性存疑

ToxicChat（唯一真实人类数据验证）显示 JB-MLM (0.837±0.013) >> 9-class (0.596±0.087)，evidence hierarchy 完全反转。论文在 Section 5 归因为 "condition-specific to multi-turn persuasion attacks" 并指出 77% 来自 FP，但两位 Reviewer 均认为：
- 解释过于笼统，缺少 per-category error analysis
- Classification objective 本身（scrambled=9-class）在 domain transfer 时有害，说明 discriminative compression 在合成→真实迁移中过度硬编码了合成数据的分布特征
- Conclusion 中 "classification DAPT via discriminative compression" 未充分限定 scope
- 核心 story 可能应从 "classification DAPT 最优" 重构为 "DAPT 效果高度依赖数据条件"

**MF2 [critical, R1-N1 + R2 AGREE]** OOD 评估中 IID benign 系统性夸大泛化能力

所有 OOD F1 数字（9-class DD = 0.994±0.005 等）受益于 benign 为 IID——模型仅需 attack-side 泛化。Abstract headline "F1 = 0.97–1.0" 未充分传达此限制。WildChat FPR=68.1%（Appendix）证实 benign-side shift 严重。Table caption 已有标注但 Abstract 缺少同等限定。建议 Abstract F1 数字后加 "(attack-side; benign IID)" 或类似短语。

**MF3 [critical, R2-N1]** "Any deterministic partition suffices" 与 Topic 变体失败的矛盾

论文 Abstract 和 Introduction 贡献 2 声称 "domain-relevant classification objectives—including scrambled labels—trigger discriminative compression sufficient for template-attack generalization"。但 Topic classifier 使用相同 jailbreak-domain 数据（5-class topic），DD F1 = 0.541±0.207。仅测试 1 种无效 + 3 种有效类型不足以支撑 "any" 泛化声明。10 random binary partitions（Appendix）提供部分缓解但不足。需收窄 claim 并将 Topic 失败机制分析提升到主文。

**MF4 [critical, R2-N3, R1 中等关注]** 新颖性有限

核心贡献 (a) 是 DAPT（Gururangan 2020）在新领域的应用——"classification supervision helps OOD" 不令人惊讶；(b) scrambled ≈ correct labels 受限于 template attacks（AA d=0.44），且 Zhang 2021 已有理论框架。Two-axis decomposition 概念上等价于 "FPR/FNR 需分别处理"。最令人惊讶的发现（ToxicChat 反转）反而削弱核心 story。R1 Excitement 3/5, R2 Excitement 2.5/5。若重构 story 为 "DAPT 效果的条件依赖性"——合成 vs 真实、小模型 vs 大模型、template vs structural attacks——novelty 可能更突出。

### Should-Fix（影响评分但不一票否决）

**SF1 [warning, R1-N3 critical → R2 REBUT → Director 降为 warning]** n=3 seeds 方差缩减 claims 统计可靠性

Population std (N divisor) 在 n=3 时有偏低估 22%。方差比值 F(2,2) CI 跨数个数量级。Introduction "substantially lower prediction variance" 在 n=3 下缺乏支撑。但论文已有 n=5 cross-hardware 验证、明确承认 "formal variance ratio tests are not applicable"、使用 "observed/associated" 措辞。**分歧记录**：R1 列 critical, R2 REBUT 降为 warning。Director 判定 warning——Introduction 措辞需降级为 "observed lower variance"。

**SF2 [warning, R2-W1]** "Disentangled" 命名误导

与 disentangled representation learning (β-VAE, Higgins 2017) 无关。Footnote 声明 "systematic disentanglement through ablation" 实质上就是 controlled ablation study。建议改 "Decomposed Pattern Detection" 或 "Factored Adaptation"。

**SF3 [warning, R2-W2]** 24.3× speedup 对比合理性

186M vs 8B 参数量差 43 倍——任何小 encoder 都比 LLM 快。CoT-optimized LLM baseline（DD 0.851, AA 0.885）大幅缩小差距但未在主文报告。建议定位为 "practical deployment cost comparison" 而非 contribution。

**SF4 [warning, R1-W1, R2 部分 REBUT]** Mean pooling ≈ BiGRU 对 multi-turn framing 的影响

检测基于 per-turn 表征均值聚合，不依赖时序。Section 5 已加 "Temporal dynamics are not exploited" 段落。R2 REBUT 认为 "multi-turn" 修饰 problem 而非 method，这本身是有价值的发现。**分歧记录**：R1 认为需更多讨论，R2 认为已充分。

**SF5 [warning, R2-W4]** Mixed-LLM AA=0.504 < majority baseline 未充分讨论

最接近真实部署条件下 DisPeD 实际失效。Abstract "remains robust under mixed-LLM training" 与正文 "preliminary" 矛盾（R1-W3, R2 AGREE）。Cross-LLM pilot 每 family n=10 证据薄弱（95% CI 下限 72.2%）。

**SF6 [warning, R2-W5]** RoBERTa-large DAPT 反转挑战核心 thesis

Vanilla RoBERTa-large AA = 1.000 vs 9-class 0.946——所有 continued pretraining 降低大模型性能。DAPT 效用 scale-dependent，论文仅在小模型充分实验。需在 Discussion 明确 DisPeD 适用范围。

**SF7 [warning, R1-W5 + R2 AGREE]** Discriminative compression 因果链不完整

所有证据（CKA, SVD, Fisher, probe）均为 correlational。替代解释：分类目标直接 memorize domain patterns。R2 认为 compression 和 memorization 可能互补。建议标注为 "consistent interpretation" 而非 "confirmed mechanism"。

**SF8 [warning, R1-W2 + R2 AGREE]** TOST δ=5pp margin 缺乏 practical significance 论证

安全关键应用中 5pp 可能意味数百额外成功攻击。AA n=10 时 δ=5pp 仍无法确认等价 (p=0.183)。需 domain-specific 论证为什么 5pp 是可接受 margin。

**SF9 [warning, R1-W4 + R2 AGREE]** 数据扩展 350→1000 混淆变量

改变了样本量和数据组成两个因素。"composition—not sample count" 因果表述过强。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识：

1. **[AGREE] ToxicChat 反转是论文最大弱点**（R1-N2 = R2-N2）：唯一人类数据验证推翻核心叙事，解释不够深入
2. **[AGREE] IID benign 夸大 OOD 数字**（R1-N1, R2 AGREE）：Abstract 需加 scope 限定
3. **[AGREE] Abstract 多处措辞需收紧**：mixed-LLM "remains robust"、F1 headline、"any partition"
4. **[AGREE] Discriminative compression 为 correlational**（R1-W5, R2 AGREE）
5. **[AGREE] 数据扩展因果表述过强**（R1-W4, R2 AGREE）
6. **[AGREE] Cross-LLM 证据太初步**（R1-W3, R2 AGREE）
7. **[AGREE] TOST margin 需论证**（R1-W2, R2 AGREE）

## Reviewer Divergence

1. **n=3 方差缩减 severity**：R1 列 critical（统计上不可靠），R2 REBUT 降为 warning（论文有 n=5 验证和谨慎措辞）。Director 判定 warning。
2. **Mean pooling ≈ BiGRU framing 影响**：R1 认为需更多讨论，R2 认为 Section 5 已充分且 "multi-turn" 修饰 problem 不修饰 method。
3. **Novelty severity**：R2 列 critical（DAPT 应用 + limited excitement），R1 Excitement 3/5 中等（scrambled label 有启发价值）。

---

## Questions

1. ToxicChat 上 JB-MLM > 9-class 的反转能否通过 per-category error analysis 分解？哪类样本导致 classification DAPT 劣势？
2. 论文已有 10-seed TOST 数据，为什么不以 10-seed 作为主文报告标准？
3. Mean pooling ≈ BiGRU 是否意味 per-turn classifier + majority vote 达到相当性能？
4. Population std (N divisor) 而非 sample std 的技术理由？
5. OOD 评估使用 OOD benign 时 variant 排序是否改变？（R1-Q5: 基于 WildChat FPR 数据推断很可能改变，9-class 不再最优）

---

## Missing References

**R2 建议（待核实真实性）**：
1. ADEPT (2025, arXiv:2510.10071) — continual pretraining 中 catastrophic forgetting 和 layer-specific adaptation 理论，与论文 layer-wise analysis 相关
2. Echo Chamber Attack (2026, arXiv:2601.05742) — 利用 completion/consistency bias 的多轮 jailbreak，与 Crescendo 不同
3. Representation Bending (2025, arXiv:2504.01550) — 表征修改增强安全性

**R1**: 未发现明显遗漏。

**R16 遗留**: 7 篇待核实引用（Yang et al. 2025 "Multi-Turn Jailbreaks Are Simpler Than They Seem", Souly et al. 2024 StrongREJECT, Li et al. 2024 inference-time intervention, Ke et al. 2023 continual pretraining 等）

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

状态：✅ done（耗时 ~4 分钟）

**Findings** (0 critical, 1 warning, 12 info):
- **[warning]** Page 16 密度过高：Figure 4 (CKA) + Figure 5 (t-SNE) + Table 12 + Table 13 四个 display items 挤在一页
- **[info]** Figure 2 柱状图分组较多，legend 字号偏小但可辨认
- **[info]** Figure 3 三面板热力图轴标签字号偏小
- **[info]** 首页无 display item，Figure 1 在 page 2（审稿人认知窗口内）
- **[info]** 全文 booktabs 风格统一，最优结果加粗，精度格式一致
- **[info]** 无 LaTeX 错误残留、margin 溢出或 section heading 孤悬
- **[info]** 参考文献格式统一，无未解析引用

---

## Overall Assessment

**Overall Score: 3.0 — Findings（可被 Findings 接收）**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | 3.25/5 |
| Excitement | 3/5 | 2.5/5 | 2.75/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**综合判断**：

这是一篇实验设计严谨、方法论扎实的 controlled ablation study。7 种 encoder adaptation 变体的系统分解和 scrambled label ≈ meaningful labels 的发现对社区有启发价值。统计方法论（TOST, BCa CI, permutation test）远超 NLP 安全领域平均水准。诚实报告 negative results 增强了可信度。

**Conference 接收的主要障碍**：

1. **ToxicChat 反转**（MF1）：唯一人类数据验证推翻核心叙事（classification DAPT > MLM），且缺乏深入的 error analysis。这是论文最大弱点——如果核心发现只在合成数据上成立，实际影响力受限。
2. **Overclaim**（MF2, MF3）：OOD 评估协议（benign IID）和 "any partition" 声称存在系统性乐观偏差。
3. **新颖性**（MF4）：核心方法（DAPT）非新提出，最有趣的发现（scrambled sufficiency）受限于 template attacks。

**Findings 接收的理由**：

- 系统性消融设计在该领域属首创
- Scrambled label 发现有理论意义
- Benign adaptation protocol 有实用价值
- 统计严谨度值得肯定
- 诚实报告 negative results

**如果作者修改的方向建议**（非处方性）：
- 将核心 story 从 "classification DAPT 是最优策略" 重构为 "DAPT 效果的条件依赖性"——合成 vs 真实、小模型 vs 大模型、template vs structural attacks
- 补充 ToxicChat per-category error analysis
- Abstract 和 Conclusion scope 限定系统性修正
- Discriminative compression 标注为 consistent interpretation

---

## Detailed Comments

### Abstract
- L7 "F1 = 0.97–1.0": 加 "(attack-side OOD; benign IID)" 限定
- L7 "remains robust under mixed-LLM training": AA=0.504 < majority baseline，改为 "partially preserves on template attacks" 或加限定
- L6 "domain-relevant classification objectives—including scrambled labels": 明确排除 misaligned objectives (topic)
- L9 "24.3× inference speedup": 标注 "deployment cost comparison; parameter counts differ by 43×"
- 信息密度仍偏高（5 个量化 claim），建议减至 2-3 个

### Introduction
- 贡献 2 "deterministic partition sufficiency": 收窄为 "domain-relevant partitions"，不能泛化为 "any"
- "substantially lower prediction variance": 降级为 "observed lower variance (n=3–5, directional)"

### Section 3 (Method)
- "Disentangled" 命名: 建议改 "Decomposed" 以避免与 disentangled representation learning 混淆
- Table 1 设计清晰有效

### Section 4 (Experiments)
- Section 4.1: IID/OOD 数据组成需一个简表概览（当前文字描述易混淆）
- Table 2-3: 统一标注 population std 且提示 Bessel-corrected 值 22% larger
- Figure 2: 建议加 error bars 与 Table 3 一致
- Section 4.2 Summary: user-turn 重叠分析和 turn-count baseline 是好的补充
- Section 4.5: "remains robust" 过度乐观，AA 实际失效
- Section 4.6: ToxicChat 分析需 per-category error breakdown

### Section 5 (Discussion)
- "Temporal dynamics are not exploited": 好的段落，但可进一步讨论在什么条件下时序可能重要
- "Condition-specific advantage": 需深化——分类目标为什么在 domain transfer 时有害？
- 建议新增 "Scale-dependent DAPT utility" 段落（RoBERTa-large 反转）
- "Two-axis decomposition" 而非 "framework"
- Discriminative compression: 标注为 "consistent interpretation" 非 "confirmed mechanism"

### Section 6 (Conclusion)
- "classification DAPT via discriminative compression": 加 "on synthetic multi-turn data" 限定
- "FPR 65–68% → 0–1.5%": 加 "preliminary, n ≤ 49/200" 限定

### Limitations
- 覆盖面尚可，已提及合成数据、single LLM、人类数据反转、benign adaptation 样本量
- 建议增加 DAPT scale-dependent 效用和统计功效限制

### Appendix
- 过长（~18 页）但内容实质性强
- Topic 失败机制分析（Table in Appendix）应提升到主文
- Benign adaptation curve 对理解核心发现重要，考虑在主文引用更多