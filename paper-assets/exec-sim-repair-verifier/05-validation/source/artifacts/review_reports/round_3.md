---
round: 3
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-19T08:41:32.446070+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study"
**目标 Venue**: EMNLP 2026 via ARR (deadline: 2026-05-25)
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
**圆桌轮次**: 1 轮（Round 1 + 交叉分享后达成共识）

---

## Summary

本文对 execution-free code verification 的三种 formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹级评分）进行了系统比较，覆盖两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（function-level、repo-level）和多 seed。核心发现：function-level 三者统计等价（TOST p=0.007, ±2pp）；repo-level CLS 大幅优于 CWM（19–26pp gap）；error complementarity 支持 ensemble。研究设计有野心，统计方法（TOST、clustered bootstrap、ICC）在 NLP 经验论文中属于高水平；但 "controlled comparison" 的执行在 repo-level 有多个系统性缺陷，新颖性定位偏高于实际贡献深度。

---

## Strengths

**S1. 研究问题重要且清晰。** 验证 pipeline 中的 formulation 选择是实际工程决策，无先前工作提供 head-to-head 比较。论文填补了一个真实空白。[R1, R2 共识]

**S2. 多维度实验设计。** 覆盖 formulation(3) × model family(2) × model size(2) × complexity(2) × seeds(up to 5)，比该领域典型论文更系统。[R1, R2 共识]

**S3. 统计方法规范。** TOST 用于 null-result claim（而非仅 "无显著差异"）、clustered bootstrap 处理 within-problem 依赖、ICC 量化相关结构——方法选择均正确。[R1, R2 共识]

**S4. Failure mode taxonomy 有洞察力。** Table 4 区分 format collapse / decision collapse / aggregation penalty，且展示同一模型在不同 configuration 下触发不同模式（DeepSeek s42 vs s123），是非平凡发现。[R1 强调, R2 认同]

**S5. 消融设计全面。** LoRA rank、序列长度 matched-context、训练数据 downsampling、few-shot baselines、relaxed matching——系统性地排除了常见替代解释。[R1, R2 共识]

**S6. Limitations 诚实。** 论文在正文和 Appendix 中主动披露了几乎所有方法论弱点（单 seed、NaN loss、eval seq_length 不一致等）。[R1 特别提及]

---

## Weaknesses

### Critical（Must-Fix，影响接收决定）

**C1. TOST ±2pp equivalence margin 缺乏正式论证和 sensitivity analysis** [R1-N1, R2 AGREE]

§4.4 的 ±2pp margin 仅以一句话论证（"unlikely to affect deployment decisions"）。缺乏：(1) margin sensitivity 分析（±1pp/±1.5pp/±2pp/±3pp 下的 p 值梯度表）；(2) smallest equivalence margin 报告；(3) 基于 deployment cost model 的实质性论证。在 85–88% 的准确率范围内，2pp 不是小差异。如果 ±1pp 下 TOST 不成立，"equivalence" 需降级为 "near-equivalence"。直接动摇 Contribution #1 的基础。

**C2. "Controlled comparison" 声称与实际设计存在系统性裂隙** [R1-N2, R2 AGREE]

标题 "Controlled Empirical Study" 暗示所有变量被控制，实际仅控制了模型大小和训练数据来源。四项未控制的关键 confound：
- (a) **Checkpoint selection**: CLS 使用 val-best；CWM/DeepSeek-s123 因 NaN validation loss 使用 final epoch。CLS 系统性获得更优 checkpoint。
- (b) **Eval seq_length**: Qwen3 CWM 8192 vs DeepSeek CWM 4096。论文自己报告 ~9pp 的 seq_length variation，但 cross-model comparison 是核心论证策略。
- (c) **Preprocessing**: s42 drop vs s123 truncate。Preprocessing 对 CLS degradation 有 ~3× 影响（4pp vs 12pp）。
- (d) **TRAJ regime**: 不同 lr (2e-4 vs 5e-5)、不同训练集大小 (~400 vs ~70K)、不同评估粒度 (n=48 vs n=9784)。

这些 confound 单独不致命（repo-level 19–26pp gap 足够大），但合在一起削弱 "formulation-driven" 的因果归因，且部分 confound 方向系统性偏向 CLS。

**C3. Repo-level n=48 variant-level 统计效力严重不足** [R1-N3, R2-N2, mutual AGREE]

n=48 下 SE ≈ 5.8pp，95% CI 宽 ±11.3pp。CLS Qwen3-8B 两 seed 差 8.33pp（72.92% vs 81.25%，仅 4 个 variant 翻转）。TRAJ DeepSeek 6-seed std = 5.00pp。variant-level 结论对 seed 极度敏感。论文混用 per-test (n=9784) 和 variant-level (n=48) 结果且未充分区分统计可靠性。Contribution #2 的 framing 远强于 variant-level 证据支撑。缺少 bootstrap CI 和 power analysis。

### Warning（Should-Fix，影响评分）

