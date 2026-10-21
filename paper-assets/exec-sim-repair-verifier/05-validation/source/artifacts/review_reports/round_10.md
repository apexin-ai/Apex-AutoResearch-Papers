---
round: 10
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T09:20:18.448909+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 12 (Fresh Review)

**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 via ACL ARR
**审稿模式**: Fresh（无前轮记忆）
**Reviewer 编排**: R1（方法严谨性 + 实验设计 + 统计分析）+ R2（新颖性 + 相关工作 + 写作 + 格式）

---

## Summary

本文系统比较了三种 execution-free 代码修复验证 formulation：CLS（per-test 二分类）、CWM（执行输出生成）和 TRAJ（trajectory-level patch 评分），在两个代码 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度级别、多 seed 下使用 ≤8B LoRA fine-tuning 进行匹配实验。核心发现：(1) function-level 下 CLS-CWM 统计等价（TOST p=0.007, 5 seeds, Bayesian ROPE P=0.975）；(2) repo-level 下 CWM 因 format collapse 退化 18-26pp（z=-23.7, DeepSeek-Coder）；(3) 14B 时 function-level gap 收窄至 0.43pp（TOST p=0.0006），一致于 capacity-dependent convergence；(4) error complementarity 和 failure mode taxonomy 为实践选择提供指导。

---

## Strengths

**S1. 统计方法论远超同领域论文一般水准。** TOST 等价性检验 + Holm-Bonferroni 校正 + clustered bootstrap（114 clusters, 10K resamples）+ mixed-effects LPM/GEE 双模型验证 + Bayesian ROPE 分析——这套统计工具箱的部署深度和一致性为 NLP 实证研究设立了方法论标杆。[R1, R2 一致]

**S2. Threats to validity 分析异常详尽和诚实。** §3.7 和 Appendix N 系统识别了五个潜在 confound（checkpoint, sequence length, preprocessing, TRAJ regime, CWM scale）并逐一评估，自我批评程度超过多数投稿论文。论文对自身局限性的坦诚值得肯定。[R1, R2 一致]

**S3. Failure mode taxonomy 有独立实用价值。** Table 4 的三类故障模式（format collapse / decision collapse / aggregation penalty）为从业者提供了可操作的诊断框架，在给定模型和 formulation 下预测可能的失败模式。[R1, R2 一致]

**S4. 实验设计在 ≤8B LoRA 范围内实现了高匹配度。** 控制了模型容量、训练数据、LoRA 配置、compute 等变量，在其约束范围内确实实现了 matched comparison。Hyperparameters 完整报告（Table 11），compute budget 明确（~370 GPU-hours），prompt templates 提供。[R1]

**S5. Comprehensive ablation program。** LoRA rank, majority voting, sequence length, data size, preprocessing, few-shot, checkpoint 的系统消融，使 repo-level 结论有更强的因果推断基础（四项干预全部失败排除了多个替代解释）。[R1]

---

## Weaknesses

### Must-Fix（共识 Critical）

**C1. CWM baseline 生态效度——核心方法论 confound [R1-N1, R2-N2, 双方 AGREE]**

论文标题声称比较"verification formulations"，但 repo-level 核心发现（CWM 退化 18-26pp）完全建立在 ≤8B LoRA fine-tuning 之上。CWM 需生成 ~477 tokens/instance vs CLS 仅 1 token；在小模型无 execution-trace pretraining 条件下，长文本生成退化是已知现象。14B function-level gap 收敛至 0.43pp（TOST p=0.0006）反而支持"capacity drives the gap"假设。论文虽在 Abstract 提到"under our ≤8B LoRA protocol"、§3.7 和 Appendix N 有详细讨论，但 Introduction §1 contribution (2) "formulation choice is moderated by code complexity" 读起来像一般性结论，未加 regime 限定。

Appendix I(c) 的意外训练证据进一步加深了这一质疑：CWM 模型误训在 CLS 格式数据上后达到 86.05% accuracy + 0% unparseable——表明退化来自 trace generation 复杂度而非 verification task 本身。

**必须修改**：(a) Title 和 Introduction contribution 中明确限定"under ≤8B LoRA fine-tuning"；(b) 如有可能，增加 14B CWM repo-level 数据点以验证 gap 是否随 capacity 缩小——这将直接决定核心结论的定性方向。

**C2. Qwen3 CWM optimal checkpoint 未评估——论文持有关键数据但未报告 [R1-N2, R2 AGREE]**

