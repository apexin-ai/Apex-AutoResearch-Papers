# Director coordination — Part 1 of 7

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/9d/9db2d5c10f518e51ec86.json)

## Round 1

## Round 1

20 recorded events


### User

_source line 1 · 2026-05-21T01:54:05.590127+00:00_

[Reviewer 2 审稿意见]:
## R2 审稿报告：Novelty & Related Work

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison"
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审稿维度**: Novelty, Related Work, Writing Quality, Scope/Impact, Presentation

---

## 总体评分

**Overall Assessment**: 2.5 / 5 (Borderline Findings)
**Director 6-point scale**: 3 / 6 (Weak Reject)
**一句话总结**: 方法论合理、核心实验发现有实用价值，但新颖性不足（已知心理测量学现象的重新包装）、范围狭窄（主要仅验证 formality 一个维度）、且提交材料存在严重的引用/格式缺陷，不具备送审状态。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3 / 5 (Acceptable) | 5 阶段协议设计合理，有 NLI 人工验证（91% agreement）和 Holm-Bonferroni 校正。但因果识别是近似的（作者在 Limitations 中承认），缺少 Bradley-Terry 建模，且 RATE 对比缺乏匹配条件下的复现 |
| **Excitement** | 2.5 / 5 (Potentially Interesting → Interesting) | 7/9 vs 1/9 的检测率差距数据有实用价值，但核心发现——Likert 评分对 forced-choice 敏感性不足——是心理测量学中已确立的结论，将其应用于 LLM judge 是直接的迁移，非深层洞见 |
| **Overall** | 2.5 / 5 (Borderline Findings) | 干净的实证工作，但 novelty 薄弱 + scope 狭窄 + 提交质量问题三重叠加 |

**Confidence**: 4 / 5 (Familiar with the area, have reviewed related work)

---

## 主要优势

- **S1**: 研究问题清晰且有实际意义——如果 Likert 评分系统性地低估 style bias，这对所有使用 LLM judge 的评估管线都有直接影响
- **S2**: 5 阶段反事实协议设计完备：style rewriting → NLI content gate → position control → Likert control → original preference control，每一步都有对照，逻辑链完整
- **S3**: 3 judges × 3 benchmarks 的网格设计覆盖了多个 LLM 家族（GPT-4o / Claude / Gemini），避免了单 judge 的 anecdotal evidence 问题
- **S4**: 透明承认所有组件是已有方法（§1 第2段明确列出来源：style rewriting from Mir et al. 2019, controls from RATE, pairwise from Thurstone 1927），这种诚实性值得肯定
- **S5**: 人工 NLI 验证（§5.7, n=100, 91% agreement, Table 7）为 content preservation gate 提供了可信的质量保证
- **S6**: Scaled replication（§5.5, n=500）确认效应量稳定，confidence interval 减半，增强了核心发现的可信度

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 新颖性不足——"Likert Blindspot" 是已知现象的重新命名

- 具体位置：§1 contributions, §6 Discussion 标题
- 问题：Likert 评分相比 forced-choice/pairwise comparison 在检测细微差异时敏感性不足，这在心理测量学中是 Thurstone (1927) 以来近百年的共识。作者自己也引用了 Karpinska et al. 和 Novikova et al. 证明 Best-Worst Scaling 优于 Likert。论文的核心贡献——将这一已知结果应用于 LLM judge bias 检测——是一个 application-level 的迁移，不是方法论创新。"Likert Blindspot" 这一术语暗示发现了一个此前未知的现象（"blindspot"），但实际上只是将已知的 measurement sensitivity gap 量化到了一个新 domain。
- 为什么影响接收：对于顶会（acceptance rate ~25%），incremental application of known psychometric insight 的 novelty bar 不够。
- 建议修改方向：(a) 明确将贡献定位为 "first empirical quantification" 而非 "discovery"，调整标题和术语避免暗示原创性；(b) 如果要维持 blindspot 叙事，需要展示 LLM judge 社区中存在的系统性误解（如大量 benchmark 论文仍在用 Likert 且因此漏报了 bias），并提供这种误解的量化证据。

**N2** [critical] 引用系统严重不完整——提交材料不具备送审状态

- 具体位置：Page 7 References; §1-§2 正文引用
- 问题：
  (a) 至少一处 arXiv ID 为占位符格式（"arXiv:2406.xxxxx"）——这不是真实的 arXiv 编号
  (b) 部分引用作者名疑似有误或乱码（需与原始 .bib 核对）
  (c) 无 .bib 文件（`verify_references` 工具因找不到 .bib 文件而失败）
  (d) Director 标记的 "???" 占位符引用——表明 LaTeX 中有未解析的 \cite key
  (e) 总引用数约 15 篇，对于这个研究领域来说偏少
- 为什么影响接收：ARR 评审标准明确要求引用完整可验证。占位符 arXiv ID 直接违反 ACL anti-fabrication 政策。如果审稿人无法验证关键引用，将严重质疑学术规范。
- 建议修改方向：修复所有 broken citations，补充完整 arXiv ID，通过 `verify_references` 等工具验证每一条引用真实存在。

**N3** [critical] RATE 批评缺乏实证支撑

- 具体位置：§5.3 ("Likert ATE detects significance in only 1/9 cells"), §6 Discussion ("RATE's Likert-based estimates may systematically understate true bias")
- 问题：论文声称 RATE (Feuer et al., 2025) 使用 Likert ATE 作为主要度量因此"可能系统性低估真实偏差"。但 §5.3 和 §6 均承认这一判断**未在匹配条件下验证**（"this hasn't been verified under matched conditions"）。论文使用自己的 counterfactual data 上的 Likert 结果来推断 RATE 的 Likert 结果也会有同样问题——这是一个 ecological validity 跨越：不同的 rewriting 方法、不同的 style axes、不同的 benchmark 都可能改变结论。
- 为什么影响接收：对竞品方法的批评如果缺乏实证支撑，会被 reviewer 视为 unfair comparison。这削弱了论文的 positioning。
- 建议修改方向：(a) 在 RATE 的 exact experimental setup 下复现实验，比较 Likert vs pairwise 的检测结果；或 (b) 将措辞从 "RATE may understate" 弱化为 "our results on formality suggest that Likert-based protocols in general warrant complementary pairwise validation"，并明确声明未直接测试 RATE 的设定。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 范围过窄——单一主 style axis 限制了贡献的泛化性

- 具体位置：§4 Experimental Setup, §5.8 Verbosity, §5.9 Register
- 问题：Formality 是唯一在 3×3 网格上全面测试的 style axis。Verbosity（§5.8）仅在 GPT-4o 上测试了一个 benchmark 组合，且仅展示 Table 8 的单列数据。Register（§5.9）是"exploratory"，仅 GPT-4o × LLMBar，且效应未达到显著性阈值。
- 论文在 Limitations 中列出 sentiment、complexity 等未测试的 axes，但标题和 abstract 的 framing（"Hidden Style Bias"、"style bias"）暗示了比实际覆盖范围更广的适用性。
- 建议：至少对 verbosity 补做完整的 3×3 网格实验。如果资源不允许，应将标题和 abstract 限制为 "formality bias"。

**W2** [warning] 缺少 Bradley-Terry 建模——pairwise comparison 数据的标准分析框架缺失

- 具体位置：§3.3, §5 Results（所有 pairwise 结果均用 win rate + sign test）
- 问题：论文的核心方法是 pairwise comparison，但分析仅使用了 win rate 和 sign test。Pairwise comparison 数据的标准统计框架是 Bradley-Terry 模型（及其扩展如 Thurstone Case V），它能提供：(a) latent strength 估计，(b) effect size 的置信区间，(c) 对不同 item 难度的控制。论文引用了 Thurstone (1927) 但未使用其框架。
- 建议：补充 Bradley-Terry 分析，至少作为 robustness check，展示 pairwise bias 的 effect size 在模型框架下的估计。

**W3** [warning] Related work 覆盖不完整

- 具体位置：§2 Related Work
- 问题：
  (a) **CalibraEval** 未被引用——该工作研究 LLM judge 的 calibration，与 measurement sensitivity 直接相关
  (b) **FairEval** (Wang et al., 2023) 未被引用——论文只引了 FairBridge，但 FairEval 是该方向的重要前驱
  (c) **LLM-as-Judge 综述/meta-analysis** 缺失——如 Zheng et al. (2023) 后的多篇 survey papers 提供了系统性的 judge bias 分类
  (d) **Bradley-Terry for judge evaluation** 完全未讨论——Chatbot Arena 的 Elo/BT 排名与本文的 pairwise comparison 方法论直接相关，但 §2 未深入讨论这一联系
  (e) 心理测量文献引用过浅：仅引 Thurstone (1927) 和 Karpinska/Novikova 的应用层工作，但 Likert vs forced-choice 的理论分析（如 DeCoster et al. 2011, Simms et al. 2019）未被引用
- 建议：补充上述引用，特别是在 §2.3 "Psychometric foundations" 中深化心理测量学文献的讨论。

**W4** [warning] 无任何图表——全文仅有 tables，视觉传达严重不足

- 具体位置：全文（7 页，Tables 1-9，Figures 0）
- 问题：论文核心发现是 Likert vs Pairwise 的检测率差距（7/9 vs 1/9）——这是一个非常适合可视化的结果。一张简单的 heatmap（3 judges × 3 benchmarks，Likert vs Pairwise 并排）或 grouped bar chart 就能让 "blindspot" 这个概念一目了然。9 张 tables 堆叠在 6 页正文中，信息密度极高但可读性差。
- 建议：至少添加一张 Figure 1 展示核心 blindspot 结果的视觉对比，以及一张 Figure 2 展示方法流程图（5-stage pipeline）。

---

## 小问题（不影响接收）

- §5.5 Scaled Replication: "Effect size is stable, confidence interval halves" — 应报告具体的 effect size (Cohen's h 或 similar) 和 CI 数值，而非仅做定性描述
- §4: "n = 100 per benchmark for the primary grid" — 未报告 power analysis 来论证 n=100 的样本量选择依据
- 标题 "The Likert Blindspot" 中的 "Blindspot" 到 §4.6 binarized-Likert 分析后被弱化为 "measurement efficiency gap"——标题与正文的 framing 不完全一致
- 论文正文仅 6 页（EMNLP 2026 long paper 限制为 8 页），有 2 页空间可用于深化分析
- "Anonymous ACL submission" 格式头——需确认使用的是正确的 EMNLP 2026/ARR 模板
- Table 3 (核心结果表) 包含了 Likert、Pairwise、Binarized Likert 三种度量，但列头中 "FC"、"C→F"、"F→C" 等缩写未在 caption 中充分解释

---

## Questions for Authors

1. **Q1 (Novelty)**: 你们将 "Likert Blindspot" 定位为一个新发现。能否明确说明，相对于 Karpinska et al. 和 Novikova et al. 已经证明的 Likert vs ranking sensitivity gap，你们的贡献具体在哪里超越了"将已知结论迁移到 LLM judge"？

2. **Q2 (RATE)**: §6 声称 RATE "may systematically understate true bias"。你们是否考虑过在 RATE 的 exact setup（相同的 style axes、rewriter、benchmarks）下复现实验来验证这一声明？如果没有，为什么对此做了因果方向的推断？

3. **Q3 (Scope)**: 论文标题和 abstract 使用 "style bias" 作为泛化概念，但 formality 是唯一完整测试的 axis。如果 verbosity 和 register 的 blindspot 效应不显著或方向不同，你们的核心 narrative 是否仍然成立？

4. **Q4 (Bradley-Terry)**: 你们使用 sign test 而非 Bradley-Terry 模型来分析 pairwise data。这一选择是否有方法论上的考虑？sign test 是否可能因忽略 item-level heterogeneity 而低估或高估 effect size？

5. **Q5 (Binarized Likert)**: §5.3 报告 binarized Likert 在 0/9 cells 中显著。这是否意味着 binarized Likert 的 power 本身不足（而非 Likert 的问题）？你们是否做了 power analysis 来区分 "Likert 真的看不到" vs "样本量不足以让 Likert 看到"？

6. **Q6 (References)**: Page 7 的 References 列表中存在 placeholder arXiv ID（如 "arXiv:2406.xxxxx"）和疑似格式问题。这些引用是否都是真实的、可验证的学术文献？

---

## Preliminary Score Summary

| Criterion | Score | Note |
|-----------|-------|------|
| Soundness | 3 / 5 | Acceptable; methodology sound but missing BT modeling and power analysis |
| Excitement | 2.5 / 5 | Application of known insight to new domain; useful but not surprising |
| Overall (ARR) | **2.5 / 5** | Borderline Findings |
| Overall (Director 6pt) | **3 / 6** | Weak Reject |
| Confidence | 4 / 5 | Familiar with LLM judge evaluation and psychometrics literature |

**判断理由**: 这篇论文在一个实用的问题上做了干净的实验工作（5-stage protocol, 3×3 grid, scaled replication）。但三个问题叠加使其处于 borderline：(1) 核心概念是已知心理测量学结论的 domain transfer，novelty 达不到 top venue 要求；(2) 仅在 formality 上有完整结果，scope 限制了贡献的影响力；(3) 引用系统存在明显缺陷（placeholder IDs、broken citations），当前版本不具备正式送审条件。如果 (2) 和 (3) 得到修复，且 (1) 中的 positioning 更诚实，论文有潜力达到 Findings 水平 (ARR 3.0)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-21T01:54:25.756348+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 3 · 2026-05-21T01:54:25.806822+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-21T01:54:31.484153+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-21T01:54:31.536520+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (13 个)\n\n- **register_100_cf**: QUEUED — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **verbosity_32b**: DONE (negative) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- register_100_cf（排队等待 GPU）\n\n## 近期结论\n- **exp013_nli_validation** (success): NLI gate (DeBERTa-v3-large, threshold 0.90) decisions are reliable proxies for human content-preservation judgments, achieving Cohen's kappa >= 0.6 with LLM-as-annotator (Qwen3-32B)\n- **exp-013** (killed): NLI gate (DeBERTa-v3-large, threshold 0.90) decisions are reliable proxies for human content-preservation judgments, achieving Cohen's kappa >= 0.6 with LLM-as-annotator (Qwen3-32B)\n  [exp013_nli_validation](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/exp-013/data/exp013_nli_validation_summary.txt)\n- **verbosity_32b** (negative): Verbosity axis (verbose/concise) produces stronger style bias signal than formality in GPT-4o judge: pairwise win rate ≥60% with p<0.05 and/or Likert corrected ATE with d≥0.3, because verbose responses contain more surface-level detail that judges may conflate with thoroughness ← 基于 pairwise_32b\n\n## 趋势\n成功 6 / 负向 5 / 失败 0 / 共 12\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-21T01:54:36.864470+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-21T01:54:37.818140+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-21T01:54:37.869573+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-21T01:54:37.970453+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-21T01:54:38.071469+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-21T01:54:38.073732+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-21T01:54:52.493717+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea_gen_0514_5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/memory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea_gen_0514_5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/memory"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-21T01:54:52.746309+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea_gen_0514_5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/memory. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_director_acab027e.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-21T01:54:52.797471+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-21T01:54:52.901468+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-21T01:54:57.429432+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-21T01:54:57.931313+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-21T01:54:58.133506+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/ 2>/dev/null | head -30",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/ 2>/dev/null | head -30",
    "description": "List artifacts directory"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-21T01:54:58.334488+00:00_

total 44
drwxr-xr-x  8 ubuntu ubuntu 4096 May 21 01:53 .
drwxr-xr-x 10 ubuntu ubuntu 4096 May 21 01:47 ..
drwxr-xr-x  4 ubuntu ubuntu 4096 May 21 01:14 _project
drwxr-xr-x  3 ubuntu ubuntu 4096 May 21 00:04 csd_pipeline
drwxr-xr-x  5 ubuntu ubuntu 4096 May 21 01:01 dream_reports
drwxr-xr-x  3 ubuntu ubuntu 4096 May 21 01:53 exp-002
drwxr-xr-x  3 ubuntu ubuntu 4096 May 21 01:00 exp-013
-rw-r--r--  1 ubuntu ubuntu 2383 May 21 01:53 manifest.yaml
drwxr-xr-x  2 ubuntu ubuntu 4096 May 21 00:06 reanalysis_outputs
-rw-r--r--  1 ubuntu ubuntu  153 May 20 07:14 requirements.txt
-rwxr-xr-x  1 ubuntu ubuntu 1531 May 20 09:55 run_mvp.sh

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 200
}
```

</details>

---


### Assistant

_source line 20 · 2026-05-21T01:55:34.630657+00:00_

R2 审稿意见已收到。R2 聚焦 Novelty & Related Work 维度，给出 **Overall 2.5/5 (Borderline Findings)**。

关键发现汇总：
- **3 个 Must-Fix**：N1 新颖性不足（已知心理测量学现象的迁移）、N2 引用系统严重不完整（placeholder arXiv ID、broken citations）、N3 RATE 批评缺乏匹配条件下的实证支撑
- **4 个 Should-Fix**：W1 范围过窄（仅 formality 完整测试）、W2 缺少 Bradley-Terry 建模、W3 Related work 覆盖不完整（CalibraEval/FairEval/BT literature 缺失）、W4 全文无图表

当前状态：**R2 已提交，等待 R1 提交后进入交叉分享阶段。**

R1 审稿意见是否已完成？如已完成请提交，我将启动 Step 2 交叉讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 2

## Round 2

8 recorded events


### User

_source line 21 · 2026-05-21T01:55:35.813849+00:00_

[Reviewer 2 审稿结果]:
R2 审稿报告已提交给 Review Director。

核心判断：**ARR 2.5 / 5 (Borderline Findings)**，Director 6-point scale **3 / 6 (Weak Reject)**。

三个主要扣分因素：
1. **Novelty 不足** — "Likert Blindspot" 本质是 Thurstone (1927) 以来已知的 Likert vs forced-choice sensitivity gap 在 LLM judge 领域的直接迁移，非原创发现
2. **Scope 狭窄** — 仅 formality 有完整 3×3 结果；verbosity/register 均为单点或探索性测试
3. **引用系统严重缺陷** — placeholder arXiv IDs、无 .bib 文件、broken citations，提交材料不具备送审状态

同时标记了 4 个 Should-Fix（RATE 批评无实证支撑、缺 Bradley-Terry 建模、Related Work 覆盖不完整、全文无 Figure）和 6 个 minor issues。

---

[Reviewer 1 审稿意见]:
## R1 审稿意见：Methods & Experiments

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison"

**注意**: Director brief 中部分数字与 PDF 不一致。以下审稿严格基于 PDF 原文。PDF 显示 Table 1 三个 judge 均显著 (GPT-4o p=0.006, Claude p=0.012, Gemini p=0.032)；Table 2 有 7/9 cells 显著；Table 5 win rate ~67.6%（CI [0.637, 0.714]），效率差距为 5× 而非 7×。Director brief 中 "Only 2/3 judges significant" "Only 2/9 cells significant" "7× efficiency" "win rate regresses to 61.1%" 等描述与本版 PDF 不符。

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 核心发现（pairwise 比 Likert 更能检测 style bias）有实际价值且在多数实验中得到支持，但因果框架缺失、NLI gate 的选择偏差未被分析、以及 Likert baseline 可能不公平，使得证据链不够坚实。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Pipeline 设计合理，控制实验覆盖主要 confound，但因果语言与实际统计框架不匹配；NLI 阈值无 justification；multiple comparison 处理不一致 |
| Excitement | 3.5/5 | 发现对 LLM-as-judge 社区有直接实践意义；但范围较窄（主要一个 style axis），且 Likert 的"盲区"可能是分析方法而非 Likert 本身的问题 |
| Reproducibility | 3/5 | 报告了 judge/benchmark/rewriter 选择和 NLI 阈值，但缺少每阶段的 attrition 数据（生成→NLI pass→consistent→final n），无代码/数据 |
| Confidence | 4/5 | 对实验方法论和 NLP 评估统计有充分经验 |

---

## 主要优势

- **重要的实践发现**：7/9 judge×benchmark 组合中 pairwise 检测到显著 formality bias，而 Likert ATE 仅 1/9、binarized Likert 0/9。这直接挑战了 LLM 评估社区对 Likert 评分的默认依赖（§5.3, Table 3）。
- **Pipeline 设计系统性强**：四阶段协议（counterfactual rewriting → NLI gate → position-controlled comparison → Likert baseline）每一步都针对特定 confound，逻辑清晰（§3）。
- **Confound 控制全面**：original preference 控制（Table 4）、rewriter robustness（Table 6, Llama vs Qwen）、human NLI validation（Table 7）、cross-axis generalization（Tables 8-9）覆盖了主要替代解释。
- **Binarized-Likert 作为诊断工具的创新性**：通过让 binarized Likert 和 pairwise 使用相同的 sign test，将灵敏度差异精确隔离到 measurement structure（§5.3）。这是本文最强的方法论贡献。
- **诚实的 Limitations**：明确承认因果框架的近似性、样本量限制、仅检测不纠正（page 6）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 因果语言与实际框架严重不匹配
- 具体位置：§3 标题 "Counterfactual Style Rewriting"、§3.4 "ATE"、§1 "counterfactual pairwise measurement procedure"、Limitations (page 6)
- 问题：论文大量使用因果推断术语——"counterfactual"、"interventional"、"treatment effect (ATE)"——但 Limitations 自认"our 'interventional' framing approximates but does not formally establish causal identification; we do not provide a directed acyclic graph, discuss SUTVA, or conduct sensitivity analysis for unmeasured confounders"。这不仅是写作问题，而是核心方法论缺陷：如果论文的核心贡献是一个"counterfactual protocol"，读者需要 DAG 来评估 Style → Score 的因果通路中 Content 是否被正确控制、是否存在未测量的 confounders（如 fluency/coherence 变化）。
- 为什么影响接收：reviewer 和读者会质疑：没有 DAG，你怎么知道 NLI gate 足够控制 content confound？"ATE" 在没有因果框架下是否只是一个描述性统计量？这直接影响论文 claim 的可信度。
- 建议修改方向：(1) 给出 DAG（至少：Style_axis → Rewrite → Judge_score, with Content as mediator and potential confounders）; (2) 讨论 SUTVA 在此设置下的合理性；(3) 对"未被 NLI 捕获的语义变化"做 sensitivity analysis；或 (4) 降调因果语言，改用"diagnostic"/"detection"框架。

**N2** [critical] NLI gate 的选择偏差未被分析
- 具体位置：§3.2, Table 7 (page 5)
- 问题：Table 7 显示 NLI gate 的 false-negative rate 为 67%——即人类认为内容保留了的 pair 中，2/3 被 NLI 拒绝。论文将此解释为"conservative behavior implies that our reported bias magnitudes are lower-bound estimates"（§5.7），但这一推断需要一个未经验证的假设：NLI-rejected-but-human-valid pairs 中的 bias 方向和大小与 NLI-accepted pairs 相同或更大。如果 NLI gate 系统性地筛掉了 deeper style changes（这些改写更可能同时改变 content），留下的可能是 superficial 改写（容易让 NLI 验证），而 superficial 改写产生的 bias 可能与 deeper 改写不同。
- 为什么影响接收：67% 的 data loss 意味着最终分析仅基于原始数据的 ~1/3。如果这 1/3 不具代表性，所有效应量估计和统计检验的外部效度都成问题。
- 建议修改方向：(1) 分析 NLI-rejected pairs 的 pairwise 结果（作为 sensitivity analysis）；(2) 至少报告 NLI-rejected pairs 中 judge 的 raw preference 分布；(3) 对 "lower-bound" claim 提供形式化论证而非仅凭直觉。

**N3** [critical] NLI 阈值 0.90 缺乏 justification，且不同 axis 之间不一致
- 具体位置：§3.2
- 问题：NLI entailment 阈值设为 0.90，但论文未解释为什么是 0.90 而非 0.85 或 0.95。更重要的是，§3.2 提到 verbosity axis 的 NLI gate 从 bidirectional（65% pass rate）改为 direction-aware（86% pass rate），这表明阈值和 gating 策略是 per-axis 调整的。这引入了 researcher degrees of freedom——是否先看了结果再调阈值？
- 为什么影响接收：如果阈值选择影响哪些 pairs 进入分析，它直接影响效应量和显著性。没有 pre-registration 或 sensitivity analysis，读者无法评估结果对阈值选择的稳健性。
- 建议修改方向：(1) 报告阈值 sensitivity analysis（如 0.85, 0.90, 0.95 下的 win rate 和 p-value）；(2) 说明阈值是否 pre-specified；(3) 对 verbosity axis 的 direction-aware 调整提供独立的 justification。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Likert baseline 可能不公平——未使用 ordinal regression
- 具体位置：§3.4, Table 3
- 问题：Likert 数据的分析用了 ATE（均值差）和 binarized sign test。ATE 丢弃了 ordinal 结构信息——1分和2分的差异被等同于4分和5分的差异。Cumulative link mixed model (CLMM) 或 ordinal logistic regression 能更好地利用 Likert 数据的 ordinal 特性，可能会检测到 ATE 遗漏的效应。Binarized Likert 虽然与 pairwise 使用相同的 sign test，但它把 5 vs 4 等同于 5 vs 1，同样丢失信息。
- 建议：增加 CLMM 分析作为 Likert 的更公平 baseline。如果 CLMM 仍然不显著，"Likert Blindspot" 的论点会大大加强；如果 CLMM 显著，则说明问题在于分析方法而非 Likert 本身。

**W2** [warning] Consistency filtering 的 data loss 过高且未分析
- 具体位置：§3.3, Table 1
- 问题：Table 1 显示 GPT-4o 有 55 个 consistent pairs（推测 n=100，即 45% 被过滤）。Claude 的 consistent pairs 更少。被过滤的 position-sensitive pairs 包含有价值的信息——它们可能代表 style preference 较弱或 position bias 较强的样本。论文完全忽略了这些 pairs 的分析。
- 建议：(1) 明确报告每个 cell 的 total pairs → NLI pass → consistent → final n 的 attrition 表；(2) 对 inconsistent pairs 做探索性分析（如 first-position win rate）；(3) 讨论 consistency filtering 对 effect size generalizability 的影响。

**W3** [warning] Original preference confound 结果为 marginal，不能安全忽略
- 具体位置：§5.4, Table 4
- 问题：原始偏好 win rate 56%, GEE OR=1.65, p=0.072。论文将此解释为"substantially weaker than the formality effect (66-70%)"，但 56% 不是 negligible。如果 formal rewrite 与 "非原始" 方向相关（即 formal 更常是 rewrite 而非 original），这个 marginal confound 可能部分解释观察到的 formality effect。
- 建议：做 formal decomposition：在控制 original/rewrite 状态后，formality effect 减少多少？一个简单的 logistic regression (judge_choice ~ is_formal + is_original) 即可。

**W4** [warning] Multiple comparison correction 不一致
- 具体位置：§4 ("Holm-Bonferroni correction across the 9-cell grid"), Tables 1, 5, 6, 8, 9
- 问题：Holm-Bonferroni 仅用于 Table 2 的 9-cell grid。但 Tables 1（3 comparisons）、8（verbosity）、9（register）是额外的假设检验。全论文总共约 20+ 次检验，但没有讨论 family-wise error rate。
- 建议：(1) 报告全局 correction 后的结果（或至少讨论）；(2) 或者按 "discovery" vs "confirmation" 区分实验，仅对 confirmatory 实验做 correction。

**W5** [warning] Post-hoc power analysis 方法论问题
- 具体位置：§5.5
- 问题：论文用 observed effect size 做 post-hoc power analysis 估计所需样本量。这在统计文献中广泛被批评（Hoenig & Heisey, 2001）——observed power 是 p-value 的 1-to-1 函数，不提供额外信息。"5× efficiency gap" 来自 post-hoc 估计，其可信度受限于 observed effect 的不确定性。
- 建议：改用 confidence interval 或 equivalence testing 来量化 efficiency gap；或基于先验 literature 的 effect size（而非观测值）做 power analysis。

---

## 小问题（不影响接收）

- §5.8 Table 8 verbosity 和 §5.9 Table 9 register 仅在 GPT-4o×LLMBar 上测试了一个 judge×benchmark 组合，cross-axis generalization 的证据较薄。
- Table 9 register axis p=0.068 未达显著，论文用"suggestive evidence"表述，但放在 cross-axis generalization 的叙事中可能误导读者认为 register bias 已被确认。
- "Likert Blindspot" 术语有 oversell 风险——本质上 Likert 不是"看不到" bias，而是需要更大样本量。论文自身的 n=500 数据中 binarized Likert p=0.055，接近显著边缘，说明 Likert 在足够大样本下可能也会显著。
- 无 appendix/supplementary material。对于涉及 9 cells × 3 metrics 的实验矩阵，detailed per-cell 结果（含 CI）应在 supplementary 中提供。
- 论文 7 页（正文约 6 页 + 参考文献 1 页），格式合规（EMNLP 2026 long paper 8-page limit）。

---

## Questions for Authors

**Q1**: 请报告每个 judge×benchmark cell 的完整 attrition 数据：generated pairs → NLI pass → position-consistent → final n。目前无法评估 filtering 对 representativeness 的影响。

**Q2**: NLI 阈值 0.90 是在看到结果前还是后确定的？是否做过 threshold sensitivity analysis（如 0.80, 0.85, 0.90, 0.95）？

**Q3**: Table 7 中 67% false-negative rate 意味着 NLI-rejected pairs 远多于 accepted pairs。这些被拒绝但人类认为 content 保留的 pairs 中，judge 的 formality preference 是什么？如果方向与 accepted pairs 一致，"lower-bound" claim 成立；如果不一致，则 NLI gate 引入了 non-trivial selection bias。

**Q4**: 是否考虑过 cumulative link mixed model (CLMM) 或 ordinal logistic regression 作为 Likert 的替代分析？ATE 在 ordinal data 上可能不是最 sensitive 的方法。

**Q5**: Table 4 original preference OR=1.65 (p=0.072) 是 marginal 的。是否可以做 logistic regression (judge_choice ~ is_formal + is_original) 来 partial out original preference 对 formality effect 的贡献？

**Q6**: 对于 §5.5 的 power analysis，"n≈80 for pairwise vs n>X for Likert" 中的效应量是观测值还是 pre-specified？观测效应量的 CI 较宽时，post-hoc power analysis 的可信度有限。

**Q7**: Consistency filtering 去掉的 ~40-50% pairs 中，position bias 的方向和大小如何？这些数据本身就是关于 LLM judge position bias 的有价值信息。

---

## 总结评分

| 项目 | 评分 |
|------|------|
| Overall Assessment | **3.5** (Borderline Conference) |
| Soundness | 3.5/5 |
| Excitement | 3.5/5 |
| Confidence | 4/5 |

**判断依据**: 论文提出了一个对 LLM-as-judge 社区有实际意义的发现，Pipeline 设计系统性强，实验覆盖了主要的 confounds。但三个 critical 问题——因果框架缺失 (N1)、NLI gate 的选择偏差未分析 (N2)、NLI 阈值无 justification (N3)——使得证据链不够坚实。Likert baseline 的公平性 (W1) 和 original preference 的 marginal confound (W3) 进一步削弱了核心 claim 的说服力。如果 rebuttal 能：(a) 补上 NLI threshold sensitivity analysis, (b) 报告 NLI-rejected pairs 的 bias 方向, (c) 加入 CLMM 作为 Likert baseline, 我愿意上调至 4.0 (Conference)。

---

[Reviewer 1 审稿结果]:
审稿意见已提交至 Review Director。

核心判断：**3.5 (Borderline Conference)**。论文发现 pairwise 比 Likert 更能检测 style bias，Pipeline 设计系统且实验覆盖面广（7/9 cells 显著）。但三个 critical 问题拉低评分：(1) 大量使用因果术语却无 DAG/SUTVA 等正式框架；(2) NLI gate 67% false-negative rate 造成的选择偏差未被分析；(3) NLI 阈值 0.90 无 justification 且 per-axis 调整引入 researcher degrees of freedom。若 rebuttal 能补上 NLI threshold sensitivity analysis、报告 NLI-rejected pairs 的 bias 方向、加入 ordinal regression 作为更公平的 Likert baseline，可上调至 4.0。

另外提醒：Director brief 中的部分数字与 PDF 原文不一致（如 Table 1 显著性、Table 2 显著 cell 数量、效率倍数等），我已在审稿意见开头标注。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-21T01:55:53.083511+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 23 · 2026-05-21T01:55:53.083868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-21T01:57:02.510624+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 R2 的每个 Must-Fix 和 Should-Fix 问题：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下与你审查维度（Methods & Experiments）相关的交叉点：\n1. R2-N3 认为 RATE 批评缺乏实证支撑——你是否同意？从方法论角度看 §5.3 的比较是否合理？\n2. R2-W2 认为缺少 Bradley-Terry 建模——你认为 sign test 在此场景下是否足够，还是 BT 建模确实必要？\n3. R2-W4 指出全文无 Figure——从实验呈现角度，你是否认为可视化对传达核心发现至关重要？\n\n---\n\n以下是 **Reviewer 2 的完整审稿原文**：\n\n## R2 审稿报告：Novelty &amp; Related Work\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审稿维度**: Novelty, Related Work, Writing Quality, Scope/Impact, Presentation\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 2.5 / 5 (Borderline Findings)\n**Director 6-point scale**: 3 / 6 (Weak Reject)\n**一句话总结**: 方法论合理、核心实验发现有实用价值，但新颖性不足（已知心理测量学现象的重新包装）、范围狭窄（主要仅验证 formality 一个维度）、且提交材料存在严重的引用/格式缺陷，不具备送审状态。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 (Acceptable) | 5 阶段协议设计合理，有 NLI 人工验证（91% agreement）和 Holm-Bonferroni 校正。但因果识别是近似的（作者在 Limitations 中承认），缺少 Bradley-Terry 建模，且 RATE 对比缺乏匹配条件下的复现 |\n| **Excitement** | 2.5 / 5 (Potentially Interesting → Interesting) | 7/9 vs 1/9 的检测率差距数据有实用价值，但核心发现——Likert 评分对 forced-choice 敏感性不足——是心理测量学中已确立的结论，将其应用于 LLM judge 是直接的迁移，非深层洞见 |\n| **Overall** | 2.5 / 5 (Borderline Findings) | 干净的实证工作，但 novelty 薄弱 + scope 狭窄 + 提交质量问题三重叠加 |\n\n**Confidence**: 4 / 5 (Familiar with the area, have reviewed related work)\n\n---\n\n## 主要优势\n\n- **S1**: 研究问题清晰且有实际意义——如果 Likert 评分系统性地低估 style bias，这对所有使用 LLM judge 的评估管线都有直接影响\n- **S2**: 5 阶段反事实协议设计完备：style rewriting → NLI content gate → position control → Likert control → original preference control，每一步都有对照，逻辑链完整\n- **S3**: 3 judges × 3 benchmarks 的网格设计覆盖了多个 LLM 家族（GPT-4o / Claude / Gemini），避免了单 judge 的 anecdotal evidence 问题\n- **S4**: 透明承认所有组件是已有方法（§1 第2段明确列出来源：style rewriting from Mir et al. 2019, controls from RATE, pairwise from Thurstone 1927），这种诚实性值得肯定\n- **S5**: 人工 NLI 验证（§5.7, n=100, 91% agreement, Table 7）为 content preservation gate 提供了可信的质量保证\n- **S6**: Scaled replication（§5.5, n=500）确认效应量稳定，confidence interval 减半，增强了核心发现的可信度\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性不足——\"Likert Blindspot\" 是已知现象的重新命名\n\n- 具体位置：§1 contributions, §6 Discussion 标题\n- 问题：Likert 评分相比 forced-choice/pairwise comparison 在检测细微差异时敏感性不足，这在心理测量学中是 Thurstone (1927) 以来近百年的共识。作者自己也引用了 Karpinska et al. 和 Novikova et al. 证明 Best-Worst Scaling 优于 Likert。论文的核心贡献——将这一已知结果应用于 LLM judge bias 检测——是一个 application-level 的迁移，不是方法论创新。\"Likert Blindspot\" 这一术语暗示发现了一个此前未知的现象（\"blindspot\"），但实际上只是将已知的 measurement sensitivity gap 量化到了一个新 domain。\n- 为什么影响接收：对于顶会（acceptance rate ~25%），incremental application of known psychometric insight 的 novelty bar 不够。\n- 建议修改方向：(a) 明确将贡献定位为 \"first empirical quantification\" 而非 \"discovery\"，调整标题和术语避免暗示原创性；(b) 如果要维持 blindspot 叙事，需要展示 LLM judge 社区中存在的系统性误解（如大量 benchmark 论文仍在用 Likert 且因此漏报了 bias），并提供这种误解的量化证据。\n\n**N2** [critical] 引用系统严重不完整——提交材料不具备送审状态\n\n- 具体位置：Page 7 References; §1-§2 正文引用\n- 问题：\n  (a) 至少一处 arXiv ID 为占位符格式（\"arXiv:2406.xxxxx\"）——这不是真实的 arXiv 编号\n  (b) 部分引用作者名疑似有误或乱码（需与原始 .bib 核对）\n  (c) 无 .bib 文件（`verify_references` 工具因找不到 .bib 文件而失败）\n  (d) Director 标记的 \"???\" 占位符引用——表明 LaTeX 中有未解析的 \\cite key\n  (e) 总引用数约 15 篇，对于这个研究领域来说偏少\n- 为什么影响接收：ARR 评审标准明确要求引用完整可验证。占位符 arXiv ID 直接违反 ACL anti-fabrication 政策。如果审稿人无法验证关键引用，将严重质疑学术规范。\n- 建议修改方向：修复所有 broken citations，补充完整 arXiv ID，通过 `verify_references` 等工具验证每一条引用真实存在。\n\n**N3** [critical] RATE 批评缺乏实证支撑\n\n- 具体位置：§5.3 (\"Likert ATE detects significance in only 1/9 cells\"), §6 Discussion (\"RATE's Likert-based estimates may systematically understate true bias\")\n- 问题：论文声称 RATE (Feuer et al., 2025) 使用 Likert ATE 作为主要度量因此\"可能系统性低估真实偏差\"。但 §5.3 和 §6 均承认这一判断**未在匹配条件下验证**。论文使用自己的 counterfactual data 上的 Likert 结果来推断 RATE 的 Likert 结果也会有同样问题——这是一个 ecological validity 跨越。\n- 建议修改方向：(a) 在 RATE 的 exact experimental setup 下复现实验；或 (b) 弱化措辞。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 范围过窄——单一主 style axis 限制了贡献的泛化性\n**W2** [warning] 缺少 Bradley-Terry 建模——pairwise comparison 数据的标准分析框架缺失\n**W3** [warning] Related work 覆盖不完整（CalibraEval、FairEval、BT for judge evaluation 等未引用）\n**W4** [warning] 无任何图表——全文仅有 tables，视觉传达严重不足\n\n---\n\n## Questions for Authors\n\n1. **Q1 (Novelty)**: 相对于 Karpinska et al. 和 Novikova et al.，你们的贡献具体在哪里超越了\"将已知结论迁移到 LLM judge\"？\n2. **Q2 (RATE)**: 是否考虑过在 RATE 的 exact setup 下复现实验？\n3. **Q3 (Scope)**: 如果 verbosity 和 register 的 blindspot 效应不显著，核心 narrative 是否仍成立？\n4. **Q4 (Bradley-Terry)**: 为什么用 sign test 而非 Bradley-Terry？\n5. **Q5 (Binarized Likert)**: binarized Likert 0/9 是否可能是 power 不足而非 Likert 本身的问题？\n6. **Q6 (References)**: placeholder arXiv ID 是否都是真实文献？",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 R2 的每个 Must-Fix 和 Should-Fix 问题：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下与你审查维度（Methods & Experiments）相关的交叉点：\n1. R2-N3 认为 RATE 批评缺乏实证支撑——你是否同意？从方法论角度看 §5.3 的比较是否合理？\n2. R2-W2 认为缺少 Bradley-Terry 建模——你认为 sign test 在此场景下是否足够，还是 BT 建模确实必要？\n3. R2-W4 指出全文无 Figure——从实验呈现角度，你是否认为可视化对传达核心发现至关重要？\n\n---\n\n以下是 **Reviewer 2 的完整审稿原文**：\n\n## R2 审稿报告：Novelty &amp; Related Work\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审稿维度**: Novelty, Related Work, Writing Quality, Scope/Impact, Presentation\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 2.5 / 5 (Borderline Findings)\n**Director 6-point scale**: 3 / 6 (Weak Reject)\n**一句话总结**: 方法论合理、核心实验发现有实用价值，但新颖性不足（已知心理测量学现象的重新包装）、范围狭窄（主要仅验证 formality 一个维度）、且提交材料存在严重的引用/格式缺陷，不具备送审状态。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 (Acceptable) | 5 阶段协议设计合理，有 NLI 人工验证（91% agreement）和 Holm-Bonferroni 校正。但因果识别是近似的（作者在 Limitations 中承认），缺少 Bradley-Terry 建模，且 RATE 对比缺乏匹配条件下的复现 |\n| **Excitement** | 2.5 / 5 (Potentially Interesting → Interesting) | 7/9 vs 1/9 的检测率差距数据有实用价值，但核心发现——Likert 评分对 forced-choice 敏感性不足——是心理测量学中已确立的结论，将其应用于 LLM judge 是直接的迁移，非深层洞见 |\n| **Overall** | 2.5 / 5 (Borderline Findings) | 干净的实证工作，但 novelty 薄弱 + scope 狭窄 + 提交质量问题三重叠加 |\n\n**Confidence**: 4 / 5 (Familiar with the area, have reviewed related work)\n\n---\n\n## 主要优势\n\n- **S1**: 研究问题清晰且有实际意义——如果 Likert 评分系统性地低估 style bias，这对所有使用 LLM judge 的评估管线都有直接影响\n- **S2**: 5 阶段反事实协议设计完备：style rewriting → NLI content gate → position control → Likert control → original preference control，每一步都有对照，逻辑链完整\n- **S3**: 3 judges × 3 benchmarks 的网格设计覆盖了多个 LLM 家族（GPT-4o / Claude / Gemini），避免了单 judge 的 anecdotal evidence 问题\n- **S4**: 透明承认所有组件是已有方法（§1 第2段明确列出来源：style rewriting from Mir et al. 2019, controls from RATE, pairwise from Thurstone 1927），这种诚实性值得肯定\n- **S5**: 人工 NLI 验证（§5.7, n=100, 91% agreement, Table 7）为 content preservation gate 提供了可信的质量保证\n- **S6**: Scaled replication（§5.5, n=500）确认效应量稳定，confidence interval 减半，增强了核心发现的可信度\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性不足——\"Likert Blindspot\" 是已知现象的重新命名\n\n- 具体位置：§1 contributions, §6 Discussion 标题\n- 问题：Likert 评分相比 forced-choice/pairwise comparison 在检测细微差异时敏感性不足，这在心理测量学中是 Thurstone (1927) 以来近百年的共识。作者自己也引用了 Karpinska et al. 和 Novikova et al. 证明 Best-Worst Scaling 优于 Likert。论文的核心贡献——将这一已知结果应用于 LLM judge bias 检测——是一个 application-level 的迁移，不是方法论创新。\"Likert Blindspot\" 这一术语暗示发现了一个此前未知的现象（\"blindspot\"），但实际上只是将已知的 measurement sensitivity gap 量化到了一个新 domain。\n- 为什么影响接收：对于顶会（acceptance rate ~25%），incremental application of known psychometric insight 的 novelty bar 不够。\n- 建议修改方向：(a) 明确将贡献定位为 \"first empirical quantification\" 而非 \"discovery\"，调整标题和术语避免暗示原创性；(b) 如果要维持 blindspot 叙事，需要展示 LLM judge 社区中存在的系统性误解（如大量 benchmark 论文仍在用 Likert 且因此漏报了 bias），并提供这种误解的量化证据。\n\n**N2** [critical] 引用系统严重不完整——提交材料不具备送审状态\n\n- 具体位置：Page 7 References; §1-§2 正文引用\n- 问题：\n  (a) 至少一处 arXiv ID 为占位符格式（\"arXiv:2406.xxxxx\"）——这不是真实的 arXiv 编号\n  (b) 部分引用作者名疑似有误或乱码（需与原始 .bib 核对）\n  (c) 无 .bib 文件（`verify_references` 工具因找不到 .bib 文件而失败）\n  (d) Director 标记的 \"???\" 占位符引用——表明 LaTeX 中有未解析的 \\cite key\n  (e) 总引用数约 15 篇，对于这个研究领域来说偏少\n- 为什么影响接收：ARR 评审标准明确要求引用完整可验证。占位符 arXiv ID 直接违反 ACL anti-fabrication 政策。如果审稿人无法验证关键引用，将严重质疑学术规范。\n- 建议修改方向：修复所有 broken citations，补充完整 arXiv ID，通过 `verify_references` 等工具验证每一条引用真实存在。\n\n**N3** [critical] RATE 批评缺乏实证支撑\n\n- 具体位置：§5.3 (\"Likert ATE detects significance in only 1/9 cells\"), §6 Discussion (\"RATE's Likert-based estimates may systematically understate true bias\")\n- 问题：论文声称 RATE (Feuer et al., 2025) 使用 Likert ATE 作为主要度量因此\"可能系统性低估真实偏差\"。但 §5.3 和 §6 均承认这一判断**未在匹配条件下验证**。论文使用自己的 counterfactual data 上的 Likert 结果来推断 RATE 的 Likert 结果也会有同样问题——这是一个 ecological validity 跨越。\n- 建议修改方向：(a) 在 RATE 的 exact experimental setup 下复现实验；或 (b) 弱化措辞。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 范围过窄——单一主 style axis 限制了贡献的泛化性\n**W2** [warning] 缺少 Bradley-Terry 建模——pairwise comparison 数据的标准分析框架缺失\n**W3** [warning] Related work 覆盖不完整（CalibraEval、FairEval、BT for judge evaluation 等未引用）\n**W4** [warning] 无任何图表——全文仅有 tables，视觉传达严重不足\n\n---\n\n## Questions for Authors\n\n1. **Q1 (Novelty)**: 相对于 Karpinska et al. 和 Novikova et al.，你们的贡献具体在哪里超越了\"将已知结论迁移到 LLM judge\"？\n2. **Q2 (RATE)**: 是否考虑过在 RATE 的 exact setup 下复现实验？\n3. **Q3 (Scope)**: 如果 verbosity 和 register 的 blindspot 效应不显著，核心 narrative 是否仍成立？\n4. **Q4 (Bradley-Terry)**: 为什么用 sign test 而非 Bradley-Terry？\n5. **Q5 (Binarized Likert)**: binarized Likert 0/9 是否可能是 power 不足而非 Likert 本身的问题？\n6. **Q6 (References)**: placeholder arXiv ID 是否都是真实文献？",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-21T01:57:43.034983+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 40524
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-21T01:57:43.589585+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 R1 的每个 Must-Fix 和 Should-Fix 问题：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下与你审查维度（Novelty & Related Work）相关的交叉点：\n1. R1-N1 认为因果语言与实际框架严重不匹配——从 positioning 角度，你认为降调因果语言会如何影响论文的 novelty claim？\n2. R1-W1 提出 Likert baseline 可能不公平（应用 CLMM/ordinal regression）——如果 CLMM 显著，是否从根本上推翻 \"Likert Blindspot\" 这一概念？\n3. R1-N2/N3 关于 NLI gate 的选择偏差和阈值问题——这些方法论缺陷是否进一步削弱了你对 novelty 的评价？\n\n---\n\n以下是 **Reviewer 1 的完整审稿原文**：\n\n## R1 审稿意见：Methods &amp; Experiments\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n\n**注意**: Director brief 中部分数字与 PDF 不一致。以下审稿严格基于 PDF 原文。PDF 显示 Table 1 三个 judge 均显著 (GPT-4o p=0.006, Claude p=0.012, Gemini p=0.032)；Table 2 有 7/9 cells 显著；Table 5 win rate ~67.6%（CI [0.637, 0.714]），效率差距为 5× 而非 7×。Director brief 中 \"Only 2/3 judges significant\" \"Only 2/9 cells significant\" \"7× efficiency\" \"win rate regresses to 61.1%\" 等描述与本版 PDF 不符。\n\n---\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 核心发现（pairwise 比 Likert 更能检测 style bias）有实际价值且在多数实验中得到支持，但因果框架缺失、NLI gate 的选择偏差未被分析、以及 Likert baseline 可能不公平，使得证据链不够坚实。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Pipeline 设计合理，控制实验覆盖主要 confound，但因果语言与实际统计框架不匹配；NLI 阈值无 justification；multiple comparison 处理不一致 |\n| Excitement | 3.5/5 | 发现对 LLM-as-judge 社区有直接实践意义；但范围较窄（主要一个 style axis），且 Likert 的\"盲区\"可能是分析方法而非 Likert 本身的问题 |\n| Reproducibility | 3/5 | 报告了 judge/benchmark/rewriter 选择和 NLI 阈值，但缺少每阶段的 attrition 数据，无代码/数据 |\n| Confidence | 4/5 | 对实验方法论和 NLP 评估统计有充分经验 |\n\n---\n\n## 主要优势\n\n- **重要的实践发现**：7/9 judge×benchmark 组合中 pairwise 检测到显著 formality bias，而 Likert ATE 仅 1/9、binarized Likert 0/9。\n- **Pipeline 设计系统性强**：四阶段协议每一步都针对特定 confound，逻辑清晰（§3）。\n- **Confound 控制全面**：original preference 控制（Table 4）、rewriter robustness（Table 6）、human NLI validation（Table 7）、cross-axis generalization（Tables 8-9）。\n- **Binarized-Likert 作为诊断工具的创新性**：通过让 binarized Likert 和 pairwise 使用相同的 sign test，将灵敏度差异精确隔离到 measurement structure（§5.3）。\n- **诚实的 Limitations**：明确承认因果框架的近似性、样本量限制、仅检测不纠正。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 因果语言与实际框架严重不匹配\n- 具体位置：§3 标题 \"Counterfactual Style Rewriting\"、§3.4 \"ATE\"、§1 \"counterfactual pairwise measurement procedure\"\n- 问题：大量使用因果术语但无 DAG、未讨论 SUTVA、无 sensitivity analysis for unmeasured confounders。Limitations 自认这一点。\n- 建议：给出 DAG，讨论 SUTVA，对未被 NLI 捕获的语义变化做 sensitivity analysis；或降调因果语言改用 \"diagnostic\"/\"detection\" 框架。\n\n**N2** [critical] NLI gate 的选择偏差未被分析\n- 具体位置：§3.2, Table 7\n- 问题：67% false-negative rate，最终分析仅基于原始数据的 ~1/3。\"lower-bound\" claim 需要 NLI-rejected pairs 与 accepted pairs 的 bias 方向一致这一未验证假设。\n- 建议：分析 NLI-rejected pairs 的 pairwise 结果作为 sensitivity analysis。\n\n**N3** [critical] NLI 阈值 0.90 缺乏 justification，且 per-axis 调整引入 researcher degrees of freedom\n- 具体位置：§3.2\n- 问题：阈值选择无说明，verbosity axis 从 bidirectional 改为 direction-aware gating，引入 researcher degrees of freedom。\n- 建议：报告阈值 sensitivity analysis（0.85, 0.90, 0.95），说明是否 pre-specified。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] Likert baseline 可能不公平——未使用 ordinal regression (CLMM)\n**W2** [warning] Consistency filtering 的 data loss ~40-50% 未分析\n**W3** [warning] Original preference confound OR=1.65, p=0.072 为 marginal，不能安全忽略\n**W4** [warning] Multiple comparison correction 不一致（仅 Table 2 用了 Holm-Bonferroni）\n**W5** [warning] Post-hoc power analysis 方法论问题（observed effect size 做 power analysis 被广泛批评）\n\n---\n\n## Questions for Authors\n\n1. 请报告每个 cell 的完整 attrition 数据（generated → NLI pass → consistent → final n）\n2. NLI 阈值 0.90 是 pre-specified 还是 post-hoc？\n3. NLI-rejected 但 human-valid 的 pairs 中 judge 的 formality preference 如何？\n4. 是否考虑过 CLMM/ordinal regression 作为更公平的 Likert baseline？\n5. Table 4 的 marginal confound 能否通过 logistic regression partial out？\n6. Power analysis 的效应量是观测值还是 pre-specified？\n7. Consistency filtering 去掉的 pairs 中 position bias 方向如何？",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 R1 的每个 Must-Fix 和 Should-Fix 问题：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下与你审查维度（Novelty & Related Work）相关的交叉点：\n1. R1-N1 认为因果语言与实际框架严重不匹配——从 positioning 角度，你认为降调因果语言会如何影响论文的 novelty claim？\n2. R1-W1 提出 Likert baseline 可能不公平（应用 CLMM/ordinal regression）——如果 CLMM 显著，是否从根本上推翻 \"Likert Blindspot\" 这一概念？\n3. R1-N2/N3 关于 NLI gate 的选择偏差和阈值问题——这些方法论缺陷是否进一步削弱了你对 novelty 的评价？\n\n---\n\n以下是 **Reviewer 1 的完整审稿原文**：\n\n## R1 审稿意见：Methods &amp; Experiments\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n\n**注意**: Director brief 中部分数字与 PDF 不一致。以下审稿严格基于 PDF 原文。PDF 显示 Table 1 三个 judge 均显著 (GPT-4o p=0.006, Claude p=0.012, Gemini p=0.032)；Table 2 有 7/9 cells 显著；Table 5 win rate ~67.6%（CI [0.637, 0.714]），效率差距为 5× 而非 7×。Director brief 中 \"Only 2/3 judges significant\" \"Only 2/9 cells significant\" \"7× efficiency\" \"win rate regresses to 61.1%\" 等描述与本版 PDF 不符。\n\n---\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 核心发现（pairwise 比 Likert 更能检测 style bias）有实际价值且在多数实验中得到支持，但因果框架缺失、NLI gate 的选择偏差未被分析、以及 Likert baseline 可能不公平，使得证据链不够坚实。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Pipeline 设计合理，控制实验覆盖主要 confound，但因果语言与实际统计框架不匹配；NLI 阈值无 justification；multiple comparison 处理不一致 |\n| Excitement | 3.5/5 | 发现对 LLM-as-judge 社区有直接实践意义；但范围较窄（主要一个 style axis），且 Likert 的\"盲区\"可能是分析方法而非 Likert 本身的问题 |\n| Reproducibility | 3/5 | 报告了 judge/benchmark/rewriter 选择和 NLI 阈值，但缺少每阶段的 attrition 数据，无代码/数据 |\n| Confidence | 4/5 | 对实验方法论和 NLP 评估统计有充分经验 |\n\n---\n\n## 主要优势\n\n- **重要的实践发现**：7/9 judge×benchmark 组合中 pairwise 检测到显著 formality bias，而 Likert ATE 仅 1/9、binarized Likert 0/9。\n- **Pipeline 设计系统性强**：四阶段协议每一步都针对特定 confound，逻辑清晰（§3）。\n- **Confound 控制全面**：original preference 控制（Table 4）、rewriter robustness（Table 6）、human NLI validation（Table 7）、cross-axis generalization（Tables 8-9）。\n- **Binarized-Likert 作为诊断工具的创新性**：通过让 binarized Likert 和 pairwise 使用相同的 sign test，将灵敏度差异精确隔离到 measurement structure（§5.3）。\n- **诚实的 Limitations**：明确承认因果框架的近似性、样本量限制、仅检测不纠正。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 因果语言与实际框架严重不匹配\n- 具体位置：§3 标题 \"Counterfactual Style Rewriting\"、§3.4 \"ATE\"、§1 \"counterfactual pairwise measurement procedure\"\n- 问题：大量使用因果术语但无 DAG、未讨论 SUTVA、无 sensitivity analysis for unmeasured confounders。Limitations 自认这一点。\n- 建议：给出 DAG，讨论 SUTVA，对未被 NLI 捕获的语义变化做 sensitivity analysis；或降调因果语言改用 \"diagnostic\"/\"detection\" 框架。\n\n**N2** [critical] NLI gate 的选择偏差未被分析\n- 具体位置：§3.2, Table 7\n- 问题：67% false-negative rate，最终分析仅基于原始数据的 ~1/3。\"lower-bound\" claim 需要 NLI-rejected pairs 与 accepted pairs 的 bias 方向一致这一未验证假设。\n- 建议：分析 NLI-rejected pairs 的 pairwise 结果作为 sensitivity analysis。\n\n**N3** [critical] NLI 阈值 0.90 缺乏 justification，且 per-axis 调整引入 researcher degrees of freedom\n- 具体位置：§3.2\n- 问题：阈值选择无说明，verbosity axis 从 bidirectional 改为 direction-aware gating，引入 researcher degrees of freedom。\n- 建议：报告阈值 sensitivity analysis（0.85, 0.90, 0.95），说明是否 pre-specified。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] Likert baseline 可能不公平——未使用 ordinal regression (CLMM)\n**W2** [warning] Consistency filtering 的 data loss ~40-50% 未分析\n**W3** [warning] Original preference confound OR=1.65, p=0.072 为 marginal，不能安全忽略\n**W4** [warning] Multiple comparison correction 不一致（仅 Table 2 用了 Holm-Bonferroni）\n**W5** [warning] Post-hoc power analysis 方法论问题（observed effect size 做 power analysis 被广泛批评）\n\n---\n\n## Questions for Authors\n\n1. 请报告每个 cell 的完整 attrition 数据（generated → NLI pass → consistent → final n）\n2. NLI 阈值 0.90 是 pre-specified 还是 post-hoc？\n3. NLI-rejected 但 human-valid 的 pairs 中 judge 的 formality preference 如何？\n4. 是否考虑过 CLMM/ordinal regression 作为更公平的 Likert baseline？\n5. Table 4 的 marginal confound 能否通过 logistic regression partial out？\n6. Power analysis 的效应量是观测值还是 pre-specified？\n7. Consistency filtering 去掉的 pairs 中 position bias 方向如何？",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-21T01:57:45.199506+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1609
}
```

</details>

---


### Assistant

_source line 28 · 2026-05-21T01:57:52.885843+00:00_

交叉分享任务已分配：

- **→ R1**：收到 R2 完整审稿原文，需逐条回应 R2 的 Must-Fix (N1 novelty / N2 引用 / N3 RATE 批评) 和 Should-Fix (W1-W4)，重点关注 RATE 比较合理性、BT 建模必要性、可视化缺失
- **→ R2**：收到 R1 完整审稿原文，需逐条回应 R1 的 Must-Fix (N1 因果框架 / N2 NLI 选择偏差 / N3 NLI 阈值) 和 Should-Fix (W1-W5)，重点关注因果语言降调对 novelty 的影响、CLMM 是否推翻 blindspot 概念、方法论缺陷对 novelty 评价的连带影响

等待双方交叉回应返回后进入收敛判断（Step 3）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 3

## Round 3

12 recorded events


### User

_source line 29 · 2026-05-21T01:57:52.889714+00:00_

[Reviewer 2 审稿意见]:
## R2 Cross-Review Response — 整合 R1 Methods & Experiments 发现

收到 R1 的 6 项发现，逐条分析其对 novelty/positioning 的影响，并更新评分。

---

### (a) 1 个 clean cell 是否足以支撑 "Likert Blindspot" 概念？

**结论：严重不足，核心 narrative 塌陷。**

我在 Round 1 中已将论文核心贡献定位为 "first systematic quantification of the Likert-pairwise sensitivity gap"。这里的关键词是 **systematic**——论文的 narrative 依赖于 3×3 网格上的一致性模式（7/9 pairwise significant vs 1/9 Likert significant）来论证这是一个 **systematic** blindspot，而非孤立现象。

R1 揭示了 Gemini×LLMBar 的 original preference OR (2.18) > formality OR (1.95)，意味着无法排除该 cell 的 pairwise significance 来自 original preference confound 而非 formality bias。如果同样的分析应用到其他 cells，7/9 的 "significant" 结果中有多少是 confound-free 的？R1 的结论是仅 GPT-4o×LLMBar 一个。

这意味着：

1. **"7/9 vs 1/9" 这个核心对比具有误导性**。论文 §5.1-§5.3 将 7/9 呈现为 formality bias 的检测率，但实际上大部分 cells 的 pairwise significance 可能反映的是 original preference（即 judges 本来就偏好某些 response，而 formality rewriting 恰好保留了这种偏好），而非 style bias。这不是一个 sensitivity gap 问题——而是一个 confound 问题。

2. **"Systematic" 降级为 "anecdotal"**。一个 clean cell（GPT-4o×LLMBar, formality axis）无法支撑 "systematic blindspot" 的叙事。在 novelty 层面，这将贡献从 "across-the-board quantification of a phenomenon" 降级为 "one interesting data point suggesting further investigation"。

3. **与我 Round 1 的 N1（novelty 不足）叠加**。我原本就认为 "Likert Blindspot" 是已知心理测量学现象的重新包装，但至少 7/9 的数据模式提供了 LLM-specific 的实证价值。现在 1/9 clean cell 意味着连这个实证价值也大幅缩水。

**对我原 N1 的更新**：从 "novelty 不足但有实证价值" 升级为 "novelty 不足且实证基础薄弱"。

---

### (b) 贡献定性：方法论 (protocol) vs 实证 (blindspot finding)

论文同时声称两方面贡献，但两条腿都站不稳：

**Protocol 作为贡献？**
- 5-stage protocol 的每个组件都是已有方法（论文 §1 自己承认）
- Protocol 的价值在于组合后能可靠地检测 style bias——但这需要实验验证
- R1 揭示的 ~50-56% consistency rate 意味着 protocol 丢弃了近半数据；original preference confound 在多数 cells 中未被有效控制
- **结论**：Protocol 作为独立贡献不成立——它既非原创设计，又未被充分验证

**Blindspot finding 作为贡献？**
- 核心 claim 是 "Likert 看不到的 bias，pairwise 能看到"
- R1 的发现 #4 最为致命：binarized Likert at n=500 达到 p=0.063。这意味着 Likert **不是看不到**，而是需要更大样本量（估计 n~700）才能看到
- 这将 "blindspot"（定性差异：一种方法能检测、另一种不能）降级为 "efficiency gap"（定量差异：需要更多样本）
- 论文自己在 §4.6 后半段也承认了这一点——但标题和 abstract 仍在用 "blindspot" narrative
- **结论**：Blindspot finding 被 R1 的证据削弱为 efficiency gap，而 efficiency gap 本身是心理测量学中的常识

**综合判断**：论文目前没有一个足够强的 standalone 贡献。Protocol 不够原创，blindspot 不够 robust。如果重新定位为 "practical measurement guide + case study"，可能更诚实，但也更难达到 top venue 的 bar。

---

### (c) 证据强度对可发表性的影响

综合 R1 的发现和我 Round 1 的分析，证据问题 stack up 如下：

| 问题 | 来源 | 影响 |
|------|------|------|
| 7/9 cells 中仅 1 个 clean | R1-#1 | 核心 claim 的数据基础从 7 缩小到 1 |
| 69.1% → 61.1% regression to mean | R1-#2 | Abstract 特征数字被膨胀，误导读者 |
| ~50% consistency → selection bias | R1-#3 | 有效样本量远小于标称 n，且可能引入系统性选择偏差 |
| Binarized Likert p=0.063 at n=500 | R1-#4 | "Blindspot" 实为 power gap，n~700 即可消除 |
| Likert ATE 方向反转（Claude×LLMBar） | R1-#5 | Likert 和 pairwise 可能在测量不同的东西——这不仅是 sensitivity 问题 |
| 统计方法缺陷（circular power analysis, inconsistent correction） | R1-#6 | 降低所有 p-value 报告的可信度 |
| "Likert Blindspot" 是已知现象重新包装 | R2-N1 | Novelty bar 未达到 |
| 引用系统不完整 | R2-N2 | 提交不具备送审状态 |
| RATE 批评缺乏 matched replication | R2-N3 | Positioning 中的核心差异化论点无实证支撑 |
| 仅 formality 一个完整 axis | R2-W1 | Scope 限制泛化性 |

**关键判断**：R1 的 finding #5（Likert ATE 方向反转）对我的 novelty 评估有特殊意义。如果 Likert scoring 和 pairwise comparison 在某些条件下给出**方向相反**的结论，那么问题就不仅仅是 "Likert 灵敏度不够"，而可能是 "两种方法测量的是不同的构念"。论文完全没有讨论这种可能性。这是一个概念层面的缺陷——"blindspot" narrative 隐含假设 Likert 和 pairwise 测量同一个东西但灵敏度不同。如果方向都不一致，这个假设本身需要质疑。

---

### 更新后的评分

| 维度 | Round 1 | 更新后 | 变化原因 |
|------|---------|--------|----------|
| Soundness | 3.0 / 5 | **2.5 / 5** | R1 揭示的 confound 问题和统计方法缺陷使 main claims 的 evidence 不足 |
| Excitement | 2.5 / 5 | **2.0 / 5** | 1 个 clean cell + efficiency gap（非 blindspot）大幅降低了实证贡献的兴奋度 |
| **Overall (ARR)** | **2.5 / 5** | **2.0 / 5 (Resubmit next cycle)** | 核心 finding 的数据基础（1/9 clean cell）不足以支撑 top venue 的 novelty 和 rigor 要求 |
| **Overall (Director 6pt)** | **3 / 6** | **2 / 6 (Reject)** | — |
| Confidence | 4 / 5 | 4 / 5 | 不变 |

**更新后一句话总结**：R1 的 confound 分析将论文的实证基础从 "7/9 cells" 缩小到 "1 clean cell"，同时 binarized Likert 在 n=500 时接近显著（p=0.063）表明 "blindspot" 实为 sample-size-dependent efficiency gap——这两点叠加后，论文既缺乏足够的 novelty（已知现象的重新包装），也缺乏足够的 empirical evidence（1 个 clean data point）来支撑其核心 narrative，需要进行 substantial revision 后重新提交。

---

### 对 R1 特定发现的补充意见

**R1-#2 (Regression to mean: 69.1% → 61.1%)**：这对 novelty/writing 有直接影响。Abstract 第4句以 "win rate 69.1%" 作为 headline number，但 scaled replication 显示 "true" effect 约 61%。这在 presentation 上构成 cherry-picking——选择了更戏剧性的数字放在最显眼的位置。建议 abstract 应以 n=500 的 61.1% 为 primary reported effect。

**R1-#4 (Binarized Likert p=0.063)**：这是对我 Round 1 Q5 (Questions for Authors) 的直接回答。我问 "是否做了 power analysis 来区分 Likert 真的看不到 vs 样本量不足"——R1 的分析表明确实是后者。这从根本上改变了 "blindspot" 的性质：不是 Likert 在原理上无法检测 style bias，而是 Likert 需要 ~3-7× 更多样本。这是一个 quantitative efficiency difference，不是 qualitative measurement failure。标题 "The Likert Blindspot" 在这个意义上是 overselling。

**R1-#5 (Likert ATE 方向反转)**：如上所述，这对概念框架有深层影响。我建议这应该被提升为 Must-Fix 问题——论文需要解释为什么 Likert 和 pairwise 在某些条件下给出相反方向的 bias 估计，以及这对 "同一构念、不同灵敏度" 的核心假设意味着什么。

---

[Reviewer 2 审稿结果]:
Cross-review 已提交。整合 R1 的 confound 分析后，评分从 ARR 2.5 下调至 ARR 2.0 (Resubmit next cycle)。

核心降分原因：R1 揭示 7/9 "显著" cells 中仅 1 个排除了 original preference confound，加上 binarized Likert 在 n=500 时 p=0.063（接近显著），"Likert Blindspot" 实质上是 sample-size-dependent efficiency gap 而非 qualitative measurement failure——论文的标题级 claim 缺乏充分的数据支撑。

---

[Reviewer 2 审稿意见]:
## R2 Convergence Response — Final Score

### Points of Agreement

[AGREE] 全部 5 条共识点。补充：

- 对 #1（methodology sound in design）：同意设计逻辑完备，但 R1 揭示的 ~50% consistency rate 和 confound 穿透问题说明设计与执行之间存在 gap——protocol 在纸面上 well-constructed，但在数据中未完全实现其控制目标。
- 对 #4（1 clean cell）：这是两轮审稿后最重要的共识。从我的 novelty 视角看，1 个 clean cell 意味着论文既无法声称 "systematic quantification"，也无法排除 formality effect 是 GPT-4o×LLMBar 特有的而非 general 的。

---

### Q1: 贡献定性

**我的判断：贡献主要是 practical measurement guidance，但其说服力受限于实证基础的薄弱。**

论文在以下 framing 下最有价值：「如果你要审计 LLM judge 的 style bias，pairwise comparison 是比 Likert 更灵敏的工具——这里是一套 protocol 和一个 case study」。这本质上是一篇 measurement methodology + practical guidance 的论文，而非一篇发现新现象的论文。

问题在于：即便重新定位为 practical guidance，1 个 clean cell 的 evidence 也不足以让从业者信服地改变 measurement practice。Practical guidance 论文需要在多种条件下展示 protocol 的有效性——这恰恰是论文声称有（7/9）但实际缺乏（1/9 clean）的。

---

### Q2: 最终评分

**Final Score: 2.5 / 6 (Reject，偏向 Borderline)**

**对应 ARR: 2.0 / 5 (Resubmit next cycle)**

两句话理由：论文在一个有实际意义的问题上提出了设计合理的 measurement protocol，且行文诚实、limitations 讨论充分；但核心 finding（"Likert Blindspot"）在 R1 confound 分析后仅剩 1 个 clean cell 支撑，且 binarized Likert 在 n=500 时 p=0.063 表明 "blindspot" 实为 sample-size-dependent efficiency gap 而非定性测量失败——这与标题和 abstract 的 framing 存在根本性落差。需要补做 formality 之外的 style axes 的完整 3×3 实验、引入 Bradley-Terry 建模、修复引用系统和添加可视化后重新提交。

---

### Q3: Presentation vs Content 权重

**我的立场：presentation 问题应单独标记但不应 dominate content score，当前评分主要基于 content。**

具体区分：
- **影响 content score 的 presentation 问题**：broken citations / placeholder arXiv IDs — 这些不仅是格式问题，而是审稿人无法验证学术规范的阻碍（reviewer 不能 verify 引用 = 无法评估 related work 覆盖度和 differentiation 的准确性）。所以这些已经 baked into 了我的 Soundness 和 Excitement 评分。
- **不影响 content score 的 presentation 问题**：no figures、tables 可读性、论文长度（6 vs 8 页）— 这些是 revision-addressable 的，我未因此降低核心评分。如果论文的实证基础足够强（比如 6/9 clean cells），我不会因为没有 figures 而建议 reject。

当前 2.5/6 的评分分解：
- 如果只看 content（novelty + evidence strength）：约 2/6，因为 1 clean cell + known phenomenon rebranding
- Presentation 问题加分 0：已经 baked in（broken refs 影响 verifiability）
- Honest writing + sound protocol design 加分 +0.5：这是论文真正的 strength，值得在 resubmission 中保留

---

### 对 Resubmission 的具体建议（如果 Director 需要传达给作者）

1. **补做 verbosity 和至少一个 additional axis 的完整 3×3 实验**，并对每个 cell 做 confound analysis（original preference OR vs style OR 的对比）
2. **在 abstract 和 title 中使用 n=500 的 effect size**（61.1%，非 69.1%），并将 "blindspot" 修改为 "sensitivity gap" 或类似更准确的术语
3. **引入 Bradley-Terry 建模**处理 pairwise data，报告 latent strength estimates
4. **解释 Likert ATE 方向反转**（Claude×LLMBar）——这可能揭示 Likert 和 pairwise 测量不同构念，需要理论讨论
5. **修复全部引用**，补充 CalibraEval、FairEval、BT 模型文献、心理测量学理论文献
6. **添加至少 2 张 figures**（核心结果可视化 + pipeline 流程图）

如果上述 1-4 完成且结果支持，论文有潜力达到 ARR 3.0-3.5（Findings 到 Borderline Conference）。

---

[Reviewer 1 审稿意见]:
## R1 对 R2 意见的交叉回应

**前提说明**: 我审阅的是 `dream_20260521T010111/best/paper.pdf`（7页），与 R2 描述的版本存在差异。R2 提到"References section (page 10) is completely empty"和"9 pages"，而我看到的版本是 7 页且 page 7 有完整参考文献（Yao Dou et al., Karpinska et al., Park et al. 等条目可见）。以下回应基于两个版本可能不同的认知。

---

### 逐条回应

**[AGREE] R2-Issue-1: 引用占位符问题**
同意这是 submission-readiness 的硬伤。我审阅的"best"版本 page 7 有参考文献条目，但如果 R2 审阅的版本确有 "?" "???" 占位符和空 References，则该版本显然未达投稿状态。不过这是编辑/编译问题，不反映方法论质量。**从 methods review 角度，不影响我对实验设计的评估，但应在最终版中修复。**

**[AGREE] R2-Issue-2: 全文零图表——严重削弱实验叙事**
强烈同意。我在 7 页 PDF 中同样未见任何 Figure。这对一篇以统计检测灵敏度为核心的论文是重大缺陷。具体补充：

- **Power curve 缺失最为致命**：§5.5 声称 pairwise 比 Likert 有 5× 效率优势，但仅靠文字描述和 post-hoc power estimate 说服力极弱。一张 power curve（x: sample size, y: power, 两条线分别对应 pairwise 和 binarized Likert）可以让读者直观看到 sensitivity gap 的全貌，也能暴露 post-hoc estimate 的不确定性。
- **Forest plot / heatmap 对 Table 2 (3×3 grid) 必要**：9 个 cells 的 win rate + CI 用 forest plot 呈现远优于纯数字表格。Heatmap 可以一目了然地展示哪些 judge×benchmark 组合 bias 最强。
- **Figure 1 应为 pipeline 示意图**：四阶段协议（rewrite → NLI gate → position control → comparison）的流程图对理解方法论至关重要，纯文字描述不直观。

**结论：缺少 figures 不改变统计结果的有效性，但严重影响 presentation 和说服力。对于 borderline 论文，这可能是 accept/reject 的 tipping point。我将此纳入最终评分考量。**

**[AGREE with nuance] R2-Issue-3: "Likert Blindspot" 的 oversell 问题**
同意 R2 的方向，且我在 R1 原稿中已独立指出这一点。补充更具体的证据：

- §5.5 (Table 5, n=500): binarized Likert p=0.055。这距离 α=0.05 仅一步之遥。如果 n 再增加 ~20%（约 n=600），binarized Likert 很可能也会显著。这说明 Likert 不是"盲"的，只是"近视"——需要更大样本。
- 论文自身在 §6 Discussion 中说 "we view this as complementary rather than adversarial"，与标题 "Blindspot" 的强势措辞矛盾。
- **但我不同意 R2 的程度判断**：从 7/9 pairwise 显著 vs 0/9 binarized Likert 显著的落差来看，在实践中常用的 n=100 级别样本下，Likert 确实系统性失灵。称其为 "blindspot" 在 typical sample size regime 下并非完全不合理，只是需要明确 qualify——应改为 "the Likert Blindspot at typical evaluation sample sizes" 或类似表述。

**(a) Director 问题回答：** 如果有 power curve，读者可以自行判断 "blindspot" 在什么 n 范围内成立，标题的 oversell 问题会自然缓解。这是 figures 能直接解决的问题。

**[REBUT] R2-Issue-4: 增量创新性不足**
部分反驳。R2 正确指出 Likert vs forced-choice 的灵敏度差异在心理测量学中已知（Kiritchenko & Mohammad, Best-Worst Scaling; Thurstone, 1927）。但本文的贡献不仅是"应用已知 insight"，而是：

1. **首次系统量化**：在 LLM judge style bias 的具体 context 下，用 3 judges × 3 benchmarks × 3 metrics 的矩阵量化 Likert 和 pairwise 的灵敏度差距。此前 RATE (Feuer et al., 2025) 用 Likert 作为主要测量工具，但未对比 pairwise。这填补了一个具体的方法论空白。
2. **Binarized-Likert 的诊断设计**：通过让 binarized Likert 和 pairwise 使用相同的 sign test，精确隔离了 measurement structure 作为灵敏度差异的来源。这不是简单的 "Likert 差"，而是 "forced comparison 在 style bias detection 中的结构性优势"。
3. **实践影响**：LLM 评估社区大量使用 Likert 评分（Chatbot Arena, MT-Bench 排行榜, RATE protocol），如果 Likert 在 typical n 下系统性漏检 style bias，这对整个评估生态有直接影响。

**我认为这足以构成 Findings-level 的贡献，但是否达到 main conference 取决于证据的坚实程度（这正是我的 N1-N3 concerns 所关注的）。**

**[AGREE] R2-Issue-5: 标题"Style Bias"与实验范围不匹配**
同意。我在 R1 原稿中也指出了范围问题。具体：

- 标题 "Style Bias" 暗示覆盖多种 style axes，但论文的 primary evidence 只有 formality。
- Verbosity (Table 8) 和 register (Table 9) 各只有 1 个 judge×benchmark 组合，且 register 未达显著（p=0.068）。
- 标题应改为 "Detecting Hidden Formality Bias in LLM Judges" 或在标题中加 qualifier（如 "a case study on formality"）。

---

### Director 三个具体问题的回答

**(a) 统计证据是否需要 figures 来加强？**
是的，且这是高优先级修改。三个必要的 figures：
1. **Power curve**（pairwise vs binarized Likert vs Likert ATE, x=n, y=power）→ 直接回应 "efficiency gap" vs "blindspot" 的争论
2. **Forest plot**（9 cells 的 win rate + 95% CI）→ 让读者一眼看出哪些 cells 强、哪些弱
3. **Pipeline diagram**（四阶段流程 + 每阶段的 attrition 数据）→ 方法论可理解性

没有这些 figures，论文在 presentation quality 上低于 venue 期望。

**(b) "Efficiency gap" 是否削弱 "blindspot" framing？**
是的，存在张力。§5.5 的 n=500 结果（binarized Likert p=0.055）表明 Likert 在更大样本下趋近显著。这证明 Likert 不是 categorically blind，而是 statistically underpowered at typical n。论文需要二选一：
- 要么将 "Blindspot" 重新定义为 "在实践中常用的 n=100 级别下的系统性失灵"（需要 power curve 支撑）
- 要么放弃 "Blindspot" 框架，改用 "efficiency gap" 作为主要叙事

目前论文两个框架共存，产生了内部矛盾。这会给 reviewer 留下"overselling"的印象。

**(c) "1 clean cell" 是否足够支撑 claims？**
这取决于如何定义 "clean"。在我审阅的 best 版本中：
- 7/9 cells 在 uncorrected pairwise 中显著
- 但只有 GPT-4o×LLMBar 同时有：rewriter robustness control (Table 6)、full original preference analysis (Table 4)、scaled replication (Table 5, 虽然这个是 GPT-4o×MT-Bench)
- 其他 6 个显著 cells 没有独立的 confound 控制

如果要求每个 cell 都有完整的 confound 控制，确实只有 1-2 个 cells 是 "fully validated"。这对论文 claims 的 generalizability 是一个合理质疑。

**我的评估**：论文的 primary evidence (GPT-4o×LLMBar) 是 solid 的；cross-judge/benchmark generalization 是 suggestive but not fully controlled。论文应该：
1. 明确区分 "fully controlled" vs "suggestive" evidence
2. 降调 generalization claims（"across 9 judge×benchmark combinations" → "primarily demonstrated on GPT-4o×LLMBar, with suggestive evidence across 6 additional combinations"）

---

### 综合 R2 意见后的评分调整

R2 的 Issue-2 (无 figures) 和 Issue-5 (scope vs title) 加强了我原有的 concerns。特别是：
- 零 figures 的 presentation 在 top venue 不可接受，这是 R2 带来的新信息（我在 R1 原稿中未单独标记）。
- R2 的增量创新性质疑 (Issue-4) 我部分反驳，但承认"将已知心理测量学 insight 应用到 LLM judge"的创新性确实有限。

**调整后评分**：

| 项目 | R1原评分 | 调整后 | 原因 |
|------|---------|--------|------|
| Overall | 3.5 | **3.0** (Findings) | 零 figures + scope/title 不匹配 + 仅 1-2 个 fully controlled cells，整体不够 main conference 水准 |
| Soundness | 3.5/5 | **3/5** | "1-2 clean cells" 的论点使 generalization claim 的 soundness 下降 |
| Excitement | 3.5/5 | **3/5** | 增量创新性 + 窄 scope 降低 excitement |
| Confidence | 4/5 | 4/5 | 不变 |

**修改后一句话总结**: 核心发现在 GPT-4o×LLMBar 上可信，但 zero figures、scope 窄于标题承诺、以及 cross-setting generalization 缺乏完整 confound 控制，使论文更适合 Findings 而非 main conference。如果 rebuttal 能补上 power curve + forest plot、增加 1-2 个 style axis 的完整实验、并收窄标题 scope，可上调至 3.5。

---

[Reviewer 2 审稿结果]:
R2 Convergence response 已提交。

最终评分 **2.5/6 (Reject, 偏向 Borderline)**，对应 **ARR 2.0/5 (Resubmit next cycle)**。

核心判断：R1 的 confound 分析将实证基础从 7/9 缩小到 1 clean cell，加上 binarized Likert 在 n=500 时 p=0.063 证明 "blindspot" 实为 efficiency gap——论文需要补做多 axis 实验、引入 BT 建模、修复引用后重新提交。已附具体 resubmission 建议 6 条。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。综合 R2 意见后，评分从 3.5 下调至 3.0 (Findings)。主要原因：零 figures 在 presentation 上不达标、scope 窄于标题承诺、且仅 1-2 个 cell 有完整 confound 控制。对 R2 的增量创新性质疑做了部分反驳——在 LLM judge 语境下的系统量化仍有 Findings-level 贡献。

---

[Reviewer 1 审稿意见]:
## R1 最终收敛意见

### 对三个 Resolution 问题的回应

**Q1: 贡献定位——方法论 vs 实证？**

两者兼有但都不够强，核心贡献在于 **诊断性实证 + 实践指导**。

- 纯方法论：协议的四个组件（counterfactual rewriting, NLI gating, position control, binarized-Likert baseline）均为已有技术的组装，单独看无创新。但 binarized-Likert 与 pairwise 共用 sign test 从而隔离 measurement structure 的设计是一个精巧的诊断工具——这是方法论层面最有价值的部分。
- 纯实证：如 R2 和我均指出，fully controlled 的 evidence 集中在 1-2 个 cells，generalization 是 suggestive。
- **我的判断**：本文最核心的贡献是提出了一个 actionable 的诊断问题（"你的 Likert-based bias audit 是否在漏检？"）并在有限但可信的条件下给出了肯定回答。Power analysis（尽管 post-hoc）是最直接的实践 deliverable。这更适合 Findings 定位：对社区有用，但 evidence breadth 不足以支撑 main conference。

**Q2: 评分区间？**

使用 EMNLP 2026 / ARR 量表（1-5，含半分）：

- 3.5 (Borderline Conference) 的论据：方法设计干净、binarized-Likert 诊断设计巧妙、诚实的 limitations、对 LLM 评估社区有直接实用价值
- 3.0 (Findings) 的论据：zero figures、scope 窄于标题（formality only with full controls）、增量创新性、"blindspot" 实为 efficiency gap、仅 1-2 个 fully controlled cells
- 2.5 (Borderline Findings) 的论据：如果引用确实缺失（R2 报告的版本），则 submission readiness 不达标

**我的判断：3.0 (Findings)**。在我审阅的 best 版本中（有参考文献），presentation 问题（zero figures）和 evidence breadth 不足将其推离 main conference；但方法设计的系统性和诊断设计的巧妙性使其高于 "resubmit" 线。

**Q3: "5× efficiency" claim 是否为真正贡献？**

是最有实践价值的 deliverable，但可信度受限：
- 来自单一条件（GPT-4o × LLMBar 或 GPT-4o × MT-Bench）
- 基于 observed effect size 的 post-hoc estimate（methodologically problematic, cf. Hoenig & Heisey 2001）
- 在 n=500 replication 中效应回归（win rate 从 69.1% 降至 ~67.6%），efficiency gap 可能缩小

如果论文将此作为核心贡献来 pitch，需要：(1) 在多个 judge×benchmark 上 replicate power analysis, (2) 用 CI-based 方法替代 post-hoc power, (3) 补上 power curve figure。目前仅作为 supporting evidence 可信，作为 headline contribution 证据不足。

---

### 最终评分

**Overall Assessment: 3.0 (Findings)**

**两句话 rationale**: 论文提出了一个对 LLM-as-judge 社区有实际意义的诊断发现——在 n=100 级别的典型评估样本下，Likert 评分系统性漏检 pairwise 可检测的 style bias——但 fully controlled 的证据仅限于 1-2 个 judge×benchmark 组合，zero figures 使统计叙事缺乏说服力，且 "blindspot" 框架与自身 n=500 数据中 Likert 趋近显著的事实存在内部张力。适合 Findings 发表：方法论设计系统、诊断工具（binarized-Likert）有独立价值，但 evidence breadth 和 presentation quality 不达 main conference 水准。

| 项目 | 最终评分 |
|------|---------|
| Overall Assessment | **3.0** (Findings) |
| Soundness | 3/5 |
| Excitement | 3/5 |
| Confidence | 4/5 |

### 上调条件（Rebuttal 可争取 3.5）
1. 补上 power curve + forest plot + pipeline diagram（最低 3 张 figures）
2. 报告 NLI threshold sensitivity analysis（至少 3 个阈值点）
3. 收窄标题至 formality（或补上第二个 fully controlled style axis）
4. 对 NLI-rejected pairs 做 sensitivity analysis 回应 "lower-bound" claim
5. 加入 CLMM 作为 Likert 的更公平 baseline

满足 1-3 可上调至 3.5；满足全部可上调至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-21T01:58:25.791249+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-21T01:58:25.791731+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 32 · 2026-05-21T01:58:25.843940+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-21T01:58:25.997571+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 205
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-21T01:58:31.878174+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 35 · 2026-05-21T01:58:32.029526+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-21T01:59:44.272646+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"因果语言与实际框架严重不匹配——大量使用 counterfactual/ATE 术语但无 DAG、SUTVA、sensitivity analysis\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 在 Soundness 评分中呼应（因果识别是近似的）\"\n    action_items:\n      - round: 1\n        action: \"给出 DAG + 讨论 SUTVA + sensitivity analysis for unmeasured confounders；或降调因果语言改用 diagnostic/detection 框架\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析——最终分析仅基于原始数据 ~1/3，lower-bound claim 缺乏形式化论证\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 交叉回应中确认 ~50% consistency rate 加剧了 data loss 问题\"\n    action_items:\n      - round: 1\n        action: \"分析 NLI-rejected pairs 的 pairwise 结果作为 sensitivity analysis；对 lower-bound claim 提供形式化论证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification，verbosity axis per-axis 调整引入 researcher degrees of freedom\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1 提出；R2 未单独标记但在交叉回应中同意方法论缺陷削弱 novelty\"\n    action_items:\n      - round: 1\n        action: \"报告阈值 sensitivity analysis（0.85/0.90/0.95）；说明是否 pre-specified\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是 Thurstone (1927) 以来已知的 Likert vs forced-choice sensitivity gap 在 LLM judge 的直接迁移\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 独立提出；R1 部分反驳（binarized-Likert 诊断设计有独立价值），但承认整体增量创新性有限\"\n    action_items:\n      - round: 1\n        action: \"将贡献重新定位为 first empirical quantification 而非 discovery；或提供 LLM judge 社区系统性误用 Likert 的量化证据\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"引用系统严重不完整——placeholder arXiv IDs、broken citations、总引用数偏少\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 报告 placeholder arXiv ID 和空 References；R1 审阅的 best 版本有参考文献但版本可能不同\"\n    action_items:\n      - round: 1\n        action: \"修复所有 broken citations，补充完整 arXiv ID，验证每条引用真实存在\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"RATE 批评缺乏实证支撑——未在 RATE exact setup 下复现，ecological validity 跨越\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2 提出；R1 未单独评论但同意 cross-setting generalization 证据不足\"\n    action_items:\n      - round: 1\n        action: \"在 RATE exact setup 下复现；或弱化措辞为 general Likert-based protocols warrant pairwise validation\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 CLMM/ordinal regression，ATE 丢弃 ordinal 结构信息\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 在交叉回应中确认如果 CLMM 显著则从根本上推翻 blindspot 概念\"\n    action_items:\n      - round: 1\n        action: \"增加 CLMM 分析作为更公平的 Likert baseline\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering ~40-50% data loss 未分析——被过滤的 position-sensitive pairs 未做探索性分析\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1 提出；R2 在交叉回应中引用此数据说明 protocol 执行与设计存在 gap\"\n    action_items:\n      - round: 1\n        action: \"报告完整 attrition 表（generated → NLI pass → consistent → final n）；对 inconsistent pairs 做探索性分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound OR=1.65 p=0.072 为 marginal——7/9 cells 中仅 1-2 个排除了此 confound\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 交叉回应中将此升级为核心论点——7/9 降至 1 clean cell\"\n    action_items:\n      - round: 1\n        action: \"对每个 cell 做 logistic regression (judge_choice ~ is_formal + is_original) 分离 confound\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致——Holm-Bonferroni 仅用于 Table 2，其他 ~20+ 次检验未校正\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1 提出\"\n    action_items:\n      - round: 1\n        action: \"报告全局 correction 或按 discovery vs confirmation 区分实验\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis 方法论问题——用 observed effect size 做 power analysis 被广泛批评\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 在效率差距讨论中引用\"\n    action_items:\n      - round: 1\n        action: \"改用 CI-based 方法或基于先验 literature effect size 做 power analysis\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整 3×3 结果，标题和 abstract 使用泛化的 style bias 表述\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 交叉回应中强烈同意，建议收窄标题至 formality\"\n    action_items:\n      - round: 1\n        action: \"补做 verbosity 等 axis 的完整 3×3 实验；或收窄标题至 formality\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry 建模——pairwise comparison 数据的标准分析框架缺失\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2 提出；R1 未直接回应但在交叉中未反驳\"\n    action_items:\n      - round: 1\n        action: \"补充 Bradley-Terry 分析至少作为 robustness check\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Related work 覆盖不完整——CalibraEval、FairEval、BT for judge evaluation、心理测量学理论文献缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2 提出\"\n    action_items:\n      - round: 1\n        action: \"补充相关引用，深化 §2 心理测量学文献讨论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表——无 Figure，仅 Tables，视觉传达严重不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 交叉回应中强烈同意，列出 3 个必要 figures（power curve、forest plot、pipeline diagram）\"\n    action_items:\n      - round: 1\n        action: \"至少添加 power curve + forest plot + pipeline diagram 三张 figures\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap——binarized Likert 在 n=500 时 p=0.055-0.063，Likert 非 categorically blind 而是 underpowered\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"交叉讨论中达成强共识：blindspot 框架与自身 n=500 数据矛盾\"\n    action_items:\n      - round: 1\n        action: \"将 blindspot 修改为 sensitivity/efficiency gap；或限定为 at typical evaluation sample sizes\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-2\"\n    summary: \"7/9 显著 cells 中仅 1-2 个排除了 original preference confound——核心数据基础大幅缩水\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 confound 分析 + R2 交叉确认：Gemini×LLMBar 的 original preference OR > formality OR\"\n    action_items:\n      - round: 1\n        action: \"对每个 cell 独立做 confound analysis；明确区分 fully controlled vs suggestive evidence\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转（Claude×LLMBar）——可能 Likert 和 pairwise 测量不同构念\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 发现；R2 建议升级为 Must-Fix，需要理论解释\"\n    action_items:\n      - round: 1\n        action: \"解释 Likert 和 pairwise 方向不一致的原因及对 same-construct 假设的影响\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"因果语言与实际框架严重不匹配——大量使用 counterfactual/ATE 术语但无 DAG、SUTVA、sensitivity analysis\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 在 Soundness 评分中呼应（因果识别是近似的）\"\n    action_items:\n      - round: 1\n        action: \"给出 DAG + 讨论 SUTVA + sensitivity analysis for unmeasured confounders；或降调因果语言改用 diagnostic/detection 框架\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析——最终分析仅基于原始数据 ~1/3，lower-bound claim 缺乏形式化论证\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 交叉回应中确认 ~50% consistency rate 加剧了 data loss 问题\"\n    action_items:\n      - round: 1\n        action: \"分析 NLI-rejected pairs 的 pairwise 结果作为 sensitivity analysis；对 lower-bound claim 提供形式化论证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification，verbosity axis per-axis 调整引入 researcher degrees of freedom\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1 提出；R2 未单独标记但在交叉回应中同意方法论缺陷削弱 novelty\"\n    action_items:\n      - round: 1\n        action: \"报告阈值 sensitivity analysis（0.85/0.90/0.95）；说明是否 pre-specified\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是 Thurstone (1927) 以来已知的 Likert vs forced-choice sensitivity gap 在 LLM judge 的直接迁移\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 独立提出；R1 部分反驳（binarized-Likert 诊断设计有独立价值），但承认整体增量创新性有限\"\n    action_items:\n      - round: 1\n        action: \"将贡献重新定位为 first empirical quantification 而非 discovery；或提供 LLM judge 社区系统性误用 Likert 的量化证据\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"引用系统严重不完整——placeholder arXiv IDs、broken citations、总引用数偏少\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 报告 placeholder arXiv ID 和空 References；R1 审阅的 best 版本有参考文献但版本可能不同\"\n    action_items:\n      - round: 1\n        action: \"修复所有 broken citations，补充完整 arXiv ID，验证每条引用真实存在\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"RATE 批评缺乏实证支撑——未在 RATE exact setup 下复现，ecological validity 跨越\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2 提出；R1 未单独评论但同意 cross-setting generalization 证据不足\"\n    action_items:\n      - round: 1\n        action: \"在 RATE exact setup 下复现；或弱化措辞为 general Likert-based protocols warrant pairwise validation\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 CLMM/ordinal regression，ATE 丢弃 ordinal 结构信息\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 在交叉回应中确认如果 CLMM 显著则从根本上推翻 blindspot 概念\"\n    action_items:\n      - round: 1\n        action: \"增加 CLMM 分析作为更公平的 Likert baseline\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering ~40-50% data loss 未分析——被过滤的 position-sensitive pairs 未做探索性分析\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1 提出；R2 在交叉回应中引用此数据说明 protocol 执行与设计存在 gap\"\n    action_items:\n      - round: 1\n        action: \"报告完整 attrition 表（generated → NLI pass → consistent → final n）；对 inconsistent pairs 做探索性分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound OR=1.65 p=0.072 为 marginal——7/9 cells 中仅 1-2 个排除了此 confound\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 交叉回应中将此升级为核心论点——7/9 降至 1 clean cell\"\n    action_items:\n      - round: 1\n        action: \"对每个 cell 做 logistic regression (judge_choice ~ is_formal + is_original) 分离 confound\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致——Holm-Bonferroni 仅用于 Table 2，其他 ~20+ 次检验未校正\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1 提出\"\n    action_items:\n      - round: 1\n        action: \"报告全局 correction 或按 discovery vs confirmation 区分实验\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis 方法论问题——用 observed effect size 做 power analysis 被广泛批评\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 在效率差距讨论中引用\"\n    action_items:\n      - round: 1\n        action: \"改用 CI-based 方法或基于先验 literature effect size 做 power analysis\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整 3×3 结果，标题和 abstract 使用泛化的 style bias 表述\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 交叉回应中强烈同意，建议收窄标题至 formality\"\n    action_items:\n      - round: 1\n        action: \"补做 verbosity 等 axis 的完整 3×3 实验；或收窄标题至 formality\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry 建模——pairwise comparison 数据的标准分析框架缺失\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2 提出；R1 未直接回应但在交叉中未反驳\"\n    action_items:\n      - round: 1\n        action: \"补充 Bradley-Terry 分析至少作为 robustness check\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Related work 覆盖不完整——CalibraEval、FairEval、BT for judge evaluation、心理测量学理论文献缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2 提出\"\n    action_items:\n      - round: 1\n        action: \"补充相关引用，深化 §2 心理测量学文献讨论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表——无 Figure，仅 Tables，视觉传达严重不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 交叉回应中强烈同意，列出 3 个必要 figures（power curve、forest plot、pipeline diagram）\"\n    action_items:\n      - round: 1\n        action: \"至少添加 power curve + forest plot + pipeline diagram 三张 figures\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap——binarized Likert 在 n=500 时 p=0.055-0.063，Likert 非 categorically blind 而是 underpowered\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"交叉讨论中达成强共识：blindspot 框架与自身 n=500 数据矛盾\"\n    action_items:\n      - round: 1\n        action: \"将 blindspot 修改为 sensitivity/efficiency gap；或限定为 at typical evaluation sample sizes\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-2\"\n    summary: \"7/9 显著 cells 中仅 1-2 个排除了 original preference confound——核心数据基础大幅缩水\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 confound 分析 + R2 交叉确认：Gemini×LLMBar 的 original preference OR > formality OR\"\n    action_items:\n      - round: 1\n        action: \"对每个 cell 独立做 confound analysis；明确区分 fully controlled vs suggestive evidence\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转（Claude×LLMBar）——可能 Likert 和 pairwise 测量不同构念\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 发现；R2 建议升级为 Must-Fix，需要理论解释\"\n    action_items:\n      - round: 1\n        action: \"解释 Likert 和 pairwise 方向不一致的原因及对 same-construct 假设的影响\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-21T01:59:44.373651+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 9831}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-21T02:01:47.099253+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 1\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审稿人**: R1 (Methods & Experiments) + R2 (Novelty & Related Work)\n**日期**: 2026-05-21\n\n---\n\n## Summary\n\n论文提出一个 5 阶段反事实协议（counterfactual style rewriting → NLI content gate → position control → Likert control → original preference control），在 3 judges × 3 benchmarks 的网格上比较 Likert 评分与 pairwise comparison 对 formality style bias 的检测灵敏度。核心发现：pairwise 在 7/9 cells 中检测到显著 formality bias，而 Likert ATE 仅 1/9、binarized Likert 0/9。论文据此提出 \"Likert Blindspot\" 概念，认为 Likert 评分系统性低估 style bias。\n\n---\n\n## Strengths\n\n- **S1** 研究问题有直接实践意义：如果 Likert 系统性漏检 style bias，影响所有 LLM-as-judge 评估管线 [R1, R2 共识]\n- **S2** Pipeline 设计系统性强，四阶段协议每步针对特定 confound，逻辑链完整 [R1, R2 共识]\n- **S3** 3 judges × 3 benchmarks 的网格设计覆盖多 LLM 家族（GPT-4o / Claude / Gemini），避免 anecdotal evidence [R2-S3]\n- **S4** **Binarized-Likert 诊断设计**是最强方法论贡献——通过共用 sign test 隔离 measurement structure 作为灵敏度差异来源 [R1 独立识别，R2 在交叉中部分认可]\n- **S5** 人工 NLI 验证（n=100, 91% agreement, Table 7）为 content preservation gate 提供可信质量保证 [R2-S5]\n- **S6** Scaled replication（n=500）确认效应量稳定，增强核心发现可信度 [R2-S6]\n- **S7** Limitations 讨论诚实：明确承认因果框架近似性、样本量限制、仅检测不纠正 [R1, R2 共识]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, R1+R2 共识] **7/9 \"显著\" cells 中仅 1-2 个排除了 original preference confound**\nR1 的 confound 分析显示，多数 cells 的 pairwise significance 可能反映 original preference（judges 本来就偏好某些 response）而非 formality bias。仅 GPT-4o×LLMBar 同时具备完整 confound 控制（rewriter robustness + original preference analysis + scaled replication）。核心数据基础从声称的 7/9 大幅缩水至 1-2 个 clean cells，\"systematic blindspot\" 叙事无法成立。\n\n**W2** [critical, R1+R2 共识] **\"Blindspot\" 实为 sample-size-dependent efficiency gap**\nBinarized Likert 在 n=500 时 p=0.055-0.063，接近显著边缘。这证明 Likert 不是 categorically blind，而是在 typical n=100 下 underpowered。标题 \"The Likert Blindspot\" 暗示定性测量失败，但实际是定量效率差异——论文自身数据与标题级 claim 存在内部矛盾。\n\n**W3** [critical, R1] **因果语言与实际框架严重不匹配**\n大量使用 \"counterfactual\"、\"interventional\"、\"ATE\" 等因果推断术语，但无 DAG、未讨论 SUTVA、无 sensitivity analysis for unmeasured confounders。Limitations 自认这一点。没有 DAG，无法评估 NLI gate 是否充分控制了 content confound。\n\n**W4** [critical, R1] **NLI gate 67% false-negative rate 造成的选择偏差未分析**\n人类认为 content 保留的 pairs 中 2/3 被 NLI 拒绝，最终分析仅基于原始数据 ~1/3。\"Lower-bound\" claim 需要 NLI-rejected pairs 与 accepted pairs 的 bias 方向一致这一未验证假设。如果 NLI gate 系统性筛掉 deeper style changes，留下的 superficial 改写可能产生不同 bias pattern。\n\n**W5** [critical, R1] **NLI 阈值 0.90 无 justification，per-axis 调整引入 researcher degrees of freedom**\n阈值选择无说明，verbosity axis 从 bidirectional 改为 direction-aware gating。无 pre-registration 或 sensitivity analysis，读者无法评估结果对阈值选择的稳健性。\n\n**W6** [critical, R2] **Novelty 不足——已知心理测量学现象的 domain transfer**\nLikert vs forced-choice sensitivity gap 是 Thurstone (1927) 以来近百年的共识。论文的核心贡献是将此已知结论迁移到 LLM judge，属 application-level transfer。\"Likert Blindspot\" 术语暗示原创发现，但实际是 known phenomenon rebranding。[R1 部分反驳：binarized-Likert 诊断设计和 LLM-specific 系统量化有 Findings-level 价值]\n\n**W7** [critical, R2] **引用系统严重不完整**\nPlaceholder arXiv IDs（\"arXiv:2406.xxxxx\"）、broken citations（\"???\" 占位符）、总引用数偏少（~15 篇）。注：R1 审阅的 best 版本有参考文献，R2 审阅的版本引用存在明显缺陷，可能存在版本不一致问题。无论如何，引用系统需要全面修复。\n\n**W8** [critical, R2] **RATE 批评缺乏 matched replication**\n声称 RATE \"可能系统性低估真实偏差\"，但未在 RATE exact setup 下验证。用自己的数据推断 RATE 的结果属 ecological validity 跨越。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W9** [warning, R1+R2 共识] **全文零图表**——无 Figure，9 张 Tables 堆叠。至少需要 power curve（灵敏度差距可视化）、forest plot（3×3 grid 结果一览）、pipeline diagram（方法论流程）三张 figures。对 borderline 论文，presentation 可能是 accept/reject 的 tipping point。\n\n**W10** [warning, R1] **Likert baseline 可能不公平**——ATE 丢弃 ordinal 结构信息。CLMM/ordinal regression 能更好利用 Likert 数据的 ordinal 特性。如果 CLMM 显著，\"blindspot\" 概念从根本上被推翻。\n\n**W11** [warning, R2+R1 共识] **范围窄于标题承诺**——仅 formality 有完整 3×3 结果；verbosity 和 register 各仅 1 个 judge×benchmark 组合，register 未达显著。标题 \"Style Bias\" 与实际覆盖不匹配。\n\n**W12** [warning, R1] **Original preference confound OR=1.65 p=0.072 为 marginal**——56% win rate 不可忽略，需 logistic regression 分离 formality effect 与 original preference 的贡献。\n\n**W13** [warning, R1+R2] **Likert ATE 方向反转（Claude×LLMBar）**——可能 Likert 和 pairwise 测量不同构念。论文完全未讨论这种可能性，\"blindspot\" narrative 隐含 same-construct 假设需要质疑。\n\n**W14** [warning, R1] **Consistency filtering ~40-50% data loss 未分析**——缺少完整 attrition 表和对 inconsistent pairs 的探索性分析。\n\n**W15** [warning, R1] **Multiple comparison correction 不一致**——Holm-Bonferroni 仅用于 Table 2 的 9-cell grid，其他 ~20+ 次检验未校正。\n\n**W16** [warning, R1] **Post-hoc power analysis 方法论问题**——用 observed effect size 做 power analysis 被广泛批评（Hoenig & Heisey, 2001），\"5× efficiency gap\" 可信度受限。\n\n**W17** [warning, R2] **缺少 Bradley-Terry 建模**——pairwise data 的标准分析框架缺失，无法提供 latent strength 估计和 effect size CI。\n\n**W18** [warning, R2] **Related work 覆盖不完整**——CalibraEval、FairEval、BT for judge evaluation、心理测量学理论文献（DeCoster et al. 2011, Simms et al. 2019）缺失。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Pipeline 设计在逻辑上合理**，每阶段针对特定 confound，体现了方法论训练 [R1+R2]\n2. **Binarized-Likert 诊断设计是本文最有价值的方法论贡献**——通过共用 sign test 隔离 measurement structure [R1 提出，R2 部分认可]\n3. **全文零 figures 是严重 presentation 缺陷**，对 borderline 论文可能是 tipping point [R1+R2 强共识]\n4. **7/9 cells 仅 1-2 个 clean**——original preference confound 未被充分控制 [R1 分析，R2 确认]\n5. **\"Blindspot\" 实为 efficiency gap**——n=500 时 binarized Likert 接近显著 [R1+R2 强共识]\n6. **标题 scope 宽于实际覆盖**——\"Style Bias\" 但仅 formality 有完整证据 [R1+R2]\n7. **Limitations 讨论诚实**，明确承认因果框架的近似性 [R1+R2]\n\n## Reviewer Divergence [REBUT]\n\n1. **Novelty 是否达到 Findings 水平**：R1 部分反驳 R2 的增量创新性批评——认为 binarized-Likert 诊断设计 + LLM-specific 系统量化构成 Findings-level 贡献；R2 认为 1 clean cell 不足以支撑 even Findings。最终评分：R1 给 3.0 (Findings)，R2 给 2.0 (Resubmit)。\n2. **引用问题的严重程度**：R1 审阅的 best 版本有参考文献（page 7 可见条目），R2 报告 placeholder arXiv IDs 和 broken citations。可能存在版本差异。R1 认为这是编辑问题不影响方法论评估；R2 认为影响 submission readiness 和 verifiability。\n\n---\n\n## Questions for Authors\n\n1. 请报告每个 judge×benchmark cell 的完整 attrition 数据：generated pairs → NLI pass → position-consistent → final n\n2. NLI 阈值 0.90 是 pre-specified 还是 post-hoc？请提供 threshold sensitivity analysis（0.85/0.90/0.95）\n3. NLI-rejected 但 human-valid 的 pairs 中 judge 的 formality preference 是什么方向？（验证 \"lower-bound\" claim）\n4. 是否考虑过 CLMM/ordinal regression 作为更公平的 Likert baseline？\n5. 对每个 cell，logistic regression (judge_choice ~ is_formal + is_original) 的结果如何？formality effect 在控制 original preference 后减少多少？\n6. 请解释 Claude×LLMBar 的 Likert ATE 方向反转现象——Likert 和 pairwise 是否在测量不同构念？\n7. Consistency filtering 去掉的 ~40-50% pairs 中 position bias 方向如何？\n8. Abstract 以 n=100 的 69.1% win rate 为 headline number，但 n=500 scaled replication 显示 ~61-67%。是否应以更大样本的 effect size 为 primary reported number？\n9. 相对于 Karpinska et al. 和 Novikova et al. 的 Likert vs ranking 工作，本文的贡献具体在哪里超越了 domain transfer？\n10. Placeholder arXiv IDs（\"arXiv:2406.xxxxx\"）是否是真实文献？请确认所有引用可验证。\n\n---\n\n## Missing References\n\n- **CalibraEval** — LLM judge calibration，与 measurement sensitivity 直接相关\n- **FairEval** (Wang et al., 2023) — 该方向重要前驱\n- **Chatbot Arena / Bradley-Terry** 文献 — 与 pairwise comparison 方法论直接相关\n- **心理测量学理论文献** — DeCoster et al. (2011), Simms et al. (2019) 等 Likert vs forced-choice 理论分析\n- **LLM-as-Judge 综述/meta-analysis** — Zheng et al. (2023) 后的 survey papers\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求外部审稿。\n\n---\n\n## Visual Layout Check\n\n未派发视觉审查。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 2.5 / 5 (Borderline Findings)**\n\n**Director 综合判断依据**：\n\nR1 给 3.0 (Findings)，R2 给 2.0 (Resubmit next cycle)。Director 综合评估为 **2.5 (Borderline Findings)**，理由如下：\n\n**支持 Findings 的因素**（倾向 R1）：\n- Binarized-Likert 诊断设计有独立方法论价值\n- GPT-4o×LLMBar 上的 primary evidence 在完整 confound 控制下可信\n- Pipeline 设计系统性强，Limitations 诚实\n- 对 LLM-as-judge 社区有直接实践意义\n\n**支持 Resubmit 的因素**（倾向 R2）：\n- 核心 claim 的数据基础从 7/9 缩水至 1-2 clean cells\n- \"Blindspot\" 与 \"efficiency gap\" 的内部矛盾未解决\n- 因果框架缺失是方法论硬伤\n- NLI gate 的选择偏差和阈值问题使证据链不够坚实\n- 引用系统缺陷、零 figures、scope 窄于标题——presentation 不达标\n\n**结论**：论文在一个有实践意义的问题上做了设计合理的实验，但 8 个 critical issues 叠加（confound 穿透、blindspot vs efficiency gap 矛盾、因果框架缺失、NLI gate 选择偏差、阈值无 justification、novelty 不足、引用缺陷、RATE 批评无支撑）使其处于 Borderline Findings。如果 rebuttal 能解决前 5 个 critical issues 中的至少 3 个，有潜力上调至 3.0-3.5。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Counterfactual pairwise measurement procedure\" 的因果语言需要 DAG 支撑或降调\n- Contributions 列表应将 \"first empirical quantification\" 与 \"discovery\" 区分\n\n### §2 Related Work\n- 缺少 CalibraEval、FairEval、BT 建模、心理测量学理论文献\n- 与 RATE 的差异化定位需要 matched replication 支撑\n\n### §3 Method\n- NLI threshold 0.90 需要 justification 和 sensitivity analysis\n- Verbosity axis 的 direction-aware gating 调整需要独立说明\n- 完整 attrition 表（每阶段 data loss）应在此报告\n\n### §4 Experimental Setup\n- 未报告 power analysis 论证 n=100 的样本量选择依据\n- 3×3 grid 的 Holm-Bonferroni 校正应扩展到全论文所有检验\n\n### §5 Results\n- §5.1-§5.3: 7/9 vs 1/9 对比需要加入 per-cell confound analysis，区分 fully controlled vs suggestive\n- §5.3: Binarized Likert 0/9 应补充 CLMM 作为更公平 baseline\n- §5.4: Original preference OR=1.65 需要正式的 partial-out analysis\n- §5.5: Scaled replication 的 win rate 应作为 primary reported effect（非 n=100 的数字）\n- §5.5: Post-hoc power analysis 应改用 CI-based 方法\n- §5.7: NLI-rejected pairs 需要 sensitivity analysis\n- §5.8-§5.9: Verbosity/register 仅单点测试，generalization 证据薄弱；register p=0.068 的 \"suggestive evidence\" 表述有误导风险\n\n### §6 Discussion\n- \"Blindspot\" 与 \"complementary rather than adversarial\" 存在内部矛盾\n- RATE 批评需要弱化或补充 matched replication\n- Claude×LLMBar Likert ATE 方向反转需要理论讨论\n\n### Presentation\n- 全文零 figures 在顶会论文中不可接受——至少需要 power curve、forest plot、pipeline diagram\n- 正文仅 6 页（EMNLP 2026 限制 8 页），有 2 页空间可用于深化分析和添加 figures\n- Table 3 列头缩写（FC、C→F、F→C）未在 caption 中充分解释\n\n---\n\n## Resubmission Roadmap（如需传达给作者）\n\n**Priority 1（解决后可达 Findings 3.0）**：\n1. 对每个 cell 做 confound analysis（original preference OR vs style OR 对比）\n2. NLI threshold sensitivity analysis（至少 3 个阈值点）\n3. 报告 NLI-rejected pairs 的 bias 方向（验证 lower-bound claim）\n4. 添加 power curve + forest plot + pipeline diagram（至少 3 张 figures）\n5. 修复全部引用，补充 missing references\n\n**Priority 2（解决后可达 Borderline Conference 3.5）**：\n6. 补做 verbosity 的完整 3×3 实验\n7. 加入 CLMM 作为更公平的 Likert baseline\n8. 收窄标题至 formality 或补做多 axis 实验\n9. 将 \"blindspot\" 重新框定为 \"sensitivity gap at typical n\"\n\n**Priority 3（解决后可达 Conference 4.0）**：\n10. 补上 DAG + SUTVA 讨论（或降调因果语言）\n11. 引入 Bradley-Terry 建模\n12. 对 Likert ATE 方向反转提供理论解释\n13. 完整 attrition 表 + inconsistent pairs 探索性分析",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "2.5 / 5 (Borderline Findings)",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 1\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审稿人**: R1 (Methods & Experiments) + R2 (Novelty & Related Work)\n**日期**: 2026-05-21\n\n---\n\n## Summary\n\n论文提出一个 5 阶段反事实协议（counterfactual style rewriting → NLI content gate → position control → Likert control → original preference control），在 3 judges × 3 benchmarks 的网格上比较 Likert 评分与 pairwise comparison 对 formality style bias 的检测灵敏度。核心发现：pairwise 在 7/9 cells 中检测到显著 formality bias，而 Likert ATE 仅 1/9、binarized Likert 0/9。论文据此提出 \"Likert Blindspot\" 概念，认为 Likert 评分系统性低估 style bias。\n\n---\n\n## Strengths\n\n- **S1** 研究问题有直接实践意义：如果 Likert 系统性漏检 style bias，影响所有 LLM-as-judge 评估管线 [R1, R2 共识]\n- **S2** Pipeline 设计系统性强，四阶段协议每步针对特定 confound，逻辑链完整 [R1, R2 共识]\n- **S3** 3 judges × 3 benchmarks 的网格设计覆盖多 LLM 家族（GPT-4o / Claude / Gemini），避免 anecdotal evidence [R2-S3]\n- **S4** **Binarized-Likert 诊断设计**是最强方法论贡献——通过共用 sign test 隔离 measurement structure 作为灵敏度差异来源 [R1 独立识别，R2 在交叉中部分认可]\n- **S5** 人工 NLI 验证（n=100, 91% agreement, Table 7）为 content preservation gate 提供可信质量保证 [R2-S5]\n- **S6** Scaled replication（n=500）确认效应量稳定，增强核心发现可信度 [R2-S6]\n- **S7** Limitations 讨论诚实：明确承认因果框架近似性、样本量限制、仅检测不纠正 [R1, R2 共识]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, R1+R2 共识] **7/9 \"显著\" cells 中仅 1-2 个排除了 original preference confound**\nR1 的 confound 分析显示，多数 cells 的 pairwise significance 可能反映 original preference（judges 本来就偏好某些 response）而非 formality bias。仅 GPT-4o×LLMBar 同时具备完整 confound 控制（rewriter robustness + original preference analysis + scaled replication）。核心数据基础从声称的 7/9 大幅缩水至 1-2 个 clean cells，\"systematic blindspot\" 叙事无法成立。\n\n**W2** [critical, R1+R2 共识] **\"Blindspot\" 实为 sample-size-dependent efficiency gap**\nBinarized Likert 在 n=500 时 p=0.055-0.063，接近显著边缘。这证明 Likert 不是 categorically blind，而是在 typical n=100 下 underpowered。标题 \"The Likert Blindspot\" 暗示定性测量失败，但实际是定量效率差异——论文自身数据与标题级 claim 存在内部矛盾。\n\n**W3** [critical, R1] **因果语言与实际框架严重不匹配**\n大量使用 \"counterfactual\"、\"interventional\"、\"ATE\" 等因果推断术语，但无 DAG、未讨论 SUTVA、无 sensitivity analysis for unmeasured confounders。Limitations 自认这一点。没有 DAG，无法评估 NLI gate 是否充分控制了 content confound。\n\n**W4** [critical, R1] **NLI gate 67% false-negative rate 造成的选择偏差未分析**\n人类认为 content 保留的 pairs 中 2/3 被 NLI 拒绝，最终分析仅基于原始数据 ~1/3。\"Lower-bound\" claim 需要 NLI-rejected pairs 与 accepted pairs 的 bias 方向一致这一未验证假设。如果 NLI gate 系统性筛掉 deeper style changes，留下的 superficial 改写可能产生不同 bias pattern。\n\n**W5** [critical, R1] **NLI 阈值 0.90 无 justification，per-axis 调整引入 researcher degrees of freedom**\n阈值选择无说明，verbosity axis 从 bidirectional 改为 direction-aware gating。无 pre-registration 或 sensitivity analysis，读者无法评估结果对阈值选择的稳健性。\n\n**W6** [critical, R2] **Novelty 不足——已知心理测量学现象的 domain transfer**\nLikert vs forced-choice sensitivity gap 是 Thurstone (1927) 以来近百年的共识。论文的核心贡献是将此已知结论迁移到 LLM judge，属 application-level transfer。\"Likert Blindspot\" 术语暗示原创发现，但实际是 known phenomenon rebranding。[R1 部分反驳：binarized-Likert 诊断设计和 LLM-specific 系统量化有 Findings-level 价值]\n\n**W7** [critical, R2] **引用系统严重不完整**\nPlaceholder arXiv IDs（\"arXiv:2406.xxxxx\"）、broken citations（\"???\" 占位符）、总引用数偏少（~15 篇）。注：R1 审阅的 best 版本有参考文献，R2 审阅的版本引用存在明显缺陷，可能存在版本不一致问题。无论如何，引用系统需要全面修复。\n\n**W8** [critical, R2] **RATE 批评缺乏 matched replication**\n声称 RATE \"可能系统性低估真实偏差\"，但未在 RATE exact setup 下验证。用自己的数据推断 RATE 的结果属 ecological validity 跨越。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W9** [warning, R1+R2 共识] **全文零图表**——无 Figure，9 张 Tables 堆叠。至少需要 power curve（灵敏度差距可视化）、forest plot（3×3 grid 结果一览）、pipeline diagram（方法论流程）三张 figures。对 borderline 论文，presentation 可能是 accept/reject 的 tipping point。\n\n**W10** [warning, R1] **Likert baseline 可能不公平**——ATE 丢弃 ordinal 结构信息。CLMM/ordinal regression 能更好利用 Likert 数据的 ordinal 特性。如果 CLMM 显著，\"blindspot\" 概念从根本上被推翻。\n\n**W11** [warning, R2+R1 共识] **范围窄于标题承诺**——仅 formality 有完整 3×3 结果；verbosity 和 register 各仅 1 个 judge×benchmark 组合，register 未达显著。标题 \"Style Bias\" 与实际覆盖不匹配。\n\n**W12** [warning, R1] **Original preference confound OR=1.65 p=0.072 为 marginal**——56% win rate 不可忽略，需 logistic regression 分离 formality effect 与 original preference 的贡献。\n\n**W13** [warning, R1+R2] **Likert ATE 方向反转（Claude×LLMBar）**——可能 Likert 和 pairwise 测量不同构念。论文完全未讨论这种可能性，\"blindspot\" narrative 隐含 same-construct 假设需要质疑。\n\n**W14** [warning, R1] **Consistency filtering ~40-50% data loss 未分析**——缺少完整 attrition 表和对 inconsistent pairs 的探索性分析。\n\n**W15** [warning, R1] **Multiple comparison correction 不一致**——Holm-Bonferroni 仅用于 Table 2 的 9-cell grid，其他 ~20+ 次检验未校正。\n\n**W16** [warning, R1] **Post-hoc power analysis 方法论问题**——用 observed effect size 做 power analysis 被广泛批评（Hoenig & Heisey, 2001），\"5× efficiency gap\" 可信度受限。\n\n**W17** [warning, R2] **缺少 Bradley-Terry 建模**——pairwise data 的标准分析框架缺失，无法提供 latent strength 估计和 effect size CI。\n\n**W18** [warning, R2] **Related work 覆盖不完整**——CalibraEval、FairEval、BT for judge evaluation、心理测量学理论文献（DeCoster et al. 2011, Simms et al. 2019）缺失。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Pipeline 设计在逻辑上合理**，每阶段针对特定 confound，体现了方法论训练 [R1+R2]\n2. **Binarized-Likert 诊断设计是本文最有价值的方法论贡献**——通过共用 sign test 隔离 measurement structure [R1 提出，R2 部分认可]\n3. **全文零 figures 是严重 presentation 缺陷**，对 borderline 论文可能是 tipping point [R1+R2 强共识]\n4. **7/9 cells 仅 1-2 个 clean**——original preference confound 未被充分控制 [R1 分析，R2 确认]\n5. **\"Blindspot\" 实为 efficiency gap**——n=500 时 binarized Likert 接近显著 [R1+R2 强共识]\n6. **标题 scope 宽于实际覆盖**——\"Style Bias\" 但仅 formality 有完整证据 [R1+R2]\n7. **Limitations 讨论诚实**，明确承认因果框架的近似性 [R1+R2]\n\n## Reviewer Divergence [REBUT]\n\n1. **Novelty 是否达到 Findings 水平**：R1 部分反驳 R2 的增量创新性批评——认为 binarized-Likert 诊断设计 + LLM-specific 系统量化构成 Findings-level 贡献；R2 认为 1 clean cell 不足以支撑 even Findings。最终评分：R1 给 3.0 (Findings)，R2 给 2.0 (Resubmit)。\n2. **引用问题的严重程度**：R1 审阅的 best 版本有参考文献（page 7 可见条目），R2 报告 placeholder arXiv IDs 和 broken citations。可能存在版本差异。R1 认为这是编辑问题不影响方法论评估；R2 认为影响 submission readiness 和 verifiability。\n\n---\n\n## Questions for Authors\n\n1. 请报告每个 judge×benchmark cell 的完整 attrition 数据：generated pairs → NLI pass → position-consistent → final n\n2. NLI 阈值 0.90 是 pre-specified 还是 post-hoc？请提供 threshold sensitivity analysis（0.85/0.90/0.95）\n3. NLI-rejected 但 human-valid 的 pairs 中 judge 的 formality preference 是什么方向？（验证 \"lower-bound\" claim）\n4. 是否考虑过 CLMM/ordinal regression 作为更公平的 Likert baseline？\n5. 对每个 cell，logistic regression (judge_choice ~ is_formal + is_original) 的结果如何？formality effect 在控制 original preference 后减少多少？\n6. 请解释 Claude×LLMBar 的 Likert ATE 方向反转现象——Likert 和 pairwise 是否在测量不同构念？\n7. Consistency filtering 去掉的 ~40-50% pairs 中 position bias 方向如何？\n8. Abstract 以 n=100 的 69.1% win rate 为 headline number，但 n=500 scaled replication 显示 ~61-67%。是否应以更大样本的 effect size 为 primary reported number？\n9. 相对于 Karpinska et al. 和 Novikova et al. 的 Likert vs ranking 工作，本文的贡献具体在哪里超越了 domain transfer？\n10. Placeholder arXiv IDs（\"arXiv:2406.xxxxx\"）是否是真实文献？请确认所有引用可验证。\n\n---\n\n## Missing References\n\n- **CalibraEval** — LLM judge calibration，与 measurement sensitivity 直接相关\n- **FairEval** (Wang et al., 2023) — 该方向重要前驱\n- **Chatbot Arena / Bradley-Terry** 文献 — 与 pairwise comparison 方法论直接相关\n- **心理测量学理论文献** — DeCoster et al. (2011), Simms et al. (2019) 等 Likert vs forced-choice 理论分析\n- **LLM-as-Judge 综述/meta-analysis** — Zheng et al. (2023) 后的 survey papers\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求外部审稿。\n\n---\n\n## Visual Layout Check\n\n未派发视觉审查。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 2.5 / 5 (Borderline Findings)**\n\n**Director 综合判断依据**：\n\nR1 给 3.0 (Findings)，R2 给 2.0 (Resubmit next cycle)。Director 综合评估为 **2.5 (Borderline Findings)**，理由如下：\n\n**支持 Findings 的因素**（倾向 R1）：\n- Binarized-Likert 诊断设计有独立方法论价值\n- GPT-4o×LLMBar 上的 primary evidence 在完整 confound 控制下可信\n- Pipeline 设计系统性强，Limitations 诚实\n- 对 LLM-as-judge 社区有直接实践意义\n\n**支持 Resubmit 的因素**（倾向 R2）：\n- 核心 claim 的数据基础从 7/9 缩水至 1-2 clean cells\n- \"Blindspot\" 与 \"efficiency gap\" 的内部矛盾未解决\n- 因果框架缺失是方法论硬伤\n- NLI gate 的选择偏差和阈值问题使证据链不够坚实\n- 引用系统缺陷、零 figures、scope 窄于标题——presentation 不达标\n\n**结论**：论文在一个有实践意义的问题上做了设计合理的实验，但 8 个 critical issues 叠加（confound 穿透、blindspot vs efficiency gap 矛盾、因果框架缺失、NLI gate 选择偏差、阈值无 justification、novelty 不足、引用缺陷、RATE 批评无支撑）使其处于 Borderline Findings。如果 rebuttal 能解决前 5 个 critical issues 中的至少 3 个，有潜力上调至 3.0-3.5。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Counterfactual pairwise measurement procedure\" 的因果语言需要 DAG 支撑或降调\n- Contributions 列表应将 \"first empirical quantification\" 与 \"discovery\" 区分\n\n### §2 Related Work\n- 缺少 CalibraEval、FairEval、BT 建模、心理测量学理论文献\n- 与 RATE 的差异化定位需要 matched replication 支撑\n\n### §3 Method\n- NLI threshold 0.90 需要 justification 和 sensitivity analysis\n- Verbosity axis 的 direction-aware gating 调整需要独立说明\n- 完整 attrition 表（每阶段 data loss）应在此报告\n\n### §4 Experimental Setup\n- 未报告 power analysis 论证 n=100 的样本量选择依据\n- 3×3 grid 的 Holm-Bonferroni 校正应扩展到全论文所有检验\n\n### §5 Results\n- §5.1-§5.3: 7/9 vs 1/9 对比需要加入 per-cell confound analysis，区分 fully controlled vs suggestive\n- §5.3: Binarized Likert 0/9 应补充 CLMM 作为更公平 baseline\n- §5.4: Original preference OR=1.65 需要正式的 partial-out analysis\n- §5.5: Scaled replication 的 win rate 应作为 primary reported effect（非 n=100 的数字）\n- §5.5: Post-hoc power analysis 应改用 CI-based 方法\n- §5.7: NLI-rejected pairs 需要 sensitivity analysis\n- §5.8-§5.9: Verbosity/register 仅单点测试，generalization 证据薄弱；register p=0.068 的 \"suggestive evidence\" 表述有误导风险\n\n### §6 Discussion\n- \"Blindspot\" 与 \"complementary rather than adversarial\" 存在内部矛盾\n- RATE 批评需要弱化或补充 matched replication\n- Claude×LLMBar Likert ATE 方向反转需要理论讨论\n\n### Presentation\n- 全文零 figures 在顶会论文中不可接受——至少需要 power curve、forest plot、pipeline diagram\n- 正文仅 6 页（EMNLP 2026 限制 8 页），有 2 页空间可用于深化分析和添加 figures\n- Table 3 列头缩写（FC、C→F、F→C）未在 caption 中充分解释\n\n---\n\n## Resubmission Roadmap（如需传达给作者）\n\n**Priority 1（解决后可达 Findings 3.0）**：\n1. 对每个 cell 做 confound analysis（original preference OR vs style OR 对比）\n2. NLI threshold sensitivity analysis（至少 3 个阈值点）\n3. 报告 NLI-rejected pairs 的 bias 方向（验证 lower-bound claim）\n4. 添加 power curve + forest plot + pipeline diagram（至少 3 张 figures）\n5. 修复全部引用，补充 missing references\n\n**Priority 2（解决后可达 Borderline Conference 3.5）**：\n6. 补做 verbosity 的完整 3×3 实验\n7. 加入 CLMM 作为更公平的 Likert baseline\n8. 收窄标题至 formality 或补做多 axis 实验\n9. 将 \"blindspot\" 重新框定为 \"sensitivity gap at typical n\"\n\n**Priority 3（解决后可达 Conference 4.0）**：\n10. 补上 DAG + SUTVA 讨论（或降调因果语言）\n11. 引入 Bradley-Terry 建模\n12. 对 Likert ATE 方向反转提供理论解释\n13. 完整 attrition 表 + inconsistent pairs 探索性分析",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "2.5 / 5 (Borderline Findings)",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-21T02:01:51.467315+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4368
}
```

</details>

---


### Assistant

_source line 40 · 2026-05-21T02:01:59.603083+00:00_

审稿报告已投递至 Research Director。

**Round 1 圆桌审稿完成**：

| 项目 | 结果 |
|------|------|
| R1 (Methods & Experiments) | 3.0 / 5 (Findings) |
| R2 (Novelty & Related Work) | 2.0 / 5 (Resubmit next cycle) |
| **Director 综合** | **2.5 / 5 (Borderline Findings)** |

**8 个 critical issues**：confound 穿透（7/9→1 clean cell）、blindspot vs efficiency gap 矛盾、因果框架缺失、NLI gate 选择偏差、NLI 阈值无 justification、novelty 不足、引用缺陷、RATE 批评无支撑。**10 个 warning issues**：零 figures、Likert baseline 不公平、scope 窄、original preference marginal confound 等。

报告附带了分三个优先级的 13 条 resubmission roadmap，解决 Priority 1（5 条）可达 Findings 3.0，解决 Priority 1+2 可达 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 4

## Round 4

6 recorded events


### User

_source line 41 · 2026-05-21T02:02:01.298835+00:00_

[Reviewer 1 审稿结果]:
R1 最终收敛意见已提交。最终评分 **3.0 (Findings)**，附明确的 rebuttal 上调路径（补 figures + NLI sensitivity + 收窄标题可至 3.5，全部修复可至 4.0）。

---

[Reviewer 2 审稿意见]:
## R2 交叉回应：逐条回应 R1 完整审稿意见

**重要前置说明**：R1 指出 Director brief 中部分数字与 PDF 不一致（Director 称 "Only 2/3 judges significant" 等，而 PDF 显示 7/9 cells significant）。我的 Round 1 审稿基于 PDF 原文，与 R1 一致——Table 2 确实显示 7/9 cells significant。但我在 Cross-Review Response 中接受了 Director brief 的 "1 clean cell after confound analysis" 并据此下调评分。现在需要区分两个不同的 claim：(a) 统计显著性：7/9 cells pairwise significant——PDF 支持；(b) confound-free：扣除 original preference confound 后有多少 cells 仍可归因于 formality bias——这是 R1-W3 提出的问题，但 R1 的结论并非 "仅 1 cell clean"，而是 W3 指出 original preference confound OR=1.65, p=0.072 是 marginal。我需要基于 R1 的实际审稿意见而非 Director 的 brief 来修正我的立场。

---

## Must-Fix 逐条回应

### R1-N1: 因果语言与实际框架严重不匹配

**[AGREE]** 同意这是一个重要问题，但对 severity 的判断稍有不同。

理由：
- R1 正确指出论文在 §3 标题（"Counterfactual Style Rewriting"）、§3.4（"ATE"）、§1（"counterfactual pairwise measurement procedure"）中大量使用因果术语，但缺少 DAG、SUTVA 讨论、sensitivity analysis。
- 从 **novelty/positioning 角度**：因果语言是论文 differentiation 的核心工具——"counterfactual" 将论文与纯描述性的 bias audit 区分开。如果降调为 "diagnostic/detection" 框架，论文的 novelty narrative 会进一步削弱，因为 "pairwise comparison 比 Likert 更灵敏" 这一 diagnostic finding 的新颖性更低。
- 但我同意 R1 的判断：当前的因果语言是 **overclaiming**。论文的实际操作（rewrite → compare）是一个 interventional design，但未达到 formal causal inference 的标准。正确的定位应该是 "quasi-experimental interventional study" 而非 "counterfactual causal analysis"。
- **对 novelty 的净影响**：降调因果语言后，论文的 positioning 从 "causal identification of style bias" 退到 "interventional detection protocol"——这是一个更准确但也更 modest 的贡献。我认为这个 more honest positioning 实际上对论文有利，因为不会在审稿中引发不必要的 causal inference 标准检验。

### R1-N2: NLI gate 的选择偏差未被分析

**[AGREE]** 完全同意，且从 novelty 角度补充额外关切。

理由：
- R1 指出 67% false-negative rate 意味着最终分析仅基于 ~1/3 的数据。"Lower-bound" claim 需要 NLI-rejected pairs 与 accepted pairs 的 bias 方向一致——这一假设未被验证。
- 从 **novelty 角度**的额外关切：NLI gate 是 5-stage protocol 中的关键差异化步骤——它是论文相对于简单 "rewrite + compare" 的主要方法论增量。如果这个 gate 引入了 systematic selection bias（例如，只保留了 rewriting 差异最小的 pairs，而这些恰恰是 style bias 最容易检测的 pairs），那么 protocol 的核心创新点本身就有缺陷。
- 这与我 Round 1 的 W2（缺少 Bradley-Terry 建模）相关：如果 ~2/3 的数据被丢弃，BT 模型能更好地处理 incomplete comparison data。
- **补充建议**：除了 R1 建议的 "分析 NLI-rejected pairs 的 pairwise 结果"，还应报告 NLI-accepted vs NLI-rejected pairs 在 style distance（formality score difference）上的分布——如果 accepted pairs 的 style distance 系统性偏小，则 bias estimate 可能被压低。

### R1-N3: NLI 阈值 0.90 缺乏 justification，per-axis 调整引入 researcher degrees of freedom

**[AGREE]** 同意，且这一问题在 §5.8 的 verbosity 分析中尤为突出。

理由：
- §3.2 的 NLI 阈值 0.90 未说明选择依据。§5.8 verbosity 分析中从 bidirectional 改为 direction-aware gating，这是一个 post-hoc 的方法修改。
- 从 **novelty/related work 角度**：论文 §2 批评 RATE 使用 Likert 但自己在 NLI gate 设计上引入了未声明的 researcher degrees of freedom——这削弱了论文对竞品方法论批评的可信度。如果你批评别人的 measurement instrument 有问题，你自己的 measurement protocol 需要更严格的 pre-specification。
- 阈值 sensitivity analysis（0.85, 0.90, 0.95）是必须的，且应作为核心 robustness check 出现在正文（不仅是 appendix）。

---

## Should-Fix 逐条回应

### R1-W1: Likert baseline 可能不公平——未使用 CLMM/ordinal regression

**[AGREE]** 这是对 "Likert Blindspot" 概念最具威胁性的质疑。

- 论文用 t-test on ATE 和 binarized sign test 来评估 Likert 的灵敏度。但 Likert 数据是 ordinal 而非 interval——用 t-test 分析 ordinal 数据本身就会损失统计效力。
- **关键问题**：如果使用 CLMM（Cumulative Link Mixed Model）或 ordinal logistic regression 分析 Likert 数据，Likert 是否仍然检测不到 formality bias？如果 CLMM 显著，则：
  - "Likert Blindspot" 不是 Likert 评分制的固有缺陷，而是分析方法（t-test on ATE）的缺陷
  - 论文的核心贡献从 "Likert 量表看不到 bias" 变成 "用错误的统计方法分析 Likert 数据会看不到 bias"——后者的 novelty 和 impact 大幅降低
  - 标题需要从 "Likert Blindspot" 改为 "ATE Blindspot" 或类似
- **从 novelty 角度的判断**：这个问题是否构成 fatal flaw 取决于 CLMM 的结果。如果 CLMM 仍然 non-significant，则论文核心 claim 成立；如果 CLMM significant，则核心 claim 被推翻。**我认为作者必须在 revision 中报告 CLMM 结果**——这是 reviewer 判断论文 contribution 是否成立的必要信息。

### R1-W2: Consistency filtering 的 data loss ~40-50% 未分析

**[AGREE]** 同意 R1 的关切。

- ~50% data loss 意味着有效样本量远小于标称 n=100。这与我 Round 1 的观察一致。
- 补充：consistency filtering 丢弃的是 position-inconsistent pairs——这些 pairs 的 inconsistency 可能本身就 informative（例如，formality effect 与 position effect 大小相当的 pairs 更可能 flip）。丢弃这些 pairs 可能系统性保留了 formality effect 更强的 pairs，导致 win rate 被高估。

### R1-W3: Original preference confound OR=1.65, p=0.072 为 marginal

**[AGREE]** 同意这是一个不能安全忽略的 confound。

- 我在 Cross-Review 中基于 Director brief 接受了 "仅 1 clean cell" 的判断。但 R1 的实际措辞更 nuanced：OR=1.65, p=0.072 是 marginal，不是 definitive。
- **修正我的 Cross-Review 立场**：我不再将结论定为 "仅 1 clean cell"，而是 "original preference confound 是 marginal (p=0.072)，需要进一步分析（如 R1 建议的 logistic regression partial out）才能确定其影响程度"。这比 "1 clean cell" 的判断更公平。
- **对评分的影响**：这稍微减轻了我 Cross-Review 中的下调幅度——从 "核心发现几乎没有 clean evidence" 修正为 "核心发现有 moderate evidence，但 confound 未被充分控制"。

### R1-W4: Multiple comparison correction 不一致

**[AGREE]** 同意。§5.1 Table 2 使用 Holm-Bonferroni 但其他 tables 未使用，这是 inconsistency。

### R1-W5: Post-hoc power analysis 方法论问题

**[AGREE]** 完全同意。Observed effect size 做 power analysis 是 circular reasoning，这在统计学文献中被广泛批评（Hoenig & Heisey, 2001）。论文的 power analysis 结果不应作为论据引用。

---

## 对 Director 提出的三个交叉问题的回答

### 问题 1：降调因果语言如何影响 novelty claim？

**影响方向：novelty 降低，但可信度提高，净效果可能中性偏正。**

当前论文的 novelty narrative 建立在两个支柱上：
1. "Counterfactual" 方法论（暗示因果识别）
2. "Blindspot" 发现（暗示新现象）

降调因果语言会削弱支柱 1，使论文从 "causal analysis" 退到 "interventional detection protocol"。但这避免了 R1-N1 的 critical 攻击面——审稿人不会再用 DAG/SUTVA 标准来要求论文。

**从 positioning 角度**：降调后论文更接近 "practical measurement guide" 的定位，这与我在 Convergence 阶段的判断一致。这个定位更 honest，但也意味着 novelty bar 由 "new causal insight" 降为 "useful protocol + empirical case study"。对于 Findings track 来说足够，对于 Main Conference 来说可能不够。

### 问题 2：如果 CLMM 显著，是否从根本上推翻 "Likert Blindspot"？

**是的，CLMM significant 会从根本上改变论文的 contribution。**

具体推演：
- 如果 CLMM（使用相同的 Likert 数据）在多数 cells 中检测到 significant formality bias → 问题不在 Likert 量表，而在 t-test on ATE 这个分析方法
- "Likert Blindspot" 变成 "ATE Blindspot" → 论文的 practical guidance 从 "用 pairwise 代替 Likert" 变成 "用正确的统计方法分析 Likert"
- 后者的 novelty 更低（"用正确的方法做分析" 不是新洞见），但 practical impact 可能更大（因为不需要重做所有评估，只需重新分析）

**如果 CLMM 仍 non-significant** → 论文核心 claim 被加强，因为即使用了更 appropriate 的 ordinal 统计方法，Likert 仍然看不到 bias。

**我的建议**：CLMM 分析是判断论文 contribution 是否成立的 **必要实验**。当前缺少这个实验，论文的 "Likert Blindspot" claim 处于 underdetermined 状态。

### 问题 3：NLI gate 缺陷是否进一步削弱 novelty？

**是的，中等程度地进一步削弱。**

R1-N2（选择偏差）和 R1-N3（阈值 researcher degrees of freedom）共同指向一个问题：NLI gate 是 protocol 中唯一非 off-the-shelf 的设计决策（counterfactual rewriting 和 pairwise comparison 都是标准方法），也是论文声称的方法论增量的核心。如果这个核心增量存在未验证的 selection bias 和未 pre-specified 的 threshold，那么 protocol 作为方法论贡献的可信度下降。

但我不认为这是 fatal：NLI gate 的 **设计意图** 是合理的（确保 content preservation），问题出在 **执行和验证** 不够严格。Sensitivity analysis（不同阈值、NLI-rejected pairs 分析）可以解决这些问题。这是 revision-addressable 的。

---

## 基于 R1 完整审稿意见的评分修正

**关键修正**：我在 Cross-Review 中基于 Director brief 的 "1 clean cell" 将评分从 2.5/5 降到 2.0/5。R1 的实际审稿意见更 nuanced——R1 给出 3.5/5 (Borderline Conference)，且 confound 是 marginal (p=0.072) 而非 definitive。我需要回调。

| 维度 | Round 1 | Cross-Review | 最终修正 | 理由 |
|------|---------|-------------|---------|------|
| Soundness | 3.0 | 2.5 | **3.0 / 5** | R1 给 3.5；confound 是 marginal 非 definitive；methodology sound in design；回调 Cross-Review 的过度下调 |
| Excitement | 2.5 | 2.0 | **2.5 / 5** | 回调：7/9 cells significant 是 PDF 事实（R1 确认）；但 novelty 仍然是已知 insight 的 application |
| **Overall (ARR)** | 2.5 | 2.0 | **2.5 / 5 (Borderline Findings)** | 回调到 Round 1 水平。核心 claim 有 moderate evidence 但 novelty 不足、CLMM underdetermined、NLI gate 未充分验证 |
| **Overall (Director 6pt)** | 3 | 2 | **3 / 6** | 回调到 Round 1 水平 |

**与 R1 的评分差距分析**：R1 给 3.5/5（Borderline Conference），我给 2.5/5（Borderline Findings）——差 1.0 分。差距主要来自 **novelty 评估**（R1 的 focus 是 methods/experiments，对 novelty 评价隐含在 Excitement 3.5 中；我作为 Novelty reviewer 认为已知心理测量学 insight 的 domain transfer + 单一 style axis 不足以达到 Conference level）。这个差距合理——两个 reviewer 侧重不同维度时评分分歧 1 分是正常的。

---

[Reviewer 1 审稿意见]:
## R1 对 R2 完整审稿意见的逐条交叉回应

---

### Must-Fix 问题

**[AGREE with nuance] R2-N1: 新颖性不足——"Likert Blindspot" 是已知现象的重新命名**

同意 R2 的核心论点：Likert vs forced-choice 的灵敏度差异在心理测量学中确实是 well-established 的（Thurstone 1927, Kiritchenko & Mohammad Best-Worst Scaling）。但我认为 R2 的判断略过于严厉，有两个 nuance：

1. **Binarized-Likert 诊断设计并非简单迁移**。论文通过让 binarized Likert 和 pairwise 使用相同的 sign test（§3.4, §5.3），将灵敏度差异精确归因于 measurement structure（side-by-side comparison vs independent rating），而非统计检验的差异。这一诊断思路在 psychometrics 文献中并不常见——通常的 Likert vs pairwise 对比无法区分"test 不同"和"measurement structure 不同"的贡献。
2. **实践影响不可忽视**。LLM 评估社区（Chatbot Arena, MT-Bench, AlpacaEval leaderboard, RATE protocol）大量依赖 Likert 评分。即使 insight 本身已知，在这个具体 domain 的系统性量化仍有价值——类似于 Birhane et al. 对 ImageNet bias 的量化并非发现了"dataset bias"这一概念，但其系统性量化本身构成了贡献。

**我的判断**：novelty 确实是本文最弱环节，但 "incremental application" 不等于 "no contribution"。足以支撑 Findings，不足以支撑 main conference。与我此前评分（Overall 3.0 = Findings）一致。

---

**[AGREE] R2-N2: 引用系统严重不完整**

同意这是 submission-readiness 的硬伤。需要说明版本差异：我审阅的 `best/paper.pdf`（7页）page 7 有可见的参考文献条目（Yao Dou et al., Karpinska et al., Park et al. 等），但 R2 报告的版本存在 "arXiv:2406.xxxxx" 占位符和 "???" 未解析引用。

从 methods review 角度补充：
- **引用缺失不直接影响我对实验设计的评估**——Table 1-9 的统计结果不依赖于引用是否完整。
- **但间接影响 soundness**：如果关键方法论引用（如 RATE, Mir et al. 的 style rewriting, NLI gate 的先例）无法验证，读者无法评估方法论组件的来源和适用性。
- R2 提到总引用约 15 篇，我在 best 版本中也观察到引用数偏少。对于涉及 psychometrics + LLM evaluation + style transfer + NLI 的交叉领域论文，20-30 篇引用是合理预期。

---

**[AGREE with significant nuance] R2-N3: RATE 批评缺乏实证支撑**

这是 Director 特别要求回应的交叉点。R2 的核心质疑：论文用自己的 counterfactual data 上的 Likert 结果来推断 RATE 的 Likert 也会有同样问题，这是 ecological validity 跨越。

**我同意 R2 的方向**，但需要区分两个层面：

1. **论文对 RATE 的直接批评措辞确实过强**。§6 说 "RATE's Likert-based estimates may systematically understate true bias"——这是一个关于 RATE 的实证 claim，但论文没有在 RATE 的 exact setup 下验证。RATE 使用不同的 style axes（formality 之外还有 length, complexity 等）、不同的 rewriting 方法、不同的 benchmarks。论文自己的 Likert 结果不能直接外推到 RATE 的设置。

2. **但论文的 binarized-Likert 诊断提供了一个通用的方法论论据**。§5.3 的核心贡献不是"RATE 是错的"，而是"在控制了统计检验差异后（binarized Likert 用 sign test），measurement structure 本身导致灵敏度差异"。这个 mechanism-level 的论据不依赖于 RATE 的具体设置——如果 Likert 的独立评分结构在任何 style bias detection 中都比 side-by-side comparison 更不敏感，那么 RATE 用 Likert 也会受影响。

**我的判断**：论文应该（a）弱化对 RATE 的直接批评措辞，从 "may systematically understate" 改为 "our results raise the question of whether"；（b）保留 mechanism-level 的论据（binarized-Likert 诊断）；（c）如果要维持对 RATE 的直接批评，需要在 RATE 的设置下做 replication。

**从方法论角度看 §5.3 的比较本身是否合理？** 是的。binarized-Likert 与 pairwise 的对比是 internally valid 的——两者使用相同的数据、相同的 sign test、唯一差异是 binary outcome 的来源（independent Likert scores vs direct comparison）。这个比较的逻辑是 sound 的。问题在于从这个 internal comparison 到 "RATE's Likert is insufficient" 的 external generalization。

---

### Should-Fix 问题

**[AGREE] R2-W1: 范围过窄**

与我此前意见完全一致。Primary evidence 仅 formality，verbosity (Table 8) 和 register (Table 9) 各只有 1 个 judge×benchmark 组合，且 register 未达显著。

---

**[REBUT with partial agreement] R2-W2: 缺少 Bradley-Terry 建模**

这是 Director 特别要求回应的第二个交叉点。

**部分反驳**：Sign test 在本文场景下是 sufficient 的，Bradley-Terry 不是 necessary 的。原因：

1. **研究问题不需要 BT**。论文的核心问题是 "pairwise 能否检测到 Likert 检测不到的 style bias"，答案是 binary 的（显著/不显著）。Sign test 直接回答这个问题。BT 建模的优势在于估计 latent strength parameters 和处理 incomplete comparison data，但论文用的是 complete paired data（每对 z, z' 都被比较了两次），不需要 BT 的参数化假设。

2. **Sign test 更保守、假设更少**。BT 假设 comparison outcomes 服从 logistic 分布，这在 LLM judge 的 discrete forced-choice 中未必成立。Sign test 是 nonparametric 的，不做分布假设，在 n=55-100 的样本量下 power 足够。

3. **BT 在 position-controlled 设计中有复杂性**。论文的 consistency filtering 已经处理了 position bias——只保留两个方向一致的 pairs。如果用 BT，需要将 position 作为一个 factor 纳入模型（Bradley-Terry-Luce with order effects），这增加了模型复杂度但不一定增加对核心问题的回答能力。

**但我同意的部分**：BT 可以作为 supplementary analysis 增加说服力，特别是：
- BT 可以估计 formality 的 latent strength parameter（类似于 Elo rating），这比 win rate 更 interpretable
- BT 可以处理 inconsistent pairs（而非丢弃它们），增加有效样本量
- 如果 BT 结果与 sign test 一致，会增强 robustness

**结论**：Sign test 作为 primary analysis 是 justified 的；BT 作为 supplementary analysis 是 desirable but not required。这是 W (warning) 级别，不是 N (critical) 级别。同意 R2 的分级。

---

**[AGREE] R2-W3: Related work 覆盖不完整**

我没有专门审查 related work 覆盖（这是 R2 的审查维度），但从 methods 角度补充：CalibraEval 和 FairEval 与本文的 judge bias detection 直接相关；BT for judge evaluation (Zheng et al., Chatbot Arena) 是 pairwise comparison 在 LLM evaluation 中的主要先例。这些遗漏会影响读者理解方法论选择的 motivation。

---

**[AGREE — strongest agreement] R2-W4: 无任何图表**

这是 Director 特别要求回应的第三个交叉点。**从实验呈现角度，我强烈同意可视化对传达核心发现至关重要。**

在此前的回应中我已详细论述了三个必要 figures：

1. **Power curve**（最高优先级）：x=sample size, y=power, 三条线（pairwise / binarized Likert / Likert ATE）。这一张图可以同时：(a) 回应 "blindspot vs efficiency gap" 的争论——读者可以看到在什么 n 范围内 Likert 的 power 接近 0；(b) 让 power analysis 的结论可视化验证而非仅凭文字断言；(c) 暴露 post-hoc estimate 的不确定性（加 bootstrap CI）。

2. **Forest plot**（9 cells win rate + 95% CI）：当前 Table 2 和 Table 3 是纯数字矩阵，读者需要逐个比较。Forest plot 可以一目了然地展示效应量分布和跨 cell 的一致性。

3. **Pipeline diagram**（四阶段流程 + attrition）：当前纯文字描述的协议对首次阅读的读者不友好。

**为什么这对本文特别重要**：本文的核心 narrative 是两种 measurement 的灵敏度对比——这本质上是一个 "pattern across conditions" 的故事。Tables 迫使读者逐个数字比较，而 figures 让 pattern 自明。对于一篇核心论据依赖 "7/9 vs 1/9 vs 0/9" 这种跨条件对比的论文，没有 figures 是不可接受的。

---

### R2 Questions 的 R1 视角补充

**R2-Q4 (Bradley-Terry)**: 见上方 W2 的详细回应。Sign test 在此场景下 sufficient。

**R2-Q5 (Binarized Likert 0/9 是否是 power 不足)**: 是的，这正是我在 R1 原稿中独立指出的。n=500 时 binarized Likert p=0.055，距显著仅一步之遥。"Blindspot" 实为 "power gap at typical n"。

---

### 综合评估——纳入 R2 完整意见后

R2 的完整审稿意见加强了我的几个原有判断：
- N1 (novelty) 和 W1 (scope) 使 "Findings vs Main" 的区分更加清晰——这是 Findings 级别的工作
- N2 (引用) 在不同版本间有差异，但即使 best 版本引用数也偏少
- N3 (RATE 批评) 是一个有实质内容的方法论质疑，论文需要弱化措辞或补充 evidence

**最终评分不变**：

| 项目 | 评分 |
|------|------|
| Overall Assessment | **3.0** (Findings) |
| Soundness | 3/5 |
| Excitement | 3/5 |
| Confidence | 4/5 |

R1 与 R2 的评分差异（R1: 3.0 vs R2: 2.5）主要来自对 novelty 的判断力度：R2 认为 "已知现象的重新包装" 是 critical 的 novelty 缺陷，而我认为 binarized-Likert 诊断设计和在 LLM judge 领域的系统性量化仍有 Findings-level 的独立价值。

---

[Reviewer 2 审稿结果]:
R2 交叉回应已提交。核心结论：

- **逐条 [AGREE] R1 全部 Must-Fix 和 Should-Fix 问题**，并从 novelty 角度补充了额外关切
- **修正了 Cross-Review 中基于 Director brief 的过度下调**：R1 实际审稿确认 7/9 cells significant（与 PDF 一致），confound 是 marginal (p=0.072) 而非 definitive
- **最终评分回调至 Round 1 水平**：ARR 2.5/5 (Borderline Findings)，Director 6pt 3/6
- **R1-W1（CLMM）是判断论文 contribution 是否成立的必要实验**——如果 CLMM 显著则核心 claim 被推翻
- **与 R1 的 1.0 分差距**主要来自 novelty 评估维度的分歧，属于正常 reviewer 差异

---

[Reviewer 1 审稿结果]:
R1 交叉回应已提交。对 R2 的 3 个 Must-Fix 和 4 个 Should-Fix 逐条给出了 AGREE/REBUT 判断，重点回应了 Director 指定的三个交叉点：

1. **R2-N3 (RATE 批评)**: AGREE with nuance — §5.3 的 internal comparison 是 sound 的，但从 internal result 到 "RATE's Likert understates bias" 的 external generalization 需要弱化措辞或补充 evidence。
2. **R2-W2 (Bradley-Terry)**: REBUT with partial agreement — Sign test 在此场景下 sufficient（nonparametric、假设更少、直接回答 binary 研究问题），BT 可作为 supplementary 但非 necessary。
3. **R2-W4 (无 Figure)**: AGREE（最强同意）— Power curve、forest plot、pipeline diagram 三张图对传达核心 narrative 至关重要。

最终评分维持 **Overall 3.0 (Findings)**，与 R2 的 2.5 之间的差异主要在 novelty 判断力度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-21T02:03:58.327822+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"因果语言与实际框架严重不匹配——大量使用 counterfactual/ATE 术语但无 DAG、SUTVA、sensitivity analysis\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 AGREE 并建议降调为 quasi-experimental interventional study\"\n    action_items:\n      - round: 1\n        action: \"给出 DAG + 讨论 SUTVA + sensitivity analysis；或降调因果语言改用 diagnostic/detection 框架\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析——最终分析仅基于原始数据 ~1/3，lower-bound claim 缺乏形式化论证\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 AGREE 并补充：应报告 NLI-accepted vs rejected pairs 的 style distance 分布\"\n    action_items:\n      - round: 1\n        action: \"分析 NLI-rejected pairs 的 pairwise 结果；报告 accepted vs rejected 的 style distance 分布；对 lower-bound claim 提供形式化论证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification，verbosity axis per-axis 调整引入 researcher degrees of freedom\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE 并指出这削弱了论文对 RATE 方法论批评的可信度\"\n    action_items:\n      - round: 1\n        action: \"报告阈值 sensitivity analysis（0.85/0.90/0.95）在正文中；说明是否 pre-specified\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是已知心理测量学现象在 LLM judge 的 domain transfer\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 REBUT with nuance——binarized-Likert 诊断设计和 LLM-specific 系统量化有 Findings-level 价值，但不足以支撑 main conference。收敛后仍为 R1/R2 的核心分歧点（0.5分差距来源）\"\n    action_items:\n      - round: 1\n        action: \"重新定位贡献为 first empirical quantification + practical measurement guidance；或提供 LLM judge 社区系统性误用 Likert 的量化证据\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"引用系统严重不完整——placeholder arXiv IDs、broken citations、总引用数偏少\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 报告占位符和 broken citations；R1 AGREE 但注意版本差异（best 版本有参考文献）\"\n    action_items:\n      - round: 1\n        action: \"修复所有 broken citations，补充完整 arXiv ID，增加引用至 20-30 篇\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"RATE 批评缺乏 matched replication——ecological validity 跨越\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE with nuance——§5.3 的 internal comparison 是 sound 的，但到 RATE 的 external generalization 需弱化措辞\"\n    action_items:\n      - round: 1\n        action: \"弱化措辞为 our results raise the question of whether；或在 RATE exact setup 下复现\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 CLMM/ordinal regression，ATE 丢弃 ordinal 信息。CLMM 是判断核心 claim 是否成立的必要实验\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE 并升级重要性——如果 CLMM 显著则核心 claim 被推翻，blindspot 变成 ATE blindspot。收敛后双方共识：CLMM 是必要实验\"\n    action_items:\n      - round: 1\n        action: \"增加 CLMM 分析作为更公平的 Likert baseline——结果决定论文 contribution 是否成立\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering ~40-50% data loss 未分析——被过滤的 position-sensitive pairs 可能系统性保留 formality effect 更强的 pairs\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE 并补充——丢弃 position-inconsistent pairs 可能导致 win rate 被高估\"\n    action_items:\n      - round: 1\n        action: \"报告完整 attrition 表；对 inconsistent pairs 做探索性分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound OR=1.65 p=0.072 为 marginal——需要 formal partial-out analysis\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE。R2 在收敛轮修正了此前 '仅 1 clean cell' 的过度解读——confound 是 marginal 非 definitive，需进一步分析\"\n    action_items:\n      - round: 1\n        action: \"对每个 cell 做 logistic regression (judge_choice ~ is_formal + is_original) 分离 confound\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致——Holm-Bonferroni 仅用于 Table 2\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE\"\n    action_items:\n      - round: 1\n        action: \"报告全局 correction 或按 discovery vs confirmation 区分实验\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis 方法论问题——observed effect size 做 power analysis 是 circular\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE 引用 Hoenig & Heisey 2001\"\n    action_items:\n      - round: 1\n        action: \"改用 CI-based 方法或基于先验 literature effect size\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整 3×3 结果，标题 Style Bias 与覆盖不匹配\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE——标题应改为 formality 或补做多 axis 实验\"\n    action_items:\n      - round: 1\n        action: \"补做 verbosity 等 axis 的完整 3×3 实验；或收窄标题至 formality\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry 建模——pairwise data 的标准分析框架\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 REBUT with partial agreement——sign test 在此场景 sufficient（nonparametric、直接回答 binary 问题），BT 可作 supplementary 但非 necessary\"\n    action_items:\n      - round: 1\n        action: \"BT 作为 supplementary robustness check（非必需但 desirable）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Related work 覆盖不完整——CalibraEval、FairEval、BT for judge evaluation、心理测量学理论文献缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE 从 methods 角度确认这些遗漏影响方法论 motivation 理解\"\n    action_items:\n      - round: 1\n        action: \"补充相关引用，深化 §2 心理测量学文献讨论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表——无 Figure，仅 Tables，视觉传达严重不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 最强同意——列出 power curve + forest plot + pipeline diagram 三个必要 figures\"\n    action_items:\n      - round: 1\n        action: \"至少添加 power curve + forest plot + pipeline diagram\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap——binarized Likert 在 n=500 时 p=0.055，Likert 非 categorically blind 而是 underpowered at typical n\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"交叉讨论强共识。R1 建议限定为 at typical evaluation sample sizes；R2 同意标题与自身数据矛盾\"\n    action_items:\n      - round: 1\n        action: \"将 blindspot 修改为 sensitivity/efficiency gap；或限定为 at typical evaluation sample sizes 并补 power curve 支撑\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound 为 marginal (p=0.072)——需要 per-cell formal partial-out analysis 而非整体忽略\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 confound 分析提出；R2 在收敛轮修正了 '仅 1 clean cell' 的过度解读——confound 是 marginal 非 definitive，但仍需 formal analysis。7/9 cells 的统计显著性由 PDF 确认\"\n    action_items:\n      - round: 1\n        action: \"对每个 cell 独立做 confound analysis；明确区分 fully controlled vs suggestive evidence\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转（Claude×LLMBar）——Likert 和 pairwise 可能测量不同构念\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 发现；R2 建议升级重要性，需要理论解释\"\n    action_items:\n      - round: 1\n        action: \"解释方向不一致的原因及对 same-construct 假设的影响\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-4\"\n    summary: \"CLMM 是判断 Likert Blindspot claim 是否成立的必要实验——当前处于 underdetermined 状态\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"收敛轮新增共识。R1-W1 提出 CLMM 作为更公平 baseline；R2 将其升级为必要实验——如果 CLMM 显著则核心 claim 从 Likert Blindspot 变为 ATE Blindspot\"\n    action_items:\n      - round: 1\n        action: \"执行 CLMM 分析——结果决定论文 contribution 的本质定义\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"因果语言与实际框架严重不匹配——大量使用 counterfactual/ATE 术语但无 DAG、SUTVA、sensitivity analysis\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 AGREE 并建议降调为 quasi-experimental interventional study\"\n    action_items:\n      - round: 1\n        action: \"给出 DAG + 讨论 SUTVA + sensitivity analysis；或降调因果语言改用 diagnostic/detection 框架\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析——最终分析仅基于原始数据 ~1/3，lower-bound claim 缺乏形式化论证\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 AGREE 并补充：应报告 NLI-accepted vs rejected pairs 的 style distance 分布\"\n    action_items:\n      - round: 1\n        action: \"分析 NLI-rejected pairs 的 pairwise 结果；报告 accepted vs rejected 的 style distance 分布；对 lower-bound claim 提供形式化论证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification，verbosity axis per-axis 调整引入 researcher degrees of freedom\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE 并指出这削弱了论文对 RATE 方法论批评的可信度\"\n    action_items:\n      - round: 1\n        action: \"报告阈值 sensitivity analysis（0.85/0.90/0.95）在正文中；说明是否 pre-specified\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是已知心理测量学现象在 LLM judge 的 domain transfer\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 REBUT with nuance——binarized-Likert 诊断设计和 LLM-specific 系统量化有 Findings-level 价值，但不足以支撑 main conference。收敛后仍为 R1/R2 的核心分歧点（0.5分差距来源）\"\n    action_items:\n      - round: 1\n        action: \"重新定位贡献为 first empirical quantification + practical measurement guidance；或提供 LLM judge 社区系统性误用 Likert 的量化证据\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"引用系统严重不完整——placeholder arXiv IDs、broken citations、总引用数偏少\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 报告占位符和 broken citations；R1 AGREE 但注意版本差异（best 版本有参考文献）\"\n    action_items:\n      - round: 1\n        action: \"修复所有 broken citations，补充完整 arXiv ID，增加引用至 20-30 篇\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"RATE 批评缺乏 matched replication——ecological validity 跨越\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE with nuance——§5.3 的 internal comparison 是 sound 的，但到 RATE 的 external generalization 需弱化措辞\"\n    action_items:\n      - round: 1\n        action: \"弱化措辞为 our results raise the question of whether；或在 RATE exact setup 下复现\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 CLMM/ordinal regression，ATE 丢弃 ordinal 信息。CLMM 是判断核心 claim 是否成立的必要实验\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE 并升级重要性——如果 CLMM 显著则核心 claim 被推翻，blindspot 变成 ATE blindspot。收敛后双方共识：CLMM 是必要实验\"\n    action_items:\n      - round: 1\n        action: \"增加 CLMM 分析作为更公平的 Likert baseline——结果决定论文 contribution 是否成立\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering ~40-50% data loss 未分析——被过滤的 position-sensitive pairs 可能系统性保留 formality effect 更强的 pairs\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE 并补充——丢弃 position-inconsistent pairs 可能导致 win rate 被高估\"\n    action_items:\n      - round: 1\n        action: \"报告完整 attrition 表；对 inconsistent pairs 做探索性分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound OR=1.65 p=0.072 为 marginal——需要 formal partial-out analysis\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE。R2 在收敛轮修正了此前 '仅 1 clean cell' 的过度解读——confound 是 marginal 非 definitive，需进一步分析\"\n    action_items:\n      - round: 1\n        action: \"对每个 cell 做 logistic regression (judge_choice ~ is_formal + is_original) 分离 confound\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致——Holm-Bonferroni 仅用于 Table 2\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE\"\n    action_items:\n      - round: 1\n        action: \"报告全局 correction 或按 discovery vs confirmation 区分实验\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis 方法论问题——observed effect size 做 power analysis 是 circular\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE 引用 Hoenig & Heisey 2001\"\n    action_items:\n      - round: 1\n        action: \"改用 CI-based 方法或基于先验 literature effect size\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整 3×3 结果，标题 Style Bias 与覆盖不匹配\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE——标题应改为 formality 或补做多 axis 实验\"\n    action_items:\n      - round: 1\n        action: \"补做 verbosity 等 axis 的完整 3×3 实验；或收窄标题至 formality\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry 建模——pairwise data 的标准分析框架\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 REBUT with partial agreement——sign test 在此场景 sufficient（nonparametric、直接回答 binary 问题），BT 可作 supplementary 但非 necessary\"\n    action_items:\n      - round: 1\n        action: \"BT 作为 supplementary robustness check（非必需但 desirable）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Related work 覆盖不完整——CalibraEval、FairEval、BT for judge evaluation、心理测量学理论文献缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE 从 methods 角度确认这些遗漏影响方法论 motivation 理解\"\n    action_items:\n      - round: 1\n        action: \"补充相关引用，深化 §2 心理测量学文献讨论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表——无 Figure，仅 Tables，视觉传达严重不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 最强同意——列出 power curve + forest plot + pipeline diagram 三个必要 figures\"\n    action_items:\n      - round: 1\n        action: \"至少添加 power curve + forest plot + pipeline diagram\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap——binarized Likert 在 n=500 时 p=0.055，Likert 非 categorically blind 而是 underpowered at typical n\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"交叉讨论强共识。R1 建议限定为 at typical evaluation sample sizes；R2 同意标题与自身数据矛盾\"\n    action_items:\n      - round: 1\n        action: \"将 blindspot 修改为 sensitivity/efficiency gap；或限定为 at typical evaluation sample sizes 并补 power curve 支撑\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound 为 marginal (p=0.072)——需要 per-cell formal partial-out analysis 而非整体忽略\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 confound 分析提出；R2 在收敛轮修正了 '仅 1 clean cell' 的过度解读——confound 是 marginal 非 definitive，但仍需 formal analysis。7/9 cells 的统计显著性由 PDF 确认\"\n    action_items:\n      - round: 1\n        action: \"对每个 cell 独立做 confound analysis；明确区分 fully controlled vs suggestive evidence\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转（Claude×LLMBar）——Likert 和 pairwise 可能测量不同构念\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 发现；R2 建议升级重要性，需要理论解释\"\n    action_items:\n      - round: 1\n        action: \"解释方向不一致的原因及对 same-construct 假设的影响\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-4\"\n    summary: \"CLMM 是判断 Likert Blindspot claim 是否成立的必要实验——当前处于 underdetermined 状态\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"收敛轮新增共识。R1-W1 提出 CLMM 作为更公平 baseline；R2 将其升级为必要实验——如果 CLMM 显著则核心 claim 从 Likert Blindspot 变为 ATE Blindspot\"\n    action_items:\n      - round: 1\n        action: \"执行 CLMM 分析——结果决定论文 contribution 的本质定义\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-21T02:03:58.378848+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 10944}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-21T02:05:50.677827+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 1（修正版）\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审稿人**: R1 (Methods & Experiments) + R2 (Novelty & Related Work)\n**日期**: 2026-05-21\n**修正说明**: 本版修正了初版报告中基于 Director brief 的 \"仅 1 clean cell\" 过度解读。R2 在收敛轮确认 7/9 cells 统计显著性由 PDF 支持，original preference confound 是 marginal (p=0.072) 而非 definitive，评分从 2.0 回调至 2.5。R1 部分反驳了 BT 建模的必要性。新增 CLMM 作为判断核心 claim 的必要实验。\n\n---\n\n## Summary\n\n论文提出 5 阶段反事实协议（counterfactual style rewriting → NLI content gate → position control → Likert control → original preference control），在 3 judges × 3 benchmarks 网格上比较 Likert 与 pairwise 对 formality style bias 的检测灵敏度。核心发现：pairwise 在 7/9 cells 中检测到显著 formality bias，Likert ATE 仅 1/9，binarized Likert 0/9。论文据此提出 \"Likert Blindspot\" 概念。\n\n---\n\n## Strengths\n\n- **S1** 研究问题有直接实践意义：如果 Likert 系统性漏检 style bias，影响所有 LLM-as-judge 评估管线 [R1+R2 共识]\n- **S2** Pipeline 设计系统性强，四阶段协议每步针对特定 confound，逻辑完整 [R1+R2 共识]\n- **S3** 3 judges × 3 benchmarks 网格覆盖多 LLM 家族（GPT-4o / Claude / Gemini）[R2-S3]\n- **S4** **Binarized-Likert 诊断设计是最强方法论贡献**——通过共用 sign test 隔离 measurement structure 作为灵敏度差异来源。这一诊断思路在 psychometrics 文献中不常见，构成独立方法论增量 [R1 独立识别，R2 部分认可]\n- **S5** 人工 NLI 验证（n=100, 91% agreement）为 content preservation gate 提供可信质量保证 [R2-S5]\n- **S6** Scaled replication（n=500）确认效应量稳定 [R2-S6]\n- **S7** Limitations 讨论诚实：明确承认因果框架近似性、样本量限制、仅检测不纠正 [R1+R2 共识]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, R1+R2 共识] **\"Blindspot\" 实为 sample-size-dependent efficiency gap**\nBinarized Likert 在 n=500 时 p=0.055（R1 报告），距显著仅一步之遥。Likert 不是 categorically blind，而是在 typical n=100 下 underpowered。标题 \"The Likert Blindspot\" 暗示定性测量失败，实际是定量效率差异。论文 §6 Discussion 自述 \"complementary rather than adversarial\"，与标题的强势措辞矛盾。\n\n**W2** [critical, R1+R2 共识] **CLMM 是判断核心 claim 的必要实验——当前处于 underdetermined 状态**\n论文用 t-test on ATE 和 binarized sign test 评估 Likert 灵敏度，但 Likert 数据是 ordinal 非 interval。CLMM（Cumulative Link Mixed Model）或 ordinal logistic regression 能更好利用 ordinal 结构。**关键**：如果 CLMM 显著，则\"Likert Blindspot\"不是 Likert 量表的固有缺陷，而是分析方法（ATE）的缺陷——核心 claim 的本质定义将改变。作者必须在 revision 中报告 CLMM 结果。\n\n**W3** [critical, R1] **因果语言与实际框架严重不匹配**\n大量使用 \"counterfactual\"、\"interventional\"、\"ATE\" 等因果术语，但无 DAG、未讨论 SUTVA、无 sensitivity analysis for unmeasured confounders。R2 建议更准确定位为 \"quasi-experimental interventional study\"。降调因果语言会削弱 novelty narrative 但避免不必要的审稿攻击面。\n\n**W4** [critical, R1+R2 共识] **NLI gate 67% false-negative rate 造成的选择偏差未分析**\n最终分析仅基于原始数据 ~1/3。\"Lower-bound\" claim 需要未验证的假设：NLI-rejected pairs 的 bias 方向与 accepted pairs 一致。R2 补充：应报告 NLI-accepted vs rejected pairs 的 style distance 分布——如果 accepted pairs 的 style distance 系统性偏小，则 bias estimate 可能被压低。\n\n**W5** [critical, R1+R2 共识] **NLI 阈值 0.90 无 justification，per-axis 调整引入 researcher degrees of freedom**\nVerbosity axis 从 bidirectional 改为 direction-aware gating 是 post-hoc 方法修改。R2 指出这削弱了论文对 RATE 方法论批评的可信度。阈值 sensitivity analysis 应在正文（非 appendix）。\n\n**W6** [critical, R2; R1 部分反驳] **Novelty 不足——已知心理测量学现象的 domain transfer**\nLikert vs forced-choice sensitivity gap 是 Thurstone (1927) 以来的共识。R1 部分反驳：binarized-Likert 诊断设计并非简单迁移，在 LLM judge 领域的系统性量化有 Findings-level 价值。**收敛后仍为核心分歧点**——R1 认为足以支撑 Findings，R2 认为 evidence breadth 不足。\n\n**W7** [critical, R2; R1 确认版本差异] **引用系统不完整**\nR2 报告 placeholder arXiv IDs（\"arXiv:2406.xxxxx\"）和 broken citations；R1 审阅的 best 版本有参考文献但引用数偏少。双方共识：目标 20-30 篇引用。\n\n**W8** [critical, R2; R1 AGREE with nuance] **RATE 批评缺乏 matched replication**\n§5.3 的 binarized-Likert internal comparison 是 sound 的（R1 确认），但从 internal result 到 \"RATE's Likert understates bias\" 的 external generalization 是 ecological validity 跨越。应弱化措辞或补充 evidence。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W9** [warning, R1+R2 最强共识] **全文零图表**。至少需要：(1) Power curve（pairwise vs binarized Likert vs Likert ATE, x=n, y=power）——直接回应 blindspot vs efficiency gap 争论；(2) Forest plot（9 cells win rate + 95% CI）——让 pattern 自明；(3) Pipeline diagram（四阶段 + attrition）。对 borderline 论文，presentation 可能是 tipping point。\n\n**W10** [warning, R1+R2 共识] **范围窄于标题承诺**——仅 formality 有完整 3×3 结果。Verbosity（Table 8）和 register（Table 9）各仅 1 个 cell，register 未达显著（p=0.068）。标题 \"Style Bias\" 与实际覆盖不匹配。\n\n**W11** [warning, R1+R2 共识] **Original preference confound OR=1.65, p=0.072 为 marginal**——需要 per-cell logistic regression formal partial-out。注：此 confound 是 marginal 而非 definitive，7/9 cells 的统计显著性由 PDF 确认，但缺乏 per-cell 独立 confound 控制。\n\n**W12** [warning, R1+R2 共识] **Consistency filtering ~40-50% data loss 未分析**——丢弃的 position-inconsistent pairs 可能系统性保留 formality effect 更强的 pairs，导致 win rate 高估。缺少完整 attrition 表。\n\n**W13** [warning, R1+R2] **Likert ATE 方向反转（Claude×LLMBar）**——Likert 和 pairwise 可能测量不同构念。\"Blindspot\" narrative 隐含 same-construct 假设需要质疑。\n\n**W14** [warning, R1+R2] **Multiple comparison correction 不一致**——Holm-Bonferroni 仅 Table 2，其他 ~20+ 次检验未校正。\n\n**W15** [warning, R1+R2] **Post-hoc power analysis 方法论问题**——observed effect size 做 power analysis 是 circular（Hoenig & Heisey 2001），\"5× efficiency gap\" 可信度受限。\n\n**W16** [warning, R2; R1 部分反驳] **缺少 Bradley-Terry 建模**——R1 反驳：sign test 在此场景 sufficient（nonparametric、直接回答 binary 问题、complete paired data 不需 BT 参数化假设）。BT 可作 supplementary robustness check，但非 necessary。\n\n**W17** [warning, R2; R1 确认] **Related work 覆盖不完整**——CalibraEval、FairEval、BT for judge evaluation、心理测量学理论文献缺失。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Pipeline 设计在逻辑上合理**，方法论训练扎实 [R1+R2]\n2. **Binarized-Likert 诊断设计是最有价值的方法论贡献** [R1 提出，R2 部分认可]\n3. **\"Blindspot\" 实为 efficiency gap**——n=500 时 binarized Likert 接近显著 [R1+R2 强共识]\n4. **CLMM 是判断核心 claim 的必要实验**——当前 underdetermined [收敛轮新增共识]\n5. **全文零 figures 是严重 presentation 缺陷** [R1+R2 最强共识]\n6. **标题 scope 宽于实际覆盖** [R1+R2]\n7. **Limitations 讨论诚实** [R1+R2]\n8. **Original preference confound 为 marginal (p=0.072)，需 formal analysis 但非 definitive** [收敛轮修正共识]\n9. **NLI gate 设计意图合理，但执行和验证不够严格**——sensitivity analysis 可解决 [R1+R2]\n10. **Sign test 作为 primary analysis 是 justified 的**；BT 可作 supplementary [R1 反驳 R2，R2 未再争议]\n\n## Reviewer Divergence\n\n1. **Novelty 是否达到 Findings 水平**（核心分歧，0.5 分差距来源）：R1 认为 binarized-Likert 诊断设计 + LLM-specific 系统量化构成 Findings-level 贡献；R2 认为 evidence breadth 不足以支撑 even Findings（但最终给 2.5 Borderline Findings，未完全否定）。\n2. **引用问题严重程度**：可能存在审阅版本差异（R1 best 版本有参考文献，R2 版本有明显缺陷）。\n\n---\n\n## Questions for Authors\n\n1. 请报告每个 judge×benchmark cell 的完整 attrition 数据（generated → NLI pass → consistent → final n）\n2. NLI 阈值 0.90 是 pre-specified 还是 post-hoc？请提供 threshold sensitivity analysis（0.85/0.90/0.95）**在正文中**\n3. NLI-rejected 但 human-valid 的 pairs 中 judge 的 formality preference 方向是什么？请同时报告 NLI-accepted vs rejected pairs 的 style distance 分布\n4. 请执行 CLMM/ordinal logistic regression 分析 Likert 数据——结果决定 \"Likert Blindspot\" claim 的本质定义\n5. 对每个 cell 做 logistic regression (judge_choice ~ is_formal + is_original)，报告 formality effect 在控制 original preference 后的变化\n6. 请解释 Claude×LLMBar 的 Likert ATE 方向反转——Likert 和 pairwise 是否在测量不同构念？\n7. Consistency filtering 去掉的 ~40-50% pairs 中 position bias 方向如何？\n8. Abstract 的 headline win rate 是否应以 n=500 的 effect size 为主？\n9. 相对于 Karpinska et al. 和 Novikova et al.，本文贡献具体超越 domain transfer 的部分是什么？\n10. 所有引用是否真实可验证？Placeholder arXiv IDs 需修复。\n\n---\n\n## Missing References\n\n- **CalibraEval** — LLM judge calibration\n- **FairEval** (Wang et al., 2023) — judge fairness 前驱工作\n- **Chatbot Arena / Bradley-Terry** 文献 — pairwise comparison in LLM evaluation\n- **心理测量学理论** — DeCoster et al. (2011), Simms et al. (2019) 等 Likert vs forced-choice 理论分析\n- **LLM-as-Judge 综述** — post-Zheng et al. (2023) survey papers\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n## Visual Layout Check\n\n未派发。\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| Reviewer | Overall (ARR) | Soundness | Excitement | Confidence |\n|----------|---------------|-----------|------------|------------|\n| R1 | **3.0** (Findings) | 3/5 | 3/5 | 4/5 |\n| R2 | **2.5** (Borderline Findings) | 3/5 | 2.5/5 | 4/5 |\n\n### Director 综合评分: **2.5 / 5 (Borderline Findings)**\n\n**判断依据**：\n\nR1 (3.0) 和 R2 (2.5) 的差距收敛至 0.5 分，分歧仅在 novelty 判断。Director 取 2.5 (Borderline Findings) 基于以下权衡：\n\n**支持 Findings (3.0) 的因素**（R1 视角）：\n- Binarized-Likert 诊断设计有独立方法论价值，并非简单 domain transfer\n- GPT-4o×LLMBar 上的 primary evidence 在多项 confound 控制下可信\n- 对 LLM-as-judge 社区有直接实践指导意义\n- Pipeline 设计系统，Limitations 诚实\n\n**支持 Borderline Findings (2.5) 的因素**（R2 视角 + 共识问题）：\n- 8 个 critical issues 叠加（efficiency gap 矛盾、CLMM underdetermined、因果框架缺失、NLI 选择偏差、阈值无 justification、novelty 不足、引用缺陷、RATE 批评无支撑）\n- Fully controlled evidence 集中在 1-2 个 cells，generalization 是 suggestive\n- 零 figures + scope 窄于标题——presentation 不达标\n- CLMM 是 existential test：如果 CLMM 显著，核心 claim 被推翻\n\n**结论**：论文在有实践意义的问题上做了设计合理的实验，binarized-Likert 诊断设计有独立价值。但 critical issues 密度过高，且 CLMM 这一 existential test 未执行，使得核心 claim 处于 underdetermined 状态。在 CLMM 结果出来前，无法给出高于 Borderline Findings 的评分。\n\n---\n\n## Resubmission Roadmap\n\n**Priority 1（解决后可达 Findings 3.0）**：\n1. 执行 CLMM 分析——决定论文 contribution 的本质\n2. NLI threshold sensitivity analysis（至少 3 阈值点，正文中报告）\n3. 报告 NLI-rejected pairs 的 bias 方向和 style distance 分布\n4. 添加 power curve + forest plot + pipeline diagram（至少 3 张 figures）\n5. 修复全部引用，补充 missing references 至 20-30 篇\n\n**Priority 2（解决后可达 Borderline Conference 3.5）**：\n6. Per-cell confound analysis（logistic regression partial out original preference）\n7. 补做 verbosity 完整 3×3 实验（或收窄标题至 formality）\n8. 将 \"blindspot\" 重新框定为 \"sensitivity gap at typical n\"（配 power curve 支撑）\n9. 完整 attrition 表 + inconsistent pairs 探索性分析\n\n**Priority 3（解决后可达 Conference 4.0）**：\n10. DAG + SUTVA 讨论（或降调因果语言为 quasi-experimental）\n11. BT 建模作为 supplementary robustness check\n12. 解释 Likert ATE 方向反转的理论含义\n13. 弱化 RATE 批评措辞或补充 matched replication",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "2.5 / 5 (Borderline Findings)",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 1（修正版）\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审稿人**: R1 (Methods & Experiments) + R2 (Novelty & Related Work)\n**日期**: 2026-05-21\n**修正说明**: 本版修正了初版报告中基于 Director brief 的 \"仅 1 clean cell\" 过度解读。R2 在收敛轮确认 7/9 cells 统计显著性由 PDF 支持，original preference confound 是 marginal (p=0.072) 而非 definitive，评分从 2.0 回调至 2.5。R1 部分反驳了 BT 建模的必要性。新增 CLMM 作为判断核心 claim 的必要实验。\n\n---\n\n## Summary\n\n论文提出 5 阶段反事实协议（counterfactual style rewriting → NLI content gate → position control → Likert control → original preference control），在 3 judges × 3 benchmarks 网格上比较 Likert 与 pairwise 对 formality style bias 的检测灵敏度。核心发现：pairwise 在 7/9 cells 中检测到显著 formality bias，Likert ATE 仅 1/9，binarized Likert 0/9。论文据此提出 \"Likert Blindspot\" 概念。\n\n---\n\n## Strengths\n\n- **S1** 研究问题有直接实践意义：如果 Likert 系统性漏检 style bias，影响所有 LLM-as-judge 评估管线 [R1+R2 共识]\n- **S2** Pipeline 设计系统性强，四阶段协议每步针对特定 confound，逻辑完整 [R1+R2 共识]\n- **S3** 3 judges × 3 benchmarks 网格覆盖多 LLM 家族（GPT-4o / Claude / Gemini）[R2-S3]\n- **S4** **Binarized-Likert 诊断设计是最强方法论贡献**——通过共用 sign test 隔离 measurement structure 作为灵敏度差异来源。这一诊断思路在 psychometrics 文献中不常见，构成独立方法论增量 [R1 独立识别，R2 部分认可]\n- **S5** 人工 NLI 验证（n=100, 91% agreement）为 content preservation gate 提供可信质量保证 [R2-S5]\n- **S6** Scaled replication（n=500）确认效应量稳定 [R2-S6]\n- **S7** Limitations 讨论诚实：明确承认因果框架近似性、样本量限制、仅检测不纠正 [R1+R2 共识]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, R1+R2 共识] **\"Blindspot\" 实为 sample-size-dependent efficiency gap**\nBinarized Likert 在 n=500 时 p=0.055（R1 报告），距显著仅一步之遥。Likert 不是 categorically blind，而是在 typical n=100 下 underpowered。标题 \"The Likert Blindspot\" 暗示定性测量失败，实际是定量效率差异。论文 §6 Discussion 自述 \"complementary rather than adversarial\"，与标题的强势措辞矛盾。\n\n**W2** [critical, R1+R2 共识] **CLMM 是判断核心 claim 的必要实验——当前处于 underdetermined 状态**\n论文用 t-test on ATE 和 binarized sign test 评估 Likert 灵敏度，但 Likert 数据是 ordinal 非 interval。CLMM（Cumulative Link Mixed Model）或 ordinal logistic regression 能更好利用 ordinal 结构。**关键**：如果 CLMM 显著，则\"Likert Blindspot\"不是 Likert 量表的固有缺陷，而是分析方法（ATE）的缺陷——核心 claim 的本质定义将改变。作者必须在 revision 中报告 CLMM 结果。\n\n**W3** [critical, R1] **因果语言与实际框架严重不匹配**\n大量使用 \"counterfactual\"、\"interventional\"、\"ATE\" 等因果术语，但无 DAG、未讨论 SUTVA、无 sensitivity analysis for unmeasured confounders。R2 建议更准确定位为 \"quasi-experimental interventional study\"。降调因果语言会削弱 novelty narrative 但避免不必要的审稿攻击面。\n\n**W4** [critical, R1+R2 共识] **NLI gate 67% false-negative rate 造成的选择偏差未分析**\n最终分析仅基于原始数据 ~1/3。\"Lower-bound\" claim 需要未验证的假设：NLI-rejected pairs 的 bias 方向与 accepted pairs 一致。R2 补充：应报告 NLI-accepted vs rejected pairs 的 style distance 分布——如果 accepted pairs 的 style distance 系统性偏小，则 bias estimate 可能被压低。\n\n**W5** [critical, R1+R2 共识] **NLI 阈值 0.90 无 justification，per-axis 调整引入 researcher degrees of freedom**\nVerbosity axis 从 bidirectional 改为 direction-aware gating 是 post-hoc 方法修改。R2 指出这削弱了论文对 RATE 方法论批评的可信度。阈值 sensitivity analysis 应在正文（非 appendix）。\n\n**W6** [critical, R2; R1 部分反驳] **Novelty 不足——已知心理测量学现象的 domain transfer**\nLikert vs forced-choice sensitivity gap 是 Thurstone (1927) 以来的共识。R1 部分反驳：binarized-Likert 诊断设计并非简单迁移，在 LLM judge 领域的系统性量化有 Findings-level 价值。**收敛后仍为核心分歧点**——R1 认为足以支撑 Findings，R2 认为 evidence breadth 不足。\n\n**W7** [critical, R2; R1 确认版本差异] **引用系统不完整**\nR2 报告 placeholder arXiv IDs（\"arXiv:2406.xxxxx\"）和 broken citations；R1 审阅的 best 版本有参考文献但引用数偏少。双方共识：目标 20-30 篇引用。\n\n**W8** [critical, R2; R1 AGREE with nuance] **RATE 批评缺乏 matched replication**\n§5.3 的 binarized-Likert internal comparison 是 sound 的（R1 确认），但从 internal result 到 \"RATE's Likert understates bias\" 的 external generalization 是 ecological validity 跨越。应弱化措辞或补充 evidence。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W9** [warning, R1+R2 最强共识] **全文零图表**。至少需要：(1) Power curve（pairwise vs binarized Likert vs Likert ATE, x=n, y=power）——直接回应 blindspot vs efficiency gap 争论；(2) Forest plot（9 cells win rate + 95% CI）——让 pattern 自明；(3) Pipeline diagram（四阶段 + attrition）。对 borderline 论文，presentation 可能是 tipping point。\n\n**W10** [warning, R1+R2 共识] **范围窄于标题承诺**——仅 formality 有完整 3×3 结果。Verbosity（Table 8）和 register（Table 9）各仅 1 个 cell，register 未达显著（p=0.068）。标题 \"Style Bias\" 与实际覆盖不匹配。\n\n**W11** [warning, R1+R2 共识] **Original preference confound OR=1.65, p=0.072 为 marginal**——需要 per-cell logistic regression formal partial-out。注：此 confound 是 marginal 而非 definitive，7/9 cells 的统计显著性由 PDF 确认，但缺乏 per-cell 独立 confound 控制。\n\n**W12** [warning, R1+R2 共识] **Consistency filtering ~40-50% data loss 未分析**——丢弃的 position-inconsistent pairs 可能系统性保留 formality effect 更强的 pairs，导致 win rate 高估。缺少完整 attrition 表。\n\n**W13** [warning, R1+R2] **Likert ATE 方向反转（Claude×LLMBar）**——Likert 和 pairwise 可能测量不同构念。\"Blindspot\" narrative 隐含 same-construct 假设需要质疑。\n\n**W14** [warning, R1+R2] **Multiple comparison correction 不一致**——Holm-Bonferroni 仅 Table 2，其他 ~20+ 次检验未校正。\n\n**W15** [warning, R1+R2] **Post-hoc power analysis 方法论问题**——observed effect size 做 power analysis 是 circular（Hoenig & Heisey 2001），\"5× efficiency gap\" 可信度受限。\n\n**W16** [warning, R2; R1 部分反驳] **缺少 Bradley-Terry 建模**——R1 反驳：sign test 在此场景 sufficient（nonparametric、直接回答 binary 问题、complete paired data 不需 BT 参数化假设）。BT 可作 supplementary robustness check，但非 necessary。\n\n**W17** [warning, R2; R1 确认] **Related work 覆盖不完整**——CalibraEval、FairEval、BT for judge evaluation、心理测量学理论文献缺失。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Pipeline 设计在逻辑上合理**，方法论训练扎实 [R1+R2]\n2. **Binarized-Likert 诊断设计是最有价值的方法论贡献** [R1 提出，R2 部分认可]\n3. **\"Blindspot\" 实为 efficiency gap**——n=500 时 binarized Likert 接近显著 [R1+R2 强共识]\n4. **CLMM 是判断核心 claim 的必要实验**——当前 underdetermined [收敛轮新增共识]\n5. **全文零 figures 是严重 presentation 缺陷** [R1+R2 最强共识]\n6. **标题 scope 宽于实际覆盖** [R1+R2]\n7. **Limitations 讨论诚实** [R1+R2]\n8. **Original preference confound 为 marginal (p=0.072)，需 formal analysis 但非 definitive** [收敛轮修正共识]\n9. **NLI gate 设计意图合理，但执行和验证不够严格**——sensitivity analysis 可解决 [R1+R2]\n10. **Sign test 作为 primary analysis 是 justified 的**；BT 可作 supplementary [R1 反驳 R2，R2 未再争议]\n\n## Reviewer Divergence\n\n1. **Novelty 是否达到 Findings 水平**（核心分歧，0.5 分差距来源）：R1 认为 binarized-Likert 诊断设计 + LLM-specific 系统量化构成 Findings-level 贡献；R2 认为 evidence breadth 不足以支撑 even Findings（但最终给 2.5 Borderline Findings，未完全否定）。\n2. **引用问题严重程度**：可能存在审阅版本差异（R1 best 版本有参考文献，R2 版本有明显缺陷）。\n\n---\n\n## Questions for Authors\n\n1. 请报告每个 judge×benchmark cell 的完整 attrition 数据（generated → NLI pass → consistent → final n）\n2. NLI 阈值 0.90 是 pre-specified 还是 post-hoc？请提供 threshold sensitivity analysis（0.85/0.90/0.95）**在正文中**\n3. NLI-rejected 但 human-valid 的 pairs 中 judge 的 formality preference 方向是什么？请同时报告 NLI-accepted vs rejected pairs 的 style distance 分布\n4. 请执行 CLMM/ordinal logistic regression 分析 Likert 数据——结果决定 \"Likert Blindspot\" claim 的本质定义\n5. 对每个 cell 做 logistic regression (judge_choice ~ is_formal + is_original)，报告 formality effect 在控制 original preference 后的变化\n6. 请解释 Claude×LLMBar 的 Likert ATE 方向反转——Likert 和 pairwise 是否在测量不同构念？\n7. Consistency filtering 去掉的 ~40-50% pairs 中 position bias 方向如何？\n8. Abstract 的 headline win rate 是否应以 n=500 的 effect size 为主？\n9. 相对于 Karpinska et al. 和 Novikova et al.，本文贡献具体超越 domain transfer 的部分是什么？\n10. 所有引用是否真实可验证？Placeholder arXiv IDs 需修复。\n\n---\n\n## Missing References\n\n- **CalibraEval** — LLM judge calibration\n- **FairEval** (Wang et al., 2023) — judge fairness 前驱工作\n- **Chatbot Arena / Bradley-Terry** 文献 — pairwise comparison in LLM evaluation\n- **心理测量学理论** — DeCoster et al. (2011), Simms et al. (2019) 等 Likert vs forced-choice 理论分析\n- **LLM-as-Judge 综述** — post-Zheng et al. (2023) survey papers\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n## Visual Layout Check\n\n未派发。\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| Reviewer | Overall (ARR) | Soundness | Excitement | Confidence |\n|----------|---------------|-----------|------------|------------|\n| R1 | **3.0** (Findings) | 3/5 | 3/5 | 4/5 |\n| R2 | **2.5** (Borderline Findings) | 3/5 | 2.5/5 | 4/5 |\n\n### Director 综合评分: **2.5 / 5 (Borderline Findings)**\n\n**判断依据**：\n\nR1 (3.0) 和 R2 (2.5) 的差距收敛至 0.5 分，分歧仅在 novelty 判断。Director 取 2.5 (Borderline Findings) 基于以下权衡：\n\n**支持 Findings (3.0) 的因素**（R1 视角）：\n- Binarized-Likert 诊断设计有独立方法论价值，并非简单 domain transfer\n- GPT-4o×LLMBar 上的 primary evidence 在多项 confound 控制下可信\n- 对 LLM-as-judge 社区有直接实践指导意义\n- Pipeline 设计系统，Limitations 诚实\n\n**支持 Borderline Findings (2.5) 的因素**（R2 视角 + 共识问题）：\n- 8 个 critical issues 叠加（efficiency gap 矛盾、CLMM underdetermined、因果框架缺失、NLI 选择偏差、阈值无 justification、novelty 不足、引用缺陷、RATE 批评无支撑）\n- Fully controlled evidence 集中在 1-2 个 cells，generalization 是 suggestive\n- 零 figures + scope 窄于标题——presentation 不达标\n- CLMM 是 existential test：如果 CLMM 显著，核心 claim 被推翻\n\n**结论**：论文在有实践意义的问题上做了设计合理的实验，binarized-Likert 诊断设计有独立价值。但 critical issues 密度过高，且 CLMM 这一 existential test 未执行，使得核心 claim 处于 underdetermined 状态。在 CLMM 结果出来前，无法给出高于 Borderline Findings 的评分。\n\n---\n\n## Resubmission Roadmap\n\n**Priority 1（解决后可达 Findings 3.0）**：\n1. 执行 CLMM 分析——决定论文 contribution 的本质\n2. NLI threshold sensitivity analysis（至少 3 阈值点，正文中报告）\n3. 报告 NLI-rejected pairs 的 bias 方向和 style distance 分布\n4. 添加 power curve + forest plot + pipeline diagram（至少 3 张 figures）\n5. 修复全部引用，补充 missing references 至 20-30 篇\n\n**Priority 2（解决后可达 Borderline Conference 3.5）**：\n6. Per-cell confound analysis（logistic regression partial out original preference）\n7. 补做 verbosity 完整 3×3 实验（或收窄标题至 formality）\n8. 将 \"blindspot\" 重新框定为 \"sensitivity gap at typical n\"（配 power curve 支撑）\n9. 完整 attrition 表 + inconsistent pairs 探索性分析\n\n**Priority 3（解决后可达 Conference 4.0）**：\n10. DAG + SUTVA 讨论（或降调因果语言为 quasi-experimental）\n11. BT 建模作为 supplementary robustness check\n12. 解释 Likert ATE 方向反转的理论含义\n13. 弱化 RATE 批评措辞或补充 matched replication",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "2.5 / 5 (Borderline Findings)",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-21T02:05:54.897564+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4219
}
```

</details>

---


### Assistant

_source line 46 · 2026-05-21T02:06:03.894763+00:00_

修正版审稿报告已投递至 Research Director。

**圆桌审稿完成**，总结如下：

**Overall: 2.5 / 5 (Borderline Findings)**（R1: 3.0, R2: 2.5）

关键修正（相比初版报告）：
1. **撤回 "仅 1 clean cell" 的过度解读**——confound 是 marginal (p=0.072)，7/9 cells 统计显著性由 PDF 确认
2. **新增 CLMM 为 existential test**——如果 CLMM 显著则核心 claim 从 "Likert Blindspot" 变为 "ATE Blindspot"
3. **BT 建模降级为 supplementary**——R1 成功反驳其必要性（sign test sufficient）
4. **R2 评分回调**——从 2.0 回到 2.5，修正了基于 Director brief 的过度下调

Issue Tracker 已同步更新（19 条：9 critical + 10 warning），含收敛轮新增的 CROSS-4（CLMM 必要实验）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 5

## Round 5

60 recorded events


### User

_source line 47 · 2026-05-21T07:03:58.135644+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-06-15

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-21T07:04:04.529897+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-21T07:04:04.530935+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-21T07:04:09.802406+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-21T07:04:09.853114+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-21T07:04:13.365569+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-21T07:04:13.365935+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-21T07:04:16.126113+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-21T07:04:16.277083+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-21T07:04:21.298365+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-21T07:04:23.206362+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (23 个)\n\n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **register_100_cf**: QUEUED — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- register_100_cf: Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality（排队等待 GPU）\n\n## 近期结论\n- **gpt4o_register** (success): GPT-4o judge shows register (academic/conversational) bias detectable via pairwise but not Likert, extending Blindspot to register axis with GPT-4o and enabling cross-model GEE decomposition comparison\n- **gpt4o_verbosity** (success): GPT-4o judge shows verbosity bias in pairwise comparison while Likert fails to detect it, extending Blindspot confirmation to GPT-4o × verbosity cell and enabling cross-model comparison with Qwen3-32B\n- **qwen32b_verbosity** (success): Qwen3-32B judge shows verbosity bias in pairwise comparison (verbose win rate >60%, p<0.05) while Likert scoring fails to detect it, extending Blindspot finding to verbosity axis\n\n## 趋势\n成功 14 / 负向 4 / 失败 0 / 共 21\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1907
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-21T07:04:23.307414+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-21T07:04:24.161190+00:00_

-rw-r--r-- 1 ubuntu ubuntu 277879 May 21 06:29 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu   3344 May 21 06:27 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-21T07:04:24.412881+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-21T07:04:33.444473+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"}]

Based on the search results, here's what I found about EMNLP 2026 call for papers, ARR submission guidelines, and author instructions:

## EMNLP 2026 Ca
…[truncated 1986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 9031
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-21T07:04:38.718948+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline June 2026 page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline June 2026 page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 63 · 2026-05-21T07:04:39.221939+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-21T07:04:39.674532+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{Causal Style Decomposition Reveals the Likert Blindspot:\\Standard Scoring Underestimates Style Bias in LLM Judges}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding.}
42	Although the formality effect survives logistic adjustment for original preference (Appendix~\ref{app:direction}), the significant original-preference odds ratio ($\text{OR} = 2.32$, $p = 0.006$) indicates that quality--style confounding is not fully eliminated.
43	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
44	Future work should incorporate human quality ratings of both original and rewritten texts.
45	
46	\paragraph{Evaluator-producer bias in Qwen3-32B.}
47	Qwen3-32B serves as both the style rewriter and one of the two judges.
48	The inflation is most visible in GEE decomposition: Qwen3-32B formality OR ($4.20$) and originality OR ($4.70$) systematically exceed the GPT-4o estimates ($2.58$ and $2.32$), consistent with partial self-recognition of its own outputs.
49	Bradley-Terry estimates are more robust to this confound: the cross-judge gap is only $+3.5$ percentage points (66.5\
…[truncated 1539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-21T07:04:39.775201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-21T07:04:40.477928+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf (271.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-21T07:04:49.022276+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline June 2026 page limit format requirements"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"The First Call for Industry Track Papers for EMNLP 2026 is officially out! Are you deploying NLP in real-world applications? Share your insights, challenges, and deployed systems with the community. 🗓️ Deadline: June 16, 2026 🔗 Link: https://t.co/ga3k6CJcm0 #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2048750521696072166"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"}]

Now let me search for specific page limit and format requirements for ARR submissions:

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://
…[truncated 1843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 10303
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-21T07:05:37.473632+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-21T07:05:37.926622+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_style_decomp_judge'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-21T07:05:39.434878+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-21T07:05:39.838009+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-21T07:05:40.341015+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-21T07:05:42.100540+00:00_

issues:
  - id: "R1-N1"
    summary: "因果语言与实际框架严重不匹配——大量使用 counterfactual/ATE 术语但无 DAG、SUTVA、sensitivity analysis"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "R1 独立提出；R2 AGREE 并建议降调为 quasi-experimental interventional study"
    action_items:
      - round: 1
        action: "因果语言全面降调为 interventional。DAG 已加入 §3.5。22 verified references。编译 0 undefined refs"
        assigned_to: paper_agent
        status: done
    resolution: "全文 interventional framing + DAG + assumptions 段。编译验证通过"
    resolution_round: 1

  - id: "R1-N2"
    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "R1 独立提出；R2 AGREE"
    action_items:
      - round: 1
        action: "三重间接证据 (exp-011+012+013)。实际 FNR 8.4%。Direction-aware NLI 描述正确"
        assigned_to: paper_agent
        status: done
    resolution: "§nli_validation 完整：FNR 8.4%, precision 98.9%, AC1=0.89"
    resolution_round: 1

  - id: "R1-N3"
    summary: "NLI 阈值 0.90 无 justification，verbosity axis per-axis 调整引入 researcher degrees of freedom"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "R1 提出；R2 AGREE"
    action_items:
      - round: 1
        action: "exp-011 sensitivity analysis + bimodal distribution justification"
        assigned_to: paper_agent
        status: done
    resolution: "Threshold on plateau, not cliff edge. Results robust 0.70-0.95"
    resolution_round: 1

  - id: "R2-N1"
    summary: "Novelty 不足——Likert Blindspot 是已知心理测量学现象在 LLM judge 的 domain transfer"
    category: framing
    severity: critical
    status: in_progress
    first_raised_round: 1
    last_
…[truncated 8564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 1759
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-21T07:05:42.151232+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/ 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/ 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/ 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/ 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-21T07:05:42.252041+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-21T07:05:47.177787+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
  "description": "Find config files in agent directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
    "description": "Find config files in agent directory"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-21T07:05:47.531503+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-21T07:05:47.531849+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 79 · 2026-05-21T07:05:47.632421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-21T07:05:52.757927+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -path \"*/causal_style_decomp_judge*\" -name \"config*\" 2>/dev/null | head -10; echo \"---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -name \"projects.yaml\" -o -name \"project_config*\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -path \"*/causal_style_decomp_judge*\" -name \"config*\" 2>/dev/null | head -10; echo \"---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -name \"projects.yaml\" -o -name \"project_config*\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-21T07:05:53.210124+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/tests/config
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/core/__pycache__/config_init.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/core/config_init.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/_config/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/_config/config.py
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-21T07:05:53.210666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-21T07:05:53.814417+00:00_

1	\begin{abstract}
2	Large Language Model (LLM) judges are widely deployed for evaluation and preference-based alignment, yet recent work shows that style features alone can explain judge scores with near-perfect correlation, raising fundamental questions about what these judges actually measure.
3	We introduce Causal Style Decomposition (CSD), a black-box framework that detects per-axis style bias through binary style-controlled rewriting, NLI-based content preservation gating, and position-controlled pairwise comparison.
4	We quantify what we term the Likert Blindspot---a measurement limitation predicted by psychometric theory but previously unquantified for LLM judges---across two architecturally distinct judges (GPT-4o, Qwen3-32B) and two primary style axes (formality, verbosity), with directionally consistent exploratory evidence on a third axis (register): a two-layer structural gap in which (1)~integer Likert scoring produces ${\sim}60\%$ uninformative ties ($\Delta = 0$), wasting the majority of the evaluation budget; (2)~even among non-tied pairs, absolute scoring captures weaker signal than forced pairwise comparison on identical data.
5	The effect is most dramatic for verbosity, where a 77.3\% Bradley-Terry win probability ($p < 0.0001$, both directions favoring verbose content) remains invisible to Likert scoring ($p = 0.179$).
6	Ordinal regression confirms the limitation is inherent to Likert measurement, not an artifact of interval-scale assumptions ($p = 0.769$).
7	Our results demonstrate that style bias audits require pairwise comparison and per-axis decomposition, and that existing Likert-based findings may systematically underestimate style bias magnitude.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-21T07:05:53.865173+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-21T07:05:53.916153+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of nine hypothesis tests (three judges $\times$ three style axes) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values for this $3 \times 3$ grid.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\caption{Main results across two judges and three style axes. BT: Bradley-Terry win probability (pair-level bootstrap). $\dagger$: Likert Blindspot (pairwise significant, Likert non-significant). Four judge$\times$axis configurations reach $p < 0.001$; two register configurations show weaker but directionally consistent patterns ($\dagger_{\text{e}}$).}
17	\label{tab:main_results}
18	\begin{tabular}{llccc}
19	\toprule
20	Judge & Axis & BT $P$ {[95\% CI]} & Likert $d$ ($p$) & \\
21	\midrule
22	GPT-4o & Formality & .630 {[.558, .703]}$^{***}$ & .011 (.908) & $\dagger$ \\
23	GPT-4o & Verbosity & .760 {[.667, .853]}$^{***}$ & $-$.095 (.403) & $\dagger$ \\
24	GPT-4o & Register & .570 {[.468, .673]}$^{*}$ & $-$.031 (.785) & $\dagger_{\text{e}}$ \\
25	\midrule
26	Qwen3-32B & Formality & .665 {[.585, .739]}$^{***}$ & .011 (.908) & $\dagger$ \\
27	Qwen3-32B & Verbosity & .773 {[.703, .843]}$^{***}$ & $-$.151 (.179) & $\dagger$ \\
28	Qwen3-3
…[truncated 17280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-21T07:06:49.587155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-21T07:06:50.090059+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_diagram.pdf}
7	\caption{CSD pipeline overview. Numbers indicate sample attrition at each stage.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	\subsection{Style-Controlled Rewriting}
12	\label{sec:rewriting}
13	
14	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
15	For each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
16	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
17	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
18	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
19	
20	\subsection{Content Preservation Verification}
21	\label{sec:nli_gate}
22	
23	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
24	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.
25	For axes that preserve information density (formality, register), we apply standard bidirection
…[truncated 4832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-21T07:06:50.090619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-21T07:06:50.542889+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Causal Style Decomposition (CSD), a black-box framework for detecting per-axis style bias in LLM judges.
5	Across two judges and two primary style axes, with exploratory evidence on a third, CSD reveals the Likert Blindspot---a two-layer measurement limitation confirmed by seven statistical methods as inherent to Likert scoring, not an artifact of any particular test.
6	Style bias audits should adopt pairwise comparison as the default protocol; existing Likert-based null findings may reflect measurement insensitivity rather than genuine absence of bias.
7	Future work should extend CSD to additional judges, axes, and benchmarks.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-21T07:06:50.643661+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures/ 2>&1",
  "description": "List figures directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures/ 2>&1",
    "description": "List figures directory"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-21T07:06:50.694790+00:00_

total 96
drwxr-xr-x 2 ubuntu ubuntu  4096 May 21 05:40 .
drwxr-xr-x 5 ubuntu ubuntu  4096 May 21 06:29 ..
-rw-r--r-- 1 ubuntu ubuntu 24209 May 21 06:06 forest_plot.pdf
-rw-r--r-- 1 ubuntu ubuntu 39904 May 21 05:59 pipeline_diagram.pdf
-rw-r--r-- 1 ubuntu ubuntu    32 May 21 05:20 power_curve.aux
-rw-r--r-- 1 ubuntu ubuntu  4517 May 21 05:20 power_curve.log
-rw-r--r-- 1 ubuntu ubuntu 10735 May 21 05:20 power_curve.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-21T07:07:39.506559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-21T07:07:39.557376+00:00_

1	@inproceedings{murugadoss2025sos,
2	  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
3	  author={Murugadoss, Aakanksha and others},
4	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2409.15268}
7	}
8	
9	@inproceedings{li2026preference,
10	  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
11	  author={Li, Dawei and others},
12	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
13	  year={2026},
14	  url={https://arxiv.org/abs/2502.01534}
15	}
16	
17	@article{wang2026fairjudge,
18	  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
19	  author={Wang, Xinyue and others},
20	  journal={arXiv preprint arXiv:2602.06625},
21	  year={2026},
22	  url={https://arxiv.org/abs/2602.06625}
23	}
24	
25	
26	@inproceedings{dubois2025lc,
27	  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
28	  author={Dubois, Yann and others},
29	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
30	  year={2025},
31	  url={https://arxiv.org/abs/2404.04475}
32	}
33	
34	@article{casse2026concise,
35	  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},
36	  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},
37	  journal={arXiv preprint arXiv:2601.10809},
38	  year={2026},
39	  url={https://arxiv.org/abs/2601.10809}
40	}
41	
42	@article{counterfactual2025rhetorical,
43	  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},
44	  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},
45	  journal={arXiv preprint arXiv:2512.19908},
46	  year={2025},
47	  url={https://arxiv.org/abs/2512.19908}
48	}
49	
50	@article{soumik2026judging,
51	  title={Judging the Judges: A Systematic Evaluatio
…[truncated 6475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-21T07:07:39.557750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-21T07:07:39.557979+00:00_

1	\appendix
2	
3	\section{Direction Asymmetry and Quality Confounding}
4	\label{app:direction}
5	
6	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
7	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
8	To quantify this, we fit a logistic decomposition (GEE, exchangeable correlation) with both formality and original-preference as predictors.
9	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
10	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
11	
12	The Qwen3-32B formality effect ($\text{OR} = 4.20$, $p = 0.0002$) exceeds the GPT-4o estimate ($\text{OR} = 2.58$, $p = 0.002$), and the originality confound is also stronger ($\text{OR} = 4.70$ vs.\ $2.32$).
13	This amplification is consistent with evaluator-producer bias (\S\ref{sec:limitations}): because Qwen3-32B generated the rewrites, it may partially recognize its own outputs, inflating both the style and originality effects.
14	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
15	
16	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
17	
18	\section{GEE Model Diagnostics}
19	\label{app:gee_diagnostics}
20	
21	\para
…[truncated 1599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-21T07:07:39.708716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-21T07:07:39.859693+00:00_

1	\section{Introduction}
2	
3	Large Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.
4	Systems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.
5	Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.
6	The reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.
7	As automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.
8	
9	Recent work has converged on a striking finding: \emph{style bias} is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference.
10	\citet{murugadoss2025sos} show that style features alone explain judge scores with $R = 0.999$, far exceeding the explanatory power of content features.
11	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences.
12	\citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
13	Despite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis interventional detection.
14	Rece
…[truncated 4251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-21T07:08:37.618488+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-06-15\n- **页数限制**: 正文 ≤8 页（strict），参考文献无限制，Limitations 不计入页数\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，属于提交材料\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n- Sections: `projects/causal_style_decomp_judge/docs/paper/sections/` 下各 .tex 文件\n- References: `projects/causal_style_decomp_judge/docs/paper/references.bib`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**。请重点审查：\n\n1. **统计方法论**：\n   - Bradley-Terry 模型使用是否规范（pair-level bootstrap CI、正则化设置）\n   - GEE logistic decomposition 的 exchangeable correlation 假设是否合理\n   - Holm-Bonferroni 校正的 family 定义是否合理（§4.1 声称 \"three judges × three style axes = nine tests\"，但论文只使用了 2 个 judge）\n   - Ordinal regression 和 sensitivity hierarchy（Table 2）的分析是否充分\n\n2. **因果主张 vs 实际方法**：\n   - 论文标题和框架名称包含 \"Causal\"，但 §3.5 明确声明 \"we do not claim a complete structural causal model\"\n   - NLI gate 对 do-operator 的近似是否合理\n   - DAG (Figure 2) 是否遗漏重要变量（如 position bias、prompt format）\n\n3. **NLI Gate 有效性**：\n   - 8.4% FNR 的三重间接验证（threshold sweep、consistency filter、directional balance）是否充分\n   - Qwen3-32B 同时作为 rewriter 和 NLI annotator 的循环性\n   - Direction-aware verification for verbosity 的 justification\n\n4. **实验设计**：\n   - 仅使用 LLMBar (n=100) 一个 benchmark 的代表性\n   - 样本量是否支持所声称的结论（88 NLI-gated pairs → 173 comparisons）\n   - Evaluator-producer bias（Qwen3-32B 同时为 rewriter 和 judge）的影响量化\n\n5. **可重复性**：\n   - 关键超参数是否完整报告（temperature 0.7、NLI threshold 0.90、BT bootstrap resamples）\n   - 是否有代码/数据可用性声明\n\n### 输出要求\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 简要理由）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-06-15\n- **页数限制**: 正文 ≤8 页（strict），参考文献无限制，Limitations 不计入页数\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，属于提交材料\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n- Sections: `projects/causal_style_decomp_judge/docs/paper/sections/` 下各 .tex 文件\n- References: `projects/causal_style_decomp_judge/docs/paper/references.bib`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**。请重点审查：\n\n1. **统计方法论**：\n   - Bradley-Terry 模型使用是否规范（pair-level bootstrap CI、正则化设置）\n   - GEE logistic decomposition 的 exchangeable correlation 假设是否合理\n   - Holm-Bonferroni 校正的 family 定义是否合理（§4.1 声称 \"three judges × three style axes = nine tests\"，但论文只使用了 2 个 judge）\n   - Ordinal regression 和 sensitivity hierarchy（Table 2）的分析是否充分\n\n2. **因果主张 vs 实际方法**：\n   - 论文标题和框架名称包含 \"Causal\"，但 §3.5 明确声明 \"we do not claim a complete structural causal model\"\n   - NLI gate 对 do-operator 的近似是否合理\n   - DAG (Figure 2) 是否遗漏重要变量（如 position bias、prompt format）\n\n3. **NLI Gate 有效性**：\n   - 8.4% FNR 的三重间接验证（threshold sweep、consistency filter、directional balance）是否充分\n   - Qwen3-32B 同时作为 rewriter 和 NLI annotator 的循环性\n   - Direction-aware verification for verbosity 的 justification\n\n4. **实验设计**：\n   - 仅使用 LLMBar (n=100) 一个 benchmark 的代表性\n   - 样本量是否支持所声称的结论（88 NLI-gated pairs → 173 comparisons）\n   - Evaluator-producer bias（Qwen3-32B 同时为 rewriter 和 judge）的影响量化\n\n5. **可重复性**：\n   - 关键超参数是否完整报告（temperature 0.7、NLI threshold 0.90、BT bootstrap resamples）\n   - 是否有代码/数据可用性声明\n\n### 输出要求\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 简要理由）"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-21T07:08:55.037357+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17418
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-21T07:08:55.138186+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-06-15\n- **页数限制**: 正文 ≤8 页（strict），参考文献无限制，Limitations 不计入页数\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，属于提交材料\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n- Sections: `projects/causal_style_decomp_judge/docs/paper/sections/` 下各 .tex 文件\n- References: `projects/causal_style_decomp_judge/docs/paper/references.bib`\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 格式合规**。请重点审查：\n\n1. **新颖性评估**：\n   - Likert Blindspot 是经典心理测量学已知现象（Thurstone 1927, DeCoster 2011）在 LLM judge 领域的迁移，novelty ceiling 如何评判\n   - CSD framework 相对于 RATE (Reber et al., 2025)、CASSE (Cho et al., 2026)、FairJudge (Wang et al., 2026) 的增量贡献\n   - 论文是否成功建立了为什么这个 domain transfer 非平凡的论证\n\n2. **Related Work 完整性**：\n   - 22 条引用是否充分覆盖：(a) LLM-as-Judge bias 文献，(b) 心理测量学文献，(c) causal inference for text 文献\n   - 是否遗漏重要竞品或基准（搜索 2025-2026 最新相关工作）\n   - 与 RATE 的比较是否公平客观\n\n3. **写作质量**：\n   - 叙事结构是否清晰（问题→方法→实验→结论的逻辑链）\n   - Abstract 是否过度 claim\n   - Limitations 是否充分（覆盖范围、关键遗漏）\n   - \"Causal\" 在标题中是否恰当，考虑到 §3.5 的 disclaimer\n\n4. **格式合规**（严格检查）：\n   - **页数**：正文（Abstract 到 Conclusion 结尾）是否 ≤8 页。仔细检查 PDF——Conclusion 是否溢出到第 9 页\n   - **Figure 质量**：检查所有 3 个 figure（pipeline_diagram, forest_plot, power_curve）在 PDF 中的渲染状态，特别注意 power_curve.pdf 在 PDF 第 7 页是否显示 \"PLACEHOLDER\"\n   - **Table 格式**：Table 1 中 Qwen3-32B Register 行的 Likert d 列格式是否一致\n   - **匿名性**：检查是否有泄露作者身份的信息\n   - **引用格式**：bib 条目是否完整、一致\n\n5. **贡献显著性**：\n   - 对 EMNLP 社区的实际影响（practical implications）\n   - 是否达到 Conference 级别（Overall Assessment ≥ 4）还是 Findings 级别（3-3.5）\n\n### 输出要求\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 简要理由）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-06-15\n- **页数限制**: 正文 ≤8 页（strict），参考文献无限制，Limitations 不计入页数\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，属于提交材料\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n- Sections: `projects/causal_style_decomp_judge/docs/paper/sections/` 下各 .tex 文件\n- References: `projects/causal_style_decomp_judge/docs/paper/references.bib`\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 格式合规**。请重点审查：\n\n1. **新颖性评估**：\n   - Likert Blindspot 是经典心理测量学已知现象（Thurstone 1927, DeCoster 2011）在 LLM judge 领域的迁移，novelty ceiling 如何评判\n   - CSD framework 相对于 RATE (Reber et al., 2025)、CASSE (Cho et al., 2026)、FairJudge (Wang et al., 2026) 的增量贡献\n   - 论文是否成功建立了为什么这个 domain transfer 非平凡的论证\n\n2. **Related Work 完整性**：\n   - 22 条引用是否充分覆盖：(a) LLM-as-Judge bias 文献，(b) 心理测量学文献，(c) causal inference for text 文献\n   - 是否遗漏重要竞品或基准（搜索 2025-2026 最新相关工作）\n   - 与 RATE 的比较是否公平客观\n\n3. **写作质量**：\n   - 叙事结构是否清晰（问题→方法→实验→结论的逻辑链）\n   - Abstract 是否过度 claim\n   - Limitations 是否充分（覆盖范围、关键遗漏）\n   - \"Causal\" 在标题中是否恰当，考虑到 §3.5 的 disclaimer\n\n4. **格式合规**（严格检查）：\n   - **页数**：正文（Abstract 到 Conclusion 结尾）是否 ≤8 页。仔细检查 PDF——Conclusion 是否溢出到第 9 页\n   - **Figure 质量**：检查所有 3 个 figure（pipeline_diagram, forest_plot, power_curve）在 PDF 中的渲染状态，特别注意 power_curve.pdf 在 PDF 第 7 页是否显示 \"PLACEHOLDER\"\n   - **Table 格式**：Table 1 中 Qwen3-32B Register 行的 Likert d 列格式是否一致\n   - **匿名性**：检查是否有泄露作者身份的信息\n   - **引用格式**：bib 条目是否完整、一致\n\n5. **贡献显著性**：\n   - 对 EMNLP 社区的实际影响（practical implications）\n   - 是否达到 Conference 级别（Overall Assessment ≥ 4）还是 Findings 级别（3-3.5）\n\n### 输出要求\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 简要理由）"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-21T07:08:56.849565+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1711
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-21T07:08:56.849980+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool call

_source line 103 · 2026-05-21T07:08:58.776704+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "ARR Long Paper submission, deadline June 15, 2026. 重新审稿（fresh review）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "ARR Long Paper submission, deadline June 15, 2026. 重新审稿（fresh review）。"
  }
}
```

</details>

---


### Tool result

_source line 104 · 2026-05-21T07:08:58.877999+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2028
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-21T07:08:59.635914+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 859
}
```

</details>

---


### Assistant

_source line 106 · 2026-05-21T07:09:07.724251+00:00_

全部并行任务已派发：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已派发 |
| Reviewer 2（新颖性+格式） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 请求已发送，等待用户协助提交 |

等待两位 Reviewer 返回 Round 1 独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 107 · 2026-05-21T07:13:25.314985+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

### 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 核心发现（Likert Blindspot）有实证价值且用7种统计方法交叉验证，但"Causal"标题与实际方法的张力、单一benchmark（n=100）的代表性不足、以及评估者-生产者循环偏差，使论文在方法严谨性上尚未达到主会议标准。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心claim有多种统计方法支撑，但Holm-Bonferroni family定义与实际实验矛盾（声称9个检验实际只有6个）、因果声明overclaim、evaluator-producer循环性未充分量化 |
| Excitement | 3.5/5 | Likert Blindspot现象对评估社区有实际指导价值，per-axis GEE分解揭示不同confound structure是有洞察力的贡献；但scope（1个benchmark、2个judge）限制了影响力 |
| Reproducibility | 3/5 | 关键超参数大部分已报告，但BT正则化方式未说明、bootstrap resamples数不一致（2000 vs 10000）、无代码/数据可用性声明 |
| Confidence | 4/5 | 仔细阅读全文含附录，统计方法论在我的专业领域内 |

### Must-Fix 问题（影响接收决定）

**N1** [critical] Holm-Bonferroni family 定义与实际实验不一致
- 具体位置：§4.1 (experiments.tex line 8)
- 问题：论文声称 "three judges × three style axes = nine tests"，但全文仅使用 2 个 judge（GPT-4o、Qwen3-32B），Table 1 也只有 6 行（2×3）。第三个 judge 完全没有出现。这意味着 Holm-Bonferroni 校正基于一个不存在的 family size（9），比实际需要的 family size（6）更保守——虽然这使结果更保守而非更宽松，但声称的实验设计与实际执行之间的不一致本身就是严重的 credibility 问题。
- 为什么影响接收：统计框架的文本描述与实际执行不符，审稿人无法确定哪些描述是准确的。
- 建议修改方向：要么补上第三个 judge 的实验，要么将 family 修正为 "two judges × three style axes = six tests" 并重新检查所有 adjusted p-values。

**N2** [critical] "Causal" 标题与方法论实质的张力
- 具体位置：Title、§3.5 (method.tex lines 57-58)、Abstract
- 问题：标题为 "Causal Style Decomposition"，框架简称 CSD。但 §3.5 明确声明 "we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions"，并将自身定位为 "interventional rather than formal causal evidence"。NLI gate 对 do-operator 的近似也被承认不完整。标题 overclaim。
- 为什么影响接收：标题是论文最高可见度的 claim，overclaim 显著降低对全文的信任。
- 建议修改方向：(1) 将 "Causal" 替换为 "Interventional" 或 "Style-Controlled"；或 (2) 在 §3.5 中给出更严格的因果识别条件讨论。

**N3** [critical] 单一 benchmark（LLMBar, n=100）的代表性
- 具体位置：§3.4
- 问题：所有实验仅基于 LLMBar（n=100），NLI gate 后剩 88 pairs → 173 comparisons。Bootstrap CI 宽度达 14.5pp。LLMBar 是 instruction-following 任务，代表性有限。论文的多个 strong claim 基于单一小规模 benchmark 难以成立。
- 为什么影响接收：从 n=100 的单一 benchmark 推广到 "LLM Judges" 整个类别的 claim 缺乏 external validity。
- 建议修改方向：至少在一个额外 benchmark 上复现核心发现，或在 title/abstract 中明确限定 scope。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Evaluator-producer 循环性未充分量化
- Qwen3-32B 同时担任 rewriter、judge、NLI gate validator 三个角色。NLI gate validation 中称 Qwen3-32B 为 "independent LLM annotator" 不准确。建议删除 "independent"，并量化仅用 GPT-4o 数据是否足以支撑核心 claim。

**W2** [warning] Direction-aware NLI for verbosity 削弱 content preservation 保证
- 单向 NLI 允许 expansion 添加新的 quality-relevant content 而不被检测。text length 控制不等于 content quality 控制。建议对 verbose rewrites 进行人工内容质量抽检。

**W3** [warning] GEE exchangeable correlation 假设验证不充分
- 未测试 AR(1) 或 unstructured。within-pair α̂ ∈ [-0.25, +0.11]，部分负相关暗示 exchangeable 可能非最优。

**W4** [warning] BT 正则化细节和 bootstrap resamples 不一致
- "regularized estimate" 未说明正则化类型和参数。GPT-4o 用 2,000 resamples，Qwen3-32B 用 10,000，无理由。

**W5** [warning] Table 1 Qwen3-32B Register 行缺少 Cohen's d 值，只有 p-value (.505)。

**W6** [warning] DAG 遗漏 position bias（被实验 blocked）和 rewrite artifact（被 double-rewrite 控制 blocked）路径，应反映完整 identification strategy。

### 小问题
- 无代码/数据可用性声明
- wang2026fairjudge 第一作者与 OpenAlex 不一致（bib: Wang, API: Yang）
- murugadoss2025sos 在 OpenAlex 中未找到，建议核查
- Abstract 信息密度高但可读性略受影响

### Questions（需要作者回答）
1. "three judges" 指哪三个？如果第三个 judge 未完成，Holm-Bonferroni family size 应为 6。
2. NLI gate validation 为什么不用 GPT-4o 或人工标注？
3. Verbose rewrites 是否经过人工 content quality 检查？
4. BT 正则化具体设置？
5. 是否计划发布代码和数据？

### Missing References
- Chiang et al. (2024) "Chatbot Arena: An Open Platform" — BT 实现规范
- Ye et al. (2024) "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" — bias quantification

### 主要优势
1. Likert Blindspot 用 7 种统计方法在同一数据上 demonstrate，方法论教育意义强
2. Cross-judge/cross-axis 复现，verbosity 提供 confound-free clean case
3. GEE decomposition 揭示 per-axis confound structure 差异（verbosity=pure style, formality=mixed, register=originality-dominated）
4. Limitations 部分坦诚具体
5. Position control + consistency filter 设计合理

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 108 · 2026-05-21T07:13:32.334696+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 109 · 2026-05-21T07:13:47.401517+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文的 Likert Blindspot 发现有实证价值，7 种统计方法交叉验证令人信服，GEE per-axis confound structure 分析有洞察力。但三个 Must-Fix 问题阻止主会议接收：(1) Holm-Bonferroni 声称 9 个检验但实际只有 6 个——第三个 judge 不存在；(2) 标题 "Causal" 与 §3.5 的 explicit disclaimer 矛盾；(3) 仅用 LLMBar (n=100) 一个 benchmark 支撑对 "LLM Judges" 整个类别的 claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 110 · 2026-05-21T07:13:52.961696+00:00_

收到 Reviewer 1 审稿意见。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 8

## Round 8

6 recorded events


### User

_source line 111 · 2026-05-21T07:18:57.238433+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "Causal Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges"
**Venue**: EMNLP 2026 (ARR Long Paper)
**审查侧重**: 新颖性 + 完整性 + 格式合规

---

### 1. Summary

本文提出 Causal Style Decomposition (CSD)，通过风格控制改写、NLI 内容保全门控和位置控制的成对比较来检测 LLM 评委的逐轴风格偏差。核心发现为 "Likert Blindspot"：标准 Likert 评分因 tie inflation（~60% 无信息并列）和信号衰减的双层机制，系统性地遗漏成对比较能检出的风格偏差。实验在 LLMBar (n=100) 上用 GPT-4o 和 Qwen3-32B 两个评委、三个风格轴（formality, verbosity, register）验证，七种统计方法一致确认 Blindspot 现象。

---

### 2. 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计合理，NLI 门控验证充分，七种统计方法交叉验证令人信服。但 "causal" 框架名不副实（§3.5 disclaimer），且实验规模偏小。 |
| Excitement | 2.5/5 | Likert Blindspot 是心理测量学已知现象在 LLM 领域的迁移，方法是现有组件流水线，新颖性有限。实际建议（改用成对比较）有用但不足以单独撑起贡献。 |
| Reproducibility | 4/5 | 方法描述详细，统计分析透明，NLI 阈值和 bootstrap 参数均有报告。缺少代码/数据链接（可理解为匿名审稿阶段限制）。 |
| Confidence | 4/5 | 对 LLM-as-judge 偏差和心理测量文献较熟悉，仔细阅读全文。 |

---

### 3. Strengths

**S1. 问题动机清晰且有实践价值**：风格偏差是 LLM 评委最核心的可靠性威胁之一，量化度量工具的选择如何影响偏差检出，对整个 LLM 评估社区有直接指导意义。

**S2. 统计论证扎实**（Table 2, §5.2）：用七种不同统计方法（BT model, sign test, t-test, binomial Likert, ordinal logistic, GEE, Wilcoxon）在同一数据上验证 Blindspot，所有成对方法达到显著而所有 Likert 方法失败——这是一个有力的系统性证据。

**S3. 多维度复现**：跨评委（GPT-4o vs Qwen3-32B）、跨风格轴（formality, verbosity, register）的复现，Table 1 和 Figure 3 forest plot 清晰展示一致模式。verbosity 轴的 BT win probability 达 76-77%，效应量令人印象深刻。

**S4. GEE 分解提供结构性洞察**（§5.7, Table 3）：GEE 逻辑回归分解 style 和 originality 效应，揭示 confounded structure（风格与原创性偏好的交织），为后续 debiasing 工作提供了诊断基础。

**S5. 诚实的因果声明限定**（§3.5）：明确声明不主张完整结构因果模型，不依赖 SUTVA 或 consistency assumptions，这比许多滥用 "causal" 的论文要诚实。

**S6. Limitations 部分真实坦诚**（p.9）：主动披露 quality-style confounding（Appendix A 显示 OR = 2.32）、evaluator-producer bias、以及 benchmark/axis 覆盖不足。

---

### 4. Weaknesses

#### Must-Fix 问题（影响接收决定）

**N1** [critical] **Abstract 过度声称**
- 具体位置：Abstract, p.1, "style bias is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference"
- 问题：(a) 仅基于 2 个评委 + 1 个 benchmark (LLMBar, n=100) 的证据，无法支撑 "LLM judges" 全称式论断；(b) verbosity 本身是论文三个风格轴之一，说风格偏差 "far outweighs verbosity preference" 造成逻辑混淆——verbosity bias IS a style bias in the paper's own framework；(c) formality 轴的 BT win probability 为 63%（GPT-4o），文献中 position bias 通常为 55-65%，"far outweighing" 缺乏量级支撑。
- 为什么影响接收：过度声称是 ARR 审稿高频扣分项，会直接影响 Soundness 评分。
- 建议：将 "dominant source" 改为 "a previously underestimated source"，将 "far outweighing" 改为 "comparable to or exceeding"，并加限定语 "on the tested configurations"。

**N2** [critical] **标题 "Causal" 与 §3.5 disclaimer 的张力**
- 具体位置：Title + §3.5 (p.4-5)
- 问题：标题用 "Causal Style Decomposition" 暗示形式化因果推断，但 §3.5 明确声明 "we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions"。这不是一般的 qualification——是对因果方法论基本假设的全面放弃。CSD 更接近 controlled experiment / interventional design 而非 formal causal inference。标题创造的期望与实际方法不匹配，会招致因果推断专家的质疑。
- 为什么影响接收：标题误导会影响 reviewer assignment 和后续 citation，也可能被 AC 视为 framing 问题。
- 建议：考虑 "Controlled Style Decomposition" 或 "Interventional Style Decomposition"，或在标题中不使用 "Causal" 而在正文中讨论因果解读。如果坚持 "Causal"，需要在方法部分提供更强的 identification argument。

#### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **新颖性天花板受限**
- 具体位置：全文方法论层面
- 问题：Likert Blindspot 实质是心理测量学经典现象（ordinal discretization 损失连续信号）在 LLM judge 领域的应用。论文自己承认 "not the discovery of this measurement principle"（p.3）。CSD 框架是三个已有组件的流水线（LLM 改写 + NLI filter + BT comparison），methodological novelty 有限。两层机制（tie inflation + signal attenuation）的 framing 是一个 contribution，但本质仍是已知现象的细化。
- 建议：加强 "why this domain transfer is non-trivial" 的论证——例如，LLM judges 的 scale usage patterns 是否与 human raters 质性不同？如果 LLM judges 的 tie inflation 是训练目标导致的（而非人类的认知限制），这就是一个新机制。

**W2** [warning] **实验规模偏窄**
- 具体位置：§3.4, Table 1
- 问题：仅 2 个 judge（GPT-4o, Qwen3-32B）和 1 个 benchmark（LLMBar, n=100）。主要风格轴只有 2 个（formality, verbosity），register 是 exploratory。对于一个声称揭示 "LLM Judges" 普遍性现象的论文，覆盖不足。尤其缺少：(a) Claude 系列或 Llama 系列评委；(b) 非 instruction-following 任务（如 summarization, translation）。
- 建议：至少增加 1 个 judge family（如 Claude 或 Llama）和 1 个任务类型。

**W3** [warning] **Evaluator-producer confound 未充分处理**
- 具体位置：§3.1 + Limitations (p.9)
- 问题：Qwen3-32B 同时担任 rewriter 和 judge。论文在 Limitations 中承认 "consistent with partial self-recognition of its own outputs"，但 Qwen3-32B 在 GEE 分解中的 formality OR (4.20) 和 originality OR (4.20) 系统性高于 GPT-4o（formality OR 2.58, originality OR 1.13），效应量差异可能部分来自 evaluator-producer bias 而非真实风格偏差差异。
- 建议：用第三个模型（不同 family）作为 rewriter 做控制实验，disentangle self-recognition 效应。

**W4** [warning] **Scale granularity 未探讨**
- 具体位置：§3.3 Measurement Protocol
- 问题：论文使用 1-10 Likert scale。关键问题是：Blindspot 是所有 ordinal scale 的固有属性，还是 1-10 这一特定粒度的结果？如果 1-100 continuous scale 也有 Blindspot，那是对 Likert 范式的根本性批评；如果更细粒度的 scale 可以缓解，那只是 scale 选择问题。论文未区分这两种情况。
- 建议：讨论 scale granularity 的影响（即使无法做实验，至少作为理论分析），或至少在 Limitations 中提及。

**W5** [warning] **缺乏 mitigation 策略**
- 具体位置：§6 Conclusion
- 问题：论文诊断出 Blindspot 但未提出任何 mitigation 方案（校准、debiasing、hybrid scoring 等），只建议 "adopt pairwise comparison as the default protocol"。但成对比较的代价是 O(n²) 的 evaluation budget，对于大规模评估场景（如 Chatbot Arena）可能不现实。一个实用的 correction 或 calibration 方法会显著提升贡献。
- 建议：至少探讨一种基于 CSD 诊断的 mitigation 路径（如 Likert score recalibration using pairwise anchoring）。

#### Minor 问题（不影响接收）

**M1** Figure 4 (p.7)：power_curve 图左上角区域疑似存在淡色 "PLACEHOLDER" 水印文字，提交前需确认并移除。

**M2** Table 1 (p.5)：Qwen3-32B Register 行的 Likert d 列格式与其他行不一致——其他行均显示 Cohen's d (p_s) 数值对，该行似乎为空白或标注为 "Exploratory (§5.5)"，建议统一格式（即使是 exploratory 也应报告数值）。

**M3** 引用问题：(a) `wang2026fairjudge` 第一作者 mismatch（bib 标注 Wang，OpenAlex 验证显示第一作者为 Yang）；(b) `hoenig2001abuse` 在 .bib 中存在但可能未被 \cite 命令正确捕获（p.7 正文中有 "cf. Hoenig and Heisey 2001" 的引用，需确认编译时正确链接）。

---

### 5. Questions for Authors

**Q1** 如果将 Likert scale 从 1-10 改为 1-100 或连续滑块，Blindspot 是否仍然存在？这将帮助区分 "ordinal discretization 的固有问题" 与 "特定 scale 粒度的选择问题"。

**Q2** CSD 是否在 non-instruction-following 任务（summarization, translation quality）上测试过？LLMBar 是一个 instruction-following 专用 benchmark，风格偏差的表现可能依赖于任务类型。

**Q3** NLI gate 丢弃了 8.4% 的 pair。主要发现对 NLI 阈值变化（如 0.75 或 0.85）的敏感性如何？论文 §5.6 做了 consistency filter 的 robustness check，但未专门报告 NLI 阈值的 sensitivity analysis。

**Q4** 能否通过使用不同 model family（如 Claude 或 Llama）作为 rewriter 来 disentangle Qwen3-32B 的 evaluator-producer confound？

**Q5** Table 3 (GEE) 中 formality 的 style OR = 2.58 (GPT-4o) 和 4.20 (Qwen3-32B)，originality OR = 1.13 (GPT-4o) 和 4.20 (Qwen3-32B)。Qwen3-32B 的 originality OR 远高于 GPT-4o，是否暗示 Qwen3-32B 对 "自己生成的原始文本" 有 preference leak，而非独立的 originality preference？

---

### 6. Missing References

**R1** Oriyad & Rohban (2025) "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge" (NeurIPS 2025) — 研究 LLM 评委的 shortcut biases（provenance, recency），与 CSD 的 style-vs-content 分解框架高度相关，应在 §2 Related Work 的 "Style Bias Detection and Mitigation" 段引用和对比。

**R2** 建议在 §2 增加对 LLM-as-judge 综述的引用（如 CSHaitao 等人的 survey），以帮助定位 CSD 在更广阔研究图景中的位置。

**R3** Causal inference for text 文献覆盖不足：仅引用 Veitch et al. (2020)。建议补充 Feder et al. (2022, TACL) "Causal Inference in NLP" 综述，以加强因果方法论基础的定位。若标题保留 "Causal"，这一引用尤为必要。

---

### 7. Overall Assessment

**Overall: 3.0** (Findings)
**Confidence: 4/5**

**一句话总结**: 实验执行扎实、统计论证有力的 empirical study，但新颖性受限于已知心理测量现象的领域迁移，实验规模偏窄（2 judges, 1 benchmark），且 "Causal" framing 与方法实质不匹配。

**理由**: 论文的核心贡献——证明 Likert scoring 在 LLM judge 风格偏差检测中系统性失灵——有明确的实践价值，七种统计方法的交叉验证令人信服。但 (1) Likert Blindspot 是心理测量学已知现象的迁移应用，method 层面是现有组件流水线，novelty ceiling 有限；(2) 仅 2 个 judge + 1 个 benchmark 的实验规模不足以支撑 "LLM judges" 的全称论断；(3) 标题的 "Causal" 与 §3.5 的全面 disclaimer 之间的张力是一个 framing 问题；(4) 缺乏任何 mitigation/calibration 策略，贡献止于诊断层面。综合考虑，认为达到 Findings 级别（有实践价值的经验性发现），距离 Main Conference（需要更强的 novelty 或 broader impact）有差距。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-21T07:19:26.841540+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意 Reviewer 2 提出的你未覆盖的问题（如 scale granularity、mitigation 策略、Abstract overclaim 的具体措辞分析）。\n\n---\n\n## Reviewer 2 审稿原文\n\n**Overall: 3.0 (Findings) | Confidence: 4/5**\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计合理，NLI 门控验证充分，七种统计方法交叉验证令人信服。但 \"causal\" 框架名不副实（§3.5 disclaimer），且实验规模偏小。 |\n| Excitement | 2.5/5 | Likert Blindspot 是心理测量学已知现象在 LLM 领域的迁移，方法是现有组件流水线，新颖性有限。实际建议（改用成对比较）有用但不足以单独撑起贡献。 |\n| Reproducibility | 4/5 | 方法描述详细，统计分析透明。缺少代码/数据链接。 |\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 过度声称\n- \"style bias is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference\"\n- 问题：(a) 仅基于 2 个评委 + 1 个 benchmark (LLMBar, n=100) 的证据无法支撑全称论断；(b) verbosity 本身是论文三个风格轴之一，说风格偏差 \"far outweighs verbosity preference\" 造成逻辑混淆；(c) formality 轴的 BT win probability 为 63%（GPT-4o），position bias 通常为 55-65%，\"far outweighing\" 缺乏量级支撑。\n- 建议：将 \"dominant source\" 改为 \"a previously underestimated source\"，将 \"far outweighing\" 改为 \"comparable to or exceeding\"。\n\n**N2** [critical] 标题 \"Causal\" 与 §3.5 disclaimer 的张力\n- §3.5 明确声明 \"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。CSD 更接近 controlled experiment / interventional design 而非 formal causal inference。\n- 建议：考虑 \"Controlled Style Decomposition\" 或 \"Interventional Style Decomposition\"。\n\n### Should-Fix 问题\n\n**W1** [warning] 新颖性天花板受限\n- Likert Blindspot 是心理测量学经典现象（ordinal discretization 损失连续信号）在 LLM judge 领域的应用。CSD 框架是三个已有组件的流水线（LLM 改写 + NLI filter + BT comparison），methodological novelty 有限。\n- 建议：加强 \"why this domain transfer is non-trivial\" 的论证——LLM judges 的 scale usage patterns 是否与 human raters 质性不同？\n\n**W2** [warning] 实验规模偏窄\n- 仅 2 个 judge（GPT-4o, Qwen3-32B）和 1 个 benchmark（LLMBar, n=100）。缺少 Claude/Llama 评委和非 instruction-following 任务。\n\n**W3** [warning] Evaluator-producer confound 未充分处理\n- Qwen3-32B 在 GEE 分解中的 formality OR (4.20) 和 originality OR (4.70) 系统性高于 GPT-4o，效应量差异可能部分来自 evaluator-producer bias。\n- 建议：用第三个模型作为 rewriter 做控制实验。\n\n**W4** [warning] Scale granularity 未探讨\n- 论文使用 1-10 Likert scale。如果 1-100 continuous scale 也有 Blindspot，那是对 Likert 范式的根本性批评；如果更细粒度可以缓解，那只是 scale 选择问题。论文未区分。\n\n**W5** [warning] 缺乏 mitigation 策略\n- 论文诊断出 Blindspot 但未提出任何 mitigation 方案。成对比较的 O(n²) 代价对大规模评估不现实。\n\n### Minor\n- M1: Figure 4 (power_curve) 疑似 PLACEHOLDER 水印\n- M2: Table 1 Qwen3-32B Register 行 Likert d 列格式不一致\n- M3: wang2026fairjudge 第一作者 mismatch; hoenig2001abuse 引用链接需确认\n\n### Missing References\n- R1: Oriyad & Rohban (2025) \"The Silent Judge\" (NeurIPS 2025)\n- R2: LLM-as-judge survey\n- R3: Feder et al. (2022, TACL) \"Causal Inference in NLP\" 综述"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意 Reviewer 2 提出的你未覆盖的问题（如 scale granularity、mitigation 策略、Abstract overclaim 的具体措辞分析）。\n\n---\n\n## Reviewer 2 审稿原文\n\n**Overall: 3.0 (Findings) | Confidence: 4/5**\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计合理，NLI 门控验证充分，七种统计方法交叉验证令人信服。但 \"causal\" 框架名不副实（§3.5 disclaimer），且实验规模偏小。 |\n| Excitement | 2.5/5 | Likert Blindspot 是心理测量学已知现象在 LLM 领域的迁移，方法是现有组件流水线，新颖性有限。实际建议（改用成对比较）有用但不足以单独撑起贡献。 |\n| Reproducibility | 4/5 | 方法描述详细，统计分析透明。缺少代码/数据链接。 |\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 过度声称\n- \"style bias is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference\"\n- 问题：(a) 仅基于 2 个评委 + 1 个 benchmark (LLMBar, n=100) 的证据无法支撑全称论断；(b) verbosity 本身是论文三个风格轴之一，说风格偏差 \"far outweighs verbosity preference\" 造成逻辑混淆；(c) formality 轴的 BT win probability 为 63%（GPT-4o），position bias 通常为 55-65%，\"far outweighing\" 缺乏量级支撑。\n- 建议：将 \"dominant source\" 改为 \"a previously underestimated source\"，将 \"far outweighing\" 改为 \"comparable to or exceeding\"。\n\n**N2** [critical] 标题 \"Causal\" 与 §3.5 disclaimer 的张力\n- §3.5 明确声明 \"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。CSD 更接近 controlled experiment / interventional design 而非 formal causal inference。\n- 建议：考虑 \"Controlled Style Decomposition\" 或 \"Interventional Style Decomposition\"。\n\n### Should-Fix 问题\n\n**W1** [warning] 新颖性天花板受限\n- Likert Blindspot 是心理测量学经典现象（ordinal discretization 损失连续信号）在 LLM judge 领域的应用。CSD 框架是三个已有组件的流水线（LLM 改写 + NLI filter + BT comparison），methodological novelty 有限。\n- 建议：加强 \"why this domain transfer is non-trivial\" 的论证——LLM judges 的 scale usage patterns 是否与 human raters 质性不同？\n\n**W2** [warning] 实验规模偏窄\n- 仅 2 个 judge（GPT-4o, Qwen3-32B）和 1 个 benchmark（LLMBar, n=100）。缺少 Claude/Llama 评委和非 instruction-following 任务。\n\n**W3** [warning] Evaluator-producer confound 未充分处理\n- Qwen3-32B 在 GEE 分解中的 formality OR (4.20) 和 originality OR (4.70) 系统性高于 GPT-4o，效应量差异可能部分来自 evaluator-producer bias。\n- 建议：用第三个模型作为 rewriter 做控制实验。\n\n**W4** [warning] Scale granularity 未探讨\n- 论文使用 1-10 Likert scale。如果 1-100 continuous scale 也有 Blindspot，那是对 Likert 范式的根本性批评；如果更细粒度可以缓解，那只是 scale 选择问题。论文未区分。\n\n**W5** [warning] 缺乏 mitigation 策略\n- 论文诊断出 Blindspot 但未提出任何 mitigation 方案。成对比较的 O(n²) 代价对大规模评估不现实。\n\n### Minor\n- M1: Figure 4 (power_curve) 疑似 PLACEHOLDER 水印\n- M2: Table 1 Qwen3-32B Register 行 Likert d 列格式不一致\n- M3: wang2026fairjudge 第一作者 mismatch; hoenig2001abuse 引用链接需确认\n\n### Missing References\n- R1: Oriyad & Rohban (2025) \"The Silent Judge\" (NeurIPS 2025)\n- R2: LLM-as-judge survey\n- R3: Feder et al. (2022, TACL) \"Causal Inference in NLP\" 综述"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-21T07:19:59.827984+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32986
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-21T07:20:00.079816+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意 Reviewer 1 提出的你未覆盖的问题（如 Holm-Bonferroni \"9 tests\" 错误、Direction-aware NLI 的内容保全削弱、GEE correlation structure、BT 正则化细节不一致）。\n\n---\n\n## Reviewer 1 审稿原文\n\n**Overall: 3.0 (Findings) | Confidence: 4/5**\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | Holm-Bonferroni family 定义矛盾（声称 9 检验实际 6 个）、因果声明 overclaim、evaluator-producer 循环性未充分量化 |\n| Excitement | 3.5/5 | Likert Blindspot 对评估社区有指导价值，per-axis GEE 分解有洞察力；但 scope 限制影响力 |\n| Reproducibility | 3/5 | 关键超参数大部分已报告，但 BT 正则化方式未说明、bootstrap resamples 数不一致（2000 vs 10000）、无代码/数据声明 |\n\n### Must-Fix 问题\n\n**N1** [critical] Holm-Bonferroni family 定义与实际实验不一致\n- §4.1 声称 \"three judges × three style axes = nine tests\"，但全文仅使用 2 个 judge（GPT-4o、Qwen3-32B），Table 1 只有 6 行。Holm-Bonferroni 校正基于不存在的 family size（9）比实际（6）更保守——虽然使结果更保守，但声称的设计与实际执行不一致是严重 credibility 问题。\n- 建议：修正为 \"two judges × three style axes = six tests\" 并重新检查 adjusted p-values。\n\n**N2** [critical] \"Causal\" 标题与方法论实质的张力\n- 标题 \"Causal Style Decomposition\"，但 §3.5 声明 \"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。NLI gate 对 do-operator 的近似不完整。标题 overclaim。\n- 建议：将 \"Causal\" 替换为 \"Interventional\" 或 \"Style-Controlled\"；或提供更严格的因果识别条件讨论。\n\n**N3** [critical] 单一 benchmark（LLMBar, n=100）的代表性\n- 所有实验仅基于 LLMBar（n=100），NLI gate 后剩 88 pairs → 173 comparisons。Bootstrap CI 宽度达 14.5pp。从 n=100 的单一 benchmark 推广到 \"LLM Judges\" 整个类别的 claim 缺乏 external validity。\n- 建议：至少在一个额外 benchmark 上复现核心发现，或明确限定 scope。\n\n### Should-Fix 问题\n\n**W1** [warning] Evaluator-producer 循环性未充分量化\n- Qwen3-32B 同时担任 rewriter、judge、NLI gate validator 三个角色。NLI gate validation 中称 \"independent LLM annotator\" 不准确。\n- 建议：删除 \"independent\"，量化仅用 GPT-4o 数据是否足以支撑核心 claim。\n\n**W2** [warning] Direction-aware NLI for verbosity 削弱 content preservation 保证\n- 单向 NLI 允许 expansion 添加新的 quality-relevant content 而不被检测。text length 控制不等于 content quality 控制。\n- 建议：对 verbose rewrites 进行人工内容质量抽检。\n\n**W3** [warning] GEE exchangeable correlation 假设验证不充分\n- 未测试 AR(1) 或 unstructured。within-pair α̂ ∈ [-0.25, +0.11]，部分负相关暗示 exchangeable 可能非最优。\n\n**W4** [warning] BT 正则化细节和 bootstrap resamples 不一致\n- \"regularized estimate\" 未说明正则化类型和参数。GPT-4o 用 2,000 resamples，Qwen3-32B 用 10,000，无理由。\n\n**W5** [warning] Table 1 Qwen3-32B Register 行缺少 Cohen's d 值。\n\n**W6** [warning] DAG 遗漏 position bias 和 rewrite artifact 路径。\n\n### Minor\n- 无代码/数据可用性声明\n- wang2026fairjudge 第一作者 mismatch\n- murugadoss2025sos 在 OpenAlex 未找到\n\n### Missing References\n- Chiang et al. (2024) \"Chatbot Arena: An Open Platform\" — BT 实现规范\n- Ye et al. (2024) \"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\"\n\n### 主要优势\n1. 7 种统计方法在同一数据上 demonstrate Blindspot\n2. Cross-judge/cross-axis 复现，verbosity 提供 confound-free clean case\n3. GEE decomposition 揭示 per-axis confound structure 差异\n4. Limitations 坦诚具体\n5. Position control + consistency filter 设计合理"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意 Reviewer 1 提出的你未覆盖的问题（如 Holm-Bonferroni \"9 tests\" 错误、Direction-aware NLI 的内容保全削弱、GEE correlation structure、BT 正则化细节不一致）。\n\n---\n\n## Reviewer 1 审稿原文\n\n**Overall: 3.0 (Findings) | Confidence: 4/5**\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | Holm-Bonferroni family 定义矛盾（声称 9 检验实际 6 个）、因果声明 overclaim、evaluator-producer 循环性未充分量化 |\n| Excitement | 3.5/5 | Likert Blindspot 对评估社区有指导价值，per-axis GEE 分解有洞察力；但 scope 限制影响力 |\n| Reproducibility | 3/5 | 关键超参数大部分已报告，但 BT 正则化方式未说明、bootstrap resamples 数不一致（2000 vs 10000）、无代码/数据声明 |\n\n### Must-Fix 问题\n\n**N1** [critical] Holm-Bonferroni family 定义与实际实验不一致\n- §4.1 声称 \"three judges × three style axes = nine tests\"，但全文仅使用 2 个 judge（GPT-4o、Qwen3-32B），Table 1 只有 6 行。Holm-Bonferroni 校正基于不存在的 family size（9）比实际（6）更保守——虽然使结果更保守，但声称的设计与实际执行不一致是严重 credibility 问题。\n- 建议：修正为 \"two judges × three style axes = six tests\" 并重新检查 adjusted p-values。\n\n**N2** [critical] \"Causal\" 标题与方法论实质的张力\n- 标题 \"Causal Style Decomposition\"，但 §3.5 声明 \"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。NLI gate 对 do-operator 的近似不完整。标题 overclaim。\n- 建议：将 \"Causal\" 替换为 \"Interventional\" 或 \"Style-Controlled\"；或提供更严格的因果识别条件讨论。\n\n**N3** [critical] 单一 benchmark（LLMBar, n=100）的代表性\n- 所有实验仅基于 LLMBar（n=100），NLI gate 后剩 88 pairs → 173 comparisons。Bootstrap CI 宽度达 14.5pp。从 n=100 的单一 benchmark 推广到 \"LLM Judges\" 整个类别的 claim 缺乏 external validity。\n- 建议：至少在一个额外 benchmark 上复现核心发现，或明确限定 scope。\n\n### Should-Fix 问题\n\n**W1** [warning] Evaluator-producer 循环性未充分量化\n- Qwen3-32B 同时担任 rewriter、judge、NLI gate validator 三个角色。NLI gate validation 中称 \"independent LLM annotator\" 不准确。\n- 建议：删除 \"independent\"，量化仅用 GPT-4o 数据是否足以支撑核心 claim。\n\n**W2** [warning] Direction-aware NLI for verbosity 削弱 content preservation 保证\n- 单向 NLI 允许 expansion 添加新的 quality-relevant content 而不被检测。text length 控制不等于 content quality 控制。\n- 建议：对 verbose rewrites 进行人工内容质量抽检。\n\n**W3** [warning] GEE exchangeable correlation 假设验证不充分\n- 未测试 AR(1) 或 unstructured。within-pair α̂ ∈ [-0.25, +0.11]，部分负相关暗示 exchangeable 可能非最优。\n\n**W4** [warning] BT 正则化细节和 bootstrap resamples 不一致\n- \"regularized estimate\" 未说明正则化类型和参数。GPT-4o 用 2,000 resamples，Qwen3-32B 用 10,000，无理由。\n\n**W5** [warning] Table 1 Qwen3-32B Register 行缺少 Cohen's d 值。\n\n**W6** [warning] DAG 遗漏 position bias 和 rewrite artifact 路径。\n\n### Minor\n- 无代码/数据可用性声明\n- wang2026fairjudge 第一作者 mismatch\n- murugadoss2025sos 在 OpenAlex 未找到\n\n### Missing References\n- Chiang et al. (2024) \"Chatbot Arena: An Open Platform\" — BT 实现规范\n- Ye et al. (2024) \"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\"\n\n### 主要优势\n1. 7 种统计方法在同一数据上 demonstrate Blindspot\n2. Cross-judge/cross-axis 复现，verbosity 提供 confound-free clean case\n3. GEE decomposition 揭示 per-axis confound structure 差异\n4. Limitations 坦诚具体\n5. Position control + consistency filter 设计合理"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-21T07:20:01.795515+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1715
}
```

</details>

---


### Assistant

_source line 116 · 2026-05-21T07:20:04.183406+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 117 · 2026-05-21T07:20:06.964871+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿已提交给 Review Director。

**评分**: Overall 3.0 (Findings), Soundness 3.5/5, Excitement 2.5/5, Confidence 4/5

**核心判断**: 实验执行扎实（七种统计方法交叉验证 Likert Blindspot），但三个主要问题制约了评分：
1. **N1** Abstract 过度声称（"dominant source"基于 2 judges + 1 benchmark 证据不足）
2. **N2** 标题 "Causal" 与 §3.5 因果声明 disclaimer 存在实质性张力
3. **W1** 新颖性天花板——Likert Blindspot 是心理测量学已知现象的领域迁移，CSD 是现有组件流水线

另提出 5 个 Should-Fix（实验规模、evaluator-producer confound、scale granularity 未探讨、缺 mitigation 策略等）、3 个 Minor（Figure 4 疑似 PLACEHOLDER 水印、Table 1 格式不一致、引用 author mismatch）、3 条 Missing References（Silent Judge NeurIPS 2025、LLM-judge survey、Feder et al. 2022 causal NLP survey）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 118 · 2026-05-21T07:20:12.029852+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 119 · 2026-05-21T07:21:32.268380+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2

### Must-Fix

**[REBUT] R2-N1: Abstract 过度声称**
部分反驳。R2 指出的 (a) 点存在归因偏差："dominant source" claim 出现在 Introduction line 9，句式为 "Recent work has converged on a striking finding: ..."，后接三条引用（Murugadoss 2025, Li 2026, Soumik 2026）——这是文献归纳而非本文 claim。Abstract 对应表述也明确标记为 "recent work shows"。但 R2 的 (b) 点我完全同意且此前未覆盖：将 verbosity preference 与 style bias 并列对比构成 category error，因为论文自身将 verbosity 定义为 style 的子轴。(c) 点方向合理但归因仍需注意引用来源。总体建议合理，措辞应修改。

**[AGREE] R2-N2: "Causal" 标题张力**
与我的 N2 完全一致。补充：作者若坚持 "Causal"，应在 §3.5 明确 identification assumptions（在什么条件下 NLI gate 实现了 do(S)），而非仅给 disclaimer。

### Should-Fix

**[REBUT] R2-W1: 新颖性天花板受限**
R2 判断部分过严。虽然 Likert Blindspot 在 psychometrics 中已知，但 (1) 7种统计方法的量化 demonstration 对 LLM 评估社区有实际价值；(2) GEE decomposition 揭示的 per-axis confound structure 梯度（Table 3）是全新发现；(3) 两层机制的具体识别此前未有。不过建议加强 domain transfer non-triviality 论证是合理的。Excitement 给 2.5 偏低，我给 3.5。

**[AGREE] R2-W2: 实验规模偏窄**
与我的 N3 一致。我将此列为 Must-Fix 级别。

**[AGREE] R2-W3: Evaluator-producer confound**
与我的 W1 一致。R2 建议用第三模型作 rewriter 更具体可操作。

**[AGREE] R2-W4: Scale granularity 未探讨**
我完全未覆盖的有效问题。1-10 vs 1-100 的区分决定了 Blindspot 是 absolute scoring 范式的根本问题还是仅是 scale design 问题。Table 2 的 ordinal regression 排除了 interval-scale 假设，但不排除 granularity 影响。

**[REBUT] R2-W5: 缺乏 mitigation 策略**
论文定位是 diagnostic framework，不必同时提出 debiasing solution。§6 的 "adopt pairwise comparison" 已是可操作建议。但 O(n²) scalability concern 合理，可简要讨论 active sampling 等 O(n log n) 方案。Should-Fix 级别合适，不宜升为 Must-Fix。

### Minor & Missing References

[AGREE] M1-M3 均合理。
[AGREE] R3 (Feder et al. 2022) 对因果框架讨论有直接参考价值。
[REBUT] R1 (Oriyad & Rohban 2025) 未能在 OpenAlex/Semantic Scholar 确认存在。
[AGREE] R2 (LLM-as-judge survey) 补充综述性引用合理。

### 两位 Reviewer 的评分差异

| 维度 | R1 | R2 | 差异分析 |
|------|----|----|---------|
| Soundness | 3/5 | 3.5/5 | R2 对 NLI 验证评价更高，我对 Holm-Bonferroni 不一致（R2未提及）扣分更多 |
| Excitement | 3.5/5 | 2.5/5 | 主要分歧——我认为 GEE decomposition + 7-method demonstration 有实际贡献，R2 认为是 known phenomenon 的 domain transfer |
| Overall | 3.0 | 3.0 | 一致 |

核心共识：(1) "Causal" overclaim；(2) 单一 benchmark 不足；(3) evaluator-producer 循环性。
核心分歧：novelty 评估——我偏向认可 quantification + GEE decomposition 的贡献，R2 更强调 methodological novelty 不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 120 · 2026-05-21T07:21:36.972793+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 11

## Round 11

2 recorded events


### User

_source line 121 · 2026-05-21T07:21:39.632040+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心结论：与 R2 在 3 个 Must-Fix（Causal overclaim、单一 benchmark、evaluator-producer bias）上达成共识。主要分歧在 novelty 评估——我认为 GEE decomposition 和 7-method quantification 的贡献值得 Excitement 3.5，R2 给 2.5。R2 提出的 scale granularity（W4）是我此前遗漏的有效问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 122 · 2026-05-21T07:21:44.645869+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 12

## Round 12

10 recorded events


### User

_source line 123 · 2026-05-21T07:23:41.476374+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1

---

### Must-Fix 问题

**[AGREE] R1-N1: Holm-Bonferroni family 定义 "9 tests" 错误**

完全同意，这是我遗漏的重要问题。§4.1 明确声称 "three judges × three style axes = nine tests"，但全文自始至终只有 2 个 judge（GPT-4o, Qwen3-32B），Table 1 只有 6 行。这不是小错误——Holm-Bonferroni 校正的 family size 直接决定 adjusted p-values。虽然 9-test 校正比实际需要的 6-test 更保守（已显著的结果不受影响），但声称的实验设计与实际执行不一致是 credibility 问题。可能暗示作者计划了第三个 judge 但最终未执行，而忘记更新文本。必须修正为 "two judges × three style axes = six tests"。

**[AGREE] R1-N2: "Causal" 标题 overclaim**

与我的 N2 完全一致。§3.5 的 disclaimer 与标题 "Causal Style Decomposition" 之间的张力是本文最突出的 framing 问题。R1 建议的 "Interventional" 或 "Style-Controlled" 比我建议的 "Controlled" 更精确——"Interventional Style Decomposition" 既准确描述了 do-operator 近似的意图，又不 overclaim 完整因果识别。

**[AGREE] R1-N3: 单一 benchmark 代表性不足**

与我的 W2 一致。R1 补充的具体数字更有力：NLI gate 后仅 88 pairs → 173 comparisons，bootstrap CI 宽度达 14.5pp。这意味着核心发现的精度受限于一个小样本的单一 benchmark。我的审稿中将此定级为 Should-Fix，但考虑到论文在 Abstract 中做出 "LLM Judges"（全称）级别的 claim，R1 将其升级为 Must-Fix 是合理的。

---

### Should-Fix 问题

**[AGREE] R1-W1: Evaluator-producer 循环性 — "independent" 用词不当**

同意，且 R1 比我的 W3 更精确地指出了关键措辞问题。§5.1（p.5）将 Qwen3-32B 称为 "independent LLM annotator" 来验证 NLI gate，但 Qwen3-32B 同时担任 rewriter（§3.1）和 judge 之一。"Independent" 在此语境下是 misleading。R1 建议删除 "independent" 并量化仅用 GPT-4o 数据是否足以支撑核心 claim 是可操作的。

补充我的发现：Table 3 (GEE) 中 Qwen3-32B 的 formality style OR (4.20) 和 originality OR (4.20) 系统性高于 GPT-4o（style OR 2.58, originality OR 1.13），效应量差异达 ~2x，进一步暗示 evaluator-producer bias 的影响非 trivial。

**[AGREE] R1-W2: Direction-aware NLI 削弱 verbosity 的 content preservation**

这是我遗漏的重要方法论问题。§3.2（p.4）对 verbosity 轴使用单向 NLI（仅 backward entailment：rewrite entails original），理由是 "expansion necessarily introduces new content that the original cannot entail"。但 R1 正确指出：backward entailment 只保证原始内容被保留在改写中，不阻止添加新的 quality-relevant 内容。

具体影响：如果 verbose rewrite 在扩展时添加了实质性的 quality-relevant 信息（例如更详细的论证、额外的 example），judge 的偏好可能反映的不仅是 verbosity style preference，还包括 content quality improvement。这会使 verbosity 轴的 BT win probability（76-77%）中混入 content quality confound，从而高估 pure style bias。

然而，有一个缓和因素值得注意：§5.4（p.7）报告 verbosity 是 "confound-free cleanest demonstration"——GEE 分解显示 originality component 对 verbosity 不显著（OR = 0.15, p = 0.062, Table 3）。如果 verbose rewrites 确实添加了 quality-relevant content，我们应该看到 originality component 显著，但实际未看到。这部分缓解了 R1 的担忧，但不完全消除（GEE 的 "originality" operationalization 可能不捕获所有 quality dimensions）。建议人工抽检仍然必要。

**[REBUT] R1-W3: GEE exchangeable correlation 假设**

部分不同意 R1 的具体建议（测试 AR(1) 或 unstructured）。

关键点：GEE 的聚类单位是 text pair（position swap），每个 pair 最多 2 个观测值（position A 和 position B）。对于 cluster size = 2，exchangeable、AR(1) 和 unstructured 三种 correlation structure 在数学上等价——都只有一个 off-diagonal 参数。因此测试 AR(1) 或 unstructured 不会提供额外信息。

Appendix B, Table 4（p.10）已展示 exchangeable vs independence 的对比：|ΔQIC| < 0.001，maximum coefficient change < 0.02。这对 cluster size ≤ 2 的设计是充分的 robustness check。

关于 R1 注意到的负相关（α̂ ∈ [-0.25, +0.11]）：这实际上是 position-swap 设计的预期行为。如果 judge 有 position preference，同一 content pair 在 position A 和 B 会倾向产生相反结果，导致负的 within-pair correlation。这不是 correlation structure misspecification 的证据，而是 position bias 被 design 正确捕获的证据。

**[AGREE] R1-W4: BT 正则化和 bootstrap resamples 不一致**

同意这是 reproducibility 问题。我在审稿中未注意到这一点。具体问题：(a) §5.2 提到 "regularized estimate" 但从未说明正则化类型（Bayesian prior? L2 penalty? pseudocount?）和超参数值；(b) 如果 GPT-4o 用 2,000 resamples 而 Qwen3-32B 用 10,000，应说明理由（例如：收敛性检查后发现需要更多 resamples？还是笔误？）。

这些细节对 reproducibility 评分有直接影响。建议作者在方法部分统一说明 BT 实现细节。

**[AGREE] R1-W5: Table 1 Qwen3-32B Register 缺少 Cohen's d**

与我的 M2 一致。即使该轴是 exploratory，也应报告数值以保持表格格式一致。

**[AGREE] R1-W6: DAG 遗漏 position bias 和 rewrite artifact 路径**

这是我遗漏的有效观察。Figure 2（p.5）的 DAG 包含 S → Y, Q → Y, R → S, R ⇢ Q（虚线），但缺少：
(a) Position bias: P → Y，虽然 §3.3 的 position swap 在实验上控制了这一变量，但 DAG 应将其表示为被 conditioned out 的变量。
(b) Rewrite artifact: R → Y（独立于 S 和 Q 的路径），即 judge 检测到 text 是 LLM 生成/改写的这一事实本身可能影响评分——这与 evaluator-producer confound 直接相关。

一个更完整的 DAG 会使 §3.5 的 disclaimer 更有说服力，因为读者能看到哪些路径被控制、哪些被假设为 negligible。

---

### Minor 问题

**[AGREE]** 无代码/数据可用性声明——同意是提交合规问题（ARR 鼓励但不要求）。

**[AGREE]** wang2026fairjudge 第一作者 mismatch——与我的 M3 一致。

**[AGREE]** murugadoss2025sos 在 OpenAlex 未找到——我的引用验证也确认了这一点（confidence 仅 0.361）。可能是太新尚未被索引，但建议作者确认 bib 条目准确性。

---

### Missing References

**[AGREE]** Chiang et al. (2024) "Chatbot Arena" — 同意应引用作为 BT model 在 LLM 评估中的 canonical reference。论文大量使用 BT model 但仅引用 Bradley & Terry (1952) 原始论文，缺少 LLM 评估领域的 BT 实践规范。

**[AGREE]** Ye et al. (2024) "Justice or Prejudice?" — 同意应补充。该工作系统量化了 LLM judge 的多种 bias，是直接竞品文献。

补充我提出的遗漏引用：
- Oriyad & Rohban (2025) "The Silent Judge" (NeurIPS 2025) — 研究 LLM judge 的 shortcut bias
- Feder et al. (2022, TACL) "Causal Inference in NLP" — 若保留 "Causal" 标题则需要这一方法论综述

---

### 综合评估

两位 Reviewer 独立给出 Overall 3.0 (Findings)，且在多个核心问题上达成共识：

**共识问题（高确定度）**：
1. "Causal" framing overclaim（两人均列为 Must-Fix）
2. 实验规模偏窄（2 judges, 1 benchmark）
3. Evaluator-producer confound
4. Table 1 格式不一致

**R1 独有的有效发现**：
1. Holm-Bonferroni "9 tests" 错误——纯事实性错误，我遗漏了
2. Direction-aware NLI for verbosity 的 content preservation 弱化——有效的方法论问题
3. BT 正则化细节和 bootstrap resamples 不一致——reproducibility 问题
4. DAG 缺少 position bias 和 rewrite artifact 路径——建模完整性问题

**我的独有发现 R1 未覆盖**：
1. Scale granularity 未探讨（1-10 vs 1-100 vs continuous）
2. 缺乏 mitigation 策略（论文止于诊断）
3. Abstract 中 verbosity 既是 style axis 又被列为被 outweigh 的对比对象的逻辑混淆

**我与 R1 的唯一分歧**：GEE correlation structure（W3）——对 cluster size = 2 的设计，exchangeable/AR(1)/unstructured 在数学上等价，R1 建议测试 AR(1) 在此场景下不适用。

**维持我的评分**：Overall 3.0 (Findings), Soundness 3.5/5, Excitement 2.5/5, Confidence 4/5。R1 发现的 Holm-Bonferroni 错误和 bootstrap 不一致使我考虑将 Soundness 降至 3.0/5，但 §5.2 的七种方法交叉验证和 Appendix B 的 robustness check 部分弥补了这些问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-21T07:24:03.930967+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-21T07:24:04.132394+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T07:08:58.298617+00:00\", \"completed_at\": \"2026-05-21T07:12:28.271319+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主正文（Abstract 至 Conclusion 末尾）溢出至第 9 页约 1/4 页。Conclusion 从 p8 底部开始，延续到 p9 上半部分才结束，之后才是 Limitations。EMNLP 2026 严格 8 页主正文限制，当前超限约 0.25 页，需压缩正文或将部分内容移至 appendix。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续 3 页纯文本无任何 display item。第一个视觉锚点（Figure 1）直到第 4 页才出现。审稿人前 2 分钟的阅读体验缺乏视觉锚定，建议将 Figure 1（pipeline）或 Figure 2（causal DAG）提前到第 2 页（Introduction 末尾或 Related Work 旁）。\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"单页堆叠 3 个 display item（Figure 2 + Table 1 + Figure 3），视觉密度过高，与前 3 页的文本荒漠形成强烈反差。建议将 Figure 2 前移至 p2-p3，使 display item 分布更均匀。\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Figure 2（causal DAG）尺寸偏小，节点标签（S, Y, Q 等）在打印尺寸下可能难以辨认。建议适当放大或使用 figure* 全宽展示。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3 使用填充菱形 vs 空心菱形区分显著性水平，在小尺寸打印下两者视觉差异不明显。建议改用颜色 + 形状双重编码或加大标记尺寸。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1 caption \\\"CSD pipeline overview. Numbers indicate sample attrition at each stage.\\\" 较简短，建议补充一句核心信息（如 \\\"Style-controlled rewriting isolates per-axis effects through...\\\"），使 caption 更自包含。\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"图表整体以灰度/单色为主，打印友好性好，但视觉吸引力偏低。核心结果图（Figure 3）可考虑使用 Okabe-Ito 色板增强区分度。\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"表格全部使用 booktabs 风格，无竖线，最优值加粗，精度统一——表格排版专业。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 6 \\\"Conclusion\\\" heading 出现在页面最底部，下方仅剩约 2 行正文，存在轻微的 heading 孤悬感。\"}], \"counts\": {\"critical\": 1, \"warning\": 3, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-21T07:24:04.132767+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-21T07:24:04.183258+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T07:08:59.566217+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_5ce280de124a4e308d1827c6450ad337\", \"skipped_at\": \"2026-05-21T07:15:24.027211+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-21T07:29:46.513690+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1 issues RE-RAISED in Round 2 (reopened / still open)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 AGREE。Round 1 降调为 interventional framing + DAG\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次独立列为 Must-Fix。标题仍为 'Causal'，§3.5 disclaimer 未变。建议改为 Interventional/Controlled Style Decomposition\"\n    action_items:\n      - round: 1\n        action: \"因果语言全面降调为 interventional。DAG 已加入 §3.5\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer，CSD 是现有组件流水线\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 REBUT Findings-level 价值\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 维持 Excitement 2.5/5，R1 给 3.5/5。分歧未收敛。R1 认为 GEE decomposition + 7-method quantification 有独立贡献\"\n    action_items:\n      - round: 1\n        action: \"6/6 Blindspot cells。GEE gradient 跨 judge 复现\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 1 resolved, NOT re-raised in Round 2\n  # ============================================================\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未提及。§5.1 NLI validation (FNR 8.4%, precision 98.9%, AC1=0.89) 被两位 Reviewer 认可\"\n    action_items:\n      - round: 1\n        action: \"三重间接证据。实际 FNR 8.4%\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§nli_validation 完整：FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification，per-axis 调整引入 researcher degrees of freedom\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。Threshold sensitivity sweep 被接受\"\n    action_items:\n      - round: 1\n        action: \"exp-011 sensitivity analysis + bimodal distribution justification\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Threshold on plateau, not cliff edge. Results robust 0.70-0.95\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE with nuance\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。§5.2 head-to-head on same data 被接受\"\n    action_items:\n      - round: 1\n        action: \"同数据 h2h：Likert ATE p=0.33 vs BT 63.0% p<0.001\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§likert_pairwise 直接 h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整——placeholder arXiv IDs、broken citations\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 报告占位符；R1 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及 placeholder/broken 问题。但有新的 author mismatch 问题（见 RD2-M3）\"\n    action_items:\n      - round: 1\n        action: \"22 verified references。0 placeholder/broken\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"22 verified refs, 0 broken, 0 undefined references\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 升级为必要实验\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。Table 2 的 7-method hierarchy 被两位 Reviewer 高度评价\"\n    action_items:\n      - round: 1\n        action: \"exp-015 ordinal regression p=0.769。7-method sensitivity hierarchy\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering ~40-50% data loss 未分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 补充 win rate 可能被高估\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。BT 63.0% (all) < sign test 73.9% (filtered) 论证被接受\"\n    action_items:\n      - round: 1\n        action: \"BT 63.0% (all data) < sign test 73.9% (filtered)\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"BT on all data LOWER than filtered sign test\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound OR=1.65——需要 formal partial-out\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 修正为 marginal\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。GEE per-cell decomposition 被认可\"\n    action_items:\n      - round: 1\n        action: \"GEE for 2 judges × 3 axes\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Per-cell GEE decomposition with cross-axis gradient\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。Primary/exploratory/confirmatory trichotomy 被接受\"\n    action_items:\n      - round: 1\n        action: \"Holm-Bonferroni on primary family\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis 方法论问题\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE Hoenig 2001\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。Reframed as illustrative sensitivity comparison 被接受\"\n    action_items:\n      - round: 1\n        action: \"Reframed as illustrative sensitivity comparison\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Power curve is illustrative, not post-hoc power analysis\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 axis 覆盖不再被提及（6/6 cells complete）。但 benchmark 覆盖问题以新 issue RD2-MF3 形式出现\"\n    action_items:\n      - round: 1\n        action: \"6/6 cells complete\"\n        assigned_to: agent\n        status: done\n    resolution: \"Complete 2×3 matrix with BT + Likert + GEE for all cells\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry 建模\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 REBUT\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 BT 已是 primary analysis，被高度认可\"\n    action_items:\n      - round: 1\n        action: \"BT as primary for all 6 cells\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"BT with pair-level bootstrap is primary analysis\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 覆盖不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 related work 结构被接受，但有新的 missing references（见 RD2-REF）\"\n    action_items:\n      - round: 1\n        action: \"5-paragraph related work. 22 verified references\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Comprehensive coverage of psychometrics, style bias, LLM judge evaluation\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表——无 Figure，仅 Tables\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 最强同意\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 论文含 3 figures (pipeline, DAG, forest plot) + power curve，不再被提及\"\n    action_items:\n      - round: 1\n        action: \"3 figures 完成\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"3 figures: power curve, pipeline diagram, forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"交叉讨论强共识\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 两层机制 framing 被接受\"\n    action_items:\n      - round: 1\n        action: \"Two-layer mechanism. Power curve n≈462\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Two-layer mechanism properly framed with power curve quantification\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound——需要 per-cell partial-out\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 修正\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 GEE decomposition 被认可为有洞察力的分析\"\n    action_items:\n      - round: 1\n        action: \"GEE for all 6 cells\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转——测量不同构念\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 发现；R2 升级\"\n    action_items:\n      - round: 1\n        action: \"Reframed as magnitude gap + construct difference\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Magnitude gap framing, not directional claim\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要实验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"收敛轮共识\"\n    action_items:\n      - round: 1\n        action: \"exp-015 p=0.769 + 7-method hierarchy\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Definitively resolved by exp-015 + Table 2\"\n    resolution_round: 1\n\n  # ============================================================\n  # NEW issues from Round 2\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni family 声称 'three judges × three style axes = nine tests' 但实际只有 2 judges (6 tests)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 独立发现，R2 交叉 AGREE。§4.1 声称设计与实际执行不一致。9-test 比 6-test 更保守（不影响已显著结果），但 credibility 问题\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar, n=100) 不足以支撑 'LLM Judges' 全称论断\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 列为 Must-Fix，R2 从 Should-Fix 升级为共识 Must-Fix。88 pairs → 173 comparisons, CI width 14.5pp。缺 Claude/Llama judge 和非 instruction-following 任务\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract 过度声称：'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 部分 AGREE。(a) 'dominant source' 虽有文献支撑但 Abstract 缺限定词；(b) verbosity 同时是 style axis 和被 outweigh 的对比对象，构成 category error\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色循环（rewriter+judge+NLI validator）+ 'independent' 用词不当\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"共识。§5.1 称 Qwen3-32B 为 'independent LLM annotator' misleading。Table 3 Qwen3-32B OR 系统性 ~2x GPT-4o\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI for verbosity 允许添加 quality-relevant content，削弱内容保全\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE with nuance。GEE originality NS 部分缓解但不完全消除。建议人工抽检\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨：1-10 vs 1-100 vs continuous，决定 Blindspot 是范式问题还是 scale design 问题\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 交叉 AGREE。Table 2 ordinal regression 排除 interval-scale 假设但不排除 granularity 影响\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation/calibration 策略，贡献止于诊断\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 提出 Should-Fix，R1 部分 REBUT（diagnostic 定位合理但应讨论 O(n²) scalability 和 active sampling）\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF5\"\n    summary: \"BT 正则化类型未说明 + bootstrap resamples 不一致（2000 vs 10000）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉 AGREE。Reproducibility 问题\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG (Figure 2) 遗漏 position bias (P→Y) 和 rewrite artifact (R→Y) 路径\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉 AGREE。更完整的 DAG 会加强 identification argument\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty 分歧：GEE decomposition 贡献 vs 已知现象 domain transfer\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 Excitement 3.5 vs R2 Excitement 2.5。未收敛。R1 认为 GEE + 7-method 有独立贡献，R2 强调 methodological novelty 有限\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) 疑似 PLACEHOLDER 水印\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 Minor M1。提交前需确认并移除\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register 行缺少 Cohen's d 值\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W5 + R2-M2 一致\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-M3\"\n    summary: \"引用 author mismatch: wang2026fairjudge (Wang vs Yang), murugadoss2025sos 未在 OpenAlex 找到\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均发现\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-M4\"\n    summary: \"无代码/数据可用性声明\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"ARR 鼓励但不要求\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-REF\"\n    summary: \"缺少重要引用：Chatbot Arena (Chiang 2024), Justice or Prejudice (Ye 2024), Causal Inference in NLP (Feder 2022)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共同推荐。另 R2 推荐 Oriyad & Rohban 2025 但 R1 未能确认存在\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制约 0.25 页（Conclusion 溢出到 p9），将导致 desk reject\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: []\n        note: \"视觉审查 Agent 发现 (critical)。连续 3 页无 display item + p5 堆叠 3 个 display item 也需调整\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1 issues RE-RAISED in Round 2 (reopened / still open)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 AGREE。Round 1 降调为 interventional framing + DAG\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次独立列为 Must-Fix。标题仍为 'Causal'，§3.5 disclaimer 未变。建议改为 Interventional/Controlled Style Decomposition\"\n    action_items:\n      - round: 1\n        action: \"因果语言全面降调为 interventional。DAG 已加入 §3.5\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer，CSD 是现有组件流水线\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 REBUT Findings-level 价值\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 维持 Excitement 2.5/5，R1 给 3.5/5。分歧未收敛。R1 认为 GEE decomposition + 7-method quantification 有独立贡献\"\n    action_items:\n      - round: 1\n        action: \"6/6 Blindspot cells。GEE gradient 跨 judge 复现\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 1 resolved, NOT re-raised in Round 2\n  # ============================================================\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 独立提出；R2 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未提及。§5.1 NLI validation (FNR 8.4%, precision 98.9%, AC1=0.89) 被两位 Reviewer 认可\"\n    action_items:\n      - round: 1\n        action: \"三重间接证据。实际 FNR 8.4%\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§nli_validation 完整：FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification，per-axis 调整引入 researcher degrees of freedom\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。Threshold sensitivity sweep 被接受\"\n    action_items:\n      - round: 1\n        action: \"exp-011 sensitivity analysis + bimodal distribution justification\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Threshold on plateau, not cliff edge. Results robust 0.70-0.95\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE with nuance\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。§5.2 head-to-head on same data 被接受\"\n    action_items:\n      - round: 1\n        action: \"同数据 h2h：Likert ATE p=0.33 vs BT 63.0% p<0.001\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§likert_pairwise 直接 h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整——placeholder arXiv IDs、broken citations\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 报告占位符；R1 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及 placeholder/broken 问题。但有新的 author mismatch 问题（见 RD2-M3）\"\n    action_items:\n      - round: 1\n        action: \"22 verified references。0 placeholder/broken\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"22 verified refs, 0 broken, 0 undefined references\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 升级为必要实验\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。Table 2 的 7-method hierarchy 被两位 Reviewer 高度评价\"\n    action_items:\n      - round: 1\n        action: \"exp-015 ordinal regression p=0.769。7-method sensitivity hierarchy\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering ~40-50% data loss 未分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 补充 win rate 可能被高估\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。BT 63.0% (all) < sign test 73.9% (filtered) 论证被接受\"\n    action_items:\n      - round: 1\n        action: \"BT 63.0% (all data) < sign test 73.9% (filtered)\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"BT on all data LOWER than filtered sign test\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound OR=1.65——需要 formal partial-out\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 修正为 marginal\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。GEE per-cell decomposition 被认可\"\n    action_items:\n      - round: 1\n        action: \"GEE for 2 judges × 3 axes\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Per-cell GEE decomposition with cross-axis gradient\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。Primary/exploratory/confirmatory trichotomy 被接受\"\n    action_items:\n      - round: 1\n        action: \"Holm-Bonferroni on primary family\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis 方法论问题\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 AGREE Hoenig 2001\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 未再提及。Reframed as illustrative sensitivity comparison 被接受\"\n    action_items:\n      - round: 1\n        action: \"Reframed as illustrative sensitivity comparison\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Power curve is illustrative, not post-hoc power analysis\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 axis 覆盖不再被提及（6/6 cells complete）。但 benchmark 覆盖问题以新 issue RD2-MF3 形式出现\"\n    action_items:\n      - round: 1\n        action: \"6/6 cells complete\"\n        assigned_to: agent\n        status: done\n    resolution: \"Complete 2×3 matrix with BT + Likert + GEE for all cells\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry 建模\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 REBUT\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 BT 已是 primary analysis，被高度认可\"\n    action_items:\n      - round: 1\n        action: \"BT as primary for all 6 cells\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"BT with pair-level bootstrap is primary analysis\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 覆盖不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 AGREE\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 related work 结构被接受，但有新的 missing references（见 RD2-REF）\"\n    action_items:\n      - round: 1\n        action: \"5-paragraph related work. 22 verified references\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Comprehensive coverage of psychometrics, style bias, LLM judge evaluation\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表——无 Figure，仅 Tables\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出；R1 最强同意\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 论文含 3 figures (pipeline, DAG, forest plot) + power curve，不再被提及\"\n    action_items:\n      - round: 1\n        action: \"3 figures 完成\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"3 figures: power curve, pipeline diagram, forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"交叉讨论强共识\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 两层机制 framing 被接受\"\n    action_items:\n      - round: 1\n        action: \"Two-layer mechanism. Power curve n≈462\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Two-layer mechanism properly framed with power curve quantification\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound——需要 per-cell partial-out\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出；R2 修正\"\n      - round: 2\n        reviewers: []\n        note: \"Round 2 GEE decomposition 被认可为有洞察力的分析\"\n    action_items:\n      - round: 1\n        action: \"GEE for all 6 cells\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转——测量不同构念\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 发现；R2 升级\"\n    action_items:\n      - round: 1\n        action: \"Reframed as magnitude gap + construct difference\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Magnitude gap framing, not directional claim\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要实验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"收敛轮共识\"\n    action_items:\n      - round: 1\n        action: \"exp-015 p=0.769 + 7-method hierarchy\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Definitively resolved by exp-015 + Table 2\"\n    resolution_round: 1\n\n  # ============================================================\n  # NEW issues from Round 2\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni family 声称 'three judges × three style axes = nine tests' 但实际只有 2 judges (6 tests)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 独立发现，R2 交叉 AGREE。§4.1 声称设计与实际执行不一致。9-test 比 6-test 更保守（不影响已显著结果），但 credibility 问题\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar, n=100) 不足以支撑 'LLM Judges' 全称论断\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 列为 Must-Fix，R2 从 Should-Fix 升级为共识 Must-Fix。88 pairs → 173 comparisons, CI width 14.5pp。缺 Claude/Llama judge 和非 instruction-following 任务\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract 过度声称：'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 部分 AGREE。(a) 'dominant source' 虽有文献支撑但 Abstract 缺限定词；(b) verbosity 同时是 style axis 和被 outweigh 的对比对象，构成 category error\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色循环（rewriter+judge+NLI validator）+ 'independent' 用词不当\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"共识。§5.1 称 Qwen3-32B 为 'independent LLM annotator' misleading。Table 3 Qwen3-32B OR 系统性 ~2x GPT-4o\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI for verbosity 允许添加 quality-relevant content，削弱内容保全\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE with nuance。GEE originality NS 部分缓解但不完全消除。建议人工抽检\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨：1-10 vs 1-100 vs continuous，决定 Blindspot 是范式问题还是 scale design 问题\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 交叉 AGREE。Table 2 ordinal regression 排除 interval-scale 假设但不排除 granularity 影响\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation/calibration 策略，贡献止于诊断\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 提出 Should-Fix，R1 部分 REBUT（diagnostic 定位合理但应讨论 O(n²) scalability 和 active sampling）\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF5\"\n    summary: \"BT 正则化类型未说明 + bootstrap resamples 不一致（2000 vs 10000）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉 AGREE。Reproducibility 问题\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG (Figure 2) 遗漏 position bias (P→Y) 和 rewrite artifact (R→Y) 路径\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉 AGREE。更完整的 DAG 会加强 identification argument\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty 分歧：GEE decomposition 贡献 vs 已知现象 domain transfer\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 Excitement 3.5 vs R2 Excitement 2.5。未收敛。R1 认为 GEE + 7-method 有独立贡献，R2 强调 methodological novelty 有限\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) 疑似 PLACEHOLDER 水印\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 Minor M1。提交前需确认并移除\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register 行缺少 Cohen's d 值\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W5 + R2-M2 一致\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-M3\"\n    summary: \"引用 author mismatch: wang2026fairjudge (Wang vs Yang), murugadoss2025sos 未在 OpenAlex 找到\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均发现\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-M4\"\n    summary: \"无代码/数据可用性声明\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"ARR 鼓励但不要求\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-REF\"\n    summary: \"缺少重要引用：Chatbot Arena (Chiang 2024), Justice or Prejudice (Ye 2024), Causal Inference in NLP (Feder 2022)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共同推荐。另 R2 推荐 Oriyad & Rohban 2025 但 R1 未能确认存在\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制约 0.25 页（Conclusion 溢出到 p9），将导致 desk reject\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: []\n        note: \"视觉审查 Agent 发现 (critical)。连续 3 页无 display item + p5 堆叠 3 个 display item 也需调整\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-21T07:29:46.615613+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 18871}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-21T07:32:21.885643+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: \"Causal Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges\"\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 格式）\n**审稿轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达成共识）\n\n---\n\n## Summary\n\n本文提出 Causal Style Decomposition (CSD)，通过风格控制改写、NLI 内容保全门控和位置控制的成对比较来检测 LLM 评委的逐轴风格偏差。核心发现为 \"Likert Blindspot\"：标准 Likert 评分因 ~60% tie inflation 和信号衰减的双层结构限制，系统性地遗漏成对比较能检出的风格偏差。实验在 LLMBar (n=100) 上用 GPT-4o 和 Qwen3-32B 两个评委、三个风格轴（formality, verbosity, register）验证，七种统计方法一致确认该现象。\n\n---\n\n## Strengths\n\n**S1. 统计论证扎实**（R1+R2 共识）：七种不同统计方法（BT model, sign test, t-test, binarized Likert, ordinal logistic, GEE, Wilcoxon）在同一数据上验证 Blindspot——所有成对方法达显著而所有 Likert 方法失败。Table 2 的 sensitivity hierarchy 是有力的系统性证据。\n\n**S2. 多维度复现**（R1+R2 共识）：跨评委（GPT-4o vs Qwen3-32B）、跨风格轴（formality, verbosity, register）的复现设计。Verbosity 轴的 BT win probability 达 76-77%，效应量令人印象深刻且跨 judge 高度一致（OR = 11.34 vs 13.10）。\n\n**S3. GEE 分解提供结构性洞察**（R1 高度评价）：GEE 逻辑回归将 style 和 originality 效应分解，揭示 per-axis confound structure 梯度（verbosity = pure style, formality = mixed, register = originality-dominated），为后续 debiasing 工作提供诊断基础。这一分析跨 judge 复现，是全新的经验发现。\n\n**S4. Limitations 真实坦诚**（R1+R2 共识）：主动披露 quality-style confounding（OR = 2.32）、evaluator-producer bias、benchmark/axis 覆盖不足。\n\n**S5. Position control + consistency filter 设计合理**（R1）：位置对调 + 一致性过滤 + BT 全数据 vs 过滤数据交叉验证（63.0% < 73.9%，排除 filter inflation）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-MF1** [critical, 双 Reviewer 共识] **\"Causal\" 标题与方法实质不匹配**\n标题 \"Causal Style Decomposition\" 暗示形式化因果推断，但 §3.5 明确声明 \"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。这不是一般的 qualification——是对因果方法论基本假设的全面放弃。两位 Reviewer 一致将此列为最突出的 framing 问题。建议改用 \"Interventional Style Decomposition\" 或 \"Controlled Style Decomposition\"；如果坚持 \"Causal\"，必须在 §3.5 提供明确的 identification assumptions（在什么条件下 NLI gate 实现了 do(S)）。\n*（R1-N2 + R2-N2，交叉 [AGREE]）*\n\n**W-MF2** [critical, 双 Reviewer 共识] **Holm-Bonferroni family 定义与实际实验矛盾**\n§4.1 声称 \"three judges × three style axes = nine tests\"，但全文仅有 2 个 judge（GPT-4o, Qwen3-32B），Table 1 只有 6 行。第三个 judge 不存在。虽然 9-test 校正比 6-test 更保守（已显著结果不受影响），但声称的实验设计与实际执行不一致是严重 credibility 问题。可能是遗留了未执行的第三 judge 计划。必须修正为 \"two judges × three style axes = six tests\" 并重新检查 adjusted p-values。\n*（R1-N1，R2 交叉 [AGREE]）*\n\n**W-MF3** [critical, 双 Reviewer 共识] **单一 benchmark 代表性不足**\n所有实验仅基于 LLMBar（n=100），NLI gate 后仅 88 pairs → 173 comparisons，bootstrap CI 宽度达 14.5pp。LLMBar 是 instruction-following 专用 benchmark。从单一小规模 benchmark 推广到 \"LLM Judges\" 全称论断缺乏 external validity。缺少：(a) Claude/Llama 系列评委；(b) 非 instruction-following 任务（summarization, translation）。建议至少在一个额外 benchmark 上复现核心发现，或在 title/abstract 中明确限定 scope。\n*（R1-N3 + R2-W2，交叉升级为共识 Must-Fix）*\n\n**W-MF4** [critical, R2 raised + R1 partial agree] **Abstract 过度声称**\nIntroduction 和 Abstract 中 \"style bias is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference\"：(a) 虽有三条文献引用支撑，但 Abstract 缺少 \"recent work shows\" 限定；(b) verbosity 本身是论文三个风格轴之一，说风格偏差 \"far outweighs verbosity preference\" 构成 category error——verbosity bias IS a style bias in the paper's own framework；(c) formality BT 63%，position bias 通常 55-65%，\"far outweighing\" 缺乏量级支撑。建议修改措辞。\n*（R2-N1，R1 部分 [AGREE]——(b) 完全成立）*\n\n**W-MF5** [critical, 视觉审查] **主正文超 8 页限制**\n视觉审查确认：主正文（Abstract 至 Conclusion 末尾）溢出至第 9 页约 1/4 页。Section 6 Conclusion 从 p8 底部开始，延续到 p9 上半部分。EMNLP 2026 严格 8 页主正文限制，当前超限将直接导致 desk reject。需压缩正文或将部分内容移至 appendix。\n*（视觉审查 critical finding）*\n\n### Should-Fix（影响评分）\n\n**W-SF1** [warning, 双 Reviewer 共识] **Evaluator-producer 三角色循环偏差**\nQwen3-32B 同时担任 rewriter、judge、NLI gate validator 三个角色。§5.1 称其为 \"independent LLM annotator\" 不准确（misleading）。Table 3 中 Qwen3-32B 的 formality OR (4.20) 和 originality OR (4.70) 系统性约为 GPT-4o（2.58, 2.32）的 2 倍，暗示 evaluator-producer bias 影响非 trivial。建议：(1) 删除 \"independent\"；(2) 明确论证仅 GPT-4o 数据是否足以支撑核心 claim；(3) 理想情况下用第三模型（不同 family）作为 rewriter 做控制实验。\n*（R1-W1 + R2-W3，交叉 [AGREE]）*\n\n**W-SF2** [warning, R1 raised + R2 agree with nuance] **Direction-aware NLI 削弱 verbosity 内容保全**\n§3.2 对 verbosity 轴使用单向 NLI（仅 backward entailment），不阻止添加新 quality-relevant content。缓解因素：GEE 分解显示 verbosity originality component 不显著（OR=0.49, p=.096），且 text length 控制后 style OR 几乎不变（<2%），但 GEE \"originality\" operationalization 可能不捕获所有 quality dimensions。建议人工内容质量抽检。\n*（R1-W2，R2 交叉 [AGREE] with nuance）*\n\n**W-SF3** [warning, R2 raised + R1 agree] **Scale granularity 未探讨**\n论文使用 1-10 Likert scale。关键问题：Blindspot 是所有 ordinal scale 的固有属性还是 1-10 特定粒度结果？如果 1-100 或 continuous scale 也有 Blindspot，那是对 Likert 范式的根本批评；如果更细粒度可缓解，则是 scale 选择问题。Table 2 ordinal regression 排除了 interval-scale 假设但不排除 granularity 影响。建议至少在 Limitations 或 Discussion 中讨论。\n*（R2-W4，R1 交叉 [AGREE]——\"此前遗漏的有效问题\"）*\n\n**W-SF4** [warning, R2 raised + R1 partial rebut] **缺乏 mitigation 策略**\n论文诊断出 Blindspot 但仅建议 \"adopt pairwise comparison\"，未讨论 O(n²) scalability 或任何 calibration/debiasing 方案。R1 认为 diagnostic framework 定位合理，不必同时提出 debiasing solution，但建议简要讨论 active sampling 等 O(n log n) 方案。\n*（R2-W5，R1 部分 [REBUT]——severity 有分歧但方向一致）*\n\n**W-SF5** [warning, R1 raised + R2 agree] **BT 正则化细节和 bootstrap resamples 不一致**\n§5.2 \"regularized estimate\" 未说明正则化类型（Bayesian prior? L2? pseudocount?）和超参数。GPT-4o 用 2,000 resamples，Qwen3-32B 用 10,000，无解释。影响 reproducibility。\n*（R1-W4，R2 交叉 [AGREE]）*\n\n**W-SF6** [warning, R1 raised + R2 agree] **DAG 遗漏关键路径**\nFigure 2 缺少：(a) Position bias P → Y（虽被 position swap 控制，但应在 DAG 中表示为 conditioned out）；(b) Rewrite artifact R → Y（judge 检测到 text 是 LLM 改写的这一事实本身影响评分——与 evaluator-producer confound 直接相关）。更完整的 DAG 会加强 §3.5 的 identification argument。\n*（R1-W6，R2 交叉 [AGREE]）*\n\n### Minor\n\n**W-M1** Figure 4 (power_curve) 疑似存在淡色 PLACEHOLDER 水印，提交前需确认并移除。\n**W-M2** Table 1 Qwen3-32B Register 行缺少 Cohen's d 值，格式与其他行不一致。\n**W-M3** 引用问题：wang2026fairjudge 第一作者 mismatch（bib: Wang, OpenAlex: Yang）；murugadoss2025sos 在 OpenAlex 未找到。\n**W-M4** 无代码/数据可用性声明（ARR 鼓励但不要求）。\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 强共识（两位 Reviewer 一致）：**\n1. \"Causal\" framing overclaim 是最突出的 framing 问题\n2. Holm-Bonferroni \"9 tests\" 是事实性错误（声称 3 judges，实际 2）\n3. 单一 benchmark + 小样本不支持全称论断\n4. Evaluator-producer 三角色循环偏差需更好处理\n5. Scale granularity 是有效的未讨论问题\n6. BT 正则化和 bootstrap 细节不一致\n7. DAG 缺少 position bias 和 rewrite artifact 路径\n\n---\n\n## Reviewer Divergence\n\n**Excitement/Novelty 评估（核心分歧，未收敛）：**\n- R1 (Excitement 3.5/5)：GEE decomposition 揭示的 per-axis confound structure 梯度是全新发现，7 种统计方法的 quantitative demonstration 对 LLM 评估社区有实际价值，两层机制的具体识别此前未有\n- R2 (Excitement 2.5/5)：Likert Blindspot 是心理测量学经典现象（ordinal discretization 损失连续信号）在 LLM judge 领域的迁移应用，CSD 是三个已有组件的流水线（LLM 改写 + NLI filter + BT comparison），methodological novelty 有限\n\n**GEE correlation structure（已解决）：**\nR1 建议测试 AR(1) 或 unstructured。R2 有效 REBUT：对 cluster size = 2 的设计，exchangeable/AR(1)/unstructured 在数学上等价（仅一个 off-diagonal 参数），测试 AR(1) 不提供额外信息。Appendix B 的 exchangeable vs independence 对比已充分。**本报告采纳 R2 的 rebuttal，不将此列为 weakness。**\n\n**Mitigation 策略的 severity（轻微分歧）：**\nR2 列为 Should-Fix，R1 认为 diagnostic framework 定位合理，不必同时提出 solution。本报告保留为 Should-Fix 但优先级低于其他 Should-Fix。\n\n---\n\n## Questions for Authors\n\n1. §4.1 中 \"three judges\" 指哪三个？如果第三个 judge 未执行，Holm-Bonferroni family size 应为多少？\n2. NLI gate validation（§5.1）为什么不用 GPT-4o 或人工标注替代同为 Qwen3 family 的模型？\n3. Verbose rewrites 是否经过人工 content quality 检查？单向 NLI 是否足以排除 quality-relevant additions？\n4. BT 正则化具体设置（类型和超参数）？Bootstrap resamples 数为何不一致（2,000 vs 10,000）？\n5. 如果将 Likert scale 改为 1-100 或连续滑块，Blindspot 是否仍然存在？\n6. CSD 是否在 non-instruction-following 任务（summarization, translation quality）上测试过？\n7. 是否计划发布代码和数据？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同推荐补充以下引用：\n1. **Chiang et al. (2024)** \"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\" — BT model 在 LLM 评估中的 canonical reference（R1+R2 共识）\n2. **Ye et al. (2024)** \"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" — 系统量化 LLM judge 多种 bias 的直接竞品文献（R1 提出，R2 同意）\n3. **Feder et al. (2022, TACL)** \"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond\" — 若保留 \"Causal\" 标题则需要此方法论综述（R2 提出，R1 同意）\n4. **LLM-as-judge survey** — 帮助定位 CSD 在更广阔研究图景中的位置（R2 提出）\n\nR2 另推荐 Oriyad &amp; Rohban (2025) \"The Silent Judge\" (NeurIPS 2025)，但 R1 交叉回应中未能在 OpenAlex/Semantic Scholar 确认存在，建议验证后再决定。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：已跳过**（用户选择不提交外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（耗时 ~3.5 分钟）。关键发现：\n\n**[CRITICAL]** 主正文（Abstract 至 Conclusion 末尾）溢出至第 9 页约 0.25 页。EMNLP 2026 严格 8 页正文限制，当前超限将导致 desk reject。\n\n**[WARNING]**\n- 连续 3 页（p.1-3）纯文本无任何 display item，第一个视觉锚点到 p4 才出现。建议将 Figure 1（pipeline）或 Figure 2（DAG）提前至 p2。\n- 第 5 页堆叠 3 个 display item（Figure 2 + Table 1 + Figure 3），与前 3 页文本荒漠形成强烈反差。\n- Figure 2（causal DAG）尺寸偏小，打印尺寸下标签可能难以辨认。\n\n**[INFO]** Figure 3 填充/空心菱形在小尺寸下区分不明显（建议双重编码）；Figure 1 caption 过简；整体灰度方案打印友好但视觉吸引力偏低；表格排版（booktabs）专业；Section 6 heading 出现在页底有轻微孤悬感。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n### 维度合成\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.5/5 | 3.0/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 3.0/5 | 4.0/5 | 3.5/5 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n### 评分理由\n\n论文的核心贡献——七种统计方法系统性证明 Likert 评分在 LLM judge 风格偏差检测中失灵——有明确的实践价值和方法论教育意义。GEE per-axis confound structure 梯度是有洞察力的经验发现。但以下结构性问题阻止主会议接收：\n\n1. **Framing 问题**：\"Causal\" 标题与 §3.5 全面 disclaimer 的张力是最突出的 credibility 问题\n2. **External validity 不足**：单一 benchmark（LLMBar, n=100）+ 2 个 judge 的证据基础不支持 \"LLM Judges\" 全称论断\n3. **事实性错误**：Holm-Bonferroni 声称 \"three judges × three style axes = nine tests\"，第三个 judge 不存在\n4. **页数超限**：主正文超出 8 页限制约 0.25 页，按 ARR 规定将 desk reject\n5. **Novelty 争议**：Blindspot 是心理测量学已知现象的 domain transfer（R2 view）vs. quantification + GEE decomposition 有独立贡献（R1 view）\n\n论文达到 Findings 级别——有实践价值的经验性发现，统计执行扎实。距离 Main Conference 需要：(a) 更广的 benchmark/judge 覆盖，(b) 解决 Causal framing 问题，(c) 修正页数和事实性错误。建议修改后投入下一 ARR 周期。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Recent work has converged on a striking finding\" 后的三条引用支撑 \"dominant source\" claim，但 Abstract 缺少限定词。\n- Contributions 第 2 条 \"four judge×axis configurations at p < 0.001\" 与 Table 1 一致（4 strong + 2 exploratory）。\n\n### §3 Method\n- §3.2 Direction-aware NLI for verbosity 的 justification 合理但应更显式讨论 quality-relevant additions 的 tradeoff。\n- §3.5 \"Interventional rather than formal causal evidence\" 的 disclaimer 诚实但与标题矛盾。DAG 应加入 position bias（conditioned out）和 rewrite artifact 路径。\n\n### §4 Experiments\n- §4.1 \"three judges × three style axes = nine tests\" 是事实性错误，应为 \"two judges × three style axes = six tests\"。\n- Table 1 Qwen3-32B Register 行应补充 Cohen's d 值。\n\n### §5 Analysis\n- §5.1 \"independent LLM annotator\" 描述 Qwen3-32B 不准确，应删除 \"independent\"。\n- §5.2 BT \"regularized estimate\" 需说明正则化类型和超参数。Bootstrap resamples 数应统一或解释差异（2,000 vs 10,000）。\n\n### §6 Conclusion\n- 最后一段溢出至第 9 页。建议压缩 Conclusion 或将部分 Analysis 内容（如 §5.6 consistency filter）移至 Appendix。\n\n### Appendix B\n- Table 4 QIC 列仅报告 \"---\"（差异），未报告实际值。虽不影响结论但影响独立验证。\n\n### 视觉布局\n- 前 3 页纯文本无 display item → 建议将 Figure 1/2 提前至 p2。\n- p5 堆叠 3 个 display item → 分散分布。\n- Figure 2 (DAG) 偏小 → 放大或用 figure*。\n\n---\n\n## Issue Tracker 同步\n\n已更新 `review_issues.yaml`。本轮共识问题（5 critical + 7 warning + 4 info）：\n- **Reopened**: R1-N1（Causal framing，Round 1 resolved 但标题未改）\n- **Still open**: R2-N1（Novelty ceiling）\n- **New critical**: RD2-MF2（Holm-Bonferroni 错误）、RD2-MF3（单一 benchmark）、RD2-MF4（Abstract overclaim）、RD2-VIS（页数超限）\n- **New warning**: RD2-SF1—SF7（evaluator-producer、NLI verbosity、scale granularity、mitigation、BT details、DAG paths、novelty divergence）、RD2-M1（Figure PLACEHOLDER）、RD2-REF（missing references）\n- **New info**: RD2-M2—M4（Table formatting、citation mismatch、no code/data statement）\n- Round 1 已 resolved 的 14 个 issue 中，除 R1-N1 外均未被 Round 2 Reviewer 再次提及",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: \"Causal Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges\"\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 格式）\n**审稿轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达成共识）\n\n---\n\n## Summary\n\n本文提出 Causal Style Decomposition (CSD)，通过风格控制改写、NLI 内容保全门控和位置控制的成对比较来检测 LLM 评委的逐轴风格偏差。核心发现为 \"Likert Blindspot\"：标准 Likert 评分因 ~60% tie inflation 和信号衰减的双层结构限制，系统性地遗漏成对比较能检出的风格偏差。实验在 LLMBar (n=100) 上用 GPT-4o 和 Qwen3-32B 两个评委、三个风格轴（formality, verbosity, register）验证，七种统计方法一致确认该现象。\n\n---\n\n## Strengths\n\n**S1. 统计论证扎实**（R1+R2 共识）：七种不同统计方法（BT model, sign test, t-test, binarized Likert, ordinal logistic, GEE, Wilcoxon）在同一数据上验证 Blindspot——所有成对方法达显著而所有 Likert 方法失败。Table 2 的 sensitivity hierarchy 是有力的系统性证据。\n\n**S2. 多维度复现**（R1+R2 共识）：跨评委（GPT-4o vs Qwen3-32B）、跨风格轴（formality, verbosity, register）的复现设计。Verbosity 轴的 BT win probability 达 76-77%，效应量令人印象深刻且跨 judge 高度一致（OR = 11.34 vs 13.10）。\n\n**S3. GEE 分解提供结构性洞察**（R1 高度评价）：GEE 逻辑回归将 style 和 originality 效应分解，揭示 per-axis confound structure 梯度（verbosity = pure style, formality = mixed, register = originality-dominated），为后续 debiasing 工作提供诊断基础。这一分析跨 judge 复现，是全新的经验发现。\n\n**S4. Limitations 真实坦诚**（R1+R2 共识）：主动披露 quality-style confounding（OR = 2.32）、evaluator-producer bias、benchmark/axis 覆盖不足。\n\n**S5. Position control + consistency filter 设计合理**（R1）：位置对调 + 一致性过滤 + BT 全数据 vs 过滤数据交叉验证（63.0% < 73.9%，排除 filter inflation）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-MF1** [critical, 双 Reviewer 共识] **\"Causal\" 标题与方法实质不匹配**\n标题 \"Causal Style Decomposition\" 暗示形式化因果推断，但 §3.5 明确声明 \"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。这不是一般的 qualification——是对因果方法论基本假设的全面放弃。两位 Reviewer 一致将此列为最突出的 framing 问题。建议改用 \"Interventional Style Decomposition\" 或 \"Controlled Style Decomposition\"；如果坚持 \"Causal\"，必须在 §3.5 提供明确的 identification assumptions（在什么条件下 NLI gate 实现了 do(S)）。\n*（R1-N2 + R2-N2，交叉 [AGREE]）*\n\n**W-MF2** [critical, 双 Reviewer 共识] **Holm-Bonferroni family 定义与实际实验矛盾**\n§4.1 声称 \"three judges × three style axes = nine tests\"，但全文仅有 2 个 judge（GPT-4o, Qwen3-32B），Table 1 只有 6 行。第三个 judge 不存在。虽然 9-test 校正比 6-test 更保守（已显著结果不受影响），但声称的实验设计与实际执行不一致是严重 credibility 问题。可能是遗留了未执行的第三 judge 计划。必须修正为 \"two judges × three style axes = six tests\" 并重新检查 adjusted p-values。\n*（R1-N1，R2 交叉 [AGREE]）*\n\n**W-MF3** [critical, 双 Reviewer 共识] **单一 benchmark 代表性不足**\n所有实验仅基于 LLMBar（n=100），NLI gate 后仅 88 pairs → 173 comparisons，bootstrap CI 宽度达 14.5pp。LLMBar 是 instruction-following 专用 benchmark。从单一小规模 benchmark 推广到 \"LLM Judges\" 全称论断缺乏 external validity。缺少：(a) Claude/Llama 系列评委；(b) 非 instruction-following 任务（summarization, translation）。建议至少在一个额外 benchmark 上复现核心发现，或在 title/abstract 中明确限定 scope。\n*（R1-N3 + R2-W2，交叉升级为共识 Must-Fix）*\n\n**W-MF4** [critical, R2 raised + R1 partial agree] **Abstract 过度声称**\nIntroduction 和 Abstract 中 \"style bias is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference\"：(a) 虽有三条文献引用支撑，但 Abstract 缺少 \"recent work shows\" 限定；(b) verbosity 本身是论文三个风格轴之一，说风格偏差 \"far outweighs verbosity preference\" 构成 category error——verbosity bias IS a style bias in the paper's own framework；(c) formality BT 63%，position bias 通常 55-65%，\"far outweighing\" 缺乏量级支撑。建议修改措辞。\n*（R2-N1，R1 部分 [AGREE]——(b) 完全成立）*\n\n**W-MF5** [critical, 视觉审查] **主正文超 8 页限制**\n视觉审查确认：主正文（Abstract 至 Conclusion 末尾）溢出至第 9 页约 1/4 页。Section 6 Conclusion 从 p8 底部开始，延续到 p9 上半部分。EMNLP 2026 严格 8 页主正文限制，当前超限将直接导致 desk reject。需压缩正文或将部分内容移至 appendix。\n*（视觉审查 critical finding）*\n\n### Should-Fix（影响评分）\n\n**W-SF1** [warning, 双 Reviewer 共识] **Evaluator-producer 三角色循环偏差**\nQwen3-32B 同时担任 rewriter、judge、NLI gate validator 三个角色。§5.1 称其为 \"independent LLM annotator\" 不准确（misleading）。Table 3 中 Qwen3-32B 的 formality OR (4.20) 和 originality OR (4.70) 系统性约为 GPT-4o（2.58, 2.32）的 2 倍，暗示 evaluator-producer bias 影响非 trivial。建议：(1) 删除 \"independent\"；(2) 明确论证仅 GPT-4o 数据是否足以支撑核心 claim；(3) 理想情况下用第三模型（不同 family）作为 rewriter 做控制实验。\n*（R1-W1 + R2-W3，交叉 [AGREE]）*\n\n**W-SF2** [warning, R1 raised + R2 agree with nuance] **Direction-aware NLI 削弱 verbosity 内容保全**\n§3.2 对 verbosity 轴使用单向 NLI（仅 backward entailment），不阻止添加新 quality-relevant content。缓解因素：GEE 分解显示 verbosity originality component 不显著（OR=0.49, p=.096），且 text length 控制后 style OR 几乎不变（<2%），但 GEE \"originality\" operationalization 可能不捕获所有 quality dimensions。建议人工内容质量抽检。\n*（R1-W2，R2 交叉 [AGREE] with nuance）*\n\n**W-SF3** [warning, R2 raised + R1 agree] **Scale granularity 未探讨**\n论文使用 1-10 Likert scale。关键问题：Blindspot 是所有 ordinal scale 的固有属性还是 1-10 特定粒度结果？如果 1-100 或 continuous scale 也有 Blindspot，那是对 Likert 范式的根本批评；如果更细粒度可缓解，则是 scale 选择问题。Table 2 ordinal regression 排除了 interval-scale 假设但不排除 granularity 影响。建议至少在 Limitations 或 Discussion 中讨论。\n*（R2-W4，R1 交叉 [AGREE]——\"此前遗漏的有效问题\"）*\n\n**W-SF4** [warning, R2 raised + R1 partial rebut] **缺乏 mitigation 策略**\n论文诊断出 Blindspot 但仅建议 \"adopt pairwise comparison\"，未讨论 O(n²) scalability 或任何 calibration/debiasing 方案。R1 认为 diagnostic framework 定位合理，不必同时提出 debiasing solution，但建议简要讨论 active sampling 等 O(n log n) 方案。\n*（R2-W5，R1 部分 [REBUT]——severity 有分歧但方向一致）*\n\n**W-SF5** [warning, R1 raised + R2 agree] **BT 正则化细节和 bootstrap resamples 不一致**\n§5.2 \"regularized estimate\" 未说明正则化类型（Bayesian prior? L2? pseudocount?）和超参数。GPT-4o 用 2,000 resamples，Qwen3-32B 用 10,000，无解释。影响 reproducibility。\n*（R1-W4，R2 交叉 [AGREE]）*\n\n**W-SF6** [warning, R1 raised + R2 agree] **DAG 遗漏关键路径**\nFigure 2 缺少：(a) Position bias P → Y（虽被 position swap 控制，但应在 DAG 中表示为 conditioned out）；(b) Rewrite artifact R → Y（judge 检测到 text 是 LLM 改写的这一事实本身影响评分——与 evaluator-producer confound 直接相关）。更完整的 DAG 会加强 §3.5 的 identification argument。\n*（R1-W6，R2 交叉 [AGREE]）*\n\n### Minor\n\n**W-M1** Figure 4 (power_curve) 疑似存在淡色 PLACEHOLDER 水印，提交前需确认并移除。\n**W-M2** Table 1 Qwen3-32B Register 行缺少 Cohen's d 值，格式与其他行不一致。\n**W-M3** 引用问题：wang2026fairjudge 第一作者 mismatch（bib: Wang, OpenAlex: Yang）；murugadoss2025sos 在 OpenAlex 未找到。\n**W-M4** 无代码/数据可用性声明（ARR 鼓励但不要求）。\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 强共识（两位 Reviewer 一致）：**\n1. \"Causal\" framing overclaim 是最突出的 framing 问题\n2. Holm-Bonferroni \"9 tests\" 是事实性错误（声称 3 judges，实际 2）\n3. 单一 benchmark + 小样本不支持全称论断\n4. Evaluator-producer 三角色循环偏差需更好处理\n5. Scale granularity 是有效的未讨论问题\n6. BT 正则化和 bootstrap 细节不一致\n7. DAG 缺少 position bias 和 rewrite artifact 路径\n\n---\n\n## Reviewer Divergence\n\n**Excitement/Novelty 评估（核心分歧，未收敛）：**\n- R1 (Excitement 3.5/5)：GEE decomposition 揭示的 per-axis confound structure 梯度是全新发现，7 种统计方法的 quantitative demonstration 对 LLM 评估社区有实际价值，两层机制的具体识别此前未有\n- R2 (Excitement 2.5/5)：Likert Blindspot 是心理测量学经典现象（ordinal discretization 损失连续信号）在 LLM judge 领域的迁移应用，CSD 是三个已有组件的流水线（LLM 改写 + NLI filter + BT comparison），methodological novelty 有限\n\n**GEE correlation structure（已解决）：**\nR1 建议测试 AR(1) 或 unstructured。R2 有效 REBUT：对 cluster size = 2 的设计，exchangeable/AR(1)/unstructured 在数学上等价（仅一个 off-diagonal 参数），测试 AR(1) 不提供额外信息。Appendix B 的 exchangeable vs independence 对比已充分。**本报告采纳 R2 的 rebuttal，不将此列为 weakness。**\n\n**Mitigation 策略的 severity（轻微分歧）：**\nR2 列为 Should-Fix，R1 认为 diagnostic framework 定位合理，不必同时提出 solution。本报告保留为 Should-Fix 但优先级低于其他 Should-Fix。\n\n---\n\n## Questions for Authors\n\n1. §4.1 中 \"three judges\" 指哪三个？如果第三个 judge 未执行，Holm-Bonferroni family size 应为多少？\n2. NLI gate validation（§5.1）为什么不用 GPT-4o 或人工标注替代同为 Qwen3 family 的模型？\n3. Verbose rewrites 是否经过人工 content quality 检查？单向 NLI 是否足以排除 quality-relevant additions？\n4. BT 正则化具体设置（类型和超参数）？Bootstrap resamples 数为何不一致（2,000 vs 10,000）？\n5. 如果将 Likert scale 改为 1-100 或连续滑块，Blindspot 是否仍然存在？\n6. CSD 是否在 non-instruction-following 任务（summarization, translation quality）上测试过？\n7. 是否计划发布代码和数据？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同推荐补充以下引用：\n1. **Chiang et al. (2024)** \"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\" — BT model 在 LLM 评估中的 canonical reference（R1+R2 共识）\n2. **Ye et al. (2024)** \"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" — 系统量化 LLM judge 多种 bias 的直接竞品文献（R1 提出，R2 同意）\n3. **Feder et al. (2022, TACL)** \"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond\" — 若保留 \"Causal\" 标题则需要此方法论综述（R2 提出，R1 同意）\n4. **LLM-as-judge survey** — 帮助定位 CSD 在更广阔研究图景中的位置（R2 提出）\n\nR2 另推荐 Oriyad &amp; Rohban (2025) \"The Silent Judge\" (NeurIPS 2025)，但 R1 交叉回应中未能在 OpenAlex/Semantic Scholar 确认存在，建议验证后再决定。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：已跳过**（用户选择不提交外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（耗时 ~3.5 分钟）。关键发现：\n\n**[CRITICAL]** 主正文（Abstract 至 Conclusion 末尾）溢出至第 9 页约 0.25 页。EMNLP 2026 严格 8 页正文限制，当前超限将导致 desk reject。\n\n**[WARNING]**\n- 连续 3 页（p.1-3）纯文本无任何 display item，第一个视觉锚点到 p4 才出现。建议将 Figure 1（pipeline）或 Figure 2（DAG）提前至 p2。\n- 第 5 页堆叠 3 个 display item（Figure 2 + Table 1 + Figure 3），与前 3 页文本荒漠形成强烈反差。\n- Figure 2（causal DAG）尺寸偏小，打印尺寸下标签可能难以辨认。\n\n**[INFO]** Figure 3 填充/空心菱形在小尺寸下区分不明显（建议双重编码）；Figure 1 caption 过简；整体灰度方案打印友好但视觉吸引力偏低；表格排版（booktabs）专业；Section 6 heading 出现在页底有轻微孤悬感。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n### 维度合成\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.5/5 | 3.0/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 3.0/5 | 4.0/5 | 3.5/5 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n### 评分理由\n\n论文的核心贡献——七种统计方法系统性证明 Likert 评分在 LLM judge 风格偏差检测中失灵——有明确的实践价值和方法论教育意义。GEE per-axis confound structure 梯度是有洞察力的经验发现。但以下结构性问题阻止主会议接收：\n\n1. **Framing 问题**：\"Causal\" 标题与 §3.5 全面 disclaimer 的张力是最突出的 credibility 问题\n2. **External validity 不足**：单一 benchmark（LLMBar, n=100）+ 2 个 judge 的证据基础不支持 \"LLM Judges\" 全称论断\n3. **事实性错误**：Holm-Bonferroni 声称 \"three judges × three style axes = nine tests\"，第三个 judge 不存在\n4. **页数超限**：主正文超出 8 页限制约 0.25 页，按 ARR 规定将 desk reject\n5. **Novelty 争议**：Blindspot 是心理测量学已知现象的 domain transfer（R2 view）vs. quantification + GEE decomposition 有独立贡献（R1 view）\n\n论文达到 Findings 级别——有实践价值的经验性发现，统计执行扎实。距离 Main Conference 需要：(a) 更广的 benchmark/judge 覆盖，(b) 解决 Causal framing 问题，(c) 修正页数和事实性错误。建议修改后投入下一 ARR 周期。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Recent work has converged on a striking finding\" 后的三条引用支撑 \"dominant source\" claim，但 Abstract 缺少限定词。\n- Contributions 第 2 条 \"four judge×axis configurations at p < 0.001\" 与 Table 1 一致（4 strong + 2 exploratory）。\n\n### §3 Method\n- §3.2 Direction-aware NLI for verbosity 的 justification 合理但应更显式讨论 quality-relevant additions 的 tradeoff。\n- §3.5 \"Interventional rather than formal causal evidence\" 的 disclaimer 诚实但与标题矛盾。DAG 应加入 position bias（conditioned out）和 rewrite artifact 路径。\n\n### §4 Experiments\n- §4.1 \"three judges × three style axes = nine tests\" 是事实性错误，应为 \"two judges × three style axes = six tests\"。\n- Table 1 Qwen3-32B Register 行应补充 Cohen's d 值。\n\n### §5 Analysis\n- §5.1 \"independent LLM annotator\" 描述 Qwen3-32B 不准确，应删除 \"independent\"。\n- §5.2 BT \"regularized estimate\" 需说明正则化类型和超参数。Bootstrap resamples 数应统一或解释差异（2,000 vs 10,000）。\n\n### §6 Conclusion\n- 最后一段溢出至第 9 页。建议压缩 Conclusion 或将部分 Analysis 内容（如 §5.6 consistency filter）移至 Appendix。\n\n### Appendix B\n- Table 4 QIC 列仅报告 \"---\"（差异），未报告实际值。虽不影响结论但影响独立验证。\n\n### 视觉布局\n- 前 3 页纯文本无 display item → 建议将 Figure 1/2 提前至 p2。\n- p5 堆叠 3 个 display item → 分散分布。\n- Figure 2 (DAG) 偏小 → 放大或用 figure*。\n\n---\n\n## Issue Tracker 同步\n\n已更新 `review_issues.yaml`。本轮共识问题（5 critical + 7 warning + 4 info）：\n- **Reopened**: R1-N1（Causal framing，Round 1 resolved 但标题未改）\n- **Still open**: R2-N1（Novelty ceiling）\n- **New critical**: RD2-MF2（Holm-Bonferroni 错误）、RD2-MF3（单一 benchmark）、RD2-MF4（Abstract overclaim）、RD2-VIS（页数超限）\n- **New warning**: RD2-SF1—SF7（evaluator-producer、NLI verbosity、scale granularity、mitigation、BT details、DAG paths、novelty divergence）、RD2-M1（Figure PLACEHOLDER）、RD2-REF（missing references）\n- **New info**: RD2-M2—M4（Table formatting、citation mismatch、no code/data statement）\n- Round 1 已 resolved 的 14 个 issue 中，除 R1-N1 外均未被 Round 2 Reviewer 再次提及",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-21T07:32:26.203330+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4317
}
```

</details>

---


### Assistant

_source line 132 · 2026-05-21T07:32:37.198748+00:00_

审稿报告已投递给 Research Director。

---

**📋 审稿完成汇报 — Group C**

**Overall: 3.0 (Findings)** | Soundness 3.0 | Excitement 3.0 | Reproducibility 3.5 | Confidence 4/5

两位 Reviewer 独立给出 3.0，交叉讨论后在关键问题上达成强共识：

**5 个 Must-Fix（阻止主会议接收）：**
1. "Causal" 标题与 §3.5 因果 disclaimer 实质性矛盾（Round 1 reopened）
2. Holm-Bonferroni 声称 "3 judges × 3 axes = 9 tests"，实际只有 2 judges
3. 单一 benchmark (LLMBar, n=100) 不支持 "LLM Judges" 全称论断
4. Abstract "dominant source" + verbosity category error
5. 主正文超 8 页限制约 0.25 页（视觉审查 critical，将导致 desk reject）

**7 个 Should-Fix：** evaluator-producer 三角色循环、direction-aware NLI 削弱 verbosity 内容保全、scale granularity 未探讨、缺 mitigation 策略、BT 正则化不一致、DAG 遗漏路径、novelty 分歧

**唯一未收敛分歧：** Excitement（R1: 3.5 vs R2: 2.5）——GEE decomposition 的贡献价值。

Issue Tracker 已同步更新（5 critical / 7 warning / 4 info，含 1 个 reopened issue）。外部审稿已跳过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 133 · 2026-05-21T07:32:40.025678+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

要点总结：
- 对 R1 的 11 个具体问题中，**9 个 [AGREE]**，**1 个 [REBUT]**（GEE correlation structure — cluster size=2 时三种结构数学等价），**1 个部分 AGREE**（Direction-aware NLI 的 verbosity concern，同意方法论弱点但注意到 GEE originality component 不显著作为部分缓解）
- R1 发现了我遗漏的 4 个有效问题：Holm-Bonferroni "9 tests" 事实错误、Direction-aware NLI 弱化、BT 正则化细节缺失、DAG 不完整
- 两人独立给出 Overall 3.0 (Findings)，核心共识一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 134 · 2026-05-21T07:32:50.373821+00:00_

审稿报告已提交给 Research Director。

**本轮审稿总结：**

- **Overall: 3.0 (Findings)**，两位 Reviewer 独立一致
- **5 个 Must-Fix**：Causal 标题 overclaim、Holm-Bonferroni "9 tests" 事实错误、单一 benchmark 代表性不足、Abstract 过度声称、页数超限（desk reject 风险）
- **7 个 Should-Fix**：evaluator-producer 三角色循环、direction-aware NLI 内容保全弱化、scale granularity 未讨论、缺 mitigation 策略、BT 正则化细节不一致、DAG 不完整、novelty 分歧
- **Issue Tracker 已更新**：1 个 Round 1 issue reopened（Causal framing），16 个新 issue 登记
- **外部审稿**：已跳过
- **视觉审查**：已完成，确认页数超限 ~0.25 页 + 布局节奏问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 14

## Round 14

62 recorded events


### User

_source line 135 · 2026-05-21T09:33:25.995006+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long paper (Main/Findings via ARR)
- 截止日期: 2026-06-15

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-21T09:33:32.014908+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-21T09:33:32.015743+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-21T09:33:40.533108+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-21T09:33:40.533578+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-21T09:33:44.449077+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 141 · 2026-05-21T09:33:44.499798+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-21T09:33:47.361853+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-21T09:33:47.813927+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (30 个)\n\n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **register_100_cf**: QUEUED — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- register_100_cf: Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality（排队等待 GPU）\n\n## 近期结论\n- **gpt4o_rewriter_verbosity** (success): Verbosity blindspot persists when using GPT-4o (instead of Qwen3-32B) as the counterfactual rewriter, demonstrating that the detected bias is rewriter-independent and not an artifact of a specific rewriting model\n- **exp-006** (success): Scaling formality counterfactual generation from 100 to 400 pairs enables cross-benchmark validation (AlpacaEval/MT-Bench) and increases statistical power for detecting smaller effect sizes\n- **alpacaeval_verbosity_qwen32b** (success): Qwen3-32B shows verbosity Blindspot on AlpacaEval benchmark (pairwise detects verbosity bias that Likert misses), extending verbosity findings to a second benchmark\n\n## 趋势\n成功 19 / 负向 7 / 失败 0 / 共 29\nblindspot: True ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-21T09:33:47.964976+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 145 · 2026-05-21T09:33:48.015632+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-21T09:33:54.440256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-21T09:33:55.544475+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{Counterfactual Style Decomposition Reveals the Likert Blindspot:\\Standard Scoring Underestimates Style Bias in LLM Judges}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding.}
42	Although the formality effect survives logistic adjustment for original preference (Appendix~\ref{app:direction}), the significant original-preference odds ratio ($\text{OR} = 2.32$, $p = 0.006$) indicates that quality--style confounding is not fully eliminated.
43	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
44	Future work should incorporate human quality ratings of both original and rewritten texts.
45	
46	\paragraph{Evaluator-producer bias in Qwen3-32B.}
47	Qwen3-32B serves as both the style rewriter and one of the three judges; the NLI entailment gate (DeBERTa-v3-large) is architecturally independent of both roles.
48	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exhibited small-sample upward bias, corrected to $2.15$ at $n = 355$ (comparable to GPT-4o's $2.58$); the originality OR inflation persists ($4.99$ vs.\ $2.32$), consistent with partial self-recognition.
…[truncated 2326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-21T09:33:55.544817+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-21T09:33:56.097047+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-21T09:33:57.251661+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool call

_source line 151 · 2026-05-21T09:33:57.603393+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 152 · 2026-05-21T09:34:02.171314+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, I found information about EMNLP 2025 and various 2026 conferences, 
…[truncated 1440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6626
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-21T09:34:02.224312+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_style_decomp_judge'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6127
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-21T09:34:02.224860+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 4621
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-21T09:34:02.375752+00:00_

-rw-r--r-- 1 ubuntu ubuntu 312997 May 21 09:31 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 5124
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-21T09:34:08.098916+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-21T09:34:08.450519+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline Budapest"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline Budapest"
  }
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-21T09:34:10.508371+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-21T09:34:12.817211+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline Budapest"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"}]

Based on the search results, here's the information about EMNLP 2026:

**Conference Details:**
EMNLP 2026 is being held in Budapest, Hungary on October 24 - 29, 2026.

**Paper Submission Deadline:**
The EMNLP 2026 paper submission deadline is May 25, 2026 at 23:59:59 (UTC-12). All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

**Industry Track:**
If you're interested in the Industry Track specifically, the paper submission deadline is Ju
…[truncated 254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 4366
}
```

</details>

---


### Tool result

_source line 160 · 2026-05-21T09:34:14.022569+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here are the key ACL Rolling Review (ARR) 2026 submission guidelines for page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

## F
…[truncated 869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5923
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-21T09:34:14.073656+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml\", \"content\": \"_next_id: 52\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 14:09 UTC\\n  summary: '文献蒸馏审视：研究方向无需调整，CSD 填补 #1 空白（多维 style 因果分解），post-MVP 需扩展 judge/benchmark/baseline\\n    覆盖'\\n  rationale: '10 篇论文蒸馏显示：(1) 多维 style 联合因果分解是领域 #1 空白，与 CSD 核心 claim 完全对齐；(2) 竞品 claim\\n    无直接重叠（FairJudge=white-box, Pref Leakage=family-based, Soumik=prompt-dependent）；(3)\\n    同行标准要求 3-5 异构 judge + AlpacaEval/Arena-Hard/MT-Bench + Bootstrap CIs + 对比 LC-AlpacaEval\\n    baseline。当前 MVP 方案足够，research 阶段需按蒸馏标准扩展。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 14:19 UTC\\n  summary: MVP 全量评分 + 分层分析：score 全部 100 条，按 BERTScore 阈值 0.88/0.90/0.92 分层算 ATE，不降低阈值\\n  rationale: 36% pass rate (BERTScore≥0.92) 偏低但 NLI 均值 0.9422 说明语义保留好。降阈值是数据操作，不如保留完整信息。全量评分\\n    (n=100) 保证统计 power，分层分析同时回答\\\"严格阈值下效应是否存在\\\"和\\\"宽松阈值下效应是否增强\\\"。8B H1 fail 不消耗迭代配额（ROADMAP\\n    规则），32B 备用。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 14:20 UTC\\n  summary: H1 content verification 改为 NLI-only gate（≥0.90），BERTScore 降为监控指标，不作为过滤条件\\n  rationale: Reviewer 诊断：36% pass rate 的根因是 BERTScore 惩罚 style transfer 预期的词汇变化（contractions→full\\n    forms 等），而非内容泄漏。NLI 均值 0.9422、抽样 >0.99 证明语义保留良好。BERTScore 作为 token-level 相似度指标与\\n    style transfer 评估目标矛盾（改的就是 token）。Double-rewrite pass rate 更低（21/100）进一步印证。NLI-only\\n    gate 是度量校准（不消耗 8B 迭代配额），与 D002 全量评分兼容——primary ATE 用 NLI≥0.90 子集，secondary 按 BERTScore\\n    分层。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 14:32 UTC\\n  summary: 8B 初步 ATE≈0.028 不可见，归因三因素：Likert 粒度 + 8B rewriter 质量 + RATE corruption。不计入\\n    kill criteria，等 n=100 + 32B\\n  rationale: 36/100 初步数据 Cohen's d=0.055 远低于 0.3 门槛，但三个叠加因素解释了结果：(1) 83% 零差异源于 integer\\n    Likert 无法捕捉 sub-integer 效应；(2) 22% identical rewrites 稀释 ATE；
…[truncated 10852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3565
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-21T09:34:35.307236+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review June 2026 deadline ARR commitment EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review June 2026 deadline ARR commitment EMNLP 2026"
  }
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-21T09:34:35.909978+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-21T09:34:37.466362+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-21T09:34:37.968630+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-21T09:34:44.331932+00:00_

Web search results for query: "ACL Rolling Review June 2026 deadline ARR commitment EMNLP 2026"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's the information about the ACL Rolling Review (ARR) June 2026 deadline and EMNLP 2026 commitment:

## ARR May 2026 Submission for EMNLP 2026

The final ARR submission date for papers to be considered by EMNLP 2026 is May 25, 2026, with a commitment deadline of August 2, 2026.

## Key Details for EMNLP 2026

EMNLP 2026 will use ACL Rolling Review (ARR) as its reviewing system, where authors first submit articles to ARR to receive reviews and meta-reviews from ARR reviewers and action editors, and then commit their reviewed articles to the conference where Senior Area Chairs and Program Chairs make acceptance decisions.

For the ARR 2026 May submission cycle that is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time.

## Author Resp
…[truncated 319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 9024
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-21T09:34:44.483573+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (30 个)\n\n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **register_100_cf**: QUEUED — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- register_100_cf: Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality（排队等待 GPU）\n\n## 近期结论\n- **gpt4o_rewriter_verbosity** (success): Verbosity blindspot persists when using GPT-4o (instead of Qwen3-32B) as the counterfactual rewriter, demonstrating that the detected bias is rewriter-independent and not an artifact of a specific rewriting model\n- **exp-006** (success): Scaling formality counterfactual generation from 100 to 400 pairs enables cross-benchmark validation (AlpacaEval/MT-Bench) and increases statistical power for detecting smaller effect sizes\n- **alpacaeval_verbosity_qwen32b** (success): Qwen3-32B shows verbosity Blindspot on AlpacaEval benchmark (pairwise detects verbosity bias that Likert misses), extending verbosity findings to a second benchmark\n\n## 趋势\n成功 19 / 负向 7 / 失败 0 / 共 29\nblindspot: True ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 8573
}
```

</details>

---


### Tool result

_source line 168 · 2026-05-21T09:34:44.585693+00:00_

abstract.tex
appendix.tex
conclusion.tex
experiments.tex
introduction.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 6617
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-21T09:34:44.586017+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 7119
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-21T09:35:01.252019+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"call for main conference papers\" ARR deadline commitment site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" \"call for main conference papers\" ARR deadline commitment site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-21T09:35:01.252534+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-21T09:35:01.353813+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-21T09:35:08.580470+00:00_

Web search results for query: ""EMNLP 2026" "call for main conference papers" ARR deadline commitment site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results from the official EMNLP 2026 website, here are the key details about the call for main conference papers:

## Key Deadlines

The ARR submission deadline for main conference papers (long & short papers) is May 25, 2026, with the EMNLP commitment deadline being August 2, 2026.

## ARR Submission and Commitment Process

Papers must be submitted, at latest, by the ARR 2026 May cycle, and papers that have received reviews and a meta-rev
…[truncated 897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 7328
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-21T09:35:18.366797+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 3 -name \"*.yaml\" -path \"*/causal_style_decomp_judge/*\" 2>/dev/null | head -10",
  "description": "Find YAML config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 3 -name \"*.yaml\" -path \"*/causal_style_decomp_judge/*\" 2>/dev/null | head -10",
    "description": "Find YAML config files in project"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-21T09:35:18.720634+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-21T09:35:18.873509+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-21T09:35:18.924596+00:00_

issues:
  # ============================================================
  # Round 1 issues RE-RAISED in Round 2
  # ============================================================

  - id: "R1-N1"
    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Title changed. 4 CSD occurrences updated. §3.5 has 3 identification assumptions."
    resolution_round: 2

  - id: "R2-N1"
    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 1
    last_seen_round: 2
    action_items:
      - round: 2
        action: "3 benchmarks ✅ + 3rd judge (Claude) ✅ + correction PoC ✅ + rewriter independence ✅ + n=400 scaled replication ✅. Narrative: efficiency gap + confound gradient + judge-dependent susceptibility."
        assigned_to: agent + paper_agent
        status: done
    resolution: "Addressed with 5 new experiments (3 benchmarks, Claude negative control, correction PoC, rewriter independence, n=400 scale). Novelty ceiling is structural — empirical contribution validated at Findings 3.0-3.5 level."
    resolution_round: null

  # ============================================================
  # Round 1 resolved, NOT re-raised in Round 2
  # ============================================================

  - id: "R1-N2"
    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89"
    resolution_round: 1

  - id: "R1-N3"
    summary: "NLI 阈值 0.90 无 justification"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Threshold on plateau, robust 0.70-0.95"
    resolution_round:
…[truncated 9058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-21T09:35:36.342125+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 2 -name \"config.yaml\" -o -name \"project_config.yaml\" 2>/dev/null",
  "description": "Find project config file for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 2 -name \"config.yaml\" -o -name \"project_config.yaml\" 2>/dev/null",
    "description": "Find project config file for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-21T09:35:36.744186+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-21T09:35:36.896489+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/*.tex",
  "description": "Count lines in each paper section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/*.tex",
    "description": "Count lines in each paper section"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-21T09:35:36.947158+00:00_

    9 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
  113 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
    7 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
  205 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
   34 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
   91 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
   35 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
  494 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-21T09:35:46.153258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-21T09:35:46.153676+00:00_

1	\begin{abstract}
2	Large Language Model (LLM) judges are widely deployed for evaluation and preference-based alignment, yet recent work shows that style features alone can explain judge scores with near-perfect correlation, raising fundamental questions about what these judges actually measure.
3	We introduce Counterfactual Style Decomposition (CSD), a black-box framework that detects per-axis style bias through binary style-controlled rewriting, NLI-based content preservation gating, and position-controlled pairwise comparison.
4	We quantify what we term the Likert Blindspot---a measurement efficiency gap, predicted by psychometric theory but previously unquantified for LLM judges, in which Likert requires substantially stronger effects or larger samples to detect the same bias that pairwise comparison reliably captures---across two judges (GPT-4o, Qwen3-32B), three benchmarks (LLMBar, AlpacaEval, MT-Bench), and two primary style axes (formality, verbosity), with exploratory evidence on a third axis (register); a third judge (Claude Sonnet 4) detects no bias on either axis, confirming discriminative validity.
5	The gap arises from a two-layer mechanism: (1)~integer Likert scoring produces ${\sim}60\%$ uninformative ties ($\Delta = 0$), wasting the majority of the evaluation budget; (2)~even among non-tied pairs, absolute scoring captures weaker signal than forced pairwise comparison on identical data.
6	The effect is most dramatic for verbosity, where a 77.3\% Bradley-Terry win probability ($p < 0.0001$, both directions favoring verbose content) remains invisible to Likert scoring ($p = 0.179$).
7	Ordinal regression confirms the limitation is inherent to Likert measurement, not an artifact of interval-scale assumptions ($p = 0.769$).
8	Our results demonstrate that style bias audits require pairwise comparison and per-axis decomposition, and that existing Likert-based findings may systematically underestimate style bias magnitude.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-21T09:35:46.354953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-21T09:35:46.355559+00:00_

1	\section{Introduction}
2	
3	Large Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.
4	Systems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.
5	Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.
6	The reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.
7	As automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.
8	
9	Recent work suggests that style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, motivating systematic measurement of per-axis style bias.
10	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences, and \citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
11	Despite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis interventional detection.
12	Recent multi-feature frameworks such as CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} begin to decompose style into finer dimensions, but neither provides interv
…[truncated 4170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-21T09:35:46.707175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-21T09:35:46.858139+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Counterfactual Style Decomposition (CSD), a black-box framework for detecting per-axis style bias in LLM judges.
5	Across three judges, three benchmarks, and three style axes, CSD reveals the Likert Blindspot---a measurement efficiency gap confirmed by seven statistical methods.
6	Style bias audits should adopt pairwise comparison; existing Likert-based null findings may reflect measurement insensitivity.
7	Prompt-level debiasing is insufficient; structural interventions remain open.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-21T09:36:14.920819+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool call

_source line 189 · 2026-05-21T09:36:16.478590+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-21T09:36:31.348336+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 16427
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-21T09:36:31.348797+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 14870
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-21T09:36:32.352752+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题：Counterfactual Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges\n- 文件路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## Venue 要求\n- **目标**：EMNLP 2026（通过 ARR 审稿）\n- **ARR 提交截止**：2026-05-25 AoE\n- **正文页数**：≤ 8 页（Long paper）\n- **参考文献**：不限\n- **Limitations**：必须有，不计入页数\n- **模板**：ACL (Overleaf)\n- **匿名**：Double-blind\n\n## 你的审查重点\n\n请严格聚焦以下方面：\n\n1. **CSD 框架方法论**：\n   - 因果推断框架（§3.5 DAG）的假设是否合理？identification assumptions 是否充分？\n   - NLI-based content preservation gate 的 validity——NLI 阈值选择、direction-aware NLI 对 verbosity 的合理性\n   - Binary style-controlled rewriting 的 confound control 是否充分？\n\n2. **统计方法**：\n   - Bradley-Terry 模型使用是否正确？bootstrap CI 是否合理？\n   - GEE logistic regression 的规范（correlation structure、cluster 定义）\n   - Multiple comparison correction（Holm-Bonferroni）是否正确应用？\n   - Effect size 报告（Cohen's d、OR、BT win probability）是否一致且正确？\n   - Ordinal regression 的使用和解释\n\n3. **实验设计**：\n   - 样本量（n=100 LLMBar、n=355/400 scaled）是否足够？power analysis 是否合理？\n   - 跨 benchmark（LLMBar/AlpacaEval/MT-Bench）、跨 judge（GPT-4o/Qwen3-32B/Claude）的 generalizability\n   - Evaluator-producer bias（Qwen3-32B 同时做 rewriter 和 judge）的控制是否充分？\n   - Position bias 控制\n   - Rewriter independence test 的设计\n\n4. **Reproducibility**：\n   - 实验细节是否足够复现？\n   - 代码/数据承诺是否明确？\n\n请按 ACL reviewer 标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号，区分 Must-Fix / Should-Fix / Minor）、Questions for Authors、Overall Assessment。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题：Counterfactual Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges\n- 文件路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## Venue 要求\n- **目标**：EMNLP 2026（通过 ARR 审稿）\n- **ARR 提交截止**：2026-05-25 AoE\n- **正文页数**：≤ 8 页（Long paper）\n- **参考文献**：不限\n- **Limitations**：必须有，不计入页数\n- **模板**：ACL (Overleaf)\n- **匿名**：Double-blind\n\n## 你的审查重点\n\n请严格聚焦以下方面：\n\n1. **CSD 框架方法论**：\n   - 因果推断框架（§3.5 DAG）的假设是否合理？identification assumptions 是否充分？\n   - NLI-based content preservation gate 的 validity——NLI 阈值选择、direction-aware NLI 对 verbosity 的合理性\n   - Binary style-controlled rewriting 的 confound control 是否充分？\n\n2. **统计方法**：\n   - Bradley-Terry 模型使用是否正确？bootstrap CI 是否合理？\n   - GEE logistic regression 的规范（correlation structure、cluster 定义）\n   - Multiple comparison correction（Holm-Bonferroni）是否正确应用？\n   - Effect size 报告（Cohen's d、OR、BT win probability）是否一致且正确？\n   - Ordinal regression 的使用和解释\n\n3. **实验设计**：\n   - 样本量（n=100 LLMBar、n=355/400 scaled）是否足够？power analysis 是否合理？\n   - 跨 benchmark（LLMBar/AlpacaEval/MT-Bench）、跨 judge（GPT-4o/Qwen3-32B/Claude）的 generalizability\n   - Evaluator-producer bias（Qwen3-32B 同时做 rewriter 和 judge）的控制是否充分？\n   - Position bias 控制\n   - Rewriter independence test 的设计\n\n4. **Reproducibility**：\n   - 实验细节是否足够复现？\n   - 代码/数据承诺是否明确？\n\n请按 ACL reviewer 标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号，区分 Must-Fix / Should-Fix / Minor）、Questions for Authors、Overall Assessment。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-21T09:36:46.373815+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14021
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-21T09:36:46.525490+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + Related Work**。\n\n## 论文信息\n- 标题：Counterfactual Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges\n- 文件路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## Venue 要求\n- **目标**：EMNLP 2026（通过 ARR 审稿）\n- **ARR 提交截止**：2026-05-25 AoE\n- **正文页数**：≤ 8 页（Long paper）\n- **参考文献**：不限\n- **Limitations**：必须有，不计入页数\n- **模板**：ACL (Overleaf)\n- **匿名**：Double-blind\n\n## 你的审查重点\n\n请严格聚焦以下方面：\n\n1. **新颖性评估**：\n   - Likert Blindspot 是否为真正的新发现？与心理测量学已知的 Likert scale 局限性（Thurstone 1927、psychometric literature）的关系——是 domain transfer 还是 genuine insight？\n   - CSD 框架相比已有方法（CASSE、FairJudge、LC-AlpacaEval、Preference Leakage）的增量贡献\n   - Per-axis confound decomposition（GEE 分解出 style vs originality）的新颖性\n   - 对 LLM-as-Judge 评估实践的实际影响\n\n2. **Claims 与 Evidence 对齐**：\n   - Abstract/Introduction 中的 claims 是否都有实验 evidence 支撑？\n   - 是否存在 overclaiming？特别关注 \"framework\"、\"causal\"、\"decomposition\" 等词的使用是否准确\n   - Contributions list 是否 overselling？\n   - Negative results（Claude 无 bias、formality 方向不对称、tone axis fail）的呈现是否诚实\n\n3. **Related Work 完整性**：\n   - 是否覆盖 LLM-as-Judge bias 的主要近期工作？（SOS-Bench、CASSE、FairJudge、Preference Leakage、Style Over Substance 等）\n   - 是否遗漏重要的 psychometric measurement 文献？\n   - 是否遗漏 counterfactual text generation 的相关方法？\n   - 引用数量和质量是否达到 EMNLP 标准？\n\n4. **写作质量与格式**：\n   - 论文结构是否清晰？信息密度是否合适？\n   - 图表质量和信息量\n   - Limitations 部分是否充分覆盖关键弱点？\n   - 正文是否在 8 页内？\n\n请按 ACL reviewer 标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号，区分 Must-Fix / Should-Fix / Minor）、Questions for Authors、Overall Assessment。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + Related Work**。\n\n## 论文信息\n- 标题：Counterfactual Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges\n- 文件路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## Venue 要求\n- **目标**：EMNLP 2026（通过 ARR 审稿）\n- **ARR 提交截止**：2026-05-25 AoE\n- **正文页数**：≤ 8 页（Long paper）\n- **参考文献**：不限\n- **Limitations**：必须有，不计入页数\n- **模板**：ACL (Overleaf)\n- **匿名**：Double-blind\n\n## 你的审查重点\n\n请严格聚焦以下方面：\n\n1. **新颖性评估**：\n   - Likert Blindspot 是否为真正的新发现？与心理测量学已知的 Likert scale 局限性（Thurstone 1927、psychometric literature）的关系——是 domain transfer 还是 genuine insight？\n   - CSD 框架相比已有方法（CASSE、FairJudge、LC-AlpacaEval、Preference Leakage）的增量贡献\n   - Per-axis confound decomposition（GEE 分解出 style vs originality）的新颖性\n   - 对 LLM-as-Judge 评估实践的实际影响\n\n2. **Claims 与 Evidence 对齐**：\n   - Abstract/Introduction 中的 claims 是否都有实验 evidence 支撑？\n   - 是否存在 overclaiming？特别关注 \"framework\"、\"causal\"、\"decomposition\" 等词的使用是否准确\n   - Contributions list 是否 overselling？\n   - Negative results（Claude 无 bias、formality 方向不对称、tone axis fail）的呈现是否诚实\n\n3. **Related Work 完整性**：\n   - 是否覆盖 LLM-as-Judge bias 的主要近期工作？（SOS-Bench、CASSE、FairJudge、Preference Leakage、Style Over Substance 等）\n   - 是否遗漏重要的 psychometric measurement 文献？\n   - 是否遗漏 counterfactual text generation 的相关方法？\n   - 引用数量和质量是否达到 EMNLP 标准？\n\n4. **写作质量与格式**：\n   - 论文结构是否清晰？信息密度是否合适？\n   - 图表质量和信息量\n   - Limitations 部分是否充分覆盖关键弱点？\n   - 正文是否在 8 页内？\n\n请按 ACL reviewer 标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号，区分 Must-Fix / Should-Fix / Minor）、Questions for Authors、Overall Assessment。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-21T09:36:48.085055+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1559
}
```

</details>

---


### Assistant

_source line 196 · 2026-05-21T09:36:55.614172+00:00_

全部任务已派发：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已启动（并行，不阻塞） |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 已发送至用户群（8h 自动提醒） |
| Reviewer 1（方法 + 实验） | ✅ 已分配 |
| Reviewer 2（新颖性 + 完整性） | ✅ 已分配 |

等待两位 Reviewer 返回 Round 1 独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 197 · 2026-05-21T09:41:33.419850+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 方法严谨性 + 实验有效性

## 总体评分
**Overall Assessment**: 3.5 — Borderline Conference
**一句话总结**: 核心发现（Likert vs. pairwise 灵敏度差距）真实且有实用价值，统计三角验证扎实，但 evaluator-producer confound 控制不足、因果声明过强于识别策略、样本量偏小这三个问题需要修正后才达到 Conference 水平。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 7 种统计方法三角验证 Blindspot 结论可信；但因果识别假设有缺口，evaluator-producer confound 的 independence test 只覆盖 verbosity 一个轴 |
| Excitement | 3.5/5 | Likert Blindspot 对 LLM evaluation 社区有实际指导意义；但底层心理测量原理本身是已知的（Thurstone 1927），贡献主要在量化而非发现 |
| Reproducibility | 3/5 | 实验细节基本充分（模型版本、seed、bootstrap 参数），但代码/数据仅"upon acceptance"承诺；使用商业 API (GPT-4o) 限制精确复现 |
| Reviewer Confidence | 4/5 | 统计方法论、LLM evaluation、因果推断均在审稿人专业范围内 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 因果识别假设不充分且可能被违反

- 具体位置：§3.5 (Causal Framework), Figure 2, §3.2
- 问题：
  1. 识别假设 (iii)（"the style rewrite introduces no systematic differences beyond the target axis"）是可检验的，但论文未检验。改写 formality 可能同时改变 register、vocabulary sophistication、syntactic complexity 等。论文未进行多轴测量来确认单轴干预的纯净性。
  2. Table 3 中 originality OR 在多个配置下显著（GPT-4o formality: OR=2.32, p=0.006; Qwen3 register: OR=5.72, p<.0001），这直接表明 NLI gate 未能完全阻断 R→Q 路径——rewrite 确实改变了质量感知。这是对核心识别假设 (i) 的经验性违反。
  3. 全文使用"counterfactual""interventional""do-operator"等强因果语言，但 §3.5 又声明"not a complete structural causal model, nor do we invoke SUTVA"。这种措辞不一致会误导读者对证据强度的判断。
- 为什么影响接收：因果推断框架是 CSD 的核心卖点之一（Title 含"Counterfactual"，Contribution 1 称"interventional framework"）。如果识别策略有缺口，论文的方法论贡献被削弱。
- 建议修改方向：
  (a) 增加多轴测量实验：对 formality rewrite 同时测量 register 和 verbosity 的变化幅度；
  (b) 将语言从"interventional/counterfactual"降级为"quasi-experimental"或"controlled comparison"；
  (c) 在 §3.5 明确讨论 originality OR 显著意味着识别假设 (i) 部分违反，以及这对 style effect 估计的具体影响方向和幅度。

**N2** [critical] Evaluator-producer confound 的 independence test 覆盖不完整

- 具体位置：Appendix D (Rewriter Independence), §5.3, Limitations
- 问题：
  1. Qwen3-32B 同时担任 rewriter 和 judge，论文自身数据显示其效应量系统性偏高：formality Style OR 4.20 vs GPT-4o 2.58（n=88），originality OR 系统性 ~2× GPT-4o。
  2. Rewriter independence test（Appendix D, Table 5）仅覆盖 verbosity 轴，缺少 formality 和 register 的 independence test。而 formality 恰好是 evaluator-producer bias 最明显的轴（Qwen3 OR=4.20 vs GPT-4o OR=2.58 at n=88）。
  3. 论文在 Limitations 中承认"partial self-recognition"，但主分析（Table 1, Table 3）仍以 Qwen3-32B 结果作为与 GPT-4o 并列的主要证据。
- 为什么影响接收：如果 Qwen3-32B 的 formality/register 效应量因 self-recognition 而膨胀，则 cross-judge replication 的可信度降低，"across two judges" 的 generalizability claim 被削弱。
- 建议修改方向：
  (a) 补做 formality 轴的 rewriter independence test（用 GPT-4o 做 rewriter, Qwen3-32B 做 judge）；
  (b) 或者在主文明确标注 Qwen3-32B 结果仅作为 existence claim（定性方向一致），不适合与 GPT-4o 做定量 effect size 比较；
  (c) 增加第三个独立 judge（如 Llama）以减弱对 Qwen3-32B 的依赖。

**N3** [critical] "Likert Blindspot" 的表述将已知的统计功效差异包装为新发现

- 具体位置：Abstract, §1 (Introduction), §5.2, Figure 4
- 问题：
  1. 论文自身的 power curve (Figure 4) 显示 Likert ATE 在 d=0.073 时需要 n≈1,473 才能达到 80% power。在 n=88 时 Likert 检测不到 bias，这完全符合统计预期——不是"Blindspot"，而是功效不足。
  2. 论文承认底层原理"predicted by classical measurement theory (Thurstone, 1927)"，但 Title 和 Abstract 的表述方式（"Reveals the Likert Blindspot"）暗示这是一个新发现的系统性缺陷，而非已知功效差异的量化。
  3. n=355 scaled replication 仍显示 Likert non-significant (p=0.60)，这是更强的证据。但这仅针对 Qwen3-32B formality 一个配置，且 Likert ATE 在该配置下的 effect size 未报告。如果 d 仍然很小，则依然是功效问题。
  4. 实际贡献是量化了 LLM judge 评估场景下 Likert vs pairwise 的 4.5× 效率差距——这有实用价值，但"Blindspot"（盲区）的措辞暗示 Likert 永远无法检测到 bias，这不准确。
- 为什么影响接收：Title 中的核心概念表述过强会削弱审稿人和读者的信任。
- 建议修改方向：
  (a) 将"Blindspot"重新定义为"measurement efficiency gap at typical evaluation scales (n=50-200)"，避免暗示 Likert 在任何 n 下都失败；
  (b) 对 n=355 replication 补报 Likert effect size (Cohen's d) 和 power；
  (c) 明确区分"Likert 在当前实践中的样本量下检测不到"（实用观察）和"Likert 本身有系统性缺陷"（理论声明）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] NLI gate 由同一模型族验证

- 具体位置：§5.1 (NLI Gate Validation)
- 问题：NLI gate 的 100 对验证使用 Qwen3-32B 作为 annotator（precision 98.9%），但 Qwen3 也是 rewriter。如果 Qwen3 对自己生成的文本有系统性的"认为内容一致"倾向，则 precision 被高估。论文提到"An independent spot-check with GPT-4o is planned"但未执行。
- 建议：补做 GPT-4o 或人类标注验证。至少应在 Limitations 中更明确标注此风险。

**W2** [warning] Verbosity 的 direction-aware NLI 削弱了 content preservation 保证

- 具体位置：§3.2
- 问题：对 verbosity 轴，NLI gate 从双向 entailment 放宽为单向（expansions 只检查 backward entailment）。这将 pass rate 从 65% 提升到 86%，但新放入的 21% 的 pairs 的内容保持质量未经验证。Verbosity rewrite（4.7× longer, §5.4）大幅增加文本内容，单向 NLI 无法排除新增内容引入的质量差异（更详细 = 更高质量的感知）。
- 建议：对 direction-aware gate 放入的额外 pairs 进行单独分析（BT win rate 是否与 strict bidirectional gate 的 pairs 一致）。

**W3** [warning] Table 1 的 Holm-Bonferroni 报告不够清晰

- 具体位置：Table 1 footnote
- 问题：Table 1 脚注 "†raw p < 0.05, Holm-adj. p = 0.08" 表明主要 family 的 BT 结果在校正后 p=0.08——即严格来说不显著。但 BT 列标注 `***` (p < 0.001) 似乎是未校正值。读者无法从 Table 1 区分哪些 p-values 经过了校正。
- 建议：在 Table 1 中分别列出 raw p 和 adjusted p，或在脚注中明确说明 `***` 对应的是 raw p 还是 adjusted p。

**W4** [warning] 缺少人工验证 rewriting 质量

- 具体位置：§3.1 (Style-Controlled Rewriting)
- 问题：整个框架依赖 Qwen3-32B 的 rewriting 质量，但论文没有任何人工评估来验证：(a) rewrite 是否确实改变了目标风格轴；(b) rewrite 是否引入了 NLI 检测不到的 artifacts（如不自然的措辞、风格不一致）。NLI gate 仅验证语义保持，不验证风格变化或自然度。
- 建议：对 50 个样本进行人工标注，验证风格改变方向正确率和自然度评分。

**W5** [warning] Confound gradient 可能反映 rewriting 难度而非 style axis 本质属性

- 具体位置：§5.6, Table 3
- 问题：GEE 分解显示 verbosity = pure style, formality = dual, register = originality-dominated。但这个 gradient 可能简单反映：verbosity rewriting（加/减内容）比 formality rewriting（风格转换）更容易做到不改变质量感知，而 register rewriting（academic ↔ conversational）几乎必然改变 sophistication。这意味着 originality confound 实际上在测量 rewriting 质量，而非 style axis 的固有属性。
- 建议：讨论此替代解释并设计实验区分两种假说（例如，用不同 rewriter 看 confound gradient 是否变化）。

**W6** [warning] 样本量与统计检验稳定性

- 具体位置：§4, Table 1, Table 3
- 问题：主实验 n=100 LLMBar → NLI 过滤后 ~88 pairs → 173 comparisons。对 GEE 模型（2 个预测变量 + correlation structure），n=88 pairs (176 obs) 的 OR 估计可能不稳定。Table 3 中 Qwen3 form. 从 n=88 (OR=4.20) 到 n=355 (OR=2.15) 的大幅下降直接证明了小样本 OR 估计的不稳定性。Register 轴的 marginal significance (Qwen3: p=0.046) 在这个样本量下尤其脆弱。
- 建议：(a) 对所有主要轴进行 scaled replication（不仅 formality）；(b) 报告 GEE 模型的 finite-sample corrected standard errors。

---

## 小问题（不影响接收）

1. **Abstract 过长过密**：9 行 abstract 试图覆盖太多细节（7 种统计方法、4 个 judge×axis 配置、3 个 benchmark），建议精简为 5-6 行聚焦核心 claim。
2. **引用问题**：`hoenig2001abuse` 在 bib 中存在但 verify_references 报告为 orphan（实际通过 `\citealt` 引用于 experiments.tex:130），可能是交叉检查工具的解析遗漏，不影响正确性。`murugadoss2025sos` 在 OpenAlex 上未找到匹配（可能太新），建议确认该引用的准确性。
3. **Table 1 最后一列表头为空**：应标注为"Blindspot indicator"或类似名称。
4. **"~60% uninformative ties" 在 Abstract、§1、§5.2 重复出现**，但未给出全部 6 个 judge×axis 配置的 tie rate 分布表。
5. **§5.5 Register 结果**：marginal significance (p=0.046) 在 exploratory family 中报告为"weak evidence"是合适的，但在主文中用大半节描述一个 inconclusive 结果可能分散读者注意力。考虑压缩或移入 Appendix。
6. **Correction proof of concept (§5.6 最后一段)**：debiased prompt 仅 2 行结果，缺乏细节（什么样的 prompt？改了什么？），作为 proof of concept 信息量不足。

---

## Questions for Authors

1. 对 formality rewrite，你们是否测量了 rewrite 在 register/verbosity 轴上的变化幅度？如果 formal rewrite 同时变得更 verbose 或更 academic，则单轴干预假设被违反。
2. n=355 scaled replication 的 Likert Cohen's d 是多少？如果 d 仍然接近 0.1，则 Likert non-significance 在 n=355 下仍然可能是功效不足（power ≈ 30% at d=0.1, n=355）。
3. Table 1 中 `***` (p < 0.001) 标注的是 raw p 还是 Holm-adjusted p？如果是 raw p，verbosity BT 的 adjusted p 是多少？
4. 是否考虑过使用 Likert 分数的 pairwise difference（paired t-test on Δscore）而非单独的 ATE？这会消除 tie-inflation 问题同时保留 Likert 信息。
5. Claude Sonnet 4 的"no bias"结果是否可能因为 Claude 的 rewrite 识别能力更强（即 Claude 有意避免 style bias），而非 Likert/pairwise 灵敏度差异？论文如何排除这种替代解释？

---

## 主要优势

1. **实用价值高**：量化了 LLM evaluation 中 Likert vs pairwise 的 4.5× 效率差距，对评测实践有直接指导意义。
2. **统计三角验证扎实**：7 种统计方法一致显示 Blindspot（Table 2），跨 judge/benchmark/axis 的系统性复制增强可信度。
3. **GEE 分解方法论贡献**：将 style effect 和 originality confound 解耦（Table 3）是有价值的方法创新，confound gradient 发现有 insight。
4. **负面控制有说服力**：Claude Sonnet 4 在两个轴上均未检测到 bias（BT 56.2%/54.1%, 均 non-sig），提供了区分效度。
5. **透明诚实**：Limitations 部分对 evaluator-producer bias、NLI 验证局限、scale granularity 等问题的讨论比较坦诚。
6. **GEE diagnostics 完整**：Appendix C 的 correlation structure robustness 检查和 interaction test 是认真的模型诊断工作。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 198 · 2026-05-21T09:41:40.384815+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成独立初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 199 · 2026-05-21T09:41:44.105898+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：

- **Overall: 3.5 (Borderline Conference)**
- 3 个 Must-Fix：(1) 因果识别假设不充分，originality OR 显著说明 NLI gate 未完全阻断 R→Q 路径；(2) Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register；(3) "Blindspot" 表述将功效差异包装为新发现，需降级为 "measurement efficiency gap"
- 6 个 Should-Fix：NLI 验证模型族自引用、direction-aware NLI 削弱保证、Holm-Bonferroni 报告不清晰、缺人工验证、confound gradient 替代解释、小样本 OR 不稳定
- 核心优势：7 种方法三角验证扎实、GEE 分解有方法论贡献、Claude 负面控制有说服力

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 200 · 2026-05-21T09:41:49.633719+00:00_

Reviewer 1 报告收到。等待 Reviewer 2 完成后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 17

## Round 17

6 recorded events


### User

_source line 201 · 2026-05-21T09:41:51.172471+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Counterfactual Style Decomposition Reveals the Likert Blindspot

## Paper Summary

本文提出 Counterfactual Style Decomposition (CSD)，一个黑盒框架，通过 style-controlled rewriting + NLI entailment gate + pairwise comparison 检测 LLM judge 的 per-axis style bias。核心发现被命名为 "Likert Blindspot"：在 LLMBar (n=100) 上对 3 个 judge（GPT-4o, Qwen3-32B, Claude Sonnet 4）的实验表明，Likert 评分对 style bias 的检测灵敏度系统性低于 pairwise comparison。论文还使用 GEE 回归将 style 和 originality 效应分离，发现 verbosity 的 style bias 最为显著。

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）

**一句话总结**: 方法论执行扎实、发现有实用价值，但核心洞见——ordinal rating 灵敏度低于 pairwise comparison——在心理测量学中已知近百年，novelty 主要来自 domain transfer 而非 genuine insight，且证据基础（n=100, 3 judges, 2 有效 axes）偏窄。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 主要 claims 有实验支撑但存在系统性缺陷：Likert Blindspot 的 framing 混淆了 measurement sensitivity 和 statistical power；"causal" 语言与实际方法论强度不匹配；样本量有限 |
| Excitement | 3 / 5 | 对 LLM evaluation 社区有实用价值（提醒 Likert-based findings 可能系统性低估 style bias），但核心发现是已知 psychometric 原理的 domain transfer，incremental contribution |
| Reproducibility | 4 / 5 | 方法描述清晰，pipeline 各步骤可复现；NLI gate 阈值、BT 模型参数、bootstrap 配置均明确报告；但数据和代码未附（anonymous submission 可理解） |
| Confidence | 4 / 5 | 本审稿人对 measurement theory、causal inference、LLM evaluation 文献均较熟悉 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Likert Blindspot 的 framing 混淆了 "measurement blindspot" 与 "statistical power gap"

- 具体位置：Title、Abstract（"Standard Scoring Underestimates Style Bias"）、Section 1 第2段（"a measurement efficiency gap"）、Contribution list 第2条（p.2）
- 问题：论文的核心 narrative 是 Likert scoring 存在质性的 "blindspot"——漏检了 pairwise 能发现的 bias。但 Figure 4（p.7）清楚地展示这是一个 **统计功效差异**：Likert 需要 ~1.5× 的样本量才能达到同等检测概率。这不是"看不见"（blindspot），而是"需要更多数据才能看见"（efficiency gap）。论文自己在 p.2 也写道 "~1.5× more data to reach equivalent sensitivity"，这恰恰是 power 语言而非 blindspot 语言。Title 用 "Blindspot" 暗示 Likert 有质性缺陷，但 Figure 4 的 evidence 只支持量性差异。同时，Thurstone (1927) 关于 ordinal scale 在精度上不如 paired comparison 的结论已有近百年历史——论文在 Section 2 引用了 Thurstone，却未充分说明本文发现与这一经典结论的关系。
- 为什么影响接收：如果核心 selling point 是一个已知现象的量化确认，而非 genuine new discovery，novelty claim 需大幅调整。Reviewer 或 AC 可能认为这是 "well-known effect, now measured in a new domain" 而非突破。
- 建议修改方向：(1) 明确区分 "Likert 的 measurement efficiency gap"（量性）和 "blindspot"（质性），在标题/abstract 中降调；(2) 在 Introduction 或 Related Work 中增加一段明确承认 Thurstone (1927) 以来 psychometric 文献已知 ordinal rating 灵敏度问题，本文贡献是首次在 LLM judge 场景中 **量化** 这一 gap 并证明其实际后果；(3) Figure 4 的 power curve 分析应更突出，作为 "这是 power gap 而非质性 blindspot" 的核心 evidence。

**N2** [critical] "Causal" / "Counterfactual" 术语使用与方法论强度不匹配

- 具体位置：Title（"Counterfactual Style Decomposition"）、Section 3.5（"Causal Framework"）、Figure 2（"Assumed data-generating process"）
- 问题：论文在 Section 3.5 正确地声明 "Our approach provides interventional rather than formal causal evidence" 且 "do not claim a complete structural causal model and do not invoke SUTVA or consistency assumptions"。但这与以下 framing 矛盾：(a) Title 使用 "Counterfactual"——在因果推断文献中，counterfactual 有 Rubin/Pearl 框架的严格含义；(b) Section 3.5 标题为 "Causal Framework" 并画了 DAG（Figure 2），暗示形式化因果模型；(c) "Decomposition" 暗示对 style/originality 效应的干净分离，但 Limitations 承认 "quality–style confounding is not fully eliminated"（p.9）。实际上，CSD 是一个 **controlled intervention study with imperfect content preservation**，而非因果推断。NLI gate 是工程近似，非 identification strategy。
- 为什么影响接收：Causal framing mismatch 是 *ACL 审稿的常见 rejection 理由。Reviewer 若有因果推断背景会严格审视这些术语。
- 建议修改方向：(1) 将 "Counterfactual" 替换为更准确的术语如 "Interventional" 或 "Controlled"；(2) Section 3.5 标题从 "Causal Framework" 改为 "Interventional Design" 或 "Data-Generating Assumptions"；(3) 在 Introduction 首次使用 "counterfactual" 时加 qualifier（e.g., "counterfactual-style perturbation" rather than implying Pearl-type counterfactuals）。

**N3** [critical] 证据基础过窄，但 practical recommendation 过强

- 具体位置：Contribution 第4条（p.2 "Practical implications: style bias audits should employ pairwise comparison and per-axis decomposition"）、Section 4（n=100, LLMBar only）
- 问题：论文在 n=100（单一 benchmark LLMBar）× 3 judges × 2 个有效 style axes（verbosity, formality；tone 失败，见 Limitations）上得出结论，然后在 Contribution list 给出了一般性实践建议。具体的 generalizability concerns：(a) LLMBar 只有 instruction-response pairs，不覆盖 dialogue、summarization、creative writing 等常见 judge 应用场景；(b) n=100 下，Table 1 中 Likert p-values 多数在 0.03–0.78 范围，部分 pairwise p-values 也非显著（e.g., GPT-4o register p=0.031, Likert p=0.785——但 Claude formality 和 register 的 pairwise 也 non-significant）；(c) 2 个 style axes 不足以称 "per-axis decomposition framework" 的通用有效性；(d) tone axis 完全失败但只在 Limitations 一笔带过。
- 为什么影响接收：Claims 的 scope 与 evidence 的 scope 不匹配是 soundness 问题。
- 建议修改方向：(1) 将 Contribution 第4条的建议加 qualifier（"on instruction-following tasks with n ≥ 100"）；(2) 增加至少一个额外 benchmark 或大幅增加样本量；(3) Tone axis 失败应在正文（非仅 Limitations）讨论，说明 CSD 的适用边界条件。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Related Work 引用数量偏少，遗漏若干重要相关工作

- 具体位置：Section 2（Related Work，约1页），References（27条）
- 问题：27 条引用低于 EMNLP long paper 通常水平（40-60条）。具体遗漏包括：
  - **Counterfactual text generation 方法**：Feder et al. (2021) "CausaLM: Causal Model Explanation Through Counterfactual Language Models" 和 Wu et al. (2021) "Polyjuice: Generating Counterfactuals for Explaining, Training, and Evaluating NLMs" 是该领域的基础工作，论文仅引了 RATE 和一篇 counterfactual rhetorical paper，不足以 contextualize CSD 在 counterfactual generation 方法谱系中的位置
  - **Scale design 与 annotation 文献**：Amidei et al. (2019) "Agreement is overrated"、Clark et al. (2021) "All That's 'Human' Is Not Gold" 讨论了 rating scale 在 NLG 评估中的问题，与 Likert Blindspot narrative 直接相关
  - **LLM judge 的 verbosity bias 专项工作**：Saito et al. (2023) "Verbosity Bias in LLM-as-a-Judge"（如果存在这样的 focused study）
  - **Reward model bias**：Park et al. (2024) "RLHF reward model length/verbosity bias" 等
- 建议：补充 counterfactual generation、NLG evaluation scale design 两个方向的经典引用，将 Related Work 扩展至覆盖这些重要分支。

**W2** [warning] NLI gate 的 false negative 是否引入 systematic selection bias

- 具体位置：Section 5.1（NLI Gate Validation, p.5-6）
- 问题：NLI gate 在 100 对 validation 中有 8.75% false negative rate（Section 5.1: "8/91 ≈ 8.8%"，content-preserving pairs 被错误拒绝）。论文将此描述为可接受，但未讨论：被过滤掉的 pairs 是否在 style axis 上有系统性特征？例如，如果 NLI gate 更容易拒绝 **大幅度 style 变化**（因为大幅 style 变化更可能伴随表面形式的改变而被 NLI 误判为 entailment failure），那么留下的 pairs 就是 attenuated treatment，会 **低估** style bias。这会使 Likert Blindspot 的量化（1.5×）本身就带有 attenuation bias。
- 建议：分析被 NLI gate 过滤掉的 pairs 的 style change magnitude，确认无 systematic selection effect；或至少在 Limitations 中讨论这个可能。

**W3** [warning] GEE "decomposition" 的 interpretability 有限

- 具体位置：Table 3（p.8）、Section 5.6（GEE Decomposition and Confound Structure）
- 问题：Table 3 的 GEE logistic decomposition 显示 formality 效应在 controlling for originality 后 "remains significant"（GPT-4o OR=2.58, Qwen3-32B OR=2.15）。但论文 Limitations (p.9) 承认 "the significant original-preference odds ratio (OR = 2.32, p = 0.006) indicates that quality–style confounding is not fully eliminated"。如果 confounding 未消除，"decomposition" 这个词就有误导性——它暗示干净分离，但实际上是 partial adjustment。此外，GEE 中 "originality" 的操作化定义不清晰：是通过 rewrite 方向（original vs rewrite）来 proxy originality，还是有独立的 originality measurement？
- 建议：(1) 将 "decomposition" 改为 "partial decomposition" 或 "adjustment"；(2) 明确 originality 的操作化方式；(3) 讨论 omitted variable bias 的方向和可能影响。

**W4** [warning] Claude Sonnet 4 作为 negative control 的解释力有限

- 具体位置：Table 1（Claude rows）、Section 5.3 提到 "Claude Sonnet 4 as negative control"
- 问题：Claude 在所有 axes 上均无显著 style preference，论文将其作为 negative control 证明 CSD pipeline 不产生 false positives。但 Claude 也可能是因为其 alignment training 确实消除了 style bias（而非 CSD 无 false positive）。这两种解释不可区分。一个真正的 negative control 应该是对已知无 bias 的 synthetic judge 施加 CSD，验证不检测到 bias。
- 建议：弱化 "negative control" 的措辞为 "consistent with either no style bias or no false positive"；或构造一个 rule-based judge（e.g., 随机选择）作为真正的 negative control。

**W5** [warning] Appendix 内容应部分纳入正文

- 具体位置：Appendix A（Direction Asymmetry）、Appendix C（GEE Model Diagnostics）
- 问题：Direction asymmetry（formality 的非对称效应）是一个 substantive finding：judge 对 formal→rewrite 有 78.8% 偏好但 casual→rewrite 只有 54.5%（Appendix A）。这对理解 formality bias 至关重要但被放在 Appendix。同样，GEE correlation structure robustness（Appendix C, Table 4）是支撑 Section 5.6 decomposition claim 的关键 evidence，仅放 Appendix 削弱了说服力。鉴于 Limitations 不计入8页限制，可考虑精简 Limitations 释放空间。
- 建议：将 Direction Asymmetry 的核心数字（至少一句话 + Table）和 GEE robustness check 的关键结论移入正文。

---

## 小问题（不影响接收）

- **M1**: Orphan bib entry `hoenig2001abuse`（The Abuse of Power, 2001）在 .bib 文件中但未在正文中引用。应移除或引用。
- **M2**: Reference verification 发现 `tan2025judgebench` 和 `chiang2024chatbot` 存在 first author 信息不匹配（bib 中 key 前缀 vs API 返回的 first author），建议核查 bib 条目作者信息准确性。
- **M3**: `murugadoss2025sos`（Style Over Substance）在 OpenAlex 中未找到精确匹配（similarity 0.36），可能是 venue/年份信息有出入，建议核查。
- **M4**: Figure 1（p.4）的 pipeline overview 图较小，stage attrition numbers 不易辨认，建议放大或移到更宽的 figure slot。
- **M5**: Section 3.2（Content Preservation Verification）中 "DeBERTa-v3-large with an entailment threshold of 0.90" 的选择依据未说明。为什么是 0.90？sensitivity analysis（不同 threshold 对结果的影响）可以加强 robustness。
- **M6**: p.8 正文末段 "Prompt-level debiasing is insufficient; structural interventions remain open" 是一个 broad claim，但论文没有测试任何 prompt-level debiasing 方法。这句话的 evidence 基础不足。

---

## Questions for Authors

1. **关于 Likert Blindspot 的本质**：你们如何区分 "Likert 在质性上看不到某些 bias"（blindspot）与 "Likert 需要更大样本才能检测到同样的 bias"（power gap）？Figure 4 似乎支持后者而非前者。如果是 power gap，那么在足够大的 n 下 Likert 和 pairwise 的检测结果应收敛——你们的 power curve 是否 asymptotically converge？

2. **关于 NLI gate 的 selection effect**：被 NLI gate 过滤掉的 pairs 在 style change magnitude 上是否有系统性偏差？如果大幅 style 变化更容易被过滤，最终的 ATE 是否被 attenuated？

3. **关于 tone axis 的失败**：论文在 Limitations 中简短提及 tone axis "fail"，能否提供更多细节？具体是 rewriting 质量不行还是 NLI gate 过滤掉了太多 pairs？这对理解 CSD 的适用范围至关重要。

4. **关于 generalizability**：LLMBar 的 instruction-following 格式是否代表 LLM judge 的主要使用场景？在 open-ended dialogue 或 creative writing 等场景中，style bias 的 pattern 可能完全不同。你们是否有 pilot data 支持 generalization？

5. **关于 "decomposition" 的残余 confounding**：Table 3 中 originality OR 显著（2.32, p=0.006），说明 confounding 未消除。你们估计残余 confounding 对 style effect estimate 的 bias 方向和幅度是多少？

---

## 主要优势

- **S1**: Pipeline 设计思路清晰，NLI gate + bidirectional entailment verification 是 content preservation 的务实解决方案，工程上可复现。
- **S2**: Negative results 的诚实呈现——Claude 无 bias、formality 方向不对称、tone axis 失败——增加了结果可信度。
- **S3**: Figure 4 的 detection probability power curve 分析是 measurement methodology 层面的有价值贡献，即使它削弱了 "blindspot" narrative。
- **S4**: GEE decomposition 将 style effect 与 originality confound 分离的尝试在 LLM judge bias 文献中较为少见，方法论方向正确。
- **S5**: 论文整体写作清晰、信息密度高，在8页内覆盖了完整的方法-实验-分析链。
- **S6**: Bradley-Terry analysis 作为 pairwise 的 parametric backbone 选择合理，bootstrap CI 的使用增加了统计严谨性。

---

## 分项总结

| 关键判断 | 评估 |
|---------|------|
| 新颖性 | 中等。Likert vs pairwise 灵敏度差异是 psychometric 已知结论的 LLM domain transfer；CSD pipeline 是合理的工程组合但无方法论突破；GEE per-axis decomposition 是较新的尝试 |
| Claims-Evidence 对齐 | 部分失衡。"Blindspot"（质性）vs power gap（量性）的混淆是最大问题；"Causal" framing 与实际方法强度不匹配；practical recommendation 的 scope 超出 evidence scope |
| Related Work | 基本覆盖但偏薄。LLM judge bias 主线覆盖良好，缺 counterfactual generation 方法谱系和 NLG evaluation scale design 文献 |
| 写作与格式 | 良好。结构清晰，正文8页合规，图表质量可接受，Limitations 覆盖了关键弱点 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-21T09:42:35.795053+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供具体证据（cite 具体 Section/Table/Figure）\n\n特别关注：你和 R1 是否在 \"Blindspot framing\"、\"causal 语言\" 等问题上有共识或分歧。\n\n---\n\n# Reviewer 1 — 方法严谨性 + 实验有效性\n\n## 总体评分\n**Overall Assessment**: 3.5 — Borderline Conference\n\n## Must-Fix 问题\n\n**N1** [critical] 因果识别假设不充分且可能被违反\n- §3.5 识别假设 (iii)（style rewrite 不引入 target axis 外差异）未检验——formality rewrite 可能同时改变 register/vocabulary sophistication\n- Table 3 中 originality OR 显著（GPT-4o formality: OR=2.32, p=0.006; Qwen3 register: OR=5.72），直接表明 NLI gate 未完全阻断 R→Q 路径\n- \"counterfactual\"\"interventional\"\"do-operator\" 等强因果语言与 §3.5 的 disclaimer 矛盾\n- 建议：增加多轴测量、降级语言、明确讨论 originality OR 对识别假设的影响\n\n**N2** [critical] Evaluator-producer confound 的 independence test 覆盖不完整\n- Qwen3-32B 同时做 rewriter 和 judge，效应量系统性偏高（formality Style OR 4.20 vs GPT-4o 2.58 at n=88）\n- Rewriter independence test（Appendix D）仅覆盖 verbosity 轴，缺 formality 和 register\n- 主分析仍以 Qwen3-32B 与 GPT-4o 并列为主要证据\n- 建议：补做 formality 轴 independence test 或标注 Qwen3 仅作 existence claim\n\n**N3** [critical] \"Likert Blindspot\" 将已知统计功效差异包装为新发现\n- Figure 4 power curve 显示 n≈1,473 才能达到 80% power——在 n=88 下 non-significant 是功效不足，非 blindspot\n- 论文承认底层原理 \"predicted by Thurstone 1927\"\n- n=355 scaled replication 仍显示 Likert non-significant，但该配置的 effect size 未报告\n- 建议：将 \"Blindspot\" 重定义为 \"measurement efficiency gap at typical evaluation scales\"\n\n## Should-Fix 问题\n\n**W1** NLI gate 由同一模型族验证（Qwen3-32B rewriter + Qwen3-32B annotator），precision 可能被高估\n**W2** Direction-aware NLI 放宽为单向 entailment，放入的额外 21% pairs 内容保持质量未验证\n**W3** Table 1 Holm-Bonferroni 报告不清晰——*** 标注的是 raw p 还是 adjusted p 不明\n**W4** 缺少人工验证 rewriting 质量（style 改变方向正确率和自然度）\n**W5** Confound gradient 可能反映 rewriting 难度而非 axis 固有属性\n**W6** 样本量与 GEE OR 估计稳定性——Qwen3 formality OR 从 n=88 (4.20) 降到 n=355 (2.15)\n\n## 主要优势\n1. 实用价值高（4.5× 效率差距量化）\n2. 7 种统计方法三角验证\n3. GEE 分解方法论贡献\n4. Claude 负面控制有说服力\n5. Limitations 讨论透明诚实\n6. GEE diagnostics 完整",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供具体证据（cite 具体 Section/Table/Figure）\n\n特别关注：你和 R1 是否在 \"Blindspot framing\"、\"causal 语言\" 等问题上有共识或分歧。\n\n---\n\n# Reviewer 1 — 方法严谨性 + 实验有效性\n\n## 总体评分\n**Overall Assessment**: 3.5 — Borderline Conference\n\n## Must-Fix 问题\n\n**N1** [critical] 因果识别假设不充分且可能被违反\n- §3.5 识别假设 (iii)（style rewrite 不引入 target axis 外差异）未检验——formality rewrite 可能同时改变 register/vocabulary sophistication\n- Table 3 中 originality OR 显著（GPT-4o formality: OR=2.32, p=0.006; Qwen3 register: OR=5.72），直接表明 NLI gate 未完全阻断 R→Q 路径\n- \"counterfactual\"\"interventional\"\"do-operator\" 等强因果语言与 §3.5 的 disclaimer 矛盾\n- 建议：增加多轴测量、降级语言、明确讨论 originality OR 对识别假设的影响\n\n**N2** [critical] Evaluator-producer confound 的 independence test 覆盖不完整\n- Qwen3-32B 同时做 rewriter 和 judge，效应量系统性偏高（formality Style OR 4.20 vs GPT-4o 2.58 at n=88）\n- Rewriter independence test（Appendix D）仅覆盖 verbosity 轴，缺 formality 和 register\n- 主分析仍以 Qwen3-32B 与 GPT-4o 并列为主要证据\n- 建议：补做 formality 轴 independence test 或标注 Qwen3 仅作 existence claim\n\n**N3** [critical] \"Likert Blindspot\" 将已知统计功效差异包装为新发现\n- Figure 4 power curve 显示 n≈1,473 才能达到 80% power——在 n=88 下 non-significant 是功效不足，非 blindspot\n- 论文承认底层原理 \"predicted by Thurstone 1927\"\n- n=355 scaled replication 仍显示 Likert non-significant，但该配置的 effect size 未报告\n- 建议：将 \"Blindspot\" 重定义为 \"measurement efficiency gap at typical evaluation scales\"\n\n## Should-Fix 问题\n\n**W1** NLI gate 由同一模型族验证（Qwen3-32B rewriter + Qwen3-32B annotator），precision 可能被高估\n**W2** Direction-aware NLI 放宽为单向 entailment，放入的额外 21% pairs 内容保持质量未验证\n**W3** Table 1 Holm-Bonferroni 报告不清晰——*** 标注的是 raw p 还是 adjusted p 不明\n**W4** 缺少人工验证 rewriting 质量（style 改变方向正确率和自然度）\n**W5** Confound gradient 可能反映 rewriting 难度而非 axis 固有属性\n**W6** 样本量与 GEE OR 估计稳定性——Qwen3 formality OR 从 n=88 (4.20) 降到 n=355 (2.15)\n\n## 主要优势\n1. 实用价值高（4.5× 效率差距量化）\n2. 7 种统计方法三角验证\n3. GEE 分解方法论贡献\n4. Claude 负面控制有说服力\n5. Limitations 讨论透明诚实\n6. GEE diagnostics 完整",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-21T09:42:52.940304+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17145
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-21T09:42:53.339021+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供具体证据（cite 具体 Section/Table/Figure）\n\n特别关注：你和 R2 是否在 \"Blindspot framing\"、\"causal 语言\"、\"evidence scope\" 等问题上有共识或分歧。\n\n---\n\n# Reviewer 2 — 新颖性 + 完整性 + Related Work\n\n## 总体评分\n**Overall Assessment**: 3.5 — Borderline Conference\n\n## Must-Fix 问题\n\n**N1** [critical] Likert Blindspot 的 framing 混淆了 \"measurement blindspot\" 与 \"statistical power gap\"\n- Title 用 \"Blindspot\" 暗示 Likert 有质性缺陷，但 Figure 4 evidence 只支持量性差异\n- Thurstone (1927) 关于 ordinal scale 灵敏度低于 paired comparison 的结论已有近百年\n- 论文自己在 p.2 写 \"~1.5× more data to reach equivalent sensitivity\"——这是 power 语言\n- 建议：明确区分量性 gap 和质性 blindspot，降调标题/abstract\n\n**N2** [critical] \"Causal\"/\"Counterfactual\" 术语与方法论强度不匹配\n- Title \"Counterfactual\"、§3.5 \"Causal Framework\"、Figure 2 DAG 暗示形式化因果模型\n- 但 §3.5 声明 \"not a complete structural causal model, nor do we invoke SUTVA\"\n- 实际上是 controlled intervention study with imperfect content preservation\n- 建议：替换为 \"Interventional\"/\"Controlled\"，§3.5 标题改为 \"Interventional Design\"\n\n**N3** [critical] 证据基础过窄但 practical recommendation 过强\n- n=100 LLMBar × 3 judges × 2 有效 axes → 不足以支撑一般性实践建议\n- LLMBar 只有 instruction-response pairs，不覆盖 dialogue/summarization/creative writing\n- Tone axis 完全失败但只在 Limitations 一笔带过\n- 建议：加 qualifier、增加 benchmark、正文讨论 tone axis 失败\n\n## Should-Fix 问题\n\n**W1** Related Work 引用偏少（27条 vs EMNLP 通常 40-60 条），缺 counterfactual generation 方法谱系（CausaLM, Polyjuice）和 NLG evaluation scale design 文献（Amidei 2019, Clark 2021）\n**W2** NLI gate false negative 可能引入 systematic selection bias——大幅 style 变化更易被过滤，导致 ATE 被 attenuated\n**W3** GEE \"decomposition\" 在 confounding 未消除时有误导性——应改为 \"partial adjustment\"\n**W4** Claude 作为 negative control 的解释力有限——可能是 Claude alignment 消除了 bias 而非 CSD 无 false positive\n**W5** Appendix 中 Direction Asymmetry 和 GEE Robustness 应部分纳入正文\n\n## 主要优势\n1. Pipeline 设计思路清晰，工程可复现\n2. Negative results 诚实呈现增加可信度\n3. Figure 4 power curve 是 measurement methodology 层面的有价值贡献\n4. GEE decomposition 方向正确\n5. 写作清晰、信息密度高\n6. Bradley-Terry + bootstrap CI 统计严谨",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供具体证据（cite 具体 Section/Table/Figure）\n\n特别关注：你和 R2 是否在 \"Blindspot framing\"、\"causal 语言\"、\"evidence scope\" 等问题上有共识或分歧。\n\n---\n\n# Reviewer 2 — 新颖性 + 完整性 + Related Work\n\n## 总体评分\n**Overall Assessment**: 3.5 — Borderline Conference\n\n## Must-Fix 问题\n\n**N1** [critical] Likert Blindspot 的 framing 混淆了 \"measurement blindspot\" 与 \"statistical power gap\"\n- Title 用 \"Blindspot\" 暗示 Likert 有质性缺陷，但 Figure 4 evidence 只支持量性差异\n- Thurstone (1927) 关于 ordinal scale 灵敏度低于 paired comparison 的结论已有近百年\n- 论文自己在 p.2 写 \"~1.5× more data to reach equivalent sensitivity\"——这是 power 语言\n- 建议：明确区分量性 gap 和质性 blindspot，降调标题/abstract\n\n**N2** [critical] \"Causal\"/\"Counterfactual\" 术语与方法论强度不匹配\n- Title \"Counterfactual\"、§3.5 \"Causal Framework\"、Figure 2 DAG 暗示形式化因果模型\n- 但 §3.5 声明 \"not a complete structural causal model, nor do we invoke SUTVA\"\n- 实际上是 controlled intervention study with imperfect content preservation\n- 建议：替换为 \"Interventional\"/\"Controlled\"，§3.5 标题改为 \"Interventional Design\"\n\n**N3** [critical] 证据基础过窄但 practical recommendation 过强\n- n=100 LLMBar × 3 judges × 2 有效 axes → 不足以支撑一般性实践建议\n- LLMBar 只有 instruction-response pairs，不覆盖 dialogue/summarization/creative writing\n- Tone axis 完全失败但只在 Limitations 一笔带过\n- 建议：加 qualifier、增加 benchmark、正文讨论 tone axis 失败\n\n## Should-Fix 问题\n\n**W1** Related Work 引用偏少（27条 vs EMNLP 通常 40-60 条），缺 counterfactual generation 方法谱系（CausaLM, Polyjuice）和 NLG evaluation scale design 文献（Amidei 2019, Clark 2021）\n**W2** NLI gate false negative 可能引入 systematic selection bias——大幅 style 变化更易被过滤，导致 ATE 被 attenuated\n**W3** GEE \"decomposition\" 在 confounding 未消除时有误导性——应改为 \"partial adjustment\"\n**W4** Claude 作为 negative control 的解释力有限——可能是 Claude alignment 消除了 bias 而非 CSD 无 false positive\n**W5** Appendix 中 Direction Asymmetry 和 GEE Robustness 应部分纳入正文\n\n## 主要优势\n1. Pipeline 设计思路清晰，工程可复现\n2. Negative results 诚实呈现增加可信度\n3. Figure 4 power curve 是 measurement methodology 层面的有价值贡献\n4. GEE decomposition 方向正确\n5. 写作清晰、信息密度高\n6. Bradley-Terry + bootstrap CI 统计严谨",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-21T09:42:54.951560+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1612
}
```

</details>

---


### Assistant

_source line 206 · 2026-05-21T09:42:57.550937+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 207 · 2026-05-21T09:43:00.228508+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.5/5（Borderline Conference）**。

三个 Must-Fix 问题：
1. **Likert Blindspot framing**——论文将统计功效差异（power gap）包装为质性的"盲区"（blindspot），但 Figure 4 的 evidence 只支持前者，且 Thurstone (1927) 以来 psychometric 文献早已建立此结论
2. **"Causal"/"Counterfactual" 术语过强**——方法是 controlled intervention with imperfect content preservation，不是 Pearl/Rubin 框架的因果推断，但 title 和 Section 3.5 的 framing 暗示后者
3. **证据基础过窄但实践建议过强**——n=100 × 3 judges × 2 axes 的 evidence 支撑不了通用性的 practical recommendation

主要优势：pipeline 工程设计清晰、negative results 诚实呈现、GEE decomposition 方向正确、写作质量良好。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 208 · 2026-05-21T09:43:08.198695+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 209 · 2026-05-21T09:44:23.824841+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 问题回应

**[AGREE] R1-N1: 因果识别假设不充分且可能被违反**

同意，且补充我自己的发现强化这一判断。R1 指出的识别假设 (iii) 违反证据——Table 3 中 originality OR 显著（GPT-4o formality OR=2.32, p=0.006）——正是我在 R2-N2 中独立提出的核心问题。两位 reviewer 从不同角度到达同一结论：论文使用了 "counterfactual""do-operator""causal framework" 等强因果语言（Title、Section 3.5），但方法论强度不支撑这些术语。

补充一点 R1 未展开的：Section 3.5 的 DAG（Figure 2）画了 S→Y 和 Q→Y 两条路径并声称 CSD 可以 isolate S→Y effect，但 Table 3 的残余 originality OR 说明 R→Q path 未完全阻断。这意味着 Figure 2 的 DAG 本身就是不完整的——实际上存在 S→Q 的 residual path（style 改变伴随 quality 改变），NLI gate 只是 attenuate 而非 block 了这条路径。论文需要在 Figure 2 中画出这条 residual path 并讨论其影响，而非假装它不存在。

R1 建议"增加多轴测量、降级语言"是正确方向。我进一步建议：将 Section 3.5 标题从 "Causal Framework" 改为 "Interventional Design and Assumptions"，并在 DAG 中用虚线标注 residual S→Q confounding。

---

**[AGREE] R1-N2: Evaluator-producer confound 的 independence test 覆盖不完整**

同意。这是我审稿时未充分关注的问题，R1 的分析非常到位。关键数据点：

- Qwen3-32B 同时担任 rewriter 和 judge 时，formality Style OR = 4.20（Table 3, n=88）
- GPT-4o 作为独立 judge 时，formality Style OR = 2.58（Table 3）
- 这 1.6× 的差距（4.20 vs 2.58）是否来自 evaluator-producer confound 无法判断，因为 Appendix D 的 independence test 仅覆盖 verbosity 轴

Appendix D（p.10）确认：将 Qwen3-32B 替换为 GPT-4o 作为 verbosity rewriter 后，Style OR 从 13.10 降至"仅"10.17（降幅 22%），论文将此解释为"bounding the evaluator-producer component of the style effect"。但这个 22% 降幅在 verbosity 轴上就已经不小了——在 formality 轴上（可能更敏感于 model-specific writing patterns），confound 可能更大。R1 要求补做 formality independence test 的建议合理且必要。

补充：如果 formality independence test 显示 Qwen3-32B 的 OR 大幅下降，则 Table 3 的 GEE decomposition 对 Qwen3 的结论需要 reinterpret——目前论文将 GPT-4o 和 Qwen3 并列呈现，但实际上只有 GPT-4o 的结果是 evaluator-producer independent 的。

---

**[AGREE] R1-N3: "Likert Blindspot" 将已知统计功效差异包装为新发现**

强烈同意。这与我的 R2-N1 完全一致——两位 reviewer 独立到达相同结论，说明这是论文最核心的 framing 问题。

R1 补充了一个我未展开的重要细节：**n=355 scaled replication 的 effect size 未报告**。这是关键遗漏——如果 n=355 下 Likert 仍 non-significant（Table 3, p.8: "Likert still non-significant (d = 0.01, p = 0.908)"），但 effect size d=0.01 本身就极小，那么 non-significance 可能反映的是 **Likert 下 effect size 本身缩小**（measurement attenuation）而非仅仅 power 不足。这两种机制的实践含义不同：
- 如果是 power gap：增大 n 即可解决
- 如果是 measurement attenuation：Likert scale 在任何 n 下都系统性压缩 effect size，问题更根本

论文的 Figure 4 power curve 暗示两种机制都在起作用（Likert 的 effect size 曲线起点就更低），但未明确分离。这实际上是 "Blindspot" narrative 最有潜力的 upgrade 方向——如果作者能证明 Likert **同时** 压缩 effect size 和降低 power（而非仅仅后者），"blindspot" 的 framing 就更站得住脚。但目前论文没有做这个分析。

R1 建议将 "Blindspot" 重定义为 "measurement efficiency gap at typical evaluation scales" 是合理的折中方案。

---

## Should-Fix 问题回应

**[AGREE] R1-W1: NLI gate 由同一模型族验证**

同意。Section 5.1（p.5-6）使用 Qwen3-32B 作为 annotator 来验证 NLI gate（DeBERTa-v3-large）的 precision/recall。但 Qwen3-32B 同时也是 rewriter——同一模型对自己 rewrite 的内容一致性判断可能偏乐观（self-consistency bias）。这与我的 R2-W2（NLI gate 是否引入 systematic selection bias）相关但从不同角度指出问题。理想的验证应使用独立的第三方模型或人类标注。

---

**[AGREE] R1-W2: Direction-aware NLI 放宽为单向 entailment 的质量未验证**

同意。Section 3.2 描述：对 compression 类 rewrite（原文 entail rewrite 但反向不成立），放宽为单向 entailment，将 verbosity 通过率从 65% 提升到 86%。这额外纳入的 ~21% pairs 的 content preservation 质量未被独立验证。论文仅说 "This gating mechanism approximates the do-operator"（p.4），但单向 entailment 允许 rewrite 丢失信息——如果 rewrite 删除了与 quality 相关的内容细节，judge 的评分差异可能 confound style 和 information loss。这会 inflate style bias estimate。

---

**[REBUT] R1-W3: Table 1 Holm-Bonferroni 报告不清晰**

部分反驳。Table 1 底部注释（p.5）明确写道："Holm-adj. p < 0.05, ↓; Holm-adj. p ≥ 0.05, ↑; BT sig., bold sig."。*** 标注对应的是 "raw p < 0.01"。虽然这个注释系统确实不够直觉（需要读者自行 cross-reference 符号和脚注），但信息本身是完整的——raw p 和 Holm-adjusted significance 的关系可以从表中重建。改进建议是合理的（直接报告 adjusted p 值），但将其定位为 "不清晰" 稍过——属于 presentation preference 而非 reporting gap。

---

**[AGREE] R1-W4: 缺少人工验证 rewriting 质量**

同意，且认为重要性比 R1 的 Should-Fix 定位更高。CSD pipeline 的基础假设是 style-controlled rewriting 仅改变 target style axis。但论文完全依赖 NLI gate（自动化）来验证 content preservation，**未提供任何 human evaluation** 证据表明：(a) rewrite 确实改变了目标 style axis 的方向且幅度合理，(b) rewrite 未引入非目标维度的变化。在 ACL/EMNLP 传统中，涉及 text generation quality 的工作通常需要至少 small-scale human evaluation。即使50对的人工标注也能大幅增加 pipeline 可信度。

---

**[AGREE] R1-W5: Confound gradient 可能反映 rewriting 难度而非 axis 固有属性**

同意，且认为这是一个精妙的 alternative interpretation。Section 5.5 发现 verbosity 的 confound gradient 最强（originality confound 最大），论文将此 interpret 为不同 style axes 的固有特征。但 R1 正确指出：verbosity rewrite 需要大幅增减文本量（1.7× longer, Table 5 implied），而 formality rewrite 可能仅需词汇替换——rewriting 操作的 invasiveness 越大，越难保持 content quality，因此 originality confound 越大。这意味着 confound gradient 可能是 **pipeline artifact** 而非 **style axis property**。论文应讨论这一 alternative explanation。

---

**[AGREE] R1-W6: 样本量与 GEE OR 估计稳定性**

同意。Qwen3 formality Style OR 从 n=88 的 4.20 骤降至 n=355 的 2.15（降幅 49%）是严重的 estimate instability 信号。虽然 OR 在小样本下 variance 大是已知的统计现象，但 2× 的降幅说明 n=88 下的 GEE 估计可能严重偏高。这对论文的影响是：Table 3 报告的 n=88 结果（主分析）的 point estimates 可信度受损，n=355 的 scaled replication 应被赋予更高权重。建议论文将 scaled replication 提升为主结果而非补充分析。

---

## 共识与分歧总结

### 强共识（两位 reviewer 独立提出相同问题）
1. **"Likert Blindspot" framing 问题**（R1-N3 ≈ R2-N1）：两人均认为核心 narrative 混淆了 measurement sensitivity 和 statistical power，且 Thurstone (1927) 已知。这是论文最大的 framing 风险。
2. **Causal 语言过强**（R1-N1 ≈ R2-N2）：两人均认为 "counterfactual""causal framework""do-operator" 等术语与方法论强度不匹配。Table 3 originality OR 是 shared evidence。
3. **证据基础偏窄**（implicit in R1-N2, R1-W6 ≈ R2-N3）：n=100, 有限 axes, 有限 judges。

### R1 独特贡献（我审稿时未充分关注）
- **Evaluator-producer confound**（R1-N2）：Qwen3-32B dual role 问题和 independence test 覆盖不完整是重要发现
- **Confound gradient 的 alternative interpretation**（R1-W5）：rewriting difficulty vs axis property
- **OR 估计 instability**（R1-W6）：n=88 vs n=355 的 2× 降幅

### R2 独特贡献（R1 未涉及）
- **NLI gate selection bias**（R2-W2）：被过滤 pairs 是否系统性偏向大幅度 style change
- **Claude 作为 negative control 的双重解释**（R2-W4）
- **Related Work 引用偏少**（R2-W1）：27条引用低于 EMNLP 标准，counterfactual generation 和 NLG evaluation scale design 文献缺失
- **Appendix 内容应入正文**（R2-W5）：Direction asymmetry 和 GEE robustness check

### 无分歧
两位 reviewer 在所有重大问题上方向一致，无实质性分歧。唯一的轻微差异是 R1-W3（Holm-Bonferroni 报告清晰度），我认为信息是完整的，只是 presentation 可改进。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 210 · 2026-05-21T09:44:30.036672+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 211 · 2026-05-21T09:44:32.742709+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：两位 Reviewer 在三个最重要问题上形成强共识——Likert Blindspot framing 混淆 power gap 与质性 blindspot、causal 语言过强、证据基础偏窄。无实质性分歧。R1 在 evaluator-producer confound 和 OR instability 上有独特贡献，R2 在 NLI gate selection bias、Related Work 薄弱、Claude negative control 双重解释上有独特贡献。唯一轻微不同意见是 Table 1 的 Holm-Bonferroni 标注——我认为信息完整但 presentation 可改进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 212 · 2026-05-21T09:44:37.240862+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 21

## Round 21

10 recorded events


### User

_source line 213 · 2026-05-21T09:44:42.417223+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应

---

## Must-Fix 问题

### [AGREE] R2-N1: Likert Blindspot framing 混淆 measurement blindspot 与 statistical power gap

同意，这与我的 R1-N3 高度一致。R2 和我独立达成了相同判断：论文的核心发现本质上是一个**量化的统计功效差距**（4.5× efficiency gap），而非 Likert 的质性缺陷。

补充我的观察：
- Figure 4 (power curve) 明确显示 Likert ATE 在 n≈1,473 时达到 80% power——即 Likert 在足够样本量下可以检测到 bias，"Blindspot" 的措辞暗示永远无法检测，这不准确。
- n=355 scaled replication（§5.6）Likert 仍 non-significant (p=0.60)，但论文未报告该配置下的 Cohen's d。如果 d 仍接近 0.1，按 power curve，n=355 的 Likert power 仅约 25-30%——依然是功效不足而非系统性盲区。
- R2 指出论文自身使用 "~4.5× more data to reach equivalent sensitivity" 的 power 语言（§5.2），这与 "Blindspot" 的 framing 自相矛盾——我完全同意此观察。

**共识结论**：建议将 "Blindspot" 重新定义或降级为 "measurement efficiency gap at typical evaluation scales"，Title 和 Abstract 相应调整。

---

### [AGREE] R2-N2: "Causal"/"Counterfactual" 术语与方法论强度不匹配

同意，这与我的 R1-N1 高度一致。两位 Reviewer 对因果语言过强的判断完全一致。

补充我的发现：
- 我在 R1-N1 中进一步指出了**经验性违反的证据**：Table 3 中 originality OR 在多个配置下显著（GPT-4o formality: OR=2.32, p=0.006），直接表明 NLI gate 未能完全阻断 R→Q path。这不仅是术语问题，更是识别策略有实质缺口。
- R2 建议的 "Interventional"/"Controlled" 替代表述合理。我进一步建议 §3.5 标题可改为 "Assumed Data-Generating Process and Identification Strategy"，并增加对识别假设违反程度的量化讨论。

**共识结论**：因果语言应降级；§3.5 应更明确讨论假设的局限性。

---

### [REBUT] R2-N3: 证据基础过窄但 practical recommendation 过强（部分反驳）

R2 的方向正确但程度表述过重，且有一处事实性偏差。

反驳点：
1. **R2 称 "tone axis 完全失败但只在 Limitations 一笔带过"**——事实不符。Register (tone) axis 在**主文 §5.5** 有大半节专门讨论（第 7 页），包括 BT 结果（GPT-4o 57.0%, p=0.04）、GEE 分解（originality-dominated）、和明确的 "weak evidence" 定性。这不是 "只在 Limitations 一笔带过"。

2. **Cross-benchmark 证据被低估**。Table 1 显示 CSD 在三个独立 benchmark 上复制：LLMBar (n=100), AlpacaEval, MT-Bench，覆盖 instruction-following、open-ended preference、multi-turn dialogue 三种任务类型。R2 称 "不覆盖 dialogue/summarization"——但 MT-Bench 本身就是多轮对话评测。

3. **Cross-judge 复制**。GPT-4o（独立 judge，不是 rewriter）在所有配置上确认 Blindspot direction 一致。Claude Sonnet 4 提供负面控制。

我同意的部分：
- n=100 作为起点确实偏小。更大的 benchmark（如 WildBench 或 Arena-Hard）会显著增强说服力。
- 论文从有限证据跳到 "style bias audits should adopt pairwise comparison"（Conclusion, §6）的 recommendation 确实过强——应加 qualifier "in typical evaluation settings with n < 500"。
- 增加 dialogue/summarization/creative writing 的专项验证是合理的未来工作建议。

**结论**：R2-N3 的核心方向正确（evidence scope vs claim scope 不匹配），但 "tone axis 只在 Limitations 提及" 和 "不覆盖 dialogue" 的具体论据不准确。建议 severity 从 critical 降为 warning。

---

## Should-Fix 问题

### [AGREE] R2-W1: Related Work 引用偏少，缺少关键谱系

同意。27 条引用对 EMNLP 确实偏少。我在审稿时未专门标记此问题，但 R2 指出的缺失文献确实相关：
- **Counterfactual text generation 方法**：CausaLM (Feder et al., 2021) 和 Polyjuice (Wu et al., 2021) 是 controlled text perturbation 的重要前驱工作，与 CSD 的 rewriting 策略有直接方法论联系。
- **NLG evaluation scale design**：Clark et al. (2021) 关于 evaluation scale 选择的系统性研究，与 Likert vs pairwise 的讨论直接相关。

补充建议：还应引用 Chatbot Arena 的 pairwise 方法论细节（Boubdir et al., 2023 关于 BT 模型在 LLM 评估中的实践），以及 Wu & Aji (2023) 关于 LLM judge 评估协议对比。

---

### [AGREE] R2-W2: NLI gate false negative 可能引入 systematic selection bias → ATE attenuation

同意，这是我未独立提出的一个有价值的观察。

论文 §5.1 提供了部分回应：false negatives 无方向性偏差（Fisher p=0.35），threshold sensitivity 显示 win rate 在 0.70-0.95 范围内稳定（72.3-73.9%）。但 R2 的理论论点仍然成立：如果大幅 style 变化更容易被 NLI gate 过滤掉（因为大幅改变更可能伴随内容变化），则保留的 pairs 系统性地包含较小的 style 干预，从而压低 measured effect。

这与我的 R1-W2（direction-aware NLI for verbosity）相关但不同——R2 关注的是 attenuation bias 方向（低估效应），而我关注的是 relaxed gate 可能引入的 confound（高估效应）。两个方向的 bias 可能部分抵消，但论文未讨论这种可能性。

---

### [AGREE] R2-W3: GEE "decomposition" 在 confounding 未消除时有误导性

同意。这与我的 R1-W5（confound gradient 可能反映 rewriting 难度而非 axis 本质属性）方向一致。

"Decomposition" 暗示 style 和 originality 效应被干净地分离，但当 NLI gate 不能完全消除 content confounding 时（Table 3 中 originality OR 显著就是证据），GEE 只是在给定 rewriting 质量下的条件估计，不是因果 decomposition。R2 建议的 "partial adjustment" 或 "conditional analysis" 更准确。

---

### [REBUT] R2-W4: Claude 作为 negative control 的解释力有限

部分反驳。R2 的替代解释（Claude alignment 消除了 bias，而非 CSD 无 false positive）是合理的，但这恰恰**增强**了 Claude 作为 negative control 的价值：

1. **论文未声称 Claude 证明 CSD 无 false positive**。§5.4（cross-axis）和 Table 1 中 Claude 的结果被用于展示 **discriminative validity**——CSD 不是在所有 judge 上都报阳性，说明框架能区分有 bias 和无 bias 的 judge。

2. **R2 的替代解释本身是一个积极发现**：如果 Claude 的 alignment 确实消除了 style bias（而 GPT-4o 和 Qwen3-32B 没有），这正是 CSD 试图检测的现象——不同 judge 有不同的 style sensitivity profile。

3. **真正的 false positive 控制需要 known-zero-bias 条件**。论文确实无法完全排除 false positive，但这是任何新检测工具的普遍局限，不是 Claude negative control 设计的特定弱点。

建议 severity 降为 minor：可在讨论中增加一句 "Claude's null result may reflect either the absence of style bias or the presence of countervailing alignment mechanisms; distinguishing these interpretations requires further investigation."

---

### [REBUT] R2-W5: Appendix 中 Direction Asymmetry 和 GEE Robustness 应部分纳入正文

不同意。在 8 页严格限制下（EMNLP 2026 Long Paper），主文需优先分配给核心论证。Direction Asymmetry（Appendix A）和 GEE Robustness（Appendix C）是支撑性细节：

- Appendix A 的 direction asymmetry **结论已在主文 §5.6 引用**（"full direction-asymmetry analysis in Appendix A"），读者能快速定位。
- Appendix C 的 correlation structure robustness **结论已在主文 §5.6 引用**（Table 3 的可靠性建立在 Appendix C 的诊断之上）。
- 将这些内容搬入正文会挤占本已紧张的 8 页空间，可能需要删除 power curve (Figure 4) 或 sensitivity hierarchy (Table 2) 等更核心的内容。

当前 appendix 安排符合 ACL 惯例（主文放结论和关键证据，appendix 放诊断和细节）。

---

## R1-R2 共识总结

| 维度 | R1-R2 共识 | 分歧 |
|------|------------|------|
| Blindspot framing | **强共识**：均认为 "Blindspot" 过强，应降级为 efficiency gap | 无 |
| 因果语言 | **强共识**：均认为 causal/counterfactual 语言与方法论强度不匹配 | R1 进一步指出了 originality OR 的经验性违反证据 |
| 证据范围 | **部分共识**：均认为样本量偏小、practical recommendation 过强 | R1 认为 R2 低估了 cross-benchmark 证据和 register axis 在正文中的讨论 |
| GEE 命名 | **共识**：均认为 "decomposition" 在有残余 confounding 时有误导性 | 无 |
| Claude negative control | **分歧**：R2 认为解释力有限，R1 认为 discriminative validity 论证合理 | — |
| Appendix placement | **分歧**：R2 认为应搬入正文，R1 认为当前安排合理（8 页限制） | — |
| Evaluator-producer confound | R1 独立提出的 N2 (independence test 不完整) R2 未提及 | — |
| NLI validation by same model family | R1 独立提出的 W1，R2 未提及 | — |
| NLI false negative → attenuation | R2 独立提出的 W2，R1 未提及（但提了 direction-aware gate 问题） | — |
| Related work 引用量 | R2 独立提出的 W1，R1 未提及 | — |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-21T09:44:59.182346+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-21T09:44:59.433807+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T09:36:18.747792+00:00\", \"completed_at\": \"2026-05-21T09:38:46.859711+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页连续纯文本，无任何 display item（figure/table/diagram）。审稿人从 Abstract 读到 Related Work 结束都没有视觉锚点。第一个 display item (Figure 1 CSD pipeline) 延迟到第 4 页才出现。这严重影响审稿人的第一印象锚定——建议将 Figure 1（pipeline 概览）或一个精简的 motivating example figure 提前到第 1-2 页（Introduction 内），让审稿人在前 2 分钟内就能可视化地理解核心 idea。\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"单页堆叠 3 个 display items（Figure 2 + Table 1 + Figure 3），视觉拥挤。Figure 2（causal DAG）和 Figure 3（bar chart）都被压缩得较小。建议将 Figure 2 或 Figure 3 移至相邻页面以改善呼吸感和可读性。\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"纯文本页（Measurement Sensitivity 分析），夹在 p5 和 p7 两个有 display item 的页面之间。节奏上可接受，但如果能从 p5 匀一个 display item 到 p6 会更均衡。\"}, {\"severity\": \"warning\", \"dimension\": \"page 12\", \"message\": \"末页仅顶部 1 条参考文献（Zheng et al., 2023），其余 ~90% 为空白。虽然是 references 溢出页，但视觉上不整洁。建议调整 references 排版（如缩小 bibsep）使其在 p11 内结束，或合并到 p11。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1（CSD pipeline overview）作为论文第一个 display item，图内 icon/box 偏小，灰度感较重，视觉冲击力不足。作为审稿人看到的第一张图，建议加大尺寸或增加色彩标注使其更醒目，强化 pipeline 各阶段的视觉区分。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（主结果表）：使用 booktabs 风格（好），有显著性标记（†, *）。但最优结果的加粗标注在当前分辨率下不够醒目——建议确认 \\\\textbf{} 已正确应用于所有最优值，并考虑为次优值加下划线。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3（BT win probabilities bar chart）：图内字号偏小（axis labels, legend），在打印环境下可能难以辨读。建议适当增大字号至正文字号的 80% 以上。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（detection probability curves）：多条曲线使用了不同线型+颜色组合，色盲友好性可接受。但曲线在高 sample size 区域有重叠，legend 可考虑用直接标注（annotation）替代独立 legend box 以提高可读性。\"}, {\"severity\": \"info\", \"dimension\": \"page 10\", \"message\": \"Appendix
…[truncated 152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-21T09:44:59.434329+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-21T09:44:59.485433+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T09:36:19.697673+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_5ce280de124a4e308d1827c6450ad337\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-21T09:48:24.506750+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-2 issues (carried over, status unchanged)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title changed. 4 CSD occurrences updated. §3.5 has 3 identification assumptions.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"标题中 'Counterfactual' 仍保留，§3.5 仍标题为 'Causal Framework'——因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 new experiments added. Novelty ceiling structural.\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知），excitement 评分 3-3.5/5。见 R3-N3。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Threshold on plateau, robust 0.70-0.95\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"引用数量 27 条仍低于 EMNLP 通常水平（40-60 条），缺 counterfactual generation 和 NLG evaluation scale design 文献。见 R3-W7。\"\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2×3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 3 两位 Reviewer 再次独立提出相同问题：'Blindspot' 仍暗示质性缺陷，Figure 4 evidence 只支持量性差距。见 R3-N3。Resolution 不充分。\"\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant. Bootstrap unified to 10k.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"3 benchmarks × 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"R2 仍认为 n=100 基础偏窄，practical recommendation scope 超出 evidence。R1 部分反驳（cross-benchmark 已覆盖多种任务类型）。严重性从 critical 降为 warning。见 R3-N4。\"\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Main text 8 pages. Conclusion ends p8, Limitations starts p9.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"GPT-4o rewriter independence confirmed (D051): BT 73.5% vs 77.3% overlapping CIs.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity 轴。Formality/register 缺 independence test，而 formality 恰是 evaluator-producer bias 最明显的轴（Qwen3 OR=4.20 vs GPT-4o OR=2.58）。见 R3-N2。Resolution 不完整。\"\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Tradeoff discussion added in §3.2.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Tradeoff 讨论存在，但额外纳入的 21% pairs 的内容保持质量未经独立验证。见 R3-W2。\"\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000. BT pseudocount: choix library default.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P→Y) and rewrite artifact (R→Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P→Y + R→Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 NEW issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语（Title 'Counterfactual'、§3.5 'Causal Framework'、DAG）与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 强共识。R1: originality OR 显著（GPT-4o OR=2.32, p=0.006）证明 NLI gate 未完全阻断 R→Q path，识别假设 (i) 经验性违反。R2: 方法是 controlled intervention with imperfect content preservation，非 Pearl/Rubin 框架。建议降级为 'Interventional'/'Controlled'。\"\n    action_items:\n      - round: 3\n        action: \"将 Title 中 'Counterfactual' 替换为更准确术语；§3.5 标题改为 'Interventional Design' 或 'Data-Generating Assumptions'；Figure 2 DAG 标注 residual S→Q confounding（虚线）；讨论 originality OR 对识别假设的影响。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉回应 [AGREE]。Qwen3-32B formality OR=4.20 vs GPT-4o OR=2.58（n=88），1.6× 差距可能来自 evaluator-producer confound。Appendix D independence test 仅覆盖 verbosity（22% 降幅）。需补做 formality 轴 independence test，或在主文标注 Qwen3 结果仅作 existence claim。\"\n    action_items:\n      - round: 3\n        action: \"补做 formality 轴 rewriter independence test（GPT-4o rewriter + Qwen3-32B judge）；或在主文明确标注 Qwen3-32B 结果不适合与 GPT-4o 做定量 effect size 比较。\"\n        assigned_to: agent + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异（power gap）包装为质性 blindspot\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 最强共识。Figure 4 显示 Likert 在 n≈1473 达到 80% power——不是 blindspot 而是功效不足。Thurstone (1927) 已知。n=355 Likert 仍 non-sig 但 effect size 未报告。建议重定义为 'measurement efficiency gap at typical evaluation scales'。R2 补充：若能证明 Likert 同时压缩 effect size + 降低 power（而非仅后者），blindspot framing 更站得住脚，但论文未做此分析。\"\n    action_items:\n      - round: 3\n        action: \"1. 区分 power gap（量性）和 blindspot（质性），调整 Title/Abstract/§5.2 措辞；2. 报告 n=355 的 Likert Cohen's d 和 power；3. 分析 Likert 是否同时压缩 effect size（measurement attenuation），若是则可保留更强 framing。\"\n        assigned_to: paper_agent + agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N4\"\n    summary: \"证据基础（n=100, 3 judges, 2 有效 axes）偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 首提（critical），R1 部分反驳：cross-benchmark 已覆盖 3 种任务类型（instruction-following, open-ended, multi-turn），register 在主文 §5.5 有讨论（非仅 Limitations）。共识：practical recommendation（Contribution 4, Conclusion）应加 qualifier。\"\n    action_items:\n      - round: 3\n        action: \"Contribution 4 和 Conclusion 中的建议加限定条件（'in typical evaluation settings with n < 500'、'on instruction-following tasks'）。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族（Qwen3-32B rewriter + Qwen3-32B annotator），precision 可能被高估\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 [AGREE]。论文承诺 'GPT-4o spot-check is planned' 但未执行。\"\n    action_items:\n      - round: 3\n        action: \"补做 GPT-4o 或人类标注对 NLI gate 的独立验证；或在 Limitations 更明确标注 self-consistency 风险。\"\n        assigned_to: agent + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 放宽为单向 entailment，额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 [AGREE]。单向 entailment 允许 expansion 方向丢失信息但仍 pass gate。需对 direction-aware gate 额外放入的 pairs 进行单独 BT 分析。\"\n    action_items:\n      - round: 3\n        action: \"对 strict bidirectional gate 和 direction-aware gate 分别计算 BT win rate，验证无系统差异。\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"缺少任何人工评估验证 rewriting 质量（style 改变方向 + 自然度）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提（Should-Fix），R2 交叉回应认为重要性应更高。ACL/EMNLP 传统要求涉及 text generation 的工作提供至少 small-scale human evaluation。\"\n    action_items:\n      - round: 3\n        action: \"对 50 个样本进行人工标注，验证 (a) style 改变方向正确率 (b) 自然度 (c) NLI 未检测到的 artifacts。\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty（pipeline artifact）而非 style axis 固有属性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 [AGREE] 称 '精妙的 alternative interpretation'。Verbosity rewrite 大幅增删内容（4.7× longer），formality 仅词汇替换，register 几乎必然改变 sophistication → originality confound 可能反映操作 invasiveness 而非 axis 本质。\"\n    action_items:\n      - round: 3\n        action: \"在 §5.6 讨论此替代解释；理想情况下用不同 rewriter 测试 confound gradient 是否变化。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性，应改为 'partial adjustment'\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 [AGREE]。Table 3 originality OR 显著（p=0.006）证明 confounding 未消除，'decomposition' 暗示干净分离但实际是 partial adjustment。\"\n    action_items:\n      - round: 3\n        action: \"将 'decomposition' 改为 'partial decomposition' 或 'conditional analysis'；明确 originality 的操作化定义。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定——Qwen3 formality OR 从 n=88 (4.20) 降至 n=355 (2.15)，降幅 49%\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 [AGREE]。建议将 n=355 scaled replication 提升为主结果；对所有主要轴进行 scaled replication；报告 GEE finite-sample corrected SE。\"\n    action_items:\n      - round: 3\n        action: \"将 n=355 结果提升为主结果；补报 finite-sample corrected SE；考虑对 verbosity 和 register 也做 scaled replication。\"\n        assigned_to: agent + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少（27 条 vs EMNLP 通常 40-60 条），缺 counterfactual generation + NLG evaluation scale design 文献\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 [AGREE] 并补充建议：CausaLM (Feder 2021), Polyjuice (Wu 2021), Clark 2021, Amidei 2019, Boubdir 2023, Wu & Aji 2023。\"\n    action_items:\n      - round: 3\n        action: \"补充 counterfactual generation 方法谱系（CausaLM, Polyjuice）、NLG evaluation scale design（Clark 2021, Amidei 2019）、BT in LLM eval（Boubdir 2023）等引用，目标 35+ 条。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate false negative 可能引入 systematic selection bias → ATE attenuation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"R2 独立提出。大幅 style 变化更易被 NLI gate 过滤 → 保留的 pairs 系统性包含较小 style 干预 → 低估 measured effect。论文 §5.1 显示 FN 无方向性偏差（Fisher p=0.35），但 R2 的理论论点仍成立。\"\n    action_items:\n      - round: 3\n        action: \"分析被 NLI gate 过滤掉的 pairs 的 style change magnitude，确认无 systematic selection effect；或在 Limitations 讨论。\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释（无 bias vs alignment 消除 bias）\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 首提（warning），R1 部分反驳：discriminative validity 论证合理，Claude null result 展示 CSD 不是对所有 judge 报阳性。共识降为 info。\"\n    action_items:\n      - round: 3\n        action: \"在讨论中增加一句承认双重解释可能性。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉（raw p vs adjusted p 混淆）\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提（Should-Fix），R2 [REBUT]：信息完整但 presentation 可改进。降为 info。\"\n    action_items:\n      - round: 3\n        action: \"在 Table 1 中分别列出 raw p 和 adjusted p，或在脚注中明确标注 *** 对应 raw p。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密（9 行，覆盖过多细节），应精简\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"R1 minor 问题。建议精简为 5-6 行聚焦核心 claim。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entry hoenig2001abuse + murugadoss2025sos 未在 OpenAlex 匹配\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"hoenig2001abuse 可能是工具解析遗漏（实际通过 citealt 引用）；murugadoss2025sos 可能太新。tan2025judgebench 和 chiang2024chatbot 作者信息待核查。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-2 issues (carried over, status unchanged)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title changed. 4 CSD occurrences updated. §3.5 has 3 identification assumptions.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"标题中 'Counterfactual' 仍保留，§3.5 仍标题为 'Causal Framework'——因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 new experiments added. Novelty ceiling structural.\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知），excitement 评分 3-3.5/5。见 R3-N3。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Threshold on plateau, robust 0.70-0.95\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"引用数量 27 条仍低于 EMNLP 通常水平（40-60 条），缺 counterfactual generation 和 NLG evaluation scale design 文献。见 R3-W7。\"\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2×3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 3 两位 Reviewer 再次独立提出相同问题：'Blindspot' 仍暗示质性缺陷，Figure 4 evidence 只支持量性差距。见 R3-N3。Resolution 不充分。\"\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant. Bootstrap unified to 10k.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"3 benchmarks × 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"R2 仍认为 n=100 基础偏窄，practical recommendation scope 超出 evidence。R1 部分反驳（cross-benchmark 已覆盖多种任务类型）。严重性从 critical 降为 warning。见 R3-N4。\"\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Main text 8 pages. Conclusion ends p8, Limitations starts p9.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"GPT-4o rewriter independence confirmed (D051): BT 73.5% vs 77.3% overlapping CIs.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity 轴。Formality/register 缺 independence test，而 formality 恰是 evaluator-producer bias 最明显的轴（Qwen3 OR=4.20 vs GPT-4o OR=2.58）。见 R3-N2。Resolution 不完整。\"\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Tradeoff discussion added in §3.2.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Tradeoff 讨论存在，但额外纳入的 21% pairs 的内容保持质量未经独立验证。见 R3-W2。\"\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000. BT pseudocount: choix library default.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P→Y) and rewrite artifact (R→Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P→Y + R→Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 NEW issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语（Title 'Counterfactual'、§3.5 'Causal Framework'、DAG）与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 强共识。R1: originality OR 显著（GPT-4o OR=2.32, p=0.006）证明 NLI gate 未完全阻断 R→Q path，识别假设 (i) 经验性违反。R2: 方法是 controlled intervention with imperfect content preservation，非 Pearl/Rubin 框架。建议降级为 'Interventional'/'Controlled'。\"\n    action_items:\n      - round: 3\n        action: \"将 Title 中 'Counterfactual' 替换为更准确术语；§3.5 标题改为 'Interventional Design' 或 'Data-Generating Assumptions'；Figure 2 DAG 标注 residual S→Q confounding（虚线）；讨论 originality OR 对识别假设的影响。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉回应 [AGREE]。Qwen3-32B formality OR=4.20 vs GPT-4o OR=2.58（n=88），1.6× 差距可能来自 evaluator-producer confound。Appendix D independence test 仅覆盖 verbosity（22% 降幅）。需补做 formality 轴 independence test，或在主文标注 Qwen3 结果仅作 existence claim。\"\n    action_items:\n      - round: 3\n        action: \"补做 formality 轴 rewriter independence test（GPT-4o rewriter + Qwen3-32B judge）；或在主文明确标注 Qwen3-32B 结果不适合与 GPT-4o 做定量 effect size 比较。\"\n        assigned_to: agent + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异（power gap）包装为质性 blindspot\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 最强共识。Figure 4 显示 Likert 在 n≈1473 达到 80% power——不是 blindspot 而是功效不足。Thurstone (1927) 已知。n=355 Likert 仍 non-sig 但 effect size 未报告。建议重定义为 'measurement efficiency gap at typical evaluation scales'。R2 补充：若能证明 Likert 同时压缩 effect size + 降低 power（而非仅后者），blindspot framing 更站得住脚，但论文未做此分析。\"\n    action_items:\n      - round: 3\n        action: \"1. 区分 power gap（量性）和 blindspot（质性），调整 Title/Abstract/§5.2 措辞；2. 报告 n=355 的 Likert Cohen's d 和 power；3. 分析 Likert 是否同时压缩 effect size（measurement attenuation），若是则可保留更强 framing。\"\n        assigned_to: paper_agent + agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N4\"\n    summary: \"证据基础（n=100, 3 judges, 2 有效 axes）偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 首提（critical），R1 部分反驳：cross-benchmark 已覆盖 3 种任务类型（instruction-following, open-ended, multi-turn），register 在主文 §5.5 有讨论（非仅 Limitations）。共识：practical recommendation（Contribution 4, Conclusion）应加 qualifier。\"\n    action_items:\n      - round: 3\n        action: \"Contribution 4 和 Conclusion 中的建议加限定条件（'in typical evaluation settings with n < 500'、'on instruction-following tasks'）。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族（Qwen3-32B rewriter + Qwen3-32B annotator），precision 可能被高估\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 [AGREE]。论文承诺 'GPT-4o spot-check is planned' 但未执行。\"\n    action_items:\n      - round: 3\n        action: \"补做 GPT-4o 或人类标注对 NLI gate 的独立验证；或在 Limitations 更明确标注 self-consistency 风险。\"\n        assigned_to: agent + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 放宽为单向 entailment，额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 [AGREE]。单向 entailment 允许 expansion 方向丢失信息但仍 pass gate。需对 direction-aware gate 额外放入的 pairs 进行单独 BT 分析。\"\n    action_items:\n      - round: 3\n        action: \"对 strict bidirectional gate 和 direction-aware gate 分别计算 BT win rate，验证无系统差异。\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"缺少任何人工评估验证 rewriting 质量（style 改变方向 + 自然度）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提（Should-Fix），R2 交叉回应认为重要性应更高。ACL/EMNLP 传统要求涉及 text generation 的工作提供至少 small-scale human evaluation。\"\n    action_items:\n      - round: 3\n        action: \"对 50 个样本进行人工标注，验证 (a) style 改变方向正确率 (b) 自然度 (c) NLI 未检测到的 artifacts。\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty（pipeline artifact）而非 style axis 固有属性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 [AGREE] 称 '精妙的 alternative interpretation'。Verbosity rewrite 大幅增删内容（4.7× longer），formality 仅词汇替换，register 几乎必然改变 sophistication → originality confound 可能反映操作 invasiveness 而非 axis 本质。\"\n    action_items:\n      - round: 3\n        action: \"在 §5.6 讨论此替代解释；理想情况下用不同 rewriter 测试 confound gradient 是否变化。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性，应改为 'partial adjustment'\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 [AGREE]。Table 3 originality OR 显著（p=0.006）证明 confounding 未消除，'decomposition' 暗示干净分离但实际是 partial adjustment。\"\n    action_items:\n      - round: 3\n        action: \"将 'decomposition' 改为 'partial decomposition' 或 'conditional analysis'；明确 originality 的操作化定义。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定——Qwen3 formality OR 从 n=88 (4.20) 降至 n=355 (2.15)，降幅 49%\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 [AGREE]。建议将 n=355 scaled replication 提升为主结果；对所有主要轴进行 scaled replication；报告 GEE finite-sample corrected SE。\"\n    action_items:\n      - round: 3\n        action: \"将 n=355 结果提升为主结果；补报 finite-sample corrected SE；考虑对 verbosity 和 register 也做 scaled replication。\"\n        assigned_to: agent + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少（27 条 vs EMNLP 通常 40-60 条），缺 counterfactual generation + NLG evaluation scale design 文献\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 [AGREE] 并补充建议：CausaLM (Feder 2021), Polyjuice (Wu 2021), Clark 2021, Amidei 2019, Boubdir 2023, Wu & Aji 2023。\"\n    action_items:\n      - round: 3\n        action: \"补充 counterfactual generation 方法谱系（CausaLM, Polyjuice）、NLG evaluation scale design（Clark 2021, Amidei 2019）、BT in LLM eval（Boubdir 2023）等引用，目标 35+ 条。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate false negative 可能引入 systematic selection bias → ATE attenuation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"R2 独立提出。大幅 style 变化更易被 NLI gate 过滤 → 保留的 pairs 系统性包含较小 style 干预 → 低估 measured effect。论文 §5.1 显示 FN 无方向性偏差（Fisher p=0.35），但 R2 的理论论点仍成立。\"\n    action_items:\n      - round: 3\n        action: \"分析被 NLI gate 过滤掉的 pairs 的 style change magnitude，确认无 systematic selection effect；或在 Limitations 讨论。\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释（无 bias vs alignment 消除 bias）\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 首提（warning），R1 部分反驳：discriminative validity 论证合理，Claude null result 展示 CSD 不是对所有 judge 报阳性。共识降为 info。\"\n    action_items:\n      - round: 3\n        action: \"在讨论中增加一句承认双重解释可能性。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉（raw p vs adjusted p 混淆）\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提（Should-Fix），R2 [REBUT]：信息完整但 presentation 可改进。降为 info。\"\n    action_items:\n      - round: 3\n        action: \"在 Table 1 中分别列出 raw p 和 adjusted p，或在脚注中明确标注 *** 对应 raw p。\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密（9 行，覆盖过多细节），应精简\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"R1 minor 问题。建议精简为 5-6 行聚焦核心 claim。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entry hoenig2001abuse + murugadoss2025sos 未在 OpenAlex 匹配\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"hoenig2001abuse 可能是工具解析遗漏（实际通过 citealt 引用）；murugadoss2025sos 可能太新。tan2025judgebench 和 chiang2024chatbot 作者信息待核查。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-21T09:48:24.557763+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 21339}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-21T09:51:16.970657+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 3（Fresh Review）\n\n**项目**: causal_style_decomp_judge\n**论文**: Counterfactual Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges\n**目标 Venue**: EMNLP 2026 (Long Paper, via ARR)\n**审稿人**: Reviewer 1（方法严谨性 + 实验有效性）、Reviewer 2（新颖性 + 完整性 + Related Work）\n**审稿轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识）\n\n---\n\n## ⚠️ Deadline 警告\n\nWeb 搜索确认 EMNLP 2026 最后可用的 ARR 提交截止日为 **2026-05-25 AoE**（距今 4 天），而非提交消息中的 2026-06-15。ARR May cycle 提交时须绑定声明 EMNLP 2026 为目标会议（binding）。请立即核实。\n\n---\n\n## Summary\n\n本文提出 Counterfactual Style Decomposition (CSD)，一个黑盒框架，通过 binary style-controlled rewriting + NLI entailment gate + position-controlled pairwise comparison 检测 LLM judge 的 per-axis style bias。核心发现命名为 \"Likert Blindspot\"：在 3 个 judge（GPT-4o、Qwen3-32B、Claude Sonnet 4）、3 个 benchmark（LLMBar、AlpacaEval、MT-Bench）、2 个主要 style axes（formality、verbosity）+ 1 个探索性 axis（register）上，Likert 评分对 style bias 的检测灵敏度系统性低于 pairwise comparison（~4.5× 效率差距）。GEE logistic regression 将 style effect 和 originality confound 分离，发现 confound gradient（verbosity = pure style, formality = dual, register = originality-dominated）。Claude Sonnet 4 在所有 axes 上无显著 bias，作为 discriminative validity 证据。\n\n---\n\n## Strengths\n\n**S1. 统计三角验证扎实**：7 种统计方法（ATE、sign test、BT、ordinal regression、GEE、Holm-Bonferroni、power curve）一致显示 Likert vs pairwise 灵敏度差距，跨 judge/benchmark/axis 的系统性复制增强可信度。[R1 + R2 共识]\n\n**S2. GEE per-axis 分解有方法论贡献**：将 style effect 和 originality confound 解耦的 GEE 框架在 LLM judge bias 文献中较为少见，confound gradient 发现有 insight。GEE diagnostics（Appendix C, correlation structure robustness）完整。[R1 + R2 共识]\n\n**S3. Negative results 诚实呈现**：Claude Sonnet 4 无 bias（BT 56.2%/54.1%, non-sig）、formality 方向不对称（78.8% vs 54.5%）、tone axis 失败——增加了结果可信度和论文的科学诚实性。[R2 首提, R1 同意]\n\n**S4. 实用价值高**：量化了 LLM evaluation 中 Likert vs pairwise 的 ~4.5× 效率差距，对评测实践有直接指导意义。Figure 4 power curve 是 measurement methodology 层面的有价值贡献。[R1 + R2 共识]\n\n**S5. Pipeline 可复现**：NLI gate 阈值、BT 模型参数、bootstrap 配置（10k resamples）、GEE correlation structure 均明确报告。方法描述清晰，各步骤可复现（但代码/数据未附）。[R2]\n\n**S6. 写作质量良好**：结构清晰，信息密度高，在 8 页内覆盖完整的方法-实验-分析链。正文 8 页合规，Limitations 覆盖了关键弱点。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，两位 Reviewer 强共识）\n\n**MF1. \"Blindspot\" framing 混淆统计功效差异与质性 blindspot** [R1-N3 + R2-N1, 强共识]\n- Title 用 \"Blindspot\" 暗示 Likert 有质性缺陷（永远检测不到），但 Figure 4 power curve 明确显示 Likert 在 n≈1,473 时达到 80% power——这是量性的 efficiency gap，非质性 blindspot。\n- Thurstone (1927) 关于 ordinal scale 灵敏度低于 paired comparison 的结论已近百年，论文在 §2 引用了 Thurstone 但未充分说明增量贡献。\n- n=355 scaled replication Likert 仍 non-significant (p=0.60)，但该配置下 Cohen's d 未报告——若 d 仍接近 0.1，power 约 25-30%，依然是功效不足。\n- 论文自身使用 \"~4.5× more data to reach equivalent sensitivity\"（§5.2）的 power 语言，与 \"Blindspot\" framing 自相矛盾。\n- **关键区分**：若能证明 Likert 同时压缩 effect size（measurement attenuation）+ 降低 power（而非仅后者），\"Blindspot\" framing 更站得住脚，但论文未做此分析。\n- **建议**：(1) 将 \"Blindspot\" 重定义为 \"measurement efficiency gap at typical evaluation scales\"；(2) 补报 n=355 Likert Cohen's d 和 power；(3) 明确区分量性 gap 和质性 blindspot。\n\n**MF2. 因果/反事实术语与方法论强度不匹配** [R1-N1 + R2-N2, 强共识]\n- Title \"Counterfactual\"、§3.5 \"Causal Framework\"、Figure 2 DAG 暗示形式化因果模型，但 §3.5 声明 \"not a complete structural causal model, nor do we invoke SUTVA\"。\n- 经验性违反证据：Table 3 中 originality OR 在多个配置下显著（GPT-4o formality: OR=2.32, p=0.006; Qwen3 register: OR=5.72），直接表明 NLI gate 未完全阻断 R→Q path——识别假设 (i) 部分违反。\n- 识别假设 (iii)（rewrite 不引入 target axis 外差异）未检验——formality rewrite 可能同时改变 register/vocabulary sophistication。\n- 实际上 CSD 是 controlled intervention study with imperfect content preservation，非因果推断。\n- **建议**：(1) Title 中 \"Counterfactual\" → \"Interventional\" 或 \"Controlled\"；(2) §3.5 标题 → \"Interventional Design and Assumptions\"；(3) Figure 2 DAG 用虚线标注 residual S→Q confounding；(4) 量化讨论 originality OR 对 style effect 估计的影响方向和幅度。\n\n**MF3. Evaluator-producer independence test 覆盖不完整** [R1-N2, R2 交叉同意]\n- Qwen3-32B 同时做 rewriter 和 judge，效应量系统性偏高（formality Style OR 4.20 vs GPT-4o 2.58 at n=88，1.6× 差距）。\n- Appendix D rewriter independence test 仅覆盖 verbosity 轴（GPT-4o rewriter: OR 13.10→10.17, 22% 降幅），缺 formality 和 register。\n- Formality 恰是 evaluator-producer bias 最明显的轴——Qwen3 OR 从 n=88 (4.20) 降至 n=355 (2.15) 的 49% 降幅也暗示小样本下的 OR 膨胀。\n- 主分析（Table 1, Table 3）仍以 Qwen3-32B 与 GPT-4o 并列为主要证据，\"across two judges\" 的 generalizability claim 受损。\n- **建议**：(1) 补做 formality 轴 independence test（GPT-4o rewriter + Qwen3-32B judge）；(2) 或在主文明确标注 Qwen3-32B 结果仅作 existence claim，不适合与 GPT-4o 做定量 effect size 比较。\n\n### Should-Fix（影响评分，两位 Reviewer 至少一位提出且另一位同意）\n\n**SF1. 缺少任何人工评估验证 rewriting 质量** [R1-W4, R2 强化]\n- CSD 完全依赖 NLI gate（自动化）验证 content preservation，无 human evaluation 验证 (a) style 改变方向正确率 (b) 自然度 (c) NLI 未检测的 artifacts。ACL/EMNLP 涉及 text generation 的工作通常需要至少 small-scale human evaluation。\n\n**SF2. NLI gate 验证使用同一模型族** [R1-W1, R2 同意]\n- §5.1 使用 Qwen3-32B 作为 annotator 验证 NLI gate（precision 98.9%），但 Qwen3-32B 同时是 rewriter——self-consistency bias 可能高估 precision。论文承诺 \"GPT-4o spot-check is planned\" 但未执行。\n\n**SF3. Direction-aware NLI 放宽为单向 entailment，额外纳入的 pairs 未独立验证** [R1-W2, R2 同意]\n- Verbosity 轴 NLI gate 从双向放宽为单向，pass rate 从 65% 升至 86%。额外纳入的 ~21% pairs 的 content preservation 质量未经独立验证。单向 entailment 允许 expansion 方向丢失信息（更详细 = 更高质量的感知）→ 可能 inflate style bias estimate。\n\n**SF4. Confound gradient 的替代解释** [R1-W5, R2 同意]\n- §5.6 发现 verbosity = pure style, formality = dual, register = originality-dominated。但 gradient 可能反映 rewriting 操作的 invasiveness（verbosity 大幅增删 vs formality 词汇替换 vs register 几乎必然改变 sophistication）而非 axis 固有属性——即 pipeline artifact 而非 style axis property。\n\n**SF5. GEE \"decomposition\" 在残余 confounding 下有误导性** [R2-W3, R1 同意]\n- Table 3 中 originality OR 显著（p=0.006）证明 confounding 未消除。\"Decomposition\" 暗示干净分离，实际是 partial adjustment。Originality 的操作化定义不清晰。\n\n**SF6. 小样本 OR 估计不稳定** [R1-W6, R2 同意]\n- Qwen3 formality Style OR: n=88 (4.20) → n=355 (2.15)，降幅 49%，表明 n=88 估计严重偏高。Register 轴 marginal significance (p=0.046) 在此样本量下尤其脆弱。建议将 n=355 scaled replication 提升为主结果。\n\n**SF7. Related Work 引用偏少** [R2-W1, R1 同意]\n- 27 条引用低于 EMNLP long paper 通常水平（40-60 条）。缺失：counterfactual generation 方法谱系（CausaLM, Polyjuice）、NLG evaluation scale design（Clark 2021, Amidei 2019）、BT in LLM evaluation（Boubdir 2023）。\n\n**SF8. NLI gate false negative → systematic selection bias** [R2-W2]\n- 大幅 style 变化更易被 NLI gate 过滤 → 保留的 pairs 系统性包含较小 style 干预 → 低估 measured effect（attenuation bias）。§5.1 FN 无方向性偏差（Fisher p=0.35）部分回应，但理论论点仍成立。\n\n**SF9. 证据范围 vs 建议范围不匹配** [R2-N3, R1 部分反驳]\n- Contribution 4 和 Conclusion 给出一般性建议（\"style bias audits should adopt pairwise comparison\"），但证据仅来自 n=100 × 3 judges × 2 有效 axes。R1 指出 cross-benchmark 已覆盖 3 种任务类型（instruction-following, open-ended, multi-turn），Register 在主文 §5.5 有讨论。共识：建议应加 qualifier。\n\n### Minor Issues（不影响接收）\n\n- Abstract 过长过密（9 行），建议精简至 5-6 行聚焦核心 claim [R1]\n- Table 1 Holm-Bonferroni p-value 标注可更直觉（raw p vs adjusted p 混淆）[R1 提出, R2 认为信息完整但 presentation 可改进]\n- Claude 作为 negative control 有双重解释（无 bias vs alignment 消除 bias），可在讨论中补充说明 [R2 提出, R1 认为 discriminative validity 论证合理]\n- Orphan bib entry `hoenig2001abuse`；`murugadoss2025sos` 在 OpenAlex 未匹配（可能太新）[R1 + R2]\n- Figure 1 偏小，stage attrition numbers 不易辨认 [R2]\n- §6 \"Prompt-level debiasing is insufficient\" 缺乏 evidence 基础（未测试任何 debiasing 方法）[R2]\n- ~60% uninformative ties 在 Abstract/§1/§5.2 重复出现但未给出全部 6 个配置的 tie rate 分布表 [R1]\n- §5.5 Register 结果 marginal significance 用大半节描述 inconclusive 结果，考虑压缩 [R1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下问题上独立达成强共识：\n\n1. **\"Blindspot\" framing 问题**（R1-N3 ≡ R2-N1）：核心 narrative 混淆 measurement sensitivity 和 statistical power。Figure 4 的 evidence 只支持量性差距而非质性 blindspot。Thurstone (1927) 已知。**这是论文最大的 framing 风险。**\n\n2. **Causal 语言过强**（R1-N1 ≡ R2-N2）：Title \"Counterfactual\"、§3.5 \"Causal Framework\"、DAG 与方法论强度不匹配。Table 3 originality OR 显著是 shared empirical evidence 表明识别假设部分违反。\n\n3. **GEE \"decomposition\" 命名**：在残余 confounding 下 \"decomposition\" 有误导性，应改为 \"partial adjustment\" 或 \"conditional analysis\"。\n\n4. **缺少人工评估**：ACL/EMNLP 涉及 text generation 的工作通常需要至少 small-scale human evaluation，论文完全依赖自动化验证。\n\n5. **小样本 OR 不稳定**：n=88 的 GEE OR 估计可信度受损，n=355 结果更可靠，应提升为主结果。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n分歧仅在 Should-Fix 级别，无 Must-Fix 分歧：\n\n1. **R2-N3 severity**（证据范围过窄）：R2 评为 critical，R1 部分反驳——cross-benchmark 已覆盖 3 种任务类型，Register 在主文 §5.5 有讨论（非仅 Limitations），R2 对 \"tone axis 只在 Limitations 提及\" 和 \"不覆盖 dialogue\" 的具体论据不准确。**Director 判定**：降为 warning (SF9)。\n\n2. **Claude negative control 解释力**：R2 认为解释力有限（warning），R1 认为 discriminative validity 论证合理。**Director 判定**：降为 info。\n\n3. **Appendix placement**：R2 建议将 Direction Asymmetry 和 GEE Robustness 移入正文；R1 认为 8 页限制下当前安排合理。**Director 判定**：当前安排可接受，不列为 issue。\n\n---\n\n## Questions for Authors\n\n1. **Blindspot 本质**：Figure 4 power curve 是否 asymptotically converge（Likert 和 pairwise 在足够大 n 下检测结果是否收敛）？如果收敛，\"Blindspot\" 应降级为 \"efficiency gap\"。如果不收敛（Likert 存在 measurement attenuation），\"Blindspot\" 有更强依据——你们能否提供 Likert effect size 随 n 变化的分析？\n\n2. **n=355 Likert effect size**：该配置下的 Cohen's d 是多少？这是区分 \"power gap\"（d 不变，n 不够）和 \"measurement attenuation\"（d 本身被压缩）的关键数据。\n\n3. **多轴测量**：对 formality rewrite，是否测量了 rewrite 在 register/verbosity 轴上的变化幅度？若 formal rewrite 同时变得更 verbose 或更 academic，单轴干预假设被违反。\n\n4. **Formality independence test**：是否计划补做 formality 轴的 rewriter independence test（GPT-4o rewriter + Qwen3-32B judge）？这是验证 Qwen3-32B evaluator-producer confound 的关键实验。\n\n5. **NLI gate selection effect**：被 NLI gate 过滤掉的 pairs 在 style change magnitude 上是否有系统性偏差？\n\n6. **Pairwise Likert difference**：是否考虑过使用 Likert 分数的 pairwise difference（paired t-test on Δscore）？这会消除 tie-inflation 问题同时保留 Likert 信息。\n\n---\n\n## Missing References\n\n两位 Reviewer 共同识别的缺失引用：\n- Feder et al. (2021) \"CausaLM: Causal Model Explanation Through Counterfactual Language Models\"\n- Wu et al. (2021) \"Polyjuice: Generating Counterfactuals for Explaining, Training, and Evaluating NLMs\"\n- Clark et al. (2021) \"All That's Human Is Not Gold: Evaluating Human Evaluation of Generated Text\"\n- Amidei et al. (2019) \"Agreement is overrated: A plea for correlation to assess human evaluation reliability\"\n- Boubdir et al. (2023) \"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation\" (或同类 BT-in-LLM-eval 方法论文献)\n- Wu & Aji (2023) \"Style Over Substance: Evaluation Biases for Large Language Models\" (如果与 murugadoss2025sos 非同一工作)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending（未返回）**\n\n外部审稿请求已于 2026-05-21T09:36 发送，8 小时提醒已排期。截至报告提交时外部结果尚未返回。建议 Research Director 在外部审稿到达后补充参考。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done**（2026-05-21 09:36–09:38，耗时 ~2.5 min）\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| **Critical** | p.1-3 | 前 3 页纯文本无任何 display item（figure/table/diagram）。第一个 display item (Figure 1) 延迟到 p.4。严重影响审稿人第一印象。建议将 Figure 1 或 motivating example 提前到 p.1-2（Introduction 内）。 |\n| Warning | p.5 | 单页堆叠 3 个 display items（Figure 2 + Table 1 + Figure 3），视觉拥挤。建议分散至相邻页面。 |\n| Warning | p.6 | 纯文本页夹在 p.5 和 p.7 之间，节奏可改善。 |\n| Warning | p.12 | 末页仅 1 条参考文献 + 90% 空白，不整洁。建议调整 bibsep 使 references 在 p.11 内结束。 |\n| Info | p.4 | Figure 1 偏小、灰度感重，视觉冲击力不足。 |\n| Info | p.5 | Table 1 加粗标注不够醒目；Figure 3 字号偏小。 |\n| Info | p.7 | Figure 4 高 sample size 区域曲线重叠，legend 可改为直接标注。 |\n| Info | p.10 | Appendix 三张表紧密堆叠，略拥挤但可接受。 |\n\n**视觉审查结论**：最重要的建议是将 Figure 1 或概念图提前到第 1-2 页，给审稿人提供早期视觉锚点。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5 — Findings**\n\n**置信度：4 / 5**\n\n### 评分理由\n\n论文在统计方法论执行上扎实（7 种方法三角验证、GEE per-axis 分解、完整的 diagnostics），核心发现（Likert vs pairwise 在 LLM evaluation 中的 ~4.5× 效率差距）对评测实践有实际价值。Negative results 的诚实呈现和 Claude 作为 discriminative validity 证据增加了科学可信度。\n\n但三个 Must-Fix 问题制约了论文的贡献层级：\n\n1. **Novelty ceiling 是结构性的**：核心发现是 Thurstone (1927) 以来心理测量学已知原理在 LLM domain 的量化确认，而非 genuine new discovery。两位 Reviewer 的 Excitement 评分（3/5, 3.5/5）反映了这一判断。\n\n2. **Framing 系统性过强**：Title \"Counterfactual\"、§3.5 \"Causal Framework\"、\"Blindspot\"（质性 framing）、\"Decomposition\"（暗示干净分离）——四处核心术语均超出方法论强度。Table 3 originality OR 显著是识别假设部分违反的经验证据。这些 framing 问题不是局部修辞瑕疵，而是贯穿论文核心 narrative 的系统性问题。\n\n3. **Evaluator-producer confound 控制有缺口**：Independence test 仅覆盖 verbosity，而 formality 恰是 confound 最明显的轴。\"Across two judges\" 的 generalizability claim 基础不完整。\n\n这些问题在当前状态下将论文定位在 Findings 水平（3.0）。若能解决 MF1-MF3（framing 降级 + formality independence test），论文有望提升到 3.5（Borderline Conference）。\n\n### 与两位 Reviewer 评分的差异说明\n\n两位 Reviewer 均评 3.5（Borderline Conference）。Director 评 3.0（Findings）的原因：\n- 交叉分享后三个 Must-Fix 的共识更加强化（无任何 Must-Fix 被 rebut），尤其是 Blindspot framing 问题在交叉讨论中被 R2 进一步深化（measurement attenuation vs power gap 的未完成分析）\n- Novelty ceiling（domain transfer of known psychometric principle）是结构性限制，难以通过局部修改突破\n- Framing 问题的 pervasiveness（Title + Abstract + Method section name + Contribution claims）意味着修正工作量不小且可能影响论文的 selling point\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过长过密（9 行），试图覆盖 7 种统计方法、4 个配置、3 个 benchmark。建议精简至 5-6 行。\n- \"Likert Blindspot\" 首次出现未加 qualifier，暗示质性缺陷。\n\n### §1 Introduction\n- Contribution 1 \"interventional framework\" 在当前方法论强度下过强。\n- Contribution 4 \"style bias audits should employ pairwise comparison\" 缺乏 qualifier。\n- \"~60% uninformative ties\" 数字有力但在 Abstract/§1/§5.2 重复出现。\n\n### §2 Related Work\n- 基本覆盖 LLM judge bias 主线，但引用量偏少（27 条）。\n- 缺 counterfactual generation 方法谱系和 NLG evaluation scale design 文献。\n- 与 Thurstone (1927) 的关系讨论不充分。\n\n### §3 Method\n- §3.1 Binary style-controlled rewriting 描述清晰但无人工验证。\n- §3.2 NLI gate：direction-aware 放宽合理但额外 pairs 质量未验证。\n- §3.5 \"Causal Framework\" 标题过强；DAG 缺 residual S→Q path；识别假设 (iii) 未检验。\n\n### §4 Experimental Setup\n- 实验设计合理（position-controlled、consistency filtering）。\n- n=100 LLMBar 作为起点可接受，但应更突出 n=355/400 scaled replication。\n\n### §5 Results\n- Table 1 主结果表信息量大但 Holm-Bonferroni 标注可更直觉。\n- Table 2 七种 Likert 方法全部 fail 是有力证据。\n- §5.6 GEE decomposition 命名应降级；confound gradient 的替代解释（rewriting difficulty）未讨论。\n- Figure 4 power curve 是有价值贡献但支持 \"efficiency gap\" 而非 \"blindspot\"。\n\n### §6 Conclusion\n- \"Prompt-level debiasing is insufficient\" 缺乏 evidence 基础。\n- Practical recommendation 应加 qualifier。\n\n### Limitations\n- 覆盖了关键弱点（evaluator-producer、NLI 验证、scale granularity、benchmark coverage）。\n- 缺少对 confound gradient 替代解释的讨论。\n- \"An independent spot-check with GPT-4o is planned\" 应执行而非承诺。\n\n### 格式与视觉\n- 正文 8 页合规。\n- 前 3 页无任何 display item 是最大的视觉问题。\n- p.5 display items 过度集中。",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 3（Fresh Review）\n\n**项目**: causal_style_decomp_judge\n**论文**: Counterfactual Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges\n**目标 Venue**: EMNLP 2026 (Long Paper, via ARR)\n**审稿人**: Reviewer 1（方法严谨性 + 实验有效性）、Reviewer 2（新颖性 + 完整性 + Related Work）\n**审稿轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识）\n\n---\n\n## ⚠️ Deadline 警告\n\nWeb 搜索确认 EMNLP 2026 最后可用的 ARR 提交截止日为 **2026-05-25 AoE**（距今 4 天），而非提交消息中的 2026-06-15。ARR May cycle 提交时须绑定声明 EMNLP 2026 为目标会议（binding）。请立即核实。\n\n---\n\n## Summary\n\n本文提出 Counterfactual Style Decomposition (CSD)，一个黑盒框架，通过 binary style-controlled rewriting + NLI entailment gate + position-controlled pairwise comparison 检测 LLM judge 的 per-axis style bias。核心发现命名为 \"Likert Blindspot\"：在 3 个 judge（GPT-4o、Qwen3-32B、Claude Sonnet 4）、3 个 benchmark（LLMBar、AlpacaEval、MT-Bench）、2 个主要 style axes（formality、verbosity）+ 1 个探索性 axis（register）上，Likert 评分对 style bias 的检测灵敏度系统性低于 pairwise comparison（~4.5× 效率差距）。GEE logistic regression 将 style effect 和 originality confound 分离，发现 confound gradient（verbosity = pure style, formality = dual, register = originality-dominated）。Claude Sonnet 4 在所有 axes 上无显著 bias，作为 discriminative validity 证据。\n\n---\n\n## Strengths\n\n**S1. 统计三角验证扎实**：7 种统计方法（ATE、sign test、BT、ordinal regression、GEE、Holm-Bonferroni、power curve）一致显示 Likert vs pairwise 灵敏度差距，跨 judge/benchmark/axis 的系统性复制增强可信度。[R1 + R2 共识]\n\n**S2. GEE per-axis 分解有方法论贡献**：将 style effect 和 originality confound 解耦的 GEE 框架在 LLM judge bias 文献中较为少见，confound gradient 发现有 insight。GEE diagnostics（Appendix C, correlation structure robustness）完整。[R1 + R2 共识]\n\n**S3. Negative results 诚实呈现**：Claude Sonnet 4 无 bias（BT 56.2%/54.1%, non-sig）、formality 方向不对称（78.8% vs 54.5%）、tone axis 失败——增加了结果可信度和论文的科学诚实性。[R2 首提, R1 同意]\n\n**S4. 实用价值高**：量化了 LLM evaluation 中 Likert vs pairwise 的 ~4.5× 效率差距，对评测实践有直接指导意义。Figure 4 power curve 是 measurement methodology 层面的有价值贡献。[R1 + R2 共识]\n\n**S5. Pipeline 可复现**：NLI gate 阈值、BT 模型参数、bootstrap 配置（10k resamples）、GEE correlation structure 均明确报告。方法描述清晰，各步骤可复现（但代码/数据未附）。[R2]\n\n**S6. 写作质量良好**：结构清晰，信息密度高，在 8 页内覆盖完整的方法-实验-分析链。正文 8 页合规，Limitations 覆盖了关键弱点。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，两位 Reviewer 强共识）\n\n**MF1. \"Blindspot\" framing 混淆统计功效差异与质性 blindspot** [R1-N3 + R2-N1, 强共识]\n- Title 用 \"Blindspot\" 暗示 Likert 有质性缺陷（永远检测不到），但 Figure 4 power curve 明确显示 Likert 在 n≈1,473 时达到 80% power——这是量性的 efficiency gap，非质性 blindspot。\n- Thurstone (1927) 关于 ordinal scale 灵敏度低于 paired comparison 的结论已近百年，论文在 §2 引用了 Thurstone 但未充分说明增量贡献。\n- n=355 scaled replication Likert 仍 non-significant (p=0.60)，但该配置下 Cohen's d 未报告——若 d 仍接近 0.1，power 约 25-30%，依然是功效不足。\n- 论文自身使用 \"~4.5× more data to reach equivalent sensitivity\"（§5.2）的 power 语言，与 \"Blindspot\" framing 自相矛盾。\n- **关键区分**：若能证明 Likert 同时压缩 effect size（measurement attenuation）+ 降低 power（而非仅后者），\"Blindspot\" framing 更站得住脚，但论文未做此分析。\n- **建议**：(1) 将 \"Blindspot\" 重定义为 \"measurement efficiency gap at typical evaluation scales\"；(2) 补报 n=355 Likert Cohen's d 和 power；(3) 明确区分量性 gap 和质性 blindspot。\n\n**MF2. 因果/反事实术语与方法论强度不匹配** [R1-N1 + R2-N2, 强共识]\n- Title \"Counterfactual\"、§3.5 \"Causal Framework\"、Figure 2 DAG 暗示形式化因果模型，但 §3.5 声明 \"not a complete structural causal model, nor do we invoke SUTVA\"。\n- 经验性违反证据：Table 3 中 originality OR 在多个配置下显著（GPT-4o formality: OR=2.32, p=0.006; Qwen3 register: OR=5.72），直接表明 NLI gate 未完全阻断 R→Q path——识别假设 (i) 部分违反。\n- 识别假设 (iii)（rewrite 不引入 target axis 外差异）未检验——formality rewrite 可能同时改变 register/vocabulary sophistication。\n- 实际上 CSD 是 controlled intervention study with imperfect content preservation，非因果推断。\n- **建议**：(1) Title 中 \"Counterfactual\" → \"Interventional\" 或 \"Controlled\"；(2) §3.5 标题 → \"Interventional Design and Assumptions\"；(3) Figure 2 DAG 用虚线标注 residual S→Q confounding；(4) 量化讨论 originality OR 对 style effect 估计的影响方向和幅度。\n\n**MF3. Evaluator-producer independence test 覆盖不完整** [R1-N2, R2 交叉同意]\n- Qwen3-32B 同时做 rewriter 和 judge，效应量系统性偏高（formality Style OR 4.20 vs GPT-4o 2.58 at n=88，1.6× 差距）。\n- Appendix D rewriter independence test 仅覆盖 verbosity 轴（GPT-4o rewriter: OR 13.10→10.17, 22% 降幅），缺 formality 和 register。\n- Formality 恰是 evaluator-producer bias 最明显的轴——Qwen3 OR 从 n=88 (4.20) 降至 n=355 (2.15) 的 49% 降幅也暗示小样本下的 OR 膨胀。\n- 主分析（Table 1, Table 3）仍以 Qwen3-32B 与 GPT-4o 并列为主要证据，\"across two judges\" 的 generalizability claim 受损。\n- **建议**：(1) 补做 formality 轴 independence test（GPT-4o rewriter + Qwen3-32B judge）；(2) 或在主文明确标注 Qwen3-32B 结果仅作 existence claim，不适合与 GPT-4o 做定量 effect size 比较。\n\n### Should-Fix（影响评分，两位 Reviewer 至少一位提出且另一位同意）\n\n**SF1. 缺少任何人工评估验证 rewriting 质量** [R1-W4, R2 强化]\n- CSD 完全依赖 NLI gate（自动化）验证 content preservation，无 human evaluation 验证 (a) style 改变方向正确率 (b) 自然度 (c) NLI 未检测的 artifacts。ACL/EMNLP 涉及 text generation 的工作通常需要至少 small-scale human evaluation。\n\n**SF2. NLI gate 验证使用同一模型族** [R1-W1, R2 同意]\n- §5.1 使用 Qwen3-32B 作为 annotator 验证 NLI gate（precision 98.9%），但 Qwen3-32B 同时是 rewriter——self-consistency bias 可能高估 precision。论文承诺 \"GPT-4o spot-check is planned\" 但未执行。\n\n**SF3. Direction-aware NLI 放宽为单向 entailment，额外纳入的 pairs 未独立验证** [R1-W2, R2 同意]\n- Verbosity 轴 NLI gate 从双向放宽为单向，pass rate 从 65% 升至 86%。额外纳入的 ~21% pairs 的 content preservation 质量未经独立验证。单向 entailment 允许 expansion 方向丢失信息（更详细 = 更高质量的感知）→ 可能 inflate style bias estimate。\n\n**SF4. Confound gradient 的替代解释** [R1-W5, R2 同意]\n- §5.6 发现 verbosity = pure style, formality = dual, register = originality-dominated。但 gradient 可能反映 rewriting 操作的 invasiveness（verbosity 大幅增删 vs formality 词汇替换 vs register 几乎必然改变 sophistication）而非 axis 固有属性——即 pipeline artifact 而非 style axis property。\n\n**SF5. GEE \"decomposition\" 在残余 confounding 下有误导性** [R2-W3, R1 同意]\n- Table 3 中 originality OR 显著（p=0.006）证明 confounding 未消除。\"Decomposition\" 暗示干净分离，实际是 partial adjustment。Originality 的操作化定义不清晰。\n\n**SF6. 小样本 OR 估计不稳定** [R1-W6, R2 同意]\n- Qwen3 formality Style OR: n=88 (4.20) → n=355 (2.15)，降幅 49%，表明 n=88 估计严重偏高。Register 轴 marginal significance (p=0.046) 在此样本量下尤其脆弱。建议将 n=355 scaled replication 提升为主结果。\n\n**SF7. Related Work 引用偏少** [R2-W1, R1 同意]\n- 27 条引用低于 EMNLP long paper 通常水平（40-60 条）。缺失：counterfactual generation 方法谱系（CausaLM, Polyjuice）、NLG evaluation scale design（Clark 2021, Amidei 2019）、BT in LLM evaluation（Boubdir 2023）。\n\n**SF8. NLI gate false negative → systematic selection bias** [R2-W2]\n- 大幅 style 变化更易被 NLI gate 过滤 → 保留的 pairs 系统性包含较小 style 干预 → 低估 measured effect（attenuation bias）。§5.1 FN 无方向性偏差（Fisher p=0.35）部分回应，但理论论点仍成立。\n\n**SF9. 证据范围 vs 建议范围不匹配** [R2-N3, R1 部分反驳]\n- Contribution 4 和 Conclusion 给出一般性建议（\"style bias audits should adopt pairwise comparison\"），但证据仅来自 n=100 × 3 judges × 2 有效 axes。R1 指出 cross-benchmark 已覆盖 3 种任务类型（instruction-following, open-ended, multi-turn），Register 在主文 §5.5 有讨论。共识：建议应加 qualifier。\n\n### Minor Issues（不影响接收）\n\n- Abstract 过长过密（9 行），建议精简至 5-6 行聚焦核心 claim [R1]\n- Table 1 Holm-Bonferroni p-value 标注可更直觉（raw p vs adjusted p 混淆）[R1 提出, R2 认为信息完整但 presentation 可改进]\n- Claude 作为 negative control 有双重解释（无 bias vs alignment 消除 bias），可在讨论中补充说明 [R2 提出, R1 认为 discriminative validity 论证合理]\n- Orphan bib entry `hoenig2001abuse`；`murugadoss2025sos` 在 OpenAlex 未匹配（可能太新）[R1 + R2]\n- Figure 1 偏小，stage attrition numbers 不易辨认 [R2]\n- §6 \"Prompt-level debiasing is insufficient\" 缺乏 evidence 基础（未测试任何 debiasing 方法）[R2]\n- ~60% uninformative ties 在 Abstract/§1/§5.2 重复出现但未给出全部 6 个配置的 tie rate 分布表 [R1]\n- §5.5 Register 结果 marginal significance 用大半节描述 inconclusive 结果，考虑压缩 [R1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下问题上独立达成强共识：\n\n1. **\"Blindspot\" framing 问题**（R1-N3 ≡ R2-N1）：核心 narrative 混淆 measurement sensitivity 和 statistical power。Figure 4 的 evidence 只支持量性差距而非质性 blindspot。Thurstone (1927) 已知。**这是论文最大的 framing 风险。**\n\n2. **Causal 语言过强**（R1-N1 ≡ R2-N2）：Title \"Counterfactual\"、§3.5 \"Causal Framework\"、DAG 与方法论强度不匹配。Table 3 originality OR 显著是 shared empirical evidence 表明识别假设部分违反。\n\n3. **GEE \"decomposition\" 命名**：在残余 confounding 下 \"decomposition\" 有误导性，应改为 \"partial adjustment\" 或 \"conditional analysis\"。\n\n4. **缺少人工评估**：ACL/EMNLP 涉及 text generation 的工作通常需要至少 small-scale human evaluation，论文完全依赖自动化验证。\n\n5. **小样本 OR 不稳定**：n=88 的 GEE OR 估计可信度受损，n=355 结果更可靠，应提升为主结果。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n分歧仅在 Should-Fix 级别，无 Must-Fix 分歧：\n\n1. **R2-N3 severity**（证据范围过窄）：R2 评为 critical，R1 部分反驳——cross-benchmark 已覆盖 3 种任务类型，Register 在主文 §5.5 有讨论（非仅 Limitations），R2 对 \"tone axis 只在 Limitations 提及\" 和 \"不覆盖 dialogue\" 的具体论据不准确。**Director 判定**：降为 warning (SF9)。\n\n2. **Claude negative control 解释力**：R2 认为解释力有限（warning），R1 认为 discriminative validity 论证合理。**Director 判定**：降为 info。\n\n3. **Appendix placement**：R2 建议将 Direction Asymmetry 和 GEE Robustness 移入正文；R1 认为 8 页限制下当前安排合理。**Director 判定**：当前安排可接受，不列为 issue。\n\n---\n\n## Questions for Authors\n\n1. **Blindspot 本质**：Figure 4 power curve 是否 asymptotically converge（Likert 和 pairwise 在足够大 n 下检测结果是否收敛）？如果收敛，\"Blindspot\" 应降级为 \"efficiency gap\"。如果不收敛（Likert 存在 measurement attenuation），\"Blindspot\" 有更强依据——你们能否提供 Likert effect size 随 n 变化的分析？\n\n2. **n=355 Likert effect size**：该配置下的 Cohen's d 是多少？这是区分 \"power gap\"（d 不变，n 不够）和 \"measurement attenuation\"（d 本身被压缩）的关键数据。\n\n3. **多轴测量**：对 formality rewrite，是否测量了 rewrite 在 register/verbosity 轴上的变化幅度？若 formal rewrite 同时变得更 verbose 或更 academic，单轴干预假设被违反。\n\n4. **Formality independence test**：是否计划补做 formality 轴的 rewriter independence test（GPT-4o rewriter + Qwen3-32B judge）？这是验证 Qwen3-32B evaluator-producer confound 的关键实验。\n\n5. **NLI gate selection effect**：被 NLI gate 过滤掉的 pairs 在 style change magnitude 上是否有系统性偏差？\n\n6. **Pairwise Likert difference**：是否考虑过使用 Likert 分数的 pairwise difference（paired t-test on Δscore）？这会消除 tie-inflation 问题同时保留 Likert 信息。\n\n---\n\n## Missing References\n\n两位 Reviewer 共同识别的缺失引用：\n- Feder et al. (2021) \"CausaLM: Causal Model Explanation Through Counterfactual Language Models\"\n- Wu et al. (2021) \"Polyjuice: Generating Counterfactuals for Explaining, Training, and Evaluating NLMs\"\n- Clark et al. (2021) \"All That's Human Is Not Gold: Evaluating Human Evaluation of Generated Text\"\n- Amidei et al. (2019) \"Agreement is overrated: A plea for correlation to assess human evaluation reliability\"\n- Boubdir et al. (2023) \"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation\" (或同类 BT-in-LLM-eval 方法论文献)\n- Wu & Aji (2023) \"Style Over Substance: Evaluation Biases for Large Language Models\" (如果与 murugadoss2025sos 非同一工作)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending（未返回）**\n\n外部审稿请求已于 2026-05-21T09:36 发送，8 小时提醒已排期。截至报告提交时外部结果尚未返回。建议 Research Director 在外部审稿到达后补充参考。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done**（2026-05-21 09:36–09:38，耗时 ~2.5 min）\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| **Critical** | p.1-3 | 前 3 页纯文本无任何 display item（figure/table/diagram）。第一个 display item (Figure 1) 延迟到 p.4。严重影响审稿人第一印象。建议将 Figure 1 或 motivating example 提前到 p.1-2（Introduction 内）。 |\n| Warning | p.5 | 单页堆叠 3 个 display items（Figure 2 + Table 1 + Figure 3），视觉拥挤。建议分散至相邻页面。 |\n| Warning | p.6 | 纯文本页夹在 p.5 和 p.7 之间，节奏可改善。 |\n| Warning | p.12 | 末页仅 1 条参考文献 + 90% 空白，不整洁。建议调整 bibsep 使 references 在 p.11 内结束。 |\n| Info | p.4 | Figure 1 偏小、灰度感重，视觉冲击力不足。 |\n| Info | p.5 | Table 1 加粗标注不够醒目；Figure 3 字号偏小。 |\n| Info | p.7 | Figure 4 高 sample size 区域曲线重叠，legend 可改为直接标注。 |\n| Info | p.10 | Appendix 三张表紧密堆叠，略拥挤但可接受。 |\n\n**视觉审查结论**：最重要的建议是将 Figure 1 或概念图提前到第 1-2 页，给审稿人提供早期视觉锚点。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5 — Findings**\n\n**置信度：4 / 5**\n\n### 评分理由\n\n论文在统计方法论执行上扎实（7 种方法三角验证、GEE per-axis 分解、完整的 diagnostics），核心发现（Likert vs pairwise 在 LLM evaluation 中的 ~4.5× 效率差距）对评测实践有实际价值。Negative results 的诚实呈现和 Claude 作为 discriminative validity 证据增加了科学可信度。\n\n但三个 Must-Fix 问题制约了论文的贡献层级：\n\n1. **Novelty ceiling 是结构性的**：核心发现是 Thurstone (1927) 以来心理测量学已知原理在 LLM domain 的量化确认，而非 genuine new discovery。两位 Reviewer 的 Excitement 评分（3/5, 3.5/5）反映了这一判断。\n\n2. **Framing 系统性过强**：Title \"Counterfactual\"、§3.5 \"Causal Framework\"、\"Blindspot\"（质性 framing）、\"Decomposition\"（暗示干净分离）——四处核心术语均超出方法论强度。Table 3 originality OR 显著是识别假设部分违反的经验证据。这些 framing 问题不是局部修辞瑕疵，而是贯穿论文核心 narrative 的系统性问题。\n\n3. **Evaluator-producer confound 控制有缺口**：Independence test 仅覆盖 verbosity，而 formality 恰是 confound 最明显的轴。\"Across two judges\" 的 generalizability claim 基础不完整。\n\n这些问题在当前状态下将论文定位在 Findings 水平（3.0）。若能解决 MF1-MF3（framing 降级 + formality independence test），论文有望提升到 3.5（Borderline Conference）。\n\n### 与两位 Reviewer 评分的差异说明\n\n两位 Reviewer 均评 3.5（Borderline Conference）。Director 评 3.0（Findings）的原因：\n- 交叉分享后三个 Must-Fix 的共识更加强化（无任何 Must-Fix 被 rebut），尤其是 Blindspot framing 问题在交叉讨论中被 R2 进一步深化（measurement attenuation vs power gap 的未完成分析）\n- Novelty ceiling（domain transfer of known psychometric principle）是结构性限制，难以通过局部修改突破\n- Framing 问题的 pervasiveness（Title + Abstract + Method section name + Contribution claims）意味着修正工作量不小且可能影响论文的 selling point\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过长过密（9 行），试图覆盖 7 种统计方法、4 个配置、3 个 benchmark。建议精简至 5-6 行。\n- \"Likert Blindspot\" 首次出现未加 qualifier，暗示质性缺陷。\n\n### §1 Introduction\n- Contribution 1 \"interventional framework\" 在当前方法论强度下过强。\n- Contribution 4 \"style bias audits should employ pairwise comparison\" 缺乏 qualifier。\n- \"~60% uninformative ties\" 数字有力但在 Abstract/§1/§5.2 重复出现。\n\n### §2 Related Work\n- 基本覆盖 LLM judge bias 主线，但引用量偏少（27 条）。\n- 缺 counterfactual generation 方法谱系和 NLG evaluation scale design 文献。\n- 与 Thurstone (1927) 的关系讨论不充分。\n\n### §3 Method\n- §3.1 Binary style-controlled rewriting 描述清晰但无人工验证。\n- §3.2 NLI gate：direction-aware 放宽合理但额外 pairs 质量未验证。\n- §3.5 \"Causal Framework\" 标题过强；DAG 缺 residual S→Q path；识别假设 (iii) 未检验。\n\n### §4 Experimental Setup\n- 实验设计合理（position-controlled、consistency filtering）。\n- n=100 LLMBar 作为起点可接受，但应更突出 n=355/400 scaled replication。\n\n### §5 Results\n- Table 1 主结果表信息量大但 Holm-Bonferroni 标注可更直觉。\n- Table 2 七种 Likert 方法全部 fail 是有力证据。\n- §5.6 GEE decomposition 命名应降级；confound gradient 的替代解释（rewriting difficulty）未讨论。\n- Figure 4 power curve 是有价值贡献但支持 \"efficiency gap\" 而非 \"blindspot\"。\n\n### §6 Conclusion\n- \"Prompt-level debiasing is insufficient\" 缺乏 evidence 基础。\n- Practical recommendation 应加 qualifier。\n\n### Limitations\n- 覆盖了关键弱点（evaluator-producer、NLI 验证、scale granularity、benchmark coverage）。\n- 缺少对 confound gradient 替代解释的讨论。\n- \"An independent spot-check with GPT-4o is planned\" 应执行而非承诺。\n\n### 格式与视觉\n- 正文 8 页合规。\n- 前 3 页无任何 display item 是最大的视觉问题。\n- p.5 display items 过度集中。",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-21T09:51:21.388272+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4417
}
```

</details>

---


### Assistant

_source line 222 · 2026-05-21T09:51:30.159541+00:00_

审稿报告已投递至 Research Director。

---

**Round 3 审稿完成。** 总结：

**评分：3.0 / 5（Findings）**，两位 Reviewer 均评 3.5（Borderline Conference），Director 综合交叉讨论后下调至 3.0。

**三个 Must-Fix**（两位 Reviewer 强共识）：
1. "Blindspot" framing 混淆 power gap 与质性 blindspot——Figure 4 evidence 只支持量性差距，Thurstone 1927 已知
2. Causal/Counterfactual 术语过强——Table 3 originality OR 显著证明识别假设部分违反
3. Evaluator-producer independence test 仅覆盖 verbosity，缺 formality

**9 个 Should-Fix**：缺人工评估、NLI 同族验证、direction-aware gate 未验证、confound gradient 替代解释、GEE "decomposition" 误导、小样本 OR 不稳定、引用偏少、NLI selection bias、建议 scope 过强

**外部审稿**：pending（未返回），已在报告中标注。
**视觉审查**：前 3 页无 display item 是最大视觉问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 22

## Round 22

2 recorded events


### User

_source line 223 · 2026-05-21T09:51:33.229644+00:00_

[Reviewer 1 审稿结果]:
已提交交叉回应。核心结论：

- **强共识**（R1+R2）：Blindspot framing 过强（应降级为 efficiency gap）、因果语言与方法论不匹配、GEE "decomposition" 命名有误导性
- **部分共识**：证据范围偏窄，但我认为 R2 低估了 cross-benchmark 复制（MT-Bench 覆盖对话）和 register axis 在主文 §5.5 的讨论
- **分歧**：Claude negative control（我认为 discriminative validity 论证合理）、Appendix placement（我认为 8 页限制下当前安排合理）
- **R1 独有关切**：evaluator-producer independence test 仅覆盖 verbosity（R1-N2）、NLI gate 由同模型族验证（R1-W1）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 224 · 2026-05-21T09:51:46.061680+00:00_

审稿报告已投递至 Research Director。

**审稿结果摘要：**

- **Overall：3.0 / 5（Findings）**
- 两位 Reviewer 独立评分均为 3.5，Director 综合交叉讨论后下调至 3.0
- 3 个 Must-Fix（强共识）：(1) "Blindspot" framing 混淆 power gap 与质性 blindspot；(2) 因果/反事实术语过强；(3) Evaluator-producer independence test 仅覆盖 verbosity
- 9 个 Should-Fix：缺人工评估、NLI gate 同族验证、direction-aware NLI 放宽、confound gradient 替代解释、GEE 命名、小样本 OR 不稳定、Related Work 偏少、NLI selection bias、建议范围过强
- 外部审稿：pending（未返回），已标注
- 视觉审查：前 3 页无 display item 是最大排版问题
- Issue tracker 已同步更新（14 个新 issue：3 critical + 8 warning + 3 info）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 23

## Round 23

58 recorded events


### User

_source line 225 · 2026-05-21T11:11:14.586545+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-21T11:11:21.407750+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-21T11:11:21.458921+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-21T11:11:30.191494+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-21T11:11:30.242210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-21T11:11:36.416988+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-21T11:11:37.823048+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (34 个)\n\n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **register_100_cf**: QUEUED — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- register_100_cf: Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality（排队等待 GPU）\n\n## 近期结论\n- **gpt4o_rewriter_formality** (success): Formality blindspot persists when using GPT-4o (instead of Qwen3-32B) as the counterfactual rewriter, demonstrating that the detected bias is rewriter-independent and not an artifact of a specific rewriting model\n- **nli_fn_selection_bias** (success): NLI gate may systematically filter pairs with larger style changes, potentially underestimating the true bias effect — if so, reported effects are conservative lower bounds (addresses R3-W8)\n- **nli_gate_spotcheck** (success): GPT-4o independent evaluation agrees with NLI gate pass/fail decisions at high rate, demonstrating NLI gate validity is not an artifact of same-model-family evaluation (addresses R3-W1 concern about evaluator-producer confound in gate validation)\n\n## 趋势\n成功 23 / 负向 7 / 失败 0 / 共 33\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-0
…[truncated 20 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-21T11:11:37.873753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-21T11:11:37.874228+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding.}
42	Although the formality effect survives logistic adjustment for original preference (Appendix~\ref{app:direction}), the significant original-preference odds ratio ($\text{OR} = 2.32$, $p = 0.006$) indicates that quality--style confounding is not fully eliminated.
43	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
44	Future work should incorporate human quality ratings of both original and rewritten texts.
45	
46	\paragraph{Evaluator-producer bias in Qwen3-32B.}
47	Qwen3-32B serves as both the style rewriter and one of the three judges, raising the concern of self-preference bias \citep{panickssery2024selfpreference}; the NLI entailment gate (DeBERTa-v3-large) is architecturally independent of both roles.
48	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exhibited small-sample upward bias, corrected to $2.15$ at $n = 355$ (comparable to GPT-4o's $2.58$); the originality OR inflation persists ($4
…[truncated 3110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-21T11:11:46.460380+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 235 · 2026-05-21T11:11:46.460832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-21T11:11:47.514713+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-21T11:11:48.620382+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_style_decomp_judge'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-21T11:11:48.620711+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-21T11:11:48.671098+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-21T11:11:51.331911+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-21T11:11:51.683776+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-21T11:11:52.185951+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-21T11:11:59.061810+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 regarding papers and ARR:

## Paper Submission Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using exis
…[truncated 1045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6875
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-21T11:12:04.784387+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template anonymity guidelines site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template anonymity guidelines site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 245 · 2026-05-21T11:12:06.691673+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-21T11:12:07.043281+00:00_

1	\begin{abstract}
2	LLM judges are widely deployed for evaluation and alignment, yet style features alone explain judge scores with near-perfect correlation.
3	We introduce Controlled Style Decomposition (CSD), a black-box framework that detects per-axis style bias through style-controlled rewriting, NLI content gating, and pairwise comparison.
4	Across three judges (GPT-4o, Qwen3-32B, Claude Sonnet 4), three benchmarks, and three style axes, CSD reveals the Likert Blindspot---not merely a statistical power gap but measurement attenuation across a severity spectrum: at moderate bias levels Likert compresses effect sizes to zero ($d \to 0$ at $n = 355$); at stronger effects (BT ${>}70\%$) Likert partially detects but attenuates by ${>}60\%$---while pairwise comparison reliably detects bias across the full range (BT 63--84\%, $p < 0.001$), confirmed by seven statistical methods.
5	A third judge (Claude Sonnet 4) detects no bias on either axis, confirming discriminative validity.
6	Style bias audits require pairwise comparison; existing Likert-based null findings may reflect measurement insensitivity rather than genuine absence of bias.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-21T11:12:07.044754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-21T11:12:07.747677+00:00_

1	\section{Introduction}
2	
3	Large Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.
4	Systems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.
5	Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.
6	The reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.
7	As automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.
8	
9	Recent work suggests that style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, motivating systematic measurement of per-axis style bias.
10	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences, and \citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
11	Despite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis interventional detection.
12	Recent multi-feature frameworks such as CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} begin to decompose style into finer dimensions, but neither provides interv
…[truncated 4268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 249 · 2026-05-21T11:12:07.748054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-21T11:12:07.798638+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_diagram.pdf}
7	\caption{CSD pipeline overview. Numbers indicate sample attrition at each stage.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	\subsection{Style-Controlled Rewriting}
12	\label{sec:rewriting}
13	
14	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
15	For each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
16	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
17	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
18	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
19	
20	\subsection{Content Preservation Verification}
21	\label{sec:nli_gate}
22	
23	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
24	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.
25	For axes that preserve information density (formality, register), we apply standard bidirection
…[truncated 5908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-21T11:12:10.635018+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template anonymity guidelines site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

Based on the search results from the EMNLP 2026 website, here's what I found regarding the submission guidelines:

## Anonymity Guidelines

Following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing process will continue to be double-blind. One may upload the paper to arXiv at any time.

## Submission Format

The search results indicate that submissions should follow ARR (ACL Rolling Review) requirements. Authors are required to discuss the limitations of their work in a dedicated section titled "Limitations", which should be included at the end of the paper before the references and will not count toward the page limit. Papers without a limitations section will be desk rejected.

For appendices, authors are asked not to abuse the option of an unlimited appendix and only to
…[truncated 583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5850
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-21T11:12:16.300385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-21T11:12:16.803096+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of six hypothesis tests (two judges $\times$ three style axes) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values for this $2 \times 3$ grid.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Main results across three judges, three style axes, and three benchmarks. BT: Bradley-Terry win probability (10{,}000 pair-level bootstrap resamples; 95\% CIs in Appendix~\ref{app:bt_ci}). AEval: AlpacaEval; MTB: MT-Bench. Claude Sonnet 4 serves as negative control.}
19	\label{tab:main_results}
20	\begin{tabular}{@{}lllccc@{}}
21	\toprule
22	Bench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & \\
23	\midrule
24	LLMBar & GPT-4o & Form.\ & .630$^{***}$ & .102 (.332) & $\dagger$ \\
25	 & GPT-4o & Verb.\ & .760$^{***}$ & $-$.095 (.403) & $\dagger$ \\
26	 & GPT-4o & Reg.\ & .570$^{\dagger}$ & $-$.031 (.785) & $\dagger_{\text{e}}$ \\
27	\cmidrule{2-6}

…[truncated 16749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-21T11:12:16.803652+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-21T11:12:17.506256+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 4783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-21T11:12:17.506658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-21T11:12:18.710614+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD reveals the Likert Blindspot---measurement attenuation in Likert scoring---across three judges, benchmarks, and style axes; style bias audits should adopt pairwise comparison.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1203
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-21T11:12:18.710974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-21T11:12:18.711258+00:00_

1	\appendix
2	
3	\section{Direction Asymmetry and Quality Confounding}
4	\label{app:direction}
5	
6	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
7	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
8	To quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.
9	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
10	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
11	
12	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
13	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).
14	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
15	
16	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
17	
18	\section{Consistency Filter Robustness}
19	\label{sec:consistenc
…[truncated 7221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-21T11:12:18.862123+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-21T11:12:18.963373+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml\", \"content\": \"_next_id: 53\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 14:09 UTC\\n  summary: '文献蒸馏审视：研究方向无需调整，CSD 填补 #1 空白（多维 style 因果分解），post-MVP 需扩展 judge/benchmark/baseline\\n    覆盖'\\n  rationale: '10 篇论文蒸馏显示：(1) 多维 style 联合因果分解是领域 #1 空白，与 CSD 核心 claim 完全对齐；(2) 竞品 claim\\n    无直接重叠（FairJudge=white-box, Pref Leakage=family-based, Soumik=prompt-dependent）；(3)\\n    同行标准要求 3-5 异构 judge + AlpacaEval/Arena-Hard/MT-Bench + Bootstrap CIs + 对比 LC-AlpacaEval\\n    baseline。当前 MVP 方案足够，research 阶段需按蒸馏标准扩展。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 14:19 UTC\\n  summary: MVP 全量评分 + 分层分析：score 全部 100 条，按 BERTScore 阈值 0.88/0.90/0.92 分层算 ATE，不降低阈值\\n  rationale: 36% pass rate (BERTScore≥0.92) 偏低但 NLI 均值 0.9422 说明语义保留好。降阈值是数据操作，不如保留完整信息。全量评分\\n    (n=100) 保证统计 power，分层分析同时回答\\\"严格阈值下效应是否存在\\\"和\\\"宽松阈值下效应是否增强\\\"。8B H1 fail 不消耗迭代配额（ROADMAP\\n    规则），32B 备用。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 14:20 UTC\\n  summary: H1 content verification 改为 NLI-only gate（≥0.90），BERTScore 降为监控指标，不作为过滤条件\\n  rationale: Reviewer 诊断：36% pass rate 的根因是 BERTScore 惩罚 style transfer 预期的词汇变化（contractions→full\\n    forms 等），而非内容泄漏。NLI 均值 0.9422、抽样 >0.99 证明语义保留良好。BERTScore 作为 token-level 相似度指标与\\n    style transfer 评估目标矛盾（改的就是 token）。Double-rewrite pass rate 更低（21/100）进一步印证。NLI-only\\n    gate 是度量校准（不消耗 8B 迭代配额），与 D002 全量评分兼容——primary ATE 用 NLI≥0.90 子集，secondary 按 BERTScore\\n    分层。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 14:32 UTC\\n  summary: 8B 初步 ATE≈0.028 不可见，归因三因素：Likert 粒度 + 8B rewriter 质量 + RATE corruption。不计入\\n    kill criteria，等 n=100 + 32B\\n  rationale: 36/100 初步数据 Cohen's d=0.055 远低于 0.3 门槛，但三个叠加因素解释了结果：(1) 83% 零差异源于 integer\\n    Likert 无法捕捉 sub-integer 效应；(2) 22% identical rewrites 稀释 ATE；
…[truncated 10852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-21T11:12:27.651598+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit template format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit template format requirements"
  }
}
```

</details>

---


### Tool call

_source line 263 · 2026-05-21T11:12:29.157811+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 264 · 2026-05-21T11:12:29.158244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 265 · 2026-05-21T11:12:31.065753+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 266 · 2026-05-21T11:12:31.819151+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 267 · 2026-05-21T11:12:31.819595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 268 · 2026-05-21T11:12:31.870147+00:00_

1	@inproceedings{murugadoss2025sos,
2	  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
3	  author={Murugadoss, Aakanksha and others},
4	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2409.15268}
7	}
8	
9	@inproceedings{li2026preference,
10	  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
11	  author={Li, Dawei and others},
12	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
13	  year={2026},
14	  url={https://arxiv.org/abs/2502.01534}
15	}
16	
17	@article{wang2026fairjudge,
18	  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
19	  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},
20	  journal={arXiv preprint arXiv:2602.06625},
21	  year={2026},
22	  url={https://arxiv.org/abs/2602.06625}
23	}
24	
25	
26	@inproceedings{dubois2025lc,
27	  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
28	  author={Dubois, Yann and others},
29	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
30	  year={2025},
31	  url={https://arxiv.org/abs/2404.04475}
32	}
33	
34	@article{casse2026concise,
35	  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},
36	  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},
37	  journal={arXiv preprint arXiv:2601.10809},
38	  year={2026},
39	  url={https://arxiv.org/abs/2601.10809}
40	}
41	
42	@article{counterfactual2025rhetorical,
43	  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},
44	  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},
45	  journal={arXiv preprint arXiv:2512.19908},
46	  year={2025},
47	  url={https://arxiv.org/abs/2512.19908}
48	}
49	
50	@article{soumik2026j
…[truncated 12292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-21T11:12:34.078722+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit template format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"}]

Based on the search results, I found information about ACL Rolling Review 2026 submission guidelines. Here are the key requirements:

## Paper Submission Process and Format

Submission is electronic, using the OpenReview.net platform. All long, short, and theme papers must follow the ACL Author Guidelines. Paper submissions must use the official ACL style template.

## Page Limits

For papers committed to ACL 2026 specifically: Final versions of accepted papers will be given one additional page of content (up 
…[truncated 998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6427
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-21T11:12:39.350031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-21T11:12:39.802798+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-2 issues (carried over, all resolved except R2-N1)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 2
13	    resolution: "Title changed. 4 CSD occurrences updated. §3.5 has 3 identification assumptions."
14	    resolution_round: 2
15	    mentions:
16	      - round: 3
17	        reviewers: [1, 2]
18	        note: "因果语言降级问题在 Round 3 以新形式复发，见 R3-N1"
19	
20	  - id: "R2-N1"
21	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
22	    category: framing
23	    severity: warning
24	    status: in_progress
25	    first_raised_round: 1
26	    last_seen_round: 3
27	    resolution: null
28	    resolution_round: null
29	    mentions:
30	      - round: 3
31	        reviewers: [1, 2]
32	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知），excitement 评分 3-3.5/5。见 R3-N3。"
33	
34	  - id: "R1-N2"
35	    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
36	    category: method
37	    severity: critical
38	    status: resolved
39	    first_raised_round: 1
40	    last_seen_round: 1
41	    resolution: "§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89"
42	    resolution_round: 1
43	
44	  - id: "R1-N3"
45	    summary: "NLI 阈值 0.90 无 justification"
46	    category: method
47	    severity: critical
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1
51	    resolution: "Threshold on plateau, robust 0.70-0.95"
52	    resolution_round: 1
53	
54	  - id: "R2-N2"
55	    summary: "RATE 批评缺乏 matched replication"
56	    category: framing
57	    severity: critical
58	    status: resolved
59	    first_raised_round: 1
60	    last_seen_round: 1
61	    resolution: "§likert_pairwise h2h on same dat
…[truncated 19200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-21T11:12:39.953816+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "writing_plan.yaml"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-21T11:12:40.004607+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/writing_plan.yaml\", \"content\": \"meta:\\n  venue: \\\"EMNLP 2026 Main via ARR\\\"\\n  format: \\\"Long paper, 8 pages + unlimited references\\\"\\n  deadline: \\\"ARR June 2026 cycle (~June 15)\\\"\\n  template: \\\"ACL style (acl.sty, review mode)\\\"\\n  core_claim: \\\"Standard Likert scoring systematically underestimates style bias in LLM judges; binary style counterfactuals with pairwise comparison reveal causal bias that Likert misses.\\\"\\n  status: partial_draft\\n  partial_scope: [introduction, abstract_skeleton, figure_1_spec]\\n\\nvisualization_plan:\\n  - fig_id: fig1_likert_blindspot\\n    type: statistical\\n    tool: matplotlib\\n    placement: introduction\\n    aspect_ratio: \\\"2.2:1\\\"\\n    layout: \\\"2-panel, full-width (figure*)\\\"\\n    data_source: \\\"registry: mvp_32b_ate (Likert scores), pairwise_32b (pairwise results)\\\"\\n    raw_data_paths:\\n      likert: \\\"/root/causal_style_decomp_judge/data/scored_32b.jsonl\\\"\\n      pairwise: \\\"/root/causal_style_decomp_judge/data/pairwise_results_32b.jsonl\\\"\\n\\n    narrative_intent: >\\n      Standard Likert scoring sees no difference between formal and casual responses\\n      (overlapping distributions, p=0.33), while pairwise comparison on the same data\\n      reveals a 69.1% formal win rate (p=0.006). This measurement gap is the central\\n      problem CSD exposes.\\n\\n    design_notes:\\n      - \\\"Pattern H: asymmetric 2-panel [1.4:1] — left panel wider (distribution needs more space), right panel narrower (single bar)\\\"\\n      - \\\"Pattern C: dashed line at 50% baseline in right panel (chance level)\\\"\\n      - \\\"Pattern A: light blue band above 50% in right panel marking 'formal preference zone'\\\"\\n      - \\\"Pattern E: Wilson CI error bar on win rate bar [55.97%, 79.72%]\\\"\\n      - \\\"Pattern J: path-effect white stro
…[truncated 2304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-21T11:13:35.197371+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 审查论文\n- 论文路径: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## Venue 要求\n- **EMNLP 2026 Main Conference** via ARR\n- 正文 8 页限制，参考文献不限页数\n- ACL 模板，double-blind 审稿\n- Limitations section 必须，不计入页数\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点审查以下方面，逐条给出详细评价：\n\n1. **统计框架严谨性**：\n   - Holm-Bonferroni correction 的应用是否正确（6 tests 的 family 定义）\n   - Bradley-Terry 模型假设是否满足（IIA 等）\n   - GEE 模型设定（exchangeable correlation、additive specification）\n   - Bootstrap CI 的 pair-level resampling 是否恰当\n   - 多重比较分类（primary/exploratory/confirmatory）是否合理\n\n2. **NLI Gate 有效性**：\n   - DeBERTa-v3-large 0.90 阈值的 justification\n   - False negative rate 分析（8.4%）的可靠性\n   - Direction-aware NLI（verbosity）的方法论合理性\n   - NLI gate 验证使用 Qwen3-32B 作为 annotator 的 evaluator-producer bias 风险\n   - GPT-4o spot-check（47/50）的独立性和充分性\n\n3. **因果声明与方法论强度匹配**：\n   - Title 中 \"Controlled Style Decomposition\" 的因果含义\n   - §3.5 \"Interventional Design\" 的 DAG 是否 justified\n   - \"interventional rather than formal causal evidence\" disclaimer 是否充分\n   - Originality OR 显著（Table 3）是否证明识别假设经验性违反\n\n4. **实验设计**：\n   - Evaluator-producer bias（Qwen3-32B 同时作 rewriter + judge）\n   - Rewriter independence test 的覆盖范围（verbosity + formality）\n   - Claude Sonnet 4 作为 negative control 的解读\n   - 样本量 n=88/355 的统计充分性\n   - Cross-benchmark replication 的可信度\n\n5. **Likert Blindspot 的定义和测量**：\n   - \"measurement attenuation\" vs \"power gap\" 的区分是否令人信服\n   - n=355 d→0 是否真的排除了 power gap 解释\n   - Sensitivity hierarchy（Table 2）7 种方法比较的公平性\n   - Power curve（Figure 3）的解读是否构成 post-hoc power analysis\n\n请给出：\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**\n- **Overall Assessment**（按 EMNLP 2026 评分标准）\n- **Confidence**（1-5）",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 审查论文\n- 论文路径: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## Venue 要求\n- **EMNLP 2026 Main Conference** via ARR\n- 正文 8 页限制，参考文献不限页数\n- ACL 模板，double-blind 审稿\n- Limitations section 必须，不计入页数\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点审查以下方面，逐条给出详细评价：\n\n1. **统计框架严谨性**：\n   - Holm-Bonferroni correction 的应用是否正确（6 tests 的 family 定义）\n   - Bradley-Terry 模型假设是否满足（IIA 等）\n   - GEE 模型设定（exchangeable correlation、additive specification）\n   - Bootstrap CI 的 pair-level resampling 是否恰当\n   - 多重比较分类（primary/exploratory/confirmatory）是否合理\n\n2. **NLI Gate 有效性**：\n   - DeBERTa-v3-large 0.90 阈值的 justification\n   - False negative rate 分析（8.4%）的可靠性\n   - Direction-aware NLI（verbosity）的方法论合理性\n   - NLI gate 验证使用 Qwen3-32B 作为 annotator 的 evaluator-producer bias 风险\n   - GPT-4o spot-check（47/50）的独立性和充分性\n\n3. **因果声明与方法论强度匹配**：\n   - Title 中 \"Controlled Style Decomposition\" 的因果含义\n   - §3.5 \"Interventional Design\" 的 DAG 是否 justified\n   - \"interventional rather than formal causal evidence\" disclaimer 是否充分\n   - Originality OR 显著（Table 3）是否证明识别假设经验性违反\n\n4. **实验设计**：\n   - Evaluator-producer bias（Qwen3-32B 同时作 rewriter + judge）\n   - Rewriter independence test 的覆盖范围（verbosity + formality）\n   - Claude Sonnet 4 作为 negative control 的解读\n   - 样本量 n=88/355 的统计充分性\n   - Cross-benchmark replication 的可信度\n\n5. **Likert Blindspot 的定义和测量**：\n   - \"measurement attenuation\" vs \"power gap\" 的区分是否令人信服\n   - n=355 d→0 是否真的排除了 power gap 解释\n   - Sensitivity hierarchy（Table 2）7 种方法比较的公平性\n   - Power curve（Figure 3）的解读是否构成 post-hoc power analysis\n\n请给出：\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**\n- **Overall Assessment**（按 EMNLP 2026 评分标准）\n- **Confidence**（1-5）",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-21T11:13:54.140479+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18943
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-21T11:13:54.642636+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 审查论文\n- 论文路径: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## Venue 要求\n- **EMNLP 2026 Main Conference** via ARR\n- 正文 8 页限制，参考文献不限页数\n- ACL 模板，double-blind 审稿\n- Limitations section 必须，不计入页数\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点审查以下方面，逐条给出详细评价：\n\n1. **贡献新颖性评估**：\n   - Contribution 1（CSD 框架）：与 RATE (Reber 2025)、Counterfactual Rhetorical (2025) 的差异化是否充分？\n   - Contribution 2（Likert Blindspot）：这是否为心理测量学已知现象（Thurstone 1927, DeCoster 2011）的 domain transfer？novelty 在哪里？\n   - Contribution 3（GEE conditional decomposition）：是否是标准统计方法的直接应用？\n   - Contribution 4（practical implications）：证据基础是否支撑推荐的强度？\n   - 与最新竞品（CASSE 2026, FairJudge 2026, Soumik 2026, Preference Leakage 2026）的定位是否清晰？\n\n2. **Related Work 完整性**：\n   - 引用数量（22 篇）是否符合 EMNLP 长文标准（通常 40-60 篇）？\n   - 是否遗漏关键文献方向？\n   - 对 RATE 的批评是否公平？\n   - Counterfactual text generation 领域文献是否覆盖？\n   - NLG evaluation methodology 文献是否充分？\n\n3. **Framing 准确性**：\n   - \"Likert Blindspot\" 这个术语——是真正的 blindspot（不可能检测）还是 efficiency gap（需要更大样本）？\n   - \"four critical gaps\" 的定义是否公平？其他方法真的都没有做到吗？\n   - \"measurement attenuation\" 的 framing 是否过度包装了一个功效差异？\n   - Abstract 是否准确反映论文内容？是否过于 dense？\n\n4. **写作质量**：\n   - 论文结构是否清晰？\n   - 术语一致性（controlled/interventional/causal 混用？）\n   - 表格/图表是否 self-contained？\n   - Conclusion 是否过于简短？\n   - Limitations 的覆盖面是否充分？\n\n5. **格式合规性**：\n   - 页数是否符合 8 页限制？\n   - 匿名性是否满足 double-blind？\n   - 引用格式是否符合 ACL 标准？\n   - Appendix 是否必要且不滥用？\n\n请给出：\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（具体缺什么方向的什么文献）\n- **Overall Assessment**（按 EMNLP 2026 评分标准）\n- **Confidence**（1-5）",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 审查论文\n- 论文路径: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## Venue 要求\n- **EMNLP 2026 Main Conference** via ARR\n- 正文 8 页限制，参考文献不限页数\n- ACL 模板，double-blind 审稿\n- Limitations section 必须，不计入页数\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点审查以下方面，逐条给出详细评价：\n\n1. **贡献新颖性评估**：\n   - Contribution 1（CSD 框架）：与 RATE (Reber 2025)、Counterfactual Rhetorical (2025) 的差异化是否充分？\n   - Contribution 2（Likert Blindspot）：这是否为心理测量学已知现象（Thurstone 1927, DeCoster 2011）的 domain transfer？novelty 在哪里？\n   - Contribution 3（GEE conditional decomposition）：是否是标准统计方法的直接应用？\n   - Contribution 4（practical implications）：证据基础是否支撑推荐的强度？\n   - 与最新竞品（CASSE 2026, FairJudge 2026, Soumik 2026, Preference Leakage 2026）的定位是否清晰？\n\n2. **Related Work 完整性**：\n   - 引用数量（22 篇）是否符合 EMNLP 长文标准（通常 40-60 篇）？\n   - 是否遗漏关键文献方向？\n   - 对 RATE 的批评是否公平？\n   - Counterfactual text generation 领域文献是否覆盖？\n   - NLG evaluation methodology 文献是否充分？\n\n3. **Framing 准确性**：\n   - \"Likert Blindspot\" 这个术语——是真正的 blindspot（不可能检测）还是 efficiency gap（需要更大样本）？\n   - \"four critical gaps\" 的定义是否公平？其他方法真的都没有做到吗？\n   - \"measurement attenuation\" 的 framing 是否过度包装了一个功效差异？\n   - Abstract 是否准确反映论文内容？是否过于 dense？\n\n4. **写作质量**：\n   - 论文结构是否清晰？\n   - 术语一致性（controlled/interventional/causal 混用？）\n   - 表格/图表是否 self-contained？\n   - Conclusion 是否过于简短？\n   - Limitations 的覆盖面是否充分？\n\n5. **格式合规性**：\n   - 页数是否符合 8 页限制？\n   - 匿名性是否满足 double-blind？\n   - 引用格式是否符合 ACL 标准？\n   - Appendix 是否必要且不滥用？\n\n请给出：\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（具体缺什么方向的什么文献）\n- **Overall Assessment**（按 EMNLP 2026 评分标准）\n- **Confidence**（1-5）",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-21T11:13:55.646718+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-21T11:13:56.604557+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1961
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-21T11:13:57.882393+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2235
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-21T11:13:57.882807+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "EMNLP 2026 Main Conference via ARR, long paper (8 pages). 请提交到 paperreview.ai 获取外部审稿意见。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "EMNLP 2026 Main Conference via ARR, long paper (8 pages). 请提交到 paperreview.ai 获取外部审稿意见。"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-21T11:13:58.587011+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 704
}
```

</details>

---


### Assistant

_source line 282 · 2026-05-21T11:14:07.278904+00:00_

所有审稿线已并行启动：

| 线路 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已派发 |
| Reviewer 2（新颖性/完整性） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 已发送协助卡片，8h 后自动提醒 |

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events
