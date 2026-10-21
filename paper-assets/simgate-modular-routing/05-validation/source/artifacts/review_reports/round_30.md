---
round: 30
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-23T04:08:50.692129+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 30 审稿报告 — simgate-modular-routing

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，核心问题达成共识）

---

## Summary

本文提出 episode-level counterfactual diagnostic framework，用于分析 LLM agent routing signal 的机制组成。在 ScienceWorld 环境（11/30 task types，245 episodes）中发现 78.9% 的 non-tie routing labels 源自 death asymmetry，DAF 在 P=100 下达 90.4%。跨模型复制（3 个 7-9B 模型族，DAF 88-90%）、agent improvement baselines（Retry, Reflexion, 72B）、跨环境探测（MATH 无信号、ALFWorld 信息不对称）提供支撑。Step-level router 训练得到接近随机的结果，框架诊断其原因为 death avoidance 是 task-type-level 二元信号。

## Strengths

**S1. 方法论设计优雅有效。** [R1-S1, R2-S1; AGREE] Per-step oracle 在 sparse-reward 环境下退化为 97.4% 平局率的观察本身是方法论贡献。Episode-level counterfactual comparison 在相同初始条件下运行，干净隔离 computation mode 为唯一变量。"先诊断再构建"的思路填补了 routing 文献中的重要缺口。

**S2. 统计分析严谨且透明度极高。** [R1-S2, R2-S2; AGREE] 21 个 Appendix (A-U) 覆盖 labeling quality audit、cluster bootstrap sensitivity、leave-one-task-out、seed robustness、penalty sensitivity、failure mode analysis、grounding ablation、extended validation 等。对小样本聚类推断局限性（K < 20-50）的诚实披露在 NLP 论文中罕见。

**S3. 跨模型复制令人信服。** [R1-S4, R2-S3; AGREE] 三个架构不同的模型族（Qwen2.5-7B、Llama-3.1-8B、Gemma-2-9B-it）收敛于 DAF 88-90%（spread 仅 2.2pp），10× scaling 到 72B 未消除 death dominance（DAF = 92.4%），有力排除 model-specific 解释。

**S4. Claims 与证据校准审慎。** [R1-S3, R2-S4; AGREE] 论文反复区分 methodological generality 与 empirical generality，将 MATH/ALFWorld 定位为 boundary probes 而非 cross-domain validation，以 label fraction (78.9%) 而非 DAF 作为 primary metric。Limitations 部分（约 1.5 页）极其详尽，自我批判性极强。

**S5. 负面结果的诊断价值。** [R1-S5, R2-S5; AGREE] Router 训练失败被转化为对信号结构的洞察：step-level signal 不存在因为 death avoidance 是 task-type-level 二元信号。两种平衡解释（noise-dominated vs. non-learnability）的呈现方式值得称赞。

**S6. Oracle degeneracy 与 anti-cherry-picking 论证。** [R1-S6, R2-S6; AGREE] Always-deterministic 匹配 96.3% 的 oracle 决策，直接表明 routing 在 ScienceWorld 中价值极低——这本身是重要实证发现。排除的 19 个任务 ΔDR (+38.2pp) 高于包含的 11 个 (+28.7pp)，排除选择性报告嫌疑。

## Weaknesses

### Critical

**C1. 核心发现新颖性受限——death dominance 部分是环境设计的数学必然。** [R1-N1, R2-W1; AGREE]

DAF = δP/(δP + Δ_nd) 在 P=100 >> Δ_nd=2.84 条件下 mechanically >90%——论文自己承认是 "mathematical consequence rather than empirical finding"（§2.4）。78.9% label fraction 虽然 penalty-invariant，但本质上测量"多少比例的 episodes 恰好一方策略死亡"（R1 表述）——比框架暗示的更简单的频率统计。

