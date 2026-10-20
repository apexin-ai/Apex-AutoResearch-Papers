---
round: 3
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-19T05:03:08.722735+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告：Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh（初审）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析；R2: 新颖性+完整性+写作质量+格式合规）
**交叉回应**: 完成（R1→R2, R2→R1），1 轮即收敛

---

## Summary

本文对 trace-based verdict prediction（pass/fail 二分类）进行了系统性的 component ablation 研究，在 4 个模型（Qwen-7B/1.5B, CodeLlama-13B, DeepSeek-6.7B）、3 个架构家族、1.5B-13B 参数范围内，比较了 7 种 trace representation 条件。核心发现：exception events 单独即可达到 ≥99.33% accuracy（3/4 模型 ≥99.83%），而 code-only baseline 仅 67-77%；添加更多 trace 信息反而降低性能。论文还提出了 information density decomposition（gradient dilution ~26% vs information overload ~74%）和 tail-truncation phase transition（384→512 tokens）两个分析性发现。

---

## Strengths

1. **实验设计系统性强**: 7 trace conditions × 4 models × 3 architecture families 的消融矩阵设计清晰，消融逻辑层次分明。[R1, R2 共识]

2. **统计报告规范**: Wilson CI、paired bootstrap resampling (B=10,000)、McNemar test 使用恰当，p-value 和 CI 报告完整，优于同类工作。[R1, R2 共识]

3. **Phase transition 发现有价值**: tail-truncation 在 384→512 tokens 处的 phase transition 跨 4 模型 3 架构一致出现，定位了 exception traceback 的 token 长度阈值，是 clean 且有信息量的 empirical finding。[R1, R2 共识]

4. **Format marker ablation 设计巧妙**: nomarker 条件有效将 format shortcut (~9%) 和 semantic understanding (~91%) 解耦，是 well-designed control experiment。[R2 提出, R1 AGREE]

5. **Limitations 诚实详尽**: 7 条 limitations 涵盖 dataset scope、model scope、seed variance、self-familiarity bias、error distribution bias 等关键问题，比多数提交更为 thorough。[R1, R2 共识]

6. **Regex baseline 设置充分**: 提供 6 个 rule-based baseline（含 format marker exploitation），使 SFT added value 可量化，在同类工作中较少见。[R1 提出, R2 AGREE]

7. **Cross-model scale invariance**: exception_only 在 1.5B-13B 保持 ≥99.33% 而 no_trace 呈单调 scale dependence (9.16pp range)，对比有说服力。[R1 提出]

