---
round: 9
overall_score: 3.0 (Findings)
timestamp: 2026-05-17T14:16:27.544066+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 10 审稿报告 — Depth Fingerprinting

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**目标 Venue**: EMNLP 2026 (ACL Rolling Review)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）
**轮次**: 1 轮（Step 2 交叉分享后达成共识，无需 Round 2）

---

## Summary

本文提出 ordinal generation depth estimation 任务，将 LLM 文本检测从二分类扩展为三类序数分类（gen-0/gen-1/gen-2+）。基于 8 个 base model（5 个家族，0.6B–8B）构建的非改写续写链（~37K 文本），作者发现 differential depth response (DDR)：中心趋势特征随深度单调漂移，形状特征保持近平稳。7 个手工特征 + XGBoost 在 LOGO 下达到 3-class macro F1=0.762（binary F1=0.694 leak-free）。下游实验通过 TOST 检验论证 depth-stratified selection 等价于 random subsampling。

---

## Strengths

1. **任务定义有价值**: Ordinal depth estimation 是未被前人探索的自然研究方向，将 binary detection 推进为 fine-grained provenance characterization
2. **实验设计严谨**: LOGO/LOFO 交叉验证、Bootstrap CI、McNemar test、Bonferroni 校正、类平衡子采样等方法论素养突出
3. **分析深度极佳**: 17 页含 11 个附录，覆盖长度控制、prompt 类型、文本扰动、跨域、采样参数、QLoRA、下游效用等多维度消融
4. **DDR 框架有启发性**: location shift + shape preservation 的二分法提供了理解递归生成的新视角
5. **可复现性好**: 特征定义完整、超参明确、软件版本记录、承诺开源
6. **Limitations 讨论诚实**: 直面 instruction tuning 限制、base-model 约束、temperature 依赖

---

## Weaknesses

### Must-Fix（5 项，Reviewer 共识）

**[M1] gen-0 seed 共享导致 LOGO 3-class 结果膨胀** (R1-N1, R2 AGREE)
- LOGO 中 test generator 的 gen-0 与 train generator 的 gen-0 是完全相同的 Wikipedia 文本。gen-0 准确率 99.1% vs gen-1 56.9%/gen-2+ 74.0%（Table 10）。3-class F1 被 gen-0 的近完美识别人为拉高。
- 论文虽报告 leak-free binary F1=0.694，但 headline 仍突出 3-class metrics。
- R2 修正：Abstract 的 0.809 来自 cross-model 5-fold CV（非 LOGO），可能不受此问题影响，但论文术语混淆了两个评估设置。
- **要求**: 以 leak-free metric 为 headline，或用 generator-disjoint seeds 重跑并量化 inflation 程度。

**[M2] Instruction tuning 完全破坏 signal，但 framing 未限定 scope** (R1-N2, R2 AGREE)
- OLMo-Instruct LOGO F1=0.338（≈三分类随机）vs base 0.763。
- Abstract/Introduction 使用 "provenance tracking"、"quality-aware data curation" 等暗示通用性的表述，未在开头限定为 base models only。
- 2026 年绝大多数部署 LLM 均为 instruction-tuned，一个仅对 base model 有效的方法其 practical motivation 需要重新论证。
- **要求**: Abstract/Intro 开头明确限定 scope；将 instruct 负面结果从 Limitations 提升到 Discussion 作为重要发现；论证 base model 场景的实际相关性。

**[M3] DDR 相对 model collapse 文献新颖性论证不足** (R2-N1, R1 AGREE)
- DDR 的核心现象（递归生成→词汇多样性下降→分布收窄）在 Shumailov et al. (2024), Guo et al. (2024) 中已有记录。
- §5 "Relation to model collapse" 仅两句带过，未系统论证 inference-side DDR 与 training-side collapse 的实质差异。
- R1 补充：DDR 的 "location shift + shape preservation" 分解是增量贡献，非质变。
- **要求**: 扩展 §5 为完整对比段落；提供实验证据（如 shape stationarity 在 model collapse 设置中是否也成立？）

