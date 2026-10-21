---
round: 24
review_mode: continue
overall_score: 3.0
timestamp: 2026-05-21T07:12:01.916769+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 24 审稿报告 — simgate-modular-routing

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (ARR Long Paper, deadline 2026-05-25)
**审稿模式**: Continue（基于 Round 23 修改验证）
**Reviewer 编排**: 2 人 + 视觉审查 Agent
- Reviewer 1: 方法严谨性 + 统计推断 + Router 实验 + noisy label
- Reviewer 2: Framing 准确性 + 写作质量 + 格式合规 + 术语一致性

---

## Summary

Round 24 为继续审稿，验证论文对 Round 20/23 提出的 4 项 Must-Fix 和 9 项 Should-Fix 问题的修改是否充分。论文在统计推断、framing 准确性、格式合规三个维度均有实质性改进。所有 4 项 Must-Fix 问题已解决（cluster bootstrap CI 修正、4B router 结论 qualified、页数收入 8 页、"structurally determined" 消除）。Should-Fix 中大部分已解决，3 项部分修复（跨环境定义仅脚注、noisy label 讨论缺一句、mislabeling circularity 微小残留），均可通过 1-2 句 editorial 修改关闭。核心 novelty concern（单环境深度分析的 excitement 上限）不可通过 writing 修复，需新环境深度分析。

---

## Strengths

1. **统计方法论严谨度大幅提升** [共识，R1 Soundness 3.5→4.0，R2 同意]: Cluster bootstrap CI 从反常窄 [95.2%, 99.5%] 修正为合理的 [73.3%, 100.0%]，Appendix E 降级为 Sensitivity Analysis 并声明 non-clustered bootstrap 为 primary inference。4B router 结果获完整统计处理（Bonferroni 校正 p<0.001、leave-one-task-type-out 49.2%、independent eval 47.1%）。Per-task 结果标注为 exploratory（power ≈ 50%）。这些修正使论文的统计基础在 NLP 会议论文中属上乘。

2. **Framing 一致性显著改善** [共识]: Label fraction 78.9% 确立为 primary headline，DAF 降级为补充指标。§2.4 新增 "Relationship between DAF and label fraction" 段落解释代数关系。"Structurally determined" 全文消除，改为 "empirically dominated"。Router 结论从 "no learnable signal" 弱化为 "under current architectures and data regime"。Dose-response "plateau" 改为 "stabilization"/"suggestive evidence"。Overclaim 系统性修正。

3. **诊断框架的跨环境验证** [共识]: ScienceWorld (DAF=90.4%)、ALFWorld (DAF=0%, information asymmetry)、MATH (null result, p=0.81) 三个环境诊断出三种质性不同的 routing mechanism，证明框架的通用诊断能力而非特定环境的后见之明。

4. **实验深度与可复现性** [共识]: 19 个 Appendix 覆盖 anti-cherry-picking analysis、leave-one-out stability、penalty sensitivity、seed robustness、extended validation、failure mode anatomy。Anti-cherry-picking 分析（excluded tasks ΔDR=+38.2pp > included +28.7pp）有效回应 selection bias 质疑。三个 model family (Qwen/Llama/Gemma) 跨架构验证 DAF 88-90% (spread 2.2pp)。

5. **Limitations 段落质量** [共识]: 新增 pure-strategy upper bound 段落、P-invariance 适用范围量化、cluster bootstrap K<40 caveat、intervention ceiling caveat。四段结构覆盖 environmental scope、methodological constraints、statistical limitations、pure-strategy upper bound，坦诚且完整。

---

## Weaknesses

### 核心 Weakness（不可通过 editorial 修复）

1. **[W1] 核心 novelty/excitement 上限** [共识方向，程度分歧]
Death dominance 在 ScienceWorld 的 −100 penalty 下近似数学必然（DAF 是 δP/(δP+Δ_nd) 的代数后果）。§5 Non-triviality 段列举的三个 a priori 不可预测结果（72B DAF=92.4%, Reflexion DAF>100%, 0.5B inverted-U）有效缓解但不消除这一根本限制。框架 "发现" 的仍主要是奖励结构的推论。增加一个非 ScienceWorld 环境（如 NetHack/Crafter 的 death mechanism）的深度分析可显著提升 excitement。
R1 Excitement 3.0, R2 Excitement 3.0（从 2.5 上调）。

