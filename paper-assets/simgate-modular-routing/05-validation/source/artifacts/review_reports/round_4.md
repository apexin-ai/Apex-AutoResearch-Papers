---
round: 4
overall_score: borderline
timestamp: 2026-05-14T19:58:32.120735+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 4 (Fresh Cycle)

**Paper**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 · ARR Short Paper · Deadline 2026-05-25
**Reviewers**: R1 (方法严谨性, 3.0/5) + R2 (新颖性与完整性, 3.0/5)
**交叉回应**: 完成。关键问题达成共识，1 轮收敛。

---

## Summary

本文提出 episode-level counterfactual analysis 方法，在 ScienceWorld 上对比纯内部推理（ReAct, Qwen2.5-7B-Instruct）和纯确定性计算策略的 episode 结果，生成 per-episode routing labels。核心发现：Death Avoidance Factor (DAF) = 90.41%——确定性策略优势中约 90% 源于避免 agent 死亡而非正面任务引导。Per-task 相关分析 (r=0.9698, n=11)、oracle degeneracy (96.3%)、penalty sensitivity analysis 提供了多角度支持。训练的 router 未能显著超越 always-deterministic baseline。

---

## Strengths

**S1. 问题切入精准** [R1, R2 共识]：97.4% step-level tie rate 的观察直接且有力地论证了 episode-level analysis 的必要性。从"routing 该怎么做"退回到"routing 到底在学什么"的 diagnostic 视角对社区有价值。

**S2. 实验设计干净** [R1, R2 共识]：Same seed + same task variation 的严格控制确保公平 counterfactual 比较。四类 episode labeling (death asymmetry / both dead / score comparison / tied alive) 互斥穷尽，逻辑清晰。Appendix A 的 oracle circularity audit 增强可信度。

**S3. 多角度分析，信息密度高** [R1, R2 共识]：短文篇幅内提供了 DAF decomposition、per-task correlation (r=0.9698)、oracle degeneracy (96.3%)、penalty sensitivity (P=10→200)、labeling quality audit——对于 4 页正文已经是高密度。

**S4. 诚实的 negative result** [R2]：Router 无法超越 always-deterministic 的结果被坦诚报告，定位为 diagnostic 而非系统提案，避免了过度包装。

**S5. Concurrent work 定位准确** [R1, R2 共识]：与 tool-overuse-illusion、when2tool、tool-use-tax、to-call-or-not 四篇 2026 并行工作的关系阐述清晰，Related Work 全面且 up-to-date。

**S6. Sensitivity analysis 透明** [R1]：Appendix D 主动暴露 DAF 对 penalty 的依赖关系（P=10→46.4%, P=100→89.6%, P=200→94.5%）。

**S7. 跨环境初步验证** [R1]：ALFWorld + MATH pilot 虽不严格，但对 short paper 是合理补充。ALFWorld 的 mechanism 区分（action space pruning vs death avoidance）诚实。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[CONSENSUS] W1: DAF "~90%" headline claim 需 penalty 条件限定 + penalty-independent metric**
- Severity: **Critical** | R1 W2 + R2 N1 | 交叉：双方 AGREE
- DAF = 1 − Δ_nd/Δ_full，其中 Δ_full 与 penalty P 线性相关。DAF 是 P 的单调递增函数——这是代数必然，非经验发现。P=10→46.4%, P=100→89.6%, P=200→94.5%（Appendix D）。但 Abstract 和 Conclusion 以"approximately 90%"为核心卖点，未附 penalty 条件。读者易将"90%"误读为环境内在属性。
- **修改要求**：(1) Abstract/Conclusion 明确 "under the default P=100 penalty"；(2) 正文（非仅 appendix）讨论 DAF 与 P 的关系；(3) 报告 penalty-independent metric——death-asymmetry episodes 占非 tie episodes 比例 = **75/95 = 78.9%**（注：R2 纠正了 R1 的 86/95 计算——86 含 score-comparison det-preferred，death-asymmetry 仅 75）。78.9% 仍支持 "dominant" 但比 "~90%" 弱一档，且不依赖 P。

