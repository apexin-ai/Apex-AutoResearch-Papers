---
round: 23
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T01:41:43.196241+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 20 审稿报告 — simgate-modular-routing

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (ARR Long Paper, deadline 2026-05-25)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人 + 视觉审查 Agent
- Reviewer 1: 方法严谨性 + 实验设计
- Reviewer 2: 新颖性 + 完整性

---

## Summary

本文提出一个 episode-level counterfactual 诊断框架，通过将 routing signal 分解为 death-avoidance 和 non-death 两个成分，诊断 modular LLM agent 中 routing 决策的驱动因素。应用于 ScienceWorld（11 task types，245 episodes，Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 来自 death asymmetry。跨模型验证（Llama-3.1-8B, Gemma-2-9B-it）和跨环境 boundary probes（MATH, ALFWorld）确认了框架的诊断能力。Router training 产生负结果，always-deterministic 匹配 96.3% 的 oracle 决策。

---

## Strengths

1. **统计方法论严谨**：四种独立检验（non-clustered bootstrap, wild cluster bootstrap, permutation test, sign test）交叉验证。Episode-level bootstrap (B=10,000) 提供可靠 CIs。统计基础在 NLP 会议论文中属上乘。[共识]

2. **Anti-cherry-picking analysis 堪称典范**：被排除的 19 个 task types 的 death asymmetry（mean ΔDR=+38.2pp）反而**强于**被纳入的 11 个 tasks（+28.7pp），有效排除 selection bias。Appendix S 扩展验证（n=20×5 tasks, DAF=0.991）进一步增强。[共识]

3. **Cross-model replication 有说服力**：三个架构族（Qwen/GQA, Llama/GQA, Gemma/SWA）独立复现 DAF 88-90%（spread 2.2pp），CIs 重叠，方向一致性 100%。72B scaling 确认持续性。[共识]

4. **负面结果诚实呈现**：Router training 负结果（§3.6）和 MATH null result（§3.4）未被掩盖，整合到框架诊断价值论证中。学术诚信度高。[共识]

5. **Appendix 极为详尽**：19 个 Appendices (A-S)，覆盖 labeling audit、correlation robustness、seed robustness、data scaling、penalty sensitivity、failure modes、grounding ablation 等。Reproducibility checklist 完整。[共识]

6. **可操作的 diagnostic pipeline**：Appendix R 三步决策框架（pilot→dominance check→decision）在 4/4 条件上 retrospective validation 正确。[共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, 强共识] **正文超出 8 页限制**
§5 Discussion 占满 page 8 双栏，§6 Conclusion 起始于 page 9（约 15 行）。正文超出约 0.3 页。EMNLP 2026 ARR 有 desk-reject 机制，Conclusion 属于正文。视觉审查也标记为 critical。
→ 压缩 §4 Related Work 或 §5 Discussion，将 Conclusion 收入 page 8。

**MF2** [critical, 强共识] **Wild cluster bootstrap CI 反常收窄，robustness check 提供 false assurance**
Non-clustered bootstrap CI = [81.1%, 99.0%]（宽度 17.9pp），wild cluster bootstrap (K=11) CI = [95.2%, 99.5%]（宽度 4.3pp）——cluster 方法反而收窄 4 倍。K < 20-30 时 wild cluster bootstrap 低估方差（Cameron et al. 2008, Webb 2023），论文自己引用了这些文献并在主文承认了 K 不足，但 Appendix E 仍以 "robustness check" 呈现更紧的 CI。
→ 移除 Appendix E CI 数值或降级为 acknowledged limitation；提供 ICC 估计；考虑 block bootstrap 替代。

**MF3** [critical, 强共识] **4B router episode-level 59.0% 与 "fundamental non-learnability" 结论矛盾**
Qwen3-4B 是所有模型中唯一突破 chance 的（59.0% ± 1.9%, p < 0.05），但论文未做 multiple comparison correction（4 scales × 2 granularities = 8 tests），也未分析 4B 的 per-task routing accuracy 以确定其是否仅捕获 task-type 信号。§3.6 末句 "leaving no learnable signal" 与此矛盾。R2 补充：Bonferroni 校正后可能仍显著（z ≈ 4.7, p < 0.001），需正面讨论。
→ 报告 corrected p-values；分析 4B per-task routing accuracy；qualify "non-learnability" 为 "在测试配置下未发现 step-level signal"。

