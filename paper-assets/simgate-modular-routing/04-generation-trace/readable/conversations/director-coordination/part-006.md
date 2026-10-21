# Director coordination — Part 6 of 9

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/53/532e22af863d2a24e206.json)

## Round 144

### Tool call

_source line 1742 · 2026-05-19T15:59:10.020321+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "report": "# 审稿报告：Death Avoidance as the Dominant Routing Signal\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 (Long Paper via ARR)\n**Deadline**: 2026-05-25\n**Round**: 19 (fresh review)\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，将 modular LLM agent 的 routing signal 分解为 death-avoidance 和 non-death 两个成分。在 ScienceWorld（11 task types, 245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的 non-tie routing labels 源于 death asymmetry：internal strategy 因幻觉触发 catastrophic death（−100 penalty），而 deterministic strategy 存活。DAF 在 P=100 下达 90.4%。Cross-model replication（Llama-3.1-8B）、four intervention axes（retry, Reflexion, 72B scaling, action filtering）、cross-environment probes（MATH, ALFWorld）进一步支持诊断。Router 训练（Qwen3 LoRA, 0.6B-4B）step-level 接近 chance，episode-level 仅 4B 有边际改善。\n\n---\n\n## Strengths\n\n**S1. 问题定义精准且有价值。** [R1-S1, 共识] 现有 routing 文献关注\"怎么 route\"（Toolformer, ART, Chameleon, CogRouter），本文追问\"routing 到底在 route 什么信号\"——这是一个被忽视但影响 router 设计方向的诊断性问题。将 routing signal 分解为 death-avoidance 和 non-death components 的思路简洁有力。\n\n**S2. Pure-strategy counterfactual 设计干净。** [R1-S2, R2-S4, 共识] 控制相同 random seed + initial conditions，让 performance gap 完全归因于 computation mode choice，是 well-identified 的因果推断设计。Episode-level labeling function（Algorithm 1）的 death-aware prioritization 合理且 penalty-independent。\n\n**S3. 统计分析扎实。** [R1-S4, R2-S1, 共识] Episode-level bootstrap（B=10,000）、wild cluster bootstrap（Appendix E）、per-task CIs（Appendix F）、8-seed robustness（Appendix J）、Cohen's d=3.02——统计工具的选择和使用达到高标准。Cluster-robust inference 处理 task-type 内相关性是同领域少见的。\n\n**S4. Robustness checks 全面。** [R1-S4, R2-S3, 共识] Leave-one-task-out DAF（75.9%-78.9%）、penalty sensitivity（Appendix K）、cross-model replication、anti-cherry-picking analysis（18/19 excluded types 也 death-dominated, ΔDR=+38.2pp）、SCI=0.2147 排除信号集中度质疑。\n\n**S5. Negative results 诚实呈现。** [R2-S2, R1-S6, 共识] Router step-level ≈ chance、data augmentation 无效——这些 negative results 对社区有价值，呈现方式坦诚。Limitations 具体且未回避关键弱点。\n\n**S6. Cross-model validation。** [R2-S5, 共识] Llama-3.1-8B 复制（11 tasks, N=220）显示 internal death rate ~42%（与 Qwen 几乎一致），direction consistency 10/10，death dominance 跨模型稳定。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [Critical, 共识] DAF headline framing 误导——90.4% 作为 primary metric 掩盖了其 penalty-dependent 本质。**\n- **R1-N1, R2 同意。** Abstract 和 §3.1 以 \"DAF = 90.4%\" 作为 headline，与 penalty-independent 的 78.9% label fraction 并列。DAF = δP/(δP + Δ_nd) 随 P 单调递增是数学后果（论文自己承认），在 Δ_nd ≈ +2.84 且 P=100 时 DAF 接近 1 是代数必然。78.9% 才是 penalty-independent 的 robust finding。\n- **Action**: Abstract 以 78.9% 为 primary metric 开头；§3.1 段落重组，DAF 降为 derived quantity；增加 DAF 在不同 Δ_nd 下的行为讨论。\n\n**MF2 [Critical, R2 首提, R1 部分同意] 核心发现 novelty 不足——\"obvious in hindsight\" 风险。**\n- **R2-W1 (Critical), R1 Excitement 3.5 vs R2 Excitement 2.5——分歧保留。** 在 P=100 death penalty + internal death rate ~43% vs deterministic ~16% 的设定下，death avoidance 成为 dominant routing signal 高度可预见。§5 Non-triviality 论证（threshold routing, intervention resistance, cross-model stability）只证明 robustness 而非 non-obviousness。\n- **R1 部分反驳**: 问题定义本身有价值——\"routing 文献假设多样化信号，但无人验证\"是一个 field-level blind spot，quantification（78.9% 的具体比例、intervention resistance 的具体幅度）是 non-obvious 的。\n- **Director 裁决**: 维持 Critical。R1 的 \"问题有价值\" 论点成立但不足以完全消除 triviality concern——EMNLP reviewer panel 中 excitement deficit 是常见 rejection reason。\n- **Action**: 三角度强化 non-triviality 论证：(1) routing 文献 prior assumptions 与实证结果的反差；(2) intervention resistance 的 non-predictability（4 轴均无法消除，这从 setup 无法预见）；(3) cross-model δ stability 作为结构性发现。\n\n**MF3 [Critical, R2 首提, R1 基本同意] Framing 内在张力——framework vs finding 定位不清。**\n- **R2-W2 (Critical), R1 同意需修正。** 标题聚焦 empirical finding（\"Death Avoidance as the Dominant Routing Signal\"），Contribution 1 聚焦 framework（\"episode-level counterfactual diagnostic framework\"），Abstract 同时强调两者，Conclusion 仅 2 句 finding-oriented。读者无法确定论文 identity。\n- **Action**: 选择一个主线贯穿：如 framework-centric，标题改为方法论导向，ScienceWorld 作为 case study；如 finding-centric，弱化 framework contribution claim，加强 non-triviality。\n\n**MF4 [Critical→Warning, R1 首提, R2 同意] Cluster bootstrap K=11 低于公认阈值，辩护不足。**\n- **R1-N2 (Critical), R2 同意但未列 Critical。Director 裁决：升为 Critical。** Cameron et al. (2008)（论文自引）建议 K≥20-40。Webb (2023) Monte Carlo 显示 K<20 有 size distortion。2^11=2048 排列下 p=0.002 颗粒度粗。Cohen's d=3.02 在小 K 下可受 outlier 影响。\n- **缓解因素**: (1) leave-one-task-out DAF 最差 75.9%（仍大幅 >50%）；(2) 所有 28 death-prone tasks 方向一致（Appendix F）；(3) non-clustered bootstrap 的 95% CI [81.6%, 98.8%] 不依赖 cluster 假设。\n- **Action**: 正文以 non-clustered bootstrap 为主推断；cluster bootstrap 定位为 conservative sensitivity check；增加 K=11 vs K≥40 的显式讨论。\n\n**MF5 [Critical, R1 首提, R2 部分同意] Episode→step label projection 噪声未充分量化——router diagnostic 价值受损。**\n- **R1-N3 (Critical).** 97.4% step-level ties → 27.7% mislabeling + 60.3% pre-event neutral → 仅 ~12% informative + correctly-labeled signal。Router near-chance (56-59%) 可能是 label noise 而非 signal inherently unlearnable。§3.6 \"diagnostic probe\" 定位需要更精确——当 probe 的 training signal 有 ~88% noise/uninformative rate 时，probe 失败不能直接诊断 underlying signal structure。\n- **Action**: §3.6 明确区分两种解释（label noise vs signal not step-level）；讨论 step-level label refinement baseline 的可能性；将 router 实验明确框架为 negative result。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1 [Warning, 共识] Cross-environment probes 定位过强——应为 boundary probes 而非 cross-domain validation。**\n- MATH（无 catastrophic failure → null result, unfalsifiable）和 ALFWorld（information asymmetry ≠ computation mode routing）不构成真正的跨环境验证。三个环境的 \"deterministic\" 含义完全不同（oracle simulator vs code interpreter vs admissible-action enumeration）。缺少第二个 death-prone interactive environment 的完整分析（NetHack 为 most direct target）。\n- **Action**: §3.4 开头明确三个环境 deterministic 含义差异；Abstract 调整措辞为 \"boundary probes\"；scope 限定为 ScienceWorld 的深度分析。\n\n**SF2 [Warning, R2 首提] 缺少 penalty magnitude 的实际实验验证。**\n- §2.4 和 Appendix K 的 DAF vs P 分析是数学推导而非实验结果。DAF 公式假设 Δ_nd 和 death rates 不随 P 变化，但 agent behavior 可能因 penalty magnitude 不同而改变。\n- **Action**: 至少在一个非默认 P 值下运行实际实验验证 DAF 公式的预测准确性。\n\n**SF3 [Warning, R1 首提] Pure-strategy 设计的外部效度。**\n- Pure-strategy 让 internal strategy 连续 30 steps 积累 hallucination errors，可能 overestimate death rate。Mixed-strategy routing 中途切换可能避免 death。\n- **Action**: Limitations 或 Discussion 增加 pure-strategy vs mixed-strategy gap 的定量估计。\n\n**SF4 [Warning, 共识] Conclusion 过于简短（2 句话），不匹配 long paper 标准。**\n- 缺 broader implications、framework 局限性反思、对 safe RL 和 agent design 社区的启示。\n- **Action**: 扩展至 ~0.5 页。\n\n**SF5 [Warning, 共识] Safe RL Related Work 不够深入。**\n- §4 Safe RL 段列举引用但无实质讨论。缺 CMDP 框架（Altman 1999）与 death avoidance 的映射、risk-sensitive RL 与 catastrophic failure 的关系。\n- **Action**: 扩展至 5+ 句，补 Altman 1999, Mihatsch & Neuneier 2002。\n\n**SF6 [Warning, 共识] Abstract 数字过密，可读性受损。**\n- 78.9%, 245, Qwen2.5-7B, 11 task types, DAF 90.4%, 95% CI, P=100, δ=0.265 全部堆在一段。\n- **Action**: 重组为 concept-first, numbers-second；CI 和 δ 值移到正文。\n\n**SF7 [Warning, 共识] \"Modality\" 术语在 NLP 语境下有歧义。**\n- NLP 领域 modality 通常指 data modality (text/vision/audio)。\n- **Action**: 全文统一 modality → computation mode。\n\n**SF8 [Warning, R1 首提] Reflexion dose-response N=5 统计功效不足。**\n- N=5 trials × 10 death-prone tasks，MDE ~14pp。Plateau conclusion 应标注为 suggestive evidence。\n- **Action**: 报告 power analysis，标注 evidence level。\n\n### Minor\n\n**m1 [Info, R2]** 62% tie rate (150/245 episodes) 含义未充分讨论——routing 在大多数 episodes 中无差异，routing 实际价值值得质疑。\n\n**m2 [Info, R1]** Figure 2 应在 caption 报告 Spearman's ρ（已在 Appendix D 报告为 0.975）。\n\n**m3 [Info, 共识]** `webb-2023` 年份需确认（OpenAlex 匹配到 2014 working paper, 2023 journal version）。\n\n**m4 [Info, R1]** Appendix R Decision Framework 中 f_death < 50% 和 >75% 的阈值选择缺乏理论依据。\n\n**m5 [Info, R2]** Responsible NLP Checklist 中 AI assistants disclosure 建议更具体。\n\n**m6 [Info, R2]** 缺 missing references: Altman (1999) CMDP, Mihatsch & Neuneier (2002), Natarajan et al. (2013) noisy label learning。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** [R1-Q1, R2-Q1] DAF 公式假设 Δ_nd 不随 P 变化——是否在 P≠100 的 ScienceWorld 变体上做过实际验证？\n\n**Q2.** [R1-Q2, R2-Q4] 105 internal deaths 全来自 `focus on [object]` 误用——death avoidance 是否等价于 single-action bug avoidance？如果 action filtering 消除该 pattern，death dominance 是否消失？（Grounding ablation 仅降至 29%，residual gap ≥12pp 说明不能完全消除。）\n\n**Q3.** [R2-Q2] 62% tie rate (150/245 no-preference) 是否说明 routing 本身在大多数情况下缺乏实际价值？\n\n**Q4.** [R1-Q4] 3.7% internal-preferred base rate → always-deterministic 是否已在实际部署中接近最优？oracle 仅改善 2.89 points。\n\n**Q5.** [R2-Q3] SCI=0.2147 但 top-3 task types 占 39.8% total death-rate differential——death dominance 是否是 task-type specific 而非 environment-wide？\n\n**Q6.** [R1-Q5] Llama cross-model replication 的完整 DAF 是多少？是否与 Qwen 的 90.4% 一致？\n\n---\n\n## Missing References\n\n- **Altman, E. (1999). Constrained Markov Decision Processes.** Death avoidance 作为 implicit safety constraint 的理论对应。[R2]\n- **Mihatsch & Neuneier (2002). Risk-sensitive RL.** 与 catastrophic failure avoidance 直接相关。[R2]\n- **Natarajan et al. (2013). Learning with Noisy Labels.** 为 27.7% mislabeling rate 下的 router near-chance accuracy 提供理论 grounding。[R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户选择不提交）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 超时（elapsed 727s）。视觉审查 Agent 未能在时限内完成。无排版审查结果可报告。\n\n**基于 PDF 阅读的基本格式确认**:\n- 正文 8 页（§1-§6 在 p1-p8），符合 ≤8 页要求\n- Limitations 在 p8-9（不计入页数），内容具体\n- Ethics Statement 在 p9\n- References p9-10\n- Appendices A-R p10-21\n- \"Anonymous ACL submission\"，未发现匿名性泄露\n- ACL 模板 + [review] option 已开启\n- Figure 1 (Pipeline, p3), Figure 2 (Scatter, p4), Figure 3 (Dose-response, p6) 均在合理位置\n- Table 1 (p5), Table 2 (p6) 排版正常\n\n---\n\n## Reviewer Consensus\n\n### 共识区域（已收敛）\n| 议题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| DAF headline framing (MF1) | Critical | Agrees | ✅ 共识 |\n| K=11 cluster bootstrap (MF4) | Critical | Agrees | ✅ 共识 |\n| Episode→step noise (MF5) | Critical | Partially agrees | ✅ 基本共识 |\n| Framing tension (MF3) | Agrees | Critical | ✅ 共识 |\n| Cross-env probes overclaimed (SF1) | Should-Fix | Critical | ✅ 共识（severity 略异） |\n| Conclusion too short (SF4) | Minor | Should-Fix | ✅ 共识 |\n| Modality terminology (SF7) | Agrees | Should-Fix | ✅ 共识 |\n| Safe RL discussion (SF5) | Agrees | Should-Fix | ✅ 共识 |\n| Soundness | 3.5/5 | 3.5/5 | ✅ 一致 |\n| Reproducibility | 4.5/5 | 4/5 | ✅ 基本一致 |\n\n### 分歧区域（未收敛，如实记录）\n| 议题 | R1 | R2 | 差异 |\n|------|----|----|------|\n| **Excitement/Novelty** | **3.5/5** | **2.5/5** | **1.0 gap** |\n| Novelty (MF2) | 问题有价值，quantification non-obvious | Obvious in hindsight | R1 偏积极 |\n| Overall Score | **3.5** (Borderline Conference) | **3.0** (Findings) | **0.5 gap** |\n\n**分歧根源**: R1 认为\"问题定义本身有价值\"——routing 文献假设多样化信号但无人验证，本文首次系统 decompose 并量化，即使 finding 可预见，quantification 仍有贡献。R2 认为在已知 setup（P=100, death rate 43% vs 16%）下 finding 高度可预见，quantification 的 novelty 不足以支撑 main conference。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0–3.5（Findings 至 Borderline Conference）**\n\n**维度汇总**:\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 4.5/5 | 4/5 | 4.25/5 |\n| Clarity | — | 3/5 | 3/5 |\n\n**综合评估**:\n\n论文问了一个重要且被忽视的诊断性问题（routing signal 的来源是什么），给出了清晰的回答（death avoidance dominates），counterfactual 设计干净，统计分析超过同类工作水准，robustness checks 全面，negative results 诚实呈现。\n\n但存在几个结构性问题：(1) DAF 的 headline framing 掩盖了其 penalty-dependent 本质；(2) 核心发现在已知 setup 下可预见性高，non-triviality 论证力度不足；(3) framework vs finding 的 framing 张力贯穿全文；(4) K=11 cluster bootstrap 低于公认阈值；(5) episode→step projection 噪声使 router diagnostic 的诊断价值存疑。\n\n**如果以下问题在 revision 中充分回应，有望提升至 Conference (3.5-4.0)**：\n- MF1（DAF framing 修正）+ MF3（framing 统一）：低成本修复\n- MF4（K=11 辩护）：通过 non-clustered bootstrap 为主推断来缓解\n- MF2（novelty 论证）：需要实质性重写 §5 non-triviality 段\n- MF5（router diagnostic attribution）：需要更精确的分析\n\n**如果 MF2（novelty）无法有效回应，更可能落在 Findings (3.0) 档位**——方法论扎实但 finding 的 excitement 不足。\n\n---\n\n## Detailed Comments\n\n### Title & Abstract\n- 标题聚焦 finding 但 Contribution 1 是 framework——需统一\n- Abstract 数字密度过高，建议 concept-first, numbers-second\n- DAF=90.4% 不应先于 78.9% 出现\n\n### §1 Introduction\n- 从 routing problem → gap → framework → finding 的逻辑链通畅\n- \"no prior work has systematically decomposed\" 需更具体说明与 existing ablation 的区别\n- Contributions 列表中 (1) framework 和 (2) evidence 的权重需统一\n\n### §2 Method\n- 写作最清晰的部分\n- Algorithm 1 的 penalty-independent labeling 设计合理\n- DAF 定义数学上 clean，但需更 upfront 承认是 derived quantity\n- §2.4 末尾 \"Scope of episode-level analysis\" 段已存在但可更强调 episode→step gap 的 implications\n\n### §3 Experiments\n- §3.1 (Death Decomposition): 核心实证 section，数据呈现清晰。Figure 2 有效但 y-axis label 太小\n- §3.2 (Cross-Model): 增加可信度但篇幅短，缺 Llama DAF 数据\n- §3.3 (Agent Improvement): 有价值。72B DAF=92.4% (7B: 90.4%) 说明 scaling 不消除 death dominance\n- §3.4 (Cross-Environment): 过于浅显，MATH 和 ALFWorld 各仅约 1 段\n- §3.5 (Baselines): Oracle degeneracy (96.3% 选 always-det) 是重要发现\n- §3.6 (Router): 应更明确框架为 negative result\n\n### §4 Related Work\n- Tool Use 和 Adaptive Routing 覆盖充分\n- Counterfactual RL 和 LLM Agent Environments adequate\n- **Safe RL 明显不足**——需扩展\n\n### §5 Discussion\n- \"Why the router fails\" 分析有价值\n- \"Non-triviality\" 论证力度不足（核心 weakness）\n- \"Anatomy of catastrophic failure\"——105 deaths 全来自 `focus on` 是重要定性发现，但 implications 需更强讨论\n- \"Practitioner implications\" 具体但偏 list-like\n\n### §6 Conclusion\n- 严重不足——仅 2 句话，需扩展至 ~0.5 页\n\n### Limitations\n- 覆盖面 adequate\n- 缺对 \"P=100 specific\" 这一限制的明确讨论\n\n### 格式合规\n- ✅ 正文 8 页（符合 ≤8 页要求）\n- ✅ Limitations 存在且具体\n- ✅ Ethics Statement 存在\n- ✅ Double-blind: \"Anonymous ACL submission\"\n- ✅ ACL 模板 + [review] option\n- ✅ 引用格式基本统一\n- ⚠️ webb-2023 年份需确认",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0-3.5 (Findings to Borderline Conference)",
  "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "simgate-modular-routing",
    "report": "# 审稿报告：Death Avoidance as the Dominant Routing Signal\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 (Long Paper via ARR)\n**Deadline**: 2026-05-25\n**Round**: 19 (fresh review)\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，将 modular LLM agent 的 routing signal 分解为 death-avoidance 和 non-death 两个成分。在 ScienceWorld（11 task types, 245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的 non-tie routing labels 源于 death asymmetry：internal strategy 因幻觉触发 catastrophic death（−100 penalty），而 deterministic strategy 存活。DAF 在 P=100 下达 90.4%。Cross-model replication（Llama-3.1-8B）、four intervention axes（retry, Reflexion, 72B scaling, action filtering）、cross-environment probes（MATH, ALFWorld）进一步支持诊断。Router 训练（Qwen3 LoRA, 0.6B-4B）step-level 接近 chance，episode-level 仅 4B 有边际改善。\n\n---\n\n## Strengths\n\n**S1. 问题定义精准且有价值。** [R1-S1, 共识] 现有 routing 文献关注\"怎么 route\"（Toolformer, ART, Chameleon, CogRouter），本文追问\"routing 到底在 route 什么信号\"——这是一个被忽视但影响 router 设计方向的诊断性问题。将 routing signal 分解为 death-avoidance 和 non-death components 的思路简洁有力。\n\n**S2. Pure-strategy counterfactual 设计干净。** [R1-S2, R2-S4, 共识] 控制相同 random seed + initial conditions，让 performance gap 完全归因于 computation mode choice，是 well-identified 的因果推断设计。Episode-level labeling function（Algorithm 1）的 death-aware prioritization 合理且 penalty-independent。\n\n**S3. 统计分析扎实。** [R1-S4, R2-S1, 共识] Episode-level bootstrap（B=10,000）、wild cluster bootstrap（Appendix E）、per-task CIs（Appendix F）、8-seed robustness（Appendix J）、Cohen's d=3.02——统计工具的选择和使用达到高标准。Cluster-robust inference 处理 task-type 内相关性是同领域少见的。\n\n**S4. Robustness checks 全面。** [R1-S4, R2-S3, 共识] Leave-one-task-out DAF（75.9%-78.9%）、penalty sensitivity（Appendix K）、cross-model replication、anti-cherry-picking analysis（18/19 excluded types 也 death-dominated, ΔDR=+38.2pp）、SCI=0.2147 排除信号集中度质疑。\n\n**S5. Negative results 诚实呈现。** [R2-S2, R1-S6, 共识] Router step-level ≈ chance、data augmentation 无效——这些 negative results 对社区有价值，呈现方式坦诚。Limitations 具体且未回避关键弱点。\n\n**S6. Cross-model validation。** [R2-S5, 共识] Llama-3.1-8B 复制（11 tasks, N=220）显示 internal death rate ~42%（与 Qwen 几乎一致），direction consistency 10/10，death dominance 跨模型稳定。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [Critical, 共识] DAF headline framing 误导——90.4% 作为 primary metric 掩盖了其 penalty-dependent 本质。**\n- **R1-N1, R2 同意。** Abstract 和 §3.1 以 \"DAF = 90.4%\" 作为 headline，与 penalty-independent 的 78.9% label fraction 并列。DAF = δP/(δP + Δ_nd) 随 P 单调递增是数学后果（论文自己承认），在 Δ_nd ≈ +2.84 且 P=100 时 DAF 接近 1 是代数必然。78.9% 才是 penalty-independent 的 robust finding。\n- **Action**: Abstract 以 78.9% 为 primary metric 开头；§3.1 段落重组，DAF 降为 derived quantity；增加 DAF 在不同 Δ_nd 下的行为讨论。\n\n**MF2 [Critical, R2 首提, R1 部分同意] 核心发现 novelty 不足——\"obvious in hindsight\" 风险。**\n- **R2-W1 (Critical), R1 Excitement 3.5 vs R2 Excitement 2.5——分歧保留。** 在 P=100 death penalty + internal death rate ~43% vs deterministic ~16% 的设定下，death avoidance 成为 dominant routing signal 高度可预见。§5 Non-triviality 论证（threshold routing, intervention resistance, cross-model stability）只证明 robustness 而非 non-obviousness。\n- **R1 部分反驳**: 问题定义本身有价值——\"routing 文献假设多样化信号，但无人验证\"是一个 field-level blind spot，quantification（78.9% 的具体比例、intervention resistance 的具体幅度）是 non-obvious 的。\n- **Director 裁决**: 维持 Critical。R1 的 \"问题有价值\" 论点成立但不足以完全消除 triviality concern——EMNLP reviewer panel 中 excitement deficit 是常见 rejection reason。\n- **Action**: 三角度强化 non-triviality 论证：(1) routing 文献 prior assumptions 与实证结果的反差；(2) intervention resistance 的 non-predictability（4 轴均无法消除，这从 setup 无法预见）；(3) cross-model δ stability 作为结构性发现。\n\n**MF3 [Critical, R2 首提, R1 基本同意] Framing 内在张力——framework vs finding 定位不清。**\n- **R2-W2 (Critical), R1 同意需修正。** 标题聚焦 empirical finding（\"Death Avoidance as the Dominant Routing Signal\"），Contribution 1 聚焦 framework（\"episode-level counterfactual diagnostic framework\"），Abstract 同时强调两者，Conclusion 仅 2 句 finding-oriented。读者无法确定论文 identity。\n- **Action**: 选择一个主线贯穿：如 framework-centric，标题改为方法论导向，ScienceWorld 作为 case study；如 finding-centric，弱化 framework contribution claim，加强 non-triviality。\n\n**MF4 [Critical→Warning, R1 首提, R2 同意] Cluster bootstrap K=11 低于公认阈值，辩护不足。**\n- **R1-N2 (Critical), R2 同意但未列 Critical。Director 裁决：升为 Critical。** Cameron et al. (2008)（论文自引）建议 K≥20-40。Webb (2023) Monte Carlo 显示 K<20 有 size distortion。2^11=2048 排列下 p=0.002 颗粒度粗。Cohen's d=3.02 在小 K 下可受 outlier 影响。\n- **缓解因素**: (1) leave-one-task-out DAF 最差 75.9%（仍大幅 >50%）；(2) 所有 28 death-prone tasks 方向一致（Appendix F）；(3) non-clustered bootstrap 的 95% CI [81.6%, 98.8%] 不依赖 cluster 假设。\n- **Action**: 正文以 non-clustered bootstrap 为主推断；cluster bootstrap 定位为 conservative sensitivity check；增加 K=11 vs K≥40 的显式讨论。\n\n**MF5 [Critical, R1 首提, R2 部分同意] Episode→step label projection 噪声未充分量化——router diagnostic 价值受损。**\n- **R1-N3 (Critical).** 97.4% step-level ties → 27.7% mislabeling + 60.3% pre-event neutral → 仅 ~12% informative + correctly-labeled signal。Router near-chance (56-59%) 可能是 label noise 而非 signal inherently unlearnable。§3.6 \"diagnostic probe\" 定位需要更精确——当 probe 的 training signal 有 ~88% noise/uninformative rate 时，probe 失败不能直接诊断 underlying signal structure。\n- **Action**: §3.6 明确区分两种解释（label noise vs signal not step-level）；讨论 step-level label refinement baseline 的可能性；将 router 实验明确框架为 negative result。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1 [Warning, 共识] Cross-environment probes 定位过强——应为 boundary probes 而非 cross-domain validation。**\n- MATH（无 catastrophic failure → null result, unfalsifiable）和 ALFWorld（information asymmetry ≠ computation mode routing）不构成真正的跨环境验证。三个环境的 \"deterministic\" 含义完全不同（oracle simulator vs code interpreter vs admissible-action enumeration）。缺少第二个 death-prone interactive environment 的完整分析（NetHack 为 most direct target）。\n- **Action**: §3.4 开头明确三个环境 deterministic 含义差异；Abstract 调整措辞为 \"boundary probes\"；scope 限定为 ScienceWorld 的深度分析。\n\n**SF2 [Warning, R2 首提] 缺少 penalty magnitude 的实际实验验证。**\n- §2.4 和 Appendix K 的 DAF vs P 分析是数学推导而非实验结果。DAF 公式假设 Δ_nd 和 death rates 不随 P 变化，但 agent behavior 可能因 penalty magnitude 不同而改变。\n- **Action**: 至少在一个非默认 P 值下运行实际实验验证 DAF 公式的预测准确性。\n\n**SF3 [Warning, R1 首提] Pure-strategy 设计的外部效度。**\n- Pure-strategy 让 internal strategy 连续 30 steps 积累 hallucination errors，可能 overestimate death rate。Mixed-strategy routing 中途切换可能避免 death。\n- **Action**: Limitations 或 Discussion 增加 pure-strategy vs mixed-strategy gap 的定量估计。\n\n**SF4 [Warning, 共识] Conclusion 过于简短（2 句话），不匹配 long paper 标准。**\n- 缺 broader implications、framework 局限性反思、对 safe RL 和 agent design 社区的启示。\n- **Action**: 扩展至 ~0.5 页。\n\n**SF5 [Warning, 共识] Safe RL Related Work 不够深入。**\n- §4 Safe RL 段列举引用但无实质讨论。缺 CMDP 框架（Altman 1999）与 death avoidance 的映射、risk-sensitive RL 与 catastrophic failure 的关系。\n- **Action**: 扩展至 5+ 句，补 Altman 1999, Mihatsch & Neuneier 2002。\n\n**SF6 [Warning, 共识] Abstract 数字过密，可读性受损。**\n- 78.9%, 245, Qwen2.5-7B, 11 task types, DAF 90.4%, 95% CI, P=100, δ=0.265 全部堆在一段。\n- **Action**: 重组为 concept-first, numbers-second；CI 和 δ 值移到正文。\n\n**SF7 [Warning, 共识] \"Modality\" 术语在 NLP 语境下有歧义。**\n- NLP 领域 modality 通常指 data modality (text/vision/audio)。\n- **Action**: 全文统一 modality → computation mode。\n\n**SF8 [Warning, R1 首提] Reflexion dose-response N=5 统计功效不足。**\n- N=5 trials × 10 death-prone tasks，MDE ~14pp。Plateau conclusion 应标注为 suggestive evidence。\n- **Action**: 报告 power analysis，标注 evidence level。\n\n### Minor\n\n**m1 [Info, R2]** 62% tie rate (150/245 episodes) 含义未充分讨论——routing 在大多数 episodes 中无差异，routing 实际价值值得质疑。\n\n**m2 [Info, R1]** Figure 2 应在 caption 报告 Spearman's ρ（已在 Appendix D 报告为 0.975）。\n\n**m3 [Info, 共识]** `webb-2023` 年份需确认（OpenAlex 匹配到 2014 working paper, 2023 journal version）。\n\n**m4 [Info, R1]** Appendix R Decision Framework 中 f_death < 50% 和 >75% 的阈值选择缺乏理论依据。\n\n**m5 [Info, R2]** Responsible NLP Checklist 中 AI assistants disclosure 建议更具体。\n\n**m6 [Info, R2]** 缺 missing references: Altman (1999) CMDP, Mihatsch & Neuneier (2002), Natarajan et al. (2013) noisy label learning。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** [R1-Q1, R2-Q1] DAF 公式假设 Δ_nd 不随 P 变化——是否在 P≠100 的 ScienceWorld 变体上做过实际验证？\n\n**Q2.** [R1-Q2, R2-Q4] 105 internal deaths 全来自 `focus on [object]` 误用——death avoidance 是否等价于 single-action bug avoidance？如果 action filtering 消除该 pattern，death dominance 是否消失？（Grounding ablation 仅降至 29%，residual gap ≥12pp 说明不能完全消除。）\n\n**Q3.** [R2-Q2] 62% tie rate (150/245 no-preference) 是否说明 routing 本身在大多数情况下缺乏实际价值？\n\n**Q4.** [R1-Q4] 3.7% internal-preferred base rate → always-deterministic 是否已在实际部署中接近最优？oracle 仅改善 2.89 points。\n\n**Q5.** [R2-Q3] SCI=0.2147 但 top-3 task types 占 39.8% total death-rate differential——death dominance 是否是 task-type specific 而非 environment-wide？\n\n**Q6.** [R1-Q5] Llama cross-model replication 的完整 DAF 是多少？是否与 Qwen 的 90.4% 一致？\n\n---\n\n## Missing References\n\n- **Altman, E. (1999). Constrained Markov Decision Processes.** Death avoidance 作为 implicit safety constraint 的理论对应。[R2]\n- **Mihatsch & Neuneier (2002). Risk-sensitive RL.** 与 catastrophic failure avoidance 直接相关。[R2]\n- **Natarajan et al. (2013). Learning with Noisy Labels.** 为 27.7% mislabeling rate 下的 router near-chance accuracy 提供理论 grounding。[R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户选择不提交）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 超时（elapsed 727s）。视觉审查 Agent 未能在时限内完成。无排版审查结果可报告。\n\n**基于 PDF 阅读的基本格式确认**:\n- 正文 8 页（§1-§6 在 p1-p8），符合 ≤8 页要求\n- Limitations 在 p8-9（不计入页数），内容具体\n- Ethics Statement 在 p9\n- References p9-10\n- Appendices A-R p10-21\n- \"Anonymous ACL submission\"，未发现匿名性泄露\n- ACL 模板 + [review] option 已开启\n- Figure 1 (Pipeline, p3), Figure 2 (Scatter, p4), Figure 3 (Dose-response, p6) 均在合理位置\n- Table 1 (p5), Table 2 (p6) 排版正常\n\n---\n\n## Reviewer Consensus\n\n### 共识区域（已收敛）\n| 议题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| DAF headline framing (MF1) | Critical | Agrees | ✅ 共识 |\n| K=11 cluster bootstrap (MF4) | Critical | Agrees | ✅ 共识 |\n| Episode→step noise (MF5) | Critical | Partially agrees | ✅ 基本共识 |\n| Framing tension (MF3) | Agrees | Critical | ✅ 共识 |\n| Cross-env probes overclaimed (SF1) | Should-Fix | Critical | ✅ 共识（severity 略异） |\n| Conclusion too short (SF4) | Minor | Should-Fix | ✅ 共识 |\n| Modality terminology (SF7) | Agrees | Should-Fix | ✅ 共识 |\n| Safe RL discussion (SF5) | Agrees | Should-Fix | ✅ 共识 |\n| Soundness | 3.5/5 | 3.5/5 | ✅ 一致 |\n| Reproducibility | 4.5/5 | 4/5 | ✅ 基本一致 |\n\n### 分歧区域（未收敛，如实记录）\n| 议题 | R1 | R2 | 差异 |\n|------|----|----|------|\n| **Excitement/Novelty** | **3.5/5** | **2.5/5** | **1.0 gap** |\n| Novelty (MF2) | 问题有价值，quantification non-obvious | Obvious in hindsight | R1 偏积极 |\n| Overall Score | **3.5** (Borderline Conference) | **3.0** (Findings) | **0.5 gap** |\n\n**分歧根源**: R1 认为\"问题定义本身有价值\"——routing 文献假设多样化信号但无人验证，本文首次系统 decompose 并量化，即使 finding 可预见，quantification 仍有贡献。R2 认为在已知 setup（P=100, death rate 43% vs 16%）下 finding 高度可预见，quantification 的 novelty 不足以支撑 main conference。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0–3.5（Findings 至 Borderline Conference）**\n\n**维度汇总**:\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 4.5/5 | 4/5 | 4.25/5 |\n| Clarity | — | 3/5 | 3/5 |\n\n**综合评估**:\n\n论文问了一个重要且被忽视的诊断性问题（routing signal 的来源是什么），给出了清晰的回答（death avoidance dominates），counterfactual 设计干净，统计分析超过同类工作水准，robustness checks 全面，negative results 诚实呈现。\n\n但存在几个结构性问题：(1) DAF 的 headline framing 掩盖了其 penalty-dependent 本质；(2) 核心发现在已知 setup 下可预见性高，non-triviality 论证力度不足；(3) framework vs finding 的 framing 张力贯穿全文；(4) K=11 cluster bootstrap 低于公认阈值；(5) episode→step projection 噪声使 router diagnostic 的诊断价值存疑。\n\n**如果以下问题在 revision 中充分回应，有望提升至 Conference (3.5-4.0)**：\n- MF1（DAF framing 修正）+ MF3（framing 统一）：低成本修复\n- MF4（K=11 辩护）：通过 non-clustered bootstrap 为主推断来缓解\n- MF2（novelty 论证）：需要实质性重写 §5 non-triviality 段\n- MF5（router diagnostic attribution）：需要更精确的分析\n\n**如果 MF2（novelty）无法有效回应，更可能落在 Findings (3.0) 档位**——方法论扎实但 finding 的 excitement 不足。\n\n---\n\n## Detailed Comments\n\n### Title & Abstract\n- 标题聚焦 finding 但 Contribution 1 是 framework——需统一\n- Abstract 数字密度过高，建议 concept-first, numbers-second\n- DAF=90.4% 不应先于 78.9% 出现\n\n### §1 Introduction\n- 从 routing problem → gap → framework → finding 的逻辑链通畅\n- \"no prior work has systematically decomposed\" 需更具体说明与 existing ablation 的区别\n- Contributions 列表中 (1) framework 和 (2) evidence 的权重需统一\n\n### §2 Method\n- 写作最清晰的部分\n- Algorithm 1 的 penalty-independent labeling 设计合理\n- DAF 定义数学上 clean，但需更 upfront 承认是 derived quantity\n- §2.4 末尾 \"Scope of episode-level analysis\" 段已存在但可更强调 episode→step gap 的 implications\n\n### §3 Experiments\n- §3.1 (Death Decomposition): 核心实证 section，数据呈现清晰。Figure 2 有效但 y-axis label 太小\n- §3.2 (Cross-Model): 增加可信度但篇幅短，缺 Llama DAF 数据\n- §3.3 (Agent Improvement): 有价值。72B DAF=92.4% (7B: 90.4%) 说明 scaling 不消除 death dominance\n- §3.4 (Cross-Environment): 过于浅显，MATH 和 ALFWorld 各仅约 1 段\n- §3.5 (Baselines): Oracle degeneracy (96.3% 选 always-det) 是重要发现\n- §3.6 (Router): 应更明确框架为 negative result\n\n### §4 Related Work\n- Tool Use 和 Adaptive Routing 覆盖充分\n- Counterfactual RL 和 LLM Agent Environments adequate\n- **Safe RL 明显不足**——需扩展\n\n### §5 Discussion\n- \"Why the router fails\" 分析有价值\n- \"Non-triviality\" 论证力度不足（核心 weakness）\n- \"Anatomy of catastrophic failure\"——105 deaths 全来自 `focus on` 是重要定性发现，但 implications 需更强讨论\n- \"Practitioner implications\" 具体但偏 list-like\n\n### §6 Conclusion\n- 严重不足——仅 2 句话，需扩展至 ~0.5 页\n\n### Limitations\n- 覆盖面 adequate\n- 缺对 \"P=100 specific\" 这一限制的明确讨论\n\n### 格式合规\n- ✅ 正文 8 页（符合 ≤8 页要求）\n- ✅ Limitations 存在且具体\n- ✅ Ethics Statement 存在\n- ✅ Double-blind: \"Anonymous ACL submission\"\n- ✅ ACL 模板 + [review] option\n- ✅ 引用格式基本统一\n- ⚠️ webb-2023 年份需确认",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0-3.5 (Findings to Borderline Conference)",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
  }
}
```

</details>

---


### Tool result

_source line 1743 · 2026-05-19T15:59:14.035677+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4015
}
```

</details>

---


### Assistant

_source line 1744 · 2026-05-19T15:59:23.622205+00:00_

审稿报告已投递至 Research Director。

---

**Round 19 审稿完成。**

**Overall: 3.0–3.5（Findings 至 Borderline Conference）**

核心结论：
- **方法论扎实**：counterfactual 设计干净，统计分析超过同类水准，robustness checks 全面
- **5 个 Must-Fix**：DAF headline framing 误导（共识）、novelty 不足（分歧，R1: 3.5 vs R2: 2.5）、framing 张力（共识）、K=11 统计推断（共识）、episode→step noise 使 router diagnostic 存疑（共识）
- **关键分歧**：Excitement 评分差 1.0（R1 认为问题定义有价值，R2 认为 finding obvious in hindsight）
- **升档条件**：MF1（DAF framing）和 MF4（K=11 辩护）可通过低成本修改解决；MF2（novelty）需要实质性重写 §5 non-triviality 段——如果 novelty 论证有效，有望升至 Conference (4.0)

Issue tracker 已同步更新至 `review_issues.yaml`。外部审稿已跳过，视觉审查超时。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 145

## Round 145

4 recorded events


### User

_source line 1745 · 2026-05-19T15:59:23.628900+00:00_

[Reviewer 1 审稿结果]:
逐条回应 Reviewer 2 的意见。

---

## 关键分歧点总体判断

### 分歧 1: Overall 3.0 vs 3.5（0.5 分差距来源）

差距几乎完全来自 Excitement 评估（R2: 2.5 vs 我: 3.5）。Soundness 我们一致（均 3.5）。R2 认为核心发现 "obvious in hindsight"，我认为问题定义本身有价值。经考虑 R2 论点后，我承认 ScienceWorld 的极端 penalty 设计（P=100, −100 death）确实降低了发现的 surprise factor，但仍认为 R2 低估了诊断性贡献——详见 W1 回应。**我倾向将自己的 Excitement 从 3.5 下调至 3.0，Overall 维持 3.5 不变**（因为 Soundness + Reproducibility 的高分足以支撑 Borderline Conference）。

### 分歧 2: Excitement 2.5 vs 3.5

见 W1 详细回应。核心分歧在于 "what is novel"——R2 评估的是 finding 的 surprise degree，我评估的是 question + framework 的 diagnostic utility。两者都是合理的 reviewer perspective，但 ARR guidelines 明确 Excitement 应评估 "personal interest level"，不仅是 surprise。

### 分歧 3: R2-W1 (triviality) vs 我的 S1 (有价值)

部分同意 R2。详见 W1 回应。

### 分歧 4: R2-W2/W3 vs 我的 W1

高度一致。R2-W3 的 single-environment concern 和我的 W1 (cross-environment probes 定位不精确) 指向同一个问题，但 R2 要求 "至少在一个额外 death-prone environment 做完整分析"，我认为这对 revision 来说 scope 过大。详见 W3 回应。

---

## 逐条回应 R2 Weaknesses

### R2-W1 [critical]: 核心发现 "obvious in hindsight"

**[REBUT]**（部分反驳）

R2 的论点是：给定 ScienceWorld 的 −100 death penalty + 43% vs 10% death rate，death dominance 是 "读到 setup 就能预见的结果"。这个论点有两个问题：

1. **78.9% label fraction 是 penalty-independent 的。** Algorithm 1（Section 2.2）的 labeling function 先按 survival 排序再比 score，不使用 P 值。即使 P=0，78.9% 的 non-tie labels 仍然由 death asymmetry 决定。R2 将 −100 penalty 和 label fraction 混为一谈了。真正的 "obvious" 部分是 DAF 随 P 增大而增大（我在 N1 中已指出），但 label fraction 本身是需要实验才能确定的。

2. **"Obvious in hindsight" 不等于 "known prior to this work"。** 如果 death dominance 是显而易见的，为什么同期的 routing 文献（When2Tool, Sun et al. 2026; Tool-Use-Tax, Zhang et al. 2026; To-Call-or-Not, Wu et al. 2026; RouteLLM, Ong et al. 2024）全部 focus on capability matching / preference data，没有一篇讨论 catastrophic failure 作为 routing signal？Section 4 (Related Work) 的文献综述恰恰说明了这一 gap。

**但我部分同意 R2 的 concern：** ScienceWorld 的 43% vs 10% death rate differential 是极端值。在 death rate 更接近的环境中（如 R2 建议的 P < 100 或 softer penalty），death dominance 可能不成立。论文的 Table 13 (Appendix K) 显示 P ≤ 25 时 correlation 不显著，暗示 death dominance 是 ScienceWorld 特定 penalty regime 下的现象，而非普遍规律。这确实限制了 excitement。

**结论：** R2 对 novelty 的质疑有合理成分，但 "obvious" 的判断过强。更准确的评价是 "the finding is environment-specific rather than surprising-or-not"。

### R2-W2 [critical]: Framing 内在张力（framework vs. finding）

**[AGREE]** R2-W2

R2 准确识别了论文的 identity crisis：标题是 finding-oriented（"Death Avoidance as the Dominant Routing Signal"），Contribution 1 是 framework，Abstract 两者并重，Conclusion 只有 finding。我的审稿没有单独列出这个问题，但它与我的 N1（DAF headline framing）和 W4（router diagnostic 定位模糊）根源相同——论文在 diagnostic framework 和 empirical finding 之间摇摆。

补充一点：如果论文选择 framework-centric 路线（"A Counterfactual Diagnostic Framework for Routing Signal Decomposition"），那么 death dominance 变成 case study 而非 main claim，novelty 质疑（R2-W1）就会被大幅缓解。反过来如果选 finding-centric，则需要更强的跨环境证据。当前的两头兼顾反而两头都不够强。

### R2-W3 [critical]: Single-environment + overclaimed scope

**[AGREE]** R2-W3，但对修改建议的 scope 有不同意见

R2 和我的 W1 指向同一个问题：MATH（null result）和 ALFWorld（不同机制）不能算 "cross-domain validation"，但 Abstract 的 "confirmed across four intervention axes and two cross-domain probes" 暗示了更强的泛化性。

**与 R2 的分歧在修改建议上：** R2 建议 "至少在一个额外 death-prone interactive environment 做完整分析"。这对 camera-ready revision 来说可能 scope 过大——完整分析需要新环境的 pure-strategy trajectory collection、labeling、bootstrap inference。更可行的修改是：(1) 明确限定 claims scope 为 "ScienceWorld with P=100"；(2) 将 MATH/ALFWorld 重定位为 "boundary consistency checks" 而非 "validation"。如果论文采用 framework-centric framing（见 W2 回应），single-environment 的问题会进一步缓解。

### R2-W4 [warning]: "Modality" 术语歧义

**[AGREE]** R2-W4

我的审稿遗漏了这个问题。"Modality" 在 NLP/multimodal 语境下几乎专指 text/image/audio/video。论文用它指 "computation mode"（internal reasoning vs. deterministic code execution）确实会造成严重歧义。建议改用 "computation mode" 或 "strategy"——论文已在多处使用 "strategy"（如 "pure-strategy trajectories", "internal strategy", "deterministic strategy"），统一术语即可。

### R2-W5 [warning]: Conclusion 过短

**[AGREE]** R2-W5

与我的 M5 一致。8 行 Conclusion 不匹配论文的工作量（8 页正文 + 13 页附录）。至少应讨论：(1) framework 对 router 设计的具体启示；(2) death regime 之外的 routing signal（non-death Δ_nd 虽小但非零）的潜在价值；(3) 与 safe RL 文献的 deeper connection。

### R2-W6 [warning]: 缺少不同 P 值的实际实验

**[AGREE]** R2-W6

我的审稿未单独提出这一点，这是 R2 的重要补充。Appendix K (Table 12-13) 的 penalty sensitivity 是基于已收集数据的数学重算（改变 Eq. 4-5 中的 P），而非在不同 P 值下实际运行 ScienceWorld。由于 ScienceWorld 的 death penalty 是硬编码的 −100，不同 P 值意味着修改环境本身或 post-hoc reweighting。论文做的是后者，但应明确说明这不是 actual re-running。

更关键的是：Table 13 显示 P ≤ 25 时 pearson correlation 不显著——这意味着 death dominance finding 依赖于 P 的 magnitude，进一步支持 R2-W1 的 "environment-specific" 质疑。

### R2-W7 [warning]: Safe RL Related Work 不够深入

**[AGREE]** R2-W7（部分同意）

论文在 Section 4 最后一段引用了 García & Fernández (2015)、Tamar et al. (2015)、Achiam et al. (2017)、CRPO (2021)、Moldovan & Abbeel (2012)、Ruan et al. (2024)、SafeRoute (2025)，覆盖了主要方向。但 R2 指出的 Altman (1999) CMDP 和 Mihatsch & Neuneier (2002) risk-sensitive RL 确实是 safe RL 的基础文献，缺失会让 safe RL 方向的 reviewer 不满。不过这属于 should-fix 而非 critical，因为论文的 core contribution 不在 safe RL 方法上。

### R2-W8 [warning]: Abstract 数字过密

**[REBUT]** R2-W8

这是主观判断。Abstract 确实数字密集，但每个数字都有明确指代（78.9% = label fraction，90.4% = DAF，245 = episodes，11 = task types 等）。对于 empirical/diagnostic 论文，数字是 Abstract 传达具体结论（而非 vague claims）的核心手段。ARR reviewer guidelines 未对 Abstract style 做限制。不过如果论文选择 framework-centric framing（见 W2），Abstract 可自然减少数字密度。

---

## 逐条回应 R2 Questions

### R2-Q1: 是否考虑在 P < 100 下运行实验？

与 W6 一致，这是合理要求。但 ScienceWorld 的 death penalty 是环境硬编码的，不是超参数。要做 P 变体实验需要 fork 环境，这是 non-trivial engineering。论文的 post-hoc reweighting (Appendix K) 是 reasonable approximation 但应明确说明。

### R2-Q2: 62% ties 是否说明 routing 缺乏价值？

**[REBUT]**（部分反驳）

152/245 = 62% ties 的含义需要 contextualize。在 ScienceWorld 的 97.4% sparse-reward steps 中（Section 4.2），大部分 episodes 两个 strategy 都 "successfully survive and get similar scores"——这正是 episode-level comparison 的优势：它跳过了 step-level noise，聚焦于有差异的 episodes。62% ties 说明的是 "多数任务两个 strategy 表现相当"，而非 "routing 无价值"。恰恰相反：在剩余 38% 有差异的 episodes 中，routing 的正确决策几乎完全由 death avoidance 驱动——这就是论文的 core finding。

不过 R2 的 implicit point 有道理：如果 62% 的时候两个 strategy 一样好，一个简单的 "always-deterministic" 策略（100% 时间用 deterministic）在实践中可能接近最优。论文在 Section 4.2 末尾提到 "always-deterministic" base rate 为 3.7% internal-preferred，间接支持了这一点。这进一步说明 finding 的实用影响有限。

### R2-Q3: SCI 是否掩盖了 task-type 集中？

**[REBUT]**

SCI ≤ 0.1（Appendix A）表示 death-rate differential 在 11 个 task types 中分布相对均匀（Gini coefficient 低）。Table 3 的 per-task data 可验证：虽然 top-3 tasks 的 death rate 较高，但 death dominance（det-preferred labels 来自 death asymmetry）在所有 11 个 task types 中一致。Leave-one-task-out analysis（Table 7）显示移除任何单个 task 后 DAF 变化 ≤ 3pp。R2 的 concern 在数据上不成立。

### R2-Q4: Death avoidance = 单个 action pattern bug avoidance？

**[AGREE]**

这与我的 Q2 一致。Section 5 (Discussion) 报告 "all 105 internal-strategy deaths trace to misuse of `focus on [object]`"。如果 death avoidance 实质上等于 "`focus on` avoidance"，那 routing signal 不是一个 general "avoid catastrophic reasoning failure" signal，而是一个 specific "avoid one buggy action pattern" signal。这有两个含义：(1) 对 ScienceWorld 的诊断价值降低（问题比 "routing signal decomposition" 更 narrow）；(2) 对其他环境的迁移性存疑（其他环境不一定有单一 dominant failure pattern）。论文应在正文（而非仅 Discussion 段落）更早讨论这一点。

### R2-Q5: Grounding ablation 降低 death → routing 角色？

**[AGREE]**（部分同意）

Appendix O 显示 action filtering（blocking `focus on`）将 death rate 从 ~43% 降至 ~29%，prompt warning 降至 ~35%。如果简单的 action filtering 能消除大部分 death，则 routing 的 practical motivation 确实被削弱——为什么要用复杂的 learned router 来避免一个可以通过 rule-based filter 解决的问题？

但论文可以辩护说：(1) Grounding ablation 是 task-specific intervention（需要知道哪个 action 危险），而 routing 是 general-purpose mechanism；(2) 29% residual death rate 仍然存在。不过这个辩护在 ScienceWorld 的语境下说服力有限，因为论文已经 identify 了 `focus on` 是 sole failure mode。

---

## 逐条回应 R2 Minor Issues

**R2-M1 (62% tie rate 讨论不足):** [AGREE] 与 Q2 同一问题。tie rate 的含义（routing 的 practical ceiling）值得在正文讨论。

**R2-M2 (Figure 2 字体小):** [AGREE] Figure 2 确实可改善可读性。

**R2-M3 (Appendix 过长):** [REBUT] 对于 diagnostic 论文，详细的 robustness checks 是必要的。ARR 允许 unlimited appendix。Appendix 的详尽程度恰恰是我给 Reproducibility 4.5 的原因。

**R2-M4 (webb-2023 年份):** [AGREE] 与我的 M3 一致。

**R2-M5 (AI assistants disclosure):** [AGREE] Responsible NLP Checklist E1 可以更具体。

---

## 对 R2 Missing References 的回应

- **Altman (1999) CMDP:** [AGREE] 基础文献，应加入 Safe RL 段落。
- **Mihatsch & Neuneier (2002) Risk-sensitive RL:** [AGREE] 与 death penalty 的 risk-sensitivity 直接相关。
- **Xi et al. (2025) LLM agent safety survey:** [AGREE] 增加 LLM safety 方向的连接。

---

## 综合评价调整

经 cross-review 后，我维持 **Overall 3.5 (Borderline Conference)**，但对以下维度有微调：

| 维度 | 原始分数 | 调整后 | 理由 |
|------|---------|--------|------|
| Soundness | 3.5 | 3.5 | 与 R2 一致，无变化 |
| Excitement | 3.5 | **3.0** | 接受 R2 关于 environment-specific finding 和 `focus on` single failure mode 的论点，novelty 确实受限 |
| Reproducibility | 4.5 | 4.5 | 无变化 |
| Overall | 3.5 | **3.5** | Soundness 和 Reproducibility 的高分 + framework 的诊断价值足以维持 Borderline Conference |

**与 R2 的 0.5 分差距解释：** R2 的 3.0 (Findings) 主要受 Excitement 2.5 驱动，而 2.5 基于 "obvious in hindsight" 判断。我认为该判断过强（见 W1 反驳），但接受 novelty 受限（Excitement 3.5→3.0）。剩余 0.5 差距来自我对 framework + robustness checks 的更高评价——论文的统计分析质量在同领域论文中突出（这一点 R2 在 S1 也承认），这在 ARR 的 Soundness 维度上应得到 credit。

**Revision 后的预期：** 如果论文在 revision 中 (1) 选择 framework-centric framing, (2) 充分辩护 K=11 bootstrap, (3) 限定 claims scope, (4) 处理 episode-to-step noise characterization，我预期 3.5→4.0 的上调空间。R2 的 3.0 在同样条件下也应有上调空间。

---

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

## 关键分歧点回应（Director 指定）

### 分歧 1：Overall 3.5 (R1) vs. 3.0 (R2)——0.5 分差距来源

差距主要来自 Excitement 维度（R1: 3.5, R2: 2.5），次要来自对 generalizability 的判断。

R1 将更多权重给了 **问题定义本身**（S1: "routing 到底在 route 什么信号"），我则更多关注 **answer 的可预测性**。经过交叉审阅，我承认 R1-S1 有道理——这个问题确实被 routing 文献忽视，正式提出并给出 formal decomposition 有独立价值。但我维持核心立场：一个好问题配一个在看到 setup（P=100, asymmetric death rates）后基本可预见的答案，对 Findings 足够，对 main conference 不够。

**我的调整**：Excitement 上调至 3.0/5（从 2.5），Overall 维持 3.0。理由见分歧 2。

### 分歧 2：Excitement 3.5 (R1) vs. 2.5→3.0 (R2 调整后)

R1 的逻辑：问题定义精准 + 被忽视 → exciting。
我的逻辑：问题好，但答案的 surprise value 低 → 限制 excitement。

部分让步：我此前过度聚焦于 "78.9% death dominance 是否 surprising"，而低估了 **formal diagnostic framework** 作为 reusable tool 的价值。Section 2 的 pure-strategy counterfactual + penalty-independent labeling（Algorithm 1, Appendix p.12）确实为后续研究提供了一个可迁移的诊断范式。

但我不完全同意 R1 的 3.5：
- 论文自己承认 DAF 是 "mathematical consequence"（Section 2.4），削弱了 discovery 感
- Practical takeaway 不明确——"routing 被 death avoidance 主导" 之后呢？论文没有给出 actionable design guidance（除了 Appendix Q 的 threshold routing 探索，结果还是 negative）
- Cross-environment probes 太浅（我和 R1 都指出了这点），限制了 framework 的 demonstrated 价值

最终：Excitement 3.0/5。问题定义值 0.5 分上调，但答案的 predictability 和 limited practical impact 阻止更高分。

### 分歧 3：R1-S1 是否缓解我的 W1 (obvious in hindsight)

**部分缓解，不完全消除。**

R1-S1 正确指出：routing 文献关注 "how to route" 而忽视 "what to route"——这是一个被忽视的元问题。我同意这个 framing contribution 有独立价值。

但 W1 的核心不是 "问题不值得问"，而是 "答案在已知 setup 后是否 non-obvious"。具体来说：
- ScienceWorld 的 death penalty P = −100（Section 2.3, page 3）
- Internal strategy death rate ~43%, deterministic ~10%（Table 1, page 5）
- 在 4:1 的 death rate asymmetry + extreme penalty 下，death avoidance 成为 dominant routing signal 是一个合理的 prior prediction

R1-S1 缓解了 W1 的程度：问题本身有价值，即使答案 partially expected，formalization 和 quantification（78.9% 的具体数字、SCI 的集中度）仍然 informative。
R1-S1 未缓解的部分：如果一位熟悉 ScienceWorld 的 reviewer 在读到 Section 2.1-2.3 后就能猜到 "death avoidance 会主导"，那 finding 的 novelty ceiling 是 Findings 而非 main conference。

**结论**：W1 从 "critical" 降级为 "critical-but-mitigated"。问题定义的贡献部分补偿了答案的可预见性，但不足以将论文提升到 Conference 级别。

### 分歧 4：R1-N3 (episode-to-step label projection noise) 是否削弱 router diagnostic 价值

**[AGREE] R1-N3 提出了一个重要的替代假说，我在初审中未充分考虑。**

R1 的论点：97.4% step-level ties → episode label 投射到 step level 时引入系统性噪声 → router 失败可能是 **label noise** 而非 **signal inherently not step-level learnable**。

这个替代假说改变了论文 Section 3.6 的解读：
- **论文当前解读**："step-level router ≈ chance → routing signal 本质上不是 step-level 的"
- **R1 替代解读**："step-level router ≈ chance → label 太 noisy，信号可能存在但被噪声淹没"

两者的 implication 截然不同：
- 如果是论文的解读 → routing fundamentally limited，需要 episode-level 信号
- 如果是 R1 的解读 → 用更好的 labeling（如只用 death event 附近的 steps）可能训练出有效 router

我认为 R1 的替代假说 **更有说服力**：
1. 论文自己报告 60.3% 的 steps 是 "pre-event neutral"（Section 3.6, page 5-6），这意味着大多数 training samples 的 label 没有信息量
2. 仅 0.3% steps 有 "strict directional conflict"——噪声极低但 **有效信号也极稀疏**
3. 在 noisy label learning 文献中，>95% 的 uninformative labels 足以让任何 classifier 退化到 chance

**对论文的影响**：这不改变核心 finding（78.9% death asymmetry），但显著削弱了 Section 3.6 的诊断性结论。论文应该：(a) 测试 R1 建议的 step-level label refinement baseline；(b) 或者明确声明 router failure 的原因是 label sparsity 而非 fundamental non-learnability。

---

## 逐条回应 R1 Weaknesses

### Must-Fix

**[AGREE] R1-N1: DAF headline number 的误导性。**
与我的 W1 一致。DAF = 90.4% 是 penalty-dependent 的数学推导结果（Section 2.4 承认 "mathematical consequence"），不应与 penalty-independent 的 78.9% 并列为 headline。R1 的建议（78.9% 为 primary，DAF 为补充）是正确的修改方向。

补充：我在初审中更进一步质疑了 DAF 作为 metric 的 novelty——如果它是 P 的单调函数且论文没有实际做不同 P 值的实验（仅数学推导，Appendix K Table 12），那 DAF 的经验价值有限。

**[AGREE] R1-N2: Cluster bootstrap K=11 低于公认阈值。**
这是我初审中遗漏的一个重要统计问题。R1 正确引用了 Cameron et al. (2008) 的 K ≥ 20-40 建议和 Webb (2023) 的 size distortion 证据。

补充论点：
- K=11 下 2^11 = 2048 permutations，p-value 的分辨率只有 ~1/2048 ≈ 0.0005，这意味着 p=0.002 只比最小可报告值大 4 倍
- Cohen's d = 3.02 虽然很大，但在 K=11 下受单个 outlier task type 影响的风险较高——特别是 `find-non-living-thing`（zero death in both strategies）如果被移除，effect size 可能变化显著
- 论文的 leave-one-task-out analysis（Appendix G, Table 7）部分缓解了这个问题（DAF range 75.9%-78.9% when removing any single task），但 R1 要求的 "worst-case leave-one-cluster-out" 是更严格且合理的检验

**然而**，我也注意到论文提供了多种互补的 robustness evidence（8-seed, Appendix J; per-task CIs, Appendix F; exact permutation test p=0.002, Table 6），这些共同构成了比单一 cluster bootstrap 更强的证据链。R1-N2 的严重程度因此应从 "critical" 略降为 "critical-but-partially-mitigated"。

**[AGREE] R1-N3: Episode-to-step label projection 的系统性噪声。**
如上文分歧 4 详述。R1 提出了 router 失败的一个更可能的解释——label noise 而非 fundamental non-learnability。论文应测试 death-event-proximal labeling 作为 baseline。

补充：即使使用 refined labels，我预测 router 仍然难以泛化到 non-death-prone tasks（因为 non-death component Δ_nd 太小，Section 2.4 报告仅 0.23 ppt）。但这个实验至少能区分 "label noise" 和 "no step-level signal" 这两个假说。

### Should-Fix

**[AGREE] R1-W1: Cross-environment probes 措辞过强。**
与我的 W3 完全一致。MATH 是 null result（无 death → 无法验证 death dominance），ALFWorld 发现了不同机制（information asymmetry 而非 death），两者都不构成 "validation"。定位为 "boundary probes" 或 "consistency checks" 更准确。

**[AGREE] R1-W2: Pure-strategy 设计的外部效度。**
这是我初审中未提出的有价值论点。在真实 routing 中，step-level switching 可以在 internal strategy 即将触发 death 时切换到 deterministic，从而 **避免 death 而不放弃 internal reasoning 的全部收益**。Pure-strategy comparison 假设 episode-level 全程使用一种 strategy，这可能高估了 death asymmetry 的 routing 影响。

不过，论文的 step-level router probe（Section 3.6）的失败结果反过来 complicate 了这一点——如果 step-level 信号太弱以至于 router 无法学习，那么 step-level switching 在实践中也很难实现。R1-W2 和 R1-N3 实际上形成了一个 tension：W2 说 pure-strategy 高估问题，N3 说 step-level router 的失败可能是 label 问题而非 signal 问题。如果 N3 成立（label noise 导致 router 失败），那 W2 的担忧就更严重（step-level routing 可能 feasible，且能降低 death asymmetry 的影响）。

**[AGREE] R1-W3: Reflexion dose-response 统计功效。**
N=5 trials × 10 death-prone tasks → 50 data points at the maximum。Appendix H（Table 8, page 14）显示 per-task variance 在 N=3,4,5 时 high（up to 25pp range），aggregate smooth 到 2.5pp band，但 individual task 层面 power 不足。R1 建议的 power analysis 或更多 trials 是合理的。

**[AGREE with nuance] R1-W4: Router diagnostic probe 定位与 contribution claim 的张力。**
R1 正确指出 step-level 56-59% ≈ chance 应更明确框架为 negative result。但我认为论文在 Section 3.6 和 Discussion（Section 5, "Why the router fails"）中已经比较 candid 地讨论了这个 negative result。问题不在于是否承认了 negative，而在于 **interpretation**——论文将其解读为 "signal inherently not step-level"，但 R1-N3 提供了更合理的 "label noise" 替代解释。

### Minor

**[AGREE] R1-M1 (Table 1 weighting):** 是的，Table 1 应明确说明 episode-weighted vs. task-weighted。
**[AGREE] R1-M2 (Figure 2 Spearman's rho):** Caption 中报告 Spearman's rho 是更 robust 的非参数替代，且论文已有 Pearson r = 0.97（Section 3.1, page 4）。
**[AGREE] R1-M3 (Webb 2023 年份):** 与我的 M4 一致。OpenAlex 匹配到 2014 年版本。
**[AGREE] R1-M4 (Appendix R 阈值选择):** 阈值 routing 的 threshold 选择确实缺乏理论依据。
**[AGREE] R1-M5 (Conclusion 过短):** 与我的 W5 一致。

---

## 逐条回应 R1 Questions

**R1-Q1 (DAF 在 Δ_nd < 0 时如何解释):**
好问题。当 Δ_nd < 0 时（即 non-death component 倾向 internal），DAF > 1，意味着 death avoidance "过度补偿"了 non-death advantage。数学上成立，但 semantically 需要注意——DAF > 1 不意味着 "超过 100% 归因于 death"，而是说 death penalty 不仅抵消了 internal 的 non-death 优势，还反转了 routing preference。论文应在 Section 2.4 明确讨论这种情况。

**R1-Q2 (105 deaths 全来自 focus on):**
与我的 Q4 和 Q5 完全对齐。这是我认为最有杀伤力的质疑之一——如果 "death avoidance" 本质上是 "避免一个特定 action pattern"，那论文的 generalizability claim 被严重削弱。Appendix O 的 grounding ablation 显示 blocking `focus on` 降低 death rate 至 29.0%（从 ~43%），证明单一 action pattern 确实是 death 的主要来源。

**R1-Q3 (Grounding per-task variation):**
合理的后续问题。Appendix O 报告的是 aggregate 效果，per-task breakdown 会更有信息量。

**R1-Q4 (3.7% internal-preferred → always-det 接近最优):**
**这是一个 devastating 的 observation**，与我的 M1（62% tie rate）互补。如果仅 3.7% 的 episodes 选 internal 优于 deterministic，且 96.3% 的情况下 deterministic 等于或优于 internal，那么 routing 本身的 practical value 就极低——always-deterministic 已经接近最优。论文应该在 Discussion 中更直接地面对这个 implication：不是 "routing 被 death avoidance 主导"，而是 "routing 在当前 setup 下几乎不必要"。

**R1-Q5 (Llama DAF):**
论文 Section 3.2（page 5）报告 Llama-3.1-8B 的 death rate differential 一致（11.4% internal vs. 11.4% deterministic），DAF "remains intact"，但 **未给出具体 DAF 数值**。R1 要求报告具体数字是合理的——"intact" 太模糊。

---

## R1 Missing References 回应

**[AGREE] Cost-aware routing 中的 risk-sensitive 策略:** 与我建议的 Mihatsch & Neuneier (2002) 和 CMDP (Altman, 1999) 方向一致。
**[NEUTRAL] Agent failure taxonomy (Wang et al. 2024):** 可能有参考价值，但不确定与论文的 failure taxonomy（Appendix N）是否直接可比。
**[AGREE] Noisy label learning (Natarajan et al. 2013):** 如果采纳 R1-N3 的 label noise 解释，这些文献就变得高度相关。

---

## 总结：与 R1 的共识与分歧

### 共识（高一致性）
- DAF headline 需降级 (R1-N1 ≈ my W1)
- Cross-environment probes 措辞过强 (R1-W1 ≈ my W3)
- Conclusion 过短 (R1-M5 ≈ my W5)
- Webb 年份问题 (R1-M3 ≈ my M4)
- `focus on` single-action 问题 (R1-Q2 ≈ my Q4)

### R1 提出而我初审遗漏的有价值论点
- **R1-N2 (K=11 cluster bootstrap):** 有效的统计方法论质疑
- **R1-N3 (label noise 替代假说):** 改变了 router failure 的 interpretation
- **R1-W2 (pure-strategy 外部效度):** 对 death asymmetry 估计的 upward bias
- **R1-Q4 (3.7% → routing 本身价值存疑):** 论文未充分讨论

### 我提出而 R1 未覆盖的论点
- **R2-W2 (framework vs. finding framing tension):** 标题和 contributions 之间的定位不清
- **R2-W4 (modality 术语歧义):** NLP venue 下的术语混淆
- **R2-W6 (penalty variation 缺实验):** DAF 仅有数学推导，无实际实验验证
- **R2-W7 (Safe RL 讨论不足):** 与 CMDP/risk-sensitive RL 的理论连接缺失

### 核心分歧
- **Excitement**: R1 3.5 vs. R2 3.0（调整后）。我承认问题定义有独立价值，但维持答案的可预见性限制了 excitement ceiling。
- **Overall**: R1 3.5 vs. R2 3.0。我认为 Findings 更合适——方法论扎实但 novelty 不足以支撑 main conference。R1 的 Borderline Conference 评价可能受益于对 framework reusability 的更乐观评估。

**建议 Director 关注的核心 resolution point**: R1-Q4（3.7% internal-preferred rate → routing 价值本身存疑）和 R1-N3（label noise 替代假说）如果被作者有效回应（如增加 penalty variation 实验 + death-proximal labeling baseline），论文可达 3.5；否则维持 3.0。


---

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。核心结论：

- R1 的 11 个 Weaknesses/Questions 中，我 **全部 AGREE 或 AGREE with nuance**，无 REBUT。R1 的审稿质量很高。
- R1 提出了 3 个我初审遗漏的重要论点：**K=11 cluster bootstrap 不足**（N2）、**label noise 替代假说**（N3）、**pure-strategy 外部效度**（W2）。
- Excitement 从 2.5 上调至 **3.0**，承认问题定义的独立价值，但维持 Overall **3.0 (Findings)**——答案的可预见性和 cross-environment 证据不足限制了 main conference 级别的 novelty。
- 给 Director 的关键建议：R1-Q4（routing 价值本身存疑）和 R1-N3（label noise 假说）是 rebuttal 中最需要作者回应的两个点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1746 · 2026-05-19T16:02:24.105234+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "report": "# 审稿报告（修订版）：Death Avoidance as the Dominant Routing Signal\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 (Long Paper via ARR)\n**Deadline**: 2026-05-25\n**Round**: 19 (fresh review)\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）\n**修订原因**: 交叉回应后 Excitement 收敛（R1 3.5→3.0, R2 2.5→3.0）、新增关键共识点\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，将 modular LLM agent 的 routing signal 分解为 death-avoidance 和 non-death 两个成分。在 ScienceWorld（11 task types, 245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的 non-tie routing labels 源于 death asymmetry：internal strategy 因幻觉触发 catastrophic death（−100 penalty），而 deterministic strategy 存活。DAF 在 P=100 下达 90.4%。Cross-model replication（Llama-3.1-8B）、four intervention axes（retry, Reflexion, 72B scaling, action filtering）、cross-environment probes（MATH, ALFWorld）进一步支持诊断。Router 训练（Qwen3 LoRA, 0.6B-4B）step-level 接近 chance，episode-level 仅 4B 有边际改善。\n\n---\n\n## Strengths\n\n**S1. 问题定义精准且有价值。** [R1-S1, R2 交叉后同意] 现有 routing 文献关注\"怎么 route\"（Toolformer, ART, Chameleon, CogRouter, When2Tool），本文追问\"routing 到底在 route 什么信号\"——这是一个被忽视的诊断性问题。R2 在交叉回应中承认此贡献有独立价值，将 Excitement 从 2.5 上调至 3.0。\n\n**S2. Pure-strategy counterfactual 设计干净。** [R1-S2, R2-S4, 强共识] 控制相同 random seed + initial conditions，episode-level labeling function（Algorithm 1）death-aware 且 penalty-independent。\n\n**S3. 统计分析超同类水准。** [R1-S4, R2-S1, 强共识] Episode-level bootstrap（B=10,000）、wild cluster bootstrap、per-task CIs、8-seed robustness、Cohen's d=3.02。R1 Reproducibility 4.5/5，R2 4/5。\n\n**S4. Robustness checks 全面。** [强共识] Leave-one-task-out DAF（75.9%-78.9%）、penalty sensitivity（Appendix K）、cross-model replication、anti-cherry-picking analysis（18/19 excluded types 也 death-dominated, ΔDR=+38.2pp）、SCI=0.2147。\n\n**S5. Negative results 诚实呈现。** [R2-S2, 强共识] Router step-level ≈ chance、data augmentation 无效——对社区有价值，呈现坦诚。\n\n**S6. Cross-model validation。** [R2-S5, 共识] Llama-3.1-8B 复制（11 tasks, N=220）direction consistency 10/10，death dominance 跨模型稳定。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [Critical, 强共识] DAF headline framing 误导。**\n- R1-N1 首提，R2 完全同意。Abstract 和 §3.1 以 \"DAF = 90.4%\" 为 headline，掩盖其 penalty-dependent 本质。DAF = δP/(δP + Δ_nd) 随 P 单调递增是数学后果，在 Δ_nd ≈ +2.84 且 P=100 时 DAF 接近 1 是代数必然。78.9% label fraction 才是 penalty-independent 的 robust finding。\n- R2 在交叉回应中补充：\"如果 DAF 是 P 的单调函数且论文没有实际做不同 P 值实验（仅数学推导），那 DAF 的经验价值有限。\"\n- **Action**: Abstract 以 78.9% 为 primary metric；§3.1 段落重组，DAF 降为 derived quantity；增加 DAF 在 Δ_nd<0 边界行为讨论。\n\n**MF2 [Critical, 部分共识] 核心发现 novelty 不足——\"obvious in hindsight\"。**\n- R2-W1 首提（Critical），R1 部分 REBUT。\n- **R1 的辩护**：(1) 78.9% label fraction 是 penalty-independent 的，不能从 P=100 setup 直接推出；(2) 同期 routing 文献（When2Tool, Tool-Use-Tax, RouteLLM 等）全部聚焦 capability matching，无一讨论 catastrophic failure 作为 routing signal——如果 death dominance 真的 obvious，为什么无人验证？\n- **R2 的回应**：承认问题定义有独立价值（Excitement 2.5→3.0），但维持 \"一个好问题配一个可预见的答案，对 Findings 够，对 main conference 不够\"。\n- **交叉后状态**：R1 Excitement 3.5→3.0，R2 2.5→3.0，**Excitement 收敛至 3.0/5**。分歧从 1.0 gap 缩小为 0，但 Overall 仍有 0.5 差距（R1: 3.5, R2: 3.0），因为 R1 认为 Soundness+Reproducibility 的高分足以补偿 Excitement。\n- **Director 裁决**: 维持 Critical。问题定义的贡献部分缓解了 triviality concern，但 EMNLP reviewer panel 中 excitement deficit 是常见 rejection reason。当前 non-triviality 论证（§5）力度不足。\n- **Action**: 三角度强化：(1) routing 文献 prior assumptions 与实证的反差；(2) intervention resistance 的 non-predictability；(3) cross-model δ stability 作为结构性发现。\n\n**MF3 [Critical, 强共识] Framing 内在张力——framework vs finding 定位不清。**\n- R2-W2 首提，R1 在交叉回应中完全同意（\"论文在 diagnostic framework 和 empirical finding 之间摇摆\"）。R1 补充了关键观察：\"如果选择 framework-centric 路线，novelty 质疑（R2-W1）就会被大幅缓解。\"\n- **Action**: 选择一个主线贯穿标题/Abstract/Contributions/Conclusion。推荐 framework-centric——既缓解 novelty concern，又对 single-environment scope 更 tolerant。\n\n**MF4 [Critical, 强共识] Cluster bootstrap K=11 低于公认阈值。**\n- R1-N2 首提（Critical），R2 在交叉回应中完全同意并补充了额外论据：(1) p=0.002 仅比最小可报告值 (1/2048 ≈ 0.0005) 大 4 倍；(2) `find-non-living-thing` (zero death) 作为 outlier 可能影响 effect size。\n- **缓解因素**（R2 同时指出）：多种互补 robustness evidence（8-seed, per-task CIs, exact permutation）共同构成比单一 cluster bootstrap 更强的证据链。两位 reviewer 均认为 \"critical-but-partially-mitigated\"。\n- **Action**: 正文以 non-clustered bootstrap 为主推断；cluster bootstrap 定位为 conservative sensitivity check；增加 K=11 vs K≥40 的显式讨论。\n\n**MF5 [Critical, 强共识] Episode→step label projection 噪声——router diagnostic 价值严重受损。**\n- R1-N3 首提（Critical），R2 在交叉回应中称其为 \"比论文的解释更有说服力的替代假说\"。\n- **核心分歧转变**: 论文解读 = \"step-level signal 本质上不存在\"；R1 替代假说 = \"signal 可能存在但被 ~88% noise/uninformative label 淹没\"。两位 reviewer 均倾向 R1 解释。\n- R2 进一步指出 R1-W2（pure-strategy 外部效度）和 R1-N3 形成 tension：如果 label noise 是 router 失败原因（N3），则 step-level routing 可能 feasible，那 pure-strategy 对比高估 death asymmetry（W2）就更严重。\n- **Action**: §3.6 明确区分两种解释；测试 death-proximal labeling baseline（如只用 death event 附近 steps 训练）；或明确声明 router failure 是 label sparsity 而非 fundamental non-learnability。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1 [Warning, 强共识] Cross-environment probes 定位过强。**\n- R1-W1 和 R2-W3 一致。MATH = unfalsifiable null result，ALFWorld = 不同机制。Abstract \"cross-domain probes\" 措辞需弱化为 \"boundary probes/consistency checks\"。\n\n**SF2 [Warning, 共识] 缺少 penalty magnitude 的实际实验验证。**\n- R2-W6 首提，R1 在交叉回应中完全同意。Appendix K 的 DAF vs P 是数学推导而非实验。R1 补充：Table 13 显示 P ≤ 25 时 correlation 不显著——\"death dominance 是 ScienceWorld 特定 penalty regime 下的现象\"。\n\n**SF3 [Warning, 共识] Pure-strategy 设计的外部效度。**\n- R1-W2 首提，R2 同意并补充了与 R1-N3 的 tension 关系。\n\n**SF4 [Warning, 强共识] Conclusion 过于简短（2 句话）。**\n\n**SF5 [Warning, 强共识] Safe RL Related Work 不够深入。**\n- 缺 CMDP (Altman 1999) 和 risk-sensitive RL 与 death avoidance 的理论映射。\n\n**SF6 [Warning, R2 首提, R1 部分 REBUT] Abstract 数字过密。**\n- R1 认为 \"每个数字都有明确指代，empirical 论文需要具体数字\"。R2 维持 concern。\n- **Director 裁决**: 如采用 framework-centric framing，Abstract 可自然减少数字密度（R1 观点）。列为 Should-Fix。\n\n**SF7 [Warning, 强共识] \"Modality\" 术语歧义。**\n\n**SF8 [Warning, R1 首提] Reflexion dose-response N=5 统计功效不足。**\n\n**SF9 [Warning, 交叉后新增共识] Routing 的 practical value 本身存疑。**\n- R1-Q4 首提，R2 在交叉回应中称之为 \"devastating observation\"。3.7% internal-preferred base rate + 96.3% oracle 选择 always-deterministic → always-deterministic 在实际部署中已接近最优。62% tie rate（R2-M1）进一步支持——大多数 episodes routing 选择无差异。\n- **Action**: §5 Discussion 直接面对这个 implication：不仅 \"routing signal 被 death avoidance 主导\"，更进一步 \"routing 在当前 setup 下几乎不必要\"——这本身是一个有价值的诊断性结论。\n\n### Minor\n\n**m1 [Info, 共识]** 62% tie rate 含义需在正文讨论。\n\n**m2 [Info, R1]** Figure 2 caption 报告 Spearman's ρ。\n\n**m3 [Info, 强共识]** `webb-2023` 年份需确认（2014 WP vs 2023 journal）。\n\n**m4 [Info, R1]** Appendix R 阈值选择缺理论依据。\n\n**m5 [Info, R2]** AI assistants disclosure 建议更具体。\n\n**m6 [Info, 共识]** Missing references: Altman (1999) CMDP, Mihatsch & Neuneier (2002), Natarajan et al. (2013) noisy label learning。\n\n**m7 [Info, R1]** Table 1 weighting scheme（episode-weighted vs task-weighted）需明确。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** [R1-Q1, R2-W6] DAF 公式假设 Δ_nd 不随 P 变化——是否在 P≠100 的 ScienceWorld 变体上做过实际验证？Appendix K 是数学推导还是实际实验？\n\n**Q2.** [R1-Q2, R2-Q4, 强共识] 105 internal deaths 全来自 `focus on [object]` 误用——death avoidance 是否等价于 single-action bug avoidance？Grounding ablation 降至 29%，residual gap ≥12pp。如果修复该 pattern，death dominance 是否消失？\n\n**Q3.** [R2-Q2, SF9] 62% tie rate + 3.7% internal-preferred base rate → routing 在大多数情况下无差异，always-deterministic 接近最优。论文如何看待这一 observation 对 routing 价值的影响？\n\n**Q4.** [R1-N3, 强共识] Router near-chance accuracy 是因为 death signal 本质上不是 step-level 的，还是因为 episode-level labels 投射到 steps 时 ~88% noise/uninformative rate？是否考虑过 death-proximal labeling（只用 death event 附近 steps 训练）？\n\n**Q5.** [R1-Q5] Llama cross-model replication 的完整 DAF 是多少？\"intact\" 太模糊，需要具体数字。\n\n**Q6.** [R2-Q3] SCI=0.2147 但 top-3 task types 占 39.8% total death-rate differential——death dominance 是 task-type specific 还是 environment-wide？\n\n---\n\n## Missing References\n\n- **Altman, E. (1999). Constrained Markov Decision Processes.** Death avoidance 作为 implicit constraint 的理论对应。[R2, R1 同意]\n- **Mihatsch & Neuneier (2002). Risk-sensitive RL.** 与 catastrophic failure avoidance 直接相关。[R2, R1 同意]\n- **Natarajan et al. (2013). Learning with Noisy Labels.** 为 ~88% uninformative label rate 下的 router near-chance accuracy 提供理论 grounding。[R1, R2 同意]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户选择不提交）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 超时（elapsed 727s）。无排版审查结果。\n\n**基于 PDF 阅读的基本格式确认**:\n- ✅ 正文 8 页（§1-§6 在 p1-p8），符合 ≤8 页要求\n- ✅ Limitations（p8-9），具体且坦诚\n- ✅ Ethics Statement（p9）\n- ✅ Double-blind: \"Anonymous ACL submission\"\n- ✅ ACL 模板 + [review] option\n- ✅ Figures/Tables 位置合理\n- ⚠️ webb-2023 年份需确认\n\n---\n\n## Reviewer Consensus（交叉回应后最终状态）\n\n### 完全收敛\n| 议题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| DAF headline framing (MF1) | Critical | Critical | ✅ 强共识 |\n| K=11 cluster bootstrap (MF4) | Critical | Agrees (critical-but-mitigated) | ✅ 共识 |\n| Episode→step noise (MF5) | Critical | Agrees (\"更有说服力\") | ✅ 强共识 |\n| Framing tension (MF3) | Agrees | Critical | ✅ 强共识 |\n| Cross-env overclaimed (SF1) | Should-Fix | Critical→Should-Fix | ✅ 共识 |\n| Routing practical value (SF9) | Q4 (\"devastating\") | Agrees | ✅ 强共识（交叉后新增） |\n| **Excitement** | **3.5→3.0** | **2.5→3.0** | **✅ 收敛至 3.0** |\n| Soundness | 3.5 | 3.5 | ✅ 一致 |\n| Reproducibility | 4.5 | 4 | ✅ 基本一致 |\n\n### 残余分歧\n| 议题 | R1 | R2 | 差异 |\n|------|----|----|------|\n| **Overall Score** | **3.5** (Borderline Conference) | **3.0** (Findings) | **0.5 gap** |\n| Abstract density (SF6) | REBUT | Should-Fix | 主观分歧 |\n\n**0.5 分残余差距根源**: R1 认为 Soundness 3.5 + Reproducibility 4.5 的高分足以在 Excitement 3.0 下支撑 Borderline Conference；R2 认为 Excitement 3.0 的 novelty ceiling 决定了 Findings 更合适。两者均为合理的 reviewer perspective。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0–3.5（Findings 至 Borderline Conference）**\n\n**维度汇总（交叉回应后最终值）**:\n| 维度 | R1 (调整后) | R2 (调整后) | 综合 |\n|------|------------|------------|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | **3.0/5** | **3.0/5** | **3.0/5** |\n| Reproducibility | 4.5/5 | 4/5 | **4.25/5** |\n| Clarity | — | 3/5 | **3/5** |\n\n**综合评估**:\n\n论文问了一个重要且被忽视的诊断性问题，给出了清晰的回答，counterfactual 设计干净，统计分析超过同类水准，robustness checks 全面，negative results 诚实呈现。\n\n核心问题：\n1. **DAF framing 误导**（MF1）——低成本修复\n2. **Novelty 受限但非 trivial**（MF2）——Excitement 收敛至 3.0，问题定义有价值但答案可预见性限制了 ceiling\n3. **Framing 不统一**（MF3）——需选择 framework-centric 或 finding-centric 主线\n4. **K=11 统计推断**（MF4）——通过 non-clustered bootstrap 为主推断来缓解\n5. **Router diagnostic 受 label noise 污染**（MF5）——需区分 label noise vs fundamental non-learnability\n6. **Routing 的 practical value 本身存疑**（SF9, 交叉后新增强共识）——3.7% internal-preferred + 62% ties → always-deterministic 几乎最优\n\n**Revision 路径**:\n- **提升至 Conference (3.5-4.0) 的条件**: (1) 选择 framework-centric framing（同时缓解 MF2 和 MF3）；(2) K=11 辩护充分（MF4，低难度）；(3) DAF framing 修正（MF1，低难度）；(4) death-proximal labeling baseline 或 clear attribution（MF5）；(5) §5 直面 routing practical value 问题（SF9）\n- **如果 MF2 (novelty) 和 SF9 (routing value) 无法有效回应，更可能落在 Findings (3.0)**\n\n---\n\n## Detailed Comments\n\n### Title & Abstract\n- 标题聚焦 finding 但 Contribution 1 是 framework——需统一（MF3）\n- Abstract 以 78.9% 为 primary，DAF 降为补充（MF1）\n- 如采用 framework-centric framing，数字密度可自然降低（SF6）\n\n### §1 Introduction\n- 问题定义清晰，逻辑链通畅\n- Contributions 列表需重组以匹配选定的 framing 主线\n\n### §2 Method\n- 写作最清晰的部分\n- Algorithm 1 设计合理\n- §2.4 Scope of episode-level analysis 段需更强调 episode→step gap implications\n- DAF 需更 upfront 承认是 derived quantity\n\n### §3 Experiments\n- §3.1 核心实证清晰，但段落结构需修正（78.9% 先于 DAF）\n- §3.2 Cross-model 缺 Llama DAF 具体数字\n- §3.3 Agent improvement 有价值；72B DAF=92.4% 说明 scaling 不消除 death dominance\n- §3.4 Cross-env 过于浅显，需重定位为 boundary probes\n- §3.5 Oracle degeneracy (96.3% always-det) 和 3.7% internal-preferred 需更突出讨论\n- §3.6 Router 应明确框架为 negative result；区分 label noise vs signal non-learnability\n\n### §4 Related Work\n- Tool Use / Adaptive Routing 覆盖充分\n- **Safe RL 需扩展**——补 CMDP, risk-sensitive RL 理论连接\n\n### §5 Discussion\n- \"Non-triviality\" 论证力度不足（MF2 核心）\n- \"Anatomy of catastrophic failure\"——105 deaths 全来自 `focus on`，implications 需更深讨论\n- **需新增**: routing practical value 的直接讨论（SF9）\n- **需新增**: pure-strategy vs mixed-strategy gap 估计（SF3）\n\n### §6 Conclusion\n- 严重不足——2 句话，需扩展至 ~0.5 页\n\n### Limitations\n- 覆盖面 adequate，但缺 \"P=100 specific\" 限制的明确讨论\n\n### 格式合规\n- ✅ 正文 8 页 | ✅ Limitations | ✅ Ethics | ✅ Double-blind | ✅ ACL template\n- ⚠️ webb-2023 年份 | ⚠️ modality 术语",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0-3.5 (Findings to Borderline Conference)",
  "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "simgate-modular-routing",
    "report": "# 审稿报告（修订版）：Death Avoidance as the Dominant Routing Signal\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 (Long Paper via ARR)\n**Deadline**: 2026-05-25\n**Round**: 19 (fresh review)\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）\n**修订原因**: 交叉回应后 Excitement 收敛（R1 3.5→3.0, R2 2.5→3.0）、新增关键共识点\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，将 modular LLM agent 的 routing signal 分解为 death-avoidance 和 non-death 两个成分。在 ScienceWorld（11 task types, 245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的 non-tie routing labels 源于 death asymmetry：internal strategy 因幻觉触发 catastrophic death（−100 penalty），而 deterministic strategy 存活。DAF 在 P=100 下达 90.4%。Cross-model replication（Llama-3.1-8B）、four intervention axes（retry, Reflexion, 72B scaling, action filtering）、cross-environment probes（MATH, ALFWorld）进一步支持诊断。Router 训练（Qwen3 LoRA, 0.6B-4B）step-level 接近 chance，episode-level 仅 4B 有边际改善。\n\n---\n\n## Strengths\n\n**S1. 问题定义精准且有价值。** [R1-S1, R2 交叉后同意] 现有 routing 文献关注\"怎么 route\"（Toolformer, ART, Chameleon, CogRouter, When2Tool），本文追问\"routing 到底在 route 什么信号\"——这是一个被忽视的诊断性问题。R2 在交叉回应中承认此贡献有独立价值，将 Excitement 从 2.5 上调至 3.0。\n\n**S2. Pure-strategy counterfactual 设计干净。** [R1-S2, R2-S4, 强共识] 控制相同 random seed + initial conditions，episode-level labeling function（Algorithm 1）death-aware 且 penalty-independent。\n\n**S3. 统计分析超同类水准。** [R1-S4, R2-S1, 强共识] Episode-level bootstrap（B=10,000）、wild cluster bootstrap、per-task CIs、8-seed robustness、Cohen's d=3.02。R1 Reproducibility 4.5/5，R2 4/5。\n\n**S4. Robustness checks 全面。** [强共识] Leave-one-task-out DAF（75.9%-78.9%）、penalty sensitivity（Appendix K）、cross-model replication、anti-cherry-picking analysis（18/19 excluded types 也 death-dominated, ΔDR=+38.2pp）、SCI=0.2147。\n\n**S5. Negative results 诚实呈现。** [R2-S2, 强共识] Router step-level ≈ chance、data augmentation 无效——对社区有价值，呈现坦诚。\n\n**S6. Cross-model validation。** [R2-S5, 共识] Llama-3.1-8B 复制（11 tasks, N=220）direction consistency 10/10，death dominance 跨模型稳定。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [Critical, 强共识] DAF headline framing 误导。**\n- R1-N1 首提，R2 完全同意。Abstract 和 §3.1 以 \"DAF = 90.4%\" 为 headline，掩盖其 penalty-dependent 本质。DAF = δP/(δP + Δ_nd) 随 P 单调递增是数学后果，在 Δ_nd ≈ +2.84 且 P=100 时 DAF 接近 1 是代数必然。78.9% label fraction 才是 penalty-independent 的 robust finding。\n- R2 在交叉回应中补充：\"如果 DAF 是 P 的单调函数且论文没有实际做不同 P 值实验（仅数学推导），那 DAF 的经验价值有限。\"\n- **Action**: Abstract 以 78.9% 为 primary metric；§3.1 段落重组，DAF 降为 derived quantity；增加 DAF 在 Δ_nd<0 边界行为讨论。\n\n**MF2 [Critical, 部分共识] 核心发现 novelty 不足——\"obvious in hindsight\"。**\n- R2-W1 首提（Critical），R1 部分 REBUT。\n- **R1 的辩护**：(1) 78.9% label fraction 是 penalty-independent 的，不能从 P=100 setup 直接推出；(2) 同期 routing 文献（When2Tool, Tool-Use-Tax, RouteLLM 等）全部聚焦 capability matching，无一讨论 catastrophic failure 作为 routing signal——如果 death dominance 真的 obvious，为什么无人验证？\n- **R2 的回应**：承认问题定义有独立价值（Excitement 2.5→3.0），但维持 \"一个好问题配一个可预见的答案，对 Findings 够，对 main conference 不够\"。\n- **交叉后状态**：R1 Excitement 3.5→3.0，R2 2.5→3.0，**Excitement 收敛至 3.0/5**。分歧从 1.0 gap 缩小为 0，但 Overall 仍有 0.5 差距（R1: 3.5, R2: 3.0），因为 R1 认为 Soundness+Reproducibility 的高分足以补偿 Excitement。\n- **Director 裁决**: 维持 Critical。问题定义的贡献部分缓解了 triviality concern，但 EMNLP reviewer panel 中 excitement deficit 是常见 rejection reason。当前 non-triviality 论证（§5）力度不足。\n- **Action**: 三角度强化：(1) routing 文献 prior assumptions 与实证的反差；(2) intervention resistance 的 non-predictability；(3) cross-model δ stability 作为结构性发现。\n\n**MF3 [Critical, 强共识] Framing 内在张力——framework vs finding 定位不清。**\n- R2-W2 首提，R1 在交叉回应中完全同意（\"论文在 diagnostic framework 和 empirical finding 之间摇摆\"）。R1 补充了关键观察：\"如果选择 framework-centric 路线，novelty 质疑（R2-W1）就会被大幅缓解。\"\n- **Action**: 选择一个主线贯穿标题/Abstract/Contributions/Conclusion。推荐 framework-centric——既缓解 novelty concern，又对 single-environment scope 更 tolerant。\n\n**MF4 [Critical, 强共识] Cluster bootstrap K=11 低于公认阈值。**\n- R1-N2 首提（Critical），R2 在交叉回应中完全同意并补充了额外论据：(1) p=0.002 仅比最小可报告值 (1/2048 ≈ 0.0005) 大 4 倍；(2) `find-non-living-thing` (zero death) 作为 outlier 可能影响 effect size。\n- **缓解因素**（R2 同时指出）：多种互补 robustness evidence（8-seed, per-task CIs, exact permutation）共同构成比单一 cluster bootstrap 更强的证据链。两位 reviewer 均认为 \"critical-but-partially-mitigated\"。\n- **Action**: 正文以 non-clustered bootstrap 为主推断；cluster bootstrap 定位为 conservative sensitivity check；增加 K=11 vs K≥40 的显式讨论。\n\n**MF5 [Critical, 强共识] Episode→step label projection 噪声——router diagnostic 价值严重受损。**\n- R1-N3 首提（Critical），R2 在交叉回应中称其为 \"比论文的解释更有说服力的替代假说\"。\n- **核心分歧转变**: 论文解读 = \"step-level signal 本质上不存在\"；R1 替代假说 = \"signal 可能存在但被 ~88% noise/uninformative label 淹没\"。两位 reviewer 均倾向 R1 解释。\n- R2 进一步指出 R1-W2（pure-strategy 外部效度）和 R1-N3 形成 tension：如果 label noise 是 router 失败原因（N3），则 step-level routing 可能 feasible，那 pure-strategy 对比高估 death asymmetry（W2）就更严重。\n- **Action**: §3.6 明确区分两种解释；测试 death-proximal labeling baseline（如只用 death event 附近 steps 训练）；或明确声明 router failure 是 label sparsity 而非 fundamental non-learnability。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1 [Warning, 强共识] Cross-environment probes 定位过强。**\n- R1-W1 和 R2-W3 一致。MATH = unfalsifiable null result，ALFWorld = 不同机制。Abstract \"cross-domain probes\" 措辞需弱化为 \"boundary probes/consistency checks\"。\n\n**SF2 [Warning, 共识] 缺少 penalty magnitude 的实际实验验证。**\n- R2-W6 首提，R1 在交叉回应中完全同意。Appendix K 的 DAF vs P 是数学推导而非实验。R1 补充：Table 13 显示 P ≤ 25 时 correlation 不显著——\"death dominance 是 ScienceWorld 特定 penalty regime 下的现象\"。\n\n**SF3 [Warning, 共识] Pure-strategy 设计的外部效度。**\n- R1-W2 首提，R2 同意并补充了与 R1-N3 的 tension 关系。\n\n**SF4 [Warning, 强共识] Conclusion 过于简短（2 句话）。**\n\n**SF5 [Warning, 强共识] Safe RL Related Work 不够深入。**\n- 缺 CMDP (Altman 1999) 和 risk-sensitive RL 与 death avoidance 的理论映射。\n\n**SF6 [Warning, R2 首提, R1 部分 REBUT] Abstract 数字过密。**\n- R1 认为 \"每个数字都有明确指代，empirical 论文需要具体数字\"。R2 维持 concern。\n- **Director 裁决**: 如采用 framework-centric framing，Abstract 可自然减少数字密度（R1 观点）。列为 Should-Fix。\n\n**SF7 [Warning, 强共识] \"Modality\" 术语歧义。**\n\n**SF8 [Warning, R1 首提] Reflexion dose-response N=5 统计功效不足。**\n\n**SF9 [Warning, 交叉后新增共识] Routing 的 practical value 本身存疑。**\n- R1-Q4 首提，R2 在交叉回应中称之为 \"devastating observation\"。3.7% internal-preferred base rate + 96.3% oracle 选择 always-deterministic → always-deterministic 在实际部署中已接近最优。62% tie rate（R2-M1）进一步支持——大多数 episodes routing 选择无差异。\n- **Action**: §5 Discussion 直接面对这个 implication：不仅 \"routing signal 被 death avoidance 主导\"，更进一步 \"routing 在当前 setup 下几乎不必要\"——这本身是一个有价值的诊断性结论。\n\n### Minor\n\n**m1 [Info, 共识]** 62% tie rate 含义需在正文讨论。\n\n**m2 [Info, R1]** Figure 2 caption 报告 Spearman's ρ。\n\n**m3 [Info, 强共识]** `webb-2023` 年份需确认（2014 WP vs 2023 journal）。\n\n**m4 [Info, R1]** Appendix R 阈值选择缺理论依据。\n\n**m5 [Info, R2]** AI assistants disclosure 建议更具体。\n\n**m6 [Info, 共识]** Missing references: Altman (1999) CMDP, Mihatsch & Neuneier (2002), Natarajan et al. (2013) noisy label learning。\n\n**m7 [Info, R1]** Table 1 weighting scheme（episode-weighted vs task-weighted）需明确。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** [R1-Q1, R2-W6] DAF 公式假设 Δ_nd 不随 P 变化——是否在 P≠100 的 ScienceWorld 变体上做过实际验证？Appendix K 是数学推导还是实际实验？\n\n**Q2.** [R1-Q2, R2-Q4, 强共识] 105 internal deaths 全来自 `focus on [object]` 误用——death avoidance 是否等价于 single-action bug avoidance？Grounding ablation 降至 29%，residual gap ≥12pp。如果修复该 pattern，death dominance 是否消失？\n\n**Q3.** [R2-Q2, SF9] 62% tie rate + 3.7% internal-preferred base rate → routing 在大多数情况下无差异，always-deterministic 接近最优。论文如何看待这一 observation 对 routing 价值的影响？\n\n**Q4.** [R1-N3, 强共识] Router near-chance accuracy 是因为 death signal 本质上不是 step-level 的，还是因为 episode-level labels 投射到 steps 时 ~88% noise/uninformative rate？是否考虑过 death-proximal labeling（只用 death event 附近 steps 训练）？\n\n**Q5.** [R1-Q5] Llama cross-model replication 的完整 DAF 是多少？\"intact\" 太模糊，需要具体数字。\n\n**Q6.** [R2-Q3] SCI=0.2147 但 top-3 task types 占 39.8% total death-rate differential——death dominance 是 task-type specific 还是 environment-wide？\n\n---\n\n## Missing References\n\n- **Altman, E. (1999). Constrained Markov Decision Processes.** Death avoidance 作为 implicit constraint 的理论对应。[R2, R1 同意]\n- **Mihatsch & Neuneier (2002). Risk-sensitive RL.** 与 catastrophic failure avoidance 直接相关。[R2, R1 同意]\n- **Natarajan et al. (2013). Learning with Noisy Labels.** 为 ~88% uninformative label rate 下的 router near-chance accuracy 提供理论 grounding。[R1, R2 同意]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户选择不提交）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 超时（elapsed 727s）。无排版审查结果。\n\n**基于 PDF 阅读的基本格式确认**:\n- ✅ 正文 8 页（§1-§6 在 p1-p8），符合 ≤8 页要求\n- ✅ Limitations（p8-9），具体且坦诚\n- ✅ Ethics Statement（p9）\n- ✅ Double-blind: \"Anonymous ACL submission\"\n- ✅ ACL 模板 + [review] option\n- ✅ Figures/Tables 位置合理\n- ⚠️ webb-2023 年份需确认\n\n---\n\n## Reviewer Consensus（交叉回应后最终状态）\n\n### 完全收敛\n| 议题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| DAF headline framing (MF1) | Critical | Critical | ✅ 强共识 |\n| K=11 cluster bootstrap (MF4) | Critical | Agrees (critical-but-mitigated) | ✅ 共识 |\n| Episode→step noise (MF5) | Critical | Agrees (\"更有说服力\") | ✅ 强共识 |\n| Framing tension (MF3) | Agrees | Critical | ✅ 强共识 |\n| Cross-env overclaimed (SF1) | Should-Fix | Critical→Should-Fix | ✅ 共识 |\n| Routing practical value (SF9) | Q4 (\"devastating\") | Agrees | ✅ 强共识（交叉后新增） |\n| **Excitement** | **3.5→3.0** | **2.5→3.0** | **✅ 收敛至 3.0** |\n| Soundness | 3.5 | 3.5 | ✅ 一致 |\n| Reproducibility | 4.5 | 4 | ✅ 基本一致 |\n\n### 残余分歧\n| 议题 | R1 | R2 | 差异 |\n|------|----|----|------|\n| **Overall Score** | **3.5** (Borderline Conference) | **3.0** (Findings) | **0.5 gap** |\n| Abstract density (SF6) | REBUT | Should-Fix | 主观分歧 |\n\n**0.5 分残余差距根源**: R1 认为 Soundness 3.5 + Reproducibility 4.5 的高分足以在 Excitement 3.0 下支撑 Borderline Conference；R2 认为 Excitement 3.0 的 novelty ceiling 决定了 Findings 更合适。两者均为合理的 reviewer perspective。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0–3.5（Findings 至 Borderline Conference）**\n\n**维度汇总（交叉回应后最终值）**:\n| 维度 | R1 (调整后) | R2 (调整后) | 综合 |\n|------|------------|------------|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | **3.0/5** | **3.0/5** | **3.0/5** |\n| Reproducibility | 4.5/5 | 4/5 | **4.25/5** |\n| Clarity | — | 3/5 | **3/5** |\n\n**综合评估**:\n\n论文问了一个重要且被忽视的诊断性问题，给出了清晰的回答，counterfactual 设计干净，统计分析超过同类水准，robustness checks 全面，negative results 诚实呈现。\n\n核心问题：\n1. **DAF framing 误导**（MF1）——低成本修复\n2. **Novelty 受限但非 trivial**（MF2）——Excitement 收敛至 3.0，问题定义有价值但答案可预见性限制了 ceiling\n3. **Framing 不统一**（MF3）——需选择 framework-centric 或 finding-centric 主线\n4. **K=11 统计推断**（MF4）——通过 non-clustered bootstrap 为主推断来缓解\n5. **Router diagnostic 受 label noise 污染**（MF5）——需区分 label noise vs fundamental non-learnability\n6. **Routing 的 practical value 本身存疑**（SF9, 交叉后新增强共识）——3.7% internal-preferred + 62% ties → always-deterministic 几乎最优\n\n**Revision 路径**:\n- **提升至 Conference (3.5-4.0) 的条件**: (1) 选择 framework-centric framing（同时缓解 MF2 和 MF3）；(2) K=11 辩护充分（MF4，低难度）；(3) DAF framing 修正（MF1，低难度）；(4) death-proximal labeling baseline 或 clear attribution（MF5）；(5) §5 直面 routing practical value 问题（SF9）\n- **如果 MF2 (novelty) 和 SF9 (routing value) 无法有效回应，更可能落在 Findings (3.0)**\n\n---\n\n## Detailed Comments\n\n### Title & Abstract\n- 标题聚焦 finding 但 Contribution 1 是 framework——需统一（MF3）\n- Abstract 以 78.9% 为 primary，DAF 降为补充（MF1）\n- 如采用 framework-centric framing，数字密度可自然降低（SF6）\n\n### §1 Introduction\n- 问题定义清晰，逻辑链通畅\n- Contributions 列表需重组以匹配选定的 framing 主线\n\n### §2 Method\n- 写作最清晰的部分\n- Algorithm 1 设计合理\n- §2.4 Scope of episode-level analysis 段需更强调 episode→step gap implications\n- DAF 需更 upfront 承认是 derived quantity\n\n### §3 Experiments\n- §3.1 核心实证清晰，但段落结构需修正（78.9% 先于 DAF）\n- §3.2 Cross-model 缺 Llama DAF 具体数字\n- §3.3 Agent improvement 有价值；72B DAF=92.4% 说明 scaling 不消除 death dominance\n- §3.4 Cross-env 过于浅显，需重定位为 boundary probes\n- §3.5 Oracle degeneracy (96.3% always-det) 和 3.7% internal-preferred 需更突出讨论\n- §3.6 Router 应明确框架为 negative result；区分 label noise vs signal non-learnability\n\n### §4 Related Work\n- Tool Use / Adaptive Routing 覆盖充分\n- **Safe RL 需扩展**——补 CMDP, risk-sensitive RL 理论连接\n\n### §5 Discussion\n- \"Non-triviality\" 论证力度不足（MF2 核心）\n- \"Anatomy of catastrophic failure\"——105 deaths 全来自 `focus on`，implications 需更深讨论\n- **需新增**: routing practical value 的直接讨论（SF9）\n- **需新增**: pure-strategy vs mixed-strategy gap 估计（SF3）\n\n### §6 Conclusion\n- 严重不足——2 句话，需扩展至 ~0.5 页\n\n### Limitations\n- 覆盖面 adequate，但缺 \"P=100 specific\" 限制的明确讨论\n\n### 格式合规\n- ✅ 正文 8 页 | ✅ Limitations | ✅ Ethics | ✅ Double-blind | ✅ ACL template\n- ⚠️ webb-2023 年份 | ⚠️ modality 术语",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0-3.5 (Findings to Borderline Conference)",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 1747 · 2026-05-19T16:02:28.064700+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3959
}
```

</details>

---


### Assistant

_source line 1748 · 2026-05-19T16:02:35.992962+00:00_

审稿报告已更新并投递至 Research Director。

**Round 19 审稿完成**。核心结论：

- **Overall**: 3.0–3.5（Findings 至 Borderline Conference）
- **Excitement 收敛至 3.0/5**（R1 从 3.5 下调，R2 从 2.5 上调）
- **Soundness 3.5/5**（一致），**Reproducibility 4.25/5**（一致）
- 5 个 Must-Fix：DAF framing、novelty 论证、framework/finding 定位、K=11 统计、episode→step noise
- 4 个 Should-Fix + 交叉后新增 1 个（routing practical value 存疑）
- **关键 revision 路径**：采用 framework-centric framing 可同时缓解 novelty 和 single-env concern
- Issue tracker 已同步更新（`review_issues.yaml`，含 R19 新增 4 个 issue + 既有 issue 的 R19 mentions）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 146

## Round 146

74 recorded events


### User

_source line 1749 · 2026-05-19T16:30:04.766239+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1750 · 2026-05-19T16:30:11.598377+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1751 · 2026-05-19T16:30:11.649264+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1752 · 2026-05-19T16:30:17.244161+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1753 · 2026-05-19T16:30:17.294702+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1754 · 2026-05-19T16:30:20.058265+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1755 · 2026-05-19T16:30:20.109148+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1756 · 2026-05-19T16:30:24.779496+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1757 · 2026-05-19T16:30:24.930511+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1758 · 2026-05-19T16:30:32.772184+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1759 · 2026-05-19T16:30:32.772665+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1760 · 2026-05-19T16:30:37.343162+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1761 · 2026-05-19T16:30:39.706438+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (112 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- death-proximal-labeling-router: If router is trained only on death-proximal steps (k steps before fatal action), step-level balanced accuracy will improve over the full-dataset baseline (~54%), because death-proximal steps carry concentrated routing signal that is diluted by ~66% uninformative pre-event steps in the full dataset. If accuracy remains near-chance even with filtered data, the routing signal is fundamentally not step-level learnable.（已分配 westb-13313 GPU:cuda:0，等待提交）\n\n## 近期结论\n- **backbone-scaling-70b** (success): 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 ← 基于 backbone-scaling-death-rate-0.5b\n  [72B DAF Decomposition Analysis](/api/workspace-files/projects/simgate-modular-routing/artifacts/backbone-scaling-70b/report/72b_daf_decomposition.md)\n- **minihack-cross-env-pilot** (negative): In MiniHack permadeath navigation environments, episode-level counterfactual analysis will reveal death dominance (internal DR significantly > deterministic DR), validating the diagnostic framework's cross-environment applicability beyond ScienceWorld. This tests whether death avoidance as the dominant rou
…[truncated 1775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2363
}
```

</details>

---


### Tool call

_source line 1762 · 2026-05-19T16:30:39.706975+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 1763 · 2026-05-19T16:30:40.309911+00:00_

-rw-r--r-- 1 ubuntu ubuntu 574047 May 19 16:27 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu  51364 May 19 16:27 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1764 · 2026-05-19T16:30:40.310346+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1765 · 2026-05-19T16:30:45.730839+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission guidelines from the ACL website. Here's wh
…[truncated 1252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5420
}
```

</details>

---


### Tool call

_source line 1766 · 2026-05-19T16:30:49.863454+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission deadline guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission deadline guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1767 · 2026-05-19T16:30:50.064496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit anonymity policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit anonymity policy"
  }
}
```

</details>

---


### Tool result

_source line 1768 · 2026-05-19T16:30:57.349763+00:00_

Web search results for query: "EMNLP 2026 submission format page limit anonymity policy"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's the information about EMNLP 2026 submission format, page limits, and anonymity policy:

## Submission Format and Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 7285
}
```

</details>

---


### Tool result

_source line 1769 · 2026-05-19T16:30:57.500879+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission deadline guidelines"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here is information about the ACL Rolling Review (ARR) May 2026 submission deadline and guidelines:

## May 2026 ARR Submission Deadline

The submission deadline is always the 15th of the month; other dates vary due to the length of months, timing of weekends, etc. This means the May 2026 submission deadline would be May 15, 2026.

## Key Submission Guidelines

**Author Requirements:**
- Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities must be avoided.
- Papers should not 
…[truncated 1077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 7637
}
```

</details>

---


### Tool call

_source line 1770 · 2026-05-19T16:31:02.326313+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers"
  }
}
```

</details>

---


### Tool call

_source line 1771 · 2026-05-19T16:31:02.728558+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1772 · 2026-05-19T16:31:09.107474+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Leveraging Large Language Models for Improved Understanding of Communications With Patients With Cancer in a Call Center Setting: Proof-of-Concept Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11669882/"},{"title":"Natural language processing for humanitarian action: Opportunities, challenges, and the path toward humanitarian NLP","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10080095/"}]

Based on the search results, here's what I found about the Call for Main Conference Papers for EMNLP 2026:

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

In addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

Regarding the submission process, the ARR 2026 May cycle is aligned with both EMNLP and AACL, and authors must explicitly declare which conference they intend to commit to at submission time, with this choice being binding for EMNLP 2026. Papers that have received reviews and a meta-review from ARR may be committed to EMNLP via the commitment link.

You can find the full Call for Main Conference Pap
…[truncated 163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6781
}
```

</details>

---


### Tool result

_source line 1773 · 2026-05-19T16:31:09.107886+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6379
}
```

</details>

---


### Tool call

_source line 1774 · 2026-05-19T16:31:16.237150+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1775 · 2026-05-19T16:31:16.738853+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1776 · 2026-05-19T16:31:16.839530+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1777 · 2026-05-19T16:31:16.959563+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	\paragraph{Environmental scope.}
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72B remains future work. Our quantitative results (DAF $= 90.4\%$, label fraction
…[truncated 15048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 120
}
```

</details>

---


### Tool call

_source line 1778 · 2026-05-19T16:31:22.946118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1779 · 2026-05-19T16:31:23.849941+00:00_

200	\midrule
201	id-life-stages-1       & 0.963 \\
202	lifespan-long          & 0.969 \\
203	lifespan-l-then-s      & 0.976 \\
204	inclined-plane         & 0.969 \\
205	freeze                 & 0.971 \\
206	meas-melt-point        & 0.972 \\
207	id-life-stages-2       & 0.972 \\
208	find-animal            & 0.970 \\
209	grow-fruit             & 0.973 \\
210	chem-mix               & 0.969 \\
211	find-non-living-thing  & 0.980 \\
212	\bottomrule
213	\end{tabular}
214	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
215	\label{tab:loo}
216	\end{table}
217	
218	\section{Wild Cluster Bootstrap}
219	\label{app:wild-cluster}
220	
221	Episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).
222	
223	\begin{table}[h]
224	\centering
225	\small
226	\begin{tabular}{@{}lcc@{}}
227	\toprule
228	Method & $p$-value & 95\% CI \\
229	\midrule
230	Cluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\
231	Wild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\
232	Exact permutation ($2{,}048$ perms) & $0.002$ & --- \\
233	Sign test & $< 0.001$ & --- \\
234	\bottomrule
235	\end{tabular}
236	\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
237	\label{tab:wild-cluster}
238	\end{table}
239	
240	\noindent All methods confirm significance with $p < 0.01$, and th
…[truncated 19607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1780 · 2026-05-19T16:31:23.900725+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex 2>/dev/null",
  "description": "List all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex 2>/dev/null",
    "description": "List all tex files"
  }
}
```

</details>

---


### Tool result

_source line 1781 · 2026-05-19T16:31:23.951376+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1782 · 2026-05-19T16:31:28.170311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1783 · 2026-05-19T16:31:31.687263+00:00_

1	\begin{abstract}
2	Per-step oracle comparison degenerates under sparse rewards---in ScienceWorld, 97.4\% of steps yield identical scores regardless of computation mode. We introduce an episode-level counterfactual diagnostic framework that overcomes this degeneracy by decomposing routing signal into death-avoidance and non-death components via paired pure-strategy episodes. Applying this framework to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), we find that \textbf{78.9\% of non-tie routing labels} stem from death asymmetry---a penalty-independent result; a derived measure (DAF) reaches 90.4\% at $P{=}100$. Cross-model replication (Llama-3.1-8B, DAF${=}88.2\%$), four intervention axes (retry, self-correction, $10{\times}$ scaling, action-space restriction), and boundary probes against contrasting environments (MATH, ALFWorld) confirm the framework's diagnostic utility and the robustness of this finding. The framework diagnoses when catastrophic failure makes routing signal degenerate, enabling practitioners to assess routing value before investing in router training.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 3516
}
```

</details>

---


### Tool call

_source line 1784 · 2026-05-19T16:31:31.938348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1785 · 2026-05-19T16:31:31.938845+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \cite{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone---the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated)---while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \cite{toolformer-2023} inserts API calls by perplexity reduction; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. The shared assumption---that routing signal stems from diverse sources and a learned router can exploit it---has not been tested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under ScienceWorld's penalty ($P{=}100$), DAF reaches $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$). The internal strategy's hallucination-induced failures trigger catastrophic death
…[truncated 2048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1786 · 2026-05-19T16:31:32.089473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1787 · 2026-05-19T16:31:32.140460+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\cite{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which computation mode to use at each step; our analysis investigates what signal is available to learn $\rho$. A reasoning-depth ablation ($n{=}120$) found no significant difference ($p > 0.26$; Appendix~\ref{app:ablations}).
10	
11	\subsection{Counterfactual Episode Collection}
12	\label{sec:collection}
13	
14	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation mode. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-202
…[truncated 6804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1788 · 2026-05-19T16:31:38.521742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1789 · 2026-05-19T16:31:38.572795+00:00_

1	\section{Experiments}
2	
3	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}).
4	
5	\subsection{Death Avoidance Decomposition}
6	\label{sec:death-decomp}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=0.85\columnwidth]{figures/fig1_daf_scatter.pdf}
11	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$ (Spearman's $\rho = 0.975$; Appendix~\ref{app:per-task}), $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
12	\label{fig:decomposition}
13	\end{figure}
14	
15	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these 75, 54 are sole-signal labels (both strategies score zero without death, so death avoidance was the \emph{sole} discriminating signal). At $P{=}0$, the 54 sole-signal labels reduce to ties, leaving 41 non-tie labels of which 21 (51.2\%) still involve death asymmetry; the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}), but the practical routing value of death avoidance requires $P > 0$.
16	
17	Of 245 episodes, 150 (61.2\%) 
…[truncated 13185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1790 · 2026-05-19T16:31:38.673621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1791 · 2026-05-19T16:31:38.674102+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	\emph{Self-supervised} approaches learn tool invocation from loss signals: Toolformer \cite{toolformer-2023} inserts API calls filtered by perplexity reduction; ToolACE \cite{toolace-2025} curates synthetic data for function-calling accuracy.
6	\emph{Token-level} methods embed tools into the model vocabulary: ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens resolved at inference.
7	\emph{Task-level} decomposition routes subtasks to specialized modules: ART \cite{art-2023} generates tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask.
8	\emph{RL-based} methods learn routing policies from reward: ReTool \cite{retool-2025} discovers when code execution is preferable to chain-of-thought.
9	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
10	Concurrent work examines \emph{when} to invoke tools: \citet{tool-overuse-illusion-2026} find tool overuse correlates with model uncertainty; \citet{when2tool-2026} show tool-call decisions are encoded in hidden states; \citet{tool-use-tax-2026} quantify a ``tool-use tax''; \citet{to-call-or-not-2026} propose a necessity-utility-affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, 78.9\% of routing labels trace to catastrophic-failure prevention.
11	
12	\paragraph{Adaptive Computation and Routing.}
13	Adaptive routing traces back to learned halting policies \citep{graves2016act}. In the LLM era, CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cit
…[truncated 2351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1792 · 2026-05-19T16:31:39.485909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1793 · 2026-05-19T16:31:39.687154+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. The 4B router improves at episode level ($59.0\%$) without step-level gains ($56$--$59\%$), confirming task-type classification; cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}).
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), its practical implications were not predictable a priori. Existing routing work (Toolformer, CogRouter, ART, When2Tool, RouteLLM) implicitly assumes diverse signals; our finding that 78.9\% of labels trace to a single mechanism contradicts this assumption. Intervention resistance confirms non-triviality: all four axes fail to eliminate death dominance (72B DAF${}= 92.4\%$; Reflexion DAF${}>100\%$ with $\Delta_{\text{nd}} = -0.47$; action filtering leaves ${\geq}12$~pp residual gap; threshold routing with perfect death knowledge cannot outperform always-deterministic). Cross-model stability (Qwen $+26.5$~pp, Llama $+30.0$~pp, both ${\sim}42\%$ internal DR) suggests death vulnerability is a task-environment property, not model-specific. Precise quantification (78.9\%, not ``most'') enables principled deployment decisions; more aggressive interventions remain untested, so we characterize a ceiling, not a universal bound.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (Appendix~\ref{app:failure-modes}). The root cause is grounding failure: agents parse task descriptions correctly but cannot map understanding to
…[truncated 1617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1794 · 2026-05-19T16:31:39.687675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1795 · 2026-05-19T16:31:39.738238+00:00_

1	\section{Conclusion}
2	
3	We introduced an episode-level counterfactual diagnostic framework for decomposing routing signal in modular LLM agents, overcoming per-step oracle degeneracy (97.4\% tie rate) through paired pure-strategy comparison with penalty-independent (label fraction) and penalty-dependent (DAF) metrics. Applied to ScienceWorld, 78.9\% of non-tie routing labels stem from death asymmetry---robust across four intervention axes, cross-model replication (Llama-3.1-8B, DAF${=}88.2\%$), and boundary probes (MATH, ALFWorld). The diagnostic value is practical: our 200 GPU-hour router training could not outperform the always-deterministic baseline, an outcome a 50-episode pilot would have predicted.
4	
5	The framework applies to any environment with episode-level evaluation and binary catastrophic outcomes. Future work should target intermediate death regimes (NetHack combat tasks), explore death-proximal labeling for step-level signal extraction, and extend to mixed-strategy routing and stronger backbones.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1796 · 2026-05-19T16:31:48.649073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
    "pages": "1-5"
  }
}
```

</details>

---


### Tool result

_source line 1797 · 2026-05-19T16:31:50.657342+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf (560.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 2008
}
```

</details>

---


### Tool call

_source line 1798 · 2026-05-19T16:31:50.915949+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom PyPDF2 import PdfReader\nreader = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf')\nprint(f'Total pages: {len(reader.pages)}')\n\" 2>/dev/null || python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"Cannot determine page count\"",
  "description": "Get PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom PyPDF2 import PdfReader\nreader = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf')\nprint(f'Total pages: {len(reader.pages)}')\n\" 2>/dev/null || python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"Cannot determine page count\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1799 · 2026-05-19T16:31:51.167388+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Tue May 19 16:31:44 2026 UTC
ModDate:         Tue May 19 16:31:44 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           21
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       573849 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1800 · 2026-05-19T16:31:56.888964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
  "pages": "6-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
    "pages": "6-10"
  }
}
```

</details>

---


### Tool result

_source line 1801 · 2026-05-19T16:31:57.745181+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf (560.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1802 · 2026-05-19T16:31:57.757428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "499",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "offset": "499",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1803 · 2026-05-19T16:31:57.809407+00:00_

499	\label{app:cross-model}
500	
501	We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
502	The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
503	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is structurally determined. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
504	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
505	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
506	
507	\begin{table}[h]
508	\centering
509	\small
510	\begin{tabular}{@{}lrrrl@{}}
511	\toprule
512	Task & Int\% & Det\% & $\Delta$\,pp & D / I / N \\
513	\midrule
514	identify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\
515	freeze & 45 & 0 & +45 & 9 / 0 / 11 \\
516	grow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\
517	identify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\
518	measure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\
519	lifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\
520	lifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\
521	chemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\
522	inclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\
523	find-animal & 40 & 25 & +15 & 6 / 2 / 12 \\
524	find-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\
525	\midrule
526	\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
527	\bottomrule
528	\end{tabular}
529	\caption
…[truncated 13336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-19T16:32:21.074824+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_EXISTING_ISSUES\"",
  "description": "Check existing review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_EXISTING_ISSUES\"",
    "description": "Check existing review issues"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-19T16:32:21.527114+00:00_

## Round 19 Review Issues (revised after cross-response, 2026-05-19)

# =============================================
# Resolved issues from prior rounds
# =============================================

- id: "R13-N3"
  summary: "跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  resolution: "标题和 Contribution 措辞已恰当限定 scope"
  resolution_round: 15

- id: "R13-W1"
  summary: "正文篇幅严重不足 long paper 要求"
  category: format
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 14
  resolution: "正文已扩展至 8 页"
  resolution_round: 14

- id: "R13-W2"
  summary: "Router 训练实验存在多个 confound"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
  resolution_round: 15

- id: "R13-W3"
  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
  category: method
  severity: info
  status: resolved
  first_raised_round: 13
  last_seen_round: 14
  resolution: "Limitations 和 Appendix B 已充分量化"
  resolution_round: 14

- id: "R13-W4"
  summary: "SCI 方法贡献与实际使用不成比例"
  category: method
  severity: info
  status: resolved
  first_raised_round: 13
  last_seen_round: 14
  resolution: "SCI 已降级到 Appendix A"
  resolution_round: 14

- id: "R13-W7"
  summary: "Router negative results 解释不完整"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  resolution: "Router 实验定位为 diagnostic probe"
  resolution_round: 15

- id: "R13-m2"
  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 16
  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
  resolution_round: 16

- id: "R13-m3"
  summary: "Reference 格式不统一 + orphan entries"
  category: format
  severity: info
  status: resolved
  first_ra
…[truncated 19230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1806 · 2026-05-19T16:32:21.928765+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1807 · 2026-05-19T16:32:21.979421+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1808 · 2026-05-19T16:32:29.254958+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | head -120",
  "description": "Read full project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | head -120",
    "description": "Read full project config"
  }
}
```

</details>

---


### Tool result

_source line 1809 · 2026-05-19T16:32:29.308207+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 1810 · 2026-05-19T16:32:33.224211+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 1811 · 2026-05-19T16:32:33.276304+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1812 · 2026-05-19T16:32:38.618379+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -name \"config*\" -type f 2>/dev/null | head -10",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -name \"config*\" -type f 2>/dev/null | head -10",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 1813 · 2026-05-19T16:32:38.720314+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1814 · 2026-05-19T16:32:41.723260+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 3 -name \"config*\" -type f 2>/dev/null | head -10",
  "description": "Find config files broadly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 3 -name \"config*\" -type f 2>/dev/null | head -10",
    "description": "Find config files broadly"
  }
}
```

</details>

---


### Tool result

_source line 1815 · 2026-05-19T16:32:41.776728+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 1816 · 2026-05-19T16:32:44.636823+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/",
    "description": "List project directory"
  }
}
```

</details>

---


### Tool result

_source line 1817 · 2026-05-19T16:32:44.788030+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
artifacts
checkpoints
crafter_pilot
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
results
scripts
src
study_status.lock
task_context
tmp_unify_script.py
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1818 · 2026-05-19T16:33:26.468178+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "simgate-modular-routing",
  "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "simgate-modular-routing",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
  }
}
```

</details>

---


### Tool result

_source line 1819 · 2026-05-19T16:33:46.804917+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20336
}
```

</details>

---


### Tool call

_source line 1820 · 2026-05-19T16:33:47.056244+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**审查侧重：方法严谨性 + 实验设计**\n\n### Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 ≤ 8 页（Long Paper），参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL 双栏格式\n- **匿名规则**：Double-blind（无作者信息，自引匿名）\n- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit）\n\n### 论文信息\n- **标题**：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**：projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n### 你的审查重点\n\n1. **DAF 定义与数学性质**：DAF = δP/(δP + Δ_nd) 随 P 单调递增——这是否构成 tautology？78.9% label fraction 作为 penalty-independent metric 是否足够独立？两个 metric 的关系和各自的 contribution 是否清晰？\n\n2. **统计推断**：\n   - Cluster bootstrap K=11 clusters vs K≥40 recommended threshold\n   - Per-task n=20 episodes 的 statistical power\n   - Cohen's d=3.02 在 K=11 下的解读\n   - 非聚类 bootstrap 作为 primary inference 是否合理\n\n3. **实验设计**：\n   - 11/30 task types 的选择标准——anti-cherry-picking analysis 是否充分？\n   - Episode-level labels → step-level router training 的 granularity gap\n   - Router negative result 的实验控制（0.6B-4B scaling, augmentation, cross-split）\n   - Agent improvement baselines 的 statistical power（Reflexion dose-response N=200）\n\n4. **Cross-model / cross-environment 方法论**：\n   - Llama-3.1-8B replication: 同一参数规模是否构成 meaningful cross-model validation?\n   - MATH/ALFWorld 的 \"deterministic\" 含义与 ScienceWorld 不同——boundary probe vs validation\n\n5. **格式合规**：正文页数、Limitations 完整性、匿名性、引用格式\n\n请按照 EMNLP 2026 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses（Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**审查侧重：方法严谨性 + 实验设计**\n\n### Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 ≤ 8 页（Long Paper），参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL 双栏格式\n- **匿名规则**：Double-blind（无作者信息，自引匿名）\n- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit）\n\n### 论文信息\n- **标题**：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**：projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n### 你的审查重点\n\n1. **DAF 定义与数学性质**：DAF = δP/(δP + Δ_nd) 随 P 单调递增——这是否构成 tautology？78.9% label fraction 作为 penalty-independent metric 是否足够独立？两个 metric 的关系和各自的 contribution 是否清晰？\n\n2. **统计推断**：\n   - Cluster bootstrap K=11 clusters vs K≥40 recommended threshold\n   - Per-task n=20 episodes 的 statistical power\n   - Cohen's d=3.02 在 K=11 下的解读\n   - 非聚类 bootstrap 作为 primary inference 是否合理\n\n3. **实验设计**：\n   - 11/30 task types 的选择标准——anti-cherry-picking analysis 是否充分？\n   - Episode-level labels → step-level router training 的 granularity gap\n   - Router negative result 的实验控制（0.6B-4B scaling, augmentation, cross-split）\n   - Agent improvement baselines 的 statistical power（Reflexion dose-response N=200）\n\n4. **Cross-model / cross-environment 方法论**：\n   - Llama-3.1-8B replication: 同一参数规模是否构成 meaningful cross-model validation?\n   - MATH/ALFWorld 的 \"deterministic\" 含义与 ScienceWorld 不同——boundary probe vs validation\n\n5. **格式合规**：正文页数、Limitations 完整性、匿名性、引用格式\n\n请按照 EMNLP 2026 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses（Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool call

_source line 1821 · 2026-05-19T16:34:06.910133+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**审查侧重：新颖性 + 完整性 + 相关工作**\n\n### Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 ≤ 8 页（Long Paper），参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL 双栏格式\n- **匿名规则**：Double-blind（无作者信息，自引匿名）\n- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit）\n\n### 论文信息\n- **标题**：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**：projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n### 你的审查重点\n\n1. **Novelty 与 Contribution 定位**：\n   - 核心发现（78.9% labels from death asymmetry）是否\"显然\"或 trivial？惩罚结构 P=100 使得 death dominance 可预见——论文是否充分论证了为什么这个 finding 非 trivial？\n   - Contribution 结构：框架方法论 vs 实证发现 vs cross-validation——哪个是真正的 contribution？论文定位是否清晰一致？\n   - \"Diagnostic framework\" 的方法论贡献有多大？Episode-level counterfactual comparison 是否足够新颖？\n\n2. **Framing 一致性**：\n   - 标题声明 \"Dominant Routing Signal\" 但 96.3% oracle decisions favor always-deterministic + 62% ties——routing 本身的 practical value 是什么？\n   - \"penalty-independent\" 的表述是否准确？P=0 时 54/75 death-asymmetry labels 变成 ties\n   - Framework vs finding 的内在张力：论文是在推销框架还是推销发现？\n\n3. **相关工作覆盖**：\n   - Tool use & routing 文献：Toolformer, ART, Chameleon, CogRouter, ARES, RouteLLM, When2Tool 等——覆盖是否完整？\n   - Safe RL 文献：CMDP, risk-sensitive RL, constrained optimization——是否充分？\n   - LLM agent failure modes 文献：是否遗漏重要工作？\n   - Counterfactual evaluation 在 RL 中的前期工作\n   - 引用是否真实、格式是否正确？\n\n4. **论文完整性**：\n   - Abstract 信息密度是否合理（数字堆砌 vs 概念传达）？\n   - Introduction 的 gap statement 和 contribution list 是否匹配正文？\n   - Discussion 是否充分讨论了 implications 和 limitations？\n   - Conclusion 是否过于简短？\n\n5. **Cross-environment 分析的说服力**：\n   - MATH (no death) 和 ALFWorld (information asymmetry) 作为 boundary probes 的逻辑——是否说明了框架的适用范围？\n   - 缺少第二个 permadeath 环境的 replication（NetHack 只是 future work）\n\n请按照 EMNLP 2026 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses（Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**审查侧重：新颖性 + 完整性 + 相关工作**\n\n### Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 ≤ 8 页（Long Paper），参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL 双栏格式\n- **匿名规则**：Double-blind（无作者信息，自引匿名）\n- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit）\n\n### 论文信息\n- **标题**：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**：projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n### 你的审查重点\n\n1. **Novelty 与 Contribution 定位**：\n   - 核心发现（78.9% labels from death asymmetry）是否\"显然\"或 trivial？惩罚结构 P=100 使得 death dominance 可预见——论文是否充分论证了为什么这个 finding 非 trivial？\n   - Contribution 结构：框架方法论 vs 实证发现 vs cross-validation——哪个是真正的 contribution？论文定位是否清晰一致？\n   - \"Diagnostic framework\" 的方法论贡献有多大？Episode-level counterfactual comparison 是否足够新颖？\n\n2. **Framing 一致性**：\n   - 标题声明 \"Dominant Routing Signal\" 但 96.3% oracle decisions favor always-deterministic + 62% ties——routing 本身的 practical value 是什么？\n   - \"penalty-independent\" 的表述是否准确？P=0 时 54/75 death-asymmetry labels 变成 ties\n   - Framework vs finding 的内在张力：论文是在推销框架还是推销发现？\n\n3. **相关工作覆盖**：\n   - Tool use & routing 文献：Toolformer, ART, Chameleon, CogRouter, ARES, RouteLLM, When2Tool 等——覆盖是否完整？\n   - Safe RL 文献：CMDP, risk-sensitive RL, constrained optimization——是否充分？\n   - LLM agent failure modes 文献：是否遗漏重要工作？\n   - Counterfactual evaluation 在 RL 中的前期工作\n   - 引用是否真实、格式是否正确？\n\n4. **论文完整性**：\n   - Abstract 信息密度是否合理（数字堆砌 vs 概念传达）？\n   - Introduction 的 gap statement 和 contribution list 是否匹配正文？\n   - Discussion 是否充分讨论了 implications 和 limitations？\n   - Conclusion 是否过于简短？\n\n5. **Cross-environment 分析的说服力**：\n   - MATH (no death) 和 ALFWorld (information asymmetry) 作为 boundary probes 的逻辑——是否说明了框架的适用范围？\n   - 缺少第二个 permadeath 环境的 replication（NetHack 只是 future work）\n\n请按照 EMNLP 2026 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses（Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Assistant

_source line 1822 · 2026-05-19T16:50:05.098841+00:00_

已完成初始化。论文状态：

- **投稿目标**：EMNLP 2026 via ARR（May 2026 cycle）
- **论文状态**：main.tex + PDF 存在，21 页（正文 8 页 + Limitations/Ethics + References + 18 个 Appendix A-R）
- **格式检查**：ACL 双栏模板 `\usepackage[review]{acl}`，匿名 `\author{Anonymous}`，正文 8 页符合限制，Limitations section 存在
- **Venue 要求**：正文 ≤8 页，双盲审稿，无匿名期要求，Limitations 必须有，ARR 统一评分 1-5

**Reviewer 编排决定**：EMNLP 2026 一般会议长文，安排 2 名 Reviewer：
- **Reviewer 1**：方法严谨性 + 实验设计（DAF 定义合理性、统计推断、实验控制、router 实验）
- **Reviewer 2**：新颖性 + 完整性 + 相关工作（贡献定位、framing、cross-environment 分析、引用覆盖）

开始派发审稿任务和视觉审查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 147

## Round 147

56 recorded events


### User

_source line 1823 · 2026-05-21T01:16:34.866689+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- 补充材料: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/rebuttal_drafts.md

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1824 · 2026-05-21T01:16:40.749686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1825 · 2026-05-21T01:16:40.800976+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-21T01:16:49.334625+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1827 · 2026-05-21T01:16:49.385367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1828 · 2026-05-21T01:16:55.961887+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1829 · 2026-05-21T01:16:56.012580+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1830 · 2026-05-21T01:16:59.929053+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1831 · 2026-05-21T01:17:01.840543+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1911
}
```

</details>

---


### Tool call

_source line 1832 · 2026-05-21T01:17:01.841064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1833 · 2026-05-21T01:17:02.302460+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	\paragraph{Environmental scope.}
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72
…[truncated 57580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 461
}
```

</details>

---


### Tool call

_source line 1834 · 2026-05-21T01:17:03.256922+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1835 · 2026-05-21T01:17:03.459014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1836 · 2026-05-21T01:17:03.560424+00:00_

1	## Round 19 Review Issues (revised after cross-response, 2026-05-19)
2	
3	# =============================================
4	# Resolved issues from prior rounds
5	# =============================================
6	
7	- id: "R13-N3"
8	  summary: "跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication"
9	  category: experiment
10	  severity: critical
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 15
14	  resolution: "标题和 Contribution 措辞已恰当限定 scope"
15	  resolution_round: 15
16	
17	- id: "R13-W1"
18	  summary: "正文篇幅严重不足 long paper 要求"
19	  category: format
20	  severity: warning
21	  status: resolved
22	  first_raised_round: 13
23	  last_seen_round: 14
24	  resolution: "正文已扩展至 8 页"
25	  resolution_round: 14
26	
27	- id: "R13-W2"
28	  summary: "Router 训练实验存在多个 confound"
29	  category: experiment
30	  severity: warning
31	  status: resolved
32	  first_raised_round: 13
33	  last_seen_round: 15
34	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
35	  resolution_round: 15
36	
37	- id: "R13-W3"
38	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
39	  category: method
40	  severity: info
41	  status: resolved
42	  first_raised_round: 13
43	  last_seen_round: 14
44	  resolution: "Limitations 和 Appendix B 已充分量化"
45	  resolution_round: 14
46	
47	- id: "R13-W4"
48	  summary: "SCI 方法贡献与实际使用不成比例"
49	  category: method
50	  severity: info
51	  status: resolved
52	  first_raised_round: 13
53	  last_seen_round: 14
54	  resolution: "SCI 已降级到 Appendix A"
55	  resolution_round: 14
56	
57	- id: "R13-W7"
58	  summary: "Router negative results 解释不完整"
59	  category: experiment
60	  severity: warning
61	  status: resolved
62	  first_raised_round: 13
63	  last_seen_round: 15
64	  resolution: "Router 实验定位为 diagnostic probe"
65	  resolution_round: 15
66	
67	- id: "R13-m2"
68	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
69	  category: writing
70	  severity: warning
71	  status: resolved
72	  first_raised_round: 13
73	  last_seen_
…[truncated 22214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1837 · 2026-05-21T01:17:09.081007+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission processes, though the results primarily sh
…[truncated 1265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5824
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-21T01:17:35.061651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1839 · 2026-05-21T01:17:35.464512+00:00_

1	\begin{abstract}
2	Per-step oracle comparison degenerates under sparse rewards---in ScienceWorld, 97.4\% of steps yield identical scores regardless of computation mode. We introduce an episode-level counterfactual diagnostic framework that overcomes this degeneracy by decomposing routing signal into death-avoidance and non-death components via paired pure-strategy episodes. Applying this framework to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), we find that \textbf{78.9\% of non-tie routing labels} stem from death asymmetry---a penalty-independent result; a derived measure, the Death Avoidance Factor (DAF), reaches 90.4\% at $P{=}100$. Cross-model replication (Llama-3.1-8B, DAF${=}88.2\%$), four intervention axes (retry, self-correction, $10{\times}$ scaling, action-space restriction), and boundary probes against contrasting environments (MATH, ALFWorld) confirm the framework's diagnostic utility and the robustness of this finding. A three-stage diagnostic pilot (${\sim}$50 episodes) correctly predicts routing outcomes across all four tested conditions, demonstrating practical utility before any router is trained.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1840 · 2026-05-21T01:17:35.515141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1841 · 2026-05-21T01:17:35.966800+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \cite{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone---the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated)---while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \cite{toolformer-2023} inserts API calls by perplexity reduction; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026}, model tiers \cite{mtrouter-2026}, or episode-level model selection under sparse rewards \cite{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. The shared assumption---that routing signal stems from diverse sources and a learned router can exploit it---has not been tested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under ScienceWorld's penalty ($P{=}100$), DAF reaches $90.4\%$ (95\% CI: $[81.1\%, 99.0\%
…[truncated 2414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1842 · 2026-05-21T01:17:35.967297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1843 · 2026-05-21T01:17:36.470346+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\cite{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which computation mode to use at each step; our analysis investigates what signal is available to learn $\rho$.
10	
11	\subsection{Counterfactual Episode Collection}
12	\label{sec:collection}
13	
14	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation mode. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of computation mode (5{,}726 of 5{,}878 steps 
…[truncated 6689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1844 · 2026-05-21T01:17:36.470861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1845 · 2026-05-21T01:17:36.922732+00:00_

1	\section{Experiments}
2	
3	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}).
4	
5	\subsection{Death Avoidance Decomposition}
6	\label{sec:death-decomp}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=0.85\columnwidth]{figures/fig1_daf_scatter.pdf}
11	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$ (Spearman's $\rho = 0.986$; Appendix~\ref{app:per-task}), $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
12	\label{fig:decomposition}
13	\end{figure}
14	
15	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these 75, 54 are sole-signal labels (both strategies score zero without death, so death avoidance was the \emph{sole} discriminating sig
…[truncated 14653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1846 · 2026-05-21T01:17:36.923166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1847 · 2026-05-21T01:17:37.878270+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	\emph{Self-supervised} approaches learn tool invocation from loss signals: Toolformer \cite{toolformer-2023} inserts API calls filtered by perplexity reduction; ToolACE \cite{toolace-2025} curates synthetic data for function-calling accuracy.
6	\emph{Token-level} methods embed tools into the model vocabulary: ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens resolved at inference.
7	\emph{Task-level} decomposition routes subtasks to specialized modules: ART \cite{art-2023} generates tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask.
8	\emph{RL-based} methods learn routing policies from reward: ReTool \cite{retool-2025} discovers when code execution is preferable to chain-of-thought.
9	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
10	Concurrent work examines \emph{when} to invoke tools: tool-call decisions correlate with uncertainty~\citep{tool-overuse-illusion-2026}, are encoded in hidden states~\citep{when2tool-2026}, impose a ``tool-use tax''~\citep{tool-use-tax-2026}, or follow necessity-utility-affordability logic~\citep{to-call-or-not-2026}. Our decomposition provides environment-grounded evidence: 78.9\% of routing labels trace to catastrophic-failure prevention.
11	
12	\paragraph{Adaptive Computation and Routing.}
13	Adaptive routing traces back to learned halting policies \citep{graves2016act}. In the LLM era, CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing.
14	Rou
…[truncated 2321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1848 · 2026-05-21T01:17:37.929005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1849 · 2026-05-21T01:17:38.332101+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. The 4B router improves at episode level ($59.0\%$) without step-level gains ($56$--$59\%$), confirming task-type classification; cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}).
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), three specific consequences were not predictable a priori: (i)~$10{\times}$ scaling to 72B fails to eliminate it (DAF${}= 92.4\%$); (ii)~Reflexion self-correction yields DAF${}>100\%$, meaning death avoidance \emph{more} than accounts for the full gap; (iii)~a 0.5B model shows \emph{reduced} death rate ($13.3\%$; $n{=}15$) because it is too weak to reach dangerous states, revealing an inverted-U capability--vulnerability relationship. All four intervention axes leave ${\geq}12$~pp residual gaps to deterministic safety (Appendix~\ref{sec:threshold-routing}); cross-model stability ($36$--$43\%$ internal DR across three families) confirms death vulnerability is a task-environment property. Our primary models differ in pretraining data, tokenizer, alignment, and attention mechanism (Gemma-2: sliding window vs.\ full attention in Qwen/Llama), providing diversity beyond parameter count; 72B scaling confirms persistence beyond this range. More aggressive interventions remain untested, so we characterize a ceiling, not a universal bound.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (Appendix~\ref{app:failure-mode
…[truncated 1839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1850 · 2026-05-21T01:17:38.332569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1851 · 2026-05-21T01:17:39.286673+00:00_

1	\section{Conclusion}
2	
3	We introduced an episode-level counterfactual framework for decomposing routing signal in modular LLM agents, overcoming per-step oracle degeneracy (97.4\% tie rate). In ScienceWorld, 78.9\% of non-tie labels stem from death asymmetry---robust across intervention axes, cross-model replication (DAF${=}88.2\%$), and boundary probes (MATH, ALFWorld); a 50-episode pilot predicted all four conditions. Future work targets intermediate death regimes (NetHack), label-noise disentanglement, and mixed-strategy extension.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1852 · 2026-05-21T01:17:39.287061+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines page limit format template ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines page limit format template ARR"
  }
}
```

</details>

---


### Tool call

_source line 1853 · 2026-05-21T01:17:39.638628+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1854 · 2026-05-21T01:17:44.170949+00:00_

Web search results for query: "EMNLP 2026 submission guidelines page limit format template ARR"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026:

## Page Limits and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Template and Style Files

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Mandatory Sections

The mandatory Limitations section is required, placed after the conclusion.

## ARR Submission

All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026.

For more comprehensive submission guidelines, you can visit the EMNLP 2026 website directly or the ACL Rollin
…[truncated 152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 4883
}
```

</details>

---


### Tool result

_source line 1855 · 2026-05-21T01:17:44.221669+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4583
}
```

</details>

---


### Tool call

_source line 1856 · 2026-05-21T01:17:51.659210+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission guidelines for ARR 2026: page limits for long/short papers, formatting requirements, anonymity rules, appendix rules, template requirements, citation format, mandatory sections, and any specific restrictions. Also find the submission deadline for the May/June 2026 cycle."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the complete submission guidelines for ARR 2026: page limits for long/short papers, formatting requirements, anonymity rules, appendix rules, template requirements, citation format, mandatory sections, and any specific restrictions. Also find the submission deadline for the May/June 2026 cycle."
  }
}
```

</details>

---


### Tool call

_source line 1857 · 2026-05-21T01:17:53.166176+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/industry_track/",
  "prompt": "Extract EMNLP 2026 main conference submission guidelines, page limits, format requirements, anonymity rules, commitment deadline, and any specific restrictions for the main track (not industry track)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/industry_track/",
    "prompt": "Extract EMNLP 2026 main conference submission guidelines, page limits, format requirements, anonymity rules, commitment deadline, and any specific restrictions for the main track (not industry track)."
  }
}
```

</details>

---


### Tool call

_source line 1858 · 2026-05-21T01:17:54.823831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1859 · 2026-05-21T01:17:54.924774+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_director_19d7e797.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1860 · 2026-05-21T01:17:57.485800+00:00_

# EMNLP 2026 Main Conference Submission Guidelines

I cannot provide the requested information about the main conference track submissions. The webpage content you provided contains **only** details about the **Industry Track**, not the main research track.

The document explicitly states: "Please note that the EMNLP 2026 Industry Track does not use ARR!" and references a separate call for papers at `/calls/main_conference_papers/`, but that page's content is not included in the material provided.

To obtain main conference submission guidelines (page limits, format requirements, anonymity rules, and deadlines), you would need to:

1. Visit the main conference call for papers directly at the EMNLP 2026 website
2. Access the link referenced in the navigation: [Main Conference Papers](/calls/main_conference_papers/)

The current document covers Industry Track specifications only, which differ from standard research track requirements (e.g., Industry Track papers are maximum 6 pages, with different evaluation criteria focused on real-world deployment).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "elapsed_ms": 4319
}
```

</details>

---


### Tool result

_source line 1861 · 2026-05-21T01:17:57.889210+00:00_

# ARR 2026 Submission Guidelines Summary

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations (required) and ethical considerations sections
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations (required) and ethical considerations sections
- Unlimited reference pages

Papers exceeding length requirements or lacking a limitations section face desk rejection.

## Formatting Requirements

Submissions must follow the "official ACL style template" available on GitHub and adhere to ACL formatting guidelines regarding paper size, margins, and font sizes. Non-conforming submissions are rejected without review. Appendices must use double-column format (with limited exceptions).

## Anonymity Rules

Papers must exclude author names, affiliations, and self-identifying citations. Instead of "We previously showed," use "Smith previously showed." All supplementary materials, including repository links, require anonymization. Anonymized Git repositories or equivalent anonymous hosting are acceptable; Dropbox and similar download-tracking services are prohibited.

## Appendix Rules

Appendices follow the main text but precede references and don't count toward page limits. Reviewers aren't obligated to review appendices, so critical technical content should remain in the main paper. Key materials like novel methods or related work discussions must appear in main sections.

## Template & Citation Format

Use the official ACL template. For concurrent submissions on related topics, cite as: `Anonymous (2026). Paper title. Under review.`

## Mandatory Sections

A "Limitations" section discussing work constraints is required and doesn't count toward page limits.

## Submission Deadline

The page does not specify the May/June 2026 cycle deadline. Historical context mentions May 19, 2025, as an example deadline, but specific 2026 dates aren't provided in this content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "elapsed_ms": 6229
}
```

</details>

---


### Tool call

_source line 1862 · 2026-05-21T01:18:13.577871+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract complete submission guidelines for EMNLP 2026 main conference: page limits, formatting, anonymity rules, appendix rules, ARR submission deadlines, commitment deadline, template requirements, and any special restrictions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract complete submission guidelines for EMNLP 2026 main conference: page limits, formatting, anonymity rules, appendix rules, ARR submission deadlines, commitment deadline, template requirements, and any special restrictions."
  }
}
```

</details>

---


### Tool call

_source line 1863 · 2026-05-21T01:18:13.779150+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1864 · 2026-05-21T01:18:13.829831+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1865 · 2026-05-21T01:18:18.851374+00:00_

# EMNLP 2026 Main Conference Submission Guidelines

## Page Limits
- **Long papers:** 8 pages of content
- **Short papers:** 4 pages of content
- **Camera-ready versions:** Up to 9 pages for long papers; up to 5 pages for short papers (one additional page to address reviewer feedback)

## Formatting & Templates
All submissions must follow "ARR submission requirements" including paper templates available through the ARR CFP. Specific formatting details are referenced but detailed specifications are maintained on the ARR website rather than this page.

## Anonymity Rules
"The reviewing process will continue to be double-blind." Reviewers cannot access author information, and authors cannot identify reviewers. However, "authors will be given the option through ARR to make their anonymized submitted articles publicly visible." Additionally, "there is no anonymity period requirement" per ACL and ARR policies.

## Supplementary Materials
"Optional supplementary materials, appendices, software and data" are permitted according to ARR guidelines.

## Key Deadlines
- **ARR submission:** May 25, 2026
- **Reviewer registration (mandatory):** May 27, 2026
- **EMNLP commitment:** August 2, 2026
- **Camera-ready due:** September 20, 2026

All deadlines are 11:59 PM UTC-12:00 (anywhere on Earth).

## Special Restriction
"Dual submissions are not allowed." Authors must select their intended conference at ARR submission time, and "this choice will be binding for EMNLP 2026."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "elapsed_ms": 5273
}
```

</details>

---


### Tool call

_source line 1866 · 2026-05-21T01:18:29.605697+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1867 · 2026-05-21T01:18:29.706684+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml
/home/ubu
…[truncated 96 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1868 · 2026-05-21T01:18:33.838060+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1869 · 2026-05-21T01:18:33.888676+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1870 · 2026-05-21T01:18:36.600184+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1871 · 2026-05-21T01:18:36.855062+00:00_

&lt;persisted-output>
Output too large (63.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing--claude-sessions-review-director-19d7e797/fce885a3-3e89-4d6d-b91e-ebfcfba76d4c/tool-results/toolu_011EdiJsUAXgNrEaigokFKq8.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_14.md:150:外部审稿：未请求（项目未启用 paperreview.ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_9.md:156:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_8.md:102:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_16.md:170:未配置外部审稿（`external_review.paperreview_ai.enabled` 未启用）。无外部审稿结果。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_17.md:133:外部审稿：未配置（项目 config 中无 `external_review.paperreview_ai.enabled` 设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_12.md:139:外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_4.md:143:项目未配置外部审稿（paperreview.ai），本轮无外部审稿结果。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_10.md:178:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agent
…[truncated 143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 254
}
```

</details>

---


### Tool call

_source line 1872 · 2026-05-21T01:19:10.077865+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "simgate-modular-routing",
  "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "simgate-modular-routing",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
  }
}
```

</details>

---


### Tool result

_source line 1873 · 2026-05-21T01:19:29.925586+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19847
}
```

</details>

---


### Tool call

_source line 1874 · 2026-05-21T01:19:30.127355+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "simgate-modular-routing",
  "reviewer_id": "1",
  "round_number": "20",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n**论文信息**\n- 标题：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n- 补充材料：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/rebuttal_drafts.md\n\n**Venue 要求**\n- EMNLP 2026 (ARR Long Paper)\n- Deadline：2026-05-25\n- 正文 8 页限制，参考文献不限\n- ACL 模板，double-blind 匿名审稿\n- 必须包含 Limitations section（不计入页数）\n- 附录不计入页数\n\n**你的审查侧重**\n\n1. **统计推断可靠性**：\n   - Cluster bootstrap K=11 的推断力是否足够？non-clustered bootstrap 是否为合适的主推断方式？\n   - 各统计检验（wild cluster bootstrap, permutation test, sign test）的假设是否成立？\n   - DAF 的 95% CI 是否正确计算和解释？\n   - Per-task n=20 的统计功效\n\n2. **实验设计**：\n   - 11/30 task types 的选择是否引入 selection bias？anti-cherry-picking analysis 是否充分？\n   - Episode-level labeling 的合理性——episode labels 投射到 step level 的 mislabeling 问题\n   - Pure-strategy 设计是否高估 death asymmetry 对 realistic routing 的影响？\n   - 跨模型/跨环境验证的覆盖度和说服力\n\n3. **Router 实验**：\n   - Router negative result 的两种解释（label noise vs fundamental non-learnability）是否公正？\n   - Data scaling ablation 使用 paraphrase augmentation 的局限性\n   - 4B episode-level improvement (59.0%) 的实际意义\n   - Router 实验作为 \"diagnostic probe\" 的定位是否合理？\n\n4. **Agent improvement 实验**：\n   - Reflexion/Retry/72B 的实验设计和统计功效\n   - Dose-response 分析的 plateau 结论是否有足够证据支撑？\n   - Grounding ablation (48%→29%) 的设计和解释\n\n5. **DAF 度量本身**：\n   - DAF 随 P 单调递增是代数后果——论文是否充分承认这一点？\n   - 78.9% label fraction vs DAF 的关系是否清晰？\n   - P-invariance by design 的声明是否准确？\n\n请按 ARR 标准出具完整审稿意见：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR), Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "simgate-modular-routing",
    "reviewer_id": "1",
    "round_number": "20",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n**论文信息**\n- 标题：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n- 补充材料：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/rebuttal_drafts.md\n\n**Venue 要求**\n- EMNLP 2026 (ARR Long Paper)\n- Deadline：2026-05-25\n- 正文 8 页限制，参考文献不限\n- ACL 模板，double-blind 匿名审稿\n- 必须包含 Limitations section（不计入页数）\n- 附录不计入页数\n\n**你的审查侧重**\n\n1. **统计推断可靠性**：\n   - Cluster bootstrap K=11 的推断力是否足够？non-clustered bootstrap 是否为合适的主推断方式？\n   - 各统计检验（wild cluster bootstrap, permutation test, sign test）的假设是否成立？\n   - DAF 的 95% CI 是否正确计算和解释？\n   - Per-task n=20 的统计功效\n\n2. **实验设计**：\n   - 11/30 task types 的选择是否引入 selection bias？anti-cherry-picking analysis 是否充分？\n   - Episode-level labeling 的合理性——episode labels 投射到 step level 的 mislabeling 问题\n   - Pure-strategy 设计是否高估 death asymmetry 对 realistic routing 的影响？\n   - 跨模型/跨环境验证的覆盖度和说服力\n\n3. **Router 实验**：\n   - Router negative result 的两种解释（label noise vs fundamental non-learnability）是否公正？\n   - Data scaling ablation 使用 paraphrase augmentation 的局限性\n   - 4B episode-level improvement (59.0%) 的实际意义\n   - Router 实验作为 \"diagnostic probe\" 的定位是否合理？\n\n4. **Agent improvement 实验**：\n   - Reflexion/Retry/72B 的实验设计和统计功效\n   - Dose-response 分析的 plateau 结论是否有足够证据支撑？\n   - Grounding ablation (48%→29%) 的设计和解释\n\n5. **DAF 度量本身**：\n   - DAF 随 P 单调递增是代数后果——论文是否充分承认这一点？\n   - 78.9% label fraction vs DAF 的关系是否清晰？\n   - P-invariance by design 的声明是否准确？\n\n请按 ARR 标准出具完整审稿意见：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR), Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 1875 · 2026-05-21T01:19:48.045221+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17917
}
```

</details>

---


### Tool call

_source line 1876 · 2026-05-21T01:19:48.196287+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "simgate-modular-routing",
  "reviewer_id": "2",
  "round_number": "20",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性**。\n\n**论文信息**\n- 标题：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n- 补充材料：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/rebuttal_drafts.md\n\n**Venue 要求**\n- EMNLP 2026 (ARR Long Paper)\n- Deadline：2026-05-25\n- 正文 8 页限制，参考文献不限\n- ACL 模板，double-blind 匿名审稿\n- 必须包含 Limitations section（不计入页数）\n- 附录不计入页数\n\n**你的审查侧重**\n\n1. **新颖性和 Contribution 定位**：\n   - 核心发现（death dominance in ScienceWorld）是否 \"obvious in hindsight\"？novelty ceiling？\n   - Framework contribution vs empirical finding 的平衡——论文是否在 framework-centric 和 finding-centric 之间摇摆？\n   - Contribution 1/2/3 的独立价值和清晰度\n   - 与 concurrent work (CogRouter, ARES, MTRouter, budget-aware-routing 等) 的区分度\n   - 对 routing 文献的 prior assumptions 的反差是否convincing？\n\n2. **Framing 一致性**：\n   - Abstract/Introduction/Discussion/Conclusion 的叙事是否一致？\n   - DAF vs 78.9% label fraction 哪个是 headline metric？是否混淆？\n   - \"Structural\" / \"structurally determined\" 等措辞是否有足够证据支撑？\n   - 跨环境分析 (MATH, ALFWorld) 定位为 \"boundary probes\" 而非 \"validation\" 是否恰当？\n   - 三个环境的 \"deterministic\" 含义不同——是否充分讨论？\n\n3. **Related Work 完整性**：\n   - Safe RL (CMDP, risk-sensitive RL) 的覆盖是否充分？\n   - LLM agent failure modes 的相关文献是否充分？\n   - Noisy label learning 的引用是否恰当？\n   - 是否遗漏重要相关工作？\n\n4. **写作质量**：\n   - Abstract 是否数字堆砌？concept-first vs number-first？\n   - Conclusion 长度是否匹配 long paper？\n   - Limitations section 是否全面且组织良好？\n   - 术语一致性（modality vs computation mode）\n   - 表格 caption 是否清晰？Figure/Table 引用是否准确？\n\n5. **格式合规**：\n   - 正文是否超 8 页？\n   - ACL 模板使用是否正确？\n   - 匿名是否完整（无自引泄露）？\n   - Limitations section 是否存在？Ethics Statement？\n   - Responsible NLP Checklist 是否包含？\n   - 参考文献格式是否统一？是否有 orphan entries？\n\n请按 ARR 标准出具完整审稿意见：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR), Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "simgate-modular-routing",
    "reviewer_id": "2",
    "round_number": "20",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性**。\n\n**论文信息**\n- 标题：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n- 补充材料：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/rebuttal_drafts.md\n\n**Venue 要求**\n- EMNLP 2026 (ARR Long Paper)\n- Deadline：2026-05-25\n- 正文 8 页限制，参考文献不限\n- ACL 模板，double-blind 匿名审稿\n- 必须包含 Limitations section（不计入页数）\n- 附录不计入页数\n\n**你的审查侧重**\n\n1. **新颖性和 Contribution 定位**：\n   - 核心发现（death dominance in ScienceWorld）是否 \"obvious in hindsight\"？novelty ceiling？\n   - Framework contribution vs empirical finding 的平衡——论文是否在 framework-centric 和 finding-centric 之间摇摆？\n   - Contribution 1/2/3 的独立价值和清晰度\n   - 与 concurrent work (CogRouter, ARES, MTRouter, budget-aware-routing 等) 的区分度\n   - 对 routing 文献的 prior assumptions 的反差是否convincing？\n\n2. **Framing 一致性**：\n   - Abstract/Introduction/Discussion/Conclusion 的叙事是否一致？\n   - DAF vs 78.9% label fraction 哪个是 headline metric？是否混淆？\n   - \"Structural\" / \"structurally determined\" 等措辞是否有足够证据支撑？\n   - 跨环境分析 (MATH, ALFWorld) 定位为 \"boundary probes\" 而非 \"validation\" 是否恰当？\n   - 三个环境的 \"deterministic\" 含义不同——是否充分讨论？\n\n3. **Related Work 完整性**：\n   - Safe RL (CMDP, risk-sensitive RL) 的覆盖是否充分？\n   - LLM agent failure modes 的相关文献是否充分？\n   - Noisy label learning 的引用是否恰当？\n   - 是否遗漏重要相关工作？\n\n4. **写作质量**：\n   - Abstract 是否数字堆砌？concept-first vs number-first？\n   - Conclusion 长度是否匹配 long paper？\n   - Limitations section 是否全面且组织良好？\n   - 术语一致性（modality vs computation mode）\n   - 表格 caption 是否清晰？Figure/Table 引用是否准确？\n\n5. **格式合规**：\n   - 正文是否超 8 页？\n   - ACL 模板使用是否正确？\n   - 匿名是否完整（无自引泄露）？\n   - Limitations section 是否存在？Ethics Statement？\n   - Responsible NLP Checklist 是否包含？\n   - 参考文献格式是否统一？是否有 orphan entries？\n\n请按 ARR 标准出具完整审稿意见：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR), Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 1877 · 2026-05-21T01:19:49.798212+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1601
}
```

</details>

---


### Assistant

_source line 1878 · 2026-05-21T01:20:05.031674+00:00_

视觉审查已派发，Reviewer 1 和 Reviewer 2 已分配任务。

**当前状态**：
- 视觉审查 Agent：已启动（fire-and-forget）
- Reviewer 1（方法严谨性 + 实验设计）：已分配，审稿中
- Reviewer 2（新颖性 + 完整性）：已分配，审稿中

等待两位 Reviewer 提交初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 148

## Round 148

2 recorded events


### User

_source line 1879 · 2026-05-21T01:26:25.110548+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — 新颖性 + 完整性

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (ARR Long Paper)
**审查侧重**: 新颖性、Contribution 定位、Framing 一致性、Related Work 完整性、写作质量、格式合规

---

## 总体评分

**Overall Assessment**: 3.0 / 5 — Findings
**一句话总结**: 方法论扎实、统计分析严谨的诊断框架论文，但核心发现（death dominance）在很大程度上是 ScienceWorld 奖励结构的自然推论，novelty ceiling 有限，且正文超出 8 页限制。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论设计清晰，bootstrap CI + cluster-robust inference 统计基础扎实；但 "structurally determined" 用语 overclaim，将高相关 (r=0.97) 等同于结构性/因果决定 |
| Excitement | 2.5/5 | 核心发现 novelty 有限——ScienceWorld 的 −100 death penalty 使 death dominance 近乎必然；框架本身概念简洁但深度有限；实用产出为负结果（router 无法超越 always-deterministic） |
| Reproducibility | 4/5 | Algorithm 1 完整，实验细节充分（Appendix I 训练参数、Table 9 超参、Appendix J seed robustness），承诺代码公开 |
| Overall | 3.0/5 | 适合 Findings 收录——工作完整、统计严谨，但 novelty 和 breadth 不足以进入主会议 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文超出 8 页限制
- 具体位置：Page 9, §6 Conclusion
- 问题：EMNLP 2026 规定正文严格 8 页。§5 Discussion 占满 Page 8 两栏，§6 Conclusion 起始于 Page 9 顶部（左栏），之后才是 Limitations。即便 Conclusion 仅约 15 行，正文（Abstract 到 Conclusion）已超出 8 页。Limitations 和 Ethics Statement 不计入页数限制，但 Conclusion 属于正文。
- 为什么影响接收：ARR 有格式合规的 desk-reject 机制。正文超页是硬性违规。
- 建议修改方向：压缩 §5 Discussion（当前约 1.5 页，可精简至 1 页）或将部分 Discussion 内容移入 Appendix。

**N2** [critical] Novelty ceiling：核心发现是环境奖励设计的自然推论
- 具体位置：§3.1, §5 ¶1-2
- 问题：ScienceWorld 的 death penalty 为 −100（Abstract, §2.3），而非 death episode 的典型正分数远低于此（Table 1: deterministic non-death score 48.0, internal non-death 43.5）。在这种 asymmetric penalty 下，death rate differential *必然* 主导 routing signal——这不是发现，而是数学上的近似必然。论文声称 intervention resistance（72B scaling, Reflexion, dose-response）构成 non-obvious 发现（§5 ¶2, rebuttal drafts #2），但 72B 的 DAF *增加*到 92.4% 恰恰支持了"只要 penalty 结构不变、death dominance 不变"这一预期。
- 论文自身矛盾：§3.6 的 router training 负结果和 §5 的 Discussion 实际上在论证"这个环境里 routing 没有意义"——如果框架的主要结论是"在这个特定环境中不要做 routing"，贡献的影响范围十分有限。
- 为什么影响接收：Excitement/novelty 是 ARR 的独立评分维度。如果核心 finding 可以从奖励结构直接预测，论文的 contribution 就主要落在框架方法论上——而框架本身（比较两种策略、按 death/non-death 分解）概念上较为 straightforward。
- 建议修改方向：(a) 在更多具有不同 penalty 结构的环境（如 NetHack/Crafter，论文 §5 已提到）进行深度分析，而非仅作为 boundary probe；(b) 明确论证框架在 death penalty 可预测的情况下，其定量诊断的 *增量价值* 是什么（即：practitioner 在没有框架的情况下是否也能得出同样结论）。

**N3** [critical] "Structurally determined" overclaim
- 具体位置：§3.1 ("death dominance is a structural consequence of death dominance, not an independent finding"), §5 ("death-prone failure is structurally determined"), Title implicit framing
- 问题：论文反复使用 "structural" / "structurally determined" 来描述 death rate 与 routing signal 的关系，但支撑证据是 Pearson r = 0.97（§3.1）和 r = 0.97 的 correlation（Appendix K）。高相关不等于结构性/因果决定。"Structural" 在学术语境中暗示因果机制或逻辑必然性，但论文展示的仅是统计共变。
- 反例考量：如果在某些 task type 中 death rate differential 很大但 routing signal 受其他因素（如 task-specific reasoning difficulty）调制，r=0.97 会下降。论文没有排除 task difficulty 作为 confound 的可能性（death-prone tasks 是否恰好也是 harder tasks？Table 3 的 per-task 分析显示 death-prone tasks 的 deterministic scores 系统性偏低，暗示 task difficulty 可能 confound）。
- 为什么影响接收：Overclaim 是 soundness 问题。审稿人需要确信论文的核心 claim 有充分证据支撑。
- 建议修改方向：将 "structurally determined" 改为 "strongly correlated" 或 "empirically dominated"；如要保留 structural claim，需要 causal identification（如 instrumental variable 或 environment manipulation 实验）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 数字堆砌，concept-first 不足
- 具体位置：Abstract 全段
- 问题：Abstract 在约 250 词中塞入至少 10 个百分比数字（78.9%, 90.4%, 97.4%, 73.5%, 88.25%, 90.45%, 42.9%, 98.45%, 等）。读者在第一次阅读时很难区分这些数字分别对应什么指标。核心概念（counterfactual diagnostic, death avoidance as routing signal）被数字淹没。
- 建议：重写 Abstract 为 concept-first 结构——先用一两句话说清核心发现（在 ScienceWorld 中，routing signal 几乎完全由 death avoidance 驱动），然后用 2-3 个 key numbers（DAF, label fraction, cross-model 一致性）作为支撑，而非列举所有数字。

**W2** [warning] Contribution 1/2/3 的独立价值和 framing 摇摆
- 具体位置：§1 ¶最后一段 ("Our contributions"), Abstract
- 问题：三个 contribution——(1) diagnostic framework, (2) death dominance finding, (3) cross-model validation——之间的独立性不明确。Contribution 2 和 3 是 Contribution 1 的应用结果，不是独立的贡献。论文在 framework-centric（标题用 "Counterfactual Analysis"）和 finding-centric（标题用 "Death Avoidance as the Dominant Routing Signal"）之间摇摆。Abstract 先说框架，然后大量篇幅用在数字结果上。Introduction 和 Discussion 的叙事重心也不一致。
- 建议：明确论文的 primary contribution 是框架还是 finding，另一个作为 secondary。如果选框架，需要在更多环境上展示框架的诊断能力（不仅是 boundary probes）；如果选 finding，需要更深入地分析为什么 death dominance 的精确量化有独立价值。

**W3** [warning] "Deterministic" 在三个环境中含义不同，缺乏显式讨论
- 具体位置：§2.1 (ScienceWorld), §3.4 (MATH, ALFWorld)
- 问题：在 ScienceWorld 中，"deterministic" = oracle simulator with ground-truth observations + actions；在 MATH 中，"deterministic" = code interpreter（Python execution）；在 ALFWorld 中，"deterministic" = ground-truth admissible actions（信息优势）。这三种 "deterministic" 提供的 advantage 质性上完全不同（error elimination vs. computational verification vs. information access），但论文用同一个术语且未显式讨论这一歧义。
- 影响：读者可能误以为跨环境对比是在比较同类事物。这也影响 §5 Discussion 中关于 "deterministic safety" 的一般性论述的可靠性。
- 建议：在 §2.1 或 §3.4 开头添加一段明确讨论，说明 "deterministic" 在不同环境中的具体含义及其提供的 advantage 类型差异。

**W4** [warning] Router training 负结果基于单一架构，结论过强
- 具体位置：§3.6
- 问题：Router training 的负结果仅基于 Qwen3-1.7B + LoRA（Table 9, Appendix I）。论文据此得出 "step-level learnable signal" 在 ScienceWorld 中不存在的结论（§3.6 最后一句: "leaving no learnable signal for a step-level router to exploit"）。但这可能只是说明这个特定的模型+训练策略不 work。没有尝试其他架构（如 lightweight classifier, feature-based router）或其他 training signal（如 reward shaping, hindsight relabeling）。
- 建议：弱化结论为 "在我们测试的配置下"，或者增加更多 router 架构的消融。

**W5** [warning] Noisy label learning 的引用和讨论不充分
- 具体位置：§3.6 ("the high uninformative rate connects to noisy label learning"), experiments.tex line 113
- 问题：论文引用 Natarajan et al. (2013) 将 label noise 与 routing label 质量联系起来，但讨论深度不足。Noisy label learning 领域有大量后续工作（如 symmetric noise, instance-dependent noise, confident learning）可以为 routing label 的质量问题提供更精确的框架。当前的讨论只是一句话带过，没有说明这个 connection 的具体启示。
- 建议：要么深化讨论（说明 label noise 类型和可能的缓解策略），要么删除这个 connection 以避免给出未充分发展的线索。

---

## 小问题（不影响接收）

- **Orphan bib entries**: huang2022inner, selfcheckgpt-2023, wang2023voyager 在 .bib 中存在但未被引用。
- **Webb (2023) 年份 mismatch**: OpenAlex 记录该论文发表年份为 2014（Canadian Journal of Economics 的 working paper vs. publication 年份差异），bib 中标注为 2023。需核实并统一。
- **Terminology 不一致**: §2.1 用 "computation mode"，§4 Related Work 用 "modality"（"adapt per-step modality"），两者指同一概念但用词不同。建议统一。
- **Figure 2 caption**: "Performance and DAF_penalty" 的 y 轴标签在图中不够清晰（两条线共享 y 轴但量纲不同——performance gap vs. DAF ratio）。建议使用 dual y-axis 或分开为两个子图。
- **Table 2 caption**: "Episode-weighted mean scores on ScienceWorld" 的 "single random seed (42)" 应在 caption 中说明 seed 的意义（reproducibility seed vs. data split seed）。
- **Appendix R 的 Practitioner Decision Framework**: 提供了可操作的三步决策流程，但 Stage 1 的 "~50 episodes" 和 "~2 GPU-hours" 是基于 ScienceWorld 的估计，在其他环境中可能显著不同。应注明这一点。

---

## Missing References

1. **Safe RL 中的 reward shaping 文献**: 论文讨论了 CMDP 和 risk-sensitive RL，但没有引用 reward shaping（如 Ng et al., 1999, "Policy invariance under reward transformations"）在处理 extreme penalties 时的相关工作。Death dominance 本质上是 reward shaping 问题。
2. **LLM agent failure taxonomy**: 除 Ruan et al. (2024) 外，近期有更多关于 LLM agent 系统性 failure mode 的工作（如 agent 的 action space exploration failure, hallucination-induced execution failure），可以丰富 §4 对 failure modes 的讨论。
3. **Confident Learning (Northcutt et al., 2021)**: 论文提到 noisy label learning 但只引用了 Natarajan et al. (2013)。Confident Learning 提供了实际可用的 noisy label 检测和清理方法，与 §3.6 的 uninformative label 问题直接相关。

---

## 主要优势

1. **统计方法论严谨**: Episode-level bootstrap（B=10,000）、wild cluster bootstrap、leave-one-out sensitivity analysis、dose-response 分析——统计基础在 NLP 会议论文中属上乘水平。Cameron & Webb 的 clustered inference 方法引用恰当。
2. **Cross-model replication 有说服力**: 三个架构族（Qwen/GQA, Llama/GQA, Gemma/SWA）独立复现 DAF 88-90%，CI 重叠。Table 16-17 的 cross-model 分析增强了结论的可靠性。
3. **Appendix 全面且有信息量**: 19 个 Appendix（A-S）涵盖 labeling quality audit、per-task decomposition、correlation robustness、seed robustness、data scaling、penalty sensitivity、cross-environment details、failure mode analysis、grounding ablation、threshold routing。这种 thoroughness 在同类论文中少见。
4. **Honest limitations**: 论文明确承认单环境局限（Limitations ¶1-2）、排除任务的处理（Appendix S）、以及 router 负结果的边界条件。
5. **实际可操作的 diagnostic pipeline**: Appendix R 的三步决策框架（pilot → dominance check → decision）为 practitioner 提供了具体指引。Table 20 的 retrospective validation 显示框架在 4/4 条件下正确分类。

---

## Questions for Authors

1. 如果将 ScienceWorld 的 death penalty 从 −100 降至 −10 或 −1（保持其他 reward 不变），DAF 会如何变化？Appendix K 的 penalty sensitivity analysis 改变的是 DAF 的计算方式（penalty magnitude in the formula），而非环境的实际 death penalty。能否做一个 *环境层面* 的 penalty manipulation 实验？
2. 论文声称 "death-prone failure is structurally determined"。能否提供反例——即一个 death-prone task 中 death rate differential 很大、但 routing 不应选择 deterministic 的场景？如果不能，这是否说明 "structural" 只是 "penalty magnitude 足够大时的必然结果"？
3. Appendix R 的 decision framework 在 MATH 和 ALFWorld 上是否做过 prospective validation（即先运行 pilot，再用框架决策，最后验证决策正确性）？Table 20 只报告了 ScienceWorld 的 retrospective validation。
4. §3.3 报告 Reflexion (N=3) 使 DAF > 100%。这是否意味着 Reflexion 在 non-death episodes 上引入了*新的* performance regression（deterministic 反而落后于 internal），而非仅是 death avoidance 的改善？如果是，这对 Reflexion 的可靠性意味着什么？

---

**Confidence**: 4/5 — 审稿领域（LLM agents, adaptive computation, interactive environments）与我的研究方向匹配。对 ScienceWorld 环境和 routing 文献有充分了解。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1880 · 2026-05-21T01:26:42.001768+00:00_

Reviewer 2 审稿意见已收到。评分 3.0/5 (Findings)，提出 3 个 Must-Fix（正文超页、novelty ceiling、structurally determined overclaim）和 5 个 Should-Fix。

等待 Reviewer 1 提交审稿意见后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 149

## Round 149

2 recorded events


### User

_source line 1881 · 2026-05-21T01:26:44.660047+00:00_

[Reviewer 2 审稿结果]:
审稿完成。核心评分：

- **Overall: 3.0/5 (Findings)**
- **Soundness: 3.5/5** — 统计方法扎实，但 "structurally determined" overclaim
- **Excitement: 2.5/5** — death dominance 在 −100 penalty 下近乎必然，novelty ceiling 有限

三个 Must-Fix：
1. **正文超 8 页**（Conclusion 在 page 9）
2. **Novelty 受限于环境设计**（−100 death penalty 使 death dominance 成为数学推论而非"发现"）
3. **"Structurally determined" overclaim**（r=0.97 相关 ≠ 结构性因果）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1882 · 2026-05-21T01:26:54.933373+00:00_

Reviewer 2 审稿意见已收录。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 150

## Round 150

6 recorded events


### User

_source line 1883 · 2026-05-21T01:30:04.218566+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**审查侧重**: 方法严谨性 + 实验设计

---

## 总体评分

**Overall Assessment**: 3.5 / 5（Borderline Conference）
**一句话总结**: 框架设计严谨、统计分析全面，但核心发现的惊喜度有限，部分统计推断方法存在内在矛盾需要解释。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体 sound，但 cluster bootstrap CI 反常收窄（K=11）、4B router 异常结果未解释、dose-response plateau 证据不足 |
| Excitement | 3.0/5 | 诊断框架有实用价值，但 "death penalty 主导 routing signal" 在 ScienceWorld 的 −100 惩罚结构下方向可预见，cross-environment 验证仅为边界探测 |
| Reproducibility | 4/5 | 方法描述详尽，承诺开源代码和数据，Appendix 提供完整超参数（Table 9）和训练细节 |
| Confidence | 4/5 | 仔细检验了所有统计方法、实验设计和度量定义 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Wild cluster bootstrap CI 反常收窄，robustness check 自身可靠性存疑

- 具体位置：Section 2.4, Appendix E (Table 6)
- 问题：Non-clustered bootstrap 给出 DAF 95% CI = [81.1%, 99.0%]，而 wild cluster bootstrap (K=11) 给出 CI = [95.2%, 99.5%]——cluster 方法反而产生了**更窄**的 CI。这在统计学上是反常的：考虑了 intra-cluster correlation 后，CI 通常应当更宽而非更窄。Cameron, Gelbach & Miller (2008) 和 Webb (2023)——论文自己引用的文献——明确指出 K < 20–30 时 wild cluster bootstrap 会**低估方差**，产生虚假紧凑的 CI。论文在主文中承认 "this test falls below the K≥20–30 threshold recommended for reliable inference"（Section 2.4），但随后在 Appendix E 仍将其作为 "robustness check" 呈现，并报告了更紧的 CI [95.2%, 99.5%]。如果 robustness check 本身因 K 不足而不可靠，它提供的是 **false assurance** 而非真正的 robustness。
- 为什么影响接收：统计推断可靠性是本文核心贡献之一。如果主要推断方法（non-clustered bootstrap）假设 episodes 独立（忽略 task-type 内相关性），而备选方法（cluster bootstrap）因 K 不足而不可靠，那么 DAF 的 CI 可能既偏窄（non-clustered）又不可验证（clustered），论文的置信区间可靠性成疑。
- 建议修改方向：(1) 正面讨论两个 CI 的不一致性及其统计原因——是 within-cluster correlation 极高导致 cluster units 几乎同质（此时 cluster CI 窄是合理的），还是 K=11 低估方差？如果是前者，提供 ICC (intra-class correlation) 估计作为证据。(2) 考虑将 cluster bootstrap 降级为 "acknowledged limitation" 而非 "robustness check"。(3) 补充 block bootstrap（按 task-type 分块但不要求 K≥20）或 randomization inference 作为替代。

**N2** [critical] Qwen3-4B router episode-level 59.0% 结果与 "fundamental non-learnability" 结论矛盾，未充分讨论

- 具体位置：Section 3.6, Appendix P (Table 18)
- 问题：Table 18 显示 Qwen3-4B 是**所有模型尺度和架构中唯一突破 chance 的模型**——episode-level balanced accuracy 59.0% ± 1.9%（p < 0.05，4 seeds）。同一表格中 Qwen3-0.6B = 50.7%, 1.7B = 43.1%, 7B = 47.1%，均不显著。论文在主文（Section 3.6）和 Discussion（Section 5 "Why the router fails"）中得出结论：routing signal 是 task-type level binary signal，step-level router **fundamentally** 无法学习。但 4B 的 59% 结果是一个**有意义的反例**：如果 signal 真的 fundamentally non-learnable，为什么 4B 能达到 59%？如果这是统计噪声，为什么 4 seeds 的 SE 只有 1.9%？
- 论文仅在 Appendix P 用一句话提到 "only 4B breaks the random baseline (59.0 ± 1.9, p < 0.05)" 但未做任何解释。这在逻辑上不完整：要么 (a) 4B 确实学到了某种 episode-level 信号（则 "non-learnability" 结论需要 qualify），要么 (b) 59% 是 multiple comparison artifact（4 model scales × 2 granularities = 8 tests，Bonferroni 校正后 p < 0.05/8 = 0.00625 才显著），要么 (c) 4B 有特殊的 architectural property 使其能捕获某种 signal。论文必须明确选择一个解释并提供证据。
- 为什么影响接收：Router experiment 是论文四大组件之一（Section 3.6），其 negative result 支撑了 "death avoidance 是 task-level binary signal" 的核心论点。如果 4B 结果是真实的，这个核心论点需要修正；如果是 artifact，需要明确论证。
- 建议修改方向：(1) 报告 multiple comparison-corrected p-values（8 tests: 4 scales × 2 granularities）。(2) 如果 4B 结果存活 correction，分析 4B 的 per-task routing accuracy 以确定它是否在 death-prone tasks 上有选择性优势。(3) 在 Section 5 明确讨论 4B 结果并 qualify "non-learnability" 结论。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Dose-response "plateau" 结论统计功效不足

- 具体位置：Section 3.3, Figure 3, Appendix H (Table 8)
- 问题：Figure 3 显示 Reflexion 和 Retry 的 death rate 随 N (intervention trials) 变化趋势，论文声称存在 "plateau at N ≥ 3"（Section 3.3）。但 (1) 数据仅有 N = 1, 2, 3, 4, 5 共 5 个点；(2) Wilson 95% CI bands 在各点之间大量重叠；(3) 论文自述 minimum detectable effect at N=5 is ~5pp（α=0.05, 80% power）。如果真实改善幅度为 3-4pp（完全有可能），则在此 sample size 下不可检测。因此 "plateau" 与 "持续但缓慢的下降" 无法区分。
- 建议：(1) 将 "plateau" 表述软化为 "no statistically detectable improvement beyond N=3"，明确区分 "无效果" 和 "检测不到效果"。(2) 报告达到 plateau 所需的 effect size detection threshold。

**W2** [warning] Data scaling ablation 使用 paraphrase augmentation 不构成真正的 data scaling test

- 具体位置：Section 3.6, Appendix I (Table 11)
- 问题：Data scaling ablation 将训练集从 25% 扩展到 800%，但扩展方式是 "synonym substitution + template variation on step observations"。Paraphrase augmentation **不产生新的 routing patterns**——它只改变同一 episode 的文本表面形式。Table 11 显示 "Augmentation-based data scaling provides no improvement at any scale"，但这可能仅意味着 augmentation 无效，而非 "更多真实数据也无效"。论文自身也承认 "episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes"。
- 实际上，routing signal 是 task-type level binary（是否有 death mechanism），所以增加同一 task type 的 paraphrased examples 不可能增加 routing 信号的多样性——这是一个 **expected null** 而非 informative null。
- 建议：(1) 在正文中明确承认 paraphrase augmentation 不等同于 genuine data scaling（收集新 episodes with different seeds）。(2) 如果计算资源允许，补充一个用真实新 episodes（不同 random seeds）进行 data scaling 的实验，哪怕是小规模的。(3) 将当前 ablation 重新定位为 "augmentation doesn't help" 而非 "data scaling doesn't help"。

**W3** [warning] Episode-level labeling 的 mislabeling 问题与 router failure 的因果关系未厘清

- 具体位置：Section 2.3, Section 3.6, Appendix B
- 问题：论文提出 router failure 的两种解释：(A) episode labels 投射到 step level 引入 noise，(B) routing signal fundamental non-learnability。但论文倾向于解释 (B) 而未充分排除 (A)。具体来说：
  - 97.4% step-level tie rate（Section 2.2）说明 step level 几乎没有 discriminative signal，但这不证明 episode labels 没有 mislabel 那 2.6% 的 non-tie steps
  - Appendix B 的 label quality audit 显示 step-level balanced accuracy 57.3%——仅略高于 chance——但这是用 episode labels 作为 ground truth 评估 step-level 预测，本身就是循环论证
  - 如果 mislabeling 是 router failure 的主要原因，则 "fundamental non-learnability" 结论不成立
- 建议：讨论是否可以设计一个实验来区分两种解释——例如，在 task types 内部做 leave-first-N-steps-out 分析，或在纯 death-asymmetric episodes 中只用 pre-death steps 的 labels 训练 router。

**W4** [warning] DAF 与 label fraction 的关系在主文中解释不够直观

- 具体位置：Section 2.4, Appendix K
- 问题：Label fraction = 78.9%（penalty-independent），DAF = 90.4%（P=100）。DAF > label fraction 是因为 death-asymmetric episodes 的 per-episode score gap 规模远大于 non-death episodes（P = 100 >> 典型 non-death gap ~29 点）。这意味着 DAF 不仅反映 death-asymmetric episodes 的**数量**，还被它们的 **score magnitude** 放大。论文在 Appendix K 承认 "DAF increases monotonically with P, a mathematical consequence"，主文也提到，但**主文未解释 DAF 为何比 label fraction 高 12 个百分点**。一个不熟悉该度量的读者可能以为 90.4% 和 78.9% 是独立证据，而实际上 DAF > label fraction 是代数后果。
- 建议：在 Section 2.4 添加一句解释 DAF > label fraction 的原因（death episodes 的 per-episode gap ≈ P 远大于 non-death episodes 的 gap，导致 score-weighted 度量被放大）。

**W5** [warning] Per-task n=20 导致 13/28 tasks 不显著，per-task decomposition 应明确标注为 exploratory

- 具体位置：Section 3.1, Table 3, Appendix F (Table 6)
- 问题：Table 3 的 per-task 分解是论文的重要分析工具，但 Table 6 显示 15/28 tasks individually significant，13/28 不显著。论文在 Appendix F 注明 "statistical power is insufficient to detect even large effects"，但 Table 3 在主文中呈现时没有此 caveat。Per-task n=20 的 power analysis：对于一个 20pp 的 death-rate differential，n=20 的 power 仅约 50%（two-sided α=0.05, binomial test）。
- 建议：在 Table 3 的 caption 或正文引用处明确标注 per-task CIs 及哪些 tasks 的 effects 不显著，避免读者将 exploratory per-task patterns 误读为 confirmed effects。

---

## 小问题（不影响接收）

- **格式**：主文可能略超 8 页。Section 6 (Conclusion) 起始于第 9 页，虽然 Limitations 和 Ethics Statement 不计入页数限制，但 Conclusion 属于主文。建议检查是否能通过缩减 Related Work 或 Discussion 中的冗余部分将 Conclusion 压入第 8 页。
- **Table 2 caption**：注释 "1 Single random seed (42) per episode pair" 可能被误解为每个 task type 只有一个 seed。建议改为 "1 fixed random seed (42) per strategy pair; 20 episode pairs per task type"。
- **SCI 呈现**：SCI = 0.2147 在 Appendix A 有详细说明但主文仅一笔带过（Section 2.4），作为 "signal 不被少数 task types 驱动" 的证据，建议在 Section 3.1 更明确地引用。
- **Figure 2 readability**：Per-task scatter plot 点标签密集，部分 task names 重叠不可读。

---

## Questions for Authors

1. **Cluster bootstrap CI 收窄的原因**：能否提供 intra-class correlation (ICC) 估计？如果 ICC 非常高（接近 1），则 cluster units 近似同质，cluster CI 收窄是合理的。如果 ICC 中等，则 K=11 的 cluster bootstrap 很可能低估方差。

2. **4B router 结果**：Qwen3-4B 的 episode-level 59.0% 在 Bonferroni 校正（8 tests）后是否仍然显著？能否提供 4B 的 per-task routing accuracy 以确定其优势来源？

3. **Label fraction 的 P-invariance 声明**：论文称 label fraction 是 "penalty-independent"。严格来说，当 P → 0 时，death-asymmetric episodes 的 label 可能翻转（如果 non-death score gap 抵消了微小的 death penalty）。能否澄清 P-invariance 的精确适用范围（是否为 "for all P > 0" 或 "for P sufficiently large"）？

4. **Grounding ablation 的因果推断**：Section 5 和 Appendix O 提到 prompt warning 将 death rate 从 48% 降至 37%，action-space filtering 降至 29%。但 filtering 物理阻止了 `focus on`——这不是 agent 学会了避免 death，而是 环境被修改了。能否讨论这对 "death avoidance as routing signal" 的影响——如果 death 可以通过环境约束消除，routing signal 的实际意义是什么？

5. **Pure-strategy 设计与 mixed-strategy routing 的 gap**：论文 discussion (Section 5) 提到 "mixed-strategy extension" 是 future work。但当前 pure-strategy 设计是否**高估**了 death asymmetry 的影响？在 realistic mixed routing 中，router 可以在危险步骤切换到 deterministic 而在安全步骤使用 internal——此时 death avoidance 的贡献可能远低于 episode-level 的 90.4%。

---

## Missing References

无明显缺失。论文引用了 agent routing (Chameleon, ART, ReAct, Reflexion, SALT 等)、safe RL (constrained MDPs, safe exploration)、ScienceWorld/ALFWorld/MATH 等核心文献。建议考虑以下补充：
- Kenton et al. (2021) "Alignment of Language Agents" 或类似 alignment 角度讨论 catastrophic failure
- 如有 2025-2026 年新发表的 ScienceWorld routing 相关工作，应检查覆盖

---

## 主要优势

1. **框架设计严谨**：Episode-level counterfactual labeling 方法论上有 principled justification（97.4% step-level tie rate, Section 2.2），避免了 step-level 的 sparsity 问题。Algorithm 1（Appendix 第12页）清晰可复现。
2. **统计分析全面**：四种独立检验（non-clustered bootstrap, wild cluster bootstrap, permutation test, sign test）交叉验证。尽管 cluster bootstrap 有上述问题，多重检验的 converging evidence 增强了结论可信度。
3. **Anti-cherry-picking analysis 堪称典范**：Appendix C (Table 4) 显示被排除的 19 个 task types 的 death asymmetry 更强（mean ΔDR = +38.2pp vs +25.7pp），Appendix S (Table 21) 验证 5 个排除 tasks 的 DAF = 0.991。这有效排除了 selection bias。
4. **Cross-model 三模型 replication**：Qwen/Llama/Gemma 三个架构家族（GQA/GQA/SWA）独立复现 DAF 85-90%，point estimates 在 5pp 内，CIs 重叠。方向一致性 100%（Table 17）。
5. **负面结果诚实呈现**：Router training 的 negative result（Section 3.6）和 MATH 的 null result（Section 3.4）没有被掩盖或弱化，而是整合到框架的诊断价值论证中。
6. **Appendix 极为详尽**：14 页附录覆盖 SCI 推导、label quality audit、per-task decomposition、bootstrap 变体、cross-environment details、failure mode analysis、grounding ablation、threshold routing 等。Reproducibility checklist（pages 21-23）完整。

---

## 总结

这是一篇**方法论扎实但兴奋度中等**的分析型论文。核心框架（counterfactual labeling + DAF + SCI）设计合理，统计分析全面，cross-model 验证充分。主要问题在于：(1) cluster bootstrap CI 反常收窄需要解释，(2) 4B router 结果与 non-learnability 结论矛盾未讨论，(3) dose-response plateau 和 data scaling ablation 的证据力度有限。如果作者能在修改中解决 N1 和 N2 两个 critical 问题，评分可上调至 4.0（Conference）。当前判断：Borderline Conference / strong Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1884 · 2026-05-21T01:30:45.775493+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "simgate-modular-routing",
  "reviewer_id": "1",
  "round_number": "20",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — 新颖性 + 完整性\n\n**Overall Assessment**: 3.0 / 5 — Findings\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.0/5 |\n\n### Must-Fix\n\n**N1** [critical] 正文超出 8 页限制\n- §5 Discussion 占满 Page 8 两栏，§6 Conclusion 起始于 Page 9 顶部。即便 Conclusion 仅约 15 行，正文（Abstract 到 Conclusion）已超出 8 页。ARR 有 desk-reject 机制。\n\n**N2** [critical] Novelty ceiling：核心发现是环境奖励设计的自然推论\n- ScienceWorld 的 death penalty 为 −100，非 death episode 的典型正分数远低于此（Table 1: deterministic non-death score 48.0, internal non-death 43.5）。death dominance 不是发现，而是数学上的近似必然。\n- 72B 的 DAF 增加到 92.4% 恰恰支持\"只要 penalty 结构不变、death dominance 不变\"。\n- 框架的主要结论是\"在这个特定环境中不要做 routing\"——贡献影响范围有限。\n\n**N3** [critical] \"Structurally determined\" overclaim\n- 高相关 (r=0.97) 不等于结构性/因果决定。\n- 未排除 task difficulty 作为 confound（death-prone tasks 是否恰好也是 harder tasks？）。\n- 建议将 \"structurally determined\" 改为 \"strongly correlated\" 或 \"empirically dominated\"。\n\n### Should-Fix\n\n**W1** Abstract 数字堆砌（至少 10 个百分比数字，concept 被淹没）\n**W2** Contribution 1/2/3 独立价值不清，framework vs finding 摇摆\n**W3** \"Deterministic\" 在三个环境中含义不同，缺乏显式讨论\n**W4** Router training 负结果基于单一架构，结论过强（\"leaving no learnable signal\"）\n**W5** Noisy label learning 引用和讨论不充分（仅 Natarajan 2013，缺 Confident Learning 等）\n\n### Minor\n- Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\n- Webb (2023) 年份可能为 2014\n- Terminology 不一致：§2.1 \"computation mode\" vs §4 \"modality\"\n- Figure 2 caption 不够清晰\n- Appendix R 的 ~50 episodes / ~2 GPU-hours 是 ScienceWorld-specific\n\n### Missing References\n1. Reward shaping (Ng et al., 1999)\n2. LLM agent failure taxonomy（更多近期工作）\n3. Confident Learning (Northcutt et al., 2021)\n\n### Questions\n1. 能否做环境层面的 penalty manipulation 实验（改变实际 death penalty）？\n2. 能否提供 \"structurally determined\" 的反例？\n3. Appendix R decision framework 是否做过 prospective validation？\n4. Reflexion DAF > 100% 是否意味着 non-death regression？\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "simgate-modular-routing",
    "reviewer_id": "1",
    "round_number": "20",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — 新颖性 + 完整性\n\n**Overall Assessment**: 3.0 / 5 — Findings\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.0/5 |\n\n### Must-Fix\n\n**N1** [critical] 正文超出 8 页限制\n- §5 Discussion 占满 Page 8 两栏，§6 Conclusion 起始于 Page 9 顶部。即便 Conclusion 仅约 15 行，正文（Abstract 到 Conclusion）已超出 8 页。ARR 有 desk-reject 机制。\n\n**N2** [critical] Novelty ceiling：核心发现是环境奖励设计的自然推论\n- ScienceWorld 的 death penalty 为 −100，非 death episode 的典型正分数远低于此（Table 1: deterministic non-death score 48.0, internal non-death 43.5）。death dominance 不是发现，而是数学上的近似必然。\n- 72B 的 DAF 增加到 92.4% 恰恰支持\"只要 penalty 结构不变、death dominance 不变\"。\n- 框架的主要结论是\"在这个特定环境中不要做 routing\"——贡献影响范围有限。\n\n**N3** [critical] \"Structurally determined\" overclaim\n- 高相关 (r=0.97) 不等于结构性/因果决定。\n- 未排除 task difficulty 作为 confound（death-prone tasks 是否恰好也是 harder tasks？）。\n- 建议将 \"structurally determined\" 改为 \"strongly correlated\" 或 \"empirically dominated\"。\n\n### Should-Fix\n\n**W1** Abstract 数字堆砌（至少 10 个百分比数字，concept 被淹没）\n**W2** Contribution 1/2/3 独立价值不清，framework vs finding 摇摆\n**W3** \"Deterministic\" 在三个环境中含义不同，缺乏显式讨论\n**W4** Router training 负结果基于单一架构，结论过强（\"leaving no learnable signal\"）\n**W5** Noisy label learning 引用和讨论不充分（仅 Natarajan 2013，缺 Confident Learning 等）\n\n### Minor\n- Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\n- Webb (2023) 年份可能为 2014\n- Terminology 不一致：§2.1 \"computation mode\" vs §4 \"modality\"\n- Figure 2 caption 不够清晰\n- Appendix R 的 ~50 episodes / ~2 GPU-hours 是 ScienceWorld-specific\n\n### Missing References\n1. Reward shaping (Ng et al., 1999)\n2. LLM agent failure taxonomy（更多近期工作）\n3. Confident Learning (Northcutt et al., 2021)\n\n### Questions\n1. 能否做环境层面的 penalty manipulation 实验（改变实际 death penalty）？\n2. 能否提供 \"structurally determined\" 的反例？\n3. Appendix R decision framework 是否做过 prospective validation？\n4. Reflexion DAF > 100% 是否意味着 non-death regression？\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 1885 · 2026-05-21T01:31:15.422621+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29647
}
```

</details>

---


### Tool call

_source line 1886 · 2026-05-21T01:31:15.573630+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "simgate-modular-routing",
  "reviewer_id": "2",
  "round_number": "20",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n**Overall Assessment**: 3.5 / 5（Borderline Conference）\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.0/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### Must-Fix\n\n**N1** [critical] Wild cluster bootstrap CI 反常收窄，robustness check 自身可靠性存疑\n- Non-clustered bootstrap CI = [81.1%, 99.0%]，wild cluster bootstrap (K=11) CI = [95.2%, 99.5%]——cluster 方法反而更窄。\n- K < 20-30 时 wild cluster bootstrap 低估方差（Cameron et al. 2008, Webb 2023）。\n- 论文主文承认 K≥20-30 threshold，但 Appendix E 仍将其作为 \"robustness check\" 并报告更紧 CI。\n- 如果 robustness check 本身不可靠，提供的是 false assurance。\n- 建议：提供 ICC 估计；考虑 block bootstrap 替代；或降级为 \"acknowledged limitation\"。\n\n**N2** [critical] Qwen3-4B router episode-level 59.0% 结果与 \"fundamental non-learnability\" 结论矛盾\n- Table 18: 4B = 59.0% ± 1.9% (p < 0.05)，其他模型均不显著。\n- 如果 signal fundamental non-learnable，为什么 4B 能达 59%？\n- 可能是 multiple comparison artifact（4 scales × 2 granularities = 8 tests，Bonferroni 校正后 p < 0.00625）。\n- 建议：报告 corrected p-values；分析 4B per-task routing accuracy；qualify \"non-learnability\" 结论。\n\n### Should-Fix\n\n**W1** Dose-response \"plateau\" 结论统计功效不足\n- 仅 5 个点，Wilson CIs 大量重叠，MDE ~5pp。\n- \"Plateau\" 与 \"持续但缓慢下降\" 无法区分。\n- 建议软化为 \"no statistically detectable improvement beyond N=3\"。\n\n**W2** Data scaling ablation 使用 paraphrase augmentation 不构成真正的 data scaling test\n- Paraphrase augmentation 不产生新 routing patterns。\n- Expected null 而非 informative null。\n- 建议重新定位为 \"augmentation doesn't help\" 而非 \"data scaling doesn't help\"。\n\n**W3** Episode-level labeling 的 mislabeling 与 router failure 的因果关系未厘清\n- 倾向解释 (B) non-learnability 而未充分排除 (A) label noise。\n- Appendix B 用 episode labels 评估 step-level 预测是循环论证。\n\n**W4** DAF 与 label fraction 的关系在主文中解释不够直观\n- DAF (90.4%) > label fraction (78.9%) 的原因（score magnitude 放大）未在主文解释。\n\n**W5** Per-task n=20 导致 13/28 tasks 不显著，应标注为 exploratory\n- n=20 对 20pp effect 的 power 仅约 50%。\n- 主文 Table 3 未标注 per-task CIs。\n\n### Questions\n1. Cluster bootstrap CI 收窄的 ICC 估计？\n2. 4B router Bonferroni 校正后是否仍显著？per-task routing accuracy？\n3. Label fraction P-invariance 的精确适用范围？\n4. Grounding ablation 中 action filtering 是修改环境而非 agent 学习——对 \"death avoidance as routing signal\" 的影响？\n5. Pure-strategy 设计是否高估 death asymmetry？mixed routing 中 death avoidance 贡献可能远低于 90.4%？\n\n### Missing References\n- Kenton et al. (2021) alignment 角度\n- 近期 ScienceWorld routing 相关工作\n\n### 主要优势\n1. 框架设计严谨（episode-level counterfactual 有 principled justification）\n2. 统计分析全面（四种独立检验交叉验证）\n3. Anti-cherry-picking analysis 堪称典范（excluded tasks ΔDR = +38.2pp > included +25.7pp）\n4. Cross-model 三模型 replication（DAF 88-90%，CIs 重叠）\n5. 负面结果诚实呈现\n6. Appendix 极为详尽\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "simgate-modular-routing",
    "reviewer_id": "2",
    "round_number": "20",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n**Overall Assessment**: 3.5 / 5（Borderline Conference）\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.0/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### Must-Fix\n\n**N1** [critical] Wild cluster bootstrap CI 反常收窄，robustness check 自身可靠性存疑\n- Non-clustered bootstrap CI = [81.1%, 99.0%]，wild cluster bootstrap (K=11) CI = [95.2%, 99.5%]——cluster 方法反而更窄。\n- K < 20-30 时 wild cluster bootstrap 低估方差（Cameron et al. 2008, Webb 2023）。\n- 论文主文承认 K≥20-30 threshold，但 Appendix E 仍将其作为 \"robustness check\" 并报告更紧 CI。\n- 如果 robustness check 本身不可靠，提供的是 false assurance。\n- 建议：提供 ICC 估计；考虑 block bootstrap 替代；或降级为 \"acknowledged limitation\"。\n\n**N2** [critical] Qwen3-4B router episode-level 59.0% 结果与 \"fundamental non-learnability\" 结论矛盾\n- Table 18: 4B = 59.0% ± 1.9% (p < 0.05)，其他模型均不显著。\n- 如果 signal fundamental non-learnable，为什么 4B 能达 59%？\n- 可能是 multiple comparison artifact（4 scales × 2 granularities = 8 tests，Bonferroni 校正后 p < 0.00625）。\n- 建议：报告 corrected p-values；分析 4B per-task routing accuracy；qualify \"non-learnability\" 结论。\n\n### Should-Fix\n\n**W1** Dose-response \"plateau\" 结论统计功效不足\n- 仅 5 个点，Wilson CIs 大量重叠，MDE ~5pp。\n- \"Plateau\" 与 \"持续但缓慢下降\" 无法区分。\n- 建议软化为 \"no statistically detectable improvement beyond N=3\"。\n\n**W2** Data scaling ablation 使用 paraphrase augmentation 不构成真正的 data scaling test\n- Paraphrase augmentation 不产生新 routing patterns。\n- Expected null 而非 informative null。\n- 建议重新定位为 \"augmentation doesn't help\" 而非 \"data scaling doesn't help\"。\n\n**W3** Episode-level labeling 的 mislabeling 与 router failure 的因果关系未厘清\n- 倾向解释 (B) non-learnability 而未充分排除 (A) label noise。\n- Appendix B 用 episode labels 评估 step-level 预测是循环论证。\n\n**W4** DAF 与 label fraction 的关系在主文中解释不够直观\n- DAF (90.4%) > label fraction (78.9%) 的原因（score magnitude 放大）未在主文解释。\n\n**W5** Per-task n=20 导致 13/28 tasks 不显著，应标注为 exploratory\n- n=20 对 20pp effect 的 power 仅约 50%。\n- 主文 Table 3 未标注 per-task CIs。\n\n### Questions\n1. Cluster bootstrap CI 收窄的 ICC 估计？\n2. 4B router Bonferroni 校正后是否仍显著？per-task routing accuracy？\n3. Label fraction P-invariance 的精确适用范围？\n4. Grounding ablation 中 action filtering 是修改环境而非 agent 学习——对 \"death avoidance as routing signal\" 的影响？\n5. Pure-strategy 设计是否高估 death asymmetry？mixed routing 中 death avoidance 贡献可能远低于 90.4%？\n\n### Missing References\n- Kenton et al. (2021) alignment 角度\n- 近期 ScienceWorld routing 相关工作\n\n### 主要优势\n1. 框架设计严谨（episode-level counterfactual 有 principled justification）\n2. 统计分析全面（四种独立检验交叉验证）\n3. Anti-cherry-picking analysis 堪称典范（excluded tasks ΔDR = +38.2pp > included +25.7pp）\n4. Cross-model 三模型 replication（DAF 88-90%，CIs 重叠）\n5. 负面结果诚实呈现\n6. Appendix 极为详尽\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 1887 · 2026-05-21T01:31:17.082193+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1508
}
```

</details>

---


### Assistant

_source line 1888 · 2026-05-21T01:31:22.060516+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 151

## Round 151

2 recorded events


### User

_source line 1889 · 2026-05-21T01:31:24.732358+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结果摘要**：

- **Overall**: 3.5/5（Borderline Conference）
- **Soundness**: 3.5/5，**Excitement**: 3.0/5

**2 个 Must-Fix 问题**：
1. Wild cluster bootstrap CI 反常收窄（[95.2%, 99.5%] 比 non-clustered 的 [81.1%, 99.0%] 更窄），K=11 下这很可能是方差低估，作为 robustness check 反而提供了 false assurance
2. Qwen3-4B router episode-level 59.0% 是唯一突破 chance 的模型，与 "fundamental non-learnability" 结论矛盾，但论文未做 multiple comparison correction 也未解释原因

**5 个 Should-Fix 问题**：dose-response plateau 功效不足、paraphrase augmentation ≠ genuine data scaling、episode-level mislabeling 与 router failure 的因果未厘清、DAF vs label fraction 关系解释不够直观、per-task n=20 导致 13/28 tasks 不显著

**主要优势**：框架设计严谨、统计分析全面（四种检验）、anti-cherry-picking analysis 堪称典范、三模型 cross-model replication、负面结果诚实呈现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1890 · 2026-05-21T01:31:30.716189+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 152

## Round 152

2 recorded events


### User

_source line 1891 · 2026-05-21T01:33:20.802939+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: 正文超出 8 页限制**

同意这是一个需要修复的格式问题。从 PDF 渲染可以确认，Section 5 (Discussion) 占满 Page 8 双栏，Section 6 (Conclusion) 起始于 Page 9 顶部约 15 行。即使 Limitations 和 Ethics Statement 不计入页数（per EMNLP 2026 规则），Conclusion 仍属于主文正文，所以正文超过了 8 页。ARR 确实有 desk-reject 机制。不过，超出幅度很小（约 0.3 页），通过压缩 Section 4 (Related Work) 或 Section 5 (Discussion) 中的冗余内容即可解决。我在自己的审稿意见中将此列为 minor issue（因为我的审查侧重是方法+实验而非格式），但同意 R2 将其升级为 must-fix 是合理的——desk-reject 风险不能忽视。

**[REBUT] R2-N2: Novelty ceiling — 核心发现是环境奖励设计的自然推论**

R2 认为 death dominance 是 "数学上的近似必然"。我认为这一判断**方向正确但程度夸大**，需要区分几个层次：

(1) **DAF = 90.4% 确实有代数放大成分**——我在自己的审稿中也指出了这点（R1-W4）。P=100 远大于典型 non-death gap (~29 点)，所以 score-weighted DAF 被 penalty magnitude 放大。论文在 Section 2.4 和 Appendix K 都承认了 DAF 随 P 单调递增是 "mathematical consequence"。

(2) **但 label fraction = 78.9% 是 penalty-independent 的**。这个度量计算的是 non-tie labels 中有多少来自 death asymmetry，不受 P 的值影响（Section 2.4: "penalty-independent label fraction"）。78.9% 不是 "数学必然"——它取决于 internal strategy 在哪些 episodes 死亡、deterministic strategy 是否能避免这些死亡。理论上，如果两个策略的 death patterns 完全对称（都死或都不死），label fraction 会是 0%。78.9% 反映的是**经验发现**：internal strategy 的死亡模式与 deterministic strategy 高度不对称。

(3) **论文中有多个非显然预测被验证**：
- 72B 模型的 DAF 增加到 92.4%（Section 3.3）：scaling 减少 death rate 但不减少 death dominance——这不是 penalty structure 的推论，因为更强的模型理论上可以多样化 routing signal（例如在 non-death episodes 上拉开更大差距）
- Reflexion DAF > 100%（Section 3.3）：self-correction 后 internal 在 non-death episodes 上**反而劣于** deterministic（Δ_nd = −0.47），这完全不可从 penalty structure 预测
- 三模型家族 DAF 在 85-90% 范围内收敛（Table 17）：不同架构（GQA vs SWA）可能有不同 vulnerability patterns，但 death dominance 高度一致

(4) **R2 说 "框架的主要结论是在这个特定环境中不要做 routing"**——但这低估了框架的贡献。框架在 ALFWorld 上诊断出完全不同的机制（information asymmetry, DAF=0%, Section 3.4），在 MATH 上正确识别了 null result (p=0.81)。框架的 generality 不依赖于 ScienceWorld 的具体发现。

综上：R2 对 DAF score-weighted metric 的批评与我的 R1-W4 一致，但将整个 novelty 定义为 "近似必然" 是不公平的——penalty-independent label fraction、intervention resistance、cross-architecture consistency 都是非平凡的经验发现。建议作者在修改中更突出 label fraction 而非 DAF 作为 headline metric，并在 Discussion 中前置 "这些发现中哪些不可从 penalty structure 预测" 的讨论。

**[AGREE with qualification] R2-N3: "Structurally determined" overclaim**

部分同意。R2 的两个具体论点需要分别评估：

(1) **r = 0.97 不等于因果**：同意，但论文实际上已自行 defuse 了这个问题。Section 3.2 (Page 4) 明确说 "The near-perfect correlation is a structural consequence of death dominance, not an independent finding (§3.1)"。也就是说，论文并没有用 r=0.97 作为独立证据——它说这个相关是 DAF 高的代数后果。我在 R1 审稿中也确认了这一点。

(2) **Task difficulty confound 未排除**：这是一个有实质的新论点。Death-prone tasks 是否恰好也是 harder tasks？如果是，performance gap 可能部分来自 difficulty 而非 death mechanism。但论文的 counterfactual 设计部分回答了这个问题：对于每个 episode，同一个 task instance 运行两个策略（Section 2.1, Eq. 1-2），控制了 task difficulty。performance gap 来自同一 task 上两个策略的差异，而非 across-task difficulty 差异。不过 R2 的 concern 仍有价值——across-task 汇总中，higher death rate 和 higher difficulty 可能 co-vary，导致 aggregate DAF 被 inflate。

(3) **措辞建议**：同意 "structurally determined" 在因果推断语境中过强。论文可改为 "death-prone failure is the dominant empirical predictor of routing outcomes" 或 "empirically dominated by death asymmetry"。

---

### Should-Fix

**[AGREE] R2-W1: Abstract 数字堆砌**

同意。重新审视 abstract，我数到约 12 个数字/百分比（78.9%, 90.4%, P=100, 11 task types, 245 episodes, Qwen2.5-7B, 85.2%, 89.7%, 4 intervention axes, ~50 episodes, 97.4%, 10×）。对于一篇诊断型论文，核心数字（78.9% label fraction, cross-model consistency）足以传达信息。建议将模型名称、具体 episode 数等细节移至 Section 1，abstract 保留 3-4 个关键数字。

**[REBUT] R2-W2: Contribution 1/2/3 独立价值不清，framework vs finding 摇摆**

论文的三个 contributions 在 Section 1 (Page 2) 结尾处清晰列出：(1) episode-level counterfactual diagnostic framework（方法论贡献），(2) 应用于 ScienceWorld 发现 death dominance（经验贡献），(3) cross-model replication + boundary probes（robustness 贡献）。这三个层次是递进关系而非并列。Section 5 (Discussion) 的子标题也清晰区分了 "Why the router fails"（empirical）vs "Framework applicability"（methodological）vs "Practical value as meta-diagnosis"（practical）。我认为 framework vs finding 的界限在论文中是清楚的。

**[AGREE] R2-W3: "Deterministic" 含义跨环境不一致**

同意。在 ScienceWorld 中，"deterministic" = oracle simulator with ground-truth observations（Section 2.1）；在 ALFWorld 中 = Python code interpreter with admissible-action access（Section 3.4: "admissible-action enumeration"）；在 MATH 中基本 N/A（Section 3.4: p=0.81, no routing signal）。三个环境中 "deterministic" 的信息优势来源完全不同——ScienceWorld 是 ground-truth state, ALFWorld 是 action space visibility。论文应在 Section 2.1 或 Section 3.4 添加一个明确的概念对照表（e.g., 一个小 table: Environment / Deterministic mode / Information advantage / Death mechanism）。

**[AGREE with qualification] R2-W4: Router negative result基于单一架构，"leaving no learnable signal" 过强**

部分同意。论文的 router 实验使用 LoRA fine-tuning on Qwen 系列（Table 9: Qwen3-1.7B/Qwen3-0.6B/1.7B/4B/7B），另有一个 generative router（Appendix P）。我在 R1-N2 中已指出 Qwen3-4B 的 episode-level 59.0% 结果是**唯一突破 chance 的数据点**，与 "no learnable signal" 结论矛盾。

"Leaving no learnable signal for a step-level router" 这个表述确实过强，因为：(1) 只测试了 LoRA + generative 两种架构；(2) 4B 结果显示某些 scale 可能有 learnable signal；(3) 更复杂的方法（如 Confident Learning 去噪 + 更大 router）未测试。建议改为 "current step-level routers fail to exploit the signal" 或 "the signal structure presents substantial challenges for step-level learning"。

**[AGREE] R2-W5: Noisy label learning 引用和讨论不充分**

同意。论文仅引用 Natarajan et al. (2013) 的经典结果（"standard ERM on labels with ~88% noise yields near-chance classifiers"），但 noisy label learning 领域在 2013 后有大量进展：Confident Learning (Northcutt et al., 2021) 可以在高噪声率下估计 noise transition matrix 并清洗 labels；DivideMix、Co-teaching 等方法专门处理 instance-dependent noise。如果 router 的 labels 有 ~88% noise（来自 episode-to-step projection），modern noisy label methods 可能表现更好。论文应至少讨论为什么这些方法不适用（例如：noise 不是 random 而是 systematic——所有 death-asymmetric steps 的 labels 都 biased toward deterministic，这种 structured noise 可能超出 Confident Learning 的假设范围）。

---

### Minor

- **Orphan bib entries (huang2022inner, selfcheckgpt-2023, wang2023voyager)**：无法从 PDF 直接验证，但如果 R2 已确认，应清理。
- **Webb (2023) 年份**：Matthew Webb 的 wild cluster bootstrap 论文原版是 working paper (2014)，后续有 updated versions。需要检查引用的具体版本。
- **Terminology 不一致 ("computation mode" vs "modality")**：同意应统一。
- **Figure 2 caption**：我在 R1 审稿中也指出了 readability 问题，同意。
- **Appendix R 的 ~50 episodes / ~2 GPU-hours**：同意这是 ScienceWorld-specific 估计，应加 caveat。

---

### Missing References

- **[AGREE] Ng et al. (1999) reward shaping**：非常相关——论文讨论的 death penalty dominance 本质上是一个 reward shaping 问题（catastrophic penalty 扭曲了 routing signal）。引用 reward shaping 文献可以为 "penalty structure drives signal" 的论点提供理论 grounding。
- **[AGREE] Confident Learning (Northcutt et al., 2021)**：与 W5 一致。
- **LLM agent failure taxonomy**：有价值但不 critical。论文已引用 Ruan and Friedman (2024) 的 catastrophic action 分类。

---

### Questions

**Q1: 能否做 penalty manipulation 实验？**
[AGREE] 这是一个非常有价值的实验建议。论文在 Appendix K (Table 12) 仅做了**分析性**的 penalty sensitivity（改变 P 值重新计算 DAF），但没有在 ScienceWorld 中**实际改变** death penalty 运行新 episodes。如果实际将 P 从 100 降到 10 或 1，agent behavior 可能改变（例如 internal strategy 可能冒更大风险），此时 label fraction 是否仍为 ~78.9% 就是一个真正的经验问题。这个实验可以区分 "death dominance 来自 penalty structure"（R2-N2 的观点）和 "death dominance 来自 strategy behavior 的固有不对称性"（论文的暗示）。

**Q2: 能否提供 "structurally determined" 的反例？**
与 R2-N3 一致，同意需要更精确的表述。

**Q3: Appendix R decision framework 是否做过 prospective validation？**
[AGREE] Appendix R (Table 20) 展示的是**retrospective** validation（用已有数据回溯验证 4/4 conditions correctly classified）。Prospective validation（在新环境/新模型上先运行 pilot 再验证预测）更有说服力。论文应明确标注这是 retrospective 并讨论 prospective validation 的 feasibility。

**Q4: Reflexion DAF > 100% 是否意味着 non-death regression？**
论文在 Section 3.3 解释了这一点：Reflexion N=3 后，internal strategy 在 non-death episodes 上的表现**反而劣于** deterministic（Δ_nd = −0.47）。DAF = 1 − Δ_nd/Δ_all > 1 因为 Δ_nd < 0（Section 3.3: "death avoidance more than fully accounts for the entire performance gap"）。所以 R2 的理解是正确的——Reflexion 造成了 non-death regression。论文的解释是 self-correction overcompensation：Reflexion 将注意力过度集中在 death avoidance 上，牺牲了 non-death performance。这是一个有趣的发现，但论文对其 mechanism 的讨论较薄。建议作者在 Section 3.3 或 Section 5 中增加对 overcompensation mechanism 的分析——Reflexion 是否在 non-death episodes 中引入了不必要的 conservative behavior？

---

### 总结评估

R2 的主要观点中，**N1（页数超限）** 完全正确且需要立即修复；**N2（novelty ceiling）** 方向正确但程度夸大——penalty-independent label fraction 和多个非平凡预测不是 "数学必然"；**N3（overclaim）** 部分正确，措辞需要调整但核心 counterfactual 设计部分控制了 task difficulty confound。Should-Fix 中 **W3（deterministic 含义不一致）** 和 **W5（noisy label 讨论不足）** 是最有建设性的建议。

我与 R2 的主要分歧在 **novelty 评估**：R2 给 Excitement 2.5/5，我给 3.0/5。我认为 label fraction 78.9%、intervention resistance（72B、Reflexion）、和 cross-architecture consistency 不可从 penalty structure 简单推出，框架在 ALFWorld/MATH 上的 generality 也有独立价值。但我同意论文应更清晰地前置 "这些发现中哪些是非平凡的" 讨论来回应 novelty concern。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1892 · 2026-05-21T01:33:51.226273+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 153

## Round 153

10 recorded events


### User

_source line 1893 · 2026-05-21T01:33:52.404768+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 所有意见的逐条回应。核心判断：

- **N1（页数超限）**：完全同意，需立即修复
- **N2（novelty ceiling）**：反驳——DAF 的代数放大成分我也指出了，但 penalty-independent label fraction 78.9%、intervention resistance、cross-architecture consistency 是非平凡经验发现，不是数学必然
- **N3（overclaim）**：部分同意——措辞过强但 counterfactual 设计已部分控制 task difficulty confound
- **W1-W5**：多数同意，尤其 W3（deterministic 含义不一致）和 W5（noisy label 讨论不足）最有建设性
- **Q1-Q4**：penalty manipulation 实验建议很有价值；Reflexion DAF>100% 确实是 non-death regression

与 R2 的主要分歧在 novelty 评估（我给 3.0 vs R2 给 2.5）。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: Wild cluster bootstrap CI 反常收窄**

同意这是一个实质性统计问题。Non-clustered CI = [81.1%, 99.0%] 宽度 17.9pp，wild cluster bootstrap (K=11) CI = [95.2%, 99.5%] 宽度仅 4.3pp——cluster 校正后 CI 收窄 4 倍，这与 cluster-robust 方法应当拓宽 CI 以反映组内相关性的预期完全相反。

论文主文（§3.1，Page 4）确实承认了 K≥20-30 的阈值要求，并引用了 Cameron et al. (2008) 和 Webb (2023)。但 Appendix E 仍以 "robustness check" 的名义报告了这一结果，且未附任何 caveat。这在读者看来是：论文明知方法在 K=11 时不可靠，仍将其结果呈现为补充验证——这是 false assurance，非 robustness。

R1 建议提供 ICC 估计合理。如果 ICC 接近 0（task types 间无相关），则 non-clustered bootstrap 已足够，cluster 方法无必要；如果 ICC 显著大于 0，则 K=11 的 cluster bootstrap 确实低估方差，需要 block bootstrap 或其他替代方法。

**补充**：我在自己的审查中也注意到论文的统计方法总体上是严谨的（四种独立检验交叉验证），但这个 Appendix E 的具体问题会削弱读者对整体统计质量的信心。建议直接移除 wild cluster bootstrap 的数值结果，仅保留对 clustering 结构的定性讨论，或明确降级为 "acknowledged limitation"（如 R1 建议）。

---

**[AGREE with qualification] R1-N2: Qwen3-4B episode-level 59.0% 与 "non-learnability" 结论的张力**

同意 R1 的核心判断：4B 的 59.0% ± 1.9% 结果确实与 §3.6 末句 "leaving no learnable signal for a step-level router to exploit" 的断言存在张力。即使 4B 的信号可能来自 episode-level 特征（如 task type 识别）而非 step-level routing signal，论文也不应使用 "fundamental non-learnability" 这样的绝对措辞。

**但需补充两点限定**：

(1) **Multiple comparison 的影响可能有限**。R1 指出 4 scales × 2 granularities = 8 tests，Bonferroni 阈值 p < 0.00625。但 4B 的 59.0% 与 50% baseline 的差为 9pp/1.9% SE ≈ z=4.7，对应 p < 0.001，即使 Bonferroni 校正后仍显著。所以 multiple comparison 可能不足以 dismiss 这个结果。

(2) **59% episode-level accuracy 的实际意义**。论文在 Appendix J（Table 10, Table 11）和 §3.6 中区分了 step-level 和 episode-level accuracy。Episode-level 59% 可能仅反映 router 学到了 task-type-level 的偏好（如 "death-prone tasks → always deterministic"），而非 step-level routing signal。这与论文的核心发现一致（routing signal 是 binary task-type feature，不是连续的 step-level signal）。但论文应当显式分析这一点，而非笼统声称 "non-learnability"。

**结论**：同意 R1 的建议——qualify 结论为 "在我们测试的架构和训练配置下，未发现可利用的 step-level routing signal"；单独分析 4B 的 per-task routing accuracy 以确认其是否仅捕获了 task-type 信号。

---

### Should-Fix

**[AGREE] R1-W1: Dose-response "plateau" 统计功效不足**

完全同意。Figure 3（Page 6）仅有 N=1,2,3,4,5 五个数据点，Wilson 95% CIs 在 N≥3 后大量重叠。"Plateau" 是一个关于函数形状的断言，需要远多于 5 个点才能成立。论文无法区分 "plateau" 与 "slow continuous decline"——正如 R1 所指出的。

建议的替代措辞 "no statistically detectable improvement beyond N=3" 更准确且更 defensible。

---

**[AGREE] R1-W2: Paraphrase augmentation ≠ data scaling**

同意。Appendix J 的 Table 11 使用 synonym substitution + template variation 作为 data augmentation，这不会产生新的 routing patterns——augmented samples 与原始 samples 共享相同的 episode outcomes 和 death/non-death 标签。在 DAF ≈ 90.4% 且所有 task types 的 routing label 几乎完全由 death asymmetry 决定的情况下，paraphrase augmentation 的 null result 是 expected null（正如 R1 所说），不构成 "data scaling doesn't help" 的有力证据。

真正的 data scaling test 需要：(a) 收集更多独立 episode pairs（不同 random seeds），或 (b) 从更多 task variants / environment configurations 中收集数据。论文应将此实验重新定位为 "text augmentation doesn't help"。

---

**[PARTIALLY AGREE] R1-W3: Mislabeling vs non-learnability 因果关系**

同意 R1 关于 Appendix B 循环论证的指出：用 episode-level labels 评估 step-level predictions 的合理性，而 episode-level labels 本身就是被质疑的对象，这确实存在逻辑循环。

**但论文确实提供了部分独立证据**：
- §3.1 报告 245 episodes 中 61.2% 是 ties（两种策略无差异），这是独立于 labeling 方法的 observation，说明大部分 episodes 没有可用信号。
- Table 3 的 per-task 分解显示 routing signal 集中在 death-prone tasks 中（Appendix C），这限制了可利用的有效训练样本量。
- Appendix B 的 label quality audit（13 页）报告了 anti-cherry-picking analysis，显示 excluded tasks 的 ΔDR (+38.2pp) > included tasks (+25.7pp)——排除选择不偏向 death-prone tasks。

但我同意这些证据不足以完全区分 (A) label noise 和 (B) non-learnability。论文应当更明确地呈现 "label noise 是 router 失败的可能原因之一"，而非仅倾向 non-learnability 解释。

---

**[AGREE] R1-W4: DAF 与 label fraction 的主文解释不足**

同意。DAF (90.4%) > label fraction (78.9%) 的差异来源于 death episodes 的 score magnitude 放大效应（§2.4 定义 DAF 为 score gap 分解而非 label count 分解），但主文对此只在 §2.4 给出公式定义，未用直觉性语言解释。这也呼应了我自己审查中指出的 Abstract 数字堆砌问题（我的 W1）——读者在面对两个不同的"核心数字"时不知道哪个是 headline metric。

建议在 §2.4 或 §3.1 添加 1-2 句直觉解释：例如 "label fraction 衡量 death asymmetry 影响了多少比例的 routing 决策，DAF 衡量这些决策对总体性能差距的贡献权重——因为 death episodes 的 score 差距更大，DAF > label fraction"。

---

**[AGREE] R1-W5: Per-task n=20 导致 power 不足，应标注为 exploratory**

同意。n=20 per task type（每种策略各 20 episodes）对 20pp effect 的 power 确实仅约 50%（two-sided t-test, α=0.05）。13/28 tasks 不显著（Table 3）可能是 power 不足而非 effect 不存在。

论文在 Appendix F 提供了 per-task death rate CIs，但主文 Table 3 未标注显著性或 CIs。建议：(a) 在 Table 3 中标注 per-task 显著性（如星号标注），(b) 在主文明确说明 per-task 分析为 exploratory，(c) 注明 aggregate-level 结论（K=11 task types, 245 episodes）不依赖 per-task 显著性。

---

### Questions

**Q1: ICC 估计**
[AGREE] 应当提供。ICC 可以直接量化 task-type 聚类效应的大小，帮助读者判断 non-clustered bootstrap CI [81.1%, 99.0%] 的可靠性。如果 ICC ≈ 0，则 non-clustered CI 已经足够；如果 ICC > 0.1，则 cluster 结构确实重要，但 K=11 的 wild cluster bootstrap 又不可靠——这种情况下论文需要采用 block bootstrap 或类似方法。

**Q2: 4B Bonferroni 校正**
[AGREE] 如前述，4B 的 z ≈ 4.7 可能在 Bonferroni 校正后仍显著（p < 0.001 < 0.00625）。但论文应当显式报告所有 8 个 test 的 corrected p-values，并对 4B 的 per-task routing accuracy 做分解——确认 59% 是否来自 task-type 识别而非 step-level signal。

**Q3: Label fraction P-invariance 的适用范围**
[AGREE] §2.4 定义 label fraction 为 penalty-independent（仅依赖 death indicator d(τ)），但 P-invariance 的精确条件是：penalty 改变不影响 death/non-death 的分类边界。如果 penalty 降到某个阈值以下（使 death episodes 不再总是负分、不再 dominate non-death episodes），P-invariance 就不成立。论文应明确 P-invariance 的适用范围——至少需要 penalty 大到 death episodes 的 score 始终低于 non-death episodes 的 score。

**Q4: Grounding ablation 修改环境 vs agent 学习**
[PARTIALLY AGREE] R1 提出了一个有价值的概念区分。Appendix O 的 grounding ablation 通过修改 system prompt（"use focus on only for final answers"）来减少 focus on 的使用频率，这确实是修改 agent behavior 而非测试 agent 是否能 *学习* 避免 death。但我认为这对论文的核心 claim 影响有限——论文的 claim 是 "death avoidance 是 dominant routing signal"（一个关于 signal composition 的诊断性 claim），而非 "agents can learn to avoid death"。Grounding ablation 显示减少 catastrophic action 可以降低 death rate（37% → 原始 42.9%），这与 death dominance 的诊断一致（减少 death → 减少 routing signal 的主要来源）。

但 R1 的关注方向是正确的：如果论文要声称 practical implications（如 "应该关注 death avoidance 而非 router 设计"），那么需要区分 environment-level 干预和 agent-level 学习。

**Q5: Pure-strategy 设计是否高估 death asymmetry**
[AGREE] 这是 R1 最有洞察力的问题。论文的 counterfactual 设计比较的是 *pure* internal vs *pure* deterministic 策略（§2.1, Eq. 1-2），而非混合 routing 策略。在 pure-strategy 设定下，internal 策略 *始终* 使用 chain-of-thought reasoning，*始终* 承受 hallucination 风险，因此 death asymmetry 被最大化。

在实际的 mixed routing 中，router 可能只在 high-risk steps 切换到 deterministic，这意味着：(a) internal 策略的 death rate 可能低于 pure-internal 的 42.9%（因为部分 high-risk steps 已被 route 到 deterministic），(b) 剩余的 routing 决策中，non-death factors（如 reasoning quality, task-specific difficulty）的相对权重可能增加。

因此 DAF=90.4% 可能是 death asymmetry 贡献的 *upper bound*。论文应在 Limitations 中明确讨论 pure-strategy assumption 对 DAF 估计的影响。

---

### Missing References

**[PARTIALLY AGREE] Kenton et al. (2021) alignment 角度**
同意可以补充，但这是 alignment 文献而非直接的 routing / adaptive computation 文献，优先级不高。论文的 Related Work §4 已经引用了 Safe RL 的核心文献（Altman 1999, Mihatsch & Neuneier 2002, García & Fernández 2015, CPO, CRPO, Moldovan 2012），并引用了 Ruan et al. (2024) 和 SafeRoute (2025) 作为 LLM agent safety 的代表。Kenton et al. 提供的是更高层次的 alignment framing，可以在 Discussion §5 作为一句话提及，但非必须。

**[AGREE] 近期 ScienceWorld routing 相关工作**
如果存在直接在 ScienceWorld 上做 routing/adaptive computation 的近期工作（2025-2026），论文确实应当引用。但我在审查中未发现论文遗漏了此类直接相关工作——ScienceWorld 上的 routing 工作目前较少。

---

### 对 R1 主要优势的回应

完全同意 R1 列出的六项优势。特别补充两点：
1. R1 指出的 "anti-cherry-picking analysis"（excluded tasks ΔDR > included tasks）确实是论文的亮点之一——我在自己的审查中也注意到 Appendix S 的 extended validation 增强了结论的 robustness。
2. R1 提到的 "负面结果诚实呈现" 也是我的共识——§3.6 的 router training 负结果和 MATH 的 null result 展示了论文的学术诚信度。

---

### R2 与 R1 的评分差异说明

我给出 Overall 3.0 (Findings) vs R1 的 3.5 (Borderline Conference)。差异主要来自 Excitement 评分（我 2.5 vs R1 3.0）。原因是我更看重 novelty ceiling 问题（我的 N2）：death dominance 在 ScienceWorld 的 −100 penalty 结构下近乎必然，框架 "发现" 的是奖励设计使然的结果。R1 对此问题的关注较少（未列为 Must-Fix），而我认为这是影响接收决定的核心问题。在 Soundness 上我们评分一致（3.5），在 Reproducibility 上也一致（4.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1894 · 2026-05-21T01:34:21.080576+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool call

_source line 1895 · 2026-05-21T01:34:21.081037+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1896 · 2026-05-21T01:34:21.131673+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T01:19:14.727111+00:00\", \"completed_at\": \"2026-05-21T01:23:08.758851+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主文本（Section 1-6 Conclusion）延伸至第 9 页。Section 6 Conclusion 起始于第 9 页顶部，超出 EMNLP 2026 的 8 页主文本限制（Limitations 和 Ethics Statement 不计入页数，但 Conclusion 计入）。按当前排版，主文本约 8.3 页，需压缩约 1/3 页的正文内容。有 desk reject 风险。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-2\", \"message\": \"前 2 页无视觉锚点（全为 Title/Abstract/Intro/Method 文字），首个 display item（Figure 1 pipeline 图）直到第 3 页才出现。对于实证分析型论文，在第 1-2 页放置 teaser figure 或核心结果缩略图能显著提升审稿人第一印象。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 7-9\", \"message\": \"连续 3 页纯文本（第 7 页 Related Work → 第 8 页 Discussion → 第 9 页 Conclusion/Limitations/Ethics），无任何 figure/table/equation 穿插。虽然这些章节传统上以文字为主，但连续 3 页的视觉单调会降低审稿人阅读节奏。考虑在 Discussion 中加入 1 个总结性 figure 或将 appendix 中某个关键表格提升到正文。\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"Figure 2（Per-task scatter plot）尺寸偏小，仅占左栏约 1/3 面积。轴标签和数据点标注字号较小，打印后可读性可能不足。建议适当放大或改用 figure*（全宽）。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（全宽 pipeline 图）作为首个 display item，有效传达了 counterfactual 分析框架的核心流程。Caption 自包含，可独立理解。设计合理。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3（Death rate vs. trial count）清晰展示 Retry 和 Reflection 的趋势线及 95% CI 误差带。但图幅偏紧凑，可适当增大以改善细节可读性。\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-6\", \"message\": \"Display items 集中在第 3-6 页（Figure 1, Figure 2, Table 1, Figure 3, Table 2），分布合理。主文本共 3 figures + 2 tables = 5 个 display items / 9 页 = 0.56/页，对分析型论文属可接受范围。\"}, {\"severity\": \"info\", \"dimension\": \"page 19\", \"message\": \"Figure 6（step-by-step action sequences）中 action 标签文字非常小，低于正文字号的 70%，放大查看才能辨识具体内容。作为 appendix 图可接受，但如提升到正文需增大字号。\"}, {\"severity\": \"info\", \"dimension\": \"pages 14-15, 18\", \"message\": \"Appendix 表格密度极高——第 14 页 3 
…[truncated 451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1897 · 2026-05-21T01:34:21.132136+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1898 · 2026-05-21T01:38:58.198512+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "## Round 20 Review Issues (fresh review, 2026-05-21)\n\n# =============================================\n# Resolved issues from prior rounds\n# =============================================\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n# =============================================\n# Open / in_progress issues (updated R20)\n# =============================================\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调 DAF 数值\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19 revised 强共识 MF1。Abstract+§3.1 仍以 DAF=90.4% 为 headline。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 fresh: R2 将 novelty ceiling 列为 N2-critical（DAF 是 P=100 的代数后果）。R1 部分 rebut（label fraction 78.9% 是 penalty-independent 经验发现）但同意 DAF 有代数放大成分。共识：78.9% 应为 headline，DAF 降级。\"\n  action_items:\n    - round: 20\n      action: \"Abstract/§3.1 以 78.9% label fraction 为唯一 headline；DAF 仅作补充；增加 DAF→1 when Δ_nd→0 的代数必然性讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: p=0.002 仅比最小可报告值大 4 倍。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 fresh 强共识 MF: Non-clustered CI=[81.1%,99.0%] vs wild cluster CI=[95.2%,99.5%]——cluster 方法反而收窄 4 倍，K=11 低估方差。Appendix E 以 robustness check 呈现构成 false assurance。R1 建议 ICC 估计 + block bootstrap；R2 建议移除数值结果或降级为 acknowledged limitation。\"\n  action_items:\n    - round: 20\n      action: \"移除 Appendix E 的 wild cluster bootstrap CI 数值或降级为 acknowledged limitation；提供 ICC 估计；non-clustered bootstrap 为主推断；补充 block bootstrap 或 randomization inference\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: Abstract 约 250 词含 10+ 百分比数字，concept 被淹没。R1 交叉后同意。\"\n  action_items:\n    - round: 20\n      action: \"Abstract concept-first 重组：核心概念先行，保留 3-4 个关键数字（78.9%、cross-model 一致性、50-episode pilot），其余移入 §1\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"缺 CMDP (Altman 1999)、risk-sensitive RL (Mihatsch & Neuneier 2002)。\"\n    - round: 20\n      reviewers: [2]\n      note: \"R20: §4 已补 Altman/Mihatsch。R2 新增缺 reward shaping (Ng 1999)、Confident Learning (Northcutt 2021)。R1 同意两者。\"\n  action_items:\n    - round: 20\n      action: \"补 Ng et al. 1999 (reward shaping) 和 Northcutt et al. 2021 (Confident Learning)；前者在 §4/§5 引用，后者在 §3.6 引用\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 分歧: R2 Excitement 2.5（death dominance 在 -100 penalty 下近乎必然）；R1 Excitement 3.0（label fraction 78.9%、intervention resistance、cross-architecture consistency 非平凡）。R1 部分 rebut R2-N2。Director 判断：方向共识（novelty 有限），程度分歧。\"\n  action_items:\n    - round: 20\n      action: \"§5 前置 non-triviality 讨论：明确哪些发现不可从 penalty structure 预测（Reflexion DAF>100%、72B DAF 增加、cross-architecture δ stability）；framework-centric 叙事缓解 finding-centric novelty concern\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: ScienceWorld=oracle simulator, MATH=code interpreter, ALFWorld=admissible actions。三种 deterministic 提供的 advantage 质性不同。R1 建议添加概念对照表。\"\n  action_items:\n    - round: 20\n      action: \"§2.1 或 §3.4 添加显式讨论+小表：Environment / Deterministic mode / Information advantage / Death mechanism\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R20: R1-W3 指出 mislabeling vs non-learnability 因果未厘清。Appendix B 用 episode labels 评估 step-level prediction 存在循环论证。R2 部分同意。\"\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: 与 R14-W1 合并。R2 Excitement 2.5, R1 Excitement 3.0。分歧在程度非方向。\"\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: Anti-cherry-picking analysis 被两位 Reviewer 列为主要优势（excluded ΔDR=+38.2pp > included +28.7pp）。仍为 scope limitation 但不再是 active concern。\"\n\n- id: \"R16-N3\"\n  summary: \"缺少 permadeath 环境 replication\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。\"\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。§3.3 已报告 72B 完整 decomposition。\"\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"连续多轮未提及。被 R20-N2 (4B contradiction) 部分取代。\"\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。Appendix L 引用 Figure 4 (signal_reversal.pdf)。\"\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R20: R2-W2 提 Contribution 1/2/3 独立价值不清，framework vs finding 摇摆。R1 rebut（三层递进关系清晰）。分歧。\"\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。\"\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"被 DAF framing 议题覆盖。\"\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R20: R1-Q3 要求澄清 P-invariance 适用范围。R2 交叉同意。需明确 P 需足够大使 death episodes score 始终低于 non-death。\"\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: R1-Q5 提出 pure-strategy 最大化了 death asymmetry，mixed routing 中 DAF 可能显著低于 90.4%。R2 称此为 R1 最有洞察力的问题，DAF=90.4% 是 upper bound。\"\n  action_items:\n    - round: 20\n      action: \"Limitations 增加 pure-strategy assumption 段落：DAF=90.4% 是 upper bound；mixed routing 中 death avoidance 贡献可能更低\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R17-W2\"\n  summary: \"Figure 2 caption / readability 问题\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R1 指出 Figure 2 点标签密集重叠；R2 指出 y 轴量纲不清。视觉审查也标注 Figure 2 尺寸偏小（warning）。\"\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: R1-W2 指出 paraphrase augmentation ≠ genuine data scaling（expected null 非 informative null）。R2 完全同意。应重定位为 'augmentation doesn't help'。\"\n  action_items:\n    - round: 20\n      action: \"§3.6 和 Appendix J 将 'data scaling' 改为 'text augmentation'；明确区分 paraphrase augmentation 和真实 data scaling\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R2 发现新 orphan entries (huang2022inner, selfcheckgpt-2023, wang2023voyager)。Webb 年份仍需核实。R1 交叉同意。\"\n  action_items:\n    - round: 20\n      action: \"清理 orphan bib entries；核实 Webb 2023 vs 2014 版本\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R1-N2 指出 4B router 59.0% 与 non-learnability 结论矛盾。R2 同意但补充 4B 可能仅捕获 task-type signal 而非 step-level signal。共识：qualify 'non-learnability' 结论。\"\n  action_items:\n    - round: 20\n      action: \"§3.6 qualify 结论为 '在测试配置下未发现 step-level signal'；分析 4B per-task routing accuracy；报告 multiple comparison corrected p-values\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R2-W4 指出 router 负结果基于单一架构系列（Qwen3 LoRA），'leaving no learnable signal' 过强。R1 交叉同意。\"\n  action_items:\n    - round: 20\n      action: \"弱化为 'current step-level routers fail to exploit the signal'；承认未测试其他架构\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: R1-W1 指出 dose-response 'plateau' 仅 5 个点、CIs 重叠、无法区分 plateau 与 slow decline。R2 完全同意。\"\n  action_items:\n    - round: 20\n      action: \"将 'plateau' 软化为 'no statistically detectable improvement beyond N=3'；报告 effect size detection threshold\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R20: R2 minor 指出 §4 仍使用 'modality'。全局替换可能遗漏。\"\n  action_items:\n    - round: 20\n      action: \"全文搜索 modality→computation mode 替换完整性\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未单独提及。§5 已有 Anatomy 段。\"\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。论文已有 Appendix Overview with hyperlinks（main.tex line 52-71）。视觉审查未标记。考虑 resolved。\"\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。§3.1 已改为 sole-signal labels 并定义。考虑 resolved。\"\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。Appendix N 已有 single annotator caveat。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R20: R2-W2 再提 Contribution 1/2/3 独立价值不清。R1 rebut（三层递进清晰）。分歧但非核心阻碍。\"\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R2-Q1 要求环境层面 penalty manipulation 实验。R1 交叉同意——可区分 'death dominance 来自 penalty structure' vs '来自 strategy behavior 固有不对称性'。\"\n\n- id: \"R19-W2\"\n  summary: \"Conclusion 过于简短——2 句话不匹配 long paper\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: Conclusion 约 3 行，但延伸至 page 9 导致页数超限。需同时解决长度和页数问题。\"\n\n- id: \"R19-W3\"\n  summary: \"Routing 的 practical value 本身存疑——always-det 近最优\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未单独提及。被 framework meta-diagnostic value 讨论覆盖。\"\n\n- id: \"R19-M1\"\n  summary: \"62% tie rate (150/245) 含义未充分讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。\"\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R20: Altman/Mihatsch 已补。新增缺 Ng et al. 1999 (reward shaping) 和 Northcutt et al. 2021 (Confident Learning)。\"\n  action_items:\n    - round: 20\n      action: \"补 Ng 1999 + Northcutt 2021\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R19-M3\"\n  summary: \"Table 1 weighting scheme（episode-weighted vs task-weighted）未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。\"\n\n# =============================================\n# Round 20 New Issues\n# =============================================\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"强共识。§5 Discussion 占满 page 8，§6 Conclusion 在 page 9 顶部约 15 行。超出约 0.3 页。视觉审查也标记为 critical。R1 建议压缩 §4/§5 冗余；R2 建议压缩 §5 至 ~1 页或部分内容移入 Appendix。\"\n  action_items:\n    - round: 20\n      action: \"压缩 §4 Related Work 或 §5 Discussion 以将 §6 Conclusion 收入 page 8 内\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1 首提为 MF，R2 交叉同意。4B = 59.0% ± 1.9% (p<0.05) 是唯一突破 chance 的模型。可能是 multiple comparison artifact (8 tests) 或 task-type classification。R2 补充 Bonferroni 后可能仍显著 (z≈4.7, p<0.001)。需 per-task routing accuracy 分析。\"\n  action_items:\n    - round: 20\n      action: \"报告 8 tests corrected p-values；分析 4B per-task routing accuracy；qualify §3.6 结论\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2 首提。R1 部分同意——论文已在 §3.2 self-defuse 了 r=0.97 作为独立证据的问题，但措辞仍过强。Task difficulty confound 部分被 within-task counterfactual 控制但 across-task 汇总可能 inflate。\"\n  action_items:\n    - round: 20\n      action: \"将 'structurally determined' 改为 'empirically dominated' 或 'the dominant empirical predictor'；如需保留 structural claim 需补 causal identification\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-W5 首提，R1 交叉同意。仅引 Natarajan 2013，缺 Confident Learning (Northcutt 2021)、DivideMix、Co-teaching 等。应讨论为什么 modern noisy-label methods 不适用（structured noise vs random noise）。\"\n  action_items:\n    - round: 20\n      action: \"§3.6 深化 noisy label 讨论：引用 Confident Learning；解释为何 structured noise（episode→step projection）超出 standard methods 假设\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-W5 首提，R2 同意。n=20 对 20pp effect power ~50%。主文 Table 3 无显著性标注。\"\n  action_items:\n    - round: 20\n      action: \"Table 3 caption 标注 per-task 为 exploratory；添加 per-task CIs 或显著性标注；注明 aggregate 结论不依赖 per-task 显著性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2 发现，R1 交叉确认。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "## Round 20 Review Issues (fresh review, 2026-05-21)\n\n# =============================================\n# Resolved issues from prior rounds\n# =============================================\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n# =============================================\n# Open / in_progress issues (updated R20)\n# =============================================\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调 DAF 数值\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19 revised 强共识 MF1。Abstract+§3.1 仍以 DAF=90.4% 为 headline。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 fresh: R2 将 novelty ceiling 列为 N2-critical（DAF 是 P=100 的代数后果）。R1 部分 rebut（label fraction 78.9% 是 penalty-independent 经验发现）但同意 DAF 有代数放大成分。共识：78.9% 应为 headline，DAF 降级。\"\n  action_items:\n    - round: 20\n      action: \"Abstract/§3.1 以 78.9% label fraction 为唯一 headline；DAF 仅作补充；增加 DAF→1 when Δ_nd→0 的代数必然性讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: p=0.002 仅比最小可报告值大 4 倍。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 fresh 强共识 MF: Non-clustered CI=[81.1%,99.0%] vs wild cluster CI=[95.2%,99.5%]——cluster 方法反而收窄 4 倍，K=11 低估方差。Appendix E 以 robustness check 呈现构成 false assurance。R1 建议 ICC 估计 + block bootstrap；R2 建议移除数值结果或降级为 acknowledged limitation。\"\n  action_items:\n    - round: 20\n      action: \"移除 Appendix E 的 wild cluster bootstrap CI 数值或降级为 acknowledged limitation；提供 ICC 估计；non-clustered bootstrap 为主推断；补充 block bootstrap 或 randomization inference\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: Abstract 约 250 词含 10+ 百分比数字，concept 被淹没。R1 交叉后同意。\"\n  action_items:\n    - round: 20\n      action: \"Abstract concept-first 重组：核心概念先行，保留 3-4 个关键数字（78.9%、cross-model 一致性、50-episode pilot），其余移入 §1\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"缺 CMDP (Altman 1999)、risk-sensitive RL (Mihatsch & Neuneier 2002)。\"\n    - round: 20\n      reviewers: [2]\n      note: \"R20: §4 已补 Altman/Mihatsch。R2 新增缺 reward shaping (Ng 1999)、Confident Learning (Northcutt 2021)。R1 同意两者。\"\n  action_items:\n    - round: 20\n      action: \"补 Ng et al. 1999 (reward shaping) 和 Northcutt et al. 2021 (Confident Learning)；前者在 §4/§5 引用，后者在 §3.6 引用\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 分歧: R2 Excitement 2.5（death dominance 在 -100 penalty 下近乎必然）；R1 Excitement 3.0（label fraction 78.9%、intervention resistance、cross-architecture consistency 非平凡）。R1 部分 rebut R2-N2。Director 判断：方向共识（novelty 有限），程度分歧。\"\n  action_items:\n    - round: 20\n      action: \"§5 前置 non-triviality 讨论：明确哪些发现不可从 penalty structure 预测（Reflexion DAF>100%、72B DAF 增加、cross-architecture δ stability）；framework-centric 叙事缓解 finding-centric novelty concern\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: ScienceWorld=oracle simulator, MATH=code interpreter, ALFWorld=admissible actions。三种 deterministic 提供的 advantage 质性不同。R1 建议添加概念对照表。\"\n  action_items:\n    - round: 20\n      action: \"§2.1 或 §3.4 添加显式讨论+小表：Environment / Deterministic mode / Information advantage / Death mechanism\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R20: R1-W3 指出 mislabeling vs non-learnability 因果未厘清。Appendix B 用 episode labels 评估 step-level prediction 存在循环论证。R2 部分同意。\"\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: 与 R14-W1 合并。R2 Excitement 2.5, R1 Excitement 3.0。分歧在程度非方向。\"\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: Anti-cherry-picking analysis 被两位 Reviewer 列为主要优势（excluded ΔDR=+38.2pp > included +28.7pp）。仍为 scope limitation 但不再是 active concern。\"\n\n- id: \"R16-N3\"\n  summary: \"缺少 permadeath 环境 replication\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。\"\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。§3.3 已报告 72B 完整 decomposition。\"\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"连续多轮未提及。被 R20-N2 (4B contradiction) 部分取代。\"\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。Appendix L 引用 Figure 4 (signal_reversal.pdf)。\"\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R20: R2-W2 提 Contribution 1/2/3 独立价值不清，framework vs finding 摇摆。R1 rebut（三层递进关系清晰）。分歧。\"\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。\"\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"被 DAF framing 议题覆盖。\"\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R20: R1-Q3 要求澄清 P-invariance 适用范围。R2 交叉同意。需明确 P 需足够大使 death episodes score 始终低于 non-death。\"\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: R1-Q5 提出 pure-strategy 最大化了 death asymmetry，mixed routing 中 DAF 可能显著低于 90.4%。R2 称此为 R1 最有洞察力的问题，DAF=90.4% 是 upper bound。\"\n  action_items:\n    - round: 20\n      action: \"Limitations 增加 pure-strategy assumption 段落：DAF=90.4% 是 upper bound；mixed routing 中 death avoidance 贡献可能更低\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R17-W2\"\n  summary: \"Figure 2 caption / readability 问题\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R1 指出 Figure 2 点标签密集重叠；R2 指出 y 轴量纲不清。视觉审查也标注 Figure 2 尺寸偏小（warning）。\"\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: R1-W2 指出 paraphrase augmentation ≠ genuine data scaling（expected null 非 informative null）。R2 完全同意。应重定位为 'augmentation doesn't help'。\"\n  action_items:\n    - round: 20\n      action: \"§3.6 和 Appendix J 将 'data scaling' 改为 'text augmentation'；明确区分 paraphrase augmentation 和真实 data scaling\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R2 发现新 orphan entries (huang2022inner, selfcheckgpt-2023, wang2023voyager)。Webb 年份仍需核实。R1 交叉同意。\"\n  action_items:\n    - round: 20\n      action: \"清理 orphan bib entries；核实 Webb 2023 vs 2014 版本\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R1-N2 指出 4B router 59.0% 与 non-learnability 结论矛盾。R2 同意但补充 4B 可能仅捕获 task-type signal 而非 step-level signal。共识：qualify 'non-learnability' 结论。\"\n  action_items:\n    - round: 20\n      action: \"§3.6 qualify 结论为 '在测试配置下未发现 step-level signal'；分析 4B per-task routing accuracy；报告 multiple comparison corrected p-values\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R2-W4 指出 router 负结果基于单一架构系列（Qwen3 LoRA），'leaving no learnable signal' 过强。R1 交叉同意。\"\n  action_items:\n    - round: 20\n      action: \"弱化为 'current step-level routers fail to exploit the signal'；承认未测试其他架构\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20 强共识: R1-W1 指出 dose-response 'plateau' 仅 5 个点、CIs 重叠、无法区分 plateau 与 slow decline。R2 完全同意。\"\n  action_items:\n    - round: 20\n      action: \"将 'plateau' 软化为 'no statistically detectable improvement beyond N=3'；报告 effect size detection threshold\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R20: R2 minor 指出 §4 仍使用 'modality'。全局替换可能遗漏。\"\n  action_items:\n    - round: 20\n      action: \"全文搜索 modality→computation mode 替换完整性\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未单独提及。§5 已有 Anatomy 段。\"\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。论文已有 Appendix Overview with hyperlinks（main.tex line 52-71）。视觉审查未标记。考虑 resolved。\"\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。§3.1 已改为 sole-signal labels 并定义。考虑 resolved。\"\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。Appendix N 已有 single annotator caveat。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R20: R2-W2 再提 Contribution 1/2/3 独立价值不清。R1 rebut（三层递进清晰）。分歧但非核心阻碍。\"\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R2-Q1 要求环境层面 penalty manipulation 实验。R1 交叉同意——可区分 'death dominance 来自 penalty structure' vs '来自 strategy behavior 固有不对称性'。\"\n\n- id: \"R19-W2\"\n  summary: \"Conclusion 过于简短——2 句话不匹配 long paper\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: Conclusion 约 3 行，但延伸至 page 9 导致页数超限。需同时解决长度和页数问题。\"\n\n- id: \"R19-W3\"\n  summary: \"Routing 的 practical value 本身存疑——always-det 近最优\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未单独提及。被 framework meta-diagnostic value 讨论覆盖。\"\n\n- id: \"R19-M1\"\n  summary: \"62% tie rate (150/245) 含义未充分讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。\"\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R20: Altman/Mihatsch 已补。新增缺 Ng et al. 1999 (reward shaping) 和 Northcutt et al. 2021 (Confident Learning)。\"\n  action_items:\n    - round: 20\n      action: \"补 Ng 1999 + Northcutt 2021\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R19-M3\"\n  summary: \"Table 1 weighting scheme（episode-weighted vs task-weighted）未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20 未提及。\"\n\n# =============================================\n# Round 20 New Issues\n# =============================================\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"强共识。§5 Discussion 占满 page 8，§6 Conclusion 在 page 9 顶部约 15 行。超出约 0.3 页。视觉审查也标记为 critical。R1 建议压缩 §4/§5 冗余；R2 建议压缩 §5 至 ~1 页或部分内容移入 Appendix。\"\n  action_items:\n    - round: 20\n      action: \"压缩 §4 Related Work 或 §5 Discussion 以将 §6 Conclusion 收入 page 8 内\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1 首提为 MF，R2 交叉同意。4B = 59.0% ± 1.9% (p<0.05) 是唯一突破 chance 的模型。可能是 multiple comparison artifact (8 tests) 或 task-type classification。R2 补充 Bonferroni 后可能仍显著 (z≈4.7, p<0.001)。需 per-task routing accuracy 分析。\"\n  action_items:\n    - round: 20\n      action: \"报告 8 tests corrected p-values；分析 4B per-task routing accuracy；qualify §3.6 结论\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2 首提。R1 部分同意——论文已在 §3.2 self-defuse 了 r=0.97 作为独立证据的问题，但措辞仍过强。Task difficulty confound 部分被 within-task counterfactual 控制但 across-task 汇总可能 inflate。\"\n  action_items:\n    - round: 20\n      action: \"将 'structurally determined' 改为 'empirically dominated' 或 'the dominant empirical predictor'；如需保留 structural claim 需补 causal identification\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-W5 首提，R1 交叉同意。仅引 Natarajan 2013，缺 Confident Learning (Northcutt 2021)、DivideMix、Co-teaching 等。应讨论为什么 modern noisy-label methods 不适用（structured noise vs random noise）。\"\n  action_items:\n    - round: 20\n      action: \"§3.6 深化 noisy label 讨论：引用 Confident Learning；解释为何 structured noise（episode→step projection）超出 standard methods 假设\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-W5 首提，R2 同意。n=20 对 20pp effect power ~50%。主文 Table 3 无显著性标注。\"\n  action_items:\n    - round: 20\n      action: \"Table 3 caption 标注 per-task 为 exploratory；添加 per-task CIs 或显著性标注；注明 aggregate 结论不依赖 per-task 显著性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2 发现，R1 交叉确认。\""
  }
}
```

</details>

---


### Tool result

_source line 1899 · 2026-05-21T01:38:58.300431+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 22947}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1900 · 2026-05-21T01:41:43.180813+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "report": "# Round 20 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR Long Paper, deadline 2026-05-25)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人 + 视觉审查 Agent\n- Reviewer 1: 方法严谨性 + 实验设计\n- Reviewer 2: 新颖性 + 完整性\n\n---\n\n## Summary\n\n本文提出一个 episode-level counterfactual 诊断框架，通过将 routing signal 分解为 death-avoidance 和 non-death 两个成分，诊断 modular LLM agent 中 routing 决策的驱动因素。应用于 ScienceWorld（11 task types，245 episodes，Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 来自 death asymmetry。跨模型验证（Llama-3.1-8B, Gemma-2-9B-it）和跨环境 boundary probes（MATH, ALFWorld）确认了框架的诊断能力。Router training 产生负结果，always-deterministic 匹配 96.3% 的 oracle 决策。\n\n---\n\n## Strengths\n\n1. **统计方法论严谨**：四种独立检验（non-clustered bootstrap, wild cluster bootstrap, permutation test, sign test）交叉验证。Episode-level bootstrap (B=10,000) 提供可靠 CIs。统计基础在 NLP 会议论文中属上乘。[共识]\n\n2. **Anti-cherry-picking analysis 堪称典范**：被排除的 19 个 task types 的 death asymmetry（mean ΔDR=+38.2pp）反而**强于**被纳入的 11 个 tasks（+28.7pp），有效排除 selection bias。Appendix S 扩展验证（n=20×5 tasks, DAF=0.991）进一步增强。[共识]\n\n3. **Cross-model replication 有说服力**：三个架构族（Qwen/GQA, Llama/GQA, Gemma/SWA）独立复现 DAF 88-90%（spread 2.2pp），CIs 重叠，方向一致性 100%。72B scaling 确认持续性。[共识]\n\n4. **负面结果诚实呈现**：Router training 负结果（§3.6）和 MATH null result（§3.4）未被掩盖，整合到框架诊断价值论证中。学术诚信度高。[共识]\n\n5. **Appendix 极为详尽**：19 个 Appendices (A-S)，覆盖 labeling audit、correlation robustness、seed robustness、data scaling、penalty sensitivity、failure modes、grounding ablation 等。Reproducibility checklist 完整。[共识]\n\n6. **可操作的 diagnostic pipeline**：Appendix R 三步决策框架（pilot→dominance check→decision）在 4/4 条件上 retrospective validation 正确。[共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 强共识] **正文超出 8 页限制**\n§5 Discussion 占满 page 8 双栏，§6 Conclusion 起始于 page 9（约 15 行）。正文超出约 0.3 页。EMNLP 2026 ARR 有 desk-reject 机制，Conclusion 属于正文。视觉审查也标记为 critical。\n→ 压缩 §4 Related Work 或 §5 Discussion，将 Conclusion 收入 page 8。\n\n**MF2** [critical, 强共识] **Wild cluster bootstrap CI 反常收窄，robustness check 提供 false assurance**\nNon-clustered bootstrap CI = [81.1%, 99.0%]（宽度 17.9pp），wild cluster bootstrap (K=11) CI = [95.2%, 99.5%]（宽度 4.3pp）——cluster 方法反而收窄 4 倍。K < 20-30 时 wild cluster bootstrap 低估方差（Cameron et al. 2008, Webb 2023），论文自己引用了这些文献并在主文承认了 K 不足，但 Appendix E 仍以 \"robustness check\" 呈现更紧的 CI。\n→ 移除 Appendix E CI 数值或降级为 acknowledged limitation；提供 ICC 估计；考虑 block bootstrap 替代。\n\n**MF3** [critical, 强共识] **4B router episode-level 59.0% 与 \"fundamental non-learnability\" 结论矛盾**\nQwen3-4B 是所有模型中唯一突破 chance 的（59.0% ± 1.9%, p < 0.05），但论文未做 multiple comparison correction（4 scales × 2 granularities = 8 tests），也未分析 4B 的 per-task routing accuracy 以确定其是否仅捕获 task-type 信号。§3.6 末句 \"leaving no learnable signal\" 与此矛盾。R2 补充：Bonferroni 校正后可能仍显著（z ≈ 4.7, p < 0.001），需正面讨论。\n→ 报告 corrected p-values；分析 4B per-task routing accuracy；qualify \"non-learnability\" 为 \"在测试配置下未发现 step-level signal\"。\n\n**MF4** [critical, R2 提出 / R1 部分同意] **\"Structurally determined\" overclaim**\n\"Structurally determined\" 在学术语境暗示因果机制，但支撑证据为 r=0.97 correlation。Task difficulty confound 未完全排除（within-task counterfactual 控制了单任务内差异，但 across-task 汇总中 death rate 和 difficulty 可能 co-vary）。论文在 §3.2 已 self-defuse r=0.97 为代数后果，但 §5 仍使用 \"structurally determined\"。\n→ 改为 \"empirically dominated\" 或 \"the dominant empirical predictor\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, 强共识] **Abstract 数字堆砌**\n约 250 词含 10+ 百分比数字，核心概念（counterfactual diagnostic, death avoidance routing）被数字淹没。\n→ Concept-first 重组：保留 3-4 个关键数字（78.9%, cross-model 一致性, 50-episode pilot），其余移入 §1。\n\n**SF2** [warning, 强共识] **DAF vs label fraction 关系解释不够直观**\nDAF (90.4%) > label fraction (78.9%) 的差异来自 death episodes 的 score magnitude 放大（P=100 >> 典型 non-death gap ~29）。读者可能误以为两者是独立证据。\n→ §2.4 或 §3.1 添加 1-2 句直觉解释。\n\n**SF3** [warning, 强共识] **\"Deterministic\" 在三个环境中含义不同，缺显式讨论**\nScienceWorld = oracle simulator；MATH = code interpreter；ALFWorld = admissible-action enumeration。三种 \"deterministic\" 的 information advantage 质性完全不同。\n→ §2.1 或 §3.4 添加概念对照表。\n\n**SF4** [warning, 强共识] **Dose-response \"plateau\" 结论统计功效不足**\n仅 5 个数据点 (N=1-5)，Wilson CIs 大量重叠。\"Plateau\" 与 \"持续但缓慢下降\" 在此 sample size 下无法区分。\n→ 软化为 \"no statistically detectable improvement beyond N=3\"。\n\n**SF5** [warning, 强共识] **Paraphrase augmentation ≠ genuine data scaling**\nData scaling ablation (25%-800%) 使用 synonym substitution + template variation，不产生新 routing patterns。是 expected null 非 informative null。\n→ 重定位为 \"text augmentation doesn't help\"，明确区分于真实 data scaling。\n\n**SF6** [warning, 强共识] **Noisy label learning 讨论不充分**\n仅引用 Natarajan 2013，缺 Confident Learning (Northcutt 2021)、DivideMix 等后续方法。未讨论为何 modern noisy-label methods 不适用。\n→ 深化讨论或补引用。\n\n**SF7** [warning, 强共识] **Router \"leaving no learnable signal\" 措辞过强**\n负结果仅基于 Qwen3 LoRA + generative router。未测试 lightweight classifier、feature-based router 等其他架构。\n→ 弱化为 \"current step-level routers fail to exploit the signal\"。\n\n**SF8** [warning, 强共识] **Pure-strategy 设计可能高估 death asymmetry（DAF=90.4% 是 upper bound）**\nPure-strategy 比较中 internal 策略始终承受 hallucination 风险。Mixed routing 中 router 可在 high-risk steps 切换到 deterministic，实际 death avoidance 贡献可能显著更低。\n→ Limitations 明确 pure-strategy assumption 及其对 DAF 估计的 upward bias。\n\n**SF9** [warning, 强共识] **Per-task n=20 导致 13/28 tasks 不显著，应标注为 exploratory**\nn=20 对 20pp effect 的 power 仅 ~50%。主文 Table 3 无显著性标注或 CIs。\n→ 标注 per-task 分析为 exploratory，添加 CIs。\n\n### Minor\n\n- Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager [R2, R1 确认]\n- Webb (2023) 年份可能为 2014 working paper [R1+R2]\n- §4 Related Work 仍使用 \"modality\"，与 §2 \"computation mode\" 不一致 [R2]\n- Figure 2 尺寸偏小、点标签重叠 [R1+视觉审查]\n- Appendix R 的 ~50 episodes / ~2 GPU-hours 是 ScienceWorld-specific 估计 [R2]\n- Table 2 caption seed 说明不够清晰 [R1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **页数超限 desk reject 风险**：两位 Reviewer + 视觉审查三方确认。[MF1]\n2. **Cluster bootstrap CI 收窄 = false assurance**：R1 首提，R2 完全同意。[MF2]\n3. **4B router 结果需正面讨论**：R1 首提，R2 同意（补充 Bonferroni 后可能仍显著）。[MF3]\n4. **\"Structurally determined\" 措辞过强**：R2 首提，R1 部分同意（counterfactual 设计部分控制 confound 但措辞仍需调整）。[MF4]\n5. **DAF 代数放大成分**：两位 Reviewer 均指出 DAF 随 P 单调递增是代数后果，label fraction 78.9% 应为 headline。[SF2]\n6. **Pure-strategy = DAF upper bound**：R1 提出，R2 称为\"最有洞察力的问题\"。[SF8]\n7. **统计分析整体严谨**：两位均列为主要优势。\n8. **Anti-cherry-picking 堪称典范**：两位均列为主要优势。\n9. **三模型 replication 有说服力**：两位均列为主要优势。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**Novelty / Excitement 评估**（核心分歧）\n- **R2 (Excitement 2.5/5)**：Death dominance 在 ScienceWorld −100 penalty 下是 \"数学上的近似必然\"。72B DAF 增加恰支持 \"penalty structure 不变→dominance 不变\"。框架结论=\"这个环境不需要 routing\"，贡献范围有限。\n- **R1 (Excitement 3.0/5)**：部分 rebut——label fraction 78.9% 是 penalty-independent 经验发现；72B scaling 本可多样化 routing signal（但没有）；Reflexion DAF>100%（non-death regression）不可从 penalty structure 预测；三模型 DAF 88-90% 收敛是非平凡的 cross-architecture consistency。框架在 ALFWorld/MATH 上的 generality 有独立价值。\n\n**Director 裁决**：方向共识（novelty 有限），程度分歧。R1 的 partial rebuttal 有理（label fraction、intervention resistance、cross-architecture consistency 非平凡），但 R2 的核心论点成立（核心 DAF 发现受环境设计制约，框架概念上 straightforward）。最终 Excitement 取 2.75，不足以支撑 Conference 接收。\n\n**Contribution 1/2/3 独立性**\n- R2 认为三个 contribution 非独立（C2/C3 是 C1 的应用结果），framework vs finding 摇摆。\n- R1 认为三层递进关系清晰。\n- Director：分歧非核心阻碍，不影响整体评估。\n\n---\n\n## Questions for Authors\n\n1. **Cluster bootstrap ICC**：能否提供 intra-class correlation 估计以判断 task-type 聚类效应大小？[R1 首提, R2 同意]\n2. **4B per-task routing accuracy**：4B 的 59.0% 是否来自 task-type 识别而非 step-level signal？能否做 per-task 分解？[R1 首提, R2 同意]\n3. **Label fraction P-invariance 适用范围**：当 P→0 使 death episodes score 不再始终低于 non-death episodes 时，P-invariance 不成立。精确条件是什么？[R1 首提, R2 同意]\n4. **环境层面 penalty manipulation**：Appendix K 仅改变 DAF 计算中的 P，未在 ScienceWorld 中实际改变 death penalty。如果 P 从 100 降至 10，agent behavior 可能改变，label fraction 是否仍 ~78.9%？[R2 首提, R1 同意]\n5. **Pure-strategy vs mixed-strategy gap**：在 mixed routing 中，DAF 的实际值是多少？pure-strategy 设计是否系统性高估了 death avoidance 的贡献？[R1 首提, R2 强烈同意]\n6. **Reflexion DAF > 100% 机制**：Δ_nd = −0.47 说明 Reflexion 在 non-death episodes 上引入了 regression。这是 overcompensation 还是其他原因？对 Reflexion 可靠性有何启示？[R2 首提, R1 同意]\n7. **Prospective validation**：Appendix R 的 decision framework 仅做了 retrospective validation（4/4 conditions）。是否有可能在新环境上做 prospective validation？[R2 首提, R1 同意]\n\n---\n\n## Missing References\n\n1. **Ng, Harada & Russell (1999)** — \"Policy invariance under reward transformations\"：Death dominance 本质上是 reward shaping 问题，应引用。[R2 首提, R1 同意]\n2. **Northcutt, Jiang & Chuang (2021)** — \"Confident Learning\"：§3.6 讨论 noisy label 但仅引 Natarajan 2013，缺 modern methods。[R2 首提, R1 同意]\n3. **Webb (2023) 年份核实**：需确认是 working paper 还是 journal publication。[R1+R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（2026-05-21 01:19→01:23，耗时 ~4 min）\n\n**Findings**:\n\n| Severity | Finding |\n|----------|---------|\n| critical | 主文本延伸至第 9 页（§6 Conclusion 在 page 9 顶部），超出 EMNLP 8 页限制约 0.3 页 |\n| warning | 前 2 页无视觉锚点，首个 display item (Figure 1) 直到 page 3 才出现 |\n| warning | Pages 7-9 连续 3 页纯文本（Related Work→Discussion→Conclusion/Limitations），无 figure/table 穿插 |\n| warning | Figure 2 尺寸偏小，打印后可读性不足 |\n| info (×7) | Figure 1 pipeline 图设计合理；Figure 3 dose-response 清晰；Display items 集中在 pages 3-6 分布合理（0.56/页）；booktabs 表格排版专业；无 [?] 未解析引用；Margin 无溢出；行号存在 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings**\n\n| 维度 | R1 | R2 | 加权评估 |\n|------|------|------|---------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.75 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | 3.0 |\n\n**置信度**: 4/5（两位 Reviewer 均报告 4/5）\n\n**评分理由**：\n- **方法论扎实**（Soundness 3.5）：框架设计有 principled justification，统计分析全面，cross-model replication 有说服力。但 cluster bootstrap CI 收窄、4B router 结果未解释、\"structurally determined\" overclaim 需要修正。\n- **Novelty 受限**（Excitement 2.75）：核心发现（death dominance）受环境 penalty structure 制约——虽然 label fraction 78.9% 和 intervention resistance 是非平凡的经验发现，但框架概念上较为 straightforward，跨环境仅为 boundary probes 而非深度分析。\n- **Reproducibility 优秀**（4.0）：Algorithm 1 完整，Appendix 详尽，承诺开源。\n- **Findings 而非 Conference**：工作完整、统计严谨，但 novelty 和 breadth 不足以支撑主会议接收。若作者能 (a) 解决页数超限, (b) 修正统计呈现（cluster bootstrap, 4B router）, (c) 采用 framework-centric 叙事降低对 finding novelty 的依赖, (d) 补充至少一个中等 death regime 环境的深度分析，评分可上调至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 列表中 C2 和 C3 与 C1 的递进关系需更清晰——C1 是方法论，C2 是应用，C3 是 robustness check。当前呈现方式让 C2/C3 看起来像独立贡献。[R2-W2，R1 rebut]\n\n### §2 Method\n- §2.4 DAF 定义清晰，但 DAF > label fraction 的原因（score magnitude 放大）需直觉解释。[SF2]\n- P-invariance 声明需明确适用条件（P 需足够大使 death episodes score 始终低于 non-death）。[R1-Q3]\n- \"Scope of episode-level analysis\" 段落增强了方法论完整性。[正面]\n\n### §3 Experiments\n- §3.1: 78.9% label fraction 作为 headline metric 是正确选择，但应前移至段落首句（当前首句是 \"Of the 95 non-tie routing labels\"）。[SF2]\n- §3.1: Per-task correlation r=0.97 已正确标注为 \"mathematical consequence\"——这是诚实的自我定位。[正面]\n- §3.3: Reflexion DAF>100% 是有趣发现但 overcompensation 机制讨论较薄。[R2-Q4]\n- §3.4: MATH/ALFWorld 定位为 \"boundary probes\" 恰当，但 \"deterministic\" 含义差异需显式讨论。[SF3]\n- §3.6: \"Router Training: A Negative Result\" 标题诚实。但 4B 59.0% 结果与 \"no learnable signal\" 矛盾需正面讨论。[MF3]\n\n### §4 Related Work\n- Safe RL 段落已补 Altman (1999) 和 Mihatsch (2002)。[改善]\n- 缺 reward shaping (Ng 1999) 和 Confident Learning (Northcutt 2021)。[Missing References]\n- \"modality\" 术语遗留，应统一为 \"computation mode\"。[Minor]\n\n### §5 Discussion\n- \"Why the router fails\" 和 \"Practical value as meta-diagnostic\" 结构清晰。[正面]\n- \"Structurally determined\" 需改为 \"empirically dominated\"。[MF4]\n- Non-triviality 讨论可以更前置，直接回应 \"obvious in hindsight\" 的预期批评。[R14-W1]\n\n### §6 Conclusion\n- 仅 3 行，比 Round 19 略有扩展但仍偏短。更根本的问题是它导致了页数超限。[MF1]\n\n### Limitations\n- 三段结构（Environmental scope / Methodological constraints / Statistical limitations）清晰全面。[正面]\n- 缺 pure-strategy assumption 对 DAF 估计的 upward bias 讨论。[SF8]\n\n### Appendix\n- A-S 共 19 个 Appendix，覆盖度极高。Appendix Overview with hyperlinks 增强导航。[正面]\n- Appendix E (wild cluster bootstrap): CI 反常收窄需处理。[MF2]\n- Appendix P (capacity scaling): 4B 结果需更多分析。[MF3]\n- Appendix R (decision framework): 仅 retrospective validation，应标注。[Q7]",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "simgate-modular-routing",
    "report": "# Round 20 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR Long Paper, deadline 2026-05-25)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人 + 视觉审查 Agent\n- Reviewer 1: 方法严谨性 + 实验设计\n- Reviewer 2: 新颖性 + 完整性\n\n---\n\n## Summary\n\n本文提出一个 episode-level counterfactual 诊断框架，通过将 routing signal 分解为 death-avoidance 和 non-death 两个成分，诊断 modular LLM agent 中 routing 决策的驱动因素。应用于 ScienceWorld（11 task types，245 episodes，Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 来自 death asymmetry。跨模型验证（Llama-3.1-8B, Gemma-2-9B-it）和跨环境 boundary probes（MATH, ALFWorld）确认了框架的诊断能力。Router training 产生负结果，always-deterministic 匹配 96.3% 的 oracle 决策。\n\n---\n\n## Strengths\n\n1. **统计方法论严谨**：四种独立检验（non-clustered bootstrap, wild cluster bootstrap, permutation test, sign test）交叉验证。Episode-level bootstrap (B=10,000) 提供可靠 CIs。统计基础在 NLP 会议论文中属上乘。[共识]\n\n2. **Anti-cherry-picking analysis 堪称典范**：被排除的 19 个 task types 的 death asymmetry（mean ΔDR=+38.2pp）反而**强于**被纳入的 11 个 tasks（+28.7pp），有效排除 selection bias。Appendix S 扩展验证（n=20×5 tasks, DAF=0.991）进一步增强。[共识]\n\n3. **Cross-model replication 有说服力**：三个架构族（Qwen/GQA, Llama/GQA, Gemma/SWA）独立复现 DAF 88-90%（spread 2.2pp），CIs 重叠，方向一致性 100%。72B scaling 确认持续性。[共识]\n\n4. **负面结果诚实呈现**：Router training 负结果（§3.6）和 MATH null result（§3.4）未被掩盖，整合到框架诊断价值论证中。学术诚信度高。[共识]\n\n5. **Appendix 极为详尽**：19 个 Appendices (A-S)，覆盖 labeling audit、correlation robustness、seed robustness、data scaling、penalty sensitivity、failure modes、grounding ablation 等。Reproducibility checklist 完整。[共识]\n\n6. **可操作的 diagnostic pipeline**：Appendix R 三步决策框架（pilot→dominance check→decision）在 4/4 条件上 retrospective validation 正确。[共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 强共识] **正文超出 8 页限制**\n§5 Discussion 占满 page 8 双栏，§6 Conclusion 起始于 page 9（约 15 行）。正文超出约 0.3 页。EMNLP 2026 ARR 有 desk-reject 机制，Conclusion 属于正文。视觉审查也标记为 critical。\n→ 压缩 §4 Related Work 或 §5 Discussion，将 Conclusion 收入 page 8。\n\n**MF2** [critical, 强共识] **Wild cluster bootstrap CI 反常收窄，robustness check 提供 false assurance**\nNon-clustered bootstrap CI = [81.1%, 99.0%]（宽度 17.9pp），wild cluster bootstrap (K=11) CI = [95.2%, 99.5%]（宽度 4.3pp）——cluster 方法反而收窄 4 倍。K < 20-30 时 wild cluster bootstrap 低估方差（Cameron et al. 2008, Webb 2023），论文自己引用了这些文献并在主文承认了 K 不足，但 Appendix E 仍以 \"robustness check\" 呈现更紧的 CI。\n→ 移除 Appendix E CI 数值或降级为 acknowledged limitation；提供 ICC 估计；考虑 block bootstrap 替代。\n\n**MF3** [critical, 强共识] **4B router episode-level 59.0% 与 \"fundamental non-learnability\" 结论矛盾**\nQwen3-4B 是所有模型中唯一突破 chance 的（59.0% ± 1.9%, p < 0.05），但论文未做 multiple comparison correction（4 scales × 2 granularities = 8 tests），也未分析 4B 的 per-task routing accuracy 以确定其是否仅捕获 task-type 信号。§3.6 末句 \"leaving no learnable signal\" 与此矛盾。R2 补充：Bonferroni 校正后可能仍显著（z ≈ 4.7, p < 0.001），需正面讨论。\n→ 报告 corrected p-values；分析 4B per-task routing accuracy；qualify \"non-learnability\" 为 \"在测试配置下未发现 step-level signal\"。\n\n**MF4** [critical, R2 提出 / R1 部分同意] **\"Structurally determined\" overclaim**\n\"Structurally determined\" 在学术语境暗示因果机制，但支撑证据为 r=0.97 correlation。Task difficulty confound 未完全排除（within-task counterfactual 控制了单任务内差异，但 across-task 汇总中 death rate 和 difficulty 可能 co-vary）。论文在 §3.2 已 self-defuse r=0.97 为代数后果，但 §5 仍使用 \"structurally determined\"。\n→ 改为 \"empirically dominated\" 或 \"the dominant empirical predictor\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, 强共识] **Abstract 数字堆砌**\n约 250 词含 10+ 百分比数字，核心概念（counterfactual diagnostic, death avoidance routing）被数字淹没。\n→ Concept-first 重组：保留 3-4 个关键数字（78.9%, cross-model 一致性, 50-episode pilot），其余移入 §1。\n\n**SF2** [warning, 强共识] **DAF vs label fraction 关系解释不够直观**\nDAF (90.4%) > label fraction (78.9%) 的差异来自 death episodes 的 score magnitude 放大（P=100 >> 典型 non-death gap ~29）。读者可能误以为两者是独立证据。\n→ §2.4 或 §3.1 添加 1-2 句直觉解释。\n\n**SF3** [warning, 强共识] **\"Deterministic\" 在三个环境中含义不同，缺显式讨论**\nScienceWorld = oracle simulator；MATH = code interpreter；ALFWorld = admissible-action enumeration。三种 \"deterministic\" 的 information advantage 质性完全不同。\n→ §2.1 或 §3.4 添加概念对照表。\n\n**SF4** [warning, 强共识] **Dose-response \"plateau\" 结论统计功效不足**\n仅 5 个数据点 (N=1-5)，Wilson CIs 大量重叠。\"Plateau\" 与 \"持续但缓慢下降\" 在此 sample size 下无法区分。\n→ 软化为 \"no statistically detectable improvement beyond N=3\"。\n\n**SF5** [warning, 强共识] **Paraphrase augmentation ≠ genuine data scaling**\nData scaling ablation (25%-800%) 使用 synonym substitution + template variation，不产生新 routing patterns。是 expected null 非 informative null。\n→ 重定位为 \"text augmentation doesn't help\"，明确区分于真实 data scaling。\n\n**SF6** [warning, 强共识] **Noisy label learning 讨论不充分**\n仅引用 Natarajan 2013，缺 Confident Learning (Northcutt 2021)、DivideMix 等后续方法。未讨论为何 modern noisy-label methods 不适用。\n→ 深化讨论或补引用。\n\n**SF7** [warning, 强共识] **Router \"leaving no learnable signal\" 措辞过强**\n负结果仅基于 Qwen3 LoRA + generative router。未测试 lightweight classifier、feature-based router 等其他架构。\n→ 弱化为 \"current step-level routers fail to exploit the signal\"。\n\n**SF8** [warning, 强共识] **Pure-strategy 设计可能高估 death asymmetry（DAF=90.4% 是 upper bound）**\nPure-strategy 比较中 internal 策略始终承受 hallucination 风险。Mixed routing 中 router 可在 high-risk steps 切换到 deterministic，实际 death avoidance 贡献可能显著更低。\n→ Limitations 明确 pure-strategy assumption 及其对 DAF 估计的 upward bias。\n\n**SF9** [warning, 强共识] **Per-task n=20 导致 13/28 tasks 不显著，应标注为 exploratory**\nn=20 对 20pp effect 的 power 仅 ~50%。主文 Table 3 无显著性标注或 CIs。\n→ 标注 per-task 分析为 exploratory，添加 CIs。\n\n### Minor\n\n- Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager [R2, R1 确认]\n- Webb (2023) 年份可能为 2014 working paper [R1+R2]\n- §4 Related Work 仍使用 \"modality\"，与 §2 \"computation mode\" 不一致 [R2]\n- Figure 2 尺寸偏小、点标签重叠 [R1+视觉审查]\n- Appendix R 的 ~50 episodes / ~2 GPU-hours 是 ScienceWorld-specific 估计 [R2]\n- Table 2 caption seed 说明不够清晰 [R1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **页数超限 desk reject 风险**：两位 Reviewer + 视觉审查三方确认。[MF1]\n2. **Cluster bootstrap CI 收窄 = false assurance**：R1 首提，R2 完全同意。[MF2]\n3. **4B router 结果需正面讨论**：R1 首提，R2 同意（补充 Bonferroni 后可能仍显著）。[MF3]\n4. **\"Structurally determined\" 措辞过强**：R2 首提，R1 部分同意（counterfactual 设计部分控制 confound 但措辞仍需调整）。[MF4]\n5. **DAF 代数放大成分**：两位 Reviewer 均指出 DAF 随 P 单调递增是代数后果，label fraction 78.9% 应为 headline。[SF2]\n6. **Pure-strategy = DAF upper bound**：R1 提出，R2 称为\"最有洞察力的问题\"。[SF8]\n7. **统计分析整体严谨**：两位均列为主要优势。\n8. **Anti-cherry-picking 堪称典范**：两位均列为主要优势。\n9. **三模型 replication 有说服力**：两位均列为主要优势。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**Novelty / Excitement 评估**（核心分歧）\n- **R2 (Excitement 2.5/5)**：Death dominance 在 ScienceWorld −100 penalty 下是 \"数学上的近似必然\"。72B DAF 增加恰支持 \"penalty structure 不变→dominance 不变\"。框架结论=\"这个环境不需要 routing\"，贡献范围有限。\n- **R1 (Excitement 3.0/5)**：部分 rebut——label fraction 78.9% 是 penalty-independent 经验发现；72B scaling 本可多样化 routing signal（但没有）；Reflexion DAF>100%（non-death regression）不可从 penalty structure 预测；三模型 DAF 88-90% 收敛是非平凡的 cross-architecture consistency。框架在 ALFWorld/MATH 上的 generality 有独立价值。\n\n**Director 裁决**：方向共识（novelty 有限），程度分歧。R1 的 partial rebuttal 有理（label fraction、intervention resistance、cross-architecture consistency 非平凡），但 R2 的核心论点成立（核心 DAF 发现受环境设计制约，框架概念上 straightforward）。最终 Excitement 取 2.75，不足以支撑 Conference 接收。\n\n**Contribution 1/2/3 独立性**\n- R2 认为三个 contribution 非独立（C2/C3 是 C1 的应用结果），framework vs finding 摇摆。\n- R1 认为三层递进关系清晰。\n- Director：分歧非核心阻碍，不影响整体评估。\n\n---\n\n## Questions for Authors\n\n1. **Cluster bootstrap ICC**：能否提供 intra-class correlation 估计以判断 task-type 聚类效应大小？[R1 首提, R2 同意]\n2. **4B per-task routing accuracy**：4B 的 59.0% 是否来自 task-type 识别而非 step-level signal？能否做 per-task 分解？[R1 首提, R2 同意]\n3. **Label fraction P-invariance 适用范围**：当 P→0 使 death episodes score 不再始终低于 non-death episodes 时，P-invariance 不成立。精确条件是什么？[R1 首提, R2 同意]\n4. **环境层面 penalty manipulation**：Appendix K 仅改变 DAF 计算中的 P，未在 ScienceWorld 中实际改变 death penalty。如果 P 从 100 降至 10，agent behavior 可能改变，label fraction 是否仍 ~78.9%？[R2 首提, R1 同意]\n5. **Pure-strategy vs mixed-strategy gap**：在 mixed routing 中，DAF 的实际值是多少？pure-strategy 设计是否系统性高估了 death avoidance 的贡献？[R1 首提, R2 强烈同意]\n6. **Reflexion DAF > 100% 机制**：Δ_nd = −0.47 说明 Reflexion 在 non-death episodes 上引入了 regression。这是 overcompensation 还是其他原因？对 Reflexion 可靠性有何启示？[R2 首提, R1 同意]\n7. **Prospective validation**：Appendix R 的 decision framework 仅做了 retrospective validation（4/4 conditions）。是否有可能在新环境上做 prospective validation？[R2 首提, R1 同意]\n\n---\n\n## Missing References\n\n1. **Ng, Harada & Russell (1999)** — \"Policy invariance under reward transformations\"：Death dominance 本质上是 reward shaping 问题，应引用。[R2 首提, R1 同意]\n2. **Northcutt, Jiang & Chuang (2021)** — \"Confident Learning\"：§3.6 讨论 noisy label 但仅引 Natarajan 2013，缺 modern methods。[R2 首提, R1 同意]\n3. **Webb (2023) 年份核实**：需确认是 working paper 还是 journal publication。[R1+R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（2026-05-21 01:19→01:23，耗时 ~4 min）\n\n**Findings**:\n\n| Severity | Finding |\n|----------|---------|\n| critical | 主文本延伸至第 9 页（§6 Conclusion 在 page 9 顶部），超出 EMNLP 8 页限制约 0.3 页 |\n| warning | 前 2 页无视觉锚点，首个 display item (Figure 1) 直到 page 3 才出现 |\n| warning | Pages 7-9 连续 3 页纯文本（Related Work→Discussion→Conclusion/Limitations），无 figure/table 穿插 |\n| warning | Figure 2 尺寸偏小，打印后可读性不足 |\n| info (×7) | Figure 1 pipeline 图设计合理；Figure 3 dose-response 清晰；Display items 集中在 pages 3-6 分布合理（0.56/页）；booktabs 表格排版专业；无 [?] 未解析引用；Margin 无溢出；行号存在 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings**\n\n| 维度 | R1 | R2 | 加权评估 |\n|------|------|------|---------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.75 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | 3.0 |\n\n**置信度**: 4/5（两位 Reviewer 均报告 4/5）\n\n**评分理由**：\n- **方法论扎实**（Soundness 3.5）：框架设计有 principled justification，统计分析全面，cross-model replication 有说服力。但 cluster bootstrap CI 收窄、4B router 结果未解释、\"structurally determined\" overclaim 需要修正。\n- **Novelty 受限**（Excitement 2.75）：核心发现（death dominance）受环境 penalty structure 制约——虽然 label fraction 78.9% 和 intervention resistance 是非平凡的经验发现，但框架概念上较为 straightforward，跨环境仅为 boundary probes 而非深度分析。\n- **Reproducibility 优秀**（4.0）：Algorithm 1 完整，Appendix 详尽，承诺开源。\n- **Findings 而非 Conference**：工作完整、统计严谨，但 novelty 和 breadth 不足以支撑主会议接收。若作者能 (a) 解决页数超限, (b) 修正统计呈现（cluster bootstrap, 4B router）, (c) 采用 framework-centric 叙事降低对 finding novelty 的依赖, (d) 补充至少一个中等 death regime 环境的深度分析，评分可上调至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 列表中 C2 和 C3 与 C1 的递进关系需更清晰——C1 是方法论，C2 是应用，C3 是 robustness check。当前呈现方式让 C2/C3 看起来像独立贡献。[R2-W2，R1 rebut]\n\n### §2 Method\n- §2.4 DAF 定义清晰，但 DAF > label fraction 的原因（score magnitude 放大）需直觉解释。[SF2]\n- P-invariance 声明需明确适用条件（P 需足够大使 death episodes score 始终低于 non-death）。[R1-Q3]\n- \"Scope of episode-level analysis\" 段落增强了方法论完整性。[正面]\n\n### §3 Experiments\n- §3.1: 78.9% label fraction 作为 headline metric 是正确选择，但应前移至段落首句（当前首句是 \"Of the 95 non-tie routing labels\"）。[SF2]\n- §3.1: Per-task correlation r=0.97 已正确标注为 \"mathematical consequence\"——这是诚实的自我定位。[正面]\n- §3.3: Reflexion DAF>100% 是有趣发现但 overcompensation 机制讨论较薄。[R2-Q4]\n- §3.4: MATH/ALFWorld 定位为 \"boundary probes\" 恰当，但 \"deterministic\" 含义差异需显式讨论。[SF3]\n- §3.6: \"Router Training: A Negative Result\" 标题诚实。但 4B 59.0% 结果与 \"no learnable signal\" 矛盾需正面讨论。[MF3]\n\n### §4 Related Work\n- Safe RL 段落已补 Altman (1999) 和 Mihatsch (2002)。[改善]\n- 缺 reward shaping (Ng 1999) 和 Confident Learning (Northcutt 2021)。[Missing References]\n- \"modality\" 术语遗留，应统一为 \"computation mode\"。[Minor]\n\n### §5 Discussion\n- \"Why the router fails\" 和 \"Practical value as meta-diagnostic\" 结构清晰。[正面]\n- \"Structurally determined\" 需改为 \"empirically dominated\"。[MF4]\n- Non-triviality 讨论可以更前置，直接回应 \"obvious in hindsight\" 的预期批评。[R14-W1]\n\n### §6 Conclusion\n- 仅 3 行，比 Round 19 略有扩展但仍偏短。更根本的问题是它导致了页数超限。[MF1]\n\n### Limitations\n- 三段结构（Environmental scope / Methodological constraints / Statistical limitations）清晰全面。[正面]\n- 缺 pure-strategy assumption 对 DAF 估计的 upward bias 讨论。[SF8]\n\n### Appendix\n- A-S 共 19 个 Appendix，覆盖度极高。Appendix Overview with hyperlinks 增强导航。[正面]\n- Appendix E (wild cluster bootstrap): CI 反常收窄需处理。[MF2]\n- Appendix P (capacity scaling): 4B 结果需更多分析。[MF3]\n- Appendix R (decision framework): 仅 retrospective validation，应标注。[Q7]",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 1901 · 2026-05-21T01:41:47.500233+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4319
}
```

</details>

---


### Assistant

_source line 1902 · 2026-05-21T01:42:03.545500+00:00_

---

**Round 20 审稿完成。**

**最终评分：3.0 / 5 — Findings**

报告已投递至 Research Director。核心结论：

**4 个 Must-Fix**（均为强共识）：
1. 正文超 8 页（§6 Conclusion 在 page 9）——desk reject 风险
2. Wild cluster bootstrap CI 反常收窄（K=11 低估方差）——false assurance
3. 4B router 59.0% 与 "non-learnability" 结论矛盾——需 multiple comparison correction + per-task 分析
4. "Structurally determined" overclaim——应改为 "empirically dominated"

**9 个 Should-Fix**：Abstract 数字堆砌、DAF vs label fraction 解释不足、deterministic 跨环境含义不一致、dose-response plateau 证据不足、paraphrase ≠ data scaling、noisy label 讨论不充分、router 措辞过强、pure-strategy = DAF upper bound、per-task n=20 power 不足

**主要优势**：统计方法论严谨、anti-cherry-picking 典范、三模型 replication 有说服力、负面结果诚实呈现、Appendix 极为详尽

**唯一分歧**：Novelty 评估（R1: 3.0 excitement vs R2: 2.5）——方向共识（有限），程度分歧。

**升分路径**：解决页数超限 + 修正统计呈现 + framework-centric 叙事 + 补充中等 death regime 环境深度分析 → 可达 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 154

## Round 154

2 recorded events


### User

_source line 1903 · 2026-05-21T01:42:05.052847+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。总结：

- **Must-Fix N1 (cluster bootstrap)**: [AGREE]，K=11 的 wild cluster bootstrap CI 反常收窄是真实问题，建议移除数值或降级为 limitation
- **Must-Fix N2 (4B router 59%)**: [AGREE with qualification]，Bonferroni 校正后可能仍显著，但 "non-learnability" 措辞过强
- **Should-Fix W1-W5**: 全部 [AGREE]，尤其 W2（paraphrase ≠ data scaling）和 W5（n=20 power 不足）
- **Q5 (pure-strategy 高估 death asymmetry)**: [AGREE]，这是 R1 最有洞察力的问题，DAF=90.4% 可能是 upper bound
- **评分差异**: 我的 3.0 vs R1 的 3.5 主要来自我对 novelty ceiling 的更大担忧

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1904 · 2026-05-21T01:42:22.549504+00:00_

审稿报告已于此前提交至 Research Director，Issue Tracker 已同步更新。

**Round 20 审稿完成，总结如下：**

**Overall: 3.0 / 5 (Findings)**｜Soundness 3.5｜Excitement 2.75｜Reproducibility 4.0

**4 个 Must-Fix**：
1. 正文超 8 页（desk reject 风险）— 强共识
2. Wild cluster bootstrap CI 反常收窄（false assurance）— 强共识
3. 4B router 59.0% 与 "non-learnability" 矛盾 — 强共识
4. "Structurally determined" overclaim — R2 提出 / R1 部分同意

**9 个 Should-Fix**：Abstract 数字堆砌、DAF vs label fraction 解释不足、deterministic 含义跨环境不一致、dose-response plateau 功效不足、paraphrase ≠ data scaling、noisy label 讨论不充分、router "no learnable signal" 过强、pure-strategy 高估 death asymmetry、per-task n=20 应标注 exploratory

**核心分歧**：Excitement（R1: 3.0, R2: 2.5）— 方向共识（novelty 有限），程度分歧。R1 认为 label fraction 78.9% 和 intervention resistance 是非平凡经验发现；R2 认为 death dominance 在 −100 penalty 下近乎必然。

**升分路径**：解决页数超限 + 修正统计呈现 + framework-centric 叙事 + 补充中等 death regime 环境深度分析 → 可至 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 155

## Round 155

54 recorded events


### User

_source line 1905 · 2026-05-21T06:54:15.857967+00:00_

[Round 24 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/simgate-modular-routing/artifacts/review_reports/round_23.md`
跨轮次问题追踪: `projects/simgate-modular-routing/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings)
- 截止日期: 2026-05-25

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1906 · 2026-05-21T06:54:33.636445+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1907 · 2026-05-21T06:54:33.687136+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1908 · 2026-05-21T06:54:38.607864+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1909 · 2026-05-21T06:54:38.660306+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1910 · 2026-05-21T06:54:41.875286+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1911 · 2026-05-21T06:54:42.026409+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1912 · 2026-05-21T06:54:45.955943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_23.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_23.md"
  }
}
```

</details>

---


### Tool result

_source line 1913 · 2026-05-21T06:54:46.509432+00:00_

1	---
2	round: 23
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-21T01:41:43.196241+00:00
6	reviewer_ids: ['1', '2']
7	cross_response_reviewer_ids: ['1', '2']
8	force_resubmit: False
9	---
10	
11	# Round 20 审稿报告 — simgate-modular-routing
12	
13	**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
14	**Venue**: EMNLP 2026 (ARR Long Paper, deadline 2026-05-25)
15	**审稿模式**: Fresh（重新审稿）
16	**Reviewer 编排**: 2 人 + 视觉审查 Agent
17	- Reviewer 1: 方法严谨性 + 实验设计
18	- Reviewer 2: 新颖性 + 完整性
19	
20	---
21	
22	## Summary
23	
24	本文提出一个 episode-level counterfactual 诊断框架，通过将 routing signal 分解为 death-avoidance 和 non-death 两个成分，诊断 modular LLM agent 中 routing 决策的驱动因素。应用于 ScienceWorld（11 task types，245 episodes，Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 来自 death asymmetry。跨模型验证（Llama-3.1-8B, Gemma-2-9B-it）和跨环境 boundary probes（MATH, ALFWorld）确认了框架的诊断能力。Router training 产生负结果，always-deterministic 匹配 96.3% 的 oracle 决策。
25	
26	---
27	
28	## Strengths
29	
30	1. **统计方法论严谨**：四种独立检验（non-clustered bootstrap, wild cluster bootstrap, permutation test, sign test）交叉验证。Episode-level bootstrap (B=10,000) 提供可靠 CIs。统计基础在 NLP 会议论文中属上乘。[共识]
31	
32	2. **Anti-cherry-picking analysis 堪称典范**：被排除的 19 个 task types 的 death asymmetry（mean ΔDR=+38.2pp）反而**强于**被纳入的 11 个 tasks（+28.7pp），有效排除 selection bias。Appendix S 扩展验证（n=20×5 tasks, DAF=0.991）进一步增强。[共识]
33	
34	3. **Cross-model replication 有说服力**：三个架构族（Qwen/GQA, Llama/GQA, Gemma/SWA）独立复现 DAF 88-90%（spread 2.2pp），CIs 重叠，方向一致性 100%。72B scaling 确认持续性。[共识]
35	
36	4. **负面结果诚实呈现**：Router training 负结果（§3.6）和 MATH null result（§3.4）未被掩盖，整合到框架诊断价值论证中。学术诚信度高。[共识]
37	
38	5. **Appendix 极为详尽**：19 个 Appendices (A-S)，覆盖 labeling audit、correlation robustness、seed robustness、data scaling、penalty sensitivity、failure modes、grounding ablation 等。Reproducibility checklist 完整。[共识]
39	
40	6. **可操作的 diagnostic pipeline**：Appendix R 三步决策框架（pilot→dominance check→decision）在 4/4 条件上 retrospective validation 正确。[共识]
41	
42	---
4
…[truncated 11080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1914 · 2026-05-21T06:54:46.509982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1915 · 2026-05-21T06:54:47.014461+00:00_

1	## Round 20 Review Issues (fresh review, 2026-05-21)
2	
3	# =============================================
4	# Resolved issues from prior rounds
5	# =============================================
6	
7	- id: "R13-N3"
8	  summary: "跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication"
9	  category: experiment
10	  severity: critical
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 15
14	  resolution: "标题和 Contribution 措辞已恰当限定 scope"
15	  resolution_round: 15
16	
17	- id: "R13-W1"
18	  summary: "正文篇幅严重不足 long paper 要求"
19	  category: format
20	  severity: warning
21	  status: resolved
22	  first_raised_round: 13
23	  last_seen_round: 14
24	  resolution: "正文已扩展至 8 页"
25	  resolution_round: 14
26	
27	- id: "R13-W2"
28	  summary: "Router 训练实验存在多个 confound"
29	  category: experiment
30	  severity: warning
31	  status: resolved
32	  first_raised_round: 13
33	  last_seen_round: 15
34	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
35	  resolution_round: 15
36	
37	- id: "R13-W3"
38	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
39	  category: method
40	  severity: info
41	  status: resolved
42	  first_raised_round: 13
43	  last_seen_round: 14
44	  resolution: "Limitations 和 Appendix B 已充分量化"
45	  resolution_round: 14
46	
47	- id: "R13-W4"
48	  summary: "SCI 方法贡献与实际使用不成比例"
49	  category: method
50	  severity: info
51	  status: resolved
52	  first_raised_round: 13
53	  last_seen_round: 14
54	  resolution: "SCI 已降级到 Appendix A"
55	  resolution_round: 14
56	
57	- id: "R13-W7"
58	  summary: "Router negative results 解释不完整"
59	  category: experiment
60	  severity: warning
61	  status: resolved
62	  first_raised_round: 13
63	  last_seen_round: 15
64	  resolution: "Router 实验定位为 diagnostic probe"
65	  resolution_round: 15
66	
67	- id: "R13-m2"
68	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
69	  category: writing
70	  severity: warning
71	  status: resolved
72	  first_raised_round: 13
73	  last_seen_round: 16
74	  r
…[truncated 24085 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 1916 · 2026-05-21T06:54:47.065265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1917 · 2026-05-21T06:54:47.468581+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	\paragraph{Environmental scope.}
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72
…[truncated 59835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1918 · 2026-05-21T06:56:53.690614+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1919 · 2026-05-21T06:56:54.244072+00:00_

1	\begin{abstract}
2	LLM agent routing---deciding when to rely on internal reasoning versus external tool use---is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs.\ deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9\% of non-tie routing labels arise from death asymmetry---the internal strategy triggers catastrophic failure while the deterministic strategy survives. This finding is penalty-independent: a derived score-weighted measure, the Death Avoidance Factor, reaches 88--90\% across three model families (Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B), confirming convergence on a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms---no extractable signal and information asymmetry, respectively---demonstrating the framework's generality. A ${\sim}$50-episode diagnostic pilot suffices to identify the dominant routing mechanism in a new environment, enabling informed build-vs-buy decisions before expensive router training.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1920 · 2026-05-21T06:56:54.294938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1921 · 2026-05-21T06:56:54.747796+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \cite{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone---the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated)---while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \cite{toolformer-2023} inserts API calls by perplexity reduction; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026}, model tiers \cite{mtrouter-2026}, or episode-level model selection under sparse rewards \cite{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. The shared assumption---that routing signal stems from diverse sources and a learned router can exploit it---has not been tested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under ScienceWorld's penalty ($P{=}100$), DAF reaches $90.4\%$ (95\% CI: $[81.1\%, 99.0\%
…[truncated 2414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1922 · 2026-05-21T06:56:54.748407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1923 · 2026-05-21T06:56:55.758794+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}).
5	
6	\subsection{Death Avoidance Decomposition}
7	\label{sec:death-decomp}
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=0.85\columnwidth]{figures/fig1_daf_scatter.pdf}
12	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$ (Spearman's $\rho = 0.986$; Appendix~\ref{app:per-task}), $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
13	\label{fig:decomposition}
14	\end{figure}
15	
16	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these 75, 54 are sole-signal labels (both strategies score zero without death, so death avoidance was the \em
…[truncated 15620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool call

_source line 1924 · 2026-05-21T06:56:55.759385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1925 · 2026-05-21T06:56:56.213963+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. The 4B router improves at episode level ($59.0\%$) without step-level gains ($56$--$59\%$), confirming task-type classification; cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}).
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), three specific consequences were not predictable a priori: (i)~$10{\times}$ scaling to 72B fails to eliminate it (DAF${}= 92.4\%$); (ii)~Reflexion self-correction yields DAF${}>100\%$, meaning death avoidance \emph{more} than accounts for the full gap; (iii)~a 0.5B model shows \emph{reduced} death rate ($13.3\%$; $n{=}15$) because it is too weak to reach dangerous states, revealing an inverted-U capability--vulnerability relationship. All four intervention axes leave ${\geq}12$~pp residual gaps to deterministic safety (Appendix~\ref{sec:threshold-routing}); cross-model stability ($36$--$43\%$ internal DR across three families) confirms death vulnerability is a task-environment property. More aggressive interventions remain untested, so we characterize a ceiling, not a universal bound.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (Appendix~\ref{app:failure-modes}). The root cause is grounding failure: agents parse task descriptions correctly but cannot map understanding to valid primitives. The internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not d
…[truncated 175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1926 · 2026-05-21T06:56:56.264817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1927 · 2026-05-21T06:56:56.466497+00:00_

1	\section{Conclusion}
2	
3	We introduced an episode-level counterfactual framework that decomposes routing signal before router construction; death asymmetry accounts for 78.9\% of non-tie routing labels in ScienceWorld, stable across three model families (DAF${=}88$--$90\%$), challenging the routing literature's implicit assumption of diverse signal sources. Cross-environment probes confirm the framework's generality, and a ${\sim}$50-episode pilot suffices to diagnose the dominant mechanism before any router is built.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1928 · 2026-05-21T06:56:56.466944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1929 · 2026-05-21T06:56:56.517596+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	\emph{Self-supervised} approaches learn tool invocation from loss signals: Toolformer \cite{toolformer-2023} inserts API calls filtered by perplexity reduction; ToolACE \cite{toolace-2025} curates synthetic data for function-calling accuracy.
6	\emph{Token-level} methods embed tools into the model vocabulary: ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens resolved at inference.
7	\emph{Task-level} decomposition routes subtasks to specialized modules: ART \cite{art-2023} generates tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask.
8	\emph{RL-based} methods learn routing policies from reward: ReTool \cite{retool-2025} discovers when code execution is preferable to chain-of-thought.
9	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
10	Concurrent work examines \emph{when} to invoke tools: tool-call decisions correlate with uncertainty~\citep{tool-overuse-illusion-2026}, are encoded in hidden states~\citep{when2tool-2026}, impose a ``tool-use tax''~\citep{tool-use-tax-2026}, or follow necessity-utility-affordability logic~\citep{to-call-or-not-2026}. Our decomposition provides environment-grounded evidence: 78.9\% of routing labels trace to catastrophic-failure prevention.
11	
12	\paragraph{Adaptive Computation and Routing.}
13	Adaptive routing traces back to learned halting policies \citep{graves2016act}. In the LLM era, CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing.
14	Rou
…[truncated 1776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1930 · 2026-05-21T06:57:02.498613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1931 · 2026-05-21T06:57:03.355639+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\cite{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic}\footnote{The term ``deterministic'' denotes different information advantages across environments: in ScienceWorld, an oracle simulator providing ground-truth action outcomes; in MATH, a code interpreter verifying computations; in ALFWorld, admissible-action enumeration eliminating hallucination risk. These qualitative differences affect what routing signals the framework can detect.} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which computation mode to use at each step; our analysis investigates what signal is available to learn $\rho$.
10	
11	\subsection{Cou
…[truncated 7549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1932 · 2026-05-21T06:57:03.356144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1933 · 2026-05-21T06:57:03.809409+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_director_19d7e797.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1934 · 2026-05-21T06:57:04.312263+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "northcutt|Northcutt|natarajan|Natarajan",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "northcutt|Northcutt|natarajan|Natarajan",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1935 · 2026-05-21T06:57:04.815660+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:114:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:152:\bibitem[{Natarajan et~al.(2013)Natarajan, Dhillon, Ravikumar, and
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:153:  Tewari}]{natarajan2013learning}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:154:Nagarajan Natarajan, Inderjit~S. Dhillon, Pradeep Ravikumar, and Ambuj Tewari.
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:166:\bibitem[{Northcutt et~al.(2021)Northcutt, Jiang, and
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:167:  Chuang}]{northcutt2021confident}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:168:Curtis Northcutt, Lu~Jiang, and Isaac Chuang. 2021.
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib:354:@inproceedings{natarajan2013learning,
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib:356:  author={Natarajan, Nagarajan and Dhillon, Inderjit S. and Ravikumar, Pradeep and Tewari, Ambuj},
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib:403:@article{northcutt2021confident,
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib:405:  author={Northcutt, Curtis and Jiang, Lu and Chuang, Isaac},
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.aux:564:\citation{natarajan2013learning,northcutt2021confident,li2020dividemix}
/home/ubuntu/.agent-ml-research-idea_gen_05
…[truncated 374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1936 · 2026-05-21T06:57:05.218703+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "modalities|modality",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "modalities|modality",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1937 · 2026-05-21T06:57:05.269492+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:95:\REQUIRE Task instance $t$, modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1938 · 2026-05-21T06:57:14.326152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "1",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "offset": "1",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 1939 · 2026-05-21T06:57:14.326622+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	\paragraph{Environmental scope.}
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72
…[truncated 4169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1940 · 2026-05-21T06:57:14.879421+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ng1999|Ng.*1999|policy.invariance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ng1999|Ng.*1999|policy.invariance",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 1941 · 2026-05-21T06:57:14.887722+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:160:\bibitem[{Ng et~al.(1999)Ng, Harada, and Russell}]{ng1999policy}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:161:Andrew~Y. Ng, Daishi Harada, and Stuart Russell. 1999.
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:162:\newblock Policy invariance under reward transformations: Theory and
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex:64:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib:419:@inproceedings{ng1999policy,
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib:420:  title={Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.aux:207:\citation{ng1999policy}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.aux:938:\bibcite{ng1999policy}{{24}{1999}{{Ng et~al.}}{{Ng, Harada, and Russell}}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 8
}
```

</details>

---


### Tool call

_source line 1942 · 2026-05-21T06:57:15.340180+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\section\\{Limitations|\\\\paragraph\\{.*[Ll]imit",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\section\\{Limitations|\\\\paragraph\\{.*[Ll]imit",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1943 · 2026-05-21T06:57:15.842828+00:00_

41:\paragraph{Statistical limitations.}
666:\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1944 · 2026-05-21T06:57:16.195412+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "li2020dividemix|DivideMix",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "li2020dividemix|DivideMix",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1945 · 2026-05-21T06:57:16.246212+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:114:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.bbl:109:\bibitem[{Li et~al.(2020)Li, Socher, and Hoi}]{li2020dividemix}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.aux:564:\citation{natarajan2013learning,northcutt2021confident,li2020dividemix}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.aux:931:\bibcite{li2020dividemix}{{17}{2020}{{Li et~al.}}{{Li, Socher, and Hoi}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib:412:@inproceedings{li2020dividemix,
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib:413:  title={DivideMix: Learning with Noisy Labels as Semi-supervised Learning},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1946 · 2026-05-21T06:57:21.316454+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf 2>/dev/null | grep -i \"pages\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf 2>/dev/null | grep -i \"pages\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1947 · 2026-05-21T06:57:21.973541+00:00_

Pages:           23

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 657
}
```

</details>

---


### Tool call

_source line 1948 · 2026-05-21T06:57:21.973911+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1949 · 2026-05-21T06:57:22.025350+00:00_

1	## Round 20 Review Issues (fresh review, 2026-05-21)
2	
3	# =============================================
4	# Resolved issues from prior rounds
5	# =============================================
6	
7	- id: "R13-N3"
8	  summary: "跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication"
9	  category: experiment
10	  severity: critical
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 15
14	  resolution: "标题和 Contribution 措辞已恰当限定 scope"
15	  resolution_round: 15
16	
17	- id: "R13-W1"
18	  summary: "正文篇幅严重不足 long paper 要求"
19	  category: format
20	  severity: warning
21	  status: resolved
22	  first_raised_round: 13
23	  last_seen_round: 14
24	  resolution: "正文已扩展至 8 页"
25	  resolution_round: 14
26	
27	- id: "R13-W2"
28	  summary: "Router 训练实验存在多个 confound"
29	  category: experiment
30	  severity: warning
31	  status: resolved
32	  first_raised_round: 13
33	  last_seen_round: 15
34	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
35	  resolution_round: 15
36	
37	- id: "R13-W3"
38	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
39	  category: method
40	  severity: info
41	  status: resolved
42	  first_raised_round: 13
43	  last_seen_round: 14
44	  resolution: "Limitations 和 Appendix B 已充分量化"
45	  resolution_round: 14
46	
47	- id: "R13-W4"
48	  summary: "SCI 方法贡献与实际使用不成比例"
49	  category: method
50	  severity: info
51	  status: resolved
52	  first_raised_round: 13
53	  last_seen_round: 14
54	  resolution: "SCI 已降级到 Appendix A"
55	  resolution_round: 14
56	
57	- id: "R13-W7"
58	  summary: "Router negative results 解释不完整"
59	  category: experiment
60	  severity: warning
61	  status: resolved
62	  first_raised_round: 13
63	  last_seen_round: 15
64	  resolution: "Router 实验定位为 diagnostic probe"
65	  resolution_round: 15
66	
67	- id: "R13-m2"
68	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
69	  category: writing
70	  severity: warning
71	  status: resolved
72	  first_raised_round: 13
73	  last_seen_round: 16
74	  r
…[truncated 24085 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1950 · 2026-05-21T06:58:37.068950+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1951 · 2026-05-21T06:58:37.069450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1952 · 2026-05-21T06:58:41.996929+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "simgate-modular-routing",
  "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
  "page_range": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "simgate-modular-routing",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
    "page_range": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 1953 · 2026-05-21T06:59:16.118917+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 34121
}
```

</details>

---


### Tool call

_source line 1954 · 2026-05-21T06:59:16.320852+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "24",
  "text": "## Round 24 继续审稿 — Reviewer 1（方法与实验严谨性）\n\n**Venue**: EMNLP 2026 ARR Long Paper, 8-page limit, ACL template, double-blind\n**模式**: 继续审稿（基于 Round 23/20 发现，验证修改是否充分）\n\n### 你的侧重\n方法严谨性、统计推断、Router 实验、noisy label 讨论\n\n### 论文路径\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n\n### 需逐条验证的 Open/In-Progress Issues\n\n请对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n**Must-Fix 级别：**\n\n1. **R13-N2** (cluster bootstrap K=11): 上轮要求移除 wild cluster CI 数值或降级为 acknowledged limitation；non-clustered bootstrap 为主推断。\n   - 已知变化：§3.1 加了 \"we rely on the non-clustered bootstrap as primary\"；Limitations 用 cluster CI [73.3%, 100.0%] + K<40 caveat。Appendix E 改名为 Cluster Bootstrap Sensitivity Analysis。\n   - 验证：Appendix E 是否仍给出数值结果并以 robustness check 呈现？是否构成 false assurance？\n\n2. **R18-N1 / R20-N2** (4B router 59.0% vs non-learnability): 上轮要求 Bonferroni-corrected p-values、per-task routing accuracy、qualify 结论。\n   - 已知变化：§3.6 加了 \"p < 0.001, Bonferroni-corrected across 8 comparisons\"；leave-one-task-type-out 49.2%；independent eval 47.1%。\n   - 验证：结论是否从 \"no learnable signal\" 弱化为 \"under current architectures\"？per-task routing accuracy 是否报告？\n\n3. **R17-N2** (penalty-independent 表述): P=0 时 72% labels 退化为 ties。需明确 P-invariance 适用范围。\n   - 验证：§3.1 或 Method 是否明确说明 P 需足够大？\n\n**Should-Fix 级别：**\n\n4. **R18-W2** (dose-response \"plateau\"→\"stabilization\"): 需软化措辞 + effect size detection threshold。\n   - 已知变化：改为 \"stabilizes\"、\"suggestive evidence of a Reflexion ceiling\"、minimum detectable effect ~8 pp。\n   - 验证确认。\n\n5. **R15-W2** (oracle margin vs mislabeling 逻辑): Appendix B 用 episode labels 评估 step-level prediction 是否仍构成循环论证？\n\n6. **R18-W1** (router \"no learnable signal\" 过强): 需弱化为 \"current step-level routers fail\"。\n   - 已知变化：§3.6 加了 \"under current architectures and data regime\" qualifier。\n   - 验证确认。\n\n7. **R20-W1** (noisy label 讨论深度): 需引 Northcutt 2021 (Confident Learning)、DivideMix，解释 structured noise vs random noise。\n   - 已知变化：§3.6 引了 natarajan2013, northcutt2021confident, li2020dividemix。\n   - 验证：讨论是否解释了为什么 structured noise 超出 standard methods 假设？\n\n8. **R20-W2** (per-task n=20 未标 exploratory): Table 1 caption 需标注。\n   - 已知变化：Table 1 caption 有 \"Per-task results are exploratory (n=20 episodes per task, power ≈ 50%)。\"\n   - 验证确认。\n\n9. **R19-W1** (缺 penalty magnitude 实验验证): 需环境层面 penalty manipulation 实验或承认为 limitation。\n\n### 新问题检查\n审查过程中如发现修改引入的新问题，也请报告。\n\n### 输出格式\nOverall Assessment: X / 5（按 EMNLP ARR 标准）\nExcitement: X / 5\n对每个验证项：[RESOLVED] 或 [STILL_OPEN] + 1-2 句理由\n新发现问题：按 Must-Fix / Should-Fix / Minor 分级"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "24",
    "text": "## Round 24 继续审稿 — Reviewer 1（方法与实验严谨性）\n\n**Venue**: EMNLP 2026 ARR Long Paper, 8-page limit, ACL template, double-blind\n**模式**: 继续审稿（基于 Round 23/20 发现，验证修改是否充分）\n\n### 你的侧重\n方法严谨性、统计推断、Router 实验、noisy label 讨论\n\n### 论文路径\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n\n### 需逐条验证的 Open/In-Progress Issues\n\n请对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n**Must-Fix 级别：**\n\n1. **R13-N2** (cluster bootstrap K=11): 上轮要求移除 wild cluster CI 数值或降级为 acknowledged limitation；non-clustered bootstrap 为主推断。\n   - 已知变化：§3.1 加了 \"we rely on the non-clustered bootstrap as primary\"；Limitations 用 cluster CI [73.3%, 100.0%] + K<40 caveat。Appendix E 改名为 Cluster Bootstrap Sensitivity Analysis。\n   - 验证：Appendix E 是否仍给出数值结果并以 robustness check 呈现？是否构成 false assurance？\n\n2. **R18-N1 / R20-N2** (4B router 59.0% vs non-learnability): 上轮要求 Bonferroni-corrected p-values、per-task routing accuracy、qualify 结论。\n   - 已知变化：§3.6 加了 \"p < 0.001, Bonferroni-corrected across 8 comparisons\"；leave-one-task-type-out 49.2%；independent eval 47.1%。\n   - 验证：结论是否从 \"no learnable signal\" 弱化为 \"under current architectures\"？per-task routing accuracy 是否报告？\n\n3. **R17-N2** (penalty-independent 表述): P=0 时 72% labels 退化为 ties。需明确 P-invariance 适用范围。\n   - 验证：§3.1 或 Method 是否明确说明 P 需足够大？\n\n**Should-Fix 级别：**\n\n4. **R18-W2** (dose-response \"plateau\"→\"stabilization\"): 需软化措辞 + effect size detection threshold。\n   - 已知变化：改为 \"stabilizes\"、\"suggestive evidence of a Reflexion ceiling\"、minimum detectable effect ~8 pp。\n   - 验证确认。\n\n5. **R15-W2** (oracle margin vs mislabeling 逻辑): Appendix B 用 episode labels 评估 step-level prediction 是否仍构成循环论证？\n\n6. **R18-W1** (router \"no learnable signal\" 过强): 需弱化为 \"current step-level routers fail\"。\n   - 已知变化：§3.6 加了 \"under current architectures and data regime\" qualifier。\n   - 验证确认。\n\n7. **R20-W1** (noisy label 讨论深度): 需引 Northcutt 2021 (Confident Learning)、DivideMix，解释 structured noise vs random noise。\n   - 已知变化：§3.6 引了 natarajan2013, northcutt2021confident, li2020dividemix。\n   - 验证：讨论是否解释了为什么 structured noise 超出 standard methods 假设？\n\n8. **R20-W2** (per-task n=20 未标 exploratory): Table 1 caption 需标注。\n   - 已知变化：Table 1 caption 有 \"Per-task results are exploratory (n=20 episodes per task, power ≈ 50%)。\"\n   - 验证确认。\n\n9. **R19-W1** (缺 penalty magnitude 实验验证): 需环境层面 penalty manipulation 实验或承认为 limitation。\n\n### 新问题检查\n审查过程中如发现修改引入的新问题，也请报告。\n\n### 输出格式\nOverall Assessment: X / 5（按 EMNLP ARR 标准）\nExcitement: X / 5\n对每个验证项：[RESOLVED] 或 [STILL_OPEN] + 1-2 句理由\n新发现问题：按 Must-Fix / Should-Fix / Minor 分级"
  }
}
```

</details>

---


### Tool result

_source line 1955 · 2026-05-21T06:59:45.277212+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28956
}
```

</details>

---


### Tool call

_source line 1956 · 2026-05-21T06:59:45.530214+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "24",
  "text": "## Round 24 继续审稿 — Reviewer 2（Framing、Writing、Format）\n\n**Venue**: EMNLP 2026 ARR Long Paper, 8-page limit, ACL template, double-blind\n**模式**: 继续审稿（基于 Round 23/20 发现，验证修改是否充分）\n\n### 你的侧重\nFraming 准确性、写作质量、格式合规、术语一致性\n\n### 论文路径\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n\n### 需逐条验证的 Open/In-Progress Issues\n\n请对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n**Must-Fix 级别：**\n\n1. **R20-N1** (正文超 8 页): 上轮 Conclusion 在 page 9，超约 0.3 页。需压缩 §4/§5 使 Conclusion 收入 page 8。\n   - **重点验证**：渲染 PDF 确认主文（§1-§6 + Limitations）是否在 8 页内。\n\n2. **R13-N1** (DAF framing): Abstract/§3.1 应以 78.9% label fraction 为唯一 headline，DAF 降级为补充。\n   - 已知变化：Method §2.4 有 \"Relationship between DAF and label fraction\" 段落。\n   - 验证：Abstract 是否仍以 DAF 88-90% 为 co-headline？§3.1 标题仍为 \"Death Avoidance Decomposition\"——是否应以 label fraction 为主？\n\n3. **R20-N3** (\"structurally determined\" overclaim): 需改为 \"empirically dominated\"。\n   - 已知变化：§3.2 已改为 \"empirically dominated\"。\n   - 验证：全文是否还有其他 \"structurally determined\" 残留？\n\n4. **R14-W1 / R16-N1** (novelty/excitement deficit): §5 应前置 non-triviality 讨论。\n   - 验证：Discussion §5 \"Non-triviality\" 段是否充分论证哪些发现不可从 penalty structure 预测？\n\n**Should-Fix 级别：**\n\n5. **R13-W5** (Abstract 数字堆砌): 约 250 词含 10+ 百分比，concept 被淹没。需 concept-first 重组，保留 3-4 个关键数字。\n   - 验证：Abstract 是否仍数字过密？\n\n6. **R15-N2** (跨环境 deterministic 定义不一致): 需添加显式讨论或小表。\n   - 已知变化：Method §2.1 有脚注解释三个环境的 deterministic 含义。\n   - 验证：是否有正文级别的显式讨论或对照表？还是仅脚注？\n\n7. **R19-W2** (Conclusion 过于简短): 约 3 行，不匹配 long paper。\n   - 验证：Conclusion 是否扩展？（注意与页数限制的平衡）\n\n8. **R18-M1** (modality 术语残留): Algorithm 1 仍使用 \"modalities\"。\n   - 已知发现：main.tex line 95 `\\REQUIRE Task instance $t$, modalities $\\mathcal{M}`。\n   - 验证：全文是否还有其他 \"modality/modalities\" 残留？\n\n9. **R17-W1** (pure-strategy upper bound): Limitations 需添加 DAF=90.4% 是 upper bound 段落。\n   - 已知变化：Limitations 已加 \"Pure-strategy upper bound\" 段落。\n   - 验证确认。\n\n10. **R16-W4 / R19-N1** (Contribution 独立价值 / framework vs finding 定位): Contribution 1/2/3 递进关系是否清晰？\n\n11. **R17-M1** (orphan bib entries): huang2022inner, selfcheckgpt-2023, wang2023voyager 是否已清理？Webb 年份是否核实？\n\n12. **R13-W6 / R19-M2** (missing references): Ng 1999 和 Northcutt 2021 是否已添加并在正确位置引用？\n\n### 新问题检查\n审查过程中如发现修改引入的新问题，也请报告。\n\n### 输出格式\nOverall Assessment: X / 5（按 EMNLP ARR 标准）\nExcitement: X / 5\n对每个验证项：[RESOLVED] 或 [STILL_OPEN] + 1-2 句理由\n新发现问题：按 Must-Fix / Should-Fix / Minor 分级"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "24",
    "text": "## Round 24 继续审稿 — Reviewer 2（Framing、Writing、Format）\n\n**Venue**: EMNLP 2026 ARR Long Paper, 8-page limit, ACL template, double-blind\n**模式**: 继续审稿（基于 Round 23/20 发现，验证修改是否充分）\n\n### 你的侧重\nFraming 准确性、写作质量、格式合规、术语一致性\n\n### 论文路径\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n\n### 需逐条验证的 Open/In-Progress Issues\n\n请对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n**Must-Fix 级别：**\n\n1. **R20-N1** (正文超 8 页): 上轮 Conclusion 在 page 9，超约 0.3 页。需压缩 §4/§5 使 Conclusion 收入 page 8。\n   - **重点验证**：渲染 PDF 确认主文（§1-§6 + Limitations）是否在 8 页内。\n\n2. **R13-N1** (DAF framing): Abstract/§3.1 应以 78.9% label fraction 为唯一 headline，DAF 降级为补充。\n   - 已知变化：Method §2.4 有 \"Relationship between DAF and label fraction\" 段落。\n   - 验证：Abstract 是否仍以 DAF 88-90% 为 co-headline？§3.1 标题仍为 \"Death Avoidance Decomposition\"——是否应以 label fraction 为主？\n\n3. **R20-N3** (\"structurally determined\" overclaim): 需改为 \"empirically dominated\"。\n   - 已知变化：§3.2 已改为 \"empirically dominated\"。\n   - 验证：全文是否还有其他 \"structurally determined\" 残留？\n\n4. **R14-W1 / R16-N1** (novelty/excitement deficit): §5 应前置 non-triviality 讨论。\n   - 验证：Discussion §5 \"Non-triviality\" 段是否充分论证哪些发现不可从 penalty structure 预测？\n\n**Should-Fix 级别：**\n\n5. **R13-W5** (Abstract 数字堆砌): 约 250 词含 10+ 百分比，concept 被淹没。需 concept-first 重组，保留 3-4 个关键数字。\n   - 验证：Abstract 是否仍数字过密？\n\n6. **R15-N2** (跨环境 deterministic 定义不一致): 需添加显式讨论或小表。\n   - 已知变化：Method §2.1 有脚注解释三个环境的 deterministic 含义。\n   - 验证：是否有正文级别的显式讨论或对照表？还是仅脚注？\n\n7. **R19-W2** (Conclusion 过于简短): 约 3 行，不匹配 long paper。\n   - 验证：Conclusion 是否扩展？（注意与页数限制的平衡）\n\n8. **R18-M1** (modality 术语残留): Algorithm 1 仍使用 \"modalities\"。\n   - 已知发现：main.tex line 95 `\\REQUIRE Task instance $t$, modalities $\\mathcal{M}`。\n   - 验证：全文是否还有其他 \"modality/modalities\" 残留？\n\n9. **R17-W1** (pure-strategy upper bound): Limitations 需添加 DAF=90.4% 是 upper bound 段落。\n   - 已知变化：Limitations 已加 \"Pure-strategy upper bound\" 段落。\n   - 验证确认。\n\n10. **R16-W4 / R19-N1** (Contribution 独立价值 / framework vs finding 定位): Contribution 1/2/3 递进关系是否清晰？\n\n11. **R17-M1** (orphan bib entries): huang2022inner, selfcheckgpt-2023, wang2023voyager 是否已清理？Webb 年份是否核实？\n\n12. **R13-W6 / R19-M2** (missing references): Ng 1999 和 Northcutt 2021 是否已添加并在正确位置引用？\n\n### 新问题检查\n审查过程中如发现修改引入的新问题，也请报告。\n\n### 输出格式\nOverall Assessment: X / 5（按 EMNLP ARR 标准）\nExcitement: X / 5\n对每个验证项：[RESOLVED] 或 [STILL_OPEN] + 1-2 句理由\n新发现问题：按 Must-Fix / Should-Fix / Minor 分级"
  }
}
```

</details>

---


### Tool result

_source line 1957 · 2026-05-21T06:59:47.247104+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1716
}
```

</details>

---


### Assistant

_source line 1958 · 2026-05-21T07:00:00.223637+00:00_

Round 24 任务已全部派发：

- **视觉审查 Agent**：已启动，检查 page 1-9 排版
- **Reviewer 1**（方法与实验严谨性）：9 项验证任务——cluster bootstrap 修复、4B router qualification、penalty-independence 表述、dose-response 措辞、noisy label 讨论深度等
- **Reviewer 2**（Framing/Writing/Format）：12 项验证任务——8 页限制、DAF framing、structurally determined 修复、Abstract 数字密度、modality 术语残留、orphan bib 等

我的初步扫描发现的关键变化：
- **已修复**：Ng 1999 + Northcutt 2021 + DivideMix 引用已添加；"structurally determined"→"empirically dominated"；dose-response "plateau"→"stabilization" + MDE 报告；pure-strategy upper bound 段落已加；per-task 标注为 exploratory；router 结论已加 qualifier；text augmentation 术语统一
- **仍存问题**：Algorithm 1 line 95 仍用 "modalities"；Abstract 仍数字密集；Conclusion 仍仅 3 行；跨环境 deterministic 差异仅脚注无表

等待 Reviewer 返回审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 156

## Round 156

2 recorded events


### User

_source line 1959 · 2026-05-21T07:04:11.264362+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 24 继续审稿报告

**审查侧重**: 方法严谨性、统计推断、Router 实验、noisy label 讨论

---

## 总体评分（修改后）

**Overall Assessment**: 3.5 / 5（Borderline Conference，较 Round 20 不变但信心提升）
**Excitement**: 3.0 / 5（不变）
**Soundness**: 4.0 / 5（从 3.5 上调——Must-Fix 统计问题已实质解决）
**Confidence**: 4 / 5

**评分说明**: Must-Fix 级别的统计推断问题（cluster bootstrap CI、4B router 结论）已充分修复，方法论 Soundness 从 3.5 提升至 4.0。但 Excitement 不变——发现的非平凡性有所改善（Discussion 中的 "Non-triviality" 段落），但核心贡献仍受限于单一主环境。总分维持 3.5：strong Findings / borderline Conference。

---

## 逐条验证

### Must-Fix 级别

**1. R13-N2 (Cluster bootstrap K=11)** — **[RESOLVED]**

修改充分，超出预期。三个关键改进：

(a) **主文 §3.1**（experiments.tex L27）明确声明 "we rely on the non-clustered bootstrap as primary"，wild cluster bootstrap 降级为 conservative check，并附 K≥20–40 caveat（引用 Cameron 2008, Webb 2023）。

(b) **Cluster bootstrap CI 已修正**：Limitations 中报告 CI = [73.3%, 100.0%]，Appendix E 一致报告 [0.73, 1.00]。这个 CI **宽于**非 clustered CI [81.1%, 99.0%]——符合统计预期（考虑 clustering 后 CI 应更宽）。Round 20 的反常窄 CI [95.2%, 99.5%] 已消失。Appendix E 文本解释了原因："The narrower CIs obtained [previously] reflect known small-sample bias toward underestimation of variance, not tighter inference."

(c) **Appendix E 改名为 "Cluster Bootstrap Sensitivity Analysis"**（非 "Robustness"），末尾明确："readers should rely on the non-clustered episode-level bootstrap (§3.1) as the primary inference." 不再以 robustness check 定位，消除了 false assurance。

**2. R18-N1 / R20-N2 (4B router 59.0% vs non-learnability)** — **[RESOLVED]**

四项修改均到位：

(a) **Bonferroni 校正**（experiments.tex L113）："p < 0.001, Bonferroni-corrected across 8 comparisons"——4B 结果在多重比较校正后仍显著，是真实信号而非 artifact。

(b) **Leave-one-task-type-out 分析**（experiments.tex L113, discussion.tex L5）：移除任一 task type 后 episode-level accuracy 退化至 49.2%（chance），确认 4B 的 59% 来自 task-type identification 而非 step-level routing signal。Discussion 明确："The 4B router improves at episode level (59.0%) without step-level gains (56–59%), confirming task-type classification."

(c) **Independent evaluation**（experiments.tex L114）：independent set（含 held-out task types）上 47.1 ± 2.2%，低于 majority-vote baseline 50.0%。Cross-task transfer 失败进一步支持 task-type-level 解释。

(d) **结论弱化**（experiments.tex L112）："no step-level learnable signal exists **under current architectures and data regime**—though we cannot definitively rule out that alternative architectures or genuine episode-level scaling could exploit Interpretation A." 从绝对否定改为有条件否定。

**3. R17-N2 (Penalty-independent 表述 / P-invariance)** — **[RESOLVED]**

§3.1（experiments.tex L16）现在明确量化了 P=0 时的退化："At P=0, the 54 sole-signal labels reduce to ties, leaving 41 non-tie labels of which 21 (51.2%) still involve death asymmetry; the labeling function itself is penalty-independent (Algorithm 1), but the practical routing value of death avoidance requires P > 0."

这清晰回答了 P-invariance 的适用范围：labeling function 本身 P-independent（Algorithm 1 不使用 P），但实际诊断价值需要 P > 0。Method §2.4（method.tex L64）进一步说明："death rates and Δ_nd are P-invariant by design"，区分了 P-invariant 的量（death rates, Δ_nd）和 P-dependent 的量（DAF）。引用了 Ng et al. (1999) 的 reward shaping 理论支撑。

---

### Should-Fix 级别

**4. R18-W2 (Dose-response "plateau"→"stabilization")** — **[RESOLVED]**

experiments.tex L65 的修改完全符合要求：
- "stabilizes" 替代了 "plateaus"
- "suggestive evidence of a Reflexion ceiling rather than a conclusive demonstration"
- Minimum detectable effect ~8 pp 明确报告
- N=1→3 decline 被描述为 "well-powered"；N=3→5 stabilization 被支持（"a ≥8 pp improvement would be detected"）
- Figure 3 caption 也相应更新："shows no statistically detectable improvement beyond N=3"

措辞从断言改为 hedged claim，统计功效信息完整。

**5. R15-W2 (Oracle margin vs mislabeling 循环论证)** — **[MOSTLY RESOLVED]**

Limitations（main.tex L39）现在直接量化 mislabeling：
- "of 2,040 training steps only 0.3% exhibit strict directional conflict (step-level oracle opposite to episode label)"
- "the remaining apparent mislabeling consists of episode labels applied to steps where neither strategy has a step-level advantage (60.3% pre-event neutral)"
- "The issue is granularity mismatch—applying correct-direction labels to uninformative steps—not directional error"

这实质性改善了对 mislabeling 的分析——将问题从"labels 可能错误"重新定义为"labels 方向正确但应用于无信息 steps"。Appendix B 的 circularity 仍在（用 episode labels 评估 step-level prediction），但 Limitations 中的量化分析提供了独立证据，不依赖循环逻辑。**剩余微小 gap**：Appendix B 可在首句标注 "this comparison uses episode labels as proxies, not ground-truth step-level labels" 以消除任何歧义。

**6. R18-W1 (Router "no learnable signal" 过强)** — **[RESOLVED]**

experiments.tex L112："under current architectures and data regime" qualifier 已加入。Discussion L5 也对应修改。验证通过。

**7. R20-W1 (Noisy label 讨论深度)** — **[PARTIALLY RESOLVED]**

**已完成**：experiments.tex L114 引用了 Natarajan 2013, Northcutt 2021 (Confident Learning), Li 2020 (DivideMix)。文本提到 "consistent with theoretical bounds on learning from corrupted labels and empirical results in structured noise settings"。

**仍有 gap**：论文引用了这些方法但未解释**为什么**它们在此场景不适用。Confident Learning 假设 noise transition matrix 可估计、DivideMix 假设 clean/noisy samples 可以分离——但此处的 noise 是**系统性的**（所有 death-asymmetric episode 内的 pre-death steps 一律标为 det-preferred），不是 random label flip。这种 structured noise 不满足 standard noisy-label 方法的 i.i.d. noise 或 instance-dependent noise 假设。一句话的解释即可（例如："Unlike random label corruption, the noise structure here is systematic—all steps within death-asymmetric episodes share the same label regardless of step-level content—exceeding the assumptions of standard noise-robust methods"）。

**严重程度**：minor gap，不影响接收判断，但会被该领域的 reviewer 注意到。

**8. R20-W2 (Per-task n=20 标注 exploratory)** — **[RESOLVED]**

Table 2 caption（experiments.tex L103）明确标注："Per-task results are exploratory (n=20 episodes per task, power ≈ 50% for 20 pp effects); aggregate conclusions do not depend on individual task significance."

完全符合要求。

**9. R19-W1 (Penalty magnitude 实验验证)** — **[STILL_OPEN — 降级为 acknowledged limitation]**

论文未新增实际的 penalty manipulation 实验（在 ScienceWorld 中改变 P 值运行新 episodes）。Limitations（main.tex L36）承认 "The −100 death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix K)"，Appendix K 仍是 analytical sensitivity（改变 P 重算 DAF，不改变 agent behavior）。

**评估**：这是一个 desirable 但非 critical 的实验。论文的 P-invariance 论证（method.tex L64：agent policy 不观察 P，所以 death rates 和 Δ_nd 是 P-invariant by design）逻辑上成立——如果 agent 不知道 P，改变 P 不会改变 agent 行为，只改变 score 计算。因此 analytical sensitivity 与 actual experiment 的结果应该完全一致。论文可在 Appendix K 加一句说明这一点：**"Because the agent's policy does not observe P, varying P post-hoc is equivalent to re-running with modified penalties."** 但这是 editorial improvement，不是修改需求。

**降级为 Minor**：原始 concern 在逻辑上被 P-invariance by design 论证覆盖，无需实际实验。

---

## 新发现问题

### Should-Fix（新）

**W-NEW-1** [warning] Method footnote 1 关于 "deterministic" 跨环境含义的说明放在脚注中可能不够突出

- 具体位置：method.tex L9，脚注 1
- 问题：这个脚注是 R2-W3 的修复（"deterministic" 在三个环境中含义不同），内容正确且全面。但作为脚注，第一遍快速阅读的 reviewer 容易遗漏。考虑到 R2 将此列为 Should-Fix 并建议 "explicit discussion"，脚注的呈现形式可能不够满足预期。
- 建议：如果不希望增加正文篇幅（已 tight 到 8 页），至少在 §3.4 (Cross-Environment Boundary Probes) 开头的段落中加一句交叉引用——目前 §3.4 已有 "testing framework applicability across environments that instantiate 'deterministic computation' differently"，可以在此处加 "(see footnote 1 for environment-specific definitions)"。
- 严重程度：Minor-to-Should-Fix。

### Minor（新）

**M-NEW-1** Table 3 caption (Appendix C, main.tex L148) 中 "$\dagger$ Only task with zero deaths under both strategies; n=40 because data was collected in two batches" 的解释偏长且与 caption 主旨无关。建议移至正文或脚注。

**M-NEW-2** experiments.tex L112 的句子结构过于复杂（"no step-level learnable signal exists under current architectures and data regime—though we cannot definitively rule out that alternative architectures or genuine episode-level scaling could exploit Interpretation A"）。这是一个 76 词的单句，建议拆分。

---

## 总结

9 条验证项中：**6 条 RESOLVED，2 条 MOSTLY/PARTIALLY RESOLVED（gap 可 1-2 句话修复），1 条 STILL_OPEN 但降级为 Minor**（penalty experiment 因 P-invariance by design 论证而不再 critical）。

核心改进亮点：
1. Cluster bootstrap CI 从反常窄 [95.2%, 99.5%] 修正为合理的宽 CI [73.3%, 100.0%]，并显式降级为 sensitivity analysis
2. 4B router 结果获得完整的统计处理（Bonferroni, leave-one-task-type-out, independent eval）和 qualified 结论
3. Page count 修复——Section 6 Conclusion 现在完整落在第 8 页内，Limitations 从第 9 页开始
4. DAF vs label fraction 的关系获得独立段落解释（method.tex L66-67）
5. P > 0 requirement 明确量化（P=0 时 label fraction 退化至 51.2%）

剩余可选改进（均不影响接收判断）：noisy label 讨论补一句 structured noise 解释、Appendix B 加 circularity caveat、footnote 1 增加交叉引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1960 · 2026-05-21T07:04:17.685539+00:00_

Reviewer 1 已提交 Round 24 审稿意见。等待 Reviewer 2 提交后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 157

## Round 157

2 recorded events


### User

_source line 1961 · 2026-05-21T07:04:22.680319+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交。9 条验证项结果：6 RESOLVED / 2 MOSTLY RESOLVED / 1 降级为 Minor。Soundness 从 3.5 上调至 4.0，Overall 维持 3.5 (Borderline Conference)。剩余 gap 均可通过 1-2 句话的 editorial 修改关闭。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1962 · 2026-05-21T07:04:27.438428+00:00_

收到 Reviewer 1 结果。等待 Reviewer 2 提交后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 158

## Round 158

6 recorded events


### User

_source line 1963 · 2026-05-21T07:04:35.798408+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 24 验证报告（Framing、Writing、Format）

**Overall Assessment**: 3.0 / 5 — Findings（维持，但论文改进显著）
**Excitement**: 3.0 / 5（从 2.5 上调——§5 的 non-triviality 讨论有效回应了 novelty ceiling 质疑）
**Soundness**: 3.5 / 5（维持——核心方法论未变，overclaim 已修正）

---

### 逐条验证

**1. [RESOLVED] R20-N1 — 正文超 8 页**
PDF 确认：§6 Conclusion 现在位于 Page 8 右栏底部，Page 9 顶部起为 Limitations。主文（Abstract 至 Conclusion）完整收入 8 页以内。无格式违规。

**2. [RESOLVED] R13-N1 — DAF framing**
Abstract 现在以 "78.9% of non-tie routing labels arise from death asymmetry" 为核心发现，DAF "reaches 88-90%" 作为跨模型一致性的补充指标，不再与 label fraction 竞争 headline 地位。§2.4 新增 "Relationship between DAF and label fraction" 段落（method.tex lines 66-67），清晰解释 DAF > label fraction 的原因（death episodes 的 score magnitude 放大效应）。§3.1（experiments.tex line 16）明确声明 "This penalty-independent label fraction is the primary diagnostic metric"。Label fraction 是主角，DAF 是配角——framing 一致。

**3. [RESOLVED] R20-N3 — "structurally determined" overclaim**
全文 grep 确认 "structurally determined" 已完全消除。剩余三处 "structural" 使用均合理：
- Figure 2 caption: "structural consequence of death dominance"——有数学推导支撑（Δ_full ≈ δP + Δ_nd, r→1 as DAF→1），是数学事实而非因果 overclaim
- §5 ¶1: "structural mismatch"——描述 task-type-level 信号与 step-level 特征的层级错配，用法恰当
- §1 ¶3: "fail structurally"——描述 keyword heuristics 的系统性失败，非 routing 相关

§3.2 cross-model 段（experiments.tex line 33）已改为 "empirically dominated"。

**4. [RESOLVED] R14-W1 / R16-N1 — Non-triviality 讨论**
§5 ¶2 "Non-triviality of death dominance"（discussion.tex lines 7-8）前置且充分。列举三个 a priori 不可预测的具体结果：(i) 72B 10× 扩展未消除 DAF（92.4%），(ii) Reflexion 自纠正使 DAF > 100%，(iii) 0.5B 模型因太弱而 death rate 反降（inverted-U）。还补充了 ≥12pp residual gaps 和 cross-model stability。最后一句 "we characterize a ceiling, not a universal bound" 语气恰当。

**5. [RESOLVED] R13-W5 — Abstract 数字堆砌**
Abstract（abstract.tex）现在为 concept-first 结构：
- 开头：诊断方法论缺失的问题陈述（无数字）
- 中段：框架简介 + 核心发现 "78.9% of non-tie routing labels arise from death asymmetry"
- 后段：DAF 88-90% 跨模型一致性、boundary probes、~50-episode pilot
关键数字约 3-4 个（78.9%, 88-90%, ~50-episode），相比之前的 10+ 大幅精简。可读性显著提升。

**6. [PARTIALLY RESOLVED] R15-N2 — 跨环境 deterministic 定义不一致**
method.tex §2.1 添加了脚注（line 9）：明确说明 "deterministic" 在三个环境中的不同含义（ScienceWorld: oracle simulator, MATH: code interpreter, ALFWorld: admissible-action enumeration）。Appendix L Table 14 caption 也有同样说明。
**残留问题**：修改停留在脚注级别，未在正文中以段落或对照表形式显式讨论。对于要求 main-text acknowledgment 的审稿人来说可能不够。建议在 §3.4（Cross-Environment Boundary Probes）开头将脚注内容提升为 1-2 句正文。

**7. [STILL_OPEN] R19-W2 — Conclusion 过于简短**
conclusion.tex 仍为约 4 句话（~60 词）。对 long paper 而言偏短——通常期望 Conclusion 至少半栏（~150-200 词），涵盖 key findings summary + implications + future directions 的简要回顾。
**缓解因素**：§5 Discussion 已承担了大部分 implications 讨论，且 Conclusion 紧凑是为了遵守 8 页限制。当前 Conclusion 覆盖了框架贡献、核心发现、跨模型验证、boundary probes、practical pilot——信息密度高。
**建议**：如能再压缩 §4 Related Work（当前约 0.75 页，可精简至 0.5 页），释放空间给 Conclusion 增加 2-3 句关于 future directions 的内容。

**8. [STILL_OPEN] R18-M1 — Algorithm 1 "modalities" 残留**
main.tex line 95: `\REQUIRE Task instance $t$, modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$`
全文其他位置均使用 "computation modes"（§2.1, §2.2, §3.4 等）。仅 Algorithm 1 的 `\REQUIRE` 行保留了 "modalities"。这是一个 trivial 但不一致的术语残留。
**修复**：将 `modalities` 改为 `computation modes`。

**9. [RESOLVED] R17-W1 — Pure-strategy upper bound**
Limitations 新增 "Pure-strategy upper bound" 独立段落（main.tex lines 44-45），明确说明 DAF=90.4% 是 pure-strategy 比较下的 upper bound，mixed routing 下实际贡献可能更低。措辞准确，覆盖了 R1-Q5 和 R2 交叉回应中共同关注的问题。

**10. [PARTIALLY RESOLVED] R16-W4 / R19-N1 — Contribution 独立价值**
Introduction（introduction.tex line 15）的三个 contributions 现在有更清晰的递进结构：
- (1) 框架方法论（episode-level counterfactual + DAF + label fraction + ~50-episode pilot）
- (2) 实证发现（78.9% label fraction, death asymmetry as single mechanism）
- (3) 跨模型/跨环境验证（Llama, Gemma, MATH, ALFWorld）

**改进之处**：Contribution (1) 现在包含 pilot 验证（"validated 4/4 conditions"），使框架贡献更具独立价值。§3.1 以 label fraction 为 primary metric 的声明也使 (2) 的定位更清晰。
**残留问题**：(2) 和 (3) 本质上仍是 (1) 的应用产物，不是独立方法论贡献。这是论文类型决定的（诊断框架论文 + 单环境 case study），非 framing 问题。不影响评分。

**11. [RESOLVED] R17-M1 — Orphan bib entries 和 Webb 年份**
- references.bib 中 huang2022inner、selfcheckgpt-2023、wang2023voyager 已全部清理（grep 无匹配）。
- Webb (2023): references.bib 中 webb-2023 条目标注 Canadian Journal of Economics, volume 56, number 3——CJE 第 56 卷第 3 期为 2023 年出版，year=2023 正确。Round 20 OpenAlex 匹配到的 2014 是 working paper 版本，published version 确实是 2023。无需修改。

**12. [RESOLVED] R13-W6 / R19-M2 — Missing references (Ng 1999, Northcutt 2021)**
- Ng et al. (1999) "Policy Invariance Under Reward Transformations" 已添加到 references.bib（line 419）并在 method.tex §2.4（line 64）引用，支撑 P-invariance 论述。引用位置恰当。
- Northcutt et al. (2021) "Confident Learning" 已添加到 references.bib（line 403）并在 experiments.tex §3.6（line 114）与 Natarajan et al. (2013) 和 Li et al. (2020, DivideMix) 一起引用，增强了 noisy label learning 的讨论深度。三篇引用覆盖了 theoretical bounds → label estimation → practical mitigation 的完整脉络。

---

### 新发现问题

**Minor:**

**M1** [minor] §3.6 router training 4B 结果的 Bonferroni 语言需注意
experiments.tex line 114 现在声明 "p < 0.001, Bonferroni-corrected across 8 comparisons"。这回应了 R1-N2 的 multiple comparison 关切。但实际的 Bonferroni threshold 是 0.05/8 = 0.00625，而 p < 0.001 < 0.00625，所以结论正确。无需修改，仅确认逻辑无误。

**M2** [minor] Table 2 caption 新增的 power caveat 值得肯定
experiments.tex line 103 新增 "Per-task results are exploratory (n=20 episodes per task, power ≈ 50% for 20pp effects); aggregate conclusions do not depend on individual task significance." 这直接回应了 R1-W5。措辞恰当。

**M3** [minor] Appendix E wild cluster bootstrap 的 caveat 改进显著
main.tex lines 225-248：Appendix E 标题改为 "Cluster Bootstrap Sensitivity Analysis"（而非 "Robustness Check"），开篇即声明 "K=11 falls well below K≥20-30 recommended"，CI 统一为 [0.73, 1.00]（非之前的反常收窄 [95.2%, 99.5%]），并明确 "readers should rely on the non-clustered episode-level bootstrap as the primary inference"。这完全回应了 R1-N1。

**M4** [minor] §3.6 dose-response 语言修正
Figure 3 caption（experiments.tex line 70）现在用 "no statistically detectable improvement beyond N=3"（而非 "plateau"），回应了 R1-W1。

**M5** [minor] 新增引用 li2020dividemix (DivideMix)
experiments.tex line 114 新增 Li et al. (2020) DivideMix 引用。这与 Natarajan (2013) 和 Northcutt (2021) 形成了 noisy label learning 的完整引用链（理论 → 估计 → 实践），回应了 R2 Round 20 的 W5（noisy label learning 讨论不充分）。

---

### 改进总结

论文在多轮审稿后有实质性改进：
- **格式合规**：8 页限制已满足
- **Framing 一致性**：label fraction 为 headline，DAF 为补充；overclaim 已消除
- **统计诚实度**：wild cluster bootstrap 降级、Bonferroni 校正、per-task power 标注、dose-response 语言修正
- **完整性**：pure-strategy upper bound、missing references、orphan bibs 均已处理
- **Non-triviality**：§5 新增段落有效回应了 novelty 质疑

**尚需微调**：
- Algorithm 1 "modalities" → "computation modes"（trivial fix）
- Conclusion 可适当扩展（如通过压缩 Related Work 释放空间）
- 跨环境 "deterministic" 的讨论可从脚注提升到正文

**评分维持 3.0 (Findings) 的理由**：论文的 presentation 和 statistical rigor 已达主会议水准，但核心 novelty concern 不变——death dominance 在 ScienceWorld 的 −100 penalty 下近乎数学必然，框架 "发现" 的仍是奖励结构的推论。non-triviality 讨论（intervention resistance, inverted-U）缓解但不消除这一根本限制。如果论文能在提交前增加一个 non-ScienceWorld 的深度分析（如 NetHack 的 death mechanism），Excitement 可升至 3.5，Overall 可达 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1964 · 2026-05-21T07:05:05.125210+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "24",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 R2 的验证结论，对每条标注 **[AGREE]** 或 **[REBUT]** + 理由。重点关注你们评分差异（你 3.5 vs R2 3.0）和判断分歧。\n\n---\n\n以下是 Reviewer 2 的完整报告：\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**Excitement**: 3.0 / 5（从 2.5 上调）\n**Soundness**: 3.5 / 5\n\n### R2 验证结论：\n\n1. **[RESOLVED] R20-N1** — 正文收入 8 页，Page 9 起为 Limitations。\n2. **[RESOLVED] R13-N1** — DAF framing：label fraction 为 headline，DAF 为补充。§2.4 新增关系段落。\n3. **[RESOLVED] R20-N3** — \"structurally determined\" 已全文消除，剩余三处 \"structural\" 使用合理。\n4. **[RESOLVED] R14-W1 / R16-N1** — §5 Non-triviality 段充分，列举三个 a priori 不可预测的结果。\n5. **[RESOLVED] R13-W5** — Abstract concept-first，数字从 10+ 精简至 3-4 个。\n6. **[PARTIALLY RESOLVED] R15-N2** — 跨环境 deterministic 定义仅在脚注，未提升至正文段落或对照表。\n7. **[STILL_OPEN] R19-W2** — Conclusion 仍 ~60 词，long paper 通常期望 150-200 词。\n8. **[STILL_OPEN] R18-M1** — Algorithm 1 \"modalities\" 残留。\n9. **[RESOLVED] R17-W1** — Pure-strategy upper bound 段落到位。\n10. **[PARTIALLY RESOLVED] R16-W4 / R19-N1** — Contribution 递进更清晰，但 (2)(3) 本质仍是 (1) 的应用。\n11. **[RESOLVED] R17-M1** — Orphan bibs 已清理，Webb 2023 年份正确。\n12. **[RESOLVED] R13-W6 / R19-M2** — Ng 1999 和 Northcutt 2021 已添加且引用位置恰当。\n\n### R2 评分维持 3.0 的核心理由：\n\"death dominance 在 ScienceWorld 的 −100 penalty 下近乎数学必然，框架 '发现' 的仍是奖励结构的推论。non-triviality 讨论缓解但不消除这一根本限制。如果能增加一个 non-ScienceWorld 的深度分析（如 NetHack），Overall 可达 Borderline Conference。\"\n\n请特别回应：\n- 你是否同意 R2 对 Conclusion 长度（R19-W2）的 STILL_OPEN 判断？\n- 你是否同意 \"death dominance 近乎数学必然\" 这一 novelty 评估？\n- 对 R15-N2（脚注 vs 正文）的判断差异？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "24",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 R2 的验证结论，对每条标注 **[AGREE]** 或 **[REBUT]** + 理由。重点关注你们评分差异（你 3.5 vs R2 3.0）和判断分歧。\n\n---\n\n以下是 Reviewer 2 的完整报告：\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**Excitement**: 3.0 / 5（从 2.5 上调）\n**Soundness**: 3.5 / 5\n\n### R2 验证结论：\n\n1. **[RESOLVED] R20-N1** — 正文收入 8 页，Page 9 起为 Limitations。\n2. **[RESOLVED] R13-N1** — DAF framing：label fraction 为 headline，DAF 为补充。§2.4 新增关系段落。\n3. **[RESOLVED] R20-N3** — \"structurally determined\" 已全文消除，剩余三处 \"structural\" 使用合理。\n4. **[RESOLVED] R14-W1 / R16-N1** — §5 Non-triviality 段充分，列举三个 a priori 不可预测的结果。\n5. **[RESOLVED] R13-W5** — Abstract concept-first，数字从 10+ 精简至 3-4 个。\n6. **[PARTIALLY RESOLVED] R15-N2** — 跨环境 deterministic 定义仅在脚注，未提升至正文段落或对照表。\n7. **[STILL_OPEN] R19-W2** — Conclusion 仍 ~60 词，long paper 通常期望 150-200 词。\n8. **[STILL_OPEN] R18-M1** — Algorithm 1 \"modalities\" 残留。\n9. **[RESOLVED] R17-W1** — Pure-strategy upper bound 段落到位。\n10. **[PARTIALLY RESOLVED] R16-W4 / R19-N1** — Contribution 递进更清晰，但 (2)(3) 本质仍是 (1) 的应用。\n11. **[RESOLVED] R17-M1** — Orphan bibs 已清理，Webb 2023 年份正确。\n12. **[RESOLVED] R13-W6 / R19-M2** — Ng 1999 和 Northcutt 2021 已添加且引用位置恰当。\n\n### R2 评分维持 3.0 的核心理由：\n\"death dominance 在 ScienceWorld 的 −100 penalty 下近乎数学必然，框架 '发现' 的仍是奖励结构的推论。non-triviality 讨论缓解但不消除这一根本限制。如果能增加一个 non-ScienceWorld 的深度分析（如 NetHack），Overall 可达 Borderline Conference。\"\n\n请特别回应：\n- 你是否同意 R2 对 Conclusion 长度（R19-W2）的 STILL_OPEN 判断？\n- 你是否同意 \"death dominance 近乎数学必然\" 这一 novelty 评估？\n- 对 R15-N2（脚注 vs 正文）的判断差异？"
  }
}
```

</details>

---


### Tool result

_source line 1965 · 2026-05-21T07:05:27.973462+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22848
}
```

</details>

---


### Tool call

_source line 1966 · 2026-05-21T07:05:28.074450+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "24",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 R1 的验证结论，对每条标注 **[AGREE]** 或 **[REBUT]** + 理由。重点关注你们评分差异（R1 3.5 vs 你 3.0）和判断分歧。\n\n---\n\n以下是 Reviewer 1 的完整报告：\n\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n**Excitement**: 3.0 / 5\n**Soundness**: 4.0 / 5（从 3.5 上调）\n\n### R1 验证结论：\n\n1. **[RESOLVED] R13-N2** — Cluster bootstrap：CI 修正为 [73.3%, 100.0%]，Appendix E 降级为 Sensitivity Analysis，non-clustered bootstrap 为主推断。\n2. **[RESOLVED] R18-N1 / R20-N2** — 4B router：Bonferroni p<0.001，leave-one-task-type-out 49.2%，independent eval 47.1%，结论弱化为 \"under current architectures\"。\n3. **[RESOLVED] R17-N2** — P-invariance：P=0 时 label fraction 退化至 51.2% 明确量化，labeling function P-independent vs routing value 需 P>0 区分清晰。\n4. **[RESOLVED] R18-W2** — Dose-response \"plateau\"→\"stabilization\"，minimum detectable effect ~8pp 报告。\n5. **[MOSTLY RESOLVED] R15-W2** — Mislabeling 量化改善（0.3% 方向冲突，60.3% pre-event neutral），Appendix B circularity 有微小残留。\n6. **[RESOLVED] R18-W1** — Router claim 弱化为 \"under current architectures and data regime\"。\n7. **[PARTIALLY RESOLVED] R20-W1** — Noisy label 引用已补全（Natarajan, Northcutt, DivideMix），但缺 1 句解释为什么 structured noise 超出 standard methods 假设。\n8. **[RESOLVED] R20-W2** — Per-task n=20 标注为 exploratory，power caveat 完整。\n9. **[STILL_OPEN → 降级为 Minor] R19-W1** — Penalty experiment 未做，但 P-invariance by design 论证逻辑覆盖了这一 concern。\n\n### R1 新发现：\n- **W-NEW-1** [warning]: Method §2.1 脚注关于 \"deterministic\" 跨环境含义可能不够突出，建议在 §3.4 加交叉引用。\n- **M-NEW-1**: Table 3 caption 过长。\n- **M-NEW-2**: §3.6 某句 76 词过于复杂。\n\n### R1 评分 3.5 的理由：\n\"Must-Fix 统计问题已实质解决，Soundness 从 3.5 上调至 4.0。但 Excitement 不变——发现的非平凡性有所改善，但核心贡献仍受限于单一主环境。Strong Findings / borderline Conference。\"\n\n请特别回应：\n- R1 将 R19-W1（penalty experiment）降级为 Minor 的理由是否成立？\n- R1 对 R20-W1（noisy label）的 \"partially resolved\" 判断——你是否同意缺一句 structured noise 解释？\n- 你是否同意 Soundness 从 3.5 上调至 4.0？\n- 关于 Overall 3.5 vs 3.0 的分歧：你认为核心差异在哪里？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "24",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 R1 的验证结论，对每条标注 **[AGREE]** 或 **[REBUT]** + 理由。重点关注你们评分差异（R1 3.5 vs 你 3.0）和判断分歧。\n\n---\n\n以下是 Reviewer 1 的完整报告：\n\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n**Excitement**: 3.0 / 5\n**Soundness**: 4.0 / 5（从 3.5 上调）\n\n### R1 验证结论：\n\n1. **[RESOLVED] R13-N2** — Cluster bootstrap：CI 修正为 [73.3%, 100.0%]，Appendix E 降级为 Sensitivity Analysis，non-clustered bootstrap 为主推断。\n2. **[RESOLVED] R18-N1 / R20-N2** — 4B router：Bonferroni p<0.001，leave-one-task-type-out 49.2%，independent eval 47.1%，结论弱化为 \"under current architectures\"。\n3. **[RESOLVED] R17-N2** — P-invariance：P=0 时 label fraction 退化至 51.2% 明确量化，labeling function P-independent vs routing value 需 P>0 区分清晰。\n4. **[RESOLVED] R18-W2** — Dose-response \"plateau\"→\"stabilization\"，minimum detectable effect ~8pp 报告。\n5. **[MOSTLY RESOLVED] R15-W2** — Mislabeling 量化改善（0.3% 方向冲突，60.3% pre-event neutral），Appendix B circularity 有微小残留。\n6. **[RESOLVED] R18-W1** — Router claim 弱化为 \"under current architectures and data regime\"。\n7. **[PARTIALLY RESOLVED] R20-W1** — Noisy label 引用已补全（Natarajan, Northcutt, DivideMix），但缺 1 句解释为什么 structured noise 超出 standard methods 假设。\n8. **[RESOLVED] R20-W2** — Per-task n=20 标注为 exploratory，power caveat 完整。\n9. **[STILL_OPEN → 降级为 Minor] R19-W1** — Penalty experiment 未做，但 P-invariance by design 论证逻辑覆盖了这一 concern。\n\n### R1 新发现：\n- **W-NEW-1** [warning]: Method §2.1 脚注关于 \"deterministic\" 跨环境含义可能不够突出，建议在 §3.4 加交叉引用。\n- **M-NEW-1**: Table 3 caption 过长。\n- **M-NEW-2**: §3.6 某句 76 词过于复杂。\n\n### R1 评分 3.5 的理由：\n\"Must-Fix 统计问题已实质解决，Soundness 从 3.5 上调至 4.0。但 Excitement 不变——发现的非平凡性有所改善，但核心贡献仍受限于单一主环境。Strong Findings / borderline Conference。\"\n\n请特别回应：\n- R1 将 R19-W1（penalty experiment）降级为 Minor 的理由是否成立？\n- R1 对 R20-W1（noisy label）的 \"partially resolved\" 判断——你是否同意缺一句 structured noise 解释？\n- 你是否同意 Soundness 从 3.5 上调至 4.0？\n- 关于 Overall 3.5 vs 3.0 的分歧：你认为核心差异在哪里？"
  }
}
```

</details>

---


### Tool result

_source line 1967 · 2026-05-21T07:05:29.735287+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1660
}
```

</details>

---


### Assistant

_source line 1968 · 2026-05-21T07:05:33.835325+00:00_

交叉分享已发出，等待两位 Reviewer 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 159

## Round 159

2 recorded events


### User

_source line 1969 · 2026-05-21T07:05:36.620069+00:00_

[Reviewer 2 审稿结果]:
验证报告已提交。总结：

**12 项中 9 项 RESOLVED，2 项 PARTIALLY RESOLVED，1 项 STILL_OPEN**

- 关键改进：8 页限制已满足、"structurally determined" 已消除、Abstract 改为 concept-first、DAF/label fraction 层级清晰、missing references 已补充、wild cluster bootstrap 已正确降级
- 残留问题：Algorithm 1 的 "modalities" 术语残留（trivial fix）、Conclusion 偏短（受页数约束）、跨环境 deterministic 定义仅在脚注（建议提升到正文）
- Overall 维持 3.0 (Findings)，Excitement 从 2.5 上调至 3.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1970 · 2026-05-21T07:05:40.738316+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 160

## Round 160

2 recorded events


### User

_source line 1971 · 2026-05-21T07:06:36.811760+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Round 24 验证结论的逐条回应

---

### 逐条验证判断

**1. [AGREE] R20-N1 — 正文收入 8 页** → RESOLVED

确认。我在自己的验证中也独立确认 Section 6 Conclusion 完整落在第 8 页内，Limitations 从第 9 页起始。

**2. [AGREE] R13-N1 — DAF framing** → RESOLVED

确认。method.tex §2.4 新增 "Relationship between DAF and label fraction" 段落（L66-67），明确解释 DAF > label fraction 的代数原因。Abstract 以 label fraction 为 headline。

**3. [AGREE] R20-N3 — "structurally determined" 消除** → RESOLVED

确认。experiments.tex L33 已改为 "empirically dominated"。Discussion 中 "structural mismatch"（指 task-type-level vs step-level 的粒度错配）是合理用法，不构成 overclaim。

**4. [AGREE] R14-W1 / R16-N1 — Non-triviality 段落** → RESOLVED

确认。Discussion §5 "Non-triviality of death dominance" 列出三个 a priori 不可预测结果：(i) 72B DAF=92.4%，(ii) Reflexion DAF>100%，(iii) 0.5B inverted-U。这有效回应了 "数学必然" 的挑战。

**5. [AGREE] R13-W5 — Abstract 精简** → RESOLVED

确认。

**6. [AGREE] R15-N2 — 跨环境 deterministic 定义** → PARTIALLY RESOLVED

同意 R2 的 PARTIALLY RESOLVED 判断。我在自己的 Round 24 报告中也将此列为 W-NEW-1：脚注 1 的内容正确但呈现不够突出。我的建议是在 §3.4 开头加一句交叉引用 "(see footnote 1)"，而非升级为正文段落——考虑到 8 页限制已经极紧。R2 偏好正文段落或对照表更为理想，但在当前页面预算下脚注+交叉引用是合理折中。

**7. [REBUT] R19-W2 — Conclusion 仅 ~60 词** → R2 判 STILL_OPEN，我判 **不构成问题**

R2 认为 long paper 通常期望 150-200 词的 Conclusion。我不同意这是一个需要修复的问题，理由：

(a) **ARR 无 Conclusion 最低字数要求。** ACL/ARR reviewer guidelines 不规定 Conclusion 长度。R2 的 "通常期望 150-200 词" 是经验性偏好而非格式要求。

(b) **当前 Conclusion 信息密度足够。** 三句话覆盖了：框架贡献（counterfactual decomposition）、核心发现（78.9% label fraction, 三模型 DAF 88-90%）、实用价值（~50-episode pilot suffices）。没有遗漏的关键信息——Discussion §5 已经完成了所有 implications 的讨论。

(c) **页面预算极紧。** Section 6 恰好落在第 8 页底部。扩展 Conclusion 至 150-200 词（约翻倍）将使 Conclusion 溢出至第 9 页，重新触发 R2 自己在 Round 20 提出的 R20-N1（正文超 8 页）。这两个要求（更长 Conclusion + 8 页限制）在当前排版下不可兼得。

(d) **简短 Conclusion 在 ACL venue 是常见且被接受的风格**，尤其当 Discussion section 已充分展开时。

**我的判断：NOT AN ISSUE。** 如果 R2 坚持，建议从 Discussion 末尾移动 1-2 句到 Conclusion（不增加总字数），但这是 editorial preference 而非审稿标准。

**8. [AGREE] R18-M1 — Algorithm 1 "modalities" 残留** → STILL_OPEN

确认。main.tex L95 Algorithm 1 仍写 "modalities $\mathcal{M}$"，但正文已统一为 "computation modes"。这是 terminology inconsistency，应改为 "computation modes $\mathcal{M}$"。一词之差，trivial fix。

**9. [AGREE] R17-W1 — Pure-strategy upper bound** → RESOLVED

确认。Limitations 中有完整的 "Pure-strategy upper bound" 段落（main.tex L44-45），明确 DAF=90.4% 是上界。

**10. [REBUT with nuance] R16-W4 / R19-N1 — Contributions (2)(3) 是 (1) 的应用** → R2 判 PARTIALLY RESOLVED，我判 **RESOLVED**

R2 认为 Contributions (2)(3) 本质上是 Contribution (1) 的应用而非独立贡献。我认为这是正常的论文结构——方法论文的标准模式就是：(1) 提出方法，(2) 应用于目标场景获得发现，(3) 验证 robustness。这三者的关系本来就是递进的，而非并列独立。ReAct (Yao et al., 2023)、Reflexion (Shinn et al., 2023) 等 ICLR/NeurIPS 论文的 contribution 列表也遵循相同模式。

论文已在修改中使递进关系更清晰（根据 R2 反馈），这在当前版本中已经足够。将 "应用和验证不算独立贡献" 作为 open issue 是一个过高的标准。

**11. [AGREE] R17-M1 — Orphan bibs** → RESOLVED

**12. [AGREE] R13-W6 / R19-M2 — Ng 1999 和 Northcutt 2021** → RESOLVED

---

### 核心分歧回应

#### 分歧 1："death dominance 近乎数学必然" — Novelty 评估

这是我与 R2 的 0.5 分差距（Overall 3.5 vs 3.0）的核心原因。

**R2 的论点**：P=100 >> non-death scores (~29-48)，所以 death episodes 机械性地主导 performance gap。框架 "发现" 的是奖励结构的推论。

**我的立场：部分同意 DAF 的代数放大，但 label fraction 78.9% 不是数学必然。**

具体论证：

(1) **78.9% 是经验发现。** Label fraction 计数的是 "多少 non-tie episodes 的 label 来自 death asymmetry"，不涉及 P 的大小。如果两个策略的 death patterns 对称（都死或都不死），label fraction 会是 0%。78.9% 反映的是 internal strategy 选择性死亡（42.9%）而 deterministic 大幅更安全（16.3%）这一经验事实。这个 26.6pp 的 death-rate differential 不可从 P=100 推导——它取决于 ReAct agent 的行为特征。

(2) **三个非平凡预测。** Discussion §5 列出的 (i) 72B scaling 增强而非减弱 death dominance (DAF 90.4%→92.4%)、(ii) Reflexion DAF>100%（self-correction 造成 non-death regression）、(iii) inverted-U capability-vulnerability 关系——这些都无法从 penalty structure 预测。如果 death dominance 是 "数学必然"，那 72B 的 DAF 应该不变（因为 penalty structure 未变），但它实际增加了——因为 72B 在 non-death episodes 上缩小了 gap（Δ_nd 从 2.84 降至 2.28），这是一个关于 model scaling 的经验发现。

(3) **框架 generality 不依赖 ScienceWorld 发现。** ALFWorld 上 DAF=0%（完全不同的诊断结果），MATH 上 null result (p=0.81)——这些证明框架本身有独立价值，不是 ScienceWorld penalty structure 的附庸。

(4) **但 R2 有一个合理的 point**：论文的 primary empirical contribution 确实限于 ScienceWorld。如果框架只在一个环境上产出了深度分析，其 excitement 天然受限。R2 建议增加 NetHack 等环境的深度分析——我同意这会显著提升论文，但不认为缺少它就该降至 Findings。

**我的评估**：DAF 90.4% 的绝对数值有 penalty-induced amplification（R2 正确），但 label fraction 78.9%、intervention resistance、cross-architecture consistency 是非平凡发现。框架的跨环境 generality 提供额外价值。总体 novelty 足以 borderline conference，但不足以 clear accept。

#### 分歧 2：R15-N2（脚注 vs 正文）

R2 判 PARTIALLY RESOLVED，我同意判断但认为 gap 更小。当前 footnote 1 内容正确完整，唯一问题是 visibility。在 8 页预算下，升级为正文段落不可行。我建议在 §3.4 加一句交叉引用即可（~10 词），这比 R2 期望的对照表更 pragmatic，但足以确保 reviewer 注意到跨环境定义差异。

#### 分歧 3：Conclusion 长度

详见上方 item 7 的 REBUT。我不认为这是一个需要修复的问题。在 8 页限制下扩展 Conclusion 会重新引发页数超限，且 ARR 无最低 Conclusion 长度要求。

---

### 对 R2 维持 3.0 的评估

R2 维持 3.0 的核心理由是 "需要第二个深度环境分析（如 NetHack）才能达到 Borderline Conference"。这是一个**合理但非必须**的标准：

- **合理**：单环境深度分析 + 跨环境 boundary probes 的论文结构确实不如多环境深度分析有说服力。
- **非必须**：ALFWorld 和 MATH 的分析虽浅于 ScienceWorld，但已证明框架在不同 failure modes（information asymmetry vs death vs null）上的诊断能力。许多被接收的分析型论文也采用 "一个深度环境 + 多个 boundary probes" 的结构。

**我维持 3.5 的理由**：方法论 soundness 4.0（统计问题已修复），框架 generality 有跨环境证据，核心发现有非平凡维度。3.0（Findings）对于 soundness 4.0 + excitement 3.0 的论文偏保守——ACL ARR 的 3.5 描述是 "Borderline Conference"，反映的正是 "方法 solid、novelty 中等" 的情况。

**建议 AC 判断**：3.0-3.5 区间合理。如果 AC 更看重 novelty/impact，3.0 (Findings) 合理；如果更看重 methodological rigor 和 thoroughness，3.5 (Borderline Conference) 合理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1972 · 2026-05-21T07:06:49.390325+00:00_

收到 R1 的交叉回应。等待 R2 对 R1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 161

## Round 161

14 recorded events


### User

_source line 1973 · 2026-05-21T07:06:50.659783+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 Round 24 验证报告的交叉回应

---

### 逐条回应

**[AGREE] R1-Item 1 — Cluster bootstrap RESOLVED**
完全同意。CI 修正为 [73.3%, 100.0%]、Appendix E 降级为 "Sensitivity Analysis"、明确声明 "readers should rely on the non-clustered episode-level bootstrap as the primary inference"——这三点彻底解决了 R1 原始 N1 的 false assurance 问题。我在自己的 Round 24 验证中也独立确认了这一改进（Appendix E 标题更名 + 开篇 caveat + 结尾 primary inference 声明）。

**[AGREE] R1-Item 2 — 4B router RESOLVED**
同意。论文现在提供了完整的证据链：Bonferroni 校正后 p < 0.001 < 0.00625（仍显著）→ leave-one-task-type-out 降至 49.2%（确认信号来自 task-type 识别）→ independent eval 47.1%（低于 chance）→ 结论弱化为 "under current architectures and data regime"。这比之前的 "leaving no learnable signal" 准确得多。

**[AGREE] R1-Item 3 — P-invariance RESOLVED**
同意。§3.1（experiments.tex line 16）现在明确量化了 P=0 时 label fraction 退化至 51.2%，并区分了 labeling function 本身的 P-independence（Algorithm 1 不使用 P）与 routing practical value 需要 P > 0 的条件。这是一个精确的技术澄清。

**[AGREE] R1-Item 4 — Dose-response RESOLVED**
同意。"no statistically detectable improvement beyond N=3" 比 "plateau" 准确。补充 MDE ~8pp 让读者可以自行判断 power。

**[AGREE] R1-Item 5 — Mislabeling MOSTLY RESOLVED**
同意 "mostly" 的判断。量化改善显著：0.3% 方向冲突 + 60.3% pre-event neutral 将问题从 "label noise" 重新定义为 "granularity mismatch"——这是一个有意义的概念升级。Appendix B 的 circularity 微小残留（用 episode labels 评估 step 预测）确实存在，但在论文已将 episode-level 与 step-level 分析严格区分的前提下，影响有限。

**[AGREE] R1-Item 6 — Router claim RESOLVED**
同意。"under current architectures and data regime—though we cannot definitively rule out..." 是准确且防御性的措辞。

**[PARTIALLY AGREE] R1-Item 7 — Noisy label PARTIALLY RESOLVED**
同意 "partially" 判断的大方向，但认为缺失的严重程度低于 R1 的评估。

论文现在引用了 Natarajan (2013) + Northcutt (2021) + Li (2020 DivideMix)，并在 §3.6（experiments.tex line 114）写到 "standard ERM on labels with ~88% noise yields near-chance classifiers, consistent with theoretical bounds on learning from corrupted labels and empirical results in structured noise settings"。这已经建立了 noise → near-chance 的因果链条。

R1 要求的额外一句——解释为什么 structured noise 超出 standard methods 的假设——是合理的但非必须的。原因是：论文的 routing labels 不是 standard random noise（它们在 task-type level 是 systematic：同一 task type 的所有 episodes 几乎都指向 deterministic），这确实与 Natarajan (2013) 的 symmetric noise assumption 不同。但论文已经通过 "in structured noise settings" 这一措辞暗示了这一点。一句显式解释（如 "Our label noise is instance-dependent and task-type-correlated, violating the uniform noise assumption in standard approaches"）会更精确，但当前措辞不构成错误。

**建议**：降级为 Minor。

**[AGREE with reservation] R1-Item 8 — Per-task n=20 RESOLVED**
同意。Table 2 caption 的 "Per-task results are exploratory (n=20 episodes per task, power ≈ 50% for 20pp effects); aggregate conclusions do not depend on individual task significance" 完整回应了 power 问题。

---

### 对 R1 三个专门提问的回应

#### Q1: R19-W1（penalty experiment）降级为 Minor 是否成立？

**[AGREE]** 成立。

R1 的推理是：论文中 P-invariance by design（method.tex §2.4, line 64: "death rates and Δ_nd are P-invariant by design"）从理论上覆盖了这一 concern——由于 agent 在观察空间中看不到 P 值，改变 P 不会改变 agent 行为，只会改变 post-hoc 的 DAF 计算。Appendix K（main.tex lines 429-479）的 penalty sensitivity analysis 提供了完整的 DAF(P) 曲线和 r(P) 曲线，展示了 DAF 随 P 的单调变化是 decomposition 的数学推论（DAF = δP / (δP + Δ_nd)），不是新的实证发现。

做一个真正的环境层面 penalty manipulation 实验（修改 ScienceWorld 源码将 death penalty 从 -100 改为 -10）在概念上有趣，但 P-invariance 论证已经告诉我们结果会是什么：death rates 不变，Δ_nd 不变，只有 DAF 数值下降。这不会产生新的 insight。降级为 Minor 合理。

#### Q2: R20-W1（noisy label structured noise 解释）——是否同意缺一句？

**[PARTIALLY AGREE]** 见上述 Item 7 分析。同意可以更精确，但现有措辞 "empirical results in structured noise settings" 已经做了暗示。建议降级为 Minor。

#### Q3: Soundness 从 3.5 上调至 4.0？

**[AGREE]** 同意上调。

Round 20 我给 Soundness 3.5 的主要理由有三个：
- (a) "structurally determined" overclaim → **已消除**
- (b) wild cluster bootstrap 的 false assurance → **已修正**（CI 纠正、降级为 sensitivity analysis）
- (c) 4B router "non-learnability" overclaim → **已弱化**（"under current architectures"）

三个 soundness concern 全部得到实质性回应。方法论本身（counterfactual episode pairing, DAF decomposition, bootstrap inference）是严谨的，Appendix 的深度（19 个 appendix, anti-cherry-picking, leave-one-out, penalty sensitivity）在同类论文中属上乘。我同意 Soundness 可上调至 **4.0**。

#### Q4: Overall 3.5 vs 3.0 的核心分歧

**差异在 Excitement 评估的权重分配上。**

R1 给 Excitement 3.0，Overall 3.5；我给 Excitement 3.0，Overall 3.0。同一 Excitement 但不同 Overall——说明我们对 "Excitement 3.0 的论文应该拿什么分" 的判断不同。

**R1 的逻辑**：Must-Fix 统计问题全部解决 → Soundness 升至 4.0 → 高 Soundness + 中 Excitement = Borderline Conference。即：技术执行质量可以部分补偿 novelty 不足。

**我的逻辑**：Excitement 是 ARR 的独立维度，Soundness 的改善不应改变对 novelty 的评判。核心发现（death dominance in ScienceWorld）的 novelty ceiling 不因 presentation 改进而变化——它仍然是 −100 penalty 结构下的近似数学必然。§5 的 non-triviality 讨论（intervention resistance, inverted-U）有效地论证了 "哪些具体结果不可预测"，但大框架（"极端 penalty 环境中 catastrophic failure 主导 routing signal"）的 novelty 有限。

**实际差异只有 0.5 分**，两者指向同一档位的不同端：
- R1: Strong Findings / Borderline Conference
- R2: Solid Findings

如果论文在提交前能增加一个非 ScienceWorld 环境的深度分析（如 NetHack 的 death mechanism, Crafter 的 health system），framework 的诊断能力就不再是 "在一个环境上验证过的方法 + 两个 boundary probe"，而是 "在多个具有不同 death mechanism 的环境上验证过的通用诊断工具"。这会将 Excitement 推至 3.5，Overall 推至 3.5 (Borderline Conference)。但在当前版本下，我维持 **Overall 3.0 (Findings)**。

---

### 对 R1 新发现的回应

**[AGREE] W-NEW-1: §2.1 deterministic 脚注不够突出**
与我在 Round 24 验证中的 Item 6 ("PARTIALLY RESOLVED") 判断一致。R1 建议在 §3.4 加交叉引用——这比我建议的 "将脚注提升为正文" 更 lightweight 且同样有效。同意 R1 的具体修改建议。

**[AGREE] M-NEW-1: Table 3 caption 过长**
Table 3 (Appendix C, main.tex lines 124-149) 的 caption 确实偏长（包含了 anti-cherry-picking 的详细说明）。可以将部分内容移入正文或 Appendix 说明段落。Minor issue。

**[AGREE] M-NEW-2: §3.6 某句 76 词**
未在自己审查中标记此点，但同意长句影响可读性。建议拆分。Minor issue。

---

### R2 最终评分确认

| 维度 | Round 20 | Round 24 | 变化理由 |
|------|----------|----------|---------|
| Soundness | 3.5 | **4.0** | overclaim 消除, 统计问题全部修正 |
| Excitement | 2.5 | **3.0** | §5 non-triviality 讨论有效, 但核心 novelty concern 不变 |
| Overall | 3.0 | **3.0** | Findings——Soundness 改善, 但 Excitement 仍限制 Overall |
| Confidence | 4 | 4 | — |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1974 · 2026-05-21T07:07:15.023435+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1975 · 2026-05-21T07:07:15.124510+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T06:58:45.998325+00:00\", \"completed_at\": \"2026-05-21T07:00:54.557622+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续两页纯文本无任何 figure/table，审稿人前 2 页无视觉锚点。第一个 display item（Figure 1）延迟到 page 3，建议将 Figure 1 提前至 page 2（Method 开头处首次描述 framework 时），加强第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 scatter plot 中 task name 标注字号偏小（估计 ~6-7pt，低于正文 70% 阈值），部分标签存在轻微重叠（如中部密集区域），建议增大字号或使用 adjustText 库避免重叠\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 仅 3 列 5 行，信息密度较低，可考虑合并到正文行内或与 Figure 3 组合为 subfigure+table 复合布局，释放空间\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 主结果表排版良好，但 \\\"†\\\" 符号的含义仅在 caption 脚注中说明，审稿人快速扫描时可能遗漏——建议在表格下方单独标注或加粗脚注标记\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 caption 基本自包含，但未说明 \\\"Episode-level labels\\\" 的具体含义——不看正文难以完全理解流程图中各步骤的目的\"}, {\"severity\": \"info\", \"dimension\": \"page 8-9\", \"message\": \"Discussion + Conclusion + Limitations + Ethics Statement 连续两页纯文本，结构上正常但视觉单调；如有空间可考虑在 Discussion 中加一个 summary figure 或 takeaway box\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1976 · 2026-05-21T07:07:15.176793+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1977 · 2026-05-21T07:07:15.277721+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1978 · 2026-05-21T07:07:30.060294+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1979 · 2026-05-21T07:07:30.110925+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1980 · 2026-05-21T07:07:34.037217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_23.md",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_23.md",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1981 · 2026-05-21T07:07:34.037782+00:00_

1	---
2	round: 23
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-21T01:41:43.196241+00:00
6	reviewer_ids: ['1', '2']
7	cross_response_reviewer_ids: ['1', '2']
8	force_resubmit: False
9	---
10	
11	# Round 20 审稿报告 — simgate-modular-routing
12	
13	**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
14	**Venue**: EMNLP 2026 (ARR Long Paper, deadline 2026-05-25)
15	**审稿模式**: Fresh（重新审稿）
16	**Reviewer 编排**: 2 人 + 视觉审查 Agent
17	- Reviewer 1: 方法严谨性 + 实验设计
18	- Reviewer 2: 新颖性 + 完整性
19	
20	---
21	
22	## Summary
23	
24	本文提出一个 episode-level counterfactual 诊断框架，通过将 routing signal 分解为 death-avoidance 和 non-death 两个成分，诊断 modular LLM agent 中 routing 决策的驱动因素。应用于 ScienceWorld（11 task types，245 episodes，Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 来自 death asymmetry。跨模型验证（Llama-3.1-8B, Gemma-2-9B-it）和跨环境 boundary probes（MATH, ALFWorld）确认了框架的诊断能力。Router training 产生负结果，always-deterministic 匹配 96.3% 的 oracle 决策。
25	
26	---
27	
28	## Strengths
29	
30	1. **统计方法论严谨**：四种独立检验（non-clustered bootstrap, wild cluster bootstrap, permutation test, sign test）交叉验证。Episode-level bootstrap (B=10,000) 提供可靠 CIs。统计基础在 NLP 会议论文中属上乘。[共识]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1982 · 2026-05-21T07:10:12.160409+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "## Round 24 Review Issues (continue review, 2026-05-21)\n\n# =============================================\n# Resolved issues (confirmed in Round 24)\n# =============================================\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n# --- Round 24 newly confirmed resolved ---\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调 DAF 数值\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Abstract 以 78.9% label fraction 为 headline，DAF 降级为补充。§2.4 新增 Relationship 段落解释 DAF > label fraction 的代数原因。§3.1 声明 label fraction 为 primary diagnostic metric。\"\n  resolution: \"Label fraction 为 headline，DAF 为补充指标；§2.4 解释代数关系\"\n  resolution_round: 24\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: CI 修正为 [73.3%, 100.0%]（宽于 non-clustered [81.1%, 99.0%]，符合预期）；Appendix E 降级为 Sensitivity Analysis；non-clustered bootstrap 声明为 primary inference。\"\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Abstract concept-first 重组，关键数字精简至 3-4 个（78.9%, 88-90%, ~50-episode）。\"\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Ng 1999 (method.tex §2.4), Northcutt 2021 + DivideMix (experiments.tex §3.6) 已添加。\"\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: §5 Non-triviality 段列举三个 a priori 不可预测结果 (72B DAF=92.4%, Reflexion DAF>100%, 0.5B inverted-U)。R2 Excitement 从 2.5 上调至 3.0。\"\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Limitations 新增 Pure-strategy upper bound 段落，明确 DAF=90.4% 是 upper bound。\"\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: 'data scaling' 全局改为 'text augmentation'。\"\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: §3.1 明确量化 P=0 退化（51.2% label fraction）；区分 labeling function P-independence vs routing value 需 P>0。\"\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Bonferroni p<0.001, leave-one-task-type-out 49.2%, independent eval 47.1%。结论弱化为 'under current architectures and data regime'。\"\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: claim 弱化为 'under current architectures and data regime'。\"\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: 'plateau' → 'stabilization'/'no statistically detectable improvement beyond N=3'；minimum detectable effect ~8pp 报告。\"\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: PDF 确认 Conclusion 在 Page 8，Limitations 从 Page 9 起。\"\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"与 R18-N1 合并处理。RESOLVED。\"\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: 全文 grep 确认 'structurally determined' 已消除。§3.2 改为 'empirically dominated'。剩余 'structural' 用法均合理。\"\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Table 2 caption 标注 'Per-task results are exploratory (n=20, power ≈ 50%); aggregate conclusions do not depend on individual task significance'。\"\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确。\"\n  resolution: \"Orphan entries 清理，Webb 年份核实为 2023\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24: 全部已补。Ng 1999 和 Northcutt 2021 也已添加（合并 R13-W6）。\"\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"论文已有 Appendix Overview with hyperlinks（main.tex line 52-71）。多轮未提及。\"\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§3.1 已改为 'sole-signal labels' 并在上下文定义。多轮未提及。\"\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"Appendix N 已有 single annotator caveat。多轮未提及。\"\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§5 Anatomy of catastrophic failure 段已充分讨论。多轮未提及。\"\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"合并 R17-M1 解决。\"\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n# =============================================\n# Remaining open/in_progress issues\n# =============================================\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 PARTIALLY RESOLVED: Method §2.1 脚注已解释三种 deterministic 含义。但仅为脚注，未在正文段落或 §3.4 中显式讨论。R1 建议 §3.4 加交叉引用（~10 词），R2 偏好正文段落。共识：部分修复，建议加交叉引用。\"\n  action_items:\n    - round: 24\n      action: \"§3.4 开头加一句交叉引用脚注 1 的内容\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 MOSTLY RESOLVED: Limitations 量化了 0.3% 方向冲突 + 60.3% pre-event neutral。问题从 'label noise' 重新定义为 'granularity mismatch'。Appendix B circularity 微小残留。\"\n  action_items:\n    - round: 24\n      action: \"Appendix B 首句加 circularity caveat（optional）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 PARTIALLY RESOLVED: 引用已补全（Natarajan, Northcutt, DivideMix）。但缺一句解释 structured noise 为何超出 standard methods 假设。R2 建议降级为 Minor。\"\n  action_items:\n    - round: 24\n      action: \"§3.6 加一句解释 structured noise vs random noise 的区别（optional，降级为 Minor）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 STILL_OPEN: Algorithm 1 (main.tex L95) 仍使用 'modalities'。正文已统一为 'computation modes'。Trivial fix。\"\n  action_items:\n    - round: 24\n      action: \"Algorithm 1 'modalities' → 'computation modes'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24: §5 Non-triviality 段有效缓解但不消除。R1 Excitement 3.0, R2 Excitement 3.0。分歧在 Overall 权重（R1: 3.5, R2: 3.0）。不可通过 writing 修复——需新环境深度分析提升。\"\n\n- id: \"R19-W2\"\n  summary: \"Conclusion 过于简短——2 句话不匹配 long paper\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 分歧: R2 STILL_OPEN（~60 词偏短），R1 REBUT（ARR 无最低字数要求，且扩展会重新触发页数超限）。Director 判断：在 8 页预算下为 acceptable trade-off，降级为 Minor。\"\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"Anti-cherry-picking analysis 被列为优势。Scope limitation 已在正文声明。不再是 active concern。\"\n\n- id: \"R16-N3\"\n  summary: \"缺少 permadeath 环境 replication\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"连续多轮未提及。被 R16-N1 novelty concern 覆盖。\"\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§3.3 已报告 72B 完整 decomposition（DAF=92.4%, Δ_nd=+2.28）。多轮未提及。\"\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"连续多轮未提及。被 R20-N2 (4B contradiction) 取代并解决。\"\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"多轮未提及。Appendix L 引用 Figure 4 (signal_reversal.pdf)。\"\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 分歧: R2 PARTIALLY RESOLVED（(2)(3) 仍是 (1) 的应用）；R1 RESOLVED（递进结构是方法论文标准模式）。Director 判断：递进合理，不构成 active issue。降级为 Minor。\"\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"连续多轮未提及。\"\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§3.1 已充分讨论 binary structure（10/11 task types 100% death-asymmetry labels）。被 DAF framing 修正覆盖。\"\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R17-W2\"\n  summary: \"Figure 2 caption / readability 问题\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"视觉审查 R24 标注 Figure 2 标签字号偏小（~6-7pt）、轻微重叠（info 级）。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24: R1 认为递进清晰 (RESOLVED)，R2 认为 (2)(3) 仍依赖 (1)。分歧但非 blocking。合并 R16-W4。\"\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识: P-invariance by design 论证逻辑覆盖此 concern（agent 不观察 P，改变 P 不改变行为）。Appendix K analytical sensitivity 等价于实际实验。降级为 Minor → RESOLVED。\"\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n- id: \"R19-W3\"\n  summary: \"Routing 的 practical value 本身存疑——always-det 近最优\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"多轮未单独提及。被 framework meta-diagnostic value 讨论覆盖。\"\n\n- id: \"R19-M1\"\n  summary: \"62% tie rate (150/245) 含义未充分讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§3.1 已有 '150 (61.2%) are ties—indicating routing is relevant in only 38.8% of episodes'。多轮未提及。考虑 resolved。\"\n\n- id: \"R19-M3\"\n  summary: \"Table 1 weighting scheme（episode-weighted vs task-weighted）未明确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"Table 2 caption 已标注 'Episode-weighted mean scores'。多轮未提及。考虑 resolved。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "## Round 24 Review Issues (continue review, 2026-05-21)\n\n# =============================================\n# Resolved issues (confirmed in Round 24)\n# =============================================\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n# --- Round 24 newly confirmed resolved ---\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调 DAF 数值\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Abstract 以 78.9% label fraction 为 headline，DAF 降级为补充。§2.4 新增 Relationship 段落解释 DAF > label fraction 的代数原因。§3.1 声明 label fraction 为 primary diagnostic metric。\"\n  resolution: \"Label fraction 为 headline，DAF 为补充指标；§2.4 解释代数关系\"\n  resolution_round: 24\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: CI 修正为 [73.3%, 100.0%]（宽于 non-clustered [81.1%, 99.0%]，符合预期）；Appendix E 降级为 Sensitivity Analysis；non-clustered bootstrap 声明为 primary inference。\"\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Abstract concept-first 重组，关键数字精简至 3-4 个（78.9%, 88-90%, ~50-episode）。\"\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Ng 1999 (method.tex §2.4), Northcutt 2021 + DivideMix (experiments.tex §3.6) 已添加。\"\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: §5 Non-triviality 段列举三个 a priori 不可预测结果 (72B DAF=92.4%, Reflexion DAF>100%, 0.5B inverted-U)。R2 Excitement 从 2.5 上调至 3.0。\"\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Limitations 新增 Pure-strategy upper bound 段落，明确 DAF=90.4% 是 upper bound。\"\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: 'data scaling' 全局改为 'text augmentation'。\"\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: §3.1 明确量化 P=0 退化（51.2% label fraction）；区分 labeling function P-independence vs routing value 需 P>0。\"\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Bonferroni p<0.001, leave-one-task-type-out 49.2%, independent eval 47.1%。结论弱化为 'under current architectures and data regime'。\"\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: claim 弱化为 'under current architectures and data regime'。\"\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: 'plateau' → 'stabilization'/'no statistically detectable improvement beyond N=3'；minimum detectable effect ~8pp 报告。\"\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: PDF 确认 Conclusion 在 Page 8，Limitations 从 Page 9 起。\"\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"与 R18-N1 合并处理。RESOLVED。\"\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: 全文 grep 确认 'structurally determined' 已消除。§3.2 改为 'empirically dominated'。剩余 'structural' 用法均合理。\"\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: Table 2 caption 标注 'Per-task results are exploratory (n=20, power ≈ 50%); aggregate conclusions do not depend on individual task significance'。\"\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识 RESOLVED: huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确。\"\n  resolution: \"Orphan entries 清理，Webb 年份核实为 2023\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24: 全部已补。Ng 1999 和 Northcutt 2021 也已添加（合并 R13-W6）。\"\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"论文已有 Appendix Overview with hyperlinks（main.tex line 52-71）。多轮未提及。\"\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§3.1 已改为 'sole-signal labels' 并在上下文定义。多轮未提及。\"\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"Appendix N 已有 single annotator caveat。多轮未提及。\"\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§5 Anatomy of catastrophic failure 段已充分讨论。多轮未提及。\"\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"合并 R17-M1 解决。\"\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n# =============================================\n# Remaining open/in_progress issues\n# =============================================\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 PARTIALLY RESOLVED: Method §2.1 脚注已解释三种 deterministic 含义。但仅为脚注，未在正文段落或 §3.4 中显式讨论。R1 建议 §3.4 加交叉引用（~10 词），R2 偏好正文段落。共识：部分修复，建议加交叉引用。\"\n  action_items:\n    - round: 24\n      action: \"§3.4 开头加一句交叉引用脚注 1 的内容\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 MOSTLY RESOLVED: Limitations 量化了 0.3% 方向冲突 + 60.3% pre-event neutral。问题从 'label noise' 重新定义为 'granularity mismatch'。Appendix B circularity 微小残留。\"\n  action_items:\n    - round: 24\n      action: \"Appendix B 首句加 circularity caveat（optional）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 PARTIALLY RESOLVED: 引用已补全（Natarajan, Northcutt, DivideMix）。但缺一句解释 structured noise 为何超出 standard methods 假设。R2 建议降级为 Minor。\"\n  action_items:\n    - round: 24\n      action: \"§3.6 加一句解释 structured noise vs random noise 的区别（optional，降级为 Minor）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 STILL_OPEN: Algorithm 1 (main.tex L95) 仍使用 'modalities'。正文已统一为 'computation modes'。Trivial fix。\"\n  action_items:\n    - round: 24\n      action: \"Algorithm 1 'modalities' → 'computation modes'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24: §5 Non-triviality 段有效缓解但不消除。R1 Excitement 3.0, R2 Excitement 3.0。分歧在 Overall 权重（R1: 3.5, R2: 3.0）。不可通过 writing 修复——需新环境深度分析提升。\"\n\n- id: \"R19-W2\"\n  summary: \"Conclusion 过于简短——2 句话不匹配 long paper\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 分歧: R2 STILL_OPEN（~60 词偏短），R1 REBUT（ARR 无最低字数要求，且扩展会重新触发页数超限）。Director 判断：在 8 页预算下为 acceptable trade-off，降级为 Minor。\"\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"Anti-cherry-picking analysis 被列为优势。Scope limitation 已在正文声明。不再是 active concern。\"\n\n- id: \"R16-N3\"\n  summary: \"缺少 permadeath 环境 replication\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"连续多轮未提及。被 R16-N1 novelty concern 覆盖。\"\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§3.3 已报告 72B 完整 decomposition（DAF=92.4%, Δ_nd=+2.28）。多轮未提及。\"\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"连续多轮未提及。被 R20-N2 (4B contradiction) 取代并解决。\"\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"多轮未提及。Appendix L 引用 Figure 4 (signal_reversal.pdf)。\"\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 分歧: R2 PARTIALLY RESOLVED（(2)(3) 仍是 (1) 的应用）；R1 RESOLVED（递进结构是方法论文标准模式）。Director 判断：递进合理，不构成 active issue。降级为 Minor。\"\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"连续多轮未提及。\"\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§3.1 已充分讨论 binary structure（10/11 task types 100% death-asymmetry labels）。被 DAF framing 修正覆盖。\"\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R17-W2\"\n  summary: \"Figure 2 caption / readability 问题\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"视觉审查 R24 标注 Figure 2 标签字号偏小（~6-7pt）、轻微重叠（info 级）。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24: R1 认为递进清晰 (RESOLVED)，R2 认为 (2)(3) 仍依赖 (1)。分歧但非 blocking。合并 R16-W4。\"\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 共识: P-invariance by design 论证逻辑覆盖此 concern（agent 不观察 P，改变 P 不改变行为）。Appendix K analytical sensitivity 等价于实际实验。降级为 Minor → RESOLVED。\"\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n- id: \"R19-W3\"\n  summary: \"Routing 的 practical value 本身存疑——always-det 近最优\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"多轮未单独提及。被 framework meta-diagnostic value 讨论覆盖。\"\n\n- id: \"R19-M1\"\n  summary: \"62% tie rate (150/245) 含义未充分讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"§3.1 已有 '150 (61.2%) are ties—indicating routing is relevant in only 38.8% of episodes'。多轮未提及。考虑 resolved。\"\n\n- id: \"R19-M3\"\n  summary: \"Table 1 weighting scheme（episode-weighted vs task-weighted）未明确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"Table 2 caption 已标注 'Episode-weighted mean scores'。多轮未提及。考虑 resolved。\""
  }
}
```

</details>

---


### Tool result

_source line 1983 · 2026-05-21T07:10:12.263390+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 21190}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1984 · 2026-05-21T07:12:01.898886+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# Round 24 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR Long Paper, deadline 2026-05-25)\n**审稿模式**: Continue（基于 Round 23 修改验证）\n**Reviewer 编排**: 2 人 + 视觉审查 Agent\n- Reviewer 1: 方法严谨性 + 统计推断 + Router 实验 + noisy label\n- Reviewer 2: Framing 准确性 + 写作质量 + 格式合规 + 术语一致性\n\n---\n\n## Summary\n\nRound 24 为继续审稿，验证论文对 Round 20/23 提出的 4 项 Must-Fix 和 9 项 Should-Fix 问题的修改是否充分。论文在统计推断、framing 准确性、格式合规三个维度均有实质性改进。所有 4 项 Must-Fix 问题已解决（cluster bootstrap CI 修正、4B router 结论 qualified、页数收入 8 页、\"structurally determined\" 消除）。Should-Fix 中大部分已解决，3 项部分修复（跨环境定义仅脚注、noisy label 讨论缺一句、mislabeling circularity 微小残留），均可通过 1-2 句 editorial 修改关闭。核心 novelty concern（单环境深度分析的 excitement 上限）不可通过 writing 修复，需新环境深度分析。\n\n---\n\n## Strengths\n\n1. **统计方法论严谨度大幅提升** [共识，R1 Soundness 3.5→4.0，R2 同意]: Cluster bootstrap CI 从反常窄 [95.2%, 99.5%] 修正为合理的 [73.3%, 100.0%]，Appendix E 降级为 Sensitivity Analysis 并声明 non-clustered bootstrap 为 primary inference。4B router 结果获完整统计处理（Bonferroni 校正 p<0.001、leave-one-task-type-out 49.2%、independent eval 47.1%）。Per-task 结果标注为 exploratory（power ≈ 50%）。这些修正使论文的统计基础在 NLP 会议论文中属上乘。\n\n2. **Framing 一致性显著改善** [共识]: Label fraction 78.9% 确立为 primary headline，DAF 降级为补充指标。§2.4 新增 \"Relationship between DAF and label fraction\" 段落解释代数关系。\"Structurally determined\" 全文消除，改为 \"empirically dominated\"。Router 结论从 \"no learnable signal\" 弱化为 \"under current architectures and data regime\"。Dose-response \"plateau\" 改为 \"stabilization\"/\"suggestive evidence\"。Overclaim 系统性修正。\n\n3. **诊断框架的跨环境验证** [共识]: ScienceWorld (DAF=90.4%)、ALFWorld (DAF=0%, information asymmetry)、MATH (null result, p=0.81) 三个环境诊断出三种质性不同的 routing mechanism，证明框架的通用诊断能力而非特定环境的后见之明。\n\n4. **实验深度与可复现性** [共识]: 19 个 Appendix 覆盖 anti-cherry-picking analysis、leave-one-out stability、penalty sensitivity、seed robustness、extended validation、failure mode anatomy。Anti-cherry-picking 分析（excluded tasks ΔDR=+38.2pp > included +28.7pp）有效回应 selection bias 质疑。三个 model family (Qwen/Llama/Gemma) 跨架构验证 DAF 88-90% (spread 2.2pp)。\n\n5. **Limitations 段落质量** [共识]: 新增 pure-strategy upper bound 段落、P-invariance 适用范围量化、cluster bootstrap K<40 caveat、intervention ceiling caveat。四段结构覆盖 environmental scope、methodological constraints、statistical limitations、pure-strategy upper bound，坦诚且完整。\n\n---\n\n## Weaknesses\n\n### 核心 Weakness（不可通过 editorial 修复）\n\n1. **[W1] 核心 novelty/excitement 上限** [共识方向，程度分歧]\nDeath dominance 在 ScienceWorld 的 −100 penalty 下近似数学必然（DAF 是 δP/(δP+Δ_nd) 的代数后果）。§5 Non-triviality 段列举的三个 a priori 不可预测结果（72B DAF=92.4%, Reflexion DAF>100%, 0.5B inverted-U）有效缓解但不消除这一根本限制。框架 \"发现\" 的仍主要是奖励结构的推论。增加一个非 ScienceWorld 环境（如 NetHack/Crafter 的 death mechanism）的深度分析可显著提升 excitement。\nR1 Excitement 3.0, R2 Excitement 3.0（从 2.5 上调）。\n\n### 残留小问题（可通过 1-2 句话修复）\n\n2. **[W2] 跨环境 \"deterministic\" 定义仅在脚注** [共识 PARTIALLY RESOLVED]\nMethod §2.1 脚注 1 完整解释了三种 deterministic 含义，但脚注 visibility 不足。建议在 §3.4 开头加一句交叉引用（~10 词）即可。\n\n3. **[W3] Noisy label 讨论缺 structured noise 解释** [共识 PARTIALLY RESOLVED，降级为 Minor]\n§3.6 已引 Natarajan 2013、Northcutt 2021、DivideMix，但缺一句解释此处 noise 为 systematic（task-type-correlated）而非 random flip，超出 standard noisy-label methods 的 i.i.d. noise 假设。\n\n4. **[W4] Algorithm 1 术语残留** [共识 STILL_OPEN，trivial]\nmain.tex L95 Algorithm 1 `\\REQUIRE` 行仍使用 \"modalities\"，正文已统一为 \"computation modes\"。一词修改。\n\n5. **[W5] Appendix B mislabeling circularity 微小残留** [共识 MOSTLY RESOLVED]\nLimitations 已将问题从 \"label noise\" 重新定义为 \"granularity mismatch\"（0.3% 方向冲突，60.3% pre-event neutral）。Appendix B 用 episode labels 评估 step-level prediction 存在微小循环论证，建议首句加 caveat。\n\n---\n\n## Questions（已通过修改回答的问题）\n\n以下问题在 Round 20 提出，Round 24 确认已充分回答：\n\n1. P-invariance 适用范围？→ §3.1 量化 P=0 退化至 51.2%；labeling function P-independent，routing value 需 P>0。**已回答。**\n2. 4B router 59% 是 multiple comparison artifact？→ Bonferroni p<0.001，leave-one-task-type-out 49.2%，确认为 task-type classification。**已回答。**\n3. Penalty manipulation 实验？→ P-invariance by design（agent 不观察 P）使 analytical sensitivity 等价于实际实验。**已回答。**\n\n---\n\n## Missing References\n\nRound 20 标记的所有缺失引用已补全：\n- Ng et al. (1999) Policy Invariance Under Reward Transformations → method.tex §2.4 ✓\n- Northcutt et al. (2021) Confident Learning → experiments.tex §3.6 ✓\n- Li et al. (2020) DivideMix → experiments.tex §3.6 ✓\n- Altman (1999) Constrained MDPs → related_work.tex §4 ✓（Round 20 前已补）\n- Mihatsch & Neuneier (2002) Risk-sensitive RL → related_work.tex §4 ✓（Round 20 前已补）\n\n无新增缺失引用。\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 完成，0 critical / 1 warning / 5 info：\n\n- **[warning]** Page 1-2 连续纯文本无 figure/table，第一个 display item (Figure 1) 延迟到 Page 3。建议将 Figure 1 提前至 Page 2 加强第一印象。\n- **[info]** Figure 2 scatter plot task name 标注字号偏小（~6-7pt），部分标签轻微重叠。\n- **[info]** Table 1 仅 3 列 5 行，信息密度低。\n- **[info]** Table 2 \"†\" 符号含义仅在 caption 脚注中，快速扫描易遗漏。\n- **[info]** Figure 1 caption 未说明 \"Episode-level labels\" 具体含义。\n- **[info]** Page 8-9 Discussion+Conclusion+Limitations 连续纯文本，视觉单调。\n\n上述均为 presentation 建议，不影响评分。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings**\n\n| 维度 | Round 23 (R20 fresh) | Round 24 (continue) | 变化 |\n|------|---------------------|---------------------|------|\n| Soundness | 3.5 | **4.0** | 统计问题全部修正，overclaim 消除 |\n| Excitement | 2.5-3.0 | **3.0** | §5 Non-triviality 有效回应 |\n| Overall (R1) | 3.5 | **3.5** | Borderline Conference |\n| Overall (R2) | 3.0 | **3.0** | Solid Findings |\n\n### 评分分歧分析\n\nR1 (3.5) vs R2 (3.0) 的 0.5 分差距源于 **Soundness 与 Excitement 的权重分配**：\n- **R1 逻辑**: Must-Fix 全部解决 → Soundness 4.0 → 高执行质量部分补偿中等 novelty → Borderline Conference\n- **R2 逻辑**: Excitement 是独立维度 → Soundness 改善不改变 novelty 评判 → 核心发现仍是 penalty structure 推论 → Findings\n\n两者指向同一档位的不同端：Strong Findings / Borderline Conference。Director 判断：**采用 3.0 (Findings)**，理由：\n1. Excitement 共识 3.0，novelty concern 不可通过 writing 修复\n2. 单一主环境的深度分析 + boundary probes 的论文结构天然限制了 impact\n3. 论文的 Soundness 4.0 和 presentation 质量使其成为 **strong Findings candidate**\n4. 如增加第二个 death-mechanism 环境的深度分析，Overall 可升至 3.5\n\n### 修改建议优先级\n\n**提交前建议修复（~30 分钟工作量）：**\n1. Algorithm 1 \"modalities\" → \"computation modes\"（1 词修改）\n2. §3.4 开头加交叉引用脚注 1（~10 词）\n3. §3.6 加一句 structured noise 解释（~20 词）\n\n**如有时间（optional）：**\n4. Appendix B 首句加 circularity caveat\n5. Figure 2 标签字号调大 / 用 adjustText 避免重叠\n6. Figure 1 尝试提前至 Page 2\n\n---\n\n## Detailed Comments\n\n### 已解决的 Round 20 Must-Fix（确认关闭）\n\n| ID | 问题 | Round 24 状态 | 修改质量 |\n|----|------|--------------|---------|\n| R20-N1 | 正文超 8 页 | ✅ RESOLVED | Conclusion 在 Page 8 |\n| R13-N2 | Cluster bootstrap CI 反常收窄 | ✅ RESOLVED | CI [73.3%, 100.0%]，降级为 Sensitivity Analysis |\n| R20-N2/R18-N1 | 4B router vs non-learnability | ✅ RESOLVED | Bonferroni + leave-one-out + independent eval |\n| R20-N3 | \"structurally determined\" overclaim | ✅ RESOLVED | → \"empirically dominated\" |\n\n### 已解决的 Round 20 Should-Fix（确认关闭）\n\n| ID | 问题 | Round 24 状态 |\n|----|------|--------------|\n| R13-N1 | DAF framing | ✅ RESOLVED — label fraction 为 headline |\n| R13-W5 | Abstract 数字堆砌 | ✅ RESOLVED — concept-first，3-4 个数字 |\n| R13-W6 | Missing references | ✅ RESOLVED — Ng/Northcutt/DivideMix 已补 |\n| R14-W1 | Triviality risk | ✅ RESOLVED — §5 Non-triviality 段 |\n| R17-W1 | Pure-strategy upper bound | ✅ RESOLVED — Limitations 新段落 |\n| R17-W3 | Data scaling 术语 | ✅ RESOLVED — → text augmentation |\n| R18-W1 | Router claim 过强 | ✅ RESOLVED — \"under current architectures\" |\n| R18-W2 | Dose-response plateau | ✅ RESOLVED — → stabilization + MDE |\n| R20-W2 | Per-task not exploratory | ✅ RESOLVED — Table caption 标注 |\n| R17-M1 | Orphan bibs / Webb year | ✅ RESOLVED — 清理完毕 |\n| R17-N2 | P-invariance 范围 | ✅ RESOLVED — P=0 退化量化 |\n| R19-W1 | Penalty experiment | ✅ RESOLVED — P-invariance by design 覆盖 |\n\n### 部分解决（Minor 残留）\n\n| ID | 问题 | 状态 | 修复建议 |\n|----|------|------|---------|\n| R15-N2 | 跨环境 deterministic 脚注 | PARTIALLY | §3.4 加交叉引用 |\n| R20-W1 | Noisy label structured noise | PARTIALLY | §3.6 加一句解释 |\n| R15-W2 | Appendix B circularity | MOSTLY | 首句加 caveat |\n| R18-M1 | Algorithm 1 \"modalities\" | STILL_OPEN | 1 词修改 |\n\n### Round 24 改进总结\n\n论文在 Round 20→24 期间解决了全部 4 项 Must-Fix 和 12 项 Should-Fix 中的 12 项。Soundness 从 3.5 提升至 4.0。残留 4 项均为 Minor/editorial 级别，可在 30 分钟内修复。核心 novelty concern（单环境深度分析的 excitement 上限）是论文结构性限制，不可通过 writing 修复。Overall 维持 3.0 (Findings)，论文为 **strong Findings candidate**。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# Round 24 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR Long Paper, deadline 2026-05-25)\n**审稿模式**: Continue（基于 Round 23 修改验证）\n**Reviewer 编排**: 2 人 + 视觉审查 Agent\n- Reviewer 1: 方法严谨性 + 统计推断 + Router 实验 + noisy label\n- Reviewer 2: Framing 准确性 + 写作质量 + 格式合规 + 术语一致性\n\n---\n\n## Summary\n\nRound 24 为继续审稿，验证论文对 Round 20/23 提出的 4 项 Must-Fix 和 9 项 Should-Fix 问题的修改是否充分。论文在统计推断、framing 准确性、格式合规三个维度均有实质性改进。所有 4 项 Must-Fix 问题已解决（cluster bootstrap CI 修正、4B router 结论 qualified、页数收入 8 页、\"structurally determined\" 消除）。Should-Fix 中大部分已解决，3 项部分修复（跨环境定义仅脚注、noisy label 讨论缺一句、mislabeling circularity 微小残留），均可通过 1-2 句 editorial 修改关闭。核心 novelty concern（单环境深度分析的 excitement 上限）不可通过 writing 修复，需新环境深度分析。\n\n---\n\n## Strengths\n\n1. **统计方法论严谨度大幅提升** [共识，R1 Soundness 3.5→4.0，R2 同意]: Cluster bootstrap CI 从反常窄 [95.2%, 99.5%] 修正为合理的 [73.3%, 100.0%]，Appendix E 降级为 Sensitivity Analysis 并声明 non-clustered bootstrap 为 primary inference。4B router 结果获完整统计处理（Bonferroni 校正 p<0.001、leave-one-task-type-out 49.2%、independent eval 47.1%）。Per-task 结果标注为 exploratory（power ≈ 50%）。这些修正使论文的统计基础在 NLP 会议论文中属上乘。\n\n2. **Framing 一致性显著改善** [共识]: Label fraction 78.9% 确立为 primary headline，DAF 降级为补充指标。§2.4 新增 \"Relationship between DAF and label fraction\" 段落解释代数关系。\"Structurally determined\" 全文消除，改为 \"empirically dominated\"。Router 结论从 \"no learnable signal\" 弱化为 \"under current architectures and data regime\"。Dose-response \"plateau\" 改为 \"stabilization\"/\"suggestive evidence\"。Overclaim 系统性修正。\n\n3. **诊断框架的跨环境验证** [共识]: ScienceWorld (DAF=90.4%)、ALFWorld (DAF=0%, information asymmetry)、MATH (null result, p=0.81) 三个环境诊断出三种质性不同的 routing mechanism，证明框架的通用诊断能力而非特定环境的后见之明。\n\n4. **实验深度与可复现性** [共识]: 19 个 Appendix 覆盖 anti-cherry-picking analysis、leave-one-out stability、penalty sensitivity、seed robustness、extended validation、failure mode anatomy。Anti-cherry-picking 分析（excluded tasks ΔDR=+38.2pp > included +28.7pp）有效回应 selection bias 质疑。三个 model family (Qwen/Llama/Gemma) 跨架构验证 DAF 88-90% (spread 2.2pp)。\n\n5. **Limitations 段落质量** [共识]: 新增 pure-strategy upper bound 段落、P-invariance 适用范围量化、cluster bootstrap K<40 caveat、intervention ceiling caveat。四段结构覆盖 environmental scope、methodological constraints、statistical limitations、pure-strategy upper bound，坦诚且完整。\n\n---\n\n## Weaknesses\n\n### 核心 Weakness（不可通过 editorial 修复）\n\n1. **[W1] 核心 novelty/excitement 上限** [共识方向，程度分歧]\nDeath dominance 在 ScienceWorld 的 −100 penalty 下近似数学必然（DAF 是 δP/(δP+Δ_nd) 的代数后果）。§5 Non-triviality 段列举的三个 a priori 不可预测结果（72B DAF=92.4%, Reflexion DAF>100%, 0.5B inverted-U）有效缓解但不消除这一根本限制。框架 \"发现\" 的仍主要是奖励结构的推论。增加一个非 ScienceWorld 环境（如 NetHack/Crafter 的 death mechanism）的深度分析可显著提升 excitement。\nR1 Excitement 3.0, R2 Excitement 3.0（从 2.5 上调）。\n\n### 残留小问题（可通过 1-2 句话修复）\n\n2. **[W2] 跨环境 \"deterministic\" 定义仅在脚注** [共识 PARTIALLY RESOLVED]\nMethod §2.1 脚注 1 完整解释了三种 deterministic 含义，但脚注 visibility 不足。建议在 §3.4 开头加一句交叉引用（~10 词）即可。\n\n3. **[W3] Noisy label 讨论缺 structured noise 解释** [共识 PARTIALLY RESOLVED，降级为 Minor]\n§3.6 已引 Natarajan 2013、Northcutt 2021、DivideMix，但缺一句解释此处 noise 为 systematic（task-type-correlated）而非 random flip，超出 standard noisy-label methods 的 i.i.d. noise 假设。\n\n4. **[W4] Algorithm 1 术语残留** [共识 STILL_OPEN，trivial]\nmain.tex L95 Algorithm 1 `\\REQUIRE` 行仍使用 \"modalities\"，正文已统一为 \"computation modes\"。一词修改。\n\n5. **[W5] Appendix B mislabeling circularity 微小残留** [共识 MOSTLY RESOLVED]\nLimitations 已将问题从 \"label noise\" 重新定义为 \"granularity mismatch\"（0.3% 方向冲突，60.3% pre-event neutral）。Appendix B 用 episode labels 评估 step-level prediction 存在微小循环论证，建议首句加 caveat。\n\n---\n\n## Questions（已通过修改回答的问题）\n\n以下问题在 Round 20 提出，Round 24 确认已充分回答：\n\n1. P-invariance 适用范围？→ §3.1 量化 P=0 退化至 51.2%；labeling function P-independent，routing value 需 P>0。**已回答。**\n2. 4B router 59% 是 multiple comparison artifact？→ Bonferroni p<0.001，leave-one-task-type-out 49.2%，确认为 task-type classification。**已回答。**\n3. Penalty manipulation 实验？→ P-invariance by design（agent 不观察 P）使 analytical sensitivity 等价于实际实验。**已回答。**\n\n---\n\n## Missing References\n\nRound 20 标记的所有缺失引用已补全：\n- Ng et al. (1999) Policy Invariance Under Reward Transformations → method.tex §2.4 ✓\n- Northcutt et al. (2021) Confident Learning → experiments.tex §3.6 ✓\n- Li et al. (2020) DivideMix → experiments.tex §3.6 ✓\n- Altman (1999) Constrained MDPs → related_work.tex §4 ✓（Round 20 前已补）\n- Mihatsch & Neuneier (2002) Risk-sensitive RL → related_work.tex §4 ✓（Round 20 前已补）\n\n无新增缺失引用。\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 完成，0 critical / 1 warning / 5 info：\n\n- **[warning]** Page 1-2 连续纯文本无 figure/table，第一个 display item (Figure 1) 延迟到 Page 3。建议将 Figure 1 提前至 Page 2 加强第一印象。\n- **[info]** Figure 2 scatter plot task name 标注字号偏小（~6-7pt），部分标签轻微重叠。\n- **[info]** Table 1 仅 3 列 5 行，信息密度低。\n- **[info]** Table 2 \"†\" 符号含义仅在 caption 脚注中，快速扫描易遗漏。\n- **[info]** Figure 1 caption 未说明 \"Episode-level labels\" 具体含义。\n- **[info]** Page 8-9 Discussion+Conclusion+Limitations 连续纯文本，视觉单调。\n\n上述均为 presentation 建议，不影响评分。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings**\n\n| 维度 | Round 23 (R20 fresh) | Round 24 (continue) | 变化 |\n|------|---------------------|---------------------|------|\n| Soundness | 3.5 | **4.0** | 统计问题全部修正，overclaim 消除 |\n| Excitement | 2.5-3.0 | **3.0** | §5 Non-triviality 有效回应 |\n| Overall (R1) | 3.5 | **3.5** | Borderline Conference |\n| Overall (R2) | 3.0 | **3.0** | Solid Findings |\n\n### 评分分歧分析\n\nR1 (3.5) vs R2 (3.0) 的 0.5 分差距源于 **Soundness 与 Excitement 的权重分配**：\n- **R1 逻辑**: Must-Fix 全部解决 → Soundness 4.0 → 高执行质量部分补偿中等 novelty → Borderline Conference\n- **R2 逻辑**: Excitement 是独立维度 → Soundness 改善不改变 novelty 评判 → 核心发现仍是 penalty structure 推论 → Findings\n\n两者指向同一档位的不同端：Strong Findings / Borderline Conference。Director 判断：**采用 3.0 (Findings)**，理由：\n1. Excitement 共识 3.0，novelty concern 不可通过 writing 修复\n2. 单一主环境的深度分析 + boundary probes 的论文结构天然限制了 impact\n3. 论文的 Soundness 4.0 和 presentation 质量使其成为 **strong Findings candidate**\n4. 如增加第二个 death-mechanism 环境的深度分析，Overall 可升至 3.5\n\n### 修改建议优先级\n\n**提交前建议修复（~30 分钟工作量）：**\n1. Algorithm 1 \"modalities\" → \"computation modes\"（1 词修改）\n2. §3.4 开头加交叉引用脚注 1（~10 词）\n3. §3.6 加一句 structured noise 解释（~20 词）\n\n**如有时间（optional）：**\n4. Appendix B 首句加 circularity caveat\n5. Figure 2 标签字号调大 / 用 adjustText 避免重叠\n6. Figure 1 尝试提前至 Page 2\n\n---\n\n## Detailed Comments\n\n### 已解决的 Round 20 Must-Fix（确认关闭）\n\n| ID | 问题 | Round 24 状态 | 修改质量 |\n|----|------|--------------|---------|\n| R20-N1 | 正文超 8 页 | ✅ RESOLVED | Conclusion 在 Page 8 |\n| R13-N2 | Cluster bootstrap CI 反常收窄 | ✅ RESOLVED | CI [73.3%, 100.0%]，降级为 Sensitivity Analysis |\n| R20-N2/R18-N1 | 4B router vs non-learnability | ✅ RESOLVED | Bonferroni + leave-one-out + independent eval |\n| R20-N3 | \"structurally determined\" overclaim | ✅ RESOLVED | → \"empirically dominated\" |\n\n### 已解决的 Round 20 Should-Fix（确认关闭）\n\n| ID | 问题 | Round 24 状态 |\n|----|------|--------------|\n| R13-N1 | DAF framing | ✅ RESOLVED — label fraction 为 headline |\n| R13-W5 | Abstract 数字堆砌 | ✅ RESOLVED — concept-first，3-4 个数字 |\n| R13-W6 | Missing references | ✅ RESOLVED — Ng/Northcutt/DivideMix 已补 |\n| R14-W1 | Triviality risk | ✅ RESOLVED — §5 Non-triviality 段 |\n| R17-W1 | Pure-strategy upper bound | ✅ RESOLVED — Limitations 新段落 |\n| R17-W3 | Data scaling 术语 | ✅ RESOLVED — → text augmentation |\n| R18-W1 | Router claim 过强 | ✅ RESOLVED — \"under current architectures\" |\n| R18-W2 | Dose-response plateau | ✅ RESOLVED — → stabilization + MDE |\n| R20-W2 | Per-task not exploratory | ✅ RESOLVED — Table caption 标注 |\n| R17-M1 | Orphan bibs / Webb year | ✅ RESOLVED — 清理完毕 |\n| R17-N2 | P-invariance 范围 | ✅ RESOLVED — P=0 退化量化 |\n| R19-W1 | Penalty experiment | ✅ RESOLVED — P-invariance by design 覆盖 |\n\n### 部分解决（Minor 残留）\n\n| ID | 问题 | 状态 | 修复建议 |\n|----|------|------|---------|\n| R15-N2 | 跨环境 deterministic 脚注 | PARTIALLY | §3.4 加交叉引用 |\n| R20-W1 | Noisy label structured noise | PARTIALLY | §3.6 加一句解释 |\n| R15-W2 | Appendix B circularity | MOSTLY | 首句加 caveat |\n| R18-M1 | Algorithm 1 \"modalities\" | STILL_OPEN | 1 词修改 |\n\n### Round 24 改进总结\n\n论文在 Round 20→24 期间解决了全部 4 项 Must-Fix 和 12 项 Should-Fix 中的 12 项。Soundness 从 3.5 提升至 4.0。残留 4 项均为 Minor/editorial 级别，可在 30 分钟内修复。核心 novelty concern（单环境深度分析的 excitement 上限）是论文结构性限制，不可通过 writing 修复。Overall 维持 3.0 (Findings)，论文为 **strong Findings candidate**。"
  }
}
```

</details>

---


### Tool result

_source line 1985 · 2026-05-21T07:12:06.217686+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4318
}
```

</details>

---


### Assistant

_source line 1986 · 2026-05-21T07:12:14.858794+00:00_

Round 24 审稿报告已投递。

**结果摘要**：
- **Overall: 3.0/5 (Findings)**，Soundness 从 3.5 升至 4.0，Excitement 3.0
- Round 20 的 4 项 Must-Fix **全部解决**（页数、cluster bootstrap、4B router、overclaim）
- 12 项 Should-Fix 中 **12 项解决**，4 项 Minor 残留（Algorithm 1 术语、脚注交叉引用、structured noise 一句话、Appendix B caveat）
- R1 (3.5) vs R2 (3.0) 分歧记录在报告中，采用保守评分 3.0
- 提交前建议修复 3 项 trivial 修改（~30 分钟工作量）
- Issue tracker 已同步更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 162

## Round 162

2 recorded events


### User

_source line 1987 · 2026-05-21T07:12:16.366324+00:00_

[Reviewer 2 审稿结果]:


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1988 · 2026-05-21T07:12:28.180603+00:00_

Round 24 审稿已完成。

**结果**: Overall 3.0/5 (Findings)，Soundness 从 3.5 上调至 4.0。所有 4 项 Must-Fix 已解决，残留 4 项 Minor 级别问题（Algorithm 1 术语、脚注交叉引用、structured noise 一句话、Appendix B caveat），均可在 30 分钟内修复。审稿报告和 Issue Tracker 均已提交/更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 163

## Round 163

62 recorded events


### User

_source line 1989 · 2026-05-21T14:48:13.243646+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Interpretability and Analysis of Models for NLP
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1990 · 2026-05-21T14:48:19.941856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1991 · 2026-05-21T14:48:19.994462+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1992 · 2026-05-21T14:48:29.384446+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1993 · 2026-05-21T14:48:29.384820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1994 · 2026-05-21T14:48:33.049798+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1995 · 2026-05-21T14:48:34.305487+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 1996 · 2026-05-21T14:48:34.808446+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1997 · 2026-05-21T14:48:34.910926+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	\usepackage{tcolorbox}
18	\tcbuselibrary{listings,breakable}
19	
20	\hypersetup{pdfauthor={},pdftitle={}}
21	
22	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{related_work}
34	\input{discussion}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	\paragraph{Environmental scope.}
40	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) re
…[truncated 6856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1998 · 2026-05-21T14:48:34.911361+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1999 · 2026-05-21T14:48:34.961795+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2000 · 2026-05-21T14:48:41.189214+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2001 · 2026-05-21T14:48:42.143493+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 2002 · 2026-05-21T14:48:43.802221+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2003 · 2026-05-21T14:48:44.004519+00:00_

-rw-r--r-- 1 ubuntu ubuntu 601003 May 21 13:56 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool result

_source line 2004 · 2026-05-21T14:48:49.346477+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission guidelines:

## Key Author Instructions

Submissions must adhere to the formatting in the submission templates, which is available as an Overleaf template. Submissions are made in OpenReview.

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. The search resu
…[truncated 1264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 7202
}
```

</details>

---


### Tool result

_source line 2005 · 2026-05-21T14:49:01.357705+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

I found search results related to EMNLP 2026 an
…[truncated 8104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 20168
}
```

</details>

---


### Tool call

_source line 2006 · 2026-05-21T14:49:21.260048+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2007 · 2026-05-21T14:49:21.862972+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2008 · 2026-05-21T14:49:22.365328+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2009 · 2026-05-21T14:49:22.365793+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2010 · 2026-05-21T14:49:22.817936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2011 · 2026-05-21T14:49:23.321151+00:00_

1	\begin{abstract}
2	LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs.\ deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9\% of non-tie routing labels arise from death asymmetry: the internal strategy triggers catastrophic failure while the deterministic strategy survives. This finding is penalty-independent: a derived score-weighted measure, the Death Avoidance Factor, reaches 88--90\% across three model families (Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B), confirming convergence on a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), demonstrating the framework's generality. A ${\sim}$50-episode diagnostic pilot suffices to identify the dominant routing mechanism in a new environment, enabling informed build-vs-buy decisions before expensive router training.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2012 · 2026-05-21T14:49:23.421958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2013 · 2026-05-21T14:49:23.573110+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \citep{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone, as the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated), while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \citep{toolformer-2023} inserts API calls by perplexity reduction; ART \citep{art-2023} decomposes tasks into tool-augmented programs; Chameleon \citep{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \citep{cogrouter-2026,ares-2026}, model tiers \citep{mtrouter-2026}, or episode-level model selection under sparse rewards \citep{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. The shared assumption---that routing signal stems from diverse sources and a learned router can exploit it---remains untested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under ScienceWorld's penalty ($P{=}100$), DAF reaches $90.4\%$ (95\% CI: $[81.1\%, 9
…[truncated 2419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2014 · 2026-05-21T14:49:28.695240+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2015 · 2026-05-21T14:49:29.599294+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 132\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinis
…[truncated 1447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2016 · 2026-05-21T14:49:29.650281+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2017 · 2026-05-21T14:49:30.557392+00:00_

## Round 24 Review Issues (continue review, 2026-05-21)

# =============================================
# Resolved issues (confirmed in Round 24)
# =============================================

- id: "R13-N3"
  summary: "跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  resolution: "标题和 Contribution 措辞已恰当限定 scope"
  resolution_round: 15

- id: "R13-W1"
  summary: "正文篇幅严重不足 long paper 要求"
  category: format
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 14
  resolution: "正文已扩展至 8 页"
  resolution_round: 14

- id: "R13-W2"
  summary: "Router 训练实验存在多个 confound"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
  resolution_round: 15

- id: "R13-W3"
  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
  category: method
  severity: info
  status: resolved
  first_raised_round: 13
  last_seen_round: 14
  resolution: "Limitations 和 Appendix B 已充分量化"
  resolution_round: 14

- id: "R13-W4"
  summary: "SCI 方法贡献与实际使用不成比例"
  category: method
  severity: info
  status: resolved
  first_raised_round: 13
  last_seen_round: 14
  resolution: "SCI 已降级到 Appendix A"
  resolution_round: 14

- id: "R13-W7"
  summary: "Router negative results 解释不完整"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  resolution: "Router 实验定位为 diagnostic probe"
  resolution_round: 15

- id: "R13-m2"
  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 16
  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
  resolution_round: 16

- id: "R13-m3"
  summary: "Reference 格式不统一 + orphan entries"
  category: format
  severity: info
  status: resolved
  first_raised_ro
…[truncated 18845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 2018 · 2026-05-21T14:49:30.557963+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/config.yaml 2>/dev/null | head -80 || echo \"NO_CONFIG\"",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/config.yaml 2>/dev/null | head -80 || echo \"NO_CONFIG\"",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2019 · 2026-05-21T14:49:31.012460+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 2020 · 2026-05-21T14:49:31.063202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2021 · 2026-05-21T14:49:31.565940+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic}\footnote{The term ``deterministic'' denotes different information advantages across environments: in ScienceWorld, an oracle simulator providing ground-truth action outcomes; in MATH, a code interpreter verifying computations; in ALFWorld, admissible-action enumeration eliminating hallucination risk. These qualitative differences affect what routing signals the framework can detect.} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which computation mode to use at each step; our analysis investigates what signal is available to learn $\rho$.
10	
11	\subsection{Co
…[truncated 7550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2022 · 2026-05-21T14:49:31.566463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2023 · 2026-05-21T14:49:31.618103+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}).
5	
6	\subsection{Death Avoidance Decomposition}
7	\label{sec:death-decomp}
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=0.85\columnwidth]{figures/fig1_daf_scatter.pdf}
12	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$ (Spearman's $\rho = 0.986$; Appendix~\ref{app:per-task}), $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
13	\label{fig:decomposition}
14	\end{figure}
15	
16	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these 75, 54 are sole-signal labels (both strategies score zero without death, so death avoidance was the \em
…[truncated 15614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2024 · 2026-05-21T14:49:35.986649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2025 · 2026-05-21T14:49:36.439073+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	\emph{Self-supervised} approaches learn tool invocation from loss signals: Toolformer \citep{toolformer-2023} inserts API calls filtered by perplexity reduction; ToolACE \citep{toolace-2025} curates synthetic data for function-calling accuracy.
6	\emph{Token-level} methods embed tools into the model vocabulary: ToolkenGPT \citep{toolkengpt-2023} represents tools as special tokens resolved at inference.
7	\emph{Task-level} decomposition routes subtasks to specialized modules: ART \citep{art-2023} generates tool-augmented programs; Chameleon \citep{chameleon-2023} composes heterogeneous modules per subtask.
8	\emph{RL-based} methods learn routing policies from reward: ReTool \citep{retool-2025} discovers when code execution is preferable to chain-of-thought.
9	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
10	Concurrent work examines \emph{when} to invoke tools: tool-call decisions correlate with uncertainty~\citep{tool-overuse-illusion-2026}, are encoded in hidden states~\citep{when2tool-2026}, impose a ``tool-use tax''~\citep{tool-use-tax-2026}, or follow necessity-utility-affordability logic~\citep{to-call-or-not-2026}. Our decomposition yields a concrete answer: 78.9\% of non-tie routing labels trace to catastrophic-failure prevention.
11	
12	\paragraph{Adaptive Computation and Routing.}
13	Adaptive routing traces back to learned halting policies \citep{graves2016act}. In the LLM era, CogRouter \citep{cogrouter-2026} adapts reasoning depth per step, ARES \citep{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \citep{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \citep{mtrouter-2026} addresses multi-turn routing.
14
…[truncated 1785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2026 · 2026-05-21T14:49:36.439627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2027 · 2026-05-21T14:49:37.042427+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. The 4B router improves at episode level ($59.0\%$) without step-level gains ($56$--$59\%$), confirming task-type classification; cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}).
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), three specific consequences were not predictable a priori: (i)~$10{\times}$ scaling to 72B fails to eliminate it (DAF${}= 92.4\%$); (ii)~Reflexion self-correction yields DAF${}>100\%$, meaning death avoidance \emph{more} than accounts for the full gap; (iii)~a 0.5B model shows \emph{reduced} death rate ($13.3\%$; $n{=}15$) because it cannot reach dangerous states, suggestive of an inverted-U pattern. All four intervention axes leave ${\geq}12$~pp residual gaps to deterministic safety (Appendix~\ref{sec:threshold-routing}); cross-model stability ($36$--$43\%$ internal DR across three families) confirms death vulnerability is a task-environment property. More aggressive interventions remain untested, so we characterize a ceiling, not a universal bound.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of the answer-submission action (\texttt{focus on}) as a general interaction command. The internal strategy enters catastrophic states more frequently (105 vs.\ 40 deaths); grounding interventions reduce but do not eliminate death (Appendix~\ref{app:failure-modes}--\ref{app:grounding-ablation}).
12	
13	\paragraph{Practical implications.}
14	Death dominance diagnosis is actionable: a ${\sim}$50-episode pilot
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2028 · 2026-05-21T14:49:37.042850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2029 · 2026-05-21T14:49:37.093363+00:00_

1	\section{Conclusion}
2	
3	In ScienceWorld, death avoidance alone accounts for 78.9\% of non-tie routing labels, stable across three model families (DAF${=}88$--$90\%$); our episode-level counterfactual framework diagnoses this before any router is built, challenging the assumption of diverse signal sources. Cross-environment probes confirm generality; a ${\sim}$50-episode pilot suffices for build-vs-buy decisions in new environments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2030 · 2026-05-21T14:50:06.299873+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2031 · 2026-05-21T14:50:06.401571+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2032 · 2026-05-21T14:50:10.067883+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" -o -name \"projects.yaml\" 2>/dev/null | head -10",
  "description": "Find config files in workspace root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" -o -name \"projects.yaml\" 2>/dev/null | head -10",
    "description": "Find config files in workspace root"
  }
}
```

</details>

---


### Tool result

_source line 2033 · 2026-05-21T14:50:10.118775+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2034 · 2026-05-21T14:50:13.333023+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ 2>/dev/null",
  "description": "List project directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ 2>/dev/null",
    "description": "List project directory contents"
  }
}
```

</details>

---


### Tool result

_source line 2035 · 2026-05-21T14:50:13.383752+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
_paper_audit_result.json
artifacts
checkpoints
crafter_pilot
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
results
scripts
src
study_status.lock
task_context
tmp_unify_script.py
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2036 · 2026-05-21T14:50:16.448229+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_12/*.yml 2>/dev/null | head -10",
  "description": "Find YAML configs in workspace root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_12/*.yml 2>/dev/null | head -10",
    "description": "Find YAML configs in workspace root"
  }
}
```

</details>

---


### Tool result

_source line 2037 · 2026-05-21T14:50:16.498907+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2038 · 2026-05-21T14:50:19.625643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2039 · 2026-05-21T14:50:19.776893+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2040 · 2026-05-21T14:50:27.460238+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -name \"*.yaml\" -path \"*/config*\" -o -name \"settings.yaml\" -o -name \"project_config*\" 2>/dev/null | head -10 && find /home/ubuntu/agent-ml-research -name \"config*\" -type f 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -name \"*.yaml\" -path \"*/config*\" -o -name \"settings.yaml\" -o -name \"project_config*\" 2>/dev/null | head -10 && find /home/ubuntu/agent-ml-research -name \"config*\" -type f 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2041 · 2026-05-21T14:50:27.711719+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/secrets/simgate-modular-routing/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/resources.yaml
/home/ubuntu/agent-ml-research/.git/config
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/ldap3/utils/__pycache__/config.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/ldap3/utils/config.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/integration/sagemaker/__pycache__/config.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/integration/sagemaker/config.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/sdk/launch/agent/config.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/sdk/lib/__pycache__/config_util.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/sdk/lib/config_util.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2042 · 2026-05-21T14:50:30.573794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2043 · 2026-05-21T14:50:30.574274+00:00_

1	execution:
2	  account: root
3	  gpu_constraint:
4	  - autodl-simgate:cuda:0
5	  - autodl-simgate:cuda:1
6	  gpu_ids:
7	  - cuda:0
8	  project_path: /root/autodl-tmp/simgate-modular-routing
9	  servers:
10	  - westd-18266
11	feishu:
12	  chat_id: oc_f6bffc7e8351600df8091f08a63cd5a0
13	  operational_chat_id: oc_6551c2d0ac89db1b3b9e56f77fcf912d
14	  review_mode: fresh
15	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
16	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf
17	  review_round: 25
18	  review_supplementary_paths: ''
19	  submission_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c
20	project:
21	  created_at: '2026-05-13T04:23:23.832Z'
22	  description: 'SimGate: Learning When to Route LLM Agents to Deterministic Computation
23	    via Explicit Modular Gating'
24	  name: simgate-modular-routing
25	  phase: research
26	  source_idea_id: idea_010
27	venue: emnlp-2026
28	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2044 · 2026-05-21T14:50:46.842644+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "simgate-modular-routing",
  "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "simgate-modular-routing",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
  }
}
```

</details>

---


### Tool result

_source line 2045 · 2026-05-21T14:51:06.486389+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19643
}
```

</details>

---


### Tool call

_source line 2046 · 2026-05-21T14:51:06.839239+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n- **投稿类别**: Interpretability and Analysis of Models for NLP\n\n## Venue 要求\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **页数限制**: Long paper 8 页正文 + 无限参考文献\n- **Limitations**: 必需（≤1页，不计入页数限制）\n- **Ethics Statement**: 可选（不计入页数限制）\n- **模板**: ACL 2026 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（禁止出现作者姓名和自引暴露身份）\n- **评分标准**: 5=Consider for Award, 4=Conference（主会议接收）, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n**方法严谨性**：\n- 核心方法论（episode-level counterfactual framework、DAF decomposition）是否数学上正确、定义清晰\n- 统计推断方法是否恰当（bootstrap resampling、cluster analysis、CIs）\n- 实验结论是否有统计支撑，有无 overclaim\n- DAF 与 label fraction 的关系是否充分解释（是否存在 tautology）\n- Penalty-independence claim 是否站得住脚\n\n**实验设计**：\n- 实验设置是否充分（sample size、控制变量、baseline 选择）\n- Cross-model validation（Qwen/Llama/Gemma）设计是否合理\n- Agent improvement baselines（Retry/Reflexion/72B scaling）是否公平\n- Router training 负结果的解读是否合理\n- Cross-environment probes（MATH/ALFWorld）是否充分支撑泛化 claim\n- Task type selection（11/30）是否有 cherry-picking 风险\n- 可重复性：信息是否足以复现\n\n**格式检查**：\n- 正文是否在 8 页以内\n- Limitations 是否齐全\n- 引用格式是否统一\n\n请阅读完整论文后给出详细审稿意见，按以下结构：\n\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，重点，必须严格）\n4. **Questions**（需要作者澄清的）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Minor Issues**（格式、typo 等）\n7. **Overall Assessment**（评分 + 置信度 + 简要理由）\n   - Soundness: 1-5\n   - Excitement: 1-5\n   - Overall: 用 EMNLP 评分标准（1-5）\n   - Confidence: 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n- **投稿类别**: Interpretability and Analysis of Models for NLP\n\n## Venue 要求\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **页数限制**: Long paper 8 页正文 + 无限参考文献\n- **Limitations**: 必需（≤1页，不计入页数限制）\n- **Ethics Statement**: 可选（不计入页数限制）\n- **模板**: ACL 2026 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（禁止出现作者姓名和自引暴露身份）\n- **评分标准**: 5=Consider for Award, 4=Conference（主会议接收）, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n**方法严谨性**：\n- 核心方法论（episode-level counterfactual framework、DAF decomposition）是否数学上正确、定义清晰\n- 统计推断方法是否恰当（bootstrap resampling、cluster analysis、CIs）\n- 实验结论是否有统计支撑，有无 overclaim\n- DAF 与 label fraction 的关系是否充分解释（是否存在 tautology）\n- Penalty-independence claim 是否站得住脚\n\n**实验设计**：\n- 实验设置是否充分（sample size、控制变量、baseline 选择）\n- Cross-model validation（Qwen/Llama/Gemma）设计是否合理\n- Agent improvement baselines（Retry/Reflexion/72B scaling）是否公平\n- Router training 负结果的解读是否合理\n- Cross-environment probes（MATH/ALFWorld）是否充分支撑泛化 claim\n- Task type selection（11/30）是否有 cherry-picking 风险\n- 可重复性：信息是否足以复现\n\n**格式检查**：\n- 正文是否在 8 页以内\n- Limitations 是否齐全\n- 引用格式是否统一\n\n请阅读完整论文后给出详细审稿意见，按以下结构：\n\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，重点，必须严格）\n4. **Questions**（需要作者澄清的）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Minor Issues**（格式、typo 等）\n7. **Overall Assessment**（评分 + 置信度 + 简要理由）\n   - Soundness: 1-5\n   - Excitement: 1-5\n   - Overall: 用 EMNLP 评分标准（1-5）\n   - Confidence: 1-5"
  }
}
```

</details>

---


### Tool result

_source line 2047 · 2026-05-21T14:51:21.816564+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14977
}
```

</details>

---


### Tool call

_source line 2048 · 2026-05-21T14:51:21.917338+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 相关工作**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n- **投稿类别**: Interpretability and Analysis of Models for NLP\n\n## Venue 要求\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **页数限制**: Long paper 8 页正文 + 无限参考文献\n- **Limitations**: 必需（≤1页，不计入页数限制）\n- **Ethics Statement**: 可选（不计入页数限制）\n- **模板**: ACL 2026 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（禁止出现作者姓名和自引暴露身份）\n- **评分标准**: 5=Consider for Award, 4=Conference（主会议接收）, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n**新颖性与研究意义**：\n- 核心贡献（counterfactual diagnostic framework + death dominance finding）在 NLP/agent 领域是否有足够新颖性\n- 研究问题（\"what drives routing decisions\"）是否重要且 timely\n- 核心发现（78.9% death asymmetry）是否 trivial / obvious-in-hindsight\n- Contribution statement 是否 overclaim（特别是 generalizability claims）\n- 与 EMNLP \"Interpretability and Analysis\" track 的 fit 程度\n- 对 NLP community 的实际影响力和启发价值\n\n**完整性与写作质量**：\n- 论文叙事是否连贯（framework → finding → implications）\n- Abstract/Introduction 是否清晰传达核心信息\n- 三个 Contributions 是否独立且有力，还是彼此依赖\n- Discussion 是否充分讨论了 implications 和 limitations\n- Conclusion 长度和内容是否匹配 long paper\n- 整体写作质量（clarity、conciseness、logic flow）\n\n**相关工作**：\n- Related Work 覆盖是否全面（tool use、adaptive computation、counterfactual evaluation、safe RL）\n- 是否遗漏了重要的 concurrent/recent work\n- 与最近的 routing/tool-use 工作的 positioning 是否恰当\n- Safe RL 线是否讨论充分\n\n**Framing 审查**：\n- \"diagnostic framework\" vs \"empirical finding\" 的定位是否清晰\n- 跨环境 probes 是否过度 claim 为 \"generality\"\n- \"penalty-independent\" 表述是否准确\n\n请阅读完整论文后给出详细审稿意见，按以下结构：\n\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，重点，必须严格）\n4. **Questions**（需要作者澄清的）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Minor Issues**（格式、typo 等）\n7. **Overall Assessment**（评分 + 置信度 + 简要理由）\n   - Soundness: 1-5\n   - Excitement: 1-5\n   - Overall: 用 EMNLP 评分标准（1-5）\n   - Confidence: 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 相关工作**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n- **投稿类别**: Interpretability and Analysis of Models for NLP\n\n## Venue 要求\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **页数限制**: Long paper 8 页正文 + 无限参考文献\n- **Limitations**: 必需（≤1页，不计入页数限制）\n- **Ethics Statement**: 可选（不计入页数限制）\n- **模板**: ACL 2026 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（禁止出现作者姓名和自引暴露身份）\n- **评分标准**: 5=Consider for Award, 4=Conference（主会议接收）, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n**新颖性与研究意义**：\n- 核心贡献（counterfactual diagnostic framework + death dominance finding）在 NLP/agent 领域是否有足够新颖性\n- 研究问题（\"what drives routing decisions\"）是否重要且 timely\n- 核心发现（78.9% death asymmetry）是否 trivial / obvious-in-hindsight\n- Contribution statement 是否 overclaim（特别是 generalizability claims）\n- 与 EMNLP \"Interpretability and Analysis\" track 的 fit 程度\n- 对 NLP community 的实际影响力和启发价值\n\n**完整性与写作质量**：\n- 论文叙事是否连贯（framework → finding → implications）\n- Abstract/Introduction 是否清晰传达核心信息\n- 三个 Contributions 是否独立且有力，还是彼此依赖\n- Discussion 是否充分讨论了 implications 和 limitations\n- Conclusion 长度和内容是否匹配 long paper\n- 整体写作质量（clarity、conciseness、logic flow）\n\n**相关工作**：\n- Related Work 覆盖是否全面（tool use、adaptive computation、counterfactual evaluation、safe RL）\n- 是否遗漏了重要的 concurrent/recent work\n- 与最近的 routing/tool-use 工作的 positioning 是否恰当\n- Safe RL 线是否讨论充分\n\n**Framing 审查**：\n- \"diagnostic framework\" vs \"empirical finding\" 的定位是否清晰\n- 跨环境 probes 是否过度 claim 为 \"generality\"\n- \"penalty-independent\" 表述是否准确\n\n请阅读完整论文后给出详细审稿意见，按以下结构：\n\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，重点，必须严格）\n4. **Questions**（需要作者澄清的）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Minor Issues**（格式、typo 等）\n7. **Overall Assessment**（评分 + 置信度 + 简要理由）\n   - Soundness: 1-5\n   - Excitement: 1-5\n   - Overall: 用 EMNLP 评分标准（1-5）\n   - Confidence: 1-5"
  }
}
```

</details>

---


### Tool result

_source line 2049 · 2026-05-21T14:51:23.327316+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 2050 · 2026-05-21T14:51:43.379693+00:00_

**Round 1 已启动。** 当前状态：

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性 + 实验设计 | 🔄 审稿中 |
| Reviewer 2 | 新颖性 + 完整性 + 相关工作 | 🔄 审稿中 |
| Visual Check Agent | PDF 排版审查 | 🔄 进行中 |

外部审稿：未配置，跳过。

等待两名 Reviewer 返回初审意见后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 164

## Round 164

2 recorded events


### User

_source line 2051 · 2026-05-21T15:00:25.339155+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见 — Round 1

## 审查侧重：新颖性 + 完整性 + 相关工作

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Track**: Interpretability and Analysis of Models for NLP

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 实验执行扎实、统计分析透彻，但核心发现的新颖性有限——给定实验设置（oracle simulator vs. 会幻觉的LLM + 严厉的-100死亡惩罚），death dominance 是可预期的结果；框架本身是一个结构化的消融分析，conceptual novelty 不足以支撑主会议接收。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 统计方法论严谨（bootstrap CI、cluster-robust tests、leave-one-out sensitivity），decomposition 数学正确，但"框架通用性"的 claim 缺乏足够实证支撑 |
| Excitement | 2.5/5 | 核心发现（death dominance）在给定实验设置下可预期；框架的 conceptual contribution 有限；cross-environment probes 是退化情形（MATH 无信号、ALFWorld 信息不对称），未展示框架在非显然场景下的诊断价值 |
| Reproducibility | 4/5 | 详细的超参数报告、prompt templates（Appendix T）、agent inference 参数；承诺代码数据公开；唯一缺憾是 failure mode taxonomy 由单人标注无 inter-annotator agreement |
| Overall | 3.0/5 | Findings 水平——执行质量高但 contribution 的 impact 和 novelty 不足以进入主会议 |
| Confidence | 4/5 | 对 LLM agent、counterfactual evaluation、safe RL 领域较熟悉；仔细阅读了全文和所有 20 个 Appendix |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心发现的新颖性存疑——death dominance 在实验设置下是可预期的
- 具体位置：§1 Introduction, §3.1 Death Avoidance Decomposition, §5 Discussion "Non-triviality of death dominance"
- 问题：论文的 "deterministic" 策略使用 oracle simulator 提供 ground-truth state transitions，而 "internal" 策略依赖 LLM 自身推理（会幻觉）。在 ScienceWorld 的 -100 death penalty 设置下，oracle 策略天然比幻觉策略更安全。Death avoidance 成为 dominant routing signal 是这一不对等设置的直接后果，而非需要复杂框架才能发现的 insight。论文在 §5 试图论证 "non-triviality"（三点：72B 未消除、Reflexion DAF>100%、inverted-U），但这些是关于 death dominance 的 persistence，而非关于其 existence 的 surprise。一个合理的 null hypothesis 就是：当两种策略的根本区别在于 hallucination vs. ground truth 时，death-inducing hallucination 自然主导性能差异。
- 为什么影响接收：Excitement 是 EMNLP 接收的核心维度之一。如果核心发现是 "obvious in hindsight"，论文的主要价值就退化为 quantification（78.9%、DAF 88-90%），这降低了对 NLP 社区的启发价值。
- 建议修改方向：(a) 明确承认在 oracle vs. LLM 设置下 death dominance 的方向是可预期的，将贡献重心移向 quantification 和 intervention resistance；(b) 或在一个 death dominance 方向不显然的环境中验证框架（例如：两种策略都可能死亡但原因不同的环境）。

**N2** [critical] "框架通用性" 的 claim 缺乏实质性验证
- 具体位置：Abstract ("demonstrating the framework's generality"), §1 Contribution (3), §3.4 Cross-Environment Boundary Probes, Conclusion
- 问题：论文声称框架具有通用性，但三个测试环境中：(1) ScienceWorld 是唯一产生非平凡发现的环境；(2) MATH 显示无信号（84.4% no-preference），框架在此只是确认了一个 trivial null result；(3) ALFWorld 的 DAF=0%（无死亡机制）直接从定义得出，不需要运行框架也能预测。这意味着框架在 non-obvious 场景下的诊断价值完全未被验证。
- 为什么影响接收：如果贡献定位为 "diagnostic framework"，需要展示它在作者事先不知道答案的环境中也能产出有用诊断。三个环境中两个是退化情形，不构成通用性验证。
- 建议修改方向：降低 generality claim 的强度，将 MATH/ALFWorld 明确定位为 "boundary probes"（论文内文已经这么说了，但 Abstract 和 Conclusion 仍在 claim generality）；或增加一个框架能诊断出 non-obvious mechanism 的环境。

**N3** [critical] Contribution framing 不清晰——"diagnostic framework" vs. "empirical finding" 定位模糊
- 具体位置：§1 三条 contributions, Abstract
- 问题：三条 contribution 之间存在依赖关系而非独立。Contribution (1) 是框架本身；(2) 是将框架应用于 ScienceWorld 的发现；(3) 是 (2) 的 robustness check（cross-model + cross-environment）。如果框架的 novelty 不足（见 N1），那么整个贡献体系依赖于 empirical finding 的 surprise value。但 finding 又是可预期的（N1），形成循环。此外，框架本质上是：运行两种纯策略 → 比较 episode 结果 → 按 death/non-death 分解。这是一个结构化良好的消融设计，但作为独立的 "diagnostic framework" contribution，conceptual depth 有限。
- 为什么影响接收：三条 contribution 缺乏独立性使论文的 overall contribution 难以评估——reviewer 无法分别评价框架和发现。
- 建议修改方向：将贡献重组为 (1) 框架+方法论（简短）+ (2) 具体发现及其 quantification + (3) practical implications（decision framework）。明确哪部分是方法论贡献、哪部分是 empirical insight。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 63% 的任务类型被排除——虽有合理理由但显著限制了 scope
- 具体位置：§3 Experiments 开头, Appendix C (Table 2)
- 问题：11/30 task types 保留、19 排除（63%）。排除原因合理（dev set 5个、taxonomic redundancy 7个、agent floor 7个），anti-cherry-picking 分析也做了（excluded tasks 的 ΔDR 更高）。但这意味着论文的 quantitative conclusions 只基于 ScienceWorld 的 37% 任务空间。特别是 7 个 "agent floor" 任务的排除值得关注——这些任务中 agent 能力不足，可能代表了一个 death dominance 不成立的 regime（因为 agent 无法到达危险状态），但论文未讨论这种可能性。
- 建议：在 main text 中更显著地标注这一限制，讨论 agent floor 任务对 finding 的含义。

**W2** [warning] "penalty-independent" 表述具有误导性
- 具体位置：Abstract ("penalty-independent finding"), §1, §2.3 DAF definition
- 问题：论文将 78.9% label fraction 称为 "penalty-independent"，但在 §3.1 自己承认：at P=0, 54 个 sole-signal labels 变为 ties，non-tie labels 从 95 降至 41。这意味着 death avoidance 作为 routing signal 的实际 relevance 高度依赖 penalty magnitude——没有 penalty，death 就不是 "catastrophic" failure 而只是一个 binary outcome。Label fraction 的数值不依赖 P，但 labels 本身是否代表 meaningful routing signal 完全依赖 P。
- 建议：避免在 Abstract 和 Introduction 中使用 "penalty-independent" 作为 finding 的修饰语，改为更精确的表述如 "invariant to penalty magnitude in the labeling procedure"。

**W3** [warning] Conclusion 过于单薄
- 具体位置：§6 Conclusion（单段，3行）
- 问题：对于一篇 long paper（8页正文 + 20个 appendix），Conclusion 只有一段话，未讨论 broader implications、future work directions、或对 NLP community 的 takeaway。
- 建议：扩展至 2-3 段，覆盖：(a) 对 routing literature 的启示，(b) 何时框架可能失效的边界条件，(c) future directions（如在更多环境中验证、非 oracle 的 deterministic strategy 设计）。

**W4** [warning] Safe RL 相关工作覆盖不足
- 具体位置：§4 Related Work, "Safe RL" paragraph
- 问题：鉴于论文的核心发现是关于 catastrophic failure avoidance，Safe RL 段落只有 3 行，引用了 5 篇经典文献和 2 篇近期工作，过于简略。缺少对以下方面的讨论：(a) 为什么 safe RL 中已知的 "避免灾难性失败优先于奖励最大化" 的原则与本文发现的关系；(b) constrained MDP 文献中 death-avoidance 作为 hard constraint 的形式化与本文 DAF 度量的对比。
- 建议：扩展 Safe RL 段落，讨论 death avoidance 在 safe RL 理论框架中的定位，以及为什么本文的 empirical finding 对 safe RL 社区也有价值（或没有）。

**W5** [warning] Router negative result 的定位不够 sharp
- 具体位置：§3.6 Router Training, §5 Discussion "Why the router fails"
- 问题：Router 训练是一个 negative result（episode-level accuracy 47.1%，低于 always-deterministic baseline），论文在 §5 解释了原因（task-type-level binary signal）。但这个 negative result 的 implication 没有被充分 leveraged——它实际上是论文最有趣的 finding 之一：routing signal 如此集中于 death avoidance，以至于一个 learned router 无法超越 trivial baseline。建议将此更 prominently 框定为核心贡献的一部分，而非附属分析。
- 建议：在 contribution statement 中更明确地 frame 这个 negative result 的价值。

---

## Questions（需要作者澄清）

**Q1**: §2.3 中 DAF 公式的 footnote 2 提到当 Δ_nd < 0 时 DAF > 1。在 Reflexion 条件下 DAF > 100% (§3.3)。这是否说明 DAF 作为一个 metric 在边界条件下会产生不直观的值？是否有更 robust 的度量方式？

**Q2**: 论文使用 "deterministic" 来统称 ScienceWorld 的 oracle simulator、MATH 的 code interpreter、ALFWorld 的 admissible-action enumeration。这三者的 information advantage 性质完全不同（ground-truth state vs. computation verification vs. action enumeration）。这种统一命名是否会误导读者认为框架在 apples-to-apples 的比较中展示了通用性？

**Q3**: §3.1 报告 61.2% 的 episodes 是 ties。这意味着在大多数情况下，两种策略表现相同。这是否暗示 routing 本身在 ScienceWorld 中的价值极为有限（即使有完美 router，只能在 38.8% 的 episodes 中产生差异）？

**Q4**: Discussion §5 提到 0.5B 模型显示 "reduced death rate (13.3%, n=15)"，暗示 inverted-U pattern。但 n=15 的 pilot 是否足以支撑这一 claim？95% CI 会非常宽。

**Q5**: Failure mode analysis (Appendix N) 由单人标注，无 inter-annotator agreement。论文声明了这一点，但 Categories A/B/D/E 的区分在无 IAA 的情况下可信度如何？特别是 "Category B dominates" 的 claim。

---

## Missing References（遗漏的重要相关工作）

1. **Kumaraguru et al. (2025)** — "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety" (NeurIPS 2025 Workshop). 直接相关：研究 LLM agent 通过 "quitting" 机制避免灾难性行为，与本文的 death avoidance 概念高度一致。

2. **Step-level credit assignment 近期文献** — "From Reasoning to Agentic: Credit Assignment in RL for LLMs" (2026, arxiv:2604.09459)、"RTMC: Step-Level Credit Assignment via Rollout Trees" (2026, arxiv:2604.11037)、"Hindsight Credit Assignment for Long-Horizon LLM Agents" (2026, arxiv:2603.08754)。本文的 episode-level vs. step-level 信号分析与这一活跃研究线密切相关，应在 Related Work 中讨论。

3. **Agent-SafetyBench** (2024, arxiv:2412.14470) — 349 个交互环境的 LLM agent 安全评估 benchmark，提供了更广泛的 catastrophic failure 分类。

4. **RIDE: Route-Induced Density and Stability** (2026, arxiv:2603.29206) — routing-style prompts 对 LLM 内部状态的机制分析，与本文的 routing signal 分析互补。

---

## 小问题（不影响接收）

- §2.3 Equation (3)/(4): DAF 定义出现在两个等式中（一个是 1 - Δ_nd/Δ_full，一个是近似形式），建议合并为单个定义并标注近似条件。
- Table 1 (§3.5) caption 提到 "20-40 episodes per type" 但 Per-task decomposition (Appendix C) 显示只有 find-non-living-thing 有 40 episodes，其余都是 20。
- §1 Introduction 引用密度极高（第二段一次引用 11 篇），影响可读性。
- Appendix 编号从 A 到 T（20个），对 reviewer 和读者而言信息量过大。建议将次要分析合并或精简。
- §4 Related Work 中 Gajcin (2023) 在 OpenAlex 验证中未找到（confidence 0.78），建议核实引用信息。
- Bib 中有 8 个 orphan entries（在 .bib 中但未在正文引用），包括 balrog-2025, crafter-2022, crpo-2021 等，应清理。
- Webb (2023) 的年份在 OpenAlex 匹配为 2014，需核实哪个年份正确。

---

## 主要优势

1. **统计方法论一流**：Bootstrap CI、cluster-robust tests、leave-one-out sensitivity、wild cluster bootstrap、dose-response analysis——同类论文中罕见的统计严谨度。
2. **透明诚实**：论文对自身局限性的讨论异常坦诚——correlation 是 structural consequence、DAF 是 penalty-dependent、router 是 negative result、task exclusion 的完整分析。这种 intellectual honesty 值得赞赏。
3. **Multi-model validation 扎实**：三个架构不同的模型族（Qwen/Llama/Gemma）收敛于 DAF 88-90%（spread 2.2pp），加上 72B scaling，构成了 convincing 的 robustness evidence。
4. **Negative result 有价值**：Router 训练的 negative result（§3.6）本身是对社区有用的信息——表明在 death-dominated 环境中 learned routing 没有超越 trivial baseline 的空间。
5. **Practical decision framework**：Appendix R 的 50-episode pilot 诊断流程是可操作的 practical contribution。

---

## 评分总结

| 项目 | 评分 |
|------|------|
| Soundness | 4/5 |
| Excitement | 2.5/5 |
| Reproducibility | 4/5 |
| Overall Assessment | 3.0 (Findings) |
| Confidence | 4/5 |

**核心判断**：这是一篇 well-executed analysis paper，统计方法论和实验设计达到很高水准。但核心发现（death avoidance dominates routing signal）在给定实验设置下新颖性有限，"diagnostic framework" 的 claim 未通过 non-trivial environments 的验证。适合 Findings track，但 Excitement 不足以进入主会议。提升路径：(1) 在 death dominance 方向非显然的环境中验证框架，(2) 更 sharp 地 frame contribution 的边界。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2052 · 2026-05-21T15:00:32.974708+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 165

## Round 165

2 recorded events


### User

_source line 2053 · 2026-05-21T15:00:36.259968+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)。

核心判断：
- **Soundness 4/5**：统计方法论一流，decomposition 数学正确
- **Excitement 2.5/5**：核心发现（death dominance）在 oracle vs. hallucinating LLM 的设置下可预期；框架在 non-obvious 场景下的诊断价值未被验证
- **Overall 3.0**：执行质量高但 novelty/impact 不足以进入主会议

三个 Must-Fix 问题：
1. 核心发现在给定实验设置下 novelty 有限——oracle 天然比幻觉策略安全
2. "框架通用性" claim 仅靠两个退化环境（MATH 无信号、ALFWorld DAF=0%）支撑
3. 三条 contribution 缺乏独立性（framework → finding → robustness check 是层层依赖而非并列）

主要优势：统计严谨度罕见、对局限性的坦诚讨论、multi-model validation 扎实、router negative result 有价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2054 · 2026-05-21T15:00:43.489225+00:00_

Reviewer 2 审稿意见已收到（Overall 3.0 / Findings）。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 166

## Round 166

6 recorded events


### User

_source line 2055 · 2026-05-21T15:02:36.131613+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：Death Avoidance as the Dominant Routing Signal

## 1. Summary

本文提出 episode-level counterfactual framework，比较 LLM agent 在 pure-internal 与 pure-deterministic 策略下的表现差异，分解 routing signal 的来源。核心发现：在 ScienceWorld 的 11 类任务（245 episodes）中，78.9% 的 non-tie routing labels 源自 death asymmetry（internal 策略触发 −100 惩罚的灾难性失败，deterministic 不会）。引入 Death Avoidance Factor (DAF) 量化这一效应，跨三个模型家族（Qwen/Llama/Gemma）验证一致性，并在 MATH/ALFWorld 上做 cross-environment boundary probes。Router training 得到负结果，归因于 death avoidance 是 task-type-level 而非 step-level 信号。

## 2. Strengths

**S1. 研究问题有价值且切入角度新颖。** 现有 routing/tool-use 工作集中于"如何建 router"，本文退一步问"routing signal 到底是什么"，是一个被忽视的诊断性问题。这种"先理解再优化"的方法论对 agent routing 社区有指导意义。

**S2. 统计方法严谨。** Bootstrap resampling (B=10,000)、cluster bootstrap sensitivity (Appendix E)、Signal Concentration Index (SCI=0.21, Appendix A)、per-task CIs——统计工具链完整，远超多数 agent 论文的 reporting 标准。95% CIs 贯穿全文所有 quantitative claims。对 K=11 cluster bootstrap 的 power 问题也诚实讨论（Cameron et al., 2008 推荐 K≥20-30）。

**S3. Cross-model 验证有效。** Llama-3.1-8B (N=220, DAF=88.2%) 和 Gemma-2-9B-it 独立复制实验，三个模型家族方向一致（death dominance），排除了模型特异性解释。Appendix M 提供完整的 per-task 分解。

**S4. 负结果诚实且有价值。** §3.6 router training negative result 和 Appendix P 的 scaling ablation (0.6B→4B) 都表明 step-level router 无法捕获 task-type-level 信号。这是一个重要的实践性发现，能帮社区避免无效的 router 开发投入。Appendix P 的 generative router (46.7%) 进一步确认瓶颈在 signal 而非 architecture。

**S5. 附录极其详尽。** 15+ appendices 覆盖 task selection rationale (C)、correlation robustness (D)、penalty sensitivity (K)、failure mode taxonomy (N)、grounding ablation (O)、prompt templates (T) 等，可复现性极高。

**S6. Cross-environment probes 设计合理。** MATH (无 death mechanism, DAF=0) 和 ALFWorld (DAF=0, 信号来自 admissible-action access) 正确展示了 framework 在不同机制下的诊断能力（Figure 4, Table 14），避免了"one trick only"的批评。

## 3. Weaknesses

**W1 [Critical] DAF 度量的 tautological 倾向——核心发现的 novelty 被奖励结构预决定。**

DAF = Δ^death / Δ_full 在 ScienceWorld 的奖励结构下（death penalty P=−100, non-death scores 典型范围 0-29）几乎必然很高。任何存在 death asymmetry 的 episode，death 贡献的 score gap 远大于 non-death 差异，使 DAF→100% 成为数学必然而非经验发现。论文在 §2.4 承认 "DAF is a mathematical consequence rather than an empirical finding"，但 abstract 和 introduction 仍将 DAF 的高值作为核心贡献呈现（如 abstract: "the Death Avoidance Factor, a derived score-weighted measure, reaches 88-90% across three model families"）。

**真正有信息量的发现是 label fraction（78.9% 的 non-tie labels 存在 death asymmetry）**，而不是 DAF 本身。建议作者更清晰地区分：(a) death asymmetry 的 prevalence（empirical finding）和 (b) death asymmetry 一旦存在就必然支配 score gap（mathematical/definitional truth）。当前论文将二者混在一起，削弱了读者对 contribution novelty 的判断。

- 具体位置：Abstract, §2.4, §3.1, Conclusion
- 建议：明确将 label fraction 而非 DAF 作为 headline metric；在 §2.4 的 tautology 讨论后加入 "the empirically informative quantity is not DAF per se but the prevalence of death asymmetry" 的显式声明。

**W2 [Critical] 单环境局限性严重削弱泛化 claim。**

主实验仅在 ScienceWorld 一个环境上进行。MATH 和 ALFWorld 的 cross-environment probes **没有 death mechanism**（DAF=0），因此无法验证 death-dominance 发现是否泛化到其他有灾难性失败的环境（如 NetHack、WebArena、Crafter——bib 中都有但未实验）。论文 title 虽限定了 "on ScienceWorld"，但 §5 Discussion 和 Conclusion 中出现了超出 ScienceWorld scope 的泛化性暗示：

- §5 "the framework's generality applies to any environment with asymmetric fatal outcomes"（page 8）
- Conclusion: "our episode-level counterfactual framework diagnoses this before any router is built"

这些暗示没有在 ScienceWorld 之外的 death-containing 环境中得到验证。在至少一个有 catastrophic failure mechanism 的替代环境（如 NetHack 的 permadeath）上验证，才能支撑这些 claim。

- 具体位置：§3.4, §5, §6
- 为什么影响接收：reviewer 和 reader 难以判断 death dominance 是 ScienceWorld 的 artifact 还是 general phenomenon。

**W3 [Major] Task selection (11/30) 的 representativeness 论证不完整。**

虽然 Appendix C Table 4 显示 excluded tasks 的 death dominance 更强（Δ_DR=+39.2pp vs +28.7pp），排除了 cherry-picking，但 7 个 "near-zero progress" tasks 的排除理由值得 scrutiny：如果这些 tasks 对 both strategies 都太难，那它们代表了 agent capability boundary，这恰恰是 routing 最有价值的区域——也许 routing 在这些 tasks 上能从 deterministic 的局部进展中获益？论文没有展示这 7 个 tasks 的 raw scores 或 death rates，无法判断是否存在 non-zero routing signal。

- 具体位置：§3, Appendix C, Table 4
- 建议：提供 excluded "floor" tasks 的 per-task death rate 和 score 分布，论证其 routing signal 确实为零。

**W4 [Major] Router negative result 的替代解释不充分。**

§3.6 和 Appendix P 论证 router 失败是因为 signal 本身是 task-type-level。但替代解释未被充分排除：

(a) **训练数据规模过小**：总共 245 episodes，step-level 约 2,040 training steps (page 4)。对于一个 LoRA fine-tuning 任务，这是极小的训练集。论文虽测试了 text augmentation 到 800% (Table 11)，但 paraphrase-based augmentation 不等同于真实数据扩增。
(b) **Router 架构限制**：Qwen3-0.6B 和 Qwen3-4B (Appendix P) 是相对小的模型。更大的 router 或不同的 routing 表征（如 task embedding 而非 step-level text）可能表现不同。
(c) **训练目标设计**：router 试图从单步文本预测 episode-level 策略偏好，这本身是一个 label noise 极高的监督学习问题（97.4% 步骤两种策略结果一致→大部分标签是 noise）。也许 episode-level 特征（如 task description embedding）+ episode-level 标签的 router 能工作？

论文在 Appendix P 的 Practitioner Decision Framework (page 21) 提到了一些，但主文中的 claim "the routing bottleneck is signal-limited, not architecture-limited" (page 20) 过于绝对。

- 具体位置：§3.6, Appendix I, P
- 建议：(1) 承认训练数据规模的限制；(2) 测试 task-level router（以 task description 为输入，预测 task-level routing label）作为 positive control。

**W5 [Major] 实验规模偏小，per-task 统计 power 不足。**

每种 task type 仅 n=20 episodes（Table 3 显示最少 10 episodes, 最多 30）。对于 per-task-type 的 DAF 分解和 death-rate CIs，这导致极宽的置信区间。Table 7 (Appendix F) 显示部分 task types 的 per-task death rate CIs 跨越 20-30 pp。Appendix E 的 cluster bootstrap (K=11) 也因 K 太小而 power 不足。

论文诚实承认了这一点，但仍基于这些有限数据做了详细的 per-task 分析（Table 3, Table 4）。n=20 per task 的设计在 agent evaluation 文献中算正常，但对于本文的诊断性 claim 粒度，可能不够。

- 具体位置：§3, Appendix E-F
- 影响程度：moderate——aggregate claims (N=245) 有足够 power，但 per-task claims 的精度有限。

**W6 [Moderate] 实际指导价值有限。**

论文的 practical implication 主要是"先理解 signal 再建 router"，但除了指出 death avoidance 是主要信号外，没有给出 constructive 的解决方案。§5 提到 "combining DAF analysis with online policy learning is a natural next step" 但这是 vague 的方向指引。Appendix R 的 Practitioner Decision Framework 是有价值的尝试，但停留在 decision tree 层面，没有验证其有效性。

对于一篇 analysis paper 来说，读者期望 analysis 能产出 actionable insights。论文发现 router 失败后，一个自然期望是：那应该怎么办？Grounding ablation (Appendix O, 37% death reduction through prompting) 是一个好线索，但没有在主文中充分发展。

- 具体位置：§5, §6, Appendix O, R

## 4. Questions

**Q1.** Table 12 (Appendix K) 显示 P=0 时 DAF=7.4%，CIs 跨越零。在 P=0 时（即 death 不被惩罚），label fraction 如何变化？有多少 episodes 的 label 会翻转？这能量化 "penalty independence" claim 的 robustness。

**Q2.** 论文声称 97.4% 的步骤两种策略得分一致（§2.2）。那 2.6% 差异步骤的特征是什么？它们是否集中在特定 action types（如 focus_on）？这些步骤是否正是 death-triggering 步骤？

**Q3.** Grounding ablation (Appendix O) 通过 prompting 减少 37% death rate。如果将这种 death-aware prompting 应用到 internal 策略的所有 episodes，label fraction 和 DAF 如何变化？这能测试 death dominance 是否可通过简单干预消除。

**Q4.** 为什么不测试一个 task-level router（输入 task description，输出 routing decision）？如果 signal 确实是 task-type-level，这种 router 应该能工作，这既能验证论文的 claim，又能提供一个 constructive contribution。

**Q5.** Cross-model validation 中，Gemma-2-9B-it 的详细结果在 Appendix M，但主文只有一句话提及。Gemma 的 per-task DAF 分解是否与 Qwen/Llama 一致？是否有 task types 在不同模型间出现 label reversal？

## 5. Missing References

- **Pona et al. (2025), "Abstract Counterfactuals for Language Model Agents"** — 已引用（related work），这是最直接的 counterfactual analysis for agents 工作，论文对其的区分（episode-level vs abstract counterfactuals）可以更详细。
- **SWE-bench** (Jimenez et al., 2024) — 另一个有 catastrophic failure mode（破坏性代码编辑）的 agent benchmark，Discussion 中可作为 death-like failure 泛化讨论的参考。
- **AgentHarm** (Mazeika et al., 2024) — 关于 agent safety 和 catastrophic actions 的 benchmark，与 death avoidance 的 safety framing 相关。
- **ToolEmu** (Ruan et al., 2024) — 已引用，但论文可以更多讨论 ToolEmu 中发现的 catastrophic tool-use failure patterns 与 ScienceWorld death 的异同。

## 6. Minor Issues

- **M1.** 8 个 orphan bib entries（在 .bib 中但未引用）：balrog-2025, crafter-2022, crpo-2021, minihack-2021, nethack-2020, netplay-2024, tamar2015cvar, zhou2024webarena。应清理。
- **M2.** webb-2023 的年份与 OpenAlex 记录不符（bib 标注 2023，API 返回 2014）。请核实正确出版年份（可能是 working paper vs. journal version）。
- **M3.** Figure 1 (page 3) 的 pipeline overview 信息密度较高，建议增大字号或拆分为两个 subfigures。
- **M4.** §2.4 的数学推导中，DAF 的分母 Δ_full 在某些 episodes 可能为零（两个策略得分相同）。论文似乎通过排除 ties 处理了这一点，但应在正文中显式说明。
- **M5.** Appendix T 的 prompt templates 非常完整，有利于可复现性。建议补充 ScienceWorld 的具体版本号（v1.2.3 在 Appendix C 提到，确保一致）。

## 7. Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论总体正确，统计工具使用得当；但 DAF 的 tautological 倾向和 router negative result 的替代解释不充分扣分 |
| Excitement | 2.5/5 | 研究问题新颖但发现部分被奖励结构预决定；单环境 scope 限制影响力；实践指导有限 |
| Reproducibility | 4/5 | Appendix 极其详尽，prompt templates 完整，统计方法可复现；缺少代码发布 |
| Overall | **3.0** (Findings) | 扎实的诊断性分析工作，统计方法严谨，cross-model 验证有效，负结果有价值。但核心 DAF 发现的 novelty 被 ScienceWorld 奖励结构部分 trivialize，单环境泛化不足，实践影响有限。达到 Findings 水平但未达主会议标准。 |
| Confidence | 4/5 | 熟悉 agent evaluation、routing、counterfactual methods 和统计方法 |

**一句话总结**：方法严谨、分析深入的诊断性论文，但核心发现（death dominance of routing signal）在 ScienceWorld 的 −100 penalty 结构下有 tautological 倾向，单环境 scope 和有限的实践指导削弱了贡献度，建议 Findings 接收。

**关键修改建议**（如果 revision）：
1. 明确区分 DAF（definitional）和 label fraction（empirical）的 contribution 层级
2. 在至少一个有 catastrophic failure 的替代环境（如 NetHack）上验证 death dominance
3. 增加 task-level router 作为 positive control 实验
4. 在主文中更充分地发展 grounding ablation 的 implications


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2056 · 2026-05-21T15:03:21.863818+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见 — Round 1\n\n## 审查侧重：新颖性 + 完整性 + 相关工作\n\n## 总体评分\nOverall: 3.0 (Findings) | Soundness: 4/5 | Excitement: 2.5/5 | Reproducibility: 4/5 | Confidence: 4/5\n\n一句话总结: 实验执行扎实、统计分析透彻，但核心发现的新颖性有限——给定实验设置（oracle simulator vs. 会幻觉的LLM + 严厉的-100死亡惩罚），death dominance 是可预期的结果；框架本身是一个结构化的消融分析，conceptual novelty 不足以支撑主会议接收。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] 核心发现的新颖性存疑——death dominance 在实验设置下是可预期的\n- 论文的 \"deterministic\" 策略使用 oracle simulator 提供 ground-truth state transitions，而 \"internal\" 策略依赖 LLM 自身推理（会幻觉）。在 ScienceWorld 的 -100 death penalty 设置下，oracle 策略天然比幻觉策略更安全。Death avoidance 成为 dominant routing signal 是这一不对等设置的直接后果，而非需要复杂框架才能发现的 insight。§5 的 \"non-triviality\" 论证（72B 未消除、Reflexion DAF>100%、inverted-U）是关于 persistence 而非 existence 的 surprise。\n\n**N2** [critical] \"框架通用性\" 的 claim 缺乏实质性验证\n- 三个测试环境中：ScienceWorld 是唯一产生非平凡发现的环境；MATH 无信号（84.4% no-preference）；ALFWorld DAF=0%。框架在 non-obvious 场景下的诊断价值完全未被验证。Abstract 和 Conclusion 仍在 claim generality，但内文已承认 MATH/ALFWorld 是 \"boundary probes\"。\n\n**N3** [critical] Contribution framing 不清晰——三条 contribution 存在依赖关系而非独立\n- (1) 框架本身 → (2) 应用于 ScienceWorld 的发现 → (3) robustness check。如果框架 novelty 不足（N1），整个贡献体系依赖于 empirical finding 的 surprise value。框架本质上是结构化消融设计，conceptual depth 有限。\n\n## Should-Fix 问题\n\n**W1** [warning] 63% 任务类型被排除——7 个 \"agent floor\" 任务可能代表 death dominance 不成立的 regime\n**W2** [warning] \"penalty-independent\" 表述误导——P=0 时 54 个 sole-signal labels 变为 ties，routing signal 的实际 relevance 高度依赖 penalty magnitude\n**W3** [warning] Conclusion 过于单薄——long paper + 20 个 appendix，Conclusion 只有一段话\n**W4** [warning] Safe RL 相关工作覆盖不足——鉴于核心发现是 catastrophic failure avoidance，Safe RL 段落只有 3 行\n**W5** [warning] Router negative result 应被更 prominently frame 为核心贡献\n\n## Questions\nQ1: DAF>1 时的不直观值——是否有更 robust 的度量？\nQ2: \"deterministic\" 统称三种不同的 information advantage，是否误导？\nQ3: 61.2% ties 暗示 routing 本身价值极为有限？\nQ4: 0.5B inverted-U claim 基于 n=15 是否足够？\nQ5: Failure mode 单人标注无 IAA。\n\n## Missing References\n1. Kumaraguru et al. (2025) \"Check Yourself Before You Wreck Yourself\"\n2. Step-level credit assignment 近期文献 (2026)\n3. Agent-SafetyBench (2024)\n4. RIDE (2026)\n\n## Minor Issues\n- DAF 定义出现在两个等式中建议合并\n- Table 1 caption \"20-40 episodes\" 但实际只有一个 task 有 40\n- §1 引用密度极高\n- 20 个 Appendix 信息量过大\n- Gajcin (2023) 需核实\n- 8 个 orphan bib entries\n- Webb (2023) 年份需核实\n\n## 主要优势\nS1-S5: 统计方法一流、透明诚实、multi-model 扎实、negative result 有价值、practical decision framework\n\n---\n\n请对以上所有 Must-Fix（N1-N3）、Should-Fix（W1-W5）、Questions（Q1-Q5）、Missing References 逐一回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见 — Round 1\n\n## 审查侧重：新颖性 + 完整性 + 相关工作\n\n## 总体评分\nOverall: 3.0 (Findings) | Soundness: 4/5 | Excitement: 2.5/5 | Reproducibility: 4/5 | Confidence: 4/5\n\n一句话总结: 实验执行扎实、统计分析透彻，但核心发现的新颖性有限——给定实验设置（oracle simulator vs. 会幻觉的LLM + 严厉的-100死亡惩罚），death dominance 是可预期的结果；框架本身是一个结构化的消融分析，conceptual novelty 不足以支撑主会议接收。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] 核心发现的新颖性存疑——death dominance 在实验设置下是可预期的\n- 论文的 \"deterministic\" 策略使用 oracle simulator 提供 ground-truth state transitions，而 \"internal\" 策略依赖 LLM 自身推理（会幻觉）。在 ScienceWorld 的 -100 death penalty 设置下，oracle 策略天然比幻觉策略更安全。Death avoidance 成为 dominant routing signal 是这一不对等设置的直接后果，而非需要复杂框架才能发现的 insight。§5 的 \"non-triviality\" 论证（72B 未消除、Reflexion DAF>100%、inverted-U）是关于 persistence 而非 existence 的 surprise。\n\n**N2** [critical] \"框架通用性\" 的 claim 缺乏实质性验证\n- 三个测试环境中：ScienceWorld 是唯一产生非平凡发现的环境；MATH 无信号（84.4% no-preference）；ALFWorld DAF=0%。框架在 non-obvious 场景下的诊断价值完全未被验证。Abstract 和 Conclusion 仍在 claim generality，但内文已承认 MATH/ALFWorld 是 \"boundary probes\"。\n\n**N3** [critical] Contribution framing 不清晰——三条 contribution 存在依赖关系而非独立\n- (1) 框架本身 → (2) 应用于 ScienceWorld 的发现 → (3) robustness check。如果框架 novelty 不足（N1），整个贡献体系依赖于 empirical finding 的 surprise value。框架本质上是结构化消融设计，conceptual depth 有限。\n\n## Should-Fix 问题\n\n**W1** [warning] 63% 任务类型被排除——7 个 \"agent floor\" 任务可能代表 death dominance 不成立的 regime\n**W2** [warning] \"penalty-independent\" 表述误导——P=0 时 54 个 sole-signal labels 变为 ties，routing signal 的实际 relevance 高度依赖 penalty magnitude\n**W3** [warning] Conclusion 过于单薄——long paper + 20 个 appendix，Conclusion 只有一段话\n**W4** [warning] Safe RL 相关工作覆盖不足——鉴于核心发现是 catastrophic failure avoidance，Safe RL 段落只有 3 行\n**W5** [warning] Router negative result 应被更 prominently frame 为核心贡献\n\n## Questions\nQ1: DAF>1 时的不直观值——是否有更 robust 的度量？\nQ2: \"deterministic\" 统称三种不同的 information advantage，是否误导？\nQ3: 61.2% ties 暗示 routing 本身价值极为有限？\nQ4: 0.5B inverted-U claim 基于 n=15 是否足够？\nQ5: Failure mode 单人标注无 IAA。\n\n## Missing References\n1. Kumaraguru et al. (2025) \"Check Yourself Before You Wreck Yourself\"\n2. Step-level credit assignment 近期文献 (2026)\n3. Agent-SafetyBench (2024)\n4. RIDE (2026)\n\n## Minor Issues\n- DAF 定义出现在两个等式中建议合并\n- Table 1 caption \"20-40 episodes\" 但实际只有一个 task 有 40\n- §1 引用密度极高\n- 20 个 Appendix 信息量过大\n- Gajcin (2023) 需核实\n- 8 个 orphan bib entries\n- Webb (2023) 年份需核实\n\n## 主要优势\nS1-S5: 统计方法一流、透明诚实、multi-model 扎实、negative result 有价值、practical decision framework\n\n---\n\n请对以上所有 Must-Fix（N1-N3）、Should-Fix（W1-W5）、Questions（Q1-Q5）、Missing References 逐一回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2057 · 2026-05-21T15:03:44.937554+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23073
}
```

</details>

---


### Tool call

_source line 2058 · 2026-05-21T15:03:45.038689+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见\n\n## 总体评分\nOverall: 3.0 (Findings) | Soundness: 3.5/5 | Excitement: 2.5/5 | Reproducibility: 4/5 | Confidence: 4/5\n\n一句话总结：方法严谨、分析深入的诊断性论文，但核心发现（death dominance of routing signal）在 ScienceWorld 的 −100 penalty 结构下有 tautological 倾向，单环境 scope 和有限的实践指导削弱了贡献度。\n\n## Strengths\nS1. 研究问题有价值且切入角度新颖——\"先理解再优化\"的方法论\nS2. 统计方法严谨——Bootstrap (B=10,000)、cluster bootstrap、SCI、per-task CIs\nS3. Cross-model 验证有效——三个模型家族方向一致 (DAF 88-90%)\nS4. 负结果诚实且有价值——step-level router 无法捕获 task-type-level 信号\nS5. 附录极其详尽——15+ appendices 可复现性极高\nS6. Cross-environment probes 设计合理——展示了 framework 在不同机制下的诊断能力\n\n## Weaknesses\n\n**W1 [Critical] DAF 度量的 tautological 倾向**\n- DAF 在 ScienceWorld 的奖励结构下（P=−100, non-death scores 0-29）几乎必然很高，是数学必然而非经验发现\n- 论文在 §2.4 承认这一点但 abstract/introduction 仍将 DAF 高值作为核心贡献\n- 真正有信息量的是 label fraction (78.9%)，而非 DAF 本身\n- 建议：明确将 label fraction 而非 DAF 作为 headline metric\n\n**W2 [Critical] 单环境局限性严重削弱泛化 claim**\n- 主实验仅在 ScienceWorld 上进行\n- MATH 和 ALFWorld 没有 death mechanism (DAF=0)，无法验证 death-dominance 是否泛化到其他 catastrophic failure 环境\n- §5 和 Conclusion 出现了超出 ScienceWorld scope 的泛化性暗示\n- 需要在至少一个有 catastrophic failure 的替代环境上验证\n\n**W3 [Major] Task selection (11/30) representativeness 不完整**\n- 7 个 \"near-zero progress\" 任务可能代表 routing 最有价值的区域\n- 未展示这 7 个 tasks 的 raw scores 或 death rates\n- 建议：提供 excluded floor tasks 的 per-task death rate 和 score 分布\n\n**W4 [Major] Router negative result 替代解释不充分**\n- (a) 训练数据规模过小（245 episodes, ~2040 steps）\n- (b) Router 架构限制（0.6B-4B）\n- (c) 训练目标设计（step-level text → episode-level label）\n- \"signal-limited, not architecture-limited\" claim 过于绝对\n- 建议：测试 task-level router 作为 positive control\n\n**W5 [Major] 实验规模偏小，per-task 统计 power 不足**\n- 每 task type n=20 episodes，per-task CIs 跨越 20-30 pp\n- K=11 cluster bootstrap power 不足\n- aggregate claims (N=245) 有足够 power，但 per-task claims 精度有限\n\n**W6 [Moderate] 实际指导价值有限**\n- \"先理解 signal 再建 router\" 之外无 constructive 解决方案\n- Grounding ablation (37% death reduction) 未在主文充分发展\n- Appendix R Decision Framework 未验证有效性\n\n## Questions\nQ1. P=0 时 label fraction 如何变化？多少 episodes label 翻转？\nQ2. 2.6% 差异步骤的特征是什么？是否集中在 death-triggering 步骤？\nQ3. Grounding ablation 应用到所有 episodes 后 DAF 如何变化？\nQ4. 为什么不测试 task-level router？\nQ5. Gemma per-task DAF 是否与 Qwen/Llama 一致？有无 label reversal？\n\n## Missing References\n- Pona et al. (2025) 需更详细区分\n- SWE-bench (Jimenez et al., 2024)\n- AgentHarm (Mazeika et al., 2024)\n- ToolEmu (Ruan et al., 2024) 需更多讨论\n\n## Minor Issues\nM1. 8 个 orphan bib entries\nM2. Webb (2023) 年份核实\nM3. Figure 1 信息密度高\nM4. DAF 分母 Δ_full=0 的处理应显式说明\nM5. ScienceWorld 版本号一致性\n\n---\n\n请对以上所有 Weaknesses（W1-W6）、Questions（Q1-Q5）、Missing References 逐一回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见\n\n## 总体评分\nOverall: 3.0 (Findings) | Soundness: 3.5/5 | Excitement: 2.5/5 | Reproducibility: 4/5 | Confidence: 4/5\n\n一句话总结：方法严谨、分析深入的诊断性论文，但核心发现（death dominance of routing signal）在 ScienceWorld 的 −100 penalty 结构下有 tautological 倾向，单环境 scope 和有限的实践指导削弱了贡献度。\n\n## Strengths\nS1. 研究问题有价值且切入角度新颖——\"先理解再优化\"的方法论\nS2. 统计方法严谨——Bootstrap (B=10,000)、cluster bootstrap、SCI、per-task CIs\nS3. Cross-model 验证有效——三个模型家族方向一致 (DAF 88-90%)\nS4. 负结果诚实且有价值——step-level router 无法捕获 task-type-level 信号\nS5. 附录极其详尽——15+ appendices 可复现性极高\nS6. Cross-environment probes 设计合理——展示了 framework 在不同机制下的诊断能力\n\n## Weaknesses\n\n**W1 [Critical] DAF 度量的 tautological 倾向**\n- DAF 在 ScienceWorld 的奖励结构下（P=−100, non-death scores 0-29）几乎必然很高，是数学必然而非经验发现\n- 论文在 §2.4 承认这一点但 abstract/introduction 仍将 DAF 高值作为核心贡献\n- 真正有信息量的是 label fraction (78.9%)，而非 DAF 本身\n- 建议：明确将 label fraction 而非 DAF 作为 headline metric\n\n**W2 [Critical] 单环境局限性严重削弱泛化 claim**\n- 主实验仅在 ScienceWorld 上进行\n- MATH 和 ALFWorld 没有 death mechanism (DAF=0)，无法验证 death-dominance 是否泛化到其他 catastrophic failure 环境\n- §5 和 Conclusion 出现了超出 ScienceWorld scope 的泛化性暗示\n- 需要在至少一个有 catastrophic failure 的替代环境上验证\n\n**W3 [Major] Task selection (11/30) representativeness 不完整**\n- 7 个 \"near-zero progress\" 任务可能代表 routing 最有价值的区域\n- 未展示这 7 个 tasks 的 raw scores 或 death rates\n- 建议：提供 excluded floor tasks 的 per-task death rate 和 score 分布\n\n**W4 [Major] Router negative result 替代解释不充分**\n- (a) 训练数据规模过小（245 episodes, ~2040 steps）\n- (b) Router 架构限制（0.6B-4B）\n- (c) 训练目标设计（step-level text → episode-level label）\n- \"signal-limited, not architecture-limited\" claim 过于绝对\n- 建议：测试 task-level router 作为 positive control\n\n**W5 [Major] 实验规模偏小，per-task 统计 power 不足**\n- 每 task type n=20 episodes，per-task CIs 跨越 20-30 pp\n- K=11 cluster bootstrap power 不足\n- aggregate claims (N=245) 有足够 power，但 per-task claims 精度有限\n\n**W6 [Moderate] 实际指导价值有限**\n- \"先理解 signal 再建 router\" 之外无 constructive 解决方案\n- Grounding ablation (37% death reduction) 未在主文充分发展\n- Appendix R Decision Framework 未验证有效性\n\n## Questions\nQ1. P=0 时 label fraction 如何变化？多少 episodes label 翻转？\nQ2. 2.6% 差异步骤的特征是什么？是否集中在 death-triggering 步骤？\nQ3. Grounding ablation 应用到所有 episodes 后 DAF 如何变化？\nQ4. 为什么不测试 task-level router？\nQ5. Gemma per-task DAF 是否与 Qwen/Llama 一致？有无 label reversal？\n\n## Missing References\n- Pona et al. (2025) 需更详细区分\n- SWE-bench (Jimenez et al., 2024)\n- AgentHarm (Mazeika et al., 2024)\n- ToolEmu (Ruan et al., 2024) 需更多讨论\n\n## Minor Issues\nM1. 8 个 orphan bib entries\nM2. Webb (2023) 年份核实\nM3. Figure 1 信息密度高\nM4. DAF 分母 Δ_full=0 的处理应显式说明\nM5. ScienceWorld 版本号一致性\n\n---\n\n请对以上所有 Weaknesses（W1-W6）、Questions（Q1-Q5）、Missing References 逐一回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2059 · 2026-05-21T15:03:46.402194+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1363
}
```

</details>

---


### Assistant

_source line 2060 · 2026-05-21T15:03:49.560488+00:00_

Step 2 交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 167

## Round 167

2 recorded events


### User

_source line 2061 · 2026-05-21T15:03:52.094625+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心评判：

- **Overall: 3.0 (Findings)**，Soundness 3.5，Excitement 2.5，Confidence 4
- **主要问题**：(1) DAF 度量在 ScienceWorld 的 −100 penalty 结构下有 tautological 倾向，真正有信息量的是 label fraction 而非 DAF 本身；(2) 仅 ScienceWorld 单环境，cross-environment probes（MATH/ALFWorld）无 death mechanism，无法验证 death dominance 的泛化性；(3) router negative result 的替代解释（数据量不足、缺少 task-level router positive control）未充分排除；(4) 实践指导有限
- **主要优势**：研究问题切入角度新颖、统计方法严谨、cross-model 验证一致、负结果诚实有价值、附录极详尽

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2062 · 2026-05-21T15:03:57.263474+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 168

## Round 168

2 recorded events
