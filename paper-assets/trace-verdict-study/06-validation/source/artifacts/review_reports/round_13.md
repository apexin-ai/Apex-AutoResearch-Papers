---
round: 13
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-25T04:38:45.276338+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 13 (Fresh Review)

**论文**: "Trace Verbosity Degrades SFT Verdict Prediction: A Systematic Analysis of Information Density Effects"
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**审稿模式**: 重新审稿（fresh）
**Reviewer**: R1（方法/实验严谨性）、R2（新颖性/完整性/Related Work/写作）
**交叉轮次**: 1 轮（共识充分，无需第二轮）

---

## Summary

本文研究执行 trace 的详尽程度如何影响 SFT verdict prediction（二分类 pass/fail）。在 4 个代码专用模型（1.5B–13B，3 个架构家族）上发现：完整 trace（77–82%）比仅含异常事件的紧凑输入（≥99.33%）低 18–23pp。通过 gradient masking 实验将 ≤4% 退化归因于训练时梯度稀释，其余归因于推理时信号稀疏。论文还识别了两层信号层级和 384→512 tail tokens 处的相变。

---

## Strengths

**S1. 实验设计严谨全面** [R1, R2 一致]
4 模型 × 3 架构家族 × 7 trace 条件 × 多种子，构成完整消融矩阵。统计方法周全：Wilson CI、paired bootstrap (B=10,000)、clustered bootstrap (n_eff=119)、Holm–Bonferroni 校正。执行质量显著高于平均 empirical study。

**S2. Gradient masking 方法论新颖** [R1, R2 一致]
通过掩蔽 99.8% 梯度更新隔离训练时梯度稀释效应（≤4% 上界），是巧妙的实验设计。虽然因果声称需弱化（见 MF-1），方法本身有独立价值。

**S3. 尾截断预算曲线与相变发现** [R1, R2 一致]
Figure 3 揭示 384→512 tokens 处的尖锐相变（4 模型一致 +13–22pp 阶跃），与 globals module dump boundary 吻合。实用性强。

**S4. 格式标记消融有效** [R1, R2 一致]
nomarker 实验分离格式依赖和语义学习（去标记后仍达 97.65%），证明模型学到超越 surface shortcuts 的模式。

**S5. 附录详尽、格式完全合规** [R1, R2 一致]
21 页附录包含完整结果、算法伪代码、trace 示例、tokenizer 分析、错误分析。格式合规性满分（8 页正文、匿名性、Abstract <200 words、Limitations section 等）。

**S6. Limitations 诚实** [R1, R2 一致]
明确承认 forward-pass attention confound、模型规模限制、任务范围限制，不过度声称。

---

## Weaknesses（按严重性排序）

### Must-Fix（影响接收决定）

**MF-1. Gradient masking 因果声称超出证据——需统一弱化为 upper bound estimate** [R1-N1, R2 cross-AGREE | 共识]

Abstract "controlled gradient masking attributes ≤4% to training-time dilution" 是因果表述，但实验仅能提供上界估计。具体问题：
- Forward-pass attention confound 未量化（§4.4 line 139-140 自身承认）
- Additivity assumption（训练效应与推理效应可加性分离）未验证
- Gradient masking 在 matched format（exception_only）下得出 ≤4%，但 full_trace 退化发生在完全不同的输入格式下，不可直接相减

需修改位置：Abstract、Introduction Contribution 3、Conclusion (line 4) 三处统一改为 "places an upper bound of ≤4% on backward-pass dilution under matched format"，并显式承认 additivity assumption。

**MF-2. "Inference-time signal sparsity" 是残差归因，与 truncation evidence 存在内部张力** [R1-N2, R2 cross-AGREE | 共识]

论文将 gradient dilution ≤4% 后剩余 ~96% gap 归因于 "inference-time signal sparsity"，但这是排除法推断而非正面证据。更严重的是论文内部存在未调和的张力：
- §4.4 (line 171): "all 217 full_trace errors occur where tokenizer truncation removes diagnostic markers" → 暗示退化因 truncation
- §4.5 (line 179): "removing the token budget entirely yields 81.76%, identical to head-2048, ruling out truncation" → 声称排除 truncation
- 但 "no truncation" 实际仍有 training max_length (2048) 的隐式截断

