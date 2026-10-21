---
round: 5
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-20T08:59:39.206599+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：What Makes Multi-Turn Jailbreaks Detectable? A Controlled Study of Domain Adaptation

**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1（方法严谨性+实验设计+统计有效性）, R2（新颖性+相关工作+完整性+格式合规）
**Round**: 5 (fresh mode)
**收敛状态**: Round 1 收敛，两位 Reviewer 评分一致（3.0），核心问题互补无矛盾

---

## Summary

本文提出 DisPeD（Disentangled Persuasion Detection），通过两阶段 pipeline（Stage 1: DeBERTa-v3 编码器领域自适应预训练 → Stage 2: 冻结 [CLS] embeddings + BiGRU 对话级分类）系统地分解跨攻击泛化（cross-attack generalization）的关键因素。7 个 Stage-1 变体的 controlled ablation 在 Qwen3-8B 合成数据上展开，覆盖 IID（Crescendo）和 3 个 OOD 攻击族（Deceptive Delight, FITD, ActorAttack），以及 ToxicChat 人类数据验证和 mixed-LLM（Qwen+Llama）训练验证。核心发现：(1) 领域暴露是跨攻击泛化的首要因素（MLM 闭合 ~60pp OOD gap），标签正确性和粒度为非因素；(2) 分类监督降低 cross-seed 方差 4-20×（3 seeds），但此优势在人类数据上逆转；(3) 编码器容量决定是否需要 adaptation（RoBERTa-large 355M 无需适配即可泛化）。

---

## Strengths

**S1. 精心设计的 controlled ablation**（R1+R2 一致）
7 个 Stage-1 变体（9-class, binary, scrambled, MLM-only, topic, wiki-MLM, vanilla）系统地隔离了 domain exposure、classification supervision、label correctness、label granularity、domain specificity 五个因素。这种因素分解方法在安全检测领域少见，比简单的 "method A vs. B" 对比有更高的学术价值。

**S2. 统计分析全面规范**（R1+R2 一致）
Bootstrap CI（10,000 resamples）、McNemar's test、paired permutation test、TOST equivalence test（含 δ=2/3/5pp sensitivity analysis）的全面使用在 NLP 论文中不常见。

**S3. 负面结果有实用价值**（R2）
scrambled ≈ correct labels、mean pooling ≈ BiGRU、granularity 无关——这三个反直觉发现对实际部署有直接指导意义：practitioners 无需昂贵标注即可构建有效检测器。

**S4. 多维度分析充实**（R1）
跨编码器（DeBERTa-v3 + RoBERTa base/large）、跨训练组合（single-source + mixed-LLM）、跨数据源（合成 + ToxicChat 人类数据）、对抗扰动、CKA/t-SNE 表征分析、策略轨迹分析——分析层次丰富。

**S5. Reproducibility 承诺**（R1+R2 一致）
详细超参数（Appendix M）、承诺开源代码和数据（CC BY-NC 4.0 + MIT）、Checklist 填写诚实。总计算量 <4 GPU-hours（单 A100），方法可复现。

**S6. Limitations 部分诚实详尽**（R1）
9 个子项覆盖合成数据、标注质量、规模、范围、单轮迁移、计算成本等主要局限，显示了自觉意识。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**MF1** [critical, R1-N1+R2-N3] **数据规模极小 + 完全依赖合成数据，外部效度不足**

训练集仅 250 jailbreak + 250 benign（350 训练/74 验证/76 测试 IID），OOD 每族 80 jailbreak + 38 benign = 118。所有训练和主要评估数据由 Qwen3-8B 单一模型生成。

- n=76 IID 测试集上 F1 的 95% CI 宽度约 ±0.05-0.08，McNemar test power 极低（≤7 discordant pairs）
- TOST 等价检验（margin ±3pp）在 F1≈1.0 时几乎没有区分度
- 论文自报 "no significant pairwise differences (all p > 0.13)" 但解读为"等价"而非 power 不足
- ToxicChat 人类数据验证仅 single-turn，无法验证多轮核心结论
- 如果合成数据存在 Qwen3-8B 特有的系统性 artifacts（如固定的 turn structure、stereotyped persuasion patterns），"domain exposure is sufficient" 可能实际在学习这些 artifacts
- Appendix J 的 500→1000 scale validation 仅覆盖 3 个变体（9-class/MLM/vanilla），不够