R1 指出：78.9% 的 non-trivial content 在于 δ=26.6pp（42.9% vs. 16.3%）这个经验事实，但论文未充分论证这一差异为何不可事先预期。论文用大量形式化指标（DAF、SCI）包装了一个相对简单的发现，可能构成 methodological overengineering（R1 用语）。R2 补充：这种防御性写作策略增加了认知负担而未增加新颖性。

真正 non-trivial 的发现——72B 不减少 DAF、Reflexion 使 DAF>100%——在论文中被置于次要位置。两位 Reviewer 均建议将这些发现提前并突出呈现。

**C2. 诊断与处方之间的实际差距限制影响力。** [R1-N2, R2 agrees]

从诊断得出的实际建议——"在 death-dominated 环境中使用 always-deterministic"——是平凡结论，不需要本框架推导。Oracle margin 仅 2.89 分（Table 2: -6.58 vs -9.47），意味着 routing 在 ScienceWorld 中 value 上限极低，进一步削弱了 routing signal 分析的动机。

最具 actionability 的贡献——Decision Framework（Appendix R）和 "50-episode pilot suffices for build-vs-buy decisions"——被埋在 appendix 中。两位 Reviewer 均建议将 Decision Framework 提升到正文 Discussion。

### Warning

**W1. [DIVERGENCE] Deterministic 策略的 oracle 特权使 "routing signal" 解读模糊。** [R2-W2 critical; R1 partially agrees as warning]

ScienceWorld 的 deterministic 策略是 oracle simulator with ground-truth state access——privileged information baseline，非实际可用工具。R2 核心论点：死亡率差异可归因于信息不对称，"routing signal is death-dominated" 可能只是 "information privilege prevents catastrophic errors" 的换一种说法。ALFWorld 分析诊断为 "information asymmetry"（§3.4）——ScienceWorld 是否同样如此？

R1 提供 partial defense：Δ_nd = 2.84（仅 9.6% of full gap）说明 oracle 优势集中在死亡避免上，而非广泛信息优势。框架能区分两种机制（ScienceWorld DAF=90.4% vs. ALFWorld DAF=0%）。

Director 判断：R2 的 concern 有效但 R1 的 Δ_nd 证据提供了部分回应。论文应在正文中更明确讨论此问题。Severity 维持 warning。

**W2. 环境覆盖过窄，跨环境 probes 未复现核心机制。** [R1-W4, R2-W3; AGREE]

MATH 无 routing signal，ALFWorld 信号来源不同——都未复现 death dominance。两个环境都未展示框架将 routing signal decompose 为多种 contributing mechanisms 的能力（R1 表述更精准）。R1 注意到论文标题已限定 ScienceWorld，但 R2 指出至少一个不同 catastrophic-failure 环境（如 NetHack, Crafter）的验证将大幅增强说服力。

**W3. Non-death component (21.1% of labels) 分析不足。** [R2-W4, R1 agrees]

20 个 non-death non-tie labels 的来源未系统分析。仅 Appendix U 一个 case study（find-non-living-thing）。未分析 labels 的分布特征、任务属性关系、score 差异来源（hallucination vs. suboptimal action vs. random variance）。R1 指出对全部 20 个 labels 的 failure mode decomposition 将大幅增强框架 decomposition 价值。

**W4. 72B scaling 证据不足以支撑 "persistent under 10× scaling"。** [R1-W2, R2 agrees]

单一模型（Qwen2.5-72B）、单一 family、未报告 72B DAF bootstrap CI。Introduction 和 Conclusion 中 "persistent under 10× scaling" 过于绝对。建议降级为 "a preliminary 72B probe suggests persistence"。

**W5. Router negative result 可能被 extreme class imbalance 混淆。** [R1-W3, R2 partially agrees]

90.5% det-preferred，仅 9 个 internal-preferred episodes。Text augmentation 无改善和 LOTO 退化到 chance 不能区分 data limitation 和 signal limitation。建议 frame 为 "inconclusive under current data regime"。论文标题 "A Preliminary Negative Result" 已部分 hedge。

**W6. "Deterministic" 术语跨环境含义不一致。** [R2-W8, R1 agrees]

