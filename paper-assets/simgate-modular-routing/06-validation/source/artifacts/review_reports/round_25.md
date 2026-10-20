---
round: 25
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T15:13:45.826286+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 25 (Fresh Review)

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**投稿类别**: Interpretability and Analysis of Models for NLP
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+相关工作）
**审稿轮次**: 1 轮（Round 1 初审 → 交叉分享 → 收敛，关键问题全部达成共识）

---

## Summary

本文提出 episode-level counterfactual diagnostic framework，比较 LLM agent 在 pure-internal（ReAct）与 pure-deterministic（oracle simulator）策略下的 episode 结果，分解 routing signal 的来源。核心发现：在 ScienceWorld 的 11 类任务（245 episodes）中，78.9% 的 non-tie routing labels 源自 death asymmetry——internal 策略触发 −100 惩罚的灾难性失败而 deterministic 策略存活。引入 Death Avoidance Factor (DAF) 量化该效应（DAF=90.4%），跨三个模型家族（Qwen-7B/Llama-8B/Gemma-9B, DAF 88-90%）和 72B scaling 验证一致性。Cross-environment boundary probes（MATH 无信号、ALFWorld 信息不对称）展示框架在不同机制下的诊断能力。Router 训练得到负结果（step-level balanced accuracy 56-59%），归因于 death avoidance 是 task-type-level 而非 step-level 信号。

---

## Strengths

**S1. 研究问题有价值且切入角度新颖 [共识]。** 现有 routing/tool-use 工作集中于"如何建 router"，本文退一步问"routing signal 到底是什么"。这种"先诊断再优化"的方法论对 agent routing 社区有指导意义，切入了一个被忽视的诊断性问题。

**S2. 统计方法论一流 [共识]。** Bootstrap resampling (B=10,000)、cluster bootstrap sensitivity (K=11, 含 wild cluster bootstrap)、Signal Concentration Index (SCI)、leave-one-task-out stability analysis、per-task CIs、dose-response analysis、Cohen's d——统计工具链完整且使用得当，远超多数 agent 论文的 reporting 标准。95% CIs 贯穿全文所有 quantitative claims。对 K=11 cluster bootstrap power 不足的问题也诚实讨论（Cameron et al. 2008 推荐 K≥20-30）。

**S3. 对自身局限性的坦诚讨论 [共识]。** 论文对局限性的讨论异常透明——r=0.97 correlation 是 structural consequence（§3.1）、DAF 是 penalty-dependent（§2.4）、router 是 negative result（§3.6）、task exclusion 有完整分析（Appendix C/S）。这种 intellectual honesty 在同类论文中罕见。

**S4. Cross-model validation 扎实 [共识]。** 三个架构不同的模型族（Qwen/Llama/Gemma）独立收敛于 DAF 88-90%（spread 2.2pp），加上 72B scaling (DAF=92.4%)，构成 convincing 的 robustness evidence。Appendix M 提供完整 per-task 分解。

**S5. Router negative result 有价值 [共识]。** §3.6 的 step-level router 无法捕获 task-type-level 信号是一个重要实践性发现，能帮社区避免无效的 router 开发投入。Appendix P 的 generative router (46.7%) 进一步确认瓶颈在 signal 而非 architecture。两位 Reviewer 一致认为这可能是论文最有实践价值的贡献。

**S6. 附录极其详尽 [共识]。** 20 个 Appendices (A-T) 覆盖 task selection rationale、correlation robustness、penalty sensitivity、failure mode taxonomy、grounding ablation、prompt templates 等，可复现性极高。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [Critical, 共识] DAF 度量在 ScienceWorld 奖励结构下有 tautological 倾向。**
DAF = δP/(δP + Δ_nd) 在 P=100、Δ_nd=2.84 的条件下必然趋近 1——这是代数事实而非经验发现。论文在 §2.4 和 §3.1 已承认（"mathematical consequence rather than an empirical finding"、"the 78.9% label fraction provides the more robust characterization"），但 Abstract 和 Introduction 仍将 DAF 88-90% 作为 prominent metric 呈现。真正有信息量的经验发现是 label fraction (78.9%)，而非 DAF 数值本身。两位 Reviewer 建议：明确将 label fraction 作为 headline metric，DAF 降级为 supplementary score-weighted measure。（R1-W1, R2 交叉 AGREE）

