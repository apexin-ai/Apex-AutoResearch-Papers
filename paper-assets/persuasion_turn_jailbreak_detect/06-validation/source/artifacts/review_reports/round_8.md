---
round: 8
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-21T10:08:54.545731+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection

**目标 venue**: EMNLP 2026 via ARR May 2026 cycle
**Deadline**: 2026-05-25 (AoE)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计检验; R2: 新颖性+完整性+Related Work+格式合规）
**轮次**: Round 1 → 交叉分享 → 共识达成（1 轮收敛）

---

## Summary

本文提出 DisPeD，一个两阶段多轮越狱检测流水线：Stage 1 通过域自适应预训练（DAPT）在 DeBERTa-v3 上训练 7 种变体（9-class/binary/scrambled/MLM-only/topic/Wiki-MLM/vanilla），Stage 2 用冻结的 BiGRU 聚合 [CLS] 嵌入进行对话级二元分类。通过 13 种编码器配置（7 变体 × 多种规模）的控制消融，论文分解了域暴露、分类监督、标签质量和粒度对跨攻击泛化的贡献。核心发现：(1) 域暴露是跨攻击迁移的主要机制（MLM 关闭 ~60pp 的 OOD gap）；(2) 分类监督提供稳定性但标签正确性/粒度不重要（scrambled ≈ 9-class, TOST-confirmed on DD at n=5）；(3) 时序建模非必需（mean pooling ≈ BiGRU）。实验在合成多轮数据（Qwen3-8B 生成，4 个攻击家族）上进行，辅以 ToxicChat 人类单轮验证和 WildChat FPR 评估。

---

## Strengths

**S1. [共识] 消融设计系统性强。** 7 种 Stage-1 变体的 factorial design 在 NLP 安全领域罕见，每个变体在概念上隔离一个因素。冻结 Stage-1 encoder 确保消融公平性。这种分解思路比"方法 A vs B"对比更有说服力。[R1 S1, R2 S1]

**S2. [共识] Scrambled ≈ 9-class 发现有独立学术价值。** 随机打乱标签产生等效检测性能（DD TOST p<0.001 at n=5; AA Cohen's d=0.09 negligible），说明分类监督以任务无关的方式改善表示质量，对域自适应的更广泛理解有启发意义。[R1 S2, R2 S1]

**S3. [共识] 多维度互补证据。** CKA 热力图、t-SNE 嵌入可视化、策略转移矩阵、前缀级分析、扰动鲁棒性、跨编码器验证、跨 LLM 验证、数据效率分析——提供了 mechanistic insight 而非单纯指标堆叠。[R1 S3, R2 S3]

**S4. [共识] 诚实面对负面结果。** Discussion 坦承 MLM 在 mixed-LLM 下崩溃、ToxicChat 上证据层级逆转、WildChat FPR 过高等问题。Limitations 覆盖广泛（10 个段落）。[R1 S4]

**S5. [共识] 可复现性完备。** 超参数完整列出，计算预算清晰（单卡 A100 共 4 GPU-hours），代码/数据计划以 MIT / CC BY-NC 4.0 发布。Appendix 详尽（22 页补充材料）。[R1 S5, R2 S5]

**S6. [共识] 写作质量好。** 行文简洁，无明显 AI 生成痕迹，符号使用基本一致，Figure 1 pipeline 图清晰。[R2 S4]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [共识] 正文超过 8 页限制——可能触发 desk reject。** Section 6 (Conclusion) 起始于第 9 页顶部，主文（Sections 1-6）约 8.1-8.2 页。EMNLP 2026 严格执行 8 页限制（Limitations 和 Ethics 不计入）。视觉审查 Agent 独立确认此问题。**注意：此问题在 Round 3 曾被标记为已解决，当前为 regression。** [R2 W1, R1 M1, Visual Check]

**MF2. [共识] 缺少与任何已发表多轮防御系统的直接实验对比。** 论文引用了 BIID、G-Guard、SafeDream、X-Boundary、JBShield 等 5+ 个已发表系统，但实验中未运行任何一个。Vanilla DeBERTa+BiGRU 声称 "equivalent to DeepContext" 但此等价性未经验证。LLM-as-judge baseline 也存在公平性问题（未经 domain-specific 训练，GPT-5.5 30-47% 不可解析可能是 prompt 设计问题）。没有外部校准点，性能声明缺乏参照系。**历史 issue R1-N2-v2，跨 6 轮未解决。** [R1 N1, R2 W7]

