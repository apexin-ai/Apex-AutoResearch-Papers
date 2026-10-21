---
round: 21
review_mode: fresh
overall_score: 3.0-3.5 (Findings to Borderline Conference)
timestamp: 2026-05-19T16:02:24.093419+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告（修订版）：Death Avoidance as the Dominant Routing Signal

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 (Long Paper via ARR)
**Deadline**: 2026-05-25
**Round**: 19 (fresh review)
**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）
**修订原因**: 交叉回应后 Excitement 收敛（R1 3.5→3.0, R2 2.5→3.0）、新增关键共识点

---

## Summary

本文提出 episode-level counterfactual diagnostic framework，将 modular LLM agent 的 routing signal 分解为 death-avoidance 和 non-death 两个成分。在 ScienceWorld（11 task types, 245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的 non-tie routing labels 源于 death asymmetry：internal strategy 因幻觉触发 catastrophic death（−100 penalty），而 deterministic strategy 存活。DAF 在 P=100 下达 90.4%。Cross-model replication（Llama-3.1-8B）、four intervention axes（retry, Reflexion, 72B scaling, action filtering）、cross-environment probes（MATH, ALFWorld）进一步支持诊断。Router 训练（Qwen3 LoRA, 0.6B-4B）step-level 接近 chance，episode-level 仅 4B 有边际改善。

---

## Strengths

**S1. 问题定义精准且有价值。** [R1-S1, R2 交叉后同意] 现有 routing 文献关注"怎么 route"（Toolformer, ART, Chameleon, CogRouter, When2Tool），本文追问"routing 到底在 route 什么信号"——这是一个被忽视的诊断性问题。R2 在交叉回应中承认此贡献有独立价值，将 Excitement 从 2.5 上调至 3.0。

**S2. Pure-strategy counterfactual 设计干净。** [R1-S2, R2-S4, 强共识] 控制相同 random seed + initial conditions，episode-level labeling function（Algorithm 1）death-aware 且 penalty-independent。

**S3. 统计分析超同类水准。** [R1-S4, R2-S1, 强共识] Episode-level bootstrap（B=10,000）、wild cluster bootstrap、per-task CIs、8-seed robustness、Cohen's d=3.02。R1 Reproducibility 4.5/5，R2 4/5。

**S4. Robustness checks 全面。** [强共识] Leave-one-task-out DAF（75.9%-78.9%）、penalty sensitivity（Appendix K）、cross-model replication、anti-cherry-picking analysis（18/19 excluded types 也 death-dominated, ΔDR=+38.2pp）、SCI=0.2147。

**S5. Negative results 诚实呈现。** [R2-S2, 强共识] Router step-level ≈ chance、data augmentation 无效——对社区有价值，呈现坦诚。

**S6. Cross-model validation。** [R2-S5, 共识] Llama-3.1-8B 复制（11 tasks, N=220）direction consistency 10/10，death dominance 跨模型稳定。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [Critical, 强共识] DAF headline framing 误导。**
- R1-N1 首提，R2 完全同意。Abstract 和 §3.1 以 "DAF = 90.4%" 为 headline，掩盖其 penalty-dependent 本质。DAF = δP/(δP + Δ_nd) 随 P 单调递增是数学后果，在 Δ_nd ≈ +2.84 且 P=100 时 DAF 接近 1 是代数必然。78.9% label fraction 才是 penalty-independent 的 robust finding。
- R2 在交叉回应中补充："如果 DAF 是 P 的单调函数且论文没有实际做不同 P 值实验（仅数学推导），那 DAF 的经验价值有限。"
- **Action**: Abstract 以 78.9% 为 primary metric；§3.1 段落重组，DAF 降为 derived quantity；增加 DAF 在 Δ_nd<0 边界行为讨论。

**MF2 [Critical, 部分共识] 核心发现 novelty 不足——"obvious in hindsight"。**
- R2-W1 首提（Critical），R1 部分 REBUT。
- **R1 的辩护**：(1) 78.9% label fraction 是 penalty-independent 的，不能从 P=100 setup 直接推出；(2) 同期 routing 文献（When2Tool, Tool-Use-Tax, RouteLLM 等）全部聚焦 capability matching，无一讨论 catastrophic failure 作为 routing signal——如果 death dominance 真的 obvious，为什么无人验证？
- **R2 的回应**：承认问题定义有独立价值（Excitement 2.5→3.0），但维持 "一个好问题配一个可预见的答案，对 Findings 够，对 main conference 不够"。
- **交叉后状态**：R1 Excitement 3.5→3.0，R2 2.5→3.0，**Excitement 收敛至 3.0/5**。分歧从 1.0 gap 缩小为 0，但 Overall 仍有 0.5 差距（R1: 3.5, R2: 3.0），因为 R1 认为 Soundness+Reproducibility 的高分足以补偿 Excitement。
- **Director 裁决**: 维持 Critical。问题定义的贡献部分缓解了 triviality concern，但 EMNLP reviewer panel 中 excitement deficit 是常见 rejection reason。当前 non-triviality 论证（§5）力度不足。
- **Action**: 三角度强化：(1) routing 文献 prior assumptions 与实证的反差；(2) intervention resistance 的 non-predictability；(3) cross-model δ stability 作为结构性发现。