**W2 [Critical, 共识] 核心发现的新颖性有限——death dominance 在实验设置下方向可预期。**
Oracle simulator 提供 ground-truth state transitions，而 internal 策略依赖会幻觉的 LLM。在 −100 death penalty 下，oracle 天然比幻觉策略更安全——death asymmetry 的 *存在* 是可预期的。§5 的 non-triviality 论证（72B 未消除、Reflexion DAF>100%、inverted-U）是关于 death dominance 的 *persistence*，而非 *existence* 的 surprise。R1 交叉回应中指出：prevalence 量化（78.9%）和 router negative result 仍有 surprise value（Δ_nd≈2.84 near-uniform 需要实证确认；router failure 不可从设置预测）。但两位 Reviewer 共识 Excitement 仅 2.5/5，这是 Findings 而非 Conference 水平的核心原因。此问题不可通过 writing 修复——需新环境深度分析或根本性新发现。（R2-N1, R1 AGREE with nuance）

**W3 [Critical, 共识] 单环境 scope + generality overclaim。**
主实验仅在 ScienceWorld 上进行。MATH（84.4% no-preference）和 ALFWorld（DAF=0%, 无死亡机制）作为 boundary probes 只展示框架的诊断能力多样性，不能验证 death-dominance 发现是否泛化到其他有灾难性失败的环境。论文正文 §3.4 已将 MATH/ALFWorld 定位为 "boundary probes (not cross-domain validation)"，但 Abstract ("demonstrating the framework's generality") 和 Conclusion 措辞仍在 overclaim。bib 中有 NetHack/MiniHack/BALROG/Crafter 等有 catastrophic failure 的环境但均为 orphan references。建议：(a) 降低 Abstract/Conclusion generality claim 至与 §3.4 一致；(b) 在至少一个有 permadeath 的替代环境上验证（如 NetHack）。（R1-W2, R2-N2, 交叉 mutual AGREE）

### Should-Fix（影响评分但不一票否决）

**W4 [Warning, 共识] Router negative result 替代解释未充分排除。**
§3.6 claim "signal-limited, not architecture-limited" 但未充分排除：(a) 训练数据规模极小（245 episodes/~2040 steps），paraphrase augmentation ≠ 真实数据扩增；(b) router 仅 0.6B-4B，更大模型或不同架构未测试；(c) 缺少 task-level router positive control（输入 task type → 输出 routing decision）。Appendix P leave-one-task-out 中 keyword variant 62.9% 间接证明 task-type identification 是唯一可学信号，但显式实验会更 clean。建议弱化 absolute claim 并添加 task-level router 实验。（R1-W4, R2 AGREE）

**W5 [Warning, 共识] Contribution framing 不清晰——三条 contribution 存在依赖关系。**
(1) 框架 → (2) 应用于 ScienceWorld → (3) robustness check，是层层依赖而非独立并列。R1 REBUT 指出 router negative result 有独立价值，排序应为 (a) router failure > (b) 78.9% prevalence > (c) 框架本身。共识：不构成 blocking issue，但 contribution statement 应更清晰区分方法论贡献与实证 insight，并更 prominently frame router failure。（R2-N3, R1 partial REBUT but agrees on framing improvement）

**W6 [Warning, 共识] Conclusion 过于单薄。**
单段约 60 词，对于 8 页正文 + 20 个 Appendix 的 long paper，未讨论 broader implications、future work 方向、或对 NLP community 的 takeaway。建议扩展至 2-3 段（在 8 页预算内）。（R2-W3, R1 AGREE）

**W7 [Warning, 共识] "penalty-independent" 表述在 Abstract/Intro 中有误导性。**
Label fraction 数值不依赖 P，但 P=0 时 54 个 sole-signal labels 变为 ties（non-tie 从 95 降至 41），routing signal 的实际 relevance 高度依赖 penalty magnitude。建议改为更精确表述如 "invariant to penalty magnitude in the labeling procedure"。（R2-W2, R1 AGREE）

**W8 [Warning, 共识] Safe RL 相关工作覆盖不足。**
§4 Safe RL 段落仅 3 行，引用 5 篇经典 + 2 篇近期。鉴于核心发现是 catastrophic failure avoidance dominates routing signal，应更详细讨论与 constrained MDPs/risk-sensitive RL 的关系，以及为什么 Safe RL 方案（如 CPO）不直接适用于 LLM agent routing。（R2-W4, R1 AGREE）

**W9 [Warning, 共识] Task selection (11/30) 的 agent-floor tasks 含义未讨论。**
63% exclusion rate 有合理理由且 anti-cherry-picking 分析到位（Appendix C/S），但 7 个 agent-floor tasks 代表什么 regime 未讨论——如果两策略都频繁死亡（无 asymmetry），routing signal 可能由非 death 因素驱动，这是 death dominance 不成立的有趣案例。建议在 Discussion 补充。（R1-W3, R2-W1, R2 partial REBUT on data availability but AGREE on framing）

**W10 [Warning, R1 提出] 实验规模偏小，per-task 统计 power 不足。**
Per-task n=20，Wilson CI ~±20pp。Table 1 caption 已标注 exploratory。共识：aggregate claims (N=245) 可靠，per-task 需谨慎解读。不构成 blocking issue。（R1-W5, R2 AGREE）