论文应区分三种机制并分别量化：(a) 外部 token budget truncation；(b) 模型 training-length 隐式截断（positional truncation）；(c) 窗口内诊断 token 被无关 token 稀释的 genuine signal sparsity。Tail-truncation 数据（tail-512 即恢复 93-98%）强烈暗示 positional truncation 是主因，而非 signal sparsity。

**MF-3. 任务范围过窄，标题/contributions 措辞暗示超出证据的普遍性** [R2-N2, R1 cross-AGREE | 共识]

Verdict prediction 是 exception-based representation 最有利的任务——二分类且异常事件几乎完全决定标签。标题副标题 "Information Density Effects" 暗示广泛适用性；三个 contributions 措辞暗示普遍性；但 Discussion §5 仅在末尾简短限定。DebugBench 验证（Appendix M）headroom 仅 3.29pp，无法独立支撑泛化论证。

建议：(1) 标题改为限定性表述如 "...in Verdict Prediction"；(2) Abstract/Intro 开头就明确任务范围；(3) "scale effects" 改为 "observed pattern across tested 1.5B-13B range"。两位 Reviewer 一致认为不需要增加新任务实验，但 framing 必须与证据匹配。

### Should-Fix（影响评分但不一票否决）

**SF-1. 核心发现在 verdict prediction 上的新颖性需重新定位** [R2-N1 critical, R1 cross-REBUT | 分歧，Director 降级为 should-fix]

R2 认为 exception ≈ verdict 使核心发现接近 tautological（稀释必然降低准确率是已知现象），建议重定位为 "quantifying a known but previously unvalidated phenomenon"。R1 反驳：贡献是 mechanism decomposition（从 "what" 到 "why"），gradient masking、phase transition、format ablation 有独立价值。

**Director 判定**：R1 的论证有说服力——mechanism decomposition 是非平凡贡献。但当前 Introduction 叙事在 "exceptions work" 和 "why traces hurt" 之间切换，容易给读者 tautological 的印象。建议在 Introduction 末尾加 explicit contribution boundary statement，明确贡献是 decomposition methodology 而非 direction of finding。与 MF-3 的 scope 限定协同修改。

**SF-2. 对 DCSH (Wang et al. 2025) 增量贡献 positioning 不充分** [R2-N3, R1 cross-REBUT | 部分共识]

DCSH 已发现 "trace utility is task-dependent" 和 "format matters"。当前 Related Work §2 仅一句话区分。R1 论证增量贡献充分（component-level ablation、gradient masking、cross-architecture validation），但同意 positioning 需更 explicit。

建议在 Introduction 或 Related Work 中用一段列出：(1) DCSH 发现了什么；(2) DCSH 没有解答什么（退化机制、训练/推理归因、组件层级）；(3) 本文如何回答这些遗留问题。

**SF-3. exception_only 49% 测试集重复导致 CI 膨胀** [R1-W1, R2-W5 | 共识]

1,190 测试样本中约 583 个独立样本（within-problem 重复）。Table 1 的 Wilson CI 基于 N=1,190，实际 CI 应扩大约 √2 倍。Clustered bootstrap (n_eff=119) 仅用于 pairwise p-value，主表未使用。

论文在 Appendix P 确认去重后变化 <0.1pp，但主表应至少报告 effective N=607 和对应 CI，或同时展示 clustered CI。

**SF-4. GPT-4o 对比混淆学习范式和输入格式** [R2-W2, R1 cross-AGREE | 共识]

Zero-shot GPT-4o (84.45%) vs. SFT Qwen-7B (99.83%) 混淆了两个变量。Abstract "a 7B SFT model surpasses GPT-4o by 12 points" 虽有限定词仍具误导性。建议弱化措辞并明确标注 "SFT vs. zero-shot, not directly comparable"，或增加 GPT-4o few-shot + exception_only 对照。

**SF-5. Label-only loss 仅在 Qwen 家族有效，跨架构 collapse 未充分解释** [R1-W5, R2 cross-AGREE | 共识]

CodeLlama/DeepSeek 在 label-only loss 下 collapse 到 majority baseline (28.5%)，§4.4 仅一句 "architecture dependence" 作为解释。后果：(1) label-only loss 作为 complementary evidence 证据力仅限 Qwen 家族；(2) gradient dilution 机制可能因架构而异。

