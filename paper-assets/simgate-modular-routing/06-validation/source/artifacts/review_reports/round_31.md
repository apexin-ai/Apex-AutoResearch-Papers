---
round: 31
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T05:35:44.709034+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 31 审稿报告

**论文**：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**目标 Venue**：EMNLP 2026（ARR May cycle, Long Paper）
**审稿模式**：Fresh（无上轮记忆）
**Reviewer 编排**：R1（方法严谨性+实验设计）、R2（新颖性+完整性+写作）

---

## Summary

本文提出 episode-level counterfactual diagnostic framework，通过在相同初始条件下运行 internal（ReAct）和 deterministic 两种纯策略，将 routing signal 分解为 death-avoidance 和 non-death 两个成分。在 ScienceWorld（11 task types, 245 episodes）中，78.9% 的 non-tie routing labels 和 90.4% 的 performance gap（DAF）源于 death asymmetry，该 pattern 在三个 7-9B 模型族（Qwen/Llama/Gemma）上复现。Cross-environment probes（MATH: DAF=0%, ALFWorld: DAF=0%）显示 routing mechanism 因环境而异。论文定位为 diagnostic contribution。

---

## Strengths

**[S1] 问题定位准确，填补方法论空白**（R1-S1, R2 agree）。现有 routing 工作直接训练 router 而不先诊断信号来源。"先诊断再建模" 范式填补了真正的方法论缺口。

**[S2] 统计严谨性远超同 venue 平均水平**（R2-S2, R1-S3）。Episode-level bootstrap (B=10,000)、cluster bootstrap sensitivity (K=11)、wild cluster bootstrap、LOTO sensitivity、per-task CIs、8-seed robustness——这套 robustness pipeline 值得其他 empirical study 参考。

**[S3] 异常诚恳的自我批评**（R1-S3, R2-S3）。论文主动承认了几乎所有潜在问题：K=11 局限、DAF 对 P 的单调依赖、router 结果不确定性、episode-level labeling 的粒度错配。这种透明度在 *ACL 投稿中罕见。

**[S4] 跨模型验证设计合理**（R1-S4）。三个架构差异显著的 7-9B 模型族收敛于 DAF 88-90%（spread 2.2pp），排除了 model-specific artifact。

**[S5] Anti-cherry-picking 分析有说服力**（R1-S5, R2-S4）。Excluded 19 个 task types 的平均 ΔDR (+38.2pp) 高于 included 11 个 (+28.7pp)，与 cherry-picking 假设预测方向相反。

**[S6] 框架简洁可复用**（R1-S2, R2-S1）。DAF 和 labeling function 形式化完整，成功无修改应用于三个不同环境，诊断出三种不同 routing mechanism。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[N1] [critical] 单一主环境 + diagnostic-only 定位限制 Main Conference 级别**（R1-W1, R2-W1, R2-W3 共识）
核心实证发现（78.9%, DAF=90.4%）完全来自 ScienceWorld 一个环境。MATH 和 ALFWorld 是 boundary probes 而非 death-dominance 验证。ScienceWorld 的 death 机制极为特殊（100% 来自单一 action `focus on`）。Diagnostic framework + single-environment finding 的 contribution type 更适合 Findings 而非 Main Conference。

**[N2] [critical] Oracle privilege 使 death avoidance 发现接近 tautology**（R1-W2, R2 部分同意）
Deterministic 策略 = simulator forking（极强 oracle privilege）。在此条件下，"oracle prevents irreversible errors" → death avoidance 主导 routing signal 在逻辑上是预期的。论文真正非直觉的洞见是 Δ_nd≈2.84（non-death gap 极小，仅占 9.6%），但被框架包装为 DAF 的副产品而非核心发现。论文已在 §2.1 加 umbrella term 和 §5 讨论 Δ_nd，但 fresh reviewer 认为仍需更突出。

### Should-Fix（影响评分）