**[CONSENSUS] W2: Pearson r=0.9698 (n=11) 统计效力不足**
- Severity: **Critical** | R1 W1 | 交叉：R2 AGREE
- r 基于 11 个 task type 聚合数据点。n=11 下 Pearson r 对杠杆点极敏感——`find-non-living` 是唯一零死亡任务，在散点图中空间分离明显。假设检验依赖双变量正态性，n=11 无法可靠验证。未报告 Spearman rank correlation、leave-one-out stability、r 的 bootstrap CI。
- **修改要求**：(1) 报告 Spearman ρ 作为 robustness check；(2) 对 r 做 bootstrap CI；(3) 报告 leave-one-out analysis（逐一移除每个 task type 后 r 的变化范围）。

### Should-Fix（影响评分）

**[CONSENSUS] W3: Router diagnostic (§3.3) 无法区分 "signal thin" vs "data insufficient"**
- Severity: **Major** | R1 W3 | 交叉：R2 部分 REBUT（有结构必要但需 caveat）
- 81 train / 14 val episodes 远远不够。Classification head 退化为 always-det (0% internal recall)；implicit router 65.4% accuracy **低于 majority-class baseline (~90.5%)**；cross-seed balanced accuracy 57-59% + internal recall 51.5-81.8% 剧烈波动。论文将此解读为 "routing signal structurally thin"，但 equally plausible 的解释是训练数据太少。
- R2 认为 §3.3 有结构必要（回答 "labels 能否训练 router"），但两位一致要求明确加入 data-insufficiency caveat。
- **修改要求**：(1) 明确承认 81-sample 固有局限；(2) "fails to outperform" 改为基于 CI 重叠的更谨慎措辞；(3) 考虑 random-label null baseline。

**[CONSENSUS] W4: 单模型 backbone (Qwen2.5-7B-Instruct) 的外部效度**
- Severity: **Major** | R2 W2 | 交叉：R1 AGREE
- 更强模型（70B / reasoning-specialized）的内部策略死亡率可能显著低于 42.9% → DAF 下降。无法区分 "death avoidance 是 routing 内在结构" vs "7B 模型 hallucination 频率高导致的 artifact"。Limitations 已提及但未讨论含义。
- **修改要求**：Limitations 增加 explicit 讨论——model scaling 对 DAF 影响方向（stronger model → lower death rate → lower DAF → death avoidance may not remain dominant）。

**[DIVERGENCE] W5: 方法论贡献 (contribution 1) framing 过强**
- Severity: R2 标 **Critical**, R1 降为 **Minor** | R2 N2 | 交叉：R1 REBUT
- R2：Episode-level comparison 是 RL 标准 policy evaluation 方法；DAF 是简单代数变换。不构成独立方法论贡献。
- R1 反驳：Findings track novelty bar 更低；核心贡献在于 diagnostic narrative（step-level degeneracy 发现 + DAF decomposition + router failure），措辞调整即可。
- **Director 判断**：R1 反驳有理——Findings paper 价值在于 empirical insight。但贡献声明 "(1) an episode-level counterfactual methodology" 确实 overclaim。**Severity: Major**（需改措辞但非 rejection 理由）。
- **修改要求**：Contribution (1) reframe 为 "identifying step-level oracle degeneracy in sparse-reward environments and applying counterfactual analysis to diagnose routing signal composition"。

### Minor Issues

**[CONSENSUS] W6: Δ_nd 符号不一致**（正文 2.84 vs Appendix D 3.07）
- 同一符号 Δ_nd 两种操作定义。此问题在 Round 3 (R3-CR1) 已提出但仍未修复。建议 Appendix D 用 Δ'_nd。

**[CONSENSUS] W7: Conclusion "58.1%" vs §3.3 "59.3%"**
- 两位独立发现。推测来自不同 cross-seed 运行。需统一为同一口径。

**[CONSENSUS] W8: ALFWorld Conclusion 措辞过强**
- "consistent with death avoidance as a general pattern" 不准确（ALFWorld mechanism 为 action space pruning）。应改为 "consistent with catastrophic failure prevention being a cross-environment phenomenon, though the specific mechanism varies"。

