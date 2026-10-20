---
round: 26
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T22:28:26.200066+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Death Avoidance as the Dominant Routing Signal

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (via ACL Rolling Review) — Interpretability and Analysis track
**审稿模式**: Fresh review (Round 26)
**Reviewer 配置**: R1 (方法严谨性+实验设计, 3.5 Borderline Conference) / R2 (新颖性+完整性+相关工作, 3.0 Findings)
**交叉分享**: 1 轮交叉，关键问题达成高度共识（8 个 AGREE / 2 个 REBUT / 1 个 partial AGREE）

---

## Summary

论文提出 episode-level counterfactual diagnostic framework，通过纯策略比较分解 LLM agent routing 信号的构成。在 ScienceWorld（11 task types, 245 episodes）上发现 78.9% 的非 tie routing labels 源于 death asymmetry（内部策略因幻觉触发致命失败，确定性策略存活）。DAF（Death Avoidance Factor）在三个 7-9B 模型家族上达到 88-90%。跨环境 probes（MATH 无信号, ALFWorld 为 information asymmetry）展示了框架的诊断能力但同时表明 death dominance 是环境特定的。Router 训练产出 negative result（step-level balanced accuracy 56-59%）。

---

## Strengths

**S1. 实验设计的系统性和统计严谨性** [AGREE x2]
跨三个模型家族（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B）的一致性验证、跨三个环境的 probes、多项 ablation（text augmentation, grounding, capacity scaling, Reflexion, retry）。统计处理在 NLP 论文中属上佳水平：episode-level bootstrap (B=10,000)、cluster bootstrap、wild cluster bootstrap、leave-one-task-out sensitivity、Bonferroni correction、penalty sensitivity analysis。

**S2. 诚实的负面结果呈现** [AGREE x2]
Router training 低 accuracy（§3.6）、cross-environment probes 否定了 death dominance 的泛化性（§3.4）、text augmentation 无提升（Appendix J）均如实报告。论文在 MATH/ALFWorld 上的 "boundary probes" 定位是诚实的。

**S3. 写作质量** [AGREE x2]
8 页正文 + 20 个 Appendices（A-T）的安排合理。核心 claim 表述清晰，实验 narrative 流畅。Limitations 章节覆盖面好（5 个子段：环境范围、方法论约束、统计限制、pure-strategy upper bound、诊断范围）。

**S4. 可复现性** [AGREE x2]
Algorithm 1 伪代码、prompt templates（Appendix T）、router 训练配置（Appendix I）、per-task 分解（Appendix C）均有详细说明。Reproducibility 4/5。

**S5. 框架设计完整性** [R1 强调]
Episode-level labeling + DAF decomposition + SCI 三指标形成完整诊断工具链。Algorithm 1 的 edge case 处理（both-dead, both-alive-tied, score-comparison）thorough。Label quality audit（Appendix B）增加数据透明度。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. DAF "dominance" 由 penalty 幅度驱动，正文未充分反映 penalty sensitivity** [AGREE x2, critical]
- Table 12 (Appendix K): P=0 时 DAF=7.4%, P=10 时 DAF=39.8%, P=100 时 DAF=90.1%。DAF=90% 是 reward design 的产物（P=100 在 0-100 score range 内为极端惩罚），而非 routing 信号的内在属性。
- 78.9% label fraction（不受 penalty 加权影响）是更 robust 的指标，但论文在 Abstract/Introduction 仍以 DAF 88-90% 为 prominent metric。
- **需要**：(1) 正文 §3.1 或 §5 增加一段正面讨论 Table 12 含义；(2) 以 label fraction 为 primary claim，DAF 降级为补充。

**N2. 跨模型验证仅覆盖 7-9B 同级模型** [AGREE x2, critical]
- 三个模型参数量和内部死亡率高度相似（~42%），一致性更可能反映 7-9B tier 的共有特征而非跨规模 robustness。
- §3.3 报告 72B DAF=92.4%（死亡率 30.6% vs det 2.75%），但位于 Agent Improvement 段而非 Cross-Model 段，且未与 7-9B 结果并列讨论。
- **需要**：(1) 将 "cross-model family" 限定为 "within 7-9B tier"；(2) 72B 结果明确定位为 scaling analysis。

