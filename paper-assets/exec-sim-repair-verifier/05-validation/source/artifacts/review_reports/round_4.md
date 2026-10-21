---
round: 4
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-19T09:57:29.095165+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5 (Fresh Review)

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study"
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计方法; R2: 新颖性+写作质量+相关工作+格式合规）
**审稿模式**: Fresh（重新审稿）

---

## Summary

本文系统比较了三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行实验。Function-level 三种方法近等效（TOST p=0.007, 5 seeds）；repo-level CLS 以 19-26pp 大幅领先 CWM。论文统计方法论在 function-level 达到上游水准，但 repo-level 核心发现受单种子、CWM baseline 规模限制、以及多重 confound 累积的制约。**正文约 11 页，超出 ARR Long Paper 8 页硬限制，是最紧迫的格式问题。**

---

## Strengths

**S1.** 首个在 matched conditions 下比较三种 verification formulation 的系统研究，填补了确实存在的文献空白。[R1 S1, R2 S1, 共识]

**S2.** Function-level 统计方法论极为扎实：5 seeds、两个模型家族、TOST equivalence test + clustered bootstrap (114 clusters, 10K resamples) + ICC + Holm-Bonferroni 多重比较校正。在 ML 实验论文中属于上游水准。[R1 S2, R2 S2, 共识]

**S3.** 对 confounds 和 limitations 的透明度罕见。Section 5 (Threats to Validity) 系统性列出 5 个 confounds 并量化每个 confound 的 observed effect。多数论文不会主动暴露如此深度的局限性。[R1 S3, R2 S3, 共识]

**S4.** Default assignment artifact 分析（§4.5）精彩：CWM 4B→8B "伪改善"的解构（unparseable rate 上升 → majority-class default → accuracy 虚增，parseable-only accuracy 实际下降）展示了评估指标如何误导。[R1 S4, 共识]

**S5.** Failure mode taxonomy (Table 3: format collapse, decision collapse, aggregation penalty) 提供了可操作的诊断框架。同一模型家族在不同 configuration 下表现出不同 failure mode 的发现对理解 formulation × configuration 交互有实质贡献。[R1 S6, R2 S4, 共识]

**S6.** 消融设计充分：LoRA rank ablation、matched-context ablation（确认 input disparity 仅解释 <3% gap）、training data downsample（控制数据量差异）、majority voting ablation、relaxed matching ablation。[R1 S5]

**S7.** 217× throughput advantage 的量化有实际部署参考意义。[R2 S5]

**S8.** 写作无明显 AI 风格痕迹（无 em-dash/en-dash、无黑名单用词），引用完整（58 篇验证无幻觉引用）。[R2 S6, S7]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [Critical] 正文超出 ARR Long Paper 8 页限制（~11 页）。** [R2-N1, R1 AGREE]
PDF 渲染约 11 页正文，超出 2-3 页。ARR 硬约束，可能直接 desk reject。Experiments section 含 5 个 subsection + 5 张 table + 2 张 figure 是主因。
→ **修复方向**: Threats to Validity 移入 Appendix 并在正文保留一段概述；压缩 Repo-Level 的 Default assignment artifact / Constrained decoding / Training and evaluation sensitivity 段落至 Appendix；精简 Introduction 贡献列表。

**W2. [Critical] TRAJ checkpoint selection 协议不一致。** [R1-W1, R2 AGREE]
论文协议：NaN validation loss 时使用 final epoch。CWM 所有 repo-level runs 遵循此协议。但 Qwen3-8B TRAJ 手动选择了 epoch 2 (72.92%) 而非 Trainer 默认 epoch 3 (70.83%)。Table 4 脚注 ♦ 记录了此选择。虽然绝对影响有限（~2pp），但构成协议不一致和 cherry-picking 嫌疑。
→ **修复方向**: 统一 checkpoint 策略，report 两组数字，明确标注 epoch 2 选择是 post-hoc 的。

**W3. [Critical] Table 4 混合 per-test (n=9,784) 和 variant-level (n=48) 指标。** [R1-W2, R2 AGREE]
CLS/CWM per-test accuracy 与 TRAJ variant-level accuracy 并排展示，脚注 ‡ 标注容易被忽略。CLS variant-level accuracy 远低于其 per-test accuracy（如 Qwen3-4B: 83.63% → 64.58%），读者若将 CLS per-test 与 TRAJ variant-level 直接比较会严重误判优劣。
→ **修复方向**: 拆分为 per-test 和 variant-level 两个表，或增加 CLS variant-level 列。