**W11 [Warning, R1 提出] 实际指导价值有限。**
诊断之外缺少 constructive 解决路径。Appendix R Decision Framework 有 retrospective 4/4 validation（R2 指出非"未验证"），但 grounding ablation (Appendix O, death rate 48%→29%) 是有潜力的方向，应在主文给更多篇幅。论文定位为 diagnostic 非 prescriptive（Limitations 明确声明），此定位本身可接受但降低了 impact。（R1-W6, R2 partial REBUT）

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上完全一致（所有交叉回应为 [AGREE]）：
1. DAF 在 ScienceWorld 奖励结构下有 tautological 倾向，label fraction 应为 headline metric
2. 单环境 scope 限制泛化性，Abstract/Conclusion generality claim 需收窄
3. 核心发现方向可预期，Excitement 不足（均 2.5/5）
4. Router negative result 被 underframed，应提升为核心 contribution
5. Conclusion 过于简短
6. Safe RL 覆盖不足
7. Per-task power 有限但 aggregate 可靠
8. Overall 3.0 (Findings)

## Reviewer Divergence

仅有轻微分歧，均已在交叉回应中解决：

1. **Contribution 独立性 (R2-N3)**：R2 认为三条 contribution 的依赖关系使 overall contribution 难以评估；R1 REBUT 指出 router negative result 有独立价值。**Director 判断**：R1 的 rebut 有道理，但不改变 overall score——contribution framing 需改进但非 blocking。

2. **Task selection 数据可用性 (R1-W3)**：R1 声称 excluded tasks 数据未展示；R2 REBUT 指出 Appendix C Table 4 和 Appendix S 已提供。**Director 判断**：R2 的事实纠正正确，R1 可能遗漏了附录数据。但 R1 的深层观点（agent-floor tasks 的 regime 含义）成立。

3. **Practical guidance (R1-W6)**：R1 称 Decision Framework "未验证"；R2 REBUT 指出有 retrospective 4/4 validation。**Director 判断**：R2 的事实纠正正确（有 post-hoc validation），但 R1 对 constructive 方案缺失的批评仍然有效。

---

## Questions（需要作者澄清）

**Q1.** P=0 时 label fraction 从 78.9% 降至 51.2%（§3.1 已有数据）——建议以表格形式突出展示 P=0/10/50/100/200 的 label fraction 变化，而非仅在段落中提及。

**Q2.** 61.2% tie rate (150/245) 意味着 routing 最多改善 38.8% 的 episodes。这对 routing 系统的实际 ROI 意味什么？建议在 Discussion 中增加分析。（R2-Q3, R1 AGREE 称"R2 最有洞察力的问题之一"）

**Q3.** 2.6% 有差异的步骤（159/6094）是否集中在 death-triggering 步骤？Appendix P 的 death-proximal labeling 间接涉及但缺少 descriptive analysis。（R1-Q2）

**Q4.** Grounding ablation (Appendix O) 将 death rate 从 48% 降至 29%。在此条件下重新计算 DAF 的值是多少？（R1-Q3, R2 AGREE——这将验证框架对 intervention 的敏感性）

**Q5.** 0.5B inverted-U claim 基于 n=15，Wilson CI 极宽。是否有足够统计 power 区分 inverted-U 和 random fluctuation？（R2-Q4, R1 AGREE）

**Q6.** "deterministic" 统称 oracle simulator (ScienceWorld)、code interpreter (MATH)、admissible-action access (ALFWorld) 三种性质不同的 information advantage。§2.1 脚注有简要说明，但主文应更显式区分以避免误导读者认为 cross-environment 比较是 apples-to-apples。（R2-Q2, R1 AGREE）

---

## Missing References

以下为两位 Reviewer 共同认可应补充的引用（经交叉验证）：

1. **Kumaraguru et al. (2025)** "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety" — agent self-monitoring 与 catastrophic failure prevention，直接相关（R2 提出，R1 AGREE 如确认存在）
2. **Agent-SafetyBench (2024)** — 349 个交互环境的 LLM agent 安全评估 benchmark（R2 提出，R1 AGREE）
3. **Step-level credit assignment 近期文献** — R2 提出具体引用 (arxiv:2604.09459, 2604.11037, 2603.08754)，与 episode-level vs step-level 信号分析相关。R1 认为已引 SALT/CSO 基本覆盖，但额外引用可增强完整性
4. **Pona et al. (2025)** — 已引用但区分不够详细，应更明确对比 abstract counterfactual (action-level perturbation) vs. episode-level pure-strategy comparison
5. **ToolEmu (Ruan et al., 2024)** — 已引用但应扩展讨论 emulated sandbox vs. real environment 的方法论对比

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~3.5 分钟）。结果：0 critical, 4 warning, 22 info。

