---
round: 6
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-21T05:15:52.220987+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 6 (Fresh)

**论文**: DisPeD: Disentangling Persuasion-Based Multi-Turn Jailbreak Detection via Domain-Adaptive Pretraining  
**Venue**: EMNLP 2026 (ARR May 2026 cycle)  
**审稿模式**: Fresh (无上轮记忆)  
**Reviewer 配置**: 2人 — R1(方法严谨性/实验设计), R2(新颖性/完整性/positioning)  
**收敛**: Round 1 达成共识，无需额外轮次

---

## Summary

本文提出 DisPeD，一个两阶段框架用于检测多轮 persuasion-based jailbreak 攻击。Stage 1 对 DeBERTa-v3-base 进行 7 种不同目标的 continued pretraining（9-class persuasion 分类、binary、scrambled labels、MLM、topic、Wiki MLM、vanilla）；Stage 2 冻结 encoder 后用 BiGRU+MLP 做 conversation-level 二分类。核心发现：classification-based DAPT 提供最强 OOD 泛化；MLM domain exposure 关闭约 60pp gap 但在 mixed-LLM 下崩溃；label correctness 和 temporal order 对检测无显著影响。论文在 4 个攻击家族上评估，包含 ToxicChat 人类数据验证和 cross-LLM 实验。

---

## Strengths

1. **系统性消融设计 (S1)**: 7 个 Stage-1 变体精确隔离单一因素（domain exposure vs. supervision vs. label correctness vs. granularity vs. domain specificity），实验设计严谨，在该领域少见。

2. **负面结果的科学价值 (S2)**: Label correctness 无关（scrambled ≈ correct）、temporal order 无关（shuffle Δ<1pp）、domain specificity matters（Wiki MLM 失败）——这些约束后续研究的设计空间。

3. **多层次统计验证 (S3)**: TOST 等价检验、BCa bootstrap CI、McNemar's test、paired permutation test——统计方法论在 NLP 安全论文中领先。

4. **实用性论证 (S4)**: 266× inference speedup over LLM-as-judge，附 WildChat FPR 分析诚实暴露部署局限。

5. **透明的局限性 (S5)**: Limitations section 覆盖 15 个独立段落，坦诚承认 single-LLM confound、WildChat FPR≥44%、synthetic-only multi-turn 等核心弱点。

---

## Weaknesses

### Must-Fix (阻碍接收)

**W1. 标准差计算自相矛盾 [Critical]**  
- `experiments.tex` L27: "population formula ($n$ divisor)"  
- `checklist.tex` L19: "sample standard deviation with Bessel's correction, $N{-}1$ divisor"  
- `appendix.tex` Table 26 caption: "sample std with $n{-}1$ divisor"  
三处描述互相矛盾。对 n=3 seeds，两种公式差异达 ~22%，直接影响所有置信区间和等价检验结论的可信度。  
**共识**: 两位 Reviewer 一致认定为 Critical，必须统一并重新验证所有报告值。

**W2. OOD 评估的 benign 分布混淆 [Critical]**  
所有 "OOD" 评估保持 benign 分布不变（同源 Qwen3-8B），仅变换攻击类型。这意味着模型可能学到 "非 Qwen-benign 即攻击" 的 shortcut，而非真正的攻击特征。WildChat 实验（FPR≥44%, ROC AUC=0.700）证实了这一担忧。论文虽承认此问题，但主文 claims 未充分限定——"cross-attack generalization" 的表述暗示了比实际更强的泛化能力。  
**共识**: 两位 Reviewer 均认为需要在 Abstract/Intro/Conclusion 的 claim 中明确限定 "OOD" 的含义。