**N3. "Contradicting the routing literature's implicit assumption" 是 strawman framing** [AGREE x2, critical/strong warning]
- 被引 routing 工作（CogRouter, ARES, MTRouter, RouteLLM, Budget-Aware Routing）操作在 model selection、computational routing、multi-turn routing 等无 catastrophic failure 的 settings。
- ScienceWorld 的极端 catastrophic failure 使这里发现 death dominance 不构成对这些工作的 "contradiction"——论文自己的 ALFWorld 结果恰好支持了其他 settings 可能有多样化信号。
- R1 认为严重程度介于 Must-Fix 和 Should-Fix——本质是 wording 问题，可通过修改几句话解决。
- **需要**：将 "contradicting" 改为 "revealing that in catastrophic-failure environments, signal diversity may collapse to a single dominant factor"。

### Should-Fix（影响评分但不一票否决）

**W1. 框架方法论新颖性** [DIVERGENCE: R2 Must-Fix / R1 Should-Fix]
- R2：Algorithm 1 是 if-else 分类树，DAF 数学上平凡，未连接因果推断文献（Pearl/Rubin）。对 Interpretability and Analysis track，期望更形式化的工具。
- R1 反驳：Analysis track 的贡献标准是诊断性洞察而非数学框架新颖性。简单方法得出深刻洞察在 probing 文献中常见。DAF 简洁不等于平凡——它将模糊直觉量化为可比较指标。但同意在 Related Work 中应简要讨论与因果推断的关系。
- **建议**：Related Work 增加一段讨论与 potential outcomes (Rubin 1974) 的关系和区别。

**W2. Router negative result 解释不完整** [AGREE x2]
- 仅覆盖 single architecture family (Qwen3) + single training paradigm (LoRA) + 2,040 training steps。
- 未排除替代假设：模型容量不足、数据量不够、更好的训练方法（contrastive learning, different loss functions）可能成功。
- Oracle margin 仅 2.89 points，进一步降低 negative result 的诊断意义。
- **建议**：明确标注为 "preliminary negative result"；补充讨论替代训练方法。

**W3. ~50-episode pilot 缺乏 power analysis** [AGREE x2]
- 当前推理仅为 "ScienceWorld 效应极大（d=3.02）所以小样本可检测"，但新环境可能有更小效应。
- **建议**：补充 power analysis，或将 "suffices" 弱化为 "provides preliminary signal"。

**W4. Cluster bootstrap K=11 正文 caveat 不够** [AGREE x2]
- K=11 远低于 Cameron et al. (2008) 推荐的 K≥20-30。正文 §3.1 仅简短提及。
- **建议**：紧跟一句明确 caveat，引导读者主要依赖非聚类 bootstrap CI。

**W5. 11/30 task types 排除 (63%)** [AGREE x2]
- 7 个 agent-floor tasks（两策略均近零进展）可能代表 death dominance 不成立的 regime，但 Discussion 未讨论此含义。
- Appendix C/S 的排除验证部分缓解但不消除 selection bias 担忧。
- **建议**：Discussion 中补充讨论 agent-floor tasks 对 death dominance 的含义。

**W6. 跨环境 probes 深度不足** [AGREE x2]
- MATH 仅 aggregate-level 无 per-category 分解；ALFWorld 仅一段简短讨论。
- ALFWorld DAF=0% 实际上暗示不同环境由不同机制驱动——论文 reframe 为 "环境诊断框架揭示异质机制" 会比 "death avoidance 是主导" 更准确。
- **建议**：调整 Abstract/Introduction 避免暗示 generalizability。

**W7. 相关工作遗漏** [部分 AGREE]
- 因果推断基础（Pearl/Rubin potential outcomes）[AGREE x2]
- Agent safety catastrophic failure avoidance 方向 [R2 建议, R1 部分 AGREE]
- Credit assignment for LLM agents [R1 REBUT: SALT/CSO 已引用，覆盖面足够]

---

## Reviewer Consensus [AGREE]

1. **DAF vs label fraction 的主次定位**：label fraction 78.9% 是 penalty-invariant 的真正 empirical finding，DAF 88-90% 是 penalty-amplified 的补充指标。论文应调整 framing 权重。
2. **Framing overclaiming**：Abstract/Introduction 中的 generality claims 超出 ScienceWorld 单一环境的证据支撑。"Contradicting" routing literature 是 strawman。
3. **Cross-model 声明范围**：三个 7-9B 模型的一致性不足以声称 "cross-model family" 复制。
4. **Router negative result 定位**：应为 "preliminary" 而非 definitive non-learnability。
5. **统计 caveats**：K=11 cluster bootstrap、~50-episode pilot 均需更显著的 caveat。
6. **核心 novelty/excitement 限制**：death dominance 的方向在 oracle vs. hallucinating-LLM 设置下可预期。§5 Non-triviality 论证（72B persistence, Reflexion DAF>100%, inverted-U）关于 persistence 而非 existence。这是 Findings 而非 Conference 水平的核心原因，不可仅通过 writing 修复。