**Warnings**:
1. **Page 5 纯文本页**：夹在 page 4 (Figure 2) 和 page 6 (Table 1 + Figure 3) 之间，视觉节奏断裂。建议将 Table 1 或 Figure 3 前移平衡密度。
2. **Pages 7-8 视觉密度偏低**：Discussion + Conclusion 全为纯文本。如能引入小型总结性 figure（如 decision framework 流程图）可改善末尾节奏。
3. **Page 20 三图挤压**：Figures 5-7 同页（占 55%），Figure 6 标签密集，灰度下可能难区分。
4. **Page 25 大面积空白**：Responsible NLP Checklist 格式限制导致，非排版错误但不够专业。

**Key Info findings**:
- 主文 8 页，Conclusion 在 page 8 底部结束，符合 EMNLP 8 页限制 ✓
- 首个 display item (Figure 1) 在 page 3，前 2 页纯文本——考虑添加 teaser figure
- 主文 display items 5 个（3 figures + 2 tables），处于推荐 5-8 个的下限
- 所有表格统一 booktabs 风格，公式渲染无错误，双栏排版对齐良好
- Figure 4 (bar chart) 建议验证灰度打印区分度

---

## Overall Assessment

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.5/5 | 4.0/5 | 3.5-4.0 |
| Excitement | 2.5/5 | 2.5/5 | 2.5 |
| Reproducibility | 4/5 | 4/5 | 4.0 |
| Overall | 3.0 | 3.0 | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | 4.0 |

**Overall: 3.0 (Findings)** — 可被 Findings 接收，但不达主会议标准。

**核心判断**：这是一篇执行质量很高的诊断性分析论文。统计方法论一流，cross-model validation 扎实，对自身局限性的讨论异常诚实，router negative result 有重要实践价值。但核心发现（death dominance of routing signal）在 oracle vs. hallucinating-LLM 的实验设置下方向可预期，DAF 度量在 ScienceWorld 奖励结构下有 tautological 倾向，单环境 scope 限制了泛化性 claim。**Excitement 是接收瓶颈**（2.5/5），Soundness 充分（3.5-4.0/5）。

**提升路径**（非本 session 职责范围，仅记录 Reviewer 共识方向）：
1. 在至少一个有 catastrophic failure 的替代环境（如 NetHack）上验证 death dominance → 解决 W3
2. 更 prominently frame router negative result 为核心贡献 → 部分缓解 W2/W5
3. 添加 task-level router positive control 实验 → 解决 W4
4. 将 label fraction 78.9% 作为 headline metric，DAF 降级 → 解决 W1
5. 收窄 Abstract/Conclusion generality claim → 解决 W3

---

## Detailed Comments（逐节）

### Abstract
- DAF 88-90% 仍作为 prominent metric，建议以 label fraction 78.9% 为 headline
- "demonstrating the framework's generality" overclaim，与 §3.4 "boundary probes" 定位不一致
- "penalty-independent" 修饰需精确化

### §1 Introduction
- 第二段一次引用 11 篇，影响可读性
- Contribution (2) 和 (3) 对 (1) 有依赖，建议重组

### §2 Method
- §2.1 脚注中 "deterministic" 三种含义的区分应提升到正文
- §2.4 DAF tautological 讨论已存在，但应在此处加入显式声明："the empirically informative quantity is not DAF per se but the prevalence of death asymmetry"
- DAF 定义出现在两个等式中（exact + approximate），建议合并

### §3 Experiments
- §3.1 P=0 label fraction 变化（95→41 non-tie, 51.2% death-asymmetry）被埋在段落中，建议以表格突出
- §3.4 "boundary probes (not cross-domain validation)" 定位正确，但 Abstract/Conclusion 未保持一致
- §3.6 Router 负结果标题和位置暗示附带发现，实际是最有价值的贡献之一

### §4 Related Work
- Safe RL 段落（3 行）过于简略，需扩展 CMDP/risk-sensitive RL 讨论
- Pona et al. (2025) 方法论区分不够详细

### §5 Discussion
- Non-triviality 段有效但不足以消除 "obvious in hindsight" 的 concern
- 61.2% tie rate 的 implication（routing ROI）未讨论
- Agent-floor tasks 的 regime 含义未讨论

### §6 Conclusion
- 过于简短（单段 ~60 词），需扩展至 2-3 段

### Limitations
- 覆盖全面（5 个 paragraph），长度合理
- Pure-strategy upper bound 段落到位

### Format/Misc
- 8 个 orphan bib entries 需清理
- Webb (2023) 年份需再次核实
- Table 1 caption "20-40 episodes per type" 但实际仅 find-non-living-thing 有 40
- ScienceWorld 版本号应全文统一（Appendix C 标 v1.2.3）
- Gajcin (2023) OpenAlex confidence 0.78，建议核实