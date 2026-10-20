---
round: 2
overall_score: weak reject
timestamp: 2026-05-18T16:07:47.224876+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告（Round 2）

**论文**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**审稿模式**: 重新审稿（fresh review，无 Round 1 记忆）
**Reviewer 编排**: 2 人（EMNLP 标准）
- Reviewer 1: 方法严谨性 + 实验设计 + 统计有效性
- Reviewer 2: 新颖性 + Related Work 定位 + 写作质量 + 完整性

---

## Summary

本文提出 DisPeD，一个两阶段框架（Stage-1 encoder adaptation + Stage-2 BiGRU aggregation），通过 7 个受控 Stage-1 变体系统分解跨攻击泛化的机制。核心发现：(1) 在 DeBERTa-v3 上 continued pretraining（MLM）桥接约 60pp OOD gap；(2) 分类监督（9-class/binary/scrambled 三种分类变体检测 F1 相同）作为 representation regularizer 而非 semantic classifier 起作用；(3) RoBERTa 交叉验证显示 encoder pretraining method 决定 domain adaptation 变为必要的难度阈值。实验在 Qwen3-8B 合成数据上覆盖 4 个攻击家族（Crescendo IID + FITD/DD/ActorAttack OOD），规模为 500 训练 + 76-118 测试对话。

---

## Strengths

**S1** [共识] **消融实验设计系统严谨**。七个 Stage-1 变体各自隔离一个因素（domain exposure, classification supervision, label quality, label granularity, domain specificity, misaligned supervision），共享相同 Stage-2 pipeline，使对比公平。这是论文最突出的方法论贡献。

**S2** [共识] **Scrambled labels 发现有洞察力**。Scrambled = binary = 9-class 在检测 F1 上完全相同（0.997±0.005, Table 2），证明分类目标作为 representation regularizer 而非 semantic classifier 起作用。这超越了简单的 domain adaptation 验证。

**S3** [共识] **Cross-encoder "difficulty threshold" 概念有价值**。DeBERTa-v3 vanilla 在 DD 上坍塌（F1=0.312）而 RoBERTa vanilla 不坍塌（0.981），但 RoBERTa 在结构更复杂的 ActorAttack 上坍塌（0.466），揭示 encoder pretraining method 决定了 adaptation 变为必要的难度阈值（Table 4）。

**S4** [共识] **诚实的 Limitations section**。论文坦率承认 TF-IDF 基线问题、strategy prediction 不泛化（OOD κ=0.126）、数据规模限制、single-seed mean pooling 等。这种 intellectual honesty 在 ML safety 论文中罕见。

**S5** [共识] **可复现性优秀**。完整超参数（Appendix E）、总计算成本 <4 GPU-hours、承诺开源。

---

## Weaknesses（按 severity 排序）

### Must-Fix（7 项 critical，影响接收决定）

**N1** [critical, 共识] **单模型（Qwen3-8B）生成全部数据造成系统性 confound**
- Qwen3-8B 同时用于生成训练数据、策略标注、OOD 测试数据和对抗性 paraphrase。TF-IDF LR 在 OOD DD 上 F1=0.944（Table 1），强烈暗示模型利用的是 Qwen3-8B stylistic fingerprint 而非 discourse-level features。论文在 Limitations 中讨论了 lexical separability 但完全未提及 single-LLM confound。
- **影响**：如果 OOD gap 的桥接主要来自学习生成模型的 stylistic artifacts，则整个 evidence hierarchy 可能是 artifact-driven。这是论文最核心 claim 的替代解释。
- **修复方向**：(1) 用不同 LLM 生成部分 OOD 数据；(2) 用人类编写数据（MHJ dataset）评估；(3) 做 probing 实验区分 lexical 和 discourse-level features。