**影响**：所有核心结论建立在小样本合成数据对比上。analysis paper 的核心价值在于发现的 generalizability；若发现仅在合成数据上成立，学术价值大打折扣。

**MF2** [critical, R1-N2, NEW] **OOD benign 与 IID benign 完全相同——OOD 评估存在系统性偏差**

Section 4.1 明确写道 OOD 评估复用 IID 的 38 条 benign 对话。这意味着 OOD 评估 **仅测试了攻击侧的泛化**，benign 侧完全未测试分布外情况。

- 如果模型过拟合了训练 benign 的表面特征，OOD F1 不会暴露这一问题
- Cross-LLM 实验（Appendix H, Table 12）已部分暴露此问题：将 Qwen benign 替换为 Llama benign 后 FP 率从 0-0.9% 飙升至 88-90%——说明 benign 分布确实影响巨大
- 但主实验中 OOD F1（Table 2-4）全部基于 IID benign 计算，高 F1 可能部分归因于 benign 侧记忆效应

**影响**：严重限制 "cross-attack generalization" 结论的外部效度。

**MF3** [critical, R1-N3, 升级自 R1-W2-v2] **缺少 end-to-end joint fine-tuning 对照实验**

Stage-2 训练时 Stage-1 编码器完全冻结。论文声称这是为了 "isolate the effect of Stage-1 representation quality"（Section 3.3），方法论上可理解，但 **缺少 joint fine-tuning 对照** 使得核心结论的可靠性存疑。

- 在标准 NLP 实践中，fine-tuning 整个模型通常优于 frozen encoder + 浅层分类器
- 如果 vanilla + end-to-end fine-tuning 接近或超过 DAPT variants，则 "domain exposure is the primary factor" 的结论被动摇——Stage-2 训练期间的梯度回传本身可能足以完成 domain adaptation
- Method Section 有文字 justification（"ensures ablation fairness"）但无实验验证

**影响**：frozen encoder 可能是性能瓶颈，导致论文低估了某些变体的潜力。整个 ablation 的解读依赖于 frozen 假设。

**MF4** [critical, R2-N1] **核心发现 "scrambled ≈ correct" 缺乏因果/机制解释**

论文反复强调 "domain exposure is the primary mechanism"，但从未深入解释 *为什么* scrambled labels 能提供与 correct labels 相当的效果。

- 存在多种可能假说：(a) 分类头作为 regularizer 迫使编码器学习更 discriminative 的表示；(b) 多任务目标的梯度多样性足够；(c) 任何额外 loss 项都足以打破 MLM-only 的退化
- 论文未区分这些假说，也未引用 auxiliary task regularization 文献（如 Caruana 1997 multitask learning 中 "noise as regularizer" 的讨论）
- 对 analysis paper 而言，"发现了什么"和"为什么"同等重要

**影响**：这是论文最核心的发现，缺乏解释使读者无法判断发现的 generalizability 和 boundary conditions。

**MF5** [critical, R2-N2, 延续 R4-W6] **遗漏多篇高度相关的 2025-2026 工作**

以下工作未被引用或讨论（需 WebSearch 核实后确认真实存在者）：
1. **JBShield** (USENIX Security 2025, arXiv:2502.07557) — representation-level jailbreak detection via activated concept analysis，与本文 representation-based 方法直接可比
2. **"How Do LLMs Persuade?"** (Jaipersaud et al., arXiv 2508.05625, 2025) — linear probes 捕捉多轮对话说服动态
3. **"Guarding the Guardrails"** (arXiv 2510.13893, 2025) — taxonomy-driven jailbreak detection
4. **Computational Persuasion Survey** (arXiv 2505.07775, 2025)
5. **Perez et al. (2022)**: "Red Teaming Language Models with Language Models" — 合成攻击生成先驱
6. **Souly et al. (2024)**: "A StrongREJECT for Empty Jailbreaks" — 评估框架
7. R2 另列 3 篇 concurrent work（Latent Adversarial Detection, Active Honeypot, Revisiting JBShield），需核实

**注意**：R2 列出的引用中部分可能为 Reviewer 幻觉。Research Director 应通过 WebSearch 逐一核实后再决定补充哪些。

**影响**：遗漏 representation-level 检测方法使论文未与最直接的方法进行对比定位；遗漏 computational persuasion 文献削弱论文声称的 persuasion-discourse 贡献可信度。

