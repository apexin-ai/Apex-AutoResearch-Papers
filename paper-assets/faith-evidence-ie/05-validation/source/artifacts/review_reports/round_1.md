---
round: 1
overall_score: 3.0 (Findings)
timestamp: 2026-05-18T07:01:12.397092+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 1

**论文**: "Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction"
**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May 2026 cycle)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法与实验严谨性；R2: 新颖性、完整性与呈现质量）
**审稿模式**: 独立初审 → 交叉分享逐条回应 → 收敛汇总（1 轮收敛）

---

## Summary

论文将 evidence-grounded document-level relation extraction 形式化为 LLM 的结构化生成任务，系统比较了 GRPO、DPO、RSFT 三种 post-training 优化范式在联合生成关系三元组和证据句子时的行为。实验跨越 4 个模型规模（1.7B-8B）、2 个模型家族、2 个数据集。论文提出三个核心发现：(1) RL 优化压力与 evidence-extraction decoupling 严重程度相关（decoupling spectrum）；(2) evidence 生成代价随模型规模非单调变化（scale-dependent evidence tax）；(3) RSFT+CED 是唯一有效路线（+4.92pp Ign-F1 over SFT）。

---

## Strengths

**S1. 研究问题重要且定位精准。** LLM-based DocRE 方法产出裸三元组而无证据支撑是真实的实用性瓶颈。论文清晰识别了 encoder-based evidence methods（SAIS/DREEAM）与 LLM extraction accuracy 之间的 gap，问题动机有说服力。[R1, R2 共识]

**S2. 实验覆盖面在 DocRE 领域罕见。** 跨 4 个模型规模、2 个模型家族、2 个数据集、3 种优化范式的系统性比较，横向覆盖面本身有参考价值。[R1, R2 共识]

**S3. Scale-dependent evidence tax 是有价值的经验发现。** 1.7B 受益、4B 受损、8B 中性的模式打破了 "evidence 一定损害 extraction" 的简单假设，对后续研究有指导意义。[R2 提出, R1 同意]

**S4. RSFT "discrete selection avoids gradient-based trade-off" 洞察有一般性意义。** 这一观察超越 DocRE 任务本身，对所有多目标 LLM post-training 场景有参考价值。[R2 提出, R1 同意]

**S5. RSFT 效果稳定。** 4-seed 方差低（±0.49），跨数据集（DocRED +4.92pp, Re-DocRED +4.86pp）和跨模型家族（LLaMA +1.74pp）改进模式一致。[R1 提出, R2 同意]