### Should-Fix（影响评分但不一票否决）

**W4. CWM baseline ≤8B LoRA 的条件限制在 Abstract/Introduction 不够突出。** [R2-N2 提出, R1 部分 REBUT]
4-8B LoRA CWM ≠ 32B mid-trained CWM。论文 Conclusion/Threats 已有 "at ≤8B LoRA scale" conditioning，但 Abstract 和 Introduction contribution list 未体现。R2 认为此差距 "essentially invalidates" repo-level 结论；R1 反驳 "invalidates" 过强——matched comparison 正是论文设计目的，conditioned claim 合理。**Director 判断**：R1 论证更有说服力，但 conditioning 确需更突出。
→ **修复方向**: Abstract 和 Introduction contribution list 中加入 "under ≤8B LoRA fine-tuning" 条件限定。

**W5. Repo-level 核心发现依赖单种子。** [R2-N3, R1 AGREE with nuance]
Qwen3 repo-level CLS vs CWM 为单种子 (s42)；variant 评估 n=48。与 function-level 5-seed 标准形成方法论不对称。R1 补充：效应量 19-26pp 远超 function-level seed noise (<2pp)，CI lower bound 10.42pp 仍 substantial，cross-model 方向一致。两人共识：limitation 真实但效应量大到不太可能被 seed noise 反转。
→ **修复方向**: 如可行补充第二个 repo-level seed；否则将措辞从 "evidence" 降级为 "preliminary evidence"。

**W6. TOST ±2pp margin 需改善正当性论证。** [R1-W3 提出, R2 部分 REBUT]
R1 认为缺乏 a priori justification；R2 反驳 ±2pp 是 code verification 场景中 defensible SESOI，观测 gap 仅 -0.45pp，讨论 ±1.5pp vs ±2pp 对实际决策几乎无影响。两人共识：需引用 Lakens (2017) SESOI 框架正式论证。Sensitivity table (Appendix E) 已有。
→ **修复方向**: §4.4 引用 Lakens (2017)，正式论证 ±2pp 选择依据。

**W7. Confounds 累积效应未讨论。** [R1-W4, R2 AGREE]
§5.6 声称 gap "exceeds any individual confound's observed effect by an order of magnitude"，假设 confounds 独立作用。Checkpoint (~2pp) + eval seq_length (~9pp) + preprocessing (~7.68pp) 可能 compound。R2 补充：confounds 大部分对 CWM 不利方向一致，不太可能反转方向，但 gap 精确大小不可靠。
→ **修复方向**: §5.6 增加 worst-case compound scenario 讨论。

**W8. TRAJ 比较存在 5 重未控制混淆因素。** [R2-W3, R1 扩展]
训练数据量 (~400 vs ~70K)、LR (2e-4 vs 5e-5)、评估粒度 (variant vs per-test)、checkpoint 策略 (W2)、label 粒度。Downsample ablation 仅控制第 1 个。CLS-TRAJ repo-level 比较严格来说 uninterpretable。
→ **修复方向**: 明确标注 CLS-TRAJ repo-level 为 preliminary/suggestive，contribution list 相应降级。

**W9. Abstract 数字密度过高。** [R2-W2, R1 AGREE; 跨 3 轮未解决]
约 170 words 含 p=0.007、±2pp、5 seeds、19-26pp、90.63%、+3.12pp、217× 等密集数据。审稿人 30 秒内难以判断核心价值。
→ **修复方向**: 保留 1-2 个关键数字，其余定性描述。

**W10. Related Work 第一段以枚举代替定位。** [R2-W1, R1 AGREE]
8 行内堆砌 ~18 引用，"A proposed X, B proposed Y" 列表式写法。缺乏按 formulation 类型的归纳和本文定位分析。
→ **修复方向**: 按 formulation 类型重组，提炼共性和局限性。

**W11. Introduction 贡献列表过长（~350 words，含大量具体数字）。** [R2-W4, R1 AGREE]
→ **修复方向**: 每条 1-2 句，具体数字移至 Results。

