---
round: 1
overall_score: weak reject
timestamp: 2026-05-18T08:54:32.586869+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 1

**论文**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap
**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)
**截止日期**: 2026-05-25
**审稿组**: Reviewer 1（方法严谨性 + 实验有效性）、Reviewer 2（新颖性 + 完整性 + 写作质量）
**收敛状态**: Round 1 完成，关键问题已达成共识，无需 Round 2

---

## Summary

论文提出 DisPeD，一个两阶段多轮 jailbreak 检测框架，通过 7 个 Stage-1 encoder 变体系统分解跨攻击泛化的机制。核心发现：continued pretraining（MLM）是桥接 OOD gap 的主要机制（vanilla 0.28 → MLM 0.91±0.12），classification supervision 提供额外稳定性（9-class 0.997±0.005）。论文据此将多轮 jailbreak 检测重新定位为 domain adaptation 问题。

---

## Strengths

**S1** [共识] 研究问题有价值且定义清晰。"What representation properties enable cross-attack generalization?" 是多轮 jailbreak defense 领域的 under-explored question，从 representation learning 角度系统分析而非追求 SOTA 数字。

**S2** [共识] 7 变体消融设计是论文最大亮点。每个变体精准隔离一个因素（domain exposure, classification supervision, label quality, label granularity, domain specificity），Table 1 展示了清晰的实验逻辑。这种 controlled decomposition 的方法论本身对社区有参考价值。

**S3** [共识] 诚实的科学态度。论文坦承 MLM 无标签即可桥接大部分 OOD gap，坦承 TF-IDF 达 0.944，坦承单 seed 变体的局限性。

**S4** [共识] 与 domain-adaptive pretraining 文献的良好连接。核心发现与 Gururangan et al. (2020) 一致，将 jailbreak detection 重新定位为 domain adaptation 问题有理论深度。

**S5** [共识] AI 写作痕迹控制良好。全文无 em-dash 滥用，无 delve/leverage/utilize 等 AI 高频词（仅一处 "additionally"），叙事连贯。

---

## Weaknesses

### Must-Fix（5 项，两位 Reviewer 均标记为 critical 且达成共识）

**MF1** [R1-N1, R2-N4] **Evidence hierarchy 统计基础不一致：binary/scrambled 仅 seed 42**
- 论文核心 evidence hierarchy 混合了 3-seed 和 single-seed 结果。binary 和 scrambled 的 F1=0.990 来自 seed 42 单点估计，无方差信息。
- 论文从中推导因果性 claim："Label quality and granularity are non-factors for detection"（Section 4.4）、"classification objective functions as a regularizer"（Section 4.4）。这些 claims 建立在两个 single-seed 数据点的巧合相等上。
- topic 变体的高方差（0.54±0.21，seed 123 低于 vanilla）证明某些变体在不同 seeds 下可能极不稳定。如果 binary/scrambled 出现类似方差，evidence hierarchy 中间层将坍塌。
- **修复要求**：所有 7 个变体必须报告相同的 3-seed（或更多）mean±std。

**MF2** [R1-N2, R2 交叉同意] **Three-layer robustness attribution 在 n=76 上缺乏统计显著性**
- Δ=2.6pp ≈ 2 个样本差异，Δ=5.3pp ≈ 4 个样本，Δ=9.2pp ≈ 7 个样本。无 McNemar's test、bootstrap CI 或 permutation test。
- 论文自身承认 "tier boundaries correspond to 1-3 misclassifications"（Section 4.3），但未降级 claim 强度。Three-layer attribution 是 Introduction Contribution #2 的核心，占正文约 1/3 讨论。
- **修复要求**：(1) 扩大 perturbation test set 至 n≥300，或 (2) 报告统计显著性检验，或 (3) 将 three-layer attribution 降级为 "observed pattern" 并大幅削减讨论篇幅。

