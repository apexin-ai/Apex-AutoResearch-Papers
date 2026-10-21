---
round: 49
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T23:59:02.186048+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 49 Consolidated Review Report

**论文**: "Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text"
**Venue**: EMNLP 2026 (ARR), Long Paper
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人 — R1 方法严谨性, R2 新颖性与完整性

---

## Summary

本文提出 depth profiling——对 base-model LLM 递归生成文本的深度进行分类——并引入 Differential Depth Response (DDR) 框架，将 7 个统计特征分解为 drifting（随深度单调漂移：entropy_mean, TTR, hapax_ratio）和 near-stationary（高阶矩稳定：entropy_max, entropy_min, entropy_std, tail_decay）两类。在 8 个 base model（5 个架构家族）上的 LOGO 评估报告 binary F1=0.694、3-class F1=0.762（handcrafted 特征）和 3-class F1=0.905（QLoRA end-to-end）。24 页附录提供了极为详尽的验证实验。

## Strengths

1. **任务定义新颖**: Depth profiling 将 binary AI text detection 扩展为 ordinal depth estimation，填补 human-vs-machine 与 model collapse 研究之间的空白。DDR 的 drifting/near-stationary 二分法提供了超越分类的可解释分析视角。(R1+R2 共识)

2. **DDR 分解经验验证扎实**: 多层统计验证——TOST 等价检验、two-way ANOVA（depth 解释 34-37% location-feature 方差，generator identity <1%）、Granger 因果、k-means 聚类、PCA、holdout generator split——达到高标准的 empirical rigor。(R1+R2 共识)

3. **评估协议严谨**: LOGO（Leave-One-Generator-Out）是比 random split 更有意义的泛化测试。Binary F1（排除 "easy" gen-0）作为 conservative primary metric 避免了 3-class F1 被 gen-0 inflate。(R1+R2 共识)

4. **24 页附录覆盖极其全面**: DDR partition 验证、robustness（perturbation, cross-temperature, cross-domain, instruction-tuning）、feature screening、confusion matrix、downstream utility、scale 实验等。在 empirical study 中罕见的 thoroughness。(R1+R2 共识)

5. **诚实的局限性讨论**: Limitations 透明报告 base-model scope、fixed decoding、English-only。Downstream utility 的 null result 被正面讨论。(R2)

6. **统计方法论全面**: Bonferroni 校正、bootstrap CI、Cohen's d、TOST、ANOVA、permutation importance、Granger causality 覆盖到位。(R1)

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [R1-N1, R2 AGREE] **LOGO CI 可能低估 generator-level 泛化不确定性**
- Binary LOGO F1=0.694, 95% CI [0.685, 0.703], 宽度仅 0.018
- Per-generator F1 范围 0.633–0.724, SD=0.028
- Generator-level CI ≈ [0.675, 0.713], 宽度 0.038, 约为报告 CI 的两倍
- Bootstrap 单位（text-level vs generator-fold-level）未明确说明
- 修复方向: 明确 CI bootstrap 单位；补充 generator-level CI；讨论差异含义

**MF2** [R1-N2 + R2-N2 + R2-W2, 双方共识] **泛化性措辞超出实验范围**
- 实验范围: 8 个 ≤8B base model、5 家族、英文 Wikipedia、固定解码
- Abstract "essential for data provenance and corpus curation" overclaim
- Conclusion "DDR constitutes a new analytical dimension for corpus auditing" 暗示通用部署
- Instruction-tuning: 3-class F1 从 ~0.76 降至 ~0.45-0.54 (Appendix k)，主文 Limitations 仅一句话
- Cross-domain: 仅 3 generators × 200 seeds/domain，规模有限
- 修复方向: Abstract/Conclusion 加限定语；Limitations 补 instruction-tuning 具体数字；cross-domain 标注 pilot study

**MF3** [R2-N1, R1 PARTIAL REBUT — 分歧记录] **DDR 新颖性定位——描述性发现缺 mechanistic grounding**
- R2: DDR 可被一句话总结（"某些特征漂移、某些不漂移"），novelty 在 Conference 门槛边界
- R1 反驳: DDR 分解非 trivial，包含系统验证框架和方法论指导（LOFO 验证 shape 特征在 perturbation 下更稳健），远非一句话可概括
- 共识: 缺乏 mechanistic explanation（为什么 location 漂移而 shape 不漂移），Discussion 应补充
- 修复方向: Discussion 加强 mechanistic intuition

