---
round: 5
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-21T06:04:19.680633+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 10 (Fresh Review)

**论文**: Less Is More: Why Exception Events Outperform Complete Traces for Verdict Prediction
**Venue**: EMNLP 2026 via ARR (Long Paper)
**审稿人**: Reviewer 1 (方法严谨性 + 实验设计), Reviewer 2 (新颖性 + 完整性 + Related Work)
**审稿模式**: 重新审稿 (fresh)

---

## Summary

本文提出 VOTA（Verdict-Oriented Trace Abstraction），将完整执行 trace 压缩为 3 类事件（exception、assertion error、loop behavior），用于代码正确性二分类（verdict prediction）。在 4 个模型（1.5B–13B，3 个家族）上通过 LoRA SFT 实验发现：仅保留 exception 事件即可达到 ≥99.33% 准确率，而完整 trace 仅约 81.8%。文章进一步通过信息密度分解将 full_trace 的性能损失归因为 24% 梯度稀释 + 76% 信息过载。

---

## Strengths

**S1. 清晰的实验设计与系统性消融**
7 种 trace 表示 × 4 个模型的交叉实验矩阵设计系统，消融层次从粗（有/无 trace）到细（单事件类型），逻辑清晰。信息密度分解（gradient dilution vs. information overload）提供了 full_trace 失败的定量解释。

**S2. 强跨模型一致性**
exception_only 在 4 个模型（跨 3 个家族、1.5B–13B）上均 ≥99.33%，且 DebugBench 跨数据集验证达 100%，显示结果不依赖特定模型架构。

**S3. 实用价值明确**
exception_only 的 token 长度仅为 full_trace 的 ~1/50，直接降低推理成本。对工业界的 CI/CD 自动化判定场景有即时应用价值。

**S4. 充实的附录**
21 页完整论文包含详尽的 per-class metrics、训练动态、校准分析、error overlap、tokenizer 分析等，实验透明度高。

---

## Weaknesses

### Must-Fix（不修复则不可接收）

**W1. [CRITICAL] Related Work 全部为 placeholder 引用 — 桌面拒稿风险**
`related_work.tex` 中 17 处引用使用 `\cite{placeholder_*}` 键名，与 `references.bib` 中的实际条目不匹配，PDF 中渲染为 [?]。这不是格式问题——Related Work 整节在当前状态下**完全不可验证**，读者无法确认任何文献声明的真实性。ARR 审稿人几乎必然将此标记为桌面拒稿级缺陷。此外，.bib 中有 39 个孤立条目未被引用。
- **R1 评分**: Must-Fix | **R2 评分**: Must-Fix | **共识**: 一致同意，最高优先级

**W2. Exception-only 结果存在近似重言式（near-tautology）嫌疑**
exception_only 条件下，输入直接包含「是否发生异常」的信号，而 verdict 标签本身很大程度由异常决定。模型可能只需学习一条简单规则（有异常→fail，无异常→pass），而非真正理解代码执行语义。文章虽在 Discussion 中简短提及 regex baseline（96.78% vs SFT 99.83%），但未充分论证 SFT 超出 regex 的 3.05pp 增益是否具有统计显著性，也未分析 SFT 处理了哪些 regex 无法覆盖的 case。
- **R1 评分**: Must-Fix（需量化 SFT 超越 regex 的统计显著性）
- **R2 评分**: Must-Fix（核心贡献的可信度依赖此论证）
- **共识**: 一致同意需要加强论证。R1 进一步建议增加 McNemar 检验或 bootstrap CI。

**W3. 数据集范围极度有限**
仅覆盖 HumanEval (164) + MBPP (427) = 591 个问题，全部为 LLM 生成的 Python 短函数。DebugBench 跨数据集验证仍在同一生态（LLM 生成 Python）内。无任何证据表明结论可推广至：(a) 人类编写的代码，(b) 其他编程语言，(c) 更复杂的多文件项目。标题中 "Less Is More" 和 Abstract 中的通用性声明超出了实验支撑范围。
- **R1 评分**: Must-Fix | **R2 评分**: Must-Fix | **共识**: 一致同意，需在 Limitations 中显著加强声明或调整标题措辞

**W4. 部分实验条件为单 seed 结果**
DeepSeek-Coder VOTA 条件排除了 seed 42（因输出格式异常），Qwen-1.5B 的消融也为单 seed。单 seed 结果无法评估方差，降低了这些数据点的可信度。
- **R1 评分**: Must-Fix | **R2 评分**: Should-Fix | **共识**: R2 认为单 seed 在消融中可接受但需标注，R1 要求补充或明确声明

### Should-Fix（显著影响论文质量）

**W5. 信息密度分解方法论存疑**
24%/76% 的 gradient dilution vs. information overload 分解通过减法得出（full_trace loss − label_only loss = dilution，remaining = overload），但两个因素并非正交，可能存在交互效应。仅 Qwen-7B 3 seeds 的数据不足以支撑这一分解的普适性，其他模型未验证。
- **R1 评分**: Should-Fix | **R2 评分**: Should-Fix | **共识**: 一致同意需讨论非正交性限制

**W6. 训练动态分析缺乏定量指标**
Figure 3 的训练曲线分析主要为定性描述（"oscillates"、"stable convergence"），未提供量化收敛指标（如最终 N 步的方差、收敛速率）。
- **R1 评分**: Should-Fix | **R2 评分**: Should-Fix

**W7. 消融实验仅限 Qwen-7B 单模型**
Table 2 的 7 条件完整消融仅在 Qwen-7B 上进行。虽然 Table 1 验证了 exception_only 的跨模型一致性，但中间条件（ae_only、loop_only、VOTA_no_ae）的行为是否跨模型一致未知。
- **R1 评分**: Should-Fix | **R2 评分**: Should-Fix