### 残留小问题（可通过 1-2 句话修复）

2. **[W2] 跨环境 "deterministic" 定义仅在脚注** [共识 PARTIALLY RESOLVED]
Method §2.1 脚注 1 完整解释了三种 deterministic 含义，但脚注 visibility 不足。建议在 §3.4 开头加一句交叉引用（~10 词）即可。

3. **[W3] Noisy label 讨论缺 structured noise 解释** [共识 PARTIALLY RESOLVED，降级为 Minor]
§3.6 已引 Natarajan 2013、Northcutt 2021、DivideMix，但缺一句解释此处 noise 为 systematic（task-type-correlated）而非 random flip，超出 standard noisy-label methods 的 i.i.d. noise 假设。

4. **[W4] Algorithm 1 术语残留** [共识 STILL_OPEN，trivial]
main.tex L95 Algorithm 1 `\REQUIRE` 行仍使用 "modalities"，正文已统一为 "computation modes"。一词修改。

5. **[W5] Appendix B mislabeling circularity 微小残留** [共识 MOSTLY RESOLVED]
Limitations 已将问题从 "label noise" 重新定义为 "granularity mismatch"（0.3% 方向冲突，60.3% pre-event neutral）。Appendix B 用 episode labels 评估 step-level prediction 存在微小循环论证，建议首句加 caveat。

---

## Questions（已通过修改回答的问题）

以下问题在 Round 20 提出，Round 24 确认已充分回答：

1. P-invariance 适用范围？→ §3.1 量化 P=0 退化至 51.2%；labeling function P-independent，routing value 需 P>0。**已回答。**
2. 4B router 59% 是 multiple comparison artifact？→ Bonferroni p<0.001，leave-one-task-type-out 49.2%，确认为 task-type classification。**已回答。**
3. Penalty manipulation 实验？→ P-invariance by design（agent 不观察 P）使 analytical sensitivity 等价于实际实验。**已回答。**

---

## Missing References

Round 20 标记的所有缺失引用已补全：
- Ng et al. (1999) Policy Invariance Under Reward Transformations → method.tex §2.4 ✓
- Northcutt et al. (2021) Confident Learning → experiments.tex §3.6 ✓
- Li et al. (2020) DivideMix → experiments.tex §3.6 ✓
- Altman (1999) Constrained MDPs → related_work.tex §4 ✓（Round 20 前已补）
- Mihatsch & Neuneier (2002) Risk-sensitive RL → related_work.tex §4 ✓（Round 20 前已补）

无新增缺失引用。

---

## External Review

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 完成，0 critical / 1 warning / 5 info：

- **[warning]** Page 1-2 连续纯文本无 figure/table，第一个 display item (Figure 1) 延迟到 Page 3。建议将 Figure 1 提前至 Page 2 加强第一印象。
- **[info]** Figure 2 scatter plot task name 标注字号偏小（~6-7pt），部分标签轻微重叠。
- **[info]** Table 1 仅 3 列 5 行，信息密度低。
- **[info]** Table 2 "†" 符号含义仅在 caption 脚注中，快速扫描易遗漏。
- **[info]** Figure 1 caption 未说明 "Episode-level labels" 具体含义。
- **[info]** Page 8-9 Discussion+Conclusion+Limitations 连续纯文本，视觉单调。

上述均为 presentation 建议，不影响评分。

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

| 维度 | Round 23 (R20 fresh) | Round 24 (continue) | 变化 |
|------|---------------------|---------------------|------|
| Soundness | 3.5 | **4.0** | 统计问题全部修正，overclaim 消除 |
| Excitement | 2.5-3.0 | **3.0** | §5 Non-triviality 有效回应 |
| Overall (R1) | 3.5 | **3.5** | Borderline Conference |
| Overall (R2) | 3.0 | **3.0** | Solid Findings |

### 评分分歧分析

R1 (3.5) vs R2 (3.0) 的 0.5 分差距源于 **Soundness 与 Excitement 的权重分配**：
- **R1 逻辑**: Must-Fix 全部解决 → Soundness 4.0 → 高执行质量部分补偿中等 novelty → Borderline Conference
- **R2 逻辑**: Excitement 是独立维度 → Soundness 改善不改变 novelty 评判 → 核心发现仍是 penalty structure 推论 → Findings