**W12. Post-hoc power analysis 方法论不当。** [R1-W6, R2 部分 AGREE]
Observed power 是 p 值单调函数（Hoenig & Heisey 2001）。R2 认为用作诊断工具解释 CLS-TRAJ 不具结论性比 confirmatory 用法更可接受。
→ **修复方向**: 引用 Hoenig & Heisey，重新表述为 minimum detectable effect。

**W13. NF4 vs bf16 混合 5-seed 分析缺乏正式交互检验。** [R1-W7, R2 AGREE]
→ **修复方向**: 报告 bf16-only TOST 结果。

**W14. Cross-model CWM eval seq_length 不一致但仍作为 consistency 证据。** [R1-W8, R2 AGREE]
→ **修复方向**: 弱化 cross-model CWM consistency 措辞。

### Minor

**M1.** "pp" (percentage points) 缩写全文未定义。[R2-W5, R1 AGREE]
**M2.** Prompt templates（CLS/CWM/TRAJ）未在论文或 Appendix 中展示。[R1-W9, R2 AGREE]
**M3.** Mutation operators 选择理由和实现细节缺失。[R1-W11, R2 AGREE]
**M4.** Table 4 脚注密度极高（4 个不同标记）。[R2-M3, R1 AGREE]
**M5.** Checklist C4 回答 "Partially"（package version numbers），提交前需补全。[R2-M2]
**M6.** 少量 trailing -ing phrases（如 "motivating complexity-aware routing..."）。[R2-M1]
**M7.** Oracle ensemble (90.63%) 仅报告单 seed，应报告多 seed 范围。[R1-W13, R2 降级]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成共识：

1. **页数超限是最紧迫问题** — 可能 desk reject [R1 AGREE, R2 首提]
2. **Repo-level 单种子是核心 limitation** — 效应量大到不太可能反转，但与 function-level 标准形成不对称 [共识]
3. **TRAJ checkpoint 不一致** — 需统一协议 [共识]
4. **Table 4 混合粒度** — 需拆分或增加 variant-level 列 [共识]
5. **Abstract 数字密度过高** — 跨 3 轮未解决 [共识]
6. **Related Work 枚举式** — 需 positioning 重写 [共识]
7. **CLS-TRAJ 比较 uninterpretable** — 5 重 confound 仅控制 1 个 [共识]
8. **Overall 3.0 (Findings)** — 两人独立给出完全一致的评分 [共识]

---

## Reviewer Divergence [REBUT]

**分歧 1: CWM baseline 规模问题的严重性**
- R2: "essentially invalidates repo-level formulation-level conclusions" [critical]
- R1 REBUT: 论文 claim 已 conditioned on "≤8B LoRA regime"；matched comparison 正是论文设计目的；4-8B 实践者仍获得 actionable 指导
- **Director 判断**: R1 论证更有说服力。论文明确 conditions 结论但需在 Abstract/Introduction 更突出

**分歧 2: TOST margin a priori justification**
- R1: 事后合理化，±1.5pp 处 borderline fail，"结论对 margin 敏感" [critical]
- R2 REBUT: ±2pp 是 domain-justified SESOI；观测 gap 仅 -0.45pp；讨论 ±1.5pp vs ±2pp 对实际决策无影响
- **Director 判断**: 均有道理。margin 应通过 SESOI 框架正式论证（R2 建议），但仍应承认 sensitivity（R1 观察）。降级为 should-fix。

**分歧 3: 多重比较校正**
- R1: 未进行多重比较校正 [major]
- R2 REBUT: 事实性错误——论文 §4.1 Statistics 段和 Appendix K (Table 15) 明确有 Holm-Bonferroni 校正
- **Director 验证**: 确认论文包含 Holm-Bonferroni。R1 遗漏。**此 weakness 撤回。**

**分歧 4: Default-to-pass 策略公平性**
- R2 Q4: CWM unparseable default-to-pass 是否公平？
- R1 REBUT: default-to-pass = default-to-majority (72.96%) 是对 CWM 最 charitable 的策略；relaxed matching 反降准确率；default-to-fail 会使 CWM 更差
- **Director 判断**: R1 论证正确。Default-to-pass 有利于 CWM，实际 gap 只会更大。此 concern 方向反了。**撤回。**

---