Table 16（Appendix L）显示 Qwen3-8B CWM eval loss 在 step 300-400 达到最小值（~0.29），final epoch（step 6600）膨胀至 ~0.52（1.8×）。论文确认 Qwen3 有 step 300/400 checkpoints 但**未报告其 repo-level accuracy**。DeepSeek 的 early-stopping 数据显示 +18.14pp improvement（75.45% vs 57.31%），暗示 Qwen3 optimal checkpoint 可能显著缩小 gap。

R2 补充了重要 nuance：即使 early-stopped DeepSeek CWM 达到 75.45%，仍低于 CLS (82-85%)，且保持 66.4% unparseable rate——format collapse 在训练早期已存在，过拟合加剧但非唯一原因。缩小后的 gap (~10pp) 仍然 non-trivial，但显著改变了 gap 的解释。

**必须修改**：评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 和 unparseable rate，并在正文中报告。

**C3. 统计功效不足导致 CLS-TRAJ 等价性结论不可靠 [R1-N3, R2 AGREE]**

n_eff ≈ 86, TOST power ~0.3。CLS-CWM 等价性确认（TOST p=0.007, P(ROPE)=0.975）与 CLS-TRAJ 未确认（adjusted p=0.075, P(ROPE)=0.542 per-test）的不对称结论可能完全是 power 不足的 artifact——在 power ~0.3 下，Type II error 概率达 70%。论文在贡献声明中将"TRAJ equivalence is not confirmed after multiple comparison correction"与"CLS-CWM equivalence"并列，读者可能误解为"CLS-TRAJ 不等价"。

R2 补充：Bayesian ROPE 在 variant-level 给出 P(ROPE)=0.970（支持等价），但 per-test level 为 0.542（inconclusive）。两个 analysis level 的不一致未在正文中讨论。

**必须修改**：(a) 正文更明确讨论 power ~0.3 意味着"未确认"不等于"非等价"；(b) 讨论 variant-level vs per-test ROPE 的不一致及其原因；(c) 避免在 contribution list 中将 TRAJ model-contingent 作为稳健结论呈现。

### Should-Fix

**W1. 贡献列表仅两条，failure mode taxonomy 未列为贡献 [R2-W2, R1 AGREE]**
Table 4 的 taxonomy（format collapse / decision collapse / aggregation penalty）是论文最具实用价值的输出之一。应增加为第三条贡献。

**W2. GenRM 对比发现未被充分讨论 [R2-W3, R1 AGREE]**
Hosseini et al. (ICLR 2025) 发现 generation-based verifier 在数学推理中优于 classification-based。本文发现在代码验证中相反。这一对比是论文最有潜力成为 surprising finding 的地方，但仅在 §4 Related Work 一段讨论。应提升到 Discussion/Conclusion 级别。

**W3. SESOI ±2pp 无 pre-registration，结论对 SESOI 选择敏感 [R1-W1, R2 AGREE]**
±1.52pp 临界值距 ±2pp 仅 0.48pp。如果 SESOI 设为 ±1.5pp，CLS-CWM 等价性就不确认。建议在正文引用 Appendix G sensitivity analysis 并承认 SESOI 的主观性。

**W4. CLS-TRAJ 训练条件根本不匹配（~400 vs ~70K, label granularity 差异）[R1-W4, R2 AGREE]**
Downsample ablation 控制了 data volume 但未控制 label granularity（per-test vs variant-level）。CLS vs TRAJ repo-level 比较本质上是 exploratory 而非 confirmatory。

**W5. Repo-level 数据处理不一致（drop vs truncate + checkpoint confound chain）[R1-W3, R2 AGREE]**
DeepSeek CLS accuracy 从 82.61% (drop) 到 74.93% (truncate) 有 7.68pp 偏差，truncate → NaN val loss → final epoch default 形成 confound chain。应在正文更显著呈现。

**W6. CLS-CWM paired comparison 使用不同 seeds（CLS s123 vs CWM s42）[R1-W5, R2 AGREE]**
Function-level seed noise (<2pp) 不能直接外推到 repo-level（DeepSeek CLS ±2.50 std）。

**W7. 种子数/实验配置不一致导致统计置信度参差不齐 [R2-W5, R1 AGREE]**
不同比较使用 1-5 seeds，统计可靠性差异大但未系统标注。

### Minor

- M1: §2.2 Failure Modes 位于 method section 造成结构困惑（R2 提出, R1 AGREE）
- M2: Appendix G' prime 符号命名不直观（R2 提出, R1 AGREE）
- M3: `wei2022emergent` 引用类型不一致（R2）
- M4: Figure 2 float 漂移 2-3 页（视觉审查）