## Reviewer Divergence [REBUT]

1. **R2-N2（框架方法论新颖性是否为 Must-Fix）**：R2 认为 Algorithm 1 + DAF 缺乏技术深度，应连接 Pearl/Rubin 形式化框架。R1 反驳——Analysis track 贡献标准不要求数学框架新颖性，简单方法产出深刻洞察是常见且被接受的模式。R1 同意作为 Should-Fix（在 Related Work 中讨论因果推断关系）。
   - **Director 判断**：降为 Should-Fix。R1 对 track-specific 贡献标准的论证成立。但论文确实应补充与因果推断文献的连接。

2. **R2-W3（DAF 在 ScienceWorld 外 DAF=0 → metric 无独立价值）**：R1 反驳——DAF=0 在无死亡环境中是正确诊断结果，非指标缺陷。DAF 在其他 catastrophic-failure 环境（自动驾驶仿真、safety-critical RL）可非零。但 R2 的核心关切——论文未论证 DAF 在更广泛场景的价值——仍成立。

3. **R1-W5（分解公式近似误差）**：R2 澄清 episode-level 是 exact partitioning，但 penalty contribution 层面确有近似（忽略死亡前 partial scores）。论文 §2.3 报告残差 0.23（0.8% of Δ_full），近似质量在 P=100 时良好。降为 minor。

---

## Questions

1. §3.3 报告 72B DAF=92.4%——这比 7B 的 90.4% 还高。如果更大模型降低了死亡率但 DAF 反而上升，这是否意味着 death dominance 在更大模型上更极端？请讨论 72B 的 Δ_nd 值及其含义。
2. 61.2% 的 episodes 是 ties（两策略无差异）。这意味着 routing 最多改善 38.8% 的 episodes。论文是否应在 Discussion 中更显式地讨论 routing 的实际价值上限？
3. Algorithm 1 对 death-asymmetric episodes 直接赋予 preference label 而不比较 score。在 P < max_possible_partial_score 时此假设是否成立？
4. 论文 "counterfactual" 的使用是 potential outcomes 意义上的（两种 treatment 下的 outcome 比较），还是 Pearl 意义上的结构反事实？请在 Related Work 中明确。

---

## Missing References

- **Pearl (2009)** *Causality: Models, Reasoning, and Inference* — 论文大量使用 "counterfactual" 但未引用因果推断基础文献 [R1 R2 均建议]
- **Rubin (1974)** potential outcomes framework — 论文的纯策略比较本质上是 potential outcomes [R1 R2 均建议]
- **"Check Yourself Before You Wreck Yourself"** (arXiv 2510.16492) — LLM agent catastrophic failure avoidance [R2 建议]
- **Credit assignment for RL-based LLM agents** (arXiv 2604.09459) [R2 建议, R1 认为 SALT/CSO 已覆盖]

---

## External Review (Stanford Agentic Reviewer)

未配置。

---

## Visual Layout Check（非评分项）

**状态**: done (耗时 ~3.5 分钟)
**结果**: 0 critical / 3 warnings / 18 infos

**Warnings**:
1. **Pages 1-2 纯文本**：前 1.5 页无任何 display item，审稿人需阅读大量密集文字才能看到 Figure 1（page 3）。建议将 Figure 1（框架概览图）提前至 page 2。
2. **Page 5 纯文本**：前后页均有图表但 page 5 整页无 display item。correlation/sensitivity 分析适合用小型 summary table 打破单调。
3. **Pages 7-8-9 连续文字**：约 2.5 页无视觉刺激。Discussion 可考虑加入 summary figure 或 highlight box。

**其他**：主体正文 8 页共 5 个 display items（3 figures + 2 tables），密度 0.625/页，偏低但对诊断分析型论文尚可。未发现 [?] 未解析引用、LaTeX 渲染错误或 margin 溢出。正文 through Conclusion 在 page 8 结束，Limitations 在 page 9，符合 EMNLP 2026 的 8 页限制。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

论文在 ScienceWorld 环境内的实证分析扎实、统计处理严谨、负面结果如实呈现。主要问题在于：

1. **Novelty/Excitement 不足**（两位 Reviewer Excitement 2.5-3.0）：核心发现（oracle 策略比 hallucinating-LLM 策略更安全）的方向在 ScienceWorld 设置下接近可预期，§5 Non-triviality 论证关于 persistence 而非 existence。这是 Findings 而非 Conference 水平的核心原因，不可仅通过 writing 修复——需要额外环境的深度分析或根本性新发现。