## Questions（需作者澄清）

**Q1.** Qwen3-8B TRAJ epoch 2 的选择是 a priori 还是 post-hoc？如果是后者，CWM 是否也检查了多个 epoch？[R1-Q1, 共识]

**Q2.** Function-level TOST 限制为 bf16 seeds（排除 NF4 seeds 789/0）后，p 值和结论是否成立？[R1-Q2, R2 AGREE]

**Q3.** CLS/CWM/TRAJ 的 prompt template 是什么？prompt 设计是否经过优化？[R1-Q3, R2 AGREE]

**Q4.** 48 个 repo-level variants 的选择标准是什么？如何从 SWE-bench Verified 500 instances 中选出？[R1-Q4]

**Q5.** Table 3 fail recall 跨 configuration 变化极大（~14% to ~57%）。有多少可归因于 formulation vs configuration？[R1-Q5]

**Q6.** Execution-free verification 的训练标签来自 execution。获取 execution labels 的一次性成本 vs 推理时执行的重复成本的 cost-benefit 分析？[R2-Q3]

**Q7.** 5 种 mutation types 如何选择？synthetic-to-real transfer gap 是否有任何 pilot study？[R2-Q2]

---

## Missing References

1. **Lakens (2017)**, "Equivalence Tests: A Practical Primer..." — TOST margin 的 SESOI 框架标准参考 [R1, R2 均建议]
2. **Hoenig & Heisey (2001)**, "The Abuse of Power..." — 如保留 post-hoc power analysis [R1]
3. **更多 grammar-constrained decoding 文献** — 论文仅引用 Outlines (Willard & Louf 2023)，但讨论了 constrained decoding 作为 CWM 改善方向 [R1, R2]
4. **Chain-of-thought code verification** — PatchReasoner 已引用但仅一笔带过；CoT 作为 CLS-CWM 中间地带值得更深入讨论 [R2]

---

## 外部审稿 (Stanford Agentic Reviewer)

**状态：未配置**（`external_review.paperreview_ai.enabled` 未设置）。跳过。

---

## Overall Assessment

### 评分: **3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 3/5 | **3.0/5** |
| Excitement | 3/5 | 3/5 | **3.0/5** |
| Reproducibility | 3/5 | 3/5 | **3.0/5** |
| Confidence | 4/5 | 4/5 | **4/5** |

### 综合判断

论文填补了一个确实存在的文献空白（matched formulation comparison），function-level 方法论严谨且结论可信。但以下因素共同将论文定位在 Findings 而非 Conference 水平：

1. **格式硬伤**：正文超 8 页限制 ~3 页，提交前必须修复，否则 desk reject。
2. **方法论不对称**：论文最有价值的发现（repo-level divergence）恰好依赖最薄弱的证据基础（单种子、多重 confound、CWM baseline 规模限制）。Function-level equivalence（最 robust 的结论）在直觉上 somewhat expected。
3. **新颖性有限**：无新方法提出；核心发现（分类在长输出场景优于生成）从 autoregressive error compounding 原理可预期；"design space" 仅 3 个离散点。
4. **Generalizable insight 不足**：所有 repo-level 结论 conditioned on ≤8B LoRA regime，CWM baseline 与原始 32B CWM 本质不同。论文对此足够诚实，但 conditioned 的结论天然限制了 impact。

**积极因素**：透明度罕见（Threats to Validity 自省式暴露 5 个 confounds）；failure mode taxonomy 和 error complementarity 有实操价值；统计方法论在 function-level 达到高标准。论文是一篇 solid empirical study，适合 Findings。

### 对 Research Director 的信号

- **W1（页数超限）** 和 **W9（Abstract 数字密度）** 是纯写作/格式问题，不涉及新实验，可在截止日期前修复。
- **W2（TRAJ checkpoint）** 和 **W3（Table 4 混合粒度）** 需要重新组织呈现方式，工作量中等。
- **W5（repo-level 单种子）** 需要新实验（如可行）或措辞降级。
- 其余 should-fix 项多为措辞和呈现优化。

---

## Detailed Comments（逐节）

### Abstract
- 数字密度过高（跨 3 轮反复指出），需大幅精简。保留 function-level equivalence 和 repo-level 19-26pp gap，删减 p 值、oracle accuracy、具体百分比组。
- "motivating complexity-aware routing over uniform formulation selection" 是 trailing -ing phrase（M6）。
- "pp" 首次出现未定义（M1）。