**W3. 单一 LLM 生成全部数据 [Major → Critical]**  
训练和评估数据均由 Qwen3-8B 生成。Cross-LLM 实验（Llama-3.1-8B）显示 benign 替换后 F1 暴跌至 0.370-0.430。这不仅是 limitation，而是对核心 claim 的根本威胁：所谓 "domain-adaptive pretraining" 可能主要是 "Qwen-style-adaptive pretraining"。  
**共识**: 两位 Reviewer 同意 cross-LLM 实验已部分缓解（mixed-LLM DD F1=0.818），但主文 claim 仍需 qualify。

**W4. TOST 等价检验失败与不合格 claims [Major]**  
9-class vs. Binary 的 TOST 在 ActorAttack 上失败（CI 包含 0.1），但论文仍声称 "equivalence"。统计检验不支持的结论不应以 unqualified 形式出现在 findings 中。  
**共识**: R1 提出，R2 同意——需修改措辞或移除等价声称。

**W5. Capacity-architecture 混淆 [Major]**  
Cross-encoder 实验用 3 个不同架构的 encoder（DeBERTa-v3-base 184M, BERT-base 110M, RoBERTa-large 355M），声称 "larger encoders need less adaptation"。但 RoBERTa-large 与 DeBERTa-v3-base 不仅 size 不同，pretraining corpus/objective/tokenizer 也不同。需 same-architecture scaling（如 DeBERTa-base vs. DeBERTa-large）才能归因于 capacity。  
**共识**: R1 提出为 Must-Fix，R2 认为 Should-Fix 但同意措辞应更 cautious。最终判定: 需修改 claim 措辞。

### Should-Fix (不阻碍接收但影响评分)

**W6. DAPT 新颖性边界模糊**  
Gururangan et al. (2020) 已证明 domain-adaptive pretraining 的有效性。本文的核心贡献是将其应用于 jailbreak detection 并进行消融，但"应用已知方法到新领域 + 消融"的新颖性在 EMNLP main 中需更强的 positioning。Related Work 未充分论证为何此消融在方法论上是 novel（而非仅仅 useful）。  
**共识**: R2 提出，R1 建议 Should-Fix 级别——需在 Introduction 中更清晰地 position contribution 为 "systematic disentanglement" 而非 "new method"。

**W7. 标题过度承诺**  
"Disentangling Persuasion-Based Multi-Turn Jailbreak Detection" 暗示 persuasion taxonomy 是检测的关键。但实验证明 label correctness 无关、scrambled 等效——即 persuasion 分类本身对检测贡献有限，domain exposure 才是关键因素。标题应反映实际发现。

**W8. Discussion section 过薄**  
3 个 paragraph 的 Discussion 与 15 段 Limitations 相比极度不平衡。关键 implications（为何 scrambled=correct? 为何 MLM 在 mixed-LLM 下崩溃?）缺乏深入分析。

**W9. WildChat FPR 部署影响未充分讨论**  
FPR≥44% 在实际部署中意味着近半数正常对话被误拦，这对 "practical alternative for multi-turn safety monitoring"（Conclusion 原文）的 claim 构成直接矛盾。需要在 Conclusion 中限定适用条件。

**W10. BiGRU temporal aggregation 与 order-invariance 矛盾**  
Section 5 的 decomposition 证明 shuffle 无影响（Δ<1pp），即 temporal order 无关。那么为何使用 BiGRU（专为序列建模设计）而非简单 mean pooling？论文承认 "mean pooling matches BiGRU" 但未解释为何仍选择更复杂的架构作为 default。

**W11. IAA 验证样本量不足**  
Strategy annotation 的 IAA 仅基于 n=50 样本，Cohen's κ=0.78。对 9-class taxonomy 而言，50 个样本每类平均仅 5-6 个，置信区间极宽。

### Minor

**W12.** Perturbation evaluation n=76 underpowered（论文已承认）。  
**W13.** 缺少 RED QUEEN (Ren et al., 2025) 等近期 multi-turn defense 的引用。  
**W14.** Page 8 过度压缩——Discussion/Conclusion/Limitations 三个 section 起始于同一页，影响可读性。

---

## Reviewer Consensus