**[W1] DAF 对 P 单调依赖——headline 应更侧重 label fraction**（R1-W4, R2-W2 共识）
DAF = δP/(δP + Δ_nd) 随 P 单调递增是数学事实（P=10: 50.4%, P=100: 90.4%, P=500: 97.9%）。论文已在 §2.4 承认并以 label fraction 为 primary，但 Abstract/Intro/Conclusion 多处仍突出 DAF=90.4%。建议进一步降低 DAF 在 headline 位置的权重。

**[W2] K=11 cluster bootstrap 推断——应以非参数检验为主**（R1-W3）
论文建议读者依赖非聚类 bootstrap CI 但同时承认 within-cluster correlation 存在——逻辑不自洽。Permutation test (p=0.002)、sign test (p<0.001) 和 100% directional consistency 是更可靠的推断依据，应在正文中提升地位。

**[W3] Episode→step 粒度错配限制框架实用性**（R1-W5）
框架产出 episode-level labels 但 routing 需 step-level 决策。88% uninformative steps。框架实用价值收窄为 "是否值得尝试 routing" 的 sanity check，应更明确定位。

**[W4] 72B probe 缺 cross-model replication at scale**（R1-W6）
7-9B 有三个模型族 replication 但 72B 仅 Qwen2.5-72B。Intro 将两者并列可能高估 scaling robustness。

**[W5] Appendix 过多（21 个, 15 页），核心证据分散**（R2-W4）
Penalty sensitivity (K)、Decision Framework (R)、Threshold Routing (Q)、cross-model 完整结果 (M) 等核心 claim 支撑在 Appendix。读者无法仅通过正文 8 页评估贡献。

**[W6] Related Work 缺 risk-sensitive RL / CVaR 文献**（R2-W5）
CVaR optimization (Chow 2015, Tamar 2015) 直接处理 trajectory-level catastrophic risk，与 death avoidance 高度相关但未讨论。

**[W7] "Counterfactual" 术语使用松散**（R2-W6）
方法更接近 matched-seed A/B testing 而非 Pearl (2009) structural counterfactual。需在 §2.1 明确定义。

**[W8] Discussion 过薄（~0.5 page, 2 个话题）**（R2-W8）
缺少条件分析（when does death avoidance dominate?）和与 concurrent work（MTRouter, CogRouter, BAAR）的对话。

---

## Reviewer Consensus

以下关键问题两位 Reviewer 达成共识：

1. **[AGREE] Overall 3.0 (Findings)**：方法论可靠、分析透彻、自我批评诚恳，但单一主环境 + 预期内发现限制影响力。两位 Reviewer 独立给出相同评分。

2. **[AGREE] 单一环境是核心局限**：缺少第二个 death-dominated 环境验证是接收为 Main Conference 的主要障碍。

3. **[AGREE] DAF=90.4% 作为 headline 需降权**：label fraction (78.9%) 是更 robust 的 primary metric；DAF 随 P 单调递增部分是方法论产物。

4. **[AGREE] 统计严谨性和诚实自评是突出优点**：21 个附录的 robustness analysis 和 "Inconclusive Results" 标注在同类工作中罕见。

5. **[AGREE] 框架可复用性是实在贡献**：无修改应用于三个环境并诊断出不同 mechanism，具有方法论价值。

---

## Reviewer Divergence

1. **Oracle privilege / tautology 的严重程度**：R1 将此列为 Must-Fix critical，认为 death avoidance 在 oracle-privileged 设定下接近同义反复；R2 将相关问题分散在 DAF circularity (W2) 和 contribution type (W3) 中，严重程度略低。Director 判断：R1 的分析更深入——如果将 Δ_nd≈2.84 提升为与 death dominance 并列的核心发现，可部分化解 tautology 质疑。

2. **Counterfactual 术语**：R2 认为术语使用松散需修正；R1 未特别关注。Director 判断：这是 writing-level 问题，不影响接收决定，但值得在 revision 中处理。