**MF3** [R1-N3, R2-N2] **缺少与已发表 multi-turn defense 系统的直接实验对比**
- 论文在 Related Work 定位 DeepContext、BIID、G-Guard、SafeDream 为 direct competitors，声称它们 "do not decompose what enables cross-attack generalization"（Section 1）。但 Experiments 无任何头对头比较。
- 实际 baselines 仅为 vanilla DeBERTa（论文自身 ablation）、TF-IDF LR、LLM-as-judge（仅测 IID）。
- R2 补充：vanilla variant 本身可视为 DeepContext 的近似复现（pretrained encoder + RNN, 无 domain adaptation），应在讨论中显式建立联系。
- **修复要求**：至少复现 DeepContext 在相同数据上的结果。

**MF4** [R1-N4, R2-N1] **数据集规模过小，所有核心 claims 的统计分辨率不足**
- 500 训练、160 OOD 测试、76 perturbation，全部由 Qwen3-8B 合成生成。
- n=80 DD 上每个 misclassification 改变 F1 约 1.25pp。区分 0.990 和 0.997（差 0.7pp）在统计上无意义。
- jailbreak-MLM vs wiki-MLM 在 full length 仅差 1pp（0.914 vs 0.904），但论文基于此讨论 domain specificity。
- 论文的 "reframe multi-turn jailbreak detection as primarily a domain adaptation problem" claim 的证据强度与 claim 广度严重不匹配。
- **修复要求**：扩大数据集规模和来源多样性，或显著降低 claim 强度并限定为 preliminary findings on synthetic data。

**MF5** [R2-N3, R1-W6→交叉升级为 critical] **有效 OOD 评估实质上是 single-dataset**
- FITD 在几乎所有变体和 prefix 长度上 F1≥0.990（含 vanilla），对方法无区分度。
- 7 变体消融分析实质上只在 DD 一个 OOD attack type 上有效。DD 可能有特殊属性（emotion-based manipulation 风格），使当前发现不具普遍性。
- "cross-attack generalization" 的 claim 仅由单一 OOD attack type 支撑，外部效度严重不足。
- **修复要求**：增加至少 2-3 个难度适中的 OOD attack types（ActorAttack, PAIR 等）。

### Should-Fix（12 项）

**SF1** [R1-W1, R2-W6] Mean pooling = BiGRU 结论基于 single seed (42)，在 n=80 上 1.000 vs 0.997 统计上无意义。"detection relies on per-turn representations rather than their sequential order" 的强因果 claim 缺乏充分支撑。如果 mean pooling 一致优于 BiGRU，Stage-2 BiGRU 的架构选择缺乏 motivation。需报告 3-seed 多变体结果。

**SF2** [R1-W2] 策略标注质量验证不充分。Qwen3-8B 标注，κ=0.78，人工验证仅 n=50（每类约 5-6 样本）。three-layer attribution 中 "correct labels" 的优势直接依赖标注质量。建议增加人工验证至 200+，报告每类 κ 或 confusion matrix。

**SF3** [R1-W3] LLM-as-judge baseline 仅测 IID，未测 OOD。论文核心贡献是 OOD generalization，虽然 IID 已严重失败（GPT-5.5 F1=0.191-0.449），但 OOD 结果应报告以加强 "content-level reasoning is insufficient" 的 claim。

**SF4** [R1-W4, R2-W4] TF-IDF LR 强表现未被充分讨论。DD-Full 0.944，perturbation 仅降 1.3pp。TF-IDF robustness 远好于 vanilla/wiki-MLM（~12pp），接近 MLM-only（2.6pp）。这质疑了 "domain-adaptive pretraining captures pragmatic features" 的机制性解释——也许模型只在捕捉词汇统计差异。建议增加 probing/attention 分析验证。

**SF5** [R1-W5] 可复现性不足。Stage-2 缺 learning rate/batch size/optimizer/warmup；数据生成 pipeline 和策略标注 prompt 未提供；无代码/数据发布承诺。建议在 Appendix 补充完整超参数表和 prompt。