**[M4] "Ordinal depth estimation" framing 与三分类实际能力不匹配** (R2-N2, R1 AGREE)
- 5-class F1≤0.50，depth 2–4 mutually indistinguishable。gen-1/gen-2+ 边界 error rate 48.42%（接近随机）。
- "Ordinal" 在统计文献中暗示 fine-grained ordered estimation，但实际只能区分三类，且最关键边界很弱。
- 结合 M1，实际有效区分力可能仅在 gen-0 vs non-gen-0 这条线上。
- **要求**: 标题/Abstract 精确描述为 "coarse ordinal" 或 "3-class depth classification"；在正文（非仅附录）讨论三类上限原因和 gen-1/gen-2+ 边界困难。

**[M5] 下游 curation 实验削弱核心动机** (R2-N3, R1 AGREE)
- Table 18: depth-stratified (ppl=2.387) = random subsampling (ppl=2.367)；full dataset (ppl=2.335) 最优。直接反驳 "quality-aware data curation" 动机。
- 仅 3 seeds，统计功效严重不足（min achievable p=0.125 对部分比较）。
- R1 补充：如果 depth 对下游无影响，depth detection 的实用动机被瓦解——检测了一个不 matter 的属性。
- **要求**: 增加 seeds 至 10+ 以获得充分统计功效；或将 curation 从核心动机降级为 "potential application"；调整 Introduction framing。

### Should-Fix（6 项）

**[S1] Temperature 敏感性需正文讨论** (R1-N3, R2 partial REBUT)
- t=1.0 下 F1 降约 8pp（0.762→~0.68），非 "近随机" 但退化显著。所有主实验仅 t=0.7。
- R2 修正 R1 的过强表述，但两者同意：需明确工作范围 [0.5, 0.9]，并在正文讨论。
- **要求**: 将 Appendix H 核心结论移入 §4 或 §5；增加 t=1.0 下 surface vs reference 特征分解分析。

**[S2] "Location shift" claim 缺正式检验** (R1-W1, R2 AGREE)
- 仅有 Spearman ρ 和 Figure 1 视觉证据，无 KS/AD test、Levene's test、Q-Q plot。
- **要求**: 补充分布检验或降低 claim 强度（"consistent with"→"suggestive of"）。

**[S3] TOST ±2% margin 无理论依据** (R1-W2, R2 AGREE)
- 未解释为何 2% perplexity 差异是 "practically negligible"。
- **要求**: 报告多 margin (1%/3%/5%) 结果 + Cohen's d。

**[S4] Cross-model F1=0.809 缺正式表格** (R2-W3, R1 AGREE)
- Abstract headline 数字仅在文字/脚注中出现，无 per-class metrics 和 CI 表格。
- **要求**: 为 cross-model chain evaluation 添加正式表格。

**[S5] 数据多样性不足** (R1-W5, R2 AGREE)
- Wikipedia-only seeds。跨域仅 3 generators × 200 seeds，Academic F1=0.628 显示显著退化。
- **要求**: 扩大跨域评估或在正文突出讨论 selection bias。

**[S6] Geng et al. (2026) 差异化不够清晰** (R2-W2, R1 AGREE)
- 两篇独立发现相似的三类边界，但 §2.2 仅两句区分。
- **要求**: 增加专门对比段落，从机制层面解释差异。

### Nice-to-Fix（5 项）

- [P1] "entropy" 术语与信息论冲突，建议统一为 "reference-model surprisal" 或明确定义
- [P2] Appendix E QLoRA F1=0.905 对主方法选择的 implication 未在正文讨论
- [P3] Baseline repurposing 应独立调参（至少 grid search），或论证统一超参的合理性
- [P4] Discussion §5 前三段复述 Results，应压缩并增加解释性内容
- [P5] 参考模型依赖（推理开销、非英语适用性）应在 Limitations 增加讨论

---

## Reviewer Consensus

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| gen-0 泄漏 inflate | Critical (N1) | AGREE | ✓ |
| Instruction tuning + framing | Critical (N2) | AGREE | ✓ |
| DDR novelty vs model collapse | AGREE | Critical (N1) | ✓ |
| Ordinal framing overpromise | AGREE | Critical (N2) | ✓ |
| Downstream contradicts motivation | AGREE | Critical (N3) | ✓ |
| Temperature sensitivity | Critical (N3) | Partial REBUT | 部分共识 |
| Location shift claim | Should-Fix (W1) | AGREE | ✓ |
| TOST margin | Should-Fix (W2) | AGREE | ✓ |
| Baseline fairness | Should-Fix (W3) | AGREE (nuance) | ✓ |
| gen-1/gen-2 boundary | Should-Fix (W4) | AGREE | ✓ |
| Data diversity | Should-Fix (W5) | AGREE | ✓ |