---

## Reviewer Consensus [AGREE]

1. **CWM baseline 公平性是核心问题**：两位 reviewer 独立提出，交叉分享后双方完全 AGREE。≤8B LoRA 对 CWM 系统性不公平，repo-level 核心发现可能是 capacity artifact 而非 formulation 差异。
2. **Qwen3 CWM optimal checkpoint 未评估是重大遗漏**：R1 提出，R2 完全 AGREE。论文持有 step 300-400 checkpoints 但未报告 accuracy。
3. **统计功效不足限制了 CLS-TRAJ 结论**：R1 提出，R2 AGREE。Power ~0.3 下"未确认等价"不应被呈现为"model-contingent"。
4. **Failure mode taxonomy 应提升为贡献**：R2 提出，R1 完全 AGREE。
5. **GenRM 对比应更深入讨论**：R2 提出，R1 AGREE。
6. **统计方法论是突出优势**：双方一致肯定。
7. **Threats to validity 讨论诚实详尽**：双方一致肯定。

---

## Reviewer Divergence [REBUT]

1. **Excitement/Novelty（核心分歧）**：
   - R2 (Excitement 2/5)："核心发现可从第一性原理预期，§2.2 理论分析就预测了实验结果"
   - R1 (Excitement 3/5)："'可预期'不等于'无价值'，引用 ARR H1 条款；gap magnitude 和四项干预失败不可预期"
   - **Director 判断**：R2 的关切更有说服力。论文的理论分析（§2.2）确实预测了实验结果的方向——function-level 等价和 repo-level 发散。虽然 magnitude 不可预期（R1 的论点），但 magnitude 的精确量化在 CWM baseline 公平性存疑的情况下（C1, C2）价值受限。R1 引用 ARR H1 是合理的，但 H1 旨在防止对 well-designed experiments confirming non-obvious hypotheses 的不公平驳回——本文的假设从自身理论框架看并非 non-obvious。

2. **Abstract 统计密度**：
   - R2："统计细节过密降低可读性"
   - R1："方法论论文需要在 Abstract 包含关键统计结果"
   - **Director 判断**：R1 的立场更合理。对于以统计方法论为核心卖点的论文，Abstract 中保留关键 p-value 和 effect size 是必要的。但可考虑精简至 2-3 个最关键数字。

3. **两个模型家族是否足够**：
   - R2："泛化性受限"
   - R1："ARR H4 不鼓励要求不必要的额外实验"
   - **Director 判断**：R1 的论点更有说服力。两个家族作为 primary + consistency check 是合理的实验经济性选择。降级为 Limitations 中提及即可。

---

## Questions

1. Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 是多少？
2. 是否有 14B CWM 的 repo-level 数据？如有，gap 是否随 capacity 缩小？
3. ±2pp SESOI 是否 pre-registered？如否，应在正文明确说明。
4. NF4 quantization 对 CWM 长文本生成质量的具体影响是什么？
5. CLS-TRAJ 等价性确认所需的最小样本量是多少（a priori power analysis）？

---

## Missing References

- **Equivalence testing 在 NLP 中的应用先例**（如有）：会加强 TOST 方法选择的 motivation [R1]
- **CVeDRL (arXiv:2601.22803, 2026)**：R2 提出但 R1 对其存在性和相关性存疑（difficulty-aware RL training 与本文 formulation comparison 主题有一定距离）

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

状态：✅ 完成（1 warning, 12 info）

**Warning**:
- Figure 2 首次引用在 page 4-5，但实际出现在 page 7 右栏（float 漂移 2-3 页）。建议调整 float 位置参数。

**Info highlights**:
- Figure 1 概念图清晰专业，三种 formulation 对比一目了然
- Tables 1-4 均使用 booktabs 风格，格式规范
- Figure 2 使用色盲友好双色方案，y-axis 非零起始已在 caption 标注
- 正文在第 8 页结束，Limitations 为简短一段覆盖 3 个要点，符合 EMNLP 规范
- Appendix 12 页（p12-22），表格密度高但作为 appendix 可接受
- 无 [?] 未解析引用

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**置信度: 4/5**

**评分理由**：

论文在方法论严谨性方面达到了 NLP 实证研究的高标准（S1, S2），failure mode taxonomy 有独立实用价值（S3），在 ≤8B LoRA 范围内的实验设计匹配度高（S4）。

但三个核心问题限制了论文达到 Conference 水平：

