---
round: 28
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T16:17:34.607653+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 28

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性 + 实验设计 + 统计分析), R2 (新颖性 + Related Work + 写作质量)
**审稿模式**: Fresh (重新审稿)

---

## Summary

本文研究 reasoning model 安全性 probe 中 layer selection metric 的影响。作者定义了 Safety Commitment Point (CP)——reasoning chain 中 safety deliberation 永久停止的第一步——并在 4 个 reasoning model (R1-8B/Llama, OT-7B/Qwen, QwQ-32B/Qwen, R1-32B/Qwen) 上比较 hidden-state (HS) probe 与 text probe 的 CP 检测性能。核心发现：crossing-rate composite metric 系统性选浅层（representation compression artifact），threshold-based metrics 选深层——同一数据在 QwQ-32B 上从 +19pp 显著优势 (p<0.005) 变为非显著 (p=0.83)。7-8B 结果通过 nested 5-fold CV 验证，32B 结果为 exploratory (n≤20)。7 种替代检测方法均未匹配 supervised probing。

---

## Strengths

**S1. 重要的方法论警告，规模量化清晰。** [Consensus R1+R2] Layer selection metric 选择逆转 safety probing 核心结论（QwQ-32B: p=0.83 at CR-composite layers vs. p<0.005 at threshold-based layers）——这不是微小量变而是 qualitative reversal。Layer sensitivity 本身已知（Belinkov 2022），但在 safety domain 中 metric-driven conclusion reversal 的规模在 prior probing literature 中无先例。

**S2. 严谨的统计验证框架。** [Consensus R1+R2] Nested 5-fold CV 正确隔离 hyperparameter tuning；Holm-Bonferroni correction 应用于 12 个 family-wise 比较；BCa bootstrap (10,000 resamples, trace-level clustering)；evidence gradient 分层标注（cross-validated → significant → exploratory）；permutation tests 补充验证。

**S3. 全面诚实的负面结果与 bug disclosure。** [Consensus R1+R2] 7 种替代方法系统性测试及失败原因分析（Table 24）。Section N 主动披露 M002 bug 的发现、影响和修正过程——在 ML 论文中极为罕见的科学诚信实践。

**S4. 高质量引用。** [Consensus R1+R2] 79 引用，双方独立验证 0 hallucinated citations。覆盖 probing methodology、safety detection、reasoning model 等核心方向。

**S5. 高可复现性。** [Consensus R1+R2] 代码/数据承诺公开；所有超参数在附录详列；seeds、split ratios 全部报告。Reproducibility 4-4.5/5。

---

## Weaknesses

### Must-Fix (Critical — 影响接收决定)

**N1. 架构多样性严重限制 generalization。** [Consensus Critical]
3/4 模型为 Qwen 家族。Random-label decomposition（Section B.1）显示 crossing-rate shallow preference 的 geometric component 是 Qwen-specific（label-independent cosine compression），而 R1-8B (Llama) 需要 genuine safety labels 才出现 metric disagreement——mechanism 因架构而异。仅 1 个非 Qwen 模型无法区分 architecture-universal 与 architecture-specific findings，限制了对 Llama/Gemma/Mistral 用户的实际警告价值。
- **建议**: 增加 ≥1 个非 Qwen/非 Llama 架构验证 metric reversal；或显著降低 generalization claim 强度。

**N2. 单一 benchmark + 中等标注信度。** [Consensus Critical]
所有实验仅用 HarmThoughts。CP 标注 inter-annotator κ=0.606（moderate），exact match 37%，MAD 8.5 steps（Table 20）。未进行 CP label perturbation analysis 以评估核心结论对 annotation noise 的 robustness。未讨论为何不使用 ToxicChat、WildGuard、BeaverTails——如果原因是"只有 HarmThoughts 有 step-level CP annotation"，应 explicitly 说明。
- **建议**: (1) CP perturbation analysis（shift ±3/±5 steps，验证 metric reversal 存活）；(2) Method/Limitations 明确 HarmThoughts 唯一性原因。