**S6. 写作质量整体良好。** 无 em-dash，无明显 AI 写作标志词，段落过渡自然，叙事主线从 Abstract 到 Conclusion 基本统一。[R1, R2 共识]

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**W1. [Critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果归因。**
GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了量化精度和 group size。论文将 catastrophic collapse 归因于量化（§4.3），Introduction 明确声称 "QLoRA acts as a catastrophic amplifier"（因果性 claim），但实验设计无法排除 G=4 vs G=8 的影响。更严重的是：GRPO bf16 G=8 的 EDCR (0.6318) 比 SFT baseline (0.6982) 更低（Table 2），去除 QLoRA 极端案例后 GRPO 并未展现明显 decoupling，spectrum 的核心叙事 "GRPO > DPO > RSFT in decoupling severity" 站不住。[R1 提出, R2 强烈同意]

**W2. [Critical] 全部结果仅在 dev set 上报告，test set 缺失。**
对于声称 "85+ configurations" 的系统性实证研究，没有任何 DocRED test set 结果（有公开 CodaLab leaderboard）。论文核心数字（+4.92pp, 50.50 vs 50.51）均基于 dev set，不能视为最终性能指标。[R1, R2 独立提出，共识]

**W3. [Critical] SFT baseline 缺少多 seed 方差，核心改进数字（+4.92pp）缺乏统计显著性检验。**
RSFT CED 有 4-seed 均值 44.66±0.49，但 SFT baseline 39.74 仅单 seed。全文无统计显著性检验（t-test/bootstrap/permutation test）。考虑 RSFT 自身 seed range = 0.96pp，SFT 方差不可忽略。+4.92pp 出现在 Abstract、Introduction、Conclusion，是论文最核心的效果数字。[R1 提出, R2 强烈同意]

**W4. [Critical] "Non-monotonic" scaling pattern 仅基于 3 个数据点，over-interpreted。**
Scale-dependent evidence tax 基于 Qwen3 的 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28），无法区分 non-monotonic pattern 与噪声。1.7B 的 +8.04 有替代解释：44.4% repetitive outputs（Limitations 承认）可能人为压低 no-evidence baseline。Abstract "+8pp" 在正文被修正为 fair subset "+6.2pp"（缩水 22%），fair subset 细节缺失。1.7B w/evi (47.86) 高于 4B w/evi (39.74) 这一反直觉结果未被讨论。[R1 提出, R2 强烈同意]

**W5. [Critical] EDCR 与 Rel-F1 的相关性存在定义循环。**
EDCR = Evi-Recall_TP / Rel-Recall，而 Rel-F1 是 Rel-Recall 和 Rel-Precision 的调和平均。ρ=-0.965 部分由定义关系预设，非完全经验发现。当 Rel-Recall 极低时（GRPO QLoRA = 0.0138），EDCR 机械性趋近 1.0。论文将 EDCR 列为四项贡献之一（Contribution 2），但未展示 EDCR 相对于简单替代指标（如 Evi-F1 - Rel-F1 差值）的增量诊断价值。此外，per-relation EDCR 与 Evi-F1 "不显著相关" 被解释为 "fully decoupled"，存在 absence of evidence ≠ evidence of absence 的逻辑错误。[R2 提出, R1 强烈同意]

**W6. [Critical] CED 与 flat-NLI 几乎无差异（0.02pp），论文自身消融否定了 CED 作为独立贡献。**
CED Rel-F1 0.4563 vs flat-NLI 0.4561，差距 0.02pp，在任何合理方差下不显著。论文承认 "comparable outcomes" 但仍在 Contribution 4 将 CED 作为核心贡献。Contrastive component 增加方法复杂度但无可测量改进。论文声称的 "interpretable per-triple discrimination" 优势未在任何实验中展示实际价值。[R2 提出, R1 强烈同意]

**W7. [Critical] RSFT 训练数据量存在不可调和的数值矛盾。**
§3.3 报告 "9,042 training examples (37.3% acceptance rate)"，Appendix Table 5 报告 "Training samples: 2,718"。数学核实：k=1 from ~3,027 docs 最多产生 ~3,027 samples（与 2,718 一致），9,042 ≈ 3,027 × 3 更像 k=3。两个数字有 3.3 倍差距，影响可复现性。[R2 提出, R1 核实数学矛盾]

### Should-Fix（影响评分但不一票否决）

**W8.** EDCR ρ=-0.965 仅基于 n=6，去除 GRPO QLoRA outlier 后（n=5 甚至 n=4，考虑 DPO 3ep 不同 protocol）几乎肯定不显著。[R1 提出, R2 同意]

**W9.** "1.7B RSFT matches 8B SFT" (50.50 vs 50.51) 基于单 seed，0.01pp 差异远小于合理方差。出现在 Abstract/Introduction/Conclusion。应改为 "approaches"。[R1 提出, R2 同意]

**W10.** Baseline 对比不完整：缺少与 SAIS/DREEAM/EIDER 的直接表格化对比（DREEAM 54.01% vs 本文 ~36% 被埋在文字中），缺少 LLM-based DocRE baseline。[R1 提出, R2 同意]

**W11.** GRPO/DPO 超参数探索不足（GRPO 仅 KL=0.01, DPO 仅 β=0.1）。如果替代超参数下不出现 decoupling，核心叙事被否定。[R1 提出, R2 同意但认为可降一级]

**W12.** 指标格式严重不一致：Ign-F1 百分比(39.74)、Rel-F1 小数(0.4049)、Evi-F1 百分比(79.86) 混用，贯穿全文所有表格。[R2 提出, R1 同意]

**W13.** 引用数量偏低（32 篇，EMNLP long paper 通常 40-60 篇），15/32 条 "and others"，2 条 Anonymous（autore2024 已发表有真实作者），5 条作者信息与 OpenAlex 不匹配。[R2 提出, R1 核实具体错误]

**W14.** 1.7B evidence benefit 的 "implicit regularization" 解释是推测性的（§4.4 "We hypothesize"），无实验支撑。"Fair evaluation subset" 仅一句提及，无定义和完整数据。[R2 提出, R1 同意]

**W15.** Multi-seed 覆盖不均匀：4B 有 4-seed，1.7B/8B/LLaMA 为单 seed。Table 3 scaling analysis 的 4 行数据有 3 行基于单次实验。[R2 提出, R1 同意]

**W16.** Related Work 缺少 multi-task learning / task interference 文献（核心发现本质上是 negative transfer），缺少 self-consistency 范式引用。[R2 提出, R1 同意]

**W17.** "pre-D076 evaluation protocol" 是内部编号，不应出现在投稿论文中。DPO 3ep 不同 protocol 却纳入 spectrum 分析，污染相关性计算。[R2 提出, R1 同意]

**W18.** RSFT ablation 缺少 random selection baseline。[R1 提出, R2 部分 REBUT：k=3 vs k=1 已间接回答，SFT 近似 no-selection baseline，但仍建议补充 explicit random-k=1]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识：

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| GRPO 混淆变量 (W1) | N1 [AGREE] | 交叉 [AGREE] | 补实验或降级表述 |
| Dev-set only (W2) | N2 [AGREE] | N4 [AGREE] | 必须提交 test set |
| SFT 缺 multi-seed (W3) | N3 [AGREE] | 交叉 [AGREE] | 必须补 seed + 统计检验 |
| Non-monotonic over-interpreted (W4) | N4 [AGREE] | 交叉 [AGREE] | 增加数据点或降级 claim |
| EDCR 定义循环 (W5) | 交叉 [AGREE] | N1 [AGREE] | 提供增量诊断价值证据 |
| CED ≈ flat-NLI (W6) | W3 [AGREE] | N2 [AGREE] | 降级 CED 贡献定位 |
| 数据量矛盾 (W7) | 小问题 [AGREE] | N3 [AGREE] | 修正数字 |
| Overall 评分 | 3.0 | 3.0 | **Findings** |

## Reviewer Divergence

仅一处轻微分歧：

| 问题 | R1 | R2 | 分歧 |
|------|----|----|------|
| Random selection baseline (W18) | W5: 应补充 | REBUT: k=3 vs k=1 已间接回答 | R2 认为不是必需的但 "仍建议补充"，实质上是同意方向、分歧在严重程度 |

---

## Questions（需要作者澄清）

1. RSFT 训练数据量到底是 9,042 还是 2,718？差异来源是什么？
2. "Fair evaluation subset"（§4.4）的构建方法、样本量和完整结果？
3. 1.7B no-evidence 模型的 repetition rate 是多少？排除重复输出后 evidence tax 还是 +8pp 吗？
4. GRPO bf16 G=8 的 EDCR (0.6318) 低于 SFT (0.6982)，如何解释 GRPO 在 spectrum 中被归为比 SFT 更严重的 decoupling？
5. DPO 3-epoch 使用的 "pre-D076 evaluation protocol" 具体是什么？与当前 protocol 有何差异？
6. EDCR 去除 GRPO QLoRA outlier 后的 Spearman ρ 是多少？
7. 1.7B with evidence (47.86) 高于 4B with evidence (39.74) 的原因？是否暗示 scale 间训练配置不等价？

---

## Missing References

两位 Reviewer 共同建议补充以下方向的引用：

**Multi-task learning / task interference**（核心发现的理论框架）：
- Ruder (2017) "An Overview of Multi-Task Learning in Deep Neural Networks"
- Standley et al. (2020) "Which Tasks Should Be Learned Together in Multi-Task Learning?"
- Yu et al. (2020) "Gradient Surgery for Multi-Task Learning"
- Fifty et al. (2021) "Efficiently Identifying Task Groupings for Multi-Task Learning"

**Chain-of-thought / faithful reasoning**：
- Wang et al. (2023) "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
- Lanham et al. (2023) "Measuring Faithfulness in Chain-of-Thought Reasoning"

**Encoder-based DocRE 数值对比**：应在表格中直接呈现 SAIS/DREEAM/EIDER 数字

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**评分：3.0 (Findings)**

**置信度：高（4/5）**

两位 Reviewer 评分完全一致（3.0），交叉回应后共识进一步强化。

**核心判断**：论文提出了一个有价值的研究问题（LLM-based DocRE 的 evidence 可验证性），实验覆盖面令人印象深刻，scale-dependent evidence tax 和 RSFT discrete selection 的洞察有启发性。但论文存在系统性的 **claim 强度超过证据支撑力度** 的问题：

1. **统计严谨性不足**：SFT 单 seed、n=6 相关性、3 点 non-monotonic claim、单 seed cross-scale 比较、全文无显著性检验
2. **混淆变量未解耦**：GRPO 的 quantization vs group size、1.7B 的 repetition vs evidence benefit
3. **贡献声明过度**：CED ≈ flat-NLI（自身消融否定）、EDCR 定义循环性、"matches" vs "approaches"
4. **可复现性障碍**：dev-set only、训练数据量矛盾（9,042 vs 2,718）、内部编号（D076）泄露

**升级路径**：如果能 (1) 提交 test set 结果，(2) 补充 SFT multi-seed + 统计检验，(3) 解耦 GRPO 实验或降级因果 claim，(4) 修正数据矛盾和 CED 贡献定位，论文有潜力升至 3.5 (Borderline Conference)。当前状态适合 Findings。

---

## Detailed Comments

### Abstract
- 约 230 words，符合长度要求但数据密集。"Three findings emerge" 后连续三段各带具体数字，读起来像实验摘要而非叙事
- "+8pp Ign-F1 benefit at 1.7B" 在正文 fair subset 上为 +6.2pp，Abstract 应使用更保守数字
- "50.50 Ign-F1 matches 8B SFT performance (50.51)" 基于单 seed，统计上无意义

### Introduction
- 叙事结构清晰（gap → formalization → findings → contributions），无 "AI 写作" 痕迹
- Contribution 2（EDCR）和 Contribution 4（CED scoring）的贡献声明强度需要与 Analysis 消融结果对齐
- "QLoRA acts as a catastrophic amplifier" (L30) 是未经验证的因果 claim

### Related Work
- Positioning 有效（encoder-based evidence vs LLM generation 的结构性差异讲得清楚）
- 缺少 multi-task learning / task interference 文献——核心发现本质上是 negative transfer
- 引用密度偏低（32 篇），bib 条目质量有问题（15 条 "and others"，5 条作者错误）

### Method
- Task formulation (§3.1) 清晰合理
- CED (§3.4) 设计合理但消融显示 contrastive component 无增量贡献
- EDCR (§3.5) 定义有循环性问题，需增量诊断价值论证
- RSFT (§3.3) 训练数据量 9,042 vs Appendix 2,718 矛盾

### Experiments
- Main results (Table 1)：格式不一致（百分比/小数混用）；SFT 单 seed 无方差
- Decoupling spectrum (Table 2)：GRPO 混淆变量；DPO 3ep 不同 protocol；n=6 相关性分析 power 不足
- Scaling (Table 3)：3 点不足以建立 non-monotonic claim；1.7B benefit 有 repetition artifact 替代解释
- Evidence strategy (§4.5)：inference-time CED reranking 在 Method 中无描述
- Generalization (§4.6)：DREEAM 对比被埋在文字中，不在表格

### Analysis
- EDCR diagnostic 的核心论证受定义循环性影响
- CED granularity 负面发现（sentence-level 失败）有价值但不支撑 CED 优于 flat-NLI
- Practical implications 段的三条建议合理但证据基础不够牢固

### Formatting
- 模板正确（ACL review mode），匿名化完成
- Limitations section 位置正确，内容诚实
- 缺少 Responsible NLP Checklist（ARR 硬性要求，desk reject 风险）
- 缺少 Ethics Statement（ARR 鼓励但不强制）
- Appendix Figure caption relation type 数字矛盾（93 vs 76 vs 96）