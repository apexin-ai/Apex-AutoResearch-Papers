---
round: 26
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T06:38:17.293140+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 26 (Fresh Review)

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 (ACL Rolling Review)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析；R2: 新颖性+完整性+写作质量+格式合规）
**审稿轮次**: Round 1 独立审稿 + 交叉分享回应，1 轮收敛

---

## Summary

本文提出 generation depth classification 任务，将 LLM 生成文本检测从二元分类（human vs. machine）扩展为按递归生成深度分类（gen-0/gen-1/gen-2+）。在 8 个 base model（0.6B-8B，5 个家族）上提取 7 个手工特征，发现 differential depth response (DDR) 三分结构（drifting/intermediate/near-stationary），用 XGBoost 在 LOGO 评估下达到 binary F1=0.694。论文实验设计严谨、统计方法规范、负面结果诚实报告，附录消融覆盖度在同类论文中属上乘。但新颖性在三篇并行工作背景下增量有限，方法仅适用于小型 base model，实用价值受限，存在两个可能导致 desk reject 的格式问题。

---

## Strengths

**S1 [实验设计严谨，控制变量全面]** Seed sharing control（independent-seed F1=0.680）、length confound control（length-matched F1=0.724）、cross-reference model validation（spread ≤0.013）、LOGO + LOFO 双层 cross-validation。统计方法涵盖 Bonferroni 校正、Cohen's d、Glass's Δ、Cliff's δ、TOST 等价性检验、bootstrap CI，远超同类 NLP 论文水平。**[R1-S2, R2-S1, 共识]**

**S2 [消融实验覆盖度高]** 29 页附录覆盖长度控制、种子独立性、温度敏感性、跨领域泛化、LOFO 特征消融、UMAP 可视化、词替换鲁棒性、LLM 模拟编辑、cross-temperature transfer 等。这种覆盖度在同类工作中较为少见。**[R1-S3]**

**S3 [诚实报告负面结果]** Downstream utility 实验明确显示 depth-aware curation 不优于 random subsampling；instruction tuning 使 DDR 结构退化（silhouette 0.632→0.338）；高温下方法性能大幅下降（-9.3 to -26.0 pp at t=0.9）。透明度增强了论文可信度。**[R1-S5, R2-S2, 共识]**

**S4 [DDR 框架具有分析价值]** 将 7 个特征按深度响应模式分为三类，提供了直观的信号分解，有助于理解递归生成的分布漂移机制。多角度验证：数据驱动 k-means（silhouette=0.632）、domain-informed 3/1/3 划分、per-generator TOST、holdout generator validation、PCA（PC1 explains 92.3%）。**[R1-S4, R2-S3, 共识]**

**S5 [叙事主线一致 + 写作质量高]** Abstract→Introduction→Method→Results→Discussion→Conclusion 形成连贯故事线，每个 contribution claim 都有对应实验支撑。无 AI 写作痕迹（无 em-dash、无 -ing phrase 句尾、无过渡词堆叠）。71 篇引用覆盖充分，57/71 通过 OpenAlex 验证，无虚假引用。**[R2-S4, R2-S5, R2-S6]**

---

## Weaknesses

### Desk Reject 风险（最高优先级）

**N1 [Critical, 格式] 缺少 Responsible NLP Research Checklist**
ARR 投稿要求必须包含 Responsible NLP Research Checklist，当前论文中未找到。缺失是 desk reject 的充分条件。**[R2-N1, R1 AGREE]**

**N2 [Critical, 格式] 正文约 8.3-8.4 页，超出 long paper 8 页限制**
§1-6 主文内容延伸至 page 9 中上部（Limitations 和 Ethics 不计入）。超页可能导致 desk reject。Discussion 中 informal conjecture（§5 L5-7）和 Results §4.2 中多种统计量的重复验证是最可能的压缩候选。**[R2-N2, R1 AGREE]**

### 新颖性与贡献（影响接收决定）

**N3 [Critical, 新颖性] 三篇并行工作背景下新颖性增量有限**
Broken Telephone (ACL 2025)、Markovian Chains (arXiv 2026)、Attractor Cycles (ACL 2025) 已独立发现 ~3-class ceiling。论文声称的三点区别（non-paraphrastic chains, DDR decomposition, "what vs. that converges"）中：(i) continuation chains 比 paraphrastic chains 更易区分（论文自己报告 paraphrastic F1=0.671 vs continuation 0.749），降低技术贡献；(ii) DDR 的 location/shape 分解在固定 temperature 下是理论可预期的（softmax temperature 控制 shape），论文自称 "post-hoc and empirical"。当前贡献更适合 Findings。**[R2-N3, R1 AGREE(附条件)]**