### Should-Fix 问题（影响评分但不一票否决）

**SF1** [warning, R2-W1, 延续 R2-N1-v2] **与 DAPT (Gururangan et al., 2020) 区分不清**
核心方法本质是 DAPT + downstream classification。Introduction 暗示 DisPeD 是新方法（"Our pipeline, DisPeD..."），但实际是实证分析。应明确定位为 empirical analysis paper。

**SF2** [warning, R1-W1] **BiGRU ≈ mean pooling 削弱 "multi-turn" 叙事**
如果时序建模与简单平均池化等效，模型并未利用轮次顺序信息。这与标题 "Multi-Turn" 和 Introduction 强调的 "adversarial intent across benign-seeming turns" 存在 tension。建议 shuffle turns 实验或更强时序 baseline（Transformer decoder）。

**SF3** [warning, R1-W2+R2-W4, 延续 R1-W4-v2] **9-class taxonomy 验证不充分**
n=50, κ=0.78 仅为 model-human agreement。无 human-human IAA baseline，无 per-class κ/混淆矩阵。更关键的是，scrambled ≈ correct 间接说明 taxonomy 的细粒度区分对检测无关紧要，削弱了 taxonomy 本身作为贡献的价值。

**SF4** [warning, R1-W3, 延续 R1-CAPACITY] **RoBERTa-large vanilla F1=1.000 on ActorAttack 需更多解释**
完全未见过 jailbreak 数据的 vanilla 编码器在最复杂攻击上完美检测——要么攻击有极易检测的 artifact，要么 n=118 测试集太小导致偶然。两种解释都削弱 "domain adaptation is necessary" 的论点。

**SF5** [warning, R1-W5, 延续 R3-W1] **3-seed 方差估计不可靠**
仅 2 自由度，标准差的标准误极大。"variance reduced 4-20×" 的声明在 n=3 下极不稳定。建议至少 5 seeds，理想 10 seeds。当前应标注为 "suggestive, observed across 3 seeds"。

**SF6** [warning, R1-W6] **因果性语言过强**
"isolate"、"decompose the mechanism"、"is the primary mechanism" 暗示因果关系，但论文提供的是行为层面的对比证据。应弱化为 "disentangle the contributions of"、"factor"、"appears to be the most important factor in our experimental setup"。

**SF7** [warning, R2-W2] **Figure 1 信息密度不足**
Figure 1 占 Page 2 约 1/3 空间，展示标准两阶段 pipeline（encoder + BiGRU），信息增量低。建议缩小或增加 ablation overview figure。

**SF8** [warning, R2-W3] **Discussion 与 Introduction contributions 重复**
Discussion 三个 observations 与 Intro 三个 contributions 高度重叠。Discussion 应提供 deeper insight：理论解释、部署 implications、broader NLP 连接。

**SF9** [warning, R2-W5, 延续 R4-W5] **TF-IDF 在 DD 上 F1=0.961-1.000 暗示 trivial lexical shortcuts**
DD 数据存在高度词汇可分性。论文已部分承认，但 DD 仍作为主结果表（Table 2）的核心 OOD 集。ActorAttack（TF-IDF=0.261）才是真正的鉴别性评估轴。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致：
- **[AGREE]** 合成数据外部效度是核心限制（MF1）
- **[AGREE]** 3-seed 方差估计不够可靠（SF5）
- **[AGREE]** 9-class taxonomy 验证不充分（SF3）
- **[AGREE]** 论文作为 analysis paper 实验设计严谨（S1）
- **[AGREE]** 统计分析在该领域论文中高于平均水平（S2）
- **[AGREE]** 负面结果有实用价值（S3）
- **[AGREE]** Reproducibility 承诺到位（S5）

## Reviewer Divergence

- **OOD benign 偏差**（MF2）：R1 将其列为 critical Must-Fix。R2 未独立提及此问题，但 R2-N3 的 external validity concern 隐含覆盖。
- **Joint fine-tuning 对照**（MF3）：R1 列为 critical。R2 未提及。这是 R1 的独到观察——如果 vanilla + unfrozen 已足够好，整个 ablation 框架需要重新解读。
- **Scrambled ≈ correct 解释**（MF4）：R2 列为 critical Must-Fix。R1 通过 W6（因果语言过强）间接触及但未要求机制分析。
- **方法论新颖性**（SF1）：R2 认为方法无创新（Excitement 3/5）。R1 认为 ablation 设计本身有价值（Excitement 3/5），但未将 novelty 列为 Must-Fix。