**N2** [critical, 共识] **核心贡献新颖性不足**
- 核心发现（continued pretraining bridges ~60pp OOD gap）是 Gururangan et al. (2020) "Don't Stop Pretraining" 在 jailbreak detection 的直接验证。更精细的 decomposition（scrambled regularizer, difficulty threshold）有趣，但在 3 seeds + 500 对话规模上统计支撑不足。
- **影响**：ACL ARR Excitement 维度要求推进领域认知。当前 headline result 在新领域验证已知结论，更适合 Findings paper 或 short paper。
- **修复方向**：以 "difficulty threshold across encoder architectures" 和 "regularizer interpretation of classification supervision" 为主线重新 frame，DAPT 验证降为支撑。

**N3** [critical, 共识] **TF-IDF 基线严重削弱 discourse-level representation 价值主张**
- TF-IDF LR 在 OOD DD 达 0.944，论文最佳 0.997，marginal gain 仅 5.3pp。论文自己承认无法区分 pragmatic features 和 lexical cues（Limitations）。关键缺失：TF-IDF per-prefix (K=1-5) 结果和 ActorAttack 结果均未报告，使 "early detection advantage" 和 "discourse-level claim" 均为 unsubstantiated。
- **修复方向**：补充 TF-IDF 全 prefix + ActorAttack 结果；做 probing experiments 证明超越 lexical cues 的 discourse features。

**N4** [critical, 共识] **"Preliminary findings" 定位与 long paper 格式矛盾**
- Abstract、Introduction、Conclusion 三处使用 "preliminary"。自我降格信号表明作者对贡献充分性缺乏信心。但仅删除 "preliminary" 而不扩大实验规模会变成 overclaiming。
- **修复方向**：同时移除 preliminary hedging 并扩大实验规模；或改投 Findings paper。

**N5** [critical, 共识] **缺少与现有 multi-turn defense 的直接实验对比**
- 讨论了 DeepContext/BIID/G-Guard/SafeDream 但未直接比较。vanilla DeBERTa（frozen, 1-layer BiGRU, 128 hidden）不能 represent DeepContext（fine-tuned BERT, 3-layer GRU, 2048 hidden）。
- **修复方向**：复现 DeepContext 或在共同 benchmark 对比；或明确定位为 analysis paper（分析什么使泛化成为可能）而非 method paper（提出更好的方法）。

**N6** [critical, 共识] **数据规模不足以支撑 statistical claims**
- 500 训练 + 76-118 测试 + 3 seeds。MLM DD-Full std=0.115（seed 456 recall=0.64）。Evidence hierarchy 中多对 confidence intervals 重叠。FITD 无 discriminative power（vanilla 和 9-class 均 F1≥0.990）。
- **修复方向**：至少 5 seeds（理想 10）；bootstrap 95% CI；paired bootstrap/permutation test。

**N7** [critical, R2 提出 R1 升级] **缺少 ACL ARR Responsible NLP Research Checklist**
- 论文涉及 jailbreak attack 技术，未包含 ARR 要求的 Responsible NLP Research Checklist。存在 desk reject 风险。
- **修复方向**：按 ARR 要求填写完整 checklist。

### Should-Fix（11 项 major/warning）

**W1** [major, 共识] **Related Work 包含大量本文实验数据**。"Domain-adaptive pretraining" 和 "Dataset artifacts" 段落中引用本文 F1 数值，应移至 Results/Discussion。

**W2** [major, 共识] **Abstract 数据过载**。~150 词中包含 12+ 数值。保留 2-3 headline numbers，其余用定性描述。

**W3** [major, 共识] **ActorAttack 样本量未在 Section 4.1 中说明**。FITD 和 DD 标注了 80 条，ActorAttack 数量缺失。

**W4** [major, 共识] **Introduction 第四段结果段过于冗长**。~200 词 15+ 数值，读者尚未了解方法细节无法消化。

**W5** [major, R1 提出] **BiGRU + frozen encoder 设计缺乏 justification**。frozen 设计可能低估某些 variants 潜力。Mean pooling single-seed 与 3-seed BiGRU 不可比。

**W6** [major, 部分分歧] **LLM-as-judge baseline 仅 zero-shot**。R1 认为不公平，R2 认为目的合理但同意应补 few-shot。共识：至少测试 few-shot 设置。