**N4 [Major, 方法] DDR 与已知 distributional drift 的本质区别不够清晰**
Model collapse 文献已记录 recursive generation 下的 vocabulary diversity 下降和 perplexity 压缩。DDR 的 drifting features（entropy mean, TTR, hapax ratio）本质上是这些已知现象的具体量化。DDR 更多是 empirical decomposition 而非新现象，论文需要更系统地对比 DDR 与已有文献发现的精确对应/区别。**[R2-W1, R1 AGREE]**

**N5 [Major, 方法] DDR 阈值缺乏理论基础 + location/shape 分离缺机制性解释**
论文的 3/1/3 partition 虽然有数据驱动 k-means（k=2, silhouette=0.632）和 d threshold gap（0.76 vs 0.55）支撑，经验稳健性在 [0.56, 0.75] 范围内已验证，但为什么 location 和 shape 会分离缺乏理论解释。Discussion 中的 temperature-as-shape-control 仅为 informal conjecture。R1 指出 entropy mean ρ=0.60 恰在边界，但 R2 纠正指出论文的 primary partition 基于 k-means 和 d 值而非 ρ cutoff，d 边界更稳健。两位 Reviewer 共识：经验分区有一定支持，但理论基础缺失是真正的弱点。**[R1-W1, R2 AGREE with nuance]**

### 实验与方法（影响评分）

**W1 [Critical→Major, 实验] Cross-model F1=0.764 存在 model-switching / generator identity confound**
Cross-model chains 中每一步使用不同生成器，引入 model-switching 效应。分类器可能检测 "depth + model-switching" 混合信号。5-fold sample-level CV 无法控制 generator identity leakage。且 cross-model 用 5-gen 而 LOGO 用 8-gen，条件不同使比较更不严谨。论文在 §4.1 承认但未控制。两位 Reviewer 独立提出并交叉确认。建议降低 cross-model F1 在叙事中的权重，或加入 generator-identity-controlled ablation。**[R1-W2 Critical, R2-W5 Major, 共识]**

**W2 [Major, 方法] Binary F1=0.694 实用意义有限 + QLoRA gap (F1=0.905)**
Binary F1=0.694 意味着每三次预测中约有一次错误。QLoRA 端到端分类器 21pp 的优势暴露了手工特征覆盖不足。R2 辩护主贡献是 DDR 分析框架而非分类性能，但也承认论文未量化 DDR 分解产生了哪些超出 "location drifts, shape stays" 的 actionable insight。R1 补充 Appendix 错误分析数据：depth-2 错误率 84.2%，gen-1/gen-2 transition 是 primary failure point。两位 Reviewer 共识 F1=0.694 不足以支撑实用工具定位。**[R1-W3 Major, R2-W2 Major, R2 partial REBUT]**

**W3 [Major, 实验] 模型规模限于 0.6B-8B，排除真实场景**
所有 8 个生成器均为小型 base model。真实世界 LLM 文本来自更大的 instruct model。Instruct model F1 降至 0.338（OLMo-2-1B instruct）。Instruct 分析未区分 RLHF vs SFT 退化来源。QLoRA 未在 instruct 上测试——这是关键实验缺口。**[R1-W4, R2 AGREE, R1-W8 补充]**

**W4 [Major, 实验] Generator subset 不一致 (5/6/8-gen) 增加解释复杂度**
5-gen (cross-model), 6-gen (appendix), 8-gen (main) 混用。每个表格有标注但跨实验比较困难。Table 29 subset 汇总位于附录末尾不易注意。建议 Method §3.4 加入 subset 对照表。**[R1-W5 Major, R2-W7 Minor, 共识]**

### 写作与格式

**W5 [Major, 写作] Abstract 约 132 words 偏短，缺少 "why important"，NLL 未定义**
低于 ACL/EMNLP 推荐的 150-250 words。缺少 depth classification 对 data provenance/curation 的具体意义。NLL 在 Abstract 中首次出现未展开定义（应为独立阅读单元）。**[R2-W3 Major, R2-W4 Major, R1 AGREE]**

---

## Reviewer Consensus

以下问题两位 Reviewer 达成明确共识（均标注 [AGREE]）：

