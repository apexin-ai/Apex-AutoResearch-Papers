---
round: 1
overall_score: weak reject
timestamp: 2026-05-15T10:10:40.958625+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Generational Depth Estimation of Recursive Synthetic Text

**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 相关工作）
**轮次**: Round 1（1 轮收敛，无需 Round 2）

---

## Summary

本文首次系统研究递归合成文本的 generational depth estimation 问题。定义经验判别边界 K*_empirical，使用 15 维统计特征 + OBD-LightGBM 分类器，在 4 个 model-mode 配置和 4 种 decoding 策略上一致得到 K*=2（≤1.5B 参数规模）。跨模型迁移保留 80-92% 精度，neural probe 在 Qwen 上达到 K*_neural=3 但 Pythia/OLMo 仍为 2。下游 filtering 实验表明 binary filtering 优于 graduated 策略。

---

## Strengths

**S1. 问题定义新颖且重要。** 将 synthetic text detection 从 binary 扩展到 ordinal depth estimation 是 well-motivated 的研究方向。DPI 保证 K*_theory 有限的理论论证简洁优雅。[R1, R2 一致]

**S2. 实验覆盖系统。** 跨 3 个模型族、2 种生成模式、4 种 decoding 策略的网格设计覆盖关键变量。GroupKFold 按 seed document 分组是正确的防泄漏设计。[R1]

**S3. 多角度交叉验证。** 从 statistical features → cross-model transfer → neural probing → downstream filtering 四层面验证 K*=2，提供互相支撑的证据链。Neural probe 的 self-familiarity 解释合理且诚实。[R1]

**S4. Limitations 诚实全面。** 明确列出 8 条限制（scale、threshold sensitivity、boundary marginality 等），在投稿论文中不常见。[R1, R2 一致]

**S5. 统计方法论规范。** Bootstrap CI、permutation test、GroupKFold 的使用得当。Reproducibility 信息充足（超参、数据统计、feature 定义均有详细附录）。[R2]

**S6. Frontier LLM baseline 有说服力。** GPT-5.5 和 Claude Opus 4.6 的 zero-shot 对比有效论证了 depth estimation 不是 trivial task。[R1]

---

## Weaknesses

### Critical（影响接收决定）

**C1. θ=0.60 阈值选择缺乏理论依据，K*=2 极度脆弱** [R1-W1 + R2-N1, 两人独立发现并一致评 Critical]
- θ=0.60 的唯一论证是 "permutation null 95th percentile < 0.55"，仅说明 AUC > 0.55 统计显著，不能 justify 0.60
- Sensitivity analysis 显示 θ ±0.05 导致 K* 从 1 到 3 剧变
- 边界极度 marginal：Qwen-cont 1v2 CI lower bound = 0.602（超 θ 约 0.2pp）；Qwen-rw 2v3 CI upper bound = 0.599（低于 θ 约 0.1pp）
- Abstract/Conclusion 以 "K*=2 is consistent" 的确定性表述呈现，构成 overclaiming
- **必须修复**：(1) 提供 θ 的 principled justification（effect size-based 或 information-theoretic）；(2) 报告 K*(θ) 完整曲线作为主要结果而非单点值；(3) 将 sensitivity analysis 从 Appendix 提至主文；(4) Abstract/Conclusion 改为 threshold-conditioned 表述

**C2. Surprisal 特征的 scorer-generator 混淆未控制** [R1-W2, R2 交叉同意 with nuance]
- 9/15 特征（60%）由 Qwen2.5-1.5B 计算 surprisal，而 Qwen 同时是两个配置的生成器
- Qwen 配置：scorer = generator（self-scoring bias）；Pythia/OLMo：scorer ≠ generator
- 论文在 neural probe 部分识别了 self-familiarity 但未将同一逻辑应用到 15D 特征
- 缓解因素：Pythia/OLMo（scorer≠generator）仍得 K*=2，部分缓解对 K* 结论本身的担忧
- **必须修复**：至少用替代 scorer 验证 feature ranking 稳定性；或弱化 "text-intrinsic" claim

