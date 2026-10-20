---
round: 6
overall_score: borderline accept
timestamp: 2026-05-15T00:16:27.719138+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6（Fresh Review）

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**目标**: EMNLP 2026 Findings track | ARR deadline: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**外部审稿**: 未启用

---

## Summary

论文提出 episode-level counterfactual analysis 方法诊断模块化 LLM agent 中的 routing signal 组成。在 ScienceWorld 环境中以 Qwen2.5-7B-Instruct 为 backbone，收集 245 个 episode 的 pure-internal 与 pure-deterministic 对照数据，发现在默认 P=100 死亡惩罚下，Death Avoidance Factor (DAF) = 90.41%——即确定性计算的优势约 90% 来自避免 agent 死亡而非正向任务引导。78.9% 的非平局 routing labels 由 death asymmetry 驱动（penalty-independent 指标）。训练的 router 仅达 58.1% balanced accuracy，不显著优于 always-deterministic baseline。

---

## Strengths

1. **实验设计清晰且控制良好**：Pure-internal vs pure-deterministic 的对照设计干净地隔离了变量；episode-level analysis 是对 step-level oracle degeneracy（97.4% tie rate）的合理、well-motivated 回应。[R1, R2 共识]

2. **统计分析深度超出 short paper 平均水平**：Bootstrap CI、Pearson + Spearman 双相关、LOO 逐任务检验、penalty sensitivity analysis、labeling quality audit（Appendix A）——robustness evidence 覆盖面广。[R1 特别肯定: "short paper 标杆"]

3. **Limitations 诚实且全面**：主动讨论 single benchmark、penalty dependence、capability-dependent failure mode、cross-environment evidence 局限，未 overclaim。Cross-environment pilots（MATH, ALFWorld）放在 Limitations 而非 Experiments，体现学术诚信。[R1, R2 共识]

4. **有价值的 community reframing**：从 "when to use tools"（capability matching）到 "how to predict/prevent catastrophic failure"（failure prevention），对 routing/tool-use 研究方向有启发意义。[R1, R2 共识]

5. **可复现性高**（R2 评 4/5）：超参表（Appendix D）、数据划分、环境配置详尽，ScienceWorld + vLLM 均公开可用。

---

## Weaknesses

### Critical（影响接收决定）

**C1. DAF "~90%" headline claim 的 penalty-dependence 在主文中 qualification 严重不足** [R1-N1 + R2-N1, 共识]

DAF(P) = δP / (δP + Δ_nd) 是 P 的单调递增函数，lim_{P→∞} DAF = 1。"~90%" 仅在 P=100 成立；P=10 时 DAF=46.4%，P=200 时 DAF=94.5%。Abstract、Introduction、Conclusion 反复以 "~90%" 为核心 claim，仅加 "under the default −100 death penalty" 轻描淡写。78.9% death-asymmetry label fraction 作为 penalty-independent companion metric 被弱化呈现，且与 DAF 度量维度不同（label count vs score gap）却并置，容易误导。

**要求**: (1) Abstract/Introduction 写出 DAF 随 P 变化的区间（如 "46%–95% across P=10–200"）；(2) 主文（非仅 Appendix）解释 DAF(P) 函数形式；(3) 将 78.9% 提升为 co-equal headline metric。

**C2. Related Work 缺失 counterfactual evaluation/explanation in RL 关键文献** [R2-N2, R1 同意 with nuance]

论文以 "counterfactual" 为标题和核心方法论贡献，但未讨论 RL 领域已有的 counterfactual explanation/evaluation 方法（Explaining RL Agents through Counterfactual Action Outcomes, AAAI 2024; Counterfactual Explanations for RL Agents, AAMAS 2023; Counterfactual state explanations for RL, AIJ 2021; off-policy evaluation 方法族）。论文的方法与这些工作操作上不同（prospective paired comparison vs post-hoc explanation），但 "counterfactual" 一词在标题中出现就有义务 contextualize。