1. **Overall 评分 3.0 (Findings)**：两位 Reviewer 独立给出相同评分
2. **Cross-model confound 是核心方法问题**：R1-W2 Critical + R2-W5 Major，交叉均 AGREE
3. **DDR 新颖性在并行工作背景下有限**：R2-N3 + R1 AGREE(附条件)
4. **Binary F1=0.694 不足以支撑实用定位**：R1-W3 + R2-W2，但 R2 辩护主贡献是分析框架
5. **Generator subset 不一致增加复杂度**：R1-W5 + R2-W7，交叉均 AGREE
6. **缺少 NLP Checklist + 超页**：R2 发现，R1 确认
7. **Base model 限制 + instruct 分析不足**：R1-W4 + R2 AGREE

## Reviewer Divergence

1. **Introduction 开头是否过于抽象**：R2-W6 Minor 认为过于抽象；R1 REBUT 认为开场已足够具体紧凑。**Review Director 判断**：R1 的 REBUT 更有说服力——§1 开头直接描述了核心研究现象，非泛泛介绍。不列为 weakness。

2. **Gen-0 seed sharing 数据泄漏的严重度**：R1-W6 Major 认为 3-class F1 可能误导；R2 REBUT 认为论文已充分处理（降级 metric + controls）。**Review Director 判断**：R2 的 REBUT 有理——论文明确采用 binary F1 为 primary metric、标注了 3-class 偏差、提供了 independent-seed control。列为 Minor 而非 Major。

3. **TOST ε=0.20 选择是否充分**：R1-W7 Minor 质疑；R2 REBUT 指出论文有 LOFO-based task-specific validation + sensitivity analysis。**Review Director 判断**：R2 的 REBUT 有理——论文的 dual justification 充分。不列为 weakness。

4. **Soundness 评分**：R1 给 3/5，R2 给 4/5。R2 认为 R1 低估了统计控制质量。**Review Director 判断**：3.5/5 更准确——统计方法论质量高，但 cross-model confound 和 DDR 理论基础缺失是实质性 soundness concern。

---

## Questions（需作者澄清）

**Q1** [R2-Q1, R1 AGREE(重要)] DDR 的 drifting/non-drifting partition 是否在 paraphrastic chains 上也成立？如果 DDR 是一个通用分析框架，需要在不同 chain 类型上验证。

**Q2** [R2-Q3, R1 AGREE(关键缺失)] QLoRA 是否在 instruction-tuned models 上测试过？如果 QLoRA 在 instruct 上仍有效，说明退化是手工特征局限；如果也退化，说明 depth signal 被根本消除。无论哪种结果都对论文 story 有重大影响。

**Q3** [R1-Q2, R2 AGREE] Cross-model 链中，depth effect vs. model-switching artifact 能否通过构造 "same-depth, different-generator" 对照实验分离？

**Q4** [R2-Q2, R1 AGREE] 是否可以通过比较不同 temperature 下 near-stationary features 的方差变化来验证 "temperature acts as shape control parameter" 假说？现有数据（t=0.7 和 t=1.0）应足以回答。

**Q5** [R1-Q3, R2 REBUT 纠正数字] LOFO 中 entropy_max（near-stationary）移除导致最大 F1 下降（-1.50pp，非 R1 所述 -3.70pp），如何解释 near-stationary 特征对分类的贡献？

---

## Missing References

1. **Ordinal classification 方法论**应在 Related Work 或 Method 中更早引入（当前仅在 §5 提及 Frank-Hall, CORAL, CORN 等）**[R1, R2 AGREE]**
2. **多粒度统计特征做 AI 文本检测的工作**（如 Zhu et al., 2023 "Beat LLMs at Their Own Game" 等）**[R1]**
3. **更多 ordinal classification 在 NLP 的应用引用**（readability assessment, stance detection 等）**[R2]**

注：R1 提到的 Dohmatob et al. (2024) 和 Fast-DetectGPT 经 R2 交叉验证已在论文中引用。

---

## External Review (Stanford Agentic Reviewer)

项目未配置外部审稿（`external_review.paperreview_ai.enabled` 不存在于项目配置中）。本轮无外部审稿结果。

---

## Overall Assessment

**Overall**: 3.0 (Findings)
**Soundness**: 3.5/5
**Excitement**: 2.5/5
**Confidence**: 4/5（两位 Reviewer 均为 4/5，交叉回应后关键问题达成共识）

### 评分理由

**论文适合 EMNLP 2026 Findings，不建议 Main Conference。**