**MF4** [critical, R2 提出 / R1 部分同意] **"Structurally determined" overclaim**
"Structurally determined" 在学术语境暗示因果机制，但支撑证据为 r=0.97 correlation。Task difficulty confound 未完全排除（within-task counterfactual 控制了单任务内差异，但 across-task 汇总中 death rate 和 difficulty 可能 co-vary）。论文在 §3.2 已 self-defuse r=0.97 为代数后果，但 §5 仍使用 "structurally determined"。
→ 改为 "empirically dominated" 或 "the dominant empirical predictor"。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, 强共识] **Abstract 数字堆砌**
约 250 词含 10+ 百分比数字，核心概念（counterfactual diagnostic, death avoidance routing）被数字淹没。
→ Concept-first 重组：保留 3-4 个关键数字（78.9%, cross-model 一致性, 50-episode pilot），其余移入 §1。

**SF2** [warning, 强共识] **DAF vs label fraction 关系解释不够直观**
DAF (90.4%) > label fraction (78.9%) 的差异来自 death episodes 的 score magnitude 放大（P=100 >> 典型 non-death gap ~29）。读者可能误以为两者是独立证据。
→ §2.4 或 §3.1 添加 1-2 句直觉解释。

**SF3** [warning, 强共识] **"Deterministic" 在三个环境中含义不同，缺显式讨论**
ScienceWorld = oracle simulator；MATH = code interpreter；ALFWorld = admissible-action enumeration。三种 "deterministic" 的 information advantage 质性完全不同。
→ §2.1 或 §3.4 添加概念对照表。

**SF4** [warning, 强共识] **Dose-response "plateau" 结论统计功效不足**
仅 5 个数据点 (N=1-5)，Wilson CIs 大量重叠。"Plateau" 与 "持续但缓慢下降" 在此 sample size 下无法区分。
→ 软化为 "no statistically detectable improvement beyond N=3"。

**SF5** [warning, 强共识] **Paraphrase augmentation ≠ genuine data scaling**
Data scaling ablation (25%-800%) 使用 synonym substitution + template variation，不产生新 routing patterns。是 expected null 非 informative null。
→ 重定位为 "text augmentation doesn't help"，明确区分于真实 data scaling。

**SF6** [warning, 强共识] **Noisy label learning 讨论不充分**
仅引用 Natarajan 2013，缺 Confident Learning (Northcutt 2021)、DivideMix 等后续方法。未讨论为何 modern noisy-label methods 不适用。
→ 深化讨论或补引用。

**SF7** [warning, 强共识] **Router "leaving no learnable signal" 措辞过强**
负结果仅基于 Qwen3 LoRA + generative router。未测试 lightweight classifier、feature-based router 等其他架构。
→ 弱化为 "current step-level routers fail to exploit the signal"。

**SF8** [warning, 强共识] **Pure-strategy 设计可能高估 death asymmetry（DAF=90.4% 是 upper bound）**
Pure-strategy 比较中 internal 策略始终承受 hallucination 风险。Mixed routing 中 router 可在 high-risk steps 切换到 deterministic，实际 death avoidance 贡献可能显著更低。
→ Limitations 明确 pure-strategy assumption 及其对 DAF 估计的 upward bias。

**SF9** [warning, 强共识] **Per-task n=20 导致 13/28 tasks 不显著，应标注为 exploratory**
n=20 对 20pp effect 的 power 仅 ~50%。主文 Table 3 无显著性标注或 CIs。
→ 标注 per-task 分析为 exploratory，添加 CIs。

### Minor

- Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager [R2, R1 确认]
- Webb (2023) 年份可能为 2014 working paper [R1+R2]
- §4 Related Work 仍使用 "modality"，与 §2 "computation mode" 不一致 [R2]
- Figure 2 尺寸偏小、点标签重叠 [R1+视觉审查]
- Appendix R 的 ~50 episodes / ~2 GPU-hours 是 ScienceWorld-specific 估计 [R2]
- Table 2 caption seed 说明不够清晰 [R1]

---

## Reviewer Consensus [AGREE]

1. **页数超限 desk reject 风险**：两位 Reviewer + 视觉审查三方确认。[MF1]
2. **Cluster bootstrap CI 收窄 = false assurance**：R1 首提，R2 完全同意。[MF2]
3. **4B router 结果需正面讨论**：R1 首提，R2 同意（补充 Bonferroni 后可能仍显著）。[MF3]
4. **"Structurally determined" 措辞过强**：R2 首提，R1 部分同意（counterfactual 设计部分控制 confound 但措辞仍需调整）。[MF4]
5. **DAF 代数放大成分**：两位 Reviewer 均指出 DAF 随 P 单调递增是代数后果，label fraction 78.9% 应为 headline。[SF2]
6. **Pure-strategy = DAF upper bound**：R1 提出，R2 称为"最有洞察力的问题"。[SF8]
7. **统计分析整体严谨**：两位均列为主要优势。
8. **Anti-cherry-picking 堪称典范**：两位均列为主要优势。
9. **三模型 replication 有说服力**：两位均列为主要优势。