ScienceWorld: ground-truth simulator；MATH: code interpreter；ALFWorld: admissible-action enumeration。三个环境中 "deterministic" 含义完全不同。"Privileged" 或 "oracle-assisted" 更准确，且能引导读者思考信息特权的角色。

**W7. 100% deaths 来自 focus on 单一模式——削弱 "death avoidance" 概念的一般性。** [R2-W7, R1 partially agrees]

Appendix N 确认所有 105 次死亡由同一动作触发。Grounding ablation 降低 death 19pp（Appendix O）。R1 反驳：grounding 后死亡率仍 ~29%（vs. deterministic 16.3%），gap 仍 ~13pp；focus on 在非死亡上下文中是合法操作。但 R2 在交叉回应中指出关键缺失实验：grounding ablation 后重新收集 counterfactual episodes 并计算 DAF——直接测试 "death dominance 是否可通过简单干预消除"。

**W8. Abstract 数字过密，可读性差。** [R2-W5, R1 agrees]

7 个统计量在 ~200 词 abstract 中。Cohen's d=3.02 不应出现在 abstract——需 K=11 context 才能正确解读。建议精简至 2-3 个核心数字。

**W9. Discussion/Conclusion 与 Introduction 重复度高。** [R2-W6, R1 agrees]

78.9% 在论文中重复至少 7 次。Conclusion 仅 3 句，缺前瞻性内容。Discussion 前两段大量重复 Experiments 内容。Conclusion 应提供具体 future work 方向。

### Info

**I1.** 61.2% no-preference base rate 应更突出——routing 仅在 38.8% cases 中 relevant。[R1, R2 agrees]

**I2.** Table 2 Trained Router 用 single seed (42) vs. full episode set，公平性存疑。[R1, R2 agrees]

**I3.** §2.4 DAF 近似 break down 条件未讨论——当 s̄_surv 不远小于 P 时近似误差如何变化。[R1, R2 agrees]

## Reviewer Consensus

以下问题双方明确达成 [AGREE]：

1. **核心发现新颖性受限**（C1）——death dominance 在 P=100 环境中部分是数学/设计后果，论文需更清楚论证 non-triviality
2. **Actionability 不足**（C2）——Decision Framework 应提升到正文，oracle degeneracy 的实际意义需深入讨论
3. **环境覆盖过窄**（W2）——两个 boundary probes 均未复现核心机制
4. **Non-death labels 分析不足**（W3）——21.1% 的非死亡 labels 需系统分析
5. **72B scaling 证据单薄**（W4）——单模型、无 CI，claim 应降级
6. **"Deterministic" 术语误导**（W6）——跨环境含义完全不同
7. **Abstract 数字过密**（W8）——Cohen's d 不适合 abstract
8. **Introduction/Discussion/Conclusion 重复**（W9）
9. **方法论贡献有价值**（S1-S6）——统计严谨性、跨模型复制、透明度均获高度认可

## Reviewer Divergence

**1. Oracle privilege confound（W1）**
- R2 [critical]：deterministic 策略的 oracle 特权使 "routing signal" 与 "information privilege" 不可分离；ScienceWorld 的 death avoidance 可能本质上就是 information asymmetry
- R1 [partially agree, warning]：Δ_nd = 2.84（9.6% of gap）说明 oracle 优势集中在死亡避免而非广泛信息优势；框架能区分两种机制（DAF=90.4% vs. DAF=0%）
- **Director 判断**：R2 的 concern 有效但 R1 的 Δ_nd 证据提供了部分回应。Severity 维持 warning。

**2. Cluster bootstrap K=11**
- R1 [warning]：K=11 低于推荐阈值，Cohen's d=3.02 可能反映 binary structure
- R2 [rebut]：论文已充分处理——§3.1 已推荐 non-clustered CI 为主，Appendix E 有 transparency statement
- **Director 判断**：R2 rebut 有效。不作为报告 weakness 列出。