3. **Router training section 的空间**：R2 认为 "inconclusive" 结论占半页不值得；R1 认为负面结果汇报标准高是优点 (S6)。Director 判断：双方都有道理——如果能更深入分析 why routing is hard（而非仅报告 inconclusive），空间使用更合理。

---

## Questions（需要作者澄清）

**[Q1]** （R1-Q1）Algorithm 1 中两个策略都 die 但 timing 不同时，是否有 pre-death partial scores 可利用？为什么不比较 death timing？

**[Q2]** （R1-Q2）Label fraction（78.9%）的 95% CI 是多少？论文多处强调 label fraction 是 primary metric 但未报告其 CI。

**[Q3]** （R1-Q3）Reflexion N=3 时 Δ_nd = -0.47（internal 略优于 deterministic in non-death episodes）是否削弱 "deterministic 全面优于 internal" 的叙事？

**[Q4]** （R1-Q5, R2-Q5）Grounding ablation 后重新计算 DAF，death dominance 是否仍成立？如果简单的 action-space filtering 就能大幅削弱 death dominance，"直接用 deterministic" 的建议可能不是最佳策略。

**[Q5]** （R2-Q1）如何 disentangle "death as a cause of routing signal" vs. "death as downstream indicator of reasoning quality"？Appendix N 的 failure categories B 和 D 暗示部分 death 源于 reasoning error 而非 unsafe action。

**[Q6]** （R2-Q3）Frontier models（GPT-4o/Claude 3.5）在 ScienceWorld 上的 death rate 可能大幅降低。是否有 evidence 表明 death avoidance 在 frontier regime 下仍主导？

---

## Missing References

1. **Risk-sensitive RL / CVaR**：Chow et al. (2015), Tamar et al. (2015) — 与 death avoidance 作为 tail-risk avoidance 直接相关（R2-R1/R2）
2. **AgentGym** (Xi et al., 2024) — 多环境 agent 训练基准含 catastrophic failure 场景（R1-R1）
3. **OSWorld** (Xie et al., 2024) — 有不可逆操作的 computer agent 环境，潜在的第二个 death-dominated 验证候选（R1-R2）
4. **Trial-and-Error** (Wang et al., 2024) — LLM agent 在有 catastrophic action 环境中的试错学习，与 death avoidance 分析互补（R1-R3）

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warning, 7 info, 0 critical）。主要发现：

- **[warning] Pages 7-8 连续两页纯文本**，无 figure/table/equation 穿插，审稿人后半段会感到视觉单调。建议在 Discussion 加总结性 figure 或 Related Work 加小表格。
- **[warning] 正文仅 4 个 display items（0.5/页）**，低于实证论文典型 5-8 个。核心分析结果缺可视化支撑，定量结论散落在行内文字中。
- **[warning] 末页（p25）底部约 40% 空白**，低于 2/3 页面利用建议。
- **[info] Figure 1 首页无 display item**，第一个视觉锚点在第 2 页。配色偏素（灰/米色），建议增加对比度。
- **[info] Figure 2 axis label 约 6-7pt**，偏小。
- **[info] 附录 13 页 vs 正文 8 页**（比例 1.6:1），审稿人可能质疑核心内容被挤出正文。
- **[info] 无 LaTeX 渲染错误、未解析引用、margin 溢出。排版合规。**

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

两位 Reviewer 独立达成 3.0 共识。论文是一篇方法论扎实、分析透彻、自我批评诚恳的 diagnostic study。核心贡献——episode-level counterfactual diagnostic framework——简洁可复用，在三个环境中成功诊断出不同 routing mechanism。统计严谨性和 robustness analysis（21 个附录）超出同 venue 平均水平。

但论文面临三个结构性限制：(1) 核心实证发现（death dominance）仅在 ScienceWorld 一个主环境验证，cross-env probes 反证了 generalizability；(2) 在 oracle-privileged 的 deterministic 策略下，death avoidance 主导 routing signal 直觉上可预期，真正非直觉的洞见（Δ_nd≈2.84）未被充分突出；(3) episode-level 诊断框架无法直接指导 step-level routing，实用性受限。