**C3. self_BLEU 特征存在训练/部署不一致和潜在 label leakage** [R1-W7 + R2-N3, 两人独立发现]
- self_BLEU 定义为 "Mean 4-gram BLEU against 100 random same-depth samples"——需要 depth label
- 部署时 depth 未知，无法按 depth 分层采样参考集
- Test fold 的 self_bleu 在知道 depth label 条件下预计算，技术上构成间接 label leakage
- **必须修复**：(1) 说明部署时计算方式；(2) 报告去除 self_BLEU 后 14D 模型 K* 是否仍为 2

### Warning（影响评分但不一票否决）

**W1. ≤1.5B 规模限制使实际价值存疑** [R2-N2 Critical, R1 降级为 Should-Fix, 存在分歧]
- 所有实验仅在 ≤1.5B 模型上进行，而实际 web 合成文本多来自 7B-70B+
- R2 认为应至少补一个 7B 验证或在 title 加 scale qualifier
- R1 反驳：Abstract 已标注 scale；方法论贡献 scale-independent；要求 7B 属 scope expansion
- **建议**：在 title 更显著标注 scale 限制；如有余力补 7B 验证会显著增强论文

**W2. C3 filtering 效果量极小，缺多重比较校正** [R1-W6 + R2-W2, 一致]
- binary-ours vs no-filter: MMLU +0.76pp，vs surprisal: +0.47pp
- 100% 合成设定极端，"50% degradation reduction" 在现实场景会缩水
- 6 策略两两比较无 Bonferroni/Holm 校正
- **建议**：补 paired test + 多重校正 + Cohen's d；考虑 mixed-ratio 实验

**W3. "8 conditions" 表述模糊** [R1-W3, R2 同意]
- 暗示 4+4=8，实为 4 model-mode + 单模型 decoding 消融
- Decoding 消融未标注使用哪个模型

**W4. "Text-intrinsic" claim 被固定 scorer 削弱** [R1-W4, R2 同意]
- Transfer 实验测试的是 "固定 scorer 下跨生成器迁移"，非 "信号内禀于文本"
- 建议弱化措辞

**W5. Prompt-chain ≠ retrain-chain 在 Introduction 区分不够** [R2-W1, R1 同意]
- Introduction 给人直接测量 model collapse 的印象
- 关键区分应从 Appendix 前置至 Introduction

**W6. Neural probe "confirming K*=2 as representation-independent lower bound" 措辞误导** [R2-W5, R1 同意]
- Qwen K*_neural=3 恰恰证明 K*=2 是 feature-set-dependent
- 建议改为 "feature-set-specific lower bound, with K*_neural ≥ 2 across all models"

**W7. Related Work 遗漏 + orphan bib entries** [R2-W4, R1 同意]
- 缺失：Krishna et al. (NeurIPS 2023) paraphrasing evasion、Sadasivan et al. (2023) AI text detection limits、Wei Hao et al. (ACL 2025)
- 12 条 orphan bib entries 未在正文引用

**W8. Permutation test p-value floor** [R1-W5, R2 同意]
- 500 resamples → min p=0.002，所有 1v2 恰好报 p=0.002
- 建议增至 10,000 或报告为 "p < 0.002"

**W9. LLM baseline 测试集规模不一致** [R1-W8, R2 同意]
- LLM 在 N=500 上评估，OBD 38.6% 来自 N=5,000
- 应补充 OBD 在同一 N=500 上的 accuracy ± CI

**W10. LLM zero-shot vs 有监督比较不公平** [R2-W3, R1 部分反驳]
- R1 认为 zero-shot 是 LLM 最自然部署方式，claim 是 "non-trivial" 而非 "OBD > LLM"
- 两人同意 "requires specialized features" 措辞过强，改为 "not solved in zero-shot setting"