---

## Questions

1. 如果 Stage-1 encoder 解冻进行 end-to-end fine-tuning，9-class vs. vanilla 的差距是否缩小或消失？（R1）
2. 对 turns 进行 shuffle 实验，F1 会下降多少？BiGRU ≈ mean pooling 是否意味着检测完全不依赖轮次顺序？（R1）
3. RoBERTa-large vanilla 在 ActorAttack 上 F1=1.000 的 per-sample prediction confidence 分布？是否存在 borderline cases？（R1）
4. Mixed-LLM 中 MLM 崩溃（0.289）但 9-class 维持（0.818）——这是否说明 classification objective 提供了比 domain exposure 更强的 inductive bias？（R1）
5. 使用独立 OOD benign 集（不同话题/来源）后 F1 变化如何？（R1）
6. scrambled labels 等效的具体机制是什么？是 regularization、gradient diversity、还是任何额外 loss 即可？能否通过 random projection head 实验区分？（R2）

---

## Missing References

以下为两位 Reviewer 提出的候选缺失引用（**需 WebSearch 核实后确认真实存在者再补充**）：

**R2 提出（7 项）**：
1. JBShield (USENIX Security 2025, arXiv:2502.07557)
2. "Latent Adversarial Detection" (arXiv:2604.28129, April 2026)
3. "How Do LLMs Persuade?" (Jaipersaud et al., arXiv:2508.05625, 2025)
4. "Guarding the Guardrails" (arXiv:2510.13893, 2025)
5. "Must Read: Computational Persuasion Survey" (arXiv:2505.07775, 2025)
6. Active Honeypot Guardrail System (arXiv:2510.15017, 2025)
7. "Revisiting JBShield" (arXiv:2605.03095, May 2026)

**R1 提出（3 项）**：
8. Alon &amp; Kamfonas (2023): "Detecting Language Model Attacks with Perplexity"
9. Perez et al. (2022): "Red Teaming Language Models with Language Models"
10. Souly et al. (2024): "A StrongREJECT for Empty Jailbreaks"

⚠️ **注意**：Reviewer 提出的引用中部分可能为幻觉（尤其 R2 列出的 arXiv ID 需逐一核实）。建议 Research Director 在采纳前通过 WebSearch 确认每篇论文的真实存在性和内容相关性。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 `external_review.paperreview_ai`）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~4 分钟）。0 critical, 4 warnings, 9 info。

**Warnings**:
1. **Pages 8-9**: 连续 2 页纯文本（Discussion + Limitations），无 figure/table/equation 穿插。建议用 summary figure 可视化 evidence hierarchy 或 capacity-dependent observation。
2. **Page 18**: 附录最后一页仅填充 ~15% 内容（Existing Assets 三条问答），超过 3/4 页空白。
3. **Page 16**: 单页塞入 4 个 display items（CKA heatmaps + t-SNE + 2 tables），页面过于拥挤，图表尺寸被压缩。
4. **Page 14**: Tables 7-8 字号明显小于正文（约 50-60%），密集数字阅读困难。

**Info**: 首页无视觉锚点（Figure 1 在 Page 2）、Figure 1 内部文字标签偏小、Figure 2 未使用 hatching 辅助灰度区分、booktabs 风格规范、无公式渲染错误或 margin 溢出。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**EMNLP 2026 评分标准**: 3 = Findings（可被 Findings 接收）

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**综合判断**：

本文是一篇设计精良的 empirical analysis paper，7 个 controlled ablation 变体系统地分解了跨攻击泛化因素，核心发现（domain exposure > label correctness, scrambled ≈ correct, BiGRU ≈ mean pooling）对学术界和工业界均有参考价值。统计分析水平高于同领域平均。

但以下因素限制其达到主会议水平：

1. **外部效度严重不足**：所有训练和 OOD 评估数据由 Qwen3-8B 合成生成，multi-turn 核心结论完全未经真实数据验证。ToxicChat 仅 single-turn 且 evidence hierarchy 在其上逆转。
2. **实验设计偏差**：OOD benign 复用 IID benign（38 条），OOD F1 可能被 benign 侧记忆效应高估。Cross-LLM 实验已暴露 benign 分布影响巨大（FP 从 0% 飙升至 88-90%）。
3. **关键对照缺失**：无 end-to-end fine-tuning 对照，frozen encoder 假设未经实验验证。
4. **核心发现解释不足**：scrambled ≈ correct 是最 surprising 的发现，但停留在描述层面，未提供机制解释。
5. **方法论新颖性有限**：核心方法是 DAPT 在新领域的应用，pipeline 组件（DeBERTa + MLM + BiGRU）均为标准技术。