**W1. CWM baseline external validity 严重受限但仍做 formulation-level 归因** [R1-W2, R2-W4, mutual AGREE]

4–8B LoRA fine-tuned CWM ≠ 32B execution-trace mid-trained CWM。正文使用 "generation formulation" / "output space complexity" 做归因，但 4B→8B 仅 2× scale，不足以推断 formulation-level 天花板。Repo-level CWM format collapse 可能是 capacity 问题而非 formulation-inherent。

**W2. Abstract 数据堆砌** [R2-W1, R1 AGREE]

~250 words 内 15+ 个数值，读起来像实验结果压缩而非叙事。违反写作规范（最多 2–3 关键数字）。

**W3. Cross-model "validation" 措辞过强** [R1-W4, R2 AGREE]

n=2 model families 不构成 "validation"，至多 "consistency check" 或 "directional evidence"。单 seed DeepSeek 数据高度不稳定（CLS 7.68pp spread）。

**W4. 新颖性定位："design space" 仅 3 个离散点** [R2-N1, R1 部分 AGREE]

标题 "Formulation Design Space" overselling——3 个离散 formulation 不构成连续 space。Function-level equivalence 较预期；repo-level 分析归结为 "生成长输出更难"。与 process vs outcome supervision 文献增量不够明确。R1 认为 failure mode taxonomy 有增量价值（轻度分歧）。

**W5. 多重比较问题未处理** [R1-W1, R2 AGREE]

论文以统计严谨性为卖点但未区分 primary/exploratory comparisons，未应用任何多重比较校正。

**W6. 合成数据外部效度讨论不足** [R2-W2, R1 AGREE]

Limitations 仅一句话提及 synthetic-to-real transfer gap。对 formulation ranking 可能因训练数据来源而变化的风险未讨论。

**W7. Error complementarity / ICC oracle analysis 适用范围未限定** [R1-W5, R2 AGREE]

Function-level ICC=0.191 用于 repo-level oracle analysis 的 transfer 未论证。Repo-level CWM format collapse 使错误互补性不成立（CWM variant-level 低于 majority baseline）。结论应限定为 function-level。

**W8. Related Work 遗漏近期直接相关工作** [R2-W3, R1 部分 AGREE]

缺失：CodePRM (ACL 2025 Findings)、FunPRM (2601.22249)。R1 另指出缺 constrained decoding 方法论文献。CodeScaler 和 CodeRL+ 的相关性需确认。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：

1. **TOST margin sensitivity**: ±2pp 论证不足，需 gradient table 和 smallest margin [C1]
2. **"Controlled" framing gap**: 四项 confound 削弱因果归因，建议改 "systematic" [C2]
3. **Repo-level statistical power**: n=48, single-seed, 缺 CI/power analysis [C3]
4. **CWM external validity**: 4–8B LoRA 结论不可推广为 formulation-level [W1]
5. **Abstract overloaded**: 15+ 数字，需精简至 2–3 [W2]
6. **Cross-model "validation"**: 措辞过强，应降为 "consistency check" [W3]
7. **Overall score**: 3.0 (Findings) [两人独立一致]

## Reviewer Divergence [REBUT]

仅有两项轻度分歧，均不影响结论：

1. **Re-repair pilot 定位** — R1 认为不应暗示为 contribution；R2 指出它已正确放置在 Appendix 作为负面 pilot，定位恰当。**结论：R2 的 REBUT 成立，论文已正确处理。**

2. **Novelty/Excitement 评分** — R1 给 3.5/5（认为 failure mode taxonomy 有增量价值），R2 给 2.5/5（认为深层机制洞察不足）。**结论：轻度分歧，不影响总分。novelty 定位为 "empirical methodology contribution" 比 "design space exploration" 更准确。**

---

## Questions（需作者回答）

**Q1.** TOST 在 ±1pp margin 下是否仍然成立？请提供 ±1pp/±1.5pp/±2pp/±3pp 下的 p 值。[R1, R2 一致提问]

**Q2.** 是否尝试过修复 CWM 的 NaN validation loss（如 gradient clipping、loss masking、更小 lr）？如果未尝试，是技术限制还是时间限制？[R1]

**Q3.** CLS Qwen3-8B 两 seed variant-level 差异 8.33pp（72.92% vs 81.25%）。如何在同一 formulation 内如此大的 seed variance 下，仍将 formulation 间差异归因于 formulation choice？[R1, R2 一致关注]

**Q4.** CWM parseable outputs 是否系统性偏向 harder instances？即 unparseable outputs 是否集中在简单 instances？[R1 独特提问]

**Q5.** Oracle ensemble 90.63% 在其他 seeds 下是否稳定？repo-level 的 error complementarity 是否成立（考虑 CWM variant-level < majority baseline）？[R1, R2 一致关注]

**Q6.** 如果改用 real bug data（非 mutation），formulation ranking 是否可能改变？[R2]

---

## Missing References

以下引用经两位 Reviewer 确认应补充：

