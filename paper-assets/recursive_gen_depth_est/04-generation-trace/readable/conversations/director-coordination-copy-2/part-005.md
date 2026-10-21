# Director coordination — Part 5 of 6

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/3d/3da1d06caead0f03c51d.json)

## Round 118

### Tool call

_source line 1284 · 2026-05-20T08:43:14.743104+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "# 交叉审稿 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，请标注：\n- **[AGREE]** 同意并简要说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 — Findings\n\n## Must-Fix 问题\n\n**N1** [critical] **Pipeline 缺乏算法创新，贡献主要在 task formalization + empirical characterization**\n- 核心 pipeline 是 19 个标准统计特征 + 标准 Random Forest。特征和分类器均为已有方法的直接应用，无算法层面创新。EMNLP 主会议期望至少在方法或理论层面有所推进。纯 benchmark-driven + empirical characterization 的贡献更适合 Findings track。\n\n**N2** [critical] **与 Binoculars 无显著差异（78.1% vs. 78.4%），削弱方法贡献**\n- Binoculars 11-feature RF 和 19-feature pipeline 差异仅 −0.3pp。Appendix B.26 feature ablation 显示 Binoculars 6 个 cross-perplexity 特征单独就能达到 75.9%，仅比完整 pipeline 低 2.2pp。读者会合理地问：为什么不直接用 Binoculars？\n\n**N3** [critical] **模型规模严重受限（≤1.5B），2026 年的实用性存疑**\n- 主实验仅覆盖 ≤1.5B 模型。14B 扩展实验 EDD_{τ=0.70} 仅为 d1，4-class accuracy 61%。2026 年主流模型 7B-70B+，≤1.5B 结论实用参考价值有限。14B 结果提供\"scaling 可能破坏 depth signal\"的证据，动摇核心 claim。\n\n## Should-Fix 问题\n\n**W1** Abstract 信息密度过载（10+ 个数字）\n**W2** d0 膨胀导致 headline metrics 误导性（同你的 N3）\n**W3** Full-replacement 设置与现实场景脱节（accumulation 缺失）\n**W4** EDD 指标理论动机薄弱（τ=0.70 选择依据不足，阈值敏感性高）\n**W5** Depth Degradation Atlas 贡献独立性存疑（用设计来捕捉 depth signal 的特征来描述 depth signal 的变化——循环性）\n**W6** Cross-strategy transfer 严重不足（59.1%），部署前景堪忧\n\n## Minor\n- M1: 2 个 orphan bib entries (dsir2023, qurating2024)\n- M2: 引用 author 顺序 mismatch（3 个条目）\n- M3: 主文过度引用附录，阅读碎片化\n- M4: \"depth\"术语在不同语境含义不同需区分\n- M5: Table 1 特征命名需更好说明\n\n## Questions\n- Q1: 14B EDD 降至 d1 是否意味着 ≥7B 规模下方法根本不可行？\n- Q2: 19-feature pipeline 相对 Binoculars 的实际优势是什么？\n- Q3: Temperature d1/d2 boundary inversion 是否使该策略下 estimation 本质不可靠？\n- Q4: 主 benchmark 仅 seed=42，能否提供 multi-seed 结果？\n- Q5: surprisal variance 和 perplexity tail 是否只是同一信号的不同视角？\n\n## Missing References\n1. **[critical]** Markovian Generation Chains in Large Language Models (arxiv:2603.11228, ICLR 2026) — 直接研究 LLM 迭代处理的 Markov 链动态\n2. [minor] 更强的 neural ordinal methods（proportional odds model 等）\n3. [minor] PAN 2026 / M4-SemEval 的评估协议讨论\n\n## EMNLP 适合度\nReviewer 2 认为：benchmark paper + empirical characterization 更符合 Findings 定位。Long Paper format 合理（内容量支撑）。\n\n---\n\n请对以上每个 Must-Fix（N1-N3）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "# 交叉审稿 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，请标注：\n- **[AGREE]** 同意并简要说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 — Findings\n\n## Must-Fix 问题\n\n**N1** [critical] **Pipeline 缺乏算法创新，贡献主要在 task formalization + empirical characterization**\n- 核心 pipeline 是 19 个标准统计特征 + 标准 Random Forest。特征和分类器均为已有方法的直接应用，无算法层面创新。EMNLP 主会议期望至少在方法或理论层面有所推进。纯 benchmark-driven + empirical characterization 的贡献更适合 Findings track。\n\n**N2** [critical] **与 Binoculars 无显著差异（78.1% vs. 78.4%），削弱方法贡献**\n- Binoculars 11-feature RF 和 19-feature pipeline 差异仅 −0.3pp。Appendix B.26 feature ablation 显示 Binoculars 6 个 cross-perplexity 特征单独就能达到 75.9%，仅比完整 pipeline 低 2.2pp。读者会合理地问：为什么不直接用 Binoculars？\n\n**N3** [critical] **模型规模严重受限（≤1.5B），2026 年的实用性存疑**\n- 主实验仅覆盖 ≤1.5B 模型。14B 扩展实验 EDD_{τ=0.70} 仅为 d1，4-class accuracy 61%。2026 年主流模型 7B-70B+，≤1.5B 结论实用参考价值有限。14B 结果提供\"scaling 可能破坏 depth signal\"的证据，动摇核心 claim。\n\n## Should-Fix 问题\n\n**W1** Abstract 信息密度过载（10+ 个数字）\n**W2** d0 膨胀导致 headline metrics 误导性（同你的 N3）\n**W3** Full-replacement 设置与现实场景脱节（accumulation 缺失）\n**W4** EDD 指标理论动机薄弱（τ=0.70 选择依据不足，阈值敏感性高）\n**W5** Depth Degradation Atlas 贡献独立性存疑（用设计来捕捉 depth signal 的特征来描述 depth signal 的变化——循环性）\n**W6** Cross-strategy transfer 严重不足（59.1%），部署前景堪忧\n\n## Minor\n- M1: 2 个 orphan bib entries (dsir2023, qurating2024)\n- M2: 引用 author 顺序 mismatch（3 个条目）\n- M3: 主文过度引用附录，阅读碎片化\n- M4: \"depth\"术语在不同语境含义不同需区分\n- M5: Table 1 特征命名需更好说明\n\n## Questions\n- Q1: 14B EDD 降至 d1 是否意味着 ≥7B 规模下方法根本不可行？\n- Q2: 19-feature pipeline 相对 Binoculars 的实际优势是什么？\n- Q3: Temperature d1/d2 boundary inversion 是否使该策略下 estimation 本质不可靠？\n- Q4: 主 benchmark 仅 seed=42，能否提供 multi-seed 结果？\n- Q5: surprisal variance 和 perplexity tail 是否只是同一信号的不同视角？\n\n## Missing References\n1. **[critical]** Markovian Generation Chains in Large Language Models (arxiv:2603.11228, ICLR 2026) — 直接研究 LLM 迭代处理的 Markov 链动态\n2. [minor] 更强的 neural ordinal methods（proportional odds model 等）\n3. [minor] PAN 2026 / M4-SemEval 的评估协议讨论\n\n## EMNLP 适合度\nReviewer 2 认为：benchmark paper + empirical characterization 更符合 Findings 定位。Long Paper format 合理（内容量支撑）。\n\n---\n\n请对以上每个 Must-Fix（N1-N3）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-20T08:43:16.305080+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1561
}
```

</details>

---


### Assistant

_source line 1286 · 2026-05-20T08:43:19.408577+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 119

## Round 119

2 recorded events


### User

_source line 1287 · 2026-05-20T08:43:22.130622+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要：**

- **Overall: 3.0 (Findings)**
- **Soundness: 3.5** — 实验设计系统扎实，但 ≤1.5B 规模和单 seed 限制了结论普适性
- **Excitement: 2.5** — 问题及时重要，但标准 RF pipeline 无算法创新且未超越 Binoculars
- **Reproducibility: 4.0** — 附录极其详尽（29 子节），复现门槛低

**3 个 Must-Fix：**
1. Pipeline 无算法创新（标准 RF + 标准统计特征），贡献限于 task formalization + empirical study
2. 与 Binoculars 无显著差异（78.1% vs 78.4%），削弱方法独立价值
3. 模型规模 ≤1.5B，14B 实验显示 EDD 降至 d1，signal 随 scale 衰减严重

**6 个 Should-Fix：** Abstract 数字过载、d0 膨胀误导 headline metrics、full-replacement 脱离现实、EDD 理论动机薄弱、Atlas 循环性、cross-strategy transfer 不足

**1 个关键 Missing Reference：** Markovian Generation Chains (ICLR 2026) — 直接研究 LLM 迭代生成的 Markov 链动态，高度相关但未引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1288 · 2026-05-20T08:43:28.011406+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 120

## Round 120

2 recorded events


### User

_source line 1289 · 2026-05-20T08:45:13.313195+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见

---

## Must-Fix 问题

**[AGREE] R2-N1: Pipeline 缺乏算法创新**

同意。核心 pipeline（19 个统计特征 + RF）在技术层面确实无新方法。特征集由标准 perplexity/surprisal/lexical/repetition 统计量组成（Table 1），分类器是 off-the-shelf RF（200 trees, Section 3.4）。Section 5.1 自己也验证了 RF/XGBoost/LightGBM 在 0.4pp 内收敛，进一步证实信号在特征不在分类器——但这同时意味着分类器选择无技术门槛。

补充我的发现：Binoculars 平局（N2）进一步加剧了这一问题。如果已有 detector 的特征重组就能达到相同性能，则连特征设计的贡献也被稀释。论文的真正贡献在于：(1) 问题形式化（ordinal depth estimation，Section 3.1 的 Definition 1）；(2) Degradation Atlas 的系统 empirical characterization（Section 4）；(3) 180K benchmark 构建。这些确实更符合 Findings 定位。

**[AGREE] R2-N2: 与 Binoculars 无显著差异**

完全同意，与我的 N1 一致。补充两点证据：

1. Appendix B.26（Table 26）中 Binoculars 6 个 cross-perplexity 特征单独达到 75.9%，是论文 19-feature pipeline（78.4%）的 96.8%。而 Binoculars 的完整 11 特征达到 78.1%，p>0.05。这说明 observer-performer divergence 已足以捕获 depth signal 的主要部分。

2. Merged 30-feature 达到 82.6%（+4.2pp），Table 26 分解显示 6 个 shared perplexity features 贡献 75.9%，本文独有的 13 个特征仅额外贡献 +2.5pp，Binoculars 独有的 5 个特征贡献 +4.2pp（从 78.4% 到 82.6%）。这意味着 Binoculars 独有特征的边际贡献反而**大于**本文独有特征——进一步削弱了特征设计的方法论贡献。

R2 的质疑"为什么不直接用 Binoculars"是合理的。论文的 deployment 论证（Section 5.1, "single reference model"）是工程优势而非科学贡献。

**[AGREE] R2-N3: 模型规模限制（≤1.5B）**

同意核心论断，但对表述程度有保留。

同意的部分：2026 年 ≤1.5B 模型确实不是主流 generator。14B 实验（Section 5.4, Appendix B.14）mean 50.8%, EDD₀.₇₀=0 是致命的实验结果。Section 5.4 列出的 5 个 confounders（instruction-tuning, self-reference, architecture shift, BPE mismatch, unknown training data）使得无法从 14B 失败中得出有用结论——既不能说方法失败，也不能说方法可行，这本身就是问题。

保留的部分：R2 称 "14B 结果提供 scaling 可能破坏 depth signal 的证据"——我认为措辞应更审慎。由于 5 个 confounders 未分离，我们不知道是 scaling 破坏了 depth signal，还是 instruction-tuning / self-reference / architecture 等因素导致的。Appendix B.14 中 Llama-3.1-8B 在 instruct 变体上"monotonicity breaks at d4"而 base model 保持 monotonic decay（Table 17），这暗示 instruction-tuning 而非 scale 可能是更大的 confound。

建议作者分离实验：例如对 Pythia-6.9B（同架构、无 instruction-tuning）做完整测试，可隔离 scale 因素。

---

## Should-Fix 问题

**[AGREE] R2-W1: Abstract 信息密度过载**

同意。Abstract 包含至少 12 个数字（78.4%, MAE=0.23, QWK=0.89, 66.4%, 59.1%, 74.1%, 82.6%, 50.8%, 19, 180K, 4, 3 等），信息密度过高。更重要的是，这些数字中部分因 d0 膨胀（我的 N3）和 self-reference confound（我的 N2）而具有误导性。

建议：Abstract 聚焦于 (1) 问题定义 (2) 关键方法洞见 (3) 最重要的 1-2 个 takeaway 数字（附带 d1-d3 caveat）。

**[AGREE] R2-W2: d0 膨胀导致 headline metrics 误导性**

完全同意，与我的 N3 一致。d0 recall >97%（Section 4.1, Table 8 in Appendix B.4）本质上是 binary human-vs-machine detection 的已解决问题。Cross-model headline 66.4% 在排除 d0 后降至 55.4%，cross-strategy 59.1% 降至 45.9%（Section 5.2-5.3 中的 d1-d3 报告）。论文标题和核心 claim 围绕 "depth estimation" 而非 "detection"，因此 d1-d3 性能才是真正的贡献度量。

**[AGREE] R2-W3: Full-replacement 设置与现实脱节**

同意。论文 Limitations（p.9）承认"full-replacement recursive chains where each depth fully replaces the prior training corpus"是简化设置，现实中更多是 accumulation（混合真实数据和合成数据）。Gerstgrasser et al. (2024) 已证明 accumulation 显著缓解 model collapse——如果 accumulation 也缓解了统计 fingerprint 的深度差异，则本文方法的 applicability 进一步受限。

不过需要指出，Limitations 中的讨论是公开透明的："Our results therefore represent an upper bound on depth discriminability"（p.9）。问题不在于缺乏 awareness，而在于主实验未包含任何 accumulation 条件下的评估数据。

**[REBUT] R2-W5: Degradation Atlas 贡献独立性存疑（循环性指控）**

不同意 R2 的 "循环性" 论断。

R2 的论点是：用设计来捕捉 depth signal 的特征来描述 depth signal 的变化构成逻辑循环。但这混淆了"测量工具"与"测量发现"。

1. **特征是测量工具，Atlas 是测量发现。** 19 个特征是 text 的统计属性（perplexity percentiles, surprisal variance, type-token ratio, n-gram repetition 等），它们不预设 depth signal 的存在——人类文本同样有这些属性值。Atlas 的发现是这些属性**如何随 depth 系统性变化**，包括：哪些属性 monotonically decay（Section 4.3, perplexity tail），哪些先降后升（lexical diversity 在某些策略下），哪些对 strategy 敏感（temperature vs nucleus 产生不同 trajectory shapes, Section 4.5）。这些 pattern 是 empirical finding，不是循环推理。

2. **Atlas 的反面发现证明非循环。** 如果是循环的，所有特征应都显示强 depth signal。但 Atlas 恰恰发现某些特征**不**随 depth 单调变化：Section 4.2 报告 repetition features 在 top-k 下 importance 低于其他策略；Section 4.3 报告某些 model-strategy cells 的 monotonicity breaks。这些"负面发现"不可能从循环论证中产出。

3. **Atlas 对非本文特征同样有价值。** Atlas 的 methodology（系统性地 sweep model × strategy × depth 并报告 feature trajectories）可用于任何统计特征集。即使用 Binoculars 特征做同样的 atlas，发现仍然有价值。

因此 Atlas 是一个 legitimate empirical contribution，不存在循环性问题。

**[AGREE] R2-W4: EDD 指标理论动机薄弱**

同意，与我的 W6 一致。τ=0.70 借自 Hosmer & Lemeshow (2000) 的 binary logistic regression AUC 判别标准（Section 3.4），但 EDD 是基于 ordinal pairwise AUC 的指标，两者的统计性质不同。Section 3.4 的 sensitivity analysis（T∈{0.65,0.70,0.75,0.80}）显示 T=0.80 时多个 cell 丢失一个 depth level（"several cells lose one depth level"，Limitations p.9），这暗示结论对阈值敏感。

补充：EDD 的 monotonicity assumption（Definition 1, "EDD_τ reports the longest contiguous prefix"）要求相邻 depth 的 AUC 单调递减。Section 4.3 报告"the sole non-monotonic case"在 1-1.5B 范围内仅出现一次，但 14B 实验（B.14）中 monotonicity 频繁打破。如果 monotonicity 在 larger scale 不成立，EDD 的适用范围被进一步限制。

**[AGREE] R2-W6: Cross-strategy transfer 严重不足**

完全同意，与我的 N4 一致。补充一个 R2 未提及的发现：Section 5.3 报告 z-score normalization 修复了 logistic regression 的 cross-strategy 性能但**不修复 RF**。这说明 RF 的 cross-strategy 失败不仅是 feature scale 问题，而是因为 RF 学到了 strategy-specific 的非线性决策边界，这些边界在策略间不可迁移。这比单纯的 "accuracy 低" 更令人担忧——它暗示不同解码策略产生了**结构性不同**的 depth signal，而非仅是量表偏移。

Appendix B.28 的 cross-strategy conditional decomposition 提出了两阶段 pipeline 作为缓解方案（先识别 strategy 再分别分类），但这需要额外的 strategy 标注，降低了方法的实用性。

---

## Questions 回应

**R2-Q1（14B EDD 降至 d1 → ≥7B 不可行？）**: 证据不足以下此结论——5 个未分离的 confounders 意味着我们不知道是 scale 本身还是其他因素导致失败。Appendix B.14 Table 17 中 base model 与 instruct 变体的差异暗示 instruction-tuning 是更大的 confound。需要 controlled experiment（如 Pythia-6.9B base）来回答。

**R2-Q2（19-feature vs Binoculars 优势？）**: 基于我的分析，科学优势不存在（p>0.05）。唯一优势是工程层面的（1 model vs 2 models）。Merged 30-feature 的 +4.2pp 提示正确方向是融合而非替代。

**R2-Q3（Temperature boundary inversion → 本质不可靠？）**: 同意这是严重问题。Section 4.5 和 5.3 的讨论表明 temperature scaling 压缩 inter-depth distance，使 d1/d2 边界消失。但论文也报告在 temperature 下 d0-vs-d3 仍可分（Appendix B.7, Table 10），所以不是完全不可靠，而是 fine-grained depth 在该策略下不可解。

**R2-Q4（Multi-seed？）**: 合理要求。Appendix B.24（Table 25）提供了 3 个 RF seed（42, 123, 456）的结果，std=0.06pp，但这只是 classifier seed。Data generation seed 未做 ablation，这是更大的 concern——不同 generation seed 可能产生不同质量的合成数据。

**R2-Q5（surprisal variance vs perplexity tail 是否同一信号？）**: 部分同意。Section 4.2 报告 p50_ppl 和 var_surprisal 的 Spearman correlation 为 0.81（Appendix B.2），表明高度共线性。但 permutation importance（Appendix B.2）显示两者独立贡献 rank 在 top-5 中稳定出现，suggesting 不完全冗余。VIF>10 的共线性问题（我的 W1）使得这个问题无法从 importance 角度清晰回答。

---

## Missing References 回应

**R2-MR1（Markovian Generation Chains, arxiv:2603.11228）**: 我未独立搜索到此引用。如果存在且直接研究 LLM 迭代生成的 Markov 链动态，确实与本文高度相关，应引用。建议 Director 验证此引用的真实性。

**R2-MR2/MR3**: 同意 proportional odds model 应在 Related Work 讨论（当前仅在 Appendix B.25 引用 McCullagh 1980）。PAN 2026 已被引用（bevendorff2026_pan），但评估协议未被讨论。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1290 · 2026-05-20T08:45:20.703253+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 121

## Round 121

2 recorded events


### User

_source line 1291 · 2026-05-20T08:45:24.170569+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **N1-N3**: 全部 [AGREE]。算法创新不足、Binoculars 平局、规模限制三个问题与我的独立发现一致，共同指向 Findings 定位。
- **W1-W4, W6**: [AGREE]。d0 膨胀、full-replacement 脱节、EDD 理论动机薄弱、cross-strategy 失败均与我的 review 吻合。
- **W5（Atlas 循环性）**: [REBUT]。R2 混淆了测量工具与测量发现——Atlas 中的负面发现（某些特征不随 depth 单调变化）恰好证明了非循环性。Atlas 是独立的 empirical contribution。

两位 Reviewer 的核心共识：问题定义有价值，但方法性能（尤其是与 Binoculars 持平、cross-strategy/scale 失败、d0 膨胀 headline）不足以支撑 Main Conference，Findings 更合适。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1292 · 2026-05-20T08:45:31.664099+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 122

## Round 122

10 recorded events


### User

_source line 1293 · 2026-05-20T08:45:44.746719+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 问题

### [AGREE] R1-N1: Binoculars 特征平局严重削弱方法论贡献

同意 R1 的判断。我在自己的 N2 中也提出了同样的问题。补充两点：

1. **Merged 30-feature 的 82.6%（Appendix B.26, Table 26）反而佐证了 R1 的论点**——如果两组特征是信息互补的，那么"本文 19 特征"并非捕获了独特信号，只是对同一分布偏移现象的另一组统计视角。这更像是 feature engineering 的枚举，而非方法论创新。

2. **R1 的表述"信号不在*这些*特征，而在*任何*能捕获分布偏移的特征"精准。** Appendix B.26 显示仅 Binoculars 的 6 个 shared perplexity 特征就达到 75.9%，仅低于完整 pipeline 2.2pp。这说明 depth signal 的核心来源是 reference-model perplexity 的分布统计量，而非本文特征设计的独特贡献。

不过，我想补充一个 nuance：论文的贡献定位应区分"pipeline 方法创新"和"task formalization + empirical study"。如果论文不声称方法论创新（§6 确实说"our contribution centers on task formulation and systematic empirical characterization"），则 Binoculars 平局是可以接受的——关键是论文在 Abstract 和 Introduction 中的 framing 是否一致。目前的 framing 偏向于暗示 pipeline 本身是贡献，这需要修正。

---

### [AGREE] R1-N2: Self-reference confound 使 Pythia 结果不可比

同意这是一个需要严肃对待的系统性偏差。补充我的分析：

1. **Appendix B.13 的 ablation 数据直接证实了 confound 的规模。** Pythia-1.4B（self）78.6% → GPT-NeoX（cross）78.6%（几乎持平），但 OLMo-1B（cross）74.5%，GPT-2 XL（cross）67.3%。这意味着 reference model 选择可造成高达 11pp 的差异。

2. **R1 观察到的"cross-model transfer 中 Pythia holdout 行 62.4% 低于 OLMo 69.2%"值得关注。** 我在 Table 5（p.8）中验证了这一点：Pythia holdout 的 d1-d3 balanced accuracy（40.9%）也低于 OLMo（46.5%）。这一反转（Pythia 在 in-distribution 最高但 holdout 最低）确实是 self-reference confound 传递到 transfer 场景的证据。

3. **但我认为 R1 说"1/3 in-distribution 结果存在系统性偏差"略有夸大。** 论文在 §5.1 明确标注了"Self reference accuracy"（Table 2 footnote），并在 Appendix B.13 提供了完整的 reference model ablation。问题更多在于 headline 数字（如 Abstract 的"68.9% four-class accuracy"）是否应排除 Pythia self-reference cells，或至少并列报告。

---

### [REBUT] R1-N3: d0 膨胀问题的严重程度被 R1 高估

**部分反驳。** 我在自己的 W2 中也指出了 d0 膨胀，但将其定位为 Should-Fix 而非 Must-Fix，理由如下：

1. **论文在大多数关键位置确实并列报告了 d1-d3 数字。** Abstract："68.9% four-class accuracy (d1-d3: 39-45%)"；Table 5（cross-model）："66.4% (d1-d3: 55.4%)"（p.8 §5.2）；Table 6（cross-strategy）："59.1% (d1-d3: 45.9%)"（p.8 §5.3）。R1 说"Abstract 报告时未突出 d1-d3 的大幅下降"不完全准确——Abstract 的括号内确实给出了 d1-d3 数字，只是不够突出。

2. **d0 的高 recall 本身也是一个有价值的发现。** 它证明了 human vs. first-generation 的区分是容易的（这与 binary detection 文献一致），而真正的挑战在 d1-d3 之间。论文在 §4.1 和 Appendix B.4 对此有详细讨论。

3. **但我同意 R1 的核心关切：headline 数字应以 d1-d3 为主打。** 这更多是一个 presentation/framing 问题（Should-Fix），而非实验设计缺陷（Must-Fix）。数据完整，问题在于突出什么。

**结论：同意问题存在，但应为 Should-Fix，非 Must-Fix。**

---

### [AGREE] R1-N4: Cross-strategy 和 cross-scale 失败动摇泛化 claim

同意这是最严重的问题之一。我在自己的 N3 中也将 scale 限制列为 critical。

1. **Cross-strategy d1-d3 45.9% 的问题比 R1 描述的更深层。** 这不仅是"接近 chance 33%"的数字问题，而是揭示了一个结构性矛盾：论文声称"perplexity tail family dominates depth discrimination across all 9 cells"（§4.2），但 cross-strategy transfer 的大幅退化表明这些 perplexity tail 特征实际上是 strategy-entangled 的。换言之，特征捕获的部分是 decoding strategy 的 fingerprint 而非 pure depth signal。

2. **14B 结果（Appendix B.14）确实令人担忧。** EDD_{τ=0.70}=d1（仅 adjacent depth-0/depth-1 可区分），4-class accuracy 61%。但我对 R1 的"方法在实际部署规模上完全失效"的措辞略有保留——14B 实验仅测试了一条 pipeline（Pythia-410M LoRA → 14B），样本量有限（200 samples/depth），且使用 nucleus 单策略。结论应更审慎地表述为"初步证据表明 scaling 方向不乐观"，而非"完全失效"。

3. **两个问题的叠加效应更为严重。** 如果部署场景同时面临 unknown decoding strategy + large scale generator，pipeline 的有效性几乎不可预期。论文目前将这些分别放在不同的 appendix 中讨论，掩盖了叠加风险。

---

## Should-Fix 问题

### [AGREE] R1-W1: 多重共线性与可解释性 claim 矛盾

R1 的统计论点成立。VIF>10 表示 14-16/19 特征存在严重共线性，此时 Gini importance 的分配是不稳定的——微小的数据扰动可能导致 importance 在共线特征之间大幅转移。论文 §3.3 已承认"effective independent dimensionality is n≈4-5"，这与 19 特征形成 tension。

补充：论文在 Appendix B.2 使用了 permutation importance 和 SHAP 作为补充，这部分缓解了 Gini 的不稳定性。但 SHAP（TreeSHAP for RF）在高共线性下也会在相关特征之间分散 attribution。论文声称"top-2 features are stable across measures"（Appendix B.2）可能仅因为 p90_ppl 和 var_surprisal 与其他特征的共线性结构恰好使它们始终排名靠前。

**建议：报告 grouped feature importance（将 19 特征按 Table 1 的 4 个 category 分组），或使用条件 permutation importance，以避免共线性带来的 attribution 伪影。**

---

### [AGREE] R1-W2: LoRA 超参无 ablation

同意。LoRA r=16, α=32 是生成 depth-d 数据的关键步骤——不同的 LoRA 配置可能产生不同程度的 distribution shift，从而影响 depth signal 的强弱。如果 r=4 的轻量微调产生更微妙的 shift（更接近真实场景），pipeline 性能可能会更低。

不过，此问题的优先级低于 N1-N4：LoRA 配置影响的是 benchmark 构建的 ecological validity，而非 pipeline 方法本身。如果论文明确将 benchmark 定位为"controlled setting with strong fine-tuning"，这个 concern 可以被部分缓解。

---

### [REBUT] R1-W3: BOS-seeded vs prompted generation 的严重程度

**部分反驳。** R1 引用的 −13.8pp gap 来自 §3.5 的 theoretical grounding（non-passage lineage = −13.8 pp），但这个数字的语境需要澄清：

1. 论文在 Appendix B.27 的 prompted generation 实验中，实际 gap 更具体：BOS-seeded baseline 的 4-class accuracy 69.5% vs. prompted generation 某个配置（需要具体看 B.27 数据）。Limitations 中明确列出了"BOS vs prompted"作为局限。

2. **关键 nuance：** 论文的 generation protocol 使用 Wikipedia seed text（§3.2："Starting from a Wikipedia subset"），不是纯 BOS-seeded。每个 depth cycle 用前一代的输出作为 prompt seed。这比纯 BOS generation 更接近现实的 recursive loop。R1 将其等同于"BOS-seeded"可能不完全准确。

3. 但 R1 关于 "ecological validity" 的核心关切有效：instruction-following 场景下的 recursive generation（如 ChatGPT 反复改写同一段文字）与论文的 continuation-based generation protocol 有本质区别。这限制了论文结论向 prompted/instruction 场景的推广。

**结论：concern 有效，但 R1 对 generation protocol 的描述需要更精确。应为 Should-Fix 而非更高。**

---

### [AGREE] R1-W4: Cross-domain 评估的局限性

同意 R1 的核心关切，但需修正一个事实：

1. **论文实际上测试了多个域，而非"仅 arXiv"。** Appendix B.11 的 wild-data classification 覆盖了 WikiText-103（editorial）、C4（web crawl, 5000 passages）、FineWeb（web crawl）。§5.4 也在 arXiv 上进行了 cross-domain 测试。

2. **但 R1 关于高 FPR 的数据点确实令人担忧。** 从 Appendix B.11（p.17, Table 13）：C4 上 GPT-2 XL 的 d1 misclassification 是最高的（对应 FPR 问题）。特别是 template/SEO content 中高 n-gram repetition 触发 false positive——这说明 pipeline 的 repetition 特征在 web text 上缺乏鲁棒性。

3. **confidence threshold 0.15 能将 FPR 降至可控范围，但代价是大幅降低 recall。** 这种 precision-recall tradeoff 在实际部署中可能不可接受。

**R1 的"single domain"表述不准确，但高 FPR 的核心关切完全成立。**

---

### [AGREE] R1-W5: 多重比较未校正

R1 的统计方法论关切有效。论文在 Appendix B.12 的 paired permutation tests 中报告了多组 p-values（cross-strategy transfer 的 15+ pairwise comparisons），但未应用 Bonferroni 或 FDR 校正。

实际影响可能有限：论文的 main conclusions 不依赖 borderline significance（核心发现如 perplexity tail dominance、cross-strategy gap 都是 large effect sizes），但作为统计规范性问题，应该补充。

---

### [AGREE] R1-W6: EDD 阈值理论依据不足

完全同意，与我自己的 W4 一致。τ=0.70 从 Hosmer & Lemeshow (2000) 的 binary logistic regression "acceptable discrimination" 标准迁移到 ordinal pairwise AUC 缺乏理论依据。两个额外 concerns：

1. **阈值敏感性在 Appendix B.7（temperature robustness）中已有证据。** τ=0.80 时 "several cells lose one depth level"（Limitations, p.9），说明 EDD 的绝对值高度依赖 τ。
2. **τ=0.70 对应 "acceptable"，是一个较低的 bar。** 如果用 τ=0.75（"good"），多数 cell 的 EDD 可能降为 d1 或 d0，这会从根本上改变论文的结论叙事。

---

## Minor 问题

**[AGREE] R1-M1:** 同意，2 个 orphan bib entries（dsir2023, qurating2024）应清理。

**[AGREE] R1-M2:** Binary RF 500 trees vs 4-class RF 200 trees 的不一致确实应解释。不同 tree count 可能影响性能比较的公平性。

**[REBUT] R1-M3:** R1 说"§4.3 monotonicity claim 与 14B non-monotonic 发现有 tension"。但论文在 §4.3 的 monotonicity claim 明确限定在 ≤1.5B 的 primary benchmark 范围内（"Depth features exhibit strong monotonic trends"），14B 结果是 Appendix B.14 的 preliminary extension。两者 scope 不同，不构成直接矛盾。14B 的 non-monotonicity 更可能是规模变化引入的新现象（如 instruction-tuned 变体的 U-shaped decay），而非反驳 primary benchmark 的 monotonicity。

**[AGREE] R1-M4:** 同意。Gini importance heatmap（Figure 1）在 VIF>10 的共线性下确实不稳定。

**[AGREE] R1-M5:** 同意。Appendix B.28 的 two-stage pipeline 是缓解 cross-strategy 问题的关键尝试，值得在主文中提及。

---

## Missing References 回应

**[AGREE] Min-K%++（Zhang et al., 2024）：** 论文引用了 Min-K% Prob（Shi et al., 2024）但未提及 Min-K%++ 作为更强的 membership inference baseline。如果 Min-K%++ 在 depth discrimination 上表现不同，这可能影响 §5.1 的 classifier comparison 结论。值得补充。

**[REBUT] 近年 ordinal classification in NLP 综述：** 论文已引用 Kasa et al. (2024) 的 comparative study（"Exploring Ordinality in Text Classification"），这是该方向最近的全面调查。此外还引用了 CORAL (2020)、CLOC (2025)、Frank & Hall (2001)、McCullagh (1980)、Rennie & Srebro (2005)。覆盖度尚可。

**[AGREE] RAID benchmark 的讨论缺失：** 论文引用了 RAID (Dugan et al., 2024) 但未解释为何不采用其评估协议。RAID 覆盖 11 个 LLMs + 多种 attack 手段，其 robustness evaluation framework 可能对本文的 generalization claims 提供更强的验证。至少应讨论 RAID protocol 与本文设置的异同。

---

## 交叉总结

R1 和我（R2）在以下问题上 **高度一致**：
1. **Binoculars 平局削弱方法贡献**（R1-N1 = R2-N2）
2. **Scale 限制是核心问题**（R1-N4 部分 = R2-N3）
3. **EDD 阈值缺乏理论依据**（R1-W6 = R2-W4）
4. **d0 膨胀需要处理**（R1-N3 ≈ R2-W2，但严重程度评估不同）

**我与 R1 的分歧**主要在：
1. **d0 膨胀的严重程度**：我认为是 Should-Fix（论文已并列报告 d1-d3），R1 认为是 Must-Fix。
2. **Self-reference confound（R1-N2）**：R1 将其列为 Must-Fix，我认为论文在 Appendix B.13 的 ablation 部分缓解了这一问题，更接近 Should-Fix（但 headline 数字确实应调整）。
3. **R1 的 W4 "single domain"表述不准确**——论文测试了 WikiText-103、arXiv、C4、FineWeb 四个域。但 web text 上的高 FPR 确实是有效关切。

**两位 Reviewer 均给出 3.0（Findings）**，核心理由一致：task formalization 有价值，empirical study 系统全面，但缺乏算法创新、规模受限、且未超越现有方法。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-20T08:46:08.365636+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-20T08:46:08.467055+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T08:34:33.373276+00:00\", \"completed_at\": \"2026-05-20T08:38:10.092500+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页连续纯文本，无任何 display item（figure/table/diagram）。第一个 display item（Table 1）直到第 4 页才出现，第一个 figure（Figure 1 热力图）直到第 6 页才出现。审稿人在前 2 分钟内只看到文字墙，缺乏视觉锚点来快速建立对论文核心贡献的认知。强烈建议在第 1-2 页加入一个概览图（如 pipeline 示意图：Wikipedia seed → 递归生成 → 特征提取 → 深度分类），或一个 teaser figure 展示核心发现\"}, {\"severity\": \"critical\", \"dimension\": \"page 8\", \"message\": \"最后一页主文本塞入 3 个 table（Table 4/5/6）+ 1 个 figure（Figure 3 混淆矩阵），过度拥挤。Figure 3 的混淆矩阵数字极小，打印后可能无法阅读。建议将部分 table 移入 appendix 或合并精简，给 Figure 3 更多空间\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-5\", \"message\": \"Display item 分布严重不均：前 5 页仅 1 个 table（Table 1, p4），后 3 页（p6-8）塞入 8 个 display items（3 tables + 1 figure on p6, 1 figure on p7, 3 tables + 1 figure on p8）。造成前半段\\\"文字墙\\\"后半段\\\"图表堆砌\\\"的节奏失衡\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"第 5 页为纯文本页（Section 3.5 Theoretical Grounding + Section 4 开头），夹在 Table 1（p4）和 Table 2/Figure 1（p6）之间，形成额外的文字断层\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"全文主体缺少方法概览图/架构图。3 个 figure 全部是分析性图表（热力图、AUC 曲线、混淆矩阵），没有一个概念性 figure 帮助读者理解方法 pipeline。对于一个提出新 benchmark + 新 metric（EDD）的论文，一个 pipeline/framework 概览图对审稿人建立理解至关重要\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 3 混淆矩阵：3 个矩阵并排显示，单个矩阵尺寸很小，内部数字字号远低于正文 70% 标准。建议增大尺寸或改用全宽 figure*\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1 热力图中的 feature name 标签字号偏小，但在 150 dpi 下仍可辨认。打印时可能需要放大。建议适当增大标签字号\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 AUC decay 曲线的 legend 字号较小，线条样式（实线/虚线）区分清晰，颜色方案可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1（19 个统计特征分类表）使用了 booktabs 风格，格式规范。但作为第一个 display item 缺乏视觉冲击力，无法传达论文核心 message\"}
…[truncated 797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-20T08:46:08.467440+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-20T08:46:08.518478+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1298 · 2026-05-20T08:48:17.117577+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n# ============================================================\n# CRITICAL ISSUES (Round 15 — Fresh Review)\n# ============================================================\n\n- id: R15-N1\n  summary: Pipeline 缺乏算法创新，19-feat RF 与 Binoculars 11-feat RF 无显著差异 (78.4% vs 78.1%, p>0.05)\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-N1 + R2-N1 + R2-N2 一致。Binoculars 平局 + 标准 RF/统计特征无算法创新。Merged 30-feat 82.6% 说明互补而非本文特征优越。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N2\n  summary: Cross-strategy (d1-d3 45.9%) 和 cross-scale (14B EDD=0, mean 50.8%) 泛化严重不足\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-N4 + R2-N3 + R2-W6 一致。Cross-strategy d1-d3 接近 chance; 14B 5个confound未分离; 不同策略产生结构性不同的 depth signal。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N3\n  summary: Self-reference confound — Pythia 同时做 generator 和 reference model，1/3 结果存在系统偏差 (4-11pp advantage)\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-N2 Must-Fix, R2 认为 B.13 ablation 部分缓解偏 Should-Fix。Director 裁定 Must-Fix: headline 数字包含 confound 膨胀。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# SHOULD-FIX ISSUES (Round 15)\n# ============================================================\n\n- id: R15-W1\n  summary: d0 膨胀 headline metrics — cross-model d1-d3 仅 55.4% (报告 66.4%), cross-strategy d1-d3 仅 45.9% (报告 59.1%)\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-N3 Must-Fix, R2-W2 Should-Fix。论文已并列报告 d1-d3 但不够突出。Director 裁定 Should-Fix（高优先级）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W2\n  summary: EDD 阈值 T=0.70 从 binary AUC 标准迁移到 ordinal pairwise AUC 缺乏理论依据，阈值敏感性高\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W6 + R2-W4 一致。T=0.80 时多个 cell 丢失 depth level; monotonicity 在 14B 打破。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W3\n  summary: 多重共线性 (VIF>10 for 14-16/19) 与 Gini/SHAP 可解释性 claim 矛盾\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W1, R2 交叉 AGREE。Gini importance 在高共线性下不稳定。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W4\n  summary: Full-replacement 设置与现实 accumulation 场景脱节，缺 accumulation 实验\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W3 部分 + R2-W3 一致。论文 Limitations 透明但主实验无 accumulation 数据。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 微调超参 (r=16, α=32) 无 ablation，影响 benchmark 生态效度\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W2, R2 交叉 AGREE。不同 LoRA 配置可能产生不同退化模式。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W6\n  summary: Abstract 信息密度过载 (10+ 数字)，核心 message 被数字洪流淹没\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R2-W1, R1 交叉 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W7\n  summary: Cross-domain 评估有限，web 文本 FPR 高 (C4 34%, FineWeb 17%)\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W4。论文测试了 4 个域但 web text 高 FPR 未在正文讨论。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W8\n  summary: 多重比较未做 Bonferroni/FDR 校正\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W5, R2 交叉 AGREE。实际影响可能有限但统计规范性不足。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏关键引用 — Markovian Generation Chains (ICLR 2026, arxiv:2603.11228)\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [2]\n    note: \"R2-MR1 critical missing ref。直接研究 LLM 迭代生成 Markov 链动态。R1 未独立验证真实性。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR / INFO ISSUES (Round 15)\n# ============================================================\n\n- id: R15-M1\n  summary: 2 个 orphan bib entries (dsir2023, qurating2024) 需清理\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-M1 + R2-M1 一致。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-M2\n  summary: Binary RF 500 trees vs 4-class RF 200 trees 的不同选择未解释\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1]\n    note: \"R1-M2。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-M3\n  summary: 主文过度引用附录导致阅读碎片化\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [2]\n    note: \"R2-M3。§4-§6 几乎每段有 Appendix B.X 引用。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-M4\n  summary: Figure 3 混淆矩阵数字极小，打印后可能无法阅读\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"视觉审查发现。建议改用 figure* 全宽。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (Rounds 12-14, all resolved/wont_fix)\n# ============================================================\n\n- id: R12-W4\n  summary: Cross-scale 14B 实验 5 重混淆，EDD=0 与 \"signal persists\" claim 矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Should-Fix, R2 Must-Fix. Director 裁定 Should-Fix.\n  - round: 13\n    reviewers: [1, 2]\n    note: 升级为 critical。论文已将标题改为 Preliminary，但 Abstract 仍言过其实。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Must-Fix. EDD=0 与 'persists' 矛盾。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N2 重新覆盖。论文已改用 'residual discrimination above chance'。措辞修复但根本问题(5 confounders)仍在。\"\n  action_items:\n  - round: 14\n    action: \"§5.4 标题改 Preliminary; Abstract/§6 删除 persists; 加 EDD=0 + confound disclaimer\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§5.4 标题改为 'Preliminary Cross-Scale Observations (14B)', Abstract/§6 全面降调. 但 R15 指出根本泛化问题仍开放。\"\n  resolution_round: 14\n\n- id: R12-W3\n  summary: Headline metrics 被 d0 召回率（>97%）系统性膨胀\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: 一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 部分改善。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Must-Fix. Abstract/Intro 以 4-class 为主指标.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W1 复发。双指标格式已应用但 headline 仍以 4-class 领头。\"\n  action_items:\n  - round: 14\n    action: \"所有 headline 双指标并列 X% (d1-d3: Y%)\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"双指标格式已全面应用。R15 认为 d1-d3 应更突出但问题严重程度降低。\"\n  resolution_round: 14\n\n- id: R14-C1\n  summary: 与 Binoculars 11-feat RF 无显著差异（78.4% vs 78.1%），Table 4 呈现不透明\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Must-Fix. Table 4 缺 11-feat RF 行.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N1 作为更大问题的一部分重新审视。Table 4 已修复但根本问题(方法贡献不足)仍在。\"\n  action_items:\n  - round: 14\n    action: \"Table 4 加 Binoculars 11-feat RF 78.1% + Merged 82.6% + p>0.05 + 部署优势论证\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"Table 4 加两行, 脚注 p>0.05, 部署优势论述完整.\"\n  resolution_round: 14\n\n- id: R14-C2\n  summary: 主文超出 8 页限制\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"视觉审查发现. §6 溢出约 0.3-0.5 页.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 视觉审查确认页数合规：正文 pp.1-8, Limitations p.9 起。\"\n  action_items:\n  - round: 14\n    action: \"压缩正文; 删除 §6 重复句; §5.3 压缩\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"页数合规。R15 确认。\"\n  resolution_round: 14\n\n- id: R12-W1\n  summary: Full-replacement 与真实 accumulation setting 差异\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2 critical, R1 REBUT. Director 裁定 Should-Fix.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W4 复发。Limitations 中有透明声明但仍缺 accumulation 实验数据。\"\n  action_items:\n  - round: 14\n    action: \"引用 accum_v3 实验数据 (70.1%/69.1% vs 84.2%)\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§6 引用 accum_v3 具体数字。R15 认为仍不足但问题已被论文 acknowledge。\"\n  resolution_round: 14\n\n- id: R12-W9\n  summary: 算法贡献不足：标准 RF + 标准特征\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. PLM R²<0 insight 应提升到主文.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N1 升级为 critical。PLM 洞察已添加但根本问题(无算法创新)不变。\"\n  action_items:\n  - round: 14\n    action: \"将 Appendix B.7 核心结论 (PLM R²<0) 提升到主文\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§6 加入 PLM R²<0 结论。但 R15 认为 task formalization 无法补偿算法创新缺失。\"\n  resolution_round: 14\n\n- id: R12-M3\n  summary: Self-reference confound 使 atlas 不可比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. Table 2 需 caveat.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N3 升级为 critical。Caveat 已加但 headline 数字仍包含 confound 膨胀。\"\n  action_items:\n  - round: 14\n    action: \"Table 2 caption 加 Pythia self-reference caveat\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"Table 2 加 † caveat。R15 认为需进一步处理 headline 数字。\"\n  resolution_round: 14\n\n- id: R12-W2\n  summary: Cross-strategy d1-d3 仅 45.9%, boundary inversion\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. 需报告 strategy classifier 准确率.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N2 作为泛化失败的一部分重新覆盖。Strategy classifier 57.8% 已报告。\"\n  action_items:\n  - round: 14\n    action: \"报告 strategy classifier 57.8% + 部署前提条件声明\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§5.3 加 strategy classifier + deployment prerequisite。\"\n  resolution_round: 14\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. 仍仅 3/9 cells.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 未单独提出但 R2-Q4 要求 multi-seed in-distribution 结果。\"\n  action_items:\n  - round: 14\n    action: \"Skip — 用户明确不跑新实验\"\n    assigned_to: research_director\n    status: wont_fix\n  resolution: \"用户指示项目收尾不再跑新实验.\"\n  resolution_round: 14\n\n- id: R12-W7\n  summary: Discussion 过薄\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  action_items:\n  - round: 14\n    action: \"与 C4 联合处理\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§6 加入 PLM R²<0, accumulation 数据, 压缩 curation.\"\n  resolution_round: 14\n\n- id: R12-W5\n  summary: Curation PoC 主比较不显著但语气偏乐观\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  action_items:\n  - round: 14\n    action: \"B.22 标题加 (Inconclusive); §6 降调\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"B.22 标题改为 Inconclusive. §6 降调。\"\n  resolution_round: 14\n\n- id: R12-W6\n  summary: Abstract 信息过载\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W6 复发。数字仍过多。\"\n  action_items:\n  - round: 14\n    action: \"与 C2 合并处理\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"双指标格式部分改善但 R15 认为仍过载。\"\n  resolution_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n# ============================================================\n# CRITICAL ISSUES (Round 15 — Fresh Review)\n# ============================================================\n\n- id: R15-N1\n  summary: Pipeline 缺乏算法创新，19-feat RF 与 Binoculars 11-feat RF 无显著差异 (78.4% vs 78.1%, p>0.05)\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-N1 + R2-N1 + R2-N2 一致。Binoculars 平局 + 标准 RF/统计特征无算法创新。Merged 30-feat 82.6% 说明互补而非本文特征优越。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N2\n  summary: Cross-strategy (d1-d3 45.9%) 和 cross-scale (14B EDD=0, mean 50.8%) 泛化严重不足\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-N4 + R2-N3 + R2-W6 一致。Cross-strategy d1-d3 接近 chance; 14B 5个confound未分离; 不同策略产生结构性不同的 depth signal。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N3\n  summary: Self-reference confound — Pythia 同时做 generator 和 reference model，1/3 结果存在系统偏差 (4-11pp advantage)\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-N2 Must-Fix, R2 认为 B.13 ablation 部分缓解偏 Should-Fix。Director 裁定 Must-Fix: headline 数字包含 confound 膨胀。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# SHOULD-FIX ISSUES (Round 15)\n# ============================================================\n\n- id: R15-W1\n  summary: d0 膨胀 headline metrics — cross-model d1-d3 仅 55.4% (报告 66.4%), cross-strategy d1-d3 仅 45.9% (报告 59.1%)\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-N3 Must-Fix, R2-W2 Should-Fix。论文已并列报告 d1-d3 但不够突出。Director 裁定 Should-Fix（高优先级）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W2\n  summary: EDD 阈值 T=0.70 从 binary AUC 标准迁移到 ordinal pairwise AUC 缺乏理论依据，阈值敏感性高\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W6 + R2-W4 一致。T=0.80 时多个 cell 丢失 depth level; monotonicity 在 14B 打破。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W3\n  summary: 多重共线性 (VIF>10 for 14-16/19) 与 Gini/SHAP 可解释性 claim 矛盾\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W1, R2 交叉 AGREE。Gini importance 在高共线性下不稳定。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W4\n  summary: Full-replacement 设置与现实 accumulation 场景脱节，缺 accumulation 实验\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W3 部分 + R2-W3 一致。论文 Limitations 透明但主实验无 accumulation 数据。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 微调超参 (r=16, α=32) 无 ablation，影响 benchmark 生态效度\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W2, R2 交叉 AGREE。不同 LoRA 配置可能产生不同退化模式。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W6\n  summary: Abstract 信息密度过载 (10+ 数字)，核心 message 被数字洪流淹没\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R2-W1, R1 交叉 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W7\n  summary: Cross-domain 评估有限，web 文本 FPR 高 (C4 34%, FineWeb 17%)\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W4。论文测试了 4 个域但 web text 高 FPR 未在正文讨论。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W8\n  summary: 多重比较未做 Bonferroni/FDR 校正\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W5, R2 交叉 AGREE。实际影响可能有限但统计规范性不足。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏关键引用 — Markovian Generation Chains (ICLR 2026, arxiv:2603.11228)\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [2]\n    note: \"R2-MR1 critical missing ref。直接研究 LLM 迭代生成 Markov 链动态。R1 未独立验证真实性。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR / INFO ISSUES (Round 15)\n# ============================================================\n\n- id: R15-M1\n  summary: 2 个 orphan bib entries (dsir2023, qurating2024) 需清理\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-M1 + R2-M1 一致。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-M2\n  summary: Binary RF 500 trees vs 4-class RF 200 trees 的不同选择未解释\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1]\n    note: \"R1-M2。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-M3\n  summary: 主文过度引用附录导致阅读碎片化\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [2]\n    note: \"R2-M3。§4-§6 几乎每段有 Appendix B.X 引用。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-M4\n  summary: Figure 3 混淆矩阵数字极小，打印后可能无法阅读\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"视觉审查发现。建议改用 figure* 全宽。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (Rounds 12-14, all resolved/wont_fix)\n# ============================================================\n\n- id: R12-W4\n  summary: Cross-scale 14B 实验 5 重混淆，EDD=0 与 \"signal persists\" claim 矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Should-Fix, R2 Must-Fix. Director 裁定 Should-Fix.\n  - round: 13\n    reviewers: [1, 2]\n    note: 升级为 critical。论文已将标题改为 Preliminary，但 Abstract 仍言过其实。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Must-Fix. EDD=0 与 'persists' 矛盾。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N2 重新覆盖。论文已改用 'residual discrimination above chance'。措辞修复但根本问题(5 confounders)仍在。\"\n  action_items:\n  - round: 14\n    action: \"§5.4 标题改 Preliminary; Abstract/§6 删除 persists; 加 EDD=0 + confound disclaimer\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§5.4 标题改为 'Preliminary Cross-Scale Observations (14B)', Abstract/§6 全面降调. 但 R15 指出根本泛化问题仍开放。\"\n  resolution_round: 14\n\n- id: R12-W3\n  summary: Headline metrics 被 d0 召回率（>97%）系统性膨胀\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: 一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 部分改善。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Must-Fix. Abstract/Intro 以 4-class 为主指标.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W1 复发。双指标格式已应用但 headline 仍以 4-class 领头。\"\n  action_items:\n  - round: 14\n    action: \"所有 headline 双指标并列 X% (d1-d3: Y%)\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"双指标格式已全面应用。R15 认为 d1-d3 应更突出但问题严重程度降低。\"\n  resolution_round: 14\n\n- id: R14-C1\n  summary: 与 Binoculars 11-feat RF 无显著差异（78.4% vs 78.1%），Table 4 呈现不透明\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Must-Fix. Table 4 缺 11-feat RF 行.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N1 作为更大问题的一部分重新审视。Table 4 已修复但根本问题(方法贡献不足)仍在。\"\n  action_items:\n  - round: 14\n    action: \"Table 4 加 Binoculars 11-feat RF 78.1% + Merged 82.6% + p>0.05 + 部署优势论证\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"Table 4 加两行, 脚注 p>0.05, 部署优势论述完整.\"\n  resolution_round: 14\n\n- id: R14-C2\n  summary: 主文超出 8 页限制\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"视觉审查发现. §6 溢出约 0.3-0.5 页.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 视觉审查确认页数合规：正文 pp.1-8, Limitations p.9 起。\"\n  action_items:\n  - round: 14\n    action: \"压缩正文; 删除 §6 重复句; §5.3 压缩\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"页数合规。R15 确认。\"\n  resolution_round: 14\n\n- id: R12-W1\n  summary: Full-replacement 与真实 accumulation setting 差异\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2 critical, R1 REBUT. Director 裁定 Should-Fix.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W4 复发。Limitations 中有透明声明但仍缺 accumulation 实验数据。\"\n  action_items:\n  - round: 14\n    action: \"引用 accum_v3 实验数据 (70.1%/69.1% vs 84.2%)\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§6 引用 accum_v3 具体数字。R15 认为仍不足但问题已被论文 acknowledge。\"\n  resolution_round: 14\n\n- id: R12-W9\n  summary: 算法贡献不足：标准 RF + 标准特征\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. PLM R²<0 insight 应提升到主文.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N1 升级为 critical。PLM 洞察已添加但根本问题(无算法创新)不变。\"\n  action_items:\n  - round: 14\n    action: \"将 Appendix B.7 核心结论 (PLM R²<0) 提升到主文\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§6 加入 PLM R²<0 结论。但 R15 认为 task formalization 无法补偿算法创新缺失。\"\n  resolution_round: 14\n\n- id: R12-M3\n  summary: Self-reference confound 使 atlas 不可比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. Table 2 需 caveat.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N3 升级为 critical。Caveat 已加但 headline 数字仍包含 confound 膨胀。\"\n  action_items:\n  - round: 14\n    action: \"Table 2 caption 加 Pythia self-reference caveat\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"Table 2 加 † caveat。R15 认为需进一步处理 headline 数字。\"\n  resolution_round: 14\n\n- id: R12-W2\n  summary: Cross-strategy d1-d3 仅 45.9%, boundary inversion\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. 需报告 strategy classifier 准确率.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N2 作为泛化失败的一部分重新覆盖。Strategy classifier 57.8% 已报告。\"\n  action_items:\n  - round: 14\n    action: \"报告 strategy classifier 57.8% + 部署前提条件声明\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§5.3 加 strategy classifier + deployment prerequisite。\"\n  resolution_round: 14\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. 仍仅 3/9 cells.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 未单独提出但 R2-Q4 要求 multi-seed in-distribution 结果。\"\n  action_items:\n  - round: 14\n    action: \"Skip — 用户明确不跑新实验\"\n    assigned_to: research_director\n    status: wont_fix\n  resolution: \"用户指示项目收尾不再跑新实验.\"\n  resolution_round: 14\n\n- id: R12-W7\n  summary: Discussion 过薄\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  action_items:\n  - round: 14\n    action: \"与 C4 联合处理\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"§6 加入 PLM R²<0, accumulation 数据, 压缩 curation.\"\n  resolution_round: 14\n\n- id: R12-W5\n  summary: Curation PoC 主比较不显著但语气偏乐观\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  action_items:\n  - round: 14\n    action: \"B.22 标题加 (Inconclusive); §6 降调\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"B.22 标题改为 Inconclusive. §6 降调。\"\n  resolution_round: 14\n\n- id: R12-W6\n  summary: Abstract 信息过载\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W6 复发。数字仍过多。\"\n  action_items:\n  - round: 14\n    action: \"与 C2 合并处理\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"双指标格式部分改善但 R15 认为仍过载。\"\n  resolution_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-20T08:48:17.218734+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml\", \"bytes\": 13081}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-20T08:50:56.811898+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "report": "# 审稿报告 — Round 15 (Fresh Review)\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle), Long Paper\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**轮次**: Round 1, 1 轮收敛（交叉分享后关键问题达成共识）\n\n---\n\n## Summary\n\n论文将递归生成深度估计形式化为序数分类问题（d0-d3），构建了 180K 样本的 benchmark（3 model families × 3 decoding strategies × 4 depths），使用 19 个统计特征 + Random Forest 实现深度分类。主要贡献包括任务形式化、Depth Degradation Atlas（系统映射不同策略下的退化轨迹）和 EDD 指标（量化可区分深度范围）。In-distribution accuracy 69-86%（d1-d3: 59-82%），cross-model transfer 66.4%（d1-d3: 55.4%），cross-strategy 59.1%（d1-d3: 45.9%），14B preliminary 50.8%（EDD₀.₇₀=0）。\n\n---\n\n## Strengths\n\n**S1. 新颖且有意义的任务形式化。** 将深度估计从二元检测扩展为序数分类是自然且未被充分探索的方向。在 model collapse 日益受关注的背景下，区分\"生成了几轮\"比仅区分\"是否生成\"有更强的实用价值。Definition 1（§3.1）和 EDD 指标（§3.4）提供了清晰的形式化框架。[R1-S1, R2-S1 一致]\n\n**S2. 系统的实验设计和全面的泛化分析。** 3×3 model-strategy grid、cross-model/cross-strategy/cross-domain transfer、7-14B 规模探索、d0-d5 深度扩展、种子稳健性——分析轴覆盖广泛。29 个附录实验展现了严肃的实验态度和高复现性。[R1-S2/S4, R2-S2 一致]\n\n**S3. Depth Degradation Atlas 的系统映射。** §4 发现了解码策略诱导的质变差异：nucleus 保持单调衰减、temperature 引入 d1/d2 boundary inversion、top-k truncation 移除 depth-discriminative 低概率 tokens。这些发现对理解递归生成的统计机制有参考价值。[R1-S2, R2-S3 一致]\n\n**S4. Limitations 部分诚实全面。** 覆盖了 full-replacement vs accumulation、scale limitation、BOS vs prompted、reference model dependency、cross-strategy deployment constraint 等核心局限。学术诚实度值得肯定。[R2-S5]\n\n**S5. 引用质量高。** 74 篇引用中 63 篇 OpenAlex 验证通过，无伪造引用，所有 \\cite 均有对应 bib 条目。[R1-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [critical] Pipeline 缺乏算法创新，且与 Binoculars 无显著差异。**\n核心 pipeline 是 19 个标准统计特征（perplexity moments/quantiles、surprisal statistics、lexical diversity、n-gram repetition）+ 标准 Random Forest（200 trees, 5-fold CV），无任何算法层面创新。更严重的是，Binoculars 11-feat RF 达到 78.1%，与本文 19-feat RF 的 78.4% 无显著差异（p>0.05, Table 4）。Merged 30-feat 82.6% 说明信息互补而非本文特征优越；Binoculars 独有 5 特征的边际贡献 (+4.2pp) 反而大于本文独有 13 特征 (+2.5pp, Appendix B.26)。\n→ 论文的方法论贡献被大幅稀释。\"discriminative signal resides in feature design\"（Abstract）的 claim 恰好被 Binoculars 平局反驳。\n[R1-N1 + R2-N1 + R2-N2 一致, 交叉 AGREE]\n\n**C2. [critical] Cross-strategy 和 cross-scale 泛化严重不足，动摇方法实用性。**\n- Cross-strategy transfer d1-d3 仅 45.9%（chance 33%），出现 d1/d2 boundary inversion。z-score normalization 修复 logistic regression 但不修复 RF，说明不同策略产生结构性不同的 depth signal（§5.3）。\n- 14B cross-scale mean 50.8%，EDD₀.₇₀=0，5 个 confounders 未分离（§5.4）。\n- 两个问题叠加：在 unknown strategy + large scale 部署场景下，pipeline 有效性几乎不可预期。\n- 2026 年主流模型 7B-70B+，≤1.5B 结论实用参考价值有限。\n→ 这不仅是 limitation，而是动摇核心 claim 的根本质疑。\n[R1-N4 + R2-N3 + R2-W6 一致, 交叉 AGREE]\n\n**C3. [critical] Self-reference confound 使 1/3 in-distribution 结果存在系统性偏差。**\nPythia-1.4B 同时是 generator 和 reference model，Table 2 显示 Pythia 比 OLMo/GPT-2 XL 高 4-11pp。Appendix B.13 换用 GPT-2 XL reference 时 accuracy 降至 67.3%（−11pp）。Cross-model transfer 中 Pythia holdout 62.4% 低于 OLMo 69.2%——self-reference confound 传递到 transfer 场景。Table 2 的 † 脚注和 B.13 ablation 部分缓解但 headline 数字仍包含膨胀。\n[R1-N2 Must-Fix, R2 偏 Should-Fix; Director 裁定 Must-Fix — headline 数字直接受 confound 影响]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. d0 膨胀 headline metrics。** d0 recall >97%（本质是已解决的 binary detection）。Cross-model headline 66.4% 排除 d0 后降至 55.4%，cross-strategy 59.1% 降至 45.9%。论文已在括号内并列 d1-d3 数字但不够突出——Abstract 和 §6 首句仍以 4-class accuracy 领头。\n[R1-N3 Must-Fix, R2-W2 Should-Fix; Director 裁定 Should-Fix（高优先级）— 数据完整，问题在 framing]\n\n**W2. EDD 阈值 T=0.70 理论依据不足。** 借自 Hosmer & Lemeshow (2000) 的 binary logistic regression AUC 标准，迁移到 ordinal pairwise AUC 未被论证。T=0.80 时多个 cell 丢失 depth level，结论对阈值敏感。monotonicity assumption 在 14B 打破。\n[R1-W6 + R2-W4 一致, 交叉 AGREE]\n\n**W3. 多重共线性（VIF>10 for 14-16/19）与可解释性 claim 矛盾。** Gini importance 和 SHAP 在高共线性下不稳定，§4.2 的特征重要性排序可靠性存疑。Appendix B.2 的 permutation importance 部分缓解但 SHAP（TreeSHAP）同样受影响。\n[R1-W1, R2 交叉 AGREE]\n\n**W4. Full-replacement 设置与现实 accumulation 场景脱节。** 主实验无 accumulation 条件。§6 引用 pilot 数据（70.1%/69.1% vs 84.2%）但缺乏系统评估。Limitations 透明但主实验 gap 仍在。\n[R1-W3 + R2-W3 一致, 交叉 AGREE]\n\n**W5. LoRA 微调超参无 ablation。** r=16, α=32 的选择直接影响生成文本质量和 depth signatures，不同 LoRA 配置可能产生不同退化模式。\n[R1-W2, R2 交叉 AGREE]\n\n**W6. Abstract 信息密度过载。** 10+ 个数字，核心 message 被淹没。建议精简至 3-4 个最关键数字。\n[R2-W1, R1 交叉 AGREE]\n\n**W7. Cross-domain web 文本 FPR 偏高。** C4 34%, FineWeb 17%（Appendix B.11），template/SEO content 的 n-gram repetition 触发 false positive。正文未充分讨论。\n[R1-W4, R2 交叉 AGREE（修正\"单域\"表述）]\n\n**W8. 多重比较未校正。** 多组 pairwise comparisons 未做 Bonferroni/FDR 校正。实际影响可能有限但统计规范性不足。\n[R1-W5, R2 交叉 AGREE]\n\n### Minor\n\n- M1: 2 个 orphan bib entries (dsir2023, qurating2024)。[R1+R2 一致]\n- M2: Binary RF 500 trees vs 4-class RF 200 trees 未解释。[R1]\n- M3: 主文过度引用附录（§4-§6 几乎每段有 Appendix B.X），阅读碎片化。[R2]\n- M4: Figure 3 混淆矩阵数字极小，建议改用 figure* 全宽。[视觉审查]\n- M5: 引用 author 顺序 mismatch：alemohammad2024_mad、guo2024_biscope、hosmer2000。[R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下关键问题两位 Reviewer 达成完全共识：\n\n1. **Binoculars 平局 + 无算法创新** → 方法论贡献不足以支撑 Main Conference [R1-N1 = R2-N1/N2]\n2. **Cross-strategy/scale 泛化失败** → 实际部署价值受限 [R1-N4 = R2-N3/W6]\n3. **EDD 阈值缺乏理论依据** → 核心指标稳健性存疑 [R1-W6 = R2-W4]\n4. **d0 膨胀需处理**（严重程度有细微差异但问题本身无争议）[R1-N3 ≈ R2-W2]\n5. **Full-replacement 脱离现实** [R1-W3 = R2-W3]\n6. **论文定位为 Findings 更合适** [R1 Overall 3.0 = R2 Overall 3.0]\n\n## Reviewer Divergence [REBUT]\n\n1. **d0 膨胀的严重程度**：R1 列为 Must-Fix（headline 数字误导），R2 列为 Should-Fix（论文已并列报告 d1-d3）。\n   → Director 裁定：**Should-Fix（高优先级）**。论文确实在关键位置并列了 d1-d3 数字，但应将 d1-d3 作为主打而非补充。\n\n2. **Self-reference confound 严重程度**：R1 列为 Must-Fix（1/3 结果系统偏差），R2 认为 B.13 ablation 部分缓解。\n   → Director 裁定：**Must-Fix**。虽然 ablation 在附录中，但 headline 数字（Abstract, Table 2）直接受 confound 影响，需要在主文中报告 excluding-Pythia 的 conservative estimate。\n\n3. **Atlas 循环性（R2-W5）**：R1 [REBUT] 论证 Atlas 使用测量工具描述测量发现不构成循环，负面发现（某些特征不随 depth 单调变化）证明了非循环性。\n   → Director 裁定：**接受 R1 的 REBUT**。Atlas 的 methodology 可用于任何特征集，其发现（strategy-dependent trajectories、feature hierarchy shifts with depth）是 legitimate empirical contribution。此项不列为 weakness。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** 如果使用完全不同架构的 reference model（如 Mamba/RWKV），特征提取结果会如何？当前 ablation（B.13）仅在 Transformer 内部换模型。[R1-Q1]\n\n**Q2.** Perplexity tail features 捕获的是 depth-specific signature 还是仅仅是文本质量代理？depth-1 低质量文本与 depth-2 \"正常\"文本，特征能否区分？[R1-Q2]\n\n**Q3.** z-score normalization 修复 logistic regression 但不修复 RF 的根本原因是什么？是否说明 RF 学到了 strategy-specific 非线性边界？[R1-Q3]\n\n**Q4.** 14B 实验中 5 个 confounders 能否通过实验设计分离？例如用 14B reference model，或测试 Pythia-6.9B base（同架构无 instruction-tuning）。[R1-Q5]\n\n**Q5.** 19-feature pipeline 相对 Binoculars 的实际优势是什么？科学上无显著差异（p>0.05），工程优势（1 model vs 2 models）是否足够？[R2-Q2]\n\n**Q6.** 主 benchmark 仅 seed=42，能否提供 in-distribution multi-seed 结果？Appendix B.24 的 3 seeds 仅测 classifier seed，未测 data generation seed。[R2-Q4]\n\n**Q7.** surprisal variance 和 perplexity tail（如 p90_ppl）在信息论上有何区别？是否是同一信号的不同视角？[R2-Q5]\n\n---\n\n## Missing References\n\n**MR1. [critical]** Markovian Generation Chains in Large Language Models (arxiv:2603.11228, ICLR 2026)。直接研究 LLM 迭代生成的 Markov 链动态（convergence to fixed points、cycle behavior、decoding strategy 影响），与本文 recursive generation setup 和 strategy-dependent trajectory 发现高度相关。[R2 提出, R1 未独立验证真实性，建议作者核实]\n\n**MR2. [minor]** Min-K%++（Zhang et al., 2024）。Min-K% Prob 的改进版本，应作为更强的 membership inference baseline 考虑。[R1]\n\n**MR3. [minor]** RAID benchmark（Dugan et al., 2024）已引用但未解释为何不采用其评估协议。RAID 覆盖 11 个 LLMs + 多种 attack 手段，其 robustness evaluation framework 可提供更强验证。[R1+R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**未请求**（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4 分钟）。发现 2 critical + 4 warning + 9 info：\n\n**Critical:**\n- **前 3 页无任何 display item**（纯文字墙）。第一个 table（Table 1）在 p4，第一个 figure（Figure 1）在 p6。审稿人前 2 分钟内缺乏视觉锚点。**强烈建议在 p1-2 加入 pipeline 概览图或 teaser figure。**\n- **Page 8 过度拥挤**：3 个 table（Table 4/5/6）+ 1 个 figure（Figure 3），Figure 3 混淆矩阵数字极小。\n\n**Warning:**\n- Display item 分布严重不均：前 5 页仅 1 个 table，后 3 页 8 个 display items。\n- Page 5 纯文本页（§3.5 + §4 开头），形成额外文字断层。\n- 全文缺少方法概览图/架构图（3 个 figure 全为分析性图表）。\n- Figure 3 混淆矩阵字号远低于正文 70%，建议改用 figure*。\n\n**页数合规**：正文 pp.1-8，Limitations p.9 起，符合 EMNLP 2026 8 页限制。\n**匿名合规**：`\\usepackage[review]{acl}`，\"Anonymous ACL submission\"，未发现去匿名化内容。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n**Confidence: 4/5**\n\n**评分理由：**\n\n论文提出了一个新颖且有意义的任务形式化（递归生成深度的序数分类），构建了系统全面的 benchmark（180K, 3×3 grid），通过 Depth Degradation Atlas 和 EDD 指标提供了有价值的 empirical contribution。实验设计严谨，Limitations 诚实，附录极其详尽。\n\n但论文的核心瓶颈在于：\n\n1. **方法论贡献不足**：标准 RF + 标准统计特征，无算法创新，且与已有 Binoculars 特征无显著差异（p>0.05）。EMNLP 主会议期望至少在方法或理论层面有实质推进。\n\n2. **泛化严重受限**：cross-strategy d1-d3 仅 45.9%（接近 chance），14B EDD₀.₇₀=0。在 2026 年 7B-70B+ 为主流的背景下，≤1.5B 的结论实用价值有限。\n\n3. **Self-reference confound 膨胀 headline 数字**：1/3 in-distribution 结果存在系统偏差（4-11pp），headline 数字未充分修正。\n\n这些问题使论文距离 Conference 水平（4.0）有明显差距。但 task formalization 的新颖性、benchmark 的系统性、Atlas 的 empirical value 使其达到 Findings 水平（3.0）——贡献真实且可复现，对 model collapse / data provenance / AI text detection 社区有参考价值。\n\n**达到 Conference 水平的路径（供参考，非建议）：**\n- 在 7B+ 规模提供完整 3×3 grid 并分离 confounders\n- 引入超越标准 RF 的方法创新（如利用 LLM hidden states）或展示显著超越 Binoculars 的场景\n- 以 non-overlapping reference model 报告 conservative headline 数字\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 信息密度过高（10+ 数字）。建议精简至：问题定义 → 方法概要 → 最重要的 2-3 个 takeaway（优先报告 d1-d3 balanced accuracy）。当前 framing 暗示 pipeline 方法本身是贡献，但 Binoculars 平局表明真正贡献在 task formalization + Atlas。\n\n**§1 Introduction**: Narrative flow 清晰（recursive loop → depth matters → no ordinal estimation → our approach）。但 contributions 列表中\"statistical features dominated by the perplexity tail family\"容易被误读为特征设计创新，建议调整措辞为\"we find that...\"的 empirical finding 语气。\n\n**§2 Related Work**: 覆盖面广（model collapse theory、AI text detection、membership inference、adjacent tasks、ordinal classification、decoding strategy effects），但遗漏 Markovian Generation Chains (ICLR 2026) 是一个 gap。PAN 2026 / M4-SemEval 的讨论过于简略。\n\n**§3 Method**: 形式化清晰（Definition 1, §3.1）。Benchmark 构建合理但 LoRA 超参缺 ablation（r=16 是否 robust？）。19 特征的 VIF>10 应在此处注明而非推到 §4.2。EDD 定义（Eq. 1）形式正确但 τ=0.70 的选择需要更充分论证。\n\n**§4 Depth Degradation Atlas**: 系统映射是论文最强贡献。Feature importance 分析（§4.2）受共线性影响需 caveat。Strategy-dependent trajectories（§4.5）发现有价值。EDD analysis（§4.4）中 depth ceiling 发现重要但 monotonicity claim 应明确限定在 ≤1.5B 范围。\n\n**§5 Generalization and Robustness**: 覆盖全面但暴露了方法的核心局限。Table 4 的 Binoculars 对比是最大的方法论挑战。Cross-model transfer（§5.2）数字包含 self-reference confound。Cross-strategy transfer（§5.3）的 45.9% d1-d3 是严重的泛化警报。§5.4 的 14B 结果措辞已审慎（\"Preliminary\"）但 5 个 confounders 使结论几乎不可解读。\n\n**§6 Discussion and Conclusion**: 密度适当，PLM R²<0 洞察和 accumulation 数据是有价值的补充。但\"perplexity tail family dominates across all nine cells\"的 claim 需修饰——cross-strategy transfer 失败表明 dominance 是 strategy-entangled 的。\n\n**Limitations**: 诚实全面，覆盖了主要局限。建议增加：(1) Binoculars 平局的讨论；(2) multicollinearity 对 feature importance 的影响；(3) data generation seed 的 variance 未充分量化。\n\n**Ethics Statement**: 存在且合理，讨论了潜在滥用风险。\n\n**格式**: 页数合规（正文 8 页），匿名合规，引用格式统一。2 个 orphan bib entries 需清理。视觉审查发现前 3 页缺 figure、page 8 拥挤等布局问题（详见 Visual Layout Check 章节）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "report": "# 审稿报告 — Round 15 (Fresh Review)\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle), Long Paper\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**轮次**: Round 1, 1 轮收敛（交叉分享后关键问题达成共识）\n\n---\n\n## Summary\n\n论文将递归生成深度估计形式化为序数分类问题（d0-d3），构建了 180K 样本的 benchmark（3 model families × 3 decoding strategies × 4 depths），使用 19 个统计特征 + Random Forest 实现深度分类。主要贡献包括任务形式化、Depth Degradation Atlas（系统映射不同策略下的退化轨迹）和 EDD 指标（量化可区分深度范围）。In-distribution accuracy 69-86%（d1-d3: 59-82%），cross-model transfer 66.4%（d1-d3: 55.4%），cross-strategy 59.1%（d1-d3: 45.9%），14B preliminary 50.8%（EDD₀.₇₀=0）。\n\n---\n\n## Strengths\n\n**S1. 新颖且有意义的任务形式化。** 将深度估计从二元检测扩展为序数分类是自然且未被充分探索的方向。在 model collapse 日益受关注的背景下，区分\"生成了几轮\"比仅区分\"是否生成\"有更强的实用价值。Definition 1（§3.1）和 EDD 指标（§3.4）提供了清晰的形式化框架。[R1-S1, R2-S1 一致]\n\n**S2. 系统的实验设计和全面的泛化分析。** 3×3 model-strategy grid、cross-model/cross-strategy/cross-domain transfer、7-14B 规模探索、d0-d5 深度扩展、种子稳健性——分析轴覆盖广泛。29 个附录实验展现了严肃的实验态度和高复现性。[R1-S2/S4, R2-S2 一致]\n\n**S3. Depth Degradation Atlas 的系统映射。** §4 发现了解码策略诱导的质变差异：nucleus 保持单调衰减、temperature 引入 d1/d2 boundary inversion、top-k truncation 移除 depth-discriminative 低概率 tokens。这些发现对理解递归生成的统计机制有参考价值。[R1-S2, R2-S3 一致]\n\n**S4. Limitations 部分诚实全面。** 覆盖了 full-replacement vs accumulation、scale limitation、BOS vs prompted、reference model dependency、cross-strategy deployment constraint 等核心局限。学术诚实度值得肯定。[R2-S5]\n\n**S5. 引用质量高。** 74 篇引用中 63 篇 OpenAlex 验证通过，无伪造引用，所有 \\cite 均有对应 bib 条目。[R1-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [critical] Pipeline 缺乏算法创新，且与 Binoculars 无显著差异。**\n核心 pipeline 是 19 个标准统计特征（perplexity moments/quantiles、surprisal statistics、lexical diversity、n-gram repetition）+ 标准 Random Forest（200 trees, 5-fold CV），无任何算法层面创新。更严重的是，Binoculars 11-feat RF 达到 78.1%，与本文 19-feat RF 的 78.4% 无显著差异（p>0.05, Table 4）。Merged 30-feat 82.6% 说明信息互补而非本文特征优越；Binoculars 独有 5 特征的边际贡献 (+4.2pp) 反而大于本文独有 13 特征 (+2.5pp, Appendix B.26)。\n→ 论文的方法论贡献被大幅稀释。\"discriminative signal resides in feature design\"（Abstract）的 claim 恰好被 Binoculars 平局反驳。\n[R1-N1 + R2-N1 + R2-N2 一致, 交叉 AGREE]\n\n**C2. [critical] Cross-strategy 和 cross-scale 泛化严重不足，动摇方法实用性。**\n- Cross-strategy transfer d1-d3 仅 45.9%（chance 33%），出现 d1/d2 boundary inversion。z-score normalization 修复 logistic regression 但不修复 RF，说明不同策略产生结构性不同的 depth signal（§5.3）。\n- 14B cross-scale mean 50.8%，EDD₀.₇₀=0，5 个 confounders 未分离（§5.4）。\n- 两个问题叠加：在 unknown strategy + large scale 部署场景下，pipeline 有效性几乎不可预期。\n- 2026 年主流模型 7B-70B+，≤1.5B 结论实用参考价值有限。\n→ 这不仅是 limitation，而是动摇核心 claim 的根本质疑。\n[R1-N4 + R2-N3 + R2-W6 一致, 交叉 AGREE]\n\n**C3. [critical] Self-reference confound 使 1/3 in-distribution 结果存在系统性偏差。**\nPythia-1.4B 同时是 generator 和 reference model，Table 2 显示 Pythia 比 OLMo/GPT-2 XL 高 4-11pp。Appendix B.13 换用 GPT-2 XL reference 时 accuracy 降至 67.3%（−11pp）。Cross-model transfer 中 Pythia holdout 62.4% 低于 OLMo 69.2%——self-reference confound 传递到 transfer 场景。Table 2 的 † 脚注和 B.13 ablation 部分缓解但 headline 数字仍包含膨胀。\n[R1-N2 Must-Fix, R2 偏 Should-Fix; Director 裁定 Must-Fix — headline 数字直接受 confound 影响]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. d0 膨胀 headline metrics。** d0 recall >97%（本质是已解决的 binary detection）。Cross-model headline 66.4% 排除 d0 后降至 55.4%，cross-strategy 59.1% 降至 45.9%。论文已在括号内并列 d1-d3 数字但不够突出——Abstract 和 §6 首句仍以 4-class accuracy 领头。\n[R1-N3 Must-Fix, R2-W2 Should-Fix; Director 裁定 Should-Fix（高优先级）— 数据完整，问题在 framing]\n\n**W2. EDD 阈值 T=0.70 理论依据不足。** 借自 Hosmer & Lemeshow (2000) 的 binary logistic regression AUC 标准，迁移到 ordinal pairwise AUC 未被论证。T=0.80 时多个 cell 丢失 depth level，结论对阈值敏感。monotonicity assumption 在 14B 打破。\n[R1-W6 + R2-W4 一致, 交叉 AGREE]\n\n**W3. 多重共线性（VIF>10 for 14-16/19）与可解释性 claim 矛盾。** Gini importance 和 SHAP 在高共线性下不稳定，§4.2 的特征重要性排序可靠性存疑。Appendix B.2 的 permutation importance 部分缓解但 SHAP（TreeSHAP）同样受影响。\n[R1-W1, R2 交叉 AGREE]\n\n**W4. Full-replacement 设置与现实 accumulation 场景脱节。** 主实验无 accumulation 条件。§6 引用 pilot 数据（70.1%/69.1% vs 84.2%）但缺乏系统评估。Limitations 透明但主实验 gap 仍在。\n[R1-W3 + R2-W3 一致, 交叉 AGREE]\n\n**W5. LoRA 微调超参无 ablation。** r=16, α=32 的选择直接影响生成文本质量和 depth signatures，不同 LoRA 配置可能产生不同退化模式。\n[R1-W2, R2 交叉 AGREE]\n\n**W6. Abstract 信息密度过载。** 10+ 个数字，核心 message 被淹没。建议精简至 3-4 个最关键数字。\n[R2-W1, R1 交叉 AGREE]\n\n**W7. Cross-domain web 文本 FPR 偏高。** C4 34%, FineWeb 17%（Appendix B.11），template/SEO content 的 n-gram repetition 触发 false positive。正文未充分讨论。\n[R1-W4, R2 交叉 AGREE（修正\"单域\"表述）]\n\n**W8. 多重比较未校正。** 多组 pairwise comparisons 未做 Bonferroni/FDR 校正。实际影响可能有限但统计规范性不足。\n[R1-W5, R2 交叉 AGREE]\n\n### Minor\n\n- M1: 2 个 orphan bib entries (dsir2023, qurating2024)。[R1+R2 一致]\n- M2: Binary RF 500 trees vs 4-class RF 200 trees 未解释。[R1]\n- M3: 主文过度引用附录（§4-§6 几乎每段有 Appendix B.X），阅读碎片化。[R2]\n- M4: Figure 3 混淆矩阵数字极小，建议改用 figure* 全宽。[视觉审查]\n- M5: 引用 author 顺序 mismatch：alemohammad2024_mad、guo2024_biscope、hosmer2000。[R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下关键问题两位 Reviewer 达成完全共识：\n\n1. **Binoculars 平局 + 无算法创新** → 方法论贡献不足以支撑 Main Conference [R1-N1 = R2-N1/N2]\n2. **Cross-strategy/scale 泛化失败** → 实际部署价值受限 [R1-N4 = R2-N3/W6]\n3. **EDD 阈值缺乏理论依据** → 核心指标稳健性存疑 [R1-W6 = R2-W4]\n4. **d0 膨胀需处理**（严重程度有细微差异但问题本身无争议）[R1-N3 ≈ R2-W2]\n5. **Full-replacement 脱离现实** [R1-W3 = R2-W3]\n6. **论文定位为 Findings 更合适** [R1 Overall 3.0 = R2 Overall 3.0]\n\n## Reviewer Divergence [REBUT]\n\n1. **d0 膨胀的严重程度**：R1 列为 Must-Fix（headline 数字误导），R2 列为 Should-Fix（论文已并列报告 d1-d3）。\n   → Director 裁定：**Should-Fix（高优先级）**。论文确实在关键位置并列了 d1-d3 数字，但应将 d1-d3 作为主打而非补充。\n\n2. **Self-reference confound 严重程度**：R1 列为 Must-Fix（1/3 结果系统偏差），R2 认为 B.13 ablation 部分缓解。\n   → Director 裁定：**Must-Fix**。虽然 ablation 在附录中，但 headline 数字（Abstract, Table 2）直接受 confound 影响，需要在主文中报告 excluding-Pythia 的 conservative estimate。\n\n3. **Atlas 循环性（R2-W5）**：R1 [REBUT] 论证 Atlas 使用测量工具描述测量发现不构成循环，负面发现（某些特征不随 depth 单调变化）证明了非循环性。\n   → Director 裁定：**接受 R1 的 REBUT**。Atlas 的 methodology 可用于任何特征集，其发现（strategy-dependent trajectories、feature hierarchy shifts with depth）是 legitimate empirical contribution。此项不列为 weakness。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** 如果使用完全不同架构的 reference model（如 Mamba/RWKV），特征提取结果会如何？当前 ablation（B.13）仅在 Transformer 内部换模型。[R1-Q1]\n\n**Q2.** Perplexity tail features 捕获的是 depth-specific signature 还是仅仅是文本质量代理？depth-1 低质量文本与 depth-2 \"正常\"文本，特征能否区分？[R1-Q2]\n\n**Q3.** z-score normalization 修复 logistic regression 但不修复 RF 的根本原因是什么？是否说明 RF 学到了 strategy-specific 非线性边界？[R1-Q3]\n\n**Q4.** 14B 实验中 5 个 confounders 能否通过实验设计分离？例如用 14B reference model，或测试 Pythia-6.9B base（同架构无 instruction-tuning）。[R1-Q5]\n\n**Q5.** 19-feature pipeline 相对 Binoculars 的实际优势是什么？科学上无显著差异（p>0.05），工程优势（1 model vs 2 models）是否足够？[R2-Q2]\n\n**Q6.** 主 benchmark 仅 seed=42，能否提供 in-distribution multi-seed 结果？Appendix B.24 的 3 seeds 仅测 classifier seed，未测 data generation seed。[R2-Q4]\n\n**Q7.** surprisal variance 和 perplexity tail（如 p90_ppl）在信息论上有何区别？是否是同一信号的不同视角？[R2-Q5]\n\n---\n\n## Missing References\n\n**MR1. [critical]** Markovian Generation Chains in Large Language Models (arxiv:2603.11228, ICLR 2026)。直接研究 LLM 迭代生成的 Markov 链动态（convergence to fixed points、cycle behavior、decoding strategy 影响），与本文 recursive generation setup 和 strategy-dependent trajectory 发现高度相关。[R2 提出, R1 未独立验证真实性，建议作者核实]\n\n**MR2. [minor]** Min-K%++（Zhang et al., 2024）。Min-K% Prob 的改进版本，应作为更强的 membership inference baseline 考虑。[R1]\n\n**MR3. [minor]** RAID benchmark（Dugan et al., 2024）已引用但未解释为何不采用其评估协议。RAID 覆盖 11 个 LLMs + 多种 attack 手段，其 robustness evaluation framework 可提供更强验证。[R1+R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**未请求**（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4 分钟）。发现 2 critical + 4 warning + 9 info：\n\n**Critical:**\n- **前 3 页无任何 display item**（纯文字墙）。第一个 table（Table 1）在 p4，第一个 figure（Figure 1）在 p6。审稿人前 2 分钟内缺乏视觉锚点。**强烈建议在 p1-2 加入 pipeline 概览图或 teaser figure。**\n- **Page 8 过度拥挤**：3 个 table（Table 4/5/6）+ 1 个 figure（Figure 3），Figure 3 混淆矩阵数字极小。\n\n**Warning:**\n- Display item 分布严重不均：前 5 页仅 1 个 table，后 3 页 8 个 display items。\n- Page 5 纯文本页（§3.5 + §4 开头），形成额外文字断层。\n- 全文缺少方法概览图/架构图（3 个 figure 全为分析性图表）。\n- Figure 3 混淆矩阵字号远低于正文 70%，建议改用 figure*。\n\n**页数合规**：正文 pp.1-8，Limitations p.9 起，符合 EMNLP 2026 8 页限制。\n**匿名合规**：`\\usepackage[review]{acl}`，\"Anonymous ACL submission\"，未发现去匿名化内容。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n**Confidence: 4/5**\n\n**评分理由：**\n\n论文提出了一个新颖且有意义的任务形式化（递归生成深度的序数分类），构建了系统全面的 benchmark（180K, 3×3 grid），通过 Depth Degradation Atlas 和 EDD 指标提供了有价值的 empirical contribution。实验设计严谨，Limitations 诚实，附录极其详尽。\n\n但论文的核心瓶颈在于：\n\n1. **方法论贡献不足**：标准 RF + 标准统计特征，无算法创新，且与已有 Binoculars 特征无显著差异（p>0.05）。EMNLP 主会议期望至少在方法或理论层面有实质推进。\n\n2. **泛化严重受限**：cross-strategy d1-d3 仅 45.9%（接近 chance），14B EDD₀.₇₀=0。在 2026 年 7B-70B+ 为主流的背景下，≤1.5B 的结论实用价值有限。\n\n3. **Self-reference confound 膨胀 headline 数字**：1/3 in-distribution 结果存在系统偏差（4-11pp），headline 数字未充分修正。\n\n这些问题使论文距离 Conference 水平（4.0）有明显差距。但 task formalization 的新颖性、benchmark 的系统性、Atlas 的 empirical value 使其达到 Findings 水平（3.0）——贡献真实且可复现，对 model collapse / data provenance / AI text detection 社区有参考价值。\n\n**达到 Conference 水平的路径（供参考，非建议）：**\n- 在 7B+ 规模提供完整 3×3 grid 并分离 confounders\n- 引入超越标准 RF 的方法创新（如利用 LLM hidden states）或展示显著超越 Binoculars 的场景\n- 以 non-overlapping reference model 报告 conservative headline 数字\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 信息密度过高（10+ 数字）。建议精简至：问题定义 → 方法概要 → 最重要的 2-3 个 takeaway（优先报告 d1-d3 balanced accuracy）。当前 framing 暗示 pipeline 方法本身是贡献，但 Binoculars 平局表明真正贡献在 task formalization + Atlas。\n\n**§1 Introduction**: Narrative flow 清晰（recursive loop → depth matters → no ordinal estimation → our approach）。但 contributions 列表中\"statistical features dominated by the perplexity tail family\"容易被误读为特征设计创新，建议调整措辞为\"we find that...\"的 empirical finding 语气。\n\n**§2 Related Work**: 覆盖面广（model collapse theory、AI text detection、membership inference、adjacent tasks、ordinal classification、decoding strategy effects），但遗漏 Markovian Generation Chains (ICLR 2026) 是一个 gap。PAN 2026 / M4-SemEval 的讨论过于简略。\n\n**§3 Method**: 形式化清晰（Definition 1, §3.1）。Benchmark 构建合理但 LoRA 超参缺 ablation（r=16 是否 robust？）。19 特征的 VIF>10 应在此处注明而非推到 §4.2。EDD 定义（Eq. 1）形式正确但 τ=0.70 的选择需要更充分论证。\n\n**§4 Depth Degradation Atlas**: 系统映射是论文最强贡献。Feature importance 分析（§4.2）受共线性影响需 caveat。Strategy-dependent trajectories（§4.5）发现有价值。EDD analysis（§4.4）中 depth ceiling 发现重要但 monotonicity claim 应明确限定在 ≤1.5B 范围。\n\n**§5 Generalization and Robustness**: 覆盖全面但暴露了方法的核心局限。Table 4 的 Binoculars 对比是最大的方法论挑战。Cross-model transfer（§5.2）数字包含 self-reference confound。Cross-strategy transfer（§5.3）的 45.9% d1-d3 是严重的泛化警报。§5.4 的 14B 结果措辞已审慎（\"Preliminary\"）但 5 个 confounders 使结论几乎不可解读。\n\n**§6 Discussion and Conclusion**: 密度适当，PLM R²<0 洞察和 accumulation 数据是有价值的补充。但\"perplexity tail family dominates across all nine cells\"的 claim 需修饰——cross-strategy transfer 失败表明 dominance 是 strategy-entangled 的。\n\n**Limitations**: 诚实全面，覆盖了主要局限。建议增加：(1) Binoculars 平局的讨论；(2) multicollinearity 对 feature importance 的影响；(3) data generation seed 的 variance 未充分量化。\n\n**Ethics Statement**: 存在且合理，讨论了潜在滥用风险。\n\n**格式**: 页数合规（正文 8 页），匿名合规，引用格式统一。2 个 orphan bib entries 需清理。视觉审查发现前 3 页缺 figure、page 8 拥挤等布局问题（详见 Visual Layout Check 章节）。"
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-20T08:51:01.633754+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4821
}
```

</details>

---


### Assistant

_source line 1302 · 2026-05-20T08:51:10.184148+00:00_

审稿报告已投递至 Research Director。

**审稿完成摘要：**

- **Overall: 3.0 (Findings)**，两位 Reviewer 一致
- **3 个 Must-Fix**: (1) 无算法创新 + Binoculars 平局削弱方法贡献; (2) cross-strategy/scale 泛化严重不足; (3) self-reference confound 膨胀 headline 数字
- **8 个 Should-Fix**: d0 膨胀 framing、EDD 阈值理论薄弱、多重共线性、full-replacement 脱节、LoRA 无 ablation、Abstract 过载、web FPR 高、多重比较未校正
- **1 个关键遗漏引用**: Markovian Generation Chains (ICLR 2026)
- **视觉审查**: 前 3 页无 figure（文字墙）、缺 pipeline 概览图、page 8 拥挤
- **Issue Tracker**: 已更新 15 个新 issue + 历史 issue 状态同步

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 123

## Round 123

2 recorded events


### User

_source line 1303 · 2026-05-20T08:51:12.930218+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **N1 (Binoculars tie)**: [AGREE] — 与我的 N2 一致，merged 30-feature 82.6% 反而证明信息互补而非本文独特
- **N2 (Self-reference confound)**: [AGREE] — Pythia self-ref 导致 11pp 偏差，但论文 B.13 ablation 部分缓解
- **N3 (d0 inflation)**: [REBUT] — 论文已并列报告 d1-d3，属 Should-Fix 而非 Must-Fix
- **N4 (Cross-strategy + cross-scale failure)**: [AGREE] — 最严重问题，两者叠加使部署前景几乎不可预期
- **W1-W6**: 4 个 AGREE，1 个部分 REBUT (W3 generation protocol 描述不精确, W4 "single domain"不准确但高 FPR 关切有效)

两位 Reviewer 均给出 **3.0 (Findings)**，核心分歧仅在 d0 膨胀和 self-reference confound 的严重程度定级上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1304 · 2026-05-20T08:51:26.160295+00:00_

审稿报告已投递至 Research Director。

**审稿结论：Overall 3.0 — Findings**

圆桌会议完成情况：
- 2 名 Reviewer 独立初审 + 交叉分享回应，1 轮收敛
- 3 个 Must-Fix：(1) 无算法创新 + Binoculars 平局；(2) cross-strategy/scale 泛化严重不足；(3) self-reference confound 膨胀 headline
- 8 个 Should-Fix：d0 膨胀 framing、EDD 阈值理论薄弱、多重共线性、full-replacement 脱节、LoRA 无 ablation、Abstract 过载、web FPR 偏高、多重比较未校正
- 1 个 critical missing reference：Markovian Generation Chains (ICLR 2026)
- 视觉审查：前 3 页无 figure（文字墙）、page 8 过度拥挤、缺 pipeline 概览图
- Issue Tracker 已同步更新（13 个新 open issues + 历史 resolved issues 保留）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 124

## Round 124

64 recorded events


### User

_source line 1305 · 2026-05-20T13:59:12.896103+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recursive_gen_depth_est
- 论文路径: docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-06-15
- 补充材料: artifacts/supplementary/README.md

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-20T13:59:18.942282+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-20T13:59:18.943201+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-20T13:59:25.621016+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1309 · 2026-05-20T13:59:25.621462+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-20T13:59:32.450498+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1311 · 2026-05-20T13:59:32.501374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1312 · 2026-05-20T13:59:47.789630+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1313 · 2026-05-20T13:59:49.245358+00:00_

{"result":"# 项目 recursive_gen_depth_est 概况\n\n## 实验状态 (139 个)\n\n- **cross_model_olmo_temp09_001**: DONE (killed) — \n- **pythia_topk50_001**: DONE (success) — \n- **cross_model_gpt2xl_001**: DONE (success) — \n- **cross_model_olmo_002**: DONE (success) — \n- **pythia_temp09_001**: DONE (success) — \n- **mvp_pipeline_pythia_002**: DONE (success) — \n- **cross_model_olmo_001**: DONE (failed) — \n- **mvp_pipeline_qwen_base_004**: DONE (killed) — \n- **mvp_pipeline_pythia_001**: DONE (killed) — \n- **mvp_pipeline_base_002**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (killed) — \n- **mvp_pipeline_001**: DONE (killed) — \n- **mvp_pipeline_base_003**: DONE (killed) — \n- **mvp_pipeline_004**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- accum_v2_mix25（准备中）\n- accum_v2_mix50（准备中）\n\n## 近期结论\n- **binoculars_14b_topk50** (success): Binoculars cross-perplexity features provide complementary signal at 14B scale under top-k sampling when merged with 19 statistical features. Tests whether the merged feature gain (~+3.7pp at temp09) holds under the weakest decoding strategy. ← 基于 qwen25_14b_topk50\n  [binoculars_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/binoculars_14b_topk50/report/binoculars_14b_topk50_results.md)\n- **qwen25_14b_topk50** (success): Recursive generation depth signal persists at 14B scale under top-k sampling (k=50), achieving RF 4-class accuracy above 25% baseline. Top-k typically yields lowest accuracy across strategies; if signal persists even here, 14B scale-generality claim is robust. Directly addresses Dream worst review M3.\n  [qwen25_14b_topk50_analysis](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report/qwen25_14b_topk50_analysis_b7a903.md) | [qwen25_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report
…[truncated 1834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 1314 · 2026-05-20T13:59:49.396479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1315 · 2026-05-20T13:59:50.201102+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{theory}
39	
40	\input{atlas}
41	
42	\input{generalization}
43	
44	\input{discussion}
45	
46	\input{conclusion}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{section_appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-20T13:59:50.201551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/supplementary/README.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/supplementary/README.md"
  }
}
```

</details>

---


### Tool result

_source line 1317 · 2026-05-20T13:59:50.904892+00:00_

1	# Supplementary Material: Recursive Generation Depth Estimation
2	
3	## Repository Structure
4	
5	```
6	├── scripts/                    # Pipeline and evaluation scripts
7	│   ├── lora_finetune.py        # LoRA fine-tuning (r=16, α=32, 3 epochs)
8	│   ├── generate_next_depth.py  # BOS-seeded generation for next depth
9	│   ├── run_pipeline.sh         # End-to-end pipeline (Pythia nucleus)
10	│   ├── run_pipeline_*.sh       # Per-cell pipeline variants (9 cells)
11	│   ├── atlas_analysis.py       # Atlas feature importance analysis
12	│   ├── d4_extension_eval*.py   # Depth extension (d4-d5) evaluation
13	│   ├── baseline_*.py           # Baseline methods (CORAL, DivEye, CE, ppl regression, zero-shot LLM)
14	│   ├── detection_baselines.py  # DetectGPT / Min-K% Prob baselines
15	│   └── prompted_generation_eval.py  # Topic-seeded generation validation
16	├── src/                        # Core analysis modules
17	│   ├── atlas_v2.py             # 9-cell atlas construction and RF training
18	│   ├── cross_model_loo.py      # Leave-one-model-family-out transfer
19	│   ├── binary_pairwise_eval.py # Pairwise AUC for EDD computation
20	│   ├── wild_data_calibration.py # Cross-domain FPR (C4, FineWeb, WikiText)
21	│   ├── w2_domain_bias.py       # LOGO / seed-group domain bias control
22	│   └── curation_poc.py         # Depth-graduated curation probe
23	├── docs/paper/                 # LaTeX source
24	│   ├── main.tex                # Main document
25	│   ├── section_appendix.tex    # Appendix (B.1-B.21)
26	│   └── figures/                # PDF figures (4 main + appendix)
27	└── artifacts/                  # Experiment outputs and analysis
28	```
29	
30	## Data Access
31	
32	**Seed corpus**: Wikipedia subset (English), publicly available.
33	
34	**Generated data**: 180K samples across 9 model-strategy cells (3 models × 3 strategies × 4 depths × 5,000 samples). Feature files (19-dimensional vectors per passage) will be released upon acceptance.
35	
36	**Models used**:
37	
…[truncated 3067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 1318 · 2026-05-20T13:59:50.905396+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1319 · 2026-05-20T13:59:50.955979+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-20T13:59:59.849476+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-20T13:59:59.900105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-20T14:00:06.111554+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR May cycle",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR May cycle",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1323 · 2026-05-20T14:00:07.969589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1324 · 2026-05-20T14:00:08.271108+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification, constructing a 180K-passage benchmark spanning three model families, three decoding strategies, and four depths under controlled full-replacement recursive chains at the 1--1.5B scale.
4	A Random Forest over statistical features dominated by the perplexity tail family achieves 69--86\% across nine model--strategy cells; convergence of RF, XGBoost, and LightGBM confirms that discriminative signal resides in perplexity distributional statistics, as independently confirmed by Binoculars feature convergence (78.1\% vs.\ 78.4\%, $p{>}0.05$).
5	Excluding the trivially separable human-written class (d0 recall ${>}$97\%), d1--d3 balanced accuracy ranges from 59\% to 82\%.
6	Cross-model transfer reaches 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, and cross-strategy transfer 59.1\% (d1--d3: 45.9\%); the gap reveals that decoding strategies induce structurally distinct degradation trajectories, formalized via the \emph{Effective Discriminable Depth} (EDD) metric ($\mathrm{EDD}_{0.70}{=}4$ for all three families); preliminary 14B observations show above-chance accuracy (mean 50.8\%, $2{\times}$ chance) but $\mathrm{EDD}_{0.70}{=}0$, indicating adjacent-depth discrimination does not survive the scale transition.
7	Perturbation-based and membership inference baselines (29--33\%) fall far below our pipeline; cross-perplexity features (Binoculars) converge to matching performance (78.1\% vs.\ 78.4\%), and merging both feature sets yields 82.6\%, decomposing the depth signal into perplexity displacement, distributional shape, and cross-model divergence channels.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1325 · 2026-05-20T14:00:08.321752+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1326 · 2026-05-20T14:00:08.674990+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	We study this question under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination typically involves partial mixing (accumulation), where synthetic and human data co-exist at unknown proportions; the full-replacement setting provides an upper bound on depth signal strength, and we discuss implications for accumulation settings in \S\ref{sec:discussion}.
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
11	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
12	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
13	No exi
…[truncated 3713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1327 · 2026-05-20T14:00:08.675339+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1328 · 2026-05-20T14:00:08.725838+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 6300 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-20T14:00:19.299984+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR May cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines for the ARR May cycle:

## Key Submission Guidelines for EMNLP 2026

EMNLP 2026 invites the submission of long and short papers featuring substant
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 13188
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-20T14:00:25.879665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-20T14:00:26.833794+00:00_

1	\subsection{Theoretical Grounding}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed by its dominance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), so EDD should decrease with scale.
15	Qwen2.5-14B confirms this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B), while d1--d3 AUCs remain above 0.70 (\S\ref{sec:gen:crossscale}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.
20	GPT-2~XL confirms this: temperature d1 median \texttt{p90\_ppl} (92.
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-20T14:00:26.834216+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-20T14:00:27.286323+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells at the 1--1.5B parameter scale, evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}1{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: MAE\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references (Appendix~\ref{app:ref_ablation}). Cross-cel
…[truncated 9236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-20T14:00:27.286705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-20T14:00:27.839249+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares methods across all 9 cells.
10	RF, XGBoost, and LightGBM converge within 0.4\,pp (feature-determined ceiling); CORAL \cite{coral2020} and DivEye \cite{diveye2026} match within 0.6\,pp on Pythia nucleus ($p{>}0.05$).
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA) underperforms RF by 16--32\,pp (d2 recall 8.4\%); RoBERTa-DCOL (ordinal contrastive; 64.5\%) narrows the gap but remains 14\,pp below RF.
14	
15	\paragraph{Binary detectors and membership inference.}
16	Perturbation-based (DetectGPT, 28.8\%) and membership-inference (Min-K\% Prob, 33.2\%; Min-K\%++ \cite{zhang2024_minkpp} comparable) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); CORAL calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%).
17	Binoculars \cite{binoculars2024}, calibrated with 11-feature RF on cross-perplexity scores, matches within 0.3\,pp (78.1\% vs.\ 78.4\%, $p{>}0.05$); merging all 30 features yields 82.6\% (+4.2\,pp; Appendix~\ref{app:feature_ablation_bino}).
18	Our pipeline needs only a single 1.4B reference model vs.\ Binoculars' 1.8B observer--performer pair.
19	
20	\paragraph{Surface-text ablation.}
21	Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (best 36.2\%; Appendix~\ref{app:zeroshot_prompt}) also fail; depth signal resides in distributional statistics inaccessible from surface text.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\caption{Method comparison (RF mean across 9 cells, 5-fold CV). Chance = 25\% / 33.3\% (d1--d3). $^\dagger$Adapted from binary detection; Binocular
…[truncated 4280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1336 · 2026-05-20T14:00:27.839635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-20T14:00:28.342052+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	Excluding trivially separable d0 (recall ${>}$97\%), d1--d3 balanced accuracy reaches 59--82\% across nine cells, with the perplexity tail family dominating ($\mathrm{EDD}_{0.70}{=}4$); cross-model transfer 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, perturbation/MIA baselines 30--35\%.
5	Pilot accumulation ($-$14 to $-$15\,pp vs.\ 84.2\% full-replacement) and preliminary 14B ($\mathrm{EDD}_{0.70}{=}0$, confounded) observations show the signal attenuates but persists above chance ($2.8{\times}$).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1338 · 2026-05-20T14:00:28.392706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-20T14:00:29.246803+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	All experiments use full-replacement recursive chains, where each depth fully replaces the prior training corpus. Real-world contamination typically involves accumulation, where synthetic and human data co-exist at unknown proportions across iterations \cite{gerstgrasser2024_accumulate}. Under accumulation, depth signal should attenuate because each generation retains human-originated distributional properties. Our results therefore represent an upper bound on feature separability; extending the framework to accumulation settings, where depth becomes a continuous mixing parameter, is a priority for future work.
6	Segment-level estimation in mixed-depth documents remains open (Appendix~\ref{app:mixed_depth}), as our framework assumes uniform depth per passage.
7	
8	\paragraph{Controlled experimental setting.}
9	The primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination.
10	Domain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\%) matches standard CV (72.0\%), seed-group prediction is at chance (10.2\%; Appendix~\ref{app:domain_bias}).
11	Cross-scale experiments (7--14B, \S\ref{sec:gen:crossscale}) show signal that attenuates with scale; at 14B, d0/d1 separability nearly vanishes ($\mathrm{EDD}_{0.70}{=}0$) while d1--d3 discrimination persists; this constitutes a boundary condition for the current feature set (confounded by five factors; Appendix~\ref{app:cross_scale_confounds}).
12	
13	\paragraph{Cross-strategy deployment constraint.}
14	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
15	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random 
…[truncated 6362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-20T14:00:29.399006+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit anonymity guidelines author instructions",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit anonymity guidelines author instructions",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-20T14:00:36.680773+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit anonymity guidelines author instructions"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results, here's comprehensive information about ACL Rolling Review 2026 submission requirements:

## Page Limits

Short papers have a maximum of 4 content pages, and long papers have a maximum of 8 c
…[truncated 1396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 7281
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-20T14:00:53.126103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1343 · 2026-05-20T14:00:53.830792+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad} and Markovian generation chains \cite{geng2026_markovian}.
6	Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
7	Mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, data scaling under constraint \cite{muennighoff2023scaling}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence analysis \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026} are active areas.
8	\citet{kazdan2025_collapse_or_thrive} systematically compare training workflows and show that data accumulation avoids collapse while pure replacement does not; \citet{suresh2025_rate_collapse} characterize the rate of collapse for fundamental distributions under recursive maximum-likelihood estimation.
9	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier that reveals strategy-dependent trajectories and
…[truncated 3775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-20T14:00:53.981844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-20T14:00:54.033179+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	All experiments use full-replacement recursive chains, where each depth fully replaces the prior training corpus. Real-world contamination typically involves accumulation, where synthetic and human data co-exist at unknown proportions across iterations \cite{gerstgrasser2024_accumulate}. Under accumulation, depth signal should attenuate because each generation retains human-originated distributional properties. Our results therefore represent an upper bound on feature separability; extending the framework to accumulation settings, where depth becomes a continuous mixing parameter, is a priority for future work.
6	Segment-level estimation in mixed-depth documents remains open (Appendix~\ref{app:mixed_depth}), as our framework assumes uniform depth per passage.
7	
8	\paragraph{Controlled experimental setting.}
9	The primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination.
10	Domain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\%) matches standard CV (72.0\%), seed-group prediction is at chance (10.2\%; Appendix~\ref{app:domain_bias}).
11	Cross-scale experiments (7--14B, \S\ref{sec:gen:crossscale}) show signal that attenuates with scale; at 14B, d0/d1 separability nearly vanishes ($\mathrm{EDD}_{0.70}{=}0$) while d1--d3 discrimination persists; this constitutes a boundary condition for the current feature set (confounded by five factors; Appendix~\ref{app:cross_scale_confounds}).
12	
13	\paragraph{Cross-strategy deployment constraint.}
14	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
15	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random 
…[truncated 6362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1346 · 2026-05-20T14:00:54.033689+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1347 · 2026-05-20T14:00:54.084193+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1348 · 2026-05-20T14:01:00.961863+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-20T14:01:01.464719+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-20T14:01:01.465182+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-20T14:01:01.918987+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-20T14:01:02.070655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-20T14:01:02.122926+00:00_

1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\t
…[truncated 7663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-20T14:01:06.606927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-20T14:01:07.060444+00:00_

1	issues:
2	# ============================================================
3	# CRITICAL ISSUES (Round 15 — Fresh Review)
4	# ============================================================
5	
6	- id: R15-N1
7	  summary: Pipeline 缺乏算法创新，19-feat RF 与 Binoculars 11-feat RF 无显著差异 (78.4% vs 78.1%, p>0.05)
8	  category: method
9	  severity: critical
10	  status: open
11	  first_raised_round: 15
12	  last_seen_round: 15
13	  mentions:
14	  - round: 15
15	    reviewers: [1, 2]
16	    note: "R1-N1 + R2-N1 + R2-N2 一致。Binoculars 平局 + 标准 RF/统计特征无算法创新。Merged 30-feat 82.6% 说明互补而非本文特征优越。"
17	  action_items: []
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: R15-N2
22	  summary: Cross-strategy (d1-d3 45.9%) 和 cross-scale (14B EDD=0, mean 50.8%) 泛化严重不足
23	  category: experiment
24	  severity: critical
25	  status: open
26	  first_raised_round: 15
27	  last_seen_round: 15
28	  mentions:
29	  - round: 15
30	    reviewers: [1, 2]
31	    note: "R1-N4 + R2-N3 + R2-W6 一致。Cross-strategy d1-d3 接近 chance; 14B 5个confound未分离; 不同策略产生结构性不同的 depth signal。"
32	  action_items: []
33	  resolution: ""
34	  resolution_round: null
35	
36	- id: R15-N3
37	  summary: Self-reference confound — Pythia 同时做 generator 和 reference model，1/3 结果存在系统偏差 (4-11pp advantage)
38	  category: experiment
39	  severity: critical
40	  status: open
41	  first_raised_round: 15
42	  last_seen_round: 15
43	  mentions:
44	  - round: 15
45	    reviewers: [1, 2]
46	    note: "R1-N2 Must-Fix, R2 认为 B.13 ablation 部分缓解偏 Should-Fix。Director 裁定 Must-Fix: headline 数字包含 confound 膨胀。"
47	  action_items: []
48	  resolution: ""
49	  resolution_round: null
50	
51	# ============================================================
52	# SHOULD-FIX ISSUES (Round 15)
53	# ============================================================
54	
55	- id: R15-W1
56	  summary: d0 膨胀 headline metrics — cross-model d1-d3 仅 55.4% (报告 66.4%), cross-strategy d1-d3 仅 45.9% (报告 59.1%)
57	  category: writing
58	  severity: warning
59	  status: open
60	  first_
…[truncated 13033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1356 · 2026-05-20T14:01:07.060927+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool call

_source line 1357 · 2026-05-20T14:01:07.663537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "offset": "150"
  }
}
```

</details>

---


### Tool result

_source line 1358 · 2026-05-20T14:01:07.965964+00:00_

150	
151	\paragraph{Cross-$\tau$ non-transferability.}
152	Leave-one-$\tau$-out transfer yields mean accuracy of 46.7\% with mean d1v2 AUC of 0.319 (Table~\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\%; \S\ref{sec:gen:crossstrategy}).
153	Holdout $\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.
154	This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.
155	
156	\paragraph{Ecological validity.}
157	On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
158	On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.
159	
160	\begin{table}[h]
161	\centering
162	\small
163	\caption{Within-$\tau$ 4-class classification (Pythia-1.4B, 5-fold CV). d$i$v$j$: pairwise AUC for depth $i$ vs.\ depth $j$.}
164	\label{tab:multi_tau_within}
165	\resizebox{\columnwidth}{!}{%
166	\begin{tabular}{@{}lcccc@{}}
167	\toprule
168	$\tau$ & 4-class acc (\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\
169	\midrule
170	0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\
171	0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\
172	0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\
173	1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	\begin{table}[h]
179	\centering
180	\small
181	\caption{Cross-$\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}
182	\label{tab:multi_tau_cross}
183	\begin{tabul
…[truncated 53627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 1359 · 2026-05-20T14:01:09.886999+00:00_

&lt;persisted-output>
Output too large (45.9KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-director-79bccd15/c3c45b39-ecc5-4082-b656-bec3ca7f4ace/tool-results/toolu_01R9F255ynfohA2fGKimrccu.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md:138:外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_3.md:147:外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_12.md:152:外部审稿：**未请求**（项目未配置 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_6.md:134:外部审稿：未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_11.md:225:**状态**: 未请求（项目未启用外部审稿 `external_review.paperreview_ai.enabled = false`）
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_4.md:148:外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_2.md:138:外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:4:[Omitted long matching line]
...

…[truncated 19 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 2826
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-20T14:01:38.310852+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1361 · 2026-05-20T14:02:04.347444+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26036
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-20T14:02:04.399104+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
  "director_session_key": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-06-15\n- **页数限制**: 长文 8 页正文（参考文献不限；Limitations 和 Ethics 不计入页数）\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（提交必须匿名化）\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 主文件: `docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n- 补充材料: `artifacts/supplementary/README.md`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 实验方法论与统计分析\n- 180K benchmark 构建的科学性（LoRA 微调 pipeline、BOS-seeded generation 的影响）\n- 19 特征 RF pipeline 的统计合理性：多重共线性（VIF>10 for 14-16/19 features）对 Gini/SHAP importance 的影响\n- 5-fold CV 设计：是否存在数据泄露（跨深度无 passage lineage）\n- 多重比较是否需要校正（论文脚注声明 p-values 为 exploratory）\n\n### 2. Self-Reference Confound\n- Pythia-1.4B 同时做 generator 和 reference model（1/3 结果），4-11pp 优势\n- 这对 headline 数字和 cross-cell 比较的影响程度\n- Appendix B.13 ablation 是否充分缓解\n\n### 3. 泛化实验\n- Cross-model transfer (66.4%, d1-d3: 55.4%) 的实际意义\n- Cross-strategy transfer (59.1%, d1-d3: 45.9%) — 是否接近 chance (33%)？\n- Cross-scale (14B: EDD=0, mean 50.8%) — 5 个 confounds 是否致命？\n- Cross-domain (arXiv 74.1%) 和 wild-data FPR (C4 34%, FineWeb 17%)\n\n### 4. EDD 指标\n- T=0.70 阈值从 binary AUC 标准迁移的合理性\n- 阈值敏感性：T=0.80 时多个 cell 丢失 depth level\n- Monotonicity 假设的限制（14B 和 cross-strategy 违反）\n\n### 5. Baseline 比较\n- 与 Binoculars 11-feat RF 的关系：78.1% vs 78.4% (p>0.05)——如果两个独立特征集达到相同性能，方法贡献在哪里？\n- Merged 30-feat 82.6% 说明什么？\n- DeBERTa/RoBERTa end-to-end 为何大幅落后 RF？\n\n### 6. 格式合规\n- 8 页正文限制\n- 匿名化\n- Limitations 和 Ethics 是否齐全\n\n请按以下结构输出你的审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)\n4. **Questions** (给作者的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Minor Issues** (格式、typo 等)\n7. **Overall Assessment** (评分 + 理由)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
    "director_session_key": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-06-15\n- **页数限制**: 长文 8 页正文（参考文献不限；Limitations 和 Ethics 不计入页数）\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（提交必须匿名化）\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 主文件: `docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n- 补充材料: `artifacts/supplementary/README.md`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 实验方法论与统计分析\n- 180K benchmark 构建的科学性（LoRA 微调 pipeline、BOS-seeded generation 的影响）\n- 19 特征 RF pipeline 的统计合理性：多重共线性（VIF>10 for 14-16/19 features）对 Gini/SHAP importance 的影响\n- 5-fold CV 设计：是否存在数据泄露（跨深度无 passage lineage）\n- 多重比较是否需要校正（论文脚注声明 p-values 为 exploratory）\n\n### 2. Self-Reference Confound\n- Pythia-1.4B 同时做 generator 和 reference model（1/3 结果），4-11pp 优势\n- 这对 headline 数字和 cross-cell 比较的影响程度\n- Appendix B.13 ablation 是否充分缓解\n\n### 3. 泛化实验\n- Cross-model transfer (66.4%, d1-d3: 55.4%) 的实际意义\n- Cross-strategy transfer (59.1%, d1-d3: 45.9%) — 是否接近 chance (33%)？\n- Cross-scale (14B: EDD=0, mean 50.8%) — 5 个 confounds 是否致命？\n- Cross-domain (arXiv 74.1%) 和 wild-data FPR (C4 34%, FineWeb 17%)\n\n### 4. EDD 指标\n- T=0.70 阈值从 binary AUC 标准迁移的合理性\n- 阈值敏感性：T=0.80 时多个 cell 丢失 depth level\n- Monotonicity 假设的限制（14B 和 cross-strategy 违反）\n\n### 5. Baseline 比较\n- 与 Binoculars 11-feat RF 的关系：78.1% vs 78.4% (p>0.05)——如果两个独立特征集达到相同性能，方法贡献在哪里？\n- Merged 30-feat 82.6% 说明什么？\n- DeBERTa/RoBERTa end-to-end 为何大幅落后 RF？\n\n### 6. 格式合规\n- 8 页正文限制\n- 匿名化\n- Limitations 和 Ethics 是否齐全\n\n请按以下结构输出你的审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)\n4. **Questions** (给作者的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Minor Issues** (格式、typo 等)\n7. **Overall Assessment** (评分 + 理由)"
  }
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-20T14:02:25.781784+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21382
}
```

</details>

---


### Tool call

_source line 1364 · 2026-05-20T14:02:25.933011+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
  "director_session_key": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 相关工作**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-06-15\n- **页数限制**: 长文 8 页正文（参考文献不限；Limitations 和 Ethics 不计入页数）\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（提交必须匿名化）\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 主文件: `docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n- 补充材料: `artifacts/supplementary/README.md`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性与方法贡献\n- \"Recursive generation depth estimation\" 作为新任务的价值：是否真的是新问题，还是 binary detection 的简单扩展？\n- Pipeline 贡献：19-feat RF 是标准特征 + 标准分类器，Binoculars 11-feat RF 达到相同性能 (p>0.05)。核心贡献到底是什么？\n- EDD 指标的价值：作为新度量是否有足够的理论和实用支撑？\n- 论文自称 \"contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty\"——这种定位在 EMNLP 是否足够？\n\n### 2. Related Work 覆盖\n- Model collapse 文献是否完整（特别是 2025-2026 最新工作）\n- AI text detection 文献的覆盖范围\n- 是否遗漏了与 depth estimation / iterative generation / data provenance 直接相关的工作\n- 引用是否真实（请尽可能验证关键引用的存在性和准确性）\n- 使用 web_search 验证你不确定的引用\n\n### 3. 论文组织与写作质量\n- Abstract：信息密度是否过载（10+ 数字）？核心 message 是否清晰？\n- Introduction：motivation 和 contribution 是否清晰陈述？\n- 主文与附录的平衡：是否过度依赖附录（§4-§6 几乎每段引用 Appendix B.X）？\n- Discussion/Conclusion 的深度：是否充分讨论了 limitations 和 future directions？\n- d0 膨胀：headline metrics 是否被 d0 recall (>97%) 系统性膨胀？报告方式是否诚实？\n\n### 4. Full-Replacement vs Accumulation\n- 论文只研究 full-replacement 设置，现实中主要是 accumulation\n- 论文 Limitations 中的声明是否足够？\n- Discussion 中提到的 pilot accumulation 数据（-14 to -15pp vs 84.2%）是否应在主实验中呈现？\n\n### 5. 整体叙事\n- 论文的核心 claim 是什么？实验结果是否支持这些 claim？\n- 14B 结果 (EDD=0) 是否 undermine 了论文的核心叙事？\n- 论文在 positive results 和 negative results 之间是否保持了适当平衡？\n\n### 6. 格式合规\n- 8 页正文限制\n- 匿名化检查\n- Limitations 和 Ethics 完整性\n\n请按以下结构输出你的审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)\n4. **Questions** (给作者的问题)\n5. **Missing References** (遗漏的重要相关工作，请用 web_search 验证)\n6. **Minor Issues** (格式、typo 等)\n7. **Overall Assessment** (评分 + 理由)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
    "director_session_key": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 相关工作**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-06-15\n- **页数限制**: 长文 8 页正文（参考文献不限；Limitations 和 Ethics 不计入页数）\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（提交必须匿名化）\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 主文件: `docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n- 补充材料: `artifacts/supplementary/README.md`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性与方法贡献\n- \"Recursive generation depth estimation\" 作为新任务的价值：是否真的是新问题，还是 binary detection 的简单扩展？\n- Pipeline 贡献：19-feat RF 是标准特征 + 标准分类器，Binoculars 11-feat RF 达到相同性能 (p>0.05)。核心贡献到底是什么？\n- EDD 指标的价值：作为新度量是否有足够的理论和实用支撑？\n- 论文自称 \"contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty\"——这种定位在 EMNLP 是否足够？\n\n### 2. Related Work 覆盖\n- Model collapse 文献是否完整（特别是 2025-2026 最新工作）\n- AI text detection 文献的覆盖范围\n- 是否遗漏了与 depth estimation / iterative generation / data provenance 直接相关的工作\n- 引用是否真实（请尽可能验证关键引用的存在性和准确性）\n- 使用 web_search 验证你不确定的引用\n\n### 3. 论文组织与写作质量\n- Abstract：信息密度是否过载（10+ 数字）？核心 message 是否清晰？\n- Introduction：motivation 和 contribution 是否清晰陈述？\n- 主文与附录的平衡：是否过度依赖附录（§4-§6 几乎每段引用 Appendix B.X）？\n- Discussion/Conclusion 的深度：是否充分讨论了 limitations 和 future directions？\n- d0 膨胀：headline metrics 是否被 d0 recall (>97%) 系统性膨胀？报告方式是否诚实？\n\n### 4. Full-Replacement vs Accumulation\n- 论文只研究 full-replacement 设置，现实中主要是 accumulation\n- 论文 Limitations 中的声明是否足够？\n- Discussion 中提到的 pilot accumulation 数据（-14 to -15pp vs 84.2%）是否应在主实验中呈现？\n\n### 5. 整体叙事\n- 论文的核心 claim 是什么？实验结果是否支持这些 claim？\n- 14B 结果 (EDD=0) 是否 undermine 了论文的核心叙事？\n- 论文在 positive results 和 negative results 之间是否保持了适当平衡？\n\n### 6. 格式合规\n- 8 页正文限制\n- 匿名化检查\n- Limitations 和 Ethics 完整性\n\n请按以下结构输出你的审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)\n4. **Questions** (给作者的问题)\n5. **Missing References** (遗漏的重要相关工作，请用 web_search 验证)\n6. **Minor Issues** (格式、typo 等)\n7. **Overall Assessment** (评分 + 理由)"
  }
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-20T14:02:27.448087+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1515
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-20T14:02:37.748863+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 独立初审",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 独立初审",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-20T14:02:37.749286+00:00_

Next wakeup scheduled for 14:07:00 (in 262s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1368 · 2026-05-20T14:02:40.643510+00:00_

两位 Reviewer 正在独立初审中，约 4-5 分钟后检查进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 125

## Round 125

4 recorded events


### User

_source line 1369 · 2026-05-20T14:09:40.321056+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性 + 实验设计

**论文**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**Venue**: EMNLP 2026 (ARR May cycle)

---

## 1. Summary

本文将递归生成深度估计形式化为序数分类问题，构建了 180K 段落基准（3 个模型族 × 3 种解码策略 × 4 个深度 × 5K 样本），提取 19 维参考模型困惑度统计特征，用随机森林分类器在受控的全替换递归链上达到 69–96% 四分类精度。论文提出 Effective Discriminable Depth (EDD) 指标量化可辨识深度边界，并报告了跨模型、跨策略、跨规模的泛化实验。问题定义新颖、实验规模可观，但 self-reference confound 膨胀了核心数字、严重多重共线性动摇了特征重要性叙事、泛化实验在深层深度接近 chance，限制了主会议级别的 claim 强度。

## 2. Strengths

**S1. 新颖且动机充分的问题定义。** 将 AI 文本检测从 binary（human vs. machine）推向 ordinal depth estimation 是一个有意义的学术跨步。现有检测方法将所有 d≥1 合并，而本文论证了深度作为连续量的重要性——这对理解 model collapse 过程和数据策展都有实际价值。

**S2. 大规模受控基准构建。** 180K 样本的 9-cell 设计（§3.2）系统地控制了模型族、解码策略和生成深度三个维度。全替换递归链（full-replacement）提供了深度信号的上界，实验设计清晰。每 cell 5K 样本 × 4 深度，配合 5-fold stratified CV，样本量充分。

**S3. EDD 指标的概念贡献。** Definition 1（§3.3）将 pairwise AUC 整合为单一可比较的 depth discriminability 指标，为不同配置间的系统比较提供了标准化度量。这一概念工具对后续研究有参考价值。

**S4. 极为详尽的附录。** 21 个 appendix section（B.1–B.28+）覆盖了 LoRA 超参、permutation importance、per-class recall、feature trajectory、cross-seed replication、wild-data calibration、instruction-tuning ablation、Binoculars 分解、prompted generation 等。实验透明度在同类工作中属上乘。

**S5. 跨模型 feature importance 的收敛发现。** §4.2 报告的 perplexity tail 特征族在所有 9 cell 中一致主导，cross-model feature-rank Spearman ρ = 0.866（§4.2），表明深度退化存在跨架构的统计规律性。

**S6. 引用覆盖全面。** 74 篇参考文献覆盖 model collapse 理论（Shumailov, Dohmatob, Alemohammad）、检测方法（Binoculars, DetectGPT, Min-K%）、ordinal classification（CORAL, CLOC）、以及最新 2025–2026 工作。引用核查显示 62/74 在线可验证，8 篇未找到（多为 2025–2026 极新 preprint），无伪造引用。

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] Self-Reference Confound 膨胀核心数字**
- 具体位置：Table 2（p.6）, §4.1, Table 2 脚注 ¹, Appendix B.13
- 问题：Pythia-1.4B 同时担任 generator 和 reference model（3/9 cells），Table 2 脚注 ¹ 承认"Self-reference accuracy (Pythia-1.4B is both generator and reference model), 4–11 pp advantage over cross-model references"。Abstract 和 §1 的 headline 数字（"achieves 69–96% across nine model-strategy cells"）未做任何修饰地包含了这些膨胀 cell。Appendix B.13 的 ablation 显示换用 GPT-2/OLMo 作 reference 后 Pythia 精度下降至 78.6 ± 0.6（GPT-NeOX）/ 74.5 ± 0.7（OLMo）/ 67.3 ± 0.7（GPT-2），说明 4–11pp 优势中有实质部分来自 self-reference 而非深度信号。
- 为什么影响接收：论文的核心 claim——"statistical fingerprints discriminate recursive depth"——与 self-reference signal 混淆。读者无法从当前呈现中判断深度信号在排除 self-reference 后的真实强度。如果 Pythia cells 移除，headline range 下限会明显上移，但上限（96%）可能同样受影响。
- 建议修改方向：(1) 主文应报告 **排除 self-reference cells 后的** 汇总统计（OLMo + GPT-2 XL 的 6/9 cells）；(2) Abstract/§1 的 headline 数字应明确区分 self-reference 和 cross-model 情况；(3) 或者统一使用非 self-reference 配置（如 Pythia cells 也用 OLMo-1B 作 reference）重新报告 Table 2。

**N2 [critical] 严重多重共线性动摇特征重要性叙事**
- 具体位置：§4.2（"VIF > 10 for 14–16 of 19 features; effective independent dimensionality is ~3–5"）, Figure 1, Table 3
- 问题：论文承认 19 个特征中 14–16 个 VIF > 10，有效独立维度仅 3–5。但 §4 的整个 "Depth Degradation Atlas" 叙事——perplexity tail 主导、surprisal variance 次之、group-level dominance pattern——全部基于 Gini importance（Figure 1, Table 3）和 SHAP（Appendix B.2）。在 VIF > 10 的条件下，Gini importance 对共线特征的分配是任意的：两个高度相关的特征会互相分割 importance，导致排名不稳定。论文声称"RF is robust to multicollinearity for prediction"（§4.2），这对 **预测精度** 成立，但对 **特征重要性解释** 不成立。Appendix B.2 的 permutation importance 验证同样受共线性影响（correlated features 可互相替代）。
- 为什么影响接收：§4 的 feature importance 分析是论文的核心贡献之一（title 即 "Statistical Fingerprints"）。如果 importance ranking 在共线性下不可靠，"perplexity tail dominates" 的核心 narrative 就缺乏充分支撑。读者无法确信换一组等价但正交化的特征后，同样的 pattern 是否成立。
- 建议修改方向：(1) 对 19 特征做 PCA 或 clustering 后在正交/去相关空间中重新计算 importance；(2) 使用 conditional permutation importance（Strobl et al., 2008）或 SHAP interaction values 在共线性下提供更稳健的归因；(3) 至少在主文中明确声明 "feature importance rankings should be interpreted at the group level (perplexity tail vs. surprisal vs. lexical vs. repetition) rather than individual feature level" 并提供 group-level ablation（即移除整个特征族后的 accuracy drop）。Appendix B.26 部分做了 Binoculars feature group 分解，但未对自身 19 特征做类似的 group ablation。

**N3 [critical] Cross-Strategy Transfer 深层深度接近 Chance**
- 具体位置：Table 6（p.8）, §5.3
- 问题：Cross-strategy transfer（leave-one-strategy-out）总体 59.1%，但 d1–d3 仅 45.9%。对 3 类分类（d1–d3），chance = 33%，45.9% 仅高出 chance 12.9pp。论文承认 "two-stage pipeline recovers 11.5 pp"（§5.3），但即使加回仍远低于 within-strategy baseline（~80%+）。更关键的是，d0 recall ≥89% 严重拉高了 overall accuracy，掩盖了 d1–d3 的弱识别力。
- 为什么影响接收：如果 statistical fingerprints 是 strategy-specific 的，那么在实际场景中（不知道对方用了什么解码策略），方法的深层深度辨识力极为有限。这从根本上制约了 §1 声称的 "depth estimation" 的普适性。论文标题暗示了 general-purpose 的能力（"How Deep Is Your Data?"），但实际上 d1–d3 的跨策略表现仅比随机好 ~13pp。
- 建议修改方向：(1) 在 Abstract/Introduction 中明确限定 claim 为 within-strategy 或 known-strategy 场景；(2) §5.3 应将 d1–d3 的 45.9% 与 33% chance 明确对比并讨论实际意义；(3) 考虑将 cross-strategy 失败分析为 feature space 的 strategy dependence（温度 vs. top-k 产生形状不同的困惑度分布，§5.3 已提及但可深化）。

**N4 [critical] Cross-Scale (14B) 失败且 Confounds 不可分离**
- 具体位置：Appendix B.14（Table 17, p.18–19）, §5.4（p.8）
- 问题：Qwen2.5-14B 上 EDD=0，mean accuracy 50.8%（4-class chance = 25%）。论文列出 5 个 confounds：(1) self-reference（Pythia-1.4B reference 用于 14B generator），(2) QLoRA 4-bit 量化，(3) architecture mismatch，(4) vocabulary mismatch，(5) scale gap。Appendix B.14 第 (3) 节进一步指出 AUC trajectories 非单调（Qwen2.5 有 U-shaped recovery at d2v3）。论文坦承 "four confounds remain" 无法隔离。
- 为什么影响接收：实际 model collapse 场景主要发生在 7B+ 模型上（Llama-3, Qwen, Mistral 等）。如果方法在 14B 上完全失效且原因不可分离，则论文的 practical relevance 被严重限制到 1–1.5B 学术模型，这对 EMNLP 主会议的 impact 标准是 significant concern。
- 建议修改方向：(1) 尝试使用 Qwen2.5-14B 自身（或同族更小模型如 Qwen2.5-7B）作为 reference model，消除 architecture/vocabulary mismatch；(2) 至少使用 full-precision LoRA（而非 QLoRA）消除量化 confound；(3) 如果无法在 deadline 前完成，应在 Limitations 中将 "method validated only at 1–1.5B scale" 作为核心限制，而非放在 appendix 中。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] EDD 阈值 T=0.70 缺乏独立验证**
- 具体位置：§3.3 Definition 1, §4.4, Appendix B.7
- 问题：T=0.70 直接从 binary AUC 的 "acceptable discrimination" 标准（Hosmer & Lemeshow, 2000）迁移到 ordinal pairwise AUC 设定。§4.4 展示了阈值敏感性——T=0.80 时多个 cell EDD 降低（特别是 top-k，仅 GPT-2 XL 维持 EDD≥3），T=0.65 时所有 cell EDD≥3。EDD 是论文的核心概念贡献，但其数值完全取决于一个从不同领域借用的阈值。
- 建议：(1) 报告 threshold-free 版本（如 mean pairwise AUC 衰减曲线，Figure 2 已有但未形式化为指标）；(2) 或通过 held-out calibration 实证确定 threshold；(3) 至少在 sensitivity analysis 中展示 T ∈ [0.60, 0.85] 的连续 EDD 变化表格。

**W2 [warning] Binoculars 11-feat 与本文 19-feat 统计不可区分**
- 具体位置：§5.1（Table 4, p.7–8）, Appendix B.26
- 问题：Binoculars 校准后的 11 特征 RF 达到 78.1%，本文 19 特征 RF 达到 78.4%，p > 0.05（Table 4 脚注 ²）。两个独立特征集达到统计不可区分的性能，这自然引发疑问：**本文 19 特征 pipeline 的 unique methodological contribution 在哪里？** Merged 30-feat 82.6% 证明了互补性，但同时也说明单独使用任一特征集都不够充分。
- 建议：(1) 更明确地讨论本文特征相对于 Binoculars 的独特价值（例如：Binoculars 需要 observer model，本文仅需 reference model；或特征的 interpretability 优势）；(2) 讨论为什么两个独立特征集收敛到相同性能——这可能暗示 depth signal 的 information ceiling 在 ~78% 附近。

**W3 [warning] BOS-Seeded Generation 限制生态效度**
- 具体位置：§3.2, Appendix B.27（Table 29, p.24）
- 问题：全部 180K 样本从 BOS token 生成，不包含任何 topic prompt。Appendix B.27 测试 prompted generation（Wikipedia topic prompts）发现精度下降 13.5pp（AUC 从 BOS baseline 下降）。实际递归污染从已有文本开始（而非 BOS），这意味着 benchmark 可能高估了可辨识性。
- 建议：在 Limitations 中明确讨论 BOS vs. prompted 差距，并将 prompted generation 的结果提升到主文（至少在 §5 中提及 13.5pp drop）。

**W4 [warning] Wild-Data FPR 过高**
- 具体位置：Table 13（Appendix B.11, p.17）, §5.1
- 问题：C4 editorial passages FPR 34%，FineWeb FPR 17%（confidence threshold P(d0) ≥ 0.15）。WikiText 上 ≥98.5% d0 accuracy，但 C4 差距巨大。论文称 "the gap reflects filtering in FineWeb removing feature-anomalous text" 并指出阈值是 domain-dependent。但 34% FPR 意味着每 3 篇真实人类文本就有 1 篇被误判为 AI 生成，这对任何实际部署场景都不可接受。
- 建议：在 Limitations 中将 wild-data FPR 作为核心限制讨论，不仅仅是 threshold calibration 问题。

**W5 [warning] DeBERTa/RoBERTa End-to-End 的失败原因分析不足**
- 具体位置：Table 4（p.7–8）, Appendix B.9（p.16）
- 问题：DeBERTa-v3-base 和 RoBERTa-base end-to-end 分类器大幅落后 RF（Table 4: 58.3%/59.5% vs RF 78.4%）。Appendix B.9 将此归因于 PLM representations 的 feature space divergence，但仅尝试了 2 个架构且都使用 raw text 输入。未测试将 19 个统计特征输入 MLP/DNN 的配置（即 RF 的神经网络对应物），也未测试用 reference model perplexity 序列（而非 raw tokens）微调 PLM。
- 建议：增加至少一个 "19-feature MLP" 实验，以区分是 RF 算法优势还是特征优势。

### 小问题（不影响接收）

**M1.** §4.1 脚注 ³ 声明 p-values 为 "exploratory"，但正文多处从个别 p 值得出强结论（如 "Pythia achieves p < 0.001 with graded confidence across families"）。建议在所有 p 值旁报告 effect size（Cohen's d 或 accuracy difference CI）。

**M2.** Table 2 的 "Chance = 25% / 33%" 在不同位置指代不同——Table 4 的 "Chance = 25%" 是 4-class，Table 5/6 的 "Chance = 25% / 33%" 分别对应 d0–d3 和 d1–d3。建议统一标注。

**M3.** §3.2 "BOS-seeded" 的定义首次出现在正文中但未给出生成停止条件（max 512 tokens），这一关键信息仅在 supplementary 中出现。

**M4.** Figure 2 的 y 轴标签 "Pairwise AUC" 与 legend 中 "Binary pairwise AUC" 不一致。

**M5.** 引用核查发现 4 条 minor mismatch（主要是 first author 姓名排序差异：alemohammad2024_mad, llama3, guo2024_biscope, hosmer2000 年份），以及 8 条 not_found（多为 2025–2026 极新 preprint，预期内）。无伪造引用。

## 4. Questions

**Q1.** 如果统一使用 OLMo-1B（而非 Pythia-1.4B）作为所有 9 cell 的 reference model，Table 2 的 overall accuracy 和 EDD 会如何变化？Appendix B.13 仅报告了 Pythia cells 的 ablation，但 OLMo/GPT-2 XL cells 使用 OLMo/GPT-2 XL 作 reference 也可能存在 partial self-reference（共享训练数据分布）。

**Q2.** §4.2 报告 effective independent dimensionality 仅 3–5。是否尝试过直接用 PCA 前 3–5 个 component 训练 RF？如果精度不变，则更 parsimonious 地支持了 claim。

**Q3.** Cross-strategy transfer 中，nucleus → temp 和 temp → nucleus 的方向性是否对称？Table 6 仅报告 leave-one-out aggregation，但不同方向可能有很大差异。

**Q4.** Appendix B.21 的 instruction-tuning ablation（Qwen2.5-1.5B-Instruct）显示精度下降但深度信号仍存在（§B.21 "reduces but does not eliminate depth signal"）。是否测试过 chat/instruction-tuned 模型在 within-1.5B 范围内的 cross-model transfer？

**Q5.** Wild-data FPR 中，C4 的 34% 和 FineWeb 的 17% 差异是否主要由 domain（web-crawl quality）还是 temporal shift（C4 2019 vs FineWeb 2020+）导致？

## 5. Missing References

- **Strobl et al. (2008)** "Conditional variable importance for random forests" — 直接相关于 N2 的多重共线性下特征重要性问题。论文使用标准 Gini 但未引用或讨论 conditional importance 替代方案。
- **Hooker et al. (2021)** "Unrestricted Permutation Forces Extrapolation" — 讨论 permutation importance 在 correlated features 下的偏差，直接相关于 Appendix B.2。
- **Accumulation 设定的更多实验研究**：论文仅讨论 full-replacement，但 Gerstgrasser et al. (2024) 的 accumulation 设定更接近实际，可在 Related Work 中更明确地讨论两种设定的 depth estimation 差异。

## 6. Minor Issues

- §1 第 2 段 "model-collapse—model cycle" 应为 "model-collapse model cycle"（多余的 em-dash）
- Table 1 caption 中 "computed from the reference model (Pythia-1.4B)" 应注明此 reference model 选择的影响
- Appendix B.5 "DCOL iteration details" 标题中 DCOL 未在正文中定义（仅在 appendix 首次出现）
- 部分 Appendix 表格（Table 17, 20, 25）的 caption 信息密度可以提高，当前需要来回翻页才能理解含义

## 7. Overall Assessment

**Overall**: 3.0 (Findings)

**Soundness**: 3/5 — 受控设定内的主要 claim（depth discriminability exists）有实验支撑，但 headline 数字被 self-reference 膨胀（N1），特征重要性分析在严重共线性下不可靠（N2），泛化 claim 明显超出实验证据（N3, N4）。

**Excitement**: 3/5 — 问题定义新颖（ordinal depth estimation），实验规模可观（180K 样本，21 个 appendix section），但方法仅在 1–1.5B 模型 + known strategy 下有效，practical impact 受限。

**Reproducibility**: 4/5 — 超参数、pipeline 细节、代码结构在 supplementary 中完整披露。数据承诺 acceptance 后发布。

**Confidence**: 4/5 — 对 model collapse、AI text detection、统计方法论均有熟悉度，仔细阅读了全部 25 页。

**理由**：本文提出了一个有价值的新问题（递归生成深度的序数估计），构建了大规模受控基准，并发现了跨架构一致的 perplexity tail 退化 pattern。然而，四个 critical issues 阻止了主会议推荐：(1) self-reference confound 使核心数字不可信（需重新报告 clean subset）；(2) 严重多重共线性下 feature importance 叙事缺乏稳健性；(3) cross-strategy transfer 在深层深度接近 chance，削弱了 general depth estimation 的 claim；(4) 14B 实验完全失败且 confounds 不可分离，限制了 practical relevance。如果 N1 和 N2 在 revision 中得到充分解决（clean baseline + group-level ablation），且 claim 相应调整为 within-strategy characterization study，论文适合 Findings 发表。

---
*Reviewer 1 | 审查侧重：方法严谨性 + 实验设计*


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-20T14:09:56.139741+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待 Reviewer 2 完成 Round 1 初审",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待 Reviewer 2 完成 Round 1 初审",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-20T14:09:56.190546+00:00_

Next wakeup scheduled for 14:13:00 (in 184s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1372 · 2026-05-20T14:10:01.961288+00:00_

Reviewer 1 初审已收到。评分 3.0（Findings），提出 4 个 critical issues（self-reference confound、多重共线性、cross-strategy 近 chance、14B 失败）。

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 126

## Round 126

8 recorded events


### User

_source line 1373 · 2026-05-20T14:10:03.051074+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints

**审查侧重：新颖性 + 完整性 + 相关工作**

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 任务形式化有价值、实验执行扎实诚实，但核心方法是标准特征+标准分类器，14B实验（EDD=0）从根本上削弱了实际意义，不足以支撑主会议接收。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨、报告诚实（主动披露d0膨胀、Pythia自引用偏差），但Pythia自引用confound影响1/3主结果，14B实验有5个混淆因素未分离 |
| Excitement | 2.5/5 | 任务形式化本身有新意，但方法无算法贡献（论文自认），14B尺度障碍严重限制实用性 |
| Reproducibility | 4/5 | 实验细节充分（LoRA配置、种子、bootstrap CI），承诺代码和数据开源，但跨尺度实验仅1个模型、单次运行 |
| Overall | 3.0/5 | Findings 水平——扎实的实证工作，但缺乏方法新颖性，且核心叙事被尺度障碍削弱 |
| Confidence | 4/5 | 仔细阅读了全文25页（含附录），验证了全部74条引用，搜索了相关工作覆盖 |

---

## 1. Summary

本文将"递归生成深度估计"形式化为序数分类任务：给定文本段落，判断其经历了多少轮递归生成（d0=人写、d1=第一轮生成、d2=第二轮...）。作者构建了180K样本的benchmark（3个1-1.5B模型族 × 3种解码策略 × 4个深度），提出EDD度量，并展示基于参考模型困惑度分布的19维统计特征 + Random Forest可达69-86%的四分类准确率。论文同时测试了跨模型/跨策略/跨域/跨尺度迁移能力，发现在14B尺度下EDD降为0。

---

## 2. Strengths

**S1. 任务形式化填补了真实空白。** 现有文献要么做二元检测（人/机），要么研究model collapse时假设depth已知。将depth estimation定义为序数分类是一个自然且有价值的问题重构。Introduction §1对问题的定位清晰，与binary detection、watermarking、model collapse文献的差异化阐述准确（第2段，lines 9-13）。

**S2. 实验设计严谨系统。** 3×3 grid覆盖了模型和解码策略两个维度的变异，180K样本量充足。在统计方法上使用bootstrap CI、5-fold CV、paired permutation test，方法学规范。EDD定义（Definition 1, §3.4）是一个有用的操作性度量，提供了超越单一准确率的深度可分辨性刻画。

**S3. 特征收敛分析有说服力。** RF、XGBoost、LightGBM在0.4pp内收敛（§5.1, Table 4），独立的Binoculars特征达到统计等价性能（78.1% vs 78.4%, p>0.05），30特征合并达82.6%——这三重证据有效论证了信号存在于特征而非分类器。这种收敛性分析在实证研究中是一个示范性做法。

**S4. 报告异常诚实透明。** 论文主动报告：(a) d0膨胀问题，始终并列d1-d3指标（§4.1, Table 2）；(b) Pythia自引用偏差，标记†并量化4-11pp（§3.2, Limitations）；(c) 14B尺度下EDD=0的负面结果（§5.4）；(d) 跨策略迁移仅45.9%（§5.3）。这种诚实度在投稿论文中不常见，值得肯定。

**S5. Related Work覆盖面广。** 74条引用涵盖model collapse理论（Shumailov, Dohmatob, Alemohammad等核心文献）、AI文本检测（DetectGPT, Binoculars, GLTR等）、数据溯源、序数分类、解码策略效应五个子领域，覆盖到2026年最新预印本。对每个子领域与本文工作的区分清晰（§2最后一段"All these methods perform binary classification"）。

**S6. Limitations部分异常充分。** 涵盖full-replacement vs accumulation、控制实验设定、跨策略瓶颈、d0膨胀、域依赖FPR、对抗鲁棒性、EDD单调性假设、参考模型依赖、单次LoRA实例共9个维度，是我见过的最详尽的Limitations之一。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] 14B结果（EDD=0）从根本上削弱了论文的核心叙事

- 具体位置：§5.4, Discussion §6 line 5, Limitations第2段
- 问题：论文的motivation是"synthetic content proliferates across the web"（Introduction §1第1段），但web上的合成内容来自GPT-4、Claude等大模型，不是1.4B模型。论文在14B（Qwen2.5-14B）上展示EDD_{0.70}=0，即相邻深度在该尺度下不可区分。这意味着：(a) 论文形式化的任务在实际相关的尺度上可能不存在；(b) "statistical fingerprints"可能是小模型的artifact，而非递归生成的本质特征。
- 为什么影响接收：论文的核心claim是"recursive generation leaves quantifiable statistical fingerprints"（Introduction第4段），但14B结果表明这些fingerprints随尺度消失。论文将此处理为"preliminary observation"（§5.4标题用"Preliminary"），但这是对论文核心thesis的反证，应当获得与正面结果等量的讨论篇幅。
- 建议修改方向：(1) 将14B结果从§5.4的3行扩展为完整子节，分析哪些特征在14B下失效、为什么、是否存在替代特征；(2) 重新定位论文的scope——明确为"small-scale recursive chain depth estimation"而非泛化到web-scale场景；(3) 讨论是否存在尺度不变的特征维度（如lexical diversity趋势）即使绝对区分度降低。

**N2** [critical] 方法贡献不足以支撑主会议接收——标准特征+标准分类器

- 具体位置：§3.3 (19 features), §3.4 (RF), §5.1 (classifier convergence)
- 问题：论文自述"contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty"（Introduction第5段）。核心pipeline是：参考模型困惑度统计特征（均值、方差、分位数——标准NLP特征）+ Random Forest。Binoculars 11特征RF达到统计等价性能（p>0.05, §5.1），表明pipeline甚至可被更简单的现有工具替代。
- 为什么影响接收：EMNLP主会议论文通常需要在以下至少一个维度有显著贡献：新方法、新理论、新大规模数据集、或改变领域认知的发现。本文的task formalization有价值，但：(a) 方法无创新；(b) EDD虽是新度量，但本质是pairwise AUC的序列阈值化，技术上简单；(c) benchmark虽有系统性，但规模和影响力不及SemEval、RAID等共享任务。论文最接近"empirical study"类型，但其核心发现（depth信号在小尺度存在但大尺度消失）的影响力有限。
- 建议修改方向：(1) 开发尺度不变的特征或方法，而非仅使用标准特征；(2) 将benchmark发展为可复用的共享任务资源（开放数据、评测脚本、排行榜）以增加资源贡献价值；(3) 如果定位为Findings，当前版本已具备Findings的质量标准。

**N3** [critical] Full-replacement设定与现实场景的巨大鸿沟

- 具体位置：§3.2第3段("controlled full-replacement chains"), Limitations第1段
- 问题：所有实验使用full-replacement chain——每一轮完全替换前一轮的训练语料。现实中的递归污染是accumulation模式（Gerstgrasser et al., 2024），合成数据与人写数据以未知比例混合。Discussion中提到的pilot accumulation数据（-14 to -15pp vs 84.2%）暗示信号大幅衰减，但这些数据仅以1行文字出现（§6 line 4-5），没有任何表格或图表支撑。
- 为什么影响接收：论文的实际价值取决于depth信号能否在现实条件下存活。仅有1行pilot observation是不够的——这应该是主实验的一部分，或至少在附录中有系统呈现。Reviewer无法从这1行判断accumulation下的depth estimation是否可行。
- 建议修改方向：(1) 在附录中加入accumulation实验的完整结果（至少在1个cell上）；(2) 给出accumulation下的EDD estimate，哪怕只有upper/lower bound；(3) 如果信号完全消失，诚实报告并调整论文定位。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract信息过载，核心message被数字淹没

- 具体位置：Abstract（8行，10+个具体数字）
- 问题：Abstract包含69-86%、78.1% vs 78.4%、p>0.05、>97%、59-82%、66.4%、55.4%、74.1%、59.1%、45.9%、50.8%、EDD_{0.70}=4、EDD_{0.70}=0、82.6%、29-33%、78.1% vs 78.4%等大量数字。读者很难从中提取核心message。
- 建议：Abstract应聚焦3个核心发现：(1) 任务可解且信号存在于困惑度尾部统计；(2) 策略比模型更影响迁移；(3) 信号随尺度衰减。具体数字留给正文。

**W2** [warning] Pythia自引用confound系统性影响结果可信度

- 具体位置：§3.2第4段，Table 2（†标记），Limitations"Reference model dependency"段
- 问题：Pythia-1.4B同时担任特征提取参考模型和3个生成器之一。这意味着Table 2中1/3的结果（Pythia行）有4-11pp的系统性优势。虽然论文诚实标记了†，但跨cell比较——包括"accuracy ranges from 68.9% to 85.9%"这一headline结论——受此confound影响。最低准确率(68.9%)恰好出现在Pythia top-k上，这是自引用优势已经加持后的结果，真实最低值可能更低。
- 建议：(1) 主表额外报告去除Pythia后的6-cell范围；(2) 或使用非生成器模型（如DeBERTa或GPT-Neo）作为参考模型，消除confound。

**W3** [warning] 主文对附录的过度依赖

- 具体位置：§4-§6几乎每段引用Appendix B.x
- 问题：关键分析被推入附录：per-class recall (App B.4)、参考模型消融 (App B.13)、域偏差控制 (App B.2)、prompted generation (App B.27)、种子复现性 (App B.24)。8页主文应能独立支撑paper的核心claims，但目前多个评估维度需要翻阅附录才能判断。
- 建议：至少将per-class recall和reference model ablation的关键数字纳入主文。

**W4** [warning] 缺乏对"谁需要depth estimation"的具体论证

- 具体位置：Introduction §1
- 问题：论文动机是"a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse"（§1第2段），但没有给出具体的deployment scenario。谁会使用这个pipeline？数据策展人？如何在实际中确定参考模型？论文Discussion§6末尾提到"toward a provenance toolkit"（Appendix B.28），但这是一个5行的展望段落，不是具体方案。
- 建议：在Introduction或Discussion中增加1段具体使用场景描述。

**W5** [warning] Discussion+Conclusion过于压缩

- 具体位置：§6（Discussion and Conclusion），仅5行正文
- 问题：Discussion和Conclusion合并为一个section，正文仅5行（不含Limitations），几乎是结果的数字复述。没有对findings的深层解读——为什么perplexity tail在所有cell中占主导？这对model collapse理论有什么implications？depth信号的尺度依赖性对AI safety意味着什么？
- 建议：拆分Discussion和Conclusion，Discussion至少增加对结果的理论解读段落。

---

## 4. Questions（给作者的问题）

**Q1.** Pilot accumulation实验（-14 to -15pp vs 84.2%）的具体设置是什么？mixing ratio是多少？在哪个cell上做的？能否提供accumulation下的EDD estimate？

**Q2.** 14B实验中EDD=0是由哪些具体因素驱动的？是所有19个特征都失去区分度，还是仅perplexity tail类特征？lexical diversity和repetition特征在14B下的表现如何？

**Q3.** 论文使用Wikipedia seed text + LoRA fine-tuning来生成递归链。如果使用prompting而非fine-tuning来生成下一轮文本（更接近现实中的递归污染路径），depth信号是否仍然存在？§5.3提到prompted generation在1个cell上验证（-13.8pp），其他cell呢？

**Q4.** EDD的实用性依赖于已知decoding strategy（cross-strategy仅45.9%）。在实际部署中，decoding strategy通常未知。论文提到two-stage pipeline回收11.5pp，但strategy identification本身只有57.8%。如何在strategy-unknown条件下使pipeline可用？

**Q5.** Binoculars 11-feature RF达到统计等价的19-feature RF（78.1% vs 78.4%, p>0.05）。这是否意味着depth信号本质上是cross-perplexity divergence，而非本文pipeline独有的贡献？合并30特征的4.2pp提升是否主要来自variance reduction而非new information？

---

## 5. Missing References（遗漏的重要相关工作）

经Web Search验证，以下工作与论文直接相关但未被引用：

1. **Wang et al. (2025). "LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs."** arXiv:2506.15690. 研究多模型网络中的model collapse动态，直接关联论文的multi-model recursive chain设定。验证状态：真实（arXiv已发表）。

2. **Xie et al. (2025). "Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?" CVPR 2025.** 提出数据溯源验证方法，与论文的"data provenance"动机直接相关。虽然是视觉领域，但方法思路（生成式模型训练数据溯源）是相同的。验证状态：CVPR 2025已接收。

3. **"AI-Generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification" (2025).** arXiv:2505.11550. 多分类AI文本检测，与论文的序数分类设定相关。

### 引用验证结果

对论文全部74条引用运行了自动验证（OpenAlex API + Web Search）：

- **62/74 在线验证通过**
- **8条未在OpenAlex找到**——经Web Search逐一验证：
  - knowledge_collapse2025 → arXiv:2509.04796 ✓（NeurIPS 2025 Workshop）
  - geng2026_markovian → arXiv:2603.11228 ✓
  - falahati2026_curated → arXiv:2605.07724 ✓
  - mitchell2023_detectgpt → 经典论文，OpenAlex索引问题 ✓
  - liu2019_roberta → 经典论文 ✓
  - qwen2.5 → 技术报告 ✓
  - rennie2005 → IJCAI Workshop论文 ✓
  - ilyas2022datamodels → ICML论文 ✓
- **4条metadata不一致**（作者排序差异）：alemohammad2024_mad, llama3, guo2024_biscope, hosmer2000——均为OpenAlex索引细节问题，不影响引用真实性。
- **0条疑似虚构引用**

总体评价：引用质量高，覆盖全面，无造假嫌疑。

---

## 6. Minor Issues

- Abstract第1句："yet no method estimates how many such iterations a text has undergone"——建议补充"from its statistical properties alone"以区分需要trace的方法
- §3.2: "No per-passage lineage exists across depths"——这一重要声明应更早出现（当前在§3.2末尾）
- Table 2 footnote 1关于multiple testing correction的声明应在Methods中更早提及
- §6 Discussion and Conclusion仅5行正文，Discussion和Conclusion应拆分
- Figure 1 (atlas heatmap) 在column width下字体偏小，建议放大或移入附录
- 术语不一致："depth estimation"和"depth classification"混用（Abstract用estimation，§3.1用classification）
- Limitations段落"Reference model dependency"过长（约15行），建议拆分为"Self-reference confound"和"Reference model choice"两个独立段落
- conclusion.tex（实际为Limitations+Ethics）使用了`\section*{Limitations}`无编号section——格式正确但检查通过

---

## 7. Overall Assessment

**评分：3.0 (Findings)**

**理由：**

本文在任务形式化和系统实证方面达到了高水准——benchmark设计严谨，结果报告诚实透明（主动披露负面结果），related work覆盖全面，Limitations异常充分。这些品质是值得肯定的。

但对于EMNLP主会议，有三个互相关联的问题：

1. **方法贡献不足**——论文自认"task formalization rather than algorithmic novelty"，核心方法是标准特征+标准分类器，Binoculars特征达到等价性能表明pipeline并非不可替代。

2. **核心叙事被14B结果削弱**——论文motivation是web-scale递归污染，但在14B尺度下EDD=0，意味着该任务在实际相关的尺度上可能不成立。论文用"Preliminary"修饰这一发现，但这实际上是对核心thesis的最严重挑战。

3. **生态效度有限**——full-replacement only，而现实是accumulation；pilot数据暗示大幅衰减但未系统呈现。

综合判断：作为empirical characterization study，本文属于Findings的上段——实验扎实、报告诚实、有useful findings（perplexity tail dominance、strategy > model for transfer、EDD ceiling）。但缺乏将其推向Conference的要素：要么需要更强的方法贡献（如尺度不变特征），要么需要更强的实际影响力（如在web-scale数据上的部署验证）。

建议作者在revision中：(1) 扩展14B分析和accumulation实验以诚实呈现task的boundary conditions；(2) 考虑将benchmark打包为shared task资源以增加影响力；(3) 如果定位Findings，当前版本在修复上述问题后完全达标。

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：
- **Overall**: 3.0 (Findings)
- **Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5

**四个 Critical Issues**：
1. **Self-Reference Confound (N1)** — Pythia 同时做 generator 和 reference model，膨胀 headline 数字 4–11pp，abstract 未修饰
2. **多重共线性 (N2)** — 19 特征中 14–16 个 VIF>10，Gini/SHAP importance 不可靠，"perplexity tail dominates" 的核心叙事缺乏稳健支撑
3. **Cross-Strategy Transfer 接近 Chance (N3)** — d1–d3 仅 45.9%（chance 33%），说明 fingerprints 是 strategy-specific 的
4. **14B 完全失败 (N4)** — EDD=0，5 个 confound 不可分离，方法仅验证于 1–1.5B

**三个 Should-Fix**：EDD 阈值 T=0.70 缺乏独立验证 (W1)、Binoculars parity 质疑 unique contribution (W2)、BOS-seeded 生成限制生态效度 (W3)、Wild-data FPR 34% 过高 (W4)、neural baseline 分析不足 (W5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-20T14:11:03.924114+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
  "director_session_key": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n## 1. Summary\n本文将递归生成深度估计形式化为序数分类问题，构建了 180K 段落基准（3 个模型族 × 3 种解码策略 × 4 个深度 × 5K 样本），提取 19 维参考模型困惑度统计特征，用随机森林分类器在受控的全替换递归链上达到 69–96% 四分类精度。论文提出 Effective Discriminable Depth (EDD) 指标量化可辨识深度边界，并报告了跨模型、跨策略、跨规模的泛化实验。问题定义新颖、实验规模可观，但 self-reference confound 膨胀了核心数字、严重多重共线性动摇了特征重要性叙事、泛化实验在深层深度接近 chance，限制了主会议级别的 claim 强度。\n\n## 2. Strengths\n**S1.** 新颖且动机充分的问题定义。将 AI 文本检测从 binary 推向 ordinal depth estimation 是一个有意义的学术跨步。\n**S2.** 大规模受控基准构建。180K 样本的 9-cell 设计系统地控制了模型族、解码策略和生成深度三个维度。\n**S3.** EDD 指标的概念贡献。Definition 1 将 pairwise AUC 整合为单一可比较的 depth discriminability 指标。\n**S4.** 极为详尽的附录。21 个 appendix section 覆盖了全面的消融和验证实验。\n**S5.** 跨模型 feature importance 的收敛发现。perplexity tail 特征族在所有 9 cell 中一致主导。\n**S6.** 引用覆盖全面。74 篇参考文献，62/74 在线可验证，无伪造引用。\n\n## 3. Weaknesses\n\n### Must-Fix\n**N1 [critical]** Self-Reference Confound 膨胀核心数字 — Pythia-1.4B 同时做 generator 和 reference model（3/9 cells），4-11pp 优势。headline 数字未修饰地包含了膨胀 cell。建议报告排除 self-reference cells 的汇总统计。\n\n**N2 [critical]** 严重多重共线性动摇特征重要性叙事 — VIF>10 for 14-16/19 features，Gini importance 在高共线性下不稳定。建议 PCA/clustering 后在正交空间重新计算 importance，或使用 conditional permutation importance。\n\n**N3 [critical]** Cross-Strategy Transfer 深层深度接近 Chance — d1-d3 仅 45.9%（chance 33%），仅高出 12.9pp。论文标题暗示 general-purpose 能力但实际上跨策略极弱。\n\n**N4 [critical]** Cross-Scale (14B) 失败且 Confounds 不可分离 — EDD=0，mean 50.8%，5 个 confounds 无法隔离。方法仅在 1-1.5B 学术模型上有效。\n\n### Should-Fix\n**W1** EDD 阈值 T=0.70 从 binary AUC 标准迁移缺乏独立验证。\n**W2** Binoculars 11-feat 与本文 19-feat 统计不可区分（78.1% vs 78.4%, p>0.05），unique contribution 存疑。\n**W3** BOS-Seeded Generation 限制生态效度（prompted generation -13.5pp）。\n**W4** Wild-Data FPR 过高（C4 34%, FineWeb 17%）。\n**W5** DeBERTa/RoBERTa End-to-End 失败原因分析不足。\n\n## 4. Questions\n**Q1.** 统一用 OLMo-1B 作 reference 时 Table 2 如何变化？\n**Q2.** PCA 前 3-5 个 component 训练 RF 精度如何？\n**Q3.** Cross-strategy transfer 方向性是否对称？\n**Q4.** Instruction-tuned 模型的 cross-model transfer？\n**Q5.** C4 vs FineWeb FPR 差异的根因？\n\n## 5. Missing References\n- Strobl et al. (2008) conditional variable importance\n- Hooker et al. (2021) unrestricted permutation extrapolation\n- Accumulation 设定的更多实验研究\n\n## 7. Overall Assessment\n**Overall**: 3.0 (Findings)。四个 critical issues 阻止主会议推荐。如果 N1+N2 解决且 claim 调整为 within-strategy characterization study，适合 Findings。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
    "director_session_key": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n## 1. Summary\n本文将递归生成深度估计形式化为序数分类问题，构建了 180K 段落基准（3 个模型族 × 3 种解码策略 × 4 个深度 × 5K 样本），提取 19 维参考模型困惑度统计特征，用随机森林分类器在受控的全替换递归链上达到 69–96% 四分类精度。论文提出 Effective Discriminable Depth (EDD) 指标量化可辨识深度边界，并报告了跨模型、跨策略、跨规模的泛化实验。问题定义新颖、实验规模可观，但 self-reference confound 膨胀了核心数字、严重多重共线性动摇了特征重要性叙事、泛化实验在深层深度接近 chance，限制了主会议级别的 claim 强度。\n\n## 2. Strengths\n**S1.** 新颖且动机充分的问题定义。将 AI 文本检测从 binary 推向 ordinal depth estimation 是一个有意义的学术跨步。\n**S2.** 大规模受控基准构建。180K 样本的 9-cell 设计系统地控制了模型族、解码策略和生成深度三个维度。\n**S3.** EDD 指标的概念贡献。Definition 1 将 pairwise AUC 整合为单一可比较的 depth discriminability 指标。\n**S4.** 极为详尽的附录。21 个 appendix section 覆盖了全面的消融和验证实验。\n**S5.** 跨模型 feature importance 的收敛发现。perplexity tail 特征族在所有 9 cell 中一致主导。\n**S6.** 引用覆盖全面。74 篇参考文献，62/74 在线可验证，无伪造引用。\n\n## 3. Weaknesses\n\n### Must-Fix\n**N1 [critical]** Self-Reference Confound 膨胀核心数字 — Pythia-1.4B 同时做 generator 和 reference model（3/9 cells），4-11pp 优势。headline 数字未修饰地包含了膨胀 cell。建议报告排除 self-reference cells 的汇总统计。\n\n**N2 [critical]** 严重多重共线性动摇特征重要性叙事 — VIF>10 for 14-16/19 features，Gini importance 在高共线性下不稳定。建议 PCA/clustering 后在正交空间重新计算 importance，或使用 conditional permutation importance。\n\n**N3 [critical]** Cross-Strategy Transfer 深层深度接近 Chance — d1-d3 仅 45.9%（chance 33%），仅高出 12.9pp。论文标题暗示 general-purpose 能力但实际上跨策略极弱。\n\n**N4 [critical]** Cross-Scale (14B) 失败且 Confounds 不可分离 — EDD=0，mean 50.8%，5 个 confounds 无法隔离。方法仅在 1-1.5B 学术模型上有效。\n\n### Should-Fix\n**W1** EDD 阈值 T=0.70 从 binary AUC 标准迁移缺乏独立验证。\n**W2** Binoculars 11-feat 与本文 19-feat 统计不可区分（78.1% vs 78.4%, p>0.05），unique contribution 存疑。\n**W3** BOS-Seeded Generation 限制生态效度（prompted generation -13.5pp）。\n**W4** Wild-Data FPR 过高（C4 34%, FineWeb 17%）。\n**W5** DeBERTa/RoBERTa End-to-End 失败原因分析不足。\n\n## 4. Questions\n**Q1.** 统一用 OLMo-1B 作 reference 时 Table 2 如何变化？\n**Q2.** PCA 前 3-5 个 component 训练 RF 精度如何？\n**Q3.** Cross-strategy transfer 方向性是否对称？\n**Q4.** Instruction-tuned 模型的 cross-model transfer？\n**Q5.** C4 vs FineWeb FPR 差异的根因？\n\n## 5. Missing References\n- Strobl et al. (2008) conditional variable importance\n- Hooker et al. (2021) unrestricted permutation extrapolation\n- Accumulation 设定的更多实验研究\n\n## 7. Overall Assessment\n**Overall**: 3.0 (Findings)。四个 critical issues 阻止主会议推荐。如果 N1+N2 解决且 claim 调整为 within-strategy characterization study，适合 Findings。"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-20T14:11:30.403714+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26479
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-20T14:11:30.757282+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
  "director_session_key": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见：新颖性 + 完整性 + 相关工作\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n## 1. Summary\n本文将\"递归生成深度估计\"形式化为序数分类任务，构建180K样本benchmark，提出EDD度量，展示19维统计特征+RF在1-1.5B模型上达69-86%四分类准确率。14B尺度下EDD=0。\n\n## 2. Strengths\n**S1.** 任务形式化填补真实空白——binary detection到ordinal depth estimation的跨步。\n**S2.** 实验设计严谨系统——3×3 grid，bootstrap CI，5-fold CV。\n**S3.** 特征收敛分析有说服力——RF/XGBoost/LightGBM 0.4pp内收敛，Binoculars等价。\n**S4.** 报告异常诚实透明——主动披露d0膨胀、Pythia自引用偏差、14B负面结果。\n**S5.** Related Work覆盖面广——74条引用，验证通过。\n**S6.** Limitations部分异常充分——9个维度的限制。\n\n## 3. Weaknesses\n\n### Must-Fix\n**N1 [critical]** 14B结果（EDD=0）从根本上削弱核心叙事 — motivation是web-scale递归污染，但web上的合成内容来自大模型不是1.4B。14B下fingerprints消失意味着该任务在实际相关尺度上可能不成立。论文用\"Preliminary\"修饰但这是对核心thesis的最严重挑战。\n\n**N2 [critical]** 方法贡献不足——标准特征+标准分类器 — 论文自认无算法创新，Binoculars达等价性能表明pipeline非不可替代。EMNLP主会议需要至少一个维度的显著贡献。\n\n**N3 [critical]** Full-replacement设定与现实accumulation场景的鸿沟 — pilot accumulation数据（-14 to -15pp）仅以1行出现在§6，无表格或图表支撑。\n\n### Should-Fix\n**W1** Abstract信息过载（10+数字），核心message被淹没。\n**W2** Pythia自引用confound系统性影响1/3结果可信度。\n**W3** 主文对附录过度依赖（§4-§6几乎每段引用Appendix B.x）。\n**W4** 缺乏\"谁需要depth estimation\"的具体使用场景论证。\n**W5** Discussion+Conclusion过于压缩（仅5行正文）。\n\n## 4. Questions\n**Q1.** Pilot accumulation实验的具体设置？mixing ratio？EDD estimate？\n**Q2.** 14B下哪些具体特征失去区分度？lexical diversity和repetition如何？\n**Q3.** 如果用prompting而非fine-tuning生成递归链，信号是否存在？\n**Q4.** Strategy-unknown条件下pipeline如何可用？\n**Q5.** Binoculars parity是否意味着depth信号本质是cross-perplexity divergence？\n\n## 5. Missing References\n1. Wang et al. (2025). \"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs.\" arXiv:2506.15690\n2. Xie et al. (2025). \"Training Data Provenance Verification\" CVPR 2025\n3. \"AI-Generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification\" (2025). arXiv:2505.11550\n\n引用验证结果：62/74通过，8条确认为极新preprint，0条伪造。\n\n## 7. Overall Assessment\n**3.0 (Findings)**。方法贡献不足 + 14B失败 + 生态效度有限。作为empirical characterization study属Findings上段。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
    "director_session_key": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见：新颖性 + 完整性 + 相关工作\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n## 1. Summary\n本文将\"递归生成深度估计\"形式化为序数分类任务，构建180K样本benchmark，提出EDD度量，展示19维统计特征+RF在1-1.5B模型上达69-86%四分类准确率。14B尺度下EDD=0。\n\n## 2. Strengths\n**S1.** 任务形式化填补真实空白——binary detection到ordinal depth estimation的跨步。\n**S2.** 实验设计严谨系统——3×3 grid，bootstrap CI，5-fold CV。\n**S3.** 特征收敛分析有说服力——RF/XGBoost/LightGBM 0.4pp内收敛，Binoculars等价。\n**S4.** 报告异常诚实透明——主动披露d0膨胀、Pythia自引用偏差、14B负面结果。\n**S5.** Related Work覆盖面广——74条引用，验证通过。\n**S6.** Limitations部分异常充分——9个维度的限制。\n\n## 3. Weaknesses\n\n### Must-Fix\n**N1 [critical]** 14B结果（EDD=0）从根本上削弱核心叙事 — motivation是web-scale递归污染，但web上的合成内容来自大模型不是1.4B。14B下fingerprints消失意味着该任务在实际相关尺度上可能不成立。论文用\"Preliminary\"修饰但这是对核心thesis的最严重挑战。\n\n**N2 [critical]** 方法贡献不足——标准特征+标准分类器 — 论文自认无算法创新，Binoculars达等价性能表明pipeline非不可替代。EMNLP主会议需要至少一个维度的显著贡献。\n\n**N3 [critical]** Full-replacement设定与现实accumulation场景的鸿沟 — pilot accumulation数据（-14 to -15pp）仅以1行出现在§6，无表格或图表支撑。\n\n### Should-Fix\n**W1** Abstract信息过载（10+数字），核心message被淹没。\n**W2** Pythia自引用confound系统性影响1/3结果可信度。\n**W3** 主文对附录过度依赖（§4-§6几乎每段引用Appendix B.x）。\n**W4** 缺乏\"谁需要depth estimation\"的具体使用场景论证。\n**W5** Discussion+Conclusion过于压缩（仅5行正文）。\n\n## 4. Questions\n**Q1.** Pilot accumulation实验的具体设置？mixing ratio？EDD estimate？\n**Q2.** 14B下哪些具体特征失去区分度？lexical diversity和repetition如何？\n**Q3.** 如果用prompting而非fine-tuning生成递归链，信号是否存在？\n**Q4.** Strategy-unknown条件下pipeline如何可用？\n**Q5.** Binoculars parity是否意味着depth信号本质是cross-perplexity divergence？\n\n## 5. Missing References\n1. Wang et al. (2025). \"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs.\" arXiv:2506.15690\n2. Xie et al. (2025). \"Training Data Provenance Verification\" CVPR 2025\n3. \"AI-Generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification\" (2025). arXiv:2505.11550\n\n引用验证结果：62/74通过，8条确认为极新preprint，0条伪造。\n\n## 7. Overall Assessment\n**3.0 (Findings)**。方法贡献不足 + 14B失败 + 生态效度有限。作为empirical characterization study属Findings上段。"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-20T14:11:32.119809+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-20T14:11:43.248775+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉分享回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉分享回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-20T14:11:43.249499+00:00_

Next wakeup scheduled for 14:16:00 (in 257s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1380 · 2026-05-20T14:11:52.609786+00:00_

交叉分享已发出：
- Reviewer 1 的完整意见 → Reviewer 2（要求逐条 [AGREE]/[REBUT]）
- Reviewer 2 的完整意见 → Reviewer 1（要求逐条 [AGREE]/[REBUT]）

等待交叉回应返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 127

## Round 127

4 recorded events


### User

_source line 1381 · 2026-05-20T14:11:55.156814+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交至 Review Director。

**审稿结论摘要：**

- **Overall: 3.0 (Findings)**
- **Soundness: 3.5** | **Excitement: 2.5** | **Reproducibility: 4**

**三个 Must-Fix 问题：**
1. **14B结果(EDD=0)从根本上削弱核心叙事** — 论文motivation是web-scale递归污染，但在实际相关的模型尺度下depth信号消失，任务可能仅在小尺度存在
2. **方法贡献不足** — 标准特征+标准分类器，Binoculars 11特征达到统计等价性能(p>0.05)，论文自认无算法新颖性
3. **Full-replacement与现实的鸿沟** — 仅研究full-replacement chain，pilot accumulation数据(-14~-15pp)暗示大幅衰减但仅1行文字描述

**核心判断：** 实验执行扎实、报告异常诚实（主动披露负面结果），related work覆盖全面（74条引用全部验证通过，无虚构），Limitations异常充分。作为empirical characterization study属于Findings上段，但缺乏推向Conference的要素（方法创新或web-scale验证）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-20T14:12:07.230523+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待交叉分享回应返回",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待交叉分享回应返回",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-20T14:12:07.231600+00:00_

Next wakeup scheduled for 14:16:00 (in 233s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 1
}
```

</details>

---


### Assistant

_source line 1384 · 2026-05-20T14:12:09.931925+00:00_

Reviewer 2 初审确认收到。交叉分享任务已发出，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 128

## Round 128

4 recorded events


### User

_source line 1385 · 2026-05-20T14:13:20.051059+00:00_

[Reviewer 2 审稿结果]:
以下是我（Reviewer 2）对 Reviewer 1 审稿意见的逐条回应。

---

## Strengths 回应

**[AGREE] R1-S1**: 与我的 S1 一致。从 binary 到 ordinal depth estimation 确实是有意义的问题重构，Introduction §1 第2-3段对此的阐述清晰。

**[AGREE] R1-S2**: 与我的 S2 一致。9-cell 设计的系统性是本文的核心实验优势。

**[AGREE] R1-S3**: 同意 EDD 有概念贡献。但我在审稿中指出 EDD 技术上较简单——本质是 pairwise AUC 的序列阈值化（Definition 1, §3.4）。它的价值更多在操作性而非理论深度。

**[AGREE] R1-S4**: 与我的 S6 一致。21 个 appendix section 覆盖极广。但我同时指出这构成了对附录的过度依赖（我的 W3），主文多处关键分析仅以附录引用形式出现。

**[AGREE] R1-S5**: 与我的 S3 一致。三种 importance measure（Gini, SHAP, permutation）的 Kendall's W=0.90（§4.2 脚注）是有说服力的收敛证据。

**[AGREE] R1-S6**: 我独立验证了全部 74 条引用（OpenAlex API + Web Search），确认 0 条伪造。与 R1 结论一致。

---

## Must-Fix Weaknesses 回应

**[AGREE] R1-N1 (Self-Reference Confound)**:
与我的 W2 一致。Pythia-1.4B 同时为 generator 和 reference model，4-11pp 系统性优势（Limitations "Reference model dependency" 段, Appendix B.13）确实膨胀了 headline 数字。R1 建议"报告排除 self-reference cells 的汇总统计"是具体可操作的，作者完全可以在 Table 2 旁增加 6-cell（OLMo + GPT-2 XL）汇总行。不过我认为论文的透明标记（†）和消融报告（67-79% across alternative references）在一定程度上缓解了该问题——这是一个 should-fix 级别的 reporting issue，而非 methodological flaw。R1 将其列为 critical 略偏严格。

**[REBUT] R1-N2 (多重共线性动摇特征重要性叙事)**:
R1 的技术观察正确——VIF>10 for 14-16/19 features 确实使 individual Gini importance 不稳定。但我认为将此定为 **critical** 过重，理由如下：

1. 论文的 claim 是关于特征**族**（family）而非个体特征。§4.2 明确写道："importance rankings below indicate feature *family* contributions rather than individual effects; permutation importance (Appendix B.3) partially mitigates collinearity bias." 困惑度尾部统计**作为一个族**在所有 9 cell 中主导，这一结论不受共线性族内成员排序不稳定性影响。

2. 论文使用了三种独立 importance measure（Gini, SHAP, permutation），Kendall's W=0.90, p<0.005（§4.2 脚注）。如果共线性真的动摇了叙事，三种方法不会高度一致。

3. 特征消融实验（§4.2）提供了不依赖 importance ranking 的直接证据：perplexity statistics alone = 76.6%，surprisal alone = 73.2%，other categories ≤ 47%。这是在特征子集上重新训练分类器的结果，不受共线性影响。

R1 建议的 PCA/conditional permutation importance 确实会加强分析，但当前证据链（三种 importance × 消融实验）已足以支撑族级 claim。建议降为 **should-fix**。

**[AGREE] R1-N3 (Cross-Strategy Transfer 接近 Chance)**:
与我的评估一致。d1-d3 仅 45.9%（Table 6），仅高出 chance 12.9pp。但我要补充两点 nuance：

1. 论文标题是 "Estimating Recursive Generation Depth via Statistical Fingerprints"，并未声称 general-purpose deployment capability。R1 说"标题暗示 general-purpose 能力"——我认为标题本身是中性的。

2. 跨策略迁移弱本身是一个有价值的 **negative finding**（§4.5："strategy effect (9.3pp range) exceeds the model effect (7.2pp)"）。发现"解码策略比模型架构更影响 depth fingerprint"对后续研究有指导意义。论文的问题不是隐瞒了这一弱点，而是未在 Abstract/Introduction 中给予足够权重——Abstract 提及 59.1% 但没有突出这一 finding 的重要性。

**[AGREE] R1-N4 (Cross-Scale 14B 失败)**:
这是我的 **N1（最高优先级 critical issue）**，完全同意 R1 的判断。EDD=0 at 14B（§5.4）意味着方法在实际相关尺度上失效。R1 指出的"5 个 confounds 不可分离"同样关键——Appendix B.15 列出了 architecture、training data、tokenizer、scale、reference model mismatch 五个混淆因素，但论文仅运行了 1 个 14B 模型的单次实验，无法 disentangle。

我与 R1 的唯一分歧是：R1 侧重于"方法仅在 1-1.5B 学术模型上有效"这一 framing，而我更强调"14B 结果 undermine 了论文的 real-world motivation"——论文 Introduction 以 web-scale 递归污染为动机，但 web 内容来自大模型。这两个角度互补。

---

## Should-Fix Weaknesses 回应

**[AGREE] R1-W1 (EDD 阈值 T=0.70 缺乏独立验证)**:
T=0.70 来自 Hosmer & Lemeshow (2000) 的 binary AUC "acceptable discrimination" 标准（§3.4 line 101），直接迁移到序数 depth 场景确实缺乏理论依据。不过§4.4 的 sensitivity analysis 显示 EDD 在 T∈{0.65, 0.70, 0.80} 范围内最多偏移 1 个 level，这在一定程度上降低了对精确阈值选择的敏感性。建议作者增加 task-specific 的阈值校准（如基于下游 deployment cost 的 utility-based threshold）。

**[AGREE] R1-W2 (Binoculars 等价性质疑 unique contribution)**:
与我的 Q5 一致。Binoculars 11-feat RF 达到 78.1% vs 本文 19-feat 78.4%（p>0.05, §5.1 Table 4），确实令人质疑本文 pipeline 的独立贡献。30-feat 合并的 +4.2pp 提升（§5.1）可能来自 variance reduction 而非 genuinely new information。这一发现对论文是双刃剑：一方面证明了 depth signal 的 robustness（多种方法收敛），另一方面削弱了 pipeline 的 novelty claim。

**[AGREE] R1-W3 (BOS-Seeded Generation 限制生态效度)**:
同意方向。BOS-seeded generation 可能放大 depth signal（§3.2 最后一段承认），prompted generation -13.8pp（§5.3）证实了信号衰减。但我注意到论文称 prompted generation 仅在 1/9 cell 验证（Limitations "Additional caveats" 段），其余 8 个 cell 的 prompted 表现未知。我在 Q3 中也提出了这个问题。

**[REBUT] R1-W4 (Wild-Data FPR 过高)**:
R1 引用了 C4 34% 和 FineWeb 17% 的 FPR 数字，但未提及论文已给出的 mitigation：confidence thresholding P(d0)≥0.15 将 FPR 从 34%/17% 降至 2.8%/0.7%（Limitations "Domain-dependent false positive rate" 段），accuracy cost 仅 -0.3pp。论文还分析了 FPR 的根因——template/SEO content 的 repetition 特征异常（rep_3gram +37%, rep_4gram +75%）。这表明 FPR 是 calibration issue 而非 fundamental limitation。R1 的 concern 有道理，但论文已提供了具体解决方案和分析，应降为 **minor**。

**[AGREE] R1-W5 (DeBERTa/RoBERTa 失败分析不足)**:
§5.1 仅用 2 行报告了 DeBERTa-v3 underperform RF 16-32pp（d2 recall 8.4%）和 RoBERTa-DCOL 14pp below RF，没有分析失败原因。可能的解释包括：(a) depth signal 存在于 distributional statistics 而非 surface text patterns，end-to-end model 无法直接 access reference-model perplexity distribution；(b) 样本量（5K per cell）对 end-to-end model 不足。论文应至少讨论这些假设。但这对论文的 core claim 影响有限——分类器收敛（§5.1）已经表明信号在特征层面，end-to-end 失败反而佐证了这一点。

---

## Questions 回应

**[AGREE] R1-Q1 (OLMo-1B 作 reference 时 Table 2 变化)**: 关键问题。Appendix B.13 报告了替代 reference 的 67-79% 范围，但未给出逐 cell 表格。这应作为 revision 必须补充的内容。

**[AGREE] R1-Q2 (PCA 前 3-5 component 的 RF 精度)**: 直接回应 N2 的建设性方案。如果 PCA 前 5 component 的 RF 精度接近 19-feat RF，则同时解决了共线性和特征贡献两个问题。

**[AGREE] R1-Q3 (Cross-strategy transfer 方向性)**: 有价值的分析方向。从 Table 6 可以看到 nucleus holdout 一致最高（69.4/65.4/59.9%），top-k holdout 一致最低——这暗示 nucleus 和 temperature 训练的特征对 top-k 测试泛化最差，但反向是否对称 Table 6 无法直接回答。

**[AGREE] R1-Q4 (Instruction-tuned 的 cross-model transfer)**: 论文提到 Llama-3.1-8B-Instruct 有 monotonically decreasing AUC（Introduction §1 第4段, Appendix B.15），与 base model 行为不同。Instruction-tuned model 的系统研究是重要的 future work。

**[AGREE] R1-Q5 (C4 vs FineWeb FPR 差异根因)**: 论文在 Limitations 中给出了部分答案——FineWeb 的 quality filtering 移除了 feature-anomalous text（Limitations "Domain-dependent" 段），但更深层的分析（如哪些具体 filter rules 与 depth features 相关）缺失。

---

## Missing References 回应

**[AGREE] R1-Strobl et al. (2008) conditional variable importance**: 对 N2（共线性）的直接技术解决方案。如果作者在 revision 中改用 conditional permutation importance，应引用此文。

**[AGREE] R1-Hooker et al. (2021) unrestricted permutation**: 同上，技术上相关。但这两篇都是统计方法论文献，对论文的核心 NLP 贡献不构成 coverage gap。

**补充我的 Missing References**: 我在审稿中还发现了 3 篇遗漏：(1) Wang et al. (2025) "LLM Web Dynamics" (arXiv:2506.15690)——多模型网络中的 collapse 动态；(2) Xie et al. (CVPR 2025) Training Data Provenance Verification；(3) arXiv:2505.11550 多分类 AI 文本检测。这些与论文的 positioning 更直接相关。

---

## Overall Assessment 回应

**[AGREE] R1 Overall 3.0 (Findings)**:
R1 和我独立给出了相同评分。我们的 critical issues 高度重叠：

| R1 Issue | R2 对应 Issue | 一致性 |
|----------|-------------|--------|
| N1 Self-Reference Confound | W2 Pythia 自引用 | 一致（我定级略低为 should-fix） |
| N2 多重共线性 | 未列为独立 issue | 我认为应降为 should-fix（见 REBUT） |
| N3 Cross-Strategy 接近 chance | 部分覆盖于我的 N3 | 一致 |
| N4 14B 失败 | N1（我的最高优先级） | 一致 |

**核心分歧**：R1 的 N2（多重共线性）我认为应降级——论文的族级 claim + 三种 importance measure + 消融实验已提供足够证据。R1 的 N1（self-reference）我认为论文的透明度足以将其从 critical 降为 should-fix。

**共识**：14B scale failure（R1-N4 / R2-N1）和方法贡献不足（R2-N2）是阻止主会议推荐的核心原因。论文作为 Findings 完全达标——实验扎实、报告诚实、有 useful findings，但缺乏 Conference 所需的方法创新或 real-world impact 突破。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-20T14:14:02.292047+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待 Reviewer 1 完成对 Reviewer 2 的交叉回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待 Reviewer 1 完成对 Reviewer 2 的交叉回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR May cycle\n- 截止日期: 2026-06-15\n- 补充材料: artifacts/supplementary/README.md\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-20T14:14:02.342808+00:00_

Next wakeup scheduled for 14:18:00 (in 238s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1388 · 2026-05-20T14:14:04.996263+00:00_

Reviewer 2 交叉回应已收到。关键分歧点：R2 认为 R1-N2（多重共线性）应降为 should-fix（族级 claim + 三种 importance + 消融实验已足够），R1-N1（self-reference）也可降级。共识：14B 失败和方法贡献不足是核心问题。

等待 Reviewer 1 对 Reviewer 2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 129

## Round 129

12 recorded events


### User

_source line 1389 · 2026-05-20T14:14:05.004507+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Strengths 回应

**[AGREE] R2-S1**: 任务形式化确实填补空白。与我的 S1 判断一致——从 binary detection 到 ordinal depth estimation 是本文最核心的学术贡献。

**[AGREE] R2-S2**: 3×3 grid + bootstrap CI + 5-fold CV 的实验框架本身设计严谨。但需附带 caveat：框架严谨不等于结论可靠——自引用 confound（我的 N1）系统性地影响了 3/9 cells 的数字，这在"严谨设计"的外壳下被掩盖。

**[AGREE] R2-S3**: RF/XGBoost/LightGBM 在 0.4pp 内收敛（§4.1）确实表明分类器选择不是关键变量。但 R2 同时提到"Binoculars 等价"——这实际上是一个 weakness 而非 strength。三个分类器收敛说明 RF 足够；但 Binoculars 11-feat 等价（78.1% vs 78.4%, p>0.05, Table 4 脚注 ²）说明本文 19 特征 pipeline 并非不可替代。R2 在 N2 中也识别了这一点，这里不应同时算作 strength。

**[AGREE] R2-S4**: 报告透明度是本文的真正优势。主动披露 d0 膨胀（Table 2 中 d0 recall ≥97%）、Pythia 自引用偏差（Table 2 脚注 ¹）、14B 负面结果（§5.4）、EDD 阈值敏感性（§4.4）——这在投稿论文中属于罕见的诚实度。

**[AGREE] R2-S5**: 与我的引用核查一致：74 条引用，62/74 在线可验证，0 伪造，覆盖了 model collapse、detection、ordinal classification 三个核心子领域。

**[AGREE] R2-S6**: Limitations 部分覆盖了 9 个维度。不过我补充一点：Limitations 缺少两个关键维度——(1) wild-data FPR 过高（C4 34%, Table 13）的实际部署影响；(2) BOS-seeded vs prompted generation 的 13.5pp gap（Appendix B.27）。这些被放在 appendix 而非 Limitations section。

---

## Weaknesses 回应

### Must-Fix

**[AGREE] R2-N1**: 14B 结果（EDD=0）从根本上削弱核心叙事。与我的 N4 完全一致。补充我的分析：Appendix B.14 Table 17 显示 Qwen2.5-14B 在 nucleus 下 mean accuracy 仅 56.1% (d1-d3: 54.1)，temperature 下 72.4%，top-k 下 47.0% (d1-d3: 4.5)。5 个 confounds 不可分离，且论文未尝试用同族模型（如 Qwen2.5-7B）作 reference model 来消除 architecture/vocabulary mismatch。R2 说 "这是对核心 thesis 的最严重挑战"——我同意，但想更精确：这不是说 depth signal 一定不存在于大模型上，而是说 **当前 pipeline 设计（1.4B reference + cross-architecture extraction）在 14B 上被证伪**。正确的结论应该是 "the method requires scale-matched reference models"，而非 "depth signals vanish at scale"。

**[REBUT] R2-N2**: "方法贡献不足"的判断过于严格。R2 称 "标准特征 + 标准分类器 = 无方法贡献"，但这一标准如果严格执行，会排除大量有价值的 empirical contribution papers。我的反驳理由：

1. **问题定义本身即贡献**：将 depth estimation 形式化为 ordinal classification（§3.1 Definition 1 的 EDD）、设计 full-replacement benchmark pipeline（§3.2）、建立 9-cell atlas（§4）——这些是 experimental methodology 的创新，不需要算法创新作为前提。EMNLP/Findings 历史上大量接收了 "standard tools, novel problem" 类型的工作。

2. **Binoculars 等价不等于 pipeline 可替代**：Binoculars 需要 observer + performer 两个模型的 cross-perplexity，本文仅需单一 reference model 的分布统计。两者达到等价性能（78.1% vs 78.4%）恰恰说明 depth signal 可从不同角度捕获，这是一个有意义的发现（§5.1）。Appendix B.26 进一步分解为 6 个 perplexity features 独立达到 75.9%（Table 26），这比 Binoculars 的 11 特征更 parsimonious。

3. 但我 **部分同意** R2 的 concern：论文确实缺乏将 standard components 组合后产生的 **超越性见解**——19 特征中 14-16 个高度共线（VIF>10, §4.2），实际有效维度仅 3-5，这意味着 pipeline 的大部分复杂性是冗余的。如果 3-5 个正交特征就能达到同等性能，那 19-feature design 的必要性确实存疑。

**综合判断**：R2-N2 作为 critical 过重，但作为 should-fix 合理。方法贡献确实偏弱，但在 Findings 标准下可以接受，前提是 claim 不 overstate。

**[AGREE] R2-N3**: Full-replacement vs accumulation 的鸿沟是真实的。§6 Limitations 仅用约 1 行提及 accumulation pilot（"-14 to -15 pp"），§6 第 1 段 "Appendix B.19" 的 mixed-depth corpus 实验也仅在附录中。Appendix B.12 的 downstream curation PoC 虽然存在（RF-filtered 10-feature F1=0.997），但样本量极小（200 samples each, 50 per depth）且仅在 Pythia-1.4B 上测试，距离真实 accumulation 场景差距很大。论文的 motivation（§1 第 1 段）以 web-scale recursive contamination 开头，但实验设定完全是 full-replacement，这种 framing mismatch 是合理的 critical concern。

### Should-Fix

**[AGREE] R2-W1**: Abstract 确实信息过载。我数了一下：Abstract 包含至少 12 个具体数字（180K, 3, 4, 1-1.5B, 19, 69-96%, RF/XGBoost/LightGBM, 0.4pp, Binoculars, 78.1% vs 78.4%, 82.6%, EDD）。核心 message（"recursive generation depth is estimable from statistical properties"）被淹没在数字中。

**[AGREE] R2-W2**: 与我的 N1 完全一致。Pythia 自引用 confound 系统性影响 1/3 结果的可信度。

**[REBUT] R2-W3**: "主文对附录过度依赖"这一批评不够公平。在 8 页限制下，论文需要将详细实验放入 appendix——这是 *ACL 社区的标准做法。§4-§6 引用 Appendix 是为了让感兴趣的 reviewer 可以验证 claim 的支撑证据，而非将核心论证外包给 appendix。关键是主文的 **self-contained 叙事是否成立**——从我的阅读看，§4 的 atlas analysis 和 §5 的 generalization analysis 即使不看 appendix 也能理解核心 claim。附录是补充而非必要条件。当然，有些信息确实应该在主文中（如 W3 的 BOS-seeded vs prompted gap），但这是信息分配问题而非"过度依赖"。

**[AGREE] R2-W4**: "谁需要 depth estimation" 的使用场景论证确实不足。§1 提到了 data curation 和 model collapse monitoring，§6 提到了 "depth becomes a continuous mixing parameter"，Appendix B.12 有 curation PoC——但这些都是高层的 sketch，缺少 concrete scenario。例如：一个数据集策展者面对 100M web passages，使用本方法后的实际工作流是什么？34% FPR（C4）下如何做决策？这个叙事缺失。

**[AGREE] R2-W5**: Discussion + Conclusion 确实过于压缩。§6 在半页内同时承担了 discussion、conclusion、limitations 和 future work 四个功能，每个部分仅 3-5 行。在 8 页限制下空间有限，但考虑到 §2 Related Work 占了整整 1 页，可以考虑压缩 §2 以释放空间给 §6。

---

## Questions 回应

**[AGREE] R2-Q1**: Pilot accumulation 设置细节缺失是合理的追问。§6 仅给出 "-14 to -15pp" 而未报告 mixing ratio、sample size、或 EDD estimate。这个数字是否来自 Appendix B.12 的 curation PoC？还是另一个未公开的实验？

**[AGREE] R2-Q2**: 14B 下哪些特征失去区分度是重要的诊断问题。Appendix B.14 第 (4) 节讨论了 "feature importance shifts under top-k"（TTR, hapax ratio 进入 top-5），但未系统报告 14B 下的 per-feature discriminability。如果 lexical diversity 和 repetition 在 14B 上仍有区分度，则说明 failure 不在 signal 消失，而在 reference model mismatch。

**[AGREE] R2-Q3**: Prompting 而非 fine-tuning 的递归链——这与我的 W3（BOS-seeded limitation）相关。Appendix B.27 测试了 prompted **generation**（topic prompts on existing pipeline），但未测试 **prompted recursive chain**（即用 prompting 而非 LoRA fine-tuning 驱动递归）。这是不同的实验：前者改变 generation seeding，后者改变整个递归机制。R2 的问题指向后者，论文未覆盖。

**[AGREE] R2-Q4**: Strategy-unknown 条件下的 pipeline 可用性直接关联我的 N3。Cross-strategy transfer d1-d3 仅 45.9%（Table 6），接近 33% chance。论文未提供 strategy-agnostic 的实际使用方案。

**[REBUT] R2-Q5**: "Binoculars parity 是否意味着 depth signal 本质是 cross-perplexity divergence"——这个推理过于简化。Appendix B.26 Table 26 分解了 Binoculars 的 feature groups：6 个 perplexity features alone 达到 75.9%，而 5 个 Binoculars-unique features（observer-performer cross-entropy 等）仅 overlap 0.4pp。本文 19 特征中的 perplexity tail features（p10-p90 quantiles）和 Binoculars 的 cross-perplexity 从不同方面捕获了同一个底层信号——perplexity distribution shift under recursive degradation——但 **mechanism** 不同：本文用单模型分布的 tail behavior，Binoculars 用双模型的 divergence。两条路径收敛到 ~78% 说明的是 **depth signal 的 information ceiling**，而非两种方法等价。

---

## Missing References 回应

**R2 推荐的 3 篇引用**：

1. **Wang et al. (2025) "LLM Web Dynamics"** — 如果该文研究网络级别的 model collapse 传播，与本文的 web-scale motivation（§1）相关。但本文聚焦于单链递归，不讨论网络拓扑，相关性中等。

2. **Xie et al. (2025) "Training Data Provenance Verification" CVPR 2025** — 这是 vision 领域的数据溯源工作。与 NLP depth estimation 的直接相关性存疑，除非该方法有跨模态启发。R2 未说明具体关联点。

3. **"AI-Generated Text Detection: A Multifaceted Approach" (2025)** — 如果该文涉及 multiclass depth classification（而非仅 binary detection），则与本文直接相关；否则只是又一个 binary detection 工作，§2 Related Work 已覆盖大量同类文献。

**我补充的遗漏引用**（来自我的 Round 1 审稿）：Strobl et al. (2008) "Conditional variable importance for random forests" 和 Hooker et al. (2021) "Unrestricted Permutation Forces Extrapolation" 直接关系到 N2 的多重共线性下特征重要性问题，比 R2 推荐的 3 篇更加关键。

---

## 综合评估对比

| 维度 | R1（我） | R2 | 一致性 |
|------|----------|------|--------|
| Overall | 3.0 (Findings) | 3.0 (Findings) | ✓ 完全一致 |
| Soundness | 3/5 | 3.5/5 | △ R2 偏高，未充分考虑 multicollinearity 对 feature importance 的影响 |
| Excitement | 3/5 | 2.5/5 | △ R2 偏低，"标准方法=无贡献" 的标准过严 |
| 14B failure | N4 (critical) | N1 (critical) | ✓ 一致 |
| Self-reference | N1 (critical) | W2 (should-fix) | △ 我认为应为 critical |
| Multicollinearity | N2 (critical) | 未提及 | ✗ R2 遗漏了此问题 |
| Cross-strategy | N3 (critical) | 隐含于 Q4 | △ R2 作为 question 而非 weakness |
| Method novelty | W2 (should-fix) | N2 (critical) | △ 严重程度分歧 |

**核心分歧**：
- R2 未识别 **multicollinearity 对 feature importance 的影响**（我的 N2），这是一个 methodological soundness 问题而非 presentation 问题。VIF>10 for 14-16/19 features 下的 Gini importance ranking 不可靠，§4 的 "Depth Degradation Atlas" 叙事因此缺乏稳健基础。
- R2 将 self-reference confound 降为 W2（should-fix），我认为应为 critical：headline 数字包含膨胀 cells 且未做修饰。
- R2 将 method novelty 提升为 N2（critical），我认为过重：Findings track 不要求算法创新。

**最终判断**：两位 reviewer 一致给出 3.0 (Findings)。我认为论文在 address N1（self-reference clean baseline）+ N2（group-level feature ablation）后可 solidly 进入 Findings 范围。14B failure（R2-N1/我的 N4）是 structural limitation，无法在一轮 revision 中解决，但如果 claim 相应限缩，不应阻止 Findings 接收。

---
*Reviewer 1 | 交叉回应 Reviewer 2*


---

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：两位 reviewer 在 Overall 3.0 (Findings) 上完全一致。主要分歧在 self-reference confound 的严重程度（我认为 critical，R2 认为 should-fix）和 method novelty 不足的严重程度（R2 认为 critical，我认为 should-fix）。R2 遗漏了 multicollinearity 对 feature importance 的影响这一关键方法论问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1390 · 2026-05-20T14:14:28.552669+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-20T14:14:28.954751+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T14:01:42.203645+00:00\", \"completed_at\": \"2026-05-20T14:05:41.036707+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页无任何视觉锚点（figure/table/架构图）。审稿人打开论文后连续阅读 3 页纯文本才看到第一个 display item（Table 1, page 4）。作为实证为主的论文，强烈建议在 page 1-2 加入一个概念图或核心结果 overview figure，帮助审稿人快速锚定论文贡献\"}, {\"severity\": \"critical\", \"dimension\": \"page 8-9\", \"message\": \"正文（Abstract 到 Discussion/Conclusion 结尾）明显超出 page 8，Discussion 部分延续到 page 9 约 1/3 处才结束。EMNLP 2026 长文限制为 8 页正文（Limitations 和 Ethics 不计入），当前排版可能违反页数限制。需要压缩正文或重新分配 display items 空间\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-5\", \"message\": \"Display items 分布严重不均：pages 1-5 仅有 1 个 display item（Table 1），而 pages 6-8 堆积了 8 个。建议将部分结果表/图前移或在 Introduction/Method 中加入概念图以平衡视觉节奏\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"单页过度密集：3 个表格（Table 4/5/6）+ 1 个含 4 panel 的 Figure 3 挤在一页。Figure 3 的混淆矩阵数字非常小，打印后可能难以辨认。建议将 Table 5 或 Table 6 移至 appendix，或将 Figure 3 放大\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 3（混淆矩阵）：4 个 panel 挤在约 1/4 页的空间内，矩阵内数字字号过小（估计 <6pt），低于正文字号 70% 的可读性阈值。建议放大或移至 appendix 并在正文引用\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1（热力图）：整体可读，颜色梯度清晰。但单元格内文字偏小，建议确认打印尺寸下仍可辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（AUC 衰减曲线）：线型清晰，置信区间 shading 合理。图例字号偏小但可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 是第一个 display item 但仅展示特征分类——信息性而非传达核心 message。审稿人更期望首个 display item 传达论文核心 idea 或关键发现\"}, {\"severity\": \"info\", \"dimension\": \"page 6-8\", \"message\": \"所有表格使用 booktabs 风格（toprule/midrule/bottomrule），最优结果加粗标注，排版规范\"}, {\"severity\": \"info\", \"dimension\": \"page 10-13\", \"message\": \"参考文献格式统一，未发现 [?] 未解析引用或明显格式不一致\"}, {\"severity\": \"info\", \"dimension\": \"page 25\", \"message\": \"最后一页（appendix）仅填充约 40
…[truncated 261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1392 · 2026-05-20T14:14:28.955174+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1393 · 2026-05-20T14:14:30.009530+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-20T14:14:30.160616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-20T14:14:30.211644+00:00_

1	issues:
2	# ============================================================
3	# CRITICAL ISSUES (Round 15 — Fresh Review)
4	# ============================================================
5	
6	- id: R15-N1
7	  summary: Pipeline 缺乏算法创新，19-feat RF 与 Binoculars 11-feat RF 无显著差异 (78.4% vs 78.1%, p>0.05)
8	  category: method
9	  severity: critical
10	  status: open
11	  first_raised_round: 15
12	  last_seen_round: 15
13	  mentions:
14	  - round: 15
15	    reviewers: [1, 2]
16	    note: "R1-N1 + R2-N1 + R2-N2 一致。Binoculars 平局 + 标准 RF/统计特征无算法创新。Merged 30-feat 82.6% 说明互补而非本文特征优越。"
17	  action_items: []
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: R15-N2
22	  summary: Cross-strategy (d1-d3 45.9%) 和 cross-scale (14B EDD=0, mean 50.8%) 泛化严重不足
23	  category: experiment
24	  severity: critical
25	  status: open
26	  first_raised_round: 15
27	  last_seen_round: 15
28	  mentions:
29	  - round: 15
30	    reviewers: [1, 2]
31	    note: "R1-N4 + R2-N3 + R2-W6 一致。Cross-strategy d1-d3 接近 chance; 14B 5个confound未分离; 不同策略产生结构性不同的 depth signal。"
32	  action_items: []
33	  resolution: ""
34	  resolution_round: null
35	
36	- id: R15-N3
37	  summary: Self-reference confound — Pythia 同时做 generator 和 reference model，1/3 结果存在系统偏差 (4-11pp advantage)
38	  category: experiment
39	  severity: critical
40	  status: open
41	  first_raised_round: 15
42	  last_seen_round: 15
43	  mentions:
44	  - round: 15
45	    reviewers: [1, 2]
46	    note: "R1-N2 Must-Fix, R2 认为 B.13 ablation 部分缓解偏 Should-Fix。Director 裁定 Must-Fix: headline 数字包含 confound 膨胀。"
47	  action_items: []
48	  resolution: ""
49	  resolution_round: null
50	
51	# ============================================================
52	# SHOULD-FIX ISSUES (Round 15)
53	# ============================================================
54	
55	- id: R15-W1
56	  summary: d0 膨胀 headline metrics — cross-model d1-d3 仅 55.4% (报告 66.4%), cross-strategy d1-d3 仅 45.9% (报告 59.1%)
57	  category: writing
58	  severity: warning
59	  status: open
60	  first_
…[truncated 13033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-20T14:16:52.298588+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n# ============================================================\n# CRITICAL ISSUES (Round 16 — Fresh Review)\n# ============================================================\n\n- id: R16-N1\n  summary: 14B 结果 (EDD=0) 从根本上削弱核心叙事——方法在实际相关的模型尺度上失效\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12-W4. 首次提出 14B confounds.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N2 覆盖。论文改用 Preliminary 标题但根本问题不变。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N4 + R2-N1 一致 critical。EDD=0, mean 50.8%, 5 confounds 不可分离。R1 指出未尝试同族 reference model; R2 指出 motivation 是 web-scale 但 web 内容来自大模型。两角度互补。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N2\n  summary: 方法贡献不足——标准特征+标准分类器，Binoculars 11-feat 达到等价性能 (p>0.05)\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12-W9. 首次提出算法贡献不足。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N1 升级为 critical。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-N2 critical, R1 交叉 REBUT 降为 should-fix（Findings 不要求算法创新 + 问题定义本身有贡献）。Director 裁定 critical: 论文自认无算法新颖性 + Binoculars parity + 14B 失败的组合效应使 task formalization alone 不足以支撑即使 Findings 的较高期望。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%（chance 33%），fingerprints 是 strategy-specific 的\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12-W2. 首次提出。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N2 合并覆盖。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N3 critical, R2 隐含于 Q4。R2 交叉 AGREE 但补充 nuance: 跨策略弱是有价值的 negative finding。Director 裁定 critical: 12.9pp above chance 对实际部署不可接受。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# SHOULD-FIX ISSUES (Round 16)\n# ============================================================\n\n- id: R16-W1\n  summary: Full-replacement 设置与现实 accumulation 场景脱节，pilot 数据仅 1 行文字\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W4.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-N3 critical, R1 交叉 AGREE。§6 仅 1 行提及 -14~-15pp，无表格。Director 裁定 should-fix (high priority): 是 structural limitation 但论文已 acknowledge。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W2\n  summary: Self-reference confound — Pythia 同时做 generator 和 reference model，1/3 结果有 4-11pp 系统偏差\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N3 critical.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N1 critical, R2-W2 should-fix。R2 交叉 AGREE 但认为透明标记(†) + ablation (67-79%) 部分缓解。Director 裁定 should-fix (high priority): 论文诚实标记但 headline 数字应报告 clean 6-cell subset。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W3\n  summary: 多重共线性 (VIF>10 for 14-16/19) 对 feature importance 叙事的影响\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W3.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N2 critical, R2 交叉 REBUT（族级 claim + 3种 importance + ablation 已足够）。Director 裁定 should-fix: R2 的 rebuttal 有说服力——族级 claim 由消融实验直接支撑，不依赖 individual importance ranking。但建议增加 group-level ablation 数字到主文。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W4\n  summary: Abstract 信息过载 (12+ 数字)，核心 message 被淹没\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W6 复发。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-W1 + R1 交叉 AGREE。R1 数了 12+ 个数字。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics — cross-model d1-d3 仅 55.4%，cross-strategy d1-d3 仅 45.9%\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W1. 双指标格式已应用但 4-class 仍领头。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N3 部分覆盖。d0 recall >97% 拉高 overall accuracy，掩盖 d1-d3 弱识别力。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W6\n  summary: EDD 阈值 T=0.70 从 binary AUC 标准迁移缺乏理论依据\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W2.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W1 + R2 交叉 AGREE。Sensitivity analysis (T∈{0.65,0.70,0.80} 偏移≤1 level) 部分缓解。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度，prompted generation -13.8pp 且仅 1/9 cell 验证\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W3 + R2 交叉 AGREE。BOS 可能放大 depth signal; prompted 仅 GPT-2 XL nucleus 验证。R1 补充: prompted recursive chain (用 prompting 而非 LoRA 驱动递归) 完全未测试。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W8\n  summary: Wild-data FPR 过高 (C4 34%, FineWeb 17%)\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W7.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W4, R2 交叉 REBUT（confidence thresholding 降至 2.8%/0.7%）。Director 保留 should-fix: 阈值方案有效但 domain-dependent，部署仍需 per-domain calibration。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W9\n  summary: Discussion+Conclusion 过于压缩（仅 5 行正文），缺乏对结果的理论解读\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12-W7 首次提出, R14 resolved.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-W5 + R1 交叉 AGREE。§6 同时承担 discussion/conclusion/limitations/future work，每部分仅 3-5 行。R1 建议压缩 §2 释放空间。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W10\n  summary: 缺乏 depth estimation 具体使用场景论证\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-W4 + R1 交叉 AGREE。§1 提到 data curation 和 model collapse monitoring，但无 concrete scenario 描述。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR / INFO ISSUES (Round 16)\n# ============================================================\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小（<6pt），打印后难以辨认\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15-M4 视觉审查发现。\"\n  - round: 16\n    reviewers: [1]\n    note: \"R1-M4 + 视觉审查再次确认。4 panel 挤在 1/4 页。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点（Figure/Table），首个 display item 在 page 4\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"视觉审查发现。强烈建议 page 1-2 加入概念图或核心结果 overview figure。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M3\n  summary: 页数合规性需验证——视觉审查报告 Discussion 可能延伸至 page 9\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"视觉审查报告 '正文超出 page 8, Discussion 延续到 page 9 约 1/3'。但 R15 视觉审查曾确认合规 (R14-C2 resolved)。需重新验证 PDF。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M4\n  summary: Display items 分布不均（pp.1-5 仅 1 个，pp.6-8 堆积 8 个）\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"视觉审查发现。Page 8 尤为密集: 3 tables + 1 figure。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M5\n  summary: 术语不一致——depth estimation 和 depth classification 混用\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [2]\n    note: \"R2 Minor. Abstract 用 estimation, §3.1 用 classification。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用——Strobl et al. (2008), Hooker et al. (2021), Wang et al. (2025) 等\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1: Strobl (2008) conditional importance, Hooker (2021) permutation extrapolation。R2: Wang (2025) LLM Web Dynamics, Xie (CVPR 2025) provenance, arXiv:2505.11550 multiclass detection。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa end-to-end 失败原因分析不足\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W5, R2 交叉 AGREE 方向但认为对 core claim 影响有限（分类器收敛已说明信号在特征层面）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R15 ISSUES NOT RAISED IN R16 (may be resolved or deprioritized)\n# ============================================================\n\n- id: R15-W5\n  summary: LoRA 微调超参 (r=16, α=32) 无 ablation，影响 benchmark 生态效度\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W2, R2 交叉 AGREE。\"\n  - round: 16\n    reviewers: []\n    note: \"本轮未被任何 Reviewer 提及，可能已被其他更高优先级问题覆盖。待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W8\n  summary: 多重比较未做 Bonferroni/FDR 校正\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W5, R2 交叉 AGREE。\"\n  - round: 16\n    reviewers: []\n    note: \"R1-M1 仅作为 minor 提及（建议报告 effect size）。本轮未作为独立 issue 提出。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏关键引用 — Markovian Generation Chains (ICLR 2026, arxiv:2603.11228)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [2]\n    note: \"R2-MR1 critical missing ref。\"\n  - round: 16\n    reviewers: []\n    note: \"论文 §2 Related Work 已引用 geng2026_markovian。\"\n  action_items: []\n  resolution: \"论文已在 Related Work 中引用 Geng et al. (2026) Markovian Generation Chains。\"\n  resolution_round: 16\n\n# ============================================================\n# HISTORICAL ISSUES (Rounds 12-14, all resolved/wont_fix)\n# ============================================================\n\n- id: R14-C2\n  summary: 主文超出 8 页限制\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"视觉审查发现. §6 溢出约 0.3-0.5 页.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 视觉审查确认页数合规。\"\n  - round: 16\n    reviewers: []\n    note: \"R16 视觉审查再次报告可能溢出。与 R15 结论矛盾，需重新验证 PDF。暂保持 resolved，以 R16-M3 追踪。\"\n  action_items:\n  - round: 14\n    action: \"压缩正文\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"R15 确认合规。R16 需重新验证。\"\n  resolution_round: 14\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. 仍仅 3/9 cells.\"\n  action_items:\n  - round: 14\n    action: \"Skip — 用户明确不跑新实验\"\n    assigned_to: research_director\n    status: wont_fix\n  resolution: \"用户指示项目收尾不再跑新实验.\"\n  resolution_round: 14\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n# ============================================================\n# CRITICAL ISSUES (Round 16 — Fresh Review)\n# ============================================================\n\n- id: R16-N1\n  summary: 14B 结果 (EDD=0) 从根本上削弱核心叙事——方法在实际相关的模型尺度上失效\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12-W4. 首次提出 14B confounds.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N2 覆盖。论文改用 Preliminary 标题但根本问题不变。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N4 + R2-N1 一致 critical。EDD=0, mean 50.8%, 5 confounds 不可分离。R1 指出未尝试同族 reference model; R2 指出 motivation 是 web-scale 但 web 内容来自大模型。两角度互补。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N2\n  summary: 方法贡献不足——标准特征+标准分类器，Binoculars 11-feat 达到等价性能 (p>0.05)\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12-W9. 首次提出算法贡献不足。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N1 升级为 critical。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-N2 critical, R1 交叉 REBUT 降为 should-fix（Findings 不要求算法创新 + 问题定义本身有贡献）。Director 裁定 critical: 论文自认无算法新颖性 + Binoculars parity + 14B 失败的组合效应使 task formalization alone 不足以支撑即使 Findings 的较高期望。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%（chance 33%），fingerprints 是 strategy-specific 的\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12-W2. 首次提出。\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N2 合并覆盖。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N3 critical, R2 隐含于 Q4。R2 交叉 AGREE 但补充 nuance: 跨策略弱是有价值的 negative finding。Director 裁定 critical: 12.9pp above chance 对实际部署不可接受。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# SHOULD-FIX ISSUES (Round 16)\n# ============================================================\n\n- id: R16-W1\n  summary: Full-replacement 设置与现实 accumulation 场景脱节，pilot 数据仅 1 行文字\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W4.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-N3 critical, R1 交叉 AGREE。§6 仅 1 行提及 -14~-15pp，无表格。Director 裁定 should-fix (high priority): 是 structural limitation 但论文已 acknowledge。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W2\n  summary: Self-reference confound — Pythia 同时做 generator 和 reference model，1/3 结果有 4-11pp 系统偏差\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-N3 critical.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N1 critical, R2-W2 should-fix。R2 交叉 AGREE 但认为透明标记(†) + ablation (67-79%) 部分缓解。Director 裁定 should-fix (high priority): 论文诚实标记但 headline 数字应报告 clean 6-cell subset。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W3\n  summary: 多重共线性 (VIF>10 for 14-16/19) 对 feature importance 叙事的影响\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W3.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N2 critical, R2 交叉 REBUT（族级 claim + 3种 importance + ablation 已足够）。Director 裁定 should-fix: R2 的 rebuttal 有说服力——族级 claim 由消融实验直接支撑，不依赖 individual importance ranking。但建议增加 group-level ablation 数字到主文。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W4\n  summary: Abstract 信息过载 (12+ 数字)，核心 message 被淹没\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W6 复发。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-W1 + R1 交叉 AGREE。R1 数了 12+ 个数字。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics — cross-model d1-d3 仅 55.4%，cross-strategy d1-d3 仅 45.9%\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W1. 双指标格式已应用但 4-class 仍领头。\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-N3 部分覆盖。d0 recall >97% 拉高 overall accuracy，掩盖 d1-d3 弱识别力。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W6\n  summary: EDD 阈值 T=0.70 从 binary AUC 标准迁移缺乏理论依据\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W2.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W1 + R2 交叉 AGREE。Sensitivity analysis (T∈{0.65,0.70,0.80} 偏移≤1 level) 部分缓解。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度，prompted generation -13.8pp 且仅 1/9 cell 验证\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W3 + R2 交叉 AGREE。BOS 可能放大 depth signal; prompted 仅 GPT-2 XL nucleus 验证。R1 补充: prompted recursive chain (用 prompting 而非 LoRA 驱动递归) 完全未测试。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W8\n  summary: Wild-data FPR 过高 (C4 34%, FineWeb 17%)\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15-W7.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W4, R2 交叉 REBUT（confidence thresholding 降至 2.8%/0.7%）。Director 保留 should-fix: 阈值方案有效但 domain-dependent，部署仍需 per-domain calibration。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W9\n  summary: Discussion+Conclusion 过于压缩（仅 5 行正文），缺乏对结果的理论解读\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12-W7 首次提出, R14 resolved.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-W5 + R1 交叉 AGREE。§6 同时承担 discussion/conclusion/limitations/future work，每部分仅 3-5 行。R1 建议压缩 §2 释放空间。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W10\n  summary: 缺乏 depth estimation 具体使用场景论证\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R2-W4 + R1 交叉 AGREE。§1 提到 data curation 和 model collapse monitoring，但无 concrete scenario 描述。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR / INFO ISSUES (Round 16)\n# ============================================================\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小（<6pt），打印后难以辨认\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15-M4 视觉审查发现。\"\n  - round: 16\n    reviewers: [1]\n    note: \"R1-M4 + 视觉审查再次确认。4 panel 挤在 1/4 页。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点（Figure/Table），首个 display item 在 page 4\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"视觉审查发现。强烈建议 page 1-2 加入概念图或核心结果 overview figure。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M3\n  summary: 页数合规性需验证——视觉审查报告 Discussion 可能延伸至 page 9\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"视觉审查报告 '正文超出 page 8, Discussion 延续到 page 9 约 1/3'。但 R15 视觉审查曾确认合规 (R14-C2 resolved)。需重新验证 PDF。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M4\n  summary: Display items 分布不均（pp.1-5 仅 1 个，pp.6-8 堆积 8 个）\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"视觉审查发现。Page 8 尤为密集: 3 tables + 1 figure。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M5\n  summary: 术语不一致——depth estimation 和 depth classification 混用\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [2]\n    note: \"R2 Minor. Abstract 用 estimation, §3.1 用 classification。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用——Strobl et al. (2008), Hooker et al. (2021), Wang et al. (2025) 等\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1: Strobl (2008) conditional importance, Hooker (2021) permutation extrapolation。R2: Wang (2025) LLM Web Dynamics, Xie (CVPR 2025) provenance, arXiv:2505.11550 multiclass detection。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa end-to-end 失败原因分析不足\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1-W5, R2 交叉 AGREE 方向但认为对 core claim 影响有限（分类器收敛已说明信号在特征层面）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R15 ISSUES NOT RAISED IN R16 (may be resolved or deprioritized)\n# ============================================================\n\n- id: R15-W5\n  summary: LoRA 微调超参 (r=16, α=32) 无 ablation，影响 benchmark 生态效度\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W2, R2 交叉 AGREE。\"\n  - round: 16\n    reviewers: []\n    note: \"本轮未被任何 Reviewer 提及，可能已被其他更高优先级问题覆盖。待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W8\n  summary: 多重比较未做 Bonferroni/FDR 校正\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W5, R2 交叉 AGREE。\"\n  - round: 16\n    reviewers: []\n    note: \"R1-M1 仅作为 minor 提及（建议报告 effect size）。本轮未作为独立 issue 提出。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏关键引用 — Markovian Generation Chains (ICLR 2026, arxiv:2603.11228)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [2]\n    note: \"R2-MR1 critical missing ref。\"\n  - round: 16\n    reviewers: []\n    note: \"论文 §2 Related Work 已引用 geng2026_markovian。\"\n  action_items: []\n  resolution: \"论文已在 Related Work 中引用 Geng et al. (2026) Markovian Generation Chains。\"\n  resolution_round: 16\n\n# ============================================================\n# HISTORICAL ISSUES (Rounds 12-14, all resolved/wont_fix)\n# ============================================================\n\n- id: R14-C2\n  summary: 主文超出 8 页限制\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"视觉审查发现. §6 溢出约 0.3-0.5 页.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 视觉审查确认页数合规。\"\n  - round: 16\n    reviewers: []\n    note: \"R16 视觉审查再次报告可能溢出。与 R15 结论矛盾，需重新验证 PDF。暂保持 resolved，以 R16-M3 追踪。\"\n  action_items:\n  - round: 14\n    action: \"压缩正文\"\n    assigned_to: paper_agent\n    status: resolved\n  resolution: \"R15 确认合规。R16 需重新验证。\"\n  resolution_round: 14\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Should-Fix. 仍仅 3/9 cells.\"\n  action_items:\n  - round: 14\n    action: \"Skip — 用户明确不跑新实验\"\n    assigned_to: research_director\n    status: wont_fix\n  resolution: \"用户指示项目收尾不再跑新实验.\"\n  resolution_round: 14\n"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-20T14:16:52.450468+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml\", \"bytes\": 12263}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-20T14:19:48.645026+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "report": "# 审稿报告：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n\n**目标 venue**: EMNLP 2026 (ARR May cycle)\n**审稿轮次**: Round 16 (Fresh Review)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+相关工作）\n**日期**: 2026-05-20\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类问题，构建了 180K 段落基准（3 个 1–1.5B 模型族 × 3 种解码策略 × 4 个深度），提取 19 维参考模型困惑度统计特征并用 Random Forest 在受控全替换递归链上达到 69–86% 四分类精度（d1–d3: 59–82%）。论文提出 Effective Discriminable Depth (EDD) 指标量化可辨识深度边界，发现 perplexity tail 特征族在所有 9 个配置中一致主导深度辨识。跨模型迁移 66.4%（d1–d3: 55.4%），跨策略迁移 59.1%（d1–d3: 45.9%），14B 尺度下 EDD=0。\n\n---\n\n## Strengths\n\n**S1. 新颖且动机充分的问题定义。** 将 AI 文本检测从 binary（human vs. machine）推向 ordinal depth estimation 是一个有意义的学术贡献，填补了 model collapse 文献（假设 depth 已知）与 detection 文献（丢弃 depth 信息）之间的空白。[R1-S1, R2-S1 一致]\n\n**S2. 大规模系统化实验设计。** 9-cell grid 系统控制了模型族、解码策略和深度三个维度。180K 样本量充足，配合 bootstrap CI、5-fold stratified CV、paired permutation test，方法学规范。[R1-S2, R2-S2 一致]\n\n**S3. 特征收敛分析。** RF/XGBoost/LightGBM 在 0.4pp 内收敛，独立的 Binoculars 特征达到等价性能（78.1% vs 78.4%, p>0.05），Merged 82.6%——三重证据有效论证了信号存在于特征而非分类器。[R1-S5, R2-S3 一致]\n\n**S4. 报告异常诚实透明。** 主动披露 d0 膨胀（Table 2 始终并列 d1–d3）、Pythia 自引用偏差（†标记 + 4–11pp 量化）、14B 负面结果（EDD=0）、跨策略迁移仅 45.9%。这种自我批评在投稿论文中罕见。[R1-S4（附录详尽）, R2-S4 一致]\n\n**S5. 引用质量高。** 74 条引用经独立验证，62/74 在线确认，8 条为极新 preprint（确认真实），0 条伪造。覆盖 model collapse 理论、AI text detection、ordinal classification、decoding strategy effects 五个子领域。[R1-S6, R2-S5 一致]\n\n**S6. Limitations 异常充分。** 覆盖 full-replacement vs accumulation、控制实验设定、跨策略瓶颈、d0 膨胀、域依赖 FPR、对抗鲁棒性、EDD 单调性、参考模型依赖、单 LoRA 实例共 9 个维度。[R2-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] 14B 结果（EDD=0）从根本上削弱核心叙事** [R1-N4 + R2-N1, 共识]\n- 论文 motivation 是 web-scale 递归污染（§1 第 1 段），但 web 上的合成内容来自 GPT-4/Claude 等大模型，不是 1.4B 模型。Qwen2.5-14B 上 EDD_{0.70}=0，mean accuracy 50.8%（2× chance），相邻深度在该尺度下不可区分。\n- 5 个 confounds（self-reference、QLoRA 量化、architecture mismatch、vocabulary mismatch、scale gap）不可分离，论文未尝试同族 reference model（如 Qwen2.5-7B）消除 architecture/vocabulary mismatch。\n- 7–8B 中间结果（Llama-3.1 70.2%, Qwen2.5-7B 60.1%）显示信号随尺度衰减但未消失，但这些实验也有量化 confound。\n- **Director 裁定**: 这是对论文核心 thesis 的最严重挑战。论文用 \"Preliminary\" 修饰但实际上这一结果需要主文级别的深入分析，而非 3 行概述 + 附录。\n\n**N2 [critical] 方法贡献不足——标准特征 + 标准分类器** [R2-N2 critical, R1 交叉 REBUT 降为 should-fix]\n- 论文自述 \"contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty\"（§1 第 5 段）。核心 pipeline 是参考模型困惑度统计特征（均值、方差、分位数）+ Random Forest——均为标准工具。\n- Binoculars 11-feat RF 达到统计等价性能（78.1% vs 78.4%, p>0.05, Table 4），表明 pipeline 并非不可替代。\n- R1 反驳称 Findings 不要求算法创新，且 Binoculars 需要 observer+performer 两个模型而本文仅需单一 reference model，部署更轻量。\n- **Director 裁定**: R1 的反驳部分有效——task formalization + benchmark 确实有 empirical contribution 价值。但当方法无创新、Binoculars parity、且 14B 失败三者叠加时，contribution 整体偏弱。维持 critical 但认为在 Findings 标准下通过适当 claim 调整可解决。\n\n**N3 [critical] Cross-strategy transfer 深层深度接近 chance** [R1-N3, R2 交叉 AGREE]\n- Cross-strategy transfer d1–d3 仅 45.9%（Table 6），chance = 33%，仅高出 12.9pp。d0 recall ≥89% 拉高 overall 到 59.1%，掩盖了深层深度的弱识别力。\n- Strategy effect (9.3pp range) 超过 model effect (7.2pp)，decoding strategy 是更强的混杂因素。\n- Two-stage pipeline 回收 11.5pp，但 strategy identification 本身仅 57.8%。\n- R2 补充：跨策略弱本身是有价值的 negative finding——\"解码策略比模型架构更影响 depth fingerprint\"对后续研究有指导意义。\n- **Director 裁定**: 在 strategy-unknown 部署场景下方法实际可用性极为有限。论文应明确限定 claim 为 within-strategy 或 known-strategy 场景。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, high priority] Full-replacement 设置与现实 accumulation 场景脱节** [R2-N3 critical, R1 AGREE]\n- 所有实验使用 full-replacement chain，现实中是 accumulation（合成+人类数据混合）。Pilot accumulation 数据（-14 to -15pp vs 84.2%）仅以 1 行文字出现在 §6，无表格支撑。\n- Director 裁定 should-fix (high priority): 是 structural limitation，论文 Limitations 已 acknowledge，但应在附录中系统呈现 accumulation 数据。\n\n**W2 [warning, high priority] Self-reference confound** [R1-N1 critical, R2-W2 should-fix]\n- Pythia-1.4B 同时做 generator 和 reference model（3/9 cells），4–11pp 系统优势。Headline 数字未修饰地包含膨胀 cells。\n- R2 认为论文的透明标记（†）和 ablation（67–79%）部分缓解。\n- Director 裁定 should-fix (high priority): 透明度值得肯定，但应在 Table 2 旁增加 6-cell clean subset 汇总，Abstract/§1 headline 应区分。\n\n**W3 [warning] 多重共线性对 feature importance 叙事的影响** [R1-N2 critical, R2 REBUT]\n- VIF>10 for 14–16/19 features，Gini importance 在高共线性下不稳定。\n- R2 有力反驳：(1) 论文 claim 是族级而非个体特征；(2) 三种 importance measure Kendall's W=0.90；(3) 消融实验（perplexity alone 76.6% vs surprisal 73.2% vs others ≤47%）直接支撑族级 claim。\n- Director 裁定 should-fix: R2 反驳有说服力，族级 claim 由消融实验直接支撑。建议增加 group-level ablation 数字到主文，使读者无需依赖 importance ranking 即可验证。\n\n**W4 [warning] Abstract 信息过载** [R2-W1, R1 AGREE]\n- 12+ 个具体数字，核心 message 被淹没。应聚焦 3 个核心发现：(1) 任务可解且信号在困惑度尾部；(2) 策略比模型更影响迁移；(3) 信号随尺度衰减。\n\n**W5 [warning] d0 膨胀 headline metrics** [R1-N3 部分, R2 隐含]\n- d0 recall >97% 系统拉高 4-class accuracy。Cross-model 66.4% 中 d0 贡献巨大（d1–d3 仅 55.4%）。论文已并列报告但 4-class 仍领头。\n\n**W6 [warning] EDD 阈值 T=0.70 缺乏独立验证** [R1-W1, R2 AGREE]\n- T=0.70 直接从 binary AUC \"acceptable discrimination\" 标准迁移。Sensitivity analysis 显示偏移 ≤1 level，部分缓解。\n\n**W7 [warning] BOS-seeded generation 限制生态效度** [R1-W3, R2 AGREE]\n- 180K 样本均从 BOS token 生成。Prompted generation -13.8pp 且仅 1/9 cell 验证。Prompted recursive chain（用 prompting 而非 LoRA 驱动递归）完全未测试。\n\n**W8 [warning] Wild-data FPR 过高** [R1-W4, R2 REBUT]\n- C4 34%, FineWeb 17%。R2 指出 confidence thresholding 降至 2.8%/0.7%（-0.3pp cost）。Director 保留 should-fix: 阈值方案有效但 domain-dependent。\n\n**W9 [warning] Discussion+Conclusion 过于压缩** [R2-W5, R1 AGREE]\n- §6 仅 5 行正文，同时承担 discussion/conclusion/limitations/future work。缺乏对结果的理论解读。\n\n**W10 [warning] 缺乏具体使用场景论证** [R2-W4, R1 AGREE]\n- 论文动机以 data curation 和 model collapse monitoring 开头，但无 concrete deployment scenario。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| 14B failure | N4 critical | N1 critical | **[AGREE]** 核心问题 |\n| Cross-strategy near chance | N3 critical | Q4 隐含 | **[AGREE]** R2 补充 negative finding 价值 |\n| Full-replacement gap | AGREE R2-N3 | N3 critical | **[AGREE]** |\n| Method novelty | W2 should-fix | N2 critical | **分歧**：R1 认为 Findings 不要求算法创新 |\n| Self-reference confound | N1 critical | W2 should-fix | **分歧**：R2 认为透明标记已缓解 |\n| Multicollinearity | N2 critical | REBUT → should-fix | **分歧**：R2 反驳族级 claim 已由消融支撑 |\n| Abstract overload | AGREE | W1 | **[AGREE]** |\n| Overall score | 3.0 Findings | 3.0 Findings | **[AGREE]** 完全一致 |\n\n---\n\n## Reviewer Divergence\n\n**分歧 1: 多重共线性的严重程度** — R1 认为 critical（VIF>10 下 Gini 不稳定动摇核心叙事），R2 REBUT 认为 should-fix（族级 claim + 消融实验不依赖 importance ranking）。Director 采纳 R2 立场：消融实验（perplexity alone 76.6% vs others ≤47%）直接支撑族级 claim，但建议主文增加 group-level ablation 数字。\n\n**分歧 2: Self-reference confound 的严重程度** — R1 认为 critical（headline 数字包含膨胀），R2 认为 should-fix（透明标记 + ablation 67–79% 部分缓解）。Director 采纳 R2 立场但提高优先级：论文诚实度应被肯定，但 headline 数字应补充 clean subset。\n\n**分歧 3: Method novelty 的严重程度** — R2 认为 critical（标准工具无创新），R1 REBUT 认为 should-fix（Findings track 接受 empirical contribution）。Director 维持 critical：方法无创新 + Binoculars parity + 14B 失败的组合效应使贡献整体偏弱，但在 Findings 标准下可通过 claim 调整解决。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** 如果统一使用 OLMo-1B 作为所有 9 cell 的 reference model，Table 2 的 overall accuracy 和 EDD 如何变化？[R1-Q1, R2 AGREE]\n\n**Q2.** PCA 前 3–5 个 component 训练 RF 精度是否接近 19-feat RF？若是，则更 parsimoniously 支撑 claim。[R1-Q2, R2 AGREE]\n\n**Q3.** Pilot accumulation 实验的具体设置——mixing ratio、cell、EDD estimate？[R2-Q1, R1 AGREE]\n\n**Q4.** 14B 下哪些具体特征失去区分度？Lexical diversity 和 repetition 在 14B 上是否保留？[R2-Q2, R1 AGREE]\n\n**Q5.** Strategy-unknown 条件下 pipeline 如何实际可用？[R2-Q4, R1 AGREE]\n\n**Q6.** Cross-strategy transfer 方向性是否对称（nucleus→temp vs temp→nucleus）？[R1-Q3]\n\n**Q7.** Binoculars parity 是否意味着 depth signal 本质是 cross-perplexity divergence，还是两条路径独立收敛于同一 information ceiling？[R2-Q5, R1 REBUT 认为是后者]\n\n---\n\n## Missing References\n\n**高相关性（应引用）：**\n1. Strobl et al. (2008) \"Conditional variable importance for random forests\" — 直接解决多重共线性下特征重要性问题 [R1]\n2. Hooker et al. (2021) \"Unrestricted Permutation Forces Extrapolation\" — permutation importance 在 correlated features 下的偏差 [R1]\n\n**中等相关性（建议引用）：**\n3. Wang et al. (2025) \"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs\" arXiv:2506.15690 — 多模型网络 collapse 动态 [R2]\n4. Xie et al. (CVPR 2025) \"Training Data Provenance Verification\" — 跨模态数据溯源 [R2]\n5. arXiv:2505.11550 \"AI-Generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification\" — 多分类检测 [R2]\n\n**引用验证结果**: 74 条引用中 62/74 在线验证通过，8 条确认为极新 preprint，0 条伪造。4 条 metadata 不一致（作者排序差异，不影响真实性）。R15-MR1 遗漏的 Markovian Generation Chains (arXiv:2603.11228) 已在 §2 Related Work 中引用，标记 resolved。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2026-05-20 14:01–14:05）\n\n**Critical findings:**\n1. **前 3 页无视觉锚点** — 审稿人连续阅读 3 页纯文本后才看到首个 display item（Table 1, page 4）。强烈建议在 page 1–2 加入概念图或核心结果 overview figure。\n2. **页数合规性存疑** — 视觉审查报告 Discussion 延伸至 page 9 约 1/3。但 R15 视觉审查曾确认合规（正文 pp.1–8, Limitations p.9 起）。**需重新验证 PDF**，可能是编译版本差异。\n\n**Warning findings:**\n3. Display items 分布严重不均（pp.1–5 仅 1 个，pp.6–8 堆积 8 个）。\n4. Page 8 过度密集：3 tables + 1 figure（Figure 3 混淆矩阵数字 <6pt，打印后可能难辨）。\n\n**Info findings:** Figure 1 热力图可读但单元格文字偏小；Figure 2 AUC 曲线清晰；所有表格 booktabs 风格规范；参考文献格式统一；Appendix 尾页正常。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.0 (Findings — 可被 Findings 接收)\n\n**Soundness**: 3.5/5 — 受控设定内的主要 claim（depth discriminability exists at 1–1.5B scale）有充分实验支撑。统计方法学规范（bootstrap CI, 5-fold CV, permutation test）。但 self-reference confound 膨胀 1/3 cells 的 headline 数字，14B 实验有 5 个不可分离的 confounds。\n\n**Excitement**: 2.5/5 — 任务形式化新颖（ordinal depth estimation），但方法无算法创新，14B 尺度障碍严重限制实际意义。perplexity tail dominance 和 strategy > model 的 finding 对后续研究有指导价值，但 information ceiling (~78%) 和 EDD=0@14B 限制了 excitement。\n\n**Reproducibility**: 4/5 — 超参数、pipeline 细节、代码结构在 supplementary 中完整披露。数据承诺 acceptance 后发布。Cross-seed replication 仅 3/9 cells（wont_fix），但已报告 seed=43 结果。\n\n**Confidence**: 4/5\n\n**理由**: 两位 Reviewer 独立给出完全一致的 3.0 Findings 评分。论文在任务形式化、benchmark 设计和报告诚实度方面达到了高水准。三个互相关联的 critical 问题阻止主会议推荐：(1) 14B 失败意味着方法在实际相关尺度上未被验证；(2) 标准方法 + Binoculars parity 使方法贡献不足；(3) cross-strategy d1–d3 仅 45.9% 限制了实际部署场景。作为 empirical characterization study，论文属于 Findings 上段——实验扎实、报告诚实、有 useful findings（perplexity tail dominance、strategy > model for transfer、EDD ceiling、feature convergence across classifiers）。建议修改方向：(1) 限缩 scope 为 \"small-scale within-strategy depth estimation\"；(2) 主文扩展 14B 分析；(3) 补充 accumulation 数据；(4) 报告 clean 6-cell baseline。\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 12+ 个数字过载。建议精简为 3 个核心发现 + 1 个核心局限（14B EDD=0）。\n\n**§1 Introduction**: Motivation 清晰但 scope 与实验能力不匹配——以 web-scale 开头但方法仅验证于 1–1.5B。建议开门见山限定 scope。缺乏具体使用场景描述。\n\n**§2 Related Work**: 覆盖全面（1 页），但可压缩以释放空间给 Discussion。引用可补充 Strobl (2008) 和 Hooker (2021) 以支持 feature importance 讨论。\n\n**§3 Method**: 问题定义清晰（§3.1）。EDD 定义（Definition 1, §3.3）有概念价值但 T=0.70 的阈值选择需增加 justification。BOS-seeded 生成应在此节讨论其对信号强度的影响。\n\n**§4 Depth Degradation Atlas**: 核心实验节。Table 2 应补充 6-cell clean subset。Feature importance 分析应在主文报告 group-level ablation 数字。Figure 1 热力图可读但列宽受限。\n\n**§5 Generalization**: 最关键的评估节。Cross-model (66.4%) 和 cross-strategy (59.1%) 的 d1–d3 数字应更突出。§5.4 的 14B 结果需大幅扩展。Binoculars parity 讨论应更深入分析 information ceiling 假说。\n\n**§6 Discussion+Conclusion**: 仅 5 行，严重不足。应拆分 Discussion 和 Conclusion，Discussion 增加：(1) perplexity tail dominance 的理论 implications；(2) strategy-dependent trajectories 对 AI safety 的意义；(3) depth signal 的 scale dependence 对 model collapse 理论的 feedback。\n\n**Limitations**: 异常充分（9 个维度），但缺少 BOS vs prompted gap 和 wild-data FPR 的部署影响讨论。\n\n**Ethics**: 覆盖基本要求。\n\n**Appendix**: 21 个 section，透明度极高。关键建议：per-class recall 和 reference model ablation 的核心数字应提升到主文。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "report": "# 审稿报告：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n\n**目标 venue**: EMNLP 2026 (ARR May cycle)\n**审稿轮次**: Round 16 (Fresh Review)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+相关工作）\n**日期**: 2026-05-20\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类问题，构建了 180K 段落基准（3 个 1–1.5B 模型族 × 3 种解码策略 × 4 个深度），提取 19 维参考模型困惑度统计特征并用 Random Forest 在受控全替换递归链上达到 69–86% 四分类精度（d1–d3: 59–82%）。论文提出 Effective Discriminable Depth (EDD) 指标量化可辨识深度边界，发现 perplexity tail 特征族在所有 9 个配置中一致主导深度辨识。跨模型迁移 66.4%（d1–d3: 55.4%），跨策略迁移 59.1%（d1–d3: 45.9%），14B 尺度下 EDD=0。\n\n---\n\n## Strengths\n\n**S1. 新颖且动机充分的问题定义。** 将 AI 文本检测从 binary（human vs. machine）推向 ordinal depth estimation 是一个有意义的学术贡献，填补了 model collapse 文献（假设 depth 已知）与 detection 文献（丢弃 depth 信息）之间的空白。[R1-S1, R2-S1 一致]\n\n**S2. 大规模系统化实验设计。** 9-cell grid 系统控制了模型族、解码策略和深度三个维度。180K 样本量充足，配合 bootstrap CI、5-fold stratified CV、paired permutation test，方法学规范。[R1-S2, R2-S2 一致]\n\n**S3. 特征收敛分析。** RF/XGBoost/LightGBM 在 0.4pp 内收敛，独立的 Binoculars 特征达到等价性能（78.1% vs 78.4%, p>0.05），Merged 82.6%——三重证据有效论证了信号存在于特征而非分类器。[R1-S5, R2-S3 一致]\n\n**S4. 报告异常诚实透明。** 主动披露 d0 膨胀（Table 2 始终并列 d1–d3）、Pythia 自引用偏差（†标记 + 4–11pp 量化）、14B 负面结果（EDD=0）、跨策略迁移仅 45.9%。这种自我批评在投稿论文中罕见。[R1-S4（附录详尽）, R2-S4 一致]\n\n**S5. 引用质量高。** 74 条引用经独立验证，62/74 在线确认，8 条为极新 preprint（确认真实），0 条伪造。覆盖 model collapse 理论、AI text detection、ordinal classification、decoding strategy effects 五个子领域。[R1-S6, R2-S5 一致]\n\n**S6. Limitations 异常充分。** 覆盖 full-replacement vs accumulation、控制实验设定、跨策略瓶颈、d0 膨胀、域依赖 FPR、对抗鲁棒性、EDD 单调性、参考模型依赖、单 LoRA 实例共 9 个维度。[R2-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] 14B 结果（EDD=0）从根本上削弱核心叙事** [R1-N4 + R2-N1, 共识]\n- 论文 motivation 是 web-scale 递归污染（§1 第 1 段），但 web 上的合成内容来自 GPT-4/Claude 等大模型，不是 1.4B 模型。Qwen2.5-14B 上 EDD_{0.70}=0，mean accuracy 50.8%（2× chance），相邻深度在该尺度下不可区分。\n- 5 个 confounds（self-reference、QLoRA 量化、architecture mismatch、vocabulary mismatch、scale gap）不可分离，论文未尝试同族 reference model（如 Qwen2.5-7B）消除 architecture/vocabulary mismatch。\n- 7–8B 中间结果（Llama-3.1 70.2%, Qwen2.5-7B 60.1%）显示信号随尺度衰减但未消失，但这些实验也有量化 confound。\n- **Director 裁定**: 这是对论文核心 thesis 的最严重挑战。论文用 \"Preliminary\" 修饰但实际上这一结果需要主文级别的深入分析，而非 3 行概述 + 附录。\n\n**N2 [critical] 方法贡献不足——标准特征 + 标准分类器** [R2-N2 critical, R1 交叉 REBUT 降为 should-fix]\n- 论文自述 \"contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty\"（§1 第 5 段）。核心 pipeline 是参考模型困惑度统计特征（均值、方差、分位数）+ Random Forest——均为标准工具。\n- Binoculars 11-feat RF 达到统计等价性能（78.1% vs 78.4%, p>0.05, Table 4），表明 pipeline 并非不可替代。\n- R1 反驳称 Findings 不要求算法创新，且 Binoculars 需要 observer+performer 两个模型而本文仅需单一 reference model，部署更轻量。\n- **Director 裁定**: R1 的反驳部分有效——task formalization + benchmark 确实有 empirical contribution 价值。但当方法无创新、Binoculars parity、且 14B 失败三者叠加时，contribution 整体偏弱。维持 critical 但认为在 Findings 标准下通过适当 claim 调整可解决。\n\n**N3 [critical] Cross-strategy transfer 深层深度接近 chance** [R1-N3, R2 交叉 AGREE]\n- Cross-strategy transfer d1–d3 仅 45.9%（Table 6），chance = 33%，仅高出 12.9pp。d0 recall ≥89% 拉高 overall 到 59.1%，掩盖了深层深度的弱识别力。\n- Strategy effect (9.3pp range) 超过 model effect (7.2pp)，decoding strategy 是更强的混杂因素。\n- Two-stage pipeline 回收 11.5pp，但 strategy identification 本身仅 57.8%。\n- R2 补充：跨策略弱本身是有价值的 negative finding——\"解码策略比模型架构更影响 depth fingerprint\"对后续研究有指导意义。\n- **Director 裁定**: 在 strategy-unknown 部署场景下方法实际可用性极为有限。论文应明确限定 claim 为 within-strategy 或 known-strategy 场景。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, high priority] Full-replacement 设置与现实 accumulation 场景脱节** [R2-N3 critical, R1 AGREE]\n- 所有实验使用 full-replacement chain，现实中是 accumulation（合成+人类数据混合）。Pilot accumulation 数据（-14 to -15pp vs 84.2%）仅以 1 行文字出现在 §6，无表格支撑。\n- Director 裁定 should-fix (high priority): 是 structural limitation，论文 Limitations 已 acknowledge，但应在附录中系统呈现 accumulation 数据。\n\n**W2 [warning, high priority] Self-reference confound** [R1-N1 critical, R2-W2 should-fix]\n- Pythia-1.4B 同时做 generator 和 reference model（3/9 cells），4–11pp 系统优势。Headline 数字未修饰地包含膨胀 cells。\n- R2 认为论文的透明标记（†）和 ablation（67–79%）部分缓解。\n- Director 裁定 should-fix (high priority): 透明度值得肯定，但应在 Table 2 旁增加 6-cell clean subset 汇总，Abstract/§1 headline 应区分。\n\n**W3 [warning] 多重共线性对 feature importance 叙事的影响** [R1-N2 critical, R2 REBUT]\n- VIF>10 for 14–16/19 features，Gini importance 在高共线性下不稳定。\n- R2 有力反驳：(1) 论文 claim 是族级而非个体特征；(2) 三种 importance measure Kendall's W=0.90；(3) 消融实验（perplexity alone 76.6% vs surprisal 73.2% vs others ≤47%）直接支撑族级 claim。\n- Director 裁定 should-fix: R2 反驳有说服力，族级 claim 由消融实验直接支撑。建议增加 group-level ablation 数字到主文，使读者无需依赖 importance ranking 即可验证。\n\n**W4 [warning] Abstract 信息过载** [R2-W1, R1 AGREE]\n- 12+ 个具体数字，核心 message 被淹没。应聚焦 3 个核心发现：(1) 任务可解且信号在困惑度尾部；(2) 策略比模型更影响迁移；(3) 信号随尺度衰减。\n\n**W5 [warning] d0 膨胀 headline metrics** [R1-N3 部分, R2 隐含]\n- d0 recall >97% 系统拉高 4-class accuracy。Cross-model 66.4% 中 d0 贡献巨大（d1–d3 仅 55.4%）。论文已并列报告但 4-class 仍领头。\n\n**W6 [warning] EDD 阈值 T=0.70 缺乏独立验证** [R1-W1, R2 AGREE]\n- T=0.70 直接从 binary AUC \"acceptable discrimination\" 标准迁移。Sensitivity analysis 显示偏移 ≤1 level，部分缓解。\n\n**W7 [warning] BOS-seeded generation 限制生态效度** [R1-W3, R2 AGREE]\n- 180K 样本均从 BOS token 生成。Prompted generation -13.8pp 且仅 1/9 cell 验证。Prompted recursive chain（用 prompting 而非 LoRA 驱动递归）完全未测试。\n\n**W8 [warning] Wild-data FPR 过高** [R1-W4, R2 REBUT]\n- C4 34%, FineWeb 17%。R2 指出 confidence thresholding 降至 2.8%/0.7%（-0.3pp cost）。Director 保留 should-fix: 阈值方案有效但 domain-dependent。\n\n**W9 [warning] Discussion+Conclusion 过于压缩** [R2-W5, R1 AGREE]\n- §6 仅 5 行正文，同时承担 discussion/conclusion/limitations/future work。缺乏对结果的理论解读。\n\n**W10 [warning] 缺乏具体使用场景论证** [R2-W4, R1 AGREE]\n- 论文动机以 data curation 和 model collapse monitoring 开头，但无 concrete deployment scenario。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| 14B failure | N4 critical | N1 critical | **[AGREE]** 核心问题 |\n| Cross-strategy near chance | N3 critical | Q4 隐含 | **[AGREE]** R2 补充 negative finding 价值 |\n| Full-replacement gap | AGREE R2-N3 | N3 critical | **[AGREE]** |\n| Method novelty | W2 should-fix | N2 critical | **分歧**：R1 认为 Findings 不要求算法创新 |\n| Self-reference confound | N1 critical | W2 should-fix | **分歧**：R2 认为透明标记已缓解 |\n| Multicollinearity | N2 critical | REBUT → should-fix | **分歧**：R2 反驳族级 claim 已由消融支撑 |\n| Abstract overload | AGREE | W1 | **[AGREE]** |\n| Overall score | 3.0 Findings | 3.0 Findings | **[AGREE]** 完全一致 |\n\n---\n\n## Reviewer Divergence\n\n**分歧 1: 多重共线性的严重程度** — R1 认为 critical（VIF>10 下 Gini 不稳定动摇核心叙事），R2 REBUT 认为 should-fix（族级 claim + 消融实验不依赖 importance ranking）。Director 采纳 R2 立场：消融实验（perplexity alone 76.6% vs others ≤47%）直接支撑族级 claim，但建议主文增加 group-level ablation 数字。\n\n**分歧 2: Self-reference confound 的严重程度** — R1 认为 critical（headline 数字包含膨胀），R2 认为 should-fix（透明标记 + ablation 67–79% 部分缓解）。Director 采纳 R2 立场但提高优先级：论文诚实度应被肯定，但 headline 数字应补充 clean subset。\n\n**分歧 3: Method novelty 的严重程度** — R2 认为 critical（标准工具无创新），R1 REBUT 认为 should-fix（Findings track 接受 empirical contribution）。Director 维持 critical：方法无创新 + Binoculars parity + 14B 失败的组合效应使贡献整体偏弱，但在 Findings 标准下可通过 claim 调整解决。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** 如果统一使用 OLMo-1B 作为所有 9 cell 的 reference model，Table 2 的 overall accuracy 和 EDD 如何变化？[R1-Q1, R2 AGREE]\n\n**Q2.** PCA 前 3–5 个 component 训练 RF 精度是否接近 19-feat RF？若是，则更 parsimoniously 支撑 claim。[R1-Q2, R2 AGREE]\n\n**Q3.** Pilot accumulation 实验的具体设置——mixing ratio、cell、EDD estimate？[R2-Q1, R1 AGREE]\n\n**Q4.** 14B 下哪些具体特征失去区分度？Lexical diversity 和 repetition 在 14B 上是否保留？[R2-Q2, R1 AGREE]\n\n**Q5.** Strategy-unknown 条件下 pipeline 如何实际可用？[R2-Q4, R1 AGREE]\n\n**Q6.** Cross-strategy transfer 方向性是否对称（nucleus→temp vs temp→nucleus）？[R1-Q3]\n\n**Q7.** Binoculars parity 是否意味着 depth signal 本质是 cross-perplexity divergence，还是两条路径独立收敛于同一 information ceiling？[R2-Q5, R1 REBUT 认为是后者]\n\n---\n\n## Missing References\n\n**高相关性（应引用）：**\n1. Strobl et al. (2008) \"Conditional variable importance for random forests\" — 直接解决多重共线性下特征重要性问题 [R1]\n2. Hooker et al. (2021) \"Unrestricted Permutation Forces Extrapolation\" — permutation importance 在 correlated features 下的偏差 [R1]\n\n**中等相关性（建议引用）：**\n3. Wang et al. (2025) \"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs\" arXiv:2506.15690 — 多模型网络 collapse 动态 [R2]\n4. Xie et al. (CVPR 2025) \"Training Data Provenance Verification\" — 跨模态数据溯源 [R2]\n5. arXiv:2505.11550 \"AI-Generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification\" — 多分类检测 [R2]\n\n**引用验证结果**: 74 条引用中 62/74 在线验证通过，8 条确认为极新 preprint，0 条伪造。4 条 metadata 不一致（作者排序差异，不影响真实性）。R15-MR1 遗漏的 Markovian Generation Chains (arXiv:2603.11228) 已在 §2 Related Work 中引用，标记 resolved。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2026-05-20 14:01–14:05）\n\n**Critical findings:**\n1. **前 3 页无视觉锚点** — 审稿人连续阅读 3 页纯文本后才看到首个 display item（Table 1, page 4）。强烈建议在 page 1–2 加入概念图或核心结果 overview figure。\n2. **页数合规性存疑** — 视觉审查报告 Discussion 延伸至 page 9 约 1/3。但 R15 视觉审查曾确认合规（正文 pp.1–8, Limitations p.9 起）。**需重新验证 PDF**，可能是编译版本差异。\n\n**Warning findings:**\n3. Display items 分布严重不均（pp.1–5 仅 1 个，pp.6–8 堆积 8 个）。\n4. Page 8 过度密集：3 tables + 1 figure（Figure 3 混淆矩阵数字 <6pt，打印后可能难辨）。\n\n**Info findings:** Figure 1 热力图可读但单元格文字偏小；Figure 2 AUC 曲线清晰；所有表格 booktabs 风格规范；参考文献格式统一；Appendix 尾页正常。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.0 (Findings — 可被 Findings 接收)\n\n**Soundness**: 3.5/5 — 受控设定内的主要 claim（depth discriminability exists at 1–1.5B scale）有充分实验支撑。统计方法学规范（bootstrap CI, 5-fold CV, permutation test）。但 self-reference confound 膨胀 1/3 cells 的 headline 数字，14B 实验有 5 个不可分离的 confounds。\n\n**Excitement**: 2.5/5 — 任务形式化新颖（ordinal depth estimation），但方法无算法创新，14B 尺度障碍严重限制实际意义。perplexity tail dominance 和 strategy > model 的 finding 对后续研究有指导价值，但 information ceiling (~78%) 和 EDD=0@14B 限制了 excitement。\n\n**Reproducibility**: 4/5 — 超参数、pipeline 细节、代码结构在 supplementary 中完整披露。数据承诺 acceptance 后发布。Cross-seed replication 仅 3/9 cells（wont_fix），但已报告 seed=43 结果。\n\n**Confidence**: 4/5\n\n**理由**: 两位 Reviewer 独立给出完全一致的 3.0 Findings 评分。论文在任务形式化、benchmark 设计和报告诚实度方面达到了高水准。三个互相关联的 critical 问题阻止主会议推荐：(1) 14B 失败意味着方法在实际相关尺度上未被验证；(2) 标准方法 + Binoculars parity 使方法贡献不足；(3) cross-strategy d1–d3 仅 45.9% 限制了实际部署场景。作为 empirical characterization study，论文属于 Findings 上段——实验扎实、报告诚实、有 useful findings（perplexity tail dominance、strategy > model for transfer、EDD ceiling、feature convergence across classifiers）。建议修改方向：(1) 限缩 scope 为 \"small-scale within-strategy depth estimation\"；(2) 主文扩展 14B 分析；(3) 补充 accumulation 数据；(4) 报告 clean 6-cell baseline。\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 12+ 个数字过载。建议精简为 3 个核心发现 + 1 个核心局限（14B EDD=0）。\n\n**§1 Introduction**: Motivation 清晰但 scope 与实验能力不匹配——以 web-scale 开头但方法仅验证于 1–1.5B。建议开门见山限定 scope。缺乏具体使用场景描述。\n\n**§2 Related Work**: 覆盖全面（1 页），但可压缩以释放空间给 Discussion。引用可补充 Strobl (2008) 和 Hooker (2021) 以支持 feature importance 讨论。\n\n**§3 Method**: 问题定义清晰（§3.1）。EDD 定义（Definition 1, §3.3）有概念价值但 T=0.70 的阈值选择需增加 justification。BOS-seeded 生成应在此节讨论其对信号强度的影响。\n\n**§4 Depth Degradation Atlas**: 核心实验节。Table 2 应补充 6-cell clean subset。Feature importance 分析应在主文报告 group-level ablation 数字。Figure 1 热力图可读但列宽受限。\n\n**§5 Generalization**: 最关键的评估节。Cross-model (66.4%) 和 cross-strategy (59.1%) 的 d1–d3 数字应更突出。§5.4 的 14B 结果需大幅扩展。Binoculars parity 讨论应更深入分析 information ceiling 假说。\n\n**§6 Discussion+Conclusion**: 仅 5 行，严重不足。应拆分 Discussion 和 Conclusion，Discussion 增加：(1) perplexity tail dominance 的理论 implications；(2) strategy-dependent trajectories 对 AI safety 的意义；(3) depth signal 的 scale dependence 对 model collapse 理论的 feedback。\n\n**Limitations**: 异常充分（9 个维度），但缺少 BOS vs prompted gap 和 wild-data FPR 的部署影响讨论。\n\n**Ethics**: 覆盖基本要求。\n\n**Appendix**: 21 个 section，透明度极高。关键建议：per-class recall 和 reference model ablation 的核心数字应提升到主文。"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-20T14:19:53.019263+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4374
}
```

</details>

---


### Assistant

_source line 1400 · 2026-05-20T14:20:02.613941+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall**: 3.0 (Findings)，两位 Reviewer 独立评分完全一致
- **3 个 Critical Issues**: (1) 14B 失败 (EDD=0) 削弱核心叙事；(2) 方法贡献不足（标准工具 + Binoculars parity）；(3) Cross-strategy d1–d3 仅 45.9% 接近 chance
- **10 个 Should-Fix**: accumulation 鸿沟、self-reference confound、多重共线性、Abstract 过载、d0 膨胀、EDD 阈值、BOS-seeded 限制、wild-data FPR、Discussion 压缩、缺使用场景
- **7 个 Minor**: Figure 3 过小、无视觉锚点、页数待验证、display items 不均、术语不一致、遗漏引用、end-to-end 分析不足
- **视觉审查**: 已完成，2 critical（页数合规待验证 + 前 3 页无视觉锚点）
- **外部审稿**: 未启用
- **Issue Tracker**: 已同步更新至 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 130

## Round 130

72 recorded events


### User

_source line 1401 · 2026-05-21T06:27:37.731678+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recursive_gen_depth_est
- 论文路径: projects/recursive_gen_depth_est/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 未提供，请自行调研

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-21T06:27:45.040904+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-21T06:27:45.041895+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-21T06:27:53.626992+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-21T06:27:53.679072+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1406 · 2026-05-21T06:27:58.584038+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1407 · 2026-05-21T06:27:58.584459+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-21T06:28:03.307391+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-21T06:28:03.358192+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-21T06:28:08.278752+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1411 · 2026-05-21T06:28:10.191477+00:00_

{"result":"# 项目 recursive_gen_depth_est 概况\n\n## 实验状态 (139 个)\n\n- **cross_model_olmo_temp09_001**: DONE (killed) — \n- **pythia_topk50_001**: DONE (success) — \n- **cross_model_gpt2xl_001**: DONE (success) — \n- **cross_model_olmo_002**: DONE (success) — \n- **pythia_temp09_001**: DONE (success) — \n- **mvp_pipeline_pythia_002**: DONE (success) — \n- **cross_model_olmo_001**: DONE (failed) — \n- **mvp_pipeline_qwen_base_004**: DONE (killed) — \n- **mvp_pipeline_pythia_001**: DONE (killed) — \n- **mvp_pipeline_base_002**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (killed) — \n- **mvp_pipeline_001**: DONE (killed) — \n- **mvp_pipeline_base_003**: DONE (killed) — \n- **mvp_pipeline_004**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- accum_v2_mix25（准备中）\n- accum_v2_mix50（准备中）\n\n## 近期结论\n- **binoculars_14b_topk50** (success): Binoculars cross-perplexity features provide complementary signal at 14B scale under top-k sampling when merged with 19 statistical features. Tests whether the merged feature gain (~+3.7pp at temp09) holds under the weakest decoding strategy. ← 基于 qwen25_14b_topk50\n  [binoculars_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/binoculars_14b_topk50/report/binoculars_14b_topk50_results.md)\n- **qwen25_14b_topk50** (success): Recursive generation depth signal persists at 14B scale under top-k sampling (k=50), achieving RF 4-class accuracy above 25% baseline. Top-k typically yields lowest accuracy across strategies; if signal persists even here, 14B scale-generality claim is robust. Directly addresses Dream worst review M3.\n  [qwen25_14b_topk50_analysis](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report/qwen25_14b_topk50_analysis_b7a903.md) | [qwen25_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report
…[truncated 1834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1912
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-21T06:28:10.192002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-21T06:28:10.744154+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{theory}
39	
40	\input{atlas}
41	
42	\input{generalization}
43	
44	\input{discussion}
45	
46	\input{conclusion}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{section_appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-21T06:28:10.744618+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission deadline"
  }
}
```

</details>

---


### Tool call

_source line 1415 · 2026-05-21T06:28:11.799069+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_EXISTS\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_EXISTS\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1416 · 2026-05-21T06:28:12.705349+00:00_

issues:
# ============================================================
# CRITICAL ISSUES (Round 16) — ALL RESOLVED via writing fixes
# ============================================================

- id: R16-N1
  summary: 14B 结果 (EDD=0) 从根本上削弱核心叙事
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 12
  last_seen_round: 16
  mentions:
  - {round: 12, reviewers: [1, 2], note: "R12-W4"}
  - {round: 15, reviewers: [1, 2], note: "R15-N2"}
  - {round: 16, reviewers: [1, 2], note: "R1-N4 + R2-N1 一致 critical"}
  action_items:
  - {round: 16, action: "Abstract/§1 scope 限定 '1-1.5B'; §6 scale dependence 段落", assigned_to: paper_agent, status: resolved}
  resolution: "Abstract 加 'at the 1-1.5B parameter scale'; §1 加 scope 限定段; §6 新增 'Scale dependence and outlook' 段落讨论 14B feedback"
  resolution_round: 16

- id: R16-N2
  summary: 方法贡献不足——标准特征+标准分类器
  category: method
  severity: critical
  status: resolved
  first_raised_round: 12
  last_seen_round: 16
  mentions:
  - {round: 12, reviewers: [1, 2], note: "R12-W9"}
  - {round: 15, reviewers: [1, 2], note: "R15-N1 critical"}
  - {round: 16, reviewers: [1, 2], note: "R2-N2 critical, R1 REBUT"}
  action_items:
  - {round: 16, action: "贡献 4→3, Binoculars 改为 validation, Abstract 去重", assigned_to: paper_agent, status: resolved}
  resolution: "§1 贡献 3 条(task+EDD / atlas+benchmark / systematic characterization); Binoculars fold 入 §5.1; Abstract 单次提及"
  resolution_round: 16

- id: R16-N3
  summary: Cross-strategy transfer d1-d3 仅 45.9%
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 12
  last_seen_round: 16
  mentions:
  - {round: 12, reviewers: [1, 2], note: "R12-W2"}
  - {round: 15, reviewers: [1, 2], note: "R15-N2"}
  - {round: 16, reviewers: [1, 2], note: "R1-N3 critical"}
  action_items:
  - {round: 16, action: "§5.3 reframe 为 structural barrier / characterization finding", assigned_to: paper_agent, status: resolved}
  resolution: "§5.3 reframed: 'structural barrier
…[truncated 10057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1417 · 2026-05-21T06:28:12.757067+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/agent/config.yaml 2>/dev/null | head -100",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/agent/config.yaml 2>/dev/null | head -100",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1418 · 2026-05-21T06:28:12.807758+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1419 · 2026-05-21T06:28:14.163167+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, the submission deadline is always the 15th of the month for ACL Rolling Review (ARR). This means that the May 2026 submission deadline would be 5/15.

The search results also indicate that ARR switched to 10-week review cycles starting in May 2025, which affects the review timeline for submissions in May 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 3418
}
```

</details>

---


### Tool call

_source line 1420 · 2026-05-21T06:28:37.384971+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline commitment deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline commitment deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 1421 · 2026-05-21T06:28:37.887257+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 dates deadlines submission site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 dates deadlines submission site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 1422 · 2026-05-21T06:28:40.297695+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-21T06:28:41.303098+00:00_

_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
atlas.tex
conclusion.tex
discussion.tex
drafts
figures
generalization.tex
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
section_appendix.tex
theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-21T06:28:41.655567+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/agent/config.yaml 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/config.yaml 2>/dev/null || echo \"NO_CONFIG\"",
  "description": "Read project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/agent/config.yaml 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/config.yaml 2>/dev/null || echo \"NO_CONFIG\"",
    "description": "Read project config files"
  }
}
```

</details>

---


### Tool result

_source line 1425 · 2026-05-21T06:28:41.756960+00:00_

---
NO_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1426 · 2026-05-21T06:28:42.962821+00:00_

Web search results for query: "EMNLP 2026 submission deadline commitment deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"The #EMNLP2023 paper deadline is a month away (June 23, 11:59 pm UTC -12h AoE). Abstract deadline is June 16. For ARR submissions, the commitment deadline is August 22. https://t.co/3rhIDMkz0X #EMNLP2023 #NLProc\" / X","url":"https://x.com/emnlpmeeting/status/1661308614508945408?lang=en"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here are the key deadlines for EMNLP 2026 related to ARR submissions and commitment:

## Important Deadlines:

**ARR Submission:** ARR submission deadline (long & short papers) is May 25, 2026

**Commitment to EMNLP:** EMNLP commitment deadline is August 2, 2026

## Key Deta
…[truncated 544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5577
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-21T06:28:44.119906+00:00_

Web search results for query: ""ACL Rolling Review" 2026 dates deadlines submission site:aclrollingreview.org"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/some-important-dates/"},{"title":"ARR Statistics","url":"http://stats.aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results from aclrollingreview.org, here are the key 2026 dates and deadlines for ACL Rolling Review:

## 2026 Submission and Review Timeline

ARR switched to 10-week review cycles starting in May 2025, and the platform now operates with 5 cycl
…[truncated 853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6232
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-21T06:29:01.308521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-21T06:29:01.817777+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a 180K-passage benchmark spanning three model families, three decoding strategies, and four depths under controlled full-replacement chains at the 1--1.5B parameter scale.
4	A lightweight pipeline---19 statistical features dominated by perplexity tail statistics, classified by Random Forest---achieves d1--d3 balanced accuracy of 59--82\% across nine model--strategy cells, with the \emph{Effective Discriminable Depth} ($\mathrm{EDD}_{0.70}$) reaching 4 for all three families.
5	Three findings emerge: (1)~depth signal concentrates in perplexity distribution tail statistics, confirmed by classifier convergence and independent cross-perplexity features (Binoculars, 78.1\% vs.\ 78.4\%); (2)~decoding strategy affects cross-condition transfer more than model architecture (d1--d3: 45.9\% cross-strategy vs.\ 55.4\% cross-model), revealing structurally distinct degradation trajectories; (3)~signal attenuates with scale---at 14B, $\mathrm{EDD}_{0.70}{=}0$ though accuracy remains $2{\times}$ chance.
6	Perturbation-based and membership-inference baselines (29--33\%) confirm that binary detection scores lack ordinal depth resolution.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 509
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-21T06:29:01.818837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-21T06:29:02.321523+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	In this work, we focus on the 1--1.5B parameter regime under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination typically involves partial mixing (accumulation), where synthetic and human data co-exist at unknown proportions; the full-replacement setting provides an upper bound on depth signal strength, and we discuss implications for accumulation settings in \S\ref{sec:discussion}.
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
11	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
12	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without 
…[truncated 3266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-21T06:29:02.322070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-21T06:29:02.774081+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad} and Markovian generation chains \cite{geng2026_markovian}.
6	Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
7	Mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, data scaling under constraint \cite{muennighoff2023scaling}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence analysis \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026} are active areas.
8	\citet{kazdan2025_collapse_or_thrive} systematically compare training workflows and show that data accumulation avoids collapse while pure replacement does not; \citet{suresh2025_rate_collapse} characterize the rate of collapse for fundamental distributions under recursive maximum-likelihood estimation.
9	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier that reveals strategy-dependent trajectories and
…[truncated 3775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1434 · 2026-05-21T06:29:02.774450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1435 · 2026-05-21T06:29:03.276766+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 6300 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-21T06:29:03.277202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 1437 · 2026-05-21T06:29:04.080658+00:00_

1	\subsection{Theoretical Grounding}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed by its dominance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), so EDD should decrease with scale.
15	Qwen2.5-14B confirms this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B), while d1--d3 AUCs remain above 0.70 (\S\ref{sec:gen:crossscale}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.
20	GPT-2~XL confirms this: temperature d1 median \texttt{p90\_ppl} (92.
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1438 · 2026-05-21T06:29:04.281985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 1439 · 2026-05-21T06:29:04.332706+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells at the 1--1.5B parameter scale, evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}1{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: MAE\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references (Appendix~\ref{app:ref_ablation}). Cross-cel
…[truncated 9350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-21T06:29:12.114200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 1441 · 2026-05-21T06:29:12.918037+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares methods across all 9 cells.
10	RF, XGBoost, and LightGBM converge within 0.4\,pp (feature-determined ceiling); CORAL \cite{coral2020} and DivEye \cite{diveye2026} match within 0.6\,pp on Pythia nucleus ($p{>}0.05$).
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA) underperforms RF by 16--32\,pp (d2 recall 8.4\%); RoBERTa-DCOL (ordinal contrastive; 64.5\%) narrows the gap but remains 14\,pp below RF.
14	
15	\paragraph{Binary detectors and membership inference.}
16	Perturbation-based (DetectGPT, 28.8\%) and membership-inference (Min-K\% Prob, 33.2\%; Min-K\%++ \cite{zhang2024_minkpp} comparable) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); CORAL calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%).
17	Binoculars \cite{binoculars2024}, calibrated with 11-feature RF on cross-perplexity scores, independently converges to matching accuracy (78.1\% vs.\ 78.4\%, $p{>}0.05$); merging all 30 features yields 82.6\% (+4.2\,pp; Appendix~\ref{app:feature_ablation_bino}).
18	Our pipeline needs only a single 1.4B reference model vs.\ Binoculars' 1.8B observer--performer pair.
19	
20	\paragraph{Surface-text ablation.}
21	Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (best 36.2\%; Appendix~\ref{app:zeroshot_prompt}) also fail; depth signal resides in distributional statistics inaccessible from surface text.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\caption{Method comparison (RF mean across 9 cells, 5-fold CV). Chance = 25\% / 33.3\% (d1--d3). $^\dagger$Adapted from binar
…[truncated 4656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1442 · 2026-05-21T06:29:13.069040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-21T06:29:13.421101+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Why tails, not means.}
5	Mean perplexity performs at chance (25.1\%) because recursive training shifts the bulk distribution only gradually; erosion concentrates in the tails \cite{dohmatob2024_tale_of_tails}, where upper-quantile features capture depth-dependent compression before bulk statistics respond.
6	The strategy effect (9.3\,pp) exceeding the model effect (7.2\,pp) implies that auditing pipelines must account for decoding configuration, not just model identity.
7	
8	\paragraph{From ceiling to floor.}
9	Full-replacement chains provide the discriminability ceiling (d1--d3: 59--82\%); pilot accumulation experiments ($-$14 to $-$15\,pp vs.\ 84.2\% full-replacement) confirm signal survives partial mixing but attenuates.
10	A deployment scenario is depth-scored data curation: score each passage for estimated recursive depth and filter or down-weight high-depth text before it enters the training loop.
11	
12	\paragraph{Scale dependence and outlook.}
13	At 14B, $\mathrm{EDD}_{0.70}{=}0$: adjacent-depth discrimination does not survive the scale transition, though accuracy remains $2{\times}$ chance; whether scale-adapted features can recover the signal remains open.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-21T06:29:13.421571+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-21T06:29:13.673004+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	All experiments use full-replacement recursive chains, where each depth fully replaces the prior training corpus.
6	Real-world contamination typically involves accumulation, where synthetic and human data co-exist at unknown proportions \cite{gerstgrasser2024_accumulate}.
7	Pilot accumulation experiments show 14--15\,pp attenuation relative to full-replacement; our results therefore represent an upper bound on feature separability, and extending the framework to accumulation settings is a priority for future work.
8	
9	\paragraph{Scale and generalization boundaries.}
10	The primary benchmark uses 1--1.5B parameter models with controlled LoRA fine-tuning.
11	At 14B, adjacent-depth discrimination does not survive the scale transition ($\mathrm{EDD}_{0.70}{=}0$), constituting a boundary condition for the current feature set.
12	Cross-strategy transfer drops d1--d3 accuracy to 45.9\%, and on web-crawl data (C4) false positive rates reach 22\%; these gaps narrow with confidence thresholding and strategy-aware pipelines but are not fully resolved.
13	Additional caveats---reference model dependency (${\leq}$11\,pp), single LoRA seed (${\sim}$1--3\,pp uncertainty), adversarial robustness, and passage length sensitivity---are detailed in the Appendix.
14	
15	\section*{Ethics Statement}
16	
17	This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
18	No human subjects were involved, no private or sensitive data were collected, and no new models were released.
19	Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
20	Code and data will be released upon acceptance.
21	This research used AI coding assistants
…[truncated 157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-21T06:29:13.673486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-21T06:29:14.026386+00:00_

1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\t
…[truncated 63286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1448 · 2026-05-21T06:29:21.507984+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1449 · 2026-05-21T06:29:22.913982+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 1450 · 2026-05-21T06:29:23.417078+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf 2>/dev/null | grep -i pages",
  "description": "Count PDF pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf 2>/dev/null | grep -i pages",
    "description": "Count PDF pages"
  }
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-21T06:29:24.371806+00:00_

Pages:           24

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-21T06:29:24.372179+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers author guidelines template anonymity page limit site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers author guidelines template anonymity page limit site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1453 · 2026-05-21T06:29:25.025007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1454 · 2026-05-21T06:29:25.075610+00:00_

1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},

…[truncated 123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-21T06:29:31.203260+00:00_

Web search results for query: "EMNLP 2026 call for papers author guidelines template anonymity page limit site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"}]

I found information about EMNLP 2026 from the official website. Here are the key details about author guidelines, anonymity, and page limits:

**Anonymity:**
Following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing process will continue to be double-blind, with reviewers not seeing authors, nor will authors see reviewers and reviews on ARR.

**Page Limits:**
The search results include information about specific tracks. For the Industry Track, the Limitations section will not count toward the page limit. For tutorials, proposals should not exceed 4 pages of content (plus one page for tutor biographies and unlimited pages for references).

**Templates:**
Proposals should use the ACL paper submission format, and authors can download the LaTeX template or use the Overleaf template.

**A
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6831
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-21T06:30:03.505252+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -name \"config*\" -type f 2>/dev/null",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -name \"config*\" -type f 2>/dev/null",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1457 · 2026-05-21T06:30:03.657515+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1458 · 2026-05-21T06:30:08.731097+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -maxdepth 3 -name \"*.yaml\" -path \"*/recursive*\" 2>/dev/null | head -20",
  "description": "Find YAML config files for the project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -maxdepth 3 -name \"*.yaml\" -path \"*/recursive*\" 2>/dev/null | head -20",
    "description": "Find YAML config files for the project"
  }
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-21T06:30:08.781813+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1460 · 2026-05-21T06:30:11.844599+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1461 · 2026-05-21T06:30:11.895411+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-21T06:30:16.267088+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"external\\|paperreview\\|stanford\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Search for external review settings in project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"external\\|paperreview\\|stanford\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Search for external review settings in project config"
  }
}
```

</details>

---


### Tool result

_source line 1463 · 2026-05-21T06:30:16.367930+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1464 · 2026-05-21T06:30:21.442998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 1465 · 2026-05-21T06:30:22.550167+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf (482.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 1107
}
```

</details>

---


### Tool call

_source line 1466 · 2026-05-21T06:30:52.581799+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1467 · 2026-05-21T06:31:27.701976+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 35120
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-21T06:31:28.519480+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "你是 Reviewer 1，负责审查本论文的**方法严谨性、实验设计和统计有效性**。\n\n## 论文信息\n- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- **论文路径**: projects/recursive_gen_depth_est/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf\n\n## Venue 要求（EMNLP 2026，ARR May cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，主文严格 8 页，参考文献不限页数\n- **Limitations 章节**必须包含（不计入页数限制）\n- **模板**: ACL review 格式\n- **匿名规则**: Double-blind\n- **评分标准**: ARR 统一审稿，Overall Assessment 评分 1-5（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）\n\n## 你的审查侧重\n\n### 1. 实验方法论\n- benchmark 构建是否合理（3 model families × 3 decoding strategies × 4 depths）？seed 数据选择是否引入偏置？\n- LoRA fine-tuning 协议是否足够严谨（单一 seed=42，r=16/α=32）？每个 depth 从 base model 初始化 fresh adapter 的设计选择是否充分论证？\n- BOS-seeded generation 的生态效度问题——论文声称 prompted generation 仍有信号（-13.8pp），但这是否足以支撑其实际应用价值？\n- full-replacement 设定与真实 accumulation 场景的差距有多大？pilot experiments 仅报告了 -14 到 -15pp 衰减，是否足够？\n\n### 2. 统计有效性\n- 19 个 features 中 14-16 个 VIF>10——严重共线性下，feature importance 排名的可信度如何？论文引用了 Strobl/Hooker，但 group-level ablation 是否真正解决了这个问题？\n- 统计检验是否恰当？p-values 未做多重比较校正（论文 footnote 承认了 exploratory），但结论部分是否超出了 exploratory 范畴？\n- Bootstrap CI 的使用是否一致？部分结果有 CI，部分没有\n- cross-seed replication 仅 2 个 seed，OLMo +3.17pp 的差异是否说明结果对 LoRA seed 敏感？\n\n### 3. 核心指标 EDD\n- EDD 定义的 T=0.70 阈值选择——引用 Hosmer (2000) 是否合理？sensitivity analysis 仅测了 {0.65, 0.70, 0.80}，是否足够？\n- EDD 对 contiguous prefix 的要求是否过于限制性？14B 的 EDD=0 是因为 d0v1 不达标，但 d1v2 和 d2v3 仍有不错的 AUC\n- 14B 使用 self-reference 而非 Pythia-1.4B reference——这使得 14B 结果与主表不可直接比较，论文是否充分讨论了这个 confound？\n\n### 4. Transfer 和 Generalization\n- cross-model transfer d1-d3 仅 55.4%，cross-strategy 仅 45.9%——这些数字对于声称的实际应用价值意味着什么？\n- wild-data FPR 高达 22.4%（GPT-2 XL on C4）——confidence thresholding 减至 2.8% 但代价是什么？\n- 14B EDD=0 的结果是否从根本上限制了这个方法的实用性？\n\n### 5. Baseline 对比\n- 与 Binoculars 的对比：78.1% vs 78.4%（p>0.05）——如果 Binoculars 已经达到同等性能，本文 pipeline 的独特价值在哪里？\n- neural end-to-end baselines（DeBERTa, RoBERTa）的失败——仅测试了 ≤125M backbone，是否应该测试更大的 PLM？\n- downstream curation PoC 不显著（p>0.4）——这是否削弱了 depth estimation 的实用价值论述？\n\n请按照 ARR 审稿格式给出完整审稿意见：Summary → Strengths → Weaknesses（必须严格，不留情面） → Questions → Missing References → Overall Assessment（1-5 评分 + 置信度）→ Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "你是 Reviewer 1，负责审查本论文的**方法严谨性、实验设计和统计有效性**。\n\n## 论文信息\n- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- **论文路径**: projects/recursive_gen_depth_est/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf\n\n## Venue 要求（EMNLP 2026，ARR May cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，主文严格 8 页，参考文献不限页数\n- **Limitations 章节**必须包含（不计入页数限制）\n- **模板**: ACL review 格式\n- **匿名规则**: Double-blind\n- **评分标准**: ARR 统一审稿，Overall Assessment 评分 1-5（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）\n\n## 你的审查侧重\n\n### 1. 实验方法论\n- benchmark 构建是否合理（3 model families × 3 decoding strategies × 4 depths）？seed 数据选择是否引入偏置？\n- LoRA fine-tuning 协议是否足够严谨（单一 seed=42，r=16/α=32）？每个 depth 从 base model 初始化 fresh adapter 的设计选择是否充分论证？\n- BOS-seeded generation 的生态效度问题——论文声称 prompted generation 仍有信号（-13.8pp），但这是否足以支撑其实际应用价值？\n- full-replacement 设定与真实 accumulation 场景的差距有多大？pilot experiments 仅报告了 -14 到 -15pp 衰减，是否足够？\n\n### 2. 统计有效性\n- 19 个 features 中 14-16 个 VIF>10——严重共线性下，feature importance 排名的可信度如何？论文引用了 Strobl/Hooker，但 group-level ablation 是否真正解决了这个问题？\n- 统计检验是否恰当？p-values 未做多重比较校正（论文 footnote 承认了 exploratory），但结论部分是否超出了 exploratory 范畴？\n- Bootstrap CI 的使用是否一致？部分结果有 CI，部分没有\n- cross-seed replication 仅 2 个 seed，OLMo +3.17pp 的差异是否说明结果对 LoRA seed 敏感？\n\n### 3. 核心指标 EDD\n- EDD 定义的 T=0.70 阈值选择——引用 Hosmer (2000) 是否合理？sensitivity analysis 仅测了 {0.65, 0.70, 0.80}，是否足够？\n- EDD 对 contiguous prefix 的要求是否过于限制性？14B 的 EDD=0 是因为 d0v1 不达标，但 d1v2 和 d2v3 仍有不错的 AUC\n- 14B 使用 self-reference 而非 Pythia-1.4B reference——这使得 14B 结果与主表不可直接比较，论文是否充分讨论了这个 confound？\n\n### 4. Transfer 和 Generalization\n- cross-model transfer d1-d3 仅 55.4%，cross-strategy 仅 45.9%——这些数字对于声称的实际应用价值意味着什么？\n- wild-data FPR 高达 22.4%（GPT-2 XL on C4）——confidence thresholding 减至 2.8% 但代价是什么？\n- 14B EDD=0 的结果是否从根本上限制了这个方法的实用性？\n\n### 5. Baseline 对比\n- 与 Binoculars 的对比：78.1% vs 78.4%（p>0.05）——如果 Binoculars 已经达到同等性能，本文 pipeline 的独特价值在哪里？\n- neural end-to-end baselines（DeBERTa, RoBERTa）的失败——仅测试了 ≤125M backbone，是否应该测试更大的 PLM？\n- downstream curation PoC 不显著（p>0.4）——这是否削弱了 depth estimation 的实用价值论述？\n\n请按照 ARR 审稿格式给出完整审稿意见：Summary → Strengths → Weaknesses（必须严格，不留情面） → Questions → Missing References → Overall Assessment（1-5 评分 + 置信度）→ Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 1469 · 2026-05-21T06:31:52.579909+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24060
}
```

</details>

---


### Tool call

_source line 1470 · 2026-05-21T06:31:52.731098+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "你是 Reviewer 2，负责审查本论文的**新颖性、贡献充分性、Related Work 覆盖和写作质量**。\n\n## 论文信息\n- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- **论文路径**: projects/recursive_gen_depth_est/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf\n\n## Venue 要求（EMNLP 2026，ARR May cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，主文严格 8 页，参考文献不限页数\n- **Limitations 章节**必须包含（不计入页数限制）\n- **模板**: ACL review 格式\n- **匿名规则**: Double-blind\n- **评分标准**: ARR 统一审稿，Overall Assessment 评分 1-5（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 论文自称贡献在于 task formalization + systematic empirical characterization，而非 algorithmic novelty——这种\"无新算法\"的定位在 EMNLP 能否被接受？\n- 19 个 statistical features 都是标准统计量（perplexity percentiles, surprisal variance, n-gram repetition），Random Forest 也是标准分类器——方法层面的贡献在哪？\n- EDD metric 本质上是 pairwise AUC 的 contiguous prefix——这算一个有意义的 metric 创新吗？\n- Depth Degradation Atlas 的概念——是否只是一个系统性实验的花哨命名？\n- 与 Mohamed et al. (2025) \"Broken Telephone\" 的区别是否足够清晰？他们也做了 iterative generation 的 characterization\n\n### 2. 贡献充分性\n- 对于 EMNLP 2026 长文，3 条贡献是否足够？\n  - 贡献 1（Task formalization + EDD）：formalizing ordinal classification 是否算实质性贡献？\n  - 贡献 2（Depth Degradation Atlas）：empirical observation 集合是否有足够的 insight？\n  - 贡献 3（Systematic characterization）：cross-model 66.4%、cross-strategy 45.9%、14B EDD=0——这些数字是积极发现还是负面结果？\n- 实验规模限制在 1-1.5B，14B 结果 EDD=0——scope 是否过窄？\n- downstream curation PoC 不显著——是否缺少 convincing application scenario？\n\n### 3. Related Work 覆盖\n- 检查以下领域是否有遗漏的重要工作：\n  - Model collapse 最新进展（2025-2026）\n  - AI text detection 最新方法\n  - Data provenance / data auditing\n  - Ordinal classification in NLP\n  - Synthetic data quality assessment\n- 检查引用是否真实（无幻觉引用）——特别关注 2026 年的引用\n- Related Work 章节的组织和定位是否清晰？论文如何区分自己与最近的 detection 和 collapse 工作？\n\n### 4. 写作质量\n- Abstract 信息密度——6 个数字 + 3 findings 是否合理？是否仍然过载？\n- Introduction 的叙事流畅性——从 problem motivation → gap → approach → findings 的逻辑链是否清晰？\n- 术语一致性：depth estimation vs. depth classification，是否全文统一？\n- §6 Discussion 仅 3 小段——对于 8 页长文是否太压缩？\n- 论文整体的 claim calibration——是否过度声称（overclaim）或过于保守（underclaim）？\n- Appendix 长达 ~15 页——哪些内容应在主文中，哪些放 Appendix 合理？\n- Figure/Table 数量和质量：主文 3 figures + 6 tables 是否合理分布？\n\n### 5. 格式合规性\n- 主文是否严格 ≤8 页？（目前 Discussion 在第 8 页，Limitations 从第 9 页开始——需确认）\n- double-blind 匿名是否完整？是否有泄露作者身份的痕迹？\n- ACL 模板使用是否正确？\n- 参考文献格式是否一致？\n\n请按照 ARR 审稿格式给出完整审稿意见：Summary → Strengths → Weaknesses（必须严格，不留情面） → Questions → Missing References → Overall Assessment（1-5 评分 + 置信度）→ Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "你是 Reviewer 2，负责审查本论文的**新颖性、贡献充分性、Related Work 覆盖和写作质量**。\n\n## 论文信息\n- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- **论文路径**: projects/recursive_gen_depth_est/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf\n\n## Venue 要求（EMNLP 2026，ARR May cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，主文严格 8 页，参考文献不限页数\n- **Limitations 章节**必须包含（不计入页数限制）\n- **模板**: ACL review 格式\n- **匿名规则**: Double-blind\n- **评分标准**: ARR 统一审稿，Overall Assessment 评分 1-5（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 论文自称贡献在于 task formalization + systematic empirical characterization，而非 algorithmic novelty——这种\"无新算法\"的定位在 EMNLP 能否被接受？\n- 19 个 statistical features 都是标准统计量（perplexity percentiles, surprisal variance, n-gram repetition），Random Forest 也是标准分类器——方法层面的贡献在哪？\n- EDD metric 本质上是 pairwise AUC 的 contiguous prefix——这算一个有意义的 metric 创新吗？\n- Depth Degradation Atlas 的概念——是否只是一个系统性实验的花哨命名？\n- 与 Mohamed et al. (2025) \"Broken Telephone\" 的区别是否足够清晰？他们也做了 iterative generation 的 characterization\n\n### 2. 贡献充分性\n- 对于 EMNLP 2026 长文，3 条贡献是否足够？\n  - 贡献 1（Task formalization + EDD）：formalizing ordinal classification 是否算实质性贡献？\n  - 贡献 2（Depth Degradation Atlas）：empirical observation 集合是否有足够的 insight？\n  - 贡献 3（Systematic characterization）：cross-model 66.4%、cross-strategy 45.9%、14B EDD=0——这些数字是积极发现还是负面结果？\n- 实验规模限制在 1-1.5B，14B 结果 EDD=0——scope 是否过窄？\n- downstream curation PoC 不显著——是否缺少 convincing application scenario？\n\n### 3. Related Work 覆盖\n- 检查以下领域是否有遗漏的重要工作：\n  - Model collapse 最新进展（2025-2026）\n  - AI text detection 最新方法\n  - Data provenance / data auditing\n  - Ordinal classification in NLP\n  - Synthetic data quality assessment\n- 检查引用是否真实（无幻觉引用）——特别关注 2026 年的引用\n- Related Work 章节的组织和定位是否清晰？论文如何区分自己与最近的 detection 和 collapse 工作？\n\n### 4. 写作质量\n- Abstract 信息密度——6 个数字 + 3 findings 是否合理？是否仍然过载？\n- Introduction 的叙事流畅性——从 problem motivation → gap → approach → findings 的逻辑链是否清晰？\n- 术语一致性：depth estimation vs. depth classification，是否全文统一？\n- §6 Discussion 仅 3 小段——对于 8 页长文是否太压缩？\n- 论文整体的 claim calibration——是否过度声称（overclaim）或过于保守（underclaim）？\n- Appendix 长达 ~15 页——哪些内容应在主文中，哪些放 Appendix 合理？\n- Figure/Table 数量和质量：主文 3 figures + 6 tables 是否合理分布？\n\n### 5. 格式合规性\n- 主文是否严格 ≤8 页？（目前 Discussion 在第 8 页，Limitations 从第 9 页开始——需确认）\n- double-blind 匿名是否完整？是否有泄露作者身份的痕迹？\n- ACL 模板使用是否正确？\n- 参考文献格式是否一致？\n\n请按照 ARR 审稿格式给出完整审稿意见：Summary → Strengths → Weaknesses（必须严格，不留情面） → Questions → Missing References → Overall Assessment（1-5 评分 + 置信度）→ Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 1471 · 2026-05-21T06:31:54.447624+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1716
}
```

</details>

---


### Assistant

_source line 1472 · 2026-05-21T06:32:04.401775+00:00_

**Round 1 已启动**：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法严谨性 + 实验设计 + 统计有效性 |
| Reviewer 2 | ✅ 已派发 | 新颖性 + 贡献充分性 + Related Work + 写作 |
| 视觉审查 Agent | ✅ 已启动 | PDF 排版质量（非评分项） |
| 外部审稿 | ⏭ 跳过 | 项目未配置 paperreview.ai |

等待 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 131

## Round 131

2 recorded events


### User

_source line 1473 · 2026-05-21T06:37:00.369250+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 方法严谨性、实验设计和统计有效性

---

## Summary

本文将递归生成深度估计形式化为序数分类问题，构建了覆盖 3 个模型族 × 3 种解码策略 × 4 个深度的 180K 样本基准，从参考模型（Pythia-1.4B）的困惑度分布中提取 19 个统计特征，使用 Random Forest 分类器。提出 Effective Discriminable Depth (EDD) 作为可区分深度的度量指标。分布内准确率 68.9–85.9%，但跨模型迁移降至 66.4%（d1-d3: 55.4%），跨策略降至 59.1%（d1-d3: 45.9%），14B 规模下 EDD=0。论文同时报告了多项消融实验和负面结果。

---

## 总体评分

**Overall Assessment**: 3.0 — Findings
**一句话总结**: 问题提出新颖、实验体系全面、负面结果报告诚实，但 full-replacement 假设、14B EDD=0、跨策略迁移仅 45.9%、以及 Binoculars 达到统计等价性能等核心限制，使其实用价值论述不充分，达到 Findings 但未及主会议门槛。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 控制实验层面方法论合理，但严重共线性下的特征重要性分析可信度存疑，LoRA seed 复制不足，full-replacement 与真实累积场景差距大 |
| Excitement | 3.0/5 | 问题提出新颖（递归深度估计 vs 二元检测），但实用限制严重（规模不可扩展、策略依赖、Binoculars 近平局），削弱了 excitement |
| Reproducibility | 4/5 | 超参数详细列出（Table 7, Appendix A），承诺公开代码和数据，但 14B 实验和累积试点缺乏充分细节 |
| Confidence | 4/5 | 通读全文含全部 24 页附录，熟悉 AI 生成文本检测和模型坍塌相关工作 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Full-replacement 假设从根本上限制了实用价值论述
- 具体位置：§3.2（Generation pipeline）、Limitations §1、§6 Discussion "From ceiling to floor"
- 问题：所有实验使用 full-replacement 递归链——每个深度完全替换前一代训练语料。但论文声称的应用场景（§6 "depth-scored data curation"）面对的是累积（accumulation）场景，即合成和人类数据以未知比例共存。论文仅在 Limitations 中提及 pilot accumulation 实验显示 -14 到 -15pp 衰减，但未给出任何详细数据（无 Table、无 per-cell 分解、无 EDD 变化、无统计检验）。
- 为什么影响接收：这不是 minor caveat——而是方法是否具有实际可部署性的根本前提。如果累积场景下特征分离度大幅下降，论文的核心价值主张（"estimating recursive generation depth for data curation"）即失去实验支撑。-14 到 -15pp 是 full-replacement baseline 的 ~18% 相对衰减，可能使部分 cell 的 d1-d3 准确率降至接近 chance。
- 建议修改方向：(1) 报告累积实验的完整结果（至少 2-3 个混合比例 × 全部 9 cells 的子集）；(2) 量化 EDD 在累积设定下的变化；(3) 或者将实用价值论述限缩为 "controlled upper bound study"，不声称数据审计应用。

**N2** [critical] 14B EDD=0 且跨规模对比被 confound（self-reference）
- 具体位置：§5.4、Appendix B.14（Table 15, Table 16）、Limitations §2
- 问题：Qwen2.5-14B 使用 self-reference（14B 模型自身计算特征）而非 Pythia-1.4B。这意味着 14B 的结果与主表（Table 2）不可直接比较——观察到的 EDD=0 可能部分来自参考模型切换而非纯粹的规模效应。论文在 Appendix B.14 "Confounds" 段承认了这一点，但未做任何控制实验来分离两个因素（例如：用 Pythia-1.4B 作为 14B 的参考模型，或用 self-reference 重跑 1-1.5B 实验）。
- 为什么影响接收：14B 是论文最重要的 generalization 结果之一。如果 EDD=0 是 self-reference 的 artifact 而非规模效应，论文的 "scale-dependent attenuation" 叙事（§3.5 Theory, §6 Discussion）就缺乏实验支撑。鉴于当前主流模型 >14B，这个 boundary condition 对方法的前景至关重要。
- 建议修改方向：(1) 用 Pythia-1.4B 作为 14B 的 cross-reference 模型重跑 EDD 分析；(2) 对 1-1.5B 模型运行 self-reference 作为对照（Appendix B.21 仅在 Qwen2.5-1.5B-Instruct 上做了，且该模型也是 instruction-tuned，引入额外 confound）；(3) 明确讨论无法分离 scale vs. reference-model confound 的后果。

**N3** [critical] 跨策略迁移 d1-d3 仅 45.9%，实质上否定了 "unknown strategy" 部署场景
- 具体位置：§5.3、Table 6、Appendix B.28
- 问题：跨策略迁移将 d1-d3 balanced accuracy 降至 45.9%（4-class: 59.1%），仅 1.4× chance。d0 recall ≥89% 膨胀了 headline accuracy。在真实部署中，解码策略通常未知。论文提出的 two-stage pipeline（策略识别 + per-strategy 分类）恢复了 11.5pp，但"presupposes known or identifiable strategy"（§5.3）——这是循环依赖。更严重的是，Appendix B.7 的跨温度实验显示 leave-one-τ-out mean d1v2 AUC 仅 0.319，甚至在 τ=0.5 holdout 时出现 inverted AUC (0.176)——同一解码族内部的迁移都不可靠。
- 为什么影响接收：论文的核心价值主张之一是 "auditing pipelines must account for decoding configuration"（§6），但如果策略未知则方法基本失效（d1-d3 接近 chance），这与声称的 data provenance 应用场景根本矛盾。
- 建议修改方向：(1) 在 §6 中明确将 claim 限定为 "within-strategy or known-strategy"，而非泛泛的 "auditing pipelines"；(2) 探索 strategy-agnostic 特征或 domain adaptation 方法；(3) 将跨策略的极低迁移率作为 core finding 而非 limitation 讨论。

**N4** [critical] 严重共线性（VIF>10, 14-16/19 features）下特征重要性分析的可信度
- 具体位置：§4.2、Table 3、Figure 1、Appendix B.2
- 问题：19 个特征中 14-16 个 VIF>10，有效独立维度仅 ~4-5（§3.3）。在此共线性水平下，Gini importance、SHAP、permutation importance 的个体特征排名均不可靠——微小的数据扰动可导致排名大幅变动。论文引用 Strobl et al. (2008) 和 Hooker et al. (2021)，声称 permutation importance 部分缓解了共线性偏差，但 conditional permutation importance 要求对条件分布的正确建模，而论文并未使用 conditional 版本——仅使用了标准 permutation importance。Group-level ablation（§4.2: perplexity 76.6%, full 78.4%）确实提供了 family-level 信息，但论文在 Table 3 中给出了 per-cell 的 top-5 个体特征排名并大量讨论，overstates 了在此共线性条件下可靠推断的范围。
- Kendall's W=0.90 across 3 methods 并不能反驳共线性——如果 3 种方法都受同一组相关特征影响，一致性高反而证实了系统性偏差。
- 为什么影响接收：特征分析是论文三大贡献之一（"perplexity tail features dominate"）。如果个体特征排名不可靠，这一贡献的可信度大打折扣，只能保留 family-level 的粗粒度结论。
- 建议修改方向：(1) 使用 conditional permutation importance（Strobl 2008 原文方法）而非标准 permutation importance；(2) 减少对个体特征排名的讨论，将叙事集中在 group-level ablation 上；(3) 报告 bootstrap 或 subsampling 下的排名稳定性（例如 rank stability across 100 bootstrap samples）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] LoRA seed 仅 2 个，OLMo +3.17pp 差异 CI 不重叠
- 具体位置：Appendix B.16, Table 20
- 问题：Cross-seed replication 仅使用 seeds 42 和 43。OLMo 从 78.94% 升至 82.11%（+3.17pp），95% CI 不重叠——这说明 LoRA 初始化对绝对准确率有非平凡影响。对于声称发现 "stable statistical fingerprints" 的论文，2 个 seed 不足以建立稳定性。GPT-2 XL 也有 +2.04pp（CI 不重叠）。Pythia 的 +0.14pp 可能只是因为 self-reference 效应掩盖了 seed 敏感性。
- 建议：至少 5 个 seed，报告 mean ± std，展示特征排名跨 seed 的一致性。

**W2** [warning] 多重比较校正缺失，但结论超出 exploratory 范畴
- 具体位置：§3.4 脚注、§6 Discussion、Abstract
- 问题：脚注明确声明 "p-values should be interpreted as exploratory"。但 Abstract 使用确定性语言（"consistent in direction but scale-dependent in magnitude"），§6 给出明确的 deployment 建议（"score each passage for estimated recursive depth and filter or down-weight"）。这在 exploratory methodology 和 confirmatory conclusions 之间存在不一致。特别是 Appendix B.12 Curation PoC 中 RF-vs-random 的显著性检验（p<0.02）涉及多重比较但未校正（论文自己承认了这一点）。
- 建议：(1) 对 Table 2 的 9-cell 比较和 Table 15 的 pairwise contrasts 应用 Bonferroni 或 FDR 校正；(2) 将 Abstract 和 §6 的语言调整为与 exploratory 定位一致。

**W3** [warning] Neural end-to-end baselines 仅测试 ≤125M backbone
- 具体位置：§5.1、Appendix B.9、Table 4
- 问题：DeBERTa-v3-base (~86M) 和 RoBERTa-base (~125M) 比 RF 低 20pp，论文据此结论 "depth estimation benefits from targeted statistical features that capture distributional tail properties absent from PLM representations"。但 PLM 的表征能力与规模强相关。Appendix B.9 的 linear probing 结果（var_surprisal 和 p90_ppl 的 R²<0）来自 base 模型——使用更大的 PLM（如 DeBERTa-v3-large 或 7B 模型 + LoRA）可能改变结论。论文也承认这是 open question（Appendix B.9 末尾）。
- 建议：测试至少一个 >1B 参数的 end-to-end baseline（例如 DeBERTa-v3-large 的稳定配置，或 Llama-3.1-8B + classification head），或将 claim 严格限定为 "at ≤125M scale"。

**W4** [warning] BOS-seeded generation 的生态效度问题
- 具体位置：§3.2 Generation pipeline、Appendix B.27
- 问题：主实验使用 BOS-seeded generation（从 BOS token 开始生成），这产生的文本具有最大化的分布指纹——没有 prompt 约束，模型完全自由地展示其分布偏差。Prompted generation 实验（Appendix B.27, Table 29）显示准确率降至 69.5%（-13.8pp），但这仅测试了 topic-seeded 而非 instruction-following 场景。对于声称 data curation 应用的论文，instruction-following（如 ChatGPT 风格）的生成才是最相关的场景，但未被测试。
- 建议：在至少一个 instruction-tuned 模型上测试 instruction-prompted generation 的分类性能。

**W5** [warning] Binoculars 达到统计等价性能（78.1% vs 78.4%, p>0.05），削弱独特价值
- 具体位置：§5.1、Table 4
- 问题：Binoculars 使用 11 个跨困惑度特征 + RF 校准即达到 78.1%（vs. 论文 pipeline 的 78.4%，p>0.05）。合并 30 特征后 82.6%，但这更像 "augmenting Binoculars with depth features" 而非 standalone pipeline 的贡献。论文声称 "our pipeline needs only a single 1.4B reference model vs. Binoculars' 1.8B observer-performer pair"——但这是效率优势而非性能优势。
- 建议：更精确地定位本文贡献——是 formulation/benchmark 的贡献而非 method 的性能优势；或展示在 Binoculars 不适用的场景（如单一模型可用时）本方法的独特价值。

**W6** [warning] Wild-data FPR 高达 22.4%（GPT-2 XL on C4），confidence thresholding 的 recall 代价未充分表征
- 具体位置：Appendix B.11, Table 13
- 问题：C4 上 GPT-2 XL 的 FPR 为 22.4%。Confidence thresholding (P(d0)≥0.15) 降至 2.8%，但 balanced accuracy 仅降 0.3pp (78.0%→77.7%)。然而，这个 "balanced accuracy" 是在 in-distribution 数据上评估的——thresholding 将 33% 的样本归入 uncertainty zone，这些被 abstained 的样本的深度分布特征未报告。在 wild data 上，thresholding 后的 recall 和 coverage 未给出。
- 建议：报告 thresholding 后在 C4 上的 coverage（被 abstain 的比例）和残余 FPR，给出 FPR-coverage tradeoff curve。

---

## 小问题（不影响接收）

1. **EDD 灵敏度分析仅测试 3 个阈值 {0.65, 0.70, 0.80}**（§3.4）。连续的 T vs. EDD 曲线（如 T 从 0.5 到 0.95 以 0.05 步长）更有信息量。

2. **EDD 的 contiguous prefix 要求可能过于限制性**。14B nucleus 下 d1v2 AUC=0.713, d2v3=0.728 均接近 0.70 阈值，但因 d0v1=0.643 未达标，EDD 直接为 0。一个 "best contiguous window" 或 "average pairwise AUC" 的替代度量可能更有信息量。

3. **Table 2 (main results) 的 CI 报告不一致**：主表有 bootstrap CI，但 Table 5 (cross-model) 和 Table 6 (cross-strategy) 没有。

4. **Appendix B.10 Domain Bias Analysis 中报告了 buggy pipeline 的数字**（LOGO 64.0%, seed-group 20.8%）以及修正后的结果——虽然透明可敬，但增加了阅读负担。建议将 buggy 数字放到脚注。

5. **理论部分（§3.5）的 EDD upper bound 论证依赖 tail mass 的 α^k 几何衰减假设**，引用了 Dohmatob et al. (2024)，但未验证该假设在本文的 LoRA fine-tuning 设定下是否成立（vs. full fine-tuning）。

---

## 主要优势

1. **问题提出新颖且重要**：从二元检测（human vs. AI）扩展到递归深度估计是一个自然但未被探索的方向。在 model collapse 日益受到关注的背景下，这个问题具有前瞻性。

2. **极其系统的实验设计**：3×3×4 grid + 180K 样本、8 个 generalization axis、24 页附录覆盖了几乎所有可预见的消融。这是我近期审稿中见过的最全面的 empirical study 之一。

3. **诚实报告负面结果**：14B EDD=0、curation PoC 不显著（p>0.4）、跨策略迁移低——这些结果被清晰报告而非隐藏，提升了论文的可信度。

4. **理论框架与实验发现的良好对应**：tail erosion 理论（§3.5）预测 perplexity tail 特征应主导，group-level ablation 确认了这一点（76.6% vs. 78.4% full）。scale-dependent attenuation 的理论预测在 14B 实验中得到验证。

5. **控制实验设计精细**：heterogeneous chain + reverse-chain control（Appendix B.15）、LOGO + negative control 消除 domain bias（Appendix B.10）、temperature robustness + memorization-prerequisite 发现（Appendix B.7）均展示了高水平的实验设计。

6. **EDD 作为新度量有独立价值**：将 "可区分深度" 形式化为一个操作性定义，可被后续工作采用。

---

## Questions to Authors

1. 能否提供累积（accumulation）场景下的完整结果（即使只覆盖部分 cells），包括 accuracy、EDD、per-class recall？pilot 中 -14 到 -15pp 的衰减是在哪个 cell 上测的？

2. 14B 实验中，是否有技术原因无法使用 Pythia-1.4B 作为 cross-reference？如果用 Pythia-1.4B 对 Qwen2.5-14B 文本做特征提取，预期结果如何？

3. 跨策略迁移中，是否尝试过 normalization-based domain adaptation（如 feature-space 的 z-score normalization per strategy）？

4. 对于 Binoculars 近平局的结果，作者如何定位本文的独特贡献——是 formulation/benchmark，还是 method 本身？

---

## Missing References

- Liang et al. (2023), "GPT Detectors Are Biased Against Non-Native English Writers" — 与 FPR 偏差分析相关
- Sadasivan et al. (2023) 的 impossibility result 已被引用，但论文未讨论其对 ordinal 设定的含义
- Hans et al. (2024), "Spotting LLMs With Binoculars" — 已引用，但应更详细对比 cross-perplexity vs. single-reference 方法在 ordinal setting 下的理论差异

---

## Overall Assessment

**评分**: 3.0 (Findings)
**置信度**: 4/5

本文在一个新颖且有前景的问题上进行了极为系统的实证研究，实验覆盖面在该领域中罕见。但核心限制——full-replacement 假设的非现实性（N1）、14B 的 confounded EDD=0（N2）、跨策略迁移的低下（N3）、以及共线性下特征分析的可信度（N4）——共同构成了一个结论：论文更适合作为一项高质量的 empirical characterization study（适合 Findings），而非具有明确实用价值的方法论贡献（所需的 Conference 水平）。Binoculars 的近平局（W5）进一步削弱了 method 层面的 novelty。

如果作者能在 rebuttal 中提供：(1) 累积场景的完整结果，(2) 14B 的 cross-reference 对照实验，(3) 更大 PLM backbone 的 end-to-end baseline，那么评分有望提升至 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1474 · 2026-05-21T06:37:07.637127+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 132

## Round 132

2 recorded events


### User

_source line 1475 · 2026-05-21T06:37:26.724572+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿意见，核心结论：

**Overall: 3.0 (Findings)**，置信度 4/5。

4 个 Must-Fix 问题：
1. **Full-replacement 假设**限制实用价值——累积场景仅有 pilot 数据（-14~-15pp），无完整报告
2. **14B EDD=0 被 self-reference confound**——与主表不可比，无法分离规模效应 vs 参考模型切换
3. **跨策略迁移 d1-d3 仅 45.9%**——策略未知时方法基本失效，与 data provenance 应用场景矛盾
4. **VIF>10 的严重共线性**下个体特征排名不可靠——论文 overstate 了可推断范围

6 个 Should-Fix：LoRA seed 不足、多重比较未校正、neural baseline 仅≤125M、BOS-seeded 生态效度、Binoculars 近平局削弱 novelty、wild-data FPR tradeoff 未充分表征。

论文优势在于问题新颖、实验极其系统（24页附录）、负面结果诚实报告。如能补充累积实验完整结果、14B cross-reference 对照、更大 PLM baseline，评分可望提升至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1476 · 2026-05-21T06:37:32.893218+00:00_

Reviewer 1 初审已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 133

## Round 133

6 recorded events


### User

_source line 1477 · 2026-05-21T06:40:17.567538+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见 — Round 1

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 新颖性、贡献充分性、Related Work 覆盖、写作质量

---

## Summary

本文将"递归生成深度估计"（recursive generation depth estimation）形式化为序数分类任务（ordinal classification，$d \in \{0, 1, \ldots, K\}$），构建了一个 180K 样本的基准数据集（3 个模型族 × 3 种解码策略 × 深度 0–5），提取 19 个标准统计特征（perplexity 分位数、surprisal 方差、n-gram 重复率等），使用 Random Forest 分类器进行深度估计。论文提出 Effective Discriminable Depth (EDD) 指标，并报告了跨模型迁移 66.4%、跨策略迁移 45.9%、14B 模型 EDD=0 等结果。论文定位为"task formalization + systematic empirical characterization"而非 algorithmic novelty。

---

## 总体评分

**Overall**: 3.0 / 5 — Findings
**一句话总结**: 问题动机扎实、实验方法论严谨，但缺乏任何方法层面的创新，且 14B EDD=0 的结果严重削弱了实际应用价值，达不到主会议 novelty/impact 门槛，处于 Findings 接收线。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | 方法论合理，实验设计系统（180K 样本、5-fold CV、多维度 ablation），但 full-replacement 假设偏离现实场景，14B 仅单模型验证 |
| **Excitement** | 2.0 / 5 | 问题本身有意义，但 19 个标准统计量 + 标准 RF 分类器无方法创新；14B EDD=0 使整个框架在实际规模上失效，实用前景堪忧 |
| **Reproducibility** | 4.0 / 5 | 数据集构建流程清晰（Appendix A），超参数完整（B.29），承诺开源代码和数据。特征提取管道可复现。 |
| **Overall Assessment** | 3.0 / 5 | Findings 级别：empirical 贡献扎实但 novelty 不足以支撑 long paper 主会议录用 |

**Reviewer Confidence**: 4 / 5 — 熟悉 model collapse、AI text detection 和 data provenance 文献

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 方法层面零创新，novelty 不足以支撑 EMNLP long paper

- 具体位置：§3.3 (Statistical Feature Design), §3.4 (EDD), §4 全节
- 问题：论文明确自称"无新算法"定位（Introduction 第 5 段："our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty"）。但 19 个特征全部是标准统计量（perplexity percentiles, surprisal moments, n-gram repetition rates）；分类器是标准 Random Forest（500 棵树）；EDD 本质上是 contiguous pairwise AUC 的最长前缀。整个方法管道中没有任何需要智力投入的设计选择——任何有统计学基础的研究者拿到 perplexity 分布后都会计算这些统计量。
- 为什么影响接收：EMNLP 2026 即使接受 empirical study，也期望有 non-trivial 的 insight 或方法论贡献。纯粹"标准特征 + 标准分类器 + 大规模实验"的组合在 novelty 维度上不满足 Conference 录用门槛（ARR Excitement ≥ 3 通常是主会议底线）。对比 EditLens（Thai et al., 2026）提出了新的 editing extent quantification 方法，或 Binoculars（Hans et al., 2024）提出了 cross-model perplexity ratio 的新思路——本文缺少类似层次的方法贡献。
- 建议修改方向：(1) 探索 learned features（如基于 PLM representation 的深度估计器），与 handcrafted 特征对比；(2) 设计针对 ordinal structure 的损失函数或架构（超越简单 RF）；(3) 将 EDD 发展为一个有理论保障的 metric（如证明其与信息论量的关系）。

**N2** [critical] 14B EDD=0 严重削弱框架的实际适用性，但论文未充分讨论

- 具体位置：§5.4（第 8 页第 1 列），Appendix B.14, B.17
- 问题：14B（Qwen2.5-14B）实验结果 EDD₁₄ᵦ=0，即相邻深度间完全不可区分。论文承认 "adjacent-depth discrimination does not survive the scale transition"。但当前主流 LLM 均为 7B–70B 规模，1–1.5B 模型生成的文本在实际中占比极小。这意味着本文的整个框架——task formalization、benchmark、EDD metric——在实际场景中**完全失效**。Appendix B.17 中 7-8B 结果也不乐观：EDD 仅 0.56–0.64，四分类准确率勉强超过 chance。
- 为什么影响接收：如果核心方法在 target use case（>7B 模型）上不 work，论文的贡献就退化为纯学术性的 toy-scale observation。审稿人和 AC 会质疑实际影响力。
- 建议修改方向：(1) 需要**深入分析**为什么特征在 scale up 后失效（不仅仅是"feature signature shifts"一句话）；(2) 探索是否有不同类型的特征（如 semantic coherence、factual consistency）可以在大模型上 work；(3) 至少在 Discussion 中诚实地将 scope 限定为 "small-scale model forensics"，而非暗示通用性。

**N3** [critical] 跨策略迁移 45.9% 几乎等同 random，实用性存疑

- 具体位置：§5.3（Table 6），§5.2（Confusion matrix, Table 5/Figure 3）
- 问题：Cross-strategy transfer 的 d1–d3 balanced accuracy 仅 45.9%，四分类 chance 为 25%——虽然高于 random 但实际场景中解码策略通常未知。Table 6 显示 nucleus 和 temperature 互相迁移尚可，但 top-k 作为 holdout 时准确率骤降至 51.5%。结合 cross-model 迁移的 66.4%（Table 5），实际场景（模型和策略均未知）的迁移性能预期更差。
- 为什么影响接收：论文 Introduction 暗示这是一个实际的 data curation 工具（"whether depth estimation translates to actionable data curation"），但当模型和策略均未知时，分类器几乎不可用。这与论文的 motivation 存在根本矛盾。
- 建议修改方向：明确论文 scope 为 known-model/known-strategy 分析工具；或开发 strategy-agnostic 特征（如移除 strategy-specific 的 n-gram 特征，仅保留 perplexity tail 特征后重新评估）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Depth Degradation Atlas" 概念过度包装

- 具体位置：§4 全节（标题 + 内容）
- 问题："Atlas" 一词暗示一个全面的、权威的映射图谱。但实际内容是：(1) per-cell 四分类结果（Table 2），(2) 特征重要性分析（Table 3, Figure 1），(3) AUC 衰减曲线（Figure 2），(4) 跨策略特征轨迹定性描述。这本质上就是"一系列标准实验结果的系统性呈现"——在其他 empirical 论文中这叫 "Results" 或 "Analysis"。用 "Atlas" 命名有 overclaiming 之嫌。
- 建议：降格为 "Systematic Analysis of Depth Degradation Patterns" 或类似表述，或者真正扩展到 atlas 级别（更多模型、更多域、更多语言）。

**W2** [warning] Full-replacement 假设偏离现实，accumulation 实验不足

- 具体位置：§3.2 (Benchmark Construction)，§6 Discussion 第 3 段
- 问题：论文使用 full-replacement chain（每个深度完全替换上一轮训练数据），但现实中的 data contamination 是 accumulation 模式（新旧数据混合）。论文自己在 Discussion（第 8 页）承认 "full-replacement vs. accumulation" 的差距，并引用 Gerstgrasser et al. (2024) 表明 accumulation 可以避免 collapse。Appendix 中的 accumulation pilot 显示特征值比 full-replacement 低 14–19 pp——但仅作为一个简短的 appendix 段落处理，缺乏系统实验。
- 建议：至少在主文中正式讨论 full-replacement 假设的限制及其对结论外推性的影响；理想情况下增加 accumulation 实验的比例（如 10%、30%、50% 合成数据混合）。

**W3** [warning] §6 Discussion 过于压缩

- 具体位置：§6（第 8 页，3 小段）
- 问题：Discussion + Conclusion 合计仅 3 段约 250 词，对于 8 页 long paper 严重不足。缺少以下关键讨论：(1) 与 detection-based approach 的深度比较（depth estimation 相对于 binary detection 的额外价值是什么？）；(2) 对 data curation pipeline 的具体 implications（downstream PoC 不显著后如何定位实际价值？）；(3) scale-up 路径（如何从 1.5B 扩展到 >7B？）；(4) 当 strategy-specific features 是主导因素时，depth 信号和 strategy 信号如何解耦？
- 建议：拆分 Discussion 和 Conclusion 为两个独立 section；扩展 Discussion 至少到半页，覆盖上述四个方面。

**W4** [warning] Abstract 信息过载

- 具体位置：Abstract（第 1 页）
- 问题：Abstract 包含 6 个具体数字（59–82%, 66.4%, 45.9%, d1–d3, 19, 180K）加 3 个 findings（perplexity tail dominance, scale-dependent, strategy-dependent trajectories）。读起来像结果摘要而非研究叙事。Key finding "14B EDD=0" 被放在最后一句，但这可能是最重要的实际发现。
- 建议：删减 2-3 个数字，保留最核心的 takeaway；重组叙事流（problem → why it matters → what we found → what this means），将 14B 结果提到更显著位置。

**W5** [warning] 下游 curation PoC 不显著（§B.12 / B.22），但 Introduction 暗示实际应用

- 具体位置：Appendix B.12（Table 14–15），B.22（Appendix B.22 downstream fine-tuning）
- 问题：Downstream curation PoC（§B.12）显示 RF-based filtering 的 perplexity 改善（F1=0.997）但 pairwise comparison（Table 15）仅 3/10 contrasts 达到 p<0.05，且 Δ PPL 值很小。Introduction 和 §6 暗示 depth estimation 可服务于 data curation，但实验证据不支持这一声明。
- 建议：要么提供更 convincing 的 downstream application（如在实际 fine-tuning 中 depth-aware filtering 显著提升模型质量），要么在 claim 中弱化应用承诺。

---

## 小问题（不影响接收）

- **术语不一致**：主文中混用 "depth estimation" 和 "depth classification"（§3.1 第 1 段 "this is an ordinal classification problem" vs. 标题 "Estimating"），建议统一。
- **Table 1 可读性**：19 个特征分 4 类展示过于紧凑，特征名（如 p10, p25, p50, p75, p90）缺乏直观解释，首次出现时需要更多说明。
- **Figure 2 的 y 轴标签**：图例中 "Bootstrap 95% CI" 的 shaded band 在黑白打印下不易区分。
- **orphan bib entry**：`penedo2024_fineweb`（FineWeb 数据集）在 bib 中但未被任何 \cite 引用。
- **Appendix 结构**：15 页 appendix 涵盖 B.1–B.29 共 29 个子节，编号但缺乏层级组织，难以导航。建议按主题分组（Feature Analysis / Generalization / Ablation / Baselines）。

---

## 主要优势

1. **问题动机充分且及时**：随着合成数据在训练管线中的渗透，递归生成深度估计是一个尚未被充分研究的实际需求。论文在 Introduction 中清晰地从 model collapse → detection gap → depth estimation 建立了逻辑链。
2. **实验方法论严谨**：180K 样本基准、3 模型族 × 3 策略 × 6 深度的系统设计、5-fold stratified CV、多维度 ablation（cross-model / cross-strategy / cross-scale / cross-domain / seed replication / accumulation）展示了高水准的实验工程。
3. **诚实报告负面结果**：14B EDD=0（§5.4）、cross-strategy 45.9%（§5.3）、downstream PoC 不显著等负面结果均被坦诚报告，没有 cherry-picking 或隐藏不利证据。
4. **Perplexity tail statistics 发现有洞察力**：p90_ppl 在所有 9 cells 中排名 top-2（Table 3, Figure 1），与 surprisal variance 共同占据 41% Gini importance，提供了可解释的 depth marker。
5. **EDD metric 设计合理**：基于 contiguous pairwise AUC 的 longest discriminable prefix 定义简洁，operationalize 了 "多深可以区分" 的问题。
6. **Related Work 覆盖面广**：76 篇引用覆盖 model collapse theory、AI text detection、data provenance、ordinal classification、decoding strategies 五个相关领域，引用验证显示绝大多数引用真实可查。

---

## Related Work 覆盖评估

### 覆盖充分的领域
- **Model collapse**: Shumailov (2024), Dohmatob (2024/2025), Alemohammad (2024), Gerstgrasser (2024), Kazdan (2025), Schaeffer (2025), 以及 2026 年新工作（Sigma, Bakshi, Wang, Falahati, Yi）——覆盖全面。
- **AI text detection**: DetectGPT, Fast-DetectGPT, Binoculars, DivEye, Ghostbuster, GLTR, DNA-GPT, BiScope, watermarking, RAID 等——覆盖全面。
- **Ordinal classification**: CORAL, CLOC, Frank (2001), McCullagh (1980), Kasa (2024)——覆盖合理。

### 可能遗漏的工作
1. **"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing"** (2025, arXiv:2502.15208)——直接研究 iterative paraphrasing 的 attractor dynamics，与本文的递归生成链高度相关。
2. **"The Canary's Echo: Auditing Privacy Risks of LLM-Generated Synthetic Text"** (2025, arXiv:2502.14921)——从 data auditing 角度研究合成文本，与 §2 Data Provenance 子节相关。
3. **"Data Provenance Auditing of Fine-Tuned Large Language Models with a Text-Preserving Technique"** (2025, arXiv:2510.09655)——数据来源审计，与论文的 provenance 动机相关。

### 引用验证结果
- 76 条 bib entries，OpenAlex 验证 64 条 verified，8 条 not_found（其中 DetectGPT、RoBERTa、Qwen2.5、Datamodels 为知名论文的索引问题），4 条 mismatch（主要是 first author ordering）。
- **所有 2025-2026 年引用均已验证为真实论文**（knowledge_collapse2025 → arXiv:2509.04796，falahati2026_curated → arXiv:2605.07724，geng2026_markovian → arXiv:2603.11228）。无幻觉引用。
- 1 条 orphan bib：penedo2024_fineweb（在 bib 中但未被引用）。

---

## Questions for Authors

1. 是否尝试过 learned features（如 PLM hidden states 的深度预测）？Appendix B.9 中的 end-to-end DeBERTa/RoBERTa 实验仅在 surface text 上训练，是否考虑过用 reference model 的 internal representation 作为特征？
2. 14B EDD=0 的根因分析：是因为 14B 模型的 perplexity 分布本身方差更小（生成质量更高），还是因为 fine-tuning 在大模型上更 "gentle"？是否有 per-feature 的 scale-dependent 分析？
3. 深度 >5 时是否存在 saturation？Figure 2 的 AUC 衰减曲线只到 d=5，是否有更深的初步数据？
4. Cross-domain transfer（§B.10, B.11）仅在 WikiText-103 上测试。是否考虑过 code、dialogue、scientific text 等更多样化的域？
5. 论文是否考虑过将 depth estimation 与 model attribution 结合？例如 Bevendorff et al. (2025) 的 two-paradigm framework 是否可以扩展到 depth-aware attribution？

---

## 格式合规性检查

- **页数**: ✅ 主文 8 页（pp.1–8），Limitations 从第 9 页开始（不计入限制），参考文献 pp.9–11，Appendix pp.12–24。合规。
- **匿名**: ✅ 标题页标注 "Anonymous ACL submission"，全文未发现作者身份泄露。Ethics Statement 中 "code and data will be released upon acceptance" 表述合规。
- **模板**: ✅ 使用 ACL 2023 模板（acl.sty）。
- **参考文献格式**: ⚠️ 基本一致，但部分条目年份与 OpenAlex 记录有 1 年出入（如 holtzman2020 实际发表于 ICLR 2020 但预印本为 2019）——这是常见问题，不构成格式错误。
- **Limitations section**: ✅ 存在（第 9 页），覆盖 full-replacement 假设、scale 限制、caveats。内容合理但可更具体（见 W2）。

---

## 最终判断

本文选择了一个有价值的研究问题（递归生成深度估计），实验方法论和执行质量均属上乘。但核心贡献停留在"标准工具的系统性应用"层面，缺乏方法论创新。更关键的是，14B EDD=0 和跨策略迁移 45.9% 这两个结果从根本上限制了框架的实际影响力。对于 EMNLP 2026 long paper 主会议录用，novelty 和 impact 均不足。作为 Findings 论文，其系统性实验和诚实的负面结果报告有一定价值，但需要在 Discussion 中更深入地分析 scale-up 路径和实际部署的可行性。

**推荐**: 3.0 / 5 — Findings（可被 Findings 接收）
**置信度**: 4 / 5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1478 · 2026-05-21T06:40:49.095890+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们之间的异同：你们都给了 3.0 (Findings)，但侧重不同——你关注方法严谨性/统计有效性，R2 关注新颖性/贡献充分性。请评估 R2 的 novelty 批评是否合理。\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1** [critical] 方法层面零创新，novelty 不足以支撑 EMNLP long paper\n- 19 个特征全部是标准统计量，分类器是标准 RF，EDD 本质是 contiguous pairwise AUC 的最长前缀\n- 整个方法管道中没有任何需要智力投入的设计选择\n- EMNLP 即使接受 empirical study 也期望有 non-trivial insight 或方法论贡献\n- 对比 EditLens、Binoculars 等有新方法思路的工作，本文缺乏类似层次的方法贡献\n\n**R2-N2** [critical] 14B EDD=0 严重削弱框架的实际适用性\n- 当前主流 LLM 均为 7B-70B，1-1.5B 生成文本实际占比极小\n- 框架在 target use case (>7B) 上完全失效\n- 贡献退化为纯学术性的 toy-scale observation\n\n**R2-N3** [critical] 跨策略迁移 45.9% 几乎等同 random，实用性存疑\n- 实际场景中解码策略通常未知\n- 模型和策略均未知时，分类器几乎不可用\n- 与 Introduction 暗示的 data curation 工具定位存在根本矛盾\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1** \"Depth Degradation Atlas\" 概念过度包装——本质是标准实验结果的系统性呈现\n**R2-W2** Full-replacement 假设偏离现实，accumulation 实验不足\n**R2-W3** §6 Discussion 过于压缩（3 段 ~250 词）\n**R2-W4** Abstract 信息过载（6 数字 + 3 findings）\n**R2-W5** 下游 curation PoC 不显著但 Introduction 暗示实际应用\n\n### Reviewer 2 的优势评价\n1. 问题动机充分且及时\n2. 实验方法论严谨（180K 样本、5-fold CV、多维度 ablation）\n3. 诚实报告负面结果\n4. Perplexity tail statistics 发现有洞察力\n5. EDD metric 设计合理\n6. Related Work 覆盖面广\n\n### Reviewer 2 的 Missing References\n1. \"Unveiling Attractor Cycles in Large Language Models\" (2025, arXiv:2502.15208)\n2. \"The Canary's Echo: Auditing Privacy Risks of LLM-Generated Synthetic Text\" (2025)\n3. \"Data Provenance Auditing of Fine-Tuned LLMs\" (2025)\n\n### Reviewer 2 的总体判断\nOverall: 3.0 (Findings)，置信度 4/5。核心判断：贡献停留在\"标准工具的系统性应用\"层面，缺乏方法论创新。14B EDD=0 和跨策略 45.9% 从根本上限制了框架的实际影响力。\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们之间的异同：你们都给了 3.0 (Findings)，但侧重不同——你关注方法严谨性/统计有效性，R2 关注新颖性/贡献充分性。请评估 R2 的 novelty 批评是否合理。\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1** [critical] 方法层面零创新，novelty 不足以支撑 EMNLP long paper\n- 19 个特征全部是标准统计量，分类器是标准 RF，EDD 本质是 contiguous pairwise AUC 的最长前缀\n- 整个方法管道中没有任何需要智力投入的设计选择\n- EMNLP 即使接受 empirical study 也期望有 non-trivial insight 或方法论贡献\n- 对比 EditLens、Binoculars 等有新方法思路的工作，本文缺乏类似层次的方法贡献\n\n**R2-N2** [critical] 14B EDD=0 严重削弱框架的实际适用性\n- 当前主流 LLM 均为 7B-70B，1-1.5B 生成文本实际占比极小\n- 框架在 target use case (>7B) 上完全失效\n- 贡献退化为纯学术性的 toy-scale observation\n\n**R2-N3** [critical] 跨策略迁移 45.9% 几乎等同 random，实用性存疑\n- 实际场景中解码策略通常未知\n- 模型和策略均未知时，分类器几乎不可用\n- 与 Introduction 暗示的 data curation 工具定位存在根本矛盾\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1** \"Depth Degradation Atlas\" 概念过度包装——本质是标准实验结果的系统性呈现\n**R2-W2** Full-replacement 假设偏离现实，accumulation 实验不足\n**R2-W3** §6 Discussion 过于压缩（3 段 ~250 词）\n**R2-W4** Abstract 信息过载（6 数字 + 3 findings）\n**R2-W5** 下游 curation PoC 不显著但 Introduction 暗示实际应用\n\n### Reviewer 2 的优势评价\n1. 问题动机充分且及时\n2. 实验方法论严谨（180K 样本、5-fold CV、多维度 ablation）\n3. 诚实报告负面结果\n4. Perplexity tail statistics 发现有洞察力\n5. EDD metric 设计合理\n6. Related Work 覆盖面广\n\n### Reviewer 2 的 Missing References\n1. \"Unveiling Attractor Cycles in Large Language Models\" (2025, arXiv:2502.15208)\n2. \"The Canary's Echo: Auditing Privacy Risks of LLM-Generated Synthetic Text\" (2025)\n3. \"Data Provenance Auditing of Fine-Tuned LLMs\" (2025)\n\n### Reviewer 2 的总体判断\nOverall: 3.0 (Findings)，置信度 4/5。核心判断：贡献停留在\"标准工具的系统性应用\"层面，缺乏方法论创新。14B EDD=0 和跨策略 45.9% 从根本上限制了框架的实际影响力。\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 1479 · 2026-05-21T06:41:19.708257+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30612
}
```

</details>

---


### Tool call

_source line 1480 · 2026-05-21T06:41:19.809547+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们之间的异同：你们都给了 3.0 (Findings)，但侧重不同——R1 关注方法严谨性/统计有效性，你关注新颖性/贡献充分性。请评估 R1 的统计方法论批评是否合理。\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1** [critical] Full-replacement 假设从根本上限制了实用价值论述\n- 所有实验使用 full-replacement 递归链\n- 声称的 data curation 应用面对的是 accumulation 场景\n- pilot accumulation 仅报告 -14 到 -15pp 衰减，无完整数据（无 Table、无 per-cell 分解、无 EDD 变化、无统计检验）\n- -14 到 -15pp 是 ~18% 相对衰减，可能使部分 cell 的 d1-d3 准确率降至接近 chance\n\n**R1-N2** [critical] 14B EDD=0 且跨规模对比被 confound（self-reference）\n- Qwen2.5-14B 使用 self-reference 而非 Pythia-1.4B\n- 14B 结果与主表不可直接比较\n- 观察到的 EDD=0 可能部分来自参考模型切换而非纯粹规模效应\n- 未做任何控制实验来分离两个因素\n\n**R1-N3** [critical] 跨策略迁移 d1-d3 仅 45.9%，实质上否定了 \"unknown strategy\" 部署场景\n- d0 recall ≥89% 膨胀了 headline accuracy\n- Appendix B.7 跨温度实验 leave-one-τ-out mean d1v2 AUC 仅 0.319，甚至出现 inverted AUC (0.176)\n- two-stage pipeline 恢复 11.5pp 但 \"presupposes known or identifiable strategy\"——循环依赖\n\n**R1-N4** [critical] 严重共线性（VIF>10, 14-16/19 features）下特征重要性分析的可信度\n- Gini/SHAP/permutation 个体特征排名均不可靠\n- 论文引用 Strobl/Hooker 但并未使用 conditional permutation importance\n- Kendall's W=0.90 across 3 methods 不能反驳共线性——可能是系统性偏差\n- 论文 overstate 了在此共线性条件下可靠推断的范围\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1** LoRA seed 仅 2 个，OLMo +3.17pp CI 不重叠\n**R1-W2** 多重比较校正缺失，但结论超出 exploratory 范畴\n**R1-W3** Neural end-to-end baselines 仅测试 ≤125M backbone\n**R1-W4** BOS-seeded generation 的生态效度问题\n**R1-W5** Binoculars 达到统计等价性能（78.1% vs 78.4%, p>0.05），削弱独特价值\n**R1-W6** Wild-data FPR 高达 22.4%，confidence thresholding 的 recall 代价未充分表征\n\n### Reviewer 1 的优势评价\n1. 问题提出新颖且重要\n2. 极其系统的实验设计\n3. 诚实报告负面结果\n4. 理论框架与实验发现的良好对应\n5. 控制实验设计精细（heterogeneous chain + reverse-chain, LOGO + negative control）\n6. EDD 作为新度量有独立价值\n\n### Reviewer 1 的 Missing References\n- Liang et al. (2023) \"GPT Detectors Are Biased Against Non-Native English Writers\"\n- Sadasivan et al. (2023) impossibility result 对 ordinal 设定的含义\n- Hans et al. (2024) cross-perplexity vs. single-reference 在 ordinal setting 下的理论差异\n\n### Reviewer 1 的总体判断\nOverall: 3.0 (Findings)，置信度 4/5。核心判断：full-replacement 假设的非现实性、14B confounded EDD=0、跨策略迁移低下、共线性下特征分析可信度——共同构成论文更适合 Findings 而非 Conference。\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们之间的异同：你们都给了 3.0 (Findings)，但侧重不同——R1 关注方法严谨性/统计有效性，你关注新颖性/贡献充分性。请评估 R1 的统计方法论批评是否合理。\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1** [critical] Full-replacement 假设从根本上限制了实用价值论述\n- 所有实验使用 full-replacement 递归链\n- 声称的 data curation 应用面对的是 accumulation 场景\n- pilot accumulation 仅报告 -14 到 -15pp 衰减，无完整数据（无 Table、无 per-cell 分解、无 EDD 变化、无统计检验）\n- -14 到 -15pp 是 ~18% 相对衰减，可能使部分 cell 的 d1-d3 准确率降至接近 chance\n\n**R1-N2** [critical] 14B EDD=0 且跨规模对比被 confound（self-reference）\n- Qwen2.5-14B 使用 self-reference 而非 Pythia-1.4B\n- 14B 结果与主表不可直接比较\n- 观察到的 EDD=0 可能部分来自参考模型切换而非纯粹规模效应\n- 未做任何控制实验来分离两个因素\n\n**R1-N3** [critical] 跨策略迁移 d1-d3 仅 45.9%，实质上否定了 \"unknown strategy\" 部署场景\n- d0 recall ≥89% 膨胀了 headline accuracy\n- Appendix B.7 跨温度实验 leave-one-τ-out mean d1v2 AUC 仅 0.319，甚至出现 inverted AUC (0.176)\n- two-stage pipeline 恢复 11.5pp 但 \"presupposes known or identifiable strategy\"——循环依赖\n\n**R1-N4** [critical] 严重共线性（VIF>10, 14-16/19 features）下特征重要性分析的可信度\n- Gini/SHAP/permutation 个体特征排名均不可靠\n- 论文引用 Strobl/Hooker 但并未使用 conditional permutation importance\n- Kendall's W=0.90 across 3 methods 不能反驳共线性——可能是系统性偏差\n- 论文 overstate 了在此共线性条件下可靠推断的范围\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1** LoRA seed 仅 2 个，OLMo +3.17pp CI 不重叠\n**R1-W2** 多重比较校正缺失，但结论超出 exploratory 范畴\n**R1-W3** Neural end-to-end baselines 仅测试 ≤125M backbone\n**R1-W4** BOS-seeded generation 的生态效度问题\n**R1-W5** Binoculars 达到统计等价性能（78.1% vs 78.4%, p>0.05），削弱独特价值\n**R1-W6** Wild-data FPR 高达 22.4%，confidence thresholding 的 recall 代价未充分表征\n\n### Reviewer 1 的优势评价\n1. 问题提出新颖且重要\n2. 极其系统的实验设计\n3. 诚实报告负面结果\n4. 理论框架与实验发现的良好对应\n5. 控制实验设计精细（heterogeneous chain + reverse-chain, LOGO + negative control）\n6. EDD 作为新度量有独立价值\n\n### Reviewer 1 的 Missing References\n- Liang et al. (2023) \"GPT Detectors Are Biased Against Non-Native English Writers\"\n- Sadasivan et al. (2023) impossibility result 对 ordinal 设定的含义\n- Hans et al. (2024) cross-perplexity vs. single-reference 在 ordinal setting 下的理论差异\n\n### Reviewer 1 的总体判断\nOverall: 3.0 (Findings)，置信度 4/5。核心判断：full-replacement 假设的非现实性、14B confounded EDD=0、跨策略迁移低下、共线性下特征分析可信度——共同构成论文更适合 Findings 而非 Conference。\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 1481 · 2026-05-21T06:41:21.428757+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1619
}
```

</details>

---


### Assistant

_source line 1482 · 2026-05-21T06:41:24.417282+00:00_

交叉分享已派发。等待两名 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 134

## Round 134

2 recorded events


### User

_source line 1483 · 2026-05-21T06:41:27.182744+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**评分**: Overall 3.0/5（Findings），Soundness 3.5，Excitement 2.0，Confidence 4/5。

**核心判断**：3 个 Must-Fix 问题——(1) 方法零创新（19 个标准统计量 + 标准 RF，无新特征/架构/损失函数），对 EMNLP long paper novelty 不足；(2) 14B EDD=0 使框架在实际规模 LLM 上完全失效；(3) 跨策略迁移仅 45.9%，实际场景（策略未知时）分类器几乎不可用。5 个 Should-Fix 问题涵盖 "Atlas" 命名 overclaim、full-replacement 假设偏离现实、Discussion 过压缩、Abstract 信息过载、downstream PoC 不显著。引用验证：76 条引用无幻觉，但建议补充 3 篇可能遗漏的相关工作（attractor cycles in successive paraphrasing、synthetic data privacy auditing、data provenance auditing）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1484 · 2026-05-21T06:41:33.173721+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 135

## Round 135

2 recorded events


### User

_source line 1485 · 2026-05-21T06:42:42.362619+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[REBUT] R2-N1: 方法层面零创新，novelty 不足以支撑 EMNLP long paper**

R2 的 "零创新" 判断过于绝对，但核心关切有一定道理。具体分析：

1. **"19 个特征全部是标准统计量"**——表面正确但忽略了设计选择的非平凡性。论文的 insight 不在于单个特征是否新，而在于 (a) 从 reference model perplexity distribution 而非 surface text 提取特征的框架设计，(b) tail statistics（p90_ppl, kurtosis）而非 mean perplexity 主导深度信号的发现。§3.3 明确指出 mean perplexity 表现等同 chance（25.1%），而 p90_ppl 单特征达 58.3%（Appendix B.23, Table 24）。这种 "tail vs. mean" 的区分对后续工作有指导价值。Surface-text ablation（§5.1: zero-shot LLM best 36.2%）和 linear probing（Appendix B.8: var_surprisal 和 p90_ppl 的 R²<0）进一步证实了这不是一个 trivial 的特征选择。

2. **"EDD 本质是 contiguous pairwise AUC 的最长前缀"**——定义简单不等于无价值。EDD 的贡献在于将 "可区分深度" 从模糊概念形式化为可操作度量，这对后续工作（尤其是跨规模、跨策略的比较）提供了统一的评估框架。类比：BLEU 也只是 n-gram precision 的几何平均，但其 formalization 有独立价值。

3. **"对比 EditLens、Binoculars 有新方法思路"**——这个对比有失公平。Binoculars 的核心思路（observer-performer cross-perplexity）确实是方法创新，但论文 Table 4 显示 Binoculars + 11-feat RF 达到 78.1% vs 本文 78.4%（p>0.05），证明两种路径殊途同归。本文的贡献更多在 formulation 和 systematic characterization 层面，而非 pipeline 创新。

**但我同意**：就 EMNLP Conference 的标准而言，纯 formulation + empirical study 的 novelty 确实偏弱。论文的主要贡献是系统性的实证发现（tail erosion 主导、strategy > model effect、EDD ceiling），而非方法论突破。这更适合 Findings 的定位，而非 Main Conference。R2 如果说 "novelty 不足以支撑 Conference-level long paper"，我同意；但 "零创新" 和 "没有任何需要智力投入的设计选择" 是 overstatement。

---

**[AGREE] R2-N2: 14B EDD=0 严重削弱框架的实际适用性**

完全同意 R2 的核心判断，并补充我的 N2 中指出的额外 confound：14B 实验使用 self-reference 而非 Pythia-1.4B 作为参考模型（Appendix B.14），使得 EDD=0 的归因不清——可能是规模效应，也可能是参考模型切换的 artifact。R2 聚焦于 "practical applicability"，我聚焦于 "confounded comparison"——两者叠加使 14B 结果的可解读性更差。

补充一点 R2 未提及的：7-8B 实验（Table 15, Appendix B.14）显示 Llama-3.1-8B 达到 70.2% 且 EDD=4，Qwen2.5-7B 达到 60.1% 且 EDD>5。因此 "框架在 >7B 上完全失效" 并不完全准确——在 7-8B 仍有信号，只是在 14B 出现断崖式下降。R2 的措辞 "target use case (>7B) 上完全失效" 应修正为 "在 14B 出现断崖式衰减，且该衰减的归因被 confound 污染"。

---

**[AGREE] R2-N3: 跨策略迁移 45.9% 几乎等同 random，实用性存疑**

完全同意。这与我的 N3 一致。补充我在 N3 中额外指出的：Appendix B.7 的跨温度实验更为严峻——leave-one-τ-out mean d1v2 AUC 仅 0.319，τ=0.5 holdout 时 AUC=0.176（inverted）。这意味着即使在同一解码族（temperature sampling）内部，不同参数间的迁移都不可靠。R2 如果将此证据纳入，其论证会更强。

---

### Should-Fix 问题

**[REBUT] R2-W1: "Depth Degradation Atlas" 概念过度包装**

不同意。"Atlas" 一词在 empirical science 中有明确含义——对一个参数空间的系统性制图。本文的 3×3 model-strategy grid × depth trajectory + 8 个 generalization axis 确实构成了一个 atlas 结构。这不是修辞包装，而是对实验组织方式的准确描述。类比：genomics 中的 "expression atlas" 也是标准实验结果的系统性呈现，但 "atlas" 准确传达了覆盖面和系统性。

更重要的是，atlas 的组织方式本身产生了 insight：例如 strategy effect (9.3pp) > model effect (7.2pp)（§4.1）、top-k 的跨模型特征排名一致性最高（§4.2: ρ=0.811）、以及 EDD ceiling 的跨模型收敛（§4.4: d4v5 AUC 收敛到 0.681-0.684，range 0.003）。这些发现来自 atlas 结构的交叉比较，而非单个实验。

---

**[AGREE] R2-W2: Full-replacement 假设偏离现实，accumulation 实验不足**

强烈同意——事实上我将此列为 **Must-Fix N1**（critical），比 R2 的 Should-Fix 定位更严重。理由见我的 N1：-14 到 -15pp 的衰减可能使部分 cell 的 d1-d3 准确率降至接近 chance，但论文未给出任何详细数据。这不是 should-fix，而是影响接收决定的核心缺陷。

---

**[AGREE] R2-W3: §6 Discussion 过于压缩**

同意。§6 仅 3 段 ~250 词，对于一篇 8 页的 empirical study 而言过于单薄。特别是以下议题值得展开讨论：(a) 跨策略迁移失败的根本原因及可能的解决方向（目前仅在 Appendix B.28 有简要讨论），(b) EDD ceiling 的物理机制与突破可能性，(c) 本方法与现有 provenance 工具（watermarking, source attribution）的互补关系（目前仅在 Appendix B.28 最后一段涉及）。将部分 Appendix 中的 extended discussion 提升到主文会改善论文的叙事完整性。

但需考虑 8 页限制的约束——这可能是作者不得已的取舍。

---

**[REBUT] R2-W4: Abstract 信息过载**

轻微不同意。重新检查 Abstract（p.1）：它包含问题定义、benchmark 规模（180K）、核心发现（perplexity tail dominance）、EDD 定义、主要数字（d1-d3 balanced accuracy 59-82%）和关键限制（14B EDD=0, -13.8pp prompted generation）。对于一篇数据密集的 empirical study，这个信息密度在 *ACL 中是正常的——ACL/EMNLP 的 abstract 惯例是 "front-load" 关键数字以帮助 reviewer 和读者快速定位论文贡献。

如果 R2 的建议是减少数字、增加 narrative——这会与 ARR reviewer guidelines 中 "summary of contributions should be concrete" 的要求冲突。我认为 Abstract 信息量适当，不构成 should-fix。

---

**[AGREE] R2-W5: 下游 curation PoC 不显著但 Introduction 暗示实际应用**

同意。这与我的 W5 一致。Appendix B.12 的 RF-vs-unfiltered p>0.4，且 RF-vs-random 的显著性未校正多重比较（论文自己在 Appendix B.12 末段承认）。但 Introduction 的 "depth-scored data curation" 叙事和 §6 的 "score each passage for estimated recursive depth and filter or down-weight" 建议暗示了已被实验否定的实用价值。

---

### R2 优势评价的补充

R2 列出的 6 个优势与我的评价高度一致。特别赞同 R2 对 "perplexity tail statistics 发现有洞察力" 的认定——这正是我在反驳 R2-N1 时的论据之一。R2 在此处与 N1 的 "零创新" 存在内部张力：如果 tail statistics 发现有洞察力，那么导致该发现的特征设计选择就不是 "零智力投入"。

---

### 关于评分的总体判断

R2 和我都给出 3.0 (Findings)，但侧重不同：
- **R2 的核心论据**：novelty 不足（标准工具的系统性应用）
- **我的核心论据**：方法论缺陷（full-replacement 假设、confounded 14B、共线性下的特征分析、统计检验不足）

我认为两个角度互补且均成立。如果作者能在 rebuttal 中 (1) 提供累积场景完整结果，(2) 提供 14B cross-reference 对照实验，(3) 适当调整 claim 的 scope，论文有望提升至 3.5。但如果仅做文字修改而无新实验，3.0 是合理评分。

---

### R2 Missing References 评价

R2 提出的 3 篇 missing references 我未单独检索，无法确认其相关性。但从标题判断：
1. "Unveiling Attractor Cycles in Large Language Models" (2025) — 与 §3.5 Theory 中的 attractor dynamics 直接相关，如果存在应被讨论
2. "The Canary's Echo" (2025) — 与 data provenance auditing 相关，值得在 Related Work §2 提及
3. "Data Provenance Auditing of Fine-Tuned LLMs" (2025) — 同上

建议作者在 rebuttal 中核实并酌情补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1486 · 2026-05-21T06:43:01.676286+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 136

## Round 136

2 recorded events


### User

_source line 1487 · 2026-05-21T06:43:04.442945+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2-N1（零创新）**: [REBUT] — "零创新"过于绝对，tail vs. mean 的特征选择和 EDD formalization 有非平凡价值，但同意 novelty 不足以支撑 Conference-level
- **R2-N2（14B EDD=0）**: [AGREE] — 补充了 self-reference confound 使归因更不可靠，但修正 R2 "7B 以上完全失效" 的措辞（7-8B 仍有信号）
- **R2-N3（跨策略 45.9%）**: [AGREE] — 补充了 Appendix B.7 跨温度实验的更严峻证据
- **R2-W1（Atlas 过度包装）**: [REBUT] — atlas 准确描述了系统性制图的实验组织
- **R2-W2（Full-replacement）**: [AGREE] — 我将其定位为 Must-Fix，比 R2 的 Should-Fix 更严重
- **R2-W3（Discussion 压缩）**: [AGREE] — 需考虑 8 页限制的约束
- **R2-W4（Abstract 信息过载）**: [REBUT] — 信息密度在 *ACL empirical study 中属正常
- **R2-W5（Curation PoC）**: [AGREE] — 与我的 W5 一致

两位 Reviewer 均给 3.0 (Findings)，角度互补：R2 聚焦 novelty 不足，我聚焦方法论/统计缺陷。指出了 R2 的 N1 与其优势评价第 4 点之间的内部张力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1488 · 2026-05-21T06:43:09.883586+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 137

## Round 137

10 recorded events


### User

_source line 1489 · 2026-05-21T06:44:36.531808+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 — 对 Reviewer 1 逐条评估

---

## Must-Fix 问题回应

### [AGREE] R1-N1: Full-replacement 假设限制实用价值

同意 R1 将此升级为 critical（我原列为 W2/Should-Fix）。R1 的论证比我更具体且更有力：

1. **pilot accumulation 缺乏系统数据**：R1 正确指出该 pilot 无独立 Table、无 per-cell 分解、无 EDD 变化曲线、无统计检验——仅在 §6 Discussion 中以"14–19 pp below full-replacement"一笔带过。这不是一个合格的 ablation。
2. **-14 到 -15pp 的影响被低估**：主表（Table 2）中多个 cell 的 d1–d3 balanced accuracy 在 60–70% 区间（如 OLMo nucleus 65.6%、GPT-2 XL top-k 63.4%）。若再下降 14–15pp，将降至 46–56%，接近四分类 chance（25%）的两倍——功能上接近不可用。R1 的 "~18% 相对衰减" 计算合理。

我原来将此列为 Should-Fix 是因为 full-replacement 在 model collapse 文献中是标准设定（Shumailov et al., 2024; Dohmatob et al., 2024 均采用）。但 R1 的关键洞察在于：**model collapse 文献的目标是展示 worst-case 现象，可以用 full-replacement；而本文声称的目标是 data curation 工具，必须在 realistic accumulation 场景下验证**。这两个目标的实验设计要求根本不同。同意升级为 critical。

**补充**：论文 Appendix B.22 (downstream fine-tuning) 中确认 downstream PoC 不显著（Table 15 仅 3/10 contrasts p<0.05），进一步削弱了 "curation 应用" 的 claim。

---

### [AGREE] R1-N2: 14B self-reference confound——我的审稿遗漏了这个关键设计缺陷

完全同意，这是我 R1 审稿中没有充分识别的重要方法论问题。

1. **Confound 确实存在**：§5.4 明确说明 "14B (Qwen2.5-14B, self-reference)"，而主表 1–1.5B 实验全部使用 Pythia-1.4B 作为固定参考模型（§3.3："we use Pythia-1.4B as a fixed reference model"）。因此 14B EDD=0 可能来自：(a) 纯粹的 scale 效应（大模型生成文本统计上更接近人类文本），(b) reference model 从 Pythia-1.4B 切换到 self-reference 导致特征语义改变，或 (c) 两者的混合。无法从当前实验中分离两个因素。
2. **缺少控制实验**：至少需要两个对照：(i) 14B 模型 + Pythia-1.4B reference（控制 reference 不变，测试纯 scale 效应），(ii) 1.4B 模型 + self-reference（控制 scale 不变，测试 reference 切换效应）。论文两个都没做。
3. **影响我的 N2 评估**：我原来在 N2 中将 14B EDD=0 直接归因于 scale 效应（"相邻深度间完全不可区分"），并据此质疑框架的实际适用性。R1 的分析表明这个归因可能不完全正确——如果 confound 被分离后 scale 效应没那么极端，框架的适用范围可能比我判断的更大。但反过来说，如果控制 reference 后 14B 仍然 EDD=0，那就是更干净的负面结果。**无论哪种情况，当前论文的实验设计都无法支撑 §5.4 的结论**。

**承认自身疏漏**：我在 N2 中指出了 14B 问题但未识别 self-reference confound。R1 的这个发现是本轮审稿中最有价值的方法论批评。

---

### [AGREE] R1-N3: 跨策略迁移——R1 的补充论据强化了我的 N3

同意，且 R1 提供了我未注意到的关键细节：

1. **d0 recall 膨胀 headline accuracy**：Table 2 显示 d0 recall 在所有 9 cells 中 ≥97%（第 5 页 "Per-class recall. Depth 0 recall exceeds 97% in all 9 cells"）。这意味着 4-class headline accuracy 的 ~25% 分量（d0 那一类）几乎是 free points。d1–d3 balanced accuracy 才是真正有诊断价值的指标，而这正是跨策略仅 45.9% 的维度。R1 的这个分析框架比我的 N3 更精确。
2. **Appendix B.7 inverted AUC (0.176)**：这是极其重要的发现。AUC < 0.5 意味着分类器在该迁移设置下**系统性地反向预测**——把浅层误判为深层、深层误判为浅层。这不是"性能下降"，而是"特征语义在不同策略下反转"。我在阅读 Appendix 时注意到 B.7 跨温度实验（Table 10–11）但没有足够关注 d1v2 AUC 0.319 和可能的 inverted AUC。R1 对此的挖掘更深入。
3. **Two-stage pipeline 循环依赖**：论文 §5.3 提出 "a two-stage pipeline (strategy identification + per-strategy classification) recovers 11.5 pp"。R1 正确指出这 "presupposes known or identifiable strategy"——但如果策略可被识别，那 depth estimation 的难度本身就降低了（因为 strategy 是主要 confound 之一）。这个循环论证我没有识别出来。

---

### [AGREE with nuance] R1-N4: 共线性下特征重要性分析的可信度

部分同意。R1 的统计方法论批评在技术上正确，但我认为论文的 **family-level 分析部分缓解**了这个问题。

**同意的部分**：
1. VIF>10 for 14–16/19 features 下，individual feature 的 Gini/SHAP/permutation importance 确实不可靠——特征间的贡献无法被正确归因。
2. 论文引用了 Strobl et al. (2008) 和 Hooker et al. (2021) 讨论共线性对 importance 的影响，但并未按这些论文建议使用 conditional permutation importance。这是引用了方法论批评但不采纳其建议的"自我矛盾"。
3. Kendall's W=0.90 across 3 methods 确实不能排除系统性偏差——如果三种方法共享同一偏差来源（RF 内部结构偏好高频分裂变量），高一致性反而强化偏差而非反驳。

**持保留意见的部分**：
1. 论文的核心 claim 是 **perplexity tail statistics 作为一个 family**（9/19 features）在所有 cells 中占主导（§4.2："the perplexity tail statistics family (p90_ppl, …) and surprisal variance (var_surprisal) dominate"）。这是 **family-level** 的 claim，而非 individual feature level 的 claim。共线性主要影响 family 内部特征的归因（p90 vs. p75 谁更重要），但不太可能将整个 family 的重要性从一个类别错误归因到另一个类别。
2. §4.2 的 group-level ablation（"group-level ablation shows perplexity features alone reach 76.6%"）是一个不受共线性影响的验证——移除整个 feature family 后观察性能变化。这个 ablation 支持 perplexity tail 是主导特征家族的结论。
3. 但 R1 是对的：**individual feature 排名**（如 "p90_ppl ranks top-2 by Gini importance in all 9 cells"）在如此高的共线性下不应被如此自信地声称。

**结论**：R1 的批评在 individual feature 层面完全成立，但不完全推翻 family-level 结论。论文应 (1) 更明确地限定 importance 结论在 family level 而非 individual feature level，(2) 在 Appendix 中补充 conditional permutation importance 结果，(3) 移除或弱化 "p90_ppl ranks top-2" 等 individual ranking 声称。

---

## Should-Fix 问题回应

### [AGREE] R1-W1: LoRA seed 仅 2 个

同意。2 个 seed 无法提供可靠的 variance 估计。OLMo 的 +3.17pp CI 不重叠提示 seed-dependent 变异可能是实质性的（非噪声），但 2 个数据点无法区分"系统性差异"和"运气"。至少需要 5 个 seed。此问题我在 Round 1 中未涉及，R1 的指出是合理的。

### [AGREE] R1-W2: 多重比较校正缺失

同意。论文脚注 2（§3.5）承认 p-values 是 exploratory，但主文和 Appendix 中多处结论语气超出 exploratory（如 Table 15 downstream PoC 的 "significant" 判定、§4.2 中的 "dominance" 声称）。若严格校正（如 Bonferroni 或 Holm），部分 p<0.05 结论可能不再成立。R1 的批评合理——要么全面校正，要么全面弱化结论语气。

### [AGREE] R1-W3: Neural baselines 仅 ≤125M

同意，但认为严重性低于 R1 可能暗示的程度。DeBERTa-v3-base (86M) 和 RoBERTa-base (125M) 是 NLU baseline 的常见选择。更大 backbone（如 DeBERTa-large 304M 或 RoBERTa-large 355M）可能缩小与 RF 的差距，但 Appendix B.9 表明 neural end-to-end 的瓶颈更可能是表示空间问题（PLM 捕获的是 surface-level distribution，而 depth signal 在 perplexity tail 中），而非参数量。不过补充 large backbone 结果确实能让这个论证更完整。

### [REBUT] R1-W4: BOS-seeded generation 的生态效度

部分反驳。R1 的担忧有道理，但论文已有部分缓解措施：

1. **论文的生成流程不是纯 BOS-seeded**：§3.2 描述的 benchmark 是 LoRA fine-tuning + generation pipeline，每个 depth 的训练数据来自上一 depth 的生成输出，seed corpus 是 Wikipedia subset。生成时使用 "batch 16, 3 epochs, dropout 0.05"——这更接近 "model produces continuation-style text" 而非 "random BOS sampling"。
2. **Appendix B.6 有 prompted generation 测试**：zero-shot LLM prompt template 实验（§B.6，第 13 页）中，prompted generation 的 depth signal 保持 monotonic decay（"BOS-seeded generation may amplify depth signal, prompted generation validation confirms signals persist"）。
3. **但 R1 的核心关切仍有道理**：real-world 合成文本（instruction-following、chat completion、RAG-augmented generation）与 continuation-style 生成的 statistical fingerprint 可能显著不同。论文 §B.21（第 20 页）的 instruction-tuned model 实验确认 instruction-tuning 改变了 AUC 衰减模式——这恰恰说明 BOS-seeded 与 instruction-following 之间的 gap 是 non-trivial 的。

**结论**：不完全同意 R1 的严重性评级，因为论文确实有 prompted/instruction-tuned 的补充实验。但同意生态效度仍是一个 limitation——论文应在主文中更透明地讨论。

### [AGREE] R1-W5: Binoculars 统计等价性能

同意，这是一个我在 Round 1 中未充分关注的问题。§5.1（第 7 页）明确报告："multi-feature RF calibration (11 cross-perplexity statistics), it reaches 78.1%—matching our 19-feature pipeline within 0.3 pp (p≥0.85)"。这意味着：
- 仅使用 Binoculars 衍生的 11 个 cross-perplexity 特征就能匹配完整 19-feature pipeline
- 额外 8 个 non-Binoculars 特征（n-gram repetition、lexical diversity 等）的边际贡献统计上不显著

这确实削弱了 "19-feature comprehensive pipeline" 的 narrative。如果 Binoculars-based features alone 就够了，那论文对 feature engineering 的 effort（§3.3 定义 19 features、§4.2 详细分析每类特征）的独特价值就要打折。不过这个发现本身也有价值——它表明 cross-perplexity 是 depth signal 的核心载体。

### [AGREE] R1-W6: Wild-data FPR 22.4%

同意。Table 13（§B.11，第 16 页）显示 GPT-2 XL 在 C4 web-crawl 数据上 FPR 高达 22.4%，即使 WikiText-103 上也有 4.7% (OLMo)。这意味着在 out-of-distribution 部署中，每 4-5 篇人类文本就有 1 篇被错误标记为合成文本。论文提出的 confidence thresholding（P(d0) ≥ 0.75）将 FPR 降至可接受范围，但 R1 正确指出这里的 **recall 代价未被量化**——threshold 提高后会 miss 多少真正的深层合成文本？这个 precision-recall tradeoff 对实际部署至关重要，论文应补充 threshold-sweep 曲线。

---

## R1 Missing References 回应

- **Liang et al. (2023) "GPT Detectors Are Biased"**：同意应引用——detection bias 与 depth estimation 的公平性直接相关（depth classifier 是否对 non-native English text 存在系统偏差？）。
- **Sadasivan et al. (2023)**：注意 R1 可能有误——论文**已引用**此工作（Related Work §2："Sadasivan et al. (2023) address sentence-level attribution by using log-probability features from white-box LLMs"，bib key: sadasivan2023_paraphrase，verify_references 确认 status=verified）。但 R1 的意思可能是论文未讨论 Sadasivan 的 **impossibility result** 对 ordinal 设定的含义——这一点是合理的。
- **Hans et al. (2024) Binoculars**：论文已大量引用（Introduction, Related Work, §5.1, Appendix B.9, B.25, B.26），R1 可能是建议讨论 cross-perplexity 在 ordinal setting 下的**理论差异**，而非指出引用遗漏。

---

## 综合评估：两位 Reviewer 的异同

### 一致之处
1. **评分一致**：R1 和 R2 均给出 3.0 (Findings)，置信度均为 4/5。
2. **核心认同**：问题重要且及时、实验方法论系统、诚实报告负面结果。
3. **共同 concern**：full-replacement 假设、14B EDD=0、跨策略迁移差、Discussion 不足。

### 互补之处
- **R1 侧重统计方法论**：共线性分析（N4）、多重比较（W2）、seed 数量（W1）——这些是我审稿中的盲区，R1 的补充使审稿整体更严谨。
- **R2 侧重 novelty/impact**：方法层面零创新（N1）、"Atlas" overclaiming（W1）、Abstract 信息过载（W4）——这些是 R1 未覆盖的角度。
- **R1-N2 (self-reference confound)** 是本轮审稿最关键的新发现——我完全认同其重要性，且承认这是我在 Round 1 中的疏漏。

### 分歧之处
- **R1-W4 (BOS-seeded generation)**：我认为论文的 prompted/instruction-tuned 补充实验部分缓解了这个问题，R1 可能低估了这些补充实验。但整体方向上一致——生态效度是一个 limitation。

### 修正后的整体判断

经过交叉审稿，我维持 **Overall 3.0 (Findings)** 的评分。R1 的 N2 (self-reference confound) 和 N4 (共线性) 发现增加了额外的方法论 concern，但 R1-W4 的生态效度问题被论文的补充实验部分缓解。综合来看，论文在 Findings 级别的 soundness 是够的，但 novelty 和 practical impact 不足以支撑 Conference 录用。

如果作者能在 revision 中 (1) 补充 14B 的控制实验（分离 scale 和 reference-model 效应），(2) 增加 accumulation 的系统实验，(3) 补充 conditional permutation importance，(4) 扩展 Discussion——论文有潜力在下一个 cycle 冲击 Conference 3.5–4.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1490 · 2026-05-21T06:44:59.272631+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1491 · 2026-05-21T06:44:59.273096+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T06:30:56.628033+00:00\", \"completed_at\": \"2026-05-21T06:33:52.860833+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-3\", \"message\": \"连续 3 页纯文本（Title/Abstract/Intro/Related Work/Method 开头），无任何 display item。审稿人前 2 分钟看到的全是文字墙，缺乏视觉锚点。第一个 display item（Table 1，特征分类表）直到第 4 页才出现，且 Table 1 本身不传达论文核心 message——建议将 Figure 1（Atlas 热力图）或 Figure 2（AUC 衰减曲线）前移至第 2-3 页区域，或在 Introduction 末尾添加一个方法概览图/pipeline 示意图作为 Figure 1\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"单页内堆叠 4 个 display items（Table 4 + Table 5 + Table 6 + Figure 3），视觉极度拥挤，与前面 pages 1-3 的纯文本形成强烈失衡。建议将部分 table 移入 Appendix 或重新分配 float 位置，使 display items 在 pages 4-8 之间更均匀分布\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 3（Confusion matrices）尺寸过小——两个热力图挤在半栏宽度内，单元格内数字和 axis label 在正常阅读距离下难以辨认。建议改为 figure*（全宽）或移至 Appendix 并在正文用文字描述关键 pattern\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1（Atlas feature importance heatmap）y 轴特征名称字号偏小，尤其长名称如 `surprisal_position_corr` 在 150dpi 下已接近可读性边界。建议适当增大字号或缩写特征名\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Abstract/Author 排版整洁，符合 ACL 匿名投稿格式，无问题\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2（主结果表）使用 booktabs 风格，最优值加粗，格式规范。但表头层级较多（Model family + Strategy + 4-class/d1-d3），首次阅读需要较多时间理解结构\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（AUC decay curves）清晰专业——线型区分度好，有 shaded confidence bands，caption 自包含。这是全文视觉质量最高的 display item\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"正文最后一页（Limitations + Ethics Statement + References 开头）内容充实，填充率 >90%，无空间浪费\"}, {\"severity\": \"info\", \"dimension\": \"page 24\", \"message\": \"最后一页（Appendix 末尾，Computational Resources）仅填充约 60%，底部约 40% 空白。因为是 Appendix 最后一页且内容完整，不构成实质问题\"}, {\"severity\": \"info\", \"dimension\": \"pages
…[truncated 433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1492 · 2026-05-21T06:44:59.424048+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-21T06:44:59.524920+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1494 · 2026-05-21T06:47:23.932459+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n# ============================================================\n# ROUND 17 — MUST-FIX (Critical)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值——accumulation 场景无系统实验\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 列为 N1 critical, R2 原列 W2 后升级为 critical。两人共识：pilot accumulation 仅报 -14~-15pp 无 Table/per-cell/EDD/统计检验；-18% 相对衰减可能使部分 cell d1-d3 接近 chance\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-W1 (framing) resolved via §6 段落，但实验数据缺口未填补\"}\n  action_items:\n  - {round: 17, action: \"报告累积实验完整结果（至少 2-3 个混合比例 × 部分 cells），包括 accuracy、EDD、per-class recall、统计检验\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染——无法分离规模效应 vs 参考模型切换\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 首次识别 confound（N2 critical），R2 完全认同并承认自身疏漏。14B 用 self-reference 而主表用 Pythia-1.4B，两个因素无法分离。R2 修正了自己 N2 的归因\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-N1 (14B EDD=0 叙事) resolved via scope 限定，但 confound 未被发现\"}\n  action_items:\n  - {round: 17, action: \"控制实验：(1) 14B + Pythia-1.4B reference, (2) 1-1.5B self-reference 对照\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%——策略未知时方法基本失效，与应用场景矛盾\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N3 + R2-N3 完全共识。R1 补充：Appendix B.7 跨温度 AUC=0.319, inverted AUC=0.176; two-stage pipeline 循环依赖。R2 承认 R1 论据更强\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-N3 resolved via reframe 为 structural barrier，但 claim scope 仍超出实验支撑\"}\n  action_items:\n  - {round: 17, action: \"§6 和 Abstract 中将 claim 明确限定为 within-strategy/known-strategy；或探索 strategy-agnostic 特征\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠——论文 overstate 可推断范围\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N4 critical; R2 agree with nuance——family-level 分析部分缓解，但 individual feature ranking 不可靠。共识：引用 Strobl/Hooker 但未用 conditional permutation importance 是自我矛盾\"}\n  - {round: 15, reviewers: [1, 2], note: \"历史: R16-W3 resolved via group-level ablation 数字，但 individual ranking 过度声称问题仍在\"}\n  action_items:\n  - {round: 17, action: \"弱化 individual feature ranking 声称；补充 conditional permutation importance 或 bootstrap rank stability\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足——标准特征+标准分类器，不满足 Conference 门槛\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2-N1 critical; R1 REBUT '零创新'过于绝对（tail vs mean 选择和 EDD formalization 有价值），但同意 novelty 不足以支撑 Conference。R2 承认 N1 与优势第 4 点存在内部张力\"}\n  action_items:\n  - {round: 17, action: \"探索 learned features 或 ordinal-specific 方法；或调整定位为 Findings-level empirical study\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 17 — SHOULD-FIX (Warning)\n# ============================================================\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，OLMo +3.17pp CI 不重叠\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W1, R2 AGREE。2 个 seed 不足以建立 stability claim\"}\n  action_items:\n  - {round: 17, action: \"至少 5 个 seed，报告 mean±std 和特征排名跨 seed 一致性\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W2, R2 AGREE。脚注声明 exploratory 但 Abstract 和 §6 用确定性语言\"}\n  action_items:\n  - {round: 17, action: \"应用 Bonferroni/FDR 校正，或弱化结论语气\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 ≤125M backbone\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W3, R2 AGREE（严重性低于 R1 暗示）。PLM 瓶颈可能是表示空间而非参数量，但需更大 backbone 验证\"}\n  action_items:\n  - {round: 17, action: \"补充 ≥300M backbone baseline（如 DeBERTa-large）或限定 claim scope\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W4\n  summary: BOS-seeded generation 生态效度——instruction-following 场景未测试\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W4, R2 partial REBUT——prompted/instruction-tuned 补充实验部分缓解，但 instruction-following 场景未测试。R2 指出 §B.21 instruction-tuning 改变 AUC 衰减模式证明 gap non-trivial\"}\n  action_items:\n  - {round: 17, action: \"在主文更透明地讨论生态效度限制\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%, p>0.05），削弱独特价值\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5, R2 AGREE。Binoculars 11-feat 即匹配 19-feat pipeline，额外 8 特征边际贡献不显著\"}\n  action_items:\n  - {round: 17, action: \"精确定位贡献为 formulation/benchmark 而非 method 性能优势\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W6\n  summary: Wild-data FPR 高达 22.4%，thresholding 后 recall/coverage 代价未量化\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W6, R2 AGREE。需 FPR-coverage tradeoff curve\"}\n  action_items:\n  - {round: 17, action: \"报告 threshold-sweep 曲线：C4 上 FPR vs coverage vs balanced accuracy\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W7\n  summary: §6 Discussion 过于压缩（3 段 ~250 词）\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2-W3, R1 AGREE。缺少跨策略失败原因、EDD ceiling 机制、provenance 工具互补关系、scale-up 路径讨论。需考虑 8 页限制约束\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-W9 resolved via §6 扩展为 3 段落，但本轮 Reviewer 认为仍不足\"}\n  action_items:\n  - {round: 17, action: \"拆分 Discussion 和 Conclusion；扩展 Discussion 至少半页\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著（p>0.4）但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5(curation) + R2-W5 AGREE。RF-vs-unfiltered p>0.4, RF-vs-random 多重比较未校正\"}\n  action_items:\n  - {round: 17, action: \"弱化 curation 应用承诺或提供更 convincing 的 downstream evidence\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 17 — MINOR (Info)\n# ============================================================\n\n- id: R17-M1\n  summary: EDD 灵敏度分析仅 3 个阈值——需更细粒度 T vs EDD 曲线\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1], note: \"R1 minor point\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: Table 2 有 CI 但 Table 5/6 没有——CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1], note: \"R1 minor point\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M3\n  summary: Appendix B.10 报告 buggy pipeline 数字增加阅读负担\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1], note: \"建议将 buggy 数字放脚注\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references（3 篇）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2: attractor cycles (2502.15208), Canary's Echo (2502.14921), Data Provenance Auditing (2510.09655). R1: Liang et al. (2023) GPT detector bias\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M5\n  summary: orphan bib entry (penedo2024_fineweb) + 术语不一致 (estimation vs classification)\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 minor points\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (from Round 16, status carried forward)\n# ============================================================\n\n- id: R16-N1\n  summary: 14B 结果 (EDD=0) 从根本上削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 12, reviewers: [1, 2], note: \"R12-W4\"}\n  - {round: 16, reviewers: [1, 2], note: \"R1-N4 + R2-N1 一致 critical\"}\n  - {round: 17, reviewers: [1, 2], note: \"R16 writing fix resolved; R17 发现新 confound → R17-N2\"}\n  resolution: \"Abstract 加 scope 限定; §6 新增 scale dependence 段落。但 R17 发现 self-reference confound 未解决 → 见 R17-N2\"\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足——标准特征+标准分类器\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-N2 critical, R1 REBUT\"}\n  - {round: 17, reviewers: [1, 2], note: \"R17 Reviewer 再次提出 → R17-N5\"}\n  resolution: \"§1 贡献 3 条重组。但 R17 novelty 批评仍在 → 见 R17-N5\"\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R1-N3 critical\"}\n  - {round: 17, reviewers: [1, 2], note: \"reframe 为 structural barrier 已完成，但 claim scope 仍超出 → R17-N3\"}\n  resolution: \"§5.3 reframed 为 structural barrier。但 R17 认为 claim 仍需进一步限定 → 见 R17-N3\"\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-N3 critical, R1 AGREE\"}\n  - {round: 17, reviewers: [1, 2], note: \"§6 段落解决了 framing 但实验缺口仍在 → R17-N1\"}\n  resolution: \"§6 新增 'From ceiling to floor' 段。但 R17 要求系统实验数据 → 见 R17-N1\"\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia †)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R1-N1, R2-W2\"}\n  resolution: \"Reviewer 确认 † + ref-model ablation 67-79% 已充分。\"\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R1-N2, R2 REBUT\"}\n  - {round: 17, reviewers: [1, 2], note: \"group-level ablation 解决了 family-level，但 individual ranking overstatement 仍在 → R17-N4\"}\n  resolution: \"§4.2 加 group-level ablation 数字。但 R17 认为 individual ranking 仍 overstated → 见 R17-N4\"\n  resolution_round: 16\n\n- id: R16-W4\n  summary: Abstract 信息过载 (12+ 数字)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-W1 + R1 AGREE\"}\n  - {round: 17, reviewers: [1, 2], note: \"R2 仍认为信息过载（W4），R1 REBUT 认为密度正常——分歧未解决\"}\n  resolution: \"Abstract ~6 数字, 3 findings 结构。R17 Reviewer 对此有分歧\"\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Abstract 和 §1 以 d1-d3 balanced accuracy 领头\"\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Sensitivity analysis 已覆盖\"\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W4 重新提出，R2 partial REBUT\"}\n  resolution: \"§3.2 已讨论 + prompted -13.8pp + Limitations 覆盖。R17 仍认为 instruction-following 未测试\"\n  resolution_round: 16\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W6 重新提出，要求 FPR-coverage tradeoff curve\"}\n  resolution: \"Thresholding 方案已覆盖。R17 要求更详细的 tradeoff 分析\"\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W7 认为扩展后仍不足\"}\n  resolution: \"§6 从 5 行扩展为 3 段落。R17 认为仍需进一步扩展\"\n  resolution_round: 16\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"§6 含 depth-scored data curation deployment scenario\"\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [], note: \"视觉审查再次确认\"}\n  resolution: \"Minor visual, acceptable for review\"\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [], note: \"视觉审查再次确认\"}\n  resolution: \"Pipeline 太简单不需要图\"\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 格式检查确认合规\"}\n  resolution: \"编译验证通过\"\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致 depth estimation / classification\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 仍注意到混用 → R17-M5\"}\n  resolution: \"统一为 depth estimation。R17 仍注意到残余不一致\"\n  resolution_round: 16\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Strobl (2008) + Hooker (2021) 已加入\"\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Classifier convergence evidence sufficient\"\n  resolution_round: 16\n\n# Historical issues not re-raised in R17 (carried forward as-is)\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [], note: \"视觉审查再次确认: page 8 堆叠 4 个 display items\"}\n  resolution: \"Structural constraint\"\n  resolution_round: 16\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"项目收尾不再跑新实验\"\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W2 重新提出\"}\n  resolution: \"Footnote caveat in §3.5\"\n  resolution_round: 16\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§2 已引用 geng2026_markovian\"\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 格式检查确认合规: 主文 pp.1-8, Limitations p.9\"}\n  resolution: \"编译验证通过\"\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"用户指示不再跑新实验\"\n  resolution_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n# ============================================================\n# ROUND 17 — MUST-FIX (Critical)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值——accumulation 场景无系统实验\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 列为 N1 critical, R2 原列 W2 后升级为 critical。两人共识：pilot accumulation 仅报 -14~-15pp 无 Table/per-cell/EDD/统计检验；-18% 相对衰减可能使部分 cell d1-d3 接近 chance\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-W1 (framing) resolved via §6 段落，但实验数据缺口未填补\"}\n  action_items:\n  - {round: 17, action: \"报告累积实验完整结果（至少 2-3 个混合比例 × 部分 cells），包括 accuracy、EDD、per-class recall、统计检验\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染——无法分离规模效应 vs 参考模型切换\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 首次识别 confound（N2 critical），R2 完全认同并承认自身疏漏。14B 用 self-reference 而主表用 Pythia-1.4B，两个因素无法分离。R2 修正了自己 N2 的归因\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-N1 (14B EDD=0 叙事) resolved via scope 限定，但 confound 未被发现\"}\n  action_items:\n  - {round: 17, action: \"控制实验：(1) 14B + Pythia-1.4B reference, (2) 1-1.5B self-reference 对照\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%——策略未知时方法基本失效，与应用场景矛盾\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N3 + R2-N3 完全共识。R1 补充：Appendix B.7 跨温度 AUC=0.319, inverted AUC=0.176; two-stage pipeline 循环依赖。R2 承认 R1 论据更强\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-N3 resolved via reframe 为 structural barrier，但 claim scope 仍超出实验支撑\"}\n  action_items:\n  - {round: 17, action: \"§6 和 Abstract 中将 claim 明确限定为 within-strategy/known-strategy；或探索 strategy-agnostic 特征\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠——论文 overstate 可推断范围\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N4 critical; R2 agree with nuance——family-level 分析部分缓解，但 individual feature ranking 不可靠。共识：引用 Strobl/Hooker 但未用 conditional permutation importance 是自我矛盾\"}\n  - {round: 15, reviewers: [1, 2], note: \"历史: R16-W3 resolved via group-level ablation 数字，但 individual ranking 过度声称问题仍在\"}\n  action_items:\n  - {round: 17, action: \"弱化 individual feature ranking 声称；补充 conditional permutation importance 或 bootstrap rank stability\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足——标准特征+标准分类器，不满足 Conference 门槛\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2-N1 critical; R1 REBUT '零创新'过于绝对（tail vs mean 选择和 EDD formalization 有价值），但同意 novelty 不足以支撑 Conference。R2 承认 N1 与优势第 4 点存在内部张力\"}\n  action_items:\n  - {round: 17, action: \"探索 learned features 或 ordinal-specific 方法；或调整定位为 Findings-level empirical study\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 17 — SHOULD-FIX (Warning)\n# ============================================================\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，OLMo +3.17pp CI 不重叠\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W1, R2 AGREE。2 个 seed 不足以建立 stability claim\"}\n  action_items:\n  - {round: 17, action: \"至少 5 个 seed，报告 mean±std 和特征排名跨 seed 一致性\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W2, R2 AGREE。脚注声明 exploratory 但 Abstract 和 §6 用确定性语言\"}\n  action_items:\n  - {round: 17, action: \"应用 Bonferroni/FDR 校正，或弱化结论语气\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 ≤125M backbone\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W3, R2 AGREE（严重性低于 R1 暗示）。PLM 瓶颈可能是表示空间而非参数量，但需更大 backbone 验证\"}\n  action_items:\n  - {round: 17, action: \"补充 ≥300M backbone baseline（如 DeBERTa-large）或限定 claim scope\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W4\n  summary: BOS-seeded generation 生态效度——instruction-following 场景未测试\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W4, R2 partial REBUT——prompted/instruction-tuned 补充实验部分缓解，但 instruction-following 场景未测试。R2 指出 §B.21 instruction-tuning 改变 AUC 衰减模式证明 gap non-trivial\"}\n  action_items:\n  - {round: 17, action: \"在主文更透明地讨论生态效度限制\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%, p>0.05），削弱独特价值\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5, R2 AGREE。Binoculars 11-feat 即匹配 19-feat pipeline，额外 8 特征边际贡献不显著\"}\n  action_items:\n  - {round: 17, action: \"精确定位贡献为 formulation/benchmark 而非 method 性能优势\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W6\n  summary: Wild-data FPR 高达 22.4%，thresholding 后 recall/coverage 代价未量化\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W6, R2 AGREE。需 FPR-coverage tradeoff curve\"}\n  action_items:\n  - {round: 17, action: \"报告 threshold-sweep 曲线：C4 上 FPR vs coverage vs balanced accuracy\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W7\n  summary: §6 Discussion 过于压缩（3 段 ~250 词）\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2-W3, R1 AGREE。缺少跨策略失败原因、EDD ceiling 机制、provenance 工具互补关系、scale-up 路径讨论。需考虑 8 页限制约束\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-W9 resolved via §6 扩展为 3 段落，但本轮 Reviewer 认为仍不足\"}\n  action_items:\n  - {round: 17, action: \"拆分 Discussion 和 Conclusion；扩展 Discussion 至少半页\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著（p>0.4）但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5(curation) + R2-W5 AGREE。RF-vs-unfiltered p>0.4, RF-vs-random 多重比较未校正\"}\n  action_items:\n  - {round: 17, action: \"弱化 curation 应用承诺或提供更 convincing 的 downstream evidence\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 17 — MINOR (Info)\n# ============================================================\n\n- id: R17-M1\n  summary: EDD 灵敏度分析仅 3 个阈值——需更细粒度 T vs EDD 曲线\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1], note: \"R1 minor point\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: Table 2 有 CI 但 Table 5/6 没有——CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1], note: \"R1 minor point\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M3\n  summary: Appendix B.10 报告 buggy pipeline 数字增加阅读负担\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1], note: \"建议将 buggy 数字放脚注\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references（3 篇）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2: attractor cycles (2502.15208), Canary's Echo (2502.14921), Data Provenance Auditing (2510.09655). R1: Liang et al. (2023) GPT detector bias\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M5\n  summary: orphan bib entry (penedo2024_fineweb) + 术语不一致 (estimation vs classification)\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 minor points\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (from Round 16, status carried forward)\n# ============================================================\n\n- id: R16-N1\n  summary: 14B 结果 (EDD=0) 从根本上削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 12, reviewers: [1, 2], note: \"R12-W4\"}\n  - {round: 16, reviewers: [1, 2], note: \"R1-N4 + R2-N1 一致 critical\"}\n  - {round: 17, reviewers: [1, 2], note: \"R16 writing fix resolved; R17 发现新 confound → R17-N2\"}\n  resolution: \"Abstract 加 scope 限定; §6 新增 scale dependence 段落。但 R17 发现 self-reference confound 未解决 → 见 R17-N2\"\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足——标准特征+标准分类器\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-N2 critical, R1 REBUT\"}\n  - {round: 17, reviewers: [1, 2], note: \"R17 Reviewer 再次提出 → R17-N5\"}\n  resolution: \"§1 贡献 3 条重组。但 R17 novelty 批评仍在 → 见 R17-N5\"\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R1-N3 critical\"}\n  - {round: 17, reviewers: [1, 2], note: \"reframe 为 structural barrier 已完成，但 claim scope 仍超出 → R17-N3\"}\n  resolution: \"§5.3 reframed 为 structural barrier。但 R17 认为 claim 仍需进一步限定 → 见 R17-N3\"\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-N3 critical, R1 AGREE\"}\n  - {round: 17, reviewers: [1, 2], note: \"§6 段落解决了 framing 但实验缺口仍在 → R17-N1\"}\n  resolution: \"§6 新增 'From ceiling to floor' 段。但 R17 要求系统实验数据 → 见 R17-N1\"\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia †)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R1-N1, R2-W2\"}\n  resolution: \"Reviewer 确认 † + ref-model ablation 67-79% 已充分。\"\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R1-N2, R2 REBUT\"}\n  - {round: 17, reviewers: [1, 2], note: \"group-level ablation 解决了 family-level，但 individual ranking overstatement 仍在 → R17-N4\"}\n  resolution: \"§4.2 加 group-level ablation 数字。但 R17 认为 individual ranking 仍 overstated → 见 R17-N4\"\n  resolution_round: 16\n\n- id: R16-W4\n  summary: Abstract 信息过载 (12+ 数字)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-W1 + R1 AGREE\"}\n  - {round: 17, reviewers: [1, 2], note: \"R2 仍认为信息过载（W4），R1 REBUT 认为密度正常——分歧未解决\"}\n  resolution: \"Abstract ~6 数字, 3 findings 结构。R17 Reviewer 对此有分歧\"\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Abstract 和 §1 以 d1-d3 balanced accuracy 领头\"\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Sensitivity analysis 已覆盖\"\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W4 重新提出，R2 partial REBUT\"}\n  resolution: \"§3.2 已讨论 + prompted -13.8pp + Limitations 覆盖。R17 仍认为 instruction-following 未测试\"\n  resolution_round: 16\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W6 重新提出，要求 FPR-coverage tradeoff curve\"}\n  resolution: \"Thresholding 方案已覆盖。R17 要求更详细的 tradeoff 分析\"\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W7 认为扩展后仍不足\"}\n  resolution: \"§6 从 5 行扩展为 3 段落。R17 认为仍需进一步扩展\"\n  resolution_round: 16\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"§6 含 depth-scored data curation deployment scenario\"\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [], note: \"视觉审查再次确认\"}\n  resolution: \"Minor visual, acceptable for review\"\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [], note: \"视觉审查再次确认\"}\n  resolution: \"Pipeline 太简单不需要图\"\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 格式检查确认合规\"}\n  resolution: \"编译验证通过\"\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致 depth estimation / classification\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 仍注意到混用 → R17-M5\"}\n  resolution: \"统一为 depth estimation。R17 仍注意到残余不一致\"\n  resolution_round: 16\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Strobl (2008) + Hooker (2021) 已加入\"\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Classifier convergence evidence sufficient\"\n  resolution_round: 16\n\n# Historical issues not re-raised in R17 (carried forward as-is)\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [], note: \"视觉审查再次确认: page 8 堆叠 4 个 display items\"}\n  resolution: \"Structural constraint\"\n  resolution_round: 16\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"项目收尾不再跑新实验\"\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W2 重新提出\"}\n  resolution: \"Footnote caveat in §3.5\"\n  resolution_round: 16\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§2 已引用 geng2026_markovian\"\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 格式检查确认合规: 主文 pp.1-8, Limitations p.9\"}\n  resolution: \"编译验证通过\"\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"用户指示不再跑新实验\"\n  resolution_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1495 · 2026-05-21T06:47:24.084357+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml\", \"bytes\": 17313}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1496 · 2026-05-21T06:50:28.024932+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# 审稿报告 — Round 17 (Fresh)\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 (ARR May cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 名 Reviewer\n- Reviewer 1: 方法严谨性 + 实验设计 + 统计有效性\n- Reviewer 2: 新颖性 + 贡献充分性 + Related Work 覆盖 + 写作质量\n\n---\n\n## Summary\n\n本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类问题，构建了覆盖 3 个模型族（Pythia-1.4B, OLMo-1B, GPT-2 XL）× 3 种解码策略（nucleus, temperature, top-k）× 4 个深度的 180K 样本基准数据集。从固定参考模型（Pythia-1.4B）的困惑度分布中提取 19 个统计特征，使用 Random Forest 分类器进行深度分类。提出 Effective Discriminable Depth (EDD) 指标量化可区分深度上限。分布内四分类准确率 68.9–85.9%（d1-d3 balanced: 58.9–81.5%），跨模型迁移 66.4%（d1-d3: 55.4%），跨策略迁移 59.1%（d1-d3: 45.9%），14B 模型 EDD=0。论文定位为 task formalization + systematic empirical characterization。\n\n---\n\n## Strengths\n\n**S1. 问题提出新颖且及时** [R1, R2 共识]\n从二元检测（human vs. AI）扩展到递归深度估计是一个自然但未被探索的方向。在 model collapse 日益受关注的背景下，\"文本经历了多少轮递归生成\"这个问题具有前瞻性。Introduction 从 model collapse → detection gap → depth estimation 建立了清晰的逻辑链。\n\n**S2. 极其系统的实验设计** [R1, R2 共识]\n3×3×4 grid + 180K 样本、8 个 generalization axis（跨模型/跨策略/跨规模/跨域/seed replication/accumulation/prompted generation/mixed-depth）、24 页附录覆盖近 30 个子实验。R1 评价：\"这是近期审稿中见过的最全面的 empirical study 之一。\"\n\n**S3. 诚实报告负面结果** [R1, R2 共识]\n14B EDD=0、cross-strategy 45.9%、downstream curation PoC 不显著（p>0.4）、跨温度 inverted AUC 等负面结果均被坦诚报告。无 cherry-picking 或隐藏不利证据。\n\n**S4. Perplexity tail statistics 发现有洞察力** [R1, R2 共识]\np90_ppl 在所有 9 cells 中排名 top-2，与 surprisal variance 共同占据 41% Gini importance。Mean perplexity 表现等同 chance (25.1%)，揭示深度信号集中在分布尾部而非均值——对后续工作有指导价值。Group-level ablation（perplexity alone 76.6% vs. full 78.4%）提供了不受共线性影响的验证。\n\n**S5. 理论框架与实验发现的良好对应** [R1]\nTail erosion 理论（§3.5）预测 perplexity tail 特征应主导深度信号，group-level ablation 确认。Scale-dependent attenuation 的理论预测在 14B 实验中得到定性验证。\n\n**S6. 控制实验设计精细** [R1]\nHeterogeneous chain + reverse-chain control（Appendix B.15）排除 architecture confound、LOGO + negative control 消除 domain bias（Appendix B.10）、temperature robustness + memorization-prerequisite 发现（Appendix B.7）展示高水平实验工程。\n\n**S7. EDD metric 有独立价值** [R1, R2 共识]\n将\"可区分深度\"从模糊概念形式化为可操作度量，contiguous pairwise AUC 的最长前缀定义简洁，可被后续工作采用。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1. Full-replacement 假设从根本上限制实用价值** [R1 critical, R2 升级为 critical]\n\n所有实验使用 full-replacement 递归链（每个深度完全替换前一代训练语料），但论文声称的应用场景（§6 \"depth-scored data curation\"）面对的是 accumulation 场景（合成和人类数据以未知比例共存）。Pilot accumulation 实验仅在 §6 中以一句话报告 \"-14 到 -15pp\"，无独立 Table、无 per-cell 分解、无 EDD 变化、无统计检验。-14 到 -15pp 相当于 full-replacement baseline 的 ~18% 相对衰减，可能使 OLMo nucleus (65.6%) 等 cell 的 d1-d3 准确率降至 ~50%，接近功能不可用。\n\nR2 的关键洞察：model collapse 文献使用 full-replacement 展示 worst-case 现象是合理的，但本文声称的目标是 data curation 工具——两个目标的实验设计要求根本不同。\n\n**N2. 14B EDD=0 被 self-reference confound 污染** [R1 critical, R2 critical + 承认自身疏漏]\n\nQwen2.5-14B 使用 self-reference（14B 模型自身计算特征），而主表（Table 2）所有 1-1.5B 实验使用 Pythia-1.4B 作为固定参考模型。这意味着观察到的 EDD=0 可能来自：(a) 纯规模效应，(b) 参考模型从 cross-reference 切换到 self-reference 导致特征语义改变，或 (c) 两者混合。论文在 Appendix B.14 承认此 confound 但未做任何控制实验来分离两个因素。\n\nR1 指出至少需要两个对照：(i) 14B + Pythia-1.4B reference（测纯规模效应），(ii) 1.4B + self-reference（测 reference 切换效应）。R2 承认这是本轮审稿中最有价值的方法论发现，修正了自己 N2 中将 EDD=0 直接归因于规模效应的分析。\n\n补充：7-8B 实验（Llama-3.1-8B 70.2% EDD=4, Qwen2.5-7B 60.1% EDD>5）表明框架在 7-8B 仍有信号，并非 \">7B 完全失效\"——更准确的表述是\"14B 出现断崖式衰减，且该衰减的归因被 confound 污染\"。\n\n**N3. 跨策略迁移 d1-d3 仅 45.9%，策略未知时方法基本失效** [R1 critical, R2 critical]\n\nCross-strategy transfer 将 d1-d3 balanced accuracy 降至 45.9%（四分类: 59.1%），仅 1.4× chance。d0 recall ≥89% 膨胀了 headline accuracy。在真实部署中解码策略通常未知，这与论文的 data provenance 应用场景根本矛盾。\n\nR1 补充了更严峻的证据：Appendix B.7 跨温度实验 leave-one-τ-out mean d1v2 AUC 仅 0.319，τ=0.5 holdout 时出现 inverted AUC (0.176)——不是\"性能下降\"而是\"特征语义在不同策略下反转\"。Two-stage pipeline（策略识别 + per-strategy 分类）恢复 11.5pp 但 presupposes 策略可被识别——循环依赖。\n\n**N4. 严重共线性（VIF>10, 14-16/19 features）下个体特征排名不可靠** [R1 critical, R2 agree with nuance]\n\n19 个特征中 14-16 个 VIF>10，有效独立维度仅 ~4-5。论文引用 Strobl et al. (2008) 和 Hooker et al. (2021) 讨论共线性影响，但并未使用 conditional permutation importance——引用方法论批评但不采纳其建议的\"自我矛盾\"。Kendall's W=0.90 across 3 methods 不能排除系统性偏差。\n\nR2 的 nuanced 回应：family-level 分析（group-level ablation: perplexity 76.6% vs. full 78.4%）不受共线性影响，支持 perplexity tail 家族主导的结论。但 individual feature ranking（\"p90_ppl ranks top-2 in all 9 cells\"）在如此共线性下不应如此自信地声称。\n\n**两位 Reviewer 共识**：family-level 结论可靠，individual feature ranking 结论需弱化。\n\n**N5. 方法层面 novelty 不足以支撑 Conference-level long paper** [R2 critical, R1 partial REBUT]\n\n19 个特征全部是标准统计量（perplexity percentiles, surprisal moments, n-gram repetition），分类器是标准 Random Forest，EDD 本质上是 contiguous pairwise AUC 的最长前缀。整个方法管道无 algorithmic novelty。\n\nR1 的 partial REBUT：(1) tail vs. mean 的特征选择并非 trivial（mean perplexity = chance, p90_ppl = 58.3%），(2) EDD 的 formalization 有独立价值（类比 BLEU），(3) \"零创新\"过于绝对。但 R1 同意就 Conference 标准而言 novelty 偏弱。\n\n**两位 Reviewer 共识**：novelty 不构成 \"零\"，但不足以支撑 Conference 录用。更适合 Findings 定位。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1. LoRA seed 仅 2 个** [R1, R2 AGREE]\nOLMo +3.17pp（CI 不重叠）说明 LoRA 初始化对绝对准确率有非平凡影响。2 个 seed 不足以建立 stability claim。至少需要 5 个 seed。\n\n**W2. 多重比较校正缺失** [R1, R2 AGREE]\n脚注声明 p-values 为 exploratory，但 Abstract 和 §6 使用确定性语言。Appendix B.12 Curation PoC 的显著性检验涉及多重比较但未校正。要么全面校正，要么全面弱化结论语气。\n\n**W3. Neural end-to-end baselines 仅测试 ≤125M backbone** [R1, R2 AGREE]\nDeBERTa-v3-base (86M) 和 RoBERTa-base (125M) 比 RF 低 20pp，但更大 backbone 可能缩小差距。R2 认为瓶颈更可能是表示空间（PLM 无法线性恢复 perplexity tail statistics）而非参数量，但需更大 backbone 验证。\n\n**W4. BOS-seeded generation 生态效度** [R1, R2 partial REBUT]\n主实验使用 BOS-seeded generation。Prompted generation 实验（-13.8pp, Appendix B.27）和 instruction-tuned model 实验（Appendix B.21）部分缓解但未完全解决——instruction-following 场景（实际中最相关）未被测试。R2 指出 §B.21 instruction-tuning 改变 AUC 衰减模式证明 gap non-trivial。\n\n**W5. Binoculars 达到统计等价性能** [R1, R2 AGREE]\nBinoculars 11-feat RF: 78.1% vs. 本文 19-feat: 78.4%（p>0.05）。额外 8 个 non-Binoculars 特征边际贡献不显著。削弱了 \"19-feature comprehensive pipeline\" 的独特价值叙事。论文应更精确地定位贡献为 formulation/benchmark 而非 pipeline 性能优势。\n\n**W6. Wild-data FPR 高达 22.4%，thresholding recall 代价未量化** [R1, R2 AGREE]\nGPT-2 XL on C4 FPR 22.4%。Confidence thresholding 降至 2.8% 但 recall/coverage 代价未报告。需 FPR-coverage tradeoff curve。\n\n**W7. §6 Discussion 过于压缩** [R2, R1 AGREE]\n3 段 ~250 词，缺少：跨策略失败根因分析、EDD ceiling 突破路径、provenance 工具互补关系、scale-up 路线图。需考虑 8 页限制约束。\n\n**W8. Downstream curation PoC 不显著但 Introduction 暗示应用** [R1, R2 AGREE]\nRF-vs-unfiltered p>0.4。RF-vs-random 的 p<0.02 涉及多重比较未校正。Introduction 和 §6 的 \"depth-scored data curation\" 叙事缺乏实验支撑。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 达成共识的关键判断：\n\n- [AGREE] **评分**: 均给出 3.0 (Findings)，置信度均为 4/5\n- [AGREE] **问题重要性**: 递归生成深度估计是有价值的新问题\n- [AGREE] **实验质量**: 系统性和诚实度均属上乘\n- [AGREE] **Full-replacement 限制** (N1): critical，需要系统性 accumulation 实验\n- [AGREE] **14B confound** (N2): critical，需要控制实验分离 scale vs. reference-model 效应\n- [AGREE] **跨策略迁移** (N3): critical，需限定 claim scope\n- [AGREE] **共线性** (N4): family-level 结论可靠，individual ranking 需弱化\n- [AGREE] **Findings 定位**: novelty 不足以支撑 Conference，但 empirical 贡献适合 Findings\n\n## Reviewer Divergence\n\n- [R1 REBUT] **R2-N1 \"零创新\"**: R1 认为 tail vs. mean 的特征选择和 EDD formalization 有非平凡价值，\"零创新\"是 overstatement。R2 承认 N1 与自己优势评价第 4 点存在内部张力。最终共识：不是\"零\"，但不足以支撑 Conference。\n- [R1 REBUT] **R2-W1 \"Atlas 过度包装\"**: R1 认为 atlas 准确描述了系统性制图的实验组织。未解决。\n- [R1 REBUT] **R2-W4 \"Abstract 信息过载\"**: R1 认为信息密度在 *ACL empirical study 中属正常。未解决。\n- [R2 partial REBUT] **R1-W4 \"BOS-seeded 生态效度\"**: R2 认为 prompted/instruction-tuned 补充实验部分缓解。部分解决。\n\n---\n\n## Questions to Authors\n\n1. 能否提供累积（accumulation）场景下的完整结果（至少覆盖部分 cells），包括 accuracy、EDD、per-class recall？pilot 中 -14 到 -15pp 的衰减是在哪个 cell 上测的？\n2. 14B 实验中，是否有技术原因无法使用 Pythia-1.4B 作为 cross-reference？如果用 Pythia-1.4B 对 Qwen2.5-14B 文本做特征提取，预期结果如何？\n3. 跨策略迁移中，是否尝试过 normalization-based domain adaptation（如 per-strategy z-score normalization）？\n4. 对于 Binoculars 近平局的结果，作者如何定位本文的独特贡献——是 formulation/benchmark，还是 method 本身？\n5. 14B EDD=0 的根因分析：是 14B 模型 perplexity 分布方差更小，还是 fine-tuning 在大模型上更\"gentle\"？是否有 per-feature 的 scale-dependent 分析？\n6. 深度 >5 时是否存在 saturation？是否有更深的初步数据？\n7. 是否考虑过将 depth estimation 与 model attribution 结合（cf. Bevendorff et al. 2025 two-paradigm framework）？\n\n---\n\n## Missing References\n\n**R1 建议**:\n- Liang et al. (2023), \"GPT Detectors Are Biased Against Non-Native English Writers\" — detection bias 与 depth estimation 的公平性直接相关\n- Sadasivan et al. (2023) 的 impossibility result 对 ordinal 设定的含义（论文已引用但未讨论）\n\n**R2 建议**:\n- \"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing\" (2025, arXiv:2502.15208) — iterative paraphrasing 的 attractor dynamics，与递归生成链高度相关\n- \"The Canary's Echo: Auditing Privacy Risks of LLM-Generated Synthetic Text\" (2025, arXiv:2502.14921) — data auditing 角度\n- \"Data Provenance Auditing of Fine-Tuned Large Language Models\" (2025, arXiv:2510.09655) — 数据来源审计\n\n**引用验证**: R2 验证 76 条 bib entries，无幻觉引用。1 条 orphan bib (penedo2024_fineweb)。\n\n---\n\n## External Review\n\n**外部审稿**: 未配置（项目未启用 paperreview.ai）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（耗时 ~3 分钟）\n\n**Warnings (3)**:\n1. **Pages 1-3 无视觉锚点**: 连续 3 页纯文本，第一个 display item（Table 1）直到第 4 页才出现。建议将 Figure 1（Atlas 热力图）或 Figure 2（AUC 衰减曲线）前移，或添加 pipeline 示意图。\n2. **Page 8 display items 堆叠**: 单页内 4 个 display items（Table 4 + Table 5 + Table 6 + Figure 3），视觉极度拥挤，与前面纯文本形成强烈失衡。\n3. **Figure 3 尺寸过小**: 两个混淆矩阵挤在半栏宽度内，数字和 axis label 在正常阅读距离下难以辨认。建议改为 figure*（全宽）或移至 Appendix。\n\n**Info (9)**: 模板合规、booktabs 格式规范、Figure 2 质量最高、无 LaTeX 渲染错误或 margin overflow。\n\n---\n\n## Overall Assessment\n\n**Overall Score**: 3.0 / 5 — Findings（可被 Findings 接收）\n\n**置信度**: 4 / 5（两位 Reviewer 均为 4/5）\n\n**维度打分汇总**:\n\n| 维度 | R1 | R2 | 合并 |\n|------|-----|-----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.0 | 2.0 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**判断理由**:\n\n本文在一个新颖且有前景的问题（递归生成深度估计）上进行了极为系统的实证研究，实验覆盖面和诚实度在该领域罕见。Perplexity tail statistics 主导深度信号的发现有洞察力，EDD metric 有独立贡献价值。\n\n但五个核心限制共同构成 Findings 而非 Conference 的判断：\n\n1. **实用性断裂**: full-replacement 假设与 accumulation 实际场景的差距缺乏系统验证（N1）\n2. **规模不可信**: 14B 的 EDD=0 被 self-reference confound 污染，无法可靠归因（N2）\n3. **迁移性不足**: 跨策略 d1-d3 仅 45.9%，策略未知时方法基本失效（N3）\n4. **统计可信度**: 共线性下个体特征排名不可靠（N4）\n5. **Novelty 不足**: 标准特征 + 标准分类器，缺乏方法论创新（N5）\n\n作为 Findings 论文，其系统性实验设计、诚实的负面结果报告、以及对 perplexity tail erosion 作为 depth marker 的实证确认有一定贡献价值。\n\n**提升路径**: 如果作者能在 revision 中 (1) 补充 accumulation 场景的系统实验，(2) 提供 14B cross-reference 控制实验，(3) 补充 conditional permutation importance 或 bootstrap rank stability，(4) 调整 claim scope 为 within-strategy/known-strategy——论文有潜力在下一个 cycle 冲击 3.5–4.0（Borderline Conference 至 Conference）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 第 5 段 \"our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty\" 的自我定位是诚实的，但可能过于前置——reviewer 在第一页就看到了\"无新算法\"的声明，影响后续阅读的期望值。建议将此定位移至贡献列表之后。\n- 贡献 3 的 \"structural barrier in cross-strategy transfer (d1–d3: 45.9%)\" 以积极发现的语气呈现了一个本质上的负面结果。建议明确标注为 limitation/boundary condition。\n\n### §3 Method\n- §3.2: BOS-seeded generation 的 caveat (\"BOS-seeded generation may amplify depth signal\") 应更显著——目前只是括号内一句话。\n- §3.3: \"effective dimensionality ≈4–5\" 是重要发现但在特征设计节轻描淡写，应提升到更显著位置并讨论其对 pipeline 简化的含义。\n- §3.4: EDD 定义清晰但 T=0.70 的阈值选择依赖 Hosmer (2000) 的一般性 ROC 指南，未针对 depth estimation 场景做 task-specific 论证。\n\n### §4 Depth Degradation Atlas\n- §4.1: d0 recall >97% 的 \"free points\" 效应应在报告 headline accuracy 时明确讨论，而非只在 Table 2 caption 中提及。\n- §4.2: \"p90_ppl ranks top-2 by Gini importance in all 9 cells\" 在 VIF>10 条件下不应如此自信地声称。建议改为 \"the perplexity tail feature family consistently dominates across all 9 cells, with group-level ablation confirming...\"\n- §4.5: strategy effect (9.3pp) > model effect (7.2pp) 是重要发现，但在主文中仅占一段——考虑到这对部署的重大含义，值得更深入讨论。\n\n### §5 Generalization\n- §5.1: Binoculars 近平局（78.1% vs 78.4%, p>0.05）应更透明地讨论其对本文独特价值的含义。\n- §5.3: \"a two-stage pipeline recovers 11.5pp\" 但 presupposes 策略可识别——应明确标注为条件性（conditional）结果。\n- §5.4: 14B 结果应在主文中明确标注 self-reference confound，而非仅在 Appendix 中讨论。\n\n### §6 Discussion\n- 三段过于压缩。建议拆分 Discussion 和 Conclusion。\n- \"From ceiling to floor\" 段的 deployment scenario（depth-scored data curation）缺乏实验支撑（Appendix B.12 PoC 不显著）。\n- \"Scale dependence and outlook\" 段应讨论 self-reference confound 对 scale 叙事的影响。\n\n### Appendix\n- 15 页 29 个子节缺乏层级组织，建议按主题分组（Feature Analysis / Generalization / Ablation / Baselines）。\n- B.10 Domain Bias Analysis 中 buggy pipeline 数字增加阅读负担，建议移至脚注。\n- B.12 Curation PoC 和 B.22 Downstream Fine-Tuning 的 inconclusive 结果应在标题中明确标注（如已标注 \"Inconclusive\"——这是好的实践）。\n\n### 格式合规性\n- ✅ 主文 8 页（pp.1-8），Limitations 从第 9 页开始，合规\n- ✅ Double-blind 匿名完整，无作者身份泄露\n- ✅ ACL review 模板（acl.sty），booktabs 格式规范\n- ⚠️ 1 条 orphan bib entry (penedo2024_fineweb)\n- ⚠️ 术语残余不一致（depth estimation vs. depth classification）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# 审稿报告 — Round 17 (Fresh)\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 (ARR May cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 名 Reviewer\n- Reviewer 1: 方法严谨性 + 实验设计 + 统计有效性\n- Reviewer 2: 新颖性 + 贡献充分性 + Related Work 覆盖 + 写作质量\n\n---\n\n## Summary\n\n本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类问题，构建了覆盖 3 个模型族（Pythia-1.4B, OLMo-1B, GPT-2 XL）× 3 种解码策略（nucleus, temperature, top-k）× 4 个深度的 180K 样本基准数据集。从固定参考模型（Pythia-1.4B）的困惑度分布中提取 19 个统计特征，使用 Random Forest 分类器进行深度分类。提出 Effective Discriminable Depth (EDD) 指标量化可区分深度上限。分布内四分类准确率 68.9–85.9%（d1-d3 balanced: 58.9–81.5%），跨模型迁移 66.4%（d1-d3: 55.4%），跨策略迁移 59.1%（d1-d3: 45.9%），14B 模型 EDD=0。论文定位为 task formalization + systematic empirical characterization。\n\n---\n\n## Strengths\n\n**S1. 问题提出新颖且及时** [R1, R2 共识]\n从二元检测（human vs. AI）扩展到递归深度估计是一个自然但未被探索的方向。在 model collapse 日益受关注的背景下，\"文本经历了多少轮递归生成\"这个问题具有前瞻性。Introduction 从 model collapse → detection gap → depth estimation 建立了清晰的逻辑链。\n\n**S2. 极其系统的实验设计** [R1, R2 共识]\n3×3×4 grid + 180K 样本、8 个 generalization axis（跨模型/跨策略/跨规模/跨域/seed replication/accumulation/prompted generation/mixed-depth）、24 页附录覆盖近 30 个子实验。R1 评价：\"这是近期审稿中见过的最全面的 empirical study 之一。\"\n\n**S3. 诚实报告负面结果** [R1, R2 共识]\n14B EDD=0、cross-strategy 45.9%、downstream curation PoC 不显著（p>0.4）、跨温度 inverted AUC 等负面结果均被坦诚报告。无 cherry-picking 或隐藏不利证据。\n\n**S4. Perplexity tail statistics 发现有洞察力** [R1, R2 共识]\np90_ppl 在所有 9 cells 中排名 top-2，与 surprisal variance 共同占据 41% Gini importance。Mean perplexity 表现等同 chance (25.1%)，揭示深度信号集中在分布尾部而非均值——对后续工作有指导价值。Group-level ablation（perplexity alone 76.6% vs. full 78.4%）提供了不受共线性影响的验证。\n\n**S5. 理论框架与实验发现的良好对应** [R1]\nTail erosion 理论（§3.5）预测 perplexity tail 特征应主导深度信号，group-level ablation 确认。Scale-dependent attenuation 的理论预测在 14B 实验中得到定性验证。\n\n**S6. 控制实验设计精细** [R1]\nHeterogeneous chain + reverse-chain control（Appendix B.15）排除 architecture confound、LOGO + negative control 消除 domain bias（Appendix B.10）、temperature robustness + memorization-prerequisite 发现（Appendix B.7）展示高水平实验工程。\n\n**S7. EDD metric 有独立价值** [R1, R2 共识]\n将\"可区分深度\"从模糊概念形式化为可操作度量，contiguous pairwise AUC 的最长前缀定义简洁，可被后续工作采用。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1. Full-replacement 假设从根本上限制实用价值** [R1 critical, R2 升级为 critical]\n\n所有实验使用 full-replacement 递归链（每个深度完全替换前一代训练语料），但论文声称的应用场景（§6 \"depth-scored data curation\"）面对的是 accumulation 场景（合成和人类数据以未知比例共存）。Pilot accumulation 实验仅在 §6 中以一句话报告 \"-14 到 -15pp\"，无独立 Table、无 per-cell 分解、无 EDD 变化、无统计检验。-14 到 -15pp 相当于 full-replacement baseline 的 ~18% 相对衰减，可能使 OLMo nucleus (65.6%) 等 cell 的 d1-d3 准确率降至 ~50%，接近功能不可用。\n\nR2 的关键洞察：model collapse 文献使用 full-replacement 展示 worst-case 现象是合理的，但本文声称的目标是 data curation 工具——两个目标的实验设计要求根本不同。\n\n**N2. 14B EDD=0 被 self-reference confound 污染** [R1 critical, R2 critical + 承认自身疏漏]\n\nQwen2.5-14B 使用 self-reference（14B 模型自身计算特征），而主表（Table 2）所有 1-1.5B 实验使用 Pythia-1.4B 作为固定参考模型。这意味着观察到的 EDD=0 可能来自：(a) 纯规模效应，(b) 参考模型从 cross-reference 切换到 self-reference 导致特征语义改变，或 (c) 两者混合。论文在 Appendix B.14 承认此 confound 但未做任何控制实验来分离两个因素。\n\nR1 指出至少需要两个对照：(i) 14B + Pythia-1.4B reference（测纯规模效应），(ii) 1.4B + self-reference（测 reference 切换效应）。R2 承认这是本轮审稿中最有价值的方法论发现，修正了自己 N2 中将 EDD=0 直接归因于规模效应的分析。\n\n补充：7-8B 实验（Llama-3.1-8B 70.2% EDD=4, Qwen2.5-7B 60.1% EDD>5）表明框架在 7-8B 仍有信号，并非 \">7B 完全失效\"——更准确的表述是\"14B 出现断崖式衰减，且该衰减的归因被 confound 污染\"。\n\n**N3. 跨策略迁移 d1-d3 仅 45.9%，策略未知时方法基本失效** [R1 critical, R2 critical]\n\nCross-strategy transfer 将 d1-d3 balanced accuracy 降至 45.9%（四分类: 59.1%），仅 1.4× chance。d0 recall ≥89% 膨胀了 headline accuracy。在真实部署中解码策略通常未知，这与论文的 data provenance 应用场景根本矛盾。\n\nR1 补充了更严峻的证据：Appendix B.7 跨温度实验 leave-one-τ-out mean d1v2 AUC 仅 0.319，τ=0.5 holdout 时出现 inverted AUC (0.176)——不是\"性能下降\"而是\"特征语义在不同策略下反转\"。Two-stage pipeline（策略识别 + per-strategy 分类）恢复 11.5pp 但 presupposes 策略可被识别——循环依赖。\n\n**N4. 严重共线性（VIF>10, 14-16/19 features）下个体特征排名不可靠** [R1 critical, R2 agree with nuance]\n\n19 个特征中 14-16 个 VIF>10，有效独立维度仅 ~4-5。论文引用 Strobl et al. (2008) 和 Hooker et al. (2021) 讨论共线性影响，但并未使用 conditional permutation importance——引用方法论批评但不采纳其建议的\"自我矛盾\"。Kendall's W=0.90 across 3 methods 不能排除系统性偏差。\n\nR2 的 nuanced 回应：family-level 分析（group-level ablation: perplexity 76.6% vs. full 78.4%）不受共线性影响，支持 perplexity tail 家族主导的结论。但 individual feature ranking（\"p90_ppl ranks top-2 in all 9 cells\"）在如此共线性下不应如此自信地声称。\n\n**两位 Reviewer 共识**：family-level 结论可靠，individual feature ranking 结论需弱化。\n\n**N5. 方法层面 novelty 不足以支撑 Conference-level long paper** [R2 critical, R1 partial REBUT]\n\n19 个特征全部是标准统计量（perplexity percentiles, surprisal moments, n-gram repetition），分类器是标准 Random Forest，EDD 本质上是 contiguous pairwise AUC 的最长前缀。整个方法管道无 algorithmic novelty。\n\nR1 的 partial REBUT：(1) tail vs. mean 的特征选择并非 trivial（mean perplexity = chance, p90_ppl = 58.3%），(2) EDD 的 formalization 有独立价值（类比 BLEU），(3) \"零创新\"过于绝对。但 R1 同意就 Conference 标准而言 novelty 偏弱。\n\n**两位 Reviewer 共识**：novelty 不构成 \"零\"，但不足以支撑 Conference 录用。更适合 Findings 定位。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1. LoRA seed 仅 2 个** [R1, R2 AGREE]\nOLMo +3.17pp（CI 不重叠）说明 LoRA 初始化对绝对准确率有非平凡影响。2 个 seed 不足以建立 stability claim。至少需要 5 个 seed。\n\n**W2. 多重比较校正缺失** [R1, R2 AGREE]\n脚注声明 p-values 为 exploratory，但 Abstract 和 §6 使用确定性语言。Appendix B.12 Curation PoC 的显著性检验涉及多重比较但未校正。要么全面校正，要么全面弱化结论语气。\n\n**W3. Neural end-to-end baselines 仅测试 ≤125M backbone** [R1, R2 AGREE]\nDeBERTa-v3-base (86M) 和 RoBERTa-base (125M) 比 RF 低 20pp，但更大 backbone 可能缩小差距。R2 认为瓶颈更可能是表示空间（PLM 无法线性恢复 perplexity tail statistics）而非参数量，但需更大 backbone 验证。\n\n**W4. BOS-seeded generation 生态效度** [R1, R2 partial REBUT]\n主实验使用 BOS-seeded generation。Prompted generation 实验（-13.8pp, Appendix B.27）和 instruction-tuned model 实验（Appendix B.21）部分缓解但未完全解决——instruction-following 场景（实际中最相关）未被测试。R2 指出 §B.21 instruction-tuning 改变 AUC 衰减模式证明 gap non-trivial。\n\n**W5. Binoculars 达到统计等价性能** [R1, R2 AGREE]\nBinoculars 11-feat RF: 78.1% vs. 本文 19-feat: 78.4%（p>0.05）。额外 8 个 non-Binoculars 特征边际贡献不显著。削弱了 \"19-feature comprehensive pipeline\" 的独特价值叙事。论文应更精确地定位贡献为 formulation/benchmark 而非 pipeline 性能优势。\n\n**W6. Wild-data FPR 高达 22.4%，thresholding recall 代价未量化** [R1, R2 AGREE]\nGPT-2 XL on C4 FPR 22.4%。Confidence thresholding 降至 2.8% 但 recall/coverage 代价未报告。需 FPR-coverage tradeoff curve。\n\n**W7. §6 Discussion 过于压缩** [R2, R1 AGREE]\n3 段 ~250 词，缺少：跨策略失败根因分析、EDD ceiling 突破路径、provenance 工具互补关系、scale-up 路线图。需考虑 8 页限制约束。\n\n**W8. Downstream curation PoC 不显著但 Introduction 暗示应用** [R1, R2 AGREE]\nRF-vs-unfiltered p>0.4。RF-vs-random 的 p<0.02 涉及多重比较未校正。Introduction 和 §6 的 \"depth-scored data curation\" 叙事缺乏实验支撑。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 达成共识的关键判断：\n\n- [AGREE] **评分**: 均给出 3.0 (Findings)，置信度均为 4/5\n- [AGREE] **问题重要性**: 递归生成深度估计是有价值的新问题\n- [AGREE] **实验质量**: 系统性和诚实度均属上乘\n- [AGREE] **Full-replacement 限制** (N1): critical，需要系统性 accumulation 实验\n- [AGREE] **14B confound** (N2): critical，需要控制实验分离 scale vs. reference-model 效应\n- [AGREE] **跨策略迁移** (N3): critical，需限定 claim scope\n- [AGREE] **共线性** (N4): family-level 结论可靠，individual ranking 需弱化\n- [AGREE] **Findings 定位**: novelty 不足以支撑 Conference，但 empirical 贡献适合 Findings\n\n## Reviewer Divergence\n\n- [R1 REBUT] **R2-N1 \"零创新\"**: R1 认为 tail vs. mean 的特征选择和 EDD formalization 有非平凡价值，\"零创新\"是 overstatement。R2 承认 N1 与自己优势评价第 4 点存在内部张力。最终共识：不是\"零\"，但不足以支撑 Conference。\n- [R1 REBUT] **R2-W1 \"Atlas 过度包装\"**: R1 认为 atlas 准确描述了系统性制图的实验组织。未解决。\n- [R1 REBUT] **R2-W4 \"Abstract 信息过载\"**: R1 认为信息密度在 *ACL empirical study 中属正常。未解决。\n- [R2 partial REBUT] **R1-W4 \"BOS-seeded 生态效度\"**: R2 认为 prompted/instruction-tuned 补充实验部分缓解。部分解决。\n\n---\n\n## Questions to Authors\n\n1. 能否提供累积（accumulation）场景下的完整结果（至少覆盖部分 cells），包括 accuracy、EDD、per-class recall？pilot 中 -14 到 -15pp 的衰减是在哪个 cell 上测的？\n2. 14B 实验中，是否有技术原因无法使用 Pythia-1.4B 作为 cross-reference？如果用 Pythia-1.4B 对 Qwen2.5-14B 文本做特征提取，预期结果如何？\n3. 跨策略迁移中，是否尝试过 normalization-based domain adaptation（如 per-strategy z-score normalization）？\n4. 对于 Binoculars 近平局的结果，作者如何定位本文的独特贡献——是 formulation/benchmark，还是 method 本身？\n5. 14B EDD=0 的根因分析：是 14B 模型 perplexity 分布方差更小，还是 fine-tuning 在大模型上更\"gentle\"？是否有 per-feature 的 scale-dependent 分析？\n6. 深度 >5 时是否存在 saturation？是否有更深的初步数据？\n7. 是否考虑过将 depth estimation 与 model attribution 结合（cf. Bevendorff et al. 2025 two-paradigm framework）？\n\n---\n\n## Missing References\n\n**R1 建议**:\n- Liang et al. (2023), \"GPT Detectors Are Biased Against Non-Native English Writers\" — detection bias 与 depth estimation 的公平性直接相关\n- Sadasivan et al. (2023) 的 impossibility result 对 ordinal 设定的含义（论文已引用但未讨论）\n\n**R2 建议**:\n- \"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing\" (2025, arXiv:2502.15208) — iterative paraphrasing 的 attractor dynamics，与递归生成链高度相关\n- \"The Canary's Echo: Auditing Privacy Risks of LLM-Generated Synthetic Text\" (2025, arXiv:2502.14921) — data auditing 角度\n- \"Data Provenance Auditing of Fine-Tuned Large Language Models\" (2025, arXiv:2510.09655) — 数据来源审计\n\n**引用验证**: R2 验证 76 条 bib entries，无幻觉引用。1 条 orphan bib (penedo2024_fineweb)。\n\n---\n\n## External Review\n\n**外部审稿**: 未配置（项目未启用 paperreview.ai）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（耗时 ~3 分钟）\n\n**Warnings (3)**:\n1. **Pages 1-3 无视觉锚点**: 连续 3 页纯文本，第一个 display item（Table 1）直到第 4 页才出现。建议将 Figure 1（Atlas 热力图）或 Figure 2（AUC 衰减曲线）前移，或添加 pipeline 示意图。\n2. **Page 8 display items 堆叠**: 单页内 4 个 display items（Table 4 + Table 5 + Table 6 + Figure 3），视觉极度拥挤，与前面纯文本形成强烈失衡。\n3. **Figure 3 尺寸过小**: 两个混淆矩阵挤在半栏宽度内，数字和 axis label 在正常阅读距离下难以辨认。建议改为 figure*（全宽）或移至 Appendix。\n\n**Info (9)**: 模板合规、booktabs 格式规范、Figure 2 质量最高、无 LaTeX 渲染错误或 margin overflow。\n\n---\n\n## Overall Assessment\n\n**Overall Score**: 3.0 / 5 — Findings（可被 Findings 接收）\n\n**置信度**: 4 / 5（两位 Reviewer 均为 4/5）\n\n**维度打分汇总**:\n\n| 维度 | R1 | R2 | 合并 |\n|------|-----|-----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.0 | 2.0 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**判断理由**:\n\n本文在一个新颖且有前景的问题（递归生成深度估计）上进行了极为系统的实证研究，实验覆盖面和诚实度在该领域罕见。Perplexity tail statistics 主导深度信号的发现有洞察力，EDD metric 有独立贡献价值。\n\n但五个核心限制共同构成 Findings 而非 Conference 的判断：\n\n1. **实用性断裂**: full-replacement 假设与 accumulation 实际场景的差距缺乏系统验证（N1）\n2. **规模不可信**: 14B 的 EDD=0 被 self-reference confound 污染，无法可靠归因（N2）\n3. **迁移性不足**: 跨策略 d1-d3 仅 45.9%，策略未知时方法基本失效（N3）\n4. **统计可信度**: 共线性下个体特征排名不可靠（N4）\n5. **Novelty 不足**: 标准特征 + 标准分类器，缺乏方法论创新（N5）\n\n作为 Findings 论文，其系统性实验设计、诚实的负面结果报告、以及对 perplexity tail erosion 作为 depth marker 的实证确认有一定贡献价值。\n\n**提升路径**: 如果作者能在 revision 中 (1) 补充 accumulation 场景的系统实验，(2) 提供 14B cross-reference 控制实验，(3) 补充 conditional permutation importance 或 bootstrap rank stability，(4) 调整 claim scope 为 within-strategy/known-strategy——论文有潜力在下一个 cycle 冲击 3.5–4.0（Borderline Conference 至 Conference）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 第 5 段 \"our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty\" 的自我定位是诚实的，但可能过于前置——reviewer 在第一页就看到了\"无新算法\"的声明，影响后续阅读的期望值。建议将此定位移至贡献列表之后。\n- 贡献 3 的 \"structural barrier in cross-strategy transfer (d1–d3: 45.9%)\" 以积极发现的语气呈现了一个本质上的负面结果。建议明确标注为 limitation/boundary condition。\n\n### §3 Method\n- §3.2: BOS-seeded generation 的 caveat (\"BOS-seeded generation may amplify depth signal\") 应更显著——目前只是括号内一句话。\n- §3.3: \"effective dimensionality ≈4–5\" 是重要发现但在特征设计节轻描淡写，应提升到更显著位置并讨论其对 pipeline 简化的含义。\n- §3.4: EDD 定义清晰但 T=0.70 的阈值选择依赖 Hosmer (2000) 的一般性 ROC 指南，未针对 depth estimation 场景做 task-specific 论证。\n\n### §4 Depth Degradation Atlas\n- §4.1: d0 recall >97% 的 \"free points\" 效应应在报告 headline accuracy 时明确讨论，而非只在 Table 2 caption 中提及。\n- §4.2: \"p90_ppl ranks top-2 by Gini importance in all 9 cells\" 在 VIF>10 条件下不应如此自信地声称。建议改为 \"the perplexity tail feature family consistently dominates across all 9 cells, with group-level ablation confirming...\"\n- §4.5: strategy effect (9.3pp) > model effect (7.2pp) 是重要发现，但在主文中仅占一段——考虑到这对部署的重大含义，值得更深入讨论。\n\n### §5 Generalization\n- §5.1: Binoculars 近平局（78.1% vs 78.4%, p>0.05）应更透明地讨论其对本文独特价值的含义。\n- §5.3: \"a two-stage pipeline recovers 11.5pp\" 但 presupposes 策略可识别——应明确标注为条件性（conditional）结果。\n- §5.4: 14B 结果应在主文中明确标注 self-reference confound，而非仅在 Appendix 中讨论。\n\n### §6 Discussion\n- 三段过于压缩。建议拆分 Discussion 和 Conclusion。\n- \"From ceiling to floor\" 段的 deployment scenario（depth-scored data curation）缺乏实验支撑（Appendix B.12 PoC 不显著）。\n- \"Scale dependence and outlook\" 段应讨论 self-reference confound 对 scale 叙事的影响。\n\n### Appendix\n- 15 页 29 个子节缺乏层级组织，建议按主题分组（Feature Analysis / Generalization / Ablation / Baselines）。\n- B.10 Domain Bias Analysis 中 buggy pipeline 数字增加阅读负担，建议移至脚注。\n- B.12 Curation PoC 和 B.22 Downstream Fine-Tuning 的 inconclusive 结果应在标题中明确标注（如已标注 \"Inconclusive\"——这是好的实践）。\n\n### 格式合规性\n- ✅ 主文 8 页（pp.1-8），Limitations 从第 9 页开始，合规\n- ✅ Double-blind 匿名完整，无作者身份泄露\n- ✅ ACL review 模板（acl.sty），booktabs 格式规范\n- ⚠️ 1 条 orphan bib entry (penedo2024_fineweb)\n- ⚠️ 术语残余不一致（depth estimation vs. depth classification）"
  }
}
```

</details>

---


### Tool result

_source line 1497 · 2026-05-21T06:50:32.753009+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4728
}
```

</details>

---


### Assistant

_source line 1498 · 2026-05-21T06:50:40.144125+00:00_

审稿报告已投递。

**Round 17 审稿完成**。两名 Reviewer 经独立初审 + 交叉分享后达成共识：

**Overall: 3.0 / 5 — Findings**

5 个 Must-Fix：
1. Full-replacement 假设缺乏 accumulation 系统实验
2. 14B EDD=0 被 self-reference confound 污染
3. 跨策略迁移 d1-d3 仅 45.9%
4. VIF>10 共线性下个体特征排名不可靠
5. 方法层面 novelty 不足以支撑 Conference

8 个 Should-Fix + 5 个 Minor。Issue Tracker 已同步更新（17 条 Round 17 新 issue + 历史 issue 状态追踪）。

提升路径：补充 accumulation 系统实验 + 14B cross-reference 控制实验 + conditional permutation importance + claim scope 限定，可在下一 cycle 冲击 3.5–4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 138

## Round 138

2 recorded events


### User

_source line 1499 · 2026-05-21T06:50:43.194317+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**核心结论**：

- **4 个 Must-Fix 全部 AGREE**，其中 R1-N2（14B self-reference confound）是我 Round 1 的重要疏漏，R1-N1 我从 Should-Fix 升级为同意 critical
- **6 个 Should-Fix 中 5 个 AGREE、1 个 REBUT**（R1-W4 BOS-seeded generation——论文有 prompted/instruction-tuned 补充实验部分缓解）
- R1 的统计方法论批评（共线性、多重比较、seed 数量）技术上正确，补充了我在 novelty/impact 维度的审查
- 维持 **Overall 3.0 (Findings)**，两位 Reviewer 的 concern 集合高度互补

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1500 · 2026-05-21T06:50:56.884289+00:00_

审稿报告已投递至 Research Director。

**Round 17 审稿完成，总结**：

- **Overall Score**: 3.0 / 5 — Findings
- **Reviewer 编排**: 2 名 Reviewer，1 轮独立审稿 + 1 轮交叉分享，关键问题全部收敛
- **5 个 Must-Fix**: full-replacement 假设(N1)、14B self-reference confound(N2)、跨策略迁移 45.9%(N3)、共线性下特征排名(N4)、novelty 不足(N5)
- **8 个 Should-Fix**: LoRA seed 不足、多重比较未校正、neural baseline 规模小、BOS-seeded 生态效度、Binoculars 近平局、wild-data FPR、Discussion 压缩、curation PoC 不显著
- **视觉审查**: 3 warnings（前 3 页无视觉锚点、page 8 堆叠、Figure 3 过小）
- **Issue Tracker**: 已同步更新至 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 139

## Round 139

68 recorded events


### User

_source line 1501 · 2026-05-21T21:29:06.605328+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recursive_gen_depth_est
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1502 · 2026-05-21T21:29:13.080638+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1503 · 2026-05-21T21:29:13.182247+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1504 · 2026-05-21T21:29:22.057204+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1505 · 2026-05-21T21:29:22.108060+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1506 · 2026-05-21T21:29:26.923850+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1507 · 2026-05-21T21:29:26.975454+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1508 · 2026-05-21T21:29:32.159964+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1509 · 2026-05-21T21:29:32.210586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1510 · 2026-05-21T21:29:37.758040+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1511 · 2026-05-21T21:29:39.419158+00:00_

{"result":"# 项目 recursive_gen_depth_est 概况\n\n## 实验状态 (145 个)\n\n- **cross_model_olmo_temp09_001**: DONE (killed) — \n- **pythia_topk50_001**: DONE (success) — \n- **cross_model_gpt2xl_001**: DONE (success) — \n- **cross_model_olmo_002**: DONE (success) — \n- **pythia_temp09_001**: DONE (success) — \n- **mvp_pipeline_pythia_002**: DONE (success) — \n- **cross_model_olmo_001**: DONE (failed) — \n- **mvp_pipeline_qwen_base_004**: DONE (killed) — \n- **mvp_pipeline_pythia_001**: DONE (killed) — \n- **mvp_pipeline_base_002**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (killed) — \n- **mvp_pipeline_001**: DONE (killed) — \n- **mvp_pipeline_base_003**: DONE (killed) — \n- **mvp_pipeline_004**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| accum_pythia_nuc_002 | Accumulation scenario with Pythia-1.4B nucleus sampling shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3): mix25 ~70% and mix50 ~69%, confirming cross-model consistency of accumulation effects on depth estimation. Retry of accum_pythia_nuc_001 (failed due to cuda:1 not existing). | — | — | — |\n| conditional_pi_001 | Perplexity tail features (p90_ppl, kurtosis_ppl, var_ppl, etc.) remain the top-ranked feature family under permutation importance (not Gini), with stable bootstrap rank CIs across all 9 model-strategy cells, refuting R17's concern that VIF>10 collinearity invalidates importance rankings. | — | — | — |\n\n## 待处理\n- accum_v2_mix25（准备中）\n- accum_v2_mix50（准备中）\n\n## 近期结论\n- **accum_olmo_temp_001** (success): Accumulation scenario with OLMo-1B temp0.9 shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3), confirming cross-strategy consistency of accumulation effects on depth estimation\n- **accum_pythia_nuc_001** (failed): Accumulation scenario with Pythia-1.4B nucleus sam
…[truncated 1829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1661
}
```

</details>

---


### Tool call

_source line 1512 · 2026-05-21T21:29:39.570528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1513 · 2026-05-21T21:29:40.374121+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\setlength{\dbltextfloatsep}{4pt plus 2pt minus 2pt}
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{method}
38	
39	\input{theory}
40	
41	\input{atlas}
42	
43	\input{generalization}
44	
45	\input{discussion}
46	
47	\input{conclusion}
48	
49	\bibliography{references}
50	
51	\clearpage
52	\appendix
53	\input{section_appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-21T21:29:40.374594+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1515 · 2026-05-21T21:29:41.431056+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1516 · 2026-05-21T21:29:41.635580+00:00_

-rw-r--r-- 1 ubuntu ubuntu 3681306 May 21 21:27 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 204
}
```

</details>

---


### Tool result

_source line 1517 · 2026-05-21T21:29:45.504263+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"}]

I searched for "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.or
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5129
}
```

</details>

---


### Tool call

_source line 1518 · 2026-05-21T21:29:52.291445+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1519 · 2026-05-21T21:29:52.704142+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 conference main paper submission deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 conference main paper submission deadline ARR cycle"
  }
}
```

</details>

---


### Tool result

_source line 1520 · 2026-05-21T21:29:58.575328+00:00_

Web search results for query: "EMNLP 2026 conference main paper submission deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here is the information about EMNLP 2026 conference main paper submission:

## EMNLP 2026 Main Paper Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026.

## Key Details about the ARR Cycle

Papers must be submitted by the ARR 2026 May cycle at the latest. Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.

## Important Policy for EMNLP 2026

For the ARR 2026 May cycle aligned with both EMNLP and AACL, a
…[truncated 467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5871
}
```

</details>

---


### Tool result

_source line 1521 · 2026-05-21T21:29:59.230218+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and author instructions:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. However, the "Limitations" section (along with, optionally, a section for ethical considerations) may be up to one page and will not count toward the final p
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6938
}
```

</details>

---


### Tool call

_source line 1522 · 2026-05-21T21:30:05.217466+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1523 · 2026-05-21T21:30:05.218029+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1524 · 2026-05-21T21:30:10.654071+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits (long paper, short paper), formatting requirements, anonymity rules, appendix rules, citation format, ARR submission deadline, commitment deadline, any special policies for EMNLP 2026. Return all details verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits (long paper, short paper), formatting requirements, anonymity rules, appendix rules, citation format, ARR submission deadline, commitment deadline, any special policies for EMNLP 2026. Return all details verbatim."
  }
}
```

</details>

---


### Tool call

_source line 1525 · 2026-05-21T21:30:12.013105+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission guidelines: page limits for long and short papers, formatting requirements, anonymity policy, limitations section rules, ethical considerations, responsible NLP checklist, and any other requirements. Return all details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the complete submission guidelines: page limits for long and short papers, formatting requirements, anonymity policy, limitations section rules, ethical considerations, responsible NLP checklist, and any other requirements. Return all details."
  }
}
```

</details>

---


### Tool result

_source line 1526 · 2026-05-21T21:30:15.834138+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long Papers:** "8 pages" with one additional page allowed in camera-ready version (up to 9 pages)
- **Short Papers:** "4 pages" with one additional page allowed in camera-ready version (up to 5 pages)

## Key Deadlines
- ARR submission: "May 25, 2026"
- Reviewer registration: "May 27, 2026"
- EMNLP commitment: "August 2, 2026"
- Acceptance notification: "August 20, 2026"
- Camera-ready due: "September 20, 2026"

All deadlines are "11:59PM UTC-12:00 ('anywhere on Earth')"

## Anonymity & Review
- "The reviewing process will continue to be double-blind"
- "No anonymity period requirement" per ACL and ARR policies
- "Instructions for Two-Way Anonymized Review" must be followed

## Formatting & Content Requirements
Authors must adhere to all ARR submission requirements including:
- Publication Ethics Policy compliance
- Ethics policy with responsible NLP research checklist
- Limitations section required
- "Optional Supplementary Materials" (appendices, software, data) permitted
- Citation and comparison guidelines per ARR standards

## Special EMNLP 2026 Policies
- "Dual submissions are not allowed"
- Author lists cannot be modified during commitment phase (reordering permitted)
- Desk rejection applies for violations of integrity policies including "hallucinated citations" and "entirely AI-generated papers"

## Presentation Requirement
"All accepted papers must be presented at the conference to appear in the proceedings"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "elapsed_ms": 5180
}
```

</details>

---


### Tool result

_source line 1527 · 2026-05-21T21:30:21.479162+00:00_

# ACL Rolling Review Submission Guidelines

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations section (required, after conclusion)
- Optional ethical considerations section (untitled or titled "Ethical considerations")
- Unlimited reference pages
- Exceeding length or missing limitations = desk rejection

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations section (required, after conclusion)
- Optional ethical considerations section
- Unlimited reference pages
- Exceeding length or missing limitations = desk rejection

## Formatting Requirements

Papers must follow the official ACL style template from GitHub (acl-org/acl-style-files). Authors cannot modify these files or use other conference templates. Submissions must adhere to ACL Author Guidelines regarding paper size, margins, and font. Non-conforming submissions face rejection without review.

## Anonymity Policy

Papers must omit author names, affiliations, and self-identifying references. Instead of "We previously showed," use "Smith previously showed." All supplementary materials require anonymization. Cloud storage links (Dropbox) are prohibited; anonymous repositories are required. Submissions violating anonymity rules face desk rejection.

## Limitations Section (Required)

This dedicated section appears before references and outside page counts. The section discusses constraints of presented work only—it cannot introduce new methods, analysis, or results. Submissions lacking this section face desk rejection. This applies to both long and short papers.

## Ethical Considerations

Authors should address ethical impact and broader implications in an optional section (doesn't count toward page limits). All authors must complete the Responsible NLP Checklist. Papers flagged for ethical concerns undergo further review by the Ethics Advisory Committee. Inadequate ethical engagement can result in rejection.

## Responsible NLP Checklist

Com
…[truncated 1194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "elapsed_ms": 9466
}
```

</details>

---


### Tool call

_source line 1528 · 2026-05-21T21:30:27.477920+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1529 · 2026-05-21T21:30:28.951565+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/memory.md\", \"content\": \"# Project Memory\\n\\n## Paper Placeholder Values (2026-05-15)\\n\\nComputed from experimental data for paper XX.X% placeholders:\\n\\n### 1. d0-excluded 3-class accuracy range (abstract.tex L5)\\n- **58.8%–82.6%** across 9 cells\\n- Source: `granularity_ablation_rf_001` registry entry, per_cell 3class acc\\n- Min: pythia_topk50 = 58.83%, Max: gpt2xl_temp09 = 82.60%\\n\\n### 2. Cross-strategy LOO d1-d3 accuracy (generalization.tex L95)\\n- **45.9%** (mean across 9 folds)\\n- Source: confusion matrices in `w6_cross_strategy_per_class_recall.json`\\n- Method: (d1_correct + d2_correct + d3_correct) / 15000 per fold, then averaged\\n- Note: 4-class mean was 59.1%; d0's near-perfect accuracy inflates it. Excluding d0 drops to 45.9%.\\n- Range across folds: 35.4% (pythia_topk50) to 59.1% (pythia_nucleus)\\n\\n### Artifact\\n- `artifacts/placeholder_values.json` — full breakdown with per-fold numbers\\n\\n## Downstream Curation PoC Insights (2026-05-15)\\n\\n### Oracle ≤ Unfiltered（反直觉发现）\\n- 完美 depth 筛选（oracle）反而不优于 unfiltered 全量数据：oracle_strict PPL 15.879 vs unfiltered 15.776（p=0.22）\\n- 原因推测：纯按 depth 筛选过度移除了有用的多样性，RF 的分类误差反而保留了有价值的变异\\n- **Framing 含义**：不能 claim \\\"RF approximates oracle\\\"，应 claim \\\"data efficiency\\\"（RF 用 44% 数据 ≈ 全量 PPL）\\n\\n### rf_moderate 统计检验偏差\\n- 我们的 t=-3.77 (p=0.02) vs Reviewer 手算 t=-5.58 (p=0.005)\\n- 其余 3 组对比偏差 <8%，此组偏差较大，以原始数据直接计算为准\\n- 定性结论一致（均显著），不影响 claim\\n\\n## ⚠️ Wild Data 解读约束 C004 (2026-05-17)\\n\\n**硬约束**：wild data RF 分类结果的 d1+ 预测是 OOD 假阳性率（FPR），不是 AI contamination 证据。\\n- C4 FPR 34%、FineWeb FPR 17%：差异来自 FineWeb 质量过滤去除了特征异常文本，不代表 C4 有更多 AI 内容\\n- C4 采集于 2019 年 Common Crawl，彼时几乎不存在 LLM 生成内容\\n- 论文中**禁止**说 \\\"contamination\\\"、\\\"AI-generated content detected\\\"\\n- 正确 framing：method limitation + calibration gap\\n- 教训：不要将分类器在 OOD 数据上的预测当作真实标签解读\\n\\n## Downstream Be
…[truncated 1470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1473
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-21T21:30:29.404664+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/ | head -40",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/ | head -40",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 1531 · 2026-05-21T21:30:30.412952+00:00_

_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
atlas.tex
conclusion.tex
discussion.tex
drafts
figures
generalization.tex
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
section_appendix.tex
theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-21T21:30:30.464091+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-21T21:30:30.868546+00:00_

issues:
# ============================================================
# ROUND 17 — MUST-FIX (Critical)
# ============================================================

- id: R17-N1
  summary: Full-replacement 假设从根本上限制实用价值——accumulation 场景无系统实验
  category: experiment
  severity: critical
  status: open
  first_raised_round: 17
  last_seen_round: 17
  mentions:
  - {round: 17, reviewers: [1, 2], note: "R1 列为 N1 critical, R2 原列 W2 后升级为 critical。两人共识：pilot accumulation 仅报 -14~-15pp 无 Table/per-cell/EDD/统计检验"}
  - {round: 12, reviewers: [1, 2], note: "历史: R16-W1 (framing) resolved via §6 段落，但实验数据缺口未填补"}
  action_items:
  - {round: 17, action: "需用户确认是否做新 accumulation 实验。已有 accum_v3 (Pythia nucleus, mix25/mix50) DONE 数据已引用于论文。新增 cells 需新实验。", assigned_to: research_director, status: open}
  resolution: ""
  resolution_round: null

- id: R17-N2
  summary: 14B EDD=0 被 self-reference confound 污染——无法分离规模效应 vs 参考模型切换
  category: experiment
  severity: critical
  status: open
  first_raised_round: 17
  last_seen_round: 17
  mentions:
  - {round: 17, reviewers: [1, 2], note: "R1 首次识别 confound（N2 critical），R2 完全认同。14B 用 self-reference 而主表用 Pythia-1.4B cross-reference"}
  action_items:
  - {round: 17, action: "需用户确认。控制实验：Pythia-1.4B ref on 14B data（仅 feature extraction，~2-3h）", assigned_to: research_director, status: open}
  resolution: ""
  resolution_round: null

- id: R17-N3
  summary: 跨策略迁移 d1-d3 仅 45.9%——策略未知时方法基本失效，与应用场景矛盾
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 17
  last_seen_round: 17
  mentions:
  - {round: 17, reviewers: [1, 2], note: "R1-N3 + R2-N3 完全共识"}
  - {round: 12, reviewers: [1, 2], note: "历史: R16-N3 resolved via reframe，但 claim scope 仍超出"}
  action_items:
  - {round: 17, action: "Abstract 已加 'depth estimation claims hold most strongly within-strategy or when the decoding configuration is known'; §5.3 已有 scope 限定; §1 贡献3 改为 boundary condition", assigned_to: research_director, status: done}
  resolution: "R17 writing f
…[truncated 14227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-21T21:30:31.522663+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-21T21:30:31.574533+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-21T21:30:44.100269+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1537 · 2026-05-21T21:30:44.101194+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1538 · 2026-05-21T21:30:49.949824+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "glob": "*.yaml",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
    "glob": "*.yaml",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-21T21:30:50.452516+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-21T21:30:50.603602+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/recursive_gen_depth_est/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/recursive_gen_depth_est/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
  }
}
```

</details>

---


### Tool result

_source line 1541 · 2026-05-21T21:30:50.654228+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1542 · 2026-05-21T21:30:53.976957+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "glob": "*.yaml",
  "output_mode": "content",
  "-C": "2",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
    "glob": "*.yaml",
    "output_mode": "content",
    "-C": "2",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1543 · 2026-05-21T21:30:54.028007+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1544 · 2026-05-21T21:30:58.885078+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "output_mode": "content",
  "-C": "2",
  "head_limit": "30",
  "glob": "*.{yaml,yml,json,toml}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
    "output_mode": "content",
    "-C": "2",
    "head_limit": "30",
    "glob": "*.{yaml,yml,json,toml}"
  }
}
```

</details>

---


### Tool result

_source line 1545 · 2026-05-21T21:30:58.936098+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-21T21:31:19.831814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1547 · 2026-05-21T21:31:20.185371+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a 180K-passage benchmark spanning three model families, three decoding strategies, and four depths under controlled full-replacement chains at the 1--1.5B parameter scale.
4	A lightweight pipeline (19 statistical features classified by Random Forest) achieves d1--d3 balanced accuracy of 59--82\% across nine model--strategy cells, with $\mathrm{EDD}_{0.70} = 3$ in 8/9 cells.
5	Three findings emerge: (1)~depth signal concentrates in perplexity distribution tails, corroborated by classifier convergence and independent cross-perplexity features; (2)~decoding strategy affects cross-condition transfer more than model architecture, suggesting structurally distinct degradation trajectories; (3)~signal attenuates with scale (14B cross-reference accuracy ${\sim}44$\%, $\mathrm{EDD}_{0.70}{=}2$), with reference-model choice accounting for ${\sim}7$\,pp of the apparent degradation.
6	Perturbation-based and membership-inference baselines lack ordinal depth resolution, confirming that depth estimation requires distributional statistics beyond binary detection scores.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1548 · 2026-05-21T21:31:20.185996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-21T21:31:20.387281+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	In this work, we focus on the 1--1.5B parameter regime under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination typically involves partial mixing (accumulation), where synthetic and human data co-exist at unknown proportions; the full-replacement setting provides an upper bound on depth signal strength, and we discuss implications for accumulation settings in \S\ref{sec:discussion}.
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors \cite{binoculars2024,fast_detectgpt2024,diveye2026} collapse all depths $d \geq 1$ into a single category; watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	We find that
…[truncated 3227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-21T21:31:20.387756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-21T21:31:20.439228+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 6335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1552 · 2026-05-21T21:31:26.718291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 1553 · 2026-05-21T21:31:27.221383+00:00_

1	\subsection{Theoretical Grounding}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed by its dominance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), predicting weaker per-step signal.
15	Qwen2.5-14B supports this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B; \S\ref{sec:gen:crossscale}); however, 7--8B results are mixed ($\mathrm{EDD}_{0.70}$ ranging from 4 to 5), suggesting confounds (QLoRA quantization, architecture) interact with the scale effect (Appendix~\ref{app:cross_scale_full}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; tempera
…[truncated 447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1554 · 2026-05-21T21:31:27.221914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 1555 · 2026-05-21T21:31:27.674671+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells at the 1--1.5B parameter scale, evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}1{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: mean absolute error (MAE)\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references (Appendix~\ref{app:re
…[truncated 9053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1556 · 2026-05-21T21:31:27.725486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 1557 · 2026-05-21T21:31:28.681062+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares methods across all 9 cells.
10	Four classifiers (RF, XGBoost, ordinal MLP, prototypical) converge within 0.8\,pp under cross-model transfer (Appendix~\ref{app:learned_estimator}), confirming a feature-determined accuracy ceiling.
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA) underperforms RF by 16--32\,pp (d2 recall 8.4\%); RoBERTa-DCOL (ordinal contrastive; 64.5\%) narrows the gap but remains 14\,pp below RF.
14	
15	\paragraph{Binary detectors and membership inference.}
16	Perturbation-based (DetectGPT, 28.8\%) and membership-inference (Min-K\% Prob, 33.2\%; Min-K\%++ \cite{zhang2024_minkpp} comparable) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); CORAL calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%).
17	Binoculars \cite{binoculars2024}, calibrated with 11-feature RF, independently converges to 78.1\% ($p{>}0.05$ vs.\ our 78.4\%); merging all 30 features yields 82.6\% (Appendix~\ref{app:feature_ablation_bino}).
18	
19	\paragraph{Surface-text ablation.}
20	Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (best 36.2\%; Appendix~\ref{app:zeroshot_prompt}) also fail; depth signal resides in distributional statistics inaccessible from surface text.
21	
22	\begin{table}[t]
23	\centering
24	\small
25	\caption{Method comparison (RF mean across 9 cells, 5-fold CV). Chance = 25\% / 33.3\% (d1--d3). $^\dagger$Adapted from binary detection; Binoculars 11-feat: $p{>}0.05$ vs.\ 19-feat RF (paired permutation test).}
26	\label{tab:baselines}
27	\resizebox{\columnwidth}{!}
…[truncated 3575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1558 · 2026-05-21T21:31:28.681440+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1559 · 2026-05-21T21:31:28.782095+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	Depth signal concentrates in perplexity tails because recursive training shifts the bulk distribution only gradually; erosion appears first in upper quantiles \cite{dohmatob2024_tale_of_tails}.
5	The strategy effect (9.3\,pp) exceeding the model effect (7.2\,pp) implies auditing pipelines must account for decoding configuration.
6	Full-replacement chains provide the discriminability ceiling (d1--d3: 59--82\%); pilot accumulation ($-$14 to $-$15\,pp) and 14B cross-reference ($\mathrm{EDD}_{0.70}$: 0${\to}$2, ${\sim}$7\,pp reference-model mismatch) confirm signal survives but attenuates with mixing and scale, motivating depth-aware curation \citep{drayson2025_detection_prevents_collapse}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1560 · 2026-05-21T21:31:28.782451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-21T21:31:28.832992+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	All experiments use full-replacement recursive chains, where each depth fully replaces the prior training corpus.
6	Real-world contamination typically involves accumulation, where synthetic and human data co-exist at unknown proportions \cite{gerstgrasser2024_accumulate}.
7	Pilot accumulation experiments show 14--15\,pp attenuation relative to full-replacement; our results therefore represent an upper bound on feature separability, and extending the framework to accumulation settings is a priority for future work.
8	
9	\paragraph{Scale and generalization boundaries.}
10	The primary benchmark uses 1--1.5B parameter models with controlled LoRA fine-tuning.
11	At 14B, cross-reference accuracy drops to 44.1\% with $\mathrm{EDD}_{0.70}{=}2$ (nucleus/temperature); reference-model choice accounts for ${\sim}$7\,pp of the apparent degradation, and the remaining signal attenuation constitutes a scale-dependent boundary for the current feature set.
12	Cross-strategy transfer drops d1--d3 accuracy to 45.9\%, and on web-crawl data (C4) false positive rates reach 22\%; these gaps narrow with confidence thresholding and strategy-aware pipelines but are not fully resolved.
13	Additional caveats (reference model dependency, ${\leq}$11\,pp; single LoRA seed, ${\sim}$1--3\,pp uncertainty; adversarial robustness; passage length sensitivity) are detailed in the Appendix.
14	
15	\section*{Ethics Statement}
16	
17	This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
18	No human subjects were involved, no private or sensitive data were collected, and no new models were released.
19	Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-o
…[truncated 267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1562 · 2026-05-21T21:31:54.957354+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1563 · 2026-05-21T21:32:15.501893+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20544
}
```

</details>

---


### Tool call

_source line 1564 · 2026-05-21T21:32:15.654108+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性与实验充分性**。\n\n## 论文信息\n- 标题：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf\n\n## 目标 Venue\n- **EMNLP 2026**（ARR May cycle），截止 2026-05-25\n- Long paper：主文 ≤8 页，Limitations 不计入页数，参考文献无限制\n- Double-blind，ACL 模板\n- ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 实验设计与统计方法\n- 180K benchmark 的构建合理性（3 模型 × 3 解码策略 × 4 深度）\n- LoRA finetuning 链的可靠性（single seed? 超参选择有 ablation 吗？）\n- Random Forest 作为主分类器的合理性和充分性\n- EDD 度量的定义和 threshold T=0.70 的 justification\n- 统计检验的适当性（bootstrap CI、p-values、多重比较校正）\n- 5-fold CV 是否存在潜在的数据泄露\n\n### 2. Baseline 和 Ablation 充分性\n- Baseline 覆盖度：binary detectors、neural end-to-end、zero-shot LLM\n- Neural baseline (DeBERTa/RoBERTa) 是否公平对比（backbone 大小、训练设置）\n- Binoculars 达到统计等价（p>0.05）对论文 claim 的影响\n- Feature ablation 是否充分（group-level vs individual）\n- VIF>10 下个体特征排名的可靠性\n\n### 3. 泛化实验的严谨性\n- Cross-model transfer (66.4%) 的实验设计\n- Cross-strategy transfer (d1-d3: 45.9%) 对核心 claim 的影响\n- 14B scale 实验：self-reference vs cross-reference confound\n- Cross-domain (arXiv 74.1%) 的评估方式\n- Accumulation scenario 的实验覆盖是否充分\n\n### 4. 可重复性\n- 超参报告完整性\n- 随机种子控制\n- 代码/数据可获取性\n\n请严格按 EMNLP/ARR 审稿标准评审。输出格式：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/minor)\n4. Questions for Authors\n5. Missing References\n6. Overall Assessment (评分 + 置信度)\n7. Detailed Comments (按 section)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查**方法严谨性与实验充分性**。\n\n## 论文信息\n- 标题：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf\n\n## 目标 Venue\n- **EMNLP 2026**（ARR May cycle），截止 2026-05-25\n- Long paper：主文 ≤8 页，Limitations 不计入页数，参考文献无限制\n- Double-blind，ACL 模板\n- ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 实验设计与统计方法\n- 180K benchmark 的构建合理性（3 模型 × 3 解码策略 × 4 深度）\n- LoRA finetuning 链的可靠性（single seed? 超参选择有 ablation 吗？）\n- Random Forest 作为主分类器的合理性和充分性\n- EDD 度量的定义和 threshold T=0.70 的 justification\n- 统计检验的适当性（bootstrap CI、p-values、多重比较校正）\n- 5-fold CV 是否存在潜在的数据泄露\n\n### 2. Baseline 和 Ablation 充分性\n- Baseline 覆盖度：binary detectors、neural end-to-end、zero-shot LLM\n- Neural baseline (DeBERTa/RoBERTa) 是否公平对比（backbone 大小、训练设置）\n- Binoculars 达到统计等价（p>0.05）对论文 claim 的影响\n- Feature ablation 是否充分（group-level vs individual）\n- VIF>10 下个体特征排名的可靠性\n\n### 3. 泛化实验的严谨性\n- Cross-model transfer (66.4%) 的实验设计\n- Cross-strategy transfer (d1-d3: 45.9%) 对核心 claim 的影响\n- 14B scale 实验：self-reference vs cross-reference confound\n- Cross-domain (arXiv 74.1%) 的评估方式\n- Accumulation scenario 的实验覆盖是否充分\n\n### 4. 可重复性\n- 超参报告完整性\n- 随机种子控制\n- 代码/数据可获取性\n\n请严格按 EMNLP/ARR 审稿标准评审。输出格式：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/minor)\n4. Questions for Authors\n5. Missing References\n6. Overall Assessment (评分 + 置信度)\n7. Detailed Comments (按 section)"
  }
}
```

</details>

---


### Tool result

_source line 1565 · 2026-05-21T21:32:31.608712+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15954
}
```

</details>

---


### Tool call

_source line 1566 · 2026-05-21T21:32:31.711981+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "recursive_gen_depth_est",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性、完整性与写作质量**。\n\n## 论文信息\n- 标题：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf\n\n## 目标 Venue\n- **EMNLP 2026**（ARR May cycle），截止 2026-05-25\n- Long paper：主文 ≤8 页，Limitations 不计入页数，参考文献无限制\n- Double-blind，ACL 模板\n- ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 任务定义（recursive generation depth estimation）的原创性\n- EDD 度量的独立价值\n- \"标准特征 + 标准分类器\"的方法创新度是否满足 EMNLP 发表门槛\n- 与 model collapse 文献、binary detection 文献的差异化是否充分\n- 论文自我定位为\"benchmark-driven empirical study\"——这个定位在 EMNLP 是否可接受\n\n### 2. Related Work 覆盖\n- model collapse 文献是否完整（Shumailov, Dohmatob, Alemohammad, Gerstgrasser, Bertrand, Drayson）\n- AI-generated text detection 文献覆盖\n- 是否遗漏重要相关工作（特别是 2025-2026 年的新工作）\n- 引用格式是否符合 ACL/ARR 规范\n\n### 3. Claim-Evidence 对齐\n- Abstract 中的 claim 是否被主文 evidence 充分支撑\n- \"three findings\" 结构是否清晰\n- 统计数字密度是否合理\n- Limitations 覆盖是否充分且诚实\n- §6 Discussion 的深度和广度\n\n### 4. 写作质量与格式\n- 论文结构是否清晰（逻辑流是否通顺）\n- 术语一致性（depth estimation vs classification 等）\n- 页数合规（主文 ≤8 页）\n- 匿名合规（是否有 de-anonymization 风险）\n- Display items（figures, tables）的质量和分布\n- Limitations 和 Ethics Statement 是否合规\n\n### 5. Framing 风险\n- Full-replacement vs accumulation 的 framing 是否会误导读者\n- 14B EDD=0 (self-ref) / EDD=2 (cross-ref) 对叙事的冲击\n- Cross-strategy transfer d1-d3 45.9% 如何影响论文的应用价值主张\n- Downstream curation 的 claim 强度是否与 evidence 匹配\n\n请严格按 EMNLP/ARR 审稿标准评审。输出格式：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/minor)\n4. Questions for Authors\n5. Missing References\n6. Overall Assessment (评分 + 置信度)\n7. Detailed Comments (按 section)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "recursive_gen_depth_est",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查**新颖性、完整性与写作质量**。\n\n## 论文信息\n- 标题：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf\n\n## 目标 Venue\n- **EMNLP 2026**（ARR May cycle），截止 2026-05-25\n- Long paper：主文 ≤8 页，Limitations 不计入页数，参考文献无限制\n- Double-blind，ACL 模板\n- ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 任务定义（recursive generation depth estimation）的原创性\n- EDD 度量的独立价值\n- \"标准特征 + 标准分类器\"的方法创新度是否满足 EMNLP 发表门槛\n- 与 model collapse 文献、binary detection 文献的差异化是否充分\n- 论文自我定位为\"benchmark-driven empirical study\"——这个定位在 EMNLP 是否可接受\n\n### 2. Related Work 覆盖\n- model collapse 文献是否完整（Shumailov, Dohmatob, Alemohammad, Gerstgrasser, Bertrand, Drayson）\n- AI-generated text detection 文献覆盖\n- 是否遗漏重要相关工作（特别是 2025-2026 年的新工作）\n- 引用格式是否符合 ACL/ARR 规范\n\n### 3. Claim-Evidence 对齐\n- Abstract 中的 claim 是否被主文 evidence 充分支撑\n- \"three findings\" 结构是否清晰\n- 统计数字密度是否合理\n- Limitations 覆盖是否充分且诚实\n- §6 Discussion 的深度和广度\n\n### 4. 写作质量与格式\n- 论文结构是否清晰（逻辑流是否通顺）\n- 术语一致性（depth estimation vs classification 等）\n- 页数合规（主文 ≤8 页）\n- 匿名合规（是否有 de-anonymization 风险）\n- Display items（figures, tables）的质量和分布\n- Limitations 和 Ethics Statement 是否合规\n\n### 5. Framing 风险\n- Full-replacement vs accumulation 的 framing 是否会误导读者\n- 14B EDD=0 (self-ref) / EDD=2 (cross-ref) 对叙事的冲击\n- Cross-strategy transfer d1-d3 45.9% 如何影响论文的应用价值主张\n- Downstream curation 的 claim 强度是否与 evidence 匹配\n\n请严格按 EMNLP/ARR 审稿标准评审。输出格式：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/minor)\n4. Questions for Authors\n5. Missing References\n6. Overall Assessment (评分 + 置信度)\n7. Detailed Comments (按 section)"
  }
}
```

</details>

---


### Tool result

_source line 1567 · 2026-05-21T21:32:33.137108+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1425
}
```

</details>

---


### Assistant

_source line 1568 · 2026-05-21T21:32:46.493261+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发，后台并行执行
- **Reviewer 1**（方法严谨性 + 实验充分性）：任务已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：任务已分配

等待两位 Reviewer 返回独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 140

## Round 140

2 recorded events


### User

_source line 1569 · 2026-05-21T21:39:39.361533+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 新颖性、完整性与写作质量

---

## 1. Summary

本文提出将递归生成深度估计（recursive generation depth estimation）形式化为序数分类问题，构建了一个包含 3 个模型族（Pythia-1.4B, OLMo-1B, GPT-2 XL）× 3 种解码策略 × 4 个深度（d0–d3）的 180K 样本基准测试，使用 19 维统计特征（perplexity 尾部统计量、surprisal 统计量、词汇多样性、重复度）+ Random Forest 分类器进行深度估计。论文提出了 Effective Discriminable Depth (EDD) 度量来量化信号衰减深度，并通过 Depth Degradation Atlas 系统分析了特征重要性的跨条件模式。三个主要发现：(1) perplexity 尾部特征是主导判别器；(2) 解码策略对跨条件迁移的影响大于模型架构；(3) 信号随模型规模增大而衰减。

---

## 2. Strengths

**S1. 任务定义的新颖性与实际意义。** 将 AI 文本检测从二分类（real vs. synthetic）推进到有序多分类（估计递归深度 d∈{0,1,...,K}）是一个有意义的概念跃迁。这直接对接 model collapse 文献的核心关切——不同递归深度的退化程度不同，二分类丢失了这一维度信息。任务定义本身是论文最重要的贡献。

**S2. 系统性的实验设计。** 3 模型族 × 3 解码策略 × 4+ 深度的网格设计，配合 5-fold CV、跨模型/跨策略迁移测试、7–8B/14B 跨规模实验（§5.4, Appendix B.14–B.17），实验轴覆盖全面。180K 样本的数据量对于这类实证研究是充分的。

**S3. EDD 度量的实用价值。** Effective Discriminable Depth（Definition 1, §3.4）提供了一个可操作的单一数字来量化"深度信号能穿透多远"，比单纯报告分类准确率更信息量丰富。其与 contraction factor α^d 的指数衰减关联（§3.5, Table 5 的 n^α 上界）建立了与 model collapse 理论的桥梁。

**S4. Depth Degradation Atlas 的分析深度。** §4.2–4.3 的特征重要性分析（Gini + SHAP + permutation 三重验证，Appendix B.2）、跨条件一致性分析（Kendall's W=0.90）、EDD 与深度的单调关系（Spearman ρ=−1, Figure 3）展现了扎实的实证工作。

**S5. 充分的消融和对比。** 论文在附录中提供了大量消融实验：特征子集消融（B.1）、置换重要性（B.2）、特征轨迹（B.3）、per-class recall（B.4）、DCOL 迭代（B.5）、zero-shot LLM baseline（B.6）、温度鲁棒性（B.7）、特征重叠分析（B.8）、end-to-end PLM baseline（B.9）、域偏差分析（B.10）、wild-data 标定（B.11）、下游 curation PoC（B.12）、参考模型消融（B.13）、7–14B 跨规模（B.14–B.17）等。工作量令人印象深刻。

**S6. Related Work 覆盖度良好。** Model collapse 核心文献（Shumailov 2024 Nature, Dohmatob 3 篇, Alemohammad MAD, Gerstgrasser accumulation, Bertrand stability, Drayson detection-prevents-collapse）均已引用。AI 检测文献、序数分类文献、解码策略文献覆盖充分。Schaeffer et al. (2025) "Model Collapse Does Not Mean What You Think" 作为重要的 position paper 也被正确引用。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 方法论创新不足——"标准特征 + 标准分类器"难以独立支撑 EMNLP 发表门槛**
- 具体位置：§3.3–3.4, Table 1
- 问题：论文的方法核心是 19 个手工统计特征（perplexity 的 mean/var/skewness/kurtosis/percentiles、surprisal 统计量、type-token ratio、hapax ratio、bigram entropy、重复 n-gram 分数）+ 200 棵 Random Forest。这些特征在 AI 文本检测文献中已被广泛使用（GLTR, Ghostbuster, DetectGPT 等都使用了 perplexity/surprisal 相关特征）。分类器是最标准的 RF，无超参搜索（§B.29）。论文自我定位为 "benchmark-driven empirical study"（§1 末尾），但即便如此，方法层面的贡献接近于零。
- 为什么影响接收：EMNLP 的 Excitement 维度要求论文提供 "something that is interesting"。纯粹用已知特征在新任务上跑 RF，即使任务定义新颖，也难以在方法层面激发 excitement。Appendix B.9 的 end-to-end PLM baseline（DeBERTa-v3, RoBERTa）表现逊于 RF，但这更可能反映训练数据量/领域匹配问题，而非证明统计特征方法的优越性。
- 建议修改方向：(a) 考虑引入至少一个 learned feature 或 hybrid 方法来提升方法层面的贡献度；(b) 或者更强力地论证为什么 interpretable statistical features 本身是一个设计选择而非局限——目前 §6 Discussion 有所讨论但力度不足；(c) 将论文重新定位为"资源+分析"论文（resource paper track 可能更合适，但 ARR 不区分 track）。

**N2 [critical] Full-replacement 假设严重限制生态效度，Limitations 处理不充分**
- 具体位置：§3.1 "each generation fully replaces the prior training set", Limitations §8 第一段
- 问题：论文的整个实验框架基于 full-replacement chain（每代完全替换上代训练数据）。但现实中的递归污染几乎都是 accumulation 模式（Gerstgrasser et al., 2024）——新合成数据与旧数据/真实数据混合。论文在 Limitations（p.8）仅用一小段提及这一点（"Real-world contamination typically involves partial mixing (accumulation)"），但未提供任何 accumulation 设定下的实验。§5.4 的 pilot accumulation 实验（EDD_a5=2 vs EDD_fs=5, 14B cross-ref）只用一句话带过。
- 为什么影响接收：Full-replacement 是最极端、信号最强的设定。如果论文的核心 claim 是"递归深度可从文本统计特征估计"，但这只在人工极端条件下成立，那么论文的实际价值大打折扣。一个 reviewer 完全可以质疑："accumulation 模式下你的方法是否还能工作？"——论文目前无法回答。
- 建议修改方向：至少对一个模型在 accumulation 设定（如 50% real + 50% synthetic per generation）下复现核心实验，报告 EDD 变化。即使结果显著退化，诚实报告也好过回避。

**N3 [critical] 14B 跨规模结果（EDD=0 self-ref）对论文核心叙事构成严重威胁，讨论不充分**
- 具体位置：§5.4, Appendix B.14–B.17
- 问题：14B（Qwen2.5-14B）self-reference 实验显示 EDD=0（即连 d0 vs d1 都无法区分），cross-reference 下 EDD=2。论文将此归因于 "self-reference evaluating Pythia-1.4B yields accuracy to 44.1% ... ~7 pp of the accuracy is attributable to reference-model mismatch rather than scale"。但这个结果意味着：在当前前沿模型规模下，论文提出的方法可能已经失效。§6 Discussion 用一段讨论了 "scale-dependent attenuation"，但语气过于轻描淡写。
- 为什么影响接收：如果方法在 14B 规模就失效（self-ref EDD=0），那么对 70B+/frontier 模型的适用性存疑。论文的实际应用价值（data curation, contamination detection）依赖于方法对当代模型的有效性。
- 建议修改方向：(a) 在 Abstract/Introduction 中更显著地承认规模限制，而非等到 §5.4 才揭示；(b) 讨论是否存在替代的参考模型选择策略能缓解这一问题；(c) 分析 cross-reference 下 EDD=2 的实际含义——这是否意味着跨模型特征比同模型特征更 robust？

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] Cross-strategy transfer 弱（d1-d3 accuracy 45.9%）削弱实用性主张**
- 具体位置：§5.3, Table 6
- 问题：当训练和测试使用不同解码策略时，d1-d3 mean accuracy 仅 45.9%（接近 chance=25%），虽然 two-stage pipeline 恢复了 11.5 pp。这意味着在实际场景中（解码策略未知），方法的细粒度深度估计能力严重下降。
- 建议：更明确地讨论这一限制对 "practical depth estimation" 主张的影响。目前 §5.3 的 framing 过于乐观。

**W2 [warning] "Benchmark-driven empirical study" 定位在 EMNLP 的可接受性**
- 具体位置：§1 末尾 "Following the tradition of benchmark-driven empirical studies in NLP, our contribution centers on task formalization and systematic characterization"
- 问题：EMNLP 确实接受 empirical study 类论文，但通常要求要么有方法创新（哪怕是 simple but effective），要么有 surprising 的发现能改变社区的理解。本文的三个 findings（perplexity tail dominates, decoding > model, signal attenuates）单独看都不 surprising——perplexity 尾部与 AI 检测相关已在 GLTR/DetectGPT 等工作中有所暗示，信号随规模衰减也是直觉上显然的。
- 建议：强化 "为什么这些发现的组合是 surprising" 的论证，或找到更 counter-intuitive 的 nugget 来提升 excitement。

**W3 [warning] 术语不一致：depth "estimation" vs "classification"**
- 具体位置：Title, §1, §3.1
- 问题：标题用 "Estimating"，§3.1 定义为 "ordinal classification problem"，但全文在 "estimation" 和 "classification" 之间反复切换。这不是纯文字问题——"estimation" 暗示连续值预测，"classification" 是离散类别预测，两者在方法论上有本质区别。
- 建议：统一术语。建议在 §3.1 明确声明 "we frame depth estimation as ordinal classification, and use the terms interchangeably throughout" 或选定一个统一使用。

**W4 [warning] Downstream curation PoC（Appendix B.12）力度不足以支撑 §6 的应用主张**
- 具体位置：§6 Discussion "motivating depth-aware curation", Appendix B.12
- 问题：§6 声称深度估计可用于 "depth-aware data curation"，但 B.12 的 PoC 仅在 Pythia-410M 上做了 fine-tuning 实验，3 个 epochs、极小规模，PPL 变化幅度很小（baseline 5.67 vs best d0-only 5.55 = -0.12）。这个实验太 toy 了，不足以支撑一个 real-world curation 应用的 claim。
- 建议：要么扩大 PoC 规模和指标（如下游任务准确率），要么降低 §6 中 curation 主张的强度。

**W5 [warning] Figure 1 的信息密度偏低**
- 具体位置：Figure 1 (p.3)
- 问题：Figure 1 占据了约半页空间，但传达的信息量有限——仅展示了 LoRA fine-tuning 生成链的示意图，这在正文 §3.1–3.2 中已经用文字清晰描述。对于一篇 8 页论文，这块空间可以更有效利用（如展示一个 motivating example：同一段文本在不同深度下的特征变化）。
- 建议：考虑将 Figure 1 缩小或移至附录，腾出空间给更有信息量的可视化。

### 小问题（不影响接收）

**M1 [minor]** §3.2 "5,000 samples per depth per cell (180K samples total)" — 3 models × 3 strategies × 4 depths × 5000 = 180K ✓，但论文未明确说明 d0 的 5000 样本是否在所有 cells 间共享（同一 seed corpus）还是独立采样。

**M2 [minor]** Table 2 (p.6) 的 4-class RF accuracy 报告了 within-distribution 性能，但未报告置信区间或标准差（仅在附录 B.16 的 cross-seed replication 中报告了 CI）。主表应至少包含 5-fold CV 的 std。

**M3 [minor]** §3.5 Theoretical Grounding 的理论推导（tail mass P_k(pp>τ) monotonically decreasing）虽然直觉正确，但论文将其标注为 "theoretical grounding" 略微 overclaim——这更接近于一个 empirical observation 的 post-hoc rationalization，而非独立的理论贡献。

**M4 [minor]** 引用格式：部分引用使用 `\cite` 应改为 `\citet` 或反之，以符合 ACL 风格指南。例如 §2 中 "Kazdan et al. (2025) systematically..." 使用了正确的 `\citet`，但其他位置存在不一致。

**M5 [minor]** Appendix 长度（17 页，B.1–B.29）可能超出部分 reviewer 的阅读意愿。考虑在主文中更明确地标注哪些附录是 "essential" 的。

---

## 4. Questions for Authors

**Q1.** Accumulation 模式下的性能如何？能否对至少一个模型（如 Pythia-1.4B）提供 50% accumulation 设定下的 EDD？

**Q2.** 14B self-reference EDD=0：如果改用更大/更强的参考模型（如 70B）提取特征，EDD 是否能恢复？

**Q3.** 19 个特征中有多少是真正 novel 的？能否明确标注哪些特征是已有检测文献中使用过的、哪些是本文新提出的？

**Q4.** Cross-strategy transfer 的 two-stage pipeline（先分类策略再分类深度）的实际可行性——"策略未知"的现实场景中如何实现第一阶段的策略分类？

**Q5.** Random Forest 的选择是否做过与其他 ordinal classifier（如 CORAL, proportional odds model）的系统比较？Appendix B.5 的 DCOL 实验似乎只在 Pythia-1.4B 上做了，且结论是 "DeBERTa-v3-large exhibited systematic numerical instability"——能否解释原因？

---

## 5. Missing References

引用验证（OpenAlex）总体结果良好：75 条 bib entries 中 63 条在线验证通过，8 条未找到（多为极新预印本或 OpenAlex 收录延迟），4 条 mismatch（主要是作者排序问题，非实质性错误）。

**可能遗漏的相关工作：**

1. **Guo et al. (2025) "Generative AI May Prefer to Present Scientific Uncertainties as Certainties"** — 关于递归生成导致信息失真的实证工作，与论文的动机相关。

2. **Li et al. (2024) "Synthetic Data (Almost) from Scratch"** — 讨论合成数据质量的层次性，与深度估计的动机呼应。

3. **关于 ordinal regression 在 NLP 中的应用**——Kasa et al. (2024) 已被引用，但 Rothe et al. (2018) "Deep ordinal regression" 等更经典的方法论工作可补充。

4. **Membership inference 与 data provenance 交叉领域** — Carlini et al. (2021) "Extracting Training Data from Large Language Models" 可作为 data provenance motivation 的补充引用。

---

## 6. Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计系统、数据量充分、统计分析规范。但 full-replacement 假设限制生态效度，14B 结果对核心 claim 构成威胁，cross-strategy transfer 弱。主要 claims 在受限条件下有充分支撑，但推广性证据不足。 |
| **Excitement** | 2.5/5 | 任务定义有新意，但方法论零创新（标准特征+RF）。三个 findings 单独看均不 surprising。Benchmark 本身有一定价值但不足以单独驱动 excitement。定位为 empirical study 但缺少改变社区认知的 surprising insight。 |
| **Reproducibility** | 4/5 | 实验细节充分（Appendix B.29 列出了超参、硬件、推理成本），特征定义清晰，数据生成流程可复现。承诺释放代码和数据。唯一不确定性是 LoRA fine-tuning 的随机性——B.16 的 cross-seed replication 部分缓解了这一问题。 |

### Overall Assessment

**Overall: 3.0 (Findings)**

**置信度: 4/5** — 我仔细阅读了全文和大部分附录，对 model collapse 和 AI 文本检测领域有较好的了解。

**一句话总结**: 论文提出了一个有价值的新任务（递归深度估计）和有用的度量（EDD），但方法论贡献过弱（标准特征+RF）、核心实验假设过强（full-replacement）、14B 规模下方法已失效（self-ref EDD=0），这三个问题叠加使论文处于 Findings 边缘。

**详细理由**: 任务定义是本文最强的贡献——将 AI 检测从二分类推进到有序深度估计，直接服务于 model collapse 文献的实际需求。EDD 度量设计优雅且实用。但论文在方法层面没有任何创新，完全依赖已有特征和经典分类器。在 1.4B 规模下效果好（EDD=5），但 14B self-reference 就 EDD=0，这严重限制了论文对当代/未来模型的适用性。Full-replacement 假设与现实场景的 gap 未通过实验弥合。Cross-strategy transfer 的弱表现进一步削弱了 practical applicability。作为 Findings 论文，任务定义的新颖性 + benchmark 的系统性 + EDD 度量的价值可能刚好够格，但主会议接收需要方法或发现层面更强的贡献。

---

## 7. Detailed Comments (按 Section)

### §1 Introduction
- 开篇动机清晰，从 model collapse → 二分类检测 → 深度估计的逻辑推进自然。
- "three findings" 的预告结构好，但 Finding 3（signal attenuates with scale）的预告在这里过于轻描淡写——考虑到 14B 结果的严重性，应在 Intro 就给读者足够的预警。
- 末段 "benchmark-driven empirical study" 的定位是诚实的，但也限制了论文的上限。

### §2 Related Work
- 覆盖全面，组织清晰（Model Collapse Theory → AI Text Detection → Membership/Provenance → Adjacent Tasks → Ordinal Classification → Decoding Strategies）。
- Schaeffer et al. (2025) position paper 的处理恰当——引用但不过度强调。
- 建议在 AI Text Detection 部分更明确地讨论本文与 GLTR (Gehrmann et al., 2019) 的关系——两者都使用统计特征，区别主要在任务定义。

### §3 Method
- 问题定义（§3.1）清晰。
- Benchmark 构建（§3.2）的三轴设计合理，但 "restricting to a narrow parameter range isolates the effect of architecture and training data from scale"（§3.2）这一说法值得商榷——1B–1.5B 的窄范围同时也限制了结论的推广性。
- 统计特征（§3.3）的 19 维设计合理但缺乏新意。Table 1 的分类（Perplexity, Surprisal, Lexical diversity, Repetition）清晰。
- EDD 定义（§3.4, Definition 1）优雅。T=0.70 的阈值选择（"acceptable discrimination" in ROC）有依据（Hosmer & Lemeshow, 2000），但对结果的敏感性分析不足——§4.3 shows EDD shifts by at most one level across T∈{0.65, 0.70, 0.80} 但没有系统的 sensitivity table。
- §3.5 Theoretical Grounding 标题过大——内容更接近于 "empirical motivation" 或 "statistical intuition"。

### §4 Depth Degradation Atlas
- §4.1 In-distribution 结果强（Table 2, 66.4%–85.9% 4-class accuracy）。
- §4.2 Feature Consistency 分析扎实（Gini/SHAP/permutation 三重验证）。
- §4.3 EDD 分析是论文最精彩的部分——Figure 3 的 AUC decay curves 直观有力。
- Figure 2 的 feature importance heatmap 信息量高，但字体偏小，建议检查打印可读性。

### §5 Generalization and Robustness
- §5.1 Surface-text ablation 巧妙地排除了 trivial artifacts。
- §5.2 Cross-model transfer（66.4% mean）合理。
- §5.3 Cross-strategy transfer 是论文最弱的环节——45.9% 接近 chance，应更 prominently 讨论其对应用场景的影响。
- §5.4 Cross-scale 结果是论文的 "inconvenient truth"——14B self-ref EDD=0。论文的处理过于 defensive（"~7 pp of the accuracy is attributable to reference-model mismatch rather than scale"），应更直接地承认这是方法的 fundamental limitation。

### §6 Discussion
- 三个讨论点（depth signal concentrates in perplexity tails, strategy > model, signal attenuates）与主文发现对齐。
- 但讨论深度不足——缺乏对 "why does the signal attenuate with scale?" 的深入分析。是因为大模型生成文本更接近人类分布？还是因为 LoRA fine-tuning 对大模型的影响更小？
- Downstream curation 的讨论（末段）过于 speculative。

### §7 Conclusion
- 简洁。正确指出了 accumulation 和 scale 作为 future work。

### §8 Limitations
- 覆盖了 full-replacement vs accumulation 和 scale boundaries——这两个是最重要的。
- 但遗漏了其他重要 limitation：(1) 仅英文文本；(2) 仅 Wikipedia seed corpus；(3) 参考模型依赖（需要 access to a reference model）；(4) 仅 LoRA fine-tuning，其他 fine-tuning 方法（full fine-tuning, prefix tuning）未测试。
- 长度合适（一小段+几个点）。

### 格式合规检查
- **页数**：主文 8 页（p.1–8），Limitations 在 p.8 底部开始 → 合规 ✓
- **匿名**：标题页显示 "Anonymous ACL submission"，全文未发现 de-anonymization 风险 ✓
- **参考文献**：格式基本规范，使用 `natbib`，`\cite`/`\citet`/`\citep` 混合使用基本正确 ✓
- **Ethics Statement**：p.9，覆盖了公共数据使用和潜在风险 ✓

---

## 引用验证细节

- 总计 75 条 bib entries，109 次引用，75 个 unique cited keys
- 0 orphan（bib 中有但未引用），0 missing（引用了但 bib 中无）
- 在线验证：63 verified, 8 not_found (多为极新预印本或 OpenAlex 索引延迟), 4 mismatch (author order)
- Not_found 中包括 mitchell2023_detectgpt (DetectGPT) 和 liu2019_roberta (RoBERTa)——这是 OpenAlex API 的收录问题，非假引用
- 4 条 mismatch 均为 first_author 排序差异（如 alemohammad vs casco-rodriguez），非实质性错误
- **结论：引用体系干净可靠，无假引用风险**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1570 · 2026-05-21T21:39:49.922469+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 141

## Round 141

2 recorded events


### User

_source line 1571 · 2026-05-21T21:39:52.397298+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**，置信度 4/5。

关键问题：
- **[N1 critical]** 方法论零创新（标准特征+RF），Excitement 不足
- **[N2 critical]** Full-replacement 假设限制生态效度，缺少 accumulation 实验
- **[N3 critical]** 14B self-ref EDD=0，方法在当代模型规模下已失效

主要优势在于任务定义的原创性、EDD 度量的设计、系统性的实验覆盖和干净的引用体系。作为 Findings 论文可能刚好够格，但主会议接收需要方法或发现层面更强的贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1572 · 2026-05-21T21:40:04.333453+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审，收齐后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 142

## Round 142

6 recorded events


### User

_source line 1573 · 2026-05-21T21:40:41.779176+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性与实验充分性

## Paper: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints

---

## 1. Summary

本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类问题，构建了 180K 样本的基准数据集（3 模型 × 3 解码策略 × 4 深度），提取 19 个统计特征（困惑度、surprisal、词汇多样性、重复度），使用 Random Forest 进行分类，并提出 Effective Discriminable Depth (EDD) 指标。核心发现：深度信号在困惑度尾部统计量中可量化检测，但跨解码策略和跨模型规模的泛化能力有限。

---

## 2. Strengths

**S1. 问题新颖且有实际意义。** 将 AI 文本检测从二元分类（人 vs. 机器）推进到序数深度估计，与 model collapse 文献的连接清晰且有理论基础。这一 framing 在现有文献中确实是新的（Section 1, 3.1）。

**S2. 基准设计系统性强。** 3×3×4 网格设计变量控制合理，生成流程清晰（Figure 1）：Wikipedia 种子语料 → LoRA 微调 → 采样 → 下一代 LoRA 微调，每个 cell 5000 样本。模型家族覆盖 Pythia-1.4B/OLMo-1B/GPT-2 XL（Section 3.2），解码策略覆盖 nucleus/temperature/top-k（Section 3.2）。

**S3. 可解释性强。** 19 个特征的 pipeline 透明可分析。特征重要性通过三种互补方法验证（Gini, SHAP, permutation importance，Section 4.2, Appendix B.2），结论一致：p50_ppl 和 var_surprisal 是跨所有 cell 的 universal top-2 特征。

**S4. EDD 指标定义合理。** Definition 1（Section 3.4）提供了深度可区分性的操作性度量，阈值敏感性分析（T ∈ {0.65, 0.70, 0.80}）显示 EDD 最多偏移一级（Section 3.4），wild-data 验证（Appendix B.11）进一步支持其稳健性。

**S5. 附录极其详尽。** 17 页附录覆盖 29 个子实验（B.1–B.29），包括特征轨迹、permutation 重要性、参考模型消融、温度鲁棒性、Binoculars 交叉分析、domain bias、end-to-end learning 等。诚实报告了负面结果（如 RoBERTa-DCOL 训练失败，Table 9）。

**S6. 负面结果的诚实报告。** 跨策略迁移 45.9%（Table 6）、14B 跨参考模型下降至 44.1%（Section 5.4）、accumulation 实验 14-15pp 衰减（Section 8）均如实报告，没有回避弱点。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 单一 LoRA 链种子严重限制基准可靠性**
- 具体位置：Section 3.2, Appendix A (Table 7), Appendix B.29
- 问题：整个 180K 基准数据集每个 model×strategy cell 仅使用单一 LoRA 链（seed=42，Table 7）。LoRA 微调具有随机性——不同种子会产生不同的 adapted model 和不同的文本分布。当前设计无法区分：(a) 递归生成在深度 d 的通用统计特性（论文声称测量的）vs. (b) 特定 LoRA 初始化的 idiosyncratic artifacts（混杂因素）。
- Appendix B.12 (Table 26) 的 RF seed robustness（3 个分类器种子，0.06pp std）仅测试分类器随机性，而非生成链随机性。B.22 (Downstream Fine-Tuning Probe) 明确承认 "single seed is insufficient for statistical significance"，但此顾虑同样适用于主基准。
- 为什么影响接收：这是整个实验体系的根基问题。如果主要发现（如"困惑度尾部单调递减"）是特定 LoRA run 的 artifact，论文的核心 contribution 就不成立。
- 建议修改方向：至少对 1-2 个 cell 运行 3 个额外 LoRA 链种子，报告链间方差。如果特征轨迹和分类精度在链间稳定（如 std < 2pp），问题可以缓解。

**N2 [critical] 跨解码策略迁移失败从根本上削弱实用性声明**
- 具体位置：Table 6, Section 5.3, Appendix B.28
- 问题：d1-d3 跨策略迁移平均准确率 45.9%（3-class chance = 33%），仅高于随机约 13pp。即使最佳 cell（nucleus → 其他）也只有 65.4%（Table 6）。两阶段 pipeline（B.28）仅恢复 11.5pp。
- 论文 Discussion（Section 6）将此描述为发现（"decoding strategies induce qualitatively different degradation trajectories"），但这更应被视为方法的根本局限：在实际应用中，生成模型的解码策略通常未知。如果特征指纹是策略依赖的，方法的部署场景极为有限。
- 为什么影响接收：实用性是本文动机的重要部分（Abstract: "yet no method estimates how many such iterations a text has undergone"）。如果在策略未知时方法接近失效，这一动机就被大幅削弱。
- 建议修改方向：(1) 明确限定 claims 的适用范围（"within known decoding strategy"）；(2) 探索策略不变特征（如 depth-dependent 但 strategy-independent 的特征子集）；(3) 或在已知策略的场景下重新定位论文的 practical contribution。

**N3 [critical] 14B 规模实验存在 self-reference 混杂**
- 具体位置：Section 5.4, Appendix B.14-B.15
- 问题：14B 实验（Qwen2.5-14B）使用自身作为参考模型时准确率 85.8%，但使用 Pythia-1.4B 作为参考模型（cross-reference）时骤降至 44.1%——41.7pp 的差距。论文将 ~7pp 归因于"reference-model mismatch"（Section 5.4），但剩余 ~35pp 差距未充分解释。
- 这意味着方法的表观可扩展性依赖于已知并可获取生成模型本身，这在检测场景中是不现实的假设。14B 结果无法与 1-1.5B 结果公平比较，因为它们使用了不同的参考模型设置。
- B.15 (Cross-Boundary Generalization) 的讨论列出了 4 个 confound（self-reference accuracy, cross-reference accuracy, instruction-tuning, vocabulary mismatch），但承认 "it is therefore infeasible to attribute the observed accuracy gap (60-70% vs. 78-85% at 1-1.5B) to any single factor"——这实际上意味着 14B 实验的结论是 inconclusive。
- 为什么影响接收：Section 5.4 的标题 "Preliminary Cross-Scale Observations" 和 "preliminary" 措辞是适当的，但这部分在 Abstract 和 Introduction 中被过度宣传。Abstract 称 EDD_14B = 5（"extending the benchmark to depth d=5"），但这仅在 self-reference 条件下成立。
- 建议修改方向：(1) 使用同族不同规模模型（如 Pythia-6.9B）作为参考来隔离 self-reference 效应；(2) 或将 14B 结果严格限定为 preliminary，从 Abstract 中移除具体数字。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] 未进行多重比较校正**
- 具体位置：Footnote 3 (page 5)
- 问题：脚注明确承认 "Statistical tests are not corrected for multiple comparisons; p-values should be interpreted as exploratory"。然而论文在多处基于未校正 p-value 做出确定性声明（如 Section 4.3 "bootstrap testing: AUC < 0.70, p < 0.001"，Section 5.1 "Binoculars 11-feat: p > 0.05"）。以 9 cells × 3 depth pairs × 多个条件计算，总测试数达 100+ 量级，多重测试负担显著。
- 建议：对关键结论涉及的测试应用 Bonferroni 或 Benjamini-Hochberg 校正，至少在主表中标注校正后的 significance level。

**W2 [warning] 累积场景（accumulation）严重不足**
- 具体位置：Section 8 (Limitations), Section 6 (Discussion)
- 问题：现实世界的数据污染是累积式的（合成数据与人类数据混合，比例未知），而非论文假设的完全替换（full-replacement）。论文仅有 "pilot accumulation experiments show 14-15pp attenuation"（Section 8），Appendix B.28 中 "conditional decomposition" 有初步讨论但未提供完整实验。
- 既然 accumulation 是实际场景，仅作为 limitations 一笔带过不够充分。建议至少提供一组系统的 accumulation 实验（如混合比例 25/50/75% 人类数据）。

**W3 [warning] 神经网络 baseline 对比可能不公平**
- 具体位置：Section 5.1, Table 4, Appendix B.9 (Table 9)
- 问题：仅使用 base-size PLMs（DeBERTa-v3-base ~184M, RoBERTa-base ~125M），未尝试 large 或 XL 变体。RoBERTa-DCOL 训练完全失败（Table 9: OOM for DeBERTa FT at m_b=10^-2, NaN gradients for RoBERTa LoRA），暗示实现问题而非方法本质限制。Feature-based 与 end-to-end 的差距仅 2pp (B.8)，larger PLMs 可能抹平此差距。
- 建议：至少尝试 DeBERTa-v3-large（~304M）或报告为什么 base-size 是公平比较。

**W4 [warning] Binoculars 达到统计等价需要更充分讨论**
- 具体位置：Table 4, Appendix B.26
- 问题：Binoculars 用 11 个特征 calibrate 后达到 78.1%（permutation test p > 0.05 vs. 19-feature RF 78.4%）。在 in-distribution 下，一个更简单的预有方法达到相同精度，这对 19 特征 pipeline 的 marginal contribution 构成质疑。
- B.26 讨论了 cross-scale 下 Binoculars 退化，但 in-distribution 等价性应在主文中更显著讨论，而非仅在附录中处理。

**W5 [warning] 参考模型依赖性未充分讨论为部署限制**
- 具体位置：Section 3.3, Appendix B.13
- 问题：方法依赖固定参考模型（Pythia-1.4B）提取特征。B.13 显示切换参考模型架构会导致 4-11pp 精度下降，B.15 显示跨规模参考模型差距更大。这意味着部署时需要选择合适的参考模型，但论文未提供选择指南。
- 建议：增加关于参考模型选择的实用指导或分析。

### 小问题（不影响接收）

**M1 [minor] 特征多重共线性。** VIF>10 的特征占 14-16/19（Section 4.2），实际独立维度约 4-5 个。建议在主文中更明确地说明"19 features effectively span ~4-5 independent dimensions"。

**M2 [minor] RF 无超参搜索。** Appendix B.29 确认 "without hyperparameter search"，200 trees 为默认值。虽然 RF 对超参相对鲁棒，但与同样未调参的 neural baselines 对比时仍引入不确定性。

**M3 [minor] 生成长度固定 512 tokens。** B.18 显示从 128 tokens 起精度单调递增。实际文本长度差异很大，512-token 假设的适用范围应更明确界定。

**M4 [minor] 引用小问题。** 引用验证显示：75 条引用全部使用、无孤立条目、无缺失引用。8 条未在 OpenAlex 找到（多为 2025-2026 年 arXiv preprints，正常）。4 条 author 顺序 mismatch（alemohammad2024_mad, guo2024_biscope, hosmer2000, llama3）——均为 API 排序差异而非真正错误。整体引用质量高。

---

## 4. Questions for Authors

**Q1.** 是否对至少一个 cell 运行过额外的 LoRA 链种子？即使只有 2-3 个额外种子的结果也能大幅缓解 N1 的顾虑。

**Q2.** 14B 实验能否使用同族不同规模模型（如 Pythia-6.9B 或 OLMo-7B）作为参考模型，以分离 self-reference advantage 与 scale effect？

**Q3.** Binoculars 在 in-distribution 下统计等价（Table 4），那么在什么具体场景下 19-feature pipeline 优于 Binoculars？主文应更明确回答这个问题。

**Q4.** 为什么不进行多重比较校正？以 100+ 测试量级，部分显著结果可能是虚假的。

**Q5.** 跨策略迁移很弱（45.9%）。是否探索过策略不变特征（如仅使用 surprisal 统计量而非完整困惑度分布）？

**Q6.** accumulation 场景能否提供超越 "pilot" 的系统性结果？即使单一控制良好的 accumulation 链（如 25/50/75% 人类数据混合比例）也会大幅增强论文。

---

## 5. Missing References

引用覆盖全面。可能相关但未引用的方向：
- LoRA rank/configuration 对生成文本分布的影响研究
- 深度特征的序数分类方法（CORAL/CLOC 之外）
- LLM 自评估和自检测能力的文献

---

## 6. Overall Assessment

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 问题新颖、方法透明、分析详尽，但单种子链的基准可靠性、跨策略迁移失败、14B self-reference 混杂这三个方法论问题共同阻止了 Conference 推荐。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法合理但单种子链、无多重比较校正、self-reference confound 削弱统计有效性 |
| Excitement | 3.5/5 | 问题 framing 新颖且有清晰实际动机；跨策略/跨规模泛化弱点压制了 excitement |
| Overall | 3/5 | Findings 水平：novel framing + 详尽的 in-distribution 刻画值得发表，但实验缺口阻止 Conference |
| Reproducibility | 3/5 | 超参报告完整（Table 7, B.29），但代码数据仅承诺 accept 后释放 |
| Confidence | 4/5 | 仔细阅读全部 25 页；熟悉 model collapse 和 AI text detection 文献 |

---

## 7. Detailed Comments (by section)

**Abstract & Introduction:** 对 14B 结果的宣传应更谨慎。Abstract 提到 EDD_14B=5 但未注明仅限 self-reference 条件。建议加 caveat。

**Section 3.2 (Benchmark Construction):** LoRA 链的种子数应明确声明（当前仅在 Table 7 的 seed=42 和 Appendix B.29 的 "3×3×1 generation matrix" 中隐含提及）。建议在主文中显式声明"each cell uses a single LoRA chain"并讨论其影响。

**Section 3.3 (Feature Design):** 19 个特征的选择有理论和实证支持。但 VIF>10 下的多重共线性应在此处而非仅在 4.2 中提及。

**Section 3.4 (EDD):** 定义清晰，阈值敏感性分析恰当。T=0.70 的 Hosmer & Lemeshow (2000) 引用是合理的 external justification。

**Section 3.5 (Theoretical Grounding):** 理论直觉（tail mass P_δ 单调递减 → 困惑度尾部是 depth marker）与实验观察一致。但这仅是 motivation level 的推理，不是 formal proof。这是可接受的。

**Section 4 (Atlas):** Table 2 的 4-class 精度和 bootstrap CI 报告清晰。但缺少跨 cell 的精度方差分析——9 个 cell 从 59% 到 85.9% 跨度很大，应讨论什么因素驱动这种差异。

**Section 4.3 (EDD Analysis):** EDD 曲线（Figure 3）有效地可视化了深度可区分性的衰减。bootstrap 95% CI 的使用恰当。

**Section 5.1 (Baselines):** Baseline 覆盖度合理（binary detectors, ordinal, neural, zero-shot LLM），但 neural baselines 仅用 base-size 模型（W3）。

**Section 5.2-5.3 (Transfer):** 跨模型 66.4% 和跨策略 45.9% 的对比鲜明。论文正确地识别了 Pythia self-reference 优势（4-11pp，B.13），但没有提供消除此 confound 后的 clean 跨模型数字。

**Section 5.4 (14B):** "Preliminary" 定位是诚实的，但 Abstract/Introduction 中的呈现不够 preliminary。

**Section 6 (Discussion):** 合理地总结了主要发现。"strategy effect (9.3pp) exceeds the model effect (7.2pp)" 是有价值的观察。

**Section 8 (Limitations):** 坦诚识别了 full-replacement vs. accumulation、scale 限制、参考模型依赖。但 accumulation 应从 limitation 提升到正文的系统性实验。

**Appendix 总评:** 极其详尽（B.1-B.29），几乎所有可预见的 reviewer 问题都被预先分析。这是论文的重要优势。但部分关键信息（如 Table 9 的 DCOL 失败、B.13 的参考模型消融）应在主文中至少简要提及。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1574 · 2026-05-21T21:41:38.763078+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n**审查侧重**: 新颖性、完整性与写作质量\n\n## Strengths\n\nS1. 任务定义的新颖性与实际意义。将 AI 文本检测从二分类推进到有序多分类是有意义的概念跃迁。\nS2. 系统性的实验设计。3×3×4+ 网格设计，180K 样本充分。\nS3. EDD 度量的实用价值。Definition 1 提供可操作的单一数字。\nS4. Depth Degradation Atlas 的分析深度。三重验证（Gini + SHAP + permutation）。\nS5. 充分的消融和对比。附录 17 页 B.1–B.29。\nS6. Related Work 覆盖度良好。\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [critical] 方法论创新不足——\"标准特征 + 标准分类器\"难以独立支撑 EMNLP 发表门槛**\n- 19 个手工统计特征 + 200 棵 RF。特征在 AI 文本检测文献中已被广泛使用（GLTR, Ghostbuster, DetectGPT）。分类器是最标准的 RF。方法层面贡献接近于零。\n- EMNLP Excitement 维度要求 \"something interesting\"。纯粹用已知特征在新任务上跑 RF 难以激发 excitement。\n- DeBERTa-v3/RoBERTa 表现逊于 RF 更可能反映训练数据量/领域匹配问题，而非统计特征方法的优越性。\n\n**N2 [critical] Full-replacement 假设严重限制生态效度，Limitations 处理不充分**\n- 整个实验基于 full-replacement chain。现实中是 accumulation 模式。\n- §8 仅一小段提及，§5.4 pilot accumulation 一句话带过。\n- Full-replacement 是最极端、信号最强的设定，实际价值大打折扣。\n\n**N3 [critical] 14B 跨规模结果（EDD=0 self-ref）对论文核心叙事构成严重威胁**\n- 14B self-reference EDD=0，cross-reference EDD=2。\n- 当前前沿模型规模下方法可能已失效。\n- §6 Discussion 语气过于轻描淡写。\n\n### Should-Fix\n\n**W1 [warning] Cross-strategy transfer 弱（d1-d3 accuracy 45.9%）削弱实用性主张**\n**W2 [warning] \"Benchmark-driven empirical study\" 定位在 EMNLP 的可接受性** — 三个 findings 单独看都不 surprising。\n**W3 [warning] 术语不一致：depth \"estimation\" vs \"classification\"**\n**W4 [warning] Downstream curation PoC（B.12）力度不足以支撑 §6 的应用主张**\n**W5 [warning] Figure 1 信息密度偏低**\n\n### Minor\nM1: d0 5000 样本是否跨 cell 共享未说明\nM2: Table 2 主表未报告 CI/std\nM3: §3.5 \"Theoretical Grounding\" 标题过大\nM4: \\cite/\\citet 不一致\nM5: Appendix 17 页可能超出阅读意愿\n\n## Questions\nQ1. Accumulation 模式下的性能？\nQ2. 14B 改用更大参考模型（如 70B）能否恢复 EDD？\nQ3. 19 个特征中有多少是 novel 的？\nQ4. 两阶段 pipeline 实际可行性？\nQ5. RF vs 其他 ordinal classifier 的系统比较？\n\n## Missing References\n1. Guo et al. (2025) \"Generative AI May Prefer to Present Scientific Uncertainties as Certainties\"\n2. Li et al. (2024) \"Synthetic Data (Almost) from Scratch\"\n3. Rothe et al. (2018) \"Deep ordinal regression\"\n4. Carlini et al. (2021) \"Extracting Training Data from Large Language Models\"\n\n## Overall: 3.0 (Findings), Confidence 4/5\nSoundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n**审查侧重**: 新颖性、完整性与写作质量\n\n## Strengths\n\nS1. 任务定义的新颖性与实际意义。将 AI 文本检测从二分类推进到有序多分类是有意义的概念跃迁。\nS2. 系统性的实验设计。3×3×4+ 网格设计，180K 样本充分。\nS3. EDD 度量的实用价值。Definition 1 提供可操作的单一数字。\nS4. Depth Degradation Atlas 的分析深度。三重验证（Gini + SHAP + permutation）。\nS5. 充分的消融和对比。附录 17 页 B.1–B.29。\nS6. Related Work 覆盖度良好。\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [critical] 方法论创新不足——\"标准特征 + 标准分类器\"难以独立支撑 EMNLP 发表门槛**\n- 19 个手工统计特征 + 200 棵 RF。特征在 AI 文本检测文献中已被广泛使用（GLTR, Ghostbuster, DetectGPT）。分类器是最标准的 RF。方法层面贡献接近于零。\n- EMNLP Excitement 维度要求 \"something interesting\"。纯粹用已知特征在新任务上跑 RF 难以激发 excitement。\n- DeBERTa-v3/RoBERTa 表现逊于 RF 更可能反映训练数据量/领域匹配问题，而非统计特征方法的优越性。\n\n**N2 [critical] Full-replacement 假设严重限制生态效度，Limitations 处理不充分**\n- 整个实验基于 full-replacement chain。现实中是 accumulation 模式。\n- §8 仅一小段提及，§5.4 pilot accumulation 一句话带过。\n- Full-replacement 是最极端、信号最强的设定，实际价值大打折扣。\n\n**N3 [critical] 14B 跨规模结果（EDD=0 self-ref）对论文核心叙事构成严重威胁**\n- 14B self-reference EDD=0，cross-reference EDD=2。\n- 当前前沿模型规模下方法可能已失效。\n- §6 Discussion 语气过于轻描淡写。\n\n### Should-Fix\n\n**W1 [warning] Cross-strategy transfer 弱（d1-d3 accuracy 45.9%）削弱实用性主张**\n**W2 [warning] \"Benchmark-driven empirical study\" 定位在 EMNLP 的可接受性** — 三个 findings 单独看都不 surprising。\n**W3 [warning] 术语不一致：depth \"estimation\" vs \"classification\"**\n**W4 [warning] Downstream curation PoC（B.12）力度不足以支撑 §6 的应用主张**\n**W5 [warning] Figure 1 信息密度偏低**\n\n### Minor\nM1: d0 5000 样本是否跨 cell 共享未说明\nM2: Table 2 主表未报告 CI/std\nM3: §3.5 \"Theoretical Grounding\" 标题过大\nM4: \\cite/\\citet 不一致\nM5: Appendix 17 页可能超出阅读意愿\n\n## Questions\nQ1. Accumulation 模式下的性能？\nQ2. 14B 改用更大参考模型（如 70B）能否恢复 EDD？\nQ3. 19 个特征中有多少是 novel 的？\nQ4. 两阶段 pipeline 实际可行性？\nQ5. RF vs 其他 ordinal classifier 的系统比较？\n\n## Missing References\n1. Guo et al. (2025) \"Generative AI May Prefer to Present Scientific Uncertainties as Certainties\"\n2. Li et al. (2024) \"Synthetic Data (Almost) from Scratch\"\n3. Rothe et al. (2018) \"Deep ordinal regression\"\n4. Carlini et al. (2021) \"Extracting Training Data from Large Language Models\"\n\n## Overall: 3.0 (Findings), Confidence 4/5\nSoundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1575 · 2026-05-21T21:42:08.918014+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30154
}
```

</details>

---


### Tool call

_source line 1576 · 2026-05-21T21:42:09.119863+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "recursive_gen_depth_est",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见\n\n**审查侧重**: 方法严谨性与实验充分性\n\n## Strengths\n\nS1. 问题新颖且有实际意义。\nS2. 基准设计系统性强。3×3×4 网格，每 cell 5000 样本。\nS3. 可解释性强。19 特征 pipeline 透明，三种 importance 方法一致。\nS4. EDD 指标定义合理。阈值敏感性分析恰当。\nS5. 附录极其详尽。17 页 29 个子实验。\nS6. 负面结果的诚实报告。\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [critical] 单一 LoRA 链种子严重限制基准可靠性**\n- 整个 180K 基准每个 cell 仅用单一 LoRA 链（seed=42）。无法区分递归生成的通用统计特性 vs 特定 LoRA 初始化的 idiosyncratic artifacts。\n- B.12 的 RF seed robustness（0.06pp std）仅测试分类器随机性，非生成链随机性。\n- 如果\"困惑度尾部单调递减\"是特定 LoRA run 的 artifact，核心 contribution 不成立。\n- 建议至少对 1-2 个 cell 运行 3 个额外 LoRA 链种子。\n\n**N2 [critical] 跨解码策略迁移失败从根本上削弱实用性声明**\n- d1-d3 跨策略迁移 45.9%，仅高于 chance 约 13pp。\n- 实际应用中解码策略通常未知，方法部署场景极为有限。\n- 建议限定 claims 适用范围或探索策略不变特征。\n\n**N3 [critical] 14B 规模实验存在 self-reference 混杂**\n- Self-reference 85.8% vs cross-reference 44.1%——41.7pp 差距。\n- ~7pp 归因于 reference-model mismatch，剩余 ~35pp 未充分解释。\n- B.15 承认 \"infeasible to attribute the observed accuracy gap to any single factor\"——结论 inconclusive。\n- Abstract 中 EDD_14B=5 未注明仅限 self-reference。\n\n### Should-Fix\n\n**W1 [warning] 未进行多重比较校正** — Footnote 3 承认，但多处基于未校正 p-value 做确定性声明。100+ 测试量级。\n**W2 [warning] 累积场景严重不足** — 仅 \"pilot\" 级别提及，无系统实验。\n**W3 [warning] 神经网络 baseline 对比可能不公平** — 仅 base-size PLMs（DeBERTa-v3-base ~184M, RoBERTa-base ~125M），未尝试 large/XL。DCOL 训练失败暗示实现问题。\n**W4 [warning] Binoculars 达到统计等价需要更充分讨论** — 11 特征 calibrate 后 78.1% vs 19-feature RF 78.4% (p>0.05)。\n**W5 [warning] 参考模型依赖性未充分讨论为部署限制**\n\n### Minor\nM1: VIF>10 特征 14-16/19，实际独立维度约 4-5\nM2: RF 无超参搜索\nM3: 生成长度固定 512 tokens\nM4: 引用质量高，4 条 author 顺序 mismatch 均为 API 差异\n\n## Questions\nQ1. 是否运行过额外 LoRA 链种子？\nQ2. 14B 能否用同族不同规模模型（Pythia-6.9B）分离 self-ref vs scale？\nQ3. Binoculars in-distribution 等价——19-feature pipeline 在什么场景下优于？\nQ4. 为什么不做多重比较校正？\nQ5. 跨策略迁移弱——是否探索过策略不变特征？\nQ6. Accumulation 能否提供系统性结果？\n\n## Missing References\n- LoRA rank/configuration 对生成文本分布的影响\n- 深度特征的序数分类方法\n- LLM 自评估和自检测文献\n\n## Overall: 3.0 (Findings), Confidence 4/5\nSoundness 3/5, Excitement 3.5/5, Reproducibility 3/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "recursive_gen_depth_est",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见\n\n**审查侧重**: 方法严谨性与实验充分性\n\n## Strengths\n\nS1. 问题新颖且有实际意义。\nS2. 基准设计系统性强。3×3×4 网格，每 cell 5000 样本。\nS3. 可解释性强。19 特征 pipeline 透明，三种 importance 方法一致。\nS4. EDD 指标定义合理。阈值敏感性分析恰当。\nS5. 附录极其详尽。17 页 29 个子实验。\nS6. 负面结果的诚实报告。\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [critical] 单一 LoRA 链种子严重限制基准可靠性**\n- 整个 180K 基准每个 cell 仅用单一 LoRA 链（seed=42）。无法区分递归生成的通用统计特性 vs 特定 LoRA 初始化的 idiosyncratic artifacts。\n- B.12 的 RF seed robustness（0.06pp std）仅测试分类器随机性，非生成链随机性。\n- 如果\"困惑度尾部单调递减\"是特定 LoRA run 的 artifact，核心 contribution 不成立。\n- 建议至少对 1-2 个 cell 运行 3 个额外 LoRA 链种子。\n\n**N2 [critical] 跨解码策略迁移失败从根本上削弱实用性声明**\n- d1-d3 跨策略迁移 45.9%，仅高于 chance 约 13pp。\n- 实际应用中解码策略通常未知，方法部署场景极为有限。\n- 建议限定 claims 适用范围或探索策略不变特征。\n\n**N3 [critical] 14B 规模实验存在 self-reference 混杂**\n- Self-reference 85.8% vs cross-reference 44.1%——41.7pp 差距。\n- ~7pp 归因于 reference-model mismatch，剩余 ~35pp 未充分解释。\n- B.15 承认 \"infeasible to attribute the observed accuracy gap to any single factor\"——结论 inconclusive。\n- Abstract 中 EDD_14B=5 未注明仅限 self-reference。\n\n### Should-Fix\n\n**W1 [warning] 未进行多重比较校正** — Footnote 3 承认，但多处基于未校正 p-value 做确定性声明。100+ 测试量级。\n**W2 [warning] 累积场景严重不足** — 仅 \"pilot\" 级别提及，无系统实验。\n**W3 [warning] 神经网络 baseline 对比可能不公平** — 仅 base-size PLMs（DeBERTa-v3-base ~184M, RoBERTa-base ~125M），未尝试 large/XL。DCOL 训练失败暗示实现问题。\n**W4 [warning] Binoculars 达到统计等价需要更充分讨论** — 11 特征 calibrate 后 78.1% vs 19-feature RF 78.4% (p>0.05)。\n**W5 [warning] 参考模型依赖性未充分讨论为部署限制**\n\n### Minor\nM1: VIF>10 特征 14-16/19，实际独立维度约 4-5\nM2: RF 无超参搜索\nM3: 生成长度固定 512 tokens\nM4: 引用质量高，4 条 author 顺序 mismatch 均为 API 差异\n\n## Questions\nQ1. 是否运行过额外 LoRA 链种子？\nQ2. 14B 能否用同族不同规模模型（Pythia-6.9B）分离 self-ref vs scale？\nQ3. Binoculars in-distribution 等价——19-feature pipeline 在什么场景下优于？\nQ4. 为什么不做多重比较校正？\nQ5. 跨策略迁移弱——是否探索过策略不变特征？\nQ6. Accumulation 能否提供系统性结果？\n\n## Missing References\n- LoRA rank/configuration 对生成文本分布的影响\n- 深度特征的序数分类方法\n- LLM 自评估和自检测文献\n\n## Overall: 3.0 (Findings), Confidence 4/5\nSoundness 3/5, Excitement 3.5/5, Reproducibility 3/5"
  }
}
```

</details>

---


### Tool result

_source line 1577 · 2026-05-21T21:42:10.431529+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1311
}
```

</details>

---


### Assistant

_source line 1578 · 2026-05-21T21:42:15.542805+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 143

## Round 143

2 recorded events


### User

_source line 1579 · 2026-05-21T21:42:18.050608+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：给出 Overall 3.0 (Findings)，Confidence 4/5。识别了 3 个 critical 问题：

1. **单种子 LoRA 链** — 180K 基准每个 cell 仅一条随机链，无法区分递归生成的通用特性 vs. 特定 LoRA 初始化的 artifact
2. **跨策略迁移失败** — d1-d3 仅 45.9%（chance 33%），在策略未知的实际场景下方法接近失效
3. **14B self-reference 混杂** — 自参考 85.8% vs. 跨参考 44.1%，41.7pp 差距使 scaling 结论 inconclusive

另有 5 个 warning（无多重比较校正、accumulation 不足、neural baseline 可能不公平、Binoculars 统计等价、参考模型依赖）和 4 个 minor。问题新颖性和分析详尽度支持 Findings 发表，但实验缺口阻止 Conference 推荐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1580 · 2026-05-21T21:42:26.115146+00:00_

交叉分享已发送，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 144

## Round 144

2 recorded events


### User

_source line 1581 · 2026-05-21T21:44:35.785093+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的交叉回应

---

## Must-Fix 问题

**[REBUT] R1-N1: 单一 LoRA 链种子严重限制基准可靠性**

R1 声称"整个 180K 基准每个 cell 仅用单一 LoRA 链（seed=42）"，但这与论文内容不完全一致。Appendix B.16（Table 21, p.20）明确报告了 cross-seed replication：seed=42（主基准）和 seed=43（独立复现），涵盖全部 3 个模型族。结果显示 seed=43 在所有模型上准确率变化在 +0.14 到 +3.17 pp 之间，CI 重叠，"consistent with noise"。因此 R1 关于"无法区分通用统计特性 vs 特定 LoRA 初始化 artifacts"的担忧已被部分缓解。

但我同意 2 个种子仍然有限。核心问题不在于是否为 artifact（B.16 的复现结果高度一致，suggest 不是），而在于统计功效：仅 2 个种子无法对生成链方差做可靠估计。建议 authors 增加到至少 3-5 个种子，但不应将此定为 critical——当前证据已初步排除 idiosyncratic artifact 的可能性。

**严重程度修正建议：从 critical 降为 warning。**

---

**[AGREE] R1-N2: 跨解码策略迁移失败从根本上削弱实用性声明**

完全同意。d1-d3 跨策略迁移 45.9%（Table 6, §5.3）接近 chance（25%），我在自己的审稿中也将此列为 W1 [warning]。R1 将其升级为 critical 有一定道理——论文在 Introduction 和 Discussion 中多处暗示方法可用于 practical depth estimation，但解码策略未知时方法几乎失效。

补充发现：§5.3 提到的 two-stage pipeline 恢复了 11.5 pp，但最终 d1-d3 accuracy 仍仅约 57.4%，远未达到实用水平。论文需要更明确地将 claims 限定为"解码策略已知或可推断"的场景。

---

**[AGREE] R1-N3: 14B 规模实验存在 self-reference 混杂**

同意核心观点。我在 N3 中也将此列为 critical。41.7pp 的 self-ref vs cross-ref 差距（85.8% vs 44.1%）确实存在严重混杂。

但需要纠正 R1 的一个事实错误：R1 称"Abstract 中 EDD_14B=5 未注明仅限 self-reference"——据我阅读，Abstract 报告的是 EDD_{1.5B}=5（1-1.5B 参数规模）和 EDD_{14B}=2（14B cross-reference 条件下），并非 EDD_14B=5。§5.4 明确区分了 self-ref（EDD=0）和 cross-ref（EDD=2）。因此 R1 对 Abstract 的具体指控不成立，但 14B self-ref EDD=0 这个结果确实对论文叙事构成威胁——这点 R1 和我的判断一致。

R1 关于"~7pp 归因于 reference-model mismatch，剩余 ~35pp 未充分解释"的分析精准。B.15 承认无法归因于单一因素，这诚实但不够——readers 需要对这个 gap 有更清晰的理解。

---

## Should-Fix 问题

**[AGREE] R1-W1: 未进行多重比较校正**

同意。Footnote 3（§3.5）明确承认"exploratory" p-values 未做校正，但主文多处基于这些 p-values 做确定性声明（如 §3.5 "monotonicity in depth is confirmed"、§4.2 "p<0.001"）。100+ 统计测试的量级下，Bonferroni 或 FDR 校正是标准做法。这不会改变核心结论（效应量足够大），但 scholarly rigor 要求至少做 sensitivity check。

---

**[AGREE] R1-W2: 累积场景严重不足**

强烈同意。我在自己的审稿中将此列为 N2 [critical]——比 R1 的 warning 更高。Full-replacement 是最极端设定，现实中几乎不存在。论文仅在 §5.4 用一句话提到 pilot accumulation 结果（EDD_a5=2），没有系统实验。这是论文生态效度的最大缺口。

---

**[REBUT] R1-W3: 神经网络 baseline 对比可能不公平**

部分不同意。R1 批评论文仅用 base-size PLMs（DeBERTa-v3-base ~184M, RoBERTa-base ~125M），但 Appendix B.5（Table 9, p.14）报告了 DeBERTa-v3-large 在 DCOL 框架下的实验——结果是"systematic numerical instability"导致训练失败（"Embed collapse" 和 "NaN gradients"）。这说明 authors 尝试了 large 但遇到了技术障碍，而非故意回避。

更重要的是，B.9（p.15）的 end-to-end PLM 实验不应被简单解读为"RF 优于 neural"。RF 使用 reference-model 提取的 perplexity 特征（需要 access to reference model），而 PLM baselines 直接从文本出发——两者的信息 access 不同。论文在 B.9 最后也承认 "the 20pp accuracy gap between feature-based and end-to-end methods stems from complementarity, not redundancy"。

但 R1 的核心建议仍有价值：至少应尝试 DeBERTa-v3-large 的标准 fine-tuning（非 DCOL），排除 DCOL 框架本身的问题。

---

**[AGREE] R1-W4: Binoculars 达到统计等价需要更充分讨论**

同意。§5.1（p.7）报告 Binoculars 11-feature calibrated 达到 78.1% vs 19-feature RF 78.4%（p>0.05）——这对论文的 19-feature pipeline 的独立价值构成挑战。如果一个已有的检测方法在 calibration 后就能达到等价性能，那么论文的特征工程贡献被削弱。

但需要注意一个 nuance：Binoculars 需要 observer+performer 两个模型（计算成本更高），而 19-feature RF 仅需单一 reference model 的 forward pass。论文未讨论这一计算效率差异，建议补充。

---

**[AGREE] R1-W5: 参考模型依赖性未充分讨论为部署限制**

同意。论文的整个 pipeline 依赖 access to a reference model（Pythia-1.4B）来提取 perplexity 特征。这在实际部署中是一个非 trivial 的约束——用户需要知道（或猜测）生成文本所用的模型族，才能选择合适的 reference model。§5.2 的 cross-model transfer（66.4%）和 B.13 的 reference model ablation 部分回应了这个问题，但 Limitations 未将其列为独立限制。

---

## Minor 问题

**[AGREE] R1-M1: VIF>10 特征 14-16/19，实际独立维度约 4-5**

同意。§4.2 报告 "effective dimensionality ~4-5 due to multicollinearity"。19 个特征中只有 4-5 个独立维度，这意味着特征集存在大量冗余。虽然 RF 对多重共线性天然 robust，但报告 "19 features" 的表述可能给读者造成特征空间比实际更丰富的印象。建议在主文中更早地提及这一降维现实。

**[AGREE] R1-M2: RF 无超参搜索** — 同意这是一个 minor 缺陷，但 200 trees 的 RF 通常不太敏感于超参，不影响核心结论。

**[AGREE] R1-M3: 生成长度固定 512 tokens** — 同意这限制了对短文本场景的推广。B.18（p.21）的 passage length ablation 显示 128 tokens 时 accuracy 仅 66.35%（vs 512 tokens 的更高值），建议在 Limitations 中提及。

**[AGREE] R1-M4: 引用质量** — 与我的引用验证结论一致。4 条 author order mismatch 均为 OpenAlex API 差异，非实质性错误。

---

## Questions 回应

**R1-Q1 (额外 LoRA 种子):** 如上 N1 所述，B.16 有 seed=43 的复现，但仅 2 个种子。Authors 应补充更多种子或解释为何 2 个足够。

**R1-Q2 (Pythia-6.9B 分离 self-ref vs scale):** 好建议。Pythia 系列有 6.9B 和 12B 变体，可以在同族内做规模梯度分析，同时保持 self-reference 一致。这将有效解耦 R1-N3 中的混杂因素。

**R1-Q3 (Binoculars 等价场景):** 如 W4 所述，关键差异在于计算成本和部署约束。19-feature pipeline 的优势可能在于：(a) 单模型 forward pass vs Binoculars 双模型；(b) 特征可解释性用于 downstream analysis（如 Atlas）。但论文未讨论这些。

**R1-Q4 (多重比较校正):** 应该做。即使结论不变，scholarly rigor 要求至少报告 FDR-corrected p-values。

**R1-Q5 (策略不变特征):** 这是一个有建设性的方向。Table 1 的特征分类中，repetition features（repeated 2/3/4-gram fractions）可能相对策略不变——但论文未验证。如果能识别出 2-3 个策略不变特征，即使 accuracy 下降，也能大幅提升实用性。

**R1-Q6 (Accumulation 系统性结果):** 与我的 Q1 一致，这是论文最大的实验缺口。

---

## Overall Assessment 比较

R1 和我均给出 **Overall 3.0 (Findings)**，置信度均为 4/5。

主要分歧：
1. **R1-N1 (LoRA 种子)**: R1 评为 critical，我认为应降为 warning——B.16 的 cross-seed replication 虽有限但已初步排除 artifact。
2. **Excitement**: R1 给 3.5/5，我给 2.5/5。我认为方法论零创新（标准特征+RF）是更大的 excitement 限制因素。R1 可能更看重任务定义的新颖性。
3. **Soundness**: R1 给 3/5，我给 3.5/5。我认为在受限条件下（in-distribution, 1-1.5B），实验设计和统计分析的质量是高的。
4. **Accumulation**: 我将此评为 N2 [critical]，R1 仅评为 W2 [warning]。我认为 full-replacement vs accumulation 的生态效度 gap 比 LoRA 种子问题更影响论文的接收决定。

两位 reviewer 的共识点：(1) 跨策略迁移弱是实用性的主要障碍；(2) 14B 结果对叙事有冲击；(3) 方法本身无新意但任务定义有价值；(4) 总体定位为 Findings 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1582 · 2026-05-21T21:44:56.574325+00:00_

收到 Reviewer 2 的交叉回应。等待 Reviewer 1 的交叉回应。

交叉回应中的关键分歧点：
- **R1-N1 (LoRA 种子)**：R2 [REBUT]，认为 B.16 的 seed=43 复现已初步排除 artifact，建议从 critical 降为 warning
- **R1-W3 (Neural baseline)**：R2 部分 [REBUT]，指出 DeBERTa-v3-large 已尝试但训练失败，非故意回避
- **Accumulation 严重程度**：R2 认为应高于 R1 的 warning，列为 critical

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 145

## Round 145

4 recorded events


### User

_source line 1583 · 2026-05-21T21:44:59.047690+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

要点总结：
- R1 的 6 个 weakness 中，我同意 4 个（N2 跨策略迁移、N3 14B 混杂、W1 多重比较、W2 累积场景），部分反驳 2 个（N1 LoRA 种子——B.16 已有 cross-seed replication，建议降级为 warning；W3 neural baseline——authors 尝试了 large 但遇到技术障碍）
- 两位 reviewer 在 Overall 3.0 (Findings) 上达成共识
- 主要分歧在 Excitement（我给 2.5 vs R1 给 3.5）和 accumulation 的严重程度（我评 critical vs R1 评 warning）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-21T21:45:05.038833+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1585 · 2026-05-21T21:45:05.089525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1586 · 2026-05-21T21:45:06.882588+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 146

## Round 146

10 recorded events


### User

_source line 1587 · 2026-05-21T21:47:41.708131+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## 自纠声明

在回应前，我需要纠正我自己 Round 1 审稿中的一个事实错误：

我的 N3 写道 "14B self-reference yields 85.8%"——**这是错误的**。经核实，Section 5.4 明确报告 14B self-reference 准确率为 **50.8%（2× chance）, EDD=0**，cross-reference 为 **44.1%, EDD=2**。Abstract 也正确报告了 "EDD_{14B} = 0→2"。我原文中的 85.8% 可能混淆了其他表格中的数字。R2 对 14B 数据的引用完全准确。这使我 N3 中描述的问题实际上比我原先表述的更为严重。

---

## Weaknesses 逐条回应

### Must-Fix

**[AGREE] R2-N1: 方法论创新不足——"标准特征 + 标准分类器"**

同意 R2 的事实判断：19 个特征中没有一个是本文首创的。困惑度统计量见于 GLTR (Gehrmann et al., 2019)、DetectGPT (Mitchell et al., 2023)；surprisal 和词汇多样性在 Ghostbuster (Verma et al., 2024) 中已有使用；RF 是最标准的集成分类器，且本文未做超参搜索（Appendix B.29）。

**补充观点**：本文的核心贡献并非方法论，而是 **(1)** 问题定义（ordinal depth estimation vs. binary detection），**(2)** EDD 指标（Definition 1, Section 3.4），**(3)** 系统性的实证 atlas。这类"已知工具 + 新任务"的工作在 EMNLP 是可接受的（如 RAID benchmark, SemEval shared tasks 均以任务定义和实证刻画为主要贡献），但 R2 对 Excitement 2.5/5 的评分有其合理性——方法层面确实缺乏 surprise。

关键问题在于：论文是否应更明确地将自身定位为 **empirical study / benchmark paper** 而非方法贡献？当前写法（"a lightweight pipeline"）可能误导读者期待方法创新。

---

**[AGREE] R2-N2: Full-replacement 假设严重限制生态效度**

完全同意。我在自己的审稿中将此列为 W2 (warning)，现在认为 R2 将其升级为 critical 是合理的。理由：

1. Section 8 (Limitations) 关于 full-replacement vs. accumulation 仅用一小段处理，措辞为 "pilot accumulation experiments show 14-15pp attenuation"——这个衰减幅度本身就很大（接近从 Findings 级下降到 borderline Findings）。
2. Gerstgrasser et al. (2024)——论文自己引用的工作——已明确论证 accumulation 和 full-replacement 的统计行为根本不同。
3. 在 full-replacement（信号最强的设定）下跨策略迁移已降至 45.9%（Table 6），在 accumulation（信号更弱的设定）下性能只会更差。

R2 正确指出这不仅是 limitation，而是对论文实际价值的根本性质疑。

---

**[AGREE] R2-N3: 14B self-reference EDD=0 对核心叙事构成严重威胁**

经核实论文数据，完全同意 R2 的评估。具体证据：

- **Section 5.4**（主文 p.8）：self-reference 准确率仅 50.8%（2× chance），EDD_{14B} = 0
- **Table 17**（Appendix B.14, p.17）：across 所有三种解码策略，d0/d1 AUC = 0.56-0.64，均低于 T=0.70 阈值
- **Appendix B.14 (4)**（p.18）："EDD_{14B} = 0 across all three strategies because the d0/d1 boundary falls below the 0.70 AUC threshold in every case (0.56-0.64)"

这意味着在 14B 规模下，方法**连最基本的 d0（人类） vs. d1（首代生成）都无法区分**。这是比我 Round 1 评估更严重的问题：
- 14B 已不是前沿规模（GPT-4/Claude 等远超此量级），EDD=0 暗示方法可能在更大模型上彻底失效
- d0-d1 是实际应用中最重要的区分（"这段文字是否经历过至少一次递归生成？"）
- 即使在最有利条件下（self-reference = 已知且可获取生成模型），方法仍然失败

**R2 关于 §6 Discussion "语气过于轻描淡写"的批评是精准的**。Section 5.4 使用 "Preliminary" 作为标题是适当的谨慎，但 Discussion 未将 EDD=0 的含义充分展开。特别是，论文没有讨论：随着模型规模继续增长，方法的有效边界在哪里？是否存在某个参数量阈值使统计指纹方法根本不可行？

**比我 Round 1 的评估更严重**：我之前错误地认为 self-reference 达到 85.8%（实为 50.8%），因此低估了这个问题的严重性。我现在将此从 "N3 confound issue" 升级为与 R2 一致的"对核心叙事的严重威胁"。

---

### Should-Fix

**[AGREE] R2-W1: Cross-strategy transfer 弱（45.9%）削弱实用性**

完全同意，与我自己的 N2 一致。我甚至将此列为 critical 而非 warning，因为论文动机的重要部分是实用性（Abstract: "yet no method estimates how many such iterations a text has undergone"）。

---

**[REBUT] R2-W2: "Benchmark-driven empirical study" 定位在 EMNLP 的可接受性**

不同意"三个 findings 单独看都不 surprising"的判断。至少以下两个发现是 non-trivial 且在先验预测中不确定的：

1. **策略效应 > 模型效应**（Section 6: strategy effect 9.3pp vs. model effect 7.2pp）——在 model collapse 文献中，大部分工作聚焦于模型/数据规模，解码策略的影响被严重低估。本文是首个量化两者相对贡献的工作。
2. **Cross-reference 提升 EDD**（Section 5.4: EDD 从 0→2 when switching from self-ref to cross-ref at 14B）——这是反直觉的：使用"错误"的参考模型反而改善了深度可区分性，尽管降低了总体精度。这揭示了自参考偏差，具有诊断价值。

此外，EMNLP/ACL 历来接受高质量 benchmark 和 empirical study 类论文（如 RAID (Dugan et al., 2024), MAGE (Li et al., 2024)），前提是任务定义有价值且实验充分。R2 对 Excitement 的低评分可以理解，但将 benchmark study 本身视为 positioning 问题值得商榷。

---

**[AGREE] R2-W3: 术语不一致 "estimation" vs "classification"**

有效的写作问题。论文在 title/abstract 中使用 "estimation"（暗示连续值或回归），在 Section 3.1 中明确定义为 "ordinal classification problem"，后续交替使用两个术语。建议统一为 "ordinal classification" 并在首次出现时解释为什么用 "estimation" 作为通俗表述。

---

**[AGREE] R2-W4: Downstream curation PoC（B.22）力度不足**

同意。Appendix B.22 的 fine-tuning probe 使用单一种子、小规模（Pythia-410M, LoRA, r=16, n=32），结果也承认 "single seed is insufficient"。PPL 变化仅 0.03-0.12，统计不显著（Table 15）。如果论文要在 Discussion 中声称深度估计可用于 downstream curation（§6），需要更有力的 PoC。

---

**[REBUT] R2-W5: Figure 1 信息密度偏低**

不同意。Figure 1 的目的是定义 task setup（recursive generation chain），而非展示数据。它清晰地展示了：(1) seed corpus D_0 → LoRA ft → sampling 的递归链，(2) binary vs. ordinal estimation 的区别，(3) 深度 d 的定义。对于一个全新的任务定义论文，这种清晰的 setup 图是必要的。如果要提高信息密度，可以考虑将 Table 1 的特征分类整合进来，但这不是 must-fix。

---

### Minor

**[AGREE] R2-M1**: d0 样本是否跨 cell 共享确实未在主文中显式声明。从实验设计推断，d0 应为同一 Wikipedia seed corpus，但这应明确说明。

**[AGREE] R2-M2**: Table 2 主表确实未报告 CI/std。CI 仅在文字中零散提及（如 "bootstrap 95% CI"）。主表应统一报告。

**[AGREE] R2-M3**: §3.5 "Theoretical Grounding" 标题确实过大。内容是 motivation-level 的直觉推理（tail mass P_δ 单调递减），不是 formal theorem。建议改为 "Theoretical Motivation" 或 "Intuitive Grounding"。

**[AGREE] R2-M4**: \cite/\citet 不一致是排版细节但应修复。

**[REBUT] R2-M5**: 附录 17 页是论文的重要优势而非劣势。几乎所有可预见的 reviewer 问题（参考模型消融、温度鲁棒性、Binoculars 交叉分析、domain bias 等）都在附录中被预先分析。Reviewer 不需要读完所有附录，但其存在证明了实验的 thoroughness。

---

## Questions 逐条回应

**[AGREE] R2-Q1 (Accumulation 性能)**: 与我的 Q6 一致，这是论文最大的实验缺口。至少需要一组系统的混合比例实验。

**[AGREE] R2-Q2 (14B 用更大参考模型)**: 好问题。但考虑到 cross-reference 已将 EDD 从 0 提升到 2（Section 5.4），更大参考模型可能进一步改善 EDD。不过这也引入了实际部署的可行性问题——需要一个大参考模型来检测另一个大模型的递归深度。

**[AGREE] R2-Q3 (19 特征的 novelty)**: 坦率地说，几乎没有单个特征是 novel 的。p50_ppl、var_surprisal 等都是标准统计量。Novelty 在于将它们**组合应用于深度估计任务**，以及通过系统消融确定了 universal top features。

**[REBUT] R2-Q4 (两阶段 pipeline 可行性)**: Appendix B.28 的两阶段方法（先分策略再分深度）在概念上是合理的——在实际部署中，先判断解码策略类型再做深度分类是可行的工作流。但 R2 的质疑也有道理：策略分类本身的准确率没有报告，end-to-end 性能不确定。

**[REBUT] R2-Q5 (RF vs 其他 ordinal classifiers)**: 论文确实比较了 CORAL 和 CLOC（Table 4, Appendix B.20, Table 21），以及 Ordinal MLP（B.20）。结果显示 RF baseline 在 leave-one-model-out transfer 下与 CORAL/Ordinal MLP 差异在 1pp 以内（Table 21）。但 R2 的问题是否还包括更广泛的 ordinal classifiers（如 proportional odds model），这确实未覆盖。

---

## Missing References

**R2 建议的 4 篇参考文献**：

1. **Guo et al. (2025) "Generative AI May Prefer to Present Scientific Uncertainties as Certainties"** — 与 model collapse 下的信息扭曲相关，但与深度估计任务的直接关联有限。Nice to have。

2. **Li et al. (2024) "Synthetic Data (Almost) from Scratch"** — 如果涉及合成数据质量与递归生成的关系，可能相关。

3. **Rothe et al. (2018) "Deep ordinal regression"** — 同意，ordinal classification 方法论部分应引用更广泛的 deep ordinal regression 文献，不仅限于 CORAL/CLOC。

4. **Carlini et al. (2021) "Extracting Training Data from Large Language Models"** — 与 membership inference 和数据来源追溯直接相关，确实应引用。**这是最重要的缺失引用。**

---

## 总结：与 R2 的一致性和分歧

### 一致（agree on substance）
- **N1** (方法论创新度低): 事实正确，但论文贡献主要在 task formulation
- **N2** (full-replacement 局限): 完全同意
- **N3** (14B EDD=0): 完全同意，且比我 Round 1 的评估更严重（我之前用了错误的数字）
- **W1** (cross-strategy weak): 完全同意
- **W3** (术语不一致): 同意
- **W4** (PoC 不足): 同意
- **M1-M4**: 基本同意

### 分歧
- **W2** (benchmark study 定位): 部分反驳——EMNLP 接受 benchmark 论文，且本文有 non-trivial findings
- **W5** (Figure 1): 反驳——任务定义图的信息密度是适当的
- **M5** (附录过长): 反驳——详尽的附录是优势
- **Q5** (ordinal classifiers): 部分反驳——论文已比较 CORAL/CLOC/Ordinal MLP

### 对 Overall 评分的看法

R2 给出 3.0 (Findings), Soundness 3.5, Excitement 2.5。我的评分为 3.0 (Findings), Soundness 3.0, Excitement 3.5。

关键分歧在于 Soundness vs. Excitement 的权重：
- R2 认为方法不新颖（Excitement 低）但执行尚可（Soundness 较高）
- 我认为任务新颖（Excitement 较高）但实验有 gap（Soundness 较低）

**在确认 14B EDD=0 的事实后，我倾向于将 Soundness 也调低至 2.5-3.0**，因为方法在当前模型规模下已接近失效。综合来看，我维持 **Overall 3.0 (Findings)** 的评分，但置信度从 4 提升到 4.5——两位 reviewer 独立达到相同分数增强了判断的可信度。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1588 · 2026-05-21T21:48:14.866971+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-21T21:48:14.917863+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T21:31:59.638268+00:00\", \"completed_at\": \"2026-05-21T21:35:20.730820+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续两页纯文本（Introduction + Related Work），无任何 figure/table/equation display item。审稿人打开论文后前两页完全没有视觉锚点，第一印象偏 text-heavy。建议：考虑将 Figure 1（当前 page 3 顶部）提前到 page 2 顶部，或在 Introduction 末尾加一个 teaser figure/概览表\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"极度拥挤——单页塞入 4 个 display items（Table 4, Figure 4, Table 5, Table 6）加上 Section 5.2/5.3/5.4/6 四个章节。审稿人阅读体验拥挤，Discussion 起始位置被挤到页面底部角落。建议：将 Table 5 或 Table 6 之一移入 Appendix，或将 Section 6 移至 page 9（利用 Limitations/Ethics 前的空间重排）\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 2（特征重要性热力图）内部文字（feature 名称、axis labels）偏小，在 150 dpi 渲染下已需要仔细辨认，打印或缩放阅读时可读性受影响。建议：增大 feature name 字号，或改用精简的 feature 缩写 + 独立图例\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4（三个混淆矩阵并排）尺寸偏小，单元格内数字需要凑近看。若无法增大图幅，考虑将此图移至 Appendix 并在正文用文字描述关键 pattern\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 的三条线主要依赖颜色区分（blue/orange/green），未使用不同 line style 或 marker shape。灰度打印或色盲读者可能难以区分。建议：添加 dashed/dotted line style 或不同 marker（circle/square/triangle）\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 caption 自包含度良好（解释了 pipeline、任务定义、binary vs ordinal）。配色方案（蓝/青绿）专业清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Tables 2 和 3 使用 booktabs 风格（toprule/midrule/bottomrule），无竖线，格式规范。最优值有加粗标注\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 排版整洁，四个 category 分组清晰。位于 Section 3.3 首次引用附近，float 位置合理\"}, {\"severity\": \"info\", \"dimension\": \"page 9-12\", \"message\": \"References 格式统一，未发现 [?] 未解析引用或明显格式不一致。排版正常无溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 13-25\", \"message\": \"Appendix 非常详尽（13 页），包含 Tables 7–30+ 和 Figure 
…[truncated 149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1590 · 2026-05-21T21:48:14.918614+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1591 · 2026-05-21T21:48:14.919130+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---
