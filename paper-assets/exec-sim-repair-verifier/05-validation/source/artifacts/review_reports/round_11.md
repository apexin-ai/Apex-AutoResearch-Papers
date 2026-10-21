---
round: 11
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-23T12:56:38.274376+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# Round 13 审稿报告（Fresh Review）

**投稿**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 (ARR May cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性/贡献+完整性）
**轮次**: Round 13 (Fresh Review)，1 轮独立审稿 + 1 轮交叉分享

---

## Summary

本文首次在匹配条件下系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别和多个 seeds。核心发现为三层结构：(1) fine-tuning 必要（35-36pp 增益）；(2) function-level 三种公式近等价（CLS-CWM TOST 确认，CLS-TRAJ Holm 校正后未确认但 gap 单调收窄至 1.07pp@14B）；(3) repo-level 在 ≤8B LoRA 下等价崩塌（CLS-CWM gap 18-26pp，由 CWM format collapse 驱动）。论文同时提供了 failure mode taxonomy 和 error complementarity 分析。

---

## Strengths

**S1. 首个匹配条件的系统比较。** 控制模型容量、训练数据、超参数和评估协议进行三方公式比较，直接回答从业者的 formulation 选择问题。Cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 差异方向一致）增强结论可信度。[两人共识]

**S2. 统计框架出色。** TOST 等价检验 + Bayesian ROPE 双验证、clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 校正（k=5）、ICC/DEFF 修正——在 NLP 实证论文中属上乘水准。特别是 §3.4 明确区分"等价"与"未能拒绝差异"，CLS-CWM 等价在多个统计方法下一致（TOST p=0.007; P(ROPE)=0.975）。[两人共识, R1 Soundness 3.5, R2 Soundness 4.0]

**S3. 透明的混淆因素分析。** §3.7 和 Appendix O 明确列出并量化 5 个 confounds，包括 preprocessing-checkpoint 链式影响（7.68pp）和 worst-case compounding 分析（±11.5pp）。CLS-TRAJ 等价在 Holm 校正后不成立也被如实报告。[两人共识]

**S4. 实用的 failure mode taxonomy。** Table 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）提供可迁移的诊断框架，对实践者有直接价值。R1 认为此贡献可独立于三方比较使用。[两人共识]

**S5. GenRM 领域特异性观察。** 代码验证中 generation ≤ discrimination（与 GenRM 在数学推理中的发现相反）是一个有价值的数据点，暗示 generation advantage 可能是 domain-dependent 的。[两人共识, 但均认为分析不够深入]

**S6. Related Work 覆盖充分。** CodeScaler, Aletheia, GenRM, GenPRM, FunPRM, CodeRM 均已引用。两位 Reviewer 均未发现 2025-2026 年的重大遗漏。[两人共识]

---

## Weaknesses

### Must-Fix（1 项）

**N1. [critical] [consensus] Appendix "P: Limitations" 标题可能违反 EMNLP 格式规则。**
- EMNLP 2026 / ARR 规定"一篇文章只能有一个 limitations section，放在正文里面，appendix 不能有 limitations section"。Appendix 概览明确列出 "P: Limitations"，构成形式违规。
- **建议**：重命名为 "Extended Experimental Details" 或 "Additional Confound Analysis"，从 Appendix 概览中移除 "Limitations" 标签。
- **R1 提出, R2 完全 AGREE。**

### Should-Fix（4 项）

**W1. [warning] [consensus] Abstract/Conclusion 中 TRAJ "not confirmed" 措辞在 power ~0.3 下 over-stated。**
- Abstract "TRAJ parity is not confirmed after multiple comparison correction at any scale tested" 在 power ~0.3 下可能让读者误解为存在差异的证据，而实际是检验力不足以检测等价（absence of evidence ≠ evidence of absence）。
- 14B 结果（三公式收敛至 1.07pp 以内）应给予更突出位置以平衡消极暗示。
- **R1 标 Must-Fix, R2 认为 Should-Fix（§3.4 已诚实报告 power）。Director 裁定 Should-Fix：方法论无缺陷，问题仅在措辞精度。**
- **建议**：Abstract 加 power 限定语；Conclusion 讨论达到 power ≥0.8 所需 seed 数。

**W2. [warning] [consensus] 核心发现可从论文自身 §2.2 理论预测，新颖性受限。**
- §2.2 预测短输出→等价、长输出→格式崩溃，两个核心结论均被自身理论预测。实证贡献降格为"验证"而非"发现"，直接限制 Excitement。
- R1 补充：quantitative boundary conditions（14B 收敛速度、failure mode 跨模型一致性）超越纯理论预测。
- **R2 标 Must-Fix, R1 AGREE（但认为有 nuance）。Director 裁定 Should-Fix：这是 inherent limitation（贡献类型为 empirical comparison），无法通过修改消除，但可通过 framing 改善——深入分析理论预测失败之处。**
- **建议**：(a) 诚实重新定位为"首次严格实证验证"；(b) 深入刻画理论预测未覆盖的边界条件。

**W3. [warning] [consensus] TRAJ 比较被训练配置严重混淆。**
- TRAJ 使用 ~400 训练实例 vs CLS/CWM ~70K；不同 lr；variant-level labels vs per-test。Downsample ablation 控制了数据量但未控制 label granularity（formulation-inherent confound）。
- §3.5 已有 "exploratory" 标注和 confound 讨论，但主文 Tables 1-3 仍将三公式并列呈现无视觉区分。
- **R2 标 Must-Fix, R1 AGREE (W1)。Director 裁定 Should-Fix：§3.5 已有充分 disclosure，但 Tables 中应添加视觉标注。**
- **建议**：Tables 1-3 为 TRAJ 行添加 † 标记 + 脚注说明训练配置差异。

**W4. [warning] [consensus] GenRM 领域特异性对比（代码中 generation ≤ discrimination vs 数学中 generation > discrimination）分析不充分。**
- §5 Conclusion 仅 1 句话讨论。论文已有支撑数据（parseable rate 差异、output token count、format compliance rate）可用于分析 WHY 领域差异存在。
- 增加 1-2 段分析可同时提升 Excitement（回应 W2 的 confirmation vs discovery 批评）。
- **R2 提出, R1 AGREE。**

### Minor（3 项）

**M1. [info]** Oracle 互补性（Contribution 2）应更明确框定为 negative result + motivation。Simple routing 仅捕获 <0.4pp 的 oracle 优势，当前不可操作。R1 认为作为 negative result 有独立价值（排除了简单方法），R2 认为 contribution 权重应降低。

**M2. [info]** PRM/ORM 映射命名反直觉——"CLS→PRM-like" 和 "TRAJ→ORM-like" 基于 per-test vs per-patch 粒度是正确的，但 "classification" 听起来像 ORM。建议加一句显式澄清。

**M3. [info]** Abstract 统计符号密度偏高（z=−23.7, TOST, pp 值），建议先陈述定性洞见再给统计支撑。考虑将部分数值移入正文。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：
- [AGREE] Appendix "P: Limitations" 格式违规需修复 (N1)
- [AGREE] TRAJ 训练配置混淆是论文的系统性弱点 (W3)
- [AGREE] GenRM 领域对比分析不充分 (W4)
- [AGREE] 14B 结论应降级为 preliminary observation
- [AGREE] PRM/ORM 映射需显式澄清 (M2)
- [AGREE] Overall 3.0 (Findings), Excitement 3/5
- [AGREE] Related Work 覆盖充分，无重大遗漏
- [AGREE] 统计框架在 NLP 实证论文中属上乘水准
- [AGREE] Failure mode taxonomy 有独立实践价值

## Reviewer Divergence [REBUT]

以下问题存在分歧，Director 已裁定：

| 问题 | R1 | R2 | Director 裁定 |
|------|----|----|--------------|
| R1-N1 severity（TRAJ power over-statement）| Must-Fix | Should-Fix | **Should-Fix**：§3.4 已诚实报告，问题仅在措辞 |
| R2-W3 页数溢出 | 不同意（PDF+LaTeX 证据显示未超页）| Should-Fix | **降级 Minor**：R1 提供 LaTeX+PDF 证据，Limitations 不计页 |
| R2-W2 互补性贡献 | 作为 negative result 有价值 | 可能误导 | **Minor**：应框定为 negative result |
| R2-M4 贡献独立性 | Taxonomy 可独立使用 | 应合并 | **Minor**：R1 论证 Table 4 可迁移 |
| Soundness 评分 | 3.5/5 | 4.0/5 | **3.5**：CLS-CWM 可靠但 TRAJ/CWM 两翼均有 confounds |

---

## Questions（需要作者澄清）

**Q1.** ±2pp SESOI 是在看到数据之前还是之后确定的？如果是后者，请讨论对 TOST 结论的影响。[R1-Q1, R2 AGREE]

**Q2.** 在当前实验设计下，需要多少 seeds 才能使 CLS-TRAJ 比较达到 power ≥0.8？[R1-Q2]

**Q3.** CLS-CWM 使用 seed-level paired analysis 而 CLS-TRAJ 使用 clustered bootstrap，两个比较使用不同统计方法是否引入方法论不对称性？[R1-Q3]

**Q4.** 代码验证中 generation ≤ discrimination（与 GenRM 数学结论相反）的具体原因是什么？是 output token 数量、结构化格式要求、还是其他因素？[R2-Q3, R1 AGREE]

**Q5.** 14B 实验能否用另一模型家族进行 cross-family 复制？[R2-Q5, R1 AGREE (M4)]

---

## Missing References

两位 Reviewer 均未发现重大遗漏。CodeScaler, Aletheia, GenRM, GenPRM, FunPRM, CodeRM, SolidCoder 等 2025-2026 关键工作均已引用。PRM/ORM 映射（CLS→PRM-like, TRAJ→ORM-like, CWM→generative verifier）在粒度维度上准确。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 13 info）：

**Warnings:**
- pp.1-2 连续两页纯文本无 display item，Figure 1 直到 p.3 才出现。审稿人前 2 页无视觉锚定。
- p.8 整页纯文本（Related Work + Conclusion），pp.7-8 区域视觉单调。

**Info (选摘):**
- Figure 1 概念图清晰，caption 自包含（p.3）
- Tables 1-4 使用 booktabs 风格，格式规范
- Figure 2 右栏放置，tick labels 偏小但可辨读（建议 ≥9pt）
- References 格式统一，无 [?] 未解析引用
- Limitations 段落约 5 行，覆盖 3 个限制点，符合 EMNLP 规范
- 最末页 appendix 约 1/4 内容，大面积空白（不影响）

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 4/5 | **3.5/5** |
| Excitement | 3/5 | 3/5 | **3/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.0 | 3.0 | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | **4/5** |

**Overall Assessment: 3.0 — Findings**

**核心判断**：本文是一篇方法论严谨的实证比较研究，统计分析水准在 NLP 实证论文中处于上游。CLS-CWM function-level 等价这一核心发现在多个统计方法下一致确认，可信度高。Failure mode taxonomy 提供了独立的实践价值。

但三方比较中 TRAJ 一翼受训练配置混淆削弱（~400 vs ~70K 实例、label granularity 差异无法消除），CWM 一翼受生态效度限制（≤8B LoRA vs 原始 32B），使得论文实际只有 CLS-CWM function-level 等价这一个完全可靠的新发现。核心结论可从论文自身 §2.2 理论分析预测，属 confirmation 而非 discovery，限制了 Excitement。14B 收敛结果有前瞻价值但证据不足（1 family, 3 seeds, borderline p-value）。

修复 N1（Appendix 格式违规）后，论文适合 Findings 发表。若能深入展开 GenRM 领域特异性分析（W4）并改善 TRAJ 比较的 framing（W3），可提升至 3.5 (Borderline Conference)。

---

## Detailed Comments

### §1 Introduction
- Contribution 2（error complementarity）应重新框定为 negative result：simple routing 仅捕获 <0.4pp，互补性存在但当前不可操作。
- Contribution 3（failure mode taxonomy）独立性成立（R1 论证可迁移），保持。
- "formulation choice is moderated by code complexity" 已有 ≤8B qualifier，措辞恰当。

### §2.2 Expected Failure Modes
- 理论分析预测了两个核心方向（function equiv + repo divergence），使实证发现的 surprise value 降低。可考虑重新定位为 "empirical validation with boundary characterization"。

### §3.1 Experimental Setup
- TRAJ 训练配置差异（~400 vs ~70K, 不同 lr, variant-level labels）在此处仅简略提及。Tables 1-3 应添加 † 标注。

### §3.4 Equivalence
- Power ~0.3 的讨论充分（§3.4 末段），但 Abstract 和 Conclusion 的 "not confirmed" 措辞未反映此限制。
- SESOI ±2pp 已标注 "not pre-registered"，sensitivity analysis 报告 ±1.52pp 临界值，处理恰当。

### §3.5 Repo-Level
- "exploratory due to limited seed coverage" 标注良好。
- Variant-level 分析使用描述性语言，避免 causal claims，处理得当。

### §4 Related Work
- PRM/ORM 映射（CLS→PRM-like, TRAJ→ORM-like）粒度维度正确，但命名反直觉。建议加一句显式澄清。
- GenRM 对比仅一句话，应扩展。

### §5 Conclusion
- GenRM domain-specificity 段落存在但过于简短。应分析 WHY（output structure, format compliance, error type）。
- 14B 结论应加更强 hedging。

### Limitations
- 简短充分（~5 行，3 点），符合 EMNLP 规范。

### Appendix
- "P: Limitations" 标题违反 EMNLP 格式规则，需重命名。[Must-Fix]
- 16 个 Appendix (A-P, ~15 pages) vs 8 页正文。量大但内容必要（equivalence testing 的 sensitivity/robustness 要求）。