8. **可复现性好**: 完整超参数报告、训练时间、硬件信息、承诺开源。[R1, R2 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[N1] DeepSeek seed 123 排除构成选择性报告** [R1 提出, R2 AGREE]
- Abstract 声称 "≥99.33% accuracy on all four models"，但 DeepSeek 3-seed mean = 96.58% ± 4.76（seed 123 = 91.09%，fail recall = 70.5%）
- 1/3 seeds 的 failure rate 不能简单归因为 "LoRA initialization failure"（论文自身承认 "direct evidence is lacking"）
- R2 补充：seed 123 的 format collapse 同时暴露了方法在长输入上的脆弱性，是 robustness concern 而非可排除的 outlier
- **建议**: 报告 3-seed mean 或将 claim 修改为 "≥99.33% on 3/4 models (DeepSeek shows seed-dependent variance, 3-seed mean 96.58%)"

**[N2] 核心发现的 novelty 不足** [R2 提出, R1 AGREE]
- Exception 是 Python runtime 的 primary fault indicator，"exception events 是最强信号" 在 SE 直觉上可预期
- Regex B5 仅通过 format marker 达 99.33%；最强 semantic regex (B4) 达 93.61%
- SFT 相对 B4 的优势仅体现在 8 个 caught-exception 边界样本（来自 2 个 distinct problems）
- nomarker ablation 证明 ~91% 语义信号（已是改进），但核心 novelty 仍更像是对已有直觉的量化确认
- **建议**: 将 framing 从 "exception 是最强信号" 转向 "why richer traces hurt" 和 information density decomposition

**[N3] 单一数据集 + DebugBench ceiling effect 不支撑 universal claims** [R1 提出, R2 AGREE]
- 主实验仅 591 problems (HumanEval + MBPP)
- DebugBench no_trace = 96.71%，headroom 仅 3.29pp，不构成独立验证
- Limitations 承认 "production code may exhibit silent logic errors where no exception is raised"，直接动摇标题级 claim
- Exception dominance 可能仅是 LLM-generated code 的 error distribution 特征（exception-dominated failures）
- **建议**: 降低 claim 强度，限定为 "on LLM-generated code with exception-dominated error distributions"；报告 fail-but-no-exception 样本比例

**[N4] "Richer traces actively hurt" 被 tokenizer 截断混淆** [R2 提出, R1 AGREE]
- DeepSeek VOTA 14.96pp deficit 主因是 91.7% 训练样本被截断（论文自身承认 "primarily a truncation artifact"）
- 排除 DeepSeek 后，VOTA cross-model range 仅 1.01pp (98.57-99.58%)
- Qwen-7B VOTA vs exception_only 差距仅 0.42pp（单 seed，p=0.01 不反映 seed-to-seed variability）
- Loss decomposition 基于单 intermediate condition 做两因素分解是 under-determined
- **建议**: 区分 truncation artifact 和 inherent property；修改 Abstract 中 "actively hurts" 表述

**[N5] 多数实验条件仅单 seed，在已知 8.24pp seed variance 下不可靠** [R1-N3, R2-N4 共识]
- VOTA、full_trace、no_trace、label_only 全部 seed=42 单次结果
- Loss decomposition (26%/74%) 基于单 seed 单模型无 CI
- VOTA (99.41%) vs exception_only (99.83%) 的 0.42pp 差异在已知 ae_only std=0.49pp 的前提下不可靠
- **建议**: 至少对 VOTA 和 full_trace 补充 3-seed 实验

**[N6] Component ablation (ae_only/loop_only) 仅在 Qwen-7B 验证** [R2-N3, R1 AGREE]
- §3.2 明确说明 "We restrict ae_only and loop_only ablations to Qwen-7B"
- Contribution 3 ("two-tier diagnostic hierarchy") 是 general claim，需 cross-model 验证
- VOTA 在不同模型差异达 14.96pp，loop_only 可能也有显著波动
- **建议**: 至少在一个非 Qwen 模型上验证，或将 claim 限定为 "on Qwen-7B"

### Should-Fix（影响评分但不一票否决）

**[W1] 48.99% test set duplicates 违反 CI 独立性假设** [R1 提出, R2 AGREE with nuance]
- Effective N=607 而非 1190，CI 宽度增加 √(1190/607) ≈ 1.4 倍
- Point estimate 不受影响（dedup sensitivity = 0.00pp delta），但所有 CI 系统性偏窄
- 仅在 Appendix 提及一次 deduplicated CI
- **建议**: 主文报告双 CI 或注明 effective N

**[W2] Loss decomposition 因果解释过强** [R1-W2, R2 AGREE]
- Abstract "the gap decomposes into..." 呈现的确定性超出 evidence
- full_trace_label_only 同时改变有效梯度 norm、隐式正则化等
- 单 seed 单模型无 error bars
- 方向性 insight 有价值但不应以精确数字作为独立 contribution
- **建议**: Abstract 加 "approximately" 限定；补充 multi-seed 或明确 caveat

**[W3] Verdict prediction 实际应用场景不清** [R1-W3, R2-W3 共识]
- CI/CD 中 test 框架直接报告 pass/fail，不需要 ML 预测
- 论文未解释在什么场景下有 trace 但不知道 verdict
- Discussion "practical implications" 未回答根本动机问题
- **建议**: 明确论述使用场景（patch correctness prediction? trace replay?）

**[W4] VOTA 组件提取规则未定义** [R1-W5, R2 AGREE]
- Method §2.3 定义了 what 但未定义 how
- Appendix 仅有极简示例，不足以复现
- **建议**: 补充算法伪代码或详细提取规则

**[W5] CodeLlama tail-2048 实验条件不匹配** [R1-W6, R2 AGREE]
- CodeLlama tail-1024/2048 使用 label-only loss，其他模型使用 standard loss
- 41.8% collapse 可能是 label-only loss artifact
- **建议**: 补充 standard loss 实验或更明确标注差异

**[W6] Related Work 遗漏多个方向，引用 31 篇偏少** [R1 missing refs, R2-W4 共识]
- 缺失：test oracle generation (TOGA)、static analysis (DeepDFA)、code agents (SWE-bench)、LLM calibration (Kadavath 2022)、defect prediction (Kamei 2013)
- 同类 EMNLP 论文通常 40-60 篇引用
- **建议**: 补充至 40+ 篇

**[W7] ARR Checklist 与论文不一致** [R2-W5, R1 AGREE]
- arr_checklist.tex 写 "single model scale (7B)" 但实际 4 模型
- 反映提交准备粗心

**[W8] 页数可能超限** [R2-W1, R1 REBUT]
- Conclusion 可能延伸至第 9 页（需编译确认）
- ACL Long Paper 限 8 页正文

---

## Reviewer Consensus

以下问题双方达成 [AGREE] 共识：

| 问题 | R1 | R2 | 交叉结果 |
|------|----|----|----------|
| DeepSeek seed 选择性报告 | Must-Fix (N1) | AGREE | **共识** |
| Novelty 不足 | Excitement 2.5 | Must-Fix (N1) | **共识** |
| 单数据集 + universal claim | Must-Fix (N2) | AGREE | **共识** |
| "Richer traces hurt" 混淆 | — | Must-Fix (N2) | R1 AGREE |
| Multi-seed 不均 | Must-Fix (N3) | Must-Fix (N4) | **共识** |
| Component ablation 单模型 | — | Must-Fix (N3) | R1 AGREE |
| Loss decomposition 过强 | Should-Fix (W2) | — | R2 AGREE |
| 任务动机不清 | Should-Fix (W3) | Should-Fix (W3) | **共识** |
| VOTA 提取算法缺失 | Should-Fix (W5) | — | R2 AGREE |
| Related Work 遗漏 | Missing Refs | Should-Fix (W4) | **共识** |

---

## Reviewer Divergence

仅 1 处 minor 分歧：

**Generator-evaluator overlap (R1-W4)**: R1 认为 Qwen-7B 生成数据并评估存在 self-familiarity bias。R2 REBUT：cross-model design（3 个非 Qwen 模型达到同等 exception_only 性能）、DebugBench (non-Qwen-generated code) 评估、Limitations 已充分讨论，部分 mitigate。此分歧不影响整体判断。

---

## Questions

1. 在没有 exception 的 fail cases（silent logic errors）中，exception_only 的 accuracy 是多少？当前数据集中此类样本占比如何？
2. VOTA 在 context window 足够长（如 4096 tokens）的条件下重训，是否仍低于 exception_only？
3. Component ablation (ae_only, loop_only) 在非 Qwen 模型上是否有初步结果？
4. CodeLlama tail-2048 在 standard loss 下是否完成实验？

---

## Missing References

1. **Test oracle generation**: TOGA (Dinella et al., ICSE 2022)
2. **Static analysis + DL**: DeepDFA (Steenhoek et al., ICSE 2024)
3. **Code agents**: SWE-bench (Jimenez et al., ICLR 2024)
4. **LLM calibration**: Kadavath et al. 2022 ("Language Models (Mostly) Know What They Know")
5. **Defect prediction**: Kamei et al. 2013 ("A Large-Scale Empirical Study of Just-in-Time Quality Assurance")
6. **Program repair with execution feedback**: RepairAgent (Bouzenia et al., 2024)

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目未配置 `external_review.paperreview_ai.enabled`）

---

## Overall Assessment

**评分: 3.0 — Findings（可被 Findings 接收）**
**置信度: 4/5**

**两位 Reviewer 独立评分均为 3.0 (Findings)，交叉回应后维持不变。**

**评分理由**:

- **Soundness (3.5/5)**: 实验设计系统性强，统计方法规范。但 DeepSeek seed 选择性报告、multi-seed 覆盖不均、truncation confound 未解耦、loss decomposition 单 seed 单模型等问题影响证据可靠性。
- **Excitement (2.5/5)**: 核心发现（exception 主导 verdict prediction）在 SE 直觉上可预期。Regex B4 达 93.61%、B5 达 99.33% 说明大部分信号可通过 trivial pattern matching 获取。信息密度分解和 phase transition 是更有趣的子发现，但整体 novelty 有限。任务范围窄（verdict prediction = pass/fail 二分类），与 NLP 社区 relevance 有限。
- **Reproducibility (4/5)**: 超参数完整，承诺代码/数据/模型开源。

**总结**: 这是一篇执行质量较高的实证消融研究，在论文的实验范围内，核心发现得到了系统性验证。Phase transition、information density decomposition、format-semantic 解耦是有价值的分析贡献。但核心发现的 novelty 有限（量化确认已有直觉），claims 超出 evidence 支撑范围（universal/architecture-independent 声明 vs. 单一数据集 + exception-dominated error distribution），实验严谨性有缺口（seed 覆盖、truncation confound）。推荐 Findings 接收，前提是解决 N1（seed 报告）、N2（framing/novelty）、N3（claim 强度）。

---

## Detailed Comments

### Abstract
- "≥99.33% accuracy on all four models" 需修改（DeepSeek 3-seed mean 96.58%）
- "adding richer trace information actively hurts" 需加截断 caveat
- "~74% information overload / ~26% gradient dilution" 需加 "approximately" 和单模型 caveat
- 整体信息密度合理（已从先前 14 个数字精简至 6 个）

### Introduction
- Contribution 1 信息密度过高（一个 bullet 含 4 个独立 claim），建议拆分
- "fault detection, not generation" 的 reframing 是好的叙事策略
- 缺少对 verdict prediction 实际使用场景的清晰论述

### Method
- VOTA 三个组件的提取规则需补充（算法伪代码或详细描述）
- 训练集生成方式（Qwen-7B 生成）的 overlap bias 已在 Limitations 讨论

### Experiments
- Table 1 DeepSeek exception_only 应报告 3-seed mean（含 seed 123）
- Table 2 component ablation 仅 Qwen-7B，应补充至少一个其他模型或限定 claim
- Table 3 loss decomposition 需标注单 seed 单模型 caveat
- Cross-model VOTA comparison 需区分截断引起的退化和信息本身的影响

### Discussion
- 内容充实（8 段实质内容）
- "Why exception_only outperforms ae_only" 段落清晰
- "Tier hierarchy: practical implications" 需先回答 "为什么需要 ML 预测 verdict"

### Related Work
- FL 段落已补充（Ochiai/Tarantula/DStar/AutoFL/AgentFL/LLM4FL）
- 仍缺 test oracle、static analysis、code agents、LLM calibration、defect prediction 方向
- 31 篇引用偏少

### Appendix
- 第 231/549 行存在 em-dash (---) AI 写作痕迹
- Appendix 整体详尽，负面结果报告诚实

### 格式
- ARR Checklist 内容需与论文同步更新
- 页数需编译确认（可能超 8 页限制）
- 标题 "X Is All You Need" 模式审稿人可能审美疲劳