**W7** [major, 共识] **策略标注质量验证不足**。κ=0.78 基于 n=50 单标注员。需至少两个独立标注员 + human-human κ + n≥100。

**W8** [warning, 共识] **Topic classification 存在 shortcut learning confound**。5-class topic labels 与 benign 数据生成的 5 个 topic 完全一致（method.tex:50 vs appendix.tex:139），topic classifier 可能学习了 jailbreak vs benign 的 shortcut 而非论文声称的 "misaligned supervision destabilizes representations"。

**W9** [warning, 共识] **DeBERTa-v3 vs RoBERTa 的 capacity confound 未控制**。DeBERTa-v3-base (184M) vs RoBERTa-base (125M) 在参数量和训练数据上不同，"pretraining method determines the difficulty threshold" claim 可能混淆 capacity effect。

**W10** [warning, R2 提出] **页数可能超限**。需确认 Conclusion 在第 8 页内结束。

**W11** [warning, R2 提出] **Figure 3 (figure*) 浮动位置可能异常**。

### Minor Issues

- **术语不一致**: "domain exposure" / "domain adaptation" / "continued pretraining" / "domain-adaptive pretraining" 混用，应统一。
- **数据重复**: 0.31±0.03 → 0.91±0.12 在 Abstract/Introduction/Related Work/Experiments/Conclusion 出现至少 6 次。
- **α=0.3 loss weight 未 justify**: 未提供选择理由或 sensitivity analysis。
- **引用格式**: austin1962 年份、chao2023pair 年份、han2024wildguard 作者可能有误。
- **FITD K=3/K=5 缺失**: Table 6 中为 "--"，原因未说明（可能因 FITD 对话仅 2-3 轮）。

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上完全一致 [AGREE]：
1. **Single-LLM confound + TF-IDF 0.944** 是最严重的威胁——整个 evidence hierarchy 可能是 stylistic artifact
2. **Novelty 有限**——headline result 是 DAPT 在新领域的验证；更精细发现统计支撑不足
3. **"Preliminary" framing + 数据规模不足** 构成恶性循环：移除 preliminary 需要更多证据，但当前证据确实只支撑 preliminary 结论
4. **缺失 baseline 直接对比** 使 method-level 贡献无法评估
5. **消融设计本身有方法论价值**（七变体隔离、scrambled regularizer、difficulty threshold）

## Reviewer Divergence

仅有两个局部分歧，均已在交叉回应中趋于共识：

1. **LLM-as-judge 公平性** (R1-W3): R1 认为仅 zero-shot 不公平，R2 认为目的合理但同意应补 few-shot。**共识**：至少补充 few-shot 评估。

2. **Scrambled labels 替代解释** (R1-Q2): R1 提出 "小数据集上任何分类 head 的 gradient signal 都够"，R2 反驳 topic classification 同有分类 head 但表现差，排除了该假设。R1 未进一步反驳。**共识**：R2 的 rebuttal 成立，但 topic classification 本身存在 shortcut confound（CROSS-Q5）。

---

## Questions（需作者澄清）

**Q1** [最高优先级] OOD test data (DD, FITD, ActorAttack) 是否也由 Qwen3-8B 生成？如果是，"cross-attack generalization" 实为 "cross-template generalization within same LLM distribution"。

**Q2** TF-IDF 在 ActorAttack 上的 F1？这决定了 discourse-level claim 是否站得住脚。

**Q3** TF-IDF 在 K=1, 2, 3, 5 各 prefix 上的表现？这决定了 "early detection advantage" 是否成立。

**Q4** ActorAttack OOD 数据的具体样本数量？

**Q5** "Pragmatic features (hedging, escalation markers, topic-shifting patterns)" 的直接 probing 证据？

**Q6** DeBERTa-v3 vs RoBERTa 的差异是 pretraining method (RTD vs MLM) 还是 model capacity (184M vs 125M) 导致？

---

## Missing References