**提升路径**（若能完成以下修改，有潜力达到 3.5 Borderline Conference）：
- 解决 MF2（独立 OOD benign 集）和 MF3（joint fine-tuning 对照，至少 3 个代表性变体）
- 补充 MF4（scrambled ≈ correct 的机制讨论，哪怕不做新实验也需引用 auxiliary task regularization 文献并提出假说）
- 核实并补充 MF5（遗漏引用）
- 全文弱化因果性语言（SF6）

---

## Detailed Comments

### Abstract
- 当前版本 ~190 words，数值控制在可接受范围。但 "classification-based adaptation remains the strongest variant" 在 ToxicChat 上被否定（MLM 0.837 >> 9-class 0.596），需限定为 "across synthetic multi-turn OOD"。

### Introduction (Section 1)
- 第四段 results preview 仍偏长（~200 words），与 Contributions 列表部分重复。
- "We isolate the factors" → 应弱化为 "We disentangle the contributions of"。
- DisPeD 全称已给出（"Disentangled Persuasion Detection"），但 R2 指出命名 misleading：Persuasion 暗示核心，但实际发现 persuasion label 不重要。

### Related Work (Section 2)
- 覆盖面较好（multi-turn attacks, defenses, computational persuasion, DAPT），但缺少 representation-level detection 方法（如 JBShield）的专门讨论。
- 引用格式问题（R1-BIB）: austin1962 年份、han2024wildguard 首作者、he2023debertav3 年份需核实。

### Method (Section 3)
- 7 变体设计清晰，Table 1 简明。
- Section 3.3 frozen encoder justification 已存在但薄弱——"ensures ablation fairness" 是设计决策，不能替代 "joint training would/wouldn't change conclusions" 的实验证据。
- α=0.3 loss weight 已有 ablation 支持（全部 F1=1.0 on IID），可接受。

### Experiments (Section 4)
- **Table 2 (Main results)**: DD 作为 primary OOD 展示但 TF-IDF 已达 0.961，暗示 lexical shortcuts。ActorAttack 更具鉴别力但仅在 Table 3 出现。
- **Section 4.2 (Decomposition)**: evidence hierarchy 清晰，但 "McNemar's test finds no significant pairwise differences" → "equivalence" 的推理不严谨（absence of evidence ≠ evidence of absence）。TOST 部分缓解，但 AA 上 underpowered。
- **Section 4.4 (Cross-encoder)**: RoBERTa-large vanilla AA F1=1.000 是异常值，需分析原因。Appendix K 的 LR control 排除了 over-adaptation 但未解释 vanilla 为何完美。
- **Section 4.5 (Mixed-LLM)**: 9-class DD F1=0.818 vs vanilla 0.291 (+53pp) 是有力证据；但 AA F1=0.504 偏低，且 MLM 崩溃（0.289）暗示 classification objective 可能比 domain exposure 更重要——这与 Section 4.2 的 "domain exposure is primary" 叙事存在 tension。
- **Section 4.6 (Human data)**: ToxicChat hierarchy reversal（MLM 0.837 >> 9-class 0.596）是关键反面证据。当前处理方式（归因于 "single-turn, so classification head provides no advantage"）合理但需要在 Abstract/Conclusion 中更显著地限定 scope。

### Discussion (Section 5)
- 三个 confound paragraphs 与 Intro contributions 重叠。建议聚焦理论解释（scrambled ≈ correct 的机制）和部署 implications。

### Limitations (Section 7)
- 9 个子项，覆盖充分。"Multi-turn human validation" 和 "Encoder scale" 为首要 open questions，定位恰当。
- Binary detection head confound（Section 7, "Binary detection head"）已提及但未实验验证。

### Format
- ACL 模板正确（`\usepackage[review]{acl}`）
- Double-blind 匿名化完整（Author: Anonymous）
- 8 页正文 + unlimited references — 符合限制
- Checklist 填写完整诚实
- 引用格式基本规范，个别年份/作者需核实