**3. Excitement 评分**
- R1：3/5（方法论 reuse value + router negative result 信息量）
- R2：2.5/5（actionability 低，结论基本是 "use deterministic"）
- **Director 判断**：倾向 R2——核心发现的 scope 和 impact 确实有限。

## Questions

**Q1.** 包含全部 30 种 ScienceWorld task types 后 label fraction 如何变化？[R1-Q1, R2 agrees important]

**Q2.** 所有 105 次死亡都由 `focus on` 触发——简单 action-level filter 能否替代 router？Grounding ablation 后重新计算 DAF，death dominance 是否仍存在？[R1-Q2/Q3, R2-W7/cross-response]

**Q3.** Gemma-2 排除 find-non-living-thing 后 DAF 从 89.7% 跳到 99.9%——DAF 对单个 zero-death 任务极度敏感？[R2-Q3]

**Q4.** T_max=100 是否能在 excluded tasks 中发现 non-death-dominated signal？[R2-Q4]

**Q5.** Oracle degeneracy（96.3%）是否意味着 ScienceWorld 不适合作为 routing 研究的 testbed？[R1-Q5, R2 agrees sharp and important]

**Q6.** Dense-reward 环境下 framework 是否仍需 episode-level 比较？[R2-Q2]

**Q7.** Task-type classifier 64.7% balanced accuracy——lookup table 足以替代 router？[R2-Q5]

## Missing References

**R2 指出，R1 partially agrees：**
1. **Hallucination detection/mitigation 文献**：核心发现涉及 hallucination-induced catastrophic failure，但 Related Work 完全未讨论（Manakul et al., 2023 "SelfCheckGPT"; Kadavath et al., 2022 "Language models know what they know"）
2. **Non-agent adaptive computation**：early exit networks（DeeBERT, PABEE）、dynamic neural networks survey（Han et al., 2021）完全缺失
3. **LLM 不确定性估计**（Kadavath et al., 2022）：与 step-level death prediction future work 直接相关

**R1 指出：** 无 critical omissions。MoE 和 safe RL 覆盖全面。FrugalGPT、AutoMix 已在 §4 引用。

## External Review (Stanford Agentic Reviewer)

**状态：pending（未返回）**

外部审稿请求已于 2026-05-23T03:44 发出，截至报告提交时尚未收到结果。

## Visual Layout Check（非评分项）

**状态：done**（耗时约 4 分钟，0 critical / 1 warning / 11 info）

主要发现：
- **[warning]** Pages 7-8（Related Work + Discussion/Conclusion）连续 2 页纯文字无 display item，"wall of text" 疲劳感
- **[info]** 主文 8 页仅 4 个 display items（2 figure + 2 table），对实证论文偏低（推荐 5-8），大量数据推到 Appendix
- **[info]** Page 1 无视觉锚点，Figure 1 在 page 2
- **[info]** Figure 2 图面较空（仅 2 条线）
- **[info]** 公式渲染正确，无 overfull hbox，所有表格 booktabs 统一，引用格式统一无未解析

## Overall Assessment

### 评分汇总

| 维度 | R1 | R2 | Director 综合 |
|------|-----|-----|--------------|
| Soundness | 4/5 | 3.5/5 | 3.5/5 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 (Borderline Conference) | 3.0 (Findings) | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | 4/5 |

### Overall: 3.0 (Findings)

方法论框架有价值——episode-level counterfactual decomposition 填补了 routing 文献中"先诊断再构建"的缺口，统计分析严谨程度（21 个 appendix、多层 robustness checks）在同类工作中罕见，跨模型复制（3 个 7-9B 模型族 DAF 88-90%）令人信服。

但三个问题合力将论文限制在 Findings 水准：

1. **核心发现新颖性受限**（C1, 两位 Reviewer 一致同意）：78.9% label fraction 本质上是 death-rate asymmetry 的频率统计，DAF 在 P=100 条件下 mechanically >90%。论文用大量形式化指标包装了一个相对简单的经验观察。虽然 72B 不减少 DAF 和 Reflexion DAF>100% 确实 non-trivial，但这些发现在论文中被置于次要位置。