**MF3 [Critical, 强共识] Framing 内在张力——framework vs finding 定位不清。**
- R2-W2 首提，R1 在交叉回应中完全同意（"论文在 diagnostic framework 和 empirical finding 之间摇摆"）。R1 补充了关键观察："如果选择 framework-centric 路线，novelty 质疑（R2-W1）就会被大幅缓解。"
- **Action**: 选择一个主线贯穿标题/Abstract/Contributions/Conclusion。推荐 framework-centric——既缓解 novelty concern，又对 single-environment scope 更 tolerant。

**MF4 [Critical, 强共识] Cluster bootstrap K=11 低于公认阈值。**
- R1-N2 首提（Critical），R2 在交叉回应中完全同意并补充了额外论据：(1) p=0.002 仅比最小可报告值 (1/2048 ≈ 0.0005) 大 4 倍；(2) `find-non-living-thing` (zero death) 作为 outlier 可能影响 effect size。
- **缓解因素**（R2 同时指出）：多种互补 robustness evidence（8-seed, per-task CIs, exact permutation）共同构成比单一 cluster bootstrap 更强的证据链。两位 reviewer 均认为 "critical-but-partially-mitigated"。
- **Action**: 正文以 non-clustered bootstrap 为主推断；cluster bootstrap 定位为 conservative sensitivity check；增加 K=11 vs K≥40 的显式讨论。

**MF5 [Critical, 强共识] Episode→step label projection 噪声——router diagnostic 价值严重受损。**
- R1-N3 首提（Critical），R2 在交叉回应中称其为 "比论文的解释更有说服力的替代假说"。
- **核心分歧转变**: 论文解读 = "step-level signal 本质上不存在"；R1 替代假说 = "signal 可能存在但被 ~88% noise/uninformative label 淹没"。两位 reviewer 均倾向 R1 解释。
- R2 进一步指出 R1-W2（pure-strategy 外部效度）和 R1-N3 形成 tension：如果 label noise 是 router 失败原因（N3），则 step-level routing 可能 feasible，那 pure-strategy 对比高估 death asymmetry（W2）就更严重。
- **Action**: §3.6 明确区分两种解释；测试 death-proximal labeling baseline（如只用 death event 附近 steps 训练）；或明确声明 router failure 是 label sparsity 而非 fundamental non-learnability。

### Should-Fix（影响评分但不一票否决）

**SF1 [Warning, 强共识] Cross-environment probes 定位过强。**
- R1-W1 和 R2-W3 一致。MATH = unfalsifiable null result，ALFWorld = 不同机制。Abstract "cross-domain probes" 措辞需弱化为 "boundary probes/consistency checks"。

**SF2 [Warning, 共识] 缺少 penalty magnitude 的实际实验验证。**
- R2-W6 首提，R1 在交叉回应中完全同意。Appendix K 的 DAF vs P 是数学推导而非实验。R1 补充：Table 13 显示 P ≤ 25 时 correlation 不显著——"death dominance 是 ScienceWorld 特定 penalty regime 下的现象"。

**SF3 [Warning, 共识] Pure-strategy 设计的外部效度。**
- R1-W2 首提，R2 同意并补充了与 R1-N3 的 tension 关系。

**SF4 [Warning, 强共识] Conclusion 过于简短（2 句话）。**

**SF5 [Warning, 强共识] Safe RL Related Work 不够深入。**
- 缺 CMDP (Altman 1999) 和 risk-sensitive RL 与 death avoidance 的理论映射。

**SF6 [Warning, R2 首提, R1 部分 REBUT] Abstract 数字过密。**
- R1 认为 "每个数字都有明确指代，empirical 论文需要具体数字"。R2 维持 concern。
- **Director 裁决**: 如采用 framework-centric framing，Abstract 可自然减少数字密度（R1 观点）。列为 Should-Fix。

**SF7 [Warning, 强共识] "Modality" 术语歧义。**

**SF8 [Warning, R1 首提] Reflexion dose-response N=5 统计功效不足。**

