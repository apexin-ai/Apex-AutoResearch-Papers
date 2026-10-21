---
round: 16
overall_score: 3.0 - Findings
timestamp: 2026-05-18T03:33:56.777160+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 16 Consolidated Review Report

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 via ARR May 2026 cycle (Long Paper)
**Reviewers**: R1 (方法严谨性/实验设计/统计推断) + R2 (新颖性/贡献/写作/完整性)
**评审轮次**: Round 16 (1 轮独立审稿 + 1 轮交叉分享，已收敛)

---

## Summary

本文提出 episode-level counterfactual 框架，通过 Death Avoidance Factor (DAF) 和 penalty-independent label fraction 两个互补指标，诊断模块化 LLM agent 中 routing signal 的来源。在 ScienceWorld（11/30 task types, 245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的非 tie routing labels 源于 death asymmetry（penalty-independent），DAF=90.4%（P=100）。Agent improvement baselines（retry, 72B scaling, Reflexion）均未消除 death dominance。MATH (N=795) 确认无 catastrophic failure 时无 routing signal (p=0.81)；ALFWorld (N=135) 识别出 information asymmetry 作为替代机制。

---

## Strengths

**S1. 方法论设计清晰且 self-aware。** Dual-metric 设计（78.9% penalty-independent + DAF 90.4% penalty-dependent）合理。作者正确识别 DAF 对 P 的单调依赖和 r=0.97 的相关是数学性质而非经验发现（§2.4, §3.1），将 78.9% 确立为 primary diagnostic。这种 self-awareness 在审稿中罕见且值得肯定。[R1-S1, R2-S1]

**S2. 负对照规范。** MATH N=795 作为 negative control 非常有效：McNemar p=0.81 严格排除了 ≥3.6pp 的 routing signal（§3.4），从反面验证了框架预测。[R1-S2, R2-S4]

**S3. Robustness 检查系统化。** Bootstrap CI (B=10,000)、LOO correlation (Appendix D)、cross-model pilot (Llama, Appendix H)、agent improvement baselines (§3.3, 三种独立维度)、penalty sensitivity (Appendix G)、data scaling ablation (Appendix F) 构成多层次验证体系。[R1-S3, R2-S2, R2-S5]

**S4. Algorithm 1 设计无 artifact。** Death-priority 与 score-comparison 对所有 death-asymmetry episodes 给出相同 label；78.9% 是真实经验发现，不是 labeling rule artifact。Appendix B labeling quality audit 进一步确认。[R1-S4]

**S5. Negative results 有诊断价值。** Router training 的系统失败分析（step-level vs episode-level generalization gap, data scaling 无效, 1.7B non-monotonic dip, capacity scaling）为 routing 研究社区提供经验教训。[R2-S3]

**S6. 引用覆盖好。** 39 条 bib entries，包括 4 篇 2026 年 concurrent work (tool-overuse-illusion, when2tool, tool-use-tax, to-call-or-not)。Related Work 分段合理，做到归纳比较而非论文堆砌。Safe RL 部分覆盖经典文献。[R2-S6]

**S7. Limitations 诚实具体。** 明确承认 K=11 cluster bootstrap 局限、63% excluded tasks、episode-level mislabeling 27.7%、single backbone。三个 paragraph headers 组织清晰。[R1-S5]

---

## Weaknesses

### Must-Fix (Critical)

**C1. [CONSENSUS] 核心发现 novelty/excitement deficit。**
DAF 公式本身（§2.4: DAF = δP/(δP + Δ_nd)）展示了 death dominance 的算术可预测性：δ=26.6pp, P=100, 0.266×100=26.6 >> 2.84。论文两次承认核心指标是 "mathematical consequence"（§2.4, §3.1）。Discussion §5 的 non-triviality 论证聚焦于 persistence（retry/scaling/Reflexion robustness）而非 surprise value。对于 EMNLP long paper，审稿人期望核心发现超越 back-of-envelope 推导。
- **R1 交叉补充**：agent improvement baselines 的 robustness 是 non-trivial 的（事前未必能预测 Reflexion 只能降到 31.4%），建议 reframing emphasis 从 "death dominates" 转向 "death dominance resists standard interventions"。
- **修改要求**：(1) 核心叙事 reframe 为 "death dominance is robust and resists standard interventions"；(2) 明确引用 concurrent routing work 中隐含的 "diverse routing signal" 假设以建立 contradiction；(3) 强调 δ=26.6pp 的量级和三种干预的 irreducibility 是 empirical surprise。
- *[R1-N3 + R2-N1, 双向 AGREE]*