**W8. Novelty 定位不够清晰**
VOTA 的核心 insight（异常事件最重要）直觉上并不令人惊讶。文章的 novelty 更多在于系统性验证而非方法创新，但叙事上偏向了方法贡献。
- **R2 评分**: Should-Fix | **R1 评分**: 部分同意（认为系统性验证本身有价值）

**W9. 格式标记消融 (nomarker) 不完整**
仅在 Qwen-7B exception_only 上测试了去除格式标记的影响，未覆盖其他条件和模型。
- **R1 评分**: Should-Fix | **R2 评分**: Should-Fix

---

## Reviewer 共识与分歧

### 共识点
1. Placeholder 引用是最紧急的修复项（桌面拒稿风险）
2. Near-tautology 论证需要量化加强
3. 数据集范围限制需要诚实声明
4. 信息密度分解的非正交性需要讨论
5. 论文实验工作量充实，附录详尽

### 分歧点
| 议题 | R1 立场 | R2 立场 | Director 裁定 |
|------|---------|---------|--------------|
| Near-tautology 严重程度 | 需要统计检验量化 SFT vs regex | 核心贡献可信度依赖此论证，但 regex baseline 已部分缓解 | 采纳 R1：需补充统计检验 |
| 单 seed 严重性 | Must-Fix（补充 seed 或显著声明） | Should-Fix（消融中可接受） | 采纳折中：至少显著标注，最好补充 |
| Novelty 评价 | 系统性验证有独立价值 | 方法创新有限，叙事应调整 | 记录分歧，不影响评分 |

---

## Questions to Authors

1. exception_only SFT (99.83%) vs regex baseline (96.78%) 的 3.05pp 差距是否统计显著？请提供 McNemar 检验或 bootstrap 95% CI。SFT 额外正确分类的样本有哪些共性？
2. 对于 exception_only 中 fail 样本无异常（或 pass 样本有异常但被 catch）的情况，SFT 模型的判断依据是什么？是否存在信息泄漏？
3. 信息密度分解中 gradient dilution 和 information overload 的交互效应如何？是否在其他模型上复现了 24%/76% 的比例？
4. 如何论证结论可推广至人类编写代码或其他编程语言？是否有初步实验或理论论证？
5. DeepSeek-Coder seed 42 VOTA 输出格式异常的具体表现是什么？排除该 seed 是否引入了选择偏差？

---

## Missing References

Related Work 节当前 17 处引用全部为 placeholder，无法评估引用完整性。修复后需重新审查以下方面：
- 是否覆盖了最新的 trace-based code understanding 工作（2025-2026）
- 是否引用了 verdict prediction / patch correctness 的完整谱系
- 是否遗漏了 information density / token efficiency 相关文献

---

## External Review

外部审稿未配置（`external_review.paperreview_ai.enabled: false`），本轮跳过。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（0 critical / 2 warnings / 9 info）

主要发现：
- ⚠️ **Pages 1–2 纯文本无任何展示元素**：Introduction 两页无图无表，建议将 Figure 1（当前在 page 4）前移以提升视觉节奏
- ⚠️ **Page 4 展示元素过密**：Figure 1 + Figure 2 + Table 2 三项堆叠，视觉密度过高
- ℹ️ Figure 2/3 轴标签约 6–7pt，接近可读性下限
- ℹ️ 其他页面布局基本合理，无严重排版问题

---

## Overall Assessment

| 审稿人 | 评分 | 对应级别 |
|--------|------|----------|
| Reviewer 1 | 3.0 | Findings |
| Reviewer 2 | 2.5 | Borderline Findings |
| **Director 综合** | **3.0** | **Findings** |

**评分理由**：

论文提出了一个清晰的研究问题（trace 的哪些成分对 verdict prediction 有用），实验设计系统，跨模型结果一致性强。这些优点足以支撑 Findings 级别的接收。

但以下问题阻止了更高评分：
1. **Placeholder 引用使 Related Work 完全失效**——这是提交前必须修复的硬性问题
2. **Near-tautology 风险未充分缓解**——exception_only 的核心贡献需要更强的统计论证来区分于简单规则匹配
3. **数据集范围与声明不匹配**——实验仅覆盖 LLM 生成的 Python 短函数，但标题和摘要暗示了更广泛的适用性
4. **部分结果缺乏统计可靠性**——单 seed 条件和未报告的显著性检验降低了定量声明的可信度

综合判断：当前版本适合 **Findings（3.0）**，修复 W1-W4 后有潜力提升至 Borderline Conference（3.5）。

---

## Detailed Comments

### 对作者的具体修改建议

**紧急（截止日期前必须完成）**：
1. 修复 `related_work.tex` 中所有 17 个 `placeholder_*` 引用，确保 .bib 键名与 \cite 命令一致
2. 清理 .bib 中 39 个孤立条目

**高优先级**：
3. 在 Discussion 中增加 SFT vs regex 的统计显著性检验（McNemar test 或 paired bootstrap），并分析 SFT 额外正确分类的样本特征
4. 在 Limitations 中明确声明数据集限制：仅 LLM 生成 Python、短函数、单文件；跨语言/人类代码推广性未验证
5. 标注所有单 seed 结果，或补充额外 seed

**中优先级**：
6. 讨论信息密度分解的非正交性限制
7. 为 Figure 3 训练动态增加定量收敛指标
8. 考虑调整标题或摘要措辞以匹配实际实验范围
9. 调整 Figure 1 位置（移入 Introduction）以改善视觉节奏