**SF9 [Warning, 交叉后新增共识] Routing 的 practical value 本身存疑。**
- R1-Q4 首提，R2 在交叉回应中称之为 "devastating observation"。3.7% internal-preferred base rate + 96.3% oracle 选择 always-deterministic → always-deterministic 在实际部署中已接近最优。62% tie rate（R2-M1）进一步支持——大多数 episodes routing 选择无差异。
- **Action**: §5 Discussion 直接面对这个 implication：不仅 "routing signal 被 death avoidance 主导"，更进一步 "routing 在当前 setup 下几乎不必要"——这本身是一个有价值的诊断性结论。

### Minor

**m1 [Info, 共识]** 62% tie rate 含义需在正文讨论。

**m2 [Info, R1]** Figure 2 caption 报告 Spearman's ρ。

**m3 [Info, 强共识]** `webb-2023` 年份需确认（2014 WP vs 2023 journal）。

**m4 [Info, R1]** Appendix R 阈值选择缺理论依据。

**m5 [Info, R2]** AI assistants disclosure 建议更具体。

**m6 [Info, 共识]** Missing references: Altman (1999) CMDP, Mihatsch & Neuneier (2002), Natarajan et al. (2013) noisy label learning。

**m7 [Info, R1]** Table 1 weighting scheme（episode-weighted vs task-weighted）需明确。

---

## Questions（需要作者澄清）

**Q1.** [R1-Q1, R2-W6] DAF 公式假设 Δ_nd 不随 P 变化——是否在 P≠100 的 ScienceWorld 变体上做过实际验证？Appendix K 是数学推导还是实际实验？

**Q2.** [R1-Q2, R2-Q4, 强共识] 105 internal deaths 全来自 `focus on [object]` 误用——death avoidance 是否等价于 single-action bug avoidance？Grounding ablation 降至 29%，residual gap ≥12pp。如果修复该 pattern，death dominance 是否消失？

**Q3.** [R2-Q2, SF9] 62% tie rate + 3.7% internal-preferred base rate → routing 在大多数情况下无差异，always-deterministic 接近最优。论文如何看待这一 observation 对 routing 价值的影响？

**Q4.** [R1-N3, 强共识] Router near-chance accuracy 是因为 death signal 本质上不是 step-level 的，还是因为 episode-level labels 投射到 steps 时 ~88% noise/uninformative rate？是否考虑过 death-proximal labeling（只用 death event 附近 steps 训练）？

**Q5.** [R1-Q5] Llama cross-model replication 的完整 DAF 是多少？"intact" 太模糊，需要具体数字。

**Q6.** [R2-Q3] SCI=0.2147 但 top-3 task types 占 39.8% total death-rate differential——death dominance 是 task-type specific 还是 environment-wide？

---

## Missing References

- **Altman, E. (1999). Constrained Markov Decision Processes.** Death avoidance 作为 implicit constraint 的理论对应。[R2, R1 同意]
- **Mihatsch & Neuneier (2002). Risk-sensitive RL.** 与 catastrophic failure avoidance 直接相关。[R2, R1 同意]
- **Natarajan et al. (2013). Learning with Noisy Labels.** 为 ~88% uninformative label rate 下的 router near-chance accuracy 提供理论 grounding。[R1, R2 同意]

---

## External Review (Stanford Agentic Reviewer)

**状态**: 已跳过（用户选择不提交）。

---

## Visual Layout Check（非评分项）

**状态**: 超时（elapsed 727s）。无排版审查结果。

**基于 PDF 阅读的基本格式确认**:
- ✅ 正文 8 页（§1-§6 在 p1-p8），符合 ≤8 页要求
- ✅ Limitations（p8-9），具体且坦诚
- ✅ Ethics Statement（p9）
- ✅ Double-blind: "Anonymous ACL submission"
- ✅ ACL 模板 + [review] option
- ✅ Figures/Tables 位置合理
- ⚠️ webb-2023 年份需确认

---

## Reviewer Consensus（交叉回应后最终状态）

### 完全收敛
| 议题 | R1 | R2 | 状态 |
|------|----|----|------|
| DAF headline framing (MF1) | Critical | Critical | ✅ 强共识 |
| K=11 cluster bootstrap (MF4) | Critical | Agrees (critical-but-mitigated) | ✅ 共识 |
| Episode→step noise (MF5) | Critical | Agrees ("更有说服力") | ✅ 强共识 |
| Framing tension (MF3) | Agrees | Critical | ✅ 强共识 |
| Cross-env overclaimed (SF1) | Should-Fix | Critical→Should-Fix | ✅ 共识 |
| Routing practical value (SF9) | Q4 ("devastating") | Agrees | ✅ 强共识（交叉后新增） |
| **Excitement** | **3.5→3.0** | **2.5→3.0** | **✅ 收敛至 3.0** |
| Soundness | 3.5 | 3.5 | ✅ 一致 |
| Reproducibility | 4.5 | 4 | ✅ 基本一致 |