两者指向同一档位的不同端：Strong Findings / Borderline Conference。Director 判断：**采用 3.0 (Findings)**，理由：
1. Excitement 共识 3.0，novelty concern 不可通过 writing 修复
2. 单一主环境的深度分析 + boundary probes 的论文结构天然限制了 impact
3. 论文的 Soundness 4.0 和 presentation 质量使其成为 **strong Findings candidate**
4. 如增加第二个 death-mechanism 环境的深度分析，Overall 可升至 3.5

### 修改建议优先级

**提交前建议修复（~30 分钟工作量）：**
1. Algorithm 1 "modalities" → "computation modes"（1 词修改）
2. §3.4 开头加交叉引用脚注 1（~10 词）
3. §3.6 加一句 structured noise 解释（~20 词）

**如有时间（optional）：**
4. Appendix B 首句加 circularity caveat
5. Figure 2 标签字号调大 / 用 adjustText 避免重叠
6. Figure 1 尝试提前至 Page 2

---

## Detailed Comments

### 已解决的 Round 20 Must-Fix（确认关闭）

| ID | 问题 | Round 24 状态 | 修改质量 |
|----|------|--------------|---------|
| R20-N1 | 正文超 8 页 | ✅ RESOLVED | Conclusion 在 Page 8 |
| R13-N2 | Cluster bootstrap CI 反常收窄 | ✅ RESOLVED | CI [73.3%, 100.0%]，降级为 Sensitivity Analysis |
| R20-N2/R18-N1 | 4B router vs non-learnability | ✅ RESOLVED | Bonferroni + leave-one-out + independent eval |
| R20-N3 | "structurally determined" overclaim | ✅ RESOLVED | → "empirically dominated" |

### 已解决的 Round 20 Should-Fix（确认关闭）

| ID | 问题 | Round 24 状态 |
|----|------|--------------|
| R13-N1 | DAF framing | ✅ RESOLVED — label fraction 为 headline |
| R13-W5 | Abstract 数字堆砌 | ✅ RESOLVED — concept-first，3-4 个数字 |
| R13-W6 | Missing references | ✅ RESOLVED — Ng/Northcutt/DivideMix 已补 |
| R14-W1 | Triviality risk | ✅ RESOLVED — §5 Non-triviality 段 |
| R17-W1 | Pure-strategy upper bound | ✅ RESOLVED — Limitations 新段落 |
| R17-W3 | Data scaling 术语 | ✅ RESOLVED — → text augmentation |
| R18-W1 | Router claim 过强 | ✅ RESOLVED — "under current architectures" |
| R18-W2 | Dose-response plateau | ✅ RESOLVED — → stabilization + MDE |
| R20-W2 | Per-task not exploratory | ✅ RESOLVED — Table caption 标注 |
| R17-M1 | Orphan bibs / Webb year | ✅ RESOLVED — 清理完毕 |
| R17-N2 | P-invariance 范围 | ✅ RESOLVED — P=0 退化量化 |
| R19-W1 | Penalty experiment | ✅ RESOLVED — P-invariance by design 覆盖 |

### 部分解决（Minor 残留）

| ID | 问题 | 状态 | 修复建议 |
|----|------|------|---------|
| R15-N2 | 跨环境 deterministic 脚注 | PARTIALLY | §3.4 加交叉引用 |
| R20-W1 | Noisy label structured noise | PARTIALLY | §3.6 加一句解释 |
| R15-W2 | Appendix B circularity | MOSTLY | 首句加 caveat |
| R18-M1 | Algorithm 1 "modalities" | STILL_OPEN | 1 词修改 |

### Round 24 改进总结

论文在 Round 20→24 期间解决了全部 4 项 Must-Fix 和 12 项 Should-Fix 中的 12 项。Soundness 从 3.5 提升至 4.0。残留 4 项均为 Minor/editorial 级别，可在 30 分钟内修复。核心 novelty concern（单环境深度分析的 excitement 上限）是论文结构性限制，不可通过 writing 修复。Overall 维持 3.0 (Findings)，论文为 **strong Findings candidate**。