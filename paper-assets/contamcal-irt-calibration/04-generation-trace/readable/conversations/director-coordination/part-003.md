# Director coordination — Part 3 of 5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/34/344e7a91893ffee82516.json)

## Round 63

### User

_source line 657 · 2026-05-21T07:33:51.475530+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性 + Related Work + 写作质量 + 格式合规

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 控制实验设计严谨，"污染≠膨胀"的核心发现有实际影响力，但 N=4 模型族支撑四类分类学的泛化性不足，且与 Han et al. (2026) 的差异化论证缺乏实证对比。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 控制实验设计合理，DID + 跨 benchmark transfer 提供因果证据链，但 N=4 限制分类学泛化性，DID 统计效力存疑 |
| Excitement | 3.5/5 | "contamination ≠ inflation" 挑战社区普遍假设，有实际指导价值；但方法论创新有限（IRT+DIF 已有先例），taxonomy 更偏描述性 |
| Reproducibility | 4/5 | 实验细节完整（模型、超参、种子数、LoRA 配置均明确），Algorithm 1 可重现，Stan 推断参数详尽；代码未开源扣 1 分 |
| Overall | 3.5/5 | Borderline Conference — 实证贡献扎实但增量性质限制了主会议水平的影响力 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] N=4 模型族支撑 4 类分类学，泛化性不足

- **具体位置**: Section 3.4 (Algorithm 1), Table 1, Section 5.1
- **问题**: 论文提出 Immune / Collapse / V-Recovery / Benefit 四类剂量-响应分类学，但仅基于 4 个模型族（Qwen2.5, Phi-4, OLMo-2, Gemma-2）。在 N=4 的情况下，恰好观测到 4 种模式可能只是对 4 个个体行为的 post-hoc 描述，而非可泛化的分类体系。Table 1 中每种模式恰好对应一个模型族（Phi-4→Immune, OLMo-2→Collapse, Qwen-7B→V-Recovery, Gemma-2→Benefit），进一步加深了 overfitting-to-sample 的担忧。论文声称这是一个 "dose-response taxonomy"（Section 1, Contribution 1），但 taxonomy 的核心价值在于泛化——一个 N=K 的分类对 K 个观测并无预测力。
- **为什么影响接收**: 这是论文的核心贡献之一。如果分类学无法泛化到新模型族，其学术价值从"发现了通用模式"降级为"描述了 4 个案例"，不足以支撑主会议接收。
- **建议修改方向**: (a) 增加更多模型族验证（如 LLaMA-3, Mistral, Yi），哪怕只在 1-2 个剂量水平上做快速验证也比 N=4 强很多；(b) 若资源受限，应将 "taxonomy" 改为更谨慎的措辞（如 "observed response profiles"），并在 Discussion 中显式分析模型属性（训练数据量、架构、预训练策略）与响应模式的潜在关联，提出可检验的假说；(c) 论文已有 Qwen-7B 和 Qwen-14B 两个 scale，可分析 family 内 scale 变化是否导致模式切换，作为泛化性的部分证据。

**N2** [critical] 与 Han et al. (2026) 的差异化论证不充分

- **具体位置**: Section 2 (Related Work, "IRT for LLM Evaluation" 段落最后两句)
- **问题**: Han et al. (2026, EACL Findings) 已将 DIF（Differential Item Functioning）应用于 LLM 污染的心理测量分析，是最直接的在先工作。论文在 Related Work 中仅用约两句话区分两者（"ContamCal differs by introducing continuous exposure covariates $\nu_{ij}$... providing domain-level decomposition"）。关键问题是：(1) continuous vs. binary exposure 的实际效果差异有多大？(2) Han et al. 的 group-based DIF 是否在某些场景下更稳健？(3) 如果 ContamCal 的 Stage 1 信号本身就是噪声的（论文 Section 5.6 承认 Min-K%++ 在 0.5B 处发生方向反转），那么将噪声信号连续化是否真比二元分组更优？这些问题均未被讨论。
- **为什么影响接收**: 审稿人需要清楚判断相对于已发表工作的增量价值。当前的区分过于简略，难以评估方法贡献的独立性。
- **建议修改方向**: (a) 在 Method 或 Related Work 中增加 ~0.5 页的详细 methodological comparison（假设差异、输入要求、输出粒度、适用范围）；(b) 理想情况下将 Han et al. 的方法实现为 baseline 加入 Table 5 的 calibration 对比；(c) 至少讨论在 Stage 1 信号噪声条件下，continuous vs. binary exposure 的理论优劣势。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 主文正文疑似超过 8 页限制

- **具体位置**: Section 6 (Discussion and Conclusion) 从 p.8 底部开始，延伸至 p.9
- **问题**: Section 6 在第 8 页底部开始，在第 9 页继续了数段讨论内容（"Diverse patterns, not uniform inflation"、"Diagnostic value beyond aggregate calibration"、"Why bigger ≠ more robust" 等）后才到 Limitations。按 EMNLP 2026 规则，正文（不含 Limitations/Ethics/References）限 8 页。当前估计正文约 8.3-8.5 页，可能触发格式审查。
- **建议**: 压缩 Discussion 内容——部分细节讨论（如 "ARC-Challenge bootstrap stability"、"Signal coverage"）可移入 Appendix，确保 Section 6 在第 8 页内结束。

**W2** [warning] DID 分析的统计效力不足以排除 item-specific effects

- **具体位置**: Section 5.4, Table 4, Figure 2
- **问题**: DID 分析基于 300 个 RRF 过滤项（treated vs. untreated），结论为 "All DID non-significant"，由此推断 "contamination operates via global capability modulation rather than item-specific memorization"。但：(1) 论文自身承认 contamination detection 信号存在系统性噪声（Section 5.6），treated/untreated 分组可能不精确；(2) N=300 在 DID 框架下检测 ~1pp 的 item-specific effect 的 power 可能不足；(3) "absence of evidence ≠ evidence of absence"，当前证据不足以排除小到中等程度的 item-specific effects。
- **建议**: (a) 报告 DID 的 power analysis 或 minimum detectable effect size；(b) 用不同 RRF 阈值（如 top-200, top-500）做 sensitivity analysis；(c) 将 "no item-specific memorization" 的措辞缓和为 "no detectable item-specific effect at our sample size"。

**W3** [warning] 跨种子稳定性偏弱（n=3 seeds），削弱 taxonomy 可靠性

- **具体位置**: Section 5.3, Table 3
- **问题**: 论文定义了两个一致性标准——cross-seed direction consistency（4/5 families agree）和 sign consistency（仅 2/5 agree：Qwen-14B, Gemma-2）。这意味着在 n=3 seeds 下，大多数模型族的分类学标签对 seed 选择敏感。论文承认这一局限但仍以 taxonomy-level 语言报告结果。
- **建议**: (a) 增加 seeds 至 5-10 个获取更可靠方差；(b) 报告 per-family 的 bootstrap CI over seeds 而非仅汇报 agree/disagree；(c) 对 seed-sensitive families 标注不确定性（如 Qwen-7B 的 V-Recovery 标签可信度低于 Gemma-2 的 Benefit）。

**W4** [warning] Algorithm 1 大量硬编码阈值缺乏充分 justification

- **具体位置**: Section 3.4, Algorithm 1
- **问题**: Algorithm 1 使用了 ≥6 个硬编码阈值（τ=1pp Immune 判定, Δ≤-1pp Collapse, mid-trajectory volatility σ*, recovery check 等），阈值选择的主文 justification 仅为 "robust to threshold hyperparameter choice (180/180 model-seed-combination pairs across 30 (τ,σ) combinations; Appendix L)"。Appendix L Table 9 仅报告 "30/30" 粗粒度结果，缺乏 sensitivity curve 展示分类如何随阈值连续变化。
- **建议**: 在 Appendix 中增加阈值 sensitivity heatmap（如 τ ∈ [0.5, 2.0] × σ ∈ [0.3, 1.5] 的分类一致性矩阵），让读者判断阈值选择的鲁棒性。

---

## 小问题（不影响接收）

- **M1**: "pp"（percentage point）在首次使用时（Abstract "≤1pp"）未定义，建议在首次出现处加注。
- **M2**: Section 5.2 中 Gemma-2 因 catastrophic forgetting 被排除出 Table 2，但该排除标准在正文中出现突然。建议在 Experimental Setup (§4) 预先声明跨 benchmark 分析的排除条件。
- **M3**: Limitations 覆盖约 10 个点（Scale ceiling, Seed sensitivity, SFT ecological validity, ARC-Challenge bootstrap stability, Signal coverage, Ensemble size, Position bias, Model misfit, Additive linearity, Prompt format sensitivity），可合并相近项目（如 Seed sensitivity + Scale ceiling → "Generalizability bounds"）精简至 4-5 个核心限制。当前篇幅偏长。
- **M4**: 引用 `holland_1993_dif` 在 OpenAlex 中匹配到 2009 年 Osterlind 编辑版本而非 1993 年 Holland & Wainer 原版；`lord_1980_irt` 匹配到 2012 再版。建议确认年份和版本一致性。
- **M5**: Figure 1 在 p.1 被文字引用 ("Table 1, Figure 1")，应确认图表已就近放置（two-column layout 下浮动体容易跳页）。

---

## 主要优势

1. **实验设计是该领域的方法论升级**: 相比事后观测研究，控制 SFT 注入提供了明确的因果推断基础。跨 4 模型族 × 3 benchmark × 5 剂量的矩阵设计在 contamination 研究中罕见，数据量充实。

2. **核心发现对社区有实际影响**: "contamination ≠ inflation" 直接挑战了普遍假设（如 contamination 必然导致分数膨胀），DID 分析 + 跨 benchmark transfer（Table 2, Section 5.2）构成了相互佐证的证据链。这一发现对 benchmark 设计者和模型评估实践者有直接指导意义。

3. **IRT 整合技术上合理**: 将 contamination detection signals 作为连续协变量融入 explanatory IRT（2PL+γ）是自然的建模选择，比 binary DIF 保留了更多信息。per-item γ 估计 + calibrated scores 的输出具有实用价值（Table 5 证明 MAE 改善）。

4. **写作整体清晰、叙事连贯**: Problem → Method → Findings → Implications 的逻辑链条完整。Algorithm 1 表达清楚，便于重现。Abstract 准确概括了三个贡献。

5. **Appendix 详尽**: 6 页 Appendix 涵盖跨 benchmark 详细结果（A）、IRT identifiability（B）、convergence（F）、DGP robustness（P）、baseline 对比（Q-R），满足可重现性要求。

---

## 可能遗漏的参考文献

1. **Golchin & Surdeanu (2024)** "Time Travel in LLMs: Tracing Data Contamination in Large Language Models" (ICLR 2024) — 提出基于 guided instruction 的 instance-level 污染检测方法，是该领域的代表性工作（150+ 引用），应在 Section 2 contamination detection 段落中讨论。

2. **Sainz et al. (2023)** "NLP Evaluation in Trouble: On the Need to Measure LLM Data Contamination for each Benchmark" (EMNLP 2023 Findings) — 系统论证了按 benchmark 度量污染的必要性，与本文的 per-benchmark dose-response 分析高度相关。

3. **Yang et al. (2023)** "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples" — 证明 string-matching decontamination 不充分、rephrasing 可绕过检测。这与 ContamCal Stage 1 中 S3 (ConStat, paraphrase-based) 信号的设计动机直接相关，应在 Method §3.2 讨论。

---

## 新颖性总体评估

论文的新颖性主要来自**实验范式**（controlled dose-response profiling）而非**方法论**（IRT+DIF 框架已有先例）。三个贡献中：
- **Dose-response taxonomy**: 实验发现有价值，但 N=4 限制了从"观察"到"分类学"的跃迁
- **Global modulation finding**: 最强贡献，因为它用 DID + cross-benchmark evidence 挑战了 contamination = memorization 的隐含假设
- **Signal failure characterization**: Min-K%++ reversal 是有用的实践发现，但更偏 empirical observation

总体新颖性定位：**适合 Findings，borderline Conference**。若能解决 N1（增加模型）和 N2（Han et al. 对比），可达 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-21T07:34:31.366606+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（方法严谨性 + 实验设计 + 统计声明可靠性）\n\n**Overall**: 3.5 — Borderline Conference\n\n## Must-Fix\n\n**N1** [critical] Cross-seed stability 声明与 n=3 样本量严重不匹配\n- n=3 下任何方差估计的置信区间都极宽——即使 3/3 seeds 同方向，bootstrap 置信水平也仅 ~87.5%。Table 3 未提供 seed 间变异性的正式统计检验。dose-response taxonomy 是核心贡献，如果分类在更多 seeds 下不稳定，整个框架的实用价值成问题。\n- 建议：增加到 n=5-10 seeds；报告 bootstrap CI 覆盖 seed 变异性；降低 claim 力度。\n\n**N2** [critical] IRT identifiability 在经验 ensemble size (J=13–16) 下刚好处于边界\n- Appendix P DGP simulation 显示 CI coverage 随 J 增大反而下降（J=500 时 coverage 仅 0.70）。Identifiability simulation 使用 uniform exposure 但实际 RRF exposure 是 right-skewed。\n- 建议：simulation 中使用 skewed exposure；明确报告每个 seed 下实际 J 和 exclusion 情况。\n\n**N3** [critical] DiD 分析的 null result 可能是 statistical power 不足而非真阴性\n- DID 值范围 −0.8 到 +0.6pp，在 n=3 下的 power 未知。Figure 2 的 symmetry 声明依赖视觉判断而非正式检验。将 \"no significant effect\" 等同于 \"no effect\" 是 absence-of-evidence ≠ evidence-of-absence 错误。\n- 建议：做 post-hoc power analysis；弱化结论为 \"we find no evidence of item-specific memorization at the current power level\"。\n\n## Should-Fix\n\n**W1** [warning] RRF fusion 缺乏 calibration 验证\n- 未验证 RRF score 是否反映真实 contamination 程度；未报告 signal 间 rank correlation 和 leave-one-signal-out 消融。\n\n**W2** [warning] SFT injection 的 ecological validity 未充分量化\n- 真实 leakage 发生在 pretraining，本文用 post-training LoRA SFT 注入。AUGMENT mode 进一步偏离真实场景。\n\n**W3** [warning] Baseline 比较中 ContamCal 的优势不够显著\n- GSM8K 上 B4-LinearRegression MAE=0.003 反而优于 ContamCal MAE=0.020。改善存在但不大。\n\n**W4** [warning] Bayesian 和 frequentist 术语混用\n- 论文用 Bayesian MCMC 推断但多处使用 \"significant\" \"p-value\" 等 frequentist 术语，credible interval 与 confidence interval 混用。\n\n## Minor\n- M1: Algorithm 1 正文未给 default τ 值\n- M2: 300 RRF-filtered items 用的是 3 还是 4 signal 不清楚\n- M3: Model exclusion criteria 过于模糊\n- M4: Figure 1 仅展示一个 seed 的结果，caption 未说明\n- M5: Eq. (2) 的 decontamination 计算方式不明确\n- M6: 引用年份不一致（holland_1993_dif, lord_1980_irt）\n\n## Questions\n- Q1: CI coverage 随 J 增大下降的 bias 来源？\n- Q2: RRF exposure skewed 分布是否引入 leverage effect？\n- Q3: 低剂量下 cross-benchmark transfer pattern 是否一致？\n- Q4: 0.5B 的 position bias 是否暗示 small models 有完全不同的 dose-response？\n\n## Missing References\n- Recht et al. (2019) benchmark overfitting\n- Yang et al. (2023) rephrased samples contamination\n- Bakhtin et al. (2024) pretraining deduplication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（方法严谨性 + 实验设计 + 统计声明可靠性）\n\n**Overall**: 3.5 — Borderline Conference\n\n## Must-Fix\n\n**N1** [critical] Cross-seed stability 声明与 n=3 样本量严重不匹配\n- n=3 下任何方差估计的置信区间都极宽——即使 3/3 seeds 同方向，bootstrap 置信水平也仅 ~87.5%。Table 3 未提供 seed 间变异性的正式统计检验。dose-response taxonomy 是核心贡献，如果分类在更多 seeds 下不稳定，整个框架的实用价值成问题。\n- 建议：增加到 n=5-10 seeds；报告 bootstrap CI 覆盖 seed 变异性；降低 claim 力度。\n\n**N2** [critical] IRT identifiability 在经验 ensemble size (J=13–16) 下刚好处于边界\n- Appendix P DGP simulation 显示 CI coverage 随 J 增大反而下降（J=500 时 coverage 仅 0.70）。Identifiability simulation 使用 uniform exposure 但实际 RRF exposure 是 right-skewed。\n- 建议：simulation 中使用 skewed exposure；明确报告每个 seed 下实际 J 和 exclusion 情况。\n\n**N3** [critical] DiD 分析的 null result 可能是 statistical power 不足而非真阴性\n- DID 值范围 −0.8 到 +0.6pp，在 n=3 下的 power 未知。Figure 2 的 symmetry 声明依赖视觉判断而非正式检验。将 \"no significant effect\" 等同于 \"no effect\" 是 absence-of-evidence ≠ evidence-of-absence 错误。\n- 建议：做 post-hoc power analysis；弱化结论为 \"we find no evidence of item-specific memorization at the current power level\"。\n\n## Should-Fix\n\n**W1** [warning] RRF fusion 缺乏 calibration 验证\n- 未验证 RRF score 是否反映真实 contamination 程度；未报告 signal 间 rank correlation 和 leave-one-signal-out 消融。\n\n**W2** [warning] SFT injection 的 ecological validity 未充分量化\n- 真实 leakage 发生在 pretraining，本文用 post-training LoRA SFT 注入。AUGMENT mode 进一步偏离真实场景。\n\n**W3** [warning] Baseline 比较中 ContamCal 的优势不够显著\n- GSM8K 上 B4-LinearRegression MAE=0.003 反而优于 ContamCal MAE=0.020。改善存在但不大。\n\n**W4** [warning] Bayesian 和 frequentist 术语混用\n- 论文用 Bayesian MCMC 推断但多处使用 \"significant\" \"p-value\" 等 frequentist 术语，credible interval 与 confidence interval 混用。\n\n## Minor\n- M1: Algorithm 1 正文未给 default τ 值\n- M2: 300 RRF-filtered items 用的是 3 还是 4 signal 不清楚\n- M3: Model exclusion criteria 过于模糊\n- M4: Figure 1 仅展示一个 seed 的结果，caption 未说明\n- M5: Eq. (2) 的 decontamination 计算方式不明确\n- M6: 引用年份不一致（holland_1993_dif, lord_1980_irt）\n\n## Questions\n- Q1: CI coverage 随 J 增大下降的 bias 来源？\n- Q2: RRF exposure skewed 分布是否引入 leverage effect？\n- Q3: 低剂量下 cross-benchmark transfer pattern 是否一致？\n- Q4: 0.5B 的 position bias 是否暗示 small models 有完全不同的 dose-response？\n\n## Missing References\n- Recht et al. (2019) benchmark overfitting\n- Yang et al. (2023) rephrased samples contamination\n- Bakhtin et al. (2024) pretraining deduplication"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-21T07:34:44.581420+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13214
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-21T07:34:44.992510+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（新颖性 + Related Work + 写作质量 + 格式合规）\n\n**Overall**: 3.5 — Borderline Conference\n\n## Must-Fix\n\n**N1** [critical] N=4 模型族支撑 4 类分类学，泛化性不足\n- 4 个模型族恰好观测到 4 种模式，可能是 post-hoc 描述。Table 1 每种模式恰好对应一个模型族，加深 overfitting-to-sample 担忧。\"taxonomy\" 的核心价值在于泛化——N=K 分类对 K 个观测无预测力。\n- 建议：增加模型族验证（LLaMA-3, Mistral, Yi）；或将 \"taxonomy\" 改为 \"observed response profiles\"。\n\n**N2** [critical] 与 Han et al. (2026) 的差异化论证不充分\n- Han et al. (2026, EACL Findings) 已将 DIF 应用于 LLM 污染。论文仅用两句话区分。未讨论 continuous vs. binary exposure 的实际效果差异，也未将 Han et al. 方法实现为 baseline。\n- 建议：增加详细 methodological comparison；理想情况下将 Han et al. 实现为 baseline。\n\n## Should-Fix\n\n**W1** [warning] 正文疑似超过 8 页限制\n- Section 6 从 p.8 底部延伸至 p.9，估计正文约 8.3-8.5 页。\n\n**W2** [warning] DID 分析统计效力不足以排除 item-specific effects\n- N=300 items 检测 ~1pp 效应的 power 可能不足。\"absence of evidence ≠ evidence of absence\"。\n- 建议：报告 power analysis 或 minimum detectable effect size。\n\n**W3** [warning] 跨种子稳定性偏弱（n=3 seeds）\n- sign consistency 仅 2/5 agree。大多数模型族的分类学标签对 seed 选择敏感。\n\n**W4** [warning] Algorithm 1 硬编码阈值缺乏充分 justification\n- ≥6 个硬编码阈值，Appendix 仅报告 \"30/30\" 粗粒度结果，缺乏 sensitivity curve。\n\n## Minor\n- M1: \"pp\" 首次使用未定义\n- M2: Gemma-2 排除在 Section 5.2 出现突然\n- M3: Limitations 10 个点可精简至 4-5 个\n- M4: 引用年份问题（holland_1993_dif, lord_1980_irt）\n- M5: Figure 1 浮动体位置需确认\n\n## Missing References\n- Golchin & Surdeanu (2024) \"Time Travel in LLMs\" (ICLR 2024)\n- Sainz et al. (2023) per-benchmark contamination measurement (EMNLP 2023 Findings)\n- Yang et al. (2023) rephrased samples contamination\n\n## 新颖性评估\n新颖性主要来自实验范式而非方法论。Global modulation finding 最强。定位：适合 Findings，borderline Conference。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（新颖性 + Related Work + 写作质量 + 格式合规）\n\n**Overall**: 3.5 — Borderline Conference\n\n## Must-Fix\n\n**N1** [critical] N=4 模型族支撑 4 类分类学，泛化性不足\n- 4 个模型族恰好观测到 4 种模式，可能是 post-hoc 描述。Table 1 每种模式恰好对应一个模型族，加深 overfitting-to-sample 担忧。\"taxonomy\" 的核心价值在于泛化——N=K 分类对 K 个观测无预测力。\n- 建议：增加模型族验证（LLaMA-3, Mistral, Yi）；或将 \"taxonomy\" 改为 \"observed response profiles\"。\n\n**N2** [critical] 与 Han et al. (2026) 的差异化论证不充分\n- Han et al. (2026, EACL Findings) 已将 DIF 应用于 LLM 污染。论文仅用两句话区分。未讨论 continuous vs. binary exposure 的实际效果差异，也未将 Han et al. 方法实现为 baseline。\n- 建议：增加详细 methodological comparison；理想情况下将 Han et al. 实现为 baseline。\n\n## Should-Fix\n\n**W1** [warning] 正文疑似超过 8 页限制\n- Section 6 从 p.8 底部延伸至 p.9，估计正文约 8.3-8.5 页。\n\n**W2** [warning] DID 分析统计效力不足以排除 item-specific effects\n- N=300 items 检测 ~1pp 效应的 power 可能不足。\"absence of evidence ≠ evidence of absence\"。\n- 建议：报告 power analysis 或 minimum detectable effect size。\n\n**W3** [warning] 跨种子稳定性偏弱（n=3 seeds）\n- sign consistency 仅 2/5 agree。大多数模型族的分类学标签对 seed 选择敏感。\n\n**W4** [warning] Algorithm 1 硬编码阈值缺乏充分 justification\n- ≥6 个硬编码阈值，Appendix 仅报告 \"30/30\" 粗粒度结果，缺乏 sensitivity curve。\n\n## Minor\n- M1: \"pp\" 首次使用未定义\n- M2: Gemma-2 排除在 Section 5.2 出现突然\n- M3: Limitations 10 个点可精简至 4-5 个\n- M4: 引用年份问题（holland_1993_dif, lord_1980_irt）\n- M5: Figure 1 浮动体位置需确认\n\n## Missing References\n- Golchin & Surdeanu (2024) \"Time Travel in LLMs\" (ICLR 2024)\n- Sainz et al. (2023) per-benchmark contamination measurement (EMNLP 2023 Findings)\n- Yang et al. (2023) rephrased samples contamination\n\n## 新颖性评估\n新颖性主要来自实验范式而非方法论。Global modulation finding 最强。定位：适合 Findings，borderline Conference。"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-21T07:34:46.797540+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1805
}
```

</details>

---


### Assistant

_source line 662 · 2026-05-21T07:34:49.807581+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 663 · 2026-05-21T07:34:52.524569+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交至 Review Director。

**核心判断**: Overall 3.5 (Borderline Conference)。

**两个 Must-Fix**:
1. N=4 模型族支撑 4 类 taxonomy，每种模式恰对应一个模型族，泛化性证据不足
2. 与 Han et al. (2026) 的差异化仅有两句话描述，缺乏实证对比

**四个 Should-Fix**: 正文疑似超 8 页限制、DID 统计效力不足以排除 item-specific effects、n=3 seeds 稳定性偏弱、Algorithm 1 硬编码阈值缺 sensitivity curve

**三篇遗漏引用**: Golchin & Surdeanu (ICLR 2024)、Sainz et al. (EMNLP 2023 Findings)、Yang et al. (2023) rephrased samples

**最强贡献**: "contamination ≠ inflation" 的 DID + cross-benchmark 证据链。若补充更多模型族验证和 Han et al. 实证对比，可提升至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 664 · 2026-05-21T07:34:58.682655+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 65

## Round 65

2 recorded events


### User

_source line 665 · 2026-05-21T07:37:37.135160+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix

**[AGREE] R2-N1: N=4 模型族支撑 4 类分类学，泛化性不足**

同意此问题的核心关切，但认为严重程度需要适度修正。

补充证据：Table 1 (p.6) 实际展示了 5 个模型（非 4 个），其中 Benefit pattern 同时出现在 Gemma-2 7B 和 OLMo-2 7B 两个不同家族，说明分类并非严格 one-to-one。此外，Section 5.1 的 per-model 分析（seed=42）涵盖了更多 model sizes（Qwen2.5 从 0.5B 到 14B），在 family 内部展示了 size-dependent pattern 变化（如 Qwen 小模型 Benefit vs 大模型 Collapse）。

然而 R2 的核心论点成立：4 个家族不足以声称 taxonomy 的泛化性。特别是：(1) 所有家族都是 2024-2025 年的 decoder-only transformer，缺乏架构多样性（无 MoE、无 encoder-decoder）；(2) Algorithm 1 (p.4) 的 pattern 枚举是从这 4 个家族归纳出来的，无法排除第 5 种 pattern 存在的可能。

R2 建议将 "taxonomy" 改为 "observed response profiles" 是合理且低成本的修改。增加 LLaMA-3/Mistral 验证更能强化论文贡献，但可能超出 revision scope。

**[AGREE with nuance] R2-N2: 与 Han et al. (2026) 的差异化论证不充分**

同意论证需要加强，但不完全同意需要将其实现为 baseline。

Related work (p.2) 确实仅用 "Han et al. (2026) apply psychometric DIF to quantify contamination on item parameters, using group-based binary indicators on naturally contaminated models. ContamCal differs by introducing continuous exposure covariates" 两句话区分，这不够充分。

关键方法论差异值得详细展开：(1) Han et al. 使用 binary group indicator（contaminated vs clean groups），而本文使用 continuous per-item exposure score v_ij——这在统计上是完全不同的建模策略（DIF 是 group comparison，explanatory IRT 是 regression-on-covariate）；(2) Han et al. 无法做 dose-response profiling，因为没有 dosage gradient；(3) 本文的 multi-signal RRF fusion 是独立贡献。

但要求将 Han et al. 实现为 baseline 可能不现实：(1) Han et al. 的方法需要事先知道哪些模型是 "contaminated group"，这在本文的 controlled injection 设定下虽然可行但在实际应用中不可行；(2) 两种方法的 output 不直接可比（binary contamination flag vs continuous contamination estimate）。建议论文增加一个 detailed methodological comparison 段落即可，不必强求 baseline 实现。

---

## Should-Fix

**[AGREE] R2-W1: 正文疑似超过 8 页限制**

确认此问题。从 PDF 视觉检查：Section 6 (Discussion and Conclusion) 起始于 p.8 底部（约页面 75% 处），延伸至 p.9 约 55% 处，之后才是 Limitations 标题。Section 6 在 p.9 上包含至少 6 个 bold 小标题段落（"Diverse patterns, not uniform inflation"、"SFT ecological validity"、"ARC-Challenge bootstrap stability"、"Signal coverage"、"Ensemble size and per-domain power"、"Position bias"、"Diagnostic value beyond aggregate calibration"）。

EMNLP 2026 规则明确要求正文（main text）严格 ≤8 页，Limitations 和 Ethics 不计入。按当前排版，正文约 8.4–8.5 页，超标约 0.4–0.5 页。这是可能导致 desk-reject 的格式问题。

修改方向：Section 6 的多个小标题段落内容与正文 Sections 5.1-5.7 的 findings 高度重叠（例如 "Position bias" 已在 Section 4.1 最后一段讨论过），可大幅压缩或移至 Appendix。

**[AGREE] R2-W2: DiD 分析统计效力不足以排除 item-specific effects**

完全同意。我在自己的审稿意见中将此列为 N3 (critical)。

补充 R2 的论点：Table 4 (p.8) 报告的 DiD 效应量范围为 −0.8pp 到 +0.6pp，在 n=3 seeds 下检测 ~1pp item-specific 效应的 power 极低。论文将 "All DiD non-significant" 直接升级为 "causal evidence that SFT contamination operates through global capability modulation rather than item-specific memorization"（p.1, Abstract; p.6, "Baseline ability gradient" section），这是典型的 absence-of-evidence ≠ evidence-of-absence 问题。至少需要 post-hoc power analysis 报告 MDES，否则因果声明不成立。

**[AGREE] R2-W3: 跨种子稳定性偏弱（n=3 seeds）**

完全同意。我在自己的审稿意见中将此列为 N1 (critical) 并做了更详细的分析。

补充一个 R2 未提到的细节：Section 5.3 (p.7) 自己承认 "strict sign consistency requires all seeds to share the same sign of Δacc(d0)" 但仅 2/5 families 满足此条件。论文随后放宽为 "taxonomy-level consistency"（4/5 families agree），但这个放宽标准（CB-based aggregation rule where mean Δ ≥ 1pp 即算 non-zero）本身降低了分类精度。当一个 taxonomy 需要通过放宽一致性标准才能显示 "stable" 时，这恰好印证了 R2 的担忧。

**[AGREE with nuance] R2-W4: Algorithm 1 硬编码阈值缺乏充分 justification**

部分同意。Algorithm 1 (p.4) 确实使用了多个阈值（τ for significance, r for recovery ratio, 以及 mid-trajectory volatility check 的 δ_max 等）。Appendix K (Table 9) 报告 "30/30 model-seed-threshold combinations" 全部通过，但这是粗粒度的 pass/fail 报告，缺乏 sensitivity curve 展示分类如何随阈值连续变化。

但我认为严重程度应低于 R2 的评估。理由：(1) Table 9 的 30 种组合覆盖了 τ ∈ {0.5, 0.75, 1.0, 1.25, 1.5, 2.0} × r ∈ {1, 1.4, 5, 6, 7} pp，这是一个合理的 grid；(2) 论文的分类主要用 direction（sign of mean Δ）作为 primary criterion（Section 3.4: "adopts direction as the primary taxonomy criterion"），阈值仅影响边缘 case。添加一条 sensitivity curve（classification label vs τ for each family）即可解决此问题，不需要重新设计算法。

---

## Minor

**[AGREE] R2-M1**: "pp" (percentage points) 确实在 Abstract 首次出现时未定义。应在首次使用时括号注明。

**[AGREE] R2-M2**: Section 5.2 (p.6) 中 "Gemma-2 excluded due to catastrophic forgetting" 确实出现突然。建议在首次提及时简要说明原因或指向 Appendix。

**[REBUT] R2-M3**: Limitations 10 个点可精简至 4-5 个。

不同意。EMNLP 2026 要求 Limitations 章节必须存在但不计入页数。当前 Limitations（p.9）覆盖了 scale ceiling、seed sensitivity、cross-seed analysis、ecological validity、format sensitivity、calibration quality 等多个维度，且每点仅 1-2 句话。对于一篇方法论论文，全面列出局限性是负责任的做法。真正的问题不是 Limitations 太长，而是 R2-W1 指出的 Section 6 正文超页——应压缩 Section 6 而非 Limitations。

**[AGREE] R2-M4**: 引用年份问题。我的 reference verification 也发现了 holland_1993_dif 和 lord_1980_irt 的年份不匹配（可能是再版 vs 原版）。应统一为原版年份并核实。

**[AGREE] R2-M5**: Figure 1 浮动体位置应确认不违反 ACL 模板的 float 规范。

---

## Missing References

**[AGREE]** Golchin & Surdeanu (2024) "Time Travel in LLMs" 是直接相关的 contamination detection 工作，应在 Related Work 的 contamination detection 段落中引用。

**[AGREE]** Sainz et al. (2023) 的 per-benchmark contamination measurement 与本文的 per-benchmark analysis 直接相关。

**[AGREE]** Yang et al. (2023) rephrased samples — 我在自己的审稿意见中也建议了此引用。

---

## 新颖性评估回应

R2 将论文新颖性定位为 "实验范式而非方法论"，我部分不同意。

2PL+γ 模型引入 continuous contamination covariate 到 explanatory IRT 框架，在方法论上确实有创新——这不是简单地将现有方法应用到新数据，而是设计了一个新的统计模型来量化 contamination 的 item-level 效应。RRF multi-signal fusion 虽然借用了 IR 技术，但其在 contamination detection 领域的应用和与 IRT 的结合是原创的。

然而 R2 的判断——"Global modulation finding 最强"——我同意。如果 DiD 的 power 问题能解决（增加 seeds 或做 power analysis），这个发现本身足以支撑 Conference 接收。

**总结**：R2 的审稿意见整体准确且建设性。N1（taxonomy 泛化性）和 W1（页数超标）是需要作者认真回应的问题。W2 和 W3 与我的 N1/N3 高度一致，交叉验证了这些问题的严重性。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 666 · 2026-05-21T07:37:43.519399+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 意见的回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 66

## Round 66

2 recorded events


### User

_source line 667 · 2026-05-21T07:37:50.883406+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。总结：

- **N1 (taxonomy 泛化性)**: AGREE，但指出 Table 1 实际有 5 个模型且 Benefit 跨 2 个家族，严重程度需修正
- **N2 (Han et al. 差异化)**: AGREE 需加强论证，但 REBUT 要求实现为 baseline（两种方法 output 不直接可比）
- **W1 (页数超标)**: AGREE，确认正文约 8.4-8.5 页，Section 6 需大幅压缩
- **W2 (DiD power)**: AGREE，与我的 N3 完全一致
- **W3 (n=3 seeds)**: AGREE，与我的 N1 完全一致
- **W4 (硬编码阈值)**: 部分 AGREE，但严重程度低于 R2 评估
- **M3 (Limitations 长度)**: REBUT——问题在于 Section 6 超页，而非 Limitations 太长
- 其余 Minor 和 Missing References 均 AGREE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 668 · 2026-05-21T07:38:08.667532+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 67

## Round 67

12 recorded events


### User

_source line 669 · 2026-05-21T07:38:36.278712+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: Cross-seed stability 声明与 n=3 样本量严重不匹配**

同意。我在自己的审稿中提出了相同问题（我的 W3）。Table 3 明确显示 taxonomy-level sign consistency 仅 2/5 families 通过（Qwen-14B 和 Gemma-2），这意味着多数模型族的分类标签对 seed 敏感。n=3 下 bootstrap 置信水平确实极低。

补充一点：论文采用了三重 convergent evidence 策略（cross-seed direction + cross-benchmark replication + dose-response shape stability，Section 5.3），这部分缓解了单一标准下的不稳定性。但 R1 的核心论点成立——如果 taxonomy 是核心贡献，n=3 的统计基础不够。建议优先级应为：增加 seeds > 降低 claim 力度。

**[REBUT] R1-N2: IRT identifiability 在 J=13–16 下"刚好处于边界"**

R1 对此问题的定性有误。论文的实证数据实际上表明 J=13–16 **不在**边界上，而是在安全区间内：

1. **Appendix P (p.17) Linear DGP 结果**：论文明确报告 "Under the Linear DGP, 95% CI coverage is nominal (≥0.93) at all J"——包括 J=16 在内的所有 ensemble sizes 均满足名义覆盖率。R1 引用的 "coverage 仅 0.70" 出现在 **Threshold DGP 的 J=500** 条件下（Table 11），这比实证 J 大了 30 倍以上，不适用于当前分析。

2. **Coverage 随 J 增大下降的原因**（也回应 R1-Q1）：论文在 Appendix P "Implications" 段落解释了这一点——当真实 DGP 是阶跃函数（threshold）而模型假设线性时，更多数据使模型更自信地收敛到一个有偏的点估计上（model misspecification bias），导致 CI 变窄但覆盖率下降。这恰恰说明**小 J 下 CI 反而更保守（更宽）**，coverage 更好，这对论文的探索性分析是有利的。

3. **论文已有自我校准**：Section 5.5 和 Appendix B 明确指出 "recovery requires AUC>0.55 at J ≥ 16"，且论文在 Limitations 中承认 "the prior sensitivity confirms the exploratory status of γ-based conclusions at current ensemble sizes"。

**但我同意 R1 的一个子论点**：Appendix P 的 DGP simulation 使用 uniform exposure 分布，而实际 RRF exposure 是 right-skewed 的（Section 3.2 报告 mean=0.041, median=0.016）。Skewed exposure 可能引入 leverage effect（R1-Q2），应在 simulation 中验证。这一遗漏值得标注为 Should-Fix 而非 Critical。

**[AGREE] R1-N3: DID null result 可能是 power 不足**

完全同意。这与我的 W2 一致。Table 4 报告 DID 范围 −0.8 到 +0.6pp，但在 n=3 seeds、300 filtered items 的条件下，检测 ~1pp item-specific effect 的 statistical power 未知。论文从 "All DID non-significant" 直接推论 "contamination operates via global capability modulation rather than item-specific memorization"（Section 5.4 及 Introduction Contribution 2），这是 absence-of-evidence ≠ evidence-of-absence 错误。R1 建议弱化为 "we find no evidence of item-specific memorization at the current power level" 是合理且容易实施的修改。

补充：Figure 2 的 "symmetry" 声明（"Difficulty-stratified analysis confirms symmetry (gap < 0.1pp across all bins)"）确实依赖视觉判断而非正式对称性检验（如 paired t-test across bins）。

---

### Should-Fix

**[AGREE] R1-W1: RRF fusion 缺乏 calibration 验证**

同意这是一个方法论缺口。论文未报告：(1) RRF score 与真实 contamination 程度的校准关系；(2) S1-S4 之间的 rank correlation；(3) leave-one-signal-out 消融。

不过，部分缓解因素值得注意：Section 5.6 讨论了 signal failure modes（Min-K%++ 在 0.5B 处反转，S4 在 <1.5B 处近随机），Appendix B 提供了 AUC-based recovery analysis（Figure 4/5）。此外，IRT 模型的 γ 估计本身对输入信号的噪声有一定鲁棒性（因为 γ 是从整个 response matrix 联合估计的，不完全依赖单项信号）。但 leave-one-signal-out 消融实验仍然是应该做的。

**[AGREE] R1-W2: SFT ecological validity**

同意这一局限存在。论文 Limitations 部分已讨论了 SFT vs. pretraining 的差异，并指出 "Pretraining-stage leakage... may produce qualitatively different contamination signatures"。AUGMENT mode 进一步增加了与真实场景的距离。

但需要公允地指出：(1) 控制实验**必须**在某种受控条件下操作——pretraining-level manipulation 对 4 个 7-14B 模型族意味着数千 GPU-hours 的成本，不切实际；(2) 论文选择 SFT+LoRA 注入是该领域当前的标准做法（与 Sun et al. 2025, Xu et al. 2025/DCR 等工作一致）。这是一个"已知但无法在当前资源下完全解决"的局限，不应成为拒稿理由。

**[REBUT] R1-W3: Baseline 比较中 ContamCal 优势不够显著**

R1 指出 GSM8K 上 B4-LinearRegression (MAE=0.003) 优于 ContamCal (MAE=0.020)。这一事实正确，但**比较维度不完整**：

1. **ContamCal 在 MMLU 上 MAE=0.006 是所有方法最优**（Table 5），在 ARC 上 MAE=0.035 也是最优。GSM8K 是三个 benchmark 中表现最弱的一个，但 GSM8K 的开放生成格式和较小 item pool 使其天然不适合 IRT 建模（论文 Section 4.2 注明 GSM8K 仅 1,319 items）。

2. **MAE 不是 ContamCal 的核心价值主张**。ContamCal 的独特优势在于：(a) **uncertainty quantification**——credible intervals 而非点估计（Table 5 显示 B4-LinearRegression 无 CI）；(b) **domain-level diagnosis**——Section 5.7 + Figure 7 展示了按认知领域分解的污染效应（如 Social Sciences 显著，STEM 最大位移），B4 无法提供这一粒度；(c) **per-item γ 估计**——允许识别哪些 items 对污染最敏感。

3. **Table 5 的 B6-DCR 列多处为 dash (—)**，说明某些 baselines 在部分条件下不可用，而 ContamCal 是唯一在所有三个 benchmark 上均有完整结果且提供不确定性量化的方法。

因此，单以 GSM8K MAE 一个数据点否定 ContamCal 的比较优势不够公允。

**[AGREE] R1-W4: Bayesian/frequentist 术语混用**

同意这是写作问题，在我的审查范围内。论文使用 Stan/NUTS（Bayesian MCMC）做 IRT 推断，但多处出现 "significant"（Section 5.4 DID 分析）、"p-value"（实际是 PPP/posterior predictive p-value，但未明确区分）。建议统一：Bayesian 框架下使用 "credible interval" 而非 "confidence interval"，DID 分析若用 frequentist 框架应明确说明方法论切换。

---

### Minor

**[AGREE] R1-M1**: Algorithm 1 的 default τ 值应在主文或 caption 中注明，不应让读者去翻 Appendix L。

**[REBUT] R1-M2**: Section 3.2 (p.3) 明确描述了 4 个信号（S1 Embedding similarity, S2 Min-K%++, S3 ConStat, S4 Self-Entropy），并说明 "Our primary pipeline uses the remaining three signals (S={S1, S2, S4})"，S3 和 S4 需要配对 paraphrase sets 因此不总是可用。300 RRF-filtered items 的信号选择在方法描述中是清楚的，但可以在 Section 5.4 首次引用时加一句澄清。

**[AGREE] R1-M3**: 模型排除标准在 Appendix G 中有详细说明（16 models 中排除 2 个），但主文中引用不够显眼。建议在 Section 4.1 明确加一句指向 Appendix G 的引用。

**[AGREE] R1-M4**: Figure 1 应在 caption 中标注是哪个 seed 的结果（或注明是所有 seeds 的代表性结果）。

**[AGREE] R1-M5**: Eq. (2)（p.3）定义了 decontaminated score 为 "posterior expectation under zero exposure"，表达式涉及后验积分。该定义本身清晰，但从实用角度看，读者可能不清楚具体计算路径——是对每个 MCMC sample 设 ν=0 然后取均值，还是有解析近似？建议加一句实现说明。

**[AGREE] R1-M6**: 引用年份问题我也在自己的审稿中标注了（我的 M4）。`holland_1993_dif` 在 OpenAlex 中匹配到 2009 年版本，`lord_1980_irt` 匹配到 2012 再版。

---

### Questions 回应

**R1-Q1** (CI coverage 随 J 增大下降)：已在上方 N2 REBUT 中详细回答。核心原因是 model misspecification bias——当真实 DGP 是 threshold 而模型假设线性时，J 越大偏差越被精确化，CI 变窄但偏离真值。这反而说明小 J 下的结论更保守、更安全。

**R1-Q2** (RRF skewed distribution 的 leverage effect)：同意这是一个未被验证的风险。论文报告 RRF mean=0.041, median=0.016（Section 3.2），分布严重右偏。少数高曝光 items 可能 disproportionately 驱动 γ 估计。Appendix P 的 DGP simulation 应加入 skewed exposure 条件来验证。

**R1-Q3** (低剂量跨 benchmark transfer)：Table 2 仅报告 d100 的跨 benchmark 结果。低剂量（如 d005/d025）下的 transfer pattern 确实缺失。但 Table 1 中低剂量的 within-benchmark 效应已经很小（多数 ≤1pp），跨 benchmark transfer 在信噪比极低的情况下很难有意义地检测。

**R1-Q4** (0.5B position bias 与 small models)：论文在 Section 4.1 明确排除了 0.5B 模型不做 MC IRT 分析（"We exclude 0.5B from MC IRT due to position bias"），说明作者认为 0.5B 的 dose-response 可能由 position bias 主导而非反映真实 contamination dynamics。这是否暗示 small models 有完全不同的 dose-response 是一个有趣的开放问题，但在当前框架下无法回答。

---

### Missing References 回应

**Yang et al. (2023)**: [AGREE] — 我在自己的审稿中也标记了这篇（我的 Missing References #3）。该工作证明 rephrasing 可绕过 string-matching decontamination，与 ContamCal S3 (ConStat) 信号的设计动机直接相关。

**Recht et al. (2019)**: [AGREE] 但优先级较低。该工作关于 benchmark overfitting / distribution shift，与 contamination 有交集但并非直接相关。可在 Related Work 中一句话带过。

**Bakhtin et al. (2024)**: [REBUT] — 该工作关于 pretraining deduplication，属于数据预处理/清洗范畴，与本文的 contamination 检测和 IRT 校准主题的关联较远。不认为是必须引用的工作。

---

### 总结

R1 和我（R2）在以下问题上完全一致：
- **n=3 seeds 不足以支撑 taxonomy stability claims**（R1-N1 = 我的 W3）
- **DID null result 存在 power 问题**（R1-N3 = 我的 W2）
- **Bayesian/frequentist 术语需统一**（R1-W4）
- **引用年份问题**（R1-M6 = 我的 M4）

我对 R1 有一个主要反驳：**R1-N2 关于 IRT identifiability "处于边界" 的判断过于严厉**。论文的 Appendix P 数据明确显示 J=13-16 下 Linear DGP coverage ≥0.93，coverage 降至 0.70 仅出现在 J=500 的 Threshold DGP 条件下。R1 将这一远离实证条件的极端结果作为主要 critical issue 有失公允。但 skewed exposure 的 simulation gap 是真实的 Should-Fix。

我同时保留自己审稿中 R1 未覆盖的问题：
- **N=4 模型族支撑 4 类 taxonomy 的泛化性**（我的 N1）
- **与 Han et al. (2026) 的差异化论证不充分**（我的 N2）
- **正文可能超过 8 页限制**（我的 W1）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-21T07:38:55.362841+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-21T07:38:55.620184+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T07:25:33.469177+00:00\", \"completed_at\": \"2026-05-21T07:30:14.860546+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-3\", \"message\": \"连续 3 页纯文本，无任何 display item（figure/table/algorithm）。审稿人打开 PDF 后前 3 页看不到视觉锚点，直到第 4 页才出现 Algorithm 1，第 6 页才出现首个 figure 和 table。对于实证为主的论文，建议将核心结果图或方法概览图提前至第 1-2 页，在审稿人形成第一印象的窗口期内建立视觉锚定。\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"Figure 1 作为全文首个 figure 出现在第 6 页，且为单栏宽度，尺寸偏小。内部颜色元素和文字在当前尺寸下可读性受限，部分文字与周围内容间距紧凑。作为论文的主要视觉锚点，建议改用 figure*（双栏全宽）增大尺寸并提前放置。\"}, {\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"主文本（Section 1 Introduction 至 Section 6 Discussion and Conclusion）延伸至第 9 页约 40% 处才进入 Limitations 段。虽然 Limitations 和 Ethics Statement 不计入页数，但 Section 6 正文内容已超出第 8 页，需用 LaTeX 编译确认是否超出 EMNLP 2026 的 8 页主文本限制。\"}, {\"severity\": \"warning\", \"dimension\": \"page 18\", \"message\": \"最后一页（附录末页）Tables 12 和 13 下方约 60% 面积为空白。可重组附录内容填充或将小表格合并以消除大面积留白。\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"纯文本页（Experimental Setup + Results 开头），位于 Algorithm 1（第 4 页）和 Table 1/Figure 1（第 6 页）之间，导致正文中间出现连续 2 页（pages 4 下半-5）无 figure/table 的视觉断档。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Algorithm 1 伪代码框格式规范、逻辑清晰，但作为全文第一个 display item 出现在第 4 页，审稿人需翻过 3 页纯文本才能看到。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1 使用颜色编码展示 dose-response pattern，需确认配色方案是否色盲友好（避免纯红绿对比）。\"}, {\"severity\": \"info\", \"dimension\": \"pages 6-8\", \"message\": \"Tables 1-5 均使用 booktabs 风格（\\\\toprule/\\\\midrule/\\\\bottomrule），无竖线，排版专业。Table 5 中最优值加粗标注，符合规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 散点图清晰可读，caption 自包含，数据点可区分。Table 4 和 Table 5 同页布局紧凑但不拥挤。\"}, {\"severity\": \"info\", \"dimension\": \"pages 14, 16\", \"message\": \"附录 Figures 3, 4, 7 为多面板小图，轴标签和 tick mark 文字偏小，建议确认字号 ≥8pt 以保证打印可
…[truncated 432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 257
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-21T07:38:55.671036+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-21T07:38:55.873041+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-21T07:40:11.456227+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:update_review_issues,submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:update_review_issues,submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-21T07:40:11.558555+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-21T07:43:34.685478+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form but framing still inconsistent.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D149+ rewrite: Title changed to 'Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families'. Paper repositioned as systematic empirical investigation of dose-response across 5 models (7B-14.7B) from 4 families. No over-scoping.\"\n  resolution_round: 7\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. All claims must be scoped to 'under SFT injection at ≤3B scale'.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Conclusion 'applies directly to settings with larger effects' is unsupported forward claim.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised as Should-Fix (R1-W2). Both agree SFT ecological validity is a known limitation. Resolution still adequate: Limitations paragraph covers this; controlled injection is standard methodology (Sun et al. 2025, Xu et al. 2025). Not a rejection reason per R2.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims to 'under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Ensure Abstract first sentence explicitly scopes to SFT injection\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Remove/caveat Conclusion 'applies directly' claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D149+ rewrite: Paper now covers 7B-14.7B. Conclusion says 'Pretraining contamination may produce qualitatively different effects' (caveat). Limitations has full SFT ecological validity paragraph. R8 re-raised as Should-Fix but resolution adequate.\"\n  resolution_round: 7\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation has two interpretations: genuine null vs model misspecification.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Both unanimously re-raise as critical. R2 proposes threshold DGP simulation.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。DGP robustness appendix (Appendix P) addresses this.\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i interaction model\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'under the additive linear specification' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Run threshold DGP simulation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 7, action: \"Write DGP robustness appendix + update Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"400-run threshold DGP simulation completed. Appendix P written. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction + underpowered J\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Bonferroni α=0.00625; CI upper bound likely includes zero.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Social Sciences at 99.1% does not pass Bonferroni. Report corrected result.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text §5.4 still presents J=13. Both AGREE: use J=16 in main text.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。J=16 now in main text, P(γ<0)=99.7% crosses Bonferroni threshold.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'uncorrected for multiplicity' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text domain γ to J=16 results\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Results §5 reports J=16 for domain γ. P(γ<0)=99.7% at J=16 crosses Bonferroni threshold. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations — IRT results unreliable\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at all J. Table 3 needs PPP annotation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003. Move ARC IRT to Appendix.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"ARC IRT moved to Appendix. §5.1 still mentions 'ARC exhibits the same pattern' which may mislead.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。ARC IRT in Appendix with PPP caveat.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Move ARC IRT results to Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Clarify ARC IRT parameters are unreliable\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"ARC IRT in Appendix sec:arc_irt with PPP<0.05 caveat. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality; MAE random control missing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. No direct RRF vs S1-only ablation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation complete: S1-only causes MCMC non-convergence. Both AGREE: RRF for exposure VARIANCE not signal QUALITY. Downgraded to warning.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Random 300-item subsets report τ but no MAE comparison.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"R1-W1 re-raises RRF calibration verification gap: no signal rank correlation, no leave-one-signal-out ablation, no calibration plot. R2 agrees but notes γ joint estimation provides partial robustness. Random MAE comparison now present (§5.4: 0.039±0.008 vs 0.006).\"}\n  action_items:\n    - {round: 3, action: \"Reword C2\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Distinguish exposure variance from signal quality\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Report MAE for random 300-item subsets\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 8, action: \"Report inter-signal rank correlation and leave-one-signal-out ablation\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"Random MAE comparison resolved (R7). New calibration verification gap raised in R8 (signal rank correlation + ablation).\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal — over-coverage and under-coverage have different root causes\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results. MMLU 95% CI covers 100% = uninformative.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Root cause diagnosis still insufficient. MMLU over-coverage = wide posteriors; ARC under-coverage = structural misfit.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。Root-cause diagnosis now in §5.4.\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage to main results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Discuss root causes separately\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Provide explicit root-cause diagnosis\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Root-cause diagnosis in §5.4. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses — J=13 domain finding vs J≥50 standard is self-contradictory\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Most interesting finding uses weakest configuration (J=13).\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text still uses J=13. Both AGREE use J=16.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。§5 opening now specifies J=16 for domain γ.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J prominently in each table\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rerun domain-level γ at J=16\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text to J=16; add model set overview at §5 start\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Results §5 specifies J=16 for domain γ. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Mean a_i comparison shows no discrimination confound. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 may reflect higher average a_i.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised. Resolution confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — caveat adequate but MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Phantom reference to Appendix E.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"MAE CI for cross-family pool not reported. Minor residual.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未直接提及此 issue。Cross-family analysis now uses 5 models from 4 families (§4.1). MAE CI still not reported.\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Remove phantom Appendix E reference\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rename §5.5 to 'Cross-Family Exploratory Analysis'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Full prior sensitivity complete. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised. Prior sensitivity in Appendix C.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2)\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Conclusion scoped. Hypothesis labeled post-hoc. Not re-raised in R8.\"\n  resolution_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption but no direct evidence.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must be scoped to 'under SFT injection'.\"}\n    - {round: 6, reviewers: \"\", note: \"Not independently re-raised. Scoped and labeled post-hoc.\"}\n  action_items:\n    - {round: 4, action: \"Reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Scope Conclusion Min-K++ claim to 'at the 0.5B scale under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure — C2 (signal filtering) partially disconnected from main question\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"3 empirical contributions. Not re-raised in R8.\"\n  resolution_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span too many types. Consolidate to 2-3.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Now 3 contributions but still span different types.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 reads like method paper contribution.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further consolidate to 2 contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reframe C2 as enabling analysis + standalone practical finding\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — DIF classics + contamination benchmark literature\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. EACL 2026 most direct concurrent work.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"New gaps: Lord, Hambleton, HELM, Magar & Schwartz.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al. needed.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"New missing refs: Golchin & Surdeanu (ICLR 2024), Sainz et al. (EMNLP 2023 Findings), Yang et al. (2023). R1 also suggests Recht et al. (2019).\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al., arXiv 2601.04301, Chen et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM, Magar & Schwartz\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Expand Han et al. comparison\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Add Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Add Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"R6 refs added. R8 identifies 3 additional missing refs.\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"PPP values filled. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'.\"}\n    - {round: 5, reviewers: \"\", note: \"PPP values now present. Resolved.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high — still ~6+ quantitative claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Abstract rewritten for dose-response taxonomy paper. Numbers serve distinct narrative purposes. Not re-raised in R8.\"\n  resolution_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"~202 words but still 8-9 numbers.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Still 6+ numbers.\"}\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF; must commit to empirical study positioning\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must position as empirical contribution.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 still reads as method. Reposition around controlled testbed + identifiability.\"}\n    - {round: 8, reviewers: \"R2\", note: \"R2 notes novelty primarily comes from experimental paradigm not methodology (IRT+DIF has precedent). R1 partially disagrees—argues continuous covariate in explanatory IRT is original.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al. as concurrent work\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Explicitly state empirical investigation positioning\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reposition Han et al. differentiation; elevate J≥50 identifiability\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Paper committed to empirical investigation. Title signals empirical finding. 3 empirical contributions.\"\n  resolution_round: 7\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. differentiation needs rework\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. Han et al. comparison needs expansion.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Han et al. differentiation self-undermining. Add DIF classics.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2-N2 re-raises Han et al. differentiation as critical: only 2 sentences, no empirical comparison, unclear whether continuous vs binary exposure actually improves results. R1 agrees need more detail but rebuts requiring baseline implementation.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite Han et al., Schaeffer et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM, Magar & Schwartz + expand Han et al.\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Rework Han et al. differentiation; add DIF classics\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Add ~0.5 page detailed methodological comparison with Han et al. (assumptions, inputs, outputs, scope)\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Page limit — needs compile verification\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Main content ~8.5 pages. Desk-reject risk.\"}\n    - {round: 6, reviewers: \"R2\", note: \"Cannot confirm page count without compilation.\"}\n    - {round: 7, reviewers: \"\", note: \"Compiled and verified: 17 pages total (8 pages main text + references + appendix). EMNLP 2026 compliant.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised. Section 6 extends to p.9 ~40-55%. Both reviewers and visual check agent confirm main text exceeds 8 pages by ~0.4-0.5 page. Desk-reject risk.\"}\n  action_items:\n    - {round: 5, action: \"Move ARC IRT to Appendix; compress; move domain γ table to Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Compile and verify ≤8 pages main content\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Compress Section 6 Discussion—move overlapping content to Appendix. Section 6 must end within page 8.\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"k reserved for benchmark, d for domain. Not re-raised in R8.\"\n  resolution_round: 7\n  mentions:\n    - {round: 5, reviewers: \"R2\", note: \"k = benchmark in §3.1 but k = stratum in Eq.2.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Use different symbol for strata.\"}\n  action_items:\n    - {round: 5, action: \"Add clarifying note when k meaning changes\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Replace k with different symbol for strata index\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R6-W1\"\n  summary: \"SFT data composition confound — injection replaces or augments general SFT data unclear\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper explicitly states AUGMENT mode. Volume confound discussed with 3 counter-arguments. Not re-raised in R8.\"\n  resolution_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"§4.1 does not specify whether benchmark items replace or augment general SFT corpus.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。§4.1 and Limitations now clearly state AUGMENT mode.\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol: replacement vs augmentation\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R6-W2\"\n  summary: \"S4 (Self-Critique) signal computation details insufficient for reproduction\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R2\", note: \"Prompt design, evaluation distribution construction, and scoring mechanism not described.\"}\n    - {round: 8, reviewers: \"\", note: \"Appendix E (S4 Self-Critique Signal Details) now provides prompt, logit extraction, and scoring formula.\"}\n  action_items:\n    - {round: 6, action: \"Add S4 computation details in appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix E added with S4 details.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported — convergence verification missing\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R1\", note: \"Training convergence is prerequisite for controlled injection validity.\"}\n    - {round: 8, reviewers: \"\", note: \"Appendix F (Training Convergence) now reports final training loss by dosage. Minimal but present.\"}\n  action_items:\n    - {round: 6, action: \"Report SFT training curves or convergence verification in Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix F added with convergence info.\"\n  resolution_round: 8\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"Cross-family GSM8K PPP=0.83 but within-family GSM8K PPP not reported.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。Still not reported in current version.\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 8 (Fresh Review) New Issues ===\n\n- id: \"R8-N1\"\n  summary: \"Cross-seed stability claims overstated — n=3 seeds insufficient for taxonomy validation\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Both reviewers independently flag this as critical. n=3 seeds yields wide CIs; strict sign consistency only 2/5 families. Taxonomy-level aggregation rule relaxes criteria to show 4/5 consistency, but this relaxation itself undermines confidence. R1: 'any variance estimate at n=3 has extremely wide CIs'. R2: 'most families' taxonomy labels are seed-sensitive'.\"}\n  action_items:\n    - {round: 8, action: \"Increase seeds to n≥5 for ≤3B models (computationally feasible); or weaken claims to 'preliminary taxonomy under limited replication'\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Report bootstrap CI covering seed variability explicitly\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N2\"\n  summary: \"DiD null result lacks power analysis — 'causal evidence for global modulation' claim unsupported\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Both reviewers independently flag. DiD values range −0.8 to +0.6pp; power to detect ~1pp item-specific effect at n=3 unknown. Abstract/Intro claim 'causal evidence' but absence of significance ≠ evidence of absence. Figure 2 symmetry claim is visual, not formally tested.\"}\n  action_items:\n    - {round: 8, action: \"Run post-hoc power analysis reporting minimum detectable effect size (MDES)\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Weaken 'causal evidence for global modulation' to 'no detectable item-specific effect at current power level'\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N3\"\n  summary: \"N=4 model families supporting 4-class taxonomy — generalization evidence insufficient\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2 raises as N1 critical. R1 agrees with nuance (notes 5 models, Benefit shared by 2 families). Core concern: 4 patterns observed on 4 families is post-hoc description, not predictive taxonomy. No out-of-sample validation. Algorithm 1 pattern enumeration derived from same 4 families—cannot exclude 5th pattern.\"}\n  action_items:\n    - {round: 8, action: \"Option A: Add 1-2 more model families (LLaMA-3/Mistral) at 1-2 dosage levels for quick validation\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Option B: Replace 'taxonomy' with 'observed response profiles' throughout; add Discussion paragraph on model attributes (training data, architecture) → pattern hypotheses\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N4\"\n  summary: \"Han et al. (2026) differentiation insufficient — only 2 sentences, no empirical comparison\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2 raises as N2 critical. Han et al. (EACL 2026 Findings) is most direct prior work applying DIF to LLM contamination. Current differentiation: 2 sentences in Related Work. Missing: (1) continuous vs binary exposure effect comparison; (2) robustness under noisy signals; (3) when group-based DIF is preferable. R1 agrees differentiation needed but rebuts requiring baseline implementation (different output types).\"}\n  action_items:\n    - {round: 8, action: \"Add ~0.5 page methodological comparison with Han et al. covering assumptions, input requirements, output granularity, and applicability scope\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W1\"\n  summary: \"Bayesian and frequentist terminology mixed throughout paper\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R1 raises as W4. R2 agrees. Paper uses Bayesian MCMC (Stan/NUTS) for IRT but 'significant', 'p-value', 'confidence interval' appear in frequentist sense. DiD analysis (Table 4) appears frequentist (p > .05) without explicit framework label. PPP vs frequentist p not distinguished.\"}\n  action_items:\n    - {round: 8, action: \"Unify terminology: use 'credible interval' for Bayesian CIs; explicitly label DiD as frequentist; distinguish PPP from frequentist p-value\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W2\"\n  summary: \"IRT identifiability simulation uses uniform exposure — mismatch with empirical right-skewed RRF distribution\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R1 raises as part of N2 critical. R2 rebuts the 'critical' severity (J=13-16 coverage ≥0.93 under Linear DGP) but agrees skewed exposure gap is real Should-Fix. Empirical RRF: mean=0.041, median=0.016, highly right-skewed. Simulation uses uniform. Few high-exposure items may create leverage effect on γ.\"}\n  action_items:\n    - {round: 8, action: \"Re-run identifiability simulation with right-skewed exposure matching empirical RRF distribution\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-W3\"\n  summary: \"Algorithm 1 threshold sensitivity — only pass/fail grid reported, no continuous sensitivity curve\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R2,R1\", note: \"R2 raises as W4. R1 partial agree (severity lower than R2's assessment). Appendix K Table 9: 30/30 pass is too coarse. No sensitivity heatmap showing how classification changes continuously with threshold.\"}\n  action_items:\n    - {round: 8, action: \"Add threshold sensitivity heatmap in Appendix (τ × σ classification matrix per family)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M1\"\n  summary: \"Missing references — Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Both reviewers flag Yang et al. (2023). R2 additionally flags Golchin & Surdeanu (ICLR 2024, contamination detection via guided instruction) and Sainz et al. (EMNLP 2023 Findings, per-benchmark contamination measurement). R1 also suggests Recht et al. (2019) on benchmark overfitting.\"}\n  action_items:\n    - {round: 8, action: \"Add Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023) to Related Work\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M2\"\n  summary: \"Minor writing issues — 'pp' undefined, Gemma-2 exclusion abrupt, Figure 1 caption incomplete, Eq.2 computation unclear\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2-M1: 'pp' not defined at first use. R2-M2: Gemma-2 GSM8K exclusion appears suddenly in §5.2. R1-M4: Figure 1 caption doesn't note seed=42. R1-M5: Eq.2 decontamination computation path unclear (per-MCMC-sample zero-out vs analytic). R1/R2-M6/M4: holland_1993_dif and lord_1980_irt year discrepancies.\"}\n  action_items:\n    - {round: 8, action: \"Fix minor writing issues: define 'pp', add Gemma-2 exclusion note in §4, add seed label to Figure 1 caption, clarify Eq.2 computation, verify bib years\", assigned_to: \"paper_agent\", status: \"open\"}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form but framing still inconsistent.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D149+ rewrite: Title changed to 'Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families'. Paper repositioned as systematic empirical investigation of dose-response across 5 models (7B-14.7B) from 4 families. No over-scoping.\"\n  resolution_round: 7\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. All claims must be scoped to 'under SFT injection at ≤3B scale'.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Conclusion 'applies directly to settings with larger effects' is unsupported forward claim.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised as Should-Fix (R1-W2). Both agree SFT ecological validity is a known limitation. Resolution still adequate: Limitations paragraph covers this; controlled injection is standard methodology (Sun et al. 2025, Xu et al. 2025). Not a rejection reason per R2.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims to 'under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Ensure Abstract first sentence explicitly scopes to SFT injection\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Remove/caveat Conclusion 'applies directly' claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D149+ rewrite: Paper now covers 7B-14.7B. Conclusion says 'Pretraining contamination may produce qualitatively different effects' (caveat). Limitations has full SFT ecological validity paragraph. R8 re-raised as Should-Fix but resolution adequate.\"\n  resolution_round: 7\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation has two interpretations: genuine null vs model misspecification.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Both unanimously re-raise as critical. R2 proposes threshold DGP simulation.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。DGP robustness appendix (Appendix P) addresses this.\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i interaction model\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'under the additive linear specification' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Run threshold DGP simulation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 7, action: \"Write DGP robustness appendix + update Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"400-run threshold DGP simulation completed. Appendix P written. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction + underpowered J\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Bonferroni α=0.00625; CI upper bound likely includes zero.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Social Sciences at 99.1% does not pass Bonferroni. Report corrected result.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text §5.4 still presents J=13. Both AGREE: use J=16 in main text.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。J=16 now in main text, P(γ<0)=99.7% crosses Bonferroni threshold.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'uncorrected for multiplicity' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text domain γ to J=16 results\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Results §5 reports J=16 for domain γ. P(γ<0)=99.7% at J=16 crosses Bonferroni threshold. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations — IRT results unreliable\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at all J. Table 3 needs PPP annotation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003. Move ARC IRT to Appendix.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"ARC IRT moved to Appendix. §5.1 still mentions 'ARC exhibits the same pattern' which may mislead.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。ARC IRT in Appendix with PPP caveat.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Move ARC IRT results to Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Clarify ARC IRT parameters are unreliable\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"ARC IRT in Appendix sec:arc_irt with PPP<0.05 caveat. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality; MAE random control missing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. No direct RRF vs S1-only ablation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation complete: S1-only causes MCMC non-convergence. Both AGREE: RRF for exposure VARIANCE not signal QUALITY. Downgraded to warning.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Random 300-item subsets report τ but no MAE comparison.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"R1-W1 re-raises RRF calibration verification gap: no signal rank correlation, no leave-one-signal-out ablation, no calibration plot. R2 agrees but notes γ joint estimation provides partial robustness. Random MAE comparison now present (§5.4: 0.039±0.008 vs 0.006).\"}\n  action_items:\n    - {round: 3, action: \"Reword C2\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Distinguish exposure variance from signal quality\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Report MAE for random 300-item subsets\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 8, action: \"Report inter-signal rank correlation and leave-one-signal-out ablation\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"Random MAE comparison resolved (R7). New calibration verification gap raised in R8 (signal rank correlation + ablation).\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal — over-coverage and under-coverage have different root causes\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results. MMLU 95% CI covers 100% = uninformative.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Root cause diagnosis still insufficient. MMLU over-coverage = wide posteriors; ARC under-coverage = structural misfit.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。Root-cause diagnosis now in §5.4.\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage to main results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Discuss root causes separately\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Provide explicit root-cause diagnosis\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Root-cause diagnosis in §5.4. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses — J=13 domain finding vs J≥50 standard is self-contradictory\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Most interesting finding uses weakest configuration (J=13).\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text still uses J=13. Both AGREE use J=16.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。§5 opening now specifies J=16 for domain γ.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J prominently in each table\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rerun domain-level γ at J=16\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text to J=16; add model set overview at §5 start\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Results §5 specifies J=16 for domain γ. Not re-raised in Round 8.\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Mean a_i comparison shows no discrimination confound. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 may reflect higher average a_i.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised. Resolution confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — caveat adequate but MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Phantom reference to Appendix E.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"MAE CI for cross-family pool not reported. Minor residual.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未直接提及此 issue。Cross-family analysis now uses 5 models from 4 families (§4.1). MAE CI still not reported.\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Remove phantom Appendix E reference\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rename §5.5 to 'Cross-Family Exploratory Analysis'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Full prior sensitivity complete. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised. Prior sensitivity in Appendix C.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2)\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Conclusion scoped. Hypothesis labeled post-hoc. Not re-raised in R8.\"\n  resolution_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption but no direct evidence.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must be scoped to 'under SFT injection'.\"}\n    - {round: 6, reviewers: \"\", note: \"Not independently re-raised. Scoped and labeled post-hoc.\"}\n  action_items:\n    - {round: 4, action: \"Reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Scope Conclusion Min-K++ claim to 'at the 0.5B scale under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure — C2 (signal filtering) partially disconnected from main question\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"3 empirical contributions. Not re-raised in R8.\"\n  resolution_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span too many types. Consolidate to 2-3.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Now 3 contributions but still span different types.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 reads like method paper contribution.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further consolidate to 2 contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reframe C2 as enabling analysis + standalone practical finding\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — DIF classics + contamination benchmark literature\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. EACL 2026 most direct concurrent work.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"New gaps: Lord, Hambleton, HELM, Magar & Schwartz.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al. needed.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"New missing refs: Golchin & Surdeanu (ICLR 2024), Sainz et al. (EMNLP 2023 Findings), Yang et al. (2023). R1 also suggests Recht et al. (2019).\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al., arXiv 2601.04301, Chen et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM, Magar & Schwartz\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Expand Han et al. comparison\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Add Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Add Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"R6 refs added. R8 identifies 3 additional missing refs.\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"PPP values filled. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'.\"}\n    - {round: 5, reviewers: \"\", note: \"PPP values now present. Resolved.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high — still ~6+ quantitative claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Abstract rewritten for dose-response taxonomy paper. Numbers serve distinct narrative purposes. Not re-raised in R8.\"\n  resolution_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"~202 words but still 8-9 numbers.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Still 6+ numbers.\"}\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF; must commit to empirical study positioning\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must position as empirical contribution.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 still reads as method. Reposition around controlled testbed + identifiability.\"}\n    - {round: 8, reviewers: \"R2\", note: \"R2 notes novelty primarily comes from experimental paradigm not methodology (IRT+DIF has precedent). R1 partially disagrees—argues continuous covariate in explanatory IRT is original.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al. as concurrent work\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Explicitly state empirical investigation positioning\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reposition Han et al. differentiation; elevate J≥50 identifiability\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Paper committed to empirical investigation. Title signals empirical finding. 3 empirical contributions.\"\n  resolution_round: 7\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. differentiation needs rework\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. Han et al. comparison needs expansion.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Han et al. differentiation self-undermining. Add DIF classics.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2-N2 re-raises Han et al. differentiation as critical: only 2 sentences, no empirical comparison, unclear whether continuous vs binary exposure actually improves results. R1 agrees need more detail but rebuts requiring baseline implementation.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite Han et al., Schaeffer et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM, Magar & Schwartz + expand Han et al.\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Rework Han et al. differentiation; add DIF classics\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Add ~0.5 page detailed methodological comparison with Han et al. (assumptions, inputs, outputs, scope)\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Page limit — needs compile verification\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Main content ~8.5 pages. Desk-reject risk.\"}\n    - {round: 6, reviewers: \"R2\", note: \"Cannot confirm page count without compilation.\"}\n    - {round: 7, reviewers: \"\", note: \"Compiled and verified: 17 pages total (8 pages main text + references + appendix). EMNLP 2026 compliant.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised. Section 6 extends to p.9 ~40-55%. Both reviewers and visual check agent confirm main text exceeds 8 pages by ~0.4-0.5 page. Desk-reject risk.\"}\n  action_items:\n    - {round: 5, action: \"Move ARC IRT to Appendix; compress; move domain γ table to Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Compile and verify ≤8 pages main content\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Compress Section 6 Discussion—move overlapping content to Appendix. Section 6 must end within page 8.\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"k reserved for benchmark, d for domain. Not re-raised in R8.\"\n  resolution_round: 7\n  mentions:\n    - {round: 5, reviewers: \"R2\", note: \"k = benchmark in §3.1 but k = stratum in Eq.2.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Use different symbol for strata.\"}\n  action_items:\n    - {round: 5, action: \"Add clarifying note when k meaning changes\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Replace k with different symbol for strata index\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R6-W1\"\n  summary: \"SFT data composition confound — injection replaces or augments general SFT data unclear\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper explicitly states AUGMENT mode. Volume confound discussed with 3 counter-arguments. Not re-raised in R8.\"\n  resolution_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"§4.1 does not specify whether benchmark items replace or augment general SFT corpus.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。§4.1 and Limitations now clearly state AUGMENT mode.\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol: replacement vs augmentation\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R6-W2\"\n  summary: \"S4 (Self-Critique) signal computation details insufficient for reproduction\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R2\", note: \"Prompt design, evaluation distribution construction, and scoring mechanism not described.\"}\n    - {round: 8, reviewers: \"\", note: \"Appendix E (S4 Self-Critique Signal Details) now provides prompt, logit extraction, and scoring formula.\"}\n  action_items:\n    - {round: 6, action: \"Add S4 computation details in appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix E added with S4 details.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported — convergence verification missing\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R1\", note: \"Training convergence is prerequisite for controlled injection validity.\"}\n    - {round: 8, reviewers: \"\", note: \"Appendix F (Training Convergence) now reports final training loss by dosage. Minimal but present.\"}\n  action_items:\n    - {round: 6, action: \"Report SFT training curves or convergence verification in Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix F added with convergence info.\"\n  resolution_round: 8\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"Cross-family GSM8K PPP=0.83 but within-family GSM8K PPP not reported.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。Still not reported in current version.\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 8 (Fresh Review) New Issues ===\n\n- id: \"R8-N1\"\n  summary: \"Cross-seed stability claims overstated — n=3 seeds insufficient for taxonomy validation\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Both reviewers independently flag this as critical. n=3 seeds yields wide CIs; strict sign consistency only 2/5 families. Taxonomy-level aggregation rule relaxes criteria to show 4/5 consistency, but this relaxation itself undermines confidence. R1: 'any variance estimate at n=3 has extremely wide CIs'. R2: 'most families' taxonomy labels are seed-sensitive'.\"}\n  action_items:\n    - {round: 8, action: \"Increase seeds to n≥5 for ≤3B models (computationally feasible); or weaken claims to 'preliminary taxonomy under limited replication'\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Report bootstrap CI covering seed variability explicitly\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N2\"\n  summary: \"DiD null result lacks power analysis — 'causal evidence for global modulation' claim unsupported\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Both reviewers independently flag. DiD values range −0.8 to +0.6pp; power to detect ~1pp item-specific effect at n=3 unknown. Abstract/Intro claim 'causal evidence' but absence of significance ≠ evidence of absence. Figure 2 symmetry claim is visual, not formally tested.\"}\n  action_items:\n    - {round: 8, action: \"Run post-hoc power analysis reporting minimum detectable effect size (MDES)\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Weaken 'causal evidence for global modulation' to 'no detectable item-specific effect at current power level'\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N3\"\n  summary: \"N=4 model families supporting 4-class taxonomy — generalization evidence insufficient\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2 raises as N1 critical. R1 agrees with nuance (notes 5 models, Benefit shared by 2 families). Core concern: 4 patterns observed on 4 families is post-hoc description, not predictive taxonomy. No out-of-sample validation. Algorithm 1 pattern enumeration derived from same 4 families—cannot exclude 5th pattern.\"}\n  action_items:\n    - {round: 8, action: \"Option A: Add 1-2 more model families (LLaMA-3/Mistral) at 1-2 dosage levels for quick validation\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Option B: Replace 'taxonomy' with 'observed response profiles' throughout; add Discussion paragraph on model attributes (training data, architecture) → pattern hypotheses\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N4\"\n  summary: \"Han et al. (2026) differentiation insufficient — only 2 sentences, no empirical comparison\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2 raises as N2 critical. Han et al. (EACL 2026 Findings) is most direct prior work applying DIF to LLM contamination. Current differentiation: 2 sentences in Related Work. Missing: (1) continuous vs binary exposure effect comparison; (2) robustness under noisy signals; (3) when group-based DIF is preferable. R1 agrees differentiation needed but rebuts requiring baseline implementation (different output types).\"}\n  action_items:\n    - {round: 8, action: \"Add ~0.5 page methodological comparison with Han et al. covering assumptions, input requirements, output granularity, and applicability scope\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W1\"\n  summary: \"Bayesian and frequentist terminology mixed throughout paper\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R1 raises as W4. R2 agrees. Paper uses Bayesian MCMC (Stan/NUTS) for IRT but 'significant', 'p-value', 'confidence interval' appear in frequentist sense. DiD analysis (Table 4) appears frequentist (p > .05) without explicit framework label. PPP vs frequentist p not distinguished.\"}\n  action_items:\n    - {round: 8, action: \"Unify terminology: use 'credible interval' for Bayesian CIs; explicitly label DiD as frequentist; distinguish PPP from frequentist p-value\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W2\"\n  summary: \"IRT identifiability simulation uses uniform exposure — mismatch with empirical right-skewed RRF distribution\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R1 raises as part of N2 critical. R2 rebuts the 'critical' severity (J=13-16 coverage ≥0.93 under Linear DGP) but agrees skewed exposure gap is real Should-Fix. Empirical RRF: mean=0.041, median=0.016, highly right-skewed. Simulation uses uniform. Few high-exposure items may create leverage effect on γ.\"}\n  action_items:\n    - {round: 8, action: \"Re-run identifiability simulation with right-skewed exposure matching empirical RRF distribution\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-W3\"\n  summary: \"Algorithm 1 threshold sensitivity — only pass/fail grid reported, no continuous sensitivity curve\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R2,R1\", note: \"R2 raises as W4. R1 partial agree (severity lower than R2's assessment). Appendix K Table 9: 30/30 pass is too coarse. No sensitivity heatmap showing how classification changes continuously with threshold.\"}\n  action_items:\n    - {round: 8, action: \"Add threshold sensitivity heatmap in Appendix (τ × σ classification matrix per family)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M1\"\n  summary: \"Missing references — Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Both reviewers flag Yang et al. (2023). R2 additionally flags Golchin & Surdeanu (ICLR 2024, contamination detection via guided instruction) and Sainz et al. (EMNLP 2023 Findings, per-benchmark contamination measurement). R1 also suggests Recht et al. (2019) on benchmark overfitting.\"}\n  action_items:\n    - {round: 8, action: \"Add Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023) to Related Work\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M2\"\n  summary: \"Minor writing issues — 'pp' undefined, Gemma-2 exclusion abrupt, Figure 1 caption incomplete, Eq.2 computation unclear\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2-M1: 'pp' not defined at first use. R2-M2: Gemma-2 GSM8K exclusion appears suddenly in §5.2. R1-M4: Figure 1 caption doesn't note seed=42. R1-M5: Eq.2 decontamination computation path unclear (per-MCMC-sample zero-out vs analytic). R1/R2-M6/M4: holland_1993_dif and lord_1980_irt year discrepancies.\"}\n  action_items:\n    - {round: 8, action: \"Fix minor writing issues: define 'pp', add Gemma-2 exclusion note in §4, add seed label to Figure 1 caption, clarify Eq.2 computation, verify bib years\", assigned_to: \"paper_agent\", status: \"open\"}"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-21T07:43:34.786957+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml\", \"bytes\": 34328}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-21T07:45:55.033376+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿模式**: 重新审稿 (fresh)\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计+统计声明; R2: 新颖性+Related Work+写作+格式)\n**审稿轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识后收敛\n\n---\n\n## Summary\n\n本文通过控制 SFT 注入（LoRA, 5 个剂量水平）对来自 4 个独立模型家族的 5 个模型（7B–14.7B）进行 benchmark 污染实验，发现污染产生了四种质性不同的剂量-响应模式（Immune / Collapse / V-Recovery / Benefit），而非通常假设的统一膨胀效应。论文使用 ContamCal——一个结合多信号 RRF 融合与污染增强 IRT (2PL+γ) 的两阶段管线——对结果进行统计表征。DiD 分析显示无 item-specific 记忆化证据，跨 benchmark 传递揭示了方向反转现象。\n\n---\n\n## Strengths\n\n1. **概念新颖性强**：将 benchmark 污染建模为连续剂量-效应关系并建立 dose-response 分类是真正的新视角。\"contamination ≠ inflation\" 直接挑战社区普遍假设，对 benchmark 设计者和模型评估实践者有实际指导意义。[R1, R2 共识]\n\n2. **实验设计是该领域的方法论升级**：控制 SFT 注入提供已知 ground truth 的因果推断基础，跨 4 家族 × 3 benchmark × 5 剂量 × 3 seeds 的矩阵设计在 contamination 研究中罕见。[R1, R2 共识]\n\n3. **DiD + 跨 benchmark 证据链构成相互佐证**：Contribution 2（global modulation）是论文最强贡献——DiD 在所有家族的 treated/untreated items 上均为非显著，跨 benchmark 方向反转（Qwen-7B: MMLU −1.8pp vs GSM8K +10.1pp）进一步证明效应是全局性的。[R1, R2 共识]\n\n4. **Appendix 详尽**：18 个 appendix sections 覆盖 identifiability simulation、DGP robustness、prior sensitivity、convergence diagnostics、classification sensitivity 等，表明作者对方法论细节的严肃态度。[R1, R2 共识]\n\n5. **IRT 整合技术上合理**：将 contamination detection signals 作为连续协变量融入 explanatory IRT（2PL+γ）是自然的建模选择，per-benchmark fitting + domain-level γ_d 提供了实用的诊断粒度。[R1, R2 共识]\n\n6. **多 baseline 比较**：7 个 baseline 方法（raw accuracy、remove-and-rescore、vanilla IRT、linear regression、Emperor、DCR、ContamCal variants）提供了较全面的参照。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, R1-N1 + R2-W3, 共识] **Cross-seed stability 声明与 n=3 样本量不匹配**\n\nn=3 seeds 下方差估计的置信区间极宽。Table 3 显示 strict sign consistency 仅 2/5 families 通过；论文通过放宽为 \"taxonomy-level consistency\"（CI-based aggregation rule）达到 4/5，但这一放宽本身降低了分类精度。核心贡献（dose-response taxonomy）的统计基础不充分。\n\n→ 建议：(a) 对 ≤3B 模型增加 seeds 至 n≥5（LoRA SFT 成本可控）；(b) 报告 cross-seed bootstrap CI；(c) 至少将 claim 弱化为 \"preliminary taxonomy under limited replication\"。\n\n**W2** [critical, R1-N3 + R2-W2, 共识] **DiD null result 缺乏 power analysis，\"causal evidence\" 声明不成立**\n\nDiD 值范围 −0.8 到 +0.6pp，在当前样本量下检测 ~1pp item-specific 效应的 statistical power 未知。Abstract/Intro 将 \"All DiD non-significant\" 升级为 \"causal evidence that contamination operates through global capability modulation rather than item-specific memorization\"，这是 absence-of-evidence ≠ evidence-of-absence 错误。Figure 2 的 symmetry 声明依赖视觉判断而非正式检验。\n\n→ 建议：(a) 做 post-hoc power analysis 报告 MDES；(b) 弱化为 \"we find no evidence of item-specific memorization at the current power level\"。\n\n**W3** [critical, R2-N1, R1 同意] **N=4 模型族支撑 4 类分类学，泛化性证据不足**\n\n4 个家族恰好观测到 4 种模式，Table 1 中每种模式恰好对应一个家族（Phi-4→Immune, Qwen-14B→Collapse, Qwen-7B→V-Recovery, Gemma-2→Benefit），存在 overfitting-to-sample 风险。Algorithm 1 的 pattern 枚举从这 4 个家族归纳，无法排除第 5 种 pattern。R1 补充指出 Benefit 实际出现在 2 个家族（Gemma-2 + OLMo-2），减轻了 one-to-one 担忧，但核心论点成立。\n\n→ 建议：(a) 增加 1-2 个模型族快速验证（LLaMA-3/Mistral，哪怕仅 1-2 个剂量水平）；(b) 若资源受限，将 \"taxonomy\" 改为 \"observed response profiles\"，并在 Discussion 中分析模型属性与 pattern 的潜在关联。\n\n**W4** [critical, R2-N2, R1 带条件同意] **与 Han et al. (2026) 的差异化论证不充分**\n\nHan et al. (2026, EACL Findings) 是最直接的在先工作（DIF 应用于 LLM 污染），当前仅 2 句话区分。未讨论：(1) continuous vs binary exposure 的实际效果差异；(2) 在 Stage 1 信号有噪声时 continuous 是否优于 binary；(3) 何时 group-based DIF 更稳健。R1 同意需要加强论证但反对将 Han et al. 实现为 baseline（两种方法输出类型不同，不直接可比）。\n\n→ 建议：在 Method 或 Related Work 中增加 ~0.5 页详细方法论对比（假设差异、输入要求、输出粒度、适用范围）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W5** [warning, R2-W1 + R1 同意, 视觉审查确认] **正文疑似超过 8 页限制**\n\nSection 6 (Discussion and Conclusion) 从 p.8 底部延伸至 p.9，正文估计约 8.4-8.5 页。EMNLP 2026 正文限 8 页（Limitations/Ethics 不计入）。**存在 desk-reject 风险。** 视觉审查 Agent 独立确认：\"Section 6 正文内容已超出第 8 页\"。Section 6 的多个小标题段落内容与 §5 findings 重叠。\n\n→ 建议：大幅压缩 Section 6，移重叠内容至 Appendix，确保 Section 6 结束于 p.8 内。\n\n**W6** [warning, R1-W4 + R2 同意] **Bayesian 和 frequentist 术语混用**\n\n论文使用 Bayesian MCMC (Stan/NUTS) 做 IRT 推断，但多处使用 \"significant\" \"p-value\" 等 frequentist 术语。DiD 分析 (Table 4) 的 \"p > .05; ns\" 似乎是 frequentist t-test，但与 Bayesian IRT 框架未明确区分。PPP 与 frequentist p-value 混淆。\n\n→ 建议：统一为 \"credible interval\"（Bayesian）vs \"confidence interval\"（frequentist），明确标注每个检验的框架。\n\n**W7** [warning, R1-W1 + R2 同意] **RRF fusion 缺乏 calibration 验证**\n\n未报告 (1) RRF score 与真实 contamination 程度的校准关系；(2) S1-S4 间的 rank correlation；(3) leave-one-signal-out 消融。§5.4 的 random-subset MAE 比较（0.039±0.008 vs 0.006）间接验证了 RRF item selection 的价值，但非 exposure score 本身的校准性。\n\n→ 建议：报告 signal rank correlation 和 leave-one-signal-out 消融。\n\n**W8** [warning, R1-N2 子论点, R2 同意降级] **Identifiability simulation 用 uniform exposure，与实际 skewed 分布不匹配**\n\nAppendix D 的 identifiability simulation 使用 uniform exposure 分布，但实际 RRF exposure 高度右偏（mean=0.041, median=0.016）。少数高 exposure items 可能产生 leverage effect 驱动 γ 估计。R2 指出 J=13-16 在 Linear DGP 下 coverage ≥0.93（不在边界上），但 skewed exposure gap 是真实缺陷。\n\n→ 建议：在 simulation 中增加 skewed exposure 条件验证。\n\n**W9** [warning, R2-W4, R1 部分同意] **Algorithm 1 阈值 sensitivity 报告过粗**\n\nAppendix K Table 9 仅报告 30/30 pass/fail，缺乏 sensitivity curve 展示分类如何随阈值连续变化。R1 认为严重程度低于 R2 评估（direction 是 primary criterion，阈值仅影响边缘 case），但添加 sensitivity heatmap 是低成本改善。\n\n→ 建议：在 Appendix 增加 τ × σ 分类一致性 heatmap。\n\n### Minor（不影响接收）\n\n- **M1**: \"pp\" (percentage points) 在 Abstract 首次使用时未定义 [R2]\n- **M2**: Gemma-2 GSM8K 排除在 §5.2 出现突然，应在 §4 预先说明 [R2]\n- **M3**: Algorithm 1 正文未给 default τ 值，需翻 Appendix [R1]\n- **M4**: Figure 1 caption 未标注 seed=42 [R1]\n- **M5**: Eq. (2) decontamination 的具体计算路径不明确（per-MCMC-sample zero-out vs analytic） [R1]\n- **M6**: 引用年份：holland_1993_dif 和 lord_1980_irt 可能是再版年份 [R1, R2]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **完全一致** [AGREE]：\n- n=3 seeds 不足以支撑 cross-seed stability claims\n- DiD null result 缺乏 power analysis，因果声明过强\n- N=4 模型族的 taxonomy 泛化性不足\n- Han et al. (2026) 差异化论证需加强\n- 正文可能超 8 页限制（desk-reject 风险）\n- Bayesian/frequentist 术语需统一\n- RRF fusion 需 calibration 验证\n- SFT ecological validity 是已知局限（但不构成拒稿理由）\n- 遗漏引用：Yang et al. (2023), Golchin & Surdeanu (2024), Sainz et al. (2023)\n\n## Reviewer Divergence\n\n**IRT identifiability 严重程度** — R1 列为 critical（J=13-16 在边界上），R2 反驳（Linear DGP coverage ≥0.93，coverage 下降仅在 J=500 Threshold DGP 下）。R2 的反驳有论文数据支撑（Appendix P），但 R1 关于 skewed exposure 的子论点被 R2 认可为 Should-Fix。**最终定级：Should-Fix**（W8）。\n\n**ContamCal baseline 优势** — R1 指出 GSM8K 上 B4 优于 ContamCal；R2 反驳 ContamCal 核心价值在 uncertainty quantification + domain diagnosis 而非 MAE，且 MMLU/ARC 上 ContamCal 最优。**不列为独立 weakness**（ContamCal 的定位已从 calibration 工具转为诊断框架）。\n\n**Bakhtin et al. (2024) 引用** — R1 建议引用，R2 反驳（pretraining deduplication 与本文主题关联较远）。**不列为遗漏**。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Appendix P 中 CI coverage 随 J 增大下降——能否详细解释 bias 来源？这是否意味着 2PL+γ 在大样本下是 misspecified 的？\n2. RRF exposure 的 right-skewed 分布是否引入 leverage effect？是否做了 influential observation 诊断？\n3. 低剂量（d005, d025）下 cross-benchmark transfer pattern 是否与 d100 一致？\n4. 0.5B 的 A-option position bias（46%→98%）是否暗示 small models 有完全不同的 dose-response 机制？是否考虑过 position bias correction 后的补充分析？\n\n---\n\n## Missing References\n\n1. **Golchin & Surdeanu (2024)** \"Time Travel in LLMs: Tracing Data Contamination in Large Language Models\" (ICLR 2024) — instance-level 污染检测代表性工作 [R2]\n2. **Sainz et al. (2023)** \"NLP Evaluation in Trouble: On the Need to Measure LLM Data Contamination for each Benchmark\" (EMNLP 2023 Findings) — per-benchmark 污染度量 [R2]\n3. **Yang et al. (2023)** \"Rethinking Benchmark and Contamination for Language Models with Rephrased Samples\" — rephrasing 绕过检测，与 S3 (ConStat) 设计动机直接相关 [R1, R2]\n4. **Recht et al. (2019)** \"Do ImageNet Classifiers Generalize to ImageNet?\" — benchmark overfitting 经典工作 [R1，R2 同意但优先级较低]\n\n---\n\n## External Review\n\n**外部审稿**: 未请求（项目未配置 paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（5 warnings, 0 critical, 8 info）：\n\n**Warnings:**\n1. **Pages 1-3 纯文本无 display item**：连续 3 页无 figure/table，直到 p.4 才出现 Algorithm 1，p.6 才出现首个 figure。建议将核心结果图或方法概览图提前至 p.1-2。\n2. **Figure 1 位置偏后且尺寸偏小**：全文首个 figure 出现在 p.6，单栏宽度，建议改用 `figure*` 双栏全宽并提前放置。\n3. **正文超 8 页**：Section 6 延伸至 p.9 约 40%，与 Reviewer 共识一致。\n4. **Appendix 末页大面积空白**：Tables 12-13 下方约 60% 空白，可合并或重组。\n5. **Pages 4-5 视觉断档**：Experimental Setup + Results 开头连续 2 页无 figure/table。\n\n**Info (正面):**\n- Title/Author/Abstract 排版整洁，ACL 匿名格式正确\n- 公式渲染正确，无 LaTeX 残留错误\n- Tables 使用 booktabs 风格，专业规范\n- Figure 2 散点图清晰可读\n- 参考文献格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**\n\n**置信度: 4/5**（两位 Reviewer 均有强领域背景，交叉回应后关键问题达成高度共识）\n\n**理由**:\n\n论文的核心贡献——用控制实验揭示 \"contamination ≠ inflation\"——有真实价值，实验设计是该领域的方法论升级。然而，四个 critical 问题共同限制了论文达到主会议水平的证据强度：\n\n1. **统计功效不足**：n=3 seeds 和 J=13-16 的组合意味着 taxonomy stability claims 和 DiD causal claims 都在统计功效边界上运行。两个核心贡献（taxonomy + global modulation）的 claim 强度均超出了证据支撑范围。\n\n2. **泛化性未验证**：N=4 家族上的 4 类分类学更接近 post-hoc 描述而非可泛化的分类体系。没有 out-of-sample 验证，taxonomy 的预测力未知。\n\n3. **差异化不充分**：与最直接的在先工作 Han et al. (2026) 仅有 2 句话区分，审稿人无法充分评估增量贡献。\n\n4. **格式风险**：正文疑似超 8 页，存在 desk-reject 风险。\n\n如果作者能：(a) 增加 seeds 或弱化 claims，(b) 补充 power analysis，(c) 增加 Han et al. 对比，(d) 修复页数问题——论文有潜力提升至 3.5 (Borderline Conference)。当前状态适合 Findings 接收。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 声称 \"causal evidence that SFT contamination operates through global capability modulation\" 过强，需降级为 \"no detectable evidence of item-specific memorization\"\n- \"qualitatively different dose-response patterns\" 的措辞 OK，但应注明样本量限制\n\n### Section 2 (Related Work)\n- Han et al. 段落需扩展至 ~0.5 页详细方法论对比\n- 缺 Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\n- DIF 经典文献（Camilli, Swaminathan, Holland）已引用 ✓\n\n### Section 3 (Method)\n- 2PL+γ 模型数学正确，假设合理 ✓\n- Eq. (2) 应补充计算路径说明\n- RRF fusion 需 signal rank correlation + leave-one-signal-out 消融\n- Algorithm 1 需在正文给出 default τ 值\n\n### Section 4 (Experimental Setup)\n- 控制注入方案合理 ✓；AUGMENT mode 需在正文早期说明\n- Gemma-2 GSM8K 排除应提前声明\n- 0.5B 排除理由充分 ✓\n\n### Section 5 (Results)\n- Table 1 (dose-response patterns): 应注明 \"N=4 families, preliminary\" 性质\n- Table 2 (cross-benchmark): 仅报告 d100，低剂量结果缺失\n- Table 3 (cross-seed): n=3 下 CI 宽度需显著声明\n- Table 4 (DiD): 需 power analysis；\"causal evidence\" 需降级\n- §5.5 (Calibration): ContamCal 核心价值在诊断而非 MAE——当前叙述可更突出此点\n- §5.7 (Domain): Social Sciences γ_d 通过 Bonferroni ✓；exploratory caveat ✓\n\n### Section 6 (Discussion and Conclusion)\n- 必须压缩至 p.8 内——多段内容与 §5 重叠\n- \"Pretraining contamination may produce qualitatively different effects\" 的 caveat 恰当 ✓\n\n### Limitations\n- 覆盖 10 个点，内容充分 ✓（R1 认为不应压缩）\n- 不计入页数，不影响格式合规\n\n### Ethics Statement\n- 恰当，覆盖了 dual-use risk ✓\n\n### Appendix\n- 详尽且有价值 ✓\n- DGP robustness (Appendix P) 需补充 skewed exposure 条件\n- S4 details (Appendix E) 已补充 ✓\n- Training convergence (Appendix F) 已补充但较简略",
  "project": "contamcal-irt-calibration",
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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿模式**: 重新审稿 (fresh)\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计+统计声明; R2: 新颖性+Related Work+写作+格式)\n**审稿轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识后收敛\n\n---\n\n## Summary\n\n本文通过控制 SFT 注入（LoRA, 5 个剂量水平）对来自 4 个独立模型家族的 5 个模型（7B–14.7B）进行 benchmark 污染实验，发现污染产生了四种质性不同的剂量-响应模式（Immune / Collapse / V-Recovery / Benefit），而非通常假设的统一膨胀效应。论文使用 ContamCal——一个结合多信号 RRF 融合与污染增强 IRT (2PL+γ) 的两阶段管线——对结果进行统计表征。DiD 分析显示无 item-specific 记忆化证据，跨 benchmark 传递揭示了方向反转现象。\n\n---\n\n## Strengths\n\n1. **概念新颖性强**：将 benchmark 污染建模为连续剂量-效应关系并建立 dose-response 分类是真正的新视角。\"contamination ≠ inflation\" 直接挑战社区普遍假设，对 benchmark 设计者和模型评估实践者有实际指导意义。[R1, R2 共识]\n\n2. **实验设计是该领域的方法论升级**：控制 SFT 注入提供已知 ground truth 的因果推断基础，跨 4 家族 × 3 benchmark × 5 剂量 × 3 seeds 的矩阵设计在 contamination 研究中罕见。[R1, R2 共识]\n\n3. **DiD + 跨 benchmark 证据链构成相互佐证**：Contribution 2（global modulation）是论文最强贡献——DiD 在所有家族的 treated/untreated items 上均为非显著，跨 benchmark 方向反转（Qwen-7B: MMLU −1.8pp vs GSM8K +10.1pp）进一步证明效应是全局性的。[R1, R2 共识]\n\n4. **Appendix 详尽**：18 个 appendix sections 覆盖 identifiability simulation、DGP robustness、prior sensitivity、convergence diagnostics、classification sensitivity 等，表明作者对方法论细节的严肃态度。[R1, R2 共识]\n\n5. **IRT 整合技术上合理**：将 contamination detection signals 作为连续协变量融入 explanatory IRT（2PL+γ）是自然的建模选择，per-benchmark fitting + domain-level γ_d 提供了实用的诊断粒度。[R1, R2 共识]\n\n6. **多 baseline 比较**：7 个 baseline 方法（raw accuracy、remove-and-rescore、vanilla IRT、linear regression、Emperor、DCR、ContamCal variants）提供了较全面的参照。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, R1-N1 + R2-W3, 共识] **Cross-seed stability 声明与 n=3 样本量不匹配**\n\nn=3 seeds 下方差估计的置信区间极宽。Table 3 显示 strict sign consistency 仅 2/5 families 通过；论文通过放宽为 \"taxonomy-level consistency\"（CI-based aggregation rule）达到 4/5，但这一放宽本身降低了分类精度。核心贡献（dose-response taxonomy）的统计基础不充分。\n\n→ 建议：(a) 对 ≤3B 模型增加 seeds 至 n≥5（LoRA SFT 成本可控）；(b) 报告 cross-seed bootstrap CI；(c) 至少将 claim 弱化为 \"preliminary taxonomy under limited replication\"。\n\n**W2** [critical, R1-N3 + R2-W2, 共识] **DiD null result 缺乏 power analysis，\"causal evidence\" 声明不成立**\n\nDiD 值范围 −0.8 到 +0.6pp，在当前样本量下检测 ~1pp item-specific 效应的 statistical power 未知。Abstract/Intro 将 \"All DiD non-significant\" 升级为 \"causal evidence that contamination operates through global capability modulation rather than item-specific memorization\"，这是 absence-of-evidence ≠ evidence-of-absence 错误。Figure 2 的 symmetry 声明依赖视觉判断而非正式检验。\n\n→ 建议：(a) 做 post-hoc power analysis 报告 MDES；(b) 弱化为 \"we find no evidence of item-specific memorization at the current power level\"。\n\n**W3** [critical, R2-N1, R1 同意] **N=4 模型族支撑 4 类分类学，泛化性证据不足**\n\n4 个家族恰好观测到 4 种模式，Table 1 中每种模式恰好对应一个家族（Phi-4→Immune, Qwen-14B→Collapse, Qwen-7B→V-Recovery, Gemma-2→Benefit），存在 overfitting-to-sample 风险。Algorithm 1 的 pattern 枚举从这 4 个家族归纳，无法排除第 5 种 pattern。R1 补充指出 Benefit 实际出现在 2 个家族（Gemma-2 + OLMo-2），减轻了 one-to-one 担忧，但核心论点成立。\n\n→ 建议：(a) 增加 1-2 个模型族快速验证（LLaMA-3/Mistral，哪怕仅 1-2 个剂量水平）；(b) 若资源受限，将 \"taxonomy\" 改为 \"observed response profiles\"，并在 Discussion 中分析模型属性与 pattern 的潜在关联。\n\n**W4** [critical, R2-N2, R1 带条件同意] **与 Han et al. (2026) 的差异化论证不充分**\n\nHan et al. (2026, EACL Findings) 是最直接的在先工作（DIF 应用于 LLM 污染），当前仅 2 句话区分。未讨论：(1) continuous vs binary exposure 的实际效果差异；(2) 在 Stage 1 信号有噪声时 continuous 是否优于 binary；(3) 何时 group-based DIF 更稳健。R1 同意需要加强论证但反对将 Han et al. 实现为 baseline（两种方法输出类型不同，不直接可比）。\n\n→ 建议：在 Method 或 Related Work 中增加 ~0.5 页详细方法论对比（假设差异、输入要求、输出粒度、适用范围）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W5** [warning, R2-W1 + R1 同意, 视觉审查确认] **正文疑似超过 8 页限制**\n\nSection 6 (Discussion and Conclusion) 从 p.8 底部延伸至 p.9，正文估计约 8.4-8.5 页。EMNLP 2026 正文限 8 页（Limitations/Ethics 不计入）。**存在 desk-reject 风险。** 视觉审查 Agent 独立确认：\"Section 6 正文内容已超出第 8 页\"。Section 6 的多个小标题段落内容与 §5 findings 重叠。\n\n→ 建议：大幅压缩 Section 6，移重叠内容至 Appendix，确保 Section 6 结束于 p.8 内。\n\n**W6** [warning, R1-W4 + R2 同意] **Bayesian 和 frequentist 术语混用**\n\n论文使用 Bayesian MCMC (Stan/NUTS) 做 IRT 推断，但多处使用 \"significant\" \"p-value\" 等 frequentist 术语。DiD 分析 (Table 4) 的 \"p > .05; ns\" 似乎是 frequentist t-test，但与 Bayesian IRT 框架未明确区分。PPP 与 frequentist p-value 混淆。\n\n→ 建议：统一为 \"credible interval\"（Bayesian）vs \"confidence interval\"（frequentist），明确标注每个检验的框架。\n\n**W7** [warning, R1-W1 + R2 同意] **RRF fusion 缺乏 calibration 验证**\n\n未报告 (1) RRF score 与真实 contamination 程度的校准关系；(2) S1-S4 间的 rank correlation；(3) leave-one-signal-out 消融。§5.4 的 random-subset MAE 比较（0.039±0.008 vs 0.006）间接验证了 RRF item selection 的价值，但非 exposure score 本身的校准性。\n\n→ 建议：报告 signal rank correlation 和 leave-one-signal-out 消融。\n\n**W8** [warning, R1-N2 子论点, R2 同意降级] **Identifiability simulation 用 uniform exposure，与实际 skewed 分布不匹配**\n\nAppendix D 的 identifiability simulation 使用 uniform exposure 分布，但实际 RRF exposure 高度右偏（mean=0.041, median=0.016）。少数高 exposure items 可能产生 leverage effect 驱动 γ 估计。R2 指出 J=13-16 在 Linear DGP 下 coverage ≥0.93（不在边界上），但 skewed exposure gap 是真实缺陷。\n\n→ 建议：在 simulation 中增加 skewed exposure 条件验证。\n\n**W9** [warning, R2-W4, R1 部分同意] **Algorithm 1 阈值 sensitivity 报告过粗**\n\nAppendix K Table 9 仅报告 30/30 pass/fail，缺乏 sensitivity curve 展示分类如何随阈值连续变化。R1 认为严重程度低于 R2 评估（direction 是 primary criterion，阈值仅影响边缘 case），但添加 sensitivity heatmap 是低成本改善。\n\n→ 建议：在 Appendix 增加 τ × σ 分类一致性 heatmap。\n\n### Minor（不影响接收）\n\n- **M1**: \"pp\" (percentage points) 在 Abstract 首次使用时未定义 [R2]\n- **M2**: Gemma-2 GSM8K 排除在 §5.2 出现突然，应在 §4 预先说明 [R2]\n- **M3**: Algorithm 1 正文未给 default τ 值，需翻 Appendix [R1]\n- **M4**: Figure 1 caption 未标注 seed=42 [R1]\n- **M5**: Eq. (2) decontamination 的具体计算路径不明确（per-MCMC-sample zero-out vs analytic） [R1]\n- **M6**: 引用年份：holland_1993_dif 和 lord_1980_irt 可能是再版年份 [R1, R2]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **完全一致** [AGREE]：\n- n=3 seeds 不足以支撑 cross-seed stability claims\n- DiD null result 缺乏 power analysis，因果声明过强\n- N=4 模型族的 taxonomy 泛化性不足\n- Han et al. (2026) 差异化论证需加强\n- 正文可能超 8 页限制（desk-reject 风险）\n- Bayesian/frequentist 术语需统一\n- RRF fusion 需 calibration 验证\n- SFT ecological validity 是已知局限（但不构成拒稿理由）\n- 遗漏引用：Yang et al. (2023), Golchin & Surdeanu (2024), Sainz et al. (2023)\n\n## Reviewer Divergence\n\n**IRT identifiability 严重程度** — R1 列为 critical（J=13-16 在边界上），R2 反驳（Linear DGP coverage ≥0.93，coverage 下降仅在 J=500 Threshold DGP 下）。R2 的反驳有论文数据支撑（Appendix P），但 R1 关于 skewed exposure 的子论点被 R2 认可为 Should-Fix。**最终定级：Should-Fix**（W8）。\n\n**ContamCal baseline 优势** — R1 指出 GSM8K 上 B4 优于 ContamCal；R2 反驳 ContamCal 核心价值在 uncertainty quantification + domain diagnosis 而非 MAE，且 MMLU/ARC 上 ContamCal 最优。**不列为独立 weakness**（ContamCal 的定位已从 calibration 工具转为诊断框架）。\n\n**Bakhtin et al. (2024) 引用** — R1 建议引用，R2 反驳（pretraining deduplication 与本文主题关联较远）。**不列为遗漏**。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Appendix P 中 CI coverage 随 J 增大下降——能否详细解释 bias 来源？这是否意味着 2PL+γ 在大样本下是 misspecified 的？\n2. RRF exposure 的 right-skewed 分布是否引入 leverage effect？是否做了 influential observation 诊断？\n3. 低剂量（d005, d025）下 cross-benchmark transfer pattern 是否与 d100 一致？\n4. 0.5B 的 A-option position bias（46%→98%）是否暗示 small models 有完全不同的 dose-response 机制？是否考虑过 position bias correction 后的补充分析？\n\n---\n\n## Missing References\n\n1. **Golchin & Surdeanu (2024)** \"Time Travel in LLMs: Tracing Data Contamination in Large Language Models\" (ICLR 2024) — instance-level 污染检测代表性工作 [R2]\n2. **Sainz et al. (2023)** \"NLP Evaluation in Trouble: On the Need to Measure LLM Data Contamination for each Benchmark\" (EMNLP 2023 Findings) — per-benchmark 污染度量 [R2]\n3. **Yang et al. (2023)** \"Rethinking Benchmark and Contamination for Language Models with Rephrased Samples\" — rephrasing 绕过检测，与 S3 (ConStat) 设计动机直接相关 [R1, R2]\n4. **Recht et al. (2019)** \"Do ImageNet Classifiers Generalize to ImageNet?\" — benchmark overfitting 经典工作 [R1，R2 同意但优先级较低]\n\n---\n\n## External Review\n\n**外部审稿**: 未请求（项目未配置 paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（5 warnings, 0 critical, 8 info）：\n\n**Warnings:**\n1. **Pages 1-3 纯文本无 display item**：连续 3 页无 figure/table，直到 p.4 才出现 Algorithm 1，p.6 才出现首个 figure。建议将核心结果图或方法概览图提前至 p.1-2。\n2. **Figure 1 位置偏后且尺寸偏小**：全文首个 figure 出现在 p.6，单栏宽度，建议改用 `figure*` 双栏全宽并提前放置。\n3. **正文超 8 页**：Section 6 延伸至 p.9 约 40%，与 Reviewer 共识一致。\n4. **Appendix 末页大面积空白**：Tables 12-13 下方约 60% 空白，可合并或重组。\n5. **Pages 4-5 视觉断档**：Experimental Setup + Results 开头连续 2 页无 figure/table。\n\n**Info (正面):**\n- Title/Author/Abstract 排版整洁，ACL 匿名格式正确\n- 公式渲染正确，无 LaTeX 残留错误\n- Tables 使用 booktabs 风格，专业规范\n- Figure 2 散点图清晰可读\n- 参考文献格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**\n\n**置信度: 4/5**（两位 Reviewer 均有强领域背景，交叉回应后关键问题达成高度共识）\n\n**理由**:\n\n论文的核心贡献——用控制实验揭示 \"contamination ≠ inflation\"——有真实价值，实验设计是该领域的方法论升级。然而，四个 critical 问题共同限制了论文达到主会议水平的证据强度：\n\n1. **统计功效不足**：n=3 seeds 和 J=13-16 的组合意味着 taxonomy stability claims 和 DiD causal claims 都在统计功效边界上运行。两个核心贡献（taxonomy + global modulation）的 claim 强度均超出了证据支撑范围。\n\n2. **泛化性未验证**：N=4 家族上的 4 类分类学更接近 post-hoc 描述而非可泛化的分类体系。没有 out-of-sample 验证，taxonomy 的预测力未知。\n\n3. **差异化不充分**：与最直接的在先工作 Han et al. (2026) 仅有 2 句话区分，审稿人无法充分评估增量贡献。\n\n4. **格式风险**：正文疑似超 8 页，存在 desk-reject 风险。\n\n如果作者能：(a) 增加 seeds 或弱化 claims，(b) 补充 power analysis，(c) 增加 Han et al. 对比，(d) 修复页数问题——论文有潜力提升至 3.5 (Borderline Conference)。当前状态适合 Findings 接收。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 声称 \"causal evidence that SFT contamination operates through global capability modulation\" 过强，需降级为 \"no detectable evidence of item-specific memorization\"\n- \"qualitatively different dose-response patterns\" 的措辞 OK，但应注明样本量限制\n\n### Section 2 (Related Work)\n- Han et al. 段落需扩展至 ~0.5 页详细方法论对比\n- 缺 Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\n- DIF 经典文献（Camilli, Swaminathan, Holland）已引用 ✓\n\n### Section 3 (Method)\n- 2PL+γ 模型数学正确，假设合理 ✓\n- Eq. (2) 应补充计算路径说明\n- RRF fusion 需 signal rank correlation + leave-one-signal-out 消融\n- Algorithm 1 需在正文给出 default τ 值\n\n### Section 4 (Experimental Setup)\n- 控制注入方案合理 ✓；AUGMENT mode 需在正文早期说明\n- Gemma-2 GSM8K 排除应提前声明\n- 0.5B 排除理由充分 ✓\n\n### Section 5 (Results)\n- Table 1 (dose-response patterns): 应注明 \"N=4 families, preliminary\" 性质\n- Table 2 (cross-benchmark): 仅报告 d100，低剂量结果缺失\n- Table 3 (cross-seed): n=3 下 CI 宽度需显著声明\n- Table 4 (DiD): 需 power analysis；\"causal evidence\" 需降级\n- §5.5 (Calibration): ContamCal 核心价值在诊断而非 MAE——当前叙述可更突出此点\n- §5.7 (Domain): Social Sciences γ_d 通过 Bonferroni ✓；exploratory caveat ✓\n\n### Section 6 (Discussion and Conclusion)\n- 必须压缩至 p.8 内——多段内容与 §5 重叠\n- \"Pretraining contamination may produce qualitatively different effects\" 的 caveat 恰当 ✓\n\n### Limitations\n- 覆盖 10 个点，内容充分 ✓（R1 认为不应压缩）\n- 不计入页数，不影响格式合规\n\n### Ethics Statement\n- 恰当，覆盖了 dual-use risk ✓\n\n### Appendix\n- 详尽且有价值 ✓\n- DGP robustness (Appendix P) 需补充 skewed exposure 条件\n- S4 details (Appendix E) 已补充 ✓\n- Training convergence (Appendix F) 已补充但较简略",
    "project": "contamcal-irt-calibration",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-21T07:45:59.457049+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4423
}
```

</details>

---


### Assistant

_source line 680 · 2026-05-21T07:46:06.192818+00:00_

审稿报告已投递至 Research Director。

---

**Round 8 审稿完成。**

**Overall: 3.0 (Findings)**

核心判断：
- **最强贡献**："contamination ≠ inflation" 的 DiD + 跨 benchmark 证据链，实验设计是该领域的方法论升级
- **四个 critical 问题**：(1) n=3 seeds 不足以支撑 taxonomy stability；(2) DiD "causal evidence" 声明缺 power analysis；(3) N=4 家族的 taxonomy 泛化性未验证；(4) Han et al. 差异化不充分
- **desk-reject 风险**：正文超 8 页约 0.4-0.5 页，需立即压缩 Section 6
- **提升路径**：修复 critical 问题后可达 3.5 (Borderline Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 68

## Round 68

2 recorded events


### User

_source line 681 · 2026-05-21T07:46:08.952969+00:00_

[Reviewer 2 审稿结果]:
核心共识：R1 和我在 n=3 seeds 不足、DID power 问题、术语混用上完全一致。主要分歧在 R1-N2（IRT identifiability）——我认为论文的 Appendix P 数据表明 J=13-16 并非处于边界，R1 引用的 coverage=0.70 仅出现在 J=500 的 Threshold DGP 极端条件下，不适用于当前分析。但 skewed exposure simulation 缺失是真实的 Should-Fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 682 · 2026-05-21T07:46:22.908538+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **评分**: 3.0 (Findings)
- **两位 Reviewer 初审均给 3.5 (Borderline Conference)**，经交叉分享后在关键问题上达成高度共识
- **4 个 Must-Fix**: (1) n=3 seeds 不足以支撑 taxonomy stability claims; (2) DiD "causal evidence" 声明缺乏 power analysis; (3) N=4 家族的 taxonomy 泛化性不足; (4) Han et al. (2026) 差异化不充分
- **5 个 Should-Fix**: 正文超 8 页 (desk-reject 风险)、术语混用、RRF calibration 验证、skewed exposure simulation、Algorithm 1 sensitivity curve
- **1 个分歧** (已解决): IRT identifiability 严重程度——R2 用 Appendix P 数据反驳 R1 的 "critical" 定级，最终降为 Should-Fix (仅 skewed exposure gap)
- **3 篇遗漏引用**: Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)
- **视觉审查**: 5 warnings (前 3 页无 display item、Figure 1 位置偏后、正文超页、末页空白、中段视觉断档)
- **Issue tracker 已同步更新**: 8 个新 issue + 历史 issue 状态更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 69

## Round 69

54 recorded events


### User

_source line 683 · 2026-05-21T15:53:03.589012+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contamcal-irt-calibration
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle (Main + Findings unified)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-21T15:53:10.675761+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-21T15:53:10.727703+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-21T15:53:16.749001+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-21T15:53:16.900070+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-21T15:53:19.961128+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-21T15:53:20.011732+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-21T15:53:25.385050+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
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

_source line 691 · 2026-05-21T15:53:25.485900+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-21T15:53:31.720587+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-21T15:53:32.824878+00:00_

{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (394 个)\n\n- **exp_001_sft_d100_05B**: DONE (success) — \n- **exp_001_sft_0pct**: DONE (success) — \n- **exp_001_sft_0pct_3B_s123**: DONE (success) — \n- **exp_001_eval_15B_d000_s42**: DONE (failed) — \n- **exp_001_sft_d005_05B_v2**: DONE (failed) — \n- **exp_001_sft_d005_05B**: DONE (killed) — \n- **exp_001_sft_100pct_05B**: DONE (failed) — \n- **exp_001_sft_0pct_3B**: DONE (success) — \n- **exp_001_sft_injection**: DONE (success) — \n- **exp_001_sft_0pct_15B_s123**: DONE (success) — \n- **exp_001_sft_0pct_05B_s123**: DONE (success) — \n- **exp_001_sft_0pct_15B**: DONE (success) — \n- **exp_001_sft_0pct_05B**: DONE (success) — \n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T15:43:56Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 391 个实验 — ANALYZING 1, DONE 353, PREPARING 35, QUEUED 2\n**DONE 分布**: failed 62, killed 16, negative 10, success 265\n\n### GPU 占用\n- **分配**: 2 张 — cqa1-21977:cuda:0, westd-29999:cuda:0\n- **空闲（分配了没跑）**: cqa1-21977:cuda:0, westd-29999:cuda:0\n\n### 💾 磁盘余量\n- **cqa1-21977**:\n  - `/autodl-pub`: 357G/7.0T 可用（已用 96%） ⚠️\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\n- **westd-29999**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `sft_llama3_d100_s0` [success] — 2026-05-21T13:50:29\n- `sft_llama3_d025_s0` [success] — 2026-05-21T12:32:40\n- `sft_llama3_d000_s0` [success] — 2026-05-21T12:21:00\n- `eval_phi4_gsm8k_d000_s0` [success] — 2026-05-21T09:05:52\n- `eval_qwen14b_d100_gsm8k_s0` [success] — 2026-05-21T09:04:52\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|
…[truncated 2652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-21T15:53:32.825251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-21T15:53:33.326917+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{float}
15	
16	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{abstract}
25	\end{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{experimental_setup}
31	\input{results}
32	\input{conclusion}
33	
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-21T15:53:33.327268+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 697 · 2026-05-21T15:53:34.431414+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 698 · 2026-05-21T15:53:34.582574+00:00_

-rw-r--r-- 1 ubuntu ubuntu 589055 May 21 15:50 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-21T15:53:38.936615+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the web search results, I found information about EMNLP 2026, though the main con
…[truncated 1249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 5609
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-21T15:53:47.130855+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limits author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limits author instructions"
  }
}
```

</details>

---


### Tool call

_source line 701 · 2026-05-21T15:53:47.682527+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Budapest call for papers deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 Budapest call for papers deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-21T15:53:49.491216+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper && ls -la *.tex *.bib 2>/dev/null && echo \"---\" && wc -l *.tex 2>/dev/null",
  "description": "List paper source files and line counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper && ls -la *.tex *.bib 2>/dev/null && echo \"---\" && wc -l *.tex 2>/dev/null",
    "description": "List paper source files and line counts"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-21T15:53:49.592367+00:00_

-rw-r--r-- 1 ubuntu ubuntu  2188 May 21 13:58 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu 32806 May 21 15:50 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu  1010 May 21 13:49 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu  1089 May 19 08:35 ethics.tex
-rw-r--r-- 1 ubuntu ubuntu  3860 May 21 11:41 experimental_setup.tex
-rw-r--r-- 1 ubuntu ubuntu  3649 May 21 13:58 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu   818 May 21 15:49 limitations.tex
-rw-r--r-- 1 ubuntu ubuntu   740 May 19 20:34 main.tex
-rw-r--r-- 1 ubuntu ubuntu 11151 May 21 08:13 method.tex
-rw-r--r-- 1 ubuntu ubuntu 23103 May 21 11:41 references.bib
-rw-r--r-- 1 ubuntu ubuntu  2895 May 21 08:13 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu 13420 May 21 15:42 results.tex
---
    1 abstract.tex
  467 appendix.tex
    3 conclusion.tex
    5 ethics.tex
   28 experimental_setup.tex
   21 introduction.tex
    4 limitations.tex
   41 main.tex
  101 method.tex
    7 related_work.tex
  136 results.tex
  814 total
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_director_c2ad40d8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 704 · 2026-05-21T15:53:52.658470+00:00_

Web search results for query: "EMNLP 2026 Budapest call for papers deadline commitment"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here's the key information about EMNLP 2026 in Budapest:

## Main Conference Papers Submission

The EMNLP 2026 paper submission deadline is May 25, 2026 at 23:59:59 (UTC-12). Papers that have received reviews and a meta-review from ARR (whether from th
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 4975
}
```

</details>

---


### Tool call

_source line 705 · 2026-05-21T15:53:52.960414+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 706 · 2026-05-21T15:53:53.111490+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-21T15:53:53.615709+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limits author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on my web search results, here's what I found about ACL Rolling Review (ARR) 2026 submission guidelines:

## Key Author Instructions:

Submissions must adhere to the formatting in the submission templates, which is available as an Overleaf template. Additionally, ARR abandoned the MS Word Template for conference submissions, with submissions based 
…[truncated 1060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 6484
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-21T15:53:58.339620+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the full submission guidelines: page limits for long papers and short papers, formatting requirements, anonymity policy, supplementary material rules, citation format, and any other requirements authors must follow."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the full submission guidelines: page limits for long papers and short papers, formatting requirements, anonymity policy, supplementary material rules, citation format, and any other requirements authors must follow."
  }
}
```

</details>

---


### Tool call

_source line 709 · 2026-05-21T15:53:59.696302+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/industry_track/",
  "prompt": "Extract the EMNLP 2026 main conference paper submission requirements, deadlines, page limits, formatting rules, and commitment deadlines. Look for any links to the main conference CFP."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/industry_track/",
    "prompt": "Extract the EMNLP 2026 main conference paper submission requirements, deadlines, page limits, formatting rules, and commitment deadlines. Look for any links to the main conference CFP."
  }
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-21T15:54:00.650532+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration -name \"config.yaml\" -o -name \"config.yml\" -o -name \"*.toml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration -name \"config.yaml\" -o -name \"config.yml\" -o -name \"*.toml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-21T15:54:01.107701+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/pandas/pyproject.toml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/pyproject.toml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-21T15:54:01.258746+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-21T15:54:01.309411+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 714 · 2026-05-21T15:54:04.924354+00:00_

# EMNLP 2026 Industry Track Requirements

Based on the webpage provided, here are the key submission details for the **Industry Track** (note: the main conference paper CFP is referenced but not detailed on this page):

## Key Deadlines
- **Submission:** June 16, 2026 (11:59 PM UTC-12:00)
- **Acceptance Notification:** August 20, 2026
- **Camera-ready:** September 20, 2026
- **Conference:** October 24-29, 2026 (Budapest, Hungary)

## Page Limits & Format
- **Maximum 6 pages** for initial submission (excluding references, limitations, ethical considerations, acknowledgments, appendices)
- Accepted papers receive **1 additional page** (up to 7 pages total) for revisions
- Must use ACL templates; non-conforming submissions face desk rejection
- Submissions in PDF format only

## Critical Requirements
- Papers must include a mandatory "Limitations" section (doesn't count toward page limit)
- Double-blind review required: no author names, affiliations, or identifying self-references
- Use anonymized repositories for code (not Dropbox/Google Drive)
- All accepted papers require in-person or online presentation
- At least one author must register by early registration deadline

## Submission Link
https://openreview.net/group?id=EMNLP/2026/Industry_Track

**Note:** This page covers the Industry Track specifically. For main conference paper requirements, you would need to consult the dedicated main conference CFP page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebFetch",
  "elapsed_ms": 5228
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-21T15:54:05.737527+00:00_

# ACL Rolling Review Submission Guidelines

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space after conclusion for limitations (required) and optional ethical considerations section
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space after conclusion for limitations (required) and optional ethical considerations section
- Unlimited reference pages

Papers exceeding length requirements or lacking a limitations section face desk rejection.

## Formatting Requirements

Submissions must adhere to the official ACL style template available on GitHub (acl-org/acl-style-files). Authors cannot modify these style files or use templates from other conferences. Papers must follow "*ACL" conference formatting guidelines regarding paper size, margins, and font sizes. Non-conforming submissions are rejected without review.

## Anonymity Policy

Papers must exclude author names, affiliations, and self-identifying references (e.g., "We previously showed..."). Instead, use third-person citations. Supplementary materials and repository links require anonymization. Dropbox and similar download-tracking services are prohibited. Violations result in desk rejection. Authors may optionally post non-anonymous preprints, with anonymous submissions receiving priority in borderline cases.

## Supplementary Materials

Appendices, software, and data are encouraged but optional. Key technical content necessary for assessing novelty and validity must appear in the main paper, not appendices. Supplementary materials must be fully anonymized. Software should be submitted as single .tgz or .zip archives through anonymized repositories (e.g., Anonymous GitHub), not cloud services like Dropbox.

## Citation Format

For concurrent papers by overlapping author sets: "Anonymous (2026). Paper title. Under review." Authors must cite relevant refereed publications and contemporaneous preprints (those posted within 3 months before submission)
…[truncated 446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebFetch",
  "elapsed_ms": 7397
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-21T15:54:11.937168+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13 -maxdepth 3 -name \"config.yaml\" 2>/dev/null",
  "description": "Find project config at broader scope"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13 -maxdepth 3 -name \"config.yaml\" 2>/dev/null",
    "description": "Find project config at broader scope"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-21T15:54:12.441365+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-21T15:54:12.642508+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-21T15:54:12.693646+00:00_

&lt;persisted-output>
Output too large (34.7KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-director-c2ad40d8/e20fcf2d-ff61-4f3b-9495-14c0b14dcbef/tool-results/bqpj5rcas.txt

Preview (first 2KB):
- id: "R2-N1"
  summary: "Title/framing promises general answer but experiments only cover SFT ≤3B"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 6
  mentions:
    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices."}
    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'. Abstract implies contamination-specific modeling."}
    - {round: 4, reviewers: "R1,R2", note: "Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing."}
    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form but framing still inconsistent."}
    - {round: 6, reviewers: "R1,R2", note: "Title question form improved but still over-scopes."}
    - {round: 8, reviewers: "", note: "本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'."}
  action_items:
    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
    - {round: 4, action: "Reframe as empirical investigation rather than method paper", assigned_to: "paper_agent", status: "done"}
    - {round: 5, action: "Rewrite Introduction from ¶1 as question-driven empirical investigation", assigned_to: "paper_agent", status: "done"
…[truncated 125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-21T15:54:39.243751+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13 -maxdepth 4 -name \"config*\" -not -path \"*/.venv/*\" -not -path \"*/node_modules/*\" -not -path \"*/__pycache__/*\" 2>/dev/null",
  "description": "Find project config files broadly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13 -maxdepth 4 -name \"config*\" -not -path \"*/.venv/*\" -not -path \"*/node_modules/*\" -not -path \"*/__pycache__/*\" 2>/dev/null",
    "description": "Find project config files broadly"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-21T15:54:39.344480+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/config

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-21T15:54:43.059925+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/ 2>/dev/null && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/contamcal-irt-calibration.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/ 2>/dev/null && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/contamcal-irt-calibration.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-21T15:54:43.160879+00:00_

approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
email_tokens.json
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_briefer.json
mcp_config_director.json
mcp_config_dream_review_director.json
mcp_config_no_project.json
mcp_config_paper_agent.json
mcp_config_paper_audit_content.json
mcp_config_paper_audit_review_visual.json
mcp_config_paper_audit_visual.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_00dfb0018fc66ec96d8b8ea00616820b.json
mcp_config_worker_074936fc4b5d802648d5b9b7fe3a8a01.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
mcp_config_worker_3223f6c92aba6990fc4fd60c9c817114.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
mcp_config_worker_34a94861e96b7887a157fa6d27e375e0.json
mcp_config_worker_34b8beca3d3e38da8c29b9af314ca15a.json
mcp_config_worker_3683e51e3c097c93488562d683342ec7.json
mcp_config_worker_39b779349130764ce7503c2772342ff4.json
mcp_config_worker_3ab953c77b6b0e7621a87cc89f47e64a.json
mcp_config_worker_4abc3d757168e825e9637e1693914dfd.json
mcp_config_worker_4dc52b836d4b7ae24139c5fa8c29372a.json
mcp_config_worker_567fac45f9ef5ad1a9223cbb3364faf1.json
mcp_config_worker_592b3808646a7c6e68254a6eac279699.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_6f0b694c30c8a0575c498898ae58e765.json
mcp_config_worker_6fd17e67a8715a880e8a0fc749aac552.json
mcp_config_worker_72b5a7797b623899786091579596a8b2.json
mcp_config_worker_7f289b4cf49d35629c3aa93f15a08233.json
mcp_config_worker_7fc16ee950d4cc0902b80c47aa5b8063.json
mcp_config_worker_8164f16cea05223301ec10d99f320a22.json
mcp_config_worker_817dc7abdffc6c37323c06d15
…[truncated 1179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-21T15:54:46.777772+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/ 2>/dev/null && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/contamcal-irt-calibration.yaml 2>/dev/null | head -60",
  "description": "Find project-specific config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/ 2>/dev/null && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/contamcal-irt-calibration.yaml 2>/dev/null | head -60",
    "description": "Find project-specific config"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-21T15:54:46.828538+00:00_

contamcal-irt-calibration.yaml
---
execution:
  gpu_ids:
  - 0
  project_path: /root/contamcal-irt-calibration
  servers:
  - gpu_ids:
    - 0
    server: cqa1-21977
  - account: root
    gpu_ids:
    - 0
    - 1
    - 2
    - 3
    server: westd-29999
feishu:
  chat_id: oc_4960c7baa442eabd4fa0aceeac2693ca
  operational_chat_id: oc_a79563aecf81c0da6bbb0710df2f0b6d
  review_mode: fresh
  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf
  review_round: 7
  review_supplementary_paths: ''
  submission_chat_id: oc_da6d629d7f92da47a5e85cb7e296ae13
project:
  created_at: '2026-05-13T04:23:49.315Z'
  description: 'ContamCal: Bayesian Calibration of Contamination-Adjusted Benchmark
    Scores via Provenance-Augmented Item Response Theory'
  name: contamcal-irt-calibration
  phase: research
  source_idea_id: idea_017
venue: emnlp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-21T15:54:52.560039+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A10 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/contamcal-irt-calibration.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_SECTION\" && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_registry.yaml 2>/dev/null | grep -A20 \"emnlp-2026\" || echo \"NO_VENUE_REGISTRY\"",
  "description": "Check external review and venue config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A10 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/contamcal-irt-calibration.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_SECTION\" && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_registry.yaml 2>/dev/null | grep -A20 \"emnlp-2026\" || echo \"NO_VENUE_REGISTRY\"",
    "description": "Check external review and venue config"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-21T15:54:52.612473+00:00_

NO_EXTERNAL_REVIEW_SECTION
---
  emnlp-2026:
    display_name: EMNLP 2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-21T15:54:58.288660+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_rules/emnlp-2026.yaml 2>/dev/null || echo \"NO_VENUE_RULES_FILE\"",
  "description": "Check EMNLP 2026 venue rules"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_rules/emnlp-2026.yaml 2>/dev/null || echo \"NO_VENUE_RULES_FILE\"",
    "description": "Check EMNLP 2026 venue rules"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-21T15:54:58.339500+00:00_

rules:
  research: []
  review:
  - created_at: '2026-05-17T12:02:15Z'
    id: c9bba9
    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
  - created_at: '2026-05-19T12:23:13Z'
    id: bd0516
    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
      main text, with unlimited space for references. Mandatory limitations and optional
      ethical considerations do not count towards this page limit, provided they do
      not contain excessive additional content.
  writing:
  - created_at: '2026-05-21T06:49:14Z'
    id: 2468a8
    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-21T15:55:17.093200+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-21T15:55:29.748107+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 12654
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-21T15:55:29.799191+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: \"Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf`\n\n### Venue 要求\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板，Long paper，正文 ≤8 页，参考文献不限\n- **Limitations**: 必需章节（不计入页数）\n- **匿名**: Double-blind\n- **评分标准 (Overall Assessment)**: 5=Consider for Award（约前2.5%），4.5=Borderline Award，4=Conference（可被主会议接收），3.5=Borderline Conference，3=Findings（可被Findings接收），2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit\n\n### 你的审查重点\n\n请从以下角度严格审查：\n\n1. **方法论严谨性**：\n   - IRT 模型的设定是否合理？参数可识别性是否有保证？\n   - 贝叶斯推断过程是否正确（先验选择、MCMC 收敛诊断、后验分析）？\n   - 统计检验是否恰当？效应量是否有实际意义（而非仅统计显著）？\n   - 是否存在混淆变量、选择偏差、或循环论证？\n\n2. **实验设计**：\n   - 实验覆盖的模型家族、规模、benchmark 是否足够支撑论文的 claim？\n   - 控制变量是否充分？ablation 是否完整？\n   - 训练细节（超参数、随机种子、数据划分）是否可复现？\n   - 负面结果（如 gamma 不显著）是否被诚实报告？\n\n3. **统计分析**：\n   - 表格和图表中的数字是否一致？\n   - 置信区间/可信区间是否正确报告？\n   - 多重比较校正是否必要且已执行？\n   - dose-response 关系的建模是否有替代方案被考虑？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (按严重程度排列) → Questions → Minor Issues → Score (使用 EMNLP 评分标准)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: \"Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf`\n\n### Venue 要求\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板，Long paper，正文 ≤8 页，参考文献不限\n- **Limitations**: 必需章节（不计入页数）\n- **匿名**: Double-blind\n- **评分标准 (Overall Assessment)**: 5=Consider for Award（约前2.5%），4.5=Borderline Award，4=Conference（可被主会议接收），3.5=Borderline Conference，3=Findings（可被Findings接收），2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit\n\n### 你的审查重点\n\n请从以下角度严格审查：\n\n1. **方法论严谨性**：\n   - IRT 模型的设定是否合理？参数可识别性是否有保证？\n   - 贝叶斯推断过程是否正确（先验选择、MCMC 收敛诊断、后验分析）？\n   - 统计检验是否恰当？效应量是否有实际意义（而非仅统计显著）？\n   - 是否存在混淆变量、选择偏差、或循环论证？\n\n2. **实验设计**：\n   - 实验覆盖的模型家族、规模、benchmark 是否足够支撑论文的 claim？\n   - 控制变量是否充分？ablation 是否完整？\n   - 训练细节（超参数、随机种子、数据划分）是否可复现？\n   - 负面结果（如 gamma 不显著）是否被诚实报告？\n\n3. **统计分析**：\n   - 表格和图表中的数字是否一致？\n   - 置信区间/可信区间是否正确报告？\n   - 多重比较校正是否必要且已执行？\n   - dose-response 关系的建模是否有替代方案被考虑？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (按严重程度排列) → Questions → Minor Issues → Score (使用 EMNLP 评分标准)。"
  }
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-21T15:55:43.550528+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13751
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-21T15:55:43.752801+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: \"Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf`\n\n### Venue 要求\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板，Long paper，正文 ≤8 页，参考文献不限\n- **Limitations**: 必需章节（不计入页数）\n- **匿名**: Double-blind\n- **评分标准 (Overall Assessment)**: 5=Consider for Award（约前2.5%），4.5=Borderline Award，4=Conference（可被主会议接收），3.5=Borderline Conference，3=Findings（可被Findings接收），2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit\n\n### 你的审查重点\n\n请从以下角度严格审查：\n\n1. **新颖性与贡献**：\n   - 论文的核心 contribution 是什么？与现有 benchmark contamination 文献相比有多少增量？\n   - \"dose-response\" 框架是否真正新颖？还是已有工作的简单组合？\n   - 分类法（Immune/Benefit/Collapse/V-recovery）是否有理论支撑还是纯经验归纳？\n   - 这篇论文对社区的实际影响力如何？\n\n2. **相关工作**：\n   - 是否遗漏了重要的相关工作？特别关注：\n     - Benchmark contamination detection 方法（Min-K++, BDA, membership inference）\n     - IRT 在 NLP/LLM 评估中的应用\n     - 数据污染对 LLM 的影响研究\n     - Dose-response modeling 在其他领域（药理学、环境科学）的先例\n   - 相关工作的讨论是否公平？是否有 straw-man 式的对比？\n\n3. **写作质量**：\n   - 论文叙事是否连贯？Introduction 的动机是否清晰？\n   - Claims 与 evidence 是否匹配？是否有 overclaiming？\n   - 术语使用是否一致？符号定义是否清晰？\n   - 图表是否信息丰富且易读？\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内？\n   - 是否使用正确的 ACL 模板？\n   - 参考文献格式是否规范？\n   - Limitations 章节是否存在且有实质内容？\n   - 匿名性是否完整（无 GitHub 链接、个人网站等泄露身份信息）？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (按严重程度排列) → Questions → Missing References → Minor Issues → Score (使用 EMNLP 评分标准)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: \"Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf`\n\n### Venue 要求\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板，Long paper，正文 ≤8 页，参考文献不限\n- **Limitations**: 必需章节（不计入页数）\n- **匿名**: Double-blind\n- **评分标准 (Overall Assessment)**: 5=Consider for Award（约前2.5%），4.5=Borderline Award，4=Conference（可被主会议接收），3.5=Borderline Conference，3=Findings（可被Findings接收），2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit\n\n### 你的审查重点\n\n请从以下角度严格审查：\n\n1. **新颖性与贡献**：\n   - 论文的核心 contribution 是什么？与现有 benchmark contamination 文献相比有多少增量？\n   - \"dose-response\" 框架是否真正新颖？还是已有工作的简单组合？\n   - 分类法（Immune/Benefit/Collapse/V-recovery）是否有理论支撑还是纯经验归纳？\n   - 这篇论文对社区的实际影响力如何？\n\n2. **相关工作**：\n   - 是否遗漏了重要的相关工作？特别关注：\n     - Benchmark contamination detection 方法（Min-K++, BDA, membership inference）\n     - IRT 在 NLP/LLM 评估中的应用\n     - 数据污染对 LLM 的影响研究\n     - Dose-response modeling 在其他领域（药理学、环境科学）的先例\n   - 相关工作的讨论是否公平？是否有 straw-man 式的对比？\n\n3. **写作质量**：\n   - 论文叙事是否连贯？Introduction 的动机是否清晰？\n   - Claims 与 evidence 是否匹配？是否有 overclaiming？\n   - 术语使用是否一致？符号定义是否清晰？\n   - 图表是否信息丰富且易读？\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内？\n   - 是否使用正确的 ACL 模板？\n   - 参考文献格式是否规范？\n   - Limitations 章节是否存在且有实质内容？\n   - 匿名性是否完整（无 GitHub 链接、个人网站等泄露身份信息）？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (按严重程度排列) → Questions → Missing References → Minor Issues → Score (使用 EMNLP 评分标准)。"
  }
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-21T15:55:45.230522+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1477
}
```

</details>

---


### Assistant

_source line 736 · 2026-05-21T15:55:52.833891+00:00_

已全部派发：

- ✅ **视觉审查 Agent**：已启动（fire-and-forget，不阻塞）
- ✅ **Reviewer 1**（方法严谨性 + 实验 + 统计）：已派发
- ✅ **Reviewer 2**（新颖性 + 相关工作 + 写作 + 格式）：已派发

等待两位 Reviewer 返回独立审稿意见，收到后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 70

## Round 70

2 recorded events


### User

_source line 737 · 2026-05-21T16:03:55.279740+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

### 论文信息
**标题**: "Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families"
**审查侧重**: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 研究问题重要且实验设计系统，但 LoRA SFT 注入的生态效度不足以支撑论文对真实污染场景的推断，分类法的理论基础和泛化性均有待加强。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 实验设计系统但 LoRA SFT ≠ 预训练污染，4 个模型家族不足以支撑分类法的泛化性 |
| Excitement | 3.5/5 | 研究问题有真实价值，dose-response 视角新颖，但技术贡献偏增量 |
| Reproducibility | 4/5 | 实验细节详尽，附录充实，Algorithm 1 可操作 |
| Overall Assessment | 3.5/5 | Borderline Conference |
| Confidence | 4/5 | 熟悉 IRT、LLM 评估和数据污染领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] LoRA SFT 注入的生态效度根本性不足
- 具体位置：Section 4.1, Limitations (p.9)
- 问题：所有污染实验均通过 LoRA SFT 注入基准题目（Section 4.1: "unified LoRA configuration"），但真实世界的 benchmark contamination 发生在预训练阶段，与 SFT 微调在学习机制上截然不同。SFT 直接优化答案匹配，而预训练中的偶然暴露是隐式的。论文在 Limitations 中仅一句话提及，但这不是边缘局限——它直接影响 4 个 dose-response pattern 的推断效度。Schaeffer et al. (2026) 已通过预训练污染展示了不同的 dose-response 关系（"contamination matters most when model capacity is high and the unique pretraining corpus is small; overtraining with fresh data dilutes the dose to near zero"），其结论与本文基于 SFT 的发现可能存在本质差异。
- 为什么影响接收：如果 dose-response pattern 是 LoRA SFT 的 artifact，论文核心贡献的实际应用价值大幅降低。
- 建议：(1) 在 Introduction/Method 中显式承认此 caveat；(2) 充分讨论 Schaeffer et al. 的预训练结果与本文的异同；(3) 提供 SFT 作为预训练暴露合理近似的论证。

**N2** [critical] 分类法理论基础薄弱，泛化性不足
- 具体位置：Algorithm 1 (p.5), Section 5.1 (p.6), Table 1 (p.6)
- 问题：四分类法完全基于经验归纳，依赖任意阈值（τ=2pp, n=5, ρ=0.3, λ=0.5pp）。Appendix P (Table 14) 的敏感性测试范围很窄。更关键的是仅 4 个独立家族，V-recovery 只在 Qwen-7B 上观察到（n=1）。
- 为什么影响接收：n=1 的 pattern 不足以构成 robust taxonomy class；4 个家族不支撑泛化 claim。
- 建议：增加模型家族验证或降低 claim 为 "exploratory taxonomy"；对 V-recovery 给出理论解释。

---

## Should-Fix 问题

**W1** [warning] "Dose-response" 框架缺乏正式的 dose-response 建模
- 论文借用药理学术语但没有拟合参数化曲线（Hill equation / sigmoid E_max model），仅在 5 个离散剂量上做分类比较。建议拟合正式 dose-response 曲线或调整术语。

**W2** [warning] 与 Schaeffer et al. (2026) 和 Han et al. (2026) 的关系讨论不充分
- 这两篇是最直接的竞争/互补工作，但前者仅在 Conclusion 一句话提及，后者在 Related Work 一句。建议专段对比。

**W3** [warning] DID 零效应的过度解读
- 正文声称 "no detectable item-specific memorization"，但 Appendix N 显示 MDES 在 1.25–2.05pp（n=3 seeds）。应 reframe 为 "effects below detection threshold" 而非无效应。

**W4** [warning] Calibration 比较基线不够强
- Table 4 的基线偏简单，缺少更先进的 calibration 方法（如 Bayesian calibration、ensemble methods）。

---

## 小问题
- Figure 1 仅展示 seed=42，主图应展示 error bars
- "catastrophic collapse" 用于 ≤25pp 下降略显夸张
- ARC IRT marginal model fit (PPP=0.003) 应在正文讨论而非仅放附录
- 引用 `holland_1993_dif` 年份 mismatch 需确认

## 缺失的重要相关工作
1. 药理学 dose-response 建模经典文献（Hill 1910; Ritz et al. 2015）
2. Balloccu et al. (2024) "Leak, Cheat, Repeat" (EACL 2024)
3. Bordt et al. (2025) "How Much Can We Forget about Data Contamination?"

## 主要优势
1. 研究问题精准且有实际价值
2. 四家族 × 五剂量 × 三基准 × 多 seed 的 factorial design 严谨
3. Cross-benchmark transfer 的 GSM8K 方向反转发现有趣
4. IRT 框架提供置信区间，对实践者有用
5. 附录极其充实，体现良好实验规范

## 格式合规
- ✅ 正文 8 页，符合 EMNLP 2026 Long paper 限制
- ✅ ACL 模板正确
- ✅ Limitations 章节存在且有实质内容
- ✅ Ethics Statement 存在
- ✅ 匿名性完整，未发现身份泄露
- ✅ 参考文献格式基本规范（minor mismatches 见上）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 738 · 2026-05-21T16:04:02.354023+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 71

## Round 71

6 recorded events


### User

_source line 739 · 2026-05-21T16:04:04.982905+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**论文**: "Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families"
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析
**参照标准**: ACL ARR Review Form (Soundness / Excitement / Overall Assessment)

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 研究问题重要、实验设计规范、IRT 框架合理，但分类法基于 ad-hoc 算法缺乏统计建模基础，核心因果声称（架构决定脆弱性）证据不足，且 N=4 家族的样本量对分类法泛化性构成根本限制。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | IRT 方法论扎实，贝叶斯推断流程规范（R̂ < 1.01, ESS > 500, PPP），但 Algorithm 1 的阈值设定 ad hoc，统一 LoRA 配置引入未讨论的混淆 |
| Excitement | 3.5/5 | Dose-response 框架新颖且有方法论贡献，但核心发现（不同模型不同反应）在直觉上可预期；分类法的实用价值受限于泛化性不足 |
| Reproducibility | 4/5 | 超参数（LoRA r=16, α=32, lr=5e-5）、种子、MCMC 配置（4 chains）、收敛诊断报告充分，附录极为详尽 |
| Reviewer Confidence | 4/5 | 熟悉 IRT、贝叶斯推断、LLM 评估方法和 DIF 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 分类法（Taxonomy）基于 ad-hoc 算法而非正式 dose-response 建模

- **具体位置**：Section 3.3, Algorithm 1 (Page 5)
- **问题**：Algorithm 1 使用多个硬编码阈值（噪声阈值 τ = 2pp, 模式阈值 n = 5, 晚期增益下限 ρ = 0.3, 饱和增益 λ = 0.5pp）将 dose-response 曲线分为 Immune / Collapse / V-Recovery / Benefit 四类。虽然 Appendix P (Table 14) 显示五个家族在"reasonable parameter range"内均达到 100% 分类稳定性，但该方法本质上是描述性规则分类，而非模型驱动的统计推断。药理学和毒理学中有成熟的参数化 dose-response 模型（如 sigmoidal Emax、log-logistic 4 参数模型、Hill 方程），可通过似然比检验或信息准则（AIC/BIC）在竞争模型间做正式选择。当前方法的根本缺陷是**无法量化分类的不确定性**——一个家族被标记为"Collapse"而不是"V-Recovery"的置信度是多少？当数据点在分类边界附近时（如 Qwen-7B 的 V-Recovery 与 Benefit 之间），规则分类无法给出概率性判断。
- **为什么影响接收**：分类法是论文三大贡献之一（Contribution 1, Section 1）。如果分类法缺乏统计基础，后续基于分类的所有推论（"架构决定脆弱性"、"65–70% 脆弱带"等）都建立在不稳固的地基上。
- **建议修改方向**：(1) 拟合参数化 dose-response 模型（如 4 参数 log-logistic）到每个家族的 accuracy-vs-dosage 曲线，通过参数比较（EC50, Hill slope, Emax）量化家族间差异；(2) 为分类结果提供不确定性度量（如 bootstrap 置信度或后验概率）；(3) 若坚持使用 Algorithm 1，至少应正式讨论为何不采用参数化 dose-response 建模，以及该选择的 trade-off。

**N2** [critical] "架构而非基线能力决定脆弱性"的因果声称证据不足

- **具体位置**：Section 6 第一段 ("architecture, not baseline ability alone, determines contamination vulnerability")；Section 1, Contribution 1；Abstract ("showing that architecture rather than baseline ability determines vulnerability")
- **问题**：该因果声称主要基于两条证据：(a) OLMo-2 (53.8% MMLU) 表现为 Benefit，与基线更高的 Qwen-7B (66.1%) 的 V-Recovery 不同，说明基线能力不是唯一决定因素；(b) 在 Qwen2.5 家族内部，14B (69.4%) 比 7B (66.1%) 更脆弱，但前者基线更高。然而，**不同模型家族在"架构"之外存在大量混淆变量**：预训练数据的分布和规模、tokenizer 词表大小和覆盖率、预训练目标（如 Phi-4 的合成数据策略）、训练步数和学习率调度、数据去重和质量过滤策略。论文无法将这些因素与架构本身（attention 类型、层数、FFN 结构等）分离。即使在 Qwen2.5 内部，14B 与 7B 可能使用了不同的预训练数据量和训练步数，而非仅仅是参数量的差异。
- **为什么影响接收**：这是论文的**标题级声称**——"Across Model Families"暗示家族间差异的根源已被识别。如果因果推断不成立，论文的贡献定位需要降级。
- **建议修改方向**：(1) 将 "architecture determines" 弱化为 "baseline ability alone does not determine"，这是数据能支撑的结论；(2) 在 Section 6 中系统列出无法排除的混淆因素；(3) 避免在 Abstract 和 Title 中暗示因果关系。当前发现是重要的**描述性**结果（不同家族确实表现不同），不需要因果包装来保持价值。

**N3** [critical] N=4 训练家族对分类法泛化性的根本限制

- **具体位置**：Section 4.1 (实验设置), Section 5.1 (Cross-family results), Table 1
- **问题**：论文从 4 个训练家族（Phi-4, Qwen-14B, OLMo-2, Qwen-7B/Gemma-2）中归纳出 4 类 dose-response 模式，并用 1 个 held-out 家族（LLaMA-3.1-8B）验证。关键问题：
  - **4 类模式恰好由 4 个家族产生**：每种模式仅由 1 个家族代表（Immune→Phi-4, Collapse→Qwen-14B, V-Recovery→OLMo-2/Qwen-7B, Benefit→Gemma-2）。无法排除这些模式是特定于具体模型的 idiosyncratic 行为，而非真正可泛化的"类型"。
  - **Held-out 验证仅覆盖一种模式**：LLaMA-3.1-8B 被分类为 Immune，但 Collapse、V-Recovery、Benefit 三种模式均无独立验证。
  - **规模范围有限**：所有模型 ≤14B。对 70B+ 模型的适用性完全未知，而这恰恰是实践中污染检测最重要的场景。
  - **仅覆盖 LoRA SFT**：real-world 污染更多发生在 pre-training 阶段（web crawl 泄露），与 LoRA SFT 注入的机制可能有本质差异。Limitations 中提到了这一点，但未讨论其对分类法泛化性的影响。
- **为什么影响接收**：分类法的学术价值在于泛化性。一个 N=4 的归纳、N=1 的验证，很难让读者相信这是通用的类型学而非实验条件下的巧合。
- **建议修改方向**：(1) 将分类法明确定位为"初步观察/假说生成"而非"已验证的类型学"；(2) 在 Section 6 和 Limitations 中清晰讨论 N=4 的局限性和泛化风险；(3) 具体列出哪些额外实验能增强泛化性（如更多家族、更大模型、full fine-tuning、pre-training 注入等）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 统一 LoRA 配置（r=16）引入的未讨论混淆

- **具体位置**：Section 4.1 ("unified LoRA configuration (r = 16, α = 32, lr = 5 × 10⁻⁵, bf16)")
- **问题**：所有模型使用相同 LoRA 超参（r=16），但 LoRA 的相对表达能力与模型参数量成反比。对 14B 模型，r=16 的参数占比远小于对 7B 模型。这意味着"treatment strength"在不同规模模型间不等价。Phi-4 14B 的 Immune 模式可能部分源于 LoRA 容量不足以实现有效 memorization——虽然 Qwen-14B 同为 14B 且表现为 Collapse 可以部分反驳这一假说，但两者架构差异可能导致 LoRA 对不同 layer 的影响效率不同。论文完全未讨论这一混淆。
- **建议**：(1) 在 Limitations 中讨论 LoRA 容量作为混淆因素；(2) 理想情况下补充 r∈{8, 16, 32, 64} 的消融实验或至少在一个家族上测试。

**W2** [warning] DID 零结果的功效限制在正文中表述不够审慎

- **具体位置**：Section 5.4, Table 3, Appendix N (MDES 1.25–2.05pp)
- **问题**：正文 Section 5.4 标题为 "No detectable item-specific memorization"，但 Appendix N 的 MDES 分析显示最小可检测效应量为 1.25pp（MMLU at d025, 80% power）至 2.05pp。这意味着 ≤1.25pp 的 item-specific 效应无法被排除。论文在 Section 5.4 末尾提到"ARC's limited power precludes the same conclusions there"，但对 MMLU 的功效限制在正文中未充分说明。将"no detectable memorization"作为 Section 标题和 Contribution 2 强调，容易被误读为"memorization does not exist"而非"we lack power to detect small effects"。
- **建议**：(1) 将 Section 5.4 标题改为更审慎的表述（如 "Limited Evidence for Item-Specific Memorization"）；(2) 在正文中明确报告 MDES 数值而非仅放在附录；(3) 讨论 1.25pp 的 item-specific 效应在实践中是否重要。

**W3** [warning] 曝光分数（s_ij）的分类性能未定量报告

- **具体位置**：Section 3.1 (Stage 1: Multi-Signal Exposure Mapping), Section 5.6 (Detection Signal Failure Modes)
- **问题**：Stage 1 构造的曝光分数 s_ij 通过 RRF 融合 4 个信号（S1 embedding similarity, S2 token-level surprisal, S3 contamination gap, S4 self-critique），直接作为协变量进入 IRT 模型。s_ij 的测量误差会传递到 γ 的估计中（衰减偏差/attenuation bias）。但论文未报告 s_ij 在已知污染标签（d000 vs. d100 的 item membership）下的分类性能指标（如 ROC-AUC、precision-recall）。Section 5.6 定性讨论了 Min-K%++ 的失败模式，Table 4 比较了不同方法的 MAE，但缺乏 s_ij 本身作为二分类器的系统评估。
- **建议**：在附录中补充 s_ij 在 d005/d025/d050/d100 下区分 treated vs. untreated items 的 AUC 及 PR 曲线，以便读者评估协变量质量。

**W4** [warning] "65–70% MMLU 基线脆弱带"声称的数据支撑薄弱

- **具体位置**：Section 5.1 第二段 ("Contamination vulnerability concentrates in the 65–70% MMLU baseline band"), Abstract, Figure 1 caption
- **问题**：该声称基于 5 个模型的数据点：Phi-4 (76.4%) Immune, Qwen-14B (69.4%) Collapse, Qwen-7B (66.1%) V-Recovery, OLMo-2 (~64%) V-Recovery, Gemma-2 (~62%) Benefit。实际数据显示的是"76% 以上免疫，62–69% 受不同方式影响"，而非精确的"65–70% band"。此外 Gemma-2 在 ~62% 显示 Benefit（明显受影响），但论文将 62% 描述为"extreme baseline"with "limited sensitivity"，这与 Benefit 分类矛盾。用 5 个数据点声称一个精确百分比区间是对稀疏数据的过度拟合。
- **建议**：弱化为定性描述（如 "models with moderate baseline accuracy appear more vulnerable than those with very high baselines"），避免给出看似精确但实际上 under-determined 的百分比区间。

---

## 小问题（不影响接收）

- Section 3.2 中 2PL+γ 的先验分布仅以"priors"一词一带而过，正文中应至少给出 θ 和 γ 的先验形式。Appendix 中有但读者不应被迫翻附录来评估模型设定的合理性。
- Figure 1: 两个子图 y 轴范围不同（MMLU ~60–80%, ARC-Challenge ~55–80%），虽然合理但两条曲线的视觉斜率不直接可比。建议在 caption 中提醒读者注意 y 轴差异。
- Table 2 (page 7): "Con." 列（consistency）的定义（"25 strict sign consistency on …"）较难直接从表中理解，建议改用更自解释的列名或在表注中展开。
- Limitations 中列出了 LoRA vs. pre-training 污染的差异，但未讨论 instruction tuning vs. continued pre-training 这两种常见污染路径在效应机制上的差异，建议补充一句。
- Section 5.2 (Cross-Benchmark Transfer): GSM8K 分析排除了 Qwen-7B（due to CvT collapse）后仅剩 4 个家族，进一步削弱了跨 benchmark 结论的泛化性。
- Section 5.5 (Calibration Quality): Table 4 将 ContamCal 与 6 个 baseline 比较，但 baseline 选择中 B5-Emperor 引用的是 Sun et al. (2025) 的缓解策略而非校准方法，两者目标不完全对齐，比较公平性值得说明。

---

## 主要优势

1. **研究问题定义清晰且有实际价值**：现有文献多做二元（污染/干净）比较，本文首次系统建模连续 dose-response 关系，填补了重要方法论空白。
2. **实验设计严谨**：控制 SFT 注入 + 已知 ground truth + 多种子 + 多家族 + held-out 验证 + 跨 benchmark 迁移——这是为数不多遵循了实验因果推断范式的 LLM 评估研究。
3. **IRT 框架的引入恰当且技术实施扎实**：将测量理论（2PL+γ, explanatory DIF）与 LLM 评估结合是有意义的方法论贡献。贝叶斯推断提供了校准的可信区间，收敛诊断（R̂, ESS, PPP）报告充分。
4. **诚实报告零结果和局限**：DID 非显著（Section 5.4）、ARC 功效不足、cross-seed CI 宽度等不利结果均如实报告，未做选择性呈现。
5. **附录极为详尽**（10 页）：涵盖收敛诊断（Appendix I）、功效分析（Appendix N）、阈值鲁棒性（Appendix P）、domain 分解（Appendix Q）、4PL 扩展（Appendix G）等，达到了高标准的可复现性。
6. **跨 benchmark 迁移分析增加深度**：GSM8K 上发现的方向性反转（Qwen-7B directional reversal）和多模式转移模式（null, consistent, directional reversal）提供了超越单一 benchmark 的见解。

---

## 问题（需要作者回应）

Q1: γ 参数的识别来源——是主要从同一模型内不同 item 的 s_ij 变异中识别（within-model cross-item），还是从不同 dosage 配置间的 s_ij 分布差异中识别（cross-dosage）？如果是后者，θ 和 γ 的分离依赖什么排除限制？

Q2: Algorithm 1 产出的分类是否对输入数据的 noise 敏感？如果在每个 dosage 下的 accuracy 加上 ±1pp 的均匀噪声，有多少家族的分类会发生变化？

Q3: 论文将 Phi-4 的 Immune 归因于架构，但 Phi-4 以大量使用合成数据（synthetic data）进行预训练著称。是否考虑过 Phi-4 的 immunity 更可能源于预训练数据策略而非架构本身？

Q4: 如果将 LoRA rank 从 16 提升到 64（增加记忆容量），Phi-4 的分类是否可能从 Immune 变为其他模式？这对"架构决定脆弱性"的结论有何影响？

---

**总结**：论文在重要问题上做了扎实的工作，IRT 框架和控制实验设计是明确的贡献。主要问题集中在三点：(1) 分类法需要更强的统计基础，(2) 因果声称需要降级为描述性发现，(3) 泛化性限制需要更坦诚地讨论。如果三个 Must-Fix 得到充分处理（主要是文本层面的弱化声称 + 方法论讨论的补充），本文具备 Conference/Findings 接收的潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-21T16:04:54.463428+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n### 总体评分\n**Overall**: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] LoRA SFT 注入的生态效度根本性不足\n- 具体位置：Section 4.1, Limitations (p.9)\n- 问题：所有污染实验均通过 LoRA SFT 注入基准题目（Section 4.1: \"unified LoRA configuration\"），但真实世界的 benchmark contamination 发生在预训练阶段，与 SFT 微调在学习机制上截然不同。SFT 直接优化答案匹配，而预训练中的偶然暴露是隐式的。论文在 Limitations 中仅一句话提及，但这不是边缘局限——它直接影响 4 个 dose-response pattern 的推断效度。Schaeffer et al. (2026) 已通过预训练污染展示了不同的 dose-response 关系，其结论与本文基于 SFT 的发现可能存在本质差异。\n- 为什么影响接收：如果 dose-response pattern 是 LoRA SFT 的 artifact，论文核心贡献的实际应用价值大幅降低。\n\n**N2** [critical] 分类法理论基础薄弱，泛化性不足\n- 具体位置：Algorithm 1 (p.5), Section 5.1 (p.6), Table 1 (p.6)\n- 问题：四分类法完全基于经验归纳，依赖任意阈值（τ=2pp, n=5, ρ=0.3, λ=0.5pp）。Appendix P (Table 14) 的敏感性测试范围很窄。更关键的是仅 4 个独立家族，V-recovery 只在 Qwen-7B 上观察到（n=1）。\n- 为什么影响接收：n=1 的 pattern 不足以构成 robust taxonomy class；4 个家族不支撑泛化 claim。\n\n### Should-Fix 问题\n\n**W1** [warning] \"Dose-response\" 框架缺乏正式的 dose-response 建模\n- 论文借用药理学术语但没有拟合参数化曲线（Hill equation / sigmoid E_max model），仅在 5 个离散剂量上做分类比较。\n\n**W2** [warning] 与 Schaeffer et al. (2026) 和 Han et al. (2026) 的关系讨论不充分\n- 这两篇是最直接的竞争/互补工作，但前者仅在 Conclusion 一句话提及，后者在 Related Work 一句。\n\n**W3** [warning] DID 零效应的过度解读\n- 正文声称 \"no detectable item-specific memorization\"，但 Appendix N 显示 MDES 在 1.25–2.05pp（n=3 seeds）。应 reframe 为 \"effects below detection threshold\" 而非无效应。\n\n**W4** [warning] Calibration 比较基线不够强\n- Table 4 的基线偏简单，缺少更先进的 calibration 方法（如 Bayesian calibration、ensemble methods）。\n\n### 小问题\n- Figure 1 仅展示 seed=42，主图应展示 error bars\n- \"catastrophic collapse\" 用于 ≤25pp 下降略显夸张\n- ARC IRT marginal model fit (PPP=0.003) 应在正文讨论而非仅放附录\n- 引用 `holland_1993_dif` 年份 mismatch 需确认\n\n### 缺失的重要相关工作\n1. 药理学 dose-response 建模经典文献（Hill 1910; Ritz et al. 2015）\n2. Balloccu et al. (2024) \"Leak, Cheat, Repeat\" (EACL 2024)\n3. Bordt et al. (2025) \"How Much Can We Forget about Data Contamination?\"\n\n### 主要优势\n1. 研究问题精准且有实际价值\n2. 四家族 × 五剂量 × 三基准 × 多 seed 的 factorial design 严谨\n3. Cross-benchmark transfer 的 GSM8K 方向反转发现有趣\n4. IRT 框架提供置信区间，对实践者有用\n5. 附录极其充实，体现良好实验规范\n\n### 格式合规\n- ✅ 正文 8 页，符合 EMNLP 2026 Long paper 限制\n- ✅ ACL 模板正确\n- ✅ Limitations 章节存在且有实质内容\n- ✅ Ethics Statement 存在\n- ✅ 匿名性完整，未发现身份泄露\n- ✅ 参考文献格式基本规范"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n### 总体评分\n**Overall**: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] LoRA SFT 注入的生态效度根本性不足\n- 具体位置：Section 4.1, Limitations (p.9)\n- 问题：所有污染实验均通过 LoRA SFT 注入基准题目（Section 4.1: \"unified LoRA configuration\"），但真实世界的 benchmark contamination 发生在预训练阶段，与 SFT 微调在学习机制上截然不同。SFT 直接优化答案匹配，而预训练中的偶然暴露是隐式的。论文在 Limitations 中仅一句话提及，但这不是边缘局限——它直接影响 4 个 dose-response pattern 的推断效度。Schaeffer et al. (2026) 已通过预训练污染展示了不同的 dose-response 关系，其结论与本文基于 SFT 的发现可能存在本质差异。\n- 为什么影响接收：如果 dose-response pattern 是 LoRA SFT 的 artifact，论文核心贡献的实际应用价值大幅降低。\n\n**N2** [critical] 分类法理论基础薄弱，泛化性不足\n- 具体位置：Algorithm 1 (p.5), Section 5.1 (p.6), Table 1 (p.6)\n- 问题：四分类法完全基于经验归纳，依赖任意阈值（τ=2pp, n=5, ρ=0.3, λ=0.5pp）。Appendix P (Table 14) 的敏感性测试范围很窄。更关键的是仅 4 个独立家族，V-recovery 只在 Qwen-7B 上观察到（n=1）。\n- 为什么影响接收：n=1 的 pattern 不足以构成 robust taxonomy class；4 个家族不支撑泛化 claim。\n\n### Should-Fix 问题\n\n**W1** [warning] \"Dose-response\" 框架缺乏正式的 dose-response 建模\n- 论文借用药理学术语但没有拟合参数化曲线（Hill equation / sigmoid E_max model），仅在 5 个离散剂量上做分类比较。\n\n**W2** [warning] 与 Schaeffer et al. (2026) 和 Han et al. (2026) 的关系讨论不充分\n- 这两篇是最直接的竞争/互补工作，但前者仅在 Conclusion 一句话提及，后者在 Related Work 一句。\n\n**W3** [warning] DID 零效应的过度解读\n- 正文声称 \"no detectable item-specific memorization\"，但 Appendix N 显示 MDES 在 1.25–2.05pp（n=3 seeds）。应 reframe 为 \"effects below detection threshold\" 而非无效应。\n\n**W4** [warning] Calibration 比较基线不够强\n- Table 4 的基线偏简单，缺少更先进的 calibration 方法（如 Bayesian calibration、ensemble methods）。\n\n### 小问题\n- Figure 1 仅展示 seed=42，主图应展示 error bars\n- \"catastrophic collapse\" 用于 ≤25pp 下降略显夸张\n- ARC IRT marginal model fit (PPP=0.003) 应在正文讨论而非仅放附录\n- 引用 `holland_1993_dif` 年份 mismatch 需确认\n\n### 缺失的重要相关工作\n1. 药理学 dose-response 建模经典文献（Hill 1910; Ritz et al. 2015）\n2. Balloccu et al. (2024) \"Leak, Cheat, Repeat\" (EACL 2024)\n3. Bordt et al. (2025) \"How Much Can We Forget about Data Contamination?\"\n\n### 主要优势\n1. 研究问题精准且有实际价值\n2. 四家族 × 五剂量 × 三基准 × 多 seed 的 factorial design 严谨\n3. Cross-benchmark transfer 的 GSM8K 方向反转发现有趣\n4. IRT 框架提供置信区间，对实践者有用\n5. 附录极其充实，体现良好实验规范\n\n### 格式合规\n- ✅ 正文 8 页，符合 EMNLP 2026 Long paper 限制\n- ✅ ACL 模板正确\n- ✅ Limitations 章节存在且有实质内容\n- ✅ Ethics Statement 存在\n- ✅ 匿名性完整，未发现身份泄露\n- ✅ 参考文献格式基本规范"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-21T16:05:20.321233+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25857
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-21T16:05:20.573686+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 分类法（Taxonomy）基于 ad-hoc 算法而非正式 dose-response 建模\n- 具体位置：Section 3.3, Algorithm 1 (Page 5)\n- 问题：Algorithm 1 使用多个硬编码阈值（τ=2pp, n=5, ρ=0.3, λ=0.5pp）将 dose-response 曲线分为四类。本质上是描述性规则分类，而非模型驱动的统计推断。药理学中有成熟的参数化 dose-response 模型（Hill 方程、log-logistic 4 参数模型），可通过 AIC/BIC 做正式模型选择。当前方法无法量化分类的不确定性。\n- 为什么影响接收：分类法是三大贡献之一，如果缺乏统计基础，后续推论均建立在不稳固地基上。\n\n**N2** [critical] \"架构而非基线能力决定脆弱性\"的因果声称证据不足\n- 具体位置：Section 6 第一段, Section 1, Abstract\n- 问题：不同模型家族在\"架构\"之外存在大量混淆变量（预训练数据、tokenizer、训练策略等），论文无法分离架构与其他因素。即使 Qwen2.5 内部，14B 与 7B 可能使用不同的预训练数据量和训练步数。\n- 为什么影响接收：这是标题级声称，因果推断不成立则贡献定位需降级。\n\n**N3** [critical] N=4 训练家族对分类法泛化性的根本限制\n- 具体位置：Section 4.1, Section 5.1, Table 1\n- 问题：4 类模式恰好由 4 个家族产生，每种模式仅 1 个家族代表。Held-out 验证仅覆盖 Immune 一种模式。规模范围 ≤14B。V-Recovery 仅 n=1。\n- 为什么影响接收：N=4 的归纳 + N=1 的验证，不足以支撑通用类型学。\n\n### Should-Fix 问题\n\n**W1** [warning] 统一 LoRA 配置（r=16）引入的未讨论混淆\n- LoRA 的相对表达能力与模型参数量成反比。对 14B 模型 r=16 的参数占比远小于 7B。Phi-4 的 Immune 可能部分源于 LoRA 容量不足。\n\n**W2** [warning] DID 零结果的功效限制在正文中表述不够审慎\n- Section 5.4 标题 \"No detectable item-specific memorization\" 易被误读为 \"memorization does not exist\"。MDES 为 1.25–2.05pp 应在正文报告。\n\n**W3** [warning] 曝光分数（s_ij）的分类性能未定量报告\n- s_ij 直接作为协变量进入 IRT 模型，但未报告其在已知污染标签下的分类性能（ROC-AUC、precision-recall）。\n\n**W4** [warning] \"65–70% MMLU 基线脆弱带\"声称数据支撑薄弱\n- 仅 5 个数据点，实际显示\"76% 以上免疫，62–69% 受不同方式影响\"，精确百分比区间是过度拟合。\n\n### 小问题\n- 2PL+γ 先验分布正文中应给出形式\n- Figure 1 两子图 y 轴范围不同，caption 应提醒\n- Table 2 \"Con.\" 列定义不够自解释\n- Limitations 未讨论 instruction tuning vs. continued pre-training 路径差异\n- GSM8K 分析排除 Qwen-7B 后仅剩 4 个家族\n- Table 4 中 B5-Emperor 的比较公平性值得说明\n\n### 问题\nQ1: γ 参数识别来源——within-model cross-item 还是 cross-dosage？分离依赖什么排除限制？\nQ2: Algorithm 1 对输入 ±1pp 噪声的敏感性？\nQ3: Phi-4 的 Immune 是否更可能源于合成数据策略而非架构？\nQ4: LoRA rank 从 16 提升到 64，Phi-4 分类是否可能变化？\n\n### 主要优势\n1. 研究问题定义清晰且有实际价值\n2. 实验设计严谨（控制 SFT + ground truth + 多种子 + 多家族 + held-out + 跨 benchmark）\n3. IRT 框架引入恰当且技术实施扎实\n4. 诚实报告零结果和局限\n5. 附录极为详尽（10 页）\n6. 跨 benchmark 迁移分析增加深度"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 分类法（Taxonomy）基于 ad-hoc 算法而非正式 dose-response 建模\n- 具体位置：Section 3.3, Algorithm 1 (Page 5)\n- 问题：Algorithm 1 使用多个硬编码阈值（τ=2pp, n=5, ρ=0.3, λ=0.5pp）将 dose-response 曲线分为四类。本质上是描述性规则分类，而非模型驱动的统计推断。药理学中有成熟的参数化 dose-response 模型（Hill 方程、log-logistic 4 参数模型），可通过 AIC/BIC 做正式模型选择。当前方法无法量化分类的不确定性。\n- 为什么影响接收：分类法是三大贡献之一，如果缺乏统计基础，后续推论均建立在不稳固地基上。\n\n**N2** [critical] \"架构而非基线能力决定脆弱性\"的因果声称证据不足\n- 具体位置：Section 6 第一段, Section 1, Abstract\n- 问题：不同模型家族在\"架构\"之外存在大量混淆变量（预训练数据、tokenizer、训练策略等），论文无法分离架构与其他因素。即使 Qwen2.5 内部，14B 与 7B 可能使用不同的预训练数据量和训练步数。\n- 为什么影响接收：这是标题级声称，因果推断不成立则贡献定位需降级。\n\n**N3** [critical] N=4 训练家族对分类法泛化性的根本限制\n- 具体位置：Section 4.1, Section 5.1, Table 1\n- 问题：4 类模式恰好由 4 个家族产生，每种模式仅 1 个家族代表。Held-out 验证仅覆盖 Immune 一种模式。规模范围 ≤14B。V-Recovery 仅 n=1。\n- 为什么影响接收：N=4 的归纳 + N=1 的验证，不足以支撑通用类型学。\n\n### Should-Fix 问题\n\n**W1** [warning] 统一 LoRA 配置（r=16）引入的未讨论混淆\n- LoRA 的相对表达能力与模型参数量成反比。对 14B 模型 r=16 的参数占比远小于 7B。Phi-4 的 Immune 可能部分源于 LoRA 容量不足。\n\n**W2** [warning] DID 零结果的功效限制在正文中表述不够审慎\n- Section 5.4 标题 \"No detectable item-specific memorization\" 易被误读为 \"memorization does not exist\"。MDES 为 1.25–2.05pp 应在正文报告。\n\n**W3** [warning] 曝光分数（s_ij）的分类性能未定量报告\n- s_ij 直接作为协变量进入 IRT 模型，但未报告其在已知污染标签下的分类性能（ROC-AUC、precision-recall）。\n\n**W4** [warning] \"65–70% MMLU 基线脆弱带\"声称数据支撑薄弱\n- 仅 5 个数据点，实际显示\"76% 以上免疫，62–69% 受不同方式影响\"，精确百分比区间是过度拟合。\n\n### 小问题\n- 2PL+γ 先验分布正文中应给出形式\n- Figure 1 两子图 y 轴范围不同，caption 应提醒\n- Table 2 \"Con.\" 列定义不够自解释\n- Limitations 未讨论 instruction tuning vs. continued pre-training 路径差异\n- GSM8K 分析排除 Qwen-7B 后仅剩 4 个家族\n- Table 4 中 B5-Emperor 的比较公平性值得说明\n\n### 问题\nQ1: γ 参数识别来源——within-model cross-item 还是 cross-dosage？分离依赖什么排除限制？\nQ2: Algorithm 1 对输入 ±1pp 噪声的敏感性？\nQ3: Phi-4 的 Immune 是否更可能源于合成数据策略而非架构？\nQ4: LoRA rank 从 16 提升到 64，Phi-4 分类是否可能变化？\n\n### 主要优势\n1. 研究问题定义清晰且有实际价值\n2. 实验设计严谨（控制 SFT + ground truth + 多种子 + 多家族 + held-out + 跨 benchmark）\n3. IRT 框架引入恰当且技术实施扎实\n4. 诚实报告零结果和局限\n5. 附录极为详尽（10 页）\n6. 跨 benchmark 迁移分析增加深度"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-21T16:05:22.094678+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1520
}
```

</details>

---


### Assistant

_source line 744 · 2026-05-21T16:05:25.438209+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 72

## Round 72

2 recorded events


### User

_source line 745 · 2026-05-21T16:05:26.484992+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成。审稿意见已提交给 Review Director。

核心判断：**Overall 3.5 (Borderline Conference)**。两个 critical 问题——(1) LoRA SFT 注入 vs 预训练污染的生态效度鸿沟，(2) 四分类法仅基于 4 个家族且 V-recovery 为 n=1。四个 warning 级问题涉及 dose-response 术语滥用、与并行工作对比不足、DID 零效应过度解读、calibration 基线偏弱。格式完全合规。

---

[Reviewer 1 审稿结果]:
Round 1 审稿完成。评分 **Overall 3.5 (Borderline Conference)**，核心问题三点：

1. **N1**: Algorithm 1 分类法缺乏正式 dose-response 统计建模基础，无法量化分类不确定性
2. **N2**: "架构决定脆弱性"的因果声称超出了数据能支撑的范围（存在大量未控制的混淆变量），应降级为描述性发现
3. **N3**: N=4 家族归纳 + N=1 验证的样本量对分类法泛化性构成根本限制

四个 Should-Fix：统一 LoRA 配置的混淆、DID 零结果功效不足的表述、曝光分数分类性能未报告、"65–70% 脆弱带"声称过于精确。

优势方面：控制实验设计严谨、IRT 贝叶斯框架实施扎实、零结果诚实报告、附录详尽。若三个 Must-Fix 得到处理（主要是弱化声称 + 补充方法论讨论），具备 Conference/Findings 接收潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 746 · 2026-05-21T16:05:32.397706+00:00_

两位 Reviewer 均已提交 Round 1 意见，现在等待他们的 Step 2 交叉回应。交叉分享任务已派发，等待返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 73

## Round 73

2 recorded events


### User

_source line 747 · 2026-05-21T16:07:09.289601+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1

### 逐条回应

**[AGREE] R1-N1 (分类法 ad-hoc)**: 完全同意。与我的 W1 一致，补充指出论文连药理学 dose-response 文献都未引用。

**[AGREE with nuance] R1-N2 (架构因果声称)**: 基本同意因果推断过强。但指出 Qwen 家族内部同架构不同规模也出现不同 pattern，这实际上削弱 "架构决定" 的 claim。Phi-4 vs Qwen-14B（两个 14B 模型，一个 Immune 一个 Collapse）表明存在 family-level 差异，但无法分离架构 vs 预训练数据/策略。建议弱化 claim 为 "family-level factors beyond raw baseline accuracy"。

**[AGREE] R1-N3 (N=4 泛化性)**: 完全同意，与我的 N2 一致。V-recovery n=1 问题最严重。

**[AGREE] R1-W1 (LoRA 容量混淆)**: 同意但部分反驳：若 LoRA 容量是主要驱动因素，两个 14B 模型应表现类似，但 Phi-4(Immune) vs Qwen-14B(Collapse) 是最大分歧。LoRA 容量不能完全解释但确实是需要讨论的混淆。

**[AGREE] R1-W2 (DID 表述)**: 完全同意，与我的 W3 一致。

**[AGREE] R1-W3 (s_ij 分类性能)**: 同意，ground truth 可得情况下此评估完全可行且必要。

**[PARTIALLY REBUT] R1-W4 (65-70% 脆弱带)**: "中等基线更脆弱"的定性观察有支撑（极端高/低 baseline 模型趋向 Immune），但精确到 65-70% 确实是对 5 个数据点的过拟合。

### 共识总结
两位 Reviewer 评分一致（3.5 Borderline Conference），在三个核心问题上完全收敛：(1) N=4 泛化性不足，(2) 因果/机制声称过强，(3) DID 零效应过度解读。R1 额外提出的 LoRA 容量混淆和 s_ij 分类性能缺失是有价值的补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 748 · 2026-05-21T16:07:14.592666+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 749 · 2026-05-21T16:07:17.117961+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。两位 Reviewer 评分一致（3.5），核心问题高度收敛：N=4 泛化性不足、因果声称过强、DID 过度解读。我额外认可了 R1 提出的 LoRA 容量混淆和 s_ij 分类性能缺失两个补充视角。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 750 · 2026-05-21T16:07:22.855519+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 75

## Round 75

28 recorded events


### User

_source line 751 · 2026-05-21T16:07:31.174084+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE with nuance] R2-N1: LoRA SFT 注入的生态效度**

同意这是一个重要局限，但不同意将其升级为"根本性不足"到影响接收的程度。

理由：
1. R2 正确指出 LoRA SFT 注入与 pre-training 阶段泄露在学习机制上不同。论文 Limitations (p.9) 确实仅一句话提及（"our LoRA-based SFT injection in AUGMENT model differs from pre-training-stage leakage via web crawl ingestion"），处理过于轻描淡写。
2. 但 R2 忽略了一个关键方法论 trade-off：**控制实验设计要求已知 ground truth**。Pre-training 污染无法精确控制 dosage——你不知道 web crawl 中包含了多少 benchmark items，也无法保证不同模型的暴露量可比。LoRA SFT 注入是目前唯一能实现"控制剂量 + 已知标签"的实验范式。论文在 Section 4.1 中明确将此定位为 controlled injection testbed。
3. R2 引用 Schaeffer et al. (2026) 称其展示了不同的 dose-response 关系——但论文 Section 6 最后一句已将此作为未来方向（"Extending to pre-training contamination (Schaeffer et al., 2026) and 70B+ scale is a natural next step"）。这表明作者意识到了这一空白。
4. **我的立场**：应在 Limitations 中**显著扩展**对 SFT vs. pre-training 差异的讨论（当前一句话不够），但不应将其视为否定全文贡献的理由。作为首个系统 dose-response 研究，选择可控实验条件是合理的起点。这是 Should-Fix（加强讨论），不是 Must-Fix（推翻结论）。

---

**[AGREE] R2-N2: 分类法泛化性不足**

完全同意，与我的 N3 一致。

但需要纠正 R2 的一个事实错误：R2 称"V-Recovery 只在 Qwen-7B 上观察到（n=1）"，但 **Table 1 (p.6) 明确列出 V-Recovery 包含两个家族：OLMo-2 7B 和 Qwen-7B**。因此 V-Recovery 的支撑是 n=2 而非 n=1。尽管如此，n=2 仍然不足以构成 robust taxonomy class，R2 的核心论点成立。

补充我的观点：更根本的问题是——4 个训练家族恰好产出 4 种模式，这在统计上几乎无法区分"发现了 4 种真实类型"与"每个家族有自己的 idiosyncratic 行为"。分类法应定位为"初步假说"而非"已验证类型学"。

---

### Should-Fix 问题

**[AGREE — 并认为应升级] R2-W1: 缺乏正式 dose-response 建模**

强烈同意，且我在自己的审稿中将此列为 **Must-Fix (N1)**，而非 Should-Fix。

R2 正确指出论文借用药理学术语（"dose-response"）却未拟合药理学标准模型（Hill equation, sigmoid E_max）。我在 N1 中详细论述了这一问题：Algorithm 1 是描述性规则分类，无法量化分类不确定性，且未与参数化 dose-response 模型进行正式比较。这不仅是术语问题——如果论文要以 "dose-response profiling" 作为核心方法论贡献，就应该使用该领域的标准工具。建议 R2 考虑将此升级为 Must-Fix。

---

**[AGREE] R2-W2: 与 Schaeffer et al. (2026) 和 Han et al. (2026) 的讨论不充分**

同意。这两篇是最直接的竞争/互补工作：
- Schaeffer et al. (2026) 做了 pre-training 污染的 dose-response 分析，其结论可能与本文的 SFT 结论存在差异——这恰恰是讨论 SFT vs. pre-training 差异的最佳锚点
- Han et al. (2026) 使用 group-based DIF 量化污染效应，方法论上与本文的 explanatory DIF 方法互补

论文应在 Related Work (Section 2) 中专门用一段对比讨论这两篇工作，说明本文的方法论差异化（controlled injection + continuous dose + item-level IRT vs. 二元检测 + 组级效应）。当前的处理方式（Conclusion 一句、Related Work 一句）不足以帮助读者理解 positioning。

---

**[AGREE] R2-W3: DID 零效应的过度解读**

完全同意，与我的 W2 一致。Section 5.4 标题 "No detectable item-specific memorization" 容易被误读为"记忆化不存在"。Appendix N 的 MDES 1.25–2.05pp 表明这是功效限制下的零结果。应改为 "effects below detection threshold" 或类似审慎措辞。

---

**[REBUT — partially] R2-W4: Calibration 比较基线不够强**

部分不同意。

1. Table 4 (p.8) 的 baseline 选择覆盖了合理的方法谱系：从最简单的 Raw Accuracy (B0)、传统校准方法 (B1b Binning & Rescale, B3 Vanilla 2PL, B4 Linear Regression)、到近期的污染感知方法 (B5 Emperor from Sun et al. 2025, B6 DCR from Xu et al. 2025)。这代表了当前 LLM benchmark 校准的主要方法类别。
2. R2 要求的"Bayesian calibration"——ContamCal 本身就是贝叶斯方法（Section 3.2: NUTS/HMC in Stan, 4 chains, posterior credible intervals）。将贝叶斯 IRT 与非贝叶斯 baseline 对比是合理的，因为要展示的是"IRT 框架的增量价值"而非"贝叶斯 vs. 频率派"。
3. 但 R2 有一个合理的隐含诉求：**缺少其他 IRT 变体作为 baseline**（如不带 γ 的标准 2PL, 3PL, Rasch model），这样才能 isolate γ 参数的边际贡献。Table 4 中 B3 (Vanilla 2PL) 部分满足了这一需求，但可以更系统。
4. "Ensemble methods"在 calibration 语境下指什么不够清楚——如果指 temperature scaling + Platt scaling 的组合，这些在 LLM benchmark 校准中并非标准方法。

**结论**：baseline 选择基本合理，但建议作者在附录中补充 2PL vs. 2PL+γ 的 ablation 以更直接展示 γ 的边际贡献。R2 此条作为 Should-Fix 略显过重，Minor 更恰当。

---

### 小问题

**[AGREE] Figure 1 仅展示 seed=42**：同意。Figure 1 是论文的 key figure，应展示 cross-seed 变异性（至少 error bars 或 shaded bands）。当前仅展示单一 seed 可能给读者"结果比实际更确定"的印象。Table 2 (p.7) 提供了 cross-seed 数据但不如视觉呈现直观。

**[AGREE with nuance] "catastrophic collapse" 措辞**：有道理。从 Table 1 和 Figure 1 看，Qwen-14B 的下降在 MMLU 上是渐进的且绝对值可能在 ~10-15pp 范围。"Catastrophic" 在工程语境中通常暗示系统性失效（如 >50% 性能损失），用于描述 ≤25pp 的下降确实有夸大之嫌。但需注意 Algorithm 1 (p.5) 中 Collapse 的定义是 "severe monotonic degradation"——如果算法的分类标签是技术定义而非修辞，可以保留但应在首次出现时明确其技术含义。

**[AGREE] ARC IRT PPP=0.003**：同意应在正文讨论。PPP=0.003 表明 2PL+γ 模型在 ARC-Challenge 上存在显著 misfit，这直接影响基于该模型的 ARC 结论的可靠性。论文在 Appendix U 中单独报告 ARC 结果已暗示了这一问题，但应在 Section 5 或 Section 6 中明确提出并讨论 implications（如 ARC 的 item 结构可能需要不同的 IRT 模型）。

**[AGREE — 需验证] holland_1993_dif 引用年份**：合理的关注点，作者应核实。Holland and Wainer (1993) 的 DIF 专著确实存在（"Differential Item Functioning", Lawrence Erlbaum），但需确认论文中的具体引用条目与实际出版年份匹配。

---

### 缺失的相关工作

**[AGREE] 药理学 dose-response 经典文献 (Hill 1910; Ritz et al. 2015)**：强烈同意，与我的 N1 直接相关。如果论文要使用 "dose-response" 框架，至少应在 Related Work 或 Method 中引用该领域的基础文献并说明借鉴/偏离之处。Ritz et al. (2015) 的 `drc` R 包提供了 4-parameter log-logistic 等标准模型，正是 Algorithm 1 的参数化替代方案。

**[AGREE] Balloccu et al. (2024) "Leak, Cheat, Repeat"**：同意，这是 contamination 影响评估的重要相关工作（EACL 2024），应在 Related Work 中讨论。

**[AGREE conditionally] Bordt et al. (2025)**：需确认该论文是否已正式发表/arXiv 可查。如果是，应加入 Related Work；如果仅为未公开的 working paper，可在 camera-ready 阶段补充。

---

### 与我的审稿意见的对照总结

| R2 问题 | R2 级别 | 我的对应意见 | 我的级别 | 一致性 |
|--------|--------|-----------|--------|--------|
| N1 LoRA 生态效度 | Must-Fix | W1 LoRA 配置混淆 | Should-Fix | 部分一致——我关注的是 LoRA 容量混淆，R2 关注的是 SFT vs. pre-training 范式差异。两者互补。 |
| N2 分类法泛化性 | Must-Fix | N3 N=4 家族限制 | Must-Fix | **高度一致** |
| W1 缺乏正式 dose-response 建模 | Should-Fix | N1 ad-hoc 算法 | Must-Fix | 一致——我认为应更高优先级 |
| W2 相关工作讨论 | Should-Fix | 未专门提出 | — | 同意 R2 |
| W3 DID 零效应解读 | Should-Fix | W2 DID 功效限制 | Should-Fix | **完全一致** |
| W4 Calibration baseline | Should-Fix | 未专门提出 | — | 部分反驳 |

**两位 Reviewer 的共识点**：(1) 分类法泛化性不足是核心问题；(2) DID 零结果需更审慎表述；(3) 论文的实验设计和 IRT 方法论是明确优势。

**分歧点**：(1) LoRA SFT 的生态效度——R2 视为根本性缺陷，我视为可通过加强讨论缓解的 Should-Fix；(2) 正式 dose-response 建模——R2 列为 Should-Fix，我认为应为 Must-Fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-21T16:07:53.469240+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-21T16:07:54.021922+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T15:55:20.584611+00:00\", \"completed_at\": \"2026-05-21T15:58:42.367840+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"Algorithm 1 跨页：伪代码从 Page 4 下半部分起始，延续到 Page 5 上半部分（约 29 行），审稿人需翻页阅读完整算法。建议压缩至单页（合并条件分支/简化描述），或调整 float 位置使其完整出现在一页内\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 2 尺寸偏小：DID 置信区间图压缩在约 1/4 栏宽内，数据点标签和误差线在正常阅读距离下难以辨认。建议放大至至少半栏宽，或改用 figure* 全宽展示\"}, {\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"Method 段视觉节奏偏单调：连续 3 页（pp3-5）以纯文本+公式为主，无 figure/table。虽然 Algorithm 1 在 pp4-5 提供了部分视觉断点，但审稿人在方法段容易疲劳。如有可能，在 Method 段增加一个示意图（如 pipeline 流程图或 IRT 模型参数的直观图解）\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 图例字号偏小：五条模型线的 legend 文字在 150 dpi 渲染下可读但勉强，打印版可能更吃力。建议将 legend 字号提升到 ≥9pt，或将 legend 移至图外部单独排列\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Figure 4（Detection AUC heatmap）使用的色阶从浅到深渐变，数值标注清晰；但若色阶涉及红-绿区分，对色盲读者不友好。建议确认使用 viridis/cividis 等色盲安全 colormap\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Figure 5（recovery heatmap）单元格内数字标注字号很小（约 6-7pt），在打印版上可能难以辨认。建议增大字号或减少网格密度\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Page 13 display item 密度过高：1 个 figure + 1 个 heatmap + 2 个 table 挤在同一页。虽然是 Appendix，但审稿人阅读体验下降。建议适当分散\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格 ✓，最优值加粗 ✓，精度一致 ✓——表格排版规范\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Tables 2-3 格式规范，CI 标注清晰，显著性标记（*/**）可见 ✓\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段简短（约 1 段），符合 EMNLP 要求。Ethics Statement 紧随其后。References 排版正常，无可见 [?] 未解析引用\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"主正文 8 页，符合 EMNLP 2026 long paper 8 页限制 ✓\"}, {\"severity\": \"info\", \"dimension\": \"page 10-11\", 
…[truncated 138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-21T16:07:54.022414+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-21T16:07:55.329497+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-21T16:07:55.329950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-21T16:07:55.481807+00:00_

1	- id: "R2-N1"
2	  summary: "Title/framing promises general answer but experiments only cover SFT ≤3B"
3	  category: framing
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 2
7	  last_seen_round: 6
8	  mentions:
9	    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices."}
10	    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'. Abstract implies contamination-specific modeling."}
11	    - {round: 4, reviewers: "R1,R2", note: "Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing."}
12	    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form but framing still inconsistent."}
13	    - {round: 6, reviewers: "R1,R2", note: "Title question form improved but still over-scopes."}
14	    - {round: 8, reviewers: "", note: "本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'."}
15	  action_items:
16	    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
17	    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
18	    - {round: 4, action: "Reframe as empirical investigation rather than method paper", assigned_to: "paper_agent", status: "done"}
19	    - {round: 5, action: "Rewrite Introduction from ¶1 as question-driven empirical investigation", assigned_to: "paper_agent", status: "done"}
20	    - {round: 6, action: "Modify title to scope claim", assigned_to: "paper_agent", status: "done"}
21	  resolution: "D149+ rewrite: Title changed to 'Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families'. Paper repositioned as sys
…[truncated 12552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-21T16:08:01.404356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-21T16:08:01.455360+00:00_

200	    - {round: 4, action: "Remove phantom Appendix E reference", assigned_to: "paper_agent", status: "done"}
201	    - {round: 5, action: "Rename §5.5 to 'Cross-Family Exploratory Analysis'", assigned_to: "paper_agent", status: "done"}
202	  resolution: ""
203	  resolution_round: null
204	
205	- id: "R3-W12"
206	  summary: "STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance"
207	  category: method
208	  severity: warning
209	  status: resolved
210	  first_raised_round: 3
211	  last_seen_round: 5
212	  resolution: "Full prior sensitivity complete. Not re-raised since R5."
213	  resolution_round: 5
214	  mentions:
215	    - {round: 3, reviewers: "R2,R1", note: "Three domains identical γ=+0.50."}
216	    - {round: 5, reviewers: "", note: "Not re-raised. Prior sensitivity in Appendix C."}
217	  action_items:
218	    - {round: 3, action: "Check prior dominance", assigned_to: "main_agent", status: "done"}
219	    - {round: 4, action: "Run prior sensitivity with N(0,0.5) and N(0,2)", assigned_to: "main_agent", status: "done"}
220	
221	- id: "R4-W2"
222	  summary: "Min-K%++ directional reversal — causal explanation is unverified hypothesis"
223	  category: method
224	  severity: warning
225	  status: resolved
226	  first_raised_round: 4
227	  last_seen_round: 6
228	  resolution: "Conclusion scoped. Hypothesis labeled post-hoc. Not re-raised in R8."
229	  resolution_round: 6
230	  mentions:
231	    - {round: 4, reviewers: "R1,R2", note: "§5.2 hypothesizes token-level surprisal disruption but no direct evidence."}
232	    - {round: 5, reviewers: "R1,R2", note: "Must be scoped to 'under SFT injection'."}
233	    - {round: 6, reviewers: "", note: "Not independently re-raised. Scoped and labeled post-hoc."}
234	  action_items:
235	    - {round: 4, action: "Reframe as observed phenomenon without causal claim", assigned_to: "paper_agent", status: "done"}
236	    - {round: 5, action: "Scope Conclusion Min-K++ claim to 'at the 0.5B scale under S
…[truncated 9964 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-21T16:08:08.438950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
  "offset": "399",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
    "offset": "399",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-21T16:08:08.489742+00:00_

399	  severity: info
400	  status: resolved
401	  first_raised_round: 6
402	  last_seen_round: 8
403	  mentions:
404	    - {round: 6, reviewers: "R2", note: "Prompt design, evaluation distribution construction, and scoring mechanism not described."}
405	    - {round: 8, reviewers: "", note: "Appendix E (S4 Self-Critique Signal Details) now provides prompt, logit extraction, and scoring formula."}
406	  action_items:
407	    - {round: 6, action: "Add S4 computation details in appendix", assigned_to: "paper_agent", status: "done"}
408	  resolution: "Appendix E added with S4 details."
409	  resolution_round: 8
410	
411	- id: "R6-W3"
412	  summary: "SFT training curves not reported — convergence verification missing"
413	  category: experiment
414	  severity: info
415	  status: resolved
416	  first_raised_round: 6
417	  last_seen_round: 8
418	  mentions:
419	    - {round: 6, reviewers: "R1", note: "Training convergence is prerequisite for controlled injection validity."}
420	    - {round: 8, reviewers: "", note: "Appendix F (Training Convergence) now reports final training loss by dosage. Minimal but present."}
421	  action_items:
422	    - {round: 6, action: "Report SFT training curves or convergence verification in Appendix", assigned_to: "paper_agent", status: "done"}
423	  resolution: "Appendix F added with convergence info."
424	  resolution_round: 8
425	
426	- id: "R6-W4"
427	  summary: "Within-family GSM8K PPP not reported"
428	  category: experiment
429	  severity: info
430	  status: open
431	  first_raised_round: 6
432	  last_seen_round: 8
433	  mentions:
434	    - {round: 6, reviewers: "R1,R2", note: "Cross-family GSM8K PPP=0.83 but within-family GSM8K PPP not reported."}
435	    - {round: 8, reviewers: "", note: "本轮未提及。Still not reported in current version."}
436	  action_items:
437	    - {round: 6, action: "Report within-family GSM8K PPP", assigned_to: "main_agent", status: "open"}
438	  resolution: ""
439	  resolution_round: null
440	
441	# === Round 8 (Fre
…[truncated 9017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-21T16:08:50.181778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-21T16:08:51.084574+00:00_

1	Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but qualitatively different dose-response patterns---from immunity (mean $\Delta < 1$\,percentage point [pp] across three seeds) through monotonic benefit ($+$2.4pp mean) to catastrophic collapse ($-$9 to $-$25pp across seeds). Contamination vulnerability concentrates in the 65--70\% MMLU baseline band; models at extreme baselines show limited sensitivity. Counter-intuitively, the 14B Qwen model is 3$\times$ more fragile than 7B. These effects are benchmark-conditional: models harmed on MMLU can simultaneously benefit on GSM8K ($+$10pp), revealing asymmetric cross-benchmark transfer. Difference-in-differences analysis finds no item-specific memorization on MMLU (minimum detectable effect size 1.2--2.0pp); ARC has limited power (2.3--5.6pp). Profiles are robust on MMLU (4/5 families $\geq$99.6\% within-seed item-level bootstrap stability); per-seed signs vary (2/5 strict sign consistency on MMLU), but ARC-Challenge shows cross-seed directional agreement for 4/5 families despite lower item-level stability due to its smaller item pool (1{,}172 vs.\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \geq 50$) above current practice. Out-of-sample validation on a held-out fifth family (LLaMA-3.1-8B) confirms taxonomy generalizability: it is classified Immune despite a baseline matching OLMo-2's Benefit, showing that architecture rather than baseline ability determines vulnerabilit
…[truncated 192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 902
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-21T16:08:51.135281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-21T16:08:51.637524+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig_dose_response.pdf}
10	\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42). Vulnerability concentrates in the 65--70\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref{sec:arc_cross_benchmark}.}
11	\label{fig:dose_response}
12	\end{figure*}
13	
14	Contamination vulnerability concentrates in the 65--70\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\times$ more fragile than 7B. Using ContamCal, a two-stage pipeline combining multi-signal item filtering with contamination-augmented
…[truncated 1706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-21T16:08:51.637930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-21T16:08:51.838671+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Controlled SFT injection reveals qualitatively different dose-response patterns across model families---not uniform inflation---with vulnerability concentrated in the 65--70\% MMLU baseline band and larger models counter-intuitively more fragile (Qwen-14B $-$15.7pp vs.\ 7B $-$1.8pp). DiD analysis finds no item-specific memorization on MMLU (MDES 1.2--2.0pp), challenging overlap-based detection; direction reproduces across seeds and benchmarks (3/5 on ARC) but magnitude is seed-sensitive. Domain-level IRT reveals heterogeneity masked by aggregate scores (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$). Out-of-sample validation on held-out LLaMA-3.1-8B (Immune despite a baseline matching OLMo-2's Benefit) confirms taxonomy generalizability and shows that architecture, not baseline ability alone, determines contamination vulnerability. Extending to pretraining contamination \citep{schaeffer2026causally} and 70B+ scale is a natural next step.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-21T16:08:51.889181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-21T16:08:51.939824+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use models at or below 14.7B parameters; 70B+ models may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without measurable signal divergence. With $n\!=\!3$ seeds per family, effect \emph{direction} is reproducible but magnitude is seed-sensitive (OLMo-2's cross-seed CI crosses zero, rendering its Benefit classification borderline), and borderline classifications should be interpreted with caution. Finally, our LoRA-based SFT injection in AUGMENT mode differs from pretraining-stage leakage via web crawl ingestion, and our dosage levels assume uniform injection of all benchmark items; real-world contamination may follow skewed exposure distributions, potentially producing different dose-response profiles.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-21T16:09:09.484951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
    "limit": "30"
  }
}
```

</details>

---


### Tool call

_source line 771 · 2026-05-21T16:09:09.486526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 772 · 2026-05-21T16:09:09.537185+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of mode
…[truncated 1854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-21T16:09:09.537840+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{table}[t]
10	\centering
11	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\% stability across 30 reasonable $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
12	\label{tab:taxonomy}
13	\footnotesize
14	\begin{tabular}{llccccc}
15	\toprule
16	Pattern & Model & Baseline & $\Delta$acc & 95\% CI & Peak & Stab. \\
17	\midrule
18	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% \\
19	Collapse & Qwen-14B & 69.4\% & $-$9.4 to $-$12.7pp & [$-$12.74, $-$9.0] & --- & 100\% \\
20	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
21	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\% \\
22	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% \\
23	\bottomrule
24	\multicolumn{7}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.6pp, s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.}
25	\end{tabular}
26	\end{table}
27	
28	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields qualitatively different dose
…[truncated 3739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-21T16:13:18.174798+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form but framing still inconsistent.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Title framing no longer flagged.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D149+ rewrite: Title changed to 'Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families'. Paper repositioned as systematic empirical investigation of dose-response across 5 models (7B-14.7B) from 4 families. No over-scoping.\"\n  resolution_round: 7\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. All claims must be scoped to 'under SFT injection at ≤3B scale'.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Conclusion 'applies directly to settings with larger effects' is unsupported forward claim.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised as Should-Fix. Both agree SFT ecological validity is known limitation.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Re-raised. R2 flags as Must-Fix (critical): LoRA SFT ≠ pretraining contamination, dose-response patterns may be SFT artifacts, Schaeffer et al. (2026) shows different DR under pretraining. R1 downgrades to Should-Fix: controlled injection is only way to get ground truth dosage, paper correctly positions as testbed. DIVERGENT on severity. Consensus: Limitations discussion still too brief (one sentence), needs significant expansion with Schaeffer et al. comparison.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims to 'under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Ensure Abstract first sentence explicitly scopes to SFT injection\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Remove/caveat Conclusion 'applies directly' claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 9, action: \"Expand Limitations SFT vs pretraining discussion significantly; add explicit comparison with Schaeffer et al. (2026) pretraining DR findings\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation has two interpretations.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Both unanimously re-raise as critical. R2 proposes threshold DGP simulation.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。DGP robustness appendix addresses this.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i interaction model\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'under the additive linear specification' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Run threshold DGP simulation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 7, action: \"Write DGP robustness appendix + update Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"400-run threshold DGP simulation completed. Appendix P written. Not re-raised in Round 8 or 9.\"\n  resolution_round: 7\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction + underpowered J\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Bonferroni α=0.00625; CI upper bound likely includes zero.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Social Sciences at 99.1% does not pass Bonferroni.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text §5.4 still presents J=13.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'uncorrected for multiplicity' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text domain γ to J=16 results\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Results §5 reports J=16 for domain γ. P(γ<0)=99.7% at J=16 crosses Bonferroni threshold.\"\n  resolution_round: 7\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations — IRT results unreliable\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at all J.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003. Move ARC IRT to Appendix.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"ARC IRT moved to Appendix.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。ARC IRT in Appendix with PPP caveat.\"}\n    - {round: 9, reviewers: \"R2\", note: \"R2 re-raises: ARC PPP=0.003 should be discussed in main text, not only Appendix. Implications for ARC-based conclusions need explicit treatment in Section 5 or 6.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Move ARC IRT results to Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Clarify ARC IRT parameters are unreliable\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 9, action: \"Add brief discussion of ARC PPP=0.003 implications in main text Section 5 or 6\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality; MAE random control missing\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. No direct RRF vs S1-only ablation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation complete. Downgraded to warning.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Random 300-item subsets report τ but no MAE comparison.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"R1-W1 re-raises RRF calibration verification gap.\"}\n    - {round: 9, reviewers: \"R1\", note: \"R1-W3 re-raises: s_ij classification performance (ROC-AUC, PR) on known contamination labels not reported. Ground truth available from controlled injection but unused for evaluating exposure score quality.\"}\n  action_items:\n    - {round: 3, action: \"Reword C2\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Distinguish exposure variance from signal quality\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Report MAE for random 300-item subsets\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 8, action: \"Report inter-signal rank correlation and leave-one-signal-out ablation\", assigned_to: \"main_agent\", status: \"in_progress\"}\n    - {round: 9, action: \"Report s_ij classification performance (AUC, PR) at each dosage level for treated vs untreated items\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal — over-coverage and under-coverage have different root causes\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Root cause diagnosis still insufficient.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。Root-cause diagnosis now in §5.4.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage to main results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Discuss root causes separately\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Provide explicit root-cause diagnosis\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Root-cause diagnosis in §5.4. Not re-raised in Round 8 or 9.\"\n  resolution_round: 7\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses — J=13 domain finding vs J≥50 standard is self-contradictory\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Most interesting finding uses weakest configuration (J=13).\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text still uses J=13.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。J=16 now in main text.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J prominently in each table\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rerun domain-level γ at J=16\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text to J=16\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Results §5 specifies J=16 for domain γ. Not re-raised in Round 8 or 9.\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Mean a_i comparison shows no discrimination confound. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 may reflect higher average a_i.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised. Resolution confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — caveat adequate but MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Phantom reference to Appendix E.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"MAE CI for cross-family pool not reported.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未直接提及。Cross-family analysis now uses 5 models from 4 families.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Remove phantom Appendix E reference\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rename §5.5 to 'Cross-Family Exploratory Analysis'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Full prior sensitivity complete. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised. Prior sensitivity in Appendix C.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2)\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Conclusion scoped. Hypothesis labeled post-hoc. Not re-raised in R8 or R9.\"\n  resolution_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption but no direct evidence.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must be scoped to 'under SFT injection'.\"}\n    - {round: 6, reviewers: \"\", note: \"Not independently re-raised. Scoped and labeled post-hoc.\"}\n  action_items:\n    - {round: 4, action: \"Reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Scope Conclusion Min-K++ claim to 'at the 0.5B scale under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure — C2 (signal filtering) partially disconnected from main question\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"3 empirical contributions. Not re-raised in R8 or R9.\"\n  resolution_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span too many types.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Now 3 contributions but still span different types.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 reads like method paper contribution.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further consolidate to 2 contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reframe C2 as enabling analysis + standalone practical finding\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — DIF classics + contamination benchmark literature\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. EACL 2026 most direct concurrent work.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"New gaps: Lord, Hambleton, HELM, Magar & Schwartz.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al. needed.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"New missing refs: Golchin & Surdeanu (ICLR 2024), Sainz et al. (EMNLP 2023 Findings), Yang et al. (2023).\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"New missing refs: Hill (1910) and Ritz et al. (2015) dose-response classics; Balloccu et al. (2024) 'Leak, Cheat, Repeat' (EACL 2024); Bordt et al. (2025). Both reviewers agree dose-response literature citation is essential if claiming DR framework.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al., arXiv 2601.04301, Chen et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM, Magar & Schwartz\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Expand Han et al. comparison\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Add Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Add Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 9, action: \"Add dose-response classics: Hill (1910), Ritz et al. (2015); add Balloccu et al. (EACL 2024), Bordt et al. (2025)\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"PPP values filled. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'.\"}\n    - {round: 5, reviewers: \"\", note: \"PPP values now present. Resolved.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high — still ~6+ quantitative claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Abstract rewritten for dose-response taxonomy paper. Not re-raised in R8 or R9.\"\n  resolution_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"~202 words but still 8-9 numbers.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Still 6+ numbers.\"}\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF; must commit to empirical study positioning\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must position as empirical contribution.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 still reads as method. Reposition around controlled testbed + identifiability.\"}\n    - {round: 8, reviewers: \"R2\", note: \"R2 notes novelty primarily comes from experimental paradigm not methodology.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Paper now positioned as empirical investigation.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al. as concurrent work\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Explicitly state empirical investigation positioning\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reposition Han et al. differentiation; elevate J≥50 identifiability\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Paper committed to empirical investigation. Title signals empirical finding. 3 empirical contributions.\"\n  resolution_round: 7\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. differentiation needs rework\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. Han et al. comparison needs expansion.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Han et al. differentiation self-undermining.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2-N2 re-raises Han et al. differentiation as critical.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"R2-W2 re-raises: Schaeffer et al. (2026) and Han et al. (2026) are most direct competing/complementary works but insufficiently discussed. Schaeffer only in Conclusion one sentence; Han only in Related Work one sentence. Both reviewers agree dedicated comparison paragraph needed.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite Han et al., Schaeffer et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM + expand Han et al.\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Rework Han et al. differentiation; add DIF classics\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Add ~0.5 page detailed methodological comparison with Han et al.\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 9, action: \"Add dedicated comparison paragraph for Schaeffer et al. (2026) and Han et al. (2026) in Related Work or Discussion\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Page limit — needs compile verification\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Main content ~8.5 pages. Desk-reject risk.\"}\n    - {round: 6, reviewers: \"R2\", note: \"Cannot confirm page count without compilation.\"}\n    - {round: 7, reviewers: \"\", note: \"Compiled and verified: 8 pages main text. EMNLP 2026 compliant.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised. Section 6 extends to p.9 ~40-55%.\"}\n    - {round: 9, reviewers: \"R2\", note: \"Visual check confirms 8 pages main text ✓. Format compliant.\"}\n  action_items:\n    - {round: 5, action: \"Move ARC IRT to Appendix; compress\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Compile and verify ≤8 pages main content\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Compress Section 6 Discussion\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n  resolution: \"Round 9 visual check confirms 8 pages main text, compliant.\"\n  resolution_round: 9\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"k reserved for benchmark, d for domain. Not re-raised in R8 or R9.\"\n  resolution_round: 7\n  mentions:\n    - {round: 5, reviewers: \"R2\", note: \"k = benchmark in §3.1 but k = stratum in Eq.2.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Use different symbol for strata.\"}\n  action_items:\n    - {round: 5, action: \"Add clarifying note when k meaning changes\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Replace k with different symbol for strata index\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R6-W1\"\n  summary: \"SFT data composition confound — injection replaces or augments general SFT data unclear\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper explicitly states AUGMENT mode. Not re-raised in R8 or R9.\"\n  resolution_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"§4.1 does not specify whether benchmark items replace or augment general SFT corpus.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R6-W2\"\n  summary: \"S4 (Self-Critique) signal computation details insufficient for reproduction\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R2\", note: \"Prompt design, evaluation distribution construction, and scoring mechanism not described.\"}\n    - {round: 8, reviewers: \"\", note: \"Appendix E now provides details.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 6, action: \"Add S4 computation details in appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix E added with S4 details.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported — convergence verification missing\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R1\", note: \"Training convergence is prerequisite for controlled injection validity.\"}\n    - {round: 8, reviewers: \"\", note: \"Appendix F now reports training convergence.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 6, action: \"Report SFT training curves or convergence verification\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix F added with convergence info.\"\n  resolution_round: 8\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"Cross-family GSM8K PPP=0.83 but within-family GSM8K PPP not reported.\"}\n    - {round: 8, reviewers: \"\", note: \"Still not reported.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Still not reported.\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N1\"\n  summary: \"Cross-seed stability claims overstated — n=3 seeds insufficient for taxonomy validation\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"n=3 seeds yields wide CIs; strict sign consistency only 2/5 families.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未直接提及 seed 数量问题，但 R1-W4 和 Table 1 Gemma-2 76.6% stability 间接相关。Paper Limitations now acknowledges seed sensitivity.\"}\n  action_items:\n    - {round: 8, action: \"Increase seeds to n≥5 for ≤3B models; or weaken claims\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Report bootstrap CI covering seed variability explicitly\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N2\"\n  summary: \"DiD null result lacks power analysis — 'causal evidence for global modulation' claim unsupported\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"DiD values range −0.8 to +0.6pp; power to detect ~1pp item-specific effect at n=3 unknown.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Both reviewers re-raise. R1-W2: Section 5.4 title 'No detectable item-specific memorization' misleading; MDES 1.25-2.05pp should be in main text. R2-W3: 'no detectable' ≠ 'does not exist'. Both AGREE: reframe as 'effects below detection threshold'. Consensus achieved.\"}\n  action_items:\n    - {round: 8, action: \"Run post-hoc power analysis reporting MDES\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 8, action: \"Weaken 'causal evidence' to 'no detectable item-specific effect at current power level'\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 9, action: \"Rename Section 5.4 title to audited phrasing (e.g. 'Limited Evidence for Item-Specific Memorization'); report MDES in main text not just appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N3\"\n  summary: \"N=4 model families supporting 4-class taxonomy — generalization evidence insufficient\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"4 patterns observed on 4 families is post-hoc description.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Both re-raise as critical (R1-N3, R2-N2). CONSENSUS: N=4 families producing exactly 4 patterns cannot distinguish genuine taxonomy from idiosyncratic behavior. V-recovery n=1 (R1 corrects R2: actually n=2 counting OLMo-2, but Collapse still n=1). Held-out validation covers only Immune. Paper claims 'each pattern attested in ≥2 families' in §5.1 but Collapse is only Qwen-14B (n=1). Both agree: reposition as 'observed response profiles' or 'preliminary taxonomy', not 'validated taxonomy'.\"}\n  action_items:\n    - {round: 8, action: \"Option A: Add 1-2 more model families\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Option B: Replace 'taxonomy' with 'observed response profiles'\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 9, action: \"Fix factual error in §5.1: 'each taxonomy pattern is attested in at least two independent families' is incorrect for Collapse (only Qwen-14B)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N4\"\n  summary: \"Han et al. (2026) differentiation insufficient — only 2 sentences, no empirical comparison\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Han et al. is most direct prior work. Missing empirical comparison.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"R2-W2 re-raises. Schaeffer et al. also insufficiently discussed. Both AGREE dedicated comparison needed.\"}\n  action_items:\n    - {round: 8, action: \"Add ~0.5 page methodological comparison with Han et al.\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W1\"\n  summary: \"Bayesian and frequentist terminology mixed throughout paper\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Paper uses Bayesian MCMC but 'significant', 'p-value', 'confidence interval' appear in frequentist sense.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Unify terminology\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W2\"\n  summary: \"IRT identifiability simulation uses uniform exposure — mismatch with empirical right-skewed RRF distribution\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Empirical RRF highly right-skewed. Simulation uses uniform.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Re-run identifiability simulation with right-skewed exposure\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-W3\"\n  summary: \"Algorithm 1 threshold sensitivity — only pass/fail grid reported, no continuous sensitivity curve\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R2,R1\", note: \"30/30 pass is too coarse. No sensitivity heatmap.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Both re-raise in context of N1 (formal DR modeling). Algorithm 1's sensitivity test (Appendix P Table 14) only shows pass/fail, not how close each family is to classification boundary. Narrow sensitivity range tested.\"}\n  action_items:\n    - {round: 8, action: \"Add threshold sensitivity heatmap in Appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M1\"\n  summary: \"Missing references — Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Both reviewers flag Yang et al. R2 additionally flags Golchin & Surdeanu and Sainz et al.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Merged into R4-W4 action items.\"}\n  action_items:\n    - {round: 8, action: \"Add Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M2\"\n  summary: \"Minor writing issues — 'pp' undefined, Gemma-2 exclusion abrupt, Figure 1 caption incomplete, Eq.2 computation unclear\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Various minor writing issues.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"R1 minor: Figure 1 y-axis ranges differ, caption should note. Table 2 'Con.' column unclear. Prior distributions not in main text. R2 minor: Figure 1 only seed=42 needs error bars. 'catastrophic collapse' for ≤25pp debatable. holland_1993_dif year mismatch.\"}\n  action_items:\n    - {round: 8, action: \"Fix minor writing issues\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 9, action: \"Add error bars to Figure 1 or note seed=42; clarify Table 2 'Con.' column; add prior distributions to main text; verify holland_1993_dif year\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"AUDIT-1\"\n  summary: \"Figure 1 missing from PDF — referenced in §5.1 but not present\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"audit\", note: \"Figure 1 does not exist in the PDF. Figure numbering starts from Figure 2.\"}\n    - {round: 9, reviewers: \"\", note: \"Resolved. Introduction now includes \\\\begin{figure*} with fig_dose_response.pdf as Figure 1. Visual check confirms Figure 1 present on page 2.\"}\n  action_items:\n    - {round: 8, action: \"Restore or create Figure 1\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Figure 1 (dose-response curves) now present in Introduction. Confirmed by Round 9 visual check.\"\n  resolution_round: 9\n\n# === Round 9 (Fresh Review) New Issues ===\n\n- id: \"R9-N1\"\n  summary: \"Taxonomy based on ad-hoc Algorithm 1 — lacks formal parametric dose-response modeling and classification uncertainty\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"CONSENSUS (R1-N1 Must-Fix + R2-W1→upgraded by R1). Algorithm 1 uses hardcoded thresholds (τ=2pp, n=5, ρ=0.3, λ=0.5pp) for rule-based classification. Pharmacology has mature parametric DR models (Hill equation, 4-parameter log-logistic, sigmoid Emax). Paper borrows 'dose-response' terminology without fitting any DR model. No classification uncertainty quantification. Cannot determine how close a family is to classification boundary. Appendix P (Table 14) sensitivity test only shows pass/fail across 30 threshold combos—too coarse.\"}\n  action_items:\n    - {round: 9, action: \"Fit parametric dose-response models (e.g. 4-param log-logistic) to each family's accuracy-vs-dosage curve; compare with Algorithm 1 via AIC/BIC\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 9, action: \"If parametric fitting infeasible: (a) provide bootstrap classification uncertainty; (b) discuss why Algorithm 1 chosen over standard DR models; (c) cite dose-response literature (Hill 1910, Ritz et al. 2015)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-N2\"\n  summary: \"'Architecture determines vulnerability' causal claim exceeds evidence — confounders uncontrolled\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"CONSENSUS (R1-N2 Must-Fix + R2 AGREE with nuance). Abstract says 'architecture rather than baseline ability determines vulnerability'. Section 6 says 'architecture, not baseline ability alone, determines contamination vulnerability'. Evidence: OLMo-2 vs LLaMA-3.1 (same baseline, different pattern) and Phi-4 vs Qwen-14B (same scale, different pattern). But models differ in pretraining data, tokenizer, training schedule, synthetic data use, data deduplication. Cannot isolate architecture from these confounders. R2 adds: Qwen within-family 14B vs 7B shows different patterns despite same architecture, further undermining architecture-as-cause. R1 suggests weaken to 'family-level factors beyond raw baseline accuracy'. R2 suggests 'family-level factors'.\"}\n  action_items:\n    - {round: 9, action: \"Replace 'architecture determines vulnerability' with 'family-level factors beyond baseline ability' in Abstract, Section 1, Section 6, Conclusion. List uncontrolled confounders (pretraining data, tokenizer, training schedule, synthetic data) in Section 6.\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-S1\"\n  summary: \"Unified LoRA r=16 creates unequal treatment strength across model scales\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"R1-W1 raises, R2 agrees with nuance. LoRA r=16 parameter fraction inversely proportional to model size. Phi-4 14B Immune may partly reflect insufficient LoRA capacity. Partial counter-argument: Qwen-14B (same scale) Collapses, so LoRA capacity alone doesn't explain. But different architectures may have different LoRA efficiency. Undiscussed confound.\"}\n  action_items:\n    - {round: 9, action: \"Discuss LoRA capacity confound in Limitations; ideally test r∈{8,16,32,64} on one family\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-S2\"\n  summary: \"'65-70% MMLU baseline vulnerability band' claim over-precise for n=5 data points\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"R1-W4 raises, R2 partially rebuts. Qualitative observation (moderate baselines more vulnerable) has support. But precise '65-70%' from 5 data points is overfitting. Gemma-2 at ~62% shows Benefit (affected), contradicting 'below vulnerability band shows limited sensitivity'. R2 agrees 65-70% is over-precise but the qualitative direction holds.\"}\n  action_items:\n    - {round: 9, action: \"Replace '65-70% vulnerability band' with qualitative description ('models with moderate baselines appear more vulnerable') in Abstract, Section 5.1, Figure 1 caption\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-S3\"\n  summary: \"Calibration baseline comparison missing IRT variants — cannot isolate γ contribution\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"R2-W4 raises, R1 partially rebuts. Table 4 includes B3 (Vanilla 2PL) which partially addresses this. R1 notes ContamCal IS Bayesian so asking for 'Bayesian calibration baseline' is moot. But systematic 2PL vs 2PL+γ ablation would better isolate γ's marginal contribution. DIVERGENT: R2 says Should-Fix, R1 says Minor at most.\"}\n  action_items:\n    - {round: 9, action: \"Add 2PL vs 2PL+γ ablation in appendix to isolate γ marginal contribution\", assigned_to: \"paper_agent\", status: \"open\"}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form but framing still inconsistent.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Title framing no longer flagged.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D149+ rewrite: Title changed to 'Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families'. Paper repositioned as systematic empirical investigation of dose-response across 5 models (7B-14.7B) from 4 families. No over-scoping.\"\n  resolution_round: 7\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. All claims must be scoped to 'under SFT injection at ≤3B scale'.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Conclusion 'applies directly to settings with larger effects' is unsupported forward claim.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised as Should-Fix. Both agree SFT ecological validity is known limitation.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Re-raised. R2 flags as Must-Fix (critical): LoRA SFT ≠ pretraining contamination, dose-response patterns may be SFT artifacts, Schaeffer et al. (2026) shows different DR under pretraining. R1 downgrades to Should-Fix: controlled injection is only way to get ground truth dosage, paper correctly positions as testbed. DIVERGENT on severity. Consensus: Limitations discussion still too brief (one sentence), needs significant expansion with Schaeffer et al. comparison.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims to 'under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Ensure Abstract first sentence explicitly scopes to SFT injection\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Remove/caveat Conclusion 'applies directly' claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 9, action: \"Expand Limitations SFT vs pretraining discussion significantly; add explicit comparison with Schaeffer et al. (2026) pretraining DR findings\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation has two interpretations.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Both unanimously re-raise as critical. R2 proposes threshold DGP simulation.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。DGP robustness appendix addresses this.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i interaction model\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'under the additive linear specification' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Run threshold DGP simulation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 7, action: \"Write DGP robustness appendix + update Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"400-run threshold DGP simulation completed. Appendix P written. Not re-raised in Round 8 or 9.\"\n  resolution_round: 7\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction + underpowered J\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Bonferroni α=0.00625; CI upper bound likely includes zero.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Social Sciences at 99.1% does not pass Bonferroni.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text §5.4 still presents J=13.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'uncorrected for multiplicity' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text domain γ to J=16 results\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Results §5 reports J=16 for domain γ. P(γ<0)=99.7% at J=16 crosses Bonferroni threshold.\"\n  resolution_round: 7\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations — IRT results unreliable\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at all J.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003. Move ARC IRT to Appendix.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"ARC IRT moved to Appendix.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。ARC IRT in Appendix with PPP caveat.\"}\n    - {round: 9, reviewers: \"R2\", note: \"R2 re-raises: ARC PPP=0.003 should be discussed in main text, not only Appendix. Implications for ARC-based conclusions need explicit treatment in Section 5 or 6.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Move ARC IRT results to Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Clarify ARC IRT parameters are unreliable\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 9, action: \"Add brief discussion of ARC PPP=0.003 implications in main text Section 5 or 6\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality; MAE random control missing\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. No direct RRF vs S1-only ablation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation complete. Downgraded to warning.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Random 300-item subsets report τ but no MAE comparison.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"R1-W1 re-raises RRF calibration verification gap.\"}\n    - {round: 9, reviewers: \"R1\", note: \"R1-W3 re-raises: s_ij classification performance (ROC-AUC, PR) on known contamination labels not reported. Ground truth available from controlled injection but unused for evaluating exposure score quality.\"}\n  action_items:\n    - {round: 3, action: \"Reword C2\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Distinguish exposure variance from signal quality\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Report MAE for random 300-item subsets\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 8, action: \"Report inter-signal rank correlation and leave-one-signal-out ablation\", assigned_to: \"main_agent\", status: \"in_progress\"}\n    - {round: 9, action: \"Report s_ij classification performance (AUC, PR) at each dosage level for treated vs untreated items\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal — over-coverage and under-coverage have different root causes\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Root cause diagnosis still insufficient.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。Root-cause diagnosis now in §5.4.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage to main results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Discuss root causes separately\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Provide explicit root-cause diagnosis\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Root-cause diagnosis in §5.4. Not re-raised in Round 8 or 9.\"\n  resolution_round: 7\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses — J=13 domain finding vs J≥50 standard is self-contradictory\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Most interesting finding uses weakest configuration (J=13).\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text still uses J=13.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。J=16 now in main text.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J prominently in each table\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rerun domain-level γ at J=16\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text to J=16\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Results §5 specifies J=16 for domain γ. Not re-raised in Round 8 or 9.\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Mean a_i comparison shows no discrimination confound. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 may reflect higher average a_i.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised. Resolution confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — caveat adequate but MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Phantom reference to Appendix E.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"MAE CI for cross-family pool not reported.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未直接提及。Cross-family analysis now uses 5 models from 4 families.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Remove phantom Appendix E reference\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rename §5.5 to 'Cross-Family Exploratory Analysis'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Full prior sensitivity complete. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised. Prior sensitivity in Appendix C.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2)\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Conclusion scoped. Hypothesis labeled post-hoc. Not re-raised in R8 or R9.\"\n  resolution_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption but no direct evidence.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must be scoped to 'under SFT injection'.\"}\n    - {round: 6, reviewers: \"\", note: \"Not independently re-raised. Scoped and labeled post-hoc.\"}\n  action_items:\n    - {round: 4, action: \"Reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Scope Conclusion Min-K++ claim to 'at the 0.5B scale under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure — C2 (signal filtering) partially disconnected from main question\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"3 empirical contributions. Not re-raised in R8 or R9.\"\n  resolution_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span too many types.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Now 3 contributions but still span different types.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 reads like method paper contribution.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further consolidate to 2 contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reframe C2 as enabling analysis + standalone practical finding\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — DIF classics + contamination benchmark literature\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. EACL 2026 most direct concurrent work.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"New gaps: Lord, Hambleton, HELM, Magar & Schwartz.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al. needed.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"New missing refs: Golchin & Surdeanu (ICLR 2024), Sainz et al. (EMNLP 2023 Findings), Yang et al. (2023).\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"New missing refs: Hill (1910) and Ritz et al. (2015) dose-response classics; Balloccu et al. (2024) 'Leak, Cheat, Repeat' (EACL 2024); Bordt et al. (2025). Both reviewers agree dose-response literature citation is essential if claiming DR framework.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al., arXiv 2601.04301, Chen et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM, Magar & Schwartz\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Expand Han et al. comparison\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Add Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Add Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 9, action: \"Add dose-response classics: Hill (1910), Ritz et al. (2015); add Balloccu et al. (EACL 2024), Bordt et al. (2025)\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"PPP values filled. Not re-raised since R5.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'.\"}\n    - {round: 5, reviewers: \"\", note: \"PPP values now present. Resolved.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values\", assigned_to: \"main_agent\", status: \"done\"}\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high — still ~6+ quantitative claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Abstract rewritten for dose-response taxonomy paper. Not re-raised in R8 or R9.\"\n  resolution_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"~202 words but still 8-9 numbers.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Still 6+ numbers.\"}\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF; must commit to empirical study positioning\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must position as empirical contribution.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 still reads as method. Reposition around controlled testbed + identifiability.\"}\n    - {round: 8, reviewers: \"R2\", note: \"R2 notes novelty primarily comes from experimental paradigm not methodology.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Paper now positioned as empirical investigation.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al. as concurrent work\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Explicitly state empirical investigation positioning\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reposition Han et al. differentiation; elevate J≥50 identifiability\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Paper committed to empirical investigation. Title signals empirical finding. 3 empirical contributions.\"\n  resolution_round: 7\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. differentiation needs rework\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. Han et al. comparison needs expansion.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Han et al. differentiation self-undermining.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"R2-N2 re-raises Han et al. differentiation as critical.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"R2-W2 re-raises: Schaeffer et al. (2026) and Han et al. (2026) are most direct competing/complementary works but insufficiently discussed. Schaeffer only in Conclusion one sentence; Han only in Related Work one sentence. Both reviewers agree dedicated comparison paragraph needed.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite Han et al., Schaeffer et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM + expand Han et al.\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Rework Han et al. differentiation; add DIF classics\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Add ~0.5 page detailed methodological comparison with Han et al.\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 9, action: \"Add dedicated comparison paragraph for Schaeffer et al. (2026) and Han et al. (2026) in Related Work or Discussion\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Page limit — needs compile verification\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Main content ~8.5 pages. Desk-reject risk.\"}\n    - {round: 6, reviewers: \"R2\", note: \"Cannot confirm page count without compilation.\"}\n    - {round: 7, reviewers: \"\", note: \"Compiled and verified: 8 pages main text. EMNLP 2026 compliant.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised. Section 6 extends to p.9 ~40-55%.\"}\n    - {round: 9, reviewers: \"R2\", note: \"Visual check confirms 8 pages main text ✓. Format compliant.\"}\n  action_items:\n    - {round: 5, action: \"Move ARC IRT to Appendix; compress\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Compile and verify ≤8 pages main content\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 8, action: \"Compress Section 6 Discussion\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n  resolution: \"Round 9 visual check confirms 8 pages main text, compliant.\"\n  resolution_round: 9\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"k reserved for benchmark, d for domain. Not re-raised in R8 or R9.\"\n  resolution_round: 7\n  mentions:\n    - {round: 5, reviewers: \"R2\", note: \"k = benchmark in §3.1 but k = stratum in Eq.2.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Use different symbol for strata.\"}\n  action_items:\n    - {round: 5, action: \"Add clarifying note when k meaning changes\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Replace k with different symbol for strata index\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R6-W1\"\n  summary: \"SFT data composition confound — injection replaces or augments general SFT data unclear\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper explicitly states AUGMENT mode. Not re-raised in R8 or R9.\"\n  resolution_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"§4.1 does not specify whether benchmark items replace or augment general SFT corpus.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R6-W2\"\n  summary: \"S4 (Self-Critique) signal computation details insufficient for reproduction\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R2\", note: \"Prompt design, evaluation distribution construction, and scoring mechanism not described.\"}\n    - {round: 8, reviewers: \"\", note: \"Appendix E now provides details.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 6, action: \"Add S4 computation details in appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix E added with S4 details.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported — convergence verification missing\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 6, reviewers: \"R1\", note: \"Training convergence is prerequisite for controlled injection validity.\"}\n    - {round: 8, reviewers: \"\", note: \"Appendix F now reports training convergence.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 6, action: \"Report SFT training curves or convergence verification\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix F added with convergence info.\"\n  resolution_round: 8\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"Cross-family GSM8K PPP=0.83 but within-family GSM8K PPP not reported.\"}\n    - {round: 8, reviewers: \"\", note: \"Still not reported.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Still not reported.\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N1\"\n  summary: \"Cross-seed stability claims overstated — n=3 seeds insufficient for taxonomy validation\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"n=3 seeds yields wide CIs; strict sign consistency only 2/5 families.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未直接提及 seed 数量问题，但 R1-W4 和 Table 1 Gemma-2 76.6% stability 间接相关。Paper Limitations now acknowledges seed sensitivity.\"}\n  action_items:\n    - {round: 8, action: \"Increase seeds to n≥5 for ≤3B models; or weaken claims\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Report bootstrap CI covering seed variability explicitly\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N2\"\n  summary: \"DiD null result lacks power analysis — 'causal evidence for global modulation' claim unsupported\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"DiD values range −0.8 to +0.6pp; power to detect ~1pp item-specific effect at n=3 unknown.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Both reviewers re-raise. R1-W2: Section 5.4 title 'No detectable item-specific memorization' misleading; MDES 1.25-2.05pp should be in main text. R2-W3: 'no detectable' ≠ 'does not exist'. Both AGREE: reframe as 'effects below detection threshold'. Consensus achieved.\"}\n  action_items:\n    - {round: 8, action: \"Run post-hoc power analysis reporting MDES\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 8, action: \"Weaken 'causal evidence' to 'no detectable item-specific effect at current power level'\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 9, action: \"Rename Section 5.4 title to audited phrasing (e.g. 'Limited Evidence for Item-Specific Memorization'); report MDES in main text not just appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N3\"\n  summary: \"N=4 model families supporting 4-class taxonomy — generalization evidence insufficient\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"4 patterns observed on 4 families is post-hoc description.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Both re-raise as critical (R1-N3, R2-N2). CONSENSUS: N=4 families producing exactly 4 patterns cannot distinguish genuine taxonomy from idiosyncratic behavior. V-recovery n=1 (R1 corrects R2: actually n=2 counting OLMo-2, but Collapse still n=1). Held-out validation covers only Immune. Paper claims 'each pattern attested in ≥2 families' in §5.1 but Collapse is only Qwen-14B (n=1). Both agree: reposition as 'observed response profiles' or 'preliminary taxonomy', not 'validated taxonomy'.\"}\n  action_items:\n    - {round: 8, action: \"Option A: Add 1-2 more model families\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 8, action: \"Option B: Replace 'taxonomy' with 'observed response profiles'\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 9, action: \"Fix factual error in §5.1: 'each taxonomy pattern is attested in at least two independent families' is incorrect for Collapse (only Qwen-14B)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N4\"\n  summary: \"Han et al. (2026) differentiation insufficient — only 2 sentences, no empirical comparison\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Han et al. is most direct prior work. Missing empirical comparison.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"R2-W2 re-raises. Schaeffer et al. also insufficiently discussed. Both AGREE dedicated comparison needed.\"}\n  action_items:\n    - {round: 8, action: \"Add ~0.5 page methodological comparison with Han et al.\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W1\"\n  summary: \"Bayesian and frequentist terminology mixed throughout paper\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Paper uses Bayesian MCMC but 'significant', 'p-value', 'confidence interval' appear in frequentist sense.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Unify terminology\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W2\"\n  summary: \"IRT identifiability simulation uses uniform exposure — mismatch with empirical right-skewed RRF distribution\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Empirical RRF highly right-skewed. Simulation uses uniform.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Re-run identifiability simulation with right-skewed exposure\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-W3\"\n  summary: \"Algorithm 1 threshold sensitivity — only pass/fail grid reported, no continuous sensitivity curve\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R2,R1\", note: \"30/30 pass is too coarse. No sensitivity heatmap.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Both re-raise in context of N1 (formal DR modeling). Algorithm 1's sensitivity test (Appendix P Table 14) only shows pass/fail, not how close each family is to classification boundary. Narrow sensitivity range tested.\"}\n  action_items:\n    - {round: 8, action: \"Add threshold sensitivity heatmap in Appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M1\"\n  summary: \"Missing references — Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Both reviewers flag Yang et al. R2 additionally flags Golchin & Surdeanu and Sainz et al.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Merged into R4-W4 action items.\"}\n  action_items:\n    - {round: 8, action: \"Add Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M2\"\n  summary: \"Minor writing issues — 'pp' undefined, Gemma-2 exclusion abrupt, Figure 1 caption incomplete, Eq.2 computation unclear\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Various minor writing issues.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"R1 minor: Figure 1 y-axis ranges differ, caption should note. Table 2 'Con.' column unclear. Prior distributions not in main text. R2 minor: Figure 1 only seed=42 needs error bars. 'catastrophic collapse' for ≤25pp debatable. holland_1993_dif year mismatch.\"}\n  action_items:\n    - {round: 8, action: \"Fix minor writing issues\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 9, action: \"Add error bars to Figure 1 or note seed=42; clarify Table 2 'Con.' column; add prior distributions to main text; verify holland_1993_dif year\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"AUDIT-1\"\n  summary: \"Figure 1 missing from PDF — referenced in §5.1 but not present\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - {round: 8, reviewers: \"audit\", note: \"Figure 1 does not exist in the PDF. Figure numbering starts from Figure 2.\"}\n    - {round: 9, reviewers: \"\", note: \"Resolved. Introduction now includes \\\\begin{figure*} with fig_dose_response.pdf as Figure 1. Visual check confirms Figure 1 present on page 2.\"}\n  action_items:\n    - {round: 8, action: \"Restore or create Figure 1\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Figure 1 (dose-response curves) now present in Introduction. Confirmed by Round 9 visual check.\"\n  resolution_round: 9\n\n# === Round 9 (Fresh Review) New Issues ===\n\n- id: \"R9-N1\"\n  summary: \"Taxonomy based on ad-hoc Algorithm 1 — lacks formal parametric dose-response modeling and classification uncertainty\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"CONSENSUS (R1-N1 Must-Fix + R2-W1→upgraded by R1). Algorithm 1 uses hardcoded thresholds (τ=2pp, n=5, ρ=0.3, λ=0.5pp) for rule-based classification. Pharmacology has mature parametric DR models (Hill equation, 4-parameter log-logistic, sigmoid Emax). Paper borrows 'dose-response' terminology without fitting any DR model. No classification uncertainty quantification. Cannot determine how close a family is to classification boundary. Appendix P (Table 14) sensitivity test only shows pass/fail across 30 threshold combos—too coarse.\"}\n  action_items:\n    - {round: 9, action: \"Fit parametric dose-response models (e.g. 4-param log-logistic) to each family's accuracy-vs-dosage curve; compare with Algorithm 1 via AIC/BIC\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 9, action: \"If parametric fitting infeasible: (a) provide bootstrap classification uncertainty; (b) discuss why Algorithm 1 chosen over standard DR models; (c) cite dose-response literature (Hill 1910, Ritz et al. 2015)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-N2\"\n  summary: \"'Architecture determines vulnerability' causal claim exceeds evidence — confounders uncontrolled\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"CONSENSUS (R1-N2 Must-Fix + R2 AGREE with nuance). Abstract says 'architecture rather than baseline ability determines vulnerability'. Section 6 says 'architecture, not baseline ability alone, determines contamination vulnerability'. Evidence: OLMo-2 vs LLaMA-3.1 (same baseline, different pattern) and Phi-4 vs Qwen-14B (same scale, different pattern). But models differ in pretraining data, tokenizer, training schedule, synthetic data use, data deduplication. Cannot isolate architecture from these confounders. R2 adds: Qwen within-family 14B vs 7B shows different patterns despite same architecture, further undermining architecture-as-cause. R1 suggests weaken to 'family-level factors beyond raw baseline accuracy'. R2 suggests 'family-level factors'.\"}\n  action_items:\n    - {round: 9, action: \"Replace 'architecture determines vulnerability' with 'family-level factors beyond baseline ability' in Abstract, Section 1, Section 6, Conclusion. List uncontrolled confounders (pretraining data, tokenizer, training schedule, synthetic data) in Section 6.\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-S1\"\n  summary: \"Unified LoRA r=16 creates unequal treatment strength across model scales\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"R1-W1 raises, R2 agrees with nuance. LoRA r=16 parameter fraction inversely proportional to model size. Phi-4 14B Immune may partly reflect insufficient LoRA capacity. Partial counter-argument: Qwen-14B (same scale) Collapses, so LoRA capacity alone doesn't explain. But different architectures may have different LoRA efficiency. Undiscussed confound.\"}\n  action_items:\n    - {round: 9, action: \"Discuss LoRA capacity confound in Limitations; ideally test r∈{8,16,32,64} on one family\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-S2\"\n  summary: \"'65-70% MMLU baseline vulnerability band' claim over-precise for n=5 data points\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"R1-W4 raises, R2 partially rebuts. Qualitative observation (moderate baselines more vulnerable) has support. But precise '65-70%' from 5 data points is overfitting. Gemma-2 at ~62% shows Benefit (affected), contradicting 'below vulnerability band shows limited sensitivity'. R2 agrees 65-70% is over-precise but the qualitative direction holds.\"}\n  action_items:\n    - {round: 9, action: \"Replace '65-70% vulnerability band' with qualitative description ('models with moderate baselines appear more vulnerable') in Abstract, Section 5.1, Figure 1 caption\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-S3\"\n  summary: \"Calibration baseline comparison missing IRT variants — cannot isolate γ contribution\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"R2-W4 raises, R1 partially rebuts. Table 4 includes B3 (Vanilla 2PL) which partially addresses this. R1 notes ContamCal IS Bayesian so asking for 'Bayesian calibration baseline' is moot. But systematic 2PL vs 2PL+γ ablation would better isolate γ's marginal contribution. DIVERGENT: R2 says Should-Fix, R1 says Minor at most.\"}\n  action_items:\n    - {round: 9, action: \"Add 2PL vs 2PL+γ ablation in appendix to isolate γ marginal contribution\", assigned_to: \"paper_agent\", status: \"open\"}"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-21T16:13:18.326588+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml\", \"bytes\": 40933}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-21T16:15:32.478558+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 9 (Fresh Review)\n\n**论文**: \"Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计; R2: 新颖性+相关工作+写作+格式）\n**审稿模式**: Fresh（重新审稿，无前轮记忆）\n\n---\n\n## Summary\n\n论文通过 LoRA SFT 控制注入，以 5 个剂量水平向 4 个独立家族的 5 个模型（7B–14.7B）注入基准题目，发现污染并非一律导致分数膨胀，而是产生四种定性不同的 dose-response 模式（Immune/Collapse/V-Recovery/Benefit）。论文使用 ContamCal（RRF 多信号融合 + 2PL+γ IRT）量化污染效应并提供校准置信区间，DiD 分析未发现 item-specific memorization，跨 benchmark 迁移分析揭示方向性反转现象。\n\n---\n\n## Strengths\n\n1. **研究问题精准且有实际价值**：现有文献几乎全做二元（有/无污染）比较，本文首次系统建模连续 dose-response 关系，填补了重要方法论空白。[R1,R2 共识]\n\n2. **实验设计严谨**：控制 SFT 注入（已知 ground truth dosage）+ 4 家族 × 5 剂量 × 3 benchmark × 多 seed 的 factorial design + held-out 家族验证 + 跨 benchmark 迁移——这是为数不多遵循实验因果推断范式的 LLM 评估研究。[R1,R2 共识]\n\n3. **IRT 框架技术实施扎实**：贝叶斯推断流程规范（R̂ < 1.01, ESS > 500, PPP 报告），收敛诊断充分，4 chains NUTS/HMC in Stan。提供校准的可信区间，对实践者有用。[R1,R2 共识]\n\n4. **诚实报告零结果和局限**：DiD 非显著、ARC 功效不足、cross-seed CI 宽度、OLMo-2 种子敏感性均如实报告，无选择性呈现。[R1,R2 共识]\n\n5. **附录极为详尽**：涵盖收敛诊断、功效分析、阈值鲁棒性、domain 分解、4PL 扩展等，达到高标准的可复现性（Reproducibility 4/5）。[R1,R2 共识]\n\n6. **跨 benchmark 迁移分析有深度**：GSM8K 方向反转发现（Qwen-7B MMLU −1.8pp 但 GSM8K +10.1pp）和三种迁移模式（null/consistent/directional reversal）提供了超越单一 benchmark 的见解。[R1,R2 共识]\n\n---\n\n## Weaknesses（按严重程度排列）\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, CONSENSUS] **分类法基于 ad-hoc 算法，缺乏正式 dose-response 建模**\n- Algorithm 1 使用硬编码阈值（τ=2pp, n=5, ρ=0.3, λ=0.5pp）做规则分类，本质是描述性归纳。药理学有成熟的参数化 DR 模型（Hill 方程、4 参数 log-logistic、sigmoid Emax），可通过 AIC/BIC 做模型选择且自然提供分类不确定性。论文借用 \"dose-response\" 术语却未使用该领域的标准工具。Appendix P 的阈值鲁棒性测试（30 组 pass/fail）过于粗糙——无法判断某家族距分类边界多远。\n- **位置**: Section 3.3, Algorithm 1 (p.5), Appendix P\n- **建议**: (1) 拟合参数化 DR 模型并与 Algorithm 1 对比; (2) 至少提供 bootstrap 分类不确定性; (3) 引用 dose-response 经典文献\n\n**MF2** [critical, CONSENSUS] **\"架构决定脆弱性\"因果声称超出证据**\n- Abstract/Section 6/Conclusion 多处声称 \"architecture rather than baseline ability determines vulnerability\"。实际证据仅为：不同家族在相似 baseline 下表现不同（OLMo-2 vs LLaMA-3.1）。但\"架构\"之外存在大量未控制混淆：预训练数据分布与规模、tokenizer 覆盖率、合成数据策略（Phi-4）、训练步数与调度。R2 指出 Qwen 内部同架构不同规模（14B Collapse vs 7B V-Recovery）进一步削弱\"架构决定\"的叙事。数据能支撑的结论是\"baseline ability alone does not determine vulnerability\"，不是\"architecture determines\"。\n- **位置**: Abstract, Section 1 C1, Section 5.1 ¶out-of-sample, Section 6 ¶1\n- **建议**: 将 \"architecture determines\" 弱化为 \"family-level factors beyond baseline ability\"; 在 Section 6 列出未控制的混淆因素\n\n**MF3** [critical, CONSENSUS] **N=4 家族对分类法泛化性的根本限制**\n- 4 类模式恰好由 4 个家族产生：Immune (Phi-4), Collapse (Qwen-14B), V-Recovery (Qwen-7B), Benefit (OLMo-2/Gemma-2)。Collapse 和 V-Recovery 各仅 1 个家族代表。Held-out 验证仅覆盖 Immune。**§5.1 声称\"each taxonomy pattern is attested in at least two independent families\"与 Collapse 仅 Qwen-14B 的事实不符**——这是一个需要修正的事实错误。N=4 无法区分\"4 种真实类型\"和\"每个家族有 idiosyncratic 行为\"。规模范围 ≤14B，70B+ 模型的适用性完全未知。\n- **位置**: Section 4.1, Section 5.1, Table 1\n- **建议**: 将分类法定位为 \"observed response profiles\" / \"preliminary taxonomy\"; 修正 §5.1 的事实错误; 明确讨论 N=4 的泛化风险\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, DIVERGENT — R2: Must-Fix, R1: Should-Fix] **LoRA SFT 注入的生态效度**\n- 真实污染发生在预训练阶段（web crawl 泄露），与 LoRA SFT 注入在学习机制上截然不同。Limitations 仅一句话提及。Schaeffer et al. (2026) 展示了预训练污染下不同的 DR 关系，论文与其对比不充分。R1 反驳：控制实验需要已知 ground truth dosage，LoRA SFT 是目前唯一可控实验范式，paper 正确定位为 testbed。**共识：不否定论文贡献，但 Limitations 讨论需大幅扩展**。\n- **建议**: 扩展 Limitations 中 SFT vs. pretraining 讨论; 与 Schaeffer et al. 做显式对比\n\n**SF2** [warning, CONSENSUS] **DID 零效应过度解读**\n- Section 5.4 标题 \"No detectable item-specific memorization\" 易被误读为\"不存在 memorization\"。Appendix N MDES 1.25–2.05pp 表明 ≤1.25pp 的效应无法排除。Contribution 2 使用同样过度确定的措辞。\n- **建议**: Section 5.4 标题改为 \"Limited Evidence for Item-Specific Memorization\"; 正文报告 MDES 数值\n\n**SF3** [warning, CONSENSUS] **LoRA r=16 统一配置的未讨论混淆**\n- LoRA 相对表达能力与模型参数量成反比。Phi-4 14B Immune 可能部分源于 LoRA 容量不足。R2 反驳：Qwen-14B 同为 14B 却 Collapse，但两者架构效率不同。\n- **建议**: 在 Limitations 讨论 LoRA 容量混淆; 理想情况测试 r∈{8,16,32,64}\n\n**SF4** [warning, CONSENSUS] **曝光分数 s_ij 分类性能未报告**\n- s_ij 作为核心协变量进入 IRT 模型，测量误差直接传递到 γ 估计。Ground truth 可得（控制注入已知 item membership），但未报告 s_ij 的 ROC-AUC、PR 曲线。\n- **建议**: 补充 s_ij 在各 dosage 下区分 treated vs. untreated items 的分类性能\n\n**SF5** [warning, CONSENSUS] **\"65–70% MMLU 基线脆弱带\"过于精确**\n- 5 个数据点不支撑精确百分比区间。Gemma-2 在 ~62% 显示 Benefit（明显受影响），与\"below band shows limited sensitivity\"矛盾。\n- **建议**: 弱化为定性描述 (\"models with moderate baselines appear more vulnerable\")\n\n**SF6** [warning, CONSENSUS] **Schaeffer et al. (2026) 和 Han et al. (2026) 讨论不充分**\n- 两篇最直接的竞争/互补工作：Schaeffer et al. 做预训练污染 DR，Han et al. 用 group-based DIF 量化污染。前者仅在 Conclusion 一句话提及，后者在 Related Work 一句。\n- **建议**: 在 Related Work 用专段对比两篇工作的方法论差异\n\n---\n\n## Reviewer Consensus（[AGREE] 标记）\n\n两位 Reviewer 在以下问题上完全一致：\n1. **[AGREE]** N=4 家族泛化性不足是核心问题（MF3）\n2. **[AGREE]** 因果声称\"架构决定脆弱性\"需降级为描述性发现（MF2）\n3. **[AGREE]** DID 零效应需更审慎表述（SF2）\n4. **[AGREE]** 正式 dose-response 建模或分类不确定性度量缺失（MF1）——R1 列为 Must-Fix，R2 初列 Should-Fix 后同意升级\n5. **[AGREE]** 实验设计严谨、IRT 方法论扎实是明确优势\n6. **[AGREE]** 附录质量高，可复现性好\n\n## Reviewer Divergence（[REBUT] 标记）\n\n1. **LoRA SFT 生态效度的严重性** — R2 视为 Must-Fix（\"根本性不足\"），R1 视为 Should-Fix（\"可控实验的合理起点，加强讨论即可缓解\"）。R1 提出关键反驳：预训练污染无法精确控制 dosage，LoRA SFT 是目前唯一可控实验范式。**Director 判断**：R1 论证更有说服力——作为首个系统 DR 研究，选择可控条件是合理的，但 Limitations 讨论确实需要大幅扩展。列为 Should-Fix。\n\n2. **Calibration 基线强度** — R2 认为 Table 4 基线偏弱（Should-Fix），R1 认为基本合理（Minor）。R1 指出 ContamCal 本身即贝叶斯方法，要求\"Bayesian calibration baseline\"无意义；B3 (Vanilla 2PL) 已部分满足 IRT 变体对比。**Director 判断**：列为 Info，建议在附录补充 2PL vs. 2PL+γ ablation。\n\n---\n\n## Questions（需要作者澄清）\n\nQ1: γ 参数的识别来源——主要从 within-model cross-item 的 s_ij 变异中识别，还是从 cross-dosage 的 s_ij 分布差异中识别？θ 和 γ 的分离依赖什么排除限制？[R1]\n\nQ2: Algorithm 1 对输入噪声的敏感性——如果在每个 dosage 下 accuracy 加 ±1pp 均匀噪声，有多少家族的分类会变化？[R1]\n\nQ3: Phi-4 的 Immune 是否更可能源于其大量使用合成数据的预训练策略，而非架构本身？[R1]\n\nQ4: 将 LoRA rank 从 16 提升到 64（增加记忆容量），Phi-4 分类是否可能变化？[R1]\n\n---\n\n## Missing References\n\n1. **Hill (1910)** — dose-response 建模奠基文献 [R1,R2]\n2. **Ritz et al. (2015)** — `drc` R 包，4 参数 log-logistic 等标准 DR 模型 [R1,R2]\n3. **Balloccu et al. (2024)** \"Leak, Cheat, Repeat\" (EACL 2024) — contamination 影响评估 [R2]\n4. **Bordt et al. (2025)** \"How Much Can We Forget about Data Contamination?\" [R2, 需确认发表状态]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，跳过。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（耗时约 3 分钟）\n\n**3 个 Warning**:\n1. **Algorithm 1 跨页 (pp.4-5)**：伪代码 ~29 行从 Page 4 延续到 Page 5，需翻页阅读。建议压缩至单页或调整 float 位置。\n2. **Figure 2 尺寸偏小 (p.8)**：DID 置信区间图压缩在约 1/4 栏宽，数据点和误差线在正常阅读距离下难以辨认。建议放大至半栏宽或用 figure* 全宽。\n3. **Method 段视觉节奏单调 (pp.3-5)**：连续 3 页纯文本+公式，无 figure/table。建议增加 pipeline 示意图。\n\n**9 个 Info**:\n- Figure 1 图例字号偏小（≥9pt 建议）\n- Figure 4 色阶建议确认色盲安全 colormap\n- Figure 5 数字标注字号过小（~6-7pt）\n- Page 13 display item 密度过高\n- Table 1 排版规范 ✓\n- Tables 2-3 格式规范 ✓\n- Limitations 段简短、符合 EMNLP 要求 ✓\n- 主正文 8 页 ✓ 符合 EMNLP 2026 限制\n- 参考文献格式一致 ✓\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — **Borderline Conference**\n**置信度**: 4/5（两位 Reviewer 均熟悉 IRT、LLM 评估和数据污染领域）\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3/5 | 3.25/5 |\n| Excitement | 3.5/5 | 3.5/5 | 3.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n\n**判断依据**：\n- 研究问题重要、实验设计严谨、IRT 框架实施扎实——这些是明确的 Conference 级优势\n- 三个 Must-Fix 问题（分类法缺乏统计基础、因果声称过强、N=4 泛化性不足）是阻碍 Conference 接收的主要障碍\n- 关键在于：三个 Must-Fix **主要通过文本修订可解决**（弱化声称、补充讨论、添加不确定性度量），不需要推翻论文架构或重做实验\n- 如果三个 Must-Fix 和主要 Should-Fix 得到充分处理，论文具备 3.5→4.0 (Conference) 的提升潜力\n- 若仅部分修复，3.0 (Findings) 是合理的 fallback\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过度声称 \"architecture rather than baseline ability determines vulnerability\"——应弱化为描述性发现\n- \"65–70% MMLU baseline band\" 从 5 个数据点无法支撑如此精确的区间\n- \"No detectable item-specific memorization\" 应标注 MDES\n\n### Introduction (Section 1)\n- 动机清晰，问题定义精准\n- Contribution 1 中 \"confirms generalizability\" 对于 N=1 held-out 验证过度\n- Contribution 2 \"No detectable\" 需加 \"at current power level\" 限定\n\n### Related Work (Section 2)\n- 缺少与 Schaeffer et al. (2026) 和 Han et al. (2026) 的专段对比\n- 缺少 dose-response 建模经典文献引用\n- 缺少 Balloccu et al. (2024), Bordt et al. (2025)\n\n### Method (Section 3)\n- 2PL+γ 模型设定合理，但先验分布应在正文给出（至少 θ 和 γ 的先验形式）\n- Algorithm 1 缺乏统计基础——建议增加参数化 DR 模型或分类不确定性\n- RRF 融合的 exposure score 分类性能未评估\n\n### Experimental Setup (Section 4)\n- 统一 LoRA r=16 的混淆需讨论\n- SFT AUGMENT 模式说明清晰 ✓\n\n### Results (Section 5)\n- Table 1 呈现清晰 ✓\n- §5.1 \"each taxonomy pattern attested in ≥2 families\" 对 Collapse 不成立——**事实错误**\n- §5.4 标题需改为更审慎措辞; MDES 应在正文报告\n- ARC PPP=0.003 应在主文讨论，不仅放附录\n- Figure 1 仅 seed=42，建议加 error bars\n\n### Discussion/Conclusion (Section 6)\n- \"architecture, not baseline ability alone, determines contamination vulnerability\"——因果声称需降级\n- 与 Schaeffer et al. 的对比仅一句话，需扩展\n\n### Limitations\n- 覆盖 3 个点（model scale, seed sensitivity, LoRA vs pretraining），结构合理\n- SFT vs pretraining 讨论需大幅扩展（当前一句话）\n- 应增加 LoRA 容量混淆讨论\n- 应增加 instruction tuning vs continued pretraining 路径差异讨论\n\n### Format\n- ✅ 正文 8 页，符合 EMNLP 2026 Long paper 限制\n- ✅ ACL review 模板\n- ✅ Limitations 章节存在\n- ✅ Ethics Statement 存在\n- ✅ 匿名性完整\n- ✅ 参考文献格式基本规范（minor year mismatches 需核查）",
  "project": "contamcal-irt-calibration",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 9 (Fresh Review)\n\n**论文**: \"Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计; R2: 新颖性+相关工作+写作+格式）\n**审稿模式**: Fresh（重新审稿，无前轮记忆）\n\n---\n\n## Summary\n\n论文通过 LoRA SFT 控制注入，以 5 个剂量水平向 4 个独立家族的 5 个模型（7B–14.7B）注入基准题目，发现污染并非一律导致分数膨胀，而是产生四种定性不同的 dose-response 模式（Immune/Collapse/V-Recovery/Benefit）。论文使用 ContamCal（RRF 多信号融合 + 2PL+γ IRT）量化污染效应并提供校准置信区间，DiD 分析未发现 item-specific memorization，跨 benchmark 迁移分析揭示方向性反转现象。\n\n---\n\n## Strengths\n\n1. **研究问题精准且有实际价值**：现有文献几乎全做二元（有/无污染）比较，本文首次系统建模连续 dose-response 关系，填补了重要方法论空白。[R1,R2 共识]\n\n2. **实验设计严谨**：控制 SFT 注入（已知 ground truth dosage）+ 4 家族 × 5 剂量 × 3 benchmark × 多 seed 的 factorial design + held-out 家族验证 + 跨 benchmark 迁移——这是为数不多遵循实验因果推断范式的 LLM 评估研究。[R1,R2 共识]\n\n3. **IRT 框架技术实施扎实**：贝叶斯推断流程规范（R̂ < 1.01, ESS > 500, PPP 报告），收敛诊断充分，4 chains NUTS/HMC in Stan。提供校准的可信区间，对实践者有用。[R1,R2 共识]\n\n4. **诚实报告零结果和局限**：DiD 非显著、ARC 功效不足、cross-seed CI 宽度、OLMo-2 种子敏感性均如实报告，无选择性呈现。[R1,R2 共识]\n\n5. **附录极为详尽**：涵盖收敛诊断、功效分析、阈值鲁棒性、domain 分解、4PL 扩展等，达到高标准的可复现性（Reproducibility 4/5）。[R1,R2 共识]\n\n6. **跨 benchmark 迁移分析有深度**：GSM8K 方向反转发现（Qwen-7B MMLU −1.8pp 但 GSM8K +10.1pp）和三种迁移模式（null/consistent/directional reversal）提供了超越单一 benchmark 的见解。[R1,R2 共识]\n\n---\n\n## Weaknesses（按严重程度排列）\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, CONSENSUS] **分类法基于 ad-hoc 算法，缺乏正式 dose-response 建模**\n- Algorithm 1 使用硬编码阈值（τ=2pp, n=5, ρ=0.3, λ=0.5pp）做规则分类，本质是描述性归纳。药理学有成熟的参数化 DR 模型（Hill 方程、4 参数 log-logistic、sigmoid Emax），可通过 AIC/BIC 做模型选择且自然提供分类不确定性。论文借用 \"dose-response\" 术语却未使用该领域的标准工具。Appendix P 的阈值鲁棒性测试（30 组 pass/fail）过于粗糙——无法判断某家族距分类边界多远。\n- **位置**: Section 3.3, Algorithm 1 (p.5), Appendix P\n- **建议**: (1) 拟合参数化 DR 模型并与 Algorithm 1 对比; (2) 至少提供 bootstrap 分类不确定性; (3) 引用 dose-response 经典文献\n\n**MF2** [critical, CONSENSUS] **\"架构决定脆弱性\"因果声称超出证据**\n- Abstract/Section 6/Conclusion 多处声称 \"architecture rather than baseline ability determines vulnerability\"。实际证据仅为：不同家族在相似 baseline 下表现不同（OLMo-2 vs LLaMA-3.1）。但\"架构\"之外存在大量未控制混淆：预训练数据分布与规模、tokenizer 覆盖率、合成数据策略（Phi-4）、训练步数与调度。R2 指出 Qwen 内部同架构不同规模（14B Collapse vs 7B V-Recovery）进一步削弱\"架构决定\"的叙事。数据能支撑的结论是\"baseline ability alone does not determine vulnerability\"，不是\"architecture determines\"。\n- **位置**: Abstract, Section 1 C1, Section 5.1 ¶out-of-sample, Section 6 ¶1\n- **建议**: 将 \"architecture determines\" 弱化为 \"family-level factors beyond baseline ability\"; 在 Section 6 列出未控制的混淆因素\n\n**MF3** [critical, CONSENSUS] **N=4 家族对分类法泛化性的根本限制**\n- 4 类模式恰好由 4 个家族产生：Immune (Phi-4), Collapse (Qwen-14B), V-Recovery (Qwen-7B), Benefit (OLMo-2/Gemma-2)。Collapse 和 V-Recovery 各仅 1 个家族代表。Held-out 验证仅覆盖 Immune。**§5.1 声称\"each taxonomy pattern is attested in at least two independent families\"与 Collapse 仅 Qwen-14B 的事实不符**——这是一个需要修正的事实错误。N=4 无法区分\"4 种真实类型\"和\"每个家族有 idiosyncratic 行为\"。规模范围 ≤14B，70B+ 模型的适用性完全未知。\n- **位置**: Section 4.1, Section 5.1, Table 1\n- **建议**: 将分类法定位为 \"observed response profiles\" / \"preliminary taxonomy\"; 修正 §5.1 的事实错误; 明确讨论 N=4 的泛化风险\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, DIVERGENT — R2: Must-Fix, R1: Should-Fix] **LoRA SFT 注入的生态效度**\n- 真实污染发生在预训练阶段（web crawl 泄露），与 LoRA SFT 注入在学习机制上截然不同。Limitations 仅一句话提及。Schaeffer et al. (2026) 展示了预训练污染下不同的 DR 关系，论文与其对比不充分。R1 反驳：控制实验需要已知 ground truth dosage，LoRA SFT 是目前唯一可控实验范式，paper 正确定位为 testbed。**共识：不否定论文贡献，但 Limitations 讨论需大幅扩展**。\n- **建议**: 扩展 Limitations 中 SFT vs. pretraining 讨论; 与 Schaeffer et al. 做显式对比\n\n**SF2** [warning, CONSENSUS] **DID 零效应过度解读**\n- Section 5.4 标题 \"No detectable item-specific memorization\" 易被误读为\"不存在 memorization\"。Appendix N MDES 1.25–2.05pp 表明 ≤1.25pp 的效应无法排除。Contribution 2 使用同样过度确定的措辞。\n- **建议**: Section 5.4 标题改为 \"Limited Evidence for Item-Specific Memorization\"; 正文报告 MDES 数值\n\n**SF3** [warning, CONSENSUS] **LoRA r=16 统一配置的未讨论混淆**\n- LoRA 相对表达能力与模型参数量成反比。Phi-4 14B Immune 可能部分源于 LoRA 容量不足。R2 反驳：Qwen-14B 同为 14B 却 Collapse，但两者架构效率不同。\n- **建议**: 在 Limitations 讨论 LoRA 容量混淆; 理想情况测试 r∈{8,16,32,64}\n\n**SF4** [warning, CONSENSUS] **曝光分数 s_ij 分类性能未报告**\n- s_ij 作为核心协变量进入 IRT 模型，测量误差直接传递到 γ 估计。Ground truth 可得（控制注入已知 item membership），但未报告 s_ij 的 ROC-AUC、PR 曲线。\n- **建议**: 补充 s_ij 在各 dosage 下区分 treated vs. untreated items 的分类性能\n\n**SF5** [warning, CONSENSUS] **\"65–70% MMLU 基线脆弱带\"过于精确**\n- 5 个数据点不支撑精确百分比区间。Gemma-2 在 ~62% 显示 Benefit（明显受影响），与\"below band shows limited sensitivity\"矛盾。\n- **建议**: 弱化为定性描述 (\"models with moderate baselines appear more vulnerable\")\n\n**SF6** [warning, CONSENSUS] **Schaeffer et al. (2026) 和 Han et al. (2026) 讨论不充分**\n- 两篇最直接的竞争/互补工作：Schaeffer et al. 做预训练污染 DR，Han et al. 用 group-based DIF 量化污染。前者仅在 Conclusion 一句话提及，后者在 Related Work 一句。\n- **建议**: 在 Related Work 用专段对比两篇工作的方法论差异\n\n---\n\n## Reviewer Consensus（[AGREE] 标记）\n\n两位 Reviewer 在以下问题上完全一致：\n1. **[AGREE]** N=4 家族泛化性不足是核心问题（MF3）\n2. **[AGREE]** 因果声称\"架构决定脆弱性\"需降级为描述性发现（MF2）\n3. **[AGREE]** DID 零效应需更审慎表述（SF2）\n4. **[AGREE]** 正式 dose-response 建模或分类不确定性度量缺失（MF1）——R1 列为 Must-Fix，R2 初列 Should-Fix 后同意升级\n5. **[AGREE]** 实验设计严谨、IRT 方法论扎实是明确优势\n6. **[AGREE]** 附录质量高，可复现性好\n\n## Reviewer Divergence（[REBUT] 标记）\n\n1. **LoRA SFT 生态效度的严重性** — R2 视为 Must-Fix（\"根本性不足\"），R1 视为 Should-Fix（\"可控实验的合理起点，加强讨论即可缓解\"）。R1 提出关键反驳：预训练污染无法精确控制 dosage，LoRA SFT 是目前唯一可控实验范式。**Director 判断**：R1 论证更有说服力——作为首个系统 DR 研究，选择可控条件是合理的，但 Limitations 讨论确实需要大幅扩展。列为 Should-Fix。\n\n2. **Calibration 基线强度** — R2 认为 Table 4 基线偏弱（Should-Fix），R1 认为基本合理（Minor）。R1 指出 ContamCal 本身即贝叶斯方法，要求\"Bayesian calibration baseline\"无意义；B3 (Vanilla 2PL) 已部分满足 IRT 变体对比。**Director 判断**：列为 Info，建议在附录补充 2PL vs. 2PL+γ ablation。\n\n---\n\n## Questions（需要作者澄清）\n\nQ1: γ 参数的识别来源——主要从 within-model cross-item 的 s_ij 变异中识别，还是从 cross-dosage 的 s_ij 分布差异中识别？θ 和 γ 的分离依赖什么排除限制？[R1]\n\nQ2: Algorithm 1 对输入噪声的敏感性——如果在每个 dosage 下 accuracy 加 ±1pp 均匀噪声，有多少家族的分类会变化？[R1]\n\nQ3: Phi-4 的 Immune 是否更可能源于其大量使用合成数据的预训练策略，而非架构本身？[R1]\n\nQ4: 将 LoRA rank 从 16 提升到 64（增加记忆容量），Phi-4 分类是否可能变化？[R1]\n\n---\n\n## Missing References\n\n1. **Hill (1910)** — dose-response 建模奠基文献 [R1,R2]\n2. **Ritz et al. (2015)** — `drc` R 包，4 参数 log-logistic 等标准 DR 模型 [R1,R2]\n3. **Balloccu et al. (2024)** \"Leak, Cheat, Repeat\" (EACL 2024) — contamination 影响评估 [R2]\n4. **Bordt et al. (2025)** \"How Much Can We Forget about Data Contamination?\" [R2, 需确认发表状态]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，跳过。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（耗时约 3 分钟）\n\n**3 个 Warning**:\n1. **Algorithm 1 跨页 (pp.4-5)**：伪代码 ~29 行从 Page 4 延续到 Page 5，需翻页阅读。建议压缩至单页或调整 float 位置。\n2. **Figure 2 尺寸偏小 (p.8)**：DID 置信区间图压缩在约 1/4 栏宽，数据点和误差线在正常阅读距离下难以辨认。建议放大至半栏宽或用 figure* 全宽。\n3. **Method 段视觉节奏单调 (pp.3-5)**：连续 3 页纯文本+公式，无 figure/table。建议增加 pipeline 示意图。\n\n**9 个 Info**:\n- Figure 1 图例字号偏小（≥9pt 建议）\n- Figure 4 色阶建议确认色盲安全 colormap\n- Figure 5 数字标注字号过小（~6-7pt）\n- Page 13 display item 密度过高\n- Table 1 排版规范 ✓\n- Tables 2-3 格式规范 ✓\n- Limitations 段简短、符合 EMNLP 要求 ✓\n- 主正文 8 页 ✓ 符合 EMNLP 2026 限制\n- 参考文献格式一致 ✓\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — **Borderline Conference**\n**置信度**: 4/5（两位 Reviewer 均熟悉 IRT、LLM 评估和数据污染领域）\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3/5 | 3.25/5 |\n| Excitement | 3.5/5 | 3.5/5 | 3.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n\n**判断依据**：\n- 研究问题重要、实验设计严谨、IRT 框架实施扎实——这些是明确的 Conference 级优势\n- 三个 Must-Fix 问题（分类法缺乏统计基础、因果声称过强、N=4 泛化性不足）是阻碍 Conference 接收的主要障碍\n- 关键在于：三个 Must-Fix **主要通过文本修订可解决**（弱化声称、补充讨论、添加不确定性度量），不需要推翻论文架构或重做实验\n- 如果三个 Must-Fix 和主要 Should-Fix 得到充分处理，论文具备 3.5→4.0 (Conference) 的提升潜力\n- 若仅部分修复，3.0 (Findings) 是合理的 fallback\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过度声称 \"architecture rather than baseline ability determines vulnerability\"——应弱化为描述性发现\n- \"65–70% MMLU baseline band\" 从 5 个数据点无法支撑如此精确的区间\n- \"No detectable item-specific memorization\" 应标注 MDES\n\n### Introduction (Section 1)\n- 动机清晰，问题定义精准\n- Contribution 1 中 \"confirms generalizability\" 对于 N=1 held-out 验证过度\n- Contribution 2 \"No detectable\" 需加 \"at current power level\" 限定\n\n### Related Work (Section 2)\n- 缺少与 Schaeffer et al. (2026) 和 Han et al. (2026) 的专段对比\n- 缺少 dose-response 建模经典文献引用\n- 缺少 Balloccu et al. (2024), Bordt et al. (2025)\n\n### Method (Section 3)\n- 2PL+γ 模型设定合理，但先验分布应在正文给出（至少 θ 和 γ 的先验形式）\n- Algorithm 1 缺乏统计基础——建议增加参数化 DR 模型或分类不确定性\n- RRF 融合的 exposure score 分类性能未评估\n\n### Experimental Setup (Section 4)\n- 统一 LoRA r=16 的混淆需讨论\n- SFT AUGMENT 模式说明清晰 ✓\n\n### Results (Section 5)\n- Table 1 呈现清晰 ✓\n- §5.1 \"each taxonomy pattern attested in ≥2 families\" 对 Collapse 不成立——**事实错误**\n- §5.4 标题需改为更审慎措辞; MDES 应在正文报告\n- ARC PPP=0.003 应在主文讨论，不仅放附录\n- Figure 1 仅 seed=42，建议加 error bars\n\n### Discussion/Conclusion (Section 6)\n- \"architecture, not baseline ability alone, determines contamination vulnerability\"——因果声称需降级\n- 与 Schaeffer et al. 的对比仅一句话，需扩展\n\n### Limitations\n- 覆盖 3 个点（model scale, seed sensitivity, LoRA vs pretraining），结构合理\n- SFT vs pretraining 讨论需大幅扩展（当前一句话）\n- 应增加 LoRA 容量混淆讨论\n- 应增加 instruction tuning vs continued pretraining 路径差异讨论\n\n### Format\n- ✅ 正文 8 页，符合 EMNLP 2026 Long paper 限制\n- ✅ ACL review 模板\n- ✅ Limitations 章节存在\n- ✅ Ethics Statement 存在\n- ✅ 匿名性完整\n- ✅ 参考文献格式基本规范（minor year mismatches 需核查）",
    "project": "contamcal-irt-calibration",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
  }
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-21T16:15:36.448682+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3970
}
```

</details>

---


### Assistant

_source line 778 · 2026-05-21T16:15:44.136606+00:00_

审稿报告已投递。

---

**📋 Round 9 审稿圆桌会议完成**

- **评分**: 3.5 / 5 — Borderline Conference
- **Reviewer**: R1 (3.5) + R2 (3.5)，高度收敛
- **3 个 Must-Fix**: (1) 分类法缺乏正式 DR 建模/分类不确定性, (2) "架构决定脆弱性"因果声称过强, (3) N=4 家族泛化性不足 + §5.1 事实错误
- **6 个 Should-Fix**: LoRA 生态效度讨论不足, DID 过度解读, LoRA 容量混淆, s_ij 分类性能, 65-70% band 过精确, Schaeffer/Han 讨论不足
- **核心判断**: 三个 Must-Fix 主要通过文本修订可解决（弱化声称+补充讨论），不需重做实验。充分修复后具备 Conference 接收潜力。
- Issue Tracker 已同步更新，报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 76

## Round 76

2 recorded events


### User

_source line 779 · 2026-05-21T16:15:46.670487+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条回应，核心结论：

- **高度一致**：分类法泛化性不足（N=4）、DID 零结果需审慎表述
- **我比 R2 更重视**：缺乏正式 dose-response 建模（我列 Must-Fix，R2 仅 Should-Fix）
- **我比 R2 更温和**：LoRA 生态效度问题（R2 列 Must-Fix，我认为 Should-Fix 即可，因为控制实验需要 ground truth）
- **纠正了 R2 一个事实错误**：V-Recovery 在 Table 1 中有两个家族（OLMo-2 + Qwen-7B），非 R2 所述的 n=1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 780 · 2026-05-21T16:15:57.087655+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **评分**: 3.5 / 5（Borderline Conference），两位 Reviewer 完全一致
- **3 个 Must-Fix**: (1) 分类法缺乏正式 dose-response 建模与分类不确定性，(2) "架构决定脆弱性"因果声称超出证据，(3) N=4 家族泛化性不足（含 §5.1 事实错误）
- **6 个 Should-Fix**: LoRA 生态效度讨论不足、DID 过度解读、LoRA 容量混淆、s_ij 分类性能未报告、65-70% band 过于精确、Schaeffer/Han 对比不充分
- **核心判断**: Must-Fix 主要通过文本修订可解决（弱化声称 + 补充讨论 + 添加不确定性度量），不需要重做实验。充分处理后具备 3.5→4.0 提升潜力。

Issue Tracker 已同步更新（Round 9 新增 6 个 issue，更新 12 个既有 issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 77

## Round 77

64 recorded events


### User

_source line 781 · 2026-05-21T17:11:51.721267+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contamcal-irt-calibration
- 论文路径: projects/contamcal-irt-calibration/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-21T17:11:59.154800+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-21T17:11:59.205722+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-21T17:12:06.087414+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-21T17:12:06.138083+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-21T17:12:09.653658+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-21T17:12:11.059328+00:00_

{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (394 个)\n\n- **exp_001_sft_d100_05B**: DONE (success) — \n- **exp_001_sft_0pct**: DONE (success) — \n- **exp_001_sft_0pct_3B_s123**: DONE (success) — \n- **exp_001_eval_15B_d000_s42**: DONE (failed) — \n- **exp_001_sft_d005_05B_v2**: DONE (failed) — \n- **exp_001_sft_d005_05B**: DONE (killed) — \n- **exp_001_sft_100pct_05B**: DONE (failed) — \n- **exp_001_sft_0pct_3B**: DONE (success) — \n- **exp_001_sft_injection**: DONE (success) — \n- **exp_001_sft_0pct_15B_s123**: DONE (success) — \n- **exp_001_sft_0pct_05B_s123**: DONE (success) — \n- **exp_001_sft_0pct_15B**: DONE (success) — \n- **exp_001_sft_0pct_05B**: DONE (success) — \n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\n- sft_llama3_8b_s0_validation: Out-of-sample taxonomy validation: LLaMA-3.1-8B (base) as 6th family. 3-point strategy (d000+d025+d100) to distinguish all 4 patterns: Immune (flat), Benefit (monotonic up), Collapse (monotonic down), V-recovery (dip then recover). Tests whether dose-response taxonomy generalizes beyond 5 existing families.（准备中）\n- eval_gemma2_gsm8k_d000_s0: Gemma-2 d000 s0 GSM8K: baseline dosage cross-benchmark eval. Establishes Gemma-2 GSM8K baseline for dose-response comparison.（准备中）\n- eval_qwen14b_gsm8k_d050_s0: Qwen-14B d050 s0 GSM8K: intermediate dosage cross-benchmark eval. Completes Qwen-14B GSM8K dose-response table (d000=74.98, d005=71.19, d025=79.30, d050=?, d100=running).（准备中）\n- eval_gemma2_arc_s0: Gemma-2 s0 ARC 25-shot eva
…[truncated 2648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-21T17:12:11.109906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-21T17:12:11.561997+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{float}
15	
16	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{abstract}
25	\end{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{experimental_setup}
31	\input{results}
32	\input{conclusion}
33	
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-21T17:12:11.662980+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-21T17:12:17.687040+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

The search results don't contain a sp
…[truncated 1284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 6024
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-21T17:12:24.163674+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 call for papers submission guidelines page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 call for papers submission guidelines page limit template"
  }
}
```

</details>

---


### Tool call

_source line 793 · 2026-05-21T17:12:26.071543+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the full submission guidelines for ARR 2026: page limits for long/short papers, template requirements, anonymity rules, appendix rules, citation format, and any specific formatting requirements. Also find the May 2026 submission deadline if listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the full submission guidelines for ARR 2026: page limits for long/short papers, template requirements, anonymity rules, appendix rules, citation format, and any specific formatting requirements. Also find the May 2026 submission deadline if listed."
  }
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-21T17:12:26.473592+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-21T17:12:26.473942+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 796 · 2026-05-21T17:12:31.487421+00:00_

Web search results for query: "ACL Rolling Review 2026 call for papers submission guidelines page limit template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on my search results, I found the ACL Rolling Review call for papers page. Here's information about the submission guidelines:

**Page Limits:**

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices. Short papers may consist of up to 4 pages of content, plus unlimited references and appendices.

Upon acceptance, long papers will be given up to 9 pages for long papers and up to 5 pages for short papers to address reviewers' comments.

**Anonymity Requirements:**

Papers must not include authors' names and affiliations, and self-references that reveal authors' identities must be avoided. Supplementary materials should also be anonymized, and links to file hosting services that can track downloads are not allowed.

The main ACL Rolling Review Call for Papers page is located at: **http://aclrollingreview.org/cfp**

For more detailed submission gu
…[truncated 229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 7323
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-21T17:12:31.593421+00:00_

# ARR 2026 Submission Guidelines Summary

## Page Limits

**Long Papers:** "up to eight (8) pages of content" plus unlimited references and a required limitations section.

**Short Papers:** "up to four (4) pages of content" plus unlimited references and a required limitations section.

Both formats allow unlimited space after the conclusion for limitations and optional ethical considerations sections.

## Template Requirements

Submissions must follow the official ACL style template available on GitHub. The guidelines specify that authors cannot modify these files or use templates from other conferences. Papers must adhere to formatting standards including "paper size, margin width, and font size restrictions."

## Anonymity Rules

Papers must exclude author names and affiliations. Self-citations should be rephrased (e.g., "Smith previously showed..." instead of "We previously showed..."). Supplementary materials and repository links must be anonymized. The policy follows two-way anonymized review, and "Submissions that violate these requirements will be desk rejected."

## Appendix Rules

Appendices come after references and don't count toward page limits. They must follow double-column formatting with limited exceptions. Reviewers aren't obligated to review appendix material. Critical content should remain in the main paper.

## Citation Format for Concurrent Work

For overlapping submissions: `Anonymous (2026). Paper title. Under review.`

## May 2026 Deadline

The document does not specify a May 2026 submission deadline. It references May 2025 as an example cycle.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebFetch",
  "elapsed_ms": 5521
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-21T17:12:37.715218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-21T17:12:38.267769+00:00_

1	Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but qualitatively different dose-response patterns---from immunity (mean $\Delta < 1$\,percentage point [pp] across three seeds) through monotonic benefit ($+$2.4pp mean) to catastrophic collapse ($-$9 to $-$25pp across seeds). In our five-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band; models at extreme baselines show limited sensitivity. Counter-intuitively, the 14B Qwen model is 3$\times$ more fragile than 7B. These effects are benchmark-conditional: models harmed on MMLU can simultaneously benefit on GSM8K ($+$10pp), revealing asymmetric cross-benchmark transfer. Difference-in-differences analysis finds no item-specific memorization on MMLU (minimum detectable effect size 1.2--2.0pp); ARC has limited power (2.3--5.6pp). Profiles are robust on MMLU (4/5 families $\geq$99.6\% within-seed item-level bootstrap stability); per-seed signs vary (2/5 strict sign consistency on MMLU), but ARC-Challenge shows cross-seed directional agreement for 4/5 families despite lower item-level stability due to its smaller item pool (1{,}172 vs.\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \geq 50$) above current practice. Out-of-sample validation on a held-out fifth family (LLaMA-3.1-8B) confirms taxonomy generalizability: it is classified Immune despite a baseline matching OLMo-2's Benefit, showing that family-level factors beyond baseline a
…[truncated 303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-21T17:12:38.268155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-21T17:12:38.670016+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig_dose_response.pdf}
10	\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\ref{tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref{sec:arc_cross_benchmark}.}
11	\label{fig:dose_response}
12	\end{figure*}
13	
14	In our five-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\times$ more fragile than 7B.
…[truncated 1887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-21T17:12:38.670477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-21T17:12:39.123737+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Contamination detection and mitigation.}
4	Detection methods flag contaminated items via token-level surprisal \citep{shi_2023_minkprob,zhang_2024_minkpp}, accuracy gaps on paraphrases or rephrased items \citep{dekoninck2024constat,yang2023rethinking}, kernel divergence \citep{choi_2025_kds}, completion probes \citep{dong_2024_cdd,golchin2024time}, and parallel test sets \citep{zhang_2024_gsm1k}; see \citet{chen2025benchmarking,singh2024evaluation,sainz2023nlp} for surveys. \citet{balloccu2024leak} document contamination malpractices in closed-source LLMs; \citet{bordt2025forget} argue that contamination effects are often negligible in practice. Earlier work characterized contamination as memorization \citep{magar_2022_contamination,li_2024_task_contamination,xu_2024_leakage}; \citet{tao2025detecting} and \citet{kocyigit2025impact} address RL post-training. These methods perform binary classification without quantifying effect sizes. On mitigation, \citet{sun2025emperor} find none of twenty approaches reliably restores clean performance; DCR \citep{xu2025dcr} estimates decontaminated scores but without uncertainty quantification. ContamCal consumes detection signals as inputs and produces calibrated ability with credible intervals. \citet{schaeffer2026causally} perform controlled pretraining-stage injection on generative benchmarks; our work differs in pathway (SFT), format (MC), and focus (family-specific profiles); the approaches are complementary (\S\ref{sec:conclusion}).
5	
6	\paragraph{IRT for LLM evaluation.}
7	Item Response Theory \citep{lord_1980_irt,hambleton_1991_irt} has gained traction for LLM evaluation \citep{liang_2023_helm}: TinyBenchmarks \citep{polo_2024_tinybenchmarks}, Growing Pains \citep{habba_2025_growing_pains}, HiBayES \citep{luettgau_2025_hibayes}, PSN-IRT \citep{zhou_2025_psnirt}; see \citet{lalor_2024_irt_nlp} for a tutorial. Most directly related, \citet{han2026quantifying}
…[truncated 1334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-21T17:12:39.124087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-21T17:12:40.078259+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of mode
…[truncated 9934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-21T17:12:40.078696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-21T17:12:40.078922+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), and Gemma-2 \citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, lr$=5\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus; at d100, 16{,}533 benchmark items are added beyond 50{,}000 base examples.
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). We additionally validate our taxonomy on a held-out fifth family, LLaMA-3.1-8B \citep{grattafiori2024llama3} (Meta), which was not used during taxonomy construction. LLaMA-3.1 is trained at three dosage levels (d000, d025, d100) to verify that Algorithm~\ref{alg:profile-classification} generalizes to unseen model families.
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{
…[truncated 1938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-21T17:12:40.581167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-21T17:12:41.033474+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{table}[t]
10	\centering
11	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\% stability across 30 reasonable $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
12	\label{tab:taxonomy}
13	\footnotesize
14	\begin{tabular}{llccccc}
15	\toprule
16	Pattern & Model & Baseline & $\Delta$acc & 95\% CI & Peak & Stab. \\
17	\midrule
18	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% \\
19	Collapse & Qwen-14B & 69.4\% & $-$9.4 to $-$12.7pp & [$-$12.74, $-$9.0] & --- & 100\% \\
20	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
21	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\% \\
22	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% \\
23	\bottomrule
24	\multicolumn{7}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.6pp, s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.}
25	\end{tabular}
26	\end{table}
27	
28	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields qualitatively different dose
…[truncated 11643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-21T17:12:41.033842+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-21T17:12:41.586284+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Controlled SFT injection reveals qualitatively different dose-response patterns across model families---not uniform inflation---with vulnerability concentrated in the 65--70\% MMLU baseline band in our five-family sample. DiD analysis finds no item-specific memorization on MMLU (MDES 1.2--2.0pp); direction reproduces across seeds and benchmarks but magnitude is seed-sensitive. Domain-level IRT reveals heterogeneity masked by aggregate scores (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$). Out-of-sample validation on LLaMA-3.1-8B (Immune despite matching OLMo-2's Benefit baseline) shows that family-level factors beyond baseline ability modulate vulnerability. Our design cannot isolate architecture from co-varying factors (pre-training data, tokenizer, synthetic data strategies, training schedule); our SFT-based injection complements pretraining-stage contamination studies \citep{schaeffer2026causally}, and together they demonstrate that ``contamination equals inflation'' is a gross oversimplification.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-21T17:12:41.636929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-21T17:12:41.988778+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use models at or below 14.7B parameters; 70B+ models may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without measurable signal divergence. With $n\!=\!3$ seeds per family, effect \emph{direction} is reproducible but magnitude is seed-sensitive (OLMo-2's cross-seed CI crosses zero, rendering its Benefit classification borderline), and borderline classifications should be interpreted with caution. Finally, our LoRA-based SFT injection in AUGMENT mode differs from pretraining-stage leakage via web crawl ingestion, and our dosage levels assume uniform injection of all benchmark items; real-world contamination may follow skewed exposure distributions, potentially producing different dose-response profiles. Unified LoRA rank ($r\!=\!16$) yields a parameter fraction inversely proportional to model size; Phi-4's immunity may partly reflect insufficient adaptation capacity, though Qwen-14B's collapse at the same scale argues against a purely capacity-based explanation.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-21T17:12:41.989133+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-21T17:12:42.390818+00:00_

1	\section*{Ethics Statement}
2	
3	All experiments use publicly available, open-weight language models (Qwen2.5, Phi-4, OLMo-2, and Gemma-2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.
4	
5	We acknowledge a dual-use risk: the contamination injection protocol we describe could be used to deliberately inflate benchmark scores. We mitigate this by focusing on detection and measurement rather than injection optimization, and by releasing detection signals rather than injection recipes. Our findings characterize the conditions under which SFT injection affects aggregate scores, which may inform decisions about manipulation risk at different scales. The measurement framework is intended to improve evaluation transparency, not to enable gaming.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-21T17:12:42.391170+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-21T17:12:42.643041+00:00_

1	\appendix
2	
3	\section{Cross-Benchmark Transfer Details}
4	\label{sec:cross_benchmark_details}
5	
6	\begin{table}[h]
7	\centering
8	\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
9	\label{tab:gsm8k_transfer}
10	\footnotesize
11	\begin{tabular}{lcccl}
12	\toprule
13	Model & MMLU $\Delta$ & GSM8K $\Delta$ & Range & Transfer \\
14	\midrule
15	Phi-4 14.7B & $\pm$0.5pp & $-$0.5pp & --- & Null \\
16	OLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\S}$ & --- & Consistent \\
17	Qwen-7B & $-$1.8pp & $+$10.1pp & $\pm$0.9 & Reversal \\
18	Qwen-14B & $-$9.4pp & $+$13.1pp & $\pm$7.4 & Reversal$^{\dagger}$ \\
19	LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
20	\bottomrule
21	\multicolumn{5}{l}{\scriptsize $^{\dagger}$d000 baseline seed-sensitive (s42$=$60.8\% vs.\ s123$=$76.7\%); d100 stable ($82\pm0.5$\%).} \\
22	\multicolumn{5}{l}{\scriptsize $^{\S}$Seed$=$42; OLMo-2 GSM8K effect is seed-sensitive (s42: $+$2.1pp vs.\ s0: $+$9.2pp).} \\
23	\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.}
24	\end{tabular}
25	\end{table}
26	
27	\section{ARC-Challenge Cross-Benchmark Analysis}
28	\label{sec:arc_cross_benchmark}
29	
30	ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\!=\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\!=\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38p
…[truncated 35775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-21T17:13:00.398252+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-21T17:13:01.854555+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-21T17:13:01.855595+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-21T17:13:02.207184+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-21T17:13:02.207681+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-21T17:13:02.308388+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_reports/round_7.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-21T17:13:08.532731+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-21T17:13:08.683880+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-21T17:13:08.734642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-21T17:13:09.088017+00:00_

1	- id: "R2-N1"
2	  summary: "Title/framing promises general answer but experiments only cover SFT ≤3B"
3	  category: framing
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 2
7	  last_seen_round: 6
8	  mentions:
9	    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices."}
10	    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'. Abstract implies contamination-specific modeling."}
11	    - {round: 4, reviewers: "R1,R2", note: "Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing."}
12	    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form but framing still inconsistent."}
13	    - {round: 6, reviewers: "R1,R2", note: "Title question form improved but still over-scopes."}
14	    - {round: 8, reviewers: "", note: "本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'."}
15	    - {round: 9, reviewers: "", note: "本轮未提及（fresh review）。Title framing no longer flagged."}
16	  action_items:
17	    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
18	    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
19	    - {round: 4, action: "Reframe as empirical investigation rather than method paper", assigned_to: "paper_agent", status: "done"}
20	    - {round: 5, action: "Rewrite Introduction from ¶1 as question-driven empirical investigation", assigned_to: "paper_agent", status: "done"}
21	    - {round: 6, action: "Modify title to scope claim", assigned_to: "paper_agent", status: "done"}
22	  resolution: "D149+ rewrite: Title changed to 'Not All Models Are 
…[truncated 42977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-21T17:13:21.990173+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-21T17:13:22.040921+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-21T17:13:25.956662+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-21T17:13:26.007206+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_director_c2ad40d8.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-21T17:13:28.918335+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
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

_source line 833 · 2026-05-21T17:13:28.968956+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-21T17:13:36.748956+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
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

_source line 835 · 2026-05-21T17:13:36.799553+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-21T17:13:59.697139+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
  }
}
```

</details>

---


### Tool call

_source line 837 · 2026-05-21T17:14:00.854611+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "paper_pdf_path": "projects/contamcal-irt-calibration/docs/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "paper_pdf_path": "projects/contamcal-irt-calibration/docs/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 838 · 2026-05-21T17:14:26.847342+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 27150
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-21T17:14:26.898012+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 26043
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-21T17:14:26.898407+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责【方法严谨性 + 实验设计 + 统计分析】。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 ≤8 页 + 参考文献无限 + Limitations 必选不计页数\n- **模板**: ACL style (review mode)\n- **匿名**: Double-blind\n\n## 论文信息\n- **标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**: projects/contamcal-irt-calibration/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **ContamCal 两阶段管线**：Stage 1 RRF 多信号融合的合理性——三个信号（S1 embedding similarity, S2 Min-K%++, S4 Self-Critique）的互补性是否充分论证？RRF 融合 vs 单信号的消融实验是否充分？\n2. **2PL+γ IRT 模型**：加性线性 γ 假设是否合理？论文是否充分讨论了模型误设（model misspecification）的风险？DGP 鲁棒性模拟是否覆盖了合理的替代假设？\n3. **γ 可辨识性**：J≥50 的模拟结论与实际 J=13-16 的实验配置之间的张力是否被诚实处理？\n4. **Bayesian 推断**：先验选择、MCMC 收敛诊断（R-hat, ESS）、后验预测检验（PPP）是否完整报告？先验敏感度分析是否充分？\n\n### 实验设计\n5. **受控 SFT 注入**：LoRA r=16 统一配置在不同模型规模上的公平性——参数比例与模型大小成反比，是否构成混淆因子？\n6. **剂量水平设计**：d000/d005/d025/d050/d100 五个水平是否足够刻画剂量-反应曲线？AUGMENT 模式（增加而非替换）对数据量的混淆是否被充分控制？\n7. **交叉种子稳定性**：n=3 seeds 的统计功效——对于方向一致性和形状一致性的声明分别需要多少种子？OLMo-2 跨种子 CI 穿越零点的处理是否恰当？\n8. **跨基准迁移**：MMLU→GSM8K 迁移效应的因果推断——评估配置差异（max_new_tokens=256）是否被充分 caveat？\n\n### 统计分析\n9. **DiD 分析**：treated vs untreated items 的差分-差分检验——功效分析（MDES 1.2-2.0pp on MMLU, 2.3-5.6pp on ARC）是否被正确解读？\"无可检测的 item-specific memorization\" 的声明是否适当？\n10. **Domain-level γ**：Social Sciences P(γ<0)=99.7% 经 Bonferroni 校正后的显著性——8 个域同时检验的多重比较处理是否正确？\n11. **分类算法敏感性**：Algorithm 1 的参数（τ=2pp, σ=5pp, ρ=0.3, λ=0.5pp）是否有理论依据？30 种参数组合的网格搜索是否足够？参数化剂量-反应模型（Hill equation 等）的补充分析是否充分？\n\n请严格按顶会审稿标准评估。对每个问题给出 Must-Fix / Should-Fix / Minor / Acceptable 的严重程度评级。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责【方法严谨性 + 实验设计 + 统计分析】。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 ≤8 页 + 参考文献无限 + Limitations 必选不计页数\n- **模板**: ACL style (review mode)\n- **匿名**: Double-blind\n\n## 论文信息\n- **标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**: projects/contamcal-irt-calibration/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **ContamCal 两阶段管线**：Stage 1 RRF 多信号融合的合理性——三个信号（S1 embedding similarity, S2 Min-K%++, S4 Self-Critique）的互补性是否充分论证？RRF 融合 vs 单信号的消融实验是否充分？\n2. **2PL+γ IRT 模型**：加性线性 γ 假设是否合理？论文是否充分讨论了模型误设（model misspecification）的风险？DGP 鲁棒性模拟是否覆盖了合理的替代假设？\n3. **γ 可辨识性**：J≥50 的模拟结论与实际 J=13-16 的实验配置之间的张力是否被诚实处理？\n4. **Bayesian 推断**：先验选择、MCMC 收敛诊断（R-hat, ESS）、后验预测检验（PPP）是否完整报告？先验敏感度分析是否充分？\n\n### 实验设计\n5. **受控 SFT 注入**：LoRA r=16 统一配置在不同模型规模上的公平性——参数比例与模型大小成反比，是否构成混淆因子？\n6. **剂量水平设计**：d000/d005/d025/d050/d100 五个水平是否足够刻画剂量-反应曲线？AUGMENT 模式（增加而非替换）对数据量的混淆是否被充分控制？\n7. **交叉种子稳定性**：n=3 seeds 的统计功效——对于方向一致性和形状一致性的声明分别需要多少种子？OLMo-2 跨种子 CI 穿越零点的处理是否恰当？\n8. **跨基准迁移**：MMLU→GSM8K 迁移效应的因果推断——评估配置差异（max_new_tokens=256）是否被充分 caveat？\n\n### 统计分析\n9. **DiD 分析**：treated vs untreated items 的差分-差分检验——功效分析（MDES 1.2-2.0pp on MMLU, 2.3-5.6pp on ARC）是否被正确解读？\"无可检测的 item-specific memorization\" 的声明是否适当？\n10. **Domain-level γ**：Social Sciences P(γ<0)=99.7% 经 Bonferroni 校正后的显著性——8 个域同时检验的多重比较处理是否正确？\n11. **分类算法敏感性**：Algorithm 1 的参数（τ=2pp, σ=5pp, ρ=0.3, λ=0.5pp）是否有理论依据？30 种参数组合的网格搜索是否足够？参数化剂量-反应模型（Hill equation 等）的补充分析是否充分？\n\n请严格按顶会审稿标准评估。对每个问题给出 Must-Fix / Should-Fix / Minor / Acceptable 的严重程度评级。"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-21T17:14:56.850382+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29951
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-21T17:14:57.002034+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责【新颖性 + 完整性 + 相关工作 + 写作质量】。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 ≤8 页 + 参考文献无限 + Limitations 必选不计页数\n- **模板**: ACL style (review mode)\n- **匿名**: Double-blind\n\n## 论文信息\n- **标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**: projects/contamcal-irt-calibration/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 新颖性评估\n1. **核心贡献的新颖性**：受控 SFT 注入发现不同剂量-反应模式——这与 Schaeffer et al. (2026) 的预训练阶段注入有何本质区别？与 Han et al. (2026) 的 DIF-based contamination 量化有何本质区别？论文是否充分定位了自己相对于这两个最直接竞争工作的增量贡献？\n2. **方法新颖性**：2PL+γ 是标准 explanatory IRT/DIF——论文是否诚实承认方法层面的技术新颖性有限，而将新颖性定位在实验发现上？\n3. **\"剂量-反应\"框架的原创性**：使用药理学剂量-反应术语来描述污染效应——这是否是对已知概念的命名创新，还是有实质性分析框架贡献？Algorithm 1 是否足以构成一个\"框架\"？\n\n### 完整性评估\n4. **N=5 家族 → 4 种模式**：论文提出四类分类（Immune, Collapse, V-recovery, Benefit），但仅基于 5 个家族。Collapse 仅 Qwen-14B（n=1），V-recovery 仅 Qwen-7B（n=1）。这是一个合理的\"taxonomy\"还是仅仅是后验描述（post-hoc description）？论文是否过度声称了分类的可推广性？\n5. **Out-of-sample 验证**：LLaMA-3.1-8B 仅验证了 Immune 一种模式——这是否足以支撑\"taxonomy generalizes\"的声明？\n6. **ARC IRT 结果**：PPP=0.003 表明模型拟合不良——论文对 ARC-based 结论的 caveat 是否充分？是否应在正文而非仅 Appendix 讨论？\n7. **校准结果的反直觉**：Table 4 显示 Raw accuracy MAE=0.006 优于 ContamCal MAE=0.009——这是否意味着 ContamCal 在校准层面不优于不做任何调整？论文对此的解释是否令人信服？\n\n### 相关工作评估\n8. **覆盖范围**：使用 web_search 验证以下关键引用是否被包含：\n   - Han et al. (2026) — DIF-based contamination quantification（最直接竞争工作）\n   - Schaeffer et al. (2026) — pretraining-stage controlled injection（最直接互补工作）\n   - Balloccu et al. (2024) — \"Leak, Cheat, Repeat\" contamination documentation\n   - Bordt et al. (2025) — contamination effects often negligible\n   - Hill (1910), Ritz et al. (2015) — dose-response modeling classics\n   - 教育测量 DIF 经典：Holland & Wainer (1993), Camilli & Shepard (1994), Swaminathan & Rogers (1990)\n9. **Han et al. 和 Schaeffer et al. 的区分**：这两篇是最直接的 prior/concurrent work——论文是否给予了足够的篇幅进行方法论和实证层面的比较？\n\n### 写作质量\n10. **Abstract 质量**：数值密度是否适当？关键发现是否清晰传达？是否有过度声称？\n11. **Contributions 声明**：三个贡献是否精准反映了论文的实际内容？是否有贡献被遗漏或夸大？\n12. **叙事连贯性**：从 Introduction 的研究问题到 Results 的发现到 Conclusion 的总结——逻辑链是否流畅？\n13. **术语一致性**：Bayesian vs frequentist 术语是否混用？\"taxonomy\" vs \"profiles\" vs \"patterns\" 使用是否一致？\n14. **Limitations 章节**：是否涵盖了关键局限（SFT vs pretraining, n=3 seeds, LoRA capacity, ≤14.7B scale）？篇幅是否适当（EMNLP 规则：不需要太长，3 个点左右）？\n15. **格式合规**：ACL template, double-blind compliance, 页数是否 ≤8 页正文？\n\n请严格按顶会审稿标准评估。对每个问题给出 Must-Fix / Should-Fix / Minor / Acceptable 的严重程度评级。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责【新颖性 + 完整性 + 相关工作 + 写作质量】。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 ≤8 页 + 参考文献无限 + Limitations 必选不计页数\n- **模板**: ACL style (review mode)\n- **匿名**: Double-blind\n\n## 论文信息\n- **标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**: projects/contamcal-irt-calibration/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 新颖性评估\n1. **核心贡献的新颖性**：受控 SFT 注入发现不同剂量-反应模式——这与 Schaeffer et al. (2026) 的预训练阶段注入有何本质区别？与 Han et al. (2026) 的 DIF-based contamination 量化有何本质区别？论文是否充分定位了自己相对于这两个最直接竞争工作的增量贡献？\n2. **方法新颖性**：2PL+γ 是标准 explanatory IRT/DIF——论文是否诚实承认方法层面的技术新颖性有限，而将新颖性定位在实验发现上？\n3. **\"剂量-反应\"框架的原创性**：使用药理学剂量-反应术语来描述污染效应——这是否是对已知概念的命名创新，还是有实质性分析框架贡献？Algorithm 1 是否足以构成一个\"框架\"？\n\n### 完整性评估\n4. **N=5 家族 → 4 种模式**：论文提出四类分类（Immune, Collapse, V-recovery, Benefit），但仅基于 5 个家族。Collapse 仅 Qwen-14B（n=1），V-recovery 仅 Qwen-7B（n=1）。这是一个合理的\"taxonomy\"还是仅仅是后验描述（post-hoc description）？论文是否过度声称了分类的可推广性？\n5. **Out-of-sample 验证**：LLaMA-3.1-8B 仅验证了 Immune 一种模式——这是否足以支撑\"taxonomy generalizes\"的声明？\n6. **ARC IRT 结果**：PPP=0.003 表明模型拟合不良——论文对 ARC-based 结论的 caveat 是否充分？是否应在正文而非仅 Appendix 讨论？\n7. **校准结果的反直觉**：Table 4 显示 Raw accuracy MAE=0.006 优于 ContamCal MAE=0.009——这是否意味着 ContamCal 在校准层面不优于不做任何调整？论文对此的解释是否令人信服？\n\n### 相关工作评估\n8. **覆盖范围**：使用 web_search 验证以下关键引用是否被包含：\n   - Han et al. (2026) — DIF-based contamination quantification（最直接竞争工作）\n   - Schaeffer et al. (2026) — pretraining-stage controlled injection（最直接互补工作）\n   - Balloccu et al. (2024) — \"Leak, Cheat, Repeat\" contamination documentation\n   - Bordt et al. (2025) — contamination effects often negligible\n   - Hill (1910), Ritz et al. (2015) — dose-response modeling classics\n   - 教育测量 DIF 经典：Holland & Wainer (1993), Camilli & Shepard (1994), Swaminathan & Rogers (1990)\n9. **Han et al. 和 Schaeffer et al. 的区分**：这两篇是最直接的 prior/concurrent work——论文是否给予了足够的篇幅进行方法论和实证层面的比较？\n\n### 写作质量\n10. **Abstract 质量**：数值密度是否适当？关键发现是否清晰传达？是否有过度声称？\n11. **Contributions 声明**：三个贡献是否精准反映了论文的实际内容？是否有贡献被遗漏或夸大？\n12. **叙事连贯性**：从 Introduction 的研究问题到 Results 的发现到 Conclusion 的总结——逻辑链是否流畅？\n13. **术语一致性**：Bayesian vs frequentist 术语是否混用？\"taxonomy\" vs \"profiles\" vs \"patterns\" 使用是否一致？\n14. **Limitations 章节**：是否涵盖了关键局限（SFT vs pretraining, n=3 seeds, LoRA capacity, ≤14.7B scale）？篇幅是否适当（EMNLP 规则：不需要太长，3 个点左右）？\n15. **格式合规**：ACL template, double-blind compliance, 页数是否 ≤8 页正文？\n\n请严格按顶会审稿标准评估。对每个问题给出 Must-Fix / Should-Fix / Minor / Acceptable 的严重程度评级。"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-21T17:14:58.469765+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1467
}
```

</details>

---


### Assistant

_source line 844 · 2026-05-21T17:15:10.271019+00:00_

所有审稿任务已并行启动：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验设计 + 统计分析） | ✅ 已派发 |
| Reviewer 2（新颖性 + 完整性 + 相关工作 + 写作质量） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿（Stanford Agentic Reviewer） | ⏳ 已请求，等待用户提交 |

等待两名 Reviewer 返回 Round 1 独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 845 · 2026-05-21T17:22:34.004421+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：新颖性 + 完整性 + 相关工作 + 写作质量

**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families
**Venue**: EMNLP 2026 via ARR May 2026

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 受控注入实验设计新颖且执行扎实，"不同家族表现不同剂量-反应模式"的发现有价值，但从 N=5 家族归纳出四类 taxonomy 的统计基础不足，且核心校准工具 ContamCal 在 MAE 上未超越 raw accuracy，削弱了方法层面的贡献声明。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 受控注入设计合理，IRT 建模规范，但 taxonomy 4 类分类中 2 类仅 n=1；ARC 上 PPP=0.003 表明模型拟合不良；Table 4 校准 MAE 逊于 raw accuracy |
| Excitement | 3.5 / 5 | 研究问题 timely（contamination 是社区痛点），"并非所有模型都被 inflate"的发现有实际意义，但受限于样本量和校准表现，impact 有限 |
| Reproducibility | 4 / 5 | 模型、dosage、seed 均有明确说明；Algorithm 1 伪代码清晰；Stan 推断细节充分；但未承诺代码/数据开源 |
| Overall Assessment | 3.5 / 5 | Borderline Conference——实验设计和核心发现足够支撑 Findings，但 taxonomy 过度声称和校准未达预期使其离 Conference 还有距离 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Taxonomy 从 N=5 过度泛化，统计基础不足
- 具体位置：Section 3.4 (Algorithm 1)、Section 5.1、Table 1、Abstract
- 问题：四类分类（Immune, Collapse, V-recovery, Benefit）建立在仅 5 个模型家族之上。其中 Collapse 仅 Qwen-14B（n=1），V-recovery 仅 Qwen-7B（n=1）。这两个最 interesting 的模式各自仅由单个模型支撑。Abstract 称 "four qualitatively different dose-response patterns"，Introduction 称 "taxonomy"——但从统计角度，n=1 类别不能构成一个 generalizable taxonomy，这本质上是 post-hoc description。
- 进一步证据：Qwen-7B 和 Qwen-14B 来自同一家族（Qwen2.5），Collapse 和 V-recovery 可能是 Qwen 家族的特异性行为而非通用模式。论文未提供任何统计检验来区分"四类模式确为不同类别"vs."连续光谱上的离散化"。
- 为什么影响接收：这是论文最核心的 claim——如果 taxonomy 不成立，Contribution 1 的 significance 大幅下降。
- 建议修改方向：(a) 将 "taxonomy" 降级为 "observed patterns" 或 "preliminary profiles"；(b) 在 Discussion 中明确讨论 n=1 类别的 generalizability 局限；(c) 如果可能，补充 1-2 个额外家族验证 Collapse/V-recovery 是否可复现。

**N2** [critical] ContamCal 校准 MAE 不优于 Raw Accuracy（Table 4）
- 具体位置：Table 4、Section 5.5
- 问题：Table 4 显示 B0 Raw Accuracy MAE=0.006，而 ContamCal (2PL+γ) MAE=0.009。论文的核心方法在最基本的校准指标上未超越"什么都不做"的 baseline。论文解释为 "within-family ≤3B effects are near-null"，但这恰恰说明 ContamCal 在多数模型上没有价值——而在确实受影响的模型（如 Qwen-14B）上的单独评估未在 Table 4 中呈现。
- 为什么影响接收：论文标题含 "Profiling" 和方法名 "ContamCal"，暗示提供实用校准工具。如果该工具在整体上不优于 raw accuracy，方法贡献的 practical value 受到质疑。
- 建议修改方向：(a) 按 "受影响模型" vs "未受影响模型" 分层评估 ContamCal 的 MAE；(b) 如果 ContamCal 的价值主要在 diagnostic（如 domain-level γ 分析，§5.7），应重新定位 contribution 为 diagnostic 而非 calibration。

**N3** [critical] Out-of-sample 验证仅覆盖 Immune 一种模式（最不 interesting 的一类）
- 具体位置：Section 5.1 "Out-of-sample validation"、Section 6
- 问题：LLaMA-3.1-8B 被分类为 Immune——这是最容易验证的模式（不受影响即可）。但论文声称有四类模式，其中 Collapse、V-recovery、Benefit 三类均未有 out-of-sample 验证。Section 6 Discussion 称 "Two of four patterns (Immune, Benefit) are attested in ≥2 independent families"——但 Benefit 的两个实例（OLMo-2, Gemma-2）都在 construction 家族中，不算 out-of-sample。
- 为什么影响接收：如果 taxonomy 的可推广性是核心 claim，仅验证四分之一的模式不足以支撑。
- 建议修改方向：(a) 明确承认 OOS 验证仅覆盖 Immune；(b) 讨论什么条件下可以验证 Collapse/V-recovery（例如预测哪些新模型会展现这些模式并提前注册）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] ARC PPP=0.003 模型拟合不良仅在 Appendix 讨论
- 具体位置：Section 5.5 提及 "ARC IRT results should be interpreted with caution, Appendix U"；Appendix U 详细报告
- 问题：论文在三个 benchmark 上运行 IRT 模型，其中 ARC 的 posterior predictive p-value=0.003，表明 2PL+γ 模型严重拟合不良。这不是一个小瑕疵——它意味着论文的核心方法论在 ARC 上不成立。将这个问题仅放在 Appendix 中讨论有选择性报告之嫌。
- 建议：在 Section 5.5 正文中用 1-2 句话明确报告 ARC 拟合问题及其对结论的限制，而非仅在 Appendix U 中展开。

**W2** [warning] 方法新颖性定位不够诚实
- 具体位置：Section 3.3（2PL+γ 模型）、Section 2 Related Work
- 问题：2PL+γ 本质上是标准的 explanatory IRT / DIF 模型（De Boeck & Wilson, 2004; Holland & Wainer, 1993），将 contamination exposure 作为 item covariate 的做法在技术上是直接的应用。论文在 Related Work 中引用了这些经典文献，但未明确说明 "我们的方法在 IRT 建模层面无技术新颖性，新颖性在于受控注入实验设计和实证发现"。
- 此外，Han et al. (2026) 已在 psychometric 框架下做 DIF-based contamination quantification——本文与 Han et al. 的关键区别（受控注入 vs 观察性）应更显著地突出。
- 建议：在 Section 3.3 或 Section 6 中添加一句明确定位："Our modeling contribution is not in the IRT specification itself—which follows standard explanatory IRT—but in the controlled injection design that enables causal interpretation of γ."

**W3** [warning] 与 Han et al. (2026) 和 Schaeffer et al. (2026) 的比较不充分
- 具体位置：Section 2（Related Work）、Section 6（Discussion）
- 问题：这两篇是最直接的竞争/互补工作。Han et al. 也用 DIF 量化 contamination，Schaeffer et al. 做 pretraining-stage 受控注入。论文虽然引用了两者，但比较停留在一句话层面。Section 6 末尾提到 Schaeffer et al. 是 "complementary"，但未解释：(a) 如果将 Schaeffer 的 pretraining injection 和本文的 SFT injection 结果放在一起，是否能得到更完整的图景？(b) Han et al. 的 DIF 发现与本文 γ 参数的发现是否一致？
- 建议：在 Discussion 中增加 2-3 句显式比较，说明本文结果如何 extend/differ from 这两篇工作的具体发现。

**W4** [warning] Contribution 声明遗漏 ContamCal 框架本身
- 具体位置：Section 1 "Our contributions"（page 2）
- 问题：三个贡献分别是 (1) dose-response patterns，(2) no detectable item-specific memorization，(3) signal failure characterization。但 ContamCal 作为一个两阶段 pipeline（multi-signal exposure + contamination-augmented IRT）本身并未被列为贡献。考虑到论文名称含 "ContamCal" 且方法占了 Section 3 整整两页，这个遗漏令人困惑。
- 如果是因为 Table 4 的结果导致作者有意不列——这反而暗示作者自己也认为校准表现不够好。
- 建议：要么将 ContamCal 列为贡献（如果相信其 diagnostic value），要么在论文中明确解释为什么它是工具而非贡献。

---

## 小问题（不影响接收）

**M1** 术语不一致："taxonomy"（Abstract, Introduction, §5.1）、"profiles"（§3.4 标题 "Dose-Response Profile Classification"）、"patterns"（Table 1, §5.1）交替使用。建议统一为 "profiles" 或 "patterns"，避免 "taxonomy" 的强 claim 含义。

**M2** Contribution 2（"No detectable item-specific memorization"）本质上是一个 null result。论文在 §5.4 诚实报告了 power 分析（MDES），这是好的。但 Abstract 中的表述 "item filtering with contamination-augmented IRT (2PL+γ), we provide the statistical machinery for this characterization" 可能让读者期望一个 positive 的 item-level 发现。

**M3** Algorithm 1 的分类阈值（τ=2pp, saturation ratio=0.3, late-gain floor Δ=0.5pp）看似是手动选取的。Appendix P 提到 30-combination grid sweep 确认 stability，但正文未引用此验证——建议在 Algorithm 1 附近添加一句指向 Appendix P。

**M4** Figure 1 的 y 轴标签 "Accuracy (%)" 和正文中的 "pp" (percentage points) 使用一致，但 MMLU 和 ARC-Challenge 图的 y 轴范围差异很大（MMLU: ~45-80%, ARC: ~30-75%），可能让读者在视觉上误判 effect size。

**M5** References 验证结果：58 条 bib 条目全部被正文引用，无 orphan 无 missing。OpenAlex 验证中 38 条 verified，12 条 mismatch（多为 first-author 姓名格式差异，非实质错误），8 条 not_found（多为较新 preprint 尚未被 OpenAlex 索引）。无虚假引用问题。

---

## 主要优势

1. **受控注入实验设计**：在 contamination 文献中，多数工作是观察性的（检测已存在的 leakage）。本文通过 controlled SFT injection 实现了对 dosage 的精确控制，使因果推断成为可能。这是相对于 Han et al. (2026) 的核心优势。

2. **"并非所有模型都被 inflate"的核心发现**：与社区默认假设（contamination = inflation）相反，论文展示了 Immune 甚至 Collapse 模式的存在（Table 1, Figure 1）。这对 benchmark reliability 的讨论有实质贡献。

3. **Cross-benchmark transfer 分析**（§5.2, Table 5, Appendix C）：发现 MMLU-targeted contamination 对 GSM8K 有 positive transfer（Benefit 家族）和 directional reversal（Collapse 家族），丰富了对 contamination 效应传播的理解。

4. **Signal failure characterization**（§5.6）：Min-K%++ 在低 dosage 处的 directional reversal（污染项得分反而低于干净项）是有实际价值的发现，对使用 membership inference 做 contamination detection 的实践者有直接指导意义。

5. **Appendix 的详尽程度**：11 页 Appendix 覆盖了 cross-benchmark details (A-C), signal reliability (D-E), IRT diagnostics (F-K), sensitivity analyses (L-Q), ARC results (U), dose-response parametric models (W) 等，展示了扎实的实验工程。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| ACL template | ✅ | 标准 ACL style (review mode) |
| Double-blind | ✅ | "Anonymous ACL submission"，正文无泄露 |
| 正文页数 | ✅ | Section 1-6 共 8 页（至 page 8），符合 ≤8 页限制 |
| Limitations | ✅ | Page 9，覆盖 scale (≤14.7B)、seed (n=3)、SFT vs pretraining、LoRA capacity 四个关键点，篇幅适当 |
| Ethics Statement | ✅ | Page 9，涵盖数据公开性、无人类受试者、潜在滥用 |
| References | ✅ | Pages 9-11，58 条，覆盖充分 |

---

## 总结

这篇论文问了一个好问题（contamination 是否对所有模型影响相同）并用精心设计的受控实验给出了 interesting 的回答（不同）。实验设计和执行质量较高。主要弱点在于：(1) 从 N=5 家族归纳 "taxonomy" 的统计基础不足，最 interesting 的两类模式仅 n=1；(2) ContamCal 在 MAE 上未超越 raw accuracy，削弱了方法的实用价值声称；(3) out-of-sample 验证仅覆盖了四类模式中最平凡的一类。如果作者能降级 taxonomy 声称并重新定位 ContamCal 为 diagnostic 而非 calibration 工具，论文的 soundness 会显著改善。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 846 · 2026-05-21T17:22:41.974471+00:00_

Reviewer 2 初审已返回（3.5/5 Borderline Conference）。核心问题：N=5 taxonomy 泛化不足、ContamCal MAE 逊于 raw accuracy、OOS 验证仅覆盖 Immune。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 79

## Round 79

2 recorded events


### User

_source line 847 · 2026-05-21T17:22:51.842907+00:00_

[Reviewer 2 审稿结果]:
临时图片清理受安全限制（仅允许清理 `_pdf_images` 目录），不影响审稿结果。审稿流程已完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 848 · 2026-05-21T17:22:59.180269+00:00_

Reviewer 2 审稿已完成，结果已收到。仍在等待 Reviewer 1 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 80

## Round 80

6 recorded events


### User

_source line 849 · 2026-05-21T17:29:15.586523+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 实验设计扎实、分类学新颖，但 J=16 导致的先验主导问题使 IRT 定量结论脆弱，AUGMENT 模式的数据量混淆因子和 Social Sciences 显著性不稳定需要补充讨论。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心方法论合理（受控注入 + IRT 框架），但 J=16 先验主导、PPP 值偏低、γ 参数化选择未充分论证 |
| Excitement | 3.5/5 | "污染≠通胀"的角度新颖且有实践价值，但分类学基于 n=3 seeds 的方向一致性，定量深度有限 |
| Reproducibility | 3.5/5 | 实验配置详细（LoRA 参数、Stan 推断设定），但代码/数据未提及公开计划；300/14042 item 选择标准需更明确 |
| Overall Assessment | 3.5/5 | 贡献真实且方向正确，需修补定量声明的稳健性 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] J=16 先验主导下的定量声明过强
- 具体位置：Section 3.3 (IRT 模型)、Section 5.5 (Calibration Quality)、Appendix K
- 问题：论文在 J=16 配置下拟合 2PL+γ 模型，Appendix K 明确承认 "the prior sensitivity confirms that J=16 provides insufficient data to override the prior, which reinforces the exploratory status of γ-based conclusions"（line 194）。具体表现为：
  - 后验均值跨先验变化 2.6×（0.34 → 0.89）
  - 50% CI over-coverage 达 83%（Section 5.5）
  - PPP = 0.16-0.25，远低于理想值 0.5
  
  然而主文仍使用这些 γ 估计作为关键发现：Social Sciences γ_ss = -0.63, P(γ<0) = 99.7%（Section 5.7）被表述为"crossing the Bonferroni-corrected threshold for eight tests"。但 Appendix K Table 10 在同一默认先验 N(0,1) 下仅得到 P(γ<0) = 98.48%，**未达到** Bonferroni 校正后阈值（8 次检验需 P > 99.375%）。两处数值的差异（99.7% vs 98.48%）在 ESS > 3800 的 MCMC 采样下不应归因于随机变异，说明 Bonferroni 显著性声明不稳健。
  
- 为什么影响接收：Domain-level heterogeneity 是论文四大贡献之一（Section 6: "Domain-level IRT reveals heterogeneity masked by aggregate scores (Social Sciences P(γ<0) = 99.7%)"）。如果该结论在模型重拟合后不可复现，核心贡献之一的可信度受损。
- 建议修改方向：
  1. 主文应明确将所有 γ 定量结论标记为 exploratory（与 Appendix K 一致）
  2. Social Sciences 结果应报告跨重拟合的 P(γ<0) 范围（如 98.5%-99.7%），而非单一值
  3. 将 Bonferroni 显著性声明降级为"approaching Bonferroni significance"或提供 bootstrap 重拟合验证
  4. 更清晰地区分稳健的定性发现（分类学方向一致性）与脆弱的定量估计（γ 值和 CI）
- 严重程度：**Must-Fix**

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] AUGMENT 模式引入训练数据量系统性混淆
- 具体位置：Section 4.1, Limitations
- 问题：AUGMENT 模式在基础 50,000 样本上**叠加**污染项目，导致不同剂量下总训练量不同：d000=50k, d005≈50.8k (+1.7%), d025≈54.1k (+8.3%), d050≈58.3k (+16.5%), d100=66.5k (+33.1%)。d050 和 d100 的数据量增长幅度足以产生独立于污染的训练效果。Limitations 中仅提到"AUGMENT mode differs from pretraining-stage leakage"，**未讨论数据量混淆**。
- 缓解因素：3/5 模型的剂量-反应方向（Phi-4 Immune、OLMo-2 Collapse、Qwen-14B Collapse）与"更多数据→更高准确率"预期相反，部分消解了混淆。Gemma-2（Benefit）和 Qwen-7B（V-recovery 的上升段）是混淆最可能影响解释的情况。
- 建议：
  1. 明确报告每个剂量的总训练集大小
  2. 讨论为何未采用 REPLACE 模式（等量替换基础数据）
  3. 在 Benefit 和 V-recovery 模式的讨论中添加数据量混淆的 caveat
- 严重程度：**Should-Fix**

**W2** [warning] 2PL+γ 参数化选择：γ 在 a_i 括号外的合理性未论证
- 具体位置：Section 3.3, Eq. (2)
- 问题：论文采用 P(y=1) = σ(a_i(θ_j - b_i) + γ_k · e_{ij})，其中 γ 在 discrimination 参数 a_i 的括号**外部**。标准 IRT-DIF 文献通常将协变量效应放在括号**内部**：σ(a_i(θ_j - b_i + γ_k · e_{ij}))。两种参数化有不同含义：
  - 论文版本：污染在 logit 尺度上产生恒定偏移，不受 item discrimination 调节。高区分度和低区分度的 item 受同等 logit 影响。
  - 标准版本：污染效应被 a_i 放大，高区分度 item 受更大 logit 影响，等价于能力尺度上的恒定偏移。
  
  论文提到"contamination shifts the effective difficulty of item i by γ_k · e_{ij} / a_i units on the ability scale"（Section 3.3），说明作者意识到该选择的含义，但未论证为何此参数化优于标准 DIF 形式。
- 建议：添加一段讨论两种参数化的选择理由，或提供对比实验。如果"全局能力调节"是主要机制（DiD 已支持），则标准参数化（inside-a_i）可能更合适。
- 严重程度：**Should-Fix**

**W3** [warning] MMLU PPP 值（0.16-0.25）的模型拟合问题讨论不足
- 具体位置：Section 5.5, Appendix K
- 问题：主文明确报告 ARC 的 PPP=0.003 并标注"should be interpreted with caution"，但 MMLU 的 PPP = 0.16-0.25 仅在 Appendix K 出现，主文未直接报告或讨论。PPP = 0.16-0.25 虽不如 ARC 严重，但仍显著低于理想值 0.5，表明 2PL+γ 模型未完全捕获 MMLU 数据结构。可能的遗漏因素包括：item-level 异质性（不同 item 的污染易感性）、guessing 效应（4PL 仅在 J≥16 时使用）、domain 内部异质性等。
- 建议：在主文中报告 MMLU PPP 值并讨论模型可能未捕获的数据特征。
- 严重程度：**Should-Fix**

**W4** [warning] LoRA r=16 统一配置的参数比例混淆
- 具体位置：Section 4.1, Limitations
- 问题：LoRA r=16 对 14.7B 模型（Phi-4、Qwen-14B）和 7B 模型产生不同的可训练参数比例——14.7B 模型的参数比例约为 7B 的一半。Limitations 中提到"Unified LoRA rank (r = 16) yields a parameter fraction inversely proportional to model size"，并以 Phi-4（Immune）vs Qwen-14B（Collapse）的对比论证 rank 非唯一驱动因素。这一论证有效但不完整：两模型架构不同（Phi-4 vs Qwen），混淆因素包括架构、预训练数据等。
- 建议：报告每个模型的实际可训练参数比例（trainable/total %），并讨论 matched-ratio 设计是否可行。
- 严重程度：**Should-Fix**

**W5** [warning] 300/14,042 MMLU item 选择的代表性
- 具体位置：Section 5.5
- 问题：IRT 模型仅在 300 个 RRF-filtered items 上拟合（占 MMLU 总量的 2.1%），选择标准为 exposure score 方差最大化。这是统计必要性（γ 可辨识性需要 exposure 方差），但引入了选择偏差：γ 估计仅反映高 exposure 变异 items 上的污染效应，不一定代表整个基准测试。低 exposure 变异 items（如所有模型一致高/低 exposure）的污染效应可能不同。
- 建议：讨论 300-item 子集的代表性，或报告使用不同 item 子集（如 top-500, top-200）时 γ 估计的稳定性。
- 严重程度：**Should-Fix**

---

## 小问题（不影响接收）

- **M1** [minor] Section 3.2: RRF 融合与学习型融合方法（如 logistic regression on signals）的对比缺失。RRF 是 rank-based 且不学习权重，可能次优。不过信号正交性（Appendix E, ρ < 0.06）和 leave-one-out 消融（Table 8）提供了充分支持。
- **M2** [minor] Section 4.1: 5 个剂量水平（0%, 5%, 25%, 50%, 100%）间距非均匀。5% 到 25% 之间的跳跃较大，可能遗漏中间剂量的拐点行为。对 V-recovery 模式的表征尤其可能受影响（需要 10%、15% 等中间点确认 V 形最低点位置）。
- **M3** [minor] Section 5.3: n=3 seeds 的 CI 宽度 1.5-14.5pp 限制了形状一致性的统计推断。论文正确使用方向一致性而非统计显著性作为分类依据，但 Appendix W 的参数化模型（Hill 等）因 n=3 不够也未能提供有力的补充推断。
- **M4** [minor] Algorithm 1 参数（τ=2pp, σ=5pp, ρ=0.3, λ=0.5pp）无理论推导。Table 14 的 30-combination grid sweep 已验证稳健性（100% 分类稳定），但阈值设定的原理可简要说明。
- **M5** [minor] Appendix C: GSM8K 评估使用 max_new_tokens=256，可能截断 chain-of-thought。论文已在附录中适当 caveat，主文应提及此限制。

---

## Director 指定的 11 项逐项评级

| # | 审查点 | 评级 | 核心理由 |
|---|--------|------|---------|
| 1 | RRF 多信号融合 | Minor | 信号正交性充分（ρ<0.06），消融实验充分 |
| 2 | 2PL+γ 加性线性假设 | Should-Fix | γ 在 a_i 外的参数化未与标准 DIF 对比论证 |
| 3 | γ 可辨识性 J≥50 vs J=16 | Should-Fix (含在 N1) | 模拟结论条件合理但实际 CI 行为与模拟矛盾 |
| 4 | Bayesian 推断 | Must-Fix (N1) | 先验主导 + PPP 偏低 + P(γ<0) 不可复现 |
| 5 | LoRA r=16 公平性 | Should-Fix (W4) | 参数比例混淆已部分缓解但未定量报告 |
| 6 | 剂量设计 + AUGMENT | Should-Fix (W1) | 数据量混淆在 d050/d100 显著，未被讨论 |
| 7 | 跨种子稳定性 n=3 | Minor (M3) | 适当 caveat，方向一致性标准合理 |
| 8 | 跨基准迁移因果推断 | Minor (M5) | 评估配置差异已 caveat |
| 9 | DiD 分析 | Acceptable | MDES 正确计算和解读，ARC 适当标注 |
| 10 | Domain-level Bonferroni | Should-Fix (含在 N1) | 校正方法正确但 P(γ<0) 数值不稳健 |
| 11 | Algorithm 1 参数敏感性 | Minor (M4) | Grid sweep 充分，缺理论推导为小问题 |

---

## 主要优势

- **受控实验设计**：跨 4 个独立模型家族的 5 级剂量 SFT 注入，是该方向首个系统性受控研究。实验规模（50+ checkpoints）和跨基准验证（MMLU/ARC/GSM8K）充分。
- **核心洞见有价值**："污染≠通胀"的发现（Immune/Collapse/V-recovery/Benefit 四模式分类学）对 leaderboard 解读和模型评估实践有直接影响。
- **统计方法论透明度高**：论文诚实报告了 CI over-coverage、PPP 值、MDES 功效分析、先验敏感度等局限。Appendix K 中"exploratory status"的表述是负责任的做法。
- **DiD 分析严谨**：treated vs untreated items 的差分-差分检验逻辑清晰，MDES 的功效-bounded 解读准确，ARC 的 caveat 恰当。
- **信号正交性验证**：Appendix E 的 pairwise Spearman ρ < 0.06 和 leave-one-out 消融为 RRF 融合提供了可信支持。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-21T17:29:59.881533+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 审稿报告（完整原文）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Taxonomy 从 N=5 过度泛化，统计基础不足\n- 四类分类（Immune, Collapse, V-recovery, Benefit）建立在仅 5 个模型家族之上。Collapse 仅 Qwen-14B（n=1），V-recovery 仅 Qwen-7B（n=1）。Abstract 称 \"four qualitatively different dose-response patterns\"，Introduction 称 \"taxonomy\"——从统计角度 n=1 类别不能构成 generalizable taxonomy。Qwen-7B 和 Qwen-14B 来自同一家族（Qwen2.5），Collapse 和 V-recovery 可能是 Qwen 家族的特异性行为。\n\n**N2** [critical] ContamCal 校准 MAE 不优于 Raw Accuracy（Table 4）\n- Table 4: B0 Raw Accuracy MAE=0.006，ContamCal (2PL+γ) MAE=0.009。核心方法在最基本的校准指标上未超越\"什么都不做\"的 baseline。论文解释为 \"within-family ≤3B effects are near-null\"，但这说明 ContamCal 在多数模型上没有价值——而在确实受影响的模型（Qwen-14B）上的单独评估未在 Table 4 中呈现。\n\n**N3** [critical] Out-of-sample 验证仅覆盖 Immune 一种模式（最不 interesting 的一类）\n- LLaMA-3.1-8B 被分类为 Immune——最容易验证的模式。Collapse、V-recovery、Benefit 三类均未有 OOS 验证。Section 6 称 \"Two of four patterns attested in ≥2 independent families\"——但 Benefit 的两个实例（OLMo-2, Gemma-2）都在 construction 家族中，不算 OOS。\n\n### Should-Fix 问题\n\n**W1** [warning] ARC PPP=0.003 模型拟合不良仅在 Appendix 讨论\n- ARC 的 PPP=0.003 表明 2PL+γ 模型严重拟合不良。将这个问题仅放在 Appendix 中讨论有选择性报告之嫌。\n\n**W2** [warning] 方法新颖性定位不够诚实\n- 2PL+γ 本质上是标准 explanatory IRT/DIF。论文未明确说明\"我们的方法在 IRT 建模层面无技术新颖性，新颖性在于受控注入实验设计和实证发现\"。\n\n**W3** [warning] 与 Han et al. (2026) 和 Schaeffer et al. (2026) 的比较不充分\n- Han et al. 也用 DIF 量化 contamination，Schaeffer et al. 做 pretraining-stage 受控注入。比较停留在一句话层面。\n\n**W4** [warning] Contribution 声明遗漏 ContamCal 框架本身\n- 三个 contributions 不含 ContamCal 本身。考虑到方法占了 Section 3 整两页，这个遗漏令人困惑。如果是因为 Table 4 结果导致有意不列——反而暗示作者自己也认为校准表现不够好。\n\n### Minor 问题\n\n**M1** 术语不一致：\"taxonomy\"/\"profiles\"/\"patterns\" 交替使用。\n**M2** Contribution 2 本质是 null result，Abstract 表述可能误导。\n**M3** Algorithm 1 阈值无理论推导，正文未指向 Appendix P 验证。\n**M4** Figure 1 y 轴范围差异可能误判 effect size。\n**M5** References 验证：58 条全部被引用，无虚假引用。\n\n---\n\n请对以上每个问题（N1-N3, W1-W4, M1-M5）逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 审稿报告（完整原文）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Taxonomy 从 N=5 过度泛化，统计基础不足\n- 四类分类（Immune, Collapse, V-recovery, Benefit）建立在仅 5 个模型家族之上。Collapse 仅 Qwen-14B（n=1），V-recovery 仅 Qwen-7B（n=1）。Abstract 称 \"four qualitatively different dose-response patterns\"，Introduction 称 \"taxonomy\"——从统计角度 n=1 类别不能构成 generalizable taxonomy。Qwen-7B 和 Qwen-14B 来自同一家族（Qwen2.5），Collapse 和 V-recovery 可能是 Qwen 家族的特异性行为。\n\n**N2** [critical] ContamCal 校准 MAE 不优于 Raw Accuracy（Table 4）\n- Table 4: B0 Raw Accuracy MAE=0.006，ContamCal (2PL+γ) MAE=0.009。核心方法在最基本的校准指标上未超越\"什么都不做\"的 baseline。论文解释为 \"within-family ≤3B effects are near-null\"，但这说明 ContamCal 在多数模型上没有价值——而在确实受影响的模型（Qwen-14B）上的单独评估未在 Table 4 中呈现。\n\n**N3** [critical] Out-of-sample 验证仅覆盖 Immune 一种模式（最不 interesting 的一类）\n- LLaMA-3.1-8B 被分类为 Immune——最容易验证的模式。Collapse、V-recovery、Benefit 三类均未有 OOS 验证。Section 6 称 \"Two of four patterns attested in ≥2 independent families\"——但 Benefit 的两个实例（OLMo-2, Gemma-2）都在 construction 家族中，不算 OOS。\n\n### Should-Fix 问题\n\n**W1** [warning] ARC PPP=0.003 模型拟合不良仅在 Appendix 讨论\n- ARC 的 PPP=0.003 表明 2PL+γ 模型严重拟合不良。将这个问题仅放在 Appendix 中讨论有选择性报告之嫌。\n\n**W2** [warning] 方法新颖性定位不够诚实\n- 2PL+γ 本质上是标准 explanatory IRT/DIF。论文未明确说明\"我们的方法在 IRT 建模层面无技术新颖性，新颖性在于受控注入实验设计和实证发现\"。\n\n**W3** [warning] 与 Han et al. (2026) 和 Schaeffer et al. (2026) 的比较不充分\n- Han et al. 也用 DIF 量化 contamination，Schaeffer et al. 做 pretraining-stage 受控注入。比较停留在一句话层面。\n\n**W4** [warning] Contribution 声明遗漏 ContamCal 框架本身\n- 三个 contributions 不含 ContamCal 本身。考虑到方法占了 Section 3 整两页，这个遗漏令人困惑。如果是因为 Table 4 结果导致有意不列——反而暗示作者自己也认为校准表现不够好。\n\n### Minor 问题\n\n**M1** 术语不一致：\"taxonomy\"/\"profiles\"/\"patterns\" 交替使用。\n**M2** Contribution 2 本质是 null result，Abstract 表述可能误导。\n**M3** Algorithm 1 阈值无理论推导，正文未指向 Appendix P 验证。\n**M4** Figure 1 y 轴范围差异可能误判 effect size。\n**M5** References 验证：58 条全部被引用，无虚假引用。\n\n---\n\n请对以上每个问题（N1-N3, W1-W4, M1-M5）逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-21T17:30:21.183147+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21301
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-21T17:30:21.334040+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 审稿报告（完整原文）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] J=16 先验主导下的定量声明过强\n- J=16 配置下，Appendix K 承认 \"J=16 provides insufficient data to override the prior\"。后验均值跨先验变化 2.6×（0.34→0.89）。50% CI over-coverage 达 83%。PPP=0.16-0.25。\n- 但主文仍使用 Social Sciences γ_ss=-0.63, P(γ<0)=99.7% 并声称 \"crossing the Bonferroni-corrected threshold\"。\n- 然而 Appendix K Table 10 在同一默认先验 N(0,1) 下仅得到 P(γ<0)=98.48%，**未达到** Bonferroni 阈值（8 次检验需 P>99.375%）。两处数值差异（99.7% vs 98.48%）不应归因于 MCMC 随机变异（ESS>3800）。\n- 建议：(1) 标记所有 γ 结论为 exploratory；(2) 报告 P(γ<0) 范围而非单一值；(3) 降级 Bonferroni 显著性声明。\n\n### Should-Fix 问题\n\n**W1** [warning] AUGMENT 模式引入训练数据量系统性混淆\n- AUGMENT 模式导致 d000=50k, d005≈50.8k(+1.7%), d100=66.5k(+33.1%)。d050/d100 的数据量增长幅度足以产生独立于污染的训练效果。Limitations 未讨论数据量混淆。\n- 缓解因素：3/5 模型方向与\"更多数据→更高准确率\"预期相反。但 Gemma-2（Benefit）和 Qwen-7B（V-recovery 上升段）是混淆最可能影响解释的情况。\n\n**W2** [warning] 2PL+γ 参数化选择：γ 在 a_i 括号外的合理性未论证\n- 论文采用 σ(a_i(θ_j-b_i)+γ_k·e_{ij})，γ 在 a_i 外部。标准 IRT-DIF 通常将协变量放在内部：σ(a_i(θ_j-b_i+γ_k·e_{ij}))。两种参数化含义不同：论文版本=logit 恒定偏移，标准版本=能力尺度恒定偏移。论文提到 \"shifts effective difficulty by γ·e/a_i\" 说明作者意识到差异，但未论证选择理由。\n\n**W3** [warning] MMLU PPP 值（0.16-0.25）模型拟合问题讨论不足\n- 主文明确报告 ARC PPP=0.003，但 MMLU PPP=0.16-0.25 仅在 Appendix K 出现。PPP 虽不如 ARC 严重但显著低于理想值 0.5。\n\n**W4** [warning] LoRA r=16 统一配置的参数比例混淆\n- 14.7B 模型参数比例约为 7B 的一半。Limitations 论证有效但不完整（Phi-4 vs Qwen-14B 来自不同家族，混淆因素多）。建议报告实际可训练参数比例。\n\n**W5** [warning] 300/14,042 MMLU item 选择的代表性\n- IRT 模型仅在 300 个 RRF-filtered items 上拟合（2.1%）。选择标准为 exposure score 方差最大化，引入选择偏差。低 exposure 变异 items 的污染效应可能不同。\n\n### Minor 问题\n\n**M1** RRF 融合 vs 学习型方法对比缺失，但正交性和消融已充分支持。\n**M2** 5 个剂量水平间距非均匀，5%→25% 跳跃可能遗漏拐点。\n**M3** n=3 seeds CI 宽度 1.5-14.5pp 限制推断，但方向一致性标准合理。\n**M4** Algorithm 1 参数无理论推导，Grid sweep 已验证。\n**M5** GSM8K max_new_tokens=256 截断 CoT，已在附录 caveat，主文应提及。\n\n---\n\n请对以上每个问题（N1, W1-W5, M1-M5）逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 审稿报告（完整原文）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] J=16 先验主导下的定量声明过强\n- J=16 配置下，Appendix K 承认 \"J=16 provides insufficient data to override the prior\"。后验均值跨先验变化 2.6×（0.34→0.89）。50% CI over-coverage 达 83%。PPP=0.16-0.25。\n- 但主文仍使用 Social Sciences γ_ss=-0.63, P(γ<0)=99.7% 并声称 \"crossing the Bonferroni-corrected threshold\"。\n- 然而 Appendix K Table 10 在同一默认先验 N(0,1) 下仅得到 P(γ<0)=98.48%，**未达到** Bonferroni 阈值（8 次检验需 P>99.375%）。两处数值差异（99.7% vs 98.48%）不应归因于 MCMC 随机变异（ESS>3800）。\n- 建议：(1) 标记所有 γ 结论为 exploratory；(2) 报告 P(γ<0) 范围而非单一值；(3) 降级 Bonferroni 显著性声明。\n\n### Should-Fix 问题\n\n**W1** [warning] AUGMENT 模式引入训练数据量系统性混淆\n- AUGMENT 模式导致 d000=50k, d005≈50.8k(+1.7%), d100=66.5k(+33.1%)。d050/d100 的数据量增长幅度足以产生独立于污染的训练效果。Limitations 未讨论数据量混淆。\n- 缓解因素：3/5 模型方向与\"更多数据→更高准确率\"预期相反。但 Gemma-2（Benefit）和 Qwen-7B（V-recovery 上升段）是混淆最可能影响解释的情况。\n\n**W2** [warning] 2PL+γ 参数化选择：γ 在 a_i 括号外的合理性未论证\n- 论文采用 σ(a_i(θ_j-b_i)+γ_k·e_{ij})，γ 在 a_i 外部。标准 IRT-DIF 通常将协变量放在内部：σ(a_i(θ_j-b_i+γ_k·e_{ij}))。两种参数化含义不同：论文版本=logit 恒定偏移，标准版本=能力尺度恒定偏移。论文提到 \"shifts effective difficulty by γ·e/a_i\" 说明作者意识到差异，但未论证选择理由。\n\n**W3** [warning] MMLU PPP 值（0.16-0.25）模型拟合问题讨论不足\n- 主文明确报告 ARC PPP=0.003，但 MMLU PPP=0.16-0.25 仅在 Appendix K 出现。PPP 虽不如 ARC 严重但显著低于理想值 0.5。\n\n**W4** [warning] LoRA r=16 统一配置的参数比例混淆\n- 14.7B 模型参数比例约为 7B 的一半。Limitations 论证有效但不完整（Phi-4 vs Qwen-14B 来自不同家族，混淆因素多）。建议报告实际可训练参数比例。\n\n**W5** [warning] 300/14,042 MMLU item 选择的代表性\n- IRT 模型仅在 300 个 RRF-filtered items 上拟合（2.1%）。选择标准为 exposure score 方差最大化，引入选择偏差。低 exposure 变异 items 的污染效应可能不同。\n\n### Minor 问题\n\n**M1** RRF 融合 vs 学习型方法对比缺失，但正交性和消融已充分支持。\n**M2** 5 个剂量水平间距非均匀，5%→25% 跳跃可能遗漏拐点。\n**M3** n=3 seeds CI 宽度 1.5-14.5pp 限制推断，但方向一致性标准合理。\n**M4** Algorithm 1 参数无理论推导，Grid sweep 已验证。\n**M5** GSM8K max_new_tokens=256 截断 CoT，已在附录 caveat，主文应提及。\n\n---\n\n请对以上每个问题（N1, W1-W5, M1-M5）逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-21T17:30:22.646687+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1312
}
```

</details>

---


### Assistant

_source line 854 · 2026-05-21T17:30:27.508499+00:00_

交叉分享已派发。两位 Reviewer 正在阅读对方的完整审稿意见并准备逐条回应。等待交叉回应返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 81

## Round 81

6 recorded events


### User

_source line 855 · 2026-05-21T17:30:30.057988+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心结论：

- **Overall 3.5 (Borderline Conference)**
- **1 个 Must-Fix**：J=16 先验主导问题——后验均值跨先验变化 2.6×，Social Sciences P(γ<0) 在主文（99.7%）与 Appendix K（98.48%）间存在差异，Bonferroni 显著性声明不稳健
- **5 个 Should-Fix**：AUGMENT 数据量混淆、γ 参数化选择未论证、MMLU PPP 值讨论不足、LoRA 参数比例未报告、300-item 子集代表性
- **5 个 Minor**：RRF 融合对比、剂量间距、n=3 seeds、Algorithm 1 参数理论依据、GSM8K 评估限制

论文的定性贡献（4 模式分类学、DiD 无 item-specific 记忆）稳健且有价值，但 IRT 定量结论在当前 ensemble size 下应明确标记为 exploratory。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-21T17:30:35.338837+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
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

_source line 857 · 2026-05-21T17:30:35.389439+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-21T17:30:41.411427+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'in_progress', 'activeForm': 'Collecting cross-sharing responses (waiting for Reviewer 2)'}, {'content': 'Step 3: Convergence judgment', 'status': 'pending', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'pending', 'activeForm': 'Synthesizing final report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'in_progress', 'activeForm': 'Collecting cross-sharing responses (waiting for Reviewer 2)'}, {'content': 'Step 3: Convergence judgment', 'status': 'pending', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'pending', 'activeForm': 'Synthesizing final report'}]"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-21T17:30:41.462151+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 860 · 2026-05-21T17:30:44.248125+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 82

## Round 82

4 recorded events


### User

_source line 861 · 2026-05-21T17:32:23.085473+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Taxonomy 从 N=5 过度泛化**

同意这是一个实质性问题。Collapse（仅 Qwen-14B, n=1）和 V-recovery（仅 Qwen-7B, n=1）均来自同一 Qwen2.5 家族，无法排除是 Qwen 架构特异性行为。论文 Section 6 称 "Two of four patterns attested in ≥2 independent families"——但这也意味着另外两类仅各有 1 个家族支持。

不过需补充两点缓解因素：
1. 论文 Appendix P (Table 14) 的分类稳健性分析表明所有分类在 30 种参数组合下 100% 稳定，排除了分类边界偶然性。
2. 论文标题用 "Profiling"（剖析）而非 "Establishing a taxonomy"（建立分类学），措辞上预留了探索性空间。

建议：Abstract 和 Introduction 中 "taxonomy" 一词应替换为更审慎的表述（如 "typology observed in our sample"），并在 Limitations 中明确承认 n=1 类别不可泛化。

---

**[REBUT] R2-N2: ContamCal 校准 MAE 不优于 Raw Accuracy**

R2 的批评建立在对 ContamCal 设计目标的误读之上。论文在 Section 3.3（Identifiability 段，method.tex line 52-54）中**明确预测并解释了**这一结果：

> "Eq. (2) depends on θ_j, not γ directly, predicting that vanilla 2PL (γ=0) achieves comparable calibration to 2PL+γ, with γ_k serving **diagnosis rather than calibration** (§5.5)."

即：γ 参数在数学上不影响 calibrated score（Eq. 3 中 e_{ij}=0），ContamCal 的价值在于**诊断**（检测哪些 domain 受污染影响、quantify 效应方向和大小），而非数值校准。Table 4 的 MAE 对比恰恰验证了这一理论预测——这是方法论一致性的体现，不是缺陷。

Section 5.5 进一步展示了诊断价值：pooled γ 不显著，但 domain-level 分析揭示 Social Sciences γ_ss = -0.63（Section 5.7），这一发现是 Raw Accuracy 无法提供的。

R2 称 "在确实受影响的模型上的单独评估未在 Table 4 中呈现" 有一定道理。但 Table 4 的设计是 within-family ≤3B（低影响区间），恰好是最保守的测试场景。在高影响模型（如 Qwen-14B Collapse）上，calibrated score 与 raw score 的差异会更大，论文可补充此数据。

---

**[AGREE] R2-N3: OOS 验证仅覆盖 Immune**

同意。LLaMA-3.1-8B 仅验证了 Immune 模式——四种模式中最"无趣"且最易验证的一种。更关键的 Collapse、V-recovery、Benefit 均缺乏独立家族的 OOS 验证。

R2 关于 Benefit 的指出尤其有力：OLMo-2 和 Gemma-2 都是 construction 家族，不构成真正的 OOS 验证。

需要注意的是，论文在 Limitations（page 9）中并未将此列为局限。考虑到受控 SFT 注入实验成本高（每个家族需训练 5 个剂量 × 多个 seed），获取更多 OOS 验证在实践上有难度——但这应被明确承认。

---

### Should-Fix 问题

**[REBUT] R2-W1: ARC PPP=0.003 仅在 Appendix 讨论**

R2 的事实陈述有误。ARC 的 PPP=0.003 **明确出现在主文 Section 5.5** 中：

> "ARC 50% intervals under-cover (45%), driven by structural misfit (PPP=0.003; ARC IRT results should be interpreted with caution)."

这句话同时报告了 PPP 值、诊断了原因（structural misfit）、并给出了解读建议（interpret with caution）。论文在这一点上的处理是透明和负责任的。

不过，我在自己的审稿中指出了一个相关但不同的问题（我的 W3）：MMLU 的 PPP=0.16-0.25 **仅在 Appendix K 出现**，主文未直接报告。这一遗漏比 ARC 的情况更值得关注，因为 MMLU 是论文的核心分析基准。

---

**[AGREE] R2-W2: 方法新颖性定位**

同意 2PL+γ 本质上是 explanatory IRT 在 LLM 评估中的应用，IRT 建模层面无技术创新。论文应更明确地定位新颖性来源：(1) 受控注入实验设计，(2) exposure score 的多信号 RRF 融合（Stage 1），(3) 实证发现（dose-response 多样性），而非暗示 IRT 模型本身是贡献。

补充：我的审查中也注意到（我的 W2），论文采用的 γ 在 a_i 括号外的参数化形式 σ(a_i(θ_j - b_i) + γ_k · e_{ij}) 与标准 DIF 文献的 σ(a_i(θ_j - b_i + γ_k · e_{ij})) 不同，但未论证选择理由——如果要声称方法贡献，这一差异需要讨论。

---

**[AGREE] R2-W3: 与 Han et al. (2026) 和 Schaeffer et al. (2026) 比较不充分**

同意。Han et al. 也使用 DIF 量化污染效应，是最直接的方法论对比对象。Schaeffer et al. 做 pretraining-stage 受控注入，是实验设计层面的对比对象。Section 2 的讨论停留在一句话提及，缺乏以下关键对比维度：
- Han et al.: DIF 参数化差异（是否使用 exposure score 作为连续协变量？还是二分 group？）
- Schaeffer et al.: pretraining-stage 注入 vs SFT 注入的可比性和局限性

Appendix U（ARC IRT Results）和 Table 17-18 有部分 baseline 对比，但不等同于与这两篇工作的方法论深度比较。

---

**[REBUT] R2-W4: Contribution 声明遗漏 ContamCal**

R2 的观察有部分道理，但推断有误。重新审查 Introduction（page 2），论文的贡献列表实际包含：

1. Dose-response patterns with cross-seed and cross-benchmark validation
2. No detectable item-specific memorization at current power levels
3. "We further characterize contamination detection signal failure..."（信号失效特征化）

且紧接贡献列表之前有明确表述："we provide the statistical machinery for this characterization"——ContamCal 被定位为实现上述发现的**工具**，而非独立贡献。这一定位选择与 R2-N2 中 Table 4 结果的讨论是一致的：如果校准能力不优于 baseline，单独列为贡献确实缺乏支撑。

R2 的推断"反而暗示作者自己也认为校准表现不够好"过度解读了。更合理的解释是：论文的核心贡献是实证发现（dose-response profiling），ContamCal 是方法手段而非目的。

---

### Minor 问题

**[AGREE] R2-M1: 术语不一致**
"taxonomy" / "profiles" / "patterns" 混用确实降低了表述精确度。建议统一使用 "dose-response profiles" 指代具体模式，"classification" 指代 Algorithm 1 的输出，避免 "taxonomy"（含泛化意味）。

**[REBUT] R2-M2: Contribution 2（null result）Abstract 误导**
Null result 在功效分析约束下是合法的实证贡献。论文 Abstract 称 "no item-specific memorization detected at MDES 1.2-2.0pp"（含功效上界），Appendix N 的 post-hoc MDES 计算（Table 12-13）严格界定了 null 的含义。这比简单声称 "无记忆化" 更诚实。不过，Abstract 中 "mean ∆ < 1 percentage point" 的表述确实可能被快速阅读为 "effect < 1pp"（而实际是 "detected effect < 1pp at limited power"），建议添加 "within detectable limits" 等修饰语。

**[REBUT] R2-M3: Algorithm 1 阈值无理论推导，正文未指向 Appendix P**
R2 事实陈述有误。Section 3.4（page 4-5）明确写道：

> "All thresholds are explicit and adjustable; a 30-combination grid sweep confirms all families are stable across all (τ, σ) combinations (180/180 model-seed-threshold pairs; **Appendix P**)."

主文直接引用了 Appendix P。缺乏理论推导是事实（我的 M4 也指出了这一点），但"正文未指向 Appendix P"的说法不成立。

**[AGREE] R2-M4: Figure 1 y 轴范围差异**
同意。MMLU 面板 y 轴约 45-80%，ARC-Challenge 面板约 45-80%（但 baseline 分布不同），视觉上可能夸大或缩小某些模型的 effect size。建议标注 y 轴范围或使用统一范围。

**[AGREE] R2-M5: 引用验证**
58 条引用全部被引用、无虚假引用是好消息，确认论文引用规范。

---

### 总结

R2 的 12 个问题中：
- **4 个 AGREE**（N1 taxonomy 过度泛化、N3 OOS 不足、W2 新颖性定位、W3 相关工作对比）
- **4 个 REBUT**（N2 MAE 误读设计目标、W1 事实错误 PPP 在主文、W4 过度推断、M3 事实错误 Appendix P 已引用）
- **3 个 AGREE with nuance**（M1 术语、M4 y 轴、M5 引用）
- **1 个 partial REBUT**（M2 null result 表述可改进但非误导）

R2 最有力的两个问题是 **N1**（n=1 分类泛化）和 **N3**（OOS 仅覆盖 Immune），这两点我在自己的审稿中未充分强调——N1 对论文 framing 的影响比我的评估更严重，建议作者认真对待。R2 最弱的两个问题是 **W1**（PPP 在主文已报告）和 **M3**（Appendix P 在主文已引用），均存在事实错误。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-21T17:32:30.721505+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'in_progress', 'activeForm': 'Collecting cross-sharing responses (Reviewer 1 done, waiting for Reviewer 2)'}, {'content': 'Step 3: Convergence judgment', 'status': 'pending', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'pending', 'activeForm': 'Synthesizing final report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'in_progress', 'activeForm': 'Collecting cross-sharing responses (Reviewer 1 done, waiting for Reviewer 2)'}, {'content': 'Step 3: Convergence judgment', 'status': 'pending', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'pending', 'activeForm': 'Synthesizing final report'}]"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-21T17:32:30.772237+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 864 · 2026-05-21T17:32:33.418890+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 83

## Round 83

2 recorded events


### User

_source line 865 · 2026-05-21T17:32:35.911504+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 12 个问题中，4 个同意（N1 分类泛化、N3 OOS 不足、W2 新颖性定位、W3 相关工作对比），4 个反驳（N2 MAE 误读设计目标、W1/M3 事实错误、W4 过度推断），其余 4 个带细微差别的同意/反驳。R2 最有力的发现是 N1 和 N3，我自己的 Round 1 审稿中对这两点关注不够。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 866 · 2026-05-21T17:32:40.821727+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 84

## Round 84

16 recorded events


### User

_source line 867 · 2026-05-21T17:34:06.539756+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## N1: J=16 先验主导下的定量声明过强

**[AGREE] R1-N1**: 这是本轮审稿中最精准的技术发现之一。

我核实了 R1 指出的数值不一致问题：Section 5.7 (p.8) 报告 Social Sciences γ_ss=−0.63, P(γ<0)=99.7%，并声称 "crossing the Bonferroni-corrected threshold for eight tests"。但 Appendix K Table 10 (p.15) 在同一默认先验 N(0,1) 下显示 γ̂=−0.497, P(γ<0)=98.48%。这存在两层问题：

1. **数值不一致**：γ 估计值本身差异显著（−0.63 vs −0.497），P(γ<0) 差异 1.2 个百分点（99.7% vs 98.48%）。R1 正确指出 ESS>3800 排除了 MCMC 随机变异的解释。这表明 Section 5.7 与 Table 10 可能使用了不同的模型配置，但论文未说明差异来源。

2. **Bonferroni 显著性声明不成立**：8 次检验的 Bonferroni 校正阈值为 P>99.375%。Table 10 的 98.48% 明显未达标。即使取 Table 10 最宽松先验 N(0,2) 的 P(γ<0)=98.95%，仍未达标。论文在先验敏感性分析自己揭示了这一问题（"P(γ<0) ≥ 97.95% in all cases"），但 Section 5.7 仍做出了 Bonferroni 显著的声明——这构成了定量层面的 inconsistency。

R1 的三点建议——标记为 exploratory、报告 P(γ<0) 范围、降级 Bonferroni 声明——我全部赞同。这应是 Must-Fix 而非 Should-Fix。

---

## W1: AUGMENT 模式引入训练数据量系统性混淆

**[AGREE] R1-W1**: 混淆真实存在，但需补充一点缓解证据。

R1 的计算正确：AUGMENT 模式下 d000=50k→d100≈66.5k (+33.1%)。这意味着高 dosage 配置的准确率提升可能部分归因于更多训练数据，而非污染本身。

**缓解因素**（R1 已部分提及）：
- Section 5.4 的 DID 分析（Table 3）显示所有家族在 d025 处 treated vs untreated items 的 DID 均不显著（p>.05）。这意味着在 item level 上，被注入的题目并未比未注入题目获得更多增益——如果准确率提升纯粹来自数据量，treated 和 untreated 应同等受益，这正是 DID 观察到的模式。
- 但 R1 正确指出，DID 仅控制了 item-level 混淆。在 **aggregate level**（Figure 1 的剂量-反应曲线），数据量混淆仍然存在：Benefit 模式（OLMo-2, Gemma-2）的准确率增益无法与"更多训练数据的通用效应"完全分离。

**R1 额外指出的关键漏洞**：Limitations (p.9) 未提及数据量混淆。这确实是一个疏忽——论文讨论了 SFT vs pretraining、seed 数量、LoRA capacity、scale，但没有讨论 AUGMENT 模式的数据量效应。

建议在 Limitations 中增加一句：AUGMENT 模式下高 dosage 配置的数据量增加（d100 较 d000 多 33%）构成潜在混淆，尤其可能影响 Benefit 模式的解释。REPLACE 模式可作为未来消歧实验。

---

## W2: 2PL+γ 参数化选择——γ 在 a_i 括号外的合理性

**[AGREE] R1-W2**: 技术观察精准，论文确实缺乏论证。

Section 3.3 (p.4) 的方程：P(y_{ij}=1) = σ(a_i(θ_j − b_i) + γ_k · e_{ij})

标准 IRT-DIF 参数化通常为：σ(a_i(θ_j − b_i + γ · e_{ij})) = σ(a_i·θ_j − a_i·b_i + a_i·γ·e_{ij})

两种选择的实质差异：
- **论文版本**：γ 在 logit 尺度上产生恒定偏移，不受 item discrimination (a_i) 调节。高辨别力题目和低辨别力题目受到相同的 logit 偏移。
- **标准版本**：γ 在 ability 尺度上产生恒定偏移，高辨别力题目的 logit 偏移更大。

论文承认 "shifts effective difficulty by γ·e/a_i"（即有效难度偏移随 a_i 递减），说明作者意识到了差异。但未回答：**为什么相信 contamination 对高辨别力和低辨别力题目的 logit 效应相同？** 从直觉上，高辨别力题目对能力变化更敏感，如果 contamination 相当于能力虚增，则标准参数化可能更合理。

这不影响定性结论（方向和模式分类），但影响 γ 的数值解释和跨 item 比较。

---

## W3: MMLU PPP 值（0.16-0.25）模型拟合问题讨论不足

**[AGREE] R1-W3**: 补充我自己的发现。

我在 Round 1 审稿中已将 ARC PPP=0.003 列为 Should-Fix (W1)，指出其仅在 Appendix U 讨论。R1 进一步发现 MMLU PPP=0.16-0.25（Appendix K Table 10）也低于理想值 0.5。

这意味着论文的核心模型在**两个** benchmark 上都存在拟合问题：
- ARC：PPP=0.003（严重拟合不良，论文已在正文 caveat）
- MMLU：PPP=0.16-0.25（中度拟合不良，仅在 Appendix K 提及）
- GSM8K：论文未报告 PPP（可能是因为使用不同评估方式）

仅 GSM8K 的拟合状况未知。对于一个以 IRT 模型为核心方法的论文，三个 benchmark 中两个存在拟合问题是值得在正文讨论的——哪怕只是一句 caveat。

---

## W4: LoRA r=16 统一配置的参数比例混淆

**[AGREE] R1-W4**: 部分同意，但论文的反驳有一定效力。

R1 正确指出 r=16 的可训练参数比例随模型大小递减。报告实际可训练参数比例是合理的透明性要求。

但论文 Limitations (p.9) 的反驳值得引用："Qwen-14B's collapse at the same scale argues against a purely capacity-based explanation"。Phi-4 (14.7B) 和 Qwen-14B 参数规模相近、LoRA 配置相同，但一个 Immune 一个 Collapse——如果参数比例是主要驱动力，两者应表现相似。

R1 的回应也合理：Phi-4 和 Qwen-14B 来自不同家族，预训练数据、tokenizer、架构等差异很多，这个控制不严格。但这也是论文核心发现的一部分——"family-level factors beyond baseline ability modulate contamination vulnerability"（Section 6, p.8）。

建议：报告可训练参数比例作为 Table 补充信息，但不需要额外实验。

---

## W5: 300/14,042 MMLU item 选择的代表性

**[AGREE] R1-W5**: 选择偏差确实存在。

论文选择 exposure score 方差最高的 300 个 items 进行 IRT 拟合。这意味着：
- 这 300 个 items 是被多个检测信号一致标记为"可能受污染"或"确认未受污染"的 items（高方差 = 跨模型/dosage 有显著差异）
- 低方差 items（跨条件变化小）被排除——但这些 items 可能包含"所有模型都受影响"或"所有模型都不受影响"的极端情况

这引入了一种 selection bias：γ 估计基于最能区分 contaminated vs clean 的 items，可能高估了 contamination 效应的 heterogeneity。

不过，论文在 Section 3.3 对此选择有一定合理性说明："S1-only selection criterion"，且 Appendix E 的 RRF signal ablation 提供了 robustness 检查。但 R1 的担忧——低 exposure 变异 items 的行为可能不同——论文未直接回应。

---

## M1: RRF 融合 vs 学习型方法对比缺失

**[AGREE] R1-M1**: Table 7 (Appendix E) 的信号正交性分析（所有 |ρ|<0.06）和 Table 8 的 leave-one-out 消融充分支持了 RRF 的选择。学习型融合在 n=31 models 上很可能过拟合，RRF 的无参数特性在此场景下是优势。Minor 评级恰当。

---

## M2: 5 个剂量水平间距非均匀

**[AGREE] R1-M2**: 5%→25% 的跳跃确实可能遗漏拐点，尤其是 Collapse 模式（Qwen-14B）在 d005→d025 之间的具体转折。但论文已有 5 个水平（0, 0.5, 5, 25, 50, 100%）——实际是 6 个水平包括 0%——这在受控注入实验中已是较高密度。Appendix W 的参数化 dose-response 拟合也部分缓解了此问题。Minor 评级恰当。

---

## M3: n=3 seeds CI 宽度限制

**[AGREE] R1-M3**: CI 宽度 1.5-14.5pp 确实影响精度，但论文的方向一致性标准（Section 3.4 Algorithm 1 中的 agreement across seeds）是合理的折衷。增加 seeds 的计算成本在 5 families × 5-6 dosages 的设计下是显著的。Minor 评级恰当。

---

## M4: Algorithm 1 参数无理论推导

**[AGREE] R1-M4**: 与我 Round 1 的 M3 一致——阈值（τ=2pp, saturation ratio=0.3 等）是手动选取的。Appendix P 的 30-combination grid sweep 验证了分类稳定性，但正文未引用此验证。建议在 Algorithm 1 附近增加一句指向 Appendix P。Minor 评级恰当。

---

## M5: GSM8K max_new_tokens=256 截断 CoT

**[AGREE] R1-M5**: Section 5.2 的 GSM8K 评估使用 max_new_tokens=256，可能截断 chain-of-thought 推理。论文在 Appendix 中 caveat 了此问题，但主文 Section 5.2 或 4.2 应明确提及"absolute accuracy is therefore a lower bound"。这影响 cross-benchmark transfer 结论的可靠性。Minor 评级恰当。

---

## 与我 Round 1 审稿的互补说明

R1 和我的审查侧重不同但互补：

| 问题 | R1 覆盖 | R2 覆盖 | 状态 |
|------|---------|---------|------|
| J=16 先验主导 + P(γ<0) 不一致 | ✅ N1 | ❌ 未发现 | R1 更深入 |
| AUGMENT 数据量混淆 | ✅ W1 | ❌ 未发现 | R1 独有发现 |
| γ 参数化选择 | ✅ W2 | ❌ 未发现 | R1 独有发现 |
| N=5 taxonomy 过度泛化 | ❌ 未覆盖 | ✅ N1 | R2 独有发现 |
| ContamCal MAE 逊于 raw accuracy | ❌ 未覆盖 | ✅ N2 | R2 独有发现 |
| OOS 验证仅 Immune | ❌ 未覆盖 | ✅ N3 | R2 独有发现 |
| 方法新颖性定位 | ❌ 未覆盖 | ✅ W2 | R2 独有发现 |
| ARC PPP 正文讨论不足 | ✅ W3 (MMLU) | ✅ W1 (ARC) | 两人互补 |

R1 在 IRT 统计建模层面的技术审查比我更深入（先验敏感性、参数化选择、PPP 三层联动）。我在论文整体 claim 与证据匹配度上的审查更全面（taxonomy 泛化性、calibration value、OOS 覆盖度）。两份审稿合并可为 AC 提供较完整的评估。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-21T17:34:33.015561+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting cross-sharing responses'}, {'content': 'Step 3: Convergence judgment', 'status': 'in_progress', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'pending', 'activeForm': 'Synthesizing final report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting cross-sharing responses'}, {'content': 'Step 3: Convergence judgment', 'status': 'in_progress', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'pending', 'activeForm': 'Synthesizing final report'}]"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-21T17:34:33.016120+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-21T17:34:44.108659+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool call

_source line 871 · 2026-05-21T17:34:44.109124+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 872 · 2026-05-21T17:34:44.160508+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"projects/contamcal-irt-calibration/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T17:14:04.017758+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_4960c7baa442eabd4fa0aceeac2693ca\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-21T17:34:44.160930+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T17:14:03.158191+00:00\", \"completed_at\": \"2026-05-21T17:17:35.870421+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯文本），Figure 1 在 Page 2 顶部出现，仍在前 3 页范围内，审稿人第一印象尚可但非最优——若能将 Figure 1 或一个精简版概念图提前到 Page 1 底部会更强\"}, {\"severity\": \"warning\", \"dimension\": \"page 2\", \"message\": \"Figure 1 图例（legend）文字偏小，5 条线的标签在打印时可能难以辨认；建议放大图例字号或将图例移至图内空白区域以增大字号\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 使用了不同颜色 + 不同 marker 形状区分模型家族，色盲友好性尚可，但建议确认色板是否为 Okabe-Ito 或类似色盲安全方案\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"页面过度密集：2 个 table（Tables 3, 4）+ 1 个 figure（Figure 2）+ 4 个 section（5.5, 5.6, 5.7, 6 Discussion），阅读节奏拥挤；Figure 2 被压缩得很小，bar/point 的标签和坐标轴文字可能低于可读阈值\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2（DID 图）为单栏图，尺寸紧凑——若数据点不多可以接受，但建议检查打印时 axis label 是否清晰可读\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-4\", \"message\": \"Method 段连续 2 页以数学推导为主，无 display item 穿插——IRT 模型公式化属于合理例外，但若能在 Stage 1/Stage 2 分界处插入一个 pipeline 示意图（如已有则提前），会大幅改善方法段的可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Algorithm 1 伪代码排版干净，Require/Ensure 结构清晰，是很好的视觉锚点\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格，排版专业；caption 包含 cross-seed 说明，自包含性良好\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 格式一致，CI 区间标注清晰\"}, {\"severity\": \"info\", \"dimension\": \"pages 6-7\", \"message\": \"表格中最优结果已加粗标注，格式规范\"}, {\"severity\": \"warning\", \"dimension\": \"page 13\", \"message\": \"Figure 4（Signal Reliability heatmap）单栏内含多个子面板，单元格内数字字号很小（估计 ≤6pt），打印时可能需要放大镜；建议改为 figure* 全宽或减少面板数\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"Figure 7（Baseline Ability vs. Contamination Effect，4 个 scatter 子图）和 Figure 8（Domain 分解，多面板 bar + 柱状图）共挤一页，两个 figure 的 a
…[truncated 834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-21T17:35:29.839379+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting cross-sharing responses'}, {'content': 'Step 3: Convergence judgment', 'status': 'completed', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'in_progress', 'activeForm': 'Synthesizing final report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting cross-sharing responses'}, {'content': 'Step 3: Convergence judgment', 'status': 'completed', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'in_progress', 'activeForm': 'Synthesizing final report'}]"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-21T17:35:29.839924+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-21T17:39:05.022678+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form but framing still inconsistent.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Title framing no longer flagged.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。Title framing resolved.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D149+ rewrite: Title changed to 'Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families'. Paper repositioned as systematic empirical investigation of dose-response across 5 models (7B-14.7B) from 4 families. No over-scoping.\"\n  resolution_round: 7\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. All claims must be scoped to 'under SFT injection at ≤3B scale'.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Conclusion 'applies directly to settings with larger effects' is unsupported forward claim.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised as Should-Fix. Both agree SFT ecological validity is known limitation.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Re-raised. Consensus: Limitations discussion still too brief. Expand with Schaeffer et al. comparison.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未直接提及（fresh review）。Section 6 includes Schaeffer et al. comparison. Limitations includes SFT caveat.\"}\n  action_items:\n    - {round: 9, action: \"Expand SFT discussion in Section 6 with Schaeffer et al. comparison\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Section 6 rewritten with Schaeffer et al. comparison. Confounders listed. Limitations includes LoRA SFT caveat.\"\n  resolution_round: 9\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation has two interpretations.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Both unanimously re-raise as critical. R2 proposes threshold DGP simulation.\"}\n    - {round: 8, reviewers: \"\", note: \"DGP robustness appendix addresses this.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。DGP simulation in Appendix P addresses concern.\"}\n  resolution: \"400-run threshold DGP simulation completed. Appendix P written.\"\n  resolution_round: 7\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) — P(γ<0) inconsistency and Bonferroni claim unstable\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 10\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Bonferroni α=0.00625; CI upper bound likely includes zero.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Social Sciences at 99.1% does not pass Bonferroni.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text §5.4 still presents J=13.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。J=16 now in main text.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix. R1-N1 discovers P(γ<0) inconsistency: §5.7 reports 99.7% but Appendix K Table 10 shows 98.48% under same N(0,1) prior (ESS>3800 rules out MCMC noise). Bonferroni threshold 99.375% not met by Table 10 values. Prior sensitivity shows posterior mean varies 2.6× (0.34→0.89). 50% CI over-coverage 83%. PPP=0.16-0.25. All γ quantitative conclusions should be marked exploratory. R2 fully agrees.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'uncorrected for multiplicity' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text domain γ to J=16 results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Resolve P(γ<0) numerical inconsistency between §5.7 (99.7%) and Appendix K Table 10 (98.48%); report P(γ<0) range not single value; downgrade Bonferroni significance claim to 'approaching'; mark all γ conclusions as exploratory in main text\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations — IRT results unreliable\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 10\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at all J.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003. Move ARC IRT to Appendix.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"ARC IRT moved to Appendix.\"}\n    - {round: 9, reviewers: \"R2\", note: \"R2 re-raises: ARC PPP=0.003 should be discussed in main text.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R2-W1 re-raises ARC PPP. R1 corrects: PPP=0.003 IS in main text §5.5. R1-W3 adds: MMLU PPP=0.16-0.25 only in Appendix K, not in main text—this is the bigger gap. Both agree MMLU PPP should be reported in main text.\"}\n  action_items:\n    - {round: 9, action: \"Add brief discussion of ARC PPP=0.003 implications in main text\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report MMLU PPP=0.16-0.25 in main text §5.5 with brief discussion of model fit limitations\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality; MAE random control missing\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"No direct RRF vs S1-only ablation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation complete. Downgraded to warning.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Random 300-item subsets report τ but no MAE comparison.\"}\n    - {round: 9, reviewers: \"R1\", note: \"s_ij classification performance reported in Appendix.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未直接提及（fresh review）。RRF ablation and s_ij classification now in Appendix.\"}\n  action_items:\n    - {round: 9, action: \"Report s_ij classification performance at each dosage level\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal — over-coverage and under-coverage have different root causes\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Root cause diagnosis still insufficient.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。Root-cause diagnosis in §5.5.\"}\n  resolution: \"Root-cause diagnosis in §5.5. Not re-raised in Round 10.\"\n  resolution_round: 7\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses — J=13 domain finding vs J≥50 standard is self-contradictory\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。J=16 now in main text.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  resolution: \"Results §5 specifies J=16 for domain γ.\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Mean a_i comparison shows no discrimination confound.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 may reflect higher average a_i.\"}\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — caveat adequate but MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Phantom reference to Appendix E.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"MAE CI for cross-family pool not reported.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 5, action: \"Rename §5.5 to 'Cross-Family Exploratory Analysis'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Full prior sensitivity complete.\"\n  resolution_round: 5\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Conclusion scoped. Hypothesis labeled post-hoc.\"\n  resolution_round: 6\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure — C2 (signal filtering) partially disconnected from main question\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"3 empirical contributions.\"\n  resolution_round: 7\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — DIF classics + contamination benchmark literature\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 10\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. EACL 2026 most direct concurrent work.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"New gaps: Lord, Hambleton, HELM, Magar & Schwartz.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al. needed.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"New missing refs: Golchin & Surdeanu, Sainz et al., Yang et al.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Hill (1910), Ritz et al. (2015), Balloccu et al. (2024), Bordt et al. (2025) added.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both reviewers confirm all previously flagged references now present. R2-M5: 58 citations verified, no fake citations. References now comprehensive.\"}\n  action_items:\n    - {round: 8, action: \"Add Golchin & Surdeanu, Sainz et al., Yang et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 9, action: \"Add Hill (1910), Ritz et al. (2015), Balloccu et al., Bordt et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high — still ~6+ quantitative claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Abstract rewritten. Not re-raised in R10.\"\n  resolution_round: 7\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF; must commit to empirical study positioning\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 10\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must position as empirical contribution.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 still reads as method. Reposition.\"}\n    - {round: 8, reviewers: \"R2\", note: \"Novelty primarily from experimental paradigm.\"}\n    - {round: 9, reviewers: \"\", note: \"Paper now positioned as empirical investigation.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R2-W2 re-raises: 2PL+γ is standard explanatory IRT/DIF, paper should explicitly acknowledge no IRT modeling novelty, novelty is in controlled injection design + empirical findings. R1 AGREE. Both suggest adding explicit positioning statement.\"}\n  action_items:\n    - {round: 6, action: \"Reposition Han et al. differentiation; elevate J≥50 identifiability\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Add explicit statement in §3.3 or §6: 'Our modeling contribution is not in the IRT specification—which follows standard explanatory IRT—but in the controlled injection design that enables causal interpretation of γ'\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. and Schaeffer et al. differentiation needs expansion\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. Han et al. comparison needs expansion.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Han et al. differentiation as critical.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Schaeffer et al. and Han et al. insufficiently discussed.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. R2-W3 + R1 AGREE. Han et al. (DIF parameterization differences: continuous exposure vs binary group?) and Schaeffer et al. (pretraining vs SFT injection, do results converge?) need explicit methodological comparison, not just one-sentence mentions. Discussion should include: what complementary picture emerges from combining both studies' findings.\"}\n  action_items:\n    - {round: 9, action: \"Add Schaeffer et al. comparison in Section 6\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Expand Han et al. and Schaeffer et al. discussion in Section 2 or 6: add DIF parameterization comparison, empirical finding comparison, explicit statement of complementarity\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R5-N1\"\n  summary: \"Page limit — needs compile verification\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R2\", note: \"Visual check confirms 8 pages main text ✓.\"}\n    - {round: 10, reviewers: \"R2\", note: \"Format compliance confirmed: 8 pages main text, ACL template, double-blind.\"}\n  resolution: \"Confirmed 8 pages main text, EMNLP 2026 compliant.\"\n  resolution_round: 9\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"k reserved for benchmark, d for domain.\"\n  resolution_round: 7\n\n- id: \"R6-W1\"\n  summary: \"SFT data composition confound — AUGMENT mode volume confound undiscussed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"§4.1 does not specify whether benchmark items replace or augment.\"}\n    - {round: 9, reviewers: \"\", note: \"Paper explicitly states AUGMENT mode.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. R1-W1 calculates: d000=50k, d100≈66.5k (+33.1%). Data volume confound not discussed in Limitations. Gemma-2 Benefit and Qwen-7B V-recovery most affected. Partial mitigation: DiD shows parallel treated/untreated changes (item-level confound controlled), but aggregate-level volume confound remains. R2 agrees, adds DID mitigation argument. Both recommend: report total training set size per dosage, discuss REPLACE mode as future work.\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report total training set size per dosage; discuss AUGMENT volume confound in Limitations (d100 +33% data); mention REPLACE mode as future disambiguation\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R6-W2\"\n  summary: \"S4 (Self-Critique) signal computation details insufficient for reproduction\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix E added with S4 details.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported — convergence verification missing\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix F added with convergence info.\"\n  resolution_round: 8\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"Cross-family GSM8K PPP=0.83 but within-family GSM8K PPP not reported.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。Still not reported.\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-N1\"\n  summary: \"Cross-seed stability claims overstated — n=3 seeds insufficient for taxonomy validation\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"n=3 seeds yields wide CIs; strict sign consistency only 2/5 families.\"}\n    - {round: 9, reviewers: \"\", note: \"Paper Limitations acknowledges seed sensitivity.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both agree n=3 is acceptable given compute constraints, and direction-based aggregation (§3.4) is a reasonable compromise. CI widths 1.5-14.5pp are honestly reported. Downgraded to Minor in this round.\"}\n  action_items:\n    - {round: 8, action: \"Increase seeds to n≥5 or weaken claims\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-N2\"\n  summary: \"DiD null result lacks power analysis — 'causal evidence for global modulation' claim unsupported\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Contribution 2 reframed with MDES. 'Causal evidence' removed.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R1 rates DiD analysis as Acceptable. MDES correctly computed and interpreted. ARC appropriately caveated. Both agree this issue is resolved.\"}\n  resolution: \"Contribution 2 title includes 'at current power levels'. MDES reported. DiD analysis rated Acceptable by R1.\"\n  resolution_round: 9\n\n- id: \"R8-N3\"\n  summary: \"N=5 model families supporting 4-class taxonomy — generalization evidence insufficient\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"4 patterns observed on 4 families is post-hoc description.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"CONSENSUS: reposition as 'observed response profiles' or 'preliminary taxonomy'.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix (R2-N1 + R1 AGREE). Collapse n=1 (Qwen-14B only), V-recovery n=1 (Qwen-7B only), both from same Qwen2.5 family—could be Qwen-specific. OOS validation covers only Immune (R2-N3, R1 AGREE). Paper says 'This empirical taxonomy is preliminary at N=5 families' (§5.1) which is honest, but Abstract/Intro still use 'four qualitatively different dose-response patterns' without adequate scoping. Section 6 'Two of four patterns attested in ≥2 independent families' is misleading—Benefit instances (OLMo-2, Gemma-2) are construction families, not OOS.\"}\n  action_items:\n    - {round: 9, action: \"Fix §5.1: accurate count (Collapse n=1, V-recovery n=1). Use 'empirical taxonomy, preliminary at N=5'.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Replace 'taxonomy' with 'profiles' or 'observed patterns' in Abstract and Introduction; add explicit acknowledgment that Collapse and V-recovery are each attested in only one family (Qwen2.5); discuss OOS validation gap in Limitations (only Immune verified out-of-sample)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N4\"\n  summary: \"Han et al. (2026) differentiation insufficient — only 2 sentences, no empirical comparison\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Han et al. is most direct prior work.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Schaeffer et al. also insufficiently discussed.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Merged with R2-W8 for this round. Both agree dedicated comparison needed.\"}\n  action_items:\n    - {round: 8, action: \"Add ~0.5 page methodological comparison with Han et al.\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W1\"\n  summary: \"Bayesian and frequentist terminology mixed throughout paper\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Paper uses Bayesian MCMC but 'significant', 'p-value', 'confidence interval' appear in frequentist sense.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未直接提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Unify terminology\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W2\"\n  summary: \"IRT identifiability simulation uses uniform exposure — mismatch with empirical right-skewed RRF distribution\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Empirical RRF highly right-skewed. Simulation uses uniform.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Re-run identifiability simulation with right-skewed exposure\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-W3\"\n  summary: \"Algorithm 1 threshold sensitivity — only pass/fail grid reported, no continuous sensitivity curve\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R2,R1\", note: \"30/30 pass is too coarse.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Appendix P Table 14 only shows pass/fail.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both rate as Minor. Appendix P now includes nearest-transition analysis (Table 14). Grid sweep 100% stability in reasonable range. Lack of theoretical derivation noted but acceptable given empirical validation.\"}\n  action_items:\n    - {round: 8, action: \"Add threshold sensitivity heatmap in Appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M1\"\n  summary: \"Missing references — Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Yang et al., Golchin & Surdeanu, Sainz et al.\"}\n    - {round: 10, reviewers: \"\", note: \"R2-M5 verifies 58 citations, all referenced in text. Golchin & Surdeanu and Sainz et al. now cited. Yang et al. status unclear—merged into R4-W4.\"}\n  action_items:\n    - {round: 8, action: \"Add missing references\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M2\"\n  summary: \"Minor writing issues — Figure 1 caption, Table formatting, prior distributions\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Various minor writing issues.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R2-M4: Figure 1 y-axis ranges differ across panels, may mislead effect size perception. R1 agrees. Minor.\"}\n  action_items:\n    - {round: 10, action: \"Annotate Figure 1 caption with y-axis range note; or unify y-axis ranges\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"AUDIT-1\"\n  summary: \"Figure 1 missing from PDF — referenced in §5.1 but not present\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"audit\", note: \"Figure 1 does not exist in the PDF.\"}\n    - {round: 9, reviewers: \"\", note: \"Resolved. Figure 1 present on page 2.\"}\n    - {round: 10, reviewers: \"\", note: \"Visual check confirms Figure 1 present on page 2.\"}\n  resolution: \"Figure 1 present in Introduction. Confirmed by visual check.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Taxonomy based on ad-hoc Algorithm 1 — lacks formal parametric dose-response modeling\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Algorithm 1 uses hardcoded thresholds. Pharmacology has parametric DR models.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Appendix W now includes parametric DR model comparison (Constant/Linear/Quadratic/Hill, AICc selection). Both reviewers acknowledge this addresses the concern. R1-M4 and R2-M3 note threshold derivation as Minor.\"}\n  resolution: \"Appendix W: Parametric DR Model Comparison. Only Qwen-14B shows AICc agreement with Algorithm 1; moderate effects indistinguishable from Constant at n=3.\"\n  resolution_round: 9\n\n- id: \"R9-N2\"\n  summary: \"'Architecture determines vulnerability' causal claim exceeds evidence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Replace with 'family-level factors beyond baseline ability'.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。All instances replaced with 'family-level factors'. Confounders listed in Section 6.\"}\n  resolution: \"All causal claims replaced. Confounders listed.\"\n  resolution_round: 9\n\n- id: \"R9-S1\"\n  summary: \"Unified LoRA r=16 creates unequal treatment strength across model scales\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"LoRA r=16 parameter fraction inversely proportional to model size.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R1-W4 re-raises. R2 agrees with nuance: Phi-4 vs Qwen-14B counter-argument has merit but control is not strict (different families). Both recommend: report actual trainable parameter percentages per model.\"}\n  action_items:\n    - {round: 9, action: \"Discuss LoRA capacity confound in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report actual trainable parameter percentages (trainable/total %) for each model in §4.1 or Table\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-S2\"\n  summary: \"'65-70% MMLU baseline vulnerability band' claim over-precise for n=5 data points\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Qualify with 'in our five-family sample'.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。All claims qualified with scope.\"}\n  resolution: \"All '65-70%' claims qualified with 'in our five-family sample'.\"\n  resolution_round: 9\n\n- id: \"R9-S3\"\n  summary: \"Calibration baseline comparison missing IRT variants — cannot isolate γ contribution\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"B3 (Vanilla 2PL) partially addresses. Systematic 2PL vs 2PL+γ ablation would be better.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未直接提及（fresh review）。R1 notes ContamCal value is diagnostic not calibration; Table 4 B3 vs ContamCal comparison exists.\"}\n  action_items:\n    - {round: 9, action: \"Add 2PL vs 2PL+γ ablation in appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n\n# === Round 10 (Fresh Review) New Issues ===\n\n- id: \"R10-N1\"\n  summary: \"ContamCal calibration MAE (0.009) worse than raw accuracy (0.006) — practical value of calibration questioned\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R2\", note: \"R2-N2: Table 4 shows B0 Raw MAE=0.006 vs ContamCal MAE=0.009. Core method underperforms 'do nothing' baseline on calibration.\"}\n    - {round: 10, reviewers: \"R1\", note: \"R1 REBUT: Paper §3.3 explicitly predicts this—Eq.3 depends on θ not γ directly; γ serves diagnosis not calibration. Table 4 validates this theoretical prediction. ContamCal's value is domain-level diagnostic (Social Sciences γ_ss=-0.63), not MAE improvement. DIVERGENT.\"}\n  action_items:\n    - {round: 10, action: \"Clarify in §5.5 that ContamCal's value proposition is diagnostic (domain-level γ analysis) not aggregate calibration improvement; optionally add per-affected-model MAE stratification\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R10-W1\"\n  summary: \"γ parameterization: outside a_i bracket differs from standard DIF, choice unjustified\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. R1-W2 raises, R2 AGREE. Paper uses σ(a_i(θ-b)+γ·e) but standard DIF uses σ(a_i(θ-b+γ·e)). Paper's version: contamination logit-constant (same shift for high/low discrimination items). Standard: contamination ability-constant (high-discrimination items get larger logit shift). Paper acknowledges difference ('shifts by γ·e/a_i') but doesn't justify choice. If global capability modulation (DiD evidence) is the mechanism, standard parameterization may be more appropriate.\"}\n  action_items:\n    - {round: 10, action: \"Add paragraph in §3.3 discussing parameterization choice: justify why γ outside a_i, or provide comparison with standard inside-a_i form\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R10-W2\"\n  summary: \"300/14042 MMLU item subset introduces selection bias toward high-exposure-variance items\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. R1-W5 raises, R2 AGREE. IRT fitted on 2.1% of MMLU items selected for maximum exposure variance. γ estimates may not generalize to full benchmark. Low-variance items (universally affected or unaffected) excluded.\"}\n  action_items:\n    - {round: 10, action: \"Discuss 300-item subset representativeness; optionally report γ stability across different subset sizes (200, 500)\", assigned_to: \"paper_agent\", status: \"open\"}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form but framing still inconsistent.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。Title framing no longer flagged.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。Title framing resolved.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D149+ rewrite: Title changed to 'Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families'. Paper repositioned as systematic empirical investigation of dose-response across 5 models (7B-14.7B) from 4 families. No over-scoping.\"\n  resolution_round: 7\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. All claims must be scoped to 'under SFT injection at ≤3B scale'.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Conclusion 'applies directly to settings with larger effects' is unsupported forward claim.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Re-raised as Should-Fix. Both agree SFT ecological validity is known limitation.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Re-raised. Consensus: Limitations discussion still too brief. Expand with Schaeffer et al. comparison.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未直接提及（fresh review）。Section 6 includes Schaeffer et al. comparison. Limitations includes SFT caveat.\"}\n  action_items:\n    - {round: 9, action: \"Expand SFT discussion in Section 6 with Schaeffer et al. comparison\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Section 6 rewritten with Schaeffer et al. comparison. Confounders listed. Limitations includes LoRA SFT caveat.\"\n  resolution_round: 9\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation has two interpretations.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Both unanimously re-raise as critical. R2 proposes threshold DGP simulation.\"}\n    - {round: 8, reviewers: \"\", note: \"DGP robustness appendix addresses this.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。DGP simulation in Appendix P addresses concern.\"}\n  resolution: \"400-run threshold DGP simulation completed. Appendix P written.\"\n  resolution_round: 7\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) — P(γ<0) inconsistency and Bonferroni claim unstable\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 10\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Bonferroni α=0.00625; CI upper bound likely includes zero.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Social Sciences at 99.1% does not pass Bonferroni.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text §5.4 still presents J=13.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。J=16 now in main text.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix. R1-N1 discovers P(γ<0) inconsistency: §5.7 reports 99.7% but Appendix K Table 10 shows 98.48% under same N(0,1) prior (ESS>3800 rules out MCMC noise). Bonferroni threshold 99.375% not met by Table 10 values. Prior sensitivity shows posterior mean varies 2.6× (0.34→0.89). 50% CI over-coverage 83%. PPP=0.16-0.25. All γ quantitative conclusions should be marked exploratory. R2 fully agrees.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'uncorrected for multiplicity' caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text domain γ to J=16 results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Resolve P(γ<0) numerical inconsistency between §5.7 (99.7%) and Appendix K Table 10 (98.48%); report P(γ<0) range not single value; downgrade Bonferroni significance claim to 'approaching'; mark all γ conclusions as exploratory in main text\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations — IRT results unreliable\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 10\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at all J.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003. Move ARC IRT to Appendix.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"ARC IRT moved to Appendix.\"}\n    - {round: 9, reviewers: \"R2\", note: \"R2 re-raises: ARC PPP=0.003 should be discussed in main text.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R2-W1 re-raises ARC PPP. R1 corrects: PPP=0.003 IS in main text §5.5. R1-W3 adds: MMLU PPP=0.16-0.25 only in Appendix K, not in main text—this is the bigger gap. Both agree MMLU PPP should be reported in main text.\"}\n  action_items:\n    - {round: 9, action: \"Add brief discussion of ARC PPP=0.003 implications in main text\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report MMLU PPP=0.16-0.25 in main text §5.5 with brief discussion of model fit limitations\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality; MAE random control missing\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"No direct RRF vs S1-only ablation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation complete. Downgraded to warning.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Random 300-item subsets report τ but no MAE comparison.\"}\n    - {round: 9, reviewers: \"R1\", note: \"s_ij classification performance reported in Appendix.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未直接提及（fresh review）。RRF ablation and s_ij classification now in Appendix.\"}\n  action_items:\n    - {round: 9, action: \"Report s_ij classification performance at each dosage level\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal — over-coverage and under-coverage have different root causes\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Root cause diagnosis still insufficient.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。Root-cause diagnosis in §5.5.\"}\n  resolution: \"Root-cause diagnosis in §5.5. Not re-raised in Round 10.\"\n  resolution_round: 7\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses — J=13 domain finding vs J≥50 standard is self-contradictory\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。J=16 now in main text.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  resolution: \"Results §5 specifies J=16 for domain γ.\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Mean a_i comparison shows no discrimination confound.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 may reflect higher average a_i.\"}\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — caveat adequate but MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Phantom reference to Appendix E.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"MAE CI for cross-family pool not reported.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 5, action: \"Rename §5.5 to 'Cross-Family Exploratory Analysis'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Full prior sensitivity complete.\"\n  resolution_round: 5\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Conclusion scoped. Hypothesis labeled post-hoc.\"\n  resolution_round: 6\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure — C2 (signal filtering) partially disconnected from main question\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"3 empirical contributions.\"\n  resolution_round: 7\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — DIF classics + contamination benchmark literature\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 10\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. EACL 2026 most direct concurrent work.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"New gaps: Lord, Hambleton, HELM, Magar & Schwartz.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al. needed.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"New missing refs: Golchin & Surdeanu, Sainz et al., Yang et al.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Hill (1910), Ritz et al. (2015), Balloccu et al. (2024), Bordt et al. (2025) added.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both reviewers confirm all previously flagged references now present. R2-M5: 58 citations verified, no fake citations. References now comprehensive.\"}\n  action_items:\n    - {round: 8, action: \"Add Golchin & Surdeanu, Sainz et al., Yang et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 9, action: \"Add Hill (1910), Ritz et al. (2015), Balloccu et al., Bordt et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high — still ~6+ quantitative claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Abstract rewritten. Not re-raised in R10.\"\n  resolution_round: 7\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF; must commit to empirical study positioning\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 10\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Must position as empirical contribution.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"C2 still reads as method. Reposition.\"}\n    - {round: 8, reviewers: \"R2\", note: \"Novelty primarily from experimental paradigm.\"}\n    - {round: 9, reviewers: \"\", note: \"Paper now positioned as empirical investigation.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R2-W2 re-raises: 2PL+γ is standard explanatory IRT/DIF, paper should explicitly acknowledge no IRT modeling novelty, novelty is in controlled injection design + empirical findings. R1 AGREE. Both suggest adding explicit positioning statement.\"}\n  action_items:\n    - {round: 6, action: \"Reposition Han et al. differentiation; elevate J≥50 identifiability\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Add explicit statement in §3.3 or §6: 'Our modeling contribution is not in the IRT specification—which follows standard explanatory IRT—but in the controlled injection design that enables causal interpretation of γ'\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. and Schaeffer et al. differentiation needs expansion\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. Han et al. comparison needs expansion.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"Han et al. differentiation as critical.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Schaeffer et al. and Han et al. insufficiently discussed.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. R2-W3 + R1 AGREE. Han et al. (DIF parameterization differences: continuous exposure vs binary group?) and Schaeffer et al. (pretraining vs SFT injection, do results converge?) need explicit methodological comparison, not just one-sentence mentions. Discussion should include: what complementary picture emerges from combining both studies' findings.\"}\n  action_items:\n    - {round: 9, action: \"Add Schaeffer et al. comparison in Section 6\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Expand Han et al. and Schaeffer et al. discussion in Section 2 or 6: add DIF parameterization comparison, empirical finding comparison, explicit statement of complementarity\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R5-N1\"\n  summary: \"Page limit — needs compile verification\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R2\", note: \"Visual check confirms 8 pages main text ✓.\"}\n    - {round: 10, reviewers: \"R2\", note: \"Format compliance confirmed: 8 pages main text, ACL template, double-blind.\"}\n  resolution: \"Confirmed 8 pages main text, EMNLP 2026 compliant.\"\n  resolution_round: 9\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"k reserved for benchmark, d for domain.\"\n  resolution_round: 7\n\n- id: \"R6-W1\"\n  summary: \"SFT data composition confound — AUGMENT mode volume confound undiscussed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"§4.1 does not specify whether benchmark items replace or augment.\"}\n    - {round: 9, reviewers: \"\", note: \"Paper explicitly states AUGMENT mode.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. R1-W1 calculates: d000=50k, d100≈66.5k (+33.1%). Data volume confound not discussed in Limitations. Gemma-2 Benefit and Qwen-7B V-recovery most affected. Partial mitigation: DiD shows parallel treated/untreated changes (item-level confound controlled), but aggregate-level volume confound remains. R2 agrees, adds DID mitigation argument. Both recommend: report total training set size per dosage, discuss REPLACE mode as future work.\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report total training set size per dosage; discuss AUGMENT volume confound in Limitations (d100 +33% data); mention REPLACE mode as future disambiguation\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R6-W2\"\n  summary: \"S4 (Self-Critique) signal computation details insufficient for reproduction\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix E added with S4 details.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported — convergence verification missing\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix F added with convergence info.\"\n  resolution_round: 8\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"Cross-family GSM8K PPP=0.83 but within-family GSM8K PPP not reported.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。Still not reported.\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-N1\"\n  summary: \"Cross-seed stability claims overstated — n=3 seeds insufficient for taxonomy validation\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"n=3 seeds yields wide CIs; strict sign consistency only 2/5 families.\"}\n    - {round: 9, reviewers: \"\", note: \"Paper Limitations acknowledges seed sensitivity.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both agree n=3 is acceptable given compute constraints, and direction-based aggregation (§3.4) is a reasonable compromise. CI widths 1.5-14.5pp are honestly reported. Downgraded to Minor in this round.\"}\n  action_items:\n    - {round: 8, action: \"Increase seeds to n≥5 or weaken claims\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-N2\"\n  summary: \"DiD null result lacks power analysis — 'causal evidence for global modulation' claim unsupported\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Contribution 2 reframed with MDES. 'Causal evidence' removed.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R1 rates DiD analysis as Acceptable. MDES correctly computed and interpreted. ARC appropriately caveated. Both agree this issue is resolved.\"}\n  resolution: \"Contribution 2 title includes 'at current power levels'. MDES reported. DiD analysis rated Acceptable by R1.\"\n  resolution_round: 9\n\n- id: \"R8-N3\"\n  summary: \"N=5 model families supporting 4-class taxonomy — generalization evidence insufficient\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"4 patterns observed on 4 families is post-hoc description.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"CONSENSUS: reposition as 'observed response profiles' or 'preliminary taxonomy'.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix (R2-N1 + R1 AGREE). Collapse n=1 (Qwen-14B only), V-recovery n=1 (Qwen-7B only), both from same Qwen2.5 family—could be Qwen-specific. OOS validation covers only Immune (R2-N3, R1 AGREE). Paper says 'This empirical taxonomy is preliminary at N=5 families' (§5.1) which is honest, but Abstract/Intro still use 'four qualitatively different dose-response patterns' without adequate scoping. Section 6 'Two of four patterns attested in ≥2 independent families' is misleading—Benefit instances (OLMo-2, Gemma-2) are construction families, not OOS.\"}\n  action_items:\n    - {round: 9, action: \"Fix §5.1: accurate count (Collapse n=1, V-recovery n=1). Use 'empirical taxonomy, preliminary at N=5'.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Replace 'taxonomy' with 'profiles' or 'observed patterns' in Abstract and Introduction; add explicit acknowledgment that Collapse and V-recovery are each attested in only one family (Qwen2.5); discuss OOS validation gap in Limitations (only Immune verified out-of-sample)\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-N4\"\n  summary: \"Han et al. (2026) differentiation insufficient — only 2 sentences, no empirical comparison\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Han et al. is most direct prior work.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Schaeffer et al. also insufficiently discussed.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Merged with R2-W8 for this round. Both agree dedicated comparison needed.\"}\n  action_items:\n    - {round: 8, action: \"Add ~0.5 page methodological comparison with Han et al.\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W1\"\n  summary: \"Bayesian and frequentist terminology mixed throughout paper\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Paper uses Bayesian MCMC but 'significant', 'p-value', 'confidence interval' appear in frequentist sense.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未直接提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Unify terminology\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W2\"\n  summary: \"IRT identifiability simulation uses uniform exposure — mismatch with empirical right-skewed RRF distribution\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Empirical RRF highly right-skewed. Simulation uses uniform.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Re-run identifiability simulation with right-skewed exposure\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-W3\"\n  summary: \"Algorithm 1 threshold sensitivity — only pass/fail grid reported, no continuous sensitivity curve\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R2,R1\", note: \"30/30 pass is too coarse.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Appendix P Table 14 only shows pass/fail.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both rate as Minor. Appendix P now includes nearest-transition analysis (Table 14). Grid sweep 100% stability in reasonable range. Lack of theoretical derivation noted but acceptable given empirical validation.\"}\n  action_items:\n    - {round: 8, action: \"Add threshold sensitivity heatmap in Appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M1\"\n  summary: \"Missing references — Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Yang et al., Golchin & Surdeanu, Sainz et al.\"}\n    - {round: 10, reviewers: \"\", note: \"R2-M5 verifies 58 citations, all referenced in text. Golchin & Surdeanu and Sainz et al. now cited. Yang et al. status unclear—merged into R4-W4.\"}\n  action_items:\n    - {round: 8, action: \"Add missing references\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M2\"\n  summary: \"Minor writing issues — Figure 1 caption, Table formatting, prior distributions\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Various minor writing issues.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R2-M4: Figure 1 y-axis ranges differ across panels, may mislead effect size perception. R1 agrees. Minor.\"}\n  action_items:\n    - {round: 10, action: \"Annotate Figure 1 caption with y-axis range note; or unify y-axis ranges\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"AUDIT-1\"\n  summary: \"Figure 1 missing from PDF — referenced in §5.1 but not present\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"audit\", note: \"Figure 1 does not exist in the PDF.\"}\n    - {round: 9, reviewers: \"\", note: \"Resolved. Figure 1 present on page 2.\"}\n    - {round: 10, reviewers: \"\", note: \"Visual check confirms Figure 1 present on page 2.\"}\n  resolution: \"Figure 1 present in Introduction. Confirmed by visual check.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Taxonomy based on ad-hoc Algorithm 1 — lacks formal parametric dose-response modeling\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Algorithm 1 uses hardcoded thresholds. Pharmacology has parametric DR models.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Appendix W now includes parametric DR model comparison (Constant/Linear/Quadratic/Hill, AICc selection). Both reviewers acknowledge this addresses the concern. R1-M4 and R2-M3 note threshold derivation as Minor.\"}\n  resolution: \"Appendix W: Parametric DR Model Comparison. Only Qwen-14B shows AICc agreement with Algorithm 1; moderate effects indistinguishable from Constant at n=3.\"\n  resolution_round: 9\n\n- id: \"R9-N2\"\n  summary: \"'Architecture determines vulnerability' causal claim exceeds evidence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Replace with 'family-level factors beyond baseline ability'.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。All instances replaced with 'family-level factors'. Confounders listed in Section 6.\"}\n  resolution: \"All causal claims replaced. Confounders listed.\"\n  resolution_round: 9\n\n- id: \"R9-S1\"\n  summary: \"Unified LoRA r=16 creates unequal treatment strength across model scales\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"LoRA r=16 parameter fraction inversely proportional to model size.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"R1-W4 re-raises. R2 agrees with nuance: Phi-4 vs Qwen-14B counter-argument has merit but control is not strict (different families). Both recommend: report actual trainable parameter percentages per model.\"}\n  action_items:\n    - {round: 9, action: \"Discuss LoRA capacity confound in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report actual trainable parameter percentages (trainable/total %) for each model in §4.1 or Table\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R9-S2\"\n  summary: \"'65-70% MMLU baseline vulnerability band' claim over-precise for n=5 data points\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Qualify with 'in our five-family sample'.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。All claims qualified with scope.\"}\n  resolution: \"All '65-70%' claims qualified with 'in our five-family sample'.\"\n  resolution_round: 9\n\n- id: \"R9-S3\"\n  summary: \"Calibration baseline comparison missing IRT variants — cannot isolate γ contribution\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"B3 (Vanilla 2PL) partially addresses. Systematic 2PL vs 2PL+γ ablation would be better.\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未直接提及（fresh review）。R1 notes ContamCal value is diagnostic not calibration; Table 4 B3 vs ContamCal comparison exists.\"}\n  action_items:\n    - {round: 9, action: \"Add 2PL vs 2PL+γ ablation in appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n\n# === Round 10 (Fresh Review) New Issues ===\n\n- id: \"R10-N1\"\n  summary: \"ContamCal calibration MAE (0.009) worse than raw accuracy (0.006) — practical value of calibration questioned\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R2\", note: \"R2-N2: Table 4 shows B0 Raw MAE=0.006 vs ContamCal MAE=0.009. Core method underperforms 'do nothing' baseline on calibration.\"}\n    - {round: 10, reviewers: \"R1\", note: \"R1 REBUT: Paper §3.3 explicitly predicts this—Eq.3 depends on θ not γ directly; γ serves diagnosis not calibration. Table 4 validates this theoretical prediction. ContamCal's value is domain-level diagnostic (Social Sciences γ_ss=-0.63), not MAE improvement. DIVERGENT.\"}\n  action_items:\n    - {round: 10, action: \"Clarify in §5.5 that ContamCal's value proposition is diagnostic (domain-level γ analysis) not aggregate calibration improvement; optionally add per-affected-model MAE stratification\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R10-W1\"\n  summary: \"γ parameterization: outside a_i bracket differs from standard DIF, choice unjustified\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. R1-W2 raises, R2 AGREE. Paper uses σ(a_i(θ-b)+γ·e) but standard DIF uses σ(a_i(θ-b+γ·e)). Paper's version: contamination logit-constant (same shift for high/low discrimination items). Standard: contamination ability-constant (high-discrimination items get larger logit shift). Paper acknowledges difference ('shifts by γ·e/a_i') but doesn't justify choice. If global capability modulation (DiD evidence) is the mechanism, standard parameterization may be more appropriate.\"}\n  action_items:\n    - {round: 10, action: \"Add paragraph in §3.3 discussing parameterization choice: justify why γ outside a_i, or provide comparison with standard inside-a_i form\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R10-W2\"\n  summary: \"300/14042 MMLU item subset introduces selection bias toward high-exposure-variance items\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. R1-W5 raises, R2 AGREE. IRT fitted on 2.1% of MMLU items selected for maximum exposure variance. γ estimates may not generalize to full benchmark. Low-variance items (universally affected or unaffected) excluded.\"}\n  action_items:\n    - {round: 10, action: \"Discuss 300-item subset representativeness; optionally report γ stability across different subset sizes (200, 500)\", assigned_to: \"paper_agent\", status: \"open\"}"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-21T17:39:05.125253+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml\", \"bytes\": 33394}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-21T17:41:35.902804+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "report": "# 审稿报告 — Round 10 (Fresh Review)\n\n**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n**Venue**: EMNLP 2026 via ARR May 2026\n**审稿模式**: Fresh（重新审稿，无历史上下文）\n**Reviewer 配置**: 2 人（R1 方法严谨性+实验设计+统计分析 / R2 新颖性+完整性+相关工作+写作质量）\n**轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识，无需进入 Round 2\n\n---\n\n## Summary\n\n本文对\"benchmark contamination 是否统一 inflate 模型分数\"这一社区默认假设进行了系统性实证检验。通过受控 SFT 注入（LoRA, 5 个剂量水平）对 5 个模型家族（4 个独立实验室，7B-14.7B）进行实验，发现 contamination 产生质的不同剂量-反应模式——从 Immune（Phi-4, ±0.5pp）到 Collapse（Qwen-14B, -9 to -25pp）。论文进一步提出 ContamCal 两阶段管线（多信号 RRF exposure mapping + contamination-augmented IRT），提供域级污染诊断。DiD 分析在 MMLU 上未发现 item-specific memorization（MDES 1.2-2.0pp），支持全局能力调节而非记忆化机制。\n\n---\n\n## Strengths\n\n1. **受控注入实验设计是核心优势**。在 contamination 文献中大多为观察性研究的背景下，本文通过 controlled SFT injection 实现了对 dosage 的精确控制（5 个水平 × 5 个家族 × 3 seeds），使因果推断成为可能。这是相对于 Han et al. (2026) 观察性 DIF 和其他检测方法的本质优势。[R1, R2 共识]\n\n2. **\"contamination ≠ inflation\" 的核心发现有实际意义**。4 种定性不同的剂量-反应模式（Immune, Collapse, V-recovery, Benefit）挑战了社区默认假设，对 leaderboard 解读和模型评估实践有直接影响。Table 1 和 Figure 1 清晰呈现了这一发现。[R1, R2 共识]\n\n3. **DiD 分析严谨**。Treated vs untreated items 的差分-差分检验逻辑清晰，post-hoc power analysis（MDES）正确计算和解读，ARC 的低功效被恰当标注。\"No detectable item-specific memorization at current power levels\" 的表述诚实且 bounded。[R1 评级 Acceptable]\n\n4. **Cross-benchmark transfer 分析丰富了理解**。MMLU-targeted contamination 对 GSM8K 的正迁移（所有非排除家族 +1 to +16pp）和方向反转（Qwen-7B: MMLU -1.8pp 但 GSM8K +10.1pp）是有价值的实证发现。[R1, R2 共识]\n\n5. **信号失效特征化有实践价值**。Min-K%++ 在 0.5B 处的方向反转（Cohen's d = -1.55 to -1.98）对使用 membership inference 做 contamination detection 的实践者有直接警示意义。[R2 特别标注]\n\n6. **统计方法论透明度高**。论文诚实报告了 CI over-coverage (83%)、PPP 值、MDES、先验敏感度、Appendix K \"exploratory status\" 等局限。11 页 Appendix 覆盖了 robustness checks、sensitivity analyses、parametric DR model comparison 等。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 项，影响接收决定）\n\n**MF-1** [R1-N1, R2 AGREE] **J=16 先验主导 + P(γ<0) 数值不一致 + Bonferroni 显著性声明不稳健**\n\n论文在 J=16 配置下的 IRT 定量结论存在三层问题：\n- **先验主导**：Appendix K 承认 \"J=16 provides insufficient data to override the prior\"，后验均值跨先验变化 2.6×（0.34→0.89），50% CI over-coverage 达 83%。\n- **数值不一致**：Section 5.7 报告 Social Sciences P(γ<0)=99.7%，但 Appendix K Table 10 在同一 N(0,1) 先验下显示 P(γ<0)=98.48%。ESS>3800 排除 MCMC 随机变异，差异来源未解释。\n- **Bonferroni 声明不成立**：8 次检验的 Bonferroni 阈值为 P>99.375%。Table 10 的 98.48% 未达标；即使取最宽松先验 N(0,2) 的 98.95% 仍未达标。Section 5.7 \"crossing the Bonferroni-corrected threshold\" 声明与论文自己的先验敏感性数据矛盾。\n\n**建议**：(1) 解决 §5.7 与 Table 10 的数值差异来源；(2) 报告 P(γ<0) 范围而非单一值；(3) 将 Bonferroni 声明降级为 \"approaching Bonferroni significance\"；(4) 主文中所有 γ 定量结论标记为 exploratory。\n\n**MF-2** [R2-N1, R1 AGREE] **N=5 家族归纳 4 类 taxonomy 的统计基础不足**\n\n四类分类中 Collapse 仅 Qwen-14B（n=1），V-recovery 仅 Qwen-7B（n=1），两者均来自同一 Qwen2.5 家族。无法排除这两种模式是 Qwen 架构特异性行为。论文 §5.1 写 \"This empirical taxonomy is preliminary at N=5 families\" 是诚实的，但 Abstract 和 Introduction 使用 \"four qualitatively different dose-response patterns\" 和 \"taxonomy\" 时 scoping 不足。Section 6 \"Two of four patterns attested in ≥2 independent families\" 有误导性——Benefit 的两个实例（OLMo-2, Gemma-2）均为 construction 家族，非 OOS。\n\n**建议**：(1) Abstract/Introduction 将 \"taxonomy\" 替换为 \"profiles\" 或 \"observed patterns\"；(2) 明确承认 Collapse/V-recovery 各 n=1；(3) 讨论 Qwen 家族特异性的可能。\n\n**MF-3** [R2-N3, R1 AGREE] **Out-of-sample 验证仅覆盖 Immune（四类中最不 interesting 的一类）**\n\nLLaMA-3.1-8B 被分类为 Immune——最容易验证的模式（不受影响即可）。Collapse、V-recovery、Benefit 三类均无独立家族的 OOS 验证。Limitations 未列此为局限。\n\n**建议**：(1) 在 Limitations 中明确承认 OOS 验证的局限性；(2) 讨论验证其他模式的条件和计划。\n\n### Should-Fix（7 项，影响评分但不一票否决）\n\n**SF-1** [R1-W1, R2 AGREE] **AUGMENT 模式的数据量混淆未讨论**。d000=50k→d100≈66.5k (+33.1%)，高 dosage 准确率提升可能部分来自更多训练数据。DiD 控制了 item-level 混淆，但 aggregate-level 混淆（尤其影响 Benefit 和 V-recovery 解释）未被讨论。Limitations 应补充。\n\n**SF-2** [R1-W2, R2 AGREE] **γ 参数化选择（outside a_i）未论证**。论文采用 σ(a_i(θ-b)+γ·e)，标准 DIF 为 σ(a_i(θ-b+γ·e))。两种形式含义不同（logit-constant vs ability-constant）。如果全局能力调节是主要机制（DiD 证据支持），标准参数化可能更合适。需讨论选择理由。\n\n**SF-3** [R1-W3, R2 AGREE] **MMLU PPP=0.16-0.25 仅在 Appendix K，主文未报告**。论文核心模型在 MMLU（主要分析基准）上 PPP 显著低于理想值 0.5，但主文仅报告了 ARC 的 PPP=0.003。两个 benchmark 的 IRT 模型均存在拟合问题应在正文提及。\n\n**SF-4** [R2-W2, R1 AGREE] **方法新颖性定位不够明确**。2PL+γ 是标准 explanatory IRT/DIF 在 LLM 评估中的应用，IRT 建模层面无技术创新。论文应在 §3.3 或 §6 明确定位：新颖性在于受控注入实验设计和实证发现，而非 IRT 模型本身。\n\n**SF-5** [R2-W3, R1 AGREE] **与 Han et al. (2026) 和 Schaeffer et al. (2026) 的比较不充分**。Han et al.（DIF-based contamination quantification）和 Schaeffer et al.（pretraining-stage controlled injection）是最直接的竞争/互补工作，当前仅一句话提及。需要方法论层面的显式对比。\n\n**SF-6** [R1-W4, R2 AGREE] **LoRA r=16 参数比例未量化报告**。Limitations 定性讨论了 Phi-4 vs Qwen-14B 反驳，但未报告各模型实际可训练参数百分比。\n\n**SF-7** [R1-W5, R2 AGREE] **300/14,042 MMLU item 子集的代表性**。IRT 在 2.1% 的 MMLU items 上拟合（选择标准为 exposure 方差最大化），引入选择偏差。低 exposure 变异 items 的污染效应可能不同。\n\n### Minor（8 项）\n\n- **m1**: \"taxonomy\"/\"profiles\"/\"patterns\" 术语交替使用，建议统一。[R2-M1, R1 AGREE]\n- **m2**: Algorithm 1 阈值（τ=2pp, σ=5pp）无理论推导。Appendix P grid sweep 已验证稳定性，但正文应简要说明参数设定理据。[R1-M4, R2 AGREE]\n- **m3**: Figure 1 各 panel y 轴范围不同，可能误导 effect size 感知。[R2-M4, R1 AGREE]\n- **m4**: GSM8K 评估 max_new_tokens=256 可能截断 CoT，附录已 caveat 但主文应提及。[R1-M5, R2 AGREE]\n- **m5**: n=3 seeds CI 宽度 1.5-14.5pp 限制精度，但方向一致性标准合理。[R1-M3, R2 AGREE]\n- **m6**: 5%→25% 剂量间距跳跃可能遗漏 V-recovery 拐点。[R1-M2, R2 AGREE]\n- **m7**: RRF vs 学习型融合方法对比缺失，但信号正交性（|ρ|<0.06）和消融已充分支持。[R1-M1, R2 AGREE]\n- **m8**: Contribution 2（null result）的 Abstract 表述可被误读为 positive 发现。[R2-M2, R1 partial rebut]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识（均标注 [AGREE]）：\n\n1. **J=16 先验主导问题是全文最重要的技术发现** [MF-1]——P(γ<0) 数值不一致直接影响论文四大发现之一的可信度\n2. **Taxonomy 过度泛化** [MF-2]——N=5, Collapse n=1, V-recovery n=1, \"taxonomy\" 措辞过强\n3. **OOS 验证不足** [MF-3]——仅覆盖 Immune，最不 interesting 的一类\n4. **定性贡献稳健** [Strengths 1-6]——受控注入设计、核心发现、DiD 分析、cross-benchmark transfer 均获两人认可\n5. **AUGMENT 混淆** [SF-1]、**γ 参数化** [SF-2]、**PPP 报告** [SF-3]、**新颖性定位** [SF-4]、**相关工作** [SF-5]——7 个 Should-Fix 全部达成共识\n\n---\n\n## Reviewer Divergence\n\n**R2-N2: ContamCal 校准 MAE 不优于 Raw Accuracy** [DIVERGENT]\n\n- **R2 立场 [Must-Fix]**：Table 4 B0 Raw MAE=0.006 vs ContamCal MAE=0.009。核心方法在校准指标上未超越 baseline，削弱方法贡献的实用价值声称。\n- **R1 立场 [Not an issue]**：论文 §3.3 明确预测并解释了这一结果——\"Eq.3 depends on θ_j, not γ directly, predicting that vanilla 2PL (γ=0) achieves comparable calibration to 2PL+γ, with γ_k serving diagnosis rather than calibration.\" Table 4 的结果是理论一致性的验证而非缺陷。ContamCal 的价值在于域级诊断（Social Sciences γ_ss=-0.63），非数值校准。\n- **Director 判定**：R1 的 rebut 有力——论文确实在 method section 预测了这一结果并定位 γ 为诊断工具。但 R2 的关注也合理：如果 ContamCal 的校准不优于 raw，且其诊断价值（γ）受先验主导影响（MF-1），则方法的整体 practical value 需要更清晰的定位。**降级为 Should-Fix**：建议在 §5.5 显式阐明 ContamCal 的价值主张是诊断而非校准，并可选地按受影响/未受影响模型分层报告 MAE。\n\n---\n\n## Questions\n\n1. Section 5.7 的 P(γ<0)=99.7% 与 Appendix K Table 10 的 P(γ<0)=98.48% 差异的具体来源是什么？是否使用了不同的 J、item subset 或 MCMC 配置？\n2. 是否考虑过 REPLACE 模式（等量替换基础 SFT 数据）以消除数据量混淆？如果未做，原因是什么？\n3. 为什么选择 γ 在 a_i 括号外的参数化？是否有预实验显示此形式拟合更优？\n4. LLaMA-3.1-8B (53.5%) 的 Immune 与 OLMo-2 (53.8%) 的 Benefit 在 baseline 几乎相同——作者对这种差异的 mechanistic 解释是什么？论文提到 \"family-level factors\" 但未具体化。\n\n---\n\n## Missing References\n\nR2 验证了 58 条引用，无虚假引用。当前引用覆盖已显著改善。以下参考建议确认：\n- Golchin & Surdeanu (ICLR 2024) — 时间戳引用\n- Sainz et al. (EMNLP 2023 Findings) — contamination survey\n- Yang et al. (2023) — rethinking benchmark contamination\n- 以上在 Round 8 action items 中标注 open，需确认是否已全部添加\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未返回**（pending since 2026-05-21T17:14:04Z）\n\n外部审稿请求已发送至用户群，当前仍在等待。本报告不等待外部审稿。如用户后续提交 paperreview.ai 审稿结果，可作为补充参考。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（2026-05-21T17:17:35Z）。0 critical / 4 warning / 14 info。\n\n**Warnings**:\n1. **Page 2**: Figure 1 图例文字偏小，5 条线标签打印时可能难以辨认。建议放大图例字号或移至图内空白区域。\n2. **Page 8**: 页面过度密集——2 个 table + 1 个 figure + 4 个 section。Figure 2 被压缩，标签可能低于可读阈值。\n3. **Page 13**: Figure 4（Signal Reliability heatmap）单元格内数字 ≤6pt，打印需放大镜。建议改为 figure* 全宽。\n4. **Page 17**: Figure 7 和 Figure 8 共挤一页，axis label 极小，严重影响可读性。建议分页。\n\n**其他确认**：格式合规（ACL template, double-blind, 8 页正文, Limitations/Ethics 完整），无 margin 溢出、公式渲染错误或未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5（高）——两位 Reviewer 独立收敛于相同评估，交叉回应后共识充分**\n\n**理由**：\n\n论文的**定性贡献**是真实且有价值的：受控注入实验设计在 contamination 文献中是首创性的系统性工作，\"contamination ≠ inflation\" 的核心发现挑战了社区默认假设，DiD 分析严谨，cross-benchmark transfer 分析丰富了理解。实验规模（50+ checkpoints, 3 benchmarks, 3 seeds）和 Appendix 的详尽程度体现了扎实的研究工程。\n\n但论文存在**三个 Must-Fix 问题**使其目前不适合 Conference track：\n1. **IRT 定量结论脆弱**——J=16 先验主导，P(γ<0) 数值不一致，Bonferroni 声明与自身数据矛盾。Domain-level heterogeneity 是核心贡献之一，但其统计基础在当前版本中不可靠。\n2. **Taxonomy 声称过度**——N=5, Collapse/V-recovery 各 n=1 且来自同一家族，\"taxonomy\" 措辞暗示的泛化性缺乏支撑。\n3. **OOS 验证不足**——仅验证了最 trivial 的 Immune 模式。\n\n这些问题是**可修复的**（主要涉及 reframing/caveating 和数值核查，不需要新实验），修复后论文的 soundness 会显著改善。当前版本适合 Findings track，修订后有潜力达到 Borderline Conference (3.5)。\n\n**评分参考**（EMNLP 2026 ARR）：\n- 3.0 = Findings（可被 Findings 接收）\n- 3.5 = Borderline Conference\n- 4.0 = Conference（可被主会议接收）\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"four qualitatively different dose-response patterns\" 应加 \"in our five-family sample\" 或替换 \"taxonomy\" 为 \"profiles\" [MF-2]\n- Contribution 1 中 \"Out-of-sample validation... provides preliminary evidence for generalizability\" 应明确仅覆盖 Immune [MF-3]\n\n### Section 3.3 (Method: IRT)\n- Eq.2 的 γ 参数化选择需要论证段落 [SF-2]\n- 添加定位语句：\"Our modeling contribution is not in the IRT specification itself—which follows standard explanatory IRT—but in the controlled injection design.\" [SF-4]\n\n### Section 4.1 (Experimental Setup)\n- 报告每个 dosage 的总训练集大小（d000=50k, d005≈50.8k, ..., d100≈66.5k）[SF-1]\n- 报告每个模型的 LoRA 可训练参数百分比 [SF-6]\n\n### Section 5.5 (Calibration Quality)\n- 报告 MMLU PPP=0.16-0.25 并简要讨论 [SF-3]\n- 阐明 ContamCal 价值主张为诊断而非校准 [divergence resolution]\n\n### Section 5.7 (Domain-Level Analysis)\n- 解决 P(γ<0) 99.7% vs 98.48% 不一致 [MF-1]\n- 将 \"crossing the Bonferroni-corrected threshold\" 降级 [MF-1]\n- 标记所有 γ 结论为 exploratory [MF-1]\n\n### Section 6 (Discussion)\n- 扩展 Han et al. 和 Schaeffer et al. 比较 [SF-5]\n\n### Limitations\n- 补充 AUGMENT 模式数据量混淆 [SF-1]\n- 补充 OOS 验证仅覆盖 Immune [MF-3]\n- 补充 300-item 子集代表性 [SF-7]\n\n### Abstract\n- 替换 \"taxonomy\" 相关措辞 [MF-2]\n- 确认 P(γ<0) 数值与正文一致 [MF-1]",
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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "report": "# 审稿报告 — Round 10 (Fresh Review)\n\n**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n**Venue**: EMNLP 2026 via ARR May 2026\n**审稿模式**: Fresh（重新审稿，无历史上下文）\n**Reviewer 配置**: 2 人（R1 方法严谨性+实验设计+统计分析 / R2 新颖性+完整性+相关工作+写作质量）\n**轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识，无需进入 Round 2\n\n---\n\n## Summary\n\n本文对\"benchmark contamination 是否统一 inflate 模型分数\"这一社区默认假设进行了系统性实证检验。通过受控 SFT 注入（LoRA, 5 个剂量水平）对 5 个模型家族（4 个独立实验室，7B-14.7B）进行实验，发现 contamination 产生质的不同剂量-反应模式——从 Immune（Phi-4, ±0.5pp）到 Collapse（Qwen-14B, -9 to -25pp）。论文进一步提出 ContamCal 两阶段管线（多信号 RRF exposure mapping + contamination-augmented IRT），提供域级污染诊断。DiD 分析在 MMLU 上未发现 item-specific memorization（MDES 1.2-2.0pp），支持全局能力调节而非记忆化机制。\n\n---\n\n## Strengths\n\n1. **受控注入实验设计是核心优势**。在 contamination 文献中大多为观察性研究的背景下，本文通过 controlled SFT injection 实现了对 dosage 的精确控制（5 个水平 × 5 个家族 × 3 seeds），使因果推断成为可能。这是相对于 Han et al. (2026) 观察性 DIF 和其他检测方法的本质优势。[R1, R2 共识]\n\n2. **\"contamination ≠ inflation\" 的核心发现有实际意义**。4 种定性不同的剂量-反应模式（Immune, Collapse, V-recovery, Benefit）挑战了社区默认假设，对 leaderboard 解读和模型评估实践有直接影响。Table 1 和 Figure 1 清晰呈现了这一发现。[R1, R2 共识]\n\n3. **DiD 分析严谨**。Treated vs untreated items 的差分-差分检验逻辑清晰，post-hoc power analysis（MDES）正确计算和解读，ARC 的低功效被恰当标注。\"No detectable item-specific memorization at current power levels\" 的表述诚实且 bounded。[R1 评级 Acceptable]\n\n4. **Cross-benchmark transfer 分析丰富了理解**。MMLU-targeted contamination 对 GSM8K 的正迁移（所有非排除家族 +1 to +16pp）和方向反转（Qwen-7B: MMLU -1.8pp 但 GSM8K +10.1pp）是有价值的实证发现。[R1, R2 共识]\n\n5. **信号失效特征化有实践价值**。Min-K%++ 在 0.5B 处的方向反转（Cohen's d = -1.55 to -1.98）对使用 membership inference 做 contamination detection 的实践者有直接警示意义。[R2 特别标注]\n\n6. **统计方法论透明度高**。论文诚实报告了 CI over-coverage (83%)、PPP 值、MDES、先验敏感度、Appendix K \"exploratory status\" 等局限。11 页 Appendix 覆盖了 robustness checks、sensitivity analyses、parametric DR model comparison 等。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 项，影响接收决定）\n\n**MF-1** [R1-N1, R2 AGREE] **J=16 先验主导 + P(γ<0) 数值不一致 + Bonferroni 显著性声明不稳健**\n\n论文在 J=16 配置下的 IRT 定量结论存在三层问题：\n- **先验主导**：Appendix K 承认 \"J=16 provides insufficient data to override the prior\"，后验均值跨先验变化 2.6×（0.34→0.89），50% CI over-coverage 达 83%。\n- **数值不一致**：Section 5.7 报告 Social Sciences P(γ<0)=99.7%，但 Appendix K Table 10 在同一 N(0,1) 先验下显示 P(γ<0)=98.48%。ESS>3800 排除 MCMC 随机变异，差异来源未解释。\n- **Bonferroni 声明不成立**：8 次检验的 Bonferroni 阈值为 P>99.375%。Table 10 的 98.48% 未达标；即使取最宽松先验 N(0,2) 的 98.95% 仍未达标。Section 5.7 \"crossing the Bonferroni-corrected threshold\" 声明与论文自己的先验敏感性数据矛盾。\n\n**建议**：(1) 解决 §5.7 与 Table 10 的数值差异来源；(2) 报告 P(γ<0) 范围而非单一值；(3) 将 Bonferroni 声明降级为 \"approaching Bonferroni significance\"；(4) 主文中所有 γ 定量结论标记为 exploratory。\n\n**MF-2** [R2-N1, R1 AGREE] **N=5 家族归纳 4 类 taxonomy 的统计基础不足**\n\n四类分类中 Collapse 仅 Qwen-14B（n=1），V-recovery 仅 Qwen-7B（n=1），两者均来自同一 Qwen2.5 家族。无法排除这两种模式是 Qwen 架构特异性行为。论文 §5.1 写 \"This empirical taxonomy is preliminary at N=5 families\" 是诚实的，但 Abstract 和 Introduction 使用 \"four qualitatively different dose-response patterns\" 和 \"taxonomy\" 时 scoping 不足。Section 6 \"Two of four patterns attested in ≥2 independent families\" 有误导性——Benefit 的两个实例（OLMo-2, Gemma-2）均为 construction 家族，非 OOS。\n\n**建议**：(1) Abstract/Introduction 将 \"taxonomy\" 替换为 \"profiles\" 或 \"observed patterns\"；(2) 明确承认 Collapse/V-recovery 各 n=1；(3) 讨论 Qwen 家族特异性的可能。\n\n**MF-3** [R2-N3, R1 AGREE] **Out-of-sample 验证仅覆盖 Immune（四类中最不 interesting 的一类）**\n\nLLaMA-3.1-8B 被分类为 Immune——最容易验证的模式（不受影响即可）。Collapse、V-recovery、Benefit 三类均无独立家族的 OOS 验证。Limitations 未列此为局限。\n\n**建议**：(1) 在 Limitations 中明确承认 OOS 验证的局限性；(2) 讨论验证其他模式的条件和计划。\n\n### Should-Fix（7 项，影响评分但不一票否决）\n\n**SF-1** [R1-W1, R2 AGREE] **AUGMENT 模式的数据量混淆未讨论**。d000=50k→d100≈66.5k (+33.1%)，高 dosage 准确率提升可能部分来自更多训练数据。DiD 控制了 item-level 混淆，但 aggregate-level 混淆（尤其影响 Benefit 和 V-recovery 解释）未被讨论。Limitations 应补充。\n\n**SF-2** [R1-W2, R2 AGREE] **γ 参数化选择（outside a_i）未论证**。论文采用 σ(a_i(θ-b)+γ·e)，标准 DIF 为 σ(a_i(θ-b+γ·e))。两种形式含义不同（logit-constant vs ability-constant）。如果全局能力调节是主要机制（DiD 证据支持），标准参数化可能更合适。需讨论选择理由。\n\n**SF-3** [R1-W3, R2 AGREE] **MMLU PPP=0.16-0.25 仅在 Appendix K，主文未报告**。论文核心模型在 MMLU（主要分析基准）上 PPP 显著低于理想值 0.5，但主文仅报告了 ARC 的 PPP=0.003。两个 benchmark 的 IRT 模型均存在拟合问题应在正文提及。\n\n**SF-4** [R2-W2, R1 AGREE] **方法新颖性定位不够明确**。2PL+γ 是标准 explanatory IRT/DIF 在 LLM 评估中的应用，IRT 建模层面无技术创新。论文应在 §3.3 或 §6 明确定位：新颖性在于受控注入实验设计和实证发现，而非 IRT 模型本身。\n\n**SF-5** [R2-W3, R1 AGREE] **与 Han et al. (2026) 和 Schaeffer et al. (2026) 的比较不充分**。Han et al.（DIF-based contamination quantification）和 Schaeffer et al.（pretraining-stage controlled injection）是最直接的竞争/互补工作，当前仅一句话提及。需要方法论层面的显式对比。\n\n**SF-6** [R1-W4, R2 AGREE] **LoRA r=16 参数比例未量化报告**。Limitations 定性讨论了 Phi-4 vs Qwen-14B 反驳，但未报告各模型实际可训练参数百分比。\n\n**SF-7** [R1-W5, R2 AGREE] **300/14,042 MMLU item 子集的代表性**。IRT 在 2.1% 的 MMLU items 上拟合（选择标准为 exposure 方差最大化），引入选择偏差。低 exposure 变异 items 的污染效应可能不同。\n\n### Minor（8 项）\n\n- **m1**: \"taxonomy\"/\"profiles\"/\"patterns\" 术语交替使用，建议统一。[R2-M1, R1 AGREE]\n- **m2**: Algorithm 1 阈值（τ=2pp, σ=5pp）无理论推导。Appendix P grid sweep 已验证稳定性，但正文应简要说明参数设定理据。[R1-M4, R2 AGREE]\n- **m3**: Figure 1 各 panel y 轴范围不同，可能误导 effect size 感知。[R2-M4, R1 AGREE]\n- **m4**: GSM8K 评估 max_new_tokens=256 可能截断 CoT，附录已 caveat 但主文应提及。[R1-M5, R2 AGREE]\n- **m5**: n=3 seeds CI 宽度 1.5-14.5pp 限制精度，但方向一致性标准合理。[R1-M3, R2 AGREE]\n- **m6**: 5%→25% 剂量间距跳跃可能遗漏 V-recovery 拐点。[R1-M2, R2 AGREE]\n- **m7**: RRF vs 学习型融合方法对比缺失，但信号正交性（|ρ|<0.06）和消融已充分支持。[R1-M1, R2 AGREE]\n- **m8**: Contribution 2（null result）的 Abstract 表述可被误读为 positive 发现。[R2-M2, R1 partial rebut]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识（均标注 [AGREE]）：\n\n1. **J=16 先验主导问题是全文最重要的技术发现** [MF-1]——P(γ<0) 数值不一致直接影响论文四大发现之一的可信度\n2. **Taxonomy 过度泛化** [MF-2]——N=5, Collapse n=1, V-recovery n=1, \"taxonomy\" 措辞过强\n3. **OOS 验证不足** [MF-3]——仅覆盖 Immune，最不 interesting 的一类\n4. **定性贡献稳健** [Strengths 1-6]——受控注入设计、核心发现、DiD 分析、cross-benchmark transfer 均获两人认可\n5. **AUGMENT 混淆** [SF-1]、**γ 参数化** [SF-2]、**PPP 报告** [SF-3]、**新颖性定位** [SF-4]、**相关工作** [SF-5]——7 个 Should-Fix 全部达成共识\n\n---\n\n## Reviewer Divergence\n\n**R2-N2: ContamCal 校准 MAE 不优于 Raw Accuracy** [DIVERGENT]\n\n- **R2 立场 [Must-Fix]**：Table 4 B0 Raw MAE=0.006 vs ContamCal MAE=0.009。核心方法在校准指标上未超越 baseline，削弱方法贡献的实用价值声称。\n- **R1 立场 [Not an issue]**：论文 §3.3 明确预测并解释了这一结果——\"Eq.3 depends on θ_j, not γ directly, predicting that vanilla 2PL (γ=0) achieves comparable calibration to 2PL+γ, with γ_k serving diagnosis rather than calibration.\" Table 4 的结果是理论一致性的验证而非缺陷。ContamCal 的价值在于域级诊断（Social Sciences γ_ss=-0.63），非数值校准。\n- **Director 判定**：R1 的 rebut 有力——论文确实在 method section 预测了这一结果并定位 γ 为诊断工具。但 R2 的关注也合理：如果 ContamCal 的校准不优于 raw，且其诊断价值（γ）受先验主导影响（MF-1），则方法的整体 practical value 需要更清晰的定位。**降级为 Should-Fix**：建议在 §5.5 显式阐明 ContamCal 的价值主张是诊断而非校准，并可选地按受影响/未受影响模型分层报告 MAE。\n\n---\n\n## Questions\n\n1. Section 5.7 的 P(γ<0)=99.7% 与 Appendix K Table 10 的 P(γ<0)=98.48% 差异的具体来源是什么？是否使用了不同的 J、item subset 或 MCMC 配置？\n2. 是否考虑过 REPLACE 模式（等量替换基础 SFT 数据）以消除数据量混淆？如果未做，原因是什么？\n3. 为什么选择 γ 在 a_i 括号外的参数化？是否有预实验显示此形式拟合更优？\n4. LLaMA-3.1-8B (53.5%) 的 Immune 与 OLMo-2 (53.8%) 的 Benefit 在 baseline 几乎相同——作者对这种差异的 mechanistic 解释是什么？论文提到 \"family-level factors\" 但未具体化。\n\n---\n\n## Missing References\n\nR2 验证了 58 条引用，无虚假引用。当前引用覆盖已显著改善。以下参考建议确认：\n- Golchin & Surdeanu (ICLR 2024) — 时间戳引用\n- Sainz et al. (EMNLP 2023 Findings) — contamination survey\n- Yang et al. (2023) — rethinking benchmark contamination\n- 以上在 Round 8 action items 中标注 open，需确认是否已全部添加\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未返回**（pending since 2026-05-21T17:14:04Z）\n\n外部审稿请求已发送至用户群，当前仍在等待。本报告不等待外部审稿。如用户后续提交 paperreview.ai 审稿结果，可作为补充参考。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（2026-05-21T17:17:35Z）。0 critical / 4 warning / 14 info。\n\n**Warnings**:\n1. **Page 2**: Figure 1 图例文字偏小，5 条线标签打印时可能难以辨认。建议放大图例字号或移至图内空白区域。\n2. **Page 8**: 页面过度密集——2 个 table + 1 个 figure + 4 个 section。Figure 2 被压缩，标签可能低于可读阈值。\n3. **Page 13**: Figure 4（Signal Reliability heatmap）单元格内数字 ≤6pt，打印需放大镜。建议改为 figure* 全宽。\n4. **Page 17**: Figure 7 和 Figure 8 共挤一页，axis label 极小，严重影响可读性。建议分页。\n\n**其他确认**：格式合规（ACL template, double-blind, 8 页正文, Limitations/Ethics 完整），无 margin 溢出、公式渲染错误或未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5（高）——两位 Reviewer 独立收敛于相同评估，交叉回应后共识充分**\n\n**理由**：\n\n论文的**定性贡献**是真实且有价值的：受控注入实验设计在 contamination 文献中是首创性的系统性工作，\"contamination ≠ inflation\" 的核心发现挑战了社区默认假设，DiD 分析严谨，cross-benchmark transfer 分析丰富了理解。实验规模（50+ checkpoints, 3 benchmarks, 3 seeds）和 Appendix 的详尽程度体现了扎实的研究工程。\n\n但论文存在**三个 Must-Fix 问题**使其目前不适合 Conference track：\n1. **IRT 定量结论脆弱**——J=16 先验主导，P(γ<0) 数值不一致，Bonferroni 声明与自身数据矛盾。Domain-level heterogeneity 是核心贡献之一，但其统计基础在当前版本中不可靠。\n2. **Taxonomy 声称过度**——N=5, Collapse/V-recovery 各 n=1 且来自同一家族，\"taxonomy\" 措辞暗示的泛化性缺乏支撑。\n3. **OOS 验证不足**——仅验证了最 trivial 的 Immune 模式。\n\n这些问题是**可修复的**（主要涉及 reframing/caveating 和数值核查，不需要新实验），修复后论文的 soundness 会显著改善。当前版本适合 Findings track，修订后有潜力达到 Borderline Conference (3.5)。\n\n**评分参考**（EMNLP 2026 ARR）：\n- 3.0 = Findings（可被 Findings 接收）\n- 3.5 = Borderline Conference\n- 4.0 = Conference（可被主会议接收）\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"four qualitatively different dose-response patterns\" 应加 \"in our five-family sample\" 或替换 \"taxonomy\" 为 \"profiles\" [MF-2]\n- Contribution 1 中 \"Out-of-sample validation... provides preliminary evidence for generalizability\" 应明确仅覆盖 Immune [MF-3]\n\n### Section 3.3 (Method: IRT)\n- Eq.2 的 γ 参数化选择需要论证段落 [SF-2]\n- 添加定位语句：\"Our modeling contribution is not in the IRT specification itself—which follows standard explanatory IRT—but in the controlled injection design.\" [SF-4]\n\n### Section 4.1 (Experimental Setup)\n- 报告每个 dosage 的总训练集大小（d000=50k, d005≈50.8k, ..., d100≈66.5k）[SF-1]\n- 报告每个模型的 LoRA 可训练参数百分比 [SF-6]\n\n### Section 5.5 (Calibration Quality)\n- 报告 MMLU PPP=0.16-0.25 并简要讨论 [SF-3]\n- 阐明 ContamCal 价值主张为诊断而非校准 [divergence resolution]\n\n### Section 5.7 (Domain-Level Analysis)\n- 解决 P(γ<0) 99.7% vs 98.48% 不一致 [MF-1]\n- 将 \"crossing the Bonferroni-corrected threshold\" 降级 [MF-1]\n- 标记所有 γ 结论为 exploratory [MF-1]\n\n### Section 6 (Discussion)\n- 扩展 Han et al. 和 Schaeffer et al. 比较 [SF-5]\n\n### Limitations\n- 补充 AUGMENT 模式数据量混淆 [SF-1]\n- 补充 OOS 验证仅覆盖 Immune [MF-3]\n- 补充 300-item 子集代表性 [SF-7]\n\n### Abstract\n- 替换 \"taxonomy\" 相关措辞 [MF-2]\n- 确认 P(γ<0) 数值与正文一致 [MF-1]",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-21T17:41:39.968744+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4065
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-21T17:41:44.824655+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting cross-sharing responses'}, {'content': 'Step 3: Convergence judgment', 'status': 'completed', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'completed', 'activeForm': 'Synthesizing final report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Collect Round 1 reviews from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting Round 1 reviews'}, {'content': \"Cross-sharing: send each Reviewer's review to the other for response\", 'status': 'completed', 'activeForm': 'Cross-sharing reviews between Reviewers'}, {'content': 'Collect cross-sharing responses from both Reviewers', 'status': 'completed', 'activeForm': 'Collecting cross-sharing responses'}, {'content': 'Step 3: Convergence judgment', 'status': 'completed', 'activeForm': 'Judging convergence'}, {'content': 'Step 4: Synthesize report, update issue tracker, submit', 'status': 'completed', 'activeForm': 'Synthesizing final report'}]"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-21T17:41:44.875371+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 882 · 2026-05-21T17:41:55.387800+00:00_

审稿完成。报告已投递至 Research Director。

**评分：3.0 / 5（Findings）**

核心结论：
- **3 个 Must-Fix**：(1) J=16 先验主导 + P(γ<0) 数值不一致 + Bonferroni 声明不成立；(2) N=5 家族归纳 4 类 taxonomy 统计基础不足（Collapse/V-recovery 各 n=1，均来自 Qwen）；(3) OOS 验证仅覆盖 Immune
- **7 个 Should-Fix**：AUGMENT 数据量混淆、γ 参数化未论证、MMLU PPP 未报告、方法新颖性定位、Han/Schaeffer 比较不充分、LoRA 参数比例未量化、300-item 子集代表性
- **1 个分歧**：ContamCal MAE 逊于 raw accuracy——R2 认为是方法缺陷，R1 认为论文已预测并定位 γ 为诊断工具。降级为 Should-Fix
- **外部审稿**：未返回
- **视觉审查**：0 critical / 4 warning（Figure 图例偏小、Page 8 过密、Appendix 图表拥挤）

论文定性贡献（受控注入设计、"contamination ≠ inflation"、DiD 分析）稳健且有价值。Must-Fix 问题均可通过 reframing/caveating 和数值核查修复，不需要新实验。修复后有潜力提升至 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 85

## Round 85

2 recorded events


### User

_source line 883 · 2026-05-21T17:41:57.891530+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**总结**：R1 的 11 个问题我全部标注为 **[AGREE]**，无 REBUT。

R1 的技术审查在 IRT 建模层面比我更深入——特别是三个我未发现的问题：
1. **N1** P(γ<0) 在正文 (99.7%) 与 Appendix K Table 10 (98.48%) 之间的数值不一致，直接导致 Bonferroni 显著性声明不成立
2. **W1** AUGMENT 模式的数据量混淆（d100 较 d000 多 33%），Limitations 未讨论
3. **W2** γ 放在 a_i 括号外 vs 内部的参数化选择未论证

我的审稿在 claim-evidence 匹配层面覆盖了 R1 未涉及的三个核心问题（N=5 taxonomy 泛化、ContamCal MAE 逊于 raw accuracy、OOS 验证仅覆盖 Immune）。两份审稿互补性强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 884 · 2026-05-21T17:42:09.035669+00:00_

审稿报告已投递至 Research Director。

**审稿完成摘要**：

- **评分**：3.0 / 5（Findings）
- **置信度**：4/5（高——两位 Reviewer 独立收敛，交叉回应后共识充分）
- **流程**：1 轮初审 + 1 轮交叉分享，13 个关键问题中 12 个达成共识，1 个分歧已记录（ContamCal MAE，降级为 Should-Fix）

**核心判断**：论文定性贡献（受控注入设计、"contamination ≠ inflation" 发现、DiD 分析）真实有价值，但 3 个 Must-Fix 问题（P(γ<0) 数值不一致 + Bonferroni 声明不成立、N=5 taxonomy 过度泛化、OOS 验证仅覆盖 Immune）使其目前不适合 Conference track。问题均可修复（reframing + 数值核查），修订后有潜力升至 Borderline Conference。

外部审稿（Stanford Agentic Reviewer）仍在等待，不阻塞本报告。视觉审查已完成（4 warning），findings 已纳入报告。Issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 86

## Round 86

2 recorded events


### User

_source line 885 · 2026-05-22T18:43:33.846707+00:00_

[飞书用户 曹晓玉 (ou_24841335582d4f08664bbf2a47fb258b)]: 咋样了

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "feishu:oc_da6d629d7f92da47a5e85cb7e296ae13"
}
```

</details>

---


### Assistant

_source line 886 · 2026-05-22T18:44:02.032834+00:00_

审稿已全部完成，报告已投递给 Research Director。

**Round 10 (Fresh Review) 结果摘要**：

| 项目 | 结果 |
|------|------|
| Overall 评分 | **3.0 (Findings)** |
| 置信度 | 4/5（高） |
| Reviewer 配置 | 2 人，1 轮初审 + 1 轮交叉分享后收敛 |
| Must-Fix | 3 项 |
| Should-Fix | 7 项 |
| Minor | 8 项 |

**3 个 Must-Fix**：
1. **P(γ<0) 数值不一致**——§5.7 报 99.7% 但 Appendix K Table 10 报 98.48%，Bonferroni 显著性声明与自身数据矛盾
2. **N=5 taxonomy 过度泛化**——Collapse/V-recovery 各 n=1 且来自同一 Qwen 家族，"taxonomy" 措辞过强
3. **OOS 验证仅覆盖 Immune**——四类中最 trivial 的一类

这些都是**可修复的**（reframing + 数值核查，不需新实验）。修复后有潜力从 3.0 升至 3.5 (Borderline Conference)。

Issue Tracker 已同步更新，视觉审查已完成（0 critical），外部审稿仍在等待。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 87

## Round 87

44 recorded events


### User

_source line 887 · 2026-05-22T22:46:01.869598+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contamcal-irt-calibration
- 论文路径: projects/contamcal-irt-calibration/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings unified)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-22T22:46:10.721954+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-22T22:46:10.772898+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-22T22:46:16.648647+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-22T22:46:16.699243+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-22T22:46:22.171794+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-22T22:46:22.272649+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-22T22:46:32.309820+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-22T22:46:34.217104+00:00_

{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (427 个)\n\n- **exp_001_sft_d100_05B**: DONE (success) — \n- **exp_001_sft_0pct**: DONE (success) — \n- **exp_001_sft_0pct_3B_s123**: DONE (success) — \n- **exp_001_eval_15B_d000_s42**: DONE (failed) — \n- **exp_001_sft_d005_05B_v2**: DONE (failed) — \n- **exp_001_sft_d005_05B**: DONE (killed) — \n- **exp_001_sft_100pct_05B**: DONE (failed) — \n- **exp_001_sft_0pct_3B**: DONE (success) — \n- **exp_001_sft_injection**: DONE (success) — \n- **exp_001_sft_0pct_15B_s123**: DONE (success) — \n- **exp_001_sft_0pct_05B_s123**: DONE (success) — \n- **exp_001_sft_0pct_15B**: DONE (success) — \n- **exp_001_sft_0pct_05B**: DONE (success) — \n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| sft_falcon3_7b_d100_s123_v2 | Falcon3-7B-Base cross-seed replication (s123) at d100 (v2 restart). Tests Benefit pattern reproducibility for Table 11. Config: bs=1 ga=16 (matches s42). | — | — | — |\n\n## 待处理\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\n- eval_phi4_mmlu_arc_westd_v2: Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.（准备中）\n- gsm8k_phi4_s42_westd: GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.（准备中）\n- sft_gemma2_s0_sweep_v2（准备中）\n- falcon3-7b-download（准备中）\n- falcon3-7b-dl-v2（准备中）\n- falcon3-7b-dl-v3（准备中）\n- fa
…[truncated 2655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1907
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-22T22:46:34.217603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-22T22:46:34.318471+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{float}
15	
16	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{abstract}
25	\end{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{experimental_setup}
31	\input{results}
32	\input{conclusion}
33	
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-22T22:46:34.670255+00:00_

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
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-22T22:46:41.213096+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found search results related to EMNLP 2026, though the main call for papers for the conference itself didn't appear in these 
…[truncated 1188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 6542
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-22T22:46:46.183283+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 901 · 2026-05-22T22:46:47.137454+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 submission guidelines page limit template anonymity requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR 2026 submission guidelines page limit template anonymity requirements"
  }
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-22T22:46:49.547659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-22T22:46:49.548019+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{float}
15	
16	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{abstract}
25	\end{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{experimental_setup}
31	\input{results}
32	\input{conclusion}
33	
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 904 · 2026-05-22T22:46:51.907887+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the key information about the EMNLP 2026 main conference call for papers submission deadline via ARR:

## ARR Submission Deadline

The ARR submis
…[truncated 790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 5724
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-22T22:47:03.503028+00:00_

Web search results for query: "ARR 2026 submission guidelines page limit template anonymity requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here are the ARR 2026 submission guidelines regarding page limits, templates, and anonymity requirements:

## Page Limits

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices. Upon acceptance, long papers will be given one additional page of content (i.e. up to 9 pages) in the proceedings so that reviewers' comments can be taken into account. Papers should be desk-rejected if they go over the page limit (4 pages for short, 8 for long papers, excluding the ethical considerations and limitations).

## Templates

Submissions must adhere to the formatting in the submission templates, which is available as an Overleaf template. Paper submissions must use the official ACL style templates. The paper templates are available as an Overleaf template and
…[truncated 894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 16365
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-22T22:47:11.182184+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-22T22:47:13.140035+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1957
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-22T22:47:13.291554+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-22T22:47:14.095118+00:00_

-rw-r--r-- 1 ubuntu ubuntu 594284 May 22 17:33 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_9/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-22T22:47:14.095510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-22T22:47:14.497209+00:00_

1	Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into six models spanning five independent families (7B--14.7B parameters) and discover that contamination produces not one effect but a spectrum of dose-response patterns. Benefit ($+$2.4pp mean) and Immune ($\Delta < 1$\,percentage point [pp]) are replicated across independent families (three and two, respectively); more extreme responses---catastrophic collapse ($-$9 to $-$25pp across seeds) and V-recovery---are each observed in one family (Qwen2.5) across three seeds, requiring further replication. In our six-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band; models at extreme baselines show limited sensitivity. Counter-intuitively, the 14B Qwen model is 3$\times$ more fragile than 7B. These effects are benchmark-conditional: models harmed on MMLU can simultaneously benefit on GSM8K ($+$11pp), revealing asymmetric cross-benchmark transfer. Difference-in-differences analysis finds no item-specific memorization on MMLU (minimum detectable effect size 1.2--2.0pp); ARC has limited power (2.3--5.6pp). Profiles are robust: within-seed bootstrap stability exceeds 99.6\% for 4/5 MMLU families, though cross-seed sign consistency is 2/5. ARC-Challenge achieves 4/5 directional agreement despite its smaller item pool (1{,}172 vs.\ 14{,}042 items). We characterize contamination detection signal failure: Min-K\%++ exhibits directional reversal at small scales (paired Cohen's $d = -1.98$ at d100; $|d| > 1.4$ at d005), actively misleading practitioners. Simulation establishes that IRT-based contamination diagnosis requires ensemble sizes ($J \geq 50$) above current practice. Out-of-sample validation on a held-out sixth family (LLaMA-3.1-8B) confirms the profiles generalize: it is classified Immune despite a baseline matchi
…[truncated 375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-22T22:47:14.648375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-22T22:47:14.648890+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled SFT injection (LoRA, five dosage levels) into six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII) and discover a spectrum of dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4, $\pm$0.5pp) and benefit ($+$3--4pp, three families) to collapse in the 65--70\% baseline band (Qwen-14B, $-$9 to $-$25pp across seeds).
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig_dose_response.pdf}
10	\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; LLaMA-3.1 at seed$=$0 with d000/d025/d100; cross-seed patterns in Table~\ref{tab:cross_seed}). Vulnerability concentrates in the 65--70\% baseline band; models at extreme baselines show limited sensitivity. Qwen-14B is 3$\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref{sec:arc_cross_benchmark}.}
11	\label{fig:dose_response}
12	\end{figure*}
13	
14	In our six-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Falcon3 $+$4.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intui
…[truncated 1757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-22T22:47:23.484528+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-22T22:47:24.037437+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 217\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\
…[truncated 1463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-22T22:47:24.037912+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-22T22:47:24.038164+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-22T22:47:26.548294+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-22T22:47:27.954506+00:00_

&lt;persisted-output>
Output too large (33.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-director-c2ad40d8/c4cba88e-3018-42fe-97f9-4b7372c6aa5d/tool-results/boovuzf7y.txt

Preview (first 2KB):
- id: "R2-N1"
  summary: "Title/framing promises general answer but experiments only cover SFT ≤3B"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 6
  mentions:
    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices."}
    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'. Abstract implies contamination-specific modeling."}
    - {round: 4, reviewers: "R1,R2", note: "Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing."}
    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form but framing still inconsistent."}
    - {round: 6, reviewers: "R1,R2", note: "Title question form improved but still over-scopes."}
    - {round: 8, reviewers: "", note: "本轮未提及。D149+ rewrite resolved this issue. Title now 'Not All Models Are Inflated'."}
    - {round: 9, reviewers: "", note: "本轮未提及（fresh review）。Title framing no longer flagged."}
    - {round: 10, reviewers: "", note: "本轮未提及（fresh review）。Title framing resolved."}
  action_items:
    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
    - {round: 4, action: "Reframe as empirical investigation rather than method paper", assign
…[truncated 305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-22T22:47:28.055338+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null || grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND_IN_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null || grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND_IN_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-22T22:47:28.156647+00:00_

NOT_FOUND_IN_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-22T22:47:41.837065+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_SECTION\"",
  "description": "Check external review config section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_SECTION\"",
    "description": "Check external review config section"
  }
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-22T22:47:41.937995+00:00_

NO_EXTERNAL_REVIEW_SECTION

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-22T22:48:05.135469+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-22T22:48:22.262289+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17126
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-22T22:48:22.413391+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "contamcal-irt-calibration",
  "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**。\n\n## Venue 信息\n- **目标**：EMNLP 2026 via ACL Rolling Review (ARR)\n- **截止日期**：2026-05-25\n- **类型**：Long paper\n- **页数限制**：正文 8 页，参考文献无限，附录无限\n- **模板**：ACL style（`\\usepackage[review,hyperref]{acl}`）\n- **匿名规则**：Double-blind（无作者信息，自引匿名化）\n- **Limitations**：必写，不计入页数\n- **Ethics**：可选，不计入页数\n- **评分标准**：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**：Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**：projects/contamcal-irt-calibration/docs/paper/main.tex\n- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_9/submitted.pdf\n\n## 你的审查侧重\n请重点审查以下方面，但不限于此：\n\n1. **IRT 建模方法**：2PL+γ 模型的合理性、可识别性、与标准 IRT 的对比是否公平\n2. **Contamination injection 方法论**：SFT LoRA injection 的生态效度、dosage 设计是否合理、是否存在 confound\n3. **统计分析**：DiD 分析的功效、bootstrap 稳定性、cross-seed 一致性的解读是否恰当\n4. **实验充分性**：6 个模型 / 5 个家族是否足以支撑论文的 claims、out-of-sample validation 的说服力\n5. **Simulation 研究**：IRT 参数恢复的 simulation 设计是否充分、J≥50 的结论是否有足够支撑\n6. **Min-K++ 分析**：signal failure characterization 是否严谨、directional reversal 的解释是否合理\n7. **Reproducibility**：方法描述是否足以复现、超参数选择是否充分 justified\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 是重点——像顶会最严格的审稿人一样评估。每个 weakness 标注严重程度：[Critical] / [Major] / [Minor]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "contamcal-irt-calibration",
    "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**。\n\n## Venue 信息\n- **目标**：EMNLP 2026 via ACL Rolling Review (ARR)\n- **截止日期**：2026-05-25\n- **类型**：Long paper\n- **页数限制**：正文 8 页，参考文献无限，附录无限\n- **模板**：ACL style（`\\usepackage[review,hyperref]{acl}`）\n- **匿名规则**：Double-blind（无作者信息，自引匿名化）\n- **Limitations**：必写，不计入页数\n- **Ethics**：可选，不计入页数\n- **评分标准**：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**：Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**：projects/contamcal-irt-calibration/docs/paper/main.tex\n- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_9/submitted.pdf\n\n## 你的审查侧重\n请重点审查以下方面，但不限于此：\n\n1. **IRT 建模方法**：2PL+γ 模型的合理性、可识别性、与标准 IRT 的对比是否公平\n2. **Contamination injection 方法论**：SFT LoRA injection 的生态效度、dosage 设计是否合理、是否存在 confound\n3. **统计分析**：DiD 分析的功效、bootstrap 稳定性、cross-seed 一致性的解读是否恰当\n4. **实验充分性**：6 个模型 / 5 个家族是否足以支撑论文的 claims、out-of-sample validation 的说服力\n5. **Simulation 研究**：IRT 参数恢复的 simulation 设计是否充分、J≥50 的结论是否有足够支撑\n6. **Min-K++ 分析**：signal failure characterization 是否严谨、directional reversal 的解释是否合理\n7. **Reproducibility**：方法描述是否足以复现、超参数选择是否充分 justified\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 是重点——像顶会最严格的审稿人一样评估。每个 weakness 标注严重程度：[Critical] / [Major] / [Minor]。"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-22T22:48:32.471821+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10058
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-22T22:48:32.628944+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "contamcal-irt-calibration",
  "text": "你是 Reviewer 2，负责**新颖性、完整性与写作质量**。\n\n## Venue 信息\n- **目标**：EMNLP 2026 via ACL Rolling Review (ARR)\n- **截止日期**：2026-05-25\n- **类型**：Long paper\n- **页数限制**：正文 8 页，参考文献无限，附录无限\n- **模板**：ACL style（`\\usepackage[review,hyperref]{acl}`）\n- **匿名规则**：Double-blind（无作者信息，自引匿名化）\n- **Limitations**：必写，不计入页数\n- **Ethics**：可选，不计入页数\n- **评分标准**：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**：Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**：projects/contamcal-irt-calibration/docs/paper/main.tex\n- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_9/submitted.pdf\n\n## 你的审查侧重\n请重点审查以下方面，但不限于此：\n\n1. **新颖性**：相对于已有 contamination 文献（Oren et al. 2024, Dekoninck et al. 2024, Dong et al. 2024, Yang et al. 2023 等），本文的增量贡献是否足够 EMNLP\n2. **Related Work 覆盖**：是否遗漏重要相关工作（benchmark contamination detection, IRT in NLP, data poisoning, LLM evaluation）\n3. **Claim-Evidence 对齐**：Abstract/Introduction 中的 claims 是否都有对应实验支撑、是否 over-claim\n4. **写作质量**：结构是否清晰、信息密度是否合理、是否有冗余或逻辑跳跃\n5. **格式合规**：8 页限制、匿名性、引用格式、图表质量和可读性\n6. **Limitations 章节**：是否充分覆盖主要局限\n7. **论文叙事**：从 Introduction 到 Conclusion 的故事线是否连贯、motivation 是否充分\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 是重点——像顶会最严格的审稿人一样评估。每个 weakness 标注严重程度：[Critical] / [Major] / [Minor]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "contamcal-irt-calibration",
    "text": "你是 Reviewer 2，负责**新颖性、完整性与写作质量**。\n\n## Venue 信息\n- **目标**：EMNLP 2026 via ACL Rolling Review (ARR)\n- **截止日期**：2026-05-25\n- **类型**：Long paper\n- **页数限制**：正文 8 页，参考文献无限，附录无限\n- **模板**：ACL style（`\\usepackage[review,hyperref]{acl}`）\n- **匿名规则**：Double-blind（无作者信息，自引匿名化）\n- **Limitations**：必写，不计入页数\n- **Ethics**：可选，不计入页数\n- **评分标准**：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**：Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**：projects/contamcal-irt-calibration/docs/paper/main.tex\n- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_9/submitted.pdf\n\n## 你的审查侧重\n请重点审查以下方面，但不限于此：\n\n1. **新颖性**：相对于已有 contamination 文献（Oren et al. 2024, Dekoninck et al. 2024, Dong et al. 2024, Yang et al. 2023 等），本文的增量贡献是否足够 EMNLP\n2. **Related Work 覆盖**：是否遗漏重要相关工作（benchmark contamination detection, IRT in NLP, data poisoning, LLM evaluation）\n3. **Claim-Evidence 对齐**：Abstract/Introduction 中的 claims 是否都有对应实验支撑、是否 over-claim\n4. **写作质量**：结构是否清晰、信息密度是否合理、是否有冗余或逻辑跳跃\n5. **格式合规**：8 页限制、匿名性、引用格式、图表质量和可读性\n6. **Limitations 章节**：是否充分覆盖主要局限\n7. **论文叙事**：从 Introduction 到 Conclusion 的故事线是否连贯、motivation 是否充分\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 是重点——像顶会最严格的审稿人一样评估。每个 weakness 标注严重程度：[Critical] / [Major] / [Minor]。"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-22T22:48:33.989458+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1360
}
```

</details>

---


### Assistant

_source line 930 · 2026-05-22T22:48:46.452132+00:00_

Round 1 已启动，三项任务并行执行中：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验设计） | 🔄 审稿中 |
| Reviewer 2（新颖性 + 完整性 + 写作） | 🔄 审稿中 |
| 视觉审查 Agent | 🔄 执行中 |
| 外部审稿 (Stanford) | ⏭️ 未启用 |

等待两位 Reviewer 返回初审意见后，进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 88

## Round 88

2 recorded events


### User

_source line 931 · 2026-05-22T22:54:20.740932+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性与实验设计

**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 论文提出了 controlled contamination injection + IRT calibration 的系统框架，方法论有新意且实验较全面，但 SFT injection 的生态效度存在根本性质疑，几个核心 dose-response pattern 各仅由单一模型支撑，claims 的普适性不足以完全支撑"across model families"的标题承诺。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | IRT建模合理但有公式不一致；DiD分析有未检验的假设；核心pattern依赖单一模型 |
| Excitement | 3.5 / 5 | Controlled injection + dose-response profiling 的思路新颖且有实用价值，但生态效度限制了影响力 |
| Reproducibility | 3.5 / 5 | 大部分超参已报告，代码承诺release，但LoRA配置不完整、RRF阈值未充分论证 |
| Confidence | 4 / 5 | 熟悉IRT建模、contamination detection和因果推断文献 |

---

## Summary

本文提出 ContamCal，一个将 controlled SFT injection 与 contamination-augmented IRT (2PL+γ) 结合的框架，用于量化 benchmark contamination 对 LLM 评分的 dose-response 效应。作者在 5 个家族的 6 个模型上以 5 个剂量水平注入污染，发现四种 dose-response pattern（Benefit, Immune, Collapse, V-recovery），claim 污染效应因家族而异，且 DiD 分析表明效应主要是 global capability modification 而非 item-specific memorization。论文还 characterize 了 Min-K%++ 的 directional reversal 现象，并通过 simulation 验证 IRT 参数恢复需 J≥50。

---

## Strengths

**S1. Controlled injection 框架填补了重要方法论空白。** 大多数 contamination 研究是 observational 的，无法建立因果关系。本文通过 controlled dosage injection + clean control (d000) 的实验设计，首次实现了 contamination 的准实验因果推断。这一思路借鉴了药理学 dose-response 建模（Hill, 1910; Ritz et al., 2015），跨学科嫁接有说服力。

**S2. IRT 建模是 principled 的选择。** 用 IRT 分离 item-level 效应与 model ability，比简单的 aggregate accuracy 更精细。2PL+γ 扩展允许 per-benchmark contamination covariate，是 DIF 分析的自然推广。Bayesian inference via Stan 和 convergence diagnostics (R̂ < 1.01, bulk ESS > 400) 体现了较好的统计实践。

**S3. 实验设计全面。** 7 个 baseline 对比（B0-B6），cross-benchmark transfer 分析，domain-level decomposition，out-of-sample validation (LLaMA-3.1)，以及 signal ablation（Appendix E），覆盖面广。DiD 分析（Section 5.4, Table 2）直接检验了 item-specific memorization 假说。

**S4. Min-K%++ directional reversal 的发现有价值。** Section 5.6 的分析表明 Min-K%++ 在 SFT 污染后出现信号反转（Cohen's d = −1.38 at d100），这对使用该信号做 contamination detection 的社区是重要的 cautionary finding。

**S5. Simulation study 验证了方法边界条件。** Appendix F 系统地评估了 IRT 参数恢复与 ensemble size J 和 signal AUC 的关系，给出了 J≥50 的实用建议，且 CI coverage 分析（Table 16）有参考价值。

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] SFT injection 的生态效度存疑，缺乏关键控制实验

- 具体位置：Section 4.1, Limitations (p.8-9)
- 问题：论文用 LoRA SFT injection 模拟 contamination，但真实污染发生在 pre-training 的 web crawl ingestion 阶段，两者在学习动态上有本质差异。SFT 产生的是显式的 supervised memorization signal，而 pre-training contamination 涉及重复但分散的暴露。更关键的是，实验采用 **augmentation** 设计（Section 4.1: "Contaminated items augment (not replace) the base SFT corpus"），高剂量组 **系统性地包含更多训练数据**（d009: 50.4k → d100: 65.4k，增加约30%），这意味着高剂量组的性能提升可能部分来自 **更多训练数据** 而非 contamination 本身。论文缺少一个关键控制：在高剂量组中加入等量的 **非 benchmark** 高质量 Q&A 数据，以分离 contamination 效应与 data quantity 效应。
- 为什么影响接收：这个 confound 直接威胁 dose-response profiles 的因果解读。如果 Benefit pattern 部分由 data quantity 驱动，那么"contamination vulnerability"的归因就不准确。
- 建议修改方向：(1) 增加 data-quantity control：在每个剂量水平上，用等量非 benchmark 数据替代 benchmark 数据做对照；(2) 或者改用 replacement 设计（保持总训练量恒定）；(3) 至少在 Discussion 中明确承认并讨论这一 confound。

**N2** [Critical] 核心 dose-response pattern 各仅由单一模型支撑，泛化性不足

- 具体位置：Section 5.1 (Table 1), Figure 1
- 问题：论文声称发现四种 dose-response pattern，但 Collapse 仅在 Qwen-14B 上观察到，V-recovery 仅在 Qwen-7B 上观察到。在 6 个模型中，Benefit（Phi-4 14.7B, Falcon3-7B, OLMo-2 7B）和 Immune（Phi-4, LLaMA-3.1）各有 2-3 个模型支撑，而 Collapse 和 V-recovery 各只有 1 个。论文标题声称 "Profiling... Across Model Families"，但实际上 4 种 pattern 中有 2 种缺乏跨模型复制。
- 为什么影响接收：无法区分 Collapse/V-recovery 是稳健的家族特性还是特定模型/种子的偶然行为。Cross-seed stability 分析（Section 5.3, n=3）虽然方向一致，但仅限于 Benefit 家族（Phi-4, OLMo-2）和 Immune (Phi-4)。Qwen-14B 的 Collapse pattern 没有跨种子复制报告。
- 建议修改方向：(1) 增加同家族不同 size 的模型（如 Qwen2.5-3B, Qwen2.5-14B）检验 Collapse 是否是 Qwen 家族的系统性行为；(2) 或者将 claims 弱化为 "observed patterns" 而非 "family-level profiles"；(3) 报告 Collapse 和 V-recovery 的 cross-seed stability。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] 2PL+γ 模型公式与文字描述不一致

- 具体位置：Section 3.3, Eq. (2), p.4
- 问题：Eq. (2) 写为 $P(y_{ij,k}=1) = \sigma(a_j(\theta_i - b_j + \gamma_j \cdot e_{ij}))$，其中 γ_j 在 a_j 的乘法项 **内部**，意味着 contamination 效应与 item discrimination 交互。但紧接着文字说 "We place γ_j outside a_j"，暗示实际模型是 $\sigma(a_j(\theta_i - b_j) + \gamma_d \cdot e_{ij})$，γ 不受 a_j 缩放。两种参数化的含义不同——前者意味着 high-discrimination items 的 contamination 效应被放大，后者则 uniform。哪个是实际实现？
- 建议：统一公式和文字描述，明确报告 Stan 代码中的实际参数化。

**W2** [Major] Algorithm 1 的阈值敏感性未评估

- 具体位置：Section 3.4, Algorithm 1 (p.5)
- 问题：Algorithm 1 使用多个硬编码阈值（noise threshold τ = 2pp, saturation ratio ρ = 0.3, late-gain floor ε = 0.5·Δ_p）来分类 dose-response pattern。论文称这些阈值"explicit and adjustable"（p.5），但未评估分类结果对阈值选择的敏感性。例如，如果 τ 从 2pp 改为 1.5pp 或 3pp，Immune 和 Benefit 的边界会怎样移动？当前 Immune 定义为 Δ < 2pp，这是定义而非发现——不同阈值可能导致 "Not All Models Are Inflated" 的结论逆转。
- 建议：(1) 报告 τ 在 [1, 3]pp 范围内的 sensitivity analysis；(2) 或者使用 data-driven 的阈值选择方法（如 changepoint detection）。

**W3** [Major] n=3 seeds 的统计功效不足以支撑 cross-seed stability claims

- 具体位置：Section 5.3
- 问题：cross-seed stability 分析仅使用 n=3 seeds per family，这导致 (1) 无法可靠区分真实不一致性与采样噪声；(2) bootstrap CI 的 coverage 在小样本下可能不准确。论文声称"magnitude is seed-sensitive but direction is consistent"（p.7），但 n=3 下的 directional consistency 有 12.5% 的概率纯由 chance 产生（若真实效应为零）。
- 建议：(1) 增加到至少 n=5 seeds 以提高功效；(2) 或者明确报告检验 directional consistency 的 p-value。

**W4** [Major] DiD 分析的 parallel trends 假设未检验

- 具体位置：Section 5.4, Table 2
- 问题：DiD 要求 treated 和 untreated items 在无污染情况下有 parallel trends。但 treated items 是被选入 SFT corpus 的 benchmark items，untreated items 是未被选入的。如果两组 items 在 difficulty、topic、format 上系统性地不同，parallel trends 假设可能被违反。论文未检验 pre-treatment period 的 parallel trends。
- 建议：(1) 报告 d000（clean control）下 treated vs. untreated items 的 baseline accuracy 差异；(2) 检验 item difficulty 分布在两组间是否均衡。

**W5** [Major] 模型规模范围窄（7-14B），限制了 "across model families" 的 claims

- 具体位置：Section 4.1, Table 1
- 问题：所有模型均在 7-14B 范围内。论文声称 family-level factors（pre-training data composition, tokenizer design, training recipe）驱动 contamination vulnerability，但未验证这些 findings 是否在更大（70B+）或更小（1-3B）模型上成立。鉴于 memorization capacity 与 model size 的已知关系（Carlini et al., 2023），dose-response profiles 可能随 model scale 根本性改变。
- 建议：在 Limitations 中明确标注 scale 范围限制，或增加至少一个 3B 和一个 >20B 模型的实验。

---

## 小问题（不影响接收）

**M1** [Minor] Section 4.1 中 dosage listing 疑似排版错误："d025" 出现两次（"50.8k (d025), 51.1k (d025)"），应为 d025 和 d050。

**M2** [Minor] RRF 聚合中 smoothing constant κ=60 和 threshold |S|=.3 的选择未 justify。这些来自 Cormack et al. (2009) 的 default 值，但在 contamination detection 场景中是否最优？

**M3** [Minor] LoRA 配置报告不完整：缺少 alpha、dropout、target modules、training epochs、batch size、warmup steps 等关键超参。Appendix J 提到 "All SFT configurations converged. Final training loss decreases monotonically with dosage"，但未给出 loss curves。

**M4** [Minor] Table 1 中 "Baseline" 列的含义不完全清晰——是 d000 (clean SFT) 后的 accuracy 还是 pre-SFT accuracy？从 context 推断应为 d000 后，但应明确标注。

**M5** [Minor] Section 5.5 中 IRT calibration quality 在 "300 highest-exposure-variance items (2.1% of MMLU)" 上评估，但这个 subset selection 可能引入 selection bias——高 exposure variance 的 items 可能系统性地不同于整体 item pool。

---

## Questions for Authors

**Q1**: 在 augmentation 设计下，d100 组比 d000 组多约30%训练数据。你们是否有evidence排除 data quantity 对 dose-response profiles 的贡献？是否考虑过 replacement 设计？

**Q2**: Collapse pattern 仅在 Qwen-14B 上观察到。是否有其他 Qwen 系列模型（如 Qwen2.5-3B, Qwen2.5-72B）的初步结果支持这是 Qwen 家族的系统性行为？

**Q3**: Eq. (2) 和后续文字关于 γ 是否在 a_j 内部存在矛盾。实际 Stan 实现用的是哪种参数化？

**Q4**: Algorithm 1 的 noise threshold τ=2pp 是如何确定的？如果改为 1pp 或 3pp，Immune 和 Benefit 的分类比例如何变化？

**Q5**: DiD 分析（Table 2）显示 contamination 不造成 item-specific memorization。那么 Benefit pattern 中 +1.2-4pp 的 accuracy gain 的机制是什么？是 SFT 本身的 general capability improvement 还是真正的 contamination effect？如果是前者，这对论文的 contamination vulnerability 归因有何影响？

---

## Missing References

- Carlini et al. (2023) "Quantifying Memorization Across Neural Language Models" — 关于 model size 与 memorization 的关系，与本文 scale 限制相关
- Oren et al. (2024) "Proving Test Set Contamination in Black-Box Language Models" — 已引用但未在 pre-training vs SFT contamination 差异的讨论中充分对比
- 药理学 dose-response 建模文献中的 Emax model 可能比 Algorithm 1 的 rule-based 分类更 principled

---

## 主要优势总结

1. 首个 controlled contamination injection + dose-response profiling 的系统框架
2. IRT-based calibration 方法论上优于 aggregate accuracy
3. 实验设计全面（7 baselines, cross-benchmark transfer, DiD, signal ablation）
4. Min-K%++ directional reversal 是有价值的社区贡献
5. Simulation study 为 IRT 应用提供了实用的 minimum sample size 指导

---

**最终评分**: Overall 3.5 (Borderline Conference), Soundness 3.5, Excitement 3.5, Confidence 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 932 · 2026-05-22T22:54:27.404452+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 89

## Round 89

2 recorded events


### User

_source line 933 · 2026-05-22T22:54:44.323716+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交结构化审稿意见，核心判断：

- **Overall 3.5 (Borderline Conference)**，Soundness 3.5，Excitement 3.5，Confidence 4
- **2 个 Critical 问题**：(1) SFT augmentation 设计引入 data quantity confound，缺少关键控制实验；(2) Collapse 和 V-recovery pattern 各仅由单一模型支撑，泛化性不足
- **5 个 Major 问题**：2PL+γ 公式不一致、Algorithm 1 阈值敏感性未评估、n=3 seeds 功效不足、DiD parallel trends 未检验、模型规模范围窄
- **5 个 Minor 问题**：排版错误、RRF 阈值未 justify、LoRA 配置不完整等

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 934 · 2026-05-22T22:54:49.335597+00:00_

Reviewer 1 完成，等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 90

## Round 90

6 recorded events


### User

_source line 935 · 2026-05-22T22:55:10.758664+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性、完整性与写作质量

### 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 论文提出了剂量-响应框架来刻画不同模型家族对 benchmark 污染的差异化反应，实验覆盖面广、附录详尽，但核心分类法（Algorithm 1）过度依赖手工阈值、关键 claim 超出实验证据、模型规模和 benchmark 多样性不足。

### 官方维度打分（ACL ARR review form）
| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3/5 | Algorithm 1 阈值无理论依据；2PL+ 可识别性讨论不足；部分 claim 证据不充分 |
| Excitement | 2.5/5 | 问题重要但"不同模型对污染反应不同"并不出人意料；手工分类削弱方法论贡献 |
| Reproducibility | 3.5/5 | 超参数和设置详尽但代码未公开；Algorithm 1 需仔细实现 |
| Confidence | 4/5 | 熟悉 contamination detection 和 IRT in NLP |

---

### Must-Fix 问题

**N1** [Critical] Abstract/Title 的 claim 显著超出实验证据
- Title "Not All Models Are Inflated" 暗示一般性结论，但实验仅覆盖 6 个 ≤14B 模型。6 个模型中 4 个（Phi-4, OLMo-2, Falcon3, Gemma-2）展现 Benefit 或 Immune，仅 Qwen-14B Collapse、Qwen-7B V-recovery。多数结果反而支持而非驳斥"contamination ≈ inflation"。
- Abstract 声称 "family-level factors beyond baseline ability—including pre-training data composition, tokenizer design, and training recipe—modulate vulnerability"，但论文无法访问这些因素，无法建立因果归因。
- "contamination equals inflation is a gross oversimplification" 过强——受控 SFT 注入不能推广到 pre-training 污染或更大模型。
- 建议：Title 加限定词；family-level factors 改为观察性描述；"gross oversimplification" 改为 "requires nuance"。

**N2** [Critical] Algorithm 1 的剂量-响应分类是完全 hand-crafted 的规则系统
- Algorithm 1 包含 29 行代码、≥6 个手工阈值（ε_noise=2pp, ε_sig=0.5, ε_late-gain=3pp 等）。Appendix R 报告 100% 分类稳定性，但可能因数据点太少而 trivially stable。未与数据驱动替代方案（聚类、change-point detection）对比。四类 pattern 是先验定义而非从数据发现。
- 建议：补充 data-driven baseline；对阈值做连续 sensitivity analysis；明确阐述为何四类分类。

---

### Should-Fix 问题

**W1** [Major] SFT 注入 ≠ 真实污染但主文限定不足
- LoRA-based SFT 注入与 pre-training 污染机制根本不同。Limitations 简要提及但主文几乎所有结论未加此限定。

**W2** [Major] 仅 3 个 benchmark 且 MMLU 主导
- ARC-Challenge short 版仅 25 items，GSM8K 用 chain-of-thought 生成评测。跨 benchmark 迁移分析（Section 5.2）结论是 "limited transfer"，反而削弱框架 generalizability。

**W3** [Major] n=3 seeds 不足以支撑 cross-seed stability 结论
- 极端 pattern（Collapse, V-recovery）各仅 1 个模型 × 3 seeds，无法可靠区分 systematic effect 与随机变异。

**W4** [Major] 2PL+ 可识别性讨论不足
- θ_j 和 γ_k·r_ij 存在可识别性问题。Appendix F 提出条件但无严格证明或模拟验证。Additive structure 可能过度简化。

**W5** [Major] "无 item-specific memorization" 与叙事张力
- Section 5.4 报告无 item-level DID 效应，结论是 "global capability modification"。但若 SFT 不导致记忆化而仅改变全局能力，它在多大程度上是 "contamination" 而非 "additional training"？未讨论此概念区分。

**W6** [Minor→Major] 与 Schaeffer et al. (2024) 区别度阐述不足
- Schaeffer et al. 同用 controlled contamination + IRT，但论文未提供 detailed head-to-head 比较和明确 delta contribution。

---

### 小问题
- M1: Algorithm 1 notation 不一致（数学符号 vs 英文名混用）
- M2: Table 1 caption 未充分解释 Baseline/Δacc 关系
- M3: Figure 1 y 轴 zoom-in 可能夸大效应量视觉印象
- M4: S2 和 S4 信号 AUC ≈ 0.48-0.51（近似随机）保留在 RRF 中的 rationale 未在主文说明
- M5: Limitations 未提及 LoRA rank 等超参数选择的潜在影响
- M6: 代码承诺发布但审稿阶段不可验证

### 可能遗漏的相关工作
1. Rodriguez et al. (2021) "Evaluation Examples Are Not Equally Informative" — IRT 用于 NLP 评测
2. Gu et al. (2024) "OLMES" — 标准化 LLM 评测
3. Zhu et al. (2023) "DyVal" — 动态评测绕过污染

### 主要优势
- S1: 研究问题重要且及时，从"是否存在污染"转向"量化异质性影响"
- S2: 实验设计系统——五个剂量、五个家族、三个 benchmark、多层分析
- S3: 附录极详尽（A-Z），展现严谨实验态度
- S4: 2PL+ 将 contamination exposure 作为连续变量建模有方法论新意
- S5: Item-level memorization 的 null finding 是有价值的负结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-22T22:55:55.417018+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "contamcal-irt-calibration",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性与实验设计）\n\n**Overall**: 3.5 / 5 (Borderline Conference), Soundness 3.5, Excitement 3.5, Confidence 4\n\n### Summary\n本文提出 ContamCal，一个将 controlled SFT injection 与 contamination-augmented IRT (2PL+γ) 结合的框架，用于量化 benchmark contamination 对 LLM 评分的 dose-response 效应。作者在 5 个家族的 6 个模型上以 5 个剂量水平注入污染，发现四种 dose-response pattern（Benefit, Immune, Collapse, V-recovery），claim 污染效应因家族而异，且 DiD 分析表明效应主要是 global capability modification 而非 item-specific memorization。论文还 characterize 了 Min-K%++ 的 directional reversal 现象，并通过 simulation 验证 IRT 参数恢复需 J≥50。\n\n### Strengths\nS1. Controlled injection 框架填补了重要方法论空白。大多数 contamination 研究是 observational 的，无法建立因果关系。本文通过 controlled dosage injection + clean control (d000) 的实验设计，首次实现了 contamination 的准实验因果推断。\nS2. IRT 建模是 principled 的选择。2PL+γ 扩展允许 per-benchmark contamination covariate，是 DIF 分析的自然推广。Bayesian inference via Stan 和 convergence diagnostics 体现了较好的统计实践。\nS3. 实验设计全面。7 个 baseline 对比，cross-benchmark transfer 分析，domain-level decomposition，out-of-sample validation (LLaMA-3.1)，以及 signal ablation。\nS4. Min-K%++ directional reversal 的发现有价值。\nS5. Simulation study 验证了方法边界条件。\n\n### Must-Fix\nN1 [Critical] SFT injection 的生态效度存疑，缺乏关键控制实验。高剂量组系统性包含更多训练数据（d009: 50.4k → d100: 65.4k，增加约30%），Benefit pattern 可能部分由 data quantity 驱动。缺少 data-quantity control。\nN2 [Critical] 核心 dose-response pattern 各仅由单一模型支撑，泛化性不足。Collapse 仅 Qwen-14B，V-recovery 仅 Qwen-7B。\n\n### Should-Fix\nW1 [Major] 2PL+γ 模型公式与文字描述不一致（Eq.2 中 γ 在 a_j 内部 vs 文字说 outside）\nW2 [Major] Algorithm 1 的阈值敏感性未评估\nW3 [Major] n=3 seeds 的统计功效不足\nW4 [Major] DiD 分析的 parallel trends 假设未检验\nW5 [Major] 模型规模范围窄（7-14B）\n\n### Minor\nM1-M5: 排版错误、RRF 阈值未 justify、LoRA 配置不完整、Table 1 标注不清、subset selection bias\n\n### Questions\nQ1: augmentation 设计下 data quantity 对 dose-response 的贡献？\nQ2: 其他 Qwen 模型是否支持 Collapse 是家族系统性行为？\nQ3: Eq.(2) 实际 Stan 实现用哪种参数化？\nQ4: Algorithm 1 的 τ=2pp 如何确定？\nQ5: DiD 显示无 item-specific memorization，那 Benefit 的 +1.2-4pp gain 的机制是什么？\n\n### Missing References\nCarlini et al. (2023), Emax model 文献"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "contamcal-irt-calibration",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性与实验设计）\n\n**Overall**: 3.5 / 5 (Borderline Conference), Soundness 3.5, Excitement 3.5, Confidence 4\n\n### Summary\n本文提出 ContamCal，一个将 controlled SFT injection 与 contamination-augmented IRT (2PL+γ) 结合的框架，用于量化 benchmark contamination 对 LLM 评分的 dose-response 效应。作者在 5 个家族的 6 个模型上以 5 个剂量水平注入污染，发现四种 dose-response pattern（Benefit, Immune, Collapse, V-recovery），claim 污染效应因家族而异，且 DiD 分析表明效应主要是 global capability modification 而非 item-specific memorization。论文还 characterize 了 Min-K%++ 的 directional reversal 现象，并通过 simulation 验证 IRT 参数恢复需 J≥50。\n\n### Strengths\nS1. Controlled injection 框架填补了重要方法论空白。大多数 contamination 研究是 observational 的，无法建立因果关系。本文通过 controlled dosage injection + clean control (d000) 的实验设计，首次实现了 contamination 的准实验因果推断。\nS2. IRT 建模是 principled 的选择。2PL+γ 扩展允许 per-benchmark contamination covariate，是 DIF 分析的自然推广。Bayesian inference via Stan 和 convergence diagnostics 体现了较好的统计实践。\nS3. 实验设计全面。7 个 baseline 对比，cross-benchmark transfer 分析，domain-level decomposition，out-of-sample validation (LLaMA-3.1)，以及 signal ablation。\nS4. Min-K%++ directional reversal 的发现有价值。\nS5. Simulation study 验证了方法边界条件。\n\n### Must-Fix\nN1 [Critical] SFT injection 的生态效度存疑，缺乏关键控制实验。高剂量组系统性包含更多训练数据（d009: 50.4k → d100: 65.4k，增加约30%），Benefit pattern 可能部分由 data quantity 驱动。缺少 data-quantity control。\nN2 [Critical] 核心 dose-response pattern 各仅由单一模型支撑，泛化性不足。Collapse 仅 Qwen-14B，V-recovery 仅 Qwen-7B。\n\n### Should-Fix\nW1 [Major] 2PL+γ 模型公式与文字描述不一致（Eq.2 中 γ 在 a_j 内部 vs 文字说 outside）\nW2 [Major] Algorithm 1 的阈值敏感性未评估\nW3 [Major] n=3 seeds 的统计功效不足\nW4 [Major] DiD 分析的 parallel trends 假设未检验\nW5 [Major] 模型规模范围窄（7-14B）\n\n### Minor\nM1-M5: 排版错误、RRF 阈值未 justify、LoRA 配置不完整、Table 1 标注不清、subset selection bias\n\n### Questions\nQ1: augmentation 设计下 data quantity 对 dose-response 的贡献？\nQ2: 其他 Qwen 模型是否支持 Collapse 是家族系统性行为？\nQ3: Eq.(2) 实际 Stan 实现用哪种参数化？\nQ4: Algorithm 1 的 τ=2pp 如何确定？\nQ5: DiD 显示无 item-specific memorization，那 Benefit 的 +1.2-4pp gain 的机制是什么？\n\n### Missing References\nCarlini et al. (2023), Emax model 文献"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-22T22:56:09.107210+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13690
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-22T22:56:09.258139+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "contamcal-irt-calibration",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性、完整性与写作质量）\n\n**Overall**: 3.0 (Findings), Soundness 3, Excitement 2.5, Confidence 4\n\n### Must-Fix\nN1 [Critical] Abstract/Title 的 claim 显著超出实验证据。Title \"Not All Models Are Inflated\" 暗示一般性结论，但实验仅覆盖 6 个 ≤14B 模型。Abstract 声称 \"family-level factors beyond baseline ability—including pre-training data composition, tokenizer design, and training recipe—modulate vulnerability\"，但论文无法访问这些因素，无法建立因果归因。\"contamination equals inflation is a gross oversimplification\" 过强。\nN2 [Critical] Algorithm 1 的剂量-响应分类是完全 hand-crafted 的规则系统，包含 ≥6 个手工阈值。未与 data-driven 替代方案对比。四类 pattern 是先验定义而非从数据发现。100% 分类稳定性可能因数据点太少而 trivially stable。\n\n### Should-Fix\nW1 [Major] SFT 注入 ≠ 真实污染但主文限定不足\nW2 [Major] 仅 3 个 benchmark 且 MMLU 主导\nW3 [Major] n=3 seeds 不足以支撑 cross-seed stability 结论\nW4 [Major] 2PL+ 可识别性讨论不足——θ_j 和 γ_k·r_ij 存在可识别性问题\nW5 [Major] \"无 item-specific memorization\" 与叙事张力——若 SFT 不导致记忆化而仅改变全局能力，它在多大程度上是 \"contamination\" 而非 \"additional training\"？\nW6 [Minor→Major] 与 Schaeffer et al. (2024) 区别度阐述不足\n\n### Minor\nM1-M6: Algorithm 1 notation 不一致、Table 1 caption 不充分、Figure 1 y轴 zoom-in 可能夸大效应、近随机 AUC 信号保留 rationale 未说明、Limitations 未提 LoRA rank 影响、代码不可验证\n\n### 可能遗漏的相关工作\nRodriguez et al. (2021) \"Evaluation Examples Are Not Equally Informative\"\nGu et al. (2024) \"OLMES\"\nZhu et al. (2023) \"DyVal\"\n\n### Strengths\nS1: 研究问题重要且及时\nS2: 实验设计系统\nS3: 附录极详尽\nS4: 2PL+ 将 contamination exposure 作为连续变量建模有方法论新意\nS5: Item-level memorization 的 null finding 是有价值的负结果"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "contamcal-irt-calibration",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性、完整性与写作质量）\n\n**Overall**: 3.0 (Findings), Soundness 3, Excitement 2.5, Confidence 4\n\n### Must-Fix\nN1 [Critical] Abstract/Title 的 claim 显著超出实验证据。Title \"Not All Models Are Inflated\" 暗示一般性结论，但实验仅覆盖 6 个 ≤14B 模型。Abstract 声称 \"family-level factors beyond baseline ability—including pre-training data composition, tokenizer design, and training recipe—modulate vulnerability\"，但论文无法访问这些因素，无法建立因果归因。\"contamination equals inflation is a gross oversimplification\" 过强。\nN2 [Critical] Algorithm 1 的剂量-响应分类是完全 hand-crafted 的规则系统，包含 ≥6 个手工阈值。未与 data-driven 替代方案对比。四类 pattern 是先验定义而非从数据发现。100% 分类稳定性可能因数据点太少而 trivially stable。\n\n### Should-Fix\nW1 [Major] SFT 注入 ≠ 真实污染但主文限定不足\nW2 [Major] 仅 3 个 benchmark 且 MMLU 主导\nW3 [Major] n=3 seeds 不足以支撑 cross-seed stability 结论\nW4 [Major] 2PL+ 可识别性讨论不足——θ_j 和 γ_k·r_ij 存在可识别性问题\nW5 [Major] \"无 item-specific memorization\" 与叙事张力——若 SFT 不导致记忆化而仅改变全局能力，它在多大程度上是 \"contamination\" 而非 \"additional training\"？\nW6 [Minor→Major] 与 Schaeffer et al. (2024) 区别度阐述不足\n\n### Minor\nM1-M6: Algorithm 1 notation 不一致、Table 1 caption 不充分、Figure 1 y轴 zoom-in 可能夸大效应、近随机 AUC 信号保留 rationale 未说明、Limitations 未提 LoRA rank 影响、代码不可验证\n\n### 可能遗漏的相关工作\nRodriguez et al. (2021) \"Evaluation Examples Are Not Equally Informative\"\nGu et al. (2024) \"OLMES\"\nZhu et al. (2023) \"DyVal\"\n\n### Strengths\nS1: 研究问题重要且及时\nS2: 实验设计系统\nS3: 附录极详尽\nS4: 2PL+ 将 contamination exposure 作为连续变量建模有方法论新意\nS5: Item-level memorization 的 null finding 是有价值的负结果"
  }
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-22T22:56:10.564139+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1305
}
```

</details>

---


### Assistant

_source line 940 · 2026-05-22T22:56:12.972906+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 91

## Round 91

2 recorded events


### User

_source line 941 · 2026-05-22T22:56:15.497974+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文选题好、实验覆盖面广，但两个 Critical 问题（overclaiming + Algorithm 1 缺乏方法论支撑）阻止其进入主会议：Title/Abstract 的因果性表述超出 6 个 ≤14B 模型的 SFT 注入实验所能支撑的范围；核心分类算法是 hand-crafted 规则树且未与 data-driven 替代方案对比。四个 Major issues（SFT≠真实污染限定不足、benchmark 多样性不足、n=3 seeds 不够、2PL+ 可识别性讨论欠缺）进一步压低评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 942 · 2026-05-22T22:56:23.132700+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 92

## Round 92

2 recorded events