建议增加 collapse 原因分析或将 label-only loss 降为 Qwen-specific 辅助分析。

**SF-6. 两层信号层级应从独立 contribution 降级** [R2-W6, R1 partial-REBUT | 部分共识]

R2 认为 Tier 1/2 区分（verdict-decisive vs. not）是可预期的观察。R1 指出合并信号反而降低性能（VOTA 99.05% < exception_only 99.83%）和 discrete clustering (k=2, silhouette≥0.74) 是非平凡发现，但同意降低权重。

建议在 Introduction Contribution 列表中将 two-tier signal hierarchy 从独立 contribution 降级为 Contribution 1 的 supporting finding。

**SF-7. 模型规模限制** [R2-W4, R1 cross-AGREE | 共识]

1.5B–13B 仅 ~8.7×，其中 6.7B 和 7B 近乎重叠，实际只有 3 个有效 scale points。Figure 2 覆盖范围不足一个数量级。建议 §4.2 中 "scale effects" 改为 "within-range observations"，Discussion 增加对更大模型（30B+）是否克服信号稀释的讨论。

**SF-8. CodeLlama full_trace 使用 head-2048 proxy** [R1-W3, R2 cross-AGREE | 共识]

Head truncation 系统性低估 full_trace 性能（tail-truncation 实验证实末尾包含诊断信息）。CodeLlama 非核心分析模型且已标注 §，影响有限，但应在 Limitations 或 footnote 中明确讨论 proxy 偏差方向。

---

## Questions for Authors

1. 论文内部 truncation vs. signal sparsity 的张力如何调和？§4.4 "217 errors are truncation-driven" 和 §4.5 "no truncation yields same result" 是否矛盾？如何区分 positional truncation 和 genuine signal sparsity 的贡献？（MF-2 核心问题）
2. 是否预期在更复杂任务（fault localization、program repair）上也观察到 exception_only 优势？如果不是，这是否意味着发现特定于 verdict prediction？（MF-3 相关）
3. Gradient masking 的 forward-pass attention confound 潜在大小估计？是否有办法量化注意力分配对性能的影响？（MF-1 相关）
4. 为何不尝试 prompt compression（如 LLMLingua / SelectiveContext）恢复 full_trace 性能？这将直接测试 signal dilution vs. signal absence 假设。（R2 提问）
5. DCSH 的具体遗留问题是什么？本文如何回答这些问题？（SF-2 相关）
6. Label-only loss 在 CodeLlama/DeepSeek 上 collapse 的根因分析？是否与 tokenizer 或 attention 机制相关？（SF-5 相关）

---

## Missing References

**两位 Reviewer 共同建议**：
- Liu et al. (2024) "Lost in the Middle: How Language Models Use Long Contexts" — 与 full_trace 中间部分信息利用不足直接相关
- Li et al. (2017) "Feature Selection: A Data Perspective" (ACM Computing Surveys) — 加强与 feature selection / Hughes effect 的理论联系
- Zheng et al. (2024) "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" — verdict prediction 作为 LLM test oracle 的文献补充

---

## External Review

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 已完成（0 critical, 1 warning, 9 info）

**Warning**:
- Page 8：Figure 4（reliability diagrams, 2×2）和 Figure 5（training dynamics）同时出现在一页，加上 Discussion 和 Conclusion 两个 section 开头。两个 figure 均被压缩到较小尺寸——Figure 4 的四个子面板 axis tick labels 和 legend 文字接近可读性下限（估计 ≤6pt），灰度打印时面板内对角参考线与数据点可能难以区分。

**Info highlights**:
- Figure 1 出现在 page 2 顶部，在前 3 页范围内，Title-Abstract-Figure 1 故事一致性良好
- Figure 2 y 轴非零起始（~93-94%），视觉放大条件间差异（ML 论文常见做法，有 label 标注）
- Limitations 简短（~1/3 栏），覆盖 3 点，符合 EMNLP 要求
- 引用格式统一，未发现 [?] 未解析引用
- 末页约 60-65%（appendix 末尾，不影响评审）

---

## Overall Assessment

**综合评分：3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 4.0/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.0/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4.5/5 | 4.0/5 | 4.0/5 |
| Overall | 3.5 | 3.0 | **3.0** |

