---
round: 13
overall_score: 2.5 - Borderline Findings
timestamp: 2026-05-17T14:43:01.484245+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 圆桌审稿报告 — Round 13

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**目标 Venue**: EMNLP 2026（ARR May 2026 cycle）
**ARR 提交截止**: 2026-05-25
**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性 + 写作/格式）

---

## Summary

论文提出 episode-level counterfactual 框架，通过 paired pure-strategy episodes 分析 modular LLM agent 中 routing signal 的来源。核心发现：在 ScienceWorld 的 11 个 task types（245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的 non-tie routing labels 来自 death asymmetry（penalty-independent），DAF=90.4%（penalty-dependent, P=100）。Router 训练（0.6B-4B）无法超越 always-deterministic baseline。Cross-environment contrasts 在 MATH（null result, p=0.81）和 ALFWorld（information asymmetry mechanism）上提供了 boundary conditions。

---

## Strengths

**S1.** 研究问题有价值且定义清晰：「what drives routing signal」是一个被忽视但重要的诊断性问题。大多数 routing 工作假设 diverse signal exists，本文质疑这一假设。[Consensus]

**S2.** 论文的学术诚实度异常高：主动承认 r=0.97 是代数推论（§3.1）、DAF 随 P 单调递增是数学性质（§2.3）、cluster bootstrap K<40 不可靠（§3.1）、augmentation ≠ real data scaling（§3.6, Appendix F）、cross-environment evidence 不是 replication（Discussion）。这种 self-awareness 在 ARR 提交中非常罕见。[Consensus]

**S3.** 统计验证扎实：Bootstrap CI（B=10,000）、LOO robustness（Table 3）、cross-split evaluation（8 seeds, 两个粒度）、McNemar test for MATH null（p=0.81, N=795）。对一篇分析型论文而言，验证工作全面。[Consensus]

**S4.** Negative results 有实际参考价值：Router 无法超越 always-deterministic 的发现，以及 MATH 的 well-powered null result，对 LLM agent routing 实践者有诊断意义。[Consensus]

**S5.** 写作质量良好：无 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无过渡词堆砌），技术写作准确。[Consensus]

**S6.** Appendix 分析深度充实：penalty sensitivity（7 个 P 值）、seed robustness（8 seeds）、per-task decomposition、capacity scaling、cross-model、failure mode、threshold routing。[Consensus]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical] DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调「经验发现」
- **位置**: §2.3 Eq. (3-4), §3.1, Abstract, Introduction
- **问题**: DAF = δP/(δP + Δ_nd)。当 P=100 而 Δ_nd=2.84 时，DAF ≈ 90.3%——这个高值由 P/Δ_nd 比值决定，不是独立经验发现。P=10 时 DAF=50.4%，P=0 时 DAF=7.5%（Appendix E, Table 5）。r=0.97 是 DAF→1 时的数学必然（论文自己承认）。给定 δ=0.265 和 P=100，DAF 的 predicted value = 26.5/(26.5+2.84) = 90.3%，与实测 90.4% 几乎吻合——DAF 分析没有产生超出「知道死亡率差异和惩罚幅度」之外的新信息。
- **penalty-independent 指标更有信息量**: 78.9%（75/95 non-tie labels from death asymmetry）是需要实验才能获得的经验数字，但在叙事中不够突出。Abstract 仍以 DAF=90.4% 为 headline。
- **Action**: 以 78.9% penalty-independent label fraction 为 primary metric，DAF 降级为 supplementary/sensitivity analysis；增加 predictability analysis 量化 predicted vs observed deviation；Abstract/Introduction 降低对 DAF 数值的依赖。
- **Reviewer consensus**: [R1 N1 + R2 N2] 双方 AGREE

**N2** [critical] 统计推断可靠性不足以支撑 claim 的强度
- **位置**: §3.1 (bootstrap CIs), §3.2 (Llama pilot), Appendix B-C
- **问题**:
  - (a) Cluster bootstrap K=11 远低于作者自引的 Cameron et al. (2008) K≥40 门槛。CI [73.3%, 100%] 不可靠，"should be interpreted cautiously" 不足以弥补前提条件不满足的问题。
  - (b) Episode-level bootstrap 假设 245 episodes 独立，但同一 task type 内 episodes 共享 task structure、scoring rubric、环境布局。
  - (c) Per-task 样本量 n=20 极小：chemistry-mix CI [-5.0, 48.6] 跨零，但论文以"10 of 11 types exhibit DAF=100%"呈现结果，掩盖 uncertainty。
  - (d) Llama pilot N=70, 7 tasks, 0 internal-preferred：binomial 95% upper bound ≈ 4.2%，不足以支撑定量结论。
  - (e) 论文 headline 用点估计（90.4%）而非 CI（[81.6%, 98.8%]，width 17pp）叙事。