---

## Reviewer Divergence [REBUT]

**Novelty / Excitement 评估**（核心分歧）
- **R2 (Excitement 2.5/5)**：Death dominance 在 ScienceWorld −100 penalty 下是 "数学上的近似必然"。72B DAF 增加恰支持 "penalty structure 不变→dominance 不变"。框架结论="这个环境不需要 routing"，贡献范围有限。
- **R1 (Excitement 3.0/5)**：部分 rebut——label fraction 78.9% 是 penalty-independent 经验发现；72B scaling 本可多样化 routing signal（但没有）；Reflexion DAF>100%（non-death regression）不可从 penalty structure 预测；三模型 DAF 88-90% 收敛是非平凡的 cross-architecture consistency。框架在 ALFWorld/MATH 上的 generality 有独立价值。

**Director 裁决**：方向共识（novelty 有限），程度分歧。R1 的 partial rebuttal 有理（label fraction、intervention resistance、cross-architecture consistency 非平凡），但 R2 的核心论点成立（核心 DAF 发现受环境设计制约，框架概念上 straightforward）。最终 Excitement 取 2.75，不足以支撑 Conference 接收。

**Contribution 1/2/3 独立性**
- R2 认为三个 contribution 非独立（C2/C3 是 C1 的应用结果），framework vs finding 摇摆。
- R1 认为三层递进关系清晰。
- Director：分歧非核心阻碍，不影响整体评估。

---

## Questions for Authors

1. **Cluster bootstrap ICC**：能否提供 intra-class correlation 估计以判断 task-type 聚类效应大小？[R1 首提, R2 同意]
2. **4B per-task routing accuracy**：4B 的 59.0% 是否来自 task-type 识别而非 step-level signal？能否做 per-task 分解？[R1 首提, R2 同意]
3. **Label fraction P-invariance 适用范围**：当 P→0 使 death episodes score 不再始终低于 non-death episodes 时，P-invariance 不成立。精确条件是什么？[R1 首提, R2 同意]
4. **环境层面 penalty manipulation**：Appendix K 仅改变 DAF 计算中的 P，未在 ScienceWorld 中实际改变 death penalty。如果 P 从 100 降至 10，agent behavior 可能改变，label fraction 是否仍 ~78.9%？[R2 首提, R1 同意]
5. **Pure-strategy vs mixed-strategy gap**：在 mixed routing 中，DAF 的实际值是多少？pure-strategy 设计是否系统性高估了 death avoidance 的贡献？[R1 首提, R2 强烈同意]
6. **Reflexion DAF > 100% 机制**：Δ_nd = −0.47 说明 Reflexion 在 non-death episodes 上引入了 regression。这是 overcompensation 还是其他原因？对 Reflexion 可靠性有何启示？[R2 首提, R1 同意]
7. **Prospective validation**：Appendix R 的 decision framework 仅做了 retrospective validation（4/4 conditions）。是否有可能在新环境上做 prospective validation？[R2 首提, R1 同意]

---

## Missing References

1. **Ng, Harada & Russell (1999)** — "Policy invariance under reward transformations"：Death dominance 本质上是 reward shaping 问题，应引用。[R2 首提, R1 同意]
2. **Northcutt, Jiang & Chuang (2021)** — "Confident Learning"：§3.6 讨论 noisy label 但仅引 Natarajan 2013，缺 modern methods。[R2 首提, R1 同意]
3. **Webb (2023) 年份核实**：需确认是 working paper 还是 journal publication。[R1+R2]

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置 external_review.paperreview_ai）。

---

## Visual Layout Check（非评分项）

**状态**: done（2026-05-21 01:19→01:23，耗时 ~4 min）

**Findings**:

