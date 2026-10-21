---
round: 13
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-23T14:44:59.963888+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# Round 15 Consolidated Review Report

**Paper**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 (ARR May cycle)
**Reviewers**: R1 (方法与实验严谨性), R2 (新颖性与完整性)
**Cross-sharing**: 完成，双方逐条回应

---

## Summary

本文系统比较了三种 execution-free 验证公式（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分）在代码修复验证任务上的表现。在 function-level，CLS 和 CWM 统计等价（TOST p=0.007, 5 seeds）；在 repo-level（≤8B LoRA），CWM 出现 18–26pp 的性能下降（z=−23.7），>50% 输出不可解析。初步 14B 结果（3 seeds, 单一模型族）将所有公式差距缩小至 1.07pp 以内。论文提出 complexity-moderated formulation choice 作为核心 contribution，并提供 failure mode taxonomy。

---

## Strengths

**S1. 实验设计严谨，统计方法全面 [共识]**
TOST 等价检验 + Bayesian ROPE + 聚类 bootstrap + Holm-Bonferroni 校正 + mixed-effects 回归，构成多层统计验证。5 seeds 复现，ICC 报告，seed variance 分析完整。这在 NLP/SE 交叉领域论文中属于上乘水平。

**S2. 研究问题有明确实践价值 [共识]**
Execution-free verification 是 APR pipeline 的实际瓶颈，比较不同公式的选择对 practitioner 有直接指导意义。

**S3. Failure mode taxonomy 提供诊断价值 [共识]**
对 CWM 的 format collapse（53–74% unparseable at repo-level）进行了系统归因，包括 truncation、delimiter errors、hallucinated outputs，超越了简单的 accuracy 比较。

**S4. 写作质量较高 [共识]**
论文结构清晰，statistical claims 有适当 qualifier（如 "preliminary"、"exploratory"），threats to validity 部分诚实全面。Abstract 控制在 200 words 以内。

**S5. 开源承诺 [R1]**
承诺公开代码和数据，有利于可复现性。

---

## Weaknesses

### 重大问题 (Major)

**W1. 规模限制削弱核心 claim 的普适性 [共识，严重程度有分歧]**
≤8B LoRA 是唯一完整复现的设置；14B 仅限 Qwen3 单一模型族、3 seeds。核心发现"CLS ≈ CWM at function-level, CLS >> CWM at repo-level"可能是容量不足的 artifact 而非公式的固有差异。论文自己承认 14B 已将差距缩小到 1.07pp——这恰恰暗示 repo-level 的 divergence 可能在更大规模下消失。

- R1 评估：论文已用 "preliminary" 和 "capacity-contingent" 做了 hedge，但主张仍以 ≤8B 为基础，可接受但需加强 qualifier
- R2 评估：这是根本性限制，8B 结果可能 3–6 个月内被推翻，降低了 contribution 的持久性
- **Director 判定**：这是本文最大的 validity threat。论文的 hedging 是到位的，但 ≤8B 作为唯一 fully-replicated 设置，读者难以判断哪些 findings 会 survive scaling。建议在 introduction 和 conclusion 更显著地标注 scale caveat。

**W2. TRAJ 比较的公平性问题 [共识]**
TRAJ 使用 patch-level binary verdict（1 token），而 CLS 使用 per-test classification。TRAJ 缺少 per-test diagnostic granularity 是设计决定而非公式固有限制——可以设计 per-test TRAJ。论文将 TRAJ 的劣势归因于 "inherent confounding"，但部分劣势来自特定实现选择。

- 两位 Reviewer 均同意 TRAJ 比较应标注为 exploratory
- **Director 判定**：论文应明确 TRAJ 的 granularity 差异是 design choice 而非 inherent limitation

**W3. CWM baseline 强度存疑 [分歧]**
CWM 使用 matched LoRA rank/data 与 CLS 对比，但未探索对 CWM 更有利的设置（如更长 max_length、专门的 format-compliance pretraining、constrained decoding）。>50% unparseable 可能是工程问题而非公式问题。

- R1 认为：matched design 是 controlled comparison 的正确做法，not a weakness
- R2 认为：CWM 的 format failure 是 straw man，fair comparison 应给 CWM 充分工程支持
- **Director 判定**：两种立场都有道理。论文的 matched design 符合实验方法论，但应在 discussion 中明确承认 CWM 可能从 format-specific interventions 获益，并将此列为 future work

**W4. 因果语言过强 [共识]**
多处使用 "reveals"、"demonstrates"、"confirms" 等因果性措辞描述观察性结果。例如 "we attribute the domain difference to output structure" 暗示因果关系，但实际是 post-hoc 解释。

### 次要问题 (Minor)

**M1. SESOI 敏感性分析应在正文提及 [共识]**
±2pp SESOI 是核心等价检验的关键参数，但敏感性分析仅在 Appendix D。至少应在正文 §3.4 用一句话提及不同 SESOI 下结论的稳健性。

**M2. "Formulation" vs "Task framing" 术语不一致 [R2, R1 部分同意]**
论文交替使用 formulation、task framing、output format，可能造成混淆。建议在 §2.1 统一定义后一致使用。

**M3. 缺少 execution upper bound [R2]**
没有报告实际执行测试的 accuracy 作为 ceiling，读者无法判断 execution-free 方法距离 practical utility 有多远。

