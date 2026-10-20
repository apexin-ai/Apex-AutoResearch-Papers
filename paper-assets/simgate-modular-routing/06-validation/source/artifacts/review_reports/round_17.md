---
round: 17
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T11:29:49.107147+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 17 Consolidated Review Report (Fresh)

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**目标 Venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review May cycle)
**截止日期**: 2026-05-25
**审稿模式**: Fresh (完全独立初审)
**Reviewer 编排**: 2 人 (R1: 方法/实验/统计; R2: 新颖性/完整性/写作)

---

## Summary

本文提出 episode-level counterfactual diagnostic framework，通过 dual-metric 设计（penalty-independent label fraction 和 penalty-dependent DAF）分解 modular LLM agent 的 routing signal。在 ScienceWorld（11/30 task types, 245 episodes, Qwen2.5-7B）上发现 78.9% 的 non-tie routing labels 来自 death asymmetry（DAF = 90.4%）。跨模型（Llama-3.1-8B, N=220）和跨环境（MATH N=795, ALFWorld N=135）验证支持框架的诊断能力。四种 agent improvement 干预（retry, Reflexion, 10× scaling, action-space filtering）均未消除 death dominance。Router training 的 negative result 进一步验证了 routing 在 death-dominant 环境中的近退化性。

---

## Strengths

**S1. 方法设计干净，dual-metric 设计是核心方法论贡献。** 同时报告 penalty-independent label fraction (78.9%) 和 penalty-dependent DAF (90.4%)，并在 §2.4 主动标注 DAF 随 P 单调递增是 "mathematical consequence"。这种自我校正式的透明度在投稿论文中少见。[R1 S2, R2 同意]

**S2. Anti-cherry-picking 分析异常充分。** Table 5 展示 19 个被排除任务的 death-rate differential (mean +38.2 pp) 高于 included tasks (+28.7 pp)，直接排除 selection bias。[R1 S3, R2 同意]

**S3. 统计方法严谨度超出 NLP 论文平均水平。** Wild cluster bootstrap, exact permutation, sign test, LOO correlation, LOTO-DAF, 8-seed cross-validation, bootstrap CIs 形成完整的 robustness 论证链。[R1 S4, R2 优势段]

**S4. Negative results 解释自洽且具诊断价值。** Router episode-level failure (47.1±2.2%, below chance) 和 MATH null (p=0.81) 不是失败，而是框架诊断能力的正向验证。[R1 S5, R2 同意]

**S5. 多轴 agent improvement baselines 增强 robustness 论证。** Retry + Reflexion + 10× scaling + action-space filtering 四条独立干预路径，加上 dose-response analysis。[R1 S6]

**S6. Practitioner decision framework 有实际工程指导价值。** Discussion 的 50-episode pilot 建议 + MATH negative control 的验证 = 可操作的工程决策流程。[R2 优势段]

---

## Weaknesses (按严重程度排序)

### Critical (影响接收决定)

**C1. [Consensus] 78.9% label fraction 在 task level 是 binary split，aggregate 是 task composition artifact。**
LOTO-DAF (Appendix D) 揭示：移除唯一 death-free 任务后 DAF→100%。10 个 death-prone 任务各贡献 100% death-asymmetry labels，1 个 death-free 任务贡献 0%。headline 78.9% 是 10:1 task ratio 的直接产物，增减 death-free 任务即可任意改变该百分比。框架的真正诊断输出可能不是连续百分比而是 binary classification（"此环境是否 death-dominated"），但论文未讨论这一 structure。[R1-N1, R2-N1 强烈同意]

**C2. [Consensus] "penalty-independent" 表述具有误导性。**
72% 的 death-asymmetry labels (54/75) 在 P=0 时退化为 ties（surviving strategy 也 scored zero）。78.9% 是 labeling function 形式化产物；routing 的实际收益依赖 P>0。P=0 时 effective non-tie labels 仅 41 个，death-asymmetry fraction 降至 21/41=51.2%。需区分 labeling-function-level independence 和 practical-value-level dependence。[R1-N2, R2-N1 交叉同意]

**C3. [Consensus] 单一灾难性失败环境 + 单一失败模式，泛化性不足。**
100% 的 internal-strategy 死亡来自同一 action pattern（`focus on` 误用, Appendix H）。MATH 和 ALFWorld 均无 catastrophic death，不构成 death-dominance replication。论文自认 NetHack/Crafter 为 "most direct replication targets" 但未执行。无法区分这是 ScienceWorld idiosyncratic 结果还是可泛化现象。**补充第二个 permadeath 环境是从 Findings 提升至 Conference 的关键条件。** [R1-W5, R2-N2, 交叉后双方强烈同意]