**MF4** [R2-N2, R1 AGREE] **实际应用动机与受控实验之间的 gap**
- Downstream utility (Appendix m): depth-aware curation 仅降低 perplexity ~2%
- 从 "signal exists" 到 "essential for curation" 缺少: wild data 鲁棒性、pipeline 集成、误分类 downstream cost
- 修复方向: 降低应用性声明或 Discussion 增加 deployment prerequisites 讨论

### Should-Fix（影响评分但不一票否决）

**SF1** [R1-W1, R2 AGREE] TOST margin |d|≤0.20 缺 task-specific 理据——d=0.20 在 depth profiling 语境下的实际意义未解释

**SF2** [R1-W2, R2 AGREE] 特征冗余性未充分讨论——entropy_mean 与 hapax_ratio r=0.81；PCA 前 3 drifting 特征占 92.3% 方差；LOFO 最大 drop 仅 0.05pp。缺 forward selection 或 minimal sufficient subset 分析

**SF3** [R1-W3 + R2-W3, 观察一致] 3→5 class 分辨率天花板——5-class F1 从 0.762 降至 0.521，gen-2+ 内部混淆严重。R2 认为 "depth profiling 名不副实"（仅 binary），R1 rebut 3-class 有独立意义。共识: 主文应更明确承认有效分辨粒度为 3-class

**SF4** [R2-W1, R1 AGREE] Concurrent works 区分度论述过于简略——Table 48 停留在表面特征对比，缺 finding-level 实证对比

**SF5** [R1-W4 + R2-W4, 分歧] QLoRA 与 XGBoost 比较 framing——R1 强调信息量不对等（7 标量 vs 完整 token 序列）+ LOGO fold 数差异；R2 认为方向正确可更清晰。共识: Table 3 应标注 feature type

**SF6** [R1-W5 + R2-Minor-2] Primary metric 未明确声明——Abstract 同时出现 0.694/0.762/0.905，读者难以判断核心指标

**SF7** [R2-W4, R1 REBUT] Handcrafted vs end-to-end trade-off 讨论不足——R1 强调可解释性是核心定位，应在主文更充分讨论

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：
- MF1: LOGO CI bootstrap 单位需澄清
- MF2: 泛化性 claim 需收窄
- MF4: 应用动机 claim 需降低或增加 deployment prerequisites
- SF1-SF4, SF6: 均达成一致
- Missing References: 4 条均达成共识

## Reviewer Divergence

1. **DDR novelty (MF3)**: R2 认为 novelty 不足（描述性）；R1 认为验证框架有方法论价值。共识方向: 补充 mechanistic explanation
2. **3-class 可区分性 (SF3)**: R2 "名不副实"；R1 反驳 3-class 有意义。共识方向: 主文明确分辨粒度
3. **QLoRA framing (SF5)**: R1 强调不公平对比；R2 认为方向正确但可改进
4. **附录长度**: R2 认为比例过大；R1 认为 empirical study 必需（不影响评分）

## Questions

1. Table 2 CI 的 bootstrap 抽样单位是 text-level 还是 generator fold？(R1-Q1)
2. TOST d=0.20 在原始特征尺度上对应多大变化？(R1-Q2)
3. Instruction-tuning 导致 DDR 模式被破坏还是信号被压缩？(R1-Q3 + R2-Q3)
4. 完整 pipeline per-text 推断成本？(R1-Q4)
5. F1=0.694 的 30% 错误率在不同应用场景下的可接受性？(R2-Q4)
6. DDR 分解的理论基础——为什么 location 漂移 shape 不漂移？(R2-Q1)
7. 非 Wikipedia seed 下 DDR 分解模式是否一致？(R2-Q2)

## Missing References