**C2. [CONSENSUS] Task selection bias: anti-cherry-picking 论证不充分。**
11/30 task types 排除 63%。Appendix C 仅比较 included vs excluded 的 deterministic death rate (17.8% vs 14.9%)，未报告 excluded tasks 的 internal death rate。排除标准 "both strategies time out within 30 steps" 意味着 time-out 是 non-death failure mode；如果 step budget 增加，excluded tasks 可能出现 non-death-dominated routing signal。63% 排除意味着 death dominance 可能仅适用于 ScienceWorld 特定 task subset。
- **修改要求**：(1) 报告 excluded tasks 的 internal death rate；(2) 在正文（非仅 Limitations）明确承认 63% exclusion 是 scope limitation；(3) 如可行：对 2-3 个 excluded tasks 做 T_max=50 pilot。
- *[R1-N1, R2 AGREE]*

**C3. [CONSENSUS] 实验规模和环境多样性不足: 缺少 permadeath 环境 replication。**
论文自认 NetHack 和 Crafter 为 "most direct replication targets"（Discussion, Conclusion）但无实验。MATH 和 ALFWorld 验证 boundary conditions（无 catastrophic death），但最有价值的 validation 是在另一个 permadeath 环境的 positive replication。单一 primary environment + 63% task exclusion + 无 permadeath replication = generalization evidence 严重不足。这是区分 Conference 和 Findings 定位的关键因素。
- **修改要求**：在 NetHack 或 Crafter 上执行 pilot study (N≥50)，或更明确讨论为何未执行及其对 claim scope 的影响。
- *[R2-N2, R1 AGREE]*

**C4. [CONSENSUS] Cross-environment "deterministic" modality 定义不一致。**
三环境的 "deterministic" 质性不同：ScienceWorld = oracle simulator (observation modality), MATH = code interpreter (solving modality), ALFWorld = admissible-action access (information asymmetry)。论文在 §3.5 承认 ALFWorld 是 information asymmetry，但 Table 2 和 Contribution 3 并列对比暗示 comparability。
- **修改要求**：(1) Table 2 caption 逐项注明含义及与 framework 假设的对应；(2) §3.5 增加 1 段 comparability caveats；(3) Contribution 3 弱化为 "boundary probes" 或 "case studies"。
- *[R1-N2, R2 AGREE]*

### Should-Fix (Warning)

**W1. [CONSENSUS] Cluster bootstrap K=11 推断力不足。**
§3.1 将 cluster bootstrap CI [73.3%, 100%] 与 episode-level bootstrap CI [81.6%, 98.8%] 并列，未明确区分 sensitivity analysis vs primary inference。Cameron 2008 的具体 concern (type-I error inflation at small K) 未讨论。
- **修改要求**：明确标注 cluster bootstrap 为 sensitivity analysis；补充 Cameron 2008 的具体 concern；考虑 wild cluster bootstrap。
- *[R1-W1, R2 AGREE]*

**W2. [CONSENSUS] 72B vs 7B DAF 对比基于不同 task population。**
72B N=200 (10 tasks), 7B N=245 (11 tasks)。§3.3 直接比较 DAF (90.9% vs 90.4%) 时未强调 population 差异。
- **修改要求**：DAF 对比注明 population 差异；在相同 11 tasks 上报告 72B DAF；Appendix 补充 72B per-task table。
- *[R1-W2, R2 AGREE]*

**W3. [CONSENSUS] Router 1.7B non-monotonic dip 解释缺乏可检验性。**
Episode-level: 0.6B=50.7%, 1.7B=43.1%, 4B=59.0%。"Memorize but insufficient to generalize" 假设无 per-class confusion matrix 或 training dynamics 支撑。
- **修改要求**：补充 1.7B per-class confusion matrix，或弱化为 observation。
- *[R1-W3, R2 AGREE]*

**W4. [CONSENSUS] Per-task n=20 statistical power 未量化。**
Per-task death rate differentials 未附 CI。n=20 检测 10-15pp 差异的 power 可能不足。
- **修改要求**：Appendix C 补充 per-task death rate differential 95% CI (Wilson/Clopper-Pearson)。
- *[R1-W4, R2 AGREE]*