**M4. Complementarity 结论力度 [共识]**
Error complementarity 被列为 contribution 之一，但实际是 negative result（互补性不足以 justify ensemble）。建议明确标注为 negative result 并调低措辞力度。

---

## Reviewer Consensus

1. 统计方法论是本文最大亮点，显著优于同领域论文平均水平
2. SESOI 敏感性分析应在正文有所体现
3. TRAJ 比较应标注为 exploratory 而非 definitive
4. 14B 结果需保持 "preliminary" qualifier
5. Complementarity 应明确为 negative result
6. 因果性语言需全文 softening

## Reviewer Divergence

1. **Scale limitation 严重程度**：R1 (3.5) 认为论文 hedging 充分，是 reasonable scope choice；R2 (3.0) 认为这是根本性限制，可能导致核心 finding 过时。Director 倾向 R2——scale limitation 的影响确实可能使 repo-level findings 的 shelf life 较短。
2. **CWM baseline 公平性**：R1 认为 matched comparison 方法正确；R2 认为 CWM 需要更多工程支持。Director 认为双方各有道理，需在 discussion 中 acknowledge。

---

## Questions for Authors

Q1. 14B 结果将差距缩小至 1.07pp——作者是否认为 repo-level divergence 会在 32B+ 完全消失？如果是，§3.5 的 repo-level findings 的实际价值是什么？

Q2. CWM 的 >50% unparseable rate 在加入 constrained decoding 或 format-specific fine-tuning 后会如何变化？是否做过相关 pilot experiment？

Q3. 为什么没有包含 execution-based oracle 作为 upper bound？这对评估 practical gap 至关重要。

Q4. TRAJ 如果改为 per-test 粒度（逐测试生成 pass/fail），是否仍然 underperform CLS？

Q5. ICC = 0.191 (function-level) 意味着 seed variance 非常大。这是否暗示 5 seeds 不足以稳定估计？

---

## Missing References

- **RepoExec** (Nam et al., 2025): 已引用但未深入讨论其 repo-level execution verification 方法论与本文的异同
- **CodeScaler** (Zhu et al., 2026): 已引用，execution-free reward model 的相关工作覆盖较完整
- 建议补充：最近的 constrained decoding for structured output 文献（如 Guidance, Outlines），与 CWM format compliance 问题直接相关

---

## External Review

未启用（status: not_requested）。

---

## Visual Layout Check

**Status**: 已完成 (0 critical, 4 warnings, 9 info)

Warnings:
1. 最后一页近空（仅含少量 references），空间利用率低
2. Pages 1–2 无 display items（图/表），纯文本密度较高
3. Appendix 部分存在较长纯文本段落
4. 部分 figure caption 与正文存在少量冗余

所有 info items 为正面评价（排版整体规范、图表质量可接受）。无需因视觉问题调整评分。

---

## Overall Assessment

**Score: 3.0 — Findings**

**Soundness**: 3.0 — 统计方法论优秀，但核心 finding（repo-level divergence）的 generalizability 受限于 ≤8B scale，且 14B 已显示 convergence trend，削弱了结论的稳健性。

**Excitement**: 2.5 — 研究问题实用，但 formulation comparison 在 ≤8B 的 finding 可能短期内被 scaling 结果推翻。Contribution 的 lasting impact 存疑。

**Justification**: 论文在方法论上表现出色——统计严谨性显著优于同领域平均水平，failure mode taxonomy 有诊断价值，写作清晰。然而，核心 empirical finding 建立在 ≤8B 这一可能不再代表 frontier 的 scale 上，14B 的 convergence 趋势进一步削弱了 repo-level divergence 这一主要 contribution 的持久性。TRAJ 比较的公平性问题和 CWM baseline 的工程优化空间也使部分结论的 definitiveness 打折。作为 Findings paper，方法论贡献（统计框架 + failure taxonomy）足以支撑，但距离主会议的 excitement 和 impact 标准有差距。

**Recommendation**: Findings 可接受。若要冲击主会议，需要 (1) 32B+ 规模的完整复现，(2) CWM 加入 format-aware 优化后的对比，(3) execution-based upper bound。

---

## Detailed Comments

### For Authors

1. **Introduction §1**: "we reveal that complexity moderates the classification–generation tradeoff" — "reveal" 暗示因果发现，建议改为 "we observe" 或 "our results suggest"

2. **§2.1**: 建议在此处统一 "formulation" 的定义，并在全文一致使用，避免与 "task framing"、"output format" 混用

3. **§3.4**: TOST 等价检验后，添加一句：SESOI 敏感性分析见 Appendix D，±1pp 和 ±3pp 下结论 [稳健/变化]

4. **§3.5**: Repo-level 结果段落开头应加入显著的 scale caveat："The following results are established under ≤8B LoRA; preliminary 14B evidence (§3.3) suggests these gaps may narrow at larger scales."

5. **§3.6 Complementarity**: 将 "error complementarity analysis" 改为 "error complementarity analysis (negative result)"，明确标注

6. **Conclusion**: "we presented the first systematic comparison" — 考虑加入 "at ≤8B scale" qualifier

7. **Table 1/2/3**: 表格清晰，但建议在 caption 中标注 seed count（5 seeds for ≤8B, 3 seeds for 14B）

8. **Limitations**: 当前覆盖了 scale、language、synthetic data 三个点，长度合适。可考虑添加半句关于 CWM 未做 format-aware optimization 的 acknowledgment