**评分理由**：

论文的实验执行质量出色——4 模型 × 3 架构 × 7 条件 × 多种子的消融矩阵配合完整统计检验链，是严谨的 empirical study。Gradient masking 方法论（S2）和尾截断相变发现（S3）是真正有价值的贡献。

但三个结构性问题限制了主会议接收的可能性：

1. **因果声称超出证据**（MF-1, MF-2）：gradient masking 的 additivity assumption 未验证，signal sparsity 归因与 truncation evidence 存在内部张力。这不是可以在 rebuttal 中简单回应的措辞问题——需要实质性修改以区分 positional truncation 和 genuine signal sparsity 的贡献。

2. **任务范围与 framing 不匹配**（MF-3, SF-1）：verdict prediction 上 exception ≈ verdict 的近 tautological 关系限制了核心发现的新颖性和影响力。标题和 contributions 暗示的普遍性超出证据支持。R1 论证 mechanism decomposition 是非平凡贡献有一定说服力，但当前 framing 未能有效传达这一定位。

3. **Excitement 不足**（SF-6, SF-7）：两层信号层级和 scale effects 的 novelty 有限，任务范围窄限制了对 NLP 社区的影响力。

**定位**：强 Findings 论文。执行质量和方法论贡献（gradient masking, phase transition）支撑 Findings 接收。

**升级路径**（→ 3.5 Borderline Conference）：
- 修正 MF-1/MF-2 的因果声称和内部张力
- 重新定位 framing：贡献是 decomposition methodology 而非 direction of finding（SF-1）
- 限定标题和 scope（MF-3）
- 更充分论证对 DCSH 的增量（SF-2）

如果作者能在 rebuttal 中 convincingly address MF-1 和 MF-2（特别是区分 positional truncation vs. signal sparsity），并调整 framing 使其与证据强度匹配，评分可上调至 3.5 (Borderline Conference)。

---

## Detailed Comments

### R1 与 R2 共识/分歧汇总

| 问题 | R1 | R2 | 交叉后状态 |
|------|-----|-----|-----------|
| Gradient masking framing | Must-Fix | Must-Fix (cross-AGREE) | **共识：Must-Fix** |
| Signal sparsity 残差归因 | Must-Fix | Must-Fix (cross-AGREE) | **共识：Must-Fix** |
| 任务范围过窄 | Should-Fix | Must-Fix | **共识：Must-Fix**（R1 同意方向，升级严重性） |
| 核心发现 tautological | 否 (REBUT) | 是 (维持) | **分歧**：Director 降级为 Should-Fix |
| DCSH 增量不足 | REBUT（增量充分） | Must-Fix | **部分共识**：positioning 需改进 |
| CI 膨胀（49% 重复） | Should-Fix | Should-Fix | **共识** |
| GPT-4o 对比 | AGREE | Should-Fix | **共识** |
| IB 理论联系 | REBUT（不可行） | Should-Fix | **分歧**：Director 降为 Minor |
| Abstract 数字 | REBUT（style） | Should-Fix | **分歧**：Director 降为 Minor |
| Scale limitation | AGREE | Should-Fix | **共识** |
| DeepSeek 2-seed | Should-Fix | REBUT（排除合理） | **分歧**：Director 降为 Minor |
| Tier hierarchy novelty | Partial-REBUT | Should-Fix | **部分共识**：降低权重 |
| Label-only loss | Should-Fix | AGREE | **共识** |
| CodeLlama proxy | Should-Fix | AGREE | **共识** |

### 跨轮次 Issue 追踪更新

本轮（Round 13）新增 4 个 issue（W2b, W12, W13, W14），更新 8 个既有 issue 的 mentions 和 action_items。详见 `artifacts/review_issues.yaml`。

关键跨轮趋势：
- **W1（tautological framing）**：Round 12 首提，Round 13 仍存在且两位 Reviewer 分歧未完全解决。但 R1 提供了有力的 rebut 论证，Director 降级为 Should-Fix。
- **W2（gradient masking confound）**：Round 12 首提，Round 13 升级——R2 补充了 truncation vs. sparsity 内部张力分析（新增 W2b）。
- **W4（over-generalization）**：Round 12 首提，Round 13 仍存在且共识更强。