**MF3. [共识] OOD 评估中 benign 是 IID，系统性膨胀了 OOD F1。** OOD 评估集的攻击来自未见家族但 benign 与训练同分布。OOD F1 衡量的是"在熟悉良性背景下检测新攻击"——这是显著更简单的任务。Table 2 中 F1 ≥ 0.99 为 upper bound。WildChat FPR=44-68% 从反面验证了此问题。**历史 issue R5-N1，跨 4 轮未解决。** [R1 N2, R2 W3]

**MF4. [共识] TOST 等价性检验统计效力不足。** n=3 时 TOST 功效 < 0.3。即使扩展到 n=5：DD confirmed (p<0.001) 但 AA 仍 p=0.08 formally inconclusive。5pp margin 无理论依据（安全关键场景中 5pp 可能是实质性差异）。Bootstrap CI 跨种子池化（76→228）违反独立性假设。"scrambled ≈ 9-class" 是核心发现之一，统计基础需加固。**历史 issue R6-N2，部分缓解但未完全解决。** [R1 N4]

**MF5. [共识] 新颖性有限——核心发现的"反直觉"程度被高估。** DAPT 有效性是 Gururangan et al. (2020) 已知结论；"标签正确性不重要"在 SSL 文献（SimCLR/BYOL）中已有先例；"时序建模不重要"在 bag-of-features 文献中已被观察到；"粒度不重要"在 transfer learning 中是常见现象。增量贡献是将这些已知现象在 jailbreak detection 领域系统验证——这有价值但不足以支撑 main conference 的 novelty 要求。**历史 issue R2-N1-v2，跨 7 轮持续存在。** [R2 W2]

**MF6. [共识] WildChat FPR 44-68% 严重削弱实用价值主张。** Introduction 中 "offering a practical alternative given matched benign distributions" 暗示实用价值，但真实数据上将近一半到三分之二的正常对话被误判。ROC AUC=0.700 表明表征层面区分力不足，post-hoc calibration 无法解决。如果速度优势的前提是系统可用，那么在 FPR 如此高时速度优势无意义。**历史 issue R6-W1。** [R2 W3, R1 context]

### Should-Fix（影响评分但不一票否决）

**SF1. [共识] 数据规模和合成依赖。** 训练 350 条合成对话（Qwen3-8B 单一来源）、ID 测试 76 条、OOD 118 条。仅 1 个有效 OOD 攻击家族（ActorAttack，因 FITD 无区分度、DD 被 TF-IDF 高度解决）。同一模型既生成数据又做标注引入系统性偏差。ToxicChat 是单轮，无法验证多轮 claim。**历史 issue R4-N3。** [R1 N3, R2 W5]

**SF2. [共识] "Single-factor isolation" 声明过度。** Binary vs 9-class 同时改变粒度和分类目标数量；Topic vs 9-class 同时改变语义内容和类别数（5 vs 9）；MLM-only 同时移除分类监督和改变训练目标。论文应更精确描述每个对比实际隔离了什么。[R1 W3]

**SF3. [共识] Scrambled ≈ 9-class 削弱 taxonomy 贡献的叙事张力。** 如果打乱标签产生等效检测，9 类 taxonomy 在检测上无因果作用。论文试图同时声称 taxonomy 为贡献又承认标签不重要——叙事逻辑矛盾。此外 n=50 人工验证对 9-class 偏小（每类仅 ~5.5 样本），且如果标签不重要，为何投入 effort 验证标签质量？**历史 issue R6-W2 + R1-W4-v2。** [R1 W4, R2 W8]

**SF4. Related Work 遗漏 domain-specific pretraining 前辈。** BioBERT (Lee et al., 2020) 和 SciBERT (Beltagy et al., 2019) 是 continued pretraining on domain text for encoder-based classifiers 的代表性前辈工作，直接相关但未被讨论。在讨论 label correctness 时，SSL 文献（SimCLR/BYOL）应作为更广泛 context 被引用。[R2 W6]

**SF5. FITD 无区分度削弱"4 攻击家族"声称。** 所有变体在 FITD 上 F1≈1.000，对消融无贡献。有效鉴别力仅来自 ActorAttack（DD 被 TF-IDF 高度解决）。论文应坦承这一点。[R2 W4]

**SF6. Population std (n divisor) 低估变异性。** n=3 时 population std 比 Bessel-corrected (n-1) 低约 18%，使误差条看起来人为偏紧。虽论文声称不影响结论，但报告样本统计量时这是非标准做法。[R1 W5]

**SF7. 术语不一致。** "cross-attack generalization" 和 "OOD" 交替使用，但本文仅攻击侧分布漂移（benign 是 IID）。K 有时表示总轮数有时表示截断位置。**历史 issue R2-TERM。** [R1 M3, R2 W9]

### Minor（不影响接收）