**要求**: 增加 "Counterfactual Evaluation in RL" 段落，精确区分本文的 prospective A/B comparison 与 post-hoc counterfactual explanation。

### Warning（影响评分但不一票否决）

**W1. n=11 数据点的 Pearson r "near-perfect correlation" 声明 inferential power 有限** [R1-N2, R2 同意]

n=11, df=9。LOO 和 bootstrap 缓解 outlier concern，但不解决 structural coupling 问题：death rate differential 和 Δ_full 通过同一个 P 线性耦合，高 r 部分是数学结构产物。R2 补充指出 permutation test 也不解决此问题。

**建议**: 弱化 "near-perfect" 为 "strong positive correlation"；正文承认 n=11 + structural coupling 局限。

**W2. Prescreening 排除 19/30 (63%) task types 的选择偏差未充分讨论** [R1-W1 + R2-W2, 共识]

排除标准合理（both strategies timeout），但 findings 仅适用于模型有基本能力的 task types。被排除 task types 的共同特征（更难？action space 更大？）未分析。增加 step budget 可能改变结论（方向不确定）。

**建议**: (1) 明确 scope qualifier；(2) 简述被排除 task types 特征；(3) 讨论 step budget 敏感性。

**W3. 缺少 failure mode 分析（WHY death avoidance dominates）** [R2-N3 critical, R1 rebut to should-fix; **分歧点**]

论文建立了 WHAT（death avoidance accounts for ~90%）但未分析 WHY（internal strategy 42.9% death rate 的 failure mode 分类、death 的 temporal pattern、trajectory 示例）。

R2 认为 critical：contribution density 不足，finding 在已知 penalty=-100 + death rate 2.6× 后近乎算术推导。R1 反驳：论文定位是 decomposition/quantification 而非 mechanism explanation；death rate differential 的经验量级非先验可知，是真正的 empirical contribution。

**Director 判断**: 降为 warning。论文贡献定位不承诺 mechanism explanation，但添加 death temporal pattern 数据（1-2 句或 appendix）会显著提升 insight 密度。

**W4. Deterministic strategy 信息流操作化描述不足** [R1-W3, R2 rebut confound claim but agrees description issue]

§3.1 "replaces only the state-transition prediction" 不够精确——读者不知 LLM 在两种 mode 下分别看到什么 observation。R2 clarified: "better informed action selection" 是 death avoidance 的实现机制而非独立混淆变量（accurate state → fewer hallucination-induced deaths），但同意操作化描述需加 1-2 句。

**W5. Cross-environment evidence (MATH 50, ALFWorld 135) 力度不足** [R1-W4, R2 同意]

MATH pilot 仅 50 题、无 CI；ALFWorld mechanism 不同（action space pruning vs death avoidance）。若 Conclusion 引用这些证据，至少应为 MATH 报告 CI。

**W6. find-non-living-thing (n=40, zero deaths, Δ=+9.58) 的 implications 讨论不充分** [R2-W4, R1 同意 with nuance]

该 task type 的 per-task DAF=0%（routing signal 完全来自 non-death 因素），与其他 10 个 task types 的 DAF>90% 构成 bimodal 分布。论文虽在 §4.1 提及，但未显式指出这种 heterogeneity。

**W7. Concurrent work 讨论深度不足** [R2-W5, R1 同意]

tool-overuse-illusion 和 tool-use-tax 与本文 "failure prevention vs capability routing" reframing 高度互补，目前仅 one-sentence listing。

**W8. Safe RL 文献覆盖不足** [R2-W1, R1 同意]

仅引 Garcia & Fernandez 2015 综述。需 2024+ safe RL 或 agent failure analysis 参考文献。

### Info（不影响接收）

