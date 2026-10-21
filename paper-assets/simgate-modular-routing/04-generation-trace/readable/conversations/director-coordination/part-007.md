# Director coordination — Part 7 of 9

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../director-coordination.md) · [Part 8 →](part-008.md) · [Structured JSON](../../../sessions/53/532e22af863d2a24e206.json)

## Round 168

### User

_source line 2063 · 2026-05-21T15:05:56.555346+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

### N1: 核心发现的新颖性存疑——death dominance 在实验设置下是可预期的

**[AGREE]（部分同意，但认为 R2 有所过度表述）**

R2 的核心论点成立：oracle simulator vs. 会幻觉的 LLM 在 −100 penalty 下，death asymmetry 的 *存在* 确实是可预期的。这与我在 W1 中提出的 DAF tautological 倾向一致。

但我认为 R2 略微低估了以下贡献的 surprise value：
- **Prevalence 的量化**（78.9% non-tie labels 源自 death asymmetry）并非显而易见。一个合理的 prior 假设是：deterministic 策略在非死亡维度上也有显著优势（如多步推理准确性、state tracking），这些非死亡差异可能贡献更多 routing signal。论文表明非死亡差异 Δ_nd ≈ 2.84 是 near-uniform across task types（Appendix K, page 17），这是一个需要实证才能确认的发现。
- **Router negative result**（§3.6）是真正的 non-trivial finding：即便 death dominance 可预期，"step-level router 无法利用这一信号"这一结论需要实验验证，不能从设置预测。
- §5 的 non-triviality 论证（72B scaling 不消除、Reflexion ceiling、inverted-U）确如 R2 所说是关于 persistence 而非 existence，但 persistence 本身有一定 novelty——one might expect 72B 或 Reflexion 能实质性降低 death rate。

综合来看，我同意 R2 对 *framing* 的批评：论文将一个"部分可预期的发现"包装为"surprising insight"，但其实证贡献（量化 + router failure）仍有价值。这是 Findings 而非 Conference 水平的核心原因。

---

### N2: "框架通用性" 的 claim 缺乏实质性验证

**[AGREE]**

完全同意，这与我的 W2 观点一致。MATH（84.4% no-preference）和 ALFWorld（DAF=0%）作为 boundary probes 只能展示框架的 *诊断能力多样性*，不能证明框架在 non-obvious 场景下产出 non-trivial insights 的能力。

补充一点 R2 未明确指出的：论文 bib 中有 NetHack (nethack-2020)、MiniHack (minihack-2021)、BALROG (balrog-2025)、Crafter (crafter-2022) 等有 catastrophic failure mechanism 的环境，但均为 orphan references（未在正文引用），暗示作者可能考虑过但放弃了在这些环境上验证。如果论文能在哪怕一个有 permadeath 的替代环境上复现 death dominance，generality claim 将大为加强。

---

### N3: 三条 Contribution 存在依赖关系

**[REBUT]（部分反驳）**

R2 的依赖关系分析（框架→发现→robustness）是正确的，但由此推出"框架 novelty 不足则整体贡献崩塌"过于严厉。

反驳理由：
1. **框架虽然是"结构化消融"，但其 episode-level counterfactual 设计有方法论贡献**。现有 agent routing 工作（RouteLLM, Budget-Aware Routing, MTRouter 等）直接训练 router 而不分析 signal 来源。本文的 episode-level decomposition（death vs. non-death）是第一个系统化的 routing signal 诊断框架。"结构化消融"不等于"没有贡献"——消融分析方法论本身可以是 contribution（如 Transformer 中的 ablation study 传统）。
2. **三条贡献的价值不均等**。我认为最有价值的贡献排序是：(a) router negative result（§3.6, Appendix P）> (b) death prevalence 量化（78.9%）> (c) 框架本身。即使框架的 conceptual novelty 有限，(a) 和 (b) 的实证价值独立存在。
3. 然而，我同意 R2 的隐含判断：**如果只看框架本身的 conceptual depth，确实不足以支撑主会议接收**。这是 Findings 定位的核心理由。

---

## Should-Fix 问题

### W1: 63% 任务类型被排除，7 个 "agent floor" 任务可能代表 death dominance 不成立的 regime

**[AGREE]**

与我的 W3 一致。论文 Appendix C（Table 4）展示了 excluded tasks 的聚合 death dominance 更强，排除了 cherry-picking，但 7 个 "floor" tasks 的 raw scores 和 death rates 未展示。我在审稿中要求作者提供这些数据。

补充 R2 的观点：如果这些 "floor" tasks 中 internal 和 deterministic 的 death rate 都很高（两者都频繁死亡），那就不存在 death *asymmetry*，routing signal 可能由其他因素驱动。这恰恰是 death dominance *不成立* 的有趣案例，值得分析。

---

### W2: "penalty-independent" 表述误导

**[AGREE]**

与我的 Q1 一致。Table 12（Appendix K）清楚显示 DAF 随 P 单调递增（P=0 时 7.4%，P=200 时 97.1%）。论文声称的"penalty-independent"指的是 *label fraction* 而非 DAF，但主文中的表述容易让读者误解。P=0 时 54 个 sole-signal labels（death-only signal episodes）变为 ties，routing signal 的实际形态发生质变。

论文应明确：(a) penalty independence 仅适用于 label direction，不适用于 gap magnitude；(b) 在 P→0 时，routing signal 本身几乎消失（因为 Δ_nd near-uniform），这进一步表明 death 是 ScienceWorld 中 *唯一* 有实质差异的 routing signal 来源。

---

### W3: Conclusion 过于单薄

**[AGREE]**

Page 8 的 Conclusion 确实只有一段约 6-7 行。对于一篇 8 页正文 + 20 个附录的 long paper，Conclusion 应至少包括：(a) 核心发现总结；(b) 主要 limitations 的简要提及；(c) future work 方向。当前版本过于简洁，没有充分反映论文的深度和广度。

---

### W4: Safe RL 相关工作覆盖不足

**[AGREE]**

Related Work §4 的 Safe RL 段落（page 7）确实只有约 3 行，引用了 Altman (1999)、Mihatsch (2002)、García (2015)、Achiam (2017)、Moldovan (2012)、Ruan (2024)、SafeRoute (2025)。但鉴于论文的核心发现是 catastrophic failure avoidance 在 routing signal 中占主导地位，这直接与 Safe RL 的 "避免灾难性状态" 目标（constrained MDPs, risk-sensitive RL）交叉。论文应更详细地讨论：(a) ScienceWorld 中 death avoidance 与 CMDP 的 constraint satisfaction 的对应关系；(b) 为什么 Safe RL 的解决方案（如 CPO）可能不直接适用于 LLM agent routing。

---

### W5: Router negative result 应更 prominently frame 为核心贡献

**[AGREE]**

强烈同意。我在自己的审稿中将 router negative result 列为主要 strength (S4)。§3.6 当前标题是"Router Training: A Negative Result"，位于第 7 页中部，几乎像一个附带发现。但这可能是论文 *最有实践价值* 的贡献——它直接告诉 routing 社区：在 death-dominated 环境中，step-level router 训练是无效的。

建议将 router failure 提升为与 DAF 发现并列的核心 contribution，而非一个 Section 3 的子节。这也能部分缓解 N1（novelty 不足）的批评：即使 death dominance 可预期，router 无法学习这一信号是真正 surprising 的。

---

## Questions

### Q1: DAF>1 时的不直观值——是否有更 robust 的度量？

**[AGREE]（问题合理）**

DAF>1 的语义是"non-death component 与 death component 方向相反"（如 deterministic death rate 更低但 non-death score 也更低）。这在数学上是良定义的，但对读者不直观。R2 建议的 "更 robust 度量" 有价值——例如，可以将 DAF clip 到 [0, 1] 并单独报告 sign-reversal cases，或使用归因比例而非原始分解。

但我认为这不是 critical issue：Table 12（Appendix K）显示 DAF>1 主要出现在 Reflexion baseline（DAF=103.3%），是一个有趣的边界案例而非系统性问题。

---

### Q2: "Deterministic" 统称三种不同的 information advantage

**[AGREE]**

好问题。ScienceWorld 中 deterministic = oracle simulator（ground-truth state transitions）；MATH 中 = code interpreter（验证性计算）；ALFWorld 中 = admissible-action access（可行动作列表）。这三种 "确定性" 的 information advantage 性质不同：oracle simulator 消除幻觉，code interpreter 提供精确计算，admissible-action access 提供动作约束。

用同一个术语 "deterministic" 涵盖这三种机制确实可能误导读者以为它们是同构的。论文在 §2.1 的脚注中有简要解释，但主文应更显式地区分。

---

### Q3: 61.2% ties 暗示 routing 本身价值极为有限？

**[AGREE]（重要观点）**

这是 R2 提出的最有洞察力的问题之一。如果 61.2% 的 episodes 是 ties（150 of 245, Table 2 page 4），那么 routing 最多只能改善 38.8% 的 episodes。这意味着 routing 本身的上限就很低——即使有完美 router，大多数时候两种策略表现一样。

这一观察实际上 *强化* 了论文的诊断价值：不仅 routing signal 被 death dominance 支配，而且大部分 episodes 连 routing signal 都不存在。但论文没有充分讨论这一 implication。建议作者在 Discussion 中增加分析：(a) 61.2% ties 的 task-type 分布；(b) 这对 routing 系统的实际 ROI 意味着什么。

---

### Q4: 0.5B inverted-U claim 基于 n=15 是否足够？

**[AGREE]**

如果 inverted-U relationship（LoRA fine-tuning 先升后降的效果曲线）基于每个数据点仅 n=15 episodes，统计 power 严重不足。我在 W5 中已提出 per-task sample size 偏小的问题。Inverted-U 是一个需要精确估计的非线性关系，n=15 下的 point estimates 噪声太大，难以区分 inverted-U 和 random fluctuation。

---

### Q5: Failure mode 单人标注无 IAA

**[AGREE]**

Appendix N 的 failure mode taxonomy 由单人标注，没有 inter-annotator agreement (IAA)。这在 NLP 社区的审稿标准下是一个 valid concern。论文声称 taxonomy 是 "qualitative illustrations, not formal labels with reliability guarantees"（Appendix N, page 19），这部分缓解了问题，但如果论文基于这些类别做定量分析（如 Figure 5 的 action distribution），IAA 会增强可信度。

不过，这不是 critical issue——taxonomy 在论文中的角色是辅助性的，不影响核心 quantitative claims。

---

## Missing References

### Kumaraguru et al. (2025) "Check Yourself Before You Wreck Yourself"

**[AGREE]（如果存在）**

我无法确认这篇论文的存在。如果它确实讨论了 agent self-monitoring 和 catastrophic failure prevention，则与本文高度相关。建议作者核实并酌情引用。

---

### Step-level credit assignment 近期文献 (2026)

**[REBUT]（部分反驳）**

论文已引用 SALT (salt-2026) 和 CSO (cso-2026) 作为 step-level credit assignment 的代表工作（Related Work §4, page 7）。R2 未给出具体遗漏的论文标题，所以我无法判断是否有重要遗漏。当前覆盖度基本足够，但如果 R2 能提供具体 citation，可以再评估。

---

### Agent-SafetyBench (2024)

**[AGREE]**

如果存在 agent safety benchmark，则与本文的 death avoidance / catastrophic failure 主题直接相关。论文已引用 Ruan et al. (2024) 的 ToolEmu，但 Agent-SafetyBench 可以加强 safe agent 行为方向的文献覆盖。

---

### RIDE (2026)

**[REBUT]（中性）**

不确定 R2 所指的 RIDE 的具体全称和内容。如果是 reward-based intrinsic exploration 方面的工作，其与本文的关联度有限——本文不做 reward design 或 exploration。需要 R2 提供完整 citation 才能评估。

---

## Minor Issues

R2 提出的 minor issues（DAF 定义合并、Table 1 caption 精度、§1 引用密度、Appendix 数量、Gajcin 2023 核实、orphan bibs、Webb 2023 年份）我均 **[AGREE]**。这些与我在 Minor Issues（M1-M5）中提出的问题有重叠，特别是 orphan bibs（M1）和 Webb 年份（M2）。均为 straightforward 修复项。

---

## 总结

与 R2 在 overall assessment 上高度一致：**3.0 (Findings)**。核心分歧在于 N3（我认为贡献的依赖关系不必然导致整体崩塌，因为 router negative result 有独立价值），但这不影响 overall score。

两位 reviewer 的 converging view：
1. 实验执行和统计方法是一流的
2. DAF 发现在 ScienceWorld 奖励结构下有 tautological/predictable 倾向
3. 单环境 scope 限制泛化性
4. Router negative result 是最有价值但被 underframe 的贡献
5. 达到 Findings 水平但不达主会议


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

_source line 2064 · 2026-05-21T15:06:04.122492+00:00_

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


## Round 169

## Round 169

2 recorded events


### User

_source line 2065 · 2026-05-21T15:06:06.665161+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 所有观点的逐条回应。

核心结论：与 R2 在 Overall 3.0 (Findings) 上一致。主要分歧仅在 N3——我认为 router negative result 的独立价值使得"三条贡献依赖关系"不构成致命问题。两位 reviewer 的 converging view 集中在：DAF 发现有 tautological 倾向、单环境限制泛化、router negative result 被 underframed。

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

_source line 2066 · 2026-05-21T15:06:12.029413+00:00_

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


## Round 170

## Round 170

20 recorded events


### User

_source line 2067 · 2026-05-21T15:06:13.536383+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 — 对 Reviewer 1 (R1) 意见的逐条回应

---

## Weaknesses 回应

### [AGREE] R1-W1: DAF 度量的 tautological 倾向
同意 R1 的核心判断。DAF = δP/(δP + Δ_nd) 在 P=100、Δ_nd=2.84 的条件下必然趋近 1，这是代数事实而非经验发现。论文在 §2.3 和 §3.1 已经承认了这一点（"mathematical consequence rather than an empirical finding"），并且在 §3.1 明确写道 "the 78.9% label fraction provides the more robust characterization"。但问题正如 R1 指出的：Abstract 和 Introduction 仍然将 DAF 作为 headline metric（Abstract: "Death Avoidance Factor, reaches 88–90%"）。这造成了 framing 与内容之间的张力。

**补充我的观点**：我在自己的审稿中（N1）从不同角度提出了类似问题——不仅 DAF 在数学上接近 tautological，整个 death dominance finding 在 oracle vs. hallucinating-LLM 的设置下方向也是可预期的。R1 的 W1 聚焦于度量本身的 tautological 性质，我的 N1 聚焦于 finding 方向的可预期性。两者共同削弱了论文的 Excitement。建议作者将 label fraction 78.9% 提为首要指标，DAF 降为 supplementary measure。

---

### [AGREE] R1-W2: 单环境局限性严重削弱泛化 claim
完全同意。这与我的 N2 观点一致。三个环境中 MATH 产出 trivial null（84.4% no-preference, §3.4），ALFWorld 的 DAF=0% 从定义直接得出（无死亡机制），均不构成框架在 non-trivial 场景下的验证。论文在 §3.4 正文中已将 MATH/ALFWorld 定位为 "boundary probes (not cross-domain validation)"，但 Abstract ("demonstrating the framework's generality") 和 Conclusion 的措辞仍在 overclaim。

R1 建议 "至少一个有 catastrophic failure 的替代环境" 是可操作的。例如 NetHack（论文 bib 中有但未 cite 的 nethack-2020）有 permadeath 机制且 failure modes 与 ScienceWorld 截然不同，可以验证框架是否在不同类型的 catastrophic failure 环境中也能诊断出 death dominance。

---

### [REBUT] R1-W3: Task selection representativeness
部分不同意。R1 声称 "未展示这 7 个 tasks 的 raw scores 或 death rates"，但论文 Appendix C Table 2 实际上提供了所有 19 个 excluded tasks 的 death rates（D%_int, D%_det, ΔDR），包括全部 7 个 agent-floor tasks（mendelian-known/unknown, power-component/renewable, test-conductivity/conductivity-unknown, use-thermometer），其 ΔDR 范围为 +20 到 +60 pp。Appendix S (Table in §S) 进一步对 5 个 representative excluded tasks 做了 n=20 的 extended validation。

但 R1 的深层观点有道理——agent-floor tasks 之所以是 "floor" 是因为 agent 在两种策略下都几乎无进展，这意味着这些任务中 routing 可能确实无意义（两种策略都失败，没有 routing 可以拯救），而非代表 "routing 最有价值的区域"。论文在 §3 开头已明确标注 "conclusions apply to the included subset"。我认为数据已经提供，但 R1 的 framing 观点（这些任务代表什么 regime）值得在 Discussion 中补充讨论。

---

### [AGREE] R1-W4: Router negative result替代解释不充分
同意 R1 的核心关切。论文 claim "signal-limited, not architecture-limited"（§3.6），但支撑证据不足以排除其他解释：

(a) **数据规模**：245 episodes、~2040 training steps 确实很小。论文虽然做了 25%-800% text augmentation ablation（Appendix J Table 6），但这是 paraphrase augmentation，不是真正的 episode-level scaling。论文自己承认 "genuine episode-level scaling remains an open question"（Appendix J）。

(b) **架构**：0.6B-4B 范围内，仅 4B 在 episode-level 超越 chance（59.0%）。论文没有测试更大的 router（如 7B+）或根本不同的架构（如 retrieval-based router）。

(c) R1 建议的 **task-level router 作为 positive control** 是一个很好的实验设计建议。论文 Appendix P 中的 leave-one-task-type-out 分析间接说明了这一点（keyword-based variant 通过 task-identity leakage 达到 62.9%），但这恰恰证明 task-type identification 是唯一可学习的特征，而非证明 signal 不存在。一个显式的 task-level router（输入 task type → 输出 routing decision）作为 positive control 可以更 cleanly 分离 signal-limited 和 architecture-limited 假说。

---

### [AGREE] R1-W5: 实验规模偏小，per-task 统计 power 不足
同意。per-task n=20 在 death rate ~40-55% 的条件下，Wilson 95% CI 约为 ±20pp，确实 power 不足。论文在 Table 1 caption 中承认 "Per-task results are exploratory (n=20 episodes per task, power ≈ 50% for 20pp effects)"。

但我认为 R1 对 aggregate claims 的 power 评估过于严格。N=245 的 aggregate bootstrap CI [81.1%, 99.0%] for DAF 是足够 informative 的，per-task claims 只是 supporting evidence。真正的 power 问题是 K=11 clusters 对 cluster bootstrap 的影响，论文已承认这一点（§3.1: "falls below the K≥20-40 threshold"）。两位 reviewer 在此点上一致——aggregate 结论可靠，per-task 结论需谨慎解读。

---

### [REBUT] R1-W6: 实际指导价值有限
部分不同意。R1 声称 Appendix R Decision Framework "未验证有效性"，但论文在 Appendix R Table 8 中提供了 retrospective validation：所有 4 个实验条件（Qwen-7B, Llama-8B, Qwen-72B, MATH）均被正确分类（4/4）。这是 post-hoc validation 而非 prospective validation，但并非"未验证"。

然而 R1 关于 "无 constructive 解决方案" 的观点有道理。论文定位为 diagnostic 而非 prescriptive（Limitations 段落明确声明），但对于一篇 long paper，在诊断之外提供更具体的下一步路径会增强实用价值。Grounding ablation（Appendix O, death rate 从 48% 降至 29%）是一个有潜力的方向，确实应该在主文中给予更多篇幅。

---

## Questions 回应

### [AGREE] R1-Q1: P=0 时 label fraction 如何变化？
这个问题的答案已在论文 §3.1 中提供。P=0 时，54 个 sole-signal labels（两种策略存活时得分均为 0，死亡是唯一区分信号）变为 ties，non-tie labels 从 95 降至 41，其中 21 (51.2%) 仍涉及 death asymmetry。R1 提出此问题可能是因为论文将这一关键信息埋在了 §3.1 的段落中而非突出展示。建议作者在修改时将 P=0 分析以表格形式呈现，提高可见性。

### [AGREE] R1-Q2: 2.6% 差异步骤的特征
好问题。论文在 §2.4 提到 "only 0.3% exhibit strict directional conflict"，在 method section 提到 97.4% tie rate，但没有对少数有差异的步骤做特征分析（如是否集中在 death-triggering 步骤附近）。Appendix P 的 death-proximal labeling ablation 间接涉及了这一点（只用 death 前 k 步训练仍 collapse to majority），但没有 descriptive analysis。这是一个值得补充的分析。

### [AGREE] R1-Q3: Grounding ablation 后 DAF 变化
同意这是一个重要的缺失分析。Appendix O 报告 grounding ablation 将 death-prone tasks 的 death rate 从 48% 降至 29%（action-space filtering），但没有在 ablation 条件下重新计算 DAF。如果 grounding intervention 成功降低了 death rate，DAF 应该下降——这将是框架的一个有力验证（干预改变 signal composition，框架能够检测到）。

### [REBUT] R1-Q4: 为什么不测试 task-level router？
R1 的建议合理，但论文实际上间接回答了这个问题。Appendix P 的 leave-one-task-type-out 分析显示：keyword-based variant 通过 task-identity leakage 达到 62.9%，而 blind routing collapse 到 50%。这意味着 task-level routing 确实是可行的——但它本质上只是 task classification（判断 "这个任务是否有死亡风险"），而非 step-level routing。论文的核心 argument 是：routing signal 就是 task-type identity（§5 Discussion "the signal *is* the task type"），所以 task-level router 会成功但这恰恰验证了负面结论。不过 R1 说得对，应该显式做这个实验作为 positive control，而非让读者自己推断。

### [REBUT] R1-Q5: Gemma per-task DAF 一致性
Appendix M (Table in cross-model section) 提供了三个模型的汇总数据。Gemma-2-9B-it 的 DAF=89.7% (95% CI [79.5%, 98.4%])，与 Qwen (90.4%) 和 Llama (88.2%) 高度一致。Table 9（Appendix M）给出了 Llama 的 per-task 分解，但 Gemma 的 per-task 分解确实不如 Llama 详细。不过 DAF 的 cross-model spread 仅 2.2pp (88.2-90.4%)，这在 bootstrap CI 范围内，说明 per-task 变异不太可能导致 label reversal。论文可以补充 Gemma 的 per-task 数据以增强说服力。

---

## Missing References 回应

### [AGREE] Pona et al. (2025) 需更详细区分
论文在 §4 Related Work 已 cite 了 pona2025abstract，但仅一笔带过。Pona et al. 的 "Abstract Counterfactuals for Language Model Agents" 与本文方法论最近，都涉及 LLM agent 的 counterfactual analysis，应该更详细对比方法论差异（action-level perturbation vs. full-episode pure-strategy comparison）。

### [REBUT] SWE-bench (Jimenez et al., 2024)
不确定 SWE-bench 的相关性。SWE-bench 是 software engineering 任务 benchmark，涉及 code editing 而非 interactive agent environments。论文的 scope 是 interactive environments with catastrophic failure mechanisms。除非 R1 认为 SWE-bench 有 catastrophic failure 类似物（如 breaking tests），否则引用必要性有限。

### [AGREE] AgentHarm (Mazeika et al., 2024)
如果此工作涉及 agent safety 和 harmful action evaluation，与本文的 death-as-catastrophic-failure 主题相关。不过需要确认其与 agent routing 的具体关联。

### [AGREE] ToolEmu (Ruan et al., 2024)
论文已 cite 了 ruan2024failures（§4 Safe RL 段落），但 ToolEmu 的 emulated sandbox approach 与本文的 counterfactual comparison 在方法论上有对比价值（模拟环境 vs. 真实环境的 pure-strategy pairing），应扩展讨论。

---

## Minor Issues 回应

### [AGREE] R1-M1: 8 个 orphan bib entries
我的引用验证也确认了这一点（balrog-2025, crafter-2022, crpo-2021, minihack-2021, nethack-2020, netplay-2024, tamar2015cvar, zhou2024webarena 在 .bib 中但未在正文引用）。应清理。

### [AGREE] R1-M2: Webb (2023) 年份核实
OpenAlex 匹配为 2014。需核实正确年份。

### [AGREE] R1-M3: Figure 1 信息密度高
Figure 1 (Fig.1 DAF scatter) 确实信息密集但清晰度尚可。更大的问题是 §1 Introduction 第二段一次引用 11 篇的做法。

### [AGREE] R1-M4: DAF 分母 Δ_full=0 的处理
当两种策略表现完全相同时（Δ_full=0），DAF 的分母为 0。论文未讨论这一边界条件的处理。在 MATH 中（Δ_full ≈ 0.5），这接近边界情形。

### [AGREE] R1-M5: ScienceWorld 版本号一致性
Appendix C 标注为 v1.2.3，但主文和其他位置未标注。应统一。

---

## 总结

R1 和我（R2）在以下核心问题上高度一致：
1. **DAF 的 tautological 性质**（R1-W1 ≈ 我的隐含关切）
2. **单环境 scope + generality overclaim**（R1-W2 ≈ 我的 N2）
3. **核心发现的 novelty/excitement 有限**（R1 Overall + 我的 N1）
4. **per-task power 不足但 aggregate 可靠**（R1-W5 ≈ 我的共识）

主要分歧点：
- R1-W3（task selection）：论文实际提供了比 R1 意识到的更多 excluded-task 数据
- R1-W6（practical guidance）：Decision framework 有 retrospective validation，非"未验证"
- SWE-bench 引用的必要性存疑

两位 reviewer 的共同 Overall 评分为 **3.0 (Findings)**，Soundness 合理但 Excitement 不足。


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

_source line 2068 · 2026-05-21T15:06:34.565352+00:00_

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

_source line 2069 · 2026-05-21T15:06:34.565978+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T14:50:50.561856+00:00\", \"completed_at\": \"2026-05-21T14:54:19.905907+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"前 2 页无视觉锚点（纯文本+1 个行内公式）。首个 display item（Figure 1 pipeline 图）出现在第 3 页。对分析型论文可接受，但若能在第 1 页放一个 teaser figure 概括核心发现（如 scatter plot 或简化框架图），可显著改善审稿人第一印象锚定\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（pipeline 图）内部文字标签偏小，多面板结构紧凑。在打印或缩放阅读时可能影响可读性。建议适当增大图内字号或简化面板标注\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（scatter plot）清晰，趋势线与数据点对比度良好，caption 自包含。无问题\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"纯文本页（Section 3.1-3.3），无任何 display item。夹在 page 4（Figure 2）和 page 6（Table 1 + Figure 3）之间，视觉节奏出现断裂。建议将 Table 1 或 Figure 3 前移至此页平衡密度\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 + Figure 3 同页，display item 密度良好。Table 1 使用 booktabs 风格，Figure 3 线条+误差带清晰可辨\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 位于页顶，booktabs 风格，最优结果有加粗标注。排版规范\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Discussion + Conclusion 全为纯文本，无任何 display item。与 page 7（仅顶部有 Table 2）合计，pages 7-8 视觉密度偏低。如果 Discussion 中能引入一个小型总结性 figure（如 decision framework 流程图）会改善末尾节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文正文 8 页，Conclusion 在 page 8 底部结束，符合 EMNLP 8 页限制\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简洁（约 3 个要点覆盖环境范围、因果 vs 相关、实验规模），长度合理。Ethics Statement 紧随其后，整页利用率约 95%\"}, {\"severity\": \"info\", \"dimension\": \"page 10-11\", \"message\": \"References 排版正常，双栏格式统一，未见 [?] 未解析引用或格式不一致\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Algorithm 1 排版清晰，伪代码结构完整。Appendix A-B 公式渲染正确\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Table 3（per-task decomposition）和 Table 4（ex
…[truncated 2096 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2070 · 2026-05-21T15:06:34.566358+00:00_

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

_source line 2071 · 2026-05-21T15:06:34.667068+00:00_

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

_source line 2072 · 2026-05-21T15:07:32.822639+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
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
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2073 · 2026-05-21T15:07:32.923532+00:00_



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

_source line 2074 · 2026-05-21T15:07:37.141704+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Synthesize consolidated review report', 'status': 'in_progress', 'activeForm': 'Synthesizing consolidated review report'}, {'content': 'Update review_issues.yaml tracker', 'status': 'pending', 'activeForm': 'Updating review issues tracker'}, {'content': 'Submit report to Research Director', 'status': 'pending', 'activeForm': 'Submitting report to Research Director'}]"
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
    "todos": "[{'content': 'Synthesize consolidated review report', 'status': 'in_progress', 'activeForm': 'Synthesizing consolidated review report'}, {'content': 'Update review_issues.yaml tracker', 'status': 'pending', 'activeForm': 'Updating review issues tracker'}, {'content': 'Submit report to Research Director', 'status': 'pending', 'activeForm': 'Submitting report to Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 2075 · 2026-05-21T15:07:37.192421+00:00_

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

_source line 2076 · 2026-05-21T15:07:43.267081+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Synthesize consolidated review report', 'status': 'in_progress', 'activeForm': 'Synthesizing consolidated review report'}, {'content': 'Update review_issues.yaml tracker', 'status': 'in_progress', 'activeForm': 'Updating review issues tracker'}, {'content': 'Submit report to Research Director', 'status': 'pending', 'activeForm': 'Submitting report to Research Director'}]"
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
    "todos": "[{'content': 'Synthesize consolidated review report', 'status': 'in_progress', 'activeForm': 'Synthesizing consolidated review report'}, {'content': 'Update review_issues.yaml tracker', 'status': 'in_progress', 'activeForm': 'Updating review issues tracker'}, {'content': 'Submit report to Research Director', 'status': 'pending', 'activeForm': 'Submitting report to Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 2077 · 2026-05-21T15:07:43.318204+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "TodoWrite",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2078 · 2026-05-21T15:10:56.981494+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "# Round 25 Review Issues (fresh review, 2026-05-21)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+相关工作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n# =============================================\n# Round 25 — Active issues (new + recurring)\n# =============================================\n\n# --- Recurring critical issues ---\n\n- id: \"R13-N1\"\n  summary: \"DAF 度量在 ScienceWorld 奖励结构下有 tautological 倾向——DAF 高值是数学必然而非经验发现\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 RESOLVED: Abstract 以 78.9% label fraction 为 headline，DAF 降级为补充。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 两位 reviewer 独立重新提出。R1-W1: DAF=δP/(δP+Δ_nd) 在 P=100、Δ_nd=2.84 下必然趋近 1，是代数事实。R2 交叉回应 AGREE。Abstract 仍将 DAF 88-90% 作为 prominent metric。共识：label fraction 78.9% 是真正的 empirical finding，DAF 是 definitional truth。论文 §2.4 和 §3.1 已承认但 Abstract/Intro framing 未充分反映。\"\n  resolution: \"\"\n  resolution_round: null\n  action_items:\n    - round: 25\n      action: \"Abstract 和 Introduction 中明确将 label fraction 78.9% 作为 headline metric，DAF 降级为 supplementary score-weighted measure\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——death dominance 在 oracle vs. hallucinating-LLM 设置下方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24: §5 Non-triviality 段有效缓解但不消除。R1 Excitement 3.0, R2 Excitement 3.0。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 两位 reviewer Excitement 均为 2.5。R2-N1: death dominance 的方向是可预期的——oracle 天然比 hallucinating LLM 安全。§5 non-triviality 论证（72B、Reflexion DAF>100%、inverted-U）是关于 persistence 而非 existence。R1 交叉回应 AGREE 但指出 prevalence 量化和 router negative result 仍有 surprise value。共识：这是 Findings 而非 Conference 水平的核心原因。不可通过 writing 修复——需新环境深度分析或根本性新发现。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清——三条 contribution 存在依赖关系\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 分歧：R1 递进合理，R2 (2)(3) 仍是 (1) 的应用。降级为 Minor。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-N3 重新提出：(1) 框架 → (2) 应用于 ScienceWorld → (3) robustness check，是层层依赖非独立并列。R1 交叉回应 REBUT：router negative result 有独立价值，最有价值排序为 (a) router failure > (b) 78.9% prevalence > (c) 框架本身。共识：不构成 blocking issue，但 contribution statement 应更清晰区分方法论贡献与实证 insight。\"\n  action_items:\n    - round: 25\n      action: \"重组 contribution statement：(1) 框架+方法论简述 (2) 实证发现+量化 (3) practical implications (decision framework + router failure)\"\n      assigned_to: research_director\n      status: pending\n\n# --- Recurring warning/info issues ---\n\n- id: \"R25-N1\"\n  summary: \"单环境 scope + Abstract/Conclusion 中 generality overclaim——MATH/ALFWorld 仅为退化 boundary probes\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-N2 独立提出，交叉回应互相 AGREE。MATH 无信号(84.4% no-pref)，ALFWorld DAF=0%(无死亡机制)，均不验证框架在 non-trivial 场景下的诊断价值。Abstract 'demonstrating the framework's generality' 和 Conclusion 措辞仍在 overclaim。bib 中有 NetHack/MiniHack/BALROG/Crafter 等有 catastrophic failure 的环境但均为 orphan references。\"\n  action_items:\n    - round: 25\n      action: \"降低 Abstract/Conclusion 中 generality claim 强度，与正文 §3.4 'boundary probes' 定位一致\"\n      assigned_to: research_director\n      status: pending\n    - round: 25\n      action: \"（可选但强烈建议）在至少一个有 catastrophic failure 的替代环境上验证 death dominance\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W1\"\n  summary: \"Router negative result 替代解释未充分排除——缺少 task-level router positive control\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W4: 训练数据规模小(245 episodes/~2040 steps)，架构仅 0.6B-4B，缺少 task-level router positive control。R2 交叉回应 AGREE，补充：leave-one-task-out 中 keyword variant 62.9% 间接证明 task-type identification 是唯一可学信号，但显式 task-level router 实验会更 clean。'signal-limited, not architecture-limited' claim 过于绝对。\"\n  action_items:\n    - round: 25\n      action: \"（建议）添加 task-level router positive control 实验；弱化 §3.6 'signal-limited' absolute claim\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"Anti-cherry-picking analysis 被列为优势。Scope limitation 已在正文声明。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2-W1 重新提出。R2 REBUT R1：Appendix C Table 4 和 Appendix S 已提供 excluded tasks 数据，R1 claims '未展示' 不完全准确。但 R1 的深层观点成立：7 个 agent-floor tasks 代表什么 regime 未讨论。如果两策略都频繁死亡（无 asymmetry），routing signal 可能由非 death 因素驱动——这是 death dominance 不成立的有趣案例。建议在 Discussion 补充讨论。\"\n  action_items:\n    - round: 25\n      action: \"Discussion 中补充讨论 agent-floor tasks 对 death dominance 的含义\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R19-W2\"\n  summary: \"Conclusion 过于简短——单段 ~60 词不匹配 8 页 long paper + 20 个 appendix\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 分歧：R2 偏短，R1 ARR 无最低字数要求且扩展触发页数超限。降级为 Minor。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 AGREE R2-W3：Conclusion 应包含核心发现总结、主要 limitations 简要提及、future work 方向。两位共识。\"\n  action_items:\n    - round: 25\n      action: \"扩展 Conclusion 至 2-3 段（在 8 页预算内）\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W2\"\n  summary: \"'penalty-independent' 表述在 Abstract/Intro 中仍有误导性——P=0 时 54 labels 退化为 ties\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 交叉回应 AGREE。§3.1 已量化 P=0 退化（R24 修复），但 Abstract 仍用 'penalty-independent finding' 修饰核心发现。label fraction 数值不依赖 P，但 routing signal 的实际 relevance 高度依赖 P（P=0 时 signal 几乎消失）。建议改为更精确表述。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Intro 中避免 'penalty-independent' 修饰核心发现，改为 'invariant to penalty magnitude in the labeling procedure'\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W3\"\n  summary: \"Safe RL 相关工作覆盖不足——§4 仅 3 行，与核心发现（catastrophic failure avoidance）的关联讨论缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 交叉回应 AGREE。引用了 Altman/Mihatsch/García/Achiam/Moldovan/Ruan/SafeRoute 但未讨论 (a) death avoidance 与 CMDP constraint satisfaction 的对应 (b) 为什么 Safe RL 方案不直接适用于 LLM agent routing。\"\n  action_items:\n    - round: 25\n      action: \"扩展 §4 Safe RL 段落，讨论与 constrained MDP 的关系\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W4\"\n  summary: \"Router negative result 在 contribution statement 中被 underframed——是论文最有实践价值的发现之一\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 交叉回应 STRONGLY AGREE。§3.6 标题 'A Negative Result' 定位为附带发现，但 step-level router 无法学习 task-type-level signal 是真正 non-trivial 且有实践指导价值的结论。R1：'这可能是论文最有实践价值的贡献'。建议提升为与 DAF 发现并列的核心 contribution。\"\n  action_items:\n    - round: 25\n      action: \"在 contribution statement 中更 prominently frame router failure 为核心贡献\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W5\"\n  summary: \"实验规模偏小（per-task n=20），per-task 统计 power 不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 AGREE。Per-task Wilson CI ~±20pp。Table 1 caption 已标注 exploratory (R24 修复)。共识：aggregate claims (N=245) 可靠，per-task 需谨慎。K=11 cluster bootstrap power 不足但论文已承认。不构成 blocking issue。\"\n\n- id: \"R25-W6\"\n  summary: \"实际指导价值有限——诊断之外缺少 constructive 解决路径\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W6 提出，R2 部分 REBUT：Appendix R Decision Framework 有 retrospective 4/4 validation，非'未验证'。但共识：grounding ablation (Appendix O, 48%→29% death rate) 是有潜力的方向，应在主文给更多篇幅。论文定位为 diagnostic 非 prescriptive（Limitations 明确声明），此定位本身可接受但降低了 impact。\"\n\n# --- Minor/Info issues ---\n\n- id: \"R25-M1\"\n  summary: \"8 个 orphan bib entries: balrog-2025, crafter-2022, crpo-2021, minihack-2021, nethack-2020, netplay-2024, tamar2015cvar, zhou2024webarena\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"两位 reviewer 独立发现。R24 清理了旧 orphan entries，但这 8 个是新的（可能是添加 cross-env 讨论时引入但未 cite 的环境）。\"\n  action_items:\n    - round: 25\n      action: \"清理 8 个 orphan bib entries 或在正文中引用\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-M2\"\n  summary: \"Webb (2023) 年份与 OpenAlex 记录不符\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R24 声称核实正确(CJE vol.56 no.3)。R25 两位 reviewer 仍标注 OpenAlex 返回 2014。需再次核实。\"\n\n- id: \"R25-M3\"\n  summary: \"Missing references: Kumaraguru et al. (2025), step-level credit assignment (2026), Agent-SafetyBench (2024)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"R2 提出 4 个 missing references。R1 AGREE Agent-SafetyBench 和 Kumaraguru（如确认存在）。SWE-bench 被 R2 REBUT（相关性存疑）。RIDE R1 需要更多信息。\"\n\n- id: \"R25-M4\"\n  summary: \"'deterministic' 术语统称三种不同 information advantage（oracle/code interpreter/admissible actions）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-Q2 提出，R1 AGREE。§2.1 脚注有简要说明但主文应更显式区分。\"\n\n# --- Previously in_progress, not raised in R25 ---\n\n- id: \"R16-N3\"\n  summary: \"缺少 permadeath 环境 replication\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"连续多轮未提及。被 R16-N1 novelty concern 覆盖。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 被 R25-N1（单环境 + generality overclaim）覆盖。两位 reviewer 均建议在有 catastrophic failure 的替代环境验证。合并到 R25-N1 处理。\"\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 降级为 Minor。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 被 R19-N1（contribution framing）覆盖。R2-N3 重新提出三条 contribution 依赖关系。\"\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: []\n      note: \"R25 未提及。多轮无 reviewer 关注，可能已修复或不影响理解。\"\n\n- id: \"R17-W2\"\n  summary: \"Figure 2 caption / readability 问题\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: []\n      note: \"R25 未直接提及 Figure 2。R1-M3 提到 Figure 1 信息密度高。视觉审查标注 Figure 1 pipeline 图标签偏小。\"\n\n- id: \"R19-W3\"\n  summary: \"Routing 的 practical value 本身存疑——always-det 近最优\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-Q3 指出 61.2% ties 暗示 routing 价值极有限，R1 AGREE 并称这是 R2 最有洞察力的问题之一。实质上强化了论文的诊断发现但未在 Discussion 充分讨论。\"\n\n- id: \"R19-M1\"\n  summary: \"62% tie rate (150/245) 含义未充分讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-Q3 + R1 AGREE：61.2% ties 意味着 routing 最多改善 38.8% episodes。论文未充分讨论 implication。合并 R19-W3 处理。\"\n\n- id: \"R19-M3\"\n  summary: \"Table 1 weighting scheme（episode-weighted vs task-weighted）未明确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: []\n      note: \"R25 未提及。Table 2 caption 已标注 'Episode-weighted mean scores'。考虑 resolved。\""
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
    "issues_yaml": "# Round 25 Review Issues (fresh review, 2026-05-21)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+相关工作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n# =============================================\n# Round 25 — Active issues (new + recurring)\n# =============================================\n\n# --- Recurring critical issues ---\n\n- id: \"R13-N1\"\n  summary: \"DAF 度量在 ScienceWorld 奖励结构下有 tautological 倾向——DAF 高值是数学必然而非经验发现\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 RESOLVED: Abstract 以 78.9% label fraction 为 headline，DAF 降级为补充。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 两位 reviewer 独立重新提出。R1-W1: DAF=δP/(δP+Δ_nd) 在 P=100、Δ_nd=2.84 下必然趋近 1，是代数事实。R2 交叉回应 AGREE。Abstract 仍将 DAF 88-90% 作为 prominent metric。共识：label fraction 78.9% 是真正的 empirical finding，DAF 是 definitional truth。论文 §2.4 和 §3.1 已承认但 Abstract/Intro framing 未充分反映。\"\n  resolution: \"\"\n  resolution_round: null\n  action_items:\n    - round: 25\n      action: \"Abstract 和 Introduction 中明确将 label fraction 78.9% 作为 headline metric，DAF 降级为 supplementary score-weighted measure\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——death dominance 在 oracle vs. hallucinating-LLM 设置下方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24: §5 Non-triviality 段有效缓解但不消除。R1 Excitement 3.0, R2 Excitement 3.0。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 两位 reviewer Excitement 均为 2.5。R2-N1: death dominance 的方向是可预期的——oracle 天然比 hallucinating LLM 安全。§5 non-triviality 论证（72B、Reflexion DAF>100%、inverted-U）是关于 persistence 而非 existence。R1 交叉回应 AGREE 但指出 prevalence 量化和 router negative result 仍有 surprise value。共识：这是 Findings 而非 Conference 水平的核心原因。不可通过 writing 修复——需新环境深度分析或根本性新发现。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清——三条 contribution 存在依赖关系\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 分歧：R1 递进合理，R2 (2)(3) 仍是 (1) 的应用。降级为 Minor。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-N3 重新提出：(1) 框架 → (2) 应用于 ScienceWorld → (3) robustness check，是层层依赖非独立并列。R1 交叉回应 REBUT：router negative result 有独立价值，最有价值排序为 (a) router failure > (b) 78.9% prevalence > (c) 框架本身。共识：不构成 blocking issue，但 contribution statement 应更清晰区分方法论贡献与实证 insight。\"\n  action_items:\n    - round: 25\n      action: \"重组 contribution statement：(1) 框架+方法论简述 (2) 实证发现+量化 (3) practical implications (decision framework + router failure)\"\n      assigned_to: research_director\n      status: pending\n\n# --- Recurring warning/info issues ---\n\n- id: \"R25-N1\"\n  summary: \"单环境 scope + Abstract/Conclusion 中 generality overclaim——MATH/ALFWorld 仅为退化 boundary probes\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-N2 独立提出，交叉回应互相 AGREE。MATH 无信号(84.4% no-pref)，ALFWorld DAF=0%(无死亡机制)，均不验证框架在 non-trivial 场景下的诊断价值。Abstract 'demonstrating the framework's generality' 和 Conclusion 措辞仍在 overclaim。bib 中有 NetHack/MiniHack/BALROG/Crafter 等有 catastrophic failure 的环境但均为 orphan references。\"\n  action_items:\n    - round: 25\n      action: \"降低 Abstract/Conclusion 中 generality claim 强度，与正文 §3.4 'boundary probes' 定位一致\"\n      assigned_to: research_director\n      status: pending\n    - round: 25\n      action: \"（可选但强烈建议）在至少一个有 catastrophic failure 的替代环境上验证 death dominance\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W1\"\n  summary: \"Router negative result 替代解释未充分排除——缺少 task-level router positive control\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W4: 训练数据规模小(245 episodes/~2040 steps)，架构仅 0.6B-4B，缺少 task-level router positive control。R2 交叉回应 AGREE，补充：leave-one-task-out 中 keyword variant 62.9% 间接证明 task-type identification 是唯一可学信号，但显式 task-level router 实验会更 clean。'signal-limited, not architecture-limited' claim 过于绝对。\"\n  action_items:\n    - round: 25\n      action: \"（建议）添加 task-level router positive control 实验；弱化 §3.6 'signal-limited' absolute claim\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"Anti-cherry-picking analysis 被列为优势。Scope limitation 已在正文声明。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2-W1 重新提出。R2 REBUT R1：Appendix C Table 4 和 Appendix S 已提供 excluded tasks 数据，R1 claims '未展示' 不完全准确。但 R1 的深层观点成立：7 个 agent-floor tasks 代表什么 regime 未讨论。如果两策略都频繁死亡（无 asymmetry），routing signal 可能由非 death 因素驱动——这是 death dominance 不成立的有趣案例。建议在 Discussion 补充讨论。\"\n  action_items:\n    - round: 25\n      action: \"Discussion 中补充讨论 agent-floor tasks 对 death dominance 的含义\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R19-W2\"\n  summary: \"Conclusion 过于简短——单段 ~60 词不匹配 8 页 long paper + 20 个 appendix\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 分歧：R2 偏短，R1 ARR 无最低字数要求且扩展触发页数超限。降级为 Minor。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 AGREE R2-W3：Conclusion 应包含核心发现总结、主要 limitations 简要提及、future work 方向。两位共识。\"\n  action_items:\n    - round: 25\n      action: \"扩展 Conclusion 至 2-3 段（在 8 页预算内）\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W2\"\n  summary: \"'penalty-independent' 表述在 Abstract/Intro 中仍有误导性——P=0 时 54 labels 退化为 ties\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 交叉回应 AGREE。§3.1 已量化 P=0 退化（R24 修复），但 Abstract 仍用 'penalty-independent finding' 修饰核心发现。label fraction 数值不依赖 P，但 routing signal 的实际 relevance 高度依赖 P（P=0 时 signal 几乎消失）。建议改为更精确表述。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Intro 中避免 'penalty-independent' 修饰核心发现，改为 'invariant to penalty magnitude in the labeling procedure'\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W3\"\n  summary: \"Safe RL 相关工作覆盖不足——§4 仅 3 行，与核心发现（catastrophic failure avoidance）的关联讨论缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 交叉回应 AGREE。引用了 Altman/Mihatsch/García/Achiam/Moldovan/Ruan/SafeRoute 但未讨论 (a) death avoidance 与 CMDP constraint satisfaction 的对应 (b) 为什么 Safe RL 方案不直接适用于 LLM agent routing。\"\n  action_items:\n    - round: 25\n      action: \"扩展 §4 Safe RL 段落，讨论与 constrained MDP 的关系\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W4\"\n  summary: \"Router negative result 在 contribution statement 中被 underframed——是论文最有实践价值的发现之一\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 交叉回应 STRONGLY AGREE。§3.6 标题 'A Negative Result' 定位为附带发现，但 step-level router 无法学习 task-type-level signal 是真正 non-trivial 且有实践指导价值的结论。R1：'这可能是论文最有实践价值的贡献'。建议提升为与 DAF 发现并列的核心 contribution。\"\n  action_items:\n    - round: 25\n      action: \"在 contribution statement 中更 prominently frame router failure 为核心贡献\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-W5\"\n  summary: \"实验规模偏小（per-task n=20），per-task 统计 power 不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 AGREE。Per-task Wilson CI ~±20pp。Table 1 caption 已标注 exploratory (R24 修复)。共识：aggregate claims (N=245) 可靠，per-task 需谨慎。K=11 cluster bootstrap power 不足但论文已承认。不构成 blocking issue。\"\n\n- id: \"R25-W6\"\n  summary: \"实际指导价值有限——诊断之外缺少 constructive 解决路径\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W6 提出，R2 部分 REBUT：Appendix R Decision Framework 有 retrospective 4/4 validation，非'未验证'。但共识：grounding ablation (Appendix O, 48%→29% death rate) 是有潜力的方向，应在主文给更多篇幅。论文定位为 diagnostic 非 prescriptive（Limitations 明确声明），此定位本身可接受但降低了 impact。\"\n\n# --- Minor/Info issues ---\n\n- id: \"R25-M1\"\n  summary: \"8 个 orphan bib entries: balrog-2025, crafter-2022, crpo-2021, minihack-2021, nethack-2020, netplay-2024, tamar2015cvar, zhou2024webarena\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"两位 reviewer 独立发现。R24 清理了旧 orphan entries，但这 8 个是新的（可能是添加 cross-env 讨论时引入但未 cite 的环境）。\"\n  action_items:\n    - round: 25\n      action: \"清理 8 个 orphan bib entries 或在正文中引用\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R25-M2\"\n  summary: \"Webb (2023) 年份与 OpenAlex 记录不符\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R24 声称核实正确(CJE vol.56 no.3)。R25 两位 reviewer 仍标注 OpenAlex 返回 2014。需再次核实。\"\n\n- id: \"R25-M3\"\n  summary: \"Missing references: Kumaraguru et al. (2025), step-level credit assignment (2026), Agent-SafetyBench (2024)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"R2 提出 4 个 missing references。R1 AGREE Agent-SafetyBench 和 Kumaraguru（如确认存在）。SWE-bench 被 R2 REBUT（相关性存疑）。RIDE R1 需要更多信息。\"\n\n- id: \"R25-M4\"\n  summary: \"'deterministic' 术语统称三种不同 information advantage（oracle/code interpreter/admissible actions）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-Q2 提出，R1 AGREE。§2.1 脚注有简要说明但主文应更显式区分。\"\n\n# --- Previously in_progress, not raised in R25 ---\n\n- id: \"R16-N3\"\n  summary: \"缺少 permadeath 环境 replication\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"连续多轮未提及。被 R16-N1 novelty concern 覆盖。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 被 R25-N1（单环境 + generality overclaim）覆盖。两位 reviewer 均建议在有 catastrophic failure 的替代环境验证。合并到 R25-N1 处理。\"\n\n- id: \"R16-W4\"\n  summary: \"Contribution 2 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24 降级为 Minor。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 被 R19-N1（contribution framing）覆盖。R2-N3 重新提出三条 contribution 依赖关系。\"\n\n- id: \"R16-M1\"\n  summary: \"Appendix C task name 不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: []\n      note: \"R25 未提及。多轮无 reviewer 关注，可能已修复或不影响理解。\"\n\n- id: \"R17-W2\"\n  summary: \"Figure 2 caption / readability 问题\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: []\n      note: \"R25 未直接提及 Figure 2。R1-M3 提到 Figure 1 信息密度高。视觉审查标注 Figure 1 pipeline 图标签偏小。\"\n\n- id: \"R19-W3\"\n  summary: \"Routing 的 practical value 本身存疑——always-det 近最优\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-Q3 指出 61.2% ties 暗示 routing 价值极有限，R1 AGREE 并称这是 R2 最有洞察力的问题之一。实质上强化了论文的诊断发现但未在 Discussion 充分讨论。\"\n\n- id: \"R19-M1\"\n  summary: \"62% tie rate (150/245) 含义未充分讨论\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-Q3 + R1 AGREE：61.2% ties 意味着 routing 最多改善 38.8% episodes。论文未充分讨论 implication。合并 R19-W3 处理。\"\n\n- id: \"R19-M3\"\n  summary: \"Table 1 weighting scheme（episode-weighted vs task-weighted）未明确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: []\n      note: \"R25 未提及。Table 2 caption 已标注 'Episode-weighted mean scores'。考虑 resolved。\""
  }
}
```

</details>

---


### Tool result

_source line 2079 · 2026-05-21T15:10:57.082739+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 24543}, \"error\": \"\"}"}

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

_source line 2080 · 2026-05-21T15:11:01.954664+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Synthesize consolidated review report', 'status': 'completed', 'activeForm': 'Synthesizing consolidated review report'}, {'content': 'Update review_issues.yaml tracker', 'status': 'completed', 'activeForm': 'Updating review issues tracker'}, {'content': 'Submit report to Research Director', 'status': 'in_progress', 'activeForm': 'Submitting report to Research Director'}]"
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
    "todos": "[{'content': 'Synthesize consolidated review report', 'status': 'completed', 'activeForm': 'Synthesizing consolidated review report'}, {'content': 'Update review_issues.yaml tracker', 'status': 'completed', 'activeForm': 'Updating review issues tracker'}, {'content': 'Submit report to Research Director', 'status': 'in_progress', 'activeForm': 'Submitting report to Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 2081 · 2026-05-21T15:11:02.005377+00:00_

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

_source line 2082 · 2026-05-21T15:13:45.804387+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 25 (Fresh Review)\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**投稿类别**: Interpretability and Analysis of Models for NLP\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+相关工作）\n**审稿轮次**: 1 轮（Round 1 初审 → 交叉分享 → 收敛，关键问题全部达成共识）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，比较 LLM agent 在 pure-internal（ReAct）与 pure-deterministic（oracle simulator）策略下的 episode 结果，分解 routing signal 的来源。核心发现：在 ScienceWorld 的 11 类任务（245 episodes）中，78.9% 的 non-tie routing labels 源自 death asymmetry——internal 策略触发 −100 惩罚的灾难性失败而 deterministic 策略存活。引入 Death Avoidance Factor (DAF) 量化该效应（DAF=90.4%），跨三个模型家族（Qwen-7B/Llama-8B/Gemma-9B, DAF 88-90%）和 72B scaling 验证一致性。Cross-environment boundary probes（MATH 无信号、ALFWorld 信息不对称）展示框架在不同机制下的诊断能力。Router 训练得到负结果（step-level balanced accuracy 56-59%），归因于 death avoidance 是 task-type-level 而非 step-level 信号。\n\n---\n\n## Strengths\n\n**S1. 研究问题有价值且切入角度新颖 [共识]。** 现有 routing/tool-use 工作集中于\"如何建 router\"，本文退一步问\"routing signal 到底是什么\"。这种\"先诊断再优化\"的方法论对 agent routing 社区有指导意义，切入了一个被忽视的诊断性问题。\n\n**S2. 统计方法论一流 [共识]。** Bootstrap resampling (B=10,000)、cluster bootstrap sensitivity (K=11, 含 wild cluster bootstrap)、Signal Concentration Index (SCI)、leave-one-task-out stability analysis、per-task CIs、dose-response analysis、Cohen's d——统计工具链完整且使用得当，远超多数 agent 论文的 reporting 标准。95% CIs 贯穿全文所有 quantitative claims。对 K=11 cluster bootstrap power 不足的问题也诚实讨论（Cameron et al. 2008 推荐 K≥20-30）。\n\n**S3. 对自身局限性的坦诚讨论 [共识]。** 论文对局限性的讨论异常透明——r=0.97 correlation 是 structural consequence（§3.1）、DAF 是 penalty-dependent（§2.4）、router 是 negative result（§3.6）、task exclusion 有完整分析（Appendix C/S）。这种 intellectual honesty 在同类论文中罕见。\n\n**S4. Cross-model validation 扎实 [共识]。** 三个架构不同的模型族（Qwen/Llama/Gemma）独立收敛于 DAF 88-90%（spread 2.2pp），加上 72B scaling (DAF=92.4%)，构成 convincing 的 robustness evidence。Appendix M 提供完整 per-task 分解。\n\n**S5. Router negative result 有价值 [共识]。** §3.6 的 step-level router 无法捕获 task-type-level 信号是一个重要实践性发现，能帮社区避免无效的 router 开发投入。Appendix P 的 generative router (46.7%) 进一步确认瓶颈在 signal 而非 architecture。两位 Reviewer 一致认为这可能是论文最有实践价值的贡献。\n\n**S6. 附录极其详尽 [共识]。** 20 个 Appendices (A-T) 覆盖 task selection rationale、correlation robustness、penalty sensitivity、failure mode taxonomy、grounding ablation、prompt templates 等，可复现性极高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [Critical, 共识] DAF 度量在 ScienceWorld 奖励结构下有 tautological 倾向。**\nDAF = δP/(δP + Δ_nd) 在 P=100、Δ_nd=2.84 的条件下必然趋近 1——这是代数事实而非经验发现。论文在 §2.4 和 §3.1 已承认（\"mathematical consequence rather than an empirical finding\"、\"the 78.9% label fraction provides the more robust characterization\"），但 Abstract 和 Introduction 仍将 DAF 88-90% 作为 prominent metric 呈现。真正有信息量的经验发现是 label fraction (78.9%)，而非 DAF 数值本身。两位 Reviewer 建议：明确将 label fraction 作为 headline metric，DAF 降级为 supplementary score-weighted measure。（R1-W1, R2 交叉 AGREE）\n\n**W2 [Critical, 共识] 核心发现的新颖性有限——death dominance 在实验设置下方向可预期。**\nOracle simulator 提供 ground-truth state transitions，而 internal 策略依赖会幻觉的 LLM。在 −100 death penalty 下，oracle 天然比幻觉策略更安全——death asymmetry 的 *存在* 是可预期的。§5 的 non-triviality 论证（72B 未消除、Reflexion DAF>100%、inverted-U）是关于 death dominance 的 *persistence*，而非 *existence* 的 surprise。R1 交叉回应中指出：prevalence 量化（78.9%）和 router negative result 仍有 surprise value（Δ_nd≈2.84 near-uniform 需要实证确认；router failure 不可从设置预测）。但两位 Reviewer 共识 Excitement 仅 2.5/5，这是 Findings 而非 Conference 水平的核心原因。此问题不可通过 writing 修复——需新环境深度分析或根本性新发现。（R2-N1, R1 AGREE with nuance）\n\n**W3 [Critical, 共识] 单环境 scope + generality overclaim。**\n主实验仅在 ScienceWorld 上进行。MATH（84.4% no-preference）和 ALFWorld（DAF=0%, 无死亡机制）作为 boundary probes 只展示框架的诊断能力多样性，不能验证 death-dominance 发现是否泛化到其他有灾难性失败的环境。论文正文 §3.4 已将 MATH/ALFWorld 定位为 \"boundary probes (not cross-domain validation)\"，但 Abstract (\"demonstrating the framework's generality\") 和 Conclusion 措辞仍在 overclaim。bib 中有 NetHack/MiniHack/BALROG/Crafter 等有 catastrophic failure 的环境但均为 orphan references。建议：(a) 降低 Abstract/Conclusion generality claim 至与 §3.4 一致；(b) 在至少一个有 permadeath 的替代环境上验证（如 NetHack）。（R1-W2, R2-N2, 交叉 mutual AGREE）\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4 [Warning, 共识] Router negative result 替代解释未充分排除。**\n§3.6 claim \"signal-limited, not architecture-limited\" 但未充分排除：(a) 训练数据规模极小（245 episodes/~2040 steps），paraphrase augmentation ≠ 真实数据扩增；(b) router 仅 0.6B-4B，更大模型或不同架构未测试；(c) 缺少 task-level router positive control（输入 task type → 输出 routing decision）。Appendix P leave-one-task-out 中 keyword variant 62.9% 间接证明 task-type identification 是唯一可学信号，但显式实验会更 clean。建议弱化 absolute claim 并添加 task-level router 实验。（R1-W4, R2 AGREE）\n\n**W5 [Warning, 共识] Contribution framing 不清晰——三条 contribution 存在依赖关系。**\n(1) 框架 → (2) 应用于 ScienceWorld → (3) robustness check，是层层依赖而非独立并列。R1 REBUT 指出 router negative result 有独立价值，排序应为 (a) router failure > (b) 78.9% prevalence > (c) 框架本身。共识：不构成 blocking issue，但 contribution statement 应更清晰区分方法论贡献与实证 insight，并更 prominently frame router failure。（R2-N3, R1 partial REBUT but agrees on framing improvement）\n\n**W6 [Warning, 共识] Conclusion 过于单薄。**\n单段约 60 词，对于 8 页正文 + 20 个 Appendix 的 long paper，未讨论 broader implications、future work 方向、或对 NLP community 的 takeaway。建议扩展至 2-3 段（在 8 页预算内）。（R2-W3, R1 AGREE）\n\n**W7 [Warning, 共识] \"penalty-independent\" 表述在 Abstract/Intro 中有误导性。**\nLabel fraction 数值不依赖 P，但 P=0 时 54 个 sole-signal labels 变为 ties（non-tie 从 95 降至 41），routing signal 的实际 relevance 高度依赖 penalty magnitude。建议改为更精确表述如 \"invariant to penalty magnitude in the labeling procedure\"。（R2-W2, R1 AGREE）\n\n**W8 [Warning, 共识] Safe RL 相关工作覆盖不足。**\n§4 Safe RL 段落仅 3 行，引用 5 篇经典 + 2 篇近期。鉴于核心发现是 catastrophic failure avoidance dominates routing signal，应更详细讨论与 constrained MDPs/risk-sensitive RL 的关系，以及为什么 Safe RL 方案（如 CPO）不直接适用于 LLM agent routing。（R2-W4, R1 AGREE）\n\n**W9 [Warning, 共识] Task selection (11/30) 的 agent-floor tasks 含义未讨论。**\n63% exclusion rate 有合理理由且 anti-cherry-picking 分析到位（Appendix C/S），但 7 个 agent-floor tasks 代表什么 regime 未讨论——如果两策略都频繁死亡（无 asymmetry），routing signal 可能由非 death 因素驱动，这是 death dominance 不成立的有趣案例。建议在 Discussion 补充。（R1-W3, R2-W1, R2 partial REBUT on data availability but AGREE on framing）\n\n**W10 [Warning, R1 提出] 实验规模偏小，per-task 统计 power 不足。**\nPer-task n=20，Wilson CI ~±20pp。Table 1 caption 已标注 exploratory。共识：aggregate claims (N=245) 可靠，per-task 需谨慎解读。不构成 blocking issue。（R1-W5, R2 AGREE）\n\n**W11 [Warning, R1 提出] 实际指导价值有限。**\n诊断之外缺少 constructive 解决路径。Appendix R Decision Framework 有 retrospective 4/4 validation（R2 指出非\"未验证\"），但 grounding ablation (Appendix O, death rate 48%→29%) 是有潜力的方向，应在主文给更多篇幅。论文定位为 diagnostic 非 prescriptive（Limitations 明确声明），此定位本身可接受但降低了 impact。（R1-W6, R2 partial REBUT）\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致（所有交叉回应为 [AGREE]）：\n1. DAF 在 ScienceWorld 奖励结构下有 tautological 倾向，label fraction 应为 headline metric\n2. 单环境 scope 限制泛化性，Abstract/Conclusion generality claim 需收窄\n3. 核心发现方向可预期，Excitement 不足（均 2.5/5）\n4. Router negative result 被 underframed，应提升为核心 contribution\n5. Conclusion 过于简短\n6. Safe RL 覆盖不足\n7. Per-task power 有限但 aggregate 可靠\n8. Overall 3.0 (Findings)\n\n## Reviewer Divergence\n\n仅有轻微分歧，均已在交叉回应中解决：\n\n1. **Contribution 独立性 (R2-N3)**：R2 认为三条 contribution 的依赖关系使 overall contribution 难以评估；R1 REBUT 指出 router negative result 有独立价值。**Director 判断**：R1 的 rebut 有道理，但不改变 overall score——contribution framing 需改进但非 blocking。\n\n2. **Task selection 数据可用性 (R1-W3)**：R1 声称 excluded tasks 数据未展示；R2 REBUT 指出 Appendix C Table 4 和 Appendix S 已提供。**Director 判断**：R2 的事实纠正正确，R1 可能遗漏了附录数据。但 R1 的深层观点（agent-floor tasks 的 regime 含义）成立。\n\n3. **Practical guidance (R1-W6)**：R1 称 Decision Framework \"未验证\"；R2 REBUT 指出有 retrospective 4/4 validation。**Director 判断**：R2 的事实纠正正确（有 post-hoc validation），但 R1 对 constructive 方案缺失的批评仍然有效。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** P=0 时 label fraction 从 78.9% 降至 51.2%（§3.1 已有数据）——建议以表格形式突出展示 P=0/10/50/100/200 的 label fraction 变化，而非仅在段落中提及。\n\n**Q2.** 61.2% tie rate (150/245) 意味着 routing 最多改善 38.8% 的 episodes。这对 routing 系统的实际 ROI 意味什么？建议在 Discussion 中增加分析。（R2-Q3, R1 AGREE 称\"R2 最有洞察力的问题之一\"）\n\n**Q3.** 2.6% 有差异的步骤（159/6094）是否集中在 death-triggering 步骤？Appendix P 的 death-proximal labeling 间接涉及但缺少 descriptive analysis。（R1-Q2）\n\n**Q4.** Grounding ablation (Appendix O) 将 death rate 从 48% 降至 29%。在此条件下重新计算 DAF 的值是多少？（R1-Q3, R2 AGREE——这将验证框架对 intervention 的敏感性）\n\n**Q5.** 0.5B inverted-U claim 基于 n=15，Wilson CI 极宽。是否有足够统计 power 区分 inverted-U 和 random fluctuation？（R2-Q4, R1 AGREE）\n\n**Q6.** \"deterministic\" 统称 oracle simulator (ScienceWorld)、code interpreter (MATH)、admissible-action access (ALFWorld) 三种性质不同的 information advantage。§2.1 脚注有简要说明，但主文应更显式区分以避免误导读者认为 cross-environment 比较是 apples-to-apples。（R2-Q2, R1 AGREE）\n\n---\n\n## Missing References\n\n以下为两位 Reviewer 共同认可应补充的引用（经交叉验证）：\n\n1. **Kumaraguru et al. (2025)** \"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\" — agent self-monitoring 与 catastrophic failure prevention，直接相关（R2 提出，R1 AGREE 如确认存在）\n2. **Agent-SafetyBench (2024)** — 349 个交互环境的 LLM agent 安全评估 benchmark（R2 提出，R1 AGREE）\n3. **Step-level credit assignment 近期文献** — R2 提出具体引用 (arxiv:2604.09459, 2604.11037, 2603.08754)，与 episode-level vs step-level 信号分析相关。R1 认为已引 SALT/CSO 基本覆盖，但额外引用可增强完整性\n4. **Pona et al. (2025)** — 已引用但区分不够详细，应更明确对比 abstract counterfactual (action-level perturbation) vs. episode-level pure-strategy comparison\n5. **ToolEmu (Ruan et al., 2024)** — 已引用但应扩展讨论 emulated sandbox vs. real environment 的方法论对比\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~3.5 分钟）。结果：0 critical, 4 warning, 22 info。\n\n**Warnings**:\n1. **Page 5 纯文本页**：夹在 page 4 (Figure 2) 和 page 6 (Table 1 + Figure 3) 之间，视觉节奏断裂。建议将 Table 1 或 Figure 3 前移平衡密度。\n2. **Pages 7-8 视觉密度偏低**：Discussion + Conclusion 全为纯文本。如能引入小型总结性 figure（如 decision framework 流程图）可改善末尾节奏。\n3. **Page 20 三图挤压**：Figures 5-7 同页（占 55%），Figure 6 标签密集，灰度下可能难区分。\n4. **Page 25 大面积空白**：Responsible NLP Checklist 格式限制导致，非排版错误但不够专业。\n\n**Key Info findings**:\n- 主文 8 页，Conclusion 在 page 8 底部结束，符合 EMNLP 8 页限制 ✓\n- 首个 display item (Figure 1) 在 page 3，前 2 页纯文本——考虑添加 teaser figure\n- 主文 display items 5 个（3 figures + 2 tables），处于推荐 5-8 个的下限\n- 所有表格统一 booktabs 风格，公式渲染无错误，双栏排版对齐良好\n- Figure 4 (bar chart) 建议验证灰度打印区分度\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4.0/5 | 3.5-4.0 |\n| Excitement | 2.5/5 | 2.5/5 | 2.5 |\n| Reproducibility | 4/5 | 4/5 | 4.0 |\n| Overall | 3.0 | 3.0 | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | 4.0 |\n\n**Overall: 3.0 (Findings)** — 可被 Findings 接收，但不达主会议标准。\n\n**核心判断**：这是一篇执行质量很高的诊断性分析论文。统计方法论一流，cross-model validation 扎实，对自身局限性的讨论异常诚实，router negative result 有重要实践价值。但核心发现（death dominance of routing signal）在 oracle vs. hallucinating-LLM 的实验设置下方向可预期，DAF 度量在 ScienceWorld 奖励结构下有 tautological 倾向，单环境 scope 限制了泛化性 claim。**Excitement 是接收瓶颈**（2.5/5），Soundness 充分（3.5-4.0/5）。\n\n**提升路径**（非本 session 职责范围，仅记录 Reviewer 共识方向）：\n1. 在至少一个有 catastrophic failure 的替代环境（如 NetHack）上验证 death dominance → 解决 W3\n2. 更 prominently frame router negative result 为核心贡献 → 部分缓解 W2/W5\n3. 添加 task-level router positive control 实验 → 解决 W4\n4. 将 label fraction 78.9% 作为 headline metric，DAF 降级 → 解决 W1\n5. 收窄 Abstract/Conclusion generality claim → 解决 W3\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- DAF 88-90% 仍作为 prominent metric，建议以 label fraction 78.9% 为 headline\n- \"demonstrating the framework's generality\" overclaim，与 §3.4 \"boundary probes\" 定位不一致\n- \"penalty-independent\" 修饰需精确化\n\n### §1 Introduction\n- 第二段一次引用 11 篇，影响可读性\n- Contribution (2) 和 (3) 对 (1) 有依赖，建议重组\n\n### §2 Method\n- §2.1 脚注中 \"deterministic\" 三种含义的区分应提升到正文\n- §2.4 DAF tautological 讨论已存在，但应在此处加入显式声明：\"the empirically informative quantity is not DAF per se but the prevalence of death asymmetry\"\n- DAF 定义出现在两个等式中（exact + approximate），建议合并\n\n### §3 Experiments\n- §3.1 P=0 label fraction 变化（95→41 non-tie, 51.2% death-asymmetry）被埋在段落中，建议以表格突出\n- §3.4 \"boundary probes (not cross-domain validation)\" 定位正确，但 Abstract/Conclusion 未保持一致\n- §3.6 Router 负结果标题和位置暗示附带发现，实际是最有价值的贡献之一\n\n### §4 Related Work\n- Safe RL 段落（3 行）过于简略，需扩展 CMDP/risk-sensitive RL 讨论\n- Pona et al. (2025) 方法论区分不够详细\n\n### §5 Discussion\n- Non-triviality 段有效但不足以消除 \"obvious in hindsight\" 的 concern\n- 61.2% tie rate 的 implication（routing ROI）未讨论\n- Agent-floor tasks 的 regime 含义未讨论\n\n### §6 Conclusion\n- 过于简短（单段 ~60 词），需扩展至 2-3 段\n\n### Limitations\n- 覆盖全面（5 个 paragraph），长度合理\n- Pure-strategy upper bound 段落到位\n\n### Format/Misc\n- 8 个 orphan bib entries 需清理\n- Webb (2023) 年份需再次核实\n- Table 1 caption \"20-40 episodes per type\" 但实际仅 find-non-living-thing 有 40\n- ScienceWorld 版本号应全文统一（Appendix C 标 v1.2.3）\n- Gajcin (2023) OpenAlex confidence 0.78，建议核实",
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
    "report": "# 审稿报告 — Round 25 (Fresh Review)\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**投稿类别**: Interpretability and Analysis of Models for NLP\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+相关工作）\n**审稿轮次**: 1 轮（Round 1 初审 → 交叉分享 → 收敛，关键问题全部达成共识）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，比较 LLM agent 在 pure-internal（ReAct）与 pure-deterministic（oracle simulator）策略下的 episode 结果，分解 routing signal 的来源。核心发现：在 ScienceWorld 的 11 类任务（245 episodes）中，78.9% 的 non-tie routing labels 源自 death asymmetry——internal 策略触发 −100 惩罚的灾难性失败而 deterministic 策略存活。引入 Death Avoidance Factor (DAF) 量化该效应（DAF=90.4%），跨三个模型家族（Qwen-7B/Llama-8B/Gemma-9B, DAF 88-90%）和 72B scaling 验证一致性。Cross-environment boundary probes（MATH 无信号、ALFWorld 信息不对称）展示框架在不同机制下的诊断能力。Router 训练得到负结果（step-level balanced accuracy 56-59%），归因于 death avoidance 是 task-type-level 而非 step-level 信号。\n\n---\n\n## Strengths\n\n**S1. 研究问题有价值且切入角度新颖 [共识]。** 现有 routing/tool-use 工作集中于\"如何建 router\"，本文退一步问\"routing signal 到底是什么\"。这种\"先诊断再优化\"的方法论对 agent routing 社区有指导意义，切入了一个被忽视的诊断性问题。\n\n**S2. 统计方法论一流 [共识]。** Bootstrap resampling (B=10,000)、cluster bootstrap sensitivity (K=11, 含 wild cluster bootstrap)、Signal Concentration Index (SCI)、leave-one-task-out stability analysis、per-task CIs、dose-response analysis、Cohen's d——统计工具链完整且使用得当，远超多数 agent 论文的 reporting 标准。95% CIs 贯穿全文所有 quantitative claims。对 K=11 cluster bootstrap power 不足的问题也诚实讨论（Cameron et al. 2008 推荐 K≥20-30）。\n\n**S3. 对自身局限性的坦诚讨论 [共识]。** 论文对局限性的讨论异常透明——r=0.97 correlation 是 structural consequence（§3.1）、DAF 是 penalty-dependent（§2.4）、router 是 negative result（§3.6）、task exclusion 有完整分析（Appendix C/S）。这种 intellectual honesty 在同类论文中罕见。\n\n**S4. Cross-model validation 扎实 [共识]。** 三个架构不同的模型族（Qwen/Llama/Gemma）独立收敛于 DAF 88-90%（spread 2.2pp），加上 72B scaling (DAF=92.4%)，构成 convincing 的 robustness evidence。Appendix M 提供完整 per-task 分解。\n\n**S5. Router negative result 有价值 [共识]。** §3.6 的 step-level router 无法捕获 task-type-level 信号是一个重要实践性发现，能帮社区避免无效的 router 开发投入。Appendix P 的 generative router (46.7%) 进一步确认瓶颈在 signal 而非 architecture。两位 Reviewer 一致认为这可能是论文最有实践价值的贡献。\n\n**S6. 附录极其详尽 [共识]。** 20 个 Appendices (A-T) 覆盖 task selection rationale、correlation robustness、penalty sensitivity、failure mode taxonomy、grounding ablation、prompt templates 等，可复现性极高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [Critical, 共识] DAF 度量在 ScienceWorld 奖励结构下有 tautological 倾向。**\nDAF = δP/(δP + Δ_nd) 在 P=100、Δ_nd=2.84 的条件下必然趋近 1——这是代数事实而非经验发现。论文在 §2.4 和 §3.1 已承认（\"mathematical consequence rather than an empirical finding\"、\"the 78.9% label fraction provides the more robust characterization\"），但 Abstract 和 Introduction 仍将 DAF 88-90% 作为 prominent metric 呈现。真正有信息量的经验发现是 label fraction (78.9%)，而非 DAF 数值本身。两位 Reviewer 建议：明确将 label fraction 作为 headline metric，DAF 降级为 supplementary score-weighted measure。（R1-W1, R2 交叉 AGREE）\n\n**W2 [Critical, 共识] 核心发现的新颖性有限——death dominance 在实验设置下方向可预期。**\nOracle simulator 提供 ground-truth state transitions，而 internal 策略依赖会幻觉的 LLM。在 −100 death penalty 下，oracle 天然比幻觉策略更安全——death asymmetry 的 *存在* 是可预期的。§5 的 non-triviality 论证（72B 未消除、Reflexion DAF>100%、inverted-U）是关于 death dominance 的 *persistence*，而非 *existence* 的 surprise。R1 交叉回应中指出：prevalence 量化（78.9%）和 router negative result 仍有 surprise value（Δ_nd≈2.84 near-uniform 需要实证确认；router failure 不可从设置预测）。但两位 Reviewer 共识 Excitement 仅 2.5/5，这是 Findings 而非 Conference 水平的核心原因。此问题不可通过 writing 修复——需新环境深度分析或根本性新发现。（R2-N1, R1 AGREE with nuance）\n\n**W3 [Critical, 共识] 单环境 scope + generality overclaim。**\n主实验仅在 ScienceWorld 上进行。MATH（84.4% no-preference）和 ALFWorld（DAF=0%, 无死亡机制）作为 boundary probes 只展示框架的诊断能力多样性，不能验证 death-dominance 发现是否泛化到其他有灾难性失败的环境。论文正文 §3.4 已将 MATH/ALFWorld 定位为 \"boundary probes (not cross-domain validation)\"，但 Abstract (\"demonstrating the framework's generality\") 和 Conclusion 措辞仍在 overclaim。bib 中有 NetHack/MiniHack/BALROG/Crafter 等有 catastrophic failure 的环境但均为 orphan references。建议：(a) 降低 Abstract/Conclusion generality claim 至与 §3.4 一致；(b) 在至少一个有 permadeath 的替代环境上验证（如 NetHack）。（R1-W2, R2-N2, 交叉 mutual AGREE）\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4 [Warning, 共识] Router negative result 替代解释未充分排除。**\n§3.6 claim \"signal-limited, not architecture-limited\" 但未充分排除：(a) 训练数据规模极小（245 episodes/~2040 steps），paraphrase augmentation ≠ 真实数据扩增；(b) router 仅 0.6B-4B，更大模型或不同架构未测试；(c) 缺少 task-level router positive control（输入 task type → 输出 routing decision）。Appendix P leave-one-task-out 中 keyword variant 62.9% 间接证明 task-type identification 是唯一可学信号，但显式实验会更 clean。建议弱化 absolute claim 并添加 task-level router 实验。（R1-W4, R2 AGREE）\n\n**W5 [Warning, 共识] Contribution framing 不清晰——三条 contribution 存在依赖关系。**\n(1) 框架 → (2) 应用于 ScienceWorld → (3) robustness check，是层层依赖而非独立并列。R1 REBUT 指出 router negative result 有独立价值，排序应为 (a) router failure > (b) 78.9% prevalence > (c) 框架本身。共识：不构成 blocking issue，但 contribution statement 应更清晰区分方法论贡献与实证 insight，并更 prominently frame router failure。（R2-N3, R1 partial REBUT but agrees on framing improvement）\n\n**W6 [Warning, 共识] Conclusion 过于单薄。**\n单段约 60 词，对于 8 页正文 + 20 个 Appendix 的 long paper，未讨论 broader implications、future work 方向、或对 NLP community 的 takeaway。建议扩展至 2-3 段（在 8 页预算内）。（R2-W3, R1 AGREE）\n\n**W7 [Warning, 共识] \"penalty-independent\" 表述在 Abstract/Intro 中有误导性。**\nLabel fraction 数值不依赖 P，但 P=0 时 54 个 sole-signal labels 变为 ties（non-tie 从 95 降至 41），routing signal 的实际 relevance 高度依赖 penalty magnitude。建议改为更精确表述如 \"invariant to penalty magnitude in the labeling procedure\"。（R2-W2, R1 AGREE）\n\n**W8 [Warning, 共识] Safe RL 相关工作覆盖不足。**\n§4 Safe RL 段落仅 3 行，引用 5 篇经典 + 2 篇近期。鉴于核心发现是 catastrophic failure avoidance dominates routing signal，应更详细讨论与 constrained MDPs/risk-sensitive RL 的关系，以及为什么 Safe RL 方案（如 CPO）不直接适用于 LLM agent routing。（R2-W4, R1 AGREE）\n\n**W9 [Warning, 共识] Task selection (11/30) 的 agent-floor tasks 含义未讨论。**\n63% exclusion rate 有合理理由且 anti-cherry-picking 分析到位（Appendix C/S），但 7 个 agent-floor tasks 代表什么 regime 未讨论——如果两策略都频繁死亡（无 asymmetry），routing signal 可能由非 death 因素驱动，这是 death dominance 不成立的有趣案例。建议在 Discussion 补充。（R1-W3, R2-W1, R2 partial REBUT on data availability but AGREE on framing）\n\n**W10 [Warning, R1 提出] 实验规模偏小，per-task 统计 power 不足。**\nPer-task n=20，Wilson CI ~±20pp。Table 1 caption 已标注 exploratory。共识：aggregate claims (N=245) 可靠，per-task 需谨慎解读。不构成 blocking issue。（R1-W5, R2 AGREE）\n\n**W11 [Warning, R1 提出] 实际指导价值有限。**\n诊断之外缺少 constructive 解决路径。Appendix R Decision Framework 有 retrospective 4/4 validation（R2 指出非\"未验证\"），但 grounding ablation (Appendix O, death rate 48%→29%) 是有潜力的方向，应在主文给更多篇幅。论文定位为 diagnostic 非 prescriptive（Limitations 明确声明），此定位本身可接受但降低了 impact。（R1-W6, R2 partial REBUT）\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致（所有交叉回应为 [AGREE]）：\n1. DAF 在 ScienceWorld 奖励结构下有 tautological 倾向，label fraction 应为 headline metric\n2. 单环境 scope 限制泛化性，Abstract/Conclusion generality claim 需收窄\n3. 核心发现方向可预期，Excitement 不足（均 2.5/5）\n4. Router negative result 被 underframed，应提升为核心 contribution\n5. Conclusion 过于简短\n6. Safe RL 覆盖不足\n7. Per-task power 有限但 aggregate 可靠\n8. Overall 3.0 (Findings)\n\n## Reviewer Divergence\n\n仅有轻微分歧，均已在交叉回应中解决：\n\n1. **Contribution 独立性 (R2-N3)**：R2 认为三条 contribution 的依赖关系使 overall contribution 难以评估；R1 REBUT 指出 router negative result 有独立价值。**Director 判断**：R1 的 rebut 有道理，但不改变 overall score——contribution framing 需改进但非 blocking。\n\n2. **Task selection 数据可用性 (R1-W3)**：R1 声称 excluded tasks 数据未展示；R2 REBUT 指出 Appendix C Table 4 和 Appendix S 已提供。**Director 判断**：R2 的事实纠正正确，R1 可能遗漏了附录数据。但 R1 的深层观点（agent-floor tasks 的 regime 含义）成立。\n\n3. **Practical guidance (R1-W6)**：R1 称 Decision Framework \"未验证\"；R2 REBUT 指出有 retrospective 4/4 validation。**Director 判断**：R2 的事实纠正正确（有 post-hoc validation），但 R1 对 constructive 方案缺失的批评仍然有效。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** P=0 时 label fraction 从 78.9% 降至 51.2%（§3.1 已有数据）——建议以表格形式突出展示 P=0/10/50/100/200 的 label fraction 变化，而非仅在段落中提及。\n\n**Q2.** 61.2% tie rate (150/245) 意味着 routing 最多改善 38.8% 的 episodes。这对 routing 系统的实际 ROI 意味什么？建议在 Discussion 中增加分析。（R2-Q3, R1 AGREE 称\"R2 最有洞察力的问题之一\"）\n\n**Q3.** 2.6% 有差异的步骤（159/6094）是否集中在 death-triggering 步骤？Appendix P 的 death-proximal labeling 间接涉及但缺少 descriptive analysis。（R1-Q2）\n\n**Q4.** Grounding ablation (Appendix O) 将 death rate 从 48% 降至 29%。在此条件下重新计算 DAF 的值是多少？（R1-Q3, R2 AGREE——这将验证框架对 intervention 的敏感性）\n\n**Q5.** 0.5B inverted-U claim 基于 n=15，Wilson CI 极宽。是否有足够统计 power 区分 inverted-U 和 random fluctuation？（R2-Q4, R1 AGREE）\n\n**Q6.** \"deterministic\" 统称 oracle simulator (ScienceWorld)、code interpreter (MATH)、admissible-action access (ALFWorld) 三种性质不同的 information advantage。§2.1 脚注有简要说明，但主文应更显式区分以避免误导读者认为 cross-environment 比较是 apples-to-apples。（R2-Q2, R1 AGREE）\n\n---\n\n## Missing References\n\n以下为两位 Reviewer 共同认可应补充的引用（经交叉验证）：\n\n1. **Kumaraguru et al. (2025)** \"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\" — agent self-monitoring 与 catastrophic failure prevention，直接相关（R2 提出，R1 AGREE 如确认存在）\n2. **Agent-SafetyBench (2024)** — 349 个交互环境的 LLM agent 安全评估 benchmark（R2 提出，R1 AGREE）\n3. **Step-level credit assignment 近期文献** — R2 提出具体引用 (arxiv:2604.09459, 2604.11037, 2603.08754)，与 episode-level vs step-level 信号分析相关。R1 认为已引 SALT/CSO 基本覆盖，但额外引用可增强完整性\n4. **Pona et al. (2025)** — 已引用但区分不够详细，应更明确对比 abstract counterfactual (action-level perturbation) vs. episode-level pure-strategy comparison\n5. **ToolEmu (Ruan et al., 2024)** — 已引用但应扩展讨论 emulated sandbox vs. real environment 的方法论对比\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~3.5 分钟）。结果：0 critical, 4 warning, 22 info。\n\n**Warnings**:\n1. **Page 5 纯文本页**：夹在 page 4 (Figure 2) 和 page 6 (Table 1 + Figure 3) 之间，视觉节奏断裂。建议将 Table 1 或 Figure 3 前移平衡密度。\n2. **Pages 7-8 视觉密度偏低**：Discussion + Conclusion 全为纯文本。如能引入小型总结性 figure（如 decision framework 流程图）可改善末尾节奏。\n3. **Page 20 三图挤压**：Figures 5-7 同页（占 55%），Figure 6 标签密集，灰度下可能难区分。\n4. **Page 25 大面积空白**：Responsible NLP Checklist 格式限制导致，非排版错误但不够专业。\n\n**Key Info findings**:\n- 主文 8 页，Conclusion 在 page 8 底部结束，符合 EMNLP 8 页限制 ✓\n- 首个 display item (Figure 1) 在 page 3，前 2 页纯文本——考虑添加 teaser figure\n- 主文 display items 5 个（3 figures + 2 tables），处于推荐 5-8 个的下限\n- 所有表格统一 booktabs 风格，公式渲染无错误，双栏排版对齐良好\n- Figure 4 (bar chart) 建议验证灰度打印区分度\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4.0/5 | 3.5-4.0 |\n| Excitement | 2.5/5 | 2.5/5 | 2.5 |\n| Reproducibility | 4/5 | 4/5 | 4.0 |\n| Overall | 3.0 | 3.0 | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | 4.0 |\n\n**Overall: 3.0 (Findings)** — 可被 Findings 接收，但不达主会议标准。\n\n**核心判断**：这是一篇执行质量很高的诊断性分析论文。统计方法论一流，cross-model validation 扎实，对自身局限性的讨论异常诚实，router negative result 有重要实践价值。但核心发现（death dominance of routing signal）在 oracle vs. hallucinating-LLM 的实验设置下方向可预期，DAF 度量在 ScienceWorld 奖励结构下有 tautological 倾向，单环境 scope 限制了泛化性 claim。**Excitement 是接收瓶颈**（2.5/5），Soundness 充分（3.5-4.0/5）。\n\n**提升路径**（非本 session 职责范围，仅记录 Reviewer 共识方向）：\n1. 在至少一个有 catastrophic failure 的替代环境（如 NetHack）上验证 death dominance → 解决 W3\n2. 更 prominently frame router negative result 为核心贡献 → 部分缓解 W2/W5\n3. 添加 task-level router positive control 实验 → 解决 W4\n4. 将 label fraction 78.9% 作为 headline metric，DAF 降级 → 解决 W1\n5. 收窄 Abstract/Conclusion generality claim → 解决 W3\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- DAF 88-90% 仍作为 prominent metric，建议以 label fraction 78.9% 为 headline\n- \"demonstrating the framework's generality\" overclaim，与 §3.4 \"boundary probes\" 定位不一致\n- \"penalty-independent\" 修饰需精确化\n\n### §1 Introduction\n- 第二段一次引用 11 篇，影响可读性\n- Contribution (2) 和 (3) 对 (1) 有依赖，建议重组\n\n### §2 Method\n- §2.1 脚注中 \"deterministic\" 三种含义的区分应提升到正文\n- §2.4 DAF tautological 讨论已存在，但应在此处加入显式声明：\"the empirically informative quantity is not DAF per se but the prevalence of death asymmetry\"\n- DAF 定义出现在两个等式中（exact + approximate），建议合并\n\n### §3 Experiments\n- §3.1 P=0 label fraction 变化（95→41 non-tie, 51.2% death-asymmetry）被埋在段落中，建议以表格突出\n- §3.4 \"boundary probes (not cross-domain validation)\" 定位正确，但 Abstract/Conclusion 未保持一致\n- §3.6 Router 负结果标题和位置暗示附带发现，实际是最有价值的贡献之一\n\n### §4 Related Work\n- Safe RL 段落（3 行）过于简略，需扩展 CMDP/risk-sensitive RL 讨论\n- Pona et al. (2025) 方法论区分不够详细\n\n### §5 Discussion\n- Non-triviality 段有效但不足以消除 \"obvious in hindsight\" 的 concern\n- 61.2% tie rate 的 implication（routing ROI）未讨论\n- Agent-floor tasks 的 regime 含义未讨论\n\n### §6 Conclusion\n- 过于简短（单段 ~60 词），需扩展至 2-3 段\n\n### Limitations\n- 覆盖全面（5 个 paragraph），长度合理\n- Pure-strategy upper bound 段落到位\n\n### Format/Misc\n- 8 个 orphan bib entries 需清理\n- Webb (2023) 年份需再次核实\n- Table 1 caption \"20-40 episodes per type\" 但实际仅 find-non-living-thing 有 40\n- ScienceWorld 版本号应全文统一（Appendix C 标 v1.2.3）\n- Gajcin (2023) OpenAlex confidence 0.78，建议核实",
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

_source line 2083 · 2026-05-21T15:13:50.324061+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4519
}
```

</details>

---


### Tool call

_source line 2084 · 2026-05-21T15:13:54.746174+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Synthesize consolidated review report', 'status': 'completed', 'activeForm': 'Synthesizing consolidated review report'}, {'content': 'Update review_issues.yaml tracker', 'status': 'completed', 'activeForm': 'Updating review issues tracker'}, {'content': 'Submit report to Research Director', 'status': 'completed', 'activeForm': 'Submitting report to Research Director'}]"
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
    "todos": "[{'content': 'Synthesize consolidated review report', 'status': 'completed', 'activeForm': 'Synthesizing consolidated review report'}, {'content': 'Update review_issues.yaml tracker', 'status': 'completed', 'activeForm': 'Updating review issues tracker'}, {'content': 'Submit report to Research Director', 'status': 'completed', 'activeForm': 'Submitting report to Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 2085 · 2026-05-21T15:13:54.746723+00:00_

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

_source line 2086 · 2026-05-21T15:14:04.165918+00:00_

审稿流程全部完成。

**Round 25 审稿报告已投递给 Research Director。**

核心结论：**Overall 3.0 (Findings)**，两位 Reviewer 完全一致。

评分分布：
- Soundness: 3.5-4.0/5（统计方法严谨，decomposition 数学正确）
- Excitement: 2.5/5（**接收瓶颈**——death dominance 在 oracle vs. hallucinating-LLM 设置下方向可预期）
- Reproducibility: 4.0/5

三个 Critical 问题（共识）：
1. **DAF tautological**：DAF 高值是 P=100 下的代数必然，label fraction 78.9% 才是真正的 empirical finding
2. **Novelty 不足**：核心发现方向可预期，§5 non-triviality 论证仅关于 persistence 非 existence
3. **单环境 scope**：MATH/ALFWorld 为退化 boundary probes，框架在 non-obvious 场景的诊断价值未验证

Issue tracker 已同步更新至 `review_issues.yaml`（13 个 open issues, 含 3 critical + 8 warning + 2 info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 171

## Round 171

2 recorded events


### User

_source line 2087 · 2026-05-21T15:14:06.722469+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 6 个 Weaknesses：3 个 [AGREE]（W1 DAF tautological、W2 单环境、W5 per-task power）、2 个 [REBUT]（W3 excluded tasks 数据实际已提供、W6 decision framework 有 retrospective validation）、1 个 [AGREE] 但补充了更深层论点（W4 router alternative explanations）。两位 reviewer 在核心判断上高度一致：Overall 3.0 (Findings)，Soundness 合格但 Excitement 不足。

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

_source line 2088 · 2026-05-21T15:14:16.621331+00:00_

审稿报告已在上轮提交完毕。Round 25 圆桌审稿全流程已完成：

- **Round 1 初审** → 两位 Reviewer 独立审稿（R1: 3.0, R2: 3.0）
- **交叉分享** → 逐条 [AGREE]/[REBUT] 回应，关键问题全部达成共识
- **收敛判断** → 1 轮即收敛，无需额外轮次
- **报告合成 & 投递** → 已提交至 Research Director
- **Issue Tracker** → 已更新至 `review_issues.yaml`

**最终评分：Overall 3.0 (Findings)**，Excitement 2.5 是接收瓶颈。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 172

## Round 172

70 recorded events


### User

_source line 2089 · 2026-05-21T22:03:27.525962+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Interpretability and Analysis
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

_source line 2090 · 2026-05-21T22:03:33.648605+00:00_

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

_source line 2091 · 2026-05-21T22:03:33.649379+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2092 · 2026-05-21T22:03:40.258195+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,WebFetch,TodoWrite",
  "max_results": "12"
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
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,WebFetch,TodoWrite",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 2093 · 2026-05-21T22:03:40.308955+00:00_



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

_source line 2094 · 2026-05-21T22:03:44.927683+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2095 · 2026-05-21T22:03:44.928090+00:00_



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

_source line 2096 · 2026-05-21T22:03:54.317702+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2097 · 2026-05-21T22:03:54.318275+00:00_

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

_source line 2098 · 2026-05-21T22:03:57.932879+00:00_

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

_source line 2099 · 2026-05-21T22:03:59.338918+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

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

_source line 2100 · 2026-05-21T22:03:59.791174+00:00_

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

_source line 2101 · 2026-05-21T22:04:00.595094+00:00_

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
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2102 · 2026-05-21T22:04:00.645822+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines page limit template site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers ARR submission guidelines page limit template site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2103 · 2026-05-21T22:04:00.947406+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
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
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2104 · 2026-05-21T22:04:01.098499+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/SETUP_NOTES.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/gen_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/pipeline_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/_pdf_images/fig1_daf_scatter_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/_pdf_images/pipeline_overview_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/_pdf_images/signal_reversal_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/death_action_distribution.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/sim
…[truncated 3309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 2105 · 2026-05-21T22:04:07.473668+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines page limit template site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on my search results, I found information about EMNLP 2026 call for papers and ARR submission guidelines. Here's what I found:

## EMNLP 2026 C
…[truncated 1394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6827
}
```

</details>

---


### Tool call

_source line 2106 · 2026-05-21T22:04:18.184039+00:00_

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


### Tool call

_source line 2107 · 2026-05-21T22:04:19.539701+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission guidelines for ACL Rolling Review: page limits for long and short papers, template requirements, anonymity rules, appendix rules, formatting requirements, and any other submission criteria. Include all specific numbers and deadlines."
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
    "prompt": "Extract the complete submission guidelines for ACL Rolling Review: page limits for long and short papers, template requirements, anonymity rules, appendix rules, formatting requirements, and any other submission criteria. Include all specific numbers and deadlines."
  }
}
```

</details>

---


### Tool call

_source line 2108 · 2026-05-21T22:04:19.791276+00:00_

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

_source line 2109 · 2026-05-21T22:04:19.892178+00:00_

1	\begin{abstract}
2	LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs.\ deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9\% of non-tie routing labels arise from death asymmetry: the internal strategy triggers catastrophic failure while the deterministic strategy survives. This label fraction is penalty-independent. A derived score-weighted measure, the Death Avoidance Factor, reaches 88--90\% across three model families (Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B), confirming convergence on a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), illustrating the framework's applicability. A ${\sim}$50-episode diagnostic pilot suffices to identify the dominant routing mechanism in a new environment, enabling informed build-vs-buy decisions before expensive router training.
3	\end{abstract}
4	

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

_source line 2110 · 2026-05-21T22:04:19.892738+00:00_

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

_source line 2111 · 2026-05-21T22:04:19.944159+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \citep{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone, as the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated), while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \citep{toolformer-2023} inserts API calls by perplexity reduction; ART \citep{art-2023} decomposes tasks into tool-augmented programs; Chameleon \citep{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \citep{cogrouter-2026,ares-2026}, model tiers \citep{mtrouter-2026}, or episode-level model selection under sparse rewards \citep{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. The shared assumption---that routing signal stems from diverse sources and a learned router can exploit it---remains untested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under ScienceWorld's penalty ($P{=}100$), DAF reaches $90.4\%$ (95\% CI: $[81.1\%, 9
…[truncated 2509 chars]

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


### Tool result

_source line 2112 · 2026-05-21T22:04:23.961634+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

More specifically:
- **Long Papers:** Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be giv
…[truncated 1021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5777
}
```

</details>

---


### Tool result

_source line 2113 · 2026-05-21T22:04:25.568522+00:00_

# ACL Rolling Review Submission Guidelines

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

Papers exceeding length requirements or lacking a limitations section face desk rejection.

## Template & Formatting

Submissions must use "the official ACL style template" available on GitHub. Authors cannot modify style files or use templates from other conferences. All text must be "addressed exclusively to the human readers and be clearly visible to them." Formatting violations regarding paper size, margins, and font restrictions result in rejection without review.

## Anonymity Requirements

Papers must exclude author names and affiliations. Self-citations should be formatted as "Smith previously showed (Smith, 1991)…" rather than first-person references. Links to file hosting services like Dropbox are prohibited. All supplementary materials, including repository links, require anonymization. Violations lead to desk rejection.

## Appendices

Appendices follow the main paper and references, remaining outside page limits. They must maintain double-column formatting per ACLPUB guidelines, with limited exceptions. Key technical content essential for assessing novelty should appear in the main paper, not appendices.

## Other Critical Requirements

- **Limitations section:** Required, untitled variations unacceptable
- **Responsible NLP Checklist:** Mandatory; incomplete or misleading responses invite desk rejection
- **Reviewer participation:** All authors must register and contribute reviews unless exempted
- **Author registration:** Completion required within 48 hours of submission deadline
- **Resubmission documentation:** Must include previous submission links and detailed revision 
…[truncated 9 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "elapsed_ms": 6028
}
```

</details>

---


### Tool call

_source line 2114 · 2026-05-21T22:04:33.248892+00:00_

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

_source line 2115 · 2026-05-21T22:04:33.902098+00:00_

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
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 2116 · 2026-05-21T22:04:33.902463+00:00_

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

_source line 2117 · 2026-05-21T22:04:34.153866+00:00_

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
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2118 · 2026-05-21T22:04:34.254753+00:00_

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

_source line 2119 · 2026-05-21T22:04:34.657422+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	Self-supervised methods learn tool invocation from loss signals \citep{toolformer-2023,toolace-2025}, token-level methods embed tools in the vocabulary \citep{toolkengpt-2023}, task-level decomposition routes subtasks to specialized modules \citep{art-2023,chameleon-2023}, and RL-based methods learn routing from reward \citep{retool-2025}.
6	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Concurrent work examines \emph{when} to invoke tools: tool-call decisions correlate with uncertainty~\citep{tool-overuse-illusion-2026}, are encoded in hidden states~\citep{when2tool-2026}, impose a ``tool-use tax''~\citep{tool-use-tax-2026}, or follow necessity-utility-affordability logic~\citep{to-call-or-not-2026}. Our decomposition yields a concrete answer: 78.9\% of non-tie routing labels trace to catastrophic-failure prevention.
8	
9	\paragraph{Adaptive Computation and Routing.}
10	Adaptive routing traces back to learned halting policies \citep{graves2016act}. In the LLM era, CogRouter \citep{cogrouter-2026} adapts reasoning depth per step, ARES \citep{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \citep{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \citep{mtrouter-2026} addresses multi-turn routing.
11	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
12	\citet{budget-aware-routing-2026} train episode-level routing policies under sparse terminal rewards, the closest setting to ours; they optimize \emph{which} model to invoke, whereas we diagnose \emph{what} drives the routing decision.
13	
14	\paragraph{Counterfactual Evaluation in RL.}
15	Prior work generates cou
…[truncated 1803 chars]

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

_source line 2120 · 2026-05-21T22:04:34.657819+00:00_

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

_source line 2121 · 2026-05-21T22:04:34.658097+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2122 · 2026-05-21T22:04:35.612183+00:00_

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

_source line 2123 · 2026-05-21T22:04:35.913765+00:00_

1	\section{Conclusion}
2	
3	In ScienceWorld, death avoidance alone accounts for 78.9\% of non-tie routing labels, stable across three model families (DAF${=}88$--$90\%$); our episode-level counterfactual framework diagnoses this before any router is built, challenging the assumption of diverse signal sources. Cross-environment probes illustrate applicability; a ${\sim}$50-episode pilot suffices for build-vs-buy decisions in new environments. Future work should validate death dominance in additional catastrophic-failure environments and develop routing methods that exploit task-type-level signals.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2124 · 2026-05-21T22:04:35.914232+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "review_issues.yaml"
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
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2125 · 2026-05-21T22:04:36.014898+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2126 · 2026-05-21T22:04:43.183002+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2127 · 2026-05-21T22:04:44.138695+00:00_

&lt;persisted-output>
Output too large (29.6KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing--claude-sessions-review-director-19d7e797/e80a30b9-b7a8-4a22-bd5f-d4f61e440bec/tool-results/bownz9dzd.txt

Preview (first 2KB):
# Round 25 Review Issues (fresh review, 2026-05-21)
# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+相关工作)

# =============================================
# Carried-over resolved issues (from prior rounds)
# =============================================

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
  summa
…[truncated 336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 2128 · 2026-05-21T22:04:44.139262+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/project_config.yaml 2>/dev/null | head -80",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/project_config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2129 · 2026-05-21T22:04:45.043362+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2130 · 2026-05-21T22:04:45.194313+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"",
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
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2131 · 2026-05-21T22:04:45.295319+00:00_

Pages:           23

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

_source line 2132 · 2026-05-21T22:04:49.311707+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2133 · 2026-05-21T22:04:49.613360+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/’: No such file or directory

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

_source line 2134 · 2026-05-21T22:04:49.613703+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml",
  "limit": "60",
  "offset": "0"
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
    "limit": "60",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 2135 · 2026-05-21T22:04:49.664266+00:00_

0	# Round 25 Review Issues (fresh review, 2026-05-21)
1	# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+相关工作)
2	
3	# =============================================
4	# Carried-over resolved issues (from prior rounds)
5	# =============================================
6	
7	- id: "R13-W1"
8	  summary: "正文篇幅严重不足 long paper 要求"
9	  category: format
10	  severity: warning
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 14
14	  resolution: "正文已扩展至 8 页"
15	  resolution_round: 14
16	
17	- id: "R13-W2"
18	  summary: "Router 训练实验存在多个 confound"
19	  category: experiment
20	  severity: warning
21	  status: resolved
22	  first_raised_round: 13
23	  last_seen_round: 15
24	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
25	  resolution_round: 15
26	
27	- id: "R13-W3"
28	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
29	  category: method
30	  severity: info
31	  status: resolved
32	  first_raised_round: 13
33	  last_seen_round: 14
34	  resolution: "Limitations 和 Appendix B 已充分量化"
35	  resolution_round: 14
36	
37	- id: "R13-W4"
38	  summary: "SCI 方法贡献与实际使用不成比例"
39	  category: method
40	  severity: info
41	  status: resolved
42	  first_raised_round: 13
43	  last_seen_round: 14
44	  resolution: "SCI 已降级到 Appendix A"
45	  resolution_round: 14
46	
47	- id: "R13-W7"
48	  summary: "Router negative results 解释不完整"
49	  category: experiment
50	  severity: warning
51	  status: resolved
52	  first_raised_round: 13
53	  last_seen_round: 15
54	  resolution: "Router 实验定位为 diagnostic probe"
55	  resolution_round: 15
56	
57	- id: "R13-m2"
58	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
59	  category: writing

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

_source line 2136 · 2026-05-21T22:04:56.140921+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 2137 · 2026-05-21T22:04:56.241850+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/experiment_plan.yaml

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

_source line 2138 · 2026-05-21T22:05:00.612242+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/project_configs/simgate-modular-routing.yaml 2>/dev/null | head -60 || find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ -name \"*.yaml\" 2>/dev/null | head -10",
  "description": "Find project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/project_configs/simgate-modular-routing.yaml 2>/dev/null | head -60 || find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ -name \"*.yaml\" 2>/dev/null | head -10",
    "description": "Find project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2139 · 2026-05-21T22:05:00.863738+00:00_

(Bash completed with no output)

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

_source line 2140 · 2026-05-21T22:05:04.078222+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 3 -name \"project_config*\" -o -name \"config.yaml\" 2>/dev/null | head -10",
  "description": "Search for project config file"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 3 -name \"project_config*\" -o -name \"config.yaml\" 2>/dev/null | head -10",
    "description": "Search for project config file"
  }
}
```

</details>

---


### Tool result

_source line 2141 · 2026-05-21T22:05:04.179186+00:00_

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

_source line 2142 · 2026-05-21T22:05:07.242098+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 2 -name \"*.yaml\" | head -20",
  "description": "List YAML files at top level"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/ -maxdepth 2 -name \"*.yaml\" | head -20",
    "description": "List YAML files at top level"
  }
}
```

</details>

---


### Tool result

_source line 2143 · 2026-05-21T22:05:07.292792+00:00_

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

_source line 2144 · 2026-05-21T22:05:15.280545+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ 2>/dev/null | head -10",
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
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ 2>/dev/null | head -10",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2145 · 2026-05-21T22:05:15.632619+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2146 · 2026-05-21T22:05:15.633321+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml 2>/dev/null | head -80",
  "description": "Check workspace config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml 2>/dev/null | head -80",
    "description": "Check workspace config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2147 · 2026-05-21T22:05:15.683912+00:00_

projects: {}

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

_source line 2148 · 2026-05-21T22:05:50.434678+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2149 · 2026-05-21T22:05:50.435138+00:00_

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

_source line 2150 · 2026-05-21T22:05:52.091930+00:00_

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

_source line 2151 · 2026-05-21T22:05:53.045826+00:00_

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

_source line 2152 · 2026-05-21T22:06:09.994261+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17902
}
```

</details>

---


### Tool result

_source line 2153 · 2026-05-21T22:06:09.994727+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 16948
}
```

</details>

---


### Tool call

_source line 2154 · 2026-05-21T22:06:10.046200+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Interpretability and Analysis\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求\n- Long paper 正文 ≤ 8 页，参考文献不限页数\n- Limitations 章节必须有，不计入页数\n- Ethics Statement 不计入页数\n- ACL 模板 (`\\usepackage[review]{acl}`)，double-blind\n- Appendices 在参考文献之后，不计入页数\n- Responsible NLP Checklist 在 OpenReview submission form 中填写（不在 PDF 中）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **Counterfactual Framework 的数学严谨性**：\n   - DAF 的定义和推导是否自洽？DAF 与 label fraction 的关系是否清晰？\n   - 分解公式 Δ_full ≈ δP + Δ_nd 的近似精度和适用条件\n   - Episode-level labeling algorithm 是否有 edge cases 或逻辑漏洞\n\n2. **统计方法**：\n   - Bootstrap resampling (B=10,000) 的合理性\n   - Cluster bootstrap (K=11) 的局限性是否充分讨论\n   - Wild cluster bootstrap 的使用是否正确\n   - Cohen's d = 3.02 在 K=11 下的可解释性\n   - 多重比较校正（Bonferroni）的使用\n\n3. **实验设计与控制**：\n   - 11/30 task types 的选择标准是否合理？排除 63% 的 task types 是否会导致 selection bias？\n   - N=245 episodes 的 power analysis\n   - 纯策略比较的生态效度（real-world applicability）\n   - Cross-model validation (3 models) 的充分性：都在 7-9B 范围，72B 仅作为 agent improvement\n   - Cross-environment probes (MATH, ALFWorld) 的深度是否足够支撑 generalizability claims\n   - Router training negative result 的可信度：是真的学不到，还是实验设置限制了\n\n4. **内部一致性**：\n   - 正文 claims 与数据/表格/图表是否一致\n   - Limitations 是否充分覆盖方法论弱点\n   - 各 Appendix 与正文的交叉引用是否准确\n\n请按 ARR 审稿标准给出详细评审意见，包含 Strengths、Weaknesses、Questions、Minor Issues。"
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
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Interpretability and Analysis\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求\n- Long paper 正文 ≤ 8 页，参考文献不限页数\n- Limitations 章节必须有，不计入页数\n- Ethics Statement 不计入页数\n- ACL 模板 (`\\usepackage[review]{acl}`)，double-blind\n- Appendices 在参考文献之后，不计入页数\n- Responsible NLP Checklist 在 OpenReview submission form 中填写（不在 PDF 中）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **Counterfactual Framework 的数学严谨性**：\n   - DAF 的定义和推导是否自洽？DAF 与 label fraction 的关系是否清晰？\n   - 分解公式 Δ_full ≈ δP + Δ_nd 的近似精度和适用条件\n   - Episode-level labeling algorithm 是否有 edge cases 或逻辑漏洞\n\n2. **统计方法**：\n   - Bootstrap resampling (B=10,000) 的合理性\n   - Cluster bootstrap (K=11) 的局限性是否充分讨论\n   - Wild cluster bootstrap 的使用是否正确\n   - Cohen's d = 3.02 在 K=11 下的可解释性\n   - 多重比较校正（Bonferroni）的使用\n\n3. **实验设计与控制**：\n   - 11/30 task types 的选择标准是否合理？排除 63% 的 task types 是否会导致 selection bias？\n   - N=245 episodes 的 power analysis\n   - 纯策略比较的生态效度（real-world applicability）\n   - Cross-model validation (3 models) 的充分性：都在 7-9B 范围，72B 仅作为 agent improvement\n   - Cross-environment probes (MATH, ALFWorld) 的深度是否足够支撑 generalizability claims\n   - Router training negative result 的可信度：是真的学不到，还是实验设置限制了\n\n4. **内部一致性**：\n   - 正文 claims 与数据/表格/图表是否一致\n   - Limitations 是否充分覆盖方法论弱点\n   - 各 Appendix 与正文的交叉引用是否准确\n\n请按 ARR 审稿标准给出详细评审意见，包含 Strengths、Weaknesses、Questions、Minor Issues。"
  }
}
```

</details>

---


### Tool result

_source line 2155 · 2026-05-21T22:06:24.551761+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14505
}
```

</details>

---


### Tool call

_source line 2156 · 2026-05-21T22:06:24.652747+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 相关工作**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Interpretability and Analysis\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求\n- Long paper 正文 ≤ 8 页，参考文献不限页数\n- Limitations 章节必须有，不计入页数\n- Ethics Statement 不计入页数\n- ACL 模板 (`\\usepackage[review]{acl}`)，double-blind\n- Appendices 在参考文献之后，不计入页数\n- Responsible NLP Checklist 在 OpenReview submission form 中填写（不在 PDF 中）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性与贡献定位**：\n   - \"Episode-level counterfactual diagnostic framework\" 是否构成足够的方法论贡献？\n   - \"Death avoidance dominates routing signal\" 这个 finding 是否 surprising 还是 trivially obvious？\n   - 与 Interpretability and Analysis track 的匹配度\n   - DAF metric 是否有独立的学术价值，还是仅服务于本论文的特定 setting？\n\n2. **Claim 与证据匹配**：\n   - 论文的 generality claims（\"framework applies to any environment\"）vs 实际验证范围（1 primary + 2 probes）\n   - \"~50-episode pilot suffices\" 这个 practical claim 的证据基础\n   - \"Contradicting the routing literature's implicit assumption of diverse signal sources\" 这个 framing 是否公允\n   - 三个 contribution 各自的证据强度\n\n3. **相关工作覆盖**：\n   - 是否遗漏重要的 tool-use routing / adaptive computation 文献（尤其 2025-2026 concurrent work）\n   - Safe RL 文献的引用是否足够深入\n   - 与 agent evaluation benchmarks（AgentBench 等）的关系是否讨论\n   - Counterfactual evaluation in RL 部分是否遗漏关键工作\n\n4. **论文完整性**：\n   - 叙事结构（Introduction → Method → Experiments → Discussion → Conclusion）是否流畅\n   - Abstract 与 Conclusion 是否准确反映了论文的实际贡献和局限\n   - 是否有重要实验或分析缺失（应做但未做的）\n   - Limitations 的覆盖面是否充分\n\n5. **写作质量**：\n   - 术语一致性和定义清晰度\n   - 图表质量和信息密度\n   - 是否存在 overclaiming 或 hedging 不当\n\n请按 ARR 审稿标准给出详细评审意见，包含 Strengths、Weaknesses、Questions、Minor Issues。"
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
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 相关工作**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Interpretability and Analysis\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求\n- Long paper 正文 ≤ 8 页，参考文献不限页数\n- Limitations 章节必须有，不计入页数\n- Ethics Statement 不计入页数\n- ACL 模板 (`\\usepackage[review]{acl}`)，double-blind\n- Appendices 在参考文献之后，不计入页数\n- Responsible NLP Checklist 在 OpenReview submission form 中填写（不在 PDF 中）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性与贡献定位**：\n   - \"Episode-level counterfactual diagnostic framework\" 是否构成足够的方法论贡献？\n   - \"Death avoidance dominates routing signal\" 这个 finding 是否 surprising 还是 trivially obvious？\n   - 与 Interpretability and Analysis track 的匹配度\n   - DAF metric 是否有独立的学术价值，还是仅服务于本论文的特定 setting？\n\n2. **Claim 与证据匹配**：\n   - 论文的 generality claims（\"framework applies to any environment\"）vs 实际验证范围（1 primary + 2 probes）\n   - \"~50-episode pilot suffices\" 这个 practical claim 的证据基础\n   - \"Contradicting the routing literature's implicit assumption of diverse signal sources\" 这个 framing 是否公允\n   - 三个 contribution 各自的证据强度\n\n3. **相关工作覆盖**：\n   - 是否遗漏重要的 tool-use routing / adaptive computation 文献（尤其 2025-2026 concurrent work）\n   - Safe RL 文献的引用是否足够深入\n   - 与 agent evaluation benchmarks（AgentBench 等）的关系是否讨论\n   - Counterfactual evaluation in RL 部分是否遗漏关键工作\n\n4. **论文完整性**：\n   - 叙事结构（Introduction → Method → Experiments → Discussion → Conclusion）是否流畅\n   - Abstract 与 Conclusion 是否准确反映了论文的实际贡献和局限\n   - 是否有重要实验或分析缺失（应做但未做的）\n   - Limitations 的覆盖面是否充分\n\n5. **写作质量**：\n   - 术语一致性和定义清晰度\n   - 图表质量和信息密度\n   - 是否存在 overclaiming 或 hedging 不当\n\n请按 ARR 审稿标准给出详细评审意见，包含 Strengths、Weaknesses、Questions、Minor Issues。"
  }
}
```

</details>

---


### Tool result

_source line 2157 · 2026-05-21T22:06:25.962260+00:00_

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

_source line 2158 · 2026-05-21T22:06:41.530437+00:00_

已完成所有并行派发：

- **视觉审查 Agent**：已启动（fire-and-forget）
- **外部审稿**：项目未配置 paperreview.ai，跳过
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配 Round 1 任务
- **Reviewer 2**（新颖性 + 完整性 + 相关工作）：已分配 Round 1 任务

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 173

## Round 173

2 recorded events


### User

_source line 2159 · 2026-05-21T22:13:03.720713+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：Death Avoidance as the Dominant Routing Signal

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 方法论框架设计合理、实验充分，但核心 finding 高度依赖 ScienceWorld 的环境特性（高死亡率 + 终端惩罚），泛化性不足，且标题/摘要的 framing 超出了实际证据范围。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 框架方法论在 ScienceWorld 范围内 sound，但 generality claims 远超实际验证范围；因果推断缺乏形式化基础 |
| Excitement | 2.5/5 | "死亡逃避主导路由信号"在 ScienceWorld 中近乎显然（内部策略幻觉→死亡，确定性策略用 ground-truth→存活），跨环境 probes 反而证明这不是一般性发现 |
| Reproducibility | 4/5 | 算法伪代码清晰，实验细节充分（Appendix I, T），承诺发布代码和数据 |
| Overall Assessment | 3.0/5 | Findings 水平——实证工作扎实但新颖性有限，主要贡献是环境特定的经验观察而非可迁移的方法论洞察 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心 finding 的环境特异性与 framing overclaiming 之间的根本矛盾

- 具体位置：Title, Abstract (p1), §1 Introduction (p1-2), §6 Conclusion (p8-9)
- 问题：标题 "Death Avoidance as **the** Dominant Routing Signal" 暗示这是关于 LLM agent routing 的一般性发现。但论文自己的跨环境 probes 直接推翻了这一点：MATH 的 DAF=0%（§3.4, p6: "no routing signal without catastrophic failure"），ALFWorld 的 DAF=0%（§3.4, p6: "the entire performance gap Δ_tot reflects information asymmetry from admissible-action access"）。核心 finding 仅在 ScienceWorld 成立，而 ScienceWorld 的环境设计（death penalty P=-100，catastrophic failure 是终端事件）使得这个发现近乎循环论证——当一个策略因幻觉而频繁触发 catastrophic failure，而另一个策略用 ground-truth simulation 规避死亡时，"死亡逃避"自然成为主导信号，这更像是环境特性的直接推论，而非关于 routing 的深层洞察。
- 为什么影响接收：如果主要贡献是一个仅在特定环境下成立的经验观察，且该观察在该环境下接近 trivially obvious，那么对 routing 社区的影响力和可操作性都很有限。标题和摘要需要大幅下调 generality claims。
- 建议修改方向：(1) 标题改为明确限定 ScienceWorld 的范围，如 "Death Avoidance as the Dominant Routing Signal in ScienceWorld"；(2) Abstract 和 Introduction 中明确承认 cross-environment probes 否定了泛化性；(3) 将论文重新定位为"一个诊断框架 + 一个环境特定的 case study"而非"一个关于 routing 的一般性发现"。

**N2** [critical] 反事实框架的方法论新颖性不足

- 具体位置：§2 Method (p2-3), Algorithm 1 (p12)
- 问题：所提出的 "episode-level counterfactual diagnostic framework" 本质上是：(a) 在两种纯策略下分别运行 episodes，(b) 比较 episode-level outcomes，(c) 根据死亡/非死亡分类标签。Algorithm 1 是一个直接的 if-else 分类树，没有技术深度。DAF metric 是一个基本的加权分数分解（Equation 4, p3: DAF = fraction of score gap attributable to death），数学上平凡。对于 Interpretability and Analysis track，reviewer 期望看到更形式化的分析工具，或者至少与因果推断文献（Pearl 2009, Rubin 1974 的 potential outcomes framework）的联系——论文本质上在估计 treatment effects（internal vs. deterministic），但完全没有使用这个成熟的理论框架。
- 为什么影响接收：如果框架本身不构成独立贡献（即剥离 ScienceWorld 的特定 finding 后，框架没有独立的学术价值），那么论文的贡献仅剩环境特定的经验观察。
- 建议修改方向：(1) 将框架形式化地连接到因果推断文献，建立理论基础；(2) 论证框架在其他环境中的诊断价值（目前 MATH 和 ALFWorld 的 probes 实际上削弱了框架的价值，因为框架在这些环境中没有产出 actionable insights）；(3) 或者诚实地将贡献重新定位为"一套实验方法论 + 一个 ScienceWorld 的 case study"。

**N3** [critical] "Contradicting the routing literature's implicit assumption" 的 framing 不公允

- 具体位置：§1 Introduction (p1, "The shared assumption—that routing signal stems from diverse sources and a learned router can exploit it—remains untested"), §5 Discussion (p8)
- 问题：论文声称挑战了 routing 文献的"隐含假设"，即 routing 信号来自多样化来源。但所引用的 routing 工作（CogRouter, ARES, MTRouter, Budget-Aware Routing 等）操作在完全不同的 settings：LLM 质量路由（RouteLLM 在模型间路由）、计算深度适配（CogRouter 调整 reasoning depth）、成本感知路由（Budget-Aware 在预算约束下路由）。这些工作不在有"死亡"机制的交互式环境中运行。说它们"假设多样化信号来源"是一种 strawman——它们在各自的 setting 中确实有多样化信号。ScienceWorld 是一个有极端 catastrophic failure 的特殊环境，在这里发现死亡逃避主导并不 "contradict" 其他 settings 的任何假设。
- 为什么影响接收：这种 framing 夸大了论文的影响力，如果 reviewer/AC 发现这是 strawman，会显著降低可信度。
- 建议修改方向：将 positioning 从 "contradicting existing assumptions" 改为 "revealing that in environments with catastrophic failure, routing signal is unexpectedly concentrated in death avoidance, suggesting environment-specific diagnostics before assuming diverse signals"。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Router training 负面结果的解释不完整

- 具体位置：§3.6 (p7), Appendix I (p15)
- 问题：Router 训练仅达到 ~56% balanced accuracy（near chance），论文将此解释为"signal is task-type-level, not step-level"。但这存在多种替代解释：(a) 反事实标签本身噪声大（论文在 §3.1 和 Appendix B 承认 label 质量问题，oracle 仅 97.4% step-level accuracy）；(b) 4B LoRA router 的模型容量不足；(c) 训练数据量不够（2,040 training steps）；(d) step-level 和 episode-level 的粒度不匹配。论文没有排除这些替代假设。
- 建议：至少报告 router 在 training set 上的 accuracy（判断是否 underfitting）；尝试用 task-type 特征（而非 step-level observation）训练一个简单 classifier 作为 upper bound。

**W2** [warning] 模型规模覆盖不足

- 具体位置：§3.2 (p5), §3.4 (p6), Appendix I (p15)
- 问题：所有实验仅使用 7-9B 模型（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B）。这些模型的幻觉率相对较高，因此内部策略的死亡率较高是预期中的。关键问题是：对于幻觉率更低的 frontier models（如 70B+ 或 GPT-4/Claude 级别），死亡逃避是否仍然主导？如果 frontier models 的内部策略死亡率显著降低，那么 routing 信号的组成可能完全不同，进一步限制论文 finding 的适用范围。
- 建议：至少在 Discussion 或 Limitations 中明确讨论这一点；如果可行，在一个模型规模上做 pilot experiment。

**W3** [warning] DAF metric 的独立学术价值未充分论证

- 具体位置：§2.3 (p3), §5 Discussion (p8)
- 问题：论文将 DAF 作为三个 contribution 之一（p2: "(ii) the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components"）。但 DAF 本质上是 Δ_death / Δ_tot，一个简单的比例。在 ScienceWorld 之外（MATH 无死亡，ALFWorld 无死亡），DAF 恒为 0，metric 无用。这使得 DAF 更像是一个论文内部的 notation convenience 而非可复用的学术工具。
- 建议：要么在 introduction 中降低 DAF 作为独立 contribution 的地位，要么论证 DAF 在更广泛的"catastrophic failure"场景中的应用价值（如 safety-critical RL、robotic control）。

**W4** [warning] ~50-episode pilot 的 practical claim 证据薄弱

- 具体位置：§6 Conclusion (p8: "a ~50-episode pilot suffices for build-vs-buy decisions"), §3.1 (p4)
- 问题：论文声称 ~50 episodes 足以做 routing 诊断，但没有提供 power analysis 或 sample-size calculation。§3.1 的 stabilization 分析（p4: "the stabilization analysis"）基于 bootstrap resampling 的 CI 收窄，但 CI width 在 N=50 时仍然相当宽。对于一个 practical recommendation，需要更严格的统计基础（如 detectable effect size, power ≥ 0.8 的最小样本量）。
- 建议：加入 formal power analysis，或至少将 "suffices" 改为 "provides preliminary evidence" 并在 Limitations 中讨论。

**W5** [warning] 相关工作的几个遗漏

- 具体位置：§4 Related Work (p7-8)
- 问题：
  (a) **因果推断基础文献**：论文的框架本质上是 potential outcomes（Rubin 1974）/do-calculus（Pearl 2009）的应用场景，但完全没有引用或连接。Pona et al. (2025) 已被引用但没有讨论其 structural causal model 框架与本文方法的关系。
  (b) **Credit assignment for LLM agents**：近期出现大量工作（如 "From Reasoning to Agentic: Credit Assignment in RL for LLMs", arXiv 2604.09459），本文的 episode-level 分解本质上是 credit assignment 问题，但未讨论。
  (c) **Agent safety 中的 catastrophic action avoidance**："Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety" (arXiv 2510.16492) 直接研究了 LLM agent 的 catastrophic failure avoidance，与本文 finding 高度相关但未引用。
  (d) **"Nuclear Deployed" (ACL 2025 Findings)**：分析 LLM agent 自主决策中的 catastrophic risks，直接相关。
  (e) **Adaptive routing for computer-use agents** (arXiv 2603.12823)：2026 年的 vision-language model routing 工作，在 agent 环境中做 adaptive routing，与本文 setting 更接近。
- 建议：在 Related Work 中至少补充 (a) 和 (c)，讨论本文框架与因果推断的关系以及与 agent safety 的 catastrophic failure avoidance 文献的联系。

## 小问题（不影响接收）

- **引用验证**：verify_references 检查发现 5 条 not_found（react-2023, mixture-of-recursions-2025, gajcin2023counterfactual, natarajan2013learning, axis-2026）和 6 条 mismatch（garcia2015comprehensive 作者名、qwen25-2024 作者名、llama3-2024 作者名、toolace-2025 作者名、webb-2023 年份 bib=2023 vs api=2014、altman1999constrained 年份）。其中 webb-2023 的年份差异（bib 标注 2023 但 OpenAlex 记录为 2014）需要核实。
- **Figure 1 (p3)**: 图例中 "Counterfactual episode collection and analysis pipeline" 信息密度偏低，右侧的 label 分类树与 Algorithm 1 重复，建议合并或增加可视化价值。
- **Table 1 (p6)**: Death率和 N 的 column header 可以更明确（当前的 "Death %" 和 "T" 不够自解释）。
- **§2.2 (p2-3)**: "per-step oracle" 的概念引入较突兀，reader 需要在 Figure 1 和正文之间反复跳转才能理解 labeling 流程。

## 主要优势

1. **实验设计的系统性**：跨三个模型家族（Qwen, Llama, Gemma）的一致性验证、跨三个环境的 probes、多项 ablation（text augmentation, grounding, capacity scaling）都做得很扎实。特别是 Appendix 的 14 个子节（A-T）提供了丰富的支撑材料。

2. **写作清晰、结构紧凑**：8 页正文 + 丰富附录的安排合理。核心 claim 表述清楚，实验 narrative 流畅。Abstract 的数字密度适当（具体的 78.9%, DAF=88-90% 等）。

3. **诚实的负面结果呈现**：Router training 的低 accuracy（§3.6）、cross-environment probes 否定了泛化性（§3.4）、text augmentation 无提升（Appendix J, Table 11）等负面结果都被如实报告，这体现了学术诚信。

4. **统计方法论严谨**：Episode-level bootstrap resampling（B=10,000）、cluster bootstrap 处理 task-type 聚类效应（Appendix E）、wild cluster bootstrap 处理小集群（Cameron et al., 2008; Webb, 2023）——统计推断的处理在 NLP 论文中属于上佳水平。

5. **Limitations 章节的覆盖面**：环境范围、统计限制、方法论约束（pure-strategy upper bound vs. mixed routing 的实际下界）都有讨论，虽然可以更深入但基本合格。

## 总结

这是一篇实证工作扎实、统计处理严谨的论文，但核心问题在于：(1) 主要 finding 高度依赖 ScienceWorld 的环境特性且接近 trivially obvious，(2) framing 的 generality claims 远超实际证据支撑，(3) 方法论框架（Algorithm 1 + DAF）概念上简单，缺乏独立的学术贡献。如果作者能诚实地将论文重新定位为"环境诊断 case study"并下调 generality claims，这是一篇合格的 Findings 论文；但目前的 framing 使得论文在 Conference 接收线以下。

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

_source line 2160 · 2026-05-21T22:13:11.110240+00:00_

Reviewer 2 的审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 174

## Round 174

4 recorded events


### User

_source line 2161 · 2026-05-21T22:13:23.602948+00:00_

[Reviewer 2 审稿结果]:
审稿完成。总结：

- **Overall: 3.0 (Findings)**
- 3 个 Must-Fix：核心 finding 的环境特异性与 overclaiming 矛盾、框架方法论新颖性不足、"contradicting routing literature" 的 strawman framing
- 5 个 Should-Fix：router 负面结果解释不完整、模型规模不足、DAF 独立价值未论证、50-episode claim 证据薄弱、相关工作遗漏（因果推断基础、agent safety catastrophic failure avoidance 等）
- 主要优势：实验系统性强、统计方法严谨、负面结果如实报告、写作清晰

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

_source line 2162 · 2026-05-21T22:13:39.618803+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 返回初审意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 返回初审意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2163 · 2026-05-21T22:13:39.619378+00:00_

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

_source line 2164 · 2026-05-21T22:13:43.072667+00:00_

Reviewer 2 给出 3.0 (Findings)，核心批评集中在 overclaiming 和环境特异性。Reviewer 1 尚未返回，收到后立即启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 175

## Round 175

8 recorded events


### User

_source line 2165 · 2026-05-21T22:15:58.034637+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 方法严谨性 + 实验设计

---

## 总体评分
**Overall Assessment**: 3.5 — Borderline Conference
**Reviewer Confidence**: 4/5

**一句话总结**: 框架设计扎实、统计分析详尽，但核心发现（DAF≈90%）高度依赖 ScienceWorld 的极端惩罚结构（P=0 时 DAF 降至 7.4%），且跨模型验证仅覆盖 7-9B 同级模型，削弱了论文对 "death avoidance 是 dominant routing signal" 这一核心主张的支撑力度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 框架数学自洽，主体分析在 ScienceWorld 内部严谨；但 DAF 对 penalty 的敏感性（Table 12）未在正文充分讨论，"dominant" 的 framing 超出证据支撑范围 |
| Excitement | 3/5 | 诊断性发现对 agent routing 社区有价值，但范围窄（一个环境 + 特定 penalty）、实践指导有限（结论本质上是 "ScienceWorld 里直接用 deterministic 即可"） |
| Reproducibility | 4/5 | 算法伪代码、prompt 模板、bootstrap 参数、训练配置均有详细说明；承诺公开代码 |
| Limitations & Societal Impact | 4/5 | Limitations 覆盖了环境范围、统计局限、方法论约束；但 penalty sensitivity 的影响讨论不足 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DAF 的 "dominance" 本质上由 penalty 幅度驱动，而非 routing 信号的内在属性

- 具体位置：Section 2.3 (DAF 定义)、Appendix K (Table 12)、Section 6 (Conclusion)
- 问题：Table 12 清楚地显示 DAF 与 penalty P 的关系：P=0 时 DAF=7.4%，P=10 时 DAF=39.8%，P=100 时 DAF=90.1%。这意味着 death avoidance "占 90% score gap" 主要是因为 ScienceWorld 对死亡施加了极端的 -100 惩罚（在 0-100 分数范围内），通过 score amplification 人为放大了 death-asymmetric episodes 的权重。在 P=0 时（不施加额外死亡惩罚），死亡不对称仅贡献 7.4% 的 gap——agent 提前死亡只是少走了几步、少完成了几个子任务。这说明 death avoidance 的 "dominance" 是 reward design 的产物，而非 routing 问题的固有特征。
- 为什么影响接收：论文标题和核心主张（"Death Avoidance as the **Dominant** Routing Signal"）暗示这是一个关于 routing 信号结构的一般性洞察。但 Table 12 的数据表明，在不同的 penalty 设计下（如连续分数环境、软惩罚环境），这一发现可能完全不成立。这不是 Limitations 一笔带过就够的——它动摇了 contribution 的核心叙事。
- 建议修改方向：(a) 在正文 Section 3.1 或 Section 5 中增加一个段落，正面讨论 Table 12 的含义，明确 DAF 是 penalty-sensitive metric；(b) 调整 framing，将 "dominant signal" 限定为 "在 ScienceWorld 的当前惩罚结构下"；(c) 补充讨论：78.9% 的 label fraction（不受 penalty 加权影响的指标）在不同 P 下是否稳定——如果稳定，这可以作为 penalty-invariant 的补充证据。

**N2** [critical] 跨模型验证仅覆盖 7-9B 参数范围，不足以支撑 "跨模型家族" 的声明

- 具体位置：Section 3.2、Table 16 (Appendix M)
- 问题：三个验证模型（Qwen2.5-7B、Llama-3.1-8B、Gemma-2-9B）参数量和能力高度相似（均为 7-9B 级别的 instruction-tuned 模型，内部死亡率均 ~42%）。论文声称 "death dominance replicates across model families"，但实际上复制的是 across models of the same capability tier。Appendix P 的 72B 容量分析显示死亡率从 ~43% 降至 ~31%（±28%），表明更大模型确实减少了致命错误的频率。然而论文未对 72B 模型计算 DAF——如果 72B 的 DAF 显著低于 90%（由于更低的死亡率），这将直接削弱 "跨模型复制" 的结论。
- 为什么影响接收：Agent routing 的实际用例通常涉及不同规模的模型（如将简单任务路由给小模型、复杂任务路由给大模型）。如果 death dominance 是 small-model-specific 的现象，论文的实践意义将大打折扣。
- 建议修改方向：(a) 对 72B 模型（Appendix P 已有数据）补算 DAF 和 label fraction，报告是否复制；(b) 如果无法补实验，在 Section 3.2 中明确将 "cross-model" 限定为 "cross-model-family within the 7-9B tier"；(c) 在 Limitations 中增加一段讨论 model scale 对 death dominance 的潜在影响。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cluster bootstrap K=11 的统计推断可靠性

- 具体位置：Section 3.1、Appendix E (Table 6)
- 问题：论文使用 K=11 个 task type 作为 cluster 进行 cluster bootstrap。Cameron et al. (2008) 和 Webb (2023) 的文献建议 K ≥ 20-30 才能保证可靠的 cluster-robust 推断。论文在 Appendix E 承认 "narrower CIs obtained reflect known small-sample bias toward underestimation of variance, not tighter inference"，但这个 caveat 在正文中不够醒目。Cohen's d = 3.02 在 K=11 下虽然效应量巨大，但其置信区间和可解释性受到小 K 的严重限制。正文 Section 3.1 报告 "Cluster bootstrap (K=11): cluster-robust CI [81.1%, 99.0%]" 而未充分 caveat 这是 potentially anti-conservative 的估计。
- 建议：在正文报告 cluster bootstrap 结果时，紧跟一句说明 K=11 远低于可靠推断所需的最低 cluster 数（K≥20-30），读者应主要依赖非聚类 bootstrap 的 CI。

**W2** [warning] 11/30 task types 的选择排除了 63% 的任务空间

- 具体位置：Section 3 第一段、Appendix C (Table 3-4)
- 问题：排除标准包括三类：(1) 5 个用于 pipeline 开发的 hold-out 任务（标准做法）；(2) 7 个与已纳入任务的 family representative 冗余的任务（合理）；(3) 7 个双策略均近零进展的任务。第三类排除有 selection bias 风险——这些任务可能代表了一类不同的 routing 动态（如两种策略都失败，但失败模式不同）。Table 4 显示被排除任务的 ΔDR 反而更高（+39.2pp），Appendix S 提供了 5 个代表性排除任务的扩展验证，这些 evidence 部分缓解了 bias 担忧，但未对全部 19 个排除任务做完整的 counterfactual analysis。
- 建议：(a) 对全部 30 个 task types 运行完整 counterfactual analysis 并在 appendix 报告（如果实验成本允许）；(b) 至少在正文说明为什么不对全部任务运行 full analysis（是计算成本还是其他原因）。

**W3** [warning] Router 训练 negative result 的实验覆盖不足

- 具体位置：Section 3.6、Appendix I
- 问题：论文在 Section 3.6 探讨 step-level router 能否学习 routing 信号，结论是 "step-level balanced accuracy (56-59%) 表明信号难以从 step level 学习"。实验覆盖了 3 个 Qwen3 规模（0.6B、1.7B、4B）+ LoRA fine-tuning。但这仍然是 single architecture family + single training paradigm。结论提供了两种解读（A: 88% 噪声标签；B: 信号是 task-type 级别的），但未充分排除第三种可能：更好的训练方法（如 contrastive learning、different loss functions、更多数据增强）可能成功。Training data 仅 2,040 步，episode 级评估数据量很小。
- 建议：(a) 在 Section 3.6 中明确标注这是 preliminary negative result，而非 definitive evidence of non-learnability；(b) 增加一段讨论替代训练方法的可能性。

**W4** [warning] 跨环境 probes 深度不足以支撑 generalizability 暗示

- 具体位置：Section 3.4、Appendix L (Tables 14-15)
- 问题：MATH 和 ALFWorld 被标注为 "boundary probes (not cross-domain validation)"，这一定位是诚实的。但论文在 Abstract 和 Introduction 中的措辞（"Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms"）暗示了比实际证据更强的 generalizability。MATH 的分析仅为 aggregate-level（N=795），无 per-task-type 分解。ALFWorld 的分析（N=135）发现 information asymmetry 而非 death avoidance 驱动 routing——这实际上 *削弱* 了 death avoidance 作为 "dominant signal" 的一般性主张，而论文将其 frame 为 "框架的诊断能力"。
- 建议：调整 Abstract/Introduction 中的措辞，避免暗示 generalizability；或者加深 MATH/ALFWorld 的分析深度（如 MATH 的 per-category 分解、ALFWorld 的 per-task-type DAF）。

**W5** [warning] 分解公式 Δ_full ≈ δP + Δ_nd 的近似误差未量化

- 具体位置：Section 2.3 (page 3)
- 问题：从完整分解到近似形式 Δ_full ≈ δP + Δ_nd 需要假设 (1) death-death episodes 的 score gap ≈ 0（双方都死亡时 score 差异可忽略）和 (2) 交互项 δP · (ā_dd − ā_nd) 可忽略。论文未报告这些假设在实际数据中的成立程度——交互项的实际量级是多少？完整分解 vs 近似分解的残差是多少？
- 建议：在 Section 2.3 或 Appendix 中报告完整分解的各项数值和近似残差。

---

## 小问题（不影响接收）

1. **页数边界**：Conclusion（Section 6）在 page 8 底部开始，最后约 2 行文字（"vironments. Future work should validate..."）溢出到 page 9。Limitations 紧随其后。从严格解读看，main text（Section 1-6）超过 8 页。建议压缩 Conclusion 或前面的内容以严格控制在 8 页内。

2. **Section 3.1 数字表述可能产生歧义**：正文提到 "150 (61.2%) are episodes indicating..." 后紧跟 "routing is relevant in only 38.8% of episodes"。这两个数字是互补的（150 no-preference + 95 有偏好 = 245），但行文结构可能让读者误以为 150 是有偏好的 episode 数。建议改写为更清晰的表述，如 "150 (61.2%) episodes show no preference between strategies; routing is relevant in the remaining 95 (38.8%)"。

3. **引用验证结果**：verify_references 工具检测到 5 条 not_found（react-2023, mixture-of-recursions-2025, gajcin2023counterfactual, natarajan2013learning, axis-2026）和 6 条 mismatch（garcia2015comprehensive, qwen25-2024, llama3-2024, toolace-2025, webb-2023, altman1999constrained）。大部分 not_found 和 mismatch 是 OpenAlex 索引问题或 LaTeX 编码差异（如重音符号），非虚假引用。但 `webb-2023` 的年份不匹配值得核查：bib 记录 2023，OpenAlex 返回 2014——Webb (2023) 可能是 Canadian Journal of Economics 的正式发表版本，2014 是 working paper 版本，建议统一为正式发表年份。

4. **Figure 2 轴标签**：scatter plot 的 x 轴标签 "Death rate differential (int. − det., pp)" 和 y 轴 "Performance gap" 的单位不够明确——y 轴是 absolute score difference 还是 percentage points？

5. **Algorithm 1 (page 12)**：算法对 death-asymmetric episodes 直接赋予 preference label 而不比较 score（line 5-6），这在 P=100 时是正确的（dying strategy score ≤ 0 < surviving strategy score ≥ 0），但算法本身未说明这一隐含假设。如果 P < max_possible_partial_score，此假设可能不成立。

---

## 主要优势

1. **框架设计**：Episode-level counterfactual labeling + DAF decomposition + SCI 三个指标形成了一个完整的诊断工具链。Algorithm 1 的 edge case 处理（both-dead、both-alive-tied、score-comparison）是 thorough 的。

2. **统计严谨性**：Multiple robustness checks（non-clustered bootstrap B=10000、cluster bootstrap、wild cluster bootstrap、leave-one-out DAF sensitivity、penalty sensitivity、Bonferroni correction）。Leave-one-task-out 分析（Appendix G, Table 7）确认无单一 task type 驱动结论（LOO DAF ≥ 78.9%，r ∈ [0.963, 0.990]）。

3. **诚实的 framing**：论文明确标注 MATH/ALFWorld 为 "boundary probes (not cross-domain validation)"，Limitations 覆盖了环境范围、统计局限、方法论约束。Router training 的 negative result 提供了两种解读而非单一结论。

4. **实践价值**：Section 5 和 Appendix Q-R 的 decision framework 为实际部署提供了 actionable guidelines（先用 ~50 episode pilot 诊断 death dominance，再决定是否需要 router）。

5. **Appendix 质量**：12 个 appendix（A-T）提供了大量支撑细节，包括 prompt templates（Appendix T）、per-task 分解（Appendix C）、dose-response 分析（Appendix H）、failure mode 分析（Appendix N-O）、grounding ablation（Appendix O）等。写作密度高且信息量大。

6. **Label quality audit**（Appendix B）：主动检查了 label 质量，报告了 tie-breaking 情况和 both-dead 分布，增加了数据透明度。

---

## 总结

论文在 ScienceWorld 环境内的分析是扎实和详尽的。主要问题在于 (1) DAF 对 penalty magnitude 的强依赖性未在正文充分讨论，使 "dominant signal" 的 framing 过度泛化；(2) 跨模型验证局限于同级模型。如果作者能在正文正面讨论 penalty sensitivity（N1）并补充/限定跨模型验证的声明（N2），论文的 contribution 将更加 solid——一个 well-calibrated diagnostic framework + 一个 environment-specific but clearly-scoped finding，足以达到 Conference 水准。当前 framing 下，介于 Borderline Conference 和 Findings 之间。

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

_source line 2166 · 2026-05-21T22:16:28.364392+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2167 · 2026-05-21T22:16:28.364787+00:00_

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

_source line 2168 · 2026-05-21T22:16:53.982781+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 核心 finding 的环境特异性与 framing overclaiming 之间的根本矛盾\n- 标题 \"Death Avoidance as **the** Dominant Routing Signal\" 暗示一般性发现，但跨环境 probes（MATH DAF=0%, ALFWorld DAF=0%）直接推翻了这一点。核心 finding 仅在 ScienceWorld 成立，而 ScienceWorld 的环境设计使得这个发现近乎循环论证。\n- 建议：标题改为限定 ScienceWorld 范围；将论文重新定位为\"诊断框架 + 环境特定 case study\"。\n\n**N2** [critical] 反事实框架的方法论新颖性不足\n- 框架本质上是：(a) 两种纯策略下分别运行 episodes，(b) 比较 episode-level outcomes，(c) 根据死亡/非死亡分类。Algorithm 1 是直接的 if-else 分类树，没有技术深度。DAF 数学上平凡。未连接因果推断文献（Pearl 2009, Rubin 1974）。\n- 建议：将框架形式化连接因果推断文献；或诚实重新定位为\"实验方法论 + case study\"。\n\n**N3** [critical] \"Contradicting the routing literature's implicit assumption\" 的 framing 不公允\n- 所引用的 routing 工作（CogRouter, ARES, MTRouter 等）操作在完全不同的 settings。说它们\"假设多样化信号来源\"是 strawman。ScienceWorld 的极端 catastrophic failure 使得这里发现死亡逃避主导并不 contradict 其他 settings。\n- 建议：将 positioning 从 \"contradicting\" 改为 \"revealing environment-specific concentration\"。\n\n### Should-Fix 问题\n\n**W1** Router training 负面结果的解释不完整——未排除替代假设（模型容量不足、数据量不够、粒度不匹配）。\n\n**W2** 模型规模覆盖不足——仅 7-9B 模型，frontier models 可能完全不同。\n\n**W3** DAF metric 的独立学术价值未充分论证——在 ScienceWorld 之外 DAF 恒为 0。\n\n**W4** ~50-episode pilot 的 practical claim 证据薄弱——缺乏 power analysis。\n\n**W5** 相关工作遗漏——因果推断基础文献（Pearl/Rubin）、agent safety catastrophic failure avoidance（\"Check Yourself Before You Wreck Yourself\"）、credit assignment for LLM agents 等。\n\n### 主要优势\n1. 实验设计系统性（三模型、三环境、多 ablation）\n2. 写作清晰、结构紧凑\n3. 诚实呈现负面结果\n4. 统计方法论严谨\n5. Limitations 覆盖面合格\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条回应 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 核心 finding 的环境特异性与 framing overclaiming 之间的根本矛盾\n- 标题 \"Death Avoidance as **the** Dominant Routing Signal\" 暗示一般性发现，但跨环境 probes（MATH DAF=0%, ALFWorld DAF=0%）直接推翻了这一点。核心 finding 仅在 ScienceWorld 成立，而 ScienceWorld 的环境设计使得这个发现近乎循环论证。\n- 建议：标题改为限定 ScienceWorld 范围；将论文重新定位为\"诊断框架 + 环境特定 case study\"。\n\n**N2** [critical] 反事实框架的方法论新颖性不足\n- 框架本质上是：(a) 两种纯策略下分别运行 episodes，(b) 比较 episode-level outcomes，(c) 根据死亡/非死亡分类。Algorithm 1 是直接的 if-else 分类树，没有技术深度。DAF 数学上平凡。未连接因果推断文献（Pearl 2009, Rubin 1974）。\n- 建议：将框架形式化连接因果推断文献；或诚实重新定位为\"实验方法论 + case study\"。\n\n**N3** [critical] \"Contradicting the routing literature's implicit assumption\" 的 framing 不公允\n- 所引用的 routing 工作（CogRouter, ARES, MTRouter 等）操作在完全不同的 settings。说它们\"假设多样化信号来源\"是 strawman。ScienceWorld 的极端 catastrophic failure 使得这里发现死亡逃避主导并不 contradict 其他 settings。\n- 建议：将 positioning 从 \"contradicting\" 改为 \"revealing environment-specific concentration\"。\n\n### Should-Fix 问题\n\n**W1** Router training 负面结果的解释不完整——未排除替代假设（模型容量不足、数据量不够、粒度不匹配）。\n\n**W2** 模型规模覆盖不足——仅 7-9B 模型，frontier models 可能完全不同。\n\n**W3** DAF metric 的独立学术价值未充分论证——在 ScienceWorld 之外 DAF 恒为 0。\n\n**W4** ~50-episode pilot 的 practical claim 证据薄弱——缺乏 power analysis。\n\n**W5** 相关工作遗漏——因果推断基础文献（Pearl/Rubin）、agent safety catastrophic failure avoidance（\"Check Yourself Before You Wreck Yourself\"）、credit assignment for LLM agents 等。\n\n### 主要优势\n1. 实验设计系统性（三模型、三环境、多 ablation）\n2. 写作清晰、结构紧凑\n3. 诚实呈现负面结果\n4. 统计方法论严谨\n5. Limitations 覆盖面合格\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2169 · 2026-05-21T22:17:14.055336+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20072
}
```

</details>

---


### Tool call

_source line 2170 · 2026-05-21T22:17:14.306867+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 的 \"dominance\" 本质上由 penalty 幅度驱动，而非 routing 信号的内在属性\n- Table 12: P=0 时 DAF=7.4%，P=10 时 DAF=39.8%，P=100 时 DAF=90.1%。Death avoidance 的 \"dominance\" 是 reward design 的产物。\n- 建议：正文讨论 Table 12 含义；调整 framing 限定为 ScienceWorld 当前惩罚结构；补充讨论 78.9% label fraction 的 penalty 不变性。\n\n**N2** [critical] 跨模型验证仅覆盖 7-9B 参数范围\n- 三个模型（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B）参数量高度相似。72B 的 DAF 未计算。如果 death dominance 是 small-model-specific 现象，实践意义将大打折扣。\n- 建议：对 72B 模型补算 DAF；或将 \"cross-model\" 限定为 \"within 7-9B tier\"。\n\n### Should-Fix 问题\n\n**W1** Cluster bootstrap K=11 的统计推断可靠性——远低于 K≥20-30 的最低要求，正文 caveat 不够。\n\n**W2** 11/30 task types 排除了 63% 任务空间——第三类排除（双策略均近零进展）有 selection bias 风险。\n\n**W3** Router 训练 negative result 实验覆盖不足——single architecture family + single training paradigm，未排除更好的训练方法可能成功。\n\n**W4** 跨环境 probes 深度不足——MATH 仅 aggregate-level，ALFWorld 发现 information asymmetry 实际上削弱了 death avoidance 的一般性。\n\n**W5** 分解公式 Δ_full ≈ δP + Δ_nd 的近似误差未量化——交互项的实际量级和残差未报告。\n\n### 小问题\n1. 页数边界：Conclusion 可能溢出到 page 9，需压缩。\n2. Section 3.1 数字表述歧义（150 vs 95 episodes）。\n3. 引用验证：webb-2023 年份不匹配需核查。\n4. Figure 2 y 轴单位不明确。\n5. Algorithm 1 隐含假设未说明（P < max_possible_partial_score 时可能不成立）。\n\n### 主要优势\n1. 框架设计完整（labeling + DAF + SCI）\n2. 统计严谨（多层 bootstrap + LOO sensitivity + Bonferroni）\n3. 诚实的 framing（boundary probes、negative result 两种解读）\n4. 实践价值（~50 episode pilot + decision framework）\n5. Appendix 质量高（A-T 共 20 个子节）\n6. Label quality audit 增加数据透明度\n\n---\n\n请对以上每个 Must-Fix (N1-N2) 和 Should-Fix (W1-W5) 逐条回应 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 的 \"dominance\" 本质上由 penalty 幅度驱动，而非 routing 信号的内在属性\n- Table 12: P=0 时 DAF=7.4%，P=10 时 DAF=39.8%，P=100 时 DAF=90.1%。Death avoidance 的 \"dominance\" 是 reward design 的产物。\n- 建议：正文讨论 Table 12 含义；调整 framing 限定为 ScienceWorld 当前惩罚结构；补充讨论 78.9% label fraction 的 penalty 不变性。\n\n**N2** [critical] 跨模型验证仅覆盖 7-9B 参数范围\n- 三个模型（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B）参数量高度相似。72B 的 DAF 未计算。如果 death dominance 是 small-model-specific 现象，实践意义将大打折扣。\n- 建议：对 72B 模型补算 DAF；或将 \"cross-model\" 限定为 \"within 7-9B tier\"。\n\n### Should-Fix 问题\n\n**W1** Cluster bootstrap K=11 的统计推断可靠性——远低于 K≥20-30 的最低要求，正文 caveat 不够。\n\n**W2** 11/30 task types 排除了 63% 任务空间——第三类排除（双策略均近零进展）有 selection bias 风险。\n\n**W3** Router 训练 negative result 实验覆盖不足——single architecture family + single training paradigm，未排除更好的训练方法可能成功。\n\n**W4** 跨环境 probes 深度不足——MATH 仅 aggregate-level，ALFWorld 发现 information asymmetry 实际上削弱了 death avoidance 的一般性。\n\n**W5** 分解公式 Δ_full ≈ δP + Δ_nd 的近似误差未量化——交互项的实际量级和残差未报告。\n\n### 小问题\n1. 页数边界：Conclusion 可能溢出到 page 9，需压缩。\n2. Section 3.1 数字表述歧义（150 vs 95 episodes）。\n3. 引用验证：webb-2023 年份不匹配需核查。\n4. Figure 2 y 轴单位不明确。\n5. Algorithm 1 隐含假设未说明（P < max_possible_partial_score 时可能不成立）。\n\n### 主要优势\n1. 框架设计完整（labeling + DAF + SCI）\n2. 统计严谨（多层 bootstrap + LOO sensitivity + Bonferroni）\n3. 诚实的 framing（boundary probes、negative result 两种解读）\n4. 实践价值（~50 episode pilot + decision framework）\n5. Appendix 质量高（A-T 共 20 个子节）\n6. Label quality audit 增加数据透明度\n\n---\n\n请对以上每个 Must-Fix (N1-N2) 和 Should-Fix (W1-W5) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2171 · 2026-05-21T22:17:15.613537+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1306
}
```

</details>

---


### Assistant

_source line 2172 · 2026-05-21T22:17:26.588156+00:00_

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


## Round 176

## Round 176

2 recorded events


### User

_source line 2173 · 2026-05-21T22:17:29.130253+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论摘要**：

- **Overall: 3.5（Borderline Conference）**，Confidence 4/5
- **2 个 Must-Fix**：
  - **N1**: DAF≈90% 本质上由 ScienceWorld 的 -100 极端惩罚驱动（P=0 时 DAF 仅 7.4%，Table 12），但这一关键敏感性被放在附录，正文 framing "dominant signal" 过度泛化
  - **N2**: 跨模型验证仅覆盖 7-9B 同级模型，72B 模型数据已有但未计算 DAF，无法支撑 "跨模型家族复制" 的声明
- **5 个 Should-Fix**：cluster bootstrap K=11 可靠性、63% task types 排除、router 训练 negative result 覆盖不足、跨环境 probes 深度不够、分解公式近似误差未量化
- **主要优势**：框架设计完整（DAF + SCI + Algorithm 1）、统计 robustness checks 详尽（bootstrap/LOO/penalty sensitivity）、Limitations 诚实、Appendix 质量高

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

_source line 2174 · 2026-05-21T22:17:33.344632+00:00_

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


## Round 177

## Round 177

2 recorded events


### User

_source line 2175 · 2026-05-21T22:19:16.312307+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix 问题

[AGREE] R1-N1: DAF "dominance" 由 penalty 幅度驱动

R1 的观察非常精准。Table 12 (Appendix K, p17) 清楚展示了 DAF 与 P 的单调递增关系：P=0 时 DAF=7.4%，P=100 时 DAF=90.1%。论文虽在 p17 承认这是 "a mathematical consequence of the decomposition"，但这恰恰说明 DAF 作为 metric 缺乏 robustness——它度量的不是 routing 信号的内在结构，而是 reward engineering 的产物。

R1 提到的 78.9% label fraction 的 penalty 不变性是论文可以依赖的更强论据（label fraction 不随 P 变化，因为它只统计死亡是否发生，不涉及 score 加权）。但论文在正文中主要推 DAF 而非 label fraction，这是 framing 策略的失误。我在自己的 N1 中也从不同角度（环境特异性 + overclaiming）提出了类似关切——R1 的 penalty-sensitivity 分析进一步加强了这一点。

**补充**：如果作者将主要 claim 从 DAF dominance 转向 label fraction dominance（78.9% 的非 tie routing labels 来自 death asymmetry，不依赖 P），论文的核心 finding 会更 robust。但这需要调整 §2.3 的叙事权重和 §5 Discussion 的 framing。

---

[AGREE] R1-N2: 跨模型验证仅覆盖 7-9B

完全同意。我在自己的 W2 中提出了相同关切。三个模型（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B）参数量几乎相同（7-9B），幻觉率处于同一水平，因此死亡率相近是预期内的。

补充两个我的 review 中更具体的观察：

(1) 论文 §3.2 (p5) 提到用 Llama-3.1-8B-Instruct 做 cross-model replication，internal death rate 41.4% vs. deterministic 11.4%。Appendix M (Table 16, p16) 的 per-task 分析也显示三个模型的 death-rate differential 模式高度相似（"nearly identical internal vulnerability (~42%: Qwen 42.9%, Llama 41.4%)"）。这种一致性更可能反映 7-9B tier 的共有特征（如相似的幻觉模式），而非 death dominance 的跨规模 robustness。

(2) 论文 Appendix I (p15) 提到用 Qwen2.5-72B 做 exploratory router 训练，但仅报告了 step-level balanced accuracy（≈50%），没有计算 72B 在 ScienceWorld 上的 DAF。这是一个显著的遗漏——72B 的数据已经部分收集但未充分利用。

---

### Should-Fix 问题

[AGREE] R1-W1: Cluster bootstrap K=11 的统计可靠性

K=11 远低于 Cameron et al. (2008) 推荐的 K≥20-30。论文在 Appendix E (p13) 使用了 wild cluster bootstrap 作为补救，这是正确的方法学选择，但 K=11 仍然意味着 cluster-level inference 的 power 很低。论文正文 §3.1 (p4-5) 仅简短提及 "narrowing under cluster resampling"，caveat 确实不够显著。

**补充**：Appendix E 提到 "Episodes within the same task type are not fully independent because they share environment dynamics"，这实际上说明 K=11 的 effective sample size 可能比 245 episodes 暗示的要小得多。建议在正文添加一句明确的 caveat。

---

[AGREE] R1-W2: 19/30 task types 排除（63%）的 selection bias 风险

同意这是一个重要关切。论文 Appendix C (Table 4, p13) 和 Appendix S (Table 21, p22) 做了排除验证，显示排除的任务并非偏向 death-prone（"Notably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.960, Table 3)"，p22）。这部分缓解了 selection bias 的担忧。

但 R1 的核心关切仍然成立：63% 的任务空间被排除意味着框架对 ScienceWorld 的覆盖面有限。特别是第三类排除（双策略均近零进展）可能系统性地排除了 routing 信号结构不同的任务（如极难任务中两种策略可能有不同的失败模式）。

---

[AGREE] R1-W3: Router 训练 negative result 的解释不完整

完全同意。我在自己的 W1 中提出了相同关切并列出了四个未排除的替代假设（标签噪声、模型容量、数据量、粒度不匹配）。R1 的表述 "single architecture family + single training paradigm" 更简洁地概括了问题。

**补充**：论文 §3.6 (p7) 提到 "oracle margin (2.89 points) caps routing upside"——如果 oracle 本身的上界只有 2.89 points，那么 router 即使完美学习信号也只能带来微小改进，这使得 negative result 的诊断意义进一步降低。这一点论文没有充分讨论。

---

[AGREE] R1-W4: 跨环境 probes 深度不足

同意。MATH 和 ALFWorld 的 probes 在我的 N1 中是支持 "finding 不泛化" 结论的核心证据。MATH 仅做了 aggregate-level 分析（§3.4, p6: 仅报告 "no routing signal without catastrophic failure, no routing signal emerges"），没有 per-category breakdown 分析路由信号在 Algebra vs. Counting & Probability 等子类中是否存在结构差异。ALFWorld 的 DAF=0% 实际上是更有信息量的结果（information asymmetry 而非 death avoidance 驱动），但论文仅用一段简短讨论带过。

**补充**：ALFWorld 的 finding 实际上暗示了一个更有趣的研究方向——不同环境的 routing 信号可能由完全不同的机制驱动（ScienceWorld: death avoidance, ALFWorld: information asymmetry, MATH: 无信号）。如果论文的 framing 是 "环境诊断框架揭示了不同环境的异质性 routing 机制" 而非 "death avoidance 是主导信号"，贡献定位会更准确也更有趣。

---

[REBUT] R1-W5: 分解公式 Δ_full ≈ δP + Δ_nd 的近似误差

这一关切部分成立但需要澄清。从 §2.3 (p3) 的定义来看，Δ_tot 是所有 episodes 的平均 score gap，可以精确分解为 death-asymmetric episodes 和 non-death-asymmetric episodes 两组的加权贡献——这是一个 **exact partitioning**（对 episodes 的 mutually exclusive 分组求和），不存在交互项。

但 R1 的关切可能指向另一个层面：当论文将 death episodes 的贡献近似为 δP（penalty differential）时，忽略了 death episodes 中死亡前的 partial scores。如果一个 episode 在 step 15 死亡且之前积累了一些 partial score，该 episode 的 score gap ≠ P，而是 (partial_score_surviving - (partial_score_dying + P))。在这个意义上，δP 确实是对 death episode 贡献的近似。

但论文 Appendix K (p17) 的 penalty sensitivity 分析表明，当 P 足够大时（P≥100），partial score 的贡献相对于 |P| 可忽略（ScienceWorld scores 通常 0-100 scale 上在个位数到几十）。所以近似误差在 P=100 时很小，但在 P=10 时可能不可忽略。

**结论**：R1 的技术关切有道理——论文应在 §2.3 或 Appendix 中明确说明分解是 exact（对 episodes）还是 approximate（对 penalty contribution），并在 P 较小时量化 residual。但这不改变主要结论的方向性。

---

### 小问题

对 R1 的 5 个小问题无异议：
1. 页数边界需核查（EMNLP 2026 正文 ≤8 页）
2. §3.1 的 150 vs 95 表述歧义应修正
3. webb-2023 年份不匹配我的引用验证也发现了（bib=2023 vs OpenAlex=2014）
4. Figure 2 y 轴标注确实需要改进
5. Algorithm 1 的隐含假设（P < max_possible_partial_score）确实应说明

---

### 总结

R1 和 R2 的审稿意见高度互补。R1 从 **技术层面**（penalty sensitivity, 统计推断, 分解近似）精确地诊断了问题，R2 从 **定位层面**（framing overclaiming, 新颖性不足, 环境特异性）提出了更宏观的关切。两份 review 的核心交集在于：

1. **DAF/death dominance 的 generality 不足**——R1 从 penalty-sensitivity 角度，R2 从 cross-environment 角度，殊途同归
2. **模型规模覆盖不足**——R1 和 R2 均指出 7-9B tier 的局限
3. **Router negative result 的解释不完整**——R1 和 R2 均认为替代假设未排除

综合两份 review，我维持 Overall 3.0 (Findings) 的评分。R1 给出 3.5 (Borderline Conference) 比我高 0.5 分，我认为差异主要在于对新颖性的评估——R1 更看重框架的完整性和统计严谨性，而我更关注 finding 的 trivially-obvious 程度和 framing 的公允性。

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

_source line 2176 · 2026-05-21T22:19:28.263320+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 178

## Round 178

2 recorded events


### User

_source line 2177 · 2026-05-21T22:19:30.760271+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：对 R1 的 7 个问题中，6 个 [AGREE]、1 个 [REBUT]（W5 分解近似误差——episode 层面是 exact partitioning，但 penalty contribution 层面确有近似，需论文澄清）。R1 和 R2 的核心关切高度一致：DAF dominance 的泛化性不足、模型规模覆盖有限、router negative result 解释不完整。两份 review 的分歧仅在 0.5 分（R1: 3.5 Borderline Conference vs R2: 3.0 Findings），主要来自对新颖性和 framing 公允性的权重差异。

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

_source line 2178 · 2026-05-21T22:19:35.673561+00:00_

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


## Round 179

## Round 179

16 recorded events


### User

_source line 2179 · 2026-05-21T22:21:03.258146+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 核心 finding 的环境特异性与 framing overclaiming**

同意 framing 层面存在问题，但不同意 "循环论证" 和 "MATH/ALFWorld 直接推翻" 的措辞。

理由与证据：
- **标题本身有 scoping**：标题副标题是 "A Counterfactual Analysis on ScienceWorld"，在标题层面已限定范围。R2 认为标题暗示一般性发现，但 "on ScienceWorld" 的存在使这一批评有所减弱。
- **但 Abstract/Introduction 确实 overclaim**：Abstract 说 "contradicting the routing literature's implicit assumption of diverse signal sources"；Introduction 说 "no prior work has decomposed what drives routing decisions in interactive environments"。这些表述超出了 ScienceWorld 单一环境的证据支撑。我同意 R2 这个层面的批评。
- **不同意 "循环论证"**：论文并非先假设死亡重要再证明死亡重要。它提出了一个开放性问题（什么驱动 routing preference？），然后通过 empirical decomposition 发现死亡不对称是主导因素。这不是循环——结论是 empirical finding，而非 definitional artifact。但正如我在 R1-N1 中指出的，DAF=90% 这一数字确实受 penalty 幅度（P=100）的强烈影响（Table 12: P=0 时 DAF=7.4%），这更多是 reward design amplification 而非 inherent signal dominance。
- **不同意 "MATH/ALFWorld 直接推翻"**：MATH 无死亡机制、ALFWorld 无死亡机制——这些环境 DAF=0% 是定义上的必然，不构成对 ScienceWorld 发现的 "推翻"。论文将其定位为 "boundary probes" 展示框架的诊断能力（在不同环境诊断出不同 dominant signal），这一定位本身是合理的。R2 将 DAF=0% 解读为反证，但它实际上是框架正确工作的表现——不同环境应该有不同的诊断结果。
- **建议方向**：同意 R2 将论文重定位为 "诊断框架 + 环境特定 case study" 的建议。但标题不一定需要改——调整 Abstract/Introduction 的 framing 即可（去掉 "contradicting" 等过强措辞）。

---

**[REBUT] R2-N2: 反事实框架的方法论新颖性不足**

不同意将此列为 Must-Fix。论文投稿 track 是 Interpretability and Analysis，其贡献标准是诊断性洞察而非数学框架新颖性。

理由与证据：
- **分析类论文的贡献标准**：EMNLP Interpretability and Analysis track 的核心评价标准是 "是否揭示了对模型/系统行为的有意义理解"，而非 "方法论是否数学复杂"。许多高影响的分析论文使用简单方法得出深刻洞察（如 probing classifiers 本质上也是 "训练一个线性层然后看准确率"）。Algorithm 1 的简单性是 feature 而非 bug——它使框架易于 replicate 和应用于新环境。
- **DAF 的非平凡之处**：R2 称 "DAF 数学上平凡"，但 DAF 的价值在于它将一个模糊的直觉（"死亡好像很重要"）量化为可比较、可跟踪的指标，并通过 decomposition 将 total gap 分解为 death-attributable 和 non-death 部分。数学上简洁不等于学术上平凡。
- **关于 Pearl/Rubin 连接**：论文使用 "counterfactual" 一词的方式是 NLP/ML 社区的常见非正式用法（"如果用另一种策略会怎样"），而非 Pearl 的结构因果模型意义上的反事实。强制要求 do-calculus 形式化对此类应用研究不合适——论文的 "counterfactual" 更接近 Rubin 框架的 potential outcomes 概念（两种 treatment 下的 outcome 比较），而 potential outcomes 框架本身的数学就是直接比较。
- **但同意作为 Should-Fix**：在 Related Work 中增加一段简要讨论与因果推断文献的关系（区分论文的 "intervention comparison" 与 Pearl 的结构因果反事实），可以增强论文的学术定位。这是 improvement 而非 blocker。

---

**[AGREE] R2-N3: "Contradicting the routing literature" 的 framing 不公允**

同意，但认为严重程度介于 Must-Fix 和 Should-Fix 之间。

理由与证据：
- **R2 的批评是准确的**：论文引用的 routing 工作（CogRouter, ARES, MTRouter, RouteLLM, Budget-Aware Routing 等）操作在 model selection、computational routing、multi-turn routing 等 settings，这些 settings 没有 ScienceWorld 式的 catastrophic failure 机制。说这些工作 "implicitly assume diverse signal sources" 是合理的推断，但说 ScienceWorld 的发现 "contradicts" 这一假设则是 strawman——在无 catastrophic failure 的环境中，信号确实可能是多样化的（ALFWorld 的结果恰好支持了这一点）。
- **"Contradicting" 应改为更精确的表述**：如 "revealing that in catastrophic-failure environments, signal diversity may collapse to a single dominant factor" 或 "complementing the routing literature by identifying conditions under which diverse-signal assumptions break down"。
- **不完全同意 Must-Fix 级别**：这本质上是一个 framing/wording 问题，可以通过修改几句话解决，不涉及实验或分析的根本缺陷。我倾向于将其归为 strong Should-Fix。

---

### Should-Fix 问题

**[AGREE] R2-W1: Router training 负面结果解释不完整**

与我的 R1-W3 一致。论文在 Section 3.6 提供了两种解读（A: 噪声标签；B: 信号在 task-type 级别），但未排除第三种可能性：更好的训练方法（不同 loss function、contrastive learning、更多数据）可能成功。实验覆盖了 3 个 Qwen3 规模（0.6B/1.7B/4B, Appendix I），但仍限于单一架构族 + LoRA，training data 仅 2,040 步。建议明确标注为 "preliminary negative result" 而非暗示 definitive non-learnability。

---

**[AGREE] R2-W2: 模型规模覆盖不足**

与我的 R1-N2 一致（我将其列为 Must-Fix）。7-9B 模型在能力和内部死亡率上高度相似（~42%），不足以声称 "cross-model" 复制。Appendix P 的 72B 数据显示死亡率降至 ~31%，但未计算 DAF——这是关键缺失。更大模型可能因更低的死亡率而根本性地改变 routing landscape。

---

**[REBUT] R2-W3: DAF metric 的独立学术价值——"在 ScienceWorld 之外 DAF 恒为 0"**

R2 的这一判断过于狭隘。

理由：
- **DAF 测量的是 death-asymmetric episodes 对 score gap 的贡献**。在没有死亡机制的环境中 DAF=0 是正确的诊断结果，不是指标的缺陷——就像测体温对健康人得到 36.5°C 不意味着体温计没有学术价值。
- **DAF 在其他 catastrophic-failure 环境中可以非零**：自动驾驶仿真、safety-critical RL、任何有 irreversible failure 的 agent 环境都可能有非零 DAF。ScienceWorld 不是唯一有死亡/失败机制的环境。
- **框架的价值不仅在 DAF**：Episode-level labeling（Algorithm 1）和 decomposition approach 本身是通用的——在 ALFWorld 中，框架诊断出 information asymmetry 而非 death avoidance 是 dominant signal（Section 3.4, Table 15）。框架的可扩展性恰恰体现在 DAF=0 时它仍然能提供有用诊断。
- **但同意一个改进方向**：论文可以讨论 DAF 的泛化版本——将 "death" 替换为一般性 "catastrophic failure"（任何导致 episode 提前终止的不可逆事件），这样 metric 的适用范围会更广。

---

**[AGREE] R2-W4: ~50-episode pilot 的 practical claim 证据薄弱**

同意。论文在 Section 5 和 Appendix R 提出 "~50-episode pilot suffices for build-vs-buy decisions"，但未提供支撑这一数字的 power analysis。当前证据仅为：ScienceWorld 中效应极大（Cohen's d = 3.02），因此小样本也能检测到。但这一推理假设新环境会有类似大小的效应——如果新环境的 effect size 较小（如 DAF=30%），50 个 episode 可能远远不够。建议补充：(a) 给出效应量假设下的 power 计算；或 (b) 将 "~50" 弱化为 "an initial pilot of tens of episodes can provide preliminary signal"。

---

**[AGREE partially] R2-W5: 相关工作遗漏**

部分同意。

- **Pearl/Rubin 因果推断文献**：[AGREE] 论文大量使用 "counterfactual" 一词，至少应在 Related Work 中简要讨论与形式化因果推断的关系和区别。这不需要重写框架，一段说明即可（"Our use of 'counterfactual' follows the potential-outcomes tradition (Rubin, 1974) of comparing realized outcomes under alternative treatments, rather than Pearl's (2009) structural counterfactuals"）。
- **Agent safety / catastrophic failure avoidance 文献**：[AGREE partially] 论文已引用了 safe RL 文献（Garcia 2015, Achiam 2017, Moldovan 2012）和 agent safety benchmark（Ruan 2024, Agent-SafetyBench 2024），覆盖面可接受。但 R2 提到的 catastrophic failure avoidance in LLM agents 方向（如将 catastrophic actions 作为 distinct failure category 的 Ruan et al. 2024——论文已引用）似乎已在 Section 4 Related Work 的 "Safe RL" 段落中涉及。需要 R2 提供具体遗漏论文才能进一步判断。
- **Credit assignment for LLM agents**：[REBUT] 论文已引用 SALT (2026) 和 CSO (2026)，这两篇是 LLM agent 领域最相关的 credit assignment 工作。除非 R2 能指出具体遗漏的 key paper，否则当前覆盖面足够。

---

## 总结：与 R2 的分歧和共识

| R2 Issue | R1 判断 | 核心分歧 |
|----------|--------|---------|
| N1 (framing overclaiming) | [AGREE] framing 需调整 | 不同意 "循环论证" 和 "MATH/ALFWorld 直接推翻" 的措辞 |
| N2 (方法论新颖性不足) | [REBUT] as Must-Fix | Analysis track 贡献标准不要求数学框架新颖性 |
| N3 ("contradicting" 是 strawman) | [AGREE] | 同意应改为更精确的定位 |
| W1 (router training) | [AGREE] | 与 R1-W3 一致 |
| W2 (model scale) | [AGREE] | 与 R1-N2 一致（R1 列为 Must-Fix） |
| W3 (DAF 独立价值) | [REBUT] | DAF 在 catastrophic-failure 环境中通用；框架价值不限于 DAF |
| W4 (~50-episode pilot) | [AGREE] | 需要 power analysis |
| W5 (related work 遗漏) | [AGREE partially] | Pearl/Rubin 应加；其他需要具体论文才能判断 |

**R1 与 R2 的主要分歧**：R2 给 3.0 (Findings)，我给 3.5 (Borderline Conference)。差异主要在于 R2 的 N2（方法论新颖性不足）——我认为这不应是 Must-Fix，因为 Analysis track 的贡献标准不同于 methods track。如果去除 N2 作为 Must-Fix，R2 的其余意见（framing 调整 + model scale + practical claim 弱化）均可通过修订解决，修订后论文质量足以达到 Borderline Conference。

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

_source line 2180 · 2026-05-21T22:21:41.999965+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉回应已收集'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题已达成共识，一轮即收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'in_progress', 'activeForm': '合成最终审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉回应已收集'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题已达成共识，一轮即收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'in_progress', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2181 · 2026-05-21T22:21:42.000536+00:00_

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

_source line 2182 · 2026-05-21T22:21:42.901183+00:00_

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

_source line 2183 · 2026-05-21T22:21:43.353565+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T22:05:55.483236+00:00\", \"completed_at\": \"2026-05-21T22:09:21.392627+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前两页为纯文本（Title + Abstract + Introduction + Method Setup），无任何 display item。审稿人需阅读超过 1.5 页密集文字才能看到第一个视觉锚点（Figure 1 在 page 3）。建议考虑将 Figure 1（框架概览图）提前至 page 2 或 page 1 底部，帮助审稿人在前 2 分钟内建立认知锚点\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（Counterfactual episode collection pipeline）仅占右栏约 1/3 高度，作为论文第一个 display item 且承载核心框架信息，偏小。考虑改为 figure*（双栏全宽）以增强第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 caption 描述了 pipeline 流程，基本自包含，但可补充一句核心发现（如 \\\"death episodes dominate the routing gap\\\"）使 caption 更具信息量\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（scatter plot）清晰可读，trend line + 置信区间呈现合理。颜色为单色点，无色盲问题。Caption 自包含程度好\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 + Figure 3 并排排列，视觉节奏好。Table 1 使用 booktabs 风格，无竖线。Figure 3 有 error bars，两色（Retry vs Reflection）区分度足够\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"纯文本页——前后分别为 page 4（有 Figure 2）和 page 6（有 Table 1 + Figure 3），page 5 整页无任何 display item。内容为 correlation structure / signal concentration / sensitivity 分析，适合用小型 summary table 或 heatmap 打破纯文本单调\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 使用 table*（全宽跨栏），排版恰当。最优值已加粗。格式规范\"}, {\"severity\": \"warning\", \"dimension\": \"page 7-8-9\", \"message\": \"三页连续以文字为主：page 7 仅顶部有 Table 2，page 8（Discussion + Conclusion）和 page 9（Limitations + Ethics）均为纯文本。审稿人在论文后半段连续阅读约 2.5 页无视觉刺激。Discussion 中可考虑加入一个 summary figure 或 key finding 的 highlight box\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"主体正文 8 页中共 5 个 display items（3 figures + 2 tables），密度 0.625/页。对于实证分析型论文偏低（通常 5-8 个），但本文偏分析诊断型，尚可接受\"}, {\"severity\": \"info\",
…[truncated 1911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2184 · 2026-05-21T22:21:43.354056+00:00_

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

_source line 2185 · 2026-05-21T22:21:44.358306+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2186 · 2026-05-21T22:21:44.459317+00:00_

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

_source line 2187 · 2026-05-21T22:21:44.811591+00:00_

1	# Round 25 Review Issues (fresh review, 2026-05-21)
2	# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+相关工作)
3	
4	# =============================================
5	# Carried-over resolved issues (from prior rounds)
6	# =============================================
7	
8	- id: "R13-W1"
9	  summary: "正文篇幅严重不足 long paper 要求"
10	  category: format
11	  severity: warning
12	  status: resolved
13	  first_raised_round: 13
14	  last_seen_round: 14
15	  resolution: "正文已扩展至 8 页"
16	  resolution_round: 14
17	
18	- id: "R13-W2"
19	  summary: "Router 训练实验存在多个 confound"
20	  category: experiment
21	  severity: warning
22	  status: resolved
23	  first_raised_round: 13
24	  last_seen_round: 15
25	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
26	  resolution_round: 15
27	
28	- id: "R13-W3"
29	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
30	  category: method
31	  severity: info
32	  status: resolved
33	  first_raised_round: 13
34	  last_seen_round: 14
35	  resolution: "Limitations 和 Appendix B 已充分量化"
36	  resolution_round: 14
37	
38	- id: "R13-W4"
39	  summary: "SCI 方法贡献与实际使用不成比例"
40	  category: method
41	  severity: info
42	  status: resolved
43	  first_raised_round: 13
44	  last_seen_round: 14
45	  resolution: "SCI 已降级到 Appendix A"
46	  resolution_round: 14
47	
48	- id: "R13-W7"
49	  summary: "Router negative results 解释不完整"
50	  category: experiment
51	  severity: warning
52	  status: resolved
53	  first_raised_round: 13
54	  last_seen_round: 15
55	  resolution: "Router 实验定位为 diagnostic probe"
56	  resolution_round: 15
57	
58	- id: "R13-m2"
59	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
60	  category: writing
61	  severity: warning
62	  status: resolved
63	  first_raised_round: 13
64	  last_seen_round: 16
65	  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
66	  resolution_round: 16
67	
68	- id: "R13-m3"
69	  summary: "Reference 格式不统一 + orphan entries"
70	  category: format
71	  severity: info
72	  status: resolved
73	  first_raised
…[truncated 27207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2188 · 2026-05-21T22:25:33.493780+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "# Round 26 Review Issues (fresh review, 2026-05-21)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+相关工作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n# =============================================\n# Round 26 — Active issues (new + recurring)\n# =============================================\n\n# --- Critical / Must-Fix ---\n\n- id: \"R26-N1\"\n  summary: \"DAF 'dominance' 由 penalty 幅度驱动（P=0 时 DAF=7.4%），正文 framing 未充分反映 penalty sensitivity\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 resolved: Abstract 以 label fraction 为 headline\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1 Must-Fix: Table 12 (P=0→DAF=7.4%, P=100→DAF=90.1%) 表明 dominance 是 reward design 产物。R2 交叉 AGREE 并补充：label fraction 78.9% 才是真正 robust metric，但论文仍以 DAF 为主推。Abstract 'DAF=88-90% across three model families' 过于突出。共识：正文 §2.3 或 §5 需正面讨论 Table 12 含义，label fraction 应为 primary claim。\"\n  action_items:\n    - round: 26\n      action: \"在正文 §3.1 或 §5 增加一段正面讨论 penalty sensitivity（Table 12），明确 DAF 是 penalty-dependent metric\"\n      assigned_to: research_director\n      status: pending\n    - round: 26\n      action: \"Abstract/Introduction 中以 78.9% label fraction 为 headline，DAF 降级为补充指标\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-N2\"\n  summary: \"跨模型验证仅覆盖 7-9B 同级模型，72B 已有数据但未计算 DAF，不支撑 'cross-model family' 声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 72B DAF decomposition 已呈现\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1 Must-Fix: 三模型 7-9B 幻觉率均 ~42%，一致性反映 tier 共性而非 cross-scale robustness。R2 交叉 AGREE 补充：72B 死亡率降至 ~31% 但 DAF 未计算是显著遗漏。论文 §3.3 报告 72B DAF=92.4%（死亡率 30.6% vs det 2.75%），但这在 Agent Improvement §3.3 中，不在 §3.2 Cross-Model 段。需核实 §3.3 数据是否已充分呈现 72B DAF。\"\n  action_items:\n    - round: 26\n      action: \"核实 §3.3 的 72B DAF=92.4% 是否充分讨论；若是，则将 'cross-model' 声明限定为 'within 7-9B tier'，72B 结果定位为 scaling analysis\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing——被引 routing 工作操作在无 catastrophic failure 的不同 settings\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R2 Must-Fix: CogRouter/ARES/MTRouter/RouteLLM 等在 model selection、computational routing settings，无 catastrophic failure 机制。R1 交叉 AGREE 但认为严重程度介于 Must-Fix 和 Should-Fix——本质是 wording 问题可通过修改几句话解决。共识：'contradicting' 应改为 'revealing that in catastrophic-failure environments, signal diversity may collapse' 或类似表述。\"\n  action_items:\n    - round: 26\n      action: \"将 Abstract/Introduction 中 'contradicting the routing literature's implicit assumption' 改为更精确的定位表述\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——death dominance 在 oracle vs. hallucinating-LLM 设置下方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 Excitement 均 2.5。§5 Non-triviality 论证有效缓解但不消除。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2 Excitement 2.5, R1 Excitement 3.0。R2-N1 称 finding 'trivially obvious'，R1 交叉回应 AGREE framing 需调整但不同意 '循环论证'——结论是 empirical finding 而非 definitional artifact。共识：这是 Findings 而非 Conference 水平的核心原因，不可通过 writing 修复。\"\n\n# --- Warning / Should-Fix ---\n\n- id: \"R26-W1\"\n  summary: \"框架方法论新颖性不足——Algorithm 1 是 if-else 分类树，DAF 数学上平凡，未连接因果推断文献\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2 列为 Must-Fix (N2)：框架缺乏技术深度，未连接 Pearl/Rubin。R1 REBUT 为 Must-Fix：Analysis track 贡献标准不要求数学框架新颖性，简单方法得出深刻洞察在 probing 文献中常见。R1 同意作为 Should-Fix——在 Related Work 中简要讨论与因果推断的关系即可。\"\n  action_items:\n    - round: 26\n      action: \"在 Related Work §4 中增加一段讨论与 potential outcomes (Rubin 1974) 和结构因果模型 (Pearl 2009) 的关系和区别\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W2\"\n  summary: \"Router negative result 解释不完整——未排除模型容量不足、数据量不够、训练方法局限等替代假设\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 resolved: Router claim 从绝对否定改为有条件否定\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1-W3 + R2-W1 一致：single architecture family (Qwen3) + single training paradigm (LoRA) + 2040 training steps。R2 补充：oracle margin 仅 2.89 points 进一步降低 negative result 的诊断意义。共识：应明确标注为 'preliminary negative result' 而非暗示 definitive non-learnability。\"\n  action_items:\n    - round: 26\n      action: \"§3.6 中明确标注为 preliminary negative result；补充讨论替代训练方法的可能性\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W3\"\n  summary: \"~50-episode pilot 的 practical claim 缺乏 power analysis 或 sample-size calculation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R2-W4 提出，R1 交叉 AGREE。当前证据仅为 ScienceWorld 效应极大（d=3.02）所以小样本可检测，但假设新环境有类似大效应不成立时 50 episodes 可能不够。\"\n  action_items:\n    - round: 26\n      action: \"补充 power analysis 或将 'suffices' 弱化为 'provides preliminary signal'\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W4\"\n  summary: \"Cluster bootstrap K=11 正文 caveat 不够显著——远低于 K≥20-30 可靠推断要求\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 resolved: non-clustered bootstrap 为主推断\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1-W1 提出，R2 交叉 AGREE。正文 §3.1 仅简短提及，caveat 不够显著。\"\n  action_items:\n    - round: 26\n      action: \"§3.1 报告 cluster bootstrap 结果时紧跟一句明确 caveat\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W5\"\n  summary: \"11/30 task types (63% excluded) 的 selection bias——agent-floor tasks 对 death dominance 的含义未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 anti-cherry-picking analysis 缓解但不消除\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1-W2 提出，R2 交叉 AGREE 但指出 Appendix C/S 已部分验证。深层关切：7 个 agent-floor tasks（两策略都死亡/无 asymmetry）可能代表 death dominance 不成立的 regime，应在 Discussion 讨论。\"\n  action_items:\n    - round: 26\n      action: \"Discussion 中补充讨论 agent-floor tasks 对 death dominance 的含义\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W6\"\n  summary: \"跨环境 probes (MATH/ALFWorld) 深度不足，且 ALFWorld DAF=0% 实际上削弱 death avoidance 的一般性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1-W4 + R2-N1 一致。MATH 仅 aggregate-level 无 per-category 分解，ALFWorld 仅一段简短讨论。R2 补充：如果 reframe 为 '不同环境有异质 routing 机制' 而非 'death avoidance 是主导'，贡献定位更准确。\"\n  action_items:\n    - round: 26\n      action: \"调整 Abstract/Introduction 措辞避免暗示 generalizability；或加深 MATH/ALFWorld 分析\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W7\"\n  summary: \"相关工作遗漏——Pearl/Rubin 因果推断、agent safety catastrophic failure avoidance 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2-W5 提出 5 类遗漏，R1 部分 AGREE：(a) Pearl/Rubin 因果推断 [AGREE]；(b) Agent safety catastrophic failure avoidance [AGREE partially，论文已引 Ruan 2024]；(c) Credit assignment [REBUT，SALT/CSO 已引用]。R2 建议具体补充：Check Yourself Before You Wreck Yourself (arXiv 2510.16492)。\"\n  action_items:\n    - round: 26\n      action: \"Related Work 中简要讨论与 potential outcomes / causal inference 的关系；评估 R2 建议的具体 missing references\"\n      assigned_to: research_director\n      status: pending\n\n# --- Minor / Info ---\n\n- id: \"R26-M1\"\n  summary: \"页数边界：Conclusion 可能溢出到 page 9（需核查）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1]\n      note: \"R1 小问题：Conclusion 末尾 ~2 行可能溢出到 page 9。视觉审查确认正文 through Conclusion 在 page 8 结束，Limitations 在 page 9——需核查 Conclusion 是否完整在 page 8 内。\"\n\n- id: \"R26-M2\"\n  summary: \"引用验证：5 条 not_found + 6 条 mismatch（多为 OpenAlex 索引问题）；webb-2023 年份需核查\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位 reviewer 独立发现相同引用问题。Webb 2023 (CJE vol.56 no.3) 在 R25 已核实正确。\"\n\n- id: \"R26-M3\"\n  summary: \"Figure 2 y 轴标签单位不明确（absolute score difference vs percentage points）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1]\n      note: \"R1 小问题。\"\n\n- id: \"R26-M4\"\n  summary: \"Algorithm 1 隐含假设（P < max_possible_partial_score 时 death-priority 规则可能不成立）未说明\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1]\n      note: \"R1 小问题。R2 无异议。\"\n\n- id: \"R26-M5\"\n  summary: \"§3.1 数字表述歧义——150 (61.2%) no-preference 和 95 有偏好 的关系需更清晰表述\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1]\n      note: \"R1 小问题。\"\n\n# --- Carried-over open/in_progress from R25, not raised in R26 ---\n\n- id: \"R25-W1\"\n  summary: \"Router negative result 替代解释未充分排除——缺少 task-level router positive control\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"被 R26-W2 覆盖（router negative result 解释不完整）\"\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"被 R26-W5 覆盖\"\n\n- id: \"R25-W5\"\n  summary: \"实验规模偏小（per-task n=20），per-task 统计 power 不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W1 (cluster bootstrap) 间接涉及。共识：aggregate claims 可靠，per-task 需谨慎。不构成 blocking issue。\"\n\n- id: \"R25-W6\"\n  summary: \"实际指导价值有限——诊断之外缺少 constructive 解决路径\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R26 未直接提及，但 R2 overall assessment 中 '结论本质上是 ScienceWorld 里直接用 deterministic 即可' 间接涉及。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2-N2 (框架新颖性) 和 R2-N3 (contradicting framing) 间接涉及。R1 REBUT N2 为 Must-Fix。\"\n"
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
    "issues_yaml": "# Round 26 Review Issues (fresh review, 2026-05-21)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+相关工作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n# =============================================\n# Round 26 — Active issues (new + recurring)\n# =============================================\n\n# --- Critical / Must-Fix ---\n\n- id: \"R26-N1\"\n  summary: \"DAF 'dominance' 由 penalty 幅度驱动（P=0 时 DAF=7.4%），正文 framing 未充分反映 penalty sensitivity\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 resolved: Abstract 以 label fraction 为 headline\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1 Must-Fix: Table 12 (P=0→DAF=7.4%, P=100→DAF=90.1%) 表明 dominance 是 reward design 产物。R2 交叉 AGREE 并补充：label fraction 78.9% 才是真正 robust metric，但论文仍以 DAF 为主推。Abstract 'DAF=88-90% across three model families' 过于突出。共识：正文 §2.3 或 §5 需正面讨论 Table 12 含义，label fraction 应为 primary claim。\"\n  action_items:\n    - round: 26\n      action: \"在正文 §3.1 或 §5 增加一段正面讨论 penalty sensitivity（Table 12），明确 DAF 是 penalty-dependent metric\"\n      assigned_to: research_director\n      status: pending\n    - round: 26\n      action: \"Abstract/Introduction 中以 78.9% label fraction 为 headline，DAF 降级为补充指标\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-N2\"\n  summary: \"跨模型验证仅覆盖 7-9B 同级模型，72B 已有数据但未计算 DAF，不支撑 'cross-model family' 声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 72B DAF decomposition 已呈现\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1 Must-Fix: 三模型 7-9B 幻觉率均 ~42%，一致性反映 tier 共性而非 cross-scale robustness。R2 交叉 AGREE 补充：72B 死亡率降至 ~31% 但 DAF 未计算是显著遗漏。论文 §3.3 报告 72B DAF=92.4%（死亡率 30.6% vs det 2.75%），但这在 Agent Improvement §3.3 中，不在 §3.2 Cross-Model 段。需核实 §3.3 数据是否已充分呈现 72B DAF。\"\n  action_items:\n    - round: 26\n      action: \"核实 §3.3 的 72B DAF=92.4% 是否充分讨论；若是，则将 'cross-model' 声明限定为 'within 7-9B tier'，72B 结果定位为 scaling analysis\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing——被引 routing 工作操作在无 catastrophic failure 的不同 settings\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R2 Must-Fix: CogRouter/ARES/MTRouter/RouteLLM 等在 model selection、computational routing settings，无 catastrophic failure 机制。R1 交叉 AGREE 但认为严重程度介于 Must-Fix 和 Should-Fix——本质是 wording 问题可通过修改几句话解决。共识：'contradicting' 应改为 'revealing that in catastrophic-failure environments, signal diversity may collapse' 或类似表述。\"\n  action_items:\n    - round: 26\n      action: \"将 Abstract/Introduction 中 'contradicting the routing literature's implicit assumption' 改为更精确的定位表述\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——death dominance 在 oracle vs. hallucinating-LLM 设置下方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 Excitement 均 2.5。§5 Non-triviality 论证有效缓解但不消除。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2 Excitement 2.5, R1 Excitement 3.0。R2-N1 称 finding 'trivially obvious'，R1 交叉回应 AGREE framing 需调整但不同意 '循环论证'——结论是 empirical finding 而非 definitional artifact。共识：这是 Findings 而非 Conference 水平的核心原因，不可通过 writing 修复。\"\n\n# --- Warning / Should-Fix ---\n\n- id: \"R26-W1\"\n  summary: \"框架方法论新颖性不足——Algorithm 1 是 if-else 分类树，DAF 数学上平凡，未连接因果推断文献\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2 列为 Must-Fix (N2)：框架缺乏技术深度，未连接 Pearl/Rubin。R1 REBUT 为 Must-Fix：Analysis track 贡献标准不要求数学框架新颖性，简单方法得出深刻洞察在 probing 文献中常见。R1 同意作为 Should-Fix——在 Related Work 中简要讨论与因果推断的关系即可。\"\n  action_items:\n    - round: 26\n      action: \"在 Related Work §4 中增加一段讨论与 potential outcomes (Rubin 1974) 和结构因果模型 (Pearl 2009) 的关系和区别\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W2\"\n  summary: \"Router negative result 解释不完整——未排除模型容量不足、数据量不够、训练方法局限等替代假设\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 resolved: Router claim 从绝对否定改为有条件否定\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1-W3 + R2-W1 一致：single architecture family (Qwen3) + single training paradigm (LoRA) + 2040 training steps。R2 补充：oracle margin 仅 2.89 points 进一步降低 negative result 的诊断意义。共识：应明确标注为 'preliminary negative result' 而非暗示 definitive non-learnability。\"\n  action_items:\n    - round: 26\n      action: \"§3.6 中明确标注为 preliminary negative result；补充讨论替代训练方法的可能性\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W3\"\n  summary: \"~50-episode pilot 的 practical claim 缺乏 power analysis 或 sample-size calculation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R2-W4 提出，R1 交叉 AGREE。当前证据仅为 ScienceWorld 效应极大（d=3.02）所以小样本可检测，但假设新环境有类似大效应不成立时 50 episodes 可能不够。\"\n  action_items:\n    - round: 26\n      action: \"补充 power analysis 或将 'suffices' 弱化为 'provides preliminary signal'\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W4\"\n  summary: \"Cluster bootstrap K=11 正文 caveat 不够显著——远低于 K≥20-30 可靠推断要求\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 resolved: non-clustered bootstrap 为主推断\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1-W1 提出，R2 交叉 AGREE。正文 §3.1 仅简短提及，caveat 不够显著。\"\n  action_items:\n    - round: 26\n      action: \"§3.1 报告 cluster bootstrap 结果时紧跟一句明确 caveat\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W5\"\n  summary: \"11/30 task types (63% excluded) 的 selection bias——agent-floor tasks 对 death dominance 的含义未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 anti-cherry-picking analysis 缓解但不消除\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1-W2 提出，R2 交叉 AGREE 但指出 Appendix C/S 已部分验证。深层关切：7 个 agent-floor tasks（两策略都死亡/无 asymmetry）可能代表 death dominance 不成立的 regime，应在 Discussion 讨论。\"\n  action_items:\n    - round: 26\n      action: \"Discussion 中补充讨论 agent-floor tasks 对 death dominance 的含义\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W6\"\n  summary: \"跨环境 probes (MATH/ALFWorld) 深度不足，且 ALFWorld DAF=0% 实际上削弱 death avoidance 的一般性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"[AGREE x2] R1-W4 + R2-N1 一致。MATH 仅 aggregate-level 无 per-category 分解，ALFWorld 仅一段简短讨论。R2 补充：如果 reframe 为 '不同环境有异质 routing 机制' 而非 'death avoidance 是主导'，贡献定位更准确。\"\n  action_items:\n    - round: 26\n      action: \"调整 Abstract/Introduction 措辞避免暗示 generalizability；或加深 MATH/ALFWorld 分析\"\n      assigned_to: research_director\n      status: pending\n\n- id: \"R26-W7\"\n  summary: \"相关工作遗漏——Pearl/Rubin 因果推断、agent safety catastrophic failure avoidance 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2-W5 提出 5 类遗漏，R1 部分 AGREE：(a) Pearl/Rubin 因果推断 [AGREE]；(b) Agent safety catastrophic failure avoidance [AGREE partially，论文已引 Ruan 2024]；(c) Credit assignment [REBUT，SALT/CSO 已引用]。R2 建议具体补充：Check Yourself Before You Wreck Yourself (arXiv 2510.16492)。\"\n  action_items:\n    - round: 26\n      action: \"Related Work 中简要讨论与 potential outcomes / causal inference 的关系；评估 R2 建议的具体 missing references\"\n      assigned_to: research_director\n      status: pending\n\n# --- Minor / Info ---\n\n- id: \"R26-M1\"\n  summary: \"页数边界：Conclusion 可能溢出到 page 9（需核查）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1]\n      note: \"R1 小问题：Conclusion 末尾 ~2 行可能溢出到 page 9。视觉审查确认正文 through Conclusion 在 page 8 结束，Limitations 在 page 9——需核查 Conclusion 是否完整在 page 8 内。\"\n\n- id: \"R26-M2\"\n  summary: \"引用验证：5 条 not_found + 6 条 mismatch（多为 OpenAlex 索引问题）；webb-2023 年份需核查\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位 reviewer 独立发现相同引用问题。Webb 2023 (CJE vol.56 no.3) 在 R25 已核实正确。\"\n\n- id: \"R26-M3\"\n  summary: \"Figure 2 y 轴标签单位不明确（absolute score difference vs percentage points）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1]\n      note: \"R1 小问题。\"\n\n- id: \"R26-M4\"\n  summary: \"Algorithm 1 隐含假设（P < max_possible_partial_score 时 death-priority 规则可能不成立）未说明\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1]\n      note: \"R1 小问题。R2 无异议。\"\n\n- id: \"R26-M5\"\n  summary: \"§3.1 数字表述歧义——150 (61.2%) no-preference 和 95 有偏好 的关系需更清晰表述\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1]\n      note: \"R1 小问题。\"\n\n# --- Carried-over open/in_progress from R25, not raised in R26 ---\n\n- id: \"R25-W1\"\n  summary: \"Router negative result 替代解释未充分排除——缺少 task-level router positive control\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"被 R26-W2 覆盖（router negative result 解释不完整）\"\n\n- id: \"R16-N2\"\n  summary: \"Task selection bias: 63% exclusion rate 的 scope limitation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"被 R26-W5 覆盖\"\n\n- id: \"R25-W5\"\n  summary: \"实验规模偏小（per-task n=20），per-task 统计 power 不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W1 (cluster bootstrap) 间接涉及。共识：aggregate claims 可靠，per-task 需谨慎。不构成 blocking issue。\"\n\n- id: \"R25-W6\"\n  summary: \"实际指导价值有限——诊断之外缺少 constructive 解决路径\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R26 未直接提及，但 R2 overall assessment 中 '结论本质上是 ScienceWorld 里直接用 deterministic 即可' 间接涉及。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2-N2 (框架新颖性) 和 R2-N3 (contradicting framing) 间接涉及。R1 REBUT N2 为 Must-Fix。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 2189 · 2026-05-21T22:25:33.645212+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 23145}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2190 · 2026-05-21T22:28:26.197681+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "report": "# 审稿报告：Death Avoidance as the Dominant Routing Signal\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (via ACL Rolling Review) — Interpretability and Analysis track\n**审稿模式**: Fresh review (Round 26)\n**Reviewer 配置**: R1 (方法严谨性+实验设计, 3.5 Borderline Conference) / R2 (新颖性+完整性+相关工作, 3.0 Findings)\n**交叉分享**: 1 轮交叉，关键问题达成高度共识（8 个 AGREE / 2 个 REBUT / 1 个 partial AGREE）\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual diagnostic framework，通过纯策略比较分解 LLM agent routing 信号的构成。在 ScienceWorld（11 task types, 245 episodes）上发现 78.9% 的非 tie routing labels 源于 death asymmetry（内部策略因幻觉触发致命失败，确定性策略存活）。DAF（Death Avoidance Factor）在三个 7-9B 模型家族上达到 88-90%。跨环境 probes（MATH 无信号, ALFWorld 为 information asymmetry）展示了框架的诊断能力但同时表明 death dominance 是环境特定的。Router 训练产出 negative result（step-level balanced accuracy 56-59%）。\n\n---\n\n## Strengths\n\n**S1. 实验设计的系统性和统计严谨性** [AGREE x2]\n跨三个模型家族（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B）的一致性验证、跨三个环境的 probes、多项 ablation（text augmentation, grounding, capacity scaling, Reflexion, retry）。统计处理在 NLP 论文中属上佳水平：episode-level bootstrap (B=10,000)、cluster bootstrap、wild cluster bootstrap、leave-one-task-out sensitivity、Bonferroni correction、penalty sensitivity analysis。\n\n**S2. 诚实的负面结果呈现** [AGREE x2]\nRouter training 低 accuracy（§3.6）、cross-environment probes 否定了 death dominance 的泛化性（§3.4）、text augmentation 无提升（Appendix J）均如实报告。论文在 MATH/ALFWorld 上的 \"boundary probes\" 定位是诚实的。\n\n**S3. 写作质量** [AGREE x2]\n8 页正文 + 20 个 Appendices（A-T）的安排合理。核心 claim 表述清晰，实验 narrative 流畅。Limitations 章节覆盖面好（5 个子段：环境范围、方法论约束、统计限制、pure-strategy upper bound、诊断范围）。\n\n**S4. 可复现性** [AGREE x2]\nAlgorithm 1 伪代码、prompt templates（Appendix T）、router 训练配置（Appendix I）、per-task 分解（Appendix C）均有详细说明。Reproducibility 4/5。\n\n**S5. 框架设计完整性** [R1 强调]\nEpisode-level labeling + DAF decomposition + SCI 三指标形成完整诊断工具链。Algorithm 1 的 edge case 处理（both-dead, both-alive-tied, score-comparison）thorough。Label quality audit（Appendix B）增加数据透明度。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. DAF \"dominance\" 由 penalty 幅度驱动，正文未充分反映 penalty sensitivity** [AGREE x2, critical]\n- Table 12 (Appendix K): P=0 时 DAF=7.4%, P=10 时 DAF=39.8%, P=100 时 DAF=90.1%。DAF=90% 是 reward design 的产物（P=100 在 0-100 score range 内为极端惩罚），而非 routing 信号的内在属性。\n- 78.9% label fraction（不受 penalty 加权影响）是更 robust 的指标，但论文在 Abstract/Introduction 仍以 DAF 88-90% 为 prominent metric。\n- **需要**：(1) 正文 §3.1 或 §5 增加一段正面讨论 Table 12 含义；(2) 以 label fraction 为 primary claim，DAF 降级为补充。\n\n**N2. 跨模型验证仅覆盖 7-9B 同级模型** [AGREE x2, critical]\n- 三个模型参数量和内部死亡率高度相似（~42%），一致性更可能反映 7-9B tier 的共有特征而非跨规模 robustness。\n- §3.3 报告 72B DAF=92.4%（死亡率 30.6% vs det 2.75%），但位于 Agent Improvement 段而非 Cross-Model 段，且未与 7-9B 结果并列讨论。\n- **需要**：(1) 将 \"cross-model family\" 限定为 \"within 7-9B tier\"；(2) 72B 结果明确定位为 scaling analysis。\n\n**N3. \"Contradicting the routing literature's implicit assumption\" 是 strawman framing** [AGREE x2, critical/strong warning]\n- 被引 routing 工作（CogRouter, ARES, MTRouter, RouteLLM, Budget-Aware Routing）操作在 model selection、computational routing、multi-turn routing 等无 catastrophic failure 的 settings。\n- ScienceWorld 的极端 catastrophic failure 使这里发现 death dominance 不构成对这些工作的 \"contradiction\"——论文自己的 ALFWorld 结果恰好支持了其他 settings 可能有多样化信号。\n- R1 认为严重程度介于 Must-Fix 和 Should-Fix——本质是 wording 问题，可通过修改几句话解决。\n- **需要**：将 \"contradicting\" 改为 \"revealing that in catastrophic-failure environments, signal diversity may collapse to a single dominant factor\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. 框架方法论新颖性** [DIVERGENCE: R2 Must-Fix / R1 Should-Fix]\n- R2：Algorithm 1 是 if-else 分类树，DAF 数学上平凡，未连接因果推断文献（Pearl/Rubin）。对 Interpretability and Analysis track，期望更形式化的工具。\n- R1 反驳：Analysis track 的贡献标准是诊断性洞察而非数学框架新颖性。简单方法得出深刻洞察在 probing 文献中常见。DAF 简洁不等于平凡——它将模糊直觉量化为可比较指标。但同意在 Related Work 中应简要讨论与因果推断的关系。\n- **建议**：Related Work 增加一段讨论与 potential outcomes (Rubin 1974) 的关系和区别。\n\n**W2. Router negative result 解释不完整** [AGREE x2]\n- 仅覆盖 single architecture family (Qwen3) + single training paradigm (LoRA) + 2,040 training steps。\n- 未排除替代假设：模型容量不足、数据量不够、更好的训练方法（contrastive learning, different loss functions）可能成功。\n- Oracle margin 仅 2.89 points，进一步降低 negative result 的诊断意义。\n- **建议**：明确标注为 \"preliminary negative result\"；补充讨论替代训练方法。\n\n**W3. ~50-episode pilot 缺乏 power analysis** [AGREE x2]\n- 当前推理仅为 \"ScienceWorld 效应极大（d=3.02）所以小样本可检测\"，但新环境可能有更小效应。\n- **建议**：补充 power analysis，或将 \"suffices\" 弱化为 \"provides preliminary signal\"。\n\n**W4. Cluster bootstrap K=11 正文 caveat 不够** [AGREE x2]\n- K=11 远低于 Cameron et al. (2008) 推荐的 K≥20-30。正文 §3.1 仅简短提及。\n- **建议**：紧跟一句明确 caveat，引导读者主要依赖非聚类 bootstrap CI。\n\n**W5. 11/30 task types 排除 (63%)** [AGREE x2]\n- 7 个 agent-floor tasks（两策略均近零进展）可能代表 death dominance 不成立的 regime，但 Discussion 未讨论此含义。\n- Appendix C/S 的排除验证部分缓解但不消除 selection bias 担忧。\n- **建议**：Discussion 中补充讨论 agent-floor tasks 对 death dominance 的含义。\n\n**W6. 跨环境 probes 深度不足** [AGREE x2]\n- MATH 仅 aggregate-level 无 per-category 分解；ALFWorld 仅一段简短讨论。\n- ALFWorld DAF=0% 实际上暗示不同环境由不同机制驱动——论文 reframe 为 \"环境诊断框架揭示异质机制\" 会比 \"death avoidance 是主导\" 更准确。\n- **建议**：调整 Abstract/Introduction 避免暗示 generalizability。\n\n**W7. 相关工作遗漏** [部分 AGREE]\n- 因果推断基础（Pearl/Rubin potential outcomes）[AGREE x2]\n- Agent safety catastrophic failure avoidance 方向 [R2 建议, R1 部分 AGREE]\n- Credit assignment for LLM agents [R1 REBUT: SALT/CSO 已引用，覆盖面足够]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **DAF vs label fraction 的主次定位**：label fraction 78.9% 是 penalty-invariant 的真正 empirical finding，DAF 88-90% 是 penalty-amplified 的补充指标。论文应调整 framing 权重。\n2. **Framing overclaiming**：Abstract/Introduction 中的 generality claims 超出 ScienceWorld 单一环境的证据支撑。\"Contradicting\" routing literature 是 strawman。\n3. **Cross-model 声明范围**：三个 7-9B 模型的一致性不足以声称 \"cross-model family\" 复制。\n4. **Router negative result 定位**：应为 \"preliminary\" 而非 definitive non-learnability。\n5. **统计 caveats**：K=11 cluster bootstrap、~50-episode pilot 均需更显著的 caveat。\n6. **核心 novelty/excitement 限制**：death dominance 的方向在 oracle vs. hallucinating-LLM 设置下可预期。§5 Non-triviality 论证（72B persistence, Reflexion DAF>100%, inverted-U）关于 persistence 而非 existence。这是 Findings 而非 Conference 水平的核心原因，不可仅通过 writing 修复。\n\n## Reviewer Divergence [REBUT]\n\n1. **R2-N2（框架方法论新颖性是否为 Must-Fix）**：R2 认为 Algorithm 1 + DAF 缺乏技术深度，应连接 Pearl/Rubin 形式化框架。R1 反驳——Analysis track 贡献标准不要求数学框架新颖性，简单方法产出深刻洞察是常见且被接受的模式。R1 同意作为 Should-Fix（在 Related Work 中讨论因果推断关系）。\n   - **Director 判断**：降为 Should-Fix。R1 对 track-specific 贡献标准的论证成立。但论文确实应补充与因果推断文献的连接。\n\n2. **R2-W3（DAF 在 ScienceWorld 外 DAF=0 → metric 无独立价值）**：R1 反驳——DAF=0 在无死亡环境中是正确诊断结果，非指标缺陷。DAF 在其他 catastrophic-failure 环境（自动驾驶仿真、safety-critical RL）可非零。但 R2 的核心关切——论文未论证 DAF 在更广泛场景的价值——仍成立。\n\n3. **R1-W5（分解公式近似误差）**：R2 澄清 episode-level 是 exact partitioning，但 penalty contribution 层面确有近似（忽略死亡前 partial scores）。论文 §2.3 报告残差 0.23（0.8% of Δ_full），近似质量在 P=100 时良好。降为 minor。\n\n---\n\n## Questions\n\n1. §3.3 报告 72B DAF=92.4%——这比 7B 的 90.4% 还高。如果更大模型降低了死亡率但 DAF 反而上升，这是否意味着 death dominance 在更大模型上更极端？请讨论 72B 的 Δ_nd 值及其含义。\n2. 61.2% 的 episodes 是 ties（两策略无差异）。这意味着 routing 最多改善 38.8% 的 episodes。论文是否应在 Discussion 中更显式地讨论 routing 的实际价值上限？\n3. Algorithm 1 对 death-asymmetric episodes 直接赋予 preference label 而不比较 score。在 P < max_possible_partial_score 时此假设是否成立？\n4. 论文 \"counterfactual\" 的使用是 potential outcomes 意义上的（两种 treatment 下的 outcome 比较），还是 Pearl 意义上的结构反事实？请在 Related Work 中明确。\n\n---\n\n## Missing References\n\n- **Pearl (2009)** *Causality: Models, Reasoning, and Inference* — 论文大量使用 \"counterfactual\" 但未引用因果推断基础文献 [R1 R2 均建议]\n- **Rubin (1974)** potential outcomes framework — 论文的纯策略比较本质上是 potential outcomes [R1 R2 均建议]\n- **\"Check Yourself Before You Wreck Yourself\"** (arXiv 2510.16492) — LLM agent catastrophic failure avoidance [R2 建议]\n- **Credit assignment for RL-based LLM agents** (arXiv 2604.09459) [R2 建议, R1 认为 SALT/CSO 已覆盖]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (耗时 ~3.5 分钟)\n**结果**: 0 critical / 3 warnings / 18 infos\n\n**Warnings**:\n1. **Pages 1-2 纯文本**：前 1.5 页无任何 display item，审稿人需阅读大量密集文字才能看到 Figure 1（page 3）。建议将 Figure 1（框架概览图）提前至 page 2。\n2. **Page 5 纯文本**：前后页均有图表但 page 5 整页无 display item。correlation/sensitivity 分析适合用小型 summary table 打破单调。\n3. **Pages 7-8-9 连续文字**：约 2.5 页无视觉刺激。Discussion 可考虑加入 summary figure 或 highlight box。\n\n**其他**：主体正文 8 页共 5 个 display items（3 figures + 2 tables），密度 0.625/页，偏低但对诊断分析型论文尚可。未发现 [?] 未解析引用、LaTeX 渲染错误或 margin 溢出。正文 through Conclusion 在 page 8 结束，Limitations 在 page 9，符合 EMNLP 2026 的 8 页限制。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n论文在 ScienceWorld 环境内的实证分析扎实、统计处理严谨、负面结果如实呈现。主要问题在于：\n\n1. **Novelty/Excitement 不足**（两位 Reviewer Excitement 2.5-3.0）：核心发现（oracle 策略比 hallucinating-LLM 策略更安全）的方向在 ScienceWorld 设置下接近可预期，§5 Non-triviality 论证关于 persistence 而非 existence。这是 Findings 而非 Conference 水平的核心原因，不可仅通过 writing 修复——需要额外环境的深度分析或根本性新发现。\n\n2. **Framing overclaiming**：标题/Abstract 的 generality claims 超出单一环境的证据范围。\"Contradicting routing literature\" 是 strawman。DAF 88-90% 被 penalty 幅度驱动（P=0 时仅 7.4%）。这些通过 reframing 可部分缓解。\n\n3. **Scope 限制**：单一环境（ScienceWorld, 11/30 task types）、同级模型（7-9B）、跨环境 probes 反而证明了 death dominance 不泛化。\n\n**如果作者能够**：(a) 将 framing 从 \"general routing finding\" 调整为 \"diagnostic framework + environment-specific case study\"；(b) 正文正面讨论 penalty sensitivity；(c) 限定 cross-model 声明范围；(d) 补充因果推断文献连接——论文是一篇合格的 Findings 论文。达到 Conference 水准需要在至少一个额外 catastrophic-failure 环境上复现 death dominance。\n\n**评分拆解** (EMNLP 2026 ARR):\n| 维度 | 分数 | 说明 |\n|------|------|------|\n| Soundness | 3.5/5 | 框架在 ScienceWorld 内 sound；DAF penalty-sensitivity + generality claims 超出证据 |\n| Excitement | 2.5/5 | 发现方向可预期；prevalence 量化有价值但不足以达到 Conference excitement |\n| Reproducibility | 4/5 | 算法、配置、prompt 均有详细说明 |\n| Overall | 3.0/5 | Findings — 实证扎实但新颖性有限、scope 受限 |\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"The shared assumption—that routing signal stems from diverse sources and a learned router can exploit it—remains untested\" → 这是 strawman。被引工作在不同 settings 中确实有多样化信号。改为 \"whether this assumption holds in environments with catastrophic failure modes remains untested\"。\n- Contribution (1) \"episode-level counterfactual diagnostic framework\" 的 generality claim 需限定。\n- Contribution (2) 中的 router diagnostic 部分是最有实践价值的发现之一 [R1 R2 共识]，建议提升其 prominence。\n\n### §2 Method\n- §2.3 DAF 定义后应立即注明 DAF 对 P 单调递增，是数学性质而非经验发现。当前措辞 \"DAF increases monotonically with P, a mathematical consequence\" 存在但不够显著。\n- 缺少与 potential outcomes framework 的连接（论文的纯策略比较本质上是 treatment effect 估计）。\n\n### §3 Experiments\n- §3.1: \"150 (61.2%) are ties\" 后的表述可能产生歧义。建议改为 \"150 (61.2%) episodes show no preference; routing is relevant in the remaining 95 (38.8%)\"。\n- §3.2: \"death dominance replicates across model families\" 应限定为 \"within the 7-9B tier\"。三个模型 ~42% 内部死亡率的一致性更可能反映 tier 共性。\n- §3.3: 72B DAF=92.4% 是重要数据点但仅在 Agent Improvement 段出现。建议在 §3.2 讨论或至少交叉引用。\n- §3.4: MATH/ALFWorld probes 深度不足。MATH 缺少 per-category 分解。ALFWorld 的 information asymmetry finding 值得更多讨论——不同环境有不同 dominant mechanism 可能是比 death dominance 更有趣的框架级 contribution。\n- §3.6: \"A Negative Result\" 标题低估了此发现的价值。Router 无法学习 task-type-level signal 有独立的实践意义 [R1 R2 共识]。应标注为 \"preliminary\"。\n\n### §4 Related Work\n- Safe RL 段需扩展：讨论 death avoidance 与 CMDP constraint satisfaction 的对应、为什么 Safe RL 方案不直接适用于 LLM agent routing。\n- 缺少因果推断文献的讨论（Pearl/Rubin）。\n- 考虑补充 agent safety catastrophic failure avoidance 方向文献。\n\n### §5 Discussion\n- \"Non-triviality of death dominance\" 段有效但论证的是 persistence/prevalence 而非 existence 的 surprise。\n- 建议增加一段讨论 penalty sensitivity 的含义（引用 Table 12）。\n- 建议讨论 agent-floor tasks 对 death dominance 不成立的 regime 意味着什么。\n\n### §6 Conclusion\n- 视觉审查确认正文 through Conclusion 在 page 8 结束——但 R1 报告末尾可能有 ~2 行溢出，需核查。\n\n### Appendices\n- 20 个 Appendices (A-T) 质量高，覆盖面广。特别是 Appendix R（Decision Framework）的 3 步流程有实践价值。\n- Algorithm 1 应注明 death-priority 规则的隐含假设（P > max possible partial score）。\n\n### 引用\n- 5 条 not_found + 6 条 mismatch 多为 OpenAlex 索引问题。webb-2023 年份在 R25 已核实正确（CJE vol.56 no.3）。建议再次核查以确保一致。",
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
    "project": "simgate-modular-routing",
    "report": "# 审稿报告：Death Avoidance as the Dominant Routing Signal\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (via ACL Rolling Review) — Interpretability and Analysis track\n**审稿模式**: Fresh review (Round 26)\n**Reviewer 配置**: R1 (方法严谨性+实验设计, 3.5 Borderline Conference) / R2 (新颖性+完整性+相关工作, 3.0 Findings)\n**交叉分享**: 1 轮交叉，关键问题达成高度共识（8 个 AGREE / 2 个 REBUT / 1 个 partial AGREE）\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual diagnostic framework，通过纯策略比较分解 LLM agent routing 信号的构成。在 ScienceWorld（11 task types, 245 episodes）上发现 78.9% 的非 tie routing labels 源于 death asymmetry（内部策略因幻觉触发致命失败，确定性策略存活）。DAF（Death Avoidance Factor）在三个 7-9B 模型家族上达到 88-90%。跨环境 probes（MATH 无信号, ALFWorld 为 information asymmetry）展示了框架的诊断能力但同时表明 death dominance 是环境特定的。Router 训练产出 negative result（step-level balanced accuracy 56-59%）。\n\n---\n\n## Strengths\n\n**S1. 实验设计的系统性和统计严谨性** [AGREE x2]\n跨三个模型家族（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B）的一致性验证、跨三个环境的 probes、多项 ablation（text augmentation, grounding, capacity scaling, Reflexion, retry）。统计处理在 NLP 论文中属上佳水平：episode-level bootstrap (B=10,000)、cluster bootstrap、wild cluster bootstrap、leave-one-task-out sensitivity、Bonferroni correction、penalty sensitivity analysis。\n\n**S2. 诚实的负面结果呈现** [AGREE x2]\nRouter training 低 accuracy（§3.6）、cross-environment probes 否定了 death dominance 的泛化性（§3.4）、text augmentation 无提升（Appendix J）均如实报告。论文在 MATH/ALFWorld 上的 \"boundary probes\" 定位是诚实的。\n\n**S3. 写作质量** [AGREE x2]\n8 页正文 + 20 个 Appendices（A-T）的安排合理。核心 claim 表述清晰，实验 narrative 流畅。Limitations 章节覆盖面好（5 个子段：环境范围、方法论约束、统计限制、pure-strategy upper bound、诊断范围）。\n\n**S4. 可复现性** [AGREE x2]\nAlgorithm 1 伪代码、prompt templates（Appendix T）、router 训练配置（Appendix I）、per-task 分解（Appendix C）均有详细说明。Reproducibility 4/5。\n\n**S5. 框架设计完整性** [R1 强调]\nEpisode-level labeling + DAF decomposition + SCI 三指标形成完整诊断工具链。Algorithm 1 的 edge case 处理（both-dead, both-alive-tied, score-comparison）thorough。Label quality audit（Appendix B）增加数据透明度。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. DAF \"dominance\" 由 penalty 幅度驱动，正文未充分反映 penalty sensitivity** [AGREE x2, critical]\n- Table 12 (Appendix K): P=0 时 DAF=7.4%, P=10 时 DAF=39.8%, P=100 时 DAF=90.1%。DAF=90% 是 reward design 的产物（P=100 在 0-100 score range 内为极端惩罚），而非 routing 信号的内在属性。\n- 78.9% label fraction（不受 penalty 加权影响）是更 robust 的指标，但论文在 Abstract/Introduction 仍以 DAF 88-90% 为 prominent metric。\n- **需要**：(1) 正文 §3.1 或 §5 增加一段正面讨论 Table 12 含义；(2) 以 label fraction 为 primary claim，DAF 降级为补充。\n\n**N2. 跨模型验证仅覆盖 7-9B 同级模型** [AGREE x2, critical]\n- 三个模型参数量和内部死亡率高度相似（~42%），一致性更可能反映 7-9B tier 的共有特征而非跨规模 robustness。\n- §3.3 报告 72B DAF=92.4%（死亡率 30.6% vs det 2.75%），但位于 Agent Improvement 段而非 Cross-Model 段，且未与 7-9B 结果并列讨论。\n- **需要**：(1) 将 \"cross-model family\" 限定为 \"within 7-9B tier\"；(2) 72B 结果明确定位为 scaling analysis。\n\n**N3. \"Contradicting the routing literature's implicit assumption\" 是 strawman framing** [AGREE x2, critical/strong warning]\n- 被引 routing 工作（CogRouter, ARES, MTRouter, RouteLLM, Budget-Aware Routing）操作在 model selection、computational routing、multi-turn routing 等无 catastrophic failure 的 settings。\n- ScienceWorld 的极端 catastrophic failure 使这里发现 death dominance 不构成对这些工作的 \"contradiction\"——论文自己的 ALFWorld 结果恰好支持了其他 settings 可能有多样化信号。\n- R1 认为严重程度介于 Must-Fix 和 Should-Fix——本质是 wording 问题，可通过修改几句话解决。\n- **需要**：将 \"contradicting\" 改为 \"revealing that in catastrophic-failure environments, signal diversity may collapse to a single dominant factor\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. 框架方法论新颖性** [DIVERGENCE: R2 Must-Fix / R1 Should-Fix]\n- R2：Algorithm 1 是 if-else 分类树，DAF 数学上平凡，未连接因果推断文献（Pearl/Rubin）。对 Interpretability and Analysis track，期望更形式化的工具。\n- R1 反驳：Analysis track 的贡献标准是诊断性洞察而非数学框架新颖性。简单方法得出深刻洞察在 probing 文献中常见。DAF 简洁不等于平凡——它将模糊直觉量化为可比较指标。但同意在 Related Work 中应简要讨论与因果推断的关系。\n- **建议**：Related Work 增加一段讨论与 potential outcomes (Rubin 1974) 的关系和区别。\n\n**W2. Router negative result 解释不完整** [AGREE x2]\n- 仅覆盖 single architecture family (Qwen3) + single training paradigm (LoRA) + 2,040 training steps。\n- 未排除替代假设：模型容量不足、数据量不够、更好的训练方法（contrastive learning, different loss functions）可能成功。\n- Oracle margin 仅 2.89 points，进一步降低 negative result 的诊断意义。\n- **建议**：明确标注为 \"preliminary negative result\"；补充讨论替代训练方法。\n\n**W3. ~50-episode pilot 缺乏 power analysis** [AGREE x2]\n- 当前推理仅为 \"ScienceWorld 效应极大（d=3.02）所以小样本可检测\"，但新环境可能有更小效应。\n- **建议**：补充 power analysis，或将 \"suffices\" 弱化为 \"provides preliminary signal\"。\n\n**W4. Cluster bootstrap K=11 正文 caveat 不够** [AGREE x2]\n- K=11 远低于 Cameron et al. (2008) 推荐的 K≥20-30。正文 §3.1 仅简短提及。\n- **建议**：紧跟一句明确 caveat，引导读者主要依赖非聚类 bootstrap CI。\n\n**W5. 11/30 task types 排除 (63%)** [AGREE x2]\n- 7 个 agent-floor tasks（两策略均近零进展）可能代表 death dominance 不成立的 regime，但 Discussion 未讨论此含义。\n- Appendix C/S 的排除验证部分缓解但不消除 selection bias 担忧。\n- **建议**：Discussion 中补充讨论 agent-floor tasks 对 death dominance 的含义。\n\n**W6. 跨环境 probes 深度不足** [AGREE x2]\n- MATH 仅 aggregate-level 无 per-category 分解；ALFWorld 仅一段简短讨论。\n- ALFWorld DAF=0% 实际上暗示不同环境由不同机制驱动——论文 reframe 为 \"环境诊断框架揭示异质机制\" 会比 \"death avoidance 是主导\" 更准确。\n- **建议**：调整 Abstract/Introduction 避免暗示 generalizability。\n\n**W7. 相关工作遗漏** [部分 AGREE]\n- 因果推断基础（Pearl/Rubin potential outcomes）[AGREE x2]\n- Agent safety catastrophic failure avoidance 方向 [R2 建议, R1 部分 AGREE]\n- Credit assignment for LLM agents [R1 REBUT: SALT/CSO 已引用，覆盖面足够]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **DAF vs label fraction 的主次定位**：label fraction 78.9% 是 penalty-invariant 的真正 empirical finding，DAF 88-90% 是 penalty-amplified 的补充指标。论文应调整 framing 权重。\n2. **Framing overclaiming**：Abstract/Introduction 中的 generality claims 超出 ScienceWorld 单一环境的证据支撑。\"Contradicting\" routing literature 是 strawman。\n3. **Cross-model 声明范围**：三个 7-9B 模型的一致性不足以声称 \"cross-model family\" 复制。\n4. **Router negative result 定位**：应为 \"preliminary\" 而非 definitive non-learnability。\n5. **统计 caveats**：K=11 cluster bootstrap、~50-episode pilot 均需更显著的 caveat。\n6. **核心 novelty/excitement 限制**：death dominance 的方向在 oracle vs. hallucinating-LLM 设置下可预期。§5 Non-triviality 论证（72B persistence, Reflexion DAF>100%, inverted-U）关于 persistence 而非 existence。这是 Findings 而非 Conference 水平的核心原因，不可仅通过 writing 修复。\n\n## Reviewer Divergence [REBUT]\n\n1. **R2-N2（框架方法论新颖性是否为 Must-Fix）**：R2 认为 Algorithm 1 + DAF 缺乏技术深度，应连接 Pearl/Rubin 形式化框架。R1 反驳——Analysis track 贡献标准不要求数学框架新颖性，简单方法产出深刻洞察是常见且被接受的模式。R1 同意作为 Should-Fix（在 Related Work 中讨论因果推断关系）。\n   - **Director 判断**：降为 Should-Fix。R1 对 track-specific 贡献标准的论证成立。但论文确实应补充与因果推断文献的连接。\n\n2. **R2-W3（DAF 在 ScienceWorld 外 DAF=0 → metric 无独立价值）**：R1 反驳——DAF=0 在无死亡环境中是正确诊断结果，非指标缺陷。DAF 在其他 catastrophic-failure 环境（自动驾驶仿真、safety-critical RL）可非零。但 R2 的核心关切——论文未论证 DAF 在更广泛场景的价值——仍成立。\n\n3. **R1-W5（分解公式近似误差）**：R2 澄清 episode-level 是 exact partitioning，但 penalty contribution 层面确有近似（忽略死亡前 partial scores）。论文 §2.3 报告残差 0.23（0.8% of Δ_full），近似质量在 P=100 时良好。降为 minor。\n\n---\n\n## Questions\n\n1. §3.3 报告 72B DAF=92.4%——这比 7B 的 90.4% 还高。如果更大模型降低了死亡率但 DAF 反而上升，这是否意味着 death dominance 在更大模型上更极端？请讨论 72B 的 Δ_nd 值及其含义。\n2. 61.2% 的 episodes 是 ties（两策略无差异）。这意味着 routing 最多改善 38.8% 的 episodes。论文是否应在 Discussion 中更显式地讨论 routing 的实际价值上限？\n3. Algorithm 1 对 death-asymmetric episodes 直接赋予 preference label 而不比较 score。在 P < max_possible_partial_score 时此假设是否成立？\n4. 论文 \"counterfactual\" 的使用是 potential outcomes 意义上的（两种 treatment 下的 outcome 比较），还是 Pearl 意义上的结构反事实？请在 Related Work 中明确。\n\n---\n\n## Missing References\n\n- **Pearl (2009)** *Causality: Models, Reasoning, and Inference* — 论文大量使用 \"counterfactual\" 但未引用因果推断基础文献 [R1 R2 均建议]\n- **Rubin (1974)** potential outcomes framework — 论文的纯策略比较本质上是 potential outcomes [R1 R2 均建议]\n- **\"Check Yourself Before You Wreck Yourself\"** (arXiv 2510.16492) — LLM agent catastrophic failure avoidance [R2 建议]\n- **Credit assignment for RL-based LLM agents** (arXiv 2604.09459) [R2 建议, R1 认为 SALT/CSO 已覆盖]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (耗时 ~3.5 分钟)\n**结果**: 0 critical / 3 warnings / 18 infos\n\n**Warnings**:\n1. **Pages 1-2 纯文本**：前 1.5 页无任何 display item，审稿人需阅读大量密集文字才能看到 Figure 1（page 3）。建议将 Figure 1（框架概览图）提前至 page 2。\n2. **Page 5 纯文本**：前后页均有图表但 page 5 整页无 display item。correlation/sensitivity 分析适合用小型 summary table 打破单调。\n3. **Pages 7-8-9 连续文字**：约 2.5 页无视觉刺激。Discussion 可考虑加入 summary figure 或 highlight box。\n\n**其他**：主体正文 8 页共 5 个 display items（3 figures + 2 tables），密度 0.625/页，偏低但对诊断分析型论文尚可。未发现 [?] 未解析引用、LaTeX 渲染错误或 margin 溢出。正文 through Conclusion 在 page 8 结束，Limitations 在 page 9，符合 EMNLP 2026 的 8 页限制。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n论文在 ScienceWorld 环境内的实证分析扎实、统计处理严谨、负面结果如实呈现。主要问题在于：\n\n1. **Novelty/Excitement 不足**（两位 Reviewer Excitement 2.5-3.0）：核心发现（oracle 策略比 hallucinating-LLM 策略更安全）的方向在 ScienceWorld 设置下接近可预期，§5 Non-triviality 论证关于 persistence 而非 existence。这是 Findings 而非 Conference 水平的核心原因，不可仅通过 writing 修复——需要额外环境的深度分析或根本性新发现。\n\n2. **Framing overclaiming**：标题/Abstract 的 generality claims 超出单一环境的证据范围。\"Contradicting routing literature\" 是 strawman。DAF 88-90% 被 penalty 幅度驱动（P=0 时仅 7.4%）。这些通过 reframing 可部分缓解。\n\n3. **Scope 限制**：单一环境（ScienceWorld, 11/30 task types）、同级模型（7-9B）、跨环境 probes 反而证明了 death dominance 不泛化。\n\n**如果作者能够**：(a) 将 framing 从 \"general routing finding\" 调整为 \"diagnostic framework + environment-specific case study\"；(b) 正文正面讨论 penalty sensitivity；(c) 限定 cross-model 声明范围；(d) 补充因果推断文献连接——论文是一篇合格的 Findings 论文。达到 Conference 水准需要在至少一个额外 catastrophic-failure 环境上复现 death dominance。\n\n**评分拆解** (EMNLP 2026 ARR):\n| 维度 | 分数 | 说明 |\n|------|------|------|\n| Soundness | 3.5/5 | 框架在 ScienceWorld 内 sound；DAF penalty-sensitivity + generality claims 超出证据 |\n| Excitement | 2.5/5 | 发现方向可预期；prevalence 量化有价值但不足以达到 Conference excitement |\n| Reproducibility | 4/5 | 算法、配置、prompt 均有详细说明 |\n| Overall | 3.0/5 | Findings — 实证扎实但新颖性有限、scope 受限 |\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"The shared assumption—that routing signal stems from diverse sources and a learned router can exploit it—remains untested\" → 这是 strawman。被引工作在不同 settings 中确实有多样化信号。改为 \"whether this assumption holds in environments with catastrophic failure modes remains untested\"。\n- Contribution (1) \"episode-level counterfactual diagnostic framework\" 的 generality claim 需限定。\n- Contribution (2) 中的 router diagnostic 部分是最有实践价值的发现之一 [R1 R2 共识]，建议提升其 prominence。\n\n### §2 Method\n- §2.3 DAF 定义后应立即注明 DAF 对 P 单调递增，是数学性质而非经验发现。当前措辞 \"DAF increases monotonically with P, a mathematical consequence\" 存在但不够显著。\n- 缺少与 potential outcomes framework 的连接（论文的纯策略比较本质上是 treatment effect 估计）。\n\n### §3 Experiments\n- §3.1: \"150 (61.2%) are ties\" 后的表述可能产生歧义。建议改为 \"150 (61.2%) episodes show no preference; routing is relevant in the remaining 95 (38.8%)\"。\n- §3.2: \"death dominance replicates across model families\" 应限定为 \"within the 7-9B tier\"。三个模型 ~42% 内部死亡率的一致性更可能反映 tier 共性。\n- §3.3: 72B DAF=92.4% 是重要数据点但仅在 Agent Improvement 段出现。建议在 §3.2 讨论或至少交叉引用。\n- §3.4: MATH/ALFWorld probes 深度不足。MATH 缺少 per-category 分解。ALFWorld 的 information asymmetry finding 值得更多讨论——不同环境有不同 dominant mechanism 可能是比 death dominance 更有趣的框架级 contribution。\n- §3.6: \"A Negative Result\" 标题低估了此发现的价值。Router 无法学习 task-type-level signal 有独立的实践意义 [R1 R2 共识]。应标注为 \"preliminary\"。\n\n### §4 Related Work\n- Safe RL 段需扩展：讨论 death avoidance 与 CMDP constraint satisfaction 的对应、为什么 Safe RL 方案不直接适用于 LLM agent routing。\n- 缺少因果推断文献的讨论（Pearl/Rubin）。\n- 考虑补充 agent safety catastrophic failure avoidance 方向文献。\n\n### §5 Discussion\n- \"Non-triviality of death dominance\" 段有效但论证的是 persistence/prevalence 而非 existence 的 surprise。\n- 建议增加一段讨论 penalty sensitivity 的含义（引用 Table 12）。\n- 建议讨论 agent-floor tasks 对 death dominance 不成立的 regime 意味着什么。\n\n### §6 Conclusion\n- 视觉审查确认正文 through Conclusion 在 page 8 结束——但 R1 报告末尾可能有 ~2 行溢出，需核查。\n\n### Appendices\n- 20 个 Appendices (A-T) 质量高，覆盖面广。特别是 Appendix R（Decision Framework）的 3 步流程有实践价值。\n- Algorithm 1 应注明 death-priority 规则的隐含假设（P > max possible partial score）。\n\n### 引用\n- 5 条 not_found + 6 条 mismatch 多为 OpenAlex 索引问题。webb-2023 年份在 R25 已核实正确（CJE vol.56 no.3）。建议再次核查以确保一致。",
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

_source line 2191 · 2026-05-21T22:28:30.263571+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4065
}
```

</details>

---


### Tool call

_source line 2192 · 2026-05-21T22:28:45.417183+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉回应已收集'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题已达成共识，一轮即收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递至 Research Director'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉回应已收集'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题已达成共识，一轮即收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递至 Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 2193 · 2026-05-21T22:28:45.468040+00:00_

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


### Assistant

_source line 2194 · 2026-05-21T22:29:09.713870+00:00_

审稿圆桌会议完成，报告已投递至 Research Director。

**最终评分：3.0 (Findings)**

核心结论：
- **3 个 Must-Fix**：DAF penalty sensitivity 未正面讨论、cross-model 仅 7-9B 同级、"contradicting routing literature" 是 strawman
- **7 个 Should-Fix**：框架新颖性（降级自 R2 Must-Fix）、router negative result 解释不完整、~50-episode pilot 缺 power analysis、cluster bootstrap caveat、task selection bias、cross-env probes 深度、相关工作遗漏
- **1 个 Divergence**：R2 认为框架方法论新颖性是 Must-Fix，R1 反驳（Analysis track 不要求数学框架新颖性）→ Director 判断降为 Should-Fix
- **Findings 而非 Conference 的核心原因**：novelty/excitement 不足（death dominance 方向可预期），不可仅通过 writing 修复——需额外 catastrophic-failure 环境的深度验证

Issue tracker 已同步更新至 `review_issues.yaml`（Round 26）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 180

## Round 180

2 recorded events


### User

_source line 2195 · 2026-05-21T22:29:12.234759+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

对 R2 的 8 条意见逐条回应：
- **3 条完全同意**（N3 framing strawman、W1 router training、W2 model scale）
- **2 条部分同意**（N1 framing overclaiming——同意 framing 需调整但反驳"循环论证"；W5 related work——同意加 Pearl/Rubin 但其他遗漏需具体论文）
- **1 条同意**（W4 pilot claim 需 power analysis）
- **2 条反驳**（N2 方法论新颖性——Analysis track 贡献标准不要求数学复杂性；W3 DAF 独立价值——DAF 在 catastrophic-failure 环境中通用）

R1 与 R2 的核心分歧在 N2（方法论新颖性），这导致 0.5 分的评分差异（R1: 3.5 vs R2: 3.0）。

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

_source line 2196 · 2026-05-21T22:29:25.114379+00:00_

审稿报告已投递至 Research Director，圆桌审稿流程完成。

**最终评分：3.0 (Findings)**

核心结论：
- **3 个 Must-Fix**：DAF penalty sensitivity 正文讨论不足、cross-model 声明范围过宽（仅 7-9B）、"contradicting routing literature" 是 strawman
- **7 个 Should-Fix**：框架与因果推断文献连接、router negative result 标注为 preliminary、~50-episode pilot power analysis、cluster bootstrap K=11 caveat、task selection bias 讨论、cross-environment probes 深度、相关工作补充
- **评分瓶颈**：novelty/excitement 不足（death dominance 方向可预期），不可仅通过 writing 修复——达到 Conference 需额外 catastrophic-failure 环境的深度验证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 181

## Round 181

50 recorded events


### User

_source line 2197 · 2026-05-22T04:37:27.530485+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Interpretability and Analysis
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

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

_source line 2198 · 2026-05-22T04:37:33.352182+00:00_

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

_source line 2199 · 2026-05-22T04:37:33.405422+00:00_

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
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 2200 · 2026-05-22T04:37:42.433889+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2201 · 2026-05-22T04:37:42.434366+00:00_



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

_source line 2202 · 2026-05-22T04:37:47.505686+00:00_

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


### Tool call

_source line 2203 · 2026-05-22T04:37:47.807269+00:00_

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

_source line 2204 · 2026-05-22T04:37:47.958372+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

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


### Tool result

_source line 2205 · 2026-05-22T04:37:47.958861+00:00_



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

_source line 2206 · 2026-05-22T04:37:51.071733+00:00_

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

_source line 2207 · 2026-05-22T04:37:51.072180+00:00_

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

_source line 2208 · 2026-05-22T04:37:51.825304+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
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
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 2209 · 2026-05-22T04:37:53.331511+00:00_

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

_source line 2210 · 2026-05-22T04:37:53.382307+00:00_

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
…[truncated 5884 chars]

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


### Tool result

_source line 2211 · 2026-05-22T04:37:58.653681+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines with ARR:

## Main Conference Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using exi
…[truncated 1029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6828
}
```

</details>

---


### Tool call

_source line 2212 · 2026-05-22T04:38:04.125423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "80",
  "limit": "50"
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
    "offset": "80",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2213 · 2026-05-22T04:38:04.879448+00:00_

80	\hyperref[app:decision-framework]{R.~Decision Framework} $\cdot$
81	\hyperref[app:extended-validation]{S.~Extended Validation} $\cdot$
82	\hyperref[app:prompt-templates]{T.~Agent Prompt Templates}
83	
84	\section{Signal Concentration Index}
85	\label{app:sci}
86	
87	Let $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:
88	\begin{equation}
89	    c_k = \frac{n_k \cdot \delta_k}{\sum_{j=1}^{K} n_j \cdot \delta_j}
90	\end{equation}
91	where $n_k$ is the number of episodes and $\delta_k = d_k^{\tt int} - d_k^{\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\{c_1, \ldots, c_K\}$:
92	\begin{equation}
93	    \text{SCI} = \frac{\sum_{i=1}^K \sum_{j=1}^K |c_i - c_j|}{2K \sum_{k=1}^K c_k}
94	\end{equation}
95	
96	\section{Labeling Quality Audit}
97	\label{app:labeling}
98	
99	\begin{algorithm}[t]
100	\caption{Episode-Level Counterfactual Labeling}
101	\label{alg:labeling}
102	\begin{algorithmic}[1]
103	\REQUIRE Task instance $t$, computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$
104	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
105	\FOR{each $m \in \mathcal{M}$}
106	    \STATE Run episode $\tau_m$ with pure-strategy $m$
107	    \STATE Record score $s_m$ and death indicator $d_m$
108	\ENDFOR
109	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
110	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
111	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
112	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
113	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
114	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
115	\ELSIF{$s_{\tt det} > s_{\tt int}$}
116	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{score comparison}
117	\ELSIF{$s_{\tt int} > s_{\tt det}$}
118	  
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 2214 · 2026-05-22T04:38:04.930167+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR May 2026 submission deadline page limit format requirements"
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
    "query": "EMNLP 2026 ARR May 2026 submission deadline page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 2215 · 2026-05-22T04:38:06.437352+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_27/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_27/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2216 · 2026-05-22T04:38:06.891124+00:00_

-rw-r--r-- 1 ubuntu ubuntu 595387 May 22 04:37 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_27/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2217 · 2026-05-22T04:38:06.941815+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "report.md",
  "max_chars": "2000"
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
    "file": "report.md",
    "max_chars": "2000"
  }
}
```

</details>

---


### Tool result

_source line 2218 · 2026-05-22T04:38:10.841528+00:00_

Web search results for query: "EMNLP 2026 ARR May 2026 submission deadline page limit format requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here is the information about EMNLP 2026 ARR May 2026 submission:

## Submission Deadline
The ARR Submission Deadline is May 25, 2026.

## Page Limits
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Format Requirements
Official EMNLP 2026 LaTeX
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5911
}
```

</details>

---


### Tool result

_source line 2219 · 2026-05-22T04:38:10.842195+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\\n- **gemma-scienceworld-v5** (success): Gemma-2-9B-it replicates the death-avoidance dominance pattern observed in Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming that high DAF is model-agnostic rather than an artifact of a specific backbone architecture\\n  [Gemma-2-9B ScienceWorld Analysis Results](/api/workspace-files/projects/simgate-modular-routing/artifacts/gemma-scienceworld-v5/data/
…[truncated 356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3900
}
```

</details>

---


### Tool call

_source line 2220 · 2026-05-22T04:38:30.317737+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 2221 · 2026-05-22T04:38:31.171945+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 2222 · 2026-05-22T04:38:31.373110+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | head -80",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2223 · 2026-05-22T04:38:31.674376+00:00_

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

_source line 2224 · 2026-05-22T04:38:31.925398+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
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
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 2225 · 2026-05-22T04:38:31.975924+00:00_

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
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_report
…[truncated 608 chars]

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

_source line 2226 · 2026-05-22T04:38:38.116274+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2227 · 2026-05-22T04:38:38.166970+00:00_

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

_source line 2228 · 2026-05-22T04:38:41.876053+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 3 -name \"*.yaml\" -path \"*/config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 2 -name \"config.*\" 2>/dev/null",
  "description": "Search for config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 3 -name \"*.yaml\" -path \"*/config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 2 -name \"config.*\" 2>/dev/null",
    "description": "Search for config files"
  }
}
```

</details>

---


### Tool result

_source line 2229 · 2026-05-22T04:38:41.927209+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/pending_approval_notifications.yaml

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

_source line 2230 · 2026-05-22T04:38:44.738571+00:00_

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

_source line 2231 · 2026-05-22T04:38:44.789240+00:00_

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
13	  check_references: false
14	  operational_chat_id: oc_6551c2d0ac89db1b3b9e56f77fcf912d
15	  review_mode: fresh
16	  review_paper_path: projects/simgate-modular-routing/docs/paper/main.tex
17	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_27/submitted.pdf
18	  review_round: 27
19	  review_supplementary_paths: ''
20	  submission_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c
21	project:
22	  created_at: '2026-05-13T04:23:23.832Z'
23	  description: 'SimGate: Learning When to Route LLM Agents to Deterministic Computation
24	    via Explicit Modular Gating'
25	  name: simgate-modular-routing
26	  phase: research
27	  source_idea_id: idea_010
28	venue: emnlp-2026
29	

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

_source line 2232 · 2026-05-22T04:38:52.268630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/emnlp-2026.yaml"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2233 · 2026-05-22T04:38:52.269173+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing:
18	  - created_at: '2026-05-21T06:49:14Z'
19	    id: 2468a8
20	    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
21	  - created_at: '2026-05-21T17:05:54Z'
22	    id: 0b1d8f
23	    text: ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
24	

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

_source line 2234 · 2026-05-22T04:38:59.059551+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
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
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2235 · 2026-05-22T04:38:59.110171+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex

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

_source line 2236 · 2026-05-22T04:39:02.022154+00:00_

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

_source line 2237 · 2026-05-22T04:39:02.223559+00:00_

1	\begin{abstract}
2	LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs.\ deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9\% of non-tie routing labels arise from death asymmetry: the internal strategy triggers catastrophic failure while the deterministic strategy survives. This label fraction is penalty-independent. A derived score-weighted measure, the Death Avoidance Factor, reaches 88--90\% across three 7--9B model families (Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B), confirming convergence on a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), illustrating the framework's applicability. A ${\sim}$50-episode diagnostic pilot provides preliminary signal for identifying the dominant routing mechanism given a large effect size ($d = 3.02$); environments with smaller effects may require larger samples, enabling informed build-vs-buy decisions before expensive router training.
3	\end{abstract}
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

_source line 2238 · 2026-05-22T04:39:02.224092+00:00_

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

_source line 2239 · 2026-05-22T04:39:02.275272+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \citep{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone, as the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated), while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \citep{toolformer-2023} inserts API calls by perplexity reduction; ART \citep{art-2023} decomposes tasks into tool-augmented programs; Chameleon \citep{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \citep{cogrouter-2026,ares-2026}, model tiers \citep{mtrouter-2026}, or episode-level model selection under sparse rewards \citep{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. These approaches, which operate in non-catastrophic settings, share the assumption that routing signal stems from diverse sources and a learned router can exploit it---an assumption that remains untested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under 
…[truncated 2659 chars]

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

_source line 2240 · 2026-05-22T04:39:40.338848+00:00_

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

_source line 2241 · 2026-05-22T04:39:55.301945+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 14963
}
```

</details>

---


### Tool call

_source line 2242 · 2026-05-22T04:39:55.503250+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## 论文信息\n- 标题：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- LaTeX 源码：projects/simgate-modular-routing/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_27/submitted.pdf\n- 投稿类别：Interpretability and Analysis\n\n## Venue 要求（EMNLP 2026，经 web 搜索确认）\n- 通过 ARR May 2026 cycle 提交，deadline 2026-05-25\n- Long paper 正文限 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- ACL 模板，double-blind 审稿\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **Counterfactual framework 方法论**：pure-strategy 对比是否有效？episode-level labeling 的设计是否合理？有无方法论缺陷？\n2. **DAF 指标设计**：score-weighted decomposition 是否 sound？penalty-independent (label fraction) 和 penalty-dependent (DAF) 两个指标的关系是否清晰？有无统计陷阱？\n3. **统计严谨性**：bootstrap CIs、cluster bootstrap (K=11) 的可靠性；sample size (245 episodes, 11 task types) 是否充分；wild cluster bootstrap 的使用是否恰当\n4. **Labeling 质量**：episode-level labels 用于 step-level prediction 的 granularity mismatch 是否被充分讨论？oracle circularity 风险？\n5. **Cross-model/cross-environment 实验**：3 个 model families (Qwen/Llama/Gemma) 的 replication 是否充分？MATH 和 ALFWorld 的 boundary probes 设计是否合理？\n6. **Router 训练与诊断**：exploratory router 的实验设计和结论是否站得住？LoRA fine-tuning 的设置是否合理？\n7. **Intervention axes**：retry/Reflexion/10x scaling/action-space restriction 四个干预的设计和结论是否可靠？\n\n请输出完整的结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → 评分建议（按 EMNLP 2026 标准）。对 Weaknesses 要严格、具体、有证据支持。"
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
    "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## 论文信息\n- 标题：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- LaTeX 源码：projects/simgate-modular-routing/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_27/submitted.pdf\n- 投稿类别：Interpretability and Analysis\n\n## Venue 要求（EMNLP 2026，经 web 搜索确认）\n- 通过 ARR May 2026 cycle 提交，deadline 2026-05-25\n- Long paper 正文限 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- ACL 模板，double-blind 审稿\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **Counterfactual framework 方法论**：pure-strategy 对比是否有效？episode-level labeling 的设计是否合理？有无方法论缺陷？\n2. **DAF 指标设计**：score-weighted decomposition 是否 sound？penalty-independent (label fraction) 和 penalty-dependent (DAF) 两个指标的关系是否清晰？有无统计陷阱？\n3. **统计严谨性**：bootstrap CIs、cluster bootstrap (K=11) 的可靠性；sample size (245 episodes, 11 task types) 是否充分；wild cluster bootstrap 的使用是否恰当\n4. **Labeling 质量**：episode-level labels 用于 step-level prediction 的 granularity mismatch 是否被充分讨论？oracle circularity 风险？\n5. **Cross-model/cross-environment 实验**：3 个 model families (Qwen/Llama/Gemma) 的 replication 是否充分？MATH 和 ALFWorld 的 boundary probes 设计是否合理？\n6. **Router 训练与诊断**：exploratory router 的实验设计和结论是否站得住？LoRA fine-tuning 的设置是否合理？\n7. **Intervention axes**：retry/Reflexion/10x scaling/action-space restriction 四个干预的设计和结论是否可靠？\n\n请输出完整的结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → 评分建议（按 EMNLP 2026 标准）。对 Weaknesses 要严格、具体、有证据支持。"
  }
}
```

</details>

---


### Tool result

_source line 2243 · 2026-05-22T04:40:07.776240+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12272
}
```

</details>

---


### Tool call

_source line 2244 · 2026-05-22T04:40:08.035171+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "你是 Reviewer 2，负责审查**新颖性、完整性和写作质量**。\n\n## 论文信息\n- 标题：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- LaTeX 源码：projects/simgate-modular-routing/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_27/submitted.pdf\n- 投稿类别：Interpretability and Analysis\n\n## Venue 要求（EMNLP 2026，经 web 搜索确认）\n- 通过 ARR May 2026 cycle 提交，deadline 2026-05-25\n- Long paper 正文限 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- ACL 模板，double-blind 审稿\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **Contribution 新颖性**：\"先诊断再建 router\" 的 framing 在现有文献中是否真正新颖？counterfactual diagnostic framework 相比已有的 tool-use/routing 分析方法有何本质区别？\n2. **Related work 覆盖**：是否遗漏了重要的相关工作？特别是：(a) agent routing/tool selection 领域, (b) counterfactual reasoning in RL/NLP, (c) catastrophic failure analysis, (d) modular computation/routing 领域近期工作\n3. **Claims 与 Evidence 匹配**：论文声称框架具有跨环境/跨模型通用性——证据是否支撑这一声明？\"diagnostic rather than prescriptive\" 的定位是否准确？\n4. **写作质量**：论文结构是否清晰？核心 message 是否容易理解？术语使用是否一致？是否有冗余或不必要的复杂表述？\n5. **Generalization claims**：只用 ScienceWorld (11/30 task types) + 两个 boundary probes (MATH, ALFWorld)，generalization 声明是否 overclaimed？\n6. **格式合规**：正文是否在 8 页限制内？匿名规则是否遵守？Limitations 和 Ethics 是否完整？Appendix 是否过度？\n7. **叙事连贯性**：从 Introduction 的 motivation 到 Conclusion 的 takeaway，论文的 story arc 是否连贯？读者是否容易跟上论证逻辑？\n\n请输出完整的结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → 评分建议（按 EMNLP 2026 标准）。对 Weaknesses 要严格、具体、有证据支持。"
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
    "text": "你是 Reviewer 2，负责审查**新颖性、完整性和写作质量**。\n\n## 论文信息\n- 标题：Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- LaTeX 源码：projects/simgate-modular-routing/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_27/submitted.pdf\n- 投稿类别：Interpretability and Analysis\n\n## Venue 要求（EMNLP 2026，经 web 搜索确认）\n- 通过 ARR May 2026 cycle 提交，deadline 2026-05-25\n- Long paper 正文限 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- ACL 模板，double-blind 审稿\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **Contribution 新颖性**：\"先诊断再建 router\" 的 framing 在现有文献中是否真正新颖？counterfactual diagnostic framework 相比已有的 tool-use/routing 分析方法有何本质区别？\n2. **Related work 覆盖**：是否遗漏了重要的相关工作？特别是：(a) agent routing/tool selection 领域, (b) counterfactual reasoning in RL/NLP, (c) catastrophic failure analysis, (d) modular computation/routing 领域近期工作\n3. **Claims 与 Evidence 匹配**：论文声称框架具有跨环境/跨模型通用性——证据是否支撑这一声明？\"diagnostic rather than prescriptive\" 的定位是否准确？\n4. **写作质量**：论文结构是否清晰？核心 message 是否容易理解？术语使用是否一致？是否有冗余或不必要的复杂表述？\n5. **Generalization claims**：只用 ScienceWorld (11/30 task types) + 两个 boundary probes (MATH, ALFWorld)，generalization 声明是否 overclaimed？\n6. **格式合规**：正文是否在 8 页限制内？匿名规则是否遵守？Limitations 和 Ethics 是否完整？Appendix 是否过度？\n7. **叙事连贯性**：从 Introduction 的 motivation 到 Conclusion 的 takeaway，论文的 story arc 是否连贯？读者是否容易跟上论证逻辑？\n\n请输出完整的结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → 评分建议（按 EMNLP 2026 标准）。对 Weaknesses 要严格、具体、有证据支持。"
  }
}
```

</details>

---


### Tool result

_source line 2245 · 2026-05-22T04:40:09.705617+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1670
}
```

</details>

---


### Assistant

_source line 2246 · 2026-05-22T04:40:21.806399+00:00_

已全部派发：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已启动 |
| Reviewer 2（新颖性/完整性） | ✅ 已启动 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿 | ⏭️ 未配置，跳过 |

等待两位 Reviewer 返回初审意见后进入 Step 2 交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 182

## Round 182

2 recorded events


### User

_source line 2247 · 2026-05-22T04:45:33.418281+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性与实验设计

## Summary

本文提出一个 episode-level counterfactual diagnostic framework，用于在构建 router 之前诊断 LLM agent routing signal 的机制来源。框架在 ScienceWorld 上发现 78.9% 的 non-tie routing labels 来源于 death asymmetry（internal strategy 触发灾难性失败而 deterministic strategy 存活），DAF = 90.4%。跨模型（Qwen/Llama/Gemma 7-9B）、跨环境（MATH/ALFWorld）验证支持框架的 applicability。一个 exploratory router 训练实验表明 step-level routing signal 不存在，router 仅能学到 task-type classification。

论文自我批评意识极强（Limitations 涵盖面广、mathematical artifacts 主动标记），附录极为详尽（20 个 appendix sections）。但核心发现的 novelty 和 generalizability 存在实质性问题。

---

## 总体评分

**Overall**: 3.0（Findings）

**一句话总结**: 方法论框架清晰、实验执行扎实，但核心发现部分受制于 penalty structure 的数学必然性，且几乎完全依赖单一环境（ScienceWorld），generalizability 不足以支撑 main conference 接收。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体 sound，统计分析有明确 caveats；但 DAF 的数学 tautology、K=11 cluster bootstrap 的 anti-conservative 问题、以及 "deterministic = oracle" 的 confound 削弱了部分 claims 的支撑力度 |
| Excitement | 2.5/5 | 发现在 retrospect 中有一定预见性（oracle access 自然防止 death）；实际 actionable insight 有限（"在灾难性惩罚环境中用 oracle"）；框架本身相对 straightforward |
| Reproducibility | 4/5 | 实验设置、超参、prompt templates 详尽记录；代码和数据承诺 acceptance 后释放；vLLM 版本、GPU 配置均已报告 |
| Overall Assessment | 3.0/5 | Findings 水平：贡献真实但范围较窄，适合作为 methodological note 而非 full research contribution |
| Confidence | 4/5 | 仔细阅读全文和所有 appendix，熟悉相关 counterfactual evaluation 和 agent routing 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DAF 的核心发现部分是 penalty structure 的数学必然，而非纯经验发现

- 具体位置：Section 2.4, Eq. 4-5; Abstract ("DAF reaches 90.4%"); Table in Appendix K
- 问题：DAF = δP/(δP + Δ_nd) 随 P 单调递增，这是一个数学恒等式。在 P=100 时 DAF=90.4%，但在 P=10 时 DAF 仅 50.4%，P=5 时仅 35.4%（Appendix K, Table）。论文虽在 Section 2.4 承认"a mathematical consequence rather than an empirical finding"，但 abstract、title framing、以及全文叙事仍将 DAF=90.4% 作为核心 empirical result 突出展示。这造成了 framing 与实际 contribution 的不匹配。真正 penalty-independent 的经验发现是 label fraction (78.9%) 和 death rate differential (+26.5 pp)，DAF 数字在很大程度上是 P 值选择的产物。
- 为什么影响接收：如果 reviewer 或读者将 DAF=90.4% 理解为纯经验发现，会高估论文的 contribution。对于 Interpretability and Analysis track，framing 的准确性尤为重要。
- 建议修改方向：(1) Abstract 中应同等突出 penalty-independent label fraction (78.9%)，并明确标注 DAF 随 P 变化的特性；(2) 考虑将 label fraction 而非 DAF 作为标题级 claim 的核心指标；(3) 在 Section 3.1 首段即交代 DAF 的 mathematical dependence on P，而非等到 Section 2.4 末尾。

**N2** [critical] "Deterministic" strategy 实为 oracle access，混淆了 routing signal 分析的解释

- 具体位置：Section 2.1 (footnote 2); Section 2.2; Appendix T (prompt templates)
- 问题：ScienceWorld 中的 "deterministic" strategy 通过 simulator forking 获得 ground-truth environment state（Appendix T: "candidates are then evaluated via simulator forking"）。这本质上是一个 **oracle**——拥有完美信息的策略。internal strategy 依赖 LLM 自生成 observations（会积累 hallucination error），而 deterministic strategy 直接获取真实状态。在这种极端信息不对称下，"oracle access prevents death more often than hallucination-prone reasoning" 几乎是 trivially expected。论文将此框定为 "routing signal decomposition"，但实际更接近 "oracle vs. non-oracle comparison"。footnote 2 承认了跨环境的操作化差异，但未充分讨论这对核心 claim 的解释力影响。
- 为什么影响接收：这是论文最核心的实验设计。如果 "deterministic" 的信息优势本身就足以解释 death asymmetry，那么 decomposition framework 诊断出的 "death avoidance as dominant signal" 可能只是在重述信息不对称的直接后果，而非揭示 routing 机制的深层结构。
- 建议修改方向：(1) 明确讨论 oracle access confound：内部策略的 higher death rate 在多大程度上可归因于 hallucination accumulation vs. 其他因素？(2) 设计一个 intermediate 对照条件（如 partial oracle access、或 noisy deterministic），以分离信息优势对 death rate 的边际贡献；(3) 在 Discussion 中明确讨论：如果一个 realistic (non-oracle) deterministic strategy 的 death rate 更高，DAF 会如何变化？

**N3** [critical] 环境覆盖范围过窄，generalizability 声明缺乏充分支撑

- 具体位置：Section 3 opening; Section 3.4; Limitations paragraph 1
- 问题：核心定量分析仅基于 ScienceWorld 的 11/30 task types（37%），即便加上 n=5 prescreening 的 19 个 excluded types，仍局限于单一环境。MATH 和 ALFWorld 被正确定位为 "boundary probes" 而非 cross-domain validation，但它们提供的是 **null results**（MATH: no signal; ALFWorld: information asymmetry, DAF=0%），不构成对 death avoidance dominance 的正面验证。Limitations 中声称 "the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical"，但论文标题和 abstract 的 framing 更像是在提出一个 general empirical finding。
- 为什么影响接收：一个主要在单一 text-based simulation 环境上验证的 diagnostic framework，在 EMNLP 审稿标准下需要更强的 generalization evidence 以支撑 Conference-level acceptance。Findings 接收则需要至少第二个具有灾难性惩罚的环境作为正面验证。
- 建议修改方向：(1) 在至少一个其他具有 catastrophic failure 的环境（如 WebArena、NetHack、BabyAI with traps）上运行完整 framework 验证；(2) 或者将论文重新定位为 purely ScienceWorld-specific analysis，相应调整标题和 claims 的 scope。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cluster bootstrap (K=11) 的统计推断 reliability 不足

- 具体位置：Section 3.1 "Sensitivity and seed robustness"; Appendix E (Table)
- 问题：论文正确指出 K=11 远低于 Cameron et al. (2008) 和 Webb (2023) 推荐的 K≥20-30 threshold，并将 cluster bootstrap 降级为 sensitivity check。但 primary inference 使用的 non-clustered episode-level bootstrap 假设 245 episodes 独立，这在 task types 共享环境动态的情况下是 anti-conservative 的。论文处于 statistical dilemma：clustered method 样本不足(K=11)，unclustered method 违反独立性假设。Appendix E 承认 "narrower CIs obtained reflect known small-sample bias toward underestimation of variance, not tighter inference"——这实际上意味着 primary CI [81.1%, 99.0%] 可能过窄。
- 建议：(1) 更明确地在主文 (而非仅 appendix) 标注 primary CI 的 anti-conservative nature；(2) 考虑报告 clustered CI [73.3%, 100.0%] 作为 conservative bound alongside primary CI。

**W2** [warning] Excluded task types (63%) 的 prescreening 样本量极小 (n=5)

- 具体位置：Appendix C, Table 2 (excluded tasks); Section 3 opening
- 问题：19 个 excluded task types 中 Group B 和 C 均基于 n=5 prescreening episodes，论文在 Table 2 caption 中承认 "should be interpreted as directional evidence rather than precise rate estimates"。但这些 n=5 estimates 被用于支撑 anti-cherry-picking argument（"mean ΔDR = +38.2 pp exceeding included tasks"），以及 extended validation (Appendix S) 仅覆盖 5/19 excluded tasks (n=20 each)。在 n=5 时，一个 40% vs 20% 的 death rate difference 的 95% CI 跨越零，无法达到统计显著性。
- 建议：扩大 extended validation 覆盖范围，或对 anti-cherry-picking claim 的 confidence 做更保守的表述。

**W3** [warning] Router 训练的 negative result 在给定 label distribution 下是 expected 的，诊断价值有限

- 具体位置：Section 3.6; Appendix I-J
- 问题：245 episodes 中仅 9 个 (3.7%) 是 internal-preferred，86 个 (35.1%) 是 det-preferred，150 个 (61.2%) 是 no-preference。在 95 个 non-tie labels 中，90.5% 偏向 deterministic。在如此极端的 class imbalance 下，任何 router 都会退化为 always-deterministic。论文将 router 失败解释为 "routing signal is task-type-level"，但更简洁的解释是：当 majority class 占 90.5% 且 minority class 仅有 9 个样本时，任何分类器都学不到 meaningful signal。Text augmentation ablation (25%-800%) 无效进一步支持这一点——paraphrase 不能制造 genuine minority-class diversity。论文在 Appendix J 末尾确认了这一解释（"the issue is minority-class diversity"），但 main text 的 framing 给读者的印象是 "routing is inherently unlearnable"，而非 "data is insufficient for the minority class"。
- 建议：在 Section 3.6 主文中更明确区分两种解释：(A) routing signal genuinely doesn't exist at step level; (B) data scarcity for the minority class makes learning impossible with current sample size。当前的 framing 过度偏向 (A)。

**W4** [warning] r=0.97 correlation 作为"证据"展示但实际是数学必然

- 具体位置：Section 3.1 "Per-task correlation structure"; Figure 2
- 问题：论文在 Section 3.1 和 Figure 2 caption 中均承认 r→1 as DAF→1 是 "structural consequence of death dominance, not an independent finding"。然而 Figure 2 在正文第 4 页 prominent 展示，给读者的初始印象仍是一个 empirical finding。既然论文自己将其定性为 "internal consistency check" 而非独立发现，建议降低其展示优先级或将其移入 appendix。
- 建议：将 Figure 2 移入 appendix（已有 Appendix D 做 correlation robustness），在主文中简要提及即可。

**W5** [warning] Episode-level labels 用于 step-level prediction 的 granularity mismatch 讨论不充分

- 具体位置：Section 2.5 "Scope of episode-level analysis"; Limitations paragraph 2
- 问题：论文报告 0.3% directional conflict，60.3% pre-event neutral，这表明绝大多数 steps 的 episode label 是 uninformative 的（正确方向但无区分信号）。Limitations 中提到 "projecting episode-level labels onto 10-50 sequential steps with path-dependent state introduces compounding error: early routing decisions alter the state trajectory, potentially invalidating later labels derived from the episode outcome"。这是一个 fundamental concern，因为 counterfactual framework 假设 fixed strategy throughout the episode，但 real deployment 中的 mixed-strategy routing 会改变 trajectory，使得 episode-level labels 不再适用。论文在 Limitations 中提到但未在 Method 或 Discussion 中充分讨论这个 distribution shift 问题。
- 建议：在 Section 5 Discussion 中专门讨论 pure-strategy → mixed-strategy distribution shift 对 framework 实用性的影响。

---

## 小问题（不影响接收）

- Section 2.2: "We use Qwen2.5-7B-Instruct (vLLM) on ScienceWorld" 中 vLLM 应标注版本（正文未标注，Appendix I 标注了 v0.21.0），建议在首次出现时即标注。
- Table 1: "Death%" 列中 Reflexion (3×) 的 N=220 与 baseline N=245 不同，difference 未解释（可能因 find-non-living-thing 排除，但不明确）。
- Figure 3 (dose-response): 72B scaling baseline (30.6%) 是 all 11 tasks 的数据，但 retry/reflexion 曲线是 10 death-prone tasks only——不同 denominator 的 horizontal lines 与曲线在同一图中可能 misleading。
- Appendix N: failure mode taxonomy 基于 single annotator，论文已标注 "no inter-annotator agreement was computed"，但鉴于 taxonomy 支持 Section 5 的 mechanistic explanation，建议增加至少一个 second annotator 或报告 annotation guidelines。
- Ethics Statement: "200 GPU-hours" 的 breakdown 很好；但 "code and data will be released upon acceptance" 在 double-blind review 期间无法验证。

---

## 主要优势

1. **方法论清晰性**：Episode-level counterfactual framework 的 motivation（per-step oracle degeneracy at 97.4% tie rate）convincing 且 well-grounded。Framework 的三个组件（labeling, DAF, SCI）各司其职，设计合理。

2. **极为突出的自我批评意识**：论文在几乎每一个潜在 weakness 上都主动标注了 caveat（DAF 的数学依赖性、correlation 的 tautological nature、cluster bootstrap 的 reliability、excluded tasks 的 cherry-picking risk）。这在 NLP 论文中罕见且值得肯定。20 个 appendix sections 提供了极为全面的 robustness checks。

3. **Cross-model convergence**：三个架构不同的模型家族（Qwen/Llama/Gemma 7-9B）在 DAF 88-90% 上的 convergence（spread 仅 2.2 pp）是 genuine empirical finding，表明 death vulnerability 是 task-environment property 而非 model-specific artifact。

4. **Intervention analysis 的系统性**：四个干预轴（retry、Reflexion、10× scaling、action-space restriction）的 dose-response analysis 设计合理，Reflexion ceiling 的发现有独立价值。Grounding ablation（Appendix O）提供了 causal evidence for the specific failure mechanism（focus on 误用）。

5. **Cross-environment probes 的 framework 验证**：MATH (no signal) 和 ALFWorld (information asymmetry, DAF=0%) 正确 demonstrate 了 framework 在不同 routing mechanism 下的 diagnostic 能力，而非仅在 ScienceWorld 上 confirm death dominance。

---

## 评分总结

| 维度 | 分数 |
|------|------|
| Overall Assessment | 3.0 (Findings) |
| Soundness | 3.5/5 |
| Excitement | 2.5/5 |
| Reproducibility | 4/5 |
| Confidence | 4/5 |

核心判断：论文提出了一个 sound 的 diagnostic framework 并在 ScienceWorld 上做了 thorough 的分析。但核心定量发现 (DAF=90.4%) 部分受制于 penalty structure 的数学性质，"deterministic = oracle access" 的 confound 未被充分分离，且 generalizability 证据不足以超越 single-environment study 的范畴。适合 Findings 接收，但距离 Conference 接收需要至少一个额外 catastrophic-failure environment 的 full validation，以及对 oracle confound 的更深入分析。


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

_source line 2248 · 2026-05-22T04:45:43.045674+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 183

## Round 183

2 recorded events


### User

_source line 2249 · 2026-05-22T04:45:59.666285+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论：Overall 3.0 (Findings)**

核心判断：

- **3 个 Must-Fix 问题**：(1) DAF=90.4% 部分是 P=100 penalty 的数学必然而非纯经验发现，但 abstract/title framing 过度突出；(2) "deterministic" strategy 实为 oracle access，信息不对称本身就足以解释 death asymmetry，未充分分离 confound；(3) 核心分析仅覆盖 ScienceWorld 一个环境的 37% task types，MATH/ALFWorld 仅提供 null results，generalizability 不足。

- **5 个 Should-Fix 问题**：K=11 cluster bootstrap 的 statistical reliability、excluded tasks 的 n=5 prescreening 样本量、router negative result 在极端 class imbalance 下的 expected nature、r=0.97 correlation 的 tautological 展示、以及 episode-level → step-level 的 distribution shift 讨论不充分。

- **主要优势**：框架清晰、cross-model convergence 是 genuine finding (DAF 88-90%, 2.2pp spread)、自我批评意识在 NLP 论文中罕见地出色、20 个 appendix 的 robustness 极为全面。

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

_source line 2250 · 2026-05-22T04:46:04.826245+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 184

## Round 184

6 recorded events


### User

_source line 2251 · 2026-05-22T04:47:46.384671+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿意见：新颖性、完整性与写作质量

### 论文信息
- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
- **投稿类别**: Interpretability and Analysis
- **Venue**: EMNLP 2026 (via ARR May 2026)

---

## 总体评分
**Overall Assessment**: 3.0 (Findings)
**一句话总结**: 方法论上稳健的诊断框架揭示了一个实用且非显然的发现（death avoidance 主导 routing signal），但单一主环境、概念简单的方法、以及本质上的 negative result 限制了 excitement；正文疑似超出 8 页限制。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论严谨，统计处理充分（bootstrap CI、cluster-robust tests、LOO sensitivity），但 generalization claims 超出证据支撑范围 |
| Excitement | 2.5/5 | 发现本身有实用价值（"先诊断再建 router"），但方法概念简单（episode-level A/B 测试），主要贡献是特定环境下的 empirical observation，且 actionability 有限 |
| Reproducibility | 4/5 | 详细报告了超参数（Table in App I）、prompt templates（App T）、统计方法、所有 random seeds；承诺 acceptance 后释放代码 |
| Confidence | 4/5 | 熟悉 LLM agent routing、counterfactual analysis、interactive environments 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文疑似超出 8 页限制
- 具体位置：PDF 第 8–9 页
- 问题：Section 5 (Discussion) 占据了第 8 页的大部分空间，Section 6 (Conclusion) 出现在第 9 页顶部。按照 EMNLP 2026 规则，正文（Abstract 至 Conclusion）限 8 页，Limitations 和 Ethics 不计入。Conclusion 即使仅占第 9 页约 5–6 行，正文仍超出 8 页。
- 为什么影响接收：硬性格式要求。ARR desk reject 政策可能直接拒稿。
- 建议修改方向：压缩 Discussion（当前三段可合并为两段）或 Related Work（当前 6 个 paragraph 可精简），将 Conclusion 收入第 8 页内。

**N2** [critical] Generalization claims 超出证据支撑
- 具体位置：Abstract ("illustrating the framework's applicability"), §1 contributions (3) ("cross-model convergence... confirm the framework's diagnostic utility"), §6 Conclusion ("Cross-environment probes illustrate applicability")
- 问题：论文声称框架具有跨环境通用性，但实际证据极为有限：
  - **主环境**：ScienceWorld 1 个环境，11/30 task types（63% 被排除）
  - **MATH probe**：无 routing signal（$73.5\%$ vs $73.0\%$, $p=0.81$），实际上无法验证框架的诊断能力——无信号环境下任何框架都会得出"无信号"结论
  - **ALFWorld probe**：诊断出 information asymmetry 而非 death avoidance，这确实展示了框架的鉴别力，但仅此一例
  - 跨模型验证（3 个 7–9B 模型）在同一环境内进行，不等同于跨环境验证
- 为什么影响接收：作为 Interpretability and Analysis 投稿，方法的通用性是核心价值主张。当前证据仅支持"在 ScienceWorld 上有效 + ALFWorld 上能区分不同机制"，不足以支撑 Abstract 和 Conclusion 中的通用性措辞。
- 建议修改方向：(a) 将 "illustrate applicability" 改为 "provide preliminary evidence"；(b) 明确区分"方法论通用性"（任何可以跑 paired episodes 的环境都能用）和"发现通用性"（death dominance 是否在其他 catastrophic-failure 环境中也成立——未验证）；(c) 增加至少一个具有 catastrophic failure 但非 ScienceWorld 的环境（如 NetHack、Crafter）来验证 death dominance 发现本身的可迁移性。

**N3** [critical] "Deterministic" 策略的不可比性未被充分讨论
- 具体位置：§2.1 脚注（三种环境中 deterministic 含义不同），§3.4（跨环境对比）
- 问题：三个环境中 "deterministic computation" 的操作化截然不同：ScienceWorld = oracle simulator（ground-truth state access），MATH = code interpreter，ALFWorld = admissible-action enumeration。这些不是同一概念的不同实例，而是质性不同的信息优势。论文在脚注中承认了这一点，但仍在跨环境对比中将它们并列为"deterministic"并计算 DAF，且 cross-environment summary table (App M, Table in §3.4) 将三者放在同一框架下比较。
- 为什么影响接收：这削弱了框架的 conceptual unity。如果"deterministic"在每个环境中意味着不同的东西，那么 DAF = 0% (ALFWorld) vs DAF = 90.4% (ScienceWorld) 的对比不是在测量同一维度上的差异，而是在比较不同的概念。
- 建议修改方向：(a) 将 "deterministic" 替换为更准确的术语（如 "privileged-information strategy"），或在每个环境中使用不同术语；(b) 在 §2.1 正文（而非仅脚注）中充分讨论这一概念差异；(c) 明确跨环境对比的 scope——框架的通用性在于诊断流程，不在于 "deterministic" 是一个统一概念。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] DAF 指标被 penalty 机械驱动，但论文以 DAF 为主打
- 具体位置：Abstract ("Death Avoidance Factor, reaches 88–90%"), §2.4 方程 (5), §3.1
- 问题：DAF = $\delta P / (\delta P + \Delta_{\text{nd}})$ 随 $P$ 单调递增——论文自己承认这是"数学后果而非实证发现"（§2.4）。在 $P=10$ 时 DAF 仅 50.4%（App K Table），$P=0$ 时 DAF=7.4%。然而 Abstract 和全文主打 DAF=90.4%（$P=100$），label fraction (78.9%) 虽被提及但处于次要位置。
- 建议：将 penalty-independent 的 label fraction (78.9%) 作为 Abstract 和 Conclusion 的首要数字，DAF 作为补充。当前 Abstract 先提 78.9%（好的），但随后重点强调 DAF 88–90%，可能误导读者认为 90% 是一个环境无关的稳健数字。

**W2** [warning] Oracle simulator 的非现实性未被充分讨论
- 具体位置：§2.1, §2.2
- 问题：ScienceWorld 中 deterministic 策略使用 oracle simulator（fork 环境、逐步获取 ground-truth state）。这在实际部署中不可用——真实环境没有可以 fork 的 simulator。论文将此定位为"诊断工具"而非"部署方案"，但读者可能会误解 "always-deterministic is trivially near-optimal" 的实际含义。
- 建议：在 §2.1 或 Discussion 中明确一段讨论：oracle simulator 是诊断用的 counterfactual baseline，不是部署方案；实际部署中的 "safe routing" 需要不同的机制（如 action filtering、safety classifiers）。App O 的 grounding ablation（action-space filtering 将 death rate 降至 29%）是一个更实际的方向，应在正文中更突出。

**W3** [warning] Appendix 过度膨胀（20 个 section，约 13 页）
- 具体位置：Appendix A–T（PDF 第 11–23 页）
- 问题：13 页 appendix 对 8 页正文的比例 (1.6:1) 显著高于常规。部分 appendix 内容（如 Algorithm 1 labeling procedure、failure mode taxonomy）对理解论文核心贡献至关重要，应在正文中呈现。同时部分 appendix（如 App T prompt templates 占约 2 页）可能过于冗长。
- 建议：(a) 将 Algorithm 1 移入正文 §2.3；(b) 将 failure mode analysis (App N) 的核心发现（100% deaths from `focus on` misuse）提升至正文 Discussion；(c) 精简 prompt templates 至关键差异。

**W4** [warning] Actionability 有限——"诊断而非处方"的定位限制了贡献的 impact
- 具体位置：§5 Discussion "Practical implications", Limitations "Diagnostic scope"
- 问题：论文诊断出 death avoidance 主导 routing signal，但对"然后怎么办"的回答仅限于：(a) 50-episode pilot decision framework（App R），阈值 (75%, 50%) 承认是 "illustrative, derived from ScienceWorld's specific reward structure"；(b) "deterministic routing matches or exceeds learned alternatives"（但 deterministic = oracle simulator，不可部署）；(c) grounding ablation（App O）作为初步干预，但仅在 appendix。
- 建议：在 Discussion 中增加一段关于可操作后续步骤的讨论——如 action-space safety filtering（已有 App O 数据）、step-level death prediction（而非 full routing）、curriculum training on death-prone tasks 等。

**W5** [warning] Router 训练的 negative result 基于有限的架构探索
- 具体位置：§3.6, App I, App P
- 问题：Router 仅探索了 LoRA-tuned Qwen3（0.6B/1.7B/4B）+ SFT implicit routing。论文声称 "routing bottleneck is signal-limited, not architecture-limited"（App P），但测试的架构空间很窄：同一 model family 的三个 scale + 一个 generative router。未测试：contrastive learning、reward models、retrieval-augmented routing、multi-task routing、graph neural networks on trajectory features 等。
- 建议：(a) 软化 "signal-limited not architecture-limited" 的措辞，改为 "under the current architecture family and data regime"；(b) 至少讨论 alternative approaches 的可能性，即使不实验。

---

## 小问题（不影响接收）

1. **Abstract 信息密度过高**：Abstract 试图涵盖 DAF、label fraction、3 个模型、cross-environment probes、50-episode pilot，导致一个段落内塞入过多数字。建议聚焦核心发现，将模型数量和 pilot 细节留给 Introduction。

2. **§2.4 DAF 推导中的 $\bar{s}_{\text{surv}}$ 近似**：$\bar{s}_{\text{surv}} = 0.87$（$P$ 的 0.9%）使得 $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ 的残差仅 0.23（0.8%），在 ScienceWorld 中成立。但应注明这一近似在 $\bar{s}_{\text{surv}}$ 较大的环境中会失效。

3. **Figure 2 散点图**（§3.1）：$r = 0.97$ 的解释应更 prominent 地标注为"数学后果"而非"实证发现"——当前在图 caption 中提到了，但正文 §3.1 "Per-task correlation structure" 段落仍以 $r = 0.97$ 开头，容易给读者留下独立发现的印象。

4. **Limitations 过于冗长**：5 个段落覆盖 environmental scope、methodological constraints、statistical limitations、pure-strategy upper bound、diagnostic scope。这种面面俱到的风格虽然诚实，但读起来像是在 pre-empt 所有可能的批评。建议精简至 3 个核心 limitation。

5. **Terminology inconsistency**：§1 使用 "catastrophic failure"，§2 使用 "death"，§3 交替使用两者。建议统一为一个术语。

6. **引用格式**：多处 2026 年引用（cogrouter-2026, ares-2026 等）疑似 arXiv preprints，应确认这些是否已正式发表或仅为 concurrent submissions。

7. **§2.4 引用 Ng et al. (1999)**：用于支持"policy 不受 $P$ 影响"的论点，但 Ng et al. (1999) 讨论的是 reward shaping 对 optimal policy 的影响，不完全对应这里"agent 的 observation 中不包含 $P$"的论证逻辑。

---

## 主要优势

1. **"先诊断再建 router" 的方法论贡献**：在 routing 文献中，这是一个被忽视但重要的视角。大多数工作直接优化 routing policy，而本文追问"routing signal 的来源是什么"，这对社区有指导价值。

2. **统计严谨性出色**：Bootstrap CI、cluster-robust tests、LOO sensitivity、wild cluster bootstrap、Cohen's $d$、exact permutation test——统计处理远超同类工作平均水平。论文对自身统计局限性的讨论（$K=11$ clusters 低于推荐的 $K \geq 20$）也很诚实。

3. **跨模型一致性**：三个架构不同的 7–9B 模型（Qwen2.5-7B、Llama-3.1-8B、Gemma-2-9B-it）在 DAF 88–90% 上收敛（spread 仅 2.2 pp），加上 72B 的 scaling 验证，有力说明 death dominance 是环境属性而非模型属性。

4. **Anti-cherry-picking 意识强**：详细报告了 task exclusion 理由（App C Table），并证明排除的 19 个 tasks 的 death asymmetry ($\Delta$DR = +38.2 pp) 强于纳入的 11 个 tasks (+28.7 pp)——排除偏向的反方向。Extended validation（App S）进一步验证。

5. **Penalty-independent label fraction 的设计**：认识到 DAF 受 $P$ 影响后，提出 78.9% label fraction 作为 penalty-invariant 指标，展示了方法论上的自觉。

6. **Negative result 的坦诚报告**：Router training 的失败（episode-level balanced accuracy 47.1%，低于 chance）被完整报告而非隐藏，包含详细的 ablation（text augmentation、capacity scaling、death-proximal labeling），这种透明度值得肯定。

---

## 对 Director 指定审查维度的逐项回应

### 1. Contribution 新颖性
**中等偏上**。"先诊断再建 router" 在 routing 文献中确实新颖——现有工作（Toolformer、CogRouter、RouteLLM 等）均直接优化 routing，无人做过系统的 routing signal 来源分析。但方法本身（run pure strategies → compare episode outcomes → decompose gap）是 episode-level A/B testing 的直接应用，概念上并不复杂。Counterfactual diagnostic framework 与已有的 counterfactual evaluation in RL（Olson et al. 2021; Gajcin et al. 2023）的本质区别在于粒度（episode-level vs action-level）和目标（diagnose routing signal vs explain individual decisions），这一区别论文已阐述清楚（§4 Related Work）。

### 2. Related work 覆盖
**整体良好，有几个缺口**：
- **(a) Agent routing/tool selection**: 覆盖充分（Toolformer、ART、Chameleon、CogRouter、ARES、MTRouter、RouteLLM、budget-aware routing 均已引用）
- **(b) Counterfactual reasoning in RL/NLP**: 基本覆盖（Olson、Gajcin、Amitai + 近期 LLM agent extensions），但缺少 NLP 领域的 counterfactual data augmentation 工作（如 Kaushik et al., 2020）
- **(c) Catastrophic failure analysis**: 引用了 ruan2024failures、SafeRoute、Agent-SafetyBench，基本覆盖
- **(d) Modular computation/routing**: 缺少与 Mixture-of-Experts routing（Switch Transformer、GShard 等）和 Neural Module Networks（Andreas et al., 2016）的联系讨论——这些是 "routing" 的重要上下文
- **额外缺口**: 缺少 process supervision vs outcome supervision 的联系（与 step-level vs episode-level labeling 直接相关），以及 reward shaping 文献的更深入讨论

### 3. Claims 与 Evidence 匹配
**主要问题见 N2 和 N3**。补充：
- "框架具有通用性" → 仅在 3 个环境中测试，且 MATH 本质上是 null result
- "death dominance persists across model scales" → 72B 验证仅限 Qwen 一个 family，且 72B 仍有 30.6% death rate
- "~50-episode pilot classifies environment" → retrospective validation on 4 conditions (Table in App R)，全部来自本文数据，无 prospective validation
- "diagnostic rather than prescriptive" → 定位准确但限制了贡献的 impact

### 4. 写作质量
**良好，但有改进空间**。结构清晰（Method → Experiments → Related Work → Discussion 的顺序合理），术语使用基本一致，核心 message 容易理解。主要问题：(a) 数字密度过高（尤其 §3.1, §3.2），段落中嵌入大量百分比和 CI 影响可读性；(b) 部分内容在正文和 Limitations 中重复；(c) Related Work 放在 Experiments 之后是合理选择（先展示结果再定位），但 Discussion 和 Conclusion 过短（Discussion 约半页，Conclusion 仅 3 句话），与前面的详尽实验形成反差。

### 5. Generalization claims
**Overclaimed**。详见 N2。核心论点：(a) 11/30 ScienceWorld task types 不足以代表 "interactive environments"；(b) MATH 的 null result 不验证框架能力；(c) ALFWorld 是唯一真正展示框架鉴别力的跨环境证据；(d) "the diagnostic procedure applies to any environment with asymmetric fatal outcomes" 是一个 methodological claim 而非 empirical claim，但 Abstract 和 Conclusion 的措辞模糊了这一区分。

### 6. 格式合规
- **正文页数**：疑似超出 8 页限制（Conclusion 在第 9 页开头），详见 N1
- **匿名**：正确（`\author{Anonymous}`，`\hypersetup{pdfauthor={}}`, "Anonymous ACL submission" header）
- **Limitations**：完整且详尽（5 段），覆盖 environmental scope、methodological constraints、statistical limitations、pure-strategy upper bound、diagnostic scope
- **Ethics Statement**：完整，报告了 GPU 资源用量（~200 GPU-hours）、数据来源、开源许可
- **Appendix**：20 个 section（A–T），约 13 页，比例偏高但无硬性限制

### 7. 叙事连贯性
**较强**。Story arc：routing 是重要问题 → 现有方法直接建 router 但不理解 signal 来源 → 我们提出诊断框架 → 发现 death avoidance 主导 → 这一发现 robust across models/interventions → 实际意义：先诊断再决定是否建 router。逻辑清晰，读者容易跟上。唯一断裂点：§3.6 Router Training 的 negative result 在 narrative 中的定位稍显突兀——它既是框架预测的验证（death-dominated signal 下 router 应该失败），又是一个独立的 negative finding。建议在 §3.6 开头更明确地连接："我们的诊断预测 router 应该失败，因为..."

---

## 总结

这是一篇方法论严谨、发现有实用价值的分析性工作。"先诊断再建 router" 的 framing 在 routing 文献中是一个有价值的贡献，78.9% death-dominated label fraction 的发现对社区有指导意义。但 (1) 正文疑似超页限，(2) generalization claims 与 evidence 不匹配（1 个主环境 + 2 个 boundary probes），(3) "deterministic" 概念在跨环境对比中的不可比性，以及 (4) 作为 negative result 的有限 actionability，使得当前版本更适合 Findings 而非 Main Conference。修复 N1（格式）、N2（措辞）和 N3（概念澄清）后，可达到 Findings 的稳固水平。


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

_source line 2252 · 2026-05-22T04:48:22.780579+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见（完整原文）\n\n### 总体评分\nOverall Assessment: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 正文疑似超出 8 页限制\n- Section 5 (Discussion) 占据第 8 页大部分空间，Section 6 (Conclusion) 出现在第 9 页顶部。按 EMNLP 2026 规则正文限 8 页，可能触发 desk reject。\n\n**N2** [critical] Generalization claims 超出证据支撑\n- 主环境仅 ScienceWorld (11/30 task types)，MATH 是 null result（无法验证框架能力），ALFWorld 是唯一展示框架鉴别力的跨环境证据。Abstract 和 Conclusion 中的通用性措辞超出实际证据。\n\n**N3** [critical] \"Deterministic\" 策略在三个环境中含义不同（ScienceWorld=oracle simulator, MATH=code interpreter, ALFWorld=admissible-action enumeration），跨环境对比的概念统一性受损。\n\n### Should-Fix 问题\n\n**W1** DAF 指标被 penalty 机械驱动但以 DAF 为主打——P=10 时仅 50.4%，应将 penalty-independent 的 label fraction (78.9%) 作为首要数字。\n\n**W2** Oracle simulator 的非现实性未充分讨论——diagnostic baseline vs deployment 的区别需更明确。\n\n**W3** Appendix 过度膨胀（20 sections, ~13 页 vs 正文 8 页），部分核心内容（Algorithm 1, failure mode analysis）应在正文呈现。\n\n**W4** Actionability 有限——\"诊断而非处方\"的定位限制了贡献 impact，Discussion 中缺少可操作后续步骤的讨论。\n\n**W5** Router 训练 negative result 基于有限架构探索（仅 LoRA-tuned Qwen3 三个 scale），\"signal-limited not architecture-limited\" 的结论过强。\n\n### 小问题\n1. Abstract 信息密度过高\n2. §2.4 DAF 推导中 $\\bar{s}_{\\text{surv}}$ 近似在其他环境可能失效\n3. Figure 2 的 r=0.97 应更 prominent 标注为数学后果\n4. Limitations 过于冗长（5 段），建议精简至 3 个核心 limitation\n5. 术语不一致：catastrophic failure vs death\n6. 2026 年引用可能是 arXiv preprints\n7. §2.4 引用 Ng et al. (1999) 的适用性存疑\n\n### 主要优势\n1. \"先诊断再建 router\" 的方法论贡献\n2. 统计严谨性出色\n3. 跨模型一致性（DAF 88-90%, spread 2.2pp）\n4. Anti-cherry-picking 意识强\n5. Penalty-independent label fraction 的方法论自觉\n6. Negative result 的坦诚报告\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条回应 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见（完整原文）\n\n### 总体评分\nOverall Assessment: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 正文疑似超出 8 页限制\n- Section 5 (Discussion) 占据第 8 页大部分空间，Section 6 (Conclusion) 出现在第 9 页顶部。按 EMNLP 2026 规则正文限 8 页，可能触发 desk reject。\n\n**N2** [critical] Generalization claims 超出证据支撑\n- 主环境仅 ScienceWorld (11/30 task types)，MATH 是 null result（无法验证框架能力），ALFWorld 是唯一展示框架鉴别力的跨环境证据。Abstract 和 Conclusion 中的通用性措辞超出实际证据。\n\n**N3** [critical] \"Deterministic\" 策略在三个环境中含义不同（ScienceWorld=oracle simulator, MATH=code interpreter, ALFWorld=admissible-action enumeration），跨环境对比的概念统一性受损。\n\n### Should-Fix 问题\n\n**W1** DAF 指标被 penalty 机械驱动但以 DAF 为主打——P=10 时仅 50.4%，应将 penalty-independent 的 label fraction (78.9%) 作为首要数字。\n\n**W2** Oracle simulator 的非现实性未充分讨论——diagnostic baseline vs deployment 的区别需更明确。\n\n**W3** Appendix 过度膨胀（20 sections, ~13 页 vs 正文 8 页），部分核心内容（Algorithm 1, failure mode analysis）应在正文呈现。\n\n**W4** Actionability 有限——\"诊断而非处方\"的定位限制了贡献 impact，Discussion 中缺少可操作后续步骤的讨论。\n\n**W5** Router 训练 negative result 基于有限架构探索（仅 LoRA-tuned Qwen3 三个 scale），\"signal-limited not architecture-limited\" 的结论过强。\n\n### 小问题\n1. Abstract 信息密度过高\n2. §2.4 DAF 推导中 $\\bar{s}_{\\text{surv}}$ 近似在其他环境可能失效\n3. Figure 2 的 r=0.97 应更 prominent 标注为数学后果\n4. Limitations 过于冗长（5 段），建议精简至 3 个核心 limitation\n5. 术语不一致：catastrophic failure vs death\n6. 2026 年引用可能是 arXiv preprints\n7. §2.4 引用 Ng et al. (1999) 的适用性存疑\n\n### 主要优势\n1. \"先诊断再建 router\" 的方法论贡献\n2. 统计严谨性出色\n3. 跨模型一致性（DAF 88-90%, spread 2.2pp）\n4. Anti-cherry-picking 意识强\n5. Penalty-independent label fraction 的方法论自觉\n6. Negative result 的坦诚报告\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2253 · 2026-05-22T04:48:50.394567+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27613
}
```

</details>

---


### Tool call

_source line 2254 · 2026-05-22T04:48:50.596386+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见（完整原文）\n\n### 总体评分\nOverall Assessment: 3.0 (Findings)\nSoundness: 3.5/5 | Excitement: 2.5/5 | Reproducibility: 4/5 | Confidence: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 的核心发现部分是 penalty structure 的数学必然\n- DAF = δP/(δP + Δ_nd) 随 P 单调递增。P=100 时 DAF=90.4%，P=10 时仅 50.4%，P=5 时 35.4%（Appendix K）。论文在 §2.4 承认是\"数学后果\"，但 abstract/title framing 仍将 DAF=90.4% 作为核心 empirical result 突出。真正 penalty-independent 的是 label fraction (78.9%) 和 death rate differential (+26.5 pp)。\n\n**N2** [critical] \"Deterministic\" strategy 实为 oracle access，混淆了 routing signal 分析\n- ScienceWorld 中 deterministic 通过 simulator forking 获取 ground-truth state（Appendix T），本质是 oracle。在极端信息不对称下 \"oracle prevents death more often\" 几乎是 trivially expected。未设计 intermediate 对照条件分离信息优势的边际贡献。\n\n**N3** [critical] 环境覆盖过窄，generalizability 声明缺乏充分支撑\n- 核心分析仅 ScienceWorld 11/30 tasks (37%)。MATH 和 ALFWorld 提供 null results，不构成对 death dominance 的正面验证。标题和 abstract 的 framing 更像 general empirical finding，但 Limitations 将通用性声明限制为 methodological。\n\n### Should-Fix 问题\n\n**W1** Cluster bootstrap (K=11) 统计推断 reliability 不足——primary CI [81.1%, 99.0%] 可能过窄，K=11 远低于推荐的 K≥20-30。\n\n**W2** Excluded task types (63%) 的 n=5 prescreening 样本量极小，anti-cherry-picking claim 的 confidence 不足。\n\n**W3** Router negative result 在极端 class imbalance (90.5% majority) 下是 expected 的——当前 framing 过度偏向 \"routing is inherently unlearnable\"，而非 \"data insufficient for minority class\"。\n\n**W4** r=0.97 correlation 是数学必然但在正文 Figure 2 prominent 展示——建议移入 appendix。\n\n**W5** Episode-level → step-level distribution shift（pure-strategy → mixed-strategy）的讨论在 Method/Discussion 中不充分。\n\n### 小问题\n- vLLM 版本应在首次出现时标注\n- Reflexion N=220 vs baseline N=245 的差异未解释\n- Figure 3 dose-response 中 72B 与 retry/reflexion 的 denominator 不同\n- Appendix N failure mode taxonomy 基于 single annotator\n- \"code and data will be released upon acceptance\" 在 double-blind 期间无法验证\n\n### 主要优势\n1. Framework 的 motivation（97.4% step-level tie rate）convincing\n2. 极为突出的自我批评意识（20 appendix robustness checks）\n3. Cross-model convergence（DAF 88-90%, 2.2pp spread）\n4. Intervention analysis 系统性（4 axes + dose-response）\n5. Cross-environment probes 展示框架诊断能力\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条回应 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见（完整原文）\n\n### 总体评分\nOverall Assessment: 3.0 (Findings)\nSoundness: 3.5/5 | Excitement: 2.5/5 | Reproducibility: 4/5 | Confidence: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 的核心发现部分是 penalty structure 的数学必然\n- DAF = δP/(δP + Δ_nd) 随 P 单调递增。P=100 时 DAF=90.4%，P=10 时仅 50.4%，P=5 时 35.4%（Appendix K）。论文在 §2.4 承认是\"数学后果\"，但 abstract/title framing 仍将 DAF=90.4% 作为核心 empirical result 突出。真正 penalty-independent 的是 label fraction (78.9%) 和 death rate differential (+26.5 pp)。\n\n**N2** [critical] \"Deterministic\" strategy 实为 oracle access，混淆了 routing signal 分析\n- ScienceWorld 中 deterministic 通过 simulator forking 获取 ground-truth state（Appendix T），本质是 oracle。在极端信息不对称下 \"oracle prevents death more often\" 几乎是 trivially expected。未设计 intermediate 对照条件分离信息优势的边际贡献。\n\n**N3** [critical] 环境覆盖过窄，generalizability 声明缺乏充分支撑\n- 核心分析仅 ScienceWorld 11/30 tasks (37%)。MATH 和 ALFWorld 提供 null results，不构成对 death dominance 的正面验证。标题和 abstract 的 framing 更像 general empirical finding，但 Limitations 将通用性声明限制为 methodological。\n\n### Should-Fix 问题\n\n**W1** Cluster bootstrap (K=11) 统计推断 reliability 不足——primary CI [81.1%, 99.0%] 可能过窄，K=11 远低于推荐的 K≥20-30。\n\n**W2** Excluded task types (63%) 的 n=5 prescreening 样本量极小，anti-cherry-picking claim 的 confidence 不足。\n\n**W3** Router negative result 在极端 class imbalance (90.5% majority) 下是 expected 的——当前 framing 过度偏向 \"routing is inherently unlearnable\"，而非 \"data insufficient for minority class\"。\n\n**W4** r=0.97 correlation 是数学必然但在正文 Figure 2 prominent 展示——建议移入 appendix。\n\n**W5** Episode-level → step-level distribution shift（pure-strategy → mixed-strategy）的讨论在 Method/Discussion 中不充分。\n\n### 小问题\n- vLLM 版本应在首次出现时标注\n- Reflexion N=220 vs baseline N=245 的差异未解释\n- Figure 3 dose-response 中 72B 与 retry/reflexion 的 denominator 不同\n- Appendix N failure mode taxonomy 基于 single annotator\n- \"code and data will be released upon acceptance\" 在 double-blind 期间无法验证\n\n### 主要优势\n1. Framework 的 motivation（97.4% step-level tie rate）convincing\n2. 极为突出的自我批评意识（20 appendix robustness checks）\n3. Cross-model convergence（DAF 88-90%, 2.2pp spread）\n4. Intervention analysis 系统性（4 axes + dose-response）\n5. Cross-environment probes 展示框架诊断能力\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2255 · 2026-05-22T04:48:52.003838+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1407
}
```

</details>

---


### Assistant

_source line 2256 · 2026-05-22T04:48:55.962312+00:00_

交叉分享已派发。两位 Reviewer 正在互审对方意见，等待 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 185

## Round 185

2 recorded events


### User

_source line 2257 · 2026-05-22T04:48:58.508578+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)。

核心判断：
- 3 个 Must-Fix：正文疑超 8 页限制、generalization claims 超出证据、"deterministic" 跨环境不可比性未充分讨论
- 5 个 Should-Fix：DAF 受 penalty 机械驱动但被主打、oracle simulator 非现实性、appendix 过度膨胀、actionability 有限、router negative result 基于有限架构探索
- 主要优势："先诊断再建 router" 的新颖视角、统计严谨性出色、跨模型一致性强、anti-cherry-picking 意识强、negative result 坦诚报告

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

_source line 2258 · 2026-05-22T04:49:03.526519+00:00_

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


## Round 186

## Round 186

2 recorded events


### User

_source line 2259 · 2026-05-22T04:50:43.349507+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

### R2-N1: 正文疑似超出 8 页限制

**[AGREE]** R2-Issue-N1

确认此问题。根据 PDF 视觉检查，Section 5 (Discussion) 占据第 8 页大部分空间，Section 6 (Conclusion) 起始于第 9 页顶部。按 EMNLP 2026 规则，Limitations 和 Ethics 不计入页数限制，但 Conclusion 属于正文，必须在第 8 页内结束。虽然 Conclusion 极短（从 conclusion.tex 看仅 3 行文字），溢出量很小，但这仍构成格式违规，可能触发 desk reject。这是一个 must-fix 但 technically trivial 的问题——通过轻微压缩 Discussion 或 Related Work 即可将 Conclusion 收回第 8 页。

我自己的审稿中未单独标注此问题，补充认同 R2 的发现。

---

### R2-N2: Generalization claims 超出证据支撑

**[AGREE]** R2-Issue-N2

与我自己的 N3 一致。核心定量分析局限于 ScienceWorld 的 11/30 task types。MATH 提供 null result（no routing signal, §3.4），ALFWorld 提供 complementary mechanism (DAF=0%, information asymmetry, §3.4)，两者均不构成对 death avoidance dominance 的正面 replication。

补充一个 R2 未提到的细节：Limitations 第 1 段（main.tex L40）中论文自己承认 "Our quantitative results (DAF = 90.4%, label fractions) are specific to ScienceWorld; the framework's generality claim is methodological...not empirical"。但 Abstract 的措辞（"confirming convergence on a single dominant mechanism"）和 Conclusion 的表述并未一致地限定为 methodological generality。这种 framing inconsistency 需要统一。

---

### R2-N3: "Deterministic" 策略在三个环境中含义不同

**[AGREE]** R2-Issue-N3

与我自己的 N2 高度相关。论文在 Section 2.1 footnote 2 中确实承认了这一差异（"The term 'deterministic' denotes different information advantages across environments"），且 Table in Appendix L (cross-environment details) 也区分了 mechanism。但 R2 正确指出：当同一个术语在三个环境中指代 oracle simulator / code interpreter / admissible-action enumeration 三种质性不同的信息优势时，跨环境对比的概念一致性 (conceptual unity) 受损。

我的补充：这个问题不仅影响 terminology，还影响 framework 的解释力。ScienceWorld 的 "deterministic" 是 perfect-information oracle，ALFWorld 的是 action-space enumeration（弱得多的信息优势），MATH 的是 computation verification。不同类型的信息优势会产生不同 magnitude 的 routing signal，但论文将它们放在同一个 framework 下比较 DAF 值（ScienceWorld 90.4% vs ALFWorld 0% vs MATH N/A），暗示 DAF 是 comparable across environments，而实际上 "deterministic" 的 operationalization 差异使这种比较缺乏 common scale。

建议论文要么 (a) 放弃统一 "deterministic" 术语，改用 environment-specific 术语（如 oracle, interpreter, enumerator），要么 (b) 在 framework definition (Section 2.1) 中明确将 "deterministic" 定义为 "any external computation mode that provides information advantage"，并讨论不同 advantage types 对 DAF 的结构性影响。

---

## Should-Fix 问题

### R2-W1: DAF 以 penalty 机械驱动，应以 label fraction 为主

**[AGREE]** R2-Issue-W1

与我自己的 N1 完全一致。DAF = δP/(δP + Δ_nd) 随 P 单调递增（Section 2.4, Eq. 5; Appendix K Table 显示 P=10 时 DAF 仅 50.4%）。论文虽在 Section 2.4 将 label fraction 称为 "primary finding"，但 Abstract 首句 headline 数字仍是 "78.9% of non-tie routing labels" 配合 "DAF reaches 88-90%"，且 Section 3.1 中 DAF=90.4% 出现在 label fraction 之后而非之前。建议：Abstract 中以 label fraction 78.9% 为唯一 headline metric，DAF 降级为 supplementary score-space characterization。

---

### R2-W2: Oracle simulator 的非现实性未充分讨论

**[AGREE]** R2-Issue-W2

与我自己 N2 的 oracle confound 论点一致。论文将 deterministic strategy 定位为 diagnostic baseline（Section 2.1: "our analysis investigates what signal is available to learn ρ"），但未充分讨论 diagnostic baseline vs. deployment-realistic alternative 之间的 gap。在 ScienceWorld 中，deterministic strategy 通过 simulator forking 获得 ground-truth state（Appendix T），这在真实 deployment 中不可用。如果用一个更 realistic 的 external tool（如 noisy simulator、partial oracle），death rate differential 会缩小，DAF 也会变化。论文的 Limitations 第 4 段（main.tex L48-49）承认 "DAF = 90.4% represents an upper bound on death avoidance's contribution to optimized routing"，但这一关键 caveat 仅出现在 Limitations 中，而非 Discussion 或 Method 中。

---

### R2-W3: Appendix 过度膨胀

**[REBUT]** R2-Issue-W3

部分不同意。对于一篇 Interpretability and Analysis track 的论文，extensive appendix 是审稿人验证 claims 的必要资源。20 个 appendix sections 中每一个都对应正文中的一个 specific claim 或 robustness check（如 Appendix E 对应 §3.1 的 cluster bootstrap caveat，Appendix S 对应 §3 的 anti-cherry-picking）。这种 "claim → appendix verification" 的结构恰恰是论文统计严谨性的体现。

但 R2 有一个合理的子论点：**Algorithm 1（当前在 Appendix B）应在正文呈现**。Algorithm 1 定义了 episode-level labeling function，是 framework 的核心组件之一，读者需要在 Method section 中直接看到它来理解 labeling logic（尤其是 death-first priority 的设计选择）。将 Algorithm 1 移入 Section 2.3 是合理的。

但 failure mode analysis (Appendix N) 保留在 appendix 更合适——它是 post-hoc mechanistic explanation，不影响 framework 的理解，且正文已有空间压力（R2-N1）。

---

### R2-W4: Actionability 有限

**[AGREE]** R2-Issue-W4

论文自己在 Limitations 第 5 段（main.tex L51-52）承认 "Our framework is diagnostic rather than prescriptive"。虽然 Appendix R 提供了一个 Practitioner Decision Framework（3-stage procedure: pilot collection → death dominance check → decision），但这在正文中仅以 "a ~50-episode diagnostic pilot" 一笔带过（Conclusion, conclusion.tex L3）。Discussion (Section 5) 的三个段落分别讨论 router failure reason、non-triviality、practical implications，但 "Practical implications" 段更多是 diagnosis 描述而非 actionable next steps。

建议在 Discussion 中增加一段明确的 "Implications for Router Design"：例如，当 f_death > 75% 时，router development budget 应转向 death prevention（如 action filtering, Appendix O）而非 routing optimization。Appendix O 的 grounding ablation 已经提供了这样的 actionable evidence（action-space filtering 降低 death rate 19 pp），但这个 insight 被埋在 appendix 中。

---

### R2-W5: Router 训练 negative result 基于有限架构探索

**[REBUT]** R2-Issue-W5

部分不同意。论文实际测试了比 R2 描述的更多架构：

1. **Implicit router** (SFT + LoRA): Qwen3-0.6B / 1.7B / 4B，三个 scale（Appendix P, Table）
2. **Classification head** (Linear + LoRA): degenerates across all configurations（Appendix I, Table）
3. **Generative router**: balanced accuracy 46.7%（Appendix P, "Generative router" paragraph）
4. **Leave-one-task-type-out routing**: collapses to always-deterministic（Appendix P）
5. **Death-proximal labeling**: step balanced accuracy 50.0%（Appendix P）
6. **Guided router with keyword leakage**: 62.9%，but only through task-identity leakage（Appendix P）

这不是仅 "LoRA-tuned Qwen3 三个 scale"。六种不同 variants 均失败（或仅通过 task-identity leakage 成功），这为 "signal-limited" 解释提供了更强的 convergent evidence。

但论文确实在 Section 3.6 末尾承认了 "Alternative architectures (e.g., contrastive objectives), larger training corpora, or multi-task setups may yield different conclusions; our finding is specific to LoRA-tuned Qwen3 on 2,040 steps"。这个 hedge 是合适的。

我唯一的补充是：如我自己 W3 所述，当 minority class 仅有 9 个 samples（3.7% internal-preferred）时，"signal-limited" vs "data-limited" 两种解释难以区分。论文倾向 "signal-limited" 但 "data-limited" 同样成立——收集 1,350+ paired episodes 以获得 50 个 internal-preferred samples 虽然昂贵但并非不可能，论文未尝试。

---

## 小问题回应

1. **Abstract 信息密度过高** — [AGREE]，Abstract 确实同时包含 framework description、ScienceWorld results (78.9%, DAF)、cross-model (3 families)、cross-environment (MATH, ALFWorld)、pilot sample size (50 episodes, d=3.02)，信息负载偏高。
2. **§2.4 s̄_surv 近似** — [AGREE]，s̄_surv = 0.87 (0.9% of P) 在 ScienceWorld 成立但在 dense-reward 环境中可能失效，值得 caveat。
3. **Figure 2 r=0.97 标注** — [AGREE]，与我自己的 W4 一致。
4. **Limitations 过长** — [REBUT]，5 段 Limitations 中每段覆盖独立维度（scope, methodology, statistics, pure-strategy bound, diagnostic scope），精简至 3 段会丢失重要 caveats。鉴于论文的 self-critical strength，保留完整性更合适。且 Limitations 不计入页数限制。
5. **术语不一致** — [AGREE]，"catastrophic failure" vs "death" 确实混用，应统一。
6. **2026 引用** — [AGREE]，concurrent work 引用（如 cogrouter-2026, ares-2026 等）确实可能是未经 peer review 的 preprints，应在 Related Work 中标注。
7. **Ng et al. (1999) 引用适用性** — [REBUT]，该引用用于支撑 "agent policy 不包含 P in observation, so death rates are P-invariant by design"（Section 2.4），这是 policy invariance under reward shaping 的标准引用，适用性成立。

---

## 总结

R2 与我（R1）的意见高度一致：核心 Must-Fix 问题集中在 (1) DAF 的数学依赖性 vs empirical framing、(2) generalization 不足、(3) "deterministic = oracle" confound。R2 额外发现的页数超限问题（N1）是重要的格式 flag。

两位 reviewer 共同认可的优势：方法论清晰、统计严谨、自我批评意识强、cross-model convergence。

建议最终评分维持 **Overall 3.0 (Findings)**。


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

_source line 2260 · 2026-05-22T04:50:49.215489+00:00_

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


## Round 187

## Round 187

2 recorded events


### User

_source line 2261 · 2026-05-22T04:50:55.533741+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 所有 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 及小问题的逐条回应。

汇总：
- **N1 (页数超限)**: [AGREE]，Section 6 Conclusion 溢出到第 9 页，格式违规需修复
- **N2 (Generalization)**: [AGREE]，与我 N3 一致
- **N3 (Deterministic 含义不统一)**: [AGREE]，与我 N2 相关，补充了 DAF 跨环境不可比的论点
- **W1 (DAF vs label fraction)**: [AGREE]，与我 N1 一致
- **W2 (Oracle 非现实性)**: [AGREE]，与我 N2 一致
- **W3 (Appendix 膨胀)**: [REBUT]，分析论文需要详尽 appendix，但同意 Algorithm 1 应移入正文
- **W4 (Actionability)**: [AGREE]，建议将 Appendix O 的 actionable insight 提升到 Discussion
- **W5 (Router 架构探索有限)**: [REBUT]，论文实际测试了 6 种 variants 而非仅 3 个 scale，但 data-limited vs signal-limited 仍难区分

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

_source line 2262 · 2026-05-22T04:51:00.041610+00:00_

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


## Round 188

## Round 188

12 recorded events


### User

_source line 2263 · 2026-05-22T04:51:05.502491+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: DAF 核心发现部分是 penalty structure 的数学必然**

同意 R1 的判断。我在自己的审稿中也提出了相同的问题（我的 W1）。DAF = δP/(δP + Δ_nd) 是 P 的单调函数，Table in App K 清楚地展示了这一点：P=5 时 DAF 仅 35.4%，P=10 时 50.4%。论文在 §2.4 诚实地承认了这是"数学后果而非实证发现"，但 Abstract 的措辞仍以 "Death Avoidance Factor, reaches 88–90% across three 7–9B model families" 作为高亮，Title 同样以 "Death Avoidance as the Dominant Routing Signal" 为主打——读者第一印象会认为 90% 是一个环境无关的稳健数字。

补充 R1 未提到的一点：论文实际上设计了 penalty-independent 的 label fraction (78.9%) 作为替代指标（§2.4 "The label fraction, invariant to penalty magnitude, serves as the primary finding"），这说明作者有方法论自觉。但 Abstract 和 Conclusion 中 label fraction 和 DAF 的权重分配需要调整——78.9% 应是主打数字，DAF 88–90% 作为 ScienceWorld 特定 penalty 下的补充度量。

**[AGREE with nuance] R1-N2: "Deterministic" strategy 实为 oracle access，death avoidance 接近 trivially expected**

部分同意，但认为 R1 的"trivially expected"判断需要限定范围。

**同意的部分**：ScienceWorld 的 deterministic 策略通过 simulator forking 获得 ground-truth state（§2.2，App T 的 deterministic candidate generation template 显示 agent 生成 top-3 candidates 由 simulator 评估），本质上是 oracle access。在这种极端信息不对称下，"oracle 比内部推理更安全"确实是 expected 的。R1 指出的"未设计 intermediate 对照条件"是合理批评——论文缺少位于 pure-internal 和 full-oracle 之间的条件（如 partial oracle、noisy state feedback、limited lookahead）来分离信息优势的边际贡献。

**反驳的部分**：R1 说"oracle prevents death more often 几乎 trivially expected"需要区分两个层次：
- (a) "Oracle 比 internal 安全"——是，这接近 trivially expected
- (b) "78.9% 的所有 routing signal 来自 death gap，non-death signal 几乎为零 (Δ_nd = 2.84)"——这并非 trivially expected

Prior expectation 可能是：oracle 在 death avoidance 上有优势，但在 non-death episodes 上 internal reasoning 也有独特优势（如更灵活的探索策略）。论文的发现是 non-death gap 几乎不存在（§3.1: Δ_nd = +2.84，仅占 Δ_full 的 9.6%），这是一个 non-trivial empirical observation。

此外，App O 的 grounding ablation 提供了部分 intermediate evidence：prompt warning 将 death rate 从 48% 降至 37%（Δ = -11pp），action-space filtering 降至 29%（Δ = -19pp），但均未接近 deterministic 的 16.3%。这暗示 oracle access 的安全优势不仅来自信息本身，还来自系统性地避免 `focus on` 误用的结构。但这些证据在 appendix 中，正文对此讨论不足（与我的 W4 一致）。

**建议**：R1 的核心建议（设计 intermediate 条件）是提升论文的最佳路径。至少应在 Discussion 中讨论 grounding ablation（App O）作为现有的 partial evidence。

**[AGREE] R1-N3: 环境覆盖过窄，generalizability 声明缺乏充分支撑**

完全同意。我在自己的审稿中将此列为 N2（critical）。

R1 的分析精准：(a) ScienceWorld 11/30 tasks = 37%；(b) MATH 是 null result；(c) ALFWorld 诊断出不同机制但不验证 death dominance。我补充的证据：
- MATH 的 $73.5\%$ vs $73.0\%$（$p = 0.81$, §3.4）本质上显示两个策略无差异，任何诊断框架都会得出相同结论——这不验证框架的诊断能力
- ALFWorld 确实展示了框架的鉴别力（DAF = 0% vs 90.4%），但仅此一个跨环境正面案例
- 论文在 Limitations 中正确将通用性限定为 methodological ("the diagnostic procedure applies to any environment with asymmetric fatal outcomes")，但 Abstract 和 Conclusion 的措辞（"Cross-environment probes illustrate applicability"）模糊了 methodological vs empirical generality 的区分

---

### Should-Fix 问题

**[REBUT] R1-W1: Cluster bootstrap (K=11) 统计推断 reliability 不足**

R1 的统计担忧本身合理（K=11 < 推荐的 K≥20–30），但论文已经正确处理了这一问题。具体证据：

1. §3.1 明确指出 "with K=11 < 20 clusters, we treat this as a sensitivity check rather than primary inference"
2. App E (Table 5) 标题为 "Cluster Bootstrap **Sensitivity** Analysis"，明确定位为敏感性检查而非 primary inference
3. App E 正文首句："With K=11 task-type clusters, cluster bootstrap falls well below the K≥20–30 recommended"
4. §3.1 指导读者 "readers should rely on the non-clustered episode-level bootstrap CIs reported above"

论文的 primary CI [81.1%, 99.0%] 来自 non-clustered episode-level bootstrap（B=10,000），不依赖 cluster assumption。Cluster bootstrap 的 wider CI [73.3%, 100.0%] 作为保守 sensitivity check 已被报告。论文的统计处理在这一点上是严谨的——R1 的担忧已被论文自身充分回应。

**[AGREE with caveat] R1-W2: Excluded tasks n=5 prescreening 样本量小**

同意 n=5 per task（App C Table 4, Groups B–C）是非常小的样本——在 n=5 时，即使 ΔDR = +40pp 的 95% CI 也约 ±43pp（论文在 App F 中自己计算了这一点）。因此 Group B–C 各 task 的具体 death rate 数字不可靠。

**但有重要 caveat**：论文的 anti-cherry-picking argument 不依赖单个 excluded task 的精确 death rate，而是依赖两个更稳健的事实：
1. **方向一致性**：18/19 excluded tasks（95%）显示 positive death asymmetry（App C Table 4），在 n=5 下方向性估计比精确率更可靠
2. **Extended validation**（App S, Table in §S）：对 5 个 representative excluded tasks 扩展到 n=20，mean ΔDR = +32.0pp，与 n=5 prescreening 一致

R1 的批评对精确率估计有效，但论文的核心 claim（"excluded tasks 不弱于 included tasks"）基于方向一致性和 extended validation，在当前证据下是站得住脚的。建议论文更清楚地标注 Group B–C 的 n=5 限制（当前在 Table 4 caption 中有提及但不够 prominent）。

**[AGREE] R1-W3: Router negative result 在极端 class imbalance 下是 expected 的**

同意 R1 的判断。这是论文 framing 中的一个重要偏差。

证据：训练数据中 86/95 = 90.5% 是 deterministic-preferred（§3.1），internal-preferred 仅 9 例（3.7%）。在如此极端的 class imbalance 下，任何标准 classifier 都会 collapse to majority-class prediction——这正是观察到的行为（App J Table 8: "Internal recall = 0.0 at all scales"）。

论文在 App J 中承认了这一点（"the episode-level routing problem is trivially solved by always choosing deterministic"），但 §3.6 正文的 framing 是 "routing bottleneck is signal-limited, not architecture-limited"（App P）。R1 正确指出更准确的 framing 应该是：

- **当前数据下** router 失败是 class imbalance 的预期结果
- **是否存在可学习的 step-level signal** 仍是 open question，需要通过收集更多 internal-preferred episodes 来回答（论文在 App J 中计算了需要 ~1,350 paired episodes 才能收集 50 个 internal-preferred，是当前 5.5× expansion）
- "Signal-limited" 和 "data-limited for minority class" 是不同的 claim，论文混淆了两者

**[REBUT] R1-W4: r=0.97 correlation 应移入 appendix**

不同意移除 Figure 2，但同意需要更明确的标注。

理由：Figure 2（§3.1）是论文的核心 visual summary——它一张图展示了 death rate differential 与 performance gap 的关系，直观传达了 "death drives everything" 的核心 message。移入 appendix 会削弱论文的可读性。

论文已经在 Figure 2 caption 中注明 "the near-perfect correlation is a structural consequence of death dominance, not an independent finding (§3.1)"，§3.1 正文也明确说 "The near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding. We retain it as an internal consistency check."

**建议折中方案**：保留 Figure 2 在正文中，但 (a) 缩小为 0.5\columnwidth（当前是 0.85\columnwidth），(b) 在 caption 首句即标注 "Internal consistency check"，(c) 移除 §3.1 中 "Per-task correlation structure" 段落以 r = 0.97 开头的措辞，改为以其数学必然性开头。

**[AGREE] R1-W5: Episode→step distribution shift 讨论不充分**

同意。论文在 Limitations 中简短提及 "Training on pure-strategy trajectories also introduces distribution shift at deployment (DAgger, 2011)"，以及 "projecting episode-level labels onto 10–50 sequential steps with path-dependent state introduces compounding error"。但这一问题在 Method（§2）和 Discussion（§5）中未被充分讨论。

具体遗漏：
1. §2.4 "Scope of episode-level analysis" 讨论了 step-level degeneracy，但未讨论 pure→mixed deployment shift
2. §5 Discussion 的 "Why the router fails" 将失败归因于 "task-type-level binary property"，但未讨论 distribution shift 作为 alternative/complementary 解释
3. §3.6 Router Training 的 negative result 可能部分由 distribution shift 而非 signal absence 导致——在 pure-strategy trajectory 上训练的 router 部署在 mixed-strategy trajectory 上，state distribution 不同

建议在 §5 或 §2.4 中增加一段讨论 distribution shift 的影响，包括与 DAgger（已引用）和 off-policy evaluation 文献的联系。

---

### 小问题快速回应

- **vLLM 版本**：同意，应在 §2.2 首次出现时标注（当前仅在 App I 提及 v0.21.0）
- **Reflexion N=220 vs baseline N=245**：有效关注点，差异可能来自 task coverage 差异，应在 §3.3 解释
- **Figure 3 denominator 不同**：同意，72B baseline (all 11 tasks, N=255) vs retry/reflexion (10 death-prone tasks, N=200) 在同一图中比较时 denominator 不同，应在 caption 中更明确标注
- **App N single annotator**：论文在 App N 已承认 "This taxonomy was produced by a single annotator; no inter-annotator agreement was computed"——这种透明度是好的，但确实限制了 taxonomy 的可靠性
- **Code release 在 blind review 期间无法验证**：标准做法，不构成问题

---

### 总体一致性评估

R1 和我（R2）在核心判断上高度一致：
- **Overall 评分**：均为 3.0 (Findings)
- **Soundness**：均为 3.5/5
- **Excitement**：均为 2.5/5
- **关键弱点共识**：(1) DAF 的 penalty dependence，(2) oracle/"deterministic" 的概念问题，(3) 环境覆盖过窄

主要分歧：R1 认为 r=0.97 应移入 appendix（我认为保留但降低 prominence），R1 对 cluster bootstrap 的担忧比我更强（我认为论文已充分处理）。

建议 Director：两位 Reviewer 的一致意见指向 **Findings 稳固水平**（Overall 3.0）。如果作者能 (1) 修复页数问题，(2) 调整 DAF vs label fraction 的权重，(3) 精确化 generalization claims 的措辞，论文可达到 3.0–3.5 区间。


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

_source line 2264 · 2026-05-22T04:51:28.387946+00:00_

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

_source line 2265 · 2026-05-22T04:51:28.590147+00:00_

1	# Round 26 Review Issues (fresh review, 2026-05-21)
2	# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+相关工作)
3	
4	# =============================================
5	# Carried-over resolved issues (from prior rounds)
6	# =============================================
7	
8	- id: "R13-W1"
9	  summary: "正文篇幅严重不足 long paper 要求"
10	  category: format
11	  severity: warning
12	  status: resolved
13	  first_raised_round: 13
14	  last_seen_round: 14
15	  resolution: "正文已扩展至 8 页"
16	  resolution_round: 14
17	
18	- id: "R13-W2"
19	  summary: "Router 训练实验存在多个 confound"
20	  category: experiment
21	  severity: warning
22	  status: resolved
23	  first_raised_round: 13
24	  last_seen_round: 15
25	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
26	  resolution_round: 15
27	
28	- id: "R13-W3"
29	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
30	  category: method
31	  severity: info
32	  status: resolved
33	  first_raised_round: 13
34	  last_seen_round: 14
35	  resolution: "Limitations 和 Appendix B 已充分量化"
36	  resolution_round: 14
37	
38	- id: "R13-W4"
39	  summary: "SCI 方法贡献与实际使用不成比例"
40	  category: method
41	  severity: info
42	  status: resolved
43	  first_raised_round: 13
44	  last_seen_round: 14
45	  resolution: "SCI 已降级到 Appendix A"
46	  resolution_round: 14
47	
48	- id: "R13-W7"
49	  summary: "Router negative results 解释不完整"
50	  category: experiment
51	  severity: warning
52	  status: resolved
53	  first_raised_round: 13
54	  last_seen_round: 15
55	  resolution: "Router 实验定位为 diagnostic probe"
56	  resolution_round: 15
57	
58	- id: "R13-m2"
59	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
60	  category: writing
61	  severity: warning
62	  status: resolved
63	  first_raised_round: 13
64	  last_seen_round: 16
65	  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
66	  resolution_round: 16
67	
68	- id: "R13-m3"
69	  summary: "Reference 格式不统一 + orphan entries"
70	  category: format
71	  severity: info
72	  status: resolved
73	  first_raised
…[truncated 22306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 2266 · 2026-05-22T04:51:28.593852+00:00_

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

_source line 2267 · 2026-05-22T04:51:28.594237+00:00_

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

_source line 2268 · 2026-05-22T04:51:28.694952+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T04:39:44.053646+00:00\", \"completed_at\": \"2026-05-22T04:44:18.921949+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"主文（Abstract 至 Section 6 Conclusion）延伸至第 9 页（Discussion 续写 + Conclusion 段落），超出 EMNLP 2026 的 8 页正文限制（Limitations/Ethics 不计入页数）。审稿人或编辑可能因此 desk reject。建议压缩 Related Work 或 Discussion 以回收约 0.5-1 栏空间。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 8-9\", \"message\": \"连续 2 页纯文本（Related Work → Discussion → Conclusion → Limitations），形成\\\"文字墙\\\"。建议在 Discussion 中加入一个总结性 display item（如 key findings 汇总表或 DAF 分解可视化）打破节奏。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-7\", \"message\": \"主文仅 5 个 display items（3 figure + 2 table），对于实证分析型论文偏少。实验结果集中在 pages 4-7，pages 1 和 3 各为纯文本页（Introduction 和 Method 公式段，后者可接受）。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 流程图作为首个视觉锚点功能性足够，但设计偏素——方框+箭头+纯色填充。可考虑增加示例数据流或视觉层次以强化第一印象。\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"附录中 Figures 5/6/7 三图挤在同一页，Figure 6（step-by-step action sequences）文字极小，150 dpi 下已接近可读性下限。建议调大字号或拆分到两页。\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", \"message\": \"末页（附录 T: Agent Prompt Templates）底部约 40% 空白，不影响评审但显示空间利用未最优。\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

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

_source line 2269 · 2026-05-22T04:51:28.695375+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

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

_source line 2270 · 2026-05-22T04:55:37.350394+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "# Round 27 Review Issues (fresh review, 2026-05-22)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n# =============================================\n# Round 27 — Active issues (new + recurring)\n# =============================================\n\n# --- Critical / Must-Fix ---\n\n- id: \"R27-N1\"\n  summary: \"正文超出 8 页限制——Conclusion 溢出到 page 9（R20-N1 复发）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 27\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"R20-N1 resolved: 正文收入 8 页\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Discussion 占满 page 8，Conclusion 3 行溢出到 page 9。格式违规，可能触发 desk reject。Technically trivial fix。\"\n  action_items:\n    - round: 27\n      action: \"压缩 Discussion 或 Related Work，将 Conclusion 收入 page 8\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% 部分是 P=100 penalty 的数学必然，Abstract/Title framing 过度突出\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-N1: Abstract 以 label fraction 为 headline 但 §5 缺 penalty sensitivity 讨论\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] DAF=δP/(δP+Δ_nd) 随 P 单调递增。P=10→50.4%, P=5→35.4% (App K)。§2.4 承认数学后果但 Abstract 仍以 DAF 88-90% 为高亮。真正 penalty-independent 的是 label fraction 78.9%。\"\n  action_items:\n    - round: 27\n      action: \"Abstract/Conclusion 以 78.9% label fraction 为唯一 headline metric，DAF 降为 ScienceWorld-specific supplementary\"\n      assigned_to: main_agent\n      status: open\n    - round: 27\n      action: \"§5 Discussion 加独立段落讨论 penalty sensitivity + 引用 App K Table\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一，oracle confound 未分离\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 27\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"R15-N2 resolved: §5.4 加交叉引用\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 三环境 deterministic 质性不同：ScienceWorld=oracle simulator, MATH=code interpreter, ALFWorld=admissible-action enumeration。仅脚注承认不足。Oracle→death asymmetry 接近 trivially expected（R1判断），但 R2 nuance: 78.9% all-from-death + Δ_nd=2.84 仅 9.6% 是 non-trivial observation。缺 intermediate 对照条件。\"\n  action_items:\n    - round: 27\n      action: \"§2.1 正文讨论 operationalization 差异（不仅脚注）；考虑 'privileged-information strategy' 替代术语\"\n      assigned_to: main_agent\n      status: open\n    - round: 27\n      action: \"§5 Discussion 讨论 oracle confound：App O grounding ablation 作为 partial intermediate evidence\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄，generalization claims 超出证据——1 个主环境 + 2 个 boundary probes\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-W6: reframe 为 environment-specific mechanisms\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] ScienceWorld 11/30 tasks (37%)。MATH=null result（任何框架都得出无信号）。ALFWorld=唯一正面跨环境案例。Limitations 限定为 methodological generality 但 Abstract/Conclusion 措辞模糊。Cross-model (3x 7-9B) 在同环境内，非跨环境验证。\"\n  action_items:\n    - round: 27\n      action: \"Abstract 'illustrate applicability' → 'provide preliminary evidence'；明确区分 methodological vs empirical generality\"\n      assigned_to: main_agent\n      status: open\n    - round: 27\n      action: \"理想情况：增加一个 catastrophic-failure 环境 (NetHack/Crafter/WebArena) 的完整验证\"\n      assigned_to: main_agent\n      status: open\n\n# --- Warning / Should-Fix ---\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing: signal-limited vs data-limited 未区分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-W2: 标为 preliminary\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 90.5% majority class + 仅 9 个 internal-preferred samples。Any classifier collapses to majority prediction (App J: internal recall=0.0)。六种 variants 均失败（R1 补充 R2 未覆盖的 variants），但 data-limited 同样成立——需 ~1350 paired episodes 获得 50 internal-preferred。§3.6 framing 偏向 signal-limited。\"\n  action_items:\n    - round: 27\n      action: \"§3.6 明确区分两种解释 (signal-limited vs data-limited for minority class)，标为 preliminary\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限——诊断出问题但'然后怎么办'回答不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R25-W6: 未直接提及\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] App R decision framework 阈值是 ScienceWorld-specific。App O grounding ablation (death rate -19pp) 是可操作证据但被埋在 appendix。Discussion 缺 actionable next steps。\"\n  action_items:\n    - round: 27\n      action: \"§5 Discussion 增加 'Implications for Router Design' 段：f_death>75% 时转向 death prevention (action filtering etc)\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W3\"\n  summary: \"Episode→step distribution shift (pure→mixed strategy) 在 Method/Discussion 中讨论不充分\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Limitations 提及 DAgger + compounding error，但 §2/§5 未讨论。Router negative result 可能部分由 distribution shift 导致（pure-strategy training → mixed-strategy deployment）。\"\n  action_items:\n    - round: 27\n      action: \"§5 或 §2.4 增加一段讨论 pure→mixed distribution shift 及其对框架实用性的影响\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks (63%) n=5 prescreening 样本量极小\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE with caveat] n=5 精确率不可靠 (CI ±43pp)，但方向一致性 18/19=95% 较稳健。Extended validation (App S, 5/19 tasks, n=20) 一致。Anti-cherry-picking claim 基于方向性而非精确率，站得住脚。\"\n  action_items:\n    - round: 27\n      action: \"Table 4 caption 或 §3 更 prominent 标注 n=5 限制\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap: primary CI [81.1%, 99.0%] 可能 anti-conservative\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-W4: §3.1 caveat 需加强\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1 认为需在主文更明确标注 anti-conservative nature；R2 rebuts 认为论文已正确处理（降级为 sensitivity check）。最终：论文处理得当但可进一步加强。\"\n  action_items:\n    - round: 27\n      action: \"§3.1 考虑报告 clustered CI [73.3%, 100.0%] 作为 conservative bound alongside primary CI\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W6\"\n  summary: \"Missing references: MoE routing (Switch Transformer, GShard), Neural Module Networks, counterfactual data augmentation (Kaushik 2020), process supervision\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"R2 发现。Agent routing/tool selection 覆盖充分，但缺 MoE routing 和 Neural Module Networks 上下文讨论，以及 counterfactual data augmentation 和 process vs outcome supervision 的联系。\"\n  action_items:\n    - round: 27\n      action: \"§4 Related Work 补充 MoE routing + Neural Module Networks 段落（2-3 句）\"\n      assigned_to: main_agent\n      status: open\n\n# --- Minor / Info ---\n\n- id: \"R27-M1\"\n  summary: \"Figure 2 r=0.97 是数学必然但 prominent 展示——建议降低 prominence\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1: 移入 appendix。R2: 保留但缩小 + caption 首句标注 'internal consistency check'。折中方案合理。\"\n\n- id: \"R27-M2\"\n  summary: \"Abstract 信息密度过高（DAF + label fraction + 3 models + cross-env + pilot）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 聚焦核心发现，模型数量和 pilot 细节留给 Introduction\"\n\n- id: \"R27-M3\"\n  summary: \"术语不一致：catastrophic failure vs death 混用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"§1 用 catastrophic failure，§2 用 death，§3 交替。应统一。\"\n\n- id: \"R27-M4\"\n  summary: \"Appendix 体量偏高 (20 sections, ~13 pages vs 8 pages main)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2: 膨胀。R1: 分析论文需要，但 Algorithm 1 应移入正文 §2.3。共识：Algorithm 1 移入正文。\"\n\n- id: \"R27-M5\"\n  summary: \"小问题集合：vLLM 版本未在首次出现标注；Reflexion N=220 vs baseline N=245 未解释；Figure 3 denominator 不同；2026 引用可能是 preprints；Ng 1999 引用适用性\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"多个小问题汇总。vLLM 版本 [AGREE]；Reflexion N [AGREE]；Figure 3 denominator [AGREE]；2026 引用 [AGREE]；Ng 1999 [R2 REBUT: 适用]\"\n\n# --- Structural / Long-standing ---\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"Excitement 2.5。§5 Non-triviality 缓解但不消除。结构性限制。\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"Excitement 仍 2.5/5。§5 non-triviality 段存在且有效。方法概念简单（episode-level A/B testing）。结构性限制不可通过 writing fix 解决，Findings 定位已确定。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 N2/N4 间接涉及。Abstract/Conclusion 在 methodological vs empirical generality 之间摇摆。\"\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"'contradicting' → 'revealing that in catastrophic-failure environments, signal diversity can collapse'\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未直接提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 26\n      action: \"Abstract/Intro 'contradicting' → 'revealing...can collapse'\"\n      assigned_to: main_agent\n      status: in_progress\n\n- id: \"R26-W1\"\n  summary: \"框架方法论新颖性不足——未连接因果推断文献 Pearl/Rubin\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"§4 加段讨论 potential outcomes 关系\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未直接提及，可能已修复，待 Research Director 确认\"\n\n- id: \"R26-W3\"\n  summary: \"~50-episode pilot 缺 power analysis\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"'suffices' → 'provides preliminary signal given d=3.02'\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未直接提及，可能已修复，待 Research Director 确认\"\n\n- id: \"R26-W5\"\n  summary: \"Agent-floor tasks 对 death dominance 的含义未讨论\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"7 个 agent-floor tasks 代表 symmetric death regime\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未直接提及，可能已修复，待 Research Director 确认\"\n\n- id: \"R25-W5\"\n  summary: \"实验规模偏小（per-task n=20）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1]\n      note: \"R1 间接涉及（sample size concerns）。共识：aggregate 可靠，per-task 需谨慎。不 blocking。\"\n"
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
    "issues_yaml": "# Round 27 Review Issues (fresh review, 2026-05-22)\n# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)\n\n# =============================================\n# Carried-over resolved issues (from prior rounds)\n# =============================================\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"正文已扩展至 8 页\"\n  resolution_round: 14\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"1.7B dip 有可检验假说，augmentation 术语修正，N 统一\"\n  resolution_round: 15\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"Limitations 和 Appendix B 已充分量化\"\n  resolution_round: 14\n\n- id: \"R13-W4\"\n  summary: \"SCI 方法贡献与实际使用不成比例\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"SCI 已降级到 Appendix A\"\n  resolution_round: 14\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Router 实验定位为 diagnostic probe\"\n  resolution_round: 15\n\n- id: \"R13-m2\"\n  summary: \"Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  resolution: \"Figure 3 已移除，数据在 Table 2 和正文中完整呈现\"\n  resolution_round: 16\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一 + orphan entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"Orphan entries 清理完毕，格式统一\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"Concurrent work 讨论过于压缩\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Concurrent work 展开讨论，各有明确 positioning\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"Selection bias from prescreening 11/30 task types\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Anti-cherry-picking analysis 到位\"\n  resolution_round: 15\n\n- id: \"R14-M1\"\n  summary: \"Table 2 caption 'Single seed' 需澄清\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Caption 已修正\"\n  resolution_round: 15\n\n- id: \"R14-M2\"\n  summary: \"Limitations section 组织松散\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"三个 paragraph headers 结构清晰\"\n  resolution_round: 15\n\n- id: \"R14-M3\"\n  summary: \"Appendix F minority-class diversity caveat 应在正文提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"§3.7 和 Appendix F 均明确提及\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11 CI 反常收窄\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Wild cluster CI 修正且降级为 sensitivity analysis；non-clustered bootstrap 为主推断\"\n  resolution_round: 24\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Abstract concept-first 重组，数字从 10+ 精简至 3-4 个\"\n  resolution_round: 24\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 24\n  resolution: \"Ng 1999, Northcutt 2021, DivideMix 已添加并在正确位置引用\"\n  resolution_round: 24\n\n- id: \"R14-W1\"\n  summary: \"核心发现存在 obvious-in-hindsight triviality 风险\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 24\n  resolution: \"§5 Non-triviality 段有效回应 novelty 质疑\"\n  resolution_round: 24\n\n- id: \"R15-N1\"\n  summary: \"'Structural' claim 推断基础不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Discussion 已弱化为 'robust under tested interventions'\"\n  resolution_round: 16\n\n- id: \"R15-N3\"\n  summary: \"Contribution 1 'any environment' generalizability claim 过宽\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Contribution 1 措辞已收窄\"\n  resolution_round: 16\n\n- id: \"R15-W1\"\n  summary: \"§3.7 Augmentation scaling 措辞易误读为 data scaling\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§3.7 明确标注为 paraphrase-based augmentation\"\n  resolution_round: 16\n\n- id: \"R15-W3\"\n  summary: \"72B 缺完整 DAF decomposition\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"72B DAF decomposition 完整呈现\"\n  resolution_round: 16\n\n- id: \"R17-W4\"\n  summary: \"Related Work 第一段论文罗列\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§4 已按功能类别重组（Self-supervised, Token-level, Task-level, RL-based）\"\n  resolution_round: 19\n\n- id: \"R17-W1\"\n  summary: \"Pure-strategy 设计高估 death asymmetry 对 realistic routing 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"Limitations 新增 pure-strategy upper bound 段落\"\n  resolution_round: 24\n\n- id: \"R17-W3\"\n  summary: \"Data scaling 'structural failure' 措辞\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"术语全局修正为 text augmentation\"\n  resolution_round: 24\n\n- id: \"R17-N2\"\n  summary: \"penalty-independent 表述误导：P=0 时 72% labels 退化为 ties\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"P-invariance 适用范围明确量化\"\n  resolution_round: 24\n\n- id: \"R18-N1\"\n  summary: \"Episode→step granularity gap 削弱框架实用性\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"4B router 结论 qualified；完整统计处理\"\n  resolution_round: 24\n\n- id: \"R18-W1\"\n  summary: \"Router 实验 confounds: compounding errors + train/val split 不清晰\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Router claim 从绝对否定改为有条件否定\"\n  resolution_round: 24\n\n- id: \"R18-W2\"\n  summary: \"Agent improvement 实验统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"措辞软化 + effect size detection threshold 完整报告\"\n  resolution_round: 24\n\n- id: \"R20-N1\"\n  summary: \"正文超出 8 页限制——§6 Conclusion 起始于 page 9，有 desk reject 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"正文收入 8 页\"\n  resolution_round: 24\n\n- id: \"R20-N2\"\n  summary: \"4B router episode-level 59.0% 与 'fundamental non-learnability' 结论矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R18-N1 解决\"\n  resolution_round: 24\n\n- id: \"R20-N3\"\n  summary: \"'Structurally determined' overclaim — r=0.97 correlation ≠ causal/structural\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"'structurally determined' → 'empirically dominated'\"\n  resolution_round: 24\n\n- id: \"R20-W2\"\n  summary: \"Per-task n=20 导致 13/28 tasks 不显著，主文未标注为 exploratory\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Per-task 结果标注为 exploratory，power caveat 完整\"\n  resolution_round: 24\n\n- id: \"R17-M1\"\n  summary: \"Orphan bib entry + Webb 年份待核实\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"huang2022inner, selfcheckgpt-2023, wang2023voyager 已清理；Webb 2023 (CJE vol.56 no.3) 年份正确\"\n  resolution_round: 24\n\n- id: \"R19-M2\"\n  summary: \"Missing references: Altman 1999, Mihatsch 2002, Natarajan 2013\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"所有缺失引用已补充\"\n  resolution_round: 24\n\n- id: \"R18-M3\"\n  summary: \"Appendix 缺索引（17 个 appendices A-R）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Appendix Overview with hyperlinks 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M4\"\n  summary: \"§3.1 '54 sole-identified labels' 首次出现未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"术语已修正并定义\"\n  resolution_round: 24\n\n- id: \"R18-M5\"\n  summary: \"Appendix N failure categories 缺 inter-annotator agreement 声明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Single annotator caveat 已存在\"\n  resolution_round: 24\n\n- id: \"R18-M2\"\n  summary: \"100% internal deaths 来自 single action pattern — implication 未讨论\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"§5 已讨论 focus on [object] 单一模式\"\n  resolution_round: 24\n\n- id: \"R20-M1\"\n  summary: \"Orphan bib entries: huang2022inner, selfcheckgpt-2023, wang2023voyager\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"合并 R17-M1 解决\"\n  resolution_round: 24\n\n- id: \"R15-N2\"\n  summary: \"跨环境模态定义不一致——三个环境的 deterministic 含义不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"§5.4 cross-env 段加交叉引用指向 §2.1 operationalization\"\n  resolution_round: 24\n\n- id: \"R15-W2\"\n  summary: \"Oracle margin vs mislabeling 逻辑层级未明确\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 24\n  resolution: \"Appendix B 加 circularity caveat; Limitations 量化 0.3% 方向冲突 + 60.3% pre-event neutral\"\n  resolution_round: 24\n\n- id: \"R20-W1\"\n  summary: \"Noisy label learning 引用和讨论深度不足\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"引用已补全；额外解释句因 8 页限制无法加入，现有措辞部分覆盖\"\n  resolution_round: 24\n\n- id: \"R18-M1\"\n  summary: \"'modality' 术语在 NLP 语境下有歧义\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"Algorithm 1 术语修正为 computation modes\"\n  resolution_round: 24\n\n- id: \"R17-N1\"\n  summary: \"78.9% label fraction binary per-task structure\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 24\n  resolution: \"§3.1 binary structure 讨论充分\"\n  resolution_round: 24\n\n- id: \"R16-W1\"\n  summary: \"72B vs 7B DAF 对比基于不同 task population 且缺少实验细节\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"72B decomposition 完整报告\"\n  resolution_round: 24\n\n- id: \"R16-W2\"\n  summary: \"Router 1.7B non-monotonic dip 解释缺乏 per-class evidence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"被 R20-N2 取代并解决\"\n  resolution_round: 24\n\n- id: \"R16-W3\"\n  summary: \"signal_reversal.pdf 存在于 figures/ 但未被任何 .tex 引用\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 24\n  resolution: \"Appendix L 已引用\"\n  resolution_round: 24\n\n- id: \"R19-W1\"\n  summary: \"缺少 penalty magnitude 的实际实验验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 24\n  resolution: \"P-invariance by design 论证逻辑覆盖\"\n  resolution_round: 24\n\n# =============================================\n# Round 27 — Active issues (new + recurring)\n# =============================================\n\n# --- Critical / Must-Fix ---\n\n- id: \"R27-N1\"\n  summary: \"正文超出 8 页限制——Conclusion 溢出到 page 9（R20-N1 复发）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 27\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"R20-N1 resolved: 正文收入 8 页\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Discussion 占满 page 8，Conclusion 3 行溢出到 page 9。格式违规，可能触发 desk reject。Technically trivial fix。\"\n  action_items:\n    - round: 27\n      action: \"压缩 Discussion 或 Related Work，将 Conclusion 收入 page 8\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N2\"\n  summary: \"DAF=90.4% 部分是 P=100 penalty 的数学必然，Abstract/Title framing 过度突出\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-N1: Abstract 以 label fraction 为 headline 但 §5 缺 penalty sensitivity 讨论\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] DAF=δP/(δP+Δ_nd) 随 P 单调递增。P=10→50.4%, P=5→35.4% (App K)。§2.4 承认数学后果但 Abstract 仍以 DAF 88-90% 为高亮。真正 penalty-independent 的是 label fraction 78.9%。\"\n  action_items:\n    - round: 27\n      action: \"Abstract/Conclusion 以 78.9% label fraction 为唯一 headline metric，DAF 降为 ScienceWorld-specific supplementary\"\n      assigned_to: main_agent\n      status: open\n    - round: 27\n      action: \"§5 Discussion 加独立段落讨论 penalty sensitivity + 引用 App K Table\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N3\"\n  summary: \"Deterministic strategy 实为 oracle access，跨环境含义不统一，oracle confound 未分离\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 27\n  mentions:\n    - round: 24\n      reviewers: []\n      note: \"R15-N2 resolved: §5.4 加交叉引用\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 三环境 deterministic 质性不同：ScienceWorld=oracle simulator, MATH=code interpreter, ALFWorld=admissible-action enumeration。仅脚注承认不足。Oracle→death asymmetry 接近 trivially expected（R1判断），但 R2 nuance: 78.9% all-from-death + Δ_nd=2.84 仅 9.6% 是 non-trivial observation。缺 intermediate 对照条件。\"\n  action_items:\n    - round: 27\n      action: \"§2.1 正文讨论 operationalization 差异（不仅脚注）；考虑 'privileged-information strategy' 替代术语\"\n      assigned_to: main_agent\n      status: open\n    - round: 27\n      action: \"§5 Discussion 讨论 oracle confound：App O grounding ablation 作为 partial intermediate evidence\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-N4\"\n  summary: \"环境覆盖过窄，generalization claims 超出证据——1 个主环境 + 2 个 boundary probes\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-W6: reframe 为 environment-specific mechanisms\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] ScienceWorld 11/30 tasks (37%)。MATH=null result（任何框架都得出无信号）。ALFWorld=唯一正面跨环境案例。Limitations 限定为 methodological generality 但 Abstract/Conclusion 措辞模糊。Cross-model (3x 7-9B) 在同环境内，非跨环境验证。\"\n  action_items:\n    - round: 27\n      action: \"Abstract 'illustrate applicability' → 'provide preliminary evidence'；明确区分 methodological vs empirical generality\"\n      assigned_to: main_agent\n      status: open\n    - round: 27\n      action: \"理想情况：增加一个 catastrophic-failure 环境 (NetHack/Crafter/WebArena) 的完整验证\"\n      assigned_to: main_agent\n      status: open\n\n# --- Warning / Should-Fix ---\n\n- id: \"R27-W1\"\n  summary: \"Router negative result framing: signal-limited vs data-limited 未区分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-W2: 标为 preliminary\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 90.5% majority class + 仅 9 个 internal-preferred samples。Any classifier collapses to majority prediction (App J: internal recall=0.0)。六种 variants 均失败（R1 补充 R2 未覆盖的 variants），但 data-limited 同样成立——需 ~1350 paired episodes 获得 50 internal-preferred。§3.6 framing 偏向 signal-limited。\"\n  action_items:\n    - round: 27\n      action: \"§3.6 明确区分两种解释 (signal-limited vs data-limited for minority class)，标为 preliminary\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W2\"\n  summary: \"Actionability 有限——诊断出问题但'然后怎么办'回答不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R25-W6: 未直接提及\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] App R decision framework 阈值是 ScienceWorld-specific。App O grounding ablation (death rate -19pp) 是可操作证据但被埋在 appendix。Discussion 缺 actionable next steps。\"\n  action_items:\n    - round: 27\n      action: \"§5 Discussion 增加 'Implications for Router Design' 段：f_death>75% 时转向 death prevention (action filtering etc)\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W3\"\n  summary: \"Episode→step distribution shift (pure→mixed strategy) 在 Method/Discussion 中讨论不充分\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] Limitations 提及 DAgger + compounding error，但 §2/§5 未讨论。Router negative result 可能部分由 distribution shift 导致（pure-strategy training → mixed-strategy deployment）。\"\n  action_items:\n    - round: 27\n      action: \"§5 或 §2.4 增加一段讨论 pure→mixed distribution shift 及其对框架实用性的影响\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W4\"\n  summary: \"Excluded tasks (63%) n=5 prescreening 样本量极小\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE with caveat] n=5 精确率不可靠 (CI ±43pp)，但方向一致性 18/19=95% 较稳健。Extended validation (App S, 5/19 tasks, n=20) 一致。Anti-cherry-picking claim 基于方向性而非精确率，站得住脚。\"\n  action_items:\n    - round: 27\n      action: \"Table 4 caption 或 §3 更 prominent 标注 n=5 限制\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W5\"\n  summary: \"K=11 cluster bootstrap: primary CI [81.1%, 99.0%] 可能 anti-conservative\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-W4: §3.1 caveat 需加强\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1 认为需在主文更明确标注 anti-conservative nature；R2 rebuts 认为论文已正确处理（降级为 sensitivity check）。最终：论文处理得当但可进一步加强。\"\n  action_items:\n    - round: 27\n      action: \"§3.1 考虑报告 clustered CI [73.3%, 100.0%] 作为 conservative bound alongside primary CI\"\n      assigned_to: main_agent\n      status: open\n\n- id: \"R27-W6\"\n  summary: \"Missing references: MoE routing (Switch Transformer, GShard), Neural Module Networks, counterfactual data augmentation (Kaushik 2020), process supervision\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"R2 发现。Agent routing/tool selection 覆盖充分，但缺 MoE routing 和 Neural Module Networks 上下文讨论，以及 counterfactual data augmentation 和 process vs outcome supervision 的联系。\"\n  action_items:\n    - round: 27\n      action: \"§4 Related Work 补充 MoE routing + Neural Module Networks 段落（2-3 句）\"\n      assigned_to: main_agent\n      status: open\n\n# --- Minor / Info ---\n\n- id: \"R27-M1\"\n  summary: \"Figure 2 r=0.97 是数学必然但 prominent 展示——建议降低 prominence\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R1: 移入 appendix。R2: 保留但缩小 + caption 首句标注 'internal consistency check'。折中方案合理。\"\n\n- id: \"R27-M2\"\n  summary: \"Abstract 信息密度过高（DAF + label fraction + 3 models + cross-env + pilot）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[AGREE x2] 聚焦核心发现，模型数量和 pilot 细节留给 Introduction\"\n\n- id: \"R27-M3\"\n  summary: \"术语不一致：catastrophic failure vs death 混用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"§1 用 catastrophic failure，§2 用 death，§3 交替。应统一。\"\n\n- id: \"R27-M4\"\n  summary: \"Appendix 体量偏高 (20 sections, ~13 pages vs 8 pages main)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2: 膨胀。R1: 分析论文需要，但 Algorithm 1 应移入正文 §2.3。共识：Algorithm 1 移入正文。\"\n\n- id: \"R27-M5\"\n  summary: \"小问题集合：vLLM 版本未在首次出现标注；Reflexion N=220 vs baseline N=245 未解释；Figure 3 denominator 不同；2026 引用可能是 preprints；Ng 1999 引用适用性\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"多个小问题汇总。vLLM 版本 [AGREE]；Reflexion N [AGREE]；Figure 3 denominator [AGREE]；2026 引用 [AGREE]；Ng 1999 [R2 REBUT: 适用]\"\n\n# --- Structural / Long-standing ---\n\n- id: \"R16-N1\"\n  summary: \"核心发现 novelty/excitement deficit——方向可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"Excitement 2.5。§5 Non-triviality 缓解但不消除。结构性限制。\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"Excitement 仍 2.5/5。§5 non-triviality 段存在且有效。方法概念简单（episode-level A/B testing）。结构性限制不可通过 writing fix 解决，Findings 定位已确定。\"\n\n- id: \"R19-N1\"\n  summary: \"Framing 内在张力：framework vs finding 定位不清\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R27 N2/N4 间接涉及。Abstract/Conclusion 在 methodological vs empirical generality 之间摇摆。\"\n\n- id: \"R26-N3\"\n  summary: \"'Contradicting the routing literature's implicit assumption' 是 strawman framing\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"'contradicting' → 'revealing that in catastrophic-failure environments, signal diversity can collapse'\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未直接提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 26\n      action: \"Abstract/Intro 'contradicting' → 'revealing...can collapse'\"\n      assigned_to: main_agent\n      status: in_progress\n\n- id: \"R26-W1\"\n  summary: \"框架方法论新颖性不足——未连接因果推断文献 Pearl/Rubin\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"§4 加段讨论 potential outcomes 关系\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未直接提及，可能已修复，待 Research Director 确认\"\n\n- id: \"R26-W3\"\n  summary: \"~50-episode pilot 缺 power analysis\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"'suffices' → 'provides preliminary signal given d=3.02'\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未直接提及，可能已修复，待 Research Director 确认\"\n\n- id: \"R26-W5\"\n  summary: \"Agent-floor tasks 对 death dominance 的含义未讨论\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"7 个 agent-floor tasks 代表 symmetric death regime\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未直接提及，可能已修复，待 Research Director 确认\"\n\n- id: \"R25-W5\"\n  summary: \"实验规模偏小（per-task n=20）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1]\n      note: \"R1 间接涉及（sample size concerns）。共识：aggregate 可靠，per-task 需谨慎。不 blocking。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 2271 · 2026-05-22T04:55:37.451876+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 24002}, \"error\": \"\"}"}

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

_source line 2272 · 2026-05-22T04:58:26.123838+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "report": "# Round 27 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作)\n**轮次**: 1 轮即收敛（关键问题全部达成共识）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，在构建 router 前诊断 LLM agent routing signal 的机制来源。框架对比 pure-strategy outcomes (internal-only vs deterministic-only)，将 routing signal 分解为机制组件。应用于 ScienceWorld (11 task types, 245 episodes) 发现：78.9% 的 non-tie routing labels 来源于 death asymmetry，DAF = 90.4% (P=100)。跨模型验证 (Qwen2.5-7B / Llama-3.1-8B / Gemma-2-9B) 显示 DAF 88-90% (spread 2.2pp)。Cross-environment probes (MATH: no signal; ALFWorld: information asymmetry, DAF=0%) 展示框架的鉴别力。Exploratory router (Qwen3 LoRA 0.6B-4B) 在 step-level balanced accuracy 56-59%，episode-level 仅 4B 超过 always-deterministic baseline。\n\n---\n\n## Strengths\n\n**S1. 方法论动机 well-grounded**：Per-step oracle comparison 在 sparse rewards 下退化（97.4% tie rate）的发现为 episode-level 框架提供了清晰的 motivation。框架三组件（labeling, DAF, SCI）各司其职，设计合理。[AGREE x2]\n\n**S2. 统计严谨性远超同类工作**：Bootstrap CI、cluster-robust tests、LOO sensitivity、wild cluster bootstrap、Cohen's d、exact permutation test——统计处理详尽。论文对自身统计局限性（K=11 clusters < 推荐 K≥20）的坦诚讨论尤其值得肯定。[AGREE x2]\n\n**S3. 跨模型一致性是 genuine empirical finding**：三个架构不同的 7-9B 模型在 DAF 88-90% 上收敛（spread 仅 2.2pp），有力说明 death dominance 是 environment property 而非 model-specific artifact。加上 72B scaling 验证，evidence 扎实。[AGREE x2]\n\n**S4. 自我批评意识在 NLP 论文中罕见**：20 个 appendix sections 覆盖了几乎所有潜在 weakness 的 robustness check。DAF 的数学依赖性、correlation 的 tautological nature、cluster bootstrap 的 reliability、excluded tasks 的 cherry-picking risk 均被主动标注。[AGREE x2]\n\n**S5. Intervention analysis 系统性强**：四个干预轴（retry, Reflexion, 10× scaling, action-space restriction）的 dose-response analysis 设计合理，Reflexion ceiling 发现有独立价值。Grounding ablation (App O) 提供了 causal evidence。[R1]\n\n**S6. Anti-cherry-picking 意识**：详细报告 task exclusion 理由 (App C Table)，excluded 19 tasks 的 ΔDR = +38.2pp 强于 included 11 tasks (+28.7pp)——排除偏向反方向。Extended validation (App S, 5/19 tasks, n=20) 进一步验证。[R2]\n\n**S7. Negative result 坦诚报告**：Router training 的失败（episode-level balanced accuracy 47.1%）被完整报告含详细 ablation，而非隐藏。这种透明度值得肯定。[AGREE x2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [AGREE x2] 正文超出 8 页限制（desk reject 风险）**\nSection 5 (Discussion) 占满 page 8，Section 6 (Conclusion) 溢出到 page 9 顶部。EMNLP 2026 规则限正文 8 页（Limitations/Ethics 不计入）。Conclusion 属正文，必须在 page 8 内结束。虽溢出量极小（约 3-5 行），仍构成格式违规。**这是 R20-N1 的复发**（曾在 R24 resolved）。\n→ 压缩 Discussion 或 Related Work，将 Conclusion 收入 page 8。Technically trivial。\n\n**N2. [AGREE x2] DAF=90.4% 部分是 penalty structure 的数学必然，framing 不匹配**\nDAF = δP/(δP + Δ_nd) 随 P 单调递增：P=100→90.4%, P=10→50.4%, P=5→35.4% (App K)。§2.4 诚实承认是\"数学后果而非实证发现\"，但 Abstract 仍以 \"DAF reaches 88-90% across three model families\" 为高亮数字，Title 以 \"Death Avoidance as the Dominant Routing Signal\" 为主打。读者第一印象会认为 90% 是环境无关的稳健数字。真正 penalty-independent 的发现是 label fraction (78.9%) 和 death rate differential (+26.5pp)。\n→ Abstract/Conclusion 以 78.9% label fraction 为唯一 headline metric；DAF 降为 ScienceWorld-specific 补充度量；§5 Discussion 加独立段落讨论 penalty sensitivity。\n\n**N3. [AGREE x2] \"Deterministic\" strategy 实为 oracle access，跨环境含义不统一**\n三个环境中 \"deterministic\" 操作化截然不同：ScienceWorld = oracle simulator (fork environment, ground-truth state)，MATH = code interpreter，ALFWorld = admissible-action enumeration。这不是同一概念的不同实例，而是质性不同的信息优势。仅在 §2.1 脚注承认不足。\n\n此外，在 ScienceWorld 的极端信息不对称下，\"oracle prevents death more often than hallucination-prone reasoning\" 接近 trivially expected（R1 判断）。但 R2 补充了重要 nuance：78.9% all-from-death 且 Δ_nd=2.84 仅占 Δ_full 的 9.6%——prior expectation 可能是 internal reasoning 在 non-death episodes 有独特优势，实际几乎不存在，这是 non-trivial observation。\n\n缺乏 intermediate 对照条件（partial oracle, noisy state feedback）来分离信息优势的边际贡献。App O grounding ablation 提供了 partial evidence（action-space filtering 降 death rate 19pp，但仍远高于 deterministic 的 16.3%）但被埋在 appendix。\n→ §2.1 正文讨论 operationalization 差异；考虑 \"privileged-information strategy\" 替代术语；§5 讨论 oracle confound + App O 证据提升。\n\n**N4. [AGREE x2] 环境覆盖过窄，generalization claims 超出证据**\n核心定量分析仅基于 ScienceWorld 11/30 task types (37%)。MATH 是 null result（任何框架都得出\"无信号\"结论，不验证框架能力）。ALFWorld 是唯一展示框架鉴别力的跨环境正面案例（DAF=0%, information asymmetry）。Cross-model (3x 7-9B) 在同一环境内进行，不等同于跨环境验证。\n\nLimitations 正确限定为 \"methodological generality\"（\"the diagnostic procedure applies to any environment with asymmetric fatal outcomes\"），但 Abstract (\"confirming convergence on a single dominant mechanism\") 和 Conclusion (\"Cross-environment probes illustrate applicability\") 措辞模糊了 methodological vs empirical generality。\n→ Abstract \"illustrate applicability\" → \"provide preliminary evidence\"；明确区分两种 generality；理想情况增加一个 catastrophic-failure 环境的完整验证。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [AGREE x2] Router negative result framing: \"signal-limited\" vs \"data-limited\" 未区分**\n训练数据 90.5% 是 deterministic-preferred (86/95)，internal-preferred 仅 9 例 (3.7%)。在此极端 class imbalance 下，任何 classifier 退化为 majority prediction 是预期结果（App J: internal recall = 0.0 at all scales）。论文测试了 6 种 variants（implicit/classification/generative router, LOTO, death-proximal labeling, guided with keyword leakage）均失败，为 convergent evidence。但 §3.6 framing 偏向 \"routing bottleneck is signal-limited, not architecture-limited\"——更准确的 framing 应区分：当前数据下 router 失败可能是 class imbalance 的预期结果；是否存在可学习的 step-level signal 仍是 open question（需 ~1,350 paired episodes 收集 50 个 internal-preferred）。\n→ §3.6 明确区分两种解释，标为 preliminary negative result。\n\n**W2. [AGREE x2] Actionability 有限**\n论文定位为 \"diagnostic rather than prescriptive\"（Limitations §5）。App R 的 Practitioner Decision Framework 阈值是 ScienceWorld-specific。App O 的 grounding ablation（action-space filtering 降 death rate 19pp）是 actionable evidence 但被埋在 appendix。Discussion 的 \"Practical implications\" 段更多是诊断描述而非 actionable next steps。\n→ §5 Discussion 增加 \"Implications for Router Design\" 段，将 App O 的 actionable insight 提升。\n\n**W3. [AGREE x2] Episode→step distribution shift 讨论不充分**\nPure-strategy training → mixed-strategy deployment 的 distribution shift 在 Limitations 中简短提及（DAgger citation），但 §2 Method 和 §5 Discussion 均未讨论。Router negative result 可能部分由 distribution shift 而非 signal absence 导致——在 pure-strategy trajectory 上训练的 router 部署在 mixed-strategy 上，state distribution 不同。\n→ §5 或 §2.4 增加一段讨论 distribution shift 对框架实用性的影响。\n\n**W4. [AGREE with caveat] Excluded tasks n=5 prescreening 样本量极小**\n19 个 excluded tasks 基于 n=5 prescreening。n=5 时 ΔDR=+40pp 的 95% CI ≈ ±43pp，精确率不可靠。但 anti-cherry-picking argument 基于方向一致性（18/19=95% 显示 positive death asymmetry）和 extended validation（App S, 5/19 tasks, n=20, mean ΔDR=+32.0pp），在当前证据下站得住脚。\n→ Table 4 caption 或 §3 更 prominent 标注 n=5 限制。\n\n**W5. [DIVERGENCE → 降为 info] Cluster bootstrap K=11**\nR1 认为 primary CI [81.1%, 99.0%] 可能 anti-conservative，应在主文更明确标注。R2 rebuts：论文已正确将 cluster bootstrap 降级为 sensitivity check（§3.1, App E），primary inference 基于 non-clustered episode-level bootstrap (B=10,000)。R2 的 rebuttal 有充分文本证据支持，论文处理得当。\n→ 可考虑在 §3.1 alongside 报告 clustered CI [73.3%, 100.0%] 作为 conservative bound。\n\n**W6. [R2] Missing references**\nRelated work 在 agent routing/tool selection 上覆盖充分（Toolformer, ART, Chameleon, CogRouter, ARES, MTRouter, RouteLLM 等）。但缺少：(a) MoE routing (Switch Transformer, GShard) 和 Neural Module Networks (Andreas et al., 2016) 作为 \"routing\" 的重要上下文；(b) counterfactual data augmentation (Kaushik et al., 2020)；(c) process supervision vs outcome supervision 的联系。\n→ §4 Related Work 补充 2-3 句。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致：\n\n| 问题 | 共识 | 严重性 |\n|------|------|--------|\n| 正文超 8 页（N1） | AGREE x2 | Critical (desk reject risk) |\n| DAF 数学依赖 vs framing (N2) | AGREE x2 | Critical |\n| Oracle/deterministic confound (N3) | AGREE x2 (R2 adds nuance) | Critical |\n| Generalization overclaim (N4) | AGREE x2 | Critical |\n| Router signal-limited vs data-limited (W1) | AGREE x2 | Warning |\n| Actionability 不足 (W2) | AGREE x2 | Warning |\n| Distribution shift 讨论缺失 (W3) | AGREE x2 | Warning |\n| Cross-model convergence 是 genuine finding | AGREE x2 | Strength |\n| 统计严谨性出色 | AGREE x2 | Strength |\n| 自我批评意识罕见 | AGREE x2 | Strength |\n| Excitement ≤ 2.5/5 | AGREE x2 | Structural limitation |\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判断 |\n|------|----|----|---------------|\n| Figure 2 (r=0.97) placement | 移入 appendix | 保留但降低 prominence | **采纳 R2 折中方案**：保留但缩小 + caption 首句标注 \"internal consistency check\" |\n| K=11 cluster bootstrap 严重性 | Warning (需在主文加强) | 论文已充分处理 | **采纳 R2**：论文处理得当，降为 info |\n| Appendix 体量 | 分析论文需要详尽 appendix | 过度膨胀 (1.6:1 比例) | **折中**：整体保留，但 Algorithm 1 应移入正文 §2.3（双方共识） |\n| Router 架构探索范围 | 6 种 variants 测试充分 | 仅 LoRA-tuned Qwen3 不够 | **采纳 R1**：6 种 variants 提供 convergent evidence；但 \"signal-limited\" 结论仍需 qualify |\n| \"Oracle prevents death\" 是否 trivially expected | 几乎 trivially expected | Non-trivial: Δ_nd=2.84 仅占 9.6% | **R2 nuance 有效**：oracle 更安全是 expected，但 non-death gap 几乎为零是 non-trivial |\n\n---\n\n## Questions（需要作者澄清）\n\n1. **Oracle confound 的可分离性**：如果使用一个 realistic 的 non-oracle deterministic strategy（如 action-space filtering, App O），DAF 会降到多少？能否从 App O 数据推算？\n2. **Router 的 data-limited 假说**：收集 ~1,350 paired episodes（当前 5.5× expansion）以获得 50 个 internal-preferred samples 的可行性如何？是否有 cost estimate？\n3. **72B 的 generalization**：Qwen2.5-72B 降低 death rate 但 \"does not eliminate death dominance\"——能否提供 72B 的完整 DAF decomposition 数字（正文仅有 30.6% death rate，无 DAF）？\n4. **Reflexion N=220 vs baseline N=245**：样本数差异的原因？\n5. **Figure 3 denominator**：72B baseline (all 11 tasks) vs retry/reflexion (10 death-prone tasks) 在同一图中，是否应统一 denominator？\n\n---\n\n## Missing References\n\n1. **MoE routing literature**: Switch Transformer (Fedus et al., 2022), GShard (Lepikhin et al., 2021) — \"routing\" 概念的重要上下文\n2. **Neural Module Networks**: Andreas et al. (2016) — modular computation routing 的经典工作\n3. **Counterfactual data augmentation**: Kaushik et al. (2020) — NLP 领域 counterfactual reasoning\n4. **Process supervision vs outcome supervision**: Lightman et al. (2023) — 与 step-level vs episode-level labeling 直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成** (2026-05-22 04:39 → 04:44, 约 5 分钟)\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | Page 9 | 主文延伸至第 9 页（Discussion 续写 + Conclusion），超出 8 页限制。与 N1 一致。 |\n| ⚠️ Warning | Pages 8-9 | 连续 2 页纯文本（Related Work → Discussion → Conclusion → Limitations），形成\"文字墙\"。建议加 display item 打破节奏。 |\n| ℹ️ Info | Pages 1-7 | 主文仅 5 个 display items（3 figure + 2 table），实证分析型论文偏少。 |\n| ℹ️ Info | Page 2 | Figure 1 流程图功能性足够但设计偏素（方框+箭头+纯色填充）。 |\n| ℹ️ Info | Page 20 | 附录 Figures 5/6/7 三图挤在同一页，Figure 6 文字极小接近可读性下限。 |\n| ℹ️ Info | Page 23 | 末页底部约 40% 空白。 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n### 维度打分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 2.5/5 | 2.5/5 | **2.5/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n### 综合判断\n\n论文提出了一个 sound 的 diagnostic framework，在 ScienceWorld 上做了 thorough 的分析，统计严谨性和自我批评意识远超同类工作。78.9% label fraction 和 cross-model convergence (DAF 88-90%, 2.2pp spread) 是 genuine empirical findings。\n\n但以下因素限制了评分：\n\n1. **核心定量发现 (DAF=90.4%) 部分受制于 penalty structure 的数学性质**——真正 penalty-independent 的发现被 DAF 数字遮蔽\n2. **\"Deterministic = oracle access\" 的 confound 未被充分分离**——需要 intermediate 对照条件\n3. **环境覆盖过窄**——单一主环境 + 两个 boundary probes (null + complementary) 不足以支撑 generalization claims\n4. **正文超出 8 页限制**——格式违规需修复（复发问题）\n5. **Excitement 受结构性限制**——方法概念相对 straightforward (episode-level A/B testing)，核心发现在 oracle access 下有一定可预期性\n\n**适合 Findings 接收**。如果作者能 (1) 修复页数问题，(2) 调整 DAF vs label fraction 的 framing 权重，(3) 精确化 generalization claims 措辞，(4) 充分讨论 oracle confound，论文可达到 **3.0-3.5 区间**（稳固 Findings 至 Borderline Conference）。距 Conference 接收 (4.0) 需要至少一个额外 catastrophic-failure 环境的完整验证。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度偏高——DAF + label fraction + 3 models + cross-env + pilot 在一段内\n- DAF 88-90% 作为 headline 数字的 framing 问题（N2）\n- \"confirming convergence on a single dominant mechanism\" 的 generality 措辞（N4）\n\n### §1 Introduction\n- Motivation (per-step oracle degeneracy) 清晰有力\n- Contribution 3 的跨环境 claim 需限定 scope\n- 2026 concurrent work 引用需标注 peer review 状态\n\n### §2 Method\n- Framework 三组件设计合理\n- §2.1 \"deterministic\" operationalization 仅在脚注讨论，不足（N3）\n- §2.4 DAF 推导清晰，penalty sensitivity 讨论在正确位置但后续 sections 未一致跟进\n- Algorithm 1 应从 App B 移入 §2.3\n\n### §3 Experiments\n- §3.1: DAF=90.4%, CI [81.1%, 99.0%] 报告完整；Figure 2 r=0.97 应降低 prominence\n- §3.2: Cross-model convergence (2.2pp spread) 是强结果；应限定 \"within 7-9B tier\"\n- §3.3: Intervention analysis 系统性好；Figure 3 denominator 不同需标注\n- §3.4: Cross-env probes 正确定位为 boundary probes；\"deterministic\" 不可比性需讨论\n- §3.6: Router negative result 的 signal-limited vs data-limited framing 问题（W1）\n\n### §4 Related Work\n- Agent routing/tool selection 覆盖充分\n- 缺 MoE routing、Neural Module Networks 上下文（W6）\n- Counterfactual RL 讨论到位\n\n### §5 Discussion\n- \"Why the router fails\" 段 informative\n- \"Non-triviality\" 段有效回应 obvious-in-hindsight 质疑\n- 缺 penalty sensitivity 讨论、oracle confound 讨论、actionable implications\n- 篇幅导致 Conclusion 溢出（N1）\n\n### §6 Conclusion\n- 仅 3 句话，极为简洁——但溢出到 page 9\n\n### Limitations\n- 5 段覆盖面广（environmental scope, methodology, statistics, pure-strategy bound, diagnostic scope）\n- 诚实且全面，但与 Limitations 不计入页数的规则配合，可考虑将部分 Discussion 内容移入 Limitations\n\n### Appendix (A-T, ~13 pages)\n- 体量偏高但每个 section 对应正文 specific claim\n- Algorithm 1 (App B) 应移入正文\n- App O grounding ablation 的 actionable findings 应在正文提升\n- App N failure mode taxonomy 的 single-annotator 限制已标注\n\n---\n\n## 修改优先级\n\n| 优先级 | 问题 | 工作量 |\n|--------|------|--------|\n| P0 (必须) | N1: 页数修复 | 小 (压缩 1-2 段) |\n| P0 (必须) | N2: DAF framing 调整 | 小 (措辞修改) |\n| P1 (强烈建议) | N3: Oracle confound 讨论 | 中 (§2.1 + §5 各加 1 段) |\n| P1 (强烈建议) | N4: Generalization 措辞精确化 | 小 (Abstract/Conclusion 措辞) |\n| P2 (建议) | W1: Router framing 调整 | 小 (§3.6 加 2-3 句) |\n| P2 (建议) | W2: Actionability → App O 提升 | 中 (§5 加 1 段) |\n| P2 (建议) | W3: Distribution shift 讨论 | 小 (§5 加 1 段) |\n| P3 (可选) | W4-W6, M1-M5 | 小 |\n\n---\n\n*报告由 Review Director 合成，基于 Reviewer 1 和 Reviewer 2 的独立审稿及交叉回应。*",
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
    "project": "simgate-modular-routing",
    "report": "# Round 27 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作)\n**轮次**: 1 轮即收敛（关键问题全部达成共识）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual diagnostic framework，在构建 router 前诊断 LLM agent routing signal 的机制来源。框架对比 pure-strategy outcomes (internal-only vs deterministic-only)，将 routing signal 分解为机制组件。应用于 ScienceWorld (11 task types, 245 episodes) 发现：78.9% 的 non-tie routing labels 来源于 death asymmetry，DAF = 90.4% (P=100)。跨模型验证 (Qwen2.5-7B / Llama-3.1-8B / Gemma-2-9B) 显示 DAF 88-90% (spread 2.2pp)。Cross-environment probes (MATH: no signal; ALFWorld: information asymmetry, DAF=0%) 展示框架的鉴别力。Exploratory router (Qwen3 LoRA 0.6B-4B) 在 step-level balanced accuracy 56-59%，episode-level 仅 4B 超过 always-deterministic baseline。\n\n---\n\n## Strengths\n\n**S1. 方法论动机 well-grounded**：Per-step oracle comparison 在 sparse rewards 下退化（97.4% tie rate）的发现为 episode-level 框架提供了清晰的 motivation。框架三组件（labeling, DAF, SCI）各司其职，设计合理。[AGREE x2]\n\n**S2. 统计严谨性远超同类工作**：Bootstrap CI、cluster-robust tests、LOO sensitivity、wild cluster bootstrap、Cohen's d、exact permutation test——统计处理详尽。论文对自身统计局限性（K=11 clusters < 推荐 K≥20）的坦诚讨论尤其值得肯定。[AGREE x2]\n\n**S3. 跨模型一致性是 genuine empirical finding**：三个架构不同的 7-9B 模型在 DAF 88-90% 上收敛（spread 仅 2.2pp），有力说明 death dominance 是 environment property 而非 model-specific artifact。加上 72B scaling 验证，evidence 扎实。[AGREE x2]\n\n**S4. 自我批评意识在 NLP 论文中罕见**：20 个 appendix sections 覆盖了几乎所有潜在 weakness 的 robustness check。DAF 的数学依赖性、correlation 的 tautological nature、cluster bootstrap 的 reliability、excluded tasks 的 cherry-picking risk 均被主动标注。[AGREE x2]\n\n**S5. Intervention analysis 系统性强**：四个干预轴（retry, Reflexion, 10× scaling, action-space restriction）的 dose-response analysis 设计合理，Reflexion ceiling 发现有独立价值。Grounding ablation (App O) 提供了 causal evidence。[R1]\n\n**S6. Anti-cherry-picking 意识**：详细报告 task exclusion 理由 (App C Table)，excluded 19 tasks 的 ΔDR = +38.2pp 强于 included 11 tasks (+28.7pp)——排除偏向反方向。Extended validation (App S, 5/19 tasks, n=20) 进一步验证。[R2]\n\n**S7. Negative result 坦诚报告**：Router training 的失败（episode-level balanced accuracy 47.1%）被完整报告含详细 ablation，而非隐藏。这种透明度值得肯定。[AGREE x2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [AGREE x2] 正文超出 8 页限制（desk reject 风险）**\nSection 5 (Discussion) 占满 page 8，Section 6 (Conclusion) 溢出到 page 9 顶部。EMNLP 2026 规则限正文 8 页（Limitations/Ethics 不计入）。Conclusion 属正文，必须在 page 8 内结束。虽溢出量极小（约 3-5 行），仍构成格式违规。**这是 R20-N1 的复发**（曾在 R24 resolved）。\n→ 压缩 Discussion 或 Related Work，将 Conclusion 收入 page 8。Technically trivial。\n\n**N2. [AGREE x2] DAF=90.4% 部分是 penalty structure 的数学必然，framing 不匹配**\nDAF = δP/(δP + Δ_nd) 随 P 单调递增：P=100→90.4%, P=10→50.4%, P=5→35.4% (App K)。§2.4 诚实承认是\"数学后果而非实证发现\"，但 Abstract 仍以 \"DAF reaches 88-90% across three model families\" 为高亮数字，Title 以 \"Death Avoidance as the Dominant Routing Signal\" 为主打。读者第一印象会认为 90% 是环境无关的稳健数字。真正 penalty-independent 的发现是 label fraction (78.9%) 和 death rate differential (+26.5pp)。\n→ Abstract/Conclusion 以 78.9% label fraction 为唯一 headline metric；DAF 降为 ScienceWorld-specific 补充度量；§5 Discussion 加独立段落讨论 penalty sensitivity。\n\n**N3. [AGREE x2] \"Deterministic\" strategy 实为 oracle access，跨环境含义不统一**\n三个环境中 \"deterministic\" 操作化截然不同：ScienceWorld = oracle simulator (fork environment, ground-truth state)，MATH = code interpreter，ALFWorld = admissible-action enumeration。这不是同一概念的不同实例，而是质性不同的信息优势。仅在 §2.1 脚注承认不足。\n\n此外，在 ScienceWorld 的极端信息不对称下，\"oracle prevents death more often than hallucination-prone reasoning\" 接近 trivially expected（R1 判断）。但 R2 补充了重要 nuance：78.9% all-from-death 且 Δ_nd=2.84 仅占 Δ_full 的 9.6%——prior expectation 可能是 internal reasoning 在 non-death episodes 有独特优势，实际几乎不存在，这是 non-trivial observation。\n\n缺乏 intermediate 对照条件（partial oracle, noisy state feedback）来分离信息优势的边际贡献。App O grounding ablation 提供了 partial evidence（action-space filtering 降 death rate 19pp，但仍远高于 deterministic 的 16.3%）但被埋在 appendix。\n→ §2.1 正文讨论 operationalization 差异；考虑 \"privileged-information strategy\" 替代术语；§5 讨论 oracle confound + App O 证据提升。\n\n**N4. [AGREE x2] 环境覆盖过窄，generalization claims 超出证据**\n核心定量分析仅基于 ScienceWorld 11/30 task types (37%)。MATH 是 null result（任何框架都得出\"无信号\"结论，不验证框架能力）。ALFWorld 是唯一展示框架鉴别力的跨环境正面案例（DAF=0%, information asymmetry）。Cross-model (3x 7-9B) 在同一环境内进行，不等同于跨环境验证。\n\nLimitations 正确限定为 \"methodological generality\"（\"the diagnostic procedure applies to any environment with asymmetric fatal outcomes\"），但 Abstract (\"confirming convergence on a single dominant mechanism\") 和 Conclusion (\"Cross-environment probes illustrate applicability\") 措辞模糊了 methodological vs empirical generality。\n→ Abstract \"illustrate applicability\" → \"provide preliminary evidence\"；明确区分两种 generality；理想情况增加一个 catastrophic-failure 环境的完整验证。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [AGREE x2] Router negative result framing: \"signal-limited\" vs \"data-limited\" 未区分**\n训练数据 90.5% 是 deterministic-preferred (86/95)，internal-preferred 仅 9 例 (3.7%)。在此极端 class imbalance 下，任何 classifier 退化为 majority prediction 是预期结果（App J: internal recall = 0.0 at all scales）。论文测试了 6 种 variants（implicit/classification/generative router, LOTO, death-proximal labeling, guided with keyword leakage）均失败，为 convergent evidence。但 §3.6 framing 偏向 \"routing bottleneck is signal-limited, not architecture-limited\"——更准确的 framing 应区分：当前数据下 router 失败可能是 class imbalance 的预期结果；是否存在可学习的 step-level signal 仍是 open question（需 ~1,350 paired episodes 收集 50 个 internal-preferred）。\n→ §3.6 明确区分两种解释，标为 preliminary negative result。\n\n**W2. [AGREE x2] Actionability 有限**\n论文定位为 \"diagnostic rather than prescriptive\"（Limitations §5）。App R 的 Practitioner Decision Framework 阈值是 ScienceWorld-specific。App O 的 grounding ablation（action-space filtering 降 death rate 19pp）是 actionable evidence 但被埋在 appendix。Discussion 的 \"Practical implications\" 段更多是诊断描述而非 actionable next steps。\n→ §5 Discussion 增加 \"Implications for Router Design\" 段，将 App O 的 actionable insight 提升。\n\n**W3. [AGREE x2] Episode→step distribution shift 讨论不充分**\nPure-strategy training → mixed-strategy deployment 的 distribution shift 在 Limitations 中简短提及（DAgger citation），但 §2 Method 和 §5 Discussion 均未讨论。Router negative result 可能部分由 distribution shift 而非 signal absence 导致——在 pure-strategy trajectory 上训练的 router 部署在 mixed-strategy 上，state distribution 不同。\n→ §5 或 §2.4 增加一段讨论 distribution shift 对框架实用性的影响。\n\n**W4. [AGREE with caveat] Excluded tasks n=5 prescreening 样本量极小**\n19 个 excluded tasks 基于 n=5 prescreening。n=5 时 ΔDR=+40pp 的 95% CI ≈ ±43pp，精确率不可靠。但 anti-cherry-picking argument 基于方向一致性（18/19=95% 显示 positive death asymmetry）和 extended validation（App S, 5/19 tasks, n=20, mean ΔDR=+32.0pp），在当前证据下站得住脚。\n→ Table 4 caption 或 §3 更 prominent 标注 n=5 限制。\n\n**W5. [DIVERGENCE → 降为 info] Cluster bootstrap K=11**\nR1 认为 primary CI [81.1%, 99.0%] 可能 anti-conservative，应在主文更明确标注。R2 rebuts：论文已正确将 cluster bootstrap 降级为 sensitivity check（§3.1, App E），primary inference 基于 non-clustered episode-level bootstrap (B=10,000)。R2 的 rebuttal 有充分文本证据支持，论文处理得当。\n→ 可考虑在 §3.1 alongside 报告 clustered CI [73.3%, 100.0%] 作为 conservative bound。\n\n**W6. [R2] Missing references**\nRelated work 在 agent routing/tool selection 上覆盖充分（Toolformer, ART, Chameleon, CogRouter, ARES, MTRouter, RouteLLM 等）。但缺少：(a) MoE routing (Switch Transformer, GShard) 和 Neural Module Networks (Andreas et al., 2016) 作为 \"routing\" 的重要上下文；(b) counterfactual data augmentation (Kaushik et al., 2020)；(c) process supervision vs outcome supervision 的联系。\n→ §4 Related Work 补充 2-3 句。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致：\n\n| 问题 | 共识 | 严重性 |\n|------|------|--------|\n| 正文超 8 页（N1） | AGREE x2 | Critical (desk reject risk) |\n| DAF 数学依赖 vs framing (N2) | AGREE x2 | Critical |\n| Oracle/deterministic confound (N3) | AGREE x2 (R2 adds nuance) | Critical |\n| Generalization overclaim (N4) | AGREE x2 | Critical |\n| Router signal-limited vs data-limited (W1) | AGREE x2 | Warning |\n| Actionability 不足 (W2) | AGREE x2 | Warning |\n| Distribution shift 讨论缺失 (W3) | AGREE x2 | Warning |\n| Cross-model convergence 是 genuine finding | AGREE x2 | Strength |\n| 统计严谨性出色 | AGREE x2 | Strength |\n| 自我批评意识罕见 | AGREE x2 | Strength |\n| Excitement ≤ 2.5/5 | AGREE x2 | Structural limitation |\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判断 |\n|------|----|----|---------------|\n| Figure 2 (r=0.97) placement | 移入 appendix | 保留但降低 prominence | **采纳 R2 折中方案**：保留但缩小 + caption 首句标注 \"internal consistency check\" |\n| K=11 cluster bootstrap 严重性 | Warning (需在主文加强) | 论文已充分处理 | **采纳 R2**：论文处理得当，降为 info |\n| Appendix 体量 | 分析论文需要详尽 appendix | 过度膨胀 (1.6:1 比例) | **折中**：整体保留，但 Algorithm 1 应移入正文 §2.3（双方共识） |\n| Router 架构探索范围 | 6 种 variants 测试充分 | 仅 LoRA-tuned Qwen3 不够 | **采纳 R1**：6 种 variants 提供 convergent evidence；但 \"signal-limited\" 结论仍需 qualify |\n| \"Oracle prevents death\" 是否 trivially expected | 几乎 trivially expected | Non-trivial: Δ_nd=2.84 仅占 9.6% | **R2 nuance 有效**：oracle 更安全是 expected，但 non-death gap 几乎为零是 non-trivial |\n\n---\n\n## Questions（需要作者澄清）\n\n1. **Oracle confound 的可分离性**：如果使用一个 realistic 的 non-oracle deterministic strategy（如 action-space filtering, App O），DAF 会降到多少？能否从 App O 数据推算？\n2. **Router 的 data-limited 假说**：收集 ~1,350 paired episodes（当前 5.5× expansion）以获得 50 个 internal-preferred samples 的可行性如何？是否有 cost estimate？\n3. **72B 的 generalization**：Qwen2.5-72B 降低 death rate 但 \"does not eliminate death dominance\"——能否提供 72B 的完整 DAF decomposition 数字（正文仅有 30.6% death rate，无 DAF）？\n4. **Reflexion N=220 vs baseline N=245**：样本数差异的原因？\n5. **Figure 3 denominator**：72B baseline (all 11 tasks) vs retry/reflexion (10 death-prone tasks) 在同一图中，是否应统一 denominator？\n\n---\n\n## Missing References\n\n1. **MoE routing literature**: Switch Transformer (Fedus et al., 2022), GShard (Lepikhin et al., 2021) — \"routing\" 概念的重要上下文\n2. **Neural Module Networks**: Andreas et al. (2016) — modular computation routing 的经典工作\n3. **Counterfactual data augmentation**: Kaushik et al. (2020) — NLP 领域 counterfactual reasoning\n4. **Process supervision vs outcome supervision**: Lightman et al. (2023) — 与 step-level vs episode-level labeling 直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成** (2026-05-22 04:39 → 04:44, 约 5 分钟)\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | Page 9 | 主文延伸至第 9 页（Discussion 续写 + Conclusion），超出 8 页限制。与 N1 一致。 |\n| ⚠️ Warning | Pages 8-9 | 连续 2 页纯文本（Related Work → Discussion → Conclusion → Limitations），形成\"文字墙\"。建议加 display item 打破节奏。 |\n| ℹ️ Info | Pages 1-7 | 主文仅 5 个 display items（3 figure + 2 table），实证分析型论文偏少。 |\n| ℹ️ Info | Page 2 | Figure 1 流程图功能性足够但设计偏素（方框+箭头+纯色填充）。 |\n| ℹ️ Info | Page 20 | 附录 Figures 5/6/7 三图挤在同一页，Figure 6 文字极小接近可读性下限。 |\n| ℹ️ Info | Page 23 | 末页底部约 40% 空白。 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n### 维度打分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 2.5/5 | 2.5/5 | **2.5/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n### 综合判断\n\n论文提出了一个 sound 的 diagnostic framework，在 ScienceWorld 上做了 thorough 的分析，统计严谨性和自我批评意识远超同类工作。78.9% label fraction 和 cross-model convergence (DAF 88-90%, 2.2pp spread) 是 genuine empirical findings。\n\n但以下因素限制了评分：\n\n1. **核心定量发现 (DAF=90.4%) 部分受制于 penalty structure 的数学性质**——真正 penalty-independent 的发现被 DAF 数字遮蔽\n2. **\"Deterministic = oracle access\" 的 confound 未被充分分离**——需要 intermediate 对照条件\n3. **环境覆盖过窄**——单一主环境 + 两个 boundary probes (null + complementary) 不足以支撑 generalization claims\n4. **正文超出 8 页限制**——格式违规需修复（复发问题）\n5. **Excitement 受结构性限制**——方法概念相对 straightforward (episode-level A/B testing)，核心发现在 oracle access 下有一定可预期性\n\n**适合 Findings 接收**。如果作者能 (1) 修复页数问题，(2) 调整 DAF vs label fraction 的 framing 权重，(3) 精确化 generalization claims 措辞，(4) 充分讨论 oracle confound，论文可达到 **3.0-3.5 区间**（稳固 Findings 至 Borderline Conference）。距 Conference 接收 (4.0) 需要至少一个额外 catastrophic-failure 环境的完整验证。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度偏高——DAF + label fraction + 3 models + cross-env + pilot 在一段内\n- DAF 88-90% 作为 headline 数字的 framing 问题（N2）\n- \"confirming convergence on a single dominant mechanism\" 的 generality 措辞（N4）\n\n### §1 Introduction\n- Motivation (per-step oracle degeneracy) 清晰有力\n- Contribution 3 的跨环境 claim 需限定 scope\n- 2026 concurrent work 引用需标注 peer review 状态\n\n### §2 Method\n- Framework 三组件设计合理\n- §2.1 \"deterministic\" operationalization 仅在脚注讨论，不足（N3）\n- §2.4 DAF 推导清晰，penalty sensitivity 讨论在正确位置但后续 sections 未一致跟进\n- Algorithm 1 应从 App B 移入 §2.3\n\n### §3 Experiments\n- §3.1: DAF=90.4%, CI [81.1%, 99.0%] 报告完整；Figure 2 r=0.97 应降低 prominence\n- §3.2: Cross-model convergence (2.2pp spread) 是强结果；应限定 \"within 7-9B tier\"\n- §3.3: Intervention analysis 系统性好；Figure 3 denominator 不同需标注\n- §3.4: Cross-env probes 正确定位为 boundary probes；\"deterministic\" 不可比性需讨论\n- §3.6: Router negative result 的 signal-limited vs data-limited framing 问题（W1）\n\n### §4 Related Work\n- Agent routing/tool selection 覆盖充分\n- 缺 MoE routing、Neural Module Networks 上下文（W6）\n- Counterfactual RL 讨论到位\n\n### §5 Discussion\n- \"Why the router fails\" 段 informative\n- \"Non-triviality\" 段有效回应 obvious-in-hindsight 质疑\n- 缺 penalty sensitivity 讨论、oracle confound 讨论、actionable implications\n- 篇幅导致 Conclusion 溢出（N1）\n\n### §6 Conclusion\n- 仅 3 句话，极为简洁——但溢出到 page 9\n\n### Limitations\n- 5 段覆盖面广（environmental scope, methodology, statistics, pure-strategy bound, diagnostic scope）\n- 诚实且全面，但与 Limitations 不计入页数的规则配合，可考虑将部分 Discussion 内容移入 Limitations\n\n### Appendix (A-T, ~13 pages)\n- 体量偏高但每个 section 对应正文 specific claim\n- Algorithm 1 (App B) 应移入正文\n- App O grounding ablation 的 actionable findings 应在正文提升\n- App N failure mode taxonomy 的 single-annotator 限制已标注\n\n---\n\n## 修改优先级\n\n| 优先级 | 问题 | 工作量 |\n|--------|------|--------|\n| P0 (必须) | N1: 页数修复 | 小 (压缩 1-2 段) |\n| P0 (必须) | N2: DAF framing 调整 | 小 (措辞修改) |\n| P1 (强烈建议) | N3: Oracle confound 讨论 | 中 (§2.1 + §5 各加 1 段) |\n| P1 (强烈建议) | N4: Generalization 措辞精确化 | 小 (Abstract/Conclusion 措辞) |\n| P2 (建议) | W1: Router framing 调整 | 小 (§3.6 加 2-3 句) |\n| P2 (建议) | W2: Actionability → App O 提升 | 中 (§5 加 1 段) |\n| P2 (建议) | W3: Distribution shift 讨论 | 小 (§5 加 1 段) |\n| P3 (可选) | W4-W6, M1-M5 | 小 |\n\n---\n\n*报告由 Review Director 合成，基于 Reviewer 1 和 Reviewer 2 的独立审稿及交叉回应。*",
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

_source line 2273 · 2026-05-22T04:58:30.191706+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4067
}
```

</details>

---


### Assistant

_source line 2274 · 2026-05-22T04:58:40.680623+00:00_

**Round 27 审稿完成。**

报告已投递至 Research Director。汇总：

**Overall: 3.0 (Findings)** | Soundness 3.5 | Excitement 2.5 | Reproducibility 4.0 | Confidence 4/5

**4 个 Must-Fix（全部 AGREE x2）：**
1. 正文超 8 页限制（Conclusion 溢出 page 9）—— desk reject 风险，复发问题
2. DAF=90.4% 是 P=100 的数学产物，framing 应以 78.9% label fraction 为主打
3. "Deterministic" = oracle access，跨环境含义不统一，confound 未分离
4. 环境覆盖过窄（1 个主环境 + 2 个 boundary probes），generalization 措辞过宽

**6 个 Should-Fix，5 个 Minor**

**主要优势：** 方法论 motivation 扎实、统计严谨性出色、跨模型 convergence 是 genuine finding、自我批评意识罕见、20 appendix 的 robustness 极为全面。

Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 189

## Round 189

2 recorded events


### User

_source line 2275 · 2026-05-22T04:58:43.275660+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 所有 Must-Fix (N1–N3) 和 Should-Fix (W1–W5) 的逐条交叉回应，已提交给 Director。

核心判断：
- **N1 (DAF penalty dependence)**: [AGREE]，补充了论文已有 label fraction 作为替代指标的优点
- **N2 (Oracle access)**: [AGREE with nuance]，区分了"oracle 更安全"（trivial）和"78.9% signal 来自 death gap"（non-trivial），并指出 App O grounding ablation 提供了部分 intermediate evidence
- **N3 (环境覆盖窄)**: [AGREE]
- **W1 (Cluster bootstrap)**: [REBUT]，论文已正确将其定位为 sensitivity check 而非 primary inference
- **W2 (n=5 prescreening)**: [AGREE with caveat]，方向一致性 + extended validation 使核心 claim 仍成立
- **W3 (Class imbalance)**: [AGREE]，论文混淆了 "signal-limited" 和 "data-limited for minority class"
- **W4 (r=0.97 移入 appendix)**: [REBUT]，建议保留但降低 prominence
- **W5 (Distribution shift)**: [AGREE]

两位 Reviewer 在 Overall 3.0 (Findings)、Soundness 3.5、Excitement 2.5 上完全一致。

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

_source line 2276 · 2026-05-22T04:58:50.687393+00:00_

审稿报告已在上一轮提交完成（Round 27，Overall 3.0 Findings），已投递至 Research Director。交叉分享也已全部完成（R1、R2 双向回应均已收集并纳入报告）。

本轮审稿流程已结束，无待处理事项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 190

## Round 190

50 recorded events


### User

_source line 2277 · 2026-05-22T08:45:06.633330+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Interpretability and Analysis
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

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

_source line 2278 · 2026-05-22T08:45:13.614405+00:00_

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

_source line 2279 · 2026-05-22T08:45:13.615286+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2280 · 2026-05-22T08:45:19.890499+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2281 · 2026-05-22T08:45:19.941189+00:00_



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

_source line 2282 · 2026-05-22T08:45:23.053887+00:00_

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

_source line 2283 · 2026-05-22T08:45:24.460923+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (121 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |\n| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gemma-scienceworld-gpu0** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.\n- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) ob
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool call

_source line 2284 · 2026-05-22T08:45:24.461420+00:00_

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

_source line 2285 · 2026-05-22T08:45:25.014778+00:00_

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
…[truncated 67045 chars]

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

_source line 2286 · 2026-05-22T08:45:25.065571+00:00_

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

_source line 2287 · 2026-05-22T08:45:30.436812+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found some relevant information about EMNLP 2026 and related submissions. Based on the s
…[truncated 1181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5371
}
```

</details>

---


### Tool call

_source line 2288 · 2026-05-22T08:45:38.474693+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit template anonymity"
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
    "query": "ACL Rolling Review 2026 submission guidelines page limit template anonymity"
  }
}
```

</details>

---


### Tool call

_source line 2289 · 2026-05-22T08:45:39.378312+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Budapest main conference call for papers commitment deadline"
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
    "query": "EMNLP 2026 Budapest main conference call for papers commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 2290 · 2026-05-22T08:45:39.579531+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
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
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2291 · 2026-05-22T08:45:43.996187+00:00_

Web search results for query: "EMNLP 2026 Budapest main conference call for papers commitment deadline"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here is the information about EMNLP 2026 in Budapest:

## Main Conference Details

EMNLP 2026 is being held in Budapest, Hungary on October 24 - 29, 2026.

## Call for Papers and Submission Deadlines

The EMNLP 2026 paper submission dea
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 4617
}
```

</details>

---


### Tool result

_source line 2292 · 2026-05-22T08:45:45.351791+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit template anonymity"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the search results, I found comprehensive information about ACL Rolling Review 2026 submission guidelines. Here are the key details:

## Page Limits

Long papers can be up to 8 pages and short papers up to 4 pages. Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references, and review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

## Template Requirements

Pape
…[truncated 872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6877
}
```

</details>

---


### Tool result

_source line 2293 · 2026-05-22T08:45:45.352294+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'config.yaml'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5772
}
```

</details>

---


### Tool call

_source line 2294 · 2026-05-22T08:45:49.268158+00:00_

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

_source line 2295 · 2026-05-22T08:45:49.469589+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2296 · 2026-05-22T08:45:49.520187+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for papers main conference"
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
    "query": "site:2026.emnlp.org call for papers main conference"
  }
}
```

</details>

---


### Tool result

_source line 2297 · 2026-05-22T08:45:55.443736+00:00_

Web search results for query: "site:2026.emnlp.org call for papers main conference"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"}]

I found the Call for Main Conference Papers for EMNLP 2026. Here's the key information:

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

Regarding submission requirements: Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

The 2026 Conference on Empirical Methods in Natural Language Processing 
…[truncated 190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5923
}
```

</details>

---


### Tool call

_source line 2298 · 2026-05-22T08:45:59.058577+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
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
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2299 · 2026-05-22T08:45:59.159341+00:00_

No matching deferred tools found

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

_source line 2300 · 2026-05-22T08:46:03.874094+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
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
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 2301 · 2026-05-22T08:46:04.026135+00:00_

&lt;persisted-output>
Output too large (66.6KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing--claude-sessions-review-director-19d7e797/fc7de88d-b287-4160-a1e3-a5b7f7e2aadb/tool-results/toolu_01HuKD2d9heEnhL7q7PaVYkh.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_9.md:156:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_8.md:102:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_16.md:170:未配置外部审稿（`external_review.paperreview_ai.enabled` 未启用）。无外部审稿结果。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_17.md:133:外部审稿：未配置（项目 config 中无 `external_review.paperreview_ai.enabled` 设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_12.md:139:外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_23.md:164:未请求（项目未配置 external_review.paperreview_ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_10.md:178:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, 
…[truncated 361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 2302 · 2026-05-22T08:46:12.009199+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
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
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2303 · 2026-05-22T08:46:12.411209+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2304 · 2026-05-22T08:46:12.411562+00:00_

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

_source line 2305 · 2026-05-22T08:46:12.462960+00:00_

1	# Round 27 Review Issues (fresh review, 2026-05-22)
2	# Two reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)
3	
4	# =============================================
5	# Carried-over resolved issues (from prior rounds)
6	# =============================================
7	
8	- id: "R13-W1"
9	  summary: "正文篇幅严重不足 long paper 要求"
10	  category: format
11	  severity: warning
12	  status: resolved
13	  first_raised_round: 13
14	  last_seen_round: 14
15	  resolution: "正文已扩展至 8 页"
16	  resolution_round: 14
17	
18	- id: "R13-W2"
19	  summary: "Router 训练实验存在多个 confound"
20	  category: experiment
21	  severity: warning
22	  status: resolved
23	  first_raised_round: 13
24	  last_seen_round: 15
25	  resolution: "1.7B dip 有可检验假说，augmentation 术语修正，N 统一"
26	  resolution_round: 15
27	
28	- id: "R13-W3"
29	  summary: "Episode-level label → step-level training 的 mislabeling 未被量化"
30	  category: method
31	  severity: info
32	  status: resolved
33	  first_raised_round: 13
34	  last_seen_round: 14
35	  resolution: "Limitations 和 Appendix B 已充分量化"
36	  resolution_round: 14
37	
38	- id: "R13-W4"
39	  summary: "SCI 方法贡献与实际使用不成比例"
40	  category: method
41	  severity: info
42	  status: resolved
43	  first_raised_round: 13
44	  last_seen_round: 14
45	  resolution: "SCI 已降级到 Appendix A"
46	  resolution_round: 14
47	
48	- id: "R13-W7"
49	  summary: "Router negative results 解释不完整"
50	  category: experiment
51	  severity: warning
52	  status: resolved
53	  first_raised_round: 13
54	  last_seen_round: 15
55	  resolution: "Router 实验定位为 diagnostic probe"
56	  resolution_round: 15
57	
58	- id: "R13-m2"
59	  summary: "Figure 3 仅含 ScienceWorld 和 MATH，缺少 ALFWorld"
60	  category: writing
61	  severity: warning
62	  status: resolved
63	  first_raised_round: 13
64	  last_seen_round: 16
65	  resolution: "Figure 3 已移除，数据在 Table 2 和正文中完整呈现"
66	  resolution_round: 16
67	
68	- id: "R13-m3"
69	  summary: "Reference 格式不统一 + orphan entries"
70	  category: format
71	  severity: info
72	  status: resolved
73	  first_raised_r
…[truncated 24144 chars]

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

_source line 2306 · 2026-05-22T08:46:18.036276+00:00_

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

_source line 2307 · 2026-05-22T08:46:18.538774+00:00_

1	\begin{abstract}
2	LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs.\ deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9\% of non-tie routing labels arise from death asymmetry---a finding replicated across three architecturally distinct 7--9B model families (spread 2.2\,pp), revealing that in catastrophic-failure environments, signal diversity can collapse to a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), providing preliminary evidence of applicability beyond death-dominated settings. The framework distinguishes \emph{methodological generality} (applicable to any environment with paired episode outcomes) from \emph{empirical generality} (full quantitative validation on ScienceWorld only). A ${\sim}$50-episode diagnostic pilot provides preliminary build-vs-buy signal given large effect sizes ($d = 3.02$); environments with smaller effects may require larger samples.
3	\end{abstract}
4	

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

_source line 2308 · 2026-05-22T08:46:18.589458+00:00_

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

_source line 2309 · 2026-05-22T08:46:19.041646+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \citep{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone, as the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated), while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \citep{toolformer-2023} inserts API calls by perplexity reduction; ART \citep{art-2023} decomposes tasks into tool-augmented programs; Chameleon \citep{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \citep{cogrouter-2026,ares-2026}, model tiers \citep{mtrouter-2026}, or episode-level model selection under sparse rewards \citep{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. These approaches, which operate in non-catastrophic settings, share the assumption that routing signal stems from diverse sources and a learned router can exploit it---an assumption that remains untested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under 
…[truncated 2672 chars]

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

_source line 2310 · 2026-05-22T08:46:19.042085+00:00_

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

_source line 2311 · 2026-05-22T08:46:19.293543+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
7	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
12	
13	\subsection{Problem Setup}
14	\label{sec:problem-setup}
15	
16	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), a privileged-information strategy that eliminates observation uncertainty---instantiated as oracle simulator (ScienceWorld), code interpreter (MATH), or admissible-action enumeration (ALFWorld); these qualitative differences affect what routing signals the framework can detect. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \math
…[truncated 7354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2312 · 2026-05-22T08:46:19.294057+00:00_

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

_source line 2313 · 2026-05-22T08:46:19.344802+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}). Prescreening used $n{=}5$ episodes per task type; directional consistency (18/19 types favoring deterministic) rather than point estimates drives the inclusion criterion.
5	
6	\subsection{Death Avoidance Decomposition}
7	\label{sec:death-decomp}
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=0.38\textwidth]{figures/fig1_daf_scatter.pdf}
12	\caption{Internal consistency check: per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$ (Spearman's $\rho = 0.986$; Appendix~\ref{app:per-task}), $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
13	\label{fig:decomposition}
14	\end{figure}
15	
16	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy
…[truncated 14899 chars]

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

_source line 2314 · 2026-05-22T08:46:23.861912+00:00_

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

_source line 2315 · 2026-05-22T08:46:24.314293+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	Self-supervised methods learn tool invocation from loss signals \citep{toolformer-2023,toolace-2025}, token-level methods embed tools in the vocabulary \citep{toolkengpt-2023}, task-level decomposition routes subtasks to specialized modules \citep{art-2023,chameleon-2023}, and RL-based methods learn routing from reward \citep{retool-2025}.
6	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Concurrent work examines \emph{when} to invoke tools: tool-call decisions correlate with uncertainty~\citep{tool-overuse-illusion-2026}, are encoded in hidden states~\citep{when2tool-2026}, impose a ``tool-use tax''~\citep{tool-use-tax-2026}, or follow necessity-utility-affordability logic~\citep{to-call-or-not-2026}. Our decomposition yields a concrete answer: 78.9\% of non-tie routing labels trace to catastrophic-failure prevention.
8	
9	\paragraph{Adaptive Computation and Routing.}
10	Adaptive routing traces back to learned halting policies \citep{graves2016act}. Mixture-of-Recursions \citep{mixture-of-recursions-2025} learns token-level recursion depths in the LLM era; concurrent work further diversifies routing granularity: CogRouter \citep{cogrouter-2026} adapts per-step depth, ARES \citep{ares-2026} selects effort levels, and MTRouter \citep{mtrouter-2026} addresses multi-turn settings.
11	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
12	Concurrently, \citet{budget-aware-routing-2026} train episode-level routing policies under sparse terminal rewards, the closest setting to ours; they optimize \emph{which} model to invoke, whereas we diagnose \emph{what} drives the routing decision.
13	Mixture-of-Experts architecture
…[truncated 2299 chars]

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

_source line 2316 · 2026-05-22T08:46:24.314837+00:00_

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

_source line 2317 · 2026-05-22T08:46:24.566220+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B, classification and generative) converge on near-chance step-level accuracy ($56$--$59\%$); this convergent failure suggests signal limitation, though extreme class imbalance (90.5\% deterministic-preferred, only 9 internal-preferred episodes) means a data-limited explanation remains viable---distinguishing these hypotheses requires ${\sim}$1{,}350 paired episodes to obtain 50 minority-class samples. Cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}). Training on pure-strategy labels but deploying under mixed-strategy routing also introduces a distribution shift~\citep{dagger-2011}; the negative result may partly reflect this train--deploy mismatch.
6	
7	\paragraph{Non-triviality and oracle confound.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), two consequences were not predictable a priori: $10{\times}$ scaling to 72B fails to eliminate it (DAF${}= 92.4\%$), and Reflexion yields DAF${}>100\%$. All four interventions leave ${\geq}12$~pp residual gaps (Appendix~\ref{sec:threshold-routing}); cross-model DR stability ($36$--$43\%$) confirms death vulnerability is a task-environment property. An oracle confound arises: is the signal merely ``use the oracle''? Two observations argue otherwise: (a)~$\Delta_{\text{nd}} = 2.84$ (9.6\% of the total gap)---on non-death episodes, internal reasoning provides almost no advantage; (b)~action-space filtering (Appendix~\ref{app:grounding-ablation}) reduces death rate by 19~pp but remains far above deterministic safety (16.3\%). The 7 excluded agent-floor tasks, where b
…[truncated 697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2318 · 2026-05-22T08:46:24.617142+00:00_

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

_source line 2319 · 2026-05-22T08:46:24.667832+00:00_

1	\section{Conclusion}
2	
3	In ScienceWorld, death avoidance alone accounts for 78.9\% of non-tie routing labels, replicated across three 7--9B model families (spread 2.2\,pp); our episode-level counterfactual framework diagnoses this before any router is built. Cross-environment probes provide preliminary evidence that the diagnostic procedure transfers; a ${\sim}$50-episode pilot provides preliminary build-vs-buy signal given large effect sizes ($d = 3.02$). Future work should validate death dominance in additional catastrophic-failure environments and develop routing methods that exploit task-type-level signals.
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

_source line 2320 · 2026-05-22T08:46:49.253149+00:00_

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

_source line 2321 · 2026-05-22T08:47:00.705406+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 11452
}
```

</details>

---


### Tool call

_source line 2322 · 2026-05-22T08:47:00.856521+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **Venue**: EMNLP 2026 (ARR May cycle), Interpretability and Analysis track\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper 正文 ≤8 页，参考文献不限；ACL 模板 [review] 模式；double-blind 匿名\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_28/submitted.pdf\n\n## 你的审查侧重\n\n1. **Counterfactual framework 设计**:\n   - Episode-level labeling 的有效性和局限性（Algorithm 1）\n   - DAF decomposition 的数学正确性和解释力\n   - Pure-strategy comparison 的假设是否合理\n\n2. **统计推断**:\n   - Bootstrap CI 和 cluster bootstrap 的适用性（K=11 task clusters）\n   - Per-task n=20 的统计功效\n   - 多重比较校正是否充分\n\n3. **实验设计**:\n   - 11/30 task types 选择的合理性和 selection bias 风险\n   - Cross-model validation（3 个 7-9B 模型 + 72B scaling）的充分性\n   - Router training 负结论的论证力度（signal-limited vs data-limited）\n   - Agent improvement baselines（Retry, Reflexion, 72B）的实验控制\n\n4. **格式检查**:\n   - 正文是否在 8 页以内\n   - 匿名性是否符合 double-blind 要求\n   - 参考文献格式\n\n请给出完整的审稿意见，包含 Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References，以及 Overall Assessment 评分。"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **Venue**: EMNLP 2026 (ARR May cycle), Interpretability and Analysis track\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper 正文 ≤8 页，参考文献不限；ACL 模板 [review] 模式；double-blind 匿名\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_28/submitted.pdf\n\n## 你的审查侧重\n\n1. **Counterfactual framework 设计**:\n   - Episode-level labeling 的有效性和局限性（Algorithm 1）\n   - DAF decomposition 的数学正确性和解释力\n   - Pure-strategy comparison 的假设是否合理\n\n2. **统计推断**:\n   - Bootstrap CI 和 cluster bootstrap 的适用性（K=11 task clusters）\n   - Per-task n=20 的统计功效\n   - 多重比较校正是否充分\n\n3. **实验设计**:\n   - 11/30 task types 选择的合理性和 selection bias 风险\n   - Cross-model validation（3 个 7-9B 模型 + 72B scaling）的充分性\n   - Router training 负结论的论证力度（signal-limited vs data-limited）\n   - Agent improvement baselines（Retry, Reflexion, 72B）的实验控制\n\n4. **格式检查**:\n   - 正文是否在 8 页以内\n   - 匿名性是否符合 double-blind 要求\n   - 参考文献格式\n\n请给出完整的审稿意见，包含 Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References，以及 Overall Assessment 评分。"
  }
}
```

</details>

---


### Tool result

_source line 2323 · 2026-05-22T08:47:09.776689+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 8920
}
```

</details>

---


### Tool call

_source line 2324 · 2026-05-22T08:47:09.927622+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **Venue**: EMNLP 2026 (ARR May cycle), Interpretability and Analysis track\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper 正文 ≤8 页，参考文献不限；ACL 模板 [review] 模式；double-blind 匿名\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_28/submitted.pdf\n\n## 你的审查侧重\n\n1. **新颖性评估**:\n   - Contribution 是否超越 \"obvious in hindsight\"\n   - Counterfactual diagnostic framework 的方法论贡献\n   - 相比 existing routing literature 的增量价值\n   - \"Interpretability and Analysis\" track 的适配度\n\n2. **完整性检查**:\n   - Cross-environment claims（MATH, ALFWorld）是否与证据匹配\n   - Methodological generality vs empirical generality 的区分是否清晰\n   - Limitations 覆盖是否充分\n   - Missing experiments 或 missing ablations\n\n3. **写作质量**:\n   - Abstract 信息密度和可读性\n   - Introduction framing: 问题动机是否令人信服\n   - 术语一致性（death vs catastrophic failure, modality vs computation mode 等）\n   - 数字/统计量的呈现是否清晰\n   - Related Work 覆盖度和 positioning\n\n4. **Missing References**:\n   - Safe RL, counterfactual reasoning, LLM agent routing 领域的遗漏\n\n请给出完整的审稿意见，包含 Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References，以及 Overall Assessment 评分。"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **Venue**: EMNLP 2026 (ARR May cycle), Interpretability and Analysis track\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper 正文 ≤8 页，参考文献不限；ACL 模板 [review] 模式；double-blind 匿名\n- **论文路径**: projects/simgate-modular-routing/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_round_28/submitted.pdf\n\n## 你的审查侧重\n\n1. **新颖性评估**:\n   - Contribution 是否超越 \"obvious in hindsight\"\n   - Counterfactual diagnostic framework 的方法论贡献\n   - 相比 existing routing literature 的增量价值\n   - \"Interpretability and Analysis\" track 的适配度\n\n2. **完整性检查**:\n   - Cross-environment claims（MATH, ALFWorld）是否与证据匹配\n   - Methodological generality vs empirical generality 的区分是否清晰\n   - Limitations 覆盖是否充分\n   - Missing experiments 或 missing ablations\n\n3. **写作质量**:\n   - Abstract 信息密度和可读性\n   - Introduction framing: 问题动机是否令人信服\n   - 术语一致性（death vs catastrophic failure, modality vs computation mode 等）\n   - 数字/统计量的呈现是否清晰\n   - Related Work 覆盖度和 positioning\n\n4. **Missing References**:\n   - Safe RL, counterfactual reasoning, LLM agent routing 领域的遗漏\n\n请给出完整的审稿意见，包含 Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References，以及 Overall Assessment 评分。"
  }
}
```

</details>

---


### Tool result

_source line 2325 · 2026-05-22T08:47:11.487310+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1559
}
```

</details>

---


### Assistant

_source line 2326 · 2026-05-22T08:47:24.944707+00:00_

已并行派发：
- ✅ 视觉审查 Agent（fire-and-forget）
- ✅ Reviewer 1（方法严谨性 + 实验设计）
- ✅ Reviewer 2（新颖性 + 完整性 + 写作质量）

等待两名 Reviewer 独立初审返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 191

## Round 191

2 recorded events


### User

_source line 2327 · 2026-05-22T08:52:03.256666+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 一篇方法论框架简洁、实证分析极其详尽的诊断型论文，核心发现（78.9% 路由标签源于死亡不对称）信息量充足，但框架概念简单度和单环境主体验证限制了影响力。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 (Strong) | 实验设计严谨，bootstrap CI / cluster-robust / LOO / cross-model 多重鲁棒性检验，统计局限性（K=11 cluster）诚实披露。唯一扣分点是 DAF 的数学必然性未在主文充分讨论。 |
| Excitement | 3/5 (Interesting) | "先诊断再建路由器"理念有价值，死亡主导发现对实践有指导意义，但框架本身概念简单（对比纯策略 episode 结果），单环境验证限制新颖性。 |
| Reproducibility | 4/5 | 完整 prompt 模板（Appendix T）、超参数表（Appendix I）、所有数据量/种子均有报告。代码和数据承诺 acceptance 后发布，尚未公开。 |
| Confidence | 4/5 | 仔细阅读全文及全部 20 个附录，LLM agent routing 和 counterfactual evaluation 在我的研究领域内。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DAF 的数学必然性与主文叙述存在张力
- 具体位置：§2.4 (Eq. 5)、§3.1、Abstract
- 问题：DAF = δP/(δP + Δ_nd)，当 P 远大于 Δ_nd 时 DAF → 1 是数学必然，而非实证发现。论文在 Appendix K 承认"this is a mathematical consequence of the decomposition, not evidence of mechanism robustness"，但主文和 Abstract 仍以"DAF = 90.4%"作为核心数字之一。Penalty sensitivity 分析（Table 8, Appendix K）显示 P=0 时 DAF 仅 7.4%，P=10 时 50.4%。这意味着 90.4% 这个数字在很大程度上是 ScienceWorld 特定 penalty 结构（P=100, max partial ≈ 100）的产物，而非一个可泛化的实证发现。虽然论文也报告了 penalty-independent 的 label fraction (78.9%)，但两个数字在主文中地位相当，读者容易误以为 DAF 本身是环境无关的鲁棒发现。
- 为什么影响接收：Analysis track 论文的核心价值在于 insight 的深度和精确性。当主要度量之一有数学必然性成分时，需要在主文——而不仅是 appendix——就这一点做更透明的讨论，否则读者可能高估 finding 的实证强度。
- 建议修改方向：（1）在 §2.4 定义 DAF 后立即加一段正文讨论其与 P 的数学关系以及为什么 label fraction 才是 primary finding；（2）考虑在 Abstract 和 Conclusion 中降低 DAF=90.4% 的突出度，以 penalty-independent label fraction 78.9% 为叙事主线。

**N2** [critical] "Deterministic" 在三个环境中含义截然不同，泛化 claim 需更谨慎
- 具体位置：§2.1 Problem Setup、§3.4 Cross-Environment Boundary Probes、Table 5 (Appendix L)
- 问题：在 ScienceWorld 中 "deterministic" = oracle simulator（ground-truth state access），在 MATH 中 = code interpreter，在 ALFWorld 中 = admissible-action enumeration。这三者在信息优势程度和机制上差异巨大。论文在 §2.1 最后一句提到了这些差异（"these qualitative differences affect what routing signals the framework can detect"），但在 cross-environment 结论中仍写"the diagnostic procedure transfers"（Conclusion）。当"deterministic"语义在环境间不可比时，"framework transfers"这个 claim 的含义需要更精确限定——转移的是 procedure（收集 paired episodes 并 decompose），而不是 operationalization（什么算"deterministic"需要每个环境重新定义）。
- 为什么影响接收：如果不严格区分 procedure transferability 和 operationalization consistency，reviewers 和读者可能期望比论文实际提供的更强的泛化性。
- 建议修改方向：在 §3.4 开头或 §2.1 中增加一段明确说明：cross-environment probes 验证的是 diagnostic procedure 的可复用性，不是"deterministic computation"概念的一致性；每个环境需要独立定义何为"deterministic baseline"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 63% task type 排除率需在主文更充分 justify
- 具体位置：§3 Experiments 第一段
- 问题：30 个 task type 中排除 19 个（63%），仅在 11 个上做完整分析。虽然 anti-cherry-picking 分析（Appendix C, Table 2）显示排除 tasks 的 ΔDR 更高（+38.2 vs +28.7 pp），extended validation（Appendix S）也确认了方向，但主文只用一句话带过（"the 19 excluded types (63%) lack actionable routing signal due to..."）。对于一篇 analysis 论文，分析对象的代表性是关键——63% 排除率加上三种不同排除原因（dev set 5, redundancy 7, agent floor 7）值得在主文多花一段讨论，而不是全部推到 appendix。
- 建议：在 §3 增加一小段，说明排除 tasks 中 death dominance 更强（Table 2 key numbers），让读者无需翻 appendix 即可确信选择无偏。

**W2** [warning] 路由器负面结果的 alternative explanations 未充分排除
- 具体位置：§3.6、§5 Discussion paragraph 1
- 问题：论文将路由器失败解读为"routing signal is task-type-level binary, no step-level signal exists"（Interpretation B）。但 internal-preferred 样本极少（9/245 = 3.7%），augmentation 只是 paraphrase 而非真实新 episode，且仅测试了 Qwen3 系列（0.6B-4B）。在数据如此极端不平衡、minority class 仅 9 个真实样本的情况下，router 失败可能只是数据不足的表现（Interpretation A 的一个变体），而非信号不存在。论文在 Discussion 中提到需要~1,350 paired episodes 来获得 50 个 minority samples，但又说"diminishing return on a 9.6% signal"——这两句之间有张力：如果数据不足以排除 Interpretation A，就不应过于确信 Interpretation B。
- 建议：在 §3.6 或 §5 中更对称地呈现两种解释的证据和局限，明确说当前数据量不足以区分 A 和 B。

**W3** [warning] Limitations 章节过长
- 具体位置：page 9, Limitations section
- 问题：Limitations 有 5 个段落，篇幅近一整页。根据 EMNLP 2026 指南，Limitations "do not count towards this page limit, provided they do not contain excessive additional content"。当前写法更像是一个完整的 discussion extension 而非标准 limitations。这本身不影响审稿决定，但过长的 limitations 可能引起其他 reviewer 注意。
- 建议：将 Limitations 压缩到 3 个核心点（environmental scope, methodological constraints, statistical limitations），将 pure-strategy upper bound 和 diagnostic scope 合并或简化。

**W4** [warning] 缺少与同期路由方法的直接比较
- 具体位置：§4 Related Work
- 问题：论文在 Related Work 中引用了 CogRouter、ARES、MTRouter、budget-aware routing 等同期工作，但没有实证比较。虽然论文的定位是 diagnostic framework 而非路由方法，但至少可以定性讨论：这些方法在 ScienceWorld 这类 death-dominated 环境中是否会遇到同样的 signal collapse 问题？这会加强论文的 practical significance。
- 建议：在 §5 Discussion 中增加一段，讨论这些 concurrent routing methods 在 death-dominated 环境中的预期表现（可以是定性分析，不需要实验）。

**W5** [warning] "Death" 术语可能限制 generality perception
- 具体位置：全文
- 问题：论文标题和核心术语是 "death avoidance"，这在 ScienceWorld 中有明确的操作定义（score = -100），但在更一般的 interactive environments 中，"death" 未必是一个通用概念。论文在 Limitations 提到"environments with softer penalties would exhibit lower DAF values"，但更根本的问题是：如果一个环境没有 binary catastrophic failure（比如只有 graded penalties），整个 DAF framework 的适用性如何？
- 建议：在 §2.4 或 Discussion 中增加 1-2 句话讨论：当 failure 不是 binary（death/alive）而是 graded 时，framework 如何调整或是否仍然适用。

---

## 小问题（不影响接收）

- §1 Introduction: "signal diversity can collapse to a single dominant mechanism" 出现两次（§1 para 5 和 contributions list item 2），措辞几乎相同。可压缩。
- §2.2: "Under sparse terminal rewards, this approach degenerates" — "degenerates" 用词不太常见于此语境，建议改为 "fails" 或 "yields no signal"。
- Figure 2 (§3.1): scatter plot 只有 11 个点（11 task types），r=0.97 在 n=11 时可视化效果有限，且论文自己说"the near-perfect correlation is a structural consequence of death dominance, not an independent finding"。建议在 figure caption 中加上这个 caveat（目前只在 caption 最后一句间接提到）。
- Table 2 (§3.5 Baselines): "Trained Router†" 只用 1 个 seed (42)，注释说了 8-seed analysis 在 appendix，但主文 table 的单 seed 结果可能误导。
- Algorithm 1 (Appendix B): 行 9-10 的注释 "death asymmetry" 出现两次（分别标注 det-pref 和 int-pref 的 case），但两个 case 方向不同——建议改为 "death asymmetry → det" 和 "death asymmetry → int" 以区分。
- References: arXiv preprints 占比较高（37 条中约 14 条是 arXiv），尤其是 2026 年的 concurrent work。这在快节奏领域可以接受但值得注意。
- §3.2 最后一句："sliding window attention, vs. full attention in Qwen/Llama" — 这个 architectural difference 是 Gemma-2 相对于 Qwen/Llama 的主要区分特征吗？对于 9B 级别模型，还有其他重要差异（训练数据、tokenizer 等）。

---

## Missing References

1. **Shielding in Safe RL**: Alshiekh et al., "Safe Reinforcement Learning via Shielding" (AAAI 2018) — 直接相关于 Appendix O 的 action-space filtering 消融实验（blocking "focus on" actions 本质上是一个简化版 shield）
2. **LLM agent failure taxonomy**: Pan et al., "Do LLMs Generate Structurally Diverse Failures? A Comprehensive Study" (2024) — 相关于 Appendix N 的 failure mode analysis
3. **Reward shaping in sparse environments**: Ng et al. 1999 已引用，但 Devlin & Kudenko, "Dynamic Potential-Based Reward Shaping" (AAMAS 2012) 也相关——dense reward shaping 可能改变 death 主导的格局
4. **Selective prediction / abstention**: Geifman & El-Yaniv, "Selective Classification for Deep Neural Networks" (NeurIPS 2017) — 与 §5 Discussion 中"always-deterministic as selective quitting"的讨论相关（论文已引 Bonagiri et al. 2025 但缺少 selective prediction 的经典文献）
5. **Concurrent work**: AppAgent (Zhang et al., 2024) 和 OS-Copilot (Wu et al., 2024) 等 interactive agent 系统可能展现不同于 ScienceWorld 的 routing signal 结构

---

## 主要优势

1. **极其详尽的鲁棒性验证**：20 个 appendix 覆盖了我能想到的几乎所有 robustness 检验（LOO、cluster bootstrap、wild bootstrap、penalty sensitivity、cross-model、cross-environment、capacity scaling、augmentation ablation 等）。这是我见过的分析型论文中最彻底的检验之一。
2. **诚实的负面结果报告**：路由器训练失败（episode-level balanced accuracy 47.1% < 50% chance）被完整报告而非隐藏，且提供了两种可能的解释。这在 agent 领域的论文中难得。
3. **Penalty-independent 与 penalty-dependent 度量的双轨报告**：论文区分了 label fraction (78.9%, penalty-independent) 和 DAF (90.4%, penalty-dependent)，并在 appendix 中展示了 DAF 随 P 变化的完整曲线。这种透明度值得肯定。
4. **Cross-model convergence**：三个架构差异显著的模型家族（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B-it）给出 DAF 88-90% (spread 2.2 pp)，加上 72B 的 92.4%，有力地排除了模型特异性解释。
5. **Track fit 优秀**：作为 Interpretability and Analysis track 的投稿，"先诊断 routing signal 的组成再决定是否训练 router"的理念与 track 定位高度匹配。
6. **写作质量整体较高**：论文结构清晰，从 framework 定义（§2）到 ScienceWorld 主实验（§3.1-3.3）到 intervention（§3.4-3.5）到 router diagnostic（§3.6）的叙事逻辑连贯。

---

**Reviewer 2 审稿完成。**

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

_source line 2328 · 2026-05-22T08:52:10.073486+00:00_

Reviewer 2 审稿意见已收到（3.5 Borderline Conference）。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 192

## Round 192

2 recorded events


### User

_source line 2329 · 2026-05-22T08:52:21.992714+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要**：Overall 3.5 (Borderline Conference)。Soundness 4/5，Excitement 3/5。

核心判断：论文提出了一个概念简洁的 episode-level counterfactual 诊断框架，发现 ScienceWorld 中 78.9% 路由标签源于死亡不对称——实证分析极其详尽（20 个 appendix），cross-model 验证（3 个模型家族 DAF 88-90%）和负面结果报告（router failure）都很诚实。两个 Must-Fix：(1) DAF=90.4% 有数学必然性成分但主文未充分讨论；(2) "deterministic" 在三个环境中语义不同，cross-environment transfer claim 需更精确限定。

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

_source line 2330 · 2026-05-22T08:52:29.514500+00:00_

Reviewer 2 审稿意见已收到（3.5 Borderline Conference）。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 193

## Round 193

6 recorded events


### User

_source line 2331 · 2026-05-22T08:53:14.141608+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 方法论严谨、实验充分的诊断分析论文，核心发现（death avoidance 主导 routing signal）在 ScienceWorld 内得到了有力论证，但 episode-level 到 step-level 的推断存在根本性张力，且 DAF 度量的 P-dependence 削弱了跨环境比较力，泛化性受限。

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 框架设计合理，统计方法多层验证，但 episode→step 推断有粒度失配，DAF 随 P 单调递增削弱了绝对数值的解释力 |
| Excitement | 3/5 | 定量诊断路由信号的视角有价值，router training 负结论有实践启示，但核心发现在有 catastrophic failure 的环境中具有一定的可预测性 |
| Reproducibility | 4/5 | 实验细节充分（Algorithm 1, Appendix T 的 prompt templates, 超参数），承诺代码公开，ScienceWorld 为公开平台 |
| Overall Assessment | 3.5/5 | Borderline Conference — 分析严谨且诚实，但 insight 的通用性和 novelty 尚不足以支持 main conference 强推荐 |
| Confidence | 4/5 | 仔细阅读全文和 24 页附录，对实验设计和统计方法有充分了解 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Episode-level labeling 与 step-level routing 之间的粒度失配未被充分讨论，核心 claim 的适用范围被高估

- 具体位置：§2.2–§2.3 (Algorithm 1), §3.3, §5 (Discussion), Limitations (p9)
- 问题：论文的核心 claim 是 "78.9% of non-tie routing labels arise from death asymmetry"（§3.1），但 Algorithm 1 的 labeling 是 episode-level 的：一整个 episode 只得到一个 label（det-pref, int-pref, no-pref）。然而实际 routing 是 per-step 决策。论文在 §3.3 承认 "Episode labels thus apply correct direction to uninformative steps—a granularity mismatch, not label error"，并在 §5 讨论 router failure 时再次提及。但论文的 **title** 和 **abstract** 都表述为 "Death Avoidance as the Dominant Routing Signal"，暗示这是一个关于 routing decision 的通用发现，而非仅限于 episode-level outcome 的观察。实际上，95 个 non-tie labels 中的 75 个来自 death asymmetry，但这 95 个 label 覆盖的是 245 个 episode 中 38.8% 的子集——另外 61.2% 的 episode 是 no_pref（两个策略表现相同）。在 step level，97.4% 的 step 是 uninformative（§2.3），真正有 routing signal 的 step 极少。论文需要更清晰地界定 claim 的 scope：这是一个关于 **episode-level outcome** 的发现，而非关于 **per-step routing decision** 的发现。
- 为什么影响接收：标题和 abstract 的表述与 methodology 的实际覆盖范围之间的 gap 可能误导读者，且削弱了论文对 practical routing system 设计的指导价值。
- 建议修改方向：(1) 在 abstract 和 introduction 中明确 "episode-level" 限定词；(2) 在 §5 Discussion 增加一段讨论：如果存在有效的 step-level routing signal 但被 episode-level aggregation 掩盖了，当前框架是否能检测到？(3) 考虑将 title 改为更精确的表述。

**N2** [critical] DAF 度量的 P-dependence 使得跨环境比较和绝对数值缺乏稳健性

- 具体位置：§2.4 (Eq. 5), Appendix K (Penalty Sensitivity)
- 问题：DAF = Δ_death / δ^P，其中 Δ_death 随 penalty P 单调递增（Appendix K: "As P increases, Δ_death grows (16.33 at P=50, 29.60 at P=100)... while Δ_nd remains fixed, mechanically increasing DAF"）。论文报告 DAF = 90.4% 是在 P=100（ScienceWorld 默认值）下的结果。但如果 P=50，DAF 会显著降低；如果 P=200，DAF 会更高。这意味着 DAF 的绝对数值（90.4%）并非环境特性的内禀度量，而是部分由 penalty magnitude 决定的。虽然论文同时报告了 P-invariant 的 label fraction（78.9%），但 DAF 是论文名称的核心概念之一（"Death Avoidance Factor"），其 P-dependence 在正文中没有足够讨论——读者必须读到 Appendix K 才能了解。
- 为什么影响接收：核心度量的 P-dependence 削弱了论文 claim 的 robustness。在 ALFWorld（无显式 death penalty）和 MATH（无 death mechanism）的 cross-environment 对比中（§3.4），DAF 的可比性不明确。
- 建议修改方向：(1) 在 §2.4 正文中明确讨论 DAF 的 P-dependence，而非仅在 Appendix K；(2) 将 label fraction（78.9%）作为 primary metric，DAF 作为 secondary metric；(3) 报告 DAF 在不同 P 值下的数值（至少 P=50, 100, 200），或推导 P-normalized 版本的 DAF。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] K=11 cluster bootstrap 处于文献推荐下限，标准误可能被低估

- 具体位置：§3.1 (Statistical inference), Appendix E (Table 6)
- 问题：论文使用 cluster bootstrap（以 11 个 task type 为 cluster）来计算 confidence interval 和 p-value。Cameron et al. (2008)（论文引用的方法来源）建议 K ≥ 20–50 以获得可靠的 bootstrap 标准误。K=11 时 bootstrap 可能低估标准误，尤其当 cluster 间方差较大时。论文在 Table 6 中展示了三种方法（cluster bootstrap, wild cluster bootstrap, exact permutation）的 p-value 均 < 0.01，且一致性较好——这一定程度上缓解了 concern。但 wild cluster bootstrap（K=11, p < 0.001）本身在 K 较小时也可能 over-reject（Webb, 2023 的 finite-sample 修正并未在论文中详述）。
- 建议：(1) 在正文或附录中讨论 K=11 作为 cluster bootstrap 最低限的局限性；(2) 报告 Cameron et al. (2008) 推荐的 K 阈值，并解释为何 K=11 在此场景下仍可接受（例如极大的 effect size Cohen's d = 3.02）；(3) 考虑补充 jackknife 或 permutation-based CI 作为 robustness check。

**W2** [warning] 11/30 task type 的选择虽有合理标准，但 63% 排除率带来 selection bias 风险

- 具体位置：§3 (Experiments, para 1), Table 4, Appendix C
- 问题：论文排除 19/30 task types，排除标准为：pipeline development (5), taxonomically redundant (7), near-zero progress (7)。Table 4 显示排除的 task 的 death dominance 更强（mean Δ_DR > included），论文以此论证排除不是 cherry-picking。但 63% 的排除率仍然很高。Near-zero progress 的 7 个 task 被排除意味着框架只能分析"至少有一个策略能取得一定进展"的 task，这是一个不平凡的前提条件。Taxonomic redundancy 的判断标准也缺少形式化定义——"a development set excluded to prevent circular evaluation; B = taxonomically redundant with an included family representative" 在 Table 4 中给出但缺乏具体标准。
- 建议：(1) 在正文中给出 taxonomic redundancy 的操作定义（什么算 "same family"）；(2) 在 Table 4 中加入 excluded task 的 DAF 数值（而非仅 label fraction），以完整展示 selection 的影响；(3) 讨论 near-zero progress task 被排除对 claim 泛化性的影响——在这些 task 上是否有 routing signal？

**W3** [warning] Router training 负结论的论证力度受限于 router 架构的简单性

- 具体位置：§3.6 (Router Training), Appendix I (Table 9-11)
- 问题：论文使用 Qwen3-1.7B + LoRA 的简单分类架构进行 router training（Appendix I）。Step-level balanced accuracy 54.1 ± 5.4%，episode-level 47.1 ± 2.2%，结论是 "signal-limited"。论文通过 text augmentation ablation（Table 11, 25%→800%）排除了 data-limited 解释。但以下方面未被探索：(a) 使用 observation history（而非单步 observation）作为 router 输入；(b) 使用 task-type 信息作为额外特征；(c) 更强的 router backbone（如 7B 模型）。论文的结论是 "the routing problem is trivially solved by always choosing deterministic"（§5），但这可能只意味着 episode-level binary signal 无法被单步分类器捕获，而非 routing 本质上不可学习。
- 建议：(1) 在 Discussion 中明确 router training 负结论的 scope：当前 architecture under episode-level labels 无法学到 signal，而非 routing 本身不可学；(2) 讨论 history-aware router 或 task-conditioned router 是否可能绕过这一限制。

**W4** [warning] Cross-model validation 仅覆盖 7–9B 模型级别，72B 仅做 scaling probe 而非完整 replication

- 具体位置：§3.2 (Multi-Model Validation), §3.3 (Agent Improvement), Appendix M
- 问题：三个 7–9B 模型（Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B）的 cross-model replication 令人信服（Table 16-17, DAF 均 > 80%）。但 72B scaling（§3.3, Table 18-19）仅作为 intervention axis 而非完整 replication：72B 的 DAF=92.1% 是在 255 episodes（与 7B 相同 task set）上的单次实验。论文未在 72B 上运行 router training 或 signal concentration 分析。对于 routing 研究，模型能力是关键变量——更强模型的 death rate 更低（42.9%→30.6%），这可能使 non-death signal 更 prominent。Appendix Q（Threshold Routing）在 72B 上的分析也仅限于 single task oracle 设置。
- 建议：(1) 在 Limitations 中明确说明 72B 实验的 scope 限制；(2) 如果资源允许，补充 72B 的 SCI 和 router training 分析；(3) 讨论在 death rate 更低的条件下（如 72B 或更强模型），non-death signal 是否可能超过 death signal。

---

## 小问题（不影响接收）

- **M1** [minor] Figure 2 (p4) 的 scatter plot 标题说 "per-task scatter"，但仅有 11 个点且 task 名称未标注，可读性有限。建议加 task name label 或在 caption 中列出对应关系。
- **M2** [minor] Eq. 4 (§2.4) 的 decomposition 公式中，Δ_death 的精确定义依赖于 Appendix 才能完全理解（正文仅给出近似表述）。建议在正文中给出完整公式或至少说明近似的量级。
- **M3** [minor] §3.4 ALFWorld 分析（p6）仅用一段话描述，没有对应的 table 或 figure。鉴于这是 cross-environment validation 的重要组成部分，建议至少在 Appendix 中补充 ALFWorld 的 per-task DAF 表（目前 Appendix L 只有 cross-environment label distribution Figure 4/14）。
- **M4** [minor] Table 1 (p5) 的 caption 中 "Top" 和 "Bottom" 的对比意图不够直观——需要阅读 footnote 才能理解 10 death-prone tasks 是另一个分析子集。
- **M5** [minor] Limitations section（p9）中 "Statistical limitations" 提到 "K = 11 task-type clusters yield wide CIs"，但未提及 Cameron et al. (2008) 对 K 的建议。这与 W1 关联——应在此处补充。
- **M6** [minor] 论文在 Related Work (§4) 中没有讨论 routing/computation allocation 在 non-agent 场景下的工作（如 early exit, speculative decoding, adaptive computation），这些工作也涉及 "何时使用更多计算" 的决策，可以丰富上下文。

---

## Questions to Authors

**Q1**: 如果在 ScienceWorld 中将 death penalty 从 P=100 降低到 P=10（使其与典型 non-death score gap 同量级），episode-level labeling 会产生什么样的 label distribution？此时 78.9% 的 death-asymmetric label fraction 是否仍然成立？（这可以验证 death dominance 是否是 penalty structure 的 artifact 而非环境动力学的本质。）

**Q2**: 在 150 个 no_pref episodes（61.2%）中，两个策略的 per-step action sequence 是否也高度相似？还是说它们采取了不同路径但达到了相同 outcome？如果是后者，这些 episode 中可能存在 step-level routing signal 但被 episode-level aggregation 掩盖了。

**Q3**: Router training（§3.6）使用 episode-level labels 训练 step-level 分类器。如果使用 step-level heuristic labels（如：在 death episode 中，仅将最后 k 步标记为 "avoid this strategy"），router 性能是否有改善？

---

## Missing References

- Schuster et al. (2022), "Confident Adaptive Language Modeling" — 关于 adaptive computation 在 language model inference 中的 early exit 策略，与 routing signal 的本质（何时需要更多计算）有概念关联。
- Raposo et al. (2024), "Mixture-of-Depths" — 关于 per-token computation allocation，虽然场景不同但涉及类似的 signal decomposition 问题。

---

## 主要优势

- **S1** 研究问题定义清晰且有实践意义：在训练 router 之前先理解 routing signal 的结构，这一"先诊断后优化"的方法论值得推广。
- **S2** 实验设计系统且 robustness check 充分：4 个 intervention axis（Retry, Reflexion, 72B, action-space filtering）、3 个模型的 cross-model replication、penalty sensitivity analysis（Appendix K）、text augmentation ablation（Appendix I Table 11）、cluster bootstrap + wild cluster bootstrap + exact permutation 三重统计验证——分析深度在 analysis track 中属于上乘。
- **S3** Router training 负结论的论证特别扎实：从 step-level overfitting（Table 10, cross-split evaluation）到 episode-level failure（Table 10），再到 data scaling 无效（Table 11），排除了 data-limited 解释，构成了一个有说服力的 negative result。
- **S4** 论文诚实地讨论了 scope limitations：Limitations section 覆盖了 environmental scope、statistical limitations、methodological constraints 和 diagnostic scope，且正文中多次使用限定词。这在 analysis 论文中尤为重要。
- **S5** 附录信息量大且组织良好：24 页论文中 16 页附录覆盖了 signal concentration index 定义、labeling quality audit、per-task decomposition、correlation robustness、bootstrap sensitivity、death rate CIs、DAF sensitivity、threshold routing、router training details、seed robustness、text augmentation、cross-environment detail、failure mode analysis、grounding ablation、capacity scaling——这些显著增强了 reproducibility 和说服力。


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

_source line 2332 · 2026-05-22T08:53:43.774147+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5/5, **Excitement**: 3/5, **Reproducibility**: 4/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] Episode-level labeling 与 step-level routing 之间的粒度失配未被充分讨论，核心 claim 的适用范围被高估\n- 论文 title 和 abstract 表述为 \"Death Avoidance as the Dominant Routing Signal\"，暗示这是关于 routing decision 的通用发现，但 Algorithm 1 是 episode-level labeling，95 个 non-tie labels 仅覆盖 38.8% episodes，step level 97.4% uninformative。Claim scope 需更精确限定为 episode-level outcome 发现。\n\n**N2** [critical] DAF 度量的 P-dependence 使得跨环境比较和绝对数值缺乏稳健性\n- DAF = δP/(δP + Δ_nd)，随 P 单调递增（P=50 → 82.6%, P=100 → 90.4%, P=200 → 94.9%）。正文未充分讨论 P-dependence，读者需翻 Appendix K 才了解。建议 label fraction (78.9%) 为 primary metric，DAF 为 secondary。\n\n### Should-Fix\n\n**W1** [warning] K=11 cluster bootstrap 处于文献推荐下限\n- Cameron et al. (2008) 建议 K≥20-50。K=11 时可能低估标准误。Cohen's d=3.02 可部分缓解。\n\n**W2** [warning] 63% task type 排除率带来 selection bias 风险\n- 排除标准（dev set 5, redundancy 7, agent floor 7）缺乏 taxonomic redundancy 的操作定义。Near-zero progress tasks 被排除意味着框架只适用于\"至少有一策略有进展\"的 task。\n\n**W3** [warning] Router training 负结论受限于 router 架构简单性\n- 仅测试 Qwen3 0.6B-4B + LoRA。未探索 observation history、task-type 特征、更强 backbone。负结论 scope 应限定为\"当前 architecture under episode-level labels\"。\n\n**W4** [warning] 72B 仅做 scaling probe 而非完整 replication\n- 72B 未运行 router training 或 SCI 分析。更强模型 death rate 更低（42.9%→30.6%），non-death signal 可能更 prominent。\n\n### Minor\n\n**M1** Figure 2 仅 11 点无 task name label\n**M2** Eq. 4 decomposition 精确定义依赖 appendix\n**M3** ALFWorld 分析仅一段话，无独立 table/figure\n**M4** Table 1 caption \"Top\"/\"Bottom\" 对比不直观\n**M5** Limitations 未提及 Cameron et al. K 建议\n**M6** Related Work 缺 non-agent 场景的 adaptive computation（early exit, speculative decoding）\n\n### Missing References\n- Schuster et al. (2022), \"Confident Adaptive Language Modeling\"\n- Raposo et al. (2024), \"Mixture-of-Depths\"\n\n### Questions\nQ1: P=10 时 label distribution 是否变化？78.9% death-asymmetric label fraction 是否仍成立？\nQ2: 150 个 no_pref episodes 中两策略 per-step action sequence 是否相似？\nQ3: 如果用 step-level heuristic labels（仅标记 death episode 最后 k 步），router 是否改善？\n\n---\n\n请逐条回应。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5/5, **Excitement**: 3/5, **Reproducibility**: 4/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] Episode-level labeling 与 step-level routing 之间的粒度失配未被充分讨论，核心 claim 的适用范围被高估\n- 论文 title 和 abstract 表述为 \"Death Avoidance as the Dominant Routing Signal\"，暗示这是关于 routing decision 的通用发现，但 Algorithm 1 是 episode-level labeling，95 个 non-tie labels 仅覆盖 38.8% episodes，step level 97.4% uninformative。Claim scope 需更精确限定为 episode-level outcome 发现。\n\n**N2** [critical] DAF 度量的 P-dependence 使得跨环境比较和绝对数值缺乏稳健性\n- DAF = δP/(δP + Δ_nd)，随 P 单调递增（P=50 → 82.6%, P=100 → 90.4%, P=200 → 94.9%）。正文未充分讨论 P-dependence，读者需翻 Appendix K 才了解。建议 label fraction (78.9%) 为 primary metric，DAF 为 secondary。\n\n### Should-Fix\n\n**W1** [warning] K=11 cluster bootstrap 处于文献推荐下限\n- Cameron et al. (2008) 建议 K≥20-50。K=11 时可能低估标准误。Cohen's d=3.02 可部分缓解。\n\n**W2** [warning] 63% task type 排除率带来 selection bias 风险\n- 排除标准（dev set 5, redundancy 7, agent floor 7）缺乏 taxonomic redundancy 的操作定义。Near-zero progress tasks 被排除意味着框架只适用于\"至少有一策略有进展\"的 task。\n\n**W3** [warning] Router training 负结论受限于 router 架构简单性\n- 仅测试 Qwen3 0.6B-4B + LoRA。未探索 observation history、task-type 特征、更强 backbone。负结论 scope 应限定为\"当前 architecture under episode-level labels\"。\n\n**W4** [warning] 72B 仅做 scaling probe 而非完整 replication\n- 72B 未运行 router training 或 SCI 分析。更强模型 death rate 更低（42.9%→30.6%），non-death signal 可能更 prominent。\n\n### Minor\n\n**M1** Figure 2 仅 11 点无 task name label\n**M2** Eq. 4 decomposition 精确定义依赖 appendix\n**M3** ALFWorld 分析仅一段话，无独立 table/figure\n**M4** Table 1 caption \"Top\"/\"Bottom\" 对比不直观\n**M5** Limitations 未提及 Cameron et al. K 建议\n**M6** Related Work 缺 non-agent 场景的 adaptive computation（early exit, speculative decoding）\n\n### Missing References\n- Schuster et al. (2022), \"Confident Adaptive Language Modeling\"\n- Raposo et al. (2024), \"Mixture-of-Depths\"\n\n### Questions\nQ1: P=10 时 label distribution 是否变化？78.9% death-asymmetric label fraction 是否仍成立？\nQ2: 150 个 no_pref episodes 中两策略 per-step action sequence 是否相似？\nQ3: 如果用 step-level heuristic labels（仅标记 death episode 最后 k 步），router 是否改善？\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 2333 · 2026-05-22T08:54:13.801828+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30027
}
```

</details>

---


### Tool call

_source line 2334 · 2026-05-22T08:54:14.956426+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5（Borderline Conference）\n**Soundness**: 4/5, **Excitement**: 3/5, **Reproducibility**: 4/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] DAF 的数学必然性与主文叙述存在张力\n- DAF = δP/(δP + Δ_nd)，P 远大于 Δ_nd 时 DAF → 1 是数学必然。Appendix K 承认\"mathematical consequence\"，但主文和 Abstract 仍以 DAF=90.4% 为核心数字之一。P=0 时 DAF 仅 7.4%，P=10 时 50.4%。建议 label fraction (78.9%) 为叙事主线，降低 DAF 突出度。\n\n**N2** [critical] \"Deterministic\" 在三环境中含义截然不同，泛化 claim 需更谨慎\n- ScienceWorld = oracle simulator, MATH = code interpreter, ALFWorld = admissible-action enumeration。§2.1 提到差异但 Conclusion 仍写 \"the diagnostic procedure transfers\"。需区分 procedure transferability vs operationalization consistency。\n\n### Should-Fix\n\n**W1** [warning] 63% task type 排除率需在主文更充分 justify\n- 主文仅一句话带过。对 analysis 论文，63% 排除率 + 三种排除原因值得一段正文讨论。\n\n**W2** [warning] 路由器负面结果的 alternative explanations 未充分排除\n- Internal-preferred 仅 9/245 = 3.7%，augmentation 只是 paraphrase，仅测试 Qwen3。在极端不平衡下 router 失败可能是数据不足而非信号不存在。\"~1,350 episodes needed\" 与 \"diminishing return on 9.6% signal\" 有张力。\n\n**W3** [warning] Limitations 过长（5 段近一整页）\n- 建议压缩到 3 个核心点，将 pure-strategy upper bound 和 diagnostic scope 合并简化。\n\n**W4** [warning] 缺少与同期路由方法的直接比较\n- Related Work 引用了 CogRouter/ARES/MTRouter 等但无实证比较。可增加定性讨论：这些方法在 death-dominated 环境中是否会遇到 signal collapse。\n\n**W5** [warning] \"Death\" 术语可能限制 generality perception\n- 当 failure 不是 binary（death/alive）而是 graded 时，DAF framework 适用性如何？\n\n### Minor\n- §1 \"signal diversity can collapse\" 重复出现\n- §2.2 \"degenerates\" 用词不常见\n- Figure 2 仅 11 点 + caption caveat 不够明确\n- Table 2 Trained Router 仅 1 seed\n- Algorithm 1 \"death asymmetry\" 注释出现两次方向不同\n- arXiv preprints 占比较高\n- §3.2 Gemma-2 区分特征仅提 sliding window attention\n\n### Missing References\n1. Alshiekh et al. (AAAI 2018), \"Safe RL via Shielding\" — 与 Appendix O action-space filtering 相关\n2. Pan et al. (2024), LLM agent failure taxonomy\n3. Devlin & Kudenko (AAMAS 2012), Dynamic reward shaping\n4. Geifman & El-Yaniv (NeurIPS 2017), Selective Classification\n5. AppAgent (Zhang et al., 2024), OS-Copilot (Wu et al., 2024)\n\n### Strengths\nS1: 极其详尽的鲁棒性验证（20 appendix）\nS2: 诚实的负面结果报告\nS3: Penalty-independent 与 penalty-dependent 度量双轨报告\nS4: Cross-model convergence（3 family, spread 2.2pp）\nS5: Track fit 优秀（Interpretability and Analysis）\nS6: 写作质量整体较高\n\n---\n\n请逐条回应。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5（Borderline Conference）\n**Soundness**: 4/5, **Excitement**: 3/5, **Reproducibility**: 4/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] DAF 的数学必然性与主文叙述存在张力\n- DAF = δP/(δP + Δ_nd)，P 远大于 Δ_nd 时 DAF → 1 是数学必然。Appendix K 承认\"mathematical consequence\"，但主文和 Abstract 仍以 DAF=90.4% 为核心数字之一。P=0 时 DAF 仅 7.4%，P=10 时 50.4%。建议 label fraction (78.9%) 为叙事主线，降低 DAF 突出度。\n\n**N2** [critical] \"Deterministic\" 在三环境中含义截然不同，泛化 claim 需更谨慎\n- ScienceWorld = oracle simulator, MATH = code interpreter, ALFWorld = admissible-action enumeration。§2.1 提到差异但 Conclusion 仍写 \"the diagnostic procedure transfers\"。需区分 procedure transferability vs operationalization consistency。\n\n### Should-Fix\n\n**W1** [warning] 63% task type 排除率需在主文更充分 justify\n- 主文仅一句话带过。对 analysis 论文，63% 排除率 + 三种排除原因值得一段正文讨论。\n\n**W2** [warning] 路由器负面结果的 alternative explanations 未充分排除\n- Internal-preferred 仅 9/245 = 3.7%，augmentation 只是 paraphrase，仅测试 Qwen3。在极端不平衡下 router 失败可能是数据不足而非信号不存在。\"~1,350 episodes needed\" 与 \"diminishing return on 9.6% signal\" 有张力。\n\n**W3** [warning] Limitations 过长（5 段近一整页）\n- 建议压缩到 3 个核心点，将 pure-strategy upper bound 和 diagnostic scope 合并简化。\n\n**W4** [warning] 缺少与同期路由方法的直接比较\n- Related Work 引用了 CogRouter/ARES/MTRouter 等但无实证比较。可增加定性讨论：这些方法在 death-dominated 环境中是否会遇到 signal collapse。\n\n**W5** [warning] \"Death\" 术语可能限制 generality perception\n- 当 failure 不是 binary（death/alive）而是 graded 时，DAF framework 适用性如何？\n\n### Minor\n- §1 \"signal diversity can collapse\" 重复出现\n- §2.2 \"degenerates\" 用词不常见\n- Figure 2 仅 11 点 + caption caveat 不够明确\n- Table 2 Trained Router 仅 1 seed\n- Algorithm 1 \"death asymmetry\" 注释出现两次方向不同\n- arXiv preprints 占比较高\n- §3.2 Gemma-2 区分特征仅提 sliding window attention\n\n### Missing References\n1. Alshiekh et al. (AAAI 2018), \"Safe RL via Shielding\" — 与 Appendix O action-space filtering 相关\n2. Pan et al. (2024), LLM agent failure taxonomy\n3. Devlin & Kudenko (AAMAS 2012), Dynamic reward shaping\n4. Geifman & El-Yaniv (NeurIPS 2017), Selective Classification\n5. AppAgent (Zhang et al., 2024), OS-Copilot (Wu et al., 2024)\n\n### Strengths\nS1: 极其详尽的鲁棒性验证（20 appendix）\nS2: 诚实的负面结果报告\nS3: Penalty-independent 与 penalty-dependent 度量双轨报告\nS4: Cross-model convergence（3 family, spread 2.2pp）\nS5: Track fit 优秀（Interpretability and Analysis）\nS6: 写作质量整体较高\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 2335 · 2026-05-22T08:54:16.567647+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---


### Assistant

_source line 2336 · 2026-05-22T08:54:18.972512+00:00_

交叉分享已派发，等待两位 Reviewer 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 194

## Round 194

2 recorded events


### User

_source line 2337 · 2026-05-22T08:54:21.705100+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3。

**两个 Must-Fix 问题**：
1. Episode-level labeling 到 step-level routing 的粒度失配——标题和 abstract 的表述范围超出了方法论的实际覆盖范围（95 个 non-tie label 仅覆盖 38.8% 的 episode，97.4% 的 step 无信息量），需要更精确的 scope 限定。
2. DAF 度量随 penalty P 单调递增——正文中报告的 90.4% 部分由 P=100 的选择决定，需在正文而非仅 Appendix K 中讨论，并将 P-invariant 的 label fraction 提升为 primary metric。

**四个 Should-Fix**：K=11 cluster bootstrap 处于文献推荐下限、63% task type 排除率的 selection bias 风险、router training 负结论受限于简单架构、72B scaling 仅作 probe 而非完整 replication。

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

_source line 2338 · 2026-05-22T08:54:26.875512+00:00_

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


## Round 195

## Round 195

2 recorded events


### User

_source line 2339 · 2026-05-22T08:55:56.079895+00:00_

[Reviewer 2 审稿结果]:
逐条回应 Reviewer 1 的审稿意见。

---

## Must-Fix 回应

**[REBUT] R1-N1**: Episode-level vs step-level 粒度失配，claim scope 被高估

R1 认为标题和 abstract 暗示了 step-level routing 的通用发现，但证据仅在 episode level。我认为这个批评部分有道理但力度偏重，原因如下：

1. 论文标题说的是 "Routing **Signal**" 而非 "Routing Decision"。论文的核心 claim 恰恰是：在 sparse-reward 环境中，可供 routing 学习的 signal 被 death avoidance 主导——这是一个关于 signal 组成的分析发现，不是关于 step-level 最优决策的 claim。
2. 论文在 §2.2 明确论证了为什么 episode-level 是此类环境的 principled granularity（97.4% step-level ties，per-step oracle degenerates），而非 fallback。这不是粒度"失配"，而是作者 deliberately 选择了唯一有信息量的分析粒度。
3. §3.6 Router Training 和 §5 Discussion paragraph 1 已经详细讨论了 step-level 路由器为何失败（episode-level 信号无法投射到 step level），且论文将此作为 negative result 完整报告。
4. 38.8% non-tie rate（95/245）不意味着 claim 只适用于这 38.8%——61.2% no-preference episodes 同样是诊断信息（两种策略无差异 = 无需路由），这是 framework 的正常输出。

但我同意 R1 一个子观点：Abstract 的表述可以更明确地标注这是 episode-level outcome analysis。当前 Abstract 说"78.9% of non-tie routing labels arise from death asymmetry"，可以加一个限定词使 scope 更清晰。这是 framing 层面的微调，不是 claim validity 问题。

---

**[AGREE] R1-N2**: DAF 的 P-dependence 使跨环境比较缺乏稳健性

完全同意。这与我自己的 N1 高度一致。DAF = δP/(δP + Δ_nd) 随 P 单调递增是数学必然（§2.4 Eq. 5），Appendix K Table 8 清楚展示了 P=10 时 DAF 仅 50.4%，P=0 时 7.4%。论文在 Appendix K 最后一段自己承认了 "this is a mathematical consequence of the decomposition, not evidence of mechanism robustness"，但这个关键 caveat 没有出现在主文。

补充一点 R1 未提到的：论文在 §2.4 最后一段"Relationship between DAF and label fraction"已经解释了为什么 DAF (90.4%) > label fraction (78.9%)——因为 death episodes 的 score gap 被 P 放大。这段文字实际上提供了降级 DAF 的论据，但叙事结构没有跟进这个逻辑。建议正文明确将 label fraction 78.9% 定为 primary metric，DAF 90.4% 定为 secondary / supplementary，并在 §2.4 加入 penalty sensitivity 的核心数字（至少 P=10 和 P=50 的 DAF）。

---

## Should-Fix 回应

**[AGREE] R1-W1**: K=11 cluster bootstrap 处于文献推荐下限

同意。论文在 Appendix E 和 Limitations (Statistical limitations 段) 确实承认了 K<20 的局限，并报告了 wild cluster bootstrap (p<0.001) 和 exact permutation (p=0.002) 作为补充（Table 4, Appendix E）。Cohen's d=3.02 说明效应量极大。但 Limitations 正文中没有显式引用 Cameron et al. (2008) 的 K≥20-50 建议作为对标，这是一个遗漏。

不过，这个问题的实际影响有限：100% 方向一致性（10/10 death-prone tasks 均显示 internal DR > deterministic DR）加上 per-task CI 分析（Appendix F, 28/28 death-prone tasks 方向一致）提供了不依赖 cluster bootstrap 的补充证据。

---

**[AGREE] R1-W2**: 63% task type 排除率和 selection bias 风险

同意，但认为论文已提供了充分的缓解证据。R1 指出 "taxonomic redundancy" 缺乏操作定义——这确实是一个弱点。论文 Appendix C 只说了 "taxonomically redundant with a retained family representative" 但没给出 taxonomy 标准。

关于 "agent floor tasks 被排除意味着框架只适用于有进展的 tasks"——这一点需要区分：这些 tasks 被排除的原因是两种策略都不工作（near-zero progress），此时确实没有 routing signal 可 decompose（因为两者都失败了）。这不是框架的局限，而是 signal 不存在的正确诊断。论文在 §5 Discussion paragraph 3 最后一句提到了这一点（"The 7 excluded agent-floor tasks... represent a symmetric failure regime that the framework correctly diagnoses as 'no signal'"）。

但我同意主文应更完整地 justify 排除标准——至少把 Table 2 (Appendix C) 的关键数字（excluded mean ΔDR=+38.2 > included +28.7 pp）提到正文中。

---

**[REBUT] R1-W3**: Router training 负结论受限于架构简单性

部分不同意。R1 建议测试更强 backbone 或更丰富的 feature（observation history, task-type 特征），但论文的 evidence 比 R1 认为的更全面：

1. **六种 router 变体收敛于同一结论**（§3.6, §5 paragraph 1）：0.6B/1.7B/4B × classification/generative，step-level accuracy 一致在 56-59% 范围。这排除了单一架构偶然失败的解释。
2. **Task-type 特征已测试**（Appendix P, "Leave-one-task-type-out routing"段）：keyword-based variant 通过 task-identity leakage 达到 62.9%，但 LOTO 下降到 50.0%——这证明唯一可学习的 routing feature IS task-type identity，不是 step-level observation。
3. **4B 的 episode-level 59.0% 也被 LOTO 打回**（Appendix P）：无 task-type identifiers 时降到 50.0%，有 task name 时升到 62.9%。
4. **Capacity scaling**（Appendix P Table 9）显示 step-level accuracy 在 0.6B-4B 范围内是 flat 的（56-59%），增加容量无帮助。

但我同意 R1 的一个子观点：负结论的 scope 确实应更精确地限定。论文说 "no step-level learnable signal exists under current architectures and data regime"（§3.6 最后段），这已经加了限定词，但 "current architectures" 的范围可以更明确（Qwen3 family with LoRA, max 4B）。

---

**[AGREE] R1-W4**: 72B 仅做 scaling probe 不够完整

同意。72B 数据（§3.4, Table 1）只收集了 episode pairs 并计算 death rate 和 DAF，没有运行：
- Router training（72B 作为 backbone 或 72B episodes 作为训练数据）
- SCI 分析
- Per-task decomposition（虽然 Appendix M Table 6 有 cross-model summary，但 72B 的 per-task 细节缺失）

R1 的推理也成立：72B death rate 降到 30.6%（vs 7B 的 42.9%），意味着更多 episodes 双方都存活，Δ_nd 的信号量可能增加。如果 non-death signal 在更强模型上更 prominent，那 "death dominance" 的结论可能在 scale-up 后需要修正。不过，72B 的 DAF=92.4% 反而更高（因为 deterministic 也更安全了），所以至少在当前数据上 death dominance 是 scale-robust 的。

---

## Minor 回应

**[AGREE] R1-M1**: Figure 2 仅 11 点无 task name label。同意，scatter plot 加 task name 标签会增加可读性，且论文自己说 r=0.97 是 "a structural consequence of death dominance, not an independent finding"（Figure 2 caption 末尾），加 label 可以帮助读者理解每个点对应什么。

**[REBUT] R1-M2**: Eq. 4 decomposition 精确定义依赖 appendix。部分不同意——§2.4 的 Eq. 4 和 Eq. 5 在正文中已给出完整的数学定义（δ = E[d^int] - E[d^det], Δ_nd, DAF = 1 - Δ_nd/Δ_full），approximation residual 也在正文报告（0.23, 0.8%）。Appendix K 提供的是 penalty sensitivity 扩展分析，不是核心定义的补充。

**[AGREE] R1-M3**: ALFWorld 分析仅一段话。同意。ALFWorld 有 135 games、6 task types（Appendix L Table 5 有 per-task breakdown），但主文只在 §3.4 用一段话总结。考虑到 ALFWorld 是论文三个 cross-environment probes 之一，且展示了一个质性不同的 routing mechanism (information asymmetry, DAF=0%)，主文至少应引用 Table 5 或 Figure 4 (signal_reversal.pdf)。

**[AGREE] R1-M4**: Table 1 caption "Top"/"Bottom" 对比不直观。同意，Table 1 的上半部分是全 11 tasks，下半部分是 10 death-prone tasks only，两部分的 N 不同（245 vs 200），baseline 也不同。这种 layout 容易导致误读。

**[AGREE] R1-M5**: Limitations 未提及 Cameron et al. K 建议。同意，与 W1 一致。Limitations "Statistical limitations" 段引用了 cameron-2008 和 webb-2023，但没有显式说"推荐 K≥20-50 而我们只有 11"。

**[AGREE] R1-M6**: Related Work 缺 non-agent 场景的 adaptive computation。同意。论文引用了 Graves (2016, ACT) 和 Mixture-of-Recursions (2025)，但缺少 early exit（如 Schuster et al. 2022, CALM）和 speculative decoding 方向。这些方法虽然不在 agent 场景，但与 "adaptive computation routing" 这个更大的 framing 直接相关。

---

## Missing References 回应

**[AGREE]** Schuster et al. (2022), "Confident Adaptive Language Modeling" — 直接相关于 adaptive computation routing 的 non-agent baseline。论文引用了 Graves (2016) 但跳过了 CALM 这个更近的 milestone。

**[AGREE]** Raposo et al. (2024), "Mixture-of-Depths" — token-level 计算资源分配，与论文的 step-level routing 在 granularity 上有对应关系，值得引用。

---

## Questions 回应

**Q1**: P=10 时 label distribution 是否变化？78.9% death-asymmetric label fraction 是否仍成立？

回答：78.9% label fraction 不随 P 变化。这是论文的一个关键设计——Algorithm 1 (Appendix B) 的 labeling function 先比较 death status（lines 5-10），再比较 score（lines 11-16）。death-asymmetric labels（75/95）由 death status 决定，与 P 无关。P 只影响 DAF 的数值（因为 DAF 是 score-weighted 度量）。论文在 §2.4 倒数第二段明确说了："In ScienceWorld, P affects only post-hoc score calculation; the agent's policy (ReAct prompting) does not include P in its observation, so death rates and Δ_nd are P-invariant by design."

但这里有一个微妙点：P=10 时，75 个 death-asymmetric labels 中有 54 个是 "sole-signal labels"（§3.1 第一段），即两策略在 non-death 维度上无差异，仅靠 death status 区分。在 P=0 时，这 54 个 label 会变成 no-preference（因为 score 相同）。所以虽然 labeling function 本身是 P-independent 的，但 Algorithm 1 的 death-first priority 实际上等价于给 death 一个隐式的无穷大 penalty——这与"penalty-independent"的叙事有微妙张力。论文在 §3.1 提到了 "at P=0 these reduce to ties"，但没有展开讨论这个 implication。这是一个值得作者回应的精妙问题。

**Q2**: 150 个 no_pref episodes 中两策略 per-step action sequence 是否相似？

回答：论文未直接分析 no_pref episodes 的 action sequence 相似度。但可从现有数据推断：§2.2 报告 97.4% step-level ties（5,935/6,094 steps），这意味着绝大多数 steps 的 intermediate score 相同，但不能推出 action sequence 相同（因为不同 actions 可能导致相同 intermediate score）。Appendix N 的 failure mode analysis 只覆盖了 death episodes。这是一个有价值的分析方向——如果 no_pref episodes 的 action sequences 高度相似，说明两种策略在非致命场景中行为趋同；如果差异大但结果相同，说明 ScienceWorld 的 evaluation function 有多解。

**Q3**: 如果用 step-level heuristic labels（仅标记 death episode 最后 k 步），router 是否改善？

回答：论文在 Appendix P "Death-proximal labeling" 段已经测试了这个想法。结果是：仅用 death event 前 k 步训练 router，step balanced accuracy 50.0%, episode balanced accuracy 50.0%, internal recall 0%——完全 collapse to majority class。这直接回答了 R1 的 Q3，且结论是否定的。论文的解释是 "the absence of step-level signal is not an artifact of label dilution across long episodes"（Appendix P 最后一段）。

---

**总结**：R1 的审稿意见整体合理。N2（DAF P-dependence）与我的 N1 高度一致，是最需要作者回应的 critical issue。N1（granularity mismatch claim scope）我认为 R1 略有过度解读，论文的 claim 实际上是关于 signal composition 而非 step-level decision。W1-W4 中 W3 的证据比 R1 认为的更充分（六种 router 变体 + LOTO），W4（72B 不完整）是一个 valid 但 scope-limited 的 concern。

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

_source line 2340 · 2026-05-22T08:56:07.569338+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 196

## Round 196

10 recorded events


### User

_source line 2341 · 2026-05-22T08:56:07.574569+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: DAF 的数学必然性与主文叙述存在张力**

完全同意。这与我的 N2 高度一致。Appendix K 明确写道 DAF "increases monotonically with P" 且是 "a mathematical consequence rather than an empirical finding"（§2.4 末尾），但 Abstract 仍将 DAF=90.4% 作为核心数字呈现（"DAF reaches 90.4%"）。R2 提供的具体数值（P=0 时 DAF=7.4%, P=10 时 50.4%）进一步量化了这一问题的严重性——DAF 从 7.4% 到 90.4% 的变化完全由 P 值驱动。论文应将 P-invariant 的 label fraction（78.9%）作为叙事主线，DAF 仅作为辅助度量。这一修改不需要改变任何实验结果，只需调整叙述重心。

**[AGREE] R2-N2: "Deterministic" 在三环境中含义截然不同**

这是我审稿时未充分关注的重要问题。§2.1 定义 deterministic strategy 为 "a privileged information strategy that eliminates computation uncertainty"，但具体实现差异很大：ScienceWorld 的 oracle simulator 可以直接获取环境真实状态（§2.1），MATH 的 code interpreter 是确定性计算工具（§3.4），ALFWorld 的 admissible-action enumeration 是动作空间约束（§3.4）。这三者对 "eliminating computation uncertainty" 的方式和程度完全不同——oracle 消除了所有不确定性，code interpreter 只消除计算错误，admissible-action 只消除无效动作。Conclusion（§6）写 "the framework's diagnostic utility and the robustness of the finding"（p8），这一表述暗示了跨环境的一致性，但实际上应区分 "diagnostic procedure is transferable"（框架可以应用）和 "the same phenomenon is observed"（同一现象被观察到——实际上 MATH 没有 death mechanism，不存在 death avoidance）。建议在 Conclusion 中增加一句限定：框架的 transferability 不意味着 death dominance 在所有环境中都成立。

---

### Should-Fix

**[AGREE] R2-W1: 63% task type 排除率需在主文更充分 justify**

与我的 W2 一致。主文仅在 §3 第一段用一句话说明排除原因（"the 19 excluded types (63%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7)"），对于一篇 analysis 论文来说过于简略。Table 4（p14, Appendix C）提供了详细的 per-task exclusion rationale，但这些信息应在正文中有更充分的展示——至少需要一段话讨论排除标准的操作定义和对结论泛化性的影响。

**[AGREE with nuance] R2-W2: 路由器负面结果的 alternative explanations 未充分排除**

同意核心论点，但需补充两点 nuance：

(1) R2 指出 internal-preferred 仅 9/245 = 3.7%，这确实是极端不平衡。但论文的 text augmentation ablation（Appendix I, Table 11）从 25% 到 800% 数据量均未改善 episode-level balanced accuracy（始终 ≤50.0%），且 balanced accuracy 本身对 class imbalance 是 robust 的（它分别计算每个类的 recall 再平均）。这部分论证是有效的。

(2) 但 R2 关于 "augmentation 只是 paraphrase" 的批评成立——paraphrase augmentation 不增加新的 routing signal，只增加了相同 signal 的语言变体。如果问题是 signal 在文本中不可见（hidden in environment dynamics rather than text surface），paraphrase 不能解决。论文需要更清晰地区分 "data-limited"（样本数不足）和 "feature-limited"（文本表面特征无法捕获 routing-relevant information）——当前的 text augmentation 只排除了前者。

R2 提到的 "~1,350 episodes needed"（Appendix I 提及 internal-preferred rate 3.7% 意味着需要 ~1,350 episodes 才能收集 50 个 internal-preferred 样本）与 "diminishing return" 之间的张力是合理的——论文应承认在当前 class imbalance 下，signal-limited vs data-limited 的区分尚不完全 conclusive。

**[REBUT] R2-W3: Limitations 过长**

不同意。EMNLP 2026 格式要求明确规定 "Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content"。论文的 Limitations section（p9）覆盖 4 个维度（Environmental scope, Statistical limitations, Methodological constraints, Diagnostic scope），每个维度 3-5 句话，总计约 0.8 页。对于一篇以 methodological rigor 为核心卖点的 analysis 论文，这些限制讨论是必要的，而非冗余的：

- Environmental scope 限定了单环境结论的适用范围
- Statistical limitations 诚实报告了 K=11 和 n=20 的功效问题
- Methodological constraints 讨论了 episode-level 方法论的固有局限
- Diagnostic scope 区分了 diagnostic framework 和 prescriptive optimization

压缩可能导致重要 caveats 被省略。我在自己的 S4 中将此列为论文优势（"论文诚实地讨论了 scope limitations"）。如果要修改，建议合并 Methodological constraints 和 Diagnostic scope 为一段，但不建议删减内容。

**[AGREE partially] R2-W4: 缺少与同期路由方法的直接比较**

同意应增加定性讨论，但不同意需要实证比较。本文是 diagnostic/analysis 论文而非 method 论文，要求实证比较 CogRouter/ARES/MTRouter 超出了论文 scope。但 R2 建议的定性讨论——"这些方法在 death-dominated 环境中是否会遇到 signal collapse"——是 Related Work（§4）中一个有价值的补充。具体来说：CogRouter（Yang et al., 2026b）使用 per-step routing，如果 step-level signal 如本文所示是 uninformative 的（97.4% steps uninformative, §2.3），CogRouter 在此类环境中可能面临同样的 signal collapse。这类讨论可以用 2-3 句话完成，不需要新实验。

**[AGREE] R2-W5: "Death" 术语可能限制 generality perception**

同意。论文框架依赖 binary death/alive 区分（Algorithm 1, line 3-9）。当 failure 是 graded（如 partial score loss, degraded performance）而非 catastrophic 时，Algorithm 1 的 death-first priority 逻辑不再适用——没有明确的 "death" 阈值。§5 Discussion 中 "Practical implications and actionability"（p8）提到 "The penalty-invariant label fraction (78.9%) is the primary diagnostic; DAF varies with P"，但未讨论 death 概念本身是否可以 generalize 到 non-binary failure modes。建议在 Discussion 或 Limitations 中增加一段讨论 graded failure 的情况，例如：可以设定 failure 阈值将 graded failure 二值化，但阈值选择引入新的自由度。

---

### Minor

- **[AGREE]** "signal diversity can collapse" 重复——minor writing issue
- **[REBUT]** "degenerates" 用词：这是标准数学/统计用语（"the approach degenerates to..."），在 NLP 论文中常见，无需修改
- **[AGREE]** Figure 2 仅 11 点：与我的 M1 一致，建议加 task name label
- **[AGREE]** Table 2 Trained Router 仅 1 seed：Appendix J（Table 10）报告了 8 seeds 的 cross-split evaluation，但 Table 2 仅展示 1 seed 结果。建议在 Table 2 中报告 mean ± std across seeds
- **[AGREE]** Algorithm 1 注释问题：minor formatting，但可能导致误解
- **[REBUT partially]** arXiv preprint 占比高：2024-2026 年的 LLM agent 领域 fast-moving，许多重要工作尚未正式发表（如 CogRouter, SafeRoute, SALT 等均为 2025-2026 preprints），高 arXiv 比例在此领域是正常的
- **[AGREE]** Gemma-2 描述不足：§3.2 仅提 sliding window attention，但 Gemma-2-9B 的 architecture 差异（如不同的 normalization, vocabulary size）也可能影响 routing signal，值得补充

### Missing References

- **[AGREE]** Alshiekh et al. (AAAI 2018) Safe RL via Shielding — 与 Appendix O (Grounding Ablation) 的 action-space filtering 直接相关，应引用
- **[AGREE]** Geifman & El-Yaniv (NeurIPS 2017) Selective Classification — 与 routing/abstention decision 有概念关联，且是 selective prediction 的经典工作
- **[NEUTRAL]** Pan et al. (2024) LLM agent failure taxonomy — 如果存在公开版本，可以增加引用；但 failure taxonomy 与 routing signal decomposition 的关联不够直接
- **[NEUTRAL]** Devlin & Kudenko (AAMAS 2012) Dynamic reward shaping — 与 penalty sensitivity（Appendix K）有间接关联，但本文不做 reward shaping，引用必要性不高
- **[NEUTRAL]** AppAgent / OS-Copilot — 这些是 agent system 论文，与本文的 diagnostic focus 关联较弱

---

### 对 R2 Strengths 的回应

全部同意（S1–S6）。特别支持 S3（双轨度量报告）和 S5（Track fit）——本文确实非常适合 Interpretability and Analysis track，分析深度在该 track 中属于上乘。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2 的 2 个 Must-Fix 均 AGREE**：N1（DAF P-dependence）与我的 N2 高度一致；N2（"deterministic" 跨环境含义不同）是我审稿时遗漏的重要问题
- **5 个 Should-Fix 中 AGREE 3 个、部分 AGREE 1 个、REBUT 1 个**：W3（Limitations 过长）我反驳——对 analysis 论文来说诚实的 limitations 是优势而非缺陷，且不占页数限制
- **7 个 Minor 中 AGREE 4 个、REBUT 2 个、AGREE 1 个**："degenerates" 是标准数学用语，arXiv 高占比在 fast-moving 领域正常
- **5 个 Missing References 中 AGREE 2 个、NEUTRAL 3 个**

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

_source line 2342 · 2026-05-22T08:56:39.050112+00:00_

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

_source line 2343 · 2026-05-22T08:56:39.151243+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T08:46:52.839773+00:00\", \"completed_at\": \"2026-05-22T08:50:24.194190+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，第一个视觉锚点（Figure 1）出现在 page 2。Title/Abstract/Intro 排版干净整洁，ACL 双栏格式规范。Figure 1 在 page 2 是可接受的，但审稿人翻开第一页只看到纯文字。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（counterfactual pipeline 图）作为首个视觉锚点，能传达核心方法流程（episode collection → death decomposition）。但图较小，图内文字偏小（尤其是公式 Δ_dd = ΔP × Δ_death 部分），建议适当放大或改为 figure* 全宽展示。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"纯文本+公式页（§2.3-2.4，方程 3-5）。数学推导密集段属于合理例外，无问题。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（scatter plot）位置合理，紧随 §3.1 统计推断讨论。图较小但数据点和回归线清晰可辨。相关系数标注文字偏小。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用 booktabs 风格，格式规范。列对齐和数字精度统一。最优值有加粗标注。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 + Table 2 同页，视觉密度好。Figure 3 使用误差带（shaded region）展示置信区间，是好的可视化实践。颜色区分度可接受。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 7-8\", \"message\": \"连续两页纯文本无任何 display item。Page 7 包含 §3.6（Router Training 负向结果）和 §4（Related Work）；Page 8 包含 Related Work 续、§5 Discussion、§6 Conclusion。虽然这些章节传统上文本密集，但连续两整页纯文字会让审稿人阅读节奏变得单调。建议：§3.6 的 router 训练结果可考虑用一个小 table 呈现而非纯文字描述。\"}, {\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"Limitations 章节过长，几乎填满整页，包含 5 个子章节（Environmental scope / Statistical limitations / Methodological constraints / Pure-strategy upper bound / Diagnostic scope）。EMNLP 指南建议 Limitations 简短覆盖 ~3 个要点即可。当前篇幅可能给审稿人\\\"防御性过强\\\"的印象。\"}, {\"severity\": \"info\", \"dimension\": \"page 10\", \"message\": \"Ethics Statement 简洁得体。References 开始，格式统一，无 [?] 未解析引用。\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Algorithm 1 伪代码框清晰，Table 3（per-task decomposition）列数多但格式规范。\"}, {\"sev
…[truncated 1216 chars]

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

_source line 2344 · 2026-05-22T08:56:39.151745+00:00_

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

_source line 2345 · 2026-05-22T08:56:39.252399+00:00_

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