- Figure 2 柱状图灰度打印下颜色难以区分，建议添加 hatching pattern [R2 W10, R1 M2]
- Figure 1 内部文字标注字号偏小，接近可读性下限 [Visual Check]
- Pages 6-8 连续 3 页 "顶部 table + 下方纯文字" 视觉节奏单调 [Visual Check]
- TF-IDF 在 K=2 时 F1=1.000 暗示短对话存在平凡词汇线索，值得讨论 [R1 M4]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上完全一致：

1. **Overall 评分 3.0 (Findings)**——执行扎实但新颖性和实用性不足以支撑 main conference
2. **页数超限**是格式硬伤，可能触发 desk reject
3. **IID benign 膨胀 OOD F1** 是系统性评估缺陷
4. **WildChat FPR 44-68%** 严重限制实用价值
5. **缺少已发表 baseline** 使性能声明缺乏参照系
6. **消融设计** 在概念层面优秀，是论文最大亮点
7. **Scrambled ≈ 9-class** 有学术价值但统计基础需加固
8. **Appendix 详尽**，可复现性好

---

## Reviewer Divergence [REBUT]

**分歧点 1: End-to-end fine-tuning 的必要性**
- R1: Frozen encoder 可能低估 vanilla 潜力，需要 E2E 对照 [Should-Fix]
- R2: Frozen encoder 是方法论优势而非缺陷，Appendix N 已提供 E2E 结果（Δ≤2.5pp）[REBUT]
- **Director 判断**: R2 的反驳有据——E2E 数据已存在且差距极小。降级为 info。

**分歧点 2: Missing references 的严重性**
- R2: BioBERT/SciBERT/CoSafe/SimCLR 等为 Must-Fix 级别遗漏
- R1: 未发现关键缺失引用，现有覆盖全面
- **Director 判断**: BioBERT/SciBERT 确实与 DAPT 方法论直接相关，但非致命遗漏。列为 Should-Fix。

---

## Questions（需作者澄清）

1. 如果在 OOD 评估中加入不同领域的 benign 对话（如客服、学术问答），F1 ≥ 0.99 是否还能维持？[R1 Q1]
2. TOST 等价性被拒绝的最小 margin 是多少？能否提供 n=3 和 n=5 的 power analysis？[R1 Q2, Q6]
3. Scrambled labels 中 random permutation 的种子是否会影响结果？不同 permutation 的 variance 有多大？[R2 Q1]
4. 为什么没有在同一数据上运行已发表的多轮防御系统？是数据格式不兼容、代码不可用，还是方法论选择？[R1 Q4]
5. Mixed-LLM 如果加入更多样化的 LLM，能否改善 WildChat FPR？[R2 Q2]
6. RoBERTa-base vanilla 已达 DD 0.981——DAPT 的价值是否 architecture-dependent？[R2 Q3]
7. 放松 BERTScore 约束（如 0.85 或 0.80）时，detection 是否显著下降？[R2 Q5]

---

## Missing References

**R2 提出（R1 未发现关键缺失）：**
- BioBERT (Lee et al., 2020) — domain-specific continued pretraining 前辈
- SciBERT (Beltagy et al., 2019) — 同上
- CoSafe (Yu et al., 2024) — 多轮对话安全评估基准
- SimCLR / BYOL / MoCo — label correctness debate 的更广泛 context
- WildJailbreak (Jiang et al., 2024) — in-the-wild jailbreak 数据集

---

## External Review (Stanford Agentic Reviewer)

外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置）。无外部审稿结果。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（2026-05-21 09:51 → 09:56，耗时约 5 分钟）。

**Warning (2)**:
1. **Page 9**: 正文 Section 6 (Conclusion) 溢出至第 9 页——与 R2 W1 / R1 M1 一致
2. **Pages 6-8**: 连续 3 页 "顶部 table + 下方纯文字" 的单调视觉节奏

**Info (10)**:
- Page 1: 首页无视觉锚点（纯文字），Figure 1 在 page 2 出现
- Page 2: Figure 1 内部文字标注字号偏小
- Page 5: Figure 2 色彩区分度良好，色盲友好
- Page 5: Table 2 booktabs 风格规范，±std 格式统一
- Page 9: Limitations 分段清晰，符合 EMNLP 要求
- Pages 13-14: Appendix 大型表格跨页呈现正常
- Page 15: Figure 3（heatmaps）双栏内尺寸偏小
- Page 16: Figures 4+5 与 Tables 密度高但可读
- Pages 10-11: References 格式统一，无 [?] 未解析引用
- Page 22: Responsible NLP Research Checklist 完整填写

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| **Overall** | **3.0** | **3.0** | **3.0** |
| Confidence | 4/5 | 4/5 | — |