### 残余分歧
| 议题 | R1 | R2 | 差异 |
|------|----|----|------|
| **Overall Score** | **3.5** (Borderline Conference) | **3.0** (Findings) | **0.5 gap** |
| Abstract density (SF6) | REBUT | Should-Fix | 主观分歧 |

**0.5 分残余差距根源**: R1 认为 Soundness 3.5 + Reproducibility 4.5 的高分足以在 Excitement 3.0 下支撑 Borderline Conference；R2 认为 Excitement 3.0 的 novelty ceiling 决定了 Findings 更合适。两者均为合理的 reviewer perspective。

---

## Overall Assessment

**Overall Score: 3.0–3.5（Findings 至 Borderline Conference）**

**维度汇总（交叉回应后最终值）**:
| 维度 | R1 (调整后) | R2 (调整后) | 综合 |
|------|------------|------------|------|
| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |
| Excitement | **3.0/5** | **3.0/5** | **3.0/5** |
| Reproducibility | 4.5/5 | 4/5 | **4.25/5** |
| Clarity | — | 3/5 | **3/5** |

**综合评估**:

论文问了一个重要且被忽视的诊断性问题，给出了清晰的回答，counterfactual 设计干净，统计分析超过同类水准，robustness checks 全面，negative results 诚实呈现。

核心问题：
1. **DAF framing 误导**（MF1）——低成本修复
2. **Novelty 受限但非 trivial**（MF2）——Excitement 收敛至 3.0，问题定义有价值但答案可预见性限制了 ceiling
3. **Framing 不统一**（MF3）——需选择 framework-centric 或 finding-centric 主线
4. **K=11 统计推断**（MF4）——通过 non-clustered bootstrap 为主推断来缓解
5. **Router diagnostic 受 label noise 污染**（MF5）——需区分 label noise vs fundamental non-learnability
6. **Routing 的 practical value 本身存疑**（SF9, 交叉后新增强共识）——3.7% internal-preferred + 62% ties → always-deterministic 几乎最优

**Revision 路径**:
- **提升至 Conference (3.5-4.0) 的条件**: (1) 选择 framework-centric framing（同时缓解 MF2 和 MF3）；(2) K=11 辩护充分（MF4，低难度）；(3) DAF framing 修正（MF1，低难度）；(4) death-proximal labeling baseline 或 clear attribution（MF5）；(5) §5 直面 routing practical value 问题（SF9）
- **如果 MF2 (novelty) 和 SF9 (routing value) 无法有效回应，更可能落在 Findings (3.0)**

---

## Detailed Comments

### Title & Abstract
- 标题聚焦 finding 但 Contribution 1 是 framework——需统一（MF3）
- Abstract 以 78.9% 为 primary，DAF 降为补充（MF1）
- 如采用 framework-centric framing，数字密度可自然降低（SF6）

### §1 Introduction
- 问题定义清晰，逻辑链通畅
- Contributions 列表需重组以匹配选定的 framing 主线

### §2 Method
- 写作最清晰的部分
- Algorithm 1 设计合理
- §2.4 Scope of episode-level analysis 段需更强调 episode→step gap implications
- DAF 需更 upfront 承认是 derived quantity

### §3 Experiments
- §3.1 核心实证清晰，但段落结构需修正（78.9% 先于 DAF）
- §3.2 Cross-model 缺 Llama DAF 具体数字
- §3.3 Agent improvement 有价值；72B DAF=92.4% 说明 scaling 不消除 death dominance
- §3.4 Cross-env 过于浅显，需重定位为 boundary probes
- §3.5 Oracle degeneracy (96.3% always-det) 和 3.7% internal-preferred 需更突出讨论
- §3.6 Router 应明确框架为 negative result；区分 label noise vs signal non-learnability

### §4 Related Work
- Tool Use / Adaptive Routing 覆盖充分
- **Safe RL 需扩展**——补 CMDP, risk-sensitive RL 理论连接

### §5 Discussion
- "Non-triviality" 论证力度不足（MF2 核心）
- "Anatomy of catastrophic failure"——105 deaths 全来自 `focus on`，implications 需更深讨论
- **需新增**: routing practical value 的直接讨论（SF9）
- **需新增**: pure-strategy vs mixed-strategy gap 估计（SF3）

### §6 Conclusion
- 严重不足——2 句话，需扩展至 ~0.5 页

### Limitations
- 覆盖面 adequate，但缺 "P=100 specific" 限制的明确讨论

### 格式合规
- ✅ 正文 8 页 | ✅ Limitations | ✅ Ethics | ✅ Double-blind | ✅ ACL template
- ⚠️ webb-2023 年份 | ⚠️ modality 术语