**[CONSENSUS] W9: Prescreening scope**
- 30→11 task types (63% excluded)。正文仅 "After prescreening" 一句。Limitations 应显式讨论排除比例和潜在 scope 限制。

**[CONSENSUS] W10: 可复现性细节不完整**
- Classification head: learning rate, optimizer, epochs 未报告。Implicit router: learning rate, training steps, scheduler 未报告。Prompt templates 未附。无代码/数据公开承诺。

**其他小问题**（两位 Reviewer 一致同意）：
- §2.1 "perfect world model" → "perfect dynamics model"（前者暗示含 reward model）
- `toolformer-2024` bib key 标 2024 但实为 NeurIPS 2023
- `dynathink-2025` first author 可能 mismatch（bib: "Yu, Xiao" vs OpenAlex），需核实
- "97.4% of steps yield tied outcomes" 计算范围未明确（全 30 task types or prescreened 11?）

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题达成 **强共识**：
1. ✅ DAF headline claim 需 penalty 条件限定 + penalty-independent metric (75/95=78.9%)
2. ✅ Pearson r (n=11) 需 Spearman/LOO/bootstrap robustness verification
3. ✅ Router diagnostic 需 data-insufficiency caveat + 措辞谨慎化
4. ✅ 单模型外部效度需更深入讨论
5. ✅ 数值不一致（Δ_nd 符号 + 58.1%/59.3%）需修复
6. ✅ ALFWorld Conclusion 措辞过强
7. ✅ 整体评分一致：3.0 / Findings

## Reviewer Divergence

1. **方法论新颖性 severity**: R2 标 critical（RL 标准方法，不构成贡献），R1 降为 minor（Findings track 低 novelty bar，措辞调整即可）。**Director 判断**：Major——需修改贡献措辞，但 Findings paper 无需方法论创新，不构成 rejection 理由。
2. **核心发现可预见性**: R2 认为 DAF 几乎可从描述统计直接推导，R1 反驳需要 Δ_nd≈0 的先验知识（而这恰是论文核心发现）。**Director 判断**：R1 论点更有力——死亡率差异无法预测非死亡场景下的 performance gap，DAF 的分解价值在于揭示 Δ_nd 的大小。
3. **Death-asymmetry ratio 计算**: R1 给出 86/95=90.5%（所有 det-preferred），R2 纠正为 75/95=78.9%（仅 death-asymmetry labels，排除 score-comparison）。**R2 正确**（Appendix A 明确：75 death-asymmetry + 20 score-comparison = 95 total non-tie）。

---

## Questions（需作者澄清）

1. Figure 1 的 Pearson r=0.9698 做 leave-one-out analysis 后最低 r 是多少？`find-non-living` 是否为高杠杆点？
2. Implicit router 65.4% accuracy 是否低于 majority-class baseline (~90.5%)？如果是，router diagnostic 的解读应如何调整？
3. Both-dead episodes (n=35) 中，两种策略的 survival duration 是否有系统性差异？当前分析是否丢弃了有用信息？
4. 请提供 penalty-independent metric：death-asymmetry labels 占非 tie labels 比例（预计 75/95=78.9%）。
5. "97.4% of steps yield tied outcomes" 的计算基于全 30 task types 还是 prescreened 11 types？
6. 更强模型（如 70B）下，预期 DAF 是否仍 >50%？如果 DAF 随模型能力提升而下降，核心 claim 应如何解读？
7. Conclusion "near-random trained-router accuracy (58.1%)" vs §3.3 "balanced accuracy 59.3%"——哪个正确？来自什么口径？

---

## Missing References

两位 Reviewer 一致建议：
1. **Safe exploration / constrained RL in LLM agents**: 论文已引 Garcia & Fernández (2015) 综述，但缺少近年将 safety constraints 应用于 LLM agent 的工作（2024-2026 SafeAgentBench 类，如有）。
2. **Temporal credit assignment 文献**: 论文的核心 motivation 之一是 episode-level vs step-level labeling。Hindsight experience replay 等 credit assignment 文献可强化 motivation section。