**N3. 32B 结果 underpowered 但叙事权重过高。** [Consensus Critical]
n≤20 test samples，MDE=8.6-9.5pp（Section Z）。Abstract 用 QwQ-32B 的 p=0.83 vs p<0.005 做 headline "reversal" example——exploratory data 作为论文最 prominent 的 illustration。R1-32B precision=+1.2pp 远低于 MDE，可能是 Type II error 而非真正 null effect。"Exploratory" 标签存在但 framing 权重不匹配。
- **建议**: (1) Abstract headline 替换为 7-8B evidence（如 R1-8B 14-layer divergence）；(2) 32B 分析大幅缩减或移至 appendix，主文仅 1-2 句 summary。

### Should-Fix (Major — 影响评分但不一票否决)

**W1. 新颖性 framing 需锐化。** [Consensus after cross-sharing]
Layer sensitivity 是已知问题（Belinkov 2022, Tenney 2019）；metric-driven qualitative reversal 在此规模是新发现。两者在 Introduction 中混为一谈。C1 应明确区分 "layer sensitivity"（已知）和 "metric-family-driven conclusion reversal"（本文贡献），并论证 safety domain 的 metric sensitivity 为何比 linguistic probing 更 consequential。
- 新颖性评估: moderate — 超越 mere replication，但低于 conceptual breakthrough。

**W2. 解决方案缺失或半成品。** [Near-consensus; R1=strong W, R2=critical N]
Section Z.1 multi-metric ensemble 仅半页，未经 cross-validation 验证。Half-baked solution 比 no solution 更减分。
- **建议**: 要么将 Z.1 扩展为 validated mitigation（CV + multi-model + vs single-metric 统计对比），要么删除 Z.1 并明确 "solving this is future work"。

**W3. Headline HS 优势数字来自弱 baseline。** [Consensus]
Abstract 报告 +20.1 to +21.9pp 来自 MiniLM-384d；BGE-large (1024d) 下仅 +6-12pp，且仅 OT-7B HB 后显著（Section S）。
- **建议**: Abstract 报告 full range（"+6 to +22pp depending on text encoder quality"）。

**W4. CR-composite vs threshold-based taxonomy 缺乏先验理论基础。** [Consensus]
5-metric taxonomy 在观察 shallow/deep divergence 后构建——存在 circular reasoning 风险。Section C 的 compression analysis 为 correlational 但非 theoretical justification。
- **建议**: 提供 principled criterion 或明确声明论文不做 metric recommendation，仅报告 sensitivity。

**W5. Researcher degrees of freedom 累积效应未充分量化。** [Consensus]
~2,240 configurations explored；Section Y.1 仅量化 layer selection 维度的 effective independent tests。Window、threshold K、temporal 维度未 corrected。
- **建议**: Discussion 增加 cumulative Type I error risk honest assessment + FDR upper bound estimate。

**W6. 过度 hedging 削弱 validated results 的感知强度。** [R2 raises, R1 partially agrees]
"Initial characterization" 出现 ≥3 次（abstract/intro/conclusion）；7-8B cross-validated 结果与 32B exploratory 使用相同 cautious language，产生 signal confusion。
- **建议**: 7-8B 结果用 assertive language（"we demonstrate"）；hedging 仅保留给 32B exploratory。

**W7. 替代方法 hyperparameter tuning 深度存疑。** [Consensus]
BOCPD: 仅 4Δ × 3 prior；MLP regularization 细节不足。
- **建议**: 明确列出每种方法的 search space + selection protocol；声明 "results upper-bounded by search budget"。

### Minor Issues

- Figure 1 出现在 p7（主文 8 页中），应提前至 p4-5。打印尺寸可读性差。Pages 3-5 连续文字墙。
- Table 4 "MDE" 缩写在主文中未展开。
- Abstract 末句 "at one set of layers...at the other" 含糊——应指明 "depending on metric family"。
- Section 2 与 Section 3.4 对替代检测方法有重复讨论。