**高优先级（交叉共识）**:
- Persuasion for Good (Wang et al., 2019) — dialogue persuasion detection 先驱
- SmoothLLM (Robey et al., 2024) — perturbation-based defense，直接相关
- TAP (Mehrotra et al., 2024) — multi-turn automated attack
- MHJ dataset (Li et al., 2024) — 人类生成的 multi-turn jailbreak（已 cite 但未用作评估）
- JailbreakBench (Chao et al., 2024) — 标准化 jailbreak 评估
- HarmBench (Mazeika et al., 2024) — 多维度安全评估 benchmark

**中等优先级**:
- AutoDAN (Liu et al., 2024) — 自动化攻击生成
- Circuit Breakers (Zou et al., 2024) — representation engineering defense
- GradSafe (Xie et al., 2024) — gradient-based jailbreak detection

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。项目配置中未启用 `external_review.paperreview_ai`。

---

## Overall Assessment

**Overall: Weak Reject (2.5/5)**
**Confidence: 4/5**

两位 Reviewer 独立给出相同评分（2.5/5），交叉回应后维持。

论文的核心价值在于消融实验设计（七变体隔离 + scrambled regularizer 发现 + cross-encoder difficulty threshold），这些在方法论上有贡献。但以下问题阻碍接收：

1. **Single-LLM confound 未解决**：所有数据可能共享 Qwen3-8B 分布，TF-IDF 0.944 是最直接的 red flag。
2. **Novelty 定位混乱**：headline result 是已知结论的领域验证，更精细发现的统计基础不足。
3. **"Preliminary" 与 long paper 矛盾**：数据规模（500 训练 + 76-118 测试 + 3 seeds）确实只能支撑 preliminary 结论。
4. **缺失关键数据点**：TF-IDF per-prefix、TF-IDF on ActorAttack、probing experiments、direct baseline comparison——任何一项补充都可能显著改变论文的可信度。

**建议路径**：
- **Path A（扩展后重投 long paper）**：补充不同 LLM/人类数据评估 + probing experiments + TF-IDF 全结果 + 5+ seeds + 明确 analysis paper 定位 → 有机会达到 borderline/weak accept
- **Path B（当前规模投 Findings）**：移除 preliminary hedging + 以 difficulty threshold / regularizer interpretation 为主线 + 补充缺失数据点 → 作为 Findings paper 有竞争力

当前版本不适合 EMNLP 2026 long paper 接收。

---

## Detailed Comments（逐节）

### Abstract
- 数据过载：12+ 数值在 ~150 词中。保留 ~60pp gap bridging 和 ActorAttack cross-encoder collapse 两个 headline numbers，其余定性描述。
- "preliminary findings" 为首句核心限定词，在 peer review 中致命。

### Introduction
- 第 1-3 段叙事线清晰（问题 → 现有不足 → gap）。
- 第 4 段是 ~200 词的 results dump，应压缩为 2-3 句 headline takeaway。
- Contributions 列表合理（3 条），但每条过于密集。

### Related Work
- 覆盖面合理（attacks, defenses, production systems, discourse, DAPT, artifacts）。
- 3 处包含本文实验数据，违反 Related Work 定位功能。
- 缺失 Persuasion for Good、SmoothLLM、TAP 等引用。

### Method
- 七变体设计清晰且各有 ablation 目标。
- Topic classification 的 5-class 与 benign 生成 topic 一致，存在 shortcut confound。
- α=0.3 loss weight 未 justify。
- Frozen encoder 选择需更多 justification。

### Experiments
- Evidence hierarchy 可视化清晰，但 confidence intervals 缺失。
- TF-IDF per-prefix 和 ActorAttack 结果缺失是最大漏洞。
- ActorAttack 样本量未说明。
- Perturbation analysis 的 three-layer pattern 在 ActorAttack 上不成立，不应作为贡献点。
- Cross-encoder 分析有价值但 capacity confound 未控制。

### Conclusion + Limitations
- Limitations 诚实全面，但 single-LLM confound 未被列为 limitation。
- "Preliminary" 在 Conclusion 中再次出现。

### Appendix
- LLM-as-judge 仅 zero-shot，应补 few-shot。
- FITD K=3/K=5 缺失未解释。
- Reproducibility details 完整但生成 prompt 未直接披露。