- **I1**: Bib key 命名与年份不一致（toolformer-2024→2023, retool-2026→2025）
- **I2**: 三个 DAF 数值（~90%, 90.41%, 89.6%）首次出现时未注明计算口径差异
- **I3**: Data split 段位于 §4.3 末尾，位置不常规
- **I4**: Qwen3-1.7B (router) vs Qwen2.5-7B-Instruct (data) 模型选择原因未解释
- **I5**: vLLM 版本号未注明（可复现性）
- **I6**: Table 1 "Trained Router" −10.70 未标注是 best seed 还是 4-seed mean
- **I7**: DAF edge case（Δ_nd < 0 时 DAF > 1）可加脚注说明语义 [R1-W5, R2 降为 info]

---

## Reviewer Consensus [AGREE]

1. **DAF penalty-dependence 是论文最核心的 presentation 问题**——"~90%" 不是 routing signal 的内在属性而是 penalty 选择的产物，需要 reframe [C1, 两位独立发现]
2. **Prescreening 选择偏差需要更透明的讨论** [W2]
3. **Cross-environment evidence 力度有限，但放在 Limitations 的处理是正确的** [W5]
4. **统计分析质量是论文的显著优势** [Strengths]
5. **Limitations section 的诚实度是加分项** [Strengths]
6. **78.9% penalty-independent metric 应被提升**——两位 reviewer 独立建议 [C1]
7. **Counterfactual-in-RL 文献缺失是真实 gap**，但补充后不会削弱 contribution [C2]

## Reviewer Divergence [REBUT]

1. **R2-N3 severity（failure mode analysis）**: R2 标 critical（contribution density 不足），R1 标 should-fix（论文定位是 decomposition 不是 mechanism explanation）。**Director 采纳 R1 立场**——论文的贡献承诺不包含 mechanism explanation，但 temporal pattern 数据作为 bonus 会加分。

2. **§4.3 Router section 空间分配**: R2 建议大幅压缩为一段，R1 反对（该 section 提供 classification head degeneration 作为独立验证、58.1% 不 trivially derivable from DAF、end-to-end evaluation 是 analysis-to-practice 桥梁）。**Director 采纳 R1 立场**——section 有独立证据价值，但可适度修剪 keyword baseline 细节。

3. **R1-W3 deterministic confound vs R2 rebut**: R1 担忧 "better informed action selection" 是独立混淆变量；R2 论证它就是 death avoidance 的实现机制。**Director 采纳 R2 立场**——不是独立混淆变量，但 §3.1 操作化描述确实需要补充。

---

## Questions for Authors

1. 如果将 headline metric 从 DAF 改为 78.9% death-asymmetry fraction（或 dual reporting），核心 narrative 是否需要调整？
2. 105 个 internal 死亡 episode 中，死亡发生在第几步？是否集中在特定 action pattern（如温度操作、容器交互）？
3. find-non-living-thing 的 Δ=+9.58 来自什么具体的 non-death advantage（state tracking accuracy? action coverage?）？
4. 被排除的 19 个 task types 是否有共同特征（action space complexity? 需要更多步数? 需要特定 domain knowledge?）？
5. Router training 用 Qwen3-1.7B 而非 Qwen2.5-7B-Instruct，这一 model mismatch 的设计理由是什么？
6. 如果将 step budget 从 30 增加到 100，被排除的 19 个 task types 中有多少可能产生 non-trivial counterfactual signal？这是否可能改变 DAF 估计？

---

## Missing References

| 文献 | 原因 | 来源 |
|------|------|------|
| Explaining RL Agents through Counterfactual Action Outcomes (AAAI 2024) | 需定位 counterfactual method 贡献 | R2 |
| Counterfactual Explanations for RL Agents (AAMAS 2023) | 同上 | R2 |
| Counterfactual state explanations for RL (AIJ 2021) | 同上 | R2 |
| A Survey of Safe RL and Constrained MDPs (2025) | 论文连接 safe RL 但覆盖不足 | R2 |
| Which Agent Causes Task Failures and When? (ICML 2025) | Agent failure attribution 直接相关 | R2 |
| How Do LLMs Fail In Agentic Scenarios? (arXiv:2512.07497) | LLM agent failure mode 分类 | R2 |
| Constrained MDP / safe exploration (CPO, LAMBDA) | Safe RL 方法论 | R1 |