**W11. 格式问题** [R1 + R2 一致]
- Limitations 在 Discussion 内而非独立 section（ACL 2023+ 要求独立）
- 缺 Ethics Statement
- Abstract 过长（~250 vs 建议 150-200 words）

### Info（不影响接收）

**I1. 多处数值精度不一致**：CI 0.6015 vs 0.602、transfer retention 83% 无法复现（应为 85%）、跨模型 0v1 AUC > 0.96 无具体值、token counts whitespace vs subword 不一致、"~88%" 应标注具体模型名

**I2. 特征共线性未分析**：9/15 surprisal 特征可能高度相关，影响 "15 维" 的解读（虽 LightGBM 对共线性不敏感）

---

## Reviewer Consensus [AGREE]

1. **θ 阈值是论文最大软肋**——两人独立发现并一致评 Critical，建议 K*(θ) 曲线 + threshold-conditioned 结论
2. **self_BLEU 部署问题**——两人独立发现，需说明推理时计算方式 + ablation
3. **C3 效果量过小**——两人一致，缺多重校正，100% 合成不现实
4. **Neural probe framing 误导**——"representation-independent" 应改为 "feature-set-specific"
5. **Related Work 有重要遗漏**——paraphrasing evasion 文献应讨论
6. **格式不合规**——Limitations 应独立、缺 Ethics Statement
7. **问题定义的新颖性和学术价值**——两人均认可

---

## Reviewer Divergence [REBUT]

| 问题 | R1 立场 | R2 立场 | 分歧实质 |
|------|---------|---------|----------|
| ≤1.5B 规模限制 | Should-Fix（Abstract 已标注 scale；要求 7B 属 scope expansion） | Critical（实际合成文本来自更大模型，结论实际价值存疑） | 方法论贡献 vs 实证泛化性的权重分配 |
| LLM baseline 比较公平性 | Minor（zero-shot 是最自然部署方式，claim 是 non-trivial） | Warning（应补 few-shot 或 acknowledge 不公平性） | 结论措辞弱化即可 vs 需补实验 |
| Table 1 0v1 无 CI (R2-M2) | Non-issue（Table S8 已有） | Minor | R1 rebut 有效 |
| OBD 首次展开 (R2-M3) | Non-issue（Abstract 已展开） | Minor | R1 rebut 有效 |
| Decoding feature ranking 不一致 (R1-M5) | Minor concern | Non-issue（论文已在 §A.3 处理） | R2 rebut 有效 |

---

## Questions to Authors（合并去重）

1. θ=0.60 是否 pre-registered？还是在看到结果后选定的？是否可通过下游任务性能反向验证最优 θ？
2. 是否测试过用 Pythia 或 OLMo 作为 surprisal scorer？如果未测试，如何论证 scorer 选择不系统性影响 K*？
3. self_BLEU 在部署时如何计算？若用 depth-agnostic 参考集，性能下降多少？
4. 80-92% transfer retention 是否主要由 0v1 驱动？去除 depth-0 后 retention 如何变化？
5. C3 binary-ours vs binary-Drayson（+0.28pp）是否通过 paired significance test？
6. 是否尝试过 15D 特征与 neural probe 特征的组合？如果组合后 K*>2 会如何影响结论？
7. 在 7B+ 模型上 K* 是否仍为 2？
8. C3 仅用 MMLU/HellaSwag 两个 benchmark，对 "curation guideline" 的实践性 claim 是否充分？

---

## Missing References

1. **Krishna et al. (NeurIPS 2023)** — "Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense"——与 rewrite mode 直接相关
2. **Sadasivan et al. (2023)** — "Can AI-Generated Text be Reliably Detected?"——AI 文本检测的理论限制
3. **Wei Hao et al. (ACL 2025)** — "Learning to Rewrite: Generalized LLM-Generated Text Detection"——与 rewrite mode 跨模型 transfer 相关
4. **12 条 orphan bib entries**：gambetta2025surplexity, gerstgrasser2024inevitable, dohmatob2025strong, amin2025escaping, shi2025generalization, kaplan2020scaling, kirchenbauer2023watermark, gehrmann2019gltr, zellers2019grover, ippolito2020detection, gupta2023continual, yi2025escaping——应引用或清理

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置 external_review.paperreview_ai.enabled = false）