1. **CodePRM** (ACL 2025 Findings) — process-level verification in code generation [R2 提出, R1 AGREE]
2. **FunPRM** (arxiv 2601.22249, 2026) — function-as-step PRM，与 TRAJ 直接相关 [R2 提出, R1 AGREE]
3. **Constrained decoding 方法论** (如 Willard & Louf 2023) — §4.5 讨论了 constrained decoding 但未引用 [R1 提出]

以下引用需确认相关性后酌情补充：
4. **CodeScaler** (arxiv 2602.17684, 2026) [R2 提出, R1 要求确认相关性]
5. **CodeRL+** (arxiv 2510.18471, 2025) [R2 提出, R1 要求确认相关性]
6. **近年 mutation-real fault coupling meta-analysis** [R1 提出]

---

## External Review (Stanford Agentic Reviewer)

外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置）。跳过。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**EMNLP 2026 ARR 评分标准**: 3 = Findings（可被 Findings 接收）

**维度评分汇总**:

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Overall | 3.0 | 3.0 | 3.0 |
| Confidence | 4/5 | 4/5 | 4/5 |

**综合判断**:

研究问题重要且实用，实验设计有野心（多 formulation × 多模型 × 多 seed × 多复杂度），统计方法在 NLP 经验论文中属于高水平。Function-level 分析扎实（5 seeds, proper TOST, bootstrap CI），failure mode taxonomy 有诊断价值。

但承载最重要结论的 repo-level 分析在统计支撑上最薄弱：n=48 variant-level evaluation, 1–2 seeds, checkpoint selection asymmetry, eval protocol inconsistency。"Controlled comparison" 的 framing 与实际控制程度不匹配。新颖性受限于 3 个离散 formulation 点和较浅的机制分析（"生成长输出更难"）。论文的 Limitations 诚实地覆盖了大部分问题，但 Abstract/Contributions 的措辞未反映这些 caveats 的严重程度。

**升级至 Conference (3.5+) 的路径**:
1. 解决 C1：提供 TOST margin sensitivity gradient table
2. 解决 C2：将 "Controlled" 改为 "Systematic"，增加 threats to validity 段落
3. 解决 C3：为 variant-level 比较增加 bootstrap CI 和 power analysis，降低 claims 语气
4. 解决 W1：全文 CWM 结论限定为 "at ≤8B LoRA scale"
5. 解决 W2：Abstract 精简至 2–3 关键数字
6. 解决 W4：调整标题，深化机制分析

以上修改在截止日（2026-05-25）前技术上可行，但需要实质性的重写和可能的补充实验。

---

## Detailed Comments（逐节）

### Abstract
- 15+ 数字，数据堆砌严重。应保留 function-level equivalence 和 repo-level gap 两个核心数字，其余定性描述。
- "same source data with formulation-appropriate label granularity" 已改善了 Round 3 的 "identical data" overclaim，但仍需进一步精简。

### Introduction
- 叙事线清晰（背景→问题→不足→方法→贡献）。
- Contribution #2 语气远强于 repo-level 证据。"Complexity-dependent divergence with formulation × model interaction" 应加 "preliminary evidence suggests" 或 "initial results indicate"。
- 需更明确论证相对 process vs outcome supervision 文献的具体增量。

### Method
- Formulation 定义清晰、数学符号恰当。
- Oracle Accuracy-Utility Framework (§3.3) 论证完整。
- CWM unparseable default-to-pass 策略应在此处讨论方向性影响（当前仅在 Appendix）。

### Experiments
- Function-level (§4.2): 扎实，5 seeds, proper statistics。
- Scaling (§4.3): "matched seeds" 措辞误导（s42 和 s123 preprocessing 不同）。"CWM stagnation" 应改为 "plateau" 或 "flat scaling"。
- Per-test vs TRAJ equivalence (§4.4): 核心问题是 margin sensitivity。NF4 vs bf16 mixing 原因应在正文说明。
- Repo-level (§4.5): 论文最重要也最薄弱的部分。CWM default-to-pass artifact 应在正文讨论。"Cross-model validation" → "Cross-model consistency"。CWM eval seq_length 差异的 caveat 应更突出。Table 3 建议拆分 per-test 和 variant-level。
- Analysis (§4.6): Aggregation penalty 分析有价值。Checkpoint selection confound 是好发现。

### Related Work
- 结构合理（3 段按主题），但偏压缩。缺 CodePRM、FunPRM、constrained decoding 引用。对 PRM/ORM 文献的增量定位不够深入。

### Conclusion
- 基本准确但应反映 variant-level 结论的 preliminary 性质。
- Limitations 段落内容全面但格式需确认是否为独立 section（ARR 要求）。

### Appendix
- 内容充实（A–I），ablation 设计合理。
- Re-repair pilot (j) 作为负面结果正确放置。
- Extended Limitations (F) 是 responsible 做法。

### References
- 38 篇引用，密度中等偏低。需补充 3–6 篇近期直接相关工作。