**SF6** [R2-W1] Abstract 过度堆砌数据（约 180 词含 ~10 个 F1 数字），读起来像压缩版 Results。建议保留 2-3 个关键数字（vanilla 0.28, MLM ≥0.97, 9-class 0.997），聚焦叙事弧。

**SF7** [R2-W2, R1 AGREE with nuance] "partially falsified our original hypothesis" 叙事策略对审稿人接收判断有负面影响。R1 认为科学诚实值得肯定但修辞效果不佳。建议正面框架叙事 + Discussion 中保留假设修正过程。

**SF8** [R2-W3] Contributions 列表过于密集（两条各 60-80 词）。第二条试图在单 bullet 中描述 three-layer attribution 的完整结构。建议拆为 3-4 条简短 bullets，每条 30-40 词。

**SF9** [R2-W5] Strategy Trajectory Analysis (Figure 3) 使用 ground-truth labels（Qwen3-8B 标注）而非模型预测。如果 9-class 模型在 OOD 上策略预测准确率低，"interpretability through strategy trajectories" 这一 contribution 不成立。必须补充 OOD 策略预测准确率。

**SF10** [R2-W7] Limitations 作为 `\paragraph{Limitations and future work.}` 嵌入 Conclusion，不符合 ACL/ARR 独立 `\section{Limitations}` 的格式要求。需拆分为独立 section。

**SF11** [R2-REF1, R1 交叉同意] 缺失关键引用方向：(1) computational persuasion detection 实证工作（SemEval propaganda detection tasks），(2) adversarial NLP robustness 基础文献（TextFooler, BERT-Attack），(3) probing classifiers（Hewitt & Manning 2019, Belinkov & Glass 2019）。覆盖方向的缺失比引用总量更重要。

**SF12** [R1 小问题, R2 小问题] 图表问题：Fig 1 Stage 1/Stage 2 标题重叠、"Frozen [CLS]" 位置拥挤；Fig 3 轴标签字体偏小（已使用 `figure*` 但仍需增大字体）。部分引用 year 不一致（chao2023pair 2023 vs 正式发表 2025）。缩写 "pp" 未定义。缺少各变体计算成本信息。仅用 user turns 的假设需更多讨论。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：
1. binary/scrambled 必须补充 multi-seed 结果（MF1）
2. three-layer attribution 缺乏统计显著性检验（MF2）
3. 必须增加 multi-turn defense baseline 对比（MF3）
4. 数据集规模不足以支撑核心 claims（MF4）
5. FITD 无区分度导致 OOD 评估实质上是 single-dataset（MF5）
6. TF-IDF 的强表现质疑 pragmatic features 的机制性解释（SF4）
7. Strategy trajectory analysis 应使用模型预测而非 ground-truth（SF9）
8. Limitations 格式需修改为独立 section（SF10）
9. 三个方向的引用覆盖缺失（SF11）

---

## Reviewer Divergence

仅一处修辞偏好分歧，非实质性矛盾：
- **"partially falsified" 叙事**：R1 认为科学诚实值得肯定（列为优势），R2 认为对审稿人接收判断有负面影响（列为 should-fix）。R1 在交叉回应中 AGREE with nuance：可正面框架叙事同时在 Discussion 中保留假设修正过程。

---

## Questions

1. binary/scrambled 仅报告 seed 42 的原因是什么？是计算资源限制还是其他原因？
2. 9-class 模型在 OOD (DD/FITD) 数据上的策略预测准确率是多少？
3. 论文声称 "pragmatic features (hedging, escalation markers, topic-shifting patterns)" 是 DAPT 捕获的特征，有什么直接证据（如 probing 实验、attention 分析）？
4. 为什么不 end-to-end fine-tune Stage 1 + Stage 2？冻结 Stage 1 的设计选择基于什么实验或理论依据？
5. assistant responses 是否可能包含有用的检测信号（如 refusal patterns, compliance indicators）？仅用 user turns 的决策是否经过实验验证？
6. 如果 mean pooling 一致优于 BiGRU，Stage-2 的 BiGRU 设计 motivation 是什么？