---

## Reviewer Consensus [AGREE]

1. **32B 叙事权重过高** — Abstract 应用 7-8B evidence 做 headline，32B 大幅降级
2. **单一 benchmark 是 genuine 限制** — AdvBench geometric precondition 不等于 layer reversal 验证
3. **架构多样性不足** — 1 个 Llama 模型不够排除 architecture-specific concern
4. **新颖性为 moderate** — layer sensitivity 已知，metric-driven reversal 规模是新的
5. **Section Z.1 需要 resolution** — 扩展验证或删除，不能保持半成品状态
6. **Figure 1 可读性** — 需提前和放大
7. **Missing reference: Belrose et al. (2023) Tuned Lens** — 应引用
8. **引用质量** — 79 引用，0 hallucinated citations，覆盖全面

## Reviewer Divergence [REBUT]

1. **因果验证需求** — R1 要求 activation patching/DAS；R2 反驳为超出 scope（论文定位 empirical characterization，Limitations 已承认 correlational，32B 计算成本高）。**Director 判断**: R2 rebuttal 合理，论文不需因果验证。
2. **"Doubly conditional" framing** — R2 认为概念过于复杂；R1 反驳认为精确捕获两个独立 confound，有 actionable value。**Director 判断**: R1 defense 有说服力，term 是 self-explanatory。
3. **"缺乏解决方案"的严重程度** — R2 评为 critical (N)；R1 评为 strong should-fix (W)。R1 引用 diagnostic paper 先例（Gelman & Loken 2013）。**Director 判断**: 关键在于 Z.1 的处理——validate or remove。

---

## Questions for Authors

1. 是否在非 safety probing tasks（syntax、POS）上测试过 metric-induced reversal？如果现象是 general 的，safety-specific 贡献需更强 justification。
2. CP label perturbation: shift ±3/±5 steps 后，metric reversal 和 HS advantage 是否 survive？
3. 能否提供 principled criterion（非 empirical observation）选择 CR-composite 还是 threshold-based metric？
4. MLP probes 具体尝试了哪些 regularization（dropout rate、weight decay、early stopping patience）？
5. QwQ-32B bootstrap samples 增至 100 traces，reversal 是 genuine 还是 small-sample artifact？
6. OT-7B 在 threshold-based layers 上 text precision > HS precision (+4.3pp)——HS 优势是否主要在 recall 而非 precision？
7. CP annotation: oscillating safety labels 的 traces 占比多少？"Final irreversible transition" rule 如何量化处理？

---

## Missing References

**Consensus (应添加)**:
- Belrose et al. (2023), "Eliciting Latent Predictions from Transformers with the Tuned Lens" — layer-wise analysis 直接相关

**Suggested (非必须)**:
- Li et al. (2024), "Inference-Time Intervention" — hidden-state manipulation at inference time [R1]
- Nanda et al. (2023), "Progress measures for grokking" — layer-wise probing in training dynamics [R1]
- Greenblatt et al. (2024), "Alignment faking in LLMs" — safety motivation [R2]
- arXiv:2605.01853 — concurrent work，May 2026 发表，可能 too recent [R2 neutral]

---

## External Review

外部审稿未配置（项目未启用 paperreview.ai）。

---

## Visual Layout Check

**状态**: done (2026-05-21 15:45-15:48 UTC)
**结果**: 0 critical, 2 warnings, 12 info

- **[Warning]** 前 5 页视觉节奏失衡：页 1 纯文本（Abstract+Intro），页 2 有 Table 1，页 3-5 连续 3 页纯文本（Related Work + Problem Setup + Methods），无 figure/table 穿插。"文字墙" 第一印象。
- **[Warning]** Figure 1（核心层级热力图）直到第 7 页才出现（主文仅 8 页）。建议提前至第 4-5 页。
- Figure 1 axis labels 字号偏小，打印时勉强可读。颜色对比度可接受，色盲友好性中等。
- Table 2-3 同页密度高但合理。Table 4 + Figure 2 同页紧凑未溢出。Figure 2 forest plot 清晰可读。
- 页数合规：Section 6 Conclusion 在 p8 结束，Limitations/Ethics 不计入 8 页限制。
- 附录 20 页以表格和文字为主，格式统一。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Consensus Range: 3.0-3.5 (Findings to Borderline Conference)**
**Confidence: 4/5**