**支撑 Findings (3.0) 的理由**：
- 问题定义（generation depth classification）有价值，是 binary detection 的自然扩展
- DDR 三分框架提供了有意义的分析视角（location vs. shape）
- 实验设计和统计方法论质量在 NLP 论文中属上乘
- 诚实报告负面结果和 boundary conditions

**不建议 Main Conference (4.0) 的理由**：
- 三篇并行工作已独立发现 ~3-class ceiling，DDR 的增量贡献有限
- DDR 的 location/shape 分解在固定 temperature 下理论上可预期，论文自称 post-hoc and empirical
- Binary F1=0.694 实用性有限，QLoRA 21pp gap 暴露手工特征覆盖不足
- 所有实验限于 0.6B-8B base model，instruct model 退化严重，实际适用性受限
- Cross-model F1=0.764 存在未控制的 model-switching confound

**Desk reject 风险**：
- 缺少 Responsible NLP Research Checklist（N1）
- 正文约超 0.3-0.4 页（N2）
- 以上两项必须在提交前修复

### 修改优先级

| 优先级 | 问题 | 类型 |
|--------|------|------|
| P0 (必须) | N1: 添加 Responsible NLP Checklist | 格式 |
| P0 (必须) | N2: 压缩正文至 ≤8 页 | 格式 |
| P1 (强烈建议) | W5: Abstract 扩充 + NLL 定义 | 写作 |
| P1 (强烈建议) | W1: 降低 cross-model F1 在叙事中的权重 | 实验 |
| P2 (如有时间) | W4: Method 加入 generator subset 对照表 | 写作 |
| P2 (如有时间) | N4: DDR vs 已有文献对比表 | 方法 |

---

## Detailed Comments

### Abstract
- 约 132 words，低于推荐范围（150-250）。缺少 "why important" 桥梁。NLL 未展开定义。最后一句 instruction tuning 限制诚实但可更简洁。

### Introduction
- 五段结构完整，逻辑推进合理（model collapse → distributional drift → depth classification）。
- Contribution 3（boundary conditions）表述技术密集，普通 reviewer 可能难以一次理解。
- 开头叙事 R1 认为足够具体，R2 认为偏抽象——Review Director 判断开头可接受。

### Related Work
- 四个子节结构清晰。与三篇并行工作的对比（§2.2 最后一段）是最关键的 positioning，三点区分论述到位但说服力不够强（见 N3）。
- §2.4 Data Quality and Provenance 与核心叙事连接较弱，可精简以节省页面（有助于解决 N2）。
- Ordinal classification 方法论应更早引入。

### Method
- 任务定义清晰，形式化恰当。Feature extraction motivation 交代充分。
- §3.3 "a priori" 选择的说法需谨慎——特征确实未在 test data 上调优，但先验理由不完全充分（为何不包含 perplexity、n-gram diversity 等）。
- Generator subset 不一致需在 §3.4 更清晰说明。

### Results
- §4.1 结果报告清晰，primary metric（binary F1）和 inflated metric（3-class F1）区分处理得当。
- §4.2 DDR 分析是核心贡献，分析深入但存在 over-quantification 风险——同时报告 ρ, d, KS, Glass's Δ, Cliff's δ, CV shift, TOST 等 7+ 种统计量。压缩此节有助于解决 N2。
- §4.3 Baseline 比较定位准确（contextualize rather than claim competitive advantage）。
- Cross-model F1=0.764 需要更审慎的解释或降级（W1）。

### Discussion
- Location/shape conjecture（§5 L5-7）有趣但过于 speculative，占用正文空间且自标 "informal conjecture"。
- Instruct tuning 分析（§5 L12-17）重要但缺 mechanistic 深度（RLHF vs SFT）。
- Downstream utility 讨论（§5 L20-21）过于简短。

### Limitations
- 极其全面，覆盖 base-model, scale, prompt-type, cross-domain, temperature, tokenizer, feature space, granularity。这是论文的显著优势。
- 缺少对 depth > 4 行为的讨论。

### Ethics
- 内容恰当，涵盖 privacy, dual use, licenses, compute budget, software versions。

### Format Compliance
- `\usepackage[review]{acl}` ✓
- `\author{Anonymous}` ✓
- `\linenumbers` ✓
- References 格式一致 ✓
- **缺少 Responsible NLP Research Checklist** ✗
- **页数超限 ~0.3-0.4 页** ✗
- Figure 字体可读 (≥7pt) ✓
- 附录 double-column ✓
- 无 em-dash AI 痕迹 ✓