### Introduction
- 问题定义和 gap identification 清晰有效。
- Contribution list 过长（~350 words），具体数字应移至 Results。第二条 contribution 单条 ~120 words。
- "The results reveal a three-layer structure" 概括有力，但后续展开过于详细。
- 每条 contribution 有对应 section/table 支撑。Contribution 2 的 hedging（"Evidence for...with identified confounds"）诚实。
- Contribution 3（error complementarity）仅基于 function-level 单 seed，claim weight 与 evidence 不对称。

### Method
- Formulation 定义清晰，notation 一致。
- §3.2 failure mode 先验分析是亮点——为后续实验提供了 testable predictions，大部分被验证。
- §3.3 oracle framework 使用 function-level ICC (0.191) 估算 repo-level oracle advantage 是 conservative 的，论文正确标注。

### Experiments
- **过长**（占全文 5-6 页），是超页数的主因。
- §4.1 Setup: 数据集描述清楚，split 和 baseline 完整。"zero problem overlap" 是正面设计。Holm-Bonferroni 在 Statistics 段提及。
- §4.2 Function-level: 最 solid 的部分。5-seed、两个模型家族、appropriate statistical tests。
- §4.3 Scaling: 仅 2 seeds (bf16 only)。CWM flat scaling 的 hedging 合理。
- §4.4 TOST: 统计方法本身正确。Sensitivity table 在 Appendix。但 SESOI 框架引用缺失。
- §4.5 Repo-level: 最大 confound 集中区。Default assignment artifact 分析是亮点。Constrained decoding 段和 Training/evaluation sensitivity 段可移入 Appendix。
- §4.6 Analysis: Aggregation penalty 分析深入。Checkpoint selection confound 是重要观察。
- §5 Threats: 全面诚实，缺 compound effect 讨论。
- TRAJ checkpoint 不一致（W2）需修复。

### Related Work
- 第一段需从 enumeration 重写为 synthesis。PRM/ORM 类比（第二段）处理得当。
- 引用量充分（58 篇），近期工作补充基本到位。缺 constrained decoding 更广文献和 CoT verification 深入讨论。

### Conclusion
- 简洁有效，practical recommendations 有实用价值。
- 措辞审慎（"under standard LoRA fine-tuning (≤8B)"）。

### Limitations
- 独立 \section*，符合 ARR 要求。内容诚实全面。

### Checklist
- 认真填写。C4 "Partially" 需补全 version numbers。

### Appendix
- 内容丰富且与正文交叉引用完整。
- Variant-level accuracy table (Table 6) 是理解 Table 4 的必要补充，建议在正文中更突出引用。
- Holm-Bonferroni (Appendix K) 是方法论亮点。
- 部分正文内容（Threats to Validity, sensitivity details）应移入以解决超页。

---

## 与历史 Issue Tracker 对比

### Round 4 → Round 5 进展
- **已解决 (6 项)**: R4-W3 (cross-model wording → 'consistency check')、R4-W5 (多重比较 → Holm-Bonferroni 完成)、R4-W8 (遗漏 CodePRM/FunPRM → 已引用)、R4-M2 (default-to-pass 讨论 → §4.5 完成)、R4-M6 (stagnation → flat scaling)、R3-W1 (Limitations section → 独立 section)
- **部分改善 (5 项)**: R4-N1 (TOST sensitivity → table 完成但需 SESOI 框架)、R4-N2 (Controlled → Systematic title)、R4-N3 (power analysis → 完成但方法论需改善)、R4-W1 (CWM conditioning → Conclusion/Threats 有但 Abstract 缺)、R4-W7 (oracle scope → function-level 限定已加)
- **未解决 (2 项)**: R4-W2/R3-W2 (Abstract 数字密度 → 跨 3 轮未解决)、R4-W4 (novelty positioning)
- **新增 (7 项)**: R5-N1 (页数超限)、R5-N2 (TRAJ checkpoint)、R5-N3 (Table 4 混合粒度)、R5-W4 (confound 累积)、R5-W5 (post-hoc power)、R5-W8 (Related Work 枚举)、R5-W11 (贡献列表过长)