---

## Overall Assessment

**评分：Weak Reject / Borderline（偏 Findings track）**
**置信度：High（4/5）**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 2.5/5 | 3.5/5 | 3.0/5 |
| Excitement | 3.5/5 | 3.0/5 | 3.25/5 |
| Overall | 3/5 | 3/5 | 3.0/5 |

**核心判断**：

论文提出了一个新颖且有学术价值的问题——递归合成文本的 generational depth estimation。DPI 理论框架优雅，实验覆盖多模型/多 decoding，统计方法论规范。然而存在三个 Critical 问题：

1. **K*=2 是 threshold artifact 而非 robust finding**。θ=0.60 的选择缺乏 principled justification，边界 marginal 到 ±0.15pp 就改变结论。论文需要从 "K*=2 is consistent" 转向 "K*(θ) 的特征化"。
2. **Scorer-generator confound 未控制**。60% 的特征空间依赖 Qwen 计算 surprisal，Qwen 配置中 scorer=generator 的 self-familiarity bias 未排除。
3. **self_BLEU 训练/部署不一致**。特征定义依赖 label 信息，部署方案未说明。

这三个问题不需要推翻论文框架，但需要补充实验和修改结论表述。C3 filtering 的效果量极小（+0.76pp MMLU）在 100% 合成设定下，作为实践性 claim 的支撑不足。

**如果以下条件得到满足，论文可达到 EMNLP main conference 水平**：
- C1：提供 θ 的 principled justification 或转为 K*(θ) 曲线呈现
- C2：补充至少一个替代 scorer 的 feature ranking 对比
- C3：报告 14D（去除 self_BLEU）ablation + 说明部署协议
- 格式合规：Limitations 独立 section、Ethics Statement

**当前状态建议 Findings track 或 major revision。**

---

## Detailed Comments（逐节）

### Abstract
- 过长（~250 words），压缩至 200 以内
- "K*=2 is consistent" 改为 threshold-conditioned 表述
- "representation-independent lower bound" 改为 "feature-set-specific lower bound"
- "8 conditions" 表述需澄清

### Introduction
- 第 2 段与 model collapse 文献的衔接给人直接测量 retrain-chain 的印象，需明确区分 prompt-chain
- "depth features are largely text-intrinsic" 措辞需弱化

### Related Work
- 补充 paraphrasing evasion 文献
- 讨论 depth estimation 对 adversarial paraphrasing 的鲁棒性
- 清理 12 条 orphan bib entries

### Method
- θ=0.60 的 justification 需加强或改为 K*(θ) 曲线
- self_BLEU 特征的部署协议需说明
- scorer 选择的潜在 confound 需讨论

### Experiments (C1)
- 将 sensitivity analysis 从 Appendix 提至主文
- "8 conditions" 澄清 decoding 消融的模型
- CI 数值精度统一（0.6015 vs 0.602）
- Transfer retention 数值修正（83% → 85%）
- 补充跨模型 0v1 AUC 具体值

### Experiments (C3)
- 策略间差异补 paired test + 多重校正
- "50% degradation reduction" 需加现实场景 caveat
- 考虑 mixed-ratio 实验

### Discussion
- Neural probe framing 修正
- "requires specialized features" 弱化为 "not solved in zero-shot setting"
- "~88%" 标注具体模型名

### Conclusion
- 同 Abstract 的 threshold-conditioned 修改

### Format
- Limitations 独立为 \section*{Limitations}
- 添加 Ethics Statement
- 压缩 Abstract