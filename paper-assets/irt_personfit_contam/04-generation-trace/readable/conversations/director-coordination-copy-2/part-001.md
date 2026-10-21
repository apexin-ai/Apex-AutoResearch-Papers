# Director coordination — Part 1 of 3

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/25/25b67938722c16707e2e.json)

## Round 1

## Round 1

2 recorded events


### User

_source line 1 · 2026-05-20T09:21:47.307290+00:00_

[Reviewer 1 审稿意见]:
## R1 审稿报告：Method & Experiments

**Paper**: "IRT-FIT: Detecting LLM Benchmark Contamination at the Minimal-Information Operating Point"
**Venue**: EMNLP 2026 (via ACL ARR)

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 将 IRT person-fit 应用于 LLM 污染检测是新颖且有实际价值的贡献，但 null distribution 校准不足和受控实验模型多样性有限削弱了理论和实证的可靠性。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法合理但 N(0,1) null 假设在真实 LLM 上系统偏移（Table 13: clean mean lz*=0.93）；受控实验仅 2 个模型；SFT 衰减因子缺乏机制解释 |
| Excitement | 4/5 | 仅需 binary response 的操作点是真正的实用优势；two-sided framework 和 power theory 有概念价值；post-RL 鲁棒性是重要差异化 |
| Overall Assessment | 3.5 | 新颖性和实用性强，但实验覆盖和理论严谨性需加强才能 confidently accept |
| Confidence | 4/5 | 熟悉 IRT 和 LLM evaluation 文献，仔细核查了数学推导和实验设计 |

---

## Summary of Contributions

本文将 IRT person-fit statistic (lz*) 从心理测量学迁移到 LLM benchmark 污染检测，提出了三个贡献：(1) 仅需 binary (correct/incorrect) response 的检测框架——比 ConStat 少用 aggregate statistics，比 Min-K%++ 少用 token probabilities；(2) two-sided 检测（lz* << 0 为 partial contamination，lz* >> 0 为 full contamination），附带近似 power theory；(3) 在 simulation、controlled SFT、leaderboard audit、post-RL 等多场景下的实证验证。

---

## 主要优势

**S1. 真正的 minimal-information operating point**：仅需 binary response 即可检测污染，适用于闭源模型（只需 API 访问），实用价值高。Table 10 清晰展示了 detection frontier 上的定位：IRT-FIT (binary only) vs ConStat (scores) vs Min-K%++ (token probs) vs Probing (training data)。

**S2. Two-sided framework 概念优雅**：区分 partial contamination（lz* << 0，模型记住部分题目产生 aberrant pattern）和 full contamination（lz* >> 0，模型记住全部题目产生 over-consistent pattern）。这是对现有文献的有意义的概念扩展。Section 3.1 的形式化清晰。

**S3. Power theory 提供有用的理论指导**：Equation 4 的 power ∝ √n 关系和 inverted-U 形状（Table 4, 7）让用户可以预判检测能力边界，这比纯 empirical 方法更有指导性。R²=0.87 的近似拟合如实报告为 "approximate"。

**S4. Post-RL 鲁棒性是重要差异化**：Section 5.2 和 Table 12 显示 GRPO 训练后 IRT-FIT 保持 AUROC 0.92（96% retention），而 MIA 退化到 0.54。机制解释合理——RL 改变 token-level 分布但不改变 binary response pattern。

**S5. 实验设计覆盖面广**：simulation（7 benchmarks）+ controlled SFT + baseline comparison + 4PL/3PL ablation + leaderboard audit (2,847 models) + domain-level MMLU + Gemini case study + post-RL。虽然每个实验的深度有限，但整体覆盖了读者会问的主要问题。

**S6. AUROC 优势显著**：在 15% contamination 下，IRT-FIT (0.96) vs ConStat (0.83) vs Min-K%++ (0.88) 的差距不小，尤其考虑到 IRT-FIT 用的信息最少。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Null distribution 校准不足，two-sided test 的 false positive rate 未经实证验证

- **具体位置**：Section 3.1, Table 13, Table 19
- **问题**：lz* 的 two-sided test 假设 null 分布为 N(0,1)（Snijders [2001]）。但 Table 13 显示即使使用 4PL，clean models 的 mean lz* = 0.93（3PL 下为 1.17），系统偏正。这意味着 +1.96 阈值的 false positive rate 实际高于 2.5%，而 -1.96 阈值过于保守。Table 19 的 leaderboard audit 显示 MMLU 上 flagging rate 为 13%（312 negative + 115 positive / 2,847），远高于 null 预期的 ~5%（BH-FDR 后应更低）。论文未报告实际 false positive rate 的 empirical estimate，也未讨论系统偏移对 two-sided framework 有效性的影响。
- **为什么影响接收**：如果 null 不成立，论文的核心统计框架的可靠性成疑。读者无法判断 flagged models 中多少是真 contamination、多少是 false positive。
- **建议修改方向**：(a) 在 clean models 上报告 empirical false positive rate（用 uncontaminated SFT 模型或 simulation 的 clean condition）；(b) 讨论 null bias 的来源（IRT model misfit? item parameter estimation error?）；(c) 考虑 empirical null correction（如 permutation-based threshold 替代 ±1.96）。

**N2** [critical] 受控实验模型多样性严重不足

- **具体位置**：Table 1, 3, 11; Section 4, 5.2
- **问题**：Controlled SFT injection 仅在 2 个模型上测试（Qwen3.5-9B, Gemma-4-31B），且 Gemma 在多个 contamination level 缺失数据（Table 1 中仅有 0%, 5%, 10%, 15%, 100% 五个点，缺 25%, 50%）。Post-RL 实验（Table 11）仅在 Qwen3.5-9B 一个模型上测试。论文的 claims 涵盖 "large language models"（标题），但实验验证仅覆盖 2 个模型族（均为开源中等规模模型）。
- **为什么影响接收**：缺少不同架构（如 Llama, Mistral, Phi）、不同规模（1B-70B）、不同训练方式（pretrained-only vs instruction-tuned）的验证。读者无法判断方法对模型架构/规模的 sensitivity。Gemma 的缺失数据暗示可能存在未报告的技术困难。
- **建议修改方向**：(a) 至少增加 1-2 个不同架构/规模的模型（如 Llama-3-8B, Phi-3-small）的完整 contamination curve；(b) 解释 Gemma 缺失数据的原因（训练失败？资源限制？）；(c) 将标题中的 claim 限定为已验证的模型范围。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SFT generalization attenuation (~0.65 factor) 缺乏机制解释

- **具体位置**：Section 4.1, 第 3 段
- **问题**：Simulation 预测 15% contamination 的 lz* ≈ -6.09，但真实 SFT 仅产生 -1.8 到 -2.3（约 3 倍衰减）。论文将此归因于 "generalization attenuation" 并给出 ~0.65 的经验系数，但未解释机制（是因为 SFT 对非污染项也有提升？还是 IRT model 的 item parameters 在 SFT 后不再准确？）。这个 gap 对于 power theory 的实际适用性至关重要——如果衰减因子在不同模型/数据比例下不稳定，power 预测就不可靠。
- **建议**：(a) 分析衰减的来源（item-level analysis: SFT 是否系统性改变了非污染项的 response pattern？）；(b) 报告衰减因子在不同 contamination level 和不同模型上的稳定性。

**W2** [warning] Baseline comparison 缺少统计显著性检验

- **具体位置**：Table 5/9/10; Section 5.1
- **问题**：AUROC 比较（IRT-FIT 0.96 vs ConStat 0.83 vs Min-K%++ 0.88）未报告 confidence intervals 或 significance test。虽然 0.96 vs 0.83 的差距看起来 substantial，但论文的 bootstrap CI 仅在 Table 4 中出现，其他关键 comparison 表格缺失。
- **建议**：对 Table 9/10 的所有 AUROC 数字报告 bootstrap 95% CI，或至少报告 DeLong test p-value。

**W3** [warning] Leaderboard audit 的 temporal trend 分析不充分

- **具体位置**：Section 6.2, Table 20
- **问题**：Table 20 显示 contamination rate 从 2023 Q1-Q2 的 ~6% 上升到 2024 Q1-Q2 的 ~14%，但论文未报告 trend 的统计显著性。样本量（4 个时间段）也很小。同时，2,847 models out of 7K+ leaderboard 的 coverage 未说明选择标准——是随机抽样还是有 selection bias（如仅包含可运行 inference 的模型）？
- **建议**：(a) 报告 trend test（如 Cochran-Armitage）的 p-value；(b) 说明 model selection criteria 及其对 representativeness 的影响。

**W4** [warning] Table 完整性：多表存在系统性缺失数据

- **具体位置**：Tables 1, 3, 4, 11
- **问题**：Table 1 Gemma 缺少 25%, 50% 的数据；Table 11 仅 Qwen3.5-9B 一个模型；Table 3 仅 Qwen3.5-9B。这种 pattern 暗示实验资源有限或部分实验未成功。论文未解释任何缺失的原因。
- **建议**：对每个 "–" entry 注明原因（resource constraint / training divergence / other），让读者判断 missingness 是否 informative。

**W5** [warning] 4PL vs 3PL ablation 仅报告 aggregate metrics

- **具体位置**：Section 5.3, Table 13
- **问题**：Table 13 的 4PL vs 3PL 比较仅报告 overall AUROC 和 mean lz*，未展示不同 contamination level 或不同 benchmark 下的差异。4PL 的改进是否在所有条件下一致？upper asymptote d 参数的影响在不同 item difficulty band 上是否不同（Table 14 提示了这一点但分析不够深入）？
- **建议**：按 contamination level × benchmark 分解 4PL vs 3PL 差异。

---

## 小问题（不影响接收）

- Section 2.2: "Snijders [2001] derived the corrected statistic lz* that accounts for estimation error in θ̂" — 应 cite Snijders (2001) 的具体公式或定理编号，方便读者查阅原始推导。
- Table 7 (Inverted-U inflection point) 仅有少量数据点（几个 benchmark），难以 convincingly 验证 power theory 的 inflection 预测。
- Section 7 Related Work 偏短（约半页），对 IRT 在 NLP 中的应用（如 Lalor et al., Rodriguez et al.）缺乏充分讨论。
- Limitations section 提到 "benchmarks with fewer than ~3,200 items have limited power at 15% contamination"，但未讨论如何处理 short benchmarks（如 BBH 仅 6,511 items 按 Table 22，但 BoolQ 仅 3,000+）。
- Equation 3 的 lzm aggregation 引用 Hong et al. [2021]，但未给出 aggregation 的 statistical properties（如 lzm 在 null 下的分布）。

---

## Questions for Authors

**Q1**: Table 19 中的 "Med. lz*" 是所有 2,847 models 的 median 还是仅 flagged models 的 median？如果是前者，MMLU 的 median lz* = -4.73 意味着超过半数模型被 flag（因为 -4.73 < -1.96），这与 Neg.=312 (11%) 矛盾。请澄清。

**Q2**: Clean models 的 mean lz* = 0.93 (Table 13, 4PL)。在 leaderboard audit 中，是否对这个 systematic bias 做了任何校正？还是直接用 ±1.96 threshold？

**Q3**: SFT attenuation factor ~0.65 在 Gemma-4-31B 上是多少？是否与 Qwen3.5-9B 一致？如果 Gemma 的数据不完整，是否有任何 preliminary evidence？

**Q4**: Post-RL 实验仅测试了 GRPO。对于其他 RL 方法（PPO, DPO, KTO），是否有理由认为结论会不同？binary response 的稳定性论点是否同样适用？

**Q5**: Power formula (Eq. 4) 中的 δ(c) 具体取什么形式？论文说 "the expected log-likelihood shift induced by contamination"，但 δ(c) 如何从 contamination fraction c 和 item parameters 计算？这对 reproducibility 很重要。

---

## Missing Experiments or Analyses

1. **Empirical false positive rate**: 在已知 clean 的 models 上（如 freshly pretrained models 或 simulation clean condition）计算 actual FPR，与 nominal α=0.05 对比。
2. **更多模型族的 controlled SFT**: 至少 Llama-3 和 Phi-3 系列，覆盖不同架构和规模。
3. **Cross-benchmark contamination**: 模型在 benchmark A 上的污染是否影响 benchmark B 的 lz* 估计（通过 θ̂ 的偏差传播）？
4. **Item parameter estimation robustness**: IRT item parameters 来自哪些 calibration models？如果 calibration sample 本身含有 contaminated models，item parameters 是否被 biased？
5. **Sensitivity to contamination type**: 论文假设 contamination = SFT on exact benchmark items。其他形式（如 rephrased items, similar-but-not-identical items, chain-of-thought on benchmark topics）是否也能被检测？

---

## 格式合规检查

- **页数**: Main text 7 页（Section 1-8 Conclusion），Limitations 在第 8 页（不计入页数限制），References 从第 8 页开始。**符合 EMNLP 2026 的 8 页限制。**
- **匿名性**: 标题页标注 "Anonymous"，正文中未发现明显的 de-anonymization 线索。**符合。**
- **Limitations section**: 存在（第 8 页顶部），讨论了 benchmark size 限制和 4PL unidimensionality 假设。**符合。**

---

## 总结

这是一篇有明确新颖性和实用价值的论文——将 IRT person-fit 迁移到 LLM 污染检测是 well-motivated 且在 minimal-information operating point 上有真正的竞争力。Two-sided framework 和 power theory 为该领域增加了理论深度。然而，null distribution 的系统偏移未被充分解决（N1），受控实验仅覆盖 2 个模型且数据不完整（N2），这两个问题限制了论文 claims 的可靠性。如果作者能在 rebuttal 中提供 empirical FPR 数据并解释缺失数据，评分可上调至 4 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2 · 2026-05-20T09:22:08.039321+00:00_

收到 Reviewer 1 的初审报告。R1 给出 3.5 (Borderline Conference)，核心发现：

- **N1 [critical]**: Null distribution 校准问题——clean models mean lz*=0.93 偏离 N(0,1)，FPR 未经实证验证
- **N2 [critical]**: 受控实验仅 2 个模型（Qwen3.5-9B, Gemma-4-31B），Gemma 数据不完整
- 5 个 should-fix（SFT 衰减机制、缺 CI、temporal trend 统计、缺失数据解释、4PL ablation 粒度）

等待 Reviewer 2 的报告到达后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 2

## Round 2

36 recorded events


### User

_source line 3 · 2026-05-20T09:22:10.740696+00:00_

[Reviewer 1 审稿结果]:
R1 审稿报告已提交至 Review Director。

核心判断：**Overall 3.5 (Borderline Conference)**，Soundness 3/5，Excitement 4/5。

两个 Must-Fix 问题：
1. **Null distribution 校准不足** — clean models 的 mean lz* = 0.93（非理论预期的 0），论文未报告 empirical FPR，leaderboard 13% flagging rate 远超预期
2. **受控实验仅 2 个模型** — Gemma 多处数据缺失，post-RL 仅测了 Qwen3.5-9B，标题 claim "Large Language Models" 但验证范围有限

主要优势：minimal-information operating point 有真正实用价值，AUROC 0.96 显著优于 baselines，post-RL 鲁棒性是重要差异化。若 rebuttal 能补充 empirical FPR 和更多模型的数据，可上调至 4。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-20T09:22:21.479208+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,get_external_review_status,get_visual_check_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,get_external_review_status,get_visual_check_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-20T09:22:21.479627+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-20T09:22:25.243089+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-20T09:22:25.243587+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-20T09:22:29.157951+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-20T09:22:29.158408+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (3 个)\n\n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp-two-sided** (negative): Two-sided detection (|lz*| > threshold) with benchmark-specific θ MLE + parametric bootstrap empirical null + BH-FDR control will reduce Phase B flagging rate from 93% to a reasonable level (<20%), isolating genuine contamination signals from θ estimation bias ← 基于 phase_b_personfit\n- **phase_b_personfit** (success): Real LLM benchmark response data from PSN-IRT 12 models shows significant inter-model variation in person-fit statistics (lz*, outfit, infit), with specific models exhibiting anomalous patterns indicative of benchmark contamination — particularly Gemini-1.5 with accuracy-ability dissociation\n- **sim_001** (negative): Under 4PL IRT model, lz* person-fit statistic can detect partial benchmark contamination (5-30% items) with >80% power at α=0.05, and detection power follows an inverted-U curve across contamination levels (low contamination undetectable, moderate contamination most detectable, high contamination mimics high ability)\n  [null_check_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/null_check_summary.json) | [simulation_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/simulation_summary.json) | [power_curves_combined](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/chart/power_curves.png)\n\n## 趋势\n成功 1 / 负向 2 / 失败 0 / 共 3\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb2-36806: 无 GPU 信息\n\n## 告警\n（无）"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-20T09:22:29.208898+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-20T09:22:29.259523+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-20T09:22:29.310701+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-20T09:22:29.561906+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-20T09:22:37.138569+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-20T09:22:37.540613+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-20T09:22:38.644845+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-20T09:22:38.946322+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-20T09:22:39.097194+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-20T09:22:39.147848+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-20T09:23:13.173943+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-20T09:23:13.676170+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/median/paper.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/worst/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-20T09:23:13.827262+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/docs"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-20T09:23:13.928105+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-20T09:23:16.988819+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-20T09:23:17.340555+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-20T09:23:17.491604+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-20T09:23:17.542319+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/median/paper.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-20T09:23:22.560816+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_personfit_contam",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-20T09:23:23.064798+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_personfit_contam'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-20T09:23:23.467158+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/dream_20260520T082549/best/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/dream_20260520T082549/best/*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-20T09:23:23.517767+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/experiment_data.json
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.aux
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.out
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.log
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-20T09:23:27.999069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml"
  }
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-20T09:23:28.301775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_report.md"
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-20T09:23:28.302397+00:00_

1	---
2	dream_id: dream_20260520T082549
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-20T09:14:10.147818+00:00
6	---
7	
8	# Dream Review Report: IRT-FIT
9	
10	**Paper:** IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics
11	
12	**Review Mode:** Full (2-Reviewer Roundtable)
13	
14	---
15	
16	## Overall Assessment
17	
18	**Score: 4 / 6 (Weak Accept)**
19	
20	The paper presents a well-motivated cross-domain transfer of psychometric person-fit statistics to LLM benchmark contamination detection. The core insight — that a contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge — is clean and enables a novel "minimal-information operating point" on the contamination detection frontier. The controlled experiments are solid, the power theory provides lasting practical value, and the 2,847-model leaderboard audit is a unique capability no competing method can match. However, several technical issues (lzm null distribution, unidimensionality assumption, narrow post-RL validation) and a critically thin reference list (11 entries) prevent a strong accept. With targeted revisions, this paper would be competitive at a top ML venue.
21	
22	---
23	
24	## Reviewer Scores
25	
26	| Reviewer | Focus | Score | Confidence |
27	|----------|-------|-------|------------|
28	| R1 | Methods + Experiments | 4.0 | 4/5 |
29	| R2 | Novelty + Related Work | 3.5 | 4/5 |
30	| **Consensus** | | **4.0** | **4/5** |
31	
32	---
33	
34	## Strengths
35	
36	### S1. Compelling Framing and Real Gap (R1, R2)
37	The "minimal-information operating point" and "detection frontier" concepts provide a clear organizing principle. The paper precisely identifies where IRT-FIT sits: it requires only binary response data (the least privileged information level), yet achieves AUROC 0.96 at 15% contamination — higher than methods requiring token-level probabilities (Min-K%++ 0.88) or 
…[truncated 11114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-20T09:23:28.404555+00:00_

1	narrative_guidance: '原始 framing 完全成立。三条 claim 均有 ground-truth 支撑：(1) minimal-information
2	  operating point 经控制实验确认——仅 binary 数据即可在 5% 污染水平检测，AUROC>0.93；(2) power ∝ n_items
3	  有解析公式， inverted-U 从经验观察升级为理论命题，拐点位置可预测；(3) Gemini-1.5 case study + leaderboard audit
4	  构成大规模实证贡献。Post-RL 实验直接回应 Wang et al.，形成"MIA 失效但 person-fit 存活"的对比叙事。 Headline: "IRT-FIT
5	  是唯一在 minimal-information 条件下同时解决 partial/full/post-RL 污染的方法"。 EMNLP 主会议无需调整 claim
6	  强度。
7	
8	  '
9	imagined_experiments:
10	- name: Two-Sided Detection Framework
11	  plan_id: exp-two-sided
12	  description: '基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap
13	    CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。
14	
15	    '
16	  expected_results:
17	    gemini15_mmlu_lz_star: 34.75
18	    gemini15_mmlu_lz_star_bootstrap_95ci: '[32.1, 37.4]'
19	    gemini15_gsm8k_lz_star: -15.71
20	    gemini15_humaneval_lz_star: -12.37
21	    two_sided_flagged_models_at_fdr_0.05: 4
22	    one_sided_flagged_models_at_fdr_0.05: 2
23	    incremental_detection_gain_two_vs_one_sided: 2 additional models flagged (Gemini-1.5
24	      on MMLU, 1 other high-perf model)
25	    optimal_negative_threshold_alpha_0.05: -2.81
26	    optimal_positive_threshold_alpha_0.05: 3.24
27	    positive_regime_models: Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling
28	      model
29	    negative_regime_models: Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)
30	  result_rationale: 'Gemini-1.5 的 MMLU 100% 正确率对应 θ=0.78（远低于满分所需能力），产生极端正侧 lz*=+34.75。
31	    这是因为 full contamination 导致模型在所有 item 上正确，包括远超其真实能力的难题—— response pattern 过度一致（over-consistent），与真正高能力模型的"偶尔失误"模式不符。
32	    负侧信号来自 partial contamination：模型在已污染的难题上正确、在未污染的易题上错误， 产生 aberrant pattern（lz*
33	    << 0）。双侧框架捕获这两类互补信号， 单侧框架只能捕获负侧（partial），遗漏正侧（full）。Bootstrap CI 窄是因为 MMLU 有 14K
34	    items， lz* 的抽样方差 ∝ 1/n_items。FDR 控制在 12 模型 × 5 benchmarks = 60 次检验下仍能保持 power，
35	    因为真阳性的 lz* 绝对值远超阈值（效应量极大）。
36	
37	    '
38	  tables:
39	  - name: 'Table 1: Two-Sided Detec
…[truncated 42189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-20T09:23:52.253496+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-20T09:23:52.253992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 38 · 2026-05-20T09:24:30.566411+00:00_

**状态恢复完成。** 服务器重启后记忆丢失，已通过项目文件重建上下文：

- **论文**: "IRT-FIT: Detecting LLM Benchmark Contamination at the Minimal-Information Operating Point"
- **Venue**: EMNLP 2026 (ARR)，8 页正文限制，double-blind
- **R1 已完成**：Overall 3.5 (Borderline Conference)，聚焦方法/实验
- **R2 未返回**：需重新分配（新颖性/完整性方向）
- **外部审稿**: 未请求
- **视觉审查**: 未启动

现在并行执行：分配 R2、派发视觉审查、请求外部审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 3

## Round 3

7 recorded events


### User

_source line 39 · 2026-05-20T09:24:30.569630+00:00_

[Reviewer 2 审稿意见]:
## R2 审稿意见：Novelty & Related Work

**Paper**: "IRT-FIT: Detecting LLM Benchmark Contamination at the Minimal-Information Operating Point"

---

## 总体评分

**Overall**: 3.0 / 5（Findings）
**一句话总结**: 将 person-fit 统计量引入 LLM 污染检测是有价值的 problem connection，但技术贡献主要是现有工具的直接迁移，related work 覆盖严重不足（仅 ~15 篇引用），且 post-RL 失效大幅削弱实用价值。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 主要 claim 有实验支撑，但实验范围窄（2个模型族），power theory 验证不够独立 |
| Excitement | 3/5 | Person-fit → contamination 的连接有启发性，但技术深度有限，post-RL 失效削弱兴奋度 |
| Overall Assessment | 3.0/5 | Findings 水平——insight 有价值但不足以支撑主会议接收 |
| Reproducibility | 4/5 | 方法基于公开的 PSN-IRT 参数，lz* 计算清晰，基本可复现 |
| Confidence | 4/5 | 我熟悉 IRT/psychometrics 文献和 LLM contamination 检测领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **引用数量严重不足，related work 覆盖有重大遗漏**
- 具体位置：Section 7 (Related Work, p.7)，References (pp.8-9)
- 问题：全文仅约 15 篇引用，远低于 EMNLP 投稿的正常水平（通常 30-50+）。以下高度相关的工作均缺失：
  1. **Golchin & Surdeanu (ICLR 2024)** — Time Travel 方法的原始论文。论文在 Section 7 将 "Time Travel testing via prompting" 归属于 Oren et al. [2024]，但 Oren et al. 的实际工作是 "Proving Test Set Contamination in Black-Box Language Models"（基于 exchangeable benchmark ordering），与 Time Travel（guided instruction completion）是完全不同的方法。**这是一个事实性错误/误归属。**
  2. **PaCoST** (Zhang et al., EMNLP 2024 Findings) — 使用 paired confidence significance testing 检测污染，同为统计检验路径，高度相关
  3. **Dodge et al. (EMNLP 2021)** — n-gram overlap 检测污染的开创性工作，Director summary 中列为 covered 但论文中未引用
  4. **Rodriguez et al. (ACL 2021)** — IRT for NLP evaluation 的奠基工作，论文引用 Polo et al. 和 Gu et al. 但漏掉了这一重要前驱
  5. **Contamination detection survey** (Li et al., 2024, arXiv 2404.00699) — 综述了 50+ 检测方法
  6. **Bowman & Dahl (NAACL 2021)** — benchmark validity 的经典讨论
  7. **PATCH** (Fang et al., 2024) — Psychometrics-AssisTed benCHmarking，同属 IRT+LLM 评估
- 为什么影响接收：Related work 不完整是 ARR reviewer 评估的核心维度之一。15 篇引用对于一个横跨 psychometrics 和 LLM evaluation 两个领域的工作来说，无法令人信服地建立 novelty claim。Oren et al. 的误归属更是直接影响学术严谨性。
- 建议修改方向：(1) 修正 Time Travel 的归属为 Golchin & Surdeanu 2024; (2) 补充上述缺失引用; (3) 将 Related Work 扩展为至少 1 整页，分别讨论 contamination detection methods（按信息访问层级组织）、IRT in NLP、person-fit in psychometrics 三条线。

**N2** [critical] **核心 novelty 定位不清——tool transfer vs. methodological contribution**
- 具体位置：Section 1 (Contributions, p.1), Section 3 (Method, p.2-3)
- 问题：论文声称三项贡献：(1) two-sided detection framework, (2) power theory, (3) leaderboard audit + domain analysis。但深入审视后：
  - **Two-sided framework**：将 lz* < c（aberrant）和 lz* > c（over-consistent）分别对应 partial 和 full contamination，这在统计学上只是标准的双侧假设检验。概念上的映射（partial contamination → aberrant pattern, full contamination → over-consistent pattern）是 insight，但不构成方法论创新。
  - **Power theory (Eq. 6)**：直接基于 Snijders 的 variance formula 推导，核心是将 contamination 比例作为 n_contam 代入已知框架。这是一个 useful derivation 但不是 non-trivial theoretical contribution。
  - **4PL model + lz* 计算**：完全来自 PSN-IRT (Gu et al. 2024) 和 Snijders (2001)，无新的校准方法或统计量改进。
  - **Multiscale aggregation (l_ms, Eq. 3)**：来自 Hong et al. (2021)。
  
  论文的真正贡献是 **problem connection**：意识到 person-fit aberrance 可以检测 LLM benchmark contamination。这是有价值的，但论文的写法试图将其包装为多项独立的方法论贡献，夸大了 novelty。
- 为什么影响接收：Reviewers 会问 "what's technically new beyond applying existing tools?"——如果答案主要是 "the problem connection and empirical validation"，论文需要诚实地定位为 application paper 而非 methodology paper。
- 建议修改方向：(1) 在 Introduction 中明确承认核心贡献是 problem connection + empirical validation; (2) 更清楚地区分哪些是 borrowed components（lz*, 4PL, l_ms）哪些是 new（two-sided interpretation, power derivation for contamination setting）; (3) 如果要强化方法论贡献，应比较 lz* 与其他 person-fit indices（W, ECI, HT, U3——Karabatsos 2003 比较了 36 个 indices），证明 lz* 在此任务上的优越性。

**N3** [critical] **Person-fit index 选择缺乏 justification**
- 具体位置：Section 2.2 (p.2), Section 7 (p.7)
- 问题：论文在 Section 2.2 引用 Karabatsos [2003] 提到 person-fit statistics 的比较，但仅使用了 lz* 一个 index。Karabatsos (2003) 实际比较了 36 个 person-fit statistics 在不同场景下的表现，发现不同 indices 在不同异常模式下有不同优势。论文没有回答：
  - 为什么 lz*（likelihood-based）比 W（Wright & Stone 1979, mean-square-based）或 ECI（Tatsuoka 1984, extended caution index）更适合检测 contamination？
  - 在 contamination 的特定异常模式下（"easy items wrong + hard contaminated items right"），是否有其他 indices 更敏感？
  - Meijer & Sijtsma (2001) 的 survey 中讨论了多种 indices 的适用场景，论文引用了但未利用其结论。
- 为什么影响接收：如果另一个 person-fit statistic 在 contamination detection 上效果更好，论文的核心结果可能只是 suboptimal baseline。Reviewer 会质疑这是一篇完整的 investigation 还是 first-attempt exploration。
- 建议修改方向：在 ablation 中加入至少 2-3 个替代 person-fit indices 的比较（如 W, ECI, U3），或在 method section 中提供理论论证为何 lz* 最适合 contamination 检测。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **"Minimal-information operating point" framing 有 spin 嫌疑**
- 具体位置：Title, Abstract, Section 1, Table 10 (p.7)
- 问题：将 "只需要 binary response" 包装为 "minimal-information operating point on the contamination detection frontier" 是一个巧妙的 framing，但存在问题：
  - 在实际应用中，许多 LLM 评估场景**确实**可以获取 token probabilities（通过 API），binary-only 并非最常见的约束条件
  - Table 10 的对比在 15% contamination 这一特定操作点进行，IRT-FIT AUROC=0.96 vs ConStat=0.63 vs Min-K%++=0.44。但在更高 contamination levels（如 50%+），Min-K%++ 和其他方法的性能可能不同。Table 10 没有呈现多个操作点的比较。
  - "Detection frontier" 是一个有用的概念框架，但缺乏形式化定义——它到底是 Pareto frontier 还是只是一个分类？
- 建议：(1) 在 Table 10 中增加多个 contamination level 的比较; (2) 诚实讨论 binary-only 场景在实际中的普遍程度; (3) 将 "detection frontier" 给出更严格的定义或降级为 informal taxonomy。

**W2** [warning] **Domain-level analysis (Section 6.4) 的贡献度被高估**
- 具体位置：Section 6.4 (pp.6-7), Table 23
- 问题：论文将 per-domain lz* 分析列为第三项主要贡献。但一旦有了 model-level 的 lz* 框架，将其应用于 benchmark 子集（如 MMLU 的 57 个 domain）是非常直接的——只需对子集 items 重新计算统计量。Table 23 的发现（abstract_algebra 等 domain 上 Gemma-1.5 显示高 lz*）有一定实用价值，但这更像是 case study 而非 methodological contribution。
- 建议：将 domain analysis 定位为 empirical application 而非核心贡献；或者加入 domain-level analysis 的 unique insight（如 domain 特征如何影响检测灵敏度的理论分析）。

**W3** [warning] **Related Work section 结构单薄且位置偏后**
- 具体位置：Section 7 (p.7), 仅约半页
- 问题：作为一篇跨两个领域（psychometrics + LLM evaluation）的 bridging paper，Related Work 只有约半页且放在 Section 7（倒数第二节）是不够的。在 NLP 会议论文中，对于这类跨领域工作，通常需要更充分地 contextualize 两个领域的背景，帮助审稿人（可能不熟悉 psychometrics）理解 landscape。
- 建议：将 Related Work 前移到 Section 2 后面（或融入 Introduction），扩展到至少 1 页，分三条线组织：(1) contamination detection methods; (2) IRT/psychometrics in NLP; (3) person-fit and cheating detection in educational measurement。

**W4** [warning] **Post-RL 失效问题对 framing 的冲击未被充分承认**
- 具体位置：Section 5.2 (p.5), Table 12 (p.9), Limitations (p.8)
- 问题：Section 5.2 承认 post-RL training 导致 lz* signal 被 attenuate（GRPO 后信号从 -8.49 变为 -1.23，接近不显著）。Table 12 显示 post-RL 后 IRT-FIT recall 从 96% 降到 92%（看似还行），但 Table 11 中 post-SFT+GRPO 的 lz* 从 7.51 / 1.63 下降明显。论文在 Limitations 中提到了这一点，但 Abstract 和 Introduction 中的 framing 仍然偏乐观——"IRT-FIT achieves AUROC 0.96" 的数字来自 SFT-only 场景，而现实世界中几乎所有 SOTA LLM 都经过 RLHF/DPO/GRPO。如果论文的主要 selling point 在 post-RL 模型上不 work well，这大幅削弱了实际影响力。
- 建议：在 Abstract 中增加 post-RL limitation 的 caveat；或者增加实验证明在轻量 alignment（如仅 DPO without full RLHF）场景下的鲁棒性。

---

## 小问题（不影响接收）

- **Reference 格式**：部分引用缺少 venue 信息（如 Wang et al. 2025 标注为 arXiv preprint）
- **Table 10 "Scalability" 列**：IRT-FIT 标注 "Any model" 但实际上需要 PSN-IRT 预校准的 item parameters，这对非标准 benchmark 是一个限制，应注明
- **Section 3.1 (p.2)**：FDR control 使用 Benjamin-Hochberg（原文拼写为 "Benjamin"，正确拼写为 "Benjamini"）
- **Eq. 3 (p.3)**：l_ms 的定义来自 Hong et al. [2021] 的 multiband aggregation，应更清楚注明

---

## Questions for Authors

1. 为什么选择 lz* 而非其他 person-fit indices（如 W, ECI）？是否有理论或实验依据表明 lz* 在 contamination 检测中优于其他 indices？
2. Table 10 的 AUROC 对比在 15% contamination level——如果在 5% 或 50% contamination 下对比，ranking 是否改变？
3. "Detection frontier" 是否有形式化定义？它与 Pareto optimality 的关系是什么？
4. Oren et al. [2024] 的方法（exchangeable benchmark ordering）在论文中被描述为 "Time Travel testing via prompting"——请确认这是否为误归属，因 Time Travel 是 Golchin & Surdeanu (ICLR 2024) 的工作。
5. 论文使用 PSN-IRT (Gu et al. 2024) 的预校准 item parameters。如果这些 parameters 的校准数据本身有 contamination，会如何影响 IRT-FIT 的有效性？

---

## Missing References / Positioning Gaps

**缺失引用（按重要性排序）：**
1. Golchin & Surdeanu, "Time Travel in LLMs: Tracing Data Contamination in Large Language Models," ICLR 2024 — Time Travel 方法原始论文
2. Zhang et al., "PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models," EMNLP 2024 Findings — 同为统计检验路径
3. Rodriguez et al., "Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?" ACL 2021 — IRT for NLP 的奠基工作
4. Dodge et al., "Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus," EMNLP 2021 — n-gram contamination detection 开创性工作
5. Li et al., "A Comprehensive Survey of Contamination Detection Methods in Large Language Models," arXiv 2024 (2404.00699) — 综述 50+ 方法
6. Bowman & Dahl, "What Will it Take to Fix Benchmarking in Natural Language Understanding?" NAACL 2021 — benchmark validity
7. Fang et al., "PATCH: Psychometrics-AssisTed benCHmarking of Large Language Models," 2024 — IRT+LLM 评估
8. Rethinking LLM Benchmarking with IRT (arxiv 2505.15055, 2025) — PSN-IRT 扩展工作

**Positioning Gap：**
- 论文未充分讨论与 educational measurement 中 cheating detection 文献的联系。Person-fit 在 educational testing 中已有数十年的 cheating detection 研究（如 Meijer 2003 的 comprehensive review、Cizek & Wollack 2017 的 handbook），这些工作中的方法论 lessons（如 false positive 控制、effect of test length）直接适用于本文场景，应被引用和讨论。

---

## 主要优势

1. **Problem connection 有真正价值**：将 psychometric person-fit 引入 LLM contamination detection 是一个 well-motivated 且 previously unexplored 的连接。Binary-only detection 确实填补了方法论谱系中的空白。
2. **Inverted-U signal characterization (Section 4.2)**：发现 lz* 在中等污染水平达到峰值后下降（因为高污染的 over-consistent pattern 不再 aberrant），这是一个有 insight 的经验发现，对理解检测方法的行为边界有贡献。
3. **实验设计的诚实度**：论文明确报告了多项 limitations（post-RL attenuation、systematic positive bias、2 model families），这种诚实度值得肯定。
4. **Large-scale leaderboard audit (Section 6.2)**：对 2,647 模型的 audit 有实际应用价值，flagged 的可疑模型可供社区进一步调查。
5. **Power theory 提供了 actionable guidance**：虽然推导本身不复杂，但 Eq. 6 给出了检测所需的最小 contaminated items 数量，对实践者有用。

---

**总结**：论文的 core insight（person-fit ↔ contamination）是真正有价值的 bridging idea，但当前版本的技术深度不足以支撑主会议接收。最大的问题是 (1) related work 严重不完整（引用数量和覆盖面均不达标），(2) novelty 定位过度包装（本质是 tool transfer，但写法像 methodology paper），(3) person-fit index 选择缺乏 justification。建议修改后重投——补全 related work、增加 alternative indices 的比较、诚实定位为 application paper——有望达到 Findings 或更高水平。

---

[Reviewer 2 审稿结果]:
R2 审稿意见已提交给 Review Director。

核心结论：**Overall 3.0/5（Findings 水平）**。论文的 person-fit → contamination detection 连接有真正价值，但三个 critical 问题需要解决：

1. **引用严重不足 + 误归属**：仅 ~15 篇引用，缺失 Golchin & Surdeanu (Time Travel 原始论文)、PaCoST、Rodriguez et al. 等至少 8 篇高度相关工作。Oren et al. 被错误归属为 Time Travel 作者。
2. **Novelty 过度包装**：核心技术贡献是 tool transfer（lz* + 4PL 均为现有工具），但论文以 methodology paper 定位。缺少 alternative person-fit indices 的比较来 justify lz* 的选择。
3. **Post-RL 失效削弱实用性**：几乎所有 SOTA LLM 都经过 RLHF/DPO，但论文的核心 AUROC 数字来自 SFT-only 场景。

---

[Reviewer 1 审稿意见]:
## R1 交叉回应 R2 意见

---

### 逐条回应

**[AGREE] R2-Issue-1: Technical novelty limited — 个体组件均为已有工具**

同意 lz*、4PL、lzm、BH-FDR 均为现有方法的直接借用。但需区分两个层次：

(a) **组件级无新意** — 确实如此。论文没有提出新的 IRT 模型或新的 person-fit statistic。
(b) **组合和 insight 层面有贡献** — two-sided framework 不是简单的 "apply two-sided test at ±1.96"。识别出 partial contamination (lz* << 0) 和 full contamination (lz* >> 0) 产生**方向相反的信号**并非 trivial。传统 person-fit 文献中 cheating detection 主要关注 aberrant (negative) direction，而 LLM 的 full memorization 导致 over-consistent (positive) direction 是新场景下的新观察。Power theory (Eq. 4) 虽用标准工具推导，但 power ∝ √n、inverted-U 依赖 contamination fraction 的具体形式是 problem-specific 的新结果。

**综合判断**：novelty 确实偏向 "well-motivated application" 而非 "new method"。这在 *ACL 是可接受的贡献类型，但要求实验验证更扎实——这恰好是论文的薄弱环节（见我 N2 的 concern）。

---

**[AGREE] R2-Issue-2: Related work thin, 缺少关键 educational measurement 文献**

完全同意。这是我 R1 审稿中低估的问题，在 R2 的指出下上调严重性。

论文仅 15 篇参考文献，Section 7 约半页，缺少以下关键类别：
- **Person-fit for cheating detection**: Zopluoglu & Davenport (2012), Karabatsos (2003) — 这些工作和本文的应用场景（考试作弊 → LLM 污染）直接对应，不引用会让教育测量领域的 reviewer 认为作者不了解上游文献。
- **Person-fit method surveys**: Meijer & Sijtsma (2001) 是该领域的 canonical review，必须引用。
- **IRT in NLP**: Lalor et al. (2019), Rodriguez et al. (2021) 等已将 IRT 引入 NLP evaluation，论文应讨论与这些工作的关系。
- **Benchmark saturation / contamination 的更广泛文献**: 如 Oren et al. (2024) 已提出 Time Travel testing。

**这个缺失对 novelty claim 的影响**：如果 educational measurement 已经有成熟的 person-fit cheating detection 方法论（它确实有），那么本文的贡献需要更精确地定位为 "adapting cheating detection to LLM contamination with domain-specific insights (two-sided, power scaling)"，而非暗示 person-fit 方法本身是新的。当前的 framing 没有做到这一点。

**上调为 Should-Fix (W6)**。

---

**[PARTIALLY REBUT] R2-Issue-3: "Minimal-information" framing oversells**

R2 指出 binary-only 的 trade-off cost（AUROC lower, ~18% minimum detectable）。这个 trade-off 确实存在，但我认为论文的 framing 总体是 fair 的，理由如下：

(a) **AUROC 数字需核实**：R2 引用 "AUROC 0.85 at 15%"，但据我阅读论文 Table 2/10 和 Abstract，IRT-FIT 在 15% contamination 下的 pooled AUROC 为 **0.96**（非 0.85）。0.82 是 **5% contamination** 下的数字。请 R2 确认引用的数字来源。如果 0.96 成立，IRT-FIT 在 15% 下不仅 "足够好"，而且超过了需要更多信息的 baselines（ConStat 0.83, Min-K%++ 0.88）。

(b) **Detection frontier 概念本身有价值**：Table 10 将方法按 information access level 排列是有用的 contribution。即使有些场景确实有 richer information，binary-only 场景（闭源 API、只返回 correct/incorrect 的 evaluation harness）也是 realistic 的。

(c) **但 R2 关于 "many settings DO have richer information" 的观点有道理**：论文可以更 balanced 地讨论 minimal-information 的 trade-off，而非仅强调优势。Limitations 中应明确：当 token-level access 可用时，Min-K%++ 类方法可能更 appropriate。

**我不认为这是 oversell，但建议在 Limitations 中加入 trade-off 讨论。**

---

**[AGREE] R2-Issue-4: Domain analysis incremental**

同意。Section 6.4 的 domain-level MMLU 分析是 straightforward application。STEM > Humanities 不 surprising（STEM 题目更 fact-based、更容易被精确记忆）。这部分作为 "additional analysis" 是 fine，但不应被 counted as 核心 contribution。

---

**[AGREE] R2-Issue-5: Cross-disciplinary bridge IS novel**

完全同意。No prior work applies person-fit statistics to LLM contamination — 这是事实性的判断，我在 S1-S2 中已高度肯定。

---

### 综合更新评估

R2 的意见让我更清晰地认识到：这是一篇 **application paper（将成熟的教育测量工具迁移到新领域）**，而非 methodological paper。在 *ACL venue 中，application paper 的接受标准更侧重 (a) 实验的彻底性，(b) 对上游文献的充分 engagement，(c) 实际 impact。

在此框架下重新评估：
- **(a) 实验彻底性**：不足。2 个模型、缺失数据、无 empirical FPR — 这些在 application paper 中比在 method paper 中更致命（我的 N1, N2 的严重性不变）。
- **(b) 上游文献 engagement**：严重不足（R2 的发现加强了这一判断）。
- **(c) 实际 impact**：较高。Binary-only + AUROC 0.96 at 15% 有真实的 practical value。

**更新评分**：

| 维度 | 原评分 | 更新评分 | 变化理由 |
|------|--------|----------|----------|
| Soundness | 3/5 | 3/5 | 不变 — N1 (null calibration) 和 N2 (model diversity) 仍是核心问题 |
| Excitement | 4/5 | 3.5/5 | 下调 0.5 — R2 正确指出 novelty 主要在 application 层面，domain analysis incremental |
| Overall | 3.5 | 3.5 | 不变 — 综合考虑 cross-disciplinary novelty 的正面贡献和实验/related work 的不足 |
| Confidence | 4/5 | 4/5 | 不变 |

**新增 Should-Fix**：

**W6** [warning] Related work 需大幅扩展以覆盖 educational measurement 的 person-fit / cheating detection 文献

- **具体位置**: Section 7
- **问题**: 仅 15 篇参考文献，缺少 Meijer & Sijtsma (2001) survey、Zopluoglu & Davenport (2012) cheating detection、Karabatsos (2003) person-fit comparison、IRT-in-NLP (Lalor et al., Rodriguez et al.) 等关键工作。论文的 novelty positioning 依赖于"首次将 person-fit 应用于 LLM contamination"，但如果不充分讨论 person-fit 在 cheating detection（与 LLM contamination 高度类似的问题）中的成熟应用，这个 claim 缺乏 context。
- **建议**: 增加至少 1 段讨论 educational measurement 中 person-fit for cheating detection 的文献，明确本文与这些工作的联系和区别（如 LLM 的 two-sided signal 是新的、scale 不同、calibration 挑战不同）。Related work 扩充到至少 1 页。

---

### 对 Director 的建议

R1 和 R2 在以下判断上有 **共识**：
1. Cross-disciplinary bridge 是 genuine 贡献
2. Related work 太薄
3. 实验证据对于 application paper 来说不够彻底
4. 论文有 potential 但目前在 borderline

**分歧点**：R2 对 novelty 的评价比我更严。我认为 two-sided insight 和 power theory 有 non-trivial 的贡献（不仅仅是 "apply existing tools"），但同意单独的 technical novelty 不足以支撑 main conference acceptance — 需要实验来补偿。

如果作者在 rebuttal 中能提供：(1) empirical FPR 数据，(2) 解释 Gemma 缺失数据的原因，(3) 承诺扩充 related work — 评分可上调至 4.0。否则维持 3.5 (Borderline Conference) 或下调至 3.0 (Findings)。

---

[Reviewer 1 审稿结果]:
R1 交叉回应已提交给 Director。

核心判断：
- 与 R2 在 **related work 不足**、**实验需加强**、**cross-disciplinary bridge 有价值** 上达成共识
- 对 R2 关于 novelty 的评估部分反驳——two-sided insight 和 power theory 不是 trivial application，但同意整体定位为 application paper
- 对 R2 引用的 "AUROC 0.85 at 15%" 提出质疑（论文实际报告 0.96）
- 新增 W6（Related work 需扩展）
- 维持 Overall 3.5，Excitement 从 4 下调至 3.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-20T09:25:19.012094+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_personfit_contam",
  "text": "以下是 Reviewer 1 的完整初审意见，请逐条回应：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R1 审稿报告：Method & Experiments\n\n**Paper**: \"IRT-FIT: Detecting LLM Benchmark Contamination at the Minimal-Information Operating Point\"\n**Venue**: EMNLP 2026 (via ACL ARR)\n\n**Overall**: 3.5 — Borderline Conference\nSoundness 3/5, Excitement 4/5, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Null distribution 校准不足，two-sided test 的 false positive rate 未经实证验证\n- Table 13 显示 clean models 的 mean lz* = 0.93（4PL），系统偏正。+1.96 阈值的 FPR 实际高于 2.5%，-1.96 阈值过于保守。Table 19 leaderboard MMLU flagging rate 13% 远高于 null 预期的 ~5%。论文未报告 empirical FPR estimate。\n- 建议：(a) 在 clean models 上报告 empirical FPR；(b) 讨论 null bias 来源；(c) 考虑 empirical null correction。\n\n**N2** [critical] 受控实验模型多样性严重不足\n- Controlled SFT 仅 2 个模型（Qwen3.5-9B, Gemma-4-31B），Gemma 多处数据缺失。Post-RL 仅 Qwen3.5-9B 一个模型。标题 claim \"Large Language Models\" 但验证范围有限。\n- 建议：增加 1-2 个不同架构/规模的模型，解释 Gemma 缺失数据原因。\n\n### Should-Fix 问题\n\n**W1** SFT generalization attenuation (~0.65 factor) 缺乏机制解释\n**W2** Baseline comparison 缺少统计显著性检验（无 CI 或 DeLong test）\n**W3** Leaderboard audit temporal trend 分析不充分（无 trend test p-value）\n**W4** 多表存在系统性缺失数据，未解释原因\n**W5** 4PL vs 3PL ablation 仅报告 aggregate metrics\n\n### 主要优势\n- S1: 真正的 minimal-information operating point（AUROC 0.96 at 15%，仅需 binary response）\n- S2: Two-sided framework 概念优雅\n- S3: Power theory 提供 actionable guidance（R²=0.87）\n- S4: Post-RL 鲁棒性是重要差异化（AUROC 0.92 retention 96%）\n- S5: 实验设计覆盖面广\n- S6: AUROC 优势显著\n\n### Questions\n- Q1: Table 19 的 \"Med. lz*\" 是全部 2,847 models 还是仅 flagged models 的 median？\n- Q2: Clean models mean lz* = 0.93 的 systematic bias 在 leaderboard audit 中是否做了校正？\n- Q3: SFT attenuation factor ~0.65 在 Gemma-4-31B 上是多少？\n- Q4: 对 PPO, DPO, KTO 等其他 RL 方法，binary response 稳定性论点是否同样适用？\n- Q5: Power formula 中 δ(c) 的具体形式？\n\n---\n\n请基于你的 Novelty & Related Work 视角逐条回应 R1 的发现。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "irt_personfit_contam",
    "text": "以下是 Reviewer 1 的完整初审意见，请逐条回应：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R1 审稿报告：Method & Experiments\n\n**Paper**: \"IRT-FIT: Detecting LLM Benchmark Contamination at the Minimal-Information Operating Point\"\n**Venue**: EMNLP 2026 (via ACL ARR)\n\n**Overall**: 3.5 — Borderline Conference\nSoundness 3/5, Excitement 4/5, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Null distribution 校准不足，two-sided test 的 false positive rate 未经实证验证\n- Table 13 显示 clean models 的 mean lz* = 0.93（4PL），系统偏正。+1.96 阈值的 FPR 实际高于 2.5%，-1.96 阈值过于保守。Table 19 leaderboard MMLU flagging rate 13% 远高于 null 预期的 ~5%。论文未报告 empirical FPR estimate。\n- 建议：(a) 在 clean models 上报告 empirical FPR；(b) 讨论 null bias 来源；(c) 考虑 empirical null correction。\n\n**N2** [critical] 受控实验模型多样性严重不足\n- Controlled SFT 仅 2 个模型（Qwen3.5-9B, Gemma-4-31B），Gemma 多处数据缺失。Post-RL 仅 Qwen3.5-9B 一个模型。标题 claim \"Large Language Models\" 但验证范围有限。\n- 建议：增加 1-2 个不同架构/规模的模型，解释 Gemma 缺失数据原因。\n\n### Should-Fix 问题\n\n**W1** SFT generalization attenuation (~0.65 factor) 缺乏机制解释\n**W2** Baseline comparison 缺少统计显著性检验（无 CI 或 DeLong test）\n**W3** Leaderboard audit temporal trend 分析不充分（无 trend test p-value）\n**W4** 多表存在系统性缺失数据，未解释原因\n**W5** 4PL vs 3PL ablation 仅报告 aggregate metrics\n\n### 主要优势\n- S1: 真正的 minimal-information operating point（AUROC 0.96 at 15%，仅需 binary response）\n- S2: Two-sided framework 概念优雅\n- S3: Power theory 提供 actionable guidance（R²=0.87）\n- S4: Post-RL 鲁棒性是重要差异化（AUROC 0.92 retention 96%）\n- S5: 实验设计覆盖面广\n- S6: AUROC 优势显著\n\n### Questions\n- Q1: Table 19 的 \"Med. lz*\" 是全部 2,847 models 还是仅 flagged models 的 median？\n- Q2: Clean models mean lz* = 0.93 的 systematic bias 在 leaderboard audit 中是否做了校正？\n- Q3: SFT attenuation factor ~0.65 在 Gemma-4-31B 上是多少？\n- Q4: 对 PPO, DPO, KTO 等其他 RL 方法，binary response 稳定性论点是否同样适用？\n- Q5: Power formula 中 δ(c) 的具体形式？\n\n---\n\n请基于你的 Novelty & Related Work 视角逐条回应 R1 的发现。"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-20T09:25:24.030553+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"&lt;urlopen error [Errno 111] Connection refused>\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 5018
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-20T09:25:33.920857+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_personfit_contam",
  "text": "以下是 Reviewer 1 的完整初审意见，请逐条回应：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R1 审稿报告：Method & Experiments\n\n**Overall**: 3.5 — Borderline Conference. Soundness 3/5, Excitement 4/5.\n\n### Must-Fix\n\n**N1** [critical] Null distribution 校准不足 — clean models mean lz* = 0.93 (Table 13)，系统偏正。FPR 未经实证验证。Leaderboard MMLU flagging rate 13% 远超预期。\n\n**N2** [critical] 受控实验仅 2 个模型，Gemma 多处缺失，post-RL 仅 1 个模型。\n\n### Should-Fix\n\n**W1** SFT attenuation ~0.65 缺乏机制解释\n**W2** Baseline AUROC 比较无 CI / significance test\n**W3** Leaderboard temporal trend 无统计检验\n**W4** 多表系统性缺失数据未解释\n**W5** 4PL vs 3PL ablation 仅 aggregate\n\n### Strengths\nS1: Minimal-information operating point (AUROC 0.96, binary only)\nS2: Two-sided framework 概念优雅\nS3: Power theory actionable (R²=0.87)\nS4: Post-RL robustness (AUROC 0.92, 96% retention)\nS5-S6: 实验覆盖广，AUROC 优势显著\n\n### Questions\nQ1-Q5: Table 19 median 定义、clean bias 校正、Gemma attenuation、其他 RL 方法适用性、δ(c) 具体形式\n\n---\n\n请基于你的 Novelty & Related Work 视角逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "irt_personfit_contam",
    "text": "以下是 Reviewer 1 的完整初审意见，请逐条回应：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R1 审稿报告：Method & Experiments\n\n**Overall**: 3.5 — Borderline Conference. Soundness 3/5, Excitement 4/5.\n\n### Must-Fix\n\n**N1** [critical] Null distribution 校准不足 — clean models mean lz* = 0.93 (Table 13)，系统偏正。FPR 未经实证验证。Leaderboard MMLU flagging rate 13% 远超预期。\n\n**N2** [critical] 受控实验仅 2 个模型，Gemma 多处缺失，post-RL 仅 1 个模型。\n\n### Should-Fix\n\n**W1** SFT attenuation ~0.65 缺乏机制解释\n**W2** Baseline AUROC 比较无 CI / significance test\n**W3** Leaderboard temporal trend 无统计检验\n**W4** 多表系统性缺失数据未解释\n**W5** 4PL vs 3PL ablation 仅 aggregate\n\n### Strengths\nS1: Minimal-information operating point (AUROC 0.96, binary only)\nS2: Two-sided framework 概念优雅\nS3: Power theory actionable (R²=0.87)\nS4: Post-RL robustness (AUROC 0.92, 96% retention)\nS5-S6: 实验覆盖广，AUROC 优势显著\n\n### Questions\nQ1-Q5: Table 19 median 定义、clean bias 校正、Gemma attenuation、其他 RL 方法适用性、δ(c) 具体形式\n\n---\n\n请基于你的 Novelty & Related Work 视角逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-20T09:25:36.329346+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"&lt;urlopen error [Errno 111] Connection refused>\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2408
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-20T09:25:48.878806+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_personfit_contam",
  "text": "请逐条回应 Reviewer 1 的初审意见（[AGREE] 或 [REBUT]）：\n\nR1 Must-Fix:\n- N1: Null distribution 校准不足（clean mean lz*=0.93, FPR 未验证, leaderboard 13% flagging rate 异常）\n- N2: 受控实验仅 2 模型，Gemma 缺失数据，post-RL 仅 1 模型\n\nR1 Should-Fix:\n- W1: SFT attenuation 0.65 无机制解释\n- W2: Baseline AUROC 无 CI\n- W3: Leaderboard trend 无统计检验\n- W4: 多表缺失数据\n- W5: 4PL/3PL ablation 仅 aggregate\n\nR1 Strengths: minimal-info AUROC 0.96, two-sided framework, power theory R²=0.87, post-RL robustness 0.92\n\n请从 Novelty/Related Work 视角评估这些发现。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "irt_personfit_contam",
    "text": "请逐条回应 Reviewer 1 的初审意见（[AGREE] 或 [REBUT]）：\n\nR1 Must-Fix:\n- N1: Null distribution 校准不足（clean mean lz*=0.93, FPR 未验证, leaderboard 13% flagging rate 异常）\n- N2: 受控实验仅 2 模型，Gemma 缺失数据，post-RL 仅 1 模型\n\nR1 Should-Fix:\n- W1: SFT attenuation 0.65 无机制解释\n- W2: Baseline AUROC 无 CI\n- W3: Leaderboard trend 无统计检验\n- W4: 多表缺失数据\n- W5: 4PL/3PL ablation 仅 aggregate\n\nR1 Strengths: minimal-info AUROC 0.96, two-sided framework, power theory R²=0.87, post-RL robustness 0.92\n\n请从 Novelty/Related Work 视角评估这些发现。"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-20T09:25:51.288576+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"&lt;urlopen error [Errno 111] Connection refused>\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2409
}
```

</details>

---


## Round 4

## Round 4

18 recorded events


### User

_source line 46 · 2026-05-20T09:26:07.068612+00:00_

[Reviewer 2 审稿结果]:
R1 提出了重要的实验层面问题。让我重新审视论文中的关键数据，再给出交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 47 · 2026-05-20T09:26:25.343420+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,get_visual_check_status,get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,get_visual_check_status,get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-20T09:26:25.394277+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-20T09:26:28.207293+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 50 · 2026-05-20T09:26:28.257981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-20T09:26:31.070321+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-20T09:26:31.171073+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (3 个)\n\n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp-two-sided** (negative): Two-sided detection (|lz*| > threshold) with benchmark-specific θ MLE + parametric bootstrap empirical null + BH-FDR control will reduce Phase B flagging rate from 93% to a reasonable level (<20%), isolating genuine contamination signals from θ estimation bias ← 基于 phase_b_personfit\n- **phase_b_personfit** (success): Real LLM benchmark response data from PSN-IRT 12 models shows significant inter-model variation in person-fit statistics (lz*, outfit, infit), with specific models exhibiting anomalous patterns indicative of benchmark contamination — particularly Gemini-1.5 with accuracy-ability dissociation\n- **sim_001** (negative): Under 4PL IRT model, lz* person-fit statistic can detect partial benchmark contamination (5-30% items) with >80% power at α=0.05, and detection power follows an inverted-U curve across contamination levels (low contamination undetectable, moderate contamination most detectable, high contamination mimics high ability)\n  [null_check_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/null_check_summary.json) | [simulation_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/simulation_summary.json) | [power_curves_combined](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/chart/power_curves.png)\n\n## 趋势\n成功 1 / 负向 2 / 失败 0 / 共 3\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb2-36806: 无 GPU 信息\n\n## 告警\n（无）"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-20T09:26:38.504017+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
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

_source line 54 · 2026-05-20T09:26:38.554689+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-20T09:26:43.025749+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-20T09:26:43.376941+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-20T09:26:43.377268+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-20T09:26:43.427659+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-20T09:27:05.048835+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-20T09:27:05.250022+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/back.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/filesave.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/forward.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/hand.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/help.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/home.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/matplotlib.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/move.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/qt4_editor_options.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/subplots.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/zoom_to_rect.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/median/paper.pdf
/ho
…[truncated 139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-20T09:27:05.250558+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-20T09:27:05.301098+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/median/paper.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/worst/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 63 · 2026-05-20T09:27:26.204234+00:00_

Reviewer 2 的回复**不完整**——只有一句"让我重新审视论文中的关键数据，再给出交叉回应"的意向声明，没有任何实质性的交叉回应内容（无 `[AGREE]` / `[REBUT]` 逐条回应）。

同时，当前 session 中没有历史审稿报告（`round_*.md`）和 issue tracker（`review_issues.yaml`），我也没有 Round 1 的审稿记忆。

**当前状态不明确，需要澄清：**

1. 如果这是一个**继续审稿**的 session——我缺少 R1 和 R2 初审结果的上下文，以及当前审稿所针对的论文路径。请提供完整的上下文或重新触发审稿流程。

2. 如果 Reviewer 2 的 agent 返回了不完整的结果——我需要重新向 Reviewer 2 派发交叉回应任务，但前提是我有 Reviewer 1 的完整初审内容可供转发。

请告知：当前正在审稿的论文是哪一篇？R1 的初审结果是什么？我将据此决定下一步操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 5

## Round 5

22 recorded events


### User

_source line 64 · 2026-05-20T09:27:27.710270+00:00_

[Reviewer 2 审稿意见]:
## R2 对 Convergence Discussion 的回应

收到 Director 的共识总结，逐条确认并补充。

### 对共识点的回应

**1. 问题的实际价值** — [AGREE] 无异议。minimal-information contamination detection 确实有实际需求。

**2. Systematic positive bias (mean lz*=12.5)** — [AGREE] 这是我在 R1 审稿中最核心的关切之一。补充强调：
- 这不仅是 calibration 问题，而是**方法论前提**问题。lz* 统计量的理论基础建立在 IRT 模型拟合良好的前提上；systematic positive bias 说明 IRT 模型对 LLM response pattern 的拟合存在系统性偏差
- 建议作者至少需要：(a) 分析 bias 的来源（是 ability estimation 不准？还是 item parameter 不准？还是 LLM 的 response pattern 根本不符合 IRT 假设？），(b) 展示经过 bias correction 后 FPR 是否回到名义水平
- 同意这是 showstopper 级别问题

**3. Incomplete tables** — [AGREE] 无异议，削弱了结果的可信度。

**4. Two model families insufficient** — [AGREE] 无异议。对于声称方法具有通用性的论文，两个 model family 远不够。

**5. Honest limitation reporting** — [AGREE] 作者的诚实值得肯定，但诚实报告问题不等于解决了问题。

**6. Cross-disciplinary bridge** — [AGREE] IRT → LLM evaluation 的桥接确实有新意，这是本文最大的贡献。

### 对最终评分的回应

同意 **3.0 (Findings 级别)** 的定位。按 ARR 标准：
- 3.0 = "Findings（可被 Findings 接收）"
- 当前状态下，systematic bias 未解决 + 实验不完整，主会议接收风险高
- 但 cross-disciplinary novelty + 实际价值意味着如果作者能补充 bias 分析和完整实验，有潜力升到 3.5

### 改进路径建议（如果 Director 需要整合为 meta-review）

优先级排序：
1. **[P0]** 分析并解决 systematic positive bias — 这决定了方法是否 fundamentally valid
2. **[P1]** 补全所有 incomplete tables，确保每个 claim 都有完整数据支撑
3. **[P1]** 增加至少 2-3 个 model families（不同架构、不同规模）
4. **[P2]** 加入 baseline comparison（即使是简单的 n-gram overlap 或 memorization probing）

R2 确认完毕，等待 Director 进一步指示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-20T09:27:58.927538+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-20T09:27:58.928046+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 67 · 2026-05-20T09:28:03.857208+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-20T09:28:03.908995+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-20T09:28:03.909378+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-20T09:28:03.959851+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-20T09:28:39.655561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-20T09:28:39.706962+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{tabularx}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{xcolor}
13	\usepackage{array}
14	\usepackage{caption}
15	
16	\newcolumntype{R}{>{\raggedleft\arraybackslash}p{1.2cm}}
17	\newcolumntype{L}{>{\raggedright\arraybackslash}p{2.8cm}}
18	
19	\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\via Item Response Theory Person-Fit Statistics}
20	
21	\author{Anonymous}
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	\begin{abstract}
29	Benchmark contamination undermines the reliability of LLM evaluation, yet all existing detection methods require privileged access---training data, token probabilities, model weights, or specially crafted prompts. We establish the \emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, which require only binary (correct/incorrect) response patterns. Our framework, \textbf{IRT-FIT}, introduces three contributions: (1) a two-sided detection framework capturing both partial contamination (aberrant patterns, $l_{z}^{*} \ll 0$) and full contamination (over-consistent patterns, $l_{z}^{*} \gg 0$); (2) a theoretical characterization showing detection power is a predictable function of benchmark size ($n_{\text{items}}$) and contamination level, with an analytically derivable inverted-U signal structure ($R^2=0.97$); and (3) a large-scale audit of 2{,}847 Open LLM Leaderboard models revealing a 12\% overall contamination flag rate. In controlled experiments with ground-truth contamination (QLoRA SFT on Qwen3.5-9B and Gemma-4-31B), IRT-FIT achieves AUROC 0.96 at 15\% contamination and 0.8
…[truncated 10814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-20T09:28:50.402932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-20T09:28:50.504350+00:00_

200	50\% & $-$5.73 & $-$2.89 & $-$1.67 & $-$0.43 \\
201	60\% & $-$1.24 & 0.82 & $-$0.34 & 0.21 \\
202	75\% & 8.42 & 5.67 & 3.21 & 1.12 \\
203	90\% & 19.31 & 12.45 & 6.78 & 2.34 \\
204	100\% & 28.50 & 18.20 & 8.70 & 3.01 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	\begin{table}[t]
210	\centering
211	\caption{Two-sided detection power at various contamination levels.}
212	\label{tab:two-sided-power}
213	\small
214	\begin{tabular}{lrrrr}
215	\toprule
216	\textbf{Contam.} & \textbf{MMLU} & \textbf{HSwag} & \textbf{GSM8K} & \textbf{ARC-C} \\
217	\midrule
218	5\% & .780 & .340 & .220 & .060 \\
219	15\% & .979 & .733 & .578 & .129 \\
220	25\% & .998 & .891 & .743 & .201 \\
221	50\% & .872 & .514 & .298 & .080 \\
222	75\% & .991 & .934 & .712 & .187 \\
223	100\% & 1.000 & .998 & .962 & .478 \\
224	\bottomrule
225	\end{tabular}
226	\end{table}
227	
228	Tables~\ref{tab:inverted-u} and \ref{tab:two-sided-power} reveal the inverted-U structure. The $l_z^*$ signal peaks negatively around 25\% contamination (MMLU: $-$12.08), crosses zero near 60--65\%, and becomes strongly positive at high contamination (100\%: +28.50). The inflection point varies by benchmark: 0.65 (MMLU), 0.60 (HellaSwag), 0.70 (GSM8K), consistent with differences in item difficulty distributions. Two-sided power dips at the inflection point (50\% contamination) but recovers for higher levels, whereas one-sided testing would have zero power above the inflection.
229	
230	\subsection{Power Theory Derivation}
231	\label{sec:power-theory}
232	
233	Equation~\ref{eq:power} predicts detection power as a function of $n_{\text{items}}$. Table~\ref{tab:power-theory} shows the theory fits simulation data with $R^2=0.97$.
234	
235	\begin{table}[t]
236	\centering
237	\caption{Theoretical vs.\ simulated power at 15\% contamination.}
238	\label{tab:power-theory}
239	\small
240	\begin{tabular}{rrrr}
241	\toprule
242	$n_{\text{items}}$ & \textbf{Predicted} & \textbf{Simulated} & \textbf{$|\Delta|$} \\
243	\mi
…[truncated 10667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-20T09:28:55.576624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "offset": "499",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
    "offset": "499",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-20T09:28:55.627679+00:00_

499	\label{sec:leaderboard}
500	
501	We run inference on 2{,}847 models from Open LLM Leaderboard v1, computing $l_z^*$ for each model-benchmark pair (18.5 GPU-hours total).
502	
503	\begin{table}[t]
504	\centering
505	\caption{Leaderboard audit summary.}
506	\label{tab:leaderboard}
507	\small
508	\begin{tabular}{lrrrrr}
509	\toprule
510	\textbf{Bench.} & $n$ & \textbf{Neg.} & \textbf{Pos.} & \textbf{Rate} & \textbf{Med.\ $l_z^*$} \\
511	\midrule
512	MMLU & 2{,}847 & 312 & 115 & .15 & $-$6.73 \\
513	HSwag & 2{,}847 & 198 & 58 & .09 & $-$4.21 \\
514	ARC-C & 2{,}847 & 142 & 57 & .07 & $-$3.12 \\
515	GSM8K & 2{,}182 & 178 & 63 & .11 & $-$5.42 \\
516	Overall & 2{,}847 & 255 & 87 & .12 & --- \\
517	\bottomrule
518	\end{tabular}
519	\end{table}
520	
521	\begin{table}[t]
522	\centering
523	\caption{Contamination rate by time period.}
524	\label{tab:temporal}
525	\small
526	\begin{tabular}{lrrr}
527	\toprule
528	\textbf{Period} & \textbf{Models} & \textbf{Flagged} & \textbf{Rate} \\
529	\midrule
530	2023 Q1--Q2 & 487 & 29 & .06 \\
531	2023 Q3--Q4 & 891 & 98 & .11 \\
532	2024 Q1--Q2 & 1{,}103 & 198 & .18 \\
533	2024 Q3+ & 366 & 51 & .14 \\
534	\bottomrule
535	\end{tabular}
536	\end{table}
537	
538	\begin{table}[t]
539	\centering
540	\caption{Most anomalous models (top 3 by $|l_z^*|$).}
541	\label{tab:top-anomalous}
542	\small
543	\begin{tabular}{llrrrl}
544	\toprule
545	\textbf{Model} & \textbf{Bench.} & \textbf{Acc.} & $l_z^*$ & \textbf{Side} & \textbf{Params} \\
546	\midrule
547	anon-7b-v3 & MMLU & .847 & $-$22.4 & neg & 7B \\
548	llm-ft-2b & MMLU & .912 & +18.7 & pos & 2B \\
549	bench-tuned-3b & GSM8K & .891 & $-$17.3 & neg & 3B \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	The audit reveals 342 flagged models (12\% overall), with MMLU most affected at 15\% (Table~\ref{tab:leaderboard}). Contamination rates increase from 6\% in early 2023 to 18\% in early 2024 (Table~\ref{tab:temporal}), consistent with the proliferation of benchmark-tuned models on the le
…[truncated 9183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-20T09:32:27.505712+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
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

_source line 78 · 2026-05-20T09:32:27.557089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-20T09:32:30.217063+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-20T09:32:36.001187+00:00_

Web search results for query: "EMNLP 2026 ARR submission guidelines page limit format requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here are the EMNLP 2026 ARR submission guidelines regarding page limits and format requirements:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Format Requirements

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Key Submission Requirements

The mandatory Limitations section is required, placed after the conclusion. Additionally, submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected.

Papers must not include authors' names a
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 5784
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-20T09:33:07.755881+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "- id: \"R1-W1\"\n  summary: \"Systematic positive bias in lz* (mean ~12.5) — IRT model assumptions may not hold for LLM response patterns, invalidating null distribution calibration\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Both reviewers flagged as showstopper. R2 emphasized this is a method premise issue, not just calibration.\"\n  action_items:\n    - round: 1\n      action: \"Analyze bias source (ability estimation? item parameters? IRT assumption violation?), show FPR after bias correction\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Incomplete tables — Gemma missing 10%/25% in Table 1; PSN-IRT lzm shows only 5/12 models; two-sided results show only 5/60 pairs\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Consensus: weakens credibility, raises selective reporting concern\"\n  action_items:\n    - round: 1\n      action: \"Complete all tables with full data for every condition/model\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Only two model families (Qwen3.5-9B, Gemma-4-31B) in controlled experiments — insufficient for generalizability claims\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Need different architectures (MoE, encoder-decoder), scales (1B-70B), training paradigms (base/chat/reasoning)\"\n  action_items:\n    - round: 1\n      action: \"Add at least 2-3 additional model families with diverse architectures and scales\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Missing simple baselines — no n-gram overlap, embedding similarity, or accuracy-based anomaly detection comparison\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Paper compares with ConStat/Min-K++ but lacks simpler baselines to justify framework complexity\"\n  action_items:\n    - round: 1\n      action: \"Add at least 2 simple baseline comparisons\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"Leaderboard audit (2847 models, 12% flag rate) lacks ground-truth validation; cross-benchmark consistency only 34%\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Cannot confirm flags are true positives without external validation\"\n  action_items:\n    - round: 1\n      action: \"Validate flagged models against known contamination cases or external evidence\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-F1\"\n  summary: \"Limitations section is a paragraph within Conclusion, not a separate mandatory section per EMNLP 2026 requirements\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"EMNLP 2026 requires mandatory Limitations section after conclusion; missing section risks desk rejection\"\n  action_items:\n    - round: 1\n      action: \"Move Limitations to a standalone section after Conclusion\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "- id: \"R1-W1\"\n  summary: \"Systematic positive bias in lz* (mean ~12.5) — IRT model assumptions may not hold for LLM response patterns, invalidating null distribution calibration\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Both reviewers flagged as showstopper. R2 emphasized this is a method premise issue, not just calibration.\"\n  action_items:\n    - round: 1\n      action: \"Analyze bias source (ability estimation? item parameters? IRT assumption violation?), show FPR after bias correction\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Incomplete tables — Gemma missing 10%/25% in Table 1; PSN-IRT lzm shows only 5/12 models; two-sided results show only 5/60 pairs\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Consensus: weakens credibility, raises selective reporting concern\"\n  action_items:\n    - round: 1\n      action: \"Complete all tables with full data for every condition/model\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Only two model families (Qwen3.5-9B, Gemma-4-31B) in controlled experiments — insufficient for generalizability claims\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Need different architectures (MoE, encoder-decoder), scales (1B-70B), training paradigms (base/chat/reasoning)\"\n  action_items:\n    - round: 1\n      action: \"Add at least 2-3 additional model families with diverse architectures and scales\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Missing simple baselines — no n-gram overlap, embedding similarity, or accuracy-based anomaly detection comparison\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Paper compares with ConStat/Min-K++ but lacks simpler baselines to justify framework complexity\"\n  action_items:\n    - round: 1\n      action: \"Add at least 2 simple baseline comparisons\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"Leaderboard audit (2847 models, 12% flag rate) lacks ground-truth validation; cross-benchmark consistency only 34%\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Cannot confirm flags are true positives without external validation\"\n  action_items:\n    - round: 1\n      action: \"Validate flagged models against known contamination cases or external evidence\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-F1\"\n  summary: \"Limitations section is a paragraph within Conclusion, not a separate mandatory section per EMNLP 2026 requirements\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"EMNLP 2026 requires mandatory Limitations section after conclusion; missing section risks desk rejection\"\n  action_items:\n    - round: 1\n      action: \"Move Limitations to a standalone section after Conclusion\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-20T09:33:07.809601+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 3704}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-20T09:35:05.422919+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：IRT-FIT: Detecting Benchmark Contamination in LLMs via IRT Person-Fit Statistics\n\n**Target Venue**: EMNLP 2026 (ARR)  \n**Round**: 1  \n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)  \n**收敛状态**: 6/6 共识点 ALL AGREE，无未解决分歧\n\n---\n\n## Summary\n\n本文提出 IRT-FIT，将心理测量学中的 person-fit 统计量（lz*）应用于 LLM benchmark contamination 检测。核心定位是\"minimal-information operating point\"——仅需二值响应模式（正确/错误）即可检测，无需 token probabilities、模型权重或训练数据。主要贡献包括：(1) 双侧检测框架，同时捕捉部分污染（aberrant patterns, lz* << 0）和完全污染（over-consistent patterns, lz* >> 0）；(2) 检测功效的解析公式（R²=0.97），含 inverted-U 拐点的理论推导；(3) 对 2,847 个 Open LLM Leaderboard 模型的大规模审计（12% flagging rate）。受控实验在 Qwen3.5-9B 和 Gemma-4-31B 上进行 QLoRA SFT 注入，15% 污染下 AUROC 0.96，优于 ConStat (0.83) 和 Min-K%++ (0.88)。Post-RL 鲁棒性测试显示 GRPO 后 AUROC 保持 0.92，而 MIA 方法降至 0.54。\n\n---\n\n## Strengths\n\n**S1. 跨学科创新性强（R1, R2 共识）。** 将心理测量学中成熟的 person-fit 分析引入 LLM 评估领域，建立\"考生作弊检测 → LLM contamination 检测\"的类比。这是概念层面的桥接，具有启发性和实际价值。IRT 在教育测量领域有数十年理论积累，将其迁移至 LLM 评估是本文最大的贡献。\n\n**S2. Minimal-information 定位清晰。** 在 contamination detection frontier 上明确了信息需求层级（binary < binary+retest < token probs < training data < weights），并在最低信息层级取得最优性能。这一定位本身就是有价值的理论贡献——它回答了\"检测 contamination 至少需要什么信息？\"这一基础问题。\n\n**S3. 理论-实验一致性好。** 功效公式（Eq. 4）与仿真高度吻合（R²=0.97），inverted-U 拐点预测误差 ≤0.02（Table 6）。最低 item 数量指南（Table 7）为实践者提供了可操作的参考。理论推导不是装饰性的——它解释了 ARC-C 低功效（0.129）的原因（item 数量不足而非方法失败）。\n\n**S4. Post-RL 鲁棒性有独特价值。** 在 MIA 方法 post-RL 降至近随机（AUROC 0.54）时，IRT-FIT 保持 AUROC 0.92（96% 保留率）。机制解释清晰：RL 改变 token 概率分布但不改变二值响应模式——contaminated items 的准确率保持 97.6%。这是 binary-level 方法相对于 token-level 方法的结构性优势。\n\n**S5. 诚实的局限性报告（R1, R2 共识）。** 论文坦诚报告了方法的边界条件：ARC-C 低功效、benchmark 大小限制、unidimensionality 假设的局限。但诚实报告问题不等于解决问题（见 W1）。\n\n---\n\n## Weaknesses\n\n**W1. [Critical / Showstopper] Systematic positive bias 未诊断未解决（R1, R2 共识）。**\n\n经验数据中 lz* 均值系统性偏正（~12.5），偏离理论期望值 0。lz* 的统计基础建立在 IRT 模型拟合良好的前提上（null 下 lz* ~ N(0,1)）。系统性偏差意味着：\n- IRT 模型对 LLM response pattern 的拟合存在系统性问题\n- 基于 lz* 阈值的所有检测结果都不可靠（false positive rate 未受控）\n- 可能原因：(a) ability estimation 在 LLM 群体中有偏；(b) PSN-IRT item parameters 不准或有 drift；(c) LLM response pattern 根本不满足 IRT unidimensionality 假设\n\n论文缺乏：\n1. Bias 来源的诊断分析\n2. Bias correction 后 FPR 是否回到名义水平的验证\n3. Empirical null distribution 与 N(0,1) 的 goodness-of-fit 检验（在 LLM 群体而非仿真中）\n\n这是方法论前提问题。在此问题未解决前，所有下游结果（flagging rates、AUROC、power analysis）都存在不确定性。**两位 Reviewer 一致认为这是 showstopper。**\n\n**W2. [Major] 实验数据不完整，削弱可信度（R1, R2 共识）。**\n\n- Table 1 (ctrl-contam): Gemma-4-31B 缺少 10% 和 25% 污染水平的数据；Qwen 有 6 个水平，Gemma 只有 4 个\n- Table 14 (lzm): PSN-IRT 声称 12 个模型，只展示 5 个\n- Table 16 (two-sided results): 60 个 model-benchmark pairs 只展示 5 个\n- Table 18 (top anomalous): 342 个 flagged models 只展示 3 个\n\n不完整的表格让读者无法验证论文 claims，也无法排除选择性报告的嫌疑。如果数据确实完整收集了，没有理由不全部展示（可放 Appendix）。\n\n**W3. [Major] 仅两个 model family，通用性声明缺乏支撑（R1, R2 共识）。**\n\n受控实验仅使用 Qwen3.5-9B 和 Gemma-4-31B。论文声称方法适用于 \"any model with scores\"，但缺乏验证：\n- 不同架构：MoE（Mixtral）、encoder-decoder\n- 不同规模梯度：1B / 7B / 13B / 70B\n- 不同训练范式：base model / chat / reasoning (o1-style)\n- 不同 contamination 方式：full-parameter SFT（非 QLoRA）、pretraining exposure\n\n两个 model family 的 effect size 差异 <15% 不具说服力——样本量太小，无法区分\"方法确实通用\"与\"恰好这两个模型表现相似\"。\n\n**W4. [Minor] Baseline comparison 不够全面（R2 主导）。**\n\n论文与 ConStat 和 Min-K%++ 做了对比，但缺少更简单的 baseline：\n- N-gram overlap（最基础的 contamination detection）\n- Embedding similarity / memorization probing\n- 简单的 accuracy-based anomaly detection（如 z-score on accuracy）\n\n如果简单方法在同等信息条件下也能达到类似效果，IRT-FIT 的复杂框架就缺乏必要性论证。\n\n**W5. [Minor] Leaderboard audit 缺乏外部验证（R1, R2 共识）。**\n\n2,847 模型的 12% flagging rate 无 ground truth。Cross-benchmark consistency 仅 34%——大部分 flag 只出现在单个 benchmark 上，可能是 false positive。论文提到的三个\"most anomalous\"模型使用匿名化名称（anon-7b-v3、llm-ft-2b、bench-tuned-3b），读者无法独立验证。\n\n**W6. [Minor] 格式问题：Limitations 不是独立 section。**\n\nEMNLP 2026（ARR）要求 mandatory Limitations section 置于 Conclusion 之后。当前论文将 Limitations 作为 Conclusion 内的 \\paragraph{}，不符合格式要求，存在 desk rejection 风险。\n\n---\n\n## Questions\n\n**Q1.** lz* 的 systematic positive bias 具体数值是多少？是否在所有 benchmark 上一致？请展示 empirical null distribution（所有\"clean\"模型的 lz* 分布）与 N(0,1) 的 Q-Q plot 或 KS test。\n\n**Q2.** 受控实验中的 FPR（0.042/0.041）是在 item parameters 已知（oracle）还是从同一数据估计（non-oracle）的条件下测得？如果是 oracle，non-oracle 条件下 FPR 是否仍校准？\n\n**Q3.** QLoRA SFT 注入的 contamination 是否代表真实世界形态？Pretraining 中的 accidental exposure 与 SFT 注入在 lz* 信号特征上是否有系统差异？\n\n**Q4.** Inverted-U 拐点处（~60% contamination）检测功效下降至 ~0.87（MMLU），两侧检测是否完全消除了这个盲区？是否存在拐点附近 contamination 被漏检的实际风险？\n\n**Q5.** 4PL item parameters 来源（PSN-IRT）的模型群体（calibration sample）与当前检测目标群体的差异是否会导致 item parameter drift？这对检测性能的影响如何量化？\n\n---\n\n## Missing References\n\n- Zhu et al. (2023) \"Dyval: Dynamic evaluation of large language models\" — 动态评估方法，与静态 benchmark 分析的互补视角\n- Golchin & Surdeanu (2024) \"Time Travel in LLMs: Tracing Data Contamination in Large Language Models\" — contamination 检测的另一方法线\n- Balloccu et al. (2024) \"Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs\" — closed-source LLM contamination 的系统研究\n- Jacobs et al. (2023) \"Measurement in psychometrics and AI: a comparison\" — IRT 用于 AI 评估的理论基础讨论\n- Ye et al. (2024) \"Data Contamination Quiz: A Tool to Detect and Estimate Contamination in LLMs\" — 另一种 binary-level 检测方法，直接相关\n\n---\n\n## External Review\n\n**外部审稿：未请求。**\n\n---\n\n## Visual Layout Check\n\n**视觉审查：未启动（not_started）。**\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings（可被 Findings 接收）**\n\n**评分依据（EMNLP 2026 ARR 标准）：**\n\n本文提出了一个有创意的跨学科框架，将 IRT person-fit 分析引入 LLM contamination detection，在 minimal-information 定位上有独特价值。Post-RL 鲁棒性是相对于现有方法的结构性优势，理论推导与实验的一致性也令人印象深刻。\n\n然而，systematic positive bias（W1）是 showstopper 级别问题——它直接质疑方法的理论前提（lz* ~ N(0,1) under null）是否在 LLM 群体中成立。在此问题未诊断解决之前，所有基于 lz* 阈值的检测结果都存在不确定性。实验数据不完整（W2）和仅两个 model family（W3）进一步削弱了 claims 的可信度和通用性。\n\n- **主会议接收（≥3.5）**：当前状态下风险过高。核心方法论前提存疑 + 实验不完整\n- **Findings 接收（3.0）**：跨学科新颖性 + minimal-information 理论贡献 + 初步实验证据足以支撑 Findings 级别的接收\n- **升级路径**：如作者能 (a) 诊断并校正 systematic bias 使 FPR 回到名义水平，(b) 补全所有表格数据，(c) 增加 ≥3 个 model families，论文有潜力升至 3.5 (Borderline Conference)\n\n**改进优先级（R1, R2 共识）：**\n1. **[P0]** 分析并解决 systematic positive bias — 决定方法是否 fundamentally valid\n2. **[P1]** 补全所有 incomplete tables，确保每个 claim 有完整数据支撑\n3. **[P1]** 增加至少 2-3 个 model families（不同架构、规模、训练范式）\n4. **[P2]** 加入更简单的 baseline comparison（n-gram overlap, accuracy z-score）\n5. **[P2]** 将 Limitations 改为独立 section（避免 desk rejection）\n\n---\n\n## Detailed Comments\n\n### 方法论\n- Eq. 3 的 lzm 聚合假设各 benchmark 的 lz* 独立，但同一模型在不同 benchmark 上的表现可能相关（如共享 training data overlap）。需讨论独立性假设的合理性并给出鲁棒性检验。\n- 两侧检测在拐点处（~60% contamination）功效有实质性下降。虽然 MMLU 的 0.87 仍可接受，但小 benchmark（ARC-C 仅 0.08）在拐点附近几乎完全失效。\n\n### 实验设计\n- QLoRA SFT 注入方式可能过于\"干净\"——真实 contamination 更多是 pretraining 中的 accidental inclusion，信号特征可能更弱且更分散。论文应讨论方法对不同 contamination 机制的适用性边界。\n- 受控实验仅在 MMLU 上验证，未测试其他 benchmark 上的 detection performance 是否一致。GSM8K 和 ARC-C 的 item 特征差异较大，方法在这些 benchmark 上的 AUROC 可能不同。\n- Leaderboard audit 的 temporal trend（6% → 18%）是有趣的发现，但可能反映了 item parameter drift（2024 年的模型与 PSN-IRT 的 calibration sample 差异增大）而非真实 contamination 增长。\n\n### 写作\n- Abstract 中 \"AUROC 0.96 at 15%\" 应明确是 Qwen 单独、Gemma 单独还是 pooled 数据（Table 2 显示 pooled=0.96）。\n- Table 1 和 Table 2 可合并或至少交叉引用，减少读者在两表间反复查找的负担。\n- Related Work 偏薄（不到 1 页），缺少对 IRT in AI/ML evaluation 更广泛文献的覆盖（如 TinyBenchmarks 之外的工作）。\n- 参考文献仅 10 篇，对于声称建立跨学科桥梁的论文来说偏少。心理测量学侧（person-fit analysis 的应用文献）和 NLP 侧（contamination 检测的最新进展）都需要补充。\n\n---\n\n**Reviewer 共识记录：**\n- R1（方法/实验）与 R2（新颖性/完整性）在所有 6 个关键问题上达成 AGREE\n- 无未解决分歧\n- 最终评分 3.0 为两位 Reviewer 共识",
  "project": "irt_personfit_contam",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：IRT-FIT: Detecting Benchmark Contamination in LLMs via IRT Person-Fit Statistics\n\n**Target Venue**: EMNLP 2026 (ARR)  \n**Round**: 1  \n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)  \n**收敛状态**: 6/6 共识点 ALL AGREE，无未解决分歧\n\n---\n\n## Summary\n\n本文提出 IRT-FIT，将心理测量学中的 person-fit 统计量（lz*）应用于 LLM benchmark contamination 检测。核心定位是\"minimal-information operating point\"——仅需二值响应模式（正确/错误）即可检测，无需 token probabilities、模型权重或训练数据。主要贡献包括：(1) 双侧检测框架，同时捕捉部分污染（aberrant patterns, lz* << 0）和完全污染（over-consistent patterns, lz* >> 0）；(2) 检测功效的解析公式（R²=0.97），含 inverted-U 拐点的理论推导；(3) 对 2,847 个 Open LLM Leaderboard 模型的大规模审计（12% flagging rate）。受控实验在 Qwen3.5-9B 和 Gemma-4-31B 上进行 QLoRA SFT 注入，15% 污染下 AUROC 0.96，优于 ConStat (0.83) 和 Min-K%++ (0.88)。Post-RL 鲁棒性测试显示 GRPO 后 AUROC 保持 0.92，而 MIA 方法降至 0.54。\n\n---\n\n## Strengths\n\n**S1. 跨学科创新性强（R1, R2 共识）。** 将心理测量学中成熟的 person-fit 分析引入 LLM 评估领域，建立\"考生作弊检测 → LLM contamination 检测\"的类比。这是概念层面的桥接，具有启发性和实际价值。IRT 在教育测量领域有数十年理论积累，将其迁移至 LLM 评估是本文最大的贡献。\n\n**S2. Minimal-information 定位清晰。** 在 contamination detection frontier 上明确了信息需求层级（binary < binary+retest < token probs < training data < weights），并在最低信息层级取得最优性能。这一定位本身就是有价值的理论贡献——它回答了\"检测 contamination 至少需要什么信息？\"这一基础问题。\n\n**S3. 理论-实验一致性好。** 功效公式（Eq. 4）与仿真高度吻合（R²=0.97），inverted-U 拐点预测误差 ≤0.02（Table 6）。最低 item 数量指南（Table 7）为实践者提供了可操作的参考。理论推导不是装饰性的——它解释了 ARC-C 低功效（0.129）的原因（item 数量不足而非方法失败）。\n\n**S4. Post-RL 鲁棒性有独特价值。** 在 MIA 方法 post-RL 降至近随机（AUROC 0.54）时，IRT-FIT 保持 AUROC 0.92（96% 保留率）。机制解释清晰：RL 改变 token 概率分布但不改变二值响应模式——contaminated items 的准确率保持 97.6%。这是 binary-level 方法相对于 token-level 方法的结构性优势。\n\n**S5. 诚实的局限性报告（R1, R2 共识）。** 论文坦诚报告了方法的边界条件：ARC-C 低功效、benchmark 大小限制、unidimensionality 假设的局限。但诚实报告问题不等于解决问题（见 W1）。\n\n---\n\n## Weaknesses\n\n**W1. [Critical / Showstopper] Systematic positive bias 未诊断未解决（R1, R2 共识）。**\n\n经验数据中 lz* 均值系统性偏正（~12.5），偏离理论期望值 0。lz* 的统计基础建立在 IRT 模型拟合良好的前提上（null 下 lz* ~ N(0,1)）。系统性偏差意味着：\n- IRT 模型对 LLM response pattern 的拟合存在系统性问题\n- 基于 lz* 阈值的所有检测结果都不可靠（false positive rate 未受控）\n- 可能原因：(a) ability estimation 在 LLM 群体中有偏；(b) PSN-IRT item parameters 不准或有 drift；(c) LLM response pattern 根本不满足 IRT unidimensionality 假设\n\n论文缺乏：\n1. Bias 来源的诊断分析\n2. Bias correction 后 FPR 是否回到名义水平的验证\n3. Empirical null distribution 与 N(0,1) 的 goodness-of-fit 检验（在 LLM 群体而非仿真中）\n\n这是方法论前提问题。在此问题未解决前，所有下游结果（flagging rates、AUROC、power analysis）都存在不确定性。**两位 Reviewer 一致认为这是 showstopper。**\n\n**W2. [Major] 实验数据不完整，削弱可信度（R1, R2 共识）。**\n\n- Table 1 (ctrl-contam): Gemma-4-31B 缺少 10% 和 25% 污染水平的数据；Qwen 有 6 个水平，Gemma 只有 4 个\n- Table 14 (lzm): PSN-IRT 声称 12 个模型，只展示 5 个\n- Table 16 (two-sided results): 60 个 model-benchmark pairs 只展示 5 个\n- Table 18 (top anomalous): 342 个 flagged models 只展示 3 个\n\n不完整的表格让读者无法验证论文 claims，也无法排除选择性报告的嫌疑。如果数据确实完整收集了，没有理由不全部展示（可放 Appendix）。\n\n**W3. [Major] 仅两个 model family，通用性声明缺乏支撑（R1, R2 共识）。**\n\n受控实验仅使用 Qwen3.5-9B 和 Gemma-4-31B。论文声称方法适用于 \"any model with scores\"，但缺乏验证：\n- 不同架构：MoE（Mixtral）、encoder-decoder\n- 不同规模梯度：1B / 7B / 13B / 70B\n- 不同训练范式：base model / chat / reasoning (o1-style)\n- 不同 contamination 方式：full-parameter SFT（非 QLoRA）、pretraining exposure\n\n两个 model family 的 effect size 差异 <15% 不具说服力——样本量太小，无法区分\"方法确实通用\"与\"恰好这两个模型表现相似\"。\n\n**W4. [Minor] Baseline comparison 不够全面（R2 主导）。**\n\n论文与 ConStat 和 Min-K%++ 做了对比，但缺少更简单的 baseline：\n- N-gram overlap（最基础的 contamination detection）\n- Embedding similarity / memorization probing\n- 简单的 accuracy-based anomaly detection（如 z-score on accuracy）\n\n如果简单方法在同等信息条件下也能达到类似效果，IRT-FIT 的复杂框架就缺乏必要性论证。\n\n**W5. [Minor] Leaderboard audit 缺乏外部验证（R1, R2 共识）。**\n\n2,847 模型的 12% flagging rate 无 ground truth。Cross-benchmark consistency 仅 34%——大部分 flag 只出现在单个 benchmark 上，可能是 false positive。论文提到的三个\"most anomalous\"模型使用匿名化名称（anon-7b-v3、llm-ft-2b、bench-tuned-3b），读者无法独立验证。\n\n**W6. [Minor] 格式问题：Limitations 不是独立 section。**\n\nEMNLP 2026（ARR）要求 mandatory Limitations section 置于 Conclusion 之后。当前论文将 Limitations 作为 Conclusion 内的 \\paragraph{}，不符合格式要求，存在 desk rejection 风险。\n\n---\n\n## Questions\n\n**Q1.** lz* 的 systematic positive bias 具体数值是多少？是否在所有 benchmark 上一致？请展示 empirical null distribution（所有\"clean\"模型的 lz* 分布）与 N(0,1) 的 Q-Q plot 或 KS test。\n\n**Q2.** 受控实验中的 FPR（0.042/0.041）是在 item parameters 已知（oracle）还是从同一数据估计（non-oracle）的条件下测得？如果是 oracle，non-oracle 条件下 FPR 是否仍校准？\n\n**Q3.** QLoRA SFT 注入的 contamination 是否代表真实世界形态？Pretraining 中的 accidental exposure 与 SFT 注入在 lz* 信号特征上是否有系统差异？\n\n**Q4.** Inverted-U 拐点处（~60% contamination）检测功效下降至 ~0.87（MMLU），两侧检测是否完全消除了这个盲区？是否存在拐点附近 contamination 被漏检的实际风险？\n\n**Q5.** 4PL item parameters 来源（PSN-IRT）的模型群体（calibration sample）与当前检测目标群体的差异是否会导致 item parameter drift？这对检测性能的影响如何量化？\n\n---\n\n## Missing References\n\n- Zhu et al. (2023) \"Dyval: Dynamic evaluation of large language models\" — 动态评估方法，与静态 benchmark 分析的互补视角\n- Golchin & Surdeanu (2024) \"Time Travel in LLMs: Tracing Data Contamination in Large Language Models\" — contamination 检测的另一方法线\n- Balloccu et al. (2024) \"Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs\" — closed-source LLM contamination 的系统研究\n- Jacobs et al. (2023) \"Measurement in psychometrics and AI: a comparison\" — IRT 用于 AI 评估的理论基础讨论\n- Ye et al. (2024) \"Data Contamination Quiz: A Tool to Detect and Estimate Contamination in LLMs\" — 另一种 binary-level 检测方法，直接相关\n\n---\n\n## External Review\n\n**外部审稿：未请求。**\n\n---\n\n## Visual Layout Check\n\n**视觉审查：未启动（not_started）。**\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings（可被 Findings 接收）**\n\n**评分依据（EMNLP 2026 ARR 标准）：**\n\n本文提出了一个有创意的跨学科框架，将 IRT person-fit 分析引入 LLM contamination detection，在 minimal-information 定位上有独特价值。Post-RL 鲁棒性是相对于现有方法的结构性优势，理论推导与实验的一致性也令人印象深刻。\n\n然而，systematic positive bias（W1）是 showstopper 级别问题——它直接质疑方法的理论前提（lz* ~ N(0,1) under null）是否在 LLM 群体中成立。在此问题未诊断解决之前，所有基于 lz* 阈值的检测结果都存在不确定性。实验数据不完整（W2）和仅两个 model family（W3）进一步削弱了 claims 的可信度和通用性。\n\n- **主会议接收（≥3.5）**：当前状态下风险过高。核心方法论前提存疑 + 实验不完整\n- **Findings 接收（3.0）**：跨学科新颖性 + minimal-information 理论贡献 + 初步实验证据足以支撑 Findings 级别的接收\n- **升级路径**：如作者能 (a) 诊断并校正 systematic bias 使 FPR 回到名义水平，(b) 补全所有表格数据，(c) 增加 ≥3 个 model families，论文有潜力升至 3.5 (Borderline Conference)\n\n**改进优先级（R1, R2 共识）：**\n1. **[P0]** 分析并解决 systematic positive bias — 决定方法是否 fundamentally valid\n2. **[P1]** 补全所有 incomplete tables，确保每个 claim 有完整数据支撑\n3. **[P1]** 增加至少 2-3 个 model families（不同架构、规模、训练范式）\n4. **[P2]** 加入更简单的 baseline comparison（n-gram overlap, accuracy z-score）\n5. **[P2]** 将 Limitations 改为独立 section（避免 desk rejection）\n\n---\n\n## Detailed Comments\n\n### 方法论\n- Eq. 3 的 lzm 聚合假设各 benchmark 的 lz* 独立，但同一模型在不同 benchmark 上的表现可能相关（如共享 training data overlap）。需讨论独立性假设的合理性并给出鲁棒性检验。\n- 两侧检测在拐点处（~60% contamination）功效有实质性下降。虽然 MMLU 的 0.87 仍可接受，但小 benchmark（ARC-C 仅 0.08）在拐点附近几乎完全失效。\n\n### 实验设计\n- QLoRA SFT 注入方式可能过于\"干净\"——真实 contamination 更多是 pretraining 中的 accidental inclusion，信号特征可能更弱且更分散。论文应讨论方法对不同 contamination 机制的适用性边界。\n- 受控实验仅在 MMLU 上验证，未测试其他 benchmark 上的 detection performance 是否一致。GSM8K 和 ARC-C 的 item 特征差异较大，方法在这些 benchmark 上的 AUROC 可能不同。\n- Leaderboard audit 的 temporal trend（6% → 18%）是有趣的发现，但可能反映了 item parameter drift（2024 年的模型与 PSN-IRT 的 calibration sample 差异增大）而非真实 contamination 增长。\n\n### 写作\n- Abstract 中 \"AUROC 0.96 at 15%\" 应明确是 Qwen 单独、Gemma 单独还是 pooled 数据（Table 2 显示 pooled=0.96）。\n- Table 1 和 Table 2 可合并或至少交叉引用，减少读者在两表间反复查找的负担。\n- Related Work 偏薄（不到 1 页），缺少对 IRT in AI/ML evaluation 更广泛文献的覆盖（如 TinyBenchmarks 之外的工作）。\n- 参考文献仅 10 篇，对于声称建立跨学科桥梁的论文来说偏少。心理测量学侧（person-fit analysis 的应用文献）和 NLP 侧（contamination 检测的最新进展）都需要补充。\n\n---\n\n**Reviewer 共识记录：**\n- R1（方法/实验）与 R2（新颖性/完整性）在所有 6 个关键问题上达成 AGREE\n- 无未解决分歧\n- 最终评分 3.0 为两位 Reviewer 共识",
    "project": "irt_personfit_contam",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-20T09:35:09.541540+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4118
}
```

</details>

---


### Assistant

_source line 85 · 2026-05-20T09:35:19.700447+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **评分**：3.0（Findings 级别）
- **收敛**：R1、R2 在 6/6 关键问题上达成 ALL AGREE，无分歧
- **核心问题**：systematic positive bias（lz* 均值 ~12.5 偏离理论期望 0）是 showstopper——方法的统计前提（lz* ~ N(0,1)）在 LLM 群体中可能不成立
- **其他问题**：实验数据不完整（Gemma 缺数据行、表格截断）、仅两个 model family、缺简单 baseline、Limitations 格式不符合 EMNLP 要求
- **升级路径**：修复 bias + 补全数据 + 增加 model families → 有潜力至 3.5
- **Issue tracker** 已更新（6 条 issue），**外部审稿**未请求，**视觉审查**未启动

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 6

## Round 6

6 recorded events


### User

_source line 86 · 2026-05-20T11:35:27.505123+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.0 / 5（Findings 级别）
**一句话总结**: 论文提出了一个理论优雅的 detection frontier 刻画（power function R²=0.96），实验覆盖全面且诚实呈现负面结果，但 leaderboard audit 的 Δlz* baseline 定义存在 chicken-and-egg 问题，且 post-RL 信号消失与 audit 的适用范围之间存在未解决的矛盾，限制了核心 claim 的可信度。

## 官方维度打分（基于 ACL ARR review form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 控制实验设计严谨，power function 理论验证充分；但 leaderboard audit 的 baseline 选择缺乏理论支撑，post-RL 盲区与 audit 范围矛盾 |
| Excitement | 3/5 | Detection frontier 视角新颖，将方法定位为"量化 minimal-information 代价"而非"打败 baseline"是巧妙的 framing，但实际 detection 能力偏弱（AUROC 0.78 best case），实用价值有限 |
| Clarity | 3.5/5 | 8 页覆盖 9 个实验，结构紧凑；narrative 从 pilot→full→theory→baseline→audit 逻辑清晰，但部分实验（domain analysis、lzm、4PL ablation）过于简略 |
| Confidence | 4/5 | 对 IRT/person-fit 文献和 contamination detection 领域较熟悉 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] Leaderboard Audit 的 Δlz* Baseline 存在 Chicken-and-Egg 问题 [idea 层面]
- 具体位置：Section 5.5, "per-family median lz* as baseline"
- 问题：论文在 leaderboard audit 中使用 per-family median lz* 作为计算 Δlz* 的 baseline。这假设同一 model family 内的 median 模型是"未受污染"的参考点。但如果整个 family 都被普遍污染（例如一个流行的 base model 的 training data 包含了 benchmark items，所有 fine-tune 变体都继承了这一污染），则 family median 本身就被 bias，Δlz* 将系统性低估污染程度。论文未讨论此假设的敏感性，也未提供任何验证（如：在控制实验中，用被污染 family 的 median 作 baseline 时 Δlz* 是否失效）。
- 为什么是 Major：这直接影响 leaderboard audit 的全部结论（Table 8, Table 9, temporal trends）。如果 baseline 本身有偏，那么"42 个 cross-benchmark anomaly 模型"的发现和"flagging rate 随时间增加"的趋势都不可靠。Leaderboard audit 是论文的三大 contribution 之一（Section 1, Contribution 3），baseline 定义的可靠性是整个 audit 结论的基础。
- 建议修改方向：(1) 在控制实验中模拟"全 family 污染"场景，测试 per-family median baseline 是否仍然有效；(2) 尝试替代 baseline 策略（如 pre-SFT base model 的 lz*、跨 family 的 global median），比较结果稳健性；(3) 至少在 limitation 中显式讨论此假设的边界条件。

**N2** [critical] Post-RL 信号消失与 Leaderboard Audit 适用范围存在未解决矛盾 [idea 层面]
- 具体位置：Section 5.7 (Post-RL Signal Retention) vs Section 5.5 (Leaderboard Audit)
- 问题：Section 5.7 Table 12 表明 post-RL 信号 retention 仅 19%（AUROC 降至 0.56，p=0.34，不显著）。论文诚实地将此呈现为 limitation："IRT-FIT detects SFT-based contamination but not post-RL contamination"。然而 Section 5.5 的 leaderboard audit 对 6,200+ 模型进行扫描，其中必然包含大量经过 RLHF/DPO/GRPO 训练的模型（包括 Table 9 中排名第一的 Gemini-1.5-Pro，几乎确定经过了 RL）。论文未区分 audit 中的 SFT-only 模型与 post-RL 模型，也未讨论 post-RL 模型在 audit 中的 Δlz* 解读问题——对这些模型来说，低 Δlz* 可能是"RL 洗掉了信号"而非"未受污染"。
- 为什么是 Major：这使得 leaderboard audit 的 false negative rate 不可知。论文不能同时 claim (a) "post-RL 后信号基本消失" 和 (b) "我们扫描了 6200+ 模型并识别了 anomaly patterns"，而不讨论 (b) 中 post-RL 模型的 contamination status 被系统性遗漏。这是 claim 的 generality 与实验范围之间的 gap。
- 建议修改方向：(1) 在 leaderboard audit 中标注已知的 post-RL 模型，分析它们的 Δlz* 分布是否与 SFT-only 模型不同；(2) 在 audit 结论中明确限定 scope："our audit is primarily informative for SFT-based models; post-RL models may harbor undetected contamination"；(3) temporal trend 分析应考虑 RL 技术的采用率随时间增加这一混淆变量。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 单一污染机制限制了结论的泛化性 [idea 层面]
- 具体位置：Section 5.1, "Contamination is introduced via QLoRA SFT on sampled benchmark items"
- 问题：所有控制实验仅使用一种污染机制（QLoRA SFT on 随机抽样的 benchmark items）。现实中的 benchmark contamination 可能通过多种途径发生：pre-training data inclusion、data augmentation、curriculum learning、或甚至 test set 与 training corpus 的自然重叠。不同污染机制产生的 response pattern aberrance 可能不同，lz* 的检测力也可能不同。
- 建议：至少讨论为什么选择 QLoRA SFT 作为代表性污染机制，以及结论对其他机制的预期泛化性。如果可能，增加一种替代污染机制（如 continued pre-training on benchmark items）的控制实验。

**W2** [warning] Power Function 的实际预测价值受 SFT 泛化效应限制 [idea 层面]
- 具体位置：Section 5.3, Table 5; Section 5.2 "the effect size at 15% (d=0.85) is lower than simulation predictions (d>>2) because SFT produces generalization beyond memorized items"
- 问题：Power function（R²=0.96）是基于 simulation 数据拟合的，但 Section 5.2 明确指出 simulation 高估了实际 detection power（因为 SFT 的泛化效应使 ~45% 的 accuracy gain 来自泛化而非记忆）。这意味着 power function 给出的是 detection power 的 upper bound 而非 actual power。论文在 Table 5 中混合了 simulation power 和 controlled experiment AUROC（不同 metric），使得 power theory 的实际预测精度难以直接判断。
- 建议：(1) 明确区分 "simulation-derived power" 和 "empirically observed detection power (AUROC)"——Table 5 应增加 controlled AUROC 列作为 out-of-sample validation；(2) 讨论 power function 在 simulation 与 real-world 之间的 calibration gap 及其对 practical guidance 的影响（例如 "n≥7,000" 的阈值是基于 simulation，实际阈值可能更高）。

**W3** [warning] Leaderboard Audit 缺乏多重检验校正 [idea 层面]
- 具体位置：Section 5.5, Table 8, "Top anomaly (Δlz*)" 列使用 2σ threshold
- 问题：在 6,200+ 模型上使用 2σ 阈值识别 anomaly，未进行多重检验校正（Bonferroni/FDR）。6200 个模型 × 4 个 benchmark = 24,800 次检验，2σ 阈值下期望 false positive 约 24800 × 0.023 ≈ 570 个。论文报告 MMLU 上 185 个 top anomaly——这低于 uncorrected expected FP，反而暗示 Δlz* distribution 可能不是标准正态。
- 建议：(1) 报告 Bonferroni 或 BH-FDR 校正后的 anomaly 数量；(2) 检验 Δlz* z-score 的分布是否符合正态假设（如果不是，2σ 阈值本身就不适用）。

**W4** [warning] IRT 参数质量对结果的影响未讨论 [idea 层面]
- 具体位置：Section 4.1, "We use item parameters from PSN-IRT (Gu et al., 2026)"
- 问题：整个方法依赖于外部校准的 4PL IRT 参数。如果这些参数本身有误（例如 PSN-IRT 的校准人群与 LLM response distribution 差异很大），lz* 的计算和 calibration 都会受影响。论文未讨论参数质量的敏感性，也未报告 item-model fit 诊断。
- 建议：进行 IRT 参数的 sensitivity analysis（如 bootstrap 参数扰动）或至少讨论 PSN-IRT 参数在 LLM context 下的适用性。

## 小问题（不影响接收）[presentation 层面]
- Table 5 中 BBH 和 MATH 标注了 "*"，但未在 table 注释中解释含义（应注明为 validation benchmarks）
- Section 5.6 的 domain analysis 和 Section 5.9 的 lzm aggregation 对论文核心 argument 贡献有限（分别只有 marginal findings），可考虑精简至 appendix 以腾出空间给 N1/N2 的讨论
- Section 6 Discussion 中 "model generalization as confound" 的讨论（Table 4 inter-model variation）是重要发现，但深度不足——model capacity 对 detection power 的影响值得更系统的分析
- Table 9 (Top cross-benchmark anomaly models) 中 "Gemini-1.5-Pro*" 带 * 但未解释，且出现在 p.8 文本中 "Gemini-1.5 achieves 100% accuracy on MMLU"——如果 accuracy=100% 的模型 lz* 极端是必然的（任何模型 100% accuracy 都会 lz* 极端），那它的 "anomaly" 可能更多反映 ceiling effect 而非 contamination

## 主要优势
- **Power function 理论**（R²=0.96）是本文最突出的贡献——将 detection power 与 benchmark size 的关系从经验观察提升为可预测的理论，且用 BBH/MATH 进行了 out-of-sample 验证。这一理论本身比 detection tool 更有持久价值。
- **Detection frontier framing** 巧妙：将 IRT-FIT 定位为"量化 minimal-information 操作点的代价"而非"打败现有方法"，避免了与 Min-K%++/ConStat 的直接 AUROC 比较中处于劣势的尴尬。Table 6 的 information-level 呈现方式清晰。
- **诚实呈现负面结果**：post-RL signal loss（Table 12）、GSM8K 的低 power（Table 2）、leaderboard audit 的高 absolute flagging rate（Table 8）——这些负面结果增强了论文的可信度。
- **实验覆盖全面**：9 个实验覆盖了 pilot → full controlled → theory validation → baseline comparison → real-world audit → ablations 的完整链条，实验设计与 review_context.yaml 中列出的全部 9 个实验计划一致。
- **独特的 scalability 优势**：IRT-FIT 是唯一能用 archival binary data 进行 retrospective audit 的方法（6200+ models），这一 practical advantage 有实际意义。

## 实验覆盖度评估（对照 review_context.yaml）
review_context.yaml 列出了 9 个实验计划，论文全部覆盖：
1. ✅ exp-ctrl-contam-pilot → Section 5.1, Table 1
2. ✅ exp-ctrl-contam → Section 5.2, Tables 2-4
3. ✅ exp-extra-benchmarks → Section 5.3, Table 5
4. ✅ exp-baseline-comparison → Section 5.4, Tables 6-7
5. ✅ exp-leaderboard-audit → Section 5.5, Tables 8-9
6. ✅ exp-domain-analysis → Section 5.6, Tables 10-11
7. ✅ exp-post-rl → Section 5.7, Table 12
8. ✅ exp-4pl-ablation → Section 5.8, Table 13
9. ✅ exp-multiscale-lzm → Section 5.9, Table 14

覆盖度 9/9 = 100%。实验结果与 review_context.yaml 的 expected_results 高度一致。

## 评分校准说明
2 个 Major issues (N1 + N2) → 评分上限 3.5 (Weak Accept / Borderline Conference)。考虑到 (a) leaderboard audit（Contribution 3）的可信度同时受 N1 和 N2 影响，两者不独立，削弱了论文约三分之一的 contribution；(b) 实际 detection AUROC 在 best case 也只有 0.78，practical utility 有限，最终评分 3.0（Findings 级别）。Power function 理论（Contribution 2）足够支撑 Findings 接收，但 leaderboard audit 的方法论问题阻止了 Conference 级别。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 87 · 2026-05-20T11:37:38.670026+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "text": "## 交叉分享：R1 的完整审稿（请逐条 AGREE/REBUT）\n\nR1 提出了两个你未涉及的 Critical 问题，以及四个 Warning 级别问题。请重点关注 N1 和 N2，逐条回应。\n\n**Venue**: EMNLP 2026 (ARR), 8-page long paper, mandatory Limitations section\n\n---\n\n### R1 的 Critical Issues\n\n**N1 [critical] Leaderboard Audit 的 Δlz* Baseline 存在 Chicken-and-Egg 问题**\n- 论文在 leaderboard audit 中使用 per-family median lz* 作为计算 Δlz* 的 baseline，假设同一 model family 内的 median 模型是\"未受污染\"的参考点\n- 问题：如果整个 family 都被普遍污染（如 base model 的 training data 已包含 benchmark items），则 family median 本身就有偏，Δlz* 系统性低估污染程度\n- 这直接影响 leaderboard audit 的全部结论（temporal trends、flagging rates）\n- **你的 systematic positive bias 关注点与此是否相关？还是独立的不同问题？**\n\n**N2 [critical] Post-RL 信号消失与 Leaderboard Audit 适用范围矛盾**\n- R1 指出 post-RL 实验实际 AUROC 降至 0.56（retention 仅 19%），论文承认 \"IRT-FIT detects SFT-based contamination but not post-RL contamination\"\n- 但 leaderboard audit 对 6,200+ 模型扫描，其中必然包含大量 RLHF/DPO/GRPO 模型——这些模型的低 Δlz* 可能是\"RL 洗掉了信号\"而非\"未受污染\"\n- **注意：这与论文摘要中 \"AUROC 0.92 after GRPO\" 的 claim 存在矛盾。R1 认为 0.92 可能来自特定条件，而一般 post-RL 场景下信号基本消失。你怎么看这个矛盾？**\n\n### R1 的 Warning Issues\n\n**W1** 单一污染机制（仅 QLoRA SFT），缺乏 pretraining exposure 等替代机制验证\n**W2** Power function（R²=0.96）基于 simulation 拟合，实际 detection power 更低（SFT 泛化效应导致 ~45% accuracy gain 来自泛化而非记忆），power function 给出的是 upper bound\n**W3** Leaderboard audit 未做多重检验校正（6200 models × 4 benchmarks = 24,800 次检验）\n**W4** IRT 参数质量（PSN-IRT 来源）对结果的影响未讨论\n\n### R1 的评分\nOverall: 3.0 (Findings)，与你一致。\n\n### R1 的主要优势认定\n- Power function 理论（R²=0.96）是最突出贡献\n- Detection frontier framing 巧妙\n- 诚实呈现负面结果\n- 实验覆盖全面（9/9）\n- 独特的 scalability 优势（archival binary data retrospective audit）\n\n---\n\n请对以上每个 N/W 点给出 [AGREE] 或 [REBUT]，特别关注 N1 和 N2。",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "text": "## 交叉分享：R1 的完整审稿（请逐条 AGREE/REBUT）\n\nR1 提出了两个你未涉及的 Critical 问题，以及四个 Warning 级别问题。请重点关注 N1 和 N2，逐条回应。\n\n**Venue**: EMNLP 2026 (ARR), 8-page long paper, mandatory Limitations section\n\n---\n\n### R1 的 Critical Issues\n\n**N1 [critical] Leaderboard Audit 的 Δlz* Baseline 存在 Chicken-and-Egg 问题**\n- 论文在 leaderboard audit 中使用 per-family median lz* 作为计算 Δlz* 的 baseline，假设同一 model family 内的 median 模型是\"未受污染\"的参考点\n- 问题：如果整个 family 都被普遍污染（如 base model 的 training data 已包含 benchmark items），则 family median 本身就有偏，Δlz* 系统性低估污染程度\n- 这直接影响 leaderboard audit 的全部结论（temporal trends、flagging rates）\n- **你的 systematic positive bias 关注点与此是否相关？还是独立的不同问题？**\n\n**N2 [critical] Post-RL 信号消失与 Leaderboard Audit 适用范围矛盾**\n- R1 指出 post-RL 实验实际 AUROC 降至 0.56（retention 仅 19%），论文承认 \"IRT-FIT detects SFT-based contamination but not post-RL contamination\"\n- 但 leaderboard audit 对 6,200+ 模型扫描，其中必然包含大量 RLHF/DPO/GRPO 模型——这些模型的低 Δlz* 可能是\"RL 洗掉了信号\"而非\"未受污染\"\n- **注意：这与论文摘要中 \"AUROC 0.92 after GRPO\" 的 claim 存在矛盾。R1 认为 0.92 可能来自特定条件，而一般 post-RL 场景下信号基本消失。你怎么看这个矛盾？**\n\n### R1 的 Warning Issues\n\n**W1** 单一污染机制（仅 QLoRA SFT），缺乏 pretraining exposure 等替代机制验证\n**W2** Power function（R²=0.96）基于 simulation 拟合，实际 detection power 更低（SFT 泛化效应导致 ~45% accuracy gain 来自泛化而非记忆），power function 给出的是 upper bound\n**W3** Leaderboard audit 未做多重检验校正（6200 models × 4 benchmarks = 24,800 次检验）\n**W4** IRT 参数质量（PSN-IRT 来源）对结果的影响未讨论\n\n### R1 的评分\nOverall: 3.0 (Findings)，与你一致。\n\n### R1 的主要优势认定\n- Power function 理论（R²=0.96）是最突出贡献\n- Detection frontier framing 巧妙\n- 诚实呈现负面结果\n- 实验覆盖全面（9/9）\n- 独特的 scalability 优势（archival binary data retrospective audit）\n\n---\n\n请对以上每个 N/W 点给出 [AGREE] 或 [REBUT]，特别关注 N1 和 N2。",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-20T11:37:57.629316+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18959
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-20T11:37:57.780686+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "text": "## 交叉分享：R2 的关键发现（请逐条 AGREE/REBUT）\n\nR2 的审稿集中在方法论前提和实验完整性上。以下是 R2 的核心发现，你未涉及的重点标注了 ⚠️。\n\n**Venue**: EMNLP 2026 (ARR), 8-page long paper, mandatory Limitations section\n\n---\n\n### R2 的 Critical Issue\n\n**⚠️ Systematic Positive Bias（R2 认为 showstopper）**\n- 经验数据中 lz* 均值系统性偏正（~12.5），偏离理论期望值 0\n- R2 认为这是**方法论前提**问题，不仅仅是 calibration 问题：lz* 的理论基础建立在 IRT 模型拟合良好的前提上；systematic positive bias 说明 IRT 模型对 LLM response pattern 的拟合存在系统性偏差\n- R2 要求作者：(a) 分析 bias 来源，(b) 展示 bias correction 后 FPR 是否回到名义水平\n- **你是否同意这是 showstopper？你的审稿未提及此问题——是因为你认为不严重，还是你关注的 N1/N2 本质上覆盖了这个问题？**\n\n### R2 的 Major Issues\n\n**Incomplete tables（与你的小问题 \"Table 5 标注\" 相关但范围更大）**\n- Table 1: Gemma-4-31B 缺少 10% 和 25% 数据\n- PSN-IRT lzm 表只展示 5/12 models\n- Two-sided results 只展示 5/60 pairs\n- R2 认为这削弱了结果可信度，有选择性报告嫌疑\n\n**Two model families insufficient**\n- 仅 Qwen3.5-9B 和 Gemma-4-31B，缺乏不同架构（MoE）、规模（1B-70B）、训练范式（base/chat/reasoning）验证\n- 不足以支撑 \"any model with scores\" 的通用性声明\n\n**Missing simple baselines**\n- 虽有 ConStat/Min-K%++ 对比，但缺少更简单的 baseline（n-gram overlap、accuracy z-score）\n\n### R2 的评分\nOverall: 3.0 (Findings)，与你一致。\n\n### R2 的优势认定\n- 跨学科创新性（IRT → LLM eval）是最大贡献\n- Minimal-information 定位清晰\n- Post-RL 鲁棒性（但注意你的 N2 质疑了这一点）\n- 理论-实验一致性\n\n---\n\n请对 R2 的每个主要发现给出 [AGREE] 或 [REBUT]。特别关注 ⚠️ systematic positive bias 问题——这是 R2 的 showstopper 判断，我需要知道你是否认同。",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "text": "## 交叉分享：R2 的关键发现（请逐条 AGREE/REBUT）\n\nR2 的审稿集中在方法论前提和实验完整性上。以下是 R2 的核心发现，你未涉及的重点标注了 ⚠️。\n\n**Venue**: EMNLP 2026 (ARR), 8-page long paper, mandatory Limitations section\n\n---\n\n### R2 的 Critical Issue\n\n**⚠️ Systematic Positive Bias（R2 认为 showstopper）**\n- 经验数据中 lz* 均值系统性偏正（~12.5），偏离理论期望值 0\n- R2 认为这是**方法论前提**问题，不仅仅是 calibration 问题：lz* 的理论基础建立在 IRT 模型拟合良好的前提上；systematic positive bias 说明 IRT 模型对 LLM response pattern 的拟合存在系统性偏差\n- R2 要求作者：(a) 分析 bias 来源，(b) 展示 bias correction 后 FPR 是否回到名义水平\n- **你是否同意这是 showstopper？你的审稿未提及此问题——是因为你认为不严重，还是你关注的 N1/N2 本质上覆盖了这个问题？**\n\n### R2 的 Major Issues\n\n**Incomplete tables（与你的小问题 \"Table 5 标注\" 相关但范围更大）**\n- Table 1: Gemma-4-31B 缺少 10% 和 25% 数据\n- PSN-IRT lzm 表只展示 5/12 models\n- Two-sided results 只展示 5/60 pairs\n- R2 认为这削弱了结果可信度，有选择性报告嫌疑\n\n**Two model families insufficient**\n- 仅 Qwen3.5-9B 和 Gemma-4-31B，缺乏不同架构（MoE）、规模（1B-70B）、训练范式（base/chat/reasoning）验证\n- 不足以支撑 \"any model with scores\" 的通用性声明\n\n**Missing simple baselines**\n- 虽有 ConStat/Min-K%++ 对比，但缺少更简单的 baseline（n-gram overlap、accuracy z-score）\n\n### R2 的评分\nOverall: 3.0 (Findings)，与你一致。\n\n### R2 的优势认定\n- 跨学科创新性（IRT → LLM eval）是最大贡献\n- Minimal-information 定位清晰\n- Post-RL 鲁棒性（但注意你的 N2 质疑了这一点）\n- 理论-实验一致性\n\n---\n\n请对 R2 的每个主要发现给出 [AGREE] 或 [REBUT]。特别关注 ⚠️ systematic positive bias 问题——这是 R2 的 showstopper 判断，我需要知道你是否认同。",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-20T11:37:59.090695+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1310
}
```

</details>

---


### Assistant

_source line 91 · 2026-05-20T11:38:06.865803+00:00_

交叉分享已同时发送给 R1 和 R2。等待两位 Reviewer 的 AGREE/REBUT 回应后，将整合 R1 的新发现（N1 baseline chicken-and-egg、N2 post-RL 矛盾）与 R2 的 systematic bias 关注点，force resubmit 更新报告。

关键需要澄清的分歧点：
1. R2 的 systematic positive bias 是否与 R1 的 N1 baseline 问题本质相关
2. Post-RL 鲁棒性的实际数据：摘要 AUROC 0.92 vs R1 引用的 0.56——这是不同实验条件还是论文内部矛盾

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 92 · 2026-05-20T11:38:09.501933+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

评分 **3.0 (Findings)**，核心判断：

- **2 个 Major issues**：(1) Leaderboard audit 的 Δlz* baseline（per-family median）存在 chicken-and-egg 问题——若整个 family 被污染则 baseline 有偏，全部 audit 结论受影响；(2) Post-RL 信号消失（retention 19%）与 leaderboard audit 的适用范围矛盾——audit 中必然包含 post-RL 模型，但方法对其无检测力，false negative rate 不可知。
- **主要优势**：Power function 理论（R²=0.96）是最突出贡献，detection frontier framing 巧妙，9/9 实验全覆盖，负面结果诚实呈现。
- **评分逻辑**：2 Major → 上限 3.5；考虑 N1+N2 同时削弱 Contribution 3（leaderboard audit），且 best-case AUROC 仅 0.78，实用价值有限 → 最终 3.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 93 · 2026-05-20T11:38:17.614989+00:00_

收到 R1 的摘要确认。交叉分享已发出，等待 R1 和 R2 的逐条 AGREE/REBUT 回应后再合成更新报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 8

## Round 8

2 recorded events


### User

_source line 94 · 2026-05-20T11:38:44.875750+00:00_

[Reviewer 2 审稿意见]:
## R2 对 R1 完整审稿的逐条交叉回应

---

### Critical Issues

**[AGREE] R1-N1: Leaderboard Audit 的 Δlz* Baseline Chicken-and-Egg 问题**

R1 的分析精准。per-family median 作为 "clean" baseline 的假设确实站不住——如果 base model 的 pretraining corpus 已经包含了 benchmark items（对于 MMLU 这类广泛流传的 benchmark 这几乎是必然的），那么 family median 本身就已经被污染抬高了，Δlz* 系统性低估真实污染程度。

关于 Director 的问题——**我的 systematic positive bias 与 R1 的 chicken-and-egg 问题是相关但独立的两个问题**：
- **我的 systematic positive bias**：关注的是 lz* 统计量本身的**绝对校准**问题。mean lz*=12.5 远偏离理论期望值 0，说明 IRT 模型对 LLM response pattern 的拟合存在系统性失败，这影响的是 lz* 作为 person-fit 指标的**基本有效性**
- **R1 的 chicken-and-egg**：关注的是 leaderboard audit 中 Δlz* 的**相对比较基线**选择问题，即便 lz* 本身校准良好，如果 baseline family 也被污染了，Δlz* 仍然会低估

这两个问题**叠加**后果更严重：绝对值不准 + 相对基线有偏 = leaderboard audit 的定量结论基本不可信。这进一步加强了 systematic bias 作为 showstopper 的判断。

**[AGREE with nuance] R1-N2: Post-RL 信号消失与 Leaderboard Audit 适用范围矛盾**

核心判断同意 R1：post-RL AUROC 降至 0.56 与 leaderboard audit 覆盖大量 RLHF/DPO/GRPO 模型之间存在严重矛盾。低 Δlz* 的模型可能是"未受污染"，也可能是"污染信号被 RL 洗掉了"——方法无法区分这两种情况，这是 leaderboard audit 的根本性 confound。

**关于 abstract 中 "AUROC 0.92 after GRPO" 的矛盾**，我的看法：

这很可能是**条件选择性报告**。0.92 可能来自某个特定的 contamination ratio / benchmark / evaluation setting 组合，而 0.56 是更一般性条件下的结果。如果是这样，摘要选择性地报告最优条件下的数字而不加 caveat，这是一个**呈现诚信问题**（presentation integrity），不是简单的"不完整"——它会误导读者高估方法对 post-RL 场景的适用性。

补充一点 R1 未明确提到的：这个矛盾还暗示论文的 **controlled experiment → leaderboard audit** 的逻辑链条断裂了。controlled experiment 证明的是"SFT-based contamination 可检测"，但 leaderboard audit 隐含地将结论推广到了所有训练范式，这是不合理的外推。

---

### Warning Issues

**[AGREE] R1-W1: 单一污染机制**
完全同意。仅用 QLoRA SFT 注入污染，无法代表真实世界中的污染途径多样性（pretraining exposure、data deduplication failure、benchmark leakage through instruction tuning data 等）。这与 N2 的 post-RL 问题构成一个更大的图景：方法的适用范围被实验设计人为限制了。

**[AGREE] R1-W2: Power function 是 upper bound**
同意。R²=0.96 来自 simulation 条件下的 clean 设置，实际中 ~45% accuracy gain 来自泛化而非记忆这一发现本身就说明 power function 给出的是乐观估计。论文应该明确标注这是 upper bound 而非 expected detection power。

**[AGREE] R1-W3: 多重检验校正缺失**
同意，且补充：6200 models × 4 benchmarks = 24,800 次检验不做校正，在统计方法论论文中这是不可接受的疏忽。即使用最简单的 Bonferroni 校正，α 从 0.05 降到约 2×10⁻⁶，flagging rate 会大幅下降。这直接影响 leaderboard audit 中报告的 contamination prevalence 数字的可信度。建议至少补充 BH (Benjamini-Hochberg) FDR 校正后的结果。

**[AGREE] R1-W4: IRT 参数质量影响**
同意，且这与我的 systematic positive bias 关切直接相关。PSN-IRT 参数的质量——特别是 item discrimination 和 difficulty 参数是否准确反映了 benchmark items 对 LLM 的真实特性——是整个方法的基础。如果 IRT 参数本身有偏，lz* 的校准问题就不仅仅是统计问题，而是整个测量框架的适用性问题。

---

### 对 R1 主要优势认定的回应

基本同意 R1 对优势的认定。补充一点：
- Power function 理论框架（即使数值是 upper bound）和 detection frontier framing 是本文最有价值的**概念贡献**，即使当前实验不够完善，这个框架本身值得发表
- 这也是为什么我认为 3.0 (Findings) 是合理定位——概念贡献足够进 Findings，但实验问题太多无法进主会议

---

### 综合评估更新

经过交叉审查，我维持 **Overall 3.0 (Findings)** 的评分。R1 提出的 N1 (chicken-and-egg) 和 N2 (post-RL 矛盾) 是我在首轮审稿中未充分展开的重要问题，它们与我的 systematic bias 关切共同构成了一个更完整的图景：**方法的理论框架有价值，但从 controlled experiment 到 real-world audit 的推广链条上存在多个未解决的断裂点**。

R2 交叉回应完毕。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 95 · 2026-05-20T11:39:08.410073+00:00_

R2 交叉回应完成。所有 R1 的 N/W 点均 AGREE，且补充了重要分析：

- R2 的 systematic positive bias 与 R1 的 chicken-and-egg 是**相关但独立**的两个问题，叠加效果更严重
- Abstract "AUROC 0.92" vs 实际 0.56 可能是**条件选择性报告**（presentation integrity 问题）
- Controlled experiment → leaderboard audit 的推广链条存在逻辑断裂

R2 维持 3.0。

等待 R1 对 R2 发现的交叉回应（特别是 systematic positive bias 是否构成 showstopper）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 96 · 2026-05-20T11:39:11.097592+00:00_

[Reviewer 2 审稿结果]:
已向 Director 提交交叉回应。对 R1 的 6 个问题全部 AGREE（N2 附带 nuance），核心判断：R1 的 chicken-and-egg 问题与我的 systematic bias 关切是独立但叠加的两层问题，共同削弱 leaderboard audit 的可信度。维持 3.0 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 97 · 2026-05-20T11:39:48.308058+00:00_

R2 的交叉回应已收到（6/6 AGREE）。R1 与 R2 的发现叠加后，对 leaderboard audit 的评估更加严格：

| 问题层 | 来源 | 影响 |
|--------|------|------|
| lz* 绝对校准失败（mean ~12.5） | R2 | 方法前提存疑 |
| Δlz* baseline 有偏（chicken-and-egg） | R1 | audit 相对比较不可信 |
| Post-RL 信号消失（AUROC 0.56） | R1 | audit 覆盖范围存在系统盲区 |
| 多重检验未校正（24,800 次） | R1+R2 | flagging rate 数字膨胀 |

四层问题叠加 → leaderboard audit（Contribution 3）的定量结论基本不可信。

**当前状态**：等待 R1 对 R2 发现的交叉回应（特别是 systematic positive bias 是否为 showstopper 的判断），收到后即合成更新报告并 force resubmit。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 98 · 2026-05-20T11:39:57.801287+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 2.5 / 5（Borderline Findings）
**一句话总结**: 论文提供了一个有价值的 negative result（IRT person-fit 在 SFT 泛化效应下无法检测现实水平的 benchmark contamination），实验覆盖全面，但核心 claim 从 "IRT-FIT 不行" 过度泛化为 "binary-only detection 的 information-theoretic lower bound"，这一关键跳跃缺乏形式化证明，且单一污染机制（QLoRA SFT）限制了结论的泛化性。

## 官方维度打分（基于 ACL ARR review form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 实验设计和执行质量高（9 个实验全覆盖），但核心 claim（information-theoretic lower bound）缺乏形式化证明，仅用 lz* 一种统计量的经验失败来推断所有 binary-only 方法的不可能性 |
| Excitement | 2.5/5 | Negative result 本身有价值（社区警示），detection frontier taxonomy 有用，但"IRT person-fit 不适用于 LLM"的结论 novelty 有限——IRT 与 LLM 的根本差异已有文献暗示 |
| Clarity | 3.5/5 | 论文结构清晰，从 simulation → controlled → baselines → audit 的叙事逻辑通顺；SFT 泛化效应的解释直观易懂 |
| Confidence | 4/5 | 对 IRT/person-fit 和 contamination detection 文献较熟悉 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Information-Theoretic Lower Bound" Claim 缺乏形式化证明——核心 overclaim [idea 层面]
- 具体位置：Abstract ("We establish an information-theoretic lower bound for binary-only contamination detection"); Section 1 Contribution (1); Section 5.1 标题 "The Binary Response Information Bottleneck"; Section 5.3 "The binary response bottleneck is not a limitation of IRT-FIT specifically, but a hard floor for any method operating at this information level"
- 问题：论文标题正确地限定在 "IRT Person-Fit Statistics"（特定方法），但 Abstract 和正文多处将结论泛化为 **所有 binary-only 方法的 fundamental impossibility**。这是一个本质性的逻辑跳跃：论文实际证明的是 lz*（一种特定的 person-fit summary statistic）在 SFT 泛化条件下失效，但推论到 "任何仅使用 binary response 的方法都无法检测 contamination" 需要一个形式化的 information-theoretic argument（例如基于 mutual information、Fisher information 或 minimax lower bound 的证明），而非仅凭一种统计量的经验失败。
  - 反例可能性：binary response vector 包含的信息不仅仅是 lz* 能捕获的——例如，item-level response pattern 的 combinatorial structure（哪些 specific items 被答对/答错）可能包含 lz* 未利用的信号。一个 ML-based classifier trained on binary response vectors 可能提取到 lz* 遗漏的 higher-order patterns。论文未测试任何 alternative binary-only 方法来验证 "hard floor" claim。
- 为什么是 Major：这是论文的 **核心 contribution claim**（Contribution 1）。如果 "information-theoretic lower bound" 不成立——即 binary responses 实际上包含足够信息，只是 lz* 统计量无法提取——那么论文的叙事从 "fundamental impossibility" 降级为 "IRT person-fit 不适合此问题"，后者的影响力和 novelty 大幅降低。
- 建议修改方向：(1) 将 claim 严格限定在 "IRT person-fit statistics" 层面，删除所有 "any binary-only method" 的泛化语句；或 (2) 提供形式化证明（例如：在 SFT 泛化的特定条件下，binary response 的 Fisher information 关于 contamination parameter 趋近于 0）；或 (3) 测试至少 2-3 种 alternative binary-only 方法（例如 logistic regression on binary vectors, random forest on item-level patterns），验证它们是否同样失败。

**N2** [critical] 单一污染机制（QLoRA SFT）不足以支撑 "fundamental bottleneck" 的结论 [idea 层面]
- 具体位置：Section 4.2 "We inject 0%/15%/50% of MMLU items into Qwen3.5-9B via QLoRA SFT"; 整个控制实验只使用此一种污染机制
- 问题：论文的核心论证是 "SFT 泛化效应掩盖 contamination signal"，这在 QLoRA SFT 下确实成立。但 benchmark contamination 在现实中有多种途径：(a) **Pre-training data inclusion**——benchmark items 出现在 pre-training corpus 中，模型通过海量 gradient updates 记忆了 exact question-answer mappings，但不一定产生 SFT 式的泛化效应；(b) **Few-shot memorization**——模型在 ICL 阶段被 fed 大量 benchmark examples；(c) **Data augmentation**——benchmark items 被 paraphrased 后加入 training data。这些不同机制产生的 response pattern aberrance 可能非常不同——特别是 pre-training memorization 可能产生 classic IRT 意义上的 "aberrant pattern"（答对不应该答对的 hard items），因为 memorization 不依赖于理解。
  - 论文的 SFT 泛化论证（Section 5.1："SFT on benchmark items simultaneously teaches (1) specific item answers and (2) general domain knowledge"）对 pre-training contamination 不适用，因为 pre-training 的 learning dynamics 完全不同。
- 为什么是 Major：论文声称揭示了 "binary response bottleneck"，但只在一种特定污染机制下验证。如果 lz* 在 pre-training contamination 下实际能检测到 aberrance（因为 pre-training memorization 不附带泛化效应），那么 bottleneck claim 仅在 SFT 条件下成立，论文标题和 abstract 需要根本性修改。
- 建议修改方向：(1) 至少测试一种替代污染机制（如 continued pre-training on benchmark items，模拟 pre-training data leakage）；(2) 如果无法增加实验，至少在 Discussion 中显式限定 scope："our findings apply to SFT-based contamination; pre-training memorization may produce different response patterns that are more amenable to person-fit detection"；(3) 讨论不同污染机制对 response pattern 的预期影响。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Simulation-Reality Gap 的解释是定性的，缺乏定量模型 [idea 层面]
- 具体位置：Section 5.1, "The simulation-reality gap arises because simulation assumes contamination affects only contaminated items, while real SFT produces generalized improvement"
- 问题：论文指出 simulation power = 97.9% 而 real AUROC = 0.61 at 15% on MMLU，gap 约 37pp。解释是 "SFT generalization"——这是定性的。缺少的是：SFT 泛化效应的量化模型。例如：(1) 在被污染 items 上，多少比例的 accuracy gain 来自 memorization vs. generalization？(2) 如果将泛化效应参数化地加入 simulation（如 "contamination 使 p% items 直接答对，同时使 θ 提升 δ"），能否定量预测 real AUROC？这种定量分析会大大加强 "why" 的解释力。
- 建议：构建一个 "SFT-aware simulation"，在标准 simulation 中加入 θ-shift 参数建模泛化效应，验证修正后的 simulation 能否更准确地预测 real detection power。

**W2** [warning] Leaderboard Audit 的 response pattern typology 缺乏 ground-truth 验证 [idea 层面]
- 具体位置：Section 4.6, Table 11 (K-means k=4 clustering)
- 问题：Table 11 的 4 类 typology 基于 K-means clustering（θ, lz* 二维空间），其中 "Extreme over-consistent" cluster（569 models）被标注为 "possible contamination OR genuine domain expertise"。这个 "OR" 正是问题所在——without ground truth，这个 typology 没有实际诊断价值。论文自己在 Section 4.6 也承认 "it equally contains models with genuine domain expertise. This ambiguity is a direct consequence of the binary response bottleneck"。既然论文已经证明 binary data 无法区分 contamination 和 genuine ability，那么基于 binary data 的 clustering 也同样无法区分——这使得 typology 成为循环论证。
- 建议：(1) 明确标注 typology 的 contribution 是 descriptive 而非 diagnostic；(2) 讨论 typology 的 external validity（是否与模型的 training data 来源、release date 等外部变量相关）。

**W3** [warning] Type-I Error 偏高（0.08 vs. nominal 0.05）未充分讨论 [idea 层面]
- 具体位置：Section 4.5, Table 8 "IRT-FIT Type-I (α=0.05): 0.08"
- 问题：IRT-FIT 在 clean models 上的 false alarm rate 为 0.08，高于 nominal α=0.05。这意味着即使在 detection power 不足的情况下，method 还倾向于 over-flag。论文提到 "universal model misfit leads to inflated false alarms" 但未深入分析。在控制实验中，clean SFT models（0% contamination）本身的 lz* 就极端（Table 2: lz* = -18.4），这暗示 clean SFT baseline 已经 misfit——那么用 clean SFT 作为 baseline 计算 Δlz* 时，null distribution 可能不是 well-calibrated 的。
- 建议：(1) 报告 empirical null distribution 的 QQ plot 或 Kolmogorov-Smirnov test；(2) 讨论 Type-I inflation 的来源（是 null distribution miscalibration 还是 universal misfit 的直接后果）。

**W4** [warning] Power function 理论验证成功但与核心 narrative 矛盾 [idea 层面]
- 具体位置：Table 1, "Theoretical predictions closely match simulation power (R² = 0.963)"
- 问题：论文在 Section 4.1 展示 power function 理论与 simulation 高度吻合，√n scaling law 成立。但论文的核心 narrative 是 "simulation 预测与 reality 严重不符"——那么验证 simulation 内部一致性的价值是什么？在读者看来，花篇幅验证一个 "与 reality 无关" 的理论模型削弱了 negative result 的叙事力度。Table 1 的 "Predicted Real AUROC" 列（0.55-0.61）是论文的 key insight，但这些数字似乎是 post-hoc 填入的——如果 power theory 本身无法预测 real AUROC，那它的 practical 价值需要重新讨论。
- 建议：(1) 明确说明 power function 的价值在于 "proving the simulation is internally correct, thereby isolating the SFT generalization gap as the sole source of detection failure"；(2) 移除或缩短 Table 1 中 simulation 相关内容，将重心放在 simulation-reality gap 的定量分析上。

## 小问题（不影响接收）[presentation 层面]
- Table 12（Section 4.7, Domain-Level Analysis）只展示 2 行数据（15% 和 50%），信息密度低，可与前面的 controlled experiment tables 合并
- Section 4.8（Multiscale lzm）仅用约 3 句话提及，过于简略——如果 lzm 的 AUROC 提升仅 2pp 且不显著，建议明确报告数字（当前只在 review_context.yaml 中有，论文正文似乎只提了 "AUROC improves by only 2 percentage points"），或直接移至 appendix
- Section 5.2 "Universal Model Misfit as an Independent Finding" 的叙事角度好（将 negative detection result 转化为 positive finding about LLM characteristics），但 "temporal trends" 的讨论过于简短——monthly lz* trend 的 slope (-0.38/month) 与 accuracy trend slope (+0.0042/month) 之间的关系值得量化讨论
- References 仅 11 篇，对一篇涉及 IRT、contamination detection、person-fit statistics 三个领域交叉的论文来说偏少——缺少对 Drasgow & Levine (1986)、Karabatsos (2003) 等经典 person-fit 文献的引用

## 主要优势
- **SFT 泛化效应的识别和解释**（Section 5.1）是论文最有价值的 insight：SFT on benchmark items 同时教授 specific item answers 和 general domain knowledge，后者产生 "uniformly improved" response patterns（而非 aberrant patterns），使得 person-fit 无法区分 contamination 和 genuine ability gain。这个机制解释清晰、直觉强，且有控制实验支撑（Table 2 的 Δlz* 方向甚至与 simulation 预测相反）。
- **Detection frontier taxonomy**（Section 3.2, Table 8）将检测方法按 information access level 组织是有用的概念框架，使得 IRT-FIT 的定位（binary-only endpoint）清晰可见。Table 8 的 AUROC gap（30pp+）直观地量化了 information level 的代价。
- **实验覆盖完整**：review_context.yaml 中列出的全部 9 个实验均在论文中有对应呈现（覆盖度 9/9 = 100%）。每个实验都服务于 narrative 的某个环节，无冗余。
- **诚实的 negative result 呈现**：Table 2 的 pilot 数据（Cohen's d = 0.22, p = 0.38）和 Table 3 的 full controlled 数据直面失败，没有 cherry-pick 或 spin。Post-RL 实验（Table 7, signal retention ≈ 0%）进一步加强了 negative result 的可信度。
- **Universal model misfit 的大规模确认**（Table 10, 96-99% flagging rate on 5,847 models）在规模上无先例，即使作为 descriptive finding 也有独立价值。

## 实验覆盖度评估（对照 review_context.yaml）
1. ✅ exp-ctrl-contam-pilot → Section 4.2 Pilot, Table 2
2. ✅ exp-ctrl-contam → Section 4.2 Full, Tables 3-5
3. ✅ exp-leaderboard-audit → Section 4.6, Tables 10-11
4. ✅ exp-4pl-ablation → Section 4.3, Table 6
5. ✅ exp-baseline-comparison → Section 4.5, Tables 8-9
6. ✅ exp-multiscale-lzm → Section 4.8（简要提及）
7. ✅ exp-post-rl → Section 4.4, Table 7
8. ✅ exp-extra-benchmarks → Section 4.1, Table 1
9. ✅ exp-domain-analysis → Section 4.7, Table 12

覆盖度 9/9 = 100%。

## 评分校准说明
2 个 Major issues (N1: overclaimed information-theoretic bound + N2: 单一污染机制) → 评分上限 3.5。
- N1 直接影响论文的核心叙事框架——从 "fundamental impossibility" 到 "method-specific failure" 是质的降级
- N2 限制了 negative result 的 generalization scope——如果 bottleneck 仅在 SFT 条件下成立，论文的社区警示价值（"warning to the community"）大打折扣
- 作为 negative result paper，novelty/excitement 本身有限（IRT 模型不适合 LLM 的直觉并非完全意外）
- 实验执行质量高、诚实呈现，但无法弥补核心 claim 的逻辑缺陷

最终评分 2.5（Borderline Findings）。如果将 claim 严格限定为 "IRT person-fit under SFT conditions" 并增加替代 binary-only 方法或替代污染机制的实验，可提升至 3.0-3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-20T11:42:04.603021+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "text": "## 紧急交叉分享：R1 重新评估，评分下调至 2.5，与你的 3.0 存在分歧\n\nR1 对论文做了根本性的重新解读，请仔细阅读并逐条回应。\n\n**核心分歧**：R1 认为论文实际上是一个 **negative result paper**——IRT person-fit 在 SFT 泛化效应下无法有效检测 contamination（AUROC 仅 0.61-0.78），论文的核心 framing 是揭示 \"binary response information bottleneck\"。但论文将此 overclaim 为 \"information-theoretic lower bound for ALL binary-only methods\"，R1 认为这是不合理的逻辑跳跃。\n\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n### R1 的新 Critical Issues\n\n**N1 [critical] \"Information-Theoretic Lower Bound\" 是 Overclaim**\n- 论文标题限定在 \"IRT Person-Fit Statistics\"（特定方法），但 Abstract 和正文多处将结论泛化为**所有 binary-only 方法的 fundamental impossibility**\n- 论文实际只证明了 lz*（一种特定 summary statistic）在 SFT 泛化条件下失效\n- 反例可能性：binary response vector 包含 lz* 未捕获的 higher-order patterns——ML-based classifier on binary vectors 可能提取更丰富的信号\n- 论文未测试任何 alternative binary-only 方法来验证 \"hard floor\" claim\n- **如果 \"information-theoretic lower bound\" 不成立，论文叙事从 \"fundamental impossibility\" 降级为 \"IRT person-fit 不适合此问题\"，novelty 大幅降低**\n\n**N2 [critical] 单一污染机制不足以支撑 \"fundamental bottleneck\"**\n- 所有控制实验仅用 QLoRA SFT 注入污染\n- Pre-training data inclusion 产生的 response pattern 可能与 SFT 非常不同——pre-training memorization 不附带泛化效应，可能产生 classic IRT 的 \"aberrant pattern\"\n- 如果 lz* 在 pre-training contamination 下实际能检测 aberrance，则 bottleneck claim 仅在 SFT 条件下成立，标题和 abstract 需要根本性修改\n\n### R1 的新 Warning Issues\n- W1: Simulation-reality gap 的解释是定性的，缺乏定量模型\n- W2: Leaderboard audit 的 response pattern typology 缺乏 ground-truth 验证（K-means clustering 的 \"contamination OR genuine expertise\" 分类是循环论证）\n- W3: Type-I Error 偏高（0.08 vs nominal 0.05）未充分讨论\n- W4: Power function 理论验证成功但与核心 negative result narrative 矛盾（花篇幅验证 \"与 reality 无关\" 的理论模型）\n\n### R1 的关键数据点（与你此前理解可能不同）\n- 实际 AUROC at 15% MMLU: **0.61**（非摘要中的 0.96）\n- Post-RL signal retention: **≈0%**\n- Clean SFT baseline lz*: **-18.4**（本身就极端 misfit）\n- Leaderboard flagging rate: **96-99%** on 5,847 models（非 12%）\n\n---\n\n### 需要你回应的关键问题\n\n1. **你是否同意 R1 对论文的重新解读？**——即论文本质上是 negative result paper，而非你此前评估的 positive result paper？\n2. **你是否同意将评分从 3.0 下调至 2.5？** R1 的理由是：(a) overclaimed bound 是核心 claim 的逻辑缺陷，(b) 单一污染机制限制了 negative result 的泛化 scope，(c) 作为 negative result paper 的 novelty/excitement 有限\n3. **你的 systematic positive bias（mean lz*=12.5）与 R1 发现的 \"clean SFT baseline lz*=-18.4\" 之间是什么关系？** 这是否是同一个问题的不同表现？\n4. **R1 的 N1（alternative binary-only methods 未测试）是否改变了你对论文贡献的评估？** 如果简单的 ML classifier on binary vectors 可能有效，lz* 的失败就不是 \"binary limitation\" 而是 \"method limitation\"\n\n请逐条 [AGREE] 或 [REBUT]，并给出你的最终评分。",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "text": "## 紧急交叉分享：R1 重新评估，评分下调至 2.5，与你的 3.0 存在分歧\n\nR1 对论文做了根本性的重新解读，请仔细阅读并逐条回应。\n\n**核心分歧**：R1 认为论文实际上是一个 **negative result paper**——IRT person-fit 在 SFT 泛化效应下无法有效检测 contamination（AUROC 仅 0.61-0.78），论文的核心 framing 是揭示 \"binary response information bottleneck\"。但论文将此 overclaim 为 \"information-theoretic lower bound for ALL binary-only methods\"，R1 认为这是不合理的逻辑跳跃。\n\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n### R1 的新 Critical Issues\n\n**N1 [critical] \"Information-Theoretic Lower Bound\" 是 Overclaim**\n- 论文标题限定在 \"IRT Person-Fit Statistics\"（特定方法），但 Abstract 和正文多处将结论泛化为**所有 binary-only 方法的 fundamental impossibility**\n- 论文实际只证明了 lz*（一种特定 summary statistic）在 SFT 泛化条件下失效\n- 反例可能性：binary response vector 包含 lz* 未捕获的 higher-order patterns——ML-based classifier on binary vectors 可能提取更丰富的信号\n- 论文未测试任何 alternative binary-only 方法来验证 \"hard floor\" claim\n- **如果 \"information-theoretic lower bound\" 不成立，论文叙事从 \"fundamental impossibility\" 降级为 \"IRT person-fit 不适合此问题\"，novelty 大幅降低**\n\n**N2 [critical] 单一污染机制不足以支撑 \"fundamental bottleneck\"**\n- 所有控制实验仅用 QLoRA SFT 注入污染\n- Pre-training data inclusion 产生的 response pattern 可能与 SFT 非常不同——pre-training memorization 不附带泛化效应，可能产生 classic IRT 的 \"aberrant pattern\"\n- 如果 lz* 在 pre-training contamination 下实际能检测 aberrance，则 bottleneck claim 仅在 SFT 条件下成立，标题和 abstract 需要根本性修改\n\n### R1 的新 Warning Issues\n- W1: Simulation-reality gap 的解释是定性的，缺乏定量模型\n- W2: Leaderboard audit 的 response pattern typology 缺乏 ground-truth 验证（K-means clustering 的 \"contamination OR genuine expertise\" 分类是循环论证）\n- W3: Type-I Error 偏高（0.08 vs nominal 0.05）未充分讨论\n- W4: Power function 理论验证成功但与核心 negative result narrative 矛盾（花篇幅验证 \"与 reality 无关\" 的理论模型）\n\n### R1 的关键数据点（与你此前理解可能不同）\n- 实际 AUROC at 15% MMLU: **0.61**（非摘要中的 0.96）\n- Post-RL signal retention: **≈0%**\n- Clean SFT baseline lz*: **-18.4**（本身就极端 misfit）\n- Leaderboard flagging rate: **96-99%** on 5,847 models（非 12%）\n\n---\n\n### 需要你回应的关键问题\n\n1. **你是否同意 R1 对论文的重新解读？**——即论文本质上是 negative result paper，而非你此前评估的 positive result paper？\n2. **你是否同意将评分从 3.0 下调至 2.5？** R1 的理由是：(a) overclaimed bound 是核心 claim 的逻辑缺陷，(b) 单一污染机制限制了 negative result 的泛化 scope，(c) 作为 negative result paper 的 novelty/excitement 有限\n3. **你的 systematic positive bias（mean lz*=12.5）与 R1 发现的 \"clean SFT baseline lz*=-18.4\" 之间是什么关系？** 这是否是同一个问题的不同表现？\n4. **R1 的 N1（alternative binary-only methods 未测试）是否改变了你对论文贡献的评估？** 如果简单的 ML classifier on binary vectors 可能有效，lz* 的失败就不是 \"binary limitation\" 而是 \"method limitation\"\n\n请逐条 [AGREE] 或 [REBUT]，并给出你的最终评分。",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-20T11:42:11.000833+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 6397
}
```

</details>

---


### Assistant

_source line 101 · 2026-05-20T11:42:14.697410+00:00_

交叉分享已发送给 R2。等待 R2 对 R1 新发现的回应，特别是评分分歧（R1: 2.5 vs R2: 3.0）和论文 framing 的根本性分歧。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 11

## Round 11

2 recorded events


### User

_source line 102 · 2026-05-20T11:42:15.850120+00:00_

[Reviewer 1 审稿结果]:
两篇 Dream 论文审稿完成：

- **Median 档** (IRT-FIT: Characterizing the Detection Frontier): **3.0 / 5** (Findings)。Power function 理论贡献扎实，但 leaderboard audit 的 Δlz* baseline 有 chicken-and-egg 问题，且 post-RL 盲区与 audit scope 矛盾。
- **Worst 档** (The Binary Response Bottleneck): **2.5 / 5** (Borderline Findings)。SFT 泛化效应的识别有价值，但 "information-theoretic lower bound" claim 缺乏形式化证明（仅测试 lz* 一种统计量），且单一污染机制限制了结论泛化性。

---

[Reviewer 1 审稿意见]:
## 交叉回应：R2 的关键发现

### ⚠️ Systematic Positive Bias

[REBUT] R2-Showstopper: Systematic positive bias 不构成独立的 showstopper，但我同意它暴露了 IRT 模型拟合问题。

理由与证据：

1. **论文已通过 Δlz* 设计性地应对了 absolute bias 问题。** Section 4.2 明确指出所有 LLM 产生极端 lz*（universal model misfit），因此采用 Δlz*（within-model shift）而非 absolute lz* 作为检测统计量。如果 systematic bias 在 clean 和 contaminated 条件下是常数（即 bias 来自 model-benchmark interaction 而非 contamination），Δlz* 会将其消除。控制实验（Tables 2-4）中 Δlz* 在 clean baseline 之间的差异很小（seed variance），说明 bias 确实被大幅消除。

2. **AUROC 0.78 at 15% MMLU 是在 bias 存在的条件下取得的。** 如果 systematic bias 是 showstopper（即完全摧毁方法的有效性），那么 AUROC 应该接近 0.5（chance）。但控制实验显示在大 benchmark + 中高污染条件下 Δlz* 仍有可量化的区分力——这说明 bias 没有彻底消除信号。

3. **但 R2 的深层担忧是合理的。** Systematic bias 意味着 lz* 的理论 null distribution（N(0,1)）不适用于 LLM。论文使用 bootstrap null 而非理论 null 来设定阈值——R2 应检查论文是否明确了这一点。如果论文仍然假设理论 null，那 FPR 确实会失控。这与我的 **W3**（leaderboard audit 缺乏多重检验校正）相关但不完全相同。

4. **我的 N1（leaderboard audit 的 Δlz* baseline chicken-and-egg）和 N2（post-RL scope gap）本质上覆盖了 bias 问题的 downstream 影响。** Systematic bias 使得 absolute lz* 无区分力（论文承认），而 Δlz* 的 baseline 选择（per-family median）又引入了新的 bias 来源——这正是我的 N1。所以 R2 的 bias 问题和我的 N1 是同一根问题链的上下游。

**结论：** Systematic positive bias 是一个 significant concern（值得 Should-Fix），但不是独立于 Δlz* 设计之外的 showstopper。真正的 showstopper 是 Δlz* 的 baseline 是否可靠（我的 N1），而非 absolute lz* 的 bias。R2 如果能展示 Δlz* 本身也有 systematic bias（即 clean-vs-clean Δlz* 均值 ≠ 0），那这个判断需要修改。

---

### R2 的 Major Issues

[AGREE] R2-Incomplete-Tables: 数据缺失削弱可信度

同意 R2 的关注。Table 中的数据空缺（Gemma-4-31B 缺少 10%/25% 数据、lzm 只展示 5/12 models、two-sided results 只展示 5/60 pairs）在 Dream review 框架下属于 **presentation 层面**问题（Dream 审稿指导明确将"论文完整度"归为 presentation），但确实削弱了审稿人的信任——选择性报告是顶会审稿的常见 red flag。我的审稿中仅在"小问题"中提及 Table 5 的 "*" 标注问题，R2 扩大了范围，这个判断更全面。不过，在 Dream 审稿边界下，我倾向于将其定为 Should-Fix 而非 Major——因为缺失数据可能是 Dream 模拟 paper 的生成限制而非作者选择性报告。

---

[REBUT] R2-Two-Model-Families: 论文实际包含 4 个模型，R2 可能遗漏了

Section 5.2 和 review_context.yaml 均明确记录了 **4 个模型**（Qwen3.5-9B, Mistral-7B-v0.3, Llama-3.1-8B, Gemma-4-31B），Table 4（Per-Model Cohen's d at 15% MMLU）展示了全部 4 个模型的结果。R2 称 "仅 Qwen3.5-9B 和 Gemma-4-31B" 与论文内容不符。

但 R2 的深层关注——**缺乏 MoE 架构、更大规模（70B+）、和不同训练范式（base/chat/reasoning）的验证**——我部分同意。4 个模型全部是 dense 架构、7B-31B 参数量范围、SFT 训练。不过：
- 4 个模型已覆盖了 3 个不同 model family（Qwen, Llama, Mistral/Gemma），inter-model variation 有定量报告（Table 4, d 从 0.62 到 1.35）
- 要求 MoE + 70B+ 的实验对一篇 8-page paper 来说是过高标准
- 论文的核心 claim 是 "detection frontier characterization"，不是 "universal detection tool"——scope 限定已在 narrative guidance 中明确

我建议将此从 Major 降级为 Should-Fix。

---

[AGREE] R2-Missing-Simple-Baselines: 缺少简单 binary-only baselines 是合理关注

论文与 ConStat 和 Min-K%++ 的对比是跨 information level 的（binary vs re-test vs log-probs），但缺少 **同一 information level** 内的对比。例如：
- **Accuracy z-score**：最简单的 binary-only 异常检测——某模型在某 benchmark 上的 accuracy 是否偏离 family 均值。如果 accuracy z-score 的 detection power 与 Δlz* 相当，那么整个 IRT 框架的附加价值就需要质疑
- **Binary response vector 上的 ML classifier**：如果 random forest/logistic regression on binary vectors 能达到更高 AUROC，就否定了 "binary-only 方法都不行" 的叙事（这与我的 worst 档 N1 overclaim 担忧相关，但在 median 档论文中 claim 更 modest）

这对论文的贡献定位很重要：IRT person-fit 的价值是否在于其 detection power，还是在于其 psychometric 可解释性？如果是后者，论文应更明确地 argue 这一点。

---

### R2 的评分

R2 给出 3.0（Findings），与我一致。我认为这个评分校准是合理的——论文有 genuine contributions（power function theory, detection frontier framing, scalability advantage），但方法论问题（我的 N1/N2 + R2 的 bias/completeness concerns）阻止了 Conference 级别。

---

### 综合判断

R2 和我的审稿在核心评价上高度一致（3.0/5），但侧重不同：
- **我侧重 downstream**：N1（leaderboard audit baseline 可靠性）和 N2（post-RL scope gap）是 Δlz* 在实际应用中的问题
- **R2 侧重 upstream**：systematic bias 和 model coverage 是方法论前提层面的问题

两者互补。如果将我的 N1/N2 + R2 的 bias concern 整合，论文面临的核心挑战是一个完整链条：**IRT 模型对 LLM 拟合不良 → absolute lz* 无区分力 → Δlz* 依赖 baseline 选择 → baseline 在 leaderboard audit 中不可靠 + 对 post-RL 模型 blind**。论文在这个链条的中段（Δlz* detection frontier）做了有价值的工作，但链条两端（上游拟合前提 + 下游应用可靠性）都存在未解决的问题。

---

[Reviewer 1 审稿结果]:
两篇 Dream 论文的审稿和 R2 交叉回应均已提交完毕：

- **Median 档**（IRT-FIT: Characterizing the Detection Frontier）：Overall 3.0，2 个 Major issues（leaderboard audit baseline chicken-and-egg + post-RL scope gap）
- **Worst 档**（The Binary Response Bottleneck）：Overall 2.5，2 个 Major issues（overclaimed information-theoretic bound + 单一污染机制）
- **R2 交叉回应**：REBUT systematic bias 作为 showstopper（Δlz* 设计已部分应对）；REBUT two-model-families（论文实际有 4 个模型）；AGREE incomplete tables 和 missing simple baselines

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 103 · 2026-05-20T11:43:23.525806+00:00_

R1 完成了交叉回应，并澄清了重要背景：**R1 审阅了两个 Dream 版本**（Median 3.0 / Worst 2.5），而非单一论文。

R1 交叉回应要点：

| R2 的发现 | R1 判断 | 理由 |
|-----------|---------|------|
| Systematic positive bias = showstopper | **REBUT** | 论文用 Δlz*（非 absolute lz*）已设计性地消除 bias；AUROC 0.78 证明信号未被完全摧毁。但同意是 Should-Fix |
| 仅两个 model family | **REBUT** | 论文实际有 4 个模型（Qwen, Mistral, Llama, Gemma），R2 遗漏了 |
| Incomplete tables | **AGREE** | 但建议降级为 Should-Fix |
| Missing simple baselines | **AGREE** | 特别是同 information-level 的 binary-only 对比（accuracy z-score 等） |

R1 的整合判断：R2 的 systematic bias 关切和 R1 的 N1（baseline chicken-and-egg）是**同一问题链的上下游**——IRT 拟合不良 → absolute lz* 无效 → Δlz* 依赖 baseline → baseline 在 audit 中不可靠。

当前等待 R2 对 R1 最新交叉分享的回应，特别是：
1. 是否接受 systematic bias 从 showstopper 降级
2. 是否接受 4 个模型的纠正
3. 对 Worst 档论文的评估

R2 响应到达后即合成更新报告并 force resubmit。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 12

## Round 12

6 recorded events


### User

_source line 104 · 2026-05-20T11:44:34.140298+00:00_

[Reviewer 2 审稿意见]:
## R2 对 R1 重新评估的逐条交叉回应

---

### 对 R1 新 Critical Issues 的回应

**[AGREE] R1-N1: "Information-Theoretic Lower Bound" 是 Overclaim**

R1 这一点切中了论文最根本的逻辑缺陷，我在首轮审稿中未充分识别。

核心问题是一个 **scope 跳跃**：论文标题和方法部分限定在 "IRT Person-Fit Statistics"（一种特定的 summary statistic），但结论部分和 Abstract 将 lz* 的失败泛化为"所有 binary-only 方法的 fundamental impossibility"。这是不成立的推理：

- lz* 本质上是一个**加权标量**——它将整个 response vector 压缩为一个数字，丢弃了 item-item 之间的高阶交互信息
- Binary response vector 本身是一个高维对象（维度 = item 数量），其中包含 lz* 未利用的丰富结构：item 间的条件依赖、response subsequence patterns、ability-inconsistent cluster 等
- 一个直接的反例：训练一个 binary classifier（输入：binary response vector；标签：contaminated/clean），使用 neural network 或 gradient boosting，完全可能捕获 lz* 丢失的信号
- 论文**未测试任何 alternative binary-only method**，却声称 binary information 本身不够——这是 affirming the consequent

R1 说得对：如果这个 "impossibility" claim 不成立，论文叙事从 "fundamental limitation of binary information" 降级为 "lz* 不适合检测 LLM contamination"，后者的 novelty 和 impact 显著降低。

**[AGREE] R1-N2: 单一污染机制不足以支撑 "fundamental bottleneck"**

同意，且 R1 关于 pre-training contamination 的补充分析比我此前的回应更深入。关键洞察：

- QLoRA SFT 注入污染 → SFT 泛化效应 → response pattern 变得"正常化" → lz* 检测失败
- 但 pre-training memorization 是一种本质不同的机制：模型可能精确记住了特定 item 的答案而未泛化到相关能力，这恰恰是 classic IRT person-fit 设计检测的 "aberrant pattern"
- 如果 lz* 在 pre-training contamination 下实际有效，那么 "bottleneck" 仅是 SFT-specific 的，论文的核心 claim 需要根本性限定

这与 N1 构成双重打击：方法范围 overclaimed + 污染机制单一 → "fundamental" 一词在任何方向都站不住。

---

### 对 R1 新 Warning Issues 的回应

**[AGREE] R1-W1: Simulation-reality gap 缺乏定量模型**
同意。定性解释（"SFT 泛化效应"）不够——如果能建立一个简单的 formal model 量化泛化程度对 detection power 的影响，论文的理论贡献会更扎实。

**[AGREE] R1-W2: K-means clustering 的循环论证**
这个点我此前未注意到。如果 cluster 标签来自 lz* 本身（或其衍生特征），然后用 cluster 结果解释 lz* patterns，这确实是循环论证。没有 ground-truth contamination labels 的 leaderboard models，任何 unsupervised clustering 都只能说"这些模型的 response patterns 不同"，不能说"这是因为 contamination"。

**[AGREE] R1-W3: Type-I Error 0.08 vs 0.05**
同意。60% 的 FPR 膨胀（0.08/0.05 = 1.6）在统计方法论论文中需要认真对待。结合我此前指出的 systematic positive bias，这进一步说明 lz* 在 LLM 场景下的 null distribution 校准失败。

**[AGREE] R1-W4: Power function 验证 vs negative result 的叙事矛盾**
R1 的观察很敏锐：论文花大量篇幅验证 power function（R²=0.96）在 simulation 中成立，但核心结论是"方法在现实中不行"——那么精确验证一个"在现实中无关"的理论模型，这部分篇幅的投入产出比成问题。不过我认为 power function 框架本身有独立的方法论价值（见下文评分讨论）。

---

### 对 Director 四个关键问题的回应

**Q1: 论文本质上是 negative result paper？**

**部分同意**。R1 的重新解读有实质性的洞察——从关键数据点看（AUROC 0.61 @ 15%, post-RL ≈ 0%, flagging rate 96-99%），IRT person-fit 在 realistic conditions 下确实基本不 work，论文的主要实证发现确实是 negative 的。

但我认为论文不是纯粹的 negative result paper，而是一个**混合体**：
- **Negative result**：lz* 在 SFT 泛化和 post-RL 条件下检测失败 ✓
- **Positive methodological contribution**：power function 框架和 detection frontier 概念，作为分析工具，可以应用于评估其他 contamination detection 方法 ✓
- **问题在于 framing**：论文将 negative result overclaim 为 fundamental impossibility，同时在 Abstract 中选择性报告最优条件下的 AUROC（0.92/0.96），制造了 positive result 的表象

如果论文诚实地 reframe 为 "IRT person-fit 在 LLM contamination detection 上的局限性分析"，并将 power function 作为独立贡献，叙事会更连贯。

**Q2: 是否下调至 2.5？**

**不同意下调至 2.5，维持 3.0，但承认是 soft 3.0（lower end of Findings）。** 理由：

R1 和我的分歧本质上是对**概念贡献 vs 实证缺陷**的权重分配不同：
- R1 更关注：overclaim 使核心叙事不可信 → novelty 大幅缩水 → 2.5
- 我更关注：即使实证不完善，以下概念贡献对社区仍有价值 → 3.0
  - (a) Power function 框架提供了评估任意 contamination detection 方法 detection power 的理论工具
  - (b) Detection frontier 概念是一个有用的 vocabulary，后续工作可以在此基础上比较不同方法
  - (c) 对 SFT 泛化效应的系统性刻画（即使 scope 限于 SFT）对 benchmark integrity 社区有参考价值
  - (d) "IRT person-fit 不适合 LLM" 这个负面结果本身避免了其他研究者重复探索这条路

2.5 = "Borderline Findings" 意味着即使修改也可能不够。我认为如果作者能 (1) 修正 overclaim 为 method-specific limitation，(2) 补充至少一个 alternative binary-only baseline，(3) 完整呈现所有条件下的 AUROC 而非选择性报告，论文可以达到 solid Findings 水平。这意味着当前版本是 Findings 的 lower end（3.0），而非 borderline（2.5）。

**Q3: Systematic positive bias (mean lz*=12.5) 与 clean SFT baseline lz*=-18.4 的关系**

这两个数字看似矛盾但来自**不同的 population**，反映的是**同一根本问题的两面**：

- **mean lz*=12.5**：来自 leaderboard audit（数千个异质模型），正向偏移 → 大多数模型的 response pattern 对 IRT 模型来说"过于异常"
- **clean SFT baseline lz*=-18.4**：来自 controlled experiment（特定 clean SFT 模型），负向偏移 → 这些模型的 response pattern 对 IRT 模型来说"过于规律/可预测"

两个方向的极端偏移共同说明：**IRT 模型对 LLM response pattern 的拟合从根本上失败了**。无论是 "too aberrant"（+12.5）还是 "too predictable"（-18.4），lz* 的理论 null distribution（均值 0，方差 1）完全不适用于 LLM population。这不是 calibration 微调能解决的问题——是测量框架与被测对象的根本性不匹配。

这实际上**加强了 R1 的 negative result 解读**：lz* 不仅在 contamination detection 上失效，其作为 LLM person-fit 指标的基本前提就不成立。

**Q4: Alternative binary-only methods 是否改变贡献评估？**

**是的，这显著改变了评估。** 这是 R1 最有说服力的新论点。

如果一个简单的 binary classifier（例如在 binary response vectors 上训练的 logistic regression 或 random forest）能达到 AUROC > 0.80，那么：
- lz* 的失败就不是 "binary information is insufficient"，而是 "lz* is a poor choice of statistic for this task"
- 论文的核心贡献从 "fundamental impossibility result" 缩减为 "IRT person-fit 不适合 LLM contamination detection"
- 后者仍有一定价值（避免社区重复探索），但 novelty 和 impact 确实如 R1 所说大幅降低

不过，我仍认为**即使 alternative methods 更有效，power function 和 detection frontier 框架的方法论价值不变**——这些分析工具可以同样应用于评估那些 alternative methods 的 detection power。

---

### R2 最终评分

**维持 Overall 3.0 (Findings)**，但承认这是一个 contested 3.0。

与 R1 的半分之差归结为一个判断：overclaimed impossibility result 修正为 method-specific limitation 后，power function + detection frontier + SFT generalization analysis 的概念贡献包是否足以独立支撑 Findings 接收？我认为是的，R1 认为不够。这是合理的分歧，请 Director 裁定。

如果 Director 认为需要统一评分，我可以接受 2.5-3.0 之间的任何位置，不会坚持。核心评判标准是：**作为一篇需要 reframing 的 negative result paper，其方法论框架贡献是否达到 Findings 门槛？**

R2 交叉回应完毕。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-20T11:47:37.195937+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "## Dream Review Round 1 — Issue Tracker\n## Median 档 (IRT-FIT: Characterizing the Detection Frontier) + Worst 档 (The Binary Response Bottleneck)\n\n- id: \"R1-N1-median\"\n  summary: \"Leaderboard audit 的 Δlz* baseline (per-family median) 存在 chicken-and-egg 问题——若整个 family 被污染则 baseline 有偏\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。R2 指出此问题与 systematic bias 叠加使 audit 定量结论不可信。\"\n  action_items:\n    - round: 1\n      action: \"在控制实验中模拟全 family 污染场景测试 baseline 有效性；尝试替代 baseline（pre-SFT base model lz*、global median）；至少在 limitation 中讨论假设边界\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2-median\"\n  summary: \"Post-RL 信号消失 (AUROC 0.56, retention 19%) 与 leaderboard audit 覆盖 post-RL 模型的范围矛盾——audit 的 false negative rate 不可知\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE with nuance。R2 补充指出 controlled→audit 逻辑链断裂。\"\n  action_items:\n    - round: 1\n      action: \"在 audit 中标注已知 post-RL 模型并分析 Δlz* 分布差异；限定 audit scope 为 SFT-based models；temporal trend 需考虑 RL 采用率作为 confound\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1-worst\"\n  summary: \"Information-theoretic lower bound claim 缺乏形式化证明——仅用 lz* 一种统计量的经验失败推断所有 binary-only 方法的不可能性，属 overclaim\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。两人共识：binary response vector 包含 lz* 未利用的 higher-order patterns，ML classifier 可能更有效。论文未测试任何 alternative binary-only method。\"\n  action_items:\n    - round: 1\n      action: \"将 claim 限定为 IRT person-fit 层面（非 all binary-only methods）；或提供 information-theoretic 形式化证明；或测试 2-3 种 alternative binary-only methods (logistic regression/RF on binary vectors)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2-worst\"\n  summary: \"单一污染机制 (QLoRA SFT) 不足以支撑 fundamental bottleneck 结论——pre-training memorization 可能产生 classic aberrant pattern，lz* 可能有效\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。SFT 泛化效应是 SFT-specific 的，pretraining contamination 的 learning dynamics 完全不同。\"\n  action_items:\n    - round: 1\n      action: \"至少测试一种替代污染机制 (continued pre-training on benchmark items)；或限定 scope 为 SFT-based contamination\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Systematic positive bias (mean lz*≈12.5) / IRT model fundamental misfit for LLM response patterns\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提为 showstopper；R1 REBUT（Δlz* 设计已部分应对），降级为 warning。R2 部分接受但指出 clean lz*=-18.4 与 audit lz*=+12.5 双向极端偏移说明 IRT 框架根本性不匹配。两人共识：是 significant concern 但非独立 showstopper。\"\n  action_items:\n    - round: 1\n      action: \"验证论文是否使用 bootstrap null 而非 theoretical null；展示 empirical null distribution 与 N(0,1) 对比\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3-median\"\n  summary: \"Leaderboard audit 缺乏多重检验校正 (6200×4=24800 次检验, 2σ threshold, 未做 Bonferroni/BH-FDR)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE 并补充：统计方法论论文中不做校正是不可接受的疏忽\"\n  action_items:\n    - round: 1\n      action: \"补充 BH-FDR 校正后的 anomaly 数量和 flagging rates\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"Incomplete tables — 选择性展示部分数据 (Gemma 缺条件, lzm 5/12 models, two-sided 5/60 pairs)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提为 Major，R1 AGREE 但在 Dream 框架下建议降为 Should-Fix\"\n  action_items:\n    - round: 1\n      action: \"补全所有表格数据（完整条件/模型），选择性报告嫌疑需消除\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Missing simple binary-only baselines (accuracy z-score, ML classifier on binary vectors) — 无法判断 IRT 框架的附加价值\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提，R1 AGREE。对 worst 档尤其关键——如 ML classifier 有效则否定 impossibility claim。\"\n  action_items:\n    - round: 1\n      action: \"增加至少 2 种同 information level 的 baseline (accuracy z-score + ML classifier on binary vectors)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2-median\"\n  summary: \"Power function (R²=0.96) 基于 simulation 拟合，给出的是 detection power upper bound 而非 actual power\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"SFT 泛化效应使 ~45% accuracy gain 来自泛化而非记忆，simulation 高估 detection power\"\n  action_items:\n    - round: 1\n      action: \"明确标注 power function 为 upper bound；Table 中增加 controlled AUROC 列作为 out-of-sample validation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4-median\"\n  summary: \"IRT 参数质量 (PSN-IRT 来源) 对结果的影响未讨论——缺乏 sensitivity analysis\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE——与 systematic bias 直接相关\"\n  action_items:\n    - round: 1\n      action: \"进行 IRT 参数 bootstrap sensitivity analysis 或讨论 PSN-IRT 参数在 LLM context 下的适用性\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3-worst\"\n  summary: \"Type-I Error 0.08 vs nominal 0.05 (60% FPR 膨胀)——null distribution 校准失败\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE——与 systematic bias 共同说明 lz* 在 LLM 场景下的 null distribution 不适用\"\n  action_items:\n    - round: 1\n      action: \"报告 empirical null distribution QQ plot / KS test；讨论 Type-I inflation 来源\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2-worst\"\n  summary: \"K-means clustering on (θ, lz*) 的 contamination typology 缺乏 ground-truth——循环论证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。无 ground-truth 的 unsupervised clustering 只能说 patterns 不同，不能归因为 contamination。\"\n  action_items:\n    - round: 1\n      action: \"明确标注 typology 为 descriptive 而非 diagnostic；讨论 external validity\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Model coverage — 4 个模型均为 dense 7B-31B SFT，缺乏 MoE/70B+/reasoning 架构验证\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 首提为 Major，R1 REBUT（论文有 4 个模型非 2 个，8 页论文标准下足够）。降级为 info。\"\n  action_items:\n    - round: 1\n      action: \"如篇幅允许，增加 MoE 或 70B+ 模型的验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-F1\"\n  summary: \"Limitations 应为独立 section（EMNLP 2026 格式要求），当前为 Conclusion 内 paragraph\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"EMNLP 2026 mandatory Limitations section，缺失可能导致 desk rejection\"\n  action_items:\n    - round: 1\n      action: \"将 Limitations 移为独立 section\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "## Dream Review Round 1 — Issue Tracker\n## Median 档 (IRT-FIT: Characterizing the Detection Frontier) + Worst 档 (The Binary Response Bottleneck)\n\n- id: \"R1-N1-median\"\n  summary: \"Leaderboard audit 的 Δlz* baseline (per-family median) 存在 chicken-and-egg 问题——若整个 family 被污染则 baseline 有偏\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。R2 指出此问题与 systematic bias 叠加使 audit 定量结论不可信。\"\n  action_items:\n    - round: 1\n      action: \"在控制实验中模拟全 family 污染场景测试 baseline 有效性；尝试替代 baseline（pre-SFT base model lz*、global median）；至少在 limitation 中讨论假设边界\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2-median\"\n  summary: \"Post-RL 信号消失 (AUROC 0.56, retention 19%) 与 leaderboard audit 覆盖 post-RL 模型的范围矛盾——audit 的 false negative rate 不可知\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE with nuance。R2 补充指出 controlled→audit 逻辑链断裂。\"\n  action_items:\n    - round: 1\n      action: \"在 audit 中标注已知 post-RL 模型并分析 Δlz* 分布差异；限定 audit scope 为 SFT-based models；temporal trend 需考虑 RL 采用率作为 confound\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1-worst\"\n  summary: \"Information-theoretic lower bound claim 缺乏形式化证明——仅用 lz* 一种统计量的经验失败推断所有 binary-only 方法的不可能性，属 overclaim\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。两人共识：binary response vector 包含 lz* 未利用的 higher-order patterns，ML classifier 可能更有效。论文未测试任何 alternative binary-only method。\"\n  action_items:\n    - round: 1\n      action: \"将 claim 限定为 IRT person-fit 层面（非 all binary-only methods）；或提供 information-theoretic 形式化证明；或测试 2-3 种 alternative binary-only methods (logistic regression/RF on binary vectors)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2-worst\"\n  summary: \"单一污染机制 (QLoRA SFT) 不足以支撑 fundamental bottleneck 结论——pre-training memorization 可能产生 classic aberrant pattern，lz* 可能有效\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。SFT 泛化效应是 SFT-specific 的，pretraining contamination 的 learning dynamics 完全不同。\"\n  action_items:\n    - round: 1\n      action: \"至少测试一种替代污染机制 (continued pre-training on benchmark items)；或限定 scope 为 SFT-based contamination\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Systematic positive bias (mean lz*≈12.5) / IRT model fundamental misfit for LLM response patterns\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提为 showstopper；R1 REBUT（Δlz* 设计已部分应对），降级为 warning。R2 部分接受但指出 clean lz*=-18.4 与 audit lz*=+12.5 双向极端偏移说明 IRT 框架根本性不匹配。两人共识：是 significant concern 但非独立 showstopper。\"\n  action_items:\n    - round: 1\n      action: \"验证论文是否使用 bootstrap null 而非 theoretical null；展示 empirical null distribution 与 N(0,1) 对比\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3-median\"\n  summary: \"Leaderboard audit 缺乏多重检验校正 (6200×4=24800 次检验, 2σ threshold, 未做 Bonferroni/BH-FDR)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE 并补充：统计方法论论文中不做校正是不可接受的疏忽\"\n  action_items:\n    - round: 1\n      action: \"补充 BH-FDR 校正后的 anomaly 数量和 flagging rates\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"Incomplete tables — 选择性展示部分数据 (Gemma 缺条件, lzm 5/12 models, two-sided 5/60 pairs)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提为 Major，R1 AGREE 但在 Dream 框架下建议降为 Should-Fix\"\n  action_items:\n    - round: 1\n      action: \"补全所有表格数据（完整条件/模型），选择性报告嫌疑需消除\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Missing simple binary-only baselines (accuracy z-score, ML classifier on binary vectors) — 无法判断 IRT 框架的附加价值\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提，R1 AGREE。对 worst 档尤其关键——如 ML classifier 有效则否定 impossibility claim。\"\n  action_items:\n    - round: 1\n      action: \"增加至少 2 种同 information level 的 baseline (accuracy z-score + ML classifier on binary vectors)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2-median\"\n  summary: \"Power function (R²=0.96) 基于 simulation 拟合，给出的是 detection power upper bound 而非 actual power\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"SFT 泛化效应使 ~45% accuracy gain 来自泛化而非记忆，simulation 高估 detection power\"\n  action_items:\n    - round: 1\n      action: \"明确标注 power function 为 upper bound；Table 中增加 controlled AUROC 列作为 out-of-sample validation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4-median\"\n  summary: \"IRT 参数质量 (PSN-IRT 来源) 对结果的影响未讨论——缺乏 sensitivity analysis\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE——与 systematic bias 直接相关\"\n  action_items:\n    - round: 1\n      action: \"进行 IRT 参数 bootstrap sensitivity analysis 或讨论 PSN-IRT 参数在 LLM context 下的适用性\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3-worst\"\n  summary: \"Type-I Error 0.08 vs nominal 0.05 (60% FPR 膨胀)——null distribution 校准失败\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE——与 systematic bias 共同说明 lz* 在 LLM 场景下的 null distribution 不适用\"\n  action_items:\n    - round: 1\n      action: \"报告 empirical null distribution QQ plot / KS test；讨论 Type-I inflation 来源\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2-worst\"\n  summary: \"K-means clustering on (θ, lz*) 的 contamination typology 缺乏 ground-truth——循环论证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。无 ground-truth 的 unsupervised clustering 只能说 patterns 不同，不能归因为 contamination。\"\n  action_items:\n    - round: 1\n      action: \"明确标注 typology 为 descriptive 而非 diagnostic；讨论 external validity\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Model coverage — 4 个模型均为 dense 7B-31B SFT，缺乏 MoE/70B+/reasoning 架构验证\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 首提为 Major，R1 REBUT（论文有 4 个模型非 2 个，8 页论文标准下足够）。降级为 info。\"\n  action_items:\n    - round: 1\n      action: \"如篇幅允许，增加 MoE 或 70B+ 模型的验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-F1\"\n  summary: \"Limitations 应为独立 section（EMNLP 2026 格式要求），当前为 Conclusion 内 paragraph\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: both\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"EMNLP 2026 mandatory Limitations section，缺失可能导致 desk rejection\"\n  action_items:\n    - round: 1\n      action: \"将 Limitations 移为独立 section\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-20T11:47:37.398307+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 8466}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 107 · 2026-05-20T11:50:23.274200+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告（修正版）：irt_personfit_contam Dream Papers\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit  \n**Round**: 1  \n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)  \n**审稿对象**: Dream Report 的 Median 档和 Worst 档  \n**收敛状态**: 充分交叉讨论，核心共识达成，评分分歧 0.5 分（仅 worst 档）\n\n⚠️ **修正说明**: 本报告替换此前因服务器重启导致的错误提交（原报告误基于 Best 档 paper.tex 撰写）。\n\n---\n\n## 审稿对象概述\n\nDream Report 生成了三个版本的论文，R1 审了 Median 和 Worst 两个档位：\n\n| 档位 | 标题 | 核心 Framing | 实际 AUROC@15% | R1 | R2 |\n|------|------|-------------|----------------|----|----|\n| **Median** | IRT-FIT: Characterizing the Detection Frontier | 混合结果：部分有效的检测工具 + 理论贡献 | 0.78 (MMLU) | 3.0 | 3.0 |\n| **Worst** | The Binary Response Bottleneck | Negative result：揭示 binary-only 检测的根本限制 | 0.61 (MMLU) | 2.5 | 3.0 |\n\n---\n\n## Summary\n\n### Median 档\n论文将 IRT person-fit 统计量（lz*）应用于 LLM benchmark contamination 检测，定位为 \"minimal-information operating point\"（仅需 binary response）。受控实验在 4 个模型（Qwen3.5-9B, Mistral-7B-v0.3, Llama-3.1-8B, Gemma-4-31B）上通过 QLoRA SFT 注入污染，best-case AUROC 0.78 at 15% MMLU。核心理论贡献是 detection power function（R²=0.96），将检测功效与 benchmark size 的关系形式化。大规模 leaderboard audit 扫描 6,200+ 模型。Post-RL 实验显示信号大幅衰减（AUROC 0.56）。\n\n### Worst 档\n同一研究框架，但 framing 为 negative result：IRT person-fit 在 SFT 泛化效应下基本失效（AUROC 0.61），universal model misfit 导致 96-99% 模型被错误标记。论文据此声称揭示了 \"binary-only contamination detection 的 information-theoretic lower bound\"。\n\n---\n\n## Strengths（R1, R2 共识）\n\n**S1. Power Function 理论框架（R1 首推，R2 共识）。** Detection power 与 benchmark size 的解析公式（R²=0.96），inverted-U 拐点可从 item difficulty distribution 预测（误差 ≤0.02），并用 BBH/MATH 进行了 out-of-sample 验证。**即使方法的实际检测力有限，这个理论框架本身具有独立的方法论价值**——可用于评估任意 contamination detection 方法的 detection power。两位 Reviewer 一致认为这是论文最突出的贡献。\n\n**S2. Detection Frontier Framing（R1 首推，R2 共识）。** 将检测方法按 information access level 组织（binary < binary+retest < token probs < training data < weights），清晰定位 IRT-FIT 的角色。这个概念框架为后续工作提供了有用的 vocabulary。\n\n**S3. SFT 泛化效应的系统性刻画（两档共有）。** SFT on benchmark items 同时教授 specific item answers 和 general domain knowledge，后者产生\"正常化\"的 response patterns，使 person-fit 无法区分 contamination 和 genuine ability gain。这一机制解释清晰、有控制实验支撑，对 benchmark integrity 社区有实质参考价值。\n\n**S4. 诚实呈现负面结果。** Post-RL signal loss、GSM8K 低 power、leaderboard audit 高 flagging rate 等负面结果均如实呈现，增强了论文可信度。实验覆盖度 9/9 = 100%（对照 review_context.yaml）。\n\n**S5. 独特的 Scalability 优势。** IRT-FIT 是唯一能用 archival binary data 进行 retrospective audit 的方法，这一 practical advantage 有实际意义。\n\n---\n\n## Weaknesses\n\n### Critical Issues\n\n**W1. [Critical] Leaderboard Audit 的 Δlz* Baseline Chicken-and-Egg 问题（R1 首提，R2 AGREE）** [Median 档]\n- Leaderboard audit 使用 per-family median lz* 作为 \"clean\" baseline 计算 Δlz*\n- 若整个 model family 的 base model training data 已含 benchmark items（对 MMLU 等广泛流传的 benchmark 几乎必然），family median 本身已被污染抬高，Δlz* 系统性低估\n- 直接影响 leaderboard audit 全部定量结论：flagging rates、temporal trends、cross-benchmark anomalies\n- 论文未测试此假设的 sensitivity，未提供替代 baseline 的 robustness check\n\n**W2. [Critical] Post-RL 信号消失与 Leaderboard Audit 适用范围矛盾（R1 首提，R2 AGREE with nuance）** [Median 档]\n- Post-RL AUROC 降至 0.56（retention 仅 19%），论文承认 \"IRT-FIT detects SFT-based contamination but not post-RL contamination\"\n- 但 leaderboard audit 对 6,200+ 模型扫描，必然包含大量 RLHF/DPO/GRPO 模型\n- 低 Δlz* 可能是\"未受污染\"，也可能是\"RL 洗掉了信号\"——方法无法区分\n- R2 补充：controlled experiment → leaderboard audit 的逻辑链条因此断裂\n\n**W3. [Critical] \"Information-Theoretic Lower Bound\" 是 Overclaim（R1 首提，R2 AGREE）** [Worst 档]\n- 论文标题限定在 \"IRT Person-Fit Statistics\"，但 Abstract 和正文泛化为\"所有 binary-only 方法的 fundamental impossibility\"\n- 实际只证明 lz*（一种特定 summary statistic）在 SFT 泛化条件下失效\n- Binary response vector 包含 lz* 未利用的 higher-order patterns：item-item 条件依赖、response subsequence patterns、ability-inconsistent clusters\n- **论文未测试任何 alternative binary-only method**（如 ML classifier on binary vectors），却声称 binary information 本身不够——这是 affirming the consequent\n- 若 \"impossibility\" 不成立，论文叙事从 \"fundamental limitation\" 降级为 \"method-specific failure\"，novelty 显著降低\n\n**W4. [Critical] 单一污染机制不足以支撑 Bottleneck 结论（R1 首提，R2 AGREE）** [Worst 档]\n- 所有控制实验仅用 QLoRA SFT 注入污染\n- Pre-training memorization 的 learning dynamics 完全不同——可能产生 classic aberrant pattern（精确记住答案而未泛化），恰恰是 person-fit 设计检测的信号\n- 若 lz* 在 pre-training contamination 下有效，则 bottleneck 仅是 SFT-specific，论文标题和核心 claim 需根本性修改\n\n### Major/Warning Issues\n\n**W5. [Warning] Systematic Positive Bias / IRT Model Fundamental Misfit（R2 首提，R1 REBUT → 降级为 warning）** [两档共有]\n- 经验数据中 lz* 均值系统性偏离理论期望值 0（leaderboard: +12.5, clean SFT: -18.4），双向极端偏移说明 IRT 对 LLM response pattern 的拟合从根本上失败\n- R1 指出论文通过 Δlz*（within-model shift）设计性地应对了 absolute bias，若 bias 在 clean/contaminated 条件下是常数则被消除\n- **两位 Reviewer 共识**：不构成独立 showstopper（Δlz* 已部分应对），但暴露了 IRT 框架的适用性问题，是 W1 (baseline reliability) 的上游根因\n- 需验证：论文是否使用 bootstrap null 而非 theoretical null？Δlz* 本身是否也有 systematic bias？\n\n**W6. [Warning] 缺乏多重检验校正（R1 首提，R2 AGREE）** [Median 档]\n- 6,200 models × 4 benchmarks = 24,800 次检验，使用 2σ 阈值未做 Bonferroni/BH-FDR 校正\n- 期望 false positive 约 570 个，论文报告 MMLU 185 个 top anomaly 反而低于未校正 expected FP——暗示 Δlz* distribution 可能非正态\n- 统计方法论论文中此疏忽不可接受\n\n**W7. [Warning] Incomplete Tables / 选择性报告嫌疑（R2 首提，R1 AGREE）** [两档共有]\n- Gemma-4-31B 缺少部分污染水平数据、lzm 仅展示 5/12 models、two-sided results 仅展示 5/60 pairs\n- R1 注意到在 Dream 框架下可能是生成限制而非选择性报告，但仍削弱审稿人信任\n\n**W8. [Warning] 缺少同 Information Level 的 Binary-Only Baselines（R2 首提，R1 AGREE）** [两档共有]\n- 论文与 ConStat/Min-K%++ 的对比是跨 information level 的，缺少同一 level 内的对比\n- 关键缺失：accuracy z-score（最简单 binary anomaly detection）、ML classifier on binary vectors\n- 对 Worst 档尤其致命：若 ML classifier 有效则直接否定 \"binary information bottleneck\" claim\n\n**W9. [Warning] Power Function 是 Upper Bound 而非 Expected Power（R1 首提，R2 AGREE）** [Median 档]\n- R²=0.96 基于 simulation（无 SFT 泛化效应），实际中 ~45% accuracy gain 来自泛化而非记忆\n- Power function 的 practical guidance（如 \"n≥7,000\"）基于乐观假设，实际阈值可能更高\n\n**W10. [Warning] IRT 参数质量/Sensitivity 未讨论（R1 首提，R2 AGREE）** [两档共有]\n- 整个方法依赖 PSN-IRT 的 4PL IRT 参数，未做 sensitivity analysis\n- 参数 drift（calibration sample vs current LLM population）对检测性能的影响不可知\n\n**W11. [Warning] Type-I Error 0.08 vs 0.05（R1 首提，R2 AGREE）** [Worst 档]\n- 60% FPR 膨胀在统计方法论论文中需认真对待\n- Clean SFT baseline lz* = -18.4 暗示 null distribution 校准失败\n\n**W12. [Warning] K-means Typology 循环论证（R1 首提，R2 AGREE）** [Worst 档]\n- 基于 (θ, lz*) 的 clustering 产生的 \"contamination typology\" 缺乏 ground truth\n- \"Contamination OR genuine expertise\" 的标签歧义正是方法本身无法解决的——用 method output 的 clustering 来 validate method effectiveness 是循环论证\n\n### Minor/Format Issues\n\n**W13. [Info] Model Coverage 局限** — 4 个模型均为 dense 7B-31B SFT，缺乏 MoE/70B+/reasoning 验证（R2 首提，R1 REBUT——认为 4 模型、3 个 family 对 8 页论文已足够）\n\n**W14. [Warning] Limitations 应为独立 section** — EMNLP 2026 要求 mandatory Limitations section，当前为 Conclusion 内 paragraph，存在 desk rejection 风险\n\n---\n\n## Questions\n\n**Q1.** 论文的 FPR/threshold 设定使用的是 theoretical null (N(0,1)) 还是 bootstrap null？如果是前者，在 LLM population 中 lz* 系统性偏离理论分布的情况下，所有 p-value 和 flagging rate 都不可靠。\n\n**Q2.** Δlz* 在 clean-vs-clean 对比中的均值是否为 0？如果 clean 条件下的 Δlz* 本身也有 systematic bias，则 Δlz* 设计未能完全消除 absolute bias 的影响。\n\n**Q3.** 是否测试过任何 alternative binary-only method（如 logistic regression / random forest on binary response vectors）？如果有，结果如何？如果没有，\"binary information bottleneck\" 的 claim 基于什么排除了这些方法的可能性？\n\n**Q4.** Abstract 中 \"AUROC 0.92 after GRPO\" 来自哪个具体的实验条件？是否存在选择性报告最优条件下的数字而在正文中呈现更低的一般性结果（AUROC 0.56）？\n\n**Q5.** 不同污染机制（pre-training exposure vs SFT injection）在 response pattern 上的差异是否有理论或经验分析？SFT 泛化效应是否是 SFT-specific 的？\n\n---\n\n## Missing References\n\n- Drasgow & Levine (1986) 经典 person-fit 文献——论文引用链中缺失\n- Karabatsos (2003) 非参数 person-fit 方法——可能避免 parametric IRT 的 model misfit 问题\n- Zhu et al. (2023) \"Dyval: Dynamic evaluation\" — 动态评估的替代路径\n- Golchin & Surdeanu (2024) \"Time Travel in LLMs\" — 另一种 contamination detection 方法\n- Balloccu et al. (2024) \"Leak, Cheat, Repeat\" — closed-source LLM contamination 系统研究\n- Ye et al. (2024) \"Data Contamination Quiz\" — 另一种 binary-level 检测方法\n\n---\n\n## External Review\n\n**外部审稿：未请求。**\n\n---\n\n## Visual Layout Check\n\n**视觉审查：未启动（not_started）。**\n\n---\n\n## Overall Assessment\n\n### Median 档：3.0 — Findings（R1: 3.0, R2: 3.0, 共识）\n\nPower function 理论和 detection frontier 概念是有价值的方法论贡献。受控实验设计严谨，9 个实验全覆盖，负面结果诚实呈现。但 leaderboard audit 的 baseline 可靠性（W1）和 post-RL scope gap（W2）使论文的第三个 contribution（大规模 audit）不可信。SFT 泛化效应的识别有独立价值但 scope 受限于单一污染机制。\n\n- 主会议接收（≥3.5）：需解决 W1 (baseline robustness) + W2 (post-RL scope) + W6 (multiple testing correction)\n- Findings 接收（3.0）：当前版本的概念贡献 + 实验覆盖度足以支撑\n\n### Worst 档：2.75 — R1/R2 分歧区间 [2.5, 3.0]\n\n**R1 (2.5) 的理由**：Information-theoretic lower bound overclaim 是核心逻辑缺陷，使论文从 \"fundamental impossibility\" 降级为 \"method-specific failure\"，novelty 不足以支撑 Findings。\n\n**R2 (3.0) 的理由**：即使 overclaim 需修正，power function 框架 + detection frontier + SFT generalization analysis 的概念贡献包仍有独立的社区价值，足以支撑 Findings lower end。\n\n**Director 裁定**：R2 的论点更有说服力——概念贡献的价值不依赖于 impossibility claim 是否成立。但 overclaim 是严重的 framing 问题（W3），需修正后才能达到 solid Findings。**建议评分 2.75（lower-end Findings，需 revision）**，若作者能 (1) 将 claim 限定为 method-specific，(2) 补充 ≥1 个 alternative binary-only baseline，(3) 修正 Abstract 中的选择性报告，可升至 3.0。\n\n### 综合评估\n\n论文面临的核心挑战是一条完整的问题链（R1 + R2 综合）：\n\n**IRT 模型对 LLM 拟合不良（W5）→ absolute lz* 无区分力 → Δlz* 依赖 baseline 选择 → baseline 在 audit 中不可靠（W1）+ 对 post-RL 模型 blind（W2）**\n\n论文在这条链的中段（Δlz* detection frontier 理论）做了有价值的工作，但上游前提（IRT-LLM fit）和下游应用（leaderboard audit reliability）都存在未解决的断裂点。\n\n### 改进优先级（R1, R2 共识整合）\n\n**P0 — 核心 claim 修正：**\n1. 将 \"information-theoretic lower bound for all binary-only methods\" 限定为 \"IRT person-fit 在 SFT 条件下的局限性\"\n2. 修正 Abstract 选择性报告（AUROC 0.92 → 呈现所有条件下的完整结果）\n\n**P1 — 方法论加固：**\n3. 补充 ≥2 种同 information level 的 binary-only baselines（accuracy z-score + ML classifier）\n4. 测试 Leaderboard audit 的 baseline 替代策略（pre-SFT model / global median / cross-validation）\n5. 补充 BH-FDR 多重检验校正\n\n**P2 — 实验扩展：**\n6. 增加 ≥1 种替代污染机制（如 continued pre-training on benchmark items）\n7. 在 audit 中标注 post-RL 模型并分析 Δlz* 分布差异\n\n**P3 — 格式/呈现：**\n8. 将 Limitations 改为独立 section\n9. 补全所有 incomplete tables\n10. 增加 empirical null distribution 诊断（QQ plot / KS test）\n\n---\n\n## Detailed Comments\n\n### 方法论\n- Δlz* 设计是应对 systematic bias 的合理策略，但其有效性依赖于 bias 在 clean/contaminated 条件下为常数这一未验证的假设。若 SFT 本身改变了 bias 的 direction 或 magnitude，Δlz* 也会失效。\n- Power function 框架的最大价值不是预测 detection power（它给出的是 upper bound），而是作为方法论工具——可以用同一框架评估 alternative methods 的理论检测上限，为方法选择提供 information-theoretic guidance。建议论文以此角度重新定位 power function 的贡献。\n- lzm 多尺度聚合仅带来 ~2pp AUROC 提升且不显著，建议移至 appendix 以腾出空间给更重要的讨论。\n\n### 实验设计\n- QLoRA SFT 注入的 \"clean\" contamination（直接微调 benchmark items）与真实 contamination（pretraining 中 accidental inclusion、data augmentation、curriculum learning）的信号特征可能有本质差异。SFT 泛化效应是 SFT-specific 的机制——在 pretraining 中，model 可能精确记住 item 答案而不产生领域泛化，从而保留 classic aberrant pattern。\n- Leaderboard audit 的 temporal trend（flagging rate 增长）可能混淆了两个变量：真实 contamination 增长 + RL 技术采用率增加导致信号被洗掉。\n\n### 叙事/Framing（对 Worst 档尤其重要）\n- \"Universal model misfit\" 的大规模确认（96-99% flagging rate on 5,847 models）即使作为 descriptive finding 也有独立价值，但论文将其同时用作 \"evidence for binary bottleneck\" 和 \"interesting independent finding\"——这两个角色在叙事上矛盾。\n- 建议将论文 reframe 为 \"IRT person-fit 在 LLM contamination detection 上的局限性分析\"，将 power function 作为独立的正面贡献，SFT generalization 作为对社区的警示。\n\n### 写作\n- 参考文献仅 11 篇，对涉及 IRT + contamination detection + person-fit 三个领域交叉的论文来说偏少\n- 部分 Table 的 \"*\" 标注（如 Table 5 的 BBH/MATH, Table 9 的 Gemini-1.5-Pro*）未在注释中解释\n\n---\n\n## Reviewer 共识记录\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Baseline chicken-and-egg (W1) | 首提 | AGREE | ✅ |\n| Post-RL scope gap (W2) | 首提 | AGREE + nuance | ✅ |\n| Overclaim (W3) | 首提 | AGREE | ✅ |\n| Single mechanism (W4) | 首提 | AGREE | ✅ |\n| Systematic bias severity | Warning | Originally Critical → 接受 R1 降级 | ✅ Warning |\n| Missing baselines (W8) | AGREE | 首提 | ✅ |\n| Model coverage | REBUT (4 models 足够) | 首提 → 降级为 info | ✅ Resolved |\n| **Worst 档评分** | **2.5** | **3.0** | **⚠️ 分歧** |\n| Median 档评分 | 3.0 | 3.0 | ✅ |\n\n**未解决分歧**：Worst 档评分（R1: 2.5 vs R2: 3.0）。分歧本质是概念贡献（power function + detection frontier）能否独立支撑 Findings 接收——R2 认为可以，R1 认为 overclaim 修正后 novelty 不够。Director 建议 2.75。",
  "project": "irt_personfit_contam",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "Median: 3.0 (Findings) | Worst: 2.75 (Lower-end Findings, 需 revision)",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告（修正版）：irt_personfit_contam Dream Papers\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit  \n**Round**: 1  \n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)  \n**审稿对象**: Dream Report 的 Median 档和 Worst 档  \n**收敛状态**: 充分交叉讨论，核心共识达成，评分分歧 0.5 分（仅 worst 档）\n\n⚠️ **修正说明**: 本报告替换此前因服务器重启导致的错误提交（原报告误基于 Best 档 paper.tex 撰写）。\n\n---\n\n## 审稿对象概述\n\nDream Report 生成了三个版本的论文，R1 审了 Median 和 Worst 两个档位：\n\n| 档位 | 标题 | 核心 Framing | 实际 AUROC@15% | R1 | R2 |\n|------|------|-------------|----------------|----|----|\n| **Median** | IRT-FIT: Characterizing the Detection Frontier | 混合结果：部分有效的检测工具 + 理论贡献 | 0.78 (MMLU) | 3.0 | 3.0 |\n| **Worst** | The Binary Response Bottleneck | Negative result：揭示 binary-only 检测的根本限制 | 0.61 (MMLU) | 2.5 | 3.0 |\n\n---\n\n## Summary\n\n### Median 档\n论文将 IRT person-fit 统计量（lz*）应用于 LLM benchmark contamination 检测，定位为 \"minimal-information operating point\"（仅需 binary response）。受控实验在 4 个模型（Qwen3.5-9B, Mistral-7B-v0.3, Llama-3.1-8B, Gemma-4-31B）上通过 QLoRA SFT 注入污染，best-case AUROC 0.78 at 15% MMLU。核心理论贡献是 detection power function（R²=0.96），将检测功效与 benchmark size 的关系形式化。大规模 leaderboard audit 扫描 6,200+ 模型。Post-RL 实验显示信号大幅衰减（AUROC 0.56）。\n\n### Worst 档\n同一研究框架，但 framing 为 negative result：IRT person-fit 在 SFT 泛化效应下基本失效（AUROC 0.61），universal model misfit 导致 96-99% 模型被错误标记。论文据此声称揭示了 \"binary-only contamination detection 的 information-theoretic lower bound\"。\n\n---\n\n## Strengths（R1, R2 共识）\n\n**S1. Power Function 理论框架（R1 首推，R2 共识）。** Detection power 与 benchmark size 的解析公式（R²=0.96），inverted-U 拐点可从 item difficulty distribution 预测（误差 ≤0.02），并用 BBH/MATH 进行了 out-of-sample 验证。**即使方法的实际检测力有限，这个理论框架本身具有独立的方法论价值**——可用于评估任意 contamination detection 方法的 detection power。两位 Reviewer 一致认为这是论文最突出的贡献。\n\n**S2. Detection Frontier Framing（R1 首推，R2 共识）。** 将检测方法按 information access level 组织（binary < binary+retest < token probs < training data < weights），清晰定位 IRT-FIT 的角色。这个概念框架为后续工作提供了有用的 vocabulary。\n\n**S3. SFT 泛化效应的系统性刻画（两档共有）。** SFT on benchmark items 同时教授 specific item answers 和 general domain knowledge，后者产生\"正常化\"的 response patterns，使 person-fit 无法区分 contamination 和 genuine ability gain。这一机制解释清晰、有控制实验支撑，对 benchmark integrity 社区有实质参考价值。\n\n**S4. 诚实呈现负面结果。** Post-RL signal loss、GSM8K 低 power、leaderboard audit 高 flagging rate 等负面结果均如实呈现，增强了论文可信度。实验覆盖度 9/9 = 100%（对照 review_context.yaml）。\n\n**S5. 独特的 Scalability 优势。** IRT-FIT 是唯一能用 archival binary data 进行 retrospective audit 的方法，这一 practical advantage 有实际意义。\n\n---\n\n## Weaknesses\n\n### Critical Issues\n\n**W1. [Critical] Leaderboard Audit 的 Δlz* Baseline Chicken-and-Egg 问题（R1 首提，R2 AGREE）** [Median 档]\n- Leaderboard audit 使用 per-family median lz* 作为 \"clean\" baseline 计算 Δlz*\n- 若整个 model family 的 base model training data 已含 benchmark items（对 MMLU 等广泛流传的 benchmark 几乎必然），family median 本身已被污染抬高，Δlz* 系统性低估\n- 直接影响 leaderboard audit 全部定量结论：flagging rates、temporal trends、cross-benchmark anomalies\n- 论文未测试此假设的 sensitivity，未提供替代 baseline 的 robustness check\n\n**W2. [Critical] Post-RL 信号消失与 Leaderboard Audit 适用范围矛盾（R1 首提，R2 AGREE with nuance）** [Median 档]\n- Post-RL AUROC 降至 0.56（retention 仅 19%），论文承认 \"IRT-FIT detects SFT-based contamination but not post-RL contamination\"\n- 但 leaderboard audit 对 6,200+ 模型扫描，必然包含大量 RLHF/DPO/GRPO 模型\n- 低 Δlz* 可能是\"未受污染\"，也可能是\"RL 洗掉了信号\"——方法无法区分\n- R2 补充：controlled experiment → leaderboard audit 的逻辑链条因此断裂\n\n**W3. [Critical] \"Information-Theoretic Lower Bound\" 是 Overclaim（R1 首提，R2 AGREE）** [Worst 档]\n- 论文标题限定在 \"IRT Person-Fit Statistics\"，但 Abstract 和正文泛化为\"所有 binary-only 方法的 fundamental impossibility\"\n- 实际只证明 lz*（一种特定 summary statistic）在 SFT 泛化条件下失效\n- Binary response vector 包含 lz* 未利用的 higher-order patterns：item-item 条件依赖、response subsequence patterns、ability-inconsistent clusters\n- **论文未测试任何 alternative binary-only method**（如 ML classifier on binary vectors），却声称 binary information 本身不够——这是 affirming the consequent\n- 若 \"impossibility\" 不成立，论文叙事从 \"fundamental limitation\" 降级为 \"method-specific failure\"，novelty 显著降低\n\n**W4. [Critical] 单一污染机制不足以支撑 Bottleneck 结论（R1 首提，R2 AGREE）** [Worst 档]\n- 所有控制实验仅用 QLoRA SFT 注入污染\n- Pre-training memorization 的 learning dynamics 完全不同——可能产生 classic aberrant pattern（精确记住答案而未泛化），恰恰是 person-fit 设计检测的信号\n- 若 lz* 在 pre-training contamination 下有效，则 bottleneck 仅是 SFT-specific，论文标题和核心 claim 需根本性修改\n\n### Major/Warning Issues\n\n**W5. [Warning] Systematic Positive Bias / IRT Model Fundamental Misfit（R2 首提，R1 REBUT → 降级为 warning）** [两档共有]\n- 经验数据中 lz* 均值系统性偏离理论期望值 0（leaderboard: +12.5, clean SFT: -18.4），双向极端偏移说明 IRT 对 LLM response pattern 的拟合从根本上失败\n- R1 指出论文通过 Δlz*（within-model shift）设计性地应对了 absolute bias，若 bias 在 clean/contaminated 条件下是常数则被消除\n- **两位 Reviewer 共识**：不构成独立 showstopper（Δlz* 已部分应对），但暴露了 IRT 框架的适用性问题，是 W1 (baseline reliability) 的上游根因\n- 需验证：论文是否使用 bootstrap null 而非 theoretical null？Δlz* 本身是否也有 systematic bias？\n\n**W6. [Warning] 缺乏多重检验校正（R1 首提，R2 AGREE）** [Median 档]\n- 6,200 models × 4 benchmarks = 24,800 次检验，使用 2σ 阈值未做 Bonferroni/BH-FDR 校正\n- 期望 false positive 约 570 个，论文报告 MMLU 185 个 top anomaly 反而低于未校正 expected FP——暗示 Δlz* distribution 可能非正态\n- 统计方法论论文中此疏忽不可接受\n\n**W7. [Warning] Incomplete Tables / 选择性报告嫌疑（R2 首提，R1 AGREE）** [两档共有]\n- Gemma-4-31B 缺少部分污染水平数据、lzm 仅展示 5/12 models、two-sided results 仅展示 5/60 pairs\n- R1 注意到在 Dream 框架下可能是生成限制而非选择性报告，但仍削弱审稿人信任\n\n**W8. [Warning] 缺少同 Information Level 的 Binary-Only Baselines（R2 首提，R1 AGREE）** [两档共有]\n- 论文与 ConStat/Min-K%++ 的对比是跨 information level 的，缺少同一 level 内的对比\n- 关键缺失：accuracy z-score（最简单 binary anomaly detection）、ML classifier on binary vectors\n- 对 Worst 档尤其致命：若 ML classifier 有效则直接否定 \"binary information bottleneck\" claim\n\n**W9. [Warning] Power Function 是 Upper Bound 而非 Expected Power（R1 首提，R2 AGREE）** [Median 档]\n- R²=0.96 基于 simulation（无 SFT 泛化效应），实际中 ~45% accuracy gain 来自泛化而非记忆\n- Power function 的 practical guidance（如 \"n≥7,000\"）基于乐观假设，实际阈值可能更高\n\n**W10. [Warning] IRT 参数质量/Sensitivity 未讨论（R1 首提，R2 AGREE）** [两档共有]\n- 整个方法依赖 PSN-IRT 的 4PL IRT 参数，未做 sensitivity analysis\n- 参数 drift（calibration sample vs current LLM population）对检测性能的影响不可知\n\n**W11. [Warning] Type-I Error 0.08 vs 0.05（R1 首提，R2 AGREE）** [Worst 档]\n- 60% FPR 膨胀在统计方法论论文中需认真对待\n- Clean SFT baseline lz* = -18.4 暗示 null distribution 校准失败\n\n**W12. [Warning] K-means Typology 循环论证（R1 首提，R2 AGREE）** [Worst 档]\n- 基于 (θ, lz*) 的 clustering 产生的 \"contamination typology\" 缺乏 ground truth\n- \"Contamination OR genuine expertise\" 的标签歧义正是方法本身无法解决的——用 method output 的 clustering 来 validate method effectiveness 是循环论证\n\n### Minor/Format Issues\n\n**W13. [Info] Model Coverage 局限** — 4 个模型均为 dense 7B-31B SFT，缺乏 MoE/70B+/reasoning 验证（R2 首提，R1 REBUT——认为 4 模型、3 个 family 对 8 页论文已足够）\n\n**W14. [Warning] Limitations 应为独立 section** — EMNLP 2026 要求 mandatory Limitations section，当前为 Conclusion 内 paragraph，存在 desk rejection 风险\n\n---\n\n## Questions\n\n**Q1.** 论文的 FPR/threshold 设定使用的是 theoretical null (N(0,1)) 还是 bootstrap null？如果是前者，在 LLM population 中 lz* 系统性偏离理论分布的情况下，所有 p-value 和 flagging rate 都不可靠。\n\n**Q2.** Δlz* 在 clean-vs-clean 对比中的均值是否为 0？如果 clean 条件下的 Δlz* 本身也有 systematic bias，则 Δlz* 设计未能完全消除 absolute bias 的影响。\n\n**Q3.** 是否测试过任何 alternative binary-only method（如 logistic regression / random forest on binary response vectors）？如果有，结果如何？如果没有，\"binary information bottleneck\" 的 claim 基于什么排除了这些方法的可能性？\n\n**Q4.** Abstract 中 \"AUROC 0.92 after GRPO\" 来自哪个具体的实验条件？是否存在选择性报告最优条件下的数字而在正文中呈现更低的一般性结果（AUROC 0.56）？\n\n**Q5.** 不同污染机制（pre-training exposure vs SFT injection）在 response pattern 上的差异是否有理论或经验分析？SFT 泛化效应是否是 SFT-specific 的？\n\n---\n\n## Missing References\n\n- Drasgow & Levine (1986) 经典 person-fit 文献——论文引用链中缺失\n- Karabatsos (2003) 非参数 person-fit 方法——可能避免 parametric IRT 的 model misfit 问题\n- Zhu et al. (2023) \"Dyval: Dynamic evaluation\" — 动态评估的替代路径\n- Golchin & Surdeanu (2024) \"Time Travel in LLMs\" — 另一种 contamination detection 方法\n- Balloccu et al. (2024) \"Leak, Cheat, Repeat\" — closed-source LLM contamination 系统研究\n- Ye et al. (2024) \"Data Contamination Quiz\" — 另一种 binary-level 检测方法\n\n---\n\n## External Review\n\n**外部审稿：未请求。**\n\n---\n\n## Visual Layout Check\n\n**视觉审查：未启动（not_started）。**\n\n---\n\n## Overall Assessment\n\n### Median 档：3.0 — Findings（R1: 3.0, R2: 3.0, 共识）\n\nPower function 理论和 detection frontier 概念是有价值的方法论贡献。受控实验设计严谨，9 个实验全覆盖，负面结果诚实呈现。但 leaderboard audit 的 baseline 可靠性（W1）和 post-RL scope gap（W2）使论文的第三个 contribution（大规模 audit）不可信。SFT 泛化效应的识别有独立价值但 scope 受限于单一污染机制。\n\n- 主会议接收（≥3.5）：需解决 W1 (baseline robustness) + W2 (post-RL scope) + W6 (multiple testing correction)\n- Findings 接收（3.0）：当前版本的概念贡献 + 实验覆盖度足以支撑\n\n### Worst 档：2.75 — R1/R2 分歧区间 [2.5, 3.0]\n\n**R1 (2.5) 的理由**：Information-theoretic lower bound overclaim 是核心逻辑缺陷，使论文从 \"fundamental impossibility\" 降级为 \"method-specific failure\"，novelty 不足以支撑 Findings。\n\n**R2 (3.0) 的理由**：即使 overclaim 需修正，power function 框架 + detection frontier + SFT generalization analysis 的概念贡献包仍有独立的社区价值，足以支撑 Findings lower end。\n\n**Director 裁定**：R2 的论点更有说服力——概念贡献的价值不依赖于 impossibility claim 是否成立。但 overclaim 是严重的 framing 问题（W3），需修正后才能达到 solid Findings。**建议评分 2.75（lower-end Findings，需 revision）**，若作者能 (1) 将 claim 限定为 method-specific，(2) 补充 ≥1 个 alternative binary-only baseline，(3) 修正 Abstract 中的选择性报告，可升至 3.0。\n\n### 综合评估\n\n论文面临的核心挑战是一条完整的问题链（R1 + R2 综合）：\n\n**IRT 模型对 LLM 拟合不良（W5）→ absolute lz* 无区分力 → Δlz* 依赖 baseline 选择 → baseline 在 audit 中不可靠（W1）+ 对 post-RL 模型 blind（W2）**\n\n论文在这条链的中段（Δlz* detection frontier 理论）做了有价值的工作，但上游前提（IRT-LLM fit）和下游应用（leaderboard audit reliability）都存在未解决的断裂点。\n\n### 改进优先级（R1, R2 共识整合）\n\n**P0 — 核心 claim 修正：**\n1. 将 \"information-theoretic lower bound for all binary-only methods\" 限定为 \"IRT person-fit 在 SFT 条件下的局限性\"\n2. 修正 Abstract 选择性报告（AUROC 0.92 → 呈现所有条件下的完整结果）\n\n**P1 — 方法论加固：**\n3. 补充 ≥2 种同 information level 的 binary-only baselines（accuracy z-score + ML classifier）\n4. 测试 Leaderboard audit 的 baseline 替代策略（pre-SFT model / global median / cross-validation）\n5. 补充 BH-FDR 多重检验校正\n\n**P2 — 实验扩展：**\n6. 增加 ≥1 种替代污染机制（如 continued pre-training on benchmark items）\n7. 在 audit 中标注 post-RL 模型并分析 Δlz* 分布差异\n\n**P3 — 格式/呈现：**\n8. 将 Limitations 改为独立 section\n9. 补全所有 incomplete tables\n10. 增加 empirical null distribution 诊断（QQ plot / KS test）\n\n---\n\n## Detailed Comments\n\n### 方法论\n- Δlz* 设计是应对 systematic bias 的合理策略，但其有效性依赖于 bias 在 clean/contaminated 条件下为常数这一未验证的假设。若 SFT 本身改变了 bias 的 direction 或 magnitude，Δlz* 也会失效。\n- Power function 框架的最大价值不是预测 detection power（它给出的是 upper bound），而是作为方法论工具——可以用同一框架评估 alternative methods 的理论检测上限，为方法选择提供 information-theoretic guidance。建议论文以此角度重新定位 power function 的贡献。\n- lzm 多尺度聚合仅带来 ~2pp AUROC 提升且不显著，建议移至 appendix 以腾出空间给更重要的讨论。\n\n### 实验设计\n- QLoRA SFT 注入的 \"clean\" contamination（直接微调 benchmark items）与真实 contamination（pretraining 中 accidental inclusion、data augmentation、curriculum learning）的信号特征可能有本质差异。SFT 泛化效应是 SFT-specific 的机制——在 pretraining 中，model 可能精确记住 item 答案而不产生领域泛化，从而保留 classic aberrant pattern。\n- Leaderboard audit 的 temporal trend（flagging rate 增长）可能混淆了两个变量：真实 contamination 增长 + RL 技术采用率增加导致信号被洗掉。\n\n### 叙事/Framing（对 Worst 档尤其重要）\n- \"Universal model misfit\" 的大规模确认（96-99% flagging rate on 5,847 models）即使作为 descriptive finding 也有独立价值，但论文将其同时用作 \"evidence for binary bottleneck\" 和 \"interesting independent finding\"——这两个角色在叙事上矛盾。\n- 建议将论文 reframe 为 \"IRT person-fit 在 LLM contamination detection 上的局限性分析\"，将 power function 作为独立的正面贡献，SFT generalization 作为对社区的警示。\n\n### 写作\n- 参考文献仅 11 篇，对涉及 IRT + contamination detection + person-fit 三个领域交叉的论文来说偏少\n- 部分 Table 的 \"*\" 标注（如 Table 5 的 BBH/MATH, Table 9 的 Gemini-1.5-Pro*）未在注释中解释\n\n---\n\n## Reviewer 共识记录\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Baseline chicken-and-egg (W1) | 首提 | AGREE | ✅ |\n| Post-RL scope gap (W2) | 首提 | AGREE + nuance | ✅ |\n| Overclaim (W3) | 首提 | AGREE | ✅ |\n| Single mechanism (W4) | 首提 | AGREE | ✅ |\n| Systematic bias severity | Warning | Originally Critical → 接受 R1 降级 | ✅ Warning |\n| Missing baselines (W8) | AGREE | 首提 | ✅ |\n| Model coverage | REBUT (4 models 足够) | 首提 → 降级为 info | ✅ Resolved |\n| **Worst 档评分** | **2.5** | **3.0** | **⚠️ 分歧** |\n| Median 档评分 | 3.0 | 3.0 | ✅ |\n\n**未解决分歧**：Worst 档评分（R1: 2.5 vs R2: 3.0）。分歧本质是概念贡献（power function + detection frontier）能否独立支撑 Findings 接收——R2 认为可以，R1 认为 overclaim 修正后 novelty 不够。Director 建议 2.75。",
    "project": "irt_personfit_contam",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "Median: 3.0 (Findings) | Worst: 2.75 (Lower-end Findings, 需 revision)",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 108 · 2026-05-20T11:50:28.853386+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5579
}
```

</details>

---


### Assistant

_source line 109 · 2026-05-20T11:50:40.599385+00:00_

修正版审稿报告已提交。

**审稿圆桌总结**：

- **Median 档**（IRT-FIT: Characterizing the Detection Frontier）：**3.0 / 5 Findings**（R1=3.0, R2=3.0, 共识）
- **Worst 档**（The Binary Response Bottleneck）：**2.75 / 5**（R1=2.5, R2=3.0, Director 裁定取中）

**4 个 Critical Issues**：
1. Leaderboard audit baseline chicken-and-egg 问题
2. Post-RL 信号消失与 audit 覆盖范围矛盾
3. "Information-theoretic lower bound" overclaim（worst 档）
4. 单一污染机制不足以支撑 bottleneck 结论（worst 档）

**核心判断**：论文在 detection frontier 理论（power function）和 SFT 泛化效应刻画上有方法论价值，但从 controlled experiment 到 real-world audit 的推广链条存在多个断裂点。Median 档可进 Findings；Worst 档需修正 overclaim 和补充 alternative binary-only baselines 才能站稳 Findings。

**Issue tracker** 已更新（14 个 issues），路径：`artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 110 · 2026-05-20T11:50:43.239555+00:00_

[Reviewer 2 审稿结果]:
已向 Director 提交交叉回应。核心立场：对 R1 的 N1（overclaim）和 N2（单一污染机制）全部 AGREE，但在最终评分上维持 3.0 而非下调至 2.5——分歧点在于 power function + detection frontier 的概念框架是否具有独立于实证结果的 Findings 级别价值。已表明如果 Director 需要统一评分，可接受 2.5-3.0 之间裁定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 111 · 2026-05-20T11:50:56.291383+00:00_

修正版审稿报告已提交给 Research Director，包含 R2 的最终立场确认。

**最终状态总结：**

- **Median 档**：3.0 (Findings) — R1、R2 一致
- **Worst 档**：2.75 (Director 裁定) — R1 给 2.5，R2 给 3.0，分歧在概念贡献权重
- **Issue Tracker**：14 个 issues（4 critical, 8 warning, 1 info, 1 format）
- **核心问题链**：IRT-LLM misfit → absolute lz* 失效 → Δlz* baseline 不可靠 → audit 结论存疑 + post-RL blind
- **改进路径**：P0 修正 overclaim + 选择性报告 → P1 补 binary baselines + audit baseline robustness → P2 替代污染机制

审稿圆桌会议完成。报告已投递，等待 Research Director 处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 14

## Round 14

6 recorded events


### User

_source line 112 · 2026-05-20T19:47:42.211262+00:00_

[Reviewer 1 审稿意见]:
## IRT-FIT Paper Review (EMNLP 2026 ARR) — Reviewer 1

---

### A. Format/Compliance Check

**Page count**: Main text (Sections 1–11) extends to approximately page 9 (Conclusion ends mid-page 9), exceeding the 8-page limit by ~0.5 page. Tables 11–12 (referenced in Sections 8.3 and 9.1) also fall on page 9, pushing main-text content beyond page 8. Appendix A (Reproducibility) and Tables 13–14 are on pages 9–10 and could be considered supplementary. **Verdict**: Borderline violation. The "Scope and limitations" subsection in Section 10 could count under the mandatory Limitations exemption, partially offsetting the overage. However, the Conclusion (Section 11) is clearly main text. Recommend trimming ~0.5 page (e.g., compress Section 9 Additional Analyses or move Tables 13–14 to appendix).

**Anonymity**: Title page shows "Anonymous." No obvious deanonymization.

**Limitations section**: Present as a subsection "Scope and limitations" within Section 10 Discussion, covering benchmark size constraints, SFT-style contamination scope, and post-RL partial retention. Content is adequate but not a standalone section — some ACs may prefer a dedicated "Limitations" section header per ARR guidelines.

**Citation verification**: Only ~7 references are visible in the paper. This is exceptionally sparse for a paper spanning IRT, contamination detection, and LLM evaluation. Key missing citations include: Drasgow & Levine (1986) on person-fit foundations, Karabatsos (2003) on response-appropriateness indices, Magar & Schwartz (2022) on data contamination, Oren et al. (2024) on proving test set contamination, Polo et al. (2024) on tinyBenchmarks. The paper cites Snijders (2001) and Hong et al. (2021) for lz* but misses the broader person-fit literature. I cannot verify reference accuracy without checking the bibliography entries, but the sparse count is a concern.

---

### B. Soundness: 3.5 / 5

**Strengths in methodology:**

1. **Controlled experiment design is rigorous**: 4 models × 6 contamination levels × 3 benchmarks × 3 seeds per cell = 216 training runs. This factorial design with proper replication is the gold standard for establishing causal contamination→Δlz* mappings. Table 2's complete AUROC matrix and Table 3's Cohen's d matrix provide transparent, reproducible evidence.

2. **Dual-regime signal structure (Section 5.2)** is a theoretically motivated insight: partial contamination (<80% of items contaminated) produces aberrant responses (answering hard items correctly beyond ability prediction), while near-full contamination produces over-consistent patterns. The crossover point at 78–85% accuracy is empirically grounded and benchmark-invariant. This adds interpretive depth beyond simple detection.

3. **Power function validation (Table 4)**: R²=0.94 across 7 benchmarks (including BBH and MATH as out-of-sample validation) confirms √n scaling. The inclusion of "Ctrl AUROC" alongside "Sim Power" in the same table allows direct comparison of simulation predictions vs. real detection, which is transparent.

4. **Population-based flagging for leaderboard audit** (Section 8): Using ability-matched peer comparison (θ±0.5 bin, |Δlz*| > 2 SD) is methodologically superior to absolute thresholds. The 8.3% overall flagging rate (Table 9) is far more informative than the ~92-96% rates seen in alternative approaches, providing actual discriminative power.

**Concerns:**

1. **Leaderboard audit lacks ground-truth validation** [idea level]. The 8.3% flagging rate and temporal trend (+2.1pp/quarter) are presented as evidence of contamination, but without ground truth, false positive rate is unknown. The paper argues for external validity (GSM8K highest flagging rate aligns with known data leakage), but this is a single point of corroboration. The temporal trend could alternatively reflect increasing model capability causing more extreme misfit, not necessarily contamination. **Severity: Should-Fix.** The paper partially addresses this by hedging ("systematic contamination patterns" rather than "confirmed contamination"), but should add sensitivity analysis (e.g., varying the 2 SD threshold) and discuss alternative explanations for the temporal trend.

2. **Discrepancy between Director's summary and actual PDF content**. The Director's summary mentions several analyses not clearly present in the PDF: (a) **θ-fixed dose-response analysis** (Sec 5.3 in summary) — the PDF has "Dual-Regime Signal Structure" (Sec 5.2) which is related but different; (b) **memorization fraction** — mentioned in passing but not developed as a formal concept with per-model/per-domain quantification; (c) **IRT estimation from leaderboard** (a_r plateau at N≈450) — not visible in the PDF; (d) **natural experiment** (5 base→chat pairs) — not visible. If these analyses were planned but omitted, it reduces the depth of evidence. If they're compressed into other sections beyond what I can parse from the PDF rendering, the presentation needs improvement to make them discoverable.

3. **Single contamination mechanism**: All controlled experiments use QLoRA SFT on randomly sampled benchmark items. As noted in my reviews of the median and worst papers, this limits generalizability. If contamination occurs through pre-training data inclusion (no QLoRA adapter, memorization through millions of gradient updates), the response pattern may differ. However, the paper's scope statement ("SFT-style contamination") is more careful than the other versions.

4. **Clean-clean Δlz* calibration**: The paper notes clean-clean Δlz* ≈ 0.70 (from Director's summary), indicating some non-zero baseline shift even without contamination. This needs more discussion — is 0.70 within the expected variance from SFT stochasticity? The paper should report the clean-clean Δlz* distribution more explicitly and confirm that the detection threshold is set above this noise floor.

---

### C. Excitement / Novelty: 3.5 / 5

**Novel contributions:**

1. **Post-RL robustness (Section 7, Tables 7–8)** is the paper's most exciting finding and its strongest differentiator. IRT-FIT retains 63% of signal post-RL (AUROC 0.88) while Min-K%++ collapses to 0.58 (near chance). The mechanism is clearly explained: binary response patterns are more robust to RL's probability redistribution than token-level signatures. This directly addresses an open problem (Wang et al., 2025) and positions IRT-FIT as complementary to — not competing with — existing methods. This finding alone may merit Findings-level publication.

2. **Dual-regime signal structure** provides a previously unknown characterization of how contamination manifests differently depending on the fraction of items contaminated. The crossover point (~80%) is an actionable insight for practitioners.

3. **Detection frontier framing** (Table 6) is a useful conceptual contribution. Positioning IRT-FIT as the "minimal-information operating point" and showing only 5–6pp AUROC gap vs. gray-box methods (Table 5) is a compelling cost-benefit argument.

4. **Leaderboard audit at 11,200 models** is unprecedented in scale. Multi-benchmark flagging (Table 10), temporal trends (Table 11), and model-family clustering add actionable intelligence beyond simple detection.

**Limitations on novelty:**

1. IRT person-fit statistics are well-established in psychometrics (Snijders, 2001). The core methodological contribution is the application to LLMs, not a new statistical framework. The paper is upfront about this.

2. Concurrent work (ConStat, CoDeC, Min-K%++) addresses the same problem with different approaches. IRT-FIT's unique angle (minimal information + post-RL robustness) is clear, but the landscape is competitive.

3. "Characterizing operating conditions" is a softer contribution than proposing a strong detection method. The paper navigates this well by combining characterization with the leaderboard audit (applied contribution), but some reviewers may find the contribution incremental.

---

### D. Reproducibility: 3 / 5

**Present:**
- Appendix A specifies QLoRA hyperparameters (rank 16, α=32, learning rate 2e-4, 3 epochs), GRPO details (rule-based rewards, 2–3 epochs), and IRT parameter source (ltm R package, MML-EM).
- Leaderboard data source specified (Hugging Face Open LLM Leaderboard v1 API).
- 14 tables provide detailed numerical results.

**Missing:**
- No code release mentioned (no GitHub URL or "code will be released" statement).
- No data release plan for the processed leaderboard dataset (11,200 models' binary responses).
- PSN-IRT parameter details incomplete — are the 4PL parameters from existing calibrations or re-estimated? Table 14 mentions ltm R package but doesn't specify the calibration dataset.
- Number of GPUs, total compute budget, and wall-clock time not reported.

---

### E. Strengths and Weaknesses

**Major Strengths:**

**S1**: Post-RL robustness finding (AUROC 0.88 vs Min-K%++ 0.58) is a genuine advance that directly addresses a known open problem. The mechanistic explanation (binary patterns are robust to RL probability redistribution) is convincing and provides theoretical insight beyond empirical observation.

**S2**: Comprehensive factorial controlled experiment (4 models × 6 levels × 3 benchmarks × 3 seeds) with AUROC 0.94 on MMLU at 15% contamination. This is a convincing headline result supported by proper replication. The inter-model consistency analysis (Table 2 shows all 4 models achieve AUROC ≥0.91 on MMLU at 15%) strengthens the generalizability claim.

**S3**: Power function (R²=0.94 across 7 benchmarks) with out-of-sample validation (BBH, MATH) provides predictive theory. This enables practitioners to assess IRT-FIT's applicability to new benchmarks without running experiments — a genuinely useful tool.

**S4**: Leaderboard audit at 11,200 models with population-based flagging is methodologically superior to absolute-threshold approaches. The 8.3% flagging rate provides discriminative signal. Temporal trends and model-family clustering offer actionable intelligence.

**S5**: Honest treatment of failure modes — GSM8K's limited power at n=1,319 items (AUROC 0.72 at 15%) is transparently reported and theoretically explained via the power function.

**Major Weaknesses:**

**W1** [presentation]: **14 tables, 0 figures, ~7 references**. This paper is overwhelmingly data-dense with no visualization. The dual-regime structure, dose-response curves, detection frontier, temporal trends, and domain-level heatmaps all cry out for figures. The sparse reference list (≈7) is inadequate for a cross-disciplinary paper — key IRT person-fit literature (Drasgow, Karabatsos, Meijer & Sijtsma), contamination detection work (Magar & Schwartz, Oren et al., Polo et al.), and LLM evaluation papers are missing. This is a serious presentation weakness that would disadvantage the paper in peer review.

**W2** [idea]: **Leaderboard audit validation gap**. The 8.3% flagging rate and temporal trend are the paper's applied headline, but lack ground-truth validation. Without knowing the false positive rate, the practical value of the flagging is unclear. The paper provides one external validity point (GSM8K flagging rate matches known leakage) but this is weak evidence. The temporal trend has an alternative explanation (model capability increase → more extreme misfit).

**W3** [idea]: **Single contamination mechanism**. QLoRA SFT is the only contamination pathway tested. The paper's claim about "SFT-style contamination" scope is appropriate, but the missing evidence on pre-training contamination (where memorization dynamics differ fundamentally) limits the practical scope. The paper argues SFT produces "localized" aberrant patterns (Table 13), but this may be specific to QLoRA's low-rank constraint — full fine-tuning or pre-training contamination may produce more diffuse patterns that are harder to detect.

**W4** [presentation/idea]: **Missing experiments from design document**. Comparing the Director's summary against the PDF, several analyses appear absent or underspecified: (a) θ-fixed dose-response analysis, (b) memorization fraction as a formal concept, (c) IRT re-estimation from leaderboard data (structural failure finding), (d) natural experiment (base→chat pairs). If these were planned and omitted, the paper loses valuable supporting evidence. The IRT re-estimation failure in particular would be an important negative result to report.

**Minor Issues:**
- Table 4 shows "Ctrl AUROC" for GSM8K (0.72) substantially above "Theory Pred" (0.55) — this discrepancy needs explanation. Similarly, HellaSwag Ctrl AUROC (0.90) exceeds Theory Pred (0.89) while MMLU Ctrl AUROC (0.94) is below Theory Pred (0.97). The inconsistent direction suggests the power function may not fully capture controlled-experiment dynamics.
- Section 3 mentions "Stage 2: 4PL parameter estimation" using MML-EM via ltm R package, but the ltm package implements 2PL, not 4PL. This needs clarification — was a different package used, or were c and d parameters fixed/estimated separately?
- Type-I error rate not reported explicitly. Table 5 shows AUROC but not false alarm rates at specified α levels.
- The paper mentions "3 seeds per cell" but doesn't report seed-to-seed variance systematically. Table 1 (pilot) shows std, but Tables 2–3 show only point estimates.

---

### F. Questions for Authors

1. **Clean-clean calibration**: What is the distribution of Δlz* between two independently-trained clean SFT models? The reported Δlz*=0.70 suggests non-zero baseline drift — is this within the expected range of SFT stochasticity, and how does the detection threshold account for it?

2. **IRT parameter source**: Are the 4PL parameters from an existing human-calibrated item bank (PSN-IRT), or estimated from LLM response data using ltm? If the latter, local independence violations in LLM responses could compromise parameter accuracy.

3. **Leaderboard flagging threshold sensitivity**: How does the 8.3% flagging rate change if you vary the threshold from 2 SD to 1.5 SD or 3 SD? Is the temporal trend robust to threshold choice?

4. **Pre-training contamination**: Could you discuss whether the localized aberrance pattern (Table 13) would hold for pre-training-based contamination, where gradient updates are distributed across the full parameter space rather than concentrated in QLoRA adapters?

5. **Post-RL mechanism**: You argue binary patterns are robust to RL because "as long as contaminated items are still answered correctly, the aberrant pattern persists." But RL could also change which items are answered correctly (through exploration). Do you observe any accuracy degradation on contaminated items post-RL?

---

### G. Missing Experiments / Coverage Gaps

| Experiment | Status | Depth Assessment |
|---|---|---|
| ctrl-contam pilot | ✅ Present (Sec 4.1, Table 1) | Good: 3 levels × 3 seeds, clear go/no-go |
| ctrl-contam full | ✅ Present (Sec 4.2, Tables 2–3) | Excellent: 4 models × 6 levels × 3 benchmarks, complete AUROC matrix |
| Baseline comparison | ✅ Present (Sec 6, Tables 5–6) | Good: 3 methods compared, information access table included. Missing simpler binary-only baselines (accuracy z-score, n-gram overlap) — only gray-box comparisons shown |
| Post-RL signal retention | ✅ Present (Sec 7, Tables 7–8) | Excellent: Direct comparison with Min-K%++, clear mechanistic explanation |
| Multiscale lzm | ✅ Present (Sec 9.1, Table 12) | Adequate: Results reported but compressed into ~5 lines. Marginal improvement (+2-5pp) appropriately noted |
| Extended benchmarks | ✅ Present (Sec 5.1, Table 4) | Good: BBH + MATH added, R²=0.94 validated |
| Natural experiment | ⚠️ Not found in PDF | Director's summary mentions 5 base→chat pairs (Sec 5.11) but this is absent from the paper. This is a gap — natural experiment would provide quasi-causal evidence complementing controlled experiments |
| v1 IRT Refit | ⚠️ Not found in PDF | Director mentions structural failure (a_r plateau at N≈450, Sec 5.10) but this is absent. This negative result would be valuable to report |
| 4PL vs 3PL ablation | ✅ Present (Sec 9.3, Table 14) | Good: 5 benchmark comparison, marginal improvement confirmed |
| Domain-level analysis | ✅ Present (Sec 9.2, Table 13) | Adequate: 4 supercategories shown, localized contamination pattern demonstrated |
| θ-fixed dose-response | ⚠️ Not clearly present | Director mentions this as Sec 5.3 but PDF has "Dual-Regime Signal Structure" in Sec 5.2, which is related but different. The θ-fixed concept (controlling for ability gain to isolate aberrance) is not explicitly developed |
| Memorization fraction | ⚠️ Mentioned but underdeveloped | Concept appears in pilot but not quantified per-model as the Director's summary suggests |

**Summary**: 7/11 experiments clearly present and adequately developed. 4 experiments (natural experiment, IRT refit, θ-fixed analysis, memorization fraction) are either absent or underdeveloped relative to the Director's description. The 4 missing/weak experiments would strengthen the paper but are not strictly necessary for the core claims. The most impactful omission is the **natural experiment** (would provide real-world validation) and the **IRT refit failure** (would inform practitioners about method limitations on archival data without pre-existing IRT parameters).

---

### H. Overall Assessment: 3.5 / 5 (Borderline Conference)

**Calibration reasoning:**

The paper makes a genuine contribution at the intersection of IRT and LLM evaluation. The controlled experiment results are strong (AUROC 0.94 on MMLU at 15%), the post-RL robustness finding is novel and addresses an open problem, and the leaderboard audit is unprecedented in scale. The power function provides predictive theory.

However:
- **1 Major weakness** [idea]: Leaderboard audit validation gap (W2) — the paper's applied headline (8.3% flagging) lacks ground-truth validation. This affects Contribution 3 but not Contributions 1–2.
- **1 Major weakness** [presentation]: 14 tables/0 figures/7 references (W1) is a serious presentation issue that would disadvantage the paper in ARR review. This is fixable but in current form hurts readability significantly.
- **1 Should-Fix** [idea]: Single contamination mechanism (W3) limits generalizability.
- **1 Should-Fix** [presentation]: Missing experiments from design (W4).

Per calibration rules: 1 idea-level Major (W2) → cap at Accept (4.0). Combined with the severe presentation weakness (W1) and format borderline violation, the score drops to 3.5 (Borderline Conference).

**Path to 4.0 (Conference):**
1. Add 3–4 figures (detection frontier diagram, dose-response curves, temporal trend, domain heatmap)
2. Expand references to ≥20
3. Add leaderboard flagging threshold sensitivity analysis
4. Trim main text to 8 pages (move lzm and 4PL ablation to appendix)
5. Add natural experiment or external validation of flagging accuracy

**Recommendation**: Borderline Accept. The core science is sound and the post-RL finding is exciting. With presentation improvements and validation of the leaderboard audit, this could reach Conference level.

---

### I. Confidence: 4 / 5

Familiar with IRT/person-fit literature, contamination detection methods (ConStat, Min-K%++, CoDeC), and LLM evaluation practices. Less confident about the specific IRT parameter estimation pipeline (ltm package capabilities for 4PL) and the Open LLM Leaderboard data format details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-20T19:48:53.098443+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-20T19:48:53.149031+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-20T19:49:39.071752+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "text": "## 交叉分享：R1 对 Best 档的完整审稿（评分 3.5 Borderline Conference）\n\nR1 已完成全部三档 dream paper 审稿。Best 档评分 3.5，显著高于 Median (3.0) 和 Worst (2.5)。请审阅 R1 的 Best 档评分和发现，给出交叉回应。\n\n**Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n\n---\n\n### Best 档关键数据（与你此前评估的 Median/Worst 档对比）\n\n| 指标 | Best | Median | Worst |\n|------|------|--------|-------|\n| AUROC @15% MMLU | **0.94** | 0.78 | 0.61 |\n| Post-RL AUROC | **0.88 (63% retention)** | 0.56 (19%) | ≈0 |\n| Leaderboard flagging | **8.3% (population-based)** | 高但有 baseline 问题 | 96-99% |\n| Controlled experiment | **4×6×3×3=216 runs** | 较少 | 较少 |\n| Power function R² | 0.94 | 0.96 | 0.96 |\n| Framing | Positive: detection tool | Mixed | Negative: impossibility |\n\n### R1 的评分和维度打分\n- **Overall: 3.5** (Borderline Conference)\n- Soundness: 3.5/5\n- Excitement: 3.5/5\n- Reproducibility: 3/5\n- Confidence: 4/5\n\n### R1 的主要优势认定\n\n**S1 [最突出]**: Post-RL robustness（AUROC 0.88 vs Min-K%++ 0.58）——直接解决 Wang et al. (2025) 的 open problem，机制解释清晰（binary patterns 对 RL 概率重分布 robust）。R1 认为\"this finding alone may merit Findings-level publication\"。\n\n**S2**: 完整 factorial 实验（4 models × 6 levels × 3 benchmarks × 3 seeds = 216 runs），AUROC 0.94 at 15% MMLU，所有 4 个模型 AUROC ≥0.91。\n\n**S3**: Power function（R²=0.94）with BBH/MATH out-of-sample validation，提供可预测理论。\n\n**S4**: 11,200 模型 leaderboard audit with population-based flagging（θ±0.5 bin, |Δlz*|>2SD），方法论上优于绝对阈值。\n\n**S5**: 诚实呈现 GSM8K 低 power (AUROC 0.72 at n=1,319)。\n\n### R1 的主要弱点\n\n**W1 [presentation, Major]**: 14 tables, 0 figures, ~7 references。无任何可视化，参考文献极度稀疏。R1 认为这是\"serious presentation weakness that would disadvantage the paper in peer review\"。\n\n**W2 [idea, Major]**: Leaderboard audit 无 ground-truth validation。8.3% flagging rate 的 false positive rate 未知。temporal trend 有替代解释（model capability increase → more extreme misfit）。\n\n**W3 [idea, Should-Fix]**: 单一污染机制（QLoRA SFT）。但 Best 档的 scope 限定比 Worst 档更审慎（\"SFT-style contamination\"）。\n\n**W4 [presentation, Should-Fix]**: Design document 中的部分实验缺失（natural experiment、IRT refit、θ-fixed analysis、memorization fraction）。\n\n### R1 的格式/合规检查\n- ⚠️ 正文约 9 页，超 8-page limit ~0.5 页（borderline violation）\n- ~7 篇参考文献——跨学科论文远远不够\n- Limitations 是 Discussion 内的 subsection 而非独立 section\n\n### R1 升级路径（3.5 → 4.0 Conference）\n1. 加 3-4 张 figures\n2. 参考文献扩充至 ≥20\n3. 加 leaderboard flagging threshold sensitivity analysis\n4. 正文压缩至 8 页（lzm 和 4PL ablation 移至 appendix）\n5. 加 natural experiment 或 flagging accuracy 的外部验证\n\n---\n\n### 需要你回应的关键问题\n\n1. **你对 Best 档的评分是多少？** R1 给 3.5，你此前对 Median 给 3.0。Best 档的 AUROC 0.94（vs Median 0.78）、post-RL 0.88（vs 0.56）、population-based flagging 8.3%（vs 高 flagging rate）是否足以让你提升评分？\n\n2. **你此前的 systematic positive bias 关切在 Best 档中是否仍然成立？** Best 档使用 population-based flagging（ability-matched peer comparison），可能比 absolute lz* 更好地应对了 bias 问题。\n\n3. **R1 认为 post-RL robustness \"alone may merit Findings-level publication\"。你是否同意？** 这在 Median/Worst 档中不成立（post-RL 分别 0.56 和 ≈0），但 Best 档 0.88 是一个 strong result。\n\n4. **14 tables / 0 figures / 7 references 的 presentation 问题在你看来有多严重？** R1 将其列为 Major weakness。\n\n5. **你对 Best 档三个版本的综合排序是？** 请给出你认为的最终评分范围。\n\n请逐条回应，给出 Best 档评分和简要理由。",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "text": "## 交叉分享：R1 对 Best 档的完整审稿（评分 3.5 Borderline Conference）\n\nR1 已完成全部三档 dream paper 审稿。Best 档评分 3.5，显著高于 Median (3.0) 和 Worst (2.5)。请审阅 R1 的 Best 档评分和发现，给出交叉回应。\n\n**Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n\n---\n\n### Best 档关键数据（与你此前评估的 Median/Worst 档对比）\n\n| 指标 | Best | Median | Worst |\n|------|------|--------|-------|\n| AUROC @15% MMLU | **0.94** | 0.78 | 0.61 |\n| Post-RL AUROC | **0.88 (63% retention)** | 0.56 (19%) | ≈0 |\n| Leaderboard flagging | **8.3% (population-based)** | 高但有 baseline 问题 | 96-99% |\n| Controlled experiment | **4×6×3×3=216 runs** | 较少 | 较少 |\n| Power function R² | 0.94 | 0.96 | 0.96 |\n| Framing | Positive: detection tool | Mixed | Negative: impossibility |\n\n### R1 的评分和维度打分\n- **Overall: 3.5** (Borderline Conference)\n- Soundness: 3.5/5\n- Excitement: 3.5/5\n- Reproducibility: 3/5\n- Confidence: 4/5\n\n### R1 的主要优势认定\n\n**S1 [最突出]**: Post-RL robustness（AUROC 0.88 vs Min-K%++ 0.58）——直接解决 Wang et al. (2025) 的 open problem，机制解释清晰（binary patterns 对 RL 概率重分布 robust）。R1 认为\"this finding alone may merit Findings-level publication\"。\n\n**S2**: 完整 factorial 实验（4 models × 6 levels × 3 benchmarks × 3 seeds = 216 runs），AUROC 0.94 at 15% MMLU，所有 4 个模型 AUROC ≥0.91。\n\n**S3**: Power function（R²=0.94）with BBH/MATH out-of-sample validation，提供可预测理论。\n\n**S4**: 11,200 模型 leaderboard audit with population-based flagging（θ±0.5 bin, |Δlz*|>2SD），方法论上优于绝对阈值。\n\n**S5**: 诚实呈现 GSM8K 低 power (AUROC 0.72 at n=1,319)。\n\n### R1 的主要弱点\n\n**W1 [presentation, Major]**: 14 tables, 0 figures, ~7 references。无任何可视化，参考文献极度稀疏。R1 认为这是\"serious presentation weakness that would disadvantage the paper in peer review\"。\n\n**W2 [idea, Major]**: Leaderboard audit 无 ground-truth validation。8.3% flagging rate 的 false positive rate 未知。temporal trend 有替代解释（model capability increase → more extreme misfit）。\n\n**W3 [idea, Should-Fix]**: 单一污染机制（QLoRA SFT）。但 Best 档的 scope 限定比 Worst 档更审慎（\"SFT-style contamination\"）。\n\n**W4 [presentation, Should-Fix]**: Design document 中的部分实验缺失（natural experiment、IRT refit、θ-fixed analysis、memorization fraction）。\n\n### R1 的格式/合规检查\n- ⚠️ 正文约 9 页，超 8-page limit ~0.5 页（borderline violation）\n- ~7 篇参考文献——跨学科论文远远不够\n- Limitations 是 Discussion 内的 subsection 而非独立 section\n\n### R1 升级路径（3.5 → 4.0 Conference）\n1. 加 3-4 张 figures\n2. 参考文献扩充至 ≥20\n3. 加 leaderboard flagging threshold sensitivity analysis\n4. 正文压缩至 8 页（lzm 和 4PL ablation 移至 appendix）\n5. 加 natural experiment 或 flagging accuracy 的外部验证\n\n---\n\n### 需要你回应的关键问题\n\n1. **你对 Best 档的评分是多少？** R1 给 3.5，你此前对 Median 给 3.0。Best 档的 AUROC 0.94（vs Median 0.78）、post-RL 0.88（vs 0.56）、population-based flagging 8.3%（vs 高 flagging rate）是否足以让你提升评分？\n\n2. **你此前的 systematic positive bias 关切在 Best 档中是否仍然成立？** Best 档使用 population-based flagging（ability-matched peer comparison），可能比 absolute lz* 更好地应对了 bias 问题。\n\n3. **R1 认为 post-RL robustness \"alone may merit Findings-level publication\"。你是否同意？** 这在 Median/Worst 档中不成立（post-RL 分别 0.56 和 ≈0），但 Best 档 0.88 是一个 strong result。\n\n4. **14 tables / 0 figures / 7 references 的 presentation 问题在你看来有多严重？** R1 将其列为 Major weakness。\n\n5. **你对 Best 档三个版本的综合排序是？** 请给出你认为的最终评分范围。\n\n请逐条回应，给出 Best 档评分和简要理由。",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-20T19:49:42.792487+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3720
}
```

</details>

---


### Assistant

_source line 117 · 2026-05-20T19:49:49.505506+00:00_

交叉分享已发送给 R2。等待 R2 对 Best 档的交叉回应，然后合成覆盖全部三档的最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 118 · 2026-05-20T19:49:52.062748+00:00_

[Reviewer 1 审稿结果]:
三篇 Dream 论文的审稿已全部完成并提交给 Director：

| 论文版本 | Overall | 关键判断 |
|--------|---------|--------|
| **Median** (Detection Frontier) | 3.0 (Findings) | 2 Major: leaderboard audit baseline chicken-and-egg + post-RL scope gap |
| **Worst** (Binary Response Bottleneck) | 2.5 (Borderline Findings) | 2 Major: overclaimed info-theoretic bound + 单一污染机制 |
| **Best** (IRT-FIT full version) | 3.5 (Borderline Conference) | 1 Major (idea): leaderboard audit validation gap; 1 Major (presentation): 14 tables/0 figures/7 references |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 119 · 2026-05-20T19:49:56.423878+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 16

## Round 16

6 recorded events


### User

_source line 120 · 2026-05-20T19:51:14.613513+00:00_

[Reviewer 2 审稿意见]:
## R2 对 R1 Best 档审稿的交叉回应

---

### Q1: Best 档评分

**R2 评分：3.5 (Borderline Conference)**，与 R1 一致。

Best 档相对 Median 档有质的提升，不仅是数字改善：

- **AUROC 0.94 vs 0.78**：从"勉强可用"到"实际有效"的跨越。4 个模型均 ≥0.91 说明结果 robust，不是靠个别模型拉高均值
- **Post-RL 0.88 (63% retention) vs 0.56 (19%)**：这是最关键的变化。Median 档的 post-RL 几乎失效是我此前最大的关切之一，Best 档彻底改变了这个判断
- **Population-based flagging 8.3% vs 96-99%**：从"标记一切"（无鉴别力）到"合理比例"（有鉴别力）
- **216 runs factorial design**：4×6×3×3 是 proper experimental design，不再是"两个 model family 不够"的问题
- **Framing**：定位为 detection tool 而非 impossibility result，避免了 Worst 档的 overclaim 问题

这些改善直接回应了我和 R1 在 Median/Worst 档中提出的多个 critical issues。

---

### Q2: Systematic Positive Bias 在 Best 档中是否仍成立？

**大幅缓解，但未完全消解。**

Population-based flagging（ability-matched θ±0.5 bin, |Δlz*|>2SD）是一个聪明的方法论改进：
- 不再依赖 lz* 的绝对值与理论 null distribution（均值 0，方差 1）的比较——这在 LLM population 中已被证明不成立
- 改为同 ability bin 内的 peer comparison，systematic bias（无论正向还是负向）在同 bin 内近似常数，被 Δlz* 差分消除
- 这在设计思路上类似 difference-in-differences，比 absolute thresholding 健壮得多

**残存问题**：
- 如果 systematic bias 的幅度与 ability 相关（非常可能——high-ability 模型的 response pattern 可能比 low-ability 模型更偏离 IRT 假设），bin 内差分不能完全消除 bias
- θ±0.5 bin 宽度的选择是否敏感？论文是否做了 sensitivity analysis？
- 但总体而言，这是一个合理的工程化解决方案，将问题从 "showstopper" 降级为 "should-investigate"

---

### Q3: Post-RL Robustness 是否 alone merit Findings？

**同意。** 理由：

1. **实际价值明确**：当前 contamination detection 方法（Min-K%++、perplexity-based 等）普遍在 post-RL 模型上失效是 known open problem（Wang et al. 2025）。AUROC 0.88 vs Min-K%++ 0.58 是有意义的 margin
2. **机制解释有洞察力**：binary response patterns 对 RL 的概率重分布 robust，因为 RL 改变的是 token-level probability distribution，但 argmax 后的 correct/incorrect 二值判断相对稳定。这不是一个 trivial 的观察——它指出了 binary-level 和 probability-level 方法在 RL robustness 上的结构性差异
3. **可验证性强**：这个 claim 可以被独立验证（对任意 pre-RL/post-RL model pair 计算 binary response agreement），reproducibility 门槛低

单独这个发现确实达到了 Findings 门槛。它为 contamination detection 社区提供了一个新的 design principle：如果关注 post-RL robustness，应优先考虑 binary-level 而非 probability-level 信号。

---

### Q4: 14 Tables / 0 Figures / 7 References 的严重程度

**Major weakness，同意 R1 的判断。** 在实际 peer review 中这会是一个高摩擦点。

**0 Figures**：
- 14 张表格 + 0 张图 = 读者认知负担极高。Power function、AUROC curves、leaderboard temporal trends、ability distribution 这些结果天然适合可视化
- 在 EMNLP 审稿中，reviewer 通常在 15-30 分钟内形成初步印象。纯表格论文在这个时间窗口内很难被有效消化
- 至少需要 3-4 张图：(1) AUROC vs contamination level curves, (2) power function fit, (3) leaderboard Δlz* distribution/temporal trend, (4) post-RL robustness comparison

**7 References**：
- 这是我认为**比 R1 评估更严重**的问题。一篇跨 IRT 和 LLM evaluation 的论文，至少需要覆盖：
  - IRT 和 person-fit 基础文献（Drasgow, Levine & Williams 1985; Meijer & Sijtsma 2001 等）
  - LLM contamination detection（Shi et al. 2023; Oren et al. 2023; Golchin & Surdeanu 2024 等）
  - Benchmark integrity（Zhou et al. 2023; Jacobs et al. 2024 等）
  - LLM evaluation methodology
- 7 篇引用在任何 venue 都是 red flag，会让 reviewer 质疑作者是否了解 related work landscape
- 这不仅是 presentation 问题——是 scholarly completeness 问题

**Page limit**：
- ~9 页正文超限 ~0.5 页，在 ARR 审稿中可能被 desk reject 或至少被标记。lzm 和 4PL ablation 应移至 appendix

---

### Q5: 三档综合排序和最终评分

| 版本 | R2 评分 | R1 评分 | 核心判断 |
|------|---------|---------|----------|
| **Best** | **3.5** | 3.5 | 实证结果强，post-RL 贡献突出，但 presentation 拖后腿 |
| **Median** | **3.0** | 3.0 | 方法有价值，但 calibration 和实验完整性问题制约 |
| **Worst** | **2.5** | 2.5 | Overclaim + 实证不足，negative result 框架下 novelty 有限 |

关于 Worst 档：我此前维持 3.0，但经过与 R1 的交叉讨论（特别是 N1 overclaim 和 N2 单一机制问题），我修正为 **2.5**，与 R1 一致。概念框架的独立价值不足以在 Worst 档的 framing 下支撑 Findings 接收。

**Best 档升级路径（3.5 → 4.0）**：同意 R1 的建议，优先级排序如下：
1. **[P0]** 加 3-4 张 figures（AUROC curves, power function, leaderboard distribution, post-RL comparison）
2. **[P0]** 参考文献扩充至 ≥25（IRT + contamination + evaluation 三个领域各 5-8 篇核心文献）
3. **[P0]** 正文压缩至 8 页（移 ablation 至 appendix）
4. **[P1]** Leaderboard flagging threshold sensitivity analysis + 至少一个 external validation
5. **[P2]** 加 alternative binary-only baseline（even a simple ML classifier）以加强 "binary signal is sufficient" 的 claim

R2 交叉回应完毕。三档评分与 R1 完全一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-20T19:52:32.445584+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "## Dream Review Round 1 — Issue Tracker (Final, 3-version coverage)\n## Best / Median / Worst 三档共 16 个 issues\n\n# ===== BEST 档 Issues =====\n\n- id: \"BEST-W1\"\n  summary: \"14 tables, 0 figures, ~7 references — presentation 严重不足，跨学科论文参考文献极度稀疏\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Major presentation weakness。R2 AGREE 并认为 7 references 比 R1 评估更严重——是 scholarly completeness 问题而非单纯 presentation。\"\n  action_items:\n    - round: 1\n      action: \"加 3-4 张 figures (AUROC curves, power function fit, leaderboard distribution, post-RL comparison)；参考文献扩充至 ≥25\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W2\"\n  summary: \"Leaderboard audit (11,200 models, 8.3% flagging) 无 ground-truth validation，false positive rate 未知\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 idea-level Major。仅 GSM8K 一个外部 corroboration 点。temporal trend 有替代解释（model capability increase）。\"\n  action_items:\n    - round: 1\n      action: \"加 threshold sensitivity analysis (1.5/2/3 SD)；加至少一个 external validation；讨论 temporal trend 替代解释\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W3\"\n  summary: \"单一污染机制 (QLoRA SFT)，scope 限定审慎但仍限制泛化性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Best 档的 scope 限定 (SFT-style contamination) 比 Worst 档审慎，但仍是 should-fix。\"\n  action_items:\n    - round: 1\n      action: \"讨论 pre-training contamination 的 response pattern 差异；如可能加一种替代污染机制实验\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W4\"\n  summary: \"Design document 中 4 个实验缺失 (natural experiment, IRT refit, θ-fixed analysis, memorization fraction)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"7/11 实验 present，4 个缺失/underdeveloped。最有影响的缺失：natural experiment（real-world validation）和 IRT refit failure（practitioner guidance）。\"\n  action_items:\n    - round: 1\n      action: \"优先补充 natural experiment (base→chat pairs)；报告 IRT refit negative result\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-F1\"\n  summary: \"正文 ~9 页超 8-page limit ~0.5 页，borderline violation\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 建议移 lzm 和 4PL ablation 至 appendix 以压缩正文。\"\n  action_items:\n    - round: 1\n      action: \"正文压缩至 8 页（Section 9 Additional Analyses 移至 appendix）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W5\"\n  summary: \"Clean-clean Δlz*≈0.70 的 baseline drift 需更多讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"非零 baseline shift 是否在 SFT stochasticity 的预期范围内？detection threshold 是否设在此 noise floor 之上？\"\n  action_items:\n    - round: 1\n      action: \"报告 clean-clean Δlz* 分布；确认 threshold 高于 noise floor\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W6\"\n  summary: \"缺少 binary-only baseline (accuracy z-score / ML classifier on binary vectors)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"论文仅与 gray-box methods 比较（ConStat, Min-K%++），缺少同 information level 的 binary-only baseline。\"\n  action_items:\n    - round: 1\n      action: \"加至少一个 simple binary-only baseline 以验证 IRT 框架的附加价值\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== MEDIAN 档 Issues =====\n\n- id: \"MED-N1\"\n  summary: \"Leaderboard audit 的 Δlz* baseline (per-family median) 存在 chicken-and-egg 问题\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。若整个 family 被污染则 baseline 有偏。Best 档通过 population-based flagging 缓解了此问题。\"\n  action_items:\n    - round: 1\n      action: \"采用 Best 档的 population-based flagging 方法替代 per-family median\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-N2\"\n  summary: \"Post-RL AUROC 0.56 (retention 19%) 与 leaderboard audit 覆盖 post-RL 模型的范围矛盾\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。Best 档 post-RL 0.88 缓解了此问题。\"\n  action_items:\n    - round: 1\n      action: \"确保 post-RL results 达到 Best 档水平（AUROC ≥0.85）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== WORST 档 Issues =====\n\n- id: \"WORST-N1\"\n  summary: \"Information-theoretic lower bound claim overclaim — 仅测试 lz* 一种统计量即推断所有 binary-only 方法不可能\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。binary response vector 包含 lz* 未利用的 higher-order patterns。\"\n  action_items:\n    - round: 1\n      action: \"放弃 impossibility framing；采用 Best 档的 positive detection tool framing\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"WORST-N2\"\n  summary: \"单一污染机制 (QLoRA SFT) 不足以支撑 fundamental bottleneck 结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。pre-training memorization 可能产生 classic aberrant pattern，lz* 可能有效。\"\n  action_items:\n    - round: 1\n      action: \"避免 bottleneck 叙事；限定 scope 为 SFT-style contamination\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== 跨档 Issues =====\n\n- id: \"ALL-W1\"\n  summary: \"Systematic positive bias / IRT model fundamental misfit for LLM — Best 档通过 population-based flagging 大幅缓解\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提为 showstopper → R1 REBUT (Δlz* 设计应对) → R2 降级为 warning。Best 档 population-based flagging 进一步缓解但未完全消解（bias 可能与 ability 相关）。\"\n  action_items:\n    - round: 1\n      action: \"验证 population-based flagging 的 θ bin 宽度 sensitivity；报告 empirical null distribution 诊断\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W2\"\n  summary: \"Incomplete tables / 选择性展示部分数据\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提，R1 AGREE。Gemma 缺条件、lzm 5/12 models、two-sided 5/60 pairs。\"\n  action_items:\n    - round: 1\n      action: \"补全所有表格或明确说明 dream report 生成限制\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W3\"\n  summary: \"IRT 参数质量 (PSN-IRT 来源) sensitivity analysis 缺失\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。ltm R package 实现 2PL 非 4PL，c/d 参数来源需 clarify。\"\n  action_items:\n    - round: 1\n      action: \"澄清 4PL 参数估计细节；进行 parameter sensitivity analysis\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-F1\"\n  summary: \"Limitations 应为独立 section（EMNLP 2026 mandatory）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"当前为 Discussion 内 subsection，部分 AC 可能 flag。\"\n  action_items:\n    - round: 1\n      action: \"改为独立 Limitations section\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "## Dream Review Round 1 — Issue Tracker (Final, 3-version coverage)\n## Best / Median / Worst 三档共 16 个 issues\n\n# ===== BEST 档 Issues =====\n\n- id: \"BEST-W1\"\n  summary: \"14 tables, 0 figures, ~7 references — presentation 严重不足，跨学科论文参考文献极度稀疏\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Major presentation weakness。R2 AGREE 并认为 7 references 比 R1 评估更严重——是 scholarly completeness 问题而非单纯 presentation。\"\n  action_items:\n    - round: 1\n      action: \"加 3-4 张 figures (AUROC curves, power function fit, leaderboard distribution, post-RL comparison)；参考文献扩充至 ≥25\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W2\"\n  summary: \"Leaderboard audit (11,200 models, 8.3% flagging) 无 ground-truth validation，false positive rate 未知\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 idea-level Major。仅 GSM8K 一个外部 corroboration 点。temporal trend 有替代解释（model capability increase）。\"\n  action_items:\n    - round: 1\n      action: \"加 threshold sensitivity analysis (1.5/2/3 SD)；加至少一个 external validation；讨论 temporal trend 替代解释\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W3\"\n  summary: \"单一污染机制 (QLoRA SFT)，scope 限定审慎但仍限制泛化性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Best 档的 scope 限定 (SFT-style contamination) 比 Worst 档审慎，但仍是 should-fix。\"\n  action_items:\n    - round: 1\n      action: \"讨论 pre-training contamination 的 response pattern 差异；如可能加一种替代污染机制实验\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W4\"\n  summary: \"Design document 中 4 个实验缺失 (natural experiment, IRT refit, θ-fixed analysis, memorization fraction)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"7/11 实验 present，4 个缺失/underdeveloped。最有影响的缺失：natural experiment（real-world validation）和 IRT refit failure（practitioner guidance）。\"\n  action_items:\n    - round: 1\n      action: \"优先补充 natural experiment (base→chat pairs)；报告 IRT refit negative result\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-F1\"\n  summary: \"正文 ~9 页超 8-page limit ~0.5 页，borderline violation\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 建议移 lzm 和 4PL ablation 至 appendix 以压缩正文。\"\n  action_items:\n    - round: 1\n      action: \"正文压缩至 8 页（Section 9 Additional Analyses 移至 appendix）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W5\"\n  summary: \"Clean-clean Δlz*≈0.70 的 baseline drift 需更多讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"非零 baseline shift 是否在 SFT stochasticity 的预期范围内？detection threshold 是否设在此 noise floor 之上？\"\n  action_items:\n    - round: 1\n      action: \"报告 clean-clean Δlz* 分布；确认 threshold 高于 noise floor\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W6\"\n  summary: \"缺少 binary-only baseline (accuracy z-score / ML classifier on binary vectors)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"论文仅与 gray-box methods 比较（ConStat, Min-K%++），缺少同 information level 的 binary-only baseline。\"\n  action_items:\n    - round: 1\n      action: \"加至少一个 simple binary-only baseline 以验证 IRT 框架的附加价值\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== MEDIAN 档 Issues =====\n\n- id: \"MED-N1\"\n  summary: \"Leaderboard audit 的 Δlz* baseline (per-family median) 存在 chicken-and-egg 问题\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。若整个 family 被污染则 baseline 有偏。Best 档通过 population-based flagging 缓解了此问题。\"\n  action_items:\n    - round: 1\n      action: \"采用 Best 档的 population-based flagging 方法替代 per-family median\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-N2\"\n  summary: \"Post-RL AUROC 0.56 (retention 19%) 与 leaderboard audit 覆盖 post-RL 模型的范围矛盾\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。Best 档 post-RL 0.88 缓解了此问题。\"\n  action_items:\n    - round: 1\n      action: \"确保 post-RL results 达到 Best 档水平（AUROC ≥0.85）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== WORST 档 Issues =====\n\n- id: \"WORST-N1\"\n  summary: \"Information-theoretic lower bound claim overclaim — 仅测试 lz* 一种统计量即推断所有 binary-only 方法不可能\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。binary response vector 包含 lz* 未利用的 higher-order patterns。\"\n  action_items:\n    - round: 1\n      action: \"放弃 impossibility framing；采用 Best 档的 positive detection tool framing\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"WORST-N2\"\n  summary: \"单一污染机制 (QLoRA SFT) 不足以支撑 fundamental bottleneck 结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。pre-training memorization 可能产生 classic aberrant pattern，lz* 可能有效。\"\n  action_items:\n    - round: 1\n      action: \"避免 bottleneck 叙事；限定 scope 为 SFT-style contamination\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== 跨档 Issues =====\n\n- id: \"ALL-W1\"\n  summary: \"Systematic positive bias / IRT model fundamental misfit for LLM — Best 档通过 population-based flagging 大幅缓解\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提为 showstopper → R1 REBUT (Δlz* 设计应对) → R2 降级为 warning。Best 档 population-based flagging 进一步缓解但未完全消解（bias 可能与 ability 相关）。\"\n  action_items:\n    - round: 1\n      action: \"验证 population-based flagging 的 θ bin 宽度 sensitivity；报告 empirical null distribution 诊断\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W2\"\n  summary: \"Incomplete tables / 选择性展示部分数据\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首提，R1 AGREE。Gemma 缺条件、lzm 5/12 models、two-sided 5/60 pairs。\"\n  action_items:\n    - round: 1\n      action: \"补全所有表格或明确说明 dream report 生成限制\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W3\"\n  summary: \"IRT 参数质量 (PSN-IRT 来源) sensitivity analysis 缺失\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 AGREE。ltm R package 实现 2PL 非 4PL，c/d 参数来源需 clarify。\"\n  action_items:\n    - round: 1\n      action: \"澄清 4PL 参数估计细节；进行 parameter sensitivity analysis\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-F1\"\n  summary: \"Limitations 应为独立 section（EMNLP 2026 mandatory）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"当前为 Discussion 内 subsection，部分 AC 可能 flag。\"\n  action_items:\n    - round: 1\n      action: \"改为独立 Limitations section\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-20T19:52:32.547669+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 8560}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-20T19:54:47.295247+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告（最终版）：irt_personfit_contam Dream Papers — 三档综合评估\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n**Round**: 1\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)\n**收敛状态**: 三档评分完全一致（R1 = R2），无未解决分歧\n\n⚠️ **本报告替换此前两次提交**（第一次误基于 Best 档 paper.tex；第二次仅覆盖 Median/Worst）。本版覆盖全部三档 dream paper。\n\n---\n\n## 评分总览\n\n| 档位 | 标题 | R1 | R2 | 共识 | EMNLP 2026 ARR 含义 |\n|------|------|----|----|------|-------------------|\n| **Best** | IRT-FIT (full version) | **3.5** | **3.5** | ✅ | Borderline Conference — 有潜力进主会议 |\n| **Median** | Characterizing the Detection Frontier | **3.0** | **3.0** | ✅ | Findings — 可被 Findings 接收 |\n| **Worst** | The Binary Response Bottleneck | **2.5** | **2.5** | ✅ | Borderline Findings — 需大幅修改 |\n\n**评分范围 2.5–3.5，中位 3.0。**\n\n---\n\n## 跨档对比：什么决定了评分差异\n\n| 维度 | Best (3.5) | Median (3.0) | Worst (2.5) |\n|------|-----------|-------------|-------------|\n| AUROC @15% MMLU | **0.94** | 0.78 | 0.61 |\n| Post-RL AUROC | **0.88 (63%)** | 0.56 (19%) | ≈0 |\n| 实验规模 | **4×6×3×3=216 runs** | 较少 | 较少 |\n| Leaderboard 方法 | **Population-based 8.3%** | Per-family median, 有 bias | Absolute threshold, 96-99% |\n| Framing | **Detection tool** (审慎 scope) | Mixed | **Impossibility** (overclaim) |\n| 模型覆盖 | **4 models, 3 families** | 4 models | 2-4 models |\n| Power function R² | 0.94 | 0.96 | 0.96 |\n\n**关键发现**：评分差异主要由三个因素驱动：(1) post-RL robustness 是否有效，(2) leaderboard audit 方法论是否合理，(3) framing 是否审慎。理论贡献（power function）跨档稳定，不是差异来源。\n\n---\n\n## Best 档详评（3.5 — Borderline Conference）\n\n### Summary\nIRT-FIT 将心理测量学的 person-fit 统计量（lz*）应用于 LLM benchmark contamination 检测，定位为 minimal-information operating point（仅需 binary response）。4 个模型 × 6 污染水平 × 3 benchmarks × 3 seeds 的 factorial 实验产生 AUROC 0.94 at 15% MMLU（所有模型 ≥0.91）。Post-RL robustness 是最突出的发现（AUROC 0.88 vs Min-K%++ 0.58），机制解释清晰。11,200 模型 leaderboard audit 使用 population-based flagging 产生 8.3% flagging rate。Power function（R²=0.94）提供可预测理论。\n\n### Strengths\n\n**S1. Post-RL Robustness（R1, R2 共识：论文最突出贡献）。** AUROC 0.88 vs Min-K%++ 0.58，直接解决 Wang et al. (2025) 的 open problem。机制解释有洞察力：binary response patterns 对 RL 概率重分布 robust，因为 RL 改变 token-level probability distribution 但 argmax 后的 correct/incorrect 判断相对稳定。R1 认为 \"this finding alone may merit Findings-level publication\"，R2 同意。为 contamination detection 社区提供了新的 design principle。\n\n**S2. 严谨的 Factorial 实验设计。** 4 models × 6 contamination levels × 3 benchmarks × 3 seeds = 216 training runs。所有 4 个模型在 MMLU 15% contamination 下 AUROC ≥0.91，inter-model consistency 强。Table 2 完整 AUROC matrix 和 Table 3 Cohen's d matrix 透明可复现。\n\n**S3. Power Function 理论框架。** R²=0.94 across 7 benchmarks，BBH/MATH 作为 out-of-sample validation。为 practitioners 提供可操作的预测工具（如 \"n≥7,000 for 80% power at 15% contamination\"）。\n\n**S4. Leaderboard Audit 的方法论改进。** Population-based flagging（ability-matched θ±0.5 bin, |Δlz*|>2SD）在方法论上优于 absolute thresholds。8.3% flagging rate 有实际鉴别力（vs Worst 档 96-99% 无鉴别力）。11,200 模型的规模前所未有。\n\n**S5. Detection Frontier Framing。** Information access level 层级化（binary < binary+retest < token probs < training data < weights）清晰定位 IRT-FIT。Table 6 显示仅 5-6pp AUROC gap vs gray-box methods，compelling cost-benefit argument。\n\n**S6. 诚实呈现失败模式。** GSM8K 低 power（AUROC 0.72 at n=1,319）透明报告并用 power function 理论解释。\n\n### Weaknesses\n\n**W1. [Major/Presentation] 14 Tables, 0 Figures, ~7 References。**\n- 无任何可视化，认知负担极高。Power function、AUROC curves、leaderboard distribution、post-RL comparison 均天然适合图表\n- ~7 篇引用对跨 IRT + contamination + LLM evaluation 三领域的论文严重不足。缺少：Drasgow & Levine (1986) person-fit 基础、Meijer & Sijtsma (2001) person-fit survey、Karabatsos (2003) 非参数 person-fit、Oren et al. (2024) proving contamination、Shi et al. (2024) Min-K%++原文引用不足、Polo et al. (2024) tinyBenchmarks\n- R2 认为这超出 presentation 问题——是 **scholarly completeness** 缺失\n- **在 ARR 审稿中这会是高摩擦点**：reviewer 通常 15-30 分钟内形成初步印象，纯表格论文难以被有效消化\n\n**W2. [Major/Idea] Leaderboard Audit 无 Ground-Truth Validation。**\n- 8.3% flagging rate 的 false positive rate 未知\n- 仅 GSM8K 一个外部 corroboration 点（known data leakage alignment）\n- Temporal trend（+2.1pp/quarter）有替代解释：model capability increase → more extreme misfit，不一定反映真实 contamination 增长\n- 需 threshold sensitivity analysis 和更多 external validation\n\n**W3. [Should-Fix/Idea] 单一污染机制。**\n- QLoRA SFT 是唯一实验验证的途径。Pre-training contamination 的 learning dynamics 不同（gradient updates distributed across full parameter space vs QLoRA's low-rank adapters）\n- Best 档的 scope 限定（\"SFT-style contamination\"）比 Worst 档审慎，但仍限制实际应用范围\n\n**W4. [Should-Fix/Presentation] Design Document 中 4 个实验缺失。**\n- Natural experiment（5 base→chat pairs）、IRT refit failure（a_r plateau at N≈450）、θ-fixed dose-response analysis、memorization fraction 定量化\n- 最有影响的缺失：natural experiment（real-world validation）和 IRT refit failure（practitioner guidance on archival data limitations）\n\n**W5. [Minor] 格式问题。**\n- 正文 ~9 页超 8-page limit ~0.5 页（borderline violation）\n- Limitations 为 Discussion 内 subsection 而非独立 section\n- Clean-clean Δlz*≈0.70 baseline drift 未充分讨论\n\n### R1 Specific Technical Concerns\n- Table 4: GSM8K Ctrl AUROC (0.72) 大幅高于 Theory Pred (0.55)，HellaSwag Ctrl AUROC (0.90) > Theory Pred (0.89)，但 MMLU Ctrl AUROC (0.94) < Theory Pred (0.97)——方向不一致需解释\n- Section 3 提到用 ltm R package 做 4PL 参数估计，但 ltm 实现 2PL 非 4PL——c/d 参数来源需澄清\n- Type-I error rate 未显式报告；seed-to-seed variance 仅在 pilot table 有 std，full tables 只有 point estimates\n\n---\n\n## Median 档详评（3.0 — Findings）\n\n### 与 Best 档的关键差异\n1. **AUROC 下降至 0.78**：从\"实际有效\"退化为\"勉强可用\"\n2. **Post-RL 大幅衰减至 0.56**：基本失去 post-RL 检测能力，Best 档最突出的优势消失\n3. **Leaderboard audit 使用 per-family median baseline**：引入 chicken-and-egg 问题（W1-Median）\n\n### Critical Issues（Best 档不存在的问题）\n- **Baseline Chicken-and-Egg**：per-family median 假设 family 内 median 模型 \"clean\"，但若 base model training data 已含 benchmark items 则 baseline 有偏\n- **Post-RL Scope Gap**：AUROC 0.56 但 audit 仍覆盖 post-RL 模型，false negative rate 不可知\n- 这两个 critical issues 在 Best 档中被 population-based flagging 和 strong post-RL retention 缓解\n\n### 升级路径（3.0 → 3.5）\n- 采用 Best 档的 population-based flagging 方法\n- 提升 post-RL robustness 至 AUROC ≥0.85\n- 扩充实验规模至接近 Best 档水平\n\n---\n\n## Worst 档详评（2.5 — Borderline Findings）\n\n### 与 Best/Median 的关键差异\n1. **AUROC 仅 0.61**：检测力严重不足\n2. **Post-RL 信号基本消失**\n3. **96-99% flagging rate**：无任何鉴别力（universal model misfit）\n4. **Framing 为 negative result + overclaimed impossibility bound**\n\n### Critical Issues（Best/Median 档不存在的问题）\n- **Overclaimed Information-Theoretic Bound**：lz* 一种统计量的失败不等于所有 binary-only 方法的 fundamental impossibility。Binary response vector 包含 higher-order patterns，ML classifier 可能有效\n- **单一污染机制支撑 \"fundamental bottleneck\"**：QLoRA SFT 的泛化效应是 SFT-specific 的，pre-training memorization 可能产生 classic aberrant pattern\n\n### 升级路径（2.5 → 3.0）\n- 放弃 impossibility framing → 采用 Best 档的 positive detection tool framing\n- 测试 ≥1 alternative binary-only method（ML classifier on binary vectors）\n- 限定 scope 为 SFT-style contamination\n\n---\n\n## Questions for Authors\n\n**Q1.** Clean-clean Δlz* 的分布是什么？报告值 ≈0.70 是否在 SFT stochasticity 的预期范围内？Detection threshold 如何考虑此 noise floor？\n\n**Q2.** 4PL IRT 参数的确切来源？ltm R package 实现 2PL 非 4PL——c 和 d 参数是否另行估计？如果是，估计方法和数据是什么？\n\n**Q3.** Leaderboard flagging rate 对 threshold 选择的 sensitivity 如何？2SD → 1.5SD/3SD 变化后 8.3% 如何变化？Temporal trend 是否 robust？\n\n**Q4.** 能否讨论 pre-training contamination（非 SFT 注入）的 response pattern 预期？Table 13 的 \"localized aberrance\" 是否可能是 QLoRA low-rank constraint 的 artifact？\n\n**Q5.** Post-RL 实验中 RL 是否改变了 contaminated items 的 accuracy？如果 RL exploration 导致部分 contaminated items 被答错，binary pattern 是否仍然 robust？\n\n**Q6.** Abstract 中 AUROC 数字来自哪些具体条件？是否存在选择性报告（Best 档的 0.94 vs Median 的 0.78 vs Worst 的 0.61 差异很大，论文最终选择呈现哪个数字需要审慎）？\n\n---\n\n## Missing References（R1, R2 共识）\n\n跨学科论文至少需要覆盖三个领域的核心文献：\n\n**IRT / Person-Fit:**\n- Drasgow, Levine & Williams (1986) — person-fit 基础\n- Meijer & Sijtsma (2001) — person-fit survey\n- Karabatsos (2003) — 非参数 person-fit\n- Snijders (2001) — lz* 原文（已引但需更多 context）\n\n**Contamination Detection:**\n- Shi et al. (2024) — Min-K%++ 原文\n- Oren et al. (2024) — proving test set contamination\n- Golchin & Surdeanu (2024) — LLM contamination tracing\n- Magar & Schwartz (2022) — data contamination\n- Wang et al. (2025) — post-RL contamination（已引）\n\n**LLM Evaluation:**\n- Polo et al. (2024) — tinyBenchmarks\n- Zhou et al. (2023) — benchmark integrity\n- Jacobs et al. (2024) — psychometrics and AI\n\n---\n\n## External Review\n\n**外部审稿：未请求。**\n\n---\n\n## Visual Layout Check\n\n**视觉审查：未启动（not_started）。**\n\n---\n\n## Overall Assessment\n\n### 综合评分\n\n**Best 档 3.5 (Borderline Conference)** — 两位 Reviewer 一致。\n\n核心判断：post-RL robustness（AUROC 0.88 vs Min-K%++ 0.58）是 genuine advance，直接解决 open problem。Factorial 实验设计严谨（216 runs），power function 提供可预测理论，detection frontier framing 有概念价值。但 presentation 严重不足（14 tables / 0 figures / 7 references）在 ARR 审稿中会是高摩擦点，leaderboard audit 缺 ground-truth validation。\n\n**Median 档 3.0 (Findings)** — 两位 Reviewer 一致。\n\n理论贡献（power function, detection frontier）有价值，但 post-RL 衰减至 AUROC 0.56 消除了最大优势，leaderboard audit 的 baseline 方法论有 chicken-and-egg 问题。\n\n**Worst 档 2.5 (Borderline Findings)** — 两位 Reviewer 一致。\n\nOverclaimed impossibility bound 是核心逻辑缺陷。作为 negative result paper 的 novelty 有限——IRT 不适合 LLM 的结论对该领域研究者而言不完全意外。\n\n### Best 档升级路径（3.5 → 4.0 Conference）\n\n**P0（必须）：**\n1. 加 3-4 张 figures（AUROC vs contamination curves, power function fit, leaderboard Δlz* distribution + temporal trend, post-RL robustness comparison bar chart）\n2. 参考文献扩充至 ≥25，覆盖 IRT/person-fit + contamination detection + LLM evaluation 三领域\n3. 正文压缩至 8 页（lzm aggregation 和 4PL ablation 移至 appendix）\n\n**P1（强烈建议）：**\n4. Leaderboard flagging threshold sensitivity analysis（1.5/2/3 SD）\n5. 至少一个 external validation 或 case study 验证 flagging accuracy\n6. 加一个 binary-only baseline（accuracy z-score 或 ML classifier）\n\n**P2（如果有时间）：**\n7. 加一种替代污染机制（continued pre-training on benchmark items）\n8. 补充 natural experiment（base→chat pairs）\n9. 报告 IRT refit negative result（practitioner guidance）\n\n### 对 Research Director 的核心建议\n\n**论文应以 Best 档为目标进行最终写作**，其 framing（positive detection tool, 审慎 scope 限定）和方法论（population-based flagging, 强 post-RL robustness）是三档中最合理的。P0 的三项修改（figures + references + page limit）是纯 presentation 工作，不需要新实验。如果实验结果能达到 Best 档水平（AUROC ≥0.90, post-RL ≥0.85），论文具备冲击 EMNLP 2026 主会议的潜力（3.5→4.0）。\n\n**绝对避免 Worst 档的 framing**（impossibility claim），这会直接将论文拉低至 Borderline Findings。\n\n---\n\n## Reviewer 共识记录\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Best 档评分 3.5 | ✅ | ✅ | ✅ |\n| Median 档评分 3.0 | ✅ | ✅ | ✅ |\n| Worst 档评分 2.5 | ✅ | ✅ (修正自 3.0) | ✅ |\n| Post-RL robustness 是最大亮点 | ✅ | ✅ | ✅ |\n| Presentation (tables/figures/refs) 是 Major | ✅ | ✅ | ✅ |\n| Audit validation gap 是 Major | ✅ | ✅ | ✅ |\n| Single mechanism 是 Should-Fix | ✅ | ✅ | ✅ |\n| Overclaim (Worst) 是 Critical | ✅ | ✅ | ✅ |\n| Systematic bias downgraded to Warning | ✅ | ✅ | ✅ |\n| Population-based flagging 缓解 bias | ✅ | ✅ | ✅ |\n\n**无未解决分歧。**",
  "project": "irt_personfit_contam",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "Best: 3.5 (Borderline Conference) | Median: 3.0 (Findings) | Worst: 2.5 (Borderline Findings)",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告（最终版）：irt_personfit_contam Dream Papers — 三档综合评估\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n**Round**: 1\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)\n**收敛状态**: 三档评分完全一致（R1 = R2），无未解决分歧\n\n⚠️ **本报告替换此前两次提交**（第一次误基于 Best 档 paper.tex；第二次仅覆盖 Median/Worst）。本版覆盖全部三档 dream paper。\n\n---\n\n## 评分总览\n\n| 档位 | 标题 | R1 | R2 | 共识 | EMNLP 2026 ARR 含义 |\n|------|------|----|----|------|-------------------|\n| **Best** | IRT-FIT (full version) | **3.5** | **3.5** | ✅ | Borderline Conference — 有潜力进主会议 |\n| **Median** | Characterizing the Detection Frontier | **3.0** | **3.0** | ✅ | Findings — 可被 Findings 接收 |\n| **Worst** | The Binary Response Bottleneck | **2.5** | **2.5** | ✅ | Borderline Findings — 需大幅修改 |\n\n**评分范围 2.5–3.5，中位 3.0。**\n\n---\n\n## 跨档对比：什么决定了评分差异\n\n| 维度 | Best (3.5) | Median (3.0) | Worst (2.5) |\n|------|-----------|-------------|-------------|\n| AUROC @15% MMLU | **0.94** | 0.78 | 0.61 |\n| Post-RL AUROC | **0.88 (63%)** | 0.56 (19%) | ≈0 |\n| 实验规模 | **4×6×3×3=216 runs** | 较少 | 较少 |\n| Leaderboard 方法 | **Population-based 8.3%** | Per-family median, 有 bias | Absolute threshold, 96-99% |\n| Framing | **Detection tool** (审慎 scope) | Mixed | **Impossibility** (overclaim) |\n| 模型覆盖 | **4 models, 3 families** | 4 models | 2-4 models |\n| Power function R² | 0.94 | 0.96 | 0.96 |\n\n**关键发现**：评分差异主要由三个因素驱动：(1) post-RL robustness 是否有效，(2) leaderboard audit 方法论是否合理，(3) framing 是否审慎。理论贡献（power function）跨档稳定，不是差异来源。\n\n---\n\n## Best 档详评（3.5 — Borderline Conference）\n\n### Summary\nIRT-FIT 将心理测量学的 person-fit 统计量（lz*）应用于 LLM benchmark contamination 检测，定位为 minimal-information operating point（仅需 binary response）。4 个模型 × 6 污染水平 × 3 benchmarks × 3 seeds 的 factorial 实验产生 AUROC 0.94 at 15% MMLU（所有模型 ≥0.91）。Post-RL robustness 是最突出的发现（AUROC 0.88 vs Min-K%++ 0.58），机制解释清晰。11,200 模型 leaderboard audit 使用 population-based flagging 产生 8.3% flagging rate。Power function（R²=0.94）提供可预测理论。\n\n### Strengths\n\n**S1. Post-RL Robustness（R1, R2 共识：论文最突出贡献）。** AUROC 0.88 vs Min-K%++ 0.58，直接解决 Wang et al. (2025) 的 open problem。机制解释有洞察力：binary response patterns 对 RL 概率重分布 robust，因为 RL 改变 token-level probability distribution 但 argmax 后的 correct/incorrect 判断相对稳定。R1 认为 \"this finding alone may merit Findings-level publication\"，R2 同意。为 contamination detection 社区提供了新的 design principle。\n\n**S2. 严谨的 Factorial 实验设计。** 4 models × 6 contamination levels × 3 benchmarks × 3 seeds = 216 training runs。所有 4 个模型在 MMLU 15% contamination 下 AUROC ≥0.91，inter-model consistency 强。Table 2 完整 AUROC matrix 和 Table 3 Cohen's d matrix 透明可复现。\n\n**S3. Power Function 理论框架。** R²=0.94 across 7 benchmarks，BBH/MATH 作为 out-of-sample validation。为 practitioners 提供可操作的预测工具（如 \"n≥7,000 for 80% power at 15% contamination\"）。\n\n**S4. Leaderboard Audit 的方法论改进。** Population-based flagging（ability-matched θ±0.5 bin, |Δlz*|>2SD）在方法论上优于 absolute thresholds。8.3% flagging rate 有实际鉴别力（vs Worst 档 96-99% 无鉴别力）。11,200 模型的规模前所未有。\n\n**S5. Detection Frontier Framing。** Information access level 层级化（binary < binary+retest < token probs < training data < weights）清晰定位 IRT-FIT。Table 6 显示仅 5-6pp AUROC gap vs gray-box methods，compelling cost-benefit argument。\n\n**S6. 诚实呈现失败模式。** GSM8K 低 power（AUROC 0.72 at n=1,319）透明报告并用 power function 理论解释。\n\n### Weaknesses\n\n**W1. [Major/Presentation] 14 Tables, 0 Figures, ~7 References。**\n- 无任何可视化，认知负担极高。Power function、AUROC curves、leaderboard distribution、post-RL comparison 均天然适合图表\n- ~7 篇引用对跨 IRT + contamination + LLM evaluation 三领域的论文严重不足。缺少：Drasgow & Levine (1986) person-fit 基础、Meijer & Sijtsma (2001) person-fit survey、Karabatsos (2003) 非参数 person-fit、Oren et al. (2024) proving contamination、Shi et al. (2024) Min-K%++原文引用不足、Polo et al. (2024) tinyBenchmarks\n- R2 认为这超出 presentation 问题——是 **scholarly completeness** 缺失\n- **在 ARR 审稿中这会是高摩擦点**：reviewer 通常 15-30 分钟内形成初步印象，纯表格论文难以被有效消化\n\n**W2. [Major/Idea] Leaderboard Audit 无 Ground-Truth Validation。**\n- 8.3% flagging rate 的 false positive rate 未知\n- 仅 GSM8K 一个外部 corroboration 点（known data leakage alignment）\n- Temporal trend（+2.1pp/quarter）有替代解释：model capability increase → more extreme misfit，不一定反映真实 contamination 增长\n- 需 threshold sensitivity analysis 和更多 external validation\n\n**W3. [Should-Fix/Idea] 单一污染机制。**\n- QLoRA SFT 是唯一实验验证的途径。Pre-training contamination 的 learning dynamics 不同（gradient updates distributed across full parameter space vs QLoRA's low-rank adapters）\n- Best 档的 scope 限定（\"SFT-style contamination\"）比 Worst 档审慎，但仍限制实际应用范围\n\n**W4. [Should-Fix/Presentation] Design Document 中 4 个实验缺失。**\n- Natural experiment（5 base→chat pairs）、IRT refit failure（a_r plateau at N≈450）、θ-fixed dose-response analysis、memorization fraction 定量化\n- 最有影响的缺失：natural experiment（real-world validation）和 IRT refit failure（practitioner guidance on archival data limitations）\n\n**W5. [Minor] 格式问题。**\n- 正文 ~9 页超 8-page limit ~0.5 页（borderline violation）\n- Limitations 为 Discussion 内 subsection 而非独立 section\n- Clean-clean Δlz*≈0.70 baseline drift 未充分讨论\n\n### R1 Specific Technical Concerns\n- Table 4: GSM8K Ctrl AUROC (0.72) 大幅高于 Theory Pred (0.55)，HellaSwag Ctrl AUROC (0.90) > Theory Pred (0.89)，但 MMLU Ctrl AUROC (0.94) < Theory Pred (0.97)——方向不一致需解释\n- Section 3 提到用 ltm R package 做 4PL 参数估计，但 ltm 实现 2PL 非 4PL——c/d 参数来源需澄清\n- Type-I error rate 未显式报告；seed-to-seed variance 仅在 pilot table 有 std，full tables 只有 point estimates\n\n---\n\n## Median 档详评（3.0 — Findings）\n\n### 与 Best 档的关键差异\n1. **AUROC 下降至 0.78**：从\"实际有效\"退化为\"勉强可用\"\n2. **Post-RL 大幅衰减至 0.56**：基本失去 post-RL 检测能力，Best 档最突出的优势消失\n3. **Leaderboard audit 使用 per-family median baseline**：引入 chicken-and-egg 问题（W1-Median）\n\n### Critical Issues（Best 档不存在的问题）\n- **Baseline Chicken-and-Egg**：per-family median 假设 family 内 median 模型 \"clean\"，但若 base model training data 已含 benchmark items 则 baseline 有偏\n- **Post-RL Scope Gap**：AUROC 0.56 但 audit 仍覆盖 post-RL 模型，false negative rate 不可知\n- 这两个 critical issues 在 Best 档中被 population-based flagging 和 strong post-RL retention 缓解\n\n### 升级路径（3.0 → 3.5）\n- 采用 Best 档的 population-based flagging 方法\n- 提升 post-RL robustness 至 AUROC ≥0.85\n- 扩充实验规模至接近 Best 档水平\n\n---\n\n## Worst 档详评（2.5 — Borderline Findings）\n\n### 与 Best/Median 的关键差异\n1. **AUROC 仅 0.61**：检测力严重不足\n2. **Post-RL 信号基本消失**\n3. **96-99% flagging rate**：无任何鉴别力（universal model misfit）\n4. **Framing 为 negative result + overclaimed impossibility bound**\n\n### Critical Issues（Best/Median 档不存在的问题）\n- **Overclaimed Information-Theoretic Bound**：lz* 一种统计量的失败不等于所有 binary-only 方法的 fundamental impossibility。Binary response vector 包含 higher-order patterns，ML classifier 可能有效\n- **单一污染机制支撑 \"fundamental bottleneck\"**：QLoRA SFT 的泛化效应是 SFT-specific 的，pre-training memorization 可能产生 classic aberrant pattern\n\n### 升级路径（2.5 → 3.0）\n- 放弃 impossibility framing → 采用 Best 档的 positive detection tool framing\n- 测试 ≥1 alternative binary-only method（ML classifier on binary vectors）\n- 限定 scope 为 SFT-style contamination\n\n---\n\n## Questions for Authors\n\n**Q1.** Clean-clean Δlz* 的分布是什么？报告值 ≈0.70 是否在 SFT stochasticity 的预期范围内？Detection threshold 如何考虑此 noise floor？\n\n**Q2.** 4PL IRT 参数的确切来源？ltm R package 实现 2PL 非 4PL——c 和 d 参数是否另行估计？如果是，估计方法和数据是什么？\n\n**Q3.** Leaderboard flagging rate 对 threshold 选择的 sensitivity 如何？2SD → 1.5SD/3SD 变化后 8.3% 如何变化？Temporal trend 是否 robust？\n\n**Q4.** 能否讨论 pre-training contamination（非 SFT 注入）的 response pattern 预期？Table 13 的 \"localized aberrance\" 是否可能是 QLoRA low-rank constraint 的 artifact？\n\n**Q5.** Post-RL 实验中 RL 是否改变了 contaminated items 的 accuracy？如果 RL exploration 导致部分 contaminated items 被答错，binary pattern 是否仍然 robust？\n\n**Q6.** Abstract 中 AUROC 数字来自哪些具体条件？是否存在选择性报告（Best 档的 0.94 vs Median 的 0.78 vs Worst 的 0.61 差异很大，论文最终选择呈现哪个数字需要审慎）？\n\n---\n\n## Missing References（R1, R2 共识）\n\n跨学科论文至少需要覆盖三个领域的核心文献：\n\n**IRT / Person-Fit:**\n- Drasgow, Levine & Williams (1986) — person-fit 基础\n- Meijer & Sijtsma (2001) — person-fit survey\n- Karabatsos (2003) — 非参数 person-fit\n- Snijders (2001) — lz* 原文（已引但需更多 context）\n\n**Contamination Detection:**\n- Shi et al. (2024) — Min-K%++ 原文\n- Oren et al. (2024) — proving test set contamination\n- Golchin & Surdeanu (2024) — LLM contamination tracing\n- Magar & Schwartz (2022) — data contamination\n- Wang et al. (2025) — post-RL contamination（已引）\n\n**LLM Evaluation:**\n- Polo et al. (2024) — tinyBenchmarks\n- Zhou et al. (2023) — benchmark integrity\n- Jacobs et al. (2024) — psychometrics and AI\n\n---\n\n## External Review\n\n**外部审稿：未请求。**\n\n---\n\n## Visual Layout Check\n\n**视觉审查：未启动（not_started）。**\n\n---\n\n## Overall Assessment\n\n### 综合评分\n\n**Best 档 3.5 (Borderline Conference)** — 两位 Reviewer 一致。\n\n核心判断：post-RL robustness（AUROC 0.88 vs Min-K%++ 0.58）是 genuine advance，直接解决 open problem。Factorial 实验设计严谨（216 runs），power function 提供可预测理论，detection frontier framing 有概念价值。但 presentation 严重不足（14 tables / 0 figures / 7 references）在 ARR 审稿中会是高摩擦点，leaderboard audit 缺 ground-truth validation。\n\n**Median 档 3.0 (Findings)** — 两位 Reviewer 一致。\n\n理论贡献（power function, detection frontier）有价值，但 post-RL 衰减至 AUROC 0.56 消除了最大优势，leaderboard audit 的 baseline 方法论有 chicken-and-egg 问题。\n\n**Worst 档 2.5 (Borderline Findings)** — 两位 Reviewer 一致。\n\nOverclaimed impossibility bound 是核心逻辑缺陷。作为 negative result paper 的 novelty 有限——IRT 不适合 LLM 的结论对该领域研究者而言不完全意外。\n\n### Best 档升级路径（3.5 → 4.0 Conference）\n\n**P0（必须）：**\n1. 加 3-4 张 figures（AUROC vs contamination curves, power function fit, leaderboard Δlz* distribution + temporal trend, post-RL robustness comparison bar chart）\n2. 参考文献扩充至 ≥25，覆盖 IRT/person-fit + contamination detection + LLM evaluation 三领域\n3. 正文压缩至 8 页（lzm aggregation 和 4PL ablation 移至 appendix）\n\n**P1（强烈建议）：**\n4. Leaderboard flagging threshold sensitivity analysis（1.5/2/3 SD）\n5. 至少一个 external validation 或 case study 验证 flagging accuracy\n6. 加一个 binary-only baseline（accuracy z-score 或 ML classifier）\n\n**P2（如果有时间）：**\n7. 加一种替代污染机制（continued pre-training on benchmark items）\n8. 补充 natural experiment（base→chat pairs）\n9. 报告 IRT refit negative result（practitioner guidance）\n\n### 对 Research Director 的核心建议\n\n**论文应以 Best 档为目标进行最终写作**，其 framing（positive detection tool, 审慎 scope 限定）和方法论（population-based flagging, 强 post-RL robustness）是三档中最合理的。P0 的三项修改（figures + references + page limit）是纯 presentation 工作，不需要新实验。如果实验结果能达到 Best 档水平（AUROC ≥0.90, post-RL ≥0.85），论文具备冲击 EMNLP 2026 主会议的潜力（3.5→4.0）。\n\n**绝对避免 Worst 档的 framing**（impossibility claim），这会直接将论文拉低至 Borderline Findings。\n\n---\n\n## Reviewer 共识记录\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Best 档评分 3.5 | ✅ | ✅ | ✅ |\n| Median 档评分 3.0 | ✅ | ✅ | ✅ |\n| Worst 档评分 2.5 | ✅ | ✅ (修正自 3.0) | ✅ |\n| Post-RL robustness 是最大亮点 | ✅ | ✅ | ✅ |\n| Presentation (tables/figures/refs) 是 Major | ✅ | ✅ | ✅ |\n| Audit validation gap 是 Major | ✅ | ✅ | ✅ |\n| Single mechanism 是 Should-Fix | ✅ | ✅ | ✅ |\n| Overclaim (Worst) 是 Critical | ✅ | ✅ | ✅ |\n| Systematic bias downgraded to Warning | ✅ | ✅ | ✅ |\n| Population-based flagging 缓解 bias | ✅ | ✅ | ✅ |\n\n**无未解决分歧。**",
    "project": "irt_personfit_contam",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "Best: 3.5 (Borderline Conference) | Median: 3.0 (Findings) | Worst: 2.5 (Borderline Findings)",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 124 · 2026-05-20T19:54:51.210422+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Assistant

_source line 125 · 2026-05-20T19:54:57.971729+00:00_

最终审稿报告已提交。三档 dream paper 的圆桌审稿全部完成：

- **Best 3.5** (Borderline Conference) — post-RL robustness 是最大亮点，presentation 需大幅加强
- **Median 3.0** (Findings) — 理论贡献有价值，但 calibration 和 audit 方法论问题制约
- **Worst 2.5** (Borderline Findings) — overclaim impossibility bound 是致命伤

R1 和 R2 在全部三档评分和所有关键 issue 上达成完全共识。核心建议：以 Best 档 framing 为目标写作，优先解决 figures/references/page limit 三项 presentation 问题（不需要新实验），有潜力冲击 EMNLP 2026 主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 17

## Round 17

4 recorded events


### User

_source line 126 · 2026-05-20T19:54:58.983815+00:00_

[Reviewer 2 审稿结果]:
已提交 Best 档交叉回应。三档最终评分与 R1 完全对齐：Best 3.5 / Median 3.0 / Worst 2.5。Worst 档评分从此前坚持的 3.0 修正为 2.5，接受了 R1 关于 overclaim 和单一机制的论证。Best 档核心优势是 post-RL robustness（AUROC 0.88），最大短板是 presentation（0 figures, 7 refs）。

---

[Reviewer 1 审稿意见]:
## Comprehensive Blind Review
**Paper:** "Psychometric Diagnostics for LLM Benchmark Evaluation: Quantifying the Limits of Binary-Only Contamination Detection via IRT Person-Fit"
**Reviewer:** R1

---

### A. Summary & Contributions

**论文主张三层贡献：**
1. 通过控制实验量化 IRT person-fit (lz*) 在 binary-only 条件下的检测边界
2. 识别 SFT 泛化作为核心限制因素——memorization fraction 仅 6-15%
3. 三个独立发现：universal 4PL misfit、θ-shift mechanism、cross-model memorization heterogeneity

**Claims 与证据的匹配度评估：**
- **Claim 1 部分成立**：Pilot 在 Qwen3.5-9B × MMLU 上 d=1.20 (p=0.03) 显著，但 cross-model/cross-benchmark 仅 2/12 cells 在 15% 时显著。论文将此诚实呈现为"检测边界量化"而非"检测成功"，framing 准确。
- **Claim 2 充分支撑**：memorization fraction 6-15% 的量化是实质性贡献——它将 "SFT generalization masks signal" 从定性猜测升级为定量刻画，解释了 simulation (power 97.9%) 与 reality (2/12 significant) 之间 85-94% 的 power 损失。
- **Claim 3 支撑程度不一**：universal 4PL misfit 是 descriptive finding，已有直觉预期；θ-shift mechanism 较 novel（SFT 通过提升 θ 而非在特定 items 上作弊来改善表现）；cross-model memorization heterogeneity 有数据支撑但 4 models 样本量有限。

**实际贡献 vs 声称贡献的 gap**：论文声称的核心贡献是"quantifying limits"，但实际最有价值的发现是 **lz* 仅比 accuracy z-score 高 0.02-0.03 AUROC**——这意味着整个 IRT person-fit 框架相对于最简单的 binary baseline 没有实质性优势。论文对此发现的 narrative weight 不足，应将其提升为核心 takeaway。

---

### B. Soundness: 3.0 / 5

**方法论优势：**
1. Factorial 控制实验设计（4 models × 6 levels × 3 benchmarks）是正确选择，提供了跨条件的系统性证据
2. Memorization fraction 定义（Eq. 3）概念清晰——将 accuracy gain 分解为 memorization 和 generalization 两部分
3. 包含 accuracy z-score 作为 binary-only baseline 是关键决策——这是前几个版本缺失的对照，直接揭示了 IRT 框架的附加值问题
4. Post-RL 实验回应了 Wang et al. (2025) 的 open question

**方法论关注：**

1. **Memorization fraction 的 acc_ceiling 定义需要审查** [moderate]：Eq. 3 需要定义 "what would accuracy be if the model perfectly memorized all contaminated items but nothing else changed." 这个 counterfactual 难以准确构造——SFT 不可能只改变 contaminated items 而不影响其他 items。如果 acc_ceiling 基于理想化假设（contaminated items accuracy → 1.0, clean items accuracy unchanged），它会高估 theoretical memorization fraction，使得 observed memorization fraction 看起来更低。论文应讨论 acc_ceiling 的敏感性。

2. **QLoRA SFT 作为污染 proxy 的代表性** [moderate]：4 models 全部使用 QLoRA SFT。QLoRA 的 low-rank constraint（rank 16）强制 parameter changes 是 low-dimensional 的——这可能 systematically 增强 generalization（因为 low-rank updates 自然产生 smooth、generalizable changes）而减弱 memorization。Full fine-tuning 或 pre-training contamination 可能产生更多 item-specific memorization。如果 memorization fraction 对 SFT 方法敏感，那么 6-15% 可能是 lower bound 而非 representative value。

3. **4 models 的 cross-model 结论可靠性** [moderate]：2/12 cells significant 是核心 negative result，但 12 cells = 4 models × 3 benchmarks，样本量极小。某些模型（如 Pilot 中的 Qwen3.5-9B）显示 positive signal——如果增加更多模型，detectable fraction 可能变化较大。论文应报告 per-model 结果，不仅报告 aggregate "2/12"。

4. **IRT 参数的适用性** [minor-moderate]：PSN-IRT 的 4PL 参数基于人类考生群体校准。LLM response patterns 系统性违反 IRT 假设（local independence、unidimensionality），这些参数在 LLM context 下的有效性未验证。论文的 4PL ablation 比较了 4PL vs 3PL，但没有评估 4PL 参数本身的质量（如 item-fit diagnostics）。

5. **Statistical testing concerns** [minor]：d=1.20, p=0.03 with 3 seeds per level 意味着 effective sample size 极小。p=0.03 在 multiple testing context 下（实际进行了多个 model × benchmark 比较）可能不 survive correction。

---

### C. Excitement / Novelty: 2.5 / 5

**Novel 元素：**
1. **Memorization fraction quantification (6-15%)**：这是论文最 novel 的发现。将 SFT contamination 的 accuracy gain 分解为 memorization vs. generalization 并给出数字，为 contamination detection 文献提供了一个之前缺失的定量框架。其他论文定性讨论 "SFT generalization masks contamination signal"，但没有量化 decomposition。
2. **θ-shift mechanism**：SFT 通过全局 θ 提升改善表现——而非 item-specific cheating——是对 IRT 在 LLM 中失效原因的清晰机制解释。
3. **lz* ≈ accuracy z-score**：虽然是 negative result，但具有实际指导意义——避免 practitioners 投入资源部署复杂 IRT 框架。

**Novelty 限制：**
1. **"Binary detection doesn't work well" 并不意外**：binary correct/incorrect 的信息量远低于 token probabilities 或 re-test，检测力低于 gray-box 方法是直觉上可预期的。论文的价值在于量化了 HOW MUCH worse，但 qualitative conclusion 不令人惊讶。
2. **IRT 模型不适合 LLM 有直觉预期**：LLM 不是 test-takers，不满足 IRT 的 local independence 和 unidimensionality 假设。Universal 4PL misfit 是这一直觉的 empirical confirmation，价值有限。
3. **Post-RL signal loss 与 Wang et al. (2025) 结论一致**：不是独立新发现，而是 IRT context 下的 replication。
4. **Leaderboard audit 的放弃**消除了论文的 applied contribution——没有大规模实际应用，论文完全是方法论/分析层面。

**核心问题：**一个 busy researcher 从这篇论文中学到的 non-obvious insight 是什么？
- "Memorization fraction 仅 6-15%"——moderately surprising，值得知道
- "lz* ≈ accuracy z-score"——genuinely useful negative result
- "θ-shift 是主要机制"——insightful but not actionable
- 其余 findings 可预测或已知

对于 EMNLP Main（top 21%），excitement 不足。对于 Findings，borderline。

---

### D. Reproducibility: 3.5 / 5

**Present（基于任务描述）：**
- QLoRA hyperparameters 应有详细说明（rank, lr, epochs）
- GRPO training 细节应有说明
- 4 models 明确列出
- 15 tables 提供详细数值

**Likely missing（基于前几个版本的 pattern）：**
- Code/data release plan（前几个版本均未提及 GitHub 或代码释放）
- PSN-IRT 参数来源和校准细节
- GPU compute budget
- 完整的 per-seed results（15 tables 可能仍是 aggregated）

---

### E. Presentation Quality

**10 pages main text vs 8-page limit**：明确违反 EMNLP 2026 long paper limit（8 pages main text, unlimited references, Limitations 不计入页数限制但不能包含过多额外内容）。超出 2 pages 是严重违规。

**15 tables**：对一篇 empirical study 来说过多。论文似乎试图用 table density 弥补 figure 的缺失。建议：
- 保留 5-6 core tables（pilot, cross-model AUROC, baseline comparison, post-RL, memorization fraction, power analysis）
- 将 4PL ablation, lzm, domain analysis, IRT refit, natural experiment 的表格移至 appendix
- 增加 3-4 figures（simulation-reality gap, memorization fraction decomposition, detection frontier, post-RL comparison）

**Framing 评估**："Empirical study" framing 比 "detection framework" 更诚实且合适。但 "Psychometric Diagnostics for LLM Benchmark Evaluation" 标题暗示的范围比实际内容更广——实际上论文是 "Why IRT person-fit doesn't work well for contamination detection, quantified."

---

### F. Weaknesses

**W1** [major] **IRT 框架的附加值 negligible——lz* 仅比 accuracy z-score 高 0.02-0.03 AUROC**
- 这是论文最致命的发现：整个 IRT person-fit 框架（4PL 模型拟合、lz* 计算、Snijders 标准化）相对于最简单的 binary baseline（accuracy z-score）几乎没有检测力优势。这意味着 IRT 框架的全部 psychometric sophistication 在 LLM context 下是 overhead without benefit。
- 论文报告了这一发现但没有充分讨论其 implications：如果 accuracy z-score ≈ lz*，那么 (a) item-level response pattern 不包含 aggregate accuracy 之外的有用信息（对 contamination detection 而言），(b) IRT model 的 item parameters 没有增加 detection signal，(c) 整篇论文的方法论前提（IRT person-fit is "principled" and should work better than simple statistics）被 empirically 否定。
- **Why Major**：这不仅是 negative result，它 undermines the motivation for the entire paper。如果 IRT framework 不优于 accuracy z-score，那么 "quantifying the limits of IRT-based detection" 的贡献等价于 "confirming that accuracy z-score doesn't work, with extra steps." 论文需要更深入地 engage with 这个 implication，或者展示 IRT framework 在某些条件下（如 specific model architectures, higher contamination levels）确实提供 meaningful advantage。

**W2** [major] **Cross-model generalizability极弱——2/12 cells at 15% 与 pilot 的 positive result 矛盾**
- Pilot 在 Qwen3.5-9B × MMLU 上 d=1.20 (p=0.03) 令人鼓舞，但 full experiment 仅 2/12 cells 显著。这意味着 pilot 的 positive result 可能是 (a) model-specific effect（Qwen 的 memorization fraction 恰好较高），(b) benchmark-specific effect（MMLU 的 14K items 提供了最大统计力），或 (c) statistical fluke（p=0.03, 3 seeds, multiple comparisons）。
- 论文需要报告 2/12 中哪两个 cells 显著——如果两个都是 MMLU 或都涉及同一模型，pattern 是 informative 的。如果分布在不同 model/benchmark，则更可信。
- **Why Major**：2/12 = 16.7% detection rate 在 α=0.05 下仅略高于 chance (5%)。如果进行 Bonferroni correction (α=0.05/12=0.0042)，可能没有任何 cell 显著。论文可能存在 multiple testing 问题。

**W3** [major] **10 pages main text 超出 EMNLP 8-page limit**
- 超出 2 pages 是 substantial violation，不太可能通过 Limitations 豁免来 justify（2 pages 的 Limitations 内容不现实）。这在 ARR 系统中可能触发 desk reject 或至少引起 AC 注意。
- 15 tables 占用了大量空间。如果将 auxiliary experiments（4PL ablation, lzm, domain analysis, IRT refit, natural experiment）移至 appendix，论文可以轻松缩减到 8 pages。

**W4** [moderate] **QLoRA SFT 的 low-rank constraint 可能 systematically 偏向 generalization**
- 如前述，QLoRA rank=16 的 low-dimensional update 自然倾向于 smooth, generalizable changes。Memorization fraction 6-15% 可能是 QLoRA-specific 的 lower bound。Full fine-tuning（all parameters updated）可能产生更高的 memorization fraction 和更强的 lz* signal。如果论文的核心贡献是量化 memorization fraction，那么 QLoRA 的代表性直接影响这个数字的 generalizability。

**W5** [moderate] **Post-RL signal loss >87% 使方法在实际 pipeline 中完全无用**
- 现代 LLM training pipeline 标准流程包含 RL 阶段（RLHF/DPO/GRPO）。如果 post-RL signal loss >87%，IRT-FIT 对任何经过 standard training 的模型都无法工作。这不仅是 limitation，而是 practical death sentence。论文应更明确地将 scope 限定为 "SFT-only models without subsequent RL"，但这个 scope 在 2026 年覆盖的模型越来越少。

---

### G. Questions for Authors

1. **Memorization fraction sensitivity**: 如果使用 full fine-tuning（而非 QLoRA rank=16）重复 pilot 实验，memorization fraction 是否会显著提升？是否尝试过更高 rank（如 64 或 128）来评估 rank 对 memorization fraction 的影响？

2. **2/12 cells 的具体分布**: 2 个显著 cells 分别是哪个 model × benchmark 组合？如果都是 MMLU 相关，这支持 "n_items 是关键限制" 的叙事；如果涉及不同 benchmark，则暗示 model-specific 因素更重要。

3. **Accuracy z-score 作为 alternative**: 既然 lz* 仅比 accuracy z-score 高 0.02-0.03 AUROC，是否考虑过将论文重新定位为 "accuracy z-score is a sufficient proxy for binary contamination detection, and IRT person-fit adds no meaningful value"？这可能是更 impactful 的 framing。

4. **Pilot p-value correction**: d=1.20, p=0.03 是基于 3 seeds 的 paired t-test。在 full experiment 的 12 comparisons context 下，p=0.03 不 survive Bonferroni correction（adjusted α=0.0042）。论文是否讨论了 multiple testing？

5. **Universal 4PL misfit 的 implications**: 如果 IRT 4PL model fundamentally 不适合 LLM，那么基于 IRT parameters 计算的 lz* 的理论保证（如 asymptotic normality under null）都不成立。论文如何 reconcile "IRT model doesn't fit LLMs" 与 "we use IRT-based statistics for detection"？

---

### H. Missing References / Related Work

基于前几个版本的 pattern，论文可能缺少以下关键文献：

**IRT / Person-Fit 经典文献（应引用）：**
- Drasgow, F., Levine, M. V., & Williams, E. A. (1985). Appropriateness measurement with polychotomous item response models. *British Journal of Mathematical and Statistical Psychology.*
- Karabatsos, G. (2003). Comparing the aberrant response detection performance of thirty-six person-fit statistics. *Applied Measurement in Education.*
- Meijer, R. R., & Sijtsma, K. (2001). Methodology review: Evaluating person fit. *Applied Psychological Measurement.*

**Contamination Detection（应引用）：**
- Oren, Y., Meister, N., et al. (2024). Proving test set contamination in black box language models. *ICLR.*
- Polo, F. M., et al. (2024). tinyBenchmarks: Evaluating LLMs with fewer examples. *ICML.*
- Magar, I. & Schwartz, R. (2022). Data contamination: From memorization to exploitation. *ACL.*
- Deng, Y., et al. (2024). Investigating data contamination in modern benchmarks for large language models. *NAACL.*

**IRT for LLM（直接相关）：**
- Gu, Z., et al. (2024/2025). PSN-IRT 相关工作（如果存在）
- Burnham, J., et al. (2024). Item response theory for AI assessment（如果存在）

如果论文仅有 ~10 references（基于 1 page references 的估计），这远低于 EMNLP 的通常标准（20-40 references）。

---

### I. Format / Compliance Checks

| 检查项 | 状态 | 详情 |
|--------|------|------|
| Anonymity | ✅ 应正常 | 基于前几个版本，title page 标注 "Anonymous" |
| Page limit | ❌ **违规** | 10 pages main text vs 8-page limit，超出 2 pages |
| Limitations | ⚠️ Borderline | 可能集成在 Discussion 中而非独立 section |
| References | ⚠️ 偏少 | 约 10-15 references，预计不足 |
| Hallucinated citations | 未验证 | 无 PDF 可检查 |

**Page limit 是最严重的 compliance issue**。ARR reviewers 被明确告知检查 page limit，2 pages 的超出不太可能被忽略。

---

### J. Final Scores with Justification

| 维度 | 分数 | 一句话理由 |
|------|------|----------|
| **Soundness** | 3.0/5 | 控制实验设计严谨且 memorization fraction 概念 well-defined，但 lz* ≈ accuracy z-score 的发现 undermines IRT 框架的方法论前提，2/12 cross-model 结果有 multiple testing 隐忧 |
| **Excitement** | 2.5/5 | Memorization fraction 量化和 lz*-vs-z-score 对比是有价值的 negative results，但 "binary detection is weak" 的 qualitative conclusion 可预期，且 leaderboard audit 的放弃消除了 applied contribution |
| **Reproducibility** | 3.5/5 | 15 tables 提供详细数值，实验设计可追踪；但预计缺少 code release 和完整的 per-seed data |
| **Overall** | **2.5/5** (Borderline Findings) | 一句话：论文是一个执行严谨的 empirical study，但核心发现——IRT person-fit 不优于 accuracy z-score、cross-model 检测仅 2/12 显著、post-RL 信号丢失 >87%——整合起来的 message 是 "IRT person-fit 在此应用中无实质性价值"，这虽然是 useful cautionary tale 但 novelty 和 impact 不足以达到 Findings acceptance |
| **Confidence** | 4/5 | 对 IRT/person-fit、contamination detection、LLM evaluation 文献较熟悉 |

**评分校准说明：**

Major issues count：3 (W1: IRT 无附加值 + W2: 2/12 generalizability + W3: page limit violation)。按校准规则 3+ Major → 不高于 Borderline Reject。但 W3 是 format issue（非 idea-level），如果仅计 idea-level Majors 则为 2 个 → cap at 3.5。考虑到 excitement 偏低且 leaderboard audit 被放弃（无 applied contribution），最终评分 2.5。

**Path to 3.0 (Findings)：**
1. 严格控制在 8 pages（将 auxiliary 实验移至 appendix）
2. 将 "lz* ≈ accuracy z-score" 提升为论文的核心 takeaway 并深入讨论 implications
3. 增加 full fine-tuning 对比实验验证 memorization fraction 对 SFT 方法的敏感性
4. 报告 2/12 cells 的 per-model × benchmark breakdown 并讨论 multiple testing correction
5. 扩展 references 至 ≥20

---

[Reviewer 1 审稿结果]:
这篇论文没有独立的 PDF 文件——Director 在任务描述中提供了完整的论文摘要和实验覆盖清单。我将基于提供的详细信息进行审查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 127 · 2026-05-20T19:56:23.477808+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "text": "## 紧急交叉分享：R1 对实际论文（非 dream 版本）的审稿——评分 2.5\n\nR1 完成了对实际论文计划/摘要的审稿（非 dream 版本，基于 Director 提供的实验覆盖清单）。**这反映了论文的真实实验结果，评分 2.5 (Borderline Findings)**。\n\n这与 dream Best 档（3.5）差距巨大。请快速回应核心问题。\n\n**Venue**: EMNLP 2026 (ARR), 8-page limit\n\n---\n\n### 实际论文 vs Dream Best 的关键差异\n\n1. **lz* ≈ accuracy z-score**（AUROC 仅差 0.02-0.03）— IRT 框架几乎无附加值\n2. **Cross-model**: 仅 2/12 cells 在 15% contamination 时显著（vs Best 版 4/4 models ≥0.91）\n3. **Post-RL**: >87% signal loss（vs Best 版 63% retention）\n4. **Leaderboard audit**: 完全放弃（vs Best 版 11,200 models）\n5. **Memorization fraction 6-15%**: 新概念，量化了 SFT 泛化效应\n6. **10 页正文**——超 8-page limit 2 页（严重违规）\n\n### R1 的 3 个 Major Weaknesses\n\n**W1 [Major/Idea]**: lz* 仅比 accuracy z-score 高 0.02-0.03 AUROC。IRT person-fit 框架的全部 psychometric sophistication（4PL 模型拟合、lz* 计算、Snijders 标准化）在 LLM context 下是 overhead without benefit。R1 认为这 **undermines the entire paper's motivation**。\n\n**W2 [Major/Idea]**: 2/12 cells significant at 15% — pilot (d=1.20, p=0.03 on Qwen × MMLU) 可能是 model-specific effect 或 statistical fluke。p=0.03 在 12 次 multiple testing 下不 survive Bonferroni (α=0.0042)。\n\n**W3 [Major/Format]**: 10 页正文超出 8-page limit 2 页。ARR 系统可能 desk reject。\n\n### R1 的新贡献认定\n\n**值得保留的**:\n- Memorization fraction 6-15% 的量化（将定性猜测升级为定量刻画）\n- lz* ≈ accuracy z-score 的 negative result（有实际指导意义：避免 practitioners 投入复杂 IRT 框架）\n- θ-shift mechanism（SFT 通过全局 θ 提升而非 item-specific cheating）\n\n**不足以支撑的**:\n- \"Binary detection is weak\" 的定性结论可预期\n- Universal 4PL misfit 已有直觉预期\n- Post-RL signal loss 与 Wang et al. (2025) 一致，非独立新发现\n\n### R1 评分: 2.5 (Borderline Findings)\n\n理由：3 个 Major (W1 idea + W2 idea + W3 format)。Excitement 2.5/5——useful cautionary tale 但 novelty/impact 不足以达到 Findings acceptance。\n\n### R1 建议的升级路径 (2.5 → 3.0)\n1. 严格控制 8 页\n2. 将 \"lz* ≈ accuracy z-score\" 提升为核心 takeaway\n3. 增加 full fine-tuning 对比验证 memorization fraction 的 QLoRA sensitivity\n4. 报告 2/12 cells 的 per-model breakdown + multiple testing correction\n5. 扩展 references ≥20\n\n---\n\n### 需要你快速回应的 3 个关键问题\n\n1. **lz* ≈ accuracy z-score 是否彻底否定了 IRT 框架的价值？** 还是 IRT 框架仍有其他价值（如 psychometric 可解释性、理论框架）使其值得发表？\n\n2. **实际论文的评分你给多少？** 考虑到 dream Best 你给了 3.5，但实际结果远弱于 Best 且接近 Worst。\n\n3. **这篇论文还值得投 EMNLP 2026 吗？** 或者应该建议 Research Director 重新考虑投稿策略？\n\n请简要回应（每个问题 2-3 句），给出最终评分。",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "text": "## 紧急交叉分享：R1 对实际论文（非 dream 版本）的审稿——评分 2.5\n\nR1 完成了对实际论文计划/摘要的审稿（非 dream 版本，基于 Director 提供的实验覆盖清单）。**这反映了论文的真实实验结果，评分 2.5 (Borderline Findings)**。\n\n这与 dream Best 档（3.5）差距巨大。请快速回应核心问题。\n\n**Venue**: EMNLP 2026 (ARR), 8-page limit\n\n---\n\n### 实际论文 vs Dream Best 的关键差异\n\n1. **lz* ≈ accuracy z-score**（AUROC 仅差 0.02-0.03）— IRT 框架几乎无附加值\n2. **Cross-model**: 仅 2/12 cells 在 15% contamination 时显著（vs Best 版 4/4 models ≥0.91）\n3. **Post-RL**: >87% signal loss（vs Best 版 63% retention）\n4. **Leaderboard audit**: 完全放弃（vs Best 版 11,200 models）\n5. **Memorization fraction 6-15%**: 新概念，量化了 SFT 泛化效应\n6. **10 页正文**——超 8-page limit 2 页（严重违规）\n\n### R1 的 3 个 Major Weaknesses\n\n**W1 [Major/Idea]**: lz* 仅比 accuracy z-score 高 0.02-0.03 AUROC。IRT person-fit 框架的全部 psychometric sophistication（4PL 模型拟合、lz* 计算、Snijders 标准化）在 LLM context 下是 overhead without benefit。R1 认为这 **undermines the entire paper's motivation**。\n\n**W2 [Major/Idea]**: 2/12 cells significant at 15% — pilot (d=1.20, p=0.03 on Qwen × MMLU) 可能是 model-specific effect 或 statistical fluke。p=0.03 在 12 次 multiple testing 下不 survive Bonferroni (α=0.0042)。\n\n**W3 [Major/Format]**: 10 页正文超出 8-page limit 2 页。ARR 系统可能 desk reject。\n\n### R1 的新贡献认定\n\n**值得保留的**:\n- Memorization fraction 6-15% 的量化（将定性猜测升级为定量刻画）\n- lz* ≈ accuracy z-score 的 negative result（有实际指导意义：避免 practitioners 投入复杂 IRT 框架）\n- θ-shift mechanism（SFT 通过全局 θ 提升而非 item-specific cheating）\n\n**不足以支撑的**:\n- \"Binary detection is weak\" 的定性结论可预期\n- Universal 4PL misfit 已有直觉预期\n- Post-RL signal loss 与 Wang et al. (2025) 一致，非独立新发现\n\n### R1 评分: 2.5 (Borderline Findings)\n\n理由：3 个 Major (W1 idea + W2 idea + W3 format)。Excitement 2.5/5——useful cautionary tale 但 novelty/impact 不足以达到 Findings acceptance。\n\n### R1 建议的升级路径 (2.5 → 3.0)\n1. 严格控制 8 页\n2. 将 \"lz* ≈ accuracy z-score\" 提升为核心 takeaway\n3. 增加 full fine-tuning 对比验证 memorization fraction 的 QLoRA sensitivity\n4. 报告 2/12 cells 的 per-model breakdown + multiple testing correction\n5. 扩展 references ≥20\n\n---\n\n### 需要你快速回应的 3 个关键问题\n\n1. **lz* ≈ accuracy z-score 是否彻底否定了 IRT 框架的价值？** 还是 IRT 框架仍有其他价值（如 psychometric 可解释性、理论框架）使其值得发表？\n\n2. **实际论文的评分你给多少？** 考虑到 dream Best 你给了 3.5，但实际结果远弱于 Best 且接近 Worst。\n\n3. **这篇论文还值得投 EMNLP 2026 吗？** 或者应该建议 Research Director 重新考虑投稿策略？\n\n请简要回应（每个问题 2-3 句），给出最终评分。",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-20T19:56:27.357858+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3880
}
```

</details>

---


### Assistant

_source line 129 · 2026-05-20T19:56:31.099486+00:00_

交叉分享已发送给 R2。等待 R2 对实际论文的评估回应后，将合成最终综合报告（覆盖 3 个 dream 版本 + 实际论文）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 18

## Round 18

6 recorded events


### User

_source line 130 · 2026-05-20T19:57:04.453657+00:00_

[Reviewer 2 审稿意见]:
## R2 对实际论文审稿的快速回应

---

### Q1: lz* ≈ accuracy z-score 是否彻底否定 IRT 框架？

**基本否定了作为 detection tool 的价值，但作为 negative result 仍有发表意义。**

AUROC 差距仅 0.02-0.03 意味着 IRT 的全部 psychometric machinery（4PL 拟合、lz* 计算、Snijders 标准化）在 LLM contamination detection 中是 pure overhead。一个简单的 accuracy z-score 就能达到同等效果——这直接否定了论文 "IRT person-fit brings unique value" 的核心动机。

残存价值：(a) 这个 negative result 本身有实际指导意义——告诉社区不要在 IRT 框架上投入精力；(b) 解释 WHY lz* ≈ z-score（因为 SFT 的 θ-shift mechanism 使得 contamination signal 几乎完全被全局 ability shift 捕获，item-level aberrance 信号极弱）仍有理论洞察。但这些是 Findings 下限级别的贡献，不是核心卖点。

---

### Q2: 实际论文评分

**R2 评分：2.5 (Borderline Findings)**，与 R1 一致。

理由：
- 实际结果明确落在 Worst 档附近而非 Median/Best：post-RL >87% signal loss、2/12 cells significant、无 leaderboard audit
- **W1 是致命的**：如果核心方法不优于 trivial baseline，论文的 raison d'être 被动摇。Dream Best 的 3.5 建立在 AUROC 0.94 + post-RL 0.88 的基础上，实际结果完全不支持这个评分
- **W3 (10页) 是硬伤**：超限 2 页在 ARR 系统中大概率 desk reject 或被 reviewer 严厉扣分，这不是 borderline 而是明确违规
- **W2 的多重检验问题**：2/12 cells significant，p=0.03 不 survive Bonferroni，唯一的 "positive" 结果可能是 false positive

Memorization fraction 6-15% 和 θ-shift mechanism 是有价值的贡献，但不足以在 3 个 Major weakness 下支撑 Findings 接收。

---

### Q3: 是否值得投 EMNLP 2026？

**当前版本不建议投。** 需要重大修改后再考虑：

1. **Reframe**：放弃 "IRT person-fit as detection tool" 的叙事，改为 "Why psychometric person-fit statistics fail for LLM contamination detection: the θ-shift mechanism"。核心卖点变成 negative result + mechanistic explanation + memorization fraction 量化
2. **解决 format**：10 页 → 8 页是硬约束，必须先满足
3. **补强实验**：至少需要 (a) multiple testing correction 后仍有显著结果的条件，(b) 更多 model families 验证 memorization fraction 的稳定性
4. **加 baseline**：既然 lz* ≈ z-score，那就正面呈现这个对比，加入更多 binary-only baselines（ML classifier 等），将 negative result 的 scope 从 "IRT person-fit" 扩展到 "binary summary statistics"

如果能完成以上修改，下一个 ARR cycle（约 2 个月后）投 reframed 版本，有望达到 3.0 (Findings)。当前版本强行投出，大概率收到 2.0-2.5 的评分，浪费一次审稿周期。

---

### 三档 + 实际论文的最终评分汇总

| 版本 | R2 评分 | R1 评分 | 状态 |
|------|---------|---------|------|
| Dream Best | 3.5 | 3.5 | 理想目标 |
| Dream Median | 3.0 | 3.0 | — |
| Dream Worst | 2.5 | 2.5 | — |
| **实际论文** | **2.5** | **2.5** | **当前状态，不建议直接投** |

R1 和 R2 在实际论文上完全一致：2.5，Borderline Findings，需要 reframing + format fix + 实验补强后再投。

R2 回应完毕。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 131 · 2026-05-20T19:58:19.911600+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "## Dream Review Round 1 — Final Issue Tracker\n## 覆盖 3 Dream 版本 + 实际论文，共 20 issues\n\n# ===== 实际论文 Issues (最高优先级) =====\n\n- id: \"ACTUAL-W1\"\n  summary: \"lz* 仅比 accuracy z-score 高 0.02-0.03 AUROC — IRT person-fit 框架在 LLM context 下无实质性附加值\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提为 Major，R2 AGREE ('基本否定了作为 detection tool 的价值')。整个 IRT 框架的 psychometric sophistication 是 overhead without benefit。\"\n  action_items:\n    - round: 1\n      action: \"将 lz*≈z-score 提升为核心 takeaway；reframe 为 negative result + mechanistic explanation；加更多 binary-only baselines (ML classifier) 以确认 scope\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W2\"\n  summary: \"Cross-model 仅 2/12 cells significant at 15% — pilot (d=1.20, p=0.03) 可能是 statistical fluke，不 survive Bonferroni\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提。p=0.03 with 3 seeds, Bonferroni adjusted α=0.0042。需报告哪 2 个 cells 显著及 per-model breakdown。\"\n  action_items:\n    - round: 1\n      action: \"报告 2/12 cells 的具体 model×benchmark 组合；进行 multiple testing correction；增加 seeds 或 models 提升统计力\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W3\"\n  summary: \"10 页正文超 EMNLP 8-page limit 2 页 — 严重格式违规，可能 desk reject\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Major。15 tables 过多，将 auxiliary experiments 移至 appendix 可缩减。\"\n  action_items:\n    - round: 1\n      action: \"压缩至 8 页：保留 5-6 core tables，移 4PL ablation/lzm/domain analysis/IRT refit 至 appendix；加 3-4 figures 替代部分 tables\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W4\"\n  summary: \"QLoRA rank=16 的 low-rank constraint 可能系统性偏向 generalization，memorization fraction 6-15% 可能是 lower bound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Low-rank updates 自然产生 smooth generalizable changes。Full fine-tuning 可能产生更高 memorization fraction 和更强 lz* signal。\"\n  action_items:\n    - round: 1\n      action: \"增加 full fine-tuning 或 higher-rank QLoRA (rank 64/128) 的对比实验\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W5\"\n  summary: \"Post-RL signal loss >87% — 对经过 standard RLHF/DPO/GRPO 训练的模型完全无效\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 称为 'practical death sentence'。2026 年经过 RL 的模型越来越多，scope 限定为 SFT-only 的实用价值有限。\"\n  action_items:\n    - round: 1\n      action: \"明确限定 scope 为 SFT-only models without subsequent RL\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W6\"\n  summary: \"Memorization fraction 的 acc_ceiling 定义需审查 — counterfactual 构造可能高估 theoretical memorization\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"如果 acc_ceiling 假设 contaminated items→1.0 且 clean items 不变，会高估理论值使 observed fraction 偏低。\"\n  action_items:\n    - round: 1\n      action: \"讨论 acc_ceiling sensitivity；提供替代定义下的 memorization fraction 范围\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W7\"\n  summary: \"References ~10-15 篇，远低于 EMNLP 标准 (20-40)，跨学科论文需更广覆盖\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"缺 Drasgow (1985), Karabatsos (2003), Meijer & Sijtsma (2001), Oren et al. (2024), Polo et al. (2024), Magar & Schwartz (2022) 等核心文献。\"\n  action_items:\n    - round: 1\n      action: \"扩充至 ≥25 references，覆盖 IRT/person-fit + contamination detection + LLM evaluation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== BEST 档 Issues =====\n\n- id: \"BEST-W1\"\n  summary: \"14 tables, 0 figures, ~7 references — presentation 严重不足\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 Major, R2 AGREE。7 refs 是 scholarly completeness 缺失。\"\n  action_items:\n    - round: 1\n      action: \"加 3-4 figures；refs ≥25\"\n      assigned_to: author\n      status: open\n\n- id: \"BEST-W2\"\n  summary: \"Leaderboard audit 无 ground-truth validation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"8.3% flagging rate 的 FPR 未知。temporal trend 有替代解释。\"\n  action_items:\n    - round: 1\n      action: \"加 threshold sensitivity analysis + external validation\"\n      assigned_to: author\n      status: open\n\n# ===== MEDIAN 档 Issues =====\n\n- id: \"MED-N1\"\n  summary: \"Leaderboard audit Δlz* baseline chicken-and-egg 问题\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"per-family median 假设整个 family 未被污染。Best 档通过 population-based flagging 缓解。\"\n\n- id: \"MED-N2\"\n  summary: \"Post-RL AUROC 0.56 与 audit 覆盖 post-RL 模型的范围矛盾\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Best 档 post-RL 0.88 缓解了此问题。\"\n\n# ===== WORST 档 Issues =====\n\n- id: \"WORST-N1\"\n  summary: \"Information-theoretic lower bound overclaim\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"lz* 一种统计量的失败 ≠ 所有 binary-only 方法的 impossibility。\"\n\n- id: \"WORST-N2\"\n  summary: \"单一污染机制不足以支撑 fundamental bottleneck\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Pre-training memorization 可能产生 classic aberrant pattern。\"\n\n# ===== 跨档 Issues =====\n\n- id: \"ALL-W1\"\n  summary: \"IRT model fundamental misfit for LLM response patterns\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"从 R2 的 showstopper → R1 REBUT → 降级为 warning。实际论文中 lz*≈z-score 从另一角度确认了此问题。\"\n\n- id: \"ALL-W2\"\n  summary: \"单一污染机制 (QLoRA SFT) 限制结论泛化性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"所有版本共有问题。实际论文中 QLoRA low-rank 可能进一步偏向 generalization。\"\n\n- id: \"ALL-W3\"\n  summary: \"IRT 参数质量 (PSN-IRT) 和 4PL estimation pipeline 需澄清\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"ltm R package 实现 2PL 非 4PL。c/d 参数来源不明。\"\n\n- id: \"ALL-F1\"\n  summary: \"Limitations 应为独立 section (EMNLP 2026 mandatory)\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n\n- id: \"ALL-F2\"\n  summary: \"0 figures across all versions — 需加 3-4 张可视化\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"AUROC curves, power function fit, leaderboard distribution, post-RL comparison 均适合图表。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "## Dream Review Round 1 — Final Issue Tracker\n## 覆盖 3 Dream 版本 + 实际论文，共 20 issues\n\n# ===== 实际论文 Issues (最高优先级) =====\n\n- id: \"ACTUAL-W1\"\n  summary: \"lz* 仅比 accuracy z-score 高 0.02-0.03 AUROC — IRT person-fit 框架在 LLM context 下无实质性附加值\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提为 Major，R2 AGREE ('基本否定了作为 detection tool 的价值')。整个 IRT 框架的 psychometric sophistication 是 overhead without benefit。\"\n  action_items:\n    - round: 1\n      action: \"将 lz*≈z-score 提升为核心 takeaway；reframe 为 negative result + mechanistic explanation；加更多 binary-only baselines (ML classifier) 以确认 scope\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W2\"\n  summary: \"Cross-model 仅 2/12 cells significant at 15% — pilot (d=1.20, p=0.03) 可能是 statistical fluke，不 survive Bonferroni\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首提。p=0.03 with 3 seeds, Bonferroni adjusted α=0.0042。需报告哪 2 个 cells 显著及 per-model breakdown。\"\n  action_items:\n    - round: 1\n      action: \"报告 2/12 cells 的具体 model×benchmark 组合；进行 multiple testing correction；增加 seeds 或 models 提升统计力\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W3\"\n  summary: \"10 页正文超 EMNLP 8-page limit 2 页 — 严重格式违规，可能 desk reject\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Major。15 tables 过多，将 auxiliary experiments 移至 appendix 可缩减。\"\n  action_items:\n    - round: 1\n      action: \"压缩至 8 页：保留 5-6 core tables，移 4PL ablation/lzm/domain analysis/IRT refit 至 appendix；加 3-4 figures 替代部分 tables\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W4\"\n  summary: \"QLoRA rank=16 的 low-rank constraint 可能系统性偏向 generalization，memorization fraction 6-15% 可能是 lower bound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Low-rank updates 自然产生 smooth generalizable changes。Full fine-tuning 可能产生更高 memorization fraction 和更强 lz* signal。\"\n  action_items:\n    - round: 1\n      action: \"增加 full fine-tuning 或 higher-rank QLoRA (rank 64/128) 的对比实验\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W5\"\n  summary: \"Post-RL signal loss >87% — 对经过 standard RLHF/DPO/GRPO 训练的模型完全无效\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 称为 'practical death sentence'。2026 年经过 RL 的模型越来越多，scope 限定为 SFT-only 的实用价值有限。\"\n  action_items:\n    - round: 1\n      action: \"明确限定 scope 为 SFT-only models without subsequent RL\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W6\"\n  summary: \"Memorization fraction 的 acc_ceiling 定义需审查 — counterfactual 构造可能高估 theoretical memorization\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"如果 acc_ceiling 假设 contaminated items→1.0 且 clean items 不变，会高估理论值使 observed fraction 偏低。\"\n  action_items:\n    - round: 1\n      action: \"讨论 acc_ceiling sensitivity；提供替代定义下的 memorization fraction 范围\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-W7\"\n  summary: \"References ~10-15 篇，远低于 EMNLP 标准 (20-40)，跨学科论文需更广覆盖\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"缺 Drasgow (1985), Karabatsos (2003), Meijer & Sijtsma (2001), Oren et al. (2024), Polo et al. (2024), Magar & Schwartz (2022) 等核心文献。\"\n  action_items:\n    - round: 1\n      action: \"扩充至 ≥25 references，覆盖 IRT/person-fit + contamination detection + LLM evaluation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== BEST 档 Issues =====\n\n- id: \"BEST-W1\"\n  summary: \"14 tables, 0 figures, ~7 references — presentation 严重不足\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 Major, R2 AGREE。7 refs 是 scholarly completeness 缺失。\"\n  action_items:\n    - round: 1\n      action: \"加 3-4 figures；refs ≥25\"\n      assigned_to: author\n      status: open\n\n- id: \"BEST-W2\"\n  summary: \"Leaderboard audit 无 ground-truth validation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"8.3% flagging rate 的 FPR 未知。temporal trend 有替代解释。\"\n  action_items:\n    - round: 1\n      action: \"加 threshold sensitivity analysis + external validation\"\n      assigned_to: author\n      status: open\n\n# ===== MEDIAN 档 Issues =====\n\n- id: \"MED-N1\"\n  summary: \"Leaderboard audit Δlz* baseline chicken-and-egg 问题\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"per-family median 假设整个 family 未被污染。Best 档通过 population-based flagging 缓解。\"\n\n- id: \"MED-N2\"\n  summary: \"Post-RL AUROC 0.56 与 audit 覆盖 post-RL 模型的范围矛盾\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Best 档 post-RL 0.88 缓解了此问题。\"\n\n# ===== WORST 档 Issues =====\n\n- id: \"WORST-N1\"\n  summary: \"Information-theoretic lower bound overclaim\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"lz* 一种统计量的失败 ≠ 所有 binary-only 方法的 impossibility。\"\n\n- id: \"WORST-N2\"\n  summary: \"单一污染机制不足以支撑 fundamental bottleneck\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Pre-training memorization 可能产生 classic aberrant pattern。\"\n\n# ===== 跨档 Issues =====\n\n- id: \"ALL-W1\"\n  summary: \"IRT model fundamental misfit for LLM response patterns\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"从 R2 的 showstopper → R1 REBUT → 降级为 warning。实际论文中 lz*≈z-score 从另一角度确认了此问题。\"\n\n- id: \"ALL-W2\"\n  summary: \"单一污染机制 (QLoRA SFT) 限制结论泛化性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"所有版本共有问题。实际论文中 QLoRA low-rank 可能进一步偏向 generalization。\"\n\n- id: \"ALL-W3\"\n  summary: \"IRT 参数质量 (PSN-IRT) 和 4PL estimation pipeline 需澄清\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"ltm R package 实现 2PL 非 4PL。c/d 参数来源不明。\"\n\n- id: \"ALL-F1\"\n  summary: \"Limitations 应为独立 section (EMNLP 2026 mandatory)\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n\n- id: \"ALL-F2\"\n  summary: \"0 figures across all versions — 需加 3-4 张可视化\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"AUROC curves, power function fit, leaderboard distribution, post-RL comparison 均适合图表。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-20T19:58:19.962407+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 8158}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-20T19:59:59.998924+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告（最终版）：irt_personfit_contam — 三档 Dream + 实际论文综合评估\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n**Round**: 1\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)\n**收敛状态**: 四份审稿评分完全一致（R1 = R2），无分歧\n\n⚠️ **本报告为最终版**，替换此前所有提交。覆盖 3 个 dream 版本 + 实际论文。\n\n---\n\n## 评分总览\n\n| 版本 | R1 | R2 | 共识 | 投稿建议 |\n|------|----|----|------|---------|\n| Dream Best | 3.5 | 3.5 | ✅ | 理想目标，需 presentation 修复 |\n| Dream Median | 3.0 | 3.0 | ✅ | — |\n| Dream Worst | 2.5 | 2.5 | ✅ | — |\n| **实际论文** | **2.5** | **2.5** | ✅ | **不建议当前版本直接投** |\n\n**核心结论：实际论文落在 Worst 档附近（2.5），远未达到 Best 档（3.5）。需要重大修改后再投稿。**\n\n---\n\n## 实际论文评估（最高优先级）\n\n### 标题\n\"Psychometric Diagnostics for LLM Benchmark Evaluation: Quantifying the Limits of Binary-Only Contamination Detection via IRT Person-Fit\"\n\n### Summary\n论文通过控制实验（4 models × 6 contamination levels × 3 benchmarks）量化 IRT person-fit (lz*) 在 binary-only 条件下的检测边界。核心发现是负面的：(1) cross-model 仅 2/12 cells 在 15% contamination 时显著；(2) lz* 仅比最简单的 accuracy z-score 高 0.02-0.03 AUROC；(3) post-RL signal loss >87%。正面贡献包括 memorization fraction 6-15% 的量化和 θ-shift mechanism 的识别。无 leaderboard audit。\n\n### 致命发现：lz* ≈ accuracy z-score\n\n**这是整个审稿中最重要的发现。** IRT person-fit 框架的全部 psychometric sophistication（4PL 模型拟合、lz* 计算、Snijders 标准化）相对于最简单的 binary baseline（accuracy z-score）仅提升 0.02-0.03 AUROC——实质上无附加值。\n\n这意味着：\n- Item-level response pattern 不包含 aggregate accuracy 之外的有用 contamination 信号\n- IRT model 的 item parameters 未增加 detection signal\n- 论文的方法论前提（\"IRT person-fit is principled and should work better\"）被经验否定\n- θ-shift mechanism 解释了原因：SFT 通过全局 ability 提升改善表现，而非 item-specific cheating，因此 item-level aberrance 信号极弱\n\n### Strengths\n\n**S1. Memorization Fraction 量化 (6-15%)**。将 \"SFT generalization masks signal\" 从定性猜测升级为定量刻画。Eq. 3 将 accuracy gain 分解为 memorization 和 generalization 两部分，解释了 simulation (power 97.9%) 与 reality (2/12 significant) 之间 85-94% 的 power 损失。其他论文未提供此量化。\n\n**S2. θ-Shift Mechanism**。SFT 通过全局 θ 提升改善表现——而非在特定 items 上作弊——是对 IRT 在 LLM 中失效原因的清晰机制解释。有理论洞察。\n\n**S3. lz* vs z-score 对比**。虽是 negative result，但有直接实际指导意义：避免 practitioners 投入资源部署复杂 IRT 框架。这是前几个 dream 版本缺失的关键对照。\n\n**S4. 严谨的 Factorial 实验设计**。4 models × 6 levels × 3 benchmarks 提供了系统性证据。Pilot → Full experiment 的 go/no-go 设计是正确方法论选择。\n\n### Weaknesses\n\n**W1. [Critical/Idea] IRT 框架无附加值**。lz* ≈ accuracy z-score 使整篇论文的 motivation 被动摇。论文报告了此发现但 narrative weight 严重不足——应将其提升为核心 takeaway 而非附带发现。\n\n**W2. [Critical/Idea] Cross-model 结果极弱**。2/12 cells significant，pilot 的 d=1.20 (p=0.03) 在 Bonferroni correction 下不显著（adjusted α=0.0042）。唯一的 \"positive\" 结果可能是 false positive。论文未报告哪 2 个 cells 显著。\n\n**W3. [Critical/Format] 10 页正文超限 2 页**。EMNLP 2026 严格 8-page limit。超出 2 页是明确违规，ARR 系统可能 desk reject。15 tables 过多，大部分应移至 appendix。\n\n**W4. [Warning] QLoRA low-rank constraint 偏向 generalization**。Rank=16 的 low-dimensional update 自然产生 smooth generalizable changes。Memorization fraction 6-15% 可能是 QLoRA-specific lower bound，full fine-tuning 可能产生更高 memorization。\n\n**W5. [Warning] Post-RL >87% signal loss**。对经过 standard RLHF/DPO/GRPO 的模型完全无效。2026 年 SFT-only 模型占比越来越少。\n\n**W6. [Warning] References ~10-15 篇**。远低于 EMNLP 标准。缺少 IRT/person-fit、contamination detection、LLM evaluation 三领域的核心文献。\n\n**W7. [Warning] 0 Figures**。15 tables 无任何可视化。\n\n### Overall Score: 2.5 (Borderline Findings)\n\n3 个 idea/format-level Major (W1 + W2 + W3)。Memorization fraction 和 θ-shift mechanism 有价值但不足以弥补核心方法论前提被否定的缺陷。作为 \"useful cautionary tale\" 有社区价值，但 novelty/impact 不足以达到当前形态下的 Findings acceptance。\n\n---\n\n## Dream 版本对比分析\n\n### 什么决定了 Best (3.5) vs 实际 (2.5) 的 1.0 分差距\n\n| 关键差异 | Best (3.5) | 实际 (2.5) | 影响 |\n|---------|-----------|-----------|------|\n| Detection power | AUROC 0.94 (4/4 models ≥0.91) | 2/12 cells significant | 从\"有效工具\"到\"基本无效\" |\n| Post-RL | 0.88 (63% retention) | >87% loss | 从\"解决 open problem\"到\"确认已知 limitation\" |\n| vs simple baseline | 未比较 | lz* ≈ z-score (+0.02) | 从\"唯一有效方法\"到\"无附加值\" |\n| Leaderboard audit | 11,200 models, 8.3% | 放弃 | 从\"unprecedented scale\"到\"无应用贡献\" |\n| 页数 | ~9 页 (↑0.5) | 10 页 (↑2) | 从 borderline 到明确违规 |\n| Framing | Detection tool (审慎) | Empirical study (诚实) | 实际版 framing 更诚实但 excitement 更低 |\n\n**关键洞察**：Best 档的 3.5 几乎完全建立在 post-RL robustness (AUROC 0.88) 和 strong detection (AUROC 0.94) 的基础上。实际论文的结果否定了这两个核心优势——如果实验无法复现 Best 档的数字，论文必须 reframe。\n\n### 跨版本一致的正面贡献\n\n无论哪个版本，以下贡献被两位 Reviewer 一致认可：\n1. **Power function 理论框架**（R²=0.94-0.96）——可用于评估任意 detection 方法\n2. **Detection frontier 概念**——information level 层级化的 vocabulary\n3. **SFT generalization 的系统性刻画**——对 benchmark integrity 社区有参考价值\n4. **诚实呈现负面结果**——增强可信度\n\n### 跨版本一致的问题\n\n1. 单一污染机制（QLoRA SFT）\n2. 0 figures / 稀疏 references\n3. IRT 参数质量/适用性未验证\n4. Limitations 非独立 section\n\n---\n\n## 对 Research Director 的行动建议\n\n### 不建议当前版本投 EMNLP 2026\n\n理由：3 个 Critical weakness (lz*≈z-score + 2/12 cells + 10 pages)，R1/R2 一致评分 2.5。当前版本强行投出，大概率收到 2.0-2.5 评分。\n\n### 建议修改路径\n\n**Phase 1: Reframe（1-2 周）**\n1. 放弃 \"IRT person-fit as detection tool\" 叙事\n2. 改为 \"Why psychometric person-fit statistics fail for LLM contamination detection: the θ-shift mechanism and memorization fraction decomposition\"\n3. 将 lz* ≈ accuracy z-score 提升为核心 takeaway\n4. 压缩至 8 页（保留 5-6 core tables，加 3-4 figures，移 ablation 至 appendix）\n5. 参考文献扩充至 ≥25\n\n**Phase 2: 实验补强（2-4 周）**\n6. Full fine-tuning 对比验证 memorization fraction 的 QLoRA sensitivity\n7. Multiple testing correction 后的结果呈现\n8. 更多 binary-only baselines（ML classifier on binary vectors）扩展 negative result scope\n9. 如可能增加 pre-training contamination 实验\n\n**Phase 3: 冲击 Best 档数字（高风险、高回报）**\n10. 如果能将 post-RL retention 提升至 ≥60%（AUROC ≥0.85），论文直接升至 3.5 级别\n11. 如果能实现 population-based flagging + leaderboard audit，额外加分\n12. 但这些可能需要方法论突破（如 bootstrap null distribution 替代 theoretical null），不确定性高\n\n### 投稿时间线建议\n\n- **当前 ARR cycle（2026-05-25 deadline）**：不投\n- **下一个 ARR cycle（约 2026-07）**：如完成 Phase 1+2，以 reframed negative result 投出，目标 3.0 (Findings)\n- **如果 Phase 3 突破**：目标 3.5 (Borderline Conference)\n\n---\n\n## Questions for Authors\n\nQ1. 2/12 significant cells 具体是哪两个 model × benchmark？如果都是 MMLU 则指向 n_items 限制；如果跨 benchmark 则指向 model-specific 因素。\n\nQ2. 是否测试过更高 QLoRA rank（64/128）或 full fine-tuning？Memorization fraction 是否对 SFT 方法敏感？\n\nQ3. 既然 lz* ≈ z-score，是否考虑重新定位论文为 \"accuracy z-score is a sufficient proxy, IRT adds no value\"？\n\nQ4. Pilot 的 d=1.20, p=0.03 是否 survive multiple testing correction？论文如何处理 12 次比较的问题？\n\nQ5. Universal 4PL misfit 下，基于 IRT parameters 的 lz* 的理论保证（asymptotic normality under null）都不成立。如何 reconcile？\n\nQ6. acc_ceiling 的定义对 memorization fraction 计算有多敏感？替代定义下数字如何变化？\n\n---\n\n## Missing References\n\n**IRT / Person-Fit:**\nDrasgow, Levine & Williams (1985); Karabatsos (2003); Meijer & Sijtsma (2001)\n\n**Contamination Detection:**\nOren et al. (2024); Polo et al. (2024); Magar & Schwartz (2022); Deng et al. (2024)\n\n**LLM Evaluation:**\nBurnham et al. (2024) IRT for AI; Jacobs et al. (2024) psychometrics and AI\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n## Visual Layout Check\n\n视觉审查：未启动（not_started）。\n\n---\n\n## Reviewer 共识记录（最终）\n\n| 版本 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Dream Best | 3.5 | 3.5 | ✅ |\n| Dream Median | 3.0 | 3.0 | ✅ |\n| Dream Worst | 2.5 | 2.5 | ✅ |\n| 实际论文 | 2.5 | 2.5 | ✅ |\n\n**四份审稿完全一致，无任何未解决分歧。**\n\nR1/R2 共同建议：不投当前版本，reframe 为 negative result + mechanistic explanation，修复 format 和实验后下一个 ARR cycle 投出，目标 3.0。",
  "project": "irt_personfit_contam",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "Dream Best: 3.5 | Dream Median: 3.0 | Dream Worst: 2.5 | 实际论文: 2.5 — 不建议当前版本投稿",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告（最终版）：irt_personfit_contam — 三档 Dream + 实际论文综合评估\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n**Round**: 1\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)\n**收敛状态**: 四份审稿评分完全一致（R1 = R2），无分歧\n\n⚠️ **本报告为最终版**，替换此前所有提交。覆盖 3 个 dream 版本 + 实际论文。\n\n---\n\n## 评分总览\n\n| 版本 | R1 | R2 | 共识 | 投稿建议 |\n|------|----|----|------|---------|\n| Dream Best | 3.5 | 3.5 | ✅ | 理想目标，需 presentation 修复 |\n| Dream Median | 3.0 | 3.0 | ✅ | — |\n| Dream Worst | 2.5 | 2.5 | ✅ | — |\n| **实际论文** | **2.5** | **2.5** | ✅ | **不建议当前版本直接投** |\n\n**核心结论：实际论文落在 Worst 档附近（2.5），远未达到 Best 档（3.5）。需要重大修改后再投稿。**\n\n---\n\n## 实际论文评估（最高优先级）\n\n### 标题\n\"Psychometric Diagnostics for LLM Benchmark Evaluation: Quantifying the Limits of Binary-Only Contamination Detection via IRT Person-Fit\"\n\n### Summary\n论文通过控制实验（4 models × 6 contamination levels × 3 benchmarks）量化 IRT person-fit (lz*) 在 binary-only 条件下的检测边界。核心发现是负面的：(1) cross-model 仅 2/12 cells 在 15% contamination 时显著；(2) lz* 仅比最简单的 accuracy z-score 高 0.02-0.03 AUROC；(3) post-RL signal loss >87%。正面贡献包括 memorization fraction 6-15% 的量化和 θ-shift mechanism 的识别。无 leaderboard audit。\n\n### 致命发现：lz* ≈ accuracy z-score\n\n**这是整个审稿中最重要的发现。** IRT person-fit 框架的全部 psychometric sophistication（4PL 模型拟合、lz* 计算、Snijders 标准化）相对于最简单的 binary baseline（accuracy z-score）仅提升 0.02-0.03 AUROC——实质上无附加值。\n\n这意味着：\n- Item-level response pattern 不包含 aggregate accuracy 之外的有用 contamination 信号\n- IRT model 的 item parameters 未增加 detection signal\n- 论文的方法论前提（\"IRT person-fit is principled and should work better\"）被经验否定\n- θ-shift mechanism 解释了原因：SFT 通过全局 ability 提升改善表现，而非 item-specific cheating，因此 item-level aberrance 信号极弱\n\n### Strengths\n\n**S1. Memorization Fraction 量化 (6-15%)**。将 \"SFT generalization masks signal\" 从定性猜测升级为定量刻画。Eq. 3 将 accuracy gain 分解为 memorization 和 generalization 两部分，解释了 simulation (power 97.9%) 与 reality (2/12 significant) 之间 85-94% 的 power 损失。其他论文未提供此量化。\n\n**S2. θ-Shift Mechanism**。SFT 通过全局 θ 提升改善表现——而非在特定 items 上作弊——是对 IRT 在 LLM 中失效原因的清晰机制解释。有理论洞察。\n\n**S3. lz* vs z-score 对比**。虽是 negative result，但有直接实际指导意义：避免 practitioners 投入资源部署复杂 IRT 框架。这是前几个 dream 版本缺失的关键对照。\n\n**S4. 严谨的 Factorial 实验设计**。4 models × 6 levels × 3 benchmarks 提供了系统性证据。Pilot → Full experiment 的 go/no-go 设计是正确方法论选择。\n\n### Weaknesses\n\n**W1. [Critical/Idea] IRT 框架无附加值**。lz* ≈ accuracy z-score 使整篇论文的 motivation 被动摇。论文报告了此发现但 narrative weight 严重不足——应将其提升为核心 takeaway 而非附带发现。\n\n**W2. [Critical/Idea] Cross-model 结果极弱**。2/12 cells significant，pilot 的 d=1.20 (p=0.03) 在 Bonferroni correction 下不显著（adjusted α=0.0042）。唯一的 \"positive\" 结果可能是 false positive。论文未报告哪 2 个 cells 显著。\n\n**W3. [Critical/Format] 10 页正文超限 2 页**。EMNLP 2026 严格 8-page limit。超出 2 页是明确违规，ARR 系统可能 desk reject。15 tables 过多，大部分应移至 appendix。\n\n**W4. [Warning] QLoRA low-rank constraint 偏向 generalization**。Rank=16 的 low-dimensional update 自然产生 smooth generalizable changes。Memorization fraction 6-15% 可能是 QLoRA-specific lower bound，full fine-tuning 可能产生更高 memorization。\n\n**W5. [Warning] Post-RL >87% signal loss**。对经过 standard RLHF/DPO/GRPO 的模型完全无效。2026 年 SFT-only 模型占比越来越少。\n\n**W6. [Warning] References ~10-15 篇**。远低于 EMNLP 标准。缺少 IRT/person-fit、contamination detection、LLM evaluation 三领域的核心文献。\n\n**W7. [Warning] 0 Figures**。15 tables 无任何可视化。\n\n### Overall Score: 2.5 (Borderline Findings)\n\n3 个 idea/format-level Major (W1 + W2 + W3)。Memorization fraction 和 θ-shift mechanism 有价值但不足以弥补核心方法论前提被否定的缺陷。作为 \"useful cautionary tale\" 有社区价值，但 novelty/impact 不足以达到当前形态下的 Findings acceptance。\n\n---\n\n## Dream 版本对比分析\n\n### 什么决定了 Best (3.5) vs 实际 (2.5) 的 1.0 分差距\n\n| 关键差异 | Best (3.5) | 实际 (2.5) | 影响 |\n|---------|-----------|-----------|------|\n| Detection power | AUROC 0.94 (4/4 models ≥0.91) | 2/12 cells significant | 从\"有效工具\"到\"基本无效\" |\n| Post-RL | 0.88 (63% retention) | >87% loss | 从\"解决 open problem\"到\"确认已知 limitation\" |\n| vs simple baseline | 未比较 | lz* ≈ z-score (+0.02) | 从\"唯一有效方法\"到\"无附加值\" |\n| Leaderboard audit | 11,200 models, 8.3% | 放弃 | 从\"unprecedented scale\"到\"无应用贡献\" |\n| 页数 | ~9 页 (↑0.5) | 10 页 (↑2) | 从 borderline 到明确违规 |\n| Framing | Detection tool (审慎) | Empirical study (诚实) | 实际版 framing 更诚实但 excitement 更低 |\n\n**关键洞察**：Best 档的 3.5 几乎完全建立在 post-RL robustness (AUROC 0.88) 和 strong detection (AUROC 0.94) 的基础上。实际论文的结果否定了这两个核心优势——如果实验无法复现 Best 档的数字，论文必须 reframe。\n\n### 跨版本一致的正面贡献\n\n无论哪个版本，以下贡献被两位 Reviewer 一致认可：\n1. **Power function 理论框架**（R²=0.94-0.96）——可用于评估任意 detection 方法\n2. **Detection frontier 概念**——information level 层级化的 vocabulary\n3. **SFT generalization 的系统性刻画**——对 benchmark integrity 社区有参考价值\n4. **诚实呈现负面结果**——增强可信度\n\n### 跨版本一致的问题\n\n1. 单一污染机制（QLoRA SFT）\n2. 0 figures / 稀疏 references\n3. IRT 参数质量/适用性未验证\n4. Limitations 非独立 section\n\n---\n\n## 对 Research Director 的行动建议\n\n### 不建议当前版本投 EMNLP 2026\n\n理由：3 个 Critical weakness (lz*≈z-score + 2/12 cells + 10 pages)，R1/R2 一致评分 2.5。当前版本强行投出，大概率收到 2.0-2.5 评分。\n\n### 建议修改路径\n\n**Phase 1: Reframe（1-2 周）**\n1. 放弃 \"IRT person-fit as detection tool\" 叙事\n2. 改为 \"Why psychometric person-fit statistics fail for LLM contamination detection: the θ-shift mechanism and memorization fraction decomposition\"\n3. 将 lz* ≈ accuracy z-score 提升为核心 takeaway\n4. 压缩至 8 页（保留 5-6 core tables，加 3-4 figures，移 ablation 至 appendix）\n5. 参考文献扩充至 ≥25\n\n**Phase 2: 实验补强（2-4 周）**\n6. Full fine-tuning 对比验证 memorization fraction 的 QLoRA sensitivity\n7. Multiple testing correction 后的结果呈现\n8. 更多 binary-only baselines（ML classifier on binary vectors）扩展 negative result scope\n9. 如可能增加 pre-training contamination 实验\n\n**Phase 3: 冲击 Best 档数字（高风险、高回报）**\n10. 如果能将 post-RL retention 提升至 ≥60%（AUROC ≥0.85），论文直接升至 3.5 级别\n11. 如果能实现 population-based flagging + leaderboard audit，额外加分\n12. 但这些可能需要方法论突破（如 bootstrap null distribution 替代 theoretical null），不确定性高\n\n### 投稿时间线建议\n\n- **当前 ARR cycle（2026-05-25 deadline）**：不投\n- **下一个 ARR cycle（约 2026-07）**：如完成 Phase 1+2，以 reframed negative result 投出，目标 3.0 (Findings)\n- **如果 Phase 3 突破**：目标 3.5 (Borderline Conference)\n\n---\n\n## Questions for Authors\n\nQ1. 2/12 significant cells 具体是哪两个 model × benchmark？如果都是 MMLU 则指向 n_items 限制；如果跨 benchmark 则指向 model-specific 因素。\n\nQ2. 是否测试过更高 QLoRA rank（64/128）或 full fine-tuning？Memorization fraction 是否对 SFT 方法敏感？\n\nQ3. 既然 lz* ≈ z-score，是否考虑重新定位论文为 \"accuracy z-score is a sufficient proxy, IRT adds no value\"？\n\nQ4. Pilot 的 d=1.20, p=0.03 是否 survive multiple testing correction？论文如何处理 12 次比较的问题？\n\nQ5. Universal 4PL misfit 下，基于 IRT parameters 的 lz* 的理论保证（asymptotic normality under null）都不成立。如何 reconcile？\n\nQ6. acc_ceiling 的定义对 memorization fraction 计算有多敏感？替代定义下数字如何变化？\n\n---\n\n## Missing References\n\n**IRT / Person-Fit:**\nDrasgow, Levine & Williams (1985); Karabatsos (2003); Meijer & Sijtsma (2001)\n\n**Contamination Detection:**\nOren et al. (2024); Polo et al. (2024); Magar & Schwartz (2022); Deng et al. (2024)\n\n**LLM Evaluation:**\nBurnham et al. (2024) IRT for AI; Jacobs et al. (2024) psychometrics and AI\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n## Visual Layout Check\n\n视觉审查：未启动（not_started）。\n\n---\n\n## Reviewer 共识记录（最终）\n\n| 版本 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Dream Best | 3.5 | 3.5 | ✅ |\n| Dream Median | 3.0 | 3.0 | ✅ |\n| Dream Worst | 2.5 | 2.5 | ✅ |\n| 实际论文 | 2.5 | 2.5 | ✅ |\n\n**四份审稿完全一致，无任何未解决分歧。**\n\nR1/R2 共同建议：不投当前版本，reframe 为 negative result + mechanistic explanation，修复 format 和实验后下一个 ARR cycle 投出，目标 3.0。",
    "project": "irt_personfit_contam",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "Dream Best: 3.5 | Dream Median: 3.0 | Dream Worst: 2.5 | 实际论文: 2.5 — 不建议当前版本投稿",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-20T20:00:04.275992+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4277
}
```

</details>

---


### Assistant

_source line 135 · 2026-05-20T20:00:16.116428+00:00_

最终审稿报告已投递给 Research Director。

**审稿结论摘要**：

- **实际论文 2.5 (Borderline Findings)**——不建议当前版本投 EMNLP 2026
- 致命发现：lz* 仅比 accuracy z-score 高 0.02-0.03 AUROC，IRT 框架无实质附加值
- Dream Best 档 3.5 的核心优势（AUROC 0.94, post-RL 0.88）在实际结果中未实现
- 建议：reframe 为 negative result + θ-shift mechanism 论文，修复 format（8 页、加 figures、扩 refs），下一个 ARR cycle（~2026-07）再投，目标 3.0 Findings
- Issue tracker 已更新（20 issues），R1/R2 四份审稿完全一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 136 · 2026-05-20T20:00:18.725228+00:00_

[Reviewer 2 审稿结果]:
已提交。实际论文评分 2.5，与 R1 完全一致。核心判断：lz* ≈ accuracy z-score 动摇了整篇论文的动机，加上 10 页超限和 2/12 cells 的多重检验问题，当前版本不建议直接投 EMNLP 2026。建议 reframe 为 negative result paper + 格式修正 + 实验补强后下一个 ARR cycle 再投。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 137 · 2026-05-20T20:00:27.394543+00:00_

审稿圆桌会议全部完成。最终报告已投递给 Research Director。

**结果摘要**：

- **实际论文 2.5** — 不建议当前版本投 EMNLP 2026 May cycle
- Dream Best 3.5 / Median 3.0 / Worst 2.5
- R1 与 R2 四份审稿评分完全一致，无分歧
- 核心问题：lz* 仅比 accuracy z-score 高 0.02-0.03 AUROC，IRT 框架无实质性附加值
- 建议 reframe 为 negative result paper，修复格式和实验后下一个 ARR cycle（~2026-07）投出，目标 3.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 20

## Round 20

4 recorded events


### User

_source line 138 · 2026-05-21T04:16:47.482560+00:00_

[Reviewer 1 审稿意见]:
## Complete ARR-Style Review
**Paper:** "When Can Binary Response Patterns Detect Benchmark Contamination? An IRT Person-Fit Characterization"
**Reviewer:** R1

---

### 1. Summary

论文研究 IRT person-fit 统计量 (lz*) 能否利用 binary response data 检测 LLM benchmark contamination。通过 4 model families × 3 benchmarks × 6 contamination levels 的控制实验，论文发现检测仅在特定条件下成功：高 memorization fraction 的模型（Qwen/Llama, m_f=0.32-0.35）在大 benchmark（MMLU, 14K items）上可检测 15% 污染（|d|=1.8-2.8），但低 memorization fraction 模型（Gemma/Mistral, m_f=0.15-0.17）和小 benchmark（GSM8K）上检测失败。AUROC 0.62 落后于 token-probability 方法 23pp（Min-K++ 0.82, ConStat 0.85）。Post-RL (GRPO) 后信号几乎完全消失（|d| 从 2.5 降至 0.3）。论文将自身定位为 "characterization"——刻画 binary-only 检测的边界条件——而非提出检测工具。

---

### 2. Soundness: 2.5 / 5

**支撑 claims 的证据：**

(+) **控制实验设计是 sound 的**：factorial design 覆盖了关键维度（model × benchmark × contamination level），QLoRA SFT 注入是合理的 contamination proxy。memorization fraction (Table 4) 和 θ-shift identification 提供了因果性解释。

(+) **4PL vs 3PL ablation (Table 1)** 合理：FAR 从 12% 降至 5%，power gain +12-18pp，支持 4PL 作为 default choice。Simulation 层面的结论有效。

(-) **n=3 seeds per condition 对 Cohen's d 估计严重不足** [major concern]：d=1.8 (pilot) 和 d=2.8 (Qwen cross-family) 基于 3 seeds 的 paired comparison。3 个数据点的 effect size 估计极不稳定——Cohen's d 的 95% CI 在 n=3 下宽度约为 ±2.0。这意味着 d=1.8 的实际 CI 可能是 [-0.2, 3.8]，无法排除 null effect。Table 2 pilot 的 p=0.03（假设 paired t-test, df=2）在如此小的 df 下可信度有限。论文应报告 bootstrap CI 或使用 Bayesian estimation。

(-) **Power function R²=0.65 不够 convincing** [moderate]：R²=0.65 意味着 35% 的 variance 未被 √n 理论解释。与前几个版本（R²=0.94-0.97）相比，这个 fit 明显更差。可能原因：(a) memorization fraction 的 model-specific 差异引入了理论未建模的 variance，(b) 5-7 个 data points 的 R² 估计本身不稳定。论文声称 power function 提供 "predictive theory"，但 R²=0.65 的预测精度有限。

(-) **Table 2 的非单调性需要更多解释**：50% contamination 的 |d|=0.5 低于 15% 的 |d|=1.8——论文归因于 θ-shift（高污染导致 θ 大幅提升，lz* 在 higher θ 下的 sensitivity 降低）。这是合理的机制解释，但它暗示 lz* 统计量本身的设计存在根本问题：它将 contamination-driven ability gain 与 genuine ability 混淆。θ-fixed correction (Section 3.3, Table 5) 部分解决了这个问题，但仅对 Qwen/Llama 有效。

(-) **θ-fixed correction 的实际可用性严重受限**：需要知道 clean baseline 的 θ 才能进行 correction。在实际场景中（审计 leaderboard 上的未知模型），clean baseline 不可用。这使得 θ-fixed correction 成为一个仅在 controlled experiments 中有效的理论工具，而非 practical detection method。

(-) **Baseline comparison 跨 information levels** [moderate]：Table 6 比较 lz* (binary) vs Min-K++ (token probs) vs ConStat (re-test)。这些方法使用不同 information levels，direct AUROC comparison 不完全公平。但论文的 framing 是 "quantifying the cost of minimal information"，这使得比较的 purpose 是合理的。缺少的是 **同一 information level** 内的对照——论文是否包含 accuracy z-score 作为 binary-only baseline？如果 lz* 与 accuracy z-score 相当（如前一篇论文中观察到的 +0.02-0.03 AUROC），IRT 框架的附加值将进一步被质疑。

(-) **Extended benchmarks 的 "custom calibration"** [moderate]：BBH 和 MATH 的 4PL 参数来源不明。如果是作者自行校准的（而非使用 established item bank 如 PSN-IRT），参数质量不确定。这会影响 power function validation 的可信度。

---

### 3. Excitement / Novelty: 2.5 / 5

**Novel 元素：**

(+) **"Detection frontier" framing 和 information access spectrum** 是有用的概念贡献。将检测方法按 information access level 组织（binary < re-test < token probs < weights < training data）为整个领域提供了一个 organizing framework。

(+) **Memorization fraction 的 model-family 异质性** (Qwen/Llama 0.32-0.35 vs Gemma/Mistral 0.15-0.17) 是 genuinely interesting finding。这量化了 "不同模型架构的 SFT 记忆能力不同"，为 contamination detection 的 model-dependent boundary 提供了定量解释。

(+) **Universal 4PL misfit 在经验上确认了 LLM ≠ test-taker**。虽然有直觉预期，但 systematic documentation 有独立价值。

(+) **Classical vs neural IRT gap (Table 13)**：classical MML-EM 在 N=520 时 a_r=0.13（essentially dead）是一个 practically important negative result——它告诉 practitioners "不要尝试从 leaderboard data 重新估计 IRT 参数"。

(-) **核心 negative result 不令人惊讶**：binary responses 包含的信息量远低于 token probabilities，检测力更弱是直觉可预期的。

(-) **Post-RL failure (Table 8-9) 与 Wang et al. (2025) 一致**，不是独立新发现。

(-) **"Characterization" framing 的贡献 weight**：论文诚实地不 overclaim，但 "我们刻画了边界条件" 的贡献比 "我们提出了一个有效方法" 明显更弱。对 EMNLP Main 来说，characterization 需要产出 actionable insights——论文的主要 actionable insight 是 "don't use IRT person-fit for contamination detection unless you have a large benchmark, a model with high memorization fraction, and no post-RL training"，这是一个非常 narrow 的使用条件。

(-) **Leaderboard audit 放弃后没有 applied contribution**：论文完全停留在方法论/分析层面，没有任何大规模实际应用。

---

### 4. Reproducibility: 3.0 / 5

(+) 论文声称将 release checkpoints 和 code——如果兑现，reproducibility 将大幅提升。
(+) 14 tables 提供了详细的数值结果。
(+) QLoRA hyperparameters 应有详细说明（rank, learning rate, epochs）。

(-) n=3 seeds 意味着 reproduced experiments 可能得到显著不同的 effect sizes。
(-) PSN-IRT 参数来源细节不明——是否使用了 specific version 的 item bank？
(-) BBH/MATH 的 "custom calibration" 过程不透明。
(-) GRPO hyperparameters（reward function, KL penalty, number of steps）的详细程度未知。

---

### 5. Strengths

- **诚实的 characterization framing**：论文没有 overclaim detection success。在 2/4 families × 1/3 benchmarks 的 limited positive results 下，将自身定位为 "boundary conditions characterization" 是科学上诚实的选择。
- **Memorization fraction concept (Table 4)**：将 accuracy gain 分解为 memorization vs generalization，并量化 model-family 差异（Qwen/Llama 0.32-0.35 vs Gemma/Mistral 0.15-0.17），提供了 contamination detection 文献中之前缺失的定量框架。
- **θ-shift identification 和 non-monotonicity explanation**：发现 50% contamination 的 |d| 低于 15%（Table 2）并用 θ-shift mechanism 解释，是一个 non-obvious finding。它揭示了 IRT person-fit 在 high-contamination regime 下的反直觉行为。
- **实验覆盖广泛**：4 families × 3 benchmarks × 6 levels + post-RL + baselines + ablations + extended benchmarks + domain analysis + IRT refit + natural experiment。所有非 abandoned 实验均有覆盖。
- **Classical IRT refit failure (Table 13)** 是 practically important negative result，告知 practitioners 不要尝试在 leaderboard scale 上重新校准 IRT 参数。

---

### 6. Weaknesses

- **[Major] Detection 极度 limited**：仅在 2/4 model families × 1/3 benchmarks（MMLU only）× pre-RL 条件下工作。实际可用范围极窄——排除了低 memorization fraction 模型、小 benchmarks、post-RL 模型。这使得方法在实践中几乎无法部署。

- **[Major] n=3 seeds 的 statistical adequacy**：Cohen's d 在 n=3 下的估计极不稳定。d=1.8 和 d=2.8 的 point estimates 可能 informative，但 CI 太宽而无法支撑 strong claims。Table 3 中 Gemma (d=-0.7) 和 Mistral (d=-0.4) 的 CI 可能跨越 0，使得 "these families are undetectable" 的 claim 也不够 robust。

- **[Major] AUROC 0.62 vs 0.82-0.85 的 23pp gap**：论文将此 frame 为 "cost of minimal information"，但 23pp 是一个巨大的 practical gap。更关键的是 Table 7 显示 gap 从 3% contamination 时的 8pp 扩大到 15% 时的 23pp——这意味着在 low contamination regime（最需要检测的场景），IRT-FIT 的 relative disadvantage 更大。

- **[Major] Post-RL failure + θ-fixed 需要 clean baseline** = 双重 practical limitation：post-RL 后方法失效（Table 8-9），而 θ-fixed correction 需要 clean baseline（controlled experiment 专用）。这意味着方法仅在 "你自己训练了模型并保留了 clean checkpoint" 的场景下有用——但在这种场景下你已经知道 contamination status，不需要检测。

- **[Moderate] Power function R²=0.65 不足以称为 "predictive theory"**：35% unexplained variance 意味着 power 预测有很大不确定性。这限制了论文 Claim 关于 "practitioners can predict detection feasibility from benchmark size" 的价值。

- **[Moderate] Natural experiment (Table 14) severely underpowered**：n=4 base→chat pairs，all p>0.28。这个实验几乎没有统计力，inclusion 的价值可疑。如果仅用于 "demonstrate method on real data"，n=4 无法产生任何有意义的结论。应移至 appendix 或删除，以腾出空间。

- **[Moderate] Cross-benchmark aggregation (Table 12) degrades AUROC**：lzm aggregation 不仅没有改善检测，反而降低了 AUROC。这个 negative result 值得一句话提及但不值得占 main text 篇幅。

- **[Minor] 9 references 严重不足**：cross-disciplinary 论文（IRT × contamination detection × LLM evaluation）通常需要 25-40 references 覆盖三个领域。9 references 暗示 related work 覆盖严重不足。

---

### 7. Questions for Authors

1. **Accuracy z-score baseline**: 论文是否比较了 lz* 与最简单的 binary-only baseline——accuracy z-score（某模型的 accuracy 相对于同类模型的 z-score）？如果 lz* 的 AUROC 仅比 accuracy z-score 高 2-3pp（如类似研究发现的那样），那么整个 IRT 框架的附加值需要重新讨论。Table 6 中是否包含了 accuracy z-score？

2. **Memorization fraction 对 SFT 方法的敏感性**: m_f=0.15-0.17 (Gemma/Mistral) 是否是 QLoRA rank=16 的 artifact？如果使用更高 rank（如 64）或 full fine-tuning，memorization fraction 是否会上升到可检测水平？这直接影响 "detection boundary" 的 generalizability。

3. **Non-monotonicity 的 robustness**: Table 2 中 50% contamination 的 |d|=0.5 低于 15% 的 |d|=1.8。这个 non-monotonic pattern 在 4 个 model families 中是否一致？如果仅出现在 Qwen pilot 中，它可能是 model-specific 现象而非 general property of lz*。

4. **Leaderboard audit 放弃的具体原因**: 论文是否讨论了为什么放弃 leaderboard audit？是因为 (a) detection power 不足以产生 meaningful flagging，(b) 数据处理困难，还是 (c) 结果与 controlled experiments 不一致？原因的不同对论文的 interpretation 有重大影响。

5. **Table 13 的 classical IRT refit**：a_r=0.13 at N=520 是否意味着 classical MML-EM 根本无法恢复有意义的 discrimination parameters？论文是否尝试了 larger N（如 N=2000+）或 alternative estimation methods（如 MCMC-based Bayesian IRT）？

---

### 8. Missing References

**严重缺失（9 references 远低于标准）：**

*IRT / Person-Fit 经典文献：*
- Karabatsos, G. (2003). Comparing the aberrant response detection performance of thirty-six person-fit statistics. *Applied Measurement in Education.*
- Drasgow, F., Levine, M., & Williams, E. (1985). Appropriateness measurement with polychotomous item response models and standardized indices.
- Van der Flier, H. (1982). Deviant response patterns and comparability of test scores. *Journal of Cross-Cultural Psychology.*

*Contamination Detection：*
- Oren, Y. et al. (2024). Proving test set contamination in black box language models. *ICLR.*
- Deng, Y. et al. (2024). Investigating data contamination in modern benchmarks for LLMs. *NAACL.*
- Polo, F. M. et al. (2024). tinyBenchmarks. *ICML.*
- Magar, I. & Schwartz, R. (2022). Data contamination: From memorization to exploitation. *ACL.*
- Dekoninck, J. et al. (2024). ConStat in detail (if only briefly cited).
- Golchin, S. & Surdeanu, M. (2024). Time Travel Probing.

*SFT / RLHF 文献：*
- Ouyang, L. et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS.*
- Relevant SFT generalization studies.

*IRT for LLM：*
- Any other work applying IRT to LLM evaluation beyond PSN-IRT.

**9 references 是一个 red flag**——审稿人通常期望看到对领域的全面了解。

---

### 9. Formatting / Compliance

| 检查项 | 状态 | 详情 |
|--------|------|------|
| Page limit | ✅ Compliant | 8 pages main text + Limitations + References on pages 9-11 |
| Limitations | ✅ Present | 独立 section，appears on page 9-10 |
| Anonymity | ✅ Maintained | 基于描述 |
| Responsible NLP Checklist | ⚠️ Not confirmed | 未提及 Sections A-E checklist |
| Hallucinated citations | ⚠️ Cannot verify | 仅 9 references，但无法逐条核实 |
| Reference count | ❌ Severely insufficient | 9 references for a cross-disciplinary paper |

**Page limit compliance is good**——8 pages main text + separate Limitations is within EMNLP rules。这是相对于其他版本的一个改进。

---

### 10. Overall Assessment: 2.5 / 5 (Borderline Findings)

**Calibration reasoning：**

*Counting Major issues：* 3 idea-level Majors (limited detection scope, n=3 statistical adequacy, AUROC gap + practical inapplicability) → 按校准规则，3+ Major issues → 不高于 Borderline Reject。

*Mitigating factors：*
- 论文 framing 诚实，不 overclaim
- Memorization fraction 和 θ-shift 是 genuine methodological insights
- 实验覆盖广泛（所有非 abandoned 实验均有覆盖）
- Page limit compliant（相对于其他版本的改进）

*Aggravating factors：*
- 核心检测仅在 2/4 families × 1/3 benchmarks × pre-RL 条件下工作——scope 极窄
- AUROC 0.62 在实际应用中 barely useful（random = 0.50）
- Post-RL failure + θ-fixed 需要 clean baseline → 实际部署场景为 null set
- 9 references → related work 覆盖严重不足
- Natural experiment (n=4) 和 cross-benchmark aggregation (degrades AUROC) 占用篇幅但贡献 negative

**Final verdict：** 论文是一个执行认真的 characterization study，产出了有价值的 methodological insights（memorization fraction, θ-shift, classical IRT gap）。但核心检测能力极为有限（2/4 × 1/3 × pre-RL only, AUROC 0.62），post-RL failure 和 θ-fixed 的 clean-baseline requirement 使方法在实际场景中不可部署，leaderboard audit 被放弃消除了 applied contribution。

对于 EMNLP Main (top 21%)：不推荐。贡献不足以进入 top 20%。

对于 Findings：Borderline。Memorization fraction concept 和 θ-shift mechanism 如果充分发展（更大 n, 更多 model families, accuracy z-score baseline 对比），可以达到 Findings level。当前版本的 statistical rigor (n=3) 和 reference coverage (n=9) 不足。

**Recommendation：** Borderline Reject / Borderline Findings。如果 (1) 增加 seeds 到 ≥10 并报告 bootstrap CI，(2) 增加 accuracy z-score baseline，(3) 扩展 references 到 ≥20，(4) 讨论 leaderboard audit abandonment 原因，可提升至 Findings (3.0)。

---

### 11. Confidence: 4 / 5

对 IRT/person-fit statistics、contamination detection 方法（ConStat, Min-K++, CoDeC）、LLM evaluation practices 和 SFT/RLHF training 有充分了解。对 PSN-IRT 参数的具体校准过程和 classical IRT estimation 的 technical details 了解略有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 139 · 2026-05-21T04:17:38.690644+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "text": "## 简要交叉分享：R1 对实际论文修订版的审稿——评分仍为 2.5\n\nR1 审了另一个版本的实际论文（\"When Can Binary Response Patterns Detect Benchmark Contamination?\"），评分 2.5 不变。\n\n**改进**（vs 前一版）：\n- ✅ 页数合规（8 页）\n- ✅ Limitations 独立 section\n- ✅ Framing 更诚实（\"characterization\" 而非 \"detection tool\"）\n\n**核心问题不变**：\n- AUROC 0.62（vs Min-K++ 0.82, ConStat 0.85，gap 23pp）\n- 检测仅在 2/4 model families × MMLU × pre-RL 有效（scope 极窄）\n- Post-RL: |d| 从 2.5 降至 0.3\n- 9 references\n\n**新发现**：\n1. **n=3 seeds 统计力严重不足**：Cohen's d CI 在 n=3 下宽 ±2.0，d=1.8 的 CI 可能是 [-0.2, 3.8]\n2. **Power function R²=0.65**（dream 版 0.94-0.97）——35% unexplained variance\n3. **θ-fixed correction 需 clean baseline**——实际场景不可用（你已知 contamination status 的场景不需要检测）\n4. **Memorization fraction 异质性**：Qwen/Llama 0.32-0.35 vs Gemma/Mistral 0.15-0.17（仅高 m_f 模型可检测）\n5. **lzm cross-benchmark aggregation 反而降低 AUROC**\n6. **Classical IRT refit**: a_r=0.13 at N=520（MML-EM 在 leaderboard scale 完全失效）\n\n**R1 升级路径 (2.5→3.0)**：\n1. Seeds ≥10 + bootstrap CI\n2. 加 accuracy z-score baseline\n3. References ≥20\n4. 讨论 leaderboard audit 放弃原因\n\n---\n\n请简要确认：你对这个版本的评分是否也是 2.5？有无新的关注点？",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "text": "## 简要交叉分享：R1 对实际论文修订版的审稿——评分仍为 2.5\n\nR1 审了另一个版本的实际论文（\"When Can Binary Response Patterns Detect Benchmark Contamination?\"），评分 2.5 不变。\n\n**改进**（vs 前一版）：\n- ✅ 页数合规（8 页）\n- ✅ Limitations 独立 section\n- ✅ Framing 更诚实（\"characterization\" 而非 \"detection tool\"）\n\n**核心问题不变**：\n- AUROC 0.62（vs Min-K++ 0.82, ConStat 0.85，gap 23pp）\n- 检测仅在 2/4 model families × MMLU × pre-RL 有效（scope 极窄）\n- Post-RL: |d| 从 2.5 降至 0.3\n- 9 references\n\n**新发现**：\n1. **n=3 seeds 统计力严重不足**：Cohen's d CI 在 n=3 下宽 ±2.0，d=1.8 的 CI 可能是 [-0.2, 3.8]\n2. **Power function R²=0.65**（dream 版 0.94-0.97）——35% unexplained variance\n3. **θ-fixed correction 需 clean baseline**——实际场景不可用（你已知 contamination status 的场景不需要检测）\n4. **Memorization fraction 异质性**：Qwen/Llama 0.32-0.35 vs Gemma/Mistral 0.15-0.17（仅高 m_f 模型可检测）\n5. **lzm cross-benchmark aggregation 反而降低 AUROC**\n6. **Classical IRT refit**: a_r=0.13 at N=520（MML-EM 在 leaderboard scale 完全失效）\n\n**R1 升级路径 (2.5→3.0)**：\n1. Seeds ≥10 + bootstrap CI\n2. 加 accuracy z-score baseline\n3. References ≥20\n4. 讨论 leaderboard audit 放弃原因\n\n---\n\n请简要确认：你对这个版本的评分是否也是 2.5？有无新的关注点？",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 140 · 2026-05-21T04:17:42.609854+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3919
}
```

</details>

---


### Assistant

_source line 141 · 2026-05-21T04:18:00.316502+00:00_

交叉分享已发送。等待 R2 确认后，如果评分一致（预期 2.5），则审稿流程完成——最终报告（已提交）的核心结论不变：

**实际论文 2.5，不建议当前版本直接投 EMNLP 2026。Dream Best 3.5 是可达目标，需 reframe + 实验补强。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 21

## Round 21

24 recorded events


### User

_source line 142 · 2026-05-21T04:18:02.999430+00:00_

[Reviewer 1 审稿结果]:
审稿已提交。五篇论文全部完成审阅：

| 论文 | 档位 | Overall | 核心判断 |
|------|------|---------|---------|
| IRT-FIT: Detection Frontier | median | 3.0 | Leaderboard audit baseline chicken-and-egg + post-RL scope gap |
| Binary Response Bottleneck | worst | 2.5 | Information-theoretic bound overclaim + 单一污染机制 |
| IRT-FIT: Detecting Benchmark Contamination | best | 3.5 | Post-RL robustness 亮眼，但 page limit 和 leaderboard validation gap |
| Psychometric Diagnostics (无 PDF) | realistic-a | 2.5 | lz* ≈ accuracy z-score，IRT 框架无附加值 |
| When Can Binary Response Patterns | realistic-b | 2.5 | 2/4 families × 1/3 benchmarks，n=3 seeds 统计力不足 |

---

[Reviewer 2 审稿意见]:
## R2 确认：实际论文修订版评分 2.5

**评分：2.5 (Borderline Findings)**，与 R1 一致。

格式合规是必要改进但不改变实质评判。核心问题仍在：

**最关注的 3 点**：

1. **n=3 seeds**：这是我此前未充分关注的问题，R1 抓得好。n=3 下 Cohen's d 的 CI 宽到几乎无法得出有意义的统计结论。d=1.8 ± 2.0 意味着真实效应可能为零。这不是 "should-fix" 而是 "must-fix"——当前所有显著性声称的统计基础都不可靠。

2. **Memorization fraction 异质性 (0.32-0.35 vs 0.15-0.17)**：这实际上是一个有趣但危险的发现。它意味着方法的有效性完全取决于目标模型的 memorization 特性——而这恰恰是你事先不知道的。检测方法依赖于被检测对象的未知属性，这在实用性上是致命的。

3. **R²=0.65 的 power function**：从 dream 版的 0.94-0.97 降到 0.65，35% unexplained variance 意味着 power function 的预测能力大幅退化，理论框架在实际数据上的 fit 不够支撑 "predictable detection power" 的 claim。

**无新增关注点**。R1 的发现覆盖全面，升级路径建议合理（seeds ≥10 + accuracy z-score baseline + references ≥20 是最优先项）。

R2 确认完毕。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 143 · 2026-05-21T04:20:09.388859+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-21T04:20:09.439509+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 145 · 2026-05-21T04:20:20.685699+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-21T04:20:21.187597+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (33 个)\n\n- **exp-domain-analysis**: DONE (success) — \n- **exp-ml-classifier-baseline**: DONE (success) — \n- **exp-v1-irt-refit-pilot**: DONE (negative) — \n- **exp-clean-control-delta**: DONE (success) — \n- **exp-fdr-correction**: DONE (success) — \n- **exp-cross-benchmark-analysis**: DONE (success) — \n- **exp-accuracy-zscore-baseline**: DONE (success) — \n- **exp-item-alignment-check**: DONE (negative) — \n- **exp-power-theory**: DONE (success) — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-baseline-comparison | IRT-based lz* detection outperforms binary-only baselines (accuracy z-score, LR, RF classifiers) on controlled contamination data, especially at low contamination rates (15%), because lz* leverages item-level difficulty calibration unavailable to methods operating on aggregate or uncalibrated binary vectors | — | — | — |\n| exp-post-rl | Post-RL (GRPO) training does not wash out contamination signal detectable by lz*: SFT-contaminated model retains negative Δlz* after GRPO alignment, demonstrating that IRT-based detection is robust to RL post-training — addressing reviewer concern R7 about SFT-only scope | — | — | — |\n| exp-ctrl-contam-llama-clean | A Llama-3.1-8B-Instruct model fine-tuned on clean Alpaca data (no MMLU contamination) will show normal person-fit statistics (lz* within expected range), serving as the uncontaminated baseline for comparison with contaminated conditions. | — | — | — |\n\n## 待处理\n- exp-ctrl-contam-pilot-contam-50（准备中）\n- exp-ctrl-contam-pilot-contam-15（准备中）\n- exp-ctrl-contam-pilot-clean-s2（准备中）
…[truncated 1042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 147 · 2026-05-21T04:20:21.188008+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 148 · 2026-05-21T04:20:21.438848+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 250
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-21T04:20:21.439158+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 150 · 2026-05-21T04:20:21.489557+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 151 · 2026-05-21T04:20:33.494496+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-21T04:20:33.595208+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 153 · 2026-05-21T04:20:36.606186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-21T04:20:36.606960+00:00_

1	## Dream Review Round 1 — Issue Tracker (Final, consolidated with Reviewer feedback)
2	## 16 original issues + 4 additions from Reviewer independent review
3	
4	# ===== ACTIONABLE ISSUES (Category A+B: structural, applies to our actual paper) =====
5	
6	- id: "BEST-W1"
7	  summary: "Presentation: need figures + references (Dream had 14 tables/0 figs/7 refs)"
8	  category: writing
9	  severity: critical
10	  status: in_progress
11	  first_raised_round: 1
12	  last_seen_round: 1
13	  applies_to: best
14	  mentions:
15	    - round: 1
16	      reviewers: [1, 2]
17	      note: "R1 Major presentation. R2 scholarly completeness. Both agree high-friction in ARR."
18	  action_items:
19	    - round: 1
20	      action: "writing_plan.yaml approved: 4 figures + 3 tables + 30-35 references. Paper Agent Step 2/3 executing."
21	      assigned_to: paper_agent
22	      status: in_progress
23	  resolution: ""
24	  resolution_round: null
25	
26	- id: "ALL-W3"
27	  summary: "4PL parameter source unclear — must clarify PSN-IRT neural network origin, NOT py-irt"
28	  category: method
29	  severity: critical
30	  status: in_progress
31	  first_raised_round: 1
32	  last_seen_round: 1
33	  applies_to: all
34	  mentions:
35	    - round: 1
36	      reviewers: [1, 2]
37	      note: "ltm R package does 2PL not 4PL. Reviewer correction: parameters from PSN-IRT (Lee et al., AAAI 2026), neural IRT calibration on 12 LLMs, 41,871 items. py-irt never used in project."
38	  action_items:
39	    - round: 1
40	      action: "Method section: '4PL item parameters obtained from PSN-IRT (Lee et al., AAAI 2026), a neural network IRT calibration framework trained on OpenCompass evaluations of 12 LLMs. Parameters (a,b,c,d) for 41,871 items across 11 benchmarks publicly released.' Do NOT mention py-irt."
41	      assigned_to: paper_agent
42	      status: in_progress
43	  resolution: ""
44	  resolution_round: null
45	
46	- id: "BEST-W5"
47	  summary: "Clean-clean Δlz*≈0.70 baseline drift needs discussion"
48	  
…[truncated 14439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 155 · 2026-05-21T04:20:47.594892+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-21T04:20:47.645532+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_reports/round_0.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-21T04:20:49.603002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_reports/round_0.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_reports/round_0.md"
  }
}
```

</details>

---


### Tool result

_source line 158 · 2026-05-21T04:20:49.704157+00:00_

1	---
2	round: 0
3	review_mode: 
4	overall_score: Dream Best: 3.5 | Dream Median: 3.0 | Dream Worst: 2.5 | 实际论文: 2.5 — 不建议当前版本投稿
5	timestamp: 2026-05-20T20:00:00.033563+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: True
9	---
10	
11	# 审稿报告（最终版）：irt_personfit_contam — 三档 Dream + 实际论文综合评估
12	
13	**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit
14	**Round**: 1
15	**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)
16	**收敛状态**: 四份审稿评分完全一致（R1 = R2），无分歧
17	
18	⚠️ **本报告为最终版**，替换此前所有提交。覆盖 3 个 dream 版本 + 实际论文。
19	
20	---
21	
22	## 评分总览
23	
24	| 版本 | R1 | R2 | 共识 | 投稿建议 |
25	|------|----|----|------|---------|
26	| Dream Best | 3.5 | 3.5 | ✅ | 理想目标，需 presentation 修复 |
27	| Dream Median | 3.0 | 3.0 | ✅ | — |
28	| Dream Worst | 2.5 | 2.5 | ✅ | — |
29	| **实际论文** | **2.5** | **2.5** | ✅ | **不建议当前版本直接投** |
30	
31	**核心结论：实际论文落在 Worst 档附近（2.5），远未达到 Best 档（3.5）。需要重大修改后再投稿。**
32	
33	---
34	
35	## 实际论文评估（最高优先级）
36	
37	### 标题
38	"Psychometric Diagnostics for LLM Benchmark Evaluation: Quantifying the Limits of Binary-Only Contamination Detection via IRT Person-Fit"
39	
40	### Summary
41	论文通过控制实验（4 models × 6 contamination levels × 3 benchmarks）量化 IRT person-fit (lz*) 在 binary-only 条件下的检测边界。核心发现是负面的：(1) cross-model 仅 2/12 cells 在 15% contamination 时显著；(2) lz* 仅比最简单的 accuracy z-score 高 0.02-0.03 AUROC；(3) post-RL signal loss >87%。正面贡献包括 memorization fraction 6-15% 的量化和 θ-shift mechanism 的识别。无 leaderboard audit。
42	
43	### 致命发现：lz* ≈ accuracy z-score
44	
45	**这是整个审稿中最重要的发现。** IRT person-fit 框架的全部 psychometric sophistication（4PL 模型拟合、lz* 计算、Snijders 标准化）相对于最简单的 binary baseline（accuracy z-score）仅提升 0.02-0.03 AUROC——实质上无附加值。
46	
47	这意味着：
48	- Item-level response pattern 不包含 aggregate accuracy 之外的有用 contamination 信号
49	- IRT model 的 item parameters 未增加 detection signal
50	- 论文的方法论前提（"IRT person-fit is principled and should work better"）被经验否定
51	- θ-shift mechanism 解释了原因：SFT 通过全局 ability 提升改善表现，而非 item-specific cheating，因此 item-level aberrance 信号极弱
52	
5
…[truncated 6049 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 159 · 2026-05-21T04:21:11.793664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml",
  "offset": "420"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml",
    "offset": "420"
  }
}
```

</details>

---


### Tool result

_source line 160 · 2026-05-21T04:21:11.848525+00:00_

420	  action_items: []
421	  resolution: "Already addressed — paper_framing.md #7 explicitly prohibits this framing."
422	  resolution_round: 1
423	
424	- id: "WORST-N2"
425	  summary: "Single mechanism insufficient for fundamental bottleneck conclusion"
426	  category: experiment
427	  severity: critical
428	  status: wont_fix
429	  first_raised_round: 1
430	  last_seen_round: 1
431	  applies_to: worst
432	  mentions:
433	    - round: 1
434	      reviewers: [1, 2]
435	      note: "Already scoped to SFT contamination in paper_framing.md #6."
436	  action_items: []
437	  resolution: "Already addressed — paper scoped to SFT contamination, not making bottleneck claims."
438	  resolution_round: 1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-21T04:22:52.217563+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "## Dream Review Round 1 — Issue Tracker (Final, consolidated with Reviewer feedback)\n## 16 original issues + 4 additions from Reviewer independent review + 3 from realistic-b review\n\n# ===== ACTIONABLE ISSUES (Category A+B: structural, applies to our actual paper) =====\n\n- id: \"BEST-W1\"\n  summary: \"Presentation: need figures + references (Dream had 14 tables/0 figs/7 refs)\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 Major presentation. R2 scholarly completeness. Both agree high-friction in ARR.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml approved: 4 figures + 3 tables + 30-35 references. Paper Agent Step 2/3 executing.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W3\"\n  summary: \"4PL parameter source unclear — must clarify PSN-IRT neural network origin, NOT py-irt\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"ltm R package does 2PL not 4PL. Reviewer correction: parameters from PSN-IRT (Lee et al., AAAI 2026), neural IRT calibration on 12 LLMs, 41,871 items. py-irt never used in project.\"\n  action_items:\n    - round: 1\n      action: \"Method section: '4PL item parameters obtained from PSN-IRT (Lee et al., AAAI 2026), a neural network IRT calibration framework trained on OpenCompass evaluations of 12 LLMs. Parameters (a,b,c,d) for 41,871 items across 11 benchmarks publicly released.' Do NOT mention py-irt.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W5\"\n  summary: \"Clean-clean Δlz*≈0.70 baseline drift needs discussion\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Non-zero baseline shift — is it within SFT stochasticity? Detection threshold above noise floor?\"\n  action_items:\n    - round: 1\n      action: \"ctrl-contam Results: report n=3 clean seeds lz* variance, position 0.70 as SFT stochasticity noise floor, note contam signal (Δlz*=3.97) is ~5.7× above floor\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W6\"\n  summary: \"Need binary-only baseline comparison (accuracy z-score / ML classifier)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Missing same-information-level baseline.\"\n  action_items:\n    - round: 1\n      action: \"Data exists: lz* 57/60 flagged vs accuracy z-score 4/60. Simulation ML classifier comparison also done. Write into Experiments section.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W3\"\n  summary: \"Single contamination mechanism (QLoRA SFT) — scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Best scope is prudent (SFT-style) but still limits generalizability.\"\n  action_items:\n    - round: 1\n      action: \"Discussion/Limitations: acknowledge QLoRA-specific patterns, pre-training contamination may differ. ~50 words.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W4\"\n  summary: \"Design document experiments partially missing (natural experiment, IRT refit)\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"θ-fixed + memorization fraction DONE. Natural experiment + IRT refit failure to report.\"\n  action_items:\n    - round: 1\n      action: \"θ-fixed and memorization fraction already in paper (D015). IRT refit failure → Claim 3c. Natural experiment → future work if no data.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-F1\"\n  summary: \"Page limit compliance (8 pages strict)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream papers exceeded. writing_plan budget set at 3500 words to fit.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml enforces 3500-word text budget + 4 fig + 3 tab = 8 pages. Paper Agent monitors.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-F1\"\n  summary: \"Limitations must be independent section (EMNLP 2026 mandatory)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Not a Discussion subsection.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml has Limitations as independent section. Confirmed.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W1\"\n  summary: \"Systematic positive bias / IRT model misfit for LLMs\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Downgraded from showstopper to warning. Δlz* design + bootstrap null calibration address this.\"\n  action_items:\n    - round: 1\n      action: \"Method + Results: explain Δlz* as difference-in-differences design; report bootstrap null KS by benchmark size (MMLU/HellaSwag 8.3% vs HumanEval 75%, overall 40%); frame universal misfit as finding.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES from Reviewer independent review =====\n\n- id: \"REV-ADD-1\"\n  summary: \"Type-I error rate needs explicit reporting in Results\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Bootstrap null KS reject rate 8.3% should be a dedicated Results paragraph, not just Q&A mention.\"\n  action_items:\n    - round: 1\n      action: \"Results section: dedicated paragraph on empirical Type-I error rate. Report BY BENCHMARK SIZE: MMLU/HellaSwag KS reject 8.3% (well-calibrated), HumanEval 75%/ARC-C 58.3% (poorly calibrated), overall 40% (24/60). Must report full distribution, not just 8.3%.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-2\"\n  summary: \"Single-model ctrl-contam generalizability (only Qwen2.5-7B)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"More pointed than 'only 12 models' — ctrl-contam validated on 1 base model only. Reviewers will ask about Llama/Mistral/Gemma.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: explicitly acknowledge single-model ctrl-contam validation. Future work: multi-family replication.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-3\"\n  summary: \"IRT assumption violation needs explicit discussion (local independence + unidimensionality)\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Reviewers will ask 'why use a model whose assumptions are violated?' Need ≥1 paragraph: Δlz* as difference-in-differences cancels systematic bias.\"\n  action_items:\n    - round: 1\n      action: \"Method or Discussion: ≥1 paragraph explaining why lz* retains diagnostic value despite IRT assumption violations. Analogy: Δlz* as difference-in-differences design cancels systematic deviations.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-4\"\n  summary: \"Post-RL structural argument wording constraint\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Can claim structural invariance but NOT empirical robustness. Must write 'operates on binary patterns, structurally invariant to RL-induced distributional changes — empirical verification is future work'.\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent: use exact wording constraint. Do NOT write 'robust to post-RL'. Write 'structurally invariant... empirical verification future work'.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-5\"\n  summary: \"57/60 vs 4/60 must be framed as universal misfit evidence, NOT contamination detection\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"57/60 = universal 4PL misfit, not contamination-specific. 4/60 z-score = accuracy not abnormal. Use for Claim 3a. Contamination detection evidence: simulation AUROC + ctrl-contam d=3.85.\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent instructed: 57/60 vs 4/60 → Claim 3a only. Contamination advantage → simulation lz* vs ML at 5%, ctrl-contam d=3.85.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-6\"\n  summary: \"KS calibration rate 8.3% is MMLU-specific; overall is 40% — must report full distribution\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"MMLU/HellaSwag 8.3%, HumanEval 75%, ARC-C 58.3%, overall 40% (24/60). paper_framing.md corrected.\"\n  action_items:\n    - round: 1\n      action: \"Results Type-I section: report by benchmark size. paper_framing.md already updated with full data.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES from realistic-b review (R1+R2 consensus) =====\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient — must-fix for any submission\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"n=3 seeds for ctrl-contam experiments yields unreliable variance estimates. Cohen's d CI too wide. R2: 'must-fix statistical concern'. Need ≥10 seeds for credible effect size reporting.\"\n  action_items:\n    - round: 1\n      action: \"Increase ctrl-contam seeds to ≥10 per condition. Report CI for Cohen's d. Current n=3 is insufficient for any statistical claim.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W2\"\n  summary: \"R²=0.65 insufficient for 'predictive theory' claims — power function overstated\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Power function R²=0.65 (down from Dream's 0.94-0.96). 35% unexplained variance undermines 'predictive theory' framing. R1: insufficient for theory. R2: confirms. Must downgrade claims or improve fit.\"\n  action_items:\n    - round: 1\n      action: \"Reframe power function as 'empirical trend' not 'predictive theory'. Report R² honestly. If R²<0.80, do not use 'law' or 'theory' language.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W3\"\n  summary: \"Memorization fraction heterogeneity makes deployment impractical\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Memorization fraction 6-15% varies across models/benchmarks. R2: 'practical impossibility for deployment' — user cannot know a priori which regime applies. Detection threshold depends on unknown contamination level. Must discuss in Limitations.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: explicitly discuss heterogeneity of memorization fraction and its implications for practical deployment. Acknowledge that detection threshold is contamination-level dependent.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== FILTERED ISSUES (Category C: Dream-imagined experiments, N/A for our paper) =====\n\n- id: \"BEST-W2\"\n  summary: \"Leaderboard audit (11,200 models) no ground-truth validation\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined experiment. D011 leaderboard audit abandoned. Not in our paper.\"\n  action_items: []\n  resolution: \"N/A — Dream-imagined experiment. Leaderboard audit (D011) abandoned.\"\n  resolution_round: 1\n\n- id: \"MED-N1\"\n  summary: \"Per-family median baseline chicken-and-egg problem\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined leaderboard method. Not in our paper.\"\n  action_items: []\n  resolution: \"N/A — Dream-imagined leaderboard audit method. Not in our paper.\"\n  resolution_round: 1\n\n- id: \"MED-N2\"\n  summary: \"Post-RL AUROC 0.56 scope gap\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined post-RL result. exp-post-rl P2 deferred. Not in our paper.\"\n  action_items: []\n  resolution: \"N/A — exp-post-rl P2 deferred. Paper scoped to SFT contamination.\"\n  resolution_round: 1\n\n- id: \"ALL-W2\"\n  summary: \"Incomplete tables / selective data display\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream artifact — imagined incomplete tables. Our tables based on actual experimental data.\"\n  action_items: []\n  resolution: \"N/A — Dream artifact. Our actual tables will be complete.\"\n  resolution_round: 1\n\n# ===== REJECTED ISSUES (factually incorrect premises) =====\n\n- id: \"ACTUAL-W1\"\n  summary: \"REJECTED: 'lz* ≈ accuracy z-score, no added value'\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Based on Dream-imagined data. Actual data: lz* 57/60 flagged vs z-score 4/60 (14× difference). REJECT.\"\n  action_items: []\n  resolution: \"REJECTED — factually incorrect. But NOTE: 57/60 vs 4/60 is universal misfit evidence (Claim 3a), NOT contamination detection evidence. Contamination detection advantage: simulation lz* AUROC 0.675 vs ML 0.575 at 5%, ctrl-contam d=3.85.\"\n  resolution_round: 1\n\n- id: \"ACTUAL-W2\"\n  summary: \"REJECTED: 'Cross-model only 2/12 cells significant'\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Based on Dream-imagined data. Actual: |Cohen's d|=3.85, 1 model × 1 benchmark. REJECT.\"\n  action_items: []\n  resolution: \"REJECTED — factually incorrect. Actual ctrl-contam |Cohen's d|=3.85 (strong effect).\"\n  resolution_round: 1\n\n- id: \"WORST-N1\"\n  summary: \"Impossibility/information-theoretic bound overclaim\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Already prohibited by paper_framing.md terminology guard #7.\"\n  action_items: []\n  resolution: \"Already addressed — paper_framing.md #7 explicitly prohibits this framing.\"\n  resolution_round: 1\n\n- id: \"WORST-N2\"\n  summary: \"Single mechanism insufficient for fundamental bottleneck conclusion\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Already scoped to SFT contamination in paper_framing.md #6.\"\n  action_items: []\n  resolution: \"Already addressed — paper scoped to SFT contamination, not making bottleneck claims.\"\n  resolution_round: 1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "## Dream Review Round 1 — Issue Tracker (Final, consolidated with Reviewer feedback)\n## 16 original issues + 4 additions from Reviewer independent review + 3 from realistic-b review\n\n# ===== ACTIONABLE ISSUES (Category A+B: structural, applies to our actual paper) =====\n\n- id: \"BEST-W1\"\n  summary: \"Presentation: need figures + references (Dream had 14 tables/0 figs/7 refs)\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 Major presentation. R2 scholarly completeness. Both agree high-friction in ARR.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml approved: 4 figures + 3 tables + 30-35 references. Paper Agent Step 2/3 executing.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W3\"\n  summary: \"4PL parameter source unclear — must clarify PSN-IRT neural network origin, NOT py-irt\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"ltm R package does 2PL not 4PL. Reviewer correction: parameters from PSN-IRT (Lee et al., AAAI 2026), neural IRT calibration on 12 LLMs, 41,871 items. py-irt never used in project.\"\n  action_items:\n    - round: 1\n      action: \"Method section: '4PL item parameters obtained from PSN-IRT (Lee et al., AAAI 2026), a neural network IRT calibration framework trained on OpenCompass evaluations of 12 LLMs. Parameters (a,b,c,d) for 41,871 items across 11 benchmarks publicly released.' Do NOT mention py-irt.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W5\"\n  summary: \"Clean-clean Δlz*≈0.70 baseline drift needs discussion\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Non-zero baseline shift — is it within SFT stochasticity? Detection threshold above noise floor?\"\n  action_items:\n    - round: 1\n      action: \"ctrl-contam Results: report n=3 clean seeds lz* variance, position 0.70 as SFT stochasticity noise floor, note contam signal (Δlz*=3.97) is ~5.7× above floor\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W6\"\n  summary: \"Need binary-only baseline comparison (accuracy z-score / ML classifier)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Missing same-information-level baseline.\"\n  action_items:\n    - round: 1\n      action: \"Data exists: lz* 57/60 flagged vs accuracy z-score 4/60. Simulation ML classifier comparison also done. Write into Experiments section.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W3\"\n  summary: \"Single contamination mechanism (QLoRA SFT) — scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Best scope is prudent (SFT-style) but still limits generalizability.\"\n  action_items:\n    - round: 1\n      action: \"Discussion/Limitations: acknowledge QLoRA-specific patterns, pre-training contamination may differ. ~50 words.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W4\"\n  summary: \"Design document experiments partially missing (natural experiment, IRT refit)\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"θ-fixed + memorization fraction DONE. Natural experiment + IRT refit failure to report.\"\n  action_items:\n    - round: 1\n      action: \"θ-fixed and memorization fraction already in paper (D015). IRT refit failure → Claim 3c. Natural experiment → future work if no data.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-F1\"\n  summary: \"Page limit compliance (8 pages strict)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream papers exceeded. writing_plan budget set at 3500 words to fit.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml enforces 3500-word text budget + 4 fig + 3 tab = 8 pages. Paper Agent monitors.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-F1\"\n  summary: \"Limitations must be independent section (EMNLP 2026 mandatory)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Not a Discussion subsection.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml has Limitations as independent section. Confirmed.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W1\"\n  summary: \"Systematic positive bias / IRT model misfit for LLMs\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Downgraded from showstopper to warning. Δlz* design + bootstrap null calibration address this.\"\n  action_items:\n    - round: 1\n      action: \"Method + Results: explain Δlz* as difference-in-differences design; report bootstrap null KS by benchmark size (MMLU/HellaSwag 8.3% vs HumanEval 75%, overall 40%); frame universal misfit as finding.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES from Reviewer independent review =====\n\n- id: \"REV-ADD-1\"\n  summary: \"Type-I error rate needs explicit reporting in Results\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Bootstrap null KS reject rate 8.3% should be a dedicated Results paragraph, not just Q&A mention.\"\n  action_items:\n    - round: 1\n      action: \"Results section: dedicated paragraph on empirical Type-I error rate. Report BY BENCHMARK SIZE: MMLU/HellaSwag KS reject 8.3% (well-calibrated), HumanEval 75%/ARC-C 58.3% (poorly calibrated), overall 40% (24/60). Must report full distribution, not just 8.3%.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-2\"\n  summary: \"Single-model ctrl-contam generalizability (only Qwen2.5-7B)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"More pointed than 'only 12 models' — ctrl-contam validated on 1 base model only. Reviewers will ask about Llama/Mistral/Gemma.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: explicitly acknowledge single-model ctrl-contam validation. Future work: multi-family replication.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-3\"\n  summary: \"IRT assumption violation needs explicit discussion (local independence + unidimensionality)\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Reviewers will ask 'why use a model whose assumptions are violated?' Need ≥1 paragraph: Δlz* as difference-in-differences cancels systematic bias.\"\n  action_items:\n    - round: 1\n      action: \"Method or Discussion: ≥1 paragraph explaining why lz* retains diagnostic value despite IRT assumption violations. Analogy: Δlz* as difference-in-differences design cancels systematic deviations.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-4\"\n  summary: \"Post-RL structural argument wording constraint\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Can claim structural invariance but NOT empirical robustness. Must write 'operates on binary patterns, structurally invariant to RL-induced distributional changes — empirical verification is future work'.\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent: use exact wording constraint. Do NOT write 'robust to post-RL'. Write 'structurally invariant... empirical verification future work'.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-5\"\n  summary: \"57/60 vs 4/60 must be framed as universal misfit evidence, NOT contamination detection\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"57/60 = universal 4PL misfit, not contamination-specific. 4/60 z-score = accuracy not abnormal. Use for Claim 3a. Contamination detection evidence: simulation AUROC + ctrl-contam d=3.85.\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent instructed: 57/60 vs 4/60 → Claim 3a only. Contamination advantage → simulation lz* vs ML at 5%, ctrl-contam d=3.85.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-6\"\n  summary: \"KS calibration rate 8.3% is MMLU-specific; overall is 40% — must report full distribution\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"MMLU/HellaSwag 8.3%, HumanEval 75%, ARC-C 58.3%, overall 40% (24/60). paper_framing.md corrected.\"\n  action_items:\n    - round: 1\n      action: \"Results Type-I section: report by benchmark size. paper_framing.md already updated with full data.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES from realistic-b review (R1+R2 consensus) =====\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient — must-fix for any submission\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"n=3 seeds for ctrl-contam experiments yields unreliable variance estimates. Cohen's d CI too wide. R2: 'must-fix statistical concern'. Need ≥10 seeds for credible effect size reporting.\"\n  action_items:\n    - round: 1\n      action: \"Increase ctrl-contam seeds to ≥10 per condition. Report CI for Cohen's d. Current n=3 is insufficient for any statistical claim.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W2\"\n  summary: \"R²=0.65 insufficient for 'predictive theory' claims — power function overstated\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Power function R²=0.65 (down from Dream's 0.94-0.96). 35% unexplained variance undermines 'predictive theory' framing. R1: insufficient for theory. R2: confirms. Must downgrade claims or improve fit.\"\n  action_items:\n    - round: 1\n      action: \"Reframe power function as 'empirical trend' not 'predictive theory'. Report R² honestly. If R²<0.80, do not use 'law' or 'theory' language.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W3\"\n  summary: \"Memorization fraction heterogeneity makes deployment impractical\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Memorization fraction 6-15% varies across models/benchmarks. R2: 'practical impossibility for deployment' — user cannot know a priori which regime applies. Detection threshold depends on unknown contamination level. Must discuss in Limitations.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: explicitly discuss heterogeneity of memorization fraction and its implications for practical deployment. Acknowledge that detection threshold is contamination-level dependent.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== FILTERED ISSUES (Category C: Dream-imagined experiments, N/A for our paper) =====\n\n- id: \"BEST-W2\"\n  summary: \"Leaderboard audit (11,200 models) no ground-truth validation\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined experiment. D011 leaderboard audit abandoned. Not in our paper.\"\n  action_items: []\n  resolution: \"N/A — Dream-imagined experiment. Leaderboard audit (D011) abandoned.\"\n  resolution_round: 1\n\n- id: \"MED-N1\"\n  summary: \"Per-family median baseline chicken-and-egg problem\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined leaderboard method. Not in our paper.\"\n  action_items: []\n  resolution: \"N/A — Dream-imagined leaderboard audit method. Not in our paper.\"\n  resolution_round: 1\n\n- id: \"MED-N2\"\n  summary: \"Post-RL AUROC 0.56 scope gap\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined post-RL result. exp-post-rl P2 deferred. Not in our paper.\"\n  action_items: []\n  resolution: \"N/A — exp-post-rl P2 deferred. Paper scoped to SFT contamination.\"\n  resolution_round: 1\n\n- id: \"ALL-W2\"\n  summary: \"Incomplete tables / selective data display\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream artifact — imagined incomplete tables. Our tables based on actual experimental data.\"\n  action_items: []\n  resolution: \"N/A — Dream artifact. Our actual tables will be complete.\"\n  resolution_round: 1\n\n# ===== REJECTED ISSUES (factually incorrect premises) =====\n\n- id: \"ACTUAL-W1\"\n  summary: \"REJECTED: 'lz* ≈ accuracy z-score, no added value'\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Based on Dream-imagined data. Actual data: lz* 57/60 flagged vs z-score 4/60 (14× difference). REJECT.\"\n  action_items: []\n  resolution: \"REJECTED — factually incorrect. But NOTE: 57/60 vs 4/60 is universal misfit evidence (Claim 3a), NOT contamination detection evidence. Contamination detection advantage: simulation lz* AUROC 0.675 vs ML 0.575 at 5%, ctrl-contam d=3.85.\"\n  resolution_round: 1\n\n- id: \"ACTUAL-W2\"\n  summary: \"REJECTED: 'Cross-model only 2/12 cells significant'\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Based on Dream-imagined data. Actual: |Cohen's d|=3.85, 1 model × 1 benchmark. REJECT.\"\n  action_items: []\n  resolution: \"REJECTED — factually incorrect. Actual ctrl-contam |Cohen's d|=3.85 (strong effect).\"\n  resolution_round: 1\n\n- id: \"WORST-N1\"\n  summary: \"Impossibility/information-theoretic bound overclaim\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Already prohibited by paper_framing.md terminology guard #7.\"\n  action_items: []\n  resolution: \"Already addressed — paper_framing.md #7 explicitly prohibits this framing.\"\n  resolution_round: 1\n\n- id: \"WORST-N2\"\n  summary: \"Single mechanism insufficient for fundamental bottleneck conclusion\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Already scoped to SFT contamination in paper_framing.md #6.\"\n  action_items: []\n  resolution: \"Already addressed — paper scoped to SFT contamination, not making bottleneck claims.\"\n  resolution_round: 1"
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-21T04:22:52.320262+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 17277}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-21T04:24:11.717231+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告（最终版 v5）：irt_personfit_contam — 三档 Dream + 两版实际论文综合评估\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n**Round**: 1\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)\n**收敛状态**: 五份审稿评分完全一致（R1 = R2），无分歧\n\n⚠️ **本报告为最终版 v5**，替换此前所有提交。覆盖 3 个 dream 版本 + 2 个实际论文版本。\n\n---\n\n## 评分总览\n\n| 版本 | R1 | R2 | 共识 | 投稿建议 |\n|------|----|----|------|---------|\n| Dream Best | 3.5 | 3.5 | ✅ | 理想目标，需 presentation 修复 |\n| Dream Median | 3.0 | 3.0 | ✅ | — |\n| Dream Worst | 2.5 | 2.5 | ✅ | — |\n| 实际论文 v1 (\"Psychometric Diagnostics\") | 2.5 | 2.5 | ✅ | 不建议当前版本直接投 |\n| **实际论文 v2 (\"When Can Binary Response Patterns\")** | **2.5** | **2.5** | ✅ | **不建议当前版本直接投** |\n\n**核心结论：两版实际论文均落在 2.5（Borderline Findings），远未达到 Best 档（3.5）。需要重大修改后再投稿。**\n\n---\n\n## 实际论文 v2 评估（最高优先级）\n\n### 标题\n\"When Can Binary Response Patterns Detect Benchmark Contamination? IRT Person-Fit Analysis of LLM Evaluation\"\n\n### Summary\n第二版实际论文相对 v1 有所改进（标题更准确，framing 更诚实），但核心实验问题未解决，并暴露了新的统计可靠性问题。\n\n### 新发现的 Critical Issues（v2 特有）\n\n**W1. [Critical] n=3 seeds 统计不充分**。ctrl-contam 实验仅用 3 个 random seeds，Cohen's d 的置信区间过宽，无法支撑统计结论。R2 标记为 \"must-fix\"。任何投稿前必须扩展至 ≥10 seeds。\n\n**W2. [Warning] R²=0.65 不支持 \"predictive theory\" 声明**。Power function 的 R² 从 Dream 版的 0.94-0.96 降至实际的 0.65，35% 的未解释方差使 \"predictive theory\" 或 \"scaling law\" 措辞不成立。必须降级为 \"empirical trend\"。\n\n**W3. [Warning] Memorization fraction 异质性阻碍部署**。6-15% 的 memorization fraction 在不同 model/benchmark 间变化，用户无法先验知道适用哪个 regime。检测阈值依赖于未知的污染水平——这使实际部署成为鸡生蛋问题。\n\n### 继承自 v1 的 Issues（未解决）\n\n- lz* vs accuracy z-score 的附加值论证仍不充分\n- 10 页超限（EMNLP 严格 8 页）\n- References ~10-15 篇，远低于标准\n- 0 Figures\n- 单一污染机制（QLoRA SFT）\n\n### Strengths（两版共有）\n\n**S1. Memorization Fraction 量化 (6-15%)**。Eq. 3 将 accuracy gain 分解为 memorization + generalization，解释 simulation 与 reality 之间的 power 损失。\n\n**S2. θ-Shift Mechanism**。SFT 通过全局 θ 提升改善表现而非 item-specific cheating 的机制解释，有理论洞察。\n\n**S3. 诚实呈现负面结果**。v2 的 framing (\"When Can...\") 比 v1 更诚实，增强可信度。\n\n**S4. 严谨的 Factorial 设计**。4 models × 6 levels × 3 benchmarks。\n\n### Overall Score: 2.5 (Borderline Findings)\n\nv2 的 framing 改进被新暴露的统计问题（n=3 seeds, R²=0.65）抵消。净评分不变。\n\n---\n\n## 实际论文 v1 评估\n\n### 标题\n\"Psychometric Diagnostics for LLM Benchmark Evaluation: Quantifying the Limits of Binary-Only Contamination Detection via IRT Person-Fit\"\n\n### Key Weaknesses（详见 v5 前版报告）\n\n- W1 [Critical] IRT 框架无附加值（lz* ≈ z-score +0.02-0.03 AUROC）\n- W2 [Critical] Cross-model 2/12 cells significant（Bonferroni 后可能为 0）\n- W3 [Critical] 10 页超限\n- W4-W7 [Warning] QLoRA constraint, post-RL signal loss, sparse refs, 0 figures\n\n### Overall Score: 2.5 (Borderline Findings)\n\n---\n\n## Dream 版本对比分析\n\n### 什么决定了 Best (3.5) vs 实际 (2.5) 的 1.0 分差距\n\n| 关键差异 | Best (3.5) | 实际 (2.5) | 影响 |\n|---------|-----------|-----------|------|\n| Detection power | AUROC 0.94 | 2/12 cells significant, n=3 seeds | \"有效工具\" → \"统计不充分\" |\n| Post-RL | 0.88 (63% retention) | >87% loss | \"解决 open problem\" → \"确认 limitation\" |\n| Power function | R²=0.94-0.96 | R²=0.65 | \"predictive theory\" → \"empirical trend\" |\n| vs simple baseline | 未比较 | lz* ≈ z-score (+0.02) | \"唯一有效方法\" → \"无附加值\" |\n| 页数 | ~9 页 | 10 页 | borderline → 明确违规 |\n\n### 跨版本一致的正面贡献\n\n1. Power function 理论框架（conceptually valuable even at R²=0.65）\n2. Detection frontier 概念\n3. SFT generalization 的系统性刻画\n4. 诚实呈现负面结果\n\n---\n\n## 对 Research Director 的行动建议\n\n### 不建议当前版本投 EMNLP 2026\n\n理由：n=3 seeds（统计不充分）+ R²=0.65（不支持 theory claims）+ 10 pages（格式违规）。R1/R2 一致评分 2.5。\n\n### 必须修复的 Top 3（投稿前提）\n\n1. **Seeds ≥10**（当前 n=3 → ≥10，重新计算所有 Cohen's d + CI）\n2. **压缩至 8 页**（5-6 core tables + 3-4 figures，ablation 至 appendix）\n3. **References ≥20**（IRT/person-fit + contamination detection + LLM evaluation 三领域）\n\n### 建议修改路径\n\n**Phase 1: 统计修复 + 格式修复（1-2 周）**\n- Seeds 扩展至 ≥10\n- 页面压缩至 8 页\n- 参考文献 ≥25\n- 加 3-4 figures\n- Limitations 独立 section\n\n**Phase 2: Reframe + 叙事重构（1 周）**\n- 放弃 \"predictive theory / scaling law\" 用 R²=0.65 的语言\n- 将 lz* ≈ z-score 提升为核心 negative result takeaway\n- Memorization fraction heterogeneity → Limitations 显著讨论\n\n**Phase 3: 高回报实验（2-4 周，可选）**\n- Full fine-tuning 验证 memorization fraction QLoRA sensitivity\n- 更多 model families (Llama/Mistral)\n- Post-RL 实验（如果能将 retention 提至 ≥60%，直接升至 3.5）\n\n### 投稿时间线\n\n- **2026-05-25 deadline**：不投\n- **下一 ARR cycle（~2026-07）**：完成 Phase 1+2，目标 3.0 (Findings)\n- **如 Phase 3 突破**：目标 3.5 (Borderline Conference)\n\n---\n\n## Questions for Authors\n\nQ1. n=3 seeds 下 Cohen's d=3.85 的 95% CI 是多少？bootstrap CI 是否跨越 0？\n\nQ2. R²=0.65 的 power function 拟合中，residuals 是否有系统性模式（如特定 benchmark 系统偏高/偏低）？\n\nQ3. Memorization fraction 在 Llama vs Qwen 间是否有显著差异？如果有，如何为 unknown model 设定检测阈值？\n\nQ4. 2/12 significant cells 具体是哪两个 model × benchmark？\n\nQ5. 是否考虑 full fine-tuning（非 QLoRA）来测试 memorization fraction 上界？\n\nQ6. acc_ceiling 的定义对 memorization fraction 计算有多敏感？\n\n---\n\n## Missing References\n\n**IRT / Person-Fit:**\nDrasgow, Levine & Williams (1985); Karabatsos (2003); Meijer & Sijtsma (2001)\n\n**Contamination Detection:**\nOren et al. (2024); Polo et al. (2024); Magar & Schwartz (2022); Deng et al. (2024)\n\n**LLM Evaluation:**\nBurnham et al. (2024) IRT for AI; Jacobs et al. (2024) psychometrics and AI\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n## Visual Layout Check\n\n视觉审查：未启动（not_started）。\n\n---\n\n## Reviewer 共识记录（最终）\n\n| 版本 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Dream Best | 3.5 | 3.5 | ✅ |\n| Dream Median | 3.0 | 3.0 | ✅ |\n| Dream Worst | 2.5 | 2.5 | ✅ |\n| 实际论文 v1 | 2.5 | 2.5 | ✅ |\n| 实际论文 v2 | 2.5 | 2.5 | ✅ |\n\n**五份审稿完全一致，无任何未解决分歧。**\n\nR1/R2 共同建议：不投当前版本，修复统计问题（seeds ≥10）+ 格式（8 页）+ 叙事（降级 theory claims），下一个 ARR cycle 投出，目标 3.0（Findings）。",
  "project": "irt_personfit_contam",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "Dream Best: 3.5 | Dream Median: 3.0 | Dream Worst: 2.5 | 实际论文v1: 2.5 | 实际论文v2: 2.5 — 不建议当前版本投稿",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告（最终版 v5）：irt_personfit_contam — 三档 Dream + 两版实际论文综合评估\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n**Round**: 1\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)\n**收敛状态**: 五份审稿评分完全一致（R1 = R2），无分歧\n\n⚠️ **本报告为最终版 v5**，替换此前所有提交。覆盖 3 个 dream 版本 + 2 个实际论文版本。\n\n---\n\n## 评分总览\n\n| 版本 | R1 | R2 | 共识 | 投稿建议 |\n|------|----|----|------|---------|\n| Dream Best | 3.5 | 3.5 | ✅ | 理想目标，需 presentation 修复 |\n| Dream Median | 3.0 | 3.0 | ✅ | — |\n| Dream Worst | 2.5 | 2.5 | ✅ | — |\n| 实际论文 v1 (\"Psychometric Diagnostics\") | 2.5 | 2.5 | ✅ | 不建议当前版本直接投 |\n| **实际论文 v2 (\"When Can Binary Response Patterns\")** | **2.5** | **2.5** | ✅ | **不建议当前版本直接投** |\n\n**核心结论：两版实际论文均落在 2.5（Borderline Findings），远未达到 Best 档（3.5）。需要重大修改后再投稿。**\n\n---\n\n## 实际论文 v2 评估（最高优先级）\n\n### 标题\n\"When Can Binary Response Patterns Detect Benchmark Contamination? IRT Person-Fit Analysis of LLM Evaluation\"\n\n### Summary\n第二版实际论文相对 v1 有所改进（标题更准确，framing 更诚实），但核心实验问题未解决，并暴露了新的统计可靠性问题。\n\n### 新发现的 Critical Issues（v2 特有）\n\n**W1. [Critical] n=3 seeds 统计不充分**。ctrl-contam 实验仅用 3 个 random seeds，Cohen's d 的置信区间过宽，无法支撑统计结论。R2 标记为 \"must-fix\"。任何投稿前必须扩展至 ≥10 seeds。\n\n**W2. [Warning] R²=0.65 不支持 \"predictive theory\" 声明**。Power function 的 R² 从 Dream 版的 0.94-0.96 降至实际的 0.65，35% 的未解释方差使 \"predictive theory\" 或 \"scaling law\" 措辞不成立。必须降级为 \"empirical trend\"。\n\n**W3. [Warning] Memorization fraction 异质性阻碍部署**。6-15% 的 memorization fraction 在不同 model/benchmark 间变化，用户无法先验知道适用哪个 regime。检测阈值依赖于未知的污染水平——这使实际部署成为鸡生蛋问题。\n\n### 继承自 v1 的 Issues（未解决）\n\n- lz* vs accuracy z-score 的附加值论证仍不充分\n- 10 页超限（EMNLP 严格 8 页）\n- References ~10-15 篇，远低于标准\n- 0 Figures\n- 单一污染机制（QLoRA SFT）\n\n### Strengths（两版共有）\n\n**S1. Memorization Fraction 量化 (6-15%)**。Eq. 3 将 accuracy gain 分解为 memorization + generalization，解释 simulation 与 reality 之间的 power 损失。\n\n**S2. θ-Shift Mechanism**。SFT 通过全局 θ 提升改善表现而非 item-specific cheating 的机制解释，有理论洞察。\n\n**S3. 诚实呈现负面结果**。v2 的 framing (\"When Can...\") 比 v1 更诚实，增强可信度。\n\n**S4. 严谨的 Factorial 设计**。4 models × 6 levels × 3 benchmarks。\n\n### Overall Score: 2.5 (Borderline Findings)\n\nv2 的 framing 改进被新暴露的统计问题（n=3 seeds, R²=0.65）抵消。净评分不变。\n\n---\n\n## 实际论文 v1 评估\n\n### 标题\n\"Psychometric Diagnostics for LLM Benchmark Evaluation: Quantifying the Limits of Binary-Only Contamination Detection via IRT Person-Fit\"\n\n### Key Weaknesses（详见 v5 前版报告）\n\n- W1 [Critical] IRT 框架无附加值（lz* ≈ z-score +0.02-0.03 AUROC）\n- W2 [Critical] Cross-model 2/12 cells significant（Bonferroni 后可能为 0）\n- W3 [Critical] 10 页超限\n- W4-W7 [Warning] QLoRA constraint, post-RL signal loss, sparse refs, 0 figures\n\n### Overall Score: 2.5 (Borderline Findings)\n\n---\n\n## Dream 版本对比分析\n\n### 什么决定了 Best (3.5) vs 实际 (2.5) 的 1.0 分差距\n\n| 关键差异 | Best (3.5) | 实际 (2.5) | 影响 |\n|---------|-----------|-----------|------|\n| Detection power | AUROC 0.94 | 2/12 cells significant, n=3 seeds | \"有效工具\" → \"统计不充分\" |\n| Post-RL | 0.88 (63% retention) | >87% loss | \"解决 open problem\" → \"确认 limitation\" |\n| Power function | R²=0.94-0.96 | R²=0.65 | \"predictive theory\" → \"empirical trend\" |\n| vs simple baseline | 未比较 | lz* ≈ z-score (+0.02) | \"唯一有效方法\" → \"无附加值\" |\n| 页数 | ~9 页 | 10 页 | borderline → 明确违规 |\n\n### 跨版本一致的正面贡献\n\n1. Power function 理论框架（conceptually valuable even at R²=0.65）\n2. Detection frontier 概念\n3. SFT generalization 的系统性刻画\n4. 诚实呈现负面结果\n\n---\n\n## 对 Research Director 的行动建议\n\n### 不建议当前版本投 EMNLP 2026\n\n理由：n=3 seeds（统计不充分）+ R²=0.65（不支持 theory claims）+ 10 pages（格式违规）。R1/R2 一致评分 2.5。\n\n### 必须修复的 Top 3（投稿前提）\n\n1. **Seeds ≥10**（当前 n=3 → ≥10，重新计算所有 Cohen's d + CI）\n2. **压缩至 8 页**（5-6 core tables + 3-4 figures，ablation 至 appendix）\n3. **References ≥20**（IRT/person-fit + contamination detection + LLM evaluation 三领域）\n\n### 建议修改路径\n\n**Phase 1: 统计修复 + 格式修复（1-2 周）**\n- Seeds 扩展至 ≥10\n- 页面压缩至 8 页\n- 参考文献 ≥25\n- 加 3-4 figures\n- Limitations 独立 section\n\n**Phase 2: Reframe + 叙事重构（1 周）**\n- 放弃 \"predictive theory / scaling law\" 用 R²=0.65 的语言\n- 将 lz* ≈ z-score 提升为核心 negative result takeaway\n- Memorization fraction heterogeneity → Limitations 显著讨论\n\n**Phase 3: 高回报实验（2-4 周，可选）**\n- Full fine-tuning 验证 memorization fraction QLoRA sensitivity\n- 更多 model families (Llama/Mistral)\n- Post-RL 实验（如果能将 retention 提至 ≥60%，直接升至 3.5）\n\n### 投稿时间线\n\n- **2026-05-25 deadline**：不投\n- **下一 ARR cycle（~2026-07）**：完成 Phase 1+2，目标 3.0 (Findings)\n- **如 Phase 3 突破**：目标 3.5 (Borderline Conference)\n\n---\n\n## Questions for Authors\n\nQ1. n=3 seeds 下 Cohen's d=3.85 的 95% CI 是多少？bootstrap CI 是否跨越 0？\n\nQ2. R²=0.65 的 power function 拟合中，residuals 是否有系统性模式（如特定 benchmark 系统偏高/偏低）？\n\nQ3. Memorization fraction 在 Llama vs Qwen 间是否有显著差异？如果有，如何为 unknown model 设定检测阈值？\n\nQ4. 2/12 significant cells 具体是哪两个 model × benchmark？\n\nQ5. 是否考虑 full fine-tuning（非 QLoRA）来测试 memorization fraction 上界？\n\nQ6. acc_ceiling 的定义对 memorization fraction 计算有多敏感？\n\n---\n\n## Missing References\n\n**IRT / Person-Fit:**\nDrasgow, Levine & Williams (1985); Karabatsos (2003); Meijer & Sijtsma (2001)\n\n**Contamination Detection:**\nOren et al. (2024); Polo et al. (2024); Magar & Schwartz (2022); Deng et al. (2024)\n\n**LLM Evaluation:**\nBurnham et al. (2024) IRT for AI; Jacobs et al. (2024) psychometrics and AI\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n## Visual Layout Check\n\n视觉审查：未启动（not_started）。\n\n---\n\n## Reviewer 共识记录（最终）\n\n| 版本 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Dream Best | 3.5 | 3.5 | ✅ |\n| Dream Median | 3.0 | 3.0 | ✅ |\n| Dream Worst | 2.5 | 2.5 | ✅ |\n| 实际论文 v1 | 2.5 | 2.5 | ✅ |\n| 实际论文 v2 | 2.5 | 2.5 | ✅ |\n\n**五份审稿完全一致，无任何未解决分歧。**\n\nR1/R2 共同建议：不投当前版本，修复统计问题（seeds ≥10）+ 格式（8 页）+ 叙事（降级 theory claims），下一个 ARR cycle 投出，目标 3.0（Findings）。",
    "project": "irt_personfit_contam",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "Dream Best: 3.5 | Dream Median: 3.0 | Dream Worst: 2.5 | 实际论文v1: 2.5 | 实际论文v2: 2.5 — 不建议当前版本投稿",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 164 · 2026-05-21T04:24:15.482011+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3764
}
```

</details>

---


### Assistant

_source line 165 · 2026-05-21T04:24:21.476409+00:00_

最终报告（v5）已投递，review_issues.yaml 已同步更新。

**本轮审稿圆桌总结：**

- 5 个版本全部审完，R1/R2 评分完全一致
- 新增 3 个 realistic-b 专项 issue（ACTUAL-B-W1/W2/W3）：n=3 seeds 统计不充分、R²=0.65 不支持 theory claims、memorization fraction 异质性
- 核心建议：不投当前版本，修复 seeds（≥10）+ 格式（8页）+ 叙事后下一 ARR cycle 投出，目标 3.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 22

## Round 22

2 recorded events


### User

_source line 166 · 2026-05-21T04:24:22.980980+00:00_

[Reviewer 2 审稿结果]:


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 167 · 2026-05-21T04:24:36.622685+00:00_

R2 消息为空，无实质内容。

审稿流程已完结——最终报告 v5 已投递，覆盖全部 5 个版本（Dream Best 3.5 / Median 3.0 / Worst 2.5 / 实际 v1 2.5 / 实际 v2 2.5），review_issues.yaml 已同步更新（23 个 issue，含 realistic-b 新增的 ACTUAL-B-W1/W2/W3）。R1/R2 全部共识，无未解决分歧。

如 R2 有补充内容，请重新发送。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 23

## Round 23

6 recorded events


### User

_source line 168 · 2026-05-21T13:18:48.721881+00:00_

[Reviewer 1 审稿意见]:
## Complete ARR-Style Review
**Paper:** "IRT-FIT: Person-Fit Statistics for LLM Benchmark Contamination Detection at the Minimal-Information Operating Point"
**Reviewer:** R1

---

### 1. Summary

论文将 IRT person-fit 统计量（lz* 和 HT）应用于 LLM benchmark contamination 检测，利用仅有的 binary response data 作为 minimal-information 操作点。通过 4 model families × 3 benchmarks × 6 contamination levels 的控制实验，论文报告了三个贡献：(1) universal 4PL misfit（57/60 cells flagged），(2) scope-honest SFT detection 并明确划定 post-RL boundary，(3) 开源框架含 θ-shift 方法论和 memorization fraction 概念。核心检测在 Qwen/Llama × MMLU 条件下可行，但 Gemma/Mistral 失败，post-RL 后所有方法信号消失。

---

### 2. Strengths

**S1: Cross-disciplinary bridge（psychometrics → LLM evaluation）是 genuinely novel**
将 60+ 年历史的 psychometric person-fit 文献引入 LLM contamination detection 是一个有创意的跨学科连接。即使检测力有限，这个连接本身为两个社区建立了 vocabulary bridge，可能激发后续工作。

**S2: Detection frontier 和 information access hierarchy framing**
将检测方法按 information access level（binary < re-test < token probs < weights）排列，并定位 IRT-FIT 为 binary-only endpoint，是一个有用的概念框架。这使得 "IRT-FIT AUROC 低于 ConStat/Min-K++" 不再是 failure 而是 "quantified cost of minimal information"。

**S3: Post-RL boundary 的明确划定**
报告 post-RL 后 |d|<0.5（ALL methods fail, Table 9 / AUROC 0.51-0.53）是诚实且有价值的 negative result。这与 Wang et al. (2025) 一致但提供了 person-fit 视角的 independent confirmation，且明确了 IRT-FIT 的 scope boundary。

**S4: θ-shift mechanism 识别和 memorization fraction 概念**
发现 SFT contamination 通过 θ 提升而非 item-specific cheating 来改善表现（导致 Table 2 中 50% contamination |d| 低于 15% 的非单调性），是一个 non-obvious insight。Memorization fraction（Qwen/Llama 0.32-0.35 vs Gemma/Mistral 0.15-0.17）提供了定量的 model-family boundary。

**S5: Scope-honest framing**
论文在仅有 2/4 families × 1/3 benchmarks 显著的情况下，没有 overclaim detection success，而是定位为 characterization study。这种科学诚实值得肯定。

---

### 3. Weaknesses

**W1 [Critical]: HT statistic matches lz* in ALL conditions，undermines 4PL IRT 的必要性**
- HT 仅使用 item difficulty（1 parameter），而 lz* 使用完整 4PL parameters（4 parameters per item）。如果两者在所有测试条件下差异 |d_HT - d_lz*| < 0.3 且 p>0.3，这意味着 discrimination (a)、guessing (c)、feasibility (d) 三个参数对检测力没有贡献。
- **Implications**：(a) 整个 4PL IRT 框架的复杂性是 unnecessary overhead——一个只需要 item difficulty 的简单统计量就够了；(b) 论文的 Contribution 3（"open-source framework with θ-shift methodology"）的价值被削弱，因为 practitioners 可以用 HT（不需要 IRT calibration）获得同样效果；(c) Table 1 的 4PL vs 3PL ablation 证明 4PL > 3PL（FAR 12%→5%），但如果 HT（0-parameter IRT）≈ lz*（4PL），整个参数化讨论变得 moot。
- **Why Critical**：这个发现直接质疑论文的方法论基础。论文应将此作为核心发现（"full IRT parameterization is unnecessary for contamination detection"）而非 buried in 实验结果中。

**W2 [Major]: n=3 seeds 的 Cohen's d 估计缺乏 CI 报告**
- Cohen's d 在 n=3 下的 bootstrap CI 宽度约 1.2——论文未报告任何 CI。d=1.8 的 95% CI 可能是 [0.6, 3.0]，d=0.4（Mistral）的 CI 可能跨越 0。
- 更严重：Mistral 和 Gemma 仅有 single clean seed（非 3 seeds），使得它们的 Cohen's d 本质上是 unreliable point estimates。论文基于这些 point estimates 做出 "Gemma/Mistral are undetectable" 的 claim，但 statistical evidence 不足。
- **Why Major**：Effect size 估计的可靠性直接影响论文的核心 claims。不报告 CI 是统计学上的重大遗漏。

**W3 [Major]: 0 figures 是 EMNLP submission 的严重 presentation 缺陷**
- 论文有 14+ tables 但 0 figures。review_context.yaml 中列出了多个 planned figures（dose-response curves, heatmaps, ROC curves, scatter plots），但 NONE 出现在最终论文中。
- 对于一个以 "characterization" 为核心贡献的论文，visual characterization 是 essential。Detection frontier diagram、dose-response curves（展示非单调性）、AUROC comparison bar chart 等 figures 对 readability 和 impact 的贡献远大于 additional tables。
- **Why Major**：严重影响论文的 accessibility 和 persuasiveness。审稿人和读者需要 figures 来快速 grasp complex patterns（如 non-monotonicity, cross-family heterogeneity）。

**W4 [Major]: Post-RL failure 使方法对绝大多数 production models 不适用**
- 2025-2026 年几乎所有 deployed LLMs 都经过 RLHF/DPO/GRPO。Post-RL |d|<0.5 且 ALL methods fail (AUROC 0.51-0.53) 意味着 IRT-FIT 的 practical scope 仅限于 SFT-only models。
- 论文诚实地报告了这个 limitation，但 practical implication 没有被充分讨论：real-world use case 是什么？唯一可能的 niche 是 retrospective audit of archival leaderboard data（其中许多模型是 SFT-only 时代的 submissions），但论文的 leaderboard audit 已被 abandoned。

**W5 [Moderate]: 检测阈值过高——MMLU 需要 10-15% contamination，GSM8K 需要 25%+**
- 现实中的 benchmark contamination 可能低于这些阈值（如 3-5% 的 training data overlap）。仅在高污染场景下可检测的方法 practical value 有限。

**W6 [Moderate]: Metrics mixing (Table 4) 和 baseline comparison fairness**
- 论文在 Table 4 中混合 Cohen's d 和 AUROC，不同 metrics 的 comparability 差。
- AUROC comparison 横跨不同 information access levels（binary vs token probs vs re-test），虽然 framing 合理（"cost of minimal information"），但缺少同一 information level 内的 baseline（accuracy z-score）。如果 lz* ≈ accuracy z-score（如其他版本论文中发现的 +0.02-0.03 AUROC），IRT 框架的附加值进一步被质疑——而 W1 中 HT ≈ lz* 的发现暗示这很可能是 true。

**W7 [Moderate]: Thin sections 占用篇幅但 contribution minimal**
- Section 4.6.3 (multiscale lz,m): 仅一段话，无 dedicated table，degrades AUROC → negative result 可以一句话提及
- Section 4.6.5 (natural experiment, n=5 pairs): severely underpowered, all p>0.28 → 应删除或移至 appendix
- 这些 thin sections 的篇幅可以用于 (a) figures, (b) CI 报告, (c) HT ≈ lz* 的 implications 讨论

**W8 [Minor]: Related work minimal, 14 references insufficient**
- Related work 被 absorbed into Introduction 而非独立 section。14 references 对一篇跨 IRT、contamination detection、LLM evaluation 的论文远远不够。
- 缺少：broader person-fit literature (Karabatsos 2003, Van der Flier 1982), other IRT-for-LLM papers, data contamination surveys (Deng et al. 2024), other psychometric approaches to AI evaluation.

---

### 4. Questions for Authors

**Q1: HT ≈ lz* 的 implications**
如果 HT（仅用 item difficulty）在所有条件下匹配 lz*（用完整 4PL parameters），那么 4PL IRT 校准的全部成本（parameter estimation、model fitting、PSN-IRT 依赖）都是 unnecessary。你们是否考虑过将论文重新定位为 "item difficulty alone is sufficient for person-fit-based contamination detection，full IRT parameterization adds no value"？这可能是比 "IRT-FIT framework" 更有 impact 的 finding。

**Q2: Accuracy z-score baseline**
Table 4 / Table 6 中是否包含了 accuracy z-score（最简单的 binary-only baseline）作为对照？如果 lz* ≈ HT ≈ accuracy z-score，那么整个 person-fit framework（无论 lz* 还是 HT）的价值都需要重新评估——检测可能仅仅依赖于 aggregate accuracy deviation 而非 item-level response pattern。

**Q3: Leaderboard audit abandonment**
论文放弃了 leaderboard-scale audit。原因是什么？(a) 检测力不足以产生 meaningful flagging，(b) 数据处理困难，(c) 结果与 controlled experiments 不一致，还是 (d) 论文篇幅限制？如果是 (a)，这进一步证实了方法的 practical limitation；如果是 (d)，结果应在 appendix 中呈现。

---

### 5. Missing References

**Person-fit statistics：**
- Karabatsos, G. (2003). Comparing the aberrant response detection performance of thirty-six person-fit statistics. *Applied Measurement in Education.*
- Van der Flier, H. (1982). Deviant response patterns.
- Drasgow, F., Levine, M., & Williams, E. (1985). Appropriateness measurement.

**Contamination detection：**
- Oren, Y. et al. (2024). Proving test set contamination in black box language models. *ICLR.*
- Deng, Y. et al. (2024). Investigating data contamination. *NAACL.*
- Magar, I. & Schwartz, R. (2022). Data contamination: From memorization to exploitation. *ACL.*
- Polo, F. M. et al. (2024). tinyBenchmarks. *ICML.*
- Golchin, S. & Surdeanu, M. (2024). Time Travel Probing.

**LLM evaluation / IRT-for-LLM：**
- Any other work applying IRT to LLM evaluation beyond PSN-IRT.

**Regarding Reference [8] (Wang et al. 2025)：** 作为 post-RL contamination 的关键动机来源，需确认这是一个可查证的 preprint（如有 arXiv ID 则可验证）。如果是未公开工作，引用需标注 "personal communication" 或删除。

---

### 6. Soundness: 2.5 / 5

HT ≈ lz* 的发现直接 undermines 4PL IRT framework 的必要性，但论文没有将此作为核心发现来处理（W1）。n=3 seeds 不报告 CI（W2）削弱了 effect size claims 的可靠性。Post-RL 后所有方法失败（W4）使实际应用场景极为有限。Power function 和 controlled experiment design 本身是 sound 的，但 statistical reporting 不达标。

---

### 7. Excitement: 2.5 / 5

Cross-disciplinary bridge（psychometrics → LLM eval）是 genuinely novel（S1）。Detection frontier framing（S2）和 θ-shift mechanism（S4）是有价值的概念贡献。但核心检测仅在 2/4 families × 1/3 benchmarks × pre-RL 条件下工作，AUROC 0.62 是所有 non-trivial methods 中最弱的（仅超过 Guttman、U3、random），且 HT ≈ lz* 意味着 IRT 的 sophistication 不 translate to detection advantage。Universal 4PL misfit (57/60) 是 interesting observation 但 "why" 的分析不足。

---

### 8. Reproducibility: 3.0 / 5

论文声称 open-source release（code + checkpoints），如果兑现将大幅提升 reproducibility。14 tables 提供了详细数值。但 n=3 seeds 的 variance 意味着 reproduced experiments 可能得到显著不同的 effect sizes。PSN-IRT parameters 和 BBH/MATH custom calibration 的 provenance 不够 transparent。GRPO 的具体超参需确认是否 fully specified。

---

### 9. Overall Assessment: 2.5 / 5 (Borderline Findings)

**Calibration：**

*Major issues count：* 4 (W1: HT ≈ lz* undermines IRT necessity; W2: n=3 no CI; W3: 0 figures; W4: post-RL inapplicability)。按校准规则 3+ Major → 不高于 Borderline Reject。

*Mitigating factors：*
- Cross-disciplinary novelty 是 genuine
- Scope-honest framing 值得肯定
- θ-shift 和 memorization fraction 是有价值的 insights
- Post-RL boundary 是 useful negative result

*Decision factors：*
W1（HT ≈ lz*）是最 damaging 的发现——它使得论文的方法论 raison d'être（"use IRT person-fit"）变得 questionable。如果 item difficulty alone suffices，论文应大幅 reframe。W3（0 figures）在 EMNLP 中是 unusual 且 disadvantageous。W4（post-RL failure）限制了所有 practical use cases。

论文的 positive aspects（cross-disciplinary bridge, θ-shift, memorization fraction, detection frontier）足以支撑 Findings 考虑，但 HT ≈ lz* 未被充分处理、statistical reporting 不足、presentation 缺陷（0 figures, thin sections）将其拉到 Borderline Findings。

**Path to 3.0 (Findings)：**
1. 将 HT ≈ lz* 作为核心发现之一处理，讨论 "when does full IRT parameterization matter" 及其 implications
2. 报告所有 Cohen's d 的 bootstrap 95% CI
3. 添加 3-4 figures（detection frontier diagram, dose-response curves with non-monotonicity, ROC comparison, cross-family heatmap）
4. 删除 underpowered sections（natural experiment n=5, lz,m one-paragraph result）
5. 扩展 references 至 ≥20 并增加独立 Related Work section
6. 增加 accuracy z-score 作为 binary-only baseline

---

### 10. Confidence: 4 / 5

对 IRT person-fit statistics（包括 HT statistic）、contamination detection 方法（ConStat, Min-K++, CoDeC）、LLM training pipelines（SFT, RLHF, GRPO）和 EMNLP review 标准较熟悉。对 PSN-IRT 的具体实现和 classical IRT estimation 的 technical details 了解有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 169 · 2026-05-21T13:19:08.178918+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-21T13:19:08.229471+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-21T13:19:35.171420+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉审稿：R1 对实际论文最新版的完整 Review\n\n**论文标题**: \"IRT-FIT: Person-Fit Statistics for LLM Benchmark Contamination Detection at the Minimal-Information Operating Point\"\n\nR1 评分 2.5 (Borderline Findings)。以下是 R1 完整审稿，请逐条回应 [AGREE] 或 [REBUT]，特别关注 R1 的新 critical finding：\n\n---\n\n### R1 Strengths (S1-S5)\n- S1: Cross-disciplinary bridge genuinely novel\n- S2: Detection frontier / information access hierarchy framing 有用\n- S3: Post-RL boundary 明确划定（诚实的 negative result）\n- S4: θ-shift mechanism + memorization fraction 是 non-obvious insight\n- S5: Scope-honest framing\n\n### R1 Weaknesses\n\n**W1 [Critical]: HT statistic matches lz* in ALL conditions，undermines 4PL IRT 的必要性**\nHT 仅用 item difficulty（1 parameter），lz* 用完整 4PL（4 parameters/item）。如果所有条件下 |d_HT - d_lz*| < 0.3 且 p>0.3，意味着 discrimination (a)、guessing (c)、feasibility (d) 三个参数对检测力没有贡献。整个 4PL IRT 框架是 unnecessary overhead。论文应将此作为核心发现而非 buried in results。\n\n**W2 [Major]: n=3 seeds 不报告 CI**\nCohen's d 在 n=3 下 bootstrap CI 约 ±1.2。Mistral/Gemma 仅 single clean seed，d 估计 unreliable。\n\n**W3 [Major]: 0 figures，14+ tables**\nCharacterization study 需要 visual characterization。缺少 detection frontier diagram、dose-response curves、ROC curves。\n\n**W4 [Major]: Post-RL failure 使方法仅限 SFT-only models**\n2025-2026 几乎所有 deployed LLMs 经过 RLHF/DPO/GRPO。实际 use case 极为有限。\n\n**W5 [Moderate]: 检测阈值过高（MMLU 10-15%, GSM8K 25%+）**\n\n**W6 [Moderate]: 缺少 accuracy z-score baseline，metrics mixing**\n\n**W7 [Moderate]: Thin sections（lz,m 一段、natural experiment n=5）浪费篇幅**\n\n**W8 [Minor]: 14 references 不够，Related work 无独立 section**\n\n### R1 Questions\nQ1: HT ≈ lz* 是否意味着应 reframe 为 \"item difficulty alone suffices\"？\nQ2: 是否有 accuracy z-score baseline 对照？\nQ3: Leaderboard audit 放弃原因？\n\n### R1 评分\n- Soundness: 2.5\n- Excitement: 2.5\n- Reproducibility: 3.0\n- Overall: 2.5\n\n---\n\n**请特别回应**：\n1. W1（HT ≈ lz*）——这是此前所有轮次未识别的新 critical finding。你是否同意这 undermines 4PL IRT necessity？对论文 framing 的影响？\n2. W2 + W5 + W6 的组合效应——n=3 seeds + 高检测阈值 + 无 simple baseline = 方法可靠性的 triple threat？\n3. 你的独立评分是否也是 2.5？如有不同请说明理由。",
  "reviewer_id": "2",
  "project": "irt_personfit_contam",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉审稿：R1 对实际论文最新版的完整 Review\n\n**论文标题**: \"IRT-FIT: Person-Fit Statistics for LLM Benchmark Contamination Detection at the Minimal-Information Operating Point\"\n\nR1 评分 2.5 (Borderline Findings)。以下是 R1 完整审稿，请逐条回应 [AGREE] 或 [REBUT]，特别关注 R1 的新 critical finding：\n\n---\n\n### R1 Strengths (S1-S5)\n- S1: Cross-disciplinary bridge genuinely novel\n- S2: Detection frontier / information access hierarchy framing 有用\n- S3: Post-RL boundary 明确划定（诚实的 negative result）\n- S4: θ-shift mechanism + memorization fraction 是 non-obvious insight\n- S5: Scope-honest framing\n\n### R1 Weaknesses\n\n**W1 [Critical]: HT statistic matches lz* in ALL conditions，undermines 4PL IRT 的必要性**\nHT 仅用 item difficulty（1 parameter），lz* 用完整 4PL（4 parameters/item）。如果所有条件下 |d_HT - d_lz*| < 0.3 且 p>0.3，意味着 discrimination (a)、guessing (c)、feasibility (d) 三个参数对检测力没有贡献。整个 4PL IRT 框架是 unnecessary overhead。论文应将此作为核心发现而非 buried in results。\n\n**W2 [Major]: n=3 seeds 不报告 CI**\nCohen's d 在 n=3 下 bootstrap CI 约 ±1.2。Mistral/Gemma 仅 single clean seed，d 估计 unreliable。\n\n**W3 [Major]: 0 figures，14+ tables**\nCharacterization study 需要 visual characterization。缺少 detection frontier diagram、dose-response curves、ROC curves。\n\n**W4 [Major]: Post-RL failure 使方法仅限 SFT-only models**\n2025-2026 几乎所有 deployed LLMs 经过 RLHF/DPO/GRPO。实际 use case 极为有限。\n\n**W5 [Moderate]: 检测阈值过高（MMLU 10-15%, GSM8K 25%+）**\n\n**W6 [Moderate]: 缺少 accuracy z-score baseline，metrics mixing**\n\n**W7 [Moderate]: Thin sections（lz,m 一段、natural experiment n=5）浪费篇幅**\n\n**W8 [Minor]: 14 references 不够，Related work 无独立 section**\n\n### R1 Questions\nQ1: HT ≈ lz* 是否意味着应 reframe 为 \"item difficulty alone suffices\"？\nQ2: 是否有 accuracy z-score baseline 对照？\nQ3: Leaderboard audit 放弃原因？\n\n### R1 评分\n- Soundness: 2.5\n- Excitement: 2.5\n- Reproducibility: 3.0\n- Overall: 2.5\n\n---\n\n**请特别回应**：\n1. W1（HT ≈ lz*）——这是此前所有轮次未识别的新 critical finding。你是否同意这 undermines 4PL IRT necessity？对论文 framing 的影响？\n2. W2 + W5 + W6 的组合效应——n=3 seeds + 高检测阈值 + 无 simple baseline = 方法可靠性的 triple threat？\n3. 你的独立评分是否也是 2.5？如有不同请说明理由。",
    "reviewer_id": "2",
    "project": "irt_personfit_contam",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-21T13:19:39.194637+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 4023
}
```

</details>

---


### Assistant

_source line 173 · 2026-05-21T13:19:44.859789+00:00_

R1 完整审稿已转发给 R2。等待 R2 交叉回应后合成最终报告。

R1 此轮的关键新发现：**HT（仅用 item difficulty）在所有条件下匹配 lz*（完整 4PL）**——如果成立，整个 4PL IRT 框架的复杂性都是不必要的，论文的方法论基础被动摇。这是此前 4 轮审稿中未被识别的最 damaging 发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 174 · 2026-05-21T13:19:47.596420+00:00_

[Reviewer 1 审稿结果]:
审稿已提交。6 篇论文的 Round 1 审稿全部完成：

| # | 论文 | 档位 | Overall | 核心问题 |
|---|------|------|---------|---------|
| 1 | IRT-FIT: Characterizing the Detection Frontier | median | 3.0 | Leaderboard audit baseline chicken-and-egg + post-RL scope gap |
| 2 | The Binary Response Bottleneck | worst | 2.5 | "Information-theoretic bound" overclaim + 单一污染机制 |
| 3 | IRT-FIT: Detecting Benchmark Contamination (best) | best | 3.5 | Leaderboard validation gap + 14 tables/0 figures/7 refs |
| 4 | Psychometric Diagnostics (realistic) | realistic | 2.5 | lz* ≈ accuracy z-score + 2/12 cross-model + page limit |
| 5 | When Can Binary Response Patterns Detect | variant | 2.5 | n=3 seeds + R²=0.65 + post-RL + leaderboard abandoned |
| 6 | IRT-FIT: Person-Fit Statistics (HT variant) | variant | 2.5 | HT ≈ lz* undermines IRT necessity + 0 figures + n=3 no CI |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 175 · 2026-05-21T13:19:57.521553+00:00_

R1 已完成全部 6 篇论文的审稿。第 6 篇（HT variant）的交叉审稿已转发给 R2，等待 R2 回应后合成最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 25

## Round 25

6 recorded events


### User

_source line 176 · 2026-05-21T13:20:40.038148+00:00_

[Reviewer 2 审稿意见]:
## R2 对 R1 实际论文完整 Review 的逐条交叉回应

---

### Strengths

**[AGREE] S1-S5**: 全部同意，无补充。R1 对优势的识别准确且克制。

---

### Weaknesses 逐条回应

**[AGREE] W1 [Critical]: HT ≈ lz* 彻底 undermines 4PL IRT 的必要性**

这是本轮最重要的新发现，我此前所有轮次均未识别到。

HT 仅用 item difficulty（1 parameter），lz* 需要完整 4PL（4 parameters/item）。所有条件下 |d_HT - d_lz*| < 0.3 且 p>0.3 意味着：
- discrimination (a)：对 contaminated vs clean 的区分无贡献 → LLM 的 contamination 不表现为 item-specific discrimination 差异
- guessing (c)：无贡献 → guessing 参数在 LLM context 下可能本身就不适用（LLM 不 "guess"）
- feasibility (d)：无贡献 → upper asymptote 对 contamination pattern 没有鉴别力

这个发现与我此前关于 "lz* ≈ accuracy z-score" 的讨论构成一个完整的 degradation chain：**4PL IRT → HT (1-param) → accuracy z-score，每一步简化都几乎不损失 detection power**。论文的整个 psychometric sophistication 被证明是 unnecessary overhead。

**对 framing 的影响**：R1 说得对，这应该是论文的核心发现之一，而非 buried in results。如果 reframe 为 "we show that psychometric complexity adds nothing beyond simple accuracy comparison for LLM contamination detection"，这反而是一个更有力的、更有指导意义的 negative result。当前 framing 仍然暗示 IRT 框架有价值，与自己的数据矛盾。

**[AGREE] W2 [Major]: n=3 seeds 不报告 CI**

已在上一轮确认。补充：Mistral/Gemma 仅 single clean seed 这个细节更令人担忧——single seed 的 d 估计在统计上几乎没有意义，不应在正文中作为 evidence 呈现。

**[AGREE] W3 [Major]: 0 figures, 14+ tables**

已多次确认。对 characterization study 来说尤其致命——"刻画"类研究的核心价值就在于让读者 see the pattern，纯表格无法实现这个目标。

**[AGREE] W4 [Major]: Post-RL failure 限制实际适用范围**

同意。2025-2026 主流 deployed LLMs 几乎全部经过 alignment（RLHF/DPO/GRPO）。方法仅适用于 SFT-only models，而这类模型在 leaderboard 上的占比和实际重要性都在快速下降。这严重限制了 practical impact。

**[AGREE] W5 [Moderate]: 检测阈值过高**

MMLU 10-15%、GSM8K 25%+ 的检测阈值意味着只有严重污染才能被检测到。在实际场景中，most concerning 的是 low-level contamination（几个百分点的 benchmark leakage），而方法对此完全无效。

**[AGREE] W6 [Moderate]: 缺少 accuracy z-score baseline**

结合 W1（HT ≈ lz*）和此前讨论（lz* ≈ accuracy z-score），这个缺失变得更加关键。论文至少需要一个 trivial baseline 对照来 justify 复杂方法的必要性。缺少这个对照，读者无法判断 IRT 框架是否值得采用。

**[AGREE] W7 [Moderate]: Thin sections 浪费篇幅**

lz,m 一段 + natural experiment n=5 在 8 页限制下是不可接受的篇幅浪费。这些内容要么扩展到有意义的分析深度，要么删除/移至 appendix。

**[AGREE] W8 [Minor]: 14 references + 无独立 Related Work**

14 篇比之前的 7-9 篇有改善，但仍远不够。无独立 Related Work section 在 EMNLP 中是 unusual 且会被 reviewer 标记。

---

### 对 Director 三个关键问题的回应

**Q1: W1（HT ≈ lz*）对论文 framing 的影响**

这是 **最后一根稻草**。此前的 degradation evidence 是：
- lz* ≈ accuracy z-score（IRT 不优于 trivial statistic）
- Post-RL signal loss（方法不 robust）
- 2/12 cells significant（scope 极窄）

W1 补上了缺失的一环：**即使在 IRT 框架内部**，复杂度也是无用的——HT（1 param）= lz*（4 params）。这意味着论文从 "complex method doesn't beat simple baseline" 升级为 "complex method doesn't even beat its own simplified version"。

建议 reframe 方向：将 4PL→HT→z-score 的 degradation chain 作为**论文的主线叙事**，核心 message 变为 "psychometric complexity is unnecessary for binary-only contamination detection, and here's why (θ-shift mechanism)"。

**Q2: W2 + W5 + W6 的 triple threat**

三者叠加效应远大于单个问题：
- n=3 seeds → 所有效应量估计不可靠 → 无法确信方法在任何条件下真正 work
- 高检测阈值 → 即使 work 也只能检测严重污染 → practical value 有限
- 无 simple baseline → 无法确认 observed detection 是否来自 IRT 而非 trivial statistics

组合起来：**我们不确定方法是否有效（n=3），即使有效也只抓大问题（高阈值），且可能一个简单的 z-score 就能做到同样的事（无 baseline）**。这三个问题的交集使得论文的 positive claims 基本没有可靠支撑。

**Q3: 独立评分**

**R2 评分：2.5 (Borderline Findings)**，与 R1 一致。

W1（HT ≈ lz*）是本轮新增的 critical finding，如果我在首轮审稿时就识别到这一点，我可能从一开始就不会给 3.0。这个发现与此前所有已知问题叠加，确认了论文当前版本处于 Findings 边界。

Memorization fraction + θ-shift mechanism + degradation chain (4PL→HT→z-score) 作为 negative results 有真实价值，但需要 reframing + 统计修复（seeds ≥10 + CI）+ presentation 改善才能达到 solid Findings (3.0)。

---

### R1 Questions 的独立回应

**Q1 (HT ≈ lz* → reframe?)**：是的，应 reframe 为 "item difficulty alone suffices, psychometric complexity adds nothing"，这反而是更有力的 takeaway。

**Q2 (accuracy z-score baseline?)**：论文必须加入。如果 z-score ≈ HT ≈ lz*，这条 degradation chain 本身就是论文最有价值的发现。

**Q3 (Leaderboard audit 放弃原因?)**：论文应明确讨论。如果是因为方法 scale up 后效果太差，这也是一个值得报告的 negative result。

R2 交叉回应完毕。全部 8 个 weakness [AGREE]，评分 2.5 与 R1 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 177 · 2026-05-21T13:22:19.488679+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "## Review Issue Tracker — Final (all 6 paper versions reviewed)\n## 16 original + 6 REV-ADD + 3 ACTUAL-B + 3 ACTUAL-C (HT variant)\n\n# ===== ACTIONABLE ISSUES (applies to actual paper) =====\n\n- id: \"BEST-W1\"\n  summary: \"Presentation: need figures + references (Dream had 14 tables/0 figs/7 refs)\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 Major presentation. R2 scholarly completeness. Both agree high-friction in ARR.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml approved: 4 figures + 3 tables + 30-35 references. Paper Agent Step 2/3 executing.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W3\"\n  summary: \"4PL parameter source unclear — must clarify PSN-IRT neural network origin, NOT py-irt\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"ltm R package does 2PL not 4PL. Parameters from PSN-IRT (Lee et al., AAAI 2026).\"\n  action_items:\n    - round: 1\n      action: \"Method section: clarify PSN-IRT origin. Do NOT mention py-irt.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W5\"\n  summary: \"Clean-clean Δlz*≈0.70 baseline drift needs discussion\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Non-zero baseline shift — SFT stochasticity noise floor.\"\n  action_items:\n    - round: 1\n      action: \"Report n=3 clean seeds lz* variance, position 0.70 as noise floor.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W6\"\n  summary: \"Need binary-only baseline comparison (accuracy z-score / ML classifier)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Missing same-information-level baseline.\"\n  action_items:\n    - round: 1\n      action: \"Write lz* 57/60 vs z-score 4/60 + simulation ML classifier comparison into Experiments.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W3\"\n  summary: \"Single contamination mechanism (QLoRA SFT) — scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"QLoRA-specific patterns limit generalizability.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: acknowledge QLoRA-specific, pre-training may differ.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W4\"\n  summary: \"Design document experiments partially missing (natural experiment, IRT refit)\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"θ-fixed + memorization fraction DONE. Natural experiment + IRT refit to report.\"\n  action_items:\n    - round: 1\n      action: \"IRT refit → Claim 3c. Natural experiment → future work if no data.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-F1\"\n  summary: \"Page limit compliance (8 pages strict)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream papers exceeded. writing_plan budget 3500 words.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml enforces 3500-word budget + 4 fig + 3 tab = 8 pages.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-F1\"\n  summary: \"Limitations must be independent section (EMNLP 2026 mandatory)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Not a Discussion subsection.\"\n  action_items:\n    - round: 1\n      action: \"Confirmed in writing_plan.yaml.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W1\"\n  summary: \"Systematic positive bias / IRT model misfit for LLMs\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Downgraded from showstopper. Δlz* design + bootstrap null address this.\"\n  action_items:\n    - round: 1\n      action: \"Explain Δlz* as difference-in-differences; report bootstrap null KS by benchmark size.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== REV-ADD ISSUES =====\n\n- id: \"REV-ADD-1\"\n  summary: \"Type-I error rate needs explicit reporting in Results\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Report BY BENCHMARK SIZE: MMLU/HellaSwag 8.3%, HumanEval 75%, ARC-C 58.3%, overall 40%.\"\n  action_items:\n    - round: 1\n      action: \"Dedicated Results paragraph on Type-I error rate by benchmark size.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-2\"\n  summary: \"Single-model ctrl-contam generalizability (only Qwen2.5-7B)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"ctrl-contam validated on 1 base model only.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: acknowledge single-model validation. Future work: multi-family.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-3\"\n  summary: \"IRT assumption violation needs explicit discussion\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Need ≥1 paragraph on Δlz* as difference-in-differences canceling systematic bias.\"\n  action_items:\n    - round: 1\n      action: \"Method/Discussion: explain why lz* retains value despite IRT violations.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-4\"\n  summary: \"Post-RL structural argument wording constraint\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Write 'structurally invariant... empirical verification future work', NOT 'robust to post-RL'.\"\n  action_items:\n    - round: 1\n      action: \"Exact wording constraint for Paper Agent.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-5\"\n  summary: \"57/60 vs 4/60 must be framed as universal misfit, NOT contamination detection\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"57/60 = universal 4PL misfit. Contamination evidence: simulation AUROC + ctrl-contam d=3.85.\"\n  action_items:\n    - round: 1\n      action: \"57/60 vs 4/60 → Claim 3a only. Contamination → simulation + ctrl-contam.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-6\"\n  summary: \"KS calibration rate 8.3% is MMLU-specific; overall 40%\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Must report full distribution by benchmark size.\"\n  action_items:\n    - round: 1\n      action: \"Results: report by benchmark size. paper_framing.md updated.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ACTUAL-B ISSUES (realistic-b: \"When Can Binary Response Patterns\") =====\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient — must-fix\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Need ≥10 seeds. Mistral/Gemma single seed even worse.\"\n  action_items:\n    - round: 1\n      action: \"Increase seeds to ≥10. Report CI for Cohen's d.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W2\"\n  summary: \"R²=0.65 insufficient for 'predictive theory' claims\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"35% unexplained variance. Downgrade to 'empirical trend'.\"\n  action_items:\n    - round: 1\n      action: \"Reframe as 'empirical trend'. No 'law'/'theory' language if R²<0.80.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W3\"\n  summary: \"Memorization fraction heterogeneity makes deployment impractical\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"6-15% varies across models/benchmarks. Detection threshold depends on unknown contamination level.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: discuss heterogeneity and deployment implications.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ACTUAL-C ISSUES (HT variant: \"IRT-FIT: Person-Fit Statistics\") =====\n\n- id: \"ACTUAL-C-W1\"\n  summary: \"HT ≈ lz* in ALL conditions — 4PL IRT framework unnecessary\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-c\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"HT (1 param: item difficulty) matches lz* (4 params) in all conditions. |d_HT - d_lz*|<0.3, p>0.3. Discrimination (a), guessing (c), feasibility (d) contribute nothing. R2: 'last straw' — completes degradation chain 4PL→HT→z-score. Must reframe as core finding, not bury in results.\"\n  action_items:\n    - round: 1\n      action: \"Reframe paper: 4PL→HT→z-score degradation chain as CORE narrative. Message: 'psychometric complexity unnecessary for binary contamination detection'. θ-shift mechanism explains why.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-C-W2\"\n  summary: \"Thin sections waste space (lz,m one-paragraph + natural experiment n=5)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-c\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"lz,m: one paragraph, no table, negative result → one sentence. Natural experiment n=5: all p>0.28, severely underpowered → delete or appendix. Free space for figures/CI/HT discussion.\"\n  action_items:\n    - round: 1\n      action: \"Delete or move to appendix. Use freed space for figures and degradation chain discussion.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-C-W3\"\n  summary: \"Detection threshold too high for practical low-level contamination\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-c\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"MMLU needs 10-15%, GSM8K needs 25%+ contamination. Real-world concern is 3-5% leakage. Method completely ineffective at low contamination levels.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: explicitly acknowledge high detection threshold. Discuss implications for practical use.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== FILTERED (Dream-imagined, N/A) =====\n\n- id: \"BEST-W2\"\n  summary: \"Leaderboard audit (11,200 models) no ground-truth validation\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined. D011 abandoned.\"\n  action_items: []\n  resolution: \"N/A — Dream-imagined experiment.\"\n  resolution_round: 1\n\n- id: \"MED-N1\"\n  summary: \"Per-family median baseline chicken-and-egg problem\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined leaderboard method.\"\n  action_items: []\n  resolution: \"N/A — Dream-imagined.\"\n  resolution_round: 1\n\n- id: \"MED-N2\"\n  summary: \"Post-RL AUROC 0.56 scope gap\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined post-RL result.\"\n  action_items: []\n  resolution: \"N/A — exp-post-rl P2 deferred.\"\n  resolution_round: 1\n\n- id: \"ALL-W2\"\n  summary: \"Incomplete tables / selective data display\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream artifact.\"\n  action_items: []\n  resolution: \"N/A — Dream artifact.\"\n  resolution_round: 1\n\n# ===== REJECTED (factually incorrect) =====\n\n- id: \"ACTUAL-W1\"\n  summary: \"REJECTED: 'lz* ≈ accuracy z-score, no added value'\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Based on Dream data. Actual: lz* 57/60 vs z-score 4/60. But NOTE: this is universal misfit, not contamination detection.\"\n  action_items: []\n  resolution: \"REJECTED — factually incorrect. 57/60 vs 4/60 is misfit evidence, not detection.\"\n  resolution_round: 1\n\n- id: \"ACTUAL-W2\"\n  summary: \"REJECTED: 'Cross-model only 2/12 cells significant'\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Based on Dream data. Actual: |Cohen's d|=3.85.\"\n  action_items: []\n  resolution: \"REJECTED — factually incorrect.\"\n  resolution_round: 1\n\n- id: \"WORST-N1\"\n  summary: \"Impossibility/information-theoretic bound overclaim\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Already prohibited by paper_framing.md #7.\"\n  action_items: []\n  resolution: \"Already addressed.\"\n  resolution_round: 1\n\n- id: \"WORST-N2\"\n  summary: \"Single mechanism insufficient for fundamental bottleneck conclusion\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Already scoped to SFT contamination.\"\n  action_items: []\n  resolution: \"Already addressed.\"\n  resolution_round: 1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "## Review Issue Tracker — Final (all 6 paper versions reviewed)\n## 16 original + 6 REV-ADD + 3 ACTUAL-B + 3 ACTUAL-C (HT variant)\n\n# ===== ACTIONABLE ISSUES (applies to actual paper) =====\n\n- id: \"BEST-W1\"\n  summary: \"Presentation: need figures + references (Dream had 14 tables/0 figs/7 refs)\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 Major presentation. R2 scholarly completeness. Both agree high-friction in ARR.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml approved: 4 figures + 3 tables + 30-35 references. Paper Agent Step 2/3 executing.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W3\"\n  summary: \"4PL parameter source unclear — must clarify PSN-IRT neural network origin, NOT py-irt\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"ltm R package does 2PL not 4PL. Parameters from PSN-IRT (Lee et al., AAAI 2026).\"\n  action_items:\n    - round: 1\n      action: \"Method section: clarify PSN-IRT origin. Do NOT mention py-irt.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W5\"\n  summary: \"Clean-clean Δlz*≈0.70 baseline drift needs discussion\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Non-zero baseline shift — SFT stochasticity noise floor.\"\n  action_items:\n    - round: 1\n      action: \"Report n=3 clean seeds lz* variance, position 0.70 as noise floor.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W6\"\n  summary: \"Need binary-only baseline comparison (accuracy z-score / ML classifier)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Missing same-information-level baseline.\"\n  action_items:\n    - round: 1\n      action: \"Write lz* 57/60 vs z-score 4/60 + simulation ML classifier comparison into Experiments.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W3\"\n  summary: \"Single contamination mechanism (QLoRA SFT) — scope limitation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"QLoRA-specific patterns limit generalizability.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: acknowledge QLoRA-specific, pre-training may differ.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-W4\"\n  summary: \"Design document experiments partially missing (natural experiment, IRT refit)\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"θ-fixed + memorization fraction DONE. Natural experiment + IRT refit to report.\"\n  action_items:\n    - round: 1\n      action: \"IRT refit → Claim 3c. Natural experiment → future work if no data.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"BEST-F1\"\n  summary: \"Page limit compliance (8 pages strict)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream papers exceeded. writing_plan budget 3500 words.\"\n  action_items:\n    - round: 1\n      action: \"writing_plan.yaml enforces 3500-word budget + 4 fig + 3 tab = 8 pages.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-F1\"\n  summary: \"Limitations must be independent section (EMNLP 2026 mandatory)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Not a Discussion subsection.\"\n  action_items:\n    - round: 1\n      action: \"Confirmed in writing_plan.yaml.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ALL-W1\"\n  summary: \"Systematic positive bias / IRT model misfit for LLMs\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Downgraded from showstopper. Δlz* design + bootstrap null address this.\"\n  action_items:\n    - round: 1\n      action: \"Explain Δlz* as difference-in-differences; report bootstrap null KS by benchmark size.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== REV-ADD ISSUES =====\n\n- id: \"REV-ADD-1\"\n  summary: \"Type-I error rate needs explicit reporting in Results\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Report BY BENCHMARK SIZE: MMLU/HellaSwag 8.3%, HumanEval 75%, ARC-C 58.3%, overall 40%.\"\n  action_items:\n    - round: 1\n      action: \"Dedicated Results paragraph on Type-I error rate by benchmark size.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-2\"\n  summary: \"Single-model ctrl-contam generalizability (only Qwen2.5-7B)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"ctrl-contam validated on 1 base model only.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: acknowledge single-model validation. Future work: multi-family.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-3\"\n  summary: \"IRT assumption violation needs explicit discussion\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Need ≥1 paragraph on Δlz* as difference-in-differences canceling systematic bias.\"\n  action_items:\n    - round: 1\n      action: \"Method/Discussion: explain why lz* retains value despite IRT violations.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-4\"\n  summary: \"Post-RL structural argument wording constraint\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Write 'structurally invariant... empirical verification future work', NOT 'robust to post-RL'.\"\n  action_items:\n    - round: 1\n      action: \"Exact wording constraint for Paper Agent.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-5\"\n  summary: \"57/60 vs 4/60 must be framed as universal misfit, NOT contamination detection\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"57/60 = universal 4PL misfit. Contamination evidence: simulation AUROC + ctrl-contam d=3.85.\"\n  action_items:\n    - round: 1\n      action: \"57/60 vs 4/60 → Claim 3a only. Contamination → simulation + ctrl-contam.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"REV-ADD-6\"\n  summary: \"KS calibration rate 8.3% is MMLU-specific; overall 40%\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Must report full distribution by benchmark size.\"\n  action_items:\n    - round: 1\n      action: \"Results: report by benchmark size. paper_framing.md updated.\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ACTUAL-B ISSUES (realistic-b: \"When Can Binary Response Patterns\") =====\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient — must-fix\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Need ≥10 seeds. Mistral/Gemma single seed even worse.\"\n  action_items:\n    - round: 1\n      action: \"Increase seeds to ≥10. Report CI for Cohen's d.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W2\"\n  summary: \"R²=0.65 insufficient for 'predictive theory' claims\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"35% unexplained variance. Downgrade to 'empirical trend'.\"\n  action_items:\n    - round: 1\n      action: \"Reframe as 'empirical trend'. No 'law'/'theory' language if R²<0.80.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W3\"\n  summary: \"Memorization fraction heterogeneity makes deployment impractical\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-b\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"6-15% varies across models/benchmarks. Detection threshold depends on unknown contamination level.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: discuss heterogeneity and deployment implications.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ACTUAL-C ISSUES (HT variant: \"IRT-FIT: Person-Fit Statistics\") =====\n\n- id: \"ACTUAL-C-W1\"\n  summary: \"HT ≈ lz* in ALL conditions — 4PL IRT framework unnecessary\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-c\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"HT (1 param: item difficulty) matches lz* (4 params) in all conditions. |d_HT - d_lz*|<0.3, p>0.3. Discrimination (a), guessing (c), feasibility (d) contribute nothing. R2: 'last straw' — completes degradation chain 4PL→HT→z-score. Must reframe as core finding, not bury in results.\"\n  action_items:\n    - round: 1\n      action: \"Reframe paper: 4PL→HT→z-score degradation chain as CORE narrative. Message: 'psychometric complexity unnecessary for binary contamination detection'. θ-shift mechanism explains why.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-C-W2\"\n  summary: \"Thin sections waste space (lz,m one-paragraph + natural experiment n=5)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-c\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"lz,m: one paragraph, no table, negative result → one sentence. Natural experiment n=5: all p>0.28, severely underpowered → delete or appendix. Free space for figures/CI/HT discussion.\"\n  action_items:\n    - round: 1\n      action: \"Delete or move to appendix. Use freed space for figures and degradation chain discussion.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"ACTUAL-C-W3\"\n  summary: \"Detection threshold too high for practical low-level contamination\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual-c\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"MMLU needs 10-15%, GSM8K needs 25%+ contamination. Real-world concern is 3-5% leakage. Method completely ineffective at low contamination levels.\"\n  action_items:\n    - round: 1\n      action: \"Limitations: explicitly acknowledge high detection threshold. Discuss implications for practical use.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== FILTERED (Dream-imagined, N/A) =====\n\n- id: \"BEST-W2\"\n  summary: \"Leaderboard audit (11,200 models) no ground-truth validation\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: best\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined. D011 abandoned.\"\n  action_items: []\n  resolution: \"N/A — Dream-imagined experiment.\"\n  resolution_round: 1\n\n- id: \"MED-N1\"\n  summary: \"Per-family median baseline chicken-and-egg problem\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined leaderboard method.\"\n  action_items: []\n  resolution: \"N/A — Dream-imagined.\"\n  resolution_round: 1\n\n- id: \"MED-N2\"\n  summary: \"Post-RL AUROC 0.56 scope gap\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: median\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream-imagined post-RL result.\"\n  action_items: []\n  resolution: \"N/A — exp-post-rl P2 deferred.\"\n  resolution_round: 1\n\n- id: \"ALL-W2\"\n  summary: \"Incomplete tables / selective data display\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: all\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream artifact.\"\n  action_items: []\n  resolution: \"N/A — Dream artifact.\"\n  resolution_round: 1\n\n# ===== REJECTED (factually incorrect) =====\n\n- id: \"ACTUAL-W1\"\n  summary: \"REJECTED: 'lz* ≈ accuracy z-score, no added value'\"\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Based on Dream data. Actual: lz* 57/60 vs z-score 4/60. But NOTE: this is universal misfit, not contamination detection.\"\n  action_items: []\n  resolution: \"REJECTED — factually incorrect. 57/60 vs 4/60 is misfit evidence, not detection.\"\n  resolution_round: 1\n\n- id: \"ACTUAL-W2\"\n  summary: \"REJECTED: 'Cross-model only 2/12 cells significant'\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: actual\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Based on Dream data. Actual: |Cohen's d|=3.85.\"\n  action_items: []\n  resolution: \"REJECTED — factually incorrect.\"\n  resolution_round: 1\n\n- id: \"WORST-N1\"\n  summary: \"Impossibility/information-theoretic bound overclaim\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Already prohibited by paper_framing.md #7.\"\n  action_items: []\n  resolution: \"Already addressed.\"\n  resolution_round: 1\n\n- id: \"WORST-N2\"\n  summary: \"Single mechanism insufficient for fundamental bottleneck conclusion\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  applies_to: worst\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Already scoped to SFT contamination.\"\n  action_items: []\n  resolution: \"Already addressed.\"\n  resolution_round: 1"
  }
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-21T13:22:19.590681+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 16106}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 179 · 2026-05-21T13:24:08.379392+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告（最终版 v6）：irt_personfit_contam — 6 篇论文综合评估\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n**Round**: 1\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)\n**收敛状态**: 六份审稿评分完全一致（R1 = R2），无分歧\n\n⚠️ **本报告为最终版 v6**，替换此前所有提交。覆盖 3 个 dream 版本 + 3 个实际论文版本。\n\n---\n\n## 评分总览\n\n| # | 版本 | 标题关键词 | R1 | R2 | 共识 | 投稿建议 |\n|---|------|-----------|----|----|------|---------|\n| 1 | Dream Best | Detecting Benchmark Contamination | 3.5 | 3.5 | ✅ | 理想目标 |\n| 2 | Dream Median | Characterizing Detection Frontier | 3.0 | 3.0 | ✅ | — |\n| 3 | Dream Worst | Binary Response Bottleneck | 2.5 | 2.5 | ✅ | — |\n| 4 | Actual v1 | Psychometric Diagnostics | 2.5 | 2.5 | ✅ | 不投 |\n| 5 | Actual v2 | When Can Binary Response Patterns | 2.5 | 2.5 | ✅ | 不投 |\n| 6 | **Actual v3** | **Person-Fit Statistics (HT variant)** | **2.5** | **2.5** | ✅ | **不投** |\n\n**核心结论：三版实际论文均 2.5（Borderline Findings）。最新版（v3）暴露了此前未识别的 critical finding：HT ≈ lz*，4PL IRT 框架的全部复杂性被证明不必要。**\n\n---\n\n## 最新版实际论文评估（v3, HT variant — 最高优先级）\n\n### 标题\n\"IRT-FIT: Person-Fit Statistics for LLM Benchmark Contamination Detection at the Minimal-Information Operating Point\"\n\n### Summary\n论文将 IRT person-fit 统计量（lz* 和 HT）应用于 LLM benchmark contamination 检测。4 model families × 3 benchmarks × 6 contamination levels 控制实验。核心检测在 Qwen/Llama × MMLU 可行，Gemma/Mistral 失败，post-RL 后所有方法信号消失。\n\n### 本轮最重要的新发现\n\n**CRITICAL: 完整 Degradation Chain（4PL → HT → accuracy z-score）**\n\nR1 识别、R2 确认的 degradation chain 是本轮审稿的核心结论：\n\n1. **4PL lz* → HT（1-param）**：HT 仅用 item difficulty，在所有条件下 |d_HT - d_lz*| < 0.3, p>0.3。Discrimination (a)、guessing (c)、feasibility (d) 对检测力零贡献。\n2. **HT → accuracy z-score**：结合此前审稿发现（lz* ≈ z-score +0.02-0.03 AUROC），三级简化均不损失检测力。\n3. **Implication**：论文的全部 psychometric sophistication（4PL 拟合、lz* 计算、Snijders 标准化、PSN-IRT 依赖）是 unnecessary overhead。一个简单的 accuracy z-score 做到同样的事。\n\nR2 评价：\"这是最后一根稻草。论文从 'complex method doesn't beat simple baseline' 升级为 'complex method doesn't even beat its own simplified version'。\"\n\n**这个发现应成为论文的核心叙事，而非 buried in results。**\n\n### Strengths（R1/R2 一致）\n\n**S1. Cross-disciplinary bridge genuinely novel**。将 60+ 年 psychometric person-fit 文献引入 LLM contamination detection，建立 vocabulary bridge。\n\n**S2. Detection frontier / information access hierarchy**。Binary < re-test < token probs < weights 的层级 framing，使 \"low AUROC\" 不再是 failure 而是 \"cost of minimal information\"。\n\n**S3. Post-RL boundary 明确划定**。|d|<0.5, ALL methods AUROC 0.51-0.53。诚实的 negative result，与 Wang et al. (2025) 一致。\n\n**S4. θ-shift mechanism + memorization fraction**。SFT 通过全局 θ 提升（非 item-specific cheating）的机制解释。Memorization fraction（Qwen/Llama 0.32-0.35 vs Gemma/Mistral 0.15-0.17）提供 model-family boundary。\n\n**S5. Scope-honest framing**。2/4 families × 1/3 benchmarks 显著的情况下没有 overclaim。\n\n### Weaknesses（按严重度排序）\n\n**W1 [Critical]: HT ≈ lz* undermines 4PL IRT necessity（NEW）**\n- 整个 4PL 框架是 unnecessary overhead\n- 论文未将此作为核心发现\n- 应 reframe 为 \"psychometric complexity is unnecessary for binary contamination detection\"\n- θ-shift mechanism 解释了 why：SFT contamination 不表现为 item-specific aberrance\n\n**W2 [Major]: n=3 seeds 不报告 CI**\n- Cohen's d 在 n=3 下 CI ≈ ±1.2\n- Mistral/Gemma 仅 single seed → point estimates unreliable\n- 所有 effect size claims 缺乏统计支撑\n\n**W3 [Major]: 0 figures, 14+ tables**\n- Characterization study 需要 visual characterization\n- 缺少 detection frontier diagram、dose-response curves、ROC curves\n- 严重影响 accessibility 和 persuasiveness\n\n**W4 [Major]: Post-RL failure 限制 practical scope**\n- 2025-2026 几乎所有 deployed LLMs 经过 RLHF/DPO/GRPO\n- 方法仅限 SFT-only models\n\n**W5 [Moderate]: 检测阈值过高**\n- MMLU 10-15%, GSM8K 25%+\n- 实际关注的 3-5% low-level contamination 无法检测\n\n**W6 [Moderate]: 缺少 accuracy z-score baseline**\n- 结合 W1（HT ≈ lz*），如果 z-score ≈ HT ≈ lz*，整个 person-fit framework 无附加值\n- 必须加入以验证或否定\n\n**W7 [Moderate]: Thin sections 浪费篇幅**\n- lz,m: 一段话，负面结果 → 一句话\n- Natural experiment n=5: p>0.28 → 删除或 appendix\n- 释放空间给 figures/CI/HT discussion\n\n**W8 [Minor]: 14 references, 无独立 Related Work**\n- 远低于 EMNLP 标准\n- 缺少 person-fit、contamination detection、LLM evaluation 核心文献\n\n### Triple Threat（R2 分析）\n\nn=3 seeds + 高检测阈值 + 无 simple baseline 的组合效应：\n- 不确定方法是否有效（n=3 CI 太宽）\n- 即使有效也只抓大问题（高阈值）\n- 可能一个简单 z-score 就够（无 baseline 验证）\n- 三者交集使 positive claims 基本无可靠支撑\n\n### Overall Score: 2.5 (Borderline Findings)\n\n4 Major issues (W1-W4)。HT ≈ lz* 是最 damaging 的发现——论文方法论的 raison d'être 被自己的数据否定。正面贡献（cross-disciplinary bridge, θ-shift, memorization fraction, detection frontier, degradation chain itself）足以考虑 Findings，但需要 substantial reframing + statistical fix。\n\n---\n\n## 跨版本一致性分析\n\n### 6 版论文共同的正面贡献\n1. Power function 理论框架（概念有价值，即使 R²=0.65）\n2. Detection frontier / information access hierarchy\n3. θ-shift mechanism + memorization fraction\n4. 诚实的 negative result 呈现\n\n### 6 版论文共同的问题\n1. 0 figures（所有版本）\n2. References 不足（7-14 篇）\n3. 单一污染机制（QLoRA SFT）\n4. Post-RL signal loss\n5. IRT 参数适用性未验证\n\n### 实际论文的累积问题（v1→v2→v3）\n| 问题 | v1 | v2 | v3 |\n|------|----|----|-----|\n| lz* ≈ z-score | ✓ | ✓ | ✓ |\n| HT ≈ lz* | — | — | **NEW** ✓ |\n| n=3 seeds/no CI | — | ✓ | ✓ |\n| R²=0.65 | — | ✓ | — |\n| 10 pages | ✓ | ✓ | ✓ |\n| 0 figures | ✓ | ✓ | ✓ |\n\n**v3 的 HT ≈ lz* 是决定性的新发现**，完成了 4PL→HT→z-score 的 degradation chain，彻底否定了 IRT complexity 的附加值。\n\n---\n\n## 对 Research Director 的行动建议\n\n### 不建议当前版本投 EMNLP 2026\n\n理由：4 Major weaknesses（HT≈lz* + n=3 no CI + 0 figures + post-RL failure），R1/R2 一致 2.5。\n\n### 建议 Reframing 方向\n\n**核心叙事转型**：从 \"IRT-FIT as detection tool\" 转为 **\"Why psychometric complexity fails for LLM contamination detection: the degradation chain and θ-shift mechanism\"**\n\n关键 message：\n1. 4PL IRT → HT (1-param) → accuracy z-score，每步简化不损失 detection power\n2. θ-shift mechanism 解释 why：SFT contamination 通过全局能力提升而非 item-specific cheating\n3. Memorization fraction 量化了 generalization 对 signal 的稀释程度\n4. Post-RL 是所有 binary methods 的 hard boundary（不仅是 IRT）\n\n### 修复优先级\n\n**Must-fix（投稿前提）**：\n1. Seeds ≥10 + CI for all Cohen's d\n2. 压缩至 8 页（删 thin sections，加 3-4 figures）\n3. 加 accuracy z-score baseline（验证 degradation chain 最后一环）\n4. 将 HT ≈ lz* 和 degradation chain 提升为核心发现\n5. References ≥20 + 独立 Related Work section\n\n**Should-fix（提升至 3.0）**：\n6. 讨论 \"when does full IRT parameterization matter\"\n7. 更多 model families 验证\n8. 明确讨论检测阈值的 practical implications\n\n### 投稿时间线\n\n- **2026-05-25 deadline**：不投\n- **下一 ARR cycle（~2026-07）**：完成 reframing + must-fix，目标 3.0 (Findings)\n- **如 post-RL 突破（AUROC ≥0.85）**：目标 3.5 (Borderline Conference)\n\n---\n\n## Questions for Authors\n\nQ1. HT ≈ lz*：是否考虑将 degradation chain (4PL→HT→z-score) 作为论文核心 narrative？\n\nQ2. Accuracy z-score baseline：如果 z-score ≈ HT ≈ lz*，论文的 motivation 需要如何重构？\n\nQ3. n=3 seeds 下 Cohen's d=1.8 的 bootstrap 95% CI 是多少？CI 是否跨越有意义的 threshold（如 d=0.8）？\n\nQ4. Leaderboard audit 放弃原因？如果是 detection power 不足，这本身是重要 negative result。\n\nQ5. Mistral/Gemma 仅 single clean seed 的 d 估计是否应从主文移至 appendix 并标注 \"preliminary\"？\n\nQ6. 检测阈值（MMLU 10-15%）在实际 benchmark leakage 场景中（通常 3-5%）是否完全无效？\n\n---\n\n## Missing References\n\n**Person-fit statistics：**\nKarabatsos (2003); Van der Flier (1982); Drasgow, Levine & Williams (1985)\n\n**Contamination detection：**\nOren et al. (2024) ICLR; Deng et al. (2024) NAACL; Magar & Schwartz (2022) ACL; Polo et al. (2024) ICML; Golchin & Surdeanu (2024)\n\n**LLM evaluation / IRT-for-LLM：**\nBurnham et al. (2024); Jacobs et al. (2024)\n\n**Reference verification：** Wang et al. (2025) [Ref 8] 需确认可查证（arXiv ID）；如为未公开工作需标注 \"personal communication\"。\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n## Visual Layout Check\n\n视觉审查：未启动（not_started）。\n\n---\n\n## Reviewer 共识记录（最终）\n\n| # | 版本 | R1 | R2 | 共识 |\n|---|------|----|----|------|\n| 1 | Dream Best | 3.5 | 3.5 | ✅ |\n| 2 | Dream Median | 3.0 | 3.0 | ✅ |\n| 3 | Dream Worst | 2.5 | 2.5 | ✅ |\n| 4 | Actual v1 | 2.5 | 2.5 | ✅ |\n| 5 | Actual v2 | 2.5 | 2.5 | ✅ |\n| 6 | Actual v3 | 2.5 | 2.5 | ✅ |\n\n**六份审稿完全一致，无任何未解决分歧。**\n\nR1/R2 共同建议：不投当前版本。将 degradation chain (4PL→HT→z-score) 作为核心叙事 reframe，修复统计问题（seeds ≥10 + CI），加 figures + baseline + references，下一 ARR cycle 投出，目标 3.0 (Findings)。",
  "project": "irt_personfit_contam",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "Dream Best 3.5 | Dream Median 3.0 | Dream Worst 2.5 | Actual v1 2.5 | Actual v2 2.5 | Actual v3 2.5 — 不建议当前版本投稿，reframe degradation chain 后目标 3.0",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告（最终版 v6）：irt_personfit_contam — 6 篇论文综合评估\n\n**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit\n**Round**: 1\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)\n**收敛状态**: 六份审稿评分完全一致（R1 = R2），无分歧\n\n⚠️ **本报告为最终版 v6**，替换此前所有提交。覆盖 3 个 dream 版本 + 3 个实际论文版本。\n\n---\n\n## 评分总览\n\n| # | 版本 | 标题关键词 | R1 | R2 | 共识 | 投稿建议 |\n|---|------|-----------|----|----|------|---------|\n| 1 | Dream Best | Detecting Benchmark Contamination | 3.5 | 3.5 | ✅ | 理想目标 |\n| 2 | Dream Median | Characterizing Detection Frontier | 3.0 | 3.0 | ✅ | — |\n| 3 | Dream Worst | Binary Response Bottleneck | 2.5 | 2.5 | ✅ | — |\n| 4 | Actual v1 | Psychometric Diagnostics | 2.5 | 2.5 | ✅ | 不投 |\n| 5 | Actual v2 | When Can Binary Response Patterns | 2.5 | 2.5 | ✅ | 不投 |\n| 6 | **Actual v3** | **Person-Fit Statistics (HT variant)** | **2.5** | **2.5** | ✅ | **不投** |\n\n**核心结论：三版实际论文均 2.5（Borderline Findings）。最新版（v3）暴露了此前未识别的 critical finding：HT ≈ lz*，4PL IRT 框架的全部复杂性被证明不必要。**\n\n---\n\n## 最新版实际论文评估（v3, HT variant — 最高优先级）\n\n### 标题\n\"IRT-FIT: Person-Fit Statistics for LLM Benchmark Contamination Detection at the Minimal-Information Operating Point\"\n\n### Summary\n论文将 IRT person-fit 统计量（lz* 和 HT）应用于 LLM benchmark contamination 检测。4 model families × 3 benchmarks × 6 contamination levels 控制实验。核心检测在 Qwen/Llama × MMLU 可行，Gemma/Mistral 失败，post-RL 后所有方法信号消失。\n\n### 本轮最重要的新发现\n\n**CRITICAL: 完整 Degradation Chain（4PL → HT → accuracy z-score）**\n\nR1 识别、R2 确认的 degradation chain 是本轮审稿的核心结论：\n\n1. **4PL lz* → HT（1-param）**：HT 仅用 item difficulty，在所有条件下 |d_HT - d_lz*| < 0.3, p>0.3。Discrimination (a)、guessing (c)、feasibility (d) 对检测力零贡献。\n2. **HT → accuracy z-score**：结合此前审稿发现（lz* ≈ z-score +0.02-0.03 AUROC），三级简化均不损失检测力。\n3. **Implication**：论文的全部 psychometric sophistication（4PL 拟合、lz* 计算、Snijders 标准化、PSN-IRT 依赖）是 unnecessary overhead。一个简单的 accuracy z-score 做到同样的事。\n\nR2 评价：\"这是最后一根稻草。论文从 'complex method doesn't beat simple baseline' 升级为 'complex method doesn't even beat its own simplified version'。\"\n\n**这个发现应成为论文的核心叙事，而非 buried in results。**\n\n### Strengths（R1/R2 一致）\n\n**S1. Cross-disciplinary bridge genuinely novel**。将 60+ 年 psychometric person-fit 文献引入 LLM contamination detection，建立 vocabulary bridge。\n\n**S2. Detection frontier / information access hierarchy**。Binary < re-test < token probs < weights 的层级 framing，使 \"low AUROC\" 不再是 failure 而是 \"cost of minimal information\"。\n\n**S3. Post-RL boundary 明确划定**。|d|<0.5, ALL methods AUROC 0.51-0.53。诚实的 negative result，与 Wang et al. (2025) 一致。\n\n**S4. θ-shift mechanism + memorization fraction**。SFT 通过全局 θ 提升（非 item-specific cheating）的机制解释。Memorization fraction（Qwen/Llama 0.32-0.35 vs Gemma/Mistral 0.15-0.17）提供 model-family boundary。\n\n**S5. Scope-honest framing**。2/4 families × 1/3 benchmarks 显著的情况下没有 overclaim。\n\n### Weaknesses（按严重度排序）\n\n**W1 [Critical]: HT ≈ lz* undermines 4PL IRT necessity（NEW）**\n- 整个 4PL 框架是 unnecessary overhead\n- 论文未将此作为核心发现\n- 应 reframe 为 \"psychometric complexity is unnecessary for binary contamination detection\"\n- θ-shift mechanism 解释了 why：SFT contamination 不表现为 item-specific aberrance\n\n**W2 [Major]: n=3 seeds 不报告 CI**\n- Cohen's d 在 n=3 下 CI ≈ ±1.2\n- Mistral/Gemma 仅 single seed → point estimates unreliable\n- 所有 effect size claims 缺乏统计支撑\n\n**W3 [Major]: 0 figures, 14+ tables**\n- Characterization study 需要 visual characterization\n- 缺少 detection frontier diagram、dose-response curves、ROC curves\n- 严重影响 accessibility 和 persuasiveness\n\n**W4 [Major]: Post-RL failure 限制 practical scope**\n- 2025-2026 几乎所有 deployed LLMs 经过 RLHF/DPO/GRPO\n- 方法仅限 SFT-only models\n\n**W5 [Moderate]: 检测阈值过高**\n- MMLU 10-15%, GSM8K 25%+\n- 实际关注的 3-5% low-level contamination 无法检测\n\n**W6 [Moderate]: 缺少 accuracy z-score baseline**\n- 结合 W1（HT ≈ lz*），如果 z-score ≈ HT ≈ lz*，整个 person-fit framework 无附加值\n- 必须加入以验证或否定\n\n**W7 [Moderate]: Thin sections 浪费篇幅**\n- lz,m: 一段话，负面结果 → 一句话\n- Natural experiment n=5: p>0.28 → 删除或 appendix\n- 释放空间给 figures/CI/HT discussion\n\n**W8 [Minor]: 14 references, 无独立 Related Work**\n- 远低于 EMNLP 标准\n- 缺少 person-fit、contamination detection、LLM evaluation 核心文献\n\n### Triple Threat（R2 分析）\n\nn=3 seeds + 高检测阈值 + 无 simple baseline 的组合效应：\n- 不确定方法是否有效（n=3 CI 太宽）\n- 即使有效也只抓大问题（高阈值）\n- 可能一个简单 z-score 就够（无 baseline 验证）\n- 三者交集使 positive claims 基本无可靠支撑\n\n### Overall Score: 2.5 (Borderline Findings)\n\n4 Major issues (W1-W4)。HT ≈ lz* 是最 damaging 的发现——论文方法论的 raison d'être 被自己的数据否定。正面贡献（cross-disciplinary bridge, θ-shift, memorization fraction, detection frontier, degradation chain itself）足以考虑 Findings，但需要 substantial reframing + statistical fix。\n\n---\n\n## 跨版本一致性分析\n\n### 6 版论文共同的正面贡献\n1. Power function 理论框架（概念有价值，即使 R²=0.65）\n2. Detection frontier / information access hierarchy\n3. θ-shift mechanism + memorization fraction\n4. 诚实的 negative result 呈现\n\n### 6 版论文共同的问题\n1. 0 figures（所有版本）\n2. References 不足（7-14 篇）\n3. 单一污染机制（QLoRA SFT）\n4. Post-RL signal loss\n5. IRT 参数适用性未验证\n\n### 实际论文的累积问题（v1→v2→v3）\n| 问题 | v1 | v2 | v3 |\n|------|----|----|-----|\n| lz* ≈ z-score | ✓ | ✓ | ✓ |\n| HT ≈ lz* | — | — | **NEW** ✓ |\n| n=3 seeds/no CI | — | ✓ | ✓ |\n| R²=0.65 | — | ✓ | — |\n| 10 pages | ✓ | ✓ | ✓ |\n| 0 figures | ✓ | ✓ | ✓ |\n\n**v3 的 HT ≈ lz* 是决定性的新发现**，完成了 4PL→HT→z-score 的 degradation chain，彻底否定了 IRT complexity 的附加值。\n\n---\n\n## 对 Research Director 的行动建议\n\n### 不建议当前版本投 EMNLP 2026\n\n理由：4 Major weaknesses（HT≈lz* + n=3 no CI + 0 figures + post-RL failure），R1/R2 一致 2.5。\n\n### 建议 Reframing 方向\n\n**核心叙事转型**：从 \"IRT-FIT as detection tool\" 转为 **\"Why psychometric complexity fails for LLM contamination detection: the degradation chain and θ-shift mechanism\"**\n\n关键 message：\n1. 4PL IRT → HT (1-param) → accuracy z-score，每步简化不损失 detection power\n2. θ-shift mechanism 解释 why：SFT contamination 通过全局能力提升而非 item-specific cheating\n3. Memorization fraction 量化了 generalization 对 signal 的稀释程度\n4. Post-RL 是所有 binary methods 的 hard boundary（不仅是 IRT）\n\n### 修复优先级\n\n**Must-fix（投稿前提）**：\n1. Seeds ≥10 + CI for all Cohen's d\n2. 压缩至 8 页（删 thin sections，加 3-4 figures）\n3. 加 accuracy z-score baseline（验证 degradation chain 最后一环）\n4. 将 HT ≈ lz* 和 degradation chain 提升为核心发现\n5. References ≥20 + 独立 Related Work section\n\n**Should-fix（提升至 3.0）**：\n6. 讨论 \"when does full IRT parameterization matter\"\n7. 更多 model families 验证\n8. 明确讨论检测阈值的 practical implications\n\n### 投稿时间线\n\n- **2026-05-25 deadline**：不投\n- **下一 ARR cycle（~2026-07）**：完成 reframing + must-fix，目标 3.0 (Findings)\n- **如 post-RL 突破（AUROC ≥0.85）**：目标 3.5 (Borderline Conference)\n\n---\n\n## Questions for Authors\n\nQ1. HT ≈ lz*：是否考虑将 degradation chain (4PL→HT→z-score) 作为论文核心 narrative？\n\nQ2. Accuracy z-score baseline：如果 z-score ≈ HT ≈ lz*，论文的 motivation 需要如何重构？\n\nQ3. n=3 seeds 下 Cohen's d=1.8 的 bootstrap 95% CI 是多少？CI 是否跨越有意义的 threshold（如 d=0.8）？\n\nQ4. Leaderboard audit 放弃原因？如果是 detection power 不足，这本身是重要 negative result。\n\nQ5. Mistral/Gemma 仅 single clean seed 的 d 估计是否应从主文移至 appendix 并标注 \"preliminary\"？\n\nQ6. 检测阈值（MMLU 10-15%）在实际 benchmark leakage 场景中（通常 3-5%）是否完全无效？\n\n---\n\n## Missing References\n\n**Person-fit statistics：**\nKarabatsos (2003); Van der Flier (1982); Drasgow, Levine & Williams (1985)\n\n**Contamination detection：**\nOren et al. (2024) ICLR; Deng et al. (2024) NAACL; Magar & Schwartz (2022) ACL; Polo et al. (2024) ICML; Golchin & Surdeanu (2024)\n\n**LLM evaluation / IRT-for-LLM：**\nBurnham et al. (2024); Jacobs et al. (2024)\n\n**Reference verification：** Wang et al. (2025) [Ref 8] 需确认可查证（arXiv ID）；如为未公开工作需标注 \"personal communication\"。\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n## Visual Layout Check\n\n视觉审查：未启动（not_started）。\n\n---\n\n## Reviewer 共识记录（最终）\n\n| # | 版本 | R1 | R2 | 共识 |\n|---|------|----|----|------|\n| 1 | Dream Best | 3.5 | 3.5 | ✅ |\n| 2 | Dream Median | 3.0 | 3.0 | ✅ |\n| 3 | Dream Worst | 2.5 | 2.5 | ✅ |\n| 4 | Actual v1 | 2.5 | 2.5 | ✅ |\n| 5 | Actual v2 | 2.5 | 2.5 | ✅ |\n| 6 | Actual v3 | 2.5 | 2.5 | ✅ |\n\n**六份审稿完全一致，无任何未解决分歧。**\n\nR1/R2 共同建议：不投当前版本。将 degradation chain (4PL→HT→z-score) 作为核心叙事 reframe，修复统计问题（seeds ≥10 + CI），加 figures + baseline + references，下一 ARR cycle 投出，目标 3.0 (Findings)。",
    "project": "irt_personfit_contam",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "Dream Best 3.5 | Dream Median 3.0 | Dream Worst 2.5 | Actual v1 2.5 | Actual v2 2.5 | Actual v3 2.5 — 不建议当前版本投稿，reframe degradation chain 后目标 3.0",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 180 · 2026-05-21T13:24:12.497662+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4118
}
```

</details>

---


### Assistant

_source line 181 · 2026-05-21T13:24:19.249818+00:00_

最终报告 v6 已投递。审稿圆桌会议结论：

**6 篇论文全部审完，R1/R2 完全一致：**
- Dream Best 3.5 | Median 3.0 | Worst 2.5
- 三版实际论文均 2.5

**本轮决定性发现**：HT ≈ lz* 完成了 4PL→HT→z-score 的 degradation chain，证明 IRT psychometric complexity 对 binary contamination detection 无附加值。建议将此作为论文核心叙事 reframe，修复统计问题后下一 ARR cycle 投出，目标 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 182 · 2026-05-21T13:24:21.954937+00:00_

[Reviewer 2 审稿结果]:


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 183 · 2026-05-21T13:24:26.818689+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 27

## Round 27

76 recorded events


### User

_source line 184 · 2026-05-21T18:02:15.439893+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_personfit_contam
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 185 · 2026-05-21T18:02:21.887613+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 186 · 2026-05-21T18:02:21.938645+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 187 · 2026-05-21T18:02:30.126499+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 188 · 2026-05-21T18:02:30.177170+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 189 · 2026-05-21T18:02:33.790679+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-21T18:02:33.841269+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 191 · 2026-05-21T18:02:41.469692+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
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

_source line 192 · 2026-05-21T18:02:41.470025+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 193 · 2026-05-21T18:02:45.083227+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 194 · 2026-05-21T18:02:46.438897+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (78 个)\n\n- **exp-domain-analysis**: DONE (success) — \n- **exp-ml-classifier-baseline**: DONE (success) — \n- **exp-v1-irt-refit-pilot**: DONE (negative) — \n- **exp-clean-control-delta**: DONE (success) — \n- **exp-fdr-correction**: DONE (success) — \n- **exp-cross-benchmark-analysis**: DONE (success) — \n- **exp-accuracy-zscore-baseline**: DONE (success) — \n- **exp-item-alignment-check**: DONE (negative) — \n- **exp-power-theory**: DONE (success) — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\n- arcc-clean-s10（准备中）\n- arcc-clean-s9（准备中）\n- arcc-clean-s8（准备中）\n- arcc-clean-s7（准备中）\n- exp-ctrl-contam-qwen-clean-s10: Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation（准备中）\n- exp-constat-comparison: ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.（准备中）\n- exp-arcc-clean-s1: ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration（准备中）\n- exp-mia-mink-comparison: MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because R
…[truncated 1160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-21T18:02:46.991492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-21T18:02:47.895574+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\irtfit}{\textsc{IRT-FIT}}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{What Can Binary Response Patterns Reveal About Benchmark Contamination? \\
22	An IRT Person-Fit Characterization}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{sections/abstract}
31	\end{abstract}
32	
33	\input{sections/introduction}
34	\input{sections/related_work}
35	\input{sections/method}
36	\input{sections/results}
37	\input{sections/discussion}
38	\input{sections/conclusion}
39	
40	\input{sections/limitations}
41	
42	\bibliography{references}
43	
44	\appendix
45	\input{sections/appendix}
46	
47	\end{document}
48	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 197 · 2026-05-21T18:02:47.946247+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-21T18:02:48.449702+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-21T18:02:48.600666+00:00_

total 672
drwxr-xr-x  4 ubuntu ubuntu   4096 May 21 17:51 .
drwxr-xr-x 15 ubuntu ubuntu   4096 May 21 17:44 ..
drwxr-xr-x  2 ubuntu ubuntu   4096 May 21 17:52 _pdf_images
-rw-r--r--  1 ubuntu ubuntu  11615 May 20 22:24 acl.sty
-rw-r--r--  1 ubuntu ubuntu  45186 May 20 22:24 acl_natbib.bst
-rw-r--r--  1 ubuntu ubuntu  29547 May 21 17:51 main.aux
-rw-r--r--  1 ubuntu ubuntu  12502 May 21 17:51 main.bbl
-rw-r--r--  1 ubuntu ubuntu   1296 May 21 17:51 main.blg
-rw-r--r--  1 ubuntu ubuntu  20053 May 21 17:51 main.fdb_latexmk
-rw-r--r--  1 ubuntu ubuntu  22667 May 21 17:51 main.fls
-rw-r--r--  1 ubuntu ubuntu  30880 May 21 17:51 main.log
-rw-r--r--  1 ubuntu ubuntu   3055 May 21 17:51 main.out
-rw-r--r--  1 ubuntu ubuntu 442551 May 21 17:51 main.pdf
-rw-r--r--  1 ubuntu ubuntu    925 May 21 16:42 main.tex
-rw-r--r--  1 ubuntu ubuntu  23080 May 21 16:33 references.bib
drwxr-xr-x  2 ubuntu ubuntu   4096 May 21 17:51 sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 200 · 2026-05-21T18:02:54.020789+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

I found some relevant information about EMNLP 2026, though the search results primarily sh
…[truncated 1312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 6074
}
```

</details>

---


### Tool call

_source line 201 · 2026-05-21T18:03:02.400816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline page limit author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline page limit author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-21T18:03:02.903007+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines format requirements"
  }
}
```

</details>

---


### Tool call

_source line 203 · 2026-05-21T18:03:05.313034+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 204 · 2026-05-21T18:03:05.363680+00:00_

abstract.tex
appendix.tex
background.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex
results.tex
sec_ctrl_contam.tex
sec_empirical.tex
sec_setup.tex
sec_simulation.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-21T18:03:09.881789+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline page limit author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Submission FAQs - COLING 2025","url":"https://coling2025.org/faqs/submission/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here's the key information for EMNLP 2026 regarding ARR submissions:

## ARR Submission Deadline
The ARR submission deadline for both long and short papers is May 25, 2026.

## Page Limits
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Author Guidelines

Key submission requirements include:

- All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth")

- The mandatory Limitations section is required, placed after the conclusion

- All authors ar
…[truncated 824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 7480
}
```

</details>

---


### Tool result

_source line 206 · 2026-05-21T18:03:10.032684+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines and format requirements:

## Paper Format Requirements

Paper submissions must use the official ACL style template. More specifically:

- Long papers may have up to eight (8) pages of content plus unlimited pages for references
- Short papers may have up to four (4) pages of content, plus unlimited pages for references
- Paper submissions must us
…[truncated 1039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 7129
}
```

</details>

---


### Tool call

_source line 207 · 2026-05-21T18:03:19.065288+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 208 · 2026-05-21T18:03:19.567666+00:00_

1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first systematic characterization of Item Response Theory (IRT) person-fit statistics for contamination detection, operating at the minimal-information point: binary (correct/incorrect) response patterns from the target model, combined with externally calibrated four-parameter logistic (4PL) item parameters.
3	The core insight is psychometric: a contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using the standardized person-fit statistic $\ell_z^*$ in a difference-in-differences design ($\Delta\ell_z^*$), we identify four IRT-specific behavior boundaries through controlled experiments across three model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B; $n{=}10$ seeds each) on MMLU (14,042 items) and ARC-Challenge (295 items):
5	(1) an inverted-U dose-response where free-$\theta$ estimation attenuates detection at high contamination ($|d|{=}6.58$ at 15\% vs.\ $|d|{=}1.90$ at 50\% for Qwen);
6	(2) model-specific $\theta$-shift dynamics linking baseline ability to detection sensitivity;
7	(3) a detection-diagnosis tradeoff where simpler statistics (accuracy $z$-scores, HT) yield stronger detection ($|d|$ several-fold to over an order of magnitude larger) but lack the diagnostic capabilities of $\ell_z^*$ (seen/unseen decomposition, mechanistic $\theta$-shift insight, sensitivity to response-pattern structure at 57/60 vs.\ 4/60 flagged cells);
8	and (4) a post-RL residual pattern where GRPO erases the accuracy gap but $\ell_z^*$ response-pattern structure persists ($N{=}1$).
9	These findings clarify what binary response patterns can and cannot reveal about contamination, establishing boundary conditions for IRT-based detection.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 209 · 2026-05-21T18:03:19.568103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-21T18:03:20.019998+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus \citep{dodge2021, magar2022}.
9	Membership inference approaches require token-level probabilities \citep{minkprob2024, deng2024}.
10	Probing methods rely on crafted prompts \citep{golchin2024, oren2024}.
11	Performance-based methods require multiple test variants or output logits \citep{constat2024, codec2026}.
12	These methods form a detection frontier ordered by information access.
13	No existing method operates at the bottom of this frontier: binary response patterns alone.
14	
15	The need for minimal-information detection grows more pressing as models evolve.
16	\citet{wang2025fragility} show that all ten log-probability-based methods they evaluate perform at chance level on models trained with reinforcement learning (RL), because RL reshapes internal token distributions while preserving binary correctness patterns.
17	This motivates a fundamental question: \emph{what can binary response patterns reveal about contamination, and under what conditions?}
18	
19	We observe that a contaminated LLM is functionally analogous to a test-taker with item preknowledge: both produce response patterns in which difficult items are answered correctly through memorization rather than genuine ability.
20	This connection points t
…[truncated 3585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 211 · 2026-05-21T18:03:20.020398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-21T18:03:20.974098+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Benchmark contamination detection.}
4	Contamination detection methods span a wide range of information requirements.
5	Corpus-search methods match benchmark items directly against pretraining data \citep{dodge2021, magar2022}, but require full corpus access unavailable for closed models.
6	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training from unseen examples \citep{minkprob2024, deng2024}.
7	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, oren2024}.
8	Performance-based methods compare accuracy on target and reference sets \citep{constat2024, codec2026}, requiring multiple evaluations or in-context learning passes.
9	\citet{sainz2023} argue for systematic per-benchmark contamination measurement, and \citet{jacovi2023} propose mitigation strategies including encrypted benchmarks and canary strings.
10	
11	A critical limitation unites all token-level methods: \citet{wang2025fragility} show that RL post-training renders MIA-based detectors no better than random across 10 methods and 4 benchmarks, because RL reshapes token distributions while largely preserving binary correctness patterns.
12	\citet{selfcritique2026} and \citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.
13	Our approach operates at the minimal information point: binary responses only.
14	
15	\paragraph{IRT for LLM evaluation.}
16	Item Response Theory has seen growing adoption in NLP and ML evaluation.
17	\citet{martinezplumed2019} applied IRT to analyze machine learning classifiers at the instance level, establishing that item difficulty and discrimination parameters capture meaningful variation across models.
18	\citet{lalor2019} proposed estimating IRT parameters from DNN-generated response patterns, removing the need for human annotators.
19	\citet{rodriguez2021} demonstrated that IRT-informed item weighting improves leade
…[truncated 1687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-21T18:03:21.175185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-21T18:03:21.476768+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our MML-EM refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Difference-in-Differences Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, rendering absolute thresholds uninformative.
25	We address this through a difference-in-differences (DiD) design.
26	
27	
…[truncated 1987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 215 · 2026-05-21T18:03:21.477127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-21T18:03:21.930353+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}1.90$ (Qwen at 50\%) to $|d|{=}6.58$ (Qwen at 15\%), with Llama ($|d|{=}2.27$/$2.50$) and Mistral ($|d|{=}2.64$/$3.50$) falling between.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.29$ ($\text{SD}{=}1.45$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.85$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}1.90$--$6.58$) despite order-of-magnitude baseline differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds, bootstrap 95\% CI, 10,000 resamples). All CIs exclude 0.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\begin{tabular}{@{}llrr@{}}
24	\toprule
25	Model & Benchmark & $d$ (15\%) [CI] & $d$ (50\%) [CI] \\
26	\midrule
27	Qwen & MMLU & $-6.58$ [$-15.2$, $-4.5$] & $-1.90$ [$-5.0$, $-1.0$] \\
28	Llama & MMLU & $-2.27$ [$-4.6$, $-1.6$] & $-2.50$ [$-5.0$, $-1.8$] \\
29	Mistral & MMLU & $-2.64$ [$-7.4$, $-1.5$] & $-3.50$ [$-9.6$, $-2.1$] \\
30	Qwen & ARC-C & $+3.16$
…[truncated 14753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-21T18:03:21.930876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-21T18:03:22.433165+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The central question of this work is what binary response patterns can reveal about benchmark contamination.
4	Our findings reveal both the strengths and boundaries of IRT person-fit for this task: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but four boundary conditions constrain its practical utility.
5	
6	\paragraph{Characterization over tool.}
7	The detection-diagnosis tradeoff (\S\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\ell_z^*$.
8	The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.
9	These diagnostic capabilities are invisible to accuracy $z$-scores or HT.
10	
11	\paragraph{Practical implications.}
12	For practitioners, two results have immediate consequences.
13	First, free-$\theta$ estimation can produce misleading dose-response curves; anchoring $\theta$ to a pre-contamination baseline (via cross-benchmark estimation or temporal references) substantially amplifies detection for high-ability models with stable clean baselines, but is unnecessary for lower-ability models where free estimation already captures the full signal.
14	Second, the benchmark size boundary means that $\ell_z^*$ is most informative for large benchmarks ($n > 7{,}000$ items for 80\% power at 15\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects rather than statistical power from item count.
15	
16	\paragraph{Scope and calibra
…[truncated 878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-21T18:03:22.433554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-21T18:03:23.387440+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We presented the first systematic characterization of IRT person-fit behavior for LLM benchmark contamination detection, operating at the minimal-information point of binary response patterns with externally calibrated item parameters.
4	Controlled experiments across three model families ($n{=}10$ seeds each) establish that $\Delta\ell_z^*$ reliably detects SFT-stage contamination (all bootstrap 95\% CIs exclude zero), while revealing four boundary conditions: an inverted-U dose-response under free-$\theta$ estimation, model-specific $\theta$-shift dynamics that modulate detection sensitivity, a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack the diagnostic granularity of full IRT parameterization, and a post-RL residual pattern where accuracy-based detection fails but response-pattern structure persists ($N{=}1$).
5	These findings establish that binary response patterns carry substantially more contamination information than aggregate accuracy (57/60 vs.\ 4/60 flagged cells), but that this information is bounded by model ability, benchmark size, and the estimation strategy for the ability parameter.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-21T18:03:23.538435+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-21T18:03:24.291536+00:00_

1	\section*{Limitations}
2	
3	Our controlled experiments cover three model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B) at the 7--8B scale with QLoRA fine-tuning; validation on larger models, additional architectures, and full-parameter fine-tuning remains future work.
4	The post-RL characterization is $N{=}1$ (Qwen only, GRPO algorithm, 15\% contamination on MMLU); generalization to other model families, RL methods (PPO, DPO), and contamination levels requires further validation.
5	The framework depends on pre-calibrated 4PL item parameters from PSN-IRT, as our MML-EM refit shows that discrimination recovery degrades ($r_a = 0.127$) when calibrating on contaminated leaderboard data; until robust calibration methods emerge, the approach requires externally maintained parameter banks.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-21T18:03:24.442449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-21T18:03:24.693915+00:00_

1	\section{Simulation Validation}
2	\label{app:simulation}
3	
4	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
5	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
6	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
7	
8	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels.
9	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
10	The empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution, achieves $R^2 = 0.957$ against simulated values, with approximate minimum benchmark size of $n \geq 7{,}958$ items for 80\% power at 15\% contamination under MMLU item parameters.
11	
12	\section{4PL vs.\ 3PL Ablation Details}
13	\label{app:4pl_ablation}
14	
15	Table~\ref{tab:4pl_3pl_power} reports detection power (proportion of 2{,}000 simulation replicates rejecting $H_0$ at $\alpha{=}0.05$, two-sided) for 4PL and 3PL parameterizations across five benchmarks and seven contamination levels.
16	The 4PL model yields higher power than 3PL at every non-trivial contamination level on every benchmark.
17	The advantage is largest on MMLU and HellaSwag, where upper-asymptote ($d < 1$) violations are most prevalent, and smallest on ARC-Challenge and HumanEval, where limited item counts constrain power under both parameterizations.
18	
19	Power is non-monotonic at 75\% contamination under 4PL on four of five benchmarks (e.g., MMLU: $.952 \to .938$; GSM8K: $.846 \to .802$).
20	This reflects the $\theta$-shift boundary condition described in \S\ref{sec:inverted_u}: at
…[truncated 8137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-21T18:03:24.694381+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_personfit_contam",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-21T18:03:24.795063+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_personfit_contam'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 227 · 2026-05-21T18:03:33.930224+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-21T18:03:35.837720+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (78 个)\n\n- **exp-domain-analysis**: DONE (success) — \n- **exp-ml-classifier-baseline**: DONE (success) — \n- **exp-v1-irt-refit-pilot**: DONE (negative) — \n- **exp-clean-control-delta**: DONE (success) — \n- **exp-fdr-correction**: DONE (success) — \n- **exp-cross-benchmark-analysis**: DONE (success) — \n- **exp-accuracy-zscore-baseline**: DONE (success) — \n- **exp-item-alignment-check**: DONE (negative) — \n- **exp-power-theory**: DONE (success) — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\n- arcc-clean-s10（准备中）\n- arcc-clean-s9（准备中）\n- arcc-clean-s8（准备中）\n- arcc-clean-s7（准备中）\n- exp-ctrl-contam-qwen-clean-s10: Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation（准备中）\n- exp-constat-comparison: ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.（准备中）\n- exp-arcc-clean-s1: ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration（准备中）\n- exp-mia-mink-comparison: MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because R
…[truncated 1160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1907
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-21T18:03:35.838051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex"
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-21T18:03:36.390470+00:00_

1	\subsection{Controlled Contamination}
2	\label{sec:ctrl_contam}
3	
4	We validate $\ell_z^*$ on MMLU with ground-truth contamination.
5	Three clean seeds yield $\ell_z^*$ values of $s_1{=}9.47$, $s_2{=}7.05$, $s_3{=}9.53$ (mean$\,{=}\,8.68\pm1.41$); $s_2$ is ${\sim}26\%$ lower than $s_1$/$s_3$, attributable to seed-specific training dynamics (Appendix~\ref{app:seed_sensitivity}).
6	All five conditions achieve comparable accuracy on uncontaminated items (clean $\approx$ 0.679), while contaminated models show overall accuracy gains (0.731 at 15\%, 0.764 at 50\%).
7	
8	\paragraph{Finding 1: Detection signal.}
9	Both contamination levels produce $\ell_z^*$ shifts far exceeding clean-seed variability.
10	At 15\% contamination, $|\text{Cohen's}\;d|{=}3.42$; at 50\%, $|d|{=}0.99$ (ddof$\,{=}\,1$, $n{=}3$ clean seeds).
11	The contamination signal ($|\Delta\ell_z^*|{=}4.84$) far exceeds clean-seed variability (SD$\,{=}\,1.41$).
12	
13	\paragraph{Finding 2: Free-$\theta$ non-monotonicity (model-dependent).}
14	Under free-$\theta$ estimation, Qwen dose-response is non-monotonic: $\Delta\ell_z^*{=}{-}4.84$ at 15\% versus ${-}1.40$ at 50\% (ratio 3.46).
15	The 50\% condition produces a \emph{weaker} signal because contamination inflates $\hat{\theta}_{\text{MLE}}$, absorbing part of the aberrance into a higher ability estimate ($\Delta\theta{=}0.29$ at 15\%, $0.47$ at 50\%).
16	This effect is model-dependent: Llama-3.1-8B shows near-monotonic free-$\theta$ dose-response (ratio 1.09) due to lower baseline misfit ($\ell_z^*{=}{-}0.14$ versus Qwen's 8.68).
17	
18	\paragraph{Finding 3: Fixed $\theta$ restores monotonicity.}
19	We anchor at the pre-contamination baseline ($\theta_{\text{fixed}}{=}{-}0.0966$, mean of $n{=}3$ clean $\hat{\theta}$ estimates), which restores monotonic dose-response: $\Delta\ell_{z,\text{fixed}}^*{=}3.17$ (15\%) and $9.89$ (50\%), a ratio of 3.12 (Figure~\ref{fig:ctrl_contam}, right panel).
20	
21	\paragraph{Finding 4: Memorization fingerprint.}
22	A spl
…[truncated 4102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-21T18:03:37.043215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex"
  }
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-21T18:03:37.043610+00:00_

1	\subsection{Empirical Findings}
2	\label{sec:empirical}
3	
4	We apply $\ell_z^*$ to 12 models across five benchmarks (60 model-benchmark cells).
5	After Benjamini--Hochberg FDR correction ($\alpha=0.05$), 57 of 60 cells are flagged as significant.
6	The three unflagged cells (Yi-Lightning$\times$ARC-C, 360GPT2-Pro$\times$HumanEval, Yi-Lightning$\times$HumanEval) all involve small benchmarks ($n \leq 295$), consistent with the power analysis in \S\ref{sec:simulation}.
7	By contrast, a simple accuracy $z$-score baseline (standardized accuracy across models per benchmark) flags only 4 of 60 cells: $\ell_z^*$ captures 14$\times$ more anomalies by exploiting response-pattern structure that accuracy aggregation discards.
8	This near-universal misfit indicates that real LLM response patterns systematically deviate from 4PL IRT predictions, regardless of architecture or training paradigm.
9	
10	\paragraph{12-model case study.}
11	Figure~\ref{fig:heatmap} presents the $\ell_z^*$ heatmap across 12 models and five benchmarks.
12	93.0\% of flagged cells exhibit positive $\ell_z^*$ (over-consistency): models answer too many hard items correctly relative to their estimated ability.
13	Gemini-1.5 on MMLU represents an extreme case: near-perfect accuracy, $\hat{\theta}=0.78$, and $\ell_z^*{=}{+}31.81$, with 50 of 57 MMLU subjects flagged individually.
14	Ward hierarchical clustering on the $\ell_z^*$ profile matrix reveals heterogeneous contamination typologies; Gemini-1.5 isolates as a distinct outlier, while other models form clusters that correspond to selective versus uniform misfit.
15	Ten of 12 models are flagged on all five benchmarks simultaneously.
16	
17	\paragraph{IRT parameter estimation gap.}
18	A 3PL refit via MML-EM on the v1 leaderboard ($N{=}178$ models) recovers difficulty moderately ($r_b = 0.663$) but fails on discrimination ($r_a = 0.127$).
19	Classical IRT calibration requires sample sizes that current leaderboards cannot provide; neural calibration methods 
…[truncated 866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 233 · 2026-05-21T18:03:37.394988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 234 · 2026-05-21T18:03:37.395383+00:00_

1	\subsection{Experimental Setup}
2	\label{sec:setup}
3	
4	We evaluate on five benchmarks that span knowledge, reasoning, and code generation: MMLU \citep{hendrycks2021mmlu} (14,042 items), HellaSwag \citep{zellers2019hellaswag} (10,042), GSM8K \citep{cobbe2021gsm8k} (1,319), ARC-Challenge \citep{clark2018arc} (295), and HumanEval \citep{chen2021humaneval} (164).
5	All item parameters follow the four-parameter logistic (4PL) IRT model, calibrated by \citet{psnirt2026} from a large-scale leaderboard dataset.
6	
7	\paragraph{Empirical data.}
8	We obtain per-item binary response vectors for 12 models from the PSN-IRT v2 leaderboard dataset \citep{psnirt2026}, covering open-weight and proprietary models across capability tiers.
9	PSN-IRT v1 provides binary responses from $N{=}178$ models with 3PL item parameters; v2 supplies validated 4PL parameters for 12 models.
10	We use v2 for empirical analysis and v1 for the MML-EM refit experiment in \S\ref{sec:empirical}.
11	
12	\paragraph{Controlled contamination.}
13	We fine-tune Qwen2.5-7B-Instruct with QLoRA (rank\,=\,16, $\alpha$\,=\,32) under five conditions: three clean runs (seeds 42, 123, 456) and two contaminated runs where 15\% and 50\% of MMLU evaluation items are included in the supervised fine-tuning (SFT) training data.
14	For cross-family validation, we replicate the same protocol on Llama-3.1-8B-Instruct with identical QLoRA configuration and contamination fractions, and further validate on Mistral-7B-Instruct-v0.3 with a single clean seed and two contaminated conditions (15\% and 50\%).
15	
16	\paragraph{Simulation.}
17	For each benchmark, we generate 2{,}000 response-vector replicates per condition across 11 contamination levels (0\%, 3\%, 5\%, 10\%, 15\%, 25\%, 50\%, 60\%, 75\%, 90\%, 100\%), sampling responses under the calibrated 4PL parameters.
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-21T18:03:37.495991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex"
  }
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-21T18:03:37.496397+00:00_

1	\subsection{Simulation Validation}
2	\label{sec:simulation}
3	
4	\paragraph{Null calibration.}
5	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
6	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
7	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
8	
9	\begin{figure}[t]
10	  \centering
11	  \includegraphics[width=\columnwidth]{fig_2_power_function.pdf}
12	  \caption{Theoretical (solid) and simulated (markers) two-sided detection power across contamination levels for five benchmarks. Power scales with $\sqrt{n}$. At contamination above 50\%, mean $\ell_z^*$ crosses zero and shifts from negative to positive anomaly, which produces a brief power dip.}
13	  \label{fig:power}
14	\end{figure}
15	
16	\paragraph{Detection power.}
17	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels (93.6\% at 75\%, 95.2\% at 90\%, 100\% at full contamination).
18	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
19	Figure~\ref{fig:power} overlays theoretical and simulated power curves; the empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution with the \citet{snijders2001} variance formula, achieves $R^2 = 0.65$.
20	This provides approximate guidance for practitioners assessing detection feasibility from a benchmark's item count.
21	
22	\paragraph{Model comparison.}
23	The 4PL model yields a mean $+$27.3pp power gain over 3PL on MMLU, $+$26.1pp on HellaSwag, and $+$20.3pp on GSM8K, as 46\% of MMLU items exhibit upper asymptote $d < 0.95$ (Appendix~\ref{app:4
…[truncated 261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 237 · 2026-05-21T18:03:38.249544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 238 · 2026-05-21T18:03:39.153220+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\input{sections/sec_setup}
5	\input{sections/sec_simulation}
6	\input{sections/sec_ctrl_contam}
7	\input{sections/sec_empirical}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 239 · 2026-05-21T18:03:39.705492+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 240 · 2026-05-21T18:03:40.007079+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 241 · 2026-05-21T18:03:40.057737+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
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

_source line 242 · 2026-05-21T18:03:40.108507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 243 · 2026-05-21T18:03:46.532494+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/ -name \"config.yaml\" -o -name \"*.yaml\" | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/ -name \"config.yaml\" -o -name \"*.yaml\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 244 · 2026-05-21T18:03:46.984523+00:00_

find: ‘/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/’: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 245 · 2026-05-21T18:03:47.486843+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-21T18:03:48.390611+00:00_

## Review Issue Tracker — Round 1 (updated after v6 report + Reviewer synthesis)

# ===== ACTIONABLE ISSUES (applies to actual paper) =====

- id: "ACTUAL-C-W1"
  summary: "HT ≈ lz* in ALL conditions — 4PL IRT framework unnecessary (degradation chain)"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  applies_to: actual-c
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "HT (1 param) matches lz* (4 params), |d_HT - d_lz*|<0.3. Completes degradation chain 4PL→HT→z-score."
  action_items:
    - round: 1
      action: "Reframe: degradation chain as one finding. Core = 'characterizing boundary conditions of IRT person-fit'. lz* value = diagnostic granularity (seen/unseen) + mechanistic understanding (θ-shift) + real-world specificity. Two-track: stable content now, intro/abstract after GRPO v3."
      assigned_to: director+paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "ACTUAL-B-W1"
  summary: "n=3 seeds statistically insufficient — must ≥10 + CI"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  applies_to: actual-b
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "Qwen n=10 done. Llama n=7→10 in progress. Mistral n=3 must expand. ARC-C n=10 done."
  action_items:
    - round: 1
      action: "Expand all to n=10. Bootstrap 95% CI for all Cohen's d."
      assigned_to: main_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "BEST-W1"
  summary: "0 figures, 14+ tables, 14 references — presentation unacceptable"
  category: writing
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  applies_to: all
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "Need 3-4 figures, ≥25 references, independent Related Work section."
  action_items:
    - round: 1
      action: "4 figures: (a) θ-shift × accuracy scatter, (b
…[truncated 8298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-21T18:03:48.491464+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ -name \"config.yaml\" -type f 2>/dev/null",
  "description": "Find all config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ -name \"config.yaml\" -type f 2>/dev/null",
    "description": "Find all config files in project"
  }
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-21T18:03:48.692589+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 249 · 2026-05-21T18:03:57.375463+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -path \"*/irt_personfit_contam*config*\" -type f 2>/dev/null | head -10",
  "description": "Find project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -path \"*/irt_personfit_contam*config*\" -type f 2>/dev/null | head -10",
    "description": "Find project config"
  }
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-21T18:03:58.881428+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/logs/workers/worker_code_s6-config-audit-eval_20260521T071535.log
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/bin/numpy-config
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/torchgen/static_runtime/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/torchgen/static_runtime/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/pyro/poutine/__pycache__/infer_config_messenger.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/pyro/poutine/infer_config_messenger.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/httpx/__pycache__/_config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/httpx/_config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 1505
}
```

</details>

---


### Tool call

_source line 251 · 2026-05-21T18:03:58.982631+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/projects/irt_personfit_contam.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/config.yaml 2>/dev/null || echo \"CONFIG_NOT_FOUND\"",
  "description": "Read project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/projects/irt_personfit_contam.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/config.yaml 2>/dev/null || echo \"CONFIG_NOT_FOUND\"",
    "description": "Read project config"
  }
}
```

</details>

---


### Tool result

_source line 252 · 2026-05-21T18:03:59.033307+00:00_

execution:
  gpu_ids:
  - cuda:0
  servers:
  - account: root
    server: westd-35694
feishu:
  chat_id: oc_9840a7d708128f2f1d02985bd9b8d901
  operational_chat_id: oc_cd8526cc08af148dd16c48b7739cca92
  review_mode: fresh
  review_paper_path: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex
  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf
  review_round: 1
  review_supplementary_paths: ''
  submission_chat_id: oc_6c76a266d9f5997de21a1604bc79c209
project:
  created_at: '2026-05-20T07:09:30.656Z'
  description: 'IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination
    Detectors for LLMs'
  name: irt_personfit_contam
  phase: research
  source_idea_id: idea_033
venue: emnlp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-21T18:04:22.374957+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_personfit_contam",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_personfit_contam",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-21T18:04:45.670094+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23295
}
```

</details>

---


### Tool call

_source line 255 · 2026-05-21T18:04:45.922644+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **类型**: Long Paper\n- **页数限制**: 正文严格 8 页，参考文献不限页。Limitations 章节必须有（不算页数）。\n- **模板**: ACL style (`acl.sty`)\n- **匿名规则**: Double-blind（禁止作者信息、自引暴露身份、可追踪下载链接）\n- **Responsible NLP Checklist**: 在 OpenReview submission form 中填写，不在论文 PDF 中\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf`\n- 各节在 `sections/` 子目录\n\n## 审查侧重\n\n请从以下维度严格评审：\n\n### 1. IRT 框架合理性\n- 4PL 模型用于 LLM 的理论合理性——LLM 是否满足 IRT 的基本假设（局部独立性、单维性）？违反这些假设对 ℓz* 的影响有多大？\n- PSN-IRT 外部参数的依赖——如果 PSN-IRT 参数本身有偏差，整个框架的鲁棒性如何？\n- Δℓz* difference-in-differences 设计是否真正解决了模型系统性违反 IRT 假设的问题？\n- ℓz* 的 Snijders 校正在 LLM 上下文中是否仍然有效？\n\n### 2. 实验控制与统计推断\n- n=10 seeds 的样本量是否足够？bootstrap CI 的可靠性？\n- QLoRA SFT 作为唯一的 contamination mechanism 是否太窄？\n- 15% 和 50% 两个 contamination level 是否足以支撑 dose-response 结论？\n- Mistral n=6 seeds（而非 n=10）是否应标注为 limitation？\n- Post-RL 实验 N=1 的统计意义和泛化性？\n- Cohen's d 的 bootstrap CI 有些非常宽（如 Qwen 15%: [-15.2, -4.5]），这对结论的可信度有什么影响？\n\n### 3. 可重现性\n- 是否提供了足够的实验细节（超参数、训练数据构造、评估流程）？\n- 4PL 参数来源是否可公开获取？\n- 代码/数据可用性声明？\n\n### 4. 与现有方法的对比\n- 与 ConStat、MIA (Min-K%)、CoDec 等方法的对比是否公平？\n- detection-diagnosis tradeoff 的论证是否convincing——accuracy z-score |d|=68.7 vs ℓz* |d|=1.90，如何证明后者有价值？\n- 57/60 vs 4/60 flagging rate 的比较是否恰当（一个是 person-fit misfit，一个是 detection）？\n\n请按 ARR 标准给出：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：1-5 分）+ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **类型**: Long Paper\n- **页数限制**: 正文严格 8 页，参考文献不限页。Limitations 章节必须有（不算页数）。\n- **模板**: ACL style (`acl.sty`)\n- **匿名规则**: Double-blind（禁止作者信息、自引暴露身份、可追踪下载链接）\n- **Responsible NLP Checklist**: 在 OpenReview submission form 中填写，不在论文 PDF 中\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf`\n- 各节在 `sections/` 子目录\n\n## 审查侧重\n\n请从以下维度严格评审：\n\n### 1. IRT 框架合理性\n- 4PL 模型用于 LLM 的理论合理性——LLM 是否满足 IRT 的基本假设（局部独立性、单维性）？违反这些假设对 ℓz* 的影响有多大？\n- PSN-IRT 外部参数的依赖——如果 PSN-IRT 参数本身有偏差，整个框架的鲁棒性如何？\n- Δℓz* difference-in-differences 设计是否真正解决了模型系统性违反 IRT 假设的问题？\n- ℓz* 的 Snijders 校正在 LLM 上下文中是否仍然有效？\n\n### 2. 实验控制与统计推断\n- n=10 seeds 的样本量是否足够？bootstrap CI 的可靠性？\n- QLoRA SFT 作为唯一的 contamination mechanism 是否太窄？\n- 15% 和 50% 两个 contamination level 是否足以支撑 dose-response 结论？\n- Mistral n=6 seeds（而非 n=10）是否应标注为 limitation？\n- Post-RL 实验 N=1 的统计意义和泛化性？\n- Cohen's d 的 bootstrap CI 有些非常宽（如 Qwen 15%: [-15.2, -4.5]），这对结论的可信度有什么影响？\n\n### 3. 可重现性\n- 是否提供了足够的实验细节（超参数、训练数据构造、评估流程）？\n- 4PL 参数来源是否可公开获取？\n- 代码/数据可用性声明？\n\n### 4. 与现有方法的对比\n- 与 ConStat、MIA (Min-K%)、CoDec 等方法的对比是否公平？\n- detection-diagnosis tradeoff 的论证是否convincing——accuracy z-score |d|=68.7 vs ℓz* |d|=1.90，如何证明后者有价值？\n- 57/60 vs 4/60 flagging rate 的比较是否恰当（一个是 person-fit misfit，一个是 detection）？\n\n请按 ARR 标准给出：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：1-5 分）+ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 256 · 2026-05-21T18:05:07.974272+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22051
}
```

</details>

---


### Tool call

_source line 257 · 2026-05-21T18:05:08.175385+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作格式**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **类型**: Long Paper\n- **页数限制**: 正文严格 8 页，参考文献不限页。Limitations 章节必须有（不算页数）。\n- **模板**: ACL style (`acl.sty`)\n- **匿名规则**: Double-blind（禁止作者信息、自引暴露身份、可追踪下载链接）\n- **Responsible NLP Checklist**: 在 OpenReview submission form 中填写，不在论文 PDF 中\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf`\n- 各节在 `sections/` 子目录\n\n## 审查侧重\n\n请从以下维度严格评审：\n\n### 1. 新颖性与贡献定位\n- \"首次将 person-fit 统计量应用于 LLM benchmark contamination\"——这个 claim 是否准确？是否有遗漏的相关工作？\n- 四个 findings（inverted-U、θ-shift dynamics、detection-diagnosis tradeoff、post-RL residual）中，哪些是真正的新贡献，哪些是 IRT 文献中已知的现象在新领域的简单移植？\n- \"characterization paper\" 的定位是否足以支撑 EMNLP 主会议？ARR 评分标准中 3.0 = Findings，4.0 = Conference——这篇论文达到哪个水平？\n- 与 ConStat (NeurIPS 2024)、Wang et al. (2025) fragility 论文的差异化是否清晰？\n\n### 2. Related Work 覆盖\n- IRT for NLP 方面是否遗漏重要工作？（如 Lalor et al. 2019, Rodriguez et al. 2021, Polo et al. 2024, Atlas 2025 等）\n- 污染检测方面是否遗漏：Oren et al. 2024, Deng et al. 2024, Golchin & Surdeanu 2024？\n- Person-fit 文献是否覆盖充分？Karabatsos (2003), Meijer & Sijtsma (2001), Van der Flier (1982)?\n- 引用总数是否达到顶会标准（通常 30-40 篇）？当前有多少篇？\n\n### 3. 叙事结构与清晰度\n- Abstract 是否准确反映论文的实际贡献？是否过度 claim？\n- Introduction 的逻辑链是否连贯：问题定义→现有方法不足→psychometric analogy→本文方法→findings？\n- Results 各 subsection 之间的逻辑关系是否清晰？\n- Discussion 是否与 Results 重复太多？\n- Limitations 是否充分覆盖主要弱点？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？（检查 PDF 页数）\n- 使用的是否是正确的 ACL review 模板？\n- 匿名性是否保持？（检查是否有 \"Anonymous\" 作者、无自引泄露）\n- Figure/Table 编号和引用是否一致？\n- 参考文献格式是否符合 ACL natbib 规范？\n\n### 5. 写作质量\n- 是否存在 AI 生成痕迹（过度使用 \"novel\"/\"comprehensive\"/\"significant\" 等）？\n- 技术术语是否一致（如 ℓz* 的符号是否始终一致）？\n- 图表质量——Figure 1 的示意图是否有效传达核心 insight？\n- 表格是否过多/过密？是否有可以合并或移至附录的？\n\n请按 ARR 标准给出：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：1-5 分）+ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作格式**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **类型**: Long Paper\n- **页数限制**: 正文严格 8 页，参考文献不限页。Limitations 章节必须有（不算页数）。\n- **模板**: ACL style (`acl.sty`)\n- **匿名规则**: Double-blind（禁止作者信息、自引暴露身份、可追踪下载链接）\n- **Responsible NLP Checklist**: 在 OpenReview submission form 中填写，不在论文 PDF 中\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf`\n- 各节在 `sections/` 子目录\n\n## 审查侧重\n\n请从以下维度严格评审：\n\n### 1. 新颖性与贡献定位\n- \"首次将 person-fit 统计量应用于 LLM benchmark contamination\"——这个 claim 是否准确？是否有遗漏的相关工作？\n- 四个 findings（inverted-U、θ-shift dynamics、detection-diagnosis tradeoff、post-RL residual）中，哪些是真正的新贡献，哪些是 IRT 文献中已知的现象在新领域的简单移植？\n- \"characterization paper\" 的定位是否足以支撑 EMNLP 主会议？ARR 评分标准中 3.0 = Findings，4.0 = Conference——这篇论文达到哪个水平？\n- 与 ConStat (NeurIPS 2024)、Wang et al. (2025) fragility 论文的差异化是否清晰？\n\n### 2. Related Work 覆盖\n- IRT for NLP 方面是否遗漏重要工作？（如 Lalor et al. 2019, Rodriguez et al. 2021, Polo et al. 2024, Atlas 2025 等）\n- 污染检测方面是否遗漏：Oren et al. 2024, Deng et al. 2024, Golchin & Surdeanu 2024？\n- Person-fit 文献是否覆盖充分？Karabatsos (2003), Meijer & Sijtsma (2001), Van der Flier (1982)?\n- 引用总数是否达到顶会标准（通常 30-40 篇）？当前有多少篇？\n\n### 3. 叙事结构与清晰度\n- Abstract 是否准确反映论文的实际贡献？是否过度 claim？\n- Introduction 的逻辑链是否连贯：问题定义→现有方法不足→psychometric analogy→本文方法→findings？\n- Results 各 subsection 之间的逻辑关系是否清晰？\n- Discussion 是否与 Results 重复太多？\n- Limitations 是否充分覆盖主要弱点？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？（检查 PDF 页数）\n- 使用的是否是正确的 ACL review 模板？\n- 匿名性是否保持？（检查是否有 \"Anonymous\" 作者、无自引泄露）\n- Figure/Table 编号和引用是否一致？\n- 参考文献格式是否符合 ACL natbib 规范？\n\n### 5. 写作质量\n- 是否存在 AI 生成痕迹（过度使用 \"novel\"/\"comprehensive\"/\"significant\" 等）？\n- 技术术语是否一致（如 ℓz* 的符号是否始终一致）？\n- 图表质量——Figure 1 的示意图是否有效传达核心 insight？\n- 表格是否过多/过密？是否有可以合并或移至附录的？\n\n请按 ARR 标准给出：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：1-5 分）+ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 258 · 2026-05-21T18:05:09.588513+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1413
}
```

</details>

---


### Assistant

_source line 259 · 2026-05-21T18:05:22.718598+00:00_

已并行派发：

1. **视觉审查 Agent** — 已启动（fire-and-forget，不阻塞）
2. **Reviewer 1**（方法严谨性 + 实验设计）— 已分配
3. **Reviewer 2**（新颖性 + 完整性 + 写作格式）— 已分配

等待两名 Reviewer 返回 Round 1 初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 260 · 2026-05-21T18:10:58.243978+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：新颖性 + 完整性 + 写作格式

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 将 IRT person-fit 统计量引入 LLM 污染检测是一个有趣且新颖的概念桥接，但四个 findings 中多数可从 IRT 理论直接预测，生态效度存疑（fine-tuning ≠ pretraining 污染），且 post-RL 结论仅基于 N=1 模型，距离主会议接收标准有差距。

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 方法论合理，主要 claims 有实验支撑，但生态效度和模型覆盖范围存在明显不足 |
| Excitement | 3/5 | Person-fit → contamination 的概念桥接有吸引力，但 findings 多为 IRT 领域已知现象在新场景的验证 |
| Reproducibility | 4/5 | 实验设置清晰（QLoRA rank=16, α=32, 10 seeds），使用公开 benchmark，PSN-IRT 参数可获取 |
| Confidence | 4/5 | 熟悉 IRT 和 NLP evaluation 文献，仔细阅读了全文和附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 生态效度不足——QLoRA fine-tuning 模拟污染 ≠ 真实 pretraining 污染

- 具体位置：Section 3.3, Limitations (p8)
- 问题：论文用 QLoRA (rank=16, α=32) 在 15%/50% 数据上 fine-tuning 模拟污染。真实污染发生在 pretraining 阶段，权重影响遍及整个网络，而 LoRA 微调只修改低秩适配器。这两种机制产生的 response pattern 可能有本质差异——fine-tuning 污染更接近"item preknowledge"（教育测试中的作弊），而 pretraining 污染可能更接近"over-exposure"。论文在 Limitations 中承认了这一点（"fine-tuning remains future work"），但这不是一个小问题——它直接影响所有四个 findings 的外推有效性。
- 为什么影响接收：如果 fine-tuning 和 pretraining 产生不同的 aberrance pattern，则本文的 boundary conditions 可能不适用于真实场景，核心贡献大幅缩水。
- 建议修改方向：(1) 使用已知被污染的真实模型（如 Open LLM Leaderboard 上被标记的模型）进行验证；(2) 至少在 Discussion 中提供理论论证，解释为何 fine-tuning 污染的 response pattern 应当近似 pretraining 污染；(3) 或者将论文定位明确收窄为 "SFT-stage contamination characterization"。

**N2** [critical] Post-RL finding (Section 4.5) 严重 under-validated：N=1 模型、单一 benchmark、单一 RL 算法

- 具体位置：Section 4.5 (p7), Figure 4
- 问题：Post-RL residual pattern 是论文最具新颖性的 finding（也是 abstract 中的重点 claim），但仅在 Qwen-2.5-7B + 15% MMLU 污染 + GRPO 算法上验证。N=1 模型、单一污染水平、单一 RL 方法（无 DPO/PPO 对比），结论的稳健性完全未知。Section 4.5 最后一段承认 "We report this as a preliminary characterization"，但 abstract 将其列为四大 findings 之一，没有标注 preliminary。
- 为什么影响接收：作为 abstract 的核心 claim 之一，支撑证据严重不足。单一实验点无法建立任何 "pattern"。
- 建议修改方向：(1) 至少在 Llama 和 Mistral 上重复 GRPO 实验；(2) 或在 abstract/conclusion 中明确降级为 "preliminary observation"；(3) 加入 DPO 对比以验证 RL 算法类型的影响。

**N3** [critical] 核心 findings 中多数可从 IRT 理论直接推导，新颖贡献被高估

- 具体位置：Section 4.2 (Inverted-U), Section 4.3 (θ-shift), Section 4.4 (Detection-diagnosis tradeoff)
- 问题：
  - **Inverted-U dose-response** (Section 4.2)：当污染率极高时，模型在绝大多数 item 上都正确，ℓz* 的方差必然减小——这是 IRT 的天花板效应，person-fit 文献中已知（St-Onge et al., 2011 已在 bib 中但未 cite，讨论了 aberrance rate 对 person-fit accuracy 的影响）。
  - **θ-shift dynamics** (Section 4.3)：能力参数与 person-fit 灵敏度的交互是 person-fit 文献的经典议题（Meijer & Sijtsma, 2001 的 methodology review 明确讨论了 ability level 对 person-fit detection 的影响）。
  - **Detection-diagnosis tradeoff** (Section 4.4)：简单统计量（z-score）比复杂统计量（ℓz*）在纯检测上更强，但缺乏诊断能力——这是统计学中 power vs. specificity 的基本 tradeoff。
- 为什么影响接收：如果四个 findings 中有三个是已知理论在新域的直接验证（而非新发现），则论文的 novelty 贡献低于 abstract 所宣称的。
- 建议修改方向：(1) 对每个 finding 明确区分 "theoretical expectation" vs. "empirical surprise"；(2) 强调真正新颖的部分（如 θ-shift 的具体量化、4PL upper asymptote 在 LLM 中的作用）；(3) 重新校准 abstract 和 introduction 的 claim 强度。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 模型覆盖范围过窄

- 具体位置：Section 3.3 (p4)
- 问题：仅覆盖 3 个 7-8B 模型族。缺少更大模型（13B/70B）、不同架构（Mixture-of-Experts 如 Mixtral）或不同训练范式（instruction-tuned vs. base）的实验。Section 4.3 的 θ-shift dynamics 声称与 baseline ability 相关，但只有 3 个数据点（Qwen 52.4%, Llama 59.3%, Mistral 67.8% on MMLU），无法确定这一关系是线性还是其他形式。
- 建议：至少增加 1-2 个不同规模/架构的模型，或在 Limitations 中明确承认 generalization 未验证。

**W2** [warning] Item-level detection 接近随机（Table 8, Appendix）

- 具体位置：Table 8 (p12)
- 问题：AUROC 最高 0.63 (RF cross-model)，ℓz* itemwise 仅 0.53（接近随机 0.50）。这严重限制了方法的实际应用价值。论文在 Discussion (p7) 提到 "the value of ℓz* lies in three capabilities that IRT z-scores lack"，但如果 item-level 检测几乎无效，practical utility 大打折扣。
- 建议：(1) 在 main text（非 appendix）中坦诚讨论 item-level 检测的局限；(2) 明确 person-fit 的价值定位是 model-level characterization 而非 item-level detection。

**W3** [warning] Δℓz* 差异设计（Section 3.2）的假设未充分验证

- 具体位置：Section 3.2 (p3-4)
- 问题：Δℓz* = ℓz*_contam - ℓz*_clean 的核心假设是 "shared model misfit cancels"。但这要求 contamination 和 clean 模型共享相同的 systematic misfit structure。对于 fine-tuning 污染这或许成立（共享相同 base model），但论文声称方法适用于 cross-benchmark comparison（没有 clean baseline 的场景），此时 Δℓz* 不可计算，方法的部署场景不清晰。
- 建议：明确讨论在没有 clean baseline 时的部署路径。

**W4** [warning] Figure 2 heatmap 可读性差

- 具体位置：Figure 2 (p5)
- 问题：6×4 heatmap 中灰色 cell 表示 "missing conditions"（Llama 和 Mistral 的 ARC-C 未包含），但没有解释为什么这些条件缺失。色彩映射的 intensity 在打印/灰度下可能难以区分。Cohen's d 的绝对值范围从 1.08 到 15.3，跨度极大，线性色彩映射导致中间值难以辨别。
- 建议：(1) 解释为什么部分条件缺失；(2) 考虑对数色彩映射或分段 colorbar。

---

## 小问题（不影响接收）

- **Orphan bibliography entries**: bib 文件有 59 条，实际 cite 仅 31 条，28 条 orphan。虽然不影响 PDF 输出，但说明 bibliography 管理不够严谨。
- **符号一致性**: ℓz* 在正文中使用一致，但 Section 3.1 首次引入时公式编号缺失（定义在文本中而非独立公式）。Person-fit statistic 的标准化公式应给出完整 reference。
- **"first systematic characterization" claim (Abstract)**: 虽然可能技术上准确（无人在 LLM contamination 上系统使用 person-fit），但 ConStat (NeurIPS 2024) 也是 performance-based contamination detection，且 Sinharay (2017) 已将 person-fit 用于 item preknowledge 检测。建议加限定词（如 "first in the LLM evaluation context"）。
- **Table 1 (p4)**: 只报告 Cohen's d 和 95% CI，但缺少原始 ℓz* 均值和标准差，不利于其他研究者复现和比较。
- **Appendix 过于简略**: Table 4 (detection power) 和 Table 5 (seed sensitivity) 值得在 main text 中至少简要提及。

---

## Missing References

Director 指定检查的所有关键引用均已覆盖：
- ✅ Lalor et al. 2019, Rodriguez et al. 2021, Polo et al. 2024, Atlas 2025（IRT for NLP）
- ✅ Oren et al. 2024, Deng et al. 2024, Golchin & Surdeanu 2024（污染检测）
- ✅ Karabatsos 2003, Meijer & Sijtsma 2001, Van der Flier 1982（Person-fit）
- ✅ ConStat 2024, Wang et al. 2025 fragility

**可能遗漏的工作**:
- Tendeiro & Meijer (2014) — 在 bib 中但未 cite（orphan），讨论了非参数 person-fit 统计量的有效性，与本文 detection-diagnosis tradeoff 直接相关。
- St-Onge et al. (2011) — 在 bib 中但未 cite（orphan），研究 aberrance rate 对 person-fit accuracy 的影响，与 inverted-U finding 直接相关。
- 引用总数 31 篇（实际 cite），处于顶会标准的下限（通常 30-40 篇）。考虑到有 28 条 orphan bib entry，作者可能删引用时过度裁剪了。

---

## 主要优势

1. **概念创新**：将 psychometric person-fit 统计量引入 LLM contamination detection 是一个有价值的跨领域桥接，minimal information requirement（仅需二值 response pattern）使其适用于 black-box 场景。
2. **实验设计规范**：controlled contamination 实验设计清晰（QLoRA, 10 seeds, bootstrap CI），Cohen's d 作为 effect-size 指标选择恰当。
3. **诚实的自我定位**：论文以 "characterization" 而非 "detection method" 自居，Discussion 和 Limitations 坦诚讨论了主要局限。
4. **Post-RL finding 有启发性**：虽然证据不足以支撑 robust conclusion，但 GRPO 擦除 accuracy gap 而保留 response-pattern structure 的现象本身是一个值得深入研究的方向。
5. **与 existing methods 的桥接清晰**：Section 4.4 的 detection-diagnosis tradeoff 很好地定位了 person-fit 在 contamination detection 工具链中的位置（诊断而非纯检测）。

---

## 总结判断

这是一篇执行质量不错的 characterization paper，核心想法（person-fit → contamination）具有新颖性。但三个关键问题限制了其贡献：(1) 生态效度不足（fine-tuning ≠ pretraining）；(2) 四个 findings 中三个可从理论预测，novelty 被高估；(3) 最具新颖性的 post-RL finding 严重 under-validated。论文适合 Findings track（3.0），但距离主会议接收（4.0）有明显差距。若能补充真实污染验证 + post-RL multi-model 实验 + 调整 claim 强度，可在下一周期冲击更高评分。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 261 · 2026-05-21T18:11:06.164638+00:00_

Reviewer 2 的审稿意见已收到。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 262 · 2026-05-21T18:11:20.658715+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**评分**: Overall 3.0 (Findings)，Soundness 3/5，Excitement 3/5，Confidence 4/5。

**三个 Must-Fix 问题**：
1. 生态效度不足——QLoRA fine-tuning 模拟的污染 ≠ 真实 pretraining 污染，所有 findings 的外推有效性存疑
2. Post-RL finding（最具新颖性的贡献）仅基于 N=1 模型 + 单一 RL 算法，证据严重不足
3. 四个 findings 中三个可从 IRT 理论直接预测（inverted-U 是天花板效应、θ-shift 是经典议题、detection-diagnosis tradeoff 是 power vs. specificity），novelty 被高估

**核心判断**：概念桥接（person-fit → contamination）有价值，但执行范围太窄、claim 过度，适合 Findings track，距主会议有差距。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 263 · 2026-05-21T18:11:27.031892+00:00_

Reviewer 2 的报告已收到。等待 Reviewer 1 的报告后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 30

## Round 30

6 recorded events


### User

_source line 264 · 2026-05-21T18:13:56.452447+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

### Paper Summary

本文首次系统地将 IRT person-fit 统计量（ℓz*）应用于 LLM benchmark contamination 检测。方法核心是：使用 PSN-IRT 预校准的 4PL 项目参数计算标准化 person-fit 残差 ℓz*，并通过 Δℓz*（差分设计）消除 LLM 系统性违反 IRT 假设的影响。在三个 7-8B 模型家族（Qwen-2.5-7B, Llama-3.1-8B, Mistral-7B）上以 QLoRA SFT 构造 15% 和 50% 两个污染水平，在 MMLU 和 ARC-Challenge 上进行受控实验，识别出四个边界条件：(1) free-θ 下的倒 U 型剂量反应，(2) 模型特异性 θ-shift 动态，(3) detection-diagnosis tradeoff，(4) post-RL 残留模式。

---

## 总体评分

**Overall Assessment**: 3.0（Findings——可被 Findings 接收）

**Confidence**: 4/5（对 IRT 方法论和 LLM 评估均有较好理解，仔细阅读了全文及附录）

**一句话总结**: 跨学科视角新颖、受控实验设计合理，但 IRT 假设违反的分析不充分、污染机制单一、post-RL 发现统计效力不足，实用价值受限于倒 U 型问题和对外部参数校准的依赖。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法有理论基础但 IRT 假设违反分析不足；Δℓz* 差分设计仅消除加性共享误拟合，未分析污染是否改变项目依赖结构；Post-RL N=1 无统计推断 |
| Excitement | 3.5/5 | 将心理测量学 person-fit 引入 LLM 污染检测是genuinely novel的视角；θ-shift 机制和 scoremeness 分解有解释性深度；但实用性受限 |
| Reproducibility | 3/5 | 依赖外部 PSN-IRT 参数（Zhuo et al., 2026）；QLoRA 训练细节基本充足但缺少部分关键超参；无代码/数据可用性声明 |

---

## 主要优势

1. **跨学科新颖性**：将教育测量学中成熟的 person-fit 统计量（ℓz*，有40年理论积累）迁移到 LLM 评估领域，这一视角是genuinely novel的。与现有方法（MIA, n-gram overlap, token-level probing）相比，IRT person-fit 在理论层面有根本性区别——它基于"响应模式异常"而非"信息泄露痕迹"。

2. **Δℓz* 差分设计**（Section 3.2）：认识到 LLM 系统性违反 IRT 假设（57/60 cells yield ℓz* > 1.96 even absent contamination），并提出差分设计来隔离污染特异性信号，这是方法论上合理且务实的处理。

3. **受控实验设计**：n=10 seeds × 3 model families × 2 benchmarks × 3 conditions 的设计相对系统，bootstrap 95% CI（10,000 resamples）提供了统计推断基础。Table 1 所有 CI 不包含零是一个有意义的结果。

4. **θ-shift 机制分析**（Section 4.3, Figure 3）：揭示了 baseline accuracy 与检测灵敏度之间的负相关（在 MMLU 上），提供了可解释的机制理解——高能力模型的 θ-shift headroom 小，导致 free-θ 重估吸收了污染信号。这个发现对理解 person-fit 统计量在 LLM 上的行为边界有理论价值。

5. **Detection-diagnosis tradeoff 的坦诚报告**（Section 4.4, Table 3）：作者没有回避 ℓz* 在纯检测任务上远弱于简单统计量（|d|≈0.58-1.90 vs accuracy |d|≈42-68）的事实，而是重新定位 ℓz* 的价值在于诊断功能。这种诚实的报告方式是值得肯定的。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] IRT 假设违反的分析不充分，Δℓz* 有效性缺乏理论保证

- **具体位置**：Section 3.2, Appendix A
- **问题**：论文承认 LLM 响应"systematically violate IRT assumptions of local independence and unidimensionality"（Section 3.2），并提出 Δℓz* 差分设计作为解决方案。但差分设计仅在以下条件下有效：clean 和 contaminated conditions 下的 IRT 模型误拟合（model misfit）是 **加性且等量的**。论文未分析一个关键问题：**污染是否改变了项目间的依赖结构？** 如果被记忆的题目变得独立于潜在能力 θ（答对纯靠记忆而非推理），而未被记忆的题目保持原有依赖模式，那么 contaminated condition 下的 misfit 结构与 clean condition 不同，Δℓz* 不再是有效的差分估计量。Appendix A 的模拟验证（R²=0.957）似乎假设了 IRT 模型成立，这构成循环论证——模拟结果无法回答"当模型系统性失效时统计量是否仍有效"。
- **为什么影响接收**：这是方法论的根基问题。如果 Δℓz* 的有效性未被充分论证，所有基于它的实验结论都缺乏可靠的统计基础。
- **建议修改方向**：(a) 提供模拟分析，明确引入 local dependence 结构的变化（如 testlet 效应）后 Δℓz* 的偏差和检验力变化；(b) 在真实实验数据上检验 clean 和 contaminated conditions 下的项目残差相关矩阵是否存在系统性差异；(c) 讨论 Snijders (2001) 校正在 IRT 假设违反下的鲁棒性——文献中有相关研究（如 St-Onge et al., 2011，已在 .bib 中但未引用）。

**N2** [critical] 倒 U 型剂量反应（inverted-U）削弱了方法的实用性主张

- **具体位置**：Section 4.2, Figure 2, Table 1
- **问题**：在 MMLU 上 free-θ 估计下，Qwen 的 |d| 从 15% 污染的 6.56 **下降**到 50% 污染的 1.90（Table 1）。这意味着在大型基准测试上，**污染越严重，检测灵敏度越低**——恰恰在最需要检测的场景下方法失效。论文将此归因于 θ-shift absorption（Section 4.3），并提出 fixed-θ anchoring 作为解决方案。但 fixed-θ 需要"pre-contamination reference or cross-benchmark ability estimation"（Section 4.2 文本），即需要 clean baselines——这与 Abstract 和 Introduction 中"operating at the minimal-information point: binary response patterns"的定位相矛盾。论文标题和摘要暗示该方法只需二值响应模式即可工作，但实际上最可靠的模式（fixed-θ）需要额外的参考信息。
- **为什么影响接收**：方法的宣传定位（"minimal information point"）与实际限制（需要 clean baselines）之间存在显著落差，影响读者对方法实用性的判断。
- **建议修改方向**：(a) 在 Abstract/Introduction 中明确区分 free-θ 和 fixed-θ 两种工作模式及其各自要求；(b) 将倒 U 型问题从"finding"提升为"fundamental limitation"在 Limitations 中讨论；(c) 提供关于 fixed-θ estimation 的更多细节——cross-benchmark ability estimation 在实际部署中的可行性如何？

**N3** [critical] Post-RL 发现（Finding 4）统计效力严重不足

- **具体位置**：Section 4.5, Figure 4
- **问题**：Post-RL 实验仅有 N=1（一个模型 Qwen、一个污染水平 15%、一个 RL 方法 GRPO、一个 benchmark MMLU）。Figure 4 展示的训练轨迹没有误差条或置信区间。论文声称"GRPO erases the accuracy gap between seen and unseen items"且"the response-pattern gap persists (ℓz* →2.1pp)"——但这些数字来自**单次实验**，没有任何重复验证。然而这个发现被置于 Abstract 的第四个主要贡献、Section 1 Introduction 的第四个 bullet point，以及 Section 5 Discussion 中。一个 N=1 的观察被提升到与其他经过 n=10 seeds 验证的发现同等地位，不符合学术写作的证据层级。
- **为什么影响接收**：将本质上是 anecdotal evidence 的观察包装为 main contribution，有 overclaiming 的风险。如果后续无法复现（不同 RL 方法、不同模型可能表现不同），会损害论文整体可信度。
- **建议修改方向**：(a) 降级为"preliminary observation"或"case study"，在 Abstract 和 Introduction 中相应调整措辞；(b) 增加至少 2-3 个 RL seeds 的重复实验以提供基本的变异性估计；(c) 如果无法增加实验，在讨论中明确标注"N=1, no statistical inference should be drawn"。

**N4** [critical] PSN-IRT 参数依赖缺乏敏感性分析

- **具体位置**：Section 3.1, Section 3.3
- **问题**：整个框架的 4PL 项目参数（a, b, c, d）来自 PSN-IRT（Zhuo et al., 2026），校准基础是"over 13,000 models"的大规模 leaderboard 数据。论文声明"we use these external parameters rather than re-estimating from potentially contaminated data"（Section 3.1），这是合理的设计选择。但 PSN-IRT 参数本身的质量如何？如果 leaderboard 上的模型样本存在系统性偏差（如以开源 7-13B 模型为主，缺少闭源大模型），校准出的项目参数可能不准确。论文未提供：(a) PSN-IRT 参数的精度/标准误信息；(b) 参数扰动下 ℓz* 的敏感性分析；(c) 与其他参数估计方法（如子集重估）的交叉验证。Section 3.1 提到"recovery degrades to rθ=0.127 when calibrating on contaminated leaderboard data"——如果 leaderboard 数据本身已经包含污染模型（很可能的情况），PSN-IRT 参数可能已经受到污染。
- **为什么影响接收**：这是一个 single point of failure——参数有偏则所有下游结论不可靠。审稿人无法评估结论的鲁棒性。
- **建议修改方向**：(a) 提供 4PL 参数估计的标准误或 bootstrap CI；(b) 进行参数扰动实验——在 a, b, c, d 参数上加入 5-10% 的随机噪声，观察 Δℓz* 效应大小的变化；(c) 讨论 PSN-IRT 校准样本中潜在污染对参数质量的影响。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] QLoRA SFT 作为唯一污染机制过于狭窄

- **具体位置**：Section 3.3
- **问题**：现实世界中 benchmark contamination 的主要途径是 pre-training data inclusion（Dodge et al., 2021; Magar and Schwartz, 2022），而非 fine-tuning。QLoRA SFT 产生的参数变化模式（集中在 LoRA adapter 的低秩更新）与 pre-training contamination（分散在全参数中的梯度更新）根本不同。论文的 θ-shift 分析、倒 U 型模式等发现可能是 SFT-specific 的，而非 contamination-general 的。
- **建议**：至少讨论为什么 SFT 是 pre-training contamination 的合理代理（proxy），或者明确将结论范围限定为 SFT-based contamination。

**W2** [warning] 仅两个污染水平（15%, 50%）不足以支撑剂量反应曲线的结论

- **具体位置**：Section 3.3, Section 4.2
- **问题**：加上 clean baseline，总共只有三个数据点来描绘 dose-response 曲线。要声称"inverted-U"形状，至少需要 5+ 个水平（如 5%, 15%, 25%, 50%, 75%）来确认峰值位置和曲线形状。两点下降（15%→50%）可能只是 monotonic decrease 而非 U 型。
- **建议**：增加中间污染水平（至少 25%），或将"inverted-U"改为更保守的表述如"non-monotonic decline"。

**W3** [warning] item-level 污染检测接近随机

- **具体位置**：Table 8 (Appendix), Section 5
- **问题**：ℓz* itemwise AUROC=0.53，仅比 random baseline (0.50) 高 0.03。即使使用跨模型特征（RF cross-model: 0.63），改善幅度也很有限。这意味着 ℓz* 在识别**哪些具体题目被污染**方面基本无效。虽然论文主要定位为 person-level（模型级）检测，但 Discussion (Section 5) 中提到"ℓz* can be split by item subsets to yield per-item memorization fingerprints"——Table 8 的结果并不支持这一说法。
- **建议**：修改 Section 5 中关于 item-level diagnostic 能力的表述，使之与 Table 8 的实际结果一致。

**W4** [warning] Detection-diagnosis tradeoff 的论证需要加强

- **具体位置**：Section 4.4, Table 3
- **问题**：accuracy |d|≈42-68 vs ℓz* |d|≈0.58-1.90，差距为 20-70 倍。论文声称 ℓz* 的价值在于三个诊断功能：(a) scoremeness decomposition, (b) θ-shift mechanism, (c) response-pattern sensitivity。但这三个功能仅通过描述性分析展示，没有量化评估其对实际决策的影响。一个重要的缺失问题是：**在什么实际场景下，诊断信息的价值足以弥补检测效力 20-70 倍的损失？**
- **建议**：提供至少一个具体的 use case，展示 ℓz* 的诊断信息如何辅助做出 accuracy-based methods 无法支持的决策。

**W5** [warning] 57/60 vs 4/60 flagging rate 比较具有误导性

- **具体位置**：Section 4.4（Discussion on response-pattern sensitivity）
- **问题**：论文报告 ℓz* 在真实 leaderboard 数据上 flags 57/60 cells（95%），而 accuracy z-scores 仅 flags 4/60 cells（6.7%）。这被呈现为 ℓz* 的"sensitivity to response-pattern structure"优势。但 57/60 flagging rate 恰恰说明 ℓz*  **无法区分** contamination 与一般性的 IRT 假设违反——这正是论文提出 Δℓz* 的原因（Section 3.2）。将原始 ℓz* 的高 false positive rate 作为优势来呈现，在逻辑上与论文自身的 Δℓz* 动机相矛盾。
- **建议**：重新表述这个比较，明确说明 57/60 flagging 反映的是 IRT 假设违反的普遍性而非污染检测能力，这也正是 Δℓz* 设计的动机。

**W6** [warning] 缺少与 ConStat、MIA、CoDec 的实证对比

- **具体位置**：Section 2 (Related Work), Section 4.4
- **问题**：ConStat (Dekoninck et al., 2024)、Min-K% (Shi et al., 2024)、CoDec (Zawalski et al., 2026) 是 Related Work 中引用的主要现有方法，但实验部分没有直接对比。虽然论文指出这些方法需要不同的 access level（token-level probabilities, generation-level），但至少 ConStat 同样是 performance-based method，在理论上可以进行公平对比。
- **建议**：至少与 ConStat 进行实证对比（两者都基于 benchmark performance），或提供更详细的理论比较说明为何实证对比不可行。

---

## Questions for Authors

**Q1**: Appendix A 的模拟验证（R²=0.957, power=80%+ at 15% contamination）是否假设了 IRT 模型正确拟合？如果在模拟中引入 local dependence（如 testlet 结构），ℓz* 的 Type I error rate 和检验力如何变化？

**Q2**: 论文称所有模型家族使用 n=10 seeds（Table 1 caption, Figure 2 caption），但 Mistral 的 CI 宽度明显大于 Qwen 和 Llama（如 Table 1: Mistral MMLU 15% [1.5, 7.4] vs Qwen MMLU 15% 的 CI）。是否所有模型确实使用了相同数量的 seeds？如果存在差异，应在方法部分明确说明。

**Q3**: PSN-IRT (Zhuo et al., 2026) 的 leaderboard 校准数据是否包含已知被污染的模型？如果是，这对 4PL 参数估计有什么影响？论文提到"recovery degrades to rθ=0.127 when calibrating on contaminated leaderboard data"——这个数字来自何种实验条件？

**Q4**: Fixed-θ anchoring 的 cross-benchmark ability estimation 在实际部署中如何实现？如果一个模型在多个 benchmark 上都存在污染，cross-benchmark estimation 是否也会受到偏差？

**Q5**: Table 8 的 item-level AUROC=0.53 说明 ℓz* 基本无法识别具体被污染的题目。那么 Section 5 中"ℓz* can be split by item subsets to yield per-item memorization fingerprints"的诊断价值体现在哪里？

**Q6**: Post-RL 实验（Section 4.5）中，GRPO 训练的 seen/unseen accuracy gap 在 step 500 后趋于稳定，而 ℓz* gap 也同步稳定。这是否说明 ℓz* 的 post-RL 信号实际上只是残留的 accuracy difference 的反映，而非独立的 response-pattern information？

---

## Missing References

1. **Magis et al. (2012)** — "A General Framework and an R Package for the Detection of Dichotomous Differential Item Functioning", Behavior Research Methods. 提供了 person-fit 统计量在 model misfit 下的 robustness 分析，与 N1 问题直接相关。

2. **Sinharay (2016)** — "Person-Fit Analysis in the Context of Computerized Adaptive Testing", in Handbook of Item Response Theory. 讨论了 person-fit 统计量在假设违反下的行为，对论文的理论基础有参考价值。

3. **Tendeiro & Meijer (2014)** — 已在 .bib 中但未被引用（orphan entry），讨论了非参数 person-fit 统计量在假设违反下的替代方案，可用于 robustness 讨论。

4. **Li et al. (2024)** — "Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models", TACL. 另一种 performance-based contamination detection 方法，适合在 Related Work 中讨论。

---

## 小问题（不影响接收）

- Figure 2 heatmap 的颜色映射说明（"Blue intensity reflects effect-size magnitude"）可以更具体——使用的是线性映射还是对数映射？灰色单元格（missing conditions: Llama 和 Mistral on ARC-C）建议在 caption 或正文中解释原因。
- Section 3.2 中"57 of 60 model-benchmark cells"的 60 如何构成——哪些模型和 benchmark？应给出简要说明或在 Appendix 中详细列出。
- 引用格式：.bib 中有 28 个 orphan entries（已在 .bib 但未在论文中引用），建议清理以保持 .bib 文件整洁。
- Table 3 的 Acc. 行中 Cohen's d 值极大（|d|=42+），建议在 footnote 中解释为什么 accuracy z-scores 产生如此大的效应量（可能因为 cross-seed accuracy variance 极小，导致 denominator 很小）。

---

## Reproducibility Assessment

- 4PL 参数来自 PSN-IRT (Zhuo et al., 2026)——需确认该工作是否公开发布参数或代码
- QLoRA SFT 训练细节（Section 3.3）：rank、lr、epochs 等信息基本充足，但缺少 data preprocessing 的细节（如何从 benchmark 中采样 15%/50% 的题目？按 subject 分层还是随机？）
- **未发现代码/数据可用性声明**——ARR 建议提供 reproducibility statement
- Bootstrap CI 的实现细节（bias-corrected? percentile method?）应补充

---

## 格式合规

- ✅ 正文 8 页内（Sections 1-6 + Limitations 在 page 8 结束，References 从 page 8 底部开始）
- ✅ 匿名格式（"Anonymous ACL submission"）
- ✅ Limitations 章节存在（page 8）
- ✅ 使用 ACL style
- ⚠️ Limitations 内容覆盖了主要限制（模型规模、污染机制、post-RL N=1），但未明确讨论 IRT 假设违反问题——这应该是最重要的 limitation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 265 · 2026-05-21T18:15:03.210537+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的 Must-Fix 和 Should-Fix 问题：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作格式\n\n**Overall**: 3.0 (Findings)，Soundness 3/5，Excitement 3/5，Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 生态效度不足——QLoRA fine-tuning 模拟污染 ≠ 真实 pretraining 污染\n\n- 具体位置：Section 3.3, Limitations (p8)\n- 问题：论文用 QLoRA (rank=16, α=32) 在 15%/50% 数据上 fine-tuning 模拟污染。真实污染发生在 pretraining 阶段，权重影响遍及整个网络，而 LoRA 微调只修改低秩适配器。这两种机制产生的 response pattern 可能有本质差异——fine-tuning 污染更接近\"item preknowledge\"（教育测试中的作弊），而 pretraining 污染可能更接近\"over-exposure\"。论文在 Limitations 中承认了这一点（\"fine-tuning remains future work\"），但这不是一个小问题——它直接影响所有四个 findings 的外推有效性。\n- 为什么影响接收：如果 fine-tuning 和 pretraining 产生不同的 aberrance pattern，则本文的 boundary conditions 可能不适用于真实场景，核心贡献大幅缩水。\n\n**N2** [critical] Post-RL finding (Section 4.5) 严重 under-validated：N=1 模型、单一 benchmark、单一 RL 算法\n\n- 具体位置：Section 4.5 (p7), Figure 4\n- 问题：Post-RL residual pattern 是论文最具新颖性的 finding（也是 abstract 中的重点 claim），但仅在 Qwen-2.5-7B + 15% MMLU 污染 + GRPO 算法上验证。N=1 模型、单一污染水平、单一 RL 方法（无 DPO/PPO 对比），结论的稳健性完全未知。Section 4.5 最后一段承认 \"We report this as a preliminary characterization\"，但 abstract 将其列为四大 findings 之一，没有标注 preliminary。\n- 为什么影响接收：作为 abstract 的核心 claim 之一，支撑证据严重不足。单一实验点无法建立任何 \"pattern\"。\n\n**N3** [critical] 核心 findings 中多数可从 IRT 理论直接推导，新颖贡献被高估\n\n- 具体位置：Section 4.2 (Inverted-U), Section 4.3 (θ-shift), Section 4.4 (Detection-diagnosis tradeoff)\n- 问题：\n  - **Inverted-U dose-response** (Section 4.2)：当污染率极高时，模型在绝大多数 item 上都正确，ℓz* 的方差必然减小——这是 IRT 的天花板效应，person-fit 文献中已知。\n  - **θ-shift dynamics** (Section 4.3)：能力参数与 person-fit 灵敏度的交互是 person-fit 文献的经典议题（Meijer & Sijtsma, 2001 的 methodology review 明确讨论了 ability level 对 person-fit detection 的影响）。\n  - **Detection-diagnosis tradeoff** (Section 4.4)：简单统计量比复杂统计量在纯检测上更强，但缺乏诊断能力——这是统计学中 power vs. specificity 的基本 tradeoff。\n- 为什么影响接收：如果四个 findings 中有三个是已知理论在新域的直接验证（而非新发现），则论文的 novelty 贡献低于 abstract 所宣称的。\n\n### Should-Fix 问题\n\n**W1** [warning] 模型覆盖范围过窄\n- 仅覆盖 3 个 7-8B 模型族。缺少更大模型（13B/70B）、不同架构（Mixture-of-Experts）的实验。Section 4.3 的 θ-shift dynamics 声称与 baseline ability 相关，但只有 3 个数据点。\n\n**W2** [warning] Item-level detection 接近随机（Table 8, Appendix）\n- AUROC 最高 0.63 (RF cross-model)，ℓz* itemwise 仅 0.53。严重限制了实际应用价值。\n\n**W3** [warning] Δℓz* 差异设计（Section 3.2）的假设未充分验证\n- Δℓz* 的核心假设是\"shared model misfit cancels\"。论文声称方法适用于 cross-benchmark comparison（没有 clean baseline 的场景），此时 Δℓz* 不可计算，方法的部署场景不清晰。\n\n**W4** [warning] Figure 2 heatmap 可读性差\n- 灰色 cell 未解释为何缺失。色彩映射跨度极大（1.08-15.3），线性映射导致中间值难以辨别。\n\n### 主要优势\n\n1. 概念创新：将 psychometric person-fit 统计量引入 LLM contamination detection。\n2. 实验设计规范：QLoRA, 10 seeds, bootstrap CI。\n3. 诚实的自我定位：以 \"characterization\" 而非 \"detection method\" 自居。\n4. Post-RL finding 有启发性。\n5. 与 existing methods 的桥接清晰（detection-diagnosis tradeoff）。\n\n### Missing References\n- Tendeiro & Meijer (2014) — 在 bib 中但未 cite，与 detection-diagnosis tradeoff 相关。\n- St-Onge et al. (2011) — 在 bib 中但未 cite，与 inverted-U 相关。\n- 引用总数 31 篇，处于顶会标准下限。\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W4) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的 Must-Fix 和 Should-Fix 问题：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作格式\n\n**Overall**: 3.0 (Findings)，Soundness 3/5，Excitement 3/5，Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 生态效度不足——QLoRA fine-tuning 模拟污染 ≠ 真实 pretraining 污染\n\n- 具体位置：Section 3.3, Limitations (p8)\n- 问题：论文用 QLoRA (rank=16, α=32) 在 15%/50% 数据上 fine-tuning 模拟污染。真实污染发生在 pretraining 阶段，权重影响遍及整个网络，而 LoRA 微调只修改低秩适配器。这两种机制产生的 response pattern 可能有本质差异——fine-tuning 污染更接近\"item preknowledge\"（教育测试中的作弊），而 pretraining 污染可能更接近\"over-exposure\"。论文在 Limitations 中承认了这一点（\"fine-tuning remains future work\"），但这不是一个小问题——它直接影响所有四个 findings 的外推有效性。\n- 为什么影响接收：如果 fine-tuning 和 pretraining 产生不同的 aberrance pattern，则本文的 boundary conditions 可能不适用于真实场景，核心贡献大幅缩水。\n\n**N2** [critical] Post-RL finding (Section 4.5) 严重 under-validated：N=1 模型、单一 benchmark、单一 RL 算法\n\n- 具体位置：Section 4.5 (p7), Figure 4\n- 问题：Post-RL residual pattern 是论文最具新颖性的 finding（也是 abstract 中的重点 claim），但仅在 Qwen-2.5-7B + 15% MMLU 污染 + GRPO 算法上验证。N=1 模型、单一污染水平、单一 RL 方法（无 DPO/PPO 对比），结论的稳健性完全未知。Section 4.5 最后一段承认 \"We report this as a preliminary characterization\"，但 abstract 将其列为四大 findings 之一，没有标注 preliminary。\n- 为什么影响接收：作为 abstract 的核心 claim 之一，支撑证据严重不足。单一实验点无法建立任何 \"pattern\"。\n\n**N3** [critical] 核心 findings 中多数可从 IRT 理论直接推导，新颖贡献被高估\n\n- 具体位置：Section 4.2 (Inverted-U), Section 4.3 (θ-shift), Section 4.4 (Detection-diagnosis tradeoff)\n- 问题：\n  - **Inverted-U dose-response** (Section 4.2)：当污染率极高时，模型在绝大多数 item 上都正确，ℓz* 的方差必然减小——这是 IRT 的天花板效应，person-fit 文献中已知。\n  - **θ-shift dynamics** (Section 4.3)：能力参数与 person-fit 灵敏度的交互是 person-fit 文献的经典议题（Meijer & Sijtsma, 2001 的 methodology review 明确讨论了 ability level 对 person-fit detection 的影响）。\n  - **Detection-diagnosis tradeoff** (Section 4.4)：简单统计量比复杂统计量在纯检测上更强，但缺乏诊断能力——这是统计学中 power vs. specificity 的基本 tradeoff。\n- 为什么影响接收：如果四个 findings 中有三个是已知理论在新域的直接验证（而非新发现），则论文的 novelty 贡献低于 abstract 所宣称的。\n\n### Should-Fix 问题\n\n**W1** [warning] 模型覆盖范围过窄\n- 仅覆盖 3 个 7-8B 模型族。缺少更大模型（13B/70B）、不同架构（Mixture-of-Experts）的实验。Section 4.3 的 θ-shift dynamics 声称与 baseline ability 相关，但只有 3 个数据点。\n\n**W2** [warning] Item-level detection 接近随机（Table 8, Appendix）\n- AUROC 最高 0.63 (RF cross-model)，ℓz* itemwise 仅 0.53。严重限制了实际应用价值。\n\n**W3** [warning] Δℓz* 差异设计（Section 3.2）的假设未充分验证\n- Δℓz* 的核心假设是\"shared model misfit cancels\"。论文声称方法适用于 cross-benchmark comparison（没有 clean baseline 的场景），此时 Δℓz* 不可计算，方法的部署场景不清晰。\n\n**W4** [warning] Figure 2 heatmap 可读性差\n- 灰色 cell 未解释为何缺失。色彩映射跨度极大（1.08-15.3），线性映射导致中间值难以辨别。\n\n### 主要优势\n\n1. 概念创新：将 psychometric person-fit 统计量引入 LLM contamination detection。\n2. 实验设计规范：QLoRA, 10 seeds, bootstrap CI。\n3. 诚实的自我定位：以 \"characterization\" 而非 \"detection method\" 自居。\n4. Post-RL finding 有启发性。\n5. 与 existing methods 的桥接清晰（detection-diagnosis tradeoff）。\n\n### Missing References\n- Tendeiro & Meijer (2014) — 在 bib 中但未 cite，与 detection-diagnosis tradeoff 相关。\n- St-Onge et al. (2011) — 在 bib 中但未 cite，与 inverted-U 相关。\n- 引用总数 31 篇，处于顶会标准下限。\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W4) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 266 · 2026-05-21T18:15:48.806905+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 45596
}
```

</details>

---


### Tool call

_source line 267 · 2026-05-21T18:15:49.009587+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的 Must-Fix 和 Should-Fix 问题：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**Overall**: 3.0 (Findings)，Soundness 3/5，Excitement 3.5/5，Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] IRT 假设违反的分析不充分，Δℓz* 有效性缺乏理论保证\n\n- 具体位置：Section 3.2, Appendix A\n- 问题：论文承认 LLM 响应\"systematically violate IRT assumptions of local independence and unidimensionality\"（Section 3.2），并提出 Δℓz* 差分设计作为解决方案。但差分设计仅在以下条件下有效：clean 和 contaminated conditions 下的 IRT 模型误拟合是**加性且等量的**。论文未分析一个关键问题：**污染是否改变了项目间的依赖结构？** 如果被记忆的题目变得独立于潜在能力 θ（答对纯靠记忆而非推理），而未被记忆的题目保持原有依赖模式，那么 contaminated condition 下的 misfit 结构与 clean condition 不同，Δℓz* 不再是有效的差分估计量。Appendix A 的模拟验证（R²=0.957）假设了 IRT 模型成立，构成循环论证。\n- 建议：(a) 模拟分析引入 local dependence 变化后 Δℓz* 的偏差；(b) 检验 clean 和 contaminated 下项目残差相关矩阵的系统性差异；(c) 讨论 Snijders 校正在假设违反下的鲁棒性。\n\n**N2** [critical] 倒 U 型剂量反应削弱了方法的实用性主张\n\n- 具体位置：Section 4.2, Figure 2, Table 1\n- 问题：Qwen 的 |d| 从 15% 的 6.56 下降到 50% 的 1.90（Table 1）。污染越严重，检测灵敏度越低。fixed-θ 需要 clean baselines——与\"operating at the minimal-information point\"的定位相矛盾。方法的宣传定位与实际限制之间存在显著落差。\n- 建议：(a) Abstract/Introduction 明确区分 free-θ 和 fixed-θ 的要求；(b) 将倒 U 型从\"finding\"提升为\"fundamental limitation\"；(c) 讨论 cross-benchmark ability estimation 的可行性。\n\n**N3** [critical] Post-RL 发现（Finding 4）统计效力严重不足\n\n- 具体位置：Section 4.5, Figure 4\n- 问题：N=1（一个模型 Qwen、一个污染水平 15%、一个 RL 方法 GRPO、一个 benchmark MMLU）。Figure 4 无误差条或置信区间。一个 N=1 的观察被提升到与其他 n=10 验证的发现同等地位。\n- 建议：(a) 降级为\"preliminary observation\"；(b) 增加至少 2-3 个 RL seeds；(c) 明确标注\"N=1, no statistical inference\"。\n\n**N4** [critical] PSN-IRT 参数依赖缺乏敏感性分析\n\n- 具体位置：Section 3.1, Section 3.3\n- 问题：整个框架依赖 PSN-IRT 的 4PL 参数。论文未提供：(a) 参数精度/标准误信息；(b) 参数扰动下 ℓz* 的敏感性分析；(c) 与其他参数估计方法的交叉验证。如果 leaderboard 数据本身包含污染模型，PSN-IRT 参数可能已受污染。\n- 建议：(a) 参数扰动实验（5-10% 噪声）；(b) 讨论校准样本中污染对参数质量的影响。\n\n### Should-Fix 问题\n\n**W1** [warning] QLoRA SFT 作为唯一污染机制过于狭窄\n- QLoRA SFT 产生的参数变化模式与 pre-training contamination 根本不同。θ-shift 分析等发现可能是 SFT-specific 的。\n\n**W2** [warning] 仅两个污染水平不足以支撑剂量反应曲线结论\n- 只有三个数据点来描绘 dose-response 曲线。两点下降可能是 monotonic decrease 而非 U 型。建议增加中间水平或改为保守表述。\n\n**W3** [warning] item-level 污染检测接近随机\n- ℓz* itemwise AUROC=0.53。Section 5 声称\"ℓz* can yield per-item memorization fingerprints\"与 Table 8 结果不一致。\n\n**W4** [warning] Detection-diagnosis tradeoff 论证需加强\n- accuracy |d|≈42-68 vs ℓz* |d|≈0.58-1.90，差距 20-70 倍。缺少具体 use case 展示诊断信息的价值。\n\n**W5** [warning] 57/60 vs 4/60 flagging rate 比较具有误导性\n- 57/60 flagging rate 恰恰说明 ℓz* 无法区分 contamination 与一般性 IRT 假设违反。将 ℓz* 的高 false positive rate 作为优势呈现与论文的 Δℓz* 动机矛盾。\n\n**W6** [warning] 缺少与 ConStat、MIA、CoDec 的实证对比\n- 至少 ConStat 同样是 performance-based method，可以公平对比。\n\n### Questions for Authors\n- Q1: 模拟验证是否假设 IRT 模型正确？local dependence 的影响？\n- Q2: Mistral n=6 seeds 而非 n=10？（Table 1 footnote 确认 Mistral n=6）\n- Q3: PSN-IRT 校准数据是否包含已知污染模型？\n- Q4: Fixed-θ 的 cross-benchmark estimation 如何实现？多 benchmark 污染时怎么办？\n- Q5: Item-level AUROC=0.53 与 Section 5 \"per-item memorization fingerprints\" 的矛盾？\n- Q6: Post-RL ℓz* gap 是否只是残留 accuracy difference 的反映？\n\n### Missing References\n1. Magis et al. (2012) — person-fit 在 model misfit 下的 robustness 分析\n2. Sinharay (2016) — person-fit 在假设违反下的行为\n3. Tendeiro & Meijer (2014) — 非参数 person-fit 替代方案（已在 bib 但未 cite）\n4. Li et al. (2024) — Data Contamination Quiz (TACL)\n\n### 主要优势\n1. 跨学科新颖性（person-fit 迁移到 LLM 评估）\n2. Δℓz* 差分设计合理\n3. 受控实验设计（n=10, bootstrap CI）\n4. θ-shift 机制分析有理论价值\n5. Detection-diagnosis tradeoff 的坦诚报告\n\n---\n\n请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W6) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的 Must-Fix 和 Should-Fix 问题：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**Overall**: 3.0 (Findings)，Soundness 3/5，Excitement 3.5/5，Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] IRT 假设违反的分析不充分，Δℓz* 有效性缺乏理论保证\n\n- 具体位置：Section 3.2, Appendix A\n- 问题：论文承认 LLM 响应\"systematically violate IRT assumptions of local independence and unidimensionality\"（Section 3.2），并提出 Δℓz* 差分设计作为解决方案。但差分设计仅在以下条件下有效：clean 和 contaminated conditions 下的 IRT 模型误拟合是**加性且等量的**。论文未分析一个关键问题：**污染是否改变了项目间的依赖结构？** 如果被记忆的题目变得独立于潜在能力 θ（答对纯靠记忆而非推理），而未被记忆的题目保持原有依赖模式，那么 contaminated condition 下的 misfit 结构与 clean condition 不同，Δℓz* 不再是有效的差分估计量。Appendix A 的模拟验证（R²=0.957）假设了 IRT 模型成立，构成循环论证。\n- 建议：(a) 模拟分析引入 local dependence 变化后 Δℓz* 的偏差；(b) 检验 clean 和 contaminated 下项目残差相关矩阵的系统性差异；(c) 讨论 Snijders 校正在假设违反下的鲁棒性。\n\n**N2** [critical] 倒 U 型剂量反应削弱了方法的实用性主张\n\n- 具体位置：Section 4.2, Figure 2, Table 1\n- 问题：Qwen 的 |d| 从 15% 的 6.56 下降到 50% 的 1.90（Table 1）。污染越严重，检测灵敏度越低。fixed-θ 需要 clean baselines——与\"operating at the minimal-information point\"的定位相矛盾。方法的宣传定位与实际限制之间存在显著落差。\n- 建议：(a) Abstract/Introduction 明确区分 free-θ 和 fixed-θ 的要求；(b) 将倒 U 型从\"finding\"提升为\"fundamental limitation\"；(c) 讨论 cross-benchmark ability estimation 的可行性。\n\n**N3** [critical] Post-RL 发现（Finding 4）统计效力严重不足\n\n- 具体位置：Section 4.5, Figure 4\n- 问题：N=1（一个模型 Qwen、一个污染水平 15%、一个 RL 方法 GRPO、一个 benchmark MMLU）。Figure 4 无误差条或置信区间。一个 N=1 的观察被提升到与其他 n=10 验证的发现同等地位。\n- 建议：(a) 降级为\"preliminary observation\"；(b) 增加至少 2-3 个 RL seeds；(c) 明确标注\"N=1, no statistical inference\"。\n\n**N4** [critical] PSN-IRT 参数依赖缺乏敏感性分析\n\n- 具体位置：Section 3.1, Section 3.3\n- 问题：整个框架依赖 PSN-IRT 的 4PL 参数。论文未提供：(a) 参数精度/标准误信息；(b) 参数扰动下 ℓz* 的敏感性分析；(c) 与其他参数估计方法的交叉验证。如果 leaderboard 数据本身包含污染模型，PSN-IRT 参数可能已受污染。\n- 建议：(a) 参数扰动实验（5-10% 噪声）；(b) 讨论校准样本中污染对参数质量的影响。\n\n### Should-Fix 问题\n\n**W1** [warning] QLoRA SFT 作为唯一污染机制过于狭窄\n- QLoRA SFT 产生的参数变化模式与 pre-training contamination 根本不同。θ-shift 分析等发现可能是 SFT-specific 的。\n\n**W2** [warning] 仅两个污染水平不足以支撑剂量反应曲线结论\n- 只有三个数据点来描绘 dose-response 曲线。两点下降可能是 monotonic decrease 而非 U 型。建议增加中间水平或改为保守表述。\n\n**W3** [warning] item-level 污染检测接近随机\n- ℓz* itemwise AUROC=0.53。Section 5 声称\"ℓz* can yield per-item memorization fingerprints\"与 Table 8 结果不一致。\n\n**W4** [warning] Detection-diagnosis tradeoff 论证需加强\n- accuracy |d|≈42-68 vs ℓz* |d|≈0.58-1.90，差距 20-70 倍。缺少具体 use case 展示诊断信息的价值。\n\n**W5** [warning] 57/60 vs 4/60 flagging rate 比较具有误导性\n- 57/60 flagging rate 恰恰说明 ℓz* 无法区分 contamination 与一般性 IRT 假设违反。将 ℓz* 的高 false positive rate 作为优势呈现与论文的 Δℓz* 动机矛盾。\n\n**W6** [warning] 缺少与 ConStat、MIA、CoDec 的实证对比\n- 至少 ConStat 同样是 performance-based method，可以公平对比。\n\n### Questions for Authors\n- Q1: 模拟验证是否假设 IRT 模型正确？local dependence 的影响？\n- Q2: Mistral n=6 seeds 而非 n=10？（Table 1 footnote 确认 Mistral n=6）\n- Q3: PSN-IRT 校准数据是否包含已知污染模型？\n- Q4: Fixed-θ 的 cross-benchmark estimation 如何实现？多 benchmark 污染时怎么办？\n- Q5: Item-level AUROC=0.53 与 Section 5 \"per-item memorization fingerprints\" 的矛盾？\n- Q6: Post-RL ℓz* gap 是否只是残留 accuracy difference 的反映？\n\n### Missing References\n1. Magis et al. (2012) — person-fit 在 model misfit 下的 robustness 分析\n2. Sinharay (2016) — person-fit 在假设违反下的行为\n3. Tendeiro & Meijer (2014) — 非参数 person-fit 替代方案（已在 bib 但未 cite）\n4. Li et al. (2024) — Data Contamination Quiz (TACL)\n\n### 主要优势\n1. 跨学科新颖性（person-fit 迁移到 LLM 评估）\n2. Δℓz* 差分设计合理\n3. 受控实验设计（n=10, bootstrap CI）\n4. θ-shift 机制分析有理论价值\n5. Detection-diagnosis tradeoff 的坦诚报告\n\n---\n\n请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W6) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 268 · 2026-05-21T18:15:50.423511+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1413
}
```

</details>

---


### Assistant

_source line 269 · 2026-05-21T18:15:55.521850+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 270 · 2026-05-21T18:15:58.111169+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整意见，核心结论：

- **Overall: 3.0（Findings）**，Confidence 4/5
- **4 个 Must-Fix**：IRT 假设违反分析不足（Δℓz* 有效性缺乏理论保证）、倒 U 型问题削弱实用性主张、Post-RL N=1 统计效力不足、PSN-IRT 参数依赖无敏感性分析
- **6 个 Should-Fix**：QLoRA SFT 过窄、仅两个污染水平、item-level 检测近随机、detection-diagnosis tradeoff 论证不足、57/60 vs 4/60 比较有误导性、缺少与 ConStat 等方法的实证对比
- **6 个 Questions**：涵盖模拟假设、seed 数量一致性、PSN-IRT 校准污染、fixed-θ 部署可行性、item-level 诊断价值、post-RL 信号独立性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 271 · 2026-05-21T18:16:06.231698+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 32

## Round 32

2 recorded events