**W5. [CONSENSUS] Abstract 数字密度偏高。**
~140 词约 12 个数字。Agent improvement 具体数字可概括为定性描述。
- **修改要求**：保留 78.9% 和 MATH p=0.81；agent improvement 数字改为定性概括。
- *[R2-W1, R1 AGREE]*

**W6. [CONSENSUS] signal_reversal.pdf 未引用。**
存在于 figures/ 但未被任何 .tex 引用。该图是 cross-env label distribution 对比图。
- **修改要求**：引入 §3.5 正文（caption 需注明 modality 定义差异），或删除。
- *[R2-W2, R1 AGREE]*

**W7. [CONSENSUS] Contribution 2 过载。**
86 词覆盖 finding + robustness + router diagnostic，缺乏焦点。
- **修改要求**：拆分 router diagnostic 为独立 contribution 或合并到 Contribution 1。
- *[R2-W4, R1 AGREE]*

**W8. [CONSENSUS] Oracle margin vs mislabeling 因果层级可更清晰。**
§3.7 定义了层级但未讨论两者独立性和各自 binding 条件。
- **修改要求**：补充 1-2 句讨论。
- *[R1-W5, R2 AGREE]*

### Minor (Info)

**M1. Appendix C task name 不一致。** "find-non-living" vs "find-non-living-thing"，应统一。[R1 格式检查]

**M2. Responsible NLP Checklist B3。** "implicitly" 可以更直接。[R1 格式检查]

**M3. Introduction vs Abstract 措辞微不一致。** Reflexion 在 Abstract 报具体数字，Introduction 用 hedged 表述。应统一。[R1 Detailed Comments]

---

## Reviewer Consensus

两位 Reviewer 独立给出 **Score = 3.0 (Findings), Confidence = 4/5**，评估高度一致。

交叉回应中共识程度极高：

| 维度 | 共识/分歧 |
|------|----------|
| C1 Novelty deficit | **强共识** (R1-N3 = R2-N1, 双向 AGREE) |
| C2 Task selection bias | **强共识** (R1-N1, R2 AGREE 并补充) |
| C3 Environment diversity | **强共识** (R2-N2, R1 AGREE 并补充) |
| C4 Cross-env modality | **强共识** (R1-N2, R2 AGREE 并补充) |
| W1-W8 所有 warning | **全部共识** |
| Overall score | **完全一致** (3.0 Findings) |

核心判断：**C1 (novelty) + C3 (scope) + C4 (cross-env) 三个 critical issues 互相强化，共同指向 Findings 而非 Conference 的定位。**

## Reviewer Divergence

仅 2 个 minor 分歧，不影响整体结论：

| Issue | R1 | R2 | Director 裁决 |
|-------|----|----|--------------|
| "Structural" claim (R2-W3) | REBUT: 上下文已足够 qualified | warning | **采纳 R1**: Discussion 已弱化为 "robust under tested interventions"。降级为 **info**，不列入 should-fix。 |
| Writing traces (R2-W5) | REBUT: 无 em-dash，证据不足 | warning | **采纳 R1**: R2 未给出具体实例。**删除**。 |

---

## Questions for Authors

1. 19 个 excluded task types 的 internal death rate 是多少？如果 excluded tasks death rate 也高但 routing signal 为零（因 both time out），是否意味着 death 存在本身不足以产生 routing signal，还需 asymmetric death rates？
2. DAF 相比直接比较 death rates 提供了什么额外 actionable information？在已知 δ 和 P 的情况下，DAF 到底增加了什么 new insight？
3. 为什么选择 MATH 和 ALFWorld（均无 catastrophic death）做 cross-env 而非 NetHack/Crafter（自认的 "most direct replication targets"）？
4. MATH "code interpreter" 的具体实现是什么？如果 code 由 LLM 生成，则非纯 deterministic——与 ScienceWorld oracle simulator 存在本质差异。
5. 72B 在相同 11 tasks 上的 DAF 是多少？排除 find-non-living 的对比是否影响结论？
6. 1.7B router 的 per-class confusion matrix（internal recall vs det recall）是什么？是否有证据支持 "memorize but insufficient to generalize"？
7. Episode-level bootstrap 将 245 episodes 视为 i.i.d.，但 episodes within task type 共享 environment dynamics。如何评估 effective sample size？