2. **影响力有限**（C2, 两位 Reviewer 一致同意）：诊断结论（"use always-deterministic"）是平凡的；oracle margin 仅 2.89 分表明 routing 在 ScienceWorld 中价值极低；最具 actionability 的 Decision Framework 被埋在 Appendix R。

3. **环境覆盖过窄**（W2, 两位 Reviewer 一致同意）：实质上只有 ScienceWorld 一个定量发现，两个 boundary probes 都未复现核心机制。框架的 decomposition 能力未得到正面验证。

### 提升路径

修订中如能做到以下 4 点，评分有望提升至 **3.5 (Borderline Conference)**：
1. 将 Decision Framework 提升到正文，强化 actionability 讨论
2. 在 abstract/intro 突出 non-trivial findings（72B persistence、Reflexion DAF>100%、oracle degeneracy）
3. 对 non-death labels 进行系统分析
4. 更明确讨论 oracle privilege confound（突出 Δ_nd=2.84 作为回应证据）

要达到 **4.0 (Conference)** 还需至少一个额外 catastrophic-failure 环境的验证。

## Detailed Comments

### Abstract
- 数字密度过高（7 个统计量），建议精简至 2-3 个核心数字
- Cohen's d=3.02 不应出现在 abstract——需 K=11 context
- "methodological generality" vs. "empirical generality" 区分在 abstract 过于压缩

### Section 1 (Introduction)
- 97.4% per-step tie rate 是好的切入点
- Contributions (1) 和 (2) 区分清楚，但未指明哪个是 primary metric——建议在此处指明 78.9% label fraction 为 primary
- "signal diversity can collapse to a single dominant mechanism" 稍显循环——catastrophic-failure 环境中信号被 catastrophic failure 支配是 expected 的
- 第 3 段（核心发现）和第 5 段（contributions）重复度高

### Section 2 (Method)
- 形式化程度恰当，counterfactual 设计干净
- Algorithm 1 放 Appendix B 合理，但正文应更明确 death-priority rule 的 justification
- DAF 推导清晰，近似 residual (0.8%) 报告增加可信度
- §2.4 末尾 "Scope of episode-level analysis" 段落放在 Method 中节奏不佳，更像 Limitations 内容

### Section 3 (Experiments)
- §3.1: 61.2% no-preference base rate 应更早/更突出——routing 仅在 38.8% cases 中 relevant
- §3.2 (Cross-Model): 论文最强贡献之一
- §3.3 (Agent Improvement): 72B 应标注为 "preliminary probe"，补充 bootstrap CI
- §3.4 (Cross-Environment): 两个 probes 未复现核心机制，降低 generality claim
- §3.5 (Baselines): Oracle degeneracy 96.3% 是重要发现，应获得更多 attention
- §3.6 (Router Training): Frame 为 "inconclusive under current data regime"；添加 summary table

### Section 4 (Related Work)
- 组织合理，5 个 paragraph 覆盖主要方向
- 缺少 hallucination detection/mitigation 文献和 non-agent adaptive computation（early exit 等）

### Section 5 (Discussion)
- "Non-triviality and oracle confound" 有效但不够突出
- "Practical implications" 过于简短——应纳入 Decision Framework（Appendix R）内容
- 缺少对 `focus on` 单一 death trigger 和 grounding ablation 的正面讨论
- 应讨论 death avoidance vs. information privilege 的关系

### Section 6 (Conclusion)
- 仅 3 句话，过于简短
- 应增加具体 future work 方向

### Limitations
- 异常全面（5 个维度，约 1.5 页），"Pure-strategy upper bound" 观点重要

### 格式合规
- **正文 Sections 1-6 在 8 页以内——符合 EMNLP 2026 要求 ✓**
- ACL review 模板 + Anonymous author——符合 double-blind 要求 ✓
- 引用格式统一 ✓