1. **Schaeffer et al. (2025)** "Position: Model Collapse Does Not Mean What You Think" — model collapse 定义多样性，与 Section 2.2 直接相关 (R2+R1 AGREE)
2. **Hans et al. (2024) Binoculars** — 已在 bib 但 Related Work 未讨论 cross-perplexity ratio 与 DDR NLL 的方法论相似性 (R1+R2 AGREE)
3. **Paraphrase/rewriting attack 文献** — recursive generation 类似 iterative paraphrasing，Related Work 未讨论 (R1+R2 AGREE)
4. **Fine-grained span-level AI text detection** — 与 depth profiling 在粒度扩展上有类比 (R2+R1 AGREE)

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用）。

## Visual Layout Check（非评分项）

视觉审查已完成。**0 critical, 0 warning, 18 info**。主要发现：
- Pages 3-5 文字密度较高（近 3 页密集文字），Figure 2/Table 2/Figure 3 集中在 page 6，视觉节奏分配不均
- Figure 1 框架图内部文字偏小，打印后可能需放大辨认
- Figure 2 子图 axis label 和 legend 字号偏小（~7pt），接近可读性下限
- 主文 8 页，display items 7 个（4 figure + 3 table），密度合理
- 无 margin 溢出、未解析引用或编译残留问题
- 颜色方案可区分，无色盲不友好配色
- 参考文献排版正常，双栏格式整齐

## Overall Assessment

**评分**: 3.5 / 5 — Borderline Conference
**R1**: 3.5 (Soundness 3.5, Excitement 3.5, Reproducibility 4, Confidence 4)
**R2**: 3.5 (Soundness 3.5, Excitement 3, Reproducibility 4, Confidence 4)

**理由**: 论文定义了一个新颖且有意义的任务（depth profiling），DDR 分解通过多层统计验证展示了令人信服的 empirical rigor，24 页附录体现了罕见的 thoroughness。然而：(1) 核心贡献偏描述性，缺乏 mechanistic grounding；(2) 泛化性 claim 超出实验范围（仅 ≤8B base model、英文 Wikipedia）；(3) 应用价值论证不足（downstream utility 近乎 null result）；(4) LOGO CI 可能低估 generator-level 不确定性。论文在 **实验执行的 thoroughness** 与 **contribution 的 novelty/impact** 之间存在不匹配——前者达到 Conference 水平，后者处于 Findings 边界。

**建议**: 如果作者能 (1) 收窄泛化性 claim，(2) 补充 DDR mechanistic intuition，(3) 明确 CI bootstrap 方法，(4) 降低应用性声明——可提升至 3.5-4.0 范围。当前状态适合 EMNLP Findings 接收。

## Detailed Comments

**Abstract**: "essential for data provenance" overclaim (MF2)；多个 F1 数字造成困惑 (SF6)；"Base-Model" 位置偏后 (MF2)

**Section 1 (Introduction)**: Scope 声明存在但显著性不够；Contributions 定位为 "descriptive empirical finding" 但 Discussion/Abstract 应用性措辞矛盾 (MF3+MF4)

**Section 2 (Related Work)**: Concurrent works 对比仅半段话 (SF4)；Binoculars 已引用但正文未讨论方法论相似性 (MR2)

**Section 3 (Method)**: LOGO 协议设计合理；特征选取有理据但冗余性未讨论 (SF2)；d 符号重载（generation depth vs Cohen's d）

**Section 4 (Results)**: 4.1 CI bootstrap 单位未说明 (MF1)；3-class 分辨率天花板未充分讨论 (SF3)。4.2 DDR 分解验证充分；TOST margin 缺 task-specific 理据 (SF1)。4.3 QLoRA 比较 framing 可改进 (SF5)

**Section 5 (Discussion)**: "corpus auditing" overclaim (MF2)；缺 DDR mechanistic explanation (MF3)；downstream null result 报告诚实但 motivation 仍偏强 (MF4)

**Section 6 (Conclusion)**: 泛化性措辞需加限定语 (MF2)

**Limitations**: Instruction-tuning 降级仅一句话缺具体数字 (MF2)；English-only 限制缺实验支撑

**Appendix**: 总体质量高；Appendix j 规模有限应标注 pilot study；Appendix k 关键数据应提到主文