---

## Missing References

1. **LLM agent 在 permadeath 环境中的工作**（NetHack/Crafter 相关，如存在）。两位 Reviewer 均提及。
2. **Wild cluster bootstrap 方法** (Cameron et al. 2008 变体, Webb 2023)，作为 K<40 时 cluster bootstrap 的改进。
3. **Safety-aware routing / uncertainty-based fallback** 策略文献。

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿（`external_review.paperreview_ai.enabled` 未启用）。无外部审稿结果。

---

## Overall Assessment

**Score: 3.0 (Findings)**
**Confidence: 4/5 (两位 Reviewer 独立一致)**

**总评**：论文提出了一个 well-designed 的 episode-level counterfactual 诊断框架，方法论在其 scope 内 sound，统计分析系统化且具有良好的 self-awareness（正确识别数学性质 vs 经验发现）。Agent improvement baselines 的系统验证和 negative results 有诊断价值。

但存在三个互相强化的核心限制：
1. **Excitement deficit**：核心发现（death dominance at P=100）在事后看来可从 back-of-envelope 预测；论文的 surprise 更多在于 interventions 的 robustness 而非 finding 本身，但叙事未充分 reframe。
2. **Scope limitation**：单一 primary environment (ScienceWorld, 11/30 tasks)，63% task exclusion，无 permadeath 环境 replication。
3. **Cross-env comparability**：三环境的 "deterministic" modality 定义质性不同，Contribution 3 的 diagnostic contrasts 更准确地是 boundary probes。

方法论贡献和分析质量足以支撑 **Findings** 发表。提升至 Conference (3.5+) 需要：(a) 在 NetHack/Crafter 上完成 permadeath 环境 replication；(b) 核心叙事 reframe 为 "death dominance resists standard interventions"；(c) 加强 cross-env comparability 讨论和 task selection bias 论证。

---

## Detailed Comments (按 Section)

### Abstract
- 保留 dual metrics (78.9%, DAF=90.4%)，但 agent improvement 具体数字（42.9%→51%→~35%, 10×, 16.3%）应概括为定性描述。~12 个数字在 ~140 词中密度过高。

### Introduction
- 叙事结构清晰（existing assumption → our question → framework → findings → contributions）。
- Contribution 2 过载（86 词），建议拆分 router diagnostic。
- Contribution 3 的 "preliminary" 限定恰当。
- 末尾 Reflexion 措辞与 Abstract 微不一致，应统一。

### Method (§2)
- Algorithm 1 清晰 self-contained，DAF decomposition 推导清楚，approximation error (0.8%) 明确量化。
- Figure 1 概念性强但信息量有限；可考虑与 label distribution 合并。

### Experiments (§3)
- §3.1: 信息密度高，r=0.97 正确定位为 internal consistency check。Cluster bootstrap CI 需明确标注为 sensitivity analysis。
- §3.3: 72B DAF decomposition 完整是进步。但 population 差异需 flag，per-task breakdown 需补充。
- §3.4: McNemar test 使用恰当，negative result 可量化。
- §3.5: ALFWorld "information asymmetry" observation insightful 但论证过简（2 sentences），建议扩展。Table 2 caption 需标注 modality 定义差异。
- §3.7: Oracle margin vs mislabeling 逻辑层级可更清晰。1.7B dip 需 per-class evidence 或弱化为 observation。

### Related Work
- 结构合理，concurrent work 引用充分。Counterfactual RL 部分较短但已充分区分差异。

### Discussion
- "Non-triviality of death dominance" 是最强论证段落。但 "Scaling predictions" 中 "We predict that in any environment where..." 相对证据过强，建议弱化为 "We conjecture" 或 "Our results suggest"。
- 核心叙事需 reframe：从 "death dominates" 转向 "death dominance resists standard interventions"。

### Limitations
- 诚实且具体。遗漏：未讨论 ScienceWorld -100 penalty 是否是真实部署环境 catastrophic failure 的合理 proxy。

### Appendix
- 内容丰富且在正文中都有引用。Appendix G (Penalty Sensitivity) 特别有价值。

### 格式
- `signal_reversal.pdf` 未引用，应引入或删除。
- Appendix C task name 不一致（find-non-living vs find-non-living-thing）。
- RNL Checklist B3 "implicitly" 可更直接。