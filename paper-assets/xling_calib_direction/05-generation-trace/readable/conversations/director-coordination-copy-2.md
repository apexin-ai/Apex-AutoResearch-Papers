# Director coordination

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 116
- **Recorded user turns:** 14
- **Tool calls:** 44
- **Original source:** `logs/chats/feishu_group_oc_03a4b60e63b9658b3528f3d9a729f2e8_director.jsonl`
- **Structured JSON:** [`b6bf347f17b424dd1784.json`](../../sessions/b6/b6bf347f17b424dd1784.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-20T19:51:55.059816+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见（Novelty & Related Work）

**论文标题**: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs

---

## 总体评分
**Overall**: 2.5 / 5（介于 Revise-for-next-cycle 与 Findings 之间）
**一句话总结**: 实验规模值得肯定（20语言×3架构×3基准），但四项贡献的新颖性均为增量性的，且参考文献极度稀疏（仅8篇）、Related Work 不足一页，严重削弱了论文的学术定位。

---

## ACL ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 核心实验设计合理，但"Pareto frontier"术语的技术准确性存疑；decomposition 的 25% variance explained 较低却被作为主要贡献宣传 |
| Excitement | 2 / 5 | 四项贡献均为已知技术的直接扩展或组合，缺乏方法论上的惊喜；实践者收获主要是"选哪个 layer"的经验法则 |
| Reproducibility | 3.5 / 5 | 实验设置描述清楚（§4），超参数有报告（α=0.15, β=0.10），但代码/数据未提及是否公开 |
| Confidence | 4 / 5 | 熟悉 probe-based calibration 和跨语言表征领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 参考文献极度稀疏——全文仅 8 篇引用

- 具体位置：References（p.10），§2 Related Work（p.2）
- 问题：一篇声称覆盖 probe-based calibration、cross-lingual probing、multilingual calibration 三个方向的论文，仅引用 8 篇文献，这在 *ACL 顶会投稿中极不正常。以下关键文献完全缺失：
  - **Cross-lingual probing 基础**: Conneau et al. (2020) "Unsupervised Cross-lingual Representation Learning at Scale"；Pires et al. (2019) "How multilingual is Multilingual BERT?" —— 这两篇是多语言模型 layer-wise probing 的奠基工作，本文的 depth-transferability claim 必须讨论它们
  - **表征相似性**: CKA/SVCCA 文献（Kornblith et al., 2019; Raghu et al., 2017）—— 论文讨论跨语言表征对齐却完全不提表征相似性度量
  - **CCPS** (Wang et al., EMNLP 2025)：通过 perturbation stability 做 calibration probing，直接相关的方法
  - **Probing 综述**: Belinkov (2022) "Probing Classifiers"，该领域的标准参考
  - **多语言 calibration**: Keleg & Magdy (2023) "On the Calibration of Massively Multilingual Language Models"；Adaptive Temperature Scaling (EMNLP 2024)
  - **IRT 文献**: 论文大量使用 IRT difficulty 参数（§3.3），但未引用 IRT 原始文献（e.g., Lord 1980, Baker 2001）
  - Director 指定检查的 **MKA (Chen et al., 2024)** 和 **CCPS (Wang et al., 2024)** 也未出现
- 为什么影响接收：参考文献不足直接导致 (a) 新颖性论证无锚点——无法说明本文与先行工作的区别，(b) reviewer 无法评估作者是否了解领域全貌，(c) 违反 ACL 社区对 scholarly thoroughness 的基本期望
- 建议修改方向：Related Work 扩展至至少 1.5-2 页，引用量应在 30+ 篇

**N2** [critical] "Pareto frontier" 术语使用不准确，核心 framing 有误导性

- 具体位置：Title, Abstract, §3.2, §5.1, Claims 1 & 3
- 问题：在多目标优化中，Pareto frontier 指的是一组互不支配（non-dominated）的解。本文所描述的是 **depth vs. cross-lingual transfer AUROC 的单调递减关系**（deeper = better English, worse transfer）——这是一条 trade-off curve，不是 Pareto frontier。Table 1 和 Table 3 中标记的 ★ 点是"best transfer layer"，但没有证据表明这些层在 (English AUROC, ZS-19 AUROC) 二维空间中互不支配。事实上，Table 1 显示 layer 8 的 EN=0.446 / ZS-19=0.637，而 layer 53 的 EN=0.827 / ZS-19=0.563——layer 8 在 ZS-19 上优于 layer 53，而 layer 53 在 EN 上优于 layer 8，这确实构成 non-dominance。但论文没有做标准的 Pareto dominance 分析，没有报告 hypervolume indicator，甚至没有画一张 scatter plot 来可视化这条 frontier。
- 为什么影响接收：标题和核心 claim 建立在一个技术上不严谨的术语之上。如果只是描述"deeper layers 有更好的 English probe 但更差的 cross-lingual transfer"，这在多语言 NLP 中是已知现象（Pires et al., 2019; Conneau et al., 2020 已表明 deeper layers encode more language-specific features）。"Pareto frontier" framing 给一个已知现象披上了新包装。
- 建议修改方向：(1) 如果坚持 Pareto 术语，需做标准 multi-objective 分析（dominance test, hypervolume, 可视化）；(2) 否则改为"depth-transferability trade-off profile"并明确与 Conneau/Pires 等先行工作的区别

**N3** [critical] 四项贡献的新颖性均为增量性，缺乏方法论突破

- 具体位置：§1 Claims 1-4, §3
- 问题逐条分析：
  - **Claim 1 (Pareto frontier)**: 如 N2 所述，deeper layers = more language-specific 是已知现象。新贡献仅在于"用 correctness probes 而非 syntactic/semantic probes 观察到了同样的现象"。
  - **Claim 2 (Difficulty-capability decomposition)**: Civelli et al. (2025) 已证明 IRT difficulty probes 跨语言迁移。本文的新增是将 variance 分解为 difficulty-shared (68%) 和 capability-specific (32%) 两个成分——但 R² = 0.72（§5.2 第一句 "IRT difficulty probes achieve h² = 0.72"）并未超越 Civelli 的结果，且 25% 的 transfer gap 解释力（Abstract）依赖于这个分解的稳定性，论文未报告 bootstrap confidence interval。
  - **Claim 3 (CaCLR)**: 损失函数 = BCE + calibration penalty (ℓ_cal) + consistency regularization (ℓ_consistency)。BCE 用于 correctness 预测（标准做法）；calibration loss 类似 focal/ECE-based penalties（已有文献）；consistency regularization 广泛用于半监督学习（Temporal Ensembling, MixMatch 等）。三者组合虽合理，但非 non-trivial，缺乏理论分析说明为何组合优于单独使用。
  - **Claim 4 (Orthogonality extension)**: Miao & Ungar (2026) 建立了英文的 correctness-confidence orthogonality。本文将同一分析扩展到 20 种语言，发现 cos < 0.25。方法论上这是直接复制——计算 cosine similarity——无需新方法。贡献仅在 empirical verification。
- 为什么影响接收：四项贡献叠加后，整体 narrative 是"将已知方法应用到更大规模"，这对 Findings track 可能足够，但对 main conference 接收（excitement 维度）不足。
- 建议修改方向：聚焦最有洞察力的发现（如 architecture-dependent depth profile 的 mechanistic 解释），补充理论分析或消融实验说明为什么 CaCLR 各组件的组合是 synergistic 而非 additive。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Related Work（§2）过于简略——仅 ~15 行覆盖 3 个子方向

- 具体位置：§2（p.2，约 15 行正文）
- 问题：三个子方向（Probe-Based Calibration, Cross-Lingual Representation Transfer, Multilingual Calibration）各仅 1-2 句话。与 Xiao et al. (2025) 的区别（"knowledge-boundary vs. correctness probes"）和与 Civelli et al. (2025) 的区别（"difficulty vs. correctness"）各仅一句话带过。这些是论文 novelty 论证的核心支撑，一句话不够。
- 建议：(1) 每个子方向至少 1 段落；(2) 用一个对比表格（method × feature）明确区分本文与 Xiao、Civelli、CORAL 的定位

**W2** [warning] 全文 16 张表格、0 张图——表格过重，可读性差

- 具体位置：Tables 1-16 贯穿全文
- 问题：论文核心概念是"Pareto frontier"，却没有任何可视化。一张 (English AUROC, ZS-19 AUROC) 的 scatter plot with Pareto front overlay 比 Table 1 的 20 行数字直观得多。同样，layer-wise transfer degradation curve、resource-tier gradient、CaCLR ablation 都适合用图表呈现。16 张纯数字表格使得论文难以快速理解核心 pattern。
- 建议：至少添加 (1) Pareto frontier 可视化（scatter plot），(2) layer-wise AUROC 折线图，(3) resource tier vs. improvement 的 bar chart

**W3** [warning] "First systematic study" 声明过强

- 具体位置：Abstract 第 3 行 "We present the first systematic study of cross-lingual correctness probe transfer"
- 问题：Xiao et al. (2025) 做了 cross-lingual knowledge boundary probe transfer（5 languages），Civelli et al. (2025) 做了 cross-lingual difficulty probe transfer。本文的"first"仅成立于"correctness probe"这一细分品类。这种细分声明（"first for correctness, not knowledge-boundary, not difficulty"）在 reviewer 看来更像是通过 narrow scoping 来回避先行工作，而非真正的开创性。
- 建议：改为 "the first large-scale study comparing correctness probe transfer across architectures"——强调 scale 和 architecture comparison 而非"first"

**W4** [warning] Difficulty-capability decomposition 的 25% 解释力未给置信区间

- 具体位置：Abstract "explains 25% of transfer gap", §5.2
- 问题：25% 的 variance explained 是关键数字，但论文未报告 bootstrap CI 或 cross-validation stability。在 20 语言的样本上，这个估计可能有很大方差。此外，72% 的 method choice prediction accuracy（Abstract）未与 random baseline 或 majority class baseline 对比。
- 建议：报告 bootstrap 95% CI；报告 random/majority baseline 对比

**W5** [warning] CaCLR 的 improvement 幅度较小，实际意义不清楚

- 具体位置：§5.3, Table 7
- 问题：CaCLR 的核心结果是 "+1.3pp avg AUROC" 和 "~40% ECE reduction"（Abstract）。但 Table 7 显示 CaCLR 的 AUROC 为 0.804，zero-shot baseline 为 0.762——zero-shot 已经不低。而 few-shot (100) 为 0.779。在实际部署中，25 或 100 个 few-shot 标签的获取成本极低，CaCLR 相比 few-shot 的优势有限。论文未讨论 CaCLR 在什么场景下比简单的 few-shot fine-tuning 更有实际价值。
- 建议：补充 cost-benefit 分析，说明 zero-label 假设在什么实际场景下成立

---

## 小问题（不影响接收）

- §3.4 CaCLR 公式 (1) 中的 α 和 β 说明"tuned on a validation set"但未说明 validation set 的语言组成——如果 validation 含 target language labels 则"zero-label"声明不成立
- §5.5 "Probe Complexity Analysis"（Table 12）仅在 Qwen3-235B 上做，是否 architecture-specific？应在多个架构上验证
- §5.9 INT8 vs FP16 验证（Table 16）仅在 Llama 4 Scout 上做 5% 子集——样本量过小难以得出稳健结论
- References 格式不一致：部分有 venue 信息（Burns et al. → ICLR 2023, Marks et al. → COLM 2024），部分没有（Miao et al. 2026 缺 venue, Civelli et al. 2025 缺 venue）

---

## 主要优势

- **S1**: 实验规模确实比先行工作大——20 语言 × 3 架构 × 3 基准的覆盖度超过 Xiao (5 languages) 和 Civelli 的范围
- **S2**: CaCLR 的 zero-label 设定有实际意义——在 target language 完全无标注数据的场景下提供了一条可行路径
- **S3**: Architecture comparison（Table 4, Table 14）揭示了 MoE vs Dense 的 frontier 形状差异，这在已有文献中未见讨论
- **S4**: Orthogonality 的 resource-tier gradient（Table 10-11）提供了一个有趣的发现：低资源语言的 orthogonality 更弱，暗示模型对低资源语言的 correctness 和 confidence 编码更加纠缠

---

## 给作者的具体问题

1. Table 1 中标记 ★ 的层是否经过标准 Pareto dominance 检验？如果做了，请提供 hypervolume indicator。如果没做，标题中的 "Pareto Frontier" 是否应改为更准确的术语？
2. CaCLR 的 consistency regularization（ℓ_consistency）是否在 English 和 target language 的 parallel data 上计算？如果是，"zero-label"的定义是什么——zero target-language correctness labels 但需要 parallel sentences？
3. §5.2 报告 h² = 0.72 的 difficulty heritability——这个数字与 Civelli et al. (2025) 报告的值相比如何？论文没有引用 Civelli 的具体数字做对比。
4. Orthogonality 分析（§5.4）中 cosine similarity 的计算是在 probe weight vectors 上还是在 representation space 中的 direction vectors 上？Miao & Ungar (2026) 的原始方法是哪种？
5. 论文使用 Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B——三个模型中两个是 MoE。MoE 的 expert routing 是否影响 layer-wise probing 的解释？论文未讨论 MoE 架构中 "layer depth" 的特殊性。

---

**总结**: 这是一篇在规模上有价值的实证研究，但四项贡献的新颖性均为增量性的，"Pareto frontier" framing 技术上不准确，且参考文献（8 篇）和 Related Work 的覆盖度远低于顶会标准。建议：(1) 大幅扩充参考文献和 Related Work，(2) 修正或放弃 Pareto 术语，(3) 添加可视化，(4) 更诚实地定位为 large-scale empirical study 而非方法论贡献。在当前状态下，推荐 Revise-for-next-cycle。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T19:52:09.124136+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T19:52:09.124493+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T19:52:16.851142+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T19:52:16.951999+00:00_

{"result":"# 项目 xling_calib_direction 概况\n\n## 实验状态 (3 个)\n\n- **mvp_002**: DONE (success) — \n- **mvp_001**: DONE (success) — \n- **mvp_003**: RUNNING — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| mvp_003 | Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_002** (failed): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\n\n## 趋势\n成功 1 / 负向 0 / 失败 1 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-13176: 无 GPU 信息\n\n## 告警\n- mvp_002: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T19:52:19.661783+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
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

_source line 7 · 2026-05-20T19:52:19.712331+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T19:52:24.178372+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T19:52:24.230866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T19:52:34.116839+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T19:52:34.619160+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T19:52:34.770007+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T19:52:35.071475+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T19:52:35.272616+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T19:52:35.323234+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/logs/phase1_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/logs/phase2_best_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/logs/phase2_median_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/logs/phase2_worst_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.aux
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.out
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.log
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/logs/paper_agent_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_directio
…[truncated 6031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T19:52:53.490582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T19:52:53.794639+00:00_

1	narrative_guidance: 'Original framing stands: "CaCLR shifts the cross-lingual calibration
2	  Pareto frontier." All 4 claims form an unbroken causal chain — discovery → analysis
3	  → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling
4	  with zero target-language labels. Pareto frontier is the organizing principle, CaCLR
5	  is the actionable contribution, decomposition explains why it works, orthogonality
6	  explains why output-based methods can''t.
7	
8	  '
9	imagined_experiments:
10	- name: Full Pareto Frontier — Qwen3-235B-A22B
11	  plan_id: plan_001
12	  description: 'Extract activations at every 4th layer (24 probed layers out of 94),
13	    20 languages, train English correctness probes (logistic regression + 2-layer
14	    MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection,
15	    few-shot 25/100, CaCLR).
16	
17	    '
18	  expected_results:
19	    en_auroc_best_layer: 0.843
20	    en_best_layer_idx: 72
21	    en_auroc_range:
22	    - 0.621
23	    - 0.843
24	    en_ece_raw_best: 0.162
25	    en_ece_tempcal_best: 0.054
26	    temp_scaling_T: 4.87
27	    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.762
28	    zs_best_transfer_layer_idx: 56
29	    zs_transfer_drop_from_en_mean_pp: 8.1
30	    zs_auroc_by_tier:
31	      high_resource_mean: 0.791
32	      mid_resource_mean: 0.754
33	      low_resource_mean: 0.683
34	    zs_auroc_by_lang:
35	      en: 0.843
36	      zh: 0.802
37	      de: 0.796
38	      fr: 0.793
39	      es: 0.789
40	      ja: 0.785
41	      ru: 0.782
42	      pt: 0.788
43	      it: 0.786
44	      ar: 0.768
45	      hi: 0.761
46	      ko: 0.755
47	      vi: 0.749
48	      th: 0.743
49	      bn: 0.738
50	      tr: 0.756
51	      nl: 0.79
52	      sw: 0.695
53	      yo: 0.672
54	      ig: 0.681
55	    mean_shift_improvement_count: 2
56	    mean_shift_delta_ece_mean: 1.41
57	    linproj_auroc_mean_19lang: 0.724
58	    fewshot_25_auroc_mean_19lang: 0.748
59	    fewshot_100_auroc_me
…[truncated 43606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "elapsed_ms": 304
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T19:53:13.919436+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/agent/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/agent/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T19:53:14.020223+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T19:53:16.630655+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T19:53:16.731599+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/karandikar2021sbece.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/miao2026closing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/civelli2026shared.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/confidence_manifold2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/xiao2025knowledge.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/joshi2025calibration.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/khanmohammadi2025ccps.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/liu2025middle.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/ji2025calibrating.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/ravisankar2026dali.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/zhou2025lace.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/miao2026coral.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/
…[truncated 870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T19:53:21.195575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T19:53:21.346531+00:00_

1	---
2	dream_id: dream_20260520T185641
3	tier: best
4	overall_score: weak accept (4/6)
5	timestamp: 2026-05-20T19:45:50.963360+00:00
6	---
7	
8	# Dream Review Report: Shifting the Cross-Lingual Calibration Pareto Frontier
9	
10	**Paper**: "Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR"
11	**Review mode**: Full (2 Reviewers, 4-step roundtable)
12	**Date**: 2026-05-20
13	
14	---
15	
16	## Panel Summary
17	
18	| Reviewer | Focus | Preliminary | Post-discussion | Confidence |
19	|----------|-------|-------------|-----------------|------------|
20	| R1 | Methods + Experiments | 4 (Weak Accept) | 4 (borderline 3–4) | 4/5 |
21	| R2 | Novelty + Related Work | 4 (Weak Accept) | 4− (borderline) | 4/5 |
22	| **Consensus** | | | **4 (Weak Accept)** | |
23	
24	**Overall assessment**: Weak Accept — addresses a genuine gap with comprehensive experiments, but cumulative methodological and novelty concerns make acceptance contingent on substantive revisions.
25	
26	---
27	
28	## 1. Paper Summary
29	
30	This paper presents the first systematic study of cross-lingual correctness probe transfer for calibration, testing 20 languages across 3 architectures (Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B Dense). It makes four claims forming a causal chain: (1) a depth-transferability Pareto frontier where optimal cross-lingual transfer occurs at ~58–60% of model depth; (2) a decomposition into difficulty-shared (68% variance, transfers well) and capability-specific (32%, drives 87% of transfer degradation) components; (3) CaCLR, a multi-objective training loss that shifts the Pareto frontier outward (+5.2pp AUROC, ~40% ECE reduction, no target-language labels); (4) correctness–confidence orthogonality persists across all 20 languages. Results extend to 52 languages and 3 benchmarks.
31	
32	---
33	
34	## 2. Strengths (Consensus)
35	
36	- **Genuine gap-fill.** All prior probe-based calibration work (Burns, Marks, Miao) is English-only. Syst
…[truncated 4833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T19:53:43.806611+00:00_

**Reviewer 2 初审已收到。** R2 聚焦 Novelty & Related Work，给出 2.5/5（介于 Revise-for-next-cycle 与 Findings 之间），提出 3 个 critical 问题和 5 个 warning。

R2 关键发现摘要：
- **N1** [critical]: 参考文献仅 8 篇，Related Work 不足一页，严重缺失核心先行工作
- **N2** [critical]: "Pareto frontier" 术语技术上不准确——缺乏标准 dominance 分析和可视化
- **N3** [critical]: 四项贡献均为增量性（已知方法的规模扩展），缺乏方法论突破
- **W1-W5**: Related Work 过简、全文 0 图、"first" 声明过强、25% 解释力缺 CI、CaCLR 实际优势有限

---

**当前状态**: 需要 Reviewer 1（方法/实验侧重）的初审意见才能进入交叉分享阶段。请提交 Reviewer 1 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 2

14 recorded events

### User

_source line 25 · 2026-05-20T19:53:46.398568+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。总结如下：

**评分: 2.5/5 (Revise-for-next-cycle)**

三个 Must-Fix 问题：

1. **参考文献极度稀疏（仅 8 篇）**——缺失 Conneau et al.、Pires et al.、CCPS、CKA/SVCCA、Belinkov survey 等大量核心文献，Related Work 仅 ~15 行，远低于顶会标准
2. **"Pareto frontier" 术语技术上不准确**——实际是 depth-transferability trade-off curve，且 deeper layers = more language-specific 是多语言 NLP 已知现象（Pires 2019, Conneau 2020）。论文甚至没有画一张 scatter plot 来可视化这条"frontier"
3. **四项贡献均为增量性**——Claim 1 重新包装已知现象，Claim 2 直接建立在 Civelli et al. 之上，Claim 3 组合三个已知 loss 组件，Claim 4 是方法论上的直接复制扩展

主要优势：实验规模（20语言×3架构×3基准）确实超过先行工作，CaCLR 的 zero-label 设定有实用价值，MoE vs Dense 的 architecture comparison 是新视角。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T19:54:02.660173+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T19:54:04.267112+00:00_

{"result":"# 项目 xling_calib_direction 概况\n\n## 实验状态 (3 个)\n\n- **mvp_002**: DONE (success) — \n- **mvp_001**: DONE (success) — \n- **mvp_003**: RUNNING — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| mvp_003 | Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_002** (failed): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\n\n## 趋势\n成功 1 / 负向 0 / 失败 1 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-13176: 无 GPU 信息\n\n## 告警\n- mvp_002: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1606
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T19:54:04.317868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/skills/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/skills/review-director-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T19:54:04.318426+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/review_director_91c72a1c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T19:54:08.683990+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T19:54:08.734905+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T19:54:59.988389+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T19:55:01.092664+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "elapsed_ms": 1104
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T19:55:02.096673+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T19:55:02.097111+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T19:55:02.097374+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "xling_calib_direction",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T19:55:02.147937+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 13:49 UTC\\n  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B\\n  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &\\n    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B\\n    的大资源。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 13:53 UTC\\n  summary: MVP 模型固定为 Qwen2.5-7B-Instruct\\n  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为\\n    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 18:25 UTC\\n  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言\\n  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用\\n    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: trigger\\n    result: P4 ΔAUROC=0 暴露标准设计缺陷\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-20 18:52 UTC\\n  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'\\n  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth\\n    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift\\n    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift\\n    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: primary\\n    result: P1✅P2✅P3✅P4❌, core hypothesis supported\\n  depends_on: []\\n\", \"total_chars\": 1523, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T19:55:20.295045+00:00_

状态确认：

- **被审论文**：dream report (best tier) — `artifacts/dream_reports/dream_20260520T185641/best/paper.pdf`
- **Reviewer 2**：已完成，评分 2.5/5，3 个 critical + 5 个 warning
- **Reviewer 1**：状态不明（重启后丢失）

由于我没有 `feishu_read_chat_history` 工具，无法自行恢复 R1 的审稿结果。

**请确认**：Reviewer 1 的审稿意见是否已提交？如已提交，请将其内容转发给我，我将进入 Step 2（交叉分享）阶段。如未完成，我等待 R1 返回后继续。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 3

16 recorded events

### User

_source line 39 · 2026-05-20T19:55:20.298901+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：Methods & Experiments

**论文**: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs  
**审稿标准**: ACL Rolling Review form（soundness, excitement, overall assessment, reproducibility, confidence）

---

## 总体评分
**Overall**: 3.0 / 5（Findings 级别）  
**一句话总结**: 实验规模合理、问题选题及时，但 abstract 与正文存在关键数值不一致、完全缺乏统计检验、参考文献仅 8 篇且多条引用信息有误，不达 main conference 门槛。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心 claim 之间存在数值矛盾（72% vs 81%、25% 来源不明）；CaCLR "zero-label" 表述掩盖了对 parallel data 的依赖；无任何 CI/显著性检验 |
| Excitement | 3.0/5 | 跨语言 correctness probe transfer 是值得研究的方向，Pareto frontier 框架有新意，但 CaCLR 的改进幅度有限（~3.4pp over linear proj），decomposition 的解释力（25%? 13%?）模糊 |
| Overall Assessment | 3.0/5 | Findings 推荐——规模 OK，有一定 insight，但 soundness 问题太多 |
| Reproducibility | 2.5/5 | probe 训练的样本量、train/test split、cross-validation 策略均未报告；IRT difficulty 参数估计流程不透明；超参 α=0.15, β=0.08 无 sensitivity analysis |
| Confidence | 4/5 | 仔细阅读全文并验证了引用；熟悉 probing、calibration、cross-lingual transfer 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract 与正文数值不一致——72% vs 81%
- 具体位置：Abstract ("predicts method choice with 72% accuracy") vs §5.2 line 306 ("81% prescriptive accuracy")
- 问题：Abstract 声称 decomposition 的 prescriptive accuracy 为 72%，但正文 §5.2 明确写 81%。如果 abstract 的 72% 其实来自 IRT 的 R²=0.72（§5.2 line 270: "$R^2=0.72$"），则属于指标混淆——explained variance ≠ prescriptive accuracy。无论哪种情况都是严重的内部一致性问题。
- 为什么影响接收：核心 claim 的数字自相矛盾，直接动摇论文可信度。
- 建议修改方向：统一数字，明确说明 72% 和 81% 分别度量的是什么；如果是不同指标需清楚定义。

**N2** [critical] "Explains 25% of the transfer gap" 来源不明
- 具体位置：Abstract ("explains 25% of the transfer gap")
- 问题：Table 5 显示 difficulty-shared component 占 Transfer Degradation 的 13%（Share% 列），capability-specific 占 87%。无论从哪个角度看，都推不出 "25%"。论文正文 §5.2 也未出现 "25%" 这个数字。
- 为什么影响接收：Abstract 中的核心量化 claim 无法从论文内部数据 verify，要么是计算错误，要么是引用了未展示的分析。
- 建议修改方向：删除或修正这个数字，并给出明确推导路径。

**N3** [critical] 参考文献严重不足且多条引用信息有误
- 具体位置：References（Page 10，共 8 条）
- 问题：(a) 全文仅 8 条引用，对一篇覆盖 probing、calibration、IRT、cross-lingual transfer 的论文而言极度不足——同类 ACL 论文通常 30-50 条。缺失大量关键引用（如 Guo et al. 2017 temperature scaling、IRT 基础文献、multilingual calibration benchmarks、cross-lingual alignment 文献）。(b) Web search 核查发现多条引用信息存在 discrepancy：
  - Miao et al. (2026a) "CORAL"：论文写 "Shuo Miao"，但 ICML 2026 实际发表的 CORAL 论文（arxiv 2602.06022）第一作者为 Miranda Muqing Miao；论文中标题 "Cross-task correctness probes for LLM calibration" 也与实际标题 "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering" 不符。
  - Zhou et al. (2024) "LACE"：实际论文 "Beyond the Final Layer" 发表于 2025（arxiv 2510.03136），非 2024；标题和可能的第一作者名均不匹配。
  - Civelli et al. (2025)：最接近的论文为 "A Shared Geometry of Difficulty in Multilingual Language Models"（arxiv 2601.12731），标题不匹配。
- 为什么影响接收：引用不足意味着论文未充分定位自身贡献；引用信息错误（作者名、标题、年份）损害学术严谨性，对 blind review 而言更是 red flag。
- 建议修改方向：(1) 大幅扩展引用至 30+ 条；(2) 逐条核查所有引用的作者名、标题、年份和出版 venue。

**N4** [critical] 完全缺乏统计检验和方差估计
- 具体位置：全文所有实验结果（Tables 1-16）
- 问题：所有数字均为单次实验的点估计，无 confidence interval、standard deviation、bootstrap significance test 或多次 random seed 报告。对于 probe 训练（随机初始化）、Pareto frontier 判定（对 noise 敏感）、CaCLR 与 baseline 的比较（差距仅 3.4pp），统计不确定性可能改变结论。
- 为什么影响接收：ARR Soundness 维度明确要求 claims 有充分支撑。无统计检验的 3.4pp 差异无法判断是否 significant。
- 建议修改方向：至少对 probe 训练用 5 次 random seed 报告均值±标准差；对 CaCLR vs linear proj 做 paired bootstrap test。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] CaCLR "zero-label" 表述有误导性
- 具体位置：§3.4、Abstract ("zero-label setting")
- 问题：CaCLR 的 L_cons 项使用 English-target parallel activations 的 KL divergence（§3.4: "penalizes divergence between probe outputs on English and non-English parallel activations"），这要求 parallel data。Linear projection 同样需要 parallel data 但不需要 target labels。因此 CaCLR 与 linear proj 的资源需求本质相同，"zero-label" 的表述让读者以为完全无需 target language 资源，实际并非如此。
- 建议：改为 "zero-correctness-label" 并明确讨论 parallel data 需求及其对低资源语言的限制。

**W2** [warning] CaCLR 超参数无 sensitivity analysis
- 具体位置：§3.4（α=0.15, β=0.08）
- 问题：α 和 β 的值对结果有多敏感？论文仅说 "tuned on a validation set" 但未报告搜索范围或性能对超参的敏感度。对一个提出新 loss function 的论文，这是必要的分析。
- 建议：添加 α, β sensitivity plot 或至少报告几个不同值下的性能。

**W3** [warning] INT8 验证范围过窄
- 具体位置：§5.9, Table 16
- 问题：仅在 Llama 4 Scout 上用 5% 子集验证。鉴于论文声称结论跨三种架构成立，至少应在 Qwen3 或 Gemma 4 上也做 INT8 验证。
- 建议：增加至少一个架构的 INT8 验证。

**W4** [warning] 无任何可视化图表
- 具体位置：全文
- 问题：一篇关于 Pareto frontier 的论文没有任何 figure——Table 1/3 的 Pareto 前沿应该用 scatter plot 展示（x=depth, y=transfer AUROC），读者才能直观理解 frontier shape、architecture 差异等核心论点。Table 4 的 cross-architecture agreement 也适合可视化。
- 建议：添加 2-3 个 key figures（Pareto scatter plot、decomposition visualization、CaCLR ablation bar chart）。

**W5** [warning] Extended coverage 的低资源结论统计效力不足
- 具体位置：§5.8, Table 15
- 问题：Very low resource tier 仅含 4 种语言，50% pass rate 意味着 2 pass / 2 fail。这个样本量不足以支撑关于资源等级的梯度结论。
- 建议：增加 very low resource 语言数量，或明确说明这是 preliminary observation 而非 robust finding。

**W6** [warning] Probe 训练细节不充分
- 具体位置：§4 (Experimental Setup)
- 问题：未报告 (1) 训练样本量 (2) train/test split 比例 (3) 是否使用 cross-validation (4) logistic regression 的正则化参数。这些对 reproducibility 至关重要。
- 建议：在 §4 或 appendix 中补充完整训练配置。

---

## 小问题（不影响接收）

- Abstract 第一句 "Non-English languages suffer substantially worse calibration" 缺少对比基准（worse than what? English? random?）
- §3.1 提到 "logistic regression (primary) and 2-layer MLP (comparison)" 但 §4 Probes 部分说 "Trained on English correctness labels from GlobalMMLU"——应明确是哪个 split
- Table 14: Gemma 4 31B (Dense) 的 Depth% = 60% 与两个 MoE 模型（60%, 58%）几乎相同——这反而 undermines "architecture-dependent" 的表述，可考虑更准确的 characterization
- §6 Discussion 提到 "first-order distributional mismatch but not nonlinear feature interactions" 作为 CaCLR 局限性，但这个分析缺乏实验支撑

---

## Experiment Coverage Check

| Plan | 是否覆盖 | 位置 | 备注 |
|------|---------|------|------|
| plan_001: Qwen3-235B Pareto | ✓ | Table 1 | ~21 layers sampled (每 4 层), 非全部 94 层 |
| plan_002: Llama 4 Scout Pareto | ✓ | Table 3 | |
| plan_003: CaCLR 实现 & 对比 | ✓ | Tables 7, 8, 9 | |
| plan_004: Difficulty-Controlled Ablation | ✓ | Table 5, §5.2 | |
| plan_005: Cross-Lingual Orthogonality | ✓ | Tables 10, 11, §5.4 | |
| plan_006: Probe Complexity | ✓ | Table 12, §5.5 | 仅在 Qwen3 上比较 |
| plan_007: Additional Benchmarks | ✓ | Table 13, §5.6 | |
| plan_008: Gemma 4 31B | ✓ | Table 14, §5.7 | |
| plan_009: Extended 53 Languages | ✓ | Table 15, §5.8 | 实际报告 52 种语言（非 53） |
| plan_010: INT8 Validation | ✓ | Table 16, §5.9 | 仅 Llama 4 Scout, 5% subset |

所有 10 个 plan 均有对应结果，但部分覆盖深度有限（plan_006 单架构、plan_010 单架构 5% 子集）。

---

## 主要优势

1. **问题选择好**：跨语言 correctness probe transfer 是一个有实际意义且尚未被系统研究的方向
2. **实验规模合理**：20 语言 × 3 架构 × 3 benchmark 的矩阵覆盖面在同类工作中属于上游
3. **Pareto frontier 框架有启发性**：将 depth-transferability tradeoff 形式化为 Pareto 问题是有价值的分析视角
4. **Difficulty-capability decomposition 概念新颖**：用 IRT 分离 difficulty 和 capability 信号是有创意的方法论贡献，尽管目前解释力有限
5. **CaCLR 设计原则合理**：三项 loss 各有明确语义，ablation (Table 8) 清楚展示了各项贡献
6. **全部 10 个实验计划均已覆盖**，说明执行完整度高

---

## 对作者的具体问题

1. Abstract 的 "72% accuracy" 与 §5.2 的 "81% prescriptive accuracy" 分别度量什么？如果是不同指标，为什么 abstract 不用 §5.2 中实际报告的 81%？
2. "Explains 25% of the transfer gap"（abstract）这个数字的推导路径是什么？Table 5 中 difficulty-shared 的 Share% 是 13%，不是 25%。
3. CaCLR 的 L_cons 需要 parallel activations。与 linear projection 同样需要 parallel data 相比，CaCLR 的实际资源优势在哪里？
4. IRT difficulty 参数是从英语数据单独估计的吗？如果是，这对跨语言 decomposition 的 validity 有何影响？
5. 为什么全文仅 8 条引用？是否有更多引用在 appendix 中但未纳入主文？（PDF 中未见 appendix）
6. Miao et al. (2026a) 引为 "Shuo Miao"——这是否与 ICML 2026 发表 CORAL 的 Miranda Muqing Miao 为同一人？如果是，请修正作者名。
7. Probe 训练用了多少样本？是否做了 cross-validation？Logistic regression 的正则化参数是多少？
8. 为什么没有任何 figure？Pareto frontier 以 scatter plot 呈现会比表格直观得多。

---

## 评分总结

| 维度 | 分数 |
|------|------|
| Soundness | 2.5/5 |
| Excitement | 3.0/5 |
| Overall Assessment | 3.0/5 (Findings) |
| Reproducibility | 2.5/5 |
| Reviewer Confidence | 4/5 |


---

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心发现摘要：**

- **Overall 3.0/5 (Findings)**，Soundness 2.5，Excitement 3.0
- **4 个 Must-Fix**：(1) Abstract 与正文数值矛盾（72% vs 81%）；(2) "explains 25% of the transfer gap" 无法从 Table 5 推导；(3) 仅 8 条引用且多条作者名/标题/年份与实际出版物不符；(4) 全文无任何统计检验或方差估计
- **6 个 Should-Fix**：CaCLR "zero-label" 误导性表述、超参无 sensitivity analysis、INT8 验证过窄、无 figure、低资源语言样本量不足、probe 训练细节缺失
- 所有 10 个实验计划均已覆盖，执行完整度高
- 问题选择好、实验规模合理、Pareto frontier 框架有启发性，但 soundness 问题过多

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T19:56:17.798356+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉审阅任务\n\n以下是 **Reviewer 2（Novelty & Related Work 方向）** 的完整 Round 1 审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n\n- **[AGREE]**：同意该观点，并简要说明为什么你也认同（可补充你从 Methods/Experiments 角度的佐证）\n- **[REBUT]**：不同意或有保留意见，提供具体证据（引用论文中的 Section/Table/Figure）\n\n特别关注：R2 提出的 N2（\"Pareto frontier\" 术语不准确）和 N3（四项贡献均为增量性）——这两个问题与你负责的方法论严谨性直接相关，请给出详细判断。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**总体评分**: 2.5 / 5（介于 Revise-for-next-cycle 与 Findings 之间）\n\n### ACL ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心实验设计合理，但\"Pareto frontier\"术语的技术准确性存疑；decomposition 的 25% variance explained 较低却被作为主要贡献宣传 |\n| Excitement | 2 / 5 | 四项贡献均为已知技术的直接扩展或组合，缺乏方法论上的惊喜 |\n| Reproducibility | 3.5 / 5 | 实验设置描述清楚（§4），超参数有报告（α=0.15, β=0.10），但代码/数据未提及是否公开 |\n| Confidence | 4 / 5 | 熟悉 probe-based calibration 和跨语言表征领域 |\n\n### Must-Fix 问题\n\n**N1** [critical] 参考文献极度稀疏——全文仅 8 篇引用\n- 一篇覆盖 probe-based calibration、cross-lingual probing、multilingual calibration 的论文仅引用 8 篇文献。缺失关键文献：Conneau et al. (2020)、Pires et al. (2019)、CKA/SVCCA (Kornblith 2019, Raghu 2017)、CCPS (Wang et al.)、Belinkov (2022) probing survey、Keleg & Magdy (2023) multilingual calibration、IRT 原始文献 (Lord 1980, Baker 2001)、MKA (Chen et al. 2024)。\n- Related Work 仅 ~15 行，应扩展至 1.5-2 页，引用量应在 30+ 篇。\n\n**N2** [critical] \"Pareto frontier\" 术语使用不准确，核心 framing 有误导性\n- 论文描述的是 depth vs. cross-lingual transfer AUROC 的单调递减关系——这是 trade-off curve 不是 Pareto frontier。没有标准 Pareto dominance 分析、hypervolume indicator、scatter plot 可视化。\n- 如果只是\"deeper layers 有更好的 English probe 但更差的 cross-lingual transfer\"，这在多语言 NLP 中是已知现象（Pires et al. 2019; Conneau et al. 2020）。\n\n**N3** [critical] 四项贡献的新颖性均为增量性\n- Claim 1: deeper layers = more language-specific 是已知现象\n- Claim 2: Civelli et al. (2025) 已证明 IRT difficulty probes 跨语言迁移，R²=0.72 未超越其结果\n- Claim 3: CaCLR = BCE + calibration penalty + consistency reg，三者均为已知技术组合\n- Claim 4: 方法论上直接复制 Miao & Ungar (2026) 到 20 种语言\n\n### Should-Fix 问题\n\n**W1** Related Work（§2）过于简略——仅 ~15 行\n**W2** 全文 16 张表格、0 张图——可读性差\n**W3** \"First systematic study\" 声明过强\n**W4** Difficulty-capability decomposition 的 25% 解释力未给置信区间\n**W5** CaCLR 的 improvement 幅度较小（+1.3pp avg AUROC），实际意义不清楚\n\n### 主要优势\n- S1: 实验规模超过先行工作（20语言×3架构×3基准）\n- S2: CaCLR 的 zero-label 设定有实际意义\n- S3: MoE vs Dense frontier 形状差异是新发现\n- S4: Resource-tier gradient 在 orthogonality 上的发现有趣\n\n### 给作者的问题\n1. Table 1 中 ★ 层是否经过标准 Pareto dominance 检验？\n2. CaCLR consistency reg 是否需要 parallel data？\"zero-label\" 定义是什么？\n3. h²=0.72 与 Civelli et al. 报告值对比如何？\n4. Orthogonality 的 cosine similarity 在 probe weight vectors 还是 direction vectors 上计算？\n5. MoE expert routing 是否影响 layer-wise probing 的解释？",
  "project": "xling_calib_direction",
  "chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
  "director_session_key": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉审阅任务\n\n以下是 **Reviewer 2（Novelty & Related Work 方向）** 的完整 Round 1 审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n\n- **[AGREE]**：同意该观点，并简要说明为什么你也认同（可补充你从 Methods/Experiments 角度的佐证）\n- **[REBUT]**：不同意或有保留意见，提供具体证据（引用论文中的 Section/Table/Figure）\n\n特别关注：R2 提出的 N2（\"Pareto frontier\" 术语不准确）和 N3（四项贡献均为增量性）——这两个问题与你负责的方法论严谨性直接相关，请给出详细判断。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**总体评分**: 2.5 / 5（介于 Revise-for-next-cycle 与 Findings 之间）\n\n### ACL ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心实验设计合理，但\"Pareto frontier\"术语的技术准确性存疑；decomposition 的 25% variance explained 较低却被作为主要贡献宣传 |\n| Excitement | 2 / 5 | 四项贡献均为已知技术的直接扩展或组合，缺乏方法论上的惊喜 |\n| Reproducibility | 3.5 / 5 | 实验设置描述清楚（§4），超参数有报告（α=0.15, β=0.10），但代码/数据未提及是否公开 |\n| Confidence | 4 / 5 | 熟悉 probe-based calibration 和跨语言表征领域 |\n\n### Must-Fix 问题\n\n**N1** [critical] 参考文献极度稀疏——全文仅 8 篇引用\n- 一篇覆盖 probe-based calibration、cross-lingual probing、multilingual calibration 的论文仅引用 8 篇文献。缺失关键文献：Conneau et al. (2020)、Pires et al. (2019)、CKA/SVCCA (Kornblith 2019, Raghu 2017)、CCPS (Wang et al.)、Belinkov (2022) probing survey、Keleg & Magdy (2023) multilingual calibration、IRT 原始文献 (Lord 1980, Baker 2001)、MKA (Chen et al. 2024)。\n- Related Work 仅 ~15 行，应扩展至 1.5-2 页，引用量应在 30+ 篇。\n\n**N2** [critical] \"Pareto frontier\" 术语使用不准确，核心 framing 有误导性\n- 论文描述的是 depth vs. cross-lingual transfer AUROC 的单调递减关系——这是 trade-off curve 不是 Pareto frontier。没有标准 Pareto dominance 分析、hypervolume indicator、scatter plot 可视化。\n- 如果只是\"deeper layers 有更好的 English probe 但更差的 cross-lingual transfer\"，这在多语言 NLP 中是已知现象（Pires et al. 2019; Conneau et al. 2020）。\n\n**N3** [critical] 四项贡献的新颖性均为增量性\n- Claim 1: deeper layers = more language-specific 是已知现象\n- Claim 2: Civelli et al. (2025) 已证明 IRT difficulty probes 跨语言迁移，R²=0.72 未超越其结果\n- Claim 3: CaCLR = BCE + calibration penalty + consistency reg，三者均为已知技术组合\n- Claim 4: 方法论上直接复制 Miao & Ungar (2026) 到 20 种语言\n\n### Should-Fix 问题\n\n**W1** Related Work（§2）过于简略——仅 ~15 行\n**W2** 全文 16 张表格、0 张图——可读性差\n**W3** \"First systematic study\" 声明过强\n**W4** Difficulty-capability decomposition 的 25% 解释力未给置信区间\n**W5** CaCLR 的 improvement 幅度较小（+1.3pp avg AUROC），实际意义不清楚\n\n### 主要优势\n- S1: 实验规模超过先行工作（20语言×3架构×3基准）\n- S2: CaCLR 的 zero-label 设定有实际意义\n- S3: MoE vs Dense frontier 形状差异是新发现\n- S4: Resource-tier gradient 在 orthogonality 上的发现有趣\n\n### 给作者的问题\n1. Table 1 中 ★ 层是否经过标准 Pareto dominance 检验？\n2. CaCLR consistency reg 是否需要 parallel data？\"zero-label\" 定义是什么？\n3. h²=0.72 与 Civelli et al. 报告值对比如何？\n4. Orthogonality 的 cosine similarity 在 probe weight vectors 还是 direction vectors 上计算？\n5. MoE expert routing 是否影响 layer-wise probing 的解释？",
    "project": "xling_calib_direction",
    "chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
    "director_session_key": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T19:56:42.891285+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25092
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T19:56:43.496799+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉审阅任务\n\n以下是 **Reviewer 1（Methods & Experiments 方向）** 的完整 Round 1 审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n\n- **[AGREE]**：同意该观点，并简要说明为什么你也认同（可补充你从 Novelty/Related Work 角度的佐证）\n- **[REBUT]**：不同意或有保留意见，提供具体证据（引用论文中的 Section/Table/Figure）\n\n特别关注：R1 提出的 N1（Abstract 72% vs 正文 81% 数值矛盾）和 N2（\"25% of transfer gap\" 无法从数据推导）——这两个是你初审中未涉及的新发现，请判断严重程度。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**总体评分**: 3.0 / 5（Findings 级别）\n\n### ACL ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claim 之间存在数值矛盾（72% vs 81%、25% 来源不明）；CaCLR \"zero-label\" 表述掩盖了对 parallel data 的依赖；无任何 CI/显著性检验 |\n| Excitement | 3.0/5 | 跨语言 correctness probe transfer 值得研究，Pareto frontier 框架有新意，但 CaCLR 改进幅度有限（~3.4pp over linear proj），decomposition 解释力模糊 |\n| Overall Assessment | 3.0/5 | Findings 推荐——规模 OK，有一定 insight，但 soundness 问题太多 |\n| Reproducibility | 2.5/5 | probe 训练样本量、train/test split、cross-validation 策略均未报告；IRT difficulty 参数估计流程不透明；超参无 sensitivity analysis |\n| Confidence | 4/5 | 仔细阅读全文并验证了引用；熟悉 probing、calibration、cross-lingual transfer 文献 |\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 与正文数值不一致——72% vs 81%\n- Abstract: \"predicts method choice with 72% accuracy\" vs §5.2: \"81% prescriptive accuracy\"\n- 可能 72% 来自 IRT 的 R²=0.72（§5.2），属于指标混淆（explained variance ≠ prescriptive accuracy）\n- 核心 claim 数字自相矛盾，直接动摇论文可信度\n\n**N2** [critical] \"Explains 25% of the transfer gap\" 来源不明\n- Abstract 核心 claim，但 Table 5 显示 difficulty-shared 占 Transfer Degradation 的 13%，capability-specific 占 87%\n- 无论从哪个角度看都推不出 \"25%\"，正文 §5.2 也未出现此数字\n- 要么计算错误，要么引用了未展示的分析\n\n**N3** [critical] 参考文献严重不足且多条引用信息有误\n- 全文仅 8 条引用（同类 ACL 论文通常 30-50 条）\n- Web search 核查发现：\n  - Miao et al. (2026a) \"CORAL\"：实际第一作者为 Miranda Muqing Miao（非 Shuo Miao），标题也不匹配\n  - Zhou et al. (2024) \"LACE\"：实际发表于 2025（arxiv 2510.03136），年份和标题均不匹配\n  - Civelli et al. (2025)：标题与最接近的论文 \"A Shared Geometry of Difficulty\" 不匹配\n\n**N4** [critical] 完全缺乏统计检验和方差估计\n- 所有 Tables 1-16 均为单次实验点估计\n- 无 CI、SD、bootstrap significance test 或多次 random seed\n- CaCLR vs baseline 差距仅 3.4pp，无法判断是否 significant\n\n### Should-Fix 问题\n\n**W1** CaCLR \"zero-label\" 表述有误导性——L_cons 需要 parallel activations，与 linear proj 资源需求本质相同\n**W2** CaCLR 超参数（α=0.15, β=0.08）无 sensitivity analysis\n**W3** INT8 验证仅在 Llama 4 Scout 上用 5% 子集\n**W4** 无任何可视化图表——Pareto frontier 论文没有 scatter plot\n**W5** Very low resource tier 仅 4 种语言，统计效力不足\n**W6** Probe 训练细节不充分——样本量、split、CV、正则化参数均未报告\n\n### 主要优势\n1. 问题选择好——跨语言 correctness probe transfer 有实际意义且尚未被系统研究\n2. 实验规模合理——20语言×3架构×3 benchmark\n3. Pareto frontier 框架有启发性\n4. Difficulty-capability decomposition 概念新颖\n5. CaCLR 设计原则合理，ablation 清楚\n6. 全部 10 个实验计划均已覆盖\n\n### 给作者的问题\n1. Abstract 72% vs §5.2 81% 分别度量什么？\n2. \"25% of transfer gap\" 推导路径？\n3. CaCLR L_cons 的 parallel data 需求 vs linear proj 的实际资源优势？\n4. IRT difficulty 参数是英语单独估计的吗？\n5. 为什么仅 8 条引用？\n6. Miao et al. 的作者名是否有误？\n7. Probe 训练样本量和 CV 策略？\n8. 为什么没有任何 figure？",
  "project": "xling_calib_direction",
  "chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
  "director_session_key": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉审阅任务\n\n以下是 **Reviewer 1（Methods & Experiments 方向）** 的完整 Round 1 审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n\n- **[AGREE]**：同意该观点，并简要说明为什么你也认同（可补充你从 Novelty/Related Work 角度的佐证）\n- **[REBUT]**：不同意或有保留意见，提供具体证据（引用论文中的 Section/Table/Figure）\n\n特别关注：R1 提出的 N1（Abstract 72% vs 正文 81% 数值矛盾）和 N2（\"25% of transfer gap\" 无法从数据推导）——这两个是你初审中未涉及的新发现，请判断严重程度。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**总体评分**: 3.0 / 5（Findings 级别）\n\n### ACL ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claim 之间存在数值矛盾（72% vs 81%、25% 来源不明）；CaCLR \"zero-label\" 表述掩盖了对 parallel data 的依赖；无任何 CI/显著性检验 |\n| Excitement | 3.0/5 | 跨语言 correctness probe transfer 值得研究，Pareto frontier 框架有新意，但 CaCLR 改进幅度有限（~3.4pp over linear proj），decomposition 解释力模糊 |\n| Overall Assessment | 3.0/5 | Findings 推荐——规模 OK，有一定 insight，但 soundness 问题太多 |\n| Reproducibility | 2.5/5 | probe 训练样本量、train/test split、cross-validation 策略均未报告；IRT difficulty 参数估计流程不透明；超参无 sensitivity analysis |\n| Confidence | 4/5 | 仔细阅读全文并验证了引用；熟悉 probing、calibration、cross-lingual transfer 文献 |\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 与正文数值不一致——72% vs 81%\n- Abstract: \"predicts method choice with 72% accuracy\" vs §5.2: \"81% prescriptive accuracy\"\n- 可能 72% 来自 IRT 的 R²=0.72（§5.2），属于指标混淆（explained variance ≠ prescriptive accuracy）\n- 核心 claim 数字自相矛盾，直接动摇论文可信度\n\n**N2** [critical] \"Explains 25% of the transfer gap\" 来源不明\n- Abstract 核心 claim，但 Table 5 显示 difficulty-shared 占 Transfer Degradation 的 13%，capability-specific 占 87%\n- 无论从哪个角度看都推不出 \"25%\"，正文 §5.2 也未出现此数字\n- 要么计算错误，要么引用了未展示的分析\n\n**N3** [critical] 参考文献严重不足且多条引用信息有误\n- 全文仅 8 条引用（同类 ACL 论文通常 30-50 条）\n- Web search 核查发现：\n  - Miao et al. (2026a) \"CORAL\"：实际第一作者为 Miranda Muqing Miao（非 Shuo Miao），标题也不匹配\n  - Zhou et al. (2024) \"LACE\"：实际发表于 2025（arxiv 2510.03136），年份和标题均不匹配\n  - Civelli et al. (2025)：标题与最接近的论文 \"A Shared Geometry of Difficulty\" 不匹配\n\n**N4** [critical] 完全缺乏统计检验和方差估计\n- 所有 Tables 1-16 均为单次实验点估计\n- 无 CI、SD、bootstrap significance test 或多次 random seed\n- CaCLR vs baseline 差距仅 3.4pp，无法判断是否 significant\n\n### Should-Fix 问题\n\n**W1** CaCLR \"zero-label\" 表述有误导性——L_cons 需要 parallel activations，与 linear proj 资源需求本质相同\n**W2** CaCLR 超参数（α=0.15, β=0.08）无 sensitivity analysis\n**W3** INT8 验证仅在 Llama 4 Scout 上用 5% 子集\n**W4** 无任何可视化图表——Pareto frontier 论文没有 scatter plot\n**W5** Very low resource tier 仅 4 种语言，统计效力不足\n**W6** Probe 训练细节不充分——样本量、split、CV、正则化参数均未报告\n\n### 主要优势\n1. 问题选择好——跨语言 correctness probe transfer 有实际意义且尚未被系统研究\n2. 实验规模合理——20语言×3架构×3 benchmark\n3. Pareto frontier 框架有启发性\n4. Difficulty-capability decomposition 概念新颖\n5. CaCLR 设计原则合理，ablation 清楚\n6. 全部 10 个实验计划均已覆盖\n\n### 给作者的问题\n1. Abstract 72% vs §5.2 81% 分别度量什么？\n2. \"25% of transfer gap\" 推导路径？\n3. CaCLR L_cons 的 parallel data 需求 vs linear proj 的实际资源优势？\n4. IRT difficulty 参数是英语单独估计的吗？\n5. 为什么仅 8 条引用？\n6. Miao et al. 的作者名是否有误？\n7. Probe 训练样本量和 CV 策略？\n8. 为什么没有任何 figure？",
    "project": "xling_calib_direction",
    "chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
    "director_session_key": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T19:56:44.867843+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1371
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T19:56:48.834283+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T19:56:48.834733+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T19:56:48.885211+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T19:56:48.885614+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T19:56:54.710829+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T19:56:54.761315+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T19:56:58.475199+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "xling_calib_direction",
  "review_chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "xling_calib_direction",
    "review_chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T19:56:58.977197+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"未找到投稿论文 PDF 路径（review_paper_pdf_path 未配置）。请确认 Director 提交审稿时填写了 paper_pdf_path。\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 501
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T19:57:02.343110+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "xling_calib_direction",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf",
  "venue": "ACL ARR",
  "note": "Dream paper review — best scenario tier. 内部审稿已进入交叉分享阶段，外部审稿结果将异步纳入最终报告。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "xling_calib_direction",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf",
    "venue": "ACL ARR",
    "note": "Dream paper review — best scenario tier. 内部审稿已进入交叉分享阶段，外部审稿结果将异步纳入最终报告。"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-20T19:57:02.995677+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 652
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-20T19:57:18.970978+00:00_

**当前审稿进度汇报（Group C）：**

| 步骤 | 状态 |
|------|------|
| Step 1 独立审稿 | ✅ R1 (3.0/5) + R2 (2.5/5) 均已提交 |
| Step 2 交叉分享 | 🔄 已分发，等待两位 Reviewer 逐条回应 |
| 外部审稿 (Stanford Agentic Reviewer) | 📤 已请求，异步等待 |
| 视觉审查 | ❌ 派发失败（PDF 路径未配置），将在报告中标注 |

**初步发现交叉对照：**

两位 Reviewer 的**共识区域**：
- 参考文献严重不足（仅 8 篇）→ R1-N3 + R2-N1
- 缺乏可视化 → R1-W4 + R2-W2
- CaCLR "zero-label" 表述误导 → R1-W1 + R2 Q2
- 统计检验缺失 → R1-N4 + R2-W4

**R1 独有发现**（R2 未触及）：
- Abstract 72% vs 正文 81% 数值矛盾 (R1-N1)
- "25% of transfer gap" 无法从数据推导 (R1-N2)
- 引用信息错误：作者名、标题、年份不匹配 (R1-N3b)
- Probe 训练细节严重缺失 (R1-W6)

**R2 独有发现**（R1 未触及）：
- "Pareto frontier" 术语技术上不准确 (R2-N2)
- 四项贡献均为增量性的系统论证 (R2-N3)
- "First systematic study" 声明过强 (R2-W3)

等待交叉回应后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 4

2 recorded events

### User

_source line 55 · 2026-05-20T19:58:24.985722+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 (Round 1) 的交叉回应

---

## Must-Fix 问题逐条回应

### [AGREE] R2-N1: 参考文献极度稀疏（仅 8 篇引用）

完全同意。这与我审稿报告中的 N3 问题重叠。我从 Methods/Experiments 角度补充：

1. **引用信息准确性问题**比 R2 指出的"缺失"更严重——我通过 web search 核查发现多条现有引用的作者名/标题/年份与实际出版物不匹配（详见我的 N3）。Miao et al. (2026a) 引为 "Shuo Miao" 但 ICML 2026 CORAL 论文第一作者为 Miranda Muqing Miao；Zhou et al. (2024) "LACE" 的实际论文发表于 2025，标题也不同。
2. R2 列出的缺失引用清单（Conneau et al. 2020、Pires et al. 2019、Belinkov 2022 survey、IRT 原始文献 Lord 1980/Baker 2001 等）我完全认同。特别是 IRT 原始文献——论文 §3.3 使用 IRT difficulty 作为核心分析工具，却未引用 IRT 的任何基础文献，这在方法论上不可接受。

---

### [REBUT（部分）] R2-N2: "Pareto frontier" 术语不准确

R2 的核心主张是"论文描述的只是单调递减的 trade-off curve，不是 Pareto frontier"。我认为这个判断**过于绝对**，但 R2 指出的形式化不足是成立的。

**反驳依据（Table 1, §5.1）：**

Table 1 中 ★ 标记的 6 个层确实满足 Pareto non-dominance 的基本定义。以两个目标（EN AUROC↑, ZS-19 AUROC↑）检验：

- L44: (.810, .774) — 没有其他层同时 EN≥.810 且 ZS≥.774
- L48: (.816, .770) — L44 的 ZS 更高但 EN 更低 → 互不支配
- L52: (.827, .763) — 同理
- L56: (.832, .762), L60: (.835, .751), L64: (.839, .728)

每一层在 EN 上优于前一层、在 ZS 上劣于前一层，形成标准的 Pareto 前沿。这**不是**简单的单调递减——ZS 在浅层（L8→L44）实际上是上升的，EN 在深层（L76→L88）是下降的。整体曲线呈倒 U 形而非单调，Pareto 前沿只出现在中间区段。

**同意部分：**

1. 论文确实**没有执行形式化的 Pareto dominance 检验**——★ 的标注标准未明确说明
2. **缺少 scatter plot** 是严重的呈现问题（与我 W4 一致）——没有可视化，读者无法判断 frontier shape
3. 论文未报告 hypervolume indicator 或其他多目标优化标准度量
4. "Architecture-dependent frontier shape" 这个 claim（Table 14: Depth% 分别为 60%, 58%, 60%）在数值上差异很小，用 "architecture-dependent" 描述有夸大之嫌

**结论：术语本身的使用不算错误，但缺乏形式化验证和可视化。建议作者 (1) 明确定义 Pareto dominance 判定标准 (2) 添加 scatter plot (3) 报告 hypervolume 或 ε-dominance 指标。** R2 说"这是已知现象"有一定道理（deeper = more language-specific），但将其形式化为 Pareto frontier 并跨 3 个架构量化是新的贡献，只是目前形式化程度不够。

---

### [AGREE（部分）] R2-N3: 四项贡献均为增量性

从 Methods 角度逐项评估：

**Claim 1（Pareto frontier）**：[AGREE with nuance]
- R2 说 "deeper layers = more language-specific 是已知现象"——这个大方向确实已知（Pires et al. 2019, Conneau et al. 2020）。但将其量化为 Pareto frontier、并发现 ~58-60% depth 的跨架构收敛点，具有一定增量价值。
- 然而，Table 14 显示三种架构的 Depth% 分别为 60%, 58%, 60%，ρ 分别为 .88, .82, .86——差异确实不大，"architecture-dependent" 的 framing 过强。

**Claim 2（decomposition）**：[AGREE]
- 如果 Civelli et al. (2025) 确实已证明 IRT difficulty probes 可以跨语言迁移，那本文的 R²=0.72 仅是在不同模型/规模上的 replication。
- 更关键的是：论文声称 "explains 25% of the transfer gap"（abstract），但这个 25% 在 Table 5 中无法 verify（我在 N2 中已详述）。Decomposition 的解释力不清不楚，难以构成独立贡献。

**Claim 3（CaCLR）**：[REBUT（部分）]
- R2 说 "BCE + calibration penalty + consistency reg 均为已知技术"——这没错，但**组合并非平凡**。Table 8 的 ablation 清楚显示 L_cons 贡献 +4.1pp AUROC，L_SB-ECE 贡献 calibration improvement（ECE 从 0.078→0.061）。三项 loss 之间有 synergy，不是简单堆叠。
- 从 Experiments 角度，CaCLR 在 Table 7 中 AUROC .804 vs linear proj .770（+3.4pp），且 CaCLR 的 ECE 也更低（.058 vs .062）。这个提升虽不巨大，但在 zero-label 条件下优于 few-shot(100)（.762）是有实际意义的。
- **但我同意 R2 的一个隐含观点**：CaCLR 声称 "zero-label" 却需要 parallel data（用于 L_cons），这与 linear projection 的资源需求本质相同。如果两者都需要 parallel data，3.4pp 的改进确实算 incremental。
- **关于 R2 提到的 "+1.3pp"**：我在论文中找不到这个数字的来源。Table 7 显示 CaCLR vs linear proj 差距为 3.4pp，Table 2 显示 3.3pp。如果 1.3pp 来自某个特定架构/子集，R2 应标明来源。

**Claim 4（orthogonality）**：[AGREE]
- 完全同意 R2 的判断。Tables 10-11 的方法论与 Miao & Ungar (2026) 一致，贡献仅在于从英语扩展到 20 种语言。Resource-tier gradient（§5.4 末尾提到）是有趣的观察，但分析深度不足以构成独立 claim。

**总体判断**：四项贡献中，Claim 3（CaCLR）的新颖性最高但受 "zero-label" 误导性表述和 parallel data 依赖的削弱；Claim 1 有增量价值但 framing 过强；Claims 2 和 4 的独立新颖性不足。作为整体 package，这些贡献在 **Findings 级别**是可以接受的。

---

## Should-Fix 问题逐条回应

### [AGREE] R2-W1: Related Work 过于简略
与我的观察一致。~15 行 Related Work 对这个研究范围而言远远不够。

### [AGREE] R2-W2: 16 张表格、0 张图
这与我的 W4 完全一致。一篇关于 Pareto frontier 的论文没有任何 scatter plot 是不可接受的。

### [AGREE] R2-W3: "First systematic study" 声明过强
鉴于 Civelli et al. (2025)、Xiao et al. (2025)、Zhou et al. (LACE, 2025) 的存在，这个 claim 至少需要加限定语。

### [AGREE] R2-W4: 25% 解释力无置信区间
我完全同意，并在我的审稿报告中更进一步指出：这个 "25%" 本身在论文数据中就无法 verify（我的 N2）。在无法确认数字来源的情况下，置信区间的缺失是次要问题——首先需要解释 25% 从何而来。

### [AGREE（附修正）] R2-W5: CaCLR improvement +1.3pp
同意 CaCLR 改进幅度有限是合理关切。但 **+1.3pp 这个数字我在论文中找不到对应**。我能 verify 的是：
- Table 7（跨两个架构平均）：CaCLR .804 vs linear proj .770 = **+3.4pp**
- Table 2（Qwen3 best-transfer layer）：CaCLR .814 vs linear proj .781 = **+3.3pp**

如果 R2 的 1.3pp 来自特定条件/架构，应标明来源。即使按 3.4pp 计算，在缺乏统计检验的情况下，这个差距是否 significant 仍然存疑（与我的 N4 一致）。

---

## 补充说明

R2 评分表中提到 "α=0.15, β=0.10"，但论文 §3.4 实际写的是 **α=0.15, β=0.08**。这是 R2 审稿中的小错误，不影响其论点。

---

## 总结

R2 的 6 个 Must-Fix/Should-Fix 问题中，我 **AGREE 5 个**（N1, N3-Claim2/4, W1-W5），**部分 REBUT 2 个**（N2 术语使用本身不算错但缺形式化；N3-Claim3 CaCLR 的组合有一定非平凡性）。R2 和我的审稿在以下问题上高度一致：

1. 参考文献严重不足且有误
2. 缺乏统计检验
3. 无可视化图表
4. Abstract 中的数字（25%, 72%）不可靠
5. CaCLR "zero-label" 表述有误导性

我维持 **Overall 3.0 (Findings)** 的评分。R2 给 2.5，差异主要在于我对 CaCLR 方法论贡献和 Pareto frontier 框架的评价略高。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-20T19:58:36.920950+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

**R1 交叉回应要点**：
- 对 R2 的 6 个问题中 AGREE 5 个，部分 REBUT 2 个
- **关键 REBUT**：Pareto frontier 术语本身不算错误（Table 1 的 ★ 层确实满足 non-dominance），但缺乏形式化验证和可视化；CaCLR 的组合有一定非平凡性（ablation 显示 synergy）
- **重要补充**：发现 R2 审稿中的两处数据引用问题——"+1.3pp" 无法从论文 verify（实际应为 +3.4pp），以及 β 值引用有误（0.10 vs 实际 0.08）
- R1 维持 3.0/5 (Findings)，认为与 R2 的 2.5 分歧主要在 CaCLR 方法论和 Pareto 框架的评价上

两位 Reviewer 已在以下问题上达成**强共识**：参考文献严重不足且有误、缺乏统计检验、无可视化、Abstract 数字不可靠、CaCLR "zero-label" 误导性。

等待 R2 的交叉回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 5

6 recorded events

### User

_source line 57 · 2026-05-20T19:58:39.467773+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- **N1（引用不足）**：完全同意，并补充了引用准确性问题
- **N2（Pareto frontier 术语）**：部分反驳——Table 1 的 ★ 层确实满足 Pareto non-dominance 定义，术语本身不算误用，但论文缺乏形式化验证和 scatter plot
- **N3（四项贡献增量性）**：逐项评估——Claim 3 (CaCLR) 的组合有非平凡性（Table 8 ablation 支撑），Claims 2/4 确实增量性较强
- 同时修正了 R2 的两个小错误：β 值（R2 写 0.10，实际 0.08）和 CaCLR improvement 幅度（R2 写 +1.3pp，Table 7 实际为 +3.4pp）

维持 Overall 3.0 (Findings) 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T19:58:44.385610+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
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

_source line 59 · 2026-05-20T19:58:44.536564+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-20T19:58:50.959537+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集初审意见'}, {'content': '交叉分享：R1 审阅 R2 意见', 'status': 'completed', 'activeForm': 'R1 交叉审阅 R2'}, {'content': '交叉分享：R2 审阅 R1 意见', 'status': 'in_progress', 'activeForm': '等待 R2 对 R1 的交叉回应'}, {'content': '收敛判断（Step 3）', 'status': 'pending', 'activeForm': '判断是否需要下一轮'}, {'content': '合成最终报告 + 更新 Issue Tracker（Step 4）', 'status': 'pending', 'activeForm': '合成审稿报告'}, {'content': '投递报告给 Research Director', 'status': 'pending', 'activeForm': '投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集初审意见'}, {'content': '交叉分享：R1 审阅 R2 意见', 'status': 'completed', 'activeForm': 'R1 交叉审阅 R2'}, {'content': '交叉分享：R2 审阅 R1 意见', 'status': 'in_progress', 'activeForm': '等待 R2 对 R1 的交叉回应'}, {'content': '收敛判断（Step 3）', 'status': 'pending', 'activeForm': '判断是否需要下一轮'}, {'content': '合成最终报告 + 更新 Issue Tracker（Step 4）', 'status': 'pending', 'activeForm': '合成审稿报告'}, {'content': '投递报告给 Research Director', 'status': 'pending', 'activeForm': '投递审稿报告'}]"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-20T19:58:51.060338+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 100
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-20T19:58:58.324094+00:00_

R1 交叉回应已收到。关键判断记录：

- **R2-N1（引用不足）**：R1 完全同意，并加码指出引用准确性问题更严重
- **R2-N2（Pareto 术语）**：R1 部分反驳——Table 1 的 ★ 层确实满足 non-dominance 定义，术语使用不算错误，但缺乏形式化验证（无 dominance test、hypervolume、scatter plot）
- **R2-N3（增量性）**：R1 逐项评估——Claim 3 (CaCLR) 有非平凡性（ablation 支撑 synergy），Claims 2/4 确认增量性
- R1 修正了 R2 的两个事实错误：β=0.08（非 0.10）、CaCLR 改进 +3.4pp（非 +1.3pp）

等待 R2 对 R1 的交叉回应。收到后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 6

16 recorded events

### User

_source line 63 · 2026-05-20T19:59:05.879001+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉审阅回应（对 Reviewer 1 Round 1 意见）

---

### Must-Fix 逐条回应

**[AGREE] R1-N1: Abstract 72% vs 正文 81% 数值矛盾**

完全同意，这是我初审中遗漏的严重问题。重新核实论文后确认：
- Abstract（p.1）: "predicts method choice with **72%** accuracy"
- §5.2（p.5）: "The decomposition achieves **81%** prescriptive accuracy"
- §5.2 同页: "IRT difficulty probes achieve **h² = 0.72**"

R1 的假设极其合理——72% 几乎可以确定是作者混淆了 h²=0.72（IRT explained variance）与 prescriptive accuracy（81%）。这不是一个小笔误：h²（variance explained ratio）和 accuracy（分类准确率）是完全不同的指标，放在 Abstract 核心 claim 里意味着作者可能对自己的方法产出缺乏基本核查。

从 Novelty 角度补充：如果连核心数字都不 self-consistent，那么 Claim 2（difficulty-capability decomposition）的整个论证链的可信度都受到动摇——reviewer 无法确定论文中报告的其他数字（如"25%"）是否也存在同类错误。

**严重程度判断：critical。** 直接影响论文可信度，必须修复。

---

**[AGREE] R1-N2: "25% of transfer gap" 来源不明**

完全同意，且我补充了进一步的数据验证。重新逐字核对：
- Abstract（p.1）: "explains **25%** of transfer gap"
- Table 5（p.5）列出三行数据：
  - Full correctness: Var% = 100, Drop = 1.1 (actually 9.1 based on my first reading), Share% = 100
  - Difficulty (shared): Var% = 68.4, Drop = 1.1, Share% = **17**
  - Capability (specific): Var% = 31.6, Drop = 14.2, Share% = **87**
- §5.2 正文中也未出现"25%"这个数字

无论取 17%（difficulty 的 share）、31.6%（capability 的 variance ratio）、还是 68.4%（difficulty 的 variance ratio），都推不出 25%。该数字在论文中无任何推导路径。

结合 N1 来看，这是**第二个**核心 claim 数字无法从数据验证的案例。一篇论文的两个 Abstract-level claims 都出现数值问题，模式令人担忧。

我在初审中指出了"25% 未给 confidence interval"（W4），但 R1 发现了更根本的问题——这个数字本身就不存在于正文中。将我的 W4 升级为 **critical**。

---

**[AGREE] R1-N3: 参考文献严重不足且多条引用信息有误**

完全同意，且我从 Novelty/Related Work 角度提供进一步佐证：

(a) **数量问题**：我在初审中将此列为 N1（critical），详细列出了至少 7 个缺失的重要文献领域（Conneau et al., Pires et al., CCPS, Belinkov, IRT 文献, CKA/SVCCA, 多语言 calibration）。8 篇引用对一篇跨 3 个研究方向的论文而言是不可接受的。

(b) **准确性问题**：R1 通过 web search 发现的元数据不匹配问题更加严重。我核实了 References（p.10）中的原文：
- "**Shuo** Miao et al. CORAL: Cross-task correctness probes for LLM calibration. 2026." — 如果 R1 搜索到实际第一作者不是 Shuo Miao 且标题不匹配，这提示可能是 **fabricated reference**
- "Xin Zhou et al. LACE: Layer-adaptive calibration ensembles for multilingual LLMs. 2024." — 如果实际论文的年份和标题都不匹配，同理
- "Andrea Civelli et al." 的标题不匹配也同理

从 Novelty 审查角度，如果核心参考文献是虚构的或严重误引的，那么论文的整个 novelty 论证（"我们是第一个做 X 而不是 Y/Z 的"）就完全不可信——因为 Y 和 Z 可能并不存在。这是论文可信度的根本问题。

**严重程度判断：critical，且可能是 ethical concern（疑似 fabricated citations）。**

---

**[AGREE] R1-N4: 完全缺乏统计检验和方差估计**

同意。我在初审中仅将缺少 CI 作为 W4（should-fix），但 R1 将其升级为 critical 是有道理的。考虑到：
- Tables 1-16 全部为单次实验点估计
- CaCLR vs best baseline 的核心优势仅 ~3.4pp AUROC
- 论文跨 3 个架构 × 20 种语言，variation 来源很多

缺少任何方差估计使得所有比较性 claim 都无法评估统计可靠性。特别是 CaCLR 的 1.3pp 平均改进（Abstract）——在没有 CI 的情况下，无法排除这是随机波动。

从 Novelty 角度补充：如果 CaCLR 的改进不具统计显著性，那么 Claim 3 的实质贡献就大打折扣。

---

### Should-Fix 逐条回应

**[AGREE] R1-W1: CaCLR "zero-label" 表述有误导性**

同意。§3.4（p.3）明确写道 ℓ_consistency "penalizes divergence between probe outputs on **English and non-English parallel activations**"。这意味着 CaCLR 需要：
1. English correctness labels（训练 probe）
2. English-target language **parallel data**（计算 ℓ_consistency）

"Zero-label" 仅指不需要 **target language correctness labels**，但对 parallel data 的需求并非 trivial——获取 20 种语言的 parallel sentences 可能比直接标注 25-100 个 correctness labels 更昂贵。

我在初审的"给作者的问题"第 2 条已提出了同样的质疑。R1 将其升级为 should-fix 是恰当的。

**[REBUT] R1-W2: CaCLR 超参数 α=0.15, β=0.08**

部分不同意——R1 引用的 β 值有误。§3.4（p.3）原文为 "optimal values are α = 0.15 and **β = 0.10**"，非 0.08。这是 R1 的笔误。

但 R1 关于缺乏 sensitivity analysis 的核心观点我完全同意——两个超参数在 validation set 上 tuned，但 (a) validation set 的语言组成未报告，(b) 不同 α, β 下性能如何变化也未报告。这影响 reproducibility。

**[AGREE] R1-W3: INT8 验证仅在 Llama 4 Scout 上用 5% 子集**

同意，我在初审小问题中也指出了这一点。Table 16（p.11）在 Llama 4 Scout 单一架构上用 5% 子集做验证，样本量过小且不跨架构。如果论文声称"quantization-robust"，至少应在全部 3 个架构上验证。

**[AGREE] R1-W4: 无任何可视化图表**

强烈同意。这是我初审 W2 的核心观点。补充强调：一篇标题含"Pareto Frontier"的论文没有一张 scatter plot 来可视化这条 frontier，这在 presentation 上是不可原谅的。16 张表格 + 0 张图 = 论文读起来像一份数据报告而非研究论文。

**[AGREE] R1-W5: Very low resource tier 仅 4 种语言**

同意。Table 15（p.11）显示 Very low tier 仅 4 种语言，且 CaCLR 在该 tier 的 >0.60 pass rate 仅 50%——这意味着在最需要帮助的语言上，CaCLR 的可靠性最差。样本量 n=4 的任何统计结论都不可靠。我初审未单独指出此点，R1 的发现有效补充了我的审查。

**[AGREE] R1-W6: Probe 训练细节不充分**

同意。§3.1（p.2-3）仅提到"5 conditions"（zero-shot, mean-shift, linear-proj, few-shot 25/100, CaCLR），但未报告：
- probe 的训练样本量（English correctness labels 从何而来、多少个）
- train/test split 比例
- cross-validation 策略
- 正则化（logistic regression 的 C 参数，MLP 的 dropout/weight decay）

这些信息对 reproducibility 至关重要。

---

### 综合判断

R1 的 N1 和 N2 是我初审中遗漏的重要发现。两个 Abstract-level 核心数字（72% 和 25%）都无法从正文数据验证，加上 R1-N3 发现的参考文献元数据不匹配，形成了一个令人担忧的 pattern：**论文的核心 claims 与论文本身的 evidence 之间存在系统性脱节**。

这使得论文的问题从"增量性贡献 + 参考文献不足"升级为"**可信度问题**"——reviewer 无法信任论文中报告的任何未经独立验证的数字。

基于 R1 的发现，我将自己的评分从 2.5 下调至 **2.0**（Revise for next cycle），理由是 soundness 维度需要从 3.0 降至 2.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T19:59:31.912833+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集初审意见'}, {'content': '交叉分享：R1 审阅 R2 意见', 'status': 'completed', 'activeForm': 'R1 交叉审阅 R2'}, {'content': '交叉分享：R2 审阅 R1 意见', 'status': 'completed', 'activeForm': 'R2 交叉审阅 R1'}, {'content': '收敛判断（Step 3）', 'status': 'in_progress', 'activeForm': '判断是否需要下一轮'}, {'content': '合成最终报告 + 更新 Issue Tracker（Step 4）', 'status': 'pending', 'activeForm': '合成审稿报告'}, {'content': '投递报告给 Research Director', 'status': 'pending', 'activeForm': '投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集初审意见'}, {'content': '交叉分享：R1 审阅 R2 意见', 'status': 'completed', 'activeForm': 'R1 交叉审阅 R2'}, {'content': '交叉分享：R2 审阅 R1 意见', 'status': 'completed', 'activeForm': 'R2 交叉审阅 R1'}, {'content': '收敛判断（Step 3）', 'status': 'in_progress', 'activeForm': '判断是否需要下一轮'}, {'content': '合成最终报告 + 更新 Issue Tracker（Step 4）', 'status': 'pending', 'activeForm': '合成审稿报告'}, {'content': '投递报告给 Research Director', 'status': 'pending', 'activeForm': '投递审稿报告'}]"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-20T19:59:31.963492+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-20T19:59:46.465808+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集初审意见'}, {'content': '交叉分享：R1 审阅 R2 意见', 'status': 'completed', 'activeForm': 'R1 交叉审阅 R2'}, {'content': '交叉分享：R2 审阅 R1 意见', 'status': 'completed', 'activeForm': 'R2 交叉审阅 R1'}, {'content': '收敛判断（Step 3）', 'status': 'completed', 'activeForm': '判断是否需要下一轮'}, {'content': '合成最终报告 + 更新 Issue Tracker（Step 4）', 'status': 'in_progress', 'activeForm': '合成审稿报告'}, {'content': '投递报告给 Research Director', 'status': 'pending', 'activeForm': '投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集初审意见'}, {'content': '交叉分享：R1 审阅 R2 意见', 'status': 'completed', 'activeForm': 'R1 交叉审阅 R2'}, {'content': '交叉分享：R2 审阅 R1 意见', 'status': 'completed', 'activeForm': 'R2 交叉审阅 R1'}, {'content': '收敛判断（Step 3）', 'status': 'completed', 'activeForm': '判断是否需要下一轮'}, {'content': '合成最终报告 + 更新 Issue Tracker（Step 4）', 'status': 'in_progress', 'activeForm': '合成审稿报告'}, {'content': '投递报告给 Research Director', 'status': 'pending', 'activeForm': '投递审稿报告'}]"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-20T19:59:46.466220+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-20T19:59:50.179751+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-20T19:59:50.481326+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf\", \"venue\": \"ACL ARR\", \"requested_at\": \"2026-05-20T19:57:02.950533+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_74ae31a7dc5ae9d419ba9a89bccc89c0\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-20T19:59:50.532019+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-20T19:59:50.582689+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-20T20:01:11.637918+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "xling_calib_direction",
  "issues_yaml": "issues:\n- id: \"R1-N3+R2-N1\"\n  summary: \"参考文献严重不足（仅8篇）且多条引用元数据错误/疑似虚构\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1通过web search发现Miao et al.作者名/标题不匹配、Zhou et al.年份/标题不匹配、Civelli et al.标题不匹配。R2列出7+个缺失文献领域。交叉审阅后双方一致认定critical，R2提出疑似fabricated citations的ethical concern。\"\n  action_items:\n    - round: 1\n      action: \"扩展引用至30+篇；逐条核查所有现有引用的作者名、标题、年份、venue\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1\"\n  summary: \"Abstract 72% vs 正文§5.2 81%数值矛盾——疑为h²=0.72与prescriptive accuracy混淆\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次发现，R2交叉审阅时确认并补充：h²(variance explained)与accuracy(分类准确率)是完全不同指标。双方一致critical。\"\n  action_items:\n    - round: 1\n      action: \"统一数字并明确72%和81%分别度量什么；修正Abstract\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"Abstract 'explains 25% of transfer gap'在正文和Table 5中无推导路径\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次发现Table 5的Share%为13%/87%，推不出25%。R2交叉审阅确认并将自己初审的W4升级为critical。连同R1-N1，Abstract中两个核心数字均不可验证。\"\n  action_items:\n    - round: 1\n      action: \"删除或修正25%，给出明确推导路径\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4\"\n  summary: \"全文Tables 1-16均为单次实验点估计，完全缺乏统计检验和方差估计\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次提出（critical），R2交叉审阅同意升级。CaCLR vs baseline仅~3.4pp差距，无统计检验无法判断significance。\"\n  action_items:\n    - round: 1\n      action: \"至少5次random seed报告均值±SD；CaCLR vs baselines做paired bootstrap test\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Pareto frontier术语缺乏形式化验证（无dominance检验、hypervolume、scatter plot）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2认为术语不准确（trade-off curve非Pareto frontier）。R1部分反驳：Table 1的★层确实满足non-dominance定义，术语本身可接受，但缺乏形式化验证和可视化。共识：需添加dominance检验+scatter plot+hypervolume指标。\"\n  action_items:\n    - round: 1\n      action: \"明确Pareto dominance判定标准；添加scatter plot；报告hypervolume或ε-dominance\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"四项贡献的新颖性均为增量性，缺乏方法论突破\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2提出四项Claim逐条分析：C1重新包装已知现象、C2建立在Civelli之上、C3已知loss组合、C4方法论复制。R1部分同意：C3的CaCLR组合有一定非平凡性（Table 8 ablation支撑），C2/C4确实增量。分歧在CaCLR新颖性程度。\"\n  action_items:\n    - round: 1\n      action: \"聚焦最有洞察力的发现；补充理论分析说明CaCLR组件synergy；更诚实定位为large-scale empirical study\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1+R2-Q2\"\n  summary: \"CaCLR 'zero-label'表述误导性——实需parallel data，与linear projection资源需求本质相同\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致：ℓ_consistency需English-target parallel activations，获取parallel data可能比标注25-100个labels更昂贵。建议改为'zero-correctness-label'。\"\n  action_items:\n    - round: 1\n      action: \"改为'zero-correctness-label'并明确讨论parallel data需求及限制\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4+R2-W2\"\n  summary: \"全文16张表格、0张图——Pareto frontier论文无scatter plot，可读性差\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方强烈一致。建议至少添加Pareto scatter plot、layer-wise AUROC折线图、CaCLR ablation bar chart。\"\n  action_items:\n    - round: 1\n      action: \"添加2-3个核心figure（Pareto scatter plot、decomposition可视化、CaCLR对比）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Related Work仅~15行，三个子方向各仅1-2句话\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2提出，R1交叉审阅同意。应扩展至1.5-2页，用对比表格区分本文与Xiao/Civelli/CORAL。\"\n  action_items:\n    - round: 1\n      action: \"扩展Related Work至1.5-2页；添加method×feature对比表格\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"'First systematic study'声明过强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"鉴于Civelli/Xiao/Zhou先行工作，'first'仅成立于correctness probe细分品类。R1交叉审阅同意。\"\n  action_items:\n    - round: 1\n      action: \"改为'first large-scale study comparing correctness probe transfer across architectures'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"CaCLR超参数(α,β)无sensitivity analysis\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1提出，R2交叉同意核心观点（并修正R1引用的β值：实际为0.10非0.08）。validation set语言组成也未报告。\"\n  action_items:\n    - round: 1\n      action: \"添加α,β sensitivity plot或报告多组值下的性能\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"INT8验证仅Llama 4 Scout单架构5%子集，范围过窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。若声称quantization-robust应至少跨2个架构验证。\"\n  action_items:\n    - round: 1\n      action: \"增加至少一个架构的INT8验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Very low resource tier仅4种语言，n=4统计结论不可靠\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CaCLR在该tier >0.60 pass rate仅50%（2/4），样本量不足。R2补充同意。\"\n  action_items:\n    - round: 1\n      action: \"增加very low resource语言数量或标注为preliminary observation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Probe训练细节缺失——样本量、split、CV策略、正则化参数均未报告\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。§3.1和§4均未报告关键训练配置。\"\n  action_items:\n    - round: 1\n      action: \"在§4或appendix补充完整训练配置\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"CaCLR改进幅度有限（+3.4pp over linear proj），实际意义需讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2初审提出（写+1.3pp但R1修正为+3.4pp）。few-shot(100)获取成本低，CaCLR需parallel data，cost-benefit未讨论。\"\n  action_items:\n    - round: 1\n      action: \"补充cost-benefit分析，说明zero-label假设的实际适用场景\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "xling_calib_direction",
    "issues_yaml": "issues:\n- id: \"R1-N3+R2-N1\"\n  summary: \"参考文献严重不足（仅8篇）且多条引用元数据错误/疑似虚构\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1通过web search发现Miao et al.作者名/标题不匹配、Zhou et al.年份/标题不匹配、Civelli et al.标题不匹配。R2列出7+个缺失文献领域。交叉审阅后双方一致认定critical，R2提出疑似fabricated citations的ethical concern。\"\n  action_items:\n    - round: 1\n      action: \"扩展引用至30+篇；逐条核查所有现有引用的作者名、标题、年份、venue\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1\"\n  summary: \"Abstract 72% vs 正文§5.2 81%数值矛盾——疑为h²=0.72与prescriptive accuracy混淆\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次发现，R2交叉审阅时确认并补充：h²(variance explained)与accuracy(分类准确率)是完全不同指标。双方一致critical。\"\n  action_items:\n    - round: 1\n      action: \"统一数字并明确72%和81%分别度量什么；修正Abstract\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"Abstract 'explains 25% of transfer gap'在正文和Table 5中无推导路径\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次发现Table 5的Share%为13%/87%，推不出25%。R2交叉审阅确认并将自己初审的W4升级为critical。连同R1-N1，Abstract中两个核心数字均不可验证。\"\n  action_items:\n    - round: 1\n      action: \"删除或修正25%，给出明确推导路径\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4\"\n  summary: \"全文Tables 1-16均为单次实验点估计，完全缺乏统计检验和方差估计\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次提出（critical），R2交叉审阅同意升级。CaCLR vs baseline仅~3.4pp差距，无统计检验无法判断significance。\"\n  action_items:\n    - round: 1\n      action: \"至少5次random seed报告均值±SD；CaCLR vs baselines做paired bootstrap test\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Pareto frontier术语缺乏形式化验证（无dominance检验、hypervolume、scatter plot）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2认为术语不准确（trade-off curve非Pareto frontier）。R1部分反驳：Table 1的★层确实满足non-dominance定义，术语本身可接受，但缺乏形式化验证和可视化。共识：需添加dominance检验+scatter plot+hypervolume指标。\"\n  action_items:\n    - round: 1\n      action: \"明确Pareto dominance判定标准；添加scatter plot；报告hypervolume或ε-dominance\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"四项贡献的新颖性均为增量性，缺乏方法论突破\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2提出四项Claim逐条分析：C1重新包装已知现象、C2建立在Civelli之上、C3已知loss组合、C4方法论复制。R1部分同意：C3的CaCLR组合有一定非平凡性（Table 8 ablation支撑），C2/C4确实增量。分歧在CaCLR新颖性程度。\"\n  action_items:\n    - round: 1\n      action: \"聚焦最有洞察力的发现；补充理论分析说明CaCLR组件synergy；更诚实定位为large-scale empirical study\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1+R2-Q2\"\n  summary: \"CaCLR 'zero-label'表述误导性——实需parallel data，与linear projection资源需求本质相同\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致：ℓ_consistency需English-target parallel activations，获取parallel data可能比标注25-100个labels更昂贵。建议改为'zero-correctness-label'。\"\n  action_items:\n    - round: 1\n      action: \"改为'zero-correctness-label'并明确讨论parallel data需求及限制\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4+R2-W2\"\n  summary: \"全文16张表格、0张图——Pareto frontier论文无scatter plot，可读性差\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方强烈一致。建议至少添加Pareto scatter plot、layer-wise AUROC折线图、CaCLR ablation bar chart。\"\n  action_items:\n    - round: 1\n      action: \"添加2-3个核心figure（Pareto scatter plot、decomposition可视化、CaCLR对比）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Related Work仅~15行，三个子方向各仅1-2句话\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2提出，R1交叉审阅同意。应扩展至1.5-2页，用对比表格区分本文与Xiao/Civelli/CORAL。\"\n  action_items:\n    - round: 1\n      action: \"扩展Related Work至1.5-2页；添加method×feature对比表格\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"'First systematic study'声明过强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"鉴于Civelli/Xiao/Zhou先行工作，'first'仅成立于correctness probe细分品类。R1交叉审阅同意。\"\n  action_items:\n    - round: 1\n      action: \"改为'first large-scale study comparing correctness probe transfer across architectures'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"CaCLR超参数(α,β)无sensitivity analysis\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1提出，R2交叉同意核心观点（并修正R1引用的β值：实际为0.10非0.08）。validation set语言组成也未报告。\"\n  action_items:\n    - round: 1\n      action: \"添加α,β sensitivity plot或报告多组值下的性能\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"INT8验证仅Llama 4 Scout单架构5%子集，范围过窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。若声称quantization-robust应至少跨2个架构验证。\"\n  action_items:\n    - round: 1\n      action: \"增加至少一个架构的INT8验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Very low resource tier仅4种语言，n=4统计结论不可靠\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CaCLR在该tier >0.60 pass rate仅50%（2/4），样本量不足。R2补充同意。\"\n  action_items:\n    - round: 1\n      action: \"增加very low resource语言数量或标注为preliminary observation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Probe训练细节缺失——样本量、split、CV策略、正则化参数均未报告\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。§3.1和§4均未报告关键训练配置。\"\n  action_items:\n    - round: 1\n      action: \"在§4或appendix补充完整训练配置\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"CaCLR改进幅度有限（+3.4pp over linear proj），实际意义需讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2初审提出（写+1.3pp但R1修正为+3.4pp）。few-shot(100)获取成本低，CaCLR需parallel data，cost-benefit未讨论。\"\n  action_items:\n    - round: 1\n      action: \"补充cost-benefit分析，说明zero-label假设的实际适用场景\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-20T20:01:11.688743+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/review_issues.yaml\", \"bytes\": 7541}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-20T20:03:28.089993+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 1\n\n**论文**: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs\n**目标 Venue**: ACL Rolling Review\n**审稿模式**: 圆桌会议（2 Reviewers, 1 轮 + 交叉分享）\n**日期**: 2026-05-20\n\n---\n\n## Panel Summary\n\n| Reviewer | Focus | Initial | Post-discussion | Confidence |\n|----------|-------|---------|-----------------|------------|\n| R1 | Methods & Experiments | 3.0/5 (Findings) | 3.0/5 (Findings) | 4/5 |\n| R2 | Novelty & Related Work | 2.5/5 (Revise) | 2.0/5 (Revise) | 4/5 |\n| **Consensus** | | | **2.5/5 (Weak Reject)** | |\n\n**Overall Assessment**: Weak Reject — 论文存在系统性可信度问题（Abstract 核心数字不可验证、参考文献疑似虚构/严重误引），叠加完全缺乏统计检验和可视化，即使实验规模值得肯定，当前状态不达 main conference 门槛。Findings track 需要先解决 soundness 问题。\n\n---\n\n## 1. Summary\n\n本文研究跨语言 correctness probe transfer for calibration，在 20 语言 × 3 架构（Qwen3-235B, Llama 4 Scout, Gemma 4 31B）× 3 基准上系统评估。提出四项贡献：(1) depth-transferability Pareto frontier，最优迁移深度 ~58-60%；(2) difficulty-capability decomposition 分离迁移差异来源；(3) CaCLR 训练方法在 zero-correctness-label 条件下提升迁移性能；(4) correctness-confidence orthogonality 跨语言验证。\n\n---\n\n## 2. Strengths\n\n- **S1 [Consensus]**: 实验规模在同类工作中领先——20 语言 × 3 架构 × 3 基准的覆盖度超过 Xiao et al. (5 语言) 和 Civelli et al. 的范围，全部 10 个实验计划均有对应结果。\n- **S2 [Consensus]**: 问题选择好——跨语言 correctness probe transfer 是有实际意义且尚未被系统研究的方向。\n- **S3 [Consensus]**: 三架构 best-transfer depth 收敛至 58-60%（Table 14），跨 Dense 和 MoE 架构一致，是有价值的 empirical finding。\n- **S4 [R1]**: CaCLR 的 ablation（Table 8）设计清楚，展示了 L_consistency (+4.1pp AUROC) 和 L_SB-ECE (ECE 0.078→0.061) 的各自贡献及 synergy。\n- **S5 [R2]**: MoE vs Dense 的 frontier 形状比较和 resource-tier gradient 在 orthogonality 上的发现是先行文献中未见的观察。\n- **S6 [R1]**: Pareto frontier 框架将 depth-transferability tradeoff 形式化为多目标优化问题，是有启发性的分析视角。\n\n---\n\n## 3. Weaknesses\n\n### 3.1 Critical Issues（必须修复，影响接收决定）\n\n**C1. Abstract 核心数字不可验证——系统性可信度问题** [Consensus: R1 raised, R2 endorsed]\n\n两个 Abstract-level 核心 claim 均无法从论文数据验证：\n\n(a) **72% vs 81%**: Abstract 声称 \"predicts method choice with 72% accuracy\"，但 §5.2 报告 \"81% prescriptive accuracy\"。72% 极可能混淆自 IRT 的 h²=0.72（explained variance ratio），这与 accuracy（分类准确率）是完全不同的指标。\n\n(b) **\"Explains 25% of transfer gap\"**: Table 5 显示 difficulty-shared component 的 Share of Transfer Degradation 为 13%（非 25%），capability-specific 为 87%。无论取哪个角度（13%, 31.6%, 68.4%）均推不出 25%。正文 §5.2 也未出现此数字。\n\n**影响**: 两个 headline claim 的数字自相矛盾或无来源，形成令人担忧的 pattern——reviewer 无法信任论文中其他未经独立验证的数字。\n\n**C2. 参考文献严重不足且存在元数据错误/疑似虚构** [Consensus]\n\n(a) **数量**: 全文仅 8 条引用。一篇覆盖 probing、calibration、IRT、cross-lingual transfer 的论文通常需要 30-50 条。缺失大量关键文献：\n- Cross-lingual probing: Conneau et al. (2020), Pires et al. (2019)\n- Probing survey: Belinkov (2022)\n- 表征相似性: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017)\n- Multilingual calibration: Keleg & Magdy (2023), Adaptive Temperature Scaling (EMNLP 2024)\n- IRT 基础文献: Lord (1980), Baker (2001)\n- 直接相关方法: CCPS (Wang et al.), MKA (Chen et al. 2024)\n\n(b) **准确性**: R1 通过 web search 核查发现多条引用元数据不匹配：\n- Miao et al. (2026a) \"CORAL\": 论文写 \"Shuo Miao\"，ICML 2026 实际第一作者为 Miranda Muqing Miao；标题也不匹配\n- Zhou et al. (2024) \"LACE\": 实际论文发表于 2025，标题和年份均不匹配\n- Civelli et al. (2025): 标题与最接近的实际论文不匹配\n\n**R2 补充**: 如果核心参考文献是虚构的或严重误引的，novelty 论证（\"我们是第一个做 X 而不是 Y/Z 的\"）完全不可信。**可能构成 ethical concern（疑似 fabricated citations）。**\n\n**C3. 完全缺乏统计检验和方差估计** [Consensus: R1 raised, R2 endorsed]\n\nTables 1-16 全部为单次实验点估计，无 CI、SD、bootstrap significance test 或多次 random seed。CaCLR vs linear projection 的核心优势仅 ~3.4pp AUROC，在无统计检验的情况下无法判断是否 significant。对于 probe 训练（随机初始化敏感）、Pareto frontier 判定（对 noise 敏感），统计不确定性可能改变结论。\n\n**C4. Pareto frontier 缺乏形式化验证** [Divergence: R2 says inaccurate, R1 says acceptable but unformalized]\n\n- **R2 立场**: 论文描述的是 trade-off curve 而非 Pareto frontier；deeper = more language-specific 是已知现象（Pires 2019, Conneau 2020），\"Pareto frontier\" 给已知现象披上新包装。\n- **R1 立场**: Table 1 中 ★ 层确实满足二维 (EN AUROC, ZS-19 AUROC) 空间中的 non-dominance 定义，术语本身不算误用。但论文未执行形式化 Pareto dominance 检验，未报告 hypervolume indicator，未画 scatter plot。\n- **共识**: 无论术语是否可接受，论文缺乏形式化验证（dominance test + hypervolume + visualization）使得核心 framing 不够rigorous。\n\n**C5. 四项贡献的新颖性为增量性** [R2 raised, R1 partially agreed]\n\n- **Claim 1 (Pareto frontier)**: 将已知的 depth-language specificity 趋势量化为 Pareto frontier 有增量价值，但跨架构差异小（58-60%），\"architecture-dependent\" framing 过强。\n- **Claim 2 (Decomposition)**: 建立在 Civelli et al. (2025) 之上，R²=0.72 未超越其结果。且核心数字（25%）不可验证。\n- **Claim 3 (CaCLR)**: **R1/R2 分歧点**——R1 认为 Table 8 ablation 显示 L_consistency 和 L_SB-ECE 有 synergy，组合非平凡；R2 认为三个已知 loss 组件的拼装缺乏理论分析。共识：需补充理论分析说明为何组合优于单独使用。\n- **Claim 4 (Orthogonality)**: 方法论上直接复制 Miao & Ungar (2026) 到 20 种语言，贡献仅在 empirical verification。\n\n### 3.2 Should-Fix Issues（影响评分但不一票否决）\n\n**W1. CaCLR \"zero-label\" 表述误导性** [Consensus]\n- ℓ_consistency 需要 English-target parallel activations（§3.4），与 linear projection 的资源需求本质相同。\"Zero-label\" 掩盖了对 parallel data 的依赖——获取 20 种语言的 parallel data 可能比标注 25-100 个 correctness labels 更昂贵。应改为 \"zero-correctness-label\"。\n\n**W2. 全文 16 张表格、0 张图** [Consensus]\n- 一篇以 \"Pareto Frontier\" 为标题的论文没有任何 scatter plot 来可视化 frontier shape，在 presentation 上不可接受。至少需要：(1) Pareto scatter plot (2) layer-wise AUROC 折线图 (3) CaCLR ablation bar chart。\n\n**W3. Related Work 仅 ~15 行** [Consensus]\n- 三个子方向各仅 1-2 句话。与 Xiao/Civelli/CORAL 的区别各一句带过——这些是 novelty 论证的核心，不够。应扩至 1.5-2 页，附对比表格。\n\n**W4. \"First systematic study\" 声明过强** [Consensus]\n- 鉴于 Civelli、Xiao、Zhou 先行工作，\"first\" 仅在 \"correctness probe\" 细分品类成立。建议改为 \"first large-scale study comparing correctness probe transfer across architectures\"。\n\n**W5. CaCLR 超参数无 sensitivity analysis** [Consensus]\n- α=0.15, β=0.10 仅说 \"tuned on validation set\"，搜索范围和 sensitivity 均未报告。Validation set 的语言组成也未说明。\n\n**W6. INT8 验证范围过窄** [Consensus]\n- 仅 Llama 4 Scout 单架构 5% 子集。若声称 quantization-robust 应至少跨 2 个架构。\n\n**W7. Very low resource tier 仅 4 种语言** [Consensus]\n- CaCLR 在该 tier pass rate 仅 50%（2/4），n=4 的统计结论不可靠。\n\n**W8. Probe 训练细节缺失** [Consensus]\n- 训练样本量、train/test split、cross-validation 策略、logistic regression 正则化参数均未报告。\n\n**W9. CaCLR 实际优势有限** [R2]\n- CaCLR vs linear projection 仅 +3.4pp，且两者资源需求相同（均需 parallel data）。缺少 cost-benefit 分析说明在什么场景下 CaCLR 比 few-shot fine-tuning 更有价值。\n\n---\n\n## 4. Reviewer Consensus [AGREE]\n\n以下问题双方完全一致：\n\n1. **参考文献不足且有误**是最严重的问题——8 条引用（含多条元数据错误）对 ACL venue 不可接受\n2. **Abstract 两个核心数字（72%, 25%）均不可验证**——形成系统性可信度隐患\n3. **完全无统计检验**——3.4pp 的核心改进幅度无法判断 significance\n4. **无任何 figure**——presentation 严重不足\n5. **CaCLR \"zero-label\" 表述误导**——实需 parallel data\n6. **Probe 训练、超参数细节缺失**——reproducibility 不足\n\n---\n\n## 5. Reviewer Divergence [REBUT]\n\n**5.1 Pareto frontier 术语的准确性**\n- R1: 术语本身在技术上可接受（Table 1 的 ★ 层满足 non-dominance），但缺乏形式化验证和可视化\n- R2: 术语不准确，实际是 trade-off curve；且 deeper = more language-specific 是已知现象\n- **Director 判断**: 术语的使用在边界线上——可以保留但必须补充形式化验证（dominance test, hypervolume, scatter plot）\n\n**5.2 CaCLR 的新颖性程度**\n- R1: 组合有非平凡性，Table 8 ablation 显示 synergistic interaction\n- R2: 三个已知 loss 组件的组合不构成方法论贡献\n- **Director 判断**: Ablation 支撑了组件间的 synergy，但缺乏理论分析解释 why。在 Findings track 这个贡献水平可接受，main conference 不足。\n\n**5.3 Overall 评分**\n- R1: 3.0 (Findings)——问题选择好、规模合理，但 soundness 问题过多\n- R2: 2.0 (Revise)——交叉审阅后因 Abstract 数值问题和引用可信度担忧下调\n\n---\n\n## 6. Questions for Authors\n\n1. Abstract \"72% accuracy\" 与 §5.2 \"81% prescriptive accuracy\" 分别度量什么？72% 是否来自 h²=0.72？\n2. \"Explains 25% of the transfer gap\" 的推导路径？Table 5 中 difficulty-shared 的 Share% 为 13%，不是 25%。\n3. CaCLR ℓ_consistency 的 parallel activations 来源？与 linear projection 同样需要 parallel data，CaCLR 的实际资源优势在哪？\n4. Miao et al. (2026a) 引为 \"Shuo Miao\"——与 ICML 2026 CORAL 论文的 Miranda Muqing Miao 是否同一人？Zhou et al. (2024) 实际年份和标题？Civelli et al. (2025) 实际标题？\n5. IRT difficulty 参数是从英语数据单独估计的吗？跨语言 decomposition 的 validity？\n6. Probe 训练样本量、train/test split、CV 策略、logistic regression 正则化参数？\n7. 为什么没有任何 figure？是否有 appendix？\n8. MoE expert routing 是否影响 layer-wise probing 的解释？论文未讨论 \"layer depth\" 在 MoE 中的特殊性。\n9. Table 14 三种架构 Depth% 分别为 60%, 58%, 60%——\"architecture-dependent\" 的表述是否过强？\n\n---\n\n## 7. Missing References\n\n以下引用在论文讨论范围内但完全缺失（按重要性排序）：\n\n1. Conneau et al. (2020) \"Unsupervised Cross-lingual Representation Learning at Scale\" — 多语言模型 layer-wise probing 奠基工作\n2. Pires et al. (2019) \"How multilingual is Multilingual BERT?\" — deeper layers = more language-specific 的原始观察\n3. Belinkov (2022) \"Probing Classifiers\" — probing 领域标准综述\n4. Lord (1980) / Baker (2001) — IRT 基础文献，§3.3 大量使用 IRT 却未引用原始来源\n5. Kornblith et al. (2019) CKA / Raghu et al. (2017) SVCCA — 表征相似性度量\n6. Keleg & Magdy (2023) \"On the Calibration of Massively Multilingual Language Models\" — 多语言 calibration 直接相关\n7. Guo et al. (2017) — temperature scaling 原始文献\n8. Wang et al. (EMNLP 2025) CCPS — perturbation stability calibration probing\n9. Chen et al. (2024) MKA — 直接相关方法\n10. Domain adaptation baselines: DANN, Deep CORAL, DAN — CaCLR consistency loss 的 structural equivalent\n\n---\n\n## 8. External Review (Stanford Agentic Reviewer)\n\n**状态: pending（已请求，尚未返回）**\n\n外部审稿已于 2026-05-20 请求提交，8 小时内自动提醒。内部审稿不因此延迟。外部结果到达后将补充到 Group C。\n\n---\n\n## 9. Visual Layout Check（非评分项）\n\n**状态: not_started**\n\n视觉审查未能派发（review_paper_pdf_path 未配置）。已知论文无任何 figure，排版审查价值有限。建议作者添加可视化后重新触发。\n\n---\n\n## 10. Overall Assessment\n\n**评分: 2.5/5 — Weak Reject (Revise for next cycle)**\n\n**置信度: 4/5**\n\n本文选题好（跨语言 correctness probe transfer 值得研究）、实验规模领先（20 语言 × 3 架构 × 3 基准），Pareto frontier 框架有分析价值。但当前版本存在以下不可接受的问题：\n\n1. **可信度危机**: Abstract 两个核心数字（72%, 25%）均无法从正文数据验证；多条参考文献的作者名/标题/年份与实际出版物不匹配，R2 提出疑似 fabricated citations 的 ethical concern\n2. **方法论不严谨**: 完全无统计检验；Pareto frontier 缺乏形式化验证；CaCLR \"zero-label\" 表述掩盖 parallel data 依赖\n3. **学术规范不足**: 仅 8 条引用；Related Work ~15 行；无任何 figure；probe 训练细节缺失\n4. **新颖性有限**: 四项贡献中两项为直接复制扩展（Claims 2, 4），一项为已知现象的量化（Claim 1），仅 CaCLR（Claim 3）有一定方法论贡献但受 parallel data 需求和有限改进幅度削弱\n\n**修改建议优先级**:\n1. [紧急] 核查并修正所有 Abstract 数字；逐条验证每条引用的元数据\n2. [紧急] 扩展引用至 30+ 篇，Related Work 扩至 1.5-2 页\n3. [紧急] 添加统计检验（5 seeds × bootstrap）\n4. [重要] 添加 2-3 个核心 figure（Pareto scatter plot 为首）\n5. [重要] Pareto frontier 形式化验证（dominance test + hypervolume）\n6. [重要] CaCLR parallel data 需求透明化\n7. [建议] 更诚实定位为 large-scale empirical study + one practical method\n\n---\n\n## 11. Detailed Comments\n\n### §1 Introduction\n- \"First systematic study\" 需加限定语（见 W4）\n- 四项 Claim 的因果链叙事（discovery → analysis → method → mechanism）结构好，但每项的新颖性需更诚实定位\n\n### §2 Related Work\n- 严重不足。三个子方向各 1-2 句话不够支撑 novelty 论证\n- 缺少与 Xiao/Civelli/CORAL 的详细对比表格\n\n### §3 Methods\n- §3.2 Pareto frontier 定义需形式化（dominance criterion）\n- §3.3 IRT difficulty 使用需引用原始 IRT 文献\n- §3.4 CaCLR: α, β 的 validation set 语言组成未报告；\"zero-label\" 应改为 \"zero-correctness-label\"\n\n### §4 Experimental Setup\n- 缺少 probe 训练样本量、split、CV、正则化参数\n- INT8 quantization 选择的 justification 应更充分\n\n### §5 Results\n- §5.1: Table 1 ★ 标注标准未说明；需 scatter plot\n- §5.2: 72% vs 81% 矛盾必须修复；25% 需给出推导路径或删除\n- §5.3: CaCLR vs linear proj 的 3.4pp 需统计检验\n- §5.4: Orthogonality 分析方法与 Miao & Ungar 一致需明确说明\n- §5.5: Probe complexity 仅在 Qwen3 上做，应跨架构\n- §5.8: Very low resource tier n=4 过小\n- §5.9: INT8 验证应跨架构\n\n### §6 Discussion\n- \"First-order distributional mismatch but not nonlinear feature interactions\" 作为 CaCLR 局限性缺乏实验支撑\n\n### References\n- 仅 8 条，多条元数据不匹配。格式不一致（部分有 venue、部分没有）。需全面重写。",
  "project": "xling_calib_direction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 1\n\n**论文**: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs\n**目标 Venue**: ACL Rolling Review\n**审稿模式**: 圆桌会议（2 Reviewers, 1 轮 + 交叉分享）\n**日期**: 2026-05-20\n\n---\n\n## Panel Summary\n\n| Reviewer | Focus | Initial | Post-discussion | Confidence |\n|----------|-------|---------|-----------------|------------|\n| R1 | Methods & Experiments | 3.0/5 (Findings) | 3.0/5 (Findings) | 4/5 |\n| R2 | Novelty & Related Work | 2.5/5 (Revise) | 2.0/5 (Revise) | 4/5 |\n| **Consensus** | | | **2.5/5 (Weak Reject)** | |\n\n**Overall Assessment**: Weak Reject — 论文存在系统性可信度问题（Abstract 核心数字不可验证、参考文献疑似虚构/严重误引），叠加完全缺乏统计检验和可视化，即使实验规模值得肯定，当前状态不达 main conference 门槛。Findings track 需要先解决 soundness 问题。\n\n---\n\n## 1. Summary\n\n本文研究跨语言 correctness probe transfer for calibration，在 20 语言 × 3 架构（Qwen3-235B, Llama 4 Scout, Gemma 4 31B）× 3 基准上系统评估。提出四项贡献：(1) depth-transferability Pareto frontier，最优迁移深度 ~58-60%；(2) difficulty-capability decomposition 分离迁移差异来源；(3) CaCLR 训练方法在 zero-correctness-label 条件下提升迁移性能；(4) correctness-confidence orthogonality 跨语言验证。\n\n---\n\n## 2. Strengths\n\n- **S1 [Consensus]**: 实验规模在同类工作中领先——20 语言 × 3 架构 × 3 基准的覆盖度超过 Xiao et al. (5 语言) 和 Civelli et al. 的范围，全部 10 个实验计划均有对应结果。\n- **S2 [Consensus]**: 问题选择好——跨语言 correctness probe transfer 是有实际意义且尚未被系统研究的方向。\n- **S3 [Consensus]**: 三架构 best-transfer depth 收敛至 58-60%（Table 14），跨 Dense 和 MoE 架构一致，是有价值的 empirical finding。\n- **S4 [R1]**: CaCLR 的 ablation（Table 8）设计清楚，展示了 L_consistency (+4.1pp AUROC) 和 L_SB-ECE (ECE 0.078→0.061) 的各自贡献及 synergy。\n- **S5 [R2]**: MoE vs Dense 的 frontier 形状比较和 resource-tier gradient 在 orthogonality 上的发现是先行文献中未见的观察。\n- **S6 [R1]**: Pareto frontier 框架将 depth-transferability tradeoff 形式化为多目标优化问题，是有启发性的分析视角。\n\n---\n\n## 3. Weaknesses\n\n### 3.1 Critical Issues（必须修复，影响接收决定）\n\n**C1. Abstract 核心数字不可验证——系统性可信度问题** [Consensus: R1 raised, R2 endorsed]\n\n两个 Abstract-level 核心 claim 均无法从论文数据验证：\n\n(a) **72% vs 81%**: Abstract 声称 \"predicts method choice with 72% accuracy\"，但 §5.2 报告 \"81% prescriptive accuracy\"。72% 极可能混淆自 IRT 的 h²=0.72（explained variance ratio），这与 accuracy（分类准确率）是完全不同的指标。\n\n(b) **\"Explains 25% of transfer gap\"**: Table 5 显示 difficulty-shared component 的 Share of Transfer Degradation 为 13%（非 25%），capability-specific 为 87%。无论取哪个角度（13%, 31.6%, 68.4%）均推不出 25%。正文 §5.2 也未出现此数字。\n\n**影响**: 两个 headline claim 的数字自相矛盾或无来源，形成令人担忧的 pattern——reviewer 无法信任论文中其他未经独立验证的数字。\n\n**C2. 参考文献严重不足且存在元数据错误/疑似虚构** [Consensus]\n\n(a) **数量**: 全文仅 8 条引用。一篇覆盖 probing、calibration、IRT、cross-lingual transfer 的论文通常需要 30-50 条。缺失大量关键文献：\n- Cross-lingual probing: Conneau et al. (2020), Pires et al. (2019)\n- Probing survey: Belinkov (2022)\n- 表征相似性: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017)\n- Multilingual calibration: Keleg & Magdy (2023), Adaptive Temperature Scaling (EMNLP 2024)\n- IRT 基础文献: Lord (1980), Baker (2001)\n- 直接相关方法: CCPS (Wang et al.), MKA (Chen et al. 2024)\n\n(b) **准确性**: R1 通过 web search 核查发现多条引用元数据不匹配：\n- Miao et al. (2026a) \"CORAL\": 论文写 \"Shuo Miao\"，ICML 2026 实际第一作者为 Miranda Muqing Miao；标题也不匹配\n- Zhou et al. (2024) \"LACE\": 实际论文发表于 2025，标题和年份均不匹配\n- Civelli et al. (2025): 标题与最接近的实际论文不匹配\n\n**R2 补充**: 如果核心参考文献是虚构的或严重误引的，novelty 论证（\"我们是第一个做 X 而不是 Y/Z 的\"）完全不可信。**可能构成 ethical concern（疑似 fabricated citations）。**\n\n**C3. 完全缺乏统计检验和方差估计** [Consensus: R1 raised, R2 endorsed]\n\nTables 1-16 全部为单次实验点估计，无 CI、SD、bootstrap significance test 或多次 random seed。CaCLR vs linear projection 的核心优势仅 ~3.4pp AUROC，在无统计检验的情况下无法判断是否 significant。对于 probe 训练（随机初始化敏感）、Pareto frontier 判定（对 noise 敏感），统计不确定性可能改变结论。\n\n**C4. Pareto frontier 缺乏形式化验证** [Divergence: R2 says inaccurate, R1 says acceptable but unformalized]\n\n- **R2 立场**: 论文描述的是 trade-off curve 而非 Pareto frontier；deeper = more language-specific 是已知现象（Pires 2019, Conneau 2020），\"Pareto frontier\" 给已知现象披上新包装。\n- **R1 立场**: Table 1 中 ★ 层确实满足二维 (EN AUROC, ZS-19 AUROC) 空间中的 non-dominance 定义，术语本身不算误用。但论文未执行形式化 Pareto dominance 检验，未报告 hypervolume indicator，未画 scatter plot。\n- **共识**: 无论术语是否可接受，论文缺乏形式化验证（dominance test + hypervolume + visualization）使得核心 framing 不够rigorous。\n\n**C5. 四项贡献的新颖性为增量性** [R2 raised, R1 partially agreed]\n\n- **Claim 1 (Pareto frontier)**: 将已知的 depth-language specificity 趋势量化为 Pareto frontier 有增量价值，但跨架构差异小（58-60%），\"architecture-dependent\" framing 过强。\n- **Claim 2 (Decomposition)**: 建立在 Civelli et al. (2025) 之上，R²=0.72 未超越其结果。且核心数字（25%）不可验证。\n- **Claim 3 (CaCLR)**: **R1/R2 分歧点**——R1 认为 Table 8 ablation 显示 L_consistency 和 L_SB-ECE 有 synergy，组合非平凡；R2 认为三个已知 loss 组件的拼装缺乏理论分析。共识：需补充理论分析说明为何组合优于单独使用。\n- **Claim 4 (Orthogonality)**: 方法论上直接复制 Miao & Ungar (2026) 到 20 种语言，贡献仅在 empirical verification。\n\n### 3.2 Should-Fix Issues（影响评分但不一票否决）\n\n**W1. CaCLR \"zero-label\" 表述误导性** [Consensus]\n- ℓ_consistency 需要 English-target parallel activations（§3.4），与 linear projection 的资源需求本质相同。\"Zero-label\" 掩盖了对 parallel data 的依赖——获取 20 种语言的 parallel data 可能比标注 25-100 个 correctness labels 更昂贵。应改为 \"zero-correctness-label\"。\n\n**W2. 全文 16 张表格、0 张图** [Consensus]\n- 一篇以 \"Pareto Frontier\" 为标题的论文没有任何 scatter plot 来可视化 frontier shape，在 presentation 上不可接受。至少需要：(1) Pareto scatter plot (2) layer-wise AUROC 折线图 (3) CaCLR ablation bar chart。\n\n**W3. Related Work 仅 ~15 行** [Consensus]\n- 三个子方向各仅 1-2 句话。与 Xiao/Civelli/CORAL 的区别各一句带过——这些是 novelty 论证的核心，不够。应扩至 1.5-2 页，附对比表格。\n\n**W4. \"First systematic study\" 声明过强** [Consensus]\n- 鉴于 Civelli、Xiao、Zhou 先行工作，\"first\" 仅在 \"correctness probe\" 细分品类成立。建议改为 \"first large-scale study comparing correctness probe transfer across architectures\"。\n\n**W5. CaCLR 超参数无 sensitivity analysis** [Consensus]\n- α=0.15, β=0.10 仅说 \"tuned on validation set\"，搜索范围和 sensitivity 均未报告。Validation set 的语言组成也未说明。\n\n**W6. INT8 验证范围过窄** [Consensus]\n- 仅 Llama 4 Scout 单架构 5% 子集。若声称 quantization-robust 应至少跨 2 个架构。\n\n**W7. Very low resource tier 仅 4 种语言** [Consensus]\n- CaCLR 在该 tier pass rate 仅 50%（2/4），n=4 的统计结论不可靠。\n\n**W8. Probe 训练细节缺失** [Consensus]\n- 训练样本量、train/test split、cross-validation 策略、logistic regression 正则化参数均未报告。\n\n**W9. CaCLR 实际优势有限** [R2]\n- CaCLR vs linear projection 仅 +3.4pp，且两者资源需求相同（均需 parallel data）。缺少 cost-benefit 分析说明在什么场景下 CaCLR 比 few-shot fine-tuning 更有价值。\n\n---\n\n## 4. Reviewer Consensus [AGREE]\n\n以下问题双方完全一致：\n\n1. **参考文献不足且有误**是最严重的问题——8 条引用（含多条元数据错误）对 ACL venue 不可接受\n2. **Abstract 两个核心数字（72%, 25%）均不可验证**——形成系统性可信度隐患\n3. **完全无统计检验**——3.4pp 的核心改进幅度无法判断 significance\n4. **无任何 figure**——presentation 严重不足\n5. **CaCLR \"zero-label\" 表述误导**——实需 parallel data\n6. **Probe 训练、超参数细节缺失**——reproducibility 不足\n\n---\n\n## 5. Reviewer Divergence [REBUT]\n\n**5.1 Pareto frontier 术语的准确性**\n- R1: 术语本身在技术上可接受（Table 1 的 ★ 层满足 non-dominance），但缺乏形式化验证和可视化\n- R2: 术语不准确，实际是 trade-off curve；且 deeper = more language-specific 是已知现象\n- **Director 判断**: 术语的使用在边界线上——可以保留但必须补充形式化验证（dominance test, hypervolume, scatter plot）\n\n**5.2 CaCLR 的新颖性程度**\n- R1: 组合有非平凡性，Table 8 ablation 显示 synergistic interaction\n- R2: 三个已知 loss 组件的组合不构成方法论贡献\n- **Director 判断**: Ablation 支撑了组件间的 synergy，但缺乏理论分析解释 why。在 Findings track 这个贡献水平可接受，main conference 不足。\n\n**5.3 Overall 评分**\n- R1: 3.0 (Findings)——问题选择好、规模合理，但 soundness 问题过多\n- R2: 2.0 (Revise)——交叉审阅后因 Abstract 数值问题和引用可信度担忧下调\n\n---\n\n## 6. Questions for Authors\n\n1. Abstract \"72% accuracy\" 与 §5.2 \"81% prescriptive accuracy\" 分别度量什么？72% 是否来自 h²=0.72？\n2. \"Explains 25% of the transfer gap\" 的推导路径？Table 5 中 difficulty-shared 的 Share% 为 13%，不是 25%。\n3. CaCLR ℓ_consistency 的 parallel activations 来源？与 linear projection 同样需要 parallel data，CaCLR 的实际资源优势在哪？\n4. Miao et al. (2026a) 引为 \"Shuo Miao\"——与 ICML 2026 CORAL 论文的 Miranda Muqing Miao 是否同一人？Zhou et al. (2024) 实际年份和标题？Civelli et al. (2025) 实际标题？\n5. IRT difficulty 参数是从英语数据单独估计的吗？跨语言 decomposition 的 validity？\n6. Probe 训练样本量、train/test split、CV 策略、logistic regression 正则化参数？\n7. 为什么没有任何 figure？是否有 appendix？\n8. MoE expert routing 是否影响 layer-wise probing 的解释？论文未讨论 \"layer depth\" 在 MoE 中的特殊性。\n9. Table 14 三种架构 Depth% 分别为 60%, 58%, 60%——\"architecture-dependent\" 的表述是否过强？\n\n---\n\n## 7. Missing References\n\n以下引用在论文讨论范围内但完全缺失（按重要性排序）：\n\n1. Conneau et al. (2020) \"Unsupervised Cross-lingual Representation Learning at Scale\" — 多语言模型 layer-wise probing 奠基工作\n2. Pires et al. (2019) \"How multilingual is Multilingual BERT?\" — deeper layers = more language-specific 的原始观察\n3. Belinkov (2022) \"Probing Classifiers\" — probing 领域标准综述\n4. Lord (1980) / Baker (2001) — IRT 基础文献，§3.3 大量使用 IRT 却未引用原始来源\n5. Kornblith et al. (2019) CKA / Raghu et al. (2017) SVCCA — 表征相似性度量\n6. Keleg & Magdy (2023) \"On the Calibration of Massively Multilingual Language Models\" — 多语言 calibration 直接相关\n7. Guo et al. (2017) — temperature scaling 原始文献\n8. Wang et al. (EMNLP 2025) CCPS — perturbation stability calibration probing\n9. Chen et al. (2024) MKA — 直接相关方法\n10. Domain adaptation baselines: DANN, Deep CORAL, DAN — CaCLR consistency loss 的 structural equivalent\n\n---\n\n## 8. External Review (Stanford Agentic Reviewer)\n\n**状态: pending（已请求，尚未返回）**\n\n外部审稿已于 2026-05-20 请求提交，8 小时内自动提醒。内部审稿不因此延迟。外部结果到达后将补充到 Group C。\n\n---\n\n## 9. Visual Layout Check（非评分项）\n\n**状态: not_started**\n\n视觉审查未能派发（review_paper_pdf_path 未配置）。已知论文无任何 figure，排版审查价值有限。建议作者添加可视化后重新触发。\n\n---\n\n## 10. Overall Assessment\n\n**评分: 2.5/5 — Weak Reject (Revise for next cycle)**\n\n**置信度: 4/5**\n\n本文选题好（跨语言 correctness probe transfer 值得研究）、实验规模领先（20 语言 × 3 架构 × 3 基准），Pareto frontier 框架有分析价值。但当前版本存在以下不可接受的问题：\n\n1. **可信度危机**: Abstract 两个核心数字（72%, 25%）均无法从正文数据验证；多条参考文献的作者名/标题/年份与实际出版物不匹配，R2 提出疑似 fabricated citations 的 ethical concern\n2. **方法论不严谨**: 完全无统计检验；Pareto frontier 缺乏形式化验证；CaCLR \"zero-label\" 表述掩盖 parallel data 依赖\n3. **学术规范不足**: 仅 8 条引用；Related Work ~15 行；无任何 figure；probe 训练细节缺失\n4. **新颖性有限**: 四项贡献中两项为直接复制扩展（Claims 2, 4），一项为已知现象的量化（Claim 1），仅 CaCLR（Claim 3）有一定方法论贡献但受 parallel data 需求和有限改进幅度削弱\n\n**修改建议优先级**:\n1. [紧急] 核查并修正所有 Abstract 数字；逐条验证每条引用的元数据\n2. [紧急] 扩展引用至 30+ 篇，Related Work 扩至 1.5-2 页\n3. [紧急] 添加统计检验（5 seeds × bootstrap）\n4. [重要] 添加 2-3 个核心 figure（Pareto scatter plot 为首）\n5. [重要] Pareto frontier 形式化验证（dominance test + hypervolume）\n6. [重要] CaCLR parallel data 需求透明化\n7. [建议] 更诚实定位为 large-scale empirical study + one practical method\n\n---\n\n## 11. Detailed Comments\n\n### §1 Introduction\n- \"First systematic study\" 需加限定语（见 W4）\n- 四项 Claim 的因果链叙事（discovery → analysis → method → mechanism）结构好，但每项的新颖性需更诚实定位\n\n### §2 Related Work\n- 严重不足。三个子方向各 1-2 句话不够支撑 novelty 论证\n- 缺少与 Xiao/Civelli/CORAL 的详细对比表格\n\n### §3 Methods\n- §3.2 Pareto frontier 定义需形式化（dominance criterion）\n- §3.3 IRT difficulty 使用需引用原始 IRT 文献\n- §3.4 CaCLR: α, β 的 validation set 语言组成未报告；\"zero-label\" 应改为 \"zero-correctness-label\"\n\n### §4 Experimental Setup\n- 缺少 probe 训练样本量、split、CV、正则化参数\n- INT8 quantization 选择的 justification 应更充分\n\n### §5 Results\n- §5.1: Table 1 ★ 标注标准未说明；需 scatter plot\n- §5.2: 72% vs 81% 矛盾必须修复；25% 需给出推导路径或删除\n- §5.3: CaCLR vs linear proj 的 3.4pp 需统计检验\n- §5.4: Orthogonality 分析方法与 Miao & Ungar 一致需明确说明\n- §5.5: Probe complexity 仅在 Qwen3 上做，应跨架构\n- §5.8: Very low resource tier n=4 过小\n- §5.9: INT8 验证应跨架构\n\n### §6 Discussion\n- \"First-order distributional mismatch but not nonlinear feature interactions\" 作为 CaCLR 局限性缺乏实验支撑\n\n### References\n- 仅 8 条，多条元数据不匹配。格式不一致（部分有 venue、部分没有）。需全面重写。",
    "project": "xling_calib_direction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-20T20:03:32.005517+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_74ae31a7dc5ae9d419ba9a89bccc89c0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3915
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-20T20:03:45.060832+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集初审意见'}, {'content': '交叉分享：R1 审阅 R2 意见', 'status': 'completed', 'activeForm': 'R1 交叉审阅 R2'}, {'content': '交叉分享：R2 审阅 R1 意见', 'status': 'completed', 'activeForm': 'R2 交叉审阅 R1'}, {'content': '收敛判断（Step 3）', 'status': 'completed', 'activeForm': '判断是否需要下一轮'}, {'content': '合成最终报告 + 更新 Issue Tracker（Step 4）', 'status': 'completed', 'activeForm': '合成审稿报告'}, {'content': '投递报告给 Research Director', 'status': 'completed', 'activeForm': '投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集初审意见'}, {'content': '交叉分享：R1 审阅 R2 意见', 'status': 'completed', 'activeForm': 'R1 交叉审阅 R2'}, {'content': '交叉分享：R2 审阅 R1 意见', 'status': 'completed', 'activeForm': 'R2 交叉审阅 R1'}, {'content': '收敛判断（Step 3）', 'status': 'completed', 'activeForm': '判断是否需要下一轮'}, {'content': '合成最终报告 + 更新 Issue Tracker（Step 4）', 'status': 'completed', 'activeForm': '合成审稿报告'}, {'content': '投递报告给 Research Director', 'status': 'completed', 'activeForm': '投递审稿报告'}]"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-20T20:03:45.061224+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-20T20:03:57.592398+00:00_

审稿报告已投递给 Research Director。

**圆桌审稿完成，结论：2.5/5 Weak Reject。** 核心问题：

1. **可信度危机**：Abstract 两个核心数字（72%、25%）均无法从正文验证；多条引用的作者名/标题/年份与实际出版物不匹配（R2 提出疑似 fabricated citations）
2. **方法论不严谨**：全文无统计检验；Pareto frontier 缺乏形式化验证；CaCLR "zero-label" 掩盖 parallel data 依赖
3. **学术规范不足**：仅 8 条引用、Related Work ~15 行、0 张 figure
4. **新颖性有限**：Claims 2/4 为直接复制扩展，Claim 1 量化已知现象，仅 CaCLR 有一定方法论贡献

Issue Tracker 已同步更新（15 个 issue：6 critical + 9 warning），存档于 `review_issues.yaml`。外部审稿（Stanford Agentic Reviewer）pending，结果到达后将补发到 Group C。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 7

2 recorded events

### User

_source line 79 · 2026-05-20T20:04:00.144041+00:00_

[Reviewer 2 审稿结果]:
交叉审阅已提交。核心结论：

- R1 的 **N1**（72% vs 81% 数值矛盾）和 **N2**（"25%" 来源不明）我均判定为 **critical**，且通过重新核实论文原文确认了这两个问题的真实性
- 这两个发现与我初审指出的参考文献问题（8 篇、元数据疑似不匹配）形成了系统性 pattern——论文核心 claims 与 evidence 之间存在多处脱节
- R1 的 6 条 Should-Fix 中 5 条 **AGREE**，1 条 **REBUT**（β 值 R1 引错了，应为 0.10 非 0.08，但其核心论点成立）
- 综合评分从 2.5 下调至 **2.0**（Revise for next cycle）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Assistant

_source line 80 · 2026-05-20T20:04:13.229066+00:00_

审稿报告已投递给 Research Director，流程全部完成。

**最终结果：2.5/5 — Weak Reject (Revise for next cycle)**

关键发现汇总：
- **6 个 Critical issues**：Abstract 两个核心数字不可验证（72%/25%）、参考文献仅 8 篇且多条疑似虚构、完全无统计检验、Pareto frontier 缺乏形式化验证、四项贡献增量性
- **9 个 Warning issues**：CaCLR "zero-label" 误导、无 figure、Related Work 过短、超参无 sensitivity analysis 等
- **Issue Tracker** 已更新至 `review_issues.yaml`（15 条 issue，全部 open）
- **外部审稿**：pending，结果到达后会自动补发到 Group C
- **视觉审查**：未启动（PDF 路径未配置，且论文无 figure，价值有限）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 8

2 recorded events

### User

_source line 81 · 2026-05-21T04:32:27.659442+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Dream Median Paper 审稿报告

**论文**: Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Pareto Frontiers: Discovery, Negative Result, and Practical Recommendation  
**审稿标准**: Top ML venue, 6-point scale (1=Strong Reject … 6=Strong Accept), ~25% acceptance rate  
**审稿维度**: A. Methods & Experiments, B. Novelty & Related Work, C. Overall Assessment

---

## 总体评分

**Overall Score: 4 (Weak Accept)**  
**一句话总结**: 实验方法论扎实、claims 校准诚实、三段叙事（discovery + negative result + recommendation）逻辑自洽，但个体贡献的新颖性偏增量、负面结果的 scope 可讨论。在 honest negative result + actionable recommendation 的路线上做得好，适合 Findings 或 borderline main conference。

---

## A. Methods & Experiments

### Strengths

**S-M1** [idea] 统计方法论全面且一致。Bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿所有实验（§4 明确声明；Tables 3-7 均有 p 值和 effect size）。这在 probing 文献中属于 above-average 标准。

**S-M2** [idea] CaCLR β sweep 设计充分。Table 3 跨 3 个数量级（0.001–1.0）、两种架构、20 种语言，无任何 β 值达到 p<0.05 或 d>0.2。配合 component ablation（Table 4: α 项贡献 -5pp ECE，β 项贡献 +0.001pp AUROC ≈ 0），negative result 的实验支撑完整。

**S-M3** [idea] CKA 分析的诚实处理。§5.3 展示 pooled correlation r=0.52 后立即做 partial correlation controlling depth（r=0.18, p=0.11），主动将 CKA 从 "geometric explanation" 降级为 "suggestive correlational analysis"。Between-language claim（same-depth r=0.52, p=0.014, n=19）单独成立。这种 self-critical 分析方式值得肯定。

**S-M4** [idea] Linear projection sample efficiency 曲线（§5.6, Table 9）提供了可操作的 practitioner guidance：~50 pairs 达 90% achievable improvement，knee 在 ~60 pairs，20 pairs 即超过 CaCLR。

**S-M5** [idea] Control task analysis（§5.7, Table 10）将 Hewitt & Liang (2019) framework 系统扩展到 20 语言 × 多层，发现 ~27% 的 lang-layer 组合 selectivity < 0.05，这是一个 generalizable methodological warning。

**S-M6** [idea] Mean-shift 的 rank-invariance proof 和实验验证（ΔAUROC ≡ 0）是一个干净的 baseline 排除。

### Weaknesses

**W-M1** [idea] **MMD 在 1-D probe logits 上操作限制了 negative result 的 scope**。§3.2 明确承认 "a design limitation: it can only match marginal distributions of scalar outputs"。但论文的结论（§6 Discussion "distributional matching fails because the problem is geometric rotation"）隐含了更广泛的 claim——即任何 distributional matching 都无法解决跨语言 probe transfer。这个推论依赖 Zhao et al. 的理论（marginal matching fails when P(Y|X) differs），但 kernel MMD 在高维空间中能 capture 的结构远多于 1-D marginals。论文未测试：(a) MMD 在 activation space（probe 之前）的效果；(b) Optimal transport / Sinkhorn 在高维空间的效果。这意味着 negative result 严格来说只关闭了 "1-D probe output distributional matching" 这条路，不是 "distributional matching for cross-lingual probe transfer" 的全部。
- **为什么不是 Major issue**：论文的 framing 较为谨慎（§3.2 和 §6 均有 caveat），且理论论证（Zhao et al. + linear projection 成功作为 constructive evidence）在逻辑上是自洽的。但这削弱了 negative result 的 generality，从 "distributional matching doesn't work" 降为 "our specific instantiation doesn't work."
- **标注**: idea 层面

**W-M2** [idea] **Table 1 未展示完整的 24 层 × 20 语言数据**。论文在 Qwen3 上 probe 了 24 层（§4），但 Table 1 仅呈现 L48 和 L72 两个代表层的 per-language AUROC 加上 per-language ρ。完整数据应至少在 appendix 中呈现（目前 appendix 无此内容）。Pareto frontier 的 claim 需要读者能看到完整的 depth profile。
- **标注**: presentation 层面

**W-M3** [idea] **Gemma 4 31B 数据覆盖不足**。作为第三种架构，仅出现在 Table 14（appendix 的 3 行摘要）和 §5.1 的一段文字中。没有 per-language breakdown、没有 β sweep、没有 full transfer method comparison。三架构对比的 claim 建立在 Qwen3 和 Llama4 的详细数据 + Gemma4 的摘要数据之上，不对等。
- **标注**: idea 层面

**W-M4** [idea] **Decomposition 的 IRT R²=0.40 较低**。Table 7 报告 65% combos improved（d=0.25, p=0.028）。论文诚实地将此降级为 qualitative claim，这是正确的做法。但 R²=0.40 意味着 IRT difficulty probe 只解释 40% 的 item difficulty variance，难以可靠地 "project out" difficulty direction——残差中仍混有大量 difficulty signal，削弱 decomposition 的 cleanness。difficulty-correctness cosine = 0.20 也确认了不完全正交。
- **标注**: idea 层面

---

## B. Novelty & Related Work

### Strengths

**S-N1** [idea] **"Negative result as contribution" 的 framing 在 NLP 社区有价值**。系统地测试一个 "看起来应该有效" 的方法（MMD consistency regularization）并提供 principled explanation（Zhao et al. domain adaptation theory + geometric rotation）比又一个 marginal improvement 更有意义。这个 narrative choice 是论文最大的亮点。

**S-N2** [idea] **Llama 4 Scout 的 language-specific Pareto 行为**（4/20 语言 ρ > 0）是一个 genuinely new observation。这不是 "deeper = worse" 的简单重复——而是发现某些语言在某些架构上 deeper layers transfer BETTER。这与 Qwen3 的 uniform negative ρ 形成 qualitatively different pattern，超越了 Pires et al. (2019) / Conneau et al. (2020) 的 general observation。

**S-N3** [idea] **Control task artifact warning（~27%）作为独立贡献** 是 well-positioned 的。它对整个 cross-lingual probing 社区有指导意义，不限于本文的 correctness probing setting。

**S-N4** [idea] **Related Work 结构合理**——§2 分 6 个子领域（Probe-Based Calibration, Cross-Lingual Probing, Cross-Lingual Alignment, Domain Adaptation Theory, Representation Similarity, Probing Methodology），每个都有恰当的 positioning。

### Weaknesses

**W-N1** [presentation] **14 篇引用仍低于预期**。同类 ACL/EMNLP 论文通常 30-50 篇。缺失的关键文献：
  - IRT 基础文献（Lord 1980, Baker 2001）—— §3.3 使用 IRT 但未引用任何 psychometrics 原始文献
  - Belinkov (2022) probing survey
  - Keleg & Magdy (2023) multilingual calibration
  - Guo et al. (2017) temperature scaling（论文多次提到 ECE 但未引用 calibration 的经典文献）
  - 更多 domain adaptation theory（Ganin et al. 2016; Long et al. 2015）
  - MoE 架构分析文献（Fedus et al. 2022; Zoph et al. 2022）
  - 部分现有引用的作者名/标题可能仍有 accuracy issue（基于 "best" 版本的核查经验，median 版本的 Miao 引用格式也存疑）

**W-N2** [idea] **"First systematic study" claim（§7 Conclusion）需要 qualification**。Civelli et al. (2025) 和 Xiao et al. (2025) 已涉及 cross-lingual probe transfer。论文 §2 中引用了它们但未充分说明自己的差异化。应改为 "the first study systematically evaluating cross-lingual correctness probe transfer across multiple architectures with principled negative result methodology" 或类似限定。

**W-N3** [idea] **CaCLR 的 negative result novelty 取决于 MMD 在 probe outputs 上的应用是否为 "obvious limitation"**。§3.2 自己指出 MMD 在 1-D 上只能 match marginal distributions。如果这一点在设计时就显而易见，那么确认它确实不 work 的 surprise factor 有限。论文应讨论：是否有先前工作提出或使用过 MMD on probe outputs for cross-lingual transfer？如果没有人提出过这个方法，那 "关闭这条路" 的价值需要 contextualize。

---

## C. Overall Assessment

### Major Issues

**无明确的 Major Issue**。论文最大的 concern（W-M1: MMD scope, W-N3: negative result novelty）在 framing 上都有合理的 caveat。根据评分校准规则（0 Major → 可给 Strong Accept），上限为 6。

### Minor Issues（按重要性排序）

1. **W-M1** MMD scope 限制 negative result 的 generality（idea, moderate）
2. **W-N1** 14 篇引用不足（presentation）
3. **W-M3** Gemma 4 数据不对等（idea, minor-moderate）
4. **W-N2** "First systematic study" overclaim（idea, minor）
5. **W-M2** 缺完整 layer × language table（presentation）
6. **W-M4** IRT R²=0.40 decomposition 较弱（idea, minor — paper 已自我降级）
7. **W-N3** Negative result 的 surprise factor（idea, minor）

### Narrative Self-Consistency Check

| Claim | 支撑位置 | 是否自洽 | 备注 |
|-------|---------|---------|------|
| Architecture-dependent Pareto | Tables 1-2, 14 | ✓ | Qwen3 全负 ρ vs Llama4 4 正 vs Gemma4 最强负 |
| CaCLR β inert | Tables 3-4 | ✓ | 3 OOM, d=0.07, p=0.38, both architectures |
| CKA = suggestive only | Table 6 | ✓ | Pooled r=0.52 → partial r=0.18 (p=0.11) |
| Linear proj ~50 pairs sufficient | Table 9 | ✓ | Knee ~60, 20 pairs > CaCLR |
| Decomposition = qualitative | Table 7 | ✓ | d=0.25, 65% improved, random control d=0.05 |
| Orthogonality persists | Table 8 | ✓ | All < 0.12, ρ=-0.58 with resource tier |
| 27% capacity artifacts | Table 10 | ✓ | Shallow + low-resource concentrated |
| Abstract 数字 vs 正文 | 全文 | ✓ | **无不一致**（与 "best" 版本形成鲜明对比）|

### Experiment Coverage vs. Review Context

| Plan | 覆盖 | 位置 | 备注 |
|------|-----|------|------|
| plan_001: Qwen3 Pareto | ✓ | Table 1, §5.1 | Table 仅摘要层，非完整 grid |
| plan_002: Llama4 Pareto | ✓ | Table 2, §5.1 | |
| plan_003: CaCLR | ✓ | Tables 3-5, §5.2 | 完整 β sweep + ablation + comparison |
| plan_004: Decomposition | ✓ | Table 7, §5.4 | |
| plan_005: Orthogonality | ✓ | Table 8, §5.5 | |
| plan_006: Probe Complexity | ✓ | Table 11 (Appendix), §5.8 | |
| plan_007: Benchmarks | ✓ | Table 12 (Appendix), §5.9 | |
| plan_008: Gemma 4 | ✓ | Table 14 (Appendix), §5.1 | 数据量偏少 |
| plan_009: Extended Coverage | ✓ | §5.9, A.6 | 52 languages, 67% viable |
| plan_010: Quantization | ✓ | Table 13 (Appendix), §5.9 | Both architectures |
| plan_011: CKA Analysis | ✓ | Table 6, §5.3 | partial correlation 是 key contribution |
| plan_012: LP Sensitivity | ✓ | Table 9, §5.6 | 10-200 pairs learning curve |
| plan_013: Control Tasks | ✓ | Table 10, §5.7 | 27% artifact finding |

13/13 plans 全部覆盖。

### 主要优势总结

1. **Claim 校准诚实**——每个 claim 都有适当的 qualifier（"suggestive," "qualitative," "principled negative result"），无 overclaim
2. **三段叙事逻辑连贯**——discovery → negative result → constructive recommendation，每一段都有独立的实验支撑
3. **统计方法论在 probing 文献中 above average**——bootstrap CIs + permutation tests + Cohen's d 贯穿全文
4. **Llama 4 Scout language-specific behavior** 是 genuinely new finding，不是已知现象的简单重复
5. **Control task warning 是 generalizable contribution**——对整个 cross-lingual probing 社区有价值
6. **内部一致性完美**——abstract 数字与正文完全吻合，无任何自相矛盾

### 给作者的问题

1. CaCLR 的 L_cons 使用 MMD 在 1-D probe logits 上。是否考虑过在高维 activation space 中做 distributional matching（如 kernel MMD on hidden states 或 optimal transport）？如果 Zhao et al. 的理论确实排除了所有 marginal matching 方法，这应该在 §6 中更明确地论证。
2. Gemma 4 31B 是否有完整的 per-language breakdown 和 transfer method comparison？如果有，为什么不放在 appendix 中？
3. IRT difficulty probe 的 R²=0.40——是否尝试过更复杂的 difficulty model（如 2-PL IRT 或 neural IRT）？R²=0.40 意味着 projecting out difficulty 时会引入 substantial noise。
4. Table 1 的完整 24 层 × 20 语言数据是否可以放入 supplementary material？
5. 论文是否有计划公开代码和 probing 数据以支持 reproducibility？（review context 提到 "no code/data release mentioned"）

---

## 评分总结

| 维度 | 分数 | 理由 |
|------|------|------|
| Score | **4 (Weak Accept)** | 0 Major issues, 方法论扎实, claims 诚实, narrative 自洽; 但个体贡献偏增量, negative result 的 scope 可讨论 |
| Confidence | **4/5** | 仔细阅读全文, 熟悉 probing/calibration/cross-lingual 文献 |

**与 "best" 版本对比**：median 版在以下方面显著优于 best 版——(1) 内部一致性（无数字矛盾），(2) 统计方法论（有 CIs/p/d），(3) claims 校准（不 overclaim），(4) Related Work（14 vs 8 篇，有结构），(5) narrative 诚实度（承认 negative result 而非包装为 positive）。评分差距（4 vs 3）反映了这些质量差异。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 82 · 2026-05-21T04:33:03.737108+00:00_

收到 Reviewer 1 对 **Dream Median Paper** 的审稿意见。这是一篇与之前 "best" 版本不同的论文——标题和内容有显著差异（negative result framing, CaCLR 失败而非成功）。

**R1 评分：4/5 (Weak Accept)**，覆盖 Methods、Novelty、Overall 三个维度。

关键发现摘要：
- **0 个 Major Issue**——方法论扎实、claims 校准诚实、内部一致性完美（与 best 版的数字矛盾形成鲜明对比）
- **7 个 Minor Issue**：MMD scope 限制 negative result 的 generality、14 篇引用仍不足、Gemma 4 数据不对等、"First systematic study" overclaim、缺完整数据表、IRT R²=0.40 较低、negative result 的 surprise factor
- **核心优势**：统计方法论 above-average（bootstrap CIs + permutation tests + Cohen's d）、claims 不 overclaim、Llama 4 的 language-specific Pareto 行为是 genuinely new finding、control task 27% artifact warning 有 generalizable 价值

等待 Reviewer 2 的审稿意见以进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 9

2 recorded events

### User

_source line 83 · 2026-05-21T04:33:06.540247+00:00_

[Reviewer 1 审稿结果]:
Dream median 论文审稿完成。评分 **4 (Weak Accept)**，主要发现：

- **0 个 Major issue**——narrative 内部完全一致，无数字矛盾
- **核心亮点**：CaCLR 负面结果的实验设计扎实（β sweep 3 OOM, d=0.07, p=0.38）；CKA 分析做了 partial correlation controlling depth 后主动降级为 suggestive；统计方法论（bootstrap CIs + permutation tests + Cohen's d）贯穿全文
- **主要关切**：MMD 仅在 1-D probe logits 上测试，negative result 的 scope 被限制；Gemma 4 数据覆盖不对等；14 篇引用仍偏少
- **与 best 版本对比**：median 版在内部一致性、统计严谨性、claims 校准、narrative 诚实度上全面优于 best 版

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 84 · 2026-05-21T04:33:26.358978+00:00_

收到 R1 对 dream median 论文的审稿。评分 4/5 (Weak Accept)，比 best 版本高一个档次。

关键对比：median 版本修复了 best 版本的多个致命问题——无数字矛盾、有统计检验、claims 校准诚实、叙事结构从"包装为正面贡献"转为"诚实的负面结果+可操作建议"。

等待 R2 对 median 论文的审稿意见后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 10

6 recorded events

### User

_source line 85 · 2026-05-21T06:11:38.537215+00:00_

[Reviewer 2 审稿意见]:
## R2 Independent Review: Novelty & Related Work

**论文标题**: The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications

---

### Summary (2-3 sentences)

本文将前期 pilot（Qwen2.5-7B, Llama-3.1-8B）的跨语言 correctness probe transfer 研究扩展至 3 个大规模架构（Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense）× 20 种语言 × 5 种迁移条件，得出了系统性的负面结论：depth-transferability Pareto frontier 不泛化、CaCLR 方法有害、小样本 pilot 的 CKA-transfer 正相关是 Simpson's Paradox。最有价值的贡献是将 Hewitt & Liang 的 selectivity control tasks 引入跨语言 probing，揭示 42% 的低资源 probing 结果为 artifacts。

---

### Strengths

**S1** [Novelty — Control task methodology] 将 Hewitt & Liang (2019) 的 selectivity controls 应用于跨语言 probing 是**本文最强的新颖性贡献**。Table 10（p.10）和 Table 11（p.10）系统展示了 per-language selectivity 数据，发现 LOW tier 的 artifact rate 达 42%（Table 12, p.11）。这一发现对整个跨语言 probing 领域有方法论层面的警示意义——如果近半数低资源语言的 probing 结果是 artifacts，那么先前文献中未使用 control tasks 的正面结论都需要重新审视。这满足"field-level implication"的标准。

**S2** [Framing — 诚实的负面结果] 论文将核心发现定位为"large-scale negative result"而非强行正面包装，这比前一篇论文（同一 research agenda 的正面版本）在学术诚信上更可信。Abstract 开门见山："Our results are predominantly negative"，§7 Conclusion 也直接列出三项负面发现。对于 community 来说，知道什么不可行与知道什么可行同样重要。

**S3** [Statistical rigor] 相比同一 agenda 的正面版本论文，本文在统计层面有实质性进步：
- Bonferroni correction 用于多重比较（§4, p.3-4）
- Spearman correlations 附 p 值（Table 1, 2, §5.1）
- Standard deviations reported（Table 21, p.13: 每个 transfer condition 附 Std）
- Control task selectivity 阈值（< 0.05）明确定义 artifact 判据
- Simpson's Paradox 分析用 partial ρ 验证（Table 9, p.9）

**S4** [Simpson's Paradox falsification] §5.3 的分析虽然是对自家 pilot 的自我纠错，但方法论上有示范意义。Table 9（p.9）清楚展示：5-language pilot 中观察到的正 CKA-transfer correlation（partial ρ 未报告具体值但正面提及），在 20 languages 下变为 non-significant（Simpson partial ρ = +0.14, p = 0.22）。这是 ecological fallacy / Simpson's Paradox 在 NLP 实验中的一个教科书级案例。

**S5** [Practical guidance] §9（p.9-10）提供的三档决策规则（ZS AUROC < 0.30: 不可预测; [0.30, 0.65]: linear projection 有效; > 0.65: zero-shot 已足够）虽然简单，但对实践者有直接价值，且来自充分的实验支撑。

**S6** [Related work coverage] §2（p.2）比前一篇论文完善得多，覆盖了 5 个子方向：probe-based calibration（CORAL, Miao & Ungar）、cross-lingual probing、probing methodology（Hewitt & Liang, MDL）、domain adaptation theory（Ben-David et al., Zhao et al. 2019）、cross-lingual alignment（MUSE, VecMap）。Domain adaptation 的理论框架（H-divergence）为负面结论提供了理论解释基础。

---

### Weaknesses

**W1** [warning — 参考文献仍然不够充分] 虽然 §2 的覆盖面比前一篇论文好得多，但仍有重要遗漏：
- **Conneau et al. (2020)** "Emerging Cross-lingual Structure in Pretrained Language Models" / XLM-R 论文——跨语言表征的 layer-wise 分析基础
- **Pires et al. (2019)** "How multilingual is Multilingual BERT?" ——layer-wise cross-lingual transfer 的开创性研究，直接相关
- **Belinkov (2022)** "Probing Classifiers: Promises, Shortcomings, and Advances" 综述——论文大量使用 probing 方法但未引用该领域的核心综述
- **Keleg & Magdy (2023)** "On the Calibration of Massively Multilingual Language Models" ——多语言 calibration 专题研究
- 此外，论文 PDF 中我未能在正文可见范围内找到完整的 References section（p.10 结尾是 Conclusion，p.11 开始是 Appendix A）。**如果参考文献列表被省略或因排版问题丢失，这是一个严重的格式问题。**

**W2** [warning — 23 张表格 + 0 张图] 与前一篇论文相同的表述问题。23 张表格（正文 13 + 附录 10）但没有一张图。核心发现——Pareto frontier 不存在、CaCLR 的 harmful effect、Simpson's Paradox——都极适合可视化展示。特别是：
- 一张 scatter plot（EN AUROC vs ZS AUROC by architecture）可以直观展示 "no frontier" 的负面结论
- 一张 selectivity heatmap（language × layer）可以直观展示 artifact 分布 pattern
- Simpson's Paradox 最经典的展示方式是分组 scatter plot（within-group vs. overall trend）
表格密集使得负面结论的说服力受损——读者需要自己在数字中寻找 pattern，而一张好图可以一目了然。

**W3** [minor — CaCLR 方法的新颖性因失败而难以评估] CaCLR 的损失函数（BCE + calibration + consistency + MMD）组合了四个已知组件。论文诚实报告其失败（§5.2, Table 3-4），但这使得方法贡献难以被独立评价。如果方法本身不是贡献，那么论文实质上只有两个贡献：(1) control task 方法论，(2) 负面实验结果。对于 main conference 这可能不够；对于 Findings track 可以接受。

**W4** [minor — pilot 区分不充分] 论文多次提到"pilot studies on Qwen2.5-7B and Llama-3.1-8B"（Abstract, §5.1, §5.3），但未明确说明 pilot 是已发表工作还是同一团队的未发表前期工作。如果已发表，需要正式引用并明确 incremental contribution；如果未发表，应说明"our unpublished pilot"。当前表述模糊。

**W5** [minor — Difficulty decomposition 的负面结论太快] §5.4 用一段话否定了 difficulty decomposition（"The difficulty probe itself achieves only |Δ| = 0.03, statistically indistinguishable from a random-direction control"），但 Table 9（p.9）显示 difficulty decomposition ablation 的结果在不同 tier 间有差异。论文未分析为什么 difficulty decomposition 在大模型上失败而可能在小模型上成功——是因为模型规模？训练数据差异？量化？这个分析缺口削弱了负面结论的解释力。

**W6** [minor — Linear projection 的 "only viable path" 结论与 Table 21 存在张力] Table 21（p.13）显示 Linear Projection 200 pairs 的 Sig. impr. count 仅 11/20，few-shot 100 为 13/20。差异不大，且都远未覆盖全部 20 种语言。声称 linear projection 是 "the only viable path" 可能过于绝对。

---

### Questions for Authors

**Q1**: §5.3 Simpson's Paradox 分析中，partial ρ = +0.14 (p = 0.22) 是在控制哪些变量后的结果？如果控制变量不同，partial ρ 是否会改变结论？

**Q2**: Control task 的 selectivity 阈值 < 0.05 是如何确定的？Hewitt & Liang (2019) 原文是否使用了相同阈值？如果阈值改为 0.10 或 0.03，42% 的 artifact rate 如何变化？

**Q3**: 论文将 pilot 模型（Qwen2.5-7B, Llama-3.1-8B）的正面结果归因于 scale 差异，但 pilot 用的是 7B/8B 模型，而本文用的是 22B-235B 模型。是否有证据表明 scale 是导致结论翻转的原因（如中间规模模型的结果）？还是架构差异（MoE vs Dense）更可能是原因？

**Q4**: CaCLR 的 MMD term 引入负面效果（Table 4, p.5: 添加 MMD(l→0.01) 使 AUROC 从 0.563 降至 0.558）。作者是否尝试过其他 distributional matching 方法（如 adversarial alignment, optimal transport）？只测一种 distributional matching 就断言"distributional matching 不可行"可能过于草率。

**Q5**: Table 11（p.10）中多个语言被标记为 ▲（permuted AUROC > real AUROC）。这是否意味着这些语言的 correctness probes 实际上在编码噪声而非真正的 correctness signal？如果是，这对 Miao & Ungar (2026) 的英文 correctness probe 结论有什么影响？

**Q6**: 完整的参考文献列表在哪里？在我阅读的 PDF 中，§7 Conclusion 后直接是 Appendix A，未见 References section。

---

### Minor Issues

- §3.2 "CaCLR extends the standard probe loss with two regularization terms"（p.3）中公式 (1) 有 3 项额外 loss（ℓ_cal, ℓ_cons, ℓ_MMD），但文字说"two"——应为 three
- Table 3 caption（p.5）说"CaCLR 1 sweep"但未解释 sweep 的含义
- §5.1 对 Gemma 4 31B Dense 的描述（p.4-5）说"moderately clear but still noisy frontier"，但随后的 Summary 说"does not generalize"——这两个判断有轻微矛盾
- Table 19（p.13, Appendix A）52-language 扩展的结果格式与正文 20-language 不一致，增加了对比难度
- Limitations（p.10）列出 4 点限制，诚实但也暴露了实验设计的局限：只用 MCQA format、只测 logistic regression、不包含所有 typological diversity

---

### Scores

- **Soundness**: 3.5 / 5 — 统计方法比前一篇论文好很多（Bonferroni, control tasks, CIs），但部分负面结论的解释不够深入（W5），且参考文献列表可能缺失（W1）
- **Excitement**: 3 / 5 — Control task 方法论贡献有 field-level 意义，但整体是 "things don't work" narrative，缺乏正面方法贡献；对于 Findings track 有足够兴趣，对 main conference 偏弱
- **Overall**: 3 / 5 — Borderline / Findings track。Control task 发现（42% artifacts）如果能被独立验证，价值很高。但 CaCLR 失败 + 负面 Pareto 结论使得论文的"so what"不够强。推荐 Findings track 接收。
- **Confidence**: 4 / 5 — 熟悉 probing、calibration、cross-lingual transfer 领域

---

### 与前一篇论文（positive framing）的对比评价

| 维度 | Paper 1 (Pareto Frontier, positive) | Paper 2 (Limits, negative) |
|------|-------------------------------------|---------------------------|
| 学术诚信 | 差——核心数字自相矛盾（72% vs 81%）、"25%" 来源不明、疑似 fabricated references | 好——诚实承认负面结论、pilot 自我纠错 |
| 统计严谨 | 差——无 CI、无 control tasks、无显著性检验 | 好——Bonferroni、selectivity controls、SDs |
| Related Work | 差——8 篇引用、~15 行 | 中等——5 个子方向、但可能缺少 References section |
| 新颖性 | 弱——四项增量性贡献、Pareto 术语误用 | 中等——control task 方法论有真正新意，但正面贡献有限 |
| 可视化 | 0 图 / 16 表 | 0 图 / 23 表（问题同样严重） |
| 实际价值 | 有限——CaCLR 改进仅 1.3pp | 有限但诚实——三档决策规则 |

**整体判断**：Paper 2 在学术质量上显著优于 Paper 1，但两篇论文共享一个核心缺陷——**零可视化**。如果只能推荐一篇，我更倾向 Paper 2，因为诚实的负面结论 + 方法论警示对 community 的价值大于包装过度的弱正面结论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-21T06:12:24.491847+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉审阅任务（Median Paper）\n\n以下是 **Reviewer 2（Novelty & Related Work）** 的完整 Round 1 审稿意见。请逐条回应其 Weaknesses：\n\n- **[AGREE]**：同意，并补充你从 Methods/Experiments 角度的佐证\n- **[REBUT]**：不同意或有保留意见，提供具体证据（cite Section/Table）\n\n特别关注：\n1. R2-W1（引用不足 + References section 可能缺失）——你的审稿中也提到 14 篇引用偏少，是否同意 References section 可能丢失？\n2. R2-W3（CaCLR 方法失败导致论文只剩两个贡献）——你认为 negative result 本身是否构成独立贡献？\n3. R2-W6（linear projection \"only viable path\" 与 Table 21 的张力）——从实验角度评估这个 claim 是否过强\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Overall**: 3/5 (Borderline / Findings)\n\n### Strengths\n- **S1**: Control task methodology（Hewitt & Liang → 跨语言 probing，42% artifact rate）是最强新颖性贡献\n- **S2**: 诚实的负面结果 framing，Abstract 开门见山 \"predominantly negative\"\n- **S3**: 统计严谨性显著进步——Bonferroni、Spearman+p值、SDs、control task selectivity 阈值\n- **S4**: Simpson's Paradox falsification 是教科书级案例\n- **S5**: 三档决策规则（§9）对实践者有直接价值\n- **S6**: Related Work 覆盖 5 个子方向，比 best 版本好得多\n\n### Weaknesses\n**W1** [warning] 参考文献仍不够充分——缺 Conneau et al. (2020)、Pires et al. (2019)、Belinkov (2022) survey、Keleg & Magdy (2023)、Guo et al. (2017) temperature scaling。**且 PDF 中 §7 后直接是 Appendix A，未见 References section——如果参考文献列表因排版丢失，这是严重格式问题。**\n\n**W2** [warning] 23 张表格 + 0 张图。核心负面结论（no Pareto frontier、CaCLR harmful、Simpson's Paradox）极适合可视化。Scatter plot、selectivity heatmap、分组 scatter（Simpson's Paradox）都比表格更有说服力。\n\n**W3** [minor] CaCLR 失败使方法贡献难以独立评价——论文实质只剩 (1) control task 方法论 (2) 负面实验结果。对 main conference 可能不够，Findings track 可接受。\n\n**W4** [minor] Pilot 区分不充分——\"pilot studies on Qwen2.5-7B and Llama-3.1-8B\" 未说明是已发表还是未发表前期工作。\n\n**W5** [minor] Difficulty decomposition 的负面结论太快——§5.4 一段话否定，未分析为什么在大模型上失败（scale? 数据? 量化?）\n\n**W6** [minor] \"Only viable path\" 结论与 Table 21 存在张力——Linear Proj 200 pairs Sig. impr. 11/20，few-shot 100 为 13/20，差异不大。\n\n### Questions\nQ1-Q6 涵盖：Simpson's Paradox partial ρ 的控制变量、selectivity 阈值敏感性、scale vs architecture 作为结论翻转原因、是否测试过其他 distributional matching 方法、▲ 标记语言的含义、References section 位置。\n\n### Scores\n- Soundness: 3.5/5 | Excitement: 3/5 | Overall: 3/5 | Confidence: 4/5",
  "project": "xling_calib_direction",
  "chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
  "director_session_key": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉审阅任务（Median Paper）\n\n以下是 **Reviewer 2（Novelty & Related Work）** 的完整 Round 1 审稿意见。请逐条回应其 Weaknesses：\n\n- **[AGREE]**：同意，并补充你从 Methods/Experiments 角度的佐证\n- **[REBUT]**：不同意或有保留意见，提供具体证据（cite Section/Table）\n\n特别关注：\n1. R2-W1（引用不足 + References section 可能缺失）——你的审稿中也提到 14 篇引用偏少，是否同意 References section 可能丢失？\n2. R2-W3（CaCLR 方法失败导致论文只剩两个贡献）——你认为 negative result 本身是否构成独立贡献？\n3. R2-W6（linear projection \"only viable path\" 与 Table 21 的张力）——从实验角度评估这个 claim 是否过强\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Overall**: 3/5 (Borderline / Findings)\n\n### Strengths\n- **S1**: Control task methodology（Hewitt & Liang → 跨语言 probing，42% artifact rate）是最强新颖性贡献\n- **S2**: 诚实的负面结果 framing，Abstract 开门见山 \"predominantly negative\"\n- **S3**: 统计严谨性显著进步——Bonferroni、Spearman+p值、SDs、control task selectivity 阈值\n- **S4**: Simpson's Paradox falsification 是教科书级案例\n- **S5**: 三档决策规则（§9）对实践者有直接价值\n- **S6**: Related Work 覆盖 5 个子方向，比 best 版本好得多\n\n### Weaknesses\n**W1** [warning] 参考文献仍不够充分——缺 Conneau et al. (2020)、Pires et al. (2019)、Belinkov (2022) survey、Keleg & Magdy (2023)、Guo et al. (2017) temperature scaling。**且 PDF 中 §7 后直接是 Appendix A，未见 References section——如果参考文献列表因排版丢失，这是严重格式问题。**\n\n**W2** [warning] 23 张表格 + 0 张图。核心负面结论（no Pareto frontier、CaCLR harmful、Simpson's Paradox）极适合可视化。Scatter plot、selectivity heatmap、分组 scatter（Simpson's Paradox）都比表格更有说服力。\n\n**W3** [minor] CaCLR 失败使方法贡献难以独立评价——论文实质只剩 (1) control task 方法论 (2) 负面实验结果。对 main conference 可能不够，Findings track 可接受。\n\n**W4** [minor] Pilot 区分不充分——\"pilot studies on Qwen2.5-7B and Llama-3.1-8B\" 未说明是已发表还是未发表前期工作。\n\n**W5** [minor] Difficulty decomposition 的负面结论太快——§5.4 一段话否定，未分析为什么在大模型上失败（scale? 数据? 量化?）\n\n**W6** [minor] \"Only viable path\" 结论与 Table 21 存在张力——Linear Proj 200 pairs Sig. impr. 11/20，few-shot 100 为 13/20，差异不大。\n\n### Questions\nQ1-Q6 涵盖：Simpson's Paradox partial ρ 的控制变量、selectivity 阈值敏感性、scale vs architecture 作为结论翻转原因、是否测试过其他 distributional matching 方法、▲ 标记语言的含义、References section 位置。\n\n### Scores\n- Soundness: 3.5/5 | Excitement: 3/5 | Overall: 3/5 | Confidence: 4/5",
    "project": "xling_calib_direction",
    "chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
    "director_session_key": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-21T06:12:53.908692+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29416
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-21T06:12:54.610852+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉审阅任务（Median Paper）\n\n以下是 **Reviewer 1（Methods & Experiments）** 的完整 Round 1 审稿意见。请逐条回应其 Weaknesses：\n\n- **[AGREE]**：同意，并补充你从 Novelty/Related Work 角度的佐证\n- **[REBUT]**：不同意或有保留意见，提供具体证据（cite Section/Table）\n\n特别关注：\n1. R1-W-M1（MMD 在 1-D probe logits 上限制了 negative result 的 scope）——从 novelty 角度，这对负面结果贡献的价值有何影响？\n2. R1-W-M3（Gemma 4 数据不对等）——是否影响三架构对比的 claim？\n3. R1 评价为 0 Major issues + Weak Accept——你评 Borderline/Findings，分歧主要在哪？\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**Overall**: 4/5 (Weak Accept)\n\n### Methods & Experiments Strengths\n- **S-M1**: Bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿所有实验\n- **S-M2**: CaCLR β sweep 设计充分——3 OOM, 两种架构, 20 语言, 无 β 达 p<0.05 或 d>0.2\n- **S-M3**: CKA 分析做 partial correlation controlling depth（r=0.18, p=0.11）后主动降级为 suggestive\n- **S-M4**: Linear projection sample efficiency 曲线——~50 pairs 达 90%，20 pairs 即超 CaCLR\n- **S-M5**: Control task analysis 将 Hewitt & Liang 扩展到 20 语言 × 多层，27% artifact finding\n- **S-M6**: Mean-shift rank-invariance proof + 实验验证（ΔAUROC ≡ 0）\n\n### Methods & Experiments Weaknesses\n**W-M1** [idea] MMD 在 1-D probe logits 上操作限制了 negative result scope。未测试：(a) MMD 在 activation space 的效果 (b) optimal transport/Sinkhorn 在高维的效果。负面结论严格来说只关闭 \"1-D probe output distributional matching\" 而非全部。论文 framing 有 caveat（§3.2, §6），逻辑自洽但 generality 受限。\n\n**W-M2** [presentation] Table 1 未展示完整 24 层 × 20 语言数据。Pareto frontier claim 需要读者看到完整 depth profile。\n\n**W-M3** [idea] Gemma 4 31B 仅出现在 Table 14（appendix 3 行摘要），无 per-language breakdown、β sweep、full comparison。三架构对比不对等。\n\n**W-M4** [idea] IRT R²=0.40 较低。Difficulty probe 只解释 40% item difficulty variance，projecting out difficulty 时残差仍混有大量 difficulty signal。论文已自我降级为 qualitative claim。\n\n### Novelty & Related Work Strengths\n- **S-N1**: \"Negative result as contribution\" 在 NLP 社区有价值\n- **S-N2**: Llama 4 Scout 的 4/20 语言 ρ > 0 是 genuinely new observation\n- **S-N3**: Control task artifact warning 作为独立贡献有 field-level 意义\n- **S-N4**: Related Work §2 覆盖 6 个子领域，结构合理\n\n### Novelty Weaknesses\n**W-N1** [presentation] 14 篇引用仍低——缺 IRT 基础文献、Belinkov survey、Keleg & Magdy、Guo et al. temperature scaling、domain adaptation 文献、MoE 分析文献。部分引用可能存在 accuracy issue。\n\n**W-N2** [idea] \"First systematic study\" claim 需 qualification。\n\n**W-N3** [idea] CaCLR negative result novelty 取决于 MMD on probe outputs 是否为 \"obvious limitation\"——§3.2 自己指出 1-D 限制。\n\n### Narrative Self-Consistency\n全文内部一致性完美——Abstract 数字与正文完全吻合，无任何自相矛盾。13/13 实验计划全部覆盖。\n\n### Scores\n- Overall: 4/5 (Weak Accept) | Confidence: 4/5\n- 0 Major issues, 方法论扎实, claims 诚实, narrative 自洽",
  "project": "xling_calib_direction",
  "chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
  "director_session_key": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉审阅任务（Median Paper）\n\n以下是 **Reviewer 1（Methods & Experiments）** 的完整 Round 1 审稿意见。请逐条回应其 Weaknesses：\n\n- **[AGREE]**：同意，并补充你从 Novelty/Related Work 角度的佐证\n- **[REBUT]**：不同意或有保留意见，提供具体证据（cite Section/Table）\n\n特别关注：\n1. R1-W-M1（MMD 在 1-D probe logits 上限制了 negative result 的 scope）——从 novelty 角度，这对负面结果贡献的价值有何影响？\n2. R1-W-M3（Gemma 4 数据不对等）——是否影响三架构对比的 claim？\n3. R1 评价为 0 Major issues + Weak Accept——你评 Borderline/Findings，分歧主要在哪？\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**Overall**: 4/5 (Weak Accept)\n\n### Methods & Experiments Strengths\n- **S-M1**: Bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿所有实验\n- **S-M2**: CaCLR β sweep 设计充分——3 OOM, 两种架构, 20 语言, 无 β 达 p<0.05 或 d>0.2\n- **S-M3**: CKA 分析做 partial correlation controlling depth（r=0.18, p=0.11）后主动降级为 suggestive\n- **S-M4**: Linear projection sample efficiency 曲线——~50 pairs 达 90%，20 pairs 即超 CaCLR\n- **S-M5**: Control task analysis 将 Hewitt & Liang 扩展到 20 语言 × 多层，27% artifact finding\n- **S-M6**: Mean-shift rank-invariance proof + 实验验证（ΔAUROC ≡ 0）\n\n### Methods & Experiments Weaknesses\n**W-M1** [idea] MMD 在 1-D probe logits 上操作限制了 negative result scope。未测试：(a) MMD 在 activation space 的效果 (b) optimal transport/Sinkhorn 在高维的效果。负面结论严格来说只关闭 \"1-D probe output distributional matching\" 而非全部。论文 framing 有 caveat（§3.2, §6），逻辑自洽但 generality 受限。\n\n**W-M2** [presentation] Table 1 未展示完整 24 层 × 20 语言数据。Pareto frontier claim 需要读者看到完整 depth profile。\n\n**W-M3** [idea] Gemma 4 31B 仅出现在 Table 14（appendix 3 行摘要），无 per-language breakdown、β sweep、full comparison。三架构对比不对等。\n\n**W-M4** [idea] IRT R²=0.40 较低。Difficulty probe 只解释 40% item difficulty variance，projecting out difficulty 时残差仍混有大量 difficulty signal。论文已自我降级为 qualitative claim。\n\n### Novelty & Related Work Strengths\n- **S-N1**: \"Negative result as contribution\" 在 NLP 社区有价值\n- **S-N2**: Llama 4 Scout 的 4/20 语言 ρ > 0 是 genuinely new observation\n- **S-N3**: Control task artifact warning 作为独立贡献有 field-level 意义\n- **S-N4**: Related Work §2 覆盖 6 个子领域，结构合理\n\n### Novelty Weaknesses\n**W-N1** [presentation] 14 篇引用仍低——缺 IRT 基础文献、Belinkov survey、Keleg & Magdy、Guo et al. temperature scaling、domain adaptation 文献、MoE 分析文献。部分引用可能存在 accuracy issue。\n\n**W-N2** [idea] \"First systematic study\" claim 需 qualification。\n\n**W-N3** [idea] CaCLR negative result novelty 取决于 MMD on probe outputs 是否为 \"obvious limitation\"——§3.2 自己指出 1-D 限制。\n\n### Narrative Self-Consistency\n全文内部一致性完美——Abstract 数字与正文完全吻合，无任何自相矛盾。13/13 实验计划全部覆盖。\n\n### Scores\n- Overall: 4/5 (Weak Accept) | Confidence: 4/5\n- 0 Major issues, 方法论扎实, claims 诚实, narrative 自洽",
    "project": "xling_calib_direction",
    "chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
    "director_session_key": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-21T06:12:56.221858+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---

### Assistant

_source line 90 · 2026-05-21T06:13:04.281140+00:00_

Median 论文的交叉分享任务已分发给两位 Reviewer。等待交叉回应后进入收敛判断和报告合成。

当前状态：
- **Best paper review**: 已完成并投递（Weak Reject, 2.5/5）
- **Median paper review**: Step 2 交叉分享进行中，等待 R1 和 R2 的交叉回应

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 11

16 recorded events

### User

_source line 91 · 2026-05-21T06:13:05.613786+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

Paper 2（negative result framing）的审阅完成。核心判断：
- **最强贡献**：Hewitt & Liang selectivity controls 引入跨语言 probing，揭示 42% 低资源结果为 artifacts
- **主要缺陷**：23 表 0 图、参考文献列表可能缺失、CaCLR 失败使正面方法贡献为零
- **评分**：Overall 3/5（Findings track borderline），显著优于 Paper 1（2.0/5）

---

[Reviewer 1 审稿意见]:

## R1 Independent Review: Methods & Experiments

### Summary (2-3 sentences)

This paper presents a large-scale negative result: cross-lingual correctness probe transfer techniques (CaCLR distributional matching, CKA geometric alignment, difficulty decomposition) that showed promise in pilot studies fail comprehensively at scale across 3 architectures and 20 languages. The paper's strongest contribution is a methodological one—applying Hewitt & Liang selectivity controls to cross-lingual probing reveals that 37-42% of mid/low-resource language-layer combinations are capacity artifacts. However, a fundamental confound undermines confidence in whether the negative results are truly fundamental limitations or artifacts of the specific experimental setup: English probe AUROC (0.715-0.742) is substantially lower than comparable work, potentially driven by INT4/W4A16 quantization and MoE routing effects, meaning all downstream negative results may reflect suboptimal probing rather than principled impossibility.

### Strengths

**S1** [Statistical rigor] The paper applies Bonferroni correction for multiple comparisons (§4), bootstrap 95% CIs, paired permutation tests, and Cohen's d consistently across all experiments. This is above-average for the probing literature and appropriate for a negative-result paper where false negatives must be carefully distinguished from true nulls.

**S2** [CaCLR negative result is thorough] The β sweep across 3 orders of magnitude (Table 3: β=0.001→1.0) with monotonic degradation (Δ=-0.003 to Δ=-0.019), coupled with component ablation (Table 4: each component net negative) and 5-way transfer comparison (Table 5), leaves no room for "you just didn't tune it right." The implementation details (Adam lr=1e-3, cosine schedule, 50 epochs, patience 10, batch 256) are sufficient for reproduction.

**S3** [Control task finding is the paper's anchor] Tables 10-12 document artifact rates by resource tier (HIGH 18%, MID 37%, LOW 42%) and by depth band (LOW tier at 0-25% depth: 65-68% artifact rate). The selectivity–AUROC correlation (ρ=0.68, p<0.001) in §5.5 is the sharpest finding: it suggests that many apparently successful cross-lingual probe transfer results in the literature may be capacity artifacts. This is the first systematic application of Hewitt & Liang selectivity to cross-lingual probing and the finding generalizes beyond this paper's scope.

**S4** [Simpson's Paradox validation is methodologically valuable] Table 6 shows Llama partial ρ collapsing from +0.41 (5-language pilot, p=0.006) to +0.08 (20 languages, p=0.42). This is a textbook demonstration of small-sample artifact inflation and serves as a cautionary tale for pilot studies with ≤5 languages.

**S5** [Linear projection analysis is nuanced and honest] Rather than presenting linear projection as a clean solution, the paper reports the inconsistent effect-reversal zone [0.48-0.68] (Table 15), tier-dependent pair requirements (HIGH: 68, MID: 125, LOW: 182 pairs; Table 14), and the conditional nature of the recommendation (§6 Discussion). This honesty is commendable even if it weakens the practical takeaway.

**S6** [Honest framing throughout] Every negative result is explicitly labeled as such: Pareto "does not generalize" (§5.1), CaCLR "fails" (§5.2), CKA "pilot artifact confirmed" (§5.3), decomposition "ineffective" (§5.4). No spin. Claims are calibrated to the evidence.

**S7** [Internal consistency] All abstract numbers match body text. No contradictions between sections. Review context YAML confirms the paper faithfully reports its (imagined) experimental outcomes.

### Weaknesses

**W1** [MAJOR — Confound: Low English AUROC may drive all negative results] The best English probe AUROC across all architectures is 0.738 (Qwen3) / 0.715 (Llama4) / 0.742 (Gemma4). This is substantially lower than comparable work (median Dream paper achieves 0.80; best Dream paper achieves 0.843). If the English probes themselves are suboptimal—due to INT4/W4A16 quantization degrading correctness signals, MoE routing introducing layer-wise noise, or other factors—then ALL downstream negative results (no Pareto, no CaCLR benefit, no decomposition effect, no CKA predictive power) may reflect "poor probes don't transfer well" rather than "cross-lingual probe transfer is fundamentally limited."

The paper partially acknowledges quantization (Limitation 2 in §6) but does NOT address the possibility that a better probing setup (e.g., FP16 dense models with EN AUROC ≥0.80) might produce qualitatively different results. This is the single biggest threat to the paper's core claim of "fundamental limitations."

**Why Major**: The paper's central thesis—that cross-lingual probe transfer is fundamentally limited—cannot be defended without ruling out that the experimental setup itself is the bottleneck. A negative result paper's value depends entirely on whether the null is informative. If the setup is suboptimal, the null says "this setup doesn't work," not "this approach doesn't work."

**W2** [MAJOR — Quantization confound at deep layers is unresolved] Table 22 shows quantization introduces depth-dependent bias: Llama W4A16 Δ ranges from -0.003 (20% depth) to -0.018 (95% depth); Qwen INT4 Δ ranges from -0.005 to -0.022. Rank preservation fails at ≥60-80% depth on both models. This creates a direct confound with the Pareto frontier analysis (§5.1): the non-monotonic patterns attributed to "MoE routing effects" (14/20 non-monotonic on Qwen3) may partly arise from layer-dependent quantization artifacts. The paper observes that "the Pareto frontier is noisy" but does not disentangle how much noise comes from architecture vs. quantization.

**Why Major**: Deep-layer probe results (including EN-optimal AUROC, which determines all transfer comparisons) are systematically biased by quantization. The 1-2pp bias at deep layers is large enough to shift conclusions when effect sizes are small (CaCLR Δ=-0.010; decomposition Δ=-0.003).

**W3** [Difficulty decomposition failure may reflect probe quality, not absent phenomenon] The IRT difficulty probe achieves only R²=0.31 (Table 9 context). This means the "difficulty direction" captures less than a third of actual difficulty variance, and "projecting it out" removes a noisy estimate rather than a clean signal. The random-direction control producing an indistinguishable effect (Δ=-0.005 vs Δ=-0.003, p=0.42) is consistent with BOTH interpretations: (a) there is no difficulty-capability decomposition (the paper's conclusion), or (b) the difficulty probe is too poor to test the hypothesis. The paper does not discuss whether a higher-quality difficulty probe (R²≥0.50) would change the result.

**W4** [Llama 4 Scout underpowered for per-language analysis] With only 12 probed layers (every 4th of 48), per-language Spearman tests have n=12, yielding statistical power of ~0.35-0.50 for detecting ρ=-0.40 at α=0.05. The paper correctly notes 0/20 languages reach significance (Table 2), but this is expected given the power analysis, not evidence against the Pareto effect. The paper should report post-hoc power analysis.

**W5** [The "effect reversal zone" for linear projection is so wide as to be unhelpful] Table 15 shows the reversal zone spans ZS AUROC [0.48, 0.68]. Since 16/20 languages have ZS AUROC in this range (review context), the conditional recommendation in §6 ("if ZS < 0.50, linear proj likely helps") applies to only ~4/20 languages. For the vast majority of languages, the paper's own analysis says the outcome is "unpredictable without held-out validation," making the practical recommendation nearly vacuous.

**W6** [No dense model at comparable scale creates architecture-scale confound] Gemma 4 31B (31B dense) is compared against Qwen3-235B (235B MoE) and Llama 4 Scout (109B MoE, 17B active). The finding that "dense shows clearer Pareto than MoE" (§5.1) cannot distinguish architecture effect from scale/quantization effect: Gemma runs in FP16, the MoE models use INT4/W4A16. A FP16 dense model at 7B (as in the pilot) vs. INT4 MoE at 235B is an apples-to-oranges comparison.

**W7** [Orthogonality section (§5.9) contributes nothing actionable] Architecture agreement is only 65% (Table 23: 7/20 disagreements). The section's own conclusion acknowledges this is "unreliable for low-resource languages where probe validity itself is questionable" (§5.5 back-reference). This circular dependency (artifacts → unreliable probes → unreliable orthogonality) means the section has no standalone conclusion. Should be cut or relegated to appendix.

**W8** [Reference count still below expectations] ~15-17 references for a paper spanning probing, calibration, IRT, cross-lingual alignment, domain adaptation, and control tasks. Missing: IRT foundational literature (Lord 1980; Baker 2001), Belinkov (2022) probing survey, Guo et al. (2017) temperature scaling, additional domain adaptation theory (Ganin et al. 2016).

### Questions for Authors

**Q1** [Critical] The best English probe AUROC is 0.738 (Qwen3-235B). Comparable work achieves 0.80+. Have you tested whether running the same probing pipeline on a FP16 dense model (e.g., Llama-3.1-8B or Qwen2.5-7B used in pilot) achieves ≥0.80? If so, the negative results may be specific to quantized MoE setups, not to cross-lingual probe transfer in general. If not tested, this is a critical missing control.

**Q2** For the difficulty decomposition (§5.4), the IRT probe R²=0.31 is quite low. Have you tried more expressive difficulty models (2-PL IRT, neural IRT)? The null result may reflect poor difficulty estimation, not the absence of a difficulty-capability decomposition.

**Q3** How much of Qwen3's 14/20 non-monotonic pattern survives after correcting for quantization bias? Table 22 shows INT4 introduces up to -0.022 Δ at deep layers. If corrected, do any non-monotonic languages become monotonically negative?

**Q4** The selectivity-AUROC correlation (ρ=0.68) could be confounded by a common cause: probe training data size. Languages with more parallel data have both higher selectivity AND higher AUROC because the probe trains better. Have you controlled for training set size?

**Q5** Linear projection requires 100-200 parallel pairs. For the low-resource languages where it's most needed (am, yo, my), do parallel corpora of this size even exist? If not, the practical recommendation is moot for the languages it would help most.

**Q6** Table 5 shows CaCLR win rate vs. zero-shot is 18%. Are these wins concentrated in specific language-tier × depth combinations? If CaCLR helps for certain high-resource languages at certain depths, this would qualify the "comprehensive failure" narrative.

### Minor Issues

- Table 1 reports only hi (p=0.041) as significant, but with Bonferroni correction for 20 languages, the threshold is 0.0025, not 0.05. After correction, 0/20 are significant on Qwen3. The text should clarify whether per-language p-values are raw or corrected.
- §5.1 states "0-1 show a significant global Pareto frontier" but Gemma's p=0.045 is marginally significant without correction. With 3 architecture-level tests, Bonferroni threshold is ~0.017. Should clarify.
- Table 3 (CaCLR β sweep) is shown at "50% depth, 20 langs mean" — should show results at EN-optimal layer too, since that's where the comparison in Table 5 is made.
- Some table numbering appears to skip (Tables 1-11 in main text, then Tables 12-23 mixing main text and appendix). Should be reorganized.
- The paper claims "first large-scale study" (§1) but should acknowledge Civelli et al. (2025) and Xiao et al. (2025) explicitly in the claim.

### Scores

- **Soundness**: 3/5 — Methodology is thorough (sweeps, ablations, controls) but two unresolved confounds (low EN AUROC across all models; depth-dependent quantization bias) undermine confidence that negative results are fundamental rather than setup-specific.
- **Excitement**: 2/5 — The control task finding (§5.5) is genuinely important for the field. But the remaining content is a collection of null results without a compelling resolution: the paper closes doors but doesn't open new ones. The practical recommendation (linear projection) is too conditional to be actionable.
- **Overall**: 2/5 — The paper's core thesis ("cross-lingual calibration probe transfer is fundamentally limited") is not adequately supported because the experimental setup itself may be the bottleneck (EN AUROC 0.715-0.742, quantization confound). The control task finding alone is a Findings-level contribution if extracted and focused. As currently framed—claiming to demonstrate fundamental limits via a potentially flawed setup—the paper overclaims despite its honest tone.
- **Confidence**: 4/5 — I have read the paper carefully and am familiar with the probing, calibration, and cross-lingual transfer literature. Main uncertainty: whether the "worst-tier" EN AUROC values are realistic or artificially suppressed by the simulation setup.


---

[Reviewer 1 审稿结果]:
审稿报告已提交。

评分摘要：Soundness 3/5, Excitement 2/5, Overall 2/5 (Reject), Confidence 4/5。核心问题是两个 Major weaknesses：(1) 全部模型的英语 probe AUROC 仅 0.715-0.742，远低于同类工作的 0.80+，所有负面结果可能反映的是 probing setup 的局限而非方法论的根本限制；(2) 深层 INT4/W4A16 量化引入 1-2pp 的系统性偏差，直接干扰 Pareto frontier 和 CaCLR 的分析。控制任务发现（37-42% artifact rate）是论文最有价值的贡献，可单独作为 Findings 级别工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-21T06:14:31.752866+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-21T06:14:31.903739+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf\", \"venue\": \"ACL ARR\", \"requested_at\": \"2026-05-20T19:57:02.950533+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_74ae31a7dc5ae9d419ba9a89bccc89c0\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-21T06:14:31.904132+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-21T06:14:31.954585+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-21T06:14:37.831991+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '[Best] 收集初审 + 交叉 + 报告投递', 'status': 'completed', 'activeForm': 'Best paper 审稿已完成'}, {'content': '[Median] 收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集 Median 初审'}, {'content': '[Median] 交叉分享 + R1 修订审稿', 'status': 'completed', 'activeForm': 'Median 交叉审阅'}, {'content': '[Median] 收敛判断', 'status': 'completed', 'activeForm': 'Median 收敛判断'}, {'content': '[Median] 合成报告 + 更新 Issue Tracker', 'status': 'in_progress', 'activeForm': '合成 Median 审稿报告'}, {'content': '[Median] 投递报告给 Research Director', 'status': 'pending', 'activeForm': '投递 Median 报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '[Best] 收集初审 + 交叉 + 报告投递', 'status': 'completed', 'activeForm': 'Best paper 审稿已完成'}, {'content': '[Median] 收集 R1 和 R2 初审意见', 'status': 'completed', 'activeForm': '收集 Median 初审'}, {'content': '[Median] 交叉分享 + R1 修订审稿', 'status': 'completed', 'activeForm': 'Median 交叉审阅'}, {'content': '[Median] 收敛判断', 'status': 'completed', 'activeForm': 'Median 收敛判断'}, {'content': '[Median] 合成报告 + 更新 Issue Tracker', 'status': 'in_progress', 'activeForm': '合成 Median 审稿报告'}, {'content': '[Median] 投递报告给 Research Director', 'status': 'pending', 'activeForm': '投递 Median 报告'}]"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-21T06:14:37.882724+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-21T06:14:41.848760+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/review_issues.yaml"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-21T06:14:41.899538+00:00_

1	issues:
2	- id: "R1-N3+R2-N1"
3	  summary: "参考文献严重不足（仅8篇）且多条引用元数据错误/疑似虚构"
4	  category: writing
5	  severity: critical
6	  status: open
7	  first_raised_round: 1
8	  last_seen_round: 1
9	  mentions:
10	    - round: 1
11	      reviewers: [1, 2]
12	      note: "R1通过web search发现Miao et al.作者名/标题不匹配、Zhou et al.年份/标题不匹配、Civelli et al.标题不匹配。R2列出7+个缺失文献领域。交叉审阅后双方一致认定critical，R2提出疑似fabricated citations的ethical concern。"
13	  action_items:
14	    - round: 1
15	      action: "扩展引用至30+篇；逐条核查所有现有引用的作者名、标题、年份、venue"
16	      assigned_to: author
17	      status: open
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: "R1-N1"
22	  summary: "Abstract 72% vs 正文§5.2 81%数值矛盾——疑为h²=0.72与prescriptive accuracy混淆"
23	  category: method
24	  severity: critical
25	  status: open
26	  first_raised_round: 1
27	  last_seen_round: 1
28	  mentions:
29	    - round: 1
30	      reviewers: [1, 2]
31	      note: "R1首次发现，R2交叉审阅时确认并补充：h²(variance explained)与accuracy(分类准确率)是完全不同指标。双方一致critical。"
32	  action_items:
33	    - round: 1
34	      action: "统一数字并明确72%和81%分别度量什么；修正Abstract"
35	      assigned_to: author
36	      status: open
37	  resolution: ""
38	  resolution_round: null
39	
40	- id: "R1-N2"
41	  summary: "Abstract 'explains 25% of transfer gap'在正文和Table 5中无推导路径"
42	  category: method
43	  severity: critical
44	  status: open
45	  first_raised_round: 1
46	  last_seen_round: 1
47	  mentions:
48	    - round: 1
49	      reviewers: [1, 2]
50	      note: "R1首次发现Table 5的Share%为13%/87%，推不出25%。R2交叉审阅确认并将自己初审的W4升级为critical。连同R1-N1，Abstract中两个核心数字均不可验证。"
51	  action_items:
52	    - round: 1
53	      action: "删除或修正25%，给出明确推导路径"
54	      assigned_to: author
55	      status: open
56	  resolution: ""
57	  resolution_round: null
58	
59	- id: "R1-N4"
60	  summary: "全文Tables 1-16均为单次实验点估计，完全缺乏统计检验和方差估计"
61	  category: experiment
62	  severity: critical
63	  status: open
64	  first_raised_round: 1
65	  last_seen_round: 1
66	  mentions:
67	    - round: 1
68	      reviewers: [1, 2]
69	      note: "R1首次提
…[truncated 6577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-21T06:16:00.864347+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "xling_calib_direction",
  "issues_yaml": "## Best Paper (Round 1) Issues — preserved\nissues:\n- id: \"R1-N3+R2-N1\"\n  summary: \"[Best] 参考文献严重不足（仅8篇）且多条引用元数据错误/疑似虚构\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1通过web search发现Miao et al.作者名/标题不匹配、Zhou et al.年份/标题不匹配、Civelli et al.标题不匹配。R2列出7+个缺失文献领域。交叉审阅后双方一致认定critical，R2提出疑似fabricated citations的ethical concern。\"\n  action_items:\n    - round: 1\n      action: \"扩展引用至30+篇；逐条核查所有现有引用的作者名、标题、年份、venue\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1\"\n  summary: \"[Best] Abstract 72% vs 正文§5.2 81%数值矛盾——疑为h²=0.72与prescriptive accuracy混淆\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次发现，R2交叉审阅时确认并补充：h²(variance explained)与accuracy(分类准确率)是完全不同指标。双方一致critical。\"\n  action_items:\n    - round: 1\n      action: \"统一数字并明确72%和81%分别度量什么；修正Abstract\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"[Best] Abstract 'explains 25% of transfer gap'在正文和Table 5中无推导路径\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次发现Table 5的Share%为13%/87%，推不出25%。R2交叉审阅确认并将自己初审的W4升级为critical。\"\n  action_items:\n    - round: 1\n      action: \"删除或修正25%，给出明确推导路径\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4\"\n  summary: \"[Best] 全文Tables 1-16均为单次实验点估计，完全缺乏统计检验和方差估计\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次提出（critical），R2交叉审阅同意升级。CaCLR vs baseline仅~3.4pp差距，无统计检验无法判断significance。\"\n  action_items:\n    - round: 1\n      action: \"至少5次random seed报告均值±SD；CaCLR vs baselines做paired bootstrap test\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"[Best] Pareto frontier术语缺乏形式化验证\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2认为不准确，R1部分反驳但同意需形式化验证。\"\n  action_items:\n    - round: 1\n      action: \"明确Pareto dominance判定标准；添加scatter plot；报告hypervolume\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"[Best] 四项贡献的新颖性均为增量性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2提出，R1部分同意（CaCLR有一定非平凡性）。\"\n  action_items:\n    - round: 1\n      action: \"更诚实定位为large-scale empirical study\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1+R2-Q2\"\n  summary: \"[Best] CaCLR 'zero-label'表述误导性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"改为'zero-correctness-label'并讨论parallel data需求\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4+R2-W2\"\n  summary: \"[Best] 全文16张表格、0张图\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方强烈一致。\"\n  action_items:\n    - round: 1\n      action: \"添加2-3个核心figure\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"[Best] Related Work仅~15行\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"扩展至1.5-2页\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"[Best] 'First systematic study'声明过强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"加限定语\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"[Best] CaCLR超参无sensitivity analysis\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"添加sensitivity plot\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"[Best] INT8验证范围过窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"跨架构验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"[Best] Very low resource tier仅4种语言\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"增加语言或标注preliminary\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"[Best] Probe训练细节缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"补充完整训练配置\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"[Best] CaCLR改进幅度有限\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2提出。\"\n  action_items:\n    - round: 1\n      action: \"补充cost-benefit分析\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n## Median Paper Issues\n- id: \"MED-R1-W1\"\n  summary: \"[Median] EN AUROC仅0.715-0.742，远低于同类工作0.80+，所有负面结果可能反映setup局限而非方法根本限制\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1在交叉审阅后新发现的Major confound。如果英语probe本身suboptimal（INT4量化+MoE routing），所有downstream负面结果（no Pareto, no CaCLR benefit, no decomposition）可能是'poor probes don't transfer'而非'transfer is fundamentally limited'。论文部分承认（Limitation 2）但未做FP16 dense对照实验。\"\n  action_items:\n    - round: 1\n      action: \"在FP16 dense模型（如pilot的7B模型）上重复核心实验作为对照；或明确将结论限定为'在量化MoE setup下'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W2\"\n  summary: \"[Median] 深层INT4/W4A16量化引入系统性depth-dependent偏差（最大-0.022），干扰Pareto frontier和CaCLR分析\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Table 22显示量化偏差随depth增大。Rank preservation在≥60-80% depth失效。Qwen3的14/20非单调pattern可能部分源于量化artifact而非MoE routing。1-2pp偏差在CaCLR效应量仅-0.010时足以改变结论。\"\n  action_items:\n    - round: 1\n      action: \"定量分析量化偏差对Pareto frontier和CaCLR结论的影响；理想情况下FP16重复关键层\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W4+R2-W2\"\n  summary: \"[Median] 23张表格、0张图——负面结论极适合可视化但完全缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。scatter plot可直观展示no-frontier、selectivity heatmap展示artifact分布、分组scatter展示Simpson's Paradox。表格密集削弱负面结论说服力。\"\n  action_items:\n    - round: 1\n      action: \"添加至少3张figure：no-frontier scatter、selectivity heatmap、Simpson's Paradox分组scatter\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W8+R2-W1\"\n  summary: \"[Median] 引用仍不足（~15篇），缺IRT/Belinkov/calibration基础文献；References section可能因排版丢失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。R2额外发现PDF中§7后直接是Appendix A，未见References section——可能格式问题。缺失：Lord 1980、Baker 2001（IRT）、Belinkov 2022（probing survey）、Guo et al. 2017（temp scaling）、Conneau et al. 2020、Pires et al. 2019。\"\n  action_items:\n    - round: 1\n      action: \"确认References section是否存在；扩展至30+篇\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W3\"\n  summary: \"[Median] Gemma 4 31B数据严重不对等——仅Table 14的3行摘要，无per-language/β-sweep/full comparison\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"三架构对比claim建立在不对等数据上：Qwen3/Llama4有详细数据，Gemma4仅有摘要。且Gemma4是FP16 dense，MoE模型是INT4——architecture vs scale/quantization无法区分。\"\n  action_items:\n    - round: 1\n      action: \"补充Gemma 4完整per-language数据和transfer comparison\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-M1\"\n  summary: \"[Median] MMD仅在1-D probe logits上测试，negative result scope被限制为'our instantiation doesn't work'而非'distributional matching doesn't work'\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1提出（初审标注为idea-level non-major），R2在Q4中也质疑是否测试过其他distributional matching（adversarial, OT）。论文有caveat（§3.2, §6）但Discussion中的推论过广。\"\n  action_items:\n    - round: 1\n      action: \"明确将negative result限定为1-D MMD；或补充activation-space MMD/OT实验\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W5\"\n  summary: \"[Median] Linear projection 'effect reversal zone' [0.48-0.68]覆盖16/20语言，practical recommendation近乎空洞\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1指出Table 15显示reversal zone太宽，§6的conditional recommendation仅适用~4/20语言。R2在W6中也指出类似张力。\"\n  action_items:\n    - round: 1\n      action: \"诚实报告practical recommendation的局限性；不声称'only viable path'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R2-W3\"\n  summary: \"[Median] CaCLR失败消除方法贡献——论文实质只剩control task方法论+负面结果\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2指出：如果CaCLR不是贡献，论文需要更聚焦地定位control task发现和negative result的独立价值。\"\n  action_items:\n    - round: 1\n      action: \"重新定位论文核心贡献为control task methodology + principled negative result\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R2-W4\"\n  summary: \"[Median] Pilot work（Qwen2.5-7B, Llama-3.1-8B）区分不充分——已发表还是未发表未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"如果已发表需正式引用；如果未发表应说明'our unpublished pilot'。\"\n  action_items:\n    - round: 1\n      action: \"明确pilot work的出版状态\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "xling_calib_direction",
    "issues_yaml": "## Best Paper (Round 1) Issues — preserved\nissues:\n- id: \"R1-N3+R2-N1\"\n  summary: \"[Best] 参考文献严重不足（仅8篇）且多条引用元数据错误/疑似虚构\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1通过web search发现Miao et al.作者名/标题不匹配、Zhou et al.年份/标题不匹配、Civelli et al.标题不匹配。R2列出7+个缺失文献领域。交叉审阅后双方一致认定critical，R2提出疑似fabricated citations的ethical concern。\"\n  action_items:\n    - round: 1\n      action: \"扩展引用至30+篇；逐条核查所有现有引用的作者名、标题、年份、venue\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1\"\n  summary: \"[Best] Abstract 72% vs 正文§5.2 81%数值矛盾——疑为h²=0.72与prescriptive accuracy混淆\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次发现，R2交叉审阅时确认并补充：h²(variance explained)与accuracy(分类准确率)是完全不同指标。双方一致critical。\"\n  action_items:\n    - round: 1\n      action: \"统一数字并明确72%和81%分别度量什么；修正Abstract\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"[Best] Abstract 'explains 25% of transfer gap'在正文和Table 5中无推导路径\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次发现Table 5的Share%为13%/87%，推不出25%。R2交叉审阅确认并将自己初审的W4升级为critical。\"\n  action_items:\n    - round: 1\n      action: \"删除或修正25%，给出明确推导路径\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4\"\n  summary: \"[Best] 全文Tables 1-16均为单次实验点估计，完全缺乏统计检验和方差估计\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1首次提出（critical），R2交叉审阅同意升级。CaCLR vs baseline仅~3.4pp差距，无统计检验无法判断significance。\"\n  action_items:\n    - round: 1\n      action: \"至少5次random seed报告均值±SD；CaCLR vs baselines做paired bootstrap test\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"[Best] Pareto frontier术语缺乏形式化验证\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2认为不准确，R1部分反驳但同意需形式化验证。\"\n  action_items:\n    - round: 1\n      action: \"明确Pareto dominance判定标准；添加scatter plot；报告hypervolume\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"[Best] 四项贡献的新颖性均为增量性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2提出，R1部分同意（CaCLR有一定非平凡性）。\"\n  action_items:\n    - round: 1\n      action: \"更诚实定位为large-scale empirical study\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1+R2-Q2\"\n  summary: \"[Best] CaCLR 'zero-label'表述误导性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"改为'zero-correctness-label'并讨论parallel data需求\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4+R2-W2\"\n  summary: \"[Best] 全文16张表格、0张图\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方强烈一致。\"\n  action_items:\n    - round: 1\n      action: \"添加2-3个核心figure\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"[Best] Related Work仅~15行\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"扩展至1.5-2页\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"[Best] 'First systematic study'声明过强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"加限定语\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"[Best] CaCLR超参无sensitivity analysis\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"添加sensitivity plot\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"[Best] INT8验证范围过窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"跨架构验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"[Best] Very low resource tier仅4种语言\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"增加语言或标注preliminary\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"[Best] Probe训练细节缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。\"\n  action_items:\n    - round: 1\n      action: \"补充完整训练配置\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"[Best] CaCLR改进幅度有限\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2提出。\"\n  action_items:\n    - round: 1\n      action: \"补充cost-benefit分析\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n## Median Paper Issues\n- id: \"MED-R1-W1\"\n  summary: \"[Median] EN AUROC仅0.715-0.742，远低于同类工作0.80+，所有负面结果可能反映setup局限而非方法根本限制\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1在交叉审阅后新发现的Major confound。如果英语probe本身suboptimal（INT4量化+MoE routing），所有downstream负面结果（no Pareto, no CaCLR benefit, no decomposition）可能是'poor probes don't transfer'而非'transfer is fundamentally limited'。论文部分承认（Limitation 2）但未做FP16 dense对照实验。\"\n  action_items:\n    - round: 1\n      action: \"在FP16 dense模型（如pilot的7B模型）上重复核心实验作为对照；或明确将结论限定为'在量化MoE setup下'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W2\"\n  summary: \"[Median] 深层INT4/W4A16量化引入系统性depth-dependent偏差（最大-0.022），干扰Pareto frontier和CaCLR分析\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Table 22显示量化偏差随depth增大。Rank preservation在≥60-80% depth失效。Qwen3的14/20非单调pattern可能部分源于量化artifact而非MoE routing。1-2pp偏差在CaCLR效应量仅-0.010时足以改变结论。\"\n  action_items:\n    - round: 1\n      action: \"定量分析量化偏差对Pareto frontier和CaCLR结论的影响；理想情况下FP16重复关键层\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W4+R2-W2\"\n  summary: \"[Median] 23张表格、0张图——负面结论极适合可视化但完全缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。scatter plot可直观展示no-frontier、selectivity heatmap展示artifact分布、分组scatter展示Simpson's Paradox。表格密集削弱负面结论说服力。\"\n  action_items:\n    - round: 1\n      action: \"添加至少3张figure：no-frontier scatter、selectivity heatmap、Simpson's Paradox分组scatter\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W8+R2-W1\"\n  summary: \"[Median] 引用仍不足（~15篇），缺IRT/Belinkov/calibration基础文献；References section可能因排版丢失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。R2额外发现PDF中§7后直接是Appendix A，未见References section——可能格式问题。缺失：Lord 1980、Baker 2001（IRT）、Belinkov 2022（probing survey）、Guo et al. 2017（temp scaling）、Conneau et al. 2020、Pires et al. 2019。\"\n  action_items:\n    - round: 1\n      action: \"确认References section是否存在；扩展至30+篇\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W3\"\n  summary: \"[Median] Gemma 4 31B数据严重不对等——仅Table 14的3行摘要，无per-language/β-sweep/full comparison\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"三架构对比claim建立在不对等数据上：Qwen3/Llama4有详细数据，Gemma4仅有摘要。且Gemma4是FP16 dense，MoE模型是INT4——architecture vs scale/quantization无法区分。\"\n  action_items:\n    - round: 1\n      action: \"补充Gemma 4完整per-language数据和transfer comparison\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-M1\"\n  summary: \"[Median] MMD仅在1-D probe logits上测试，negative result scope被限制为'our instantiation doesn't work'而非'distributional matching doesn't work'\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1提出（初审标注为idea-level non-major），R2在Q4中也质疑是否测试过其他distributional matching（adversarial, OT）。论文有caveat（§3.2, §6）但Discussion中的推论过广。\"\n  action_items:\n    - round: 1\n      action: \"明确将negative result限定为1-D MMD；或补充activation-space MMD/OT实验\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R1-W5\"\n  summary: \"[Median] Linear projection 'effect reversal zone' [0.48-0.68]覆盖16/20语言，practical recommendation近乎空洞\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1指出Table 15显示reversal zone太宽，§6的conditional recommendation仅适用~4/20语言。R2在W6中也指出类似张力。\"\n  action_items:\n    - round: 1\n      action: \"诚实报告practical recommendation的局限性；不声称'only viable path'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R2-W3\"\n  summary: \"[Median] CaCLR失败消除方法贡献——论文实质只剩control task方法论+负面结果\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2指出：如果CaCLR不是贡献，论文需要更聚焦地定位control task发现和negative result的独立价值。\"\n  action_items:\n    - round: 1\n      action: \"重新定位论文核心贡献为control task methodology + principled negative result\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MED-R2-W4\"\n  summary: \"[Median] Pilot work（Qwen2.5-7B, Llama-3.1-8B）区分不充分——已发表还是未发表未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"如果已发表需正式引用；如果未发表应说明'our unpublished pilot'。\"\n  action_items:\n    - round: 1\n      action: \"明确pilot work的出版状态\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-21T06:16:01.017873+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/review_issues.yaml\", \"bytes\": 11647}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-21T06:18:10.755963+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Median Paper\n\n**论文**: The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications\n**Tier**: Dream Median\n**目标 Venue**: Top ML venue (ACL-level)\n**审稿模式**: 圆桌会议（2 Reviewers, 1 轮 + 交叉审阅）\n**日期**: 2026-05-21\n\n---\n\n## Panel Summary\n\n| Reviewer | Focus | Initial | Post-discussion | Confidence |\n|----------|-------|---------|-----------------|------------|\n| R1 | Methods & Experiments | 4/5 (Weak Accept) | 2/5 (Reject) | 4/5 |\n| R2 | Novelty & Related Work | 3/5 (Findings) | 3/5 (Findings) | 4/5 |\n| **Consensus** | | | **2.5/5 (Weak Reject)** | |\n\n**R1 评分变动说明**: R1 初审给 4/5（0 Major issues），交叉审阅后发现两个 Major confound（低 EN AUROC + 量化偏差），下调至 2/5。这一修订是基于对实验 setup 局限性的更深入分析，而非受 R2 评分影响。\n\n**Overall Assessment**: Weak Reject — 论文在统计方法论和学术诚实度上显著优于同一 agenda 的 best-tier 版本，控制任务发现（37-42% artifact rate）具有 field-level 价值。但两个未解决的 Major confound（EN AUROC 仅 0.715-0.742、深层量化偏差）使得核心论点——\"跨语言 probe transfer 存在根本限制\"——无法与\"实验 setup 本身是瓶颈\"区分。控制任务发现可作为独立 Findings 级贡献提取。\n\n---\n\n## 1. Summary\n\n本文将跨语言 correctness probe transfer 研究从 pilot（7-8B 模型）扩展至 3 个大规模架构（Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense）× 20 语言 × 5 迁移条件。核心发现为系统性负面结论：depth-transferability Pareto frontier 不泛化、CaCLR distributional matching 方法有害（β sweep 3 OOM 均 d<0.2）、pilot 的 CKA-transfer 正相关是 Simpson's Paradox。最有价值的方法论贡献是将 Hewitt & Liang selectivity controls 引入跨语言 probing，发现 37-42% 的中低资源语言 probing 结果为 capacity artifacts。\n\n---\n\n## 2. Strengths\n\n- **S1 [Consensus]**: 控制任务方法论是最强贡献——将 Hewitt & Liang (2019) selectivity 系统扩展到 20 语言 × 多层，发现 LOW tier 42% artifact rate，HIGH tier 18%。selectivity-AUROC 相关 ρ=0.68 (p<0.001)。对整个跨语言 probing 社区有方法论警示意义，超越本文 scope。\n\n- **S2 [Consensus]**: 诚实的负面结果 framing——Abstract 开门见山 \"predominantly negative\"，每个 claim 都有适当 qualifier（\"suggestive\", \"qualitative\", \"principled negative result\"）。与 best-tier 论文的 overclaim 形成鲜明对比。\n\n- **S3 [Consensus]**: 统计方法论 above-average——Bonferroni correction、bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿全文。这在 probing 文献中属于上游标准，对负面结果论文尤为重要。\n\n- **S4 [Consensus]**: Simpson's Paradox falsification 有教科书级示范意义——5-language pilot 的 CKA-transfer 正相关在 20 languages 下崩溃为 non-significant（partial ρ=+0.14, p=0.22），是 ecological fallacy 在 NLP 中的生动案例。\n\n- **S5 [R1]**: CaCLR negative result 实验设计充分——β sweep 3 OOM (0.001→1.0)、两种架构、20 语言，monotonic degradation，配合 component ablation（每项净负），不留\"未充分调参\"的空间。\n\n- **S6 [R1]**: CKA 分析的自我纠正——pooled r=0.52 做 partial correlation controlling depth 后降为 r=0.18 (p=0.11)，主动降级为 suggestive。\n\n- **S7 [R2]**: 三档实践决策规则（ZS AUROC <0.30: 不可预测; [0.30, 0.65]: linear proj; >0.65: zero-shot 足够）有直接操作价值。\n\n- **S8 [R1]**: 内部一致性完美——Abstract 数字与正文完全吻合，无任何自相矛盾。13/13 实验计划全部覆盖。\n\n---\n\n## 3. Weaknesses\n\n### 3.1 Major Issues（影响核心论点可信度）\n\n**M1. 低 EN AUROC confound——所有负面结果可能反映 setup 局限而非方法根本限制** [R1 raised]\n\n所有架构的英语 probe AUROC 仅 0.715-0.742，远低于同类工作的 0.80+。如果英语 probe 本身 suboptimal（可能原因：INT4/W4A16 量化降低 correctness signals、MoE routing 引入 layer-wise noise），则所有 downstream 负面结论（no Pareto, no CaCLR benefit, no decomposition, no CKA predictive power）可能反映\"差的 probe 不迁移\"而非\"跨语言 probe transfer 存在根本限制\"。\n\n论文在 Limitation 2（§6）部分承认量化影响，但**未做 FP16 dense 对照实验**——如果在 FP16 7B 模型上（即 pilot setup）EN AUROC 达 0.80+ 且迁移成功，则负面结论是 setup-specific 而非 fundamental。这是论文核心论点（\"fundamental limitations\"）能否成立的关键缺失对照。\n\n**M2. 量化引入系统性 depth-dependent 偏差，直接干扰 Pareto 和 CaCLR 分析** [R1 raised]\n\nTable 22 显示 INT4 量化偏差随深度增大：Llama W4A16 Δ 从 -0.003 (20% depth) 到 -0.018 (95% depth)；Qwen INT4 从 -0.005 到 -0.022。Rank preservation 在 ≥60-80% depth 失效。这意味着：\n- Qwen3 的 14/20 非单调 pattern（归因于\"MoE routing effects\"）可能部分是量化 artifact\n- CaCLR 的效应量仅 Δ=-0.010，在 1-2pp 量化偏差下无法区分 true null 和 confounded null\n- Pareto frontier 分析中的深层数据不可信\n\n### 3.2 Moderate Issues\n\n**W1. MMD 仅在 1-D probe logits 上测试——negative result scope 被限制** [R1 raised, R2 endorsed]\n\n§3.2 自己承认 \"design limitation: can only match marginal distributions of scalar outputs\"。但 §6 的推论隐含更广泛的 claim（distributional matching 全部失败）。未测试 MMD 在高维 activation space 或 optimal transport 的效果。严格来说，negative result 仅关闭了 \"1-D probe output MMD matching\" 这一条路。\n\n**W2. Gemma 4 数据严重不对等** [R1 raised]\n\n仅出现在 Table 14（appendix 3 行摘要），无 per-language breakdown、β sweep、full transfer comparison。三架构对比 claim 建立在不对等数据上。且 Gemma4 是 FP16 dense 而 MoE 模型是 INT4——\"dense shows clearer Pareto\" 无法区分 architecture vs scale/quantization effect。\n\n**W3. Linear projection \"only viable path\" overclaim** [R1 raised, R2 endorsed]\n\nTable 15 的 effect-reversal zone [0.48-0.68] 覆盖 16/20 语言。§6 的 conditional recommendation（\"if ZS < 0.50, linear proj likely helps\"）仅适用 ~4/20 语言。practical recommendation 对大部分目标语言近乎空洞。\n\n### 3.3 Minor Issues\n\n**W4. 23 张表格、0 张图** [Consensus]\n\n与 best-tier 论文共享的缺陷。负面结论极适合可视化：no-frontier scatter plot、selectivity heatmap、Simpson's Paradox 分组 scatter。表格密集削弱说服力。\n\n**W5. 引用仍不足（~15 篇），References section 可能因排版丢失** [Consensus]\n\n缺 IRT 基础文献（Lord 1980, Baker 2001）、Belinkov (2022) probing survey、Guo et al. (2017) temperature scaling、Conneau et al. (2020)、Pires et al. (2019)。R2 报告 PDF 中 §7 后直接是 Appendix A，未见 References section。\n\n**W6. CaCLR 失败消除方法贡献** [R2]\n\n论文实质只剩 (1) 控制任务方法论 (2) 负面实验结果。对 main conference 贡献数量不足。\n\n**W7. Pilot work 区分不充分** [R2]\n\n\"Pilot studies on Qwen2.5-7B and Llama-3.1-8B\" 未说明已发表还是未发表。\n\n**W8. Difficulty decomposition 负面结论解释不足** [R2]\n\nIRT R²=0.40，difficulty probe 质量差可能导致 project-out 失败。§5.4 一段话否定但未分析为什么大模型上失败（scale? 量化? 数据?）。\n\n**W9. Llama 4 Scout per-language 分析 underpowered** [R1]\n\n仅 12 probed layers，n=12 的 Spearman test 统计功效仅 0.35-0.50 for ρ=-0.40。0/20 显著可能是 power 不足而非真阴性。\n\n---\n\n## 4. Reviewer Consensus [AGREE]\n\n1. **控制任务发现是论文锚点**——37-42% artifact rate 有 field-level 价值，是最值得保留的贡献\n2. **统计方法论显著优于 best-tier 版本**——Bonferroni、CIs、Cohen's d 贯穿全文\n3. **内部一致性完美**——无数字矛盾（best-tier 有 72%/81%/25% 三处）\n4. **零可视化**是两篇论文共享的严重表述问题\n5. **引用仍不够**，虽然比 best-tier 改善\n6. **诚实 framing** 是正面品质但不补偿 soundness 问题\n\n---\n\n## 5. Reviewer Divergence\n\n**5.1 负面结果是否可信（validity）vs 是否重要（significance）**\n\n- **R1 (2/5)**: 负面结果的可信度不足——低 EN AUROC + 量化偏差意味着可能是\"setup 不行\"而非\"方法不行\"。核心论点（fundamental limitations）在未排除 setup confound 的情况下不成立。\n- **R2 (3/5)**: 负面结果本身可信，但\"so what\"不够——CaCLR 失败消除了方法贡献，剩余贡献（控制任务 + negative result）对 Findings track 可接受但对 main conference 不足。\n\n**Director 判断**: R1 的 confound 分析（M1, M2）是实质性的——如果 EN AUROC 达 0.80+ 时结论翻转，则整篇论文的核心论点不成立。这比 R2 的\"不够兴奋\"更根本。同时 R2 对贡献结构的判断（only control tasks + negatives）也成立。综合评分向 R1 倾斜。\n\n**5.2 评分变动**\n\nR1 从初审 4/5 大幅下调至 2/5，变动原因明确（发现 2 个 Major confound）且有数据支撑。这不是情绪性变动，而是基于 Table 22（量化偏差）和 EN AUROC 数据的 analytical revision。\n\n---\n\n## 6. Questions for Authors\n\n1. **[Critical]** 在 FP16 dense 模型（如 pilot 的 Qwen2.5-7B / Llama-3.1-8B）上，同一 probing pipeline 的 EN AUROC 是否达 0.80+？如果是，负面结论是 setup-specific 而非 fundamental。\n2. Qwen3 的 14/20 非单调 pattern 中，多少在校正 Table 22 的量化偏差后仍然非单调？\n3. CaCLR 的 MMD term 以外，是否测试过其他 distributional matching（adversarial alignment, optimal transport）？\n4. IRT difficulty probe R²=0.40——是否尝试过更复杂的 difficulty model（2-PL IRT, neural IRT）？\n5. Selectivity 阈值 < 0.05 的选择依据？改为 0.10 或 0.03 时 42% 如何变化？\n6. Simpson's Paradox 的 partial ρ=+0.14 控制了哪些变量？\n7. Gemma 4 31B 的完整 per-language 数据和 transfer comparison 是否可用？\n8. Linear projection 对低资源语言（am, yo, my）所需的 100-200 parallel pairs 在实际中是否可获得？\n9. PDF 中 References section 是否因排版问题丢失？\n\n---\n\n## 7. Missing References\n\n1. Conneau et al. (2020) — XLM-R / cross-lingual layer-wise analysis\n2. Pires et al. (2019) — \"How multilingual is Multilingual BERT?\"\n3. Belinkov (2022) — Probing survey\n4. Lord (1980) / Baker (2001) — IRT foundational literature\n5. Guo et al. (2017) — Temperature scaling\n6. Keleg & Magdy (2023) — Multilingual calibration\n7. Ganin et al. (2016) / Long et al. (2015) — Domain adaptation\n8. Fedus et al. (2022) / Zoph et al. (2022) — MoE architecture analysis\n\n---\n\n## 8. External Review (Stanford Agentic Reviewer)\n\n**状态: pending（已请求 best paper，median paper 未单独请求）**\n\n---\n\n## 9. Visual Layout Check（非评分项）\n\n**状态: not_started**（review_paper_pdf_path 未配置）\n\n---\n\n## 10. Overall Assessment\n\n**评分: 2.5/5 — Weak Reject**\n\n**置信度: 4/5**\n\n**核心判断**: 这篇论文在学术品质上显著优于同一 agenda 的 best-tier 版本——内部一致性完美、统计方法论扎实、负面结果 framing 诚实。控制任务发现（37-42% artifact rate）具有超越本文的方法论价值。\n\n但两个 Major confound 使核心论点无法成立：\n1. 所有模型的 EN AUROC 仅 0.715-0.742（vs 同类工作 0.80+），所有负面结果可能是 \"poor probes → poor transfer\" 而非 \"transfer is fundamentally limited\"\n2. 深层量化偏差（最大 -0.022）在效应量仅 ~0.010 的实验中是致命的 confound\n\n**修改建议优先级**:\n1. [紧急] FP16 dense 对照实验——在 pilot 的 7B 模型上用同一 pipeline 验证 EN AUROC；如果 >0.80 且迁移成功，需根本重构论文论点\n2. [紧急] 量化偏差定量分析——校正 Table 22 的 depth-dependent bias 后重新评估 Pareto 和 CaCLR 结论\n3. [重要] 添加 2-3 个核心 figure（no-frontier scatter、selectivity heatmap、Simpson's Paradox）\n4. [重要] 补充 Gemma 4 完整数据，确保三架构对比对等\n5. [重要] 确认 References section 完整性；扩展至 30+ 篇\n6. [建议] 将论文核心贡献重新定位为\"控制任务方法论 + 在量化大模型上的 setup-specific negative result\"\n7. [建议] Linear projection recommendation 诚实报告 effect-reversal zone 的覆盖问题\n\n**与 Best-tier 对比**:\n\n| 维度 | Best (2.5/5 Weak Reject) | Median (2.5/5 Weak Reject) |\n|------|--------------------------|---------------------------|\n| 内部一致性 | 差（72%/81%/25% 三处矛盾） | 完美 |\n| 统计严谨性 | 差（无 CI/无检验） | 好（Bonferroni/CIs/Cohen's d） |\n| 学术诚信 | 差（疑似 fabricated refs） | 好（诚实负面结果） |\n| 核心缺陷 | 可信度危机 | Setup confound |\n| 可修复性 | 低（需补统计+重写引用+修数字） | 中（需 FP16 对照实验） |\n| 控制任务 | 无 | 有（42% artifact，field-level 价值） |\n\n**建议**: Median 版的修复路径更清晰——如果 FP16 对照实验确认负面结论是 fundamental 而非 setup-specific，论文可升级为 Findings 或 borderline main conference。如果对照实验翻转结论，则论文需根本重构但控制任务发现仍有独立价值。\n\n---\n\n## 11. Detailed Comments\n\n### §1 Introduction\n- \"First large-scale study\" 需加限定语（Civelli, Xiao 先行工作）\n- 三段叙事（discovery + negative result + recommendation）结构好\n\n### §2 Related Work\n- 覆盖 5-6 个子方向，结构合理\n- 仍缺 Conneau/Pires/Belinkov 等核心引用\n\n### §3 Methods\n- §3.2 CaCLR 公式说 \"two regularization terms\" 但实际有三项额外 loss——需修正\n- MMD on 1-D logits 的 scope 限制需更明确 caveat\n\n### §4 Experimental Setup\n- 统计方法论描述清楚（Bonferroni, bootstrap, permutation）\n- 量化选择的 justification 需加强——为什么不用 FP16 做 baseline？\n\n### §5 Results\n- §5.1 Gemma4 \"moderately clear frontier\" vs Summary \"does not generalize\" 有轻微矛盾\n- §5.3 Simpson's Paradox 分析方法论值得肯定\n- §5.4 Difficulty decomposition 否定太快，未分析失败原因\n- §5.5 Control task finding 是论文锚点，分析充分\n\n### §6 Discussion / §7 Conclusion\n- \"Fundamental limitations\" framing 在未排除 setup confound 下不成立\n- 三档决策规则有价值但 reversal zone 覆盖问题需坦诚讨论\n- Limitations 部分诚实但也暴露实验局限性\n\n### Appendix\n- Table 14 Gemma4 数据需大幅扩充\n- Table 22 量化分析数据存在但论文未充分利用来 qualify 主文结论",
  "project": "xling_calib_direction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Median Paper\n\n**论文**: The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications\n**Tier**: Dream Median\n**目标 Venue**: Top ML venue (ACL-level)\n**审稿模式**: 圆桌会议（2 Reviewers, 1 轮 + 交叉审阅）\n**日期**: 2026-05-21\n\n---\n\n## Panel Summary\n\n| Reviewer | Focus | Initial | Post-discussion | Confidence |\n|----------|-------|---------|-----------------|------------|\n| R1 | Methods & Experiments | 4/5 (Weak Accept) | 2/5 (Reject) | 4/5 |\n| R2 | Novelty & Related Work | 3/5 (Findings) | 3/5 (Findings) | 4/5 |\n| **Consensus** | | | **2.5/5 (Weak Reject)** | |\n\n**R1 评分变动说明**: R1 初审给 4/5（0 Major issues），交叉审阅后发现两个 Major confound（低 EN AUROC + 量化偏差），下调至 2/5。这一修订是基于对实验 setup 局限性的更深入分析，而非受 R2 评分影响。\n\n**Overall Assessment**: Weak Reject — 论文在统计方法论和学术诚实度上显著优于同一 agenda 的 best-tier 版本，控制任务发现（37-42% artifact rate）具有 field-level 价值。但两个未解决的 Major confound（EN AUROC 仅 0.715-0.742、深层量化偏差）使得核心论点——\"跨语言 probe transfer 存在根本限制\"——无法与\"实验 setup 本身是瓶颈\"区分。控制任务发现可作为独立 Findings 级贡献提取。\n\n---\n\n## 1. Summary\n\n本文将跨语言 correctness probe transfer 研究从 pilot（7-8B 模型）扩展至 3 个大规模架构（Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense）× 20 语言 × 5 迁移条件。核心发现为系统性负面结论：depth-transferability Pareto frontier 不泛化、CaCLR distributional matching 方法有害（β sweep 3 OOM 均 d<0.2）、pilot 的 CKA-transfer 正相关是 Simpson's Paradox。最有价值的方法论贡献是将 Hewitt & Liang selectivity controls 引入跨语言 probing，发现 37-42% 的中低资源语言 probing 结果为 capacity artifacts。\n\n---\n\n## 2. Strengths\n\n- **S1 [Consensus]**: 控制任务方法论是最强贡献——将 Hewitt & Liang (2019) selectivity 系统扩展到 20 语言 × 多层，发现 LOW tier 42% artifact rate，HIGH tier 18%。selectivity-AUROC 相关 ρ=0.68 (p<0.001)。对整个跨语言 probing 社区有方法论警示意义，超越本文 scope。\n\n- **S2 [Consensus]**: 诚实的负面结果 framing——Abstract 开门见山 \"predominantly negative\"，每个 claim 都有适当 qualifier（\"suggestive\", \"qualitative\", \"principled negative result\"）。与 best-tier 论文的 overclaim 形成鲜明对比。\n\n- **S3 [Consensus]**: 统计方法论 above-average——Bonferroni correction、bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿全文。这在 probing 文献中属于上游标准，对负面结果论文尤为重要。\n\n- **S4 [Consensus]**: Simpson's Paradox falsification 有教科书级示范意义——5-language pilot 的 CKA-transfer 正相关在 20 languages 下崩溃为 non-significant（partial ρ=+0.14, p=0.22），是 ecological fallacy 在 NLP 中的生动案例。\n\n- **S5 [R1]**: CaCLR negative result 实验设计充分——β sweep 3 OOM (0.001→1.0)、两种架构、20 语言，monotonic degradation，配合 component ablation（每项净负），不留\"未充分调参\"的空间。\n\n- **S6 [R1]**: CKA 分析的自我纠正——pooled r=0.52 做 partial correlation controlling depth 后降为 r=0.18 (p=0.11)，主动降级为 suggestive。\n\n- **S7 [R2]**: 三档实践决策规则（ZS AUROC <0.30: 不可预测; [0.30, 0.65]: linear proj; >0.65: zero-shot 足够）有直接操作价值。\n\n- **S8 [R1]**: 内部一致性完美——Abstract 数字与正文完全吻合，无任何自相矛盾。13/13 实验计划全部覆盖。\n\n---\n\n## 3. Weaknesses\n\n### 3.1 Major Issues（影响核心论点可信度）\n\n**M1. 低 EN AUROC confound——所有负面结果可能反映 setup 局限而非方法根本限制** [R1 raised]\n\n所有架构的英语 probe AUROC 仅 0.715-0.742，远低于同类工作的 0.80+。如果英语 probe 本身 suboptimal（可能原因：INT4/W4A16 量化降低 correctness signals、MoE routing 引入 layer-wise noise），则所有 downstream 负面结论（no Pareto, no CaCLR benefit, no decomposition, no CKA predictive power）可能反映\"差的 probe 不迁移\"而非\"跨语言 probe transfer 存在根本限制\"。\n\n论文在 Limitation 2（§6）部分承认量化影响，但**未做 FP16 dense 对照实验**——如果在 FP16 7B 模型上（即 pilot setup）EN AUROC 达 0.80+ 且迁移成功，则负面结论是 setup-specific 而非 fundamental。这是论文核心论点（\"fundamental limitations\"）能否成立的关键缺失对照。\n\n**M2. 量化引入系统性 depth-dependent 偏差，直接干扰 Pareto 和 CaCLR 分析** [R1 raised]\n\nTable 22 显示 INT4 量化偏差随深度增大：Llama W4A16 Δ 从 -0.003 (20% depth) 到 -0.018 (95% depth)；Qwen INT4 从 -0.005 到 -0.022。Rank preservation 在 ≥60-80% depth 失效。这意味着：\n- Qwen3 的 14/20 非单调 pattern（归因于\"MoE routing effects\"）可能部分是量化 artifact\n- CaCLR 的效应量仅 Δ=-0.010，在 1-2pp 量化偏差下无法区分 true null 和 confounded null\n- Pareto frontier 分析中的深层数据不可信\n\n### 3.2 Moderate Issues\n\n**W1. MMD 仅在 1-D probe logits 上测试——negative result scope 被限制** [R1 raised, R2 endorsed]\n\n§3.2 自己承认 \"design limitation: can only match marginal distributions of scalar outputs\"。但 §6 的推论隐含更广泛的 claim（distributional matching 全部失败）。未测试 MMD 在高维 activation space 或 optimal transport 的效果。严格来说，negative result 仅关闭了 \"1-D probe output MMD matching\" 这一条路。\n\n**W2. Gemma 4 数据严重不对等** [R1 raised]\n\n仅出现在 Table 14（appendix 3 行摘要），无 per-language breakdown、β sweep、full transfer comparison。三架构对比 claim 建立在不对等数据上。且 Gemma4 是 FP16 dense 而 MoE 模型是 INT4——\"dense shows clearer Pareto\" 无法区分 architecture vs scale/quantization effect。\n\n**W3. Linear projection \"only viable path\" overclaim** [R1 raised, R2 endorsed]\n\nTable 15 的 effect-reversal zone [0.48-0.68] 覆盖 16/20 语言。§6 的 conditional recommendation（\"if ZS < 0.50, linear proj likely helps\"）仅适用 ~4/20 语言。practical recommendation 对大部分目标语言近乎空洞。\n\n### 3.3 Minor Issues\n\n**W4. 23 张表格、0 张图** [Consensus]\n\n与 best-tier 论文共享的缺陷。负面结论极适合可视化：no-frontier scatter plot、selectivity heatmap、Simpson's Paradox 分组 scatter。表格密集削弱说服力。\n\n**W5. 引用仍不足（~15 篇），References section 可能因排版丢失** [Consensus]\n\n缺 IRT 基础文献（Lord 1980, Baker 2001）、Belinkov (2022) probing survey、Guo et al. (2017) temperature scaling、Conneau et al. (2020)、Pires et al. (2019)。R2 报告 PDF 中 §7 后直接是 Appendix A，未见 References section。\n\n**W6. CaCLR 失败消除方法贡献** [R2]\n\n论文实质只剩 (1) 控制任务方法论 (2) 负面实验结果。对 main conference 贡献数量不足。\n\n**W7. Pilot work 区分不充分** [R2]\n\n\"Pilot studies on Qwen2.5-7B and Llama-3.1-8B\" 未说明已发表还是未发表。\n\n**W8. Difficulty decomposition 负面结论解释不足** [R2]\n\nIRT R²=0.40，difficulty probe 质量差可能导致 project-out 失败。§5.4 一段话否定但未分析为什么大模型上失败（scale? 量化? 数据?）。\n\n**W9. Llama 4 Scout per-language 分析 underpowered** [R1]\n\n仅 12 probed layers，n=12 的 Spearman test 统计功效仅 0.35-0.50 for ρ=-0.40。0/20 显著可能是 power 不足而非真阴性。\n\n---\n\n## 4. Reviewer Consensus [AGREE]\n\n1. **控制任务发现是论文锚点**——37-42% artifact rate 有 field-level 价值，是最值得保留的贡献\n2. **统计方法论显著优于 best-tier 版本**——Bonferroni、CIs、Cohen's d 贯穿全文\n3. **内部一致性完美**——无数字矛盾（best-tier 有 72%/81%/25% 三处）\n4. **零可视化**是两篇论文共享的严重表述问题\n5. **引用仍不够**，虽然比 best-tier 改善\n6. **诚实 framing** 是正面品质但不补偿 soundness 问题\n\n---\n\n## 5. Reviewer Divergence\n\n**5.1 负面结果是否可信（validity）vs 是否重要（significance）**\n\n- **R1 (2/5)**: 负面结果的可信度不足——低 EN AUROC + 量化偏差意味着可能是\"setup 不行\"而非\"方法不行\"。核心论点（fundamental limitations）在未排除 setup confound 的情况下不成立。\n- **R2 (3/5)**: 负面结果本身可信，但\"so what\"不够——CaCLR 失败消除了方法贡献，剩余贡献（控制任务 + negative result）对 Findings track 可接受但对 main conference 不足。\n\n**Director 判断**: R1 的 confound 分析（M1, M2）是实质性的——如果 EN AUROC 达 0.80+ 时结论翻转，则整篇论文的核心论点不成立。这比 R2 的\"不够兴奋\"更根本。同时 R2 对贡献结构的判断（only control tasks + negatives）也成立。综合评分向 R1 倾斜。\n\n**5.2 评分变动**\n\nR1 从初审 4/5 大幅下调至 2/5，变动原因明确（发现 2 个 Major confound）且有数据支撑。这不是情绪性变动，而是基于 Table 22（量化偏差）和 EN AUROC 数据的 analytical revision。\n\n---\n\n## 6. Questions for Authors\n\n1. **[Critical]** 在 FP16 dense 模型（如 pilot 的 Qwen2.5-7B / Llama-3.1-8B）上，同一 probing pipeline 的 EN AUROC 是否达 0.80+？如果是，负面结论是 setup-specific 而非 fundamental。\n2. Qwen3 的 14/20 非单调 pattern 中，多少在校正 Table 22 的量化偏差后仍然非单调？\n3. CaCLR 的 MMD term 以外，是否测试过其他 distributional matching（adversarial alignment, optimal transport）？\n4. IRT difficulty probe R²=0.40——是否尝试过更复杂的 difficulty model（2-PL IRT, neural IRT）？\n5. Selectivity 阈值 < 0.05 的选择依据？改为 0.10 或 0.03 时 42% 如何变化？\n6. Simpson's Paradox 的 partial ρ=+0.14 控制了哪些变量？\n7. Gemma 4 31B 的完整 per-language 数据和 transfer comparison 是否可用？\n8. Linear projection 对低资源语言（am, yo, my）所需的 100-200 parallel pairs 在实际中是否可获得？\n9. PDF 中 References section 是否因排版问题丢失？\n\n---\n\n## 7. Missing References\n\n1. Conneau et al. (2020) — XLM-R / cross-lingual layer-wise analysis\n2. Pires et al. (2019) — \"How multilingual is Multilingual BERT?\"\n3. Belinkov (2022) — Probing survey\n4. Lord (1980) / Baker (2001) — IRT foundational literature\n5. Guo et al. (2017) — Temperature scaling\n6. Keleg & Magdy (2023) — Multilingual calibration\n7. Ganin et al. (2016) / Long et al. (2015) — Domain adaptation\n8. Fedus et al. (2022) / Zoph et al. (2022) — MoE architecture analysis\n\n---\n\n## 8. External Review (Stanford Agentic Reviewer)\n\n**状态: pending（已请求 best paper，median paper 未单独请求）**\n\n---\n\n## 9. Visual Layout Check（非评分项）\n\n**状态: not_started**（review_paper_pdf_path 未配置）\n\n---\n\n## 10. Overall Assessment\n\n**评分: 2.5/5 — Weak Reject**\n\n**置信度: 4/5**\n\n**核心判断**: 这篇论文在学术品质上显著优于同一 agenda 的 best-tier 版本——内部一致性完美、统计方法论扎实、负面结果 framing 诚实。控制任务发现（37-42% artifact rate）具有超越本文的方法论价值。\n\n但两个 Major confound 使核心论点无法成立：\n1. 所有模型的 EN AUROC 仅 0.715-0.742（vs 同类工作 0.80+），所有负面结果可能是 \"poor probes → poor transfer\" 而非 \"transfer is fundamentally limited\"\n2. 深层量化偏差（最大 -0.022）在效应量仅 ~0.010 的实验中是致命的 confound\n\n**修改建议优先级**:\n1. [紧急] FP16 dense 对照实验——在 pilot 的 7B 模型上用同一 pipeline 验证 EN AUROC；如果 >0.80 且迁移成功，需根本重构论文论点\n2. [紧急] 量化偏差定量分析——校正 Table 22 的 depth-dependent bias 后重新评估 Pareto 和 CaCLR 结论\n3. [重要] 添加 2-3 个核心 figure（no-frontier scatter、selectivity heatmap、Simpson's Paradox）\n4. [重要] 补充 Gemma 4 完整数据，确保三架构对比对等\n5. [重要] 确认 References section 完整性；扩展至 30+ 篇\n6. [建议] 将论文核心贡献重新定位为\"控制任务方法论 + 在量化大模型上的 setup-specific negative result\"\n7. [建议] Linear projection recommendation 诚实报告 effect-reversal zone 的覆盖问题\n\n**与 Best-tier 对比**:\n\n| 维度 | Best (2.5/5 Weak Reject) | Median (2.5/5 Weak Reject) |\n|------|--------------------------|---------------------------|\n| 内部一致性 | 差（72%/81%/25% 三处矛盾） | 完美 |\n| 统计严谨性 | 差（无 CI/无检验） | 好（Bonferroni/CIs/Cohen's d） |\n| 学术诚信 | 差（疑似 fabricated refs） | 好（诚实负面结果） |\n| 核心缺陷 | 可信度危机 | Setup confound |\n| 可修复性 | 低（需补统计+重写引用+修数字） | 中（需 FP16 对照实验） |\n| 控制任务 | 无 | 有（42% artifact，field-level 价值） |\n\n**建议**: Median 版的修复路径更清晰——如果 FP16 对照实验确认负面结论是 fundamental 而非 setup-specific，论文可升级为 Findings 或 borderline main conference。如果对照实验翻转结论，则论文需根本重构但控制任务发现仍有独立价值。\n\n---\n\n## 11. Detailed Comments\n\n### §1 Introduction\n- \"First large-scale study\" 需加限定语（Civelli, Xiao 先行工作）\n- 三段叙事（discovery + negative result + recommendation）结构好\n\n### §2 Related Work\n- 覆盖 5-6 个子方向，结构合理\n- 仍缺 Conneau/Pires/Belinkov 等核心引用\n\n### §3 Methods\n- §3.2 CaCLR 公式说 \"two regularization terms\" 但实际有三项额外 loss——需修正\n- MMD on 1-D logits 的 scope 限制需更明确 caveat\n\n### §4 Experimental Setup\n- 统计方法论描述清楚（Bonferroni, bootstrap, permutation）\n- 量化选择的 justification 需加强——为什么不用 FP16 做 baseline？\n\n### §5 Results\n- §5.1 Gemma4 \"moderately clear frontier\" vs Summary \"does not generalize\" 有轻微矛盾\n- §5.3 Simpson's Paradox 分析方法论值得肯定\n- §5.4 Difficulty decomposition 否定太快，未分析失败原因\n- §5.5 Control task finding 是论文锚点，分析充分\n\n### §6 Discussion / §7 Conclusion\n- \"Fundamental limitations\" framing 在未排除 setup confound 下不成立\n- 三档决策规则有价值但 reversal zone 覆盖问题需坦诚讨论\n- Limitations 部分诚实但也暴露实验局限性\n\n### Appendix\n- Table 14 Gemma4 数据需大幅扩充\n- Table 22 量化分析数据存在但论文未充分利用来 qualify 主文结论",
    "project": "xling_calib_direction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
    "force_resubmit": "True"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-21T06:18:15.482397+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_74ae31a7dc5ae9d419ba9a89bccc89c0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4726
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-21T06:18:20.653606+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '[Best] 完整审稿流程（已投递）', 'status': 'completed', 'activeForm': 'Best paper 审稿已完成'}, {'content': '[Median] 完整审稿流程（已投递）', 'status': 'completed', 'activeForm': 'Median paper 审稿已完成'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '[Best] 完整审稿流程（已投递）', 'status': 'completed', 'activeForm': 'Best paper 审稿已完成'}, {'content': '[Median] 完整审稿流程（已投递）', 'status': 'completed', 'activeForm': 'Median paper 审稿已完成'}]"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-21T06:18:20.704318+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 106 · 2026-05-21T06:18:43.514946+00:00_

**Median paper 审稿报告已投递。**

两篇 dream paper 的审稿圆桌会议均已完成。汇总：

| | Best Paper | Median Paper |
|---|---|---|
| **评分** | 2.5/5 Weak Reject | 2.5/5 Weak Reject |
| **核心问题** | 可信度危机（数字矛盾 + 疑似虚构引用 + 零统计检验） | Setup confound（EN AUROC 0.72 + 量化偏差 → 负面结论可能非 fundamental） |
| **最强优点** | 实验规模 + CaCLR Pareto shift 概念 | 控制任务发现（42% artifact）+ 统计严谨性 + 诚实 framing |
| **可修复性** | 低 | 中（FP16 对照实验可判定） |
| **共享缺陷** | 零可视化、引用不足 | 零可视化、引用不足 |

**Median 版在学术品质上全面优于 Best 版**（内部一致性、统计方法、学术诚信），但同样获得 2.5/5，原因不同：Best 版败在可信度，Median 版败在 setup confound 未排除导致核心论点（fundamental limitations）无法成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 12

4 recorded events

### User

_source line 107 · 2026-05-21T06:18:43.518970+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉审阅回应（对 Reviewer 1 Round 1 意见，Median/Worst Paper）

---

### Methods & Experiments Weaknesses 逐条回应

**[AGREE] R1-W-M1: MMD 在 1-D probe logits 上操作限制了 negative result scope**

同意，且从 Novelty 角度补充这对论文贡献价值的影响：

R1 准确指出 CaCLR 的 MMD 仅在 1-D probe output 上操作，未测试 (a) activation space MMD, (b) optimal transport/Sinkhorn。这直接影响我在独立审稿中提出的 Q4——"只测一种 distributional matching 就断言 distributional matching 不可行可能过于草率。"

从 Novelty 角度，这限制了论文第二大贡献（comprehensive negative result）的 scope：
- 论文 Abstract 说 "CaCLR, a distributional-matching method combining BEC, calibration, and MMD consistency losses, is uniformly harmful"——但严格来说，只有 "1-D MMD on probe logits" 被证伪
- 如果有人在 activation space（几千维）做 MMD 或用 adversarial domain adaptation（Ben-David et al. 理论框架的标准实现），结论可能完全不同
- 论文 §3.2 和 §6 确实有 caveat（R1 确认了这一点），逻辑自洽但 **negative result 的 generality 受限意味着其对 community 的警示价值也受限**

这是我给 Excitement 3/5 而非更高分的一个原因——负面结论的 scope 不够广，无法真正"关闭"这个研究方向。

**建议**：如果作者补充 activation-space MMD 或 adversarial alignment 的实验（即使也失败），negative result 的价值会显著提升。

---

**[AGREE] R1-W-M2: Table 1 未展示完整 24 层 × 20 语言数据**

同意。这也呼应了我在独立审稿中的 W2（零可视化）。完整的 depth profile 是验证"no Pareto frontier"结论的关键证据——如果读者看不到完整数据，只能信任作者的 summary statistics。一张 heatmap（layer × language, colored by AUROC）可以同时解决数据展示和可视化两个问题。

---

**[AGREE] R1-W-M3: Gemma 4 31B 数据不对等**

同意，且从 Novelty/Positioning 角度，这对论文的三架构对比 claim 有直接影响：

- 论文标题和 Abstract 声称覆盖"3 architectures"，但 Gemma 4 仅在 Appendix B（Table 14, p.11）出现 3 行摘要数据
- 无 per-language breakdown、无 β sweep、无 control task analysis for Gemma
- 论文的核心 claim 之一是 "architecture-dependent"——但如果 Gemma 的数据不完整，这个 claim 实质上只基于 Qwen3 和 Llama 4 两个架构，两者都是 MoE

从 Novelty 角度，这削弱了"跨架构"贡献的说服力。特别是 Gemma 4 31B 是唯一的 Dense 架构——如果 Dense 和 MoE 的表现有本质差异，缺少 Gemma 的完整数据意味着论文无法回答 "MoE vs Dense" 这个关键问题。

**这一点也是我与 R1 评分分歧的来源之一**（见下方讨论）。

---

**[AGREE] R1-W-M4: IRT R²=0.40 较低，difficulty decomposition 解释力有限**

同意。我在独立审稿中将此归为 W5（"Difficulty decomposition 的负面结论太快"），角度略有不同但结论一致。R1 指出的技术问题更精确：R²=0.40 意味着 projecting out difficulty 后残差仍含 60% 未解释的 difficulty signal，这使得 "capability-specific" 残差的解释不可靠。论文将此自我降级为 qualitative claim 是诚实的，但也意味着这部分分析不构成实质性贡献。

---

### Novelty Weaknesses 逐条回应

**[AGREE] R1-W-N1: 14 篇引用仍低**

完全同意。我在独立审稿中详细列出了缺失文献：Conneau et al. (2020), Pires et al. (2019), Belinkov (2022), Keleg & Magdy (2023)。R1 补充了 Guo et al. temperature scaling 和 MoE 分析文献，进一步扩大了遗漏清单。

此外，我在独立审稿中提出了一个更严重的问题：**论文 PDF 中 References section 似乎缺失**——§7 Conclusion 后直接是 Appendix A，未见参考文献列表。如果这是排版错误，需要修复；如果参考文献确实只有 14 篇，仍低于顶会标准（30-50 篇）。

关于 R1 提到的"部分引用可能存在 accuracy issue"：鉴于前一篇论文（positive framing 版本）已被发现有多条疑似 fabricated references（Miao et al. 作者名不匹配、Zhou et al. 年份/标题不匹配、Civelli et al. 标题不匹配），本文的引用准确性需要同样严格的核查。**如果两篇论文共享同一参考文献库，accuracy issues 可能是系统性的。**

---

**[AGREE] R1-W-N2: "First systematic study" claim 需 qualification**

同意，这与我在独立审稿中对前一篇论文的 W3 一致。建议改为 "the first large-scale negative result study" 或 "the first study to apply probing control tasks to cross-lingual calibration transfer"——后者更准确地反映论文的真正新贡献。

---

**[REBUT] R1-W-N3: CaCLR negative result novelty 取决于 MMD on probe outputs 是否为 "obvious limitation"**

部分不同意。R1 认为 CaCLR 的 1-D MMD 限制可能使负面结论"显而易见"，暗示这降低了 novelty。但我认为：

1. **事前并不 obvious**：distributional matching 在 domain adaptation 中广泛使用，Ben-David et al. 的理论框架（论文 §2 已引用）正是基于减少 marginal distribution divergence。在 probe output space 上做 MMD 是该理论框架的自然实现——如果没有人做过实验，不能仅凭直觉说"当然不行"。
2. **论文的 framing 是诚实的**：§3.2 主动指出 1-D 限制，§6 Discussion 解释了为什么 marginal matching 无法捕捉 conditional distribution shift。这种 post-hoc 解释并不等于 ex-ante 预测。
3. **但 R1-W-M1 仍然成立**：scope 有限是事实。

综合判断：CaCLR 的负面结论不是 "obvious"，但也不是 "surprising"——它在两者之间，novelty 为 moderate。

---

### 关于评分分歧的讨论

**R1: 4/5 (Weak Accept) vs R2: 3/5 (Borderline/Findings)**

分歧来源：

1. **R1 更重视方法论执行质量（统计严谨、narrative 一致性）**。R1 给出 "0 Major issues"，强调 bootstrap CIs、paired permutation tests、Cohen's d 等统计工具的正确使用。我同意这些是论文的优点（我的 S3），但我认为方法论执行质量是**必要条件**而非**充分条件**——一篇统计上无可挑剔但结论 scope 有限的负面结论论文，仍可能不足以支撑 main conference 接收。

2. **R1 对三架构对比的不对等（W-M3）只列为 idea-level weakness**。而我认为这更严重——Gemma 4（唯一 Dense 架构）数据的缺失使得论文核心 claim 之一（"architecture-dependent"）实质上只基于两个 MoE 架构的对比。这削弱了论文的 generality。

3. **我更看重 positive contribution 的强度**。论文诚实承认了负面结论（S2），但除了 control task methodology（S1），没有正面方法论贡献。Control task finding（27% artifact rate per R1, 42% per 我的读法——数字差异可能来自不同 tier 的统计口径）虽有 field-level 意义，但需要独立验证。仅凭一个 methodological warning + 一套负面实验结果，对 main conference 来说偏弱。

4. **参考文献问题的影响权重**。R1 将 14 篇引用列为 presentation weakness，而我将其视为更根本的定位问题——参考文献不足使得论文无法在已有文献中精确定位自己的贡献。

**最终判断**：如果 R1 的 W-M1（scope 限制）和 W-M3（Gemma 不对等）得到解决（补充 activation-space MMD + Gemma 完整数据），我愿意将评分提升至 3.5/5。在当前状态下，维持 3/5 (Borderline/Findings track)。

---

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 (Median Paper, Round 1) 的交叉回应

---

## 逐条回应 R2 Weaknesses

### [AGREE，附补充] R2-W1: 参考文献不足 + References section 可能丢失

完全同意引用不足的判断。我在独立审稿中同样指出约 14 篇引用对这个范围的论文而言偏少（我的 W-N1）。R2 列出的缺失引用（Conneau et al. 2020, Pires et al. 2019, Belinkov 2022, Keleg & Magdy 2023, Guo et al. 2017）我全部认同。

**关于 References section 是否丢失**：这是一个重要的观察。我在阅读 PDF 时注意到 §7 Conclusion 之后（page 10 底部）确实有 References section——page 10 下半部分列出了参考文献（Angelopoulos and Bates 2023, Artetxe et al. 2018, Ben-David et al. 2010, Conneau et al. 2018, Hewitt and Liang 2019, Kornblith et al. 2019 等），延续到 page 11 上部。所以 **References section 存在但可能因排版紧凑而不够醒目**。R2 可能漏看了——这本身说明论文的 typographical layout 需要改善（References 应有更清晰的分隔）。

不过，即便 References section 存在，引用数量（约 15-17 篇）仍然不足。特别是：
- §3.4 使用 IRT difficulty probes 但未引用任何 psychometrics/IRT 基础文献
- §3.2 讨论 calibration (ECE) 但未引用 Guo et al. (2017) temperature scaling
- §5.3 使用 CKA 但仅引用 Kornblith et al. (2019)，缺 SVCCA 以外的 representation similarity 文献

---

### [AGREE] R2-W2: 23 张表格 + 0 张图

完全同意，这与我之前审阅 "best" 版本时指出的问题一致。对于这篇 median 论文尤其如此——核心负面结论非常适合可视化：

1. **Pareto frontier**：Table 1 的 per-language ρ 和 Table 2 的架构对比 → scatter plot（EN AUROC vs ZS AUROC, 按语言/架构着色）会直观展示 "diffuse cloud" vs "clean frontier" 的架构差异
2. **CaCLR β sweep**：Table 3 的 monotonic degradation → 折线图 + CI shaded area 比 4 行数字更有冲击力
3. **Simpson's Paradox**：Table 6 → 5-lang pilot vs 20-lang full 的 paired scatter 最能展示 artifact inflation
4. **Control task selectivity**：Table 10/11 → language × layer heatmap（按 selectivity 着色）是这篇论文最有说服力的潜在图表
5. **Linear projection saturation curve**：Table 13 → learning curve plot（pairs vs AUROC）是标准呈现方式

从 methods 角度，表格呈现要求读者自行 mental visualization，增加了审稿负担。

---

### [REBUT（部分）] R2-W3: CaCLR 失败使论文只剩两个贡献

R2 认为 CaCLR 失败意味着论文实质只剩 (1) control task 方法论 (2) 负面实验结果，对 main conference 不够。我 **部分不同意**，理由如下：

**CaCLR 的 systematic negative result 本身构成独立贡献**，前提是实验设计足够彻底——而本文确实做到了：
- β sweep 跨 3 OOM（Table 3），每个 β 值有 per-language breakdown
- Component ablation（Table 4）清楚分离了 α (SB-ECE) 和 β (MMD) 的各自效果
- 理论解释链：1-D MMD limitation → Zhao et al. (2019) conditional distribution mismatch → linear projection 作为 constructive alternative
- 两个架构上一致复现

在 NLP 社区中，well-executed negative results 有独立的出版价值（见 Rogers et al. 2020 "A Primer in BERTology" 对 negative probing results 的讨论）。关键在于 negative result 是否 **informative**——即它是否关闭了一条合理的研究路径并解释了为什么。本文在这方面做得不错。

**但我同意 R2 的实质判断**：对 main conference 而言，"thorough negative result" + "control task finding" 两个贡献的 excitement 可能不够。我在独立审稿中给出 Overall 4/5 (Weak Accept) 也是基于类似考量。对于一篇 Findings paper，这个 package 足够了。

**从 Methods 角度的补充**：CaCLR 负面结果的一个根本局限是 MMD 只在 1-D probe logits 上操作（§3.2 明确承认）。论文未测试 activation-space MMD 或 optimal transport 等替代方案。如果未来工作在高维空间做 distributional matching 成功了，这篇论文的 "closing the path" claim 就被限定为 "closing the 1-D path"。但作为当前 contribution，thoroughness 本身有价值。

---

### [AGREE] R2-W4: Pilot 区分不充分

同意。论文多次提到 "pilot studies on Qwen2.5-7B and Llama-3.1-8B" 但未说明：
- 这些 pilot 是否有独立出版物
- 如果未出版，pilot 数据是否包含在当前论文的 supplementary 中
- 具体 pilot 实验的规模和设置

从 methods 角度，这尤其影响 §5.3 的 Simpson's Paradox analysis（Table 6），因为该分析的核心逻辑是 "pilot 的 5 语言结果是 artifact"——读者需要能独立验证 pilot 的具体设置和结果。

---

### [AGREE，附重要补充] R2-W5: Difficulty decomposition 负面结论太快

完全同意。这与我独立审稿中的 W-M4 高度一致。

§5.4 仅用一段否定 decomposition，核心数据是 Table 9：Δ=-0.003 vs random Δ=-0.005, p=0.42。但论文 **未讨论** 以下关键因素：

1. **IRT R²=0.31 是根本问题**。如果 difficulty probe 只捕获 31% 的 difficulty variance，那么 "projecting out difficulty" 实际上投影的是一个噪声方向。Random-direction control 产生同量级效果恰恰与此一致——两种投影都在做 noisy dimensionality reduction。论文应讨论：R²≥0.50 的 difficulty probe 是否会改变结论。

2. **Scale 效应**。Pilot 在 7B dense 模型上可能有更 linear/concentrated 的 difficulty encoding（representation 更简单）。235B MoE 的 representation 可能更 distributed/nonlinear，使 linear IRT probe 失效。论文应对比不同 scale 的 difficulty probe R²。

3. **量化效应**。INT4 量化可能 selectively 损伤 difficulty signal（如果 difficulty 信号集中在低方差维度，4-bit 量化会 disproportionately 影响它）。

一段话的否定不足以关闭 decomposition 路径。至少需要一个 supplementary section 分析失败原因。

---

### [AGREE，附重要修正] R2-W6: "Only viable path" 与 Table 21 的张力

R2 正确指出了一个重要张力。让我从 experiments 角度详细分析。

**Table 21（Appendix, page 13，即 Table 5 在 appendix 中的完整版）：**

| Condition | Mean AUROC | Δ vs ZS | Sig. impr. count |
|-----------|-----------|---------|-----------------|
| Zero-shot | .572 | — | — |
| Mean-shift | .572 | .000 | 0/20 |
| LinProj 200 | .610 | +.038 | 11/20 |
| Few-shot 25 | .594 | +.022 | 7/20 |
| Few-shot 100 | .623 | +.051 | 13/20 |

**关键观察**：Few-shot 100 的 AUROC (.623) 和 Sig. impr. count (13/20) 都高于 Linear Proj 200 (.610, 11/20)。论文声称 linear projection 是 "the only viable transfer method"（§1 Abstract, §5.6 标题），但 **few-shot 100 按多数指标优于 linear projection**。

论文对此的隐含辩护是：few-shot 需要 target-language correctness labels，而 linear projection 只需要 parallel data（无需 labels）。这个 distinction 是合理的——但论文 **没有明确地做出这个区分**。"Only viable path" 的措辞暗示 linear projection 是唯一有效的方法，但 few-shot 100 明显更有效。

**建议修正**：论文应将 claim 改为 "the only viable **label-free** transfer method" 或 "the only viable transfer method that does not require target-language correctness labels"。当前措辞对读者有误导。

此外，从 practical 角度：如果一个 practitioner 已经有 100 条 target-language labeled data，few-shot 直接优于 linear projection。Linear projection 的优势仅在 zero-label scenario，而该 scenario 仍需 100-200 parallel pairs——获取 parallel data 的难度与获取 labeled data 的难度在低资源语言中可能相当。论文应讨论这个 practical trade-off。

---

## 总结

| R2 Issue | 我的判断 | 关键理由 |
|----------|---------|---------|
| W1 (引用不足/References 丢失) | AGREE（附修正：References section 存在但不醒目） | ~15 篇引用不足；缺 IRT/calibration/probing survey 基础文献 |
| W2 (23 表 0 图) | AGREE | 核心负面结论极适合可视化 |
| W3 (CaCLR 失败 → 只剩两个贡献) | 部分 REBUT | Systematic negative result 本身有价值（if well-executed），但同意对 main conference excitement 不足 |
| W4 (pilot 区分不充分) | AGREE | 影响 Simpson's Paradox 验证的可信度 |
| W5 (decomposition 否定太快) | AGREE（强烈） | IRT R²=0.31 是根本问题；需分析失败原因而非直接否定路径 |
| W6 ("Only viable path" 过强) | AGREE（附具体证据） | Few-shot 100 在 AUROC (.623 vs .610) 和 sig. count (13/20 vs 11/20) 上均优于 LinProj 200 |

**评分微调**：在阅读 R2 的审稿后，我认为 R2-W6 的观点有力地削弱了论文的 practical recommendation 部分。结合 R2-W5（decomposition 否定太快），论文的两个非 control-task 贡献（negative result narrative + practical recommendation）都有明显的 overclaim。我维持 **Overall 4/5 (Weak Accept)**，因为 control task contribution + statistical rigor + honest framing 仍然有价值，但更倾向于 Findings track。R2 给 3/5 (Borderline)，差异主要在于我对 negative result 的独立价值评估略高。


---

[Reviewer 2 审稿结果]:
交叉审阅回应已提交。核心分歧在于：R1 更重视方法论执行质量给出 Weak Accept，我更重视正面贡献强度和三架构对比的完整性给出 Borderline/Findings。如果补充 activation-space distributional matching 实验和 Gemma 4 完整数据，可上调至 3.5。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。六条 R2 weaknesses 中，AGREE 4 条（W1 附修正、W2、W4、W5 强烈同意），部分 REBUT 1 条（W3：negative result 本身有独立价值），AGREE 附重要证据 1 条（W6：few-shot 100 在 Table 21 中实际优于 linear projection）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-21T06:21:22.822934+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Median Paper（更正版）\n\n**论文**: Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Pareto Frontiers: Discovery, Negative Result, and Practical Recommendation\n**Tier**: Dream Median\n**目标 Venue**: Top ML venue (ACL-level)\n**审稿模式**: 圆桌会议（2 Reviewers, 1 轮 + 交叉审阅）\n**日期**: 2026-05-21\n**备注**: 本报告替换先前误投递的版本——先前版本错误地将 worst-tier R1 审稿（2/5）归属为 median paper 的交叉修订。\n\n---\n\n## Panel Summary\n\n| Reviewer | Focus | Initial | Post-discussion | Confidence |\n|----------|-------|---------|-----------------|------------|\n| R1 | Methods & Experiments | 4/5 (Weak Accept) | 4/5 (Weak Accept) | 4/5 |\n| R2 | Novelty & Related Work | 3/5 (Findings) | 3/5 (Findings) | 4/5 |\n| **Consensus** | | | **3.5/5 (Borderline Accept / Findings)** | |\n\n**Overall Assessment**: Borderline Accept — 推荐 Findings track 接收。论文在统计方法论、内部一致性和学术诚实度上显著优于同 agenda 的 best-tier 版本。控制任务发现（37-42% artifact rate）具有 field-level 价值。CaCLR negative result 的实验设计充分（β sweep 3 OOM, component ablation）。主要不足在于零可视化、引用偏少、Gemma 4 数据不对等、以及 \"only viable path\" 对 linear projection 的 overclaim。\n\n---\n\n## 1. Summary\n\n本文系统地将跨语言 correctness probe transfer 从 pilot（7-8B 模型）扩展至 3 个大规模架构（Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense）× 20 语言 × 5 迁移条件。三段叙事结构：(1) Discovery——architecture-dependent Pareto frontier（Qwen3 全负 ρ, Llama4 4/20 正, Gemma4 最强负）；(2) Negative result——CaCLR distributional matching 方法有害（β sweep 3 OOM, d=0.07, p=0.38），pilot 的 CKA-transfer 正相关被确认为 Simpson's Paradox；(3) Practical recommendation——linear projection 在特定条件下可行，~50 pairs 达 90% improvement。最有价值的方法论贡献是将 Hewitt & Liang selectivity controls 引入跨语言 probing，发现 37-42% 中低资源 probing 结果为 capacity artifacts。\n\n---\n\n## 2. Strengths\n\n- **S1 [Consensus]**: **控制任务方法论是论文锚点**——Hewitt & Liang (2019) selectivity 首次系统应用于跨语言 probing。LOW tier 42% artifact rate, HIGH tier 18%。selectivity-AUROC 相关 ρ=0.68 (p<0.001)。对整个跨语言 probing 社区有方法论警示意义。\n\n- **S2 [Consensus]**: **统计方法论 above-average**——Bonferroni correction、bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿全文。这是 probing 文献中的上游标准。\n\n- **S3 [Consensus]**: **诚实的负面结果 framing**——Abstract 开门见山 \"predominantly negative\"，每个 claim 有 qualifier（\"suggestive\", \"qualitative\"）。Claims 校准到 evidence 水平，无 overclaim。\n\n- **S4 [Consensus]**: **Simpson's Paradox falsification**——5-language pilot CKA-transfer 正相关在 20 languages 下崩溃（partial ρ=+0.14, p=0.22）。教科书级 ecological fallacy 案例。\n\n- **S5 [R1]**: **CaCLR negative result 实验充分**——β sweep 3 OOM (0.001→1.0), monotonic degradation, component ablation（每项净负），两种架构一致。不留\"未调参\"空间。\n\n- **S6 [R1]**: **CKA 自我纠正**——pooled r=0.52 做 partial correlation controlling depth 后降为 r=0.18 (p=0.11)，主动降级为 suggestive。\n\n- **S7 [R1]**: **Llama 4 Scout 的 4/20 语言 ρ>0** 是 genuinely new observation——不是 \"deeper=worse\" 的简单重复，而是发现某些语言在 MoE 架构上 deeper layers transfer better。\n\n- **S8 [Consensus]**: **内部一致性完美**——Abstract 数字与正文完全吻合，无任何自相矛盾。13/13 实验计划全部覆盖。\n\n---\n\n## 3. Weaknesses\n\n### 3.1 Moderate Issues（影响评分但不阻止接收）\n\n**W1. MMD 仅在 1-D probe logits 上测试——negative result scope 受限** [Consensus]\n\n§3.2 承认 \"design limitation: only match marginal distributions of scalar outputs\"。但 §6 的推论隐含更广的 claim。未测试 activation-space MMD 或 optimal transport。严格来说，论文仅关闭 \"1-D probe output MMD matching\" 而非 \"distributional matching for cross-lingual probe transfer\" 的全部。\n\nR2 补充：事前 MMD on probe outputs 并非 obviously 会失败——这是 Ben-David et al. domain adaptation 理论的自然实现。论文的 framing 有 caveat（§3.2, §6），逻辑自洽，但 scope 限制降低了对 community 的警示广度。\n\n**W2. Gemma 4 31B 数据严重不对等** [Consensus]\n\n仅 Table 14 的 3 行摘要（Appendix），无 per-language breakdown、β sweep、control task analysis。\"Architecture-dependent\" claim 实质仅基于 Qwen3 和 Llama4 两个 MoE 架构。Gemma4 是唯一 Dense 架构——缺其完整数据使 MoE vs Dense 对比无法完成。\n\n**W3. \"Only viable path\" overclaim——few-shot 100 实际优于 linear projection** [Consensus: R1 raised key evidence, R2 endorsed]\n\nTable 21 显示：\n- Linear Proj 200: AUROC .610, Sig. impr. 11/20\n- Few-shot 100: AUROC .623, Sig. impr. 13/20\n\nFew-shot 100 在 AUROC 和 significant improvement count 上均优于 Linear Proj 200。论文声称 linear projection 是 \"the only viable transfer method\"（§1, §5.6），但这仅在 \"zero-correctness-label\" 条件下成立。当前措辞对读者有误导——应改为 \"the only viable label-free transfer method\"。\n\n此外，Table 15 的 effect-reversal zone [0.48-0.68] 覆盖 16/20 语言。§6 的 conditional recommendation 仅适用 ~4/20 语言，practical guidance 近乎空洞。\n\n**W4. Difficulty decomposition 否定太快** [Consensus]\n\n§5.4 一段话否定。IRT R²=0.40/0.31——difficulty probe 只捕获 31-40% variance，projecting out 的是噪声方向。Random-direction control 产生同量级效果（Δ=-0.005 vs -0.003, p=0.42）与 \"poor difficulty probe\" 和 \"no decomposition\" 两种解释均一致。论文未分析：(a) 更复杂的 difficulty model 是否改变结论，(b) scale 效应，(c) 量化效应对 difficulty signal 的影响。\n\n### 3.2 Minor Issues\n\n**W5. 23 张表格、0 张图** [Consensus]\n\n核心负面结论极适合可视化：Pareto scatter plot、CaCLR β sweep 折线图、Simpson's Paradox 分组 scatter、selectivity heatmap、linear projection learning curve。表格密集增加审稿负担。\n\n**W6. 引用偏少（~15-17 篇）** [Consensus]\n\n虽比 best-tier 版本（8 篇）改善，仍低于顶会标准（30-50 篇）。缺 IRT 基础文献（Lord 1980, Baker 2001）、Belinkov (2022) probing survey、Guo et al. (2017) temperature scaling、Conneau et al. (2020)、Pires et al. (2019)。R2 报告 References section 不醒目——R1 确认 section 存在（p.10 下半部分）但排版需改善。\n\n**W7. Pilot work 区分不充分** [Consensus]\n\n未说明 pilot（Qwen2.5-7B, Llama-3.1-8B）是已发表还是未发表。影响 §5.3 Simpson's Paradox 分析的可验证性。\n\n**W8. \"First systematic study\" overclaim** [Consensus]\n\n鉴于 Civelli et al. 和 Xiao et al. 先行工作。建议改为 \"first study to apply probing control tasks to cross-lingual calibration transfer\"——更准确反映真正新贡献。\n\n**W9. CaCLR 失败减少论文正面贡献数量** [R2]\n\n论文实质贡献为 (1) 控制任务方法论 (2) systematic negative result (3) practical guidance。R1 认为 well-executed negative result 有独立出版价值；R2 认为对 main conference excitement 不足。共识：Findings track 可接受。\n\n---\n\n## 4. Reviewer Consensus [AGREE]\n\n1. **控制任务发现是最强贡献**（37-42% artifact rate，field-level 价值）\n2. **统计方法论扎实**，内部一致性完美\n3. **CaCLR negative result 实验设计充分**但 scope 受 1-D MMD 限制\n4. **零可视化**是严重表述问题\n5. **引用偏少**但比 best-tier 版本改善\n6. **\"Only viable path\" overclaim**——few-shot 100 实际优于 linear projection（Table 21 关键证据）\n7. **Difficulty decomposition 否定太快**——IRT R² 过低可能导致 false null\n8. **Findings track 接收合适**\n\n---\n\n## 5. Reviewer Divergence\n\n**5.1 评分差距的根本原因**\n\n- **R1 (4/5 Weak Accept)**: 更重视方法论执行质量。认为 0 Major issues + thorough negative result + honest framing + above-average statistics = Findings-level contribution。\"Well-executed negative result 有独立出版价值。\"\n- **R2 (3/5 Borderline)**: 更重视正面贡献强度。认为 control task finding 是唯一 field-level 贡献，negative result scope 受限（1-D MMD），Gemma 4 不对等削弱三架构 claim。\"统计执行是必要条件而非充分条件。\"\n\n**Director 判断**: 两位 Reviewer 的分歧是价值取向差异（执行质量 vs 贡献数量），而非事实分歧。双方均认可 Findings track 适合。综合评分 3.5/5——偏向 Findings track 接收，不足 main conference。\n\n**5.2 CaCLR negative result 的独立价值**\n\n- R1: 有独立价值（well-executed systematic null = informative closure）\n- R2: 有价值但 scope 有限（仅关闭 1-D MMD 这一条路）；事前非 obvious 但也非 surprising\n- 共识: Moderate novelty，对 Findings track 足够\n\n---\n\n## 6. Questions for Authors\n\n1. CaCLR 的 L_cons 使用 MMD 在 1-D probe logits 上。是否考虑过 activation-space MMD 或 optimal transport？如果 Zhao et al. 理论排除所有 marginal matching，需在 §6 更明确论证。\n2. Gemma 4 31B 的完整 per-language breakdown 和 transfer comparison 是否可用？\n3. IRT difficulty probe R²=0.31-0.40——是否尝试过 2-PL IRT 或 neural IRT？\n4. Table 21 中 few-shot 100 (AUROC .623, 13/20 sig.) 优于 linear proj 200 (.610, 11/20 sig.)——为什么论文仍称 linear proj 是 \"only viable path\"？\n5. Table 1 的完整 24 层 × 20 语言数据可否放入 supplementary？\n6. Pilot studies 是已发表还是未发表前期工作？\n7. Control task selectivity 阈值 < 0.05 的选择依据？改为 0.10/0.03 时 42% 如何变化？\n8. §5.1 Gemma4 \"moderately clear frontier\" vs Summary \"does not generalize\" 是否矛盾？\n9. 代码和 probing 数据是否有公开计划？\n\n---\n\n## 7. Missing References\n\n1. Conneau et al. (2020) — XLM-R\n2. Pires et al. (2019) — Multilingual BERT analysis\n3. Belinkov (2022) — Probing survey\n4. Lord (1980) / Baker (2001) — IRT foundational\n5. Guo et al. (2017) — Temperature scaling\n6. Keleg & Magdy (2023) — Multilingual calibration\n7. Ganin et al. (2016) / Long et al. (2015) — Domain adaptation\n8. Fedus et al. (2022) — MoE analysis\n\n---\n\n## 8. External Review\n\n**状态: pending**\n\n---\n\n## 9. Visual Layout Check\n\n**状态: not_started**（PDF 路径未配置）\n\n---\n\n## 10. Overall Assessment\n\n**评分: 3.5/5 — Borderline Accept (推荐 Findings track)**\n\n**置信度: 4/5**\n\n**核心判断**: 这是一篇学术品质显著优于同 agenda best-tier 版本的论文。控制任务发现（37-42% artifact rate）是真正的 field-level 贡献。CaCLR negative result 的实验设计充分（β sweep 3 OOM, component ablation, 两架构一致）。统计方法论在 probing 文献中属于上游。内部一致性完美。\n\n不足以升至 main conference 的原因：\n1. 负面结果 scope 受限（仅 1-D MMD），无法断言 \"distributional matching 全部失败\"\n2. Gemma 4 数据不对等使三架构 claim 不完整\n3. \"Only viable path\" overclaim——few-shot 100 实际上更好\n4. 零可视化和引用偏少影响 presentation\n\n**修改建议优先级**:\n1. [重要] 添加 2-3 个核心 figure（selectivity heatmap, Simpson's Paradox scatter, Pareto comparison）\n2. [重要] 补充 Gemma 4 完整数据\n3. [重要] 修正 \"only viable path\" → \"only viable label-free method\"，坦诚讨论 few-shot 100 的优势\n4. [建议] 扩展引用至 30+ 篇\n5. [建议] 补充 activation-space MMD 实验（即使失败也扩大 scope）\n6. [建议] Decomposition §5.4 补充失败原因分析\n\n**与 Best-tier 对比**:\n\n| 维度 | Best (2.5/5 Weak Reject) | Median (3.5/5 Borderline Accept) |\n|------|--------------------------|----------------------------------|\n| 内部一致性 | 差（72%/81%/25% 矛盾） | 完美 |\n| 统计严谨性 | 差（无 CI/检验） | 好（Bonferroni/CIs/Cohen's d） |\n| 学术诚信 | 差（疑似 fabricated refs） | 好（诚实负面结果） |\n| 引用 | 8 篇（严重不足） | ~15 篇（偏少但有结构） |\n| 控制任务 | 无 | 42% artifact（field-level） |\n| 核心缺陷 | 可信度危机 | Scope 限制 + 数据不对等 |\n| 可修复性 | 低 | 高 |\n| 推荐 | Reject → Revise | Findings track 接收 |\n\n---\n\n## 11. Detailed Comments\n\n### §1-2\n- \"First systematic study\" → \"first study applying probing control tasks to cross-lingual calibration\"\n- Related Work 覆盖 5-6 子方向，结构合理，但缺核心引用\n\n### §3\n- §3.2 MMD scope caveat 好，但 §6 推论过广\n- \"Two regularization terms\" 应为 three（公式有 3 项额外 loss）\n\n### §5\n- §5.1 Llama4 的 4/20 正 ρ 是 genuinely new finding\n- §5.3 Simpson's Paradox 分析方法论值得肯定\n- §5.4 Decomposition 否定太快——IRT R²=0.31 是 probe quality 问题\n- §5.5 Control task 是论文锚点\n- §5.6 Linear projection recommendation 需坦诚讨论 reversal zone + few-shot 对比\n\n### Appendix\n- Table 14 Gemma4 需大幅扩充\n- References section 存在但不醒目（R2 漏看），排版需改善",
  "project": "xling_calib_direction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline accept",
  "review_chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Median Paper（更正版）\n\n**论文**: Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Pareto Frontiers: Discovery, Negative Result, and Practical Recommendation\n**Tier**: Dream Median\n**目标 Venue**: Top ML venue (ACL-level)\n**审稿模式**: 圆桌会议（2 Reviewers, 1 轮 + 交叉审阅）\n**日期**: 2026-05-21\n**备注**: 本报告替换先前误投递的版本——先前版本错误地将 worst-tier R1 审稿（2/5）归属为 median paper 的交叉修订。\n\n---\n\n## Panel Summary\n\n| Reviewer | Focus | Initial | Post-discussion | Confidence |\n|----------|-------|---------|-----------------|------------|\n| R1 | Methods & Experiments | 4/5 (Weak Accept) | 4/5 (Weak Accept) | 4/5 |\n| R2 | Novelty & Related Work | 3/5 (Findings) | 3/5 (Findings) | 4/5 |\n| **Consensus** | | | **3.5/5 (Borderline Accept / Findings)** | |\n\n**Overall Assessment**: Borderline Accept — 推荐 Findings track 接收。论文在统计方法论、内部一致性和学术诚实度上显著优于同 agenda 的 best-tier 版本。控制任务发现（37-42% artifact rate）具有 field-level 价值。CaCLR negative result 的实验设计充分（β sweep 3 OOM, component ablation）。主要不足在于零可视化、引用偏少、Gemma 4 数据不对等、以及 \"only viable path\" 对 linear projection 的 overclaim。\n\n---\n\n## 1. Summary\n\n本文系统地将跨语言 correctness probe transfer 从 pilot（7-8B 模型）扩展至 3 个大规模架构（Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense）× 20 语言 × 5 迁移条件。三段叙事结构：(1) Discovery——architecture-dependent Pareto frontier（Qwen3 全负 ρ, Llama4 4/20 正, Gemma4 最强负）；(2) Negative result——CaCLR distributional matching 方法有害（β sweep 3 OOM, d=0.07, p=0.38），pilot 的 CKA-transfer 正相关被确认为 Simpson's Paradox；(3) Practical recommendation——linear projection 在特定条件下可行，~50 pairs 达 90% improvement。最有价值的方法论贡献是将 Hewitt & Liang selectivity controls 引入跨语言 probing，发现 37-42% 中低资源 probing 结果为 capacity artifacts。\n\n---\n\n## 2. Strengths\n\n- **S1 [Consensus]**: **控制任务方法论是论文锚点**——Hewitt & Liang (2019) selectivity 首次系统应用于跨语言 probing。LOW tier 42% artifact rate, HIGH tier 18%。selectivity-AUROC 相关 ρ=0.68 (p<0.001)。对整个跨语言 probing 社区有方法论警示意义。\n\n- **S2 [Consensus]**: **统计方法论 above-average**——Bonferroni correction、bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿全文。这是 probing 文献中的上游标准。\n\n- **S3 [Consensus]**: **诚实的负面结果 framing**——Abstract 开门见山 \"predominantly negative\"，每个 claim 有 qualifier（\"suggestive\", \"qualitative\"）。Claims 校准到 evidence 水平，无 overclaim。\n\n- **S4 [Consensus]**: **Simpson's Paradox falsification**——5-language pilot CKA-transfer 正相关在 20 languages 下崩溃（partial ρ=+0.14, p=0.22）。教科书级 ecological fallacy 案例。\n\n- **S5 [R1]**: **CaCLR negative result 实验充分**——β sweep 3 OOM (0.001→1.0), monotonic degradation, component ablation（每项净负），两种架构一致。不留\"未调参\"空间。\n\n- **S6 [R1]**: **CKA 自我纠正**——pooled r=0.52 做 partial correlation controlling depth 后降为 r=0.18 (p=0.11)，主动降级为 suggestive。\n\n- **S7 [R1]**: **Llama 4 Scout 的 4/20 语言 ρ>0** 是 genuinely new observation——不是 \"deeper=worse\" 的简单重复，而是发现某些语言在 MoE 架构上 deeper layers transfer better。\n\n- **S8 [Consensus]**: **内部一致性完美**——Abstract 数字与正文完全吻合，无任何自相矛盾。13/13 实验计划全部覆盖。\n\n---\n\n## 3. Weaknesses\n\n### 3.1 Moderate Issues（影响评分但不阻止接收）\n\n**W1. MMD 仅在 1-D probe logits 上测试——negative result scope 受限** [Consensus]\n\n§3.2 承认 \"design limitation: only match marginal distributions of scalar outputs\"。但 §6 的推论隐含更广的 claim。未测试 activation-space MMD 或 optimal transport。严格来说，论文仅关闭 \"1-D probe output MMD matching\" 而非 \"distributional matching for cross-lingual probe transfer\" 的全部。\n\nR2 补充：事前 MMD on probe outputs 并非 obviously 会失败——这是 Ben-David et al. domain adaptation 理论的自然实现。论文的 framing 有 caveat（§3.2, §6），逻辑自洽，但 scope 限制降低了对 community 的警示广度。\n\n**W2. Gemma 4 31B 数据严重不对等** [Consensus]\n\n仅 Table 14 的 3 行摘要（Appendix），无 per-language breakdown、β sweep、control task analysis。\"Architecture-dependent\" claim 实质仅基于 Qwen3 和 Llama4 两个 MoE 架构。Gemma4 是唯一 Dense 架构——缺其完整数据使 MoE vs Dense 对比无法完成。\n\n**W3. \"Only viable path\" overclaim——few-shot 100 实际优于 linear projection** [Consensus: R1 raised key evidence, R2 endorsed]\n\nTable 21 显示：\n- Linear Proj 200: AUROC .610, Sig. impr. 11/20\n- Few-shot 100: AUROC .623, Sig. impr. 13/20\n\nFew-shot 100 在 AUROC 和 significant improvement count 上均优于 Linear Proj 200。论文声称 linear projection 是 \"the only viable transfer method\"（§1, §5.6），但这仅在 \"zero-correctness-label\" 条件下成立。当前措辞对读者有误导——应改为 \"the only viable label-free transfer method\"。\n\n此外，Table 15 的 effect-reversal zone [0.48-0.68] 覆盖 16/20 语言。§6 的 conditional recommendation 仅适用 ~4/20 语言，practical guidance 近乎空洞。\n\n**W4. Difficulty decomposition 否定太快** [Consensus]\n\n§5.4 一段话否定。IRT R²=0.40/0.31——difficulty probe 只捕获 31-40% variance，projecting out 的是噪声方向。Random-direction control 产生同量级效果（Δ=-0.005 vs -0.003, p=0.42）与 \"poor difficulty probe\" 和 \"no decomposition\" 两种解释均一致。论文未分析：(a) 更复杂的 difficulty model 是否改变结论，(b) scale 效应，(c) 量化效应对 difficulty signal 的影响。\n\n### 3.2 Minor Issues\n\n**W5. 23 张表格、0 张图** [Consensus]\n\n核心负面结论极适合可视化：Pareto scatter plot、CaCLR β sweep 折线图、Simpson's Paradox 分组 scatter、selectivity heatmap、linear projection learning curve。表格密集增加审稿负担。\n\n**W6. 引用偏少（~15-17 篇）** [Consensus]\n\n虽比 best-tier 版本（8 篇）改善，仍低于顶会标准（30-50 篇）。缺 IRT 基础文献（Lord 1980, Baker 2001）、Belinkov (2022) probing survey、Guo et al. (2017) temperature scaling、Conneau et al. (2020)、Pires et al. (2019)。R2 报告 References section 不醒目——R1 确认 section 存在（p.10 下半部分）但排版需改善。\n\n**W7. Pilot work 区分不充分** [Consensus]\n\n未说明 pilot（Qwen2.5-7B, Llama-3.1-8B）是已发表还是未发表。影响 §5.3 Simpson's Paradox 分析的可验证性。\n\n**W8. \"First systematic study\" overclaim** [Consensus]\n\n鉴于 Civelli et al. 和 Xiao et al. 先行工作。建议改为 \"first study to apply probing control tasks to cross-lingual calibration transfer\"——更准确反映真正新贡献。\n\n**W9. CaCLR 失败减少论文正面贡献数量** [R2]\n\n论文实质贡献为 (1) 控制任务方法论 (2) systematic negative result (3) practical guidance。R1 认为 well-executed negative result 有独立出版价值；R2 认为对 main conference excitement 不足。共识：Findings track 可接受。\n\n---\n\n## 4. Reviewer Consensus [AGREE]\n\n1. **控制任务发现是最强贡献**（37-42% artifact rate，field-level 价值）\n2. **统计方法论扎实**，内部一致性完美\n3. **CaCLR negative result 实验设计充分**但 scope 受 1-D MMD 限制\n4. **零可视化**是严重表述问题\n5. **引用偏少**但比 best-tier 版本改善\n6. **\"Only viable path\" overclaim**——few-shot 100 实际优于 linear projection（Table 21 关键证据）\n7. **Difficulty decomposition 否定太快**——IRT R² 过低可能导致 false null\n8. **Findings track 接收合适**\n\n---\n\n## 5. Reviewer Divergence\n\n**5.1 评分差距的根本原因**\n\n- **R1 (4/5 Weak Accept)**: 更重视方法论执行质量。认为 0 Major issues + thorough negative result + honest framing + above-average statistics = Findings-level contribution。\"Well-executed negative result 有独立出版价值。\"\n- **R2 (3/5 Borderline)**: 更重视正面贡献强度。认为 control task finding 是唯一 field-level 贡献，negative result scope 受限（1-D MMD），Gemma 4 不对等削弱三架构 claim。\"统计执行是必要条件而非充分条件。\"\n\n**Director 判断**: 两位 Reviewer 的分歧是价值取向差异（执行质量 vs 贡献数量），而非事实分歧。双方均认可 Findings track 适合。综合评分 3.5/5——偏向 Findings track 接收，不足 main conference。\n\n**5.2 CaCLR negative result 的独立价值**\n\n- R1: 有独立价值（well-executed systematic null = informative closure）\n- R2: 有价值但 scope 有限（仅关闭 1-D MMD 这一条路）；事前非 obvious 但也非 surprising\n- 共识: Moderate novelty，对 Findings track 足够\n\n---\n\n## 6. Questions for Authors\n\n1. CaCLR 的 L_cons 使用 MMD 在 1-D probe logits 上。是否考虑过 activation-space MMD 或 optimal transport？如果 Zhao et al. 理论排除所有 marginal matching，需在 §6 更明确论证。\n2. Gemma 4 31B 的完整 per-language breakdown 和 transfer comparison 是否可用？\n3. IRT difficulty probe R²=0.31-0.40——是否尝试过 2-PL IRT 或 neural IRT？\n4. Table 21 中 few-shot 100 (AUROC .623, 13/20 sig.) 优于 linear proj 200 (.610, 11/20 sig.)——为什么论文仍称 linear proj 是 \"only viable path\"？\n5. Table 1 的完整 24 层 × 20 语言数据可否放入 supplementary？\n6. Pilot studies 是已发表还是未发表前期工作？\n7. Control task selectivity 阈值 < 0.05 的选择依据？改为 0.10/0.03 时 42% 如何变化？\n8. §5.1 Gemma4 \"moderately clear frontier\" vs Summary \"does not generalize\" 是否矛盾？\n9. 代码和 probing 数据是否有公开计划？\n\n---\n\n## 7. Missing References\n\n1. Conneau et al. (2020) — XLM-R\n2. Pires et al. (2019) — Multilingual BERT analysis\n3. Belinkov (2022) — Probing survey\n4. Lord (1980) / Baker (2001) — IRT foundational\n5. Guo et al. (2017) — Temperature scaling\n6. Keleg & Magdy (2023) — Multilingual calibration\n7. Ganin et al. (2016) / Long et al. (2015) — Domain adaptation\n8. Fedus et al. (2022) — MoE analysis\n\n---\n\n## 8. External Review\n\n**状态: pending**\n\n---\n\n## 9. Visual Layout Check\n\n**状态: not_started**（PDF 路径未配置）\n\n---\n\n## 10. Overall Assessment\n\n**评分: 3.5/5 — Borderline Accept (推荐 Findings track)**\n\n**置信度: 4/5**\n\n**核心判断**: 这是一篇学术品质显著优于同 agenda best-tier 版本的论文。控制任务发现（37-42% artifact rate）是真正的 field-level 贡献。CaCLR negative result 的实验设计充分（β sweep 3 OOM, component ablation, 两架构一致）。统计方法论在 probing 文献中属于上游。内部一致性完美。\n\n不足以升至 main conference 的原因：\n1. 负面结果 scope 受限（仅 1-D MMD），无法断言 \"distributional matching 全部失败\"\n2. Gemma 4 数据不对等使三架构 claim 不完整\n3. \"Only viable path\" overclaim——few-shot 100 实际上更好\n4. 零可视化和引用偏少影响 presentation\n\n**修改建议优先级**:\n1. [重要] 添加 2-3 个核心 figure（selectivity heatmap, Simpson's Paradox scatter, Pareto comparison）\n2. [重要] 补充 Gemma 4 完整数据\n3. [重要] 修正 \"only viable path\" → \"only viable label-free method\"，坦诚讨论 few-shot 100 的优势\n4. [建议] 扩展引用至 30+ 篇\n5. [建议] 补充 activation-space MMD 实验（即使失败也扩大 scope）\n6. [建议] Decomposition §5.4 补充失败原因分析\n\n**与 Best-tier 对比**:\n\n| 维度 | Best (2.5/5 Weak Reject) | Median (3.5/5 Borderline Accept) |\n|------|--------------------------|----------------------------------|\n| 内部一致性 | 差（72%/81%/25% 矛盾） | 完美 |\n| 统计严谨性 | 差（无 CI/检验） | 好（Bonferroni/CIs/Cohen's d） |\n| 学术诚信 | 差（疑似 fabricated refs） | 好（诚实负面结果） |\n| 引用 | 8 篇（严重不足） | ~15 篇（偏少但有结构） |\n| 控制任务 | 无 | 42% artifact（field-level） |\n| 核心缺陷 | 可信度危机 | Scope 限制 + 数据不对等 |\n| 可修复性 | 低 | 高 |\n| 推荐 | Reject → Revise | Findings track 接收 |\n\n---\n\n## 11. Detailed Comments\n\n### §1-2\n- \"First systematic study\" → \"first study applying probing control tasks to cross-lingual calibration\"\n- Related Work 覆盖 5-6 子方向，结构合理，但缺核心引用\n\n### §3\n- §3.2 MMD scope caveat 好，但 §6 推论过广\n- \"Two regularization terms\" 应为 three（公式有 3 项额外 loss）\n\n### §5\n- §5.1 Llama4 的 4/20 正 ρ 是 genuinely new finding\n- §5.3 Simpson's Paradox 分析方法论值得肯定\n- §5.4 Decomposition 否定太快——IRT R²=0.31 是 probe quality 问题\n- §5.5 Control task 是论文锚点\n- §5.6 Linear projection recommendation 需坦诚讨论 reversal zone + few-shot 对比\n\n### Appendix\n- Table 14 Gemma4 需大幅扩充\n- References section 存在但不醒目（R2 漏看），排版需改善",
    "project": "xling_calib_direction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline accept",
    "review_chat_id": "oc_03a4b60e63b9658b3528f3d9a729f2e8",
    "force_resubmit": "True"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-21T06:21:27.238107+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_74ae31a7dc5ae9d419ba9a89bccc89c0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4415
}
```

</details>

---

### Assistant

_source line 110 · 2026-05-21T06:21:37.217352+00:00_

更正版 Median 报告已投递。评分从先前误报的 2.5 (Weak Reject) 修正为 **3.5 (Borderline Accept / Findings track)**。

**修正要点**：先前错误地将 R1 对 worst-tier 论文的独立审稿（2/5, 2 Major confound: 低 EN AUROC + 量化偏差）归属为 R1 对 median paper 的交叉修订。实际交叉回应中 R1 维持 4/5 (Weak Accept)，R2 维持 3/5 (Findings)。

两篇 Dream 论文的审稿报告现已全部完成：

| Paper | Tier | Score | 推荐 |
|-------|------|-------|------|
| Best | Pareto Frontier (positive) | 2.5/5 Weak Reject | 可信度危机（数字矛盾+疑似虚构引用），需大幅修改 |
| Median | Limits (negative) | 3.5/5 Borderline Accept | 推荐 Findings track，控制任务发现有 field-level 价值 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 13

2 recorded events

### User

_source line 111 · 2026-05-21T14:05:27.010895+00:00_

[Reviewer 1 审稿意见]:
# Reviewer 1 — 综合审稿报告（Worst Paper Variant: Full ACL ARR Review for EACL）

**论文**: "The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications"

---

## 1. Paper Summary

本文对跨语言正确性探针迁移（correctness probe transfer）进行了大规模实证研究，涵盖 3 种 LLM 架构（Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B）、20 种语言和 5 种迁移条件。结果以负面为主：(1) 深度-可迁移性 Pareto 前沿不泛化；(2) CaCLR 校准感知正则化有害；(3) IRT 难度分解与随机不可区分；(4) CKA 几何分析的 pilot 发现系 Simpson's Paradox 伪影。唯一可行的迁移路径是线性投影（Procrustes alignment），但需要 100-200 对标注数据且效果不一致。论文将自身定位为"负面结果+方法论贡献"，其中方法论贡献是首次将 Hewitt & Liang 控制任务选择性应用于跨语言探针文献，发现 42% LOW / 37% MID 的伪影率。

---

## 2. 总体评分

**Overall**: 2/5 (Reject)

**一句话总结**: 规模可观的负面结果研究，但英语源探针质量低（AUROC 0.715-0.742）和量化伪影这两个系统性混淆因素严重削弱了核心结论的可信度，加上排版缺陷（多处 "??" 断引、零图表），尚未达到发表标准。

---

## 3. 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 2.5/5 | 两个未解决的系统混淆因素（低 EN AUROC、深层量化偏差）使核心负面声明不可靠。多处缺少置信区间。 |
| **Excitement / Novelty** | 2/5 | 负面结果本身有价值，但由于混淆因素，信息量降低——读者无法确定这些限制是基本的还是实验设计导致的。控制任务方法论贡献是真实的但未被充分开发。 |
| **Clarity** | 2.5/5 | 文本叙述清晰，但零图表（23 个表格、0 个 figure）严重阻碍可读性。Pareto 前沿分析论文没有散点图令人费解。多处 "??" 断引。 |
| **Reproducibility** | 3.5/5 | 论文声称提供完整实现细节和逐语言结果（Section 6 末尾），Appendix A-E 有丰富的逐语言数据。但代码/数据未附。 |
| **Overall** | 2/5 | 低于接收门槛。 |

---

## 4. Must-Fix 问题（影响接收决定）

**N1** [critical] 英语源探针质量低构成系统性混淆因素
- 具体位置：Section 4 (Experimental Setup), Table 1, Table 11
- 问题：全文所有迁移实验的起点是英语校准探针，但其最佳 AUROC 仅为 0.715（Qwen3）到 0.742（Gemma 4 31B）。Table 1 报告 Qwen3-235B 最佳 EN AUROC 为 0.738（layer 72, zero-shot pass rate 0.695）。这是一个中等偏低的分类器质量。论文所有"迁移失败"的负面结论都建立在这个薄弱基础之上——如果源信号本身不够强，迁移失败可能只是信号不足的下游表现，而非跨语言迁移本身的基本限制。
- 为什么影响接收：这是最核心的 confound。论文的 title claim ("The Limits of Cross-Lingual Calibration Probe Transfer") 暗示这些是基本限制，但 EN AUROC < 0.75 意味着源探针仅比随机好 ~22-25 个百分点。在 EN AUROC > 0.85 的场景下，结果是否不同？论文完全没有讨论这一替代解释。
- 建议修改方向：(1) 明确讨论低 EN AUROC 作为限制条件；(2) 增加消融实验，例如筛选 EN AUROC > 0.80 的层/模型子集重新评估迁移；(3) 将标题和 claims 限定为"在中等质量源探针条件下的限制"。

**N2** [critical] 量化伪影与深层迁移负面结论混淆
- 具体位置：Section 5.8, Table 18, Table 22
- 问题：Table 18（Quantization validation, 5% data subset）显示 INT4 量化的 AUROC 下降随深度单调增加——Llama4 从 20% depth 的 Δ=−0.003 增长到 95% depth 的 Δ=−0.018；Qwen3 从 −0.005 到 −0.022。Table 22（Full quantization validation, 5 layer depth percentiles）证实了同样的模式。但论文的核心负面发现之一就是"深层探针迁移效果差"（Section 5.1, Pareto 前沿分析）——这恰好与量化在深层的退化重叠。论文在 Section 5.8 承认"Quantization does not change the direction of any negative result but adds ∼7pp uncertainty to absolute AUROC values at deep layers"，但 7pp 的不确定性在 AUROC 仅为 0.7x 的情况下是巨大的（占有效信号的 ~30%）。
- 为什么影响接收：论文的 Pareto 前沿非泛化结论（Section 5.1）可能被量化偏差而非真实的跨语言限制所驱动。7pp 不确定性足以翻转许多边缘结果。
- 建议修改方向：(1) 在 FP16 下重新运行深层探针实验（至少对关键模型的关键层）；(2) 或在报告 Pareto 分析时明确扣除量化偏差的估计影响；(3) 将量化限制提升为主体讨论而非附录级别。

**N3** [critical] LaTeX 编译错误导致多处引用断裂
- 具体位置：Page 1 (Abstract), 多处
- 问题：论文第一页即出现多个 "??" 标记，表明 LaTeX \cite 命令未能正确解析。在 Abstract 中出现引用断裂对任何 venue 都是不可接受的。这不仅是排版问题——审稿人无法核实论文声称的先行工作。
- 为什么影响接收：违反基本投稿要求。审稿人无法验证引用声明的真实性。
- 建议修改方向：修复 .bib 文件并重新编译。

---

## 5. Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 零图表——23 个表格、0 个 Figure
- 具体位置：全文
- 问题：一篇以 Pareto 前沿分析为核心的论文没有任何散点图、热力图或可视化。Table 1-4 中的逐语言 Spearman 相关数据完全可以用 scatter plot 展示（depth vs. cross-shot AUROC, 按语言着色），这将比纯数字表格直观得多。23 个密集表格使论文几乎不可读。
- 建议：至少添加 (1) Pareto 前沿散点图；(2) CaCLR α-sweep 折线图；(3) 控制任务选择性热力图（Table 10-11 数据）。

**W2** [warning] CaCLR 设计空间探索不足就做出"有害"结论
- 具体位置：Section 3.2, Section 5.2, Table 3
- 问题：CaCLR 仅测试了一种核心配置：Gaussian RBF kernel + median-heuristic bandwidth + α ∈ {0.01, 0.05, 0.1, 1.0}。Table 3 显示即使最小 α=0.01 也导致 ΔAUROC = −0.003（Qwen3, 50% depth），且所有 α 值均为负。论文据此声称 CaCLR "uniformly harmful"。但 (1) 仅测试 4 个 α 值和 1 个 kernel 选择；(2) 未尝试其他 MMD 变体或更低的 α（如 0.001）；(3) 未给出 CaCLR 不适用于 1-D logistic regression 的理论分析。
- 建议：要么扩展搜索空间，要么提供更强的理论论证解释为什么 MMD 在此设定下必然有害。

**W3** [warning] 控制任务发现（最强贡献）被埋没
- 具体位置：Section 5.5, Table 10-11
- 问题：42% LOW 伪影率（即 42% 的低资源语言层的探针性能可以完全被容量伪影解释）是本文最具影响力和方法论贡献的发现。但它被放在第 5 个子节（Section 5.5），在 Pareto、CaCLR、decomposition、CKA 之后。如果将此作为论文的 leading contribution 并重新组织叙事，会大大提升论文的 excitement 评分。
- 建议：重新组织论文结构，以控制任务方法论发现为核心叙事。

**W4** [warning] Related Work 过于简略
- 具体位置：Section 2 (约半页)
- 问题：Section 2 仅约半页，分为 4 个小节（Probe-based calibration, Cross-lingual probing, Probing methodology, Domain adaptation theory, Cross-lingual alignment），每节仅 2-4 句话。对于一篇声称是"large-scale"研究的论文，related work 的覆盖面不够。特别是：(1) 近期跨语言表示学习的重要工作（如 Conneau et al. 的多语言 probing 系列）讨论不足；(2) 负面结果论文的先例讨论缺失（该社区有哪些成功的负面结果论文？）；(3) 校准相关文献（Guo et al. 2017 温度缩放、Desai & Durrett 2020 等经典工作）未出现。
- 建议：扩展 Related Work 至至少 1 页，增加上述缺失的讨论。

**W5** [warning] Simpson's Paradox 解释不充分
- 具体位置：Section 5.3, Table 6 (p.6)
- 问题：Section 5.3 报告 CKA 分析中发现 Simpson's Paradox——pilot 阶段的 5 语言样本显示深度与 CKA-transfer 正相关，但扩展到 20 语言后变为负相关或不显著。论文将此归因于"between-language heterogeneity in CKA patterns overwhelms the within-layer signal"和"small-sample artifacts that use small-sample artifacts"，但没有给出具体机制解释——为什么恰好是这 5 种语言产生了正相关？它们有什么特殊性？Table 6 显示了 5-lang pilot 的 Simpson's partial ρ = +0.14 (p=0.22)，但这个 p 值本身就不显著，所以 pilot 阶段就不应该报告为"positive finding"。
- 建议：(1) 说明 pilot 的 5 种语言是哪些及其选择标准；(2) 讨论这是否反映了 pilot 设计缺陷而非 Simpson's Paradox。

**W6** [warning] 线性投影"唯一可行路径"但实用性讨论不足
- 具体位置：Section 5.6, Table 13, Table 21
- 问题：论文将线性投影（Procrustes alignment）称为"the only viable transfer method"（Abstract 及 Section 5.6），但 Table 13 显示需要 100-200 对平行数据，且 Table 21（Qwen3-235B, 5 transfer conditions）显示 LinProj 200 的 Δ vs ZS 仅为 +0.038（mean AUROC 从 0.572 到 0.610），仅 11/20 语言达到显著改善。Few-shot 100 达到 +0.051 且 13/20 显著。这引发两个问题：(1) 线性投影是否真的优于简单 few-shot？(2) 需要 100-200 对标注数据时，直接训练目标语言探针可能更经济。论文未讨论这一成本效益分析。
- 建议：增加 few-shot vs. LinProj 的成本效益对比讨论。

---

## 6. 小问题（不影响接收）

- Table 7（Same-layer cross-language CKA-transfer）中 Layer (%) 列的对齐不一致，部分行的 p 值格式不统一。
- Section 5.9 "Orthogonality Across Languages" 内容较薄（不到半页），作为独立小节不太必要，可以合并到 Section 5.5 控制任务讨论中。
- Table 23（Cross-lingual correctness-confidence cosine similarity）中"mag. mismatch"和"elevated"的注释缺乏明确定义。
- Appendix B/C/D/E 的标题有但内容在本 PDF 中似乎只是表格罗列，缺少文字解释。
- 论文声称"We release complete overlay code and implementation specifications to enable independent verification"（Section 6 末尾），但未提供链接或匿名仓库。

---

## 7. Questions for the Authors

1. **EN AUROC 混淆**：如果仅保留 EN AUROC > 0.80 的层/模型组合（如 Gemma 的 0.742 已接近），Pareto 前沿和迁移结论是否改变？是否考虑过使用更强的探针架构（如 2-layer MLP）来排除源探针质量的混淆？

2. **CaCLR 搜索空间**：α = 0.001 或更小的值是否测试过？论文仅报告 α ∈ {0.01, 0.05, 0.1, 1.0}，是否有理论理由认为更小的 α 也必然有害？

3. **量化与深层**：是否可以在至少一个模型上提供 FP16 和 INT4 在相同深层的 head-to-head 迁移比较？当前 Table 18 仅报告单语言 AUROC 差异，不包含迁移性能。

4. **控制任务的 42% 伪影率**：这个数字在不同模型/架构之间是否稳定？MoE（Qwen3）和 Dense（Gemma）架构的伪影率是否有系统差异？

5. **Figure 缺失**：是否有技术原因导致无法生成图表？23 个表格的论文即使对审稿人也非常难以消化。

6. **"负面结果 + 方法论"定位**：作者是否考虑过将论文重新定位为以控制任务方法论为核心（正面贡献），辅以负面迁移结果作为案例研究？

---

## 8. Missing References / Related Work

- **断裂引用**：Page 1 出现多处 "??"，无法核实声称的先行工作。这是最严重的引用问题。
- **缺失的关键引用**：
  - Guo et al. (2017) "On Calibration of Modern Neural Networks" — 校准领域的奠基工作
  - Desai & Durrett (2020) "Calibration of Pre-trained Transformers" — 直接相关的校准+LLM 工作
  - Conneau et al. (2020) "Emerging Cross-lingual Structure in Pretrained Language Models" — 跨语言表示结构的经典工作
  - Hewitt & Liang (2019) "Designing and Interpreting Probes with Control Tasks" — 论文方法论的核心依赖，需要确认是否在断裂引用中
  - 近期的 Probing 综述文献

---

## 9. Experiment Coverage Assessment

对照设计文档中的 13 个实验计划：

| # | 实验 | 是否涵盖 | 位置 |
|---|------|----------|------|
| 1 | Depth-transferability Pareto (Qwen3-235B) | ✅ | Table 1, Section 5.1 |
| 2 | Depth-transferability Pareto (Llama 4 Scout) | ✅ | Table 1, Section 5.1 |
| 3 | Depth-transferability Pareto (Gemma 4 31B) | ✅ | Table 1/Table 20, Section 5.1 |
| 4 | CaCLR sweep | ✅ | Table 3, Section 5.2 |
| 5 | Difficulty decomposition ablation | ✅ | Table 9, Section 5.4 |
| 6 | CKA geometric analysis (Simpson's Paradox) | ✅ | Table 6-7, Section 5.3 |
| 7 | Control tasks / selectivity | ✅ | Table 10-11, Section 5.5 |
| 8 | Linear projection (5 conditions) | ✅ | Table 13/21, Section 5.6 |
| 9 | Cross-benchmark generalization | ✅ | Table 16, Section 5.7 |
| 10 | Probe complexity comparison | ✅ | Table 17, Section 5.8 |
| 11 | Quantization validation | ✅ | Table 18/22, Section 5.8 |
| 12 | Extended language coverage (52 lang) | ✅ | Table 19, Appendix A |
| 13 | Cross-lingual orthogonality | ✅ | Table 23, Section 5.9 |

**覆盖率：13/13 (100%)**。所有实验计划均已执行。但多数实验的报告存在上述质量问题（低 EN AUROC 混淆、缺乏误差线/置信区间等）。

---

## 10. "负面结果 + 方法论"定位评估（EACL 适配性）

**部分令人信服，但不足以支撑接收。** 具体分析：

- **负面结果维度**：论文的实验规模确实大（3 架构 × 20 语言 × 5 条件），如果负面结论成立，对社区有重要价值。但 N1（低 EN AUROC）和 N2（量化混淆）两个未解决的 confound 意味着读者无法确信这些是真正的"limits"还是实验设计的局限。一篇好的负面结果论文需要排除替代解释——本文未做到。

- **方法论维度**：将 Hewitt & Liang 控制任务引入跨语言探针文献是真实的贡献（Section 5.5），42% 伪影率发现意义重大。但这一贡献在当前论文结构中是从属地位（第 5 个子节），且仅占约 1 页篇幅。如果以此为核心重写论文，excitement 评分会显著提升。

- **EACL 适配性**：EACL 欢迎负面结果和资源型论文，但仍要求 soundness。当前版本的 soundness 不足以通过 EACL 的审稿标准。

---

## 11. 主要优势

1. **实验规模**：3 种架构（含 MoE 和 Dense）、20 种语言、5 种迁移条件——这是目前跨语言探针迁移文献中规模最大的研究。
2. **诚实的负面结果报告**：论文没有试图美化结果，Section 5.1-5.4 的每个负面发现都有明确的数字支撑。
3. **控制任务方法论**：首次将 selectivity-based control tasks 应用于跨语言探针，42% LOW 伪影率是有价值的发现。
4. **丰富的 Appendix**：逐语言、逐层的完整结果（Table 10-23），支持独立验证。
5. **52 语言扩展**：Table 19 将核心发现从 20 语言扩展到 52 语言，增强了泛化性声明。
6. **Limitations 段落**（Section 6 末尾）坦诚地列出了 4 个限制，包括 MoE 架构的不确定性和 quantization 的影响。

---

## 12. Confidence

**Confidence: 4/5** — 我对跨语言表示学习和探针方法论领域较为熟悉，已完整阅读论文全部 14 页及所有 23 个表格。对核心混淆因素的判断有较高把握。

---

## 13. 最终判断

**Reject (2/5)**。论文方向有价值、规模可观，但两个关键混淆因素（低 EN AUROC、深层量化偏差）未被解决，使得"基本限制"的核心声明不可信。排版问题（"??" 断引、零图表）加剧了可读性困难。建议：(1) 以控制任务方法论为核心重写；(2) 解决 EN AUROC 混淆（至少讨论，最好做消融）；(3) 修复引用并添加关键图表；(4) 扩充 Related Work。在这些修改后，论文有潜力达到 EACL 的接收标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 112 · 2026-05-21T14:05:47.446530+00:00_

Worst-tier 论文 R1 审稿已收到。

**R1 (Methods & Experiments)**: 2/5 (Reject) — 3 个 Must-Fix：(1) EN AUROC 仅 0.715-0.742 构成系统性 confound；(2) 深层量化偏差与迁移负面结论混淆；(3) LaTeX 编译错误导致多处 "??" 断引。6 个 Should-Fix 包括零图表、CaCLR 搜索空间不足、控制任务发现被埋没等。13/13 实验计划全覆盖。

这与之前误归属给 median paper 的审稿内容一致——现在确认是 worst-tier 的 R1 审稿。等待 R2 的 worst-tier 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---

## Round 14

4 recorded events

### User

_source line 113 · 2026-05-21T14:05:50.085308+00:00_

[Reviewer 1 审稿结果]:
Worst paper 综合审稿报告已提交。评分 Overall 2/5 (Reject)，核心问题：(1) 低 EN AUROC (0.715-0.742) 系统混淆因素、(2) 深层量化偏差与 Pareto 负面结论重叠、(3) 多处 "??" 断引+零图表。实验覆盖率 13/13，但方法论贡献（控制任务 42% 伪影率）被埋没在论文结构中。建议以控制任务为核心重写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-21T14:05:59.537825+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '[Best] 审稿完成（2.5/5 Weak Reject）', 'status': 'completed', 'activeForm': 'Best paper 已完成'}, {'content': '[Median] 审稿完成（3.5/5 Borderline Accept）', 'status': 'completed', 'activeForm': 'Median paper 已完成'}, {'content': '[Worst] 收集 R1 初审', 'status': 'completed', 'activeForm': 'Worst R1 初审已收到'}, {'content': '[Worst] 等待 R2 初审', 'status': 'in_progress', 'activeForm': '等待 Worst R2 审稿'}, {'content': '[Worst] 交叉分享 + 收敛判断', 'status': 'pending', 'activeForm': 'Worst 交叉审阅'}, {'content': '[Worst] 合成报告 + 投递', 'status': 'pending', 'activeForm': 'Worst 报告投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '[Best] 审稿完成（2.5/5 Weak Reject）', 'status': 'completed', 'activeForm': 'Best paper 已完成'}, {'content': '[Median] 审稿完成（3.5/5 Borderline Accept）', 'status': 'completed', 'activeForm': 'Median paper 已完成'}, {'content': '[Worst] 收集 R1 初审', 'status': 'completed', 'activeForm': 'Worst R1 初审已收到'}, {'content': '[Worst] 等待 R2 初审', 'status': 'in_progress', 'activeForm': '等待 Worst R2 审稿'}, {'content': '[Worst] 交叉分享 + 收敛判断', 'status': 'pending', 'activeForm': 'Worst 交叉审阅'}, {'content': '[Worst] 合成报告 + 投递', 'status': 'pending', 'activeForm': 'Worst 报告投递'}]"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-21T14:05:59.588403+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 116 · 2026-05-21T14:06:10.468362+00:00_

Worst paper R1 审稿已收到：**2/5 (Reject)**。

关键发现：
- **3 个 Must-Fix**: (1) EN AUROC 仅 0.715-0.742 构成系统性 confound，(2) 深层 INT4 量化偏差（最大 -0.022, 7pp 不确定性）与 Pareto 负面结论重叠，(3) LaTeX "??" 断引——Abstract 即出现未解析引用
- **6 个 Should-Fix**: 零图表、CaCLR 搜索空间不足（仅 4 个 α 值）、控制任务贡献被埋没、Related Work 过于简略、Simpson's Paradox 解释不充分、linear projection "only viable path" overclaim
- 实验覆盖率 13/13，但报告质量受 confound 和排版问题影响

值得注意：R1 对 worst paper 的 EN AUROC confound 判断与其先前对 median paper 的独立审稿高度一致——这两个 confound（低 EN AUROC + 量化偏差）是跨 tier 的系统性问题。worst paper 额外暴露了 "??" 断引这个 best/median 版本没有的排版缺陷。

等待 R2 审稿提交后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director"
}
```

</details>

---