| Severity | Finding |
|----------|---------|
| critical | 主文本延伸至第 9 页（§6 Conclusion 在 page 9 顶部），超出 EMNLP 8 页限制约 0.3 页 |
| warning | 前 2 页无视觉锚点，首个 display item (Figure 1) 直到 page 3 才出现 |
| warning | Pages 7-9 连续 3 页纯文本（Related Work→Discussion→Conclusion/Limitations），无 figure/table 穿插 |
| warning | Figure 2 尺寸偏小，打印后可读性不足 |
| info (×7) | Figure 1 pipeline 图设计合理；Figure 3 dose-response 清晰；Display items 集中在 pages 3-6 分布合理（0.56/页）；booktabs 表格排版专业；无 [?] 未解析引用；Margin 无溢出；行号存在 |

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

| 维度 | R1 | R2 | 加权评估 |
|------|------|------|---------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.75 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | 3.0 |

**置信度**: 4/5（两位 Reviewer 均报告 4/5）

**评分理由**：
- **方法论扎实**（Soundness 3.5）：框架设计有 principled justification，统计分析全面，cross-model replication 有说服力。但 cluster bootstrap CI 收窄、4B router 结果未解释、"structurally determined" overclaim 需要修正。
- **Novelty 受限**（Excitement 2.75）：核心发现（death dominance）受环境 penalty structure 制约——虽然 label fraction 78.9% 和 intervention resistance 是非平凡的经验发现，但框架概念上较为 straightforward，跨环境仅为 boundary probes 而非深度分析。
- **Reproducibility 优秀**（4.0）：Algorithm 1 完整，Appendix 详尽，承诺开源。
- **Findings 而非 Conference**：工作完整、统计严谨，但 novelty 和 breadth 不足以支撑主会议接收。若作者能 (a) 解决页数超限, (b) 修正统计呈现（cluster bootstrap, 4B router）, (c) 采用 framework-centric 叙事降低对 finding novelty 的依赖, (d) 补充至少一个中等 death regime 环境的深度分析，评分可上调至 3.5 (Borderline Conference)。

---

## Detailed Comments

### §1 Introduction
- Contribution 列表中 C2 和 C3 与 C1 的递进关系需更清晰——C1 是方法论，C2 是应用，C3 是 robustness check。当前呈现方式让 C2/C3 看起来像独立贡献。[R2-W2，R1 rebut]

### §2 Method
- §2.4 DAF 定义清晰，但 DAF > label fraction 的原因（score magnitude 放大）需直觉解释。[SF2]
- P-invariance 声明需明确适用条件（P 需足够大使 death episodes score 始终低于 non-death）。[R1-Q3]
- "Scope of episode-level analysis" 段落增强了方法论完整性。[正面]

### §3 Experiments
- §3.1: 78.9% label fraction 作为 headline metric 是正确选择，但应前移至段落首句（当前首句是 "Of the 95 non-tie routing labels"）。[SF2]
- §3.1: Per-task correlation r=0.97 已正确标注为 "mathematical consequence"——这是诚实的自我定位。[正面]
- §3.3: Reflexion DAF>100% 是有趣发现但 overcompensation 机制讨论较薄。[R2-Q4]
- §3.4: MATH/ALFWorld 定位为 "boundary probes" 恰当，但 "deterministic" 含义差异需显式讨论。[SF3]
- §3.6: "Router Training: A Negative Result" 标题诚实。但 4B 59.0% 结果与 "no learnable signal" 矛盾需正面讨论。[MF3]

### §4 Related Work
- Safe RL 段落已补 Altman (1999) 和 Mihatsch (2002)。[改善]
- 缺 reward shaping (Ng 1999) 和 Confident Learning (Northcutt 2021)。[Missing References]
- "modality" 术语遗留，应统一为 "computation mode"。[Minor]

### §5 Discussion
- "Why the router fails" 和 "Practical value as meta-diagnostic" 结构清晰。[正面]
- "Structurally determined" 需改为 "empirically dominated"。[MF4]
- Non-triviality 讨论可以更前置，直接回应 "obvious in hindsight" 的预期批评。[R14-W1]

### §6 Conclusion
- 仅 3 行，比 Round 19 略有扩展但仍偏短。更根本的问题是它导致了页数超限。[MF1]

### Limitations
- 三段结构（Environmental scope / Methodological constraints / Statistical limitations）清晰全面。[正面]
- 缺 pure-strategy assumption 对 DAF 估计的 upward bias 讨论。[SF8]

### Appendix
- A-S 共 19 个 Appendix，覆盖度极高。Appendix Overview with hyperlinks 增强导航。[正面]
- Appendix E (wild cluster bootstrap): CI 反常收窄需处理。[MF2]
- Appendix P (capacity scaling): 4B 结果需更多分析。[MF3]
- Appendix R (decision framework): 仅 retrospective validation，应标注。[Q7]