**C4. [Consensus] 核心发现 novelty/excitement deficit。**
DAF = δP/(δP+Δ_nd) 在给定 δ=0.265, P=100, Δ_nd=2.84 后是代数必然。78.9% 本质上是 "多少 non-tie episodes 有 death asymmetry" 的重新表述。真正 non-trivial 的部分是 intervention robustness（Reflexion 仅降至 31.4%，72B 仅降至 34.5%），但论文 framing 将 discovery emphasis 放在 dominance 而非 persistence 上。[R2-N1, R1 交叉同意 framing 问题; R1 Excitement 3/5, R2 2.5/5]

### Warning (影响评分但不一票否决)

**W1. [Consensus] Abstract 数字堆砌。** ~140 词中 8+ 个数字，信息密度过高。建议保留 78.9%、DAF 90.4%、p=0.81 三个关键数字，其余改为定性描述。[R1 minor, R2-W1]

**W2. [Consensus] 72B 实验设计细节不完整。** Deterministic strategy 使用什么模型未说明；72B deterministic death rate 和 Δ_nd 未报告；72B vs 7B DAF 对比基于不同 task population (10 vs 11 tasks) 未标注。[R1-W3, R2-W3]

**W3. [Consensus] 跨环境 "deterministic" 模态定义不一致。** ScienceWorld (oracle simulator), MATH (code interpreter), ALFWorld (admissible actions) 三种 "deterministic" 质性不同。Table 2 caption 未标注 comparability limitation。[R2-W2, R1 partial agree]

**W4. [Consensus] Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响。** 42.9% internal death rate 是 worst-case；mixed-strategy 中偶尔切换 deterministic 可能大幅降低 death rate。DAgger 引用但未量化 transferability gap。[R1-W1, R2 同意]

**W5. [Consensus] Data scaling "structural failure" 结论基于 paraphrase augmentation 而非 real data。** 25%-800% scaling 不生成新 routing patterns，应弱化为 "failure under current data regime"。[R1-W6, R2 同意]

**W6. [Director 裁决] K=11 cluster 推断可靠性。** R1 标为 Must-Fix，R2 rebut 降为 Should-Fix（Cohen's d=3.02, exact permutation p=0.002 不依赖 asymptotic assumptions）。**Director 裁决：Warning。** 方向性结论 robust，magnitude 精度有限但 CI 下界 73% 仍排除 50%。建议将 Cohen's d 提升至正文。

**W7. [Director 裁决] Contribution 2 过载。** R2 标为 Must-Fix，R1 rebut 为 editorial。**Director 裁决：Warning。** 合理关切但不影响接收。建议将 router-as-diagnostic-probe 移入 Contribution 1。

### Minor

**M1.** Figure 1 (scatter) caption 缺 "mathematical consequence" caveat。[R1-W2, R2 同意]
**M2.** Related Work 第一段 6 citations 连续列举，应按功能类别重组。[R2-W5, R1 同意]
**M3.** Orphan bib entry (altman1999cmdp)；ART 等条目需更新为正式出版信息。[R2 格式]
**M4.** Abstract 中 "Retry yields only marginal reduction (43.5%)" 括号内是 post-retry death rate 非 reduction 量，首次阅读有歧义。[R1 minor]

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉回应后达成一致：

1. **[AGREE] 78.9% binary task-level structure** — aggregate 是 task composition artifact，需在正文讨论
2. **[AGREE] "penalty-independent" 误导** — P=0 时 72% labels 退化为 ties，需区分形式化 vs 实用价值
3. **[AGREE] 缺少第二个 permadeath 环境** — Conference vs Findings 的关键分水岭
4. **[AGREE] Novelty framing 问题** — 应从 "death dominates" 转向 "death dominance resists interventions"
5. **[AGREE] Abstract 数字堆砌** — 保留 2-3 个关键数字
6. **[AGREE] 72B 实验细节不完整** — 需澄清 deterministic model、报告完整 decomposition
7. **[AGREE] Related Work 罗列** — 需按功能类别重组

---

## Reviewer Divergence

