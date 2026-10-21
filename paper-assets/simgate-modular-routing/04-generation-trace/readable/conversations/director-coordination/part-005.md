# Director coordination — Part 5 of 9

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/53/532e22af863d2a24e206.json)

## Round 122

### User

_source line 1409 · 2026-05-19T11:19:11.219825+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)
**审查侧重**: 方法严谨性 + 实验设计 + 统计推断

---

## Summary

本文提出 episode-level counterfactual diagnostic framework，通过 dual-metric 设计（penalty-independent 的 death-asymmetry label fraction 和 penalty-dependent 的 DAF）分解 modular LLM agent 的 routing signal 组成。在 ScienceWorld 上（11 task types, 245 episodes, Qwen2.5-7B），78.9% 的 non-tie routing labels 来自 death asymmetry，DAF = 90.4%。跨模型（Llama-3.1-8B）和跨环境（MATH, ALFWorld）验证支持框架的诊断能力，router training 的 negative result 进一步说明 routing 在 death-dominant 环境中近乎退化。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 方法设计严谨，dual-metric 设计合理，统计分析诚实且附带充分 caveats。主要担忧：78.9% 是 task composition 的产物（10 个 death-prone 任务 100% + 1 个 death-free 任务 0%），以及 K=11 cluster 推断的可靠性。 |
| Excitement | 3/5 | 框架本身有方法论价值，"routing signal 被 catastrophic failure 主导"的发现对 agent routing 社区有实际指导意义。但 scope 限于一个环境，核心发现在明确 penalty 机制后有一定可预期性。 |
| Reproducibility | 4/5 | 超参数完整（Table 6），统计方法详尽，分析 pipeline 描述清晰。代码和数据承诺 acceptance 后释放，预发布可进一步提升可复现性。 |
| Overall Assessment | **3.5** (Borderline Conference) | 方法论贡献扎实、分析严谨透明，但实证范围有限（单一主环境），若补充一个具有 permadeath 的新环境验证（如 NetHack/Crafter）可显著增强说服力。适合 Findings；距 main conference 需解决 scope 问题。 |
| Confidence | **4/5** | 仔细检查了方法设计、统计推断和实验逻辑，熟悉 tool-use routing、agent 环境和 small-cluster 统计推断相关文献。 |

---

## 主要优势

**S1. 方法设计干净且动机明确。** Counterfactual episode collection 通过 same-seed pure-strategy pairs 隔离了 modality choice 作为唯一变量（Section 2.2），避免了 confounding。97.4% step-level tie rate 的展示清楚论证了为什么需要 episode-level 而非 step-level labeling。

**S2. Dual-metric 设计是本文最重要的方法论贡献。** 同时报告 penalty-independent 的 label fraction（78.9%）和 penalty-dependent 的 DAF（90.4%），并在 Section 2.4 中明确指出 DAF 随 P 单调递增是 "mathematical consequence rather than empirical finding"。这种自我校正式的透明度在投稿论文中少见。

**S3. Anti-cherry-picking 分析异常充分。** Table 5（Appendix C）展示 19 个被排除的 task types 的 death-rate differential（mean +38.2 pp）高于 included tasks（+28.7 pp），排除理由（dev set / 族冗余 / agent floor）逐一列出，直接回应 selection bias 质疑。

**S4. 多层次 robustness checks 形成互补论证链。** Seed robustness（DAF 89.7% vs 90.4%）、cross-model replication（Llama-3.1-8B, 10/10 direction consistency）、LOTO-DAF（最大变动 3.0 pp）、wild cluster bootstrap + exact permutation + sign test 多重检验互相印证。

**S5. Negative results 解释自洽。** Router training 的 episode-level failure（47.1 ± 2.2%, below chance）和 MATH 的 null result（p = 0.81）并非失败，而是框架诊断能力的正向验证：在 death-dominant 环境中 routing 退化，在无 catastrophic failure 环境中无 routing signal。4B model 的 59.0% 被合理归因于 task-type classification 而非 generalizable routing。

**S6. Agent improvement baselines 覆盖多个干预轴。** Retry、Reflexion、10× scaling、action-space filtering 四条独立干预路径，加上 dose-response analysis，提供了 death dominance 鲁棒性的有力证据。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **78.9% label fraction 实质是 task-level 二值特性的 aggregate artifact，而非连续性的诊断结果**
- 具体位置：Section 3.1, Appendix D (Table, LOTO-DAF)
- 问题：LOTO-DAF 分析（Appendix D）揭示了一个关键结构：移除唯一的 death-free 任务（find-non-living-thing）后 DAF 跳至 100%。这意味着 78.9% 并非反映 "在各任务中约 79% 的 signal 来自 death"，而是 "10 个 death-prone 任务贡献了 100% death-asymmetry labels，1 个 death-free 任务贡献了 100% score-comparison labels"。aggregate 78.9% 是 task composition（10:1 的 death-prone vs death-free 比例）的直接产物，增减 death-free 任务数量即可任意改变该百分比。
- 为什么影响接收：这是论文的 headline finding。如果审稿人理解到 78.9% 在 task level 分解为 {100%, 100%, ..., 100%, 0%}，该数字的诊断价值会大幅下降。论文应在正文中明确讨论这一 binary structure，而不是仅在 Appendix D 的 LOTO 表中隐含展示。
- 建议修改方向：(1) 在 Section 3.1 增加 1-2 句话明确指出 label fraction 在 task-type level 呈现 binary split（death-prone 任务中 100%，death-free 任务中 0%）；(2) 讨论这种 binary structure 对框架诊断价值的影响——框架的真正诊断输出可能不是一个连续百分比，而是一个 binary classification（"此环境是否 death-dominated"）。

**N2** [critical] **72% 的 death-asymmetry labels 在 P=0 时退化为 ties，削弱了 "penalty-independent" 的表述**
- 具体位置：Section 3.1（"Of these 75, 54 (72.0%) reduce to ties when the death penalty is removed entirely"）
- 问题：论文将 78.9% 称为 "penalty-independent death-asymmetry label fraction"。技术上准确——labeling function（Algorithm 1）基于 binary death indicator 而非 penalty magnitude，所以 label count 不依赖 P。但论文同时披露 54/75（72%）death-asymmetry episodes 中 surviving strategy 也 scored zero，即这些 episodes 的 routing preference 只在 P > 0 时才有实际意义。这意味着 "penalty-independent" 的表述容易误导读者高估 routing 的实际价值：如果 penalty 被设为 0（或环境允许 restart without penalty），这 54 个 labels 失去意义。
- 为什么影响接收：这关乎核心 claim 的解读。审稿人和读者需要清楚理解：78.9% 是 labeling function 的形式化产物，而非无条件的实用价值度量。
- 建议修改方向：(1) 在 Section 2.3 或 3.1 明确区分 "labeling-function-level penalty independence"（label 定义不依赖 P）与 "practical-value-level penalty dependence"（routing 的实际收益依赖 P > 0）；(2) 报告 P=0 时的 effective non-tie label count（41 个）和其中 death-asymmetry 的比例（21/41 = 51.2%），作为实际 routing 价值的 lower bound。

**N3** [critical] **K=11 cluster 推断可靠性不足，论文虽承认但未充分量化其对核心结论的影响**
- 具体位置：Limitations ("Cluster bootstrap with K=11... should be interpreted cautiously"), Appendix D (Table, wild cluster bootstrap)
- 问题：Cameron & Gelbach (2008) 和 Webb (2023) 均指出 K < 40 时 cluster-robust 推断可能 over-reject。论文的补充检验（wild cluster bootstrap p < 0.001, exact permutation p = 0.002, sign test p < 0.001）均假定 cluster-level independence，但 ScienceWorld 的 11 task types 共享相同 environment dynamics（物理引擎、action space、reward function）。exact permutation 的 2,048 permutations 是所有可能的 sign assignments（2^11），这提供了一个 non-parametric 检验，但其有效性仍依赖于 cluster 间的 exchangeability 假设。95% CI [73%, 100%] 的宽度反映了 small-K 的根本限制。
- 为什么影响接收：Death asymmetry 的存在（方向性）几乎无可争议（10/11 task types 一致），但其 magnitude 的精确估计受限于 K=11。论文的核心 claim 是 "dominant"（>50%），而 CI 下界 73% 仍支持这一 claim。但如果审稿人对 cluster exchangeability 有怀疑，CI 可能更宽。
- 建议修改方向：(1) 在正文中（而非仅 Limitations）讨论 K=11 的实际含义——诚实地说 "directional finding is robust, magnitude precision is limited"；(2) 考虑 report cluster-level effect sizes（Cohen's d = 3.02 已在 Appendix D 中报告，应提升至正文）；(3) 如果可以获取 excluded tasks 的完整数据（不仅 n=5 prescreening），扩展至 K=30 会大幅增强 cluster 推断的可信度。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Pure-strategy 设计高估了 death asymmetry 对 routing 的实际影响**
- 具体位置：Section 2.2
- 问题：Pure-strategy comparison 让 internal strategy 在每一步都使用 LLM 推理，没有 deterministic fallback 的 "safety net"。在真实 mixed-strategy routing 中，即使偶尔几步切换到 deterministic 就可能避免 catastrophic death。因此 42.9% 的 internal death rate 是 worst-case scenario，不代表 realistic routing 场景下的 death rate。论文通过 DAgger (2011) 引用承认了 distribution shift，但未量化 pure-strategy findings 到 mixed-strategy 的 transferability gap。
- 建议：在 Discussion 中增加一段话讨论 pure-strategy 上界与 mixed-strategy 实际值之间可能的 gap，或在 Section 2.2 增加 justification 说明为什么 pure-strategy diagnostic 仍然有效（例如：如果 mixed-strategy 也出现 death dominance，结论更强；如果不出现，则框架成功诊断了 pure-strategy 的特殊性）。

**W2** [warning] **r = 0.97 的 Figure 1 caption 缺少 "mathematical consequence" caveat**
- 具体位置：Figure 1 caption ("r = 0.97, p < 10^{-6}, n = 11 task types")
- 问题：Section 3.1 正文已明确说明 "the near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding"。但 Figure 1 caption 仅报告 r、p 和 n，未加任何 caveat。许多读者（尤其是快速浏览的审稿人）只看 figure + caption，可能误以为这是一个独立的实证发现。
- 建议：在 Figure 1 caption 中加一句 "See Section 3.1 for why this correlation is a mathematical consequence of death dominance rather than an independent finding" 或 "Note: this correlation is structurally implied by the decomposition when DAF → 1."

**W3** [warning] **72B DAF 对比缺少关键实验细节**
- 具体位置：Section 3.3（"Recomputing DAF with 72B yields 90.9%"）
- 问题：72B 实验是否收集了完整的 72B episode pairs（72B internal vs 72B deterministic）？还是仅收集了 72B internal strategy 的数据，与 7B deterministic baseline 对比？由于 deterministic strategy 也使用 LLM 进行 action selection（只是接收 ground-truth observations），模型规模改变可能影响 deterministic death rate。论文未明确说明 72B 实验的 deterministic 策略使用什么模型。
- 建议：明确说明 72B 实验设计——deterministic strategy 是否也使用 72B，并报告 72B deterministic death rate 和 Δ_nd。

**W4** [warning] **Episode-level labeling 的 ~27.7% mislabeling fraction 对 router training 的影响未充分讨论**
- 具体位置：Limitations ("The mislabeling fraction... is approximately 27.7%")
- 问题：27.7% 的 episode-level labels 与 step-level oracle labels 不一致，集中在 death-asymmetry episodes 的早期步骤。这不仅影响 router training（Section 3.7），也影响对 routing signal 本身的解读——death-asymmetry episode 的早期步骤可能偏好 internal strategy，但 episode label 强制为 det-preferred。论文将此作为 router failure 的部分解释，但未讨论其对 78.9% label fraction 诊断价值的影响。
- 建议：增加分析——如果使用 step-level labels 而非 episode-level labels，death-asymmetry 的 fraction 会如何变化？或至少讨论 episode-level aggregation 可能导致的信息损失规模。

**W5** [warning] **Cross-environment probes 未在新环境中复制 death-dominance finding**
- 具体位置：Section 3.4-3.5
- 问题：MATH 是 negative control（无 death → 无 signal），ALFWorld 诊断出 information asymmetry（另一种机制）。两者都验证了框架的诊断能力，但都没有在一个新的 permadeath 环境中复制 "death dominance" 的核心发现。论文在 Conclusion 中提到 NetHack 和 Crafter 作为 "most direct replication targets"——如果能包含其中一个环境的初步数据，论文的说服力会大幅提升。
- 建议：如果无法在 camera-ready 前获取新环境数据，至少在 Discussion 中更 prominently 讨论 ScienceWorld-specific factors（固定 P=100, binary death, text-based interface）可能如何影响 generalizability。

**W6** [warning] **Data scaling ablation 使用 paraphrase augmentation 而非 real data，结论可能不成立**
- 具体位置：Appendix F, Table 9
- 问题：Data scaling 从 25% 到 800% 使用 paraphrase augmentation（synonym substitution + template variation），但 augmentation 不生成新的 routing patterns。论文承认 "real-data scaling remains an open question"，但仍从该实验得出 "failure is structural" 的结论。如果 real data 中 internal-preferred episodes 的比例更高（例如通过更复杂的任务），router 可能学到有意义的 signal。
- 建议：(1) 弱化 "structural failure" 的表述为 "failure under current data distribution"；(2) 在正文中更 prominently 标注 augmentation-based scaling 的局限性。

---

## Questions（需要作者回答）

**Q1.** 论文在 Section 3.3 中报告 72B 的 death-prone death rate 为 34.5%。这里的 deterministic strategy 使用的是 72B 还是 7B？如果是 72B，72B deterministic 的 death rate 是多少？

**Q2.** 论文声称 find-non-living-thing 作为 "internal counterexample" 包含在内（Appendix C）。但该任务的 n=40（其他任务 n=20），选择性加倍 episodes 的决策是在看到初始结果后做出的吗？如果是，这构成 data-dependent inclusion 的轻微风险。

**Q3.** Reflexion 将 death rate 从 42.9% 降至 31.4%（Section 3.3），但 Reflexion 的 Δ_nd 是否也发生了变化？如果 Reflexion 不仅减少 death，还改变了 non-death episodes 的 score gap，DAF 的 recomputation 需要同时考虑两个变量。

**Q4.** 论文引用 Cameron & Gelbach (2008) 指出 K < 40 的问题，但正文 CI 报告使用的是 episode-level bootstrap（B=10,000）而非 cluster bootstrap。正文 DAF 95% CI [81.6%, 98.8%] 是 episode-level 还是 cluster-level bootstrap？如果是 episode-level，它可能低估 uncertainty。

**Q5.** Discussion 中提到 "below a capability threshold (~0.5B), agents fail to reach dangerous states at all (13.3% death rate in a 15-episode pilot)"。这个 inverted-U hypothesis 很有趣但仅基于 15 个 episodes。作者是否有更多数据支持这一观察？

---

## 小问题（不影响接收）

- Abstract 中 "Retry yields only marginal reduction (43.5%)" 括号内是 post-retry death rate 而非 reduction 量，首次阅读时容易造成歧义。建议改为 "Retry yields only marginal reduction (from 48.0% to 43.5%)" 或类似表述。
- Table 4 (per-task decomposition) 的 D%_int 和 D%_det 列头含义需在 caption 首次出现时定义，当前在正文中有定义但 caption 中仅说 "D%: death rate"。
- references.bib 中 ART (2023) 为 arXiv preprint (@article)，但已发表；建议更新为正式出版信息。
- Algorithm 1 中 "both dead → no-pref" 的设计丢失了部分信息（early death vs late death 可能有 routing 价值），虽然 Section Limitations 已讨论，但可在 Algorithm 1 附近加脚注说明。
- SCI（Signal Concentration Index）在方法中定义但在结果中仅用一句话报告（SCI = 0.2147），对其解读缺少 benchmark（什么样的 SCI 算 "low"）。

---

## Missing References

未发现严重遗漏。建议考虑以下引用以增强 Related Work：
- HuggingGPT / TaskMatrix (Shen et al., 2023)——多模块 agent 的 routing/orchestration，与 modular routing 直接相关
- CREATOR (Qian et al., 2023)——tool creation vs tool use 的 routing 决策
- 如果存在空间，Safe RL 段落可引用 SafeDreamer (Huang et al., 2024)——model-based safe RL 在 interactive 环境中的应用

---

## 总体评分

**Overall**: **3.5** (Borderline Conference)

**一句话总结**: 方法论贡献扎实（dual-metric 诊断框架 + router-as-diagnostic-probe），统计分析诚实透明，但 78.9% headline 的 binary task-level structure 和单一环境的实证范围是主要瓶颈——补充一个 permadeath 环境的验证（如论文自身提到的 NetHack/Crafter）可使本文从 Borderline Conference 提升至 Conference 水平。


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

_source line 1410 · 2026-05-19T11:19:29.138478+00:00_

Reviewer 1 审稿意见已收到。关键发现记录如下：

**R1 评分**: 3.5 (Borderline Conference), Confidence 4/5

**Must-Fix (3 条)**:
- N1: 78.9% 实质是 task-level binary split 的 aggregate artifact（10 个 death-prone 任务 100% + 1 个 death-free 任务 0%），非连续性诊断
- N2: 72% death-asymmetry labels 在 P=0 时退化为 ties，"penalty-independent" 表述有误导性
- N3: K=11 cluster 推断可靠性不足，核心结论的 magnitude precision 受限

**Should-Fix (6 条)**: pure-strategy 高估、Figure 1 caption 缺 caveat、72B 实验细节不全、mislabeling 影响未充分讨论、无 permadeath 环境复制、augmentation scaling 结论过强

等待 Reviewer 2 审稿意见，收齐后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 123

## Round 123

2 recorded events


### User

_source line 1411 · 2026-05-19T11:19:31.753904+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心结论：**Overall 3.5（Borderline Conference）**。

三个 Must-Fix 问题：
1. **78.9% label fraction 的 binary structure**：10 个 death-prone 任务各贡献 100% death-asymmetry labels，1 个 death-free 任务贡献 0%，aggregate 百分比是 task composition 的产物而非连续性诊断指标
2. **"penalty-independent" 表述的误导性**：72% 的 death-asymmetry labels 在 P=0 时退化为 ties，routing 的实际价值依赖 P > 0
3. **K=11 cluster 推断可靠性**：95% CI [73%, 100%] 过宽，补充检验虽多但 cluster exchangeability 假设仍受限

六个 Should-Fix + 五个 Minor 问题，涵盖 pure-strategy 设计的 realistic gap、Figure 1 caption 缺 caveat、72B 实验设计不明确、data scaling ablation 局限性等。

优势方面：dual-metric 设计、anti-cherry-picking 分析的充分性、negative results 的自洽解释、多层次 robustness checks 都达到较高水准。

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

_source line 1412 · 2026-05-19T11:19:39.477330+00:00_

Reviewer 1 审稿意见已收到。核心评分 3.5 (Borderline Conference)，3 个 Must-Fix + 6 个 Should-Fix。

等待 Reviewer 2 提交审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 124

## Round 124

6 recorded events


### User

_source line 1413 · 2026-05-19T11:19:40.984275+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿完成 — Round 1

**审查侧重**: 新颖性/贡献度 + 完整性 + 写作/格式

### 总体评分
- **Overall**: 3.0 (Findings)
- **Soundness**: 3.5/5
- **Excitement**: 2.5/5
- **Reproducibility**: 4/5
- **Confidence**: 4/5

### Must-Fix 问题 (3 条)

**N1 [critical]** DAF 作为 headline metric 新颖性存疑。DAF = δP/(δP + Δ_nd) 在 P=100 下是数学必然（作者自己在 §3.1 承认 "derived quantity"）。Penalty-independent label fraction (78.9%) 也受 Algorithm 1 的 death-first priority 设计影响——本质上只是在问 "多少 non-tie episodes 有 death asymmetry"。两个核心指标的"发现"属性都被高估了。

**N2 [critical]** 单一灾难性失败环境 + 单一失败模式。Appendix H 显示 100% 的 internal-strategy 死亡来自同一 action pattern (`focus on` 误用)。没有第二个 permadeath 环境验证（NetHack/Crafter 仅提为 future work），无法区分这是 ScienceWorld 的 idiosyncratic 结果还是可泛化现象。

**N3 [critical]** Contribution 2 过载，混合了 empirical finding + robustness + router diagnostic implication，难以评估各自独立贡献。

### Should-Fix 问题 (5 条)

**W1** Abstract 数字堆砌（8+ 数字/3句话）。
**W2** 跨环境 "deterministic" 模态定义不一致，MATH 的 negative control 本质上是 tautological。
**W3** 跨模型仅限 7-8B 范围；72B 未做完整 framework replication。
**W4** ScienceWorld 63% task types 排除，anti-cherry-picking 论证依赖 n=5 prescreening。
**W5** Related Work 第一段有论文罗列倾向。

### 主要优势
- 统计方法严谨（wild cluster bootstrap, LOO, 8-seed CV）
- Anti-cherry-picking 分析（Table 4）有效
- Negative result（router episode-level 47.1%）诚实报告
- Practitioner decision framework 有应用价值
- Limitations 诚实充分

### 格式合规
- ACL template 正确（`\usepackage[review]{acl}`），匿名化完整
- 正文约 8 页，Limitations/Ethics 不计入限制，合规
- 1 个 orphan bib entry (altman1999cmdp)
- 部分 bib 年份/作者与 OpenAlex 不完全一致（minor）
- 引用覆盖基本充分，缺少 ToolBench 等

### 判断
Findings 水平。统计分析质量高但核心发现新颖性有限（数学预决定 + 单环境单失败模式）。补充第二个 permadeath 环境 + 重新 framing 核心指标可能提升至 3.5。

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

_source line 1414 · 2026-05-19T11:20:12.141317+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计 + 统计推断）\n\n**Overall**: 3.5 (Borderline Conference) | Soundness 4/5 | Excitement 3/5 | Confidence 4/5\n\n### Must-Fix\n\n**R1-N1** [critical] 78.9% label fraction 实质是 task-level 二值特性的 aggregate artifact。LOTO-DAF 分析显示移除唯一 death-free 任务后 DAF 跳至 100%。aggregate 78.9% 是 task composition（10:1 比例）的直接产物，增减 death-free 任务数量即可任意改变该百分比。框架的真正诊断输出可能不是连续百分比，而是 binary classification（\"此环境是否 death-dominated\"）。\n\n**R1-N2** [critical] \"penalty-independent\" 表述误导。72% 的 death-asymmetry labels（54/75）在 P=0 时退化为 ties（surviving strategy scored zero）。78.9% 是 labeling function 的形式化产物，routing 的实际收益依赖 P > 0。建议报告 P=0 时的 effective non-tie label count（41 个）和 death-asymmetry 比例（21/41 = 51.2%）。\n\n**R1-N3** [critical] K=11 cluster 推断可靠性不足。Cameron & Gelbach (2008), Webb (2023) 指出 K < 40 时 over-reject 风险。95% CI [73%, 100%] 过宽。补充检验均假定 cluster-level independence，但 ScienceWorld 11 task types 共享 environment dynamics。建议将 Cohen's d = 3.02 提升至正文，扩展至 K=30 如有条件。\n\n### Should-Fix\n\n**R1-W1** Pure-strategy 设计高估 death asymmetry 对 realistic mixed-strategy routing 的影响。42.9% internal death rate 是 worst-case，未量化 mixed-strategy transferability gap。\n\n**R1-W2** Figure 1 caption 缺少 \"mathematical consequence\" caveat，快速浏览的读者可能误解为独立实证发现。\n\n**R1-W3** 72B DAF 对比缺关键细节——deterministic strategy 用的是 72B 还是 7B？72B deterministic death rate 未报告。\n\n**R1-W4** Episode-level ~27.7% mislabeling fraction 对 78.9% label fraction 诊断价值的影响未讨论。\n\n**R1-W5** Cross-environment probes 未在新 permadeath 环境中复制 death-dominance finding。\n\n**R1-W6** Data scaling ablation 用 paraphrase augmentation 而非 real data，\"structural failure\" 结论可能不成立。\n\n### Questions\nQ1: 72B 实验中 deterministic strategy 用的模型？\nQ2: find-non-living-thing n=40 的加倍决策是否 data-dependent？\nQ3: Reflexion 是否改变 Δ_nd？\nQ4: 正文 DAF 95% CI 是 episode-level 还是 cluster-level bootstrap？\nQ5: Inverted-U hypothesis 仅基于 15 episodes，有更多数据吗？\n\n---\n\n请逐条 [AGREE] 或 [REBUT]，附理由和证据。",
  "reviewer_id": "2",
  "project": "simgate-modular-routing",
  "round_number": "1"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计 + 统计推断）\n\n**Overall**: 3.5 (Borderline Conference) | Soundness 4/5 | Excitement 3/5 | Confidence 4/5\n\n### Must-Fix\n\n**R1-N1** [critical] 78.9% label fraction 实质是 task-level 二值特性的 aggregate artifact。LOTO-DAF 分析显示移除唯一 death-free 任务后 DAF 跳至 100%。aggregate 78.9% 是 task composition（10:1 比例）的直接产物，增减 death-free 任务数量即可任意改变该百分比。框架的真正诊断输出可能不是连续百分比，而是 binary classification（\"此环境是否 death-dominated\"）。\n\n**R1-N2** [critical] \"penalty-independent\" 表述误导。72% 的 death-asymmetry labels（54/75）在 P=0 时退化为 ties（surviving strategy scored zero）。78.9% 是 labeling function 的形式化产物，routing 的实际收益依赖 P > 0。建议报告 P=0 时的 effective non-tie label count（41 个）和 death-asymmetry 比例（21/41 = 51.2%）。\n\n**R1-N3** [critical] K=11 cluster 推断可靠性不足。Cameron & Gelbach (2008), Webb (2023) 指出 K < 40 时 over-reject 风险。95% CI [73%, 100%] 过宽。补充检验均假定 cluster-level independence，但 ScienceWorld 11 task types 共享 environment dynamics。建议将 Cohen's d = 3.02 提升至正文，扩展至 K=30 如有条件。\n\n### Should-Fix\n\n**R1-W1** Pure-strategy 设计高估 death asymmetry 对 realistic mixed-strategy routing 的影响。42.9% internal death rate 是 worst-case，未量化 mixed-strategy transferability gap。\n\n**R1-W2** Figure 1 caption 缺少 \"mathematical consequence\" caveat，快速浏览的读者可能误解为独立实证发现。\n\n**R1-W3** 72B DAF 对比缺关键细节——deterministic strategy 用的是 72B 还是 7B？72B deterministic death rate 未报告。\n\n**R1-W4** Episode-level ~27.7% mislabeling fraction 对 78.9% label fraction 诊断价值的影响未讨论。\n\n**R1-W5** Cross-environment probes 未在新 permadeath 环境中复制 death-dominance finding。\n\n**R1-W6** Data scaling ablation 用 paraphrase augmentation 而非 real data，\"structural failure\" 结论可能不成立。\n\n### Questions\nQ1: 72B 实验中 deterministic strategy 用的模型？\nQ2: find-non-living-thing n=40 的加倍决策是否 data-dependent？\nQ3: Reflexion 是否改变 Δ_nd？\nQ4: 正文 DAF 95% CI 是 episode-level 还是 cluster-level bootstrap？\nQ5: Inverted-U hypothesis 仅基于 15 episodes，有更多数据吗？\n\n---\n\n请逐条 [AGREE] 或 [REBUT]，附理由和证据。",
    "reviewer_id": "2",
    "project": "simgate-modular-routing",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-19T11:20:21.147418+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9006
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-19T11:20:21.299298+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 审稿意见（新颖性/贡献度 + 完整性 + 写作/格式）\n\n**Overall**: 3.0 (Findings) | Soundness 3.5/5 | Excitement 2.5/5 | Confidence 4/5\n\n### Must-Fix\n\n**R2-N1** [critical] DAF 作为 headline metric 新颖性存疑。DAF = δP/(δP + Δ_nd) 在 P=100 下是数学必然。Penalty-independent label fraction (78.9%) 受 Algorithm 1 的 death-first priority 设计影响——本质上只是在问 \"多少 non-tie episodes 有 death asymmetry\"。两个核心指标的\"发现\"属性都被高估了。\n\n**R2-N2** [critical] 单一灾难性失败环境 + 单一失败模式。Appendix H 显示 100% internal-strategy 死亡来自同一 action pattern (focus on 误用)。没有第二个 permadeath 环境验证。无法区分 ScienceWorld idiosyncratic 结果还是可泛化现象。\n\n**R2-N3** [critical] Contribution 2 过载，混合了 empirical finding + robustness + router diagnostic implication，难以评估各自独立贡献。\n\n### Should-Fix\n\n**R2-W1** Abstract 数字堆砌（8+ 数字/3句话）。\n\n**R2-W2** 跨环境 \"deterministic\" 模态定义不一致，MATH 的 negative control 本质上是 tautological——code interpreter vs internal reasoning 不是 ScienceWorld 意义上的 \"deterministic\"。\n\n**R2-W3** 跨模型仅限 7-8B 范围；72B 未做完整 framework replication。\n\n**R2-W4** ScienceWorld 63% task types 排除，anti-cherry-picking 论证依赖 n=5 prescreening。\n\n**R2-W5** Related Work 第一段有论文罗列倾向（Toolformer → ToolkenGPT → ART → Chameleon → ReTool → ToolACE 连续列举）。\n\n### 格式问题\n- 1 个 orphan bib entry (altman1999cmdp)\n- 部分 bib 年份/作者与 OpenAlex 不完全一致\n\n### Reviewer 2 判断\nFindings 水平。统计分析质量高但核心发现新颖性有限（数学预决定 + 单环境单失败模式）。补充第二个 permadeath 环境 + 重新 framing 核心指标可能提升至 3.5。\n\n---\n\n请逐条 [AGREE] 或 [REBUT]，附理由和证据。",
  "reviewer_id": "1",
  "project": "simgate-modular-routing",
  "round_number": "1"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 审稿意见（新颖性/贡献度 + 完整性 + 写作/格式）\n\n**Overall**: 3.0 (Findings) | Soundness 3.5/5 | Excitement 2.5/5 | Confidence 4/5\n\n### Must-Fix\n\n**R2-N1** [critical] DAF 作为 headline metric 新颖性存疑。DAF = δP/(δP + Δ_nd) 在 P=100 下是数学必然。Penalty-independent label fraction (78.9%) 受 Algorithm 1 的 death-first priority 设计影响——本质上只是在问 \"多少 non-tie episodes 有 death asymmetry\"。两个核心指标的\"发现\"属性都被高估了。\n\n**R2-N2** [critical] 单一灾难性失败环境 + 单一失败模式。Appendix H 显示 100% internal-strategy 死亡来自同一 action pattern (focus on 误用)。没有第二个 permadeath 环境验证。无法区分 ScienceWorld idiosyncratic 结果还是可泛化现象。\n\n**R2-N3** [critical] Contribution 2 过载，混合了 empirical finding + robustness + router diagnostic implication，难以评估各自独立贡献。\n\n### Should-Fix\n\n**R2-W1** Abstract 数字堆砌（8+ 数字/3句话）。\n\n**R2-W2** 跨环境 \"deterministic\" 模态定义不一致，MATH 的 negative control 本质上是 tautological——code interpreter vs internal reasoning 不是 ScienceWorld 意义上的 \"deterministic\"。\n\n**R2-W3** 跨模型仅限 7-8B 范围；72B 未做完整 framework replication。\n\n**R2-W4** ScienceWorld 63% task types 排除，anti-cherry-picking 论证依赖 n=5 prescreening。\n\n**R2-W5** Related Work 第一段有论文罗列倾向（Toolformer → ToolkenGPT → ART → Chameleon → ReTool → ToolACE 连续列举）。\n\n### 格式问题\n- 1 个 orphan bib entry (altman1999cmdp)\n- 部分 bib 年份/作者与 OpenAlex 不完全一致\n\n### Reviewer 2 判断\nFindings 水平。统计分析质量高但核心发现新颖性有限（数学预决定 + 单环境单失败模式）。补充第二个 permadeath 环境 + 重新 framing 核心指标可能提升至 3.5。\n\n---\n\n请逐条 [AGREE] 或 [REBUT]，附理由和证据。",
    "reviewer_id": "1",
    "project": "simgate-modular-routing",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1417 · 2026-05-19T11:20:22.814667+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1515
}
```

</details>

---


### Assistant

_source line 1418 · 2026-05-19T11:20:25.707652+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 125

## Round 125

2 recorded events


### User

_source line 1419 · 2026-05-19T11:20:28.286684+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已汇报 Director。

**核心判断：Overall 3.0 (Findings)**

三个 Must-Fix 问题：
1. DAF 是 P=100 下的数学必然而非经验发现，label fraction 也受 labeling 设计影响——核心指标的"发现"属性被高估
2. 100% 的死亡来自单一 action pattern (`focus on`)，且无第二个 permadeath 环境验证，泛化性不足
3. Contribution 2 过载

主要优势在于统计方法严谨（wild cluster bootstrap, LOO 等超出 NLP 论文平均水平）和诚实的 negative result 报告。补充 NetHack/Crafter pilot + 重新 framing 核心指标后有望提升至 Borderline Conference。

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

_source line 1420 · 2026-05-19T11:20:33.273180+00:00_

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


## Round 126

## Round 126

2 recorded events


### User

_source line 1421 · 2026-05-19T11:22:34.654181+00:00_

[Reviewer 1 审稿意见]:

# R1 对 R2 审稿意见的逐条交叉回应

---

## Must-Fix

**[AGREE with nuance] R2-N1: DAF 新颖性 + 78.9% label fraction 的 "发现" 属性**

R2 核心批评成立：DAF 在给定 δ、P、Δ_nd 后是代数必然（论文 Section 2.4 自己说了 "mathematical consequence"）；78.9% 是 Algorithm 1 定义出的度量，不是意外发现。

但 R2 低估了两点：(1) 框架的诊断价值不等于指标的新颖性——之前 agent routing 文献假设 signal 来自 diverse sources（Section 1, para 2），框架提供了可操作的 decomposition procedure 来检验这一假设；(2) Algorithm 1 的 death-first priority 不是为了膨胀 death signal——如果一个 strategy 死亡（-100）另一个存活（≥0），routing 偏向存活方是合理语义。

**但 framing 问题我完全同意**，且与我的 N1 一致：78.9% 在 task level 是 binary split（10 个 death-prone 任务 100%，1 个 death-free 任务 0%），aggregate 数字是 task composition 的产物。应 reframe 为 "framework 输出揭示 degenerate structure"。

---

**[AGREE] R2-N2: 单一环境 + 单一失败模式**

完全同意。Appendix H 显示 100% deaths 来自同一 action pattern（`focus on` 误用），核心发现可能只是 "ScienceWorld answer-submission 机制 + 7B action grounding 缺陷 = death dominance"。论文 Limitations 有区分 methodological vs empirical generality，但 title/abstract/intro 的 framing 暗示更广适用性。与我的 W5 一致。补充 NetHack/Crafter 是提升至 Conference 的关键。

---

**[REBUT] R2-N3: Contribution 2 过载**

认为这是表述偏好而非 critical flaw。Contribution 2 的三个子成分（78.9% finding → four-axis robustness → oracle degeneracy implication）形成因果链，拆分反而制造冗余。可将 "router as diagnostic probe" 移至 Contribution 1（方法论部分）来减轻 C2 负载，但这是 editorial 调整。

---

## Should-Fix

**[AGREE] R2-W1: Abstract 数字堆砌**
完全同意。~110 词中 8+ 个数字，建议保留 78.9% 和 p=0.81，其余移至正文。

**[REBUT with partial agree] R2-W2: MATH negative control tautological**
"deterministic" 定义不一致的观察正确，但 MATH 不是 tautological——它排除了 "任何 two-modality comparison 都产生 one-sided signal" 的混淆解释，null result（p=0.81, 107 vs 95 labels）是具体实证检验。论文 Section 3.4 已标注 "boundary probe" 而非 replication。但同意应更明确讨论模态定义差异的影响。

**[AGREE] R2-W3: 跨模型限于 7-8B；72B 未做完整 replication**
同意，与我的 W3 一致。72B 应报告完整 framework 输出（Δ_nd、label distribution）。

**[AGREE with caveat] R2-W4: 63% 排除 + n=5**
n=5 per task 确实功效不足，但 anti-cherry-picking 只需方向性证据：18/19 excluded tasks 显示 positive ΔDR（Table 5），effect size 极大（+20 to +60 pp），sign-test 级别可信。Paper 已标注 "directional evidence"。

**[AGREE] R2-W5: Related Work 论文罗列**
Section 5 第一段 6 citations 连续列举，应合并为功能类别做 comparative positioning。

---

## 格式问题
均同意。altman1999cmdp orphan entry + ART 等 bib 条目需更新。

---

## 总体评价

与 R2 分歧在 Excitement（我 3/5 vs R2 2.5/5）——我认为 diagnostic framework 本身有方法论复用价值（Discussion para 4 的 50-episode pilot 建议有工程意义），R2 更侧重 empirical novelty。总体方向一致：当前版本 Findings (3.0-3.5)，补充第二个 permadeath 环境可同时上调。我维持 3.5 (Borderline Conference)。


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

_source line 1422 · 2026-05-19T11:22:40.269109+00:00_

Reviewer 1 对 Reviewer 2 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 127

## Round 127

2 recorded events


### User

_source line 1423 · 2026-05-19T11:22:42.865785+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：与 R2 在 5 个 Must-Fix/Should-Fix 上达成一致（R2-N1 framing、R2-N2 单环境、R2-W1 abstract、R2-W3 72B、R2-W5 罗列），在 2 个问题上反驳（R2-N3 Contribution 过载是 editorial 问题非 critical flaw；R2-W2 MATH 不是 tautological 而是有效的 boundary probe），1 个附带 caveat 的同意（R2-W4 n=5 虽弱但方向性仍可信）。与 R2 的总体评分差 0.5 分（我 3.5 vs R2 3.0），分歧在框架方法论价值的权重。

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

_source line 1424 · 2026-05-19T11:22:48.085380+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 128

## Round 128

10 recorded events


### User

_source line 1425 · 2026-05-19T11:23:58.466106+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 — 完成

### 总结

R1 的审稿质量很高，三个 Must-Fix 中两个我强烈同意（N1, N2），一个我认为 severity 过高（N3 应降为 Should-Fix）。6 个 Should-Fix 中我同意 5 个，反驳 1 个（W4）。

### Must-Fix 回应

**[AGREE] R1-N1** 78.9% 是 task composition artifact — 同意核心论点。LOTO-DAF 显示移除 find-non-living-thing 后 DAF→100%。但 binary classification 建议可能过于简化，SCI=0.2147 说明 signal 分布均匀。建议同时报告 binary + continuous metrics。

**[AGREE] R1-N2** "penalty-independent" 误导 — 强烈同意。论文自己的数据显示 P=0 时 54/75 death-asymmetry labels 退化为 ties，effective death fraction 仅 21/41=51.2%。与我的 N1（DAF 新颖性）完全一致。

**[REBUT] R1-N3** K=11 不足 — 部分反驳。Cohen's d=3.02, exact permutation p=0.002 不依赖 asymptotic assumptions, directional consistency 10/10。CI 宽度已在 Limitations 讨论。建议降为 Should-Fix（CI caveat + 正文报告 Cohen's d）。

### Should-Fix 回应

[AGREE] R1-W1 pure-strategy overestimates — 同意但论文 framing 为 diagnostic 部分缓解
[AGREE] R1-W2 Figure 2 caption 缺 caveat — 同意（R1 原文写 Figure 1，应为 Figure 2）
[AGREE] R1-W3 72B deterministic model 不明 — 同意，需澄清
[REBUT] R1-W4 27.7% mislabeling 影响 — 反驳。这是 step-vs-episode level 混淆，78.9% 是 episode-level metric 不受影响
[AGREE] R1-W5 缺 permadeath 环境 — 强烈同意，与我的 N2 一致
[AGREE] R1-W6 paraphrase ≠ real data — 同意，"structural failure" 应改为 "failure under current data regime"

### 对 R1 评分的看法

R1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。差异主要在 Excitement (R1: 3, 我: 2.5)。R1 更看重 framework 的方法论价值；我更看重核心发现的 surprising degree。考虑 R1 的分析后，我维持 3.0 但认为 3.5 可以讨论——如果作者补充 P=0 analysis (R1-N2) 和第二个 permadeath 环境 (R1-W5/我的 N2)，3.5 是可达的。

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

_source line 1426 · 2026-05-19T11:25:02.765726+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "review_issues.yaml",
  "max_chars": "0"
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
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-19T11:25:02.816448+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-19T11:25:06.432097+00:00_

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

_source line 1429 · 2026-05-19T11:25:06.483292+00:00_

1	## Round 16 Review Issues (updated 2026-05-18 R16 consolidated report)
2	
3	- id: "R13-N1"
4	  summary: "DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现"
5	  category: framing
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 13
9	  last_seen_round: 15
10	  mentions:
11	    - round: 13
12	      reviewers: [1, 2]
13	      note: "Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。"
14	    - round: 14
15	      reviewers: [1, 2]
16	      note: "R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。"
17	    - round: 15
18	      reviewers: [1, 2]
19	      note: "R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。"
20	    - round: 16
21	      reviewers: []
22	      note: "R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。"
23	  resolution: "78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence"
24	  resolution_round: 15
25	
26	- id: "R13-N2"
27	  summary: "统计推断可靠性不足：cluster bootstrap K=11、per-task n=20、Llama pilot N=70"
28	  category: method
29	  severity: warning
30	  status: in_progress
31	  first_raised_round: 13
32	  last_seen_round: 16
33	  mentions:
34	    - round: 13
35	      reviewers: [1, 2]
36	      note: "Consensus. Cluster bootstrap K=11 违反 K>=40 要求。"
37	    - round: 14
38	      reviewers: [1, 2]
39	      note: "R14 divergence on severity. 降级为 warning。"
40	    - round: 15
41	      reviewers: [1, 2]
42	      note: "R15 consensus. Cautionary language 和 Cameron 2008 引用到位。"
43	    - round: 16
44	      reviewers: [1, 2]
45	      note: "R16 consensus. §3.1 将 cluster bootstrap 放在 Sensitivity analysis 段落下，但未明确 label 为 sensitivity analysis vs primary CI。R1-W1 要求明确区分。新增 R1-W4: per-task n=20 power 未量化。"
46	  action_items:
47	    - round: 13
48	      action: "对 cluster bootstrap K=11 做更诚实讨论"
49	      assigned_to: paper_agent
50	      status: done
51	    - round: 15
52	      action: "§4.1 明确标注 cluster bootstrap 为 sensitivity analysis"
53	      assigned_to: paper_agent
54	      status: in_progress
55	    - roun
…[truncated 17383 chars]

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

_source line 1430 · 2026-05-19T11:27:54.337719+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "## Round 17 Review Issues (updated 2026-05-19 R17 fresh consolidated report)\n\n# =============================================\n# Resolved issues from prior rounds (unchanged)\n# =============================================\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。\"\n    - round: 16\n      reviewers: []\n      note: \"R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。\"\n  resolution: \"78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence\"\n  resolution_round: 15\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化 27.7% mislabeling fraction\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"引用覆盖充分，orphan entries 已清理\"\n  resolution_round: 15\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld + MATH N 标注不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及 minority-class diversity confound\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'，structural 仅用于 router failure 的 Appendix 描述\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n# =============================================\n# Open / in_progress issues (updated with R17)\n# =============================================\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11、per-task n=20\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. Cluster bootstrap K=11 违反 K>=40 要求。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 divergence on severity. 降级为 warning。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 consensus. Cautionary language 和 Cameron 2008 引用到位。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1 标为 Must-Fix (CI [73%,100%] 过宽，cluster exchangeability 受限)。R2 rebut 降为 Should-Fix (Cohen's d=3.02, exact permutation p=0.002 不依赖 asymptotic assumptions)。Director 裁决：维持 warning。方向性结论 robust，magnitude 精度有限但 CI 下界仍排除 50%。建议正文提升 Cohen's d。\"\n  action_items:\n    - round: 13\n      action: \"对 cluster bootstrap K=11 做更诚实讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 17\n      action: \"将 Cohen's d=3.02 从 Appendix 提升至正文 §3.1；明确 primary CI 为 episode-level bootstrap，cluster-level CI 为 sensitivity analysis\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"约 200 词中 10+ 统计量。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍含 12+ 数字。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus. ~140 词中约 12 个数字。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 consensus. 当前 ~140 词中 8+ 数字。R1/R2 均建议保留 78.9% 和 p=0.81，其余改为定性概括。\"\n  action_items:\n    - round: 17\n      action: \"Abstract 保留 78.9%、DAF 90.4%、p=0.81 三个关键数字；retry/scaling/Reflexion 具体数字改为定性描述\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 认为 78.9% 也 trivial；R1 认为 δ=0.265 是 empirical 非先验可知。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus (critical). back-of-envelope 可预测 death dominance。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 consensus. R2-N1: DAF 是数学必然，78.9% 是 Algorithm 1 设计产物。R1 同意 framing 问题但认为框架的 diagnostic procedure 本身有价值。两人均认为 reframing 为 'death dominance resists interventions' 可提升 novelty perception。\"\n  action_items:\n    - round: 17\n      action: \"核心叙事 reframe: 强调 intervention robustness (δ persists under retry/Reflexion/scaling/filtering) 而非 death dominance 本身的发现\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 consensus.\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-W2 再提 MATH negative control 的 tautological 质疑。R1 rebut: MATH 是有效 boundary probe (p=0.81 是具体实证检验)，但同意模态定义差异应更 prominently 讨论。Director: 同意 R1——MATH 不是 tautological，但 comparability limitation 应在 Table caption + §3.5 明确标注。\"\n  action_items:\n    - round: 17\n      action: \"Table 2 caption 逐项注明每环境 deterministic 的具体含义 (oracle simulator / code interpreter / admissible actions)\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及此 issue。R1-W4 讨论了 mislabeling 对 78.9% 的影响但 R2 rebut 认为 episode-level metric 不受 step-level mislabeling 影响。可能已充分处理。\"\n  action_items:\n    - round: 16\n      action: \"§3.7 补充 oracle margin 与 mislabeling 的独立性讨论\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M1\"\n  summary: \"缺少 permadeath 环境 LLM agent 工作引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"ToolACE, Inner Monologue, Tamar 2015 已补充。NetHack/Crafter LLM agent 工作仍缺。\"\n    - round: 17\n      reviewers: [1]\n      note: \"R17 R1 未单独提及缺失引用，建议 HuggingGPT, CREATOR, SafeDreamer。R2 建议 ToolBench。\"\n  action_items:\n    - round: 17\n      action: \"检查并补充 LLM agent in permadeath environments 引用（BALROG 和 NetPlay 已有，可能足够）\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit: death dominance 在 ScienceWorld penalty 结构下可从 back-of-envelope 预测\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Strong consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 strong consensus. R2 Excitement 2.5/5，R1 3/5。两人均认为框架方法论有价值但 empirical finding 可预期。Reframe 方向：'death dominance resists standard interventions' 比 'death dominates routing signal' 更有 novelty。R1 补充：agent improvement baselines 的 robustness 是事前不可预测的。\"\n  action_items:\n    - round: 17\n      action: \"(1) Reframe Introduction/Abstract 核心叙事从 finding 转向 methodology + intervention robustness; (2) Discussion 增加 'what was not predictable: intervention failure ceiling'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"63% exclusion 意味着 death dominance 可能仅适用于 ScienceWorld 特定 task subset。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-W4 再提 n=5 prescreening 的局限。R1 同意但 caveat: anti-cherry-picking 需方向性证据，18/19 excluded tasks 方向一致（Table 5），sign-test 级别可信。Director: 论证充分但应在正文（非仅 Appendix）明确 63% exclusion 为 scope limitation。\"\n  action_items:\n    - round: 17\n      action: \"§3 开头段明确标注 63% exclusion 是 scope limitation 而非仅在 Limitations 提及\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N3\"\n  summary: \"实验规模和环境多样性不足: 缺少 permadeath 环境 replication (NetHack/Crafter)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"两位 reviewer 均认为这是影响 Conference vs Findings 定位的关键因素。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 strong consensus. R1-W5 和 R2-N2 独立提出。R2 进一步指出 100% deaths 来自同一 action pattern (focus on)，无法区分 ScienceWorld idiosyncratic vs generalizable。两人均认为补充第二个 permadeath 环境是从 Findings 提升至 Conference 的关键。\"\n  action_items:\n    - round: 17\n      action: \"(1) NetHack 或 Crafter pilot (N>=50) 是升级至 Conference 的关键; (2) 如无法执行，Discussion 中更 prominently 讨论 ScienceWorld-specific factors (固定 P=100, 单一 fatal action pattern, text-based interface)\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"§3.3 将 72B DAF=90.9% 直接与 7B DAF=90.4% 比较时未强调 population 差异。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W3 + R2-W3 consensus。72B 实验设计不明确——deterministic strategy 使用什么模型？72B deterministic death rate 未报告。72B 未做完整 framework replication。\"\n  action_items:\n    - round: 17\n      action: \"(1) 明确 72B 实验设计 (deterministic strategy model); (2) 报告 72B deterministic death rate 和 Δ_nd; (3) 注明 population 差异 (10 vs 11 tasks)\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"0.6B=50.7%, 1.7B=43.1%, 4B=59.0%。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及此 issue。可能被 router diagnostic 整体评价覆盖。\"\n  action_items:\n    - round: 16\n      action: \"补充 1.7B per-class confusion matrix 或弱化解释\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"该图是 cross-env label distribution 对比图。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及，但当前版本 Appendix I 已引用 signal_reversal.pdf (Figure 4)。待确认引用是否正式。\"\n  action_items:\n    - round: 16\n      action: \"正式引入或删除 signal_reversal.pdf\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载（覆盖 finding + robustness + router diagnostic）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 首提，R1 同意。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-N3 升为 Must-Fix。R1 rebut: 三个子成分形成因果链，拆分制造冗余，这是 editorial 调整而非 critical flaw。Director 裁决：维持 warning——合理关切但不影响接收决定。建议将 router diagnostic 移入 Contribution 1。\"\n  action_items:\n    - round: 17\n      action: \"将 router-as-diagnostic-probe 从 Contribution 2 移至 Contribution 1（方法论部分），减轻 C2 负载\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致 (find-non-living vs find-non-living-thing)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及，待确认是否已修复。\"\n  action_items:\n    - round: 16\n      action: \"统一 task name\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# =============================================\n# Round 17 New Issues\n# =============================================\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction 在 task level 呈现 binary split (death-prone 100%, death-free 0%)，aggregate 是 task composition artifact\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N1 首提，R2 强烈同意。LOTO-DAF (Appendix D) 显示移除 find-non-living-thing 后 DAF→100%。10 个 death-prone 任务各贡献 100% death-asymmetry labels。aggregate 78.9% 可通过增减 death-free 任务数量任意改变。框架的真正诊断输出是 binary classification 而非连续百分比。\"\n  action_items:\n    - round: 17\n      action: \"(1) §3.1 增加 1-2 句明确指出 binary per-task structure; (2) 讨论框架诊断输出的 binary vs continuous 性质; (3) LOTO-DAF 关键结论提升至正文\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-N2\"\n  summary: \"'penalty-independent' 表述误导：72% death-asymmetry labels 在 P=0 时退化为 ties\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N2 首提，R2 强烈同意。54/75 death-asymmetry episodes 中 surviving strategy scored zero。labeling-function-level independence ≠ practical-value-level independence。P=0 时 effective non-tie labels 仅 41 个，death-asymmetry fraction 降至 21/41=51.2%。\"\n  action_items:\n    - round: 17\n      action: \"(1) §2.3 或 §3.1 明确区分 labeling-function-level vs practical-value-level penalty independence; (2) 报告 P=0 effective non-tie count (41) 和 death fraction (51.2%) 作为 lower bound; (3) 讨论 routing value 对 P>0 的依赖\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic mixed-strategy routing 的影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W1 首提，R2 同意但认为 diagnostic framing 部分缓解。42.9% internal death rate 是 pure-strategy worst-case，mixed-strategy 中偶尔切换 deterministic 可能大幅降低 death rate。Distribution shift (DAgger 2011) 已引用但未量化 transferability gap。\"\n  action_items:\n    - round: 17\n      action: \"Discussion 增加一段讨论 pure-strategy diagnostic vs mixed-strategy deployment 的 gap\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Figure 1 (scatter plot) caption 缺 'mathematical consequence' caveat\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W2 首提，R2 同意。正文 §3.1 已解释但 Figure caption 独立阅读时缺少 caveat。\"\n  action_items:\n    - round: 17\n      action: \"Figure 1 caption 添加 'Note: this correlation is structurally implied by the decomposition (§3.1)'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W3\"\n  summary: \"Data scaling ablation 的 'structural failure' 结论基于 paraphrase augmentation 而非 real data\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W6 首提，R2 同意。Appendix F 25%-800% scaling 用 paraphrase augmentation 不生成新 routing patterns。'structural failure' 应弱化为 'failure under current data regime'。论文承认 real-data scaling 是 open question。\"\n  action_items:\n    - round: 17\n      action: \"Appendix F 和 §3.7 将 'structural' 改为 'under current data distribution / augmentation regime'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Related Work §5 第一段有论文罗列倾向\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W5 首提，R1 同意。Toolformer→ToolkenGPT→ART→Chameleon→ReTool→ToolACE 连续列举。应按功能类别做 comparative positioning。\"\n  action_items:\n    - round: 17\n      action: \"Related Work 第一段按功能类别重组（self-supervised / token-level / task-level / RL-based）\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry (altman1999cmdp) + ART 等条目需更新为正式出版信息\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"altman1999cmdp 在 references.bib 中存在但未被 .tex 引用。ART (2023) 为 arXiv preprint 但已正式发表。\"\n  action_items:\n    - round: 17\n      action: \"删除 altman1999cmdp orphan entry；更新 ART 等已发表论文的 bib 条目\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "## Round 17 Review Issues (updated 2026-05-19 R17 fresh consolidated report)\n\n# =============================================\n# Resolved issues from prior rounds (unchanged)\n# =============================================\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。\"\n    - round: 16\n      reviewers: []\n      note: \"R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。\"\n  resolution: \"78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence\"\n  resolution_round: 15\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化 27.7% mislabeling fraction\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"引用覆盖充分，orphan entries 已清理\"\n  resolution_round: 15\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld + MATH N 标注不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及 minority-class diversity confound\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'，structural 仅用于 router failure 的 Appendix 描述\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n# =============================================\n# Open / in_progress issues (updated with R17)\n# =============================================\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11、per-task n=20\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. Cluster bootstrap K=11 违反 K>=40 要求。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 divergence on severity. 降级为 warning。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 consensus. Cautionary language 和 Cameron 2008 引用到位。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1 标为 Must-Fix (CI [73%,100%] 过宽，cluster exchangeability 受限)。R2 rebut 降为 Should-Fix (Cohen's d=3.02, exact permutation p=0.002 不依赖 asymptotic assumptions)。Director 裁决：维持 warning。方向性结论 robust，magnitude 精度有限但 CI 下界仍排除 50%。建议正文提升 Cohen's d。\"\n  action_items:\n    - round: 13\n      action: \"对 cluster bootstrap K=11 做更诚实讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 17\n      action: \"将 Cohen's d=3.02 从 Appendix 提升至正文 §3.1；明确 primary CI 为 episode-level bootstrap，cluster-level CI 为 sensitivity analysis\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"约 200 词中 10+ 统计量。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍含 12+ 数字。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus. ~140 词中约 12 个数字。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 consensus. 当前 ~140 词中 8+ 数字。R1/R2 均建议保留 78.9% 和 p=0.81，其余改为定性概括。\"\n  action_items:\n    - round: 17\n      action: \"Abstract 保留 78.9%、DAF 90.4%、p=0.81 三个关键数字；retry/scaling/Reflexion 具体数字改为定性描述\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 认为 78.9% 也 trivial；R1 认为 δ=0.265 是 empirical 非先验可知。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus (critical). back-of-envelope 可预测 death dominance。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 consensus. R2-N1: DAF 是数学必然，78.9% 是 Algorithm 1 设计产物。R1 同意 framing 问题但认为框架的 diagnostic procedure 本身有价值。两人均认为 reframing 为 'death dominance resists interventions' 可提升 novelty perception。\"\n  action_items:\n    - round: 17\n      action: \"核心叙事 reframe: 强调 intervention robustness (δ persists under retry/Reflexion/scaling/filtering) 而非 death dominance 本身的发现\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 consensus.\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-W2 再提 MATH negative control 的 tautological 质疑。R1 rebut: MATH 是有效 boundary probe (p=0.81 是具体实证检验)，但同意模态定义差异应更 prominently 讨论。Director: 同意 R1——MATH 不是 tautological，但 comparability limitation 应在 Table caption + §3.5 明确标注。\"\n  action_items:\n    - round: 17\n      action: \"Table 2 caption 逐项注明每环境 deterministic 的具体含义 (oracle simulator / code interpreter / admissible actions)\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及此 issue。R1-W4 讨论了 mislabeling 对 78.9% 的影响但 R2 rebut 认为 episode-level metric 不受 step-level mislabeling 影响。可能已充分处理。\"\n  action_items:\n    - round: 16\n      action: \"§3.7 补充 oracle margin 与 mislabeling 的独立性讨论\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M1\"\n  summary: \"缺少 permadeath 环境 LLM agent 工作引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"ToolACE, Inner Monologue, Tamar 2015 已补充。NetHack/Crafter LLM agent 工作仍缺。\"\n    - round: 17\n      reviewers: [1]\n      note: \"R17 R1 未单独提及缺失引用，建议 HuggingGPT, CREATOR, SafeDreamer。R2 建议 ToolBench。\"\n  action_items:\n    - round: 17\n      action: \"检查并补充 LLM agent in permadeath environments 引用（BALROG 和 NetPlay 已有，可能足够）\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit: death dominance 在 ScienceWorld penalty 结构下可从 back-of-envelope 预测\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Strong consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 strong consensus. R2 Excitement 2.5/5，R1 3/5。两人均认为框架方法论有价值但 empirical finding 可预期。Reframe 方向：'death dominance resists standard interventions' 比 'death dominates routing signal' 更有 novelty。R1 补充：agent improvement baselines 的 robustness 是事前不可预测的。\"\n  action_items:\n    - round: 17\n      action: \"(1) Reframe Introduction/Abstract 核心叙事从 finding 转向 methodology + intervention robustness; (2) Discussion 增加 'what was not predictable: intervention failure ceiling'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"63% exclusion 意味着 death dominance 可能仅适用于 ScienceWorld 特定 task subset。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-W4 再提 n=5 prescreening 的局限。R1 同意但 caveat: anti-cherry-picking 需方向性证据，18/19 excluded tasks 方向一致（Table 5），sign-test 级别可信。Director: 论证充分但应在正文（非仅 Appendix）明确 63% exclusion 为 scope limitation。\"\n  action_items:\n    - round: 17\n      action: \"§3 开头段明确标注 63% exclusion 是 scope limitation 而非仅在 Limitations 提及\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N3\"\n  summary: \"实验规模和环境多样性不足: 缺少 permadeath 环境 replication (NetHack/Crafter)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"两位 reviewer 均认为这是影响 Conference vs Findings 定位的关键因素。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 strong consensus. R1-W5 和 R2-N2 独立提出。R2 进一步指出 100% deaths 来自同一 action pattern (focus on)，无法区分 ScienceWorld idiosyncratic vs generalizable。两人均认为补充第二个 permadeath 环境是从 Findings 提升至 Conference 的关键。\"\n  action_items:\n    - round: 17\n      action: \"(1) NetHack 或 Crafter pilot (N>=50) 是升级至 Conference 的关键; (2) 如无法执行，Discussion 中更 prominently 讨论 ScienceWorld-specific factors (固定 P=100, 单一 fatal action pattern, text-based interface)\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"§3.3 将 72B DAF=90.9% 直接与 7B DAF=90.4% 比较时未强调 population 差异。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W3 + R2-W3 consensus。72B 实验设计不明确——deterministic strategy 使用什么模型？72B deterministic death rate 未报告。72B 未做完整 framework replication。\"\n  action_items:\n    - round: 17\n      action: \"(1) 明确 72B 实验设计 (deterministic strategy model); (2) 报告 72B deterministic death rate 和 Δ_nd; (3) 注明 population 差异 (10 vs 11 tasks)\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"0.6B=50.7%, 1.7B=43.1%, 4B=59.0%。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及此 issue。可能被 router diagnostic 整体评价覆盖。\"\n  action_items:\n    - round: 16\n      action: \"补充 1.7B per-class confusion matrix 或弱化解释\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"该图是 cross-env label distribution 对比图。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及，但当前版本 Appendix I 已引用 signal_reversal.pdf (Figure 4)。待确认引用是否正式。\"\n  action_items:\n    - round: 16\n      action: \"正式引入或删除 signal_reversal.pdf\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载（覆盖 finding + robustness + router diagnostic）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 首提，R1 同意。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-N3 升为 Must-Fix。R1 rebut: 三个子成分形成因果链，拆分制造冗余，这是 editorial 调整而非 critical flaw。Director 裁决：维持 warning——合理关切但不影响接收决定。建议将 router diagnostic 移入 Contribution 1。\"\n  action_items:\n    - round: 17\n      action: \"将 router-as-diagnostic-probe 从 Contribution 2 移至 Contribution 1（方法论部分），减轻 C2 负载\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致 (find-non-living vs find-non-living-thing)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及，待确认是否已修复。\"\n  action_items:\n    - round: 16\n      action: \"统一 task name\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# =============================================\n# Round 17 New Issues\n# =============================================\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction 在 task level 呈现 binary split (death-prone 100%, death-free 0%)，aggregate 是 task composition artifact\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N1 首提，R2 强烈同意。LOTO-DAF (Appendix D) 显示移除 find-non-living-thing 后 DAF→100%。10 个 death-prone 任务各贡献 100% death-asymmetry labels。aggregate 78.9% 可通过增减 death-free 任务数量任意改变。框架的真正诊断输出是 binary classification 而非连续百分比。\"\n  action_items:\n    - round: 17\n      action: \"(1) §3.1 增加 1-2 句明确指出 binary per-task structure; (2) 讨论框架诊断输出的 binary vs continuous 性质; (3) LOTO-DAF 关键结论提升至正文\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-N2\"\n  summary: \"'penalty-independent' 表述误导：72% death-asymmetry labels 在 P=0 时退化为 ties\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N2 首提，R2 强烈同意。54/75 death-asymmetry episodes 中 surviving strategy scored zero。labeling-function-level independence ≠ practical-value-level independence。P=0 时 effective non-tie labels 仅 41 个，death-asymmetry fraction 降至 21/41=51.2%。\"\n  action_items:\n    - round: 17\n      action: \"(1) §2.3 或 §3.1 明确区分 labeling-function-level vs practical-value-level penalty independence; (2) 报告 P=0 effective non-tie count (41) 和 death fraction (51.2%) 作为 lower bound; (3) 讨论 routing value 对 P>0 的依赖\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic mixed-strategy routing 的影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W1 首提，R2 同意但认为 diagnostic framing 部分缓解。42.9% internal death rate 是 pure-strategy worst-case，mixed-strategy 中偶尔切换 deterministic 可能大幅降低 death rate。Distribution shift (DAgger 2011) 已引用但未量化 transferability gap。\"\n  action_items:\n    - round: 17\n      action: \"Discussion 增加一段讨论 pure-strategy diagnostic vs mixed-strategy deployment 的 gap\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Figure 1 (scatter plot) caption 缺 'mathematical consequence' caveat\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W2 首提，R2 同意。正文 §3.1 已解释但 Figure caption 独立阅读时缺少 caveat。\"\n  action_items:\n    - round: 17\n      action: \"Figure 1 caption 添加 'Note: this correlation is structurally implied by the decomposition (§3.1)'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W3\"\n  summary: \"Data scaling ablation 的 'structural failure' 结论基于 paraphrase augmentation 而非 real data\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W6 首提，R2 同意。Appendix F 25%-800% scaling 用 paraphrase augmentation 不生成新 routing patterns。'structural failure' 应弱化为 'failure under current data regime'。论文承认 real-data scaling 是 open question。\"\n  action_items:\n    - round: 17\n      action: \"Appendix F 和 §3.7 将 'structural' 改为 'under current data distribution / augmentation regime'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Related Work §5 第一段有论文罗列倾向\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W5 首提，R1 同意。Toolformer→ToolkenGPT→ART→Chameleon→ReTool→ToolACE 连续列举。应按功能类别做 comparative positioning。\"\n  action_items:\n    - round: 17\n      action: \"Related Work 第一段按功能类别重组（self-supervised / token-level / task-level / RL-based）\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry (altman1999cmdp) + ART 等条目需更新为正式出版信息\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"altman1999cmdp 在 references.bib 中存在但未被 .tex 引用。ART (2023) 为 arXiv preprint 但已正式发表。\"\n  action_items:\n    - round: 17\n      action: \"删除 altman1999cmdp orphan entry；更新 ART 等已发表论文的 bib 条目\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-19T11:27:54.439297+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 21031}, \"error\": \"\"}"}

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

_source line 1432 · 2026-05-19T11:29:49.102351+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 17 Consolidated Review Report (Fresh)\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**目标 Venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review May cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh (完全独立初审)\n**Reviewer 编排**: 2 人 (R1: 方法/实验/统计; R2: 新颖性/完整性/写作)\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，通过 dual-metric 设计（penalty-independent label fraction 和 penalty-dependent DAF）分解 modular LLM agent 的 routing signal。在 ScienceWorld（11/30 task types, 245 episodes, Qwen2.5-7B）上发现 78.9% 的 non-tie routing labels 来自 death asymmetry（DAF = 90.4%）。跨模型（Llama-3.1-8B, N=220）和跨环境（MATH N=795, ALFWorld N=135）验证支持框架的诊断能力。四种 agent improvement 干预（retry, Reflexion, 10× scaling, action-space filtering）均未消除 death dominance。Router training 的 negative result 进一步验证了 routing 在 death-dominant 环境中的近退化性。\n\n---\n\n## Strengths\n\n**S1. 方法设计干净，dual-metric 设计是核心方法论贡献。** 同时报告 penalty-independent label fraction (78.9%) 和 penalty-dependent DAF (90.4%)，并在 §2.4 主动标注 DAF 随 P 单调递增是 \"mathematical consequence\"。这种自我校正式的透明度在投稿论文中少见。[R1 S2, R2 同意]\n\n**S2. Anti-cherry-picking 分析异常充分。** Table 5 展示 19 个被排除任务的 death-rate differential (mean +38.2 pp) 高于 included tasks (+28.7 pp)，直接排除 selection bias。[R1 S3, R2 同意]\n\n**S3. 统计方法严谨度超出 NLP 论文平均水平。** Wild cluster bootstrap, exact permutation, sign test, LOO correlation, LOTO-DAF, 8-seed cross-validation, bootstrap CIs 形成完整的 robustness 论证链。[R1 S4, R2 优势段]\n\n**S4. Negative results 解释自洽且具诊断价值。** Router episode-level failure (47.1±2.2%, below chance) 和 MATH null (p=0.81) 不是失败，而是框架诊断能力的正向验证。[R1 S5, R2 同意]\n\n**S5. 多轴 agent improvement baselines 增强 robustness 论证。** Retry + Reflexion + 10× scaling + action-space filtering 四条独立干预路径，加上 dose-response analysis。[R1 S6]\n\n**S6. Practitioner decision framework 有实际工程指导价值。** Discussion 的 50-episode pilot 建议 + MATH negative control 的验证 = 可操作的工程决策流程。[R2 优势段]\n\n---\n\n## Weaknesses (按严重程度排序)\n\n### Critical (影响接收决定)\n\n**C1. [Consensus] 78.9% label fraction 在 task level 是 binary split，aggregate 是 task composition artifact。**\nLOTO-DAF (Appendix D) 揭示：移除唯一 death-free 任务后 DAF→100%。10 个 death-prone 任务各贡献 100% death-asymmetry labels，1 个 death-free 任务贡献 0%。headline 78.9% 是 10:1 task ratio 的直接产物，增减 death-free 任务即可任意改变该百分比。框架的真正诊断输出可能不是连续百分比而是 binary classification（\"此环境是否 death-dominated\"），但论文未讨论这一 structure。[R1-N1, R2-N1 强烈同意]\n\n**C2. [Consensus] \"penalty-independent\" 表述具有误导性。**\n72% 的 death-asymmetry labels (54/75) 在 P=0 时退化为 ties（surviving strategy 也 scored zero）。78.9% 是 labeling function 形式化产物；routing 的实际收益依赖 P>0。P=0 时 effective non-tie labels 仅 41 个，death-asymmetry fraction 降至 21/41=51.2%。需区分 labeling-function-level independence 和 practical-value-level dependence。[R1-N2, R2-N1 交叉同意]\n\n**C3. [Consensus] 单一灾难性失败环境 + 单一失败模式，泛化性不足。**\n100% 的 internal-strategy 死亡来自同一 action pattern（`focus on` 误用, Appendix H）。MATH 和 ALFWorld 均无 catastrophic death，不构成 death-dominance replication。论文自认 NetHack/Crafter 为 \"most direct replication targets\" 但未执行。无法区分这是 ScienceWorld idiosyncratic 结果还是可泛化现象。**补充第二个 permadeath 环境是从 Findings 提升至 Conference 的关键条件。** [R1-W5, R2-N2, 交叉后双方强烈同意]\n\n**C4. [Consensus] 核心发现 novelty/excitement deficit。**\nDAF = δP/(δP+Δ_nd) 在给定 δ=0.265, P=100, Δ_nd=2.84 后是代数必然。78.9% 本质上是 \"多少 non-tie episodes 有 death asymmetry\" 的重新表述。真正 non-trivial 的部分是 intervention robustness（Reflexion 仅降至 31.4%，72B 仅降至 34.5%），但论文 framing 将 discovery emphasis 放在 dominance 而非 persistence 上。[R2-N1, R1 交叉同意 framing 问题; R1 Excitement 3/5, R2 2.5/5]\n\n### Warning (影响评分但不一票否决)\n\n**W1. [Consensus] Abstract 数字堆砌。** ~140 词中 8+ 个数字，信息密度过高。建议保留 78.9%、DAF 90.4%、p=0.81 三个关键数字，其余改为定性描述。[R1 minor, R2-W1]\n\n**W2. [Consensus] 72B 实验设计细节不完整。** Deterministic strategy 使用什么模型未说明；72B deterministic death rate 和 Δ_nd 未报告；72B vs 7B DAF 对比基于不同 task population (10 vs 11 tasks) 未标注。[R1-W3, R2-W3]\n\n**W3. [Consensus] 跨环境 \"deterministic\" 模态定义不一致。** ScienceWorld (oracle simulator), MATH (code interpreter), ALFWorld (admissible actions) 三种 \"deterministic\" 质性不同。Table 2 caption 未标注 comparability limitation。[R2-W2, R1 partial agree]\n\n**W4. [Consensus] Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响。** 42.9% internal death rate 是 worst-case；mixed-strategy 中偶尔切换 deterministic 可能大幅降低 death rate。DAgger 引用但未量化 transferability gap。[R1-W1, R2 同意]\n\n**W5. [Consensus] Data scaling \"structural failure\" 结论基于 paraphrase augmentation 而非 real data。** 25%-800% scaling 不生成新 routing patterns，应弱化为 \"failure under current data regime\"。[R1-W6, R2 同意]\n\n**W6. [Director 裁决] K=11 cluster 推断可靠性。** R1 标为 Must-Fix，R2 rebut 降为 Should-Fix（Cohen's d=3.02, exact permutation p=0.002 不依赖 asymptotic assumptions）。**Director 裁决：Warning。** 方向性结论 robust，magnitude 精度有限但 CI 下界 73% 仍排除 50%。建议将 Cohen's d 提升至正文。\n\n**W7. [Director 裁决] Contribution 2 过载。** R2 标为 Must-Fix，R1 rebut 为 editorial。**Director 裁决：Warning。** 合理关切但不影响接收。建议将 router-as-diagnostic-probe 移入 Contribution 1。\n\n### Minor\n\n**M1.** Figure 1 (scatter) caption 缺 \"mathematical consequence\" caveat。[R1-W2, R2 同意]\n**M2.** Related Work 第一段 6 citations 连续列举，应按功能类别重组。[R2-W5, R1 同意]\n**M3.** Orphan bib entry (altman1999cmdp)；ART 等条目需更新为正式出版信息。[R2 格式]\n**M4.** Abstract 中 \"Retry yields only marginal reduction (43.5%)\" 括号内是 post-retry death rate 非 reduction 量，首次阅读有歧义。[R1 minor]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉回应后达成一致：\n\n1. **[AGREE] 78.9% binary task-level structure** — aggregate 是 task composition artifact，需在正文讨论\n2. **[AGREE] \"penalty-independent\" 误导** — P=0 时 72% labels 退化为 ties，需区分形式化 vs 实用价值\n3. **[AGREE] 缺少第二个 permadeath 环境** — Conference vs Findings 的关键分水岭\n4. **[AGREE] Novelty framing 问题** — 应从 \"death dominates\" 转向 \"death dominance resists interventions\"\n5. **[AGREE] Abstract 数字堆砌** — 保留 2-3 个关键数字\n6. **[AGREE] 72B 实验细节不完整** — 需澄清 deterministic model、报告完整 decomposition\n7. **[AGREE] Related Work 罗列** — 需按功能类别重组\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 裁决 |\n|------|----|----|---------------|\n| K=11 cluster 推断 | Must-Fix (CI 过宽) | Should-Fix (Cohen's d 足够) | **Warning** — 方向性 robust，提升 Cohen's d 至正文 |\n| Contribution 2 过载 | Editorial, not critical | Must-Fix | **Warning** — 建议重组但非 critical |\n| MATH tautological? | Rebut (有效 boundary probe) | Tautological | **R1 正确** — p=0.81 是具体实证，但需标注模态差异 |\n| 27.7% mislabeling 影响 78.9%? | 需讨论 | 不影响 (episode-level) | **R2 正确** — 78.9% 是 episode-level metric |\n\n---\n\n## Questions for Authors\n\n**Q1.** [R1] 72B 实验中 deterministic strategy 使用的是 72B 还是 7B？72B deterministic death rate 和 Δ_nd 是多少？\n\n**Q2.** [R1] find-non-living-thing n=40（其他任务 n=20）——加倍 episodes 的决策是否在看到初始结果后做出的？如果是，这构成 data-dependent inclusion 的轻微风险。\n\n**Q3.** [R1] Reflexion 在将 death rate 从 42.9% 降至 31.4% 的同时，Δ_nd 是否也发生了变化？\n\n**Q4.** [R1] 正文 DAF 95% CI [81.6%, 98.8%] 是 episode-level 还是 cluster-level bootstrap？如果是前者，可能低估 uncertainty。\n\n**Q5.** [R1] Discussion 中 inverted-U hypothesis（~0.5B 以下 agents 无法到达危险状态）仅基于 15 episodes，有更多数据支持吗？\n\n---\n\n## Missing References\n\nR1 建议：HuggingGPT / TaskMatrix (Shen et al., 2023)、CREATOR (Qian et al., 2023)、SafeDreamer (Huang et al., 2024)\nR2 建议：ToolBench (Qin et al., 2023)\n共同关注：LLM agents in permadeath environments（已引 BALROG + NetPlay，但 NetHack/Crafter 的 LLM agent 实验性工作如有则应引用）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 config 中无 `external_review.paperreview_ai.enabled` 设置）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Soundness | 4/5 | 3.5/5 | 4/5 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由：**\n\n本文方法论贡献扎实（dual-metric diagnostic framework + router-as-diagnostic-probe），统计分析严谨程度超出 NLP 论文平均水平，negative results 报告诚实。但以下因素限制了 Conference 水平的定位：\n\n1. **核心发现新颖性有限**（C4）：death dominance 在明确 penalty 结构后 back-of-envelope 可预测，两个核心指标的\"发现\"属性被高估\n2. **单一环境 + 单一失败模式**（C3）：100% deaths 来自同一 action pattern，无第二个 permadeath 环境验证\n3. **headline metric 的结构性问题**（C1, C2）：78.9% 是 binary task-composition artifact，\"penalty-independent\" 表述实际依赖 P>0\n\n**Findings 定位的积极因素：** 框架的诊断 procedure 可复用于其他环境；四轴 agent improvement baselines 的 robustness 论证是 non-trivial 的贡献；practitioner decision framework 有工程价值。\n\n**升级至 Borderline Conference (3.5) 的路径：**\n1. 补充 NetHack 或 Crafter 的 N≥50 pilot study（最关键）\n2. 将核心叙事 reframe 为 \"death dominance resists standard interventions\"\n3. 在 §3.1 明确讨论 78.9% 的 binary per-task structure 和 P=0 lower bound (51.2%)\n\n---\n\n## Detailed Comments (按章节)\n\n### Abstract\n- 数字密度过高（8+ 数字/~140 词），建议削减至 3 个关键数字 [W1]\n- \"Retry yields only marginal reduction (43.5%)\" 歧义——改为 \"from 48.0% to 43.5%\" [M4]\n\n### Introduction\n- 叙事线清晰（问题→假设→框架→发现→贡献），无结构性问题\n- Contribution 2 过载（86 词），建议重组 [W7]\n- 核心 framing 应从 \"death dominates\" 转向 \"death dominance resists interventions\" [C4]\n\n### Method (§2)\n- Counterfactual episode collection 设计合理，97.4% tie rate 充分论证了 episode-level 方法的必要性\n- Algorithm 1 的 death-first priority 是合理语义（death=-100 vs alive≥0）\n- DAF 定义数学上清晰，penalty sensitivity analysis (Appendix G) 完整\n- 需区分 labeling-function-level vs practical-value-level penalty independence [C2]\n\n### Experiments (§3)\n- §3.1: 需讨论 78.9% 的 binary per-task structure [C1]；Cohen's d=3.02 应提升至正文 [W6]\n- §3.2: Cross-model replication (Llama-3.1-8B) 可信\n- §3.3: 72B 实验设计需澄清 [W2]；DAF recomputation 需报告完整 decomposition\n- §3.4-3.5: MATH negative control 有效但需标注模态定义差异 [W3]\n- §3.7: \"structural failure\" 应弱化为 \"under current data regime\" [W5]\n\n### Related Work (§5)\n- 第一段 6 citations 连续罗列，应按功能类别重组 [M2]\n- 引用覆盖基本充分；建议考虑 HuggingGPT, ToolBench\n\n### Discussion (§4)\n- Practitioner decision framework 有价值\n- Non-triviality 论证应聚焦 intervention robustness 而非 death dominance 本身 [C4]\n- 需增加 pure-strategy vs mixed-strategy gap 的讨论 [W4]\n\n### Limitations\n- 结构清晰（三个 paragraph headers），覆盖 scope/method/stats\n- 63% task exclusion 应在正文（非仅 Limitations）提及\n\n### Format\n- ACL template 正确，匿名化完整，正文 ~8 页合规\n- Orphan bib entry (altman1999cmdp) [M3]\n- Responsible NLP Checklist 填写充分",
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
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
    "report": "# Round 17 Consolidated Review Report (Fresh)\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**目标 Venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review May cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh (完全独立初审)\n**Reviewer 编排**: 2 人 (R1: 方法/实验/统计; R2: 新颖性/完整性/写作)\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，通过 dual-metric 设计（penalty-independent label fraction 和 penalty-dependent DAF）分解 modular LLM agent 的 routing signal。在 ScienceWorld（11/30 task types, 245 episodes, Qwen2.5-7B）上发现 78.9% 的 non-tie routing labels 来自 death asymmetry（DAF = 90.4%）。跨模型（Llama-3.1-8B, N=220）和跨环境（MATH N=795, ALFWorld N=135）验证支持框架的诊断能力。四种 agent improvement 干预（retry, Reflexion, 10× scaling, action-space filtering）均未消除 death dominance。Router training 的 negative result 进一步验证了 routing 在 death-dominant 环境中的近退化性。\n\n---\n\n## Strengths\n\n**S1. 方法设计干净，dual-metric 设计是核心方法论贡献。** 同时报告 penalty-independent label fraction (78.9%) 和 penalty-dependent DAF (90.4%)，并在 §2.4 主动标注 DAF 随 P 单调递增是 \"mathematical consequence\"。这种自我校正式的透明度在投稿论文中少见。[R1 S2, R2 同意]\n\n**S2. Anti-cherry-picking 分析异常充分。** Table 5 展示 19 个被排除任务的 death-rate differential (mean +38.2 pp) 高于 included tasks (+28.7 pp)，直接排除 selection bias。[R1 S3, R2 同意]\n\n**S3. 统计方法严谨度超出 NLP 论文平均水平。** Wild cluster bootstrap, exact permutation, sign test, LOO correlation, LOTO-DAF, 8-seed cross-validation, bootstrap CIs 形成完整的 robustness 论证链。[R1 S4, R2 优势段]\n\n**S4. Negative results 解释自洽且具诊断价值。** Router episode-level failure (47.1±2.2%, below chance) 和 MATH null (p=0.81) 不是失败，而是框架诊断能力的正向验证。[R1 S5, R2 同意]\n\n**S5. 多轴 agent improvement baselines 增强 robustness 论证。** Retry + Reflexion + 10× scaling + action-space filtering 四条独立干预路径，加上 dose-response analysis。[R1 S6]\n\n**S6. Practitioner decision framework 有实际工程指导价值。** Discussion 的 50-episode pilot 建议 + MATH negative control 的验证 = 可操作的工程决策流程。[R2 优势段]\n\n---\n\n## Weaknesses (按严重程度排序)\n\n### Critical (影响接收决定)\n\n**C1. [Consensus] 78.9% label fraction 在 task level 是 binary split，aggregate 是 task composition artifact。**\nLOTO-DAF (Appendix D) 揭示：移除唯一 death-free 任务后 DAF→100%。10 个 death-prone 任务各贡献 100% death-asymmetry labels，1 个 death-free 任务贡献 0%。headline 78.9% 是 10:1 task ratio 的直接产物，增减 death-free 任务即可任意改变该百分比。框架的真正诊断输出可能不是连续百分比而是 binary classification（\"此环境是否 death-dominated\"），但论文未讨论这一 structure。[R1-N1, R2-N1 强烈同意]\n\n**C2. [Consensus] \"penalty-independent\" 表述具有误导性。**\n72% 的 death-asymmetry labels (54/75) 在 P=0 时退化为 ties（surviving strategy 也 scored zero）。78.9% 是 labeling function 形式化产物；routing 的实际收益依赖 P>0。P=0 时 effective non-tie labels 仅 41 个，death-asymmetry fraction 降至 21/41=51.2%。需区分 labeling-function-level independence 和 practical-value-level dependence。[R1-N2, R2-N1 交叉同意]\n\n**C3. [Consensus] 单一灾难性失败环境 + 单一失败模式，泛化性不足。**\n100% 的 internal-strategy 死亡来自同一 action pattern（`focus on` 误用, Appendix H）。MATH 和 ALFWorld 均无 catastrophic death，不构成 death-dominance replication。论文自认 NetHack/Crafter 为 \"most direct replication targets\" 但未执行。无法区分这是 ScienceWorld idiosyncratic 结果还是可泛化现象。**补充第二个 permadeath 环境是从 Findings 提升至 Conference 的关键条件。** [R1-W5, R2-N2, 交叉后双方强烈同意]\n\n**C4. [Consensus] 核心发现 novelty/excitement deficit。**\nDAF = δP/(δP+Δ_nd) 在给定 δ=0.265, P=100, Δ_nd=2.84 后是代数必然。78.9% 本质上是 \"多少 non-tie episodes 有 death asymmetry\" 的重新表述。真正 non-trivial 的部分是 intervention robustness（Reflexion 仅降至 31.4%，72B 仅降至 34.5%），但论文 framing 将 discovery emphasis 放在 dominance 而非 persistence 上。[R2-N1, R1 交叉同意 framing 问题; R1 Excitement 3/5, R2 2.5/5]\n\n### Warning (影响评分但不一票否决)\n\n**W1. [Consensus] Abstract 数字堆砌。** ~140 词中 8+ 个数字，信息密度过高。建议保留 78.9%、DAF 90.4%、p=0.81 三个关键数字，其余改为定性描述。[R1 minor, R2-W1]\n\n**W2. [Consensus] 72B 实验设计细节不完整。** Deterministic strategy 使用什么模型未说明；72B deterministic death rate 和 Δ_nd 未报告；72B vs 7B DAF 对比基于不同 task population (10 vs 11 tasks) 未标注。[R1-W3, R2-W3]\n\n**W3. [Consensus] 跨环境 \"deterministic\" 模态定义不一致。** ScienceWorld (oracle simulator), MATH (code interpreter), ALFWorld (admissible actions) 三种 \"deterministic\" 质性不同。Table 2 caption 未标注 comparability limitation。[R2-W2, R1 partial agree]\n\n**W4. [Consensus] Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响。** 42.9% internal death rate 是 worst-case；mixed-strategy 中偶尔切换 deterministic 可能大幅降低 death rate。DAgger 引用但未量化 transferability gap。[R1-W1, R2 同意]\n\n**W5. [Consensus] Data scaling \"structural failure\" 结论基于 paraphrase augmentation 而非 real data。** 25%-800% scaling 不生成新 routing patterns，应弱化为 \"failure under current data regime\"。[R1-W6, R2 同意]\n\n**W6. [Director 裁决] K=11 cluster 推断可靠性。** R1 标为 Must-Fix，R2 rebut 降为 Should-Fix（Cohen's d=3.02, exact permutation p=0.002 不依赖 asymptotic assumptions）。**Director 裁决：Warning。** 方向性结论 robust，magnitude 精度有限但 CI 下界 73% 仍排除 50%。建议将 Cohen's d 提升至正文。\n\n**W7. [Director 裁决] Contribution 2 过载。** R2 标为 Must-Fix，R1 rebut 为 editorial。**Director 裁决：Warning。** 合理关切但不影响接收。建议将 router-as-diagnostic-probe 移入 Contribution 1。\n\n### Minor\n\n**M1.** Figure 1 (scatter) caption 缺 \"mathematical consequence\" caveat。[R1-W2, R2 同意]\n**M2.** Related Work 第一段 6 citations 连续列举，应按功能类别重组。[R2-W5, R1 同意]\n**M3.** Orphan bib entry (altman1999cmdp)；ART 等条目需更新为正式出版信息。[R2 格式]\n**M4.** Abstract 中 \"Retry yields only marginal reduction (43.5%)\" 括号内是 post-retry death rate 非 reduction 量，首次阅读有歧义。[R1 minor]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉回应后达成一致：\n\n1. **[AGREE] 78.9% binary task-level structure** — aggregate 是 task composition artifact，需在正文讨论\n2. **[AGREE] \"penalty-independent\" 误导** — P=0 时 72% labels 退化为 ties，需区分形式化 vs 实用价值\n3. **[AGREE] 缺少第二个 permadeath 环境** — Conference vs Findings 的关键分水岭\n4. **[AGREE] Novelty framing 问题** — 应从 \"death dominates\" 转向 \"death dominance resists interventions\"\n5. **[AGREE] Abstract 数字堆砌** — 保留 2-3 个关键数字\n6. **[AGREE] 72B 实验细节不完整** — 需澄清 deterministic model、报告完整 decomposition\n7. **[AGREE] Related Work 罗列** — 需按功能类别重组\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 裁决 |\n|------|----|----|---------------|\n| K=11 cluster 推断 | Must-Fix (CI 过宽) | Should-Fix (Cohen's d 足够) | **Warning** — 方向性 robust，提升 Cohen's d 至正文 |\n| Contribution 2 过载 | Editorial, not critical | Must-Fix | **Warning** — 建议重组但非 critical |\n| MATH tautological? | Rebut (有效 boundary probe) | Tautological | **R1 正确** — p=0.81 是具体实证，但需标注模态差异 |\n| 27.7% mislabeling 影响 78.9%? | 需讨论 | 不影响 (episode-level) | **R2 正确** — 78.9% 是 episode-level metric |\n\n---\n\n## Questions for Authors\n\n**Q1.** [R1] 72B 实验中 deterministic strategy 使用的是 72B 还是 7B？72B deterministic death rate 和 Δ_nd 是多少？\n\n**Q2.** [R1] find-non-living-thing n=40（其他任务 n=20）——加倍 episodes 的决策是否在看到初始结果后做出的？如果是，这构成 data-dependent inclusion 的轻微风险。\n\n**Q3.** [R1] Reflexion 在将 death rate 从 42.9% 降至 31.4% 的同时，Δ_nd 是否也发生了变化？\n\n**Q4.** [R1] 正文 DAF 95% CI [81.6%, 98.8%] 是 episode-level 还是 cluster-level bootstrap？如果是前者，可能低估 uncertainty。\n\n**Q5.** [R1] Discussion 中 inverted-U hypothesis（~0.5B 以下 agents 无法到达危险状态）仅基于 15 episodes，有更多数据支持吗？\n\n---\n\n## Missing References\n\nR1 建议：HuggingGPT / TaskMatrix (Shen et al., 2023)、CREATOR (Qian et al., 2023)、SafeDreamer (Huang et al., 2024)\nR2 建议：ToolBench (Qin et al., 2023)\n共同关注：LLM agents in permadeath environments（已引 BALROG + NetPlay，但 NetHack/Crafter 的 LLM agent 实验性工作如有则应引用）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 config 中无 `external_review.paperreview_ai.enabled` 设置）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Soundness | 4/5 | 3.5/5 | 4/5 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由：**\n\n本文方法论贡献扎实（dual-metric diagnostic framework + router-as-diagnostic-probe），统计分析严谨程度超出 NLP 论文平均水平，negative results 报告诚实。但以下因素限制了 Conference 水平的定位：\n\n1. **核心发现新颖性有限**（C4）：death dominance 在明确 penalty 结构后 back-of-envelope 可预测，两个核心指标的\"发现\"属性被高估\n2. **单一环境 + 单一失败模式**（C3）：100% deaths 来自同一 action pattern，无第二个 permadeath 环境验证\n3. **headline metric 的结构性问题**（C1, C2）：78.9% 是 binary task-composition artifact，\"penalty-independent\" 表述实际依赖 P>0\n\n**Findings 定位的积极因素：** 框架的诊断 procedure 可复用于其他环境；四轴 agent improvement baselines 的 robustness 论证是 non-trivial 的贡献；practitioner decision framework 有工程价值。\n\n**升级至 Borderline Conference (3.5) 的路径：**\n1. 补充 NetHack 或 Crafter 的 N≥50 pilot study（最关键）\n2. 将核心叙事 reframe 为 \"death dominance resists standard interventions\"\n3. 在 §3.1 明确讨论 78.9% 的 binary per-task structure 和 P=0 lower bound (51.2%)\n\n---\n\n## Detailed Comments (按章节)\n\n### Abstract\n- 数字密度过高（8+ 数字/~140 词），建议削减至 3 个关键数字 [W1]\n- \"Retry yields only marginal reduction (43.5%)\" 歧义——改为 \"from 48.0% to 43.5%\" [M4]\n\n### Introduction\n- 叙事线清晰（问题→假设→框架→发现→贡献），无结构性问题\n- Contribution 2 过载（86 词），建议重组 [W7]\n- 核心 framing 应从 \"death dominates\" 转向 \"death dominance resists interventions\" [C4]\n\n### Method (§2)\n- Counterfactual episode collection 设计合理，97.4% tie rate 充分论证了 episode-level 方法的必要性\n- Algorithm 1 的 death-first priority 是合理语义（death=-100 vs alive≥0）\n- DAF 定义数学上清晰，penalty sensitivity analysis (Appendix G) 完整\n- 需区分 labeling-function-level vs practical-value-level penalty independence [C2]\n\n### Experiments (§3)\n- §3.1: 需讨论 78.9% 的 binary per-task structure [C1]；Cohen's d=3.02 应提升至正文 [W6]\n- §3.2: Cross-model replication (Llama-3.1-8B) 可信\n- §3.3: 72B 实验设计需澄清 [W2]；DAF recomputation 需报告完整 decomposition\n- §3.4-3.5: MATH negative control 有效但需标注模态定义差异 [W3]\n- §3.7: \"structural failure\" 应弱化为 \"under current data regime\" [W5]\n\n### Related Work (§5)\n- 第一段 6 citations 连续罗列，应按功能类别重组 [M2]\n- 引用覆盖基本充分；建议考虑 HuggingGPT, ToolBench\n\n### Discussion (§4)\n- Practitioner decision framework 有价值\n- Non-triviality 论证应聚焦 intervention robustness 而非 death dominance 本身 [C4]\n- 需增加 pure-strategy vs mixed-strategy gap 的讨论 [W4]\n\n### Limitations\n- 结构清晰（三个 paragraph headers），覆盖 scope/method/stats\n- 63% task exclusion 应在正文（非仅 Limitations）提及\n\n### Format\n- ACL template 正确，匿名化完整，正文 ~8 页合规\n- Orphan bib entry (altman1999cmdp) [M3]\n- Responsible NLP Checklist 填写充分",
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-19T11:29:53.217205+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4114
}
```

</details>

---


### Assistant

_source line 1434 · 2026-05-19T11:30:01.905024+00:00_

**Round 17 审稿圆桌完成。**

**最终评分：3.0 (Findings)**

报告已投递给 Research Director。核心结论：

**4 个 Critical 问题（共识）：**
1. 78.9% 是 binary task-composition artifact（10 个 death-prone 任务 100% + 1 个 death-free 0%）
2. "penalty-independent" 表述误导——P=0 时 72% labels 退化为 ties，实际 lower bound 51.2%
3. 单一环境 + 单一失败模式（100% deaths 来自 `focus on` 误用），无 permadeath 环境验证
4. 核心发现 novelty 有限——DAF 在明确 penalty 结构后代数可预测

**升级路径（→ 3.5 Borderline Conference）：**
1. 补充 NetHack/Crafter N≥50 pilot（最关键）
2. Reframe 核心叙事：从 "death dominates" → "death dominance resists standard interventions"
3. 明确讨论 78.9% 的 binary structure 和 P=0 lower bound

Issue Tracker 已同步更新（`review_issues.yaml`，含 R17 新增 7 个 issue + 更新 10 个历史 issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 129

## Round 129

2 recorded events


### User

_source line 1435 · 2026-05-19T11:30:04.556295+00:00_

[Reviewer 2 审稿结果]:
交叉回应完成。

**回应总结**：

R1 的 3 个 Must-Fix 中：
- **[AGREE] N1 + N2**：78.9% 是 task composition 产物 + "penalty-independent" 误导（P=0 时 death fraction 仅 51.2%）。这两点与我的 N1 互相加强，是论文最核心的 framing 问题。
- **[REBUT] N3**：K=11 cluster 推断——Cohen's d=3.02 且 exact permutation p=0.002 不依赖 asymptotic assumptions，建议降为 Should-Fix。

R1 的 6 个 Should-Fix 中同意 5 个，反驳 W4（27.7% step-level mislabeling 不影响 episode-level 的 78.9%，是 level-of-analysis 混淆）。

评分差异（R1: 3.5 vs 我: 3.0）主要在 Excitement 维度。我维持 3.0，但认为如果作者补充 P=0 分析和第二个 permadeath 环境，3.5 可达。

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

_source line 1436 · 2026-05-19T11:30:16.417413+00:00_

审稿圆桌会议 Round 17 已完成。

**最终结果：Overall 3.0 (Findings)**

审稿报告已投递至 Research Director。Issue Tracker 已同步更新（新增 R17-N1/N2、R17-W1~W4、R17-M1，更新 8 个 open/in_progress 历史 issue）。

**核心结论摘要：**
- 4 个 Critical issues：78.9% binary structure、penalty-independent 误导、单环境+单失败模式、novelty deficit
- 7 个 Warning issues：Abstract 数字、72B 细节、跨环境模态差异、pure-strategy gap、data scaling 措辞、K=11 推断、Contribution 2 过载
- 升级至 3.5 的关键路径：补充 NetHack/Crafter pilot + reframe 核心叙事 + 讨论 P=0 lower bound

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 130

## Round 130

66 recorded events


### User

_source line 1437 · 2026-05-19T13:56:05.284316+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
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

_source line 1438 · 2026-05-19T13:56:11.561822+00:00_

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

_source line 1439 · 2026-05-19T13:56:11.663050+00:00_

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
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-19T13:56:17.953947+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,read_local_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
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
    "query": "select:director_get_project_overview,read_project_file,read_local_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1441 · 2026-05-19T13:56:18.004624+00:00_



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

_source line 1442 · 2026-05-19T13:56:22.180169+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-19T13:56:22.180618+00:00_



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

_source line 1444 · 2026-05-19T13:56:27.347888+00:00_

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

_source line 1445 · 2026-05-19T13:56:28.704890+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (111 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **minihack-cross-env-pilot** (negative): In MiniHack permadeath navigation environments, episode-level counterfactual analysis will reveal death dominance (internal DR significantly > deterministic DR), validating the diagnostic framework's cross-environment applicability beyond ScienceWorld. This tests whether death avoidance as the dominant routing signal is a general phenomenon of LLM agents in irreversible-failure environments, not an artifact of ScienceWorld's specific task design. ← 基于 plan-012-full\n- **backbone-scaling-70b** (success): 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 ← 基于 backbone-scaling-death-rate-0.5b\n  [72B DAF Decomposition Analysis](/api/workspace-files/projects/simgate-modular-routing/artifacts/backbone-scaling-70b/report/72b_daf_decomposition.md)\n- **llama-cross-model-full** (success): Death dominance mechanism (DAF ~78.9% on Qwen-7B) generalizes across model families: Llama-3.1-8B-Instruct on the same 11 ScienceWorld tasks will show (1) DAF direction consistent with Qwen, (2) similar death-prone vs non-death-prone task pattern, and (3) high per-task death ra
…[truncated 1667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-19T13:56:28.705546+00:00_

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

_source line 1447 · 2026-05-19T13:56:29.660605+00:00_

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
…[truncated 6240 chars]

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

_source line 1448 · 2026-05-19T13:56:29.661151+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
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
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1449 · 2026-05-19T13:56:30.463637+00:00_

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

_source line 1450 · 2026-05-19T13:56:30.679406+00:00_

-rw-r--r-- 1 ubuntu ubuntu 571631 May 19 13:16 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 215
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-19T13:56:36.471242+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found information about EMNLP 2025 
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6810
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-19T13:56:43.096070+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
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
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 1453 · 2026-05-19T13:56:43.598169+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline commitment deadline"
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
    "query": "EMNLP 2026 call for papers submission deadline commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 1454 · 2026-05-19T13:56:45.003516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "100",
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
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-19T13:56:45.509752+00:00_

100	\begin{table}[h]
101	\centering
102	\scriptsize
103	\setlength{\tabcolsep}{2.5pt}
104	\begin{tabular}{@{}lrrccc@{}}
105	\toprule
106	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
107	\midrule
108	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
109	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
110	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
111	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
112	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
113	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
114	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
115	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
116	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
117	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
118	\midrule
119	find-non-living-thing$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
120	\midrule
121	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
122	\bottomrule
123	\end{tabular}
124	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
125	\label{tab:per-task}
126	\end{table}
127	
128	\paragraph{Task selection and anti-cherry-picking.}
129	Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\%
…[truncated 5592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 506
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-19T13:56:45.710879+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "review_issues.yaml",
  "max_chars": "5000"
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
    "file": "review_issues.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1457 · 2026-05-19T13:56:49.375261+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

Based on the search results from aclrollingreview.org, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). Short papers have a 4 content pages maximum, while lo
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6279
}
```

</details>

---


### Tool result

_source line 1458 · 2026-05-19T13:56:56.463376+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/vi
…[truncated 1014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 12865
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-19T13:56:56.463746+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10752
}
```

</details>

---


### Tool call

_source line 1460 · 2026-05-19T13:57:00.755217+00:00_

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

_source line 1461 · 2026-05-19T13:57:00.755702+00:00_

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

_source line 1462 · 2026-05-19T13:57:06.047575+00:00_

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

_source line 1463 · 2026-05-19T13:57:06.952229+00:00_

1	## Round 17 Review Issues (updated 2026-05-19 D123 action matrix dispatched)
2	
3	# =============================================
4	# Resolved issues from prior rounds (unchanged)
5	# =============================================
6	
7	- id: "R13-N1"
8	  summary: "DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现"
9	  category: framing
10	  severity: critical
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 15
14	  mentions:
15	    - round: 13
16	      reviewers: [1, 2]
17	      note: "Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。"
18	    - round: 14
19	      reviewers: [1, 2]
20	      note: "R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。"
21	    - round: 15
22	      reviewers: [1, 2]
23	      note: "R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。"
24	    - round: 16
25	      reviewers: []
26	      note: "R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。"
27	  resolution: "78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence"
28	  resolution_round: 15
29	
30	- id: "R13-N3"
31	  summary: "跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication"
32	  category: experiment
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 13
36	  last_seen_round: 15
37	  resolution: "标题和 Contribution 措辞已恰当限定 scope"
38	  resolution_round: 15
39	
40	- id: "R13-W1"
41	  summary: "正文篇幅严重不足 long paper 要求"
42	  category: format
43	  severity: warning
44	  status: resolved
45	  first_raised_round: 13
46	  last_seen_round: 14
47	  resolution: "正文已扩展至 8 页"
48	  resolution_round: 14
49	
50	- id: "R13-W2"
51	  summary: "Router 训练实验存在多个 confound"
52	  category: experiment
53	  severity: warning
54	  status: resolved
55	  first_raised_round: 13
56	  last_seen_round: 15
57	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
58	  resolution_round: 15
59	
60	- id: "R13-W3"
61	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
62	  category: method
63	  severity: info
64	 
…[truncated 21817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1464 · 2026-05-19T13:57:06.952766+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for main conference papers submission format anonymity site:2026.emnlp.org"
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
    "query": "EMNLP 2026 call for main conference papers submission format anonymity site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1465 · 2026-05-19T13:57:07.454830+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/",
  "description": "List paper directory contents"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 1466 · 2026-05-19T13:57:07.505513+00:00_

SETUP_NOTES.md
_pdf_images_r5
abstract.tex
acl.sty
acl_natbib.bst
conclusion.tex
discussion.tex
experiments.tex
figures
introduction.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex
responsibleNLPchecklist.tex

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


### Tool result

_source line 1467 · 2026-05-19T13:57:13.129847+00:00_

Web search results for query: "EMNLP 2026 call for main conference papers submission format anonymity site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Guardians of the data: NER and LLMs for effective medical record anonymization in Brazilian Portuguese","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12813187/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"}]

Based on the search results from the EMNLP 2026 Call for Main Conference Papers page, here's what I found regarding submission format and anonymity:

**Anonymity Policy:**
Following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing process will continue to be double-blind, with reviewers not seeing authors, nor will authors see reviewers and reviews on ARR.

Authors will be given the option through ARR to make their anonymized submitted articles publicly visible.

**Submission Format:**
The page indicates that EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

**Deadlines:**
All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

For more detailed formatting specifications, you may want to visit the full Call for Main Conference Papers page at https://2026.emnlp.org/calls/main_conference_papers/ directly, as the search results don't include all the technical formatting deta
…[truncated 107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6177
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-19T13:57:42.629927+00:00_

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

_source line 1469 · 2026-05-19T13:57:43.082467+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \emph{what} drives routing decisions. We introduce an episode-level counterfactual framework that decomposes routing signal into death-avoidance and non-death components. Applied to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), \textbf{78.9\% of non-tie routing labels} arise from death asymmetry: the internal strategy's hallucination-induced failures trigger catastrophic agent death, while the deterministic strategy survives. This death dominance resists four representative intervention axes spanning retry, self-correction, $10{\times}$ parameter scaling, and action-space restriction; all reduce death rates yet none closes the gap to deterministic safety. A MATH evaluation ($N{=}795$, $p = 0.81$) confirms no routing signal without catastrophic failure. The framework reveals when catastrophic failure makes routing degenerate and when learned routers may add value.
3	\end{abstract}
4	

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

_source line 1470 · 2026-05-19T13:57:43.082935+00:00_

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

_source line 1471 · 2026-05-19T13:57:43.534288+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	Concurrent analyses of when and whether to invoke tools~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026} further presuppose diverse routing signals.
10	The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.
11	But no prior work has systematically decomposed what drives routing decisions in interactive environments. Without such a decomposition, the field cannot distinguish settings where diverse routing signals justify learned routers from tho
…[truncated 4256 chars]

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

_source line 1472 · 2026-05-19T13:57:43.534646+00:00_

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

_source line 1473 · 2026-05-19T13:57:43.785513+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\cite{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which modality to use at each step; our analysis investigates what signal is available to learn $\rho$. A reasoning-depth ablation ($n{=}120$) found no significant difference ($p > 0.26$; Appendix~\ref{app:ablations}).
10	
11	\subsection{Counterfactual Episode Collection}
12	\label{sec:collection}
13	
14	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-20
…[truncated 6032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 250
}
```

</details>

---


### Tool call

_source line 1474 · 2026-05-19T13:57:43.786123+00:00_

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

_source line 1475 · 2026-05-19T13:57:43.886947+00:00_

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
11	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types. This near-perfect correlation is structurally implied by the decomposition (\S\ref{sec:death-decomp}); see text for interpretation.}
12	\label{fig:decomposition}
13	\end{figure}
14	
15	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$, episode-level bootstrap, $B{=}10{,}000$; at the default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). Given observed $\delta = 0.265$ and $P = 100$, the predicted DAF $= \delta P / (\delta P + \Delta_{\text{nd}}) = 26.5 / 29.37 \approx 90.3\%$, closely matching the observed value; DAF is thus a derived quantity once $\delta$, $P$, and $\Delta_{\text{nd}}$ are known, while the 78.9\% label fraction is the penalty-independent empirical finding. Of these 75, 54 (72.0\%) reduce to ties when the death penalty is removed entirely: in those episodes, both modalities score zero without death, so the only reason one strategy outscored the other was avoiding the $-100
…[truncated 11483 chars]

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


### Tool call

_source line 1476 · 2026-05-19T13:57:49.110546+00:00_

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

_source line 1477 · 2026-05-19T13:57:49.613383+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10 of 11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step state trajectories, not individual action semantics. The 4B router's episode-level improvement ($59.0\%$) without step-level gains ($56$--$59\%$, flat) confirms that capacity scaling captures task-type classification rather than generalizable features. Cross-task-type transfer to physical-science tasks yields chance-level accuracy (49.2\%, 95\% CI $[42.4\%, 55.9\%]$; Appendix~\ref{app:ablations}), and 7 of 11 task types contain only deterministic-preferred labels, making majority-class collapse a structural consequence of the label distribution.
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance itself follows from the penalty structure (\S\ref{sec:daf}), its resistance to intervention was not predictable a priori. Four representative axes spanning retry, self-correction, parameter scaling, and action-space restriction all fail to close the gap to deterministic safety (16.3\%): Retry ($43.5\%$ at $N{=}5$), Reflexion ($34.0\%$ at $N{=}3$, plateauing at $34$--$36.5\%$), $10{\times}$ scaling ($31.4\%$, 72B, $N{=}255$), and action-space filtering ($29.0\%$; Appendix~\ref{app:grounding-ablation}). Action filtering and 72B scaling yield the strongest reductions yet still leave ${\geq}$12~pp residual gaps. Reflexion and scaling converge to overlapping 95\% Wilson CIs ($[27.8\%, 40.8\%]$ and $[26.0\%, 37.3\%]$); this overlap suggests a shared bound from the lack of ground-truth state access. The oracle matches always-deterministic on 96.3\% of decisions (score improvement: 2.89 points), and even with perfect per-task death risk knowledge, threshold routing cannot outperform always-determi
…[truncated 3702 chars]

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

_source line 1478 · 2026-05-19T13:57:49.613735+00:00_

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

_source line 1479 · 2026-05-19T13:57:50.065352+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	\emph{Self-supervised} approaches learn tool invocation from loss signals: Toolformer \cite{toolformer-2023} inserts API calls filtered by perplexity reduction; ToolACE \cite{toolace-2025} curates synthetic data for function-calling accuracy.
6	\emph{Token-level} methods embed tools into the model vocabulary: ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens resolved at inference.
7	\emph{Task-level} decomposition routes subtasks to specialized modules: ART \cite{art-2023} generates tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask.
8	\emph{RL-based} methods learn routing policies from reward: ReTool \cite{retool-2025} discovers when code execution is preferable to chain-of-thought.
9	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
10	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect where LLMs default to external tools even when internal knowledge suffices, finding that tool overuse correlates with model uncertainty rather than task difficulty. \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax,'' and \citet{to-call-or-not-2026} propose a necessity, utility, and affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, 78.9\% of routing labels trace to catastrophic-failure prevention.
11	
12	\paragraph{Adaptive Computation and Routing.}
13	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-o
…[truncated 2234 chars]

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

_source line 1480 · 2026-05-19T13:57:50.065727+00:00_

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

_source line 1481 · 2026-05-19T13:57:50.116151+00:00_

1	\section{Conclusion}
2	
3	We presented a diagnostic framework for decomposing routing signal in modular LLM agents via episode-level counterfactual analysis. Applied to ScienceWorld (245 episodes, 11 task types), 78.9\% of non-tie routing labels arise from death asymmetry; agent improvement baselines (retry, self-correction, $10{\times}$ scaling, action-space restriction) confirm this is robust. Cross-domain contrasts support framework predictions: MATH shows no routing signal without catastrophic failure; ALFWorld identifies information asymmetry as an alternative mechanism. Future work should target environments with intermediate death regimes, such as NetHack~\citep{nethack-2020} combat tasks and Crafter~\citep{crafter-2022} with tuned difficulty, building on recent LLM agent benchmarks \citep{balrog-2025,netplay-2024}; evaluation with stronger backbones is another direct open direction.
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

_source line 1482 · 2026-05-19T13:57:56.243848+00:00_

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

_source line 1483 · 2026-05-19T13:57:57.046403+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 1484 · 2026-05-19T13:57:57.247560+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_CONFIG_FOUND\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_CONFIG_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1485 · 2026-05-19T13:57:57.298460+00:00_

NO_CONFIG_FOUND

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

_source line 1486 · 2026-05-19T13:58:01.976194+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -name \"config.*\" -not -path \"*/.claude/*\" | head -5",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -name \"config.*\" -not -path \"*/.claude/*\" | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1487 · 2026-05-19T13:58:02.078172+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/’: No such file or directory
---

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

_source line 1488 · 2026-05-19T13:58:05.357914+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.{yaml,yml,json}",
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
    "pattern": "**/config.{yaml,yml,json}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1489 · 2026-05-19T13:58:05.408704+00:00_

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


### Tool call

_source line 1490 · 2026-05-19T13:58:09.474817+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 2 -name \"config.*\" -type f 2>/dev/null | head -10",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 2 -name \"config.*\" -type f 2>/dev/null | head -10",
    "description": "Find config files in workspace root"
  }
}
```

</details>

---


### Tool result

_source line 1491 · 2026-05-19T13:58:09.525559+00:00_

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

_source line 1492 · 2026-05-19T13:58:12.342042+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/",
  "description": "List project root directory"
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
    "description": "List project root directory"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-19T13:58:12.393009+00:00_

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
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1494 · 2026-05-19T13:58:15.673599+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
  "description": "Search for external review config"
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
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1495 · 2026-05-19T13:58:15.724480+00:00_

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

_source line 1496 · 2026-05-19T13:58:31.376680+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.count('\\x0c') + 1\nprint(f'Pages: {pages}')\n\" 2>/dev/null || echo \"Cannot determine page count\"",
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.count('\\x0c') + 1\nprint(f'Pages: {pages}')\n\" 2>/dev/null || echo \"Cannot determine page count\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1497 · 2026-05-19T13:58:31.478288+00:00_

Pages:           21
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_director_19d7e797

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

_source line 1498 · 2026-05-19T13:58:42.926976+00:00_

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

_source line 1499 · 2026-05-19T13:59:10.318043+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 27391
}
```

</details>

---


### Tool call

_source line 1500 · 2026-05-19T13:59:10.519201+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Long paper (ARR)\n- **截止日期**: 2026-05-25\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## Venue 格式要求（实时搜索确认）\n- **页数限制**: 正文严格 8 页，参考文献无限制\n- **Limitations 节**: 必须有，不计入页数，仅限讨论局限性，严禁含新实验/图表/分析\n- **Ethics 节**: 可选，标题须为 \"Ethical considerations\"，不计入页数\n- **匿名规则**: Double-blind（作者不可见，审稿人不可见）\n- **模板**: ACL template，必须使用 [review] 选项\n- **MS Word 模板**: 2026年3月起不接受，使用将被 desk-reject\n- **评分标准 (Overall Assessment)**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 方法论严谨性\n- Episode-level counterfactual framework 的理论基础是否牢固？假设是否合理？\n- DAF 指标的定义和解释是否正确？penalty-independent vs penalty-dependent 双指标设计是否恰当？\n- Algorithm 1 (Episode-Level Counterfactual Labeling) 的设计——death-aware labeling 优先 survival 再比较 score——是否引入 bias？\n- 78.9% label fraction 是否存在 tautological 或 trivial 的成分（考虑 P=100 的 penalty 结构）？\n- 统计推断：episode-level bootstrap (B=10000) 是否合适？cluster bootstrap K=11 的可靠性？Cohen's d=3.02 的解释？\n\n### 2. 实验设计\n- 11/30 task types 的选择标准是否合理？63% 排除率的 scope limitation 是否被充分讨论？\n- Anti-cherry-picking analysis (Table 5) 是否令人信服？n=5 prescreening 的证据力度？\n- Cross-model validation (Llama-3.1-8B): N=220 是否足够？direction consistency 10/10 的说服力？\n- Agent improvement baselines (Retry, Reflexion, 72B, action filtering): 实验设计是否合理？控制变量是否充分？\n- 72B 实验：deterministic strategy 使用什么模型？72B deterministic death rate 是否报告？population 差异 (10 vs 11 tasks) 如何处理？\n- MATH 和 ALFWorld cross-environment probes：模态定义不一致的影响？\n- Router training diagnostic: 作为 diagnostic probe 的定位是否令人信服？0.6B/1.7B/4B 的 non-monotonic pattern？\n- Data scaling ablation: paraphrase augmentation vs real data 的区别？\n\n### 3. 统计分析\n- 所有 confidence intervals 和 p-values 是否正确使用和解释？\n- Per-task correlation r=0.97 被标注为 \"mathematical consequence\"——这是否充分？\n- Seed robustness analysis 的设计？\n- Wild cluster bootstrap 和 per-task CI 的补充证据？\n\n请给出完整的审稿意见，包括：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (使用 EMNLP 2026 评分标准)\n9. **Confidence** (1-5)\n10. **Detailed Comments** (逐节)"
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
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Long paper (ARR)\n- **截止日期**: 2026-05-25\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## Venue 格式要求（实时搜索确认）\n- **页数限制**: 正文严格 8 页，参考文献无限制\n- **Limitations 节**: 必须有，不计入页数，仅限讨论局限性，严禁含新实验/图表/分析\n- **Ethics 节**: 可选，标题须为 \"Ethical considerations\"，不计入页数\n- **匿名规则**: Double-blind（作者不可见，审稿人不可见）\n- **模板**: ACL template，必须使用 [review] 选项\n- **MS Word 模板**: 2026年3月起不接受，使用将被 desk-reject\n- **评分标准 (Overall Assessment)**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 方法论严谨性\n- Episode-level counterfactual framework 的理论基础是否牢固？假设是否合理？\n- DAF 指标的定义和解释是否正确？penalty-independent vs penalty-dependent 双指标设计是否恰当？\n- Algorithm 1 (Episode-Level Counterfactual Labeling) 的设计——death-aware labeling 优先 survival 再比较 score——是否引入 bias？\n- 78.9% label fraction 是否存在 tautological 或 trivial 的成分（考虑 P=100 的 penalty 结构）？\n- 统计推断：episode-level bootstrap (B=10000) 是否合适？cluster bootstrap K=11 的可靠性？Cohen's d=3.02 的解释？\n\n### 2. 实验设计\n- 11/30 task types 的选择标准是否合理？63% 排除率的 scope limitation 是否被充分讨论？\n- Anti-cherry-picking analysis (Table 5) 是否令人信服？n=5 prescreening 的证据力度？\n- Cross-model validation (Llama-3.1-8B): N=220 是否足够？direction consistency 10/10 的说服力？\n- Agent improvement baselines (Retry, Reflexion, 72B, action filtering): 实验设计是否合理？控制变量是否充分？\n- 72B 实验：deterministic strategy 使用什么模型？72B deterministic death rate 是否报告？population 差异 (10 vs 11 tasks) 如何处理？\n- MATH 和 ALFWorld cross-environment probes：模态定义不一致的影响？\n- Router training diagnostic: 作为 diagnostic probe 的定位是否令人信服？0.6B/1.7B/4B 的 non-monotonic pattern？\n- Data scaling ablation: paraphrase augmentation vs real data 的区别？\n\n### 3. 统计分析\n- 所有 confidence intervals 和 p-values 是否正确使用和解释？\n- Per-task correlation r=0.97 被标注为 \"mathematical consequence\"——这是否充分？\n- Seed robustness analysis 的设计？\n- Wild cluster bootstrap 和 per-task CI 的补充证据？\n\n请给出完整的审稿意见，包括：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (使用 EMNLP 2026 评分标准)\n9. **Confidence** (1-5)\n10. **Detailed Comments** (逐节)"
  }
}
```

</details>

---


### Tool call

_source line 1501 · 2026-05-19T13:59:31.751078+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Long paper (ARR)\n- **截止日期**: 2026-05-25\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## Venue 格式要求（实时搜索确认）\n- **页数限制**: 正文严格 8 页，参考文献无限制\n- **Limitations 节**: 必须有，不计入页数，仅限讨论局限性，严禁含新实验/图表/分析\n- **Ethics 节**: 可选，标题须为 \"Ethical considerations\"，不计入页数\n- **匿名规则**: Double-blind（作者不可见，审稿人不可见）\n- **模板**: ACL template，必须使用 [review] 选项\n- **MS Word 模板**: 2026年3月起不接受，使用将被 desk-reject\n- **评分标准 (Overall Assessment)**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性评估\n- 核心发现 \"death dominance drives routing\" 在 ScienceWorld 的 penalty 结构下是否 obvious-in-hindsight / trivial？P=100 的 death penalty 是否使得 death dominance 成为数学必然？\n- DAF 作为 metric 的贡献——是否只是简单的代数分解？78.9% label fraction 是否才是真正的 empirical finding？\n- 框架本身（episode-level counterfactual + DAF + diagnostic procedure）作为方法论贡献的价值如何？\n- \"Death dominance resists standard interventions\" 是否足以支撑 EMNLP Conference 级别的 novelty？\n- 与 concurrent work (when2tool, tool-use-tax, to-call-or-not) 的区分是否充分？\n- Contribution 1-3 的 framing 是否清晰、non-overlapping？特别是 Contribution 2 是否过载？\n\n### 2. 完整性检查\n- 实验覆盖是否完整？是否有明显缺失的 baseline 或 ablation？\n- Related Work 覆盖是否充分？是否有重要的遗漏？特别关注：\n  - LLM agent in permadeath environments (NetHack, Crafter with LLM agents)\n  - Safe RL 文献\n  - Tool use decision-making\n  - 是否存在论文罗列倾向？\n- Cross-environment validation 是否充分支撑 generalization claims？\n- 是否缺少第二个 catastrophic-failure 环境的 replication（如 NetHack）？\n- Limitations 讨论是否诚实完整？\n\n### 3. 写作质量\n- Abstract：~140 词中数字密度如何？是否能 self-contained？\n- Introduction：叙事流畅度？从 problem → gap → solution → contribution 的逻辑链是否清晰？\n- Method：符号和定义是否清晰一致？\n- Experiments：结果呈现是否有效？表格/图表是否信息密集且可读？\n- Discussion：是否深入？是否提供 actionable insights？\n- Related Work：按功能类别组织还是论文罗列？positioning 是否清晰？\n- Conclusion：是否简洁有效？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？\n- Limitations 节是否仅含局限性讨论（无新实验/图表）？\n- 是否使用 ACL template + [review] 选项？\n- 匿名性：是否有匿名泄露？\n- 引用格式：natbib？是否有 orphan entries？\n\n请给出完整的审稿意见，包括：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (使用 EMNLP 2026 评分标准)\n9. **Confidence** (1-5)\n10. **Detailed Comments** (逐节)"
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
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Long paper (ARR)\n- **截止日期**: 2026-05-25\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## Venue 格式要求（实时搜索确认）\n- **页数限制**: 正文严格 8 页，参考文献无限制\n- **Limitations 节**: 必须有，不计入页数，仅限讨论局限性，严禁含新实验/图表/分析\n- **Ethics 节**: 可选，标题须为 \"Ethical considerations\"，不计入页数\n- **匿名规则**: Double-blind（作者不可见，审稿人不可见）\n- **模板**: ACL template，必须使用 [review] 选项\n- **MS Word 模板**: 2026年3月起不接受，使用将被 desk-reject\n- **评分标准 (Overall Assessment)**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性评估\n- 核心发现 \"death dominance drives routing\" 在 ScienceWorld 的 penalty 结构下是否 obvious-in-hindsight / trivial？P=100 的 death penalty 是否使得 death dominance 成为数学必然？\n- DAF 作为 metric 的贡献——是否只是简单的代数分解？78.9% label fraction 是否才是真正的 empirical finding？\n- 框架本身（episode-level counterfactual + DAF + diagnostic procedure）作为方法论贡献的价值如何？\n- \"Death dominance resists standard interventions\" 是否足以支撑 EMNLP Conference 级别的 novelty？\n- 与 concurrent work (when2tool, tool-use-tax, to-call-or-not) 的区分是否充分？\n- Contribution 1-3 的 framing 是否清晰、non-overlapping？特别是 Contribution 2 是否过载？\n\n### 2. 完整性检查\n- 实验覆盖是否完整？是否有明显缺失的 baseline 或 ablation？\n- Related Work 覆盖是否充分？是否有重要的遗漏？特别关注：\n  - LLM agent in permadeath environments (NetHack, Crafter with LLM agents)\n  - Safe RL 文献\n  - Tool use decision-making\n  - 是否存在论文罗列倾向？\n- Cross-environment validation 是否充分支撑 generalization claims？\n- 是否缺少第二个 catastrophic-failure 环境的 replication（如 NetHack）？\n- Limitations 讨论是否诚实完整？\n\n### 3. 写作质量\n- Abstract：~140 词中数字密度如何？是否能 self-contained？\n- Introduction：叙事流畅度？从 problem → gap → solution → contribution 的逻辑链是否清晰？\n- Method：符号和定义是否清晰一致？\n- Experiments：结果呈现是否有效？表格/图表是否信息密集且可读？\n- Discussion：是否深入？是否提供 actionable insights？\n- Related Work：按功能类别组织还是论文罗列？positioning 是否清晰？\n- Conclusion：是否简洁有效？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？\n- Limitations 节是否仅含局限性讨论（无新实验/图表）？\n- 是否使用 ACL template + [review] 选项？\n- 匿名性：是否有匿名泄露？\n- 引用格式：natbib？是否有 orphan entries？\n\n请给出完整的审稿意见，包括：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (使用 EMNLP 2026 评分标准)\n9. **Confidence** (1-5)\n10. **Detailed Comments** (逐节)"
  }
}
```

</details>

---


### Assistant

_source line 1502 · 2026-05-19T14:16:05.600972+00:00_

21 页 PDF（正文 + 参考文献 + Limitations + Ethics + Appendix）。现在并行派发视觉审查和两位 Reviewer。

**审稿编排**：EMNLP 2026 长文，安排 2 位 Reviewer：
- **Reviewer 1**：方法严谨性 + 实验设计
- **Reviewer 2**：新颖性 + 完整性 + 写作质量

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 131

## Round 131

40 recorded events


### User

_source line 1503 · 2026-05-19T14:22:08.752450+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
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

_source line 1504 · 2026-05-19T14:22:14.870757+00:00_

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

_source line 1505 · 2026-05-19T14:22:14.922137+00:00_

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
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1506 · 2026-05-19T14:22:21.052638+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,TodoWrite",
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,TodoWrite",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1507 · 2026-05-19T14:22:21.103573+00:00_



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

_source line 1508 · 2026-05-19T14:22:25.269893+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1509 · 2026-05-19T14:22:25.371356+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1510 · 2026-05-19T14:22:33.301025+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '执行收敛判断'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '执行收敛判断'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1511 · 2026-05-19T14:22:33.301563+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1512 · 2026-05-19T14:22:36.482817+00:00_

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

_source line 1513 · 2026-05-19T14:22:37.838673+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (111 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **minihack-cross-env-pilot** (negative): In MiniHack permadeath navigation environments, episode-level counterfactual analysis will reveal death dominance (internal DR significantly > deterministic DR), validating the diagnostic framework's cross-environment applicability beyond ScienceWorld. This tests whether death avoidance as the dominant routing signal is a general phenomenon of LLM agents in irreversible-failure environments, not an artifact of ScienceWorld's specific task design. ← 基于 plan-012-full\n- **backbone-scaling-70b** (success): 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 ← 基于 backbone-scaling-death-rate-0.5b\n  [72B DAF Decomposition Analysis](/api/workspace-files/projects/simgate-modular-routing/artifacts/backbone-scaling-70b/report/72b_daf_decomposition.md)\n- **llama-cross-model-full** (success): Death dominance mechanism (DAF ~78.9% on Qwen-7B) generalizes across model families: Llama-3.1-8B-Instruct on the same 11 ScienceWorld tasks will show (1) DAF direction consistent with Qwen, (2) similar death-prone vs non-death-prone task pattern, and (3) high per-task death ra
…[truncated 1667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-19T14:22:37.839175+00:00_

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

_source line 1515 · 2026-05-19T14:22:38.793134+00:00_

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
…[truncated 6240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1516 · 2026-05-19T14:22:38.843918+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1517 · 2026-05-19T14:22:39.548222+00:00_

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

_source line 1518 · 2026-05-19T14:22:39.699194+00:00_

-rw-r--r-- 1 ubuntu ubuntu 571639 May 19 14:00 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 1519 · 2026-05-19T14:22:45.120423+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

I found information related to EMNLP 2026, thou
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6276
}
```

</details>

---


### Tool call

_source line 1520 · 2026-05-19T14:22:52.060787+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline May 2026 commitment deadline"
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
    "query": "EMNLP 2026 ARR submission deadline May 2026 commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 1521 · 2026-05-19T14:22:52.663709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
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
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool result

_source line 1522 · 2026-05-19T14:22:56.427658+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline May 2026 commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key deadlines for EMNLP 2026:

## ARR Submission Deadline
The ARR submission deadline is May 25, 2026.

## EMNLP Commitment Deadline
The EMNLP commitment deadline is August 2, 2026.

## Additional Important Dates
- Reviewer registration deadline for all authors: May 27, 2026
- Author response and author-reviewer discussion: July 7-13, 2026
- Meta review released: July 30, 2026
- Notification of acceptance: August 20, 2026
- Camera-ready papers due: September 20, 2026

## Imp
…[truncated 324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 4366
}
```

</details>

---


### Tool result

_source line 1523 · 2026-05-19T14:22:58.837200+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026 regarding page limits and format requirements:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). More specifically:

- **Long Papers**: Review versions of long papers may have up to eight (8) pages of conte
…[truncated 944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6173
}
```

</details>

---


### Tool call

_source line 1524 · 2026-05-19T14:23:13.501811+00:00_

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

_source line 1525 · 2026-05-19T14:23:14.104764+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 126\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinis
…[truncated 1447 chars]

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

_source line 1526 · 2026-05-19T14:23:14.506847+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/project_config.yaml 2>/dev/null | grep -A 10 \"external_review\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/project_config.yaml 2>/dev/null | grep -A 10 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1527 · 2026-05-19T14:23:15.009492+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1528 · 2026-05-19T14:23:15.211236+00:00_

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

_source line 1529 · 2026-05-19T14:23:15.262594+00:00_

## Round 17 Review Issues (updated 2026-05-19 D123 action matrix dispatched)

# =============================================
# Resolved issues from prior rounds (unchanged)
# =============================================

- id: "R13-N1"
  summary: "DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 13
  last_seen_round: 15
  mentions:
    - round: 13
      reviewers: [1, 2]
      note: "Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。"
    - round: 14
      reviewers: [1, 2]
      note: "R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。"
    - round: 15
      reviewers: [1, 2]
      note: "R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。"
    - round: 16
      reviewers: []
      note: "R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。"
  resolution: "78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence"
  resolution_round: 15

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
  resolution: "Limitations 和 Appendix B 已充分量化 27.7% mislabeling fraction"
  resolution_round: 14

- id: "R13-W4"
  sum
…[truncated 19209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-19T14:23:55.154107+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '执行收敛判断'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '执行收敛判断'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1531 · 2026-05-19T14:23:55.204921+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-19T14:24:00.123842+00:00_

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


### Tool call

_source line 1533 · 2026-05-19T14:24:02.483653+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "simgate-modular-routing",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "simgate-modular-routing",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 1534 · 2026-05-19T14:24:15.464739+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 15340
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-19T14:24:15.465142+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 12981
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-19T14:24:16.419645+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (via ARR)\n- **类别**: Long paper (正文 8 页 + 无限参考文献)\n- **匿名规则**: Double-blind\n- **Deadline**: ARR 提交截止 2026-05-25\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **Limitations/Ethics**: 不计入页数限制\n\n## 论文路径\n- LaTeX: `projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心关注**：\n1. **Counterfactual 框架设计**：episode-level labeling 方法论是否 sound？labeling algorithm 有无 circularity/bias？\n2. **统计推断**：bootstrap CI、cluster bootstrap、effect size 的使用是否正确？sample size 是否足以支撑结论？\n3. **实验设计**：task selection (11/30) 是否引入 selection bias？cross-environment (MATH, ALFWorld) 和 cross-model (Llama, 72B) 验证是否充分？\n4. **Router 实验**：router 训练的 diagnostic 解读是否合理？negative results 的解释是否充分？\n5. **Ablation 和 Robustness**：agent improvement baselines (Reflexion, retry, action filter, 72B scaling) 的实验设计是否公平？\n6. **可重复性**：实验细节是否充分、数据规模是否足够\n\n**输出格式**：\n按以下结构输出你的审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n- Questions (需要作者回答的)\n- Missing References (如有)\n- Overall Assessment (评分 1-5，按 EMNLP 2026 ARR 标准)\n- Confidence (1-5)\n\n**审稿标准**：像顶会最严格的审稿人一样评估。不留情面，严正客观。",
  "reviewer_id": "1",
  "project": "simgate-modular-routing",
  "round_number": "1"
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
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (via ARR)\n- **类别**: Long paper (正文 8 页 + 无限参考文献)\n- **匿名规则**: Double-blind\n- **Deadline**: ARR 提交截止 2026-05-25\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **Limitations/Ethics**: 不计入页数限制\n\n## 论文路径\n- LaTeX: `projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心关注**：\n1. **Counterfactual 框架设计**：episode-level labeling 方法论是否 sound？labeling algorithm 有无 circularity/bias？\n2. **统计推断**：bootstrap CI、cluster bootstrap、effect size 的使用是否正确？sample size 是否足以支撑结论？\n3. **实验设计**：task selection (11/30) 是否引入 selection bias？cross-environment (MATH, ALFWorld) 和 cross-model (Llama, 72B) 验证是否充分？\n4. **Router 实验**：router 训练的 diagnostic 解读是否合理？negative results 的解释是否充分？\n5. **Ablation 和 Robustness**：agent improvement baselines (Reflexion, retry, action filter, 72B scaling) 的实验设计是否公平？\n6. **可重复性**：实验细节是否充分、数据规模是否足够\n\n**输出格式**：\n按以下结构输出你的审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n- Questions (需要作者回答的)\n- Missing References (如有)\n- Overall Assessment (评分 1-5，按 EMNLP 2026 ARR 标准)\n- Confidence (1-5)\n\n**审稿标准**：像顶会最严格的审稿人一样评估。不留情面，严正客观。",
    "reviewer_id": "1",
    "project": "simgate-modular-routing",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1537 · 2026-05-19T14:24:25.875680+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9456
}
```

</details>

---


### Tool call

_source line 1538 · 2026-05-19T14:24:26.177212+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (via ARR)\n- **类别**: Long paper (正文 8 页 + 无限参考文献)\n- **匿名规则**: Double-blind\n- **Deadline**: ARR 提交截止 2026-05-25\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **Limitations/Ethics**: 不计入页数限制\n\n## 论文路径\n- LaTeX: `projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心关注**：\n1. **Novelty / Excitement**：核心发现（death avoidance dominates routing signal）是否 trivial / obvious-in-hindsight？论文的知识贡献是什么——是 finding 本身还是 diagnostic framework？\n2. **Framing 合理性**：标题、Abstract、Contributions 的 claim scope 是否与实证支持匹配？是否存在 overclaim？\n3. **Related Work 覆盖**：LLM agent routing、safe RL、tool-augmented LLM、permadeath environments 的引用是否充分？positioning 是否清晰？\n4. **写作质量**：Abstract 是否有数字堆砌？行文是否清晰流畅？Section 结构是否逻辑连贯？\n5. **贡献定位**：Contribution 1/2/3 各自的边界是否清晰？是否有 overloaded contribution？\n6. **格式合规**：页数、匿名、引用格式、Limitations section 是否符合 EMNLP 2026 ARR 要求？\n\n**输出格式**：\n按以下结构输出你的审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n- Questions (需要作者回答的)\n- Missing References (如有)\n- Overall Assessment (评分 1-5，按 EMNLP 2026 ARR 标准)\n- Confidence (1-5)\n- Excitement (1-5)\n\n**审稿标准**：像顶会最严格的审稿人一样评估。不留情面，严正客观。",
  "reviewer_id": "2",
  "project": "simgate-modular-routing",
  "round_number": "1"
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
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (via ARR)\n- **类别**: Long paper (正文 8 页 + 无限参考文献)\n- **匿名规则**: Double-blind\n- **Deadline**: ARR 提交截止 2026-05-25\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **Limitations/Ethics**: 不计入页数限制\n\n## 论文路径\n- LaTeX: `projects/simgate-modular-routing/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心关注**：\n1. **Novelty / Excitement**：核心发现（death avoidance dominates routing signal）是否 trivial / obvious-in-hindsight？论文的知识贡献是什么——是 finding 本身还是 diagnostic framework？\n2. **Framing 合理性**：标题、Abstract、Contributions 的 claim scope 是否与实证支持匹配？是否存在 overclaim？\n3. **Related Work 覆盖**：LLM agent routing、safe RL、tool-augmented LLM、permadeath environments 的引用是否充分？positioning 是否清晰？\n4. **写作质量**：Abstract 是否有数字堆砌？行文是否清晰流畅？Section 结构是否逻辑连贯？\n5. **贡献定位**：Contribution 1/2/3 各自的边界是否清晰？是否有 overloaded contribution？\n6. **格式合规**：页数、匿名、引用格式、Limitations section 是否符合 EMNLP 2026 ARR 要求？\n\n**输出格式**：\n按以下结构输出你的审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n- Questions (需要作者回答的)\n- Missing References (如有)\n- Overall Assessment (评分 1-5，按 EMNLP 2026 ARR 标准)\n- Confidence (1-5)\n- Excitement (1-5)\n\n**审稿标准**：像顶会最严格的审稿人一样评估。不留情面，严正客观。",
    "reviewer_id": "2",
    "project": "simgate-modular-routing",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-19T14:24:27.645342+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1468
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-19T14:24:35.231108+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 返回审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '执行收敛判断'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 返回审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '执行收敛判断'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1541 · 2026-05-19T14:24:35.231510+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1542 · 2026-05-19T14:24:40.037598+00:00_

所有任务已并行派发：
- ✓ 视觉审查 Agent 已启动
- ✓ 外部审稿请求已发送（Stanford Agentic Reviewer，8h 自动提醒）
- ✓ Reviewer 1（方法严谨性 + 实验设计）已分配
- ✓ Reviewer 2（新颖性 + 完整性）已分配

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 132

## Round 132

2 recorded events


### User

_source line 1543 · 2026-05-19T14:30:00.461251+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld

## Summary

本文提出一个 episode 级别的反事实诊断框架，用于分解模块化 LLM agent 中路由信号的来源。核心发现是：在 ScienceWorld 环境中，78.9% 的非平局路由标签源于死亡不对称（内部策略的幻觉导致灾难性 agent 死亡），而非能力差异。作者定义了 Death Avoidance Factor (DAF) 指标，进行了四种干预实验、跨模型复制（Llama-3.1-8B）、以及 MATH/ALFWorld 跨环境边界探测。论文整体方法严谨，但核心发现在 permadeath 环境中近乎 tautological，且单一主环境限制了影响力。

## Strengths

**S1. 框架设计严谨，方法论扎实。** 反事实 episode 收集流程（Algorithm 1）清晰规范；标签体系（det-pref, int-pref, no-pref）定义明确；统计推断采用 cluster-robust bootstrap（Cameron et al., 2008; Webb, 2023）处理 episode 内依赖，并报告 bootstrap 95% CIs。整体方法论水平超过多数 agent 分析论文。

**S2. 定量分解是新颖的贡献。** 将路由分数差分解为 Δ_death 和 Δ_nd（Section 2.4, Eq. 4）是一个此前未见的形式化。Signal Concentration Index (SCI) 作为补充度量也有诊断价值。

**S3. 鲁棒性检验充分。** 跨模型复制（Llama-3.1-8B，Appendix M）、leave-one-task-out 敏感性分析（Appendix G/Table 7）、per-task-type breakdown（Table 3）、labeling quality audit（Appendix B）、wild cluster bootstrap（Table 6）等。附录 A-Q 覆盖面广，远超正文所需。

**S4. Framing 诚实。** 标题明确限定 "on ScienceWorld"，未 overclaim 为通用结论。Limitations section 坦诚讨论了单环境局限、独立性假设、方法论约束等。

**S5. 跨环境边界探测有诊断价值。** MATH（无灾难性失败 → 无路由信号）和 ALFWorld（信息不对称而非死亡回避）的对比展示了框架在检测机制差异上的能力。

**S6. 引用完整性良好。** 46 篇引用全部有对应 bib 条目，无 orphan 或 missing。经 OpenAlex 验证，36 篇 verified，4 篇 not_found（多为较新 preprint），6 篇 mismatch（主要是 LaTeX 编码/年份差异），无 fabricated references。

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 核心发现在 permadeath 环境中近乎 tautological**
- 具体位置：Section 2.4, Section 3.1, Section 5 ("Why the router fails")
- 问题：ScienceWorld 设置中，内部策略（LLM 推理）会因幻觉触发 -100 death penalty，而确定性策略（ground-truth state transition）**by design 不会死亡**。在这种设置下，"死亡回避主导路由信号" 几乎是构造性地 true：一个能死的策略 vs. 一个不能死的策略，偏好后者的原因当然主要是"后者不会死"。论文在 Section 5 承认 "death avoidance is a task-type-level binary property"，penalty sensitivity（Appendix K, Table 12）也表明 DAF 随 P→0 单调递减——这恰好说明这个发现是 reward structure 的数学结果而非关于 routing 的 deep insight。
- 为什么影响接收：如果核心发现可以从环境设计中 trivially 推导，novelty claim 就大幅削弱。读者可能会问："在一个有 permadeath 且一个策略免疫死亡的环境中，death dominance 不是显然的吗？"
- 建议修改方向：(1) 明确区分 "死亡回避主导" 作为 quantitative finding vs. qualitative insight，强调 78.9% 的具体数值和 DAF 指标本身的诊断价值；(2) 增加一个没有 permadeath 但有 partial penalty（如扣分但不终止）的消融，展示在非二元死亡结构下框架是否仍能识别有意义的信号分解；(3) 更坦诚地在 introduction 中 frame 这个 contribution 为 "量化一个直觉上合理但此前未被精确衡量的现象"。

**N2 [critical] 单一主环境严重限制框架的 demonstrated utility**
- 具体位置：Section 3 全部实验、Section 3.4-3.5 跨环境探测
- 问题：核心分析 100% 依赖 ScienceWorld。MATH 和 ALFWorld 的"跨环境探测"过于单薄：MATH 仅确认无路由信号（p=0.81），未产生正面诊断价值；ALFWorld 仅用 6 task types/135 games 得到一个定性结论（信息不对称），缺乏与 ScienceWorld 同等深度的量化分析。框架的价值命题依赖于在多种环境中产生 actionable diagnostics，但目前只在一个环境中 fully demonstrated。
- 为什么影响接收：框架论文如果只在一个环境上 work，说服力大减。特别是 ScienceWorld 的 permadeath 结构使得发现可能不 generalize。
- 建议修改方向：(1) 对 ALFWorld 进行与 ScienceWorld 同等深度的分析（DAF 计算、intervention experiments、per-task breakdown）；(2) 增加至少一个有 intermediate death regime（non-binary failure）的环境，如 NetHack/MiniHack（论文已在 Discussion 中提及）；(3) 如果资源不足，至少在 ALFWorld 上做完整的 DAF 分解并讨论与 ScienceWorld 的机制差异。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] Contribution 2（DAF penalty-dependent）作为独立 contribution 较弱**
- 具体位置：Section 1 Contributions 列表第 2 条，Section 2.4
- 问题：DAF 随 penalty P 单调递增是其定义（Eq. 5, DAF = δP/(δP + Δ_nd)）的数学必然结果，论文自己也在 page 4 承认 "it increases monotonically with P, a mathematical consequence rather than empirical finding"。将自己定义的指标的数学性质列为 contribution 是 overloaded。
- 建议：将 Contribution 2 重新表述为 empirical finding（如 "DAF ≈ 90% across tasks in ScienceWorld, with death dominance robust to four representative interventions"），而非 metric property。

**W2 [warning] 干预实验（Section 3.2-3.3）覆盖面有限且 ad hoc**
- 具体位置：Section 3.2（4 种干预），Section 3.3（agent improvement baselines）
- 问题：四种干预（retry, self-correction/Reflexion, 10× scaling, action-space restriction）未涵盖最直接的死亡对抗策略——如显式死亡状态检测、safe action filtering（在 RL safety 文献中已有成熟方法如 CPO, CRPO 等论文已引用但未实验）、或 LLM 的 chain-of-thought safety prompting。干预选择缺乏系统性 rationale。
- 建议：(1) 增加至少一种直接针对死亡机制的干预（如在 prompt 中显式告知死亡状态列表）；(2) 如果资源有限，至少系统地论证为什么选择这四种干预以及它们如何覆盖不同的失败 mode。

**W3 [warning] Trained router（Section 3.6）的结果 underwhelming 且解读不充分**
- 具体位置：Table 2, Section 3.6
- 问题：Trained Router 的 episode-weighted mean score（-10.70）与 Always-Deterministic（-9.67）接近，death rate 从 16.3%（确定性 baseline）仅降至 17.6%，balanced accuracy 仅 54%（接近 chance）。论文将此解读为"路由信号被死亡主导"的证据，但同样可以解读为 router 架构/训练不足。特别是只用了 Qwen-3.17B 做 router（Section I, Appendix），batch size 选择影响巨大（gradient accumulation 1 vs 8 差异显著），且 4B router 超过 always-deterministic baseline 但论文轻描淡写（"only 4B exceeds the always-deterministic baseline"）。
- 建议：(1) 讨论 router 训练不足的可能性作为 alternative hypothesis；(2) 更详细地报告 4B router 结果并讨论 capacity scaling 的意义。

**W4 [warning] Abstract 数字密度过高，首次阅读理解门槛高**
- 具体位置：Abstract
- 问题：Abstract 包含 78.9%, 245 episodes, 11 task types, Qwen2.5-7B-Instruct, N=795, p=0.81 等大量数字/术语。"non-tie routing labels" 未定义即使用。对未读过正文的读者，这些数字缺乏锚定上下文。
- 建议：(1) 减少 abstract 中的具体数字，保留最关键的 1-2 个（如 78.9% 和 DAF）；(2) 将 "non-tie routing labels" 替换为更直觉的表述（如 "cases where one strategy clearly outperforms the other"）；(3) 将 MATH validation 的细节移至正文。

**W5 [warning] Related Work 中 Safe RL 部分连接薄弱**
- 具体位置：Section 4 最后一段
- 问题：论文引用了 García & Fernández (2015), Tamar et al. (2015), Achiam et al. (2017), CRPO (2021), SafeRoute (2025)，但仅用一句话总结："Our diagnostic shows modality routing already functions as an implicit safety mechanism in environments with catastrophic failure." 这些 safe RL 方法与本文框架的关系未被深入讨论。既然论文发现死亡回避是主导信号，那么 safe RL 的 constrained optimization 方法是否可以直接应用于 router training？这是一个明显的 missing connection。
- 建议：增加 1-2 句讨论 safe RL 方法如何可能作为 router training 的替代范式，特别是 CPO/CRPO 风格的约束优化是否适用于本文的 routing 问题。

## Minor Issues

- **M1**: Figure 2 (page 4) 散点图中的 δ 和 Δ_death 符号在图内文字偏小，建议增大。
- **M2**: Section 2.1 定义了 routing policy π: O* → M，但未明确说明 O* 是什么（observation history?），直到后文才隐含。
- **M3**: Table 1 的 "10-death-prone tasks only" 行与主体 "All 11 tasks" 行的对比较混乱，建议用更清晰的分组。
- **M4**: Appendix E（Wild Cluster Bootstrap）和 Appendix D（Correlation Robustness）的内容可以合并精简。
- **M5**: 论文在 Discussion（Section 5）提到 "NetHack, Crafter, BALROG" 但未在 related work 中讨论 permadeath game environments 作为一个类别。
- **M6**: 引用格式：webb-2023 年份 mismatch（bib 标注 2023，OpenAlex 匹配到 2014 年版本），应核实正确年份。

## Questions for Authors

**Q1**: 如果将 ScienceWorld 的 death penalty 从 -100 降到 -10 或 -1（而非完全移除），DAF 如何变化？Table 12 的 penalty sensitivity 只展示了极端值（P=0 和 P=100 附近），中间区间的行为对理解框架的 sensitivity 更重要。

**Q2**: ALFWorld 的确定性策略优势来自"信息不对称"（admissible action access），这与 ScienceWorld 的死亡回避是两种完全不同的机制。框架是否能 formalize 这种区分（而非仅定性描述）？如果不能，框架的通用性如何保证？

**Q3**: Section 3.6 的 trained router 是否尝试过 death-aware training objective（如给死亡 episode 更高 weight，或用 constrained optimization 显式最小化死亡率）？如果 router 被显式训练为避死，性能是否改善？

**Q4**: Contribution 1 声称框架 "applies to any environment with controllable modality comparison and binary catastrophic outcome"——但 MATH（无灾难性结果）和 ALFWorld（非 binary 机制）的探测结果表明框架在这些环境中提供的洞察有限。如何调和这一矛盾？

## Missing References

1. **FrugalGPT** (Chen et al., 2023): LLM cascading/routing 的开创性工作，直接相关于 router cost-quality tradeoff。
2. **AutoMix** (Madaan et al., 2024): 自适应混合不同规模模型，与 modality routing 有概念重叠。
3. **Think before you speak / Pause tokens** (Goyal et al., 2024): adaptive computation 的另一种形式，与 Section 4 的 "Adaptive Computation and Routing" 部分相关。
4. **SayCan** (Ahn et al., 2022): grounding LLM with affordance functions，直接相关于 agent 中 feasibility-aware routing。
5. 更广泛的 **LLM hallucination/safety in interactive environments** 文献（如 TruthX, FactScore 等），因为论文的核心机制是幻觉导致死亡。

## 格式合规检查

- **页数**：正文 8 页（Sections 1-6），✓ 合规
- **匿名**：标题页显示 "Anonymous ACL submission"，正文无可识别信息，✓ 合规
- **Limitations**：Page 9 有独立 Limitations section，内容实质性，✓ 合规
- **Ethics Statement**：Page 9 有 Ethics Statement，✓ 合规
- **Responsible NLP Checklist**：Pages 20-21 完整填写，✓ 合规
- **引用格式**：整体规范，个别年份需核实（webb-2023），基本合规

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论严谨（counterfactual design, bootstrap CIs, cluster-robust inference），但核心发现在 permadeath 环境中可预见性高，且主要结论依赖单一环境 |
| Excitement | 2.5/5 | 框架本身有新颖性，但 "death avoidance dominates in permadeath" 不令人意外；缺乏 actionable solution；跨环境 utility 未充分展示 |

## 总体评分

**Overall**: 3.0 — Findings（可被 Findings 接收）
**一句话总结**: 方法严谨、框架设计有价值的诊断性工作，但核心发现在 permadeath 环境中的 near-tautological nature 和单环境依赖限制了 novelty 和 impact，更适合 Findings track。

**Confidence**: 4/5 — 熟悉 LLM agent、tool use、routing 和 safe RL 文献，仔细阅读了正文和全部附录。
**Excitement**: 2.5/5 — 框架概念有一定新颖性，但发现本身不够 exciting，对社区的 actionable impact 有限。


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

_source line 1544 · 2026-05-19T14:30:09.821248+00:00_

Reviewer 2 审稿意见已收到。Overall 3.0 (Findings)，Excitement 2.5/5。核心问题集中在 near-tautological nature 和单环境依赖。

等待 Reviewer 1 返回审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 133

## Round 133

2 recorded events


### User

_source line 1545 · 2026-05-19T14:30:24.247670+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0（Findings）**，Soundness 3.5，Excitement 2.5，Confidence 4。

主要问题：
1. **[N1 critical]** 核心发现（death avoidance dominates）在 permadeath + 一个策略免疫死亡的环境中近乎 tautological，novelty 受限
2. **[N2 critical]** 核心分析 100% 依赖 ScienceWorld，MATH/ALFWorld 探测过于单薄，框架的跨环境 utility 未充分展示
3. **[W1-W5]** DAF 作为独立 contribution 偏弱、干预实验 ad hoc、trained router 结果 underwhelming、abstract 数字过密、safe RL 连接薄弱

主要优势：方法论严谨（bootstrap CIs, cluster-robust inference）、框架形式化有新颖性、附录鲁棒性检验充分、framing 诚实。

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

_source line 1546 · 2026-05-19T14:30:34.076361+00:00_

Reviewer 2 审稿意见已收到。核心判定 **3.0（Findings）**，两个 critical issue（tautological nature + 单环境依赖）。

等待 Reviewer 1 返回初审结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 134

## Round 134

20 recorded events


### User

_source line 1547 · 2026-05-19T14:31:51.928465+00:00_

[Reviewer 1 审稿结果]:
现在查看完毕。清理 PDF 图片并提交审稿意见。

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

_source line 1548 · 2026-05-19T14:32:12.668307+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status",
  "max_results": "3"
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
    "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-19T14:32:12.668781+00:00_

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

_source line 1550 · 2026-05-19T14:32:15.382221+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director project overview review status visual check",
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
    "query": "director project overview review status visual check",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-19T14:32:15.432881+00:00_



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

_source line 1552 · 2026-05-19T14:32:21.806403+00:00_

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

_source line 1553 · 2026-05-19T14:32:22.308604+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (111 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **minihack-cross-env-pilot** (negative): In MiniHack permadeath navigation environments, episode-level counterfactual analysis will reveal death dominance (internal DR significantly > deterministic DR), validating the diagnostic framework's cross-environment applicability beyond ScienceWorld. This tests whether death avoidance as the dominant routing signal is a general phenomenon of LLM agents in irreversible-failure environments, not an artifact of ScienceWorld's specific task design. ← 基于 plan-012-full\n- **backbone-scaling-70b** (success): 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 ← 基于 backbone-scaling-death-rate-0.5b\n  [72B DAF Decomposition Analysis](/api/workspace-files/projects/simgate-modular-routing/artifacts/backbone-scaling-70b/report/72b_daf_decomposition.md)\n- **llama-cross-model-full** (success): Death dominance mechanism (DAF ~78.9% on Qwen-7B) generalizes across model families: Llama-3.1-8B-Instruct on the same 11 ScienceWorld tasks will show (1) DAF direction consistent with Qwen, (2) similar death-prone vs non-death-prone task pattern, and (3) high per-task death ra
…[truncated 1667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1554 · 2026-05-19T14:32:22.309175+00:00_

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

_source line 1555 · 2026-05-19T14:32:22.359673+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-19T14:24:04.360606+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_f6bffc7e8351600df8091f08a63cd5a0\", \"skipped_at\": \"2026-05-19T14:24:54.529847+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1556 · 2026-05-19T14:32:22.512195+00:00_

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

_source line 1557 · 2026-05-19T14:32:22.613136+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-19T14:24:03.550387+00:00\", \"completed_at\": \"2026-05-19T14:24:34.663965+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"parse_fallback\", \"message\": \"Agent output not in expected format (len=1). Raw output preserved in audit result file.\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1558 · 2026-05-19T14:32:48.070626+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
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
    "pattern": "**/*review*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1559 · 2026-05-19T14:32:48.071074+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/best/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/report/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1560 · 2026-05-19T14:32:48.121480+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*reviewer*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
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
    "pattern": "**/*reviewer*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-19T14:32:48.172137+00:00_

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


### Tool call

_source line 1562 · 2026-05-19T14:32:51.602100+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
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
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1563 · 2026-05-19T14:32:51.953856+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_16.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_17.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1564 · 2026-05-19T14:32:53.850378+00:00_

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

_source line 1565 · 2026-05-19T14:32:53.851230+00:00_

1	## Round 17 Review Issues (updated 2026-05-19 D123 action matrix dispatched)
2	
3	# =============================================
4	# Resolved issues from prior rounds (unchanged)
5	# =============================================
6	
7	- id: "R13-N1"
8	  summary: "DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现"
9	  category: framing
10	  severity: critical
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 15
14	  mentions:
15	    - round: 13
16	      reviewers: [1, 2]
17	      note: "Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。"
18	    - round: 14
19	      reviewers: [1, 2]
20	      note: "R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。"
21	    - round: 15
22	      reviewers: [1, 2]
23	      note: "R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。"
24	    - round: 16
25	      reviewers: []
26	      note: "R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。"
27	  resolution: "78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence"
28	  resolution_round: 15
29	
30	- id: "R13-N3"
31	  summary: "跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication"
32	  category: experiment
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 13
36	  last_seen_round: 15
37	  resolution: "标题和 Contribution 措辞已恰当限定 scope"
38	  resolution_round: 15
39	
40	- id: "R13-W1"
41	  summary: "正文篇幅严重不足 long paper 要求"
42	  category: format
43	  severity: warning
44	  status: resolved
45	  first_raised_round: 13
46	  last_seen_round: 14
47	  resolution: "正文已扩展至 8 页"
48	  resolution_round: 14
49	
50	- id: "R13-W2"
51	  summary: "Router 训练实验存在多个 confound"
52	  category: experiment
53	  severity: warning
54	  status: resolved
55	  first_raised_round: 13
56	  last_seen_round: 15
57	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
58	  resolution_round: 15
59	
60	- id: "R13-W3"
61	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
62	  category: method
63	  severity: info
64	 
…[truncated 21817 chars]

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


### Assistant

_source line 1566 · 2026-05-19T14:33:26.901713+00:00_

当前状态汇总：

- **外部审稿**：已跳过
- **视觉审查**：已完成（0 critical, 0 warning, 1 info — parse fallback）
- **历史轮次**：已有 17 轮审稿报告存档
- **Open issues**：15 个 in_progress

**Reviewer 1 的返回内容有问题**——仅包含状态信息"现在查看完毕。清理 PDF 图片并提交审稿意见"，没有实际审稿意见。这不是有效的审稿报告。

需要确认：这是 Reviewer 1 的完整输出，还是后续还有实际审稿内容待转发？如果这就是全部内容，我需要重新派发 Reviewer 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 135

## Round 135

62 recorded events


### User

_source line 1567 · 2026-05-19T14:37:18.566300+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
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

_source line 1568 · 2026-05-19T14:37:24.938517+00:00_

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

_source line 1569 · 2026-05-19T14:37:24.939237+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1570 · 2026-05-19T14:37:31.763715+00:00_

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

_source line 1571 · 2026-05-19T14:37:31.764233+00:00_



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

_source line 1572 · 2026-05-19T14:37:35.577856+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
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
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1573 · 2026-05-19T14:37:35.578340+00:00_



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

_source line 1574 · 2026-05-19T14:37:38.797883+00:00_

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

_source line 1575 · 2026-05-19T14:37:38.848544+00:00_

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

_source line 1576 · 2026-05-19T14:37:45.775382+00:00_

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

_source line 1577 · 2026-05-19T14:37:47.181425+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (111 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **minihack-cross-env-pilot** (negative): In MiniHack permadeath navigation environments, episode-level counterfactual analysis will reveal death dominance (internal DR significantly > deterministic DR), validating the diagnostic framework's cross-environment applicability beyond ScienceWorld. This tests whether death avoidance as the dominant routing signal is a general phenomenon of LLM agents in irreversible-failure environments, not an artifact of ScienceWorld's specific task design. ← 基于 plan-012-full\n- **backbone-scaling-70b** (success): 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 ← 基于 backbone-scaling-death-rate-0.5b\n  [72B DAF Decomposition Analysis](/api/workspace-files/projects/simgate-modular-routing/artifacts/backbone-scaling-70b/report/72b_daf_decomposition.md)\n- **llama-cross-model-full** (success): Death dominance mechanism (DAF ~78.9% on Qwen-7B) generalizes across model families: Llama-3.1-8B-Instruct on the same 11 ScienceWorld tasks will show (1) DAF direction consistent with Qwen, (2) similar death-prone vs non-death-prone task pattern, and (3) high per-task death ra
…[truncated 1667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1578 · 2026-05-19T14:37:47.934748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "80"
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
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1579 · 2026-05-19T14:37:48.336823+00:00_

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
…[truncated 4000 chars]

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

_source line 1580 · 2026-05-19T14:37:48.337284+00:00_

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

_source line 1581 · 2026-05-19T14:37:49.241152+00:00_

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

_source line 1582 · 2026-05-19T14:37:49.392789+00:00_

-rw-r--r-- 1 ubuntu ubuntu 571639 May 19 14:00 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf
PDF_EXISTS

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


### Tool result

_source line 1583 · 2026-05-19T14:38:00.178490+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found search results related to EMNLP 2026, though they mostly relate to workshops and tutorials rather than the main confere
…[truncated 3684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 11841
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-19T14:38:06.651649+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers page limit format template double blind anonymity 2026.emnlp.org"
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
    "query": "EMNLP 2026 call for papers page limit format template double blind anonymity 2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1585 · 2026-05-19T14:38:06.953142+00:00_

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


### Tool call

_source line 1586 · 2026-05-19T14:38:07.957210+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
  "description": "Check if review_issues.yaml exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool call

_source line 1587 · 2026-05-19T14:38:08.961527+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex 2>/dev/null",
  "description": "List all tex files in paper directory"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex 2>/dev/null",
    "description": "List all tex files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 1588 · 2026-05-19T14:38:14.832907+00:00_

Web search results for query: "EMNLP 2026 call for papers page limit format template double blind anonymity 2026.emnlp.org"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results from the official EMNLP 2026 call for papers page (2026.emnlp.org), here are the key details you requested:

## Page Limit and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP 2026 uses the official LaTeX template with ACL style files, identical to the one used for ACL, NAACL, and other *ACL conferences.

## Double-Blind Anonymity

Following the ACL and ARR policies, there is no anonymity period requirement. However, when submissions are under review
…[truncated 647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 8181
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-19T14:38:14.883655+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7930
}
```

</details>

---


### Tool result

_source line 1590 · 2026-05-19T14:38:14.934877+00:00_

-rw-r--r-- 1 ubuntu ubuntu  1094 May 19 11:41 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
-rw-r--r-- 1 ubuntu ubuntu   900 May 19 13:15 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu  5648 May 19 14:00 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
-rw-r--r-- 1 ubuntu ubuntu 13147 May 19 14:00 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  6160 May 19 11:54 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
-rw-r--r-- 1 ubuntu ubuntu 49001 May 19 14:00 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
-rw-r--r-- 1 ubuntu ubuntu  7831 May 19 11:17 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
-rw-r--r-- 1 ubuntu ubuntu  4165 May 19 11:46 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  5500 May 18 03:50 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 5973
}
```

</details>

---


### Tool result

_source line 1591 · 2026-05-19T14:38:14.935313+00:00_

-rw-r--r-- 1 ubuntu ubuntu 24289 May 19 11:41 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 6978
}
```

</details>

---


### Tool call

_source line 1592 · 2026-05-19T14:38:19.453885+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission guidelines page limit appendix policy aclrollingreview.org"
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
    "query": "ACL Rolling Review 2026 May cycle submission guidelines page limit appendix policy aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 1593 · 2026-05-19T14:38:19.956355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1594 · 2026-05-19T14:38:20.408621+00:00_

1	## Round 17 Review Issues (updated 2026-05-19 D123 action matrix dispatched)
2	
3	# =============================================
4	# Resolved issues from prior rounds (unchanged)
5	# =============================================
6	
7	- id: "R13-N1"
8	  summary: "DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现"
9	  category: framing
10	  severity: critical
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 15
14	  mentions:
15	    - round: 13
16	      reviewers: [1, 2]
17	      note: "Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。"
18	    - round: 14
19	      reviewers: [1, 2]
20	      note: "R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。"
21	    - round: 15
22	      reviewers: [1, 2]
23	      note: "R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。"
24	    - round: 16
25	      reviewers: []
26	      note: "R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。"
27	  resolution: "78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence"
28	  resolution_round: 15
29	
30	- id: "R13-N3"
31	  summary: "跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication"
32	  category: experiment
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 13
36	  last_seen_round: 15
37	  resolution: "标题和 Contribution 措辞已恰当限定 scope"
38	  resolution_round: 15
39	
40	- id: "R13-W1"
41	  summary: "正文篇幅严重不足 long paper 要求"
42	  category: format
43	  severity: warning
44	  status: resolved
45	  first_raised_round: 13
46	  last_seen_round: 14
47	  resolution: "正文已扩展至 8 页"
48	  resolution_round: 14
49	
50	- id: "R13-W2"
51	  summary: "Router 训练实验存在多个 confound"
52	  category: experiment
53	  severity: warning
54	  status: resolved
55	  first_raised_round: 13
56	  last_seen_round: 15
57	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
58	  resolution_round: 15
59	
60	- id: "R13-W3"
61	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
62	  category: method
63	  severity: info
64	 
…[truncated 973 chars]

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

_source line 1595 · 2026-05-19T14:38:20.710527+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/project_config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/project_config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1596 · 2026-05-19T14:38:20.762002+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1597 · 2026-05-19T14:38:28.701724+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission guidelines page limit appendix policy aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

Based on my search results from aclrollingreview.org, here is information about the ACL Rolling Review submission guidelines:

## Page Limits

The search results mention page limits but don't provide a complete specification for the May 2026 cycle. However, I can share what is available:

Short papers may consist of up to four (4) pages of content, plus unli
…[truncated 1287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 9247
}
```

</details>

---


### Tool call

_source line 1598 · 2026-05-19T14:38:33.068589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
  "offset": "100",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1599 · 2026-05-19T14:38:33.922541+00:00_

100	- id: "R13-m2"
101	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld + MATH N 标注不一致"
102	  category: writing
103	  severity: warning
104	  status: resolved
105	  first_raised_round: 13
106	  last_seen_round: 16
107	  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
108	  resolution_round: 16
109	
110	- id: "R13-m3"
111	  summary: "Reference 格式不统一 + orphan entries"
112	  category: format
113	  severity: info
114	  status: resolved
115	  first_raised_round: 13
116	  last_seen_round: 15
117	  resolution: "Orphan entries 清理完毕，格式统一"
118	  resolution_round: 15
119	
120	- id: "R14-W2"
121	  summary: "Concurrent work 讨论过于压缩"
122	  category: writing
123	  severity: info
124	  status: resolved
125	  first_raised_round: 14
126	  last_seen_round: 15
127	  resolution: "Concurrent work 展开讨论，各有明确 positioning"
128	  resolution_round: 15
129	
130	- id: "R14-W3"
131	  summary: "Selection bias from prescreening 11/30 task types"
132	  category: experiment
133	  severity: warning
134	  status: resolved
135	  first_raised_round: 14
136	  last_seen_round: 15
137	  resolution: "Anti-cherry-picking analysis 到位"
138	  resolution_round: 15
139	
140	- id: "R14-M1"
141	  summary: "Table 2 caption 'Single seed' 需澄清"
142	  category: writing
143	  severity: info
144	  status: resolved
145	  first_raised_round: 14
146	  last_seen_round: 15
147	  resolution: "Caption 已修正"
148	  resolution_round: 15
149	
150	- id: "R14-M2"
151	  summary: "Limitations section 组织松散"
152	  category: writing
153	  severity: info
154	  status: resolved
155	  first_raised_round: 14
156	  last_seen_round: 15
157	  resolution: "三个 paragraph headers 结构清晰"
158	  resolution_round: 15
159	
160	- id: "R14-M3"
161	  summary: "Appendix F minority-class diversity caveat 应在正文提及"
162	  category: writing
163	  severity: info
164	  status: resolved
165	  first_raised_round: 14
166	  last_seen_round: 16
167	  resolution: "§3.7 和 Appendix F 均明确提及 minority-class diversity confound"
168	  resolution_round: 16
169	
170	- id: "R15-N
…[truncated 4579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1600 · 2026-05-19T14:38:34.073612+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"project_config*\" -o -name \"config*\" 2>/dev/null | head -10",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"project_config*\" -o -name \"config*\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1601 · 2026-05-19T14:38:34.124489+00:00_

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

_source line 1602 · 2026-05-19T14:38:37.847955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
  "offset": "299",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
    "offset": "299",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1603 · 2026-05-19T14:38:38.300158+00:00_

299	  resolution: ""
300	  resolution_round: null
301	
302	- id: "R15-N2"
303	  summary: "跨环境模态定义不一致——三个环境的 deterministic 含义不同"
304	  category: experiment
305	  severity: warning
306	  status: in_progress
307	  first_raised_round: 15
308	  last_seen_round: 17
309	  mentions:
310	    - round: 15
311	      reviewers: [1, 2]
312	      note: "R15 consensus."
313	    - round: 16
314	      reviewers: [1, 2]
315	      note: "R16 consensus."
316	    - round: 17
317	      reviewers: [1, 2]
318	      note: "R17: R2-W2 再提 MATH negative control 的 tautological 质疑。R1 rebut: MATH 是有效 boundary probe (p=0.81 是具体实证检验)，但同意模态定义差异应更 prominently 讨论。Director: 同意 R1——MATH 不是 tautological，但 comparability limitation 应在 Table caption + §3.5 明确标注。"
319	  action_items:
320	    - round: 17
321	      action: "Table 2 caption 逐项注明每环境 deterministic 的具体含义 (oracle simulator / code interpreter / admissible actions)"
322	      assigned_to: paper_agent
323	      status: in_progress
324	  resolution: ""
325	  resolution_round: null
326	
327	- id: "R15-W2"
328	  summary: "Oracle margin vs mislabeling 逻辑层级未明确"
329	  category: writing
330	  severity: warning
331	  status: in_progress
332	  first_raised_round: 15
333	  last_seen_round: 16
334	  mentions:
335	    - round: 16
336	      reviewers: [1, 2]
337	      note: "R16 consensus."
338	    - round: 17
339	      reviewers: []
340	      note: "R17 未单独提及此 issue。R1-W4 讨论了 mislabeling 对 78.9% 的影响但 R2 rebut 认为 episode-level metric 不受 step-level mislabeling 影响。可能已充分处理。"
341	  action_items:
342	    - round: 16
343	      action: "§3.7 补充 oracle margin 与 mislabeling 的独立性讨论"
344	      assigned_to: paper_agent
345	      status: in_progress
346	  resolution: ""
347	  resolution_round: null
348	
349	- id: "R15-M1"
350	  summary: "缺少 permadeath 环境 LLM agent 工作引用"
351	  category: writing
352	  severity: info
353	  status: in_progress
354	  first_raised_round: 15
355	  last_seen_round: 17
356	  mentions:
357	    - round: 16
358	      reviewers: [1, 2]
359	      note: "Tool
…[truncated 5473 chars]

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

_source line 1604 · 2026-05-19T14:38:38.551616+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"^- id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
  "description": "List all issue IDs in review_issues.yaml"
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
    "command": "grep -n \"^- id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
    "description": "List all issue IDs in review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1605 · 2026-05-19T14:38:38.602396+00:00_

7:- id: "R13-N1"
30:- id: "R13-N3"
40:- id: "R13-W1"
50:- id: "R13-W2"
60:- id: "R13-W3"
70:- id: "R13-W4"
80:- id: "R13-W6"
90:- id: "R13-W7"
100:- id: "R13-m2"
110:- id: "R13-m3"
120:- id: "R14-W2"
130:- id: "R14-W3"
140:- id: "R14-M1"
150:- id: "R14-M2"
160:- id: "R14-M3"
170:- id: "R15-N1"
180:- id: "R15-N3"
190:- id: "R15-W1"
200:- id: "R15-W3"
214:- id: "R13-N2"
249:- id: "R13-W5"
277:- id: "R14-W1"
302:- id: "R15-N2"
327:- id: "R15-W2"
349:- id: "R15-M1"
371:- id: "R16-N1"
393:- id: "R16-N2"
415:- id: "R16-N3"
437:- id: "R16-W1"
459:- id: "R16-W2"
481:- id: "R16-W3"
503:- id: "R16-W4"
525:- id: "R16-M1"
548:- id: "R17-N1"
567:- id: "R17-N2"
586:- id: "R17-W1"
605:- id: "R17-W2"
624:- id: "R17-W3"
643:- id: "R17-W4"
662:- id: "R17-M1"

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

_source line 1606 · 2026-05-19T14:38:42.065790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
  "offset": "498",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
    "offset": "498",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1607 · 2026-05-19T14:38:42.116831+00:00_

498	      assigned_to: paper_agent
499	      status: in_progress
500	  resolution: ""
501	  resolution_round: null
502	
503	- id: "R16-W4"
504	  summary: "Contribution 2 过载（覆盖 finding + robustness + router diagnostic）"
505	  category: writing
506	  severity: warning
507	  status: in_progress
508	  first_raised_round: 16
509	  last_seen_round: 17
510	  mentions:
511	    - round: 16
512	      reviewers: [1, 2]
513	      note: "R2-W4 首提，R1 同意。"
514	    - round: 17
515	      reviewers: [1, 2]
516	      note: "R17: R2-N3 升为 Must-Fix。R1 rebut: 三个子成分形成因果链，拆分制造冗余，这是 editorial 调整而非 critical flaw。Director 裁决：维持 warning——合理关切但不影响接收决定。建议将 router diagnostic 移入 Contribution 1。"
517	  action_items:
518	    - round: 17
519	      action: "将 router-as-diagnostic-probe 从 Contribution 2 移至 Contribution 1（方法论部分），减轻 C2 负载"
520	      assigned_to: paper_agent
521	      status: in_progress
522	  resolution: ""
523	  resolution_round: null
524	
525	- id: "R16-M1"
526	  summary: "Appendix C task name 不一致 (find-non-living vs find-non-living-thing)"
527	  category: format
528	  severity: info
529	  status: in_progress
530	  first_raised_round: 16
531	  last_seen_round: 16
532	  mentions:
533	    - round: 17
534	      reviewers: []
535	      note: "R17 未单独提及，待确认是否已修复。"
536	  action_items:
537	    - round: 16
538	      action: "统一 task name"
539	      assigned_to: paper_agent
540	      status: in_progress
541	  resolution: ""
542	  resolution_round: null
543	
544	# =============================================
545	# Round 17 New Issues
546	# =============================================
547	
548	- id: "R17-N1"
549	  summary: "78.9% label fraction 在 task level 呈现 binary split (death-prone 100%, death-free 0%)，aggregate 是 task composition artifact"
550	  category: framing
551	  severity: critical
552	  status: in_progress
553	  first_raised_round: 17
554	  last_seen_round: 17
555	  mentions:
556	    - round: 17
557	      reviewers: [1, 2]
558	      note: "R1-N1 首提，R2 强烈同意。LOTO-DAF (Appendix D) 显示移除
…[truncated 4864 chars]

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

_source line 1608 · 2026-05-19T14:39:17.185566+00:00_

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

_source line 1609 · 2026-05-19T14:39:18.089649+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 126\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinis
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

_source line 1610 · 2026-05-19T14:39:18.240740+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10",
  "description": "Find agent config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10",
    "description": "Find agent config files"
  }
}
```

</details>

---


### Tool result

_source line 1611 · 2026-05-19T14:39:18.343359+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1612 · 2026-05-19T14:39:23.129329+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -name \"project_config*\" -o -name \"projects.yaml\" 2>/dev/null | head -5",
  "description": "Find project configuration files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -name \"project_config*\" -o -name \"projects.yaml\" 2>/dev/null | head -5",
    "description": "Find project configuration files"
  }
}
```

</details>

---


### Tool result

_source line 1613 · 2026-05-19T14:39:23.180950+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1614 · 2026-05-19T14:39:26.798891+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 2 -name \"*.yaml\" -not -path \"*/artifacts/*\" -not -path \"*/docs/*\" 2>/dev/null | head -15",
  "description": "Find yaml config files at top level"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 2 -name \"*.yaml\" -not -path \"*/artifacts/*\" -not -path \"*/docs/*\" 2>/dev/null | head -15",
    "description": "Find yaml config files at top level"
  }
}
```

</details>

---


### Tool result

_source line 1615 · 2026-05-19T14:39:26.849631+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/pending_approval_notifications.yaml
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

_source line 1616 · 2026-05-19T14:39:30.011473+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml 2>/dev/null | grep -A 20 \"simgate-modular-routing\" | head -30",
  "description": "Check workspace config for project settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml 2>/dev/null | grep -A 20 \"simgate-modular-routing\" | head -30",
    "description": "Check workspace config for project settings"
  }
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-19T14:39:30.062202+00:00_

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

_source line 1618 · 2026-05-19T14:39:32.773179+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml 2>/dev/null | head -60",
  "description": "Read workspace config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml 2>/dev/null | head -60",
    "description": "Read workspace config"
  }
}
```

</details>

---


### Tool result

_source line 1619 · 2026-05-19T14:39:32.873931+00:00_

projects: {}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-19T14:39:36.398232+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ 2>/dev/null",
  "description": "Search for external review config"
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
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ 2>/dev/null",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1621 · 2026-05-19T14:39:36.499100+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1622 · 2026-05-19T14:40:14.052038+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## Venue 信息\n- 目标：EMNLP 2026（ARR May 2026 cycle）\n- 截止日期：2026-05-25\n- 页数限制：Long paper 正文 8 页 + 无限参考文献\n- 模板：ACL style files（\\usepackage[review]{acl}）\n- 匿名规则：Double-blind\n- Limitations section 必须有，不计入页数\n- Appendix 不计入页数\n\n## 论文路径\n- LaTeX: projects/simgate-modular-routing/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **Counterfactual 方法论**：episode-level labeling 设计是否合理？pure-strategy comparison 的假设和局限是否充分讨论？labeling function 的 soundness。\n2. **统计有效性**：bootstrap CI 的可靠性（特别是 cluster bootstrap K=11）、效应量报告、p 值使用、样本量充分性（per-task n=20）。\n3. **实验设计**：cross-environment（ScienceWorld / MATH / ALFWorld）对比的公平性、跨模型验证（Llama / Qwen / 72B）的完整性、ablation 设计。\n4. **Router 实验**：router training 作为 diagnostic probe 的设计是否合理、confounds 是否充分控制。\n5. **Reproducibility**：实验细节是否足够复现（hyperparameters、seed policy、评估 protocol）。\n6. **Agent improvement baselines**：Reflexion / retry / scaling 实验的设计和解释。\n\n请以 ACL/ARR reviewer 标准输出完整审稿意见，包含：Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Soundness (1-5)、Excitement (1-5)、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）、Confidence (1-5)。"
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
    "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## Venue 信息\n- 目标：EMNLP 2026（ARR May 2026 cycle）\n- 截止日期：2026-05-25\n- 页数限制：Long paper 正文 8 页 + 无限参考文献\n- 模板：ACL style files（\\usepackage[review]{acl}）\n- 匿名规则：Double-blind\n- Limitations section 必须有，不计入页数\n- Appendix 不计入页数\n\n## 论文路径\n- LaTeX: projects/simgate-modular-routing/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **Counterfactual 方法论**：episode-level labeling 设计是否合理？pure-strategy comparison 的假设和局限是否充分讨论？labeling function 的 soundness。\n2. **统计有效性**：bootstrap CI 的可靠性（特别是 cluster bootstrap K=11）、效应量报告、p 值使用、样本量充分性（per-task n=20）。\n3. **实验设计**：cross-environment（ScienceWorld / MATH / ALFWorld）对比的公平性、跨模型验证（Llama / Qwen / 72B）的完整性、ablation 设计。\n4. **Router 实验**：router training 作为 diagnostic probe 的设计是否合理、confounds 是否充分控制。\n5. **Reproducibility**：实验细节是否足够复现（hyperparameters、seed policy、评估 protocol）。\n6. **Agent improvement baselines**：Reflexion / retry / scaling 实验的设计和解释。\n\n请以 ACL/ARR reviewer 标准输出完整审稿意见，包含：Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Soundness (1-5)、Excitement (1-5)、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）、Confidence (1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-19T14:40:26.504344+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12452
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-19T14:40:26.656349+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## Venue 信息\n- 目标：EMNLP 2026（ARR May 2026 cycle）\n- 截止日期：2026-05-25\n- 页数限制：Long paper 正文 8 页 + 无限参考文献\n- 模板：ACL style files（\\usepackage[review]{acl}）\n- 匿名规则：Double-blind\n- Limitations section 必须有，不计入页数\n- Appendix 不计入页数\n\n## 论文路径\n- LaTeX: projects/simgate-modular-routing/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，重点关注：\n\n1. **Novelty / Contribution**：核心发现（death avoidance dominates routing signal）的新颖性如何？是否存在 obvious-in-hindsight / triviality 风险？贡献声明是否与实际证据匹配？框架的方法论贡献 vs 经验发现的平衡。\n2. **Framing / Positioning**：标题、abstract、introduction 的叙事是否准确反映论文实际贡献？是否过度声明？与现有工作的差异化是否清晰？\n3. **Related Work**：相关工作覆盖是否充分？是否有重要遗漏（safe RL、LLM agent failure modes、permadeath environments、tool-augmented agents）？引用是否真实且格式正确？\n4. **Writing Quality**：行文流畅性、逻辑结构、数字/统计量呈现密度、abstract 是否过于数字堆砌、段落间过渡。\n5. **格式合规**：正文是否在 8 页以内？Limitations section 是否存在且充分？匿名性是否完整（无泄露作者身份的线索）？Figure/Table 质量和 caption 完整性。\n6. **完整性**：论文是否自包含？关键内容是否都在正文而非仅在 appendix？参考文献格式一致性。\n\n请以 ACL/ARR reviewer 标准输出完整审稿意见，包含：Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Soundness (1-5)、Excitement (1-5)、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）、Confidence (1-5)。"
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
    "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## Venue 信息\n- 目标：EMNLP 2026（ARR May 2026 cycle）\n- 截止日期：2026-05-25\n- 页数限制：Long paper 正文 8 页 + 无限参考文献\n- 模板：ACL style files（\\usepackage[review]{acl}）\n- 匿名规则：Double-blind\n- Limitations section 必须有，不计入页数\n- Appendix 不计入页数\n\n## 论文路径\n- LaTeX: projects/simgate-modular-routing/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，重点关注：\n\n1. **Novelty / Contribution**：核心发现（death avoidance dominates routing signal）的新颖性如何？是否存在 obvious-in-hindsight / triviality 风险？贡献声明是否与实际证据匹配？框架的方法论贡献 vs 经验发现的平衡。\n2. **Framing / Positioning**：标题、abstract、introduction 的叙事是否准确反映论文实际贡献？是否过度声明？与现有工作的差异化是否清晰？\n3. **Related Work**：相关工作覆盖是否充分？是否有重要遗漏（safe RL、LLM agent failure modes、permadeath environments、tool-augmented agents）？引用是否真实且格式正确？\n4. **Writing Quality**：行文流畅性、逻辑结构、数字/统计量呈现密度、abstract 是否过于数字堆砌、段落间过渡。\n5. **格式合规**：正文是否在 8 页以内？Limitations section 是否存在且充分？匿名性是否完整（无泄露作者身份的线索）？Figure/Table 质量和 caption 完整性。\n6. **完整性**：论文是否自包含？关键内容是否都在正文而非仅在 appendix？参考文献格式一致性。\n\n请以 ACL/ARR reviewer 标准输出完整审稿意见，包含：Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Soundness (1-5)、Excitement (1-5)、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）、Confidence (1-5)。"
  }
}
```

</details>

---


### Tool call

_source line 1625 · 2026-05-19T14:40:27.914748+00:00_

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

_source line 1626 · 2026-05-19T14:40:28.221209+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1564
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-19T14:40:29.884051+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1969
}
```

</details>

---


### Assistant

_source line 1628 · 2026-05-19T14:40:41.582735+00:00_

**Round 1 已派发：**
- ✅ Reviewer 1（方法严谨性 + 实验设计）已启动
- ✅ Reviewer 2（新颖性 + 完整性 + 写作质量）已启动
- ✅ 视觉审查 Agent 已启动

等待两位 Reviewer 返回独立审稿意见。收到后进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 136

## Round 136

4 recorded events


### User

_source line 1629 · 2026-05-19T14:47:06.266248+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性、完整性、写作质量

---

## 总体评分

**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）
**一句话总结**: 方法论设计扎实、统计分析严谨的经验性诊断研究，但核心发现受限于单一主环境、DAF 指标被 penalty 幅度机械放大、且实际可操作性有限，贡献尚不足以支撑主会议接收。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 反事实设计和 bootstrap 统计推断方法论扎实，但 DAF 指标对 P 的单调依赖削弱了其作为独立发现的地位；单环境为主的验证限制了 claim 的普适性 |
| Excitement | 2.5/5 | 发现本身有趣但存在 obvious-in-hindsight 风险；实际可操作建议（"先检查 death asymmetry 再建 router"）较为直白；router 训练实验为 negative result |
| Reproducibility | 4/5 | 模型、环境、超参数均有详细说明（Table 9, Appendix E）；报告了计算成本；但代码/数据未附 |
| Overall Assessment | 3.0 | 扎实的经验分析，适合 Findings；贡献的窄度和新颖性风险使其难以进入主会议 |
| Confidence | 4/5 | 仔细阅读了全文（含全部 17 个 Appendix），熟悉 LLM agent routing 和 safe RL 相关工作 |

---

## Summary

本文提出了一个诊断框架，通过 episode-level 反事实比较来分解模块化 LLM agent 中 routing signal 的组成。在 ScienceWorld 上收集 245 组 paired pure-strategy episodes（internal reasoning vs. deterministic computation），引入 Death Avoidance Factor (DAF) 指标，发现 78.9% 的 non-tie routing labels 来自 death asymmetry——internal strategy 的 hallucination 触发 catastrophic agent death，而 deterministic strategy 存活。论文通过多模型复现（Llama-3.1-8B）、四类干预实验、跨环境边界探测（MATH, ALFWorld）验证了这一发现，并训练了一个 4B router 作为诊断探针，证明该 signal 是 task-type-level 的二值信号而非可学习的 per-step routing pattern。

---

## 主要优势

**S1. 反事实诊断框架设计精巧**。Episode-level paired comparison（Algorithm 1）通过控制随机种子和初始条件，将 routing signal 的诊断从相关性提升到了近因果水平。Death-aware labeling 先比较存活状态再比较 score 的分层设计合理（Section 2.3, Algorithm 1）。

**S2. 统计方法论严谨**。Wild cluster bootstrap（Cameron et al., 2008; Webb, 2023）处理 task-type 内 episode 非独立性；Signal Concentration Index（Appendix A）量化 signal 集中度；leave-one-task-out 验证（Appendix G, Table 7）证明不依赖单一 outlier task。对于 NLP 领域的经验研究，这一水平的统计处理值得肯定。

**S3. 鲁棒性验证全面**。跨模型（Llama-3.1-8B, Section 3.2, Table 15）、跨环境（MATH, ALFWorld, Section 3.4）、四类干预（retry, self-correction, 10× scaling, action-space restriction, Section 3.3, Table 1）、多种 bootstrap 方法（Table 6）、per-seed breakdown（Table 8-10）等，覆盖面远超一般经验研究。

**S4. 78.9% penalty-independent label fraction 是一个干净的经验发现**。这一数字不依赖于 P 的大小（Section 2.4, 定义为 death-asymmetric episodes 占 non-tie episodes 的比例），是论文最有说服力的量化结论。

**S5. Practitioner Decision Framework（Appendix R）实用**。三阶段决策流程（pilot → death dominance check → decision）有明确的阈值和回顾验证（Table 18），提供了可操作的实践指导。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DAF 指标对 death penalty P 的单调依赖使其作为"发现"具有误导性
- 具体位置：Section 2.4, Equation 5; Section 4.1（第 4 页）; Appendix K, Table 12（第 16-17 页）
- 问题：DAF = δP/(δP + Δ_nd) 随 P 单调递增，这是代数恒等式而非经验发现。ScienceWorld 的 P=100 远大于正常 score 范围（0-1），使得即使很小的 death-rate differential δ 也被放大为极高的 DAF。论文在 Section 4.1 和 Appendix K 承认了这一点（"this is a mathematical consequence of the decomposition, not evidence of mechanism robustness"），但 abstract 和 title 仍以 DAF 为中心叙事，造成 framing 与实际证据的张力。
- 为什么影响接收：如果核心 metric 的数值主要由环境参数（penalty 幅度）而非经验现象驱动，那么"90.4% of routing signal is attributable to death avoidance"这一 claim 的可移植性存疑。Reviewer 或读者换一个 P=10 的环境，DAF 会大幅下降，但 death asymmetry 的 *存在性* 并未改变。
- 建议修改方向：**将 78.9% penalty-independent label fraction 提升为主指标**，DAF 降为补充指标。Abstract 和 Introduction 应明确区分"78.9% 的 routing 决策由 death asymmetry 决定"（penalty-independent）和"death avoidance 解释了 90.4% 的 score gap"（P-dependent）。或者，报告 DAF 在多个 P 值下的敏感性曲线（Table 12 已有数据，但被埋在 Appendix K 里）。

**N2** [critical] 核心 claim 的 generalizability 证据不足——单主环境 + 浅层跨环境探测
- 具体位置：Section 3.4（第 6 页）; Section 6 Conclusion; Section 5 Discussion（第 7-8 页）
- 问题：论文的完整分析仅在 ScienceWorld 上完成（245 episodes, 11 task types）。MATH 和 ALFWorld 被定位为"boundary probes"（Section 3.4），分别只用了 795 problems / 135 games，且未做完整的 DAF 分解或干预实验。然而 Discussion（Section 5）和 Conclusion（Section 6）将发现外推到 NetHack、Crafter 等未测试的 permadeath 环境（"recent benchmarks (Paglieri et al., 2025; Jeurissen et al., 2024) provide infrastructure"），这是不当的 claim 外推。
- 为什么影响接收：论文标题未限定于 ScienceWorld，暗示了更广的适用性。但 ScienceWorld 的 -100 penalty 结构、text-based 交互、30-step 上限等特征并不普适。在 penalty 更温和或连续的环境中，death avoidance 可能不再 dominate。
- 建议修改方向：(1) 标题加限定，或在 abstract 明确框定 scope；(2) 至少在一个 permadeath 环境（如 MiniHack/Crafter）做完整 DAF 分解作为第二个完整数据点；(3) Discussion 中对未测试环境的推测应加 explicit caveats。

**N3** [critical] "Routing signal" 的定义从 episode-level 到 step-level 的 gap 未充分讨论
- 具体位置：Section 2（Method 整体）; Section 3.6（Router Training as Diagnostic Probe, 第 6 页）
- 问题：论文将 "routing signal" 定义为 episode-level 的 pure-strategy performance gap。但实际 routing 决策发生在 step level。Section 3.6 的 router 训练实验揭示了这一断层：step-level balanced accuracy 仅 54.1±5.4%（near chance），episode-level 47.1±2.2%。论文将此解读为"signal is task-type-level binary rather than learnable per-step patterns"，但另一种解读是 **episode-level 的 dominance 分析根本不能直接指导 step-level routing 设计**，这是框架的 fundamental limitation 而非仅仅是一个额外发现。
- 为什么影响接收：如果 episode-level 分析无法指导 step-level 决策（而 step-level 才是 routing 的实际粒度），那么框架的诊断价值被大幅削弱。论文的 framing 应更诚实地面对这一局限。
- 建议修改方向：在 Method 或 Discussion 中增加一段明确讨论 episode-level vs. step-level 的 granularity gap，说明 episode-level 分析的适用场景（如决定"是否值得建 router"）和不适用场景（如"如何设计 step-level 路由策略"）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 数字密度过高，可读性受损
- 具体位置：Abstract（第 1 页）
- 问题：Abstract 在约 150 词内塞入了 78.9%、245 episodes、Qwen2.5-7B-Instruct、κ=0.97、r≈0.81 等至少 8 个数字/统计量。对于首次接触论文的读者，难以快速抓住核心信息。
- 建议：保留 78.9%（核心发现）和 DAF（核心指标），其余数字移入 Introduction 或 Method。Abstract 应以 narrative 为主，突出 "what we found and why it matters"。

**W2** [warning] "Non-trivality of death dominance" 论证（Section 5）说服力不足
- 具体位置：Section 5 Discussion, "Non-trivality of death dominance" 段落（第 8 页）
- 问题：论文论证 death dominance 不 trivial 的理由是 "its resistance to intervention was not predictable a priori"（四类干预都无法消除 death dominance）。但 resistance to intervention 更可能说明 hallucination-induced death 是一个 hard problem（这在 LLM agent 文献中已有共识），而非 death dominance 本身是 non-trivial finding。
- 建议：更有效的 non-triviality 论证应从 *prior beliefs* 出发——引用 routing 文献中假设 routing signal 来源多样化的工作，指出本文发现与这些假设的冲突。或者承认 finding 本身可能 obvious-in-hindsight，但强调 quantification 和 diagnostic framework 的方法论价值。

**W3** [warning] Related Work 中 safe RL 覆盖偏薄
- 具体位置：Section 4 Related Work, "Safe RL" 段落（第 7 页底部）
- 问题：Safe RL 仅用一句话带过五篇引用（García & Fernández 2015; Tamar et al. 2015; Achiam et al. 2017; CRPO 2021; SafeRoute 2025）。鉴于论文核心发现关于 catastrophic failure avoidance，与 safe RL 中的 constrained optimization / irreversible action avoidance 文献（如 constrained MDPs、reward shaping for safety）有更深的概念联系。特别缺失：(a) irreversible/catastrophic action 的形式化讨论；(b) reward shaping 作为 death avoidance 的替代机制；(c) safe exploration 文献。
- 建议：扩展 safe RL 段落至 3-5 句，明确论文发现与 safe RL 文献的联系和区别（safe RL 假设可以训练 policy 来避免 unsafe states，而本文发现 LLM agent 的 death avoidance 是 emergent routing signal 而非被显式优化的）。

**W4** [warning] 跨模型复现（Section 3.2）缺少定量对比表格
- 具体位置：Section 3.2（第 5 页）; Appendix M, Table 15（第 17 页）
- 问题：Section 3.2 仅用文字描述 Llama-3.1-8B 的复现结果（"death-rate differential +30.0 pp, DAF = 92.4%"），完整数据在 Appendix M（Table 15）。主文应至少提供 Qwen vs. Llama 的 side-by-side 对比表格，使读者无需翻 appendix 即可判断一致性。
- 建议：在 Section 3.2 增加 2-3 行 inline 对比（如 mini-table 或结构化文字：Qwen DAF=90.4% vs. Llama DAF=92.4%; Qwen δ=+26.6pp vs. Llama δ=+30.0pp）。

**W5** [warning] Figure 2 scatter plot 的回归线解读过度
- 具体位置：Section 2.4, Figure 2（第 4 页）
- 问题：Figure 2 展示 death-rate differential vs. performance gap 的 per-task scatter，报告 r = 0.97 的 near-perfect correlation。但论文同时在 Section 4.1 承认 "The near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding"。既然如此，Figure 2 的回归线和 r 值主要是在展示一个代数关系而非经验发现，这可能误导读者。
- 建议：在 Figure 2 caption 中明确注明 "The high correlation is a structural consequence of the decomposition (Eq. 4) rather than an independent empirical relationship"，或将此图重新定位为 *illustrative* 而非 *evidential*。

---

## 小问题（不影响接收）

- **M1**: webb-2023 引用年份可能有误。OpenAlex 显示该论文（Webb, "Reworking Wild Bootstrap-Based Inference for Clustered Errors"）首次发布于 2014 年（working paper），2023 年可能是期刊正式出版年。建议核实并使用正式出版年份及 venue 信息。
- **M2**: Section 3.1 提到 "54 sole-identified labels"（第 4 页底部），但这一术语未在 Method 中定义，首次出现时应 clarify。
- **M3**: Table 2 caption 说 "1 Single random seed (42) per episode pair"，但 Section 3.5 讨论了 N=3,4,5 的 per-seed 扩展。建议在 Table 2 caption 中注明 robustness checks 在哪些 appendices。
- **M4**: Appendix N（Failure Mode Analysis）的 failure category 分类（A-E）质量高，但仅基于 "manual inspection"。如果篇幅允许，可补充 inter-annotator agreement 或至少说明标注人数。
- **M5**: Page 8 "Anatomy of catastrophic failure" 段落中 "All 105 internal-strategy deaths (100%) are triggered by the same action pattern: focus on [object]" — 如果 100% 都是同一 pattern，这意味着 death avoidance 本质上等价于 "avoid focus on [object]"，进一步支持 signal 是 trivially binary 的解读。建议在此处讨论这一 implication。

---

## Questions for Authors

**Q1**: DAF 在 P=10（接近正常 score 范围）时降至多少？Table 12 似乎未包含 P<50 的数据点。这一信息对评估 DAF 在其他环境中的适用性至关重要。

**Q2**: 如果将 ScienceWorld 的 death penalty 改为 -1（与正常 score 同量级），death asymmetry 是否仍然 dominate routing labels？此时 78.9% label fraction 是否改变？（理论上 Algorithm 1 的 death-aware labeling 是 P-independent 的，但极端低 penalty 下可能改变 episode 的有效排序。）

**Q3**: Section 3.6 的 router 训练实验中，如果仅在 task-type level 训练一个简单的 lookup table（而非 step-level router），balanced accuracy 是多少？这能直接验证 "signal is task-type-level binary" 的 claim。

**Q4**: grow-plant 是唯一 zero-death task 且 DAF=0（Appendix C, Table 3），同时也是唯一被 SCI 分析排除的 outlier。如果 ScienceWorld 有更多 zero-death tasks，整体 DAF 会如何变化？

---

## Missing References

1. **Irreversible action avoidance in RL**: Moldovan & Abbeel (2012) "Safe Exploration in Markov Decision Processes" — 直接讨论 catastrophic/irreversible states 的形式化，与本文 death avoidance 概念高度相关。
2. **LLM agent failure taxonomy**: 近期有多篇工作系统分类 LLM agent 的 failure modes（如 Ruan et al., 2024 "Identifying the Risks of LM Agents with an LM-Emulated Sandbox"），可丰富 Section 5 的 failure analysis 讨论。
3. **Adaptive computation allocation**: Graves (2016) "Adaptive Computation Time for Recurrent Neural Networks" — 作为 adaptive routing 的经典前身，在 Related Work 的 adaptive computation 段落中值得提及。

---

## 引用验证报告

通过 OpenAlex 自动验证 46 条 bib 条目：
- **36 verified**, **6 mismatch**（多为 author encoding 差异，如 García vs garcia, Küttler vs kuttler），**4 not_found**（react-2023, mixture-of-recursions-2025, gajcin2023counterfactual, zhou2024webarena — 这些是 OpenAlex 索引延迟，论文本身可验证）
- **0 orphan**（bib 中无未引用条目），**0 missing**（tex 中无缺 bib 条目）
- **webb-2023 年份疑问**：bib 标注 2023，OpenAlex 匹配到 2014 版本，可能是 working paper vs. 正式出版的差异，建议作者核实。

整体引用质量良好，无伪造引用迹象。

---

## 格式合规检查

| 检查项 | 结果 | 说明 |
|--------|------|------|
| 正文页数 ≤ 8 页 | ✓ | 正文到 Section 6 Conclusion 结束于第 8 页 |
| Limitations section | ✓ | 第 9 页，涵盖 environmental scope、methodological constraints、generalization scope，较为充分 |
| Ethics Statement | ✓ | 第 9 页，涵盖数据公开性、无人类受试者、计算成本 |
| 匿名性 | ✓ | "Anonymous ACL submission"；未发现作者身份泄露 |
| Responsible NLP Checklist | ✓ | 第 20-21 页，逐条回答 |
| 参考文献格式 | ✓ | 46 条，ACL style，无明显格式异常 |
| Figure/Table caption | ✓ | Figure 1-7, Table 1-18 均有 caption；Figure 1 caption 简洁清晰 |

---

**总结**: 这是一篇方法论设计认真、统计分析严谨的经验性诊断研究。78.9% death-asymmetry label fraction 是一个干净的经验发现，diagnostic framework 有方法论价值。但 (1) DAF 指标的 P-dependence 使核心 framing 存在误导风险，(2) 单主环境验证限制了 claim 的 scope，(3) episode-level 到 step-level 的 granularity gap 削弱了框架对实际 routing 设计的指导价值。建议定位为 Findings，修改后可成为该类别的扎实贡献。

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

_source line 1630 · 2026-05-19T14:47:22.501635+00:00_

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

_source line 1631 · 2026-05-19T14:47:22.954732+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (111 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **minihack-cross-env-pilot** (negative): In MiniHack permadeath navigation environments, episode-level counterfactual analysis will reveal death dominance (internal DR significantly > deterministic DR), validating the diagnostic framework's cross-environment applicability beyond ScienceWorld. This tests whether death avoidance as the dominant routing signal is a general phenomenon of LLM agents in irreversible-failure environments, not an artifact of ScienceWorld's specific task design. ← 基于 plan-012-full\n- **backbone-scaling-70b** (success): 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 ← 基于 backbone-scaling-death-rate-0.5b\n  [72B DAF Decomposition Analysis](/api/workspace-files/projects/simgate-modular-routing/artifacts/backbone-scaling-70b/report/72b_daf_decomposition.md)\n- **llama-cross-model-full** (success): Death dominance mechanism (DAF ~78.9% on Qwen-7B) generalizes across model families: Llama-3.1-8B-Instruct on the same 11 ScienceWorld tasks will show (1) DAF direction consistent with Qwen, (2) similar death-prone vs non-death-prone task pattern, and (3) high per-task death ra
…[truncated 1667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 453
}
```

</details>

---


### Assistant

_source line 1632 · 2026-05-19T14:47:35.630604+00:00_

**Reviewer 2 审稿意见已收到。** Overall: 3.0（Findings），Soundness 3.5，Excitement 2.5，Confidence 4。

关键发现：3 个 Must-Fix（DAF 的 P-dependence 误导性、单主环境泛化不足、episode-to-step granularity gap）+ 5 个 Should-Fix。

等待 Reviewer 1 提交后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 137

## Round 137

6 recorded events


### User

_source line 1633 · 2026-05-19T14:47:36.652784+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 方法严谨性 + 实验设计

---

### Summary

本文提出一个 episode-level counterfactual 诊断框架，用于分析模块化 LLM agent 中 routing 决策的驱动因素。框架将 routing signal 分解为 death avoidance（避死）和 non-death 两个分量。在 ScienceWorld 上以 Qwen2.5-7B-Instruct 为 backbone 实验发现：78.9% 的非平局 routing 标签来自 death asymmetry（一种策略导致 agent 死亡而另一种存活），DAF（Death Avoidance Factor）= 90.4%。框架在 MATH（预测 null，已验证）和 ALFWorld（识别信息不对称作为替代机制）上进行了跨环境验证，在 Llama-3.1-8B 上进行了跨模型复制。Agent 改进干预（Reflexion、retry、scaling）效果有限。Router 训练作为 diagnostic probe 显示其主要学到 death avoidance signal。

---

## 总体评分

**Overall Assessment**: 3.5 — Borderline Conference

**一句话总结**: 一个形式化良好的诊断框架，有扎实的多维验证，但核心指标 DAF 在高惩罚下近乎 tautological，统计推断受限于 K=11 clusters，且 actionability 尚未充分展示。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 | 框架形式化清晰，但 DAF 的 penalty-dependence 使核心发现近似结构性结论而非经验发现；cluster bootstrap K=11 统计推断可靠性不足 |
| **Excitement** | 3/5 | 研究问题有价值（routing signal 诊断是实际需求），但发现的 actionability 有限——router 并未因此产生实际改进 |
| **Reproducibility** | 4/5 | 超参数、seed policy、GPU 资源均有报告；Algorithm 1 可直接实现；代码和数据承诺发布但目前不可用 |
| **Confidence** | 4/5 | 仔细阅读全文含 13 页附录，熟悉 agent routing、counterfactual analysis 和 bootstrap 方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DAF 在高惩罚下近乎 tautological，核心发现的 framing 有误导性
- 具体位置：§2.4 Eq.(5), §3.1, §5 第2段
- 问题：DAF = δP/(δP + Δ\_nd)，其中 δP 是 death-rate differential 乘以 penalty P。当 P=100 时，death 贡献在数学上必然压倒性主导，DAF→1 是结构性结论而非经验发现。论文自己承认"DAF increases monotonically with P"（§5）以及"a mathematical consequence of death dominance, not an independent empirical finding"（§3.1），但仍将 DAF=90.4% 作为标题级发现呈现（Abstract, §1, §3.1）。Penalty-independent label fraction（78.9%）是更 informative 的指标，但被置于次要位置。
- 为什么影响接收：一篇以"dominant routing signal"为标题的论文，其核心定量指标（90.4%）在很大程度上是惩罚结构的数学产物，而非对 agent 行为的独立经验发现。这构成了 contribution framing 的根本问题。
- 建议修改方向：(1) 以 penalty-independent 78.9% label fraction 为主要定量发现，DAF 降级为依赖于 P 的辅助指标；(2) 报告 DAF 随 P 的敏感性曲线（论文提到 P sensitivity 在 Appendix K 但正文未呈现关键数值）；(3) 明确区分"在 ScienceWorld 的 P=100 设定下 death 主导 routing signal"（经验发现）与"DAF 在高 P 下数学上趋近 1"（结构性性质）。

**N2** [critical] Cluster bootstrap K=11 统计推断不可靠
- 具体位置：§3.1, Limitations §42, Appendix E
- 问题：论文使用 task type 作为 cluster 进行 cluster bootstrap，但只有 K=11 个 clusters。论文引用的 Cameron et al. (2008) 建议 K≥40 才能获得可靠推断。结果 CI 为 [73.0%, 100%]，极端宽泛。论文补充了 wild cluster bootstrap（K=11, p<0.001, Appendix E）作为缓解，但 wild bootstrap 同样受小 K 影响。Exact permutation（K=11, 2048 perms）的 p=0.002 看似显著，但 2^11=2048 意味着穷举了全部排列，最小可达 p≈0.0005，0.002 并不像表面上那么强。
- 为什么影响接收：论文的统计显著性声明依赖于 cluster-robust 方法，但 K=11 使得这些方法的渐近理论不成立。这不是可以用 supplementary analysis 完全弥补的问题——它是实验设计的固有约束。
- 建议修改方向：(1) 以 non-clustered bootstrap 为主要推断方法，cluster bootstrap 明确标注为 sensitivity check 并承认 K=11 不满足渐近条件；(2) 增加 Appendix F 中 per-task CI 的 Bonferroni/BH 校正（28 个 task 的多重比较）；(3) 正文中直接讨论 K=11 的局限而非仅放在 Limitations。

**N3** [critical] 27.7% episode-level mislabeling rate 削弱框架实用性
- 具体位置：Limitations §38–39（"The mislabeling fraction...is approximately 27.7%"）
- 问题：超过四分之一的 episode-level 标签与 step-level oracle 标签不一致，且集中在 death-asymmetry episodes——恰恰是论文最依赖的那部分标签。这意味着框架为约 27.7% 的 episodes 给出了"错误"的 step-level routing guidance。论文将此归因于"early steps may have favored the eventually-dying strategy"，但这恰恰说明 episode-level labeling 可能系统性地误导 step-level routing。
- 为什么影响接收：框架的核心贡献是 episode-level counterfactual labeling。如果 27.7% 的标签在 step-level 上是错误的，框架对实际 routing 的指导价值大打折扣。
- 建议修改方向：(1) 分析 mislabeling 对 router 训练质量的影响（e.g., 用 step-level oracle labels 训练 router 对比 episode-level labels）；(2) 量化 mislabeled episodes 的分布——是集中在特定 task types 还是均匀分布？(3) 讨论是否可以通过 step-level 信息修正 episode-level 标签。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 信号集中度高，11/30 task types 的选择削弱 universality 声明
- 具体位置：Table 3 (p.12), Appendix A (SCI=0.21), Limitations §35–36
- 问题：SCI=0.21 表示 top 3 tasks 贡献了 29.8% 的 death-rate differential。论文仅使用 30 个 task types 中的 11 个（63% 被排除），排除原因是"both strategies typically time out within 30 steps"。但论文声称"death avoidance is a task-type-level binary property"（§5）——这一 universality claim 建立在 11 个 tasks 上，其中信号集中在 3 个。Footnote 5（p.12）提到被排除 tasks 的 ΔDR=+38.2pp（高于 included tasks 的 +28.7pp），说明排除并非因为这些 tasks 无 death dominance，而是因为 agent 能力不足（两种策略都超时）。
- 建议：(1) 在正文讨论 signal concentration 的含义；(2) 增加 step budget 的 sensitivity analysis（e.g., 50 步而非 30 步时，被排除 tasks 是否产生有效信号？）。

**W2** [warning] Cross-environment validation 深度不足
- 具体位置：§3.4, §5
- 问题：MATH 仅作为 null check（无 catastrophic failure → 无 routing signal，p=0.81 确认）。ALFWorld 识别了"information asymmetry"作为替代机制，但分析非常简略（§3.4 仅几句话，无定量分解）。两个环境都未提供正面验证——即在新环境中用框架识别出可操作的 routing signal 并据此改进 agent。
- 建议：(1) 对 ALFWorld 做完整的 DAF 分解（目前只有 Figure 4 的标签分布图，缺定量 DAF）；(2) 讨论框架在非 binary death/alive 环境中的适用性。

**W3** [warning] Router 实验设计的 confounds
- 具体位置：§3.6, Appendix I–J
- 问题：(a) Router 的 step-level（68%）vs episode-level（47.1%）performance gap 被归因于 death avoidance signal 是 per-episode binary property。但 multi-step routing 中 compounding errors 同样可以解释此 gap——step-level 小误差在 10–30 步 episodes 中累积导致 episode-level 失败。(b) End-to-end deployment 中 4B router 得分 −12.03（95% CI [−17.82, −6.45]），未超过 always-deterministic（−9.47）。论文将此解读为"routing signal 主要是 death avoidance"，但也可能只是 245 episodes 训练数据不足或 LoRA 架构容量有限。(c) Router generalization test（Appendix J）中 step-level generalization gap（step=54.1±5.4% vs episode=47.1±2.2%）是否可能来自 same-episode leakage（同 episode 的 steps 出现在 train 和 validation 中）？
- 建议：(1) 增加 compounding error 的 ablation（e.g., 在 oracle routing 上加不同比例的随机噪声，观察 episode-level 退化曲线）；(2) 明确 train/val split 是否是 episode-level 的（避免 leakage）。

**W4** [warning] Agent improvement 实验统计功效不足
- 具体位置：§3.3, Table 1, Figure 3
- 问题：(a) Reflexion 实验仅在 10 个 death-prone tasks 上做 N=5 trials，总数据量 50 个 data points，统计功效有限。(b) Retry 的 n=200 vs Reflexion 的 N=5 存在 compute budget 不对等——Reflexion 获得 5× 更多尝试，但论文直接比较二者效果。(c) 72B scaling 也仅在 10 death-prone tasks 上做（Table 1），sample size 极小。(d) Figure 3 的 error bars（Wilson 95% CIs）重叠严重，大部分差异不 significant。
- 建议：(1) 报告 Reflexion vs baseline 的 paired test（McNemar 或 paired bootstrap）而非仅比较 aggregate rates；(2) 增大 per-task sample size 或明确报告 minimum detectable effect size。

**W5** [warning] Router 的 practical value 未建立
- 具体位置：§3.5, §3.6, Table 2
- 问题：Trained router（−10.70）未显著优于 always-deterministic（−9.47），oracle router 仅达 −6.56（Table 2）。论文称 oracle 的改进主要来自 4 个 internal-preferred tasks。这意味着即使有 perfect routing signal，改进空间也很小（仅 ~3 分）。框架诊断出"death avoidance 是主导信号"，但这一诊断并未转化为实际 routing 改进。
- 建议：讨论诊断框架的 practical downstream value——如果发现的 signal 不足以改进 router，框架的价值定位是什么？是纯粹的 scientific understanding 还是有 engineering implications？

---

## 小问题（不影响接收）

- **术语**: 论文用"modality"指代 internal reasoning vs deterministic computation（§2.1）。在 NLP 中"modality"通常指 text/vision/audio，建议用"computation mode"或"strategy"以避免歧义。
- **Figure 2** (p.4): 11 点的 scatter plot 显示 near-perfect correlation (r=0.97)，但考虑到 DAF 的数学结构，这是预期结果而非独立验证。正文应注明这一点。
- **引用年份**: Webb (2023) 的 bib 年份为 2023，但 OpenAlex 匹配到 2014 年版本（Canadian Journal of Economics）。请核实是否有 2023 年修订版。
- **Appendix 结构**: 13 页附录（A–R + Responsible NLP Checklist）内容极其丰富，但缺少索引——读者难以快速定位。建议在附录开头添加 Table of Contents。
- **Algorithm 1** (p.12): 当 both strategies survive 且 scores 相等时标注 `no-pref`（Line 16）。但若两种策略的 trajectory 质量有差异（e.g., 步数不同），相同分数可能掩盖有意义的偏好。

---

## Questions to Authors

1. **DAF sensitivity**: 当 P 从 100 降到 10、1 时，DAF 和 label fraction 如何变化？论文提到 Appendix K 有 penalty sensitivity，但正文未报告关键数值。请提供 DAF vs P 的曲线。

2. **Step-level mislabeling**: 27.7% 的 mislabeled episodes 中，有多少比例的 steps 实际上被错误标注？如果一个 30-step episode 被 episode-level 标为 det-preferred，但前 25 步 step-level oracle 认为 int-preferred，那 router 训练中 25/30 = 83% 的 step-level labels 就是错误的。

3. **Excluded tasks**: 如果将 step budget 从 30 增加到 50 或 100，被排除的 19 个 task types 是否会产生有效 routing signal？这将直接影响 universality claim。

4. **Router train/val split**: §3.6 和 Appendix J 是否使用 episode-level split？即同一 episode 的 steps 是否可能同时出现在 train 和 val 中？

5. **Compounding error**: 如果在 oracle step-level routing 上随机翻转 x% 的决策，episode-level performance 如何退化？这能区分"router 学到了 death avoidance binary signal"和"step-level errors 在 multi-step execution 中累积"两种解释。

---

## Missing References

- 论文的 safe RL 讨论（§4）仅引用经典工作（Garcia & Fernandez 2015, CPO, CRPO, CVaR）。建议补充近期 LLM agent 安全性工作，特别是关于 catastrophic action prevention 的文献。
- 引用验证结果：46 条引用，36 条 verified，4 条 OpenAlex 未找到（react-2023, mixture-of-recursions-2025, gajcin2023counterfactual, zhou2024webarena——均为真实论文，仅 OpenAlex 索引问题），6 条轻微 mismatch（author encoding / year discrepancy）。无虚假引用。

---

## 主要优势

1. **形式化贡献扎实**：Counterfactual labeling function（Algorithm 1）、DAF 分解（Eq. 4–5）、SCI（Appendix A）定义清晰，framework 可直接复用于其他环境。
2. **多维度验证体系**：Cross-model（Llama 3.1-8B, 10/10 directional consistency）、cross-environment（MATH null check, ALFWorld qualitative）、robustness checks（cluster bootstrap, wild bootstrap, per-task CIs, labeling quality audit）构成了比大多数 agent 论文更严谨的验证。
3. **诚实的 Limitations**：论文主动报告 DAF 的 penalty-dependence、K=11 cluster bootstrap 的局限、27.7% mislabeling rate，这种自我批判在 agent 论文中不常见。
4. **实用框架**：Practitioner decision framework（Appendix R）将诊断结果翻译为 3-stage 流程，具有实际指导价值。
5. **完整的 Responsible NLP Checklist**：Pages 20–21 详尽回答了所有 checklist 问题，包括 AI assistant 使用声明。

---

## 格式检查

- ✅ 正文 8 页（含 Limitations + Ethics Statement）
- ✅ `\usepackage[review]{acl}` double-blind 格式
- ✅ Author 列为 "Anonymous"
- ✅ Limitations section 存在且详尽
- ✅ Ethics Statement 存在
- ✅ Responsible NLP Checklist 完整
- ✅ 引用格式一致（ACL natbib）

---

**Overall Assessment: 3.5 (Borderline Conference)**
**Soundness: 3/5**
**Excitement: 3/5**  
**Reproducibility: 4/5**
**Confidence: 4/5**

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0（Findings）**。

三个 Must-Fix 问题：
1. **DAF 指标的 P-dependence** — DAF = δP/(δP+Δ_nd) 随 death penalty P 单调递增，ScienceWorld 的 P=100 机械放大了数值。建议以 78.9% penalty-independent label fraction 为主指标。
2. **单主环境 generalizability 不足** — 完整分析仅在 ScienceWorld 完成，MATH/ALFWorld 只是浅层 boundary probes，但 Discussion 和 Conclusion 外推到未测试的 permadeath 环境。
3. **Episode-level 到 step-level 的 granularity gap** — 论文定义的 routing signal 是 episode-level 的，但实际 routing 发生在 step level。Section 3.6 的 router 训练（~54% balanced accuracy ≈ chance）暴露了这一断层，框架的实际指导价值被削弱。

优势方面：反事实设计精巧、统计方法论（wild cluster bootstrap、SCI）严谨、robustness 验证全面（17 个 Appendix）。78.9% label fraction 本身是一个干净的经验发现。

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：评分 **Overall 3.5（Borderline Conference）**，Soundness 3/5，Excitement 3/5。

三个 Must-Fix 问题：
1. **DAF 在高惩罚下近乎 tautological**——核心指标 90.4% 是 P=100 惩罚结构的数学产物，非独立经验发现，framing 有误导性
2. **Cluster bootstrap K=11 推断不可靠**——远低于 Cameron et al. (2008) 建议的 K≥40，CI [73%, 100%] 极端宽泛
3. **27.7% episode-level mislabeling rate**——超过四分之一的标签在 step-level 上不一致，削弱框架实用性

主要优势在于形式化贡献清晰（Algorithm 1、DAF 分解）、多维度验证体系完整、以及论文对自身局限的诚实讨论。

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

_source line 1634 · 2026-05-19T14:48:18.688250+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** — 同意该观点，并说明理由\n- **[REBUT]** — 反驳该观点，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**Overall Assessment**: 3.0 — Findings\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 指标对 death penalty P 的单调依赖使其作为\"发现\"具有误导性\n- DAF = δP/(δP + Δ_nd) 随 P 单调递增，ScienceWorld 的 P=100 远大于正常 score 范围（0-1），使得即使很小的 death-rate differential δ 也被放大为极高的 DAF。论文在 Section 4.1 和 Appendix K 承认了这一点，但 abstract 和 title 仍以 DAF 为中心叙事。\n- 建议：将 78.9% penalty-independent label fraction 提升为主指标，DAF 降为补充指标。\n\n**N2** [critical] 核心 claim 的 generalizability 证据不足——单主环境 + 浅层跨环境探测\n- 完整分析仅在 ScienceWorld 上完成（245 episodes, 11 task types）。MATH 和 ALFWorld 被定位为\"boundary probes\"，分析简略。但 Discussion 和 Conclusion 将发现外推到 NetHack、Crafter 等未测试环境。\n- 建议：标题加限定，或在至少一个 permadeath 环境做完整 DAF 分解。\n\n**N3** [critical] \"Routing signal\" 的定义从 episode-level 到 step-level 的 gap 未充分讨论\n- 论文将 routing signal 定义为 episode-level pure-strategy performance gap，但实际 routing 发生在 step level。Router 训练实验（step-level balanced accuracy 仅 54.1±5.4%）暴露了这一断层。框架的 framing 应更诚实地面对这一局限。\n- 建议：在 Method 或 Discussion 中明确讨论 episode-level vs step-level 的 granularity gap。\n\n### Should-Fix 问题\n\n**W1** [warning] Abstract 数字密度过高（~150 词中 8+ 数字）\n- 建议：保留 78.9% 和 DAF，其余数字移入 Introduction。\n\n**W2** [warning] \"Non-triviality of death dominance\" 论证（Section 5）说服力不足\n- resistance to intervention 更可能说明 hallucination-induced death 是 hard problem（LLM agent 文献已有共识），而非 death dominance 本身 non-trivial。\n- 建议：从 prior beliefs 出发论证，或承认 finding 可能 obvious-in-hindsight 但强调方法论价值。\n\n**W3** [warning] Related Work 中 safe RL 覆盖偏薄\n- 缺失：irreversible action avoidance 形式化、reward shaping for safety、safe exploration。\n- 建议引用：Moldovan & Abbeel (2012)。\n\n**W4** [warning] 跨模型复现（Section 3.2）缺少定量对比表格\n- 完整数据在 Appendix M Table 15，主文仅文字描述。\n\n**W5** [warning] Figure 2 scatter plot 的回归线解读过度\n- 正文承认 r=0.97 是数学结果，但 Figure 2 呈现方式可能误导读者。\n- 建议 caption 注明结构性关系。\n\n### Missing References\n1. Moldovan & Abbeel (2012) — Safe Exploration in MDPs\n2. Ruan et al. (2024) — LLM agent failure taxonomy\n3. Graves (2016) — Adaptive Computation Time\n\n### Questions\nQ1: DAF 在 P=10 时降至多少？\nQ2: Death penalty 改为 -1 时 78.9% 是否改变？\nQ3: Task-type level lookup table 的 balanced accuracy？\nQ4: 更多 zero-death tasks 时整体 DAF 变化？\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** — 同意该观点，并说明理由\n- **[REBUT]** — 反驳该观点，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**Overall Assessment**: 3.0 — Findings\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 指标对 death penalty P 的单调依赖使其作为\"发现\"具有误导性\n- DAF = δP/(δP + Δ_nd) 随 P 单调递增，ScienceWorld 的 P=100 远大于正常 score 范围（0-1），使得即使很小的 death-rate differential δ 也被放大为极高的 DAF。论文在 Section 4.1 和 Appendix K 承认了这一点，但 abstract 和 title 仍以 DAF 为中心叙事。\n- 建议：将 78.9% penalty-independent label fraction 提升为主指标，DAF 降为补充指标。\n\n**N2** [critical] 核心 claim 的 generalizability 证据不足——单主环境 + 浅层跨环境探测\n- 完整分析仅在 ScienceWorld 上完成（245 episodes, 11 task types）。MATH 和 ALFWorld 被定位为\"boundary probes\"，分析简略。但 Discussion 和 Conclusion 将发现外推到 NetHack、Crafter 等未测试环境。\n- 建议：标题加限定，或在至少一个 permadeath 环境做完整 DAF 分解。\n\n**N3** [critical] \"Routing signal\" 的定义从 episode-level 到 step-level 的 gap 未充分讨论\n- 论文将 routing signal 定义为 episode-level pure-strategy performance gap，但实际 routing 发生在 step level。Router 训练实验（step-level balanced accuracy 仅 54.1±5.4%）暴露了这一断层。框架的 framing 应更诚实地面对这一局限。\n- 建议：在 Method 或 Discussion 中明确讨论 episode-level vs step-level 的 granularity gap。\n\n### Should-Fix 问题\n\n**W1** [warning] Abstract 数字密度过高（~150 词中 8+ 数字）\n- 建议：保留 78.9% 和 DAF，其余数字移入 Introduction。\n\n**W2** [warning] \"Non-triviality of death dominance\" 论证（Section 5）说服力不足\n- resistance to intervention 更可能说明 hallucination-induced death 是 hard problem（LLM agent 文献已有共识），而非 death dominance 本身 non-trivial。\n- 建议：从 prior beliefs 出发论证，或承认 finding 可能 obvious-in-hindsight 但强调方法论价值。\n\n**W3** [warning] Related Work 中 safe RL 覆盖偏薄\n- 缺失：irreversible action avoidance 形式化、reward shaping for safety、safe exploration。\n- 建议引用：Moldovan & Abbeel (2012)。\n\n**W4** [warning] 跨模型复现（Section 3.2）缺少定量对比表格\n- 完整数据在 Appendix M Table 15，主文仅文字描述。\n\n**W5** [warning] Figure 2 scatter plot 的回归线解读过度\n- 正文承认 r=0.97 是数学结果，但 Figure 2 呈现方式可能误导读者。\n- 建议 caption 注明结构性关系。\n\n### Missing References\n1. Moldovan & Abbeel (2012) — Safe Exploration in MDPs\n2. Ruan et al. (2024) — LLM agent failure taxonomy\n3. Graves (2016) — Adaptive Computation Time\n\n### Questions\nQ1: DAF 在 P=10 时降至多少？\nQ2: Death penalty 改为 -1 时 78.9% 是否改变？\nQ3: Task-type level lookup table 的 balanced accuracy？\nQ4: 更多 zero-death tasks 时整体 DAF 变化？\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-19T14:48:45.292155+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26603
}
```

</details>

---


### Tool call

_source line 1636 · 2026-05-19T14:48:45.494032+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** — 同意该观点，并说明理由\n- **[REBUT]** — 反驳该观点，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n\n**Overall Assessment**: 3.5 — Borderline Conference\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 在高惩罚下近乎 tautological，核心发现的 framing 有误导性\n- DAF = δP/(δP + Δ_nd)，当 P=100 时 death 贡献在数学上必然压倒性主导，DAF→1 是结构性结论而非经验发现。论文自己承认这一点但仍将 DAF=90.4% 作为标题级发现。Penalty-independent label fraction（78.9%）是更 informative 的指标。\n- 建议：以 78.9% label fraction 为主要定量发现；报告 DAF vs P 的敏感性曲线；明确区分经验发现与结构性性质。\n\n**N2** [critical] Cluster bootstrap K=11 统计推断不可靠\n- K=11 远低于 Cameron et al. (2008) 建议的 K≥40。CI [73.0%, 100%] 极端宽泛。Wild cluster bootstrap 同样受小 K 影响。Exact permutation 的 p=0.002 在 2^11=2048 穷举下并不如表面强。\n- 建议：以 non-clustered bootstrap 为主要推断；cluster bootstrap 标注为 sensitivity check；增加 per-task CI 的多重比较校正。\n\n**N3** [critical] 27.7% episode-level mislabeling rate 削弱框架实用性\n- 超过四分之一的标签在 step-level 上不一致，集中在 death-asymmetry episodes。框架为约 27.7% 的 episodes 给出了\"错误\"的 step-level routing guidance。\n- 建议：分析 mislabeling 对 router 训练的影响；量化 mislabeled episodes 分布；讨论 step-level 信息修正可能性。\n\n### Should-Fix 问题\n\n**W1** [warning] 信号集中度高，11/30 task types 的选择削弱 universality 声明\n- SCI=0.21，top 3 tasks 贡献 29.8%。63% tasks 被排除。被排除 tasks 的 ΔDR=+38.2pp > included 的 +28.7pp，排除并非因为无 death dominance。\n- 建议：讨论 signal concentration 含义；增加 step budget sensitivity analysis。\n\n**W2** [warning] Cross-environment validation 深度不足\n- MATH 仅作 null check，ALFWorld 分析简略。两个环境都未提供正面验证（在新环境中用框架改进 agent）。\n- 建议：对 ALFWorld 做完整 DAF 分解。\n\n**W3** [warning] Router 实验设计的 confounds\n- (a) Step-level vs episode-level gap 可能来自 compounding errors 而非 binary signal；(b) 245 episodes 训练数据可能不足或 LoRA 容量有限；(c) train/val split 是否 episode-level（避免 leakage）？\n- 建议：增加 compounding error ablation；明确 split 方式。\n\n**W4** [warning] Agent improvement 实验统计功效不足\n- Reflexion N=5 trials × 10 tasks = 50 data points；retry n=200 与 Reflexion N=5 compute budget 不对等；72B 也仅 10 tasks；Figure 3 error bars 重叠严重。\n- 建议：paired test + 增大 sample size 或报告 minimum detectable effect size。\n\n**W5** [warning] Router 的 practical value 未建立\n- Trained router（−10.70）未显著优于 always-deterministic（−9.47），oracle 仅 −6.56。即使 perfect routing，改进空间也很小（~3 分）。框架诊断并未转化为实际 routing 改进。\n- 建议：讨论框架的 practical downstream value。\n\n### 小问题\n- \"modality\" 术语歧义（NLP 中通常指 text/vision/audio）\n- Figure 2 的 r=0.97 是预期结果非独立验证\n- Webb (2023) 引用年份疑问\n- Appendix 缺索引\n- Algorithm 1 平分时标注 no-pref 可能掩盖有意义的偏好\n\n### Questions\n1. DAF vs P 曲线（P=100→10→1）？\n2. 27.7% mislabeled episodes 中各 step 实际错误比例？\n3. Step budget 增加到 50/100 时被排除 tasks 是否产生有效信号？\n4. Router train/val 是否 episode-level split？\n5. Oracle routing 上随机翻转 x% 决策的 episode-level 退化曲线？\n\n### Missing References\n- 近期 LLM agent 安全性工作（catastrophic action prevention）\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** — 同意该观点，并说明理由\n- **[REBUT]** — 反驳该观点，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n\n**Overall Assessment**: 3.5 — Borderline Conference\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 在高惩罚下近乎 tautological，核心发现的 framing 有误导性\n- DAF = δP/(δP + Δ_nd)，当 P=100 时 death 贡献在数学上必然压倒性主导，DAF→1 是结构性结论而非经验发现。论文自己承认这一点但仍将 DAF=90.4% 作为标题级发现。Penalty-independent label fraction（78.9%）是更 informative 的指标。\n- 建议：以 78.9% label fraction 为主要定量发现；报告 DAF vs P 的敏感性曲线；明确区分经验发现与结构性性质。\n\n**N2** [critical] Cluster bootstrap K=11 统计推断不可靠\n- K=11 远低于 Cameron et al. (2008) 建议的 K≥40。CI [73.0%, 100%] 极端宽泛。Wild cluster bootstrap 同样受小 K 影响。Exact permutation 的 p=0.002 在 2^11=2048 穷举下并不如表面强。\n- 建议：以 non-clustered bootstrap 为主要推断；cluster bootstrap 标注为 sensitivity check；增加 per-task CI 的多重比较校正。\n\n**N3** [critical] 27.7% episode-level mislabeling rate 削弱框架实用性\n- 超过四分之一的标签在 step-level 上不一致，集中在 death-asymmetry episodes。框架为约 27.7% 的 episodes 给出了\"错误\"的 step-level routing guidance。\n- 建议：分析 mislabeling 对 router 训练的影响；量化 mislabeled episodes 分布；讨论 step-level 信息修正可能性。\n\n### Should-Fix 问题\n\n**W1** [warning] 信号集中度高，11/30 task types 的选择削弱 universality 声明\n- SCI=0.21，top 3 tasks 贡献 29.8%。63% tasks 被排除。被排除 tasks 的 ΔDR=+38.2pp > included 的 +28.7pp，排除并非因为无 death dominance。\n- 建议：讨论 signal concentration 含义；增加 step budget sensitivity analysis。\n\n**W2** [warning] Cross-environment validation 深度不足\n- MATH 仅作 null check，ALFWorld 分析简略。两个环境都未提供正面验证（在新环境中用框架改进 agent）。\n- 建议：对 ALFWorld 做完整 DAF 分解。\n\n**W3** [warning] Router 实验设计的 confounds\n- (a) Step-level vs episode-level gap 可能来自 compounding errors 而非 binary signal；(b) 245 episodes 训练数据可能不足或 LoRA 容量有限；(c) train/val split 是否 episode-level（避免 leakage）？\n- 建议：增加 compounding error ablation；明确 split 方式。\n\n**W4** [warning] Agent improvement 实验统计功效不足\n- Reflexion N=5 trials × 10 tasks = 50 data points；retry n=200 与 Reflexion N=5 compute budget 不对等；72B 也仅 10 tasks；Figure 3 error bars 重叠严重。\n- 建议：paired test + 增大 sample size 或报告 minimum detectable effect size。\n\n**W5** [warning] Router 的 practical value 未建立\n- Trained router（−10.70）未显著优于 always-deterministic（−9.47），oracle 仅 −6.56。即使 perfect routing，改进空间也很小（~3 分）。框架诊断并未转化为实际 routing 改进。\n- 建议：讨论框架的 practical downstream value。\n\n### 小问题\n- \"modality\" 术语歧义（NLP 中通常指 text/vision/audio）\n- Figure 2 的 r=0.97 是预期结果非独立验证\n- Webb (2023) 引用年份疑问\n- Appendix 缺索引\n- Algorithm 1 平分时标注 no-pref 可能掩盖有意义的偏好\n\n### Questions\n1. DAF vs P 曲线（P=100→10→1）？\n2. 27.7% mislabeled episodes 中各 step 实际错误比例？\n3. Step budget 增加到 50/100 时被排除 tasks 是否产生有效信号？\n4. Router train/val 是否 episode-level split？\n5. Oracle routing 上随机翻转 x% 决策的 episode-level 退化曲线？\n\n### Missing References\n- 近期 LLM agent 安全性工作（catastrophic action prevention）\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 1637 · 2026-05-19T14:48:46.858189+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1364
}
```

</details>

---


### Assistant

_source line 1638 · 2026-05-19T14:48:57.853759+00:00_

交叉分享已派发。两位 Reviewer 正在互审对方意见，等待 [AGREE]/[REBUT] 回应。

**当前进度**：
- ✅ Step 0：资料检查 + Venue 调研
- ✅ Step 0.5：Reviewer 编排（2 人）
- ✅ Step 0.7：视觉审查 Agent 已派发
- ✅ Step 1：Round 1 独立审稿完成（R1: 3.5 Borderline Conference / R2: 3.0 Findings）
- 🔄 Step 2：交叉分享进行中，等待回应

**两位 Reviewer 的主要共识点**（初步观察）：
- DAF 的 P-dependence / tautological 性质（R1-N1 ≈ R2-N1）— 双方一致
- 跨环境验证深度不足（R1-W2 ≈ R2-N2）— R2 升为 Must-Fix
- Router 实用价值有限（R1-W5 ≈ R2-N3）— R2 从不同角度切入

**主要分歧点**（待交叉回应确认）：
- R1 强调 K=11 统计推断问题（N2）和 27.7% mislabeling（N3），R2 未单独列为 Must-Fix
- R2 强调 episode-to-step granularity gap（N3），R1 在 W3 中从 confound 角度讨论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 138

## Round 138

2 recorded events


### User

_source line 1639 · 2026-05-19T14:50:40.405312+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: DAF 在高惩罚下近乎 tautological**

完全同意。这与我在 R2-N1 中提出的核心关切一致。DAF = δP/(δP + Δ_nd) 在 P=100 时对 death-rate differential 的放大是代数结构决定的，论文自己在 Appendix K（第 16-17 页）也承认 "this is a mathematical consequence of the decomposition, not evidence of mechanism robustness"。但 Abstract 和 Title 仍以 DAF=90.4% 为叙事中心，framing 和证据之间存在系统性张力。

R1 建议以 78.9% penalty-independent label fraction 为主指标，这与我的建议完全一致。补充一点：即使是 78.9% 这个数字，其稳健性也依赖于 Algorithm 1 的 death-aware labeling 的分层设计——如果改用 score-only labeling（不区分死亡状态），这个比例会变化。建议作者同时报告 score-only labeling 下的 death-correlated fraction 作为 sensitivity check。

**[AGREE] R1-N2: Cluster bootstrap K=11 统计推断不可靠——但严重程度应降级为 Should-Fix**

同意 K=11 远低于 Cameron et al. (2008) 建议的 K≥40 的经验门槛，cluster-level variance 估计确实不可靠。CI [73.0%, 100%] 的极端宽度也印证了这一点。

但我认为 R1 将此定为 critical 过重，理由如下：
1. 论文已提供 **四种**并行推断方法（Table 6, 第 14 页）：standard cluster-robust、wild cluster bootstrap (B=10,000)、exact permutation (p=0.002)，**所有方法均 p<0.001**。即使 cluster bootstrap CI 宽，结论方向一致。
2. Exact permutation 在 2^11=2048 的穷举空间中 p=0.002，意味着仅约 4 个排列产生更极端的统计量——这在 small-K 情况下实际上是相当强的 cluster-level 证据，因为它不依赖渐近近似。
3. 更关键的是，论文的核心发现（78.9% label fraction, DAF decomposition）并不依赖于 cluster bootstrap 的 p-value——它们是描述性统计量，bootstrap 仅提供 uncertainty quantification。

建议作者将 non-clustered bootstrap 提升为主要推断方式，将 cluster bootstrap 标注为 conservative sensitivity check（如 R1 所建议），但 **这一统计问题不应被视为影响接收决定的 critical issue**。论文的方法论诚实性（同时报告四种方法、承认 small-K limitation in Limitations section 第 9 页）值得肯定。

**[AGREE] R1-N3: 27.7% episode-level mislabeling rate 削弱框架实用性**

同意，这与我在 R2-N3 中提出的 episode-level vs. step-level granularity gap 关切高度相关。论文在 Section 3.6（第 6 页）报告 step-level balanced accuracy 仅 54.1±5.4%，且 mislabeling fraction 约 27.7% 集中在 death-asymmetry episodes。

这一数据有两层含义：
1. **诊断层面**（论文的定位）：27.7% 的 mislabeling 不影响 "death avoidance dominates routing signal" 的 episode-level 诊断结论——因为这些 episode 的 episode-level label *确实*反映了 death asymmetry，只是 step-level granularity 更细。
2. **实用层面**（R1 的关切）：如果有人试图用这个框架的输出来训练 step-level router，超过四分之一的训练信号是"错误"的。这严重限制了框架从 "诊断" 到 "行动" 的转化。

R1 建议分析 mislabeled episodes 的分布——这是个好建议。进一步，我建议作者在论文中明确声明框架的适用边界：**本框架是 episode-level 的诊断工具（回答"是否值得建 router"），不是 step-level 的训练信号来源（回答"怎么建 router"）**。目前论文的 framing 对这一区分不够清晰。

---

### Should-Fix 问题

**[REBUT] R1-W1: 信号集中度高、63% tasks 被排除削弱 universality 声明**

部分不同意。R1 指出 "被排除 tasks 的 ΔDR=+38.2pp > included 的 +28.7pp，排除并非因为无 death dominance"——这一观察恰恰 **支持** 而非削弱论文结论。Appendix C（Table 3, 第 12 页）详细列出了 19 个被排除 task types 的排除理由：5 个用于 pipeline development，7 个与 included tasks 分类冗余（taxonomically redundant），7 个 zero-progress tasks（agent capability floor）。排除标准是 methodological（避免数据泄漏和冗余），不是 cherry-picking。

然而，R1 关于 SCI=0.21 的关切有部分合理性：如果 death dominance 集中在少数 task types，那么"routing signal 的 dominant component 是 death avoidance"这一 claim 的 universality 确实受限。论文在 Appendix A（第 12 页）报告 SCI=0.21（top 3 tasks 贡献 29.8%），但也指出 "the aggregate 78.9% reflects a per-task binary structure: all 10 death-prone task types produce 100% death-asymmetry labels"。这意味着 signal concentration 不是"少数 tasks 贡献了大部分 signal"，而是"所有 death-prone tasks 都展示 100% death dominance，只是 magnitude 不同"。

建议作者在主文中更清楚地传达这一区分。

**[AGREE] R1-W2: Cross-environment validation 深度不足**

完全同意，与我的 R2-N2 一致。MATH 作为 null check、ALFWorld 作为 boundary probe 的定位可以接受，但论文标题和 abstract 的 claim scope 超出了这一验证深度。R1 建议对 ALFWorld 做完整 DAF 分解——这是合理的最小要求。

**[AGREE] R1-W3: Router 实验设计的 confounds**

同意 R1 的三个具体关切，但需要纠正一个事实：关于 train/val split，论文在 Appendix J（Table 10, 第 15 页）已经明确报告了 **两种** split 方式的结果：
- **Step-level**: steps from same episode may appear in both train/val → step accuracy 54.1±5.4%
- **Episode-level**: entire episodes held out → episode accuracy 47.1±2.2%

两种方式都接近 chance，排除了 episode-level data leakage 导致 inflated accuracy 的可能。但主文（Section 3.6）对此说明不够清晰，R1 提出这个问题说明表述需要改善。

关于 compounding error ablation，R1 的建议有价值。如果 step-level 的 near-chance accuracy 来自 compounding errors（而非 binary signal），那么在 partial-episode evaluation（如仅评估前 5 步）中 accuracy 应更高。Appendix P（第 19 页）的 capacity scaling 实验接触了这一方向（从 Qwen3-0.6B 到 Qwen3-4B），但未直接测试 partial-episode hypothesis。

**[AGREE] R1-W4: Agent improvement 实验统计功效不足**

同意。Reflexion N=5 × 10 death-prone tasks 的样本量确实小。Figure 3（第 6 页）的 error bars 严重重叠，使得 "Reflexion drops steeply to 34.0% at N=3" 的 claim 缺乏 statistical significance 支撑。论文在 Appendix H（第 14 页）提供了 per-trial breakdown（Table 8），显示 Reflexion's per-trial conditions 在 Trial 3 后 death rate 维持在 ~88%，但这仍是基于很小的 N。

补充：R1 提到 "retry n=200 与 Reflexion N=5 compute budget 不对等"——这是合理的。两种干预的 compute budget 不可比：retry 每 episode 多跑一次（2× cost），Reflexion 每 episode 跑 5 次（5× cost）。论文未报告 per-intervention compute cost，使得跨干预比较不够公平。

**[REBUT] R1-W5: Router 的 practical value 未建立**

部分不同意。R1 的期望是框架应"转化为实际 routing 改进"，但论文从 Section 1 开始就明确将自身定位为 **diagnostic framework**（"We propose a formal diagnostic framework"，第 1 页），而非 routing improvement method。Section 3.6 的 router 训练实验被标题为 "Router Training as Diagnostic Probe"——"as Diagnostic Probe" 明确表示这是诊断工具而非产品。

trained router 未优于 always-deterministic 恰恰验证了论文的核心 claim：在 ScienceWorld 中，routing signal 是 task-type-level binary 的，因此一个 learned step-level router 无法提取比 "always choose deterministic on death-prone tasks" 更多的信息。这是一个 **informative negative result**，而非 framework failure。

然而，我同意 R1 的隐含关切：如果框架的最终建议是"在 death-prone 环境中默认用 deterministic"，那么整个框架的 marginal value 需要更好的论证——"为什么不直接测试两种策略的 death rate 差异就够了？" 论文需要更明确地论证 episode-level counterfactual decomposition 相比简单的 death-rate comparison 提供了什么额外诊断信息。

---

### 小问题回应

- **"modality" 术语歧义**: [AGREE] 合理关切。NLP 社区默认 modality = text/vision/audio，论文用 modality 指 computation modality（internal vs. deterministic）。建议改用 "computation mode" 或 "strategy"。
- **Figure 2 r=0.97 是预期结果**: [AGREE] 与我 R2-W5 一致，这是 decomposition 的代数结果而非独立验证。
- **Webb (2023) 年份**: [AGREE] 与我 R2-M1 一致。
- **Appendix 缺索引**: [AGREE] 17 个 appendices (A-R) 确实需要一个索引表，改善可导航性。
- **Algorithm 1 平分 no-pref**: [AGREE] 但影响较小——no-pref 在总 245 episodes 中占多少比例需要确认。如果比例很低，这不影响结论。

---

### 总体评价对比

R1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于：
1. **Excitement**: R1 给 3/5，我给 2.5/5。我对 obvious-in-hindsight 风险的评估更 pessimistic——"避免死亡比优化 score 更重要" 在直觉上并不令人惊讶，论文的价值更多在于 quantification 和 methodology 而非 finding 本身。
2. **Soundness**: R1 给 3/5，我给 3.5/5。我认为论文的统计方法论（四种 bootstrap 并行、sensitivity analysis、multi-model replication）在 NLP 经验研究中属上乘，K=11 的 cluster bootstrap 问题不应过度权重。
3. **N2 (cluster bootstrap)**: R1 将此定为 critical，我认为应降级为 warning——这不影响核心发现的方向性。

两位 reviewer 的共识区域：DAF 的 P-dependence（R1-N1 = R2-N1）、cross-environment 验证不足（R1-W2 = R2-N2）、episode-to-step granularity gap（R1-N3 ≈ R2-N3）。这三点是论文最需要回应的核心问题。

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

_source line 1640 · 2026-05-19T14:50:52.544227+00:00_

已收到 Reviewer 2 的交叉回应。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 139

## Round 139

12 recorded events


### User

_source line 1641 · 2026-05-19T14:50:53.564823+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心共识：两位 reviewer 在三个关键问题上一致——DAF 的 P-dependence 使 framing 有误导性、跨环境验证不足、episode-to-step granularity gap 限制实用性。分歧在于 cluster bootstrap K=11 的严重程度（我认为应降级）和 router negative result 的解读（我认为是 informative negative result 而非 framework failure）。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2 审稿意见

---

### Must-Fix 问题

**[AGREE] R2-N1: DAF 指标对 death penalty P 的单调依赖使其作为"发现"具有误导性**

同意。这与我的 R1-N1 高度一致。DAF = δP/(δP + Δ\_nd) 在 P=100 下数学上必然趋近 1，论文自己在 §3.1 承认这是"a mathematical consequence of death dominance, not an independent empirical finding"，但标题和 Abstract 仍以 DAF=90.4% 为核心叙事。penalty-independent label fraction 78.9%（§3.1）是更 honest 的指标。论文在 §2.4 明确指出 DAF 随 P 单调递增，Figure 2 的 r=0.97 也是数学结构而非经验发现。建议以 78.9% 为主指标，DAF 降级。

---

**[REBUT] R2-N2: 核心 claim 的 generalizability 证据不足——应升级为完整 DAF 分解或标题加限定**

部分不同意此问题应作为 Must-Fix。理由：

1. **标题已含限定**：标题明确写"A Counterfactual Analysis on ScienceWorld"，并未声称跨环境普适性。
2. **论文的 generality claim 是方法论层面的，非经验层面的**：Limitations（p.9）明确区分："the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical (the specific percentages may differ across environments)." 这一声明是准确的——框架本身（Algorithm 1, DAF 分解）确实可应用于任何有 binary death/alive 结局的环境。
3. **Discussion 中的 NetHack/Crafter 引用是 future work 性质**：§5 最后一段和 Conclusion 说"Future work should target environments with intermediate death regimes, such as NetHack, Crafter"——这是指方向，非外推结论。
4. **跨环境 probes 的深度虽有限但方向正确**：MATH 作为 null check（p=0.81，§3.4）验证了框架的鉴别力（无 catastrophic failure 时正确预测无 routing signal）；ALFWorld（§3.4, Figure 4, Table 14）识别出不同机制（information asymmetry）。两者共同展示框架的 diagnostic 价值。

我的判断：这是 **Should-Fix**（我已在 R1-W2 指出），不是 Must-Fix。补充 ALFWorld 的完整 DAF 定量分解（目前仅有 Figure 4 标签分布，缺 DAF 数值）即可满足。要求在额外 permadeath 环境做完整实验超出了 ARR revision cycle 的合理范围。

---

**[AGREE] R2-N3: Episode-level 到 step-level 的 gap 未充分讨论**

同意这是重要问题，与我的 R1-N3 一致。补充以下证据加强此观点：

1. **27.7% mislabeling rate**（Limitations §38-39）：超过四分之一的 episode-level 标签在 step-level 不一致。论文提到"concentrated in death-asymmetry episodes where early steps may have favored the eventually-dying strategy"——这意味着框架的核心依据（death-asymmetry labels）恰恰是 mislabeling 最集中的子集。
2. **Router 实验数据支撑**：§3.6 报告 step-level balanced accuracy 54.1±5.4%（cross-split），episode-level 47.1±2.2%。这个 gap 可能来自 (a) death avoidance 是 episode-level binary property（论文解释），也可能来自 (b) compounding errors（我在 R1-W3 提出的 confound）。论文没有做实验区分这两种解释。
3. **Method 部分缺少讨论**：§2 定义了 episode-level labeling 但未讨论其 step-level 含义。Limitations 中的讨论太晚且太简短。

不过，我认为此问题的严重程度介于 Must-Fix 和 Should-Fix 之间。论文确实在 Limitations 中坦承了这一点，且 97.4% step-level tie rate（§2.1）为 episode-level 方法提供了合理辩护——如果几乎所有步骤的中间分数相同，step-level oracle 本身就没有鉴别力。建议在 §2 末尾增加一段正式讨论这一 granularity gap 即可，不必重新设计框架。

---

### Should-Fix 问题

**[REBUT] R2-W1: Abstract 数字密度过高**

不同意。Abstract 约 150 词中的数字（78.9%, DAF=90.4%, 11 task types, 245 episodes, P=100, MATH p=0.81, r=0.97, P'=100）均直接对应论文的核心定量发现。对于一篇以 counterfactual empirical analysis 为核心的论文，这些数字是 claim 的 evidence，不是装饰。ACL/EMNLP 的 empirical papers 通常在 abstract 中包含关键数值以区分 contribution 的 specificity。移除数字反而会使 abstract 沦为泛泛之谈。

如果要优化，建议合并而非删除：例如将"245 episodes, 11 task types"合并为一处。但整体密度是合理的。

---

**[AGREE] R2-W2: "Non-triviality of death dominance" 论证说服力不足**

同意。§5 "Non-triviality of death dominance" 段落的论证结构是：death dominance 对干预有 resistance → therefore non-trivial。但 R2 正确指出，hallucination-induced death 作为 hard problem 在 LLM agent 文献中已有广泛共识（ScienceWorld 原论文 Wang et al. 2022 已讨论 agent 死亡问题，ReAct/Reflexion 等工作也涉及）。"干预难以消除死亡"不等于"death dominance 在 routing signal 中的地位是非显然的"。

更有说服力的 non-triviality 论证应该是：(a) prior 上我们可能预期 score difference（non-death component）也是重要的 routing signal，但实证发现 non-death component 仅占 0.8%（§3.1 approximation residual）；(b) 从 routing 文献（RouteLLM, CogRouter 等）出发，现有工作隐含假设 routing signal 来自 capability/quality difference，而非 safety signal——本文揭示这一假设在 interactive environments 中不成立。论文在 §1 和 §4 有此方向的论述但不够集中。

---

**[AGREE] R2-W3: Related Work 中 safe RL 覆盖偏薄**

同意。我在 R1 的 Missing References 中也指出了 safe RL 覆盖不足。§4 Related Work 的 "Safe RL" 段落仅引用了 5 篇经典/概述性工作（Garcia & Fernandez 2015, CPO, CRPO, CVaR, SafeRoute）。Moldovan & Abbeel (2012) 的 safe exploration 形式化与本文的 death avoidance framing 直接相关。Ruan et al. (2024) 的 LLM agent failure taxonomy 也值得引用以定位论文发现在更广泛 failure mode 图景中的位置。

---

**[REBUT] R2-W4: 跨模型复现缺少主文定量表格**

不同意。在 8 页正文限制下，将完整 per-task 表格放入 Appendix M（Table 15, p.17）是标准做法。§3.2 主文已报告关键定量结论：(a) death dominance replicates with 10/10 directional consistency，(b) internal death rate 41.4% vs Qwen 42.9%，(c) deterministic death rate 11.4% vs Qwen 16.3%，(d) differential magnitude varies (+30.0 pp vs +26.5 pp)。这些数字足以让读者在主文中评估 replication 质量。

如果 R2 认为需要更直观的呈现，一个折中方案是在主文添加一个 2-row summary table（Qwen vs Llama 的 aggregate metrics），而非搬入完整的 11-task breakdown。

---

**[AGREE] R2-W5: Figure 2 regression line解读过度**

同意，与我的 minor issue 一致。Figure 2（p.4）caption 应明确注明 r=0.97 是 DAF 分解的数学结构的预期结果，而非独立的经验验证。当前 caption 说"see text for interpretation"但正文的说明（§3.1）也比较含糊——说"near-perfect correlation is structurally implied by the decomposition"但紧接着就用它来支持 finding。建议 caption 直接写："The near-perfect correlation is a structural consequence of the DAF decomposition (Eq. 4), not an independent empirical validation."

---

### 总结

| R2 Issue | 我的判断 | 与 R1 审稿的关系 |
|----------|--------|----------------|
| N1 (DAF misleading) | **AGREE** — critical | 与 R1-N1 一致 |
| N2 (generalizability) | **REBUT** — 降为 Should-Fix | R1-W2 已提出类似但更温和 |
| N3 (episode→step gap) | **AGREE** — 介于 critical/warning | 与 R1-N3 一致 |
| W1 (abstract density) | **REBUT** | R1 未提此问题 |
| W2 (non-triviality weak) | **AGREE** | R1 未单独提出但认同 |
| W3 (safe RL thin) | **AGREE** | 与 R1 Missing References 一致 |
| W4 (cross-model table) | **REBUT** | R1 未提此问题 |
| W5 (Figure 2 overinterp) | **AGREE** | 与 R1 minor issue 一致 |

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

_source line 1642 · 2026-05-19T14:51:24.539178+00:00_

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

_source line 1643 · 2026-05-19T14:51:24.589822+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"timeout\", \"elapsed_seconds\": 655}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1644 · 2026-05-19T14:51:24.690605+00:00_

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

_source line 1645 · 2026-05-19T14:51:24.791446+00:00_

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

_source line 1646 · 2026-05-19T14:52:12.862200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
  "limit": "680"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
    "limit": "680"
  }
}
```

</details>

---


### Tool result

_source line 1647 · 2026-05-19T14:52:12.914887+00:00_

1	## Round 17 Review Issues (updated 2026-05-19 D123 action matrix dispatched)
2	
3	# =============================================
4	# Resolved issues from prior rounds (unchanged)
5	# =============================================
6	
7	- id: "R13-N1"
8	  summary: "DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现"
9	  category: framing
10	  severity: critical
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 15
14	  mentions:
15	    - round: 13
16	      reviewers: [1, 2]
17	      note: "Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。"
18	    - round: 14
19	      reviewers: [1, 2]
20	      note: "R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。"
21	    - round: 15
22	      reviewers: [1, 2]
23	      note: "R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。"
24	    - round: 16
25	      reviewers: []
26	      note: "R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。"
27	  resolution: "78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence"
28	  resolution_round: 15
29	
30	- id: "R13-N3"
31	  summary: "跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication"
32	  category: experiment
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 13
36	  last_seen_round: 15
37	  resolution: "标题和 Contribution 措辞已恰当限定 scope"
38	  resolution_round: 15
39	
40	- id: "R13-W1"
41	  summary: "正文篇幅严重不足 long paper 要求"
42	  category: format
43	  severity: warning
44	  status: resolved
45	  first_raised_round: 13
46	  last_seen_round: 14
47	  resolution: "正文已扩展至 8 页"
48	  resolution_round: 14
49	
50	- id: "R13-W2"
51	  summary: "Router 训练实验存在多个 confound"
52	  category: experiment
53	  severity: warning
54	  status: resolved
55	  first_raised_round: 13
56	  last_seen_round: 15
57	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
58	  resolution_round: 15
59	
60	- id: "R13-W3"
61	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
62	  category: method
63	  severity: info
64	 
…[truncated 21817 chars]

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

_source line 1648 · 2026-05-19T14:58:25.633144+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "## Round 18 Review Issues (fresh review, updated 2026-05-19)\n\n# =============================================\n# Resolved issues from prior rounds (unchanged)\n# =============================================\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。\"\n    - round: 16\n      reviewers: []\n      note: \"R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18 fresh review 两位 reviewer 均再次将 DAF P-dependence 列为 critical Must-Fix。当前版本 title/abstract 仍以 DAF=90.4% 为叙事中心。Resolution 可能未有效落地或有回归。参见 R18 consolidated MF1。\"\n  resolution: \"78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence\"\n  resolution_round: 15\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化 27.7% mislabeling fraction\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18 fresh review 两位 reviewer 再次提出 safe RL 覆盖偏薄（R2-W3, R1 Missing Refs agree）。当前版本 §4 safe RL 段仍仅一句话带过五篇引用。Resolution 可能未充分落地。\"\n  resolution: \"引用覆盖充分，orphan entries 已清理\"\n  resolution_round: 15\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld + MATH N 标注不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及 minority-class diversity confound\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'，structural 仅用于 router failure 的 Appendix 描述\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n# =============================================\n# Open / in_progress issues\n# =============================================\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11、per-task n=20\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. Cluster bootstrap K=11 违反 K>=40 要求。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 divergence on severity. 降级为 warning。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 consensus. Cautionary language 和 Cameron 2008 引用到位。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1 标为 Must-Fix (CI [73%,100%] 过宽，cluster exchangeability 受限)。R2 rebut 降为 Should-Fix (Cohen's d=3.02, exact permutation p=0.002 不依赖 asymptotic assumptions)。Director 裁决：维持 warning。方向性结论 robust，magnitude 精度有限但 CI 下界仍排除 50%。建议正文提升 Cohen's d。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R1 再提为 Critical（CI [73%,100%] 极宽，2^11 穷举下 p=0.002 不如表面强）。R2 rebut 降级（四种方法均 p<0.001，exact permutation 不依赖渐近近似，核心发现是描述性统计量）。Director 裁决：维持 warning。建议 non-clustered bootstrap 为主推断，cluster bootstrap 标为 sensitivity check。\"\n  action_items:\n    - round: 13\n      action: \"对 cluster bootstrap K=11 做更诚实讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 17\n      action: \"将 Cohen's d=3.02 从 Appendix 提升至正文 §3.1；明确 primary CI 为 episode-level bootstrap，cluster-level CI 为 sensitivity analysis\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"正文以 non-clustered bootstrap 为主要推断方式，cluster bootstrap 标注为 conservative sensitivity check\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"约 200 词中 10+ 统计量。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍含 12+ 数字。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus. ~140 词中约 12 个数字。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 consensus. 当前 ~140 词中 8+ 数字。R1/R2 均建议保留 78.9% 和 p=0.81，其余改为定性概括。\"\n    - round: 18\n      reviewers: [2]\n      note: \"R18: R2 再提 (~150 词中 8+ 数字)。R1 rebut: empirical paper 数字是证据非装饰。Director: 分歧保留，不列入正式 weakness。R1 rebuttal 有理但建议合并冗余数字。\"\n  action_items:\n    - round: 17\n      action: \"Abstract 保留 78.9%、DAF 90.4%、p=0.81 三个关键数字；retry/scaling/Reflexion 具体数字改为定性描述\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 认为 78.9% 也 trivial；R1 认为 δ=0.265 是 empirical 非先验可知。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus (critical). back-of-envelope 可预测 death dominance。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 consensus. 两人均认为 reframing 为 'death dominance resists interventions' 可提升 novelty perception。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2-W2 non-triviality 论证不足 (resistance to intervention = hard problem 已有共识)。R1 agree。两人建议从 routing 文献 prior assumptions 出发论证。R2 Excitement 2.5/5, R1 3/5。\"\n  action_items:\n    - round: 17\n      action: \"核心叙事 reframe: 强调 intervention robustness 而非 death dominance 本身的发现\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"§5 non-triviality 段从 routing 文献 prior assumptions 出发重写——现有工作假设 signal 来自 capability/quality difference，本文揭示在 interactive environments 中不成立\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 consensus.\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 同意模态定义差异应更 prominently 讨论。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及此 issue。跨环境讨论被 generalizability 大议题覆盖。可能已充分处理或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"Table 2 caption 逐项注明每环境 deterministic 的具体含义\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及此 issue。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。被 R18-N1 (episode→step gap) 整体讨论覆盖。\"\n  action_items:\n    - round: 16\n      action: \"§3.7 补充 oracle margin 与 mislabeling 的独立性讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M1\"\n  summary: \"缺少 permadeath 环境 LLM agent 工作引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"ToolACE, Inner Monologue, Tamar 2015 已补充。NetHack/Crafter LLM agent 工作仍缺。\"\n    - round: 17\n      reviewers: [1]\n      note: \"R17 R1 建议 HuggingGPT, CREATOR, SafeDreamer。R2 建议 ToolBench。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2 建议补充 Moldovan & Abbeel 2012 (safe exploration), Ruan et al. 2024 (LLM agent failure taxonomy), Graves 2016 (adaptive computation time)。R1 建议补充近期 catastrophic action prevention 工作。\"\n  action_items:\n    - round: 17\n      action: \"检查并补充 LLM agent in permadeath environments 引用\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"补充 Moldovan & Abbeel 2012, Ruan et al. 2024, Graves 2016；评估近期 catastrophic action prevention 工作\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit: death dominance 在 ScienceWorld penalty 结构下可从 back-of-envelope 预测\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Strong consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 strong consensus. Reframe 方向：'death dominance resists standard interventions'。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2 Excitement 2.5/5, R1 3/5。R2-W2 指出 non-triviality 论证不足（resistance to intervention = hard problem 已有共识）。R1 agree。两人均认为论文价值在 quantification 和 methodology 而非 finding 本身。\"\n  action_items:\n    - round: 17\n      action: \"Reframe Introduction/Abstract 核心叙事从 finding 转向 methodology + intervention robustness\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"63% exclusion 意味着 death dominance 可能仅适用于 ScienceWorld 特定 task subset。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 论证充分但应在正文明确标注。\"\n    - round: 18\n      reviewers: [1]\n      note: \"R18 R1-W1 再提：SCI=0.21, top 3 tasks 贡献 29.8%。被排除 tasks ΔDR=+38.2pp 支持非 cherry-picking，但排除率仍是 scope limitation。R2 rebut: 排除标准 methodological (Table 3)，所有 death-prone tasks 100% death dominance，signal concentration 是 magnitude 差异非 existence 差异。Director: 维持 warning。\"\n  action_items:\n    - round: 17\n      action: \"§3 开头段明确标注 63% exclusion 是 scope limitation 而非仅在 Limitations 提及\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N3\"\n  summary: \"实验规模和环境多样性不足: 缺少 permadeath 环境 replication (NetHack/Crafter)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"两位 reviewer 均认为这是影响 Conference vs Findings 定位的关键因素。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 strong consensus. 补充第二个 permadeath 环境是从 Findings 提升至 Conference 的关键。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2-N2 列为 Must-Fix (需 permadeath 完整 DAF 分解或标题加限定)。R1 rebut 降为 Should-Fix (标题已含 'on ScienceWorld' 限定，generality claim 是方法论层面)。MiniHack pilot 结果为 negative (项目 overview)。Director: 降为 Should-Fix——R1 rebuttal 成立。ALFWorld 需完整 DAF 定量分解。\"\n  action_items:\n    - round: 17\n      action: \"MiniHack pilot N>=100 via BALROG\"\n      assigned_to: main_agent\n      status: in_progress\n    - round: 18\n      action: \"ALFWorld 做完整 DAF 定量分解（当前仅 Figure 4 标签分布，缺 DAF 数值）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"§3.3 将 72B DAF=90.9% 直接与 7B DAF=90.4% 比较时未强调 population 差异。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"72B 实验设计不明确。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及此 issue。可能已修复或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"明确 72B 实验设计; 报告 72B deterministic death rate 和 Δ_nd; 注明 population 差异\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。连续两轮未被提出，可能已修复或不再突出，待 Research Director 确认。\"\n  action_items:\n    - round: 16\n      action: \"补充 1.7B per-class confusion matrix 或弱化解释\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及，当前版本 Appendix I 已引用 signal_reversal.pdf (Figure 4)。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 16\n      action: \"正式引入或删除 signal_reversal.pdf\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载（覆盖 finding + robustness + router diagnostic）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 首提，R1 同意。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 维持 warning。建议将 router diagnostic 移入 Contribution 1。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。可能已修复或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"将 router-as-diagnostic-probe 从 Contribution 2 移至 Contribution 1\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致 (find-non-living vs find-non-living-thing)\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及，待 Research Director 确认是否已修复。\"\n  action_items:\n    - round: 16\n      action: \"统一 task name\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction 在 task level 呈现 binary split (death-prone 100%, death-free 0%)，aggregate 是 task composition artifact\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N1 首提，R2 强烈同意。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立 issue 提出。被 DAF framing 大议题（MF1）覆盖。\"\n  action_items:\n    - round: 17\n      action: \"§3.1 增加 binary per-task structure 讨论; LOTO-DAF 关键结论提升至正文\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-N2\"\n  summary: \"'penalty-independent' 表述误导：72% death-asymmetry labels 在 P=0 时退化为 ties\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"P=0 时 effective non-tie labels 仅 41 个，death-asymmetry fraction 降至 51.2%。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立 issue 提出。R2-Q2 询问 P=-1 时 78.9% 是否变化，间接触及此问题。\"\n  action_items:\n    - round: 17\n      action: \"明确区分 labeling-function-level vs practical-value-level penalty independence; 报告 P=0 lower bound 51.2%\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic mixed-strategy routing 的影响\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"42.9% internal death rate 是 pure-strategy worst-case。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立 issue 提出。被 episode→step gap (R18-N1) 整体覆盖。\"\n  action_items:\n    - round: 17\n      action: \"Discussion 增加一段讨论 pure-strategy diagnostic vs mixed-strategy deployment 的 gap\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Figure 1 (scatter plot) caption 缺 'mathematical consequence' caveat\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W2 首提，R2 同意。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2-W5 再提（caption 需注明 structural consequence），R1 交叉回应 agree。建议 caption 直接写 'structural consequence of the DAF decomposition (Eq. 4), not an independent empirical validation'。\"\n  action_items:\n    - round: 17\n      action: \"Figure 1 caption 添加 structural consequence caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W3\"\n  summary: \"Data scaling ablation 的 'structural failure' 结论基于 paraphrase augmentation 而非 real data\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"'structural failure' 应弱化为 'failure under current data regime'。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。可能已修复或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"Appendix F 和 §3.7 将 'structural' 改为 'under current data distribution / augmentation regime'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Related Work §5 第一段有论文罗列倾向\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"应按功能类别做 comparative positioning。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。可能已修复或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"Related Work 第一段按功能类别重组\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry (altman1999cmdp) + ART 等条目需更新为正式出版信息\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"altman1999cmdp 在 references.bib 中存在但未被 .tex 引用。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2-M1 和 R1 均指出 webb-2023 年份可能有误（OpenAlex 匹配到 2014 版本）。altman1999cmdp 未再提及。引用验证：46 条中 36 verified, 6 mismatch (author encoding), 4 not_found (OpenAlex 索引), 0 orphan, 0 missing。\"\n  action_items:\n    - round: 17\n      action: \"删除 altman1999cmdp orphan entry；更新 ART 等已发表论文的 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"核实 webb-2023 引用年份（2014 working paper vs 2023 正式发表）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# =============================================\n# Round 18 New Issues\n# =============================================\n\n- id: \"R18-N1\"\n  summary: \"Episode-level 到 step-level 的 granularity gap 削弱框架实用性——框架适用边界未在 Method 中正式讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2-N3 强共识。Router step-level balanced accuracy 54.1±5.4% ≈ chance。27.7% mislabeling 集中在 death-asymmetry episodes。R2: 框架是 episode-level 诊断工具非 step-level 训练信号来源，需明确声明适用边界。R1: 应分析 mislabeling 对 router 训练的具体影响。97.4% step-level tie rate 为 episode-level 方法提供合理辩护但需在 Method 部分说明。\"\n  action_items:\n    - round: 18\n      action: \"§2 末尾或 §3.6 增加正式讨论：(1) 框架适用边界（episode-level diagnostic vs step-level guidance）; (2) 97.4% step-level tie rate 为 episode-level 方法的合理性论证; (3) mislabeling 分布分析\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors 可能解释 step→episode gap，train/val split 方式主文不清晰\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W3 首提。Step→episode gap 可能来自 compounding errors 而非 binary signal。R2 确认 Appendix J 已报告 episode-level split（排除 leakage），但主文不清晰。R2 建议 partial-episode evaluation ablation。\"\n  action_items:\n    - round: 18\n      action: \"(1) §3.6 主文明确 train/val 是 episode-level split; (2) 考虑增加 compounding error ablation（partial-episode evaluation）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足: Reflexion N=5, Figure 3 error bars 严重重叠\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W4 首提，R2 agree。Reflexion N=5 × 10 tasks = 50 data points。Retry n=200 与 Reflexion N=5 compute budget 不对等。论文未报告 per-intervention compute cost。\"\n  action_items:\n    - round: 18\n      action: \"报告 Reflexion vs baseline 的 paired test 或 minimum detectable effect size; 注明 compute budget 差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义（通常指 text/vision/audio）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1 minor issue。建议改用 'computation mode' 或 'strategy'。\"\n  action_items:\n    - round: 18\n      action: \"评估是否将 'modality' 改为 'computation mode' 或 'strategy'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-M2\"\n  summary: \"100% internal-strategy deaths 来自同一 action pattern (focus on [object])——implication 未讨论\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [2]\n      note: \"R2-M5: death avoidance 本质上等价于 'avoid focus on [object]'，进一步支持 signal 是 trivially binary。建议讨论 implication。\"\n  action_items:\n    - round: 18\n      action: \"§5 'Anatomy of catastrophic failure' 段讨论 single action pattern 的 implication\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "## Round 18 Review Issues (fresh review, updated 2026-05-19)\n\n# =============================================\n# Resolved issues from prior rounds (unchanged)\n# =============================================\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 consensus. dual-metric 设计到位但 DAF 仍获更多权重。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。\"\n    - round: 16\n      reviewers: []\n      note: \"R16 未单独提及此 issue（已 resolved），但 novelty concern（R16-N1）延续了 framing 讨论。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18 fresh review 两位 reviewer 均再次将 DAF P-dependence 列为 critical Must-Fix。当前版本 title/abstract 仍以 DAF=90.4% 为叙事中心。Resolution 可能未有效落地或有回归。参见 R18 consolidated MF1。\"\n  resolution: \"78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence\"\n  resolution_round: 15\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化 27.7% mislabeling fraction\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18 fresh review 两位 reviewer 再次提出 safe RL 覆盖偏薄（R2-W3, R1 Missing Refs agree）。当前版本 §4 safe RL 段仍仅一句话带过五篇引用。Resolution 可能未充分落地。\"\n  resolution: \"引用覆盖充分，orphan entries 已清理\"\n  resolution_round: 15\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld + MATH N 标注不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及 minority-class diversity confound\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'，structural 仅用于 router failure 的 Appendix 描述\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n# =============================================\n# Open / in_progress issues\n# =============================================\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11、per-task n=20\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. Cluster bootstrap K=11 违反 K>=40 要求。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 divergence on severity. 降级为 warning。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 consensus. Cautionary language 和 Cameron 2008 引用到位。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1 标为 Must-Fix (CI [73%,100%] 过宽，cluster exchangeability 受限)。R2 rebut 降为 Should-Fix (Cohen's d=3.02, exact permutation p=0.002 不依赖 asymptotic assumptions)。Director 裁决：维持 warning。方向性结论 robust，magnitude 精度有限但 CI 下界仍排除 50%。建议正文提升 Cohen's d。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R1 再提为 Critical（CI [73%,100%] 极宽，2^11 穷举下 p=0.002 不如表面强）。R2 rebut 降级（四种方法均 p<0.001，exact permutation 不依赖渐近近似，核心发现是描述性统计量）。Director 裁决：维持 warning。建议 non-clustered bootstrap 为主推断，cluster bootstrap 标为 sensitivity check。\"\n  action_items:\n    - round: 13\n      action: \"对 cluster bootstrap K=11 做更诚实讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 17\n      action: \"将 Cohen's d=3.02 从 Appendix 提升至正文 §3.1；明确 primary CI 为 episode-level bootstrap，cluster-level CI 为 sensitivity analysis\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"正文以 non-clustered bootstrap 为主要推断方式，cluster bootstrap 标注为 conservative sensitivity check\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"约 200 词中 10+ 统计量。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍含 12+ 数字。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus. ~140 词中约 12 个数字。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 consensus. 当前 ~140 词中 8+ 数字。R1/R2 均建议保留 78.9% 和 p=0.81，其余改为定性概括。\"\n    - round: 18\n      reviewers: [2]\n      note: \"R18: R2 再提 (~150 词中 8+ 数字)。R1 rebut: empirical paper 数字是证据非装饰。Director: 分歧保留，不列入正式 weakness。R1 rebuttal 有理但建议合并冗余数字。\"\n  action_items:\n    - round: 17\n      action: \"Abstract 保留 78.9%、DAF 90.4%、p=0.81 三个关键数字；retry/scaling/Reflexion 具体数字改为定性描述\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 认为 78.9% 也 trivial；R1 认为 δ=0.265 是 empirical 非先验可知。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus (critical). back-of-envelope 可预测 death dominance。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 consensus. 两人均认为 reframing 为 'death dominance resists interventions' 可提升 novelty perception。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2-W2 non-triviality 论证不足 (resistance to intervention = hard problem 已有共识)。R1 agree。两人建议从 routing 文献 prior assumptions 出发论证。R2 Excitement 2.5/5, R1 3/5。\"\n  action_items:\n    - round: 17\n      action: \"核心叙事 reframe: 强调 intervention robustness 而非 death dominance 本身的发现\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"§5 non-triviality 段从 routing 文献 prior assumptions 出发重写——现有工作假设 signal 来自 capability/quality difference，本文揭示在 interactive environments 中不成立\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 consensus.\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 同意模态定义差异应更 prominently 讨论。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及此 issue。跨环境讨论被 generalizability 大议题覆盖。可能已充分处理或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"Table 2 caption 逐项注明每环境 deterministic 的具体含义\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16 consensus.\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及此 issue。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。被 R18-N1 (episode→step gap) 整体讨论覆盖。\"\n  action_items:\n    - round: 16\n      action: \"§3.7 补充 oracle margin 与 mislabeling 的独立性讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M1\"\n  summary: \"缺少 permadeath 环境 LLM agent 工作引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"ToolACE, Inner Monologue, Tamar 2015 已补充。NetHack/Crafter LLM agent 工作仍缺。\"\n    - round: 17\n      reviewers: [1]\n      note: \"R17 R1 建议 HuggingGPT, CREATOR, SafeDreamer。R2 建议 ToolBench。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2 建议补充 Moldovan & Abbeel 2012 (safe exploration), Ruan et al. 2024 (LLM agent failure taxonomy), Graves 2016 (adaptive computation time)。R1 建议补充近期 catastrophic action prevention 工作。\"\n  action_items:\n    - round: 17\n      action: \"检查并补充 LLM agent in permadeath environments 引用\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"补充 Moldovan & Abbeel 2012, Ruan et al. 2024, Graves 2016；评估近期 catastrophic action prevention 工作\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit: death dominance 在 ScienceWorld penalty 结构下可从 back-of-envelope 预测\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Strong consensus.\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 strong consensus. Reframe 方向：'death dominance resists standard interventions'。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2 Excitement 2.5/5, R1 3/5。R2-W2 指出 non-triviality 论证不足（resistance to intervention = hard problem 已有共识）。R1 agree。两人均认为论文价值在 quantification 和 methodology 而非 finding 本身。\"\n  action_items:\n    - round: 17\n      action: \"Reframe Introduction/Abstract 核心叙事从 finding 转向 methodology + intervention robustness\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"63% exclusion 意味着 death dominance 可能仅适用于 ScienceWorld 特定 task subset。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 论证充分但应在正文明确标注。\"\n    - round: 18\n      reviewers: [1]\n      note: \"R18 R1-W1 再提：SCI=0.21, top 3 tasks 贡献 29.8%。被排除 tasks ΔDR=+38.2pp 支持非 cherry-picking，但排除率仍是 scope limitation。R2 rebut: 排除标准 methodological (Table 3)，所有 death-prone tasks 100% death dominance，signal concentration 是 magnitude 差异非 existence 差异。Director: 维持 warning。\"\n  action_items:\n    - round: 17\n      action: \"§3 开头段明确标注 63% exclusion 是 scope limitation 而非仅在 Limitations 提及\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N3\"\n  summary: \"实验规模和环境多样性不足: 缺少 permadeath 环境 replication (NetHack/Crafter)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"两位 reviewer 均认为这是影响 Conference vs Findings 定位的关键因素。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17 strong consensus. 补充第二个 permadeath 环境是从 Findings 提升至 Conference 的关键。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2-N2 列为 Must-Fix (需 permadeath 完整 DAF 分解或标题加限定)。R1 rebut 降为 Should-Fix (标题已含 'on ScienceWorld' 限定，generality claim 是方法论层面)。MiniHack pilot 结果为 negative (项目 overview)。Director: 降为 Should-Fix——R1 rebuttal 成立。ALFWorld 需完整 DAF 定量分解。\"\n  action_items:\n    - round: 17\n      action: \"MiniHack pilot N>=100 via BALROG\"\n      assigned_to: main_agent\n      status: in_progress\n    - round: 18\n      action: \"ALFWorld 做完整 DAF 定量分解（当前仅 Figure 4 标签分布，缺 DAF 数值）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"§3.3 将 72B DAF=90.9% 直接与 7B DAF=90.4% 比较时未强调 population 差异。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"72B 实验设计不明确。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及此 issue。可能已修复或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"明确 72B 实验设计; 报告 72B deterministic death rate 和 Δ_nd; 注明 population 差异\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。连续两轮未被提出，可能已修复或不再突出，待 Research Director 确认。\"\n  action_items:\n    - round: 16\n      action: \"补充 1.7B per-class confusion matrix 或弱化解释\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及，当前版本 Appendix I 已引用 signal_reversal.pdf (Figure 4)。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 16\n      action: \"正式引入或删除 signal_reversal.pdf\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载（覆盖 finding + robustness + router diagnostic）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 首提，R1 同意。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 维持 warning。建议将 router diagnostic 移入 Contribution 1。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。可能已修复或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"将 router-as-diagnostic-probe 从 Contribution 2 移至 Contribution 1\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致 (find-non-living vs find-non-living-thing)\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及，待 Research Director 确认是否已修复。\"\n  action_items:\n    - round: 16\n      action: \"统一 task name\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction 在 task level 呈现 binary split (death-prone 100%, death-free 0%)，aggregate 是 task composition artifact\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N1 首提，R2 强烈同意。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立 issue 提出。被 DAF framing 大议题（MF1）覆盖。\"\n  action_items:\n    - round: 17\n      action: \"§3.1 增加 binary per-task structure 讨论; LOTO-DAF 关键结论提升至正文\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-N2\"\n  summary: \"'penalty-independent' 表述误导：72% death-asymmetry labels 在 P=0 时退化为 ties\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"P=0 时 effective non-tie labels 仅 41 个，death-asymmetry fraction 降至 51.2%。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立 issue 提出。R2-Q2 询问 P=-1 时 78.9% 是否变化，间接触及此问题。\"\n  action_items:\n    - round: 17\n      action: \"明确区分 labeling-function-level vs practical-value-level penalty independence; 报告 P=0 lower bound 51.2%\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic mixed-strategy routing 的影响\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"42.9% internal death rate 是 pure-strategy worst-case。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立 issue 提出。被 episode→step gap (R18-N1) 整体覆盖。\"\n  action_items:\n    - round: 17\n      action: \"Discussion 增加一段讨论 pure-strategy diagnostic vs mixed-strategy deployment 的 gap\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Figure 1 (scatter plot) caption 缺 'mathematical consequence' caveat\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W2 首提，R2 同意。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2-W5 再提（caption 需注明 structural consequence），R1 交叉回应 agree。建议 caption 直接写 'structural consequence of the DAF decomposition (Eq. 4), not an independent empirical validation'。\"\n  action_items:\n    - round: 17\n      action: \"Figure 1 caption 添加 structural consequence caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W3\"\n  summary: \"Data scaling ablation 的 'structural failure' 结论基于 paraphrase augmentation 而非 real data\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"'structural failure' 应弱化为 'failure under current data regime'。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。可能已修复或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"Appendix F 和 §3.7 将 'structural' 改为 'under current data distribution / augmentation regime'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Related Work §5 第一段有论文罗列倾向\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"应按功能类别做 comparative positioning。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。可能已修复或不再突出。\"\n  action_items:\n    - round: 17\n      action: \"Related Work 第一段按功能类别重组\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry (altman1999cmdp) + ART 等条目需更新为正式出版信息\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"altman1999cmdp 在 references.bib 中存在但未被 .tex 引用。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R2-M1 和 R1 均指出 webb-2023 年份可能有误（OpenAlex 匹配到 2014 版本）。altman1999cmdp 未再提及。引用验证：46 条中 36 verified, 6 mismatch (author encoding), 4 not_found (OpenAlex 索引), 0 orphan, 0 missing。\"\n  action_items:\n    - round: 17\n      action: \"删除 altman1999cmdp orphan entry；更新 ART 等已发表论文的 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"核实 webb-2023 引用年份（2014 working paper vs 2023 正式发表）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# =============================================\n# Round 18 New Issues\n# =============================================\n\n- id: \"R18-N1\"\n  summary: \"Episode-level 到 step-level 的 granularity gap 削弱框架实用性——框架适用边界未在 Method 中正式讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2-N3 强共识。Router step-level balanced accuracy 54.1±5.4% ≈ chance。27.7% mislabeling 集中在 death-asymmetry episodes。R2: 框架是 episode-level 诊断工具非 step-level 训练信号来源，需明确声明适用边界。R1: 应分析 mislabeling 对 router 训练的具体影响。97.4% step-level tie rate 为 episode-level 方法提供合理辩护但需在 Method 部分说明。\"\n  action_items:\n    - round: 18\n      action: \"§2 末尾或 §3.6 增加正式讨论：(1) 框架适用边界（episode-level diagnostic vs step-level guidance）; (2) 97.4% step-level tie rate 为 episode-level 方法的合理性论证; (3) mislabeling 分布分析\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors 可能解释 step→episode gap，train/val split 方式主文不清晰\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W3 首提。Step→episode gap 可能来自 compounding errors 而非 binary signal。R2 确认 Appendix J 已报告 episode-level split（排除 leakage），但主文不清晰。R2 建议 partial-episode evaluation ablation。\"\n  action_items:\n    - round: 18\n      action: \"(1) §3.6 主文明确 train/val 是 episode-level split; (2) 考虑增加 compounding error ablation（partial-episode evaluation）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足: Reflexion N=5, Figure 3 error bars 严重重叠\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W4 首提，R2 agree。Reflexion N=5 × 10 tasks = 50 data points。Retry n=200 与 Reflexion N=5 compute budget 不对等。论文未报告 per-intervention compute cost。\"\n  action_items:\n    - round: 18\n      action: \"报告 Reflexion vs baseline 的 paired test 或 minimum detectable effect size; 注明 compute budget 差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义（通常指 text/vision/audio）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1 minor issue。建议改用 'computation mode' 或 'strategy'。\"\n  action_items:\n    - round: 18\n      action: \"评估是否将 'modality' 改为 'computation mode' 或 'strategy'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-M2\"\n  summary: \"100% internal-strategy deaths 来自同一 action pattern (focus on [object])——implication 未讨论\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [2]\n      note: \"R2-M5: death avoidance 本质上等价于 'avoid focus on [object]'，进一步支持 signal 是 trivially binary。建议讨论 implication。\"\n  action_items:\n    - round: 18\n      action: \"§5 'Anatomy of catastrophic failure' 段讨论 single action pattern 的 implication\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1649 · 2026-05-19T14:58:25.734672+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 26166}, \"error\": \"\"}"}

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

_source line 1650 · 2026-05-19T15:00:31.387426+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 18 审稿报告 — simgate-modular-routing\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual 诊断框架，分析模块化 LLM agent 中 routing signal 的组成。在 ScienceWorld 上（245 episodes, 11/30 task types, Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 来自 death asymmetry（internal strategy 的 hallucination 触发 catastrophic death，deterministic strategy 存活），DAF=90.4%。框架在 MATH（null check, p=0.81）和 ALFWorld（识别 information asymmetry 替代机制）做了跨环境探测，在 Llama-3.1-8B 做了跨模型复现（10/10 directional consistency）。四类干预（retry/Reflexion/10× scaling/action filtering）均未消除 death dominance。Router 训练作为 diagnostic probe 显示 step-level routing signal 不可学习（balanced accuracy 54.1±5.4% ≈ chance）。\n\n---\n\n## Strengths\n\n**S1. 形式化贡献扎实** [R1, R2 共识]\nCounterfactual labeling function（Algorithm 1）和 DAF 分解（Eq. 4-5）定义清晰，框架可复用于任何有 binary fatal outcome 的环境。\n\n**S2. 统计方法论严谨** [R1, R2 共识]\n四种并行推断方法（standard cluster-robust, wild cluster bootstrap, exact permutation, non-clustered bootstrap），SCI 量化 signal 集中度，leave-one-task-out 验证。在 NLP 经验研究中属上乘水准。\n\n**S3. 多维度验证体系** [R1, R2 共识]\n跨模型（Llama 3.1-8B, 10/10 directional consistency）、跨环境（MATH null check, ALFWorld qualitative）、四类干预、per-seed breakdown、labeling quality audit。覆盖面远超一般 agent 论文。\n\n**S4. 78.9% penalty-independent label fraction 是干净的经验发现** [R1, R2 共识]\n该数字不依赖 death penalty P 的大小，是论文最有说服力的定量结论。\n\n**S5. 诚实的自我批判** [R1, R2 共识]\n论文主动报告 DAF 的 P-dependence、K=11 limitation、27.7% mislabeling rate。Practitioner Decision Framework（Appendix R）提供实操指导。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, R1-N1 + R2-N1, 强共识] **DAF 指标在高惩罚下近乎 tautological，核心 framing 有误导性**\n\nDAF = δP/(δP + Δ_nd) 在 P=100 时数学上必然趋近 1。论文自己承认这是 \"a mathematical consequence\"（§3.1, §5），但 title 和 abstract 仍以 DAF=90.4% 为核心叙事。Penalty-independent label fraction 78.9% 是更 honest 的指标但被置于次要位置。\n\n**Director 裁决**：必须修改。以 78.9% 为主指标，DAF 降级为 P-dependent 辅助指标。正文需呈现 DAF vs P 敏感性曲线（Appendix K 数据已有）。标题和 abstract 不应以 DAF 数值为叙事锚点。\n\n**MF2** [critical, R1-N3 + R2-N3, 强共识] **Episode-level 到 step-level 的 granularity gap 削弱框架实用性**\n\n论文定义 routing signal 为 episode-level pure-strategy performance gap，但实际 routing 发生在 step level。Router 训练（step-level balanced accuracy 54.1±5.4% ≈ chance）暴露了这一断层。27.7% 的 episode-level 标签在 step-level 上不一致，且集中在 death-asymmetry episodes。\n\nR2 补充：论文应明确声明框架是 episode-level 诊断工具（回答\"是否值得建 router\"），不是 step-level 训练信号来源。R1 进一步指出应分析 mislabeling 对 router 训练的具体影响。97.4% step-level tie rate 为 episode-level 方法提供了合理辩护，但需要在 Method 部分而非仅 Limitations 中说明。\n\n**Director 裁决**：必须在 §2 末尾或 §3.6 增加正式讨论，明确框架适用边界。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, R2-N2 提出, R1 rebut 降级] **跨环境 generalizability 证据不足**\n\nR2 列为 Must-Fix（需 permadeath 环境完整 DAF 分解或标题加限定）。R1 rebut：标题已含 \"on ScienceWorld\" 限定，generality claim 是方法论层面非经验层面，Discussion 对未测试环境是 future work 指向。\n\n**Director 裁决**：维持 Should-Fix。R1 rebuttal 成立——标题已限定 scope。但 ALFWorld 应提供完整 DAF 定量分解（当前仅 Figure 4 标签分布，缺 DAF 数值）。补充第二个 permadeath 环境能显著提升竞争力但不是 Must-Fix。\n\n**SF2** [warning, R1-N2 提出, R2 rebut 降级] **Cluster bootstrap K=11 推断可靠性**\n\nR1 列为 Critical。R2 rebut：(1) 四种并行方法均 p<0.001，方向 robust；(2) exact permutation p=0.002 不依赖渐近近似；(3) 核心发现是描述性统计量，bootstrap 仅提供 uncertainty quantification。\n\n**Director 裁决**：维持 Warning。R2 的 rebuttal 有力。建议正文以 non-clustered bootstrap 为主要推断，cluster bootstrap 标注为 conservative sensitivity check。\n\n**SF3** [warning, R2-W2, R1 agree] **Non-triviality 论证不足**\n\n§5 \"Non-triviality of death dominance\" 段的论证（resistance to intervention → non-trivial）不充分。Hallucination-induced death 是 hard problem 在 LLM agent 文献中已有共识。更有效的论证应从 routing 文献 prior assumptions 出发——现有工作假设 signal 来自 capability/quality difference，本文揭示在 interactive environments 中不成立。\n\n**SF4** [warning, R1-W1] **Signal concentration + 63% task exclusion 的 scope limitation**\n\nSCI=0.21，信号集中在少数 tasks。63% 被排除 tasks 的 ΔDR=+38.2pp 支持非 cherry-picking，但排除率仍构成 scope limitation。R2 rebut：排除标准是 methodological，所有 death-prone tasks 100% death dominance。应在正文明确讨论。\n\n**SF5** [warning, R1-W3, R2 部分 agree] **Router 实验 confounds**\n\n(a) Step→episode gap 可能来自 compounding errors 而非 binary signal；(b) train/val split 方式需在主文明确（Appendix J 已报告 episode-level split 排除 leakage，但主文不清晰）。\n\n**SF6** [warning, R1-W4, R2 agree] **Agent improvement 实验统计功效不足**\n\nReflexion N=5 × 10 tasks = 50 data points，Figure 3 error bars 严重重叠。Retry n=200 与 Reflexion N=5 compute budget 不对等，论文未报告 per-intervention compute cost。\n\n**SF7** [warning, R2-W3, R1 agree] **Safe RL 相关工作覆盖偏薄**\n\n§4 safe RL 段落仅一句话带过五篇引用。缺 irreversible action avoidance 形式化、safe exploration 文献。\n\n### Minor Issues\n\n- **m1** [info] Figure 2 caption 需添加 \"structural consequence of the DAF decomposition\" caveat [R1, R2 agree]\n- **m2** [info] \"modality\" 术语歧义——建议改用 \"computation mode\" 或 \"strategy\" [R1]\n- **m3** [info] Webb (2023) 引用年份需核实（可能是 2014 working paper vs 2023 正式发表）[R1, R2]\n- **m4** [info] Appendix 缺索引（17 个 appendices A-R）[R1]\n- **m5** [info] §3.1 \"54 sole-identified labels\" 首次出现未定义 [R2]\n- **m6** [info] Appendix N failure categories 基于 manual inspection，缺 inter-annotator agreement [R2]\n- **m7** [info] 100% deaths 来自同一 action pattern (focus on [object])——应讨论 signal trivially binary 的 implication [R2]\n\n---\n\n## Reviewer Consensus\n\n1. **DAF framing 需修正** [R1-N1 = R2-N1]：DAF=90.4% 是 P=100 的数学产物，78.9% penalty-independent label fraction 应为主指标。\n2. **Episode→step gap 需正式讨论** [R1-N3 ≈ R2-N3]：框架的 episode-level 定位与 step-level routing 需求之间的鸿沟需在 Method 部分讨论。\n3. **Non-triviality 论证需加强** [R2-W2, R1 agree]：当前论证不足以化解 obvious-in-hindsight 风险。\n4. **Safe RL 覆盖需扩展** [R2-W3, R1 agree]。\n5. **Figure 2 caption 需 caveat** [R2-W5, R1 agree]。\n6. **统计方法论值得肯定** [R1-S2, R2-S2]：四种并行推断方法在 NLP 经验研究中属上乘。\n7. **形式化贡献清晰** [R1-S1, R2-S1]：Algorithm 1 和 DAF 分解可直接复用。\n\n---\n\n## Reviewer Divergence\n\n| 分歧点 | R1 | R2 | Director 裁决 |\n|--------|-----|-----|--------------|\n| Cluster bootstrap K=11 严重程度 | Critical | Warning — 四种方法均 p<0.001 | **Warning** — R2 论据更充分 |\n| Generalizability 严重程度 | Should-Fix | Critical — 需 permadeath replication | **Should-Fix** — 标题已限定 scope |\n| Abstract 数字密度 | Rebut（数字是证据） | Warning — 8+ 数字过多 | **不列入正式 weakness** |\n| Cross-model 主文表格 | Rebut（appendix 标准做法） | Warning | **Minor** — 可选添加 2-row summary |\n| Router practical value | Warning — 未转化为改进 | Rebut — diagnostic 定位明确 | **分歧保留** — 双方各有道理 |\n\n---\n\n## Questions for Authors\n\n1. DAF 在 P=10、P=1 时分别降至多少？78.9% label fraction 在 P=0 时如何变化？\n2. 27.7% mislabeled episodes 中，step-level 实际错误比例是多少？分布在哪些 task types？\n3. 如果在 task-type level 训练 lookup table（而非 step-level router），balanced accuracy 是多少？\n4. Step budget 从 30 增加到 50/100 时，被排除的 19 个 tasks 是否产生有效 routing signal？\n5. Oracle routing 上随机翻转 x% 决策的 episode-level 退化曲线如何？\n\n---\n\n## Missing References\n\n1. **Moldovan & Abbeel (2012)** \"Safe Exploration in Markov Decision Processes\" — irreversible/catastrophic states 形式化 [R2, R1 agree]\n2. **Ruan et al. (2024)** LLM agent failure taxonomy [R2]\n3. **Graves (2016)** \"Adaptive Computation Time for RNNs\" — adaptive routing 经典前身 [R2]\n4. 近期 LLM agent catastrophic action prevention 工作 [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，跳过。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已派发但**超时**（elapsed: 655s）。无排版质量评估可用。\n\n格式合规由 Reviewer 手动检查：\n- ✅ 正文 ≤ 8 页\n- ✅ `\\usepackage[review]{acl}` double-blind\n- ✅ Author \"Anonymous\"，无身份泄露\n- ✅ Limitations section 存在且充分\n- ✅ Ethics Statement 存在\n- ✅ Responsible NLP Checklist 完整\n- ✅ 引用格式一致（ACL natbib），46 条引用，无虚假引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings（可被 Findings 接收）**\n\n| 维度 | R1 | R2 | 加权判断 |\n|------|-----|-----|---------|\n| Soundness | 3/5 | 3.5/5 | 3.5/5 — R2 对统计方法论的肯定更准确 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 — obvious-in-hindsight 风险实质存在 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**理由**：\n\n1. **方法论价值确认**：Counterfactual diagnostic framework 设计严谨，形式化清晰，统计处理在 NLP 经验研究中属上乘。78.9% penalty-independent label fraction 是一个干净的经验发现。这些优点支撑 Findings 接收。\n\n2. **Framing 问题严重**：DAF=90.4% 作为标题级叙事锚点，但其数值主要由 P=100 的惩罚结构决定，是数学产物而非独立经验发现。这构成 framing 与证据之间的系统性张力，是阻碍 Conference 接收的核心问题。\n\n3. **Novelty 风险**：R1 Excitement 3/5, R2 Excitement 2.5/5。\"避免死亡比优化 score 更重要\"在直觉上并不令人惊讶。论文的价值更多在 quantification 和 methodology 而非 finding 本身，但 non-triviality 论证不足以充分化解这一风险。\n\n4. **Scope 受限**：完整分析仅在 ScienceWorld（11/30 tasks）上完成。跨环境 probes（MATH, ALFWorld）深度有限。MiniHack pilot 结果为 negative（项目实验记录），进一步限制了 generalizability 证据。\n\n5. **Episode→step gap**：框架的 diagnostic 输出无法直接指导 step-level routing 设计（router ≈ chance），实际 actionability 有限。\n\n**提升至 3.5（Borderline Conference）的明确路径**：\n1. 修正 DAF framing（以 78.9% 为核心，DAF 降级为 P-dependent 辅助指标）\n2. 补充第二个 permadeath 环境的完整 DAF 分解（或至少 ALFWorld 完整定量）\n3. 加强 non-triviality 论证（从 routing 文献 prior assumptions 出发）\n4. 明确框架的 episode-level diagnostic 定位和适用边界\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 核心叙事 reframe：从 \"death avoidance dominates routing signal\" 转向 \"death dominance resists standard interventions\"，突出 intervention robustness 的非先验可预测性 [SF3]\n\n### §2 Method\n- §2 末尾增加 episode-level vs step-level granularity gap 的正式讨论 [MF2]\n- 说明 97.4% step-level tie rate 为 episode-level 方法提供的合理性辩护 [MF2]\n- \"modality\" 考虑改为 \"computation mode\" 或 \"strategy\" [m2]\n\n### §3 Experiments\n- §3.1: 以 78.9% 为主指标，DAF 降级；呈现 DAF vs P 敏感性曲线 [MF1]\n- §3.2: 可选添加 Qwen vs Llama 2-row summary inline 对比 [minor]\n- §3.3: Agent improvement 实验增加 paired test 或报告 minimum detectable effect size [SF6]\n- §3.4: ALFWorld 需完整 DAF 定量分解 [SF1]\n- §3.6: 主文明确 train/val 是 episode-level split [SF5]\n\n### §4 Related Work\n- Safe RL 段落扩展至 3-5 句，补充 Moldovan & Abbeel 2012 等 [SF7]\n\n### §5 Discussion\n- \"Non-triviality\" 段从 routing 文献 prior assumptions 出发重写 [SF3]\n- \"Anatomy of catastrophic failure\" 讨论 single action pattern 的 implication [m7]\n\n### Figures/Tables\n- Figure 2 caption 添加 structural consequence caveat [m1]\n\n### References\n- 核实 Webb (2023) 年份 [m3]\n- 补充 Moldovan & Abbeel 2012, Ruan et al. 2024, Graves 2016 [SF7]\n\n### 引用验证\n46 条 bib 条目：36 verified, 6 minor mismatch (author encoding), 4 not_found (OpenAlex 索引延迟), 0 orphan, 0 missing, 0 fake。整体引用质量良好。",
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
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
    "report": "# Round 18 审稿报告 — simgate-modular-routing\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual 诊断框架，分析模块化 LLM agent 中 routing signal 的组成。在 ScienceWorld 上（245 episodes, 11/30 task types, Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 来自 death asymmetry（internal strategy 的 hallucination 触发 catastrophic death，deterministic strategy 存活），DAF=90.4%。框架在 MATH（null check, p=0.81）和 ALFWorld（识别 information asymmetry 替代机制）做了跨环境探测，在 Llama-3.1-8B 做了跨模型复现（10/10 directional consistency）。四类干预（retry/Reflexion/10× scaling/action filtering）均未消除 death dominance。Router 训练作为 diagnostic probe 显示 step-level routing signal 不可学习（balanced accuracy 54.1±5.4% ≈ chance）。\n\n---\n\n## Strengths\n\n**S1. 形式化贡献扎实** [R1, R2 共识]\nCounterfactual labeling function（Algorithm 1）和 DAF 分解（Eq. 4-5）定义清晰，框架可复用于任何有 binary fatal outcome 的环境。\n\n**S2. 统计方法论严谨** [R1, R2 共识]\n四种并行推断方法（standard cluster-robust, wild cluster bootstrap, exact permutation, non-clustered bootstrap），SCI 量化 signal 集中度，leave-one-task-out 验证。在 NLP 经验研究中属上乘水准。\n\n**S3. 多维度验证体系** [R1, R2 共识]\n跨模型（Llama 3.1-8B, 10/10 directional consistency）、跨环境（MATH null check, ALFWorld qualitative）、四类干预、per-seed breakdown、labeling quality audit。覆盖面远超一般 agent 论文。\n\n**S4. 78.9% penalty-independent label fraction 是干净的经验发现** [R1, R2 共识]\n该数字不依赖 death penalty P 的大小，是论文最有说服力的定量结论。\n\n**S5. 诚实的自我批判** [R1, R2 共识]\n论文主动报告 DAF 的 P-dependence、K=11 limitation、27.7% mislabeling rate。Practitioner Decision Framework（Appendix R）提供实操指导。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, R1-N1 + R2-N1, 强共识] **DAF 指标在高惩罚下近乎 tautological，核心 framing 有误导性**\n\nDAF = δP/(δP + Δ_nd) 在 P=100 时数学上必然趋近 1。论文自己承认这是 \"a mathematical consequence\"（§3.1, §5），但 title 和 abstract 仍以 DAF=90.4% 为核心叙事。Penalty-independent label fraction 78.9% 是更 honest 的指标但被置于次要位置。\n\n**Director 裁决**：必须修改。以 78.9% 为主指标，DAF 降级为 P-dependent 辅助指标。正文需呈现 DAF vs P 敏感性曲线（Appendix K 数据已有）。标题和 abstract 不应以 DAF 数值为叙事锚点。\n\n**MF2** [critical, R1-N3 + R2-N3, 强共识] **Episode-level 到 step-level 的 granularity gap 削弱框架实用性**\n\n论文定义 routing signal 为 episode-level pure-strategy performance gap，但实际 routing 发生在 step level。Router 训练（step-level balanced accuracy 54.1±5.4% ≈ chance）暴露了这一断层。27.7% 的 episode-level 标签在 step-level 上不一致，且集中在 death-asymmetry episodes。\n\nR2 补充：论文应明确声明框架是 episode-level 诊断工具（回答\"是否值得建 router\"），不是 step-level 训练信号来源。R1 进一步指出应分析 mislabeling 对 router 训练的具体影响。97.4% step-level tie rate 为 episode-level 方法提供了合理辩护，但需要在 Method 部分而非仅 Limitations 中说明。\n\n**Director 裁决**：必须在 §2 末尾或 §3.6 增加正式讨论，明确框架适用边界。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, R2-N2 提出, R1 rebut 降级] **跨环境 generalizability 证据不足**\n\nR2 列为 Must-Fix（需 permadeath 环境完整 DAF 分解或标题加限定）。R1 rebut：标题已含 \"on ScienceWorld\" 限定，generality claim 是方法论层面非经验层面，Discussion 对未测试环境是 future work 指向。\n\n**Director 裁决**：维持 Should-Fix。R1 rebuttal 成立——标题已限定 scope。但 ALFWorld 应提供完整 DAF 定量分解（当前仅 Figure 4 标签分布，缺 DAF 数值）。补充第二个 permadeath 环境能显著提升竞争力但不是 Must-Fix。\n\n**SF2** [warning, R1-N2 提出, R2 rebut 降级] **Cluster bootstrap K=11 推断可靠性**\n\nR1 列为 Critical。R2 rebut：(1) 四种并行方法均 p<0.001，方向 robust；(2) exact permutation p=0.002 不依赖渐近近似；(3) 核心发现是描述性统计量，bootstrap 仅提供 uncertainty quantification。\n\n**Director 裁决**：维持 Warning。R2 的 rebuttal 有力。建议正文以 non-clustered bootstrap 为主要推断，cluster bootstrap 标注为 conservative sensitivity check。\n\n**SF3** [warning, R2-W2, R1 agree] **Non-triviality 论证不足**\n\n§5 \"Non-triviality of death dominance\" 段的论证（resistance to intervention → non-trivial）不充分。Hallucination-induced death 是 hard problem 在 LLM agent 文献中已有共识。更有效的论证应从 routing 文献 prior assumptions 出发——现有工作假设 signal 来自 capability/quality difference，本文揭示在 interactive environments 中不成立。\n\n**SF4** [warning, R1-W1] **Signal concentration + 63% task exclusion 的 scope limitation**\n\nSCI=0.21，信号集中在少数 tasks。63% 被排除 tasks 的 ΔDR=+38.2pp 支持非 cherry-picking，但排除率仍构成 scope limitation。R2 rebut：排除标准是 methodological，所有 death-prone tasks 100% death dominance。应在正文明确讨论。\n\n**SF5** [warning, R1-W3, R2 部分 agree] **Router 实验 confounds**\n\n(a) Step→episode gap 可能来自 compounding errors 而非 binary signal；(b) train/val split 方式需在主文明确（Appendix J 已报告 episode-level split 排除 leakage，但主文不清晰）。\n\n**SF6** [warning, R1-W4, R2 agree] **Agent improvement 实验统计功效不足**\n\nReflexion N=5 × 10 tasks = 50 data points，Figure 3 error bars 严重重叠。Retry n=200 与 Reflexion N=5 compute budget 不对等，论文未报告 per-intervention compute cost。\n\n**SF7** [warning, R2-W3, R1 agree] **Safe RL 相关工作覆盖偏薄**\n\n§4 safe RL 段落仅一句话带过五篇引用。缺 irreversible action avoidance 形式化、safe exploration 文献。\n\n### Minor Issues\n\n- **m1** [info] Figure 2 caption 需添加 \"structural consequence of the DAF decomposition\" caveat [R1, R2 agree]\n- **m2** [info] \"modality\" 术语歧义——建议改用 \"computation mode\" 或 \"strategy\" [R1]\n- **m3** [info] Webb (2023) 引用年份需核实（可能是 2014 working paper vs 2023 正式发表）[R1, R2]\n- **m4** [info] Appendix 缺索引（17 个 appendices A-R）[R1]\n- **m5** [info] §3.1 \"54 sole-identified labels\" 首次出现未定义 [R2]\n- **m6** [info] Appendix N failure categories 基于 manual inspection，缺 inter-annotator agreement [R2]\n- **m7** [info] 100% deaths 来自同一 action pattern (focus on [object])——应讨论 signal trivially binary 的 implication [R2]\n\n---\n\n## Reviewer Consensus\n\n1. **DAF framing 需修正** [R1-N1 = R2-N1]：DAF=90.4% 是 P=100 的数学产物，78.9% penalty-independent label fraction 应为主指标。\n2. **Episode→step gap 需正式讨论** [R1-N3 ≈ R2-N3]：框架的 episode-level 定位与 step-level routing 需求之间的鸿沟需在 Method 部分讨论。\n3. **Non-triviality 论证需加强** [R2-W2, R1 agree]：当前论证不足以化解 obvious-in-hindsight 风险。\n4. **Safe RL 覆盖需扩展** [R2-W3, R1 agree]。\n5. **Figure 2 caption 需 caveat** [R2-W5, R1 agree]。\n6. **统计方法论值得肯定** [R1-S2, R2-S2]：四种并行推断方法在 NLP 经验研究中属上乘。\n7. **形式化贡献清晰** [R1-S1, R2-S1]：Algorithm 1 和 DAF 分解可直接复用。\n\n---\n\n## Reviewer Divergence\n\n| 分歧点 | R1 | R2 | Director 裁决 |\n|--------|-----|-----|--------------|\n| Cluster bootstrap K=11 严重程度 | Critical | Warning — 四种方法均 p<0.001 | **Warning** — R2 论据更充分 |\n| Generalizability 严重程度 | Should-Fix | Critical — 需 permadeath replication | **Should-Fix** — 标题已限定 scope |\n| Abstract 数字密度 | Rebut（数字是证据） | Warning — 8+ 数字过多 | **不列入正式 weakness** |\n| Cross-model 主文表格 | Rebut（appendix 标准做法） | Warning | **Minor** — 可选添加 2-row summary |\n| Router practical value | Warning — 未转化为改进 | Rebut — diagnostic 定位明确 | **分歧保留** — 双方各有道理 |\n\n---\n\n## Questions for Authors\n\n1. DAF 在 P=10、P=1 时分别降至多少？78.9% label fraction 在 P=0 时如何变化？\n2. 27.7% mislabeled episodes 中，step-level 实际错误比例是多少？分布在哪些 task types？\n3. 如果在 task-type level 训练 lookup table（而非 step-level router），balanced accuracy 是多少？\n4. Step budget 从 30 增加到 50/100 时，被排除的 19 个 tasks 是否产生有效 routing signal？\n5. Oracle routing 上随机翻转 x% 决策的 episode-level 退化曲线如何？\n\n---\n\n## Missing References\n\n1. **Moldovan & Abbeel (2012)** \"Safe Exploration in Markov Decision Processes\" — irreversible/catastrophic states 形式化 [R2, R1 agree]\n2. **Ruan et al. (2024)** LLM agent failure taxonomy [R2]\n3. **Graves (2016)** \"Adaptive Computation Time for RNNs\" — adaptive routing 经典前身 [R2]\n4. 近期 LLM agent catastrophic action prevention 工作 [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，跳过。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已派发但**超时**（elapsed: 655s）。无排版质量评估可用。\n\n格式合规由 Reviewer 手动检查：\n- ✅ 正文 ≤ 8 页\n- ✅ `\\usepackage[review]{acl}` double-blind\n- ✅ Author \"Anonymous\"，无身份泄露\n- ✅ Limitations section 存在且充分\n- ✅ Ethics Statement 存在\n- ✅ Responsible NLP Checklist 完整\n- ✅ 引用格式一致（ACL natbib），46 条引用，无虚假引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings（可被 Findings 接收）**\n\n| 维度 | R1 | R2 | 加权判断 |\n|------|-----|-----|---------|\n| Soundness | 3/5 | 3.5/5 | 3.5/5 — R2 对统计方法论的肯定更准确 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 — obvious-in-hindsight 风险实质存在 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**理由**：\n\n1. **方法论价值确认**：Counterfactual diagnostic framework 设计严谨，形式化清晰，统计处理在 NLP 经验研究中属上乘。78.9% penalty-independent label fraction 是一个干净的经验发现。这些优点支撑 Findings 接收。\n\n2. **Framing 问题严重**：DAF=90.4% 作为标题级叙事锚点，但其数值主要由 P=100 的惩罚结构决定，是数学产物而非独立经验发现。这构成 framing 与证据之间的系统性张力，是阻碍 Conference 接收的核心问题。\n\n3. **Novelty 风险**：R1 Excitement 3/5, R2 Excitement 2.5/5。\"避免死亡比优化 score 更重要\"在直觉上并不令人惊讶。论文的价值更多在 quantification 和 methodology 而非 finding 本身，但 non-triviality 论证不足以充分化解这一风险。\n\n4. **Scope 受限**：完整分析仅在 ScienceWorld（11/30 tasks）上完成。跨环境 probes（MATH, ALFWorld）深度有限。MiniHack pilot 结果为 negative（项目实验记录），进一步限制了 generalizability 证据。\n\n5. **Episode→step gap**：框架的 diagnostic 输出无法直接指导 step-level routing 设计（router ≈ chance），实际 actionability 有限。\n\n**提升至 3.5（Borderline Conference）的明确路径**：\n1. 修正 DAF framing（以 78.9% 为核心，DAF 降级为 P-dependent 辅助指标）\n2. 补充第二个 permadeath 环境的完整 DAF 分解（或至少 ALFWorld 完整定量）\n3. 加强 non-triviality 论证（从 routing 文献 prior assumptions 出发）\n4. 明确框架的 episode-level diagnostic 定位和适用边界\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 核心叙事 reframe：从 \"death avoidance dominates routing signal\" 转向 \"death dominance resists standard interventions\"，突出 intervention robustness 的非先验可预测性 [SF3]\n\n### §2 Method\n- §2 末尾增加 episode-level vs step-level granularity gap 的正式讨论 [MF2]\n- 说明 97.4% step-level tie rate 为 episode-level 方法提供的合理性辩护 [MF2]\n- \"modality\" 考虑改为 \"computation mode\" 或 \"strategy\" [m2]\n\n### §3 Experiments\n- §3.1: 以 78.9% 为主指标，DAF 降级；呈现 DAF vs P 敏感性曲线 [MF1]\n- §3.2: 可选添加 Qwen vs Llama 2-row summary inline 对比 [minor]\n- §3.3: Agent improvement 实验增加 paired test 或报告 minimum detectable effect size [SF6]\n- §3.4: ALFWorld 需完整 DAF 定量分解 [SF1]\n- §3.6: 主文明确 train/val 是 episode-level split [SF5]\n\n### §4 Related Work\n- Safe RL 段落扩展至 3-5 句，补充 Moldovan & Abbeel 2012 等 [SF7]\n\n### §5 Discussion\n- \"Non-triviality\" 段从 routing 文献 prior assumptions 出发重写 [SF3]\n- \"Anatomy of catastrophic failure\" 讨论 single action pattern 的 implication [m7]\n\n### Figures/Tables\n- Figure 2 caption 添加 structural consequence caveat [m1]\n\n### References\n- 核实 Webb (2023) 年份 [m3]\n- 补充 Moldovan & Abbeel 2012, Ruan et al. 2024, Graves 2016 [SF7]\n\n### 引用验证\n46 条 bib 条目：36 verified, 6 minor mismatch (author encoding), 4 not_found (OpenAlex 索引延迟), 0 orphan, 0 missing, 0 fake。整体引用质量良好。",
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
  }
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-19T15:00:35.402084+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4014
}
```

</details>

---


### Assistant

_source line 1652 · 2026-05-19T15:00:43.276510+00:00_

**Round 18 审稿完成。**

报告已投递至 Research Director。

**审稿结论：Overall 3.0 — Findings**

核心发现：
- **2 个 Must-Fix**：(1) DAF=90.4% 是 P=100 的数学产物，需以 78.9% label fraction 为主指标；(2) Episode→step granularity gap 需在 Method 中正式讨论框架适用边界
- **7 个 Should-Fix**：跨环境验证深度不足、non-triviality 论证弱、K=11 统计局限、signal concentration、router confounds、agent improvement 统计功效、safe RL 覆盖薄
- **提升路径明确**：修正 DAF framing + 补充跨环境完整定量 + 加强 novelty 论证 → 可达 3.5 Borderline Conference

Issue Tracker 已同步更新至 `review_issues.yaml`（Round 18）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 140

## Round 140

2 recorded events


### User

_source line 1653 · 2026-05-19T15:00:44.788456+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 8 个问题：

- **AGREE** 5 个：N1（DAF misleading）、N3（episode→step gap）、W2（non-triviality 论证弱）、W3（safe RL 覆盖薄）、W5（Figure 2 过度解读）
- **REBUT** 3 个：N2（generalizability 不应为 Must-Fix，标题已含"on ScienceWorld"限定，框架 generality claim 是方法论层面的）、W1（abstract 数字密度合理，empirical paper 需要数字支撑 claim）、W4（跨模型数据在主文已有关键数值，完整表在 Appendix M 符合页数限制下的标准做法）

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

_source line 1654 · 2026-05-19T15:00:54.216580+00:00_

审稿报告已成功投递至 Research Director。

**Round 18 审稿总结：**

- **Overall Score: 3.0 — Findings**
- **2 个 Must-Fix**：DAF framing 误导性（P-dependent 指标作为标题级发现）、episode→step granularity gap 未正式讨论
- **7 个 Should-Fix**：跨环境验证不足、K=11 cluster bootstrap、non-triviality 论证弱、signal concentration、router confounds、agent improvement 统计功效、safe RL 覆盖
- **7 个 Minor**：Figure 2 caption、术语歧义、引用年份等

两位 Reviewer 在 DAF framing 和 episode→step gap 上强共识；在 cluster bootstrap 严重程度和 generalizability 级别上有分歧（均已裁决）。Issue Tracker 已同步更新至 Round 18。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 141

## Round 141

66 recorded events


### User

_source line 1655 · 2026-05-19T15:41:16.461407+00:00_

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

_source line 1656 · 2026-05-19T15:41:24.146006+00:00_

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

_source line 1657 · 2026-05-19T15:41:24.146901+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-19T15:41:33.832710+00:00_

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

_source line 1659 · 2026-05-19T15:41:33.933572+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1660 · 2026-05-19T15:41:37.080004+00:00_

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

_source line 1661 · 2026-05-19T15:41:37.532212+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (111 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **minihack-cross-env-pilot** (negative): In MiniHack permadeath navigation environments, episode-level counterfactual analysis will reveal death dominance (internal DR significantly > deterministic DR), validating the diagnostic framework's cross-environment applicability beyond ScienceWorld. This tests whether death avoidance as the dominant routing signal is a general phenomenon of LLM agents in irreversible-failure environments, not an artifact of ScienceWorld's specific task design. ← 基于 plan-012-full\n- **backbone-scaling-70b** (success): 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 ← 基于 backbone-scaling-death-rate-0.5b\n  [72B DAF Decomposition Analysis](/api/workspace-files/projects/simgate-modular-routing/artifacts/backbone-scaling-70b/report/72b_daf_decomposition.md)\n- **llama-cross-model-full** (success): Death dominance mechanism (DAF ~78.9% on Qwen-7B) generalizes across model families: Llama-3.1-8B-Instruct on the same 11 ScienceWorld tasks will show (1) DAF direction consistent with Qwen, (2) similar death-prone vs non-death-prone task pattern, and (3) high per-task death ra
…[truncated 1667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1662 · 2026-05-19T15:41:37.532590+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
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
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1663 · 2026-05-19T15:41:37.583060+00:00_



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

_source line 1664 · 2026-05-19T15:41:45.377366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "80"
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
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1665 · 2026-05-19T15:41:46.432080+00:00_

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
…[truncated 4693 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1666 · 2026-05-19T15:41:46.432631+00:00_

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

_source line 1667 · 2026-05-19T15:41:46.985161+00:00_

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


### Tool call

_source line 1668 · 2026-05-19T15:41:47.537693+00:00_

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

_source line 1669 · 2026-05-19T15:42:03.962983+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found search results related to EMNLP 2026, though the results primarily show information about tutorials and workshops co-lo
…[truncated 3585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 17530
}
```

</details>

---


### Tool result

_source line 1670 · 2026-05-19T15:42:03.963438+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 16978
}
```

</details>

---


### Tool result

_source line 1671 · 2026-05-19T15:42:03.963603+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 16425
}
```

</details>

---


### Tool call

_source line 1672 · 2026-05-19T15:42:10.600927+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit anonymity policy ARR 2026"
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
    "query": "EMNLP 2026 submission format page limit anonymity policy ARR 2026"
  }
}
```

</details>

---


### Tool call

_source line 1673 · 2026-05-19T15:42:11.303927+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml"
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
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool call

_source line 1674 · 2026-05-19T15:42:15.384183+00:00_

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


### Tool call

_source line 1675 · 2026-05-19T15:42:15.685659+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | head -100",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | head -100",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1676 · 2026-05-19T15:42:18.954721+00:00_

Web search results for query: "EMNLP 2026 submission format page limit anonymity policy ARR 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"}]

Based on the search results, here is information about EMNLP 2026 submission format, page limits, anonymity policy, and ARR 2026:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Additionally, the mandatory Limitations section is required, placed after the conclusion.

## Anonymity Policy

Following the ACL and ARR policies, there is no anonymity period requirement. However, there is no anonymity period or limitation on posting or discussin
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 8353
}
```

</details>

---


### Tool result

_source line 1677 · 2026-05-19T15:42:19.006124+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 126\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinis
…[truncated 10983 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7702
}
```

</details>

---


### Tool result

_source line 1678 · 2026-05-19T15:42:19.250049+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 3564
}
```

</details>

---


### Tool result

_source line 1679 · 2026-05-19T15:42:19.250540+00:00_

-rw-r--r-- 1 ubuntu ubuntu 574779 May 19 15:41 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 3866
}
```

</details>

---


### Tool call

_source line 1680 · 2026-05-19T15:42:23.712569+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10",
  "description": "Find agent config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10",
    "description": "Find agent config files"
  }
}
```

</details>

---


### Tool result

_source line 1681 · 2026-05-19T15:42:24.415900+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 1682 · 2026-05-19T15:42:24.416446+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ARR 2026\" \"author guidelines\" page limit template double-blind long paper short paper format"
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
    "query": "\"ARR 2026\" \"author guidelines\" page limit template double-blind long paper short paper format"
  }
}
```

</details>

---


### Tool result

_source line 1683 · 2026-05-19T15:42:31.550464+00:00_

Web search results for query: ""ARR 2026" "author guidelines" page limit template double-blind long paper short paper format"

Links: [{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Frequently Asked Questions for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/faq/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results for ARR 2026 author guidelines, here's what I found:

## Page Limits

The submission requirements are the same as first-round review (4-page limit for short papers, 8 pages for long papers).

## Template and Format

Paper submissions must use the official ACL style template, and authors should follow the paper formatting guidelines general to "*ACL" conferences. The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template.

## Double-Blind Review

Regarding anonymity, a paper can only be (re)submitted to ARR if it has been anonymous for at least a month before the first submission, and it must remain anonymous while it is under review. Authors may allow their anonymized submission to be publicly av
…[truncated 542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 7134
}
```

</details>

---


### Tool call

_source line 1684 · 2026-05-19T15:42:35.977870+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 3 -name \"config.yaml\" -o -name \"project.yaml\" 2>/dev/null | head -10",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 3 -name \"config.yaml\" -o -name \"project.yaml\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1685 · 2026-05-19T15:42:36.279750+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1686 · 2026-05-19T15:42:36.280190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "80"
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
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1687 · 2026-05-19T15:42:36.330758+00:00_

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
…[truncated 4693 chars]

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

_source line 1688 · 2026-05-19T15:42:43.164646+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex 2>/dev/null",
  "description": "List all tex files in paper directory"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex 2>/dev/null",
    "description": "List all tex files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 1689 · 2026-05-19T15:42:44.118476+00:00_

-rw-r--r-- 1 ubuntu ubuntu  1094 May 19 11:41 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
-rw-r--r-- 1 ubuntu ubuntu   290 May 19 15:41 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu  3912 May 19 15:42 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
-rw-r--r-- 1 ubuntu ubuntu 14252 May 19 15:41 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  5907 May 19 15:23 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
-rw-r--r-- 1 ubuntu ubuntu 50752 May 19 15:40 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
-rw-r--r-- 1 ubuntu ubuntu  8348 May 19 15:40 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
-rw-r--r-- 1 ubuntu ubuntu  4575 May 19 15:36 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  5500 May 18 03:50 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1690 · 2026-05-19T15:42:44.420046+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
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
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1691 · 2026-05-19T15:42:44.571253+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Tue May 19 15:42:42 2026 UTC
ModDate:         Tue May 19 15:42:42 2026 UTC
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
File size:       574680 bytes
Optimized:       no
PDF version:     1.7

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

_source line 1692 · 2026-05-19T15:42:50.444923+00:00_

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

_source line 1693 · 2026-05-19T15:42:50.846919+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \emph{what} drives routing decisions. We introduce an episode-level counterfactual framework that decomposes routing signal into death-avoidance and non-death components. Applied to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), \textbf{78.9\% of non-tie routing labels} arise from death asymmetry: the internal strategy's hallucination-induced failures trigger catastrophic agent death, while the deterministic strategy survives. This death dominance resists four representative intervention axes spanning retry, self-correction, $10{\times}$ parameter scaling, and action-space restriction; all reduce death rates yet none closes the gap to deterministic safety. A MATH evaluation ($N{=}795$, $p = 0.81$) confirms no routing signal without catastrophic failure. The framework reveals when catastrophic failure makes routing degenerate and when learned routers may add value.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1694 · 2026-05-19T15:42:50.847438+00:00_

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

_source line 1695 · 2026-05-19T15:42:51.399737+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	Concurrent analyses of when and whether to invoke tools~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026} further presuppose diverse routing signals.
10	The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.
11	But no prior work has systematically decomposed what drives routing decisions in interactive environments. Without such a decomposition, the field cannot distinguish settings where diverse routing signals justify learned routers from tho
…[truncated 3985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1696 · 2026-05-19T15:42:51.400160+00:00_

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

_source line 1697 · 2026-05-19T15:42:51.852194+00:00_

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
14	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld
…[truncated 6558 chars]

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

_source line 1698 · 2026-05-19T15:42:51.852585+00:00_

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

_source line 1699 · 2026-05-19T15:42:52.404946+00:00_

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
11	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
12	\label{fig:decomposition}
13	\end{figure}
14	
15	Of 95 non-tie routing labels across 245 episodes, 75 (78.9\%) arise from death asymmetry: one strategy dies while the other survives. This label fraction is penalty-independent---it depends only on which episodes produce asymmetric deaths, not on how death is penalized. Of these 75, 54 are sole-signal labels (episodes where only one strategy produced a non-zero score): both strategies score zero without death, so death avoidance was the \emph{sole} discriminating signal. The remaining 21 death-asymmetry labels involve episodes where the surviving strategy also earned positive score. At $P{=}0$, the 54 sole-signal labels reduce to ties, leaving 41 non-tie labels of which 21 (51.2\%) still involve death asymmetry; the labeling function itself is penalty-independent (A
…[truncated 12596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1700 · 2026-05-19T15:42:52.405347+00:00_

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

_source line 1701 · 2026-05-19T15:42:52.807102+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	\emph{Self-supervised} approaches learn tool invocation from loss signals: Toolformer \cite{toolformer-2023} inserts API calls filtered by perplexity reduction; ToolACE \cite{toolace-2025} curates synthetic data for function-calling accuracy.
6	\emph{Token-level} methods embed tools into the model vocabulary: ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens resolved at inference.
7	\emph{Task-level} decomposition routes subtasks to specialized modules: ART \cite{art-2023} generates tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask.
8	\emph{RL-based} methods learn routing policies from reward: ReTool \cite{retool-2025} discovers when code execution is preferable to chain-of-thought.
9	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
10	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect where LLMs default to external tools even when internal knowledge suffices, finding that tool overuse correlates with model uncertainty rather than task difficulty. \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax,'' and \citet{to-call-or-not-2026} propose a necessity, utility, and affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, 78.9\% of routing labels trace to catastrophic-failure prevention.
11	
12	\paragraph{Adaptive Computation and Routing.}
13	Adaptive routing traces back to learned halting policies \citep{graves2016act}. In the LLM era, CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, AR
…[truncated 2644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1702 · 2026-05-19T15:42:52.807477+00:00_

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

_source line 1703 · 2026-05-19T15:42:53.209216+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. The 4B router improves at episode level ($59.0\%$) without step-level gains ($56$--$59\%$), confirming task-type classification; cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}).
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), three properties were not predictable a priori: (i)~\emph{routing prior}---the oracle matches always-deterministic on 96.3\% of decisions (2.89-point improvement), and threshold routing with perfect death risk knowledge still cannot outperform always-deterministic (Appendix~\ref{sec:threshold-routing}), so the rational prior is ``do not route''; (ii)~\emph{intervention resistance}---retry ($43.5\%$), Reflexion ($34.0\%$), $10{\times}$ scaling ($30.6\%$), and action-space filtering ($29.0\%$) all leave ${\geq}$12~pp residual gaps to deterministic safety ($16.3\%$), with Reflexion and scaling converging to overlapping Wilson CIs suggesting a shared bound from lacking ground-truth state access; (iii)~\emph{cross-model stability}---Qwen-7B and Llama-8B show nearly identical internal vulnerability (${\sim}$42\%), and 72B scaling leaves death dominance intact (DAF $= 92.4\%$). More aggressive interventions (Tree-of-Thought, process reward models) remain untested; we characterize a ceiling, not a universal bound.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (Appendix~\ref{app:failure-modes}). The root cause is g
…[truncated 1957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1704 · 2026-05-19T15:42:53.209589+00:00_

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

_source line 1705 · 2026-05-19T15:42:53.260026+00:00_

1	\section{Conclusion}
2	
3	We decomposed routing signal in modular LLM agents: in ScienceWorld, 78.9\% of non-tie labels arise from death asymmetry, confirmed across four intervention axes and two cross-domain probes. Future work should target intermediate death regimes and stronger backbones.
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

_source line 1706 · 2026-05-19T15:43:00.185802+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -name \"config.yaml\" -o -name \"config.json\" -o -name \"project_config*\" 2>/dev/null | head -20",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -name \"config.yaml\" -o -name \"config.json\" -o -name \"project_config*\" 2>/dev/null | head -20",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 1707 · 2026-05-19T15:43:01.641345+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 1708 · 2026-05-19T15:43:01.641802+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
    "description": "Check existing review issues"
  }
}
```

</details>

---


### Tool result

_source line 1709 · 2026-05-19T15:43:02.094266+00:00_

## Round 18 Review Issues (updated after R18 Action Matrix dispatch, 2026-05-19)

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
  resolution: "Limitations 和 Appendix B 已充分量化 27.7% mislabeling fraction"
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
  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld + MATH N 标注不一致"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 13
  last_seen_round: 16
  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
  resolution_round: 16

- id: "R13-m3"
  summary: "Reference 格式不统一 + orphan entries"
  category:
…[truncated 16724 chars]

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

_source line 1710 · 2026-05-19T15:43:02.245325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
  "pages": "1-8"
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
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 1711 · 2026-05-19T15:43:02.800160+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf (561.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 1712 · 2026-05-19T15:43:57.007249+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## 论文信息\n- **标题**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **Venue**: EMNLP 2026 (Long Paper via ARR)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，正文 ≤ 8 页，参考文献不限，Limitations 必须有（不计入页数），double-blind\n- **评分标准**: Overall Assessment: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 方法严谨性（重点）\n- **DAF 定义与解释**：DAF = δP/(δP + Δ_nd) 随 P 单调递增——论文是否充分说明这是数学后果而非经验发现？penalty-independent 的 78.9% label fraction 与 penalty-dependent 的 DAF 90.4% 是否区分清楚？\n- **Episode-level vs step-level gap**：97.4% step-level tie rate 下的 episode-level labeling 是否有充分方法论辩护？episode labels 投射到 step-level router 训练时，27.7% mislabeling 和 60.3% pre-event neutral 是否合理量化？\n- **统计推断**：cluster bootstrap K=11 的可靠性（Cameron et al. 2008 建议 K≥40）、Cohen's d=3.02 的报告方式、wild cluster bootstrap 的适用条件\n- **Counterfactual 设计**：pure-strategy trajectories 的外部效度——现实 routing 场景中 agent 不会全程使用单一模式，pure-strategy 设计是否高估了 death asymmetry 的实际影响？\n\n### 2. 实验设计\n- **Task selection bias**：11/30 task types（37% 覆盖率），63% 排除的合理性，anti-cherry-picking analysis 的可信度\n- **Cross-environment probes**：MATH（无 catastrophic failure → 无信号）和 ALFWorld（information asymmetry ≠ computation mode switch）——\"deterministic\" 在三个环境中含义不同，是否算真正的跨环境验证？\n- **Agent improvement baselines**：Retry/Reflexion/72B/action filtering 的实验规模和统计功效，N=5 trials 的 Reflexion dose-response 功效是否足够？\n- **Router 实验**：作为 diagnostic probe 的定位是否合理？0.6B-4B 三个 scale 的结果如何解读？step-level balanced accuracy 56-59% 接近 chance 但 episode-level 4B 有统计显著改善——这一 disconnect 的解释是否站得住？\n\n### 3. 格式合规检查\n- 正文是否严格 ≤ 8 页\n- Limitations 和 Ethics Statement 是否完整\n- 引用格式是否统一\n- 匿名性是否维持（无 self-citation 泄露）\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清)\n5. **Missing References**\n6. **Overall Assessment** (评分 + 置信度 1-5)\n7. **Detailed Comments** (按章节)"
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
    "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## 论文信息\n- **标题**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **Venue**: EMNLP 2026 (Long Paper via ARR)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，正文 ≤ 8 页，参考文献不限，Limitations 必须有（不计入页数），double-blind\n- **评分标准**: Overall Assessment: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 方法严谨性（重点）\n- **DAF 定义与解释**：DAF = δP/(δP + Δ_nd) 随 P 单调递增——论文是否充分说明这是数学后果而非经验发现？penalty-independent 的 78.9% label fraction 与 penalty-dependent 的 DAF 90.4% 是否区分清楚？\n- **Episode-level vs step-level gap**：97.4% step-level tie rate 下的 episode-level labeling 是否有充分方法论辩护？episode labels 投射到 step-level router 训练时，27.7% mislabeling 和 60.3% pre-event neutral 是否合理量化？\n- **统计推断**：cluster bootstrap K=11 的可靠性（Cameron et al. 2008 建议 K≥40）、Cohen's d=3.02 的报告方式、wild cluster bootstrap 的适用条件\n- **Counterfactual 设计**：pure-strategy trajectories 的外部效度——现实 routing 场景中 agent 不会全程使用单一模式，pure-strategy 设计是否高估了 death asymmetry 的实际影响？\n\n### 2. 实验设计\n- **Task selection bias**：11/30 task types（37% 覆盖率），63% 排除的合理性，anti-cherry-picking analysis 的可信度\n- **Cross-environment probes**：MATH（无 catastrophic failure → 无信号）和 ALFWorld（information asymmetry ≠ computation mode switch）——\"deterministic\" 在三个环境中含义不同，是否算真正的跨环境验证？\n- **Agent improvement baselines**：Retry/Reflexion/72B/action filtering 的实验规模和统计功效，N=5 trials 的 Reflexion dose-response 功效是否足够？\n- **Router 实验**：作为 diagnostic probe 的定位是否合理？0.6B-4B 三个 scale 的结果如何解读？step-level balanced accuracy 56-59% 接近 chance 但 episode-level 4B 有统计显著改善——这一 disconnect 的解释是否站得住？\n\n### 3. 格式合规检查\n- 正文是否严格 ≤ 8 页\n- Limitations 和 Ethics Statement 是否完整\n- 引用格式是否统一\n- 匿名性是否维持（无 self-citation 泄露）\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清)\n5. **Missing References**\n6. **Overall Assessment** (评分 + 置信度 1-5)\n7. **Detailed Comments** (按章节)"
  }
}
```

</details>

---


### Tool result

_source line 1713 · 2026-05-19T15:44:18.303902+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21296
}
```

</details>

---


### Tool call

_source line 1714 · 2026-05-19T15:44:18.506652+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## 论文信息\n- **标题**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **Venue**: EMNLP 2026 (Long Paper via ARR)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，正文 ≤ 8 页，参考文献不限，Limitations 必须有（不计入页数），double-blind\n- **评分标准**: Overall Assessment: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献（重点）\n- **核心发现的 novelty**：death avoidance dominates routing signal——这是否属于 obvious-in-hindsight？一个带 -100 death penalty 的环境中 death avoidance 成为主信号，是否在读到 setup 后就能预见？论文如何论证 non-triviality？\n- **方法论贡献**：episode-level counterfactual framework + DAF metric——是否足够构成 EMNLP long paper 级别的贡献？与 RL 中已有的 counterfactual evaluation 方法相比，novelty 在哪？\n- **Contribution 结构**：三个 contributions (framework, death dominance evidence, cross-environment probes) 是否均衡？哪个最强/最弱？\n- **Excitement level**：作为 EMNLP reviewer，这篇论文是否让你 excited？为什么？\n\n### 2. 完整性\n- **Related work 覆盖**：tool use, adaptive routing, counterfactual RL, safe RL, LLM agent environments——是否有重要遗漏？\n- **Ablation 完整性**：是否缺少关键 ablation（如不同 penalty 值下的系统实验、不同 backbone 的完整对比）？\n- **负面结果的处理**：router 训练失败（step-level ≈ chance）和 data augmentation 无效——这些 negative results 是否被诚实且有价值地呈现？\n- **Reproducibility**：实验细节是否足以复现？代码/数据 availability？\n\n### 3. 写作质量（重点）\n- **Abstract**：是否过于数字堆砌？信息密度与可读性的平衡？\n- **Introduction 叙事**：从 routing problem → existing gap → proposed framework → key finding 的逻辑链是否流畅？\n- **Framing 一致性**：paper 在 \"diagnostic framework\" 和 \"empirical finding\" 之间的定位是否清晰？标题聚焦 finding，但 contribution 1 是 framework——是否存在 framing tension？\n- **术语一致性**：如 \"modality\" 在 NLP 语境下是否有歧义？全文术语使用是否一致？\n- **Figure/Table 质量**：Figure 1 (pipeline), Figure 2 (scatter), Figure 3 (dose-response), Table 1, Table 2——是否清晰、自解释？caption 是否充分？\n- **Conclusion**：是否过于简短（仅 2 句）？\n- **Safe RL 段落**：Related Work 中的 Safe RL 讨论是否充分？\n\n### 4. 格式检查\n- 引用格式统一性\n- 未引用的 figure/table/appendix\n- Orphan bibliography entries\n- 匿名性\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清)\n5. **Missing References**\n6. **Overall Assessment** (评分 + 置信度 1-5)\n7. **Detailed Comments** (按章节)"
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
    "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## 论文信息\n- **标题**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **Venue**: EMNLP 2026 (Long Paper via ARR)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，正文 ≤ 8 页，参考文献不限，Limitations 必须有（不计入页数），double-blind\n- **评分标准**: Overall Assessment: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献（重点）\n- **核心发现的 novelty**：death avoidance dominates routing signal——这是否属于 obvious-in-hindsight？一个带 -100 death penalty 的环境中 death avoidance 成为主信号，是否在读到 setup 后就能预见？论文如何论证 non-triviality？\n- **方法论贡献**：episode-level counterfactual framework + DAF metric——是否足够构成 EMNLP long paper 级别的贡献？与 RL 中已有的 counterfactual evaluation 方法相比，novelty 在哪？\n- **Contribution 结构**：三个 contributions (framework, death dominance evidence, cross-environment probes) 是否均衡？哪个最强/最弱？\n- **Excitement level**：作为 EMNLP reviewer，这篇论文是否让你 excited？为什么？\n\n### 2. 完整性\n- **Related work 覆盖**：tool use, adaptive routing, counterfactual RL, safe RL, LLM agent environments——是否有重要遗漏？\n- **Ablation 完整性**：是否缺少关键 ablation（如不同 penalty 值下的系统实验、不同 backbone 的完整对比）？\n- **负面结果的处理**：router 训练失败（step-level ≈ chance）和 data augmentation 无效——这些 negative results 是否被诚实且有价值地呈现？\n- **Reproducibility**：实验细节是否足以复现？代码/数据 availability？\n\n### 3. 写作质量（重点）\n- **Abstract**：是否过于数字堆砌？信息密度与可读性的平衡？\n- **Introduction 叙事**：从 routing problem → existing gap → proposed framework → key finding 的逻辑链是否流畅？\n- **Framing 一致性**：paper 在 \"diagnostic framework\" 和 \"empirical finding\" 之间的定位是否清晰？标题聚焦 finding，但 contribution 1 是 framework——是否存在 framing tension？\n- **术语一致性**：如 \"modality\" 在 NLP 语境下是否有歧义？全文术语使用是否一致？\n- **Figure/Table 质量**：Figure 1 (pipeline), Figure 2 (scatter), Figure 3 (dose-response), Table 1, Table 2——是否清晰、自解释？caption 是否充分？\n- **Conclusion**：是否过于简短（仅 2 句）？\n- **Safe RL 段落**：Related Work 中的 Safe RL 讨论是否充分？\n\n### 4. 格式检查\n- 引用格式统一性\n- 未引用的 figure/table/appendix\n- Orphan bibliography entries\n- 匿名性\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清)\n5. **Missing References**\n6. **Overall Assessment** (评分 + 置信度 1-5)\n7. **Detailed Comments** (按章节)"
  }
}
```

</details>

---


### Tool result

_source line 1715 · 2026-05-19T15:44:20.226161+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1719
}
```

</details>

---


### Tool call

_source line 1716 · 2026-05-19T15:44:20.286710+00:00_

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


### Tool call

_source line 1717 · 2026-05-19T15:44:20.862716+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "simgate-modular-routing",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "simgate-modular-routing",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 1718 · 2026-05-19T15:44:21.938273+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1651
}
```

</details>

---


### Tool result

_source line 1719 · 2026-05-19T15:44:22.592186+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 1729
}
```

</details>

---


### Assistant

_source line 1720 · 2026-05-19T15:44:32.542943+00:00_

Round 1 已启动：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验设计） | ✅ 已派发 |
| Reviewer 2（新颖性 + 完整性 + 写作质量） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 已请求，8h 后自动提醒 |

等待 Reviewer 1 和 Reviewer 2 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1721 · 2026-05-19T15:49:58.468102+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Death Avoidance as the Dominant Routing Signal

## 1. Summary

本文提出一个 episode-level counterfactual diagnostic framework，用于分析 modular LLM agent 中 routing 决策的驱动因素。在 ScienceWorld 环境（11 task types, 245 episodes, Qwen2.5-7B-Instruct）上，将 routing signal 分解为 death-avoidance 和 non-death 两个成分，发现 78.9% 的 non-tie routing labels 源于 death asymmetry——即 internal reasoning strategy 因幻觉触发 catastrophic death（−100 penalty），而 deterministic strategy 存活。作者定义了 Death Avoidance Factor (DAF) 量化该比例，并在 MATH 和 ALFWorld 上做了 cross-environment probe。

## 2. Strengths

**S1. 方法论严谨，统计分析扎实。** Episode-level bootstrap resampling（B=10,000）、wild cluster bootstrap（Appendix E）、per-task confidence intervals（Appendix F）、8-seed robustness（Appendix J）——统计工具的选择和使用都达到高标准。特别是 cluster-robust inference 处理 task-type 内相关性（Cameron et al., 2008; Webb, 2023）是同领域论文中不常见的。

**S2. Negative results 的诚实呈现。** Router 训练 step-level 泛化失败（balanced accuracy ≈ chance）、data augmentation 无效（Appendix J）——这些 negative results 对社区同样有价值，且呈现方式坦诚。Section 3.6 和 Appendix I-J 提供了充分的失败分析。

**S3. 分析覆盖度高。** Dose-response 曲线（Figure 3）、grounding ablation（Appendix O）、failure mode taxonomy（Appendix N, 4 个 failure categories）、action distribution analysis（Appendix N, Figures 5-7）、capacity scaling（Appendix P）、threshold routing（Appendix Q）——附录内容构成了对核心发现的全方位验证。

**S4. Counterfactual 设计干净。** Pure-strategy trajectories 在相同 initial conditions 下独立运行，消除了 step-level confounding。Episode-level labeling function（Algorithm 1）是 penalty-independent 的，这一设计选择合理且有意义。

**S5. Cross-model validation 增加可信度。** Llama-3.1-8B-Instruct 复制（Section 3.2, Appendix M）显示 internal death rate 11.4% vs. deterministic 11.4%（death-rate differential 一致），DAF 保持 intact，证明发现不依赖特定模型。

## 3. Weaknesses

### Must-Fix

**W1 [critical] 核心发现的 novelty 不足——"obvious in hindsight" 问题。**
- 具体位置：Section 1 (Introduction), Section 5 (Non-triviality), Abstract
- 问题：ScienceWorld 对 agent death 施加 −100 penalty（P=100），而 internal strategy 的 death rate 显著高于 deterministic strategy（~43% vs. ~10%, Table 1）。在这种 asymmetric death rate + extreme penalty 的设定下，death avoidance 成为 dominant routing signal 是一个在读到 experimental setup 后就可以预见的结果。Section 5 的 "Non-triviality" 论证试图通过 threshold routing 不能超越 always-deterministic 来论证非平凡性，但这只是说明了发现的 robustness，不是非显而易见性。论文自己在 Section 2.4 承认 DAF "increases monotonically with P" 且是 "a mathematical consequence rather than an empirical finding"。
- 为什么影响接收：对 EMNLP long paper，reviewer 需要看到 non-obvious insight。如果核心 claim 在看到 setup 后就是显而易见的，则 contribution 显著削弱。
- 建议修改方向：(a) 增加 expert prediction study 或 reader survey，证明领域专家在看到 setup 后并不能预测 78.9% 这个具体比例或 SCI 的集中度；(b) 或者彻底重新 framing——把贡献重心从 "finding" 转到 "framework"，强调方法论本身的通用性和可迁移价值；(c) 在不同 P 值（如 P=10, 25, 50, 100, 200）下做系统实验，展示 death dominance 的 phase transition point，这比论证 P=100 下的单一结果有更高 novelty。

**W2 [critical] Framing 内在张力：framework vs. finding 定位不清。**
- 具体位置：Title, Abstract, Section 1 (Contributions), Section 6 (Conclusion)
- 问题：标题 "Death Avoidance as the Dominant Routing Signal" 聚焦 empirical finding，但 Contribution 1 是 "episode-level counterfactual framework"。Abstract 同时强调两者但重心在数字。Conclusion 只有 2 句话，完全 finding-oriented。这导致读者无法确定论文的核心 identity——是一个通用的 diagnostic tool（那 ScienceWorld 只是 case study），还是一个关于 ScienceWorld 的 empirical observation（那 framework 只是工具）。
- 为什么影响接收：Framing 不清会导致 reviewer 和 AC 对论文的 contribution 类型产生分歧，进而影响评分一致性。
- 建议修改方向：选择一个主线并贯穿始终。如果选 framework，标题改为强调方法论（如 "An Episode-Level Counterfactual Framework for Diagnosing Routing Signals in LLM Agents"），ScienceWorld 结果作为 demonstration；如果选 finding，则弱化 framework 的 contribution claim，但需要更强地论证 finding 的 non-triviality。

**W3 [critical] Single-environment 深度 vs. 广度不足，但 claim 覆盖面过广。**
- 具体位置：Abstract ("routing signal is concentrated in a few types or distributed systematically"), Section 3.4, Section 5 (Discussion)
- 问题：主体实验仅基于 ScienceWorld（1 个环境，1 个 backbone）。MATH 和 ALFWorld 的 cross-environment probes（Section 3.4, 各约半页）过于简略——MATH 只报告了 balanced labels 和 "no catastrophic failure"，ALFWorld 只报告了 "information asymmetry rather than death"。这三个环境的 routing dynamics 差异很大（MATH 无 death，ALFWorld 无 −100 penalty），很难从中提取 generalizable conclusions。但 Abstract 和 Discussion 中的 claims 暗示了跨环境的普遍性。
- 为什么影响接收：EMNLP long paper 对 generalizability 有较高期待。仅靠一个环境 + 两个浅层 probe 难以支撑 "routing signal in interactive environments" 的一般性论述。
- 建议修改方向：(a) 至少在一个额外的 death-prone interactive environment（如 NetHack/MiniHack，论文已在 Discussion 中提到）做完整分析；(b) 或者明确限定 scope 为 "ScienceWorld analysis"，将 generalizability 作为 future work 而非 implied claim。

### Should-Fix

**W4 [warning] "Modality" 术语在 NLP 语境下有严重歧义。**
- 具体位置：全文（Section 2.1, 2.2, 2.3 等），Method 部分定义 "modality m ∈ M"
- 问题：论文用 "modality" 指代 computation mode（internal reasoning vs. deterministic）。在 NLP/ML 领域，"modality" 绝大多数情况指 data modality（text, vision, audio）。这在 EMNLP venue 下尤其容易造成误导。
- 建议："strategy" 或 "computation mode" 更准确，且全文已有混用（如 "pure-strategy trajectories"）。统一术语即可。

**W5 [warning] Conclusion（Section 6）过于简短，不匹配 long paper 标准。**
- 具体位置：Section 6，仅 2 句话
- 问题：对于 8 页正文的 long paper，Conclusion 仅有 "We decomposed routing signal... 78.9% of non-tie labels arise from death asymmetry... Future work should target intermediate death regimes and stronger backbones." 没有对 broader implications 的讨论，没有对 framework 局限性的反思，没有对不同 community（safe RL, agent design）的启示。Discussion（Section 5）虽然包含一些内容，但 Conclusion 本身作为论文的收尾是不完整的。
- 建议：扩展 Conclusion 至 ~0.5 页，涵盖 key takeaways、practical implications for agent designers、framework 的适用边界。

**W6 [warning] 缺少 penalty magnitude 的系统实验。**
- 具体位置：Section 2.4 (DAF definition), Appendix K (Penalty Sensitivity)
- 问题：Section 2.4 推导了 DAF 随 P 单调递增的数学关系，Appendix K 的 Table 12 给出了 P=10,25,50,100,200 的 DAF 值，但这些是 **数学推导** 而非实验结果。论文没有实际在不同 P 值下运行 ScienceWorld 实验来验证推导是否成立。这是一个明显的 validation gap——DAF 的公式假设 Δ_nd 和 death rates 不随 P 变化，但在实际环境中，agent behavior 可能会因 penalty magnitude 不同而改变。
- 建议：至少在 P=10 和 P=50 下运行实际实验，验证 DAF 公式的预测是否与实际匹配。

**W7 [warning] Safe RL Related Work 不够深入。**
- 具体位置：Section 4 (Related Work)，最后一段 "Safe RL"
- 问题：论文本质上发现了 routing 中的 safety-driven 行为，但 Safe RL 讨论仅一段，列举了 García & Fernández (2015), Tamar et al. (2015), Achiam et al. (2017), CRPO (2021), Moldovan & Abbeel (2012), Ruan et al. (2024), SafeRoute (2025) 等引用，但没有实质性地讨论这些工作与本文发现的关系。例如：constrained MDP framework 如何解释 death avoidance 作为 implicit constraint？risk-sensitive RL 中的 CVaR 优化与 death avoidance 的关系？
- 建议：将 Safe RL 段落扩展到 ~0.5 段，具体讨论 death avoidance 如何映射到 safe RL 的 formalism（如 CMDP 的 constraint 对应 death avoidance，cost function 对应 death penalty）。

**W8 [warning] Abstract 数字过密，可读性受损。**
- 具体位置：Abstract
- 问题：Abstract 中出现 "78.9%"、"245 episodes"、"Qwen2.5-7B-Instruct"、"11 task types"、"DAF reaches 90.4%"、"95% CI: [81.6%, 98.8%]"、"P=100"、"δ = 0.265"——大量数字和技术细节压缩在一段中，首次阅读时难以抓住核心 message。
- 建议：Abstract 前半段用概念性语言阐述 framework 和 key insight，后半段再给关键数字。将 CI 和 δ 值等细节移到正文。

### Minor

**M1** Section 3.1 第一段 "Of 93 non-tie routing labels across 245 episodes, 75 (78.9%) arise from death asymmetry"——93 non-tie out of 245 means 152 episodes are ties (62%)。这个 tie rate 很高但论文未充分讨论其含义。如果大多数 episodes 两种 strategy 表现相同，那 routing 的实际价值本身就值得质疑。

**M2** Figure 2 的 y-axis label ("Performance gap (det. − int., ppt)") 字体过小，难以辨认。建议增大字体或简化 label。

**M3** Appendix 篇幅极长（A-R，12 页），部分内容可合并（如 Appendix C-F 可合并为一个 per-task analysis section）。

**M4** 引用验证：`webb-2023` 实际发表年份为 2014（OpenAlex 匹配），bib 标注 2023，需核实是否为修订版。`react-2023` 和 `zhou2024webarena` 未在 OpenAlex 上找到（可能是 indexing 问题，非 fake citation）。`mixture-of-recursions-2025` 同样未找到。

**M5** Responsible NLP Checklist (page 21) 提到 "AI assistants were used for code development and manuscript editing"——适当的 disclosure，但建议具体说明使用了哪些 AI assistants 及其使用范围。

## 4. Questions for Authors

**Q1.** 你们是否考虑过在 death penalty 不同的 ScienceWorld 变体（如修改 reward function 使 P < 100）上运行实际实验？DAF 公式假设 Δ_nd 不随 P 变化，这一假设是否在实际中成立？

**Q2.** 62% 的 episodes 是 ties（两种 strategy 同分）。这是否说明在大多数情况下 routing 本身缺乏价值？你们如何看待这一 observation 对论文 framing 的影响？

**Q3.** Signal Concentration Index (SCI ≤ 0.1, Appendix A) 显示 death avoidance 集中在 top-3 task types（占 30.8% 的 total death-rate differential）。这是否意味着 "death dominance" 本质上是 task-type specific 而非 environment-wide 的现象？

**Q4.** 论文提到 internal strategy 的 105 次 death（Table 1）中 "All 105 internal-strategy deaths trace to misuse of `focus on {object}`"（Section 5, Anatomy of catastrophic failure, page 8 / Appendix N）。这是否意味着 "death avoidance" 本质上是 "一个特定 action 的 bug avoidance"？如果修复这一个 action pattern，death dominance 是否会消失？

**Q5.** Grounding ablation（Appendix O）显示 blocking `focus on` 降低 death rate 至 29.0%。这与 Q4 相关——如果大部分 death 可以通过简单的 action filtering 消除，那 routing 的角色是什么？

## 5. Missing References

- **Constrained MDP / CMDP 基础文献**：Altman, E. (1999). *Constrained Markov Decision Processes*. 论文的 death avoidance 本质上是一个 safety constraint，CMDP 框架是自然的理论对应，但未引用。
- **Risk-sensitive RL 中的 death avoidance**：Mihatsch & Neuneier (2002). "Risk-sensitive reinforcement learning." 与论文的 catastrophic failure avoidance 直接相关。
- **LLM agent safety 更广泛的 survey**：如 Xi et al. (2025) 等更近期的 LLM agent safety survey，可能比 Ruan et al. (2024) 提供更全面的 landscape。

## 6. Overall Assessment

**Overall**: 3 (Findings)
**Confidence**: 4/5

**一句话总结**：方法论扎实、分析彻底，但核心发现在环境设计已知的前提下缺乏 surprise，framing 存在 framework vs. finding 的张力，单环境+浅层 cross-environment probe 限制了 generalizability。适合 Findings track，但难以支撑 main conference 级别的 novelty 要求。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论设计合理，统计分析严谨（bootstrap, cluster-robust inference），但 DAF 是数学推导而非 empirical metric，且缺少 penalty variation 的实际验证 |
| Excitement | 2.5/5 | 核心发现在知道 setup 后基本可预见；practical takeaway 不明确（"routing 被 death avoidance 主导" → 所以呢？）；对 agent design 的指导意义需要更强论证 |
| Reproducibility | 4/5 | 附录极其详细（hyperparameters, seed robustness, per-task breakdowns），但未明确提供 code/data release plan |
| Clarity | 3/5 | "modality" 术语歧义，Abstract 过密，framing 不清（framework vs. finding），但 Method 和 Experiments 的写作本身是清晰的 |

## 7. Detailed Comments by Section

### Title & Abstract
- 标题聚焦 finding 但 contribution 1 是 framework——建议调整一致性
- Abstract 数字密度过高，建议重组为 concept-first, numbers-second

### Section 1 (Introduction)
- 从 routing problem → gap → framework → finding 的逻辑链基本通畅
- 但 "what signal drives the routing decision" 作为 research question 的 framing 不够 sharp——应该更早说明为什么 existing routing work 没有回答这个问题
- 第 3 段提到 "no prior work has systematically decomposed what drives routing decisions"——需要更具体地说明 "decomposed" 在这里的含义，与 existing ablation/analysis 的区别

### Section 2 (Method)
- 写得最清晰的部分
- Algorithm 1 (Appendix) 的 penalty-independent labeling 是一个好的设计选择
- Section 2.4 的 DAF 定义数学上清晰，但论文需要更 upfront 地承认这是 derived quantity 而非 discovered metric

### Section 3 (Experiments)
- Section 3.1 (Death Decomposition) 结果呈现清晰
- Section 3.2 (Multi-Model Validation) 加分但篇幅过短
- Section 3.3 (Agent-Level Improvement) 有价值，展示了 Reflexion 和 self-correction 的边际效果
- Section 3.4 (Cross-Environment Probes) 过于浅显——MATH 和 ALFWorld 各只有 ~1 段，结果只是 "confirms similar pattern" 或 "different mechanism"，没有深入分析
- Section 3.5 (Baselines) 中 Oracle 的 90.3% 远低于 100%——这个 gap 值得更多讨论（为什么 perfect routing 仍有 9.7% 的信息损失？）
- Section 3.6 (Router Training) 作为 negative result 有价值，但与 main narrative 的连接需加强

### Section 4 (Related Work)
- Tool Use 和 Adaptive Computation/Routing 覆盖充分
- Counterfactual RL 覆盖 adequate
- LLM Agent Environments 覆盖充分
- **Safe RL 明显不足**——仅一段，需扩展

### Section 5 (Discussion)
- "Why the router fails" 分析有价值
- "Non-triviality" 论证不够有力（见 W1）
- "Anatomy of catastrophic failure" 是重要的定性分析
- "Practitioner implications" 段落实用但过于 list-like

### Section 6 (Conclusion)
- 严重不足——仅 2 句话。见 W5。

### Limitations
- 覆盖面 adequate：single environment, single backbone, 19 excluded tasks, step-level error compounding
- 但缺少对 "P=100 specific" 这一限制的明确讨论

### Figures & Tables
- Figure 1 (Pipeline)：清晰，自解释
- Figure 2 (Scatter)：核心证据图，展示 r≈1 的近完美相关，有效但 y-axis label 太小
- Figure 3 (Dose-response)：信息量大，展示 N=1→5 的 death rate 下降，好图
- Table 1：清晰的 per-condition death rate 分解
- Table 2：Episode-weighted mean scores，信息完整
- Figure 4 (Cross-environment, Appendix L)：label distributions 有用但讨论不够

### 格式合规
- ✅ 正文 8 页（Conclusion 在 page 8 底部结束）
- ✅ Limitations 在正文后（page 9），不计入页数
- ✅ Ethics Statement 在 Limitations 后
- ✅ Double-blind: "Anonymous ACL submission"
- ✅ 引用格式基本统一（\cite / \citep / \citet 使用合理）
- ✅ 无 orphan bibliography entries（verify_references 确认 0 orphan, 0 missing）
- ⚠️ `webb-2023` 年份可能有误（API 匹配到 2014 年版本）


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

_source line 1722 · 2026-05-19T15:50:10.003608+00:00_

Reviewer 2 审稿意见已收到。评分：Overall 3 (Findings)，Excitement 2.5/5。主要 critical issues：novelty 不足（obvious-in-hindsight）、framing 张力（framework vs. finding）、单环境深度不足。

等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 143

## Round 143

6 recorded events


### User

_source line 1723 · 2026-05-19T15:50:13.897588+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性与实验设计

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 (Long Paper via ARR)

---

## 1. Summary

本文提出一个 episode-level counterfactual diagnostic framework，用 pure-strategy trajectory 对比量化模块化 LLM agent 中 routing 信号的来源。核心发现：在 ScienceWorld 的 245 episode pairs（11 task types）中，78.9% 的 non-tie routing labels 源于 death asymmetry（internal strategy 的幻觉引发 catastrophic agent death），而非 nuanced capability matching。Death Avoidance Factor (DAF) 在默认 penalty（P=100）下达 90.4%。跨环境 boundary probes（MATH、ALFWorld）和 router 训练实验进一步支持该诊断。

论文问了一个好问题（routing 信号到底是什么？），给出了一个清晰且 largely convincing 的回答，实验工作量大（21 页含详细附录），但在统计推断、跨环境证据、router 实用性方面有不可忽视的缺陷。

---

## 2. Strengths

**S1. 问题定义精准且有价值。** 现有 routing 文献关注"怎么 route"，本文追问"routing 到底在 route 什么信号"——这是一个被忽视但影响 router 设计方向的诊断性问题。将 routing signal 分解为 death-avoidance 和 non-death components 的思路简洁有力。

**S2. Pure-strategy counterfactual 设计干净。** 控制相同 random seed + initial conditions，让 performance gap 完全归因于 computation mode choice（Section 2.2），是 well-identified 的因果推断设计。Episode-level labeling function（Algorithm 1）先按 survival 排序再比较 score 是合理的——在 sparse reward 环境中 step-level oracle 无法区分策略。

**S3. DAF 分解数学上 clean。** Eq. (4)-(5) 将 full gap 分解为 δP（death-rate differential × penalty）和 Δ_nd（non-death score gap），公式推导正确。论文明确指出 DAF 随 P 单调递增是数学后果而非经验发现（Section 2.4, p4 top），这种诚实性值得肯定。

**S4. Robustness checks 全面。** Leave-one-task-out DAF sensitivity（Appendix G, Table 7）、penalty sensitivity（Appendix K, Table 12-13）、cross-model replication with Llama-3.1-8B（Section 3.2）、anti-cherry-picking analysis（Appendix C）、8-seed robustness（Appendix J, Table 8）——覆盖了主要的 robustness 角度。

**S5. Signal Concentration Index (SCI ≤ 0.1, Appendix A)** 有效回应了"信号是否集中在少数 task types"的质疑，表明 death dominance 分布相对均匀。

**S6. Limitations 坦诚且具体。** 明确讨论了 single environment scope、pure-strategy distribution shift、cluster bootstrap K=11 限制、current routing scope limitations（Section 9/Limitations），未回避关键弱点。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] DAF headline number 的误导性与 penalty-independent metric 的关系未充分厘清**

- **具体位置**: Abstract ("penalty-weighted DAF reaches 90.4%"), Section 2.4 (Eq. 5), Section 3.1
- **问题**: DAF = δP/(δP + Δ_nd)。当 Δ_nd 较小且为正时（论文数据 Δ_nd ≈ 0.23），DAF 在任何 P > 0 时都会接近 1，因为 δP = (death_rate_diff) × P 随 P 线性增长。论文在 p4 顶部承认这是数学后果，但 Abstract 和 Section 3.1 仍以 "DAF = 90.4%" 作为 headline finding，与 penalty-independent 的 78.9% label fraction 并列呈现。读者容易误解 90.4% 是独立于 penalty 设计的经验发现。
- **为什么影响接收**: 如果核心量化指标的 informativeness 被质疑，论文的主要 contribution 会打折扣。90.4% 和 78.9% 应被清楚定位：78.9% 是 penalty-independent 的 robust finding，DAF 是说明 penalty 放大效应的补充指标。
- **建议修改方向**: (1) Abstract 以 78.9% 为 primary metric，DAF 降为补充；(2) 在 Section 2.4 增加一段讨论 DAF 在不同 Δ_nd 下的行为——当 Δ_nd < 0（non-death gap 反向）时 DAF 的解释力；(3) 考虑报告 DAF 在 Δ_nd = 0 的边界行为。

**N2 [critical] Cluster bootstrap K=11 低于公认阈值，wild cluster bootstrap 的适用性辩护不足**

- **具体位置**: Section 2.4 ("episode-level bootstrap resampling"), Appendix E (Table 6), Limitations (p9)
- **问题**: 论文使用 K=11 task types 作为 cluster units 进行 cluster bootstrap。Cameron et al. (2008)（论文自己引用的文献）建议 K ≥ 20 甚至 K ≥ 40 以获得可靠推断。Wild cluster bootstrap（Webb 2023）在小 K 下有改善但并非万能——Webb (2023) 原文的 Monte Carlo 模拟显示 K < 20 时 rejection rate 仍有明显 size distortion。
  - Table 6 报告 wild cluster bootstrap p = 0.002 且 exact permutation (2,048 perms) p = 0.002，但 2^11 = 2048 的排列总数意味着 p = 0.002 对应的是 4/2048 ≈ 0.002 的极端排列数——这个分辨率本身就说明 K=11 下置换检验的颗粒度很粗。
  - Cohen's d = 3.02 是极端大的效应量（远超社会科学的 d ≈ 0.8 "large" 标准），在小 K 下更可能受 outlier task types 影响。
- **为什么影响接收**: 统计推断的可靠性是方法论论文的基石。审稿人和读者需要确信 p-values 和 CIs 不是 K=11 的 artifact。
- **建议修改方向**: (1) 在正文（而非仅 Limitations）明确讨论 K=11 vs Cameron et al. 的 K ≥ 40 建议，解释为什么 wild cluster bootstrap + exact permutation 在本场景下足够（例如：effect size 极大，所有 11 clusters 方向一致等）；(2) 报告 leave-one-cluster-out sensitivity（已有 Table 7，但应在正文引用并讨论最差情况下 DAF 的下界）；(3) 讨论 Cohen's d = 3.02 在小 K 下的可解释性。

**N3 [critical] Episode-to-step label projection 的系统性噪声未被充分量化和缓解**

- **具体位置**: Section 2.3 ("episode labels thus apply correct direction to uninformative steps"), Section 4.2, Appendix B
- **问题**: 97.4% 的 steps 是 step-level ties（Table 2 area），episode labels 投射到这些 steps 产生 27.7% mislabeling（Section 4.2）和 60.3% pre-event neutral steps。这意味着 router 训练数据中：
  - ~60% 的 steps 在 death event 之前，label 方向正确但 signal 强度为零
  - ~28% 的 steps 被 mislabel（episode label 与 step-level truth 不一致）
  - 仅 ~12% 的 steps 有 informative + correctly-labeled signal
  - 这解释了 step-level balanced accuracy 56-59% 接近 chance。
- **为什么影响接收**: 论文将 router 定位为 "diagnostic probe"，但如果 probe 的 training signal 本身有 88% 的 noise/uninformative rate，那么 probe 失败不能证明 "death avoidance signal is not step-level learnable"——它可能只证明了 episode labels 是 noisy step-level supervision。这削弱了 Section 4.2 ("router diagnostic") 的诊断价值。
- **建议修改方向**: (1) 实验一个 step-level label refinement baseline——例如只用 death event 后的 steps 训练，或按 proximity-to-death 加权；(2) 如果不做实验，至少提供更精确的 noise characterization（e.g., confusion matrix of episode vs step labels across all steps）；(3) 明确 router failure 的 attribution：是 signal inherently not step-level，还是 label noise 太高？

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] Cross-environment probes 的定位与措辞需要更精确**

- **具体位置**: Section 3.4, Table 2 (MATH row, ALFWorld row)
- **问题**: MATH 无 catastrophic failure → 无 death asymmetry signal，ALFWorld 的 deterministic advantage 来自 information asymmetry（admissible-action access）而非 computation mode switch。论文将这两个称为 "cross-environment boundary probes"（Section 3.4 标题），但 Abstract 的 "confirmed across four intervention axes and two cross-domain probes" 暗示了更强的验证力度。
  - 实际上：MATH 是 null result（符合预测但 unfalsifiable——任何无 death 的环境都会得到相同结果），ALFWorld 验证了不同机制下的 death dominance 但机制本身不同（information advantage ≠ computation mode routing）。
- **建议**: (1) 调整 Abstract 措辞，将 boundary probes 明确定位为 "consistency checks" 而非 "cross-domain validation"；(2) 在 Section 3.4 讨论 "deterministic" 在三个环境中含义不同的问题。

**W2 [warning] Pure-strategy 设计的外部效度需更深入讨论**

- **具体位置**: Section 2.2 (pure-strategy definition), Limitations (p9)
- **问题**: 现实 routing 场景中 agent 不会全程使用单一模式。Pure-strategy 设计让 internal strategy 有 30 steps 来连续积累 hallucination errors，可能 amplify death rate。如果 routing 在中途切换，death event 可能被避免。因此 pure-strategy 对比可能 overestimate death asymmetry 在 mixed-strategy routing 中的实际影响。
  - 论文在 Discussion (Section 5) 提到 "multi-step nature of routing (10-30 actions) with compounding state uncertainty creates inherent label noise"，但未直接量化 pure-strategy overestimation。
- **建议**: 提供一个 back-of-envelope 估计或 sensitivity analysis：如果 router 在 episode 中途（如 step 15）切换到 deterministic，death rate 会下降多少？

**W3 [warning] Reflexion dose-response 的统计功效（N=5 trials, 10 death-prone tasks）**

- **具体位置**: Section 3.3, Figure 3, Appendix H (Table 8)
- **问题**: N=5 trials per task，10 death-prone tasks。Reflexion 的 death rate 从 62.9% → ~48% (N=3) → plateau。Wilson 95% CIs 已报告（Figure 3），error bars 大。Table 8 显示 per-task variance 高达 25pp。关键问题：N=5 的功效是否足以区分 "Reflexion plateau = genuine ceiling" vs "Reflexion plateau = insufficient trials"？
  - 论文承认 "the minimum detectable effect at n=20(N=14) pp (α=0.05, power=0.80)"——这意味着 N=5 下可检测的最小效应更大，Reflexion 可能有被 underpowered 遗漏的中等效应。
- **建议**: (1) 报告 power analysis for N=5 的 minimum detectable effect；(2) 讨论 N=5 的 Reflexion 结果是 conclusive evidence 还是 suggestive evidence。

**W4 [warning] Router "diagnostic probe" 定位与 contribution claim 之间的张力**

- **具体位置**: Section 3.6, Section 4.2, Appendix I-P
- **问题**: 论文同时 claim (a) 提出了一个 diagnostic framework 和 (b) router training results 是 diagnostic probe。但 router 结果非常弱（step-level 56-59% ≈ chance, episode-level 只有 4B 有改善且 47.1 ± 2.2% ≈ chance for smaller scales），这使得论文的实用影响受限。如果 router 只是为了证明 death signal hard to learn at step level，那 Section 3.6 的 framing 应更明确地说"这是一个 negative result"，而非暗示 4B 的 marginal improvement 有实际意义。
- **建议**: 将 router 实验明确框架为 negative result（step-level death avoidance signal 难以学习），讨论 implications for router architecture design（什么样的 router 可能绕过这个问题？）。

### Minor 问题（不影响接收）

**M1.** Table 1 caption "Episode-weighted mean scores" 但未说明 weighting scheme 是否 uniform across 11 task types 还是按 episode count weighted。Appendix 中 Table 3 的 per-task data 可以验证但正文应明确。

**M2.** Figure 2 scatter plot 的 r = 0.97 pearson correlation 在 K=11 points 下容易受 leverage points 影响。应报告 robust correlation（如 Spearman's rho，已在 Appendix D 报告为 ρ = 0.975，建议在正文 Figure 2 caption 也提及）。

**M3.** Webb (2023) 在 bib 中标注 year=2023，但 OpenAlex 显示该论文发表于 2014（Canadian Journal of Economics, 56(3):839-858, originally 2014 working paper, journal version 2023）。建议确认引用的是 journal version 还是 working paper。

**M4.** Appendix R "Decision Framework" (Section R, p20) 中 "f_death < 50%" 和 ">75%" 的阈值选择缺乏理论依据，可能限制 framework 的泛化性。

**M5.** 论文第 8 页结尾 Section 6 Conclusion 较短（约 8 行），可适当扩展讨论 broader impact 和 future directions。

---

## 4. Questions（需要作者澄清）

**Q1.** DAF 在 Δ_nd < 0（deterministic non-death score 低于 internal non-death score）的 task types 中是否存在？如果存在，DAF 如何解释？Table 3 中是否有这样的 task type？

**Q2.** 论文报告 "all 105 internal-strategy deaths trace to misuse of `focus on [object]`"（Section 5, Discussion）。这是否意味着 death avoidance signal 实质上是 "`focus on` action avoidance" signal？如果 router 只需要学习 "avoid focus on"，这是否简化了问题定义？

**Q3.** Grounding ablation（Appendix O）显示 explicit system prompt 减少了 aggregate death rate 但 per-task variation large（35-40% residual）。如果 grounding intervention 的效果 task-dependent，这对 DAF decomposition 有什么影响？

**Q4.** 论文提到 "the 3.7% internal-preferred base rate makes real-data collection expensive"（Section 4.2, p5 bottom）。如果只有 3.7% 的 real routing decisions 倾向 internal，这是否意味着一个简单的 "always-deterministic" baseline 已经在实际部署中接近最优？

**Q5.** Cross-model replication (Llama-3.1-8B) 的 death rate 11.4% vs 11.4% (Appendix M, Table 15) 看起来非常接近。Llama 的 DAF 是多少？是否与 Qwen 的 DAF 一致？

---

## 5. Missing References

论文的 related work 覆盖较全面，但建议考虑以下方向：

- **Routing with risk awareness**: 最近的 SafeRoute (Lee et al., 2025) 已引用，但 cost-aware routing 文献中 risk-sensitive 策略的讨论可以更深入（如 conditional value-at-risk approaches beyond Tamar et al. 2015）。
- **Agent failure taxonomy**: 除了 Ruan et al. (2024) 的 failure identification，Wang et al. (2024) "On the Resilience of Multi-Agent Systems" 或类似的 failure mode classification 工作可能相关。
- **Label noise in binary classification**: 27.7% mislabeling rate 下的 router training 可以连接到 noisy label learning 文献（如 Natarajan et al. 2013 "Learning with Noisy Labels"），提供 theoretical grounding for the observed near-chance accuracy。

---

## 6. 格式合规检查

- **正文页数**: 8 页（Section 1-6 在 p1-p8），符合 ≤ 8 页要求 ✓
- **Limitations**: 存在（p9），内容具体，讨论了 single environment、statistical limitations、methodological constraints ✓
- **Ethics Statement**: 存在（p9），确认无人类受试者、数据公开、模型开源 ✓
- **Responsible NLP Checklist**: p20-21，逐项回答完整 ✓
- **匿名性**: 标题页 "Anonymous ACL submission"，未发现 self-citation 泄露 ✓
- **引用格式**: 49 条引用，格式基本统一。Webb (2023) 年份需确认（见 M3）。4 条 OpenAlex 未找到但均为已知论文（ReAct、WebArena 等），非伪造 ✓

---

## 7. Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法论 clean 且 well-motivated，但 K=11 cluster bootstrap 低于公认阈值、episode-to-step label projection 噪声未充分量化缓解。DAF monotonicity 处理诚实但 headline framing 有误导风险。|
| **Excitement** | 3.5/5 | "Routing 到底在 route 什么"是有价值的诊断性问题，death dominance finding 对 router 设计有实际启示。但 router probe 本身结果弱（near-chance），跨环境证据有限，限制了 excitement。|
| **Reproducibility** | 4.5/5 | 详细的超参数（Appendix E, I）、seeds、per-task breakdowns（Table 3-4）、compute budget（Ethics Statement）。代码和数据 via API，4-seed cross-split（Appendix J）。接近模范水平。|
| **Datasets** | 2/5 | 使用现有环境（ScienceWorld, MATH, ALFWorld），未贡献新数据集。245 episode pairs 可作为 benchmark 但论文未明确 release plan。|
| **Software** | 2/5 | 诊断 framework 可复用，但无独立 software release 计划。|
| **Reviewer Confidence** | 4/5 | 熟悉 LLM agent routing、counterfactual evaluation、bootstrap methods。仔细阅读了全文（21 页含所有附录）。|

### Overall Assessment

**Overall: 3.5 — Borderline Conference**

**一句话总结**: 论文问了一个重要且被忽视的诊断性问题（routing signal 到底是什么），给出了清晰的回答（death avoidance dominates），实验工作量大且 robustness checks 全面，但 K=11 统计推断的可靠性、episode-to-step projection 噪声对 router diagnostic 的影响、以及跨环境证据的有限性，使其处于 Conference 和 Findings 的边界。

**Conference 方向的论据**: 问题定义精准、counterfactual 设计干净、78.9% death-asymmetry label fraction 在多个 robustness check 下稳定、cross-model replication 一致、limitations 诚实。
**Findings 方向的论据**: K=11 低于公认阈值且辩护不足（N2）、router probe 几乎是 negative result 但 framing 模糊（N3/W4）、cross-environment evidence 弱于论文措辞暗示的程度（W1）、DAF 的 headline framing 需要修正（N1）。

如果 N1（DAF framing）和 N2（K=11 辩护）在 revision 中得到充分回应，我会倾向于上调至 4.0 (Conference)。

---

## 8. Detailed Comments（按章节）

### Section 1 (Introduction)
- 清晰地 motivate 了问题。"78.9% of non-tie routing labels arise from death asymmetry" 作为 opening hook 很有效。
- 但 "penalty-weighted DAF reaches 90.4%" 出现在第二句，位置过高，容易形成 "90.4% is the main finding" 的印象（见 N1）。

### Section 2 (Method)
- Algorithm 1 的 labeling function 设计合理——先按 survival 排序，death-aware prioritization 有理论依据。
- Eq. (4)-(5) 的 DAF 分解公式推导正确，Δ_res ≈ 0.23 (0.8% of Δ_full) 的 residual 确认了分解的 completeness。
- 但 Section 2.3 "episode labels thus apply correct direction to uninformative steps—a granularity mismatch, not label error" 的说法值得商榷：direction 正确但 magnitude 为零的 supervision 在 gradient-based training 中是否真的 "not label error"？这取决于 loss function（BCE 会将 magnitude=0 的正确 direction 当作 confident signal）。

### Section 3 (Experiments)
- 3.1 Death Decomposition: 核心实证 section，数据呈现清晰。Figure 2 scatter 有效。
- 3.2 Cross-Model: Llama replication 增加可信度，但仅报告了 aggregate death rate，未报告 DAF。
- 3.3 Baselines: Retry/Reflexion/72B/action filtering 覆盖了主要 intervention 方向。"All interventions reduce death rate but none approaches deterministic safety" 是 strong claim，基于 Table 1 的证据可以支持。
- 3.4 Cross-Environment: 见 W1。
- 3.6 Router: 见 N3, W4。

### Section 4 (Related Work)
- 结构清晰（Tool Use, Adaptive Computation, Counterfactual RL, LLM Agent, Safe RL），覆盖全面。
- 最后一句 "the deterministic strategy sidesteps catastrophic states entirely" 是论文 key insight 的精炼表述。

### Section 5 (Discussion)
- "all 105 internal-strategy deaths trace to misuse of `focus on`" 是重要的 qualitative finding，但出现在 Discussion 而非 Experiments 让人意外——建议在 Section 3 中更早呈现，因为这直接影响 death avoidance signal 的可解释性。
- Practitioner implications 具体且 actionable（三阶段诊断 framework）。
- "Framework applicability" 段落的 "DAF decreases monotonically with P" 应为 "DAF values in Table 12 increase monotonically"（数字上递增，但 informativeness 递减）——请确认措辞。

### Section 6 (Conclusion)
- 过于简短（~8 行）。"Future work should target intermediate death regimes and stronger backbones" 是 reasonable direction 但 generic。

### Limitations
- 全面且诚实，覆盖了 scope、statistical、methodological constraints。K=11 cluster bootstrap 的 limitation 已提及但可更具体（见 N2）。

### Appendices
- 非常详细（A-R），是论文的重要支撑。特别是 Appendix B (Labeling Quality Audit)、G (Leave-One-Task-Out)、K (Penalty Sensitivity)、N (Failure Mode Analysis) 提供了有价值的深度信息。
- Appendix R (Decision Framework) 是 practical contribution 但阈值选择需 justification（见 M4）。


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

_source line 1724 · 2026-05-19T15:51:20.678225+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下关键分歧点：\n1. R2 给 Overall 3.0 (Findings)，你给 3.5 (Borderline Conference)——0.5 分差距主要来自哪里？\n2. R2 的 Excitement 2.5/5 vs 你的 3.5/5——对 novelty 的评估差异较大\n3. R2-W1 (obvious in hindsight) vs 你的 S1 (问题定义精准且有价值)——你是否认为核心发现存在 triviality 风险？\n4. R2-W2 (framing tension) 和 R2-W3 (single-environment broad claims) 是否与你的 W1 (cross-environment probes) 一致？\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## 1. Summary\n\n本文提出一个 episode-level counterfactual diagnostic framework，用于分析 modular LLM agent 中 routing 决策的驱动因素。在 ScienceWorld 环境（11 task types, 245 episodes, Qwen2.5-7B-Instruct）上，将 routing signal 分解为 death-avoidance 和 non-death 两个成分，发现 78.9% 的 non-tie routing labels 源于 death asymmetry——即 internal reasoning strategy 因幻觉触发 catastrophic death（−100 penalty），而 deterministic strategy 存活。作者定义了 Death Avoidance Factor (DAF) 量化该比例，并在 MATH 和 ALFWorld 上做了 cross-environment probe。\n\n## 2. Strengths\n\n**S1. 方法论严谨，统计分析扎实。** Episode-level bootstrap resampling（B=10,000）、wild cluster bootstrap（Appendix E）、per-task confidence intervals（Appendix F）、8-seed robustness（Appendix J）——统计工具的选择和使用都达到高标准。特别是 cluster-robust inference 处理 task-type 内相关性（Cameron et al., 2008; Webb, 2023）是同领域论文中不常见的。\n\n**S2. Negative results 的诚实呈现。** Router 训练 step-level 泛化失败（balanced accuracy ≈ chance）、data augmentation 无效（Appendix J）——这些 negative results 对社区同样有价值，且呈现方式坦诚。Section 3.6 和 Appendix I-J 提供了充分的失败分析。\n\n**S3. 分析覆盖度高。** Dose-response 曲线（Figure 3）、grounding ablation（Appendix O）、failure mode taxonomy（Appendix N, 4 个 failure categories）、action distribution analysis（Appendix N, Figures 5-7）、capacity scaling（Appendix P）、threshold routing（Appendix Q）——附录内容构成了对核心发现的全方位验证。\n\n**S4. Counterfactual 设计干净。** Pure-strategy trajectories 在相同 initial conditions 下独立运行，消除了 step-level confounding。Episode-level labeling function（Algorithm 1）是 penalty-independent 的，这一设计选择合理且有意义。\n\n**S5. Cross-model validation 增加可信度。** Llama-3.1-8B-Instruct 复制（Section 3.2, Appendix M）显示 death dominance replicates across model families。\n\n## 3. Weaknesses\n\n### Must-Fix\n\n**W1 [critical] 核心发现的 novelty 不足——\"obvious in hindsight\" 问题。**\n- ScienceWorld 对 agent death 施加 −100 penalty（P=100），而 internal strategy 的 death rate 显著高于 deterministic strategy（~43% vs. ~10%, Table 1）。在这种 asymmetric death rate + extreme penalty 的设定下，death avoidance 成为 dominant routing signal 是一个在读到 experimental setup 后就可以预见的结果。Section 5 的 \"Non-triviality\" 论证试图通过 threshold routing 不能超越 always-deterministic 来论证非平凡性，但这只是说明了发现的 robustness，不是非显而易见性。\n- 建议：(a) 增加 expert prediction study；(b) 彻底重新 framing 为 framework-centric；(c) 在不同 P 值下做系统实验展示 phase transition。\n\n**W2 [critical] Framing 内在张力：framework vs. finding 定位不清。**\n- 标题聚焦 finding，Contribution 1 是 framework，Abstract 同时强调两者。Conclusion 只有 2 句话，完全 finding-oriented。读者无法确定论文的核心 identity。\n- 建议：选择一个主线并贯穿始终。\n\n**W3 [critical] Single-environment 深度 vs. 广度不足，但 claim 覆盖面过广。**\n- 主体实验仅基于 ScienceWorld。MATH 和 ALFWorld 的 cross-environment probes 过于简略。但 Abstract 和 Discussion 中的 claims 暗示了跨环境的普遍性。\n- 建议：至少在一个额外的 death-prone interactive environment 做完整分析，或明确限定 scope。\n\n### Should-Fix\n\n**W4 [warning] \"Modality\" 术语在 NLP 语境下有严重歧义。**\n\n**W5 [warning] Conclusion 过于简短，不匹配 long paper 标准。**\n\n**W6 [warning] 缺少 penalty magnitude 的系统实验。** Section 2.4 的 DAF vs P 分析是数学推导而非实验结果。论文没有实际在不同 P 值下运行 ScienceWorld 实验。\n\n**W7 [warning] Safe RL Related Work 不够深入。**\n\n**W8 [warning] Abstract 数字过密，可读性受损。**\n\n### Minor\n\n**M1** 93 non-tie out of 245 means 152 episodes are ties (62%)——高 tie rate 的含义未充分讨论。\n\n**M2** Figure 2 的 y-axis label 字体过小。\n\n**M3** Appendix 篇幅极长（A-R，12 页），部分内容可合并。\n\n**M4** 引用验证：`webb-2023` 年份可能有误。\n\n**M5** Responsible NLP Checklist AI assistants disclosure 建议更具体。\n\n## 4. Questions\n\n**Q1.** 是否考虑过在 P < 100 的 ScienceWorld 变体上运行实际实验？\n**Q2.** 62% ties 是否说明 routing 本身缺乏价值？\n**Q3.** SCI 显示集中在 top-3 task types——是否是 task-type specific 而非 environment-wide？\n**Q4.** 105 deaths 全部来自 `focus on [object]`——是否意味着 death avoidance = 单个 action pattern bug avoidance？\n**Q5.** Grounding ablation 降低至 29.0%——如果大部分 death 可通过 action filtering 消除，routing 的角色是什么？\n\n## 5. Missing References\n\n- Altman (1999) CMDP\n- Mihatsch & Neuneier (2002) Risk-sensitive RL\n- Xi et al. (2025) LLM agent safety survey\n\n## 6. Overall Assessment\n\n**Overall**: 3 (Findings)\n**Confidence**: 4/5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Clarity | 3/5 |"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下关键分歧点：\n1. R2 给 Overall 3.0 (Findings)，你给 3.5 (Borderline Conference)——0.5 分差距主要来自哪里？\n2. R2 的 Excitement 2.5/5 vs 你的 3.5/5——对 novelty 的评估差异较大\n3. R2-W1 (obvious in hindsight) vs 你的 S1 (问题定义精准且有价值)——你是否认为核心发现存在 triviality 风险？\n4. R2-W2 (framing tension) 和 R2-W3 (single-environment broad claims) 是否与你的 W1 (cross-environment probes) 一致？\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## 1. Summary\n\n本文提出一个 episode-level counterfactual diagnostic framework，用于分析 modular LLM agent 中 routing 决策的驱动因素。在 ScienceWorld 环境（11 task types, 245 episodes, Qwen2.5-7B-Instruct）上，将 routing signal 分解为 death-avoidance 和 non-death 两个成分，发现 78.9% 的 non-tie routing labels 源于 death asymmetry——即 internal reasoning strategy 因幻觉触发 catastrophic death（−100 penalty），而 deterministic strategy 存活。作者定义了 Death Avoidance Factor (DAF) 量化该比例，并在 MATH 和 ALFWorld 上做了 cross-environment probe。\n\n## 2. Strengths\n\n**S1. 方法论严谨，统计分析扎实。** Episode-level bootstrap resampling（B=10,000）、wild cluster bootstrap（Appendix E）、per-task confidence intervals（Appendix F）、8-seed robustness（Appendix J）——统计工具的选择和使用都达到高标准。特别是 cluster-robust inference 处理 task-type 内相关性（Cameron et al., 2008; Webb, 2023）是同领域论文中不常见的。\n\n**S2. Negative results 的诚实呈现。** Router 训练 step-level 泛化失败（balanced accuracy ≈ chance）、data augmentation 无效（Appendix J）——这些 negative results 对社区同样有价值，且呈现方式坦诚。Section 3.6 和 Appendix I-J 提供了充分的失败分析。\n\n**S3. 分析覆盖度高。** Dose-response 曲线（Figure 3）、grounding ablation（Appendix O）、failure mode taxonomy（Appendix N, 4 个 failure categories）、action distribution analysis（Appendix N, Figures 5-7）、capacity scaling（Appendix P）、threshold routing（Appendix Q）——附录内容构成了对核心发现的全方位验证。\n\n**S4. Counterfactual 设计干净。** Pure-strategy trajectories 在相同 initial conditions 下独立运行，消除了 step-level confounding。Episode-level labeling function（Algorithm 1）是 penalty-independent 的，这一设计选择合理且有意义。\n\n**S5. Cross-model validation 增加可信度。** Llama-3.1-8B-Instruct 复制（Section 3.2, Appendix M）显示 death dominance replicates across model families。\n\n## 3. Weaknesses\n\n### Must-Fix\n\n**W1 [critical] 核心发现的 novelty 不足——\"obvious in hindsight\" 问题。**\n- ScienceWorld 对 agent death 施加 −100 penalty（P=100），而 internal strategy 的 death rate 显著高于 deterministic strategy（~43% vs. ~10%, Table 1）。在这种 asymmetric death rate + extreme penalty 的设定下，death avoidance 成为 dominant routing signal 是一个在读到 experimental setup 后就可以预见的结果。Section 5 的 \"Non-triviality\" 论证试图通过 threshold routing 不能超越 always-deterministic 来论证非平凡性，但这只是说明了发现的 robustness，不是非显而易见性。\n- 建议：(a) 增加 expert prediction study；(b) 彻底重新 framing 为 framework-centric；(c) 在不同 P 值下做系统实验展示 phase transition。\n\n**W2 [critical] Framing 内在张力：framework vs. finding 定位不清。**\n- 标题聚焦 finding，Contribution 1 是 framework，Abstract 同时强调两者。Conclusion 只有 2 句话，完全 finding-oriented。读者无法确定论文的核心 identity。\n- 建议：选择一个主线并贯穿始终。\n\n**W3 [critical] Single-environment 深度 vs. 广度不足，但 claim 覆盖面过广。**\n- 主体实验仅基于 ScienceWorld。MATH 和 ALFWorld 的 cross-environment probes 过于简略。但 Abstract 和 Discussion 中的 claims 暗示了跨环境的普遍性。\n- 建议：至少在一个额外的 death-prone interactive environment 做完整分析，或明确限定 scope。\n\n### Should-Fix\n\n**W4 [warning] \"Modality\" 术语在 NLP 语境下有严重歧义。**\n\n**W5 [warning] Conclusion 过于简短，不匹配 long paper 标准。**\n\n**W6 [warning] 缺少 penalty magnitude 的系统实验。** Section 2.4 的 DAF vs P 分析是数学推导而非实验结果。论文没有实际在不同 P 值下运行 ScienceWorld 实验。\n\n**W7 [warning] Safe RL Related Work 不够深入。**\n\n**W8 [warning] Abstract 数字过密，可读性受损。**\n\n### Minor\n\n**M1** 93 non-tie out of 245 means 152 episodes are ties (62%)——高 tie rate 的含义未充分讨论。\n\n**M2** Figure 2 的 y-axis label 字体过小。\n\n**M3** Appendix 篇幅极长（A-R，12 页），部分内容可合并。\n\n**M4** 引用验证：`webb-2023` 年份可能有误。\n\n**M5** Responsible NLP Checklist AI assistants disclosure 建议更具体。\n\n## 4. Questions\n\n**Q1.** 是否考虑过在 P < 100 的 ScienceWorld 变体上运行实际实验？\n**Q2.** 62% ties 是否说明 routing 本身缺乏价值？\n**Q3.** SCI 显示集中在 top-3 task types——是否是 task-type specific 而非 environment-wide？\n**Q4.** 105 deaths 全部来自 `focus on [object]`——是否意味着 death avoidance = 单个 action pattern bug avoidance？\n**Q5.** Grounding ablation 降低至 29.0%——如果大部分 death 可通过 action filtering 消除，routing 的角色是什么？\n\n## 5. Missing References\n\n- Altman (1999) CMDP\n- Mihatsch & Neuneier (2002) Risk-sensitive RL\n- Xi et al. (2025) LLM agent safety survey\n\n## 6. Overall Assessment\n\n**Overall**: 3 (Findings)\n**Confidence**: 4/5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Clarity | 3/5 |"
  }
}
```

</details>

---


### Tool result

_source line 1725 · 2026-05-19T15:51:55.868058+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 35189
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-19T15:51:57.022347+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下关键分歧点：\n1. R1 给 Overall 3.5 (Borderline Conference)，你给 3.0 (Findings)——0.5 分差距主要来自哪里？\n2. R1 的 Excitement 3.5/5 vs 你的 2.5/5——你是否低估了问题定义本身的价值？\n3. R1-S1 认为\"问题定义精准且有价值\"——这是否缓解了你 W1 (obvious in hindsight) 的担忧？\n4. R1-N3 (episode-to-step label projection) 提出了 router 失败的另一种解释（label noise 而非 signal inherently not step-level）——你是否同意这削弱了 router diagnostic 的诊断价值？\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## 1. Summary\n\n本文提出一个 episode-level counterfactual diagnostic framework，用 pure-strategy trajectory 对比量化模块化 LLM agent 中 routing 信号的来源。核心发现：在 ScienceWorld 的 245 episode pairs（11 task types）中，78.9% 的 non-tie routing labels 源于 death asymmetry。Death Avoidance Factor (DAF) 在默认 penalty（P=100）下达 90.4%。\n\n论文问了一个好问题（routing 信号到底是什么？），给出了一个清晰且 largely convincing 的回答，实验工作量大（21 页含详细附录），但在统计推断、跨环境证据、router 实用性方面有不可忽视的缺陷。\n\n## 2. Strengths\n\n**S1. 问题定义精准且有价值。** 现有 routing 文献关注\"怎么 route\"，本文追问\"routing 到底在 route 什么信号\"——这是一个被忽视但影响 router 设计方向的诊断性问题。\n\n**S2. Pure-strategy counterfactual 设计干净。** 控制相同 random seed + initial conditions，是 well-identified 的因果推断设计。\n\n**S3. DAF 分解数学上 clean。** Eq. (4)-(5) 推导正确。论文明确指出 DAF 随 P 单调递增是数学后果。\n\n**S4. Robustness checks 全面。** Leave-one-task-out、penalty sensitivity、cross-model replication、anti-cherry-picking、8-seed robustness。\n\n**S5. SCI 有效回应了信号集中度质疑。**\n\n**S6. Limitations 坦诚且具体。**\n\n## 3. Weaknesses\n\n### Must-Fix\n\n**N1 [critical] DAF headline number 的误导性。**\n- Abstract 和 Section 3.1 以 \"DAF = 90.4%\" 作为 headline，与 penalty-independent 的 78.9% 并列，读者易误解 90.4% 是独立于 penalty 的经验发现。\n- 建议：Abstract 以 78.9% 为 primary，DAF 降为补充。\n\n**N2 [critical] Cluster bootstrap K=11 低于公认阈值。**\n- Cameron et al. (2008) 建议 K ≥ 20-40。Webb (2023) Monte Carlo 模拟显示 K < 20 时 rejection rate 仍有 size distortion。2^11 = 2048 排列的 p=0.002 颗粒度很粗。Cohen's d = 3.02 在小 K 下可能受 outlier 影响。\n- 建议：正文讨论 K=11 vs K≥40 建议；报告 leave-one-cluster-out sensitivity 的最差情况。\n\n**N3 [critical] Episode-to-step label projection 的系统性噪声。**\n- 97.4% step-level ties → 27.7% mislabeling + 60.3% pre-event neutral → 仅 ~12% informative + correctly-labeled signal。Router probe 失败可能是 label noise 所致，而非 signal inherently not step-level learnable。\n- 建议：实验 step-level label refinement baseline（如只用 death event 附近 steps 训练）；或精确量化 noise 的影响。\n\n### Should-Fix\n\n**W1 [warning] Cross-environment probes 措辞过强。** MATH 是 unfalsifiable null result，ALFWorld 验证了不同机制。应定位为 \"consistency checks\" 而非 \"cross-domain validation\"。\n\n**W2 [warning] Pure-strategy 设计的外部效度。** 现实 routing 中途切换可能避免 death，pure-strategy 可能 overestimate death asymmetry。\n\n**W3 [warning] Reflexion dose-response 统计功效。** N=5 trials，power 是否足以区分 genuine ceiling vs insufficient trials？\n\n**W4 [warning] Router \"diagnostic probe\" 定位与 contribution claim 的张力。** Step-level 56-59% ≈ chance，应更明确框架为 negative result。\n\n### Minor\n\n**M1.** Table 1 weighting scheme 未明确。\n**M2.** Figure 2 应在 caption 报告 Spearman's rho。\n**M3.** Webb (2023) 年份需确认。\n**M4.** Appendix R 阈值选择缺乏理论依据。\n**M5.** Conclusion 过于简短。\n\n## 4. Questions\n\n**Q1.** DAF 在 Δ_nd < 0 的 task types 中如何解释？\n**Q2.** 105 deaths 全来自 `focus on [object]`——death avoidance 是否实质上是 single action avoidance？\n**Q3.** Grounding intervention 的 per-task variation 对 DAF decomposition 有何影响？\n**Q4.** 3.7% internal-preferred base rate → always-deterministic 是否已接近最优？\n**Q5.** Llama cross-model replication 的 DAF 是多少？\n\n## 5. Missing References\n\n- Cost-aware routing 中的 risk-sensitive 策略\n- Agent failure taxonomy (Wang et al. 2024)\n- Noisy label learning 文献 (Natarajan et al. 2013)\n\n## 6. Overall Assessment\n\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Reproducibility | 4.5/5 |"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下关键分歧点：\n1. R1 给 Overall 3.5 (Borderline Conference)，你给 3.0 (Findings)——0.5 分差距主要来自哪里？\n2. R1 的 Excitement 3.5/5 vs 你的 2.5/5——你是否低估了问题定义本身的价值？\n3. R1-S1 认为\"问题定义精准且有价值\"——这是否缓解了你 W1 (obvious in hindsight) 的担忧？\n4. R1-N3 (episode-to-step label projection) 提出了 router 失败的另一种解释（label noise 而非 signal inherently not step-level）——你是否同意这削弱了 router diagnostic 的诊断价值？\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## 1. Summary\n\n本文提出一个 episode-level counterfactual diagnostic framework，用 pure-strategy trajectory 对比量化模块化 LLM agent 中 routing 信号的来源。核心发现：在 ScienceWorld 的 245 episode pairs（11 task types）中，78.9% 的 non-tie routing labels 源于 death asymmetry。Death Avoidance Factor (DAF) 在默认 penalty（P=100）下达 90.4%。\n\n论文问了一个好问题（routing 信号到底是什么？），给出了一个清晰且 largely convincing 的回答，实验工作量大（21 页含详细附录），但在统计推断、跨环境证据、router 实用性方面有不可忽视的缺陷。\n\n## 2. Strengths\n\n**S1. 问题定义精准且有价值。** 现有 routing 文献关注\"怎么 route\"，本文追问\"routing 到底在 route 什么信号\"——这是一个被忽视但影响 router 设计方向的诊断性问题。\n\n**S2. Pure-strategy counterfactual 设计干净。** 控制相同 random seed + initial conditions，是 well-identified 的因果推断设计。\n\n**S3. DAF 分解数学上 clean。** Eq. (4)-(5) 推导正确。论文明确指出 DAF 随 P 单调递增是数学后果。\n\n**S4. Robustness checks 全面。** Leave-one-task-out、penalty sensitivity、cross-model replication、anti-cherry-picking、8-seed robustness。\n\n**S5. SCI 有效回应了信号集中度质疑。**\n\n**S6. Limitations 坦诚且具体。**\n\n## 3. Weaknesses\n\n### Must-Fix\n\n**N1 [critical] DAF headline number 的误导性。**\n- Abstract 和 Section 3.1 以 \"DAF = 90.4%\" 作为 headline，与 penalty-independent 的 78.9% 并列，读者易误解 90.4% 是独立于 penalty 的经验发现。\n- 建议：Abstract 以 78.9% 为 primary，DAF 降为补充。\n\n**N2 [critical] Cluster bootstrap K=11 低于公认阈值。**\n- Cameron et al. (2008) 建议 K ≥ 20-40。Webb (2023) Monte Carlo 模拟显示 K < 20 时 rejection rate 仍有 size distortion。2^11 = 2048 排列的 p=0.002 颗粒度很粗。Cohen's d = 3.02 在小 K 下可能受 outlier 影响。\n- 建议：正文讨论 K=11 vs K≥40 建议；报告 leave-one-cluster-out sensitivity 的最差情况。\n\n**N3 [critical] Episode-to-step label projection 的系统性噪声。**\n- 97.4% step-level ties → 27.7% mislabeling + 60.3% pre-event neutral → 仅 ~12% informative + correctly-labeled signal。Router probe 失败可能是 label noise 所致，而非 signal inherently not step-level learnable。\n- 建议：实验 step-level label refinement baseline（如只用 death event 附近 steps 训练）；或精确量化 noise 的影响。\n\n### Should-Fix\n\n**W1 [warning] Cross-environment probes 措辞过强。** MATH 是 unfalsifiable null result，ALFWorld 验证了不同机制。应定位为 \"consistency checks\" 而非 \"cross-domain validation\"。\n\n**W2 [warning] Pure-strategy 设计的外部效度。** 现实 routing 中途切换可能避免 death，pure-strategy 可能 overestimate death asymmetry。\n\n**W3 [warning] Reflexion dose-response 统计功效。** N=5 trials，power 是否足以区分 genuine ceiling vs insufficient trials？\n\n**W4 [warning] Router \"diagnostic probe\" 定位与 contribution claim 的张力。** Step-level 56-59% ≈ chance，应更明确框架为 negative result。\n\n### Minor\n\n**M1.** Table 1 weighting scheme 未明确。\n**M2.** Figure 2 应在 caption 报告 Spearman's rho。\n**M3.** Webb (2023) 年份需确认。\n**M4.** Appendix R 阈值选择缺乏理论依据。\n**M5.** Conclusion 过于简短。\n\n## 4. Questions\n\n**Q1.** DAF 在 Δ_nd < 0 的 task types 中如何解释？\n**Q2.** 105 deaths 全来自 `focus on [object]`——death avoidance 是否实质上是 single action avoidance？\n**Q3.** Grounding intervention 的 per-task variation 对 DAF decomposition 有何影响？\n**Q4.** 3.7% internal-preferred base rate → always-deterministic 是否已接近最优？\n**Q5.** Llama cross-model replication 的 DAF 是多少？\n\n## 5. Missing References\n\n- Cost-aware routing 中的 risk-sensitive 策略\n- Agent failure taxonomy (Wang et al. 2024)\n- Noisy label learning 文献 (Natarajan et al. 2013)\n\n## 6. Overall Assessment\n\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Reproducibility | 4.5/5 |"
  }
}
```

</details>

---


### Tool result

_source line 1727 · 2026-05-19T15:51:58.331386+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1309
}
```

</details>

---


### Assistant

_source line 1728 · 2026-05-19T15:52:02.086396+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 144

## Round 144

16 recorded events


### User

_source line 1729 · 2026-05-19T15:52:03.080114+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

核心评判：**Overall 3 (Findings)**，Confidence 4/5。

主要判断依据：
- **方法论扎实**（bootstrap, cluster-robust inference, pure-strategy counterfactual design），统计质量高于同类工作
- **核心发现 novelty 不足**——在 P=−100 death penalty + internal strategy death rate ~43% vs. deterministic ~10% 的设定下，death avoidance dominate routing 是高度可预见的。论文自身承认 DAF 是 "mathematical consequence rather than empirical finding"
- **Framing 张力**未解决——标题聚焦 finding，Contribution 1 聚焦 framework，Conclusion 仅 2 句话
- **Generalizability 受限**——单环境主实验 + 两个浅层 cross-environment probe 难以支撑一般性论述

三个 Must-Fix：novelty 论证（W1）、framing 一致性（W2）、single-environment + overclaiming（W3）。四个 Should-Fix：术语歧义（W4）、Conclusion 过短（W5）、缺 penalty variation 实验（W6）、Safe RL 讨论不足（W7）。

---

[Reviewer 1 审稿结果]:
审稿完成。总结：

**Overall: 3.5 (Borderline Conference)**

3 个 Must-Fix 问题：
- **N1**: DAF = 90.4% 是 penalty 单调递增的数学后果，不应作为 headline finding，78.9% label fraction 才是 robust metric
- **N2**: K=11 cluster bootstrap 低于 Cameron et al. (2008) 建议的 K≥40，wild cluster bootstrap 在小 K 下的适用性辩护不足
- **N3**: Episode-to-step label projection 产生 ~88% 的 noise/uninformative rate，router near-chance accuracy 可能是 label noise 而非 signal inherently unlearnable

4 个 Should-Fix：cross-environment probes 定位需更精确（W1）、pure-strategy 外部效度（W2）、Reflexion N=5 功效（W3）、router "diagnostic probe" vs negative result 的 framing 张力（W4）。

如果 N1 和 N2 在 revision 中充分回应，倾向上调至 4.0 (Conference)。

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

_source line 1730 · 2026-05-19T15:52:35.460215+00:00_

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

_source line 1731 · 2026-05-19T15:52:35.460658+00:00_

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

_source line 1732 · 2026-05-19T15:52:35.561294+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"running\", \"started_at\": \"2026-05-19T15:44:21.540507+00:00\"}, \"error\": null, \"metadata\": {}}"}

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


### Tool result

_source line 1733 · 2026-05-19T15:52:35.561717+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-19T15:44:22.550490+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_f6bffc7e8351600df8091f08a63cd5a0\", \"skipped_at\": \"2026-05-19T15:46:01.656597+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1734 · 2026-05-19T15:52:58.686453+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
  "description": "Count lines in review issues file"
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
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
    "description": "Count lines in review issues file"
  }
}
```

</details>

---


### Tool result

_source line 1735 · 2026-05-19T15:52:58.839182+00:00_

721 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1736 · 2026-05-19T15:53:05.221537+00:00_

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

_source line 1737 · 2026-05-19T15:53:05.272721+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"running\", \"started_at\": \"2026-05-19T15:44:21.540507+00:00\"}, \"error\": null, \"metadata\": {}}"}

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


### Tool call

_source line 1738 · 2026-05-19T15:56:23.891320+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "## Round 19 Review Issues (fresh review, 2026-05-19)\n\n# =============================================\n# Resolved issues from prior rounds\n# =============================================\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化 27.7% mislabeling fraction\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld + MATH N 标注不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及 minority-class diversity confound\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n# =============================================\n# Open / in_progress issues (updated R19)\n# =============================================\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调 DAF 数值\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18 fresh review 再次列为 critical Must-Fix。根因：§3.1 文本顺序未修正。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19 fresh review 强共识 Must-Fix。R1-N1: Abstract 和 §3.1 仍以 DAF=90.4% 为 headline，与 78.9% 并列呈现，读者易误解为独立于 penalty 的经验发现。§3.1 虽在段落中部提到 DAF 是 derived quantity，但首段结构未修正。R2 完全同意。\"\n  action_items:\n    - round: 13\n      action: \"对 cluster bootstrap K=11 做更诚实讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 18\n      action: \"结构性修复：§3.1 首句以 78.9% 开头，DAF 移至段落中后部\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Abstract 以 78.9% label fraction 为 primary metric 开头，DAF=90.4% 降为补充说明；§3.1 段落重组；增加 DAF 在 Δ_nd<0 边界行为的讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11、per-task n=20\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R1 再提为 Critical。R2 rebut 降级。Director 裁决：维持 warning。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-N2 升为 Critical。Cameron et al. (2008) K≥40 vs 本文 K=11。Webb (2023) Monte Carlo 显示 K<20 有 size distortion。2^11=2048 排列颗粒度粗。Cohen's d=3.02 在小 K 下可受 outlier 影响。R2 同意关切但未列为 critical。Director 裁决：升为 critical（R1 论据充分）。\"\n  action_items:\n    - round: 18\n      action: \"正文以 non-clustered bootstrap 为主要推断方式，cluster bootstrap 标注为 conservative sensitivity check\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"正文增加 K=11 vs K≥40 的显式讨论；引用 leave-one-cluster-out 最差情况（DAF 75.9%）；讨论 Cohen's d=3.02 在小 K 下的可解释性；将 non-clustered bootstrap 作为主推断，cluster bootstrap 作为 conservative check\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [2]\n      note: \"R18: R2 再提。R1 rebut: 数字是证据。\"\n    - round: 19\n      reviewers: [2]\n      note: \"R19: R2-W8 再提。78.9%、245、Qwen2.5-7B、11 task types、DAF 90.4%、95% CI、P=100、δ=0.265 全部堆在一段。R1 未反对。\"\n  action_items:\n    - round: 19\n      action: \"Abstract 重组为 concept-first, numbers-second：前半段用概念性语言阐述 framework 和 key insight，后半段给关键数字；CI 和 δ 值移到正文\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: §4 safe RL 段仍仅一句话带过五篇引用。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W7 再提。Safe RL 段列举了引用但无实质性讨论。缺少 CMDP 框架（Altman 1999）与 death avoidance 的映射、CVaR 与 catastrophic failure 的关系。R1 建议补充 noisy label learning 文献。\"\n  action_items:\n    - round: 19\n      action: \"§4 Safe RL 段扩展至 5+ 句：(1) 补 Altman 1999 CMDP，讨论 death avoidance 作为 implicit constraint 的映射；(2) 补 Mihatsch & Neuneier 2002 risk-sensitive RL；(3) 讨论 routing 作为 implicit safety mechanism vs explicit safe RL 的区别\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: non-triviality 论证不足。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W1 列为 Critical Must-Fix——P=100 + death rate 43% vs 10% 设定下 death dominance 高度可预见。§5 Non-triviality 论证只证明 robustness 而非 non-obviousness。R1 部分 rebut——问题定义本身有价值（Excitement 3.5 vs R2 的 2.5），但承认 finding 可预见性。分歧保留在报告中。\"\n  action_items:\n    - round: 19\n      action: \"三角度强化 non-triviality：(1) 从 routing 文献的 prior assumptions 出发——现有工作假设多样化信号，本文证明单一信号主导；(2) intervention resistance 的 non-predictability——4 轴干预均无法消除，这是 setup 无法预见的；(3) cross-model δ stability——两个模型 ~42% internal death rate 的一致性是结构性发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。被 generalizability 大议题覆盖。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-W1 和 R2-W3 均提及。MATH 无 death→null result (unfalsifiable)；ALFWorld 是 information asymmetry 非 computation mode switch。Abstract 'confirmed across two cross-domain probes' 措辞过强。共识：应定位为 'consistency checks' 或 'boundary probes'，非 'validation'。\"\n  action_items:\n    - round: 19\n      action: \"§3.4 开头明确三个环境 deterministic 含义不同；Abstract 调整措辞为 boundary probes/consistency checks\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未单独提及。被 episode→step gap 整体覆盖。\"\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18 Excitement 2.5-3/5。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1 Excitement 3.5/5（问题定义有价值）vs R2 Excitement 2.5/5（finding obvious）。分歧未收敛。与 R14-W1 合并处理。\"\n  action_items:\n    - round: 19\n      action: \"与 R14-W1 合并：三角度 non-triviality 论证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W3 提及 single-environment + 63% exclusion。Anti-cherry-picking analysis (Appendix C, 18/19 excluded types 也 death-dominated, ΔDR=+38.2pp) 被两位 reviewer 认可但不足以完全消除 concern。\"\n  action_items:\n    - round: 19\n      action: \"§3 开头段保持当前 scope limitation 声明；确保不出现暗示 30 task types 全部适用的措辞\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R16-N3\"\n  summary: \"缺少 permadeath 环境 replication\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W3 强调 MATH 和 ALFWorld 不能替代第二个 death-prone 环境。R1-W1 同意 cross-env evidence 有限。MiniHack negative (0% death), Crafter negative (100% death both) 仅作为 boundary conditions。NetHack 仍为 future work。\"\n  action_items:\n    - round: 19\n      action: \"维持 future work 定位；§5 Framework applicability 段明确 NetHack 为 most direct replication target\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未单独提及。§3.3 已报告 72B DAF=92.4%（7B: 90.4%）with decomposition。可能已修复。\"\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"连续多轮未被提出。待确认是否已修复。\"\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"连续多轮未提及。待确认。\"\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。待确认。\"\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未独立提出。§3.1 已讨论 binary structure（10/11 death-prone → 100% death labels, 1/11 → 0%）。被 DAF framing 议题覆盖。\"\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未独立提出。§3.1 已报告 P=0 时 54 sole-signal labels 退化为 ties，剩余 41 non-tie labels 中 21 (51.2%) 仍涉及 death asymmetry。可能已修复。\"\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R19: R1-W2 再提。Pure-strategy 让 internal strategy 连续 30 steps 积累 hallucination errors，可能 amplify death rate。Mixed-strategy routing 中途切换可能避免 death。需 back-of-envelope 估计或 sensitivity analysis。\"\n  action_items:\n    - round: 19\n      action: \"Limitations 或 Discussion 增加 pure-strategy vs mixed-strategy gap 的定量估计（如基于 death event step distribution 估算中途切换的 death rate 下降）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R17-W2\"\n  summary: \"Figure 1 caption 缺 mathematical consequence caveat\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R19: R1-M2 建议 Figure 2 caption 增加 Spearman's rho。相关但不完全相同。\"\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）。已修复。\"\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-M3 和 R2-M4 均提及 webb-2023 年份可能有误（OpenAlex 匹配到 2014 working paper, 2023 journal version）。\"\n  action_items:\n    - round: 19\n      action: \"确认 Webb 引用为 2023 journal version (Canadian Journal of Economics, 56(3)) 并在 bib 中标注完整信息\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性，框架适用边界未在 Method 中正式讨论\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"强共识。Router ≈ chance。97.4% step-level tie rate。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-N3 升为 Critical。精确量化：97.4% step-level ties → 27.7% mislabeling + 60.3% pre-event neutral → 仅 ~12% informative + correctly-labeled signal。Router near-chance (56-59%) 可能是 label noise 而非 signal inherently unlearnable——这削弱了 §3.6 作为 diagnostic probe 的诊断价值。R2 部分同意。\"\n  action_items:\n    - round: 18\n      action: \"§2 末尾增加 Scope of Episode-Level Analysis 段落\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"(1) §3.6 明确区分两种解释：label noise vs signal not step-level learnable；(2) 讨论 step-level label refinement baseline 的可能性（如 proximity-to-death 加权）；(3) 报告 episode-level split 在正文而非仅 Appendix\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R19: R1-W4 再提——router 'diagnostic probe' 定位与 contribution claim 张力。Step-level near-chance 但 4B episode-level 有改善，应更明确框架为 negative result。\"\n  action_items:\n    - round: 19\n      action: \"§3.6 明确将 router 实验框架为 negative result；讨论 what kind of router architecture might bypass the granularity mismatch\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足: Reflexion N=5\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R19: R1-W3 再提。N=5 trials × 10 death-prone tasks = 50 points。MDE ~14pp (α=0.05, 80% power)。N=5 功效是否足以区分 genuine ceiling vs insufficient trials？需报告 power analysis 并标注 evidence 为 suggestive 而非 conclusive。\"\n  action_items:\n    - round: 19\n      action: \"报告 N=5 power analysis；将 plateau conclusion 标注为 suggestive evidence\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W4 再提为 Should-Fix。NLP 领域 modality 通常指 data modality (text/vision/audio)。论文已部分使用 computation mode 和 strategy，但未统一。\"\n  action_items:\n    - round: 19\n      action: \"全文统一：modality → computation mode（仅在 internal/deterministic 语境下）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-Q2 和 R2-Q4 均追问——105 deaths 全来自 focus on [object] 误用，death avoidance 是否等价于 single-action bug avoidance？Grounding ablation (48%→29%) 减少但不消除。§5 Anatomy 段已讨论但 implication 可更强。\"\n  action_items:\n    - round: 19\n      action: \"§5 Anatomy 段增加讨论：(1) 这是 grounding failure 的 symptom 而非 full story——即使 fix 这一个 pattern，其他 grounding failures 可能出现；(2) action filtering 降至 29% 但 ≥12pp residual gap 说明 death vulnerability 有更深层原因\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。论文已在 Appendix 开头增加 Overview with hyperlinks。可能已修复。\"\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19: §3.1 已改为 'sole-signal labels' 并在括号中定义。可能已修复。\"\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。待确认。\"\n\n# =============================================\n# Round 19 New Issues\n# =============================================\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清——标题/Abstract/Contributions/Conclusion 各自重心不同\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W2 首提为 Critical。标题聚焦 finding，Contribution 1 聚焦 framework，Abstract 同时强调两者，Conclusion 仅 2 句 finding-oriented。R1 同意 framing 需统一。共识：必须选择一个主线贯穿始终。\"\n  action_items:\n    - round: 19\n      action: \"选择 framework-centric 或 finding-centric 主线，统一标题/Abstract/Contributions/Conclusion。如选 framework：标题强调方法论，ScienceWorld 作为 case study；如选 finding：弱化 framework contribution claim，加强 non-triviality 论证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证——DAF vs P 分析仅为数学推导\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W6 首提。§2.4 和 Appendix K 的 DAF vs P 分析是数学推导而非实验结果。DAF 公式假设 Δ_nd 和 death rates 不随 P 变化，但 agent behavior 可能因 penalty magnitude 不同而改变。至少需要 P=10 和 P=50 的实际实验。R1 未反对。\"\n  action_items:\n    - round: 19\n      action: \"在 P=10 和 P=50（或至少一个非默认 P 值）下运行实际 ScienceWorld 实验，验证 DAF 公式预测与实际是否匹配\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W2\"\n  summary: \"Conclusion（§6）过于简短——仅 2 句话，不匹配 long paper 标准\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W5 首提，R1-M5 同意。2 句话的 Conclusion 缺少 broader implications、framework 局限性反思、对不同社区（safe RL, agent design）的启示。\"\n  action_items:\n    - round: 19\n      action: \"Conclusion 扩展至 ~0.5 页：key takeaways, practical implications for agent designers, framework 适用边界, future directions\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-M1\"\n  summary: \"62% tie rate (150/245 episodes) 的含义未充分讨论——routing 实际价值存疑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-M1 和 R2-Q2。245 episodes 中 150 是 no-preference（两种 strategy 同分或同死）。高 tie rate 意味着在大多数情况下 routing 选择无差异——这本身是对 routing 价值的质疑。论文未充分讨论。\"\n  action_items:\n    - round: 19\n      action: \"§3.1 或 §5 增加对 62% tie rate 含义的讨论——在大多数 episodes 中 routing 无差异，仅在 38% episodes 中有信号，且其中 78.9% 来自 death avoidance\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999 CMDP, Mihatsch & Neuneier 2002, noisy label learning\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2: Altman (1999) CMDP, Mihatsch & Neuneier (2002) risk-sensitive RL。R1: Natarajan et al. (2013) noisy label learning（与 router 27.7% mislabeling rate 相关）。\"\n  action_items:\n    - round: 19\n      action: \"补充 3 条 missing references 并在相应段落中讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "## Round 19 Review Issues (fresh review, 2026-05-19)\n\n# =============================================\n# Resolved issues from prior rounds\n# =============================================\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑泛化——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"标题和 Contribution 措辞已恰当限定 scope\"\n  resolution_round: 15\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化 27.7% mislabeling fraction\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld + MATH N 标注不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及 minority-class diversity confound\"\n  resolution_round: 16\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n# =============================================\n# Open / in_progress issues (updated R19)\n# =============================================\n\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调 DAF 数值\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 resolved. 78.9% 为 primary metric，DAF 降级为 derived quantity。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18 fresh review 再次列为 critical Must-Fix。根因：§3.1 文本顺序未修正。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19 fresh review 强共识 Must-Fix。R1-N1: Abstract 和 §3.1 仍以 DAF=90.4% 为 headline，与 78.9% 并列呈现，读者易误解为独立于 penalty 的经验发现。§3.1 虽在段落中部提到 DAF 是 derived quantity，但首段结构未修正。R2 完全同意。\"\n  action_items:\n    - round: 13\n      action: \"对 cluster bootstrap K=11 做更诚实讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 18\n      action: \"结构性修复：§3.1 首句以 78.9% 开头，DAF 移至段落中后部\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Abstract 以 78.9% label fraction 为 primary metric 开头，DAF=90.4% 降为补充说明；§3.1 段落重组；增加 DAF 在 Δ_nd<0 边界行为的讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11、per-task n=20\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: R1 再提为 Critical。R2 rebut 降级。Director 裁决：维持 warning。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-N2 升为 Critical。Cameron et al. (2008) K≥40 vs 本文 K=11。Webb (2023) Monte Carlo 显示 K<20 有 size distortion。2^11=2048 排列颗粒度粗。Cohen's d=3.02 在小 K 下可受 outlier 影响。R2 同意关切但未列为 critical。Director 裁决：升为 critical（R1 论据充分）。\"\n  action_items:\n    - round: 18\n      action: \"正文以 non-clustered bootstrap 为主要推断方式，cluster bootstrap 标注为 conservative sensitivity check\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"正文增加 K=11 vs K≥40 的显式讨论；引用 leave-one-cluster-out 最差情况（DAF 75.9%）；讨论 Cohen's d=3.02 在小 K 下的可解释性；将 non-clustered bootstrap 作为主推断，cluster bootstrap 作为 conservative check\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [2]\n      note: \"R18: R2 再提。R1 rebut: 数字是证据。\"\n    - round: 19\n      reviewers: [2]\n      note: \"R19: R2-W8 再提。78.9%、245、Qwen2.5-7B、11 task types、DAF 90.4%、95% CI、P=100、δ=0.265 全部堆在一段。R1 未反对。\"\n  action_items:\n    - round: 19\n      action: \"Abstract 重组为 concept-first, numbers-second：前半段用概念性语言阐述 framework 和 key insight，后半段给关键数字；CI 和 δ 值移到正文\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: §4 safe RL 段仍仅一句话带过五篇引用。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W7 再提。Safe RL 段列举了引用但无实质性讨论。缺少 CMDP 框架（Altman 1999）与 death avoidance 的映射、CVaR 与 catastrophic failure 的关系。R1 建议补充 noisy label learning 文献。\"\n  action_items:\n    - round: 19\n      action: \"§4 Safe RL 段扩展至 5+ 句：(1) 补 Altman 1999 CMDP，讨论 death avoidance 作为 implicit constraint 的映射；(2) 补 Mihatsch & Neuneier 2002 risk-sensitive RL；(3) 讨论 routing 作为 implicit safety mechanism vs explicit safe RL 的区别\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: non-triviality 论证不足。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W1 列为 Critical Must-Fix——P=100 + death rate 43% vs 10% 设定下 death dominance 高度可预见。§5 Non-triviality 论证只证明 robustness 而非 non-obviousness。R1 部分 rebut——问题定义本身有价值（Excitement 3.5 vs R2 的 2.5），但承认 finding 可预见性。分歧保留在报告中。\"\n  action_items:\n    - round: 19\n      action: \"三角度强化 non-triviality：(1) 从 routing 文献的 prior assumptions 出发——现有工作假设多样化信号，本文证明单一信号主导；(2) intervention resistance 的 non-predictability——4 轴干预均无法消除，这是 setup 无法预见的；(3) cross-model δ stability——两个模型 ~42% internal death rate 的一致性是结构性发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。被 generalizability 大议题覆盖。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-W1 和 R2-W3 均提及。MATH 无 death→null result (unfalsifiable)；ALFWorld 是 information asymmetry 非 computation mode switch。Abstract 'confirmed across two cross-domain probes' 措辞过强。共识：应定位为 'consistency checks' 或 'boundary probes'，非 'validation'。\"\n  action_items:\n    - round: 19\n      action: \"§3.4 开头明确三个环境 deterministic 含义不同；Abstract 调整措辞为 boundary probes/consistency checks\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未单独提及。被 episode→step gap 整体覆盖。\"\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18 Excitement 2.5-3/5。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1 Excitement 3.5/5（问题定义有价值）vs R2 Excitement 2.5/5（finding obvious）。分歧未收敛。与 R14-W1 合并处理。\"\n  action_items:\n    - round: 19\n      action: \"与 R14-W1 合并：三角度 non-triviality 论证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W3 提及 single-environment + 63% exclusion。Anti-cherry-picking analysis (Appendix C, 18/19 excluded types 也 death-dominated, ΔDR=+38.2pp) 被两位 reviewer 认可但不足以完全消除 concern。\"\n  action_items:\n    - round: 19\n      action: \"§3 开头段保持当前 scope limitation 声明；确保不出现暗示 30 task types 全部适用的措辞\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R16-N3\"\n  summary: \"缺少 permadeath 环境 replication\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W3 强调 MATH 和 ALFWorld 不能替代第二个 death-prone 环境。R1-W1 同意 cross-env evidence 有限。MiniHack negative (0% death), Crafter negative (100% death both) 仅作为 boundary conditions。NetHack 仍为 future work。\"\n  action_items:\n    - round: 19\n      action: \"维持 future work 定位；§5 Framework applicability 段明确 NetHack 为 most direct replication target\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未单独提及。§3.3 已报告 72B DAF=92.4%（7B: 90.4%）with decomposition。可能已修复。\"\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"连续多轮未被提出。待确认是否已修复。\"\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"连续多轮未提及。待确认。\"\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。待确认。\"\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未独立提出。§3.1 已讨论 binary structure（10/11 death-prone → 100% death labels, 1/11 → 0%）。被 DAF framing 议题覆盖。\"\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未独立提出。§3.1 已报告 P=0 时 54 sole-signal labels 退化为 ties，剩余 41 non-tie labels 中 21 (51.2%) 仍涉及 death asymmetry。可能已修复。\"\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R19: R1-W2 再提。Pure-strategy 让 internal strategy 连续 30 steps 积累 hallucination errors，可能 amplify death rate。Mixed-strategy routing 中途切换可能避免 death。需 back-of-envelope 估计或 sensitivity analysis。\"\n  action_items:\n    - round: 19\n      action: \"Limitations 或 Discussion 增加 pure-strategy vs mixed-strategy gap 的定量估计（如基于 death event step distribution 估算中途切换的 death rate 下降）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R17-W2\"\n  summary: \"Figure 1 caption 缺 mathematical consequence caveat\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R19: R1-M2 建议 Figure 2 caption 增加 Spearman's rho。相关但不完全相同。\"\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）。已修复。\"\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-M3 和 R2-M4 均提及 webb-2023 年份可能有误（OpenAlex 匹配到 2014 working paper, 2023 journal version）。\"\n  action_items:\n    - round: 19\n      action: \"确认 Webb 引用为 2023 journal version (Canadian Journal of Economics, 56(3)) 并在 bib 中标注完整信息\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性，框架适用边界未在 Method 中正式讨论\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"强共识。Router ≈ chance。97.4% step-level tie rate。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-N3 升为 Critical。精确量化：97.4% step-level ties → 27.7% mislabeling + 60.3% pre-event neutral → 仅 ~12% informative + correctly-labeled signal。Router near-chance (56-59%) 可能是 label noise 而非 signal inherently unlearnable——这削弱了 §3.6 作为 diagnostic probe 的诊断价值。R2 部分同意。\"\n  action_items:\n    - round: 18\n      action: \"§2 末尾增加 Scope of Episode-Level Analysis 段落\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"(1) §3.6 明确区分两种解释：label noise vs signal not step-level learnable；(2) 讨论 step-level label refinement baseline 的可能性（如 proximity-to-death 加权）；(3) 报告 episode-level split 在正文而非仅 Appendix\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R19: R1-W4 再提——router 'diagnostic probe' 定位与 contribution claim 张力。Step-level near-chance 但 4B episode-level 有改善，应更明确框架为 negative result。\"\n  action_items:\n    - round: 19\n      action: \"§3.6 明确将 router 实验框架为 negative result；讨论 what kind of router architecture might bypass the granularity mismatch\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足: Reflexion N=5\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R19: R1-W3 再提。N=5 trials × 10 death-prone tasks = 50 points。MDE ~14pp (α=0.05, 80% power)。N=5 功效是否足以区分 genuine ceiling vs insufficient trials？需报告 power analysis 并标注 evidence 为 suggestive 而非 conclusive。\"\n  action_items:\n    - round: 19\n      action: \"报告 N=5 power analysis；将 plateau conclusion 标注为 suggestive evidence\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W4 再提为 Should-Fix。NLP 领域 modality 通常指 data modality (text/vision/audio)。论文已部分使用 computation mode 和 strategy，但未统一。\"\n  action_items:\n    - round: 19\n      action: \"全文统一：modality → computation mode（仅在 internal/deterministic 语境下）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R1-Q2 和 R2-Q4 均追问——105 deaths 全来自 focus on [object] 误用，death avoidance 是否等价于 single-action bug avoidance？Grounding ablation (48%→29%) 减少但不消除。§5 Anatomy 段已讨论但 implication 可更强。\"\n  action_items:\n    - round: 19\n      action: \"§5 Anatomy 段增加讨论：(1) 这是 grounding failure 的 symptom 而非 full story——即使 fix 这一个 pattern，其他 grounding failures 可能出现；(2) action filtering 降至 29% 但 ≥12pp residual gap 说明 death vulnerability 有更深层原因\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。论文已在 Appendix 开头增加 Overview with hyperlinks。可能已修复。\"\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19: §3.1 已改为 'sole-signal labels' 并在括号中定义。可能已修复。\"\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。待确认。\"\n\n# =============================================\n# Round 19 New Issues\n# =============================================\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清——标题/Abstract/Contributions/Conclusion 各自重心不同\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W2 首提为 Critical。标题聚焦 finding，Contribution 1 聚焦 framework，Abstract 同时强调两者，Conclusion 仅 2 句 finding-oriented。R1 同意 framing 需统一。共识：必须选择一个主线贯穿始终。\"\n  action_items:\n    - round: 19\n      action: \"选择 framework-centric 或 finding-centric 主线，统一标题/Abstract/Contributions/Conclusion。如选 framework：标题强调方法论，ScienceWorld 作为 case study；如选 finding：弱化 framework contribution claim，加强 non-triviality 论证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证——DAF vs P 分析仅为数学推导\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W6 首提。§2.4 和 Appendix K 的 DAF vs P 分析是数学推导而非实验结果。DAF 公式假设 Δ_nd 和 death rates 不随 P 变化，但 agent behavior 可能因 penalty magnitude 不同而改变。至少需要 P=10 和 P=50 的实际实验。R1 未反对。\"\n  action_items:\n    - round: 19\n      action: \"在 P=10 和 P=50（或至少一个非默认 P 值）下运行实际 ScienceWorld 实验，验证 DAF 公式预测与实际是否匹配\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W2\"\n  summary: \"Conclusion（§6）过于简短——仅 2 句话，不匹配 long paper 标准\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W5 首提，R1-M5 同意。2 句话的 Conclusion 缺少 broader implications、framework 局限性反思、对不同社区（safe RL, agent design）的启示。\"\n  action_items:\n    - round: 19\n      action: \"Conclusion 扩展至 ~0.5 页：key takeaways, practical implications for agent designers, framework 适用边界, future directions\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-M1\"\n  summary: \"62% tie rate (150/245 episodes) 的含义未充分讨论——routing 实际价值存疑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-M1 和 R2-Q2。245 episodes 中 150 是 no-preference（两种 strategy 同分或同死）。高 tie rate 意味着在大多数情况下 routing 选择无差异——这本身是对 routing 价值的质疑。论文未充分讨论。\"\n  action_items:\n    - round: 19\n      action: \"§3.1 或 §5 增加对 62% tie rate 含义的讨论——在大多数 episodes 中 routing 无差异，仅在 38% episodes 中有信号，且其中 78.9% 来自 death avoidance\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999 CMDP, Mihatsch & Neuneier 2002, noisy label learning\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2: Altman (1999) CMDP, Mihatsch & Neuneier (2002) risk-sensitive RL。R1: Natarajan et al. (2013) noisy label learning（与 router 27.7% mislabeling rate 相关）。\"\n  action_items:\n    - round: 19\n      action: \"补充 3 条 missing references 并在相应段落中讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1739 · 2026-05-19T15:56:23.993328+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 23814}, \"error\": \"\"}"}

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

_source line 1740 · 2026-05-19T15:56:29.137040+00:00_

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

_source line 1741 · 2026-05-19T15:56:29.187683+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"timeout\", \"elapsed_seconds\": 727}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---