**与 3.5 (Borderline Conference) 的差距**：如果论文能 (a) 在至少一个额外 death-dominated 环境验证（如 OSWorld、NetHack），(b) 将 Δ_nd≈0 的洞见提升为核心发现（而非 DAF 副产品），(c) 扩展 Discussion 包含条件分析和 concurrent work 对话，评分可上调。

**格式合规**：正文 ≤8 页 ✅ | ACL template ✅ | Double-blind ✅ | Limitations section ✅（仅讨论，无新实验） | Ethics Statement ✅ | References 格式正确 ✅

---

## Detailed Comments

### §1 Introduction
- Contribution (2) 将 72B probe 与三个模型族 replication 并列呈现——72B 仅一个模型 (Qwen2.5-72B)，应更明确标注 preliminary 性质
- "Death Avoidance as the Dominant Routing Signal" 标题暗示通用性但 finding 仅在 ScienceWorld 成立

### §2 Method
- DAF 定义数学上干净（Eq. 3-4），但需在 §2.4 更明确区分 accounting decomposition 和 causal mechanism
- "Counterfactual" 术语：论文引用 Pearl (2009) 但实际方法是 matched-seed strategy comparison，非 structural counterfactual reasoning
- SCI 列为框架三大组件之一但正文仅用一次（SCI=0.2147），建议降低 Method 中的显著度

### §3 Experiments
- §3.1 Death Avoidance Decomposition：label fraction (78.9%) 的 CI 应在正文报告（目前只有 DAF CI）
- §3.3 Agent Improvement Baselines：Reflexion Δ_nd<0 的含义值得在正文讨论——暗示 self-correction 改善了 non-death 表现
- §3.4 Cross-Environment：作为 boundary probes 的定位是准确的，但 §1 contribution 措辞可能误导读者认为存在跨环境一致性
- §3.5 Baselines：仅 3 行，作为独立小节不必要——可并入 §3.1
- §3.6 Router Training：负面结果汇报质量高（S6），但缺乏 why routing is hard 的深入分析。半页 "inconclusive" 如果能转化为 actionable insight（如 what minimal signal would need to exist for routing to work）会更有价值

### §4 Related Work
- 缺 risk-sensitive RL / CVaR 文献（Chow 2015, Tamar 2015）和 catastrophic-failure agent environments（AgentGym, OSWorld, Trial-and-Error）
- 与 MTRouter (Zhang et al., 2026c, ACL 2026) 的对比可更深入——MTRouter 是否隐式学会了 death avoidance？

### §5 Discussion
- 仅 ~0.5 page, 2 个话题。建议扩展：(a) 条件分析：在什么条件下 death avoidance 预期会/不会主导？(b) DAF 的 penalty sensitivity 对实际 routing 设计的影响；(c) 与 concurrent work 的 findings 互补关系
- Δ_nd≈2.84 是真正非直觉的洞见，应在 Discussion 中专段讨论而非仅作为 decomposition 的数值结果

### §6 Conclusion
- 简洁但可扩展——future work 仅一句，建议具体化（哪些 death-prone environments？step-level extension 的可行路径？）

### Limitations
- 内容全面、诚实（5 段, ~1.5 页），但对 ARR mandatory limitations 偏长。Pure-strategy upper bound 段落尤其有价值。建议精简至 3 段，将 statistical limitations 的细节移至 Appendix。

### Ethics Statement
- ⚠️ RTX 5090 硬件：需确认是否已公开发售。如果是特定实验室的早期访问，可能泄露作者身份违反 double-blind。

### Appendix
- 21 个 appendix (A-U) 共 15 页。内容丰富但正文对 Appendix 依赖过重。建议将 penalty sensitivity (K) 和 Decision Framework (R) 的核心内容移入正文。