---

## Reviewer Divergence

**唯一分歧: R1-N3 温度敏感性的严重程度**
- R1 表述: "t=1.0 时退化为近随机水平"（升级为 critical）
- R2 修正: "t=1.0 下 F1≈0.68，远高于随机 0.33；退化 significant 但非 catastrophic"（降为 should-fix）
- **Director 判断**: R2 的修正有数据支撑（Appendix H Table 12），R1 "近随机" 的措辞不准确。但敏感性本身是真实问题，归入 Should-Fix [S1]。

---

## Questions to Authors

1. 如果在 LOGO 中使用 generator-disjoint gen-0 seeds，3-class F1 下降多少？
2. DDR 的 shape stationarity 在 model collapse 设置（retrain on own output）中是否也成立？
3. t=0.8/0.9 中间温度下，surface features (TTR, hapax) 是否比 reference features 更 robust？
4. Downstream utility：是否尝试过更精细的 depth-aware 策略（如按深度加权而非简单过滤）？
5. QLoRA F1=0.905 vs 手工特征 0.809——为何不以 QLoRA 为主方法？"Interpretability" 是否足以作为理由？

---

## Missing References

- Madaan et al. (2023, Self-Refine): 迭代 LLM 输出优化，涉及多步生成
- Hammoudeh & Lowd (2024): 训练数据溯源，与 provenance 动机相关
- Kumarage et al. (2023): Stylometric features 做 AI 检测，与 surface features 直接相关

---

## External Review (Stanford Agentic Reviewer)

项目未配置外部审稿，本轮无外部审稿结果。

---

## Overall Assessment

**评分: 3.0 / 5 (Findings)**

**置信度: 4 / 5** (两位 Reviewer 均熟悉相关文献，对论文进行了完整深入阅读)

**核心判断**: 论文的任务定义新颖、实验设计严谨、分析覆盖全面，是一篇执行良好的实证研究。但五个 Must-Fix 问题共同指向一个核心结论：**论文的实际区分力（leak-free binary F1=0.694）和适用范围（base model + t≤0.9 + continuation chains）被当前 framing 显著夸大**。DDR 相对 model collapse 文献的增量有限，下游实验为负面结果，"ordinal" framing 与三分类实际能力不匹配。

如果作者能 (1) 用 leak-free metrics 重构 headline，(2) 限定 scope 并调整 framing，(3) 正面论证 DDR vs model collapse 的差异，(4) 诚实面对 downstream negative result 的含义，本文可以成为一篇坚实的 **Findings** 论文。当前状态不足以支撑主会议录用。

---

## Detailed Comments (按章节)

### Abstract
- 0.809 (cross-model) 作为 headline 数字可能不受 gen-0 泄漏影响，但与 LOGO 0.762 的关系需澄清
- "complicating provenance tracking and quality-aware data curation" 的 motivation claim 被 §4.4 实验反驳
- 建议在 Abstract 中明确 "base pretrained models" scope

### Introduction
- §1 para 1 的 motivation（recursive contamination → quality degradation）被 downstream 实验否定
- Contribution 3 ("Detectable ≠ harmful") 试图把负结果变成正面贡献，但逻辑上瓦解了 detection 的实用动机
- 建议重新定位动机为 "characterization/scientific understanding" 而非 "practical curation"

### Method
- §3.2 gen-0 seed sharing 的 rationale 清晰，但对 leakage 后果的处理不够
- §3.3 "entropy" shorthand 与信息论冲突，建议用 "NLL" 或 "reference surprisal"
- §3.4 XGBoost 统一超参的合理性论证不充分

### Results
- Table 1 呈现清晰，但 gen-0 inflation 问题需要 footnote 或 caveat
- §4.2 DDR claim 需要 formal distributional tests 支撑
- §4.3 "competitive at lower cost" claim 对 4-det ensemble 的表述需要更精确（3-class 0.774 vs 0.795 = 2.1pp 差距）

### Discussion
- "Relation to model collapse" 段需大幅扩展
- "Practical applicability" 段的 corpus-level flagging 论述有价值，建议突出
- gen-1/gen-2+ boundary 分析应从 Appendix 移入正文

### Limitations
- 已相当全面和诚实
- 建议增加：参考模型依赖、非英语泛化、computation overhead 量化