---

## External Review (Stanford Agentic Reviewer)

项目未配置外部审稿（paperreview.ai），本轮无外部审稿结果。

---

## Overall Assessment

**Overall Score: Borderline (3.0/5)**
**Confidence: High (4/5)**
**建议 Track: Findings**

**两位 Reviewer 评分**：R1 = 3.0 (Findings / Weak Accept), R2 = 3.0 (Borderline / Findings acceptance)

**理由**：

本文是一篇干净的分析性短文，提出了有社区价值的 diagnostic insight——在 ScienceWorld 的 modular routing 中，death avoidance 是压倒性的 routing signal 来源。实验设计严谨（same seed counterfactual），labeling 方案逻辑清晰（四类互斥穷尽），negative result 表述诚实（router 无法超越 always-deterministic），信息密度在 4 页正文中很高。

但存在以下核心限制：
1. **DAF headline claim 过强**："~90%" 是 P=100 的产物，P=10 时仅 46.4%。Penalty-independent 的 death-asymmetry episode ratio 为 78.9%——仍支持 "dominant" 但弱一档，且更稳健。
2. **统计 robustness 不足**：n=11 Pearson r 未经 LOO/Spearman 验证；14 val episodes 的 router evaluation 统计功效低。
3. **单环境 + 单模型**：ScienceWorld + Qwen2.5-7B-Instruct 无法确立 generalization。更强模型可能大幅降低 DAF。
4. **方法论贡献 overclaim**：Episode-level comparison 在 RL 中非新方法，contribution (1) 措辞需调整。

**修改后可接收条件**：如果 W1（penalty qualification + 78.9% metric）、W2（Pearson robustness）、W5（贡献 reframing）得到妥善修改，本文适合 Findings track 录用。核心发现对 modular agent 设计有实践参考价值——告诉社区 routing 的主要价值可能在于 catastrophic failure prevention 而非正向任务引导。

---

## Detailed Comments（逐节）

### Abstract
- "approximately 90%" 需加 penalty 条件 "under the default −100 death penalty"
- 考虑同时报告 78.9% death-asymmetry episode ratio

### §1 Introduction
- 97.4% step-tie 观察是最强 motivation，保留
- Contribution (1) "an episode-level counterfactual methodology" → "identifying step-level oracle degeneracy and applying counterfactual analysis to diagnose routing signal composition"

### §2 Method
- §2.1: "equivalent to a perfect world model" → "perfect dynamics model"
- §2.1: 明确 prescreening 排除了 19/30 task types 及原因
- §2.3: DAF 与 P 的关系应在正文讨论（当前仅 appendix 提及），引入 75/95 companion metric

### §3 Experiments
- §3.1: 补充 Spearman ρ 和 LOO analysis for r=0.9698
- §3.3: 明确承认 81-sample training + 14-sample validation 的固有局限
- §3.3: "fails to outperform" → "does not statistically outperform (overlapping 95% CIs)"
- §3.3: 明确 65.4% 低于 majority-class baseline 的含义

### §4 Related Work
- 考虑增加 safe exploration in LLM agents 引用和 temporal credit assignment 引用

### Limitations
- 增加 prescreening scope 讨论（30→11, 63% excluded）
- 增加 model scaling 对 DAF 影响方向的 explicit 讨论
- "97.4% tied" 明确计算范围

### Conclusion
- "58.1%" → 统一为 §3.3 的 "59.3%"
- ALFWorld 措辞调整："catastrophic failure prevention is cross-environment, though the specific mechanism varies"

### Appendix
- Appendix D: Δ_nd 用不同符号（如 Δ'_nd）区分两种计算口径
- Appendix C: 补充 classification head 和 implicit router 的 hyperparameter table
- 考虑增加 ALFWorld/MATH 实验细节 appendix

### Bibliography
- `toolformer-2024` key → 实为 NeurIPS 2023
- `dynathink-2025` first author 核实