2. **Framing overclaiming**：标题/Abstract 的 generality claims 超出单一环境的证据范围。"Contradicting routing literature" 是 strawman。DAF 88-90% 被 penalty 幅度驱动（P=0 时仅 7.4%）。这些通过 reframing 可部分缓解。

3. **Scope 限制**：单一环境（ScienceWorld, 11/30 task types）、同级模型（7-9B）、跨环境 probes 反而证明了 death dominance 不泛化。

**如果作者能够**：(a) 将 framing 从 "general routing finding" 调整为 "diagnostic framework + environment-specific case study"；(b) 正文正面讨论 penalty sensitivity；(c) 限定 cross-model 声明范围；(d) 补充因果推断文献连接——论文是一篇合格的 Findings 论文。达到 Conference 水准需要在至少一个额外 catastrophic-failure 环境上复现 death dominance。

**评分拆解** (EMNLP 2026 ARR):
| 维度 | 分数 | 说明 |
|------|------|------|
| Soundness | 3.5/5 | 框架在 ScienceWorld 内 sound；DAF penalty-sensitivity + generality claims 超出证据 |
| Excitement | 2.5/5 | 发现方向可预期；prevalence 量化有价值但不足以达到 Conference excitement |
| Reproducibility | 4/5 | 算法、配置、prompt 均有详细说明 |
| Overall | 3.0/5 | Findings — 实证扎实但新颖性有限、scope 受限 |

---

## Detailed Comments

### §1 Introduction
- "The shared assumption—that routing signal stems from diverse sources and a learned router can exploit it—remains untested" → 这是 strawman。被引工作在不同 settings 中确实有多样化信号。改为 "whether this assumption holds in environments with catastrophic failure modes remains untested"。
- Contribution (1) "episode-level counterfactual diagnostic framework" 的 generality claim 需限定。
- Contribution (2) 中的 router diagnostic 部分是最有实践价值的发现之一 [R1 R2 共识]，建议提升其 prominence。

### §2 Method
- §2.3 DAF 定义后应立即注明 DAF 对 P 单调递增，是数学性质而非经验发现。当前措辞 "DAF increases monotonically with P, a mathematical consequence" 存在但不够显著。
- 缺少与 potential outcomes framework 的连接（论文的纯策略比较本质上是 treatment effect 估计）。

### §3 Experiments
- §3.1: "150 (61.2%) are ties" 后的表述可能产生歧义。建议改为 "150 (61.2%) episodes show no preference; routing is relevant in the remaining 95 (38.8%)"。
- §3.2: "death dominance replicates across model families" 应限定为 "within the 7-9B tier"。三个模型 ~42% 内部死亡率的一致性更可能反映 tier 共性。
- §3.3: 72B DAF=92.4% 是重要数据点但仅在 Agent Improvement 段出现。建议在 §3.2 讨论或至少交叉引用。
- §3.4: MATH/ALFWorld probes 深度不足。MATH 缺少 per-category 分解。ALFWorld 的 information asymmetry finding 值得更多讨论——不同环境有不同 dominant mechanism 可能是比 death dominance 更有趣的框架级 contribution。
- §3.6: "A Negative Result" 标题低估了此发现的价值。Router 无法学习 task-type-level signal 有独立的实践意义 [R1 R2 共识]。应标注为 "preliminary"。

### §4 Related Work
- Safe RL 段需扩展：讨论 death avoidance 与 CMDP constraint satisfaction 的对应、为什么 Safe RL 方案不直接适用于 LLM agent routing。
- 缺少因果推断文献的讨论（Pearl/Rubin）。
- 考虑补充 agent safety catastrophic failure avoidance 方向文献。

### §5 Discussion
- "Non-triviality of death dominance" 段有效但论证的是 persistence/prevalence 而非 existence 的 surprise。
- 建议增加一段讨论 penalty sensitivity 的含义（引用 Table 12）。
- 建议讨论 agent-floor tasks 对 death dominance 不成立的 regime 意味着什么。

### §6 Conclusion
- 视觉审查确认正文 through Conclusion 在 page 8 结束——但 R1 报告末尾可能有 ~2 行溢出，需核查。

### Appendices
- 20 个 Appendices (A-T) 质量高，覆盖面广。特别是 Appendix R（Decision Framework）的 3 步流程有实践价值。
- Algorithm 1 应注明 death-priority 规则的隐含假设（P > max possible partial score）。

### 引用
- 5 条 not_found + 6 条 mismatch 多为 OpenAlex 索引问题。webb-2023 年份在 R25 已核实正确（CJE vol.56 no.3）。建议再次核查以确保一致。