---

## Overall Assessment

**Score: Borderline Accept（适合 Findings track，需修改）**

**R1**: 3.5/5 (Soundness 4/5, Excitement 3/5)
**R2**: 3.0/5 (Soundness 3/5, Excitement 2/5)
**Consolidated**: 3.25/5

**Confidence**: 4/5（两位 reviewer 均表示高信心）

**理由**: 论文有真实且有价值的 empirical contribution——定量分解 routing signal 并发现 death avoidance 的主导地位，统计分析质量高，实验设计严谨。主要问题集中在 presentation（DAF headline 的 penalty-dependence 需要更显式 qualification）和 positioning（缺失 counterfactual-in-RL 文献），这些都是可修复的。核心 finding 的 surprising 程度中等（R2 concern），但 R1 正确指出 death rate differential 的经验量级非先验可知。对 Findings track 而言，soundness + reproducibility + honest limitations 足以达到 acceptance bar，前提是 C1 和 C2 得到修复。

**修改优先级**:
1. [必做] C1: DAF penalty-dependence reframe + 78.9% 提升
2. [必做] C2: 增加 counterfactual-in-RL 文献段落
3. [强烈建议] W1: 弱化 "near-perfect" 措辞
4. [强烈建议] W2: 扩展 prescreening 讨论
5. [建议] W3-W8: 按优先级逐步改善

---

## Detailed Comments

### Abstract
- "approximately 90% of the routing signal" → 需同时提及 penalty-independent 78.9% 和 DAF 的 P-dependence 区间
- "Death Avoidance Factor" 首次出现即应暗示其 penalty-dependent 性质

### §1 Introduction
- 第 7 段 contribution (1) "identifying step-level oracle degeneracy and applying episode-level counterfactual analysis" → 需在 Related Work 中 contextualize against RL counterfactual literature
- 推荐 dual reporting: "78.9% of non-tie routing labels are driven by death asymmetry (penalty-independent); under the default P=100 death penalty, this translates to a Death Avoidance Factor of 90.41%"

### §3.1 Method - Counterfactual Episode Collection
- "deterministic computation replaces only the state-transition prediction, not action selection" → 补充操作化描述：in deterministic mode, LLM receives ground-truth environment observation string; in internal mode, LLM generates own prediction of next observation

### §3.3 Death Avoidance Factor
- DAF(P) 函数形式应在此出现（目前仅在 Appendix E）
- 首次出现 89.6% 时即时注明与 90.41% 的计算口径差异
- 考虑加脚注讨论 DAF > 1 的 edge case 语义

### §4.1 Death Avoidance Decomposition
- "near-perfect cross-task correlation (r = 0.9698)" → "strong positive cross-task correlation (r = 0.97, n = 11)"
- 补充 1 句 structural coupling caveat
- 指出 per-task DAF 的 bimodal 分布（find-non-living-thing DAF=0% vs others >90%）

### §4.3 Router Training as Diagnostic
- 可适度精简 keyword baseline 细节，释放少量空间
- Table 1 Trained Router 标注 seed 信息
- Data split 段建议前移

### §5 Related Work
- 增加 "Counterfactual Evaluation in RL" 段落 [C2]
- 增加 1-2 篇 2024+ safe RL / agent failure 文献 [W8]
- 扩展 concurrent work 讨论深度 [W7]

### Limitations
- 扩展 prescreening 讨论：被排除 task types 特征、step budget 敏感性 [W2]
- Death temporal pattern 数据（可选 appendix）[W3]
- MATH pilot 加 CI [W5]

### Format
- 修正 bib key 年份 [I1]
- 补充 vLLM 版本号 [I5]
- Router model choice rationale [I4]