---

## Missing References

1. **Computational persuasion detection**：SemEval propaganda detection shared tasks (Da San Martino et al., 2019; Dimitrov et al., 2021)
2. **Adversarial NLP robustness**：TextFooler (Jin et al., 2020), BERT-Attack (Li et al., 2020)
3. **Probing classifiers**：Hewitt & Manning 2019, Belinkov & Glass 2019
4. 部分引用条目 year 不一致需核实（chao2023pair, austin1962speechacts, han2024wildguard）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，跳过。

---

## Overall Assessment

**评分: Weak Reject (2/5)**
**置信度: 4/5**

论文提出了一个有价值的研究问题（什么使跨攻击泛化成为可能），7 变体消融的实验设计思路优秀，核心发现（domain adaptation 是主要机制）有理论意义。但当前版本存在 5 项 critical 问题的联合效应严重：

1. **统计可信度不足**：binary/scrambled 单 seed、n=76 三层归因无显著性检验、n=80 上精细排序无统计意义
2. **评估范围不足**：有效 OOD 仅 DD 单数据集，缺少与 SOTA multi-turn defense 的直接对比
3. **Claim 强度与证据不匹配**："reframe multi-turn jailbreak detection as primarily a domain adaptation problem" 基于 500 条合成对话和单一 OOD attack type

R1 评分 2/5（Resubmit），R2 评分 2.5/5（Borderline Findings）。综合判断：weak reject。如果 (1) 所有变体补充 multi-seed 结果，(2) 增加 2-3 个 OOD attack types，(3) 至少复现 DeepContext 作为 baseline，(4) 补充统计显著性检验或降级 three-layer attribution claims，论文有望在下一个 ARR cycle 达到 accept 水平。当前版本更适合 Findings track（如果降低 claim 强度并补充关键实验）。

---

## Detailed Comments

### Abstract
- 约 180 词，在范围内，但数字过密（~10 个 F1 值 + 2 个 std）。建议保留 3 个关键数字，其余移入正文。
- "pp" 缩写未定义。

### Introduction
- "partially falsified our original hypothesis" 叙事有科学价值但对接收不利，建议正面重构。
- Contributions 列表过于密集，建议拆为 3-4 条。
- Evidence hierarchy 在 Introduction 中完整呈现（含 6 个 F1 值），信息过载。

### Related Work
- 结构清晰，5 个 paragraph 覆盖 attacks/defenses/production systems/discourse/DAPT。
- "none systematically analyze why" 的 gap 声明过强，建议温和化为 "provide limited insight into which representation properties drive cross-attack generalization"。
- 缺失 3 个引用方向（propaganda detection, adversarial robustness, probing classifiers）。

### Method
- 7 变体设计逻辑清晰，Table 1 是论文最佳表格。
- 策略标注质量验证不足（κ=0.78, n=50）。
- 仅用 user turns 的假设合理但需更多讨论。

### Experiments
- 核心问题：数据规模、seed 不一致、单 OOD 数据集、缺 baseline 对比。
- Three-layer robustness attribution 的 claim 强度需大幅降级。
- Figure 3 使用 ground-truth labels 而非模型预测，不支撑 interpretability claim。
- Mean pooling 实验仅单 seed，与 BiGRU 架构选择矛盾。

### Conclusion
- Limitations 需拆为独立 section（ACL/ARR 格式要求）。
- 论文诚实承认多项局限但未在主体 claims 中做对应降级。

### Figures
- Fig 1: Stage 1/Stage 2 标题重叠，"Frozen [CLS]" 拥挤，需调整 layout。
- Fig 2: 清晰展示 prefix-length trajectory，是有效的可视化。
- Fig 3: 轴标签字体偏小，strategy 名称难辨认。应使用 ground-truth + 模型预测的对比版本。

### References
- 31 条（bib 头注释 31，实际可能略多），覆盖基本到位但 3 个方向缺失。
- 部分 year 不一致需核实。