两位 Reviewer 在以下关键判断上达成一致：
- Overall 3.0 (Findings)
- W1 (std 矛盾) 为 Critical，必须修复
- W2 (benign OOD confound) 需要 claim qualification
- W3 (single LLM) 已部分缓解但 claims 仍需限定
- W4 (TOST failure) 需修改措辞
- 消融设计是主要优势
- 负面结果有科学价值
- 论文不满足 EMNLP main 的新颖性门槛但适合 Findings

## Reviewer Divergence

| 议题 | R1 | R2 | 解决 |
|------|----|----|------|
| 9-class taxonomy 价值 | 有独立解释性价值 | 被 scrambled=correct 削弱 | 保留分歧，不影响评分 |
| Frozen encoder 是否为 limitation | 是——限制了实用性上界 | 否——设计选择服务于消融公平性 | R2 论据更强，降级为 minor |
| W5 严重程度 | Must-Fix | Should-Fix | 折中：需修改 claim 措辞 |

---

## Questions for Authors

1. 请确认所有报告的 std 使用的是 population ($n$) 还是 sample ($n-1$) divisor，并说明为何三处描述不一致。
2. 如果 scrambled labels ≈ correct labels，那么 9-class taxonomy 的 scientific contribution 具体是什么？是否应重新定位为 "interpretability aid" 而非 "detection enabler"？
3. Cross-LLM 实验中 mixed-LLM training 仅测试了 2 个 LLM。需要多少个 LLM 才能声称方法具有 LLM-agnostic 的泛化能力？
4. WildChat FPR≥44% 下，论文 Conclusion 中 "practical alternative" 的 claim 如何成立？
5. 为何 mean pooling=BiGRU 后仍选择 BiGRU 作为默认架构？

---

## Missing References

- RED QUEEN: Ren et al. (2025) — multi-turn jailbreak defense with exogenous safety signals
- MultiBreak: Song et al. (2026) — 论文引用但未充分对比实验设置差异
- Constitutional Classifiers (Anthropic, 2025) — 已引用但未讨论其 multi-turn 局限
- Adaptive attacks literature (Tramer et al., 2020) — 未讨论 adaptive adversary 下的鲁棒性

---

## External Review

**状态**: 未请求（项目配置未启用外部审稿）

---

## Visual Layout Check

**状态**: 已完成 (4 warnings, 0 critical)

| # | 位置 | 发现 | 严重度 |
|---|------|------|--------|
| 1 | Pages 1, 3 | 纯文本页面缺乏视觉锚点（无 figure/table） | Warning |
| 2 | Figure 2 | 柱状图 x 轴标签字号偏小，密集排列可读性差 | Warning |
| 3 | Page 8 | Discussion + Conclusion + Limitations 三节起始于同一页，极度压缩 | Warning |
| 4 | Pages 9-10 | Limitations 连续纯文本，缺乏结构化视觉辅助 | Warning |

*注: 视觉审查为参考项，不纳入评分。*

---

## Overall Assessment

**评分: 3.0 — Findings**

**理由**: 论文提供了有价值的系统性消融，负面结果（label correctness 无关、temporal order 无关）对领域有 constraining contribution。但存在以下阻碍 main conference 接收的问题：(1) 核心统计报告自相矛盾，削弱所有定量结论的可信度；(2) OOD 评估设计存在 benign 分布混淆，使 "cross-attack generalization" claim 的实际覆盖范围远小于表述；(3) 方法论新颖性有限——DAPT 是已知技术，贡献主要在应用+消融层面；(4) WildChat 实验暴露实际部署困难（FPR≥44%），与 "practical alternative" 的 claim 矛盾。消融设计的严谨性和负面结果的科学价值支撑 Findings 接收，但 claim 需全面 qualify。

**Confidence**: High (两位 Reviewer 独立得出相同评分并在交叉讨论后确认)

---

*审稿完成。Report by Review Director, Round 6.*