| 维度 | R1 | R2 (adjusted) | Director 综合 |
|------|-----|----------------|---------------|
| Soundness | 3.5 | 3.75 | 3.5 |
| Excitement | 3.0 | 2.75 | 2.75 |
| Reproducibility | 4.0 | 4.5 | 4.0 |
| Overall | 3.5 | 3.25 | 3.0 |

**评分理由**:

论文在方法论严谨性上达到了该领域的高标准（nested CV、HB correction、evidence gradient、comprehensive negative results + bug disclosure），核心发现（metric-driven layer selection reversal）是真实且有实际价值的方法论警告。引用质量高（0 hallucinated citations, 79 refs covering all relevant areas）。

三个结构性限制共同阻止 Conference 接收：
1. **架构覆盖** (3/4 Qwen, 且关键 mechanism 被证实 Qwen-specific) — structural, 难以通过写作修复
2. **单一 benchmark** (HarmThoughts only, CP annotation κ=0.606) — structural
3. **无 validated solution** (Z.1 半成品) — fixable but currently unresolved

32B 叙事权重过高加剧了可信度问题，但这是 fixable 的写作问题。

作为 Findings 论文是扎实的——方法论贡献有价值，negative results 对后续研究有指导意义，统计验证框架可作为该领域的 reference standard。

**达到 Borderline Conference 的路径** (所有条件均需满足):
(a) 增加 ≥1 个非 Qwen 架构验证 metric reversal generalization
(b) Section Z.1 要么充分验证要么删除
(c) 32B 从主叙事降级，Abstract 用 7-8B evidence 做 headline
(d) Novelty framing 锐化——区分 "known layer sensitivity" vs "metric-driven reversal"

---

## Detailed Comments

**Abstract**: 信息密度高但可接受。"Initial characterization" 对 validated 7-8B 结果过于谦虚。Headline 数字 (+20-22pp) 来自弱 baseline，应报告 encoder 全范围。QwQ-32B reversal example 应替换为 7-8B evidence。

**Section 1 (Introduction)**: C1 新颖性定位需锐化——区分 "layer sensitivity"（Belinkov 2022）和 "metric-driven reversal"（本文新发现）。Table 1 作为首个 display item 合理但为元数据；核心 Figure 应尽早出现。

**Section 2 (Related Work)**: 覆盖全面。建议引用 Tuned Lens（Belrose 2023）。与 Section 3.4 有部分重叠。

**Section 3 (Method)**: CP 定义清晰。5-metric taxonomy post-hoc 性质应更明确承认。K=5 threshold sensitivity 主文讨论不足。

**Section 4 (Experiments)**: 7-8B 结果有说服力。Section 4.4 32B 讨论应大幅缩减。Section 4.6 负面结果应声明 "upper-bounded by search budget"。

**Section 5 (Discussion)**: Random-label controls 和 compression mechanism 讨论有价值。Mechanistic claims 应标注为 "correlational hypothesis"。QwQ-32B position confound 全吸收未在 Conclusion 充分反映。

**Section 6 (Conclusion)**: 有效总结但混合 validated 与 exploratory 证据。建议分开报告：7-8B cross-validated (+20-22pp) vs 32B exploratory (+15-19pp)。

**Limitations**: 涵盖 3 点但不完整——缺少 CP annotation noise 影响和 BCa small-sample coverage 讨论。应增加 HarmThoughts 唯一性原因。

**Appendix**: 22 页覆盖详尽，是论文重要补充。Section Z.1 需明确定位（validated vs preliminary）。