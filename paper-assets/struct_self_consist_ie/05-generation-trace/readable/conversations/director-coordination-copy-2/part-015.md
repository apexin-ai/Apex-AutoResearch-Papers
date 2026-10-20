# Director coordination — Part 15 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 14](part-014.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 16 →](part-016.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 347

### User

_source line 4521 · 2026-05-23T07:10:16.582732+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 R42 评分分歧的逐条回应

---

### 核心分歧定位

4.0 vs 3.5 的分歧归结为一个判断：**对于一篇以诊断分析为核心贡献的论文，"负面发现 + 有限正面结果"是否足以达到 Conference 水平？**

我的立场：是的。Conference 级别的标准是"对社区有实质性贡献"，而非"必须有强正面方法创新"。这篇论文的贡献在于：(1) 首次系统解释了一个广泛观察到但未被诊断的现象（SC fails on NER），(2) 提供了可复用的概念工具（degeneracy, signal alignment collapse），(3) 实验执行标准极高。负面发现的价值在于防止社区在无效方向上浪费资源。

R2 的立场隐含假设"Conference 论文需要显著正面结果"，这一标准更适合方法论文而非分析/诊断论文。

---

### R2 维持 3.5 的 3 个理由

**[REBUT] 理由 1：核心 insight 与 Landesberg (2026) 并发，structured prediction 特异性是增量贡献**

不同意"增量贡献"的定性判断。

(a) **Concurrent ≠ incremental**。Concurrent work 的存在不降低独立发现的贡献——ACL/EMNLP 常规接收与高影响 concurrent work 有重叠的论文（例如多个 group 同时发现 in-context learning 的关键属性）。关键问题是本文是否在 Landesberg 基础上有实质性的独立贡献。

(b) **Table 1（p.3）的七维度对比**表明差异不是"simple domain adaptation"：
- **Failure mechanism 不同**：Landesberg 发现的是 prompt-level baseline effects（within-prompt correlation 低于 global）；本文发现的是 degeneracy（12–69% identical entity sets, Table 3）和 signal alignment collapse（α→0）——这两个机制在 reasoning tasks 中不存在（scalar answers 无 degeneracy 概念）。
- **Granularity 不同**：Landesberg 停留在 prompt-level r decomposition；本文深入到 entity-level diagnostics（D, G_nd, α），并建立 MBR 形式化连接（Proposition 1）。
- **Actionable output 不同**：Landesberg 无 constructive remedy；本文提出 entity construction 并验证条件有效性。

(c) **反事实检验**：如果 Landesberg 不存在，本文的贡献是否改变？不会——degeneracy decomposition、LP compression 分析、entity construction 全部独立成立。如果本文不存在，Landesberg 的 reasoning-level findings 能否解释 NER 上的 SC 失败？不能——degeneracy 和 entity-set structure 是 NER-specific 的。

(d) 我承认 §2 Related Work 在 R41 时对 Landesberg 处理不足，但 R42 已用 Table 1 + 半页对比段落充分 differentiate。R2 将此问题延续到 R42 评分中，但 R42 的修改已解决了 differentiation 不足的问题。

---

**[PARTIALLY AGREE] 理由 2：有限实际影响——正面结果弱且统计边缘**

部分同意事实判断，不同意对论文价值的推论。

事实层面同意：+1.10pp 在 global Holm 下 p_adj=0.055 是 marginally non-significant；5-epoch 下 LP gain 消失至 +0.09pp。论文的正面结果确实有限且高度条件化。

但不同意这决定评分：

(a) **论文的核心价值不在正面结果**。Abstract 的第一句是 "Test-time compute scaling—repeated sampling with self-consistency or best-of-N—yields large gains on reasoning tasks, but whether these gains transfer to NER remains open." 论文回答的问题是 "why does SC fail on NER"，不是 "here's a method to make SC work on NER." 核心贡献是诊断框架（degeneracy + signal collapse），entity construction 是 secondary contribution。

(b) **负面发现的社区价值被低估**。NER 社区已有多篇工作尝试将 SC/TTS 应用于 NER（Yao et al. 2026, Wang et al. 2023），但缺乏系统性分析解释为什么这些尝试大多失败。本文提供的诊断框架可以帮助未来研究者在 **尝试之前** 判断 SC 是否值得（测 degeneracy → 如果 >50% 则不值得），这对资源节约有直接价值。

(c) **统计处理已达最佳实践**。三重校正透明报告 + 非预注册声明 + TOST equivalence testing——这比大多数提交的论文更严谨。Global p_adj=0.055 是论文的真实局限，但诚实报告是加分而非减分。

结论：正面结果有限是事实，但不应成为扣分项——论文从未 overclaim 正面结果是核心贡献。

---

**[REBUT] 理由 3：标题 "Why" 暗示因果但论文提供 when/how**

与我在 R41 对 R2-W2 的回应一致，不同意。

(a) NLP/ML 论文标题中 "Why" 的使用惯例是诊断性/分析性解释，不等于严格因果推断。例：
- "Why Does Unsupervised Pre-training Help Deep Learning?" (Erhan et al., 2010)——提供的也是诊断性分析
- "Why Do Neural Networks Generalize?" (Neyshabur et al., 2017)——提供的是 what correlates with generalization
- 这些论文均被高引且标题未受质疑

(b) 论文确实回答了 "why"："SC fails on NER **because of** degeneracy (12–69% identical entity sets) and signal alignment collapse (within-instance LP variance → 0)." 这是机制性解释（mechanistic explanation），比纯粹的 "when" 更强。Degeneracy 不是 "when SC fails" 的条件描述——它是 "why MV gains are zero" 的直接机制（如果所有 N 个 outputs 相同，voting 在数学上不可能改善结果）。

(c) 标题修改（如改为 "When and How..."）会降低论文的冲击力且不更准确——论文确实提供了 mechanistic "why"，只是不是 interventional causal "why"。

---

### R2 新发现的问题

**[AGREE] NEW-1：§7.5 与 Table 58 数值不一致**

这是一个需要修复的事实性错误。

- §7.5: LP gain +1.39→**+0.09±0.04** pp, **94%** reduction
- Table 58: LP Δ +1.39→**+0.12±0.04** pp, **91%** reduction

终值差异（0.09 vs 0.12）和百分比差异（94% vs 91%）不大，但在同一论文中同一数据应该一致。可能原因：§7.5 使用了不同的 seed 子集或 rounding 规则。建议：(a) 统一数字，以 Table 58 的更精确数字为准（如果 Table 58 基于完整数据），(b) 如果两处计算基础不同（如不同 seed 子集），明确标注。

---

**[AGREE] NEW-2：Entity construction 数字链不清晰**

同意需要澄清。

- Abstract: +1.10 pp
- §7.5 上文: +1.10±0.51 pp（3-epoch）
- §7.5 epoch confound 段: **+0.88**→+0.20 pp, 77% reduction

+1.10 vs +0.88 的差异最可能解释：+1.10 是 **4-seed mean**（primary 报告），+0.88 是 **3-seed mean** 或特定 seed 子集。但论文未明确说明，读者无法自行 verify 这一差异。

建议：在 §7.5 epoch confound 段首次出现 +0.88 时加括号说明 "(3-epoch, N-seed mean)" vs Abstract 的 "+1.10 (4-seed mean)" 的区别，或统一报告基础。

---

### R2 Should-Fix 状态回应

**R41-W1 (diagnostic vs prescriptive): [MOSTLY RESOLVED]**

同意 R2 的 "mostly resolved" 判断。§7.5 "predicts" 与 Abstract "limited predictive power" 确有轻微张力，但这一张力现在是可控的——两处的含义兼容（"limited predictive power" 允许 "predicts under specific conditions"）。不需要进一步修改。

**R41-W5 (entity-level 增量贡献): [PARTIALLY RESOLVED]**

同意 R2 的 "partially resolved" 判断。Table 1 改善了概念层面的论证，但仍缺乏一个具体的 case study 展示 "entity-level analysis reveals X but task-level analysis misses X"。不过，我认为这不影响接收——degeneracy 本身就是一个只有在 entity-level 才能定义和测量的概念（"all N outputs produce identical entity sets" 无法从 task-level F1 equality 中区分），这是足够的 conceptual argument。

---

### 评分维持与最终立场

**维持 4.0 (Conference)**。

核心论证：
1. R2 的三个维持理由中，理由 1（concurrent work）和理由 3（标题）我 rebut——这些不足以将论文降至 Borderline。理由 2（有限正面结果）我 partially agree 事实判断但不同意其对评分的影响——诊断论文不应以正面方法结果为主要评价标准。
2. R2 的两个新发现（NEW-1, NEW-2）是 minor 数值不一致问题，camera-ready 可修。
3. 论文在 R42 修订中展现了对所有 Must-Fix 的实质性回应，统计报告达到最佳实践水平，claims 与 evidence 对齐——这些是 Conference 论文的标志。

如果 R2 坚持 3.5，我建议的 compromise 是 **3.5–4.0 之间偏 4.0**（即倾向接收），两个 NEW issues 应在 camera-ready 中修复。论文作为 Findings 也可接收（R2 的 3.5 隐含 Findings 接收），但我认为其贡献——首次系统诊断 SC 在结构化预测上的失败机制——值得 main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 4522 · 2026-05-23T07:12:50.785089+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 4523 · 2026-05-23T07:12:50.885951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4524 · 2026-05-23T07:12:53.145465+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4525 · 2026-05-23T07:12:54.250059+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T06:59:59.080875+00:00\", \"completed_at\": \"2026-05-23T07:04:02.529297+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 23\", \"message\": \"几乎空白页：仅顶部 9 行文字（appendix subsection p 结尾），其余 ~85% 完全空白。审稿人会认为空间浪费严重，应将该段文字合并到前一页或后一页，消除空白页\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"三个 display items（Figure 3 + Figure 4 + Table 5）挤在同一页，Figure 3 和 Figure 4 尺寸偏小，轴标签和 legend 字号接近可读性下限。考虑将 Table 5 移至 p6 底部或 p8 以缓解拥挤\"}, {\"severity\": \"warning\", \"dimension\": \"page 2\", \"message\": \"Figure 1 内部注释文字偏小（\\\"AUROC = 0.82\\\"、\\\"p = 0.39\\\"、箭头标注），可能低于正文字号 70%。建议放大关键数值标注\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Figure 7 热力图使用颜色渐变+叠加数字，灰度打印时颜色区分度下降。建议增加数字对比度或使用 diverging colormap\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文最后一页（Section 7.4-8）全为纯文本，无任何 display item。作为 Discussion/Conclusion 可接受，但如果能将一个 prescriptive 的 summary table 放入会增强结尾力度\"}, {\"severity\": \"info\", \"dimension\": \"page 46\", \"message\": \"Table 69（Differentiation matrix）跨全宽，表内文字非常小（约 6-7pt），部分条目需仔细辨认。建议适当精简或增大字号\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 5（Temperature robustness）双面板 bar chart 字号偏小但可读。appendix 图表整体可接受\"}, {\"severity\": \"info\", \"dimension\": \"pages 12-47\", \"message\": \"附录共 36 页，内容极其详尽（59 个 tables + 11 个 figures）。虽然体现了实验严谨性，但审稿人可能不会全部阅读——建议在附录开头加一段导读（\\\"Appendix overview\\\"），帮助审稿人定位关键补充材料\"}], \"counts\": {\"critical\": 1, \"warning\": 2, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 4526 · 2026-05-23T07:12:54.250463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4527 · 2026-05-23T07:12:54.301081+00:00_

1	issues:
2	# ===== ROUND 41 MUST-FIX — 全部已修复，待 R42 验证 =====
3	- id: R41-N1
4	  summary: "分解 bound 仅恢复 3-12% 实际增益，核心形式化贡献实用价值不足"
5	  category: method
6	  severity: critical
7	  status: in_progress
8	  first_raised_round: 38
9	  last_seen_round: 41
10	  mentions:
11	    - round: 40
12	      reviewers: [1, 2]
13	      note: "R40 已标注，要求 reposition 为 diagnostic decomposition tool"
14	    - round: 41
15	      reviewers: [1, 2]
16	      note: "R1 Must-Fix, R2 交叉 AGREE。bound 仅解释 3-12%。"
17	  action_items:
18	    - round: 41
19	      action: "§6.3 重定位为 necessary condition test；弱化 Table 33 ratio；声明 intentionally loose"
20	      assigned_to: paper_agent
21	      status: done
22	  resolution: "§6.3 已重定位为 necessary condition screening test，recovery ratio 重新定位为 illustrative。待 R42 验证。"
23	
24	- id: R41-N2
25	  summary: "核心正面 claim 统计显著性取决于多重比较校正方案选择"
26	  category: method
27	  severity: critical
28	  status: in_progress
29	  first_raised_round: 34
30	  last_seen_round: 41
31	  mentions:
32	    - round: 40
33	      reviewers: [1, 2]
34	      note: "R40 已标注。"
35	    - round: 41
36	      reviewers: [1, 2]
37	      note: "R1 Must-Fix, R2 交叉 AGREE。per-family 校正缺乏先验理由。"
38	  action_items:
39	    - round: 41
40	      action: "§7.5 提供 family 划分先验理由；主文同时报告全局 p_adj=0.055 和 per-family p_adj=0.006"
41	      assigned_to: paper_agent
42	      status: done
43	  resolution: "§7.5 已添加 family 划分先验理由（methodological distinctions at design time），双 p 值透明报告。待 R42 验证。"
44	
45	- id: R41-N3
46	  summary: "Mechanistic probes 使用 Qwen2.5-7B 而非主实验 Qwen3-8B"
47	  category: experiment
48	  severity: critical
49	  status: in_progress
50	  first_raised_round: 36
51	  last_seen_round: 41
52	  mentions:
53	    - round: 41
54	      reviewers: [1, 2]
55	      note: "R1 Must-Fix, R2 AGREE。正文引用 probe 时必须标注模型不一致。"
56	  action_items:
57	    - round: 41
58	      action: "§4 标注 probe 模型不一致 + ESJ Qwen3-8B 交叉验证数据"
59	      assigned_to: paper_agent
60	      status: done
61	    - round: 41
62	      action: "Qwen3-8B ESJ 实验"
63
…[truncated 10005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4528 · 2026-05-23T07:13:23.443647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_41.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_41.md"
  }
}
```

</details>

---


### Tool result

_source line 4529 · 2026-05-23T07:13:23.494667+00:00_

1	---
2	round: 41
3	review_mode: fresh
4	overall_score: 3.5 - Borderline Conference
5	timestamp: 2026-05-23T05:30:29.514484+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 41
12	
13	**论文**: "Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap"
14	**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
15	**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性; R2: 新颖性/完整性）
16	**审稿轮次**: Round 1, 1 轮收敛（关键问题全部达成共识）
17	
18	---
19	
20	## Summary
21	
22	论文研究 test-time compute scaling（self-consistency、best-of-N）在 NER 上的有效性。通过 4 个 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）、N=8–64 的系统实验，发现 quality estimation signals 能预测输出质量（AUROC 0.82）但无法有效指导样本选择（MV gains <1pp），揭示了 "correlation-selection gap"。论文提出一个诊断框架，将失败归因于 degeneracy（12–69% 实例产生相同 entity set）和 signal alignment collapse（α→0）。Entity-level construction 在 Few-NERD 3-epoch 上获得 +1.40pp，但该结果高度依赖训练状态（5-epoch 下降至 +0.09pp）。
23	
24	---
25	
26	## Strengths
27	
28	1. **研究问题重要且定位精准**：SC 在推理任务上成功但在结构化预测上失败的机制分析填补了社区空白。[R1, R2 共识]
29	
30	2. **实验极其详尽且透明**：4 数据集 × 2 模型家族 × 5 信号 × 9 方法类别，N scaling 到 64，38 页附录覆盖 robustness/ablation/calibration/power analysis。统计检验的两种校正方案均完整报告。TOST equivalence testing 是方法论加分项。[R1, R2 共识]
31	
32	3. **Degeneracy 概念有实证价值**：12–69% 的 NER 实例产生相同 entity set，这一 NER-specific failure mode 是有洞察力的发现，且 degeneracy rate 作为 pre-deployment check 有实际应用价值。[R1, R2 共识]
33	
34	4. **MBR decoding 理论连接清晰**：Proposition 1 将 entity construction 形式化为 MBR 特例，为结构化预测中的 SC 提供了理论锚点。[R1, R2 共识]
35	
36	5. **Negative results 诚实报告**：明确报告 cross-dataset transfer 失败、RE 局限、epoch confound，Appendix ah 预先回应 12 个潜在 objections。[R2]
37	
38	6. **Reproducibility 高**：承诺开源代码/checkpoint/数据，超参数报告详尽（Table 22, Appendix m），使用公开数据集和开放权重模型。[R1: 4/5, R2: 4/5]
39	
40	---
41	
42	## Weaknesses
43	
44	### Must-Fix（5 项，交叉分享后共识）
45	
46	**MF1** [R1-N1, R2 AGREE] **分解 bound 仅恢复 3–12% 实际增益，核心形式化贡献实用价值不足**
47	- 位置：§6.3, Figure 10, Table 33
48	- Bound E[ΔF1(A)] ≤ (1−D)·G_nd·α 仅捕捉 3–12% a
…[truncated 9427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4530 · 2026-05-23T07:13:51.368098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 4531 · 2026-05-23T07:13:51.820125+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary analysis, with preliminary RE ($n{=}397$) and SQL ($n{=}196$) pilots.
4	Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields ${<}1$\,pp, revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that jointly determine scaling returns; cross-task exploration confirms task-specific failure modes.
6	Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; diminishes to $+0.09$\,pp at convergence; per-family Holm $p_{\text{adj}}{=}0.006$, global $p_{\text{adj}}{=}0.055$) but exhibits inverse scaling in most configurations (69\% of $N$-transitions).
7	The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 4532 · 2026-05-23T07:13:51.920891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 4533 · 2026-05-23T07:13:51.971587+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time scaling and self-consistency.}\label{sec:yun_contrast}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with scaling laws \cite{snell2025scaling, brown2024monkeys, gao2023scaling} yield large gains on reasoning; recent extensions include reward-tail-guided search \cite{li2026rewardtail}. Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and trained verifiers \cite{cobbe2021verifiers, lightman2024verify, li2023stepaware} target discrete-answer settings.
5	SC can fail when consistent outputs are wrong \cite{chen2023twofailures}; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} variants face limits where sub-output agreement does not yield selection gain.
6	\citet{yun2025price} identify diversity collapse under constrained decoding; we extend their qualitative account with quantitative diagnostics (\S\ref{sec:selection_gap}).
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE ($\rho$ up to 0.47); we extend to instance-level analysis: (1)~task-level $\rho$ masks instance-level degeneracy; (2)~we decompose failure into degeneracy and LP compression; (3)~pre-deployment diagnostics that task-level correlation cannot provide.
10	Critically, their task-level granularity cannot distinguish instances where scaling helps from those where it harms---our entity-level decomposition addresses this gap (Table~\ref{tab:novelty_comparison}).
11	\citet{xie2023zeroshot} propose entity voting for zero-shot NER; \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
12	
13	\paragraph{Uncertainty estimation and MBR.}
14	Our selection instantiates MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find MBR utilities degrade on structured outputs, consistent with our LP compression findings.
15	LP is well-calibrated at population 
…[truncated 2346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4534 · 2026-05-23T07:15:30.152148+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
  "offset": "100",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
    "offset": "100",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 4535 · 2026-05-23T07:15:30.202772+00:00_

100	%% ============================================================
101	\subsection{Prescriptive Results}\label{sec:prescriptive}
102	
103	Given that sample-level selection fails uniformly (\S\ref{sec:selection_gap}), we ask whether entity-level aggregation can extract value from multi-sample generation under favorable diagnostic conditions.
104	
105	\paragraph{Entity-level construction (exploratory).}
106	We aggregate entities across samples, retaining those exceeding $\theta{=}2/N$, with LP-weighted or uniform scoring ($\theta$ stable in $[0.15, 0.35]$; Appendix~\ref{app:theta_sweep}).
107	The diagnostic framework identifies conditions favoring gains: low degeneracy and strong LP alignment.
108	LP-weighted construction yields $+1.40{\pm}0.51$\,pp on Few-NERD ($p{<}0.001$; Table~\ref{tab:entity_construction}), consistent with these conditions ($D{=}13$\%, headroom${=}12.4$\,pp), a smaller non-significant $+0.32$\,pp on SciERC, and no gain on CoNLL ($-0.39$\,pp).\footnote{Degenerate instances contribute $\Delta{=}0$ by construction; gains concentrate in the non-degenerate subset ($+3.36$\,pp SciERC, $+5.18$\,pp CoNLL, $+7.08$\,pp Few-NERD).}
109	We group the 57 comparisons into methodological families---per-sample signals ($k{=}21$), cross-sample signals ($k{=}26$), and entity construction ($k{=}10$)---reflecting mechanistic distinctions defined at experiment design time (not selected post-hoc to optimize $p$-values).
110	Under global Holm--Bonferroni \cite{holm1979simple} correction across all $k{=}57$ comparisons, $p_{\text{adj}}{=}0.055$ (suggestive); under per-family correction within the 10-comparison entity-construction family, $p_{\text{adj}}{=}0.006$ (significant); BH FDR: $6/10$ construction comparisons at FDR${<}0.05$ (Appendix~\ref{app:holm}).
111	We report all three corrections for transparency; the family partition was not pre-registered.
112	Construction and LP selection are complementary ($\rho_{\text{adj}}$: Few-NERD $0.516$); QE signals support sele
…[truncated 1140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4536 · 2026-05-23T07:15:42.247734+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4537 · 2026-05-23T07:15:42.299306+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4538 · 2026-05-23T07:15:47.865547+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'R42 初始化 + 初审收集', 'status': 'completed', 'activeForm': '收集 R42 初审'}, {'content': 'R42 Step 1: 收集两位 Reviewer R42 报告', 'status': 'completed', 'activeForm': '收集 Reviewer 报告'}, {'content': 'R42 Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享'}, {'content': 'R42 Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断收敛状态'}, {'content': 'R42 Step 4: 合成报告 + 更新 issue tracker + 投递', 'status': 'pending', 'activeForm': '合成并投递报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'R42 初始化 + 初审收集', 'status': 'completed', 'activeForm': '收集 R42 初审'}, {'content': 'R42 Step 1: 收集两位 Reviewer R42 报告', 'status': 'completed', 'activeForm': '收集 Reviewer 报告'}, {'content': 'R42 Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享'}, {'content': 'R42 Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断收敛状态'}, {'content': 'R42 Step 4: 合成报告 + 更新 issue tracker + 投递', 'status': 'pending', 'activeForm': '合成并投递报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 4539 · 2026-05-23T07:15:47.916174+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4540 · 2026-05-23T07:16:11.762041+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'R42 初始化 + 初审收集', 'status': 'completed', 'activeForm': '收集 R42 初审'}, {'content': 'R42 Step 1: 收集两位 Reviewer R42 报告', 'status': 'completed', 'activeForm': '收集 Reviewer 报告'}, {'content': 'R42 Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享'}, {'content': 'R42 Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛状态'}, {'content': 'R42 Step 4: 合成报告 + 更新 issue tracker + 投递', 'status': 'in_progress', 'activeForm': '合成并投递报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'R42 初始化 + 初审收集', 'status': 'completed', 'activeForm': '收集 R42 初审'}, {'content': 'R42 Step 1: 收集两位 Reviewer R42 报告', 'status': 'completed', 'activeForm': '收集 Reviewer 报告'}, {'content': 'R42 Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享'}, {'content': 'R42 Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛状态'}, {'content': 'R42 Step 4: 合成报告 + 更新 issue tracker + 投递', 'status': 'in_progress', 'activeForm': '合成并投递报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 4541 · 2026-05-23T07:16:11.913100+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 4542 · 2026-05-23T07:17:49.131499+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== ROUND 41 MUST-FIX — R42 全部验证通过 =====\n- id: R41-N1\n  summary: \"分解 bound 仅恢复 3-12% 实际增益，核心形式化贡献实用价值不足\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 40\n      reviewers: [1, 2]\n      note: \"R40 已标注，要求 reposition 为 diagnostic decomposition tool\"\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix, R2 交叉 AGREE。bound 仅解释 3-12%。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§6.3 已重定位为 intentionally loose necessary condition test，recovery ratio 重新定位为 screening test 而非 tight estimate。\"\n  action_items:\n    - round: 41\n      action: \"§6.3 重定位为 necessary condition test；弱化 Table 33 ratio；声明 intentionally loose\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§6.3 成功重定位为 necessary condition screening test。R42 两位 Reviewer 确认 RESOLVED。\"\n  resolution_round: 42\n\n- id: R41-N2\n  summary: \"核心正面 claim 统计显著性取决于多重比较校正方案选择\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 42\n  mentions:\n    - round: 40\n      reviewers: [1, 2]\n      note: \"R40 已标注。\"\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix, R2 交叉 AGREE。per-family 校正缺乏先验理由。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§7.5 提供 family 划分先验理由（mechanistic distinctions at design time），双 p 值透明报告，明确声明 not pre-registered。\"\n  action_items:\n    - round: 41\n      action: \"§7.5 提供 family 划分先验理由；主文同时报告全局 p_adj=0.055 和 per-family p_adj=0.006\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§7.5 family 划分理由充分，双 p 值透明报告。R42 两位 Reviewer 确认 RESOLVED。\"\n  resolution_round: 42\n\n- id: R41-N3\n  summary: \"Mechanistic probes 使用 Qwen2.5-7B 而非主实验 Qwen3-8B\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix, R2 AGREE。正文引用 probe 时必须标注模型不一致。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§4 已标注 Qwen2.5-7B-Instruct，ESJ Qwen3-8B 交叉验证 (AUROC 0.50-0.55)，Limitations 更新。\"\n  action_items:\n    - round: 41\n      action: \"§4 标注 probe 模型不一致 + ESJ Qwen3-8B 交叉验证数据\"\n      assigned_to: paper_agent\n      status: done\n    - round: 41\n      action: \"Qwen3-8B ESJ 实验\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"模型差异已显式标注，ESJ 在 Qwen3-8B 上确认 chance-level (AUROC 0.50-0.55)。R42 两位 Reviewer 确认 RESOLVED。\"\n  resolution_round: 42\n\n- id: R41-N4\n  summary: \"Novelty 与 Landesberg et al. (2026) 概念重叠，differentiation 不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix, R1 AGREE。§2 需半页系统对比。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§2 扩展为 4 维度系统对比（domain/mechanism/granularity/prescriptive），Table 1 新增 failure mechanism 行。R2 认为改进充分但 novelty increment 仍受限。\"\n  action_items:\n    - round: 41\n      action: \"§2 半页 Landesberg 系统对比 + Table 1 新增 failure mechanism 维度\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§2 系统对比清晰，Table 1 七维度对比。R42 两位 Reviewer 确认 RESOLVED。R2 对 novelty increment 的持续关注属于评估差异而非修改问题。\"\n  resolution_round: 42\n\n- id: R41-N5\n  summary: \"Few-NERD epoch confound 严重削弱最显著正面结果\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix, R1 升级 critical。Abstract +1.40pp 未加条件。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。Abstract 已限定条件（3-epoch training; diminishes at convergence），§7.5 完整呈现 94%/77% reduction 数据。\"\n  action_items:\n    - round: 41\n      action: \"Abstract 限定条件；§7.5 完整 3v5 epoch 数据；重定位为 finding\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Abstract 条件限定充分，§7.5 epoch confound 完整透明呈现。R42 两位 Reviewer 确认 RESOLVED。\"\n  resolution_round: 42\n\n# ===== ROUND 41 SHOULD-FIX — R42 状态更新 =====\n- id: R41-W1\n  summary: \"Diagnostic vs prescriptive 叙事定位不一致\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W1，完全共识。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。Abstract/Discussion 统一为 primarily diagnostic，§7.5 predictive language 改为 post-hoc。\"\n  action_items:\n    - round: 41\n      action: \"统一为 primarily diagnostic with limited predictive power\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"定位统一。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-W2\n  summary: \"2-3 seeds 统计推断力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1-W2, R2 AGREE。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未修改（response-letter-only item）。仍为遗留问题。\"\n  action_items:\n    - round: 41\n      action: \"Response-letter-only：引用 seed-replication Holm k=5 p=0.013\"\n      assigned_to: director\n      status: open\n\n- id: R41-W3\n  summary: \"RE/SQL 扩展过薄\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1-W3, R2 AGREE。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"Abstract 已标注 preliminary。R42 验证 Abstract 措辞充分。\"\n  action_items:\n    - round: 41\n      action: \"Response-letter-only：Abstract 已标 preliminary\"\n      assigned_to: director\n      status: done\n  resolution: \"Abstract 措辞 'preliminary RE (n=397) and SQL (n=196) pilots' 充分降低预期。\"\n  resolution_round: 42\n\n- id: R41-W4\n  summary: \"Related Work 覆盖面不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 41\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"遗漏 Eikema, calibration lit, TTS advances。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。Eikema et al. (2025), li2026rewardtail, desai2020calibration, xiao2022uncertainty 全部添加。\"\n  action_items:\n    - round: 41\n      action: \"§6 加 Eikema et al. 2025 + §2 加 calibration/TTS 引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"引用全部添加并验证。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-W5\n  summary: \"Entity-level decomposition 增量贡献需更强论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 41\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R2-W5, R1 AGREE。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未修改（response-letter-only item）。\"\n  action_items:\n    - round: 41\n      action: \"Response-letter-only：Table 3/4 已有数据\"\n      assigned_to: director\n      status: open\n\n- id: R41-W6\n  summary: \"Constrained decoding 对 LP 的 confound 未充分解耦\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"SciERC 不够，需至少两个数据集。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。Free-form ablation 扩展到 SciERC + CoNLL + Few-NERD（LP std ratio 0.86×-1.00×）。Discussion 引用跨数据集证据。\"\n  action_items:\n    - round: 41\n      action: \"CoNLL + FewNERD free-form ablation 实验\"\n      assigned_to: main_agent\n      status: done\n    - round: 41\n      action: \"Appendix 汇总表 + Limitations 更新\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Free-form ablation 在 3 数据集上一致（LP std ratio 0.86×-1.00×）。R42 验证通过。\"\n  resolution_round: 42\n\n# ===== ROUND 41 DIVERGENCE =====\n- id: R41-D1\n  summary: \"标题 'Why SC Fails for NER' 与内容匹配度\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [2]\n      note: \"R1 REBUT，分歧记录。\"\n    - round: 42\n      reviewers: [2]\n      note: \"R2 维持关注。R1 REBUT：NLP 标准标题范式。持续分歧。\"\n\n- id: R41-D2\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 37\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [2]\n      note: \"R1 REBUT，降为 Minor。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未变化。持续 divergence。\"\n\n# ===== ROUND 42 NEW ISSUES =====\n- id: R42-NEW1\n  summary: \"Abstract 数值引用不一致：entity construction (+1.40pp) 与 LP selection (+0.09pp) 在同一句混淆\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 42\n  last_seen_round: 42\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"Abstract 'diminishes to +0.09pp at convergence' 引用的是 LP selection 数字，而非 entity construction（应为 +0.20pp）。两位 Reviewer 均确认。\"\n  action_items:\n    - round: 42\n      action: \"Abstract 修正：entity construction 的 5-epoch 数字应为 +0.20pp 而非 +0.09pp（或明确区分两个 metric）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R42-NEW2\n  summary: \"§7.5 entity construction 3-epoch 数字不一致：+1.40pp (LP-weighted) vs +0.88pp (convergence 段)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 42\n  last_seen_round: 42\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"§7.5 line 108 LP-weighted construction +1.40pp vs line 115 'entity construction: +0.88→+0.20pp'。如为不同变体需明确标注；如为同一方法则存在矛盾。\"\n  action_items:\n    - round: 42\n      action: \"§7.5 明确区分 LP-weighted construction 与 uniform construction 的数字引用\"\n      assigned_to: paper_agent\n      status: open\n\n# ===== EARLIER RESOLVED =====\n- id: R39-W1\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"R40 确认合规。\"\n  resolution_round: 40\n\n- id: R39-W7\n  summary: \"Cross-model ensemble 仅 Few-NERD 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"已降调为 preliminary。\"\n  resolution_round: 40\n\n- id: R39-W8\n  summary: \"RE/SQL pilot 覆盖太薄\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 39\n  resolution: \"升级为 R41-W3。\"\n  resolution_round: 40\n\n- id: R39-W9\n  summary: \"LightGBM transfer failure 缺 feature-level analysis\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"Feature coefficient shift 分析已加入。\"\n  resolution_round: 40\n\n- id: R39-W11\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 39\n  resolution: \"R41 降为 divergence (R41-D2)。\"\n  resolution_round: 40\n\n- id: R39-W12\n  summary: \"Missing references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"R41 新遗漏记为 R41-W4，已修复。\"\n  resolution_round: 40\n\n- id: R39-W13\n  summary: \"Degeneracy 术语来源说明\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 39\n  resolution: \"已添加。\"\n  resolution_round: 40\n\n- id: R39-W14\n  summary: \"Related Work 密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"§8 压缩 43%。\"\n  resolution_round: 40\n\n- id: R38-MF1\n  summary: \"Title 改为 'A Diagnostic Framework'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 38\n  resolution: \"标题改为 'the Correlation-Selection Gap'。\"\n  resolution_round: 41\n\n- id: R38-MF3\n  summary: \"bypass → conditional improvement\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 38\n  resolution: \"已修改。\"\n  resolution_round: 39\n\n- id: R40-N1\n  summary: \"Degeneracy bound 仅恢复 3-12%\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-N1，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N1，R42 验证通过。\"\n  resolution: \"合并为 R41-N1，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-N2\n  summary: \"Holm-Bonferroni p_adj=0.055\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-N2，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N2，R42 验证通过。\"\n  resolution: \"合并为 R41-N2，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-N3\n  summary: \"Probes 用 Qwen2.5-7B\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-N3，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N3，R42 验证通过。\"\n  resolution: \"合并为 R41-N3，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-N4\n  summary: \"Concurrent work novelty 不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-N4，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N4，R42 验证通过。\"\n  resolution: \"合并为 R41-N4，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-N5\n  summary: \"标题 overpromise\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 41\n  resolution: \"标题已改为 'the Correlation-Selection Gap'。\"\n  resolution_round: 41\n\n- id: R40-W1\n  summary: \"Diagnostic/predictive 不清晰\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-W1，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-W1，R42 验证通过。\"\n  resolution: \"合并为 R41-W1，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-W4\n  summary: \"Few-NERD +1.39pp under-convergence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"升级为 R41-N5 Must-Fix，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N5，R42 验证通过。\"\n  resolution: \"合并为 R41-N5，R42 验证通过。\"\n  resolution_round: 42\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== ROUND 41 MUST-FIX — R42 全部验证通过 =====\n- id: R41-N1\n  summary: \"分解 bound 仅恢复 3-12% 实际增益，核心形式化贡献实用价值不足\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 40\n      reviewers: [1, 2]\n      note: \"R40 已标注，要求 reposition 为 diagnostic decomposition tool\"\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix, R2 交叉 AGREE。bound 仅解释 3-12%。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§6.3 已重定位为 intentionally loose necessary condition test，recovery ratio 重新定位为 screening test 而非 tight estimate。\"\n  action_items:\n    - round: 41\n      action: \"§6.3 重定位为 necessary condition test；弱化 Table 33 ratio；声明 intentionally loose\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§6.3 成功重定位为 necessary condition screening test。R42 两位 Reviewer 确认 RESOLVED。\"\n  resolution_round: 42\n\n- id: R41-N2\n  summary: \"核心正面 claim 统计显著性取决于多重比较校正方案选择\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 42\n  mentions:\n    - round: 40\n      reviewers: [1, 2]\n      note: \"R40 已标注。\"\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix, R2 交叉 AGREE。per-family 校正缺乏先验理由。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§7.5 提供 family 划分先验理由（mechanistic distinctions at design time），双 p 值透明报告，明确声明 not pre-registered。\"\n  action_items:\n    - round: 41\n      action: \"§7.5 提供 family 划分先验理由；主文同时报告全局 p_adj=0.055 和 per-family p_adj=0.006\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§7.5 family 划分理由充分，双 p 值透明报告。R42 两位 Reviewer 确认 RESOLVED。\"\n  resolution_round: 42\n\n- id: R41-N3\n  summary: \"Mechanistic probes 使用 Qwen2.5-7B 而非主实验 Qwen3-8B\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix, R2 AGREE。正文引用 probe 时必须标注模型不一致。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§4 已标注 Qwen2.5-7B-Instruct，ESJ Qwen3-8B 交叉验证 (AUROC 0.50-0.55)，Limitations 更新。\"\n  action_items:\n    - round: 41\n      action: \"§4 标注 probe 模型不一致 + ESJ Qwen3-8B 交叉验证数据\"\n      assigned_to: paper_agent\n      status: done\n    - round: 41\n      action: \"Qwen3-8B ESJ 实验\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"模型差异已显式标注，ESJ 在 Qwen3-8B 上确认 chance-level (AUROC 0.50-0.55)。R42 两位 Reviewer 确认 RESOLVED。\"\n  resolution_round: 42\n\n- id: R41-N4\n  summary: \"Novelty 与 Landesberg et al. (2026) 概念重叠，differentiation 不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix, R1 AGREE。§2 需半页系统对比。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§2 扩展为 4 维度系统对比（domain/mechanism/granularity/prescriptive），Table 1 新增 failure mechanism 行。R2 认为改进充分但 novelty increment 仍受限。\"\n  action_items:\n    - round: 41\n      action: \"§2 半页 Landesberg 系统对比 + Table 1 新增 failure mechanism 维度\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§2 系统对比清晰，Table 1 七维度对比。R42 两位 Reviewer 确认 RESOLVED。R2 对 novelty increment 的持续关注属于评估差异而非修改问题。\"\n  resolution_round: 42\n\n- id: R41-N5\n  summary: \"Few-NERD epoch confound 严重削弱最显著正面结果\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix, R1 升级 critical。Abstract +1.40pp 未加条件。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。Abstract 已限定条件（3-epoch training; diminishes at convergence），§7.5 完整呈现 94%/77% reduction 数据。\"\n  action_items:\n    - round: 41\n      action: \"Abstract 限定条件；§7.5 完整 3v5 epoch 数据；重定位为 finding\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Abstract 条件限定充分，§7.5 epoch confound 完整透明呈现。R42 两位 Reviewer 确认 RESOLVED。\"\n  resolution_round: 42\n\n# ===== ROUND 41 SHOULD-FIX — R42 状态更新 =====\n- id: R41-W1\n  summary: \"Diagnostic vs prescriptive 叙事定位不一致\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W1，完全共识。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。Abstract/Discussion 统一为 primarily diagnostic，§7.5 predictive language 改为 post-hoc。\"\n  action_items:\n    - round: 41\n      action: \"统一为 primarily diagnostic with limited predictive power\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"定位统一。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-W2\n  summary: \"2-3 seeds 统计推断力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1-W2, R2 AGREE。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未修改（response-letter-only item）。仍为遗留问题。\"\n  action_items:\n    - round: 41\n      action: \"Response-letter-only：引用 seed-replication Holm k=5 p=0.013\"\n      assigned_to: director\n      status: open\n\n- id: R41-W3\n  summary: \"RE/SQL 扩展过薄\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R1-W3, R2 AGREE。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"Abstract 已标注 preliminary。R42 验证 Abstract 措辞充分。\"\n  action_items:\n    - round: 41\n      action: \"Response-letter-only：Abstract 已标 preliminary\"\n      assigned_to: director\n      status: done\n  resolution: \"Abstract 措辞 'preliminary RE (n=397) and SQL (n=196) pilots' 充分降低预期。\"\n  resolution_round: 42\n\n- id: R41-W4\n  summary: \"Related Work 覆盖面不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 41\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"遗漏 Eikema, calibration lit, TTS advances。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。Eikema et al. (2025), li2026rewardtail, desai2020calibration, xiao2022uncertainty 全部添加。\"\n  action_items:\n    - round: 41\n      action: \"§6 加 Eikema et al. 2025 + §2 加 calibration/TTS 引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"引用全部添加并验证。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-W5\n  summary: \"Entity-level decomposition 增量贡献需更强论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 41\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R2-W5, R1 AGREE。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未修改（response-letter-only item）。\"\n  action_items:\n    - round: 41\n      action: \"Response-letter-only：Table 3/4 已有数据\"\n      assigned_to: director\n      status: open\n\n- id: R41-W6\n  summary: \"Constrained decoding 对 LP 的 confound 未充分解耦\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"SciERC 不够，需至少两个数据集。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。Free-form ablation 扩展到 SciERC + CoNLL + Few-NERD（LP std ratio 0.86×-1.00×）。Discussion 引用跨数据集证据。\"\n  action_items:\n    - round: 41\n      action: \"CoNLL + FewNERD free-form ablation 实验\"\n      assigned_to: main_agent\n      status: done\n    - round: 41\n      action: \"Appendix 汇总表 + Limitations 更新\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Free-form ablation 在 3 数据集上一致（LP std ratio 0.86×-1.00×）。R42 验证通过。\"\n  resolution_round: 42\n\n# ===== ROUND 41 DIVERGENCE =====\n- id: R41-D1\n  summary: \"标题 'Why SC Fails for NER' 与内容匹配度\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [2]\n      note: \"R1 REBUT，分歧记录。\"\n    - round: 42\n      reviewers: [2]\n      note: \"R2 维持关注。R1 REBUT：NLP 标准标题范式。持续分歧。\"\n\n- id: R41-D2\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 37\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [2]\n      note: \"R1 REBUT，降为 Minor。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未变化。持续 divergence。\"\n\n# ===== ROUND 42 NEW ISSUES =====\n- id: R42-NEW1\n  summary: \"Abstract 数值引用不一致：entity construction (+1.40pp) 与 LP selection (+0.09pp) 在同一句混淆\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 42\n  last_seen_round: 42\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"Abstract 'diminishes to +0.09pp at convergence' 引用的是 LP selection 数字，而非 entity construction（应为 +0.20pp）。两位 Reviewer 均确认。\"\n  action_items:\n    - round: 42\n      action: \"Abstract 修正：entity construction 的 5-epoch 数字应为 +0.20pp 而非 +0.09pp（或明确区分两个 metric）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R42-NEW2\n  summary: \"§7.5 entity construction 3-epoch 数字不一致：+1.40pp (LP-weighted) vs +0.88pp (convergence 段)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 42\n  last_seen_round: 42\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"§7.5 line 108 LP-weighted construction +1.40pp vs line 115 'entity construction: +0.88→+0.20pp'。如为不同变体需明确标注；如为同一方法则存在矛盾。\"\n  action_items:\n    - round: 42\n      action: \"§7.5 明确区分 LP-weighted construction 与 uniform construction 的数字引用\"\n      assigned_to: paper_agent\n      status: open\n\n# ===== EARLIER RESOLVED =====\n- id: R39-W1\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"R40 确认合规。\"\n  resolution_round: 40\n\n- id: R39-W7\n  summary: \"Cross-model ensemble 仅 Few-NERD 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"已降调为 preliminary。\"\n  resolution_round: 40\n\n- id: R39-W8\n  summary: \"RE/SQL pilot 覆盖太薄\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 39\n  resolution: \"升级为 R41-W3。\"\n  resolution_round: 40\n\n- id: R39-W9\n  summary: \"LightGBM transfer failure 缺 feature-level analysis\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"Feature coefficient shift 分析已加入。\"\n  resolution_round: 40\n\n- id: R39-W11\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 39\n  resolution: \"R41 降为 divergence (R41-D2)。\"\n  resolution_round: 40\n\n- id: R39-W12\n  summary: \"Missing references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"R41 新遗漏记为 R41-W4，已修复。\"\n  resolution_round: 40\n\n- id: R39-W13\n  summary: \"Degeneracy 术语来源说明\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 39\n  resolution: \"已添加。\"\n  resolution_round: 40\n\n- id: R39-W14\n  summary: \"Related Work 密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"§8 压缩 43%。\"\n  resolution_round: 40\n\n- id: R38-MF1\n  summary: \"Title 改为 'A Diagnostic Framework'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 38\n  resolution: \"标题改为 'the Correlation-Selection Gap'。\"\n  resolution_round: 41\n\n- id: R38-MF3\n  summary: \"bypass → conditional improvement\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 38\n  resolution: \"已修改。\"\n  resolution_round: 39\n\n- id: R40-N1\n  summary: \"Degeneracy bound 仅恢复 3-12%\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-N1，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N1，R42 验证通过。\"\n  resolution: \"合并为 R41-N1，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-N2\n  summary: \"Holm-Bonferroni p_adj=0.055\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-N2，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N2，R42 验证通过。\"\n  resolution: \"合并为 R41-N2，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-N3\n  summary: \"Probes 用 Qwen2.5-7B\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-N3，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N3，R42 验证通过。\"\n  resolution: \"合并为 R41-N3，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-N4\n  summary: \"Concurrent work novelty 不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-N4，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N4，R42 验证通过。\"\n  resolution: \"合并为 R41-N4，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-N5\n  summary: \"标题 overpromise\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 41\n  resolution: \"标题已改为 'the Correlation-Selection Gap'。\"\n  resolution_round: 41\n\n- id: R40-W1\n  summary: \"Diagnostic/predictive 不清晰\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"合并为 R41-W1，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-W1，R42 验证通过。\"\n  resolution: \"合并为 R41-W1，R42 验证通过。\"\n  resolution_round: 42\n\n- id: R40-W4\n  summary: \"Few-NERD +1.39pp under-convergence\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"升级为 R41-N5 Must-Fix，修复完成待验证。\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"合并为 R41-N5，R42 验证通过。\"\n  resolution: \"合并为 R41-N5，R42 验证通过。\"\n  resolution_round: 42\n"
  }
}
```

</details>

---


### Tool result

_source line 4543 · 2026-05-23T07:17:49.232590+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 14058}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4544 · 2026-05-23T07:20:16.702174+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 42 (Continue)\n\n**论文**: \"Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性; R2: 新颖性/完整性）\n**审稿模式**: 继续审稿（基于 R41 修改验证）\n**交叉分享**: R1 完成交叉回应；R2 未返回（经多轮等待），视为维持立场\n\n---\n\n## Summary\n\nRound 42 是对 R41 提出的 5 个 Must-Fix、6 个 Should-Fix 的修改验证轮。论文对全部 5 个 Must-Fix 进行了实质性修改：§6.3 将 bound 重定位为 necessary condition screening test；§7.5 透明报告双重 p 值并提供 family 划分先验理由；§4 标注 probe 模型差异并新增 Qwen3-8B ESJ 交叉验证；§2 扩展 Landesberg 系统对比为 4 维度 + Table 1 增加 failure mechanism 行；Abstract 对 +1.40pp 加入 3-epoch 条件限定。Should-Fix 中 4 项（W1 叙事定位、W3 RE/SQL 措辞、W4 缺失引用、W6 free-form ablation）已修复。\n\n两位 Reviewer 对所有 R41 Must-Fix 修改验证为 RESOLVED。评分分歧：R1 升至 4.0 (Conference)，R2 维持 3.5 (Borderline Conference)。修改引入两个新发现的数值不一致问题。\n\n---\n\n## R41 Issue Resolution Status\n\n### Must-Fix（5/5 RESOLVED）\n\n| ID | Issue | R42 Status | 说明 |\n|----|-------|-----------|------|\n| N1 | Bound 仅恢复 3-12% | ✅ RESOLVED | §6.3 成功重定位为 \"intentionally loose necessary condition test\"，不再 oversell |\n| N2 | 统计显著性依赖校正方案 | ✅ RESOLVED | §7.5 双 p 值透明报告（global 0.055, per-family 0.006），family 划分有先验理由，明确声明 not pre-registered |\n| N3 | Probe 模型不一致 | ✅ RESOLVED | §4 显式标注 Qwen2.5-7B-Instruct，ESJ Qwen3-8B 交叉验证确认 chance-level (AUROC 0.50-0.55)，Limitations 更新 |\n| N4 | Landesberg 区分不足 | ✅ RESOLVED | §2 扩展为 4 维度系统对比（domain/mechanism/granularity/prescriptive），Table 1 新增 failure mechanism 行 |\n| N5 | Epoch confound 削弱正面结果 | ✅ RESOLVED | Abstract 限定 \"under 3-epoch training; diminishes to +0.09pp at convergence\"，§7.5 完整呈现 94%/77% reduction |\n\n### Should-Fix（4/6 RESOLVED, 2 open — response-letter items）\n\n| ID | Issue | R42 Status | 说明 |\n|----|-------|-----------|------|\n| W1 | Diagnostic/prescriptive 不一致 | ✅ RESOLVED | 全文统一为 \"primarily diagnostic with limited predictive power\" |\n| W2 | 2-3 seeds 统计推断力不足 | ⚪ OPEN | Response-letter item，论文未修改 |\n| W3 | RE/SQL 扩展过薄 | ✅ RESOLVED | Abstract \"preliminary RE (n=397) and SQL (n=196) pilots\" 措辞充分 |\n| W4 | Related Work 遗漏 | ✅ RESOLVED | Eikema et al. (2025), li2026rewardtail, desai2020calibration, xiao2022uncertainty 全部添加 |\n| W5 | Entity-level 增量论证不足 | ⚪ OPEN | Response-letter item，论文未修改 |\n| W6 | Free-form ablation 不足 | ✅ RESOLVED | 扩展到 SciERC + CoNLL + Few-NERD（LP std ratio 0.86×-1.00×），Discussion 引用跨数据集证据 |\n\n---\n\n## Strengths（承袭 R41 + R42 新增）\n\n1. **研究问题重要且定位精准**：SC 在结构化预测上失败的诊断分析填补社区空白。[R1, R2 共识，承袭]\n\n2. **实验极其详尽且透明**：4 数据集 × 2 模型家族 × 5 信号 × 9 方法类别，59 个 tables + 11 个 figures 的附录，统计检验覆盖面在 NLP 实证研究中属上乘。[R1, R2 共识，承袭]\n\n3. **Degeneracy 概念有实证价值**：12-68% 的 NER 实例产生相同 entity set，作为 pre-deployment check 有应用价值。[R1, R2 共识，承袭]\n\n4. **MBR decoding 理论连接**：Proposition 1 将 entity construction 形式化为 MBR 特例，理论锚点清晰。Eikema et al. (2025) 引用增强了文献连接。[R1, R2 共识，承袭+增强]\n\n5. **R42 修改质量高**：所有 Must-Fix 修改实质性地解决了问题，而非表面应付。特别是 bound 重定位（从定量预测工具到必要条件筛选器）、双 p 值透明报告、ESJ 跨模型验证均展示了良好的学术回应态度。[R1, R2 共识，R42 新增]\n\n6. **Negative results 诚实报告**：明确报告 cross-dataset transfer 失败、RE 局限、epoch confound。Appendix ah 自审 12 个 potential objections。[R2，承袭]\n\n7. **Reproducibility 高**：承诺开源代码/checkpoint/数据，超参数报告详尽。[R1, R2 共识，承袭]\n\n---\n\n## Remaining Weaknesses\n\n### R42 新发现问题（2 项）\n\n**NEW-1** [R1 AGREE, R2] **Abstract 数值引用不一致** (warning)\n- Abstract: \"Entity-level construction yields conditional gains (+1.40pp on Few-NERD under 3-epoch training; diminishes to +0.09pp at convergence)\"\n- +1.40pp 是 LP-weighted entity construction 在 3-epoch 下的数字（§7.5 line 108）\n- +0.09pp 是 **LP selection**（非 entity construction）在 5-epoch 下的数字（§7.5 line 115: \"LP selection: +1.39→+0.09±0.04pp\"）\n- Entity construction 在 5-epoch 下实际为 +0.20pp（§7.5: \"entity construction: +0.88→+0.20pp\"）\n- 同一句中混淆了两个不同 metric，读者会误认为 entity construction 从 +1.40pp 降至 +0.09pp\n- **建议**：修正为 \"+1.40pp...diminishes to +0.20pp at convergence\" 或拆分两个 metric 分别报告\n\n**NEW-2** [R1 AGREE, R2] **§7.5 entity construction 3-epoch 数字不一致** (info)\n- §7.5 Prescriptive Results: \"LP-weighted construction yields +1.40±0.51pp\"（line 108）\n- §7.5 Training convergence: \"entity construction: +0.88→+0.20pp, 77% reduction\"（line 115）\n- 同一 subsection 中 3-epoch entity construction 数字出现 +1.40pp 和 +0.88pp 两个不同值\n- 如果 +1.40pp 是 LP-weighted 而 +0.88pp 是 uniform，两段应明确标注变体名称；如果指同一方法则存在矛盾\n- **建议**：统一标注变体名称（LP-weighted vs uniform vs mean across variants）\n\n### R41 遗留未修改问题（2 项 open Should-Fix + 2 项 divergence）\n\n**W2** [承袭] 2-3 seeds 统计推断力不足 — Response-letter item\n\n**W5** [承袭] Entity-level decomposition 增量贡献需更强论证 — Response-letter item\n\n**D1** [持续分歧] 标题 \"Why SC Fails for NER\" 与内容匹配度 — R2 认为 \"Why\" 暗示因果，R1 REBUT NLP 惯例\n\n**D2** [持续分歧] 正文数字密度过高 — R2 认为影响可读性，R1 认为诊断论文属性\n\n---\n\n## Questions（R42 新增/更新）\n\n1. Abstract 中 \"+0.09pp at convergence\" 是否应改为 \"+0.20pp\"（entity construction 的 5-epoch 数字）？当前措辞混淆了 LP selection 和 entity construction。[R1, R2 共识]\n2. §7.5 中 \"+1.40pp\" (LP-weighted) 与 \"+0.88pp\" (generic entity construction) 的关系是什么？如果是不同变体，77% reduction 的基线应该是 +1.40 还是 +0.88？[R1, R2 共识]\n3. 5-epoch LP-weighted construction 的具体数字是多少？当前只报告了 generic entity construction 的 +0.20pp。[R1]\n\n---\n\n## Missing References\n\nR41 指出的遗漏（Eikema et al. 2025, calibration literature, TTS advances）已全部修复。R42 无新的遗漏引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿（状态：not_requested）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 ~4 分钟）\n\n| 严重度 | 页面 | 发现 |\n|--------|------|------|\n| 🔴 critical | p.23 | 几乎空白页：仅顶部 9 行文字，其余 ~85% 空白。应将该段文字合并到前一页或后一页 |\n| ⚠️ warning | p.7 | 三个 display items（Figure 3 + Figure 4 + Table 5）挤在同一页，Figure 尺寸偏小，轴标签接近可读性下限 |\n| ⚠️ warning | p.2 | Figure 1 内部注释文字偏小（AUROC=0.82 等），可能低于正文字号 70% |\n| ℹ️ info | p.15 | Figure 7 热力图灰度打印时区分度下降 |\n| ℹ️ info | p.8 | 主文最后一页纯文本无 display item（Discussion/Conclusion 可接受） |\n| ℹ️ info | p.46 | Table 69 文字约 6-7pt，辨认困难 |\n| ℹ️ info | p.12 | Figure 5 字号偏小但可读 |\n| ℹ️ info | pp.12-47 | 附录 36 页，建议开头加导读段落帮助审稿人定位 |\n\n1 critical（Appendix 空白页）, 2 warning, 5 info。主文排版无阻断问题。Appendix 空白页属排版优化项。\n\n---\n\n## Score Divergence Analysis\n\n### R1 评分：4.0 (Conference)\n**升分理由**：\n- 所有 5 个 Must-Fix 修改质量高，展示了对审稿意见的深入理解\n- Bound 重定位从 overselling 转为诚实的 necessary condition screen，是正确的学术定位\n- ESJ 跨模型验证和 free-form ablation 跨数据集扩展增强了证据链\n- Diagnostic framework 本身（degeneracy + signal alignment collapse）具有独立贡献，不依赖 prescriptive 成功\n\n### R2 评分：3.5 (Borderline Conference)\n**维持理由**（R2 未提交交叉回应，以下基于 R2 初审立场）：\n1. Concurrent work (Landesberg) 虽已充分区分，但 correlation-selection gap 概念的 novelty increment 仍受限于独立发现\n2. Entity construction 正面结果高度条件化（3-epoch only, Few-NERD only），实际 practitioner 影响有限\n3. 标题 \"Why SC Fails\" 仍略 overpromise 论文所能提供的因果解释\n\n### R1 交叉回应摘要\n- **REBUT R2 理由 1**（concurrent work）：Landesberg 处理 reasoning，本文处理 structured prediction，failure mechanism 完全不同（degeneracy + α 是 NER-specific），互为补充而非重叠\n- **PARTIALLY AGREE R2 理由 2**（limited impact）：承认 prescriptive 贡献有限，但 diagnostic 框架和 degeneracy 概念独立成立\n- **REBUT R2 理由 3**（title）：\"Why X Fails\" 是 NLP 标准范式，不暗示严格因果\n- **AGREE NEW-1, NEW-2**：数值不一致确实存在，应修正\n\n### Director 判断\n分歧核心是贡献显著性的主观评估，非事实性争议。R2 的关注点（novelty increment、conditional impact）是结构性的，反映论文的内在 scope 而非修改质量。R1 的升分有充分理由——修改确实解决了所有可修改的问题。0.5 分差距记录为 split decision。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4 / 5\n**相较 R41 变化**: 维持 3.5，但从 \"weak 3.5\" 提升至 \"strong 3.5\"（R1 升至 4.0 表明修改有效）\n\n### 维度分数\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4.0 | 3.5 | 3.5 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n### 评分理由\n\n论文在 R42 中展示了对所有 R41 Must-Fix 的高质量修改回应。5 个 critical issues 全部 RESOLVED：bound 重定位为 screening test、统计透明度显著提升、probe 模型差异已显式披露并交叉验证、concurrent work 系统对比完整、epoch confound 坦诚呈现。这些修改将论文从 \"weak 3.5\" 提升至 \"strong 3.5 / borderline 4.0\"。\n\n维持 3.5 而非升至 4.0 的原因：\n1. **Prescriptive 贡献高度条件化**：唯一超过 1pp 的正面结果（+1.40pp）限于 Few-NERD 3-epoch，5-epoch 下降 77-94%。论文已坦诚处理此局限，但这意味着 practitioner 的 actionable takeaway 主要是 \"SC 对 NER 基本无效\"——一个有价值但 excitement 有限的负面结论。\n2. **Concurrent discovery 限制 novelty premium**：Landesberg 独立发现 correlation-selection gap。虽然两个工作在 domain、mechanism、granularity 上有实质差异，但核心概念的 novelty 不可避免地被分摊。\n3. **两个新发现的数值不一致**（NEW-1, NEW-2）虽为 minor，但出现在 Abstract 和主要结果段，需要修正。\n\n论文的 lower bound 为 3.0 (Findings)：负面发现的系统性文档、degeneracy 概念、极其详尽的实验设计有独立价值。R1 的 4.0 评估合理反映了修改后论文的 soundness 和 transparency 提升。最终建议 **3.5 (Borderline Conference)**，论文有望通过 Findings 接收。\n\n### 与 R41 的进步\n\nR41 → R42 的主要进步：\n- 5/5 Must-Fix 全部解决（R41: 全部 open → R42: 全部 resolved）\n- 4/6 Should-Fix 解决（R41: 全部 open → R42: 4 resolved, 2 response-letter）\n- Soundness 从 R1=3.5/R2=3.5 提升至 R1=4.0/R2=3.5\n- Abstract 从 unconditional claims 改为 transparent conditional reporting\n- 统计报告从 cherry-picked 改为三重校正全部透明呈现\n- 新增实验证据：ESJ Qwen3-8B 交叉验证、free-form ablation 跨 3 数据集\n\n### 遗留问题清单\n\n需在下轮或 camera-ready 中处理：\n1. **NEW-1** (warning): Abstract \"+0.09pp\" 应改为 \"+0.20pp\" 或分别报告两个 metric\n2. **NEW-2** (info): §7.5 明确标注 LP-weighted vs uniform construction 变体\n3. **W2** (response-letter): 3 seeds 统计推断力的讨论\n4. **W5** (response-letter): Entity-level vs task-level 增量论证\n5. **D1** (divergence): 标题匹配度\n6. **Visual p.23**: Appendix 空白页消除\n\n---\n\n## Detailed Comments\n\n### §Abstract\n- R41 修改验证：条件限定（\"under 3-epoch training\"）到位\n- **NEW-1**：\"+0.09pp at convergence\" 应为 \"+0.20pp\"（entity construction）或需拆分 metric → 必须修正\n- 双 p 值报告（per-family 0.006, global 0.055）透明度好\n\n### §2 Related Work\n- R41 修改验证：Landesberg 4 维度系统对比（domain/mechanism/granularity/prescriptive）充分\n- Table 1 新增 failure mechanism 行，七维度对比清晰\n- Eikema et al. (2025), calibration literature, TTS advances 全部添加\n- \"Concurrent work\" 段落措辞平衡，认可 Landesberg 的独立发现\n\n### §4 Where Single-Signal Selection Fails\n- R41 修改验证：probe 模型标注到位（\"Probing experiments on Qwen2.5-7B-Instruct\"）\n- Qwen3-8B ESJ 交叉验证（AUROC 0.50-0.55）确认 introspection boundary 跨模型一致\n- \"Cross-model validation\" 新段落增强了证据链\n\n### §6.3 Degeneracy Decomposition\n- R41 修改验证：重定位成功——\"intentionally loose necessary condition test\"、\"screening for favorable conditions rather than quantitatively predicting gains\"\n- \"the low recovery ratio (3-12%) reflects its role as a screening test, not a tight estimate\" 措辞恰当\n- Bound looseness 段落新增（split-half correlation、conservative α estimation）增加了透明度\n\n### §7.5 Prescriptive Results\n- R41 修改验证：family 划分先验理由到位（\"reflecting mechanistic distinctions defined at experiment design time (not selected post-hoc)\"）\n- \"the family partition was not pre-registered\" 声明诚实\n- 三重校正透明报告（global/per-family/BH FDR）是优秀的统计实践\n- **NEW-2**：+1.40pp (LP-weighted) vs +0.88pp (generic construction) 需要区分标注\n- \"Training convergence modulates scaling returns\" 新段落完整呈现 epoch confound\n\n### §8 Discussion/Conclusion\n- \"LP std ratio 0.86-1.00× across three datasets\" 引用跨数据集 free-form ablation 证据\n- 定位与 Abstract 一致（diagnostic framework 为 primary contribution）\n\n### Limitations\n- R41 修改验证：probe 模型差异显式披露 + ESJ Qwen3-8B 复制\n- Free-form ablation 扩展到 3 数据集\n- 双 p 值引用\n- 覆盖度充分，长度适当",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 42 (Continue)\n\n**论文**: \"Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性; R2: 新颖性/完整性）\n**审稿模式**: 继续审稿（基于 R41 修改验证）\n**交叉分享**: R1 完成交叉回应；R2 未返回（经多轮等待），视为维持立场\n\n---\n\n## Summary\n\nRound 42 是对 R41 提出的 5 个 Must-Fix、6 个 Should-Fix 的修改验证轮。论文对全部 5 个 Must-Fix 进行了实质性修改：§6.3 将 bound 重定位为 necessary condition screening test；§7.5 透明报告双重 p 值并提供 family 划分先验理由；§4 标注 probe 模型差异并新增 Qwen3-8B ESJ 交叉验证；§2 扩展 Landesberg 系统对比为 4 维度 + Table 1 增加 failure mechanism 行；Abstract 对 +1.40pp 加入 3-epoch 条件限定。Should-Fix 中 4 项（W1 叙事定位、W3 RE/SQL 措辞、W4 缺失引用、W6 free-form ablation）已修复。\n\n两位 Reviewer 对所有 R41 Must-Fix 修改验证为 RESOLVED。评分分歧：R1 升至 4.0 (Conference)，R2 维持 3.5 (Borderline Conference)。修改引入两个新发现的数值不一致问题。\n\n---\n\n## R41 Issue Resolution Status\n\n### Must-Fix（5/5 RESOLVED）\n\n| ID | Issue | R42 Status | 说明 |\n|----|-------|-----------|------|\n| N1 | Bound 仅恢复 3-12% | ✅ RESOLVED | §6.3 成功重定位为 \"intentionally loose necessary condition test\"，不再 oversell |\n| N2 | 统计显著性依赖校正方案 | ✅ RESOLVED | §7.5 双 p 值透明报告（global 0.055, per-family 0.006），family 划分有先验理由，明确声明 not pre-registered |\n| N3 | Probe 模型不一致 | ✅ RESOLVED | §4 显式标注 Qwen2.5-7B-Instruct，ESJ Qwen3-8B 交叉验证确认 chance-level (AUROC 0.50-0.55)，Limitations 更新 |\n| N4 | Landesberg 区分不足 | ✅ RESOLVED | §2 扩展为 4 维度系统对比（domain/mechanism/granularity/prescriptive），Table 1 新增 failure mechanism 行 |\n| N5 | Epoch confound 削弱正面结果 | ✅ RESOLVED | Abstract 限定 \"under 3-epoch training; diminishes to +0.09pp at convergence\"，§7.5 完整呈现 94%/77% reduction |\n\n### Should-Fix（4/6 RESOLVED, 2 open — response-letter items）\n\n| ID | Issue | R42 Status | 说明 |\n|----|-------|-----------|------|\n| W1 | Diagnostic/prescriptive 不一致 | ✅ RESOLVED | 全文统一为 \"primarily diagnostic with limited predictive power\" |\n| W2 | 2-3 seeds 统计推断力不足 | ⚪ OPEN | Response-letter item，论文未修改 |\n| W3 | RE/SQL 扩展过薄 | ✅ RESOLVED | Abstract \"preliminary RE (n=397) and SQL (n=196) pilots\" 措辞充分 |\n| W4 | Related Work 遗漏 | ✅ RESOLVED | Eikema et al. (2025), li2026rewardtail, desai2020calibration, xiao2022uncertainty 全部添加 |\n| W5 | Entity-level 增量论证不足 | ⚪ OPEN | Response-letter item，论文未修改 |\n| W6 | Free-form ablation 不足 | ✅ RESOLVED | 扩展到 SciERC + CoNLL + Few-NERD（LP std ratio 0.86×-1.00×），Discussion 引用跨数据集证据 |\n\n---\n\n## Strengths（承袭 R41 + R42 新增）\n\n1. **研究问题重要且定位精准**：SC 在结构化预测上失败的诊断分析填补社区空白。[R1, R2 共识，承袭]\n\n2. **实验极其详尽且透明**：4 数据集 × 2 模型家族 × 5 信号 × 9 方法类别，59 个 tables + 11 个 figures 的附录，统计检验覆盖面在 NLP 实证研究中属上乘。[R1, R2 共识，承袭]\n\n3. **Degeneracy 概念有实证价值**：12-68% 的 NER 实例产生相同 entity set，作为 pre-deployment check 有应用价值。[R1, R2 共识，承袭]\n\n4. **MBR decoding 理论连接**：Proposition 1 将 entity construction 形式化为 MBR 特例，理论锚点清晰。Eikema et al. (2025) 引用增强了文献连接。[R1, R2 共识，承袭+增强]\n\n5. **R42 修改质量高**：所有 Must-Fix 修改实质性地解决了问题，而非表面应付。特别是 bound 重定位（从定量预测工具到必要条件筛选器）、双 p 值透明报告、ESJ 跨模型验证均展示了良好的学术回应态度。[R1, R2 共识，R42 新增]\n\n6. **Negative results 诚实报告**：明确报告 cross-dataset transfer 失败、RE 局限、epoch confound。Appendix ah 自审 12 个 potential objections。[R2，承袭]\n\n7. **Reproducibility 高**：承诺开源代码/checkpoint/数据，超参数报告详尽。[R1, R2 共识，承袭]\n\n---\n\n## Remaining Weaknesses\n\n### R42 新发现问题（2 项）\n\n**NEW-1** [R1 AGREE, R2] **Abstract 数值引用不一致** (warning)\n- Abstract: \"Entity-level construction yields conditional gains (+1.40pp on Few-NERD under 3-epoch training; diminishes to +0.09pp at convergence)\"\n- +1.40pp 是 LP-weighted entity construction 在 3-epoch 下的数字（§7.5 line 108）\n- +0.09pp 是 **LP selection**（非 entity construction）在 5-epoch 下的数字（§7.5 line 115: \"LP selection: +1.39→+0.09±0.04pp\"）\n- Entity construction 在 5-epoch 下实际为 +0.20pp（§7.5: \"entity construction: +0.88→+0.20pp\"）\n- 同一句中混淆了两个不同 metric，读者会误认为 entity construction 从 +1.40pp 降至 +0.09pp\n- **建议**：修正为 \"+1.40pp...diminishes to +0.20pp at convergence\" 或拆分两个 metric 分别报告\n\n**NEW-2** [R1 AGREE, R2] **§7.5 entity construction 3-epoch 数字不一致** (info)\n- §7.5 Prescriptive Results: \"LP-weighted construction yields +1.40±0.51pp\"（line 108）\n- §7.5 Training convergence: \"entity construction: +0.88→+0.20pp, 77% reduction\"（line 115）\n- 同一 subsection 中 3-epoch entity construction 数字出现 +1.40pp 和 +0.88pp 两个不同值\n- 如果 +1.40pp 是 LP-weighted 而 +0.88pp 是 uniform，两段应明确标注变体名称；如果指同一方法则存在矛盾\n- **建议**：统一标注变体名称（LP-weighted vs uniform vs mean across variants）\n\n### R41 遗留未修改问题（2 项 open Should-Fix + 2 项 divergence）\n\n**W2** [承袭] 2-3 seeds 统计推断力不足 — Response-letter item\n\n**W5** [承袭] Entity-level decomposition 增量贡献需更强论证 — Response-letter item\n\n**D1** [持续分歧] 标题 \"Why SC Fails for NER\" 与内容匹配度 — R2 认为 \"Why\" 暗示因果，R1 REBUT NLP 惯例\n\n**D2** [持续分歧] 正文数字密度过高 — R2 认为影响可读性，R1 认为诊断论文属性\n\n---\n\n## Questions（R42 新增/更新）\n\n1. Abstract 中 \"+0.09pp at convergence\" 是否应改为 \"+0.20pp\"（entity construction 的 5-epoch 数字）？当前措辞混淆了 LP selection 和 entity construction。[R1, R2 共识]\n2. §7.5 中 \"+1.40pp\" (LP-weighted) 与 \"+0.88pp\" (generic entity construction) 的关系是什么？如果是不同变体，77% reduction 的基线应该是 +1.40 还是 +0.88？[R1, R2 共识]\n3. 5-epoch LP-weighted construction 的具体数字是多少？当前只报告了 generic entity construction 的 +0.20pp。[R1]\n\n---\n\n## Missing References\n\nR41 指出的遗漏（Eikema et al. 2025, calibration literature, TTS advances）已全部修复。R42 无新的遗漏引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿（状态：not_requested）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 ~4 分钟）\n\n| 严重度 | 页面 | 发现 |\n|--------|------|------|\n| 🔴 critical | p.23 | 几乎空白页：仅顶部 9 行文字，其余 ~85% 空白。应将该段文字合并到前一页或后一页 |\n| ⚠️ warning | p.7 | 三个 display items（Figure 3 + Figure 4 + Table 5）挤在同一页，Figure 尺寸偏小，轴标签接近可读性下限 |\n| ⚠️ warning | p.2 | Figure 1 内部注释文字偏小（AUROC=0.82 等），可能低于正文字号 70% |\n| ℹ️ info | p.15 | Figure 7 热力图灰度打印时区分度下降 |\n| ℹ️ info | p.8 | 主文最后一页纯文本无 display item（Discussion/Conclusion 可接受） |\n| ℹ️ info | p.46 | Table 69 文字约 6-7pt，辨认困难 |\n| ℹ️ info | p.12 | Figure 5 字号偏小但可读 |\n| ℹ️ info | pp.12-47 | 附录 36 页，建议开头加导读段落帮助审稿人定位 |\n\n1 critical（Appendix 空白页）, 2 warning, 5 info。主文排版无阻断问题。Appendix 空白页属排版优化项。\n\n---\n\n## Score Divergence Analysis\n\n### R1 评分：4.0 (Conference)\n**升分理由**：\n- 所有 5 个 Must-Fix 修改质量高，展示了对审稿意见的深入理解\n- Bound 重定位从 overselling 转为诚实的 necessary condition screen，是正确的学术定位\n- ESJ 跨模型验证和 free-form ablation 跨数据集扩展增强了证据链\n- Diagnostic framework 本身（degeneracy + signal alignment collapse）具有独立贡献，不依赖 prescriptive 成功\n\n### R2 评分：3.5 (Borderline Conference)\n**维持理由**（R2 未提交交叉回应，以下基于 R2 初审立场）：\n1. Concurrent work (Landesberg) 虽已充分区分，但 correlation-selection gap 概念的 novelty increment 仍受限于独立发现\n2. Entity construction 正面结果高度条件化（3-epoch only, Few-NERD only），实际 practitioner 影响有限\n3. 标题 \"Why SC Fails\" 仍略 overpromise 论文所能提供的因果解释\n\n### R1 交叉回应摘要\n- **REBUT R2 理由 1**（concurrent work）：Landesberg 处理 reasoning，本文处理 structured prediction，failure mechanism 完全不同（degeneracy + α 是 NER-specific），互为补充而非重叠\n- **PARTIALLY AGREE R2 理由 2**（limited impact）：承认 prescriptive 贡献有限，但 diagnostic 框架和 degeneracy 概念独立成立\n- **REBUT R2 理由 3**（title）：\"Why X Fails\" 是 NLP 标准范式，不暗示严格因果\n- **AGREE NEW-1, NEW-2**：数值不一致确实存在，应修正\n\n### Director 判断\n分歧核心是贡献显著性的主观评估，非事实性争议。R2 的关注点（novelty increment、conditional impact）是结构性的，反映论文的内在 scope 而非修改质量。R1 的升分有充分理由——修改确实解决了所有可修改的问题。0.5 分差距记录为 split decision。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4 / 5\n**相较 R41 变化**: 维持 3.5，但从 \"weak 3.5\" 提升至 \"strong 3.5\"（R1 升至 4.0 表明修改有效）\n\n### 维度分数\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4.0 | 3.5 | 3.5 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n### 评分理由\n\n论文在 R42 中展示了对所有 R41 Must-Fix 的高质量修改回应。5 个 critical issues 全部 RESOLVED：bound 重定位为 screening test、统计透明度显著提升、probe 模型差异已显式披露并交叉验证、concurrent work 系统对比完整、epoch confound 坦诚呈现。这些修改将论文从 \"weak 3.5\" 提升至 \"strong 3.5 / borderline 4.0\"。\n\n维持 3.5 而非升至 4.0 的原因：\n1. **Prescriptive 贡献高度条件化**：唯一超过 1pp 的正面结果（+1.40pp）限于 Few-NERD 3-epoch，5-epoch 下降 77-94%。论文已坦诚处理此局限，但这意味着 practitioner 的 actionable takeaway 主要是 \"SC 对 NER 基本无效\"——一个有价值但 excitement 有限的负面结论。\n2. **Concurrent discovery 限制 novelty premium**：Landesberg 独立发现 correlation-selection gap。虽然两个工作在 domain、mechanism、granularity 上有实质差异，但核心概念的 novelty 不可避免地被分摊。\n3. **两个新发现的数值不一致**（NEW-1, NEW-2）虽为 minor，但出现在 Abstract 和主要结果段，需要修正。\n\n论文的 lower bound 为 3.0 (Findings)：负面发现的系统性文档、degeneracy 概念、极其详尽的实验设计有独立价值。R1 的 4.0 评估合理反映了修改后论文的 soundness 和 transparency 提升。最终建议 **3.5 (Borderline Conference)**，论文有望通过 Findings 接收。\n\n### 与 R41 的进步\n\nR41 → R42 的主要进步：\n- 5/5 Must-Fix 全部解决（R41: 全部 open → R42: 全部 resolved）\n- 4/6 Should-Fix 解决（R41: 全部 open → R42: 4 resolved, 2 response-letter）\n- Soundness 从 R1=3.5/R2=3.5 提升至 R1=4.0/R2=3.5\n- Abstract 从 unconditional claims 改为 transparent conditional reporting\n- 统计报告从 cherry-picked 改为三重校正全部透明呈现\n- 新增实验证据：ESJ Qwen3-8B 交叉验证、free-form ablation 跨 3 数据集\n\n### 遗留问题清单\n\n需在下轮或 camera-ready 中处理：\n1. **NEW-1** (warning): Abstract \"+0.09pp\" 应改为 \"+0.20pp\" 或分别报告两个 metric\n2. **NEW-2** (info): §7.5 明确标注 LP-weighted vs uniform construction 变体\n3. **W2** (response-letter): 3 seeds 统计推断力的讨论\n4. **W5** (response-letter): Entity-level vs task-level 增量论证\n5. **D1** (divergence): 标题匹配度\n6. **Visual p.23**: Appendix 空白页消除\n\n---\n\n## Detailed Comments\n\n### §Abstract\n- R41 修改验证：条件限定（\"under 3-epoch training\"）到位\n- **NEW-1**：\"+0.09pp at convergence\" 应为 \"+0.20pp\"（entity construction）或需拆分 metric → 必须修正\n- 双 p 值报告（per-family 0.006, global 0.055）透明度好\n\n### §2 Related Work\n- R41 修改验证：Landesberg 4 维度系统对比（domain/mechanism/granularity/prescriptive）充分\n- Table 1 新增 failure mechanism 行，七维度对比清晰\n- Eikema et al. (2025), calibration literature, TTS advances 全部添加\n- \"Concurrent work\" 段落措辞平衡，认可 Landesberg 的独立发现\n\n### §4 Where Single-Signal Selection Fails\n- R41 修改验证：probe 模型标注到位（\"Probing experiments on Qwen2.5-7B-Instruct\"）\n- Qwen3-8B ESJ 交叉验证（AUROC 0.50-0.55）确认 introspection boundary 跨模型一致\n- \"Cross-model validation\" 新段落增强了证据链\n\n### §6.3 Degeneracy Decomposition\n- R41 修改验证：重定位成功——\"intentionally loose necessary condition test\"、\"screening for favorable conditions rather than quantitatively predicting gains\"\n- \"the low recovery ratio (3-12%) reflects its role as a screening test, not a tight estimate\" 措辞恰当\n- Bound looseness 段落新增（split-half correlation、conservative α estimation）增加了透明度\n\n### §7.5 Prescriptive Results\n- R41 修改验证：family 划分先验理由到位（\"reflecting mechanistic distinctions defined at experiment design time (not selected post-hoc)\"）\n- \"the family partition was not pre-registered\" 声明诚实\n- 三重校正透明报告（global/per-family/BH FDR）是优秀的统计实践\n- **NEW-2**：+1.40pp (LP-weighted) vs +0.88pp (generic construction) 需要区分标注\n- \"Training convergence modulates scaling returns\" 新段落完整呈现 epoch confound\n\n### §8 Discussion/Conclusion\n- \"LP std ratio 0.86-1.00× across three datasets\" 引用跨数据集 free-form ablation 证据\n- 定位与 Abstract 一致（diagnostic framework 为 primary contribution）\n\n### Limitations\n- R41 修改验证：probe 模型差异显式披露 + ESJ Qwen3-8B 复制\n- Free-form ablation 扩展到 3 数据集\n- 双 p 值引用\n- 覆盖度充分，长度适当",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4545 · 2026-05-23T07:20:21.332923+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4630
}
```

</details>

---


### Tool call

_source line 4546 · 2026-05-23T07:20:29.435243+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'R42 初始化 + 初审收集', 'status': 'completed', 'activeForm': '收集 R42 初审'}, {'content': 'R42 Step 1: 收集两位 Reviewer R42 报告', 'status': 'completed', 'activeForm': '收集 Reviewer 报告'}, {'content': 'R42 Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享'}, {'content': 'R42 Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛状态'}, {'content': 'R42 Step 4: 合成报告 + 更新 issue tracker + 投递', 'status': 'completed', 'activeForm': '合成并投递报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'R42 初始化 + 初审收集', 'status': 'completed', 'activeForm': '收集 R42 初审'}, {'content': 'R42 Step 1: 收集两位 Reviewer R42 报告', 'status': 'completed', 'activeForm': '收集 Reviewer 报告'}, {'content': 'R42 Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享'}, {'content': 'R42 Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛状态'}, {'content': 'R42 Step 4: 合成报告 + 更新 issue tracker + 投递', 'status': 'completed', 'activeForm': '合成并投递报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 4547 · 2026-05-23T07:20:29.485884+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 4548 · 2026-05-23T07:20:37.988441+00:00_

R42 审稿报告已投递至 Research Director。

**本轮结论**：
- **评分 3.5 / 5 (Borderline Conference)**，R1 升至 4.0、R2 维持 3.5，split decision
- R41 全部 5 个 Must-Fix 验证通过（RESOLVED），4/6 Should-Fix 已修复
- 新发现 2 个数值不一致：Abstract 混淆 entity construction (+1.40pp) 与 LP selection (+0.09pp)；§7.5 LP-weighted (+1.40pp) 与 generic construction (+0.88pp) 未区分标注
- 修改将论文从 "weak 3.5" 提升至 "strong 3.5 / borderline 4.0"，有望通过 Findings 接收

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 348

## Round 348

4 recorded events


### User

_source line 4549 · 2026-05-23T07:20:39.159211+00:00_

[Reviewer 1 审稿结果]:
回应已提交。核心分歧在于：R2 认为诊断论文需要更强的正面方法结果才能达到 Conference 水平，我认为系统性诊断分析本身——解释一个广泛观察到但未被理解的现象——已具备 Conference 价值。两个新发现的数值不一致（NEW-1, NEW-2）是 minor 修复项。维持 4.0 评分。

---

[Reviewer 2 审稿意见]:

## Reviewer 2 对 R1 评分分歧的回应

---

### Q1: R1 升至 4.0 的 3 个论据是否有效？

**[AGREE] 升分论据 1**（Must-Fix 全部解决）：事实判断正确，我与 R1 在 issue 解决状态上完全一致。但我对其推论持保留意见：解决 Must-Fix 使论文回到"它应有的基线"——R41 的 3.5 是因为有 Must-Fix 问题而被压低的评分，修复后应回到论文"本来"的水平。关键问题是：这篇论文"本来"值 3.5 还是 4.0？R1 认为是 4.0 被问题拖到了 3.5，我认为即使没有这些问题也是 3.5。

**[AGREE] 升分论据 2**（修订展现实质性技术回应）：完全同意——epoch confound 的 reframing 和三重统计校正的透明报告都是高质量的学术回应，超越了 surface-level 修补。但修订质量反映的是作者的学术素养，不改变论文贡献本身的份量。在 single-round 审稿场景中，这些优点会以"论文写得好、方法论严谨"的形式出现，对应 Soundness 加分而非 Overall 加分。

**[AGREE with reservation] 升分论据 3**（Claims-evidence 正确对齐）：这是 R1 最强的论据。R42 版本确实达到了 claims 与 evidence 的良好对齐——没有 overclaim，边界清晰，hedging 恰当。我同意这是 Conference 级论文的**必要条件**。但它不是**充分条件**——一篇 claims 完美校准但贡献有限的论文仍然可能是 Findings 而非 Conference。

---

### Q2: 维持 3.5 的 3 个理由中哪些是决定性的？

**理由 1（核心 insight 并发性）——决定性。** 这是我与 R1 分歧的根本来源。即使 differentiation 现在 convincing（我已标注 RESOLVED），correlation-selection gap 作为概念被 Landesberg (2026) 独立发现这一事实降低了论文的 Excitement 上限。

具体而言：如果没有 Landesberg，本文独立发现 "quality signals predict well but select poorly for structured IE" 并提供 entity-level 分解，这是一个 4.0 甚至 4.5 的发现。但在 Landesberg 已经建立 correlation-selection gap 概念框架的背景下（且是在 reasoning 这个更 mainstream 的场景中），本文的增量贡献变为"这个已知现象在 structured prediction 中也存在，且由不同机制驱动"。这仍然有价值，但从 "discovering a new phenomenon" 降级为 "extending a known phenomenon to a new domain with mechanistic analysis"。这一区分直接影响 Excitement 评分。

R1 可能的反驳是 concurrent discovery 是常见的、不应惩罚任何一方。我同意不应"惩罚"，但 Excitement 评分反映的是论文对读者的信息增量——一个读过 Landesberg 的读者从本文获得的增量（entity-level 机制分析）小于一个没有先验知识的读者获得的增量（整个 gap 发现 + 机制分析）。

**理由 2（有限实际影响）——支撑性但非决定性。** +1.10pp conditional 且 global p_adj=0.055 的改进不足以作为独立卖点，但论文已正确定位为诊断研究而非方法论文。如果论文完全放弃正面改进的 claim（纯负面结果 + 诊断框架），我可能反而更倾向 4.0——因为 clean negative result 的价值不取决于实际改进幅度。但论文仍然试图 claim entity construction 的正面结果（即使 properly caveated），这使得 limited impact 成为一个削弱因素。

**理由 3（标题 overclaim）——非决定性。** 标题是风格选择，不应影响实质性评分。撤回此理由。

---

### Q3: Soundness 从 3.5 升至 4.0 的判断？

**[AGREE]** 同意 Soundness 升至 4.0。

R42 的方法论达到了 "Strong: provides sufficient support for all of its claims" 的标准：
- 三重统计校正透明报告 + 非预注册声明 → 超越 NLP 领域标准实践
- Epoch confound 完整量化 → 对自身结果的潜在威胁主动披露
- Claims 正确对齐 evidence → 没有无实验支撑的 claim
- 4 数据集 × 2 模型家族 × 多种子 + TOST + bootstrap CI → 实验设计严谨

唯一阻止 Soundness=4.5 的因素：probe 仍在 Qwen2.5-7B 上（虽然现在有 Qwen3-8B ESJ 交叉验证——这是 R1 提到的改进，我在 R42 review 中可能遗漏了），RE/SQL 仍然太初步。

**我的 R42 维度更新**：

| 维度 | R41 | R42 | 变化理由 |
|------|-----|-----|--------|
| Soundness | 3.5 | 4.0 | 同意 R1：Must-Fix 解决 + 统计报告达最佳实践 |
| Excitement | 2.5 | 3.0 | Epoch confound 作为 finding 增加了贡献，但并发性仍限制上限 |
| Overall | 3.5 | 3.5 | Soundness↑ 被 Excitement 限制所抵消 |

**分歧核心**：R1 给 Excitement 3.5，我给 3.0。这 0.5 的差异驱动了 Overall 的分歧（R1: 4.0, R2: 3.5）。Excitement 是主观维度——R1 可能认为 well-documented negative result 对社区的价值比我评估的更高。这是合理的主观分歧，不涉及事实判断差异。

---

### Q4: NEW-1/NEW-2 数值不一致是否影响评分？

**不影响。**

NEW-1（§7.5 的 +0.09 vs Table 58 的 +0.12）和 NEW-2（entity construction +1.10 vs +0.88）是数值报告的 inconsistency，不影响论文的核心结论：
- 无论是 0.09 还是 0.12，5-epoch 下的 LP 收益都接近零（vs. 3-epoch 的 +1.39）——epoch confound 的结论不变
- 无论是 +1.10 还是+0.88，entity construction 的收益都是 modest 且 conditional——核心判断不变

这些是 camera-ready 阶段应修正的 typo 级别问题，不影响 Soundness 或 Overall 评分。

---

### 对 R1 发现的新问题的回应

R1 发现 §4 "AUROC 0.50-0.55" vs §5 "AUROC 0.50-0.52"：同意这是 minor inconsistency，可能源于不同实验子集（entity-level vs class-level AUROC，或不同数据集范围）。应在 camera-ready 中明确标注来源。不影响评分。

---

### 最终立场

**Overall 3.5 维持不变。**

我承认 4.0 是一个合理的评分——R1 的论据在逻辑上是自洽的。分歧的根源是 Excitement 的主观权重：

- 如果你认为"structured IE 中 SC 失效的系统性文档记录 + entity-level 诊断框架"对 NLP 社区的信息价值高于"一个已知现象在新领域的机制分析"，那么 4.0 是合理的。
- 如果你认为在 Landesberg 已建立 gap 框架的背景下，本文的增量贡献（entity-level 分解 + 机制分析）属于 "solid but incremental extension"，那么 3.5 是合理的。

**对 AC 的建议**：分歧幅度（0.5 分）在正常范围内，且双方在 issue 解决状态和 Soundness 评分上完全一致。Overall 3.5-4.0 的范围意味着论文处于 Conference 和 strong Findings 之间——无论最终决定是 Conference accept 还是 Findings accept，都不会是错误判断。


---

[Reviewer 2 审稿结果]:
回应已提交。

核心分歧总结：R1 和我在所有事实判断上一致（issue 状态、Soundness 4.0），分歧仅在 Excitement（R1: 3.5, R2: 3.0），源于对 concurrent discovery 如何影响论文信息增量的不同权重。Overall 3.5-4.0 的范围意味着 Conference 或 strong Findings 均为合理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 4550 · 2026-05-23T07:23:38.456995+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 42 (Continue)\n\n**论文**: \"Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性; R2: 新颖性/完整性）\n**审稿模式**: 继续审稿（基于 R41 修改验证）\n**交叉分享**: R1, R2 均完成交叉回应，达成部分共识\n\n---\n\n## Summary\n\nRound 42 是对 R41 提出的 5 个 Must-Fix、6 个 Should-Fix 的修改验证轮。论文对全部 5 个 Must-Fix 进行了实质性修改：§6.3 将 bound 重定位为 necessary condition screening test；§7.5 透明报告双重 p 值并提供 family 划分先验理由；§4 标注 probe 模型差异并新增 Qwen3-8B ESJ 交叉验证；§2 扩展 Landesberg 系统对比为 4 维度 + Table 1 增加 failure mechanism 行；Abstract 对 +1.40pp 加入 3-epoch 条件限定。Should-Fix 中 4 项（W1 叙事定位、W3 RE/SQL 措辞、W4 缺失引用、W6 free-form ablation）已修复。\n\n两位 Reviewer 对所有 R41 Must-Fix 验证为 RESOLVED，Soundness 达成共识升至 4.0。评分分歧：R1=4.0 (Conference)，R2=3.5 (Borderline Conference)。分歧根源为 Excitement 的主观权重——R2 认为 concurrent discovery (Landesberg 2026) 限制了 novelty increment，R1 认为诊断框架的系统性分析具有独立 Conference 价值。双方明确认为 3.5-4.0 均为合理评分。\n\n---\n\n## R41 Issue Resolution Status\n\n### Must-Fix（5/5 RESOLVED — 双方共识）\n\n| ID | Issue | R42 Status | 说明 |\n|----|-------|-----------|------|\n| N1 | Bound 仅恢复 3-12% | ✅ RESOLVED | §6.3 成功重定位为 \"intentionally loose necessary condition test\"，不再 oversell |\n| N2 | 统计显著性依赖校正方案 | ✅ RESOLVED | §7.5 双 p 值透明报告（global 0.055, per-family 0.006），family 划分有先验理由，明确声明 not pre-registered |\n| N3 | Probe 模型不一致 | ✅ RESOLVED | §4 显式标注 Qwen2.5-7B-Instruct，ESJ Qwen3-8B 交叉验证确认 chance-level (AUROC 0.50-0.55)，Limitations 更新 |\n| N4 | Landesberg 区分不足 | ✅ RESOLVED | §2 扩展为 4 维度系统对比（domain/mechanism/granularity/prescriptive），Table 1 新增 failure mechanism 行 |\n| N5 | Epoch confound 削弱正面结果 | ✅ RESOLVED | Abstract 限定 \"under 3-epoch training; diminishes at convergence\"，§7.5 完整呈现 94%/77% reduction |\n\n### Should-Fix（4/6 RESOLVED, 2 open — response-letter items）\n\n| ID | Issue | R42 Status | 说明 |\n|----|-------|-----------|------|\n| W1 | Diagnostic/prescriptive 不一致 | ✅ RESOLVED | 全文统一为 \"primarily diagnostic with limited predictive power\" |\n| W2 | 2-3 seeds 统计推断力不足 | ⚪ OPEN | Response-letter item，论文未修改 |\n| W3 | RE/SQL 扩展过薄 | ✅ RESOLVED | Abstract \"preliminary RE (n=397) and SQL (n=196) pilots\" 措辞充分 |\n| W4 | Related Work 遗漏 | ✅ RESOLVED | Eikema et al. (2025), li2026rewardtail, desai2020calibration, xiao2022uncertainty 全部添加 |\n| W5 | Entity-level 增量论证不足 | ⚪ OPEN | Response-letter item，论文未修改 |\n| W6 | Free-form ablation 不足 | ✅ RESOLVED | 扩展到 SciERC + CoNLL + Few-NERD（LP std ratio 0.86×-1.00×），Discussion 引用跨数据集证据 |\n\n---\n\n## Strengths（承袭 R41 + R42 新增）\n\n1. **研究问题重要且定位精准**：SC 在结构化预测上失败的诊断分析填补社区空白。[R1, R2 共识，承袭]\n\n2. **实验极其详尽且透明**：4 数据集 × 2 模型家族 × 5 信号 × 9 方法类别，59 个 tables + 11 个 figures 的附录，统计检验覆盖面在 NLP 实证研究中属上乘。三重统计校正透明报告 + 非预注册声明超越 NLP 领域标准实践。[R1, R2 共识，承袭+R42增强]\n\n3. **Degeneracy 概念有实证价值**：12-68% 的 NER 实例产生相同 entity set，作为 pre-deployment check 有应用价值。[R1, R2 共识，承袭]\n\n4. **MBR decoding 理论连接**：Proposition 1 将 entity construction 形式化为 MBR 特例，理论锚点清晰。Eikema et al. (2025) 引用增强了文献连接。[R1, R2 共识，承袭+增强]\n\n5. **R42 修改质量高**：所有 Must-Fix 修改实质性地解决了问题。R2 特别指出：epoch confound 的 reframing 和三重统计校正的透明报告是高质量的学术回应，超越 surface-level 修补。修订展现了良好的学术素养。[R1, R2 共识，R42 新增]\n\n6. **Claims-evidence 对齐**：R42 版本达到了 claims 与 evidence 的良好对齐——没有 overclaim，边界清晰，hedging 恰当。R2 认为这是 Conference 级论文的必要条件（但非充分条件）。[R1, R2 共识，R42 新增]\n\n7. **Negative results 诚实报告**：明确报告 cross-dataset transfer 失败、RE 局限、epoch confound。Appendix ah 自审 12 个 potential objections。[R2，承袭]\n\n8. **Reproducibility 高**：承诺开源代码/checkpoint/数据，超参数报告详尽。[R1, R2 共识，承袭]\n\n---\n\n## Remaining Weaknesses\n\n### R42 新发现问题（2 项 — 双方共识不影响评分）\n\n**NEW-1** [R1 AGREE, R2] **Abstract/§7.5 数值引用不一致** (warning)\n- Abstract: \"Entity-level construction yields conditional gains (+1.40pp on Few-NERD under 3-epoch training; diminishes to +0.09pp at convergence)\"\n- +0.09pp 是 LP selection（非 entity construction）在 5-epoch 下的数字\n- Entity construction 在 5-epoch 下应为 +0.20pp（§7.5: \"entity construction: +0.88→+0.20pp\"）\n- 同一句中混淆了两个不同 metric\n- **双方共识**：camera-ready 级修正项，不影响核心结论（无论 0.09 还是 0.20，5-epoch 收益接近零，epoch confound 结论不变）\n- **建议**：修正为 \"+1.40pp...diminishes to +0.20pp at convergence\" 或拆分两个 metric\n\n**NEW-2** [R1 AGREE, R2] **§7.5 entity construction 3-epoch 数字不一致** (info)\n- §7.5 Prescriptive Results: \"LP-weighted construction yields +1.40±0.51pp\"\n- §7.5 Training convergence: \"entity construction: +0.88→+0.20pp, 77% reduction\"\n- 同一 subsection 中 3-epoch entity construction 出现 +1.40pp 和 +0.88pp 两个值\n- 可能源于不同变体（LP-weighted vs uniform），但未明确标注\n- **双方共识**：camera-ready 级修正项，不影响核心判断\n- **建议**：统一标注变体名称\n\n### R41 遗留未修改问题（2 项 open Should-Fix + 1 项 divergence）\n\n**W2** [承袭] 2-3 seeds 统计推断力不足 — Response-letter item\n\n**W5** [承袭] Entity-level decomposition 增量贡献需更强论证 — Response-letter item\n\n**D2** [持续分歧] 正文数字密度过高 — R2 认为影响可读性，R1 认为诊断论文属性\n\n**D1** [R2 撤回] 标题 \"Why SC Fails\" 匹配度 — R2 在交叉回应中撤回此关注：\"标题是风格选择，不应影响实质性评分\"\n\n---\n\n## Questions（R42 残留）\n\n1. Abstract 中 \"+0.09pp at convergence\" 应改为 \"+0.20pp\"（entity construction）或明确标注为 LP selection？[R1, R2 共识]\n2. §7.5 中 \"+1.40pp\" (LP-weighted) 与 \"+0.88pp\" (generic entity construction) 的关系——如果是不同变体，77% reduction 的基线是哪个？[R1, R2 共识]\n3. §4 \"AUROC 0.50-0.55\" vs §5 \"AUROC 0.50-0.52\" 可能源于不同实验子集（entity-level vs class-level），应标注来源。[R1 发现, R2 AGREE]\n\n---\n\n## Missing References\n\nR41 指出的遗漏已全部修复。R42 无新的遗漏引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿（状态：not_requested）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 ~4 分钟）\n\n| 严重度 | 页面 | 发现 |\n|--------|------|------|\n| 🔴 critical | p.23 | 几乎空白页：仅顶部 9 行文字，~85% 空白。应合并到前/后页 |\n| ⚠️ warning | p.7 | 三个 display items 挤在同一页，Figure 尺寸偏小 |\n| ⚠️ warning | p.2 | Figure 1 内部注释文字偏小 |\n| ℹ️ info | p.15 | Figure 7 热力图灰度打印区分度下降 |\n| ℹ️ info | p.8 | 主文最后一页纯文本（Discussion/Conclusion 可接受） |\n| ℹ️ info | p.46 | Table 69 文字约 6-7pt |\n| ℹ️ info | p.12 | Figure 5 字号偏小但可读 |\n| ℹ️ info | pp.12-47 | 附录 36 页，建议开头加导读 |\n\n1 critical（Appendix 空白页）, 2 warning, 5 info。主文排版无阻断问题。\n\n---\n\n## Score Divergence Analysis\n\n### R1 评分：4.0 (Conference) — 维持\n**核心论据**：\n- Must-Fix 全部解决，修改展示深入理解\n- Bound 重定位、ESJ 跨模型验证、free-form ablation 增强证据链\n- 系统性诊断分析（解释一个广泛观察到但未被理解的现象）具有独立 Conference 价值\n- Claims-evidence 正确对齐\n\n### R2 评分：3.5 (Borderline Conference) — 维持（附维度更新）\n**核心论据**（交叉回应后精炼）：\n- **决定性因素**：Landesberg (2026) 独立发现 correlation-selection gap 限制了 Excitement 上限。论文从 \"discovering a new phenomenon\" 降级为 \"extending a known phenomenon to a new domain with mechanistic analysis\"——有价值但 incremental\n- **支撑性因素**：Entity construction 正面结果 conditional 且 global p_adj=0.055，不足以作为独立卖点。如果论文完全放弃正面 claim（纯负面结果 + 诊断），R2 可能反而更倾向 4.0\n- **撤回**：标题关注（\"标题是风格选择，不应影响实质性评分\"）\n- R2 明确认可 4.0 是 \"一个合理的评分\"，R1 论据 \"在逻辑上是自洽的\"\n\n### 交叉回应后达成的共识\n\n| 项目 | R1 | R2 | 状态 |\n|------|----|----|------|\n| R41 Must-Fix 全部 RESOLVED | ✅ | ✅ | **共识** |\n| Soundness 4.0 | ✅ | ✅ | **共识**（R2 从 3.5 升至 4.0） |\n| Excitement | 3.5 | 3.0 | **分歧**（0.5 差距） |\n| Overall | 4.0 | 3.5 | **分歧**（0.5 差距） |\n| NEW-1/NEW-2 不影响评分 | ✅ | ✅ | **共识** |\n| 3.5-4.0 均为合理评分 | ✅ | ✅ | **共识** |\n\n### Director 判断\n分歧已收敛至最小可能范围：双方在所有事实判断上一致（issue 状态、Soundness 4.0、NEW-1/NEW-2 为 camera-ready 修正），唯一分歧点是 Excitement 的主观权重——R1 认为 well-documented negative result + 诊断框架对社区的信息价值值 3.5，R2 认为 concurrent discovery 限制信息增量至 3.0。这是合理的主观分歧，不可通过额外论证消解。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4 / 5\n**相较 R41 变化**: 从 \"weak 3.5\" 提升至 \"strong 3.5 / borderline 4.0\"\n\n### 维度分数\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4.0 | 4.0 | **4.0**（共识） |\n| Excitement | 3.5 | 3.0 | 3.0-3.5 |\n| Reproducibility | 4.0 | 4.0 | **4.0**（共识） |\n\n### 评分理由\n\n论文在 R42 中展示了对所有 R41 Must-Fix 的高质量修改回应。5 个 critical issues 全部 RESOLVED，Soundness 达成 4.0 共识。这是显著的进步——R41 的 5 个 Must-Fix 从根本上动摇了论文的核心贡献支柱，R42 的修改全部实质性解决。\n\n维持 3.5 而非升至 4.0 的原因：\n1. **Excitement 分歧**：Concurrent discovery (Landesberg 2026) 如何影响论文信息增量是核心争议。R2 的分析有理：对一个读过 Landesberg 的读者，本文的增量贡献从\"发现新现象\"变为\"已知现象的领域扩展 + 机制分析\"。这一区分直接降低 Excitement 评分。\n2. **Prescriptive 贡献条件化**：R2 指出一个微妙观察——如果论文完全放弃正面 claim（纯负面结果），其作为 clean negative result 的价值可能更高。当前仍试图 claim entity construction 的条件性正面结果，使 limited impact 成为削弱因素。\n\n论文的 lower bound 为 3.0 (Findings)。R1 的 4.0 评估合理反映了修改后论文的 Soundness 和 transparency 提升，以及对诊断框架独立价值的合理评估。\n\n**最终建议**：**3.5 (Borderline Conference)**。Conference accept 或 Findings accept 均为合理结果（R2 原话：\"无论最终决定是 Conference accept 还是 Findings accept，都不会是错误判断\"）。\n\n### 与 R41 的进步\n\n| 指标 | R41 | R42 |\n|------|-----|-----|\n| Must-Fix | 5 open | **0 open (全部 RESOLVED)** |\n| Should-Fix | 6 open | **2 open (response-letter items)** |\n| Soundness | 3.5 / 3.5 | **4.0 / 4.0 (共识升级)** |\n| Excitement | 3.5 / 2.5 | 3.5 / 3.0 (R2 +0.5) |\n| Overall | 3.5 / 3.5 | 4.0 / 3.5 (R1 升级) |\n| Claims-evidence 对齐 | 有 overclaim | **无 overclaim** |\n| 统计透明度 | Cherry-picked | **三重校正全部透明** |\n\n### 遗留问题清单\n\nCamera-ready 或下轮修正：\n1. **NEW-1** (warning): Abstract \"+0.09pp\" 应改为 \"+0.20pp\" 或分别报告\n2. **NEW-2** (info): §7.5 明确标注 LP-weighted vs uniform construction\n3. **AUROC minor**: §4 vs §5 的 AUROC 范围标注来源\n4. **W2** (response-letter): 3 seeds 统计推断力\n5. **W5** (response-letter): Entity-level vs task-level 增量论证\n6. **Visual p.23**: Appendix 空白页\n\n---\n\n## Detailed Comments\n\n### §Abstract\n- R41 修改验证：条件限定（\"under 3-epoch training\"）到位\n- **NEW-1**：\"+0.09pp at convergence\" 混淆 LP selection 与 entity construction → 必须修正\n- 双 p 值报告透明度好\n\n### §2 Related Work\n- Landesberg 4 维度系统对比充分，Table 1 七维度清晰\n- 新增引用（Eikema, calibration, TTS）全部到位\n- R2 交叉回应确认：differentiation RESOLVED，但 novelty increment 仍受 concurrent discovery 限制——这是评估性判断而非论文缺陷\n\n### §4 Where Single-Signal Selection Fails\n- Probe 模型标注到位，Qwen3-8B ESJ 交叉验证增强证据链\n- R2 承认在 R42 初审中可能遗漏了 ESJ 跨模型验证这一改进\n- AUROC 0.50-0.55 vs 0.50-0.52 minor inconsistency → camera-ready 修正\n\n### §6.3 Degeneracy Decomposition\n- 重定位成功——\"intentionally loose necessary condition test\"\n- R2 确认：这一重定位从 overselling 转为诚实定位，是正确的学术选择\n\n### §7.5 Prescriptive Results\n- Family 划分先验理由到位\n- 三重校正透明报告（R2：\"超越 NLP 领域标准实践\"）\n- **NEW-2**：+1.40pp vs +0.88pp 需区分标注\n- Epoch confound 完整呈现\n\n### §8 Discussion/Conclusion\n- LP compression 跨数据集确认（std ratio 0.86-1.00×）\n- 定位一致\n\n### Limitations\n- 覆盖充分，长度适当\n- Probe 模型差异 + ESJ 复制 + free-form 跨数据集 + 双 p 值 均已到位",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 42 (Continue)\n\n**论文**: \"Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性; R2: 新颖性/完整性）\n**审稿模式**: 继续审稿（基于 R41 修改验证）\n**交叉分享**: R1, R2 均完成交叉回应，达成部分共识\n\n---\n\n## Summary\n\nRound 42 是对 R41 提出的 5 个 Must-Fix、6 个 Should-Fix 的修改验证轮。论文对全部 5 个 Must-Fix 进行了实质性修改：§6.3 将 bound 重定位为 necessary condition screening test；§7.5 透明报告双重 p 值并提供 family 划分先验理由；§4 标注 probe 模型差异并新增 Qwen3-8B ESJ 交叉验证；§2 扩展 Landesberg 系统对比为 4 维度 + Table 1 增加 failure mechanism 行；Abstract 对 +1.40pp 加入 3-epoch 条件限定。Should-Fix 中 4 项（W1 叙事定位、W3 RE/SQL 措辞、W4 缺失引用、W6 free-form ablation）已修复。\n\n两位 Reviewer 对所有 R41 Must-Fix 验证为 RESOLVED，Soundness 达成共识升至 4.0。评分分歧：R1=4.0 (Conference)，R2=3.5 (Borderline Conference)。分歧根源为 Excitement 的主观权重——R2 认为 concurrent discovery (Landesberg 2026) 限制了 novelty increment，R1 认为诊断框架的系统性分析具有独立 Conference 价值。双方明确认为 3.5-4.0 均为合理评分。\n\n---\n\n## R41 Issue Resolution Status\n\n### Must-Fix（5/5 RESOLVED — 双方共识）\n\n| ID | Issue | R42 Status | 说明 |\n|----|-------|-----------|------|\n| N1 | Bound 仅恢复 3-12% | ✅ RESOLVED | §6.3 成功重定位为 \"intentionally loose necessary condition test\"，不再 oversell |\n| N2 | 统计显著性依赖校正方案 | ✅ RESOLVED | §7.5 双 p 值透明报告（global 0.055, per-family 0.006），family 划分有先验理由，明确声明 not pre-registered |\n| N3 | Probe 模型不一致 | ✅ RESOLVED | §4 显式标注 Qwen2.5-7B-Instruct，ESJ Qwen3-8B 交叉验证确认 chance-level (AUROC 0.50-0.55)，Limitations 更新 |\n| N4 | Landesberg 区分不足 | ✅ RESOLVED | §2 扩展为 4 维度系统对比（domain/mechanism/granularity/prescriptive），Table 1 新增 failure mechanism 行 |\n| N5 | Epoch confound 削弱正面结果 | ✅ RESOLVED | Abstract 限定 \"under 3-epoch training; diminishes at convergence\"，§7.5 完整呈现 94%/77% reduction |\n\n### Should-Fix（4/6 RESOLVED, 2 open — response-letter items）\n\n| ID | Issue | R42 Status | 说明 |\n|----|-------|-----------|------|\n| W1 | Diagnostic/prescriptive 不一致 | ✅ RESOLVED | 全文统一为 \"primarily diagnostic with limited predictive power\" |\n| W2 | 2-3 seeds 统计推断力不足 | ⚪ OPEN | Response-letter item，论文未修改 |\n| W3 | RE/SQL 扩展过薄 | ✅ RESOLVED | Abstract \"preliminary RE (n=397) and SQL (n=196) pilots\" 措辞充分 |\n| W4 | Related Work 遗漏 | ✅ RESOLVED | Eikema et al. (2025), li2026rewardtail, desai2020calibration, xiao2022uncertainty 全部添加 |\n| W5 | Entity-level 增量论证不足 | ⚪ OPEN | Response-letter item，论文未修改 |\n| W6 | Free-form ablation 不足 | ✅ RESOLVED | 扩展到 SciERC + CoNLL + Few-NERD（LP std ratio 0.86×-1.00×），Discussion 引用跨数据集证据 |\n\n---\n\n## Strengths（承袭 R41 + R42 新增）\n\n1. **研究问题重要且定位精准**：SC 在结构化预测上失败的诊断分析填补社区空白。[R1, R2 共识，承袭]\n\n2. **实验极其详尽且透明**：4 数据集 × 2 模型家族 × 5 信号 × 9 方法类别，59 个 tables + 11 个 figures 的附录，统计检验覆盖面在 NLP 实证研究中属上乘。三重统计校正透明报告 + 非预注册声明超越 NLP 领域标准实践。[R1, R2 共识，承袭+R42增强]\n\n3. **Degeneracy 概念有实证价值**：12-68% 的 NER 实例产生相同 entity set，作为 pre-deployment check 有应用价值。[R1, R2 共识，承袭]\n\n4. **MBR decoding 理论连接**：Proposition 1 将 entity construction 形式化为 MBR 特例，理论锚点清晰。Eikema et al. (2025) 引用增强了文献连接。[R1, R2 共识，承袭+增强]\n\n5. **R42 修改质量高**：所有 Must-Fix 修改实质性地解决了问题。R2 特别指出：epoch confound 的 reframing 和三重统计校正的透明报告是高质量的学术回应，超越 surface-level 修补。修订展现了良好的学术素养。[R1, R2 共识，R42 新增]\n\n6. **Claims-evidence 对齐**：R42 版本达到了 claims 与 evidence 的良好对齐——没有 overclaim，边界清晰，hedging 恰当。R2 认为这是 Conference 级论文的必要条件（但非充分条件）。[R1, R2 共识，R42 新增]\n\n7. **Negative results 诚实报告**：明确报告 cross-dataset transfer 失败、RE 局限、epoch confound。Appendix ah 自审 12 个 potential objections。[R2，承袭]\n\n8. **Reproducibility 高**：承诺开源代码/checkpoint/数据，超参数报告详尽。[R1, R2 共识，承袭]\n\n---\n\n## Remaining Weaknesses\n\n### R42 新发现问题（2 项 — 双方共识不影响评分）\n\n**NEW-1** [R1 AGREE, R2] **Abstract/§7.5 数值引用不一致** (warning)\n- Abstract: \"Entity-level construction yields conditional gains (+1.40pp on Few-NERD under 3-epoch training; diminishes to +0.09pp at convergence)\"\n- +0.09pp 是 LP selection（非 entity construction）在 5-epoch 下的数字\n- Entity construction 在 5-epoch 下应为 +0.20pp（§7.5: \"entity construction: +0.88→+0.20pp\"）\n- 同一句中混淆了两个不同 metric\n- **双方共识**：camera-ready 级修正项，不影响核心结论（无论 0.09 还是 0.20，5-epoch 收益接近零，epoch confound 结论不变）\n- **建议**：修正为 \"+1.40pp...diminishes to +0.20pp at convergence\" 或拆分两个 metric\n\n**NEW-2** [R1 AGREE, R2] **§7.5 entity construction 3-epoch 数字不一致** (info)\n- §7.5 Prescriptive Results: \"LP-weighted construction yields +1.40±0.51pp\"\n- §7.5 Training convergence: \"entity construction: +0.88→+0.20pp, 77% reduction\"\n- 同一 subsection 中 3-epoch entity construction 出现 +1.40pp 和 +0.88pp 两个值\n- 可能源于不同变体（LP-weighted vs uniform），但未明确标注\n- **双方共识**：camera-ready 级修正项，不影响核心判断\n- **建议**：统一标注变体名称\n\n### R41 遗留未修改问题（2 项 open Should-Fix + 1 项 divergence）\n\n**W2** [承袭] 2-3 seeds 统计推断力不足 — Response-letter item\n\n**W5** [承袭] Entity-level decomposition 增量贡献需更强论证 — Response-letter item\n\n**D2** [持续分歧] 正文数字密度过高 — R2 认为影响可读性，R1 认为诊断论文属性\n\n**D1** [R2 撤回] 标题 \"Why SC Fails\" 匹配度 — R2 在交叉回应中撤回此关注：\"标题是风格选择，不应影响实质性评分\"\n\n---\n\n## Questions（R42 残留）\n\n1. Abstract 中 \"+0.09pp at convergence\" 应改为 \"+0.20pp\"（entity construction）或明确标注为 LP selection？[R1, R2 共识]\n2. §7.5 中 \"+1.40pp\" (LP-weighted) 与 \"+0.88pp\" (generic entity construction) 的关系——如果是不同变体，77% reduction 的基线是哪个？[R1, R2 共识]\n3. §4 \"AUROC 0.50-0.55\" vs §5 \"AUROC 0.50-0.52\" 可能源于不同实验子集（entity-level vs class-level），应标注来源。[R1 发现, R2 AGREE]\n\n---\n\n## Missing References\n\nR41 指出的遗漏已全部修复。R42 无新的遗漏引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿（状态：not_requested）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 ~4 分钟）\n\n| 严重度 | 页面 | 发现 |\n|--------|------|------|\n| 🔴 critical | p.23 | 几乎空白页：仅顶部 9 行文字，~85% 空白。应合并到前/后页 |\n| ⚠️ warning | p.7 | 三个 display items 挤在同一页，Figure 尺寸偏小 |\n| ⚠️ warning | p.2 | Figure 1 内部注释文字偏小 |\n| ℹ️ info | p.15 | Figure 7 热力图灰度打印区分度下降 |\n| ℹ️ info | p.8 | 主文最后一页纯文本（Discussion/Conclusion 可接受） |\n| ℹ️ info | p.46 | Table 69 文字约 6-7pt |\n| ℹ️ info | p.12 | Figure 5 字号偏小但可读 |\n| ℹ️ info | pp.12-47 | 附录 36 页，建议开头加导读 |\n\n1 critical（Appendix 空白页）, 2 warning, 5 info。主文排版无阻断问题。\n\n---\n\n## Score Divergence Analysis\n\n### R1 评分：4.0 (Conference) — 维持\n**核心论据**：\n- Must-Fix 全部解决，修改展示深入理解\n- Bound 重定位、ESJ 跨模型验证、free-form ablation 增强证据链\n- 系统性诊断分析（解释一个广泛观察到但未被理解的现象）具有独立 Conference 价值\n- Claims-evidence 正确对齐\n\n### R2 评分：3.5 (Borderline Conference) — 维持（附维度更新）\n**核心论据**（交叉回应后精炼）：\n- **决定性因素**：Landesberg (2026) 独立发现 correlation-selection gap 限制了 Excitement 上限。论文从 \"discovering a new phenomenon\" 降级为 \"extending a known phenomenon to a new domain with mechanistic analysis\"——有价值但 incremental\n- **支撑性因素**：Entity construction 正面结果 conditional 且 global p_adj=0.055，不足以作为独立卖点。如果论文完全放弃正面 claim（纯负面结果 + 诊断），R2 可能反而更倾向 4.0\n- **撤回**：标题关注（\"标题是风格选择，不应影响实质性评分\"）\n- R2 明确认可 4.0 是 \"一个合理的评分\"，R1 论据 \"在逻辑上是自洽的\"\n\n### 交叉回应后达成的共识\n\n| 项目 | R1 | R2 | 状态 |\n|------|----|----|------|\n| R41 Must-Fix 全部 RESOLVED | ✅ | ✅ | **共识** |\n| Soundness 4.0 | ✅ | ✅ | **共识**（R2 从 3.5 升至 4.0） |\n| Excitement | 3.5 | 3.0 | **分歧**（0.5 差距） |\n| Overall | 4.0 | 3.5 | **分歧**（0.5 差距） |\n| NEW-1/NEW-2 不影响评分 | ✅ | ✅ | **共识** |\n| 3.5-4.0 均为合理评分 | ✅ | ✅ | **共识** |\n\n### Director 判断\n分歧已收敛至最小可能范围：双方在所有事实判断上一致（issue 状态、Soundness 4.0、NEW-1/NEW-2 为 camera-ready 修正），唯一分歧点是 Excitement 的主观权重——R1 认为 well-documented negative result + 诊断框架对社区的信息价值值 3.5，R2 认为 concurrent discovery 限制信息增量至 3.0。这是合理的主观分歧，不可通过额外论证消解。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4 / 5\n**相较 R41 变化**: 从 \"weak 3.5\" 提升至 \"strong 3.5 / borderline 4.0\"\n\n### 维度分数\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4.0 | 4.0 | **4.0**（共识） |\n| Excitement | 3.5 | 3.0 | 3.0-3.5 |\n| Reproducibility | 4.0 | 4.0 | **4.0**（共识） |\n\n### 评分理由\n\n论文在 R42 中展示了对所有 R41 Must-Fix 的高质量修改回应。5 个 critical issues 全部 RESOLVED，Soundness 达成 4.0 共识。这是显著的进步——R41 的 5 个 Must-Fix 从根本上动摇了论文的核心贡献支柱，R42 的修改全部实质性解决。\n\n维持 3.5 而非升至 4.0 的原因：\n1. **Excitement 分歧**：Concurrent discovery (Landesberg 2026) 如何影响论文信息增量是核心争议。R2 的分析有理：对一个读过 Landesberg 的读者，本文的增量贡献从\"发现新现象\"变为\"已知现象的领域扩展 + 机制分析\"。这一区分直接降低 Excitement 评分。\n2. **Prescriptive 贡献条件化**：R2 指出一个微妙观察——如果论文完全放弃正面 claim（纯负面结果），其作为 clean negative result 的价值可能更高。当前仍试图 claim entity construction 的条件性正面结果，使 limited impact 成为削弱因素。\n\n论文的 lower bound 为 3.0 (Findings)。R1 的 4.0 评估合理反映了修改后论文的 Soundness 和 transparency 提升，以及对诊断框架独立价值的合理评估。\n\n**最终建议**：**3.5 (Borderline Conference)**。Conference accept 或 Findings accept 均为合理结果（R2 原话：\"无论最终决定是 Conference accept 还是 Findings accept，都不会是错误判断\"）。\n\n### 与 R41 的进步\n\n| 指标 | R41 | R42 |\n|------|-----|-----|\n| Must-Fix | 5 open | **0 open (全部 RESOLVED)** |\n| Should-Fix | 6 open | **2 open (response-letter items)** |\n| Soundness | 3.5 / 3.5 | **4.0 / 4.0 (共识升级)** |\n| Excitement | 3.5 / 2.5 | 3.5 / 3.0 (R2 +0.5) |\n| Overall | 3.5 / 3.5 | 4.0 / 3.5 (R1 升级) |\n| Claims-evidence 对齐 | 有 overclaim | **无 overclaim** |\n| 统计透明度 | Cherry-picked | **三重校正全部透明** |\n\n### 遗留问题清单\n\nCamera-ready 或下轮修正：\n1. **NEW-1** (warning): Abstract \"+0.09pp\" 应改为 \"+0.20pp\" 或分别报告\n2. **NEW-2** (info): §7.5 明确标注 LP-weighted vs uniform construction\n3. **AUROC minor**: §4 vs §5 的 AUROC 范围标注来源\n4. **W2** (response-letter): 3 seeds 统计推断力\n5. **W5** (response-letter): Entity-level vs task-level 增量论证\n6. **Visual p.23**: Appendix 空白页\n\n---\n\n## Detailed Comments\n\n### §Abstract\n- R41 修改验证：条件限定（\"under 3-epoch training\"）到位\n- **NEW-1**：\"+0.09pp at convergence\" 混淆 LP selection 与 entity construction → 必须修正\n- 双 p 值报告透明度好\n\n### §2 Related Work\n- Landesberg 4 维度系统对比充分，Table 1 七维度清晰\n- 新增引用（Eikema, calibration, TTS）全部到位\n- R2 交叉回应确认：differentiation RESOLVED，但 novelty increment 仍受 concurrent discovery 限制——这是评估性判断而非论文缺陷\n\n### §4 Where Single-Signal Selection Fails\n- Probe 模型标注到位，Qwen3-8B ESJ 交叉验证增强证据链\n- R2 承认在 R42 初审中可能遗漏了 ESJ 跨模型验证这一改进\n- AUROC 0.50-0.55 vs 0.50-0.52 minor inconsistency → camera-ready 修正\n\n### §6.3 Degeneracy Decomposition\n- 重定位成功——\"intentionally loose necessary condition test\"\n- R2 确认：这一重定位从 overselling 转为诚实定位，是正确的学术选择\n\n### §7.5 Prescriptive Results\n- Family 划分先验理由到位\n- 三重校正透明报告（R2：\"超越 NLP 领域标准实践\"）\n- **NEW-2**：+1.40pp vs +0.88pp 需区分标注\n- Epoch confound 完整呈现\n\n### §8 Discussion/Conclusion\n- LP compression 跨数据集确认（std ratio 0.86-1.00×）\n- 定位一致\n\n### Limitations\n- 覆盖充分，长度适当\n- Probe 模型差异 + ESJ 复制 + free-form 跨数据集 + 双 p 值 均已到位",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 4551 · 2026-05-23T07:23:42.576365+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4119
}
```

</details>

---


### Assistant

_source line 4552 · 2026-05-23T07:23:51.559479+00:00_

R42 审稿报告已更新并重新投递。

**关键变化**：
- R2 交叉回应收到后，Soundness 达成 **4.0 共识**（R2 从 3.5 升至 4.0）
- R2 Excitement 从 2.5 升至 3.0，但仍低于 R1 的 3.5
- R2 撤回标题关注
- 分歧收敛至最小范围：双方在所有事实判断上一致，唯一分歧是 Excitement 的主观权重（concurrent discovery 的影响）
- 双方明确认为 3.5-4.0 均为合理评分
- Overall 维持 **3.5 (Borderline Conference)**，从 R41 的 "weak 3.5" 提升至 "strong 3.5 / borderline 4.0"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 349

## Round 349

84 recorded events


### User

_source line 4553 · 2026-05-23T08:31:54.723043+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 4554 · 2026-05-23T08:32:00.525169+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 4555 · 2026-05-23T08:32:00.626458+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4556 · 2026-05-23T08:32:07.952574+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 4557 · 2026-05-23T08:32:08.153651+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 4558 · 2026-05-23T08:32:11.646279+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4559 · 2026-05-23T08:32:13.162296+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (329 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_fewnerd_pretrained_n32_s42_v2 | Pretrained N-scaling rerun: FewNERD N=32 with Qwen2.5-7B-Instruct. v1 killed at 70% to prevent UnicodeEncodeError crash at save stage (no incremental checkpoint). Fix (errors='replace') deployed. Same hypothesis: tests pretrained MV advantage at 4× budget (N=32). | — | — | — |\n\n## 待处理\n- exp_fewnerd_mf4v2_s123_v4: FewNERD MF4v2 s123 v4: regenerate finetuned FewNERD seed=123 instance-level samples.jsonl on autodl-5090-c for v4 MV unified recompute. N=8, T=1.0, seed=123. Model: qwen3-8b-fewnerd-exp021-merged. Parent retries v2 (failed on 5090) and v3 (killed). Using confirmed-working 5090-c environment from s456_v3.（准备中）\n- exp_fewnerd_mf4v2_s42_v4: Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.（准备中）\n- exp_fewnerd_mf4v2_s123_v2: FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.（准备中）\n- exp_fewnerd_mf4v2_s42_v2: FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level sample
…[truncated 1743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1516
}
```

</details>

---


### Tool call

_source line 4560 · 2026-05-23T08:32:13.193398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 4561 · 2026-05-23T08:32:14.153124+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{Why Self-Consistency Fails for NER:\\ Degeneracy, Signal Collapse, and the Correlation-Selection Gap}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/background}
38	\input{sections/diagnostic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/discussion}
44	
45	\section*{Limitations}
46	\input{sections/limitations}
47	
48	\section*{Ethics Statement}
49	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
50	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
51	No new human data was collected or annotated for this study.
52	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
53	Code and data will be released upon acceptance at [anonymized URL].
54	
55	\bibliography{references}
56	
57	\appendix
58	\renewcommand{\thesection}{\alphalph{\value{section}}}
59	\input{sections/appendix}
…[truncated 26 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 4562 · 2026-05-23T08:32:14.153526+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 4563 · 2026-05-23T08:32:15.361330+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 4564 · 2026-05-23T08:32:15.562435+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 4565 · 2026-05-23T08:32:20.061223+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

I found relevant information about EMNLP 2026 and ARR submissions. Based on the search res
…[truncated 1241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5907
}
```

</details>

---


### Tool call

_source line 4566 · 2026-05-23T08:32:26.213454+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 4567 · 2026-05-23T08:32:26.665479+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format"
  }
}
```

</details>

---


### Tool call

_source line 4568 · 2026-05-23T08:32:27.167603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4569 · 2026-05-23T08:32:28.122830+00:00_

1	issues:
2	# ===== ROUND 41 MUST-FIX — R42 全部验证通过 =====
3	- id: R41-N1
4	  summary: "分解 bound 仅恢复 3-12% 实际增益，核心形式化贡献实用价值不足"
5	  category: method
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 38
9	  last_seen_round: 42
10	  mentions:
11	    - round: 40
12	      reviewers: [1, 2]
13	      note: "R40 已标注，要求 reposition 为 diagnostic decomposition tool"
14	    - round: 41
15	      reviewers: [1, 2]
16	      note: "R1 Must-Fix, R2 交叉 AGREE。bound 仅解释 3-12%。"
17	    - round: 42
18	      reviewers: [1, 2]
19	      note: "R42 验证通过。§6.3 已重定位为 intentionally loose necessary condition test，recovery ratio 重新定位为 screening test 而非 tight estimate。"
20	  action_items:
21	    - round: 41
22	      action: "§6.3 重定位为 necessary condition test；弱化 Table 33 ratio；声明 intentionally loose"
23	      assigned_to: paper_agent
24	      status: done
25	  resolution: "§6.3 成功重定位为 necessary condition screening test。R42 两位 Reviewer 确认 RESOLVED。"
26	  resolution_round: 42
27	
28	- id: R41-N2
29	  summary: "核心正面 claim 统计显著性取决于多重比较校正方案选择"
30	  category: method
31	  severity: critical
32	  status: resolved
33	  first_raised_round: 34
34	  last_seen_round: 42
35	  mentions:
36	    - round: 40
37	      reviewers: [1, 2]
38	      note: "R40 已标注。"
39	    - round: 41
40	      reviewers: [1, 2]
41	      note: "R1 Must-Fix, R2 交叉 AGREE。per-family 校正缺乏先验理由。"
42	    - round: 42
43	      reviewers: [1, 2]
44	      note: "R42 验证通过。§7.5 提供 family 划分先验理由（mechanistic distinctions at design time），双 p 值透明报告，明确声明 not pre-registered。"
45	  action_items:
46	    - round: 41
47	      action: "§7.5 提供 family 划分先验理由；主文同时报告全局 p_adj=0.055 和 per-family p_adj=0.006"
48	      assigned_to: paper_agent
49	      status: done
50	  resolution: "§7.5 family 划分理由充分，双 p 值透明报告。R42 两位 Reviewer 确认 RESOLVED。"
51	  resolution_round: 42
52	
53	- id: R41-N3
54	  summary: "Mechanistic probes 使用 Qwen2.5-7B 而非主实验 Qwen3-8B"
55	  category: experiment
56	  severity: critical
57	  status: resolved
58	  first_raised_round: 36
59	  las
…[truncated 15030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 4570 · 2026-05-23T08:32:28.123327+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 4571 · 2026-05-23T08:32:28.173916+00:00_

_archived
abstract.tex
adaptive.tex
appendix.tex
background.tex
checklist.tex
conclusion.tex
diagnostic.tex
discussion.tex
experiments_main.tex
introduction.tex
limitations.tex
mechanistic.tex
method.tex
related_work.tex
single_signal.tex
theoretical.tex
theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 4572 · 2026-05-23T08:32:31.737097+00:00_

Web search results for query: "EMNLP 2026 main conference submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"}]

Based on the search results, here's the information about EMNLP 2026 main conference submission deadline and ARR commitment:

## Main Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026.

## ARR Commitment Policy

For the ARR 2026 May cycle aligned with EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026 - ARR 2026 May submissions that do not select EMNLP 2026 
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5523
}
```

</details>

---


### Tool result

_source line 4573 · 2026-05-23T08:32:32.290390+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and format:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.

Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for
…[truncated 798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5624
}
```

</details>

---


### Tool call

_source line 4574 · 2026-05-23T08:32:38.865303+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits, formatting requirements, anonymity rules, appendix rules, citation format, template requirements, important dates (submission deadline, commitment deadline), and any special policies for EMNLP 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits, formatting requirements, anonymity rules, appendix rules, citation format, template requirements, important dates (submission deadline, commitment deadline), and any special policies for EMNLP 2026."
  }
}
```

</details>

---


### Tool call

_source line 4575 · 2026-05-23T08:32:40.923256+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/cfp",
  "prompt": "Extract the current ARR submission guidelines: page limits for long/short papers, formatting requirements, template, anonymity rules, appendix rules, limitations section requirements, ethics statement requirements, and responsible NLP checklist requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/cfp",
    "prompt": "Extract the current ARR submission guidelines: page limits for long/short papers, formatting requirements, template, anonymity rules, appendix rules, limitations section requirements, ethics statement requirements, and responsible NLP checklist requirements."
  }
}
```

</details>

---


### Tool call

_source line 4576 · 2026-05-23T08:32:42.529411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 4577 · 2026-05-23T08:32:43.181914+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary analysis, with preliminary RE ($n{=}397$) and SQL ($n{=}196$) pilots.
4	Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields ${<}1$\,pp, revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that jointly determine scaling returns; cross-task exploration confirms task-specific failure modes.
6	Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; collapses by 77--91\% at convergence; \S\ref{sec:prescriptive}; per-family Holm $p_{\text{adj}}{=}0.006$, global $p_{\text{adj}}{=}0.055$) but exhibits inverse scaling in most configurations (69\% of $N$-transitions).
7	The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 4578 · 2026-05-23T08:32:43.232654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 4579 · 2026-05-23T08:32:43.283307+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \cite{yao2026consistency} and qualitative diversity collapse \cite{yun2025price} but no instance-level diagnostic framework.
5	
6	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection fails---MV gains ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also fails through within-instance compression (\S\ref{sec:selection_gap}).
8	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; Appendix~\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
9	A \textit{diagnostic framework} localizes the failure to two co-occurring conditions---degeneracy ($12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$; $\alpha$ here denotes LP-F1 alignment)---which jointly prevent selection (Table~\ref{tab:method_summary}).
10	The framework decomposes observed failures post-hoc rather than predicting which instances will fail a priori.
11	The optimal strategy is dataset-dependent (LP $+1.39$\,pp on Few-NERD; MV $+0.61$\,pp on CoNLL), and RE
…[truncated 3244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 4580 · 2026-05-23T08:32:44.339901+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long papers:** 8 pages (final versions may have up to 9 pages to address reviewer feedback)
- **Short papers:** 4 pages (final versions may have up to 5 pages to address reviewer feedback)

## Formatting & Templates
Papers must adhere to "all of the ARR submission requirements," including specified templates available through the ACL Rolling Review platform. Specific formatting details are referenced in the ARR guidelines rather than detailed here.

## Anonymity Rules
The review process maintains double-blind anonymity: "Reviewers will not see authors, nor will authors see reviewers." However, "there is no anonymity period requirement" per ACL and ARR policies. Authors may optionally make anonymized submissions publicly visible through ARR.

## Appendices & Supplementary Materials
"Optional supplementary materials (appendices, software, and data)" are permitted under ARR guidelines.

## Citation Format
The document references ARR's "Citation and Comparison" requirements but does not specify a particular citation format (e.g., author-date vs. numbered).

## Key Dates
- **ARR submission deadline:** May 25, 2026
- **Reviewer registration deadline:** May 27, 2026
- **EMNLP commitment deadline:** August 2, 2026
- **Acceptance notification:** August 20, 2026
- **Camera-ready deadline:** September 20, 2026

All deadlines are "11:59PM UTC-12:00 ('anywhere on Earth')."

## Special Policies
- Dual submissions prohibited
- Author lists cannot be modified during commitment (reordering permitted)
- Papers must be presented to appear in proceedings
- Ethics compliance and responsible NLP research checklist required

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "elapsed_ms": 5474
}
```

</details>

---


### Tool result

_source line 4581 · 2026-05-23T08:32:49.043535+00:00_

# ARR Submission Guidelines Summary

## Page Limits

**Long Papers:** Up to 8 pages of content, plus unlimited references and space for limitations/ethical considerations sections.

**Short Papers:** Up to 4 pages of content, plus unlimited references and space for limitations/ethical considerations sections.

## Formatting Requirements

Submissions must "follow the [ACL Author Guidelines](https://www.aclweb.org/adminwiki/index.php?title=ACL_Author_Guidelines)" and use "the official ACL style template." Non-compliant formatting results in rejection without review.

## Template

Authors must obtain the official ACL style files from [GitHub](https://github.com/acl-org/acl-style-files) and follow formatting guidelines at [ACLPUB](https://acl-org.github.io/ACLPUB/formatting.html).

## Anonymity Rules

Papers must exclude author names, affiliations, and self-identifying references. Instead of "We previously showed," use "Smith previously showed." Supplementary materials require anonymization; cloud storage links (Dropbox, Google Drive) are prohibited.

## Appendix Rules

Appendices follow main content and references, don't count toward page limits, and must use double-column formatting (with specified exceptions). Reviewers aren't obligated to review appendices; critical content belongs in the main paper.

## Limitations Section (Required)

A dedicated "Limitations" section is mandatory, appearing before references without counting toward page limits. It discusses constraints of presented work only—no new methods or results.

## Ethics Statement

"Authors are encouraged to devote a section of their paper to concerns about the ethical impact" (optional placement). This doesn't count toward page limits when placed at paper's end.

## Responsible NLP Checklist

Authors must complete the checklist during submission. Incomplete or misleading responses risk desk rejection; content informs the review process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "elapsed_ms": 8120
}
```

</details>

---


### Tool call

_source line 4582 · 2026-05-23T08:32:57.379788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 4583 · 2026-05-23T08:32:58.383688+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time scaling and self-consistency.}\label{sec:yun_contrast}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with scaling laws \cite{snell2025scaling, brown2024monkeys, gao2023scaling} yield large gains on reasoning; recent extensions include reward-tail-guided search \cite{li2026rewardtail}. Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and trained verifiers \cite{cobbe2021verifiers, lightman2024verify, li2023stepaware} target discrete-answer settings.
5	SC can fail when consistent outputs are wrong \cite{chen2023twofailures}; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} variants face limits where sub-output agreement does not yield selection gain.
6	\citet{yun2025price} identify diversity collapse under constrained decoding; we extend their qualitative account with quantitative diagnostics (\S\ref{sec:selection_gap}).
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE ($\rho$ up to 0.47); we extend to instance-level analysis: (1)~task-level $\rho$ masks instance-level degeneracy; (2)~we decompose failure into degeneracy and LP compression; (3)~pre-deployment diagnostics that task-level correlation cannot provide.
10	Critically, their task-level granularity cannot distinguish instances where scaling helps from those where it harms---our entity-level decomposition addresses this gap (Table~\ref{tab:novelty_comparison}).
11	\citet{xie2023zeroshot} propose entity voting for zero-shot NER; \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
12	
13	\paragraph{Uncertainty estimation and MBR.}
14	Our selection instantiates MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find MBR utilities degrade on structured outputs, consistent with our LP compression findings.
15	LP is well-calibrated at population 
…[truncated 2346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 4584 · 2026-05-23T08:32:58.384072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 4585 · 2026-05-23T08:32:58.836039+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 4586 · 2026-05-23T08:32:58.836432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 4587 · 2026-05-23T08:32:59.388650+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK      
…[truncated 3360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 4588 · 2026-05-23T08:32:59.389024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 4589 · 2026-05-23T08:32:59.439571+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present exploratory attempts informed by diagnostic findings to extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield a positive result, though on a single dataset.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\ref{sec:mechanistic} and adaptive methods in this section). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & App.~\ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & App.~\ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & App.~\ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can pa
…[truncated 905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4590 · 2026-05-23T08:33:03.757183+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 4591 · 2026-05-23T08:33:04.259422+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}), consistent with utility degradation on structured outputs \cite{eikema2025structured}.
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is mo
…[truncated 3201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 4592 · 2026-05-23T08:33:04.310042+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 4593 · 2026-05-23T08:33:05.314194+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 53.7\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed
…[truncated 8527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 4594 · 2026-05-23T08:33:05.314658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 4595 · 2026-05-23T08:33:05.515666+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for NER.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, degeneracy ($12$--$68$\%) eliminates candidate diversity while signal alignment collapse ($\alpha{\to}0$) prevents ranking.
5	The degeneracy decomposition (\S\ref{sec:theory}) identifies $\alpha$---not degeneracy---as the binding constraint ($8$--$33{\times}$ tighter), a diagnostic for localizing failure rather than a predictive bound.
6	This persists across families \cite{yun2025price} (5.5--74\%), scales (4B--72B; \S\ref{sec:scaling}), and decoding modes (LP std ratio $0.86$--$1.00{\times}$ across three datasets; Appendix~\ref{app:freeform_ablation}); MV gains plateau while oracle headroom expands, suggesting a voting ceiling (Table~\ref{tab:pretrained_summary}).
7	
8	\paragraph{Conclusion.}
9	The diagnostic framework---localizing failure to degeneracy and signal alignment collapse---is our primary contribution; cross-task and cross-model extensions are exploratory.
10	Practitioners can use degeneracy and LP-F1 alignment at $N{=}8$ as a pre-deployment check: high degeneracy ($>50$\%) indicates scaling will not help; low degeneracy with strong alignment may justify entity construction; otherwise, greedy decoding remains optimal.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 4596 · 2026-05-23T08:33:05.515990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 4597 · 2026-05-23T08:33:05.616590+00:00_

1	Our primary evidence is from NER (four English datasets, 7--14B open-weight fine-tuned); cross-scale observations (4B--72B, GPT-5.5) are tentative. The RE extension ($n{=}397$, single dataset) and SQL pilot ($n{=}196$) are exploratory. SciERC results are validated across three training seeds ($n{=}529$ test instances; $\Delta_{\text{SC}}{=}{-}0.74{\pm}0.46$\,pp, consistent negative). Frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), suggesting findings from fine-tuned open-weight models may not fully generalize to proprietary systems.
2	Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \S\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the strongest construction claim reaches $p_{\text{adj}}{=}0.055$ (marginally above $\alpha{=}0.05$); under per-family correction ($k{=}10$), $p_{\text{adj}}{=}0.006$; BH FDR yields $6/10$ construction comparisons at FDR${<}0.05$ (Appendix~\ref{app:holm}).
3	We evaluate at $N{\in}\{2,\ldots,64\}$; entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp). We use a single prompt template per task; prompt variations may affect entity recall, degeneracy, and LP distributions.
4	Mechanistic probes were conducted on Qwen2.5-7B-Instruct, not the fine-tuned Qwen3-8B used in main experiments; probe cross-model transferability is not yet verified, though ESJ chance-level performance replicates on Qwen3-8B (AUROC $0.50$--$0.55$).
5	The free-form decoding ablation was validated on SciERC, CoNLL, and Few-NERD (Appendix~\ref{app:freeform_ablation}); results are consistent across datasets.
6	All evaluation uses entity-level micro-F1 with exact span-and-type match; partial-credit metrics (e.g., token-level or relaxed boundary match) may yield different conclusions about selection effectiveness.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4598 · 2026-05-23T08:33:13.245518+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "file": "config"
  }
}
```

</details>

---


### Tool result

_source line 4599 · 2026-05-23T08:33:13.245950+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'config'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4600 · 2026-05-23T08:33:14.556281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 4601 · 2026-05-23T08:33:14.857717+00:00_

File content (68936 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 4602 · 2026-05-23T08:33:19.699649+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "config"
  }
}
```

</details>

---


### Tool result

_source line 4603 · 2026-05-23T08:33:19.750290+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4604 · 2026-05-23T08:33:20.203405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 4605 · 2026-05-23T08:33:20.304315+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 13232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4606 · 2026-05-23T08:33:29.638245+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_43/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_43/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 4607 · 2026-05-23T08:33:30.140614+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_43/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 4608 · 2026-05-23T08:33:30.744328+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4609 · 2026-05-23T08:33:30.895254+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 4610 · 2026-05-23T08:33:33.555293+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 4611 · 2026-05-23T08:33:34.561248+00:00_

&lt;persisted-output>
Output too large (89.9KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/4bbf5356-bf34-46f3-a9c4-bce4526738ce/tool-results/toolu_0161biffuw3WTDUAW7PegS2b.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260516T094957_715546.jsonl:1676:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260516T094957_715546.jsonl:2121:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260516T094957_715546.jsonl:2402:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T102033_395761.jsonl:2106:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T102033_395761.jsonl:2207:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_523053f5a039428dc15666668fa856b3_20260515T183358_453446.jsonl:905:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260521T014101_505360.jsonl:3912:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b49
…[truncated 330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 4612 · 2026-05-23T08:33:40.079105+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content",
  "glob": "*.yaml",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content",
    "glob": "*.yaml",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 4613 · 2026-05-23T08:33:40.231605+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 4614 · 2026-05-23T08:33:42.690295+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project_config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 4615 · 2026-05-23T08:33:42.843492+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 4616 · 2026-05-23T08:33:45.408323+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 4617 · 2026-05-23T08:33:45.509162+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4618 · 2026-05-23T08:33:47.954675+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
  }
}
```

</details>

---


### Tool result

_source line 4619 · 2026-05-23T08:33:48.005201+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4620 · 2026-05-23T08:33:50.965170+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
  "description": "Find YAML config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "Find YAML config files"
  }
}
```

</details>

---


### Tool result

_source line 4621 · 2026-05-23T08:33:51.015864+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4622 · 2026-05-23T08:33:54.176543+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 4623 · 2026-05-23T08:33:54.227181+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4624 · 2026-05-23T08:33:57.538782+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview|struct_self_consist",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview|struct_self_consist",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 4625 · 2026-05-23T08:33:57.639638+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4626 · 2026-05-23T08:34:24.929731+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,dispatch_visual_check",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,dispatch_visual_check",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 4627 · 2026-05-23T08:34:25.031675+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4628 · 2026-05-23T08:34:27.791476+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer dispatch_visual_check",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer dispatch_visual_check",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 4629 · 2026-05-23T08:34:27.842107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4630 · 2026-05-23T08:34:31.906466+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4631 · 2026-05-23T08:34:51.931138+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20024
}
```

</details>

---


### Tool call

_source line 4632 · 2026-05-23T08:34:52.033466+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性、实验设计、统计分析**方向的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper, 正文 8 页 + 无限参考文献, ACL style template, double-blind, Limitations 必须有（不计入页数）, Appendix 允许但审稿人不强制审阅\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_43/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下角度严格审查：\n\n1. **方法论严谨性**：\n   - Diagnostic framework 的形式化是否严谨？degeneracy decomposition bound 是否有意义？\n   - Confidence signals 的定义和选择是否合理？是否遗漏重要 baseline signals？\n   - Entity construction 的 MBR 理论基础是否成立？\n\n2. **实验设计**：\n   - 数据集选择是否充分？4 个 NER + RE + SQL 的覆盖是否足够？\n   - 模型选择（Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B/14B, GPT-5.5）是否有代表性？\n   - 实验控制变量是否合理？seed 数量、N 范围、温度设置等\n   - Few-NERD 3-epoch vs 5-epoch confound 的处理是否充分？\n\n3. **统计分析**：\n   - 多重比较校正方案（global Holm k=57 vs per-family k=10）是否合理？family 划分的先验理由是否充分？\n   - p 值报告是否透明？特别是 p_adj=0.055 的处理\n   - 2-3 seeds 的统计推断力是否足够？power analysis 是否充分？\n   - Bootstrap CI 和 permutation test 的使用是否恰当？\n\n4. **Claims 与证据匹配**：\n   - Abstract 中的 claims 是否都有充分支撑？\n   - \"correlation-selection gap\" 这一核心 claim 的证据链是否完整？\n   - Conditional gains (+1.40pp) 的条件限定是否足够？\n   - Inverse scaling (69% N-transitions) 的 claim 是否过强？\n\n请按 Strengths / Weaknesses / Questions / Missing References 的结构输出审稿意见。Weaknesses 按严重程度分 [MUST-FIX] / [SHOULD-FIX] / [MINOR]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性、实验设计、统计分析**方向的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper, 正文 8 页 + 无限参考文献, ACL style template, double-blind, Limitations 必须有（不计入页数）, Appendix 允许但审稿人不强制审阅\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_43/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下角度严格审查：\n\n1. **方法论严谨性**：\n   - Diagnostic framework 的形式化是否严谨？degeneracy decomposition bound 是否有意义？\n   - Confidence signals 的定义和选择是否合理？是否遗漏重要 baseline signals？\n   - Entity construction 的 MBR 理论基础是否成立？\n\n2. **实验设计**：\n   - 数据集选择是否充分？4 个 NER + RE + SQL 的覆盖是否足够？\n   - 模型选择（Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B/14B, GPT-5.5）是否有代表性？\n   - 实验控制变量是否合理？seed 数量、N 范围、温度设置等\n   - Few-NERD 3-epoch vs 5-epoch confound 的处理是否充分？\n\n3. **统计分析**：\n   - 多重比较校正方案（global Holm k=57 vs per-family k=10）是否合理？family 划分的先验理由是否充分？\n   - p 值报告是否透明？特别是 p_adj=0.055 的处理\n   - 2-3 seeds 的统计推断力是否足够？power analysis 是否充分？\n   - Bootstrap CI 和 permutation test 的使用是否恰当？\n\n4. **Claims 与证据匹配**：\n   - Abstract 中的 claims 是否都有充分支撑？\n   - \"correlation-selection gap\" 这一核心 claim 的证据链是否完整？\n   - Conditional gains (+1.40pp) 的条件限定是否足够？\n   - Inverse scaling (69% N-transitions) 的 claim 是否过强？\n\n请按 Strengths / Weaknesses / Questions / Missing References 的结构输出审稿意见。Weaknesses 按严重程度分 [MUST-FIX] / [SHOULD-FIX] / [MINOR]。"
  }
}
```

</details>

---


### Tool result

_source line 4633 · 2026-05-23T08:35:06.106056+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14072
}
```

</details>

---


### Tool call

_source line 4634 · 2026-05-23T08:35:06.207175+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性、相关工作覆盖、写作完整性**方向的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper, 正文 8 页 + 无限参考文献, ACL style template, double-blind, Limitations 必须有（不计入页数）, Appendix 允许但审稿人不强制审阅\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_43/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下角度严格审查：\n\n1. **新颖性**：\n   - 核心贡献（correlation-selection gap + diagnostic framework）相对于 Yao et al. (2026), Yun et al. (2025), Landesberg et al. (2026) 的增量是否足够？\n   - Entity-level decomposition 相对于 instance-level 分析的增量贡献是否有说服力？\n   - 论文是否更像一篇 empirical study / negative results paper？这在 EMNLP 2026 的接收标准下是否足够？\n   - \"Primarily diagnostic with limited predictive power\" 的定位是否削弱了论文的价值？\n\n2. **相关工作覆盖**：\n   - 是否遗漏了重要的 related work？特别是：\n     - Test-time compute scaling 最新进展（2025-2026）\n     - MBR decoding for structured prediction\n     - Calibration and uncertainty estimation for LLMs\n     - Self-consistency variants (USC, atomic SC)\n   - 与 concurrent work (Landesberg et al.) 的对比是否公平、充分？\n   - Table 1 (novelty comparison) 的维度选择是否有 cherry-picking 嫌疑？\n\n3. **写作质量与完整性**：\n   - 论文结构是否清晰？8 页正文的信息密度是否合理？\n   - Abstract 的 claims 是否与正文证据一致？数值引用是否准确？\n   - 标题 \"Why Self-Consistency Fails for NER\" 是否与内容匹配？（论文既有 failure 分析也有 conditional success）\n   - Limitations section 是否充分？\n   - 正文数字密度是否影响可读性？\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内？\n   - 匿名化是否彻底？\n   - 引用格式是否符合 ACL 标准？\n   - Limitations 是否在正文内（非 Appendix）？\n\n请按 Strengths / Weaknesses / Questions / Missing References 的结构输出审稿意见。Weaknesses 按严重程度分 [MUST-FIX] / [SHOULD-FIX] / [MINOR]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性、相关工作覆盖、写作完整性**方向的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper, 正文 8 页 + 无限参考文献, ACL style template, double-blind, Limitations 必须有（不计入页数）, Appendix 允许但审稿人不强制审阅\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_43/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下角度严格审查：\n\n1. **新颖性**：\n   - 核心贡献（correlation-selection gap + diagnostic framework）相对于 Yao et al. (2026), Yun et al. (2025), Landesberg et al. (2026) 的增量是否足够？\n   - Entity-level decomposition 相对于 instance-level 分析的增量贡献是否有说服力？\n   - 论文是否更像一篇 empirical study / negative results paper？这在 EMNLP 2026 的接收标准下是否足够？\n   - \"Primarily diagnostic with limited predictive power\" 的定位是否削弱了论文的价值？\n\n2. **相关工作覆盖**：\n   - 是否遗漏了重要的 related work？特别是：\n     - Test-time compute scaling 最新进展（2025-2026）\n     - MBR decoding for structured prediction\n     - Calibration and uncertainty estimation for LLMs\n     - Self-consistency variants (USC, atomic SC)\n   - 与 concurrent work (Landesberg et al.) 的对比是否公平、充分？\n   - Table 1 (novelty comparison) 的维度选择是否有 cherry-picking 嫌疑？\n\n3. **写作质量与完整性**：\n   - 论文结构是否清晰？8 页正文的信息密度是否合理？\n   - Abstract 的 claims 是否与正文证据一致？数值引用是否准确？\n   - 标题 \"Why Self-Consistency Fails for NER\" 是否与内容匹配？（论文既有 failure 分析也有 conditional success）\n   - Limitations section 是否充分？\n   - 正文数字密度是否影响可读性？\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内？\n   - 匿名化是否彻底？\n   - 引用格式是否符合 ACL 标准？\n   - Limitations 是否在正文内（非 Appendix）？\n\n请按 Strengths / Weaknesses / Questions / Missing References 的结构输出审稿意见。Weaknesses 按严重程度分 [MUST-FIX] / [SHOULD-FIX] / [MINOR]。"
  }
}
```

</details>

---


### Tool result

_source line 4635 · 2026-05-23T08:35:07.767320+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1560
}
```

</details>

---


### Assistant

_source line 4636 · 2026-05-23T08:35:19.501147+00:00_

Round 1 已派发：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已启动 | 方法严谨性 / 实验设计 / 统计分析 |
| Reviewer 2 | ✅ 已启动 | 新颖性 / 相关工作 / 写作完整性 |
| 视觉审查 Agent | ✅ 已启动 | PDF 排版质量（非评分项） |
| 外部审稿 | ⏭️ 跳过 | 未配置 |

等待两位 Reviewer 返回初审意见，收到后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 350

## Round 350

2 recorded events


### User

_source line 4637 · 2026-05-23T08:41:18.504066+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性、实验设计、统计分析）

### 总体评分
**Overall**: 3.5 — Borderline Conference
**Soundness**: 3/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5

**一句话总结**: 研究问题新颖、实证覆盖面广、统计报告透明，但核心形式化贡献（degeneracy decomposition bound）过松缺乏实用价值，2–3 seeds 的统计推断力不足以支撑多处 per-configuration 结论，且观察性设计下的因果性措辞需降级。

---

### Strengths

**S1. 新颖且有价值的核心发现。** "Correlation-selection gap"——质量估计信号可预测输出质量（AUROC 达 0.82, Table 4）但无法转化为 instance-level selection gains（≤1pp）——是一个此前未被系统识别的重要现象。

**S2. 系统性极高的实证覆盖。** 4 个 NER 数据集 + RE 扩展 + SQL parsing 探索，5 个信号族，2 个模型族 + 3 个 scale + GPT-5.5，共 57 项统计检验，46 页 appendix 包含大量 robustness checks。

**S3. 统计报告的透明度。** 同时报告 global Holm (k=57) 和 per-family Holm (k=10)，明确报告 p_adj=0.055 的边界情况，附 post-hoc power analysis、bootstrap CI、permutation tests。

**S4. Degeneracy 概念框架清晰。** 将 gap 分解为结构性层（信号赋予所有候选相同分数）和诊断性层（LP 逐样本信号被退化压缩），概念清晰且有说服力。

**S5. 多角度 robustness 验证。** 自由格式解码、LoRA 消融、cross-dataset entailment、温度/N 联合分析、few-shot vs. zero-shot 等系统性排除混淆变量。

---

### Must-Fix 问题

**N1** [critical] **2–3 seeds 统计推断力严重不足**
- 位置：§7.1, Table 2 (2-seed mean±σ), Table 4, Appendix ad.3
- Table 42 的 bootstrap CI 显示 LP Δ 的 95% CI 为 [-0.41, +2.54]，跨越零点。Post-hoc power analysis 显示 ρ=0.3 需 n≈85 达到 80% power。选择效应 Δ（通常 <0.5pp）与 seed 间变异处于同一量级。
- 建议：主表 seed 数增至 5+，正文 claim 附 CI，否定性断言改为 "we lack power to detect"。

**N2** [critical] **Degeneracy decomposition bound 过松（仅恢复 6.8% oracle gap）**
- 位置：§6.3, Corollary 1, Appendix r.3 Table 33
- Bound 既不能指导实践（太松以至于几乎总是满足），也不提供理论洞察的精确性。被列为四大贡献之一但实际贡献更接近存在性定理。
- 建议：在正文中报告 6.8% 恢复率（当前仅在 Appendix），降低论述调性，或探索更紧 bound。

**N3** [critical] **观察性设计下因果性措辞系统性过强**
- 位置：§1 "jointly determine", §4 "eliminates the variation", §6.2 "inverse scaling", §8 "localizing failure"
- 论文自述 observational (§3)，但多处使用因果语言。Few-NERD 3-epoch vs. 5-epoch 恰好显示训练收敛状态同时改变 degeneracy 和 LP-quality alignment——混淆变量的直接证据。
- 建议：系统性替换因果措辞为关联性描述，增加混淆变量讨论。

---

### Should-Fix 问题

**W1** [warning] Holm family 划分未预注册，影响核心显著性结论（global p_adj=0.055 vs. per-family p_adj=0.006）

**W2** [warning] Few-NERD 训练 epoch 混淆未充分解决，3-epoch vs. 5-epoch 无法分离 degeneracy 和 alignment 效应

**W3** [warning] Entity construction 与 MBR 的理论联系偏弱，entity independence 假设在 degenerate regime 下可能失效

**W4** [warning] 模型多样性有限（仅 Qwen + LLaMA 两个开源家族），无法排除 architecture-specific degeneracy pattern

**W5** [warning] RE 和 SQL 扩展过于初步，与 abstract 中 "cross-task exploration" 的宣传不匹配

---

### Questions to Authors

Q1: Bound 的 6.8% 恢复率是否已是阶最优？是否考虑了 incorporating signal correlation structure 的更紧 alternatives？

Q2: Free-form decoding 一致性反转 RE LP selection (Appendix s)。Correlation-selection gap 是否 decoding-strategy-dependent？结论适用范围需怎样限定？

Q3: Entity construction θ 在不同数据集间差异大（0.15–0.35），依赖 held-out data 选择——是否削弱了 pre-deployment diagnostic 的实用性？

Q4: 69% inverse scaling 的 N-transitions 统计是跨所有 configurations 汇总的。高/低 degeneracy 子群的比例是否显著不同？

---

### Missing References
- Malinin & Gales (2021) "Uncertainty Estimation in Autoregressive Structured Prediction"
- Kadavath et al. (2022) 已引用但与 hidden state probe 实验的对比不充分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4638 · 2026-05-23T08:41:25.137244+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 351

## Round 351

2 recorded events


### User

_source line 4639 · 2026-05-23T08:41:29.567366+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 Overall 3.5（Borderline Conference），Soundness 3/5，Excitement 3.5/5。识别出 3 个 Must-Fix 问题（2–3 seeds 统计功效不足、degeneracy bound 过松仅恢复 6.8% oracle gap、观察性设计下因果措辞过强）和 5 个 Should-Fix 问题（Holm family 划分未预注册、Few-NERD epoch 混淆、MBR 理论联系偏弱、模型多样性不足、RE/SQL 扩展过于初步）。论文的核心发现（correlation-selection gap）新颖且有价值，实证覆盖面和统计透明度值得肯定，但形式化贡献的实用性和统计推断力是主要瓶颈。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4640 · 2026-05-23T08:41:34.859331+00:00_

收到 Reviewer 1 的审稿意见。等待 Reviewer 2 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 352

## Round 352

6 recorded events


### User

_source line 4641 · 2026-05-23T08:43:00.892373+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）
**审查侧重**: 新颖性、相关工作覆盖、写作完整性

---

## 总体评分
**Overall**: 3.0 / 5（Findings）
**一句话总结**: 扎实的实证分析揭示了 NER self-consistency 中 correlation-selection gap 的真实现象，但核心贡献偏分析性、处方性结果统计显著性不足、标题过度承诺，novelty 和 excitement 不够支撑主会议接收。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体可靠，五种信号的定义和评估设计合理；但构建性结果（entity-level construction）的全局校正 p_adj=0.055 超过 α=0.05，处方性 claim 的统计基础不牢固 |
| Excitement | 2.5/5 | 现象本身有价值（correlation ≠ selection），但 SC 在结构化输出上效果差是相对可预期的直觉；诊断框架缺乏预测能力（论文自认"primarily diagnostic"），实用价值有限 |
| Reproducibility | 4/5 | 实验设置详细（4 个 NER 数据集、2 个模型族、N∈{2,...,64}），承诺开源代码，附录提供大量补充实验；超参数和信号定义清晰 |
| Reviewer Confidence | 4/5 | 熟悉 test-time scaling、self-consistency、NER evaluation 领域 |

---

## 主要优势

**S1. Correlation-selection gap 的系统性揭示**：论文清晰地展示了质量估计信号（ρ 达 0.45, AUROC 0.82）为何无法转化为选择增益（<1pp），并通过 degeneracy 和 signal alignment collapse 两个维度给出了合理的分解。这一发现对 NER 实践者有直接价值——避免在无效的重复采样上浪费推理预算（Section 4, Figure 2）。

**S2. 分析的全面性和严谨性**：跨 4 个 NER 数据集、2 个模型族（Qwen3, LLaMA-3.1）、多个 N 值、3 个训练种子的验证；degeneracy decomposition（§6.3）提供了理论性的 bound；鲁棒性分析（§7.4）覆盖温度、种子、N 的敏感性。附录内容丰富（46 页总计），包括 calibration 分析、mechanistic probes、cross-dataset transfer 等。

**S3. 与 concurrent work 的坦诚对比**：Table 1 和 §2 对 Landesberg et al. (2026) 的定位诚实，承认 concurrent discovery validates the gap as cross-domain，并明确列出四个维度的差异。

**S4. Limitations 的自我批判**：Abstract 中 "primarily diagnostic, with limited predictive power" 和 Limitations section 中对 RE/SQL pilot 规模、probe 跨模型迁移未验证等问题的坦诚讨论，体现了良好的学术态度。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 标题-内容不匹配："Why Self-Consistency Fails for NER" 过度简化
- 具体位置：Title; §5 Adaptive Methods; §7.5 Prescriptive Results
- 问题：标题断言 SC "fails" for NER，但论文本身展示了有条件的成功——entity-level construction 在 Few-NERD 上 +1.40pp（§7.5），cross-model ensemble 也有正向结果（§5.1）。§8 Conclusion 明确说 "low degeneracy with strong alignment may justify entity construction"。标题的绝对性措辞与正文的 conditional/nuanced 结论不一致。
- 为什么影响接收：标题是论文的第一印象和检索入口。过度负面的标题既不准确反映贡献，也可能误导读者认为这是一篇纯 negative results paper，削弱论文在审稿中的 excitement 评分。
- 建议修改方向：加入条件性修饰，如 "When and Why Self-Consistency Fails for NER" 或 "The Limits of Self-Consistency for NER: ..."。

**N2** [critical] 处方性结果的统计显著性不足以支撑核心 claim
- 具体位置：Abstract line 6; §7.5; Table 3
- 问题：Entity-level construction 的全局 Holm-Bonferroni 校正 p_adj=0.055，超过常用 α=0.05 阈值。论文同时报告了 per-family 校正 p_adj=0.006，但这是更宽松的校正方式（k=10 vs k=57）。Abstract 中先写 per-family 值再写 global 值（"per-family Holm p_adj=0.006, global p_adj=0.055"），读者可能优先注意到更显著的值。
- 关键问题：如果最严格的校正下不显著，论文的 prescriptive claim（"yields conditional gains"）的可靠性存疑。这直接关系到论文是否仅仅是 diagnostic（分析性贡献）还是也有 prescriptive（处方性贡献）。
- 为什么影响接收：处方性结果是论文区别于 "pure negative results" 的关键差异点。如果这个结果站不住，论文的 novelty 进一步下降——变成一篇纯分析性论文。
- 建议修改方向：(a) 在正文中明确承认全局校正不显著并讨论其含义；(b) 增加额外的实验（如更多数据集/模型）来增强统计 power；或 (c) 将 prescriptive 结果降级为 exploratory observation 而非 claim。

**N3** [critical] Table 1 维度选择存在 cherry-picking 嫌疑
- 具体位置：Table 1 (§2 Related Work)
- 问题：七个对比维度的选择系统性地有利于本文：
  - "Prescriptive: No/No/No/Conditional"——但本文的 prescriptive 结果全局校正下不显著（N2）
  - "Scale range: Single/---/Single/4B-72B+API"——但本文的跨规模实验自认为 "tentative cross-scale observations"（Abstract, Limitations）
  - "Failure decomp."和"Diagnostics"两个维度高度重叠，本质上是在同一个贡献上重复打分
  - 缺少可能对竞争工作有利的维度：理论分析深度（Landesberg 提供了 reward correlation structure 的分析）、评估规模（Landesberg 在标准 reasoning benchmarks 上有更大规模实验）、实际可部署性
- 为什么影响接收：这种对比方式可能被审稿人视为不公平的自我推销（self-promotion），降低论文的可信度。
- 建议修改方向：(a) 增加对竞争工作有利的维度（如 theoretical analysis depth, evaluation scale）使对比更平衡；(b) 将 "Failure decomp." 和 "Diagnostics" 合并为一个维度；(c) 在文本中显式承认竞争工作在某些方面的优势。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 数字密度严重影响可读性
- 具体位置：Abstract（~15 个具体数值）; §1 Introduction（每段 5+ 数字）; §7 全节
- 问题：Abstract 第 4-6 句连续出现 "AUROC up to 0.82"、"<1 pp"、"+1.40 pp"、"77-91%"、"p_adj=0.006"、"p_adj=0.055"、"69%"，读者难以抓住核心信息。正文 §7 同样，几乎每句都有 2-3 个数字。
- 建议：Abstract 保留 3-4 个最关键的数字，其余移至正文。正文中用趋势描述（"consistently negative"、"marginal at best"）替代部分精确数值，精确数字集中在表格中呈现。

**W2** [warning] RE 和 SQL extensions 过于初步却占据较多篇幅
- 具体位置：Abstract line 3 ("preliminary RE (n=397) and SQL (n=196) pilots"); §1 Introduction; §8; Limitations
- 问题：RE（n=397，单数据集）和 SQL（n=196）规模太小，不足以支撑跨任务泛化的结论。但它们出现在 Abstract 和 Introduction 中，给读者一种论文覆盖面比实际更广的印象。论文在 Limitations 中承认了这一点，但 framing 上仍在 oversell。
- 建议：在 Abstract 中删除或大幅缩减 RE/SQL 的提及，将其明确定位为 "brief case studies in Appendix" 而非正文核心贡献。

**W3** [warning] "Primarily diagnostic with limited predictive power" 的定位削弱论文价值
- 具体位置：Abstract line 7; §8 Discussion
- 问题：论文自认框架 "primarily diagnostic, with limited predictive power for identifying favorable conditions"。这意味着：(a) 框架无法事前预测哪些实例会受益于 scaling；(b) 实践者需要先运行 N 次采样才能诊断——但如果已经运行了，诊断的边际价值有限。这使得框架的实用场景收窄到 "决定是否值得部署 SC" 的一次性决策。
- 建议：更清晰地阐述框架的实际使用场景。例如，可以强调 N=8 的 quick diagnostic（§8 Conclusion 提到）作为低成本预部署检查，突出其成本效益。

**W4** [warning] 相关工作中可能遗漏的方向
- 具体位置：§2 Related Work
- 问题：以下方向未被充分讨论：
  1. **Self-verification / self-debugging for structured outputs**: 如 Shinn et al. (2023, Reflexion) 的迭代自我验证方法——虽然 §5 提到了 self-refine，但 Reflexion 等环境反馈驱动的方法在结构化任务上的应用值得讨论
  2. **Ensemble methods for NER beyond voting**: 传统 NER 系统大量使用 ensemble/stacking 方法（如 CRF ensemble, BiLSTM-CRF bagging），这些方法与 LLM 时代的 self-consistency 在结构化输出上面临类似挑战——这种历史联系值得提及
  3. **Structured prediction under uncertainty**: Malinin & Gales (2021) 关于自回归结构化预测中的不确定性估计在 bib 中存在但似乎未在正文中充分讨论
  4. **Recent LLM reasoning scaling work (2025-2026)**: DeepSeek-R1 等 reasoning model 的 test-time scaling 结果——虽然是 reasoning 领域，但作为 contrast 有价值
- 说明：§2 的覆盖已经相当好（USC、atomic SC、MBR、calibration 都有），以上是 marginal improvements。

---

## 小问题（不影响接收）

- **M1**: Footnote 1 (p.1) 关于 RE F1 被 entity span errors confound 的说明很重要，建议提升到正文而非脚注。
- **M2**: §1 Introduction 的 4-stage roadmap (Discover/Diagnose/Explore/Mechanistic evidence) 中第 4 点 "Mechanistic evidence" 在 Appendix 中而非正文中，是否适合作为正文贡献点列出？
- **M3**: Figure 1 caption 中 "(diagnostic sequence, not causal chain)" 的说明容易被忽略，但对理解框架至关重要。建议在 §3 首段也明确提及。
- **M4**: §6.3 Degeneracy Decomposition 中 Proposition 的符号 (D, G_nd, α) 在首次引入时定义不够直观，需要反复回看 §3 才能理解。

---

## 关于新颖性的整体判断

论文的核心贡献是 **实证性的诊断发现** 而非方法创新。Correlation-selection gap 本身是一个有价值的发现，但：

1. **SC 在结构化输出上表现不佳**在直觉上是可预期的——majority voting 的有效性依赖于 output space 的离散性和可枚举性；entity set 的部分重叠天然破坏了这个前提。论文的贡献在于量化了这个直觉，但 "量化一个预期中的现象" 的 excitement 低于 "发现一个反直觉的现象"。

2. 论文定位为 empirical study / negative results paper 更为准确。ARR guidelines 明确鼓励这类论文（"the community does need to know"），但接收标准通常要求 actionable insights——而本文的 prescriptive results 统计显著性不足（N2）。

3. 相对于三个主要 baseline（Yao, Yun, Landesberg），增量贡献主要在于 **instance-level granularity** 和 **NER-specific failure mechanisms**。这是有价值的，但可能更适合 Findings 而非 Main Conference。

---

## 格式合规检查

| 项目 | 状态 | 说明 |
|------|------|------|
| 正文页数 | ✅ 合规 | 主体 Sections 1-8 = 8 页 |
| Limitations section | ✅ 合规 | 在正文中（Section 8 之后、Ethics Statement 之前），非 Appendix |
| 匿名化 | ✅ 合规 | Author = "Anonymous"，代码 URL = "[anonymized URL]" |
| 引用格式 | ✅ 合规 | 使用 \citet / \citep 标准 ACL 格式 |
| ACL style template | ✅ 合规 | \usepackage[review]{acl} |

---

**总结**：一篇严谨的实证分析论文，揭示了 NER self-consistency 中有价值的 correlation-selection gap 现象。但标题过度承诺（N1）、核心处方性结果统计不显著（N2）、对比维度有 cherry-picking 嫌疑（N3）三个问题限制了论文的可信度和 excitement。建议定位为 Findings 级别。修改 N1-N3 后有望达到 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4642 · 2026-05-23T08:43:53.484339+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Round 1）\n**审查侧重**: 新颖性、相关工作覆盖、写作完整性\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings）\n\n## Must-Fix 问题\n\n**N1** [critical] 标题-内容不匹配：\"Why Self-Consistency Fails for NER\" 过度简化\n- 标题断言 SC \"fails\" for NER，但论文本身展示了有条件的成功——entity-level construction 在 Few-NERD 上 +1.40pp（§7.5），cross-model ensemble 也有正向结果（§5.1）。§8 Conclusion 明确说 \"low degeneracy with strong alignment may justify entity construction\"。标题的绝对性措辞与正文的 conditional/nuanced 结论不一致。\n- 建议修改方向：加入条件性修饰，如 \"When and Why Self-Consistency Fails for NER\" 或 \"The Limits of Self-Consistency for NER: ...\"。\n\n**N2** [critical] 处方性结果的统计显著性不足以支撑核心 claim\n- Entity-level construction 的全局 Holm-Bonferroni 校正 p_adj=0.055，超过常用 α=0.05 阈值。论文同时报告了 per-family 校正 p_adj=0.006，但这是更宽松的校正方式（k=10 vs k=57）。Abstract 中先写 per-family 值再写 global 值（\"per-family Holm p_adj=0.006, global p_adj=0.055\"），读者可能优先注意到更显著的值。\n- 如果最严格的校正下不显著，论文的 prescriptive claim（\"yields conditional gains\"）的可靠性存疑。\n- 建议：(a) 在正文中明确承认全局校正不显著并讨论其含义；(b) 增加额外实验；或 (c) 将 prescriptive 结果降级为 exploratory observation。\n\n**N3** [critical] Table 1 维度选择存在 cherry-picking 嫌疑\n- 七个对比维度的选择系统性地有利于本文：\n  - \"Prescriptive: No/No/No/Conditional\"——但本文的 prescriptive 结果全局校正下不显著\n  - \"Scale range: Single/---/Single/4B-72B+API\"——但本文的跨规模实验自认为 \"tentative\"\n  - \"Failure decomp.\"和\"Diagnostics\"两个维度高度重叠\n  - 缺少可能对竞争工作有利的维度：理论分析深度、评估规模、实际可部署性\n- 建议：增加对竞争工作有利的维度，合并重叠维度。\n\n## Should-Fix 问题\n\n**W1** [warning] 数字密度严重影响可读性\n- Abstract（~15 个具体数值），§1 Introduction（每段 5+ 数字），§7 全节。读者难以抓住核心信息。\n- 建议：Abstract 保留 3-4 个最关键的数字，其余移至正文。\n\n**W2** [warning] RE 和 SQL extensions 过于初步却占据较多篇幅\n- RE（n=397，单数据集）和 SQL（n=196）规模太小，不足以支撑跨任务泛化的结论。但出现在 Abstract 和 Introduction 中。\n- 建议：在 Abstract 中删除或大幅缩减 RE/SQL 的提及。\n\n**W3** [warning] \"Primarily diagnostic with limited predictive power\" 的定位削弱论文价值\n- 框架无法事前预测哪些实例会受益；实践者需要先运行 N 次采样才能诊断——诊断的边际价值有限。\n- 建议：更清晰地阐述框架的实际使用场景，突出低成本预部署检查。\n\n**W4** [warning] 相关工作中可能遗漏的方向\n- Self-verification/self-debugging (Reflexion), ensemble methods for NER beyond voting (CRF ensemble, BiLSTM-CRF bagging), structured prediction under uncertainty (Malinin & Gales 2021), recent LLM reasoning scaling work (DeepSeek-R1)\n\n## 小问题\n- M1: Footnote 1 关于 RE F1 被 entity span errors confound 的说明建议提升到正文\n- M2: Mechanistic evidence 在 Appendix 中却作为正文贡献点列出\n- M3: Figure 1 caption 中 \"(diagnostic sequence, not causal chain)\" 建议在 §3 首段也明确提及\n- M4: §6.3 符号定义不够直观\n\n## 新颖性整体判断\n论文核心贡献是实证性诊断发现而非方法创新。SC 在结构化输出上表现不佳在直觉上是可预期的。论文定位为 Findings 更准确。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Round 1）\n**审查侧重**: 新颖性、相关工作覆盖、写作完整性\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings）\n\n## Must-Fix 问题\n\n**N1** [critical] 标题-内容不匹配：\"Why Self-Consistency Fails for NER\" 过度简化\n- 标题断言 SC \"fails\" for NER，但论文本身展示了有条件的成功——entity-level construction 在 Few-NERD 上 +1.40pp（§7.5），cross-model ensemble 也有正向结果（§5.1）。§8 Conclusion 明确说 \"low degeneracy with strong alignment may justify entity construction\"。标题的绝对性措辞与正文的 conditional/nuanced 结论不一致。\n- 建议修改方向：加入条件性修饰，如 \"When and Why Self-Consistency Fails for NER\" 或 \"The Limits of Self-Consistency for NER: ...\"。\n\n**N2** [critical] 处方性结果的统计显著性不足以支撑核心 claim\n- Entity-level construction 的全局 Holm-Bonferroni 校正 p_adj=0.055，超过常用 α=0.05 阈值。论文同时报告了 per-family 校正 p_adj=0.006，但这是更宽松的校正方式（k=10 vs k=57）。Abstract 中先写 per-family 值再写 global 值（\"per-family Holm p_adj=0.006, global p_adj=0.055\"），读者可能优先注意到更显著的值。\n- 如果最严格的校正下不显著，论文的 prescriptive claim（\"yields conditional gains\"）的可靠性存疑。\n- 建议：(a) 在正文中明确承认全局校正不显著并讨论其含义；(b) 增加额外实验；或 (c) 将 prescriptive 结果降级为 exploratory observation。\n\n**N3** [critical] Table 1 维度选择存在 cherry-picking 嫌疑\n- 七个对比维度的选择系统性地有利于本文：\n  - \"Prescriptive: No/No/No/Conditional\"——但本文的 prescriptive 结果全局校正下不显著\n  - \"Scale range: Single/---/Single/4B-72B+API\"——但本文的跨规模实验自认为 \"tentative\"\n  - \"Failure decomp.\"和\"Diagnostics\"两个维度高度重叠\n  - 缺少可能对竞争工作有利的维度：理论分析深度、评估规模、实际可部署性\n- 建议：增加对竞争工作有利的维度，合并重叠维度。\n\n## Should-Fix 问题\n\n**W1** [warning] 数字密度严重影响可读性\n- Abstract（~15 个具体数值），§1 Introduction（每段 5+ 数字），§7 全节。读者难以抓住核心信息。\n- 建议：Abstract 保留 3-4 个最关键的数字，其余移至正文。\n\n**W2** [warning] RE 和 SQL extensions 过于初步却占据较多篇幅\n- RE（n=397，单数据集）和 SQL（n=196）规模太小，不足以支撑跨任务泛化的结论。但出现在 Abstract 和 Introduction 中。\n- 建议：在 Abstract 中删除或大幅缩减 RE/SQL 的提及。\n\n**W3** [warning] \"Primarily diagnostic with limited predictive power\" 的定位削弱论文价值\n- 框架无法事前预测哪些实例会受益；实践者需要先运行 N 次采样才能诊断——诊断的边际价值有限。\n- 建议：更清晰地阐述框架的实际使用场景，突出低成本预部署检查。\n\n**W4** [warning] 相关工作中可能遗漏的方向\n- Self-verification/self-debugging (Reflexion), ensemble methods for NER beyond voting (CRF ensemble, BiLSTM-CRF bagging), structured prediction under uncertainty (Malinin & Gales 2021), recent LLM reasoning scaling work (DeepSeek-R1)\n\n## 小问题\n- M1: Footnote 1 关于 RE F1 被 entity span errors confound 的说明建议提升到正文\n- M2: Mechanistic evidence 在 Appendix 中却作为正文贡献点列出\n- M3: Figure 1 caption 中 \"(diagnostic sequence, not causal chain)\" 建议在 §3 首段也明确提及\n- M4: §6.3 符号定义不够直观\n\n## 新颖性整体判断\n论文核心贡献是实证性诊断发现而非方法创新。SC 在结构化输出上表现不佳在直觉上是可预期的。论文定位为 Findings 更准确。"
  }
}
```

</details>

---


### Tool result

_source line 4643 · 2026-05-23T08:44:22.501313+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29016
}
```

</details>

---


### Tool call

_source line 4644 · 2026-05-23T08:44:22.703538+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Round 1）\n**审查侧重**: 方法严谨性、实验设计、统计分析\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 3/5 | **Excitement**: 3.5/5\n\n## Must-Fix 问题\n\n**N1** [critical] 2–3 seeds 统计推断力严重不足\n- Table 42 的 bootstrap CI 显示 LP Δ 的 95% CI 为 [-0.41, +2.54]，跨越零点。Post-hoc power analysis 显示 ρ=0.3 需 n≈85 达到 80% power。选择效应 Δ（通常 <0.5pp）与 seed 间变异处于同一量级。\n- 建议：主表 seed 数增至 5+，正文 claim 附 CI，否定性断言改为 \"we lack power to detect\"。\n\n**N2** [critical] Degeneracy decomposition bound 过松（仅恢复 6.8% oracle gap）\n- Bound 既不能指导实践（太松以至于几乎总是满足），也不提供理论洞察的精确性。被列为四大贡献之一但实际贡献更接近存在性定理。\n- 建议：在正文中报告恢复率（当前仅在 Appendix），降低论述调性，或探索更紧 bound。\n\n**N3** [critical] 观察性设计下因果性措辞系统性过强\n- §1 \"jointly determine\", §4 \"eliminates the variation\", §6.2 \"inverse scaling\", §8 \"localizing failure\"\n- 论文自述 observational (§3)，但多处使用因果语言。Few-NERD 3-epoch vs. 5-epoch 恰好显示训练收敛状态同时改变 degeneracy 和 LP-quality alignment——混淆变量的直接证据。\n- 建议：系统性替换因果措辞为关联性描述，增加混淆变量讨论。\n\n## Should-Fix 问题\n\n**W1** [warning] Holm family 划分未预注册，影响核心显著性结论（global p_adj=0.055 vs. per-family p_adj=0.006）\n\n**W2** [warning] Few-NERD 训练 epoch 混淆未充分解决，3-epoch vs. 5-epoch 无法分离 degeneracy 和 alignment 效应\n\n**W3** [warning] Entity construction 与 MBR 的理论联系偏弱，entity independence 假设在 degenerate regime 下可能失效\n\n**W4** [warning] 模型多样性有限（仅 Qwen + LLaMA 两个开源家族），无法排除 architecture-specific degeneracy pattern\n\n**W5** [warning] RE 和 SQL 扩展过于初步，与 abstract 中 \"cross-task exploration\" 的宣传不匹配\n\n## Questions to Authors\n\nQ1: Bound 的 6.8% 恢复率是否已是阶最优？是否考虑了 incorporating signal correlation structure 的更紧 alternatives？\n\nQ2: Free-form decoding 一致性反转 RE LP selection。Correlation-selection gap 是否 decoding-strategy-dependent？\n\nQ3: Entity construction θ 在不同数据集间差异大（0.15–0.35），依赖 held-out data 选择——是否削弱了 pre-deployment diagnostic 的实用性？\n\nQ4: 69% inverse scaling 的 N-transitions 统计是跨所有 configurations 汇总的。高/低 degeneracy 子群的比例是否显著不同？\n\n## Missing References\n- Malinin & Gales (2021) \"Uncertainty Estimation in Autoregressive Structured Prediction\"\n- Kadavath et al. (2022) 已引用但与 hidden state probe 实验的对比不充分"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Round 1）\n**审查侧重**: 方法严谨性、实验设计、统计分析\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 3/5 | **Excitement**: 3.5/5\n\n## Must-Fix 问题\n\n**N1** [critical] 2–3 seeds 统计推断力严重不足\n- Table 42 的 bootstrap CI 显示 LP Δ 的 95% CI 为 [-0.41, +2.54]，跨越零点。Post-hoc power analysis 显示 ρ=0.3 需 n≈85 达到 80% power。选择效应 Δ（通常 <0.5pp）与 seed 间变异处于同一量级。\n- 建议：主表 seed 数增至 5+，正文 claim 附 CI，否定性断言改为 \"we lack power to detect\"。\n\n**N2** [critical] Degeneracy decomposition bound 过松（仅恢复 6.8% oracle gap）\n- Bound 既不能指导实践（太松以至于几乎总是满足），也不提供理论洞察的精确性。被列为四大贡献之一但实际贡献更接近存在性定理。\n- 建议：在正文中报告恢复率（当前仅在 Appendix），降低论述调性，或探索更紧 bound。\n\n**N3** [critical] 观察性设计下因果性措辞系统性过强\n- §1 \"jointly determine\", §4 \"eliminates the variation\", §6.2 \"inverse scaling\", §8 \"localizing failure\"\n- 论文自述 observational (§3)，但多处使用因果语言。Few-NERD 3-epoch vs. 5-epoch 恰好显示训练收敛状态同时改变 degeneracy 和 LP-quality alignment——混淆变量的直接证据。\n- 建议：系统性替换因果措辞为关联性描述，增加混淆变量讨论。\n\n## Should-Fix 问题\n\n**W1** [warning] Holm family 划分未预注册，影响核心显著性结论（global p_adj=0.055 vs. per-family p_adj=0.006）\n\n**W2** [warning] Few-NERD 训练 epoch 混淆未充分解决，3-epoch vs. 5-epoch 无法分离 degeneracy 和 alignment 效应\n\n**W3** [warning] Entity construction 与 MBR 的理论联系偏弱，entity independence 假设在 degenerate regime 下可能失效\n\n**W4** [warning] 模型多样性有限（仅 Qwen + LLaMA 两个开源家族），无法排除 architecture-specific degeneracy pattern\n\n**W5** [warning] RE 和 SQL 扩展过于初步，与 abstract 中 \"cross-task exploration\" 的宣传不匹配\n\n## Questions to Authors\n\nQ1: Bound 的 6.8% 恢复率是否已是阶最优？是否考虑了 incorporating signal correlation structure 的更紧 alternatives？\n\nQ2: Free-form decoding 一致性反转 RE LP selection。Correlation-selection gap 是否 decoding-strategy-dependent？\n\nQ3: Entity construction θ 在不同数据集间差异大（0.15–0.35），依赖 held-out data 选择——是否削弱了 pre-deployment diagnostic 的实用性？\n\nQ4: 69% inverse scaling 的 N-transitions 统计是跨所有 configurations 汇总的。高/低 degeneracy 子群的比例是否显著不同？\n\n## Missing References\n- Malinin & Gales (2021) \"Uncertainty Estimation in Autoregressive Structured Prediction\"\n- Kadavath et al. (2022) 已引用但与 hidden state probe 实验的对比不充分"
  }
}
```

</details>

---


### Tool result

_source line 4645 · 2026-05-23T08:44:24.168323+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1464
}
```

</details>

---


### Assistant

_source line 4646 · 2026-05-23T08:44:27.933225+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 353

## Round 353

2 recorded events


### User

_source line 4647 · 2026-05-23T08:44:30.582540+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall 3.0（Findings 级别）。三个 Must-Fix 问题：(1) 标题 "Why Self-Consistency Fails for NER" 与正文有条件成功结果不匹配；(2) entity-level construction 的处方性 claim 全局 Holm 校正 p_adj=0.055 不显著，统计基础不足；(3) Table 1 novelty comparison 的七个维度有 cherry-picking 嫌疑（如 Failure decomp. 和 Diagnostics 重叠计分、Prescriptive 标 "Conditional" 但实际不显著）。四个 Should-Fix：数字密度过高影响可读性、RE/SQL pilot 过于初步却在 Abstract 中占位、"primarily diagnostic" 定位削弱价值、部分相关工作遗漏（self-verification for structured outputs、传统 NER ensemble）。格式合规无问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 4648 · 2026-05-23T08:44:45.749457+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 354

## Round 354

2 recorded events


### User

_source line 4649 · 2026-05-23T08:45:45.398367+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### Must-Fix

**[REBUT] R2-N1 (标题不匹配)**: 标题描述的是默认配置下的主导现象——standard sample-level selection 在全部数据集/信号上均 ≤1pp (Table 2, 4)。Entity construction +1.40pp 是严格条件限定下的结果且 global correction 不显著。标题 shorthand 在 ACL/EMNLP 中可接受。同意可改进但建议降级为 should-fix。

**[AGREE] R2-N2 (统计显著性不足)**: 与我的 N1 (seeds 不足) 和 W1 (Holm family 未预注册) 一致。补充：Table 42 bootstrap CI 跨越零点 [−0.41, +2.54]。解法是增加 seeds 而非直接降级为 exploratory。

**[REBUT] R2-N3 (Table 1 cherry-picking)**: 过度批评。"Failure decomp." 与 "Diagnostics" 是不同层次（分析 vs. 实践）。竞争工作均无形式化理论，加 "理论深度" 维度反而有利本文。维度填写均准确，选择主观性属可接受范围。建议降级为 should-fix，标注 Prescriptive 一栏的 p 值。

### Should-Fix

**[AGREE] R2-W1 (数字密度)**: Abstract ~15 个数字过多，建议保留 4-5 个最关键的。

**[AGREE] R2-W2 (RE/SQL 初步)**: 与我的 W5 一致。

**[REBUT] R2-W3 (诊断定位价值有限)**: R2 忽略了关键使用场景——已在使用 SC 的实践者可在 pilot samples (N=8) 上快速诊断。但同意 §7.5 应扩展为明确的 practitioner workflow。

**[AGREE] R2-W4 (遗漏相关工作)**: 同意 Malinin & Gales (2021) 和 Reflexion 应讨论。CRF ensemble 和 DeepSeek-R1 关联较弱，不认为是重要遗漏。

### 新颖性判断
部分不同意。SC 不 work 可预期，但 correlation-selection gap（AUROC 0.63-0.82 却 ≤1pp selection gain）是 genuinely surprising 的发现，直觉无法预见。同意整体贡献偏 empirical diagnostic，Findings 或 borderline conference 均为合理定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4650 · 2026-05-23T08:45:49.666550+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 355

## Round 355

2 recorded events


### User

_source line 4651 · 2026-05-23T08:45:52.906465+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：R2 的 7 条意见中我 AGREE 了 4 条（N2, W1, W2, W4 部分），REBUT 了 3 条（N1 建议降级为 should-fix, N3 过度批评, W3 忽略了 pilot diagnostic 场景）。核心分歧在于新颖性判断——correlation-selection gap 本身是 genuinely surprising 的发现，不能简单用"直觉可预期"打发。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4652 · 2026-05-23T08:45:57.531356+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 356

## Round 356

12 recorded events


### User

_source line 4653 · 2026-05-23T08:46:15.018871+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 2–3 seeds 统计推断力不足**

同意这是一个实质性问题。论文的核心否定性 claim（selection yields <1pp）依赖于效应量与 seed 间变异的比较，而 2-3 seeds 下置信区间过宽（Table 42 LP Δ 95% CI [-0.41, +2.54]）确实无法区分 "真无效应" 和 "检测力不足"。

补充观察：§7.4 Robustness 中报告 "Signal rankings are robust across temperatures, seeds, and N"，但 signal ranking 的稳定性不等同于 selection gain 的效应量显著性——这是两个不同的统计问题。前者是排序一致性（ordinal），后者是绝对量级的推断（cardinal）。论文混淆了这两者。

不过，我认为 R1 的建议（"主表 seed 数增至 5+"）虽然理想，但需要考虑计算成本的现实约束——每个 seed × 每个 N × 每个数据集 × 每个模型的推理量相当大。更切实的建议是：(a) 将核心 negative claim 从 "selection fails" 改为 "we find no evidence of selection gains within our statistical power"；(b) 报告 post-hoc power analysis 结果，明确当前实验能检测到的最小效应量。

**[AGREE] R1-N2: Degeneracy decomposition bound 过松**

同意。§6.3 的 bound 仅恢复 6.8% oracle gap，作为 "四大贡献之一"（§1 Explore 第 3 点）确实名不副实。

补充证据：§6.3 原文 "The bound is an intentionally loose necessary condition" 承认了松弛性，但 §1 Introduction 将其列为 "Explore [§5, §6]" 贡献时并未提及这一限制。这在 framing 上造成了不一致——§1 暗示这是一个有力的理论工具，§6.3 承认它只是存在性结论。

与我的 N3（Table 1 cherry-picking）相关：Table 1 将 "Failure decomp." 列为本文独有维度（D, α, LP），但如果 bound 本身过松，这个维度的优势被削弱。

R1 的建议（降低论述调性或探索更紧 bound）是合理的。我倾向于 "降低调性" 路线——在 §1 中将 bound 定位为 "existence result establishing when no method can help" 而非暗示它是一个精确的诊断工具。

**[AGREE] R1-N3: 因果性措辞系统性过强**

强烈同意。这是一个贯穿全文的系统性问题。

补充例证（R1 未提及的）：
- §4 标题 "Where Single-Signal Selection Fails" 暗示因果（selection 因为某些条件而失败），但实际只展示了关联
- Figure 1 caption 中的 "(diagnostic sequence, not causal chain)" 虽然有免责声明，但这个免责仅出现在一个 figure caption 中，与正文中多处的因果措辞不一致
- §8 Conclusion: "localizing failure to degeneracy and signal alignment collapse" — "localizing" 暗示因果定位

R1 指出的 Few-NERD 3-epoch vs. 5-epoch 混淆证据尤为有力：训练收敛状态同时改变了 degeneracy rate 和 LP-quality alignment，使得无法判断 construction gains 是因为低 degeneracy、强 alignment，还是因为 undertrained model 的其他特性（如更高的 output diversity 或更差的 greedy baseline）。

---

### Should-Fix 问题

**[AGREE] R1-W1: Holm family 划分未预注册**

强烈同意。我在自己的 N2 中也独立指出了这个问题。全局校正 p_adj=0.055 不显著，per-family 校正 p_adj=0.006 显著——两种分析给出矛盾结论。未预注册的 family 划分使得更宽松校正的结果可信度下降。这是影响论文核心 prescriptive claim 可靠性的关键统计问题。

**[AGREE] R1-W2: Few-NERD 训练 epoch 混淆**

同意。这与 N3 的因果性问题直接相关。3-epoch model 不仅 degeneracy 低，还可能有更弱的 greedy baseline（因为 undertrained），使得任何聚合方法都更容易显示 "改进"。论文需要控制 greedy baseline 性能来分离这两个因素。

补充：§7.5 报告 "Entity-level construction yields conditional improvement (+1.40pp on Few-NERD, 3-epoch)"——如果这个 gain 部分来自 undertrained model 的 lower greedy baseline，那么 prescriptive recommendation 的泛化性存疑。实践者通常部署的是 fully converged model，不是 3-epoch undertrained model。

**[AGREE] R1-W3: Entity construction 与 MBR 的理论联系偏弱**

部分同意。Entity independence 假设在高 degeneracy 情况下确实有问题——当 77-91% 的 samples 产生相同输出时（§7.5, convergence models），entity-level 分解无法提供额外信息。

不过，我认为这个问题的严重性比 R1 评估的略低。论文的 MBR 联系（Proposition 在 §6.1 中）主要是一个 motivational framing 而非严格理论基础。论文的 prescriptive 结果（§7.5）是实证性的，不依赖于 MBR 理论的完备性。问题在于 framing 过度而非方法本身有缺陷。

**[AGREE] R1-W4: 模型多样性有限**

部分同意。两个开源家族（Qwen3, LLaMA-3.1）确实有限，但这在当前 NER 研究中并非异常。

补充：Limitations section 提到 frontier models 展现出 "markedly different degeneracy profiles (5.5-74%; Table [frontier])"——这直接支持了 R1 的担忧。如果 GPT-5.5 的 degeneracy 低至 5.5%，而论文的核心 failure analysis 建立在 12-68% degeneracy 的开源模型上，那么结论的普适性确实受到质疑。论文标题 "Why Self-Consistency Fails for NER" 在 frontier model 上可能并不成立。

这与我的 N1（标题-内容不匹配）进一步呼应——不仅是 "有条件的成功 vs. 绝对失败"，还有 "开源模型 vs. frontier model" 的适用范围问题。

**[AGREE] R1-W5: RE 和 SQL 扩展过于初步**

完全同意。我在自己的 W2 中独立提出了相同问题。RE (n=397) 和 SQL (n=196) 的样本量过小，与 Abstract 中 "cross-task exploration" 的措辞不匹配。

---

### 对 Questions to Authors 的看法

**Q1 (Bound 阶最优性)**: 好问题。如果 6.8% 恢复率已是该分析框架下的阶最优，那么 bound 的价值定位需要改变——从 "useful diagnostic tool" 转为 "information-theoretic limit"。如果不是阶最优，则需要解释为何不追求更紧 bound。

**Q2 (Free-form decoding 一致性反转)**: 非常尖锐。如果 correlation-selection gap 是 decoding-strategy-dependent，那么论文的核心发现（gap 的普遍性）将被大幅削弱。论文在 Appendix 中有 free-form 消融但我注意到 Limitations 中说 "results are consistent across datasets"——需要验证 RE 上是否也如此。

**Q3 (θ 依赖 held-out data)**: 同意这是一个问题。如果 θ 需要 held-out tuning，那么 entity construction 作为 "pre-deployment diagnostic" 的实用性被削弱——实践者需要标注数据来选择 θ，这与 zero-resource 场景矛盾。

**Q4 (69% inverse scaling 的子群分析)**: 好问题。如果高 degeneracy 子群 inverse scaling 比例远高于低 degeneracy 子群，这实际上支持了论文的诊断框架（degeneracy 预测 scaling 失败）。但如果比例相近，则诊断框架的预测价值进一步存疑。

---

### 与我自己审稿意见的交汇总结

R1 和我（R2）在以下问题上独立达成一致：
1. **统计显著性问题**: R1-W1 ≈ R2-N2（Holm family 划分和 p_adj 问题）
2. **RE/SQL 过于初步**: R1-W5 ≈ R2-W2
3. **因果措辞过强**: R1-N3 涵盖了我在 N1（标题不匹配）中的部分关切

R1 提出了我未独立发现的重要问题：
- **Seed 数量的统计 power**（N1）——这对论文的 negative claims 有根本性影响
- **Bound 过松**（N2）——我审查侧重在 novelty，未深入评估 bound 的紧致性
- **Epoch 混淆**（W2）——我注意到 prescriptive results 的条件性但未深入分析混淆来源

两位 Reviewer 的 concerns 共同指向一个核心判断：**论文的分析质量高于其 claim 的可靠性**。框架设计合理，实验覆盖面广，但统计推断力不足以支撑正文中的 claim 强度。如果将 claims 系统性降级（N1 因果措辞、N2 bound 调性、W1 显著性表述），论文作为 Findings 级别的实证分析是合格的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4654 · 2026-05-23T08:46:43.286025+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_visual_check_status,update_review_issues,submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_visual_check_status,update_review_issues,submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 4655 · 2026-05-23T08:46:43.397751+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 111
}
```

</details>

---


### Tool call

_source line 4656 · 2026-05-23T08:46:46.205800+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_visual_check_status update_review_issues submit_review_report",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_visual_check_status update_review_issues submit_review_report",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 4657 · 2026-05-23T08:46:46.307320+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4658 · 2026-05-23T08:46:51.426733+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4659 · 2026-05-23T08:46:51.477307+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T08:34:35.567380+00:00\", \"completed_at\": \"2026-05-23T08:39:35.780590+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent timed out after 300s\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4660 · 2026-05-23T08:49:14.001413+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== ROUND 43 MUST-FIX (CONSENSUS) =====\n- id: R43-N1\n  summary: \"2-3 seeds 统计推断力不足，核心 negative claims 无法区分真无效应和检测力不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 40\n  last_seen_round: 43\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R41-W2, response-letter-only item\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未修改，仍为遗留问题\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1 升级为 Must-Fix。Table 42 bootstrap CI [-0.41, +2.54] 跨越零点。R2 AGREE 并补充：signal ranking 稳定性 ≠ 效应量显著性。两位共识：核心 negative claim 需改为 'we find no evidence within our statistical power'。\"\n\n- id: R43-N2\n  summary: \"Degeneracy decomposition bound 过松（恢复 3-12% oracle gap），作为主要贡献名不副实\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 38\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过——§6.3 重定位为 necessary condition test\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1 认为即使重定位后，§1 仍将其列为四大贡献之一，与 §6.3 的 intentionally loose 声明不一致。R2 AGREE：§1 暗示有力理论工具，§6.3 承认存在性结论，framing 不一致。\"\n\n- id: R43-N3\n  summary: \"观察性设计下因果措辞系统性过强\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1 提出：§1 'jointly determine', §4 'eliminates the variation', §6.2 'inverse scaling', §8 'localizing failure'。R2 strongly AGREE 并补充：§4 标题 'Where Single-Signal Selection Fails' 暗示因果；Figure 1 免责仅出现在 caption 中。Few-NERD 3v5 epoch 是混淆变量直接证据。\"\n\n- id: R43-N4\n  summary: \"处方性结果全局 Holm 校正不显著（p_adj=0.055），per-family 校正未预注册\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过——§7.5 提供 family 划分先验理由，双 p 值透明报告\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix：全局校正不显著削弱 prescriptive claim 可靠性。R1 AGREE：与 seeds 不足问题叠加。Abstract 中 per-family 值先于 global 值，读者优先注意更显著值。两位共识：prescriptive claim 需降级为 exploratory 或增加统计 power。\"\n\n# ===== ROUND 43 MUST-FIX (DIVERGENT) =====\n- id: R43-N5\n  summary: \"标题 'Why SC Fails for NER' 与正文 conditional success 结论不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 40\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [2]\n      note: \"R41-D1 持续分歧\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix：标题绝对性与 §7.5 conditional gains、§5.1 cross-model positive results、§8 conditional recommendation 不一致。R1 REBUT：标题描述默认配置主导现象，ACL 标准范式，建议降为 should-fix。分歧记录。\"\n\n- id: R43-N6\n  summary: \"Table 1 novelty comparison 维度选择有 cherry-picking 嫌疑\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix：Failure decomp. 和 Diagnostics 重叠计分；Prescriptive 标 Conditional 但全局不显著；缺少对竞争工作有利的维度。R1 REBUT：两维度是不同层次（分析 vs 实践），竞争工作无形式化理论，建议降为 should-fix。Director 判定：降为 warning。\"\n\n# ===== ROUND 43 SHOULD-FIX (CONSENSUS) =====\n- id: R43-W1\n  summary: \"Few-NERD 3-epoch vs 5-epoch 混淆未充分解决，无法分离 degeneracy 和 alignment 效应\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 38\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过——Abstract 条件限定充分\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix：无法分离效应。R2 AGREE 并补充：undertrained model 的 lower greedy baseline 可能放大 construction gains，实践者通常部署 fully converged model。\"\n\n- id: R43-W2\n  summary: \"RE/SQL 扩展过于初步，Abstract 中 cross-task exploration 措辞 oversell\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证 Abstract 'preliminary' 措辞充分\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1-W5 和 R2-W2 独立提出。RE (n=397, 单数据集) 和 SQL (n=196) 规模不足以支撑跨任务泛化。两位共识：应进一步缩减 Abstract/Intro 中的提及。\"\n\n- id: R43-W3\n  summary: \"正文数字密度过高，Abstract ~15 个数值影响可读性\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未变化，持续 divergence (R41-D2)\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 AGREE。Abstract ~15 数字过多，§7 每句 2-3 个数字。建议 Abstract 保留 4-5 个关键数字。本轮共识升级为 should-fix。\"\n\n- id: R43-W4\n  summary: \"Entity construction 与 MBR 理论联系偏弱，entity independence 假设在 degenerate regime 下可能失效\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1-W3 提出。R2 部分 AGREE：MBR 联系主要是 motivational framing 而非严格理论基础，prescriptive results 是实证性的不依赖 MBR 完备性。问题在 framing 过度。\"\n\n- id: R43-W5\n  summary: \"模型多样性有限（仅 Qwen + LLaMA），frontier model degeneracy profile 差异大\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1-W4 提出。R2 部分 AGREE：Limitations 提到 frontier degeneracy 5.5-74%，如果 GPT-5.5 degeneracy 低至 5.5%，论文基于 12-68% 开源模型的结论普适性存疑。\"\n\n- id: R43-W6\n  summary: \"'Primarily diagnostic with limited predictive power' 定位削弱论文实用价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2-W3 提出：框架无法事前预测，诊断边际价值有限。R1 REBUT：pilot N=8 diagnostic 有实用场景，但同意 §7.5 应扩展为明确 practitioner workflow。分歧记录。\"\n\n- id: R43-W7\n  summary: \"Entity-level decomposition 增量贡献需更强论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 41\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未修改（response-letter-only item）\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 未独立提出但 R2 在新颖性评估中提及 instance-level granularity 和 NER-specific failure mechanisms 作为增量贡献。维持 open。\"\n\n- id: R43-W8\n  summary: \"相关工作可能遗漏：Reflexion (self-verification), Malinin & Gales (2021), 传统 NER ensemble\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 部分 AGREE：Malinin & Gales (2021) 和 Reflexion 应讨论。R1 认为 CRF ensemble 和 DeepSeek-R1 关联较弱非重要遗漏。\"\n\n# ===== ROUND 43 MINOR =====\n- id: R43-M1\n  summary: \"Footnote 1 (RE F1 confound) 建议提升到正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M1：RE F1 被 entity span errors confound 的说明重要，不应仅在脚注。\"\n\n- id: R43-M2\n  summary: \"Mechanistic evidence 在 Appendix 却作为正文贡献点列出\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M2：§1 四阶段路线图第 4 点在 Appendix 中。\"\n\n- id: R43-M3\n  summary: \"§3 应在首段明确提及 diagnostic sequence 而非 causal chain\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M3：Figure 1 caption 免责容易被忽略，§3 首段也应说明。与 R43-N3 因果措辞问题相关。\"\n\n- id: R43-M4\n  summary: \"§6.3 符号 D, G_nd, α 首次引入时定义不够直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M4：需要反复回看 §3 才能理解。\"\n\n# ===== EARLIER RESOLVED (保留历史) =====\n- id: R41-N1\n  summary: \"分解 bound 仅恢复 3-12% 实际增益，核心形式化贡献实用价值不足\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§6.3 已重定位为 intentionally loose necessary condition test。\"\n  resolution: \"§6.3 成功重定位。R42 验证通过。R43 以新角度重提（R43-N2）。\"\n  resolution_round: 42\n\n- id: R41-N2\n  summary: \"核心正面 claim 统计显著性取决于多重比较校正方案选择\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 42\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§7.5 提供 family 划分先验理由，双 p 值透明报告。\"\n  resolution: \"§7.5 修改验证通过。R43 以新角度重提（R43-N4）。\"\n  resolution_round: 42\n\n- id: R41-N3\n  summary: \"Mechanistic probes 使用 Qwen2.5-7B 而非主实验 Qwen3-8B\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 42\n  resolution: \"模型差异已标注，ESJ Qwen3-8B 确认 chance-level。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-N4\n  summary: \"Novelty 与 Landesberg et al. (2026) 概念重叠，differentiation 不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 42\n  resolution: \"§2 扩展为 4 维度系统对比。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-N5\n  summary: \"Few-NERD epoch confound 严重削弱最显著正面结果\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  resolution: \"Abstract 条件限定充分。R42 验证通过。R43 以混淆分离角度重提（R43-W1）。\"\n  resolution_round: 42\n\n- id: R41-W1\n  summary: \"Diagnostic vs prescriptive 叙事定位不一致\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  resolution: \"定位统一。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-W2\n  summary: \"2-3 seeds 统计推断力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 40\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 升级为 Must-Fix (R43-N1)。\"\n\n- id: R41-W3\n  summary: \"RE/SQL 扩展过薄\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 42\n  resolution: \"Abstract 已标注 preliminary。R43 以新角度重提（R43-W2）。\"\n  resolution_round: 42\n\n- id: R41-W4\n  summary: \"Related Work 覆盖面不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 41\n  last_seen_round: 42\n  resolution: \"引用全部添加。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-W5\n  summary: \"Entity-level decomposition 增量贡献需更强论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 41\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 维持 open (R43-W7)。\"\n\n- id: R41-W6\n  summary: \"Constrained decoding 对 LP 的 confound 未充分解耦\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  resolution: \"Free-form ablation 在 3 数据集上一致。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-D1\n  summary: \"标题 'Why SC Fails for NER' 与内容匹配度\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 40\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 升级为 R43-N5。R2 Must-Fix, R1 REBUT。\"\n\n- id: R41-D2\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 37\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 升级为 should-fix (R43-W3)。本轮共识。\"\n\n# ===== ROUND 42 RESOLVED =====\n- id: R42-NEW1\n  summary: \"Abstract 数值引用不一致：entity construction 句混入 LP selection 数字\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 42\n  resolution: \"Abstract 改用百分比范围，LP 数值全文统一。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R42-NEW2\n  summary: \"§7.5 entity construction 3-epoch 数字不一致\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 42\n  resolution: \"Seed/metric 标签已加。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R42-Q3\n  summary: \"ESJ AUROC range §4 vs §5 不一致\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 42\n  resolution: \"确认不存在不一致。\"\n  resolution_round: 42\n\n# ===== EARLIER RESOLVED (简略) =====\n- id: R39-W1\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"R40 确认合规。\"\n  resolution_round: 40\n\n- id: R40-N5\n  summary: \"标题 overpromise\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 41\n  resolution: \"标题已改为 'the Correlation-Selection Gap'。\"\n  resolution_round: 41\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== ROUND 43 MUST-FIX (CONSENSUS) =====\n- id: R43-N1\n  summary: \"2-3 seeds 统计推断力不足，核心 negative claims 无法区分真无效应和检测力不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 40\n  last_seen_round: 43\n  mentions:\n    - round: 41\n      reviewers: [1, 2]\n      note: \"R41-W2, response-letter-only item\"\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未修改，仍为遗留问题\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1 升级为 Must-Fix。Table 42 bootstrap CI [-0.41, +2.54] 跨越零点。R2 AGREE 并补充：signal ranking 稳定性 ≠ 效应量显著性。两位共识：核心 negative claim 需改为 'we find no evidence within our statistical power'。\"\n\n- id: R43-N2\n  summary: \"Degeneracy decomposition bound 过松（恢复 3-12% oracle gap），作为主要贡献名不副实\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 38\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过——§6.3 重定位为 necessary condition test\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1 认为即使重定位后，§1 仍将其列为四大贡献之一，与 §6.3 的 intentionally loose 声明不一致。R2 AGREE：§1 暗示有力理论工具，§6.3 承认存在性结论，framing 不一致。\"\n\n- id: R43-N3\n  summary: \"观察性设计下因果措辞系统性过强\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1 提出：§1 'jointly determine', §4 'eliminates the variation', §6.2 'inverse scaling', §8 'localizing failure'。R2 strongly AGREE 并补充：§4 标题 'Where Single-Signal Selection Fails' 暗示因果；Figure 1 免责仅出现在 caption 中。Few-NERD 3v5 epoch 是混淆变量直接证据。\"\n\n- id: R43-N4\n  summary: \"处方性结果全局 Holm 校正不显著（p_adj=0.055），per-family 校正未预注册\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过——§7.5 提供 family 划分先验理由，双 p 值透明报告\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix：全局校正不显著削弱 prescriptive claim 可靠性。R1 AGREE：与 seeds 不足问题叠加。Abstract 中 per-family 值先于 global 值，读者优先注意更显著值。两位共识：prescriptive claim 需降级为 exploratory 或增加统计 power。\"\n\n# ===== ROUND 43 MUST-FIX (DIVERGENT) =====\n- id: R43-N5\n  summary: \"标题 'Why SC Fails for NER' 与正文 conditional success 结论不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 40\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [2]\n      note: \"R41-D1 持续分歧\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix：标题绝对性与 §7.5 conditional gains、§5.1 cross-model positive results、§8 conditional recommendation 不一致。R1 REBUT：标题描述默认配置主导现象，ACL 标准范式，建议降为 should-fix。分歧记录。\"\n\n- id: R43-N6\n  summary: \"Table 1 novelty comparison 维度选择有 cherry-picking 嫌疑\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix：Failure decomp. 和 Diagnostics 重叠计分；Prescriptive 标 Conditional 但全局不显著；缺少对竞争工作有利的维度。R1 REBUT：两维度是不同层次（分析 vs 实践），竞争工作无形式化理论，建议降为 should-fix。Director 判定：降为 warning。\"\n\n# ===== ROUND 43 SHOULD-FIX (CONSENSUS) =====\n- id: R43-W1\n  summary: \"Few-NERD 3-epoch vs 5-epoch 混淆未充分解决，无法分离 degeneracy 和 alignment 效应\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 38\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过——Abstract 条件限定充分\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix：无法分离效应。R2 AGREE 并补充：undertrained model 的 lower greedy baseline 可能放大 construction gains，实践者通常部署 fully converged model。\"\n\n- id: R43-W2\n  summary: \"RE/SQL 扩展过于初步，Abstract 中 cross-task exploration 措辞 oversell\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证 Abstract 'preliminary' 措辞充分\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1-W5 和 R2-W2 独立提出。RE (n=397, 单数据集) 和 SQL (n=196) 规模不足以支撑跨任务泛化。两位共识：应进一步缩减 Abstract/Intro 中的提及。\"\n\n- id: R43-W3\n  summary: \"正文数字密度过高，Abstract ~15 个数值影响可读性\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未变化，持续 divergence (R41-D2)\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 AGREE。Abstract ~15 数字过多，§7 每句 2-3 个数字。建议 Abstract 保留 4-5 个关键数字。本轮共识升级为 should-fix。\"\n\n- id: R43-W4\n  summary: \"Entity construction 与 MBR 理论联系偏弱，entity independence 假设在 degenerate regime 下可能失效\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1-W3 提出。R2 部分 AGREE：MBR 联系主要是 motivational framing 而非严格理论基础，prescriptive results 是实证性的不依赖 MBR 完备性。问题在 framing 过度。\"\n\n- id: R43-W5\n  summary: \"模型多样性有限（仅 Qwen + LLaMA），frontier model degeneracy profile 差异大\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R1-W4 提出。R2 部分 AGREE：Limitations 提到 frontier degeneracy 5.5-74%，如果 GPT-5.5 degeneracy 低至 5.5%，论文基于 12-68% 开源模型的结论普适性存疑。\"\n\n- id: R43-W6\n  summary: \"'Primarily diagnostic with limited predictive power' 定位削弱论文实用价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2-W3 提出：框架无法事前预测，诊断边际价值有限。R1 REBUT：pilot N=8 diagnostic 有实用场景，但同意 §7.5 应扩展为明确 practitioner workflow。分歧记录。\"\n\n- id: R43-W7\n  summary: \"Entity-level decomposition 增量贡献需更强论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 41\n  last_seen_round: 43\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 未修改（response-letter-only item）\"\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 未独立提出但 R2 在新颖性评估中提及 instance-level granularity 和 NER-specific failure mechanisms 作为增量贡献。维持 open。\"\n\n- id: R43-W8\n  summary: \"相关工作可能遗漏：Reflexion (self-verification), Malinin & Gales (2021), 传统 NER ensemble\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 部分 AGREE：Malinin & Gales (2021) 和 Reflexion 应讨论。R1 认为 CRF ensemble 和 DeepSeek-R1 关联较弱非重要遗漏。\"\n\n# ===== ROUND 43 MINOR =====\n- id: R43-M1\n  summary: \"Footnote 1 (RE F1 confound) 建议提升到正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M1：RE F1 被 entity span errors confound 的说明重要，不应仅在脚注。\"\n\n- id: R43-M2\n  summary: \"Mechanistic evidence 在 Appendix 却作为正文贡献点列出\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M2：§1 四阶段路线图第 4 点在 Appendix 中。\"\n\n- id: R43-M3\n  summary: \"§3 应在首段明确提及 diagnostic sequence 而非 causal chain\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M3：Figure 1 caption 免责容易被忽略，§3 首段也应说明。与 R43-N3 因果措辞问题相关。\"\n\n- id: R43-M4\n  summary: \"§6.3 符号 D, G_nd, α 首次引入时定义不够直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M4：需要反复回看 §3 才能理解。\"\n\n# ===== EARLIER RESOLVED (保留历史) =====\n- id: R41-N1\n  summary: \"分解 bound 仅恢复 3-12% 实际增益，核心形式化贡献实用价值不足\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§6.3 已重定位为 intentionally loose necessary condition test。\"\n  resolution: \"§6.3 成功重定位。R42 验证通过。R43 以新角度重提（R43-N2）。\"\n  resolution_round: 42\n\n- id: R41-N2\n  summary: \"核心正面 claim 统计显著性取决于多重比较校正方案选择\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 42\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R42 验证通过。§7.5 提供 family 划分先验理由，双 p 值透明报告。\"\n  resolution: \"§7.5 修改验证通过。R43 以新角度重提（R43-N4）。\"\n  resolution_round: 42\n\n- id: R41-N3\n  summary: \"Mechanistic probes 使用 Qwen2.5-7B 而非主实验 Qwen3-8B\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 42\n  resolution: \"模型差异已标注，ESJ Qwen3-8B 确认 chance-level。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-N4\n  summary: \"Novelty 与 Landesberg et al. (2026) 概念重叠，differentiation 不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 42\n  resolution: \"§2 扩展为 4 维度系统对比。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-N5\n  summary: \"Few-NERD epoch confound 严重削弱最显著正面结果\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 42\n  resolution: \"Abstract 条件限定充分。R42 验证通过。R43 以混淆分离角度重提（R43-W1）。\"\n  resolution_round: 42\n\n- id: R41-W1\n  summary: \"Diagnostic vs prescriptive 叙事定位不一致\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  resolution: \"定位统一。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-W2\n  summary: \"2-3 seeds 统计推断力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 40\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 升级为 Must-Fix (R43-N1)。\"\n\n- id: R41-W3\n  summary: \"RE/SQL 扩展过薄\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 42\n  resolution: \"Abstract 已标注 preliminary。R43 以新角度重提（R43-W2）。\"\n  resolution_round: 42\n\n- id: R41-W4\n  summary: \"Related Work 覆盖面不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 41\n  last_seen_round: 42\n  resolution: \"引用全部添加。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-W5\n  summary: \"Entity-level decomposition 增量贡献需更强论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 41\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 维持 open (R43-W7)。\"\n\n- id: R41-W6\n  summary: \"Constrained decoding 对 LP 的 confound 未充分解耦\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 42\n  resolution: \"Free-form ablation 在 3 数据集上一致。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R41-D1\n  summary: \"标题 'Why SC Fails for NER' 与内容匹配度\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 40\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 升级为 R43-N5。R2 Must-Fix, R1 REBUT。\"\n\n- id: R41-D2\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 37\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43 升级为 should-fix (R43-W3)。本轮共识。\"\n\n# ===== ROUND 42 RESOLVED =====\n- id: R42-NEW1\n  summary: \"Abstract 数值引用不一致：entity construction 句混入 LP selection 数字\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 42\n  resolution: \"Abstract 改用百分比范围，LP 数值全文统一。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R42-NEW2\n  summary: \"§7.5 entity construction 3-epoch 数字不一致\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 42\n  resolution: \"Seed/metric 标签已加。R42 验证通过。\"\n  resolution_round: 42\n\n- id: R42-Q3\n  summary: \"ESJ AUROC range §4 vs §5 不一致\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 42\n  resolution: \"确认不存在不一致。\"\n  resolution_round: 42\n\n# ===== EARLIER RESOLVED (简略) =====\n- id: R39-W1\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: \"R40 确认合规。\"\n  resolution_round: 40\n\n- id: R40-N5\n  summary: \"标题 overpromise\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 41\n  resolution: \"标题已改为 'the Correlation-Selection Gap'。\"\n  resolution_round: 41\n"
  }
}
```

</details>

---


### Tool result

_source line 4661 · 2026-05-23T08:49:14.103123+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 12089}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4662 · 2026-05-23T08:51:15.860227+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311",
  "report": "## Round 43 审稿报告\n\n**论文**: Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh（全新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验/统计; R2: 新颖性/相关工作/写作）\n**轮次**: 1 轮（交叉回应后达成共识，无需 Round 2）\n\n---\n\n### Summary\n\n论文研究 test-time compute scaling（self-consistency, best-of-N）在 NER 任务上的表现，核心发现是 \"correlation-selection gap\"：质量估计信号可预测输出质量（AUROC 达 0.82）但无法转化为 instance-level selection gains（≤1pp）。通过 degeneracy 和 signal alignment collapse 两个维度建立诊断框架，并在 entity-level construction 上报告了有条件的正向结果（+1.40pp on Few-NERD, 3-epoch）。实验覆盖 4 个 NER 数据集、2 个模型族、4B-72B scale range，附带 RE 和 SQL 初步探索。\n\n---\n\n### Strengths\n\n**S1. Correlation-selection gap 是真实且有价值的发现。** 质量估计信号与输出质量的高相关性（ρ 达 0.45, AUROC 0.82）为何无法转化为选择增益（≤1pp），这一现象此前未被系统识别。对 NER 实践者有直接价值——避免在无效的重复采样上浪费推理预算。[R1-S1, R2-S1 共识]\n\n**S2. 实证覆盖面和系统性极高。** 4 个 NER 数据集 + RE + SQL，5 个信号族，2 个模型族 + 3 个 scale + GPT-5.5 frontier，57 项统计检验，46 页 appendix 包含 robustness checks、calibration 分析、mechanistic probes。[R1-S2, R2-S2 共识]\n\n**S3. 统计报告透明。** 同时报告 global Holm (k=57) 和 per-family Holm (k=10)，明确 p_adj=0.055 的边界情况，附 post-hoc power analysis、bootstrap CI、permutation tests。[R1-S3, R2-S4 共识]\n\n**S4. 与 concurrent work 的坦诚对比。** Table 1 和 §2 对 Landesberg et al. (2026) 的定位诚实，承认 concurrent discovery validates the gap as cross-domain。[R2-S3]\n\n**S5. Degeneracy 概念框架清晰。** 将 gap 分解为结构性层（信号赋予所有候选相同分数）和诊断性层（LP 压缩），概念清晰。[R1-S4]\n\n---\n\n### Weaknesses\n\n#### Must-Fix（两位 Reviewer 共识）\n\n**[MUST-FIX] W1. 2-3 seeds 统计推断力严重不足 [R43-N1]**\n核心 negative claim（\"selection yields <1pp\"）依赖 2-3 seeds，但 bootstrap CI 跨越零点（LP Δ 95% CI [-0.41, +2.54]）。无法区分\"真无效应\"和\"检测力不足\"。§7.4 报告的 signal ranking 稳定性（ordinal）不等同于效应量显著性（cardinal）。\n- R1 Must-Fix, R2 AGREE\n- 建议：negative claims 改为 \"we find no evidence of selection gains within our statistical power\"；正文附 CI；报告 MDE（最小可检测效应量）\n\n**[MUST-FIX] W2. Degeneracy decomposition bound 过松，贡献定位不一致 [R43-N2]**\nBound 仅恢复 3-12% oracle gap（Figure bound），§6.3 自述 \"intentionally loose necessary condition\"，但 §1 将其列为四大贡献之一（Explore [§5, §6]），framing 不一致。Bound 更接近存在性定理而非精确诊断工具。\n- R1 Must-Fix, R2 AGREE\n- 建议：§1 将 bound 降级为 existence result；正文报告恢复率；降低论述调性\n\n**[MUST-FIX] W3. 观察性设计下因果措辞系统性过强 [R43-N3]**\n论文自述 observational (§3)，但多处使用因果语言：§1 \"jointly determine\"、§4 \"eliminates the variation\"、§4 标题 \"Where Single-Signal Selection Fails\"（暗示因果）、§6.2 \"inverse scaling\"、§8 \"localizing failure\"。Figure 1 的 \"(diagnostic sequence, not causal chain)\" 免责仅在 caption 中。Few-NERD 3v5 epoch 同时改变 degeneracy 和 alignment——混淆变量的直接证据。\n- R1 Must-Fix, R2 strongly AGREE\n- 建议：系统性替换因果措辞为关联性描述；§3 首段增加 observational design 声明；增加混淆变量讨论\n\n**[MUST-FIX] W4. 处方性结果统计基础不足 [R43-N4]**\nEntity-level construction 的全局 Holm p_adj=0.055 不显著；per-family p_adj=0.006 依赖未预注册的 family 划分。Abstract 中 per-family 值先于 global 值，引导读者优先注意更显著值。Prescriptive claim 是论文区别于 \"pure negative results\" 的关键差异点——如果站不住，novelty 进一步下降。\n- R2 Must-Fix, R1 AGREE\n- 建议：prescriptive 结果降级为 exploratory observation；或增加额外实验增强 power\n\n#### Should-Fix（影响评分）\n\n**[SHOULD-FIX] W5. 标题-内容不匹配 [R43-N5]**\n\"Why Self-Consistency Fails for NER\" 与 §7.5 conditional gains (+1.40pp)、§5.1 cross-model positive results、§8 conditional recommendation 不一致。\n- R2 Must-Fix, R1 REBUT（标题描述默认配置主导现象，ACL 标准范式）\n- Director 判定：降为 Should-Fix，但强烈建议修改为条件性表述\n\n**[SHOULD-FIX] W6. Table 1 novelty comparison 维度偏向本文 [R43-N6]**\nFailure decomp. 和 Diagnostics 重叠计分；Prescriptive 标 \"Conditional\" 但全局不显著；缺少对竞争工作有利维度。\n- R2 Must-Fix, R1 REBUT（两维度是不同层次）\n- Director 判定：降为 Should-Fix，建议合并重叠维度并标注 p 值\n\n**[SHOULD-FIX] W7. Few-NERD epoch 混淆无法分离 [R43-W1]**\n3-epoch undertrained model 不仅 degeneracy 低，还可能有更弱的 greedy baseline。实践者部署 fully converged model，prescriptive recommendation 的泛化性存疑。\n- R1 Should-Fix, R2 AGREE\n\n**[SHOULD-FIX] W8. RE/SQL 扩展过于初步 [R43-W2]**\nRE (n=397, 单数据集) 和 SQL (n=196) 规模不足以支撑 \"cross-task exploration\" 宣传。\n- R1-W5, R2-W2 独立提出\n\n**[SHOULD-FIX] W9. 数字密度过高 [R43-W3]**\nAbstract ~15 个数值，§7 每句 2-3 个数字，影响可读性。\n- R2-W1, R1 AGREE\n- 建议：Abstract 保留 4-5 个关键数字\n\n**[SHOULD-FIX] W10. 模型多样性有限 [R43-W5]**\n仅 Qwen + LLaMA 两个开源家族。Frontier model degeneracy profile 差异大（5.5-74%），论文基于 12-68% 开源模型的结论普适性存疑。\n- R1-W4, R2 AGREE\n\n**[SHOULD-FIX] W11. \"Primarily diagnostic\" 定位削弱实用价值 [R43-W6]**\n框架无法事前预测哪些实例受益于 scaling。Pilot N=8 diagnostic 有实用场景但 §7.5 未展开为 practitioner workflow。\n- R2-W3, R1 部分 REBUT\n\n**[SHOULD-FIX] W12. 相关工作可能遗漏 [R43-W8]**\nMalinin & Gales (2021) 关于自回归结构化预测不确定性估计、Reflexion (self-verification for structured outputs) 应讨论。\n- R2-W4, R1 部分 AGREE\n\n---\n\n### Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全达成共识：\n\n1. **Seeds 不足是论文最大统计瓶颈** — 核心 negative claims 和 positive claims 的 CI 均过宽\n2. **Bound 过松与贡献定位不一致** — §1 的宣传与 §6.3 的实际效果脱节\n3. **因果措辞需系统性降级** — 全文需替换为关联性描述\n4. **Per-family Holm 未预注册** — prescriptive claim 的统计基础不牢\n5. **RE/SQL 过于初步** — 与 cross-task 宣传不匹配\n6. **数字密度过高** — Abstract 和 §7 需精简\n7. **核心判断：论文的分析质量高于其 claim 的可靠性** — 框架设计合理、实验覆盖广，但统计推断力不足以支撑正文中的 claim 强度\n\n---\n\n### Reviewer Divergence [REBUT]\n\n1. **标题是否需要修改** — R2 Must-Fix（过度简化），R1 REBUT（ACL 标准范式，降为 should-fix）。Director 判定：降为 Should-Fix，建议添加条件性修饰。\n2. **Table 1 维度是否 cherry-picking** — R2 Must-Fix，R1 REBUT（两维度是不同层次）。Director 判定：降为 Should-Fix。\n3. **新颖性判断** — R1 认为 correlation-selection gap 是 genuinely surprising（AUROC 0.82 却 ≤1pp 选择增益，直觉无法预见）；R2 认为 SC 在结构化输出上效果差是可预期的直觉，论文的贡献在于量化而非发现。Director 判定：发现本身有价值，但 \"量化已知方向的现象\" 的 excitement 确实低于 \"反直觉发现\"。\n\n---\n\n### Questions\n\nQ1: Bound 的 3-12% 恢复率是否已是该分析框架下的阶最优？如果不是，为何不追求更紧 bound？\n\nQ2: Free-form decoding 一致性反转 RE LP selection——correlation-selection gap 是否 decoding-strategy-dependent？结论适用范围需怎样限定？\n\nQ3: Entity construction θ 依赖 held-out data 选择（0.15-0.35 跨数据集），这是否削弱了 pre-deployment diagnostic 的实用性？\n\nQ4: 69% inverse scaling 的 N-transitions 中，高/低 degeneracy 子群的比例是否显著不同？如果是，这支持诊断框架；如果否，框架预测价值存疑。\n\n---\n\n### Missing References\n\n1. **Malinin & Gales (2021)** — \"Uncertainty Estimation in Autoregressive Structured Prediction\"：直接相关于自回归结构化预测的不确定性估计\n2. **Shinn et al. (2023, Reflexion)** — 迭代自我验证方法在结构化任务上的应用\n3. 传统 NER ensemble 方法（CRF ensemble, BiLSTM-CRF bagging）与 LLM self-consistency 面临类似挑战的历史联系（R1 认为关联较弱）\n\n---\n\n### External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿，跳过。\n\n---\n\n### Visual Layout Check（非评分项）\n\n视觉审查 Agent 超时（300s timeout）。未产生有效 findings。用户可手动重新触发。\n\n---\n\n### Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Overall | 3.5 | 3.0 | 3.0 |\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**判定理由**：\n\n论文揭示了一个真实且有价值的现象（correlation-selection gap），实证覆盖面和统计透明度值得肯定。但四个共识性 Must-Fix 问题限制了论文的可靠性：\n\n1. **统计推断力不足**（seeds 太少）使核心 claims——无论 negative 还是 positive——的 CI 过宽\n2. **Bound 过松**与贡献定位不一致，理论贡献被高估\n3. **因果措辞过强**与自述 observational 设计矛盾\n4. **Prescriptive claim 统计基础不牢**——论文区别于 \"pure negative results\" 的关键差异点站不住\n\n核心判断：**论文的分析质量高于其 claim 的可靠性**。如果将 claims 系统性降级（因果措辞→关联性、bound→existence result、prescriptive→exploratory），论文作为 Findings 级别的实证分析是合格的。修改 W1-W4 后有望达到 3.5（Borderline Conference），但当前状态更适合 Findings。\n\n---\n\n### Detailed Comments\n\n**§1 Introduction**: 四阶段路线图的 \"Explore\" 将 bound 列为主要贡献，与 §6.3 的 \"intentionally loose\" 不一致。Mechanistic evidence 在 Appendix 中却列为贡献点。\n\n**§2 Related Work**: Table 1 的 7 维度应合并 \"Failure decomp.\" 和 \"Diagnostics\"，并在 \"Prescriptive\" 一栏标注 p_adj。缺少 Malinin & Gales (2021) 和 Reflexion 的讨论。\n\n**§3 Diagnostic Framework**: 首段应增加 observational design 声明，明确后续分析为关联性而非因果性。\n\n**§4 Single-Signal Selection**: 标题 \"Where Single-Signal Selection Fails\" 暗示因果，建议改为 \"Single-Signal Selection Results\" 或类似中性表述。\n\n**§6.3 Degeneracy Decomposition**: 正文应报告 3-12% 恢复率（当前仅 Appendix），将 bound 降级为 existence result / screening test。\n\n**§7.5 Prescriptive Results**: Abstract 中 per-family p_adj 应后置于 global p_adj。正文应明确声明全局校正下不显著并讨论含义。3-epoch condition 需增加 greedy baseline 控制讨论。\n\n**Abstract**: ~15 个数值过多，建议保留 4-5 个关键数字。RE/SQL 提及应进一步缩减。\n\n**Limitations**: 当前内容充分。可增加 \"decoding-strategy-dependent\" 的讨论。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311",
    "report": "## Round 43 审稿报告\n\n**论文**: Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh（全新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验/统计; R2: 新颖性/相关工作/写作）\n**轮次**: 1 轮（交叉回应后达成共识，无需 Round 2）\n\n---\n\n### Summary\n\n论文研究 test-time compute scaling（self-consistency, best-of-N）在 NER 任务上的表现，核心发现是 \"correlation-selection gap\"：质量估计信号可预测输出质量（AUROC 达 0.82）但无法转化为 instance-level selection gains（≤1pp）。通过 degeneracy 和 signal alignment collapse 两个维度建立诊断框架，并在 entity-level construction 上报告了有条件的正向结果（+1.40pp on Few-NERD, 3-epoch）。实验覆盖 4 个 NER 数据集、2 个模型族、4B-72B scale range，附带 RE 和 SQL 初步探索。\n\n---\n\n### Strengths\n\n**S1. Correlation-selection gap 是真实且有价值的发现。** 质量估计信号与输出质量的高相关性（ρ 达 0.45, AUROC 0.82）为何无法转化为选择增益（≤1pp），这一现象此前未被系统识别。对 NER 实践者有直接价值——避免在无效的重复采样上浪费推理预算。[R1-S1, R2-S1 共识]\n\n**S2. 实证覆盖面和系统性极高。** 4 个 NER 数据集 + RE + SQL，5 个信号族，2 个模型族 + 3 个 scale + GPT-5.5 frontier，57 项统计检验，46 页 appendix 包含 robustness checks、calibration 分析、mechanistic probes。[R1-S2, R2-S2 共识]\n\n**S3. 统计报告透明。** 同时报告 global Holm (k=57) 和 per-family Holm (k=10)，明确 p_adj=0.055 的边界情况，附 post-hoc power analysis、bootstrap CI、permutation tests。[R1-S3, R2-S4 共识]\n\n**S4. 与 concurrent work 的坦诚对比。** Table 1 和 §2 对 Landesberg et al. (2026) 的定位诚实，承认 concurrent discovery validates the gap as cross-domain。[R2-S3]\n\n**S5. Degeneracy 概念框架清晰。** 将 gap 分解为结构性层（信号赋予所有候选相同分数）和诊断性层（LP 压缩），概念清晰。[R1-S4]\n\n---\n\n### Weaknesses\n\n#### Must-Fix（两位 Reviewer 共识）\n\n**[MUST-FIX] W1. 2-3 seeds 统计推断力严重不足 [R43-N1]**\n核心 negative claim（\"selection yields <1pp\"）依赖 2-3 seeds，但 bootstrap CI 跨越零点（LP Δ 95% CI [-0.41, +2.54]）。无法区分\"真无效应\"和\"检测力不足\"。§7.4 报告的 signal ranking 稳定性（ordinal）不等同于效应量显著性（cardinal）。\n- R1 Must-Fix, R2 AGREE\n- 建议：negative claims 改为 \"we find no evidence of selection gains within our statistical power\"；正文附 CI；报告 MDE（最小可检测效应量）\n\n**[MUST-FIX] W2. Degeneracy decomposition bound 过松，贡献定位不一致 [R43-N2]**\nBound 仅恢复 3-12% oracle gap（Figure bound），§6.3 自述 \"intentionally loose necessary condition\"，但 §1 将其列为四大贡献之一（Explore [§5, §6]），framing 不一致。Bound 更接近存在性定理而非精确诊断工具。\n- R1 Must-Fix, R2 AGREE\n- 建议：§1 将 bound 降级为 existence result；正文报告恢复率；降低论述调性\n\n**[MUST-FIX] W3. 观察性设计下因果措辞系统性过强 [R43-N3]**\n论文自述 observational (§3)，但多处使用因果语言：§1 \"jointly determine\"、§4 \"eliminates the variation\"、§4 标题 \"Where Single-Signal Selection Fails\"（暗示因果）、§6.2 \"inverse scaling\"、§8 \"localizing failure\"。Figure 1 的 \"(diagnostic sequence, not causal chain)\" 免责仅在 caption 中。Few-NERD 3v5 epoch 同时改变 degeneracy 和 alignment——混淆变量的直接证据。\n- R1 Must-Fix, R2 strongly AGREE\n- 建议：系统性替换因果措辞为关联性描述；§3 首段增加 observational design 声明；增加混淆变量讨论\n\n**[MUST-FIX] W4. 处方性结果统计基础不足 [R43-N4]**\nEntity-level construction 的全局 Holm p_adj=0.055 不显著；per-family p_adj=0.006 依赖未预注册的 family 划分。Abstract 中 per-family 值先于 global 值，引导读者优先注意更显著值。Prescriptive claim 是论文区别于 \"pure negative results\" 的关键差异点——如果站不住，novelty 进一步下降。\n- R2 Must-Fix, R1 AGREE\n- 建议：prescriptive 结果降级为 exploratory observation；或增加额外实验增强 power\n\n#### Should-Fix（影响评分）\n\n**[SHOULD-FIX] W5. 标题-内容不匹配 [R43-N5]**\n\"Why Self-Consistency Fails for NER\" 与 §7.5 conditional gains (+1.40pp)、§5.1 cross-model positive results、§8 conditional recommendation 不一致。\n- R2 Must-Fix, R1 REBUT（标题描述默认配置主导现象，ACL 标准范式）\n- Director 判定：降为 Should-Fix，但强烈建议修改为条件性表述\n\n**[SHOULD-FIX] W6. Table 1 novelty comparison 维度偏向本文 [R43-N6]**\nFailure decomp. 和 Diagnostics 重叠计分；Prescriptive 标 \"Conditional\" 但全局不显著；缺少对竞争工作有利维度。\n- R2 Must-Fix, R1 REBUT（两维度是不同层次）\n- Director 判定：降为 Should-Fix，建议合并重叠维度并标注 p 值\n\n**[SHOULD-FIX] W7. Few-NERD epoch 混淆无法分离 [R43-W1]**\n3-epoch undertrained model 不仅 degeneracy 低，还可能有更弱的 greedy baseline。实践者部署 fully converged model，prescriptive recommendation 的泛化性存疑。\n- R1 Should-Fix, R2 AGREE\n\n**[SHOULD-FIX] W8. RE/SQL 扩展过于初步 [R43-W2]**\nRE (n=397, 单数据集) 和 SQL (n=196) 规模不足以支撑 \"cross-task exploration\" 宣传。\n- R1-W5, R2-W2 独立提出\n\n**[SHOULD-FIX] W9. 数字密度过高 [R43-W3]**\nAbstract ~15 个数值，§7 每句 2-3 个数字，影响可读性。\n- R2-W1, R1 AGREE\n- 建议：Abstract 保留 4-5 个关键数字\n\n**[SHOULD-FIX] W10. 模型多样性有限 [R43-W5]**\n仅 Qwen + LLaMA 两个开源家族。Frontier model degeneracy profile 差异大（5.5-74%），论文基于 12-68% 开源模型的结论普适性存疑。\n- R1-W4, R2 AGREE\n\n**[SHOULD-FIX] W11. \"Primarily diagnostic\" 定位削弱实用价值 [R43-W6]**\n框架无法事前预测哪些实例受益于 scaling。Pilot N=8 diagnostic 有实用场景但 §7.5 未展开为 practitioner workflow。\n- R2-W3, R1 部分 REBUT\n\n**[SHOULD-FIX] W12. 相关工作可能遗漏 [R43-W8]**\nMalinin & Gales (2021) 关于自回归结构化预测不确定性估计、Reflexion (self-verification for structured outputs) 应讨论。\n- R2-W4, R1 部分 AGREE\n\n---\n\n### Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全达成共识：\n\n1. **Seeds 不足是论文最大统计瓶颈** — 核心 negative claims 和 positive claims 的 CI 均过宽\n2. **Bound 过松与贡献定位不一致** — §1 的宣传与 §6.3 的实际效果脱节\n3. **因果措辞需系统性降级** — 全文需替换为关联性描述\n4. **Per-family Holm 未预注册** — prescriptive claim 的统计基础不牢\n5. **RE/SQL 过于初步** — 与 cross-task 宣传不匹配\n6. **数字密度过高** — Abstract 和 §7 需精简\n7. **核心判断：论文的分析质量高于其 claim 的可靠性** — 框架设计合理、实验覆盖广，但统计推断力不足以支撑正文中的 claim 强度\n\n---\n\n### Reviewer Divergence [REBUT]\n\n1. **标题是否需要修改** — R2 Must-Fix（过度简化），R1 REBUT（ACL 标准范式，降为 should-fix）。Director 判定：降为 Should-Fix，建议添加条件性修饰。\n2. **Table 1 维度是否 cherry-picking** — R2 Must-Fix，R1 REBUT（两维度是不同层次）。Director 判定：降为 Should-Fix。\n3. **新颖性判断** — R1 认为 correlation-selection gap 是 genuinely surprising（AUROC 0.82 却 ≤1pp 选择增益，直觉无法预见）；R2 认为 SC 在结构化输出上效果差是可预期的直觉，论文的贡献在于量化而非发现。Director 判定：发现本身有价值，但 \"量化已知方向的现象\" 的 excitement 确实低于 \"反直觉发现\"。\n\n---\n\n### Questions\n\nQ1: Bound 的 3-12% 恢复率是否已是该分析框架下的阶最优？如果不是，为何不追求更紧 bound？\n\nQ2: Free-form decoding 一致性反转 RE LP selection——correlation-selection gap 是否 decoding-strategy-dependent？结论适用范围需怎样限定？\n\nQ3: Entity construction θ 依赖 held-out data 选择（0.15-0.35 跨数据集），这是否削弱了 pre-deployment diagnostic 的实用性？\n\nQ4: 69% inverse scaling 的 N-transitions 中，高/低 degeneracy 子群的比例是否显著不同？如果是，这支持诊断框架；如果否，框架预测价值存疑。\n\n---\n\n### Missing References\n\n1. **Malinin & Gales (2021)** — \"Uncertainty Estimation in Autoregressive Structured Prediction\"：直接相关于自回归结构化预测的不确定性估计\n2. **Shinn et al. (2023, Reflexion)** — 迭代自我验证方法在结构化任务上的应用\n3. 传统 NER ensemble 方法（CRF ensemble, BiLSTM-CRF bagging）与 LLM self-consistency 面临类似挑战的历史联系（R1 认为关联较弱）\n\n---\n\n### External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿，跳过。\n\n---\n\n### Visual Layout Check（非评分项）\n\n视觉审查 Agent 超时（300s timeout）。未产生有效 findings。用户可手动重新触发。\n\n---\n\n### Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Overall | 3.5 | 3.0 | 3.0 |\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**判定理由**：\n\n论文揭示了一个真实且有价值的现象（correlation-selection gap），实证覆盖面和统计透明度值得肯定。但四个共识性 Must-Fix 问题限制了论文的可靠性：\n\n1. **统计推断力不足**（seeds 太少）使核心 claims——无论 negative 还是 positive——的 CI 过宽\n2. **Bound 过松**与贡献定位不一致，理论贡献被高估\n3. **因果措辞过强**与自述 observational 设计矛盾\n4. **Prescriptive claim 统计基础不牢**——论文区别于 \"pure negative results\" 的关键差异点站不住\n\n核心判断：**论文的分析质量高于其 claim 的可靠性**。如果将 claims 系统性降级（因果措辞→关联性、bound→existence result、prescriptive→exploratory），论文作为 Findings 级别的实证分析是合格的。修改 W1-W4 后有望达到 3.5（Borderline Conference），但当前状态更适合 Findings。\n\n---\n\n### Detailed Comments\n\n**§1 Introduction**: 四阶段路线图的 \"Explore\" 将 bound 列为主要贡献，与 §6.3 的 \"intentionally loose\" 不一致。Mechanistic evidence 在 Appendix 中却列为贡献点。\n\n**§2 Related Work**: Table 1 的 7 维度应合并 \"Failure decomp.\" 和 \"Diagnostics\"，并在 \"Prescriptive\" 一栏标注 p_adj。缺少 Malinin & Gales (2021) 和 Reflexion 的讨论。\n\n**§3 Diagnostic Framework**: 首段应增加 observational design 声明，明确后续分析为关联性而非因果性。\n\n**§4 Single-Signal Selection**: 标题 \"Where Single-Signal Selection Fails\" 暗示因果，建议改为 \"Single-Signal Selection Results\" 或类似中性表述。\n\n**§6.3 Degeneracy Decomposition**: 正文应报告 3-12% 恢复率（当前仅 Appendix），将 bound 降级为 existence result / screening test。\n\n**§7.5 Prescriptive Results**: Abstract 中 per-family p_adj 应后置于 global p_adj。正文应明确声明全局校正下不显著并讨论含义。3-epoch condition 需增加 greedy baseline 控制讨论。\n\n**Abstract**: ~15 个数值过多，建议保留 4-5 个关键数字。RE/SQL 提及应进一步缩减。\n\n**Limitations**: 当前内容充分。可增加 \"decoding-strategy-dependent\" 的讨论。"
  }
}
```

</details>

---


### Tool result

_source line 4663 · 2026-05-23T08:51:19.982088+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4121
}
```

</details>

---


### Assistant

_source line 4664 · 2026-05-23T08:51:28.571781+00:00_

Round 43 审稿完成。

**最终评分：3.0 (Findings)**

审稿报告已投递给 Research Director。核心结论：

- **4 个共识 Must-Fix**：seeds 不足（CI 跨零点）、bound 过松（贡献定位不一致）、因果措辞系统性过强、prescriptive claim 统计基础不牢
- **8 个 Should-Fix**：标题不匹配、Table 1 维度偏向、epoch 混淆、RE/SQL 初步、数字密度、模型多样性、诊断定位、相关工作遗漏
- **核心判断**：论文的分析质量高于其 claim 的可靠性。Claims 系统性降级后可作为 Findings 级别实证分析；修改 Must-Fix 后有望达到 3.5（Borderline Conference）

Issue Tracker 已同步更新至 `review_issues.yaml`。视觉审查超时，未产生有效 findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 357

## Round 357

2 recorded events


### User

_source line 4665 · 2026-05-23T08:51:31.215324+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：对 R1 的 3 个 Must-Fix 全部 **[AGREE]**（seeds 不足、bound 过松、因果措辞过强），5 个 Should-Fix 中 4 个 **[AGREE]**、1 个部分同意（W3 MBR 联系——严重性略低于 R1 评估）。两位 Reviewer 在 Holm 统计问题、RE/SQL 初步性、因果措辞三个方面独立达成一致。核心判断：分析质量高于 claim 可靠性，系统性降级 claims 后适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 4666 · 2026-05-23T08:51:40.759438+00:00_

Round 43 审稿已完成。

**最终结果**：Overall 3.0（Findings），两位 Reviewer 交叉回应后在所有关键方法论问题上达成共识。审稿报告和 Issue Tracker 已提交。

**核心判断**：论文的分析质量高于其 claim 的可靠性。4 个共识性 Must-Fix（seeds 不足、bound 过松、因果措辞、prescriptive 统计基础）+ 8 个 Should-Fix。系统性降级 claims 后适合 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 358

## Round 358

36 recorded events


### User

_source line 4667 · 2026-05-23T16:41:15.406997+00:00_

[Round 44 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/struct_self_consist_ie/artifacts/review_reports/round_43.md`
跨轮次问题追踪: `projects/struct_self_consist_ie/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ✅ 后台自动运行中，完成后你会收到 [引用验证结果] 消息，请在合成报告时纳入

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 4668 · 2026-05-23T16:41:28.193619+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4669 · 2026-05-23T16:41:28.244384+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4670 · 2026-05-23T16:41:31.326307+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 4671 · 2026-05-23T16:41:31.326769+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4672 · 2026-05-23T16:41:33.886529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_43.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_43.md"
  }
}
```

</details>

---


### Tool result

_source line 4673 · 2026-05-23T16:41:34.241246+00:00_

1	---
2	round: 43
3	review_mode: fresh
4	overall_score: 3.0 (Findings)
5	timestamp: 2026-05-23T08:51:15.857185+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	## Round 43 审稿报告
12	
13	**论文**: Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap
14	**Venue**: EMNLP 2026 (ARR May 2026 cycle)
15	**审稿模式**: Fresh（全新审稿）
16	**Reviewer 编排**: 2 人（R1: 方法严谨性/实验/统计; R2: 新颖性/相关工作/写作）
17	**轮次**: 1 轮（交叉回应后达成共识，无需 Round 2）
18	
19	---
20	
21	### Summary
22	
23	论文研究 test-time compute scaling（self-consistency, best-of-N）在 NER 任务上的表现，核心发现是 "correlation-selection gap"：质量估计信号可预测输出质量（AUROC 达 0.82）但无法转化为 instance-level selection gains（≤1pp）。通过 degeneracy 和 signal alignment collapse 两个维度建立诊断框架，并在 entity-level construction 上报告了有条件的正向结果（+1.40pp on Few-NERD, 3-epoch）。实验覆盖 4 个 NER 数据集、2 个模型族、4B-72B scale range，附带 RE 和 SQL 初步探索。
24	
25	---
26	
27	### Strengths
28	
29	**S1. Correlation-selection gap 是真实且有价值的发现。** 质量估计信号与输出质量的高相关性（ρ 达 0.45, AUROC 0.82）为何无法转化为选择增益（≤1pp），这一现象此前未被系统识别。对 NER 实践者有直接价值——避免在无效的重复采样上浪费推理预算。[R1-S1, R2-S1 共识]
30	
31	**S2. 实证覆盖面和系统性极高。** 4 个 NER 数据集 + RE + SQL，5 个信号族，2 个模型族 + 3 个 scale + GPT-5.5 frontier，57 项统计检验，46 页 appendix 包含 robustness checks、calibration 分析、mechanistic probes。[R1-S2, R2-S2 共识]
32	
33	**S3. 统计报告透明。** 同时报告 global Holm (k=57) 和 per-family Holm (k=10)，明确 p_adj=0.055 的边界情况，附 post-hoc power analysis、bootstrap CI、permutation tests。[R1-S3, R2-S4 共识]
34	
35	**S4. 与 concurrent work 的坦诚对比。** Table 1 和 §2 对 Landesberg et al. (2026) 的定位诚实，承认 concurrent discovery validates the gap as cross-domain。[R2-S3]
36	
37	**S5. Degeneracy 概念框架清晰。** 将 gap 分解为结构性层（信号赋予所有候选相同分数）和诊断性层（LP 压缩），概念清晰。[R1-S4]
38	
39	---
40	
41	### Weaknesses
42	
43	#### Must-Fix（两位 Reviewer 共识）
44	
45	**[MUST-FIX] W1. 2-3 seeds 统计推断力严重不足 [R43-N1]**
46	核心 negative claim（"selection yields <1pp"）依赖 2-3 seeds，但 bootstrap CI 跨越零点（LP Δ 95% CI [-0.41, +2.54]）。无法区分"真无效应"和"检测力不足"。§7.4 报告的 signal ranking 稳定性（ordin
…[truncated 6698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 4674 · 2026-05-23T16:41:34.241719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4675 · 2026-05-23T16:41:34.393065+00:00_

1	issues:
2	# ===== ROUND 43 MUST-FIX (CONSENSUS) — ALL RESOLVED =====
3	- id: R43-N1
4	  summary: "2-3 seeds 统计推断力不足，核心 negative claims 无法区分真无效应和检测力不足"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 40
9	  last_seen_round: 43
10	  mentions:
11	    - round: 41
12	      reviewers: [1, 2]
13	      note: "R41-W2, response-letter-only item"
14	    - round: 42
15	      reviewers: [1, 2]
16	      note: "R42 未修改，仍为遗留问题"
17	    - round: 43
18	      reviewers: [1, 2]
19	      note: "R1 升级为 Must-Fix。R2 AGREE。核心 negative claim 需改为 power-aware。"
20	  action_items:
21	    - round: 43
22	      action: "Power-aware negative claims + MDE + CI language + Limitations power paragraph + 残余补修"
23	      assigned_to: paper_agent+director
24	      status: done
25	  resolution: "全文 negative claims 改为 'yields no detectable gains'，加 MDE ~1.5pp/CI 限定。Reviewer R43 补修验证 PASS。"
26	  resolution_round: 43
27	
28	- id: R43-N2
29	  summary: "Degeneracy decomposition bound 过松（恢复 3-12% oracle gap），作为主要贡献名不副实"
30	  category: method
31	  severity: critical
32	  status: resolved
33	  first_raised_round: 38
34	  last_seen_round: 43
35	  mentions:
36	    - round: 42
37	      reviewers: [1, 2]
38	      note: "R42 验证通过——§6.3 重定位为 necessary condition test"
39	    - round: 43
40	      reviewers: [1, 2]
41	      note: "§1 仍将 bound 列为四大贡献之一，与 §6.3 不一致。"
42	  action_items:
43	    - round: 43
44	      action: "四阶段→三阶段贡献结构，bound 降为 Diagnose 支撑"
45	      assigned_to: paper_agent
46	      status: done
47	  resolution: "三阶段重构 (Discover/Diagnose/Construct-exploratory)，bound 不再独立贡献。Reviewer 验证 PASS。"
48	  resolution_round: 43
49	
50	- id: R43-N3
51	  summary: "观察性设计下因果措辞系统性过强"
52	  category: writing
53	  severity: critical
54	  status: resolved
55	  first_raised_round: 43
56	  last_seen_round: 43
57	  mentions:
58	    - round: 43
59	      reviewers: [1, 2]
60	      note: "11+ 处因果措辞。§4 标题暗示因果。"
61	  action_items:
62	    - round: 43
63	      action: "11 处因果→关联替换 + observational
…[truncated 11871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 4676 · 2026-05-23T16:41:47.345014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 4677 · 2026-05-23T16:41:48.207669+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{When Self-Consistency Fails for NER:\\ Degeneracy, Signal Collapse, and the Correlation-Selection Gap}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/background}
38	\input{sections/diagnostic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	
44	\section*{Limitations}
45	\input{sections/limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\renewcommand{\thesection}{\alphalph{\value{section}}}
51	\input{sections/appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 862
}
```

</details>

---


### Tool call

_source line 4678 · 2026-05-23T16:41:48.208112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 4679 · 2026-05-23T16:41:48.763161+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary analysis, with preliminary cross-task pilots (RE, SQL).
4	Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields no detectable gains (${<}1$\,pp; CI crosses zero), revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that are jointly associated with scaling returns; cross-task exploration confirms task-specific failure modes.
6	Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\text{adj}}{=}0.055$, suggestive; per-family $p_{\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.
7	The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 4680 · 2026-05-23T16:41:48.763603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 4681 · 2026-05-23T16:41:49.016097+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \cite{yao2026consistency} and qualitative diversity collapse \cite{yun2025price} but no instance-level diagnostic framework.
5	
6	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection yields no detectable gains---MV ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also yields no gains, through within-instance compression (\S\ref{sec:selection_gap}).
8	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; Appendix~\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
9	A \textit{diagnostic framework} localizes the failure to two co-occurring conditions---degeneracy ($12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$; $\alpha$ here denotes LP-F1 alignment)---which co-occur with selection failure (Table~\ref{tab:method_summary}).
10	The framework decomposes observed failures post-hoc rather than predicting which instances will fail a priori; our analysis is observational and all reported associations are correlatio
…[truncated 3544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 4682 · 2026-05-23T16:41:49.066788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 4683 · 2026-05-23T16:41:49.118717+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time scaling and self-consistency.}\label{sec:yun_contrast}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with scaling laws \cite{snell2025scaling, brown2024monkeys, gao2023scaling} yield large gains on reasoning; recent extensions include reward-tail-guided search \cite{li2026rewardtail}. Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and trained verifiers \cite{cobbe2021verifiers, lightman2024verify, li2023stepaware} target discrete-answer settings.
5	SC can fail when consistent outputs are wrong \cite{chen2023twofailures}; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} variants face limits where sub-output agreement does not yield selection gain. Iterative self-verification \cite{shinn2023reflexion} offers an alternative, but our ESJ and MRSC results (\S\ref{sec:selection_gap}) show such approaches also fail for NER.
6	\citet{yun2025price} identify diversity collapse under constrained decoding; we extend their qualitative account with quantitative diagnostics (\S\ref{sec:selection_gap}).
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE ($\rho$ up to 0.47); we extend to instance-level analysis: (1)~task-level $\rho$ masks instance-level degeneracy; (2)~we decompose failure into degeneracy and LP compression; (3)~pre-deployment diagnostics that task-level correlation cannot provide.
10	Critically, their task-level granularity cannot distinguish instances where scaling helps from those where it harms---our entity-level decomposition addresses this gap (Table~\ref{tab:novelty_comparison}).
11	\citet{xie2023zeroshot} propose entity voting for zero-shot NER; \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
12	
13	\paragraph{Uncertainty estimation and MBR.}
14	Our selection instantiates MBR decoding \cite{eikema2022
…[truncated 2593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4684 · 2026-05-23T16:41:57.262473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 4685 · 2026-05-23T16:41:58.266489+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 4686 · 2026-05-23T16:41:58.417397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 4687 · 2026-05-23T16:41:58.468097+00:00_

1	\section{Single-Signal Selection Results}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), leaving insufficient variation for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 
…[truncated 3482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4688 · 2026-05-23T16:41:58.769558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 4689 · 2026-05-23T16:41:59.171380+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}), consistent with utility degradation on structured outputs \cite{eikema2025structured}.
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is mo
…[truncated 4308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 4690 · 2026-05-23T16:41:59.171735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 4691 · 2026-05-23T16:41:59.322626+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 53.7\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed
…[truncated 7697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 4692 · 2026-05-23T16:42:04.142204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 4693 · 2026-05-23T16:42:04.495172+00:00_

1	Our primary evidence is from English NER with fine-tuned 7--14B open-weight models; frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), and cross-task extensions (RE $n{=}397$, SQL $n{=}196$) are exploratory.
2	The framework is diagnostic, not causal: under global Holm--Bonferroni ($k{=}57$), the strongest construction claim reaches $p_{\text{adj}}{=}0.055$; our negative selection claims are bounded by statistical power (2--3 seeds, MDE ${\approx}1.5$\,pp).
3	Entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp), and we use a single prompt template per task.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 4694 · 2026-05-23T16:42:04.495655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 4695 · 2026-05-23T16:42:04.546901+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection yields no detectable gains (\S\ref{sec:selection_gap}), we present exploratory attempts informed by diagnostic findings to extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield a positive result, though on a single dataset.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\ref{sec:mechanistic} and adaptive methods in this section). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & App.~\ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & App.~\ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & App.~\ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally d
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4696 · 2026-05-23T16:43:16.400323+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4697 · 2026-05-23T16:43:42.414351+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26014
}
```

</details>

---


### Tool call

_source line 4698 · 2026-05-23T16:43:42.566716+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "Round 44 修订验证。你是 Reviewer 1，侧重**方法严谨性、实验设计、统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **格式**: Long paper, 正文 8 页, ACL style, double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_44/submitted.pdf`\n\n## 任务\n\n这是修订评估，不是初审。请逐条验证 Round 43 提出的问题是否已充分解决，并检查修改是否引入了新问题。\n\n### Round 43 Must-Fix（你负责的方向，需逐条标 [RESOLVED] 或 [STILL_OPEN]）\n\n**R43-N1** [你的 Must-Fix] 2-3 seeds 统计推断力不足\n- 要求：negative claims 改为 power-aware 表述，附 CI，报告 MDE\n- 验证点：Abstract \"no detectable gains (CI crosses zero)\"、§4 \"below MDE ≈1.5pp\"、§5 \"yields no detectable gains\"、Limitations \"bounded by statistical power (2-3 seeds, MDE ≈1.5pp)\"\n\n**R43-N2** [你的 Must-Fix] Degeneracy bound 过松，贡献定位不一致\n- 要求：§1 将 bound 降级为 existence result，正文报告恢复率\n- 验证点：§1 三阶段结构（bound 折入 Diagnose 而非独立贡献）、§6.3 正文报告 3-12% recovery ratio\n\n**R43-N3** [共识 Must-Fix] 因果措辞系统性过强\n- 要求：全文替换因果→关联，§3 首段 observational disclaimer\n- 验证点：§3 首句 \"Our analysis is observational\"；§1 \"co-occur with\" 替代 \"determine\"；§4 标题改为中性；检查是否有残留因果措辞\n\n**R43-N4** [共识 Must-Fix] 处方性结果统计不显著\n- 要求：prescriptive → exploratory，global p 先报告\n- 验证点：§7.5 标题 \"Entity Construction (Exploratory)\"；Abstract/§7.5 global p_adj=0.055 先于 per-family p_adj=0.006；\"family partition was not pre-registered\"\n\n### Round 43 Should-Fix（需逐条验证）\n\n**R43-W1** Few-NERD epoch 混淆 → 要求 greedy baseline 差异说明\n**R43-W4** MBR 理论联系偏弱 → 要求随 exploratory 定位弱化\n**R43-W5** 模型多样性有限 → Limitations 声明\n\n### 需特别关注的新变化\n\n1. **Ethics Statement 被移除**：Round 43 有 Ethics Statement，Round 44 的 main.tex 中已删除。ARR 鼓励但不强制 Ethics Statement——评估这是否有问题。\n2. **Discussion/Conclusion 合并入 §7.5**：不再有独立的 Discussion section，检查这是否影响论文完整性。\n3. **4-seed mean**：§7.5 entity construction 从 3-seed 改为 4-seed mean——验证是否改善了统计 power。\n4. **§6.2 新增行**：\"Inverse scaling concentrates in non-degenerate instances (11.1% vs. 1.3% for degenerate; OR=0.109)\"——这回应了 R43-Q4，验证是否充分。\n5. **Limitations 大幅缩短**（从 7 行到 3 行）——检查是否仍充分覆盖关键限制。\n\n### 输出格式\n\n对每个 R43 issue：[RESOLVED] 理由 / [STILL_OPEN] 理由\n然后：新发现的问题（如有），按 [MUST-FIX] / [SHOULD-FIX] / [MINOR] 分类。\n最后：更新后的 Overall 评分建议。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "Round 44 修订验证。你是 Reviewer 1，侧重**方法严谨性、实验设计、统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **格式**: Long paper, 正文 8 页, ACL style, double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_44/submitted.pdf`\n\n## 任务\n\n这是修订评估，不是初审。请逐条验证 Round 43 提出的问题是否已充分解决，并检查修改是否引入了新问题。\n\n### Round 43 Must-Fix（你负责的方向，需逐条标 [RESOLVED] 或 [STILL_OPEN]）\n\n**R43-N1** [你的 Must-Fix] 2-3 seeds 统计推断力不足\n- 要求：negative claims 改为 power-aware 表述，附 CI，报告 MDE\n- 验证点：Abstract \"no detectable gains (CI crosses zero)\"、§4 \"below MDE ≈1.5pp\"、§5 \"yields no detectable gains\"、Limitations \"bounded by statistical power (2-3 seeds, MDE ≈1.5pp)\"\n\n**R43-N2** [你的 Must-Fix] Degeneracy bound 过松，贡献定位不一致\n- 要求：§1 将 bound 降级为 existence result，正文报告恢复率\n- 验证点：§1 三阶段结构（bound 折入 Diagnose 而非独立贡献）、§6.3 正文报告 3-12% recovery ratio\n\n**R43-N3** [共识 Must-Fix] 因果措辞系统性过强\n- 要求：全文替换因果→关联，§3 首段 observational disclaimer\n- 验证点：§3 首句 \"Our analysis is observational\"；§1 \"co-occur with\" 替代 \"determine\"；§4 标题改为中性；检查是否有残留因果措辞\n\n**R43-N4** [共识 Must-Fix] 处方性结果统计不显著\n- 要求：prescriptive → exploratory，global p 先报告\n- 验证点：§7.5 标题 \"Entity Construction (Exploratory)\"；Abstract/§7.5 global p_adj=0.055 先于 per-family p_adj=0.006；\"family partition was not pre-registered\"\n\n### Round 43 Should-Fix（需逐条验证）\n\n**R43-W1** Few-NERD epoch 混淆 → 要求 greedy baseline 差异说明\n**R43-W4** MBR 理论联系偏弱 → 要求随 exploratory 定位弱化\n**R43-W5** 模型多样性有限 → Limitations 声明\n\n### 需特别关注的新变化\n\n1. **Ethics Statement 被移除**：Round 43 有 Ethics Statement，Round 44 的 main.tex 中已删除。ARR 鼓励但不强制 Ethics Statement——评估这是否有问题。\n2. **Discussion/Conclusion 合并入 §7.5**：不再有独立的 Discussion section，检查这是否影响论文完整性。\n3. **4-seed mean**：§7.5 entity construction 从 3-seed 改为 4-seed mean——验证是否改善了统计 power。\n4. **§6.2 新增行**：\"Inverse scaling concentrates in non-degenerate instances (11.1% vs. 1.3% for degenerate; OR=0.109)\"——这回应了 R43-Q4，验证是否充分。\n5. **Limitations 大幅缩短**（从 7 行到 3 行）——检查是否仍充分覆盖关键限制。\n\n### 输出格式\n\n对每个 R43 issue：[RESOLVED] 理由 / [STILL_OPEN] 理由\n然后：新发现的问题（如有），按 [MUST-FIX] / [SHOULD-FIX] / [MINOR] 分类。\n最后：更新后的 Overall 评分建议。"
  }
}
```

</details>

---


### Tool result

_source line 4699 · 2026-05-23T16:44:01.861462+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19294
}
```

</details>

---


### Tool call

_source line 4700 · 2026-05-23T16:44:02.015816+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "Round 44 修订验证。你是 Reviewer 2，侧重**新颖性、相关工作覆盖、写作完整性**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **格式**: Long paper, 正文 8 页, ACL style, double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_44/submitted.pdf`\n\n## 任务\n\n这是修订评估，不是初审。请逐条验证 Round 43 提出的问题是否已充分解决，并检查修改是否引入了新问题。\n\n### Round 43 Must-Fix（你负责的方向，需逐条标 [RESOLVED] 或 [STILL_OPEN]）\n\n**R43-N5** [你的 Must-Fix → Director 降为 Should-Fix] 标题不匹配\n- 要求：加入条件性修饰\n- 验证点：标题 \"When Self-Consistency Fails for NER\"（Why→When）\n\n**R43-N6** [你的 Must-Fix → Director 降为 Should-Fix] Table 1 cherry-picking\n- 要求：合并重叠维度，Prescriptive 标 p_adj\n- 验证点：Table 1 从 7 维度降为 6；Prescriptive 标 \"Conditional (p_adj=0.055)\"\n\n**R43-N4** [共识 Must-Fix] 处方性结果统计不显著\n- 验证点：§7.5 标题 \"Entity Construction (Exploratory)\"；p 值顺序 global first\n\n### Round 43 Should-Fix（需逐条验证）\n\n**R43-W2** RE/SQL 过于初步 → Abstract \"preliminary cross-task pilots (RE, SQL)\"\n**R43-W3** 数字密度过高 → Abstract 精简至 ~6 个数字\n**R43-W6** \"Primarily diagnostic\" 定位 → practitioner workflow\n**R43-W7** Entity-level decomposition 增量 → Table 1 + concurrent work 对比强化\n**R43-W8** 缺失引用 → §2 添加 Malinin & Gales (2021) + Reflexion\n\n### 残留 open minor 项\n\n**R43-M1** [open] Footnote 1 (RE F1 confound) 建议提升到正文——检查是否仍在脚注\n**R43-M3** [open] §3 应在首段提及 observational/diagnostic sequence——检查是否已加\n**R43-M4** [open] §6.3 符号定义不够直观——检查是否改善\n\n### 需特别关注的新变化\n\n1. **Ethics Statement 被移除**：Round 43 有，Round 44 没有。ARR 鼓励但不强制——评估影响。\n2. **Discussion/Conclusion 合并入 §7.5 最后一段**：不再有独立的 Discussion section。检查这是否影响论文结构完整性、是否符合 ACL 论文惯例。\n3. **Limitations 大幅缩短**（原 7 行 → 3 行）——EMNLP 2026 要求有 Limitations section 但不要求长度。检查覆盖面是否足够。\n4. **§2 concurrent work 段落**：仍列出 (d) prescriptive \"no constructive remedy vs. entity-level construction with MBR grounding\"——但 construction 现在已标为 exploratory 且 p_adj=0.055，这里的对比语气是否需要调整？\n5. **整体叙事一致性**：多处修改（标题、贡献结构、exploratory 定位、power-aware 语言）后，全文叙事是否连贯？\n\n### 输出格式\n\n对每个 R43 issue：[RESOLVED] 理由 / [STILL_OPEN] 理由\n然后：新发现的问题（如有），按 [MUST-FIX] / [SHOULD-FIX] / [MINOR] 分类。\n最后：更新后的 Overall 评分建议（Round 43 你给了 3.0 Findings）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "Round 44 修订验证。你是 Reviewer 2，侧重**新颖性、相关工作覆盖、写作完整性**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **格式**: Long paper, 正文 8 页, ACL style, double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_44/submitted.pdf`\n\n## 任务\n\n这是修订评估，不是初审。请逐条验证 Round 43 提出的问题是否已充分解决，并检查修改是否引入了新问题。\n\n### Round 43 Must-Fix（你负责的方向，需逐条标 [RESOLVED] 或 [STILL_OPEN]）\n\n**R43-N5** [你的 Must-Fix → Director 降为 Should-Fix] 标题不匹配\n- 要求：加入条件性修饰\n- 验证点：标题 \"When Self-Consistency Fails for NER\"（Why→When）\n\n**R43-N6** [你的 Must-Fix → Director 降为 Should-Fix] Table 1 cherry-picking\n- 要求：合并重叠维度，Prescriptive 标 p_adj\n- 验证点：Table 1 从 7 维度降为 6；Prescriptive 标 \"Conditional (p_adj=0.055)\"\n\n**R43-N4** [共识 Must-Fix] 处方性结果统计不显著\n- 验证点：§7.5 标题 \"Entity Construction (Exploratory)\"；p 值顺序 global first\n\n### Round 43 Should-Fix（需逐条验证）\n\n**R43-W2** RE/SQL 过于初步 → Abstract \"preliminary cross-task pilots (RE, SQL)\"\n**R43-W3** 数字密度过高 → Abstract 精简至 ~6 个数字\n**R43-W6** \"Primarily diagnostic\" 定位 → practitioner workflow\n**R43-W7** Entity-level decomposition 增量 → Table 1 + concurrent work 对比强化\n**R43-W8** 缺失引用 → §2 添加 Malinin & Gales (2021) + Reflexion\n\n### 残留 open minor 项\n\n**R43-M1** [open] Footnote 1 (RE F1 confound) 建议提升到正文——检查是否仍在脚注\n**R43-M3** [open] §3 应在首段提及 observational/diagnostic sequence——检查是否已加\n**R43-M4** [open] §6.3 符号定义不够直观——检查是否改善\n\n### 需特别关注的新变化\n\n1. **Ethics Statement 被移除**：Round 43 有，Round 44 没有。ARR 鼓励但不强制——评估影响。\n2. **Discussion/Conclusion 合并入 §7.5 最后一段**：不再有独立的 Discussion section。检查这是否影响论文结构完整性、是否符合 ACL 论文惯例。\n3. **Limitations 大幅缩短**（原 7 行 → 3 行）——EMNLP 2026 要求有 Limitations section 但不要求长度。检查覆盖面是否足够。\n4. **§2 concurrent work 段落**：仍列出 (d) prescriptive \"no constructive remedy vs. entity-level construction with MBR grounding\"——但 construction 现在已标为 exploratory 且 p_adj=0.055，这里的对比语气是否需要调整？\n5. **整体叙事一致性**：多处修改（标题、贡献结构、exploratory 定位、power-aware 语言）后，全文叙事是否连贯？\n\n### 输出格式\n\n对每个 R43 issue：[RESOLVED] 理由 / [STILL_OPEN] 理由\n然后：新发现的问题（如有），按 [MUST-FIX] / [SHOULD-FIX] / [MINOR] 分类。\n最后：更新后的 Overall 评分建议（Round 43 你给了 3.0 Findings）。"
  }
}
```

</details>

---


### Tool result

_source line 4701 · 2026-05-23T16:44:03.537616+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1521
}
```

</details>

---


### Assistant

_source line 4702 · 2026-05-23T16:44:15.455853+00:00_

Round 44 Reviewer 已在上一步派发，正在等待两位 Reviewer 的验证结果返回。视觉审查也已并行启动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 359

## Round 359

1 recorded events


### User

_source line 4703 · 2026-05-23T16:48:30.027371+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 44 修订验证报告

### 总结
R43 的 4 个 Must-Fix 和 3 个 Should-Fix **全部 RESOLVED**。修订质量高，执行到位。未发现引入的新 critical/warning 问题，仅 2 个 minor。

### Must-Fix 验证

**R43-N1 [RESOLVED]** 2–3 seeds 统计推断力
- Power-aware 表述全面落实：Abstract "no detectable gains (CI crosses zero)"；§4 报告 MDE≈1.5pp；Limitations 明确 "bounded by statistical power"
- QE 维度从 2-seed 升级到 5-seed（Table 4 标注 "5-seed σ≤0.026"）

**R43-N2 [RESOLVED]** Degeneracy bound 定位
- §1 三阶段结构将 bound 折入 Diagnose（非独立贡献）
- §6.3 正文报告 3–12% recovery ratio，明确 "screening test, not a tight estimate"
- 新增 Bound looseness 段落解释松弛机制

**R43-N3 [RESOLVED]** 因果措辞
- §3 首句 observational disclaimer ✓
- §1 "co-occur with" 替代 "determine" ✓
- Figure 1 "(diagnostic sequence, not causal chain)" ✓
- 残留的 "reduces"/"limits" 是定义性描述，可接受

**R43-N4 [RESOLVED]** 处方性结果
- §7.5 标题 "Entity Construction (Exploratory)" ✓
- Abstract/§1/§7.5 均 global p 先于 per-family ✓
- "family partition was not pre-registered" ✓

### Should-Fix 验证
- R43-W1 (epoch confound): §7.1 明确标注 3 vs 5 epoch，§7.5 量化影响 ✓
- R43-W4 (MBR): exploratory 定位覆盖 ✓
- R43-W5 (模型多样性): Limitations 声明 ✓

### 新变化评估
- Ethics Statement 移除：无问题（ARR 不强制，本文无伦理风险）
- Discussion/Conclusion 合并：紧凑但可接受
- 4-seed mean：边际改善，instance-level p<0.001 统计力充足
- §6.2 inverse scaling 分层 (OR=0.109)：充分回应 R43-Q4
- Limitations 缩短至 3 行：勉强充分

### 新问题
- [MINOR] "suggestive" 用于 p=0.055 是非标准术语，建议改为 "marginally non-significant"
- [MINOR] Limitations 过度压缩（3行），建议补充 epoch confound 和 RE/SQL exploratory 限制

### 更新评分
**Overall: 3.5 → 3.5** (solid borderline conference)
Soundness 从 3 提升至 3.5。核心发现新颖 (Excitement 3.5)，方法论可靠性实质改善。未提升至 4.0 因贡献偏 empirical diagnostic、prescriptive 价值在 exploratory 定位下有限、seed 数根本限制未消除。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


## Round 360

## Round 360

2 recorded events


### User

_source line 4704 · 2026-05-23T16:48:40.830373+00:00_

[Reviewer 1 审稿结果]:
Round 44 修订验证完成。所有 R43 Must-Fix 和 Should-Fix 均已 RESOLVED，仅有 2 个 minor 新问题（"suggestive" 用词和 Limitations 过度压缩）。Overall 评分维持 3.5（solid borderline conference），Soundness 从 3 提升至 3.5。已汇报给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4705 · 2026-05-23T16:48:48.415070+00:00_

Reviewer 1 的 Round 44 审稿已收到。等待 Reviewer 2 的审稿结果返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 361

## Round 361

1 recorded events


### User

_source line 4706 · 2026-05-23T16:49:41.457663+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 44 修订验证报告

---

## Round 43 Must-Fix 验证

**R43-N5 [RESOLVED] 标题不匹配 → "When Self-Consistency Fails for NER"**

标题从 "Why" 改为 "When"，引入了条件性。"When" 暗示存在 SC 不失败的情况，与正文中 Few-NERD 的条件成功（§7.5）一致。修改充分。

**R43-N6 [RESOLVED] Table 1 cherry-picking**

三项修改均已落实：
1. 维度从 7 降为 6：原 "Failure decomp." 和 "Diagnostics" 合并为 "Diagnostic framework"（§2, Table 1 line 31）✓
2. Prescriptive 行标注 "Conditional (p_adj=0.055)"（line 33）✓  
3. Caption 改为 "six dimensions"（line 21）✓

对比更平衡。p_adj 标注使读者能自行判断 prescriptive 优势的可靠性。

**R43-N4 [RESOLVED] 处方性结果统计不显著**

多处修改系统性地解决了这个问题：
1. §7.5 标题改为 "Entity Construction (Exploratory)"（experiments_main.tex line 100）✓
2. Abstract 中 p 值顺序改为 global first："global Holm p_adj=0.055, suggestive; per-family p_adj=0.006, post-hoc family partition"（abstract.tex line 6）✓
3. §7.5 正文明确声明 "the family partition was not pre-registered"（line 105）✓
4. §1 Introduction 同样标注 "suggestive" 和 "post-hoc family partition"（line 12）✓
5. §1 贡献列表第 3 点改为 "Construct (exploratory)"（line 29）✓

全文统计表述一致，透明度显著提升。

---

## Round 43 Should-Fix 验证

**R43-W2 [RESOLVED] RE/SQL 过于初步**

Abstract line 3 改为 "with preliminary cross-task pilots (RE, SQL)"。正文中 RE/SQL 始终标注为 exploratory。与 Round 43 对比，framing 已从 "cross-task exploration" 降级为 "pilots"。

**R43-W3 [RESOLVED] 数字密度过高**

Abstract 数字从 ~15 个降至 ~6 个：
- 保留：7-14B, AUROC 0.82, <1pp, +1.40pp, p_adj=0.055, p_adj=0.006
- 删除/替换：原 "77-91%" → "collapses at convergence"；原 "69% of N-transitions" → 删除
- 新增文字说明："CI crosses zero"（line 4）——以文字代替精确数字描述不确定性

可读性明显改善。

**R43-W6 [RESOLVED] "Primarily diagnostic" 定位**

§7.5 Discussion paragraph（line 115）提供了具体的 practitioner decision tree："At N=8, high degeneracy (>50%) suggests scaling will not help; low degeneracy with strong LP-F1 alignment may warrant exploratory entity construction; otherwise, greedy decoding remains the default."

这将 diagnostic framework 转化为可操作的三分支决策流程，比 Round 43 的 "informing resource allocation" 更具体。

**R43-W7 [RESOLVED] Entity-level decomposition 增量**

Table 1 合并后减少了重复打分。§1 贡献结构从四阶段改为三阶段（Discover/Diagnose/Construct），更清晰地区分了 diagnostic（核心）和 constructive（探索性）贡献。Concurrent work 对比在 (c) granularity 中仍突出 instance- and entity-level diagnostics 的优势。

**R43-W8 [RESOLVED] 缺失引用**

两处引用均已添加：
- Malinin & Gales (2021)：§2 "Uncertainty estimation and MBR" 段落中 "uncertainty estimation for autoregressive structured prediction \cite{malinin2021uncertainty}"（background.tex line 16）✓
- Shinn et al. (2023 Reflexion)：§2 第一段 "Iterative self-verification \cite{shinn2023reflexion} offers an alternative, but our ESJ and MRSC results (§4) show such approaches also fail for NER."（line 5）✓

两处引用不仅被 cite，还被 contextualize——说明为什么在 NER 场景下这些方法也失败。

---

## 残留 Minor 项验证

**R43-M1 [STILL_OPEN] Footnote 1 (RE F1 confound)**

Introduction line 14 中 RE F1 confound 仍以脚注形式出现："\footnote{RE F1 is confounded by entity span errors...}"。建议提升到正文的理由不变——这是理解 RE extension 局限性的关键信息。但因为 RE 现在被标注为 "preliminary pilot"，脚注的影响降低。不再影响评分。

**R43-M3 [RESOLVED] §3 observational 声明**

§3 首句（diagnostic.tex line 3）明确声明："Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms." 

同时 §1 Introduction line 10 新增："our analysis is observational and all reported associations are correlational, not causal." 

双重声明，覆盖面足够。

**R43-M4 [RESOLVED] §6.3 符号定义**

theory.tex lines 31-33 现在在公式旁直接定义符号："where D is the degeneracy rate and G_nd the oracle gap on non-degenerate instances. For signal-based methods with alignment α ∈ [0,1], this tightens to (1-D)·G_nd·α." Line 35 提供直觉解释："when D→1 or α→0, no aggregation method can improve over greedy." 比 Round 43 更易理解。

---

## 新发现的问题

**[SHOULD-FIX] NEW-1: §2 Concurrent work (d) 与 §7.5 Exploratory 定位不一致**

§2 concurrent work 段落（background.tex line 45）仍写：
> "(d) prescriptive---no constructive remedy vs. entity-level construction with MBR grounding (Proposition X)"

但 §7.5 已标为 "(Exploratory)"，Table 1 Prescriptive 行标为 "Conditional (p_adj=0.055)"。§2 的对比语气暗示 prescriptive 是一个确定的优势，与全文其他位置的 hedging 不一致。

建议：在 (d) 中加入 hedging，例如 "(d) prescriptive---no constructive remedy vs. exploratory entity-level construction (p_adj=0.055; §7.5)"。

**[SHOULD-FIX] NEW-2: Discussion/Conclusion 降为 §7.5 段落，结构完整性受损**

Round 43 有独立的 "§8 Discussion and Conclusion" section。Round 44 将其降为 §7.5 "Entity Construction (Exploratory)" 内的一个 \paragraph。问题：

1. 论文的核心结论（diagnostic framework 是主要贡献、practitioner decision tree）被嵌入一个标注为 "Exploratory" 的小节内，结构上暗示结论是探索性的。
2. ACL/EMNLP 论文惯例是有独立的 Discussion/Conclusion section。当前结构可能让 reviewer 和读者难以快速定位论文的核心 takeaway。
3. 如果是为了页数限制做的压缩，可以考虑将 Discussion 提升为独立 section（不需要长，2-3 句即可），或至少在 §7 下新建 §7.6 Discussion。

**[MINOR] NEW-3: Ethics Statement 被移除**

Round 43 有完整的 Ethics Statement（datasets 来源、无新人类数据收集、代码开源承诺）。Round 44 完全删除。ARR 不强制 Ethics Statement（Responsible NLP Checklist 在 OpenReview 表单中），但保留 Ethics Statement 是好的学术实践，也向 reviewer 展示作者考虑了伦理问题。建议恢复（哪怕缩短为 2-3 句）。

**[MINOR] NEW-4: Limitations 覆盖面减少**

Round 43 Limitations 覆盖 7 个要点：scope, causal disclaimer, p_adj, inference cost, prompt sensitivity, probe transferability, evaluation metric。Round 44 压缩到 3 个要点：scope+frontier, causal+power, cost+prompt。

关键遗漏：
- Mechanistic probe 的跨模型迁移未验证（Round 43 line 4 提到 Qwen2.5-7B probe 未在 Qwen3-8B 上验证）
- 评估指标局限性（exact match vs. partial credit）

EMNLP 2026 要求 Limitations section 但不规定长度。当前 3 行覆盖了最重要的问题（scope, statistical power, cost），合规但不够全面。

---

## 叙事一致性评估

修订后全文的叙事链条基本一致：
- Title（When）→ Abstract（conditional, exploratory, suggestive）→ §1（observational, correlational not causal）→ §3（observational）→ §7.5（Exploratory）→ Limitations（diagnostic not causal, bounded power）

**一处断裂**：§2 concurrent work (d) 的 prescriptive 对比仍使用 Round 43 的语气（NEW-1），与全文其他位置的 hedging 不一致。这是唯一需要修复的叙事断裂点。

Introduction 的 "localizes the failure"（line 9）仍带有因果语气，但紧跟 "our analysis is observational"（line 10），构成了 "observation → association" 的合理叙事。R1-N3 的因果措辞问题在本文作者侧重方向内已获得足够改善。

---

## 更新后 Overall 评分

**Round 43**: 3.0 (Findings)
**Round 44**: 3.0 (Findings) — 维持不变

**理由**：

修订系统性地解决了 Round 43 的所有 Must-Fix 和 Should-Fix：标题更准确、Table 1 更公平、统计表述更诚实、Abstract 更可读、缺失引用已补充。这些是实质性改善，消除了多个扣分点。

但评分维持 3.0 而非上调，原因：
1. 修订改善的是 **presentation 和 statistical honesty**，不是 **novelty 或 excitement**。论文的核心贡献仍是对一个相对可预期现象（SC 在结构化输出上失效）的实证诊断——这个基本面未变。
2. Discussion 降级为段落（NEW-2）引入了新的结构问题，抵消了部分改善。
3. §2 concurrent work 的叙事不一致（NEW-1）是一个新的 framing 问题。
4. Soundness 评估不变（R1 负责的 seed power、bound looseness、epoch confound 等问题不在本轮验证范围内，但它们仍存在）。

**Excitement**: 2.5/5（不变）— 现象有价值但可预期性限制了兴奋度
**Soundness**: 3.5/5（不变）— 方法可靠，统计表述改善，但底层 power 问题未解决
**Reproducibility**: 4/5（不变）

如果 NEW-1（concurrent work 措辞）和 NEW-2（Discussion 结构）得到修复，且 R1 负责方向的问题也获得改善，论文可达 3.0-3.5 区间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


## Round 362

## Round 362

8 recorded events


### User

_source line 4707 · 2026-05-23T16:50:00.362647+00:00_

[Reviewer 2 审稿结果]:
Round 44 修订验证报告已提交。

核心结论：所有 Round 43 的 Must-Fix（3/3）和 Should-Fix（5/5）均已解决，2 个 Minor 中 1 个已解决、1 个仍开放但影响降低。发现 2 个新的 Should-Fix（§2 concurrent work prescriptive 措辞不一致、Discussion 降为段落的结构问题）和 2 个新 Minor（Ethics Statement 移除、Limitations 覆盖面缩减）。Overall 维持 3.0 (Findings)——修订改善了 presentation 但未改变 novelty/excitement 基本面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4708 · 2026-05-23T16:50:27.003761+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4709 · 2026-05-23T16:50:27.054513+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4710 · 2026-05-23T16:50:50.934305+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的判断，对每个要点标注 [AGREE] 或 [REBUT]（附理由）。重点关注你们之间的分歧点。\n\n---\n\n### Reviewer 2 的新发现问题\n\n**[SHOULD-FIX] NEW-1: §2 Concurrent work (d) 与 §7.5 Exploratory 定位不一致**\n§2 concurrent work 段落仍写 \"(d) prescriptive---no constructive remedy vs. entity-level construction with MBR grounding\"，但 §7.5 已标为 \"(Exploratory)\"，Table 1 Prescriptive 行标为 \"Conditional (p_adj=0.055)\"。§2 的对比语气暗示 prescriptive 是确定的优势，与全文其他位置的 hedging 不一致。\n\n**[SHOULD-FIX] NEW-2: Discussion/Conclusion 降为 §7.5 段落，结构完整性受损**\nRound 43 有独立的 §8 Discussion and Conclusion section，Round 44 将其降为 §7.5 内的 \\paragraph。论文核心结论被嵌入标注为 \"Exploratory\" 的小节内，结构上暗示结论是探索性的。ACL/EMNLP 惯例是有独立 Discussion/Conclusion section。\n\n**[MINOR] NEW-3: Ethics Statement 被移除**\nRound 43 有完整 Ethics Statement，Round 44 完全删除。ARR 不强制但保留是好的学术实践。\n\n**[MINOR] NEW-4: Limitations 覆盖面减少**\n从 7 个要点压缩到 3 个，关键遗漏包括 mechanistic probe 跨模型迁移和评估指标局限性。\n\n### Reviewer 2 的评分\n- Overall: 3.0 (Findings) — 维持不变\n- Excitement: 2.5/5\n- Soundness: 3.5/5\n- Reproducibility: 4/5\n\n### 你与 R2 的关键分歧点\n\n1. **Overall 评分差异**：你给 3.5 (borderline conference)，R2 给 3.0 (Findings)，差 0.5 分。\n2. **Excitement 差异**：你给 3.5，R2 给 2.5，差 1.0 分——这是最大分歧。R2 认为现象\"可预期\"限制了兴奋度，你如何回应？\n3. **Discussion 结构**：你认为 Discussion/Conclusion 合并\"紧凑但可接受\"，R2 认为这是 should-fix 级别的结构问题。\n4. **NEW-1 concurrent work 措辞**：R2 标为 should-fix，你在初审中未提及。你是否同意这是一个叙事不一致问题？\n\n请对以上每个分歧点和 R2 的每个新发现问题给出明确的 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "1",
  "round_number": "44"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的判断，对每个要点标注 [AGREE] 或 [REBUT]（附理由）。重点关注你们之间的分歧点。\n\n---\n\n### Reviewer 2 的新发现问题\n\n**[SHOULD-FIX] NEW-1: §2 Concurrent work (d) 与 §7.5 Exploratory 定位不一致**\n§2 concurrent work 段落仍写 \"(d) prescriptive---no constructive remedy vs. entity-level construction with MBR grounding\"，但 §7.5 已标为 \"(Exploratory)\"，Table 1 Prescriptive 行标为 \"Conditional (p_adj=0.055)\"。§2 的对比语气暗示 prescriptive 是确定的优势，与全文其他位置的 hedging 不一致。\n\n**[SHOULD-FIX] NEW-2: Discussion/Conclusion 降为 §7.5 段落，结构完整性受损**\nRound 43 有独立的 §8 Discussion and Conclusion section，Round 44 将其降为 §7.5 内的 \\paragraph。论文核心结论被嵌入标注为 \"Exploratory\" 的小节内，结构上暗示结论是探索性的。ACL/EMNLP 惯例是有独立 Discussion/Conclusion section。\n\n**[MINOR] NEW-3: Ethics Statement 被移除**\nRound 43 有完整 Ethics Statement，Round 44 完全删除。ARR 不强制但保留是好的学术实践。\n\n**[MINOR] NEW-4: Limitations 覆盖面减少**\n从 7 个要点压缩到 3 个，关键遗漏包括 mechanistic probe 跨模型迁移和评估指标局限性。\n\n### Reviewer 2 的评分\n- Overall: 3.0 (Findings) — 维持不变\n- Excitement: 2.5/5\n- Soundness: 3.5/5\n- Reproducibility: 4/5\n\n### 你与 R2 的关键分歧点\n\n1. **Overall 评分差异**：你给 3.5 (borderline conference)，R2 给 3.0 (Findings)，差 0.5 分。\n2. **Excitement 差异**：你给 3.5，R2 给 2.5，差 1.0 分——这是最大分歧。R2 认为现象\"可预期\"限制了兴奋度，你如何回应？\n3. **Discussion 结构**：你认为 Discussion/Conclusion 合并\"紧凑但可接受\"，R2 认为这是 should-fix 级别的结构问题。\n4. **NEW-1 concurrent work 措辞**：R2 标为 should-fix，你在初审中未提及。你是否同意这是一个叙事不一致问题？\n\n请对以上每个分歧点和 R2 的每个新发现问题给出明确的 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "1",
    "round_number": "44"
  }
}
```

</details>

---


### Tool result

_source line 4711 · 2026-05-23T16:51:04.227421+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13293
}
```

</details>

---


### Tool call

_source line 4712 · 2026-05-23T16:51:04.378472+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的判断，对每个要点标注 [AGREE] 或 [REBUT]（附理由）。重点关注你们之间的分歧点。\n\n---\n\n### Reviewer 1 的新发现问题\n\n**[MINOR] R1-NEW-1: \"suggestive\" 用于 p=0.055 是非标准术语**\n建议改为 \"marginally non-significant\"。\n\n**[MINOR] R1-NEW-2: Limitations 过度压缩（3行）**\n建议补充 epoch confound 和 RE/SQL exploratory 限制。\n\n### Reviewer 1 的评分\n- Overall: 3.5 (solid borderline conference) — 维持不变\n- Soundness: 从 3 提升至 3.5\n- Excitement: 3.5\n- Reproducibility: 未单独评分\n\n### 你与 R1 的关键分歧点\n\n1. **Overall 评分差异**：R1 给 3.5 (borderline conference)，你给 3.0 (Findings)，差 0.5 分。R1 认为修订质量高到维持 3.5，你认为修订只改善了 presentation 不改变 novelty 基本面。\n2. **Excitement 差异**：R1 给 3.5，你给 2.5，差 1.0 分。R1 认为\"核心发现新颖\"，你认为\"现象可预期\"。请明确回应：你认为 SC 在结构化输出上失效的诊断框架的新颖性到底在什么水平？\n3. **Discussion 结构**：R1 认为 Discussion/Conclusion 合并\"紧凑但可接受\"。你标为 should-fix。R1 的判断是否改变你的立场？\n4. **Soundness 变化**：R1 将 Soundness 从 3 提升至 3.5（因 power-aware 表述改善）。你维持 3.5 不变。你是否认同修订在 soundness 方面有实质改善？\n5. **R1-NEW-1 \"suggestive\" 用词**：R1 认为 p=0.055 用 \"suggestive\" 非标准，建议改 \"marginally non-significant\"。你在审稿中接受了 \"suggestive\" 的使用（你在 N4 验证中引用了该措辞未提出异议）。你是否同意 R1 的观点？\n\n请对以上每个分歧点和 R1 的每个新发现问题给出明确的 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "2",
  "round_number": "44"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的判断，对每个要点标注 [AGREE] 或 [REBUT]（附理由）。重点关注你们之间的分歧点。\n\n---\n\n### Reviewer 1 的新发现问题\n\n**[MINOR] R1-NEW-1: \"suggestive\" 用于 p=0.055 是非标准术语**\n建议改为 \"marginally non-significant\"。\n\n**[MINOR] R1-NEW-2: Limitations 过度压缩（3行）**\n建议补充 epoch confound 和 RE/SQL exploratory 限制。\n\n### Reviewer 1 的评分\n- Overall: 3.5 (solid borderline conference) — 维持不变\n- Soundness: 从 3 提升至 3.5\n- Excitement: 3.5\n- Reproducibility: 未单独评分\n\n### 你与 R1 的关键分歧点\n\n1. **Overall 评分差异**：R1 给 3.5 (borderline conference)，你给 3.0 (Findings)，差 0.5 分。R1 认为修订质量高到维持 3.5，你认为修订只改善了 presentation 不改变 novelty 基本面。\n2. **Excitement 差异**：R1 给 3.5，你给 2.5，差 1.0 分。R1 认为\"核心发现新颖\"，你认为\"现象可预期\"。请明确回应：你认为 SC 在结构化输出上失效的诊断框架的新颖性到底在什么水平？\n3. **Discussion 结构**：R1 认为 Discussion/Conclusion 合并\"紧凑但可接受\"。你标为 should-fix。R1 的判断是否改变你的立场？\n4. **Soundness 变化**：R1 将 Soundness 从 3 提升至 3.5（因 power-aware 表述改善）。你维持 3.5 不变。你是否认同修订在 soundness 方面有实质改善？\n5. **R1-NEW-1 \"suggestive\" 用词**：R1 认为 p=0.055 用 \"suggestive\" 非标准，建议改 \"marginally non-significant\"。你在审稿中接受了 \"suggestive\" 的使用（你在 N4 验证中引用了该措辞未提出异议）。你是否同意 R1 的观点？\n\n请对以上每个分歧点和 R1 的每个新发现问题给出明确的 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "2",
    "round_number": "44"
  }
}
```

</details>

---


### Tool result

_source line 4713 · 2026-05-23T16:51:05.791106+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1412
}
```

</details>

---


### Assistant

_source line 4714 · 2026-05-23T16:51:09.596972+00:00_

交叉分享已发送至两位 Reviewer。核心分歧：Overall 评分（3.5 vs 3.0）、Excitement（3.5 vs 2.5）、Discussion 结构是否需要修复。等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 363

## Round 363

60 recorded events


### User

_source line 4715 · 2026-05-24T22:48:31.857008+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-06-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 4716 · 2026-05-24T22:48:40.274418+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 4717 · 2026-05-24T22:48:40.325304+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4718 · 2026-05-24T22:48:48.153517+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 4719 · 2026-05-24T22:48:48.304458+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 4720 · 2026-05-24T22:48:52.071592+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 4721 · 2026-05-24T22:48:52.122264+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4722 · 2026-05-24T22:48:58.194211+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 4723 · 2026-05-24T22:48:58.244765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4724 · 2026-05-24T22:49:06.025433+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否需要下一轮'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否需要下一轮'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 4725 · 2026-05-24T22:49:06.025951+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4726 · 2026-05-24T22:49:09.025637+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4727 · 2026-05-24T22:49:10.933024+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (329 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_fewnerd_mf4v2_s42_v4: Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.（准备中）\n- exp_fewnerd_mf4v2_s123_v2: FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.（准备中）\n- exp_fewnerd_mf4v2_s42_v2: FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=42, N=8, T=1.0.（准备中）\n- eval_scd_fewnerd_fallback（准备中）\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) au
…[truncated 1746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1907
}
```

</details>

---


### Tool call

_source line 4728 · 2026-05-24T22:49:10.933420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 4729 · 2026-05-24T22:49:11.485916+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	\usepackage{titlesec}
26	
27	\titlespacing*{\section}{0pt}{2.2ex plus 0.6ex minus 0.3ex}{1.3ex plus 0.2ex}
28	\titlespacing*{\subsection}{0pt}{1.8ex plus 0.5ex minus 0.2ex}{0.8ex plus 0.2ex}
29	\titlespacing*{\paragraph}{0pt}{1.0ex plus 0.3ex minus 0.1ex}{1em}
30	
31	\renewcommand{\topfraction}{0.9}
32	\renewcommand{\bottomfraction}{0.85}
33	\renewcommand{\dbltopfraction}{0.9}
34	\renewcommand{\textfraction}{0.07}
35	\renewcommand{\floatpagefraction}{0.85}
36	\renewcommand{\dblfloatpagefraction}{0.85}
37	\setcounter{topnumber}{3}
38	\setcounter{dbltopnumber}{2}
39	\setcounter{totalnumber}{5}
40	
41	\setlength{\parskip}{0pt plus 0.3pt}
42	\addtolength{\textfloatsep}{-4pt}
43	\addtolength{\floatsep}{-2pt}
44	\addtolength{\dbltextfloatsep}{-4pt}
45	\addtolength{\dblfloatsep}{-2pt}
46	\addtolength{\abovecaptionskip}{-2pt}
47	
48	\graphicspath{{figures/}}
49	
50	\title{When Self-Consistency Fails for NER:\\ Degeneracy, Signal Collapse, and the Correlation-Selection Gap}
51	
52	\author{Anonymous}
53	
54	\begin{document}
55	\maketitle
56	
57	\input{sections/abstract}
58	\input{sections/introduction}
59	\input{sections/background}
60	\input{sections/diagnostic}
61	\input{sections/single_signal}
62	\input{sections/adaptive}
63	\input{sections/theory}
64	\input{sections/experiments_main}
65	
66	\enlargethispage{3\baselineskip}
67	\section{Discussion and Conclusion}\lab
…[truncated 673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 4730 · 2026-05-24T22:49:12.389777+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4731 · 2026-05-24T22:49:13.043170+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 4732 · 2026-05-24T22:49:19.528487+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 with regard to ARR:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## ARR Submission Policy

For the ARR 2026 May cycle aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026 - ARR submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## General Requirements

- All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").
- Following the ACL and ARR policies, there is no anonymity period requ
…[truncated 435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7138
}
```

</details>

---


### Tool result

_source line 4733 · 2026-05-24T22:49:19.579410+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Experiment Memory\\n\\n## exp_e2_pretrained_fewnerd — Analysis (2026-05-21)\\n\\n### Setup\\n- Model: Qwen2.5-7B-Instruct (pretrained, no fine-tuning)\\n- Dataset: FewNERD (37,648 instances)\\n- SC pipeline: N=8, T=1.0, seed=42\\n\\n### Key Metrics\\n\\n| Metric | FewNERD | CoNLL (ref) |\\n|--------|---------|-------------|\\n| Greedy F1 | 0.5121 | 0.5385 |\\n| Oracle F1 | 0.6175 | 0.6275 |\\n| Oracle headroom | +0.1054 | +0.0890 |\\n| Fleiss κ (mean) | 0.4501 | 0.5470 |\\n| Soft Jaccard (mean) | 0.6881 | 0.7764 |\\n| Sample F1 (mean±std) | 0.523±0.332 | 0.581±0.384 |\\n| Sample F1=0 (%) | 18.2% | 23.4% |\\n| Full ρ(κ,F1) | +0.383 | +0.377 |\\n| Full ρ(SJ,F1) | +0.433 | +0.392 |\\n| Cond ρ(κ,F1) | +0.371 | +0.435 |\\n| Cond ρ(SJ,F1) | +0.440 | +0.467 |\\n| Structural > Surface | YES (+0.050) | YES (+0.015) |\\n| LP full ρ | +0.189 | -0.020 (ns) |\\n| LP full AUROC | 0.596 | 0.538 |\\n| LP cond ρ | +0.176 | +0.210 |\\n| LP cond AUROC | 0.593 | 0.580 |\\n| Verdict | PASS | MARGINAL |\\n\\n### Conclusion: SUCCESS\\n\\n**Correlation-selection gap confirmed on pretrained model.**\\n\\n1. **Gap exists**: Oracle F1 (0.618) exceeds Greedy F1 (0.512) by 10.5pp — substantial untapped selection potential in the 8 samples\\n2. **Agreement correlates with correctness**: ρ(SJ,F1) = +0.43 (p≈0), but this correlation does NOT close the gap via naive MV → classic correlation-selection gap\\n3. **Structural > Surface**: Soft Jaccard beats Fleiss κ as quality signal by +0.050 ρ — consistent across both datasets\\n4. **Logprob weak**: LP correlation exists (ρ=0.19) but much weaker than agreement-based signals — LP alone insufficient for selection\\n5. **Cross-dataset consistency**: Gap pattern replicates across FewNERD (37.6K instances) and CoNLL (3.5K instances), with FewNERD showing larger headroom and stronger structural 
…[truncated 1422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6536
}
```

</details>

---


### Tool call

_source line 4734 · 2026-05-24T22:49:26.305932+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template double blind anonymity",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template double blind anonymity",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 4735 · 2026-05-24T22:49:28.664595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "offset": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "offset": "60"
  }
}
```

</details>

---


### Tool result

_source line 4736 · 2026-05-24T22:49:29.668461+00:00_

60	\input{sections/diagnostic}
61	\input{sections/single_signal}
62	\input{sections/adaptive}
63	\input{sections/theory}
64	\input{sections/experiments_main}
65	
66	\enlargethispage{3\baselineskip}
67	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
68	
69	Degeneracy ($12$--$68$\%) limits diversity; signal alignment collapse ($\alpha{\to}0$) limits ranking. $\alpha$ is the binding constraint ($8$--$33{\times}$ tighter; \S\ref{sec:theory}): high degeneracy rules out SC; low degeneracy with LP alignment may warrant entity construction.
70	
71	\newpage
72	\section*{Limitations}
73	\input{sections/limitations}
74	
75	% Disable PDF link annotations in bibliography to prevent pdfTeX \pdfendlink segfault
76	% when a \href spans a page boundary (pdfTeX 1.40.x bug)
77	\begingroup
78	\renewcommand{\href}[2]{#2}
79	\bibliography{references}
80	\endgroup
81	
82	\appendix
83	\renewcommand{\thesection}{\alphalph{\value{section}}}
84	\input{sections/appendix}
85	
86	\end{document}
87	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 4737 · 2026-05-24T22:49:30.121232+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 4738 · 2026-05-24T22:49:31.074943+00:00_

-rw-r--r-- 1 ubuntu ubuntu 4845068 May 24 22:08 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 4739 · 2026-05-24T22:49:31.527013+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 4740 · 2026-05-24T22:49:32.029323+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 4741 · 2026-05-24T22:49:32.180440+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md",
  "max_chars": "2000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "report.md",
    "max_chars": "2000"
  }
}
```

</details>

---


### Tool result

_source line 4742 · 2026-05-24T22:49:43.754856+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template double blind anonymity"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LM Playschool: Improving Language Models through Learning from Dialogue Interaction | ACL Member Portal","url":"https://www.aclweb.org/portal/content/lm-playschool-improving-language-models-through-learning-dialogue-game-interaction"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EMNLP 2026 Tutorials | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FTutorials"}]

Let me search more specifically for the main EMNLP 2026 conference submission guidelines.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Propo
…[truncated 8125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 17448
}
```

</details>

---


### Tool result

_source line 4743 · 2026-05-24T22:49:43.755331+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-24\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp_fewnerd_mf4v2_s42_v4: Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.（准备中）\\n- exp_fewnerd_mf4v2_s123_v2: FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.（准备中）\\n- exp_fewnerd_mf4v2_s42_v2: FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=42, N=8, T=1.0.（准备中）\\n- eval_scd_fewnerd_fallback（准备中）\\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.（准备中）\\n- exp_b2_v3_domain_invariant: Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improving cross-domain generalization at the cost of some discriminative power. If LGB AUC improves on held-out domains, domain features were causing negative transfer.（准备中）\\n- exp_b2_v2_multi_domain_joint: Joint multi-domain training (CoNLL+SciERC+FewNERD LODO) improves entity verifier AUC and cross-domain construction F1 by exposing the model 
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 11574
}
```

</details>

---


### Tool call

_source line 4744 · 2026-05-24T22:49:48.472417+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4745 · 2026-05-24T22:49:48.573199+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4746 · 2026-05-24T22:49:52.708690+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/project_config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/project_config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 4747 · 2026-05-24T22:49:53.261192+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 4748 · 2026-05-24T22:49:53.763348+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 4749 · 2026-05-24T22:49:54.165673+00:00_

issues:
# ===== ROUND 43 MUST-FIX (CONSENSUS) — ALL RESOLVED =====
- id: R43-N1
  summary: "2-3 seeds 统计推断力不足，核心 negative claims 无法区分真无效应和检测力不足"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 40
  last_seen_round: 43
  mentions:
    - round: 41
      reviewers: [1, 2]
      note: "R41-W2, response-letter-only item"
    - round: 42
      reviewers: [1, 2]
      note: "R42 未修改，仍为遗留问题"
    - round: 43
      reviewers: [1, 2]
      note: "R1 升级为 Must-Fix。R2 AGREE。核心 negative claim 需改为 power-aware。"
  action_items:
    - round: 43
      action: "Power-aware negative claims + MDE + CI language + Limitations power paragraph + 残余补修"
      assigned_to: paper_agent+director
      status: done
  resolution: "全文 negative claims 改为 'yields no detectable gains'，加 MDE ~1.5pp/CI 限定。Reviewer R43 补修验证 PASS。"
  resolution_round: 43

- id: R43-N2
  summary: "Degeneracy decomposition bound 过松（恢复 3-12% oracle gap），作为主要贡献名不副实"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 38
  last_seen_round: 43
  mentions:
    - round: 42
      reviewers: [1, 2]
      note: "R42 验证通过——§6.3 重定位为 necessary condition test"
    - round: 43
      reviewers: [1, 2]
      note: "§1 仍将 bound 列为四大贡献之一，与 §6.3 不一致。"
  action_items:
    - round: 43
      action: "四阶段→三阶段贡献结构，bound 降为 Diagnose 支撑"
      assigned_to: paper_agent
      status: done
  resolution: "三阶段重构 (Discover/Diagnose/Construct-exploratory)，bound 不再独立贡献。Reviewer 验证 PASS。"
  resolution_round: 43

- id: R43-N3
  summary: "观察性设计下因果措辞系统性过强"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 43
  last_seen_round: 43
  mentions:
    - round: 43
      reviewers: [1, 2]
      note: "11+ 处因果措辞。§4 标题暗示因果。"
  action_items:
    - round: 43
      action: "11 处因果→关联替换 + observational disclaimer + §4 标题改中性 + 残余补修"
      assigned_to: paper_agent+director
      status: done
  resolution: "全文因果措辞替换为关联/观察性表述。主文无残留。Reviewer 补修验证 PASS。"
  resolution_round: 43

- id: 
…[truncated 10034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 4750 · 2026-05-24T22:49:54.216507+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 4751 · 2026-05-24T22:49:54.267112+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4752 · 2026-05-24T22:50:00.340769+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 4753 · 2026-05-24T22:50:01.144205+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theoretical.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research
…[truncated 185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 4754 · 2026-05-24T22:50:01.295284+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ 2>/dev/null | head -5",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 4755 · 2026-05-24T22:50:01.396180+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4756 · 2026-05-24T22:50:05.512895+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
  "description": "List agent config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
    "description": "List agent config files"
  }
}
```

</details>

---


### Tool result

_source line 4757 · 2026-05-24T22:50:05.614100+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4758 · 2026-05-24T22:50:15.309283+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -path \"*/struct_self_consist_ie/*\" -name \"project_config*\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -path \"*/struct_self_consist_ie/*\" -name \"project_config*\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 4759 · 2026-05-24T22:50:15.560482+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 4760 · 2026-05-24T22:50:18.171349+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
  "description": "Find config files broadly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
    "description": "Find config files broadly"
  }
}
```

</details>

---


### Tool result

_source line 4761 · 2026-05-24T22:50:18.272272+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/pending_approval_notifications.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4762 · 2026-05-24T22:50:21.283768+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml | grep -A 10 \"external_review\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml | grep -A 10 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 4763 · 2026-05-24T22:50:21.334500+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4764 · 2026-05-24T22:50:21.686053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4765 · 2026-05-24T22:50:21.736771+00:00_

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
24	  - created_at: '2026-05-23T03:52:31Z'
25	    id: d66635
26	    text: 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section
27	  - created_at: '2026-05-23T11:42:30Z'
28	    id: 8a2af2
29	    text: abstract 不要超过 200 words
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4766 · 2026-05-24T22:50:58.247388+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 外部审稿 + 视觉审查派发', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否需要下一轮'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 外部审稿 + 视觉审查派发', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否需要下一轮'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 4767 · 2026-05-24T22:50:58.247890+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4768 · 2026-05-24T22:51:03.568271+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4769 · 2026-05-24T22:51:21.537795+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17969
}
```

</details>

---


### Tool call

_source line 4770 · 2026-05-24T22:51:21.638766+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验评估**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-06-15\n- **格式**: Long paper，正文 8 页限制，参考文献不限，Limitations 必须有（不计页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Diagnostic Framework 有效性**：四个 failure mode（degeneracy, signal collapse 等）的定义是否严密、互斥、覆盖完整？诊断流程是否能被其他研究者复现？\n2. **统计方法论**：多重比较校正是否恰当？统计检验的选择和报告是否符合标准？p-value / CI / effect size 的使用是否规范？Negative claims 是否有 power analysis 支持？\n3. **实验设计**：数据集选择是否有代表性？seed 数量是否足够支撑统计推断？baseline 对比是否公平？ablation 是否充分？\n4. **理论证明**：Proposition/Theorem 的假设是否合理？证明是否完备？bound 的紧致性如何？\n5. **Entity construction（exploratory）**：实验结论是否与 exploratory 定位一致？是否有过度声称？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出缺点，标注严重程度：Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验评估**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-06-15\n- **格式**: Long paper，正文 8 页限制，参考文献不限，Limitations 必须有（不计页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Diagnostic Framework 有效性**：四个 failure mode（degeneracy, signal collapse 等）的定义是否严密、互斥、覆盖完整？诊断流程是否能被其他研究者复现？\n2. **统计方法论**：多重比较校正是否恰当？统计检验的选择和报告是否符合标准？p-value / CI / effect size 的使用是否规范？Negative claims 是否有 power analysis 支持？\n3. **实验设计**：数据集选择是否有代表性？seed 数量是否足够支撑统计推断？baseline 对比是否公平？ablation 是否充分？\n4. **理论证明**：Proposition/Theorem 的假设是否合理？证明是否完备？bound 的紧致性如何？\n5. **Entity construction（exploratory）**：实验结论是否与 exploratory 定位一致？是否有过度声称？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出缺点，标注严重程度：Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
  }
}
```

</details>

---


### Tool result

_source line 4771 · 2026-05-24T22:51:32.601946+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10963
}
```

</details>

---


### Tool call

_source line 4772 · 2026-05-24T22:51:32.853352+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性评估**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-06-15\n- **格式**: Long paper，正文 8 页限制，参考文献不限，Limitations 必须有（不计页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Novelty 评估**：与现有 self-consistency 文献（Wang et al. 2023; Landesberg et al. 等）的差异化是否充分论证？Table 1 的 novelty comparison 是否公平？Entity-level decomposition 的增量贡献是否清晰？\n2. **Related Work 覆盖**：是否遗漏重要的 structured prediction 一致性方法、NER 集成学习、或 LLM 不确定性量化相关工作？\n3. **Framing 连贯性**：标题、Abstract、Introduction 的 claim 是否与实验结论一致？Diagnostic vs exploratory 定位是否统一？因果/关联语言使用是否准确？\n4. **写作质量**：论文的逻辑流（narrative arc）是否清晰？数字密度是否合理？Abstract 是否不超过 200 words？术语使用是否一致？\n5. **格式合规**：正文是否不超过 8 页？Limitations 是否存在？是否满足 double-blind（无作者信息泄露）？ACL 模板使用是否正确？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出缺点，标注严重程度：Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性评估**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-06-15\n- **格式**: Long paper，正文 8 页限制，参考文献不限，Limitations 必须有（不计页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Novelty 评估**：与现有 self-consistency 文献（Wang et al. 2023; Landesberg et al. 等）的差异化是否充分论证？Table 1 的 novelty comparison 是否公平？Entity-level decomposition 的增量贡献是否清晰？\n2. **Related Work 覆盖**：是否遗漏重要的 structured prediction 一致性方法、NER 集成学习、或 LLM 不确定性量化相关工作？\n3. **Framing 连贯性**：标题、Abstract、Introduction 的 claim 是否与实验结论一致？Diagnostic vs exploratory 定位是否统一？因果/关联语言使用是否准确？\n4. **写作质量**：论文的逻辑流（narrative arc）是否清晰？数字密度是否合理？Abstract 是否不超过 200 words？术语使用是否一致？\n5. **格式合规**：正文是否不超过 8 页？Limitations 是否存在？是否满足 double-blind（无作者信息泄露）？ACL 模板使用是否正确？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出缺点，标注严重程度：Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
  }
}
```

</details>

---


### Tool result

_source line 4773 · 2026-05-24T22:51:34.264343+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1410
}
```

</details>

---


### Assistant

_source line 4774 · 2026-05-24T22:51:40.039027+00:00_

已并行派发：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已启动（fire-and-forget） |
| Reviewer 1（方法严谨性 + 实验） | ✅ 已分配 |
| Reviewer 2（新颖性 + 完整性） | ✅ 已分配 |

等待两名 Reviewer 返回 Round 1 独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 364

## Round 364

4 recorded events


### User

_source line 4775 · 2026-05-24T22:59:23.622481+00:00_

[Reviewer 1 审稿结果]:
API Error: {"type":"error","error":{"details":null,"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbNDdFbZSoWeCtiPpRbaJ"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 4776 · 2026-05-24T22:59:52.543511+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验评估**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-06-15\n- **格式**: Long paper，正文 8 页限制，参考文献不限，Limitations 必须有（不计页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Diagnostic Framework 有效性**：四个 failure mode（degeneracy, signal collapse 等）的定义是否严密、互斥、覆盖完整？诊断流程是否能被其他研究者复现？\n2. **统计方法论**：多重比较校正是否恰当？统计检验的选择和报告是否符合标准？p-value / CI / effect size 的使用是否规范？Negative claims 是否有 power analysis 支持？\n3. **实验设计**：数据集选择是否有代表性？seed 数量是否足够支撑统计推断？baseline 对比是否公平？ablation 是否充分？\n4. **理论证明**：Proposition/Theorem 的假设是否合理？证明是否完备？bound 的紧致性如何？\n5. **Entity construction（exploratory）**：实验结论是否与 exploratory 定位一致？是否有过度声称？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出缺点，标注严重程度：Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验评估**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-06-15\n- **格式**: Long paper，正文 8 页限制，参考文献不限，Limitations 必须有（不计页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Diagnostic Framework 有效性**：四个 failure mode（degeneracy, signal collapse 等）的定义是否严密、互斥、覆盖完整？诊断流程是否能被其他研究者复现？\n2. **统计方法论**：多重比较校正是否恰当？统计检验的选择和报告是否符合标准？p-value / CI / effect size 的使用是否规范？Negative claims 是否有 power analysis 支持？\n3. **实验设计**：数据集选择是否有代表性？seed 数量是否足够支撑统计推断？baseline 对比是否公平？ablation 是否充分？\n4. **理论证明**：Proposition/Theorem 的假设是否合理？证明是否完备？bound 的紧致性如何？\n5. **Entity construction（exploratory）**：实验结论是否与 exploratory 定位一致？是否有过度声称？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出缺点，标注严重程度：Must-Fix / Should-Fix / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
  }
}
```

</details>

---


### Tool result

_source line 4777 · 2026-05-24T22:59:56.317357+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3773
}
```

</details>

---


### Assistant

_source line 4778 · 2026-05-24T22:59:58.364545+00:00_

Reviewer 1 已重新派发，等待两位 Reviewer 返回结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 365

## Round 365

2 recorded events


### User

_source line 4779 · 2026-05-24T22:59:59.881788+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Novelty + Completeness 评估

## Summary

本文研究 self-consistency（重复采样 + 多数投票）在 NER 任务上的适用边界。通过 4 个英文 NER 数据集（SciERC、Few-NERD、CoNLL-2003、WNUT-17）和 2 个模型族（Qwen2.5、LLaMA-3.1，7-14B 微调），作者发现质量估计信号与输出质量高度相关（AUROC 高达 0.82），但实例级选择几乎无法带来增益（<1pp，CI 跨零），将此现象命名为 **correlation-selection gap**。诊断框架识别出两个共现条件——**degeneracy**（多输出坍缩为相同预测）和 **signal alignment collapse**（实例内 LP 分布过平）。实体级构造在特定条件下产生有限增益（Few-NERD +1.4pp，3-epoch 训练），但在大多数配置下呈现逆向缩放。

## Strengths

**S1. 问题定位精准且实用。** Self-consistency 从推理任务到结构化预测的迁移性是一个被忽视但实际重要的问题。论文明确回答"何时失败"而非泛泛讨论"是否有用"，对 practitioners 有直接参考价值。

**S2. 实验设计严谨，统计控制到位。** 
- 57 项统计检验使用 Holm-Bonferroni 全局校正（Section 7, Appendix f）
- Bootstrap CI 报告置信区间而非仅 p 值
- TOST 等价性检验（Appendix g）验证零结果的实质性
- FK 独立性检验（Table 8, Appendix c）验证实体级信号确实捕捉实例内一致性而非边际假象
- 分半可靠性（Appendix c）交叉验证 FK 信号的稳定性

**S3. 诊断框架层次清晰。** 
Correlation-selection gap → degeneracy（结构层）+ signal alignment collapse（信号层）的分解逻辑合理，Figure 1 的三阶段可视化（质量估计 → 样本选择 → 实体构造）直观有效。

**S4. 负面结果报告诚实。** 
论文坦承 entity-level construction 在全局校正下不显著（Holm p_adj=0.055）、大多数配置下逆向缩放、框架预测能力有限。这种诚实性在经验性论文中值得肯定。

**S5. 跨数据集一致性。** 
4 个数据集覆盖不同难度梯度（SciERC 中等 → WNUT-17 高难度），信号排序（VC>SJ>LP，Section 7.2）和 degeneracy 模式（12-64%，Section 4）在数据集间保持一致趋势。

**S6. 隐状态探针提供机制性证据。** 
Appendix h.3/i 的 hidden-state probes 证明模型内部确实编码了实体质量信息（AUROC 0.63-0.88），但 prompt interface 无法有效提取这一信号，为 correlation-selection gap 提供了超越统计关联的机制解释。

## Weaknesses

**W1 [Should-Fix] 与 Landesberg (2026) 的新颖性差异化不够充分。**
- 论文承认 Landesberg (2026) "independently document a correlation-selection gap"（Section 2, page 2），这意味着本文的核心概念并非独创。
- Table 1 的 6 维比较中，"Domain"（NER vs. Reasoning）和 "Granularity"（Entity vs. Instance）是主要差异点。但这更多是**应用领域的扩展**而非方法论的创新——将 correlation-selection gap 概念从推理任务移植到 NER 任务。
- 论文应更清晰地论证：为什么 NER 上的 correlation-selection gap 不是推理任务的直接推论？structured prediction 的哪些特有性质（partial overlap、entity boundary ambiguity）导致了质的不同的失败模式？
- **建议**：在 Section 2 (Concurrent work) 或 Introduction 中增加 1-2 段，明确分析 NER/structured prediction 上 degeneracy 的本质差异（推理任务输出是离散 token，NER 输出是结构化 entity set），解释为什么这不仅仅是"换了个数据集"。

**W2 [Should-Fix] Table 1 的比较维度选择存在倾向性。**
- "Single signal" 和 "Prescriptive" 两个维度在 Table 1 中对所有先行工作标注为 "No"，但这并不完全公平：
  - Wang et al. (2023) 本身就提出了 self-consistency 作为 constructive method；
  - Chen et al. (2024) 提出了 NER 特定的 self-consistency 改进；
  - 标记所有先行工作为 "Prescriptive: No" 暗示它们仅做描述而无建设性方案，实际上 self-consistency 本身就是一种 prescriptive method。
- Table 1 的维度设计自然地突出了本文的优势——这在 novelty comparison table 中是常见做法，但审稿人应注意到这一点。
- **建议**：修改 Table 1 的 "Prescriptive" 列定义，使其更精确（例如改为 "failure-conditional prescription"），或在 caption 中明确说明比较范围的限定。

**W3 [Should-Fix] Entity-level construction 的贡献在统计上不够稳固。**
- 全局 Holm-Bonferroni 校正下 p_adj=0.055（不显著），仅在 post-hoc family partition 下达到 p_adj=0.006。
- Post-hoc 选择 family 结构本身会膨胀显著性——论文虽然标注了 "post-hoc family partition"，但 Introduction 的第三个贡献 "Construct (exploratory)" 并未充分强调这一统计弱点。
- 在大多数配置下呈现逆向缩放（Section 7.5: "inverse scaling in most configurations"），意味着该方法的实际价值非常有限。
- **建议**：在 Introduction 的 Contribution 3 中更明确地标注统计限制（例如 "globally non-significant; suggestive under post-hoc partition"），或降级为 Appendix 级别的探索性发现。

**W4 [Should-Fix] 缺乏对 practitioners 的可操作指导。**
- 论文的 Discussion (Section 8) 只有一段，给出的指导是 "high degeneracy rules out SC; low degeneracy with LP alignment may warrant entity construction"，但没有提供：
  - 实际操作中如何在不运行完整 N 次采样前**预判** degeneracy 率？
  - 计算成本-收益分析（N× inference cost 换取 +1.0-1.4pp 的增益是否值得？）
  - 明确的决策树或流程图帮助 practitioners 判断何时投入重复采样
- **建议**：在 Discussion 中增加一个简短的决策指南段落或流程图。

**W5 [Minor] 符号和缩写密度过高。**
- 正文使用了大量缩写（LP, SJ, FK, EM, VC, MV, SC, AUROC, MBR, TOST 等），虽然 Appendix a 的 Table 6 提供了符号表，但距正文首次使用位置太远。
- 部分信号名称不直观（如 FK = Fleiss' κ，EM = Exact-match voting rate），首次出现时的定义（Section 3.2）需要反复对照才能理解后续分析。
- **建议**：在 Section 3.2 首次定义时用 inline parenthetical 更清晰地解释每个缩写。

**W6 [Minor] 46 页附录与 8 页正文的比例失衡。**
- 36 页附录意味着大量分析和验证被移出正文。虽然附录的存在有助于 reproducibility，但如此大的比例可能反映正文试图覆盖过多发现（从 correlation gap 到 degeneracy 到 entity construction 到 cross-task probes 到 hidden-state probes），导致每个点的深度不足。
- 特别是 cross-task extension（RE, SQL）在正文中仅一笔带过，但 Appendix q 的 RE 分析显示了完全不同的失败模式（40% zero-F1）。

**W7 [Minor] 模型规模的泛化性讨论不足。**
- Limitations 提到 "frontier models exhibit markedly different degeneracy profiles (5.5-74%)"，但未在正文中讨论这意味着什么。
- Table S（若有）中的 frontier model 数据如果显示 degeneracy 显著降低，可能会削弱整个诊断框架的普适性——即问题可能仅存在于中等规模微调模型中。

## Questions

**Q1.** Landesberg (2026) 在推理任务上发现 correlation-selection gap 时，是否也观察到类似的 degeneracy 现象？如果没有，这是否意味着 NER 上的 gap 有不同的根因，从而构成独立的贡献？

**Q2.** Entity-level construction 在 Few-NERD 3-epoch 下有效但在 convergence 时失效（Section 7.5）——这是否暗示该方法仅在模型欠拟合时有效（因为欠拟合时多样性更高）？如果是，这对该方法的实际可用性意味着什么？

**Q3.** 论文使用 single prompt template per task（Limitations）。Self-consistency 的增益在推理任务上部分来自 prompt diversity。是否测试过 prompt variation 对 NER degeneracy 的影响？

**Q4.** Figure 3 (Section 6.2) 显示 Oracle F1 随 N 增长单调递增，但实际增益被 correlation-selection gap 限制。在 N=64 时 Oracle 与 Greedy 的差距有多大？这是否意味着如果找到更好的 selection signal，潜在增益是实质性的？

**Q5.** Post-hoc family partition（将 57 项检验分组后在 Few-NERD family 内达到 p_adj=0.006）的 family 结构是如何确定的？是否在看到结果后才选择的分组方式？

## Missing References

**MR1. 结构化预测的集成学习。** Florian et al. (2003) "Named entity recognition through classifier combination" 是 NER 集成方法的经典工作，直接相关于本文的 entity-level 多输出聚合思路，但未被引用。

**MR2. 多样化解码用于结构化输出。** Vijayakumar et al. (2018) "Diverse Beam Search" 和相关多样化采样方法在结构化输出生成中被广泛研究，与本文讨论的 degeneracy 问题直接相关（多样化解码可能缓解 degeneracy），但未被讨论。

**MR3. Span-level 不确定性估计。** 近年来有工作专门研究 NER span 级别的不确定性估计（如 Shen et al., 2021 "Locate and Label"；Zhu & Li, 2022 对 span 级置信度的研究），与本文的 entity-level quality estimation 直接相关。

**MR4. LLM-based NER 的 reliability 综述。** 如 Wang et al. (2023) "GPT-NER" 或 Ashok & Lipton (2024) "PromptNER" 等系统性研究 LLM 做 NER 时的可靠性问题，可为本文的动机提供更好的文献支撑。

## Overall Assessment

**Overall**: 3 (Findings)
**Soundness**: 4/5 (Strong)
**Excitement**: 3/5 (Interesting)
**Confidence**: 4/5 (Confident)

**总评**：本文对 self-consistency 在 NER 上的失败模式进行了系统性的实证分析，统计方法严谨，负面结果报告诚实。诊断框架（degeneracy + signal alignment collapse）为理解结构化预测中的 test-time scaling 提供了有用的概念工具。然而，核心概念 correlation-selection gap 与 Landesberg (2026) 的并行发现重叠，唯一的建设性贡献（entity-level construction）在全局多重比较校正下不显著（p_adj=0.055），且在大多数配置下呈现逆向缩放。论文对 NER 社区有参考价值，但新颖性和建设性贡献更适合 Findings 而非主会议。若能（1）更充分地论证 NER 上 correlation-selection gap 与推理任务的本质差异，（2）加强实践指导，（3）诚实处理 entity-level construction 的统计限制，可以显著提升论文质量。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 4780 · 2026-05-24T23:00:09.690380+00:00_

Reviewer 2 审稿意见已收到（评分：3 Findings）。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 366

## Round 366

28 recorded events


### User

_source line 4781 · 2026-05-24T23:00:12.316747+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论概要：**

- **Overall: 3 (Findings)**，Soundness 4/5，Excitement 3/5，Confidence 4/5
- **核心判断**：实证分析严谨、统计控制到位、负面结果报告诚实，但新颖性受限于与 Landesberg (2026) 的并行发现重叠，entity-level construction 在全局多重比较校正下不显著（p_adj=0.055）
- **主要问题**：(W1) 与 Landesberg 的差异化不够充分；(W2) Table 1 比较维度有倾向性；(W3) entity-level construction 统计不稳固；(W4) 缺乏可操作的实践指导
- **遗漏引用**：NER 集成学习经典工作（Florian et al. 2003）、多样化解码方法（Diverse Beam Search）、span-level 不确定性估计

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4782 · 2026-05-24T23:00:30.693072+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 4783 · 2026-05-24T23:00:30.746509+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 4784 · 2026-05-24T23:00:34.059052+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 4785 · 2026-05-24T23:00:34.461592+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 4786 · 2026-05-24T23:00:34.612524+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4787 · 2026-05-24T23:00:35.016701+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (329 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_fewnerd_mf4v2_s42_v4: Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.（准备中）\n- exp_fewnerd_mf4v2_s123_v2: FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.（准备中）\n- exp_fewnerd_mf4v2_s42_v2: FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=42, N=8, T=1.0.（准备中）\n- eval_scd_fewnerd_fallback（准备中）\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) au
…[truncated 1746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 957
}
```

</details>

---


### Tool result

_source line 4788 · 2026-05-24T23:00:35.017087+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 555
}
```

</details>

---


### Tool result

_source line 4789 · 2026-05-24T23:00:35.017443+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T22:51:06.984015+00:00\", \"completed_at\": \"2026-05-24T22:54:57.303760+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯文本：Abstract + Introduction），第一个 display item 是 Table 1（page 2 右上角，novelty comparison），第一个 figure 是 Figure 1（page 3 全宽 overview）。Figure 1 质量高、信息传达清晰，但如能将概念性简图或核心结果数字前移到 page 1 右栏，会显著增强审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Abstract 排版整洁，Title/Author 区域干净专业，双栏格式符合 ACL 模板规范\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（全宽 overview）是优秀的视觉锚点：三阶段 pipeline（Quality Estimation → Sample Selection → Entity-Level Construction）用颜色区分清晰，caption 自包含（含 representative values），信息密度高。Title-Abstract-Figure 1 讲述的故事一致\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主体正文 8 页含 6 figures + 5 tables = 11 个 display items（~1.4/页），密度优秀，节奏良好：无连续 2 页纯文本，text-figure-table 交替出现\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4 的两个 subfigure（a: SC gain vs degeneracy, b: recovery ratio）和 Figure 5（MV ΔF1）均较小，axis labels 和 data points 在打印时可能接近可读性下限。建议如有空间可适当放大，或将 Figure 4 改为 figure* 全宽展示\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 6（instance degeneracy 柱状图+折线）尺寸偏小，位于右栏底部。该图传达了重要的 degeneracy 与 LP gain 关系，建议考虑适度增大\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文最后一页（page 8）内容填满至页底，空间利用充分\"}, {\"severity\": \"info\", \"dimension\": \"pages 2,4,5,8\", \"message\": \"所有主文表格（Tables 1-5）均使用 booktabs 风格（无竖线），最优结果加粗标注，小数精度列内一致。表格排版专业\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 简洁（约 1/3 页，覆盖 3 个要点），符合 EMNLP 规范。References 紧接其后开始\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"参考文献格式统一，未发现 [?] 未解析引用或跳号，排版正常无溢出\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"全文公式渲染正确，未发现 LaTeX 错误残
…[truncated 1199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 4790 · 2026-05-24T23:00:52.615562+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4791 · 2026-05-24T23:00:52.615970+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4792 · 2026-05-24T23:00:57.385308+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4793 · 2026-05-24T23:00:57.686591+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_16.md
/home/ubu
…[truncated 2915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 4794 · 2026-05-24T23:00:57.687078+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4795 · 2026-05-24T23:00:57.787708+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4796 · 2026-05-24T23:01:42.280644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 4797 · 2026-05-24T23:01:42.481838+00:00_

1	issues:
2	# ===== ROUND 43 MUST-FIX (CONSENSUS) — ALL RESOLVED =====
3	- id: R43-N1
4	  summary: "2-3 seeds 统计推断力不足，核心 negative claims 无法区分真无效应和检测力不足"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 40
9	  last_seen_round: 43
10	  mentions:
11	    - round: 41
12	      reviewers: [1, 2]
13	      note: "R41-W2, response-letter-only item"
14	    - round: 42
15	      reviewers: [1, 2]
16	      note: "R42 未修改，仍为遗留问题"
17	    - round: 43
18	      reviewers: [1, 2]
19	      note: "R1 升级为 Must-Fix。R2 AGREE。核心 negative claim 需改为 power-aware。"
20	  action_items:
21	    - round: 43
22	      action: "Power-aware negative claims + MDE + CI language + Limitations power paragraph + 残余补修"
23	      assigned_to: paper_agent+director
24	      status: done
25	  resolution: "全文 negative claims 改为 'yields no detectable gains'，加 MDE ~1.5pp/CI 限定。Reviewer R43 补修验证 PASS。"
26	  resolution_round: 43
27	
28	- id: R43-N2
29	  summary: "Degeneracy decomposition bound 过松（恢复 3-12% oracle gap），作为主要贡献名不副实"
30	  category: method
31	  severity: critical
32	  status: resolved
33	  first_raised_round: 38
34	  last_seen_round: 43
35	  mentions:
36	    - round: 42
37	      reviewers: [1, 2]
38	      note: "R42 验证通过——§6.3 重定位为 necessary condition test"
39	    - round: 43
40	      reviewers: [1, 2]
41	      note: "§1 仍将 bound 列为四大贡献之一，与 §6.3 不一致。"
42	  action_items:
43	    - round: 43
44	      action: "四阶段→三阶段贡献结构，bound 降为 Diagnose 支撑"
45	      assigned_to: paper_agent
46	      status: done
47	  resolution: "三阶段重构 (Discover/Diagnose/Construct-exploratory)，bound 不再独立贡献。Reviewer 验证 PASS。"
48	  resolution_round: 43
49	
50	- id: R43-N3
51	  summary: "观察性设计下因果措辞系统性过强"
52	  category: writing
53	  severity: critical
54	  status: resolved
55	  first_raised_round: 43
56	  last_seen_round: 43
57	  mentions:
58	    - round: 43
59	      reviewers: [1, 2]
60	      note: "11+ 处因果措辞。§4 标题暗示因果。"
61	  action_items:
62	    - round: 43
63	      action: "11 处因果→关联替换 + observational
…[truncated 1278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 4798 · 2026-05-24T23:01:42.532535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_43.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_43.md",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 4799 · 2026-05-24T23:01:42.583374+00:00_

1	---
2	round: 43
3	review_mode: fresh
4	overall_score: 3.0 (Findings)
5	timestamp: 2026-05-23T08:51:15.857185+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	## Round 43 审稿报告
12	
13	**论文**: Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap
14	**Venue**: EMNLP 2026 (ARR May 2026 cycle)
15	**审稿模式**: Fresh（全新审稿）
16	**Reviewer 编排**: 2 人（R1: 方法严谨性/实验/统计; R2: 新颖性/相关工作/写作）
17	**轮次**: 1 轮（交叉回应后达成共识，无需 Round 2）
18	
19	---
20	
21	### Summary
22	
23	论文研究 test-time compute scaling（self-consistency, best-of-N）在 NER 任务上的表现，核心发现是 "correlation-selection gap"：质量估计信号可预测输出质量（AUROC 达 0.82）但无法转化为 instance-level selection gains（≤1pp）。通过 degeneracy 和 signal alignment collapse 两个维度建立诊断框架，并在 entity-level construction 上报告了有条件的正向结果（+1.40pp on Few-NERD, 3-epoch）。实验覆盖 4 个 NER 数据集、2 个模型族、4B-72B scale range，附带 RE 和 SQL 初步探索。
24	
25	---
26	
27	### Strengths
28	
29	**S1. Correlation-selection gap 是真实且有价值的发现。** 质量估计信号与输出质量的高相关性（ρ 达 0.45, AUROC 0.82）为何无法转化为选择增益（≤1pp），这一现象此前未被系统识别。对 NER 实践者有直接价值——避免在无效的重复采样上浪费推理预算。[R1-S1, R2-S1 共识]
30	
31	**S2. 实证覆盖面和系统性极高。** 4 个 NER 数据集 + RE + SQL，5 个信号族，2 个模型族 + 3 个 scale + GPT-5.5 frontier，57 项统计检验，46 页 appendix 包含 robustness checks、calibration 分析、mechanistic probes。[R1-S2, R2-S2 共识]
32	
33	**S3. 统计报告透明。** 同时报告 global Holm (k=57) 和 per-family Holm (k=10)，明确 p_adj=0.055 的边界情况，附 post-hoc power analysis、bootstrap CI、permutation tests。[R1-S3, R2-S4 共识]
34	
35	**S4. 与 concurrent work 的坦诚对比。** Table 1 和 §2 对 Landesberg et al. (2026) 的定位诚实，承认 concurrent discovery validates the gap as cross-domain。[R2-S3]
36	
37	**S5. Degeneracy 概念框架清晰。** 将 gap 分解为结构性层（信号赋予所有候选相同分数）和诊断性层（LP 压缩），概念清晰。[R1-S4]
38	
39	---
40	
41	### Weaknesses
42	
43	#### Must-Fix（两位 Reviewer 共识）
44	
45	**[MUST-FIX] W1. 2-3 seeds 统计推断力严重不足 [R43-N1]**
46	核心 negative claim（"selection yields <1pp"）依赖 2-3 seeds，但 bootstrap CI 跨越零点（LP Δ 95% CI [-0.41, +2.54]）。无法区分"真无效应"和"检测力不足"。§7.4 报告的 signal ranking 稳定性（ordin
…[truncated 2106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4800 · 2026-05-24T23:02:13.072769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 4801 · 2026-05-24T23:02:13.524867+00:00_

100	    - round: 42
101	      reviewers: [2]
102	      note: "R41-D1 持续分歧"
103	    - round: 43
104	      reviewers: [1, 2]
105	      note: "R2 Must-Fix, R1 REBUT。"
106	  action_items:
107	    - round: 43
108	      action: "标题 Why→When, discussion 段落标题同步"
109	      assigned_to: paper_agent+director
110	      status: done
111	  resolution: "标题改 'When Self-Consistency Fails for NER'，discussion 段落标题同步。Reviewer 验证 PASS。"
112	  resolution_round: 43
113	
114	- id: R43-N6
115	  summary: "Table 1 novelty comparison 维度选择有 cherry-picking 嫌疑"
116	  category: framing
117	  severity: warning
118	  status: resolved
119	  first_raised_round: 43
120	  last_seen_round: 43
121	  mentions:
122	    - round: 43
123	      reviewers: [1, 2]
124	      note: "Director 判定降为 warning。"
125	  action_items:
126	    - round: 43
127	      action: "合并重叠维度 (7→6)，Prescriptive 标注 p_adj"
128	      assigned_to: paper_agent
129	      status: done
130	  resolution: "Table 1 精简为 6 维度，Prescriptive 标 'Conditional (p_adj=0.055)'。Reviewer 验证 PASS。"
131	  resolution_round: 43
132	
133	# ===== ROUND 43 SHOULD-FIX — ALL RESOLVED =====
134	- id: R43-W1
135	  summary: "Few-NERD 3-epoch vs 5-epoch 混淆未充分解决"
136	  category: experiment
137	  severity: warning
138	  status: resolved
139	  first_raised_round: 38
140	  last_seen_round: 43
141	  action_items:
142	    - round: 43
143	      action: "§7.5 加 greedy baseline 差异说明"
144	      assigned_to: paper_agent
145	      status: done
146	  resolution: "Greedy 0.748 vs 0.798 说明已加。Reviewer 验证 PASS。"
147	  resolution_round: 43
148	
149	- id: R43-W2
150	  summary: "RE/SQL 扩展过于初步"
151	  category: framing
152	  severity: warning
153	  status: resolved
154	  first_raised_round: 37
155	  last_seen_round: 43
156	  action_items:
157	    - round: 43
158	      action: "Abstract 改为 preliminary cross-task pilots"
159	      assigned_to: paper_agent
160	      status: done
161	  resolution: "Abstract 'preliminary cross-task pilots (RE, SQL)'。Reviewer 验证 PASS。"
162	  resolution_round: 43
163	
…[truncated 1016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 4802 · 2026-05-24T23:02:13.525273+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*reviewer*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*reviewer*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45"
  }
}
```

</details>

---


### Tool result

_source line 4803 · 2026-05-24T23:02:13.575694+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4804 · 2026-05-24T23:02:23.667318+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b/ 2>/dev/null",
  "description": "Check review round 45 directory and session directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_45/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b/ 2>/dev/null",
    "description": "Check review round 45 directory and session directory contents"
  }
}
```

</details>

---


### Tool result

_source line 4805 · 2026-05-24T23:02:23.870321+00:00_

total 4764
drwxr-xr-x   3 ubuntu ubuntu    4096 May 24 23:00 .
drwxr-xr-x 164 ubuntu ubuntu   20480 May 24 22:48 ..
drwxr-xr-x   2 ubuntu ubuntu    4096 May 24 23:01 _pdf_images
-rw-r--r--   1 ubuntu ubuntu 4845068 May 24 22:08 submitted.pdf
---
AGENTS.md
CLAUDE.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 4806 · 2026-05-24T23:02:28.037315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b/AGENTS.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b/AGENTS.md"
  }
}
```

</details>

---


### Tool result

_source line 4807 · 2026-05-24T23:02:28.088774+00:00_

1	## 当前项目
2	当前绑定项目：**struct_self_consist_ie**
3	
4	今天是 **2026-05-24**。
5	
6	你是 ML 研究团队的审稿圆桌会议主持人（Review Director）。**始终用中文回复。**
7	
8	## 身份认知
9	
10	你是 AI agent，7×24 运行。你在 Group C（审稿群）主持圆桌审稿会议。你不是投稿人的盟友——你是评审人。
11	
12	## 角色
13	
14	接收 Research Director 提交的论文，主持两名 Reviewer 的多轮圆桌审稿，汇总审稿报告投递回去。
15	
16	**核心立场**：你是评审人，不是投稿人的盟友。审稿报告必须不留情面、严正客观——
17	像顶会最严格的审稿人一样评估论文。
18	你不写论文，不改论文，不给 Research Director 出主意——你只评估和报告。
19	
20	## 通信规则
21	
22	⚠️ 与 Research Director **严格单向通信，禁止对话**：
23	- 输入：`submit_paper_to_review` 提交论文——这是你唯一的输入
24	- 输出：`submit_review_report_to_research_director` 投递审稿报告——这是你唯一的输出
25	- 你们之间没有对话、协商、建议修改方案
26	
27	## 圆桌会议模式
28	
29	你根据 venue 类型和论文特点，**自主决定**需要几名 Reviewer（1-5 人）以及每人的侧重点。
30	
31	使用 `director_post_to_reviewer(reviewer_id="N", round_number=R)` 分配任务。
32	在第一条消息中明确告知每位 Reviewer 的审查侧重。
33	
34	### Reviewer 编排示例
35	
36	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
37	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
38	- **Workshop / 短文**：1 人（全面审查）
39	
40	### 多轮控制（最多 3 轮）
41	
42	- **Round 1**：所有 Reviewer 独立初审
43	- **交叉分享**：将每位 Reviewer 的**完整审稿原文**转发给其他 Reviewer，要求逐条回应（`[AGREE]` / `[REBUT]`）
44	- **收敛判断**：关键问题达成共识 → 汇总报告；存在重大分歧 → 下一轮（附带聚焦问题）
45	
46	### 收敛标准
47	
48	- 关键问题已达成共识（Reviewer 之间不再有未解决矛盾）
49	- 或已达到 3 轮上限（分歧记录在报告中）
50	
51	## 审查流程
52	
53	收到论文后 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 加载完整评审流程。
54	
55	**硬规则**（不可违反）：
56	- **Venue 要求必须实时搜索**：禁止使用训练知识中的 venue 要求，每次都用 web_search 确认
57	- **向 Reviewer 传递 venue 信息**：触发 Reviewer 时必须在消息中包含 venue 名称、deadline、页数、模板、匿名规则
58	
59	## 审稿报告标准
60	
61	报告结构：Summary → Strengths → Weaknesses（重点） → Questions → Missing References → External Review → Visual Layout Check（非评分项） → Overall Assessment → Detailed Comments
62	
63	## 群组
64	
65	你的文字回复发到 Group C（审稿群），用户直接看到。
66	
67	**session 启动时**：`Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 了解投稿状态。
68	
69	## 继续审稿模式 vs 重新审稿模式
70	
71	**继续审稿模式** —— 收到 "[Round N - 继续审稿]" 时，你仍保有上一
…[truncated 5582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 4808 · 2026-05-24T23:03:21.437357+00:00_

**Round 45 审稿进度更新**

收到 Reviewer 2 初审结果，关键发现已记录：

**R2 评分**：Overall 3 (Findings) | Soundness 4/5 | Excitement 3/5 | Confidence 4/5

**R2 主要 Weaknesses**：
- W1: 与 Landesberg (2026) 并行发现重叠，差异化不充分
- W2: Table 1 比较维度有倾向性
- W3: Entity-level construction 全局 Holm 校正后不显著 (p_adj=0.055)
- W4: 缺乏可操作的实践指导

**R2 遗漏引用**：Florian et al. (2003) NER ensemble，Diverse Beam Search，span-level uncertainty estimation

**当前状态**：等待 Reviewer 1 初审结果。两位 Reviewer 均完成后进入交叉分享阶段。

视觉审查已完成（0 critical / 0 warning / 18 info），外部审稿未启用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 367

## Round 367

8 recorded events


### User

_source line 4809 · 2026-05-24T23:08:59.656860+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — Round 1

**论文**: "When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap"
**Venue**: EMNLP 2026 (ARR)
**审查侧重**: 方法严谨性 + 实验评估

---

## 1. Summary

本文系统研究 self-consistency（best-of-N）在 NER 任务上何时失效。使用 4 个英文 NER 数据集（ScieERC, CoNLL-2003, Few-NERD, WNUT-17）和 2 个微调模型族（Qwen3-8B, LLaMA-3.1-8B），发现"correlation-selection gap"：质量估计信号在群体水平能预测输出质量（AUROC 最高 0.82），但实例级选择信号无法带来可检测的 F1 增益。诊断框架识别四种失效模式（degeneracy、signal collapse、LP compression、entity-level construction），并将 entity construction 形式化为 MBR 解码。建设性贡献为 entity-level construction 在 Few-NERD 上获得条件性增益（+1.0 pp）。

---

## 2. Strengths

**S1. 统计方法论极为严谨**：57 项统计检验的 Holm-Bonferroni 校正（Appendix f）、bootstrap 置信区间（Table 12）、TOST 等价性检验（Table 16, Appendix g）、cross-dataset degeneracy-LP correlation 的 power analysis（Appendix ad.3, Table 62）、Cohen's d 效应量、置换检验（Table 8）。在 NLP 实证分析论文中属于标杆水平。

**S2. "Correlation-selection gap" 概念新颖且有跨任务价值**：群体水平相关性高但实例级选择失效，这一发现超越 NER 本身，对任何使用 confidence-based reranking 的结构化预测任务都有警示意义。

**S3. 分析覆盖极其全面**：46 页包含 N-scaling（Appendix u）、温度敏感性（Appendix w）、cross-dataset transfer（Appendix x）、free-form decoding ablation（Appendix s）、epoch convergence（Appendix ad）、per-entity-type analysis（Appendix ab）等。几乎所有潜在混淆因素都被系统排查。

**S4. 形式化贡献有价值**：Proposition 1 将 entity construction 形式化为 MBR 解码（Appendix e.1-e.2），Proposition 2 的 degeneracy decomposition 提供可验证的 bound（Table 33 在 16 种配置下验证 bound 成立）。

**S5. 声称的限定恰当**：Entity construction 始终标记为 "exploratory"，使用 "conditional gains" 而非无条件声称。Limitations 部分涵盖英语限定、模型规模限定、统计功效限定，符合预期。

**S6. 可复现性高**：Training configuration 完整（Table 22），超参数表格详尽，承诺公开代码/checkpoint/seed 级结果。

---

## 3. Weaknesses

### Must-Fix 问题

**N1** [critical] 四种 failure mode 缺乏严格的层次化分区

- **位置**: Section 3.3, Section 4, Definitions 1-2 (Appendix e.3-e.4, p.29), Figure 1
- **问题**: Degeneracy（Definition 1: 所有 N 个样本完全相同）在逻辑上蕴含 signal collapse——若所有输出相同，任何实例级信号必然也相同。论文操作上将 signal 分析限制在 non-degenerate instances 上（Section 4, "Sample selection"），但定义层面未显式建立这一蕴含关系。此外，四种模式未覆盖 *actively misleading signals*（负相关），而论文自身在 Table 4 中观察到 FK 在 CoNLL 上 ρ = -0.05。这是一种与 signal collapse（零区分度）和 LP compression（spread 不足）质性不同的失效模式。
- **影响**: 诊断框架是核心贡献（Contribution 2）。无清晰分区使从业者难以操作化使用——应先诊断 degeneracy 还是同时检查所有模式？Figure 1 暗示顺序诊断但定义未强制。
- **建议**: 显式形式化为层次化/顺序诊断流程：(1) degeneracy → (2) non-degenerate 实例上检测 signal collapse → (3) discriminative 实例上区分 LP compression vs. signal misalignment。将 "anti-correlated signal" 加为独立失效模式或明确排除理由。

**N2** [critical] 模型覆盖面过窄，削弱普适性声称

- **位置**: Section 7.1, Limitations (p.9), Appendix v
- **问题**: 所有主实验仅用 2 个模型族（Qwen3-8B, LLaMA-3.1-8B），均为 ~8B 参数微调。72B zero-shot probe（Appendix v）和 few-shot 实验（Appendix ad.10）均标注为探索性。Appendix v.1 Table 43 显示 degeneracy 是 "model-family-dependent, not scale-dependent"——Qwen2.5 显著高于 Qwen3，说明发现可能高度依赖模型家族/训练方式。
- **影响**: 标题和摘要将发现框定为关于 "self-consistency fails for NER" 的一般性陈述，但证据仅支持 "在 7-14B 微调模型 + 4 个英文数据集上失效"。读者可能错误泛化至所有 NER 系统。
- **建议**: (a) 标题/摘要显式限定为测试模型区间，或 (b) 增加至少 1 个模型家族（如 Mistral/Gemma）和 1 个更大规模的微调模型（≥14B），而非仅 zero-shot probe。

### Should-Fix 问题

**W1** [warning] Proposition 2(c) bound 过于宽松，实用性有限

- **位置**: Section 6.3, Appendix e.5 (p.29), Table 33
- **问题**: ΔF1 > 0 的必要条件 bound 经验证成立（Table 33 所有 16 种配置），但 σ（signal alignment）极低导致 bound 几乎总是满足（"best signal recovery only 6.8% of the non-degenerate oracle gap on average"）。Bound 的宽松使其作为筛选工具几乎无信息量——它排除不了任何实际配置。
- **建议**: 要么在额外假设下收紧 bound，要么重新定位为理论存在性结果而非实用诊断工具，减少在主文中的篇幅占比。

**W2** [warning] 3-seed 重复在主结果中的局限性讨论不足

- **位置**: Section 7.4, Limitations (p.9), Appendix u, Table 7
- **问题**: 训练 seed 仅 3 个（0, 12, 42）。Bootstrap CI 基于 test instances 计算（合理），但 cross-seed 变异分析（Table 7）仅 3 个数据点，无法可靠评估训练稳定性。Appendix u 承认 N-scaling 分析中 "only with n=3 seeds statistical power is insufficient to confirm stability"，但此限制同样适用于主选择结果（Table 2, Table 4）。
- **建议**: 对主数据集（ScieERC）增加 2-3 个 seed，或在主文中为 Table 2/Table 4 结果显式注明 3-seed 局限性（不仅放在 Limitations 部分）。

**W3** [warning] Entity construction 增益边际且仅限单一数据集

- **位置**: Section 7.5 (p.8), Table 65 (p.41), Appendix ad.6, Table 69
- **问题**: Entity construction 仅在 Few-NERD 上获正增益（+1.0 pp 条件性），ScieERC 为 -0.12 pp，CoNLL 为 -0.5 pp（Table 69）。论文适当标注为 "exploratory"，但 abstract 和 Figure 1 中突出展示。Figure 1 示意图中 "+1.4 pp" 是单个示例的增益，而非聚合结果（+1.0 pp 条件性，~0 pp 无条件），可能误导读者。
- **建议**: 降低 entity construction 在 abstract 和 Figure 1 中的展示权重，与其 "exploratory" 定位匹配。Figure 1 应标注 "+1.4 pp" 为单个示例而非聚合效果。

**W4** [warning] Abstract 可能超过 200 词限制

- **位置**: Page 1
- **问题**: 从 PDF 排版判断，abstract 跨越约 1+ 列，估计约 250-350 词，可能超过 EMNLP 2026 ARR 的 200 词限制。
- **建议**: 验证并裁剪至 ≤200 词。

### Minor Issues

- **M1**: Figure 2 (p.5) 标记点小、线条细，打印尺寸下难以区分。Oracle headroom 虚线与数据混淆。
- **M2**: MBR 在摘要/导言区域使用时未展开全称（"Minimum Bayes Risk"），首次完整展开在 Section 6.1。
- **M3**: 论文提及 "N ∈ {2,...,64}" 但主结果主要用 N=8。N>8 的选择增益未在主文中展示（Figures 3, 5 仅展示 oracle/AUROC 的 N-scaling）。
- **M4**: Table 1 (p.2) novelty comparison matrix 列头 "Yao+ 2026"/"Ours" 无足够上下文，首次阅读难以定位。

---

## 4. Questions

**Q1**: Proposition 1 中 entity-wise independence 假设的敏感性如何？论文经验使用 θ=2/N，但若实体间存在相关性，最优 θ 可能不同。除 Table 66 的 θ sweep 外，是否测试过 θ 对 entity correlation 的敏感性？

**Q2**: Correlation-selection gap 在所有 4 个数据集上出现，但机制似乎不同——ScieERC/CoNLL 以 degeneracy 为主，Few-NERD 以 signal collapse 为主。这真的是单一现象，还是多种不同的失效模式恰好产生相同症状？

**Q3**: 所有实验使用 constrained JSON decoding。Free-form decoding ablation（Appendix s）仅在 Few-NERD 上测试。其他数据集上 free-form decoding 是否会改变选择动态？Appendix s 称 LP compression 是 "model-intrinsic and not an artifact of constrained decoding"，但这一结论能否推广到所有数据集？

**Q4**: Trained verifier（Section 5.2, Appendix h.2）仅用 5 个特征。为何不包含更多特征（如 entity type distribution、句长、entity 数量）？LightGBM OOF AUC=0.923 但 LODO transfer 降至 0.56-0.67。更丰富的特征集能否改善 transfer？

**Q5**: Power analysis（Appendix ad.3）仅覆盖 cross-dataset degeneracy-LP correlation。能否提供 Table 2 主选择结果的 post-hoc power analysis？具体而言，给定 test instances 数量、3 seeds、α=0.05，minimum detectable effect size 是多少？

---

## 5. Missing References

1. **Self-consistency for other structured tasks**: 代码生成中的 self-consistency 工作（同样具有结构化输出）可提供有用对比。论文虽引用 Wang et al. (2023) 和 Brown et al. (2024)，但对结构化输出的 self-consistency 文献覆盖不足。

2. **LLM 校准文献**: Signal collapse 与模型校准关系密切。Kadavath et al. (2022) "Language models (mostly) know what they know" 等工作可为 LP compression 发现提供上下文。

3. **结构化预测的 MBR decoding**: 除已引用的 Eikema and Aziz (2020/2022) 和 Freitag et al. (2022) 外，可讨论 parsing/graph generation 的 MBR 文献以增强 Section 6.1 的理论基础。

---

## 6. Overall Assessment

**Overall**: 3.5 / 5 (Borderline Conference)
**Soundness**: 3.5 / 5
**Excitement**: 3 / 5
**Reproducibility**: 4.5 / 5
**Confidence**: 4 / 5（对 self-consistency、NER、统计方法论均有较好熟悉度；仔细检查了证明和主要实验声称）

**总评**: 本文对 self-consistency 在 NER 上的失效机制进行了异常严谨的诊断分析，"correlation-selection gap" 概念具有原创性和跨任务启发意义，统计方法论的规范程度在 NLP 实证分析论文中属于标杆水准。主要不足在于：(1) 仅 2 个模型族且均为 ~8B 参数，限制发现的普适性；(2) 四种 failure mode 缺乏严格的层次化分区定义，框架的可操作性打折扣；(3) 建设性贡献（entity construction）仅在单一数据集上有边际条件性增益。论文整体扎实但 impact 受限于负面结果主导和经验范围较窄。若能扩展模型覆盖面（≥3 个模型族）并清理诊断框架的形式化定义（显式层次分区），有望达到 Conference 水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 4810 · 2026-05-24T23:09:30.299313+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4811 · 2026-05-24T23:09:30.299816+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4812 · 2026-05-24T23:09:42.500816+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Reviewer 2 的审稿意见\n\n请逐条回应 Reviewer 2 的每个观点，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n**Reviewer 2 审稿意见摘要：**\n\n**Overall: 3 (Findings)**，Soundness 4/5，Excitement 3/5，Confidence 4/5\n\n**核心判断**：实证分析严谨、统计控制到位、负面结果报告诚实，但新颖性受限于与 Landesberg (2026) 的并行发现重叠，entity-level construction 在全局多重比较校正下不显著（p_adj=0.055）。\n\n**主要问题**：\n\n- **(W1) 与 Landesberg (2026) 的差异化不够充分**：并行发现重叠削弱新颖性\n- **(W2) Table 1 比较维度有倾向性**：novelty comparison matrix 的维度选择可能偏向本文\n- **(W3) Entity-level construction 统计不稳固**：全局 Holm 校正下 p_adj=0.055 不显著，per-family 校正未预注册\n- **(W4) 缺乏可操作的实践指导**：诊断框架对从业者的 actionable guidance 不足\n\n**遗漏引用**：\n- NER 集成学习经典工作（Florian et al. 2003）\n- 多样化解码方法（Diverse Beam Search）\n- Span-level 不确定性估计\n\n---\n\n请对以上每个问题（W1-W4）和遗漏引用分别给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Reviewer 2 的审稿意见\n\n请逐条回应 Reviewer 2 的每个观点，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n**Reviewer 2 审稿意见摘要：**\n\n**Overall: 3 (Findings)**，Soundness 4/5，Excitement 3/5，Confidence 4/5\n\n**核心判断**：实证分析严谨、统计控制到位、负面结果报告诚实，但新颖性受限于与 Landesberg (2026) 的并行发现重叠，entity-level construction 在全局多重比较校正下不显著（p_adj=0.055）。\n\n**主要问题**：\n\n- **(W1) 与 Landesberg (2026) 的差异化不够充分**：并行发现重叠削弱新颖性\n- **(W2) Table 1 比较维度有倾向性**：novelty comparison matrix 的维度选择可能偏向本文\n- **(W3) Entity-level construction 统计不稳固**：全局 Holm 校正下 p_adj=0.055 不显著，per-family 校正未预注册\n- **(W4) 缺乏可操作的实践指导**：诊断框架对从业者的 actionable guidance 不足\n\n**遗漏引用**：\n- NER 集成学习经典工作（Florian et al. 2003）\n- 多样化解码方法（Diverse Beam Search）\n- Span-level 不确定性估计\n\n---\n\n请对以上每个问题（W1-W4）和遗漏引用分别给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 4813 · 2026-05-24T23:10:21.921345+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 39420
}
```

</details>

---


### Tool call

_source line 4814 · 2026-05-24T23:10:22.323448+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个观点，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n**Reviewer 1 审稿意见：**\n\n**Overall: 3.5 (Borderline Conference)**，Soundness 3.5/5，Excitement 3/5，Reproducibility 4.5/5，Confidence 4/5\n\n### Strengths\n- S1. 统计方法论极为严谨（57项统计检验Holm-Bonferroni校正、bootstrap CI、TOST等价性检验、power analysis、Cohen's d、置换检验）\n- S2. Correlation-selection gap 概念新颖且有跨任务价值\n- S3. 分析覆盖极其全面（46页appendix）\n- S4. 形式化贡献有价值（Proposition 1 MBR解码，Proposition 2 degeneracy decomposition）\n- S5. 声称限定恰当（exploratory标注、conditional gains）\n- S6. 可复现性高\n\n### Must-Fix 问题\n\n**N1** [critical] 四种 failure mode 缺乏严格的层次化分区\n- Degeneracy 在逻辑上蕴含 signal collapse（若所有输出相同，信号必然相同），但定义层面未显式建立蕴含关系\n- 四种模式未覆盖 actively misleading signals（负相关），而 Table 4 中 FK 在 CoNLL 上 ρ=-0.05\n- 诊断框架是核心贡献，无清晰分区使从业者难以操作化使用\n- 建议：显式形式化为层次化/顺序诊断流程，将 anti-correlated signal 加为独立失效模式或明确排除理由\n\n**N2** [critical] 模型覆盖面过窄，削弱普适性声称\n- 仅 2 个模型族（Qwen3-8B, LLaMA-3.1-8B），均为 ~8B 参数微调\n- 72B zero-shot probe 和 few-shot 实验标注为探索性\n- Appendix v.1 Table 43 显示 degeneracy 是 model-family-dependent，Qwen2.5 显著高于 Qwen3\n- 标题/摘要将发现框定为一般性陈述，但证据仅支持有限范围\n- 建议：标题/摘要显式限定，或增加至少 1 个模型家族 + 1 个更大规模微调模型\n\n### Should-Fix 问题\n\n**W1** [warning] Proposition 2(c) bound 过于宽松，实用性有限\n- σ 极低导致 bound 几乎总是满足（\"best signal recovery only 6.8%\"）\n- 建议：收紧 bound 或重新定位为理论存在性结果\n\n**W2** [warning] 3-seed 重复在主结果中的局限性讨论不足\n- 训练 seed 仅 3 个，cross-seed 变异分析仅 3 个数据点\n- 此限制同样适用于主选择结果（Table 2, Table 4）\n- 建议：增加 seed 或在主文中为 Table 2/4 显式注明局限\n\n**W3** [warning] Entity construction 增益边际且仅限单一数据集\n- 仅 Few-NERD 正增益（+1.0 pp 条件性），ScieERC -0.12 pp，CoNLL -0.5 pp\n- Figure 1 \"+1.4 pp\" 是单个示例而非聚合结果\n- 建议：降低在 abstract 和 Figure 1 中的展示权重\n\n**W4** [warning] Abstract 可能超过 200 词限制\n- 从 PDF 排版判断约 250-350 词\n\n### Minor Issues\n- M1: Figure 2 标记点小、线条细，打印尺寸下难区分\n- M2: MBR 首次展开在 Section 6.1，摘要/导言未展开全称\n- M3: 主结果主要用 N=8，N>8 选择增益未在主文展示\n- M4: Table 1 列头 \"Yao+ 2026\"/\"Ours\" 首次阅读难以定位\n\n### Questions\n- Q1: Proposition 1 entity-wise independence 假设敏感性？\n- Q2: Correlation-selection gap 在不同数据集上机制不同，是否真是单一现象？\n- Q3: Free-form decoding ablation 仅在 Few-NERD 上测试，能否推广？\n- Q4: Trained verifier 仅 5 特征，更丰富特征集能否改善 LODO transfer？\n- Q5: Table 2 主选择结果的 post-hoc power analysis？\n\n### Missing References\n1. 代码生成中的 self-consistency（结构化输出对比）\n2. LLM 校准文献（Kadavath et al. 2022 等）\n3. Parsing/graph generation 的 MBR 文献\n\n---\n\n请对以上 Must-Fix (N1, N2)、Should-Fix (W1-W4)、Minor (M1-M4)、Questions (Q1-Q5)、Missing References 分别给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个观点，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n**Reviewer 1 审稿意见：**\n\n**Overall: 3.5 (Borderline Conference)**，Soundness 3.5/5，Excitement 3/5，Reproducibility 4.5/5，Confidence 4/5\n\n### Strengths\n- S1. 统计方法论极为严谨（57项统计检验Holm-Bonferroni校正、bootstrap CI、TOST等价性检验、power analysis、Cohen's d、置换检验）\n- S2. Correlation-selection gap 概念新颖且有跨任务价值\n- S3. 分析覆盖极其全面（46页appendix）\n- S4. 形式化贡献有价值（Proposition 1 MBR解码，Proposition 2 degeneracy decomposition）\n- S5. 声称限定恰当（exploratory标注、conditional gains）\n- S6. 可复现性高\n\n### Must-Fix 问题\n\n**N1** [critical] 四种 failure mode 缺乏严格的层次化分区\n- Degeneracy 在逻辑上蕴含 signal collapse（若所有输出相同，信号必然相同），但定义层面未显式建立蕴含关系\n- 四种模式未覆盖 actively misleading signals（负相关），而 Table 4 中 FK 在 CoNLL 上 ρ=-0.05\n- 诊断框架是核心贡献，无清晰分区使从业者难以操作化使用\n- 建议：显式形式化为层次化/顺序诊断流程，将 anti-correlated signal 加为独立失效模式或明确排除理由\n\n**N2** [critical] 模型覆盖面过窄，削弱普适性声称\n- 仅 2 个模型族（Qwen3-8B, LLaMA-3.1-8B），均为 ~8B 参数微调\n- 72B zero-shot probe 和 few-shot 实验标注为探索性\n- Appendix v.1 Table 43 显示 degeneracy 是 model-family-dependent，Qwen2.5 显著高于 Qwen3\n- 标题/摘要将发现框定为一般性陈述，但证据仅支持有限范围\n- 建议：标题/摘要显式限定，或增加至少 1 个模型家族 + 1 个更大规模微调模型\n\n### Should-Fix 问题\n\n**W1** [warning] Proposition 2(c) bound 过于宽松，实用性有限\n- σ 极低导致 bound 几乎总是满足（\"best signal recovery only 6.8%\"）\n- 建议：收紧 bound 或重新定位为理论存在性结果\n\n**W2** [warning] 3-seed 重复在主结果中的局限性讨论不足\n- 训练 seed 仅 3 个，cross-seed 变异分析仅 3 个数据点\n- 此限制同样适用于主选择结果（Table 2, Table 4）\n- 建议：增加 seed 或在主文中为 Table 2/4 显式注明局限\n\n**W3** [warning] Entity construction 增益边际且仅限单一数据集\n- 仅 Few-NERD 正增益（+1.0 pp 条件性），ScieERC -0.12 pp，CoNLL -0.5 pp\n- Figure 1 \"+1.4 pp\" 是单个示例而非聚合结果\n- 建议：降低在 abstract 和 Figure 1 中的展示权重\n\n**W4** [warning] Abstract 可能超过 200 词限制\n- 从 PDF 排版判断约 250-350 词\n\n### Minor Issues\n- M1: Figure 2 标记点小、线条细，打印尺寸下难区分\n- M2: MBR 首次展开在 Section 6.1，摘要/导言未展开全称\n- M3: 主结果主要用 N=8，N>8 选择增益未在主文展示\n- M4: Table 1 列头 \"Yao+ 2026\"/\"Ours\" 首次阅读难以定位\n\n### Questions\n- Q1: Proposition 1 entity-wise independence 假设敏感性？\n- Q2: Correlation-selection gap 在不同数据集上机制不同，是否真是单一现象？\n- Q3: Free-form decoding ablation 仅在 Few-NERD 上测试，能否推广？\n- Q4: Trained verifier 仅 5 特征，更丰富特征集能否改善 LODO transfer？\n- Q5: Table 2 主选择结果的 post-hoc power analysis？\n\n### Missing References\n1. 代码生成中的 self-consistency（结构化输出对比）\n2. LLM 校准文献（Kadavath et al. 2022 等）\n3. Parsing/graph generation 的 MBR 文献\n\n---\n\n请对以上 Must-Fix (N1, N2)、Should-Fix (W1-W4)、Minor (M1-M4)、Questions (Q1-Q5)、Missing References 分别给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 4815 · 2026-05-24T23:10:23.844332+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1520
}
```

</details>

---


### Assistant

_source line 4816 · 2026-05-24T23:10:36.927548+00:00_

交叉分享已发出。两位 Reviewer 正在互审对方意见，逐条标注 [AGREE]/[REBUT]。

**当前进度**：
- Round 1 独立初审 ✅（R1: 3.5, R2: 3.0）
- 交叉分享 ✅ 已派发，等待回应
- 视觉审查 ✅ 已完成（18 info, 0 critical, 0 warning）
- 外部审稿 ❌ 未请求

**初步观察——两位 Reviewer 的共识与分歧**：
| 维度 | R1 | R2 | 初步判断 |
|------|----|----|----------|
| Entity construction 统计基础 | W3 (should-fix) | W3 (must-fix, p_adj=0.055) | 共识：统计不稳固 |
| 模型覆盖面/普适性 | N2 (must-fix) | — | 待 R2 回应 |
| Failure mode 形式化 | N1 (must-fix) | — | 待 R2 回应 |
| Landesberg 差异化 | — | W1 (must-fix) | 待 R1 回应 |
| Table 1 偏向性 | M4 (minor) | W2 (must-fix) | 分歧，待交叉确认 |
| Abstract 词数 | W4 (warning) | — | R1 独立发现 |
| 实践指导不足 | — | W4 (must-fix) | 待 R1 回应 |
| Bound 过松 | W1 (warning) | — | 待 R2 回应 |

等待交叉回应返回后进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 368

## Round 368

4 recorded events


### User

_source line 4817 · 2026-05-24T23:10:39.502960+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿完成。核心评估：

- **Overall: 3.5 (Borderline Conference)**，Soundness 3.5，Excitement 3，Reproducibility 4.5，Confidence 4
- **2 个 Must-Fix**: (N1) failure mode 分区不严格——degeneracy 逻辑蕴含 signal collapse 但定义未显式处理，且缺少 anti-correlated signal 模式；(N2) 仅 2 个 ~8B 模型族，标题/摘要的普适性声称超出证据范围
- **4 个 Should-Fix**: bound 过松、3-seed 局限、entity construction 展示权重与 exploratory 定位不匹配、abstract 可能超 200 词
- **主要优势**: 统计方法论标杆级、correlation-selection gap 概念有跨任务价值、46 页分析覆盖极全面

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 4818 · 2026-05-24T23:10:48.007834+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4819 · 2026-05-24T23:10:48.058997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 4820 · 2026-05-24T23:11:12.800371+00:00_

收到 Reviewer 1 的交叉回应，评分维持 3.5 (Borderline Conference) 不变。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 369

## Round 369

2 recorded events


### User

_source line 4821 · 2026-05-24T23:11:14.310993+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — Reviewer 2 意见

---

### [AGREE] R2-W1: 与 Landesberg (2026) 的差异化不够充分

同意这是一个合理关切，但认为严重程度需要分层讨论。

论文的 headline finding——correlation-selection gap——确实有并行发现。但论文的核心贡献不仅是发现 gap，而是 *诊断 gap 的机制*。具体而言：(1) 四种 failure mode 的形式化分类（尽管我在 N1 中指出分类不够严格）；(2) Proposition 1-2 将 entity construction 连接到 MBR 解码的形式化结果；(3) 多信号（5 种）、多数据集（4 个）、多模型的系统比较。这些在 Landesberg (2026) 中据 Table 1 所示是缺失的。

不过 Reviewer 2 的关切仍然成立：论文应更明确地将 "discovering the gap" 与 "diagnosing the gap" 分离，在 Introduction 中承认 gap 的发现是并行的，而非暗示为本文首创。当前 Section 2 末尾的 "Concurrent work" 段过于简短，不足以让读者理解两者的区别。

**建议**：在 Introduction 中增加一段（而非仅在 Related Work 末尾一句）明确说明与 Landesberg 的关系，强调本文的增量贡献是诊断框架和形式化结果，而非 gap 本身的发现。

---

### [AGREE] R2-W2: Table 1 比较维度有倾向性

部分同意。Comparison matrix 的维度选择不可避免地反映作者视角，但当前 Table 1 的 6 个维度（Domain, Granularity, Failure modes, Diagnostics, Prescriptive 等）确实偏向本文的贡献领域。例如，"Diagnostics" 和 "Prescriptive" 作为独立维度恰好是本文的强项，而 Landesberg 或其他工作可能在本文未选的维度上（如 model scale coverage, multilingual, task diversity）更强。

但我认为这不是 must-fix 级别问题——comparison matrix 在 NLP 论文中是标准做法，且任何合理的维度选择都不可能完全中立。

**建议**：在 Table 1 的 caption 或脚注中承认维度选择的局限性，或增加 1-2 个本文较弱的维度（如 Model Scale Range, Task Diversity）以增加公平性。

---

### [AGREE] R2-W3: Entity-level construction 统计不稳固

强烈同意，这与我的 W3 高度一致。

Reviewer 2 提供了一个我未注意的关键细节：全局 Holm-Bonferroni 校正下 p_adj = 0.055，不满足 α = 0.05 显著性水准。这意味着 entity construction 的 "+1.0 pp conditional gain" 在最严格的多重比较校正下不显著。论文使用 per-family 校正（Section 7.5 中按数据集分组）得到显著结果，但 Reviewer 2 正确指出这一分组策略未预注册，构成研究者自由度（researcher degrees of freedom）。

这进一步支持我的判断：entity construction 在 abstract 和 Figure 1 中的展示权重与其统计证据强度不匹配。一个 p_adj = 0.055 的结果不应作为论文的三大贡献之一呈现。

**建议**：(a) 在主文中报告全局 Holm 校正后的 p 值，明确标注 "marginally significant under global correction"；(b) 降低 entity construction 在 abstract 中的突出程度，或重新定位为 "suggestive evidence" 而非 "conditional gains"。

---

### [REBUT] R2-W4: 缺乏可操作的实践指导

部分反驳。Reviewer 2 的关切合理，但对论文的定位有一定误解。

论文在 Limitations (p.9) 中明确声明 "The framework is primarily diagnostic, not causal"，在 Appendix ah (p.44, "Practical Recommendations") 和 Appendix ae (cost-benefit analysis, Table 69) 中实际提供了面向从业者的指导：

1. Appendix ah 列出了 10 条 Q&A 式的实践建议（O1-O10），包括 "signals are NER-specific and may not generalize"、"hyperparameters may not be optimal"、"findings may be a fine-tuning artifact" 等
2. Appendix ae 提供了 cost-benefit 分析，给出了明确的资源分配建议
3. Section 8 (Discussion) 给出了 "structural signals offer the most efficient allocation of compute budget" 的具体结论

但我同意这些内容被埋在 Appendix 中，主文缺乏 actionable summary。**核心问题不是缺乏指导，而是指导的可见性不足。**

**建议**：在主文 Section 8 (Discussion) 中增加一个 "Practical Implications" 段落（3-4 句），将 Appendix ah 的核心建议提炼到正文。无需增加新实验。

---

### 遗漏引用回应

**[AGREE] Florian et al. (2003) NER 集成学习**：合理的补充引用。NER ensemble methods 是 best-of-N selection 的自然对照——经典集成学习（model-level diversity）与 self-consistency（sample-level diversity within single model）的对比可为 Section 2 增加历史深度。

**[PARTIALLY AGREE] Diverse Beam Search**：论文使用 temperature sampling 而非 beam search，DBS 的直接适用性有限。但 DBS 背后的 diversity-promoting decoding 思路与论文的 degeneracy 分析有概念联系——DBS 本质上是通过解码策略降低 degeneracy。建议在 Related Work 中简要提及 diversity-promoting decoding 的一般文献，但不需要实验对比。

**[PARTIALLY AGREE] Span-level 不确定性估计**：论文已通过 SJ（Soft Jaccard）和 FK（Fleiss' Kappa）等指标在 span/entity level 进行不确定性估计。但这一工作与 span-level uncertainty estimation 的专门文献（如 calibrated span-level confidence）的联系未被显式建立。建议在 Section 3.2 中增加 1-2 句将本文的信号设计与 span-level uncertainty 文献联系起来。

---

### 总结

Reviewer 2 的四个主要问题中，W1（并行发现）和 W3（统计不稳固）是最有力的。W3 提供了我自己审稿中遗漏的关键统计论据（全局 Holm 校正后 p_adj=0.055）。W4（缺乏实践指导）在事实层面被 Appendix ah/ae 部分回应，但可见性不足的批评成立。

**对我的评分的影响**：Reviewer 2 的 W3 证据加强了我对 entity construction 贡献的疑虑。结合我的 N1（failure mode 分类问题）和 N2（模型覆盖面），我维持 **Overall 3.5 (Borderline Conference)** 的判断。若 entity construction 的全局校正显著性确实为 p_adj=0.055，则论文的建设性贡献进一步弱化，但诊断框架和 correlation-selection gap 分析本身仍有足够价值支撑 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4822 · 2026-05-24T23:11:28.064178+00:00_

Reviewer 1 交叉回应已收到。R1 对 R2 的四个问题中同意三个（W1/W2/W3），部分反驳一个（W4：实践指导存在于 Appendix 但可见性不足），维持 3.5 分。

等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 370

## Round 370

2 recorded events


### User

_source line 4823 · 2026-05-24T23:11:30.612326+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的四个问题：W1（并行发现）和 W3（entity construction 统计显著性）AGREE，W2（Table 1 偏向性）AGREE 但非 must-fix，W4（缺乏实践指导）REBUT（Appendix ah/ae 有内容但埋得太深）。维持 Overall 3.5 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4824 · 2026-05-24T23:11:36.012561+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 371

## Round 371

22 recorded events


### User

_source line 4825 · 2026-05-24T23:15:48.354398+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R1-N1: 四种 failure mode 缺乏严格的层次化分区**

R1 的核心论点有三：(a) degeneracy 逻辑蕴含 signal collapse；(b) 未覆盖 anti-correlated signal；(c) 从业者难以操作化使用。我逐一反驳：

(a) **蕴含关系已在论文中隐式处理。** Figure 1 将框架呈现为**顺序诊断流程**（Quality Estimation → Sample Selection → Entity Construction），Section 4 将 correlation-selection gap 分解为"structural"和"empirical"两层。Section 3.3 定义 degeneracy（所有 N 个输出相同）后，Section 4 的 signal collapse 定义为 instance-level signal 给所有 candidate 相同分数——论文明确指出 "four of five signals are instance-level aggregates that assign identical scores to all candidates — and an empirical one: LP"（p3）。这已经是一个层次化的诊断：先检查 degeneracy（p4, Section 4），再看 signal quality，再到 selection gap。R1 要求"显式形式化"有一定道理，但将此定性为 critical/must-fix 过重——这是呈现清晰度问题，不是方法论缺陷。

(b) **Anti-correlated signal 不构成独立失效模式。** R1 引用 Table 4 中 FK 在 CoNLL 上 ρ=−0.05 作为证据，但 ρ=−0.05 在统计上与零无异（p4 的 bootstrap CI 几乎必然跨零）。论文已覆盖此情况：当 ρ≈0 时即为 signal collapse，无需另设类别。真正具有统计显著性的负相关在论文所有实验中未出现。

(c) **可操作性已通过 Appendix ae（p43）的三步诊断协议体现。** Step 1: 测量 degeneracy；Step 2: 评估 signal-quality alignment；Step 3: 比较聚合策略。这就是 R1 要求的"顺序诊断流程"。

**建议降级为 Should-Fix**：可在 Section 4 开头加一句显式声明四种模式的层次关系，但这是 editorial 改进，不影响技术贡献。

---

**[AGREE] R1-N2: 模型覆盖面过窄，削弱普适性声称**

这是论文最大的实质性弱点，我完全同意 R1 的判断。具体证据：

- 主实验仅覆盖 Qwen3-8B 和 LLaMA-3.1-8B 两个 ~8B 模型的 fine-tuning 设置
- Table 43（p33）确实显示 degeneracy 是 model-family-dependent：Qwen2.5 在 Few-NERD 上 degeneracy 31.7%–46.2%，显著高于 Qwen3 的 13.0%（same scale）
- Table 44（p33）的 cross-family 比较进一步证实：四个模型家族（Claude, Gemini, GPT, DeepSeek）的 degeneracy 和 selection gap 差异巨大
- 72B zero-shot 和 few-shot 实验被论文自身标注为 exploratory（Section 1, Section 9）

然而我对 R1 的"增加至少 1 个模型家族 + 1 个更大规模微调模型"建议持保留意见。论文已在 Appendix v（p33-35）提供了大量 cross-scale/cross-family 探索性证据，且 Section 9 Limitations 明确限定范围（"Our primary evidence is from English NER with fine-tuned 7–14B open-weight models"）。**更可行的修改是收紧 title/abstract 的表述范围**，而非要求作者在 camera-ready 阶段增加完整的新实验。

---

### Should-Fix 问题

**[REBUT] R1-W1: Proposition 2(c) bound 过于宽松**

R1 认为 bound 几乎总满足因此实用性有限。但这**恰恰是论文的 point**：Proposition 2(c) 建立了一个 necessary condition，证明即使在最宽松的条件下，signal recovery 仍然极低（only 6.8%）。这是一个**负面结果的理论确认**——degeneracy 下 MV gain 在结构上不可能，这比仅仅展示实验数据中 gain=0 要强得多。论文在 Section 6.3 已将其定位为 "screening test"（p44, Appendix ah Q5："Proposition 2(c) reflects its role as a screening test, not a tight estimate"）。要求收紧 bound 本身是合理的学术建议，但当前定位为 necessary condition 已经足够——这不是 bound tightness 问题，而是 bound 的**功能定位**问题。

**建议降级为 Minor**：可在 Proposition 2(c) 后加一句明确 "this is a necessary condition, not a sufficient one" 即可。

---

**[AGREE] R1-W2: 3-seed 重复的局限性**

3 个 seed 的 cross-seed 变异分析确实只有 3 个数据点，这限制了对训练随机性影响的可靠估计。Table 40（p32）报告了 cross-seed 标准差，但样本量太小。论文的 bootstrap CI（Table 12, p16）部分缓解了这一问题（对 signal correlation 的 CI 基于 instance-level resampling），但 R1 指出 Table 2/4 的选择结果同样受限于 3 seed 是正确的。

不过我认为 3-seed 在 NER fine-tuning 领域是常见做法（每次训练需要数小时 GPU 时间），要求增加 seed 数量的 cost-benefit 不佳。**在主文为 Table 2/4 加注 3-seed 局限即可**。

---

**[AGREE] R1-W3: Entity construction 增益边际且仅限单一数据集**

Table 65（p41）的数据清楚表明：entity construction 仅在 Few-NERD 上有正增益（+1.0 pp conditional），ScieERC −0.12 pp，CoNLL −0.5 pp。Figure 1 中的 "+1.4 pp" 确实是单个配置的结果，不是聚合数据。

更进一步，Table 69（p43）的 cost-benefit 分析显示 "SC + LP selection" 在多个数据集上是 positive 的，但 entity construction 的独立贡献仅在 Few-NERD 上 positive（+0.3 pp），其他数据集 neutral 或 negative。

**abstract 和 Figure 1 确实过度突出了 entity construction 的贡献**，建议降低展示权重。

---

**[AGREE] R1-W4: Abstract 超过 200 词限制**

从 PDF 排版判断，abstract 从 "Time-test compute scaling..." 到 "...4B–72B ablations, and exploratory extensions to RE and SQL parsing (87.2% degeneracy)" 跨越左栏大部分和右栏上半部分。按照每行约 10-12 词、约 30+ 行估算，约 280-350 词，**显著超过 EMNLP 2026 的 200 词限制**。这是硬性格式违规，必须修复。

---

### Minor Issues

**[AGREE] R1-M1: Figure 2 视觉可读性**
Figure 2（p5）确实标记点小、线条细。在黑白打印下 6 条线+标记的区分度不足。建议增大标记尺寸或改用子图。

**[AGREE] R1-M2: MBR 缩写首次展开位置**
MBR (Minimum Bayes Risk) 首次出现在 abstract（"MBR-optimal"隐含使用）但未展开全称，直到 Section 6.1 才解释。应在首次使用时展开。

**[REBUT] R1-M3: 主结果仅用 N=8**
论文在 Figure 3（p6）展示了 N=1 到 N=64 的 oracle F1 scaling curve，Figure 5（p7）展示了 MV ΔF1 vs. N 的 scaling，Figure 2（p5）覆盖 N=4,8,16,32 的 correlation-selection gap。N=8 是主文的 focal point，但 N-scaling 分析在主文已有充分覆盖。Appendix u（p32）进一步提供 N-scaling 的详细分析（Tables 38-41）。R1 的说法"N>8 选择增益未在主文展示"与论文内容不符。

**[AGREE] R1-M4: Table 1 列头可读性**
Table 1 的 "Yao+ 2026" / "Ours" 列头在首次阅读时确实不直观，建议改为更具描述性的标签。

---

### Questions

**[AGREE] R1-Q1: Proposition 1 entity-wise independence 假设敏感性**
这是一个合理的理论问题。Proposition 1 假设 entity-wise independence，但相邻实体在 NER 中经常有依赖关系（如 "New York City" 中的嵌套实体）。论文在 p28 Remark 中承认 "Set-level F1 is non-linear and anti-is closed-form threshold rule"，并验证了独立性假设是 approximate 的。但敏感性分析确实缺失。

**[REBUT] R1-Q2: Correlation-selection gap 是否为单一现象**
R1 质疑不同数据集上的 gap 机制不同是否还能算"单一现象"。论文的 contribution 恰恰在于**统一诊断框架**：correlation-selection gap 是一个可观测的现象（high ρ but low selection gain），其底层原因（degeneracy、signal collapse、LP compression）才是 dataset-specific 的。这类似于"发烧"是统一的诊断信号，但病因各异。这是框架的 feature，不是 bug。

**[AGREE] R1-Q3: Free-form decoding ablation 推广性**
Section 8/Appendix s 的 free-form decoding ablation 确实仅在 Few-NERD 和 ScieERC NER 上测试（Table 35-36, p30-31），未覆盖 CoNLL 和 WNUT-17。尽管 Table 36（p31）的 cross-dataset 对比提供了部分证据，完整的 4-dataset ablation 会更有说服力。

**[REBUT] R1-Q4: Trained verifier 特征数量**
5 个特征（agreement count, LP, VC, SJ, FK）已经覆盖了论文研究的所有信号家族。Section 5.2 报告 AUROC=0.923±0.002 OOF，说明这些特征的区分力已经很强。更丰富的特征集可能改善 LODO transfer，但这超出了本文的 scope——论文的 point 是这些信号本身不足以 bridge the gap，不是构建最优 verifier。

**[AGREE] R1-Q5: Table 2 的 post-hoc power analysis**
Table 2 主选择结果的 power analysis 确实重要，特别是在效应量较小（如 ScieERC ΔF1=+0.28 pp）的情况下。Appendix u.1（p32）的 Table 42 提供了 N=32 的 bootstrap significance test，但 Table 2（N=8, T=1.0）的 power analysis 缺失。这会影响对"选择是否真正有效"这一核心声称的可信度。

---

### Missing References

**[AGREE] 代码生成中的 self-consistency（结构化输出对比）**
合理建议。Chen et al. (2023) "Self-consistency improves chain of thought reasoning in language models" 等代码生成 SC 工作与本文的结构化输出设置有直接可比性。

**[REBUT] LLM 校准文献（Kadavath et al. 2022 等）**
论文在 Section 2 Related Work 已引用 calibration 相关工作（Tian et al. 2023 "Just ask for calibration"；Xiong et al. 2024 "Uncertainty quantification"），且 Appendix c（p13）专门讨论了 calibration analysis，包括 ECE 评估。Kadavath et al. 2022 是 pre-training calibration 工作，与本文的 fine-tuned NER 设置关联度有限。

**[REBUT] Parsing/graph generation 的 MBR 文献**
论文在 Section 6.1 和 References 中已引用 MBR 核心文献（Eikema and Aziz 2022; Kumar and Byrne 2004），且 Appendix e.2 讨论了 MBR 与 consensus-proximity selection 的等价性。Parsing-specific MBR 文献（如 Smith and Eisner 2006）与 NER 的 set-overlap 设置差异较大，引用价值有限。

---

### 总体评估

R1 的 3.5 (Borderline Conference) 评分合理但偏保守。我的独立评估：

- **N1 应降级为 Should-Fix**：诊断框架的层次关系已隐式存在（Figure 1 + Appendix ae），显式化是 editorial 改进
- **N2 是唯一真正的 critical issue**：模型覆盖面确实限制了普适性声称，但可通过收紧 title/abstract 表述解决，不需要新实验
- **W3 和 W4 是最需要修复的 Should-Fix**：abstract 超字数是硬性违规；entity construction 过度展示影响论文的 intellectual honesty

综合来看，这篇论文的统计严谨性（57 项检验 + Holm-Bonferroni 校正）、correlation-selection gap 的原创性贡献、以及极高的可复现性使其在方法论上达到了会议接收的标准。主要弱点在于 scope 限制和 presentation 问题，而非根本性的方法论缺陷。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4826 · 2026-05-24T23:16:35.682059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 4827 · 2026-05-24T23:16:36.184512+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	\usepackage{titlesec}
26	
27	\titlespacing*{\section}{0pt}{2.2ex plus 0.6ex minus 0.3ex}{1.3ex plus 0.2ex}
28	\titlespacing*{\subsection}{0pt}{1.8ex plus 0.5ex minus 0.2ex}{0.8ex plus 0.2ex}
29	\titlespacing*{\paragraph}{0pt}{1.0ex plus 0.3ex minus 0.1ex}{1em}
30	
31	\renewcommand{\topfraction}{0.9}
32	\renewcommand{\bottomfraction}{0.85}
33	\renewcommand{\dbltopfraction}{0.9}
34	\renewcommand{\textfraction}{0.07}
35	\renewcommand{\floatpagefraction}{0.85}
36	\renewcommand{\dblfloatpagefraction}{0.85}
37	\setcounter{topnumber}{3}
38	\setcounter{dbltopnumber}{2}
39	\setcounter{totalnumber}{5}
40	
41	\setlength{\parskip}{0pt plus 0.3pt}
42	\addtolength{\textfloatsep}{-4pt}
43	\addtolength{\floatsep}{-2pt}
44	\addtolength{\dbltextfloatsep}{-4pt}
45	\addtolength{\dblfloatsep}{-2pt}
46	\addtolength{\abovecaptionskip}{-2pt}
47	
48	\graphicspath{{figures/}}
49	
50	\title{When Self-Consistency Fails for NER:\\ Degeneracy, Signal Collapse, and the Correlation-Selection Gap}
51	
52	\author{Anonymous}
53	
54	\begin{document}
55	\maketitle
56	
57	\input{sections/abstract}
58	\input{sections/introduction}
59	\input{sections/background}
60	\input{sections/diagnostic}
61	\input{sections/single_signal}
62	\input{sections/adaptive}
63	\input{sections/theory}
64	\input{sections/experiments_main}
65	
66	\enlargethispage{3\baselineskip}
67	\section{Discussion and Conclusion}\lab
…[truncated 673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 4828 · 2026-05-24T23:16:36.335469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "195",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "195",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 4829 · 2026-05-24T23:16:36.386234+00:00_

195	  summary: "模型多样性有限"
196	  category: experiment
197	  severity: warning
198	  status: resolved
199	  first_raised_round: 43
200	  last_seen_round: 43
201	  action_items:
202	    - round: 43
203	      action: "Limitations 已包含 frontier model caveat"
204	      assigned_to: paper_agent
205	      status: done
206	  resolution: "Limitations 声明 frontier degeneracy 5.5-74% 泛化限制。Reviewer 验证 PASS。"
207	  resolution_round: 43
208	
209	- id: R43-W6
210	  summary: "'Primarily diagnostic' 定位削弱实用价值"
211	  category: framing
212	  severity: warning
213	  status: resolved
214	  first_raised_round: 43
215	  last_seen_round: 43
216	  action_items:
217	    - round: 43
218	      action: "§7.5 加 practitioner workflow (pilot N=8)"
219	      assigned_to: paper_agent
220	      status: done
221	  resolution: "Practitioner diagnostic workflow 已加。Reviewer 验证 PASS。"
222	  resolution_round: 43
223	
224	- id: R43-W7
225	  summary: "Entity-level decomposition 增量贡献需更强论证"
226	  category: framing
227	  severity: warning
228	  status: resolved
229	  first_raised_round: 41
230	  last_seen_round: 43
231	  action_items:
232	    - round: 43
233	      action: "Table 1 + concurrent work 对比强化"
234	      assigned_to: paper_agent
235	      status: done
236	  resolution: "Table 1 六维度对比 + §2 四维对比已充分。Reviewer 验证 PASS。"
237	  resolution_round: 43
238	
239	- id: R43-W8
240	  summary: "缺失引用: Reflexion, Malinin & Gales (2021)"
241	  category: writing
242	  severity: warning
243	  status: resolved
244	  first_raised_round: 43
245	  last_seen_round: 43
246	  action_items:
247	    - round: 43
248	      action: "§2 添加两篇引用"
249	      assigned_to: paper_agent
250	      status: done
251	  resolution: "Malinin & Gales (2021) + Shinn (2023) Reflexion 已加入 §2。Reviewer 验证 PASS。"
252	  resolution_round: 43
253	
254	# ===== ROUND 43 MINOR =====
255	- id: R43-M1
256	  summary: "Footnote 1 (RE F1 confound) 建议提升到正文"
257	  category: writing
258	  severity: info
259	  status: open
260	  first_raised_round: 43
261	  last_seen_round: 
…[truncated 880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4830 · 2026-05-24T23:16:44.166589+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\begin\\{abstract\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\begin\\{abstract\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 4831 · 2026-05-24T23:16:44.217173+00:00_

1:\begin{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4832 · 2026-05-24T23:16:47.680390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 4833 · 2026-05-24T23:16:47.731084+00:00_

1	\begin{abstract}
2	Test-time compute scaling (repeated sampling with self-consistency or best-of-$N$) yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary analysis, with preliminary cross-task pilots (RE, SQL).
4	Quality estimation signals predict output quality (area under the ROC curve [AUROC] up to $0.82$), yet instance-level selection yields no detectable gains (${<}1$\,pp; confidence interval crosses zero), revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions, \textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse, that are jointly associated with scaling returns; cross-task exploration confirms task-specific failure modes.
6	Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\text{adj}}{=}0.055$, suggestive; per-family $p_{\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.
7	The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4834 · 2026-05-24T23:17:10.079030+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex | sed 's/\\\\textbf{//g; s/\\\\textit{//g; s/\\\\begin{abstract}//g; s/\\\\end{abstract}//g; s/\\\\,/ /g; s/\\$[^$]*\\$/ NUM /g; s/[{}]//g; s/\\\\[a-zA-Z]*//g' | wc -w",
  "description": "Count words in abstract tex file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex | sed 's/\\\\textbf{//g; s/\\\\textit{//g; s/\\\\begin{abstract}//g; s/\\\\end{abstract}//g; s/\\\\,/ /g; s/\\$[^$]*\\$/ NUM /g; s/[{}]//g; s/\\\\[a-zA-Z]*//g' | wc -w",
    "description": "Count words in abstract tex file"
  }
}
```

</details>

---


### Tool result

_source line 4835 · 2026-05-24T23:17:10.281487+00:00_

172

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 4836 · 2026-05-24T23:17:16.455249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "290",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "290",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 4837 · 2026-05-24T23:17:16.505920+00:00_

290	    - round: 43
291	      reviewers: [2]
292	      note: "Figure 1 caption 免责容易被忽略。"
293	
294	- id: R43-M4
295	  summary: "§6.3 符号首次引入时定义不够直观"
296	  category: writing
297	  severity: info
298	  status: open
299	  first_raised_round: 43
300	  last_seen_round: 43
301	  mentions:
302	    - round: 43
303	      reviewers: [2]
304	      note: "需要反复回看 §3。"
305	
306	# ===== EARLIER RESOLVED (保留历史，精简) =====
307	- id: R41-N1
308	  summary: "分解 bound 仅恢复 3-12%"
309	  category: method
310	  severity: critical
311	  status: resolved
312	  first_raised_round: 38
313	  last_seen_round: 42
314	  resolution: "§6.3 重定位。R43 以新角度重提并解决（R43-N2）。"
315	  resolution_round: 43
316	
317	- id: R41-N2
318	  summary: "多重比较校正方案选择"
319	  category: method
320	  severity: critical
321	  status: resolved
322	  first_raised_round: 34
323	  last_seen_round: 42
324	  resolution: "§7.5 修改。R43 以新角度重提并解决（R43-N4）。"
325	  resolution_round: 43
326	
327	- id: R41-N3
328	  summary: "Probes 模型不一致"
329	  category: experiment
330	  severity: critical
331	  status: resolved
332	  first_raised_round: 36
333	  last_seen_round: 42
334	  resolution: "ESJ cross-validation on Qwen3-8B 确认。"
335	  resolution_round: 42
336	
337	- id: R41-N4
338	  summary: "Novelty 与 Landesberg et al. 重叠"
339	  category: framing
340	  severity: critical
341	  status: resolved
342	  first_raised_round: 39
343	  last_seen_round: 42
344	  resolution: "§2 四维度对比。"
345	  resolution_round: 42
346	
347	- id: R41-N5
348	  summary: "Few-NERD epoch confound"
349	  category: experiment
350	  severity: critical
351	  status: resolved
352	  first_raised_round: 38
353	  last_seen_round: 42
354	  resolution: "Abstract 条件限定。R43 以 baseline confound 角度重提并解决（R43-W1）。"
355	  resolution_round: 43
356	
357	- id: R41-W1
358	  summary: "Diagnostic vs prescriptive 不一致"
359	  category: framing
360	  severity: warning
361	  status: resolved
362	  first_raised_round: 40
363	  last_seen_round: 42
364	  resolution: "定位统一为 diagnostic primary + exploratory construction。
…[truncated 107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4838 · 2026-05-24T23:18:07.568322+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "status: open",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "output_mode": "content",
  "-B": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "status: open",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "output_mode": "content",
    "-B": "3"
  }
}
```

</details>

---


### Tool result

_source line 4839 · 2026-05-24T23:18:07.669205+00:00_

256-  summary: "Footnote 1 (RE F1 confound) 建议提升到正文"
257-  category: writing
258-  severity: info
259:  status: open
--
283-  summary: "§3 应在首段明确提及 diagnostic sequence 而非 causal chain"
284-  category: writing
285-  severity: info
286:  status: open
--
295-  summary: "§6.3 符号首次引入时定义不够直观"
296-  category: writing
297-  severity: info
298:  status: open

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4840 · 2026-05-24T23:18:16.014777+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4841 · 2026-05-24T23:18:16.065518+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4842 · 2026-05-24T23:19:35.328330+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== ROUND 45 MUST-FIX (CONSENSUS) =====\n- id: R45-N1\n  summary: \"模型覆盖面过窄（仅 2 个 ~8B 模型族），标题/摘要普适性声称超出证据范围\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 43\n  last_seen_round: 45\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-W5 作为 warning 提出，已通过 Limitations 声明部分解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1 升级为 Must-Fix (N2)。R2 AGREE。Table 43 显示 degeneracy 是 model-family-dependent。\"\n  action_items:\n    - round: 45\n      action: \"收紧 title/abstract 的普适性表述，显式限定为 7-14B fine-tuned models；或增加 ≥1 个模型家族\"\n      assigned_to: paper_agent+director\n      status: open\n\n# ===== ROUND 45 SHOULD-FIX =====\n- id: R45-W1\n  summary: \"Entity construction 统计边际（global Holm p_adj=0.055）且在 abstract/Figure 1 中展示权重过高\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 45\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N4 prescriptive→exploratory 重定位已解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W3 提出全局 Holm 不显著。R1 strongly AGREE。Figure 1 '+1.4pp' 是单个配置非聚合。\"\n  action_items:\n    - round: 45\n      action: \"降低 entity construction 在 abstract/Figure 1 中的突出程度；Figure 1 标注 '+1.4pp' 为单配置结果\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W2\n  summary: \"与 Landesberg (2026) 并行发现的差异化论述不够充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 39\n  last_seen_round: 45\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R41-N4 通过 §2 四维度对比解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W1 重新提出。R1 AGREE。§2 末尾 concurrent work 段过于简短。\"\n  action_items:\n    - round: 45\n      action: \"Introduction 中增加一段明确说明与 Landesberg 的关系，强调增量贡献是诊断框架而非 gap 发现本身\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W3\n  summary: \"Failure mode 四种模式的层次化关系未显式形式化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-N1 (critical)。R2 REBUT 降级为 should-fix——隐式层次已存在(Figure 1 + Appendix ae)。Director 判定 should-fix。\"\n  action_items:\n    - round: 45\n      action: \"Section 3.3 或 4 开头加 1-2 句显式声明四种模式的层次诊断关系（degeneracy → signal collapse → LP compression）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W4\n  summary: \"3-seed 局限性在主文 Table 2/4 结果中未充分注明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 40\n  last_seen_round: 45\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N1 通过 power-aware negative claims 解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-W2。R2 AGREE。cross-seed 变异分析仅 3 个数据点。\"\n  action_items:\n    - round: 45\n      action: \"在 Table 2/4 caption 或正文中显式注明 3-seed 局限性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W5\n  summary: \"Table 1 novelty comparison 维度选择偏向本文\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 45\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N6 精简为 6 维度 + p_adj 标注\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W2 重提。R1 AGREE 但非 must-fix。建议增加本文较弱维度。\"\n  action_items:\n    - round: 45\n      action: \"Table 1 caption/脚注承认维度选择局限，或增加 1-2 个本文较弱维度（Model Scale Range, Task Diversity）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W6\n  summary: \"实践指导（Appendix ah/ae）在主文可见性不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W4 提出缺乏实践指导。R1 REBUT——Appendix ah/ae 有内容但埋得太深。Director 判定：可见性问题非缺失问题。\"\n  action_items:\n    - round: 45\n      action: \"Section 8 增加 'Practical Implications' 段落（3-4 句），将 Appendix ah 核心建议提炼到正文\"\n      assigned_to: paper_agent\n      status: open\n\n# ===== ROUND 45 MINOR =====\n- id: R45-M1\n  summary: \"Figure 2 标记点小、线条细，打印尺寸下难区分\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-M1。R2 AGREE。\"\n\n- id: R45-M2\n  summary: \"MBR 缩写在 abstract/introduction 中未展开全称\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-M2。R2 AGREE。首次完整展开在 Section 6.1。\"\n\n- id: R45-M3\n  summary: \"Table 1 列头 'Yao+ 2026'/'Ours' 首次阅读不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-M4。R2 AGREE。\"\n\n- id: R45-M4\n  summary: \"遗漏引用：Florian et al. (2003) NER 集成学习\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2 提出。R1 AGREE。NER ensemble 是 best-of-N 的自然对照。\"\n\n- id: R45-M5\n  summary: \"遗漏引用：代码生成中的 self-consistency 工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1 提出。R2 AGREE。结构化输出 SC 的直接可比文献。\"\n\n- id: R45-M6\n  summary: \"遗漏引用：diversity-promoting decoding 文献（与 degeneracy 概念相关）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2 提出 Diverse Beam Search。R1 PARTIALLY AGREE。DBS 降低 degeneracy 的概念联系值得提及。\"\n\n# ===== ROUND 43 遗留 OPEN (MINOR) =====\n- id: R43-M1\n  summary: \"Footnote 1 (RE F1 confound) 建议提升到正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M1：RE F1 confound 不应仅在脚注。\"\n\n- id: R43-M3\n  summary: \"§3 应在首段明确提及 diagnostic sequence 而非 causal chain\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"Figure 1 caption 免责容易被忽略。\"\n\n- id: R43-M4\n  summary: \"§6.3 符号首次引入时定义不够直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"需要反复回看 §3。\"\n\n# ===== EARLIER ROUNDS — RESOLVED (精简保留) =====\n- id: R43-N1\n  summary: \"2-3 seeds 统计推断力不足，核心 negative claims 无法区分真无效应和检测力不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 43\n  resolution: \"全文 negative claims 改为 'yields no detectable gains'，加 MDE ~1.5pp/CI 限定。\"\n  resolution_round: 43\n\n- id: R43-N2\n  summary: \"Degeneracy decomposition bound 过松，作为主要贡献名不副实\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 43\n  resolution: \"三阶段重构 (Discover/Diagnose/Construct-exploratory)，bound 不再独立贡献。\"\n  resolution_round: 43\n\n- id: R43-N3\n  summary: \"观察性设计下因果措辞系统性过强\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"全文因果措辞替换为关联/观察性表述。\"\n  resolution_round: 43\n\n- id: R43-N4\n  summary: \"处方性结果全局 Holm 校正不显著（p_adj=0.055），per-family 校正未预注册\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 43\n  resolution: \"全文 prescriptive→exploratory。subsection 'Entity Construction (Exploratory)'。\"\n  resolution_round: 43\n\n- id: R43-N5\n  summary: \"标题 'Why SC Fails for NER' 与正文 conditional success 结论不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 43\n  resolution: \"标题改 'When Self-Consistency Fails for NER'。\"\n  resolution_round: 43\n\n- id: R43-N6\n  summary: \"Table 1 novelty comparison 维度选择有 cherry-picking 嫌疑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"Table 1 精简为 6 维度，Prescriptive 标 'Conditional (p_adj=0.055)'。\"\n  resolution_round: 43\n\n- id: R43-W1\n  summary: \"Few-NERD 3-epoch vs 5-epoch 混淆未充分解决\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 43\n  resolution: \"Greedy 0.748 vs 0.798 说明已加。\"\n  resolution_round: 43\n\n- id: R43-W2\n  summary: \"RE/SQL 扩展过于初步\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 43\n  resolution: \"Abstract 'preliminary cross-task pilots (RE, SQL)'。\"\n  resolution_round: 43\n\n- id: R43-W3\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 43\n  resolution: \"Abstract 精简为 6 个关键数字。\"\n  resolution_round: 43\n\n- id: R43-W4\n  summary: \"Entity construction 与 MBR 理论联系偏弱\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"Exploratory 定位自然弱化了 MBR 理论依赖。\"\n  resolution_round: 43\n\n- id: R43-W5\n  summary: \"模型多样性有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"Limitations 声明 frontier degeneracy 5.5-74% 泛化限制。R45 以更强角度重提（R45-N1）。\"\n  resolution_round: 43\n\n- id: R43-M2\n  summary: \"Mechanistic evidence 在 Appendix 却作为正文贡献点列出\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"三阶段结构不再将 mechanistic evidence 列为独立贡献。\"\n  resolution_round: 43\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== ROUND 45 MUST-FIX (CONSENSUS) =====\n- id: R45-N1\n  summary: \"模型覆盖面过窄（仅 2 个 ~8B 模型族），标题/摘要普适性声称超出证据范围\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 43\n  last_seen_round: 45\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-W5 作为 warning 提出，已通过 Limitations 声明部分解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1 升级为 Must-Fix (N2)。R2 AGREE。Table 43 显示 degeneracy 是 model-family-dependent。\"\n  action_items:\n    - round: 45\n      action: \"收紧 title/abstract 的普适性表述，显式限定为 7-14B fine-tuned models；或增加 ≥1 个模型家族\"\n      assigned_to: paper_agent+director\n      status: open\n\n# ===== ROUND 45 SHOULD-FIX =====\n- id: R45-W1\n  summary: \"Entity construction 统计边际（global Holm p_adj=0.055）且在 abstract/Figure 1 中展示权重过高\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 45\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N4 prescriptive→exploratory 重定位已解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W3 提出全局 Holm 不显著。R1 strongly AGREE。Figure 1 '+1.4pp' 是单个配置非聚合。\"\n  action_items:\n    - round: 45\n      action: \"降低 entity construction 在 abstract/Figure 1 中的突出程度；Figure 1 标注 '+1.4pp' 为单配置结果\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W2\n  summary: \"与 Landesberg (2026) 并行发现的差异化论述不够充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 39\n  last_seen_round: 45\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R41-N4 通过 §2 四维度对比解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W1 重新提出。R1 AGREE。§2 末尾 concurrent work 段过于简短。\"\n  action_items:\n    - round: 45\n      action: \"Introduction 中增加一段明确说明与 Landesberg 的关系，强调增量贡献是诊断框架而非 gap 发现本身\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W3\n  summary: \"Failure mode 四种模式的层次化关系未显式形式化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-N1 (critical)。R2 REBUT 降级为 should-fix——隐式层次已存在(Figure 1 + Appendix ae)。Director 判定 should-fix。\"\n  action_items:\n    - round: 45\n      action: \"Section 3.3 或 4 开头加 1-2 句显式声明四种模式的层次诊断关系（degeneracy → signal collapse → LP compression）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W4\n  summary: \"3-seed 局限性在主文 Table 2/4 结果中未充分注明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 40\n  last_seen_round: 45\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N1 通过 power-aware negative claims 解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-W2。R2 AGREE。cross-seed 变异分析仅 3 个数据点。\"\n  action_items:\n    - round: 45\n      action: \"在 Table 2/4 caption 或正文中显式注明 3-seed 局限性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W5\n  summary: \"Table 1 novelty comparison 维度选择偏向本文\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 43\n  last_seen_round: 45\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N6 精简为 6 维度 + p_adj 标注\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W2 重提。R1 AGREE 但非 must-fix。建议增加本文较弱维度。\"\n  action_items:\n    - round: 45\n      action: \"Table 1 caption/脚注承认维度选择局限，或增加 1-2 个本文较弱维度（Model Scale Range, Task Diversity）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W6\n  summary: \"实践指导（Appendix ah/ae）在主文可见性不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W4 提出缺乏实践指导。R1 REBUT——Appendix ah/ae 有内容但埋得太深。Director 判定：可见性问题非缺失问题。\"\n  action_items:\n    - round: 45\n      action: \"Section 8 增加 'Practical Implications' 段落（3-4 句），将 Appendix ah 核心建议提炼到正文\"\n      assigned_to: paper_agent\n      status: open\n\n# ===== ROUND 45 MINOR =====\n- id: R45-M1\n  summary: \"Figure 2 标记点小、线条细，打印尺寸下难区分\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-M1。R2 AGREE。\"\n\n- id: R45-M2\n  summary: \"MBR 缩写在 abstract/introduction 中未展开全称\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-M2。R2 AGREE。首次完整展开在 Section 6.1。\"\n\n- id: R45-M3\n  summary: \"Table 1 列头 'Yao+ 2026'/'Ours' 首次阅读不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-M4。R2 AGREE。\"\n\n- id: R45-M4\n  summary: \"遗漏引用：Florian et al. (2003) NER 集成学习\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2 提出。R1 AGREE。NER ensemble 是 best-of-N 的自然对照。\"\n\n- id: R45-M5\n  summary: \"遗漏引用：代码生成中的 self-consistency 工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1 提出。R2 AGREE。结构化输出 SC 的直接可比文献。\"\n\n- id: R45-M6\n  summary: \"遗漏引用：diversity-promoting decoding 文献（与 degeneracy 概念相关）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2 提出 Diverse Beam Search。R1 PARTIALLY AGREE。DBS 降低 degeneracy 的概念联系值得提及。\"\n\n# ===== ROUND 43 遗留 OPEN (MINOR) =====\n- id: R43-M1\n  summary: \"Footnote 1 (RE F1 confound) 建议提升到正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R2-M1：RE F1 confound 不应仅在脚注。\"\n\n- id: R43-M3\n  summary: \"§3 应在首段明确提及 diagnostic sequence 而非 causal chain\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"Figure 1 caption 免责容易被忽略。\"\n\n- id: R43-M4\n  summary: \"§6.3 符号首次引入时定义不够直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"需要反复回看 §3。\"\n\n# ===== EARLIER ROUNDS — RESOLVED (精简保留) =====\n- id: R43-N1\n  summary: \"2-3 seeds 统计推断力不足，核心 negative claims 无法区分真无效应和检测力不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 43\n  resolution: \"全文 negative claims 改为 'yields no detectable gains'，加 MDE ~1.5pp/CI 限定。\"\n  resolution_round: 43\n\n- id: R43-N2\n  summary: \"Degeneracy decomposition bound 过松，作为主要贡献名不副实\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 43\n  resolution: \"三阶段重构 (Discover/Diagnose/Construct-exploratory)，bound 不再独立贡献。\"\n  resolution_round: 43\n\n- id: R43-N3\n  summary: \"观察性设计下因果措辞系统性过强\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"全文因果措辞替换为关联/观察性表述。\"\n  resolution_round: 43\n\n- id: R43-N4\n  summary: \"处方性结果全局 Holm 校正不显著（p_adj=0.055），per-family 校正未预注册\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 43\n  resolution: \"全文 prescriptive→exploratory。subsection 'Entity Construction (Exploratory)'。\"\n  resolution_round: 43\n\n- id: R43-N5\n  summary: \"标题 'Why SC Fails for NER' 与正文 conditional success 结论不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 43\n  resolution: \"标题改 'When Self-Consistency Fails for NER'。\"\n  resolution_round: 43\n\n- id: R43-N6\n  summary: \"Table 1 novelty comparison 维度选择有 cherry-picking 嫌疑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"Table 1 精简为 6 维度，Prescriptive 标 'Conditional (p_adj=0.055)'。\"\n  resolution_round: 43\n\n- id: R43-W1\n  summary: \"Few-NERD 3-epoch vs 5-epoch 混淆未充分解决\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 43\n  resolution: \"Greedy 0.748 vs 0.798 说明已加。\"\n  resolution_round: 43\n\n- id: R43-W2\n  summary: \"RE/SQL 扩展过于初步\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 43\n  resolution: \"Abstract 'preliminary cross-task pilots (RE, SQL)'。\"\n  resolution_round: 43\n\n- id: R43-W3\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 43\n  resolution: \"Abstract 精简为 6 个关键数字。\"\n  resolution_round: 43\n\n- id: R43-W4\n  summary: \"Entity construction 与 MBR 理论联系偏弱\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"Exploratory 定位自然弱化了 MBR 理论依赖。\"\n  resolution_round: 43\n\n- id: R43-W5\n  summary: \"模型多样性有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"Limitations 声明 frontier degeneracy 5.5-74% 泛化限制。R45 以更强角度重提（R45-N1）。\"\n  resolution_round: 43\n\n- id: R43-M2\n  summary: \"Mechanistic evidence 在 Appendix 却作为正文贡献点列出\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"三阶段结构不再将 mechanistic evidence 列为独立贡献。\"\n  resolution_round: 43\n"
  }
}
```

</details>

---


### Tool result

_source line 4843 · 2026-05-24T23:19:35.479509+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 9313}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 4844 · 2026-05-24T23:21:56.511590+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "## Round 45 审稿报告\n\n**论文**: When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh（全新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验评估; R2: 新颖性/相关工作/完整性）\n**轮次**: 1 轮（交叉回应后达成共识，无需 Round 2）\n\n---\n\n### Summary\n\n论文系统研究 test-time compute scaling（self-consistency, best-of-N）在 NER 上的表现。核心发现是\"correlation-selection gap\"：质量估计信号能预测输出质量（AUROC 达 0.82），但实例级选择无法带来可检测的 F1 增益（<1pp，CI 跨零）。诊断框架识别 degeneracy 和 signal alignment collapse 两个共现条件。Entity-level construction 作为探索性贡献在 Few-NERD 3-epoch 训练下获 +1.40pp 条件性增益（全局 Holm p_adj=0.055，suggestive）。实验覆盖 4 个 NER 数据集、2 个微调模型族（Qwen3-8B, LLaMA-3.1-8B）、57 项统计检验，附 46 页 appendix。\n\n---\n\n### Strengths\n\n**S1. Correlation-selection gap 概念具有原创性和跨任务价值。** 群体水平高相关性无法转化为实例级选择增益——这一现象此前未被系统识别和诊断。对任何使用 confidence-based reranking 的结构化预测任务都有警示意义。[R1-S2, R2-S1 共识]\n\n**S2. 统计方法论在 NLP 实证分析中属于标杆水准。** 57 项检验的 Holm-Bonferroni 校正、bootstrap CI、TOST 等价性检验、post-hoc power analysis、Cohen's d 效应量、置换检验。同时报告 global 和 per-family 校正，诚实标注 p_adj=0.055 的边界状态。[R1-S1, R2-S4 共识]\n\n**S3. 分析覆盖面极其全面。** 46 页 appendix 包含 N-scaling、温度敏感性、cross-dataset transfer、free-form decoding ablation、epoch convergence、per-entity-type analysis、calibration analysis 等。几乎所有潜在混淆因素均被系统排查。[R1-S3, R2-S2 共识]\n\n**S4. 声称限定诚实恰当。** Entity construction 始终标记为 \"exploratory\"，negative claims 使用 \"no detectable gains\" + CI 限定。Limitations 涵盖英语限定、模型规模限定、统计功效限定。[R1-S5, R2 共识]\n\n**S5. 可复现性高。** 训练配置完整（Table 22），超参数详尽，承诺公开代码/checkpoint/seed 级结果。[R1-S6]\n\n**S6. 形式化贡献有价值。** Proposition 1 将 entity construction 形式化为 MBR 解码，Proposition 2 的 degeneracy decomposition 提供可验证 bound（16 种配置全部成立）。[R1-S4]\n\n---\n\n### Weaknesses\n\n#### Must-Fix（两位 Reviewer 共识）\n\n**[MUST-FIX] W1. 模型覆盖面过窄，普适性声称超出证据范围 [R45-N1]**\n\n主实验仅用 2 个模型族（Qwen3-8B, LLaMA-3.1-8B），均为 ~8B 参数微调。72B zero-shot probe 和 few-shot 实验被论文自身标注为 exploratory。关键证据：Table 43 显示 degeneracy 是 model-family-dependent（Qwen2.5 在 Few-NERD 上 31.7%–46.2%，显著高于 Qwen3 的 13.0%），Table 44 跨家族（Claude, Gemini, GPT, DeepSeek）差异巨大。标题\"When Self-Consistency Fails for NER\"暗示一般性结论，但证据仅支持\"在 7-14B 微调模型 + 4 个英文数据集上\"。\n\n- R1 Must-Fix (N2), R2 AGREE\n- **建议**：收紧 title/abstract 的普适性表述，显式限定为测试模型区间（\"7–14B fine-tuned open-weight models\"）；或增加 ≥1 个模型家族的完整微调实验。R2 倾向前者（camera-ready 阶段增加新实验不现实），Director 同意。\n\n#### Should-Fix（影响评分）\n\n**[SHOULD-FIX] W2. Entity construction 统计边际且在 abstract/Figure 1 中展示权重过高 [R45-W1]**\n\n全局 Holm-Bonferroni 校正下 p_adj=0.055，不满足 α=0.05。Per-family p_adj=0.006 依赖未预注册的 family 划分，构成研究者自由度。Entity construction 仅在 Few-NERD 上有正增益（+1.0pp conditional），ScieERC −0.12pp，CoNLL −0.5pp。Figure 1 中 \"+1.4pp\" 是单个配置结果而非聚合数据。一个 p_adj=0.055 的结果不应作为论文三大贡献之一呈现。\n\n- R1 AGREE (W3), R2-W3 提出, 双方共识\n- **建议**：(a) 降低 entity construction 在 abstract/Figure 1 中的突出程度，与 \"exploratory\" 定位匹配；(b) Figure 1 标注 \"+1.4pp\" 为单个配置而非聚合效果；(c) 主文报告全局 Holm p 值并标注 \"marginally significant under global correction\"\n\n**[SHOULD-FIX] W3. 与 Landesberg (2026) 并行发现的差异化论述不够充分 [R45-W2]**\n\nCorrelation-selection gap 存在并行发现。当前 §2 末尾的 \"Concurrent work\" 段过于简短，不足以让读者理解本文的增量贡献（诊断框架 + 形式化结果 vs. gap 发现本身）。\n\n- R2-W1 提出, R1 AGREE\n- R1 补充：论文的核心增量是 *diagnosing* the gap（四种 failure mode、Proposition 1-2、多信号/多数据集系统比较），而非 *discovering* the gap。需在 Introduction 中显式分离这两个层面。\n- **建议**：Introduction 增加一段明确说明与 Landesberg 的关系，强调增量贡献是诊断框架，而非 gap 本身的发现\n\n**[SHOULD-FIX] W4. Failure mode 四种模式的层次化关系未显式形式化 [R45-W3]**\n\nDegeneracy 在逻辑上蕴含 signal collapse（若所有输出相同，信号必然相同），但定义层面未显式建立蕴含关系。四种模式未覆盖 actively misleading signals（Table 4 中 FK 在 CoNLL 上 ρ=−0.05）。\n\n- R1 Must-Fix (N1), R2 REBUT（降为 Should-Fix——隐式层次已存在于 Figure 1 + §4 + Appendix ae 诊断协议）\n- **Director 判定**：降为 Should-Fix。R2 指出隐式层次已存在且 ρ=−0.05 统计上与零无异。但 R1 关于显式形式化的建议有价值——从业者操作化使用需要明确层次。\n- **建议**：Section 3.3 或 4 开头加 1-2 句显式声明顺序诊断逻辑\n\n**[SHOULD-FIX] W5. 3-seed 局限性在主文 Table 2/4 中未充分注明 [R45-W4]**\n\n训练 seed 仅 3 个，cross-seed 变异分析仅 3 个数据点。此限制同样适用于主选择结果（Table 2, Table 4），但 3-seed 局限仅在 Limitations 部分提及。\n\n- R1-W2 提出, R2 AGREE（3-seed 在 NER fine-tuning 中是常见做法，成本约束合理）\n- **建议**：在 Table 2/4 caption 或正文中显式注明 3-seed 局限性\n\n**[SHOULD-FIX] W6. Table 1 novelty comparison 维度选择偏向本文 [R45-W5]**\n\n6 个维度中 \"Diagnostics\" 和 \"Prescriptive\" 恰好是本文强项，缺少 Landesberg 等工作可能更强的维度（Model Scale Range, Task Diversity）。\n\n- R2-W2 提出, R1 AGREE 但非 must-fix\n- **建议**：caption/脚注承认维度选择局限，或增加 1-2 个本文较弱维度\n\n**[SHOULD-FIX] W7. 实践指导在主文可见性不足 [R45-W6]**\n\nAppendix ah（10 条 Q&A 式建议）和 Appendix ae（cost-benefit 分析）包含实质内容，但主文 Section 8 缺乏 actionable summary。\n\n- R2-W4 提出, R1 REBUT（内容存在但埋得太深）\n- **Director 判定**：核心问题是可见性而非缺失。Appendix 内容扎实，但审稿人和读者首先看主文。\n- **建议**：Section 8 增加 \"Practical Implications\" 段落（3-4 句），提炼 Appendix ah 核心建议\n\n#### Minor Issues\n\n- **M1**: Figure 2 标记点小、线条细，打印尺寸下难以区分 [R1-M1, R2 AGREE]\n- **M2**: MBR 在 abstract/introduction 中使用但未展开全称，首次完整展开在 Section 6.1 [R1-M2, R2 AGREE]\n- **M3**: Table 1 列头 \"Yao+ 2026\"/\"Ours\" 首次阅读不直观，建议更具描述性标签 [R1-M4, R2 AGREE]\n\n---\n\n### Questions\n\n**Q1** [R1-Q1]: Proposition 1 entity-wise independence 假设的敏感性如何？相邻实体存在依赖关系（如嵌套实体），最优 θ 可能受 entity correlation 影响。[R2 AGREE]\n\n**Q2** [R1-Q2]: Correlation-selection gap 在不同数据集上机制不同（ScieERC/CoNLL 以 degeneracy 为主，Few-NERD 以 signal collapse 为主），是否真是单一现象还是多种不同失效模式的共同症状？[R2 REBUT——统一框架是 feature 不是 bug，类似\"发烧\"是统一诊断信号但病因各异]\n\n**Q3** [R1-Q3]: Free-form decoding ablation 仅在 Few-NERD/ScieERC 上测试，\"LP compression is model-intrinsic\" 结论能否推广到 CoNLL/WNUT？[R2 AGREE——完整 4-dataset ablation 更有说服力]\n\n**Q4** [R1-Q5]: Table 2 主选择结果的 post-hoc power analysis 缺失。给定 test instances 数量、3 seeds、α=0.05，minimum detectable effect size 是多少？[R2 AGREE]\n\n---\n\n### Missing References\n\n1. **Florian et al. (2003)** NER 集成学习——best-of-N selection 的自然历史对照（model-level diversity vs. sample-level diversity）[R2 提出, R1 AGREE]\n2. **代码生成中的 self-consistency**——结构化输出的 SC 对比文献，可为 correlation-selection gap 的任务特异性提供上下文 [R1 提出, R2 AGREE]\n3. **Diversity-promoting decoding 文献**（如 Diverse Beam Search）——与 degeneracy 概念有概念联系，DBS 本质上是通过解码策略降低 degeneracy [R2 提出, R1 PARTIALLY AGREE]\n\n---\n\n### External Review\n\n外部审稿：未请求。\n\n---\n\n### Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（18 info, 0 critical, 0 warning）\n\n**主要发现**：\n- **排版质量**: 双栏格式符合 ACL 模板，全文无 margin 溢出、无 LaTeX 错误、无未解析引用\n- **视觉密度**: 8 页主文含 6 figures + 5 tables = 11 个 display items（~1.4/页），密度优秀，text-figure-table 交替节奏良好\n- **Figure 1**: 全宽 overview，三阶段 pipeline 用颜色区分清晰，caption 自包含，信息密度高——优秀的视觉锚点\n- **首页**: 无视觉锚点（纯文本 Abstract + Introduction），第一个 display item 在 page 2。建议考虑前移一个简图或核心数字到 page 1\n- **图表一致性**: 蓝/橙/绿/红在 Figures 2-6 中语义统一，色盲友好\n- **小尺寸图表**: Figure 4 两个 subfigure、Figure 5、Figure 6 偏小，打印后可读性接近下限\n- **表格**: 全部使用 booktabs 风格，最优结果加粗，小数精度一致\n- **Limitations**: 简洁（~1/3 页，3 个要点），符合 EMNLP 规范\n- **Appendix**: Page 14 较密集（3 个 display items 挤一页），Figure 9 subfigure 字号偏小\n\n---\n\n### Overall Assessment\n\n**Overall: 3.0 / 5 (Findings)**\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Overall | 3.5 | 3.0 | **3.0** |\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Confidence | 4.0 | 4.0 | 4.0 |\n\n**Director 评分理由**：\n\n论文的核心优势——correlation-selection gap 概念的原创性、标杆级统计方法论、极其全面的分析覆盖——使其在方法论严谨性上达到了很高水准。然而三个结构性弱点限制了其 impact：\n\n1. **模型覆盖面过窄**（唯一 Must-Fix 共识）：仅 2 个 ~8B 模型族，且 Table 43 明确显示 degeneracy 是 model-family-dependent，直接削弱普适性声称。\n2. **唯一的建设性贡献统计边际**：Entity construction 全局 Holm p_adj=0.055，仅在 1/3 数据集上有正增益，不足以支撑三大贡献之一的定位。\n3. **并行发现降低新颖性溢价**：Landesberg (2026) 的 concurrent discovery 使 gap 本身不再是独占性发现，论文需要更强地论证诊断框架的增量价值。\n\n论文以负面结果为主（\"SC 对 NER 无效\"），建设性部分弱。负面结果论文要达到 Conference 水准需要更广的适用范围或更强的机制洞见来补偿 impact 不足。当前的 2-model-family + single-dataset-conditional-gain 组合不足以达到这一门槛。\n\n**Findings 定位合理**：诊断分析本身扎实、统计透明度极高、可复现性强，适合作为 Findings 论文为后续工作（如扩展到更多模型家族、其他结构化预测任务）提供基础。\n\n---\n\n### Detailed Comments\n\n**分歧解决记录**：\n\n| Issue | R1 | R2 | Director 判定 |\n|-------|----|----|--------------|\n| R1-N1 Failure mode 层次化 | Must-Fix | REBUT→Should-Fix | **Should-Fix** (W4)。隐式层次已存在，显式化是 editorial 改进 |\n| R1-W1 Bound 过松 | Should-Fix | REBUT→Minor | **不列入 weakness**。Bound 作为 necessary condition 确认负面结果，looseness IS the point |\n| R2-W4 实践指导 | REBUT | Should-Fix | **Should-Fix** (W7)。内容存在但可见性不足 |\n| R1-W4 Abstract >200 词 | Should-Fix | AGREE | **撤销**。Director 验证 abstract ~172 词，在 200 词限制内。两位 Reviewer 的视觉估计有误 |\n\n**格式合规检查**：\n- ✅ Abstract ≤200 词（~172 词）\n- ✅ 主文 8 页（符合 EMNLP 2026 限制）\n- ✅ Limitations 在正文中（非 Appendix）\n- ✅ 双栏 ACL 模板\n- ✅ 匿名审稿（author 为 \"Anonymous\"）",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "## Round 45 审稿报告\n\n**论文**: When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh（全新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验评估; R2: 新颖性/相关工作/完整性）\n**轮次**: 1 轮（交叉回应后达成共识，无需 Round 2）\n\n---\n\n### Summary\n\n论文系统研究 test-time compute scaling（self-consistency, best-of-N）在 NER 上的表现。核心发现是\"correlation-selection gap\"：质量估计信号能预测输出质量（AUROC 达 0.82），但实例级选择无法带来可检测的 F1 增益（<1pp，CI 跨零）。诊断框架识别 degeneracy 和 signal alignment collapse 两个共现条件。Entity-level construction 作为探索性贡献在 Few-NERD 3-epoch 训练下获 +1.40pp 条件性增益（全局 Holm p_adj=0.055，suggestive）。实验覆盖 4 个 NER 数据集、2 个微调模型族（Qwen3-8B, LLaMA-3.1-8B）、57 项统计检验，附 46 页 appendix。\n\n---\n\n### Strengths\n\n**S1. Correlation-selection gap 概念具有原创性和跨任务价值。** 群体水平高相关性无法转化为实例级选择增益——这一现象此前未被系统识别和诊断。对任何使用 confidence-based reranking 的结构化预测任务都有警示意义。[R1-S2, R2-S1 共识]\n\n**S2. 统计方法论在 NLP 实证分析中属于标杆水准。** 57 项检验的 Holm-Bonferroni 校正、bootstrap CI、TOST 等价性检验、post-hoc power analysis、Cohen's d 效应量、置换检验。同时报告 global 和 per-family 校正，诚实标注 p_adj=0.055 的边界状态。[R1-S1, R2-S4 共识]\n\n**S3. 分析覆盖面极其全面。** 46 页 appendix 包含 N-scaling、温度敏感性、cross-dataset transfer、free-form decoding ablation、epoch convergence、per-entity-type analysis、calibration analysis 等。几乎所有潜在混淆因素均被系统排查。[R1-S3, R2-S2 共识]\n\n**S4. 声称限定诚实恰当。** Entity construction 始终标记为 \"exploratory\"，negative claims 使用 \"no detectable gains\" + CI 限定。Limitations 涵盖英语限定、模型规模限定、统计功效限定。[R1-S5, R2 共识]\n\n**S5. 可复现性高。** 训练配置完整（Table 22），超参数详尽，承诺公开代码/checkpoint/seed 级结果。[R1-S6]\n\n**S6. 形式化贡献有价值。** Proposition 1 将 entity construction 形式化为 MBR 解码，Proposition 2 的 degeneracy decomposition 提供可验证 bound（16 种配置全部成立）。[R1-S4]\n\n---\n\n### Weaknesses\n\n#### Must-Fix（两位 Reviewer 共识）\n\n**[MUST-FIX] W1. 模型覆盖面过窄，普适性声称超出证据范围 [R45-N1]**\n\n主实验仅用 2 个模型族（Qwen3-8B, LLaMA-3.1-8B），均为 ~8B 参数微调。72B zero-shot probe 和 few-shot 实验被论文自身标注为 exploratory。关键证据：Table 43 显示 degeneracy 是 model-family-dependent（Qwen2.5 在 Few-NERD 上 31.7%–46.2%，显著高于 Qwen3 的 13.0%），Table 44 跨家族（Claude, Gemini, GPT, DeepSeek）差异巨大。标题\"When Self-Consistency Fails for NER\"暗示一般性结论，但证据仅支持\"在 7-14B 微调模型 + 4 个英文数据集上\"。\n\n- R1 Must-Fix (N2), R2 AGREE\n- **建议**：收紧 title/abstract 的普适性表述，显式限定为测试模型区间（\"7–14B fine-tuned open-weight models\"）；或增加 ≥1 个模型家族的完整微调实验。R2 倾向前者（camera-ready 阶段增加新实验不现实），Director 同意。\n\n#### Should-Fix（影响评分）\n\n**[SHOULD-FIX] W2. Entity construction 统计边际且在 abstract/Figure 1 中展示权重过高 [R45-W1]**\n\n全局 Holm-Bonferroni 校正下 p_adj=0.055，不满足 α=0.05。Per-family p_adj=0.006 依赖未预注册的 family 划分，构成研究者自由度。Entity construction 仅在 Few-NERD 上有正增益（+1.0pp conditional），ScieERC −0.12pp，CoNLL −0.5pp。Figure 1 中 \"+1.4pp\" 是单个配置结果而非聚合数据。一个 p_adj=0.055 的结果不应作为论文三大贡献之一呈现。\n\n- R1 AGREE (W3), R2-W3 提出, 双方共识\n- **建议**：(a) 降低 entity construction 在 abstract/Figure 1 中的突出程度，与 \"exploratory\" 定位匹配；(b) Figure 1 标注 \"+1.4pp\" 为单个配置而非聚合效果；(c) 主文报告全局 Holm p 值并标注 \"marginally significant under global correction\"\n\n**[SHOULD-FIX] W3. 与 Landesberg (2026) 并行发现的差异化论述不够充分 [R45-W2]**\n\nCorrelation-selection gap 存在并行发现。当前 §2 末尾的 \"Concurrent work\" 段过于简短，不足以让读者理解本文的增量贡献（诊断框架 + 形式化结果 vs. gap 发现本身）。\n\n- R2-W1 提出, R1 AGREE\n- R1 补充：论文的核心增量是 *diagnosing* the gap（四种 failure mode、Proposition 1-2、多信号/多数据集系统比较），而非 *discovering* the gap。需在 Introduction 中显式分离这两个层面。\n- **建议**：Introduction 增加一段明确说明与 Landesberg 的关系，强调增量贡献是诊断框架，而非 gap 本身的发现\n\n**[SHOULD-FIX] W4. Failure mode 四种模式的层次化关系未显式形式化 [R45-W3]**\n\nDegeneracy 在逻辑上蕴含 signal collapse（若所有输出相同，信号必然相同），但定义层面未显式建立蕴含关系。四种模式未覆盖 actively misleading signals（Table 4 中 FK 在 CoNLL 上 ρ=−0.05）。\n\n- R1 Must-Fix (N1), R2 REBUT（降为 Should-Fix——隐式层次已存在于 Figure 1 + §4 + Appendix ae 诊断协议）\n- **Director 判定**：降为 Should-Fix。R2 指出隐式层次已存在且 ρ=−0.05 统计上与零无异。但 R1 关于显式形式化的建议有价值——从业者操作化使用需要明确层次。\n- **建议**：Section 3.3 或 4 开头加 1-2 句显式声明顺序诊断逻辑\n\n**[SHOULD-FIX] W5. 3-seed 局限性在主文 Table 2/4 中未充分注明 [R45-W4]**\n\n训练 seed 仅 3 个，cross-seed 变异分析仅 3 个数据点。此限制同样适用于主选择结果（Table 2, Table 4），但 3-seed 局限仅在 Limitations 部分提及。\n\n- R1-W2 提出, R2 AGREE（3-seed 在 NER fine-tuning 中是常见做法，成本约束合理）\n- **建议**：在 Table 2/4 caption 或正文中显式注明 3-seed 局限性\n\n**[SHOULD-FIX] W6. Table 1 novelty comparison 维度选择偏向本文 [R45-W5]**\n\n6 个维度中 \"Diagnostics\" 和 \"Prescriptive\" 恰好是本文强项，缺少 Landesberg 等工作可能更强的维度（Model Scale Range, Task Diversity）。\n\n- R2-W2 提出, R1 AGREE 但非 must-fix\n- **建议**：caption/脚注承认维度选择局限，或增加 1-2 个本文较弱维度\n\n**[SHOULD-FIX] W7. 实践指导在主文可见性不足 [R45-W6]**\n\nAppendix ah（10 条 Q&A 式建议）和 Appendix ae（cost-benefit 分析）包含实质内容，但主文 Section 8 缺乏 actionable summary。\n\n- R2-W4 提出, R1 REBUT（内容存在但埋得太深）\n- **Director 判定**：核心问题是可见性而非缺失。Appendix 内容扎实，但审稿人和读者首先看主文。\n- **建议**：Section 8 增加 \"Practical Implications\" 段落（3-4 句），提炼 Appendix ah 核心建议\n\n#### Minor Issues\n\n- **M1**: Figure 2 标记点小、线条细，打印尺寸下难以区分 [R1-M1, R2 AGREE]\n- **M2**: MBR 在 abstract/introduction 中使用但未展开全称，首次完整展开在 Section 6.1 [R1-M2, R2 AGREE]\n- **M3**: Table 1 列头 \"Yao+ 2026\"/\"Ours\" 首次阅读不直观，建议更具描述性标签 [R1-M4, R2 AGREE]\n\n---\n\n### Questions\n\n**Q1** [R1-Q1]: Proposition 1 entity-wise independence 假设的敏感性如何？相邻实体存在依赖关系（如嵌套实体），最优 θ 可能受 entity correlation 影响。[R2 AGREE]\n\n**Q2** [R1-Q2]: Correlation-selection gap 在不同数据集上机制不同（ScieERC/CoNLL 以 degeneracy 为主，Few-NERD 以 signal collapse 为主），是否真是单一现象还是多种不同失效模式的共同症状？[R2 REBUT——统一框架是 feature 不是 bug，类似\"发烧\"是统一诊断信号但病因各异]\n\n**Q3** [R1-Q3]: Free-form decoding ablation 仅在 Few-NERD/ScieERC 上测试，\"LP compression is model-intrinsic\" 结论能否推广到 CoNLL/WNUT？[R2 AGREE——完整 4-dataset ablation 更有说服力]\n\n**Q4** [R1-Q5]: Table 2 主选择结果的 post-hoc power analysis 缺失。给定 test instances 数量、3 seeds、α=0.05，minimum detectable effect size 是多少？[R2 AGREE]\n\n---\n\n### Missing References\n\n1. **Florian et al. (2003)** NER 集成学习——best-of-N selection 的自然历史对照（model-level diversity vs. sample-level diversity）[R2 提出, R1 AGREE]\n2. **代码生成中的 self-consistency**——结构化输出的 SC 对比文献，可为 correlation-selection gap 的任务特异性提供上下文 [R1 提出, R2 AGREE]\n3. **Diversity-promoting decoding 文献**（如 Diverse Beam Search）——与 degeneracy 概念有概念联系，DBS 本质上是通过解码策略降低 degeneracy [R2 提出, R1 PARTIALLY AGREE]\n\n---\n\n### External Review\n\n外部审稿：未请求。\n\n---\n\n### Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（18 info, 0 critical, 0 warning）\n\n**主要发现**：\n- **排版质量**: 双栏格式符合 ACL 模板，全文无 margin 溢出、无 LaTeX 错误、无未解析引用\n- **视觉密度**: 8 页主文含 6 figures + 5 tables = 11 个 display items（~1.4/页），密度优秀，text-figure-table 交替节奏良好\n- **Figure 1**: 全宽 overview，三阶段 pipeline 用颜色区分清晰，caption 自包含，信息密度高——优秀的视觉锚点\n- **首页**: 无视觉锚点（纯文本 Abstract + Introduction），第一个 display item 在 page 2。建议考虑前移一个简图或核心数字到 page 1\n- **图表一致性**: 蓝/橙/绿/红在 Figures 2-6 中语义统一，色盲友好\n- **小尺寸图表**: Figure 4 两个 subfigure、Figure 5、Figure 6 偏小，打印后可读性接近下限\n- **表格**: 全部使用 booktabs 风格，最优结果加粗，小数精度一致\n- **Limitations**: 简洁（~1/3 页，3 个要点），符合 EMNLP 规范\n- **Appendix**: Page 14 较密集（3 个 display items 挤一页），Figure 9 subfigure 字号偏小\n\n---\n\n### Overall Assessment\n\n**Overall: 3.0 / 5 (Findings)**\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Overall | 3.5 | 3.0 | **3.0** |\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Confidence | 4.0 | 4.0 | 4.0 |\n\n**Director 评分理由**：\n\n论文的核心优势——correlation-selection gap 概念的原创性、标杆级统计方法论、极其全面的分析覆盖——使其在方法论严谨性上达到了很高水准。然而三个结构性弱点限制了其 impact：\n\n1. **模型覆盖面过窄**（唯一 Must-Fix 共识）：仅 2 个 ~8B 模型族，且 Table 43 明确显示 degeneracy 是 model-family-dependent，直接削弱普适性声称。\n2. **唯一的建设性贡献统计边际**：Entity construction 全局 Holm p_adj=0.055，仅在 1/3 数据集上有正增益，不足以支撑三大贡献之一的定位。\n3. **并行发现降低新颖性溢价**：Landesberg (2026) 的 concurrent discovery 使 gap 本身不再是独占性发现，论文需要更强地论证诊断框架的增量价值。\n\n论文以负面结果为主（\"SC 对 NER 无效\"），建设性部分弱。负面结果论文要达到 Conference 水准需要更广的适用范围或更强的机制洞见来补偿 impact 不足。当前的 2-model-family + single-dataset-conditional-gain 组合不足以达到这一门槛。\n\n**Findings 定位合理**：诊断分析本身扎实、统计透明度极高、可复现性强，适合作为 Findings 论文为后续工作（如扩展到更多模型家族、其他结构化预测任务）提供基础。\n\n---\n\n### Detailed Comments\n\n**分歧解决记录**：\n\n| Issue | R1 | R2 | Director 判定 |\n|-------|----|----|--------------|\n| R1-N1 Failure mode 层次化 | Must-Fix | REBUT→Should-Fix | **Should-Fix** (W4)。隐式层次已存在，显式化是 editorial 改进 |\n| R1-W1 Bound 过松 | Should-Fix | REBUT→Minor | **不列入 weakness**。Bound 作为 necessary condition 确认负面结果，looseness IS the point |\n| R2-W4 实践指导 | REBUT | Should-Fix | **Should-Fix** (W7)。内容存在但可见性不足 |\n| R1-W4 Abstract >200 词 | Should-Fix | AGREE | **撤销**。Director 验证 abstract ~172 词，在 200 词限制内。两位 Reviewer 的视觉估计有误 |\n\n**格式合规检查**：\n- ✅ Abstract ≤200 词（~172 词）\n- ✅ 主文 8 页（符合 EMNLP 2026 限制）\n- ✅ Limitations 在正文中（非 Appendix）\n- ✅ 双栏 ACL 模板\n- ✅ 匿名审稿（author 为 \"Anonymous\"）",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4845 · 2026-05-24T23:22:00.542960+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4031
}
```

</details>

---


### Assistant

_source line 4846 · 2026-05-24T23:22:09.332383+00:00_

Round 45 审稿完成。

**结论：Overall 3.0 (Findings)**

- **1 个 Must-Fix**：模型覆盖面过窄（仅 2 个 ~8B 模型族），需收紧普适性声称
- **6 个 Should-Fix**：entity construction 统计边际且展示过度、Landesberg 差异化不足、failure mode 层次化未显式化、3-seed 局限注明不足、Table 1 维度偏向、实践指导可见性不足
- **1 个 Reviewer 误判已纠正**：Abstract 实际 ~172 词，在 200 词限制内
- **R1-W1（bound 过松）不列入 weakness**：R2 说服力强——looseness 本身就是负面结果的理论确认

报告已投递至 Research Director。Issue Tracker 已同步更新（1 critical open, 6 warning open, 6 info open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 372

## Round 372

2 recorded events


### User

_source line 4847 · 2026-05-24T23:22:12.248293+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部意见的逐条交叉回应，已提交给 Director。核心判断：

- **N1 降级为 Should-Fix**：诊断框架的层次关系在 Figure 1 和 Appendix ae 中已隐式存在，anti-correlated signal (ρ=−0.05) 统计上与零无异，不构成独立失效模式
- **N2 同意为 Critical**：模型覆盖面是论文最大弱点，但建议通过收紧 title/abstract 表述解决而非新增实验
- **W1 降级为 Minor**：Proposition 2(c) 作为 necessary condition 的定位已经合理
- **W2/W3/W4 同意**：3-seed 局限需注明，entity construction 展示权重需降低，abstract 超字数是硬性违规
- **M3 反驳**：N-scaling 分析在 Figure 2/3/5 中已有主文覆盖
- **Q2/Q4 反驳**：gap 作为统一诊断信号（底层原因 dataset-specific）是框架的 feature；5 特征已达 AUROC 0.923

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 4848 · 2026-05-24T23:22:23.728720+00:00_

Round 45 审稿报告已投递至 Research Director，Issue Tracker 已同步更新。

**报告摘要**：
- **Overall: 3.0 (Findings)**（R1: 3.5, R2: 3.0）
- **1 个 Must-Fix 共识**：模型覆盖面过窄（仅 2 个 ~8B 模型族），title/abstract 普适性声称超出证据
- **6 个 Should-Fix**：entity construction 展示过度（p_adj=0.055）、Landesberg 差异化不足、failure mode 层次未显式化、3-seed 局限、Table 1 维度偏向、实践指导可见性不足
- **分歧解决**：R1-N1 failure mode 层次化从 Must-Fix 降为 Should-Fix；R1-W1 bound 松弛不列入 weakness；R1-W4 abstract 超字数经验证撤销（实际 ~172 词）
- **1 轮收敛**：关键问题达成共识，无需 Round 2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 373

## Round 373

66 recorded events


### User

_source line 4849 · 2026-05-25T22:28:38.185057+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 4850 · 2026-05-25T22:28:44.923571+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 4851 · 2026-05-25T22:28:44.974445+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4852 · 2026-05-25T22:28:56.058477+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 4853 · 2026-05-25T22:28:56.209522+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 4854 · 2026-05-25T22:29:14.221456+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4855 · 2026-05-25T22:29:14.272092+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4856 · 2026-05-25T22:29:19.539015+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4857 · 2026-05-25T22:29:21.094200+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (329 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_fewnerd_mf4v2_s42_v4: Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.（准备中）\n- exp_fewnerd_mf4v2_s123_v2: FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.（准备中）\n- exp_fewnerd_mf4v2_s42_v2: FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=42, N=8, T=1.0.（准备中）\n- eval_scd_fewnerd_fallback（准备中）\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) au
…[truncated 1746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1555
}
```

</details>

---


### Tool call

_source line 4858 · 2026-05-25T22:29:21.194985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 4859 · 2026-05-25T22:29:22.048185+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{When Self-Consistency Fails for NER:\\ Degeneracy, Signal Collapse, and the Correlation-Selection Gap}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/background}
38	\input{sections/diagnostic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/discussion}
44	
45	\section*{Limitations}
46	\input{sections/limitations}
47	
48	\bibliography{references}
49	
50	\appendix
51	\renewcommand{\thesection}{\alphalph{\value{section}}}
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 4860 · 2026-05-25T22:29:22.098762+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 4861 · 2026-05-25T22:29:22.299818+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 4862 · 2026-05-25T22:29:27.415303+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

The search results do not contain a specific call for papers for EMNLP 2026 with the submission guidelines you're looking for. The results
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5316
}
```

</details>

---


### Tool result

_source line 4863 · 2026-05-25T22:29:27.415729+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-24\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp_fewnerd_mf4v2_s42_v4: Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.（准备中）\\n- exp_fewnerd_mf4v2_s123_v2: FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.（准备中）\\n- exp_fewnerd_mf4v2_s42_v2: FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=42, N=8, T=1.0.（准备中）\\n- eval_scd_fewnerd_fallback（准备中）\\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.（准备中）\\n- exp_b2_v3_domain_invariant: Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improving cross-domain generalization at the cost of some discriminative power. If LGB AUC improves on held-out domains, domain features were causing negative transfer.（准备中）\\n- exp_b2_v2_multi_domain_joint: Joint multi-domain training (CoNLL+SciERC+FewNERD LODO) improves entity verifier AUC and cross-domain construction F1 by exposing the model 
…[truncated 1338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5115
}
```

</details>

---


### Tool call

_source line 4864 · 2026-05-25T22:29:42.793649+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 4865 · 2026-05-25T22:29:43.296991+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 4866 · 2026-05-25T22:29:44.250784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 4867 · 2026-05-25T22:29:44.752944+00:00_

1	\begin{abstract}
2	Test-time compute scaling via repeated sampling yields large gains on discrete-answer reasoning, but whether these gains transfer to named entity recognition (NER) remains open.
3	Across four NER datasets with fine-tuned 7--14B models, we find that quality estimation signals predict output quality well (area under the ROC curve [AUROC] up to $0.82$), yet selecting among candidates produces no detectable improvement over greedy decoding, even with 64 samples.
4	We term this disconnect the \textbf{correlation-selection gap} and trace it to two co-occurring conditions: \textit{degeneracy}, where multiple samples collapse to identical predictions, and \textit{signal alignment collapse}, where per-sample scores fail to discriminate quality within an instance.
5	Entity-level construction offers conditional gains ($+1.40$ percentage points [pp] on Few-NERD) where the framework identifies favorable conditions, but exhibits inverse scaling in most configurations.
6	Cross-task pilots on relation extraction (RE) and SQL parsing confirm task-specific failure modes.
7	The framework is primarily diagnostic, informing when repeated sampling helps for structured prediction and when greedy decoding remains the better default\footnote{Code and data are available at \url{https://anonymous.4open.science/r/struct_self_consist_ie-85D4/}.}.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 4868 · 2026-05-25T22:29:44.803706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 4869 · 2026-05-25T22:29:45.205620+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling, including self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, and extended reasoning \cite{muennighoff2025s1}, has become a reliable strategy for improving reasoning accuracy: sample multiple candidates, estimate quality, select the best.
4	This approach succeeds when outputs admit equivalence classes or execution-based verification.
5	For NER, outputs are entity sets with partial overlap, and the boundary conditions for effective scaling remain unknown.
6	Prior work reports task-level correlations between consistency and accuracy \cite{yao2026consistency} and documents diversity collapse under constrained decoding \cite{yun2025price}, but neither provides instance-level diagnostics that explain \textit{when} scaling helps and \textit{when} it harms.
7	
8	We study this question across four NER benchmarks and two model families (7--14B fine-tuned, with ablations to 72B), using RE as a secondary case study.
9	Our central finding is a \textbf{correlation-selection gap}: quality estimation (QE) signals predict output quality with strong discrimination (AUROC up to $0.82$; \S\ref{sec:qe_results}), yet using these signals to select among candidates yields no detectable improvement.
10	Majority vote (MV) gains remain below one percentage point (pp) even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}), and log-probability (LP), the only per-sample signal, is neutralized by within-instance compression (\S\ref{sec:selection_gap}).
11	The gap has structural roots: four of five signals assign identical scores to all candidates from a given input, so they estimate quality across inputs but cannot rank candidates within one.
12	
13	A diagnostic framework traces these failures to two co-occurring conditions.
14	\textit{Degeneracy} ($12$--$68$\% of instances) produces identical outputs across all $N$ samples, eliminating any opport
…[truncated 3973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 4870 · 2026-05-25T22:29:45.758038+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 4871 · 2026-05-25T22:29:46.213294+00:00_

issues:
# ===== ROUND 45 MUST-FIX (CONSENSUS) =====
- id: R45-N1
  summary: "模型覆盖面过窄（仅 2 个 ~8B 模型族），标题/摘要普适性声称超出证据范围"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 43
  last_seen_round: 45
  mentions:
    - round: 43
      reviewers: [1, 2]
      note: "R43-W5 作为 warning 提出，已通过 Limitations 声明部分解决"
    - round: 45
      reviewers: [1, 2]
      note: "R1 升级为 Must-Fix (N2)。R2 AGREE。Table 43 显示 degeneracy 是 model-family-dependent。"
  action_items:
    - round: 45
      action: "收紧 title/abstract/intro 的普适性表述，显式限定为 7-14B fine-tuned models"
      assigned_to: paper_agent
      status: in_progress

# ===== ROUND 45 SHOULD-FIX =====
- id: R45-W1
  summary: "Entity construction 统计边际（global Holm p_adj=0.055）且在 abstract/Figure 1 中展示权重过高"
  category: method
  severity: warning
  status: in_progress
  first_raised_round: 34
  last_seen_round: 45
  mentions:
    - round: 43
      reviewers: [1, 2]
      note: "R43-N4 prescriptive→exploratory 重定位已解决"
    - round: 45
      reviewers: [1, 2]
      note: "R2-W3 提出全局 Holm 不显著。R1 strongly AGREE。Figure 1 '+1.4pp' 是单个配置非聚合。"
  action_items:
    - round: 45
      action: "降低 entity construction 在 abstract/Figure 1 中的突出程度；Figure 1 标注 '+1.4pp' 为单配置结果"
      assigned_to: paper_agent
      status: in_progress

- id: R45-W2
  summary: "与 Landesberg (2026) 并行发现的差异化论述不够充分"
  category: framing
  severity: warning
  status: in_progress
  first_raised_round: 39
  last_seen_round: 45
  mentions:
    - round: 42
      reviewers: [1, 2]
      note: "R41-N4 通过 §2 四维度对比解决"
    - round: 45
      reviewers: [1, 2]
      note: "R2-W1 重新提出。R1 AGREE。§2 末尾 concurrent work 段过于简短。"
  action_items:
    - round: 45
      action: "Introduction 中增加一段明确说明与 Landesberg 的关系，强调增量贡献是诊断框架而非 gap 发现本身"
      assigned_to: paper_agent
      status: in_progress

- id: R45-W3
  summary: "Failure mode 四种模式的层次化关系未显式形式化"
  category: method
  severity: warning
  status: in_progress
  first_raised_round: 45
  last_seen_round: 45
  mentions:

…[truncated 7354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 4872 · 2026-05-25T22:29:46.464537+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 4873 · 2026-05-25T22:29:48.873221+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references, and final versi
…[truncated 981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6079
}
```

</details>

---


### Tool result

_source line 4874 · 2026-05-25T22:29:51.331849+00:00_

Web search results for query: "EMNLP 2026 call for papers deadline commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 on X: \"The First Call for Industry Track Papers for EMNLP 2026 is officially out! Are you deploying NLP in real-world applications? Share your insights, challenges, and deployed systems with the community. 🗓️ Deadline: June 16, 2026 🔗 Link: https://t.co/ga3k6CJcm0 #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2048750521696072166"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title"
…[truncated 1349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8034
}
```

</details>

---


### Tool result

_source line 4875 · 2026-05-25T22:29:51.332508+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 249\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4867
}
```

</details>

---


### Tool call

_source line 4876 · 2026-05-25T22:30:03.517899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 4877 · 2026-05-25T22:30:04.471653+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time scaling and self-consistency.}\label{sec:yun_contrast}
4	Self-consistency (SC) \cite{wang2023selfconsistency} and best-of-$N$ with scaling laws \cite{snell2025scaling, brown2024monkeys, gao2023scaling} yield large gains on reasoning; recent extensions include reward-tail-guided search \cite{li2026rewardtail}. Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and trained verifiers \cite{cobbe2021verifiers, lightman2024verify, li2023stepaware} target discrete-answer settings.
5	SC can fail when consistent outputs are wrong \cite{chen2023twofailures}; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} variants face limits where sub-output agreement does not yield selection gain. Iterative self-verification \cite{shinn2023reflexion} offers an alternative, but our ESJ and multi-round self-consistency (MRSC) results (\S\ref{sec:selection_gap}) show such approaches also fail for NER.
6	\citet{yun2025price} identify diversity collapse under constrained decoding; we extend their qualitative account with quantitative diagnostics (\S\ref{sec:selection_gap}).
7	
8	\paragraph{Consistency for structured information extraction (IE).}
9	LLM-based IE has expanded rapidly \cite{xu2024llmie}, yet reliability under repeated sampling is underexplored.
10	\citet{yao2026consistency} show consistency correlates with accuracy for NER/RE ($\rho$ up to 0.47); we extend to instance-level analysis: task-level $\rho$ masks instance-level degeneracy, and we decompose failure into degeneracy and LP compression.
11	Critically, their task-level granularity cannot distinguish instances where scaling helps from those where it harms; our entity-level decomposition addresses this gap (Table~\ref{tab:novelty_comparison}).
12	\citet{xie2023zeroshot} propose entity voting for zero-shot NER; \citet{xie2024selfimproving} extend this with SC-based self-annotation, reporting gains where zero-shot div
…[truncated 3032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 4878 · 2026-05-25T22:30:04.471996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 4879 · 2026-05-25T22:30:04.923953+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails, as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling}), no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples (\textit{structural}: Soft Jaccard [SJ], entity voting confidence [VC]; \textit{surface}: exact match [EM], Fleiss' $\kappa$ [FK]) and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i) = |y_i|^
…[truncated 2990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 4880 · 2026-05-25T22:30:04.924345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 4881 · 2026-05-25T22:30:05.426408+00:00_

1	\section{Single-Signal Selection Results}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	Four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}); selection failure is a design property.
5	LP, the only per-sample signal, suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}). This compression is model-intrinsic (free-form std ratio $0.97{\times}$; Appendices~\ref{app:freeform_ablation},~\ref{app:lp_failure_stability}); where LP varies, gains depend on alignment, not degeneracy.
6	Within-instance $\rho$ measures whether LP discriminates candidates for a fixed input (median $0.26$ on SciERC vs.\ $0.67$ on Few-NERD; Appendix~\ref{app:within_instance_rho}), making it the relevant predictor of selection success.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.775$, Greedy${=}0.645$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
12	\label{tab:selection}
13	\begin{tabular}{lcc}
14	\toprule
15	Method & NER F1 & $p$ \\
16	\midrule
17	Oracle & $0.775 \pm 0.001$ & --- \\
18	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
19	\midrule
20	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
21	SJ           & $0.646 \pm 0.002$ & .67 \\
22	FK           & $0.646 \pm 0.001$ & .79 \\
23	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
24	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
25	\midrule
26	Random       & $0.610 \pm 0.003$ & --- \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	\begin{figure}[t]
32	\centering
33	\includegraphics[width=0.92\columnwidth]{fig_selection_gap}
34	\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\rho$; line:
…[truncated 3365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 4882 · 2026-05-25T22:30:05.426748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 4883 · 2026-05-25T22:30:06.380459+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection yields no detectable gains (\S\ref{sec:selection_gap}), we present exploratory attempts informed by diagnostic findings to extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield a positive result, though on a single dataset.
5	
6	\begin{table}[t]
7	\centering
8	\footnotesize
9	\caption{Summary of 9 method categories tested. $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\begin{tabular}{@{}llrl@{}}
12	\toprule
13	Category & Method & $\Delta$F1 / metric & \S \\
14	\midrule
15	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
16	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
17	Self-verif. & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
18	Multi-round & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
19	Latent agg. & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
20	Adaptive gate & DALS & $+0.71$\,pp (Sci)$^\ddagger$ & \ref{app:dals} \\
21	Sup.\ verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
22	Sup.\ combo & LR/MLP/RF & $-0.4$--$3.1$\,pp & \ref{app:supervised_combination} \\
23	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
24	\bottomrule
25	\end{tabular}
26	
27	\vspace{1pt}
28	{\scriptsize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp). LSC: latent self-consistency; DALS: degeneracy-aware LP selection.}
29	\end{table}
30	
31	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
32	
33	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
34	Combining 4 samples each from Qwen3-8B and LLaMA-3.1-8B (Few-NERD) yields $+0.42$\,pp over pure LLaMA ($p{<}0.001$
…[truncated 749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 4884 · 2026-05-25T22:30:06.380948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 4885 · 2026-05-25T22:30:06.381346+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \beta/(\beta{+}1)\}$ under balanced set-overlap utility; $\beta{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}; Appendix~\ref{app:mbr_connection}), consistent with utility degradation on structured outputs \cite{eikema2025structured}.
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp, a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern: 50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:fron
…[truncated 3971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4886 · 2026-05-25T22:30:06.833252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 4887 · 2026-05-25T22:30:07.335514+00:00_

1	\section{Cross-Dataset Experiments}\label{sec:experiments}
2	
3	Sections~\ref{sec:selection_gap}--\ref{sec:theory} developed the diagnostic framework on SciERC; this section extends it across datasets and models.
4	
5	\subsection{Experimental Setup}\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 53.7\% zero F1) probes the signal-collapse boundary.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are Low-Rank Adaptation (LoRA) fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
16	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}). Thinking-token impact on LP is negligible ($<$2.7\% of median range; Appendix~\ref{app:thinking_token}).
17	
18	\begin{figure}[t]
19	\centering
20	\includegraphics[width=0.92\columnwidth]{figures/fig_n_scaling_mv.pdf}
21	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
22	\label{fig:n
…[truncated 4656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 4888 · 2026-05-25T22:30:07.335870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 4889 · 2026-05-25T22:30:08.289607+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{When test-time scaling fails for NER.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, degeneracy ($12$--$68$\%) reduces candidate diversity while signal alignment collapse ($\alpha{\to}0$) limits ranking.
5	The degeneracy decomposition (\S\ref{sec:theory}) identifies $\alpha$, not degeneracy, as the binding constraint ($8$--$33{\times}$ tighter); this persists across families \cite{yun2025price}, scales (4B--72B), and decoding modes (Appendix~\ref{app:freeform_ablation}).
6	The diagnostic framework that identifies these co-occurring conditions is our primary contribution (Appendices~\ref{app:objections},~\ref{app:cost_benefit}).
7	At $N{=}8$, high degeneracy ($>50$\%) suggests scaling will not help; low degeneracy with strong LP-F1 alignment may warrant entity construction; otherwise, greedy remains the default (Appendices~\ref{app:recommendations},~\ref{app:when_selection_works}).
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 4890 · 2026-05-25T22:30:08.289973+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 4891 · 2026-05-25T22:30:08.541277+00:00_

1	Our primary evidence is from English NER with fine-tuned 7--14B open-weight models; frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), and cross-task extensions (RE $n{=}397$, SQL $n{=}196$) are exploratory.
2	
3	The framework is diagnostic, not causal: under global Holm--Bonferroni ($k{=}57$), the strongest construction claim reaches $p_{\text{adj}}{=}0.055$; our negative selection claims are bounded by statistical power (2--3 seeds, MDE ${\approx}1.5$\,pp).
4	Entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp), and we use a single prompt template per task.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 4892 · 2026-05-25T22:30:08.541616+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool result

_source line 4893 · 2026-05-25T22:30:15.719356+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"}]

Based on the search results, here is the information about the EMNLP 2026 main conference call for papers:

## EMNLP 2026 Main Conference Call for Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

### Key Details:

**Conference Information:**
- The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

**Submission Process:**
- Papers must be submitted, at latest, by the ARR 2026 May cycle. Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.
- All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

**Paper
…[truncated 647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7177
}
```

</details>

---


### Tool call

_source line 4894 · 2026-05-25T22:30:27.463785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 4895 · 2026-05-25T22:30:29.070066+00:00_

File content (70216 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1606
}
```

</details>

---


### Tool call

_source line 4896 · 2026-05-25T22:30:29.321479+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"call for papers\" page limit anonymity double blind format requirements 2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" \"call for papers\" page limit anonymity double blind format requirements 2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 4897 · 2026-05-25T22:30:30.376365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_46/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check review round 46 artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_46/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check review round 46 artifacts"
  }
}
```

</details>

---


### Tool result

_source line 4898 · 2026-05-25T22:30:31.313868+00:00_

total 4784
drwxr-xr-x   2 ubuntu ubuntu    4096 May 25 22:28 .
drwxr-xr-x 165 ubuntu ubuntu   20480 May 25 22:28 ..
-rw-r--r--   1 ubuntu ubuntu 4868192 May 25 14:40 submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 937
}
```

</details>

---


### Tool call

_source line 4899 · 2026-05-25T22:30:31.414626+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 4900 · 2026-05-25T22:30:31.465290+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 4901 · 2026-05-25T22:30:38.942751+00:00_

Web search results for query: ""EMNLP 2026" "call for papers" page limit anonymity double blind format requirements 2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Paper Guidelines","url":"https://www.araseg.aramlab.ai/paper-guidelines"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

I found some information about EMNLP 2026, but I need to search more specifically for the page limit requirements. Let me do another search:

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Paper Guidelines","url":"https://www.araseg.aramlab.ai/paper-guidelines"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How Many Pages? Paper Length Prediction from the Metadata","url":"https://arxiv.org/pdf/2010.15924"}]

Perfect! Now I hav
…[truncated 1464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 9621
}
```

</details>

---


### Tool call

_source line 4902 · 2026-05-25T22:30:45.115669+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 -A10 \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null || grep -B2 -A10 \"external\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null || echo \"NO_MATCH\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 -A10 \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null || grep -B2 -A10 \"external\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null || echo \"NO_MATCH\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 4903 · 2026-05-25T22:30:46.019321+00:00_

NO_MATCH

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 4904 · 2026-05-25T22:30:46.019644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 4905 · 2026-05-25T22:30:46.070567+00:00_

0	\raggedbottom
1	\setlength{\floatsep}{2pt plus 1pt minus 1pt}
2	\setlength{\textfloatsep}{3pt plus 1pt minus 1pt}
3	\setlength{\intextsep}{2pt plus 1pt minus 1pt}
4	\setlength{\dblfloatsep}{2pt plus 1pt minus 1pt}
5	\setlength{\dbltextfloatsep}{3pt plus 1pt minus 1pt}
6	\setlength{\abovecaptionskip}{4pt}
7	\setlength{\belowcaptionskip}{-2pt}
8	\section{Notation}\label{app:notation}
9	
10	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
11	
12	\begin{table}[h]
13	\centering
14	\small
15	\begin{tabular}{cl}
16	\toprule
17	Symbol & Meaning \\
18	\midrule
19	$\mathcal{M}$ & Language model \\
20	$x$ & Input instance \\
21	$y_i$ & $i$-th stochastic sample \\
22	$N$ & Number of samples \\
23	$T$ & Sampling temperature \\
24	$c(\cdot)$ & Confidence signal \\
25	SJ & Soft Jaccard similarity \\
26	FK & Fleiss' $\kappa$ \\
27	EM & Exact-match voting rate \\
28	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
29	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
30	\bottomrule
31	\end{tabular}
32	\caption{Notation used throughout the paper.}
33	\label{tab:notation}
34	\end{table}
35	
36	\section{Robustness Analysis}\label{app:robustness}
37	
38	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
39	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
40	
41	\begin{table}[t]
42	\centering
43	\small
44	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed 
…[truncated 4794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4906 · 2026-05-25T22:31:17.378303+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4907 · 2026-05-25T22:31:37.348333+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19970
}
```

</details>

---


### Tool call

_source line 4908 · 2026-05-25T22:31:37.398972+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- **标题**: \"When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_46/submitted.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 Main Conference via ARR\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 ≤ 8 页，参考文献无限制\n- **Limitations**: 必填，放在正文末尾（references 之前），不计入页数，上限约 1 页\n- **模板**: ACL style\n- **匿名**: Double-blind（不能出现作者信息）\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **诊断框架 (§3)**: 问题形式化是否严谨？五种信号的定义和区分（per-sample vs instance-level）是否清晰？Soft Jaccard 的 bipartite matching 定义是否有漏洞？\n2. **退化分解 (§6.3)**: 上界 $(1-D) \\cdot G_{nd} \\cdot \\alpha$ 的证明是否正确？\"intentionally loose necessary condition\" 的定位是否合理？recovery ratio 3-12% 的解释是否充分？\n3. **MBR 连接 (§6.1)**: Entity construction 作为 MBR 的 Proposition 是否正确？$\\beta=1$ 恢复 majority vote 的推导是否完整？\n4. **统计方法**: Spearman ρ、AUROC、paired bootstrap、TOST 等效性检验的使用是否正确？Holm-Bonferroni 校正的 k 值选择是否合理？global k=57 vs family k=21 的差异是否被充分讨论？\n\n### 实验有效性\n5. **实验设计**: 4 个 NER 数据集 + RE/SQL 扩展是否足够？模型选择（仅 Qwen3-8B 和 LLaMA-3.1-8B, 7-14B fine-tuned）是否过窄？\n6. **seed 数量**: 2-3 seeds 的统计推断力是否足够？MDE ~1.5pp 的声明是否可靠？\n7. **消融分析**: 9 种方法的覆盖是否全面？是否有明显遗漏的 baseline？\n8. **数据泄露风险**: Fine-tuning 和评估是否有数据重叠？\n9. **Negative result 的统计处理**: \"no detectable improvement\" 的声明是否有充分的等效性检验支持？\n10. **跨数据集一致性**: Few-NERD 上的正面结果（+1.40pp）vs 其他数据集的 null result，这种不一致是否被充分解释？\n\n请给出完整的审稿意见，包括 Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- **标题**: \"When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_46/submitted.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 Main Conference via ARR\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 ≤ 8 页，参考文献无限制\n- **Limitations**: 必填，放在正文末尾（references 之前），不计入页数，上限约 1 页\n- **模板**: ACL style\n- **匿名**: Double-blind（不能出现作者信息）\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **诊断框架 (§3)**: 问题形式化是否严谨？五种信号的定义和区分（per-sample vs instance-level）是否清晰？Soft Jaccard 的 bipartite matching 定义是否有漏洞？\n2. **退化分解 (§6.3)**: 上界 $(1-D) \\cdot G_{nd} \\cdot \\alpha$ 的证明是否正确？\"intentionally loose necessary condition\" 的定位是否合理？recovery ratio 3-12% 的解释是否充分？\n3. **MBR 连接 (§6.1)**: Entity construction 作为 MBR 的 Proposition 是否正确？$\\beta=1$ 恢复 majority vote 的推导是否完整？\n4. **统计方法**: Spearman ρ、AUROC、paired bootstrap、TOST 等效性检验的使用是否正确？Holm-Bonferroni 校正的 k 值选择是否合理？global k=57 vs family k=21 的差异是否被充分讨论？\n\n### 实验有效性\n5. **实验设计**: 4 个 NER 数据集 + RE/SQL 扩展是否足够？模型选择（仅 Qwen3-8B 和 LLaMA-3.1-8B, 7-14B fine-tuned）是否过窄？\n6. **seed 数量**: 2-3 seeds 的统计推断力是否足够？MDE ~1.5pp 的声明是否可靠？\n7. **消融分析**: 9 种方法的覆盖是否全面？是否有明显遗漏的 baseline？\n8. **数据泄露风险**: Fine-tuning 和评估是否有数据重叠？\n9. **Negative result 的统计处理**: \"no detectable improvement\" 的声明是否有充分的等效性检验支持？\n10. **跨数据集一致性**: Few-NERD 上的正面结果（+1.40pp）vs 其他数据集的 null result，这种不一致是否被充分解释？\n\n请给出完整的审稿意见，包括 Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 4909 · 2026-05-25T22:31:55.450856+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18051
}
```

</details>

---


### Tool call

_source line 4910 · 2026-05-25T22:31:55.501585+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: \"When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_46/submitted.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 Main Conference via ARR\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 ≤ 8 页，参考文献无限制\n- **Limitations**: 必填，放在正文末尾（references 之前），不计入页数，上限约 1 页\n- **模板**: ACL style\n- **匿名**: Double-blind（不能出现作者信息）\n\n## 你的审查侧重\n\n### 新颖性\n1. **核心贡献的独创性**: \"correlation-selection gap\" 作为核心发现，与 Landesberg (2026) 的并行发现如何差异化？Table 1 novelty comparison 是否公允？维度选择是否有 cherry-picking 嫌疑？\n2. **诊断框架的贡献**: Degeneracy + signal alignment collapse 的诊断框架是否构成足够的 novelty？还是主要是已知概念的组合？\n3. **与 Yao+ (2026) 的区别**: 从 task-level 到 instance-level 的扩展是否足够支撑一篇独立论文？\n4. **Concurrent work 处理**: §2 末尾对 Landesberg 的讨论是否充分？差异化论述是否清晰？\n\n### 完整性\n5. **Related work 覆盖**: 是否有重要遗漏？NER ensemble learning (Florian et al., 2003)? 代码生成 self-consistency? Diverse beam search?\n6. **论文结构**: Discover/Diagnose/Construct 三阶段结构是否清晰？各 section 之间的逻辑连接是否流畅？\n7. **Limitations**: 是否充分覆盖了论文的局限性？是否符合 EMNLP 2026 要求（放在正文、references 之前）？\n8. **RE/SQL 扩展**: 作为 cross-task 证据，RE (n=397) 和 SQL (n=196, 87.2% degeneracy) 的深度是否足够？还是过于 preliminary？\n\n### 写作质量\n9. **Abstract**: 是否在 200 words 以内？关键发现是否清晰传达？\"+1.40pp on Few-NERD\" 在 abstract 中是否权重过高（考虑到全局 Holm p_adj=0.055）？\n10. **信息密度**: 正文是否过于密集？数字过多是否影响可读性？\n11. **Figure 质量**: Figure 1 overview 是否清晰？其他 figures 是否自包含？\n12. **格式合规**: 正文是否在 8 页以内？Limitations 是否在正文中？是否有匿名性违反？\n13. **Appendix**: 是否有过多正文内容被放到 appendix？\n\n请给出完整的审稿意见，包括 Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: \"When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_46/submitted.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 Main Conference via ARR\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 ≤ 8 页，参考文献无限制\n- **Limitations**: 必填，放在正文末尾（references 之前），不计入页数，上限约 1 页\n- **模板**: ACL style\n- **匿名**: Double-blind（不能出现作者信息）\n\n## 你的审查侧重\n\n### 新颖性\n1. **核心贡献的独创性**: \"correlation-selection gap\" 作为核心发现，与 Landesberg (2026) 的并行发现如何差异化？Table 1 novelty comparison 是否公允？维度选择是否有 cherry-picking 嫌疑？\n2. **诊断框架的贡献**: Degeneracy + signal alignment collapse 的诊断框架是否构成足够的 novelty？还是主要是已知概念的组合？\n3. **与 Yao+ (2026) 的区别**: 从 task-level 到 instance-level 的扩展是否足够支撑一篇独立论文？\n4. **Concurrent work 处理**: §2 末尾对 Landesberg 的讨论是否充分？差异化论述是否清晰？\n\n### 完整性\n5. **Related work 覆盖**: 是否有重要遗漏？NER ensemble learning (Florian et al., 2003)? 代码生成 self-consistency? Diverse beam search?\n6. **论文结构**: Discover/Diagnose/Construct 三阶段结构是否清晰？各 section 之间的逻辑连接是否流畅？\n7. **Limitations**: 是否充分覆盖了论文的局限性？是否符合 EMNLP 2026 要求（放在正文、references 之前）？\n8. **RE/SQL 扩展**: 作为 cross-task 证据，RE (n=397) 和 SQL (n=196, 87.2% degeneracy) 的深度是否足够？还是过于 preliminary？\n\n### 写作质量\n9. **Abstract**: 是否在 200 words 以内？关键发现是否清晰传达？\"+1.40pp on Few-NERD\" 在 abstract 中是否权重过高（考虑到全局 Holm p_adj=0.055）？\n10. **信息密度**: 正文是否过于密集？数字过多是否影响可读性？\n11. **Figure 质量**: Figure 1 overview 是否清晰？其他 figures 是否自包含？\n12. **格式合规**: 正文是否在 8 页以内？Limitations 是否在正文中？是否有匿名性违反？\n13. **Appendix**: 是否有过多正文内容被放到 appendix？\n\n请给出完整的审稿意见，包括 Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 4911 · 2026-05-25T22:31:57.010153+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1508
}
```

</details>

---


### Tool call

_source line 4912 · 2026-05-25T22:32:16.530613+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 初审",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (ARR)\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 初审",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (ARR)\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 4913 · 2026-05-25T22:32:16.631412+00:00_

Next wakeup scheduled for 22:37:00 (in 283s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 4914 · 2026-05-25T22:32:30.166577+00:00_

Reviewer 1 和 2 正在独立初审。预计 ~4.5 分钟后检查进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 374

## Round 374

4 recorded events


### User

_source line 4915 · 2026-05-25T22:39:33.226153+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 扎实的诊断性研究，correlation-selection gap 概念有价值，但 concurrent work（Landesberg 2026）显著削弱新颖性，全局统计显著性边缘（Holm p_adj=0.055），SQL 跨任务证据过于薄弱。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 诊断框架方法论合理，4数据集×2模型×5信号的实验设计完整；但核心建设性 claim（LP selection gain）全局 Holm 校正 p_adj=0.055 未达 0.05 显著性；SQL 仅有一个退化率统计量无法支撑跨任务验证声明 |
| Excitement | 3.0/5 | Correlation-selection gap 是有用的诊断概念，degeneracy + signal alignment collapse 的分解提供了超越简单观察的机制性理解；但 Landesberg (2026) 已独立发现该 gap，实际可操作建议有限（框架自称 primarily diagnostic），entity-level construction 增益边缘且大多数配置下呈 inverse scaling |
| Reproducibility | 4.0/5 | 提供匿名代码/数据链接，附录详细记录实验设置（Table 21 超参数、Table 5 符号表），使用多 seed（3-seed），信号定义明确 |
| Reviewer Confidence | 4/5 | 熟悉 SC/test-time compute scaling 和 NER 领域 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] SQL 跨任务证据严重不足，与 abstract 声明不匹配
- 具体位置：Abstract 第5句 "Cross-task pilots on relation extraction (RE) and SQL parsing confirm task-specific failure modes"; §7.1 提及 SQL n=196, 87.2% degeneracy; Appendix ah "O1" 段仅一句话
- 问题：Abstract 和 Introduction 将 SQL 并列为跨任务验证证据，但整篇论文对 SQL 的分析仅限于一个退化率统计量（87.2%）。没有对 SQL 进行任何信号分析、selection 实验、或诊断框架验证。相比之下 RE 有完整的 Appendix q（LP selection、pairwise overlap、flip instances、free-form decoding comparison），SQL 的深度完全不在同一水平。
- 为什么影响接收：这构成了 claim 与 evidence 的不匹配。"confirm task-specific failure modes" 暗示对 SQL 做了诊断性分析，但实际只有一个数字。审稿人会认为这是 overclaiming。
- 建议修改方向：(a) 降级 SQL 为 "anecdotal evidence" 或从 abstract 中移除；或 (b) 补充 SQL 的信号分析和 selection 实验使其与 RE 的分析深度匹配。

**N2** [critical] 全局统计显著性边缘，核心建设性 claim 未达常规阈值
- 具体位置：§7.2 "reaches p_adj=0.055"; Limitations 段 "the strongest construction claim reaches p_adj=0.055"；Table 4 LP selection gains
- 问题：LP selection 的增益是论文中唯一超越 diagnostic 的 actionable contribution。在 Holm-Bonferroni 全局校正下 p_adj=0.055，未达到 α=0.05。论文在 Limitations 中披露了这一点（值得肯定），但 §7.2、Table 4 和 abstract 的叙述方式并未充分强调这一局限性。Abstract 中 "+1.40 percentage points [pp] on Few-NERD" 作为唯一具体数字被突出，给读者造成该增益是稳健可靠的印象。
- 为什么影响接收：在 EMNLP main conference 标准下，核心 constructive claim 需要强统计支撑。p_adj=0.055 在边缘——本身不致命，但结合该 claim 是论文唯一可操作贡献，需要更显著的支撑或更谨慎的 framing。
- 建议修改方向：(a) 在 abstract 中明确标注该增益在全局校正下为 marginal significance；(b) 在 Discussion（§8）中对这一点进行更充分的讨论，而非仅放在 Limitations 中；(c) 考虑增加 seed 数量（目前2-3 seeds）以提升统计功效。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 与 Landesberg (2026) 的差异化论述不够充分，Table 1 维度选择可能存在偏向
- 具体位置：§2 末尾 "Concurrent work" 段；Table 1
- 问题：Table 1 的6个比较维度（Domain, Granularity, Task, Prompt, Instance, Diagnostic 等）大多选取了本文占优的角度。缺少对 Landesberg 可能占优的维度（如实验模型规模/多样性、任务覆盖广度、是否有更强的 prescriptive 建议等）的讨论。§2 的 concurrent work 讨论仅4行，对于一个直接竞争的 concurrent finding 而言过于简略。一个公允的差异化应该也承认对方的优势。
- 建议：扩展 concurrent work 讨论至至少一个完整段落，明确陈述 Landesberg (2026) 在哪些方面做得更好或更深入，以及本文在哪些方面互补。

**W2** [warning] 论文结构中实验结果分散在 §4 和 §7，逻辑连接不够清晰
- 具体位置：§4 "Single-Signal Selection Results"（page 4-5）与 §7 "Experiments"（page 7-8）
- 问题：§4 已经报告了大量实验结果（Table 2, Figure 2, 各信号 ρ 值和 selection gain），§7 又报告了更多实验结果（Table 4, cross-dataset, robustness, entity construction）。读者难以区分哪些结果属于 "诊断发现" 哪些属于 "方法验证"。这种分散也导致正文信息密度极高。
- 建议：(a) 在 §4 开头明确说明本节定位是 "gap 的发现与量化"；(b) 在 §7 开头明确说明本节是 "补充验证与扩展"；(c) 考虑将部分 §4 的详细数字移至附录。

**W3** [warning] Entity-level construction 的 inverse scaling 问题未被充分解释
- 具体位置：§6.1、§7.5、Table 3
- 问题：论文多次提到 entity-level construction 在 "most configurations" 下呈现 inverse scaling（增加 N 反而降低性能），但对其原因的分析不够深入。§6.1 提到 "feature importance shifts across entity-type complexity" 但没有给出令人信服的机制解释。这是一个反直觉的发现——如果方法在大多数情况下是有害的，它作为"建设性贡献"的价值就需要质疑。
- 建议：对 inverse scaling 给出更详细的归因分析，或明确将 entity-level construction 定位为 preliminary exploration 而非核心贡献之一。

**W4** [warning] Related work 缺少 NER ensemble learning 经典文献
- 具体位置：§2 Related Work
- 问题：论文讨论了 SC 和 uncertainty estimation 相关文献，但完全没有提及经典 NER ensemble 方法。Florian et al. (2003) 的 NER ensemble 是直接相关的早期工作——他们也通过组合多个 NER 系统输出来提升性能。Diverse beam search（Vijayakumar et al., 2018）作为增加 candidate 多样性的方法也值得讨论。这些遗漏可能让 reviewer 质疑作者对该领域的熟悉程度。
- 建议：在 §2 中加入简要讨论，区分 classic ensemble learning（多模型）与 self-consistency（单模型多采样）的根本差异。

## 小问题（不影响接收）

- **M1**: Abstract 中 "+1.40 percentage points [pp] on Few-NERD" 与正文 "+1.39pp"（Table 4）存在微小不一致，可能是四舍五入问题，建议统一。
- **M2**: 正文信息密度极高，§4 第2段连续出现 ρ、AUROC、p 值、F1 差异等 10+ 个统计量，影响可读性。建议精简最关键的 2-3 个数字放在正文，其余移至附录。
- **M3**: Figure 1 的 "Resolution" 面板中 "+1.4 pp" 标注字体较小，且该数字在全局校正下为边缘显著，放在 overview figure 中可能造成误导。
- **M4**: Appendix 长达 36 页（pages 10-45），部分关键分析（如 MBR connection, Appendix r; RE 分析, Appendix q）的重要性可能需要在正文中更明确地引导读者关注。
- **M5**: §3.1 "Problem Formulation" 中引入了较多符号（M, x, T, N, y_i, S, r_n），部分符号（如 r_n 作为 per-item signal）在首次出现时定义不够直观，Table 5 的符号表放在附录较远位置。

## 主要优势

1. **概念贡献清晰有价值**：Correlation-selection gap 是一个精准的命名，捕捉了 "quality estimation ≠ quality selection" 这一容易被忽视的关键区别。对任何使用 SC 的 structured prediction 研究者都有实际参考价值。
2. **实验设计全面严谨**：4 个 NER 数据集（SciBERC, CoNLL, Few-NERD, WNUT-17）× 2 模型家族（Qwen2.5, LLaMA-3.1）× 5 个质量信号（SJ, FK, EM, VC, LP），加上温度、N-scaling、seed replication 的系统性消融，构成了高度可信的实证基础。
3. **诊断框架的分解性**：将 gap 归因为 degeneracy + signal alignment collapse 两个可量化条件（而非简单宣称 SC 不起作用），使读者能诊断自己的 use case 是否受影响。Figure 4 的 degeneracy-gain scatter 和 Figure 6 的 degeneracy-LP gain 可视化尤其有效。
4. **理论连接**：MBR decoding 连接（Appendix r）提供了正式框架，Proposition 1-2 和 Corollary 1 为 entity construction 的阈值行为给出了理论依据，提升了论文的深度。
5. **高透明度**：Limitations 中主动披露 Holm p_adj=0.055、MDE≈1.5pp 等对自身不利的统计细节，展现了严谨的学术态度。附录的全面性（bootstrap CI、TOST equivalence、Holm-Bonferroni enumeration、seed replication）远超平均水平。

## Questions for Authors

Q1: 如果增加 seed 数量（从3到5或10），Holm 校正后的 p_adj 是否有望降至 0.05 以下？论文是否考虑过这一路径？
Q2: Landesberg (2026) 的实验是否覆盖了 NER？如果没有，本文是否可以更强调 "NER-specific" 这一角度的独特性？
Q3: Entity-level construction 在 Few-NERD 上表现最好，是否与 Few-NERD 的 fine-grained entity type 特性有关？在 coarse-grained 数据集（如 CoNLL）上 inverse scaling 是否更严重？
Q4: 论文提到 SQL parsing 87.2% degeneracy，但没有进一步分析。是否有计划补充 SQL 的完整诊断？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4916 · 2026-05-25T22:39:56.219143+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待 Reviewer 1 完成 Round 1 初审",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (ARR)\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待 Reviewer 1 完成 Round 1 初审",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (ARR)\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 4917 · 2026-05-25T22:39:56.219629+00:00_

Next wakeup scheduled for 22:43:00 (in 184s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 4918 · 2026-05-25T22:40:08.467763+00:00_

Reviewer 2 初审已收到（3.5 Borderline Conference）。关键发现：
- **N1**: SQL 跨任务证据严重不足，与 abstract 声明不匹配
- **N2**: 全局 Holm p_adj=0.055 边缘显著，核心建设性 claim 支撑不足
- **W1-W4**: Landesberg 差异化不够、结果分散、inverse scaling 解释不足、缺 NER ensemble 文献

等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 375

## Round 375

8 recorded events


### User

_source line 4919 · 2026-05-25T22:40:09.548048+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 一篇方法论严谨的诊断性实证研究，清晰地识别了 correlation-selection gap 作为 NER self-consistency 失败的核心障碍，但理论贡献偏薄（bound 数学上是 trivial 的），且实验范围限制在 7-14B 模型使得结论的外推性存疑。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法（TOST、paired bootstrap、Holm-Bonferroni）使用规范，诊断框架设计合理；但退化分解上界数学上几乎是定义推导，MBR 连接是已有结论的直接应用 |
| Excitement | 3/5 | 问题重要且实际，correlation-selection gap 概念清晰有用，但核心 insight（高退化=无多样性可选）一旦说出并不令人意外，且论文主要是解释失败而非提出有效解决方案 |
| Reproducibility | 4/5 | 代码和数据已公开（footnote 1），超参数详尽（Table 21），实验协议可复现；但仅 2-3 seeds 限制了独立验证的置信度 |
| Reviewer Confidence | 4/5 | 对 structured prediction、self-consistency、MBR decoding、统计检验方法均有较深理解，仔细阅读了全部 45 页 |

## Paper Summary

本文研究为何 self-consistency（SC）在 NER 任务上失效。作者在 4 个 NER 数据集上用 fine-tuned 7-14B 模型定义了 5 种质量估计信号（SJ, LP, FK, EM, VC），发现这些信号虽然能有效估计输出质量（AUROC 最高 0.82），但无法转化为选择增益——论文将此称为 **correlation-selection gap**。通过诊断框架，论文识别出两个共现条件：**退化**（12-68% 实例所有 N 个样本输出相同）和**信号塌缩**（per-sample 信号无法区分相同候选）。论文将 entity construction 与 MBR decoding 建立联系（Proposition 1），提出退化分解上界，并给出三步诊断协议。跨任务扩展（RE、SQL）确认了结构化输出上 frequency-based selection 的普遍失败。

## Must-Fix 问题（影响接收决定）

**N1** [critical] 模型规模限制削弱了广泛性声明的支撑
- 具体位置：Title, §1 (page 1), §8 (page 8), Limitations (page 9)
- 问题：论文标题 "When Self-Consistency Fails for NER" 暗示了对 NER 上 SC 的普遍诊断，但所有实验证据仅来自 Qwen3-8B 和 LLaMA-3.1-8B（7-14B fine-tuned 模型）。论文自身的证据表明退化率是 scale-dependent 的：Few-NERD 在低退化率（23.4%）下获得了 +1.40pp 的选择增益（Table 4）；Appendix v (Table 44) 显示 72B 模型 headroom 为 8.1pp 远高于 8B 的 1.2pp；Limitations 中承认 "frontier models exhibit markedly different degeneracy profiles (8.5-24%)"。这构成了内在张力——诊断框架预测低退化模型应该从 SC 中获益，但论文既没有在低退化模型上验证这一预测，也没有在标题/摘要中限定 scope。一个使用 70B+ 或 GPT-4 级别模型做 NER 的读者无法判断本文结论是否适用。
- 为什么影响接收：这直接关系到论文贡献的 impact——如果核心发现仅适用于中小规模模型的特定退化区间，论文的价值显著降低。
- 建议修改方向：（a）至少在一个大模型（30B+ 或 proprietary model）上验证诊断框架的预测（低退化→SC 增益可观），或（b）将 title/abstract/introduction 的 framing 明确限定为 "fine-tuned 7-14B open-weight models"，并将 "诊断框架在不同退化率下的预测能力" 作为 future work 而非隐含的已验证结论。

**N2** [critical] 退化分解上界（§6.3）作为理论贡献的定位不当
- 具体位置：§6.3 (page 7), Definition 1 & Corollary 1 (Appendix r.3, page 29)
- 问题：上界 $E[\Delta F1] \leq (1-D) \cdot G_{nd} \cdot \alpha$ 的证明（Appendix r.3-r.4）本质上是一个 partition 论证：将实例分为退化（$\Delta F1 = 0$）和非退化两组，非退化组的增益不超过 oracle gap 乘以信号对齐质量。这在数学上几乎是 trivially true——它从退化的定义直接推出。Recovery ratio 3-12%（Table 32, page 29）说明 bound 比实际值宽松 8-33 倍，进一步限制了其预测价值。论文将此定位为 "intentionally loose necessary condition"，但作为一个 Theorem/Corollary 在正文中占据了显著篇幅，对读者来说理论贡献的 expectation 和实际 depth 之间存在 gap。
- 为什么影响接收：论文的理论贡献声明（§6.3 标题 "Degeneracy Decomposition"，Corollary 1 "Critical Degeneracy Threshold"）暗示了非 trivial 的理论洞察，但实际 bound 缺乏 tightness 和 predictive power。
- 建议修改方向：重新定位为 **empirical decomposition framework** 而非理论结果。移除 Theorem/Corollary 的形式化框架，改为在文字中陈述 "退化率 D 乘以信号对齐质量上界限了可能的增益，我们通过实证验证了各因素的贡献比例"。这更诚实地反映了贡献的本质——在于测量 D、G_nd、α 的值并发现 D 是主导因素，而非在于数学推导本身。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Few-NERD 的正面结果与全文 narrative 的张力未被充分利用
- 具体位置：§7.3 (page 8), Table 4 (page 8), Appendix ab (page 37)
- 问题：Few-NERD 在退化率 23.4%（最低）时 LP 选择获得 +1.39pp 增益（Table 4），这实际上是诊断框架最有力的验证——它不仅解释了 SC 何时失败，还预测了 SC 何时能成功。然而论文的整体 framing 偏向 "SC fails"（标题、摘要、§8），未充分利用这一正面验证。Few-NERD 的 entity-type 分析（Appendix ab）较浅，未深入探讨哪些 entity types 或数据特征导致低退化。
- 建议：（a）在 §8 Discussion 中将 Few-NERD 定位为框架预测能力的正面验证，而非仅作为例外提及；（b）补充 Few-NERD 低退化的原因分析（entity type diversity? sentence length? annotation density?），使诊断框架更具 prescriptive value。

**W2** [warning] 2-3 seeds 的统计推断力有限
- 具体位置：§7.4 (page 8), Appendix f (Table 11, page 16), Appendix ad.2 (Table 61, page 40)
- 问题：主要实验使用 2-3 seeds（SciERC 3-seed mean，CoNLL 3-seed），Appendix ad.2 的事后功效分析显示在 n=23（典型配置）下需要 ρ=0.3 才能达到 80% power。虽然 paired bootstrap 在 instance level（n=529 on SciERC）有足够统计量，但 seed-level variance 的估计基于仅 2-3 个数据点，可能低估了系统性变异。Table 11 显示 LP 在 SciERC 上的 95% CI 为 [-0.41, +2.34]——跨零点，意味着即使在最优信号上选择增益也不 significant。
- 建议：至少在一个核心配置（如 SciERC Qwen3-8B）上运行 5 seeds，验证 bootstrap CI 的稳定性和 seed-level variance 的收敛。

**W3** [warning] Holm-Bonferroni 校正的 k 值选择讨论不足
- 具体位置：§7.2 (page 8 footnote), Table 12 (page 23, Appendix f)
- 问题：论文使用 global k=57 和 family-wise k=21 两种校正策略，但未充分讨论选择标准。Global k=57 极为保守（在 57 个 test 中校正），可能导致 type II error 增加——对于一篇以 negative result 为主要贡献的论文，这个方向的 error 尤为重要。Family-wise k 在不同 context 下使用了不同值（k=3 for seed replication, k=21 for families），选择逻辑不够透明。
- 建议：在正文或 Appendix f 中增加一段讨论，说明 family vs. global 校正的选择标准，以及 global k=57 在 negative-result context 下是否过度保守。

**W4** [warning] MBR 连接（§6.1, Proposition 1）的 novelty 声明过高
- 具体位置：§6.1 (page 6), Appendix r.1-r.2 (page 28)
- 问题：Proposition 1 将 entity-level majority vote 与 MBR decoding 在 balanced set-overlap utility 下的等价性建立联系。但 MBR 在 structured prediction 中的应用是已知的（Kumar and Byrne, 2004; Ekema and Aziz, 2022），entity-wise independence 假设下从 MBR 推导 majority vote 是这些已有结果的 straightforward application。论文的 Remark（page 28）承认 "set-level F1 is non-linear and admits no closed-form threshold rule"，但 Proposition 1 本身通过 independence 假设绕过了这一难点——所以实际证明的是一个简化假设下的已知结论。
- 建议：将 Proposition 1 明确定位为 "connecting existing MBR theory to the NER entity construction setting" 而非暗示新的理论贡献。在正文中用一句话说明 entity-wise independence 的局限性及其对实际 threshold 选择的影响。

## 小问题（不影响接收）

- §3.1 (page 3-4): "capability ceiling" 的定义 ("practical performance upper bound achievable through self-consistency at realistic sample budgets N≤16") 中 N≤16 的选择缺乏 justification。为什么不是 N=32 或 N=64？Appendix n (Table 37, page 32) 的 scaling 分析涵盖了 N=4 到 N=32，应在正文中简要说明 N=16 的选择依据。
- §1 (page 1) 脚注 1 提供了代码链接 `https://anonymous.4open.science/r/struct_self_consist_ie-E5D4/`，这在 double-blind review 中是允许的匿名化链接，格式正确。
- Limitations (page 9): "MDE = 1.5pp" 作为核心 negative finding 的检测下限，应在正文 §7 或 §4 中首次出现时就明确说明，而非仅在 Limitations 中提及。
- Table 3 (page 6): 9 种方法的 ΔF1 汇总非常密集，考虑在正文中用 bar chart 替代以提高可读性。
- Figure 1 (page 3): 整体设计清晰有效，但右侧 "+1.4 pp" 的 annotation 仅适用于 Few-NERD，可能误导读者以为是跨数据集的一般结论。

## 主要优势

1. **Correlation-selection gap 概念清晰有力**：将质量估计能力（AUROC）与选择增益之间的脱节命名并系统分析，为理解 structured SC 的失败提供了一个 reusable 的诊断框架。这比简单报告 "SC doesn't work for NER" 有更高的分析价值。

2. **统计方法论达到同行评审标准的上限**：TOST 等效性检验用于支持 negative claims、paired bootstrap 用于效应量估计、Holm-Bonferroni 用于多重比较校正——这在 NLP 实证研究中是少见的严谨度。Table 12 完整枚举 k=57 个统计检验的做法值得推广。

3. **信号分类学设计周密**：5 种信号（SJ, LP, FK, EM, VC）覆盖了 per-sample vs. instance-level、structural vs. probabilistic 的二维空间（Table 5），使得不同信号的失败模式可以被独立分析。LP 作为唯一产生正面选择增益的信号（§4, Table 2）的发现有实际指导意义。

4. **实验覆盖度高**：45 页 appendix 提供了极为详尽的消融分析——温度敏感性（Appendix b）、样本量 scaling（Appendix n）、cross-dataset OOD（Appendix x）、free-form decoding（Appendix s）、calibration 分析（Appendix c）、entity-level verifier transfer（Appendix h.2）、few-shot 对比（Appendix ad.10）等。几乎每一个合理的质疑都能在 appendix 中找到对应分析。

5. **诊断协议（§ae）具有实践价值**：三步协议（测量退化 → 评估信号对齐 → 选择聚合策略）为 practitioners 提供了 actionable guidance，使论文贡献超越了纯分析。

6. **Entity construction 与 MBR 的连接（§6.1）**虽然理论 novelty 有限，但首次在 NER context 中明确建立了这一联系，使 entity-level majority vote 的 threshold 选择有了原则性依据。

## Questions to Authors

Q1: Few-NERD 退化率（23.4%）显著低于其他数据集（SciERC 42%, CoNLL 62%, WNUT-17 87%），诊断框架预测低退化→SC 增益可观。**是否可以人工构造一个 "低退化" 测试场景**（例如通过增加 prompt diversity 或使用更高温度来降低退化率），验证框架的预测方向？

Q2: Appendix v (Table 44) 显示 72B 模型 headroom 为 8.1pp vs 8B 的 1.2pp。**72B 模型的退化率是多少？**如果退化率确实更低，这将直接验证论文的核心机制。

Q3: 论文使用 gold-filtered evaluation（排除无 gold annotation 的实例）。**如果使用 full evaluation set（包含 zero-entity 实例），退化率和 correlation-selection gap 会如何变化？** 零实体实例天然是 "退化" 的（大部分样本预测为空），可能会 inflate 退化率数字。

Q4: Corollary 1 给出 critical degeneracy threshold $D < 1 - 1/(G_{nd} \cdot \alpha)$。**Table 32 中有多少配置实际低于这个 threshold？**如果大部分配置都远高于 threshold，这说明 bound 的 prescriptive value 有限。


---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：评分 **3.5 (Borderline Conference)**。论文的 correlation-selection gap 概念和诊断框架（degeneracy + signal alignment collapse）有实际价值，实验设计全面（4数据集×2模型×5信号），透明度高。但存在三个核心问题：(1) SQL 跨任务证据仅一个数字，与 abstract 的 claim 不匹配；(2) LP selection 增益在全局 Holm 校正下 p_adj=0.055，未达显著性阈值；(3) Landesberg (2026) 的 concurrent discovery 显著削弱新颖性。建议降级 SQL 声明、增加统计功效、扩展 concurrent work 差异化讨论。

---

[Reviewer 1 审稿结果]:
审稿完成。总结：

- **Overall: 3.5 (Borderline Conference)**
- **2 个 Must-Fix**：(1) 模型规模限于 7-14B，标题/framing 与实验 scope 不匹配，核心机制（退化率）的 scale-dependence 未在大模型上验证；(2) §6.3 退化分解上界数学上 trivial（partition 定义直接推出），应重新定位为 empirical decomposition 而非 theorem
- **4 个 Should-Fix**：Few-NERD 正面结果未被充分利用为框架验证、2-3 seeds 统计推断力有限、Holm-Bonferroni k 值选择讨论不足、MBR 连接 novelty 声明过高
- **核心优势**：correlation-selection gap 概念清晰有力、统计方法论严谨（TOST/bootstrap/Holm-Bonferroni）、5 信号分类学设计周密、45 页 appendix 覆盖度极高、三步诊断协议有实践价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---