**Overall: 3.0 — Findings（可被 Findings 接收）**

### 总评

一项执行扎实的控制消融研究，系统地分解了 encoder adaptation 在多轮 jailbreak 检测中的各因素贡献。消融设计是最大亮点——7 种变体的 factorial approach 在 NLP 安全领域少见。Domain-exposure > label-correctness 的发现有真正的学术价值，scrambled ≈ correct labels 的观察对 DAPT 理论有启发意义。

但论文面临三个结构性问题：(1) 核心发现在 DAPT/SSL 文献中均有先例，增量新颖性有限——更适合定位为"安全关键领域的系统验证"而非"反直觉发现"；(2) IID benign 膨胀了 OOD F1，WildChat FPR 44-68% 暴露了真实场景下的严重局限，削弱了论文的实用价值叙事；(3) 关键统计检验（TOST n=3/5、跨种子池化 bootstrap CI）的效力不足以支撑核心结论的确定性程度。

此外，正文超过 8 页限制和缺少已发表 baseline 的实验对比是需要立即解决的格式/实验问题。

**建议接收为 Findings**，条件是修复页数超限、降级统计声明、更诚实地定位新颖性和实用价值。

---

## Detailed Comments

### 按章节详细意见

**Abstract**: 数值使用克制（~5 个），scope 限定为 "synthetic multi-turn data" 是正确的。但 "condition-dependent" 和 "evidence hierarchy" 首次出现时缺乏直观解释。

**Introduction**: Contribution 列表结构清晰但信息密度仍偏高。"Counter-intuitive findings" 的 framing 需降温——在更广泛 ML 文献中这些并非反直觉。第四段结果预览偏长（历史 issue R2-W4-v2 未解决）。

**Related Work**: 覆盖面广（31 篇引用），但遗漏 domain-specific BERT 前辈（BioBERT/SciBERT）。与 computational persuasion 文献的联系充分。

**Method (Section 3)**: Table 1 清晰传达 7 种变体设计。但 "single-factor isolation" 声明需加 caveat（Binary/Topic/MLM 存在混淆）。Strategy annotation 质量验证不足（n=50, κ=0.78）。

**Experiments (Section 4)**:
- **Setup**: 数据规模偏小（350 训练，76/118 测试）。OOD benign = IID 是系统性缺陷。
- **Cross-Attack (4.2)**: Table 2 清晰但 F1 ≥ 0.99 应标注为 upper bound。
- **Decomposition (4.3)**: Evidence hierarchy 是论文核心贡献。TOST 统计基础已改善（n=5）但 AA 仍 inconclusive。4-20× variance reduction 需降级为描述性观察。
- **Cross-Encoder (4.4)**: RoBERTa-large vanilla 1.000 on AA 是重要发现，但 scale claim 被架构差异混淆（历史 issue R1-CAPACITY）。
- **Mixed-LLM (4.5)**: MLM 崩溃是重要负面结果。
- **Human Data (4.6)**: ToxicChat 是单轮——正文应更明确标注。
- **Perturbation (4.7)**: AA 下 DAPT 降 20pp 是重要局限。
- **Strategy (4.8)**: OOD κ=0.126 坦诚但削弱 taxonomy 价值。

**Discussion (Section 5)**: 与 Introduction contributions 有重复。"Benign distribution as the remaining bottleneck" 段落重要但应提前至更显眼位置。

**Conclusion (Section 6)**: 溢出到第 9 页——必须压缩。

**Limitations (Section 7)**: 覆盖广泛（10 段），内容充实。但正文 framing 与 Limitations 中承认的局限之间存在温度差。

**Appendix**: 极其详尽（22 页），包含 per-prefix 分析、CKA、cross-LLM、TOST sensitivity、数据效率等。Reproducibility details 完备。

### 历史 issue 追踪摘要

本轮（Round 8 fresh review）重新发现了以下长期未解决的 issues：
- **R2-N1-v2** (新颖性不足): 跨 7 轮持续存在 → 本轮再次确认
- **R1-N2-v2** (缺少已发表 baseline): 跨 6 轮未解决 → 本轮再次确认
- **R5-N1** (IID benign): 跨 4 轮未解决 → 本轮再次确认
- **R6-N2** (TOST 效力): 部分缓解（n=5）但未完全解决 → 本轮再次确认
- **R2-W6-v2** (页数超限): Round 3 标记为已解决，**当前为 regression**

新发现 issues：
- **R8-N1**: Single-factor isolation 声明过度
- **R8-N2**: FITD 无区分度
- **R8-N3**: BioBERT/SciBERT 等 related work 遗漏
- **R8-N4**: LLM baseline 对比公平性