| 问题 | R1 | R2 | Director 裁决 |
|------|----|----|---------------|
| K=11 cluster 推断 | Must-Fix (CI 过宽) | Should-Fix (Cohen's d 足够) | **Warning** — 方向性 robust，提升 Cohen's d 至正文 |
| Contribution 2 过载 | Editorial, not critical | Must-Fix | **Warning** — 建议重组但非 critical |
| MATH tautological? | Rebut (有效 boundary probe) | Tautological | **R1 正确** — p=0.81 是具体实证，但需标注模态差异 |
| 27.7% mislabeling 影响 78.9%? | 需讨论 | 不影响 (episode-level) | **R2 正确** — 78.9% 是 episode-level metric |

---

## Questions for Authors

**Q1.** [R1] 72B 实验中 deterministic strategy 使用的是 72B 还是 7B？72B deterministic death rate 和 Δ_nd 是多少？

**Q2.** [R1] find-non-living-thing n=40（其他任务 n=20）——加倍 episodes 的决策是否在看到初始结果后做出的？如果是，这构成 data-dependent inclusion 的轻微风险。

**Q3.** [R1] Reflexion 在将 death rate 从 42.9% 降至 31.4% 的同时，Δ_nd 是否也发生了变化？

**Q4.** [R1] 正文 DAF 95% CI [81.6%, 98.8%] 是 episode-level 还是 cluster-level bootstrap？如果是前者，可能低估 uncertainty。

**Q5.** [R1] Discussion 中 inverted-U hypothesis（~0.5B 以下 agents 无法到达危险状态）仅基于 15 episodes，有更多数据支持吗？

---

## Missing References

R1 建议：HuggingGPT / TaskMatrix (Shen et al., 2023)、CREATOR (Qian et al., 2023)、SafeDreamer (Huang et al., 2024)
R2 建议：ToolBench (Qin et al., 2023)
共同关注：LLM agents in permadeath environments（已引 BALROG + NetPlay，但 NetHack/Crafter 的 LLM agent 实验性工作如有则应引用）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 config 中无 `external_review.paperreview_ai.enabled` 设置）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | Director |
|------|----|----|----------|
| Soundness | 4/5 | 3.5/5 | 4/5 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分理由：**

本文方法论贡献扎实（dual-metric diagnostic framework + router-as-diagnostic-probe），统计分析严谨程度超出 NLP 论文平均水平，negative results 报告诚实。但以下因素限制了 Conference 水平的定位：

1. **核心发现新颖性有限**（C4）：death dominance 在明确 penalty 结构后 back-of-envelope 可预测，两个核心指标的"发现"属性被高估
2. **单一环境 + 单一失败模式**（C3）：100% deaths 来自同一 action pattern，无第二个 permadeath 环境验证
3. **headline metric 的结构性问题**（C1, C2）：78.9% 是 binary task-composition artifact，"penalty-independent" 表述实际依赖 P>0

**Findings 定位的积极因素：** 框架的诊断 procedure 可复用于其他环境；四轴 agent improvement baselines 的 robustness 论证是 non-trivial 的贡献；practitioner decision framework 有工程价值。

**升级至 Borderline Conference (3.5) 的路径：**
1. 补充 NetHack 或 Crafter 的 N≥50 pilot study（最关键）
2. 将核心叙事 reframe 为 "death dominance resists standard interventions"
3. 在 §3.1 明确讨论 78.9% 的 binary per-task structure 和 P=0 lower bound (51.2%)

---

## Detailed Comments (按章节)

### Abstract
- 数字密度过高（8+ 数字/~140 词），建议削减至 3 个关键数字 [W1]
- "Retry yields only marginal reduction (43.5%)" 歧义——改为 "from 48.0% to 43.5%" [M4]

### Introduction
- 叙事线清晰（问题→假设→框架→发现→贡献），无结构性问题
- Contribution 2 过载（86 词），建议重组 [W7]
- 核心 framing 应从 "death dominates" 转向 "death dominance resists interventions" [C4]

### Method (§2)
- Counterfactual episode collection 设计合理，97.4% tie rate 充分论证了 episode-level 方法的必要性
- Algorithm 1 的 death-first priority 是合理语义（death=-100 vs alive≥0）
- DAF 定义数学上清晰，penalty sensitivity analysis (Appendix G) 完整
- 需区分 labeling-function-level vs practical-value-level penalty independence [C2]

### Experiments (§3)
- §3.1: 需讨论 78.9% 的 binary per-task structure [C1]；Cohen's d=3.02 应提升至正文 [W6]
- §3.2: Cross-model replication (Llama-3.1-8B) 可信
- §3.3: 72B 实验设计需澄清 [W2]；DAF recomputation 需报告完整 decomposition
- §3.4-3.5: MATH negative control 有效但需标注模态定义差异 [W3]
- §3.7: "structural failure" 应弱化为 "under current data regime" [W5]

### Related Work (§5)
- 第一段 6 citations 连续罗列，应按功能类别重组 [M2]
- 引用覆盖基本充分；建议考虑 HuggingGPT, ToolBench

### Discussion (§4)
- Practitioner decision framework 有价值
- Non-triviality 论证应聚焦 intervention robustness 而非 death dominance 本身 [C4]
- 需增加 pure-strategy vs mixed-strategy gap 的讨论 [W4]

### Limitations
- 结构清晰（三个 paragraph headers），覆盖 scope/method/stats
- 63% task exclusion 应在正文（非仅 Limitations）提及

### Format
- ACL template 正确，匿名化完整，正文 ~8 页合规
- Orphan bib entry (altman1999cmdp) [M3]
- Responsible NLP Checklist 填写充分