- **Action**: 对 cluster bootstrap 不可靠性做更诚实讨论或使用替代方法；Llama pilot 降级为 anecdotal evidence，不出现在 Contribution 3；per-task 结果报告时体现 uncertainty；headline 使用 CI。
- **Reviewer consensus**: [R1 N2] R2 AGREE（承认自己 Round 1 遗漏）

**N3** [critical] 跨环境证据不足以支撑 Contribution 3
- **位置**: §3.4-3.5, Introduction Contribution 3, Discussion
- **问题**: 论文声称"cross-environment diagnostic contrasts establishing framework boundary conditions"，但：
  - MATH (N=795) 验证 predicted null（弱检验：任何合理框架都预测无 death penalty → 无 death-driven signal）
  - ALFWorld (N=135) 的 modality 定义根本不同（admissible actions = action space pruning vs ground-truth observations = state estimation），是"information asymmetry rather than computation mode switch"（论文自己承认）
  - Llama pilot (N=70) 样本量过小
  - **最关键缺失**: 无第二个具有 catastrophic failure 的环境（NetHack/Crafter 仅列为 future work）
- **Action**: 降级 Contribution 3 为"preliminary cross-environment evidence"；最理想：增加 NetHack/Crafter 的 quantitative DAF replication。
- **Reviewer consensus**: [R1 N3 + R2 N3] 双方 AGREE

### Should-Fix（影响评分但不一票否决）

**W1** [strong warning] 正文篇幅严重不足 long paper 要求
- 渲染 PDF 正文（§1-§Conclusion）约 5 页，距 8 页限制差约 3 页。大量核心证据（per-task decomposition、penalty sensitivity、capacity scaling、seed robustness）藏在 Appendix。Discussion 仅约 0.5 页。
- R2 列 critical，R1 列 warning。Director 判定：strong warning / borderline critical——严重影响可读性和审稿体验，但属组织结构问题而非方法论缺陷，可通过将关键 Appendix 内容提升至正文修复。
- **Action**: 将 Appendix B/E/F 核心内容纳入正文；大幅扩展 Discussion。
- **Reviewer consensus**: 双方 AGREE（severity 定级有分歧）

**W2** [warning] Router 训练实验存在多个 confound
- (a) Paraphrase augmentation ≠ real data scaling，但 Introduction 仍断言"confirm this is structural rather than data-limited"
- (b) 4B end-to-end N=275 vs baselines N=245，引入 task distribution confound
- (c) 1.7B episode-level 43.1%（低于 0.6B 的 50.7%，Table 4）的 non-monotonic dip 未解释
- **Action**: "data scaling" 改为 "augmentation scaling" 并调整结论；在 shared task set 上统一比较；对 1.7B dip 提供可检验 hypothesis。
- **Reviewer consensus**: [R1 W1 + R2 W6] 双方 AGREE

**W3** [warning] Episode-level label → step-level training 的 mislabeling 未被量化
- 论文承认 episode-level labels 可能对 individual steps 标记不准（Limitations），但未量化规模。估算：42.9% internal 死亡率 × ~19/30 non-terminal steps ≈ 27% step-level labels 可能是 mislabeled。
- **Action**: 计算并报告 "potentially mislabeled step fraction"。
- **Reviewer consensus**: [R1 W2] R2 AGREE

**W4** [warning] SCI（Signal Concentration Index）方法贡献与使用不成比例
- Method §2.4 完整定义但全文仅使用一次（SCI=0.2147）。本质是 Gini coefficient 的 rename，K=11 时估计方差大。"top-3 tasks account for 39.8%"传达相同信息。
- **Action**: 降级 SCI 到 Appendix，主文用描述性语言替代。
- **Reviewer consensus**: [R1 W3 + R2 W3] 双方 AGREE

**W5** [warning] Abstract 数字堆砌
- 约 200 词中嵌入 10+ 统计量，读起来像 results summary 而非 compelling narrative。应减至 5-6 个关键数字。
- **Reviewer consensus**: [R2 W1] R1 AGREE

**W6** [warning] Safe RL 和 LLM agent failure mode 引用覆盖不足
- Safe RL 仅 Garcia 2015 + CRPO 2021，但论文明确将 routing 框架为 safety problem（Discussion）。缺少 constrained MDP（Altman 1999）、CPO、LLM agent failure analysis、Voyager 等引用。
- R1 部分同意（不认为"严重"但承认可补充）；R2 认为较严重。
- **Reviewer consensus**: [R2 W2 + R2 W5] R1 PARTIALLY AGREE

**W7** [warning] Router negative results 解释不完整
- Discussion 缺乏对 router failure 根本原因的深入分析：什么条件下 router 可能有用？更强 internal reasoning（Reflexion）可能改变结论？
- **Reviewer consensus**: [R2 W6] R1 AGREE

---

## Reviewer Consensus

以下问题双方达成完全共识 [AGREE]：
1. DAF=90.4% 和 r=0.97 是环境参数 P=100 的代数后果，不是独立经验发现（N1）
2. 无第二个 catastrophic-failure 环境的 replication 是核心缺陷（N3）
3. SCI 应降级至 Appendix（W4）
4. Abstract 需精简统计量（W5）
5. 写作质量良好，无 AI 痕迹（S5）
6. 学术诚实度异常高（S2）

## Reviewer Divergence

1. **Algorithm 1 形式化程度**: R2 认为 over-formalized（3-case 判断用 8 行伪代码，W4），R1 REBUT——认为是 Contribution 1 的锚点，priority ordering 需要形式化保证 reproducibility。**Director 判定**: R1 的理由更有说服力，Algorithm 1 保留合理，不列为问题。
2. **篇幅问题严重性**: R2 列 critical (N1)，R1 列 warning (W4)。**Director 判定**: 列为 strong warning——组织结构问题而非方法论缺陷，但严重影响审稿体验。
3. **Safe RL 覆盖度**: R2 认为"严重不足"，R1 认为"可补充 1-2 篇"。**Director 判定**: 论文将 routing 框架为 safety problem 但 Safe RL 引用仅 2 篇，需补充但不构成 critical gap。

---

## Questions（需要作者澄清）

**Q1.** 给定已知的 δ=0.265 和 P=100，DAF 的 predicted value = 90.3%，与实测 90.4% 几乎吻合。DAF 分析产生了哪些超出「知道死亡率差异和惩罚幅度」之外的新信息？[R1 + R2]

**Q2.** P=1 时 DAF≈8.5%，此时是否仍能得出"death avoidance is dominant"的结论？如果不能，核心 claim 本质上是关于惩罚幅度而非 routing mechanism。[R2]

**Q3.** 54/75 death-asymmetry labels 移除 death penalty 后变为 tie（both score 0）。这是否说明 30-step budget 对 internal strategy 过于苛刻，而非 routing mechanism 本身的性质？如果增加 step budget，当前发现是否会改变？[R2, R1 agrees]

**Q4.** ALFWorld 的 deterministic modality（admissible actions = action space pruning）与 ScienceWorld（ground-truth observations = state estimation）是根本不同的定义。将两者放在同一 framework 下比较是否存在概念混淆？[R1 + R2]

**Q5.** 1.7B router 的 episode-level 43.1%（显著低于 0.6B 的 50.7%）是否学到了某种反向 spurious correlation？有无可检验的 hypothesis？[R1]

---

## Missing References

**需补充方向（按优先级排序）**：
1. **Voyager** (Wang et al., 2023) — ScienceWorld 上的重要 LLM agent 工作 [R1]
2. **Constrained MDP** (Altman 1999) — 论文将 routing 框架为 safety problem 的理论基础 [R2]
3. **OPE 文献** (Precup et al. 2000, Jiang & Li 2016) — 与 prospective counterfactual evaluation 的方法论对比 [R1]
4. **LLM agent failure analysis** — WebArena/InterCode 中的 agent failure patterns [R2]
5. **Cost-aware routing** — FrugalGPT (Chen et al., 2023) [R2]
6. **Grounded hallucination** — 与 state hallucination → cascading errors 机制相关 [R2]

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Overall Assessment

**综合评分: 2.5（Borderline Findings）**

- **Reviewer 1**: 3.0 (Findings)
- **Reviewer 2**: 2.5 (Borderline Findings)
- **Confidence**: 4/5（两位 Reviewer 均为 4/5）

**评分理由**:

论文提出了一个有价值的诊断性问题（what drives routing signal），设计了合理的 counterfactual 框架，以罕见的学术诚实度呈现了结果。统计验证扎实，写作质量良好。

主要顾虑：
1. **核心发现的经验性贡献被削弱**：DAF=90.4% 和 r=0.97 是 P=100 的代数后果，penalty-independent 的 78.9% 更有信息量但在叙事中未充分突出。给定已知的死亡率差异和惩罚幅度，核心发现的"surprise"有限。
2. **统计推断与 claim 强度不匹配**：cluster bootstrap K=11 不可靠、per-task n=20 CI 极宽、Llama pilot N=70 不足以支撑定量结论。
3. **跨环境证据不构成 framework replication**：无第二个 catastrophic-failure 环境，Contribution 3 的实际证据远弱于其 claim。
4. **正文篇幅不足**：约 5 页 vs 8 页限制，大量核心证据藏在 Appendix。

**R1 给 3.0、R2 给 2.5 的分歧来源**：(1) R1 对 78.9% penalty-independent metric 和 97.4% step-level tie rate 给予更多 credit；(2) R1 认为篇幅是组织问题而非贡献不足；(3) R1 对学术诚实度和 negative results 的加分更高。Director 采纳 2.5 作为 conservative estimate——当前状态下论文需要实质性修改才能达到 Findings 接收标准。

**提升路径**（如果完成以下修改，评分可提升至 3.0-3.5）：
1. 叙事重组：以 78.9% penalty-independent label fraction 为 primary metric，DAF 降级为 supplementary，增加 predictability analysis
2. 将关键 Appendix 内容（per-task decomposition、penalty sensitivity、capacity scaling）纳入正文，填满 8 页限制
3. 降级 Contribution 3 措辞，或增加 NetHack/Crafter 的 catastrophic-failure environment replication
4. 大幅扩展 Discussion：router failure 根本原因、Reflexion 等更强 baseline 的预测、framework applicability boundary
5. 修复统计报告：cluster bootstrap caveat 加强、per-task uncertainty 体现、Llama pilot 降级

---

## Detailed Comments

### §Abstract
- 约 190 词中嵌入 10+ 统计量（78.9%, 75/95, 90.4%, P=100, r=0.97, 59.0%, 4B, N=795, p=0.81, N=135...），信息密度过高。建议精简至 5-6 个关键数字，聚焦"why this matters"。
- 以 DAF=90.4% 为 headline 强化了 tautology 印象。应前置 78.9% penalty-independent finding。

### §1 Introduction
- "a surprisingly concentrated answer"（§1 para 2）：给定 42.9% vs 16.3% 死亡率和 P=100，death dominance 是可预测的，不是"surprising"。
- Contribution 3 的措辞（"establishing framework boundary conditions"）过强——实际是 preliminary evidence。
- 97.4% step-level tie rate 的 methodological insight 有价值，建议更突出。

### §2 Method
- §2.4 SCI 的 formal 定义占用正文空间但仅使用一次，建议降级至 Appendix。
- Algorithm 1 的 death-first priority ordering 对 78.9% metric 有 mechanical 影响（72% 的 death-asymmetry labels 去除 penalty 后变为 tie），论文应更明确讨论这一设计选择。

### §3 Experiments
- §3.1："10 of 11 types exhibit DAF=100%"——掩盖了 per-task n=20 下 CI 极宽的事实。
- §3.1 cluster bootstrap CI [73.3%, 100%]——用自己承认不可靠的方法得出的 CI 来支撑 claim 不严谨。
- §3.4 Llama pilot：Abstract 和 Contribution 3 的 claim 强度与 N=70 的证据强度不匹配。
- §3.5 ALFWorld："information asymmetry rather than computation mode switch"——modality 定义的不可通约性需在正文中更明确讨论。
- §3.6："Data scaling (32×) ablations confirm this is structural"——应改为"augmentation scaling"并降低结论强度。
- §3.6 1.7B dip (43.1%)：需要至少一个可检验的 hypothesis。
- §3.6 4B N=275 vs baselines N=245：应在 shared task set 上统一比较或更好地解释差异。

### §4 Related Work
- Safe RL 段落仅 3 行 2 篇引用，与论文将 routing 框架为 safety problem 的 claim 不匹配。
- 缺少 LLM agent failure mode analysis 和 Voyager 引用。

### §5 Discussion
- 仅约 0.5 页，远不够充分。需扩展：(1) router failure 的根本原因分析；(2) Reflexion/stronger baseline 的预测；(3) framework applicability 的精确边界；(4) DAF 的 P-dependence 的实质含义。

### §Limitations
- "increasing the step budget could surface additional signal"——应量化或至少讨论 step budget 对发现的敏感性。
- Episode-level → step-level mislabeling fraction 应被计算和报告（估算约 27%）。

### Formatting
- Title TeX 源码（"a Dominant"）与渲染 PDF（"the Dominant"）不一致，需统一。
- Figure 3 仅含 ScienceWorld + MATH，缺少 ALFWorld。
- Reference 格式：部分条目使用"and others"而非完整作者列表，需统一。
- 正文约 5 页，需将关键 Appendix 内容纳入正文达到 8 页。