1. **CWM baseline 公平性（C1）**——这是最严重的问题。如果 repo-level 的 18-26pp gap 主要由 model capacity 而非 formulation 差异驱动（14B function-level 收敛至 0.43pp 提供了强间接证据），则论文的中心 claim（"complexity-moderated formulation choice"）的通用性大幅受限。论文需要在 Introduction 的贡献声明中更显著地限定这一点。

2. **CWM checkpoint 遗漏（C2）**——论文持有 optimal checkpoint 但未报告其 accuracy，DeepSeek 的 early-stopping 数据暗示 gap 可能缩小约 18pp。这是一个可以执行但未执行的关键实验。

3. **Novelty ceiling（R6-N4 系列）**——核心发现（function-level 等价 + repo-level 发散）可从论文自身的 §2.2 理论分析直接预期。虽然统计严谨的量化验证有价值，但在核心 claim 受 C1 和 C2 质疑的情况下，magnitude 的精确量化也失去了部分说服力。R1 (3.5, Borderline Conference) 和 R2 (3.0, Findings) 的评分差异主要反映对 novelty 的不同判断。

**如果作者在 rebuttal 中能提供**：(a) Qwen3 CWM optimal checkpoint 的 repo-level accuracy，(b) 14B CWM repo-level 数据点——**评分可能上调至 3.5**。目前，Findings 是合适的定位。

---

## Detailed Comments

### §1 Introduction
- Contribution (2) "formulation choice is moderated by code complexity" 缺少 ≤8B LoRA 限定。这是核心 claim，应在首次出现时就明确限定条件。
- 仅列出两条贡献。Failure mode taxonomy（Table 4）应作为第三条。
- "primarily methodological" 的自我定位虽诚实但策略上不利——建议重新框定为揭示了 generation advantage 的 domain-specificity。

### §2 Method
- §2.2 Failure Modes 更适合放在 §3 Experiments 中，与 Table 4 的实证 taxonomy 相邻。当前位置在 Method section 会让读者误以为是方法设计而非理论预测。
- Oracle Accuracy-Utility Framework（§2.3）的 ICC 参数来自 function-level 分析，在 repo-level 应用时存在 domain mismatch（repo-level ICC=0.3146 vs function-level ICC=0.191）。

### §3 Experiments
- Table 1: 信息密度高但缺少视觉分隔（primary results / cross-model / baselines 之间）。
- §3.2 Scaling: "At 8B, the ranking is CLS > TRAJ > CWM"——这三个数字基于 2 seeds，排名的统计置信度有限。
- §3.4 Equivalence: TOST sensitivity analysis 结果（±1.52pp 临界值）应在正文中引用和讨论，而非仅放在 Appendix G。
- §3.4 Statistical power 段落已有（good），但应更明确说明 power ~0.3 意味着 CLS-TRAJ 的 non-confirmation 是 inconclusive 而非 negative。
- §3.5 Repo-Level: CWM convergence analysis 确认了 systematic overfitting，但 Qwen3 optimal checkpoint 的 accuracy 是关键缺失数据。
- §3.6 Analysis: Oracle combination 基于 single-seed，应更醒目标注。
- §3.7 Threats: preprocessing-checkpoint confound chain 应更显著呈现。

### §4 Related Work
- GenRM 对比发现（generation advantage 在代码领域失效）是论文最有潜力的 insight，但埋在 Related Work 中。应提升至 Discussion 级别。
- 三段式组织（Execution Simulation / Process vs Outcome / Repair & Task Framing）清晰合理。
- 引用真实性抽查通过，未发现幻觉引用。

### §5 Conclusion
- "Primary statistical findings are established under ≤8B LoRA fine-tuning" 是正确且必要的限定。
- Future direction (2) "capacity scaling or execution trace pretraining" 实际上是论文的 primary open question——考虑在 Conclusion 中更显著地承认这一点动摇了当前结论的通用性。

### Limitations
- 覆盖 4 个要点（model family, ≤8B, Python-only, synthetic mutations），简短合规。
- "synthetic-to-real transfer gap remains untested" 是重要限制，已提及。

### Appendix
- 14 个 appendix section（A-P），含 mini TOC（good）。
- Appendix G' 的 prime 符号应改为 G.2。
- Appendix P "Extended limitations" 不构成格式违规（R1 REBUT 合理），但内容实质上扩展了正文 Limitations，存在被审稿人质疑的风险。
- `wei2022emergent` 引用类型应为 article（TMLR）而非 inproceedings。
