# Director coordination — Part 1 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 1

## Round 1

16 recorded events


### User

_source line 1 · 2026-05-14T12:11:44.846919+00:00_

[Reviewer 1 审稿意见]:
## R1 审稿意见：方法与实验

### 总体评分
**Overall Assessment**: 3/5 (Findings) | Director 1-6 scale: **4/6** (Weak Accept, borderline Findings)
**一句话总结**: 实验覆盖面广、诊断分析有深度的 empirical study，但模型规模单一（仅 8B）、零图表的呈现方式、以及误导性的成本分析共同削弱了核心主张的说服力。

### ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法论合理，评估协议（4 指标 + LOO circularity check）良好；但成本分析存在误导，仅 2 个 8B 模型限制普适性 |
| Excitement | 3/5 | 研究问题及时（TTS for structured IE），compound error boundary 有启发性；但贡献以 empirical comparison 为主 |
| Reproducibility | 4/5 | 数据集公开、参数详尽；但未发布代码，prompt 模板未给出 |
| Confidence | 4/5 | 熟悉 NER/RE 评估和 TTS 方法 |

---

### 主要优势

**S1. 系统且全面的实验矩阵**
5 种 signal × 3 NER 数据集 × 1 RE 数据集 × 2 模型 × 2 采样预算 × 2 温度 × 4 评估指标。15 个计划实验中 13/15 完整覆盖，2/15 部分覆盖（adaptive_compute_demo 隐含在 Section 5.2/5.5 但无显式 adaptive 策略；selection_curves 数据在 Table 8 但以表格呈现）。该领域首个如此系统的比较。

**S2. LOO-SJ circularity check 是方法论亮点**
Table 1 中 Leave-one-out SJ（ρ=0.40, Δ=0.02 vs full SJ ρ=0.42）证明 SJ 有效性不依赖于自我循环。严谨。

**S3. Compound error boundary 诊断有理论价值**
Section 5.9 识别 RE 中所有 signal 退化（ρ < 0.28）的根因是 compound error propagation（head + tail + relation type 三重叠加），Table 12 per-relation-type 分析提供具体证据。

**S4. 多维度鲁棒性验证**
Multi-seed（Table 2, Std ≤ 0.01）、cross-dataset（Table 4, 排序一致）、cross-model（Table 5）、OOD（Table 17, SJ-LP gap 从 +0.15 降至 +0.12 但仍显著）。

**S5. Inverted-U pattern（Section 5.11, Table 15）**
SJ ρ 在 F1 bucket [0.3, 0.7] 最高（ρ ≈ 0.45），极端区间下降。为 SJ 适用条件提供直觉。

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] 模型规模单一，严重限制普适性
- Section 4, Section 7
- 仅 Qwen3-8B 和 LLaMA-3.1-8B 两个 8B 模型。confidence calibration 和 output diversity 随模型规模变化显著。更大模型的 greedy 可能已足够准确（LP 优势更明显），更小模型高方差可能放大 SJ 优势。Abstract 中 "establish" 措辞过强。
- 建议：至少增加一个 >30B 或 <3B 模型，或降级措辞。

**N2** [critical] 成本分析系统性误导
- Section 6 "Practical implications"
- 称 SJ 额外成本 "negligible (O(N²) set comparisons vs. O(N) LLM forward passes)"，但忽略 LP 可在 greedy decode（1 pass）上工作，而 SJ 需要 N≥8 pass。公平对比：LP@N=1 → ρ≈0.26; SJ@N=8 → 8× cost → ρ≈0.38; SJ@N=16 → 16× cost → ρ≈0.42。将 8-16× 推理开销描述为 "negligible" 是不准确的。
- 建议：增加 cost-effectiveness 分析（F1 gain per unit compute）。

**N3** [critical] 全文零图表
- 17 个表格，0 个 Figure。对 confidence/calibration 研究而言，缺少 selection curves、reliability diagrams、cost-effectiveness scatter 是严重呈现缺陷。Table 8 有 selection curve 数据但以表格呈现。
- 建议：至少添加 3 个核心 Figure。

---

### Should-Fix 问题

**W1** [warning] 未探索 signal combination
- Section 5.8 发现 SJ 和 LP 互补（NER Δρ=0.14），但未尝试任何组合策略。
- 建议：至少尝试 α·SJ + (1-α)·LP 线性组合。

**W2** [warning] 单一 prompt 模板，缺乏 prompt sensitivity
- Section 4 未提及 prompt 变体。LLM-based IE 输出格式直接影响 set-based 指标。
- 建议：appendix 中给出完整 prompt，讨论 format 影响。

**W3** [warning] RE 仅有 SciERC 一个数据集
- NER 有 3 个跨域数据集，RE 只有 1 个。"universal bottleneck" 主张建立在单一数据集上。
- 建议：增加至少一个 RE 数据集或降级措辞。

**W4** [warning] 统计检验不系统
- Section 5.1 提到 p < 10⁻¹⁵，但 Table 4/5 的 cross-dataset/cross-model 比较无检验。3 seed 的 std 不能替代正式统计检验。
- 建议：对核心比较报告 bootstrap 95% CI。

**W5** [warning] 缺少 SJ 失败案例分析
- SJ ρ 最佳也仅 0.42-0.51。未分析高 SJ 低 F1（模型一致地错）或低 SJ 高 F1 的失败模式。
- 建议：增加 error analysis subsection。

---

### 小问题
- 标题 "Log-Probability Is All You Need?" 暗示答案为 yes，但实际结论为 no。建议改为 "Beyond Log-Probability: ..."。
- Table 16（Appendix）entity count 6+ 时 SJ ρ 降至 0.34，未解释原因。
- Eq.(1) SJ 的 similarity kernel（token-level overlap 的具体方式）未明确。
- adaptive_compute_demo 实验无显式 adaptive 策略呈现。

### 15 个实验覆盖度
13/15 完整覆盖，2/15 部分覆盖（adaptive_compute_demo、selection_curves）。

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

_source line 2 · 2026-05-14T12:12:00.486506+00:00_

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

_source line 3 · 2026-05-14T12:12:02.856172+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 2369
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-14T12:12:02.906835+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-14T12:12:02.958330+00:00_



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

_source line 6 · 2026-05-14T12:12:08.934773+00:00_

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

_source line 7 · 2026-05-14T12:12:09.438401+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (26 个)\n\n- **exp_015_metrics_expansion**: QUEUED — \n- **exp_005**: DONE (success) — \n- **exp_007_ner_llama**: PREPARING — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_001_n16_seed456 | — | — | — | — |\n| exp_001_n16_seed123 | — | — | — | — |\n| exp_008_re_n16 | — | — | — | — |\n\n## 待处理\n- exp_015_metrics_expansion（排队等待 GPU）\n- exp_007_ner_multi_model（已分配 autodl-5090 GPU:cuda:3，等待提交）\n- exp008_re_n16（准备中）\n- exp001_seed456（准备中）\n- exp001_seed123（准备中）\n- exp_007_ner_llama（准备中）\n\n## 近期结论\n- **exp_001_ner_n16_scierc** (success): —\n  [exp001_n16_samples](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_001_ner_n16_scierc/data/exp001_n16_samples_pointer.txt) | [exp001_all_signals_report](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_001_ner_n16_scierc/report/exp001_all_signals_summary.txt)\n- **exp_004_re_diagnostic** (success): —\n  [exp004_re_diagnostic_report](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_004_re_diagnostic/report/analyze_exp004_re_diagnostic.py)\n- **exp_005** (success): —\n  [exp005_temperature_analysis](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_005/report/summary.md)\n\n## 趋势\n成功 7 / 负向 6 / 失败 1 / 共 15\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:
…[truncated 112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-14T12:12:09.540146+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "review_issues.yaml",
  "max_chars": "12000"
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
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-14T12:12:09.590785+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

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

_source line 10 · 2026-05-14T12:12:27.565391+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 11 · 2026-05-14T12:12:27.666240+00:00_

No matching deferred tools found

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

_source line 12 · 2026-05-14T12:12:31.836588+00:00_

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

_source line 13 · 2026-05-14T12:12:32.288602+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.

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

_source line 14 · 2026-05-14T12:12:32.539952+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
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
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-14T12:12:32.590950+00:00_

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


### Assistant

_source line 16 · 2026-05-14T12:12:53.312703+00:00_

**R1 审稿意见已收到。**

R1 侧重方法与实验，给出 4/6（Weak Accept, borderline Findings），提出 3 个 critical 问题：
- **N1**: 模型规模单一（仅 8B），普适性不足
- **N2**: 成本分析误导（8-16× 推理开销被称 "negligible"）
- **N3**: 全文零图表，呈现缺陷严重

另有 5 个 should-fix（signal combination、prompt sensitivity、RE 数据集单一、统计检验不系统、SJ 失败案例缺失）。

等待 R2（新颖性/完整性侧重）审稿意见返回后，启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 2

## Round 2

6 recorded events


### User

_source line 17 · 2026-05-14T12:12:54.540199+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：本文在方法与实验维度上给出 **Overall 3/5 (Findings) / Director scale 4/6 (Weak Accept)**。核心优势是系统的实验矩阵（13/15 实验覆盖）、LOO circularity check、compound error boundary 诊断。三个 critical 问题：(1) 仅 8B 模型限制了 "establish best practice" 主张的普适性；(2) 成本分析将 8-16× 推理开销描述为 "negligible" 属于误导；(3) 全文零图表不符合 confidence/calibration 研究惯例。

---

[Reviewer 2 审稿意见]:
## R2 审稿完成：新颖性与相关工作

**论文**: "Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"

---

## 总体评分
**Overall**: 3/5 (Findings)
**一句话总结**: 实验设计扎实的经验研究，但方法新颖性有限（SJ 是评估指标的自然迁移），RE 上的 task-complexity boundary claim 仅由单一数据集支撑，相关工作存在显著遗漏。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | NER claims 有多 seed + 多数据集 + p-value 支撑；RE complexity boundary 仅基于 SciERC 一个数据集(n=397)，证据链不完整 |
| Excitement | 2.5/5 | 研究问题实用，但核心发现（set-level agreement > sequence-level log-prob）对领域内可预期；"diagnostic framework" 实为标准消融包装 |
| Overall | 3/5 | Findings 水平——有用的经验贡献但不够 Main 的新颖性门槛 |
| Reproducibility | 4/5 | 方法清晰、超参明确、多 seed，但未提供代码 |
| Confidence | 4/5 | 熟悉 self-consistency、calibration、NER/RE 文献 |

## Must-Fix 问题

**N1** [critical] 方法新颖性有限——SJ 是 IE 评估指标到 confidence 的自然迁移
- Section 3.2, Eq(1): type-grouped Hungarian matching + token-overlap kernel 本质是 set-level F1/Jaccard 的 confidence 版本
- 未提供理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融

**N2** [critical] Task-complexity boundary 证据严重不足
- Section 5.9, Table 12: 全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行
- "Universal bottleneck" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis

**N3** [critical] 相关工作显著遗漏
- **Guo et al. 2017** (On Calibration of Modern Neural Networks, ICML) — 论文讨论 ECE 但未引用定义 ECE 的奠基论文
- **Snell et al. 2024** (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却未引用该核心工作
- **Aggarwal et al. 2023** (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling (Section 5.2) 直接相关
- **CISC** (Huang et al. 2025, Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 "最 calibrated 的方法反而最无效"，直接挑战本文解读
- **传统 IE confidence** — CRF 边际概率、span-level confidence、MC-dropout uncertainty 完全未讨论

**N4** [critical] 标题与核心发现不匹配
- "Log-Probability Is All You Need?" 暗示 log-prob 可能足够，但论文核心发现是 SJ 显著优于 log-prob (Δρ=0.16, p<10⁻²⁵)
- 修辞反问制造阅读期望与实际结论的认知冲突

## Should-Fix 问题

**W1** [warning] 仅 2 个 8B 模型，70B+ 模型的 calibration 可能改变 SJ vs log-prob 的差距
**W2** [warning] 未比较任何 trained approach (verifier/reward model/learned combination)
**W3** [warning] "Diagnostic framework" 过度包装——实际是标准 error analysis (F1 分桶、component 分解、stratification)
**W4** [warning] 全文 17 张表 0 张图，可读性差
**W5** [warning] Exact-Match Voting 对结构化输出是 straw man baseline

## 小问题
- Abstract 有 "?" 未解析引用
- 仅英语数据集
- 温度敏感性分析仅 T=0.7 和 T=1.0 两点

## 主要优势
- **S1**: 研究问题清晰且有实际意义
- **S2**: 实验设计系统化（3 dataset × 2 model × 2 budget × 4 metric × 3 seed）
- **S3**: SJ 的 Hungarian matching 设计合理，leave-one-out 验证排除 circularity
- **S4**: Best-of-N selection 将 ranking → F1 gain，实用性强
- **S5**: 消融维度全面（N-scaling、cross-dataset、cross-model、temperature、OOD、stratification）

## 对 Director 问题的回应

**1. "首个系统比较" claim 是否成立？**
基本成立但需限定。在 {LLM-based IE} × {多种 confidence signals} × {best-of-N selection} 这个交叉点上，我未找到直接先驱工作。但论文忽略了：(a) 传统 IE 的 confidence 估计传统；(b) reasoning 任务上的类似比较（CISC 等）。建议改为 "first systematic comparison for LLM-based structured IE"。

**2. 负面结果信息量？**
需要澄清：论文的核心发现实际上是 **正面结果**（SJ > log-prob），不是 Director 概要中说的 "consistency 不优于 log-probability"。RE 上的退化是次要发现，且仅单数据集支撑。负面结果（RE 退化）的可预测性中等——compound error 对有 IE 经验的人不意外，但系统量化有一定价值。

**3. Diagnostic framework 贡献是否充分？**
不充分。这些是标准消融技术（分桶、分层、component 分解），不构成可复用的 framework。建议降格为 "diagnostic analysis"。

**4. EMNLP 定位？**
Findings 可接受，Main 偏弱。论文的实用价值（practitioners 的 confidence signal 选择指南）适合 Findings 定位，但方法新颖性和 claim 覆盖不足以支撑 Main。

---

[Reviewer 2 审稿结果]:
审稿已完成并提交给 Review Director。

核心判断：**Overall 3/5 (Findings)**。4 个 Must-Fix 问题中最关键的是——(1) SJ 方法新颖性有限（评估指标到 confidence 的自然迁移），(2) RE task-complexity boundary 仅由 SciERC 一个数据集支撑无法称 "universal"，(3) 5 篇重要参考文献缺失（Guo 2017、Snell 2024、Aggarwal 2023、CISC 2025、传统 IE confidence），(4) 标题暗示 log-prob 足够但论文实际证明 SJ 大幅优于 log-prob，存在 framing 冲突。

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

_source line 18 · 2026-05-14T12:13:45.281696+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性与相关工作方向）的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## R2 审稿意见：新颖性与相关工作\n\n### 总体评分\n**Overall**: 3/5 (Findings)\n**一句话总结**: 实验设计扎实的经验研究，但方法新颖性有限（SJ 是评估指标的自然迁移），RE 上的 task-complexity boundary claim 仅由单一数据集支撑，相关工作存在显著遗漏。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | NER claims 有多 seed + 多数据集 + p-value 支撑；RE complexity boundary 仅基于 SciERC 一个数据集(n=397)，证据链不完整 |\n| Excitement | 2.5/5 | 研究问题实用，但核心发现（set-level agreement > sequence-level log-prob）对领域内可预期；\"diagnostic framework\" 实为标准消融包装 |\n| Overall | 3/5 | Findings 水平——有用的经验贡献但不够 Main 的新颖性门槛 |\n| Reproducibility | 4/5 | 方法清晰、超参明确、多 seed，但未提供代码 |\n| Confidence | 4/5 | 熟悉 self-consistency、calibration、NER/RE 文献 |\n\n### Must-Fix 问题\n\n**N1** [critical] 方法新颖性有限——SJ 是 IE 评估指标到 confidence 的自然迁移\n- Section 3.2, Eq(1): type-grouped Hungarian matching + token-overlap kernel 本质是 set-level F1/Jaccard 的 confidence 版本\n- 未提供理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融\n\n**N2** [critical] Task-complexity boundary 证据严重不足\n- Section 5.9, Table 12: 全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行\n- \"Universal bottleneck\" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis\n\n**N3** [critical] 相关工作显著遗漏\n- **Guo et al. 2017** (On Calibration of Modern Neural Networks, ICML) — 论文讨论 ECE 但未引用定义 ECE 的奠基论文\n- **Snell et al. 2024** (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却未引用该核心工作\n- **Aggarwal et al. 2023** (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling (Section 5.2) 直接相关\n- **CISC** (Huang et al. 2025, Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 \"最 calibrated 的方法反而最无效\"，直接挑战本文解读\n- **传统 IE confidence** — CRF 边际概率、span-level confidence、MC-dropout uncertainty 完全未讨论\n\n**N4** [critical] 标题与核心发现不匹配\n- \"Log-Probability Is All You Need?\" 暗示 log-prob 可能足够，但论文核心发现是 SJ 显著优于 log-prob (Δρ=0.16, p<10⁻²⁵)\n- 修辞反问制造阅读期望与实际结论的认知冲突\n\n### Should-Fix 问题\n\n**W1** [warning] 仅 2 个 8B 模型，70B+ 模型的 calibration 可能改变 SJ vs log-prob 的差距\n**W2** [warning] 未比较任何 trained approach (verifier/reward model/learned combination)\n**W3** [warning] \"Diagnostic framework\" 过度包装——实际是标准 error analysis (F1 分桶、component 分解、stratification)\n**W4** [warning] 全文 17 张表 0 张图，可读性差\n**W5** [warning] Exact-Match Voting 对结构化输出是 straw man baseline\n\n### 小问题\n- Abstract 有 \"?\" 未解析引用\n- 仅英语数据集\n- 温度敏感性分析仅 T=0.7 和 T=1.0 两点\n\n### 主要优势\n- S1: 研究问题清晰且有实际意义\n- S2: 实验设计系统化\n- S3: SJ 的 Hungarian matching 设计合理，leave-one-out 验证排除 circularity\n- S4: Best-of-N selection 将 ranking → F1 gain，实用性强\n- S5: 消融维度全面\n\n### 对 Director 问题的回应\n\n**1. \"首个系统比较\" claim 是否成立？**\n基本成立但需限定。建议改为 \"first systematic comparison for LLM-based structured IE\"。\n\n**2. 负面结果信息量？**\n论文核心发现实际上是正面结果（SJ > log-prob）。RE 退化是次要发现，仅单数据集支撑。\n\n**3. Diagnostic framework 贡献是否充分？**\n不充分。标准消融技术不构成可复用 framework。建议降格为 \"diagnostic analysis\"。\n\n**4. EMNLP 定位？**\nFindings 可接受，Main 偏弱。\n\n---\n\n请对以上每个 Must-Fix（N1-N4）、Should-Fix（W1-W5）和小问题逐条给出 [AGREE] 或 [REBUT] 回应。"
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
    "text": "## 交叉分享：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性与相关工作方向）的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## R2 审稿意见：新颖性与相关工作\n\n### 总体评分\n**Overall**: 3/5 (Findings)\n**一句话总结**: 实验设计扎实的经验研究，但方法新颖性有限（SJ 是评估指标的自然迁移），RE 上的 task-complexity boundary claim 仅由单一数据集支撑，相关工作存在显著遗漏。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | NER claims 有多 seed + 多数据集 + p-value 支撑；RE complexity boundary 仅基于 SciERC 一个数据集(n=397)，证据链不完整 |\n| Excitement | 2.5/5 | 研究问题实用，但核心发现（set-level agreement > sequence-level log-prob）对领域内可预期；\"diagnostic framework\" 实为标准消融包装 |\n| Overall | 3/5 | Findings 水平——有用的经验贡献但不够 Main 的新颖性门槛 |\n| Reproducibility | 4/5 | 方法清晰、超参明确、多 seed，但未提供代码 |\n| Confidence | 4/5 | 熟悉 self-consistency、calibration、NER/RE 文献 |\n\n### Must-Fix 问题\n\n**N1** [critical] 方法新颖性有限——SJ 是 IE 评估指标到 confidence 的自然迁移\n- Section 3.2, Eq(1): type-grouped Hungarian matching + token-overlap kernel 本质是 set-level F1/Jaccard 的 confidence 版本\n- 未提供理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融\n\n**N2** [critical] Task-complexity boundary 证据严重不足\n- Section 5.9, Table 12: 全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行\n- \"Universal bottleneck\" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis\n\n**N3** [critical] 相关工作显著遗漏\n- **Guo et al. 2017** (On Calibration of Modern Neural Networks, ICML) — 论文讨论 ECE 但未引用定义 ECE 的奠基论文\n- **Snell et al. 2024** (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却未引用该核心工作\n- **Aggarwal et al. 2023** (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling (Section 5.2) 直接相关\n- **CISC** (Huang et al. 2025, Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 \"最 calibrated 的方法反而最无效\"，直接挑战本文解读\n- **传统 IE confidence** — CRF 边际概率、span-level confidence、MC-dropout uncertainty 完全未讨论\n\n**N4** [critical] 标题与核心发现不匹配\n- \"Log-Probability Is All You Need?\" 暗示 log-prob 可能足够，但论文核心发现是 SJ 显著优于 log-prob (Δρ=0.16, p<10⁻²⁵)\n- 修辞反问制造阅读期望与实际结论的认知冲突\n\n### Should-Fix 问题\n\n**W1** [warning] 仅 2 个 8B 模型，70B+ 模型的 calibration 可能改变 SJ vs log-prob 的差距\n**W2** [warning] 未比较任何 trained approach (verifier/reward model/learned combination)\n**W3** [warning] \"Diagnostic framework\" 过度包装——实际是标准 error analysis (F1 分桶、component 分解、stratification)\n**W4** [warning] 全文 17 张表 0 张图，可读性差\n**W5** [warning] Exact-Match Voting 对结构化输出是 straw man baseline\n\n### 小问题\n- Abstract 有 \"?\" 未解析引用\n- 仅英语数据集\n- 温度敏感性分析仅 T=0.7 和 T=1.0 两点\n\n### 主要优势\n- S1: 研究问题清晰且有实际意义\n- S2: 实验设计系统化\n- S3: SJ 的 Hungarian matching 设计合理，leave-one-out 验证排除 circularity\n- S4: Best-of-N selection 将 ranking → F1 gain，实用性强\n- S5: 消融维度全面\n\n### 对 Director 问题的回应\n\n**1. \"首个系统比较\" claim 是否成立？**\n基本成立但需限定。建议改为 \"first systematic comparison for LLM-based structured IE\"。\n\n**2. 负面结果信息量？**\n论文核心发现实际上是正面结果（SJ > log-prob）。RE 退化是次要发现，仅单数据集支撑。\n\n**3. Diagnostic framework 贡献是否充分？**\n不充分。标准消融技术不构成可复用 framework。建议降格为 \"diagnostic analysis\"。\n\n**4. EMNLP 定位？**\nFindings 可接受，Main 偏弱。\n\n---\n\n请对以上每个 Must-Fix（N1-N4）、Should-Fix（W1-W5）和小问题逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-14T12:14:18.170272+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32888
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-14T12:14:18.322377+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法与实验方向）的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 特别关注你与 R1 是否在相同问题上有不同判断\n\n---\n\n## R1 审稿意见：方法与实验\n\n### 总体评分\n**Overall Assessment**: 3/5 (Findings) | Director 1-6 scale: **4/6** (Weak Accept, borderline Findings)\n**一句话总结**: 实验覆盖面广、诊断分析有深度的 empirical study，但模型规模单一（仅 8B）、零图表的呈现方式、以及误导性的成本分析共同削弱了核心主张的说服力。\n\n### ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心方法论合理，评估协议良好；但成本分析存在误导，仅 2 个 8B 模型限制普适性 |\n| Excitement | 3/5 | 研究问题及时，compound error boundary 有启发性；但贡献以 empirical comparison 为主 |\n| Reproducibility | 4/5 | 数据集公开、参数详尽；但未发布代码，prompt 模板未给出 |\n| Confidence | 4/5 | 熟悉 NER/RE 评估和 TTS 方法 |\n\n### 主要优势\n\n**S1.** 系统且全面的实验矩阵（5 signal × 3 NER dataset × 1 RE dataset × 2 model × 2 budget × 2 temp × 4 metric，13/15 完整覆盖）\n**S2.** LOO-SJ circularity check 是方法论亮点（Table 1, ρ=0.40 vs full SJ ρ=0.42）\n**S3.** Compound error boundary 诊断有理论价值（Section 5.9, Table 12）\n**S4.** 多维度鲁棒性验证（multi-seed, cross-dataset, cross-model, OOD）\n**S5.** Inverted-U pattern（Section 5.11, Table 15）为 SJ 适用条件提供直觉\n\n### Must-Fix 问题\n\n**N1** [critical] 模型规模单一，严重限制普适性\n- 仅 Qwen3-8B 和 LLaMA-3.1-8B 两个 8B 模型\n- 更大模型的 greedy 可能已足够准确（LP 优势更明显），更小模型高方差可能放大 SJ 优势\n- Abstract 中 \"establish\" 措辞过强\n- 建议：至少增加一个 >30B 或 <3B 模型，或降级措辞\n\n**N2** [critical] 成本分析系统性误导\n- Section 6: 称 SJ 额外成本 \"negligible (O(N²) set comparisons vs. O(N) LLM forward passes)\"\n- 忽略 LP 可在 greedy decode（1 pass）上工作，SJ 需要 N≥8 pass\n- 公平对比：LP@N=1 → ρ≈0.26; SJ@N=8 → 8× cost → ρ≈0.38; SJ@N=16 → 16× cost → ρ≈0.42\n- 将 8-16× 推理开销描述为 \"negligible\" 是不准确的\n- 建议：增加 cost-effectiveness 分析\n\n**N3** [critical] 全文零图表\n- 17 个表格，0 个 Figure\n- 缺少 selection curves、reliability diagrams、cost-effectiveness scatter\n- Table 8 有 selection curve 数据但以表格呈现\n- 建议：至少添加 3 个核心 Figure\n\n### Should-Fix 问题\n\n**W1** [warning] 未探索 signal combination（Section 5.8, SJ 和 LP 互补 Δρ=0.14）\n**W2** [warning] 单一 prompt 模板，缺乏 prompt sensitivity 分析\n**W3** [warning] RE 仅有 SciERC 一个数据集，\"universal bottleneck\" 主张建立在单一数据集上\n**W4** [warning] 统计检验不系统（3 seed std 不替代正式 bootstrap CI）\n**W5** [warning] 缺少 SJ 失败案例分析（高 SJ 低 F1 / 低 SJ 高 F1 的模式）\n\n### 小问题\n- 标题暗示答案为 yes，但实际结论为 no\n- Table 16 entity count 6+ 时 SJ ρ 降至 0.34 未解释\n- Eq.(1) SJ 的 similarity kernel 未明确\n- adaptive_compute_demo 无显式 adaptive 策略呈现\n\n---\n\n请对以上每个 Must-Fix（N1-N3）、Should-Fix（W1-W5）和小问题逐条给出 [AGREE] 或 [REBUT] 回应。"
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
    "text": "## 交叉分享：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法与实验方向）的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 特别关注你与 R1 是否在相同问题上有不同判断\n\n---\n\n## R1 审稿意见：方法与实验\n\n### 总体评分\n**Overall Assessment**: 3/5 (Findings) | Director 1-6 scale: **4/6** (Weak Accept, borderline Findings)\n**一句话总结**: 实验覆盖面广、诊断分析有深度的 empirical study，但模型规模单一（仅 8B）、零图表的呈现方式、以及误导性的成本分析共同削弱了核心主张的说服力。\n\n### ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心方法论合理，评估协议良好；但成本分析存在误导，仅 2 个 8B 模型限制普适性 |\n| Excitement | 3/5 | 研究问题及时，compound error boundary 有启发性；但贡献以 empirical comparison 为主 |\n| Reproducibility | 4/5 | 数据集公开、参数详尽；但未发布代码，prompt 模板未给出 |\n| Confidence | 4/5 | 熟悉 NER/RE 评估和 TTS 方法 |\n\n### 主要优势\n\n**S1.** 系统且全面的实验矩阵（5 signal × 3 NER dataset × 1 RE dataset × 2 model × 2 budget × 2 temp × 4 metric，13/15 完整覆盖）\n**S2.** LOO-SJ circularity check 是方法论亮点（Table 1, ρ=0.40 vs full SJ ρ=0.42）\n**S3.** Compound error boundary 诊断有理论价值（Section 5.9, Table 12）\n**S4.** 多维度鲁棒性验证（multi-seed, cross-dataset, cross-model, OOD）\n**S5.** Inverted-U pattern（Section 5.11, Table 15）为 SJ 适用条件提供直觉\n\n### Must-Fix 问题\n\n**N1** [critical] 模型规模单一，严重限制普适性\n- 仅 Qwen3-8B 和 LLaMA-3.1-8B 两个 8B 模型\n- 更大模型的 greedy 可能已足够准确（LP 优势更明显），更小模型高方差可能放大 SJ 优势\n- Abstract 中 \"establish\" 措辞过强\n- 建议：至少增加一个 >30B 或 <3B 模型，或降级措辞\n\n**N2** [critical] 成本分析系统性误导\n- Section 6: 称 SJ 额外成本 \"negligible (O(N²) set comparisons vs. O(N) LLM forward passes)\"\n- 忽略 LP 可在 greedy decode（1 pass）上工作，SJ 需要 N≥8 pass\n- 公平对比：LP@N=1 → ρ≈0.26; SJ@N=8 → 8× cost → ρ≈0.38; SJ@N=16 → 16× cost → ρ≈0.42\n- 将 8-16× 推理开销描述为 \"negligible\" 是不准确的\n- 建议：增加 cost-effectiveness 分析\n\n**N3** [critical] 全文零图表\n- 17 个表格，0 个 Figure\n- 缺少 selection curves、reliability diagrams、cost-effectiveness scatter\n- Table 8 有 selection curve 数据但以表格呈现\n- 建议：至少添加 3 个核心 Figure\n\n### Should-Fix 问题\n\n**W1** [warning] 未探索 signal combination（Section 5.8, SJ 和 LP 互补 Δρ=0.14）\n**W2** [warning] 单一 prompt 模板，缺乏 prompt sensitivity 分析\n**W3** [warning] RE 仅有 SciERC 一个数据集，\"universal bottleneck\" 主张建立在单一数据集上\n**W4** [warning] 统计检验不系统（3 seed std 不替代正式 bootstrap CI）\n**W5** [warning] 缺少 SJ 失败案例分析（高 SJ 低 F1 / 低 SJ 高 F1 的模式）\n\n### 小问题\n- 标题暗示答案为 yes，但实际结论为 no\n- Table 16 entity count 6+ 时 SJ ρ 降至 0.34 未解释\n- Eq.(1) SJ 的 similarity kernel 未明确\n- adaptive_compute_demo 无显式 adaptive 策略呈现\n\n---\n\n请对以上每个 Must-Fix（N1-N3）、Should-Fix（W1-W5）和小问题逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-14T12:14:19.891668+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1569
}
```

</details>

---


### Assistant

_source line 22 · 2026-05-14T12:14:32.910731+00:00_

交叉分享任务已分发。当前状态：

**Round 1 初审汇总：**
- **R1（方法与实验）**: 3/5 Findings, 4/6 Weak Accept — 3 critical（模型规模单一、成本分析误导、零图表）
- **R2（新颖性与相关工作）**: 3/5 Findings — 4 critical（方法新颖性有限、RE boundary 证据不足、5 篇重要文献缺失、标题 framing 冲突）

**两位 Reviewer 的共识区域（初步观察）：**
- 模型仅 8B 限制普适性（R1-N1, R2-W1）
- RE 仅 SciERC 单数据集（R1-W3, R2-N2）
- 零图表可读性差（R1-N3, R2-W4）
- 总体定位：Findings 可接受，Main 偏弱

**潜在分歧点：**
- R1 给 Excitement 3/5，R2 给 2.5/5（R2 认为核心发现可预期）
- R1 将成本分析列为 critical，R2 未单独提及
- R2 将方法新颖性和文献遗漏列为 critical，R1 未涉及

等待两位 Reviewer 的交叉回应后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 23 · 2026-05-14T12:16:48.821029+00:00_

[Reviewer 1 审稿意见]:
## R1 对 R2 的交叉回应

### Must-Fix

**[AGREE] R2-N1: SJ 新颖性有限**
同意。SJ 是 set-level Jaccard 的直接 confidence 化应用。论文定位为 empirical study 但措辞（"establish", "diagnostic framework"）暗示更高原创性。补充：缺少 similarity kernel 消融（token overlap vs edit distance vs embedding cosine），这同时是实验完备性问题。

**[AGREE] R2-N2: Task-complexity boundary 证据不足**
完全同意（与 R1-W3 一致）。SciERC RE 仅 6 relation types, n=397。"Universal bottleneck" 需降级。但补充：Section 5.9 conditional analysis（RE conditional on NER F1≥1）提供了 compound error 机制的初步因果证据，分析方法本身有价值。

**[AGREE] R2-N3: 相关工作遗漏**
逐条核实 pages 9-11 引用列表确认：
- Guo et al. 2017 (ECE 定义)：严重遗漏，论文用 ECE 作核心指标却未引
- Snell et al. 2024 (Scaling TTS)：严重遗漏，标题围绕 TTS 却缺核心引用
- Aggarwal et al. 2023 (Adaptive-Consistency)：同意，与 N-scaling 直接相关
- CISC (Huang et al. 2025)：同意，与 calibration + consistency 结论存在张力
- 传统 IE confidence：部分同意——scope 限于 LLM-based IE 合理，但应用一两句话说明排除理由

**[REBUT] R2-N4: 标题不匹配 → 应降为 should-fix**
标题用问号是修辞反问，abstract 第一句即引导质疑 log-prob 充分性。不理想但不影响接收决定。R1 已列为小问题。

### Should-Fix

**[AGREE] R2-W1: 仅 8B 模型** — 与 R1-N1 一致，我列为 critical。
**[REBUT] R2-W2: 未比较 trained approach** — 论文 scope 明确限定为 training-free signals（Section 7, Limitations），合理。但应在 Related Work 中更充分讨论 trained approaches 作为 upper bound。降级为 Related Work 补充问题。
**[AGREE] R2-W3: "Diagnostic framework" 过度包装** — 标准消融技术，建议降格为 "diagnostic analysis"。
**[AGREE] R2-W4: 零图表** — 与 R1-N3 一致。
**[REBUT] R2-W5: EM 是 straw man** — EM 是 Wang et al. (2023a) SC 的原始实现。Table 9 (NER EM rate=6%, RE=1.5%) 量化了 SC 在结构化输出上的失效，本身是有信息量的实证发现。

### 小问题
- Abstract "?" 引用：AGREE
- 英语数据集：AGREE
- 温度两点：REBUT — T=0.7/1.0 覆盖实践常用范围，Table 14 显示 SJ Δ=0.015，两点足以支撑有限主张。

### 对 Director 问题
1. "首个系统比较"：同意 R2，需限定为 "for LLM-based structured IE"
2. 负面结果：同意 R2 修正——核心发现是正面结果（SJ > LP on NER）。Director 原始描述与论文实际结论矛盾。
3. Diagnostic framework：同意降格为 "diagnostic analysis"
4. 定位：Findings 可接受，Main 偏弱。核心障碍：(a) 模型规模单一 (b) 零图表 (c) 成本分析误导 (d) RE 证据不足

### R1 综合评分维持
Overall 3/5 (Findings) | 1-6 scale: 4/6 (Weak Accept, borderline Findings)

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

_source line 24 · 2026-05-14T12:16:56.271387+00:00_

R1 交叉回应已收到。等待 R2 对 R1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 4

## Round 4

2 recorded events


### User

_source line 25 · 2026-05-14T12:16:58.944729+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：R2 的 12 个论点中，我同意 8 个（N1、N2、N3、W1、W3、W4 + 2 个小问题），反驳 3 个（N4 应降级、W2 scope 合理、W5 EM 非 straw man），1 个温度点部分反驳。R1 综合评分维持 3/5 (Findings) 不变。

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

_source line 26 · 2026-05-14T12:17:05.727508+00:00_

收到 R1 交叉回应。等待 R2 交叉回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 5

## Round 5

8 recorded events


### User

_source line 27 · 2026-05-14T12:17:13.473321+00:00_

[Reviewer 2 审稿意见]:
## R2 交叉回应 R1 审稿意见

### 汇总

| R1 Issue | R2 判断 | 要点 |
|----------|--------|------|
| N1 模型规模 | [AGREE] | 与 R2-W1 一致，8B→8B 只验证了架构鲁棒性非规模鲁棒性 |
| N2 成本误导 | [REBUT] | 同意加 cost-effectiveness 分析，但反对"系统性误导"定性——论文在 TTS 语境内准确（同 N 下 SJ 远优于 LP），R1 的 LP@N=1 vs SJ@N=8 对比混淆了 selective prediction 与 TTS |
| N3 零图表 | [AGREE] | 与 R2-W4 一致 |
| W1 signal combo | [AGREE] | 与 R2-W2 一致，Section 5.8 已证明互补性却不做组合实验 |
| W2 prompt sensitivity | [AGREE] | R1 的有价值补充，我原始审稿未覆盖 |
| W3 RE 单数据集 | [AGREE] | 与 R2-N2 一致，两位 reviewer 共同 critical |
| W4 统计检验 | [AGREE] | 部分同意，但 p-value 极小(10⁻²⁵)已部分弥补 |
| W5 失败案例 | [REBUT] | Section 5.11 inverted-U + Table 15 已提供统计层面分析，但确实缺实例级 case study |
| Minor-1 标题 | [AGREE] | 与 R2-N4 一致 |
| Minor-2 Table 16 | [AGREE] | entity count 6+ 的 ρ 下降需解释 |
| Minor-3 Eq.(1) kernel | [REBUT] | Section 3.2 有写"token-level overlap"，只是表述分散 |
| Minor-4 adaptive demo | [AGREE] | PDF 中未找到相关内容 |

### R1 与 R2 的共识和分歧

**共识（高置信度问题）**:
- 模型规模不足（R1-N1 = R2-W1）
- RE 单数据集不支撑 universal claim（R1-W3 = R2-N2）
- 零图表严重影响可读性（R1-N3 = R2-W4）
- 标题与结论矛盾（R1-Minor-1 = R2-N4）
- 需要 signal combination 实验（R1-W1 ≈ R2-W2）

**分歧**:
- **成本分析**: R1 定性为 "systematic misleading"（critical），我认为在 TTS 语境下论文的 O(N²) vs O(N) 陈述是准确的，应降为 warning 级（需补充 cost-effectiveness 分析但不构成误导）
- **SJ 失败分析**: R1 认为完全缺失，我认为 Section 5.11 的 inverted-U 分析部分覆盖了此问题
- **严重程度排序**: R1 将模型规模列为最高优先级 critical，我认为相关工作遗漏（R2-N3）同等或更高优先级——遗漏 Snell et al. 2024、Guo et al. 2017、CISC 等核心文献对论文可信度的影响大于模型数量

### 总体判断一致性
两位 reviewer 对 Overall 评分完全一致：**3/5 (Findings)**。核心分歧在于具体问题的严重程度排序，而非论文整体定位。

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

_source line 28 · 2026-05-14T12:17:33.358761+00:00_

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


### Tool result

_source line 29 · 2026-05-14T12:17:33.459565+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-14T12:18:34.323331+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"模型规模单一（仅 2 个 8B 模型），严重限制普适性主张\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 列为 critical，R2 列为 warning 但交叉回应中 AGREE。两位 reviewer 共识：8B→8B 仅验证架构鲁棒性非规模鲁棒性。建议增加 >30B 或 <3B 模型，或降级 establish 措辞。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"成本分析将 8-16× 推理开销描述为 negligible，存在误导\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 定为 critical（系统性误导），R2 认为 TTS 语境下 O(N²) vs O(N) 陈述准确但需补充 cost-effectiveness 分析。分歧在严重程度，共识在需要补充分析。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"全文零图表（17 表 0 图），不符合 confidence/calibration 研究惯例\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 reviewer 完全一致。缺少 selection curves、reliability diagrams、cost-effectiveness scatter。Table 8 有数据但以表格呈现。建议至少添加 3 个核心 Figure。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"SJ 方法新颖性有限——评估指标到 confidence 的自然迁移，缺少 kernel 消融\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 交叉回应 AGREE。type-grouped Hungarian matching + token-overlap kernel 本质是 set-level F1/Jaccard 的 confidence 版本。缺少与 edit distance、embedding similarity 等 kernel 的消融。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"RE task-complexity boundary 仅由 SciERC 单数据集支撑，不足以称 universal bottleneck\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 reviewer 共识 critical。SciERC RE 仅 6 relation types, n=397。需跨数据集验证（TACRED/DocRED/NYT）或降级措辞为 hypothesis。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"相关工作显著遗漏：5 篇核心文献缺失\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 逐条核实后 AGREE。遗漏：Guo et al. 2017 (ECE 定义)、Snell et al. 2024 (Scaling TTS)、Aggarwal et al. 2023 (Adaptive-Consistency)、CISC Huang et al. 2025 (挑战本文解读)、传统 IE confidence（R1 部分同意）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N4\"\n    summary: \"标题 Log-Probability Is All You Need? 与核心发现（SJ >> LP）存在 framing 冲突\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 认为问号修辞反问可接受，建议降为 should-fix。最终定为 warning——不理想但不影响接收决定。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"未探索 signal combination（SJ+LP 互补性已证明但未尝试组合）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。Section 5.8 已证明互补性（Δρ=0.14）却未尝试 α·SJ+(1-α)·LP 线性组合。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"单一 prompt 模板，缺乏 prompt sensitivity 分析\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉回应 AGREE（原始审稿未覆盖此点）。LLM-based IE 输出格式影响 set-based 指标。建议 appendix 给出完整 prompt。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"统计检验不系统——3 seed std 不替代正式 bootstrap CI\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 部分同意（p-value 极小已部分弥补但核心比较仍缺 CI）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"缺少 SJ 失败案例的实例级分析\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 认为完全缺失，R2 认为 Section 5.11 inverted-U 部分覆盖但缺实例级 case study。定为 warning。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"未比较 trained approach（verifier/reward model），Related Work 讨论不足\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 反驳 scope 限定合理但同意 Related Work 应更充分讨论 trained approaches 作为 upper bound。降为 Related Work 补充。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Diagnostic framework 过度包装——实为标准消融技术\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。建议降格为 diagnostic analysis。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"Exact-Match Voting 对结构化输出是否为 straw man baseline\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 认为 EM 是 straw man，R1 反驳——EM 是 Wang et al. (2023a) SC 原始实现，Table 9 量化了 SC 在结构化输出上的失效（NER EM rate=6%, RE=1.5%）。降为 info。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"MISC-1\"\n    summary: \"Abstract 存在未解析引用标记\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Abstract 有 ? 未解析引用\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"MISC-2\"\n    summary: \"仅英语数据集，未讨论多语言适用性\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"仅英语数据集\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"MISC-3\"\n    summary: \"Eq.(1) SJ similarity kernel 表述分散\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 指出未明确，R2 反驳 Section 3.2 有写但表述分散。建议集中说明。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"MISC-4\"\n    summary: \"Table 16 entity count 6+ 时 SJ ρ 降至 0.34 未解释\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
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
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"模型规模单一（仅 2 个 8B 模型），严重限制普适性主张\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 列为 critical，R2 列为 warning 但交叉回应中 AGREE。两位 reviewer 共识：8B→8B 仅验证架构鲁棒性非规模鲁棒性。建议增加 >30B 或 <3B 模型，或降级 establish 措辞。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"成本分析将 8-16× 推理开销描述为 negligible，存在误导\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 定为 critical（系统性误导），R2 认为 TTS 语境下 O(N²) vs O(N) 陈述准确但需补充 cost-effectiveness 分析。分歧在严重程度，共识在需要补充分析。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"全文零图表（17 表 0 图），不符合 confidence/calibration 研究惯例\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 reviewer 完全一致。缺少 selection curves、reliability diagrams、cost-effectiveness scatter。Table 8 有数据但以表格呈现。建议至少添加 3 个核心 Figure。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"SJ 方法新颖性有限——评估指标到 confidence 的自然迁移，缺少 kernel 消融\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 交叉回应 AGREE。type-grouped Hungarian matching + token-overlap kernel 本质是 set-level F1/Jaccard 的 confidence 版本。缺少与 edit distance、embedding similarity 等 kernel 的消融。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"RE task-complexity boundary 仅由 SciERC 单数据集支撑，不足以称 universal bottleneck\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 reviewer 共识 critical。SciERC RE 仅 6 relation types, n=397。需跨数据集验证（TACRED/DocRED/NYT）或降级措辞为 hypothesis。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"相关工作显著遗漏：5 篇核心文献缺失\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 逐条核实后 AGREE。遗漏：Guo et al. 2017 (ECE 定义)、Snell et al. 2024 (Scaling TTS)、Aggarwal et al. 2023 (Adaptive-Consistency)、CISC Huang et al. 2025 (挑战本文解读)、传统 IE confidence（R1 部分同意）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N4\"\n    summary: \"标题 Log-Probability Is All You Need? 与核心发现（SJ >> LP）存在 framing 冲突\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 认为问号修辞反问可接受，建议降为 should-fix。最终定为 warning——不理想但不影响接收决定。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"未探索 signal combination（SJ+LP 互补性已证明但未尝试组合）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。Section 5.8 已证明互补性（Δρ=0.14）却未尝试 α·SJ+(1-α)·LP 线性组合。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"单一 prompt 模板，缺乏 prompt sensitivity 分析\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉回应 AGREE（原始审稿未覆盖此点）。LLM-based IE 输出格式影响 set-based 指标。建议 appendix 给出完整 prompt。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"统计检验不系统——3 seed std 不替代正式 bootstrap CI\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 部分同意（p-value 极小已部分弥补但核心比较仍缺 CI）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"缺少 SJ 失败案例的实例级分析\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 认为完全缺失，R2 认为 Section 5.11 inverted-U 部分覆盖但缺实例级 case study。定为 warning。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"未比较 trained approach（verifier/reward model），Related Work 讨论不足\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 反驳 scope 限定合理但同意 Related Work 应更充分讨论 trained approaches 作为 upper bound。降为 Related Work 补充。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Diagnostic framework 过度包装——实为标准消融技术\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。建议降格为 diagnostic analysis。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"Exact-Match Voting 对结构化输出是否为 straw man baseline\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 认为 EM 是 straw man，R1 反驳——EM 是 Wang et al. (2023a) SC 原始实现，Table 9 量化了 SC 在结构化输出上的失效（NER EM rate=6%, RE=1.5%）。降为 info。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"MISC-1\"\n    summary: \"Abstract 存在未解析引用标记\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Abstract 有 ? 未解析引用\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"MISC-2\"\n    summary: \"仅英语数据集，未讨论多语言适用性\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"仅英语数据集\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"MISC-3\"\n    summary: \"Eq.(1) SJ similarity kernel 表述分散\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 指出未明确，R2 反驳 Section 3.2 有写但表述分散。建议集中说明。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"MISC-4\"\n    summary: \"Table 16 entity count 6+ 时 SJ ρ 降至 0.34 未解释\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-14T12:18:34.426004+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 7293}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-14T12:20:27.268290+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告：Round 1 圆桌审稿\n\n**论文**: \"Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 (ARR)\n**Reviewer 配置**: R1（方法与实验）+ R2（新颖性与相关工作）\n**轮次**: Round 1（已收敛，无需第二轮）\n\n---\n\n## Summary\n\n本文系统比较了 5 种 training-free confidence signals（Log-Probability、Entropy、Set Jaccard、Token Jaccard、Exact-Match）在 LLM-based 结构化信息抽取（NER/RE）的 best-of-N selection 场景中的表现。核心发现：(1) Set Jaccard (SJ) 在 NER 上显著优于 log-probability (Δρ≈0.16, p<10⁻²⁵)；(2) RE 中所有 signal 退化，归因于 compound error propagation。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个 8B 模型，多 seed/多温度/OOD 等消融维度。\n\n---\n\n## Strengths\n\n**S1. 系统且全面的实验矩阵** [R1+R2 共识]\n5 signal × 3 NER dataset × 1 RE dataset × 2 model × 2 budget × 2 temperature × 4 metric，13/15 实验完整覆盖。该领域首个如此系统的比较（限定为 LLM-based structured IE）。\n\n**S2. LOO-SJ circularity check 方法论亮点** [R1 提出，R2 认可]\nTable 1 Leave-one-out SJ（ρ=0.40 vs full SJ ρ=0.42, Δ=0.02）严谨地排除了 SJ 有效性依赖于自我循环的担忧。\n\n**S3. Compound error boundary 诊断有理论价值** [R1 提出，R2 认可]\nSection 5.9 对 RE 退化的因果分析（head + tail + relation type 三重叠加），Table 12 per-relation-type 证据具体。\n\n**S4. 多维度鲁棒性验证** [R1+R2 共识]\nMulti-seed（Std ≤ 0.01）、cross-dataset（排序一致）、cross-model、OOD（SJ-LP gap 从 +0.15 降至 +0.12 但仍显著）。\n\n**S5. Best-of-N selection 实用性** [R2 提出]\n将 ranking 指标转化为 F1 gain，对 practitioners 有直接指导价值。\n\n**S6. Inverted-U pattern** [R1 提出]\nSection 5.11, Table 15: SJ ρ 在 F1 bucket [0.3, 0.7] 最高，为 SJ 适用条件划定边界。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**C1. 模型规模单一，严重限制普适性** [R1 critical + R2 agree]\n仅 Qwen3-8B 和 LLaMA-3.1-8B 两个同规模模型。Confidence calibration 和 output diversity 随规模变化显著——更大模型的 greedy 可能已足够准确使 LP 优势明显化，更小模型高方差可能放大 SJ 优势。Abstract 中 \"establish\" 措辞过强。**建议**：至少增加一个 >30B 或 <3B 模型，或将 \"establish\" 降级为 \"investigate\"/\"examine\"。\n\n**C2. 相关工作显著遗漏** [R2 critical + R1 逐条核实 agree]\n5 篇核心文献缺失：\n- Guo et al. 2017 (On Calibration of Modern Neural Networks, ICML) — 论文用 ECE 作核心指标却未引用其定义来源\n- Snell et al. 2024 (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却缺核心引用\n- Aggarwal et al. 2023 (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling 直接相关\n- CISC: Huang et al. 2025 (Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 \"最 calibrated 的方法反而最无效\"，直接挑战本文解读\n- 传统 IE confidence（CRF 边际概率、span-level confidence、MC-dropout）— 至少应说明排除理由\n\n**C3. RE task-complexity boundary 证据严重不足** [R1+R2 共识 critical]\n全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行。\"Universal bottleneck\" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis。**建议**：增加至少一个 RE 数据集或降级措辞。\n\n**C4. SJ 方法新颖性有限** [R2 critical + R1 agree]\nSJ 是 set-level F1/Jaccard 的 confidence 化自然迁移（type-grouped Hungarian matching + token-overlap kernel）。缺少理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融。论文定位为 empirical study 但措辞暗示更高原创性。\n\n**C5. 全文零图表** [R1 critical + R2 agree]\n17 个表格，0 个 Figure。对 confidence/calibration 研究而言，缺少 selection curves、reliability diagrams、cost-effectiveness scatter 是严重呈现缺陷。Table 8 有 selection curve 数据但以表格呈现。**建议**：至少添加 3 个核心 Figure（selection curve、reliability diagram、cost-effectiveness）。\n\n**C6. 成本分析需补充** [R1 critical, R2 rebut 为 warning — 存在分歧]\nSection 6 称 SJ 额外成本 \"negligible (O(N²) set comparisons vs. O(N) LLM forward passes)\"，但 LP 可在 greedy decode（1 pass）上工作，SJ 需 N≥8 pass。**R1 立场**：将 8-16× 推理开销描述为 \"negligible\" 是系统性误导。**R2 立场**：在 TTS 语境（同 N 下比较）内论文陈述准确，LP@N=1 vs SJ@N=8 混淆了 selective prediction 与 TTS。**共识**：需补充 cost-effectiveness 分析（F1 gain per unit compute）。\n\n### Should-Fix\n\n**W1. 未探索 signal combination** [R1+R2 共识]\nSection 5.8 证明 SJ 和 LP 互补（Δρ=0.14），却未尝试 α·SJ+(1-α)·LP 线性组合。\n\n**W2. 标题与核心发现不匹配** [R2 critical → R1 rebut 降为 warning]\n\"Log-Probability Is All You Need?\" 暗示 log-prob 可能足够，但核心发现是 SJ 显著优于 log-prob。R1 认为问号修辞反问可接受，最终定为 warning。**建议**：改为 \"Beyond Log-Probability: ...\" 或类似。\n\n**W3. 单一 prompt 模板** [R1 提出，R2 agree]\n未提及 prompt 变体。LLM-based IE 输出格式直接影响 set-based 指标。**建议**：appendix 给出完整 prompt，讨论 format 影响。\n\n**W4. 统计检验不系统** [R1 提出，R2 部分 agree]\n核心比较（Table 4/5 cross-dataset/cross-model）无 bootstrap CI，3 seed std 不替代正式统计检验。p-value 极小部分弥补但不充分。\n\n**W5. SJ 失败案例分析不足** [R1 提出，R2 部分 rebut]\nSJ ρ 最佳也仅 0.42-0.51。Section 5.11 inverted-U 提供统计层面分析，但缺实例级 case study（高 SJ 低 F1 / 低 SJ 高 F1 的具体模式）。\n\n**W6. \"Diagnostic framework\" 过度包装** [R2 提出，R1 agree]\n标准消融技术（F1 分桶、component 分解、stratification）不构成可复用 framework。**建议**：降格为 \"diagnostic analysis\"。\n\n**W7. 未讨论 trained approaches 作为 upper bound** [R2 提出，R1 部分 agree]\nScope 限定为 training-free signals 合理，但 Related Work 应更充分讨论 verifier/reward model 等 trained approaches。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致：\n1. **Overall 评分**: 3/5 (Findings)，Main 偏弱\n2. **模型规模不足**: 仅 8B 模型不支撑普适性主张\n3. **RE 单数据集**: \"Universal bottleneck\" 需降级\n4. **零图表**: 严重影响可读性和说服力\n5. **相关工作遗漏**: 5 篇核心文献必须补充\n6. **Signal combination**: 已证明互补性但未尝试组合\n7. **\"首个系统比较\"**: 需限定为 \"for LLM-based structured IE\"\n8. **Diagnostic framework**: 降格为 \"diagnostic analysis\"\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | 最终定级 |\n|------|---------|---------|----------|\n| 成本分析 | Critical（系统性误导） | Warning（TTS 语境下准确，需补充分析） | Critical（保守取高，但记录分歧） |\n| SJ 失败分析 | 完全缺失 | Section 5.11 部分覆盖 | Warning（缺实例级分析） |\n| 优先级排序 | 模型规模 > 成本分析 > 零图表 | 相关工作 > RE 数据集 > 新颖性 | 均为 critical |\n| EM baseline | 合理（SC 原始实现） | Straw man | Info（R1 论证更充分） |\n\n---\n\n## Questions（需作者澄清）\n\n1. 是否计划增加 >30B 或 <3B 模型实验？如不可行，如何限定当前结论的适用范围？\n2. Table 16 entity count 6+ 时 SJ ρ 降至 0.34 的原因是什么？\n3. SJ 的 similarity kernel 是否考虑过其他选择（edit distance、embedding cosine）？选择 token-level overlap 的理由？\n4. Section 5.8 发现 SJ 和 LP 互补后，是否尝试过任何形式的组合？\n5. 如何回应 CISC (Huang et al. 2025) 发现 \"最 calibrated 的方法反而最无效\" 与本文结论的张力？\n\n---\n\n## Missing References\n\n1. **Guo et al. 2017** — On Calibration of Modern Neural Networks (ICML) — ECE 定义来源\n2. **Snell et al. 2024** — Scaling LLM Test-Time Compute Optimally (ICLR 2025) — TTS 核心工作\n3. **Aggarwal et al. 2023** — Adaptive-Consistency (EMNLP 2023) — N-scaling 相关\n4. **Huang et al. 2025** — CISC: Confidence Improves Self-Consistency (ACL Findings 2025) — 挑战本文解读\n5. **传统 IE confidence 文献** — CRF 边际概率、span-level confidence、MC-dropout uncertainty\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分**: 3/5 (Findings) — 两位 Reviewer 完全一致\n**Director Scale**: 3.5/6 (Borderline Reject / Weak Accept for Findings)\n**置信度**: 4/5\n\n**定位判断**: Findings 可接受，Main 不足。论文的实用价值（practitioners 的 confidence signal 选择指南）适合 Findings 定位，但 6 个 critical 问题（模型规模、相关工作、RE 数据集、方法新颖性、零图表、成本分析）共同削弱了当前版本的竞争力。\n\n**核心障碍**（按优先级）:\n1. 模型规模单一 — 普适性主张无法成立\n2. 相关工作遗漏 — 5 篇核心文献缺失严重损害可信度\n3. RE 证据不足 — \"Universal bottleneck\" 仅单数据集支撑\n4. 零图表 — calibration 研究无图不可接受\n5. 方法新颖性有限 — SJ 是自然迁移，缺 kernel 消融\n6. 成本分析 — 需补充 cost-effectiveness\n\n**修改建议优先级**:\n- P0（决定性）: 补充相关工作 + 添加核心图表 + 降级 \"establish\"/\"universal\" 措辞\n- P1（强烈建议）: 增加 ≥1 个非 8B 模型 + 增加 ≥1 个 RE 数据集 + 补充 cost-effectiveness 分析\n- P2（改善质量）: signal combination 实验 + prompt sensitivity + 失败案例分析 + bootstrap CI\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"establish best practices\" 措辞过强，改为 \"investigate\" 或 \"examine\"\n- 缺少 Snell et al. 2024 (TTS) 和 Guo et al. 2017 (ECE) 引用\n\n### Section 3 (Method)\n- Eq.(1) SJ similarity kernel 的具体实现分散在多处，建议集中说明\n- 缺少 kernel 选择的动机说明和消融\n\n### Section 4 (Experimental Setup)\n- 未给出完整 prompt 模板\n- 仅 T=0.7 和 T=1.0 两个温度点（R1 认为足够，R2 认为偏少）\n\n### Section 5 (Results)\n- Table 8 selection curve 数据应可视化为 Figure\n- Table 16 entity count 6+ ρ 下降未解释\n- Section 5.9 \"universal bottleneck\" 需降级措辞或增加数据集\n- Section 5.11 inverted-U 缺实例级 case study\n\n### Section 6 (Discussion)\n- 成本分析需区分 TTS 内比较 vs 跨范式比较\n- 补充 F1 gain per unit compute 分析\n- \"Diagnostic framework\" 降格为 \"diagnostic analysis\"\n\n### Section 7 (Limitations)\n- 需明确讨论模型规模限制的影响\n- 需讨论 trained approaches 作为 upper bound\n\n### Related Work\n- 补充 5 篇遗漏文献\n- 讨论传统 IE confidence 或说明排除理由\n- 讨论 CISC 与本文结论的张力\n\n### Format\n- Abstract 有未解析引用标记（\"?\"）\n- 全文需添加至少 3 个核心 Figure\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
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
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告：Round 1 圆桌审稿\n\n**论文**: \"Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 (ARR)\n**Reviewer 配置**: R1（方法与实验）+ R2（新颖性与相关工作）\n**轮次**: Round 1（已收敛，无需第二轮）\n\n---\n\n## Summary\n\n本文系统比较了 5 种 training-free confidence signals（Log-Probability、Entropy、Set Jaccard、Token Jaccard、Exact-Match）在 LLM-based 结构化信息抽取（NER/RE）的 best-of-N selection 场景中的表现。核心发现：(1) Set Jaccard (SJ) 在 NER 上显著优于 log-probability (Δρ≈0.16, p<10⁻²⁵)；(2) RE 中所有 signal 退化，归因于 compound error propagation。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个 8B 模型，多 seed/多温度/OOD 等消融维度。\n\n---\n\n## Strengths\n\n**S1. 系统且全面的实验矩阵** [R1+R2 共识]\n5 signal × 3 NER dataset × 1 RE dataset × 2 model × 2 budget × 2 temperature × 4 metric，13/15 实验完整覆盖。该领域首个如此系统的比较（限定为 LLM-based structured IE）。\n\n**S2. LOO-SJ circularity check 方法论亮点** [R1 提出，R2 认可]\nTable 1 Leave-one-out SJ（ρ=0.40 vs full SJ ρ=0.42, Δ=0.02）严谨地排除了 SJ 有效性依赖于自我循环的担忧。\n\n**S3. Compound error boundary 诊断有理论价值** [R1 提出，R2 认可]\nSection 5.9 对 RE 退化的因果分析（head + tail + relation type 三重叠加），Table 12 per-relation-type 证据具体。\n\n**S4. 多维度鲁棒性验证** [R1+R2 共识]\nMulti-seed（Std ≤ 0.01）、cross-dataset（排序一致）、cross-model、OOD（SJ-LP gap 从 +0.15 降至 +0.12 但仍显著）。\n\n**S5. Best-of-N selection 实用性** [R2 提出]\n将 ranking 指标转化为 F1 gain，对 practitioners 有直接指导价值。\n\n**S6. Inverted-U pattern** [R1 提出]\nSection 5.11, Table 15: SJ ρ 在 F1 bucket [0.3, 0.7] 最高，为 SJ 适用条件划定边界。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**C1. 模型规模单一，严重限制普适性** [R1 critical + R2 agree]\n仅 Qwen3-8B 和 LLaMA-3.1-8B 两个同规模模型。Confidence calibration 和 output diversity 随规模变化显著——更大模型的 greedy 可能已足够准确使 LP 优势明显化，更小模型高方差可能放大 SJ 优势。Abstract 中 \"establish\" 措辞过强。**建议**：至少增加一个 >30B 或 <3B 模型，或将 \"establish\" 降级为 \"investigate\"/\"examine\"。\n\n**C2. 相关工作显著遗漏** [R2 critical + R1 逐条核实 agree]\n5 篇核心文献缺失：\n- Guo et al. 2017 (On Calibration of Modern Neural Networks, ICML) — 论文用 ECE 作核心指标却未引用其定义来源\n- Snell et al. 2024 (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却缺核心引用\n- Aggarwal et al. 2023 (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling 直接相关\n- CISC: Huang et al. 2025 (Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 \"最 calibrated 的方法反而最无效\"，直接挑战本文解读\n- 传统 IE confidence（CRF 边际概率、span-level confidence、MC-dropout）— 至少应说明排除理由\n\n**C3. RE task-complexity boundary 证据严重不足** [R1+R2 共识 critical]\n全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行。\"Universal bottleneck\" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis。**建议**：增加至少一个 RE 数据集或降级措辞。\n\n**C4. SJ 方法新颖性有限** [R2 critical + R1 agree]\nSJ 是 set-level F1/Jaccard 的 confidence 化自然迁移（type-grouped Hungarian matching + token-overlap kernel）。缺少理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融。论文定位为 empirical study 但措辞暗示更高原创性。\n\n**C5. 全文零图表** [R1 critical + R2 agree]\n17 个表格，0 个 Figure。对 confidence/calibration 研究而言，缺少 selection curves、reliability diagrams、cost-effectiveness scatter 是严重呈现缺陷。Table 8 有 selection curve 数据但以表格呈现。**建议**：至少添加 3 个核心 Figure（selection curve、reliability diagram、cost-effectiveness）。\n\n**C6. 成本分析需补充** [R1 critical, R2 rebut 为 warning — 存在分歧]\nSection 6 称 SJ 额外成本 \"negligible (O(N²) set comparisons vs. O(N) LLM forward passes)\"，但 LP 可在 greedy decode（1 pass）上工作，SJ 需 N≥8 pass。**R1 立场**：将 8-16× 推理开销描述为 \"negligible\" 是系统性误导。**R2 立场**：在 TTS 语境（同 N 下比较）内论文陈述准确，LP@N=1 vs SJ@N=8 混淆了 selective prediction 与 TTS。**共识**：需补充 cost-effectiveness 分析（F1 gain per unit compute）。\n\n### Should-Fix\n\n**W1. 未探索 signal combination** [R1+R2 共识]\nSection 5.8 证明 SJ 和 LP 互补（Δρ=0.14），却未尝试 α·SJ+(1-α)·LP 线性组合。\n\n**W2. 标题与核心发现不匹配** [R2 critical → R1 rebut 降为 warning]\n\"Log-Probability Is All You Need?\" 暗示 log-prob 可能足够，但核心发现是 SJ 显著优于 log-prob。R1 认为问号修辞反问可接受，最终定为 warning。**建议**：改为 \"Beyond Log-Probability: ...\" 或类似。\n\n**W3. 单一 prompt 模板** [R1 提出，R2 agree]\n未提及 prompt 变体。LLM-based IE 输出格式直接影响 set-based 指标。**建议**：appendix 给出完整 prompt，讨论 format 影响。\n\n**W4. 统计检验不系统** [R1 提出，R2 部分 agree]\n核心比较（Table 4/5 cross-dataset/cross-model）无 bootstrap CI，3 seed std 不替代正式统计检验。p-value 极小部分弥补但不充分。\n\n**W5. SJ 失败案例分析不足** [R1 提出，R2 部分 rebut]\nSJ ρ 最佳也仅 0.42-0.51。Section 5.11 inverted-U 提供统计层面分析，但缺实例级 case study（高 SJ 低 F1 / 低 SJ 高 F1 的具体模式）。\n\n**W6. \"Diagnostic framework\" 过度包装** [R2 提出，R1 agree]\n标准消融技术（F1 分桶、component 分解、stratification）不构成可复用 framework。**建议**：降格为 \"diagnostic analysis\"。\n\n**W7. 未讨论 trained approaches 作为 upper bound** [R2 提出，R1 部分 agree]\nScope 限定为 training-free signals 合理，但 Related Work 应更充分讨论 verifier/reward model 等 trained approaches。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致：\n1. **Overall 评分**: 3/5 (Findings)，Main 偏弱\n2. **模型规模不足**: 仅 8B 模型不支撑普适性主张\n3. **RE 单数据集**: \"Universal bottleneck\" 需降级\n4. **零图表**: 严重影响可读性和说服力\n5. **相关工作遗漏**: 5 篇核心文献必须补充\n6. **Signal combination**: 已证明互补性但未尝试组合\n7. **\"首个系统比较\"**: 需限定为 \"for LLM-based structured IE\"\n8. **Diagnostic framework**: 降格为 \"diagnostic analysis\"\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | 最终定级 |\n|------|---------|---------|----------|\n| 成本分析 | Critical（系统性误导） | Warning（TTS 语境下准确，需补充分析） | Critical（保守取高，但记录分歧） |\n| SJ 失败分析 | 完全缺失 | Section 5.11 部分覆盖 | Warning（缺实例级分析） |\n| 优先级排序 | 模型规模 > 成本分析 > 零图表 | 相关工作 > RE 数据集 > 新颖性 | 均为 critical |\n| EM baseline | 合理（SC 原始实现） | Straw man | Info（R1 论证更充分） |\n\n---\n\n## Questions（需作者澄清）\n\n1. 是否计划增加 >30B 或 <3B 模型实验？如不可行，如何限定当前结论的适用范围？\n2. Table 16 entity count 6+ 时 SJ ρ 降至 0.34 的原因是什么？\n3. SJ 的 similarity kernel 是否考虑过其他选择（edit distance、embedding cosine）？选择 token-level overlap 的理由？\n4. Section 5.8 发现 SJ 和 LP 互补后，是否尝试过任何形式的组合？\n5. 如何回应 CISC (Huang et al. 2025) 发现 \"最 calibrated 的方法反而最无效\" 与本文结论的张力？\n\n---\n\n## Missing References\n\n1. **Guo et al. 2017** — On Calibration of Modern Neural Networks (ICML) — ECE 定义来源\n2. **Snell et al. 2024** — Scaling LLM Test-Time Compute Optimally (ICLR 2025) — TTS 核心工作\n3. **Aggarwal et al. 2023** — Adaptive-Consistency (EMNLP 2023) — N-scaling 相关\n4. **Huang et al. 2025** — CISC: Confidence Improves Self-Consistency (ACL Findings 2025) — 挑战本文解读\n5. **传统 IE confidence 文献** — CRF 边际概率、span-level confidence、MC-dropout uncertainty\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分**: 3/5 (Findings) — 两位 Reviewer 完全一致\n**Director Scale**: 3.5/6 (Borderline Reject / Weak Accept for Findings)\n**置信度**: 4/5\n\n**定位判断**: Findings 可接受，Main 不足。论文的实用价值（practitioners 的 confidence signal 选择指南）适合 Findings 定位，但 6 个 critical 问题（模型规模、相关工作、RE 数据集、方法新颖性、零图表、成本分析）共同削弱了当前版本的竞争力。\n\n**核心障碍**（按优先级）:\n1. 模型规模单一 — 普适性主张无法成立\n2. 相关工作遗漏 — 5 篇核心文献缺失严重损害可信度\n3. RE 证据不足 — \"Universal bottleneck\" 仅单数据集支撑\n4. 零图表 — calibration 研究无图不可接受\n5. 方法新颖性有限 — SJ 是自然迁移，缺 kernel 消融\n6. 成本分析 — 需补充 cost-effectiveness\n\n**修改建议优先级**:\n- P0（决定性）: 补充相关工作 + 添加核心图表 + 降级 \"establish\"/\"universal\" 措辞\n- P1（强烈建议）: 增加 ≥1 个非 8B 模型 + 增加 ≥1 个 RE 数据集 + 补充 cost-effectiveness 分析\n- P2（改善质量）: signal combination 实验 + prompt sensitivity + 失败案例分析 + bootstrap CI\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"establish best practices\" 措辞过强，改为 \"investigate\" 或 \"examine\"\n- 缺少 Snell et al. 2024 (TTS) 和 Guo et al. 2017 (ECE) 引用\n\n### Section 3 (Method)\n- Eq.(1) SJ similarity kernel 的具体实现分散在多处，建议集中说明\n- 缺少 kernel 选择的动机说明和消融\n\n### Section 4 (Experimental Setup)\n- 未给出完整 prompt 模板\n- 仅 T=0.7 和 T=1.0 两个温度点（R1 认为足够，R2 认为偏少）\n\n### Section 5 (Results)\n- Table 8 selection curve 数据应可视化为 Figure\n- Table 16 entity count 6+ ρ 下降未解释\n- Section 5.9 \"universal bottleneck\" 需降级措辞或增加数据集\n- Section 5.11 inverted-U 缺实例级 case study\n\n### Section 6 (Discussion)\n- 成本分析需区分 TTS 内比较 vs 跨范式比较\n- 补充 F1 gain per unit compute 分析\n- \"Diagnostic framework\" 降格为 \"diagnostic analysis\"\n\n### Section 7 (Limitations)\n- 需明确讨论模型规模限制的影响\n- 需讨论 trained approaches 作为 upper bound\n\n### Related Work\n- 补充 5 篇遗漏文献\n- 讨论传统 IE confidence 或说明排除理由\n- 讨论 CISC 与本文结论的张力\n\n### Format\n- Abstract 有未解析引用标记（\"?\"）\n- 全文需添加至少 3 个核心 Figure\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-14T12:20:31.851360+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4583
}
```

</details>

---


### Assistant

_source line 34 · 2026-05-14T12:20:40.992052+00:00_

**Round 1 圆桌审稿完成。**

汇总：
- **评分**：3/5 (Findings)，两位 Reviewer 完全一致
- **6 个 Critical 问题**：模型规模单一、相关工作遗漏 5 篇、RE 仅单数据集、SJ 新颖性有限、零图表、成本分析需补充
- **7 个 Warning 问题**：signal combination、标题矛盾、prompt sensitivity、统计检验、失败案例、framework 包装、trained approach 讨论
- **主要分歧**：成本分析严重程度（R1 critical vs R2 warning）——保守取高但记录分歧
- **Issue Tracker** 已同步 18 条 issue
- **审稿报告** 已投递至 Research Director

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 35 · 2026-05-14T12:20:43.721660+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。汇总：

- **8/12 项 AGREE**（N1 模型规模、N3 零图表、W1-W4、Minor-1/2），其中多项与我的原始审稿高度重叠
- **3/12 项 REBUT**：
  - **N2 成本误导**：论文在 TTS 语境下准确（同 N 时 SJ≫LP），R1 的 LP@N=1 vs SJ@N=8 对比混淆了 selective prediction 与 TTS，"系统性误导"定性过重
  - **W5 失败案例**：Section 5.11 inverted-U 已提供统计层面分析，但确实缺实例级 case study
  - **Minor-3 Eq.(1) kernel**：Section 3.2 明确写了 "token-level overlap"，只是表述分散
- **1 项无法验证**（Minor-4 adaptive demo，PDF 中未出现）

两位 reviewer 的 Overall 评分一致：**3/5 (Findings)**。

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

_source line 36 · 2026-05-14T12:20:54.691354+00:00_

圆桌审稿已完成。

**最终结果**：两位 Reviewer 一致评分 **3/5 (Findings)**，Director Scale **3.5/6 (Borderline)**。审稿报告已投递给 Research Director。Issue Tracker 已同步 18 个 issue（6 critical / 7 warning / 5 info）。

R2 的交叉回应在报告提交前到达，其内容与报告中记录的分歧一致（成本分析严重程度、SJ 失败分析覆盖程度、Eq.(1) kernel 表述），无需修订报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 7

## Round 7

58 recorded events


### User

_source line 37 · 2026-05-15T01:47:45.902206+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

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

_source line 38 · 2026-05-15T01:47:53.648538+00:00_

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

_source line 39 · 2026-05-15T01:47:53.699892+00:00_

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
…[truncated 2458 chars]

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

_source line 40 · 2026-05-15T01:47:57.416369+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 41 · 2026-05-15T01:47:57.416712+00:00_



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

_source line 42 · 2026-05-15T01:48:02.841608+00:00_

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

_source line 43 · 2026-05-15T01:48:03.595506+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (73 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_017_llama_conll_n16_s456_r1024（准备中）\n- exp_017_llama_conll_n16_r1024（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n- exp_007_ner_llama（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp008_re_n16（准备中）\n\n## 近期结论\n- **exp_002_conll_n16_r1024** (killed): —\n- **exp_007_llama_n16_r1024** (killed): —\n- **exp_017_llama_conll_n16_s123_r1024** (killed): —\n\n## 趋势\n成功 37 / 负向 18 / 失败 1 / 共 64\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-15T01:48:03.595916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-15T01:48:03.646343+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.

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

_source line 46 · 2026-05-15T01:48:08.418347+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
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
    "pattern": "**/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-15T01:48:08.570508+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-15T01:48:08.570994+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
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
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-15T01:48:08.621545+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

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

_source line 50 · 2026-05-15T01:48:14.146844+00:00_

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

_source line 51 · 2026-05-15T01:48:14.197598+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

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

_source line 52 · 2026-05-15T01:48:14.298426+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 53 · 2026-05-15T01:48:14.399350+00:00_



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

_source line 54 · 2026-05-15T01:48:19.170260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
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
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-15T01:48:19.976778+00:00_

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

_source line 56 · 2026-05-15T01:48:20.579812+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-15T01:48:20.680722+00:00_

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

_source line 58 · 2026-05-15T01:48:20.781891+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumpti
…[truncated 3524 chars]

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

_source line 59 · 2026-05-15T01:48:20.782303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-15T01:48:20.833168+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 2626 chars]

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

_source line 61 · 2026-05-15T01:48:30.069584+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061
…[truncated 2707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 10899
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-15T01:48:37.400500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-15T01:48:37.752684+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Our primary model is \textbf{Qwen3-8B} (LoRA, $r{=}32$); for cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct}.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \mu
…[truncated 7771 chars]

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

_source line 64 · 2026-05-15T01:48:37.753203+00:00_

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

_source line 65 · 2026-05-15T01:48:38.255717+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).
8	This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	
11	\paragraph{Why quality estimators fail as selectors.}
12	Quality estimation ranks \textit{instances} by expected output quality via output distribution entropy; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.
13	On SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).
14	The $\rho$--AUROC dissociation illuminates the same asymmetry: on SciERC, EM achieves the highest AUROC (0.749 NER, 0.706 RE) yet ranks third or last in $\rho$; both metrics measure be
…[truncated 1013 chars]

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

_source line 66 · 2026-05-15T01:48:38.256186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-15T01:48:39.211495+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	All target reasoning/QA with discrete answers.
9	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
13	However, they rely on surface-level matching (explicitly acknowledging it ``overlooks semantically consistent outputs''), do not study best-of-$N$ selection, and evaluate a single domain with hard prompting.
14	Our Soft Jaccard signal addresses the matching limitation through type-aware bipartite matching with span overlap.
15	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
16	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie
…[truncated 1727 chars]

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

_source line 68 · 2026-05-15T01:48:39.211873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-15T01:48:39.514847+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-15T01:48:39.565553+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 paper format page limit long paper short paper ACL template"
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
    "query": "EMNLP 2026 paper format page limit long paper short paper ACL template"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-15T01:48:47.854330+00:00_

Web search results for query: "EMNLP 2026 paper format page limit long paper short paper ACL template"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Association for Computational Linguistics (ACL) conference - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Instructions for EMNLP 2023 Proceedings","url":"https://arxiv.org/html/2404.01679v2"}]

Based on the search results, here is the information about EMNLP 2026 paper format requirements:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## ACL Template

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Limitations Section

The mandatory Limitations section is required, placed after the conclusion.

## Additional Details

EMNLP 2026 invites the submission
…[truncated 240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8288
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-15T01:48:52.424522+00:00_

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

_source line 73 · 2026-05-15T01:48:53.328691+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-15T01:48:53.329276+00:00_

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

_source line 75 · 2026-05-15T01:48:53.781694+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 9406 chars]

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

_source line 76 · 2026-05-15T01:48:53.782102+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limits references appendix anonymity policy"
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
    "query": "ACL Rolling Review 2026 submission format page limits references appendix anonymity policy"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-15T01:49:00.458912+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limits references appendix anonymity policy"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on my web search for ACL Rolling Review 2026 submission format guidelines, here's what I found:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

## References and Appendices

The conference encourages submission of appendices and supplementary material, which are not required to fit within these page limits. However, review versions of papers must be self-
…[truncated 942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6676
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-15T01:49:12.661251+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "6"
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
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-15T01:49:12.711970+00:00_



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

_source line 80 · 2026-05-15T01:49:16.027211+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "review_issues.yaml"
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
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-15T01:49:16.529656+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-15T01:49:17.433553+00:00_

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

_source line 83 · 2026-05-15T01:49:17.484268+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md

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

_source line 84 · 2026-05-15T01:49:28.731085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-15T01:49:28.731489+00:00_

1	---
2	round: 0
3	overall_score: borderline
4	timestamp: 2026-05-14T12:20:27.321042+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告：Round 1 圆桌审稿
11	
12	**论文**: "Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"
13	**目标 Venue**: EMNLP 2026 (ARR)
14	**Reviewer 配置**: R1（方法与实验）+ R2（新颖性与相关工作）
15	**轮次**: Round 1（已收敛，无需第二轮）
16	
17	---
18	
19	## Summary
20	

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

_source line 86 · 2026-05-15T01:49:29.233933+00:00_

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

_source line 87 · 2026-05-15T01:49:29.736261+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-15T01:49:30.138226+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
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
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-15T01:49:30.188998+00:00_

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

_source line 90 · 2026-05-15T01:50:24.475371+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template (`\\usepackage[review]{acl}`)，长文 8 页正文 + 无限参考文献 + 附录不计页\n- **匿名规则**: Double-blind (作者已标注 Anonymous)\n\n### 论文信息\n- **标题**: \"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\"\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **各 section 文件**: `docs/paper/sections/` 下的 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计有效性**。重点关注：\n\n1. **方法论**：\n   - 5 个 confidence signal 的数学定义是否严谨、无歧义\n   - Soft Jaccard 的 bipartite matching + Hungarian algorithm 是否正确形式化\n   - Entity voting confidence 的定义是否合理（mean frequency vs. 其他聚合方式）\n   - Instance-level vs per-sample signal 的区分是否清晰且有理论支撑\n\n2. **实验设计**：\n   - 数据集选择（SciERC、CoNLL-2003、WNUT-17）是否充分覆盖难度梯度\n   - 模型选择（Qwen3-8B、LLaMA-3.1-8B）是否足够，8B 是否太小\n   - N=8/16 的采样量是否充分，T=1.0 是否合理\n   - Evaluation protocol：Spearman ρ + AUROC + best-of-N F1 三个指标是否全面\n   - Greedy baseline 的公平性（T=0, N=1 vs T=1.0, N=8）\n\n3. **统计有效性**：\n   - p=0.39 的 bootstrap 检验是否正确执行\n   - Cohen's d=0.038 报告是否充分\n   - 3-seed ±std 是否足够，是否需要更多 seed\n   - WNUT-17 的 p=0.106 是否应更谨慎解读\n   - 置信区间的使用是否一致\n\n4. **结果可复现性**：\n   - 是否有足够的实现细节（LoRA 配置、vLLM 参数、prompt 格式等）\n   - 数据预处理是否清晰\n\n5. **格式合规**：\n   - 页数是否在 8 页限制内\n   - 表格/图表是否清晰可读\n   - Limitations section 是否存在且充分\n\n请按 EMNLP 顶会最严格标准评审，不留情面。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)。"
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
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template (`\\usepackage[review]{acl}`)，长文 8 页正文 + 无限参考文献 + 附录不计页\n- **匿名规则**: Double-blind (作者已标注 Anonymous)\n\n### 论文信息\n- **标题**: \"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\"\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **各 section 文件**: `docs/paper/sections/` 下的 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计有效性**。重点关注：\n\n1. **方法论**：\n   - 5 个 confidence signal 的数学定义是否严谨、无歧义\n   - Soft Jaccard 的 bipartite matching + Hungarian algorithm 是否正确形式化\n   - Entity voting confidence 的定义是否合理（mean frequency vs. 其他聚合方式）\n   - Instance-level vs per-sample signal 的区分是否清晰且有理论支撑\n\n2. **实验设计**：\n   - 数据集选择（SciERC、CoNLL-2003、WNUT-17）是否充分覆盖难度梯度\n   - 模型选择（Qwen3-8B、LLaMA-3.1-8B）是否足够，8B 是否太小\n   - N=8/16 的采样量是否充分，T=1.0 是否合理\n   - Evaluation protocol：Spearman ρ + AUROC + best-of-N F1 三个指标是否全面\n   - Greedy baseline 的公平性（T=0, N=1 vs T=1.0, N=8）\n\n3. **统计有效性**：\n   - p=0.39 的 bootstrap 检验是否正确执行\n   - Cohen's d=0.038 报告是否充分\n   - 3-seed ±std 是否足够，是否需要更多 seed\n   - WNUT-17 的 p=0.106 是否应更谨慎解读\n   - 置信区间的使用是否一致\n\n4. **结果可复现性**：\n   - 是否有足够的实现细节（LoRA 配置、vLLM 参数、prompt 格式等）\n   - 数据预处理是否清晰\n\n5. **格式合规**：\n   - 页数是否在 8 页限制内\n   - 表格/图表是否清晰可读\n   - Limitations section 是否存在且充分\n\n请按 EMNLP 顶会最严格标准评审，不留情面。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-15T01:50:42.598081+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18122
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-15T01:50:42.750335+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 整体连贯性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template (`\\usepackage[review]{acl}`)，长文 8 页正文 + 无限参考文献 + 附录不计页\n- **匿名规则**: Double-blind (作者已标注 Anonymous)\n\n### 论文信息\n- **标题**: \"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\"\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **各 section 文件**: `docs/paper/sections/` 下的 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex\n\n### 你的审查侧重\n\n**新颖性 + Related Work 完整性 + 整体连贯性**。重点关注：\n\n1. **新颖性评估**：\n   - \"correlation-selection gap\" 概念是否为真正的新发现，还是已知现象的重新命名\n   - 5 个 confidence signal 中哪些是新提出的、哪些是已有方法的直接套用\n   - Soft Jaccard with Hungarian matching 的技术新颖性如何\n   - 对比 Nedellec et al. (2026)，本文的增量贡献是否足够支撑 EMNLP 长文\n   - \"systematic comparison\" 类论文在 EMNLP 的接受标准——是否有足够的 insight 而非仅仅是 benchmark\n\n2. **Related Work 完整性**：\n   - Self-consistency 线：Wang et al. (2023), Chen et al. (2024), Taubenfeld et al. (2025), Kang et al. (2025) 等是否全面\n   - Structured IE 线：是否遗漏重要的 generative IE / constrained decoding 工作\n   - Uncertainty/calibration 线：是否遗漏关键方法（如 conformal prediction 在 NLP 中的应用）\n   - Test-time compute scaling 线：Snell et al. (2024), Brown et al. (2024) 之外是否有遗漏\n   - 是否有 2025-2026 年的重要新工作被遗漏\n   - **验证引用真实性**：抽查至少 5 篇引用，确认作者、年份、标题、venue 是否正确（特别关注 2025-2026 年的引用）\n\n3. **整体连贯性**：\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的叙事线是否一致\n   - Claims 是否都有实验支撑，是否有 overclaim\n   - \"Strong Predictors, Weak Selectors\" 标题是否准确反映论文内容\n   - Contribution list 是否与实际内容匹配\n   - Discussion section 是否有多余的推测性内容\n\n4. **写作质量**：\n   - 术语一致性（signal names、metric names）\n   - 图表标题是否自足（self-contained）\n   - 数学符号是否一致\n   - 是否有 repetitive content 或不必要的冗余\n\n5. **遗漏的重要引用搜索**：\n   - 请用 web_search 搜索以下关键词，检查是否有遗漏的重要 2025-2026 工作：\n     - \"self-consistency structured prediction 2025 2026\"\n     - \"confidence estimation information extraction LLM 2025 2026\"\n     - \"test-time scaling NER relation extraction 2025 2026\"\n\n请按 EMNLP 顶会最严格标准评审，不留情面。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Missing References → Questions → Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)。"
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
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 整体连贯性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template (`\\usepackage[review]{acl}`)，长文 8 页正文 + 无限参考文献 + 附录不计页\n- **匿名规则**: Double-blind (作者已标注 Anonymous)\n\n### 论文信息\n- **标题**: \"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\"\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **各 section 文件**: `docs/paper/sections/` 下的 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex\n\n### 你的审查侧重\n\n**新颖性 + Related Work 完整性 + 整体连贯性**。重点关注：\n\n1. **新颖性评估**：\n   - \"correlation-selection gap\" 概念是否为真正的新发现，还是已知现象的重新命名\n   - 5 个 confidence signal 中哪些是新提出的、哪些是已有方法的直接套用\n   - Soft Jaccard with Hungarian matching 的技术新颖性如何\n   - 对比 Nedellec et al. (2026)，本文的增量贡献是否足够支撑 EMNLP 长文\n   - \"systematic comparison\" 类论文在 EMNLP 的接受标准——是否有足够的 insight 而非仅仅是 benchmark\n\n2. **Related Work 完整性**：\n   - Self-consistency 线：Wang et al. (2023), Chen et al. (2024), Taubenfeld et al. (2025), Kang et al. (2025) 等是否全面\n   - Structured IE 线：是否遗漏重要的 generative IE / constrained decoding 工作\n   - Uncertainty/calibration 线：是否遗漏关键方法（如 conformal prediction 在 NLP 中的应用）\n   - Test-time compute scaling 线：Snell et al. (2024), Brown et al. (2024) 之外是否有遗漏\n   - 是否有 2025-2026 年的重要新工作被遗漏\n   - **验证引用真实性**：抽查至少 5 篇引用，确认作者、年份、标题、venue 是否正确（特别关注 2025-2026 年的引用）\n\n3. **整体连贯性**：\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的叙事线是否一致\n   - Claims 是否都有实验支撑，是否有 overclaim\n   - \"Strong Predictors, Weak Selectors\" 标题是否准确反映论文内容\n   - Contribution list 是否与实际内容匹配\n   - Discussion section 是否有多余的推测性内容\n\n4. **写作质量**：\n   - 术语一致性（signal names、metric names）\n   - 图表标题是否自足（self-contained）\n   - 数学符号是否一致\n   - 是否有 repetitive content 或不必要的冗余\n\n5. **遗漏的重要引用搜索**：\n   - 请用 web_search 搜索以下关键词，检查是否有遗漏的重要 2025-2026 工作：\n     - \"self-consistency structured prediction 2025 2026\"\n     - \"confidence estimation information extraction LLM 2025 2026\"\n     - \"test-time scaling NER relation extraction 2025 2026\"\n\n请按 EMNLP 顶会最严格标准评审，不留情面。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Missing References → Questions → Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-15T01:50:44.473560+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1723
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-15T01:50:48.942058+00:00_

Round 1 任务已分配：
- **R1**（方法严谨性 + 实验设计 + 统计有效性）→ 已触发
- **R2**（新颖性 + Related Work 完整性 + 整体连贯性）→ 已触发

等待两位 Reviewer 返回初审结果。收到后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 8

## Round 8

18 recorded events


### User

_source line 95 · 2026-05-15T01:55:46.425590+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿完成

### 总体评分
**Overall**: 3.0/5（Findings track acceptance）
**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5
**Confidence**: 4/5

### 核心判断
论文选择了有价值的研究问题，实验设计合理、统计检验到位。但作为 EMNLP 主会长文有三个核心不足：

### Must-Fix 问题 (3 个)

**N1** [critical] "Correlation-selection gap" 的解释力不足——4/5 个 signals 是 instance-level 的，它们不能做 per-sample selection 是定义上的必然结果，不是发现。真正需要深入分析的是唯一的 per-sample signal (logprob) 为何也失败（calibration? length bias? constrained decoding 干扰?），但论文对此几乎没有分析。

**N2** [critical] Per-sample signal 探索严重不足——5 个 signals 中只有 logprob 1 个能做 per-sample selection，论文却声称 "systematic comparison"。LOO-SJ 已在 Appendix D 计算（Δρ=-0.014），但未测试其 selection 能力——这是一个自然的 per-sample structural signal。Consensus-proximity ranking 也未被分析。

**N3** [critical] 对 Nedellec et al. (2026) 的增量贡献论证不足。三个区分点中：selection 结论是负面的、multi-domain 是标准做法、SJ 的优势不一致（CoNLL 上 EM > SJ，conditional filtering 后 EM > SJ）。

### Should-Fix 问题 (5 个)
- W1: "first systematic evaluation" claim 过强，需收窄 scope
- W2: 遗漏 Singer et al. (2026) conformal prediction for NER（arXiv:2601.16999）和 ICLR 2025 conformal structured prediction
- W3: 遗漏 "Optimal Self-Consistency" (arXiv:2511.12309) 和 "Difficulty-Adaptive SC" (NAACL 2025 Findings)
- W4: 实验规模偏小（仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 非典型 generative IE 设置）
- W5: ρ-AUROC dissociation 机制分析浅，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应

### 引用真实性
46 篇中 43 篇验证通过。`nedellec2026consistency` 第一作者应为 Yao 而非 Nédellec，论文中 "Nedellec et al." 引用有误。`lightman2024verify` 和 `hobelsberger2025systematic` 未匹配但属 API 问题，实质上是真实论文。

### 遗漏重要引用
1. Singer et al. (2026) "UQ for NER via Conformal Prediction"
2. Conformal Structured Prediction (ICLR 2025)
3. Optimal Self-Consistency (arXiv:2511.12309)
4. Difficulty-Adaptive Self-Consistency (NAACL 2025 Findings)
5. Generative Self-Aggregation (arXiv:2503.04104)

### 审稿判断
当前版本更适合 Findings track。如能深入分析 per-sample signal failure 原因、测试 LOO-SJ 等 per-sample structural signals、讨论 constrained decoding 影响，可提升至主会水准。

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

_source line 96 · 2026-05-15T01:56:00.522361+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-15T01:56:00.573069+00:00_



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

_source line 98 · 2026-05-15T01:56:03.186343+00:00_

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

_source line 99 · 2026-05-15T01:56:03.186747+00:00_

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


### Tool result

_source line 100 · 2026-05-15T01:56:03.488653+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (73 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_017_llama_conll_n16_s456_r1024（准备中）\n- exp_017_llama_conll_n16_r1024（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n- exp_007_ner_llama（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp008_re_n16（准备中）\n\n## 近期结论\n- **exp_002_conll_n16_r1024** (killed): —\n- **exp_007_llama_n16_r1024** (killed): —\n- **exp_017_llama_conll_n16_s123_r1024** (killed): —\n\n## 趋势\n成功 37 / 负向 18 / 失败 1 / 共 64\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-15T01:56:03.489249+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-15T01:56:07.659489+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
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
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-15T01:56:08.061653+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-15T01:56:08.162386+00:00_

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

_source line 105 · 2026-05-15T01:56:08.213090+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

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

_source line 106 · 2026-05-15T01:56:10.774989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-15T01:56:11.026529+00:00_

1	---
2	round: 0
3	overall_score: borderline
4	timestamp: 2026-05-14T12:20:27.321042+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告：Round 1 圆桌审稿
11	
12	**论文**: "Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"
13	**目标 Venue**: EMNLP 2026 (ARR)
14	**Reviewer 配置**: R1（方法与实验）+ R2（新颖性与相关工作）
15	**轮次**: Round 1（已收敛，无需第二轮）
16	
17	---
18	
19	## Summary
20	
21	本文系统比较了 5 种 training-free confidence signals（Log-Probability、Entropy、Set Jaccard、Token Jaccard、Exact-Match）在 LLM-based 结构化信息抽取（NER/RE）的 best-of-N selection 场景中的表现。核心发现：(1) Set Jaccard (SJ) 在 NER 上显著优于 log-probability (Δρ≈0.16, p<10⁻²⁵)；(2) RE 中所有 signal 退化，归因于 compound error propagation。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个 8B 模型，多 seed/多温度/OOD 等消融维度。
22	
23	---
24	
25	## Strengths
26	
27	**S1. 系统且全面的实验矩阵** [R1+R2 共识]
28	5 signal × 3 NER dataset × 1 RE dataset × 2 model × 2 budget × 2 temperature × 4 metric，13/15 实验完整覆盖。该领域首个如此系统的比较（限定为 LLM-based structured IE）。
29	
30	**S2. LOO-SJ circularity check 方法论亮点** [R1 提出，R2 认可]
31	Table 1 Leave-one-out SJ（ρ=0.40 vs full SJ ρ=0.42, Δ=0.02）严谨地排除了 SJ 有效性依赖于自我循环的担忧。
32	
33	**S3. Compound error boundary 诊断有理论价值** [R1 提出，R2 认可]
34	Section 5.9 对 RE 退化的因果分析（head + tail + relation type 三重叠加），Table 12 per-relation-type 证据具体。
35	
36	**S4. 多维度鲁棒性验证** [R1+R2 共识]
37	Multi-seed（Std ≤ 0.01）、cross-dataset（排序一致）、cross-model、OOD（SJ-LP gap 从 +0.15 降至 +0.12 但仍显著）。
38	
39	**S5. Best-of-N selection 实用性** [R2 提出]
40	将 ranking 指标转化为 F1 gain，对 practitioners 有直接指导价值。
41	
42	**S6. Inverted-U pattern** [R1 提出]
43	Section 5.11, Table 15: SJ ρ 在 F1 bucket [0.3, 0.7] 最高，为 SJ 适用条件划定边界。
44	
45	---
46	
47	## Weaknesses（按严重程度排序）
48	
49	### Must-Fix（影响接收决定）
50	
51	**C1. 模型规模单一，严重限制普适性** [R1 critical + R2 agree]
52	仅 Qwen3-8B 和 LLaMA-3.1-8B 两个同规模模型。Confidence calibration 和 output diversity 随规模变化显著——更大模型的 greedy 可能已足够准确使 LP 优势明显化，更小模型高方差可能放大 SJ 优势。Abstract 中 "establis
…[truncated 6634 chars]

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

_source line 108 · 2026-05-15T01:56:11.027006+00:00_

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

_source line 109 · 2026-05-15T01:56:11.078318+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "模型规模单一（仅 2 个 8B 模型），严重限制普适性主张"
4	    category: experiment
5	    severity: critical
6	    status: open
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2]
12	        note: "R1 列为 critical，R2 列为 warning 但交叉回应中 AGREE。两位 reviewer 共识：8B→8B 仅验证架构鲁棒性非规模鲁棒性。建议增加 >30B 或 <3B 模型，或降级 establish 措辞。"
13	    action_items: []
14	    resolution: ""
15	    resolution_round: null
16	
17	  - id: "R1-N2"
18	    summary: "成本分析将 8-16× 推理开销描述为 negligible，存在误导"
19	    category: method
20	    severity: critical
21	    status: open
22	    first_raised_round: 1
23	    last_seen_round: 1
24	    mentions:
25	      - round: 1
26	        reviewers: [1, 2]
27	        note: "R1 定为 critical（系统性误导），R2 认为 TTS 语境下 O(N²) vs O(N) 陈述准确但需补充 cost-effectiveness 分析。分歧在严重程度，共识在需要补充分析。"
28	    action_items: []
29	    resolution: ""
30	    resolution_round: null
31	
32	  - id: "R1-N3"
33	    summary: "全文零图表（17 表 0 图），不符合 confidence/calibration 研究惯例"
34	    category: writing
35	    severity: critical
36	    status: open
37	    first_raised_round: 1
38	    last_seen_round: 1
39	    mentions:
40	      - round: 1
41	        reviewers: [1, 2]
42	        note: "两位 reviewer 完全一致。缺少 selection curves、reliability diagrams、cost-effectiveness scatter。Table 8 有数据但以表格呈现。建议至少添加 3 个核心 Figure。"
43	    action_items: []
44	    resolution: ""
45	    resolution_round: null
46	
47	  - id: "R2-N1"
48	    summary: "SJ 方法新颖性有限——评估指标到 confidence 的自然迁移，缺少 kernel 消融"
49	    category: method
50	    severity: critical
51	    status: open
52	    first_raised_round: 1
53	    last_seen_round: 1
54	    mentions:
55	      - round: 1
56	        reviewers: [1, 2]
57	        note: "R2 提出，R1 交叉回应 AGREE。type-grouped Hungarian matching + token-overlap kernel 本质是 set-level F1/Jaccard 的 confidence 版本。缺少与 edit distance、embedding similarity 等 kernel 的消融。"
58	    action_items: []
59	    resolution: ""
60	    resolution_round: null
61	
62	  - id: "R2-
…[truncated 7209 chars]

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

_source line 110 · 2026-05-15T01:56:42.267569+00:00_

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

_source line 111 · 2026-05-15T01:56:42.318520+00:00_

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
…[truncated 2458 chars]

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


### Assistant

_source line 112 · 2026-05-15T01:57:21.376559+00:00_

**Reviewer 2 Round 1 初审已收到。** 

R2 核心发现：
- **3 个 Must-Fix**：correlation-selection gap 解释力不足（instance-level signals 不能做 per-sample selection 是定义必然）、per-sample signal 探索严重不足（5 个 signals 中仅 1 个 per-sample）、对 Nedellec et al. (2026) 增量贡献论证不充分
- **5 个 Should-Fix**：claim 过强、遗漏 5 篇引用（Singer et al., Conformal Prediction, Optimal SC, Difficulty-Adaptive SC, Generative Self-Aggregation）、实验规模偏小、ρ-AUROC dissociation 机制分析浅
- **Overall**: 3.0/5 — Findings track 可接受，主会不足
- **引用真实性**：46 篇中 43 篇通过，`nedellec2026consistency` 第一作者有误

与 Round 0 对比，R2 新增了一个重要视角：**correlation vs. selection 的概念区分**——instance-level signals（Entropy/TJ/EM/SJ）在定义上无法做 per-sample selection，这不算"发现"。唯一能做 per-sample selection 的 logprob 为何也失败，论文分析不足。

**等待 Reviewer 1 的 Round 1 审稿返回后，将进入交叉分享阶段。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 9

## Round 9

8 recorded events


### User

_source line 113 · 2026-05-15T01:57:22.669347+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：Overall 3.0/5，建议 Findings track。三个 critical 问题：(1) correlation-selection gap 是定义推论而非发现，logprob failure 分析缺失；(2) per-sample signal 只测了 logprob 一个，LOO-SJ 未测 selection；(3) 与 Nedellec 2026 增量贡献论证不足。另有 5 个 should-fix（遗漏 conformal prediction for NER 等重要引用、"first" claim 过强、实验规模偏小等）。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

### 审查侧重：方法严谨性 + 实验设计 + 统计有效性

---

## 总体评分

**Overall**: 3/5 — Findings
**一句话总结**: 研究问题清晰、实验设计规范，"correlation-selection gap"概念有价值，但仅限 8B 模型、单一 RE 数据集、统计检验细节不足，核心负面结论的证据强度不够支撑 Main Conference。

## 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 五个 signal 定义基本严谨，实验设计合理，但 bootstrap 检验细节缺失、Soft Jaccard 形式化有歧义、logprob 温度敏感性缺失削弱了方法论完整性 |
| Excitement | 3/5 | 质量估计 vs. 样本选择的解耦和 correlation-selection gap 概念有洞见；但核心结论是负面结果（signals 不优于 greedy），且实用指导有限 |
| Reproducibility | 3.5/5 | 数据集公开、信号定义有公式，但 LoRA 配置仅给 r=32、prompt 格式未展示、vLLM 约束解码具体配置缺失、bootstrap 参数不明 |
| Confidence | 4/5 | 与本文方向（uncertainty estimation + IE + test-time scaling）有扎实背景 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] Bootstrap 检验细节严重不足，核心统计结论无法验证

- 具体位置：Section 5.3, "p=0.39, 3-seed bootstrap; Cohen's d=0.038"
- 问题：论文的核心负面结论（"no signal reliably surpasses greedy"）完全建立在 p=0.39 这一 bootstrap 检验上，但以下关键细节未报告：(1) bootstrap 迭代次数；(2) 是 paired bootstrap 还是 unpaired；(3) 检验统计量是什么；(4) "3-seed bootstrap"的含义不明——是对 3 个 seed 做 bootstrap（n=3，完全无统计功效），还是在每个 seed 内对 instance 做 bootstrap 再合并？如果是前者，p=0.39 无任何诊断价值。
- 为什么影响接收：这是支撑全文标题（"Weak Selectors"）和主要贡献（contribution #2）的唯一定量证据。

**N2** [critical] 仅 8B 模型，"model-agnostic" claim 缺乏支撑

- 具体位置：Section 5.1, 5.4, Discussion 多处使用"model-agnostic"
- 问题：只测试了 Qwen3-8B 和 LLaMA-3.1-8B-Instruct——同一参数规模。70B+ 模型可能产生更高质量更多样的样本，从根本上改变 correlation-selection gap 的形态。Limitations 承认了这一点，但 Discussion 仍使用"model-agnostic"措辞，形成内部矛盾（ARR R4 overclaiming）。

**N3** [critical] RE 结论仅基于 SciERC，44% zero-F1 floor effect 严重扭曲信号评估

- 具体位置：Section 5.1, Limitations 第 1 段
- 问题：RE 的所有结论全部来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。论文声称覆盖"NER and RE"但 RE 实验基础极其薄弱。

## Should-Fix 问题

**W1** [warning] Soft Jaccard 形式化有歧义：g_i/g_j 未定义，sim 具体公式缺失，Hungarian algorithm 匹配阈值未说明。

**W2** [warning] Entity voting 的 mean frequency 聚合方式未讨论替代选择（median、thresholded voting 等），当模型产生大量低频幻觉实体时 |E_∪| 膨胀导致置信度系统性偏低。

**W3** [warning] ρ=0.38 被反复描述为"effective/strong quality estimation"但仅解释 ~14% F1 方差，未与 uncertainty estimation 文献中其他方法的 ρ 对比 contextualize。

**W4** [warning] Logprob（唯一 per-sample signal、selection 最佳信号）的温度敏感性数据缺失（T=0.7 unavailable），但论文做出了"signals robust across temperatures"的笼统结论。

**W5** [warning] WNUT-17 p=0.106 被解读为"establishing the capability boundary where all signals break down"，措辞过于确定——fail to reject null ≠ accept null。

**W6** [warning] Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct（未说明是否微调）训练设置不对称，可能混淆 cross-model 比较。

**W7** [warning] 约束解码对 sampling diversity 的影响未讨论——这可能是 correlation-selection gap 的一个成因。

## 小问题

- Table 2 EM "---" 需更显著的解释
- Limitations 提到"logistic regression proxy as an upper bound"但正文/Appendix 无此分析结果
- snell2024scaling bib 作者格式与 OpenAlex 有 mismatch
- Cross-model Δ=0.005 未报告是否在 bootstrap CI 内
- Introduction "+18pp on GSM8K" 未注明具体模型(PaLM-540B)
- Appendix D \textsc 编译检查

## 主要优势

1. 研究问题定义精准：quality estimation vs. sample selection 的解耦是有价值的概念贡献
2. 实验设计的系统性出色：5 signals × 3 families × 3 datasets × 2 models × 2 N × 2 T + 多项辅助分析
3. Task difficulty gradient 设计合理（CoNLL/SciERC/WNUT），信号排序随难度变化的发现有实用价值
4. 统计实践总体规范（p-values, Cohen's d, CI, 3-seed, Fisher z-test, LOO circularity check）
5. Limitations section 全面诚实

## Overall Assessment

**Verdict: Borderline → Weak Accept for Findings**

核心顾虑：(1) bootstrap 细节不足以确认核心负面结论成立（N1）；(2) model-agnostic overclaim（N2）；(3) RE 结论基础薄弱（N3）。如果 N1 确认执行正确、N2/N3 做适当限定，适合 Findings。进入 Main Conference 需要额外模型规模或 RE 数据集验证。

---

[Reviewer 1 审稿结果]:
Round 1 审稿完成，已汇报给 Review Director。

核心判断：**Overall 3/5 (Findings)**。三个 Must-Fix 问题：(1) bootstrap 检验细节严重不足，核心"Weak Selectors"结论的统计基础无法验证；(2) 仅两个 8B 模型却声称 model-agnostic，overclaim；(3) RE 结论仅依赖 SciERC 一个数据集且 44% 零分样本严重扭曲评估。七个 Should-Fix 问题涵盖 Soft Jaccard 形式化歧义、entity voting 聚合方式、ρ=0.38 的 contextualization、logprob 温度数据缺失、WNUT-17 解读过于强硬、模型训练设置不对称、约束解码对 diversity 的影响。

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

_source line 114 · 2026-05-15T01:57:35.765434+00:00_

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

_source line 115 · 2026-05-15T01:57:35.816046+00:00_



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

_source line 116 · 2026-05-15T01:58:06.092521+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见\n\n请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### 总体评分\n**Overall**: 3.0/5（Findings track acceptance）\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5\n**Confidence**: 4/5\n\n### 核心判断\n论文选择了有价值的研究问题，实验设计合理、统计检验到位。但作为 EMNLP 主会长文有三个核心不足：\n\n### Must-Fix 问题 (3 个)\n\n**N1** [critical] \"Correlation-selection gap\" 的解释力不足——4/5 个 signals 是 instance-level 的，它们不能做 per-sample selection 是定义上的必然结果，不是发现。真正需要深入分析的是唯一的 per-sample signal (logprob) 为何也失败（calibration? length bias? constrained decoding 干扰?），但论文对此几乎没有分析。\n\n**N2** [critical] Per-sample signal 探索严重不足——5 个 signals 中只有 logprob 1 个能做 per-sample selection，论文却声称 \"systematic comparison\"。LOO-SJ 已在 Appendix D 计算（Δρ=-0.014），但未测试其 selection 能力——这是一个自然的 per-sample structural signal。Consensus-proximity ranking 也未被分析。\n\n**N3** [critical] 对 Nedellec et al. (2026) 的增量贡献论证不足。三个区分点中：selection 结论是负面的、multi-domain 是标准做法、SJ 的优势不一致（CoNLL 上 EM > SJ，conditional filtering 后 EM > SJ）。\n\n### Should-Fix 问题 (5 个)\n- W1: \"first systematic evaluation\" claim 过强，需收窄 scope\n- W2: 遗漏 Singer et al. (2026) conformal prediction for NER（arXiv:2601.16999）和 ICLR 2025 conformal structured prediction\n- W3: 遗漏 \"Optimal Self-Consistency\" (arXiv:2511.12309) 和 \"Difficulty-Adaptive SC\" (NAACL 2025 Findings)\n- W4: 实验规模偏小（仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 非典型 generative IE 设置）\n- W5: ρ-AUROC dissociation 机制分析浅，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应\n\n### 引用真实性\n46 篇中 43 篇验证通过。`nedellec2026consistency` 第一作者应为 Yao 而非 Nédellec，论文中 \"Nedellec et al.\" 引用有误。`lightman2024verify` 和 `hobelsberger2025systematic` 未匹配但属 API 问题，实质上是真实论文。\n\n### 遗漏重要引用\n1. Singer et al. (2026) \"UQ for NER via Conformal Prediction\"\n2. Conformal Structured Prediction (ICLR 2025)\n3. Optimal Self-Consistency (arXiv:2511.12309)\n4. Difficulty-Adaptive Self-Consistency (NAACL 2025 Findings)\n5. Generative Self-Aggregation (arXiv:2503.04104)\n\n### 审稿判断\n当前版本更适合 Findings track。如能深入分析 per-sample signal failure 原因、测试 LOO-SJ 等 per-sample structural signals、讨论 constrained decoding 影响，可提升至主会水准。"
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
    "text": "## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见\n\n请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### 总体评分\n**Overall**: 3.0/5（Findings track acceptance）\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5\n**Confidence**: 4/5\n\n### 核心判断\n论文选择了有价值的研究问题，实验设计合理、统计检验到位。但作为 EMNLP 主会长文有三个核心不足：\n\n### Must-Fix 问题 (3 个)\n\n**N1** [critical] \"Correlation-selection gap\" 的解释力不足——4/5 个 signals 是 instance-level 的，它们不能做 per-sample selection 是定义上的必然结果，不是发现。真正需要深入分析的是唯一的 per-sample signal (logprob) 为何也失败（calibration? length bias? constrained decoding 干扰?），但论文对此几乎没有分析。\n\n**N2** [critical] Per-sample signal 探索严重不足——5 个 signals 中只有 logprob 1 个能做 per-sample selection，论文却声称 \"systematic comparison\"。LOO-SJ 已在 Appendix D 计算（Δρ=-0.014），但未测试其 selection 能力——这是一个自然的 per-sample structural signal。Consensus-proximity ranking 也未被分析。\n\n**N3** [critical] 对 Nedellec et al. (2026) 的增量贡献论证不足。三个区分点中：selection 结论是负面的、multi-domain 是标准做法、SJ 的优势不一致（CoNLL 上 EM > SJ，conditional filtering 后 EM > SJ）。\n\n### Should-Fix 问题 (5 个)\n- W1: \"first systematic evaluation\" claim 过强，需收窄 scope\n- W2: 遗漏 Singer et al. (2026) conformal prediction for NER（arXiv:2601.16999）和 ICLR 2025 conformal structured prediction\n- W3: 遗漏 \"Optimal Self-Consistency\" (arXiv:2511.12309) 和 \"Difficulty-Adaptive SC\" (NAACL 2025 Findings)\n- W4: 实验规模偏小（仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 非典型 generative IE 设置）\n- W5: ρ-AUROC dissociation 机制分析浅，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应\n\n### 引用真实性\n46 篇中 43 篇验证通过。`nedellec2026consistency` 第一作者应为 Yao 而非 Nédellec，论文中 \"Nedellec et al.\" 引用有误。`lightman2024verify` 和 `hobelsberger2025systematic` 未匹配但属 API 问题，实质上是真实论文。\n\n### 遗漏重要引用\n1. Singer et al. (2026) \"UQ for NER via Conformal Prediction\"\n2. Conformal Structured Prediction (ICLR 2025)\n3. Optimal Self-Consistency (arXiv:2511.12309)\n4. Difficulty-Adaptive Self-Consistency (NAACL 2025 Findings)\n5. Generative Self-Aggregation (arXiv:2503.04104)\n\n### 审稿判断\n当前版本更适合 Findings track。如能深入分析 per-sample signal failure 原因、测试 LOO-SJ 等 per-sample structural signals、讨论 constrained decoding 影响，可提升至主会水准。"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-15T01:58:23.884066+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17791
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-15T01:58:24.337233+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整 Round 1 审稿意见\n\n请逐条回应 Reviewer 1 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### 总体评分\n**Overall**: 3/5 — Findings\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 3.5/5\n**Confidence**: 4/5\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Bootstrap 检验细节严重不足，核心统计结论无法验证\n\n- 具体位置：Section 5.3, \"p=0.39, 3-seed bootstrap; Cohen's d=0.038\"\n- 问题：论文的核心负面结论（\"no signal reliably surpasses greedy\"）完全建立在 p=0.39 这一 bootstrap 检验上，但以下关键细节未报告：(1) bootstrap 迭代次数；(2) 是 paired bootstrap 还是 unpaired；(3) 检验统计量是什么；(4) \"3-seed bootstrap\"的含义不明——是对 3 个 seed 做 bootstrap（n=3，完全无统计功效），还是在每个 seed 内对 instance 做 bootstrap 再合并？如果是前者，p=0.39 无任何诊断价值。\n- 为什么影响接收：这是支撑全文标题（\"Weak Selectors\"）和主要贡献（contribution #2）的唯一定量证据。\n\n**N2** [critical] 仅 8B 模型，\"model-agnostic\" claim 缺乏支撑\n\n- 具体位置：Section 5.1, 5.4, Discussion 多处使用\"model-agnostic\"\n- 问题：只测试了 Qwen3-8B 和 LLaMA-3.1-8B-Instruct——同一参数规模。70B+ 模型可能产生更高质量更多样的样本，从根本上改变 correlation-selection gap 的形态。Limitations 承认了这一点，但 Discussion 仍使用\"model-agnostic\"措辞，形成内部矛盾（ARR R4 overclaiming）。\n\n**N3** [critical] RE 结论仅基于 SciERC，44% zero-F1 floor effect 严重扭曲信号评估\n\n- 具体位置：Section 5.1, Limitations 第 1 段\n- 问题：RE 的所有结论全部来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。论文声称覆盖\"NER and RE\"但 RE 实验基础极其薄弱。\n\n### Should-Fix 问题\n\n**W1** [warning] Soft Jaccard 形式化有歧义：g_i/g_j 未定义，sim 具体公式缺失，Hungarian algorithm 匹配阈值未说明。\n\n**W2** [warning] Entity voting 的 mean frequency 聚合方式未讨论替代选择（median、thresholded voting 等），当模型产生大量低频幻觉实体时 |E_∪| 膨胀导致置信度系统性偏低。\n\n**W3** [warning] ρ=0.38 被反复描述为\"effective/strong quality estimation\"但仅解释 ~14% F1 方差，未与 uncertainty estimation 文献中其他方法的 ρ 对比 contextualize。\n\n**W4** [warning] Logprob（唯一 per-sample signal、selection 最佳信号）的温度敏感性数据缺失（T=0.7 unavailable），但论文做出了\"signals robust across temperatures\"的笼统结论。\n\n**W5** [warning] WNUT-17 p=0.106 被解读为\"establishing the capability boundary where all signals break down\"，措辞过于确定——fail to reject null ≠ accept null。\n\n**W6** [warning] Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct（未说明是否微调）训练设置不对称，可能混淆 cross-model 比较。\n\n**W7** [warning] 约束解码对 sampling diversity 的影响未讨论——这可能是 correlation-selection gap 的一个成因。\n\n### 小问题\n- Table 2 EM \"---\" 需更显著的解释\n- Limitations 提到\"logistic regression proxy as an upper bound\"但正文/Appendix 无此分析结果\n- snell2024scaling bib 作者格式与 OpenAlex 有 mismatch\n- Cross-model Δ=0.005 未报告是否在 bootstrap CI 内\n- Introduction \"+18pp on GSM8K\" 未注明具体模型(PaLM-540B)\n- Appendix D \\textsc 编译检查\n\n### 主要优势\n1. 研究问题定义精准：quality estimation vs. sample selection 的解耦是有价值的概念贡献\n2. 实验设计的系统性出色：5 signals × 3 families × 3 datasets × 2 models × 2 N × 2 T + 多项辅助分析\n3. Task difficulty gradient 设计合理（CoNLL/SciERC/WNUT），信号排序随难度变化的发现有实用价值\n4. 统计实践总体规范（p-values, Cohen's d, CI, 3-seed, Fisher z-test, LOO circularity check）\n5. Limitations section 全面诚实\n\n### Overall Assessment\n**Verdict: Borderline → Weak Accept for Findings**\n核心顾虑：(1) bootstrap 细节不足以确认核心负面结论成立（N1）；(2) model-agnostic overclaim（N2）；(3) RE 结论基础薄弱（N3）。如果 N1 确认执行正确、N2/N3 做适当限定，适合 Findings。进入 Main Conference 需要额外模型规模或 RE 数据集验证。"
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
    "text": "## 交叉分享：Reviewer 1 的完整 Round 1 审稿意见\n\n请逐条回应 Reviewer 1 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### 总体评分\n**Overall**: 3/5 — Findings\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 3.5/5\n**Confidence**: 4/5\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Bootstrap 检验细节严重不足，核心统计结论无法验证\n\n- 具体位置：Section 5.3, \"p=0.39, 3-seed bootstrap; Cohen's d=0.038\"\n- 问题：论文的核心负面结论（\"no signal reliably surpasses greedy\"）完全建立在 p=0.39 这一 bootstrap 检验上，但以下关键细节未报告：(1) bootstrap 迭代次数；(2) 是 paired bootstrap 还是 unpaired；(3) 检验统计量是什么；(4) \"3-seed bootstrap\"的含义不明——是对 3 个 seed 做 bootstrap（n=3，完全无统计功效），还是在每个 seed 内对 instance 做 bootstrap 再合并？如果是前者，p=0.39 无任何诊断价值。\n- 为什么影响接收：这是支撑全文标题（\"Weak Selectors\"）和主要贡献（contribution #2）的唯一定量证据。\n\n**N2** [critical] 仅 8B 模型，\"model-agnostic\" claim 缺乏支撑\n\n- 具体位置：Section 5.1, 5.4, Discussion 多处使用\"model-agnostic\"\n- 问题：只测试了 Qwen3-8B 和 LLaMA-3.1-8B-Instruct——同一参数规模。70B+ 模型可能产生更高质量更多样的样本，从根本上改变 correlation-selection gap 的形态。Limitations 承认了这一点，但 Discussion 仍使用\"model-agnostic\"措辞，形成内部矛盾（ARR R4 overclaiming）。\n\n**N3** [critical] RE 结论仅基于 SciERC，44% zero-F1 floor effect 严重扭曲信号评估\n\n- 具体位置：Section 5.1, Limitations 第 1 段\n- 问题：RE 的所有结论全部来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。论文声称覆盖\"NER and RE\"但 RE 实验基础极其薄弱。\n\n### Should-Fix 问题\n\n**W1** [warning] Soft Jaccard 形式化有歧义：g_i/g_j 未定义，sim 具体公式缺失，Hungarian algorithm 匹配阈值未说明。\n\n**W2** [warning] Entity voting 的 mean frequency 聚合方式未讨论替代选择（median、thresholded voting 等），当模型产生大量低频幻觉实体时 |E_∪| 膨胀导致置信度系统性偏低。\n\n**W3** [warning] ρ=0.38 被反复描述为\"effective/strong quality estimation\"但仅解释 ~14% F1 方差，未与 uncertainty estimation 文献中其他方法的 ρ 对比 contextualize。\n\n**W4** [warning] Logprob（唯一 per-sample signal、selection 最佳信号）的温度敏感性数据缺失（T=0.7 unavailable），但论文做出了\"signals robust across temperatures\"的笼统结论。\n\n**W5** [warning] WNUT-17 p=0.106 被解读为\"establishing the capability boundary where all signals break down\"，措辞过于确定——fail to reject null ≠ accept null。\n\n**W6** [warning] Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct（未说明是否微调）训练设置不对称，可能混淆 cross-model 比较。\n\n**W7** [warning] 约束解码对 sampling diversity 的影响未讨论——这可能是 correlation-selection gap 的一个成因。\n\n### 小问题\n- Table 2 EM \"---\" 需更显著的解释\n- Limitations 提到\"logistic regression proxy as an upper bound\"但正文/Appendix 无此分析结果\n- snell2024scaling bib 作者格式与 OpenAlex 有 mismatch\n- Cross-model Δ=0.005 未报告是否在 bootstrap CI 内\n- Introduction \"+18pp on GSM8K\" 未注明具体模型(PaLM-540B)\n- Appendix D \\textsc 编译检查\n\n### 主要优势\n1. 研究问题定义精准：quality estimation vs. sample selection 的解耦是有价值的概念贡献\n2. 实验设计的系统性出色：5 signals × 3 families × 3 datasets × 2 models × 2 N × 2 T + 多项辅助分析\n3. Task difficulty gradient 设计合理（CoNLL/SciERC/WNUT），信号排序随难度变化的发现有实用价值\n4. 统计实践总体规范（p-values, Cohen's d, CI, 3-seed, Fisher z-test, LOO circularity check）\n5. Limitations section 全面诚实\n\n### Overall Assessment\n**Verdict: Borderline → Weak Accept for Findings**\n核心顾虑：(1) bootstrap 细节不足以确认核心负面结论成立（N1）；(2) model-agnostic overclaim（N2）；(3) RE 结论基础薄弱（N3）。如果 N1 确认执行正确、N2/N3 做适当限定，适合 Findings。进入 Main Conference 需要额外模型规模或 RE 数据集验证。"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-15T01:58:25.997325+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1660
}
```

</details>

---


### Assistant

_source line 120 · 2026-05-15T01:58:39.247748+00:00_

交叉分享已发出。两位 Reviewer 的完整审稿意见已互相转发，等待各自逐条回应（`[AGREE]` / `[REBUT]`）。

**当前进度**：
- Round 1 独立审稿 ✅（R1: 3/5 Findings, R2: 3.0/5 Findings）
- 交叉分享 ✅（已互发完整原文）
- 等待交叉回应 ⏳

**两位 Reviewer 的共识方向**：
- 评分一致：均给 3/5，建议 Findings track
- 共同关切：模型规模仅 8B、RE 仅 SciERC 单数据集、overclaiming 措辞
- 互补视角：R1 聚焦统计检验细节（bootstrap）和方法形式化；R2 聚焦概念贡献力度（correlation-selection gap 是否为真发现）和文献完整性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 121 · 2026-05-15T02:01:28.386410+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

### Must-Fix 问题

**[AGREE with nuance] R2-N1: Correlation-selection gap 的解释力**

同意 R2 的核心判断：4/5 instance-level signals 无法做 per-sample selection 在定义上是预期的（Section 3.1 明确区分了 per-sample vs. instance-level，Eq. 5–8 只产出单一 score），这削弱了"发现"的新颖性。

但需补充两点：
1. 论文在 Section 3.3 中通过"select the sample closest to the consensus output"将 instance-level signals 转化为 per-sample 排序——这不是纯粹定义性的，是一个合理的 selection 策略，只不过效果不好（Table 5: SJ=0.645 vs. Greedy=0.644）。
2. R2 关于 logprob 失败原因分析不足的批评完全成立。论文仅在 Section 5.1 提到 conditional filtering 后"logprob RE collapses to ρ=0.011"（Figure 2 右），说明其 full-set correlation 来自 zero/non-zero 分离；Discussion 段简要提到 constrained decoding 可能的影响，但未做任何实验验证。作为唯一的 per-sample signal，logprob 值得至少一段深入分析。

**[REBUT] R2-N2: Per-sample signal 探索严重不足**

R2 认为 LOO-SJ 的 selection 能力"未被测试"，但这与论文实际实验不符。Section 3.3 明确说 instance-level signals 通过 consensus-proximity 选择候选样本。对于 SJ，consensus-proximity 就是：对每个 y_i 计算其对所有其他样本的平均 SJ——这在数学上等价于 LOO-SJ 排序。Table 5 中 SJ 行（NER F1=0.645, RE F1=0.386）就是 LOO-SJ 的 selection 结果，只是论文没有显式使用"LOO-SJ selection"这个术语。

真正的问题是论文没有把这个等价关系说清楚，是表述问题而非实验缺失。

不过，R2 关于只有 1 个 per-sample signal 的批评仍然有效——"systematic comparison" 但 per-sample 维度极度单薄。

**[AGREE] R2-N3: 对 Nedellec et al. (2026) 的增量贡献论证不足**

同意。补充发现：bib 文件中 nedellec2026consistency 的 author 字段确认第一作者是 Yao，论文全文使用"Nédellec et al."是事实性错误。SJ 优势不一致性确实削弱区分论证（CoNLL: EM ρ=0.451 > SJ ρ=0.436; conditional filtering 后 EM 在所有 4 个配置领先）。

但 negative selection result 本身仍有学术价值——Nedellec et al. 未涉及 selection，论文首次系统验证了 best-of-N selection 在 IE 中的失败。问题在于论证方式不够有力，而非贡献不存在。

### Should-Fix 问题

**[AGREE] R2-W1**: "first systematic" claim 需收窄，加限定语如"first to compare signals from multiple families for both quality estimation and sample selection in generative IE"。

**[REBUT] R2-W2**: 论文已引用 conformal prediction 代表性工作（Fisch 2021, Angelopoulos 2021）并在 Conclusion 讨论 future integration。Singer et al. 和 ICLR 2025 conformal 属不同研究路线（supervised conformal vs. unsupervised consistency），添加为 related work 合理，但非 critical omission。

**[AGREE] R2-W3**: Optimal Self-Consistency 和 Difficulty-Adaptive SC 与论文核心主题高度相关，应引用讨论。尤其后者——论文的核心发现之一就是 signal rankings depend on task difficulty。

**[AGREE with nuance] R2-W4**: 实验覆盖度在 EMNLP 标准下不算小（2 模型族 × 3 数据集 × robustness 分析）。但仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 设置确是限制。补充同意 R2 的"非典型设置"观点——LoRA fine-tuning 可能使模型输出分布比 hard-prompted 更集中，人为压低 sample diversity，使 selection signals 更难区分候选样本，这是潜在混淆变量。

**[AGREE] R2-W5**: EM=1 压缩效应在 Appendix D 有讨论但仅在 appendix，应在主文明确阐述。

### 引用真实性

**[AGREE]** nedellec2026consistency 第一作者应为 Yao，论文"Nédellec et al."引用有误，已从 bib 文件确认。

### 遗漏引用

- [AGREE] #3 Optimal SC, #4 Difficulty-Adaptive SC 应引用
- [REBUT] #1 Singer et al., #2 ICLR 2025 conformal 非 critical omission
- [NEUTRAL] #5 Generative Self-Aggregation 需确认内容再判断

### 审稿判断

[AGREE with qualification] 同意 Findings track 判断方向。核心问题：(1) gap 的理论贡献被部分定义性质削弱，(2) per-sample signal 维度单薄，(3) logprob 失败机制分析缺失。

对 R2 修改路径的补充建议：LOO-SJ 实际已隐式测试（Table 5 SJ 行），更有价值的方向是引入真正新的 per-sample signals（per-entity logprob、learned verifier probe）或分析 constrained decoding 对 logprob 信号的系统性扭曲。

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

_source line 122 · 2026-05-15T02:01:34.648387+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 11

## Round 11

1 recorded events


### User

_source line 123 · 2026-05-15T02:01:40.007584+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **N1**: 部分同意——4/5 signals 不能做 per-sample selection 确有定义性成分，但 consensus-proximity 策略不完全是 trivial 的；logprob 失败分析不足的批评完全成立
- **N2**: 反驳——LOO-SJ 通过 consensus-proximity 在 Table 5 已隐式测试（SJ 行），是表述问题而非实验缺失；但"只有 1 个 per-sample signal"的批评仍有效
- **N3**: 同意——增量论证弱，但 negative selection result 本身有学术价值；引用中 Yao→Nédellec 的错误已从 bib 确认
- **W1-W5**: W1/W3/W5 同意，W2 反驳（非 critical omission），W4 部分同意并补充 LoRA 作为混淆变量的观点
- **整体判断**: 同意 Findings track 方向，但建议修改路径侧重引入新 per-sample signals 和分析 constrained decoding 对 logprob 的影响

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


## Round 12

## Round 12

10 recorded events


### User

_source line 124 · 2026-05-15T02:02:56.107349+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 Round 1 意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Bootstrap 检验细节严重不足**

同意，且认为这是本文最关键的方法论缺陷。

逐一验证 R1 的子问题：
1. **Bootstrap 迭代次数**：全文未报告。Section 5.3 仅写 "p=0.39, 3-seed bootstrap; Cohen's d=0.038"，Appendix 未补充。
2. **Paired vs unpaired**：未说明。这对 best-of-N vs greedy 比较至关重要——paired bootstrap 在每个 instance 上匹配两种方法，统计功效远高于 unpaired。
3. **检验统计量**：未说明是对 F1 差值做 bootstrap，还是对 paired difference 做 bootstrap-t。
4. **"3-seed bootstrap" 含义**：这是最致命的歧义。对照 Table 1 的 N=16 block 使用 "3-seed mean±std" 的语境，"3-seed" 最可能指 3 次独立 sampling 的随机种子。如果 bootstrap 是在这 3 个 seed 的 mean F1 上做 (n=3)，则完全无统计功效——任何 p 值都没有诊断价值。即使是在每个 seed 内对 551 个 SciERC instance 做 paired bootstrap 再合并，论文也必须说明合并策略。

**补充发现**：论文在 5 处重复引用 "p>0.39, bootstrap"（Abstract、Introduction ×2、Section 5.3、Conclusion），但从未给出检验的完整规范。这个 p 值支撑了标题 ("Weak Selectors")、Contribution #2（correlation-selection gap）、以及 Discussion 中对 trained verifier 的呼吁。如果检验无效，论文的核心贡献坍塌为 "我们没有足够的统计功效来判断 selection 是否有效"——这是一个完全不同的结论。

---

**[AGREE] R1-N2: "Model-agnostic" overclaim，但需精确定位**

同意存在 overclaiming，但 R1 对问题的定位可以更精确。

论文中 "model-agnostic" 出现两处：
- Section 5.4 (experiments.tex:135): "The structural-over-logprob advantage is model-agnostic, holding across all four N=16 settings"
- Discussion (discussion.tex:8): "This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative"

两处的上下文都是在描述 Qwen3-8B 与 LLaMA-3.1-8B 之间的一致性。论文确实在 Limitations 中承认 "Whether our findings hold for larger models (70B+) or closed-source APIs remains untested"（limitations.tex:5-6）。R1 正确指出这构成内部矛盾。

然而，我认为修复成本很低：将 "model-agnostic" 替换为 "consistent across tested model families" 即可。核心发现（structural > logprob 在两个 8B 模型上一致）本身是有效的，overclaim 在于措辞而非实验设计。ARR R4 标准下，这是 Should-Fix 级别——需要措辞修正，但不构成一票否决。

---

**[AGREE] R1-N3: RE 结论仅基于 SciERC，但严重程度可适度下调**

同意 RE 实验基础薄弱。SciERC RE 是唯一的 RE 数据集，44% zero-F1 严重限制了信号区分度。论文自身在 Section 5.1 (experiments.tex:62) 承认 "all signals weaken due to the 44% zero-F1 floor effect"，Limitations 再次确认（limitations.tex:1-2），Appendix 的 per-relation diagnostic 也指出 "entity span errors account for 55.5% of RE false negatives"——这意味着 RE correlation 很大程度上反映 NER 上游错误传播，而非 RE 本身的信号质量。

但有两点缓和因素 R1 未提及：
1. **Conditional filtering**（Appendix, appendix.tex:120-121）移除 zero-F1 instance 后，SJ RE 恢复到 ρ=0.405，EM RE 达到 ρ=0.417——说明在 non-trivial subset 上信号仍有区分力。
2. **Capability stratification**（Appendix, appendix.tex:112）在高复杂度 RE 子集上，Voting 达到 ρ=0.630——说明信号在有足够结构信息时表现良好。

综合看：R1 说 "RE 的所有结论全部来自 SciERC RE 一个数据集" 是事实。但论文标题和贡献声称覆盖 "NER and RE"，RE 部分用 conditional analysis 做了缓解。我建议将 R1 的评估从 critical 降到 high-warning：要求作者在 Discussion 中更显式地限定 RE 结论的泛化范围，而非要求追加 RE 数据集实验（这超出 revision 的合理范围）。

---

### Should-Fix 问题

**[AGREE] R1-W1: Soft Jaccard 形式化有歧义**

同意。Eq. (4) 中 g_i, g_j 在文本中说是 "per-type extraction counts"（method.tex:43），但符号定义和 denominator 的直觉不够清晰——读者需要推断 denominator 是 type-wise max count 的求和。sim 在文本中定义为 "span-level Jaccard overlap"（method.tex:43），但未给出公式（是 token-level IoU 还是 character-level？）。Hungarian algorithm 的匹配阈值（e.g., 最低 overlap 要求）也未说明。

这些缺失不影响论文结论的有效性，但影响 reproducibility。

---

**[AGREE] R1-W2: Entity voting 的 mean frequency 聚合方式**

同意这是一个有效的方法论关注。Eq. (6) 用 |E_∪| 做分母，当模型产生大量低频幻觉实体时，|E_∪| 膨胀导致 c_vote 系统性偏低。论文未讨论替代方案（median frequency、frequency-thresholded voting、top-k entity filtering）。

补充一个 R1 未提到的相关问题：entity voting 和 Soft Jaccard 在概念上有 overlap——两者都基于 entity-level 跨 sample 一致性，只是聚合方式不同。论文未讨论这两个 structural signal 之间的冗余度（e.g., 它们的 instance-level correlation 是多少？）。如果高度相关，那么 "两个 structural signal 都优于 surface signal" 的论证就被削弱——实际上可能是同一个 signal 的两种近似。

---

**[REBUT] R1-W3: ρ=0.38 被描述为 "effective/strong"**

部分反驳。R1 的 framing 有偏差。

论文实际措辞是 "effective quality estimators"（Section 5.3 标题, discussion.tex:1-4）和 "strongest rank correlation"（discussion.tex:1），而非 "strong correlation"。"Strongest" 是相对于其他信号的比较级，"effective" 指向实用价值。论文从未声称 ρ=0.38 在绝对意义上 "strong"。

更重要的是，ρ 不是论文用来论证实用价值的唯一指标：AUROC=0.749（NER）和 0.706（RE）才是面向 routing/triage 应用的核心证据。AUROC 0.75 意味着 75% 的概率正确区分高/低质量 instance——这对于 "flagging uncertain instances for human review"（discussion.tex:15）而言是实用的。

但 R1 关于缺乏 contextualization 的批评部分成立：论文未与 uncertainty estimation 文献中的其他方法（如 semantic entropy、P(True)、ensemble-based uncertainty）的 ρ 值对比。这个对比在 Related Work 中是缺失的。

---

**[AGREE] R1-W4: Logprob 温度敏感性数据缺失**

同意。Section 5.4 (experiments.tex:132) 说 "Signal rankings are robust across temperatures"，但 logprob 是唯一的 per-sample signal（也是 Section 5.3 中 selection F1 最高的 signal），其 T=0.7 数据在 Limitations 中承认 "unavailable"（limitations.tex:15）。

这不仅是一个数据缺失问题，还影响论文的核心论点：如果 logprob 在 T=0.7 时 selection 表现显著不同，那么 "no signal reliably surpasses greedy" 的结论可能不成立。论文至少应将 "robust across temperatures" 的表述限定为 "consistency-based signals are robust across temperatures; logprob temperature sensitivity remains uncharacterized"。

---

**[AGREE] R1-W5: WNUT-17 "establishing the capability boundary" 措辞过度**

同意 R1 的统计学批评：fail to reject null ≠ accept null。p=0.106 不能 "establish" 一个 boundary。

但补充 R1 未提到的一点：WNUT-17 上 ρ=0.082 的效应量本身（不论 p 值）已经非常小，结合 54% zero-F1 的先验信息，"capability boundary" 的实质结论是合理的。问题在于 statistical rhetoric——应改为 "consistent with a capability boundary" 或 "suggests that signals break down"。

---

**[AGREE] R1-W6: Qwen3-8B (LoRA) vs LLaMA-3.1-8B-Instruct 训练设置不对称**

同意。Section 5.1 (experiments.tex:14) 说 "Qwen3-8B (LoRA, r=32)" 但 LLaMA-3.1-8B-Instruct 未说明是否经过 LoRA/SFT fine-tuning。如果 LLaMA 使用的是 off-the-shelf instruction-tuned model 而 Qwen 经过了 task-specific LoRA fine-tuning，那么 cross-model comparison 混淆了 model architecture 和 training strategy 两个变量。

这个问题在 Table 1 的 cross-model 比较 (Δ=0.005) 和 Section 5.4 的 "model-agnostic" 结论中尤为突出。

---

**[AGREE] R1-W7: 约束解码对 sampling diversity 的影响**

同意，且认为 R1 低估了这个问题的重要性。

约束解码（constrained decoding via Outlines/vLLM, method.tex:5）强制输出符合预定义的 JSON/structured schema。这会显著减少 token-level 自由度，从而压缩 per-sample variance。如果 per-sample variance 被约束解码人为压低，那么 correlation-selection gap 可能部分是实验设计的 artifact 而非结构化 IE 的固有属性。

具体来说：
- Discussion (discussion.tex:12-13) 用 random baseline (0.608) 和 greedy (0.644) 的 gap (3.6 pp) 证明 "per-instance sample variance exists"。但这个 variance 是在约束解码下的 variance——无约束解码下可能更大。
- 如果无约束解码产生更多样的（但可能格式不正确的）输出，selection 的 headroom 可能更大，信号的 selection 能力可能更强。

论文应至少讨论这个 confound，即使无法提供无约束解码的对比实验。

---

### 小问题

**[AGREE] Table 2 EM "---"**：Caption 中有解释（"EM produces binary agreement without sample ranking"），但 Table 2 自身缺乏脚注或更显眼的标注。

**[AGREE] Logistic regression proxy**：Limitations (limitations.tex:8) 提到 "logistic regression proxy as an upper bound" 但正文和 Appendix 均未报告结果。要么展示结果，要么删除提及。

**[AGREE] snell2024scaling bib**：bib entry 显示 "Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral" (ICLR 2025)。需要与 OpenAlex 交叉验证是否缺少作者。

**[AGREE] Cross-model Δ=0.005 bootstrap CI**：experiments.tex:73 报告 SJ ρ=0.436 (Qwen) vs 0.431 (LLaMA) 但未报告差异是否在 CI 内。鉴于 N=16 的 3-seed std 约 0.007，Δ=0.005 几乎确定不显著，但应明确报告。

**[AGREE] Introduction "+18pp on GSM8K" 未注明模型**：wang2023selfconsistency 的 +18pp 来自 PaLM-540B，一个与本文 8B 模型规模相差甚远的模型。不注明可能误导读者认为 +18pp 在小模型上也成立。

**[AGREE] Appendix D \textsc**：appendix.tex:102 使用 `\textsc{Feature-Of}` 和 `\textsc{Hyponym-Of}`，需确认编译无误（特别是连字符在 small caps 下的渲染）。

---

### 对 R1 主要优势的回应

R1 列出的 5 点优势全部成立，我补充两点：

1. **Quality estimation vs sample selection 的概念解耦**确实是本文最有价值的贡献。这个 framing 对后续工作有直接指导意义——不论负面结论（weak selectors）是否最终成立。
2. **Conditional filtering analysis**（Appendix）是一个被忽视的亮点。它揭示了 EM 在 non-trivial subset 上的优势，并提供了 "task difficulty determines signal choice" 的额外证据维度。

---

### 对 R1 Overall Assessment 的回应

R1 给出 "Borderline → Weak Accept for Findings, Overall 3/5"。我基本同意这个判断区间。

我与 R1 的主要分歧在于问题严重程度的校准：
- **N1 (bootstrap)**：完全同意 critical。这是最需要修复的问题。
- **N2 (model-agnostic)**：同意需修正，但认为是 should-fix 级别（措辞修正即可），不构成 critical。
- **N3 (RE 基础薄弱)**：同意 concern，但论文已有 conditional analysis 作为缓解，建议降为 high-warning。
- **W7 (constrained decoding)**：R1 将此列为 warning，我认为应升级——这可能从根本上解释 correlation-selection gap，而非仅是一个遗漏的讨论点。

如果 N1 bootstrap 细节补全且确认方法学正确，加上 N2 措辞修正，本文适合 Findings track。

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

_source line 125 · 2026-05-15T02:05:06.000008+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-15T02:05:06.050767+00:00_



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

_source line 127 · 2026-05-15T02:06:47.392433+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues — status updated based on Round 1 findings\n  # ============================================================\n\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B），严重限制普适性主张\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性。建议增加 >30B 或 <3B 模型。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 列为 critical (N2)，R2 降为 should-fix（认为措辞修正即可）。Discussion 仍用 model-agnostic 但 Limitations 承认局限，构成内部矛盾。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失：Guo 2017, Snell 2024, Aggarwal 2023, CISC Huang 2025, 传统 IE confidence。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Round 0 遗漏可能部分修复（未再提及 Guo/Snell/Aggarwal/CISC）。但 Round 1 发现新遗漏：Singer 2026 conformal NER, ICLR 2025 conformal structured prediction, Optimal SC (2511.12309), Difficulty-Adaptive SC (NAACL 2025), Generative Self-Aggregation。R1 认为 conformal 类非 critical，R2 坚持。Optimal SC 和 Difficulty-Adaptive SC 两位共识应引用。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集，不足以称 universal bottleneck\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"SciERC RE 仅 6 relation types, n=397。需跨数据集验证或降级措辞。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 维持 critical (N3)，补充 44% zero-F1 floor effect 扭曲信号评估。R2 降为 high-warning，认为 conditional filtering (ρ=0.405) 和 capability stratification (Voting ρ=0.630) 部分缓解。分歧在严重程度。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限——评估指标到 confidence 的自然迁移\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少与 edit distance、embedding similarity 等 kernel 的消融。\"\n      - round: 1\n        reviewers: [2]\n        note: \"演变为 R2-N3: Nedellec et al. (2026) 增量贡献论证不足。SJ 优势不一致（CoNLL EM>SJ, conditional filtering 后 EM>SJ）。R1 同意增量论证弱但 negative selection result 有学术价值。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表（17 表 0 图）\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams、cost-effectiveness scatter。\"\n      - round: 1\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及，可能已修复，待 Research Director 确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C6\"\n    summary: \"成本分析将 8-16× 推理开销描述为 negligible\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"R1 定为 critical（系统性误导），R2 认为 TTS 语境下准确但需补充分析。\"\n      - round: 1\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及，可能已修复，待 Research Director 确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination（SJ+LP 互补性已证明但未尝试组合）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"Section 5.8 已证明互补性（Δρ=0.14）却未尝试组合。\"\n      - round: 1\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及，可能已修复，待 Research Director 确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统——3 seed std 不替代正式 bootstrap CI\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"p-value 极小已部分弥补但核心比较仍缺 CI。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"演变为更具体的 R1-N1: bootstrap 检验细节严重不足。p=0.39 支撑核心负面结论但迭代次数、paired/unpaired、统计量、3-seed含义均未报告。R2 完全同意并补充：5 处重复引用该 p 值。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling 声明 +0.018 on SciERC 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"experiments.tex L220 声称 +0.018，实际 Δ=-0.080。\"\n      - round: 1\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及，可能已修复（in_progress from Round 0），待确认。\"\n    action_items:\n      - round: 0\n        action: \"修正 experiments.tex 中 +0.018 声明\"\n        assigned_to: \"Main Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 1 new issues\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节严重不足，核心 'Weak Selectors' 结论的统计基础无法验证\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 完全同意并列为本文最关键方法论缺陷。p=0.39 在 5 处被引用支撑标题和 Contribution #2，但 bootstrap 迭代次数、paired/unpaired、统计量、'3-seed bootstrap' 含义均未报告。若 n=3 则完全无统计功效。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"Correlation-selection gap 解释力不足——4/5 signals 不能做 per-sample selection 是定义性结果\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 部分同意（consensus-proximity 策略非 trivial，但 logprob 失败分析不足完全成立）。论文未深入分析唯一 per-sample signal (logprob) 失败的原因（calibration? length bias? constrained decoding?）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 探索严重不足——仅 logprob 1 个 per-sample signal\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出 LOO-SJ selection 未测试。R1 反驳——consensus-proximity (Table 5 SJ 行) 数学上等价于 LOO-SJ 排序，是表述问题非实验缺失。但 R1 同意 'systematic comparison' 中 per-sample 维度极度单薄。两位共识：只有 1 个 per-sample signal 限制了 selection 结论的说服力。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"对 Nedellec et al. (2026) 增量贡献论证不足 + 引用作者错误\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 同意。bib 中第一作者为 Yao 但全文引用为 Nédellec et al.——事实性错误。SJ 优势不一致（CoNLL EM>SJ, conditional filtering 后 EM>SJ）削弱区分论证。R1 补充 negative selection result 有学术价值，但论证方式不够有力。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Soft Jaccard 形式化有歧义（g_i/g_j 未定义，sim 公式缺失，Hungarian 阈值未说明）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。不影响结论有效性但影响 reproducibility。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Entity voting mean frequency 聚合方式未讨论替代选择，幻觉实体膨胀 |E_∪|\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意并补充：entity voting 与 SJ 概念上有 overlap，两者 instance-level correlation 未报告——若高度相关则'两个 structural signal 优于 surface signal'论证被削弱。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 描述为 effective/strong 但仅解释 ~14% 方差，缺乏 contextualization\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出。R2 部分反驳——论文用 'effective' 和 'strongest'(比较级)而非 'strong'(绝对值)，AUROC=0.749 是面向应用的核心证据。但 R2 同意缺乏与 uncertainty estimation 文献其他方法的 ρ 对比。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度敏感性数据缺失（T=0.7 unavailable），'robust across temperatures' 结论过强\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意并升级——logprob 是唯一 per-sample signal，其温度敏感性直接影响核心负面结论。应限定为 'consistency-based signals are robust; logprob temperature sensitivity remains uncharacterized'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 'establishing capability boundary' 措辞过度——fail to reject null ≠ accept null\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。ρ=0.082 效应量小 + 54% zero-F1 支持实质结论，但统计措辞应改为 'consistent with' 或 'suggests'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。LLaMA 是否经过 fine-tuning 未说明。若 Qwen 为 task-specific LoRA 而 LLaMA 为 off-the-shelf，则 cross-model comparison 混淆了 architecture 和 training strategy。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W7\"\n    summary: \"约束解码对 sampling diversity 的影响未讨论——可能是 correlation-selection gap 的成因\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 列为 warning，R2 同意并认为应升级——约束解码压缩 token-level 自由度，人为压低 per-sample variance，gap 可能部分是实验 artifact 而非 IE 固有属性。Discussion 用 random baseline (0.608) vs greedy (0.644) 的 gap (3.6pp) 证明 variance 存在，但这是约束解码下的 variance。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W8\"\n    summary: \"'first systematic evaluation' claim 过强，需收窄 scope\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 同意。应加限定语如 'first to compare signals from multiple families for both quality estimation and sample selection in generative IE'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用：Optimal SC (2511.12309)、Difficulty-Adaptive SC (NAACL 2025)、conformal prediction for NER\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出 5 篇遗漏。R1 同意 Optimal SC 和 Difficulty-Adaptive SC 应引用（与论文核心主题高度相关）；对 conformal prediction 类反驳——属不同研究路线，非 critical omission。Generative Self-Aggregation 待确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 机制分析浅，EM=1 压缩效应需主文明确阐述\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 同意。Appendix D 有讨论但仅在 appendix，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M1\"\n    summary: \"Limitations 提及 logistic regression proxy as upper bound 但正文/Appendix 无结果\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。要么展示结果，要么删除提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M2\"\n    summary: \"Introduction '+18pp on GSM8K' 未注明具体模型 (PaLM-540B)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。与本文 8B 模型规模差异大，不注明可能误导。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告是否在 bootstrap CI 内\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。3-seed std 约 0.007，Δ=0.005 几乎确定不显著但应明确报告。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues — status updated based on Round 1 findings\n  # ============================================================\n\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B），严重限制普适性主张\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性。建议增加 >30B 或 <3B 模型。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 列为 critical (N2)，R2 降为 should-fix（认为措辞修正即可）。Discussion 仍用 model-agnostic 但 Limitations 承认局限，构成内部矛盾。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失：Guo 2017, Snell 2024, Aggarwal 2023, CISC Huang 2025, 传统 IE confidence。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Round 0 遗漏可能部分修复（未再提及 Guo/Snell/Aggarwal/CISC）。但 Round 1 发现新遗漏：Singer 2026 conformal NER, ICLR 2025 conformal structured prediction, Optimal SC (2511.12309), Difficulty-Adaptive SC (NAACL 2025), Generative Self-Aggregation。R1 认为 conformal 类非 critical，R2 坚持。Optimal SC 和 Difficulty-Adaptive SC 两位共识应引用。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集，不足以称 universal bottleneck\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"SciERC RE 仅 6 relation types, n=397。需跨数据集验证或降级措辞。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 维持 critical (N3)，补充 44% zero-F1 floor effect 扭曲信号评估。R2 降为 high-warning，认为 conditional filtering (ρ=0.405) 和 capability stratification (Voting ρ=0.630) 部分缓解。分歧在严重程度。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限——评估指标到 confidence 的自然迁移\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少与 edit distance、embedding similarity 等 kernel 的消融。\"\n      - round: 1\n        reviewers: [2]\n        note: \"演变为 R2-N3: Nedellec et al. (2026) 增量贡献论证不足。SJ 优势不一致（CoNLL EM>SJ, conditional filtering 后 EM>SJ）。R1 同意增量论证弱但 negative selection result 有学术价值。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表（17 表 0 图）\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams、cost-effectiveness scatter。\"\n      - round: 1\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及，可能已修复，待 Research Director 确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C6\"\n    summary: \"成本分析将 8-16× 推理开销描述为 negligible\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"R1 定为 critical（系统性误导），R2 认为 TTS 语境下准确但需补充分析。\"\n      - round: 1\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及，可能已修复，待 Research Director 确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination（SJ+LP 互补性已证明但未尝试组合）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"Section 5.8 已证明互补性（Δρ=0.14）却未尝试组合。\"\n      - round: 1\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及，可能已修复，待 Research Director 确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统——3 seed std 不替代正式 bootstrap CI\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"p-value 极小已部分弥补但核心比较仍缺 CI。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"演变为更具体的 R1-N1: bootstrap 检验细节严重不足。p=0.39 支撑核心负面结论但迭代次数、paired/unpaired、统计量、3-seed含义均未报告。R2 完全同意并补充：5 处重复引用该 p 值。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling 声明 +0.018 on SciERC 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"experiments.tex L220 声称 +0.018，实际 Δ=-0.080。\"\n      - round: 1\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及，可能已修复（in_progress from Round 0），待确认。\"\n    action_items:\n      - round: 0\n        action: \"修正 experiments.tex 中 +0.018 声明\"\n        assigned_to: \"Main Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 1 new issues\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节严重不足，核心 'Weak Selectors' 结论的统计基础无法验证\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 完全同意并列为本文最关键方法论缺陷。p=0.39 在 5 处被引用支撑标题和 Contribution #2，但 bootstrap 迭代次数、paired/unpaired、统计量、'3-seed bootstrap' 含义均未报告。若 n=3 则完全无统计功效。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"Correlation-selection gap 解释力不足——4/5 signals 不能做 per-sample selection 是定义性结果\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 部分同意（consensus-proximity 策略非 trivial，但 logprob 失败分析不足完全成立）。论文未深入分析唯一 per-sample signal (logprob) 失败的原因（calibration? length bias? constrained decoding?）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 探索严重不足——仅 logprob 1 个 per-sample signal\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出 LOO-SJ selection 未测试。R1 反驳——consensus-proximity (Table 5 SJ 行) 数学上等价于 LOO-SJ 排序，是表述问题非实验缺失。但 R1 同意 'systematic comparison' 中 per-sample 维度极度单薄。两位共识：只有 1 个 per-sample signal 限制了 selection 结论的说服力。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"对 Nedellec et al. (2026) 增量贡献论证不足 + 引用作者错误\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 同意。bib 中第一作者为 Yao 但全文引用为 Nédellec et al.——事实性错误。SJ 优势不一致（CoNLL EM>SJ, conditional filtering 后 EM>SJ）削弱区分论证。R1 补充 negative selection result 有学术价值，但论证方式不够有力。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Soft Jaccard 形式化有歧义（g_i/g_j 未定义，sim 公式缺失，Hungarian 阈值未说明）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。不影响结论有效性但影响 reproducibility。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Entity voting mean frequency 聚合方式未讨论替代选择，幻觉实体膨胀 |E_∪|\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意并补充：entity voting 与 SJ 概念上有 overlap，两者 instance-level correlation 未报告——若高度相关则'两个 structural signal 优于 surface signal'论证被削弱。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 描述为 effective/strong 但仅解释 ~14% 方差，缺乏 contextualization\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出。R2 部分反驳——论文用 'effective' 和 'strongest'(比较级)而非 'strong'(绝对值)，AUROC=0.749 是面向应用的核心证据。但 R2 同意缺乏与 uncertainty estimation 文献其他方法的 ρ 对比。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度敏感性数据缺失（T=0.7 unavailable），'robust across temperatures' 结论过强\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意并升级——logprob 是唯一 per-sample signal，其温度敏感性直接影响核心负面结论。应限定为 'consistency-based signals are robust; logprob temperature sensitivity remains uncharacterized'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 'establishing capability boundary' 措辞过度——fail to reject null ≠ accept null\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。ρ=0.082 效应量小 + 54% zero-F1 支持实质结论，但统计措辞应改为 'consistent with' 或 'suggests'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。LLaMA 是否经过 fine-tuning 未说明。若 Qwen 为 task-specific LoRA 而 LLaMA 为 off-the-shelf，则 cross-model comparison 混淆了 architecture 和 training strategy。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W7\"\n    summary: \"约束解码对 sampling diversity 的影响未讨论——可能是 correlation-selection gap 的成因\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 列为 warning，R2 同意并认为应升级——约束解码压缩 token-level 自由度，人为压低 per-sample variance，gap 可能部分是实验 artifact 而非 IE 固有属性。Discussion 用 random baseline (0.608) vs greedy (0.644) 的 gap (3.6pp) 证明 variance 存在，但这是约束解码下的 variance。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W8\"\n    summary: \"'first systematic evaluation' claim 过强，需收窄 scope\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 同意。应加限定语如 'first to compare signals from multiple families for both quality estimation and sample selection in generative IE'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用：Optimal SC (2511.12309)、Difficulty-Adaptive SC (NAACL 2025)、conformal prediction for NER\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出 5 篇遗漏。R1 同意 Optimal SC 和 Difficulty-Adaptive SC 应引用（与论文核心主题高度相关）；对 conformal prediction 类反驳——属不同研究路线，非 critical omission。Generative Self-Aggregation 待确认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 机制分析浅，EM=1 压缩效应需主文明确阐述\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 同意。Appendix D 有讨论但仅在 appendix，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M1\"\n    summary: \"Limitations 提及 logistic regression proxy as upper bound 但正文/Appendix 无结果\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。要么展示结果，要么删除提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M2\"\n    summary: \"Introduction '+18pp on GSM8K' 未注明具体模型 (PaLM-540B)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。与本文 8B 模型规模差异大，不注明可能误导。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告是否在 bootstrap CI 内\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。3-seed std 约 0.007，Δ=0.005 几乎确定不显著但应明确报告。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-15T02:06:47.493490+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 13263}, \"error\": \"\"}"}

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

_source line 129 · 2026-05-15T02:09:02.414520+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "report": "# 审稿报告：Round 1 圆桌审稿\n\n**论文**: \"Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 (ARR)\n**Reviewer 配置**: R1（方法严谨性 + 实验设计 + 统计有效性）+ R2（新颖性 + 完整性）\n**轮次**: Round 1（交叉分享后已收敛，无需第二轮）\n\n---\n\n## Summary\n\n本文系统比较 5 种 training-free confidence signals（Log-Probability、Entropy、Set Jaccard、Token Jaccard、Exact-Match）在 LLM-based 结构化信息抽取（NER/RE）中的 quality estimation 和 best-of-N sample selection 能力。核心概念贡献是将 quality estimation（ranking correlation）与 sample selection（F1 gain over greedy）解耦，发现二者存在 \"correlation-selection gap\"——即使信号与 F1 有中等正相关（SJ ρ≈0.42），实际 selection 也未能稳定超越 greedy baseline (p=0.39)。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个 8B 模型，多 seed/多温度/OOD 等消融维度。\n\n---\n\n## Strengths\n\n**S1. Quality estimation vs sample selection 的概念解耦** [R1+R2 共识]\n将 ranking correlation 与 selection F1 gain 分离是有价值的概念贡献，对后续 test-time scaling 研究有直接指导意义——不论负面结论是否最终成立。\n\n**S2. 实验设计的系统性** [R1+R2 共识]\n5 signals × 3 signal families × 3 NER datasets × 1 RE dataset × 2 models × 2 N × 2 T + task difficulty gradient (CoNLL/SciERC/WNUT) + 多项辅助分析（LOO circularity、conditional filtering、capability stratification、inverted-U pattern）。\n\n**S3. Task difficulty gradient 设计** [R1 提出，R2 认可]\nCoNLL（easy）→ SciERC（medium）→ WNUT（hard）的难度梯度设计合理，信号排序随难度变化的发现有实用价值。\n\n**S4. Conditional filtering analysis** [R2 提出，R1 认可]\nAppendix 中移除 zero-F1 instance 后 RE 信号恢复（SJ ρ=0.405, EM ρ=0.417），揭示了 EM 在 non-trivial subset 上的优势，提供了 \"task difficulty determines signal choice\" 的额外证据。\n\n**S5. Limitations section 全面诚实** [R1 提出]\n主动承认模型规模、RE 数据集、logprob 温度数据等限制。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**C1. Bootstrap 检验细节严重不足，核心负面结论无法验证** [R1 提出 critical, R2 完全同意 critical]\n\n论文核心负面结论（\"no signal reliably surpasses greedy\"）建立在 Section 5.3 的 \"p=0.39, 3-seed bootstrap; Cohen's d=0.038\" 上，但以下关键细节均未报告：\n- Bootstrap 迭代次数\n- Paired 还是 unpaired bootstrap\n- 检验统计量\n- \"3-seed bootstrap\" 含义不明——对 3 个 seed 做 bootstrap (n=3, 完全无统计功效) 还是每个 seed 内对 instance 做 bootstrap 再合并？\n\n该 p 值在论文 5 处被重复引用（Abstract、Introduction ×2、Section 5.3、Conclusion），支撑标题 (\"Weak Selectors\")、Contribution #2（correlation-selection gap）及 Discussion 对 trained verifier 的呼吁。若检验无效，核心贡献坍塌为 \"没有足够统计功效来判断 selection 是否有效\"——完全不同的结论。\n\n**C2. Correlation-selection gap 的理论贡献被定义性质部分削弱，logprob 失败分析缺失** [R2 提出, R1 部分同意]\n\n4/5 个 signals（Entropy, SJ, TJ, Voting）是 instance-level 的——它们不能做 per-sample selection 在定义上是预期结果（Section 3.1 Eq. 5–8 只产出单一 score），而非实证发现。R1 补充：Section 3.3 通过 consensus-proximity 将 instance-level signals 转化为 per-sample 排序，这不完全是 trivial 的，但效果确实差（Table 5: SJ=0.645 vs Greedy=0.644）。\n\n真正需要深入分析的是唯一 per-sample signal logprob 为何也失败——calibration 问题？length bias？constrained decoding 干扰？论文仅在 Section 5.1 提到 conditional filtering 后 \"logprob RE collapses to ρ=0.011\"，Discussion 简要提及 constrained decoding 可能影响，但无实验验证。\n\n**C3. 对 Nedellec et al. (2026) 增量贡献论证不足 + 引用作者错误** [R2 提出 critical, R1 同意]\n\nbib 文件中 `nedellec2026consistency` 第一作者为 Yao，但全文引用为 \"Nédellec et al.\"——事实性错误。三个区分点的说服力不足：\n- Selection 结论是负面的（未能超越 greedy）\n- Multi-domain 是标准做法\n- SJ 优势不一致（CoNLL: EM ρ=0.451 > SJ ρ=0.436; conditional filtering 后 EM 在所有 4 个配置领先）\n\nR1 补充：negative selection result 本身有学术价值（Nedellec 未涉及 selection），问题在于论证方式不够有力，而非贡献不存在。\n\n**C4. 仅 8B 模型 \"model-agnostic\" overclaim** [R1 critical, R2 降为 should-fix — 存在分歧]\n\n仅 Qwen3-8B 和 LLaMA-3.1-8B-Instruct 两个同规模模型。Discussion 使用 \"model-agnostic\" 但 Limitations 承认 \"Whether our findings hold for larger models (70B+) remains untested\"——构成内部矛盾 (ARR R4 overclaiming)。\n\n**R2 立场**：修复成本低——将 \"model-agnostic\" 替换为 \"consistent across tested model families\" 即可，核心发现（structural > logprob 在两个模型上一致）本身有效。应为 should-fix。\n**R1 立场**：70B+ 模型可能产生更高质量更多样的样本，从根本上改变 gap 形态。应为 critical。\n**Director 定级**：Critical（保守取高），但记录 R2 的缓和意见。\n\n**C5. RE 结论仅基于 SciERC, 44% zero-F1 floor effect 扭曲评估** [R1 critical, R2 降为 high-warning — 存在分歧]\n\nRE 所有结论来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。\n\n**R2 缓和因素**：(1) Conditional filtering 后 SJ RE ρ=0.405, EM RE ρ=0.417——non-trivial subset 上信号有区分力；(2) Capability stratification 中高复杂度 RE 子集 Voting ρ=0.630。\n**R1 立场**：论文声称覆盖 \"NER and RE\" 但 RE 基础极其薄弱，\"universal bottleneck\" 需降级。\n**Director 定级**：Critical for \"NER and RE\" / \"universal bottleneck\" 措辞；Warning if 仅要求限定 RE 结论的泛化范围。\n\n---\n\n### Should-Fix\n\n**W1. Per-sample signal 探索单薄** [R2 提出, R1 部分同意]\n5 个 signals 中仅 logprob 1 个能做 per-sample selection，论文却声称 \"systematic comparison\"。R1 反驳：consensus-proximity (Table 5 SJ 行) 数学上等价于 LOO-SJ 排序——是表述问题非实验缺失。但两位共识：per-sample 维度极度单薄。\n\n**W2. 约束解码对 sampling diversity 的影响** [R1 warning, R2 认为应升级]\nConstrained decoding (Outlines/vLLM) 强制输出符合预定义 schema，压缩 token-level 自由度和 per-sample variance。Correlation-selection gap 可能部分是实验 artifact 而非结构化 IE 固有属性。Discussion 用 random baseline (0.608) vs greedy (0.644) 的 gap (3.6pp) 论证 \"variance exists\"，但这是约束解码下的 variance。\n\n**W3. Soft Jaccard 形式化有歧义** [R1 提出, R2 同意]\nEq. (4) 中 g_i/g_j 未定义，sim 具体公式缺失（token-level IoU? character-level?），Hungarian algorithm 匹配阈值未说明。影响 reproducibility。\n\n**W4. Entity voting 与 SJ 的冗余度未分析** [R1 提出, R2 同意并补充]\nMean frequency 聚合未讨论替代选择。R2 补充：entity voting 和 SJ 概念上 overlap，instance-level correlation 未报告——若高度相关则 \"两个 structural signal 优于 surface signal\" 论证被削弱。\n\n**W5. Logprob 温度数据缺失** [R1+R2 共识]\nLogprob 是唯一 per-sample signal，T=0.7 数据 \"unavailable\"，但论文声称 \"signals robust across temperatures\"。应限定为 \"consistency-based signals are robust; logprob temperature sensitivity remains uncharacterized\"。\n\n**W6. ρ=0.38 缺乏 contextualization** [R1 提出, R2 部分反驳]\nR1 认为仅解释 ~14% F1 方差，未与 uncertainty estimation 文献对比。R2 反驳：论文用 \"effective\" 和 \"strongest\"（比较级）而非 \"strong\"（绝对值），AUROC=0.749 是面向应用的核心证据。但 R2 同意缺乏与 semantic entropy、P(True) 等方法的 ρ 对比。\n\n**W7. WNUT-17 \"establishing capability boundary\" 措辞** [R1+R2 共识]\np=0.106, fail to reject null ≠ accept null。ρ=0.082 效应量小 + 54% zero-F1 支持实质结论，但统计措辞应改为 \"consistent with\" 或 \"suggests\"。\n\n**W8. 模型训练设置不对称** [R1 提出, R2 同意]\nQwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct——后者是否经过 fine-tuning 未说明。若为 off-the-shelf vs task-specific LoRA，则 cross-model comparison 混淆了 architecture 和 training strategy。\n\n**W9. \"first systematic evaluation\" claim 过强** [R2 提出, R1 同意]\n需收窄为 \"first to compare signals from multiple families for both quality estimation and sample selection in generative IE\"。\n\n**W10. 遗漏引用** [R2 提出, R1 部分同意]\n- **共识应引用**：Optimal Self-Consistency (arXiv:2511.12309)、Difficulty-Adaptive SC (NAACL 2025 Findings)——与论文核心主题 (task difficulty determines signal choice) 高度相关\n- **R2 认为应引用, R1 反驳为非 critical**：Singer et al. (2026) conformal NER, ICLR 2025 conformal structured prediction——属不同研究路线 (supervised conformal vs unsupervised consistency)\n- **待确认**：Generative Self-Aggregation (arXiv:2503.04104)\n\n**W11. ρ-AUROC dissociation 机制分析浅** [R2 提出, R1 同意]\nEM=1 同时包含 all-correct 和 all-wrong 的压缩效应仅在 Appendix D 讨论，应在主文明确阐述。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致：\n1. **Overall 评分**: 3/5 (Findings)\n2. **Bootstrap 细节不足 (C1)**: 本文最关键的方法论缺陷，影响核心贡献成立性\n3. **Logprob 失败分析缺失**: 唯一 per-sample signal 值得专门深入分析\n4. **Nedellec 引用错误**: Yao → Nédellec 是事实性错误\n5. **约束解码 confound**: 应至少讨论其对 diversity 和 gap 的潜在影响\n6. **\"model-agnostic\" 措辞矛盾**: 需与 Limitations 一致\n7. **WNUT-17 措辞**: \"establishing\" → \"consistent with\" / \"suggests\"\n8. **\"first systematic\" 需限定**\n9. **Quality estimation vs selection 解耦**: 本文最有价值的概念贡献\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 定级 |\n|------|---------|---------|---------------|\n| C4 模型规模 overclaim | Critical（70B 可能根本改变 gap） | Should-fix（措辞修正即可） | Critical（保守取高） |\n| C5 RE 单数据集 | Critical（RE 基础极其薄弱） | High-warning（conditional analysis 部分缓解） | Critical for \"universal\" 措辞 |\n| W1 LOO-SJ selection | 已隐式测试（Table 5 SJ 行 = consensus-proximity） | 未测试，应显式报告 | Warning（是表述问题，但 per-sample 维度确实单薄） |\n| W6 ρ contextualization | 缺乏对比 | 论文措辞准确（比较级），AUROC 是核心证据 | Warning（补充对比即可） |\n| W2 约束解码严重程度 | Warning | 应升级（可能解释 gap 的根本原因） | Warning（论据充分但无约束解码对比数据） |\n| W10 Conformal prediction 引用 | 非 critical omission（不同路线） | 应引用 | Warning（在 Related Work 中讨论） |\n\n---\n\n## Questions（需作者澄清）\n\n1. **Bootstrap 检验完整规范**：迭代次数、paired/unpaired、统计量、\"3-seed bootstrap\" 确切含义？若 n=3，则需在每个 seed 内对 instance 做 paired bootstrap 并报告合并策略。\n2. **LLaMA-3.1-8B-Instruct 是否经过 LoRA/SFT fine-tuning**？若未 fine-tune，cross-model comparison 混淆了 architecture 和 training strategy。\n3. **Consensus-proximity selection 与 LOO-SJ 的等价关系**：Table 5 SJ 行是否等价于 LOO-SJ selection？若是，应在正文中显式说明。\n4. **Logprob 在 constrained decoding 下的行为**：constrained decoding 是否系统性扭曲了 logprob 的 calibration？是否有 unconstrained 对比数据？\n5. **Entity voting 与 SJ 的 instance-level correlation**：Spearman ρ 是多少？高冗余度是否削弱 \"两类 structural signal 独立验证\" 的论证？\n6. **Logistic regression proxy**：Limitations 提到但正文/Appendix 无结果——是否计划展示？\n\n---\n\n## Missing References\n\n### 共识应引用\n1. **Optimal Self-Consistency** (arXiv:2511.12309) — 与 selection 机制直接相关\n2. **Difficulty-Adaptive Self-Consistency** (NAACL 2025 Findings) — 与论文核心发现 \"task difficulty determines signal choice\" 高度相关\n\n### 建议引用（存在分歧）\n3. Singer et al. (2026) \"UQ for NER via Conformal Prediction\" (arXiv:2601.16999)\n4. Conformal Structured Prediction (ICLR 2025)\n5. Generative Self-Aggregation (arXiv:2503.04104)\n\n### 引用错误\n- `nedellec2026consistency`: 第一作者应为 Yao，全文 \"Nédellec et al.\" 引用有误\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分**: 3/5 (Findings) — 两位 Reviewer 完全一致\n**Director Scale**: 3.5/6 (Borderline — Weak Accept for Findings)\n**置信度**: 4/5\n\n### 定位判断\n\nFindings 可接受（需修复 C1 bootstrap 细节），Main 不足。\n\n论文的概念贡献（quality estimation vs selection 解耦）和系统实验设计有 Findings 水准的价值，但 5 个 critical 问题共同限制了竞争力：\n\n1. **C1 Bootstrap 细节** — 核心负面结论的统计基础无法验证（最优先修复）\n2. **C2 Gap 解释力** — 4/5 signals 的 selection 失败有定义性成分，logprob 失败机制未分析\n3. **C3 Nedellec 增量** — 贡献论证弱 + 引用错误\n4. **C4 Model-agnostic** — Overclaim，但修复成本低（措辞修正）\n5. **C5 RE 单数据集** — \"Universal bottleneck\" 仅单数据集支撑\n\n### 与 Round 0 的对比\n\nRound 0 的部分 critical 问题可能已修复（零图表、成本分析均未被本轮 Reviewer 提及），但新的 critical 问题浮现（bootstrap 细节、gap 定义性、Nedellec 增量）。模型规模和 RE 数据集问题持续存在。整体评分与 Round 0 持平（3/5），论文在不同维度有进步和退步。\n\n### 修改建议优先级\n\n- **P0（决定性）**: 补充 bootstrap 检验完整规范 + 修正 Nedellec 引用错误 + 降级 \"model-agnostic\"/\"universal\"/\"establish\" 措辞\n- **P1（强烈建议）**: 深入分析 logprob selection 失败原因 + 讨论约束解码 confound + 补充 Optimal SC / Difficulty-Adaptive SC 引用 + 显式说明 consensus-proximity = LOO-SJ selection\n- **P2（改善质量）**: SJ 形式化补全 + entity voting/SJ 冗余度分析 + ρ contextualization + 温度 robustness 限定 + LLaMA fine-tuning 状态说明\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"Weak Selectors\" 结论建立在 p=0.39 上——若 bootstrap 细节补全后确认有效则可保留，否则需重新表述\n\n### Section 1 (Introduction)\n- \"+18pp on GSM8K\" 未注明具体模型 (PaLM-540B)，与本文 8B 规模差异大\n- \"first systematic evaluation\" 需加限定语\n\n### Section 3 (Method)\n- Eq. (4) SJ: g_i/g_j 定义、sim 公式、Hungarian 阈值需补全\n- Section 3.3 consensus-proximity selection 应显式说明与 LOO-SJ 排序的等价关系\n- Entity voting mean frequency 聚合未讨论替代选择\n\n### Section 5 (Results)\n- Section 5.3: bootstrap 检验规范必须完整报告\n- Section 5.4: \"model-agnostic\" → \"consistent across tested model families\"\n- Section 5.4: Cross-model Δ=0.005 应报告是否在 CI 内\n- WNUT-17: \"establishing the capability boundary\" → \"consistent with a capability boundary\"\n- Logprob T=0.7 缺失应在温度 robustness 结论中明确限定\n\n### Section 6 (Discussion)\n- 补充约束解码对 sampling diversity 和 correlation-selection gap 的讨论\n- \"Universal bottleneck\" 需降级或增加 RE 数据集\n- Logistic regression proxy: 展示结果或删除提及\n\n### Related Work\n- 补充 Optimal SC、Difficulty-Adaptive SC\n- 讨论 conformal prediction for structured prediction（可简要说明与本文研究路线的关系）\n- 更充分讨论 trained approaches (verifier/reward model) 作为 upper bound context\n\n### References\n- 修正 nedellec2026consistency 第一作者 (Yao → 正确引用)\n- 检查 snell2024scaling bib 作者格式\n\n### Appendix\n- ρ-AUROC dissociation / EM=1 压缩效应应在主文至少简要提及\n- Appendix D \\textsc 编译检查"
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
    "overall_score": "borderline",
    "report": "# 审稿报告：Round 1 圆桌审稿\n\n**论文**: \"Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 (ARR)\n**Reviewer 配置**: R1（方法严谨性 + 实验设计 + 统计有效性）+ R2（新颖性 + 完整性）\n**轮次**: Round 1（交叉分享后已收敛，无需第二轮）\n\n---\n\n## Summary\n\n本文系统比较 5 种 training-free confidence signals（Log-Probability、Entropy、Set Jaccard、Token Jaccard、Exact-Match）在 LLM-based 结构化信息抽取（NER/RE）中的 quality estimation 和 best-of-N sample selection 能力。核心概念贡献是将 quality estimation（ranking correlation）与 sample selection（F1 gain over greedy）解耦，发现二者存在 \"correlation-selection gap\"——即使信号与 F1 有中等正相关（SJ ρ≈0.42），实际 selection 也未能稳定超越 greedy baseline (p=0.39)。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个 8B 模型，多 seed/多温度/OOD 等消融维度。\n\n---\n\n## Strengths\n\n**S1. Quality estimation vs sample selection 的概念解耦** [R1+R2 共识]\n将 ranking correlation 与 selection F1 gain 分离是有价值的概念贡献，对后续 test-time scaling 研究有直接指导意义——不论负面结论是否最终成立。\n\n**S2. 实验设计的系统性** [R1+R2 共识]\n5 signals × 3 signal families × 3 NER datasets × 1 RE dataset × 2 models × 2 N × 2 T + task difficulty gradient (CoNLL/SciERC/WNUT) + 多项辅助分析（LOO circularity、conditional filtering、capability stratification、inverted-U pattern）。\n\n**S3. Task difficulty gradient 设计** [R1 提出，R2 认可]\nCoNLL（easy）→ SciERC（medium）→ WNUT（hard）的难度梯度设计合理，信号排序随难度变化的发现有实用价值。\n\n**S4. Conditional filtering analysis** [R2 提出，R1 认可]\nAppendix 中移除 zero-F1 instance 后 RE 信号恢复（SJ ρ=0.405, EM ρ=0.417），揭示了 EM 在 non-trivial subset 上的优势，提供了 \"task difficulty determines signal choice\" 的额外证据。\n\n**S5. Limitations section 全面诚实** [R1 提出]\n主动承认模型规模、RE 数据集、logprob 温度数据等限制。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**C1. Bootstrap 检验细节严重不足，核心负面结论无法验证** [R1 提出 critical, R2 完全同意 critical]\n\n论文核心负面结论（\"no signal reliably surpasses greedy\"）建立在 Section 5.3 的 \"p=0.39, 3-seed bootstrap; Cohen's d=0.038\" 上，但以下关键细节均未报告：\n- Bootstrap 迭代次数\n- Paired 还是 unpaired bootstrap\n- 检验统计量\n- \"3-seed bootstrap\" 含义不明——对 3 个 seed 做 bootstrap (n=3, 完全无统计功效) 还是每个 seed 内对 instance 做 bootstrap 再合并？\n\n该 p 值在论文 5 处被重复引用（Abstract、Introduction ×2、Section 5.3、Conclusion），支撑标题 (\"Weak Selectors\")、Contribution #2（correlation-selection gap）及 Discussion 对 trained verifier 的呼吁。若检验无效，核心贡献坍塌为 \"没有足够统计功效来判断 selection 是否有效\"——完全不同的结论。\n\n**C2. Correlation-selection gap 的理论贡献被定义性质部分削弱，logprob 失败分析缺失** [R2 提出, R1 部分同意]\n\n4/5 个 signals（Entropy, SJ, TJ, Voting）是 instance-level 的——它们不能做 per-sample selection 在定义上是预期结果（Section 3.1 Eq. 5–8 只产出单一 score），而非实证发现。R1 补充：Section 3.3 通过 consensus-proximity 将 instance-level signals 转化为 per-sample 排序，这不完全是 trivial 的，但效果确实差（Table 5: SJ=0.645 vs Greedy=0.644）。\n\n真正需要深入分析的是唯一 per-sample signal logprob 为何也失败——calibration 问题？length bias？constrained decoding 干扰？论文仅在 Section 5.1 提到 conditional filtering 后 \"logprob RE collapses to ρ=0.011\"，Discussion 简要提及 constrained decoding 可能影响，但无实验验证。\n\n**C3. 对 Nedellec et al. (2026) 增量贡献论证不足 + 引用作者错误** [R2 提出 critical, R1 同意]\n\nbib 文件中 `nedellec2026consistency` 第一作者为 Yao，但全文引用为 \"Nédellec et al.\"——事实性错误。三个区分点的说服力不足：\n- Selection 结论是负面的（未能超越 greedy）\n- Multi-domain 是标准做法\n- SJ 优势不一致（CoNLL: EM ρ=0.451 > SJ ρ=0.436; conditional filtering 后 EM 在所有 4 个配置领先）\n\nR1 补充：negative selection result 本身有学术价值（Nedellec 未涉及 selection），问题在于论证方式不够有力，而非贡献不存在。\n\n**C4. 仅 8B 模型 \"model-agnostic\" overclaim** [R1 critical, R2 降为 should-fix — 存在分歧]\n\n仅 Qwen3-8B 和 LLaMA-3.1-8B-Instruct 两个同规模模型。Discussion 使用 \"model-agnostic\" 但 Limitations 承认 \"Whether our findings hold for larger models (70B+) remains untested\"——构成内部矛盾 (ARR R4 overclaiming)。\n\n**R2 立场**：修复成本低——将 \"model-agnostic\" 替换为 \"consistent across tested model families\" 即可，核心发现（structural > logprob 在两个模型上一致）本身有效。应为 should-fix。\n**R1 立场**：70B+ 模型可能产生更高质量更多样的样本，从根本上改变 gap 形态。应为 critical。\n**Director 定级**：Critical（保守取高），但记录 R2 的缓和意见。\n\n**C5. RE 结论仅基于 SciERC, 44% zero-F1 floor effect 扭曲评估** [R1 critical, R2 降为 high-warning — 存在分歧]\n\nRE 所有结论来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。\n\n**R2 缓和因素**：(1) Conditional filtering 后 SJ RE ρ=0.405, EM RE ρ=0.417——non-trivial subset 上信号有区分力；(2) Capability stratification 中高复杂度 RE 子集 Voting ρ=0.630。\n**R1 立场**：论文声称覆盖 \"NER and RE\" 但 RE 基础极其薄弱，\"universal bottleneck\" 需降级。\n**Director 定级**：Critical for \"NER and RE\" / \"universal bottleneck\" 措辞；Warning if 仅要求限定 RE 结论的泛化范围。\n\n---\n\n### Should-Fix\n\n**W1. Per-sample signal 探索单薄** [R2 提出, R1 部分同意]\n5 个 signals 中仅 logprob 1 个能做 per-sample selection，论文却声称 \"systematic comparison\"。R1 反驳：consensus-proximity (Table 5 SJ 行) 数学上等价于 LOO-SJ 排序——是表述问题非实验缺失。但两位共识：per-sample 维度极度单薄。\n\n**W2. 约束解码对 sampling diversity 的影响** [R1 warning, R2 认为应升级]\nConstrained decoding (Outlines/vLLM) 强制输出符合预定义 schema，压缩 token-level 自由度和 per-sample variance。Correlation-selection gap 可能部分是实验 artifact 而非结构化 IE 固有属性。Discussion 用 random baseline (0.608) vs greedy (0.644) 的 gap (3.6pp) 论证 \"variance exists\"，但这是约束解码下的 variance。\n\n**W3. Soft Jaccard 形式化有歧义** [R1 提出, R2 同意]\nEq. (4) 中 g_i/g_j 未定义，sim 具体公式缺失（token-level IoU? character-level?），Hungarian algorithm 匹配阈值未说明。影响 reproducibility。\n\n**W4. Entity voting 与 SJ 的冗余度未分析** [R1 提出, R2 同意并补充]\nMean frequency 聚合未讨论替代选择。R2 补充：entity voting 和 SJ 概念上 overlap，instance-level correlation 未报告——若高度相关则 \"两个 structural signal 优于 surface signal\" 论证被削弱。\n\n**W5. Logprob 温度数据缺失** [R1+R2 共识]\nLogprob 是唯一 per-sample signal，T=0.7 数据 \"unavailable\"，但论文声称 \"signals robust across temperatures\"。应限定为 \"consistency-based signals are robust; logprob temperature sensitivity remains uncharacterized\"。\n\n**W6. ρ=0.38 缺乏 contextualization** [R1 提出, R2 部分反驳]\nR1 认为仅解释 ~14% F1 方差，未与 uncertainty estimation 文献对比。R2 反驳：论文用 \"effective\" 和 \"strongest\"（比较级）而非 \"strong\"（绝对值），AUROC=0.749 是面向应用的核心证据。但 R2 同意缺乏与 semantic entropy、P(True) 等方法的 ρ 对比。\n\n**W7. WNUT-17 \"establishing capability boundary\" 措辞** [R1+R2 共识]\np=0.106, fail to reject null ≠ accept null。ρ=0.082 效应量小 + 54% zero-F1 支持实质结论，但统计措辞应改为 \"consistent with\" 或 \"suggests\"。\n\n**W8. 模型训练设置不对称** [R1 提出, R2 同意]\nQwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct——后者是否经过 fine-tuning 未说明。若为 off-the-shelf vs task-specific LoRA，则 cross-model comparison 混淆了 architecture 和 training strategy。\n\n**W9. \"first systematic evaluation\" claim 过强** [R2 提出, R1 同意]\n需收窄为 \"first to compare signals from multiple families for both quality estimation and sample selection in generative IE\"。\n\n**W10. 遗漏引用** [R2 提出, R1 部分同意]\n- **共识应引用**：Optimal Self-Consistency (arXiv:2511.12309)、Difficulty-Adaptive SC (NAACL 2025 Findings)——与论文核心主题 (task difficulty determines signal choice) 高度相关\n- **R2 认为应引用, R1 反驳为非 critical**：Singer et al. (2026) conformal NER, ICLR 2025 conformal structured prediction——属不同研究路线 (supervised conformal vs unsupervised consistency)\n- **待确认**：Generative Self-Aggregation (arXiv:2503.04104)\n\n**W11. ρ-AUROC dissociation 机制分析浅** [R2 提出, R1 同意]\nEM=1 同时包含 all-correct 和 all-wrong 的压缩效应仅在 Appendix D 讨论，应在主文明确阐述。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致：\n1. **Overall 评分**: 3/5 (Findings)\n2. **Bootstrap 细节不足 (C1)**: 本文最关键的方法论缺陷，影响核心贡献成立性\n3. **Logprob 失败分析缺失**: 唯一 per-sample signal 值得专门深入分析\n4. **Nedellec 引用错误**: Yao → Nédellec 是事实性错误\n5. **约束解码 confound**: 应至少讨论其对 diversity 和 gap 的潜在影响\n6. **\"model-agnostic\" 措辞矛盾**: 需与 Limitations 一致\n7. **WNUT-17 措辞**: \"establishing\" → \"consistent with\" / \"suggests\"\n8. **\"first systematic\" 需限定**\n9. **Quality estimation vs selection 解耦**: 本文最有价值的概念贡献\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 定级 |\n|------|---------|---------|---------------|\n| C4 模型规模 overclaim | Critical（70B 可能根本改变 gap） | Should-fix（措辞修正即可） | Critical（保守取高） |\n| C5 RE 单数据集 | Critical（RE 基础极其薄弱） | High-warning（conditional analysis 部分缓解） | Critical for \"universal\" 措辞 |\n| W1 LOO-SJ selection | 已隐式测试（Table 5 SJ 行 = consensus-proximity） | 未测试，应显式报告 | Warning（是表述问题，但 per-sample 维度确实单薄） |\n| W6 ρ contextualization | 缺乏对比 | 论文措辞准确（比较级），AUROC 是核心证据 | Warning（补充对比即可） |\n| W2 约束解码严重程度 | Warning | 应升级（可能解释 gap 的根本原因） | Warning（论据充分但无约束解码对比数据） |\n| W10 Conformal prediction 引用 | 非 critical omission（不同路线） | 应引用 | Warning（在 Related Work 中讨论） |\n\n---\n\n## Questions（需作者澄清）\n\n1. **Bootstrap 检验完整规范**：迭代次数、paired/unpaired、统计量、\"3-seed bootstrap\" 确切含义？若 n=3，则需在每个 seed 内对 instance 做 paired bootstrap 并报告合并策略。\n2. **LLaMA-3.1-8B-Instruct 是否经过 LoRA/SFT fine-tuning**？若未 fine-tune，cross-model comparison 混淆了 architecture 和 training strategy。\n3. **Consensus-proximity selection 与 LOO-SJ 的等价关系**：Table 5 SJ 行是否等价于 LOO-SJ selection？若是，应在正文中显式说明。\n4. **Logprob 在 constrained decoding 下的行为**：constrained decoding 是否系统性扭曲了 logprob 的 calibration？是否有 unconstrained 对比数据？\n5. **Entity voting 与 SJ 的 instance-level correlation**：Spearman ρ 是多少？高冗余度是否削弱 \"两类 structural signal 独立验证\" 的论证？\n6. **Logistic regression proxy**：Limitations 提到但正文/Appendix 无结果——是否计划展示？\n\n---\n\n## Missing References\n\n### 共识应引用\n1. **Optimal Self-Consistency** (arXiv:2511.12309) — 与 selection 机制直接相关\n2. **Difficulty-Adaptive Self-Consistency** (NAACL 2025 Findings) — 与论文核心发现 \"task difficulty determines signal choice\" 高度相关\n\n### 建议引用（存在分歧）\n3. Singer et al. (2026) \"UQ for NER via Conformal Prediction\" (arXiv:2601.16999)\n4. Conformal Structured Prediction (ICLR 2025)\n5. Generative Self-Aggregation (arXiv:2503.04104)\n\n### 引用错误\n- `nedellec2026consistency`: 第一作者应为 Yao，全文 \"Nédellec et al.\" 引用有误\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分**: 3/5 (Findings) — 两位 Reviewer 完全一致\n**Director Scale**: 3.5/6 (Borderline — Weak Accept for Findings)\n**置信度**: 4/5\n\n### 定位判断\n\nFindings 可接受（需修复 C1 bootstrap 细节），Main 不足。\n\n论文的概念贡献（quality estimation vs selection 解耦）和系统实验设计有 Findings 水准的价值，但 5 个 critical 问题共同限制了竞争力：\n\n1. **C1 Bootstrap 细节** — 核心负面结论的统计基础无法验证（最优先修复）\n2. **C2 Gap 解释力** — 4/5 signals 的 selection 失败有定义性成分，logprob 失败机制未分析\n3. **C3 Nedellec 增量** — 贡献论证弱 + 引用错误\n4. **C4 Model-agnostic** — Overclaim，但修复成本低（措辞修正）\n5. **C5 RE 单数据集** — \"Universal bottleneck\" 仅单数据集支撑\n\n### 与 Round 0 的对比\n\nRound 0 的部分 critical 问题可能已修复（零图表、成本分析均未被本轮 Reviewer 提及），但新的 critical 问题浮现（bootstrap 细节、gap 定义性、Nedellec 增量）。模型规模和 RE 数据集问题持续存在。整体评分与 Round 0 持平（3/5），论文在不同维度有进步和退步。\n\n### 修改建议优先级\n\n- **P0（决定性）**: 补充 bootstrap 检验完整规范 + 修正 Nedellec 引用错误 + 降级 \"model-agnostic\"/\"universal\"/\"establish\" 措辞\n- **P1（强烈建议）**: 深入分析 logprob selection 失败原因 + 讨论约束解码 confound + 补充 Optimal SC / Difficulty-Adaptive SC 引用 + 显式说明 consensus-proximity = LOO-SJ selection\n- **P2（改善质量）**: SJ 形式化补全 + entity voting/SJ 冗余度分析 + ρ contextualization + 温度 robustness 限定 + LLaMA fine-tuning 状态说明\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"Weak Selectors\" 结论建立在 p=0.39 上——若 bootstrap 细节补全后确认有效则可保留，否则需重新表述\n\n### Section 1 (Introduction)\n- \"+18pp on GSM8K\" 未注明具体模型 (PaLM-540B)，与本文 8B 规模差异大\n- \"first systematic evaluation\" 需加限定语\n\n### Section 3 (Method)\n- Eq. (4) SJ: g_i/g_j 定义、sim 公式、Hungarian 阈值需补全\n- Section 3.3 consensus-proximity selection 应显式说明与 LOO-SJ 排序的等价关系\n- Entity voting mean frequency 聚合未讨论替代选择\n\n### Section 5 (Results)\n- Section 5.3: bootstrap 检验规范必须完整报告\n- Section 5.4: \"model-agnostic\" → \"consistent across tested model families\"\n- Section 5.4: Cross-model Δ=0.005 应报告是否在 CI 内\n- WNUT-17: \"establishing the capability boundary\" → \"consistent with a capability boundary\"\n- Logprob T=0.7 缺失应在温度 robustness 结论中明确限定\n\n### Section 6 (Discussion)\n- 补充约束解码对 sampling diversity 和 correlation-selection gap 的讨论\n- \"Universal bottleneck\" 需降级或增加 RE 数据集\n- Logistic regression proxy: 展示结果或删除提及\n\n### Related Work\n- 补充 Optimal SC、Difficulty-Adaptive SC\n- 讨论 conformal prediction for structured prediction（可简要说明与本文研究路线的关系）\n- 更充分讨论 trained approaches (verifier/reward model) 作为 upper bound context\n\n### References\n- 修正 nedellec2026consistency 第一作者 (Yao → 正确引用)\n- 检查 snell2024scaling bib 作者格式\n\n### Appendix\n- ρ-AUROC dissociation / EM=1 压缩效应应在主文至少简要提及\n- Appendix D \\textsc 编译检查"
  }
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-15T02:09:06.732574+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4318
}
```

</details>

---


### Tool call

_source line 131 · 2026-05-15T02:09:11.208755+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/",
  "description": "List existing review report files"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/",
    "description": "List existing review report files"
  }
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-15T02:09:11.362286+00:00_

round_0.md
round_1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Assistant

_source line 133 · 2026-05-15T02:09:20.638024+00:00_

报告已自动存档为 `round_1.md`。

---

**Round 1 圆桌审稿完成。**

- **评分**: 3/5 (Findings)，两位 Reviewer 完全一致
- **5 个 Critical 问题**: (1) Bootstrap 检验细节缺失——核心负面结论无法验证；(2) Correlation-selection gap 有定义性成分 + logprob 失败分析缺失；(3) Nedellec 增量论证弱 + 引用作者错误；(4) "model-agnostic" overclaim；(5) RE 仅 SciERC 单数据集
- **主要分歧**: 模型规模和 RE 数据集的严重程度校准（R1 偏严，R2 偏宽），但双方均认同问题存在
- **与 Round 0 对比**: 零图表、成本分析问题可能已修复（本轮未被提及），但新增 bootstrap 细节、gap 定义性等 critical 问题。整体评分持平
- **最优先修复**: 补充 bootstrap 完整规范 + 修正 Nedellec 引用 + 降级 overclaim 措辞

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 134 · 2026-05-15T02:09:23.444432+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R1 的 3 个 Must-Fix 全部 AGREE（N1 bootstrap 细节最为关键），7 个 Should-Fix 中 6 个 AGREE、1 个 REBUT（W3 关于 ρ=0.38 "effective" 的措辞——论文实际并未称 "strong"，且 AUROC=0.75 才是实用性论据），所有小问题 AGREE。主要分歧在于问题严重程度校准：建议 N2 从 critical 降为 should-fix（措辞修正即可），W7（约束解码对 diversity 的影响）从 warning 升级——这可能是 correlation-selection gap 的根本成因而非仅是讨论遗漏。

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

_source line 135 · 2026-05-15T02:09:34.322469+00:00_

报告已提交，Reviewer 2 的交叉回应确认了收敛。审稿报告已包含 R2 的所有交叉回应要点（N2 降级建议、W7 升级建议、W3 反驳均已记录在 Reviewer Divergence 表中）。

**本轮圆桌审稿完成。**

总结：
- **评分**：3/5 (Findings)，两位 Reviewer 完全一致
- **5 个 Critical**：bootstrap 检验细节缺失（最优先）、gap 定义性解释力不足、Nedellec 增量论证弱+引用错误、model-agnostic overclaim、RE 单数据集
- **11 个 Warning**：约束解码 confound、per-sample signal 单薄、SJ 形式化歧义、logprob 温度缺失等
- **与 Round 0 对比**：零图表和成本分析问题可能已修复，但新 critical 问题浮现，整体持平

报告和 Issue Tracker 已同步更新并投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 14

## Round 14

80 recorded events


### User

_source line 136 · 2026-05-15T02:38:38.161536+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

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

_source line 137 · 2026-05-15T02:38:44.478419+00:00_

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

_source line 138 · 2026-05-15T02:38:44.529409+00:00_

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
…[truncated 2458 chars]

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

_source line 139 · 2026-05-15T02:38:51.717732+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 140 · 2026-05-15T02:38:51.768355+00:00_



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

_source line 141 · 2026-05-15T02:39:02.314291+00:00_

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

_source line 142 · 2026-05-15T02:39:02.767657+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (73 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_017_llama_conll_n16_s456_r1024（准备中）\n- exp_017_llama_conll_n16_r1024（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n- exp_007_ner_llama（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp008_re_n16（准备中）\n\n## 近期结论\n- **exp_002_conll_n16_r1024** (killed): —\n- **exp_007_llama_n16_r1024** (killed): —\n- **exp_017_llama_conll_n16_s123_r1024** (killed): —\n\n## 趋势\n成功 37 / 负向 18 / 失败 1 / 共 64\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 143 · 2026-05-15T02:39:03.721918+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/paper/**",
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
    "pattern": "projects/struct_self_consist_ie/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-15T02:39:03.772587+00:00_

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

_source line 145 · 2026-05-15T02:39:09.445236+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
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
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-15T02:39:09.897601+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 147 · 2026-05-15T02:39:10.199256+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
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
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 148 · 2026-05-15T02:39:10.249974+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

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

_source line 149 · 2026-05-15T02:39:15.071298+00:00_

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

_source line 150 · 2026-05-15T02:39:15.523700+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

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

_source line 151 · 2026-05-15T02:39:15.524047+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 152 · 2026-05-15T02:39:15.574550+00:00_



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

_source line 153 · 2026-05-15T02:39:23.206551+00:00_

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

_source line 154 · 2026-05-15T02:39:23.257206+00:00_

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

_source line 155 · 2026-05-15T02:39:23.458312+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
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
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-15T02:39:33.903396+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061
…[truncated 2413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 10445
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-15T02:39:37.668371+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 paper format page limit template ACL style double blind",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
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
    "query": "EMNLP 2026 paper format page limit template ACL style double blind",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-15T02:39:39.380438+00:00_

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

_source line 159 · 2026-05-15T02:39:39.431224+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex

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


### Tool result

_source line 160 · 2026-05-15T02:39:43.146500+00:00_

Web search results for query: "EMNLP 2026 paper format page limit template ACL style double blind"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Style Files and Formatting - ACL 2023","url":"https://2023.aclweb.org/calls/style_and_formatting/"},{"title":"EMNLP 2023: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2023-call-papers"},{"title":"Empirical Methods in Natural Language Processing EMNLP 2022 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/empirical-methods-natural-language-processing-emnlp-2022"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about EMNLP 2026 paper submission requirements:

## Submission System and Anonymity

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will 
…[truncated 1026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5478
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-15T02:39:47.012676+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission requirements page limit long paper short paper format",
  "allowed_domains": "['aclrollingreview.org']"
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
    "query": "ACL Rolling Review 2026 submission requirements page limit long paper short paper format",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-15T02:39:54.353326+00:00_

Web search results for query: "ACL Rolling Review 2026 submission requirements page limit long paper short paper format"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here are the ACL Rolling Review 2026 submission requirements for page limits and paper format:


…[truncated 937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7340
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-15T02:40:03.996580+00:00_

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

_source line 164 · 2026-05-15T02:40:04.950919+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-15T02:40:04.951413+00:00_

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

_source line 166 · 2026-05-15T02:40:05.403766+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 3826 chars]

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

_source line 167 · 2026-05-15T02:40:05.454503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 168 · 2026-05-15T02:40:05.907399+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-s
…[truncated 2466 chars]

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

_source line 169 · 2026-05-15T02:40:05.907864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-15T02:40:06.360272+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 2853 chars]

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

_source line 171 · 2026-05-15T02:40:06.360780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-15T02:40:06.863697+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
…[truncated 9072 chars]

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

_source line 173 · 2026-05-15T02:40:06.914628+00:00_

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

_source line 174 · 2026-05-15T02:40:07.818803+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).
8	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
11	
12	\paragraph{Why quality estimators fail as selectors.}
13	The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
14	Quality estimation ranks \textit{instances} by expected output quality; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance
…[truncated 3070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 175 · 2026-05-15T02:40:07.819331+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 176 · 2026-05-15T02:40:08.271935+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient.
11	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
12	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
13	
14	Several directions remain open.
15	Trained verifiers or reward models could close the selection gap by learning per-
…[truncated 555 chars]

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

_source line 177 · 2026-05-15T02:40:08.272442+00:00_

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

_source line 178 · 2026-05-15T02:40:08.724481+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	

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

_source line 179 · 2026-05-15T02:40:08.775309+00:00_

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

_source line 180 · 2026-05-15T02:40:08.775851+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 10209 chars]

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

_source line 181 · 2026-05-15T02:40:09.931094+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 182 · 2026-05-15T02:40:09.981751+00:00_



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

_source line 183 · 2026-05-15T02:40:17.464342+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
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
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 184 · 2026-05-15T02:40:17.515044+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

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

_source line 185 · 2026-05-15T02:40:17.917216+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 186 · 2026-05-15T02:40:17.967769+00:00_

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

_source line 187 · 2026-05-15T02:40:21.231599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 188 · 2026-05-15T02:40:21.734491+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 17900 chars]

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

_source line 189 · 2026-05-15T02:40:21.985929+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "config",
  "max_chars": "5000"
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
    "file": "config",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-15T02:40:22.036578+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

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

_source line 191 · 2026-05-15T02:40:28.318261+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/config*.yaml",
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
    "pattern": "**/struct_self_consist_ie/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 192 · 2026-05-15T02:40:28.820684+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 193 · 2026-05-15T02:40:28.871304+00:00_

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

_source line 194 · 2026-05-15T02:40:28.921883+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

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

_source line 195 · 2026-05-15T02:40:32.887905+00:00_

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

_source line 196 · 2026-05-15T02:40:33.491167+00:00_

1	issues:
2	  # ============================================================
3	  # Round 0 issues — updated with Round 1 actions
4	  # ============================================================
5	
6	  - id: "R0-C1"
7	    summary: "模型规模单一（仅 8B），严重限制普适性主张"
8	    category: experiment
9	    severity: critical
10	    status: in_progress
11	    first_raised_round: 0
12	    last_seen_round: 1
13	    mentions:
14	      - round: 0
15	        reviewers: [1, 2]
16	        note: "8B→8B 仅验证架构鲁棒性非规模鲁棒性。建议增加 >30B 或 <3B 模型。"
17	      - round: 1
18	        reviewers: [1, 2]
19	        note: "R1 列为 critical (C4)，R2 降为 should-fix。Discussion 仍用 model-agnostic 但 Limitations 承认局限，构成内部矛盾。"
20	    action_items:
21	      - round: 1
22	        action: "全文替换 model-agnostic → consistent across tested model families，消除与 Limitations 的内部矛盾"
23	        assigned_to: "Paper Agent"
24	        status: in_progress
25	    resolution: ""
26	    resolution_round: null
27	
28	  - id: "R0-C2"
29	    summary: "相关工作显著遗漏"
30	    category: framing
31	    severity: warning
32	    status: in_progress
33	    first_raised_round: 0
34	    last_seen_round: 1
35	    mentions:
36	      - round: 0
37	        reviewers: [1, 2]
38	        note: "5 篇核心文献缺失：Guo 2017, Snell 2024, Aggarwal 2023, CISC Huang 2025, 传统 IE confidence。"
39	      - round: 1
40	        reviewers: [1, 2]
41	        note: "Round 0 遗漏可能部分修复。Round 1 发现新遗漏：Optimal SC (2511.12309), Difficulty-Adaptive SC (NAACL 2025 Findings), conformal prediction 类。"
42	    action_items:
43	      - round: 1
44	        action: "补充 Optimal SC + Difficulty-Adaptive SC 引用；Related Work 简述 conformal prediction 路线；验证 Generative Self-Aggregation 真实性"
45	        assigned_to: "Agent (验证) + Paper Agent (写入)"
46	        status: in_progress
47	    resolution: ""
48	    resolution_round: null
49	
50	  - id: "R0-C3"
51	    summary: "RE 结论仅基于 SciERC 单数据集，不足以称 universal bottleneck"
52	    category: experiment
53	    severity: critical
54	    status: in_progress
55	    first_raised_round
…[truncated 15474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 197 · 2026-05-15T02:40:33.591993+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
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
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 198 · 2026-05-15T02:40:33.744664+00:00_

Found 3 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl
AGENTS.md
CLAUDE.md

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

_source line 199 · 2026-05-15T02:40:38.162682+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review.*paperreview.*enabled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
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
    "pattern": "external_review.*paperreview.*enabled",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 200 · 2026-05-15T02:40:38.314968+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl:39:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl:111:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl:138:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl:199:{"ts": "2026-05-15T02:40:38.162682+00:00", "role": "tool", "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director", "text": "called Grep", "tool": "Grep", "tool_args": {"pattern": "external_review.*paperreview.*enabled", "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1", "output_mode": "content"}}

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

_source line 201 · 2026-05-15T02:40:41.829212+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "paperreview_ai|external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "*.yaml",
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
    "pattern": "paperreview_ai|external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 202 · 2026-05-15T02:40:41.880398+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 203 · 2026-05-15T02:40:45.848322+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/project.yaml",
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
    "pattern": "**/struct_self_consist_ie/project.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 204 · 2026-05-15T02:40:46.150034+00:00_

No files found

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

_source line 205 · 2026-05-15T02:40:46.150457+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/*.yaml",
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
    "pattern": "**/struct_self_consist_ie/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 206 · 2026-05-15T02:40:46.251338+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/secrets/struct_self_consist_ie/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml

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

_source line 207 · 2026-05-15T02:40:55.192390+00:00_

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

_source line 208 · 2026-05-15T02:40:55.242987+00:00_

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

_source line 209 · 2026-05-15T02:42:03.576424+00:00_

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

_source line 210 · 2026-05-15T02:42:03.627020+00:00_



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

_source line 211 · 2026-05-15T02:42:32.698684+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper ≤8 页正文，double-blind\n- **匿名规则**: Double-blind，无匿名期要求\n- **附录**: 允许，不计页数，不保证审稿人阅读\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`（sections/ 子目录含全部章节，references.bib 含 40 条引用）\n\n### 你的审查侧重\n**方法严谨性 + 实验设计**。重点关注：\n1. **统计检验规范性**：bootstrap 检验是否完整报告（n, B, paired/unpaired, CI, 统计量）\n2. **Soft Jaccard 形式化**：Eq.(4) 定义是否完备（sim 函数、g_i/g_j 含义、Hungarian 阈值）\n3. **Correlation-selection gap 论证**：instance-level vs per-sample 区分是否清晰，logprob 失败原因分析是否充分\n4. **实验覆盖度**：RE 仅 SciERC 单数据集是否充分 hedge，WNUT-17 boundary claim 措辞是否过强\n5. **训练设置对称性**：Qwen/LLaMA 是否相同训练流程，cross-model 比较是否 fair\n6. **Robustness 分析**：logprob 温度敏感性数据缺失是否充分说明，N-scaling 结论是否 supported\n\n### Round 0-1 遗留 Open Issues（你需要检查是否已修复）\n- **R1-N1 [critical]**: Bootstrap 检验细节不足——需确认 Section 5.3 是否已补完整规范（n=529, B=10,000, paired, 统计量, seed 含义）\n- **R1-N2 [critical]**: Correlation-selection gap 解释力不足——需确认 Discussion 是否已区分 instance-level limitation vs per-sample empirical finding，logprob failure 分析是否充分\n- **R1-N3 [warning]**: Per-sample signal 仅 logprob 1 个——需确认是否已说明 Table 5 SJ = consensus-proximity = LOO-SJ\n- **R1-W1 [warning]**: SJ 形式化有歧义——需确认 Eq.(4) g_i/g_j、sim 公式、Hungarian 阈值是否已补全\n- **R1-W2 [warning]**: Entity voting & SJ 冗余度——需确认是否已报告 Voting-SJ correlation 并论证差异\n- **R0-W4/R1-N1 [critical]**: 统计检验不系统——需确认是否已补充 bootstrap CI\n- **R1-W4 [warning]**: Logprob 温度敏感性数据缺失——需确认 robustness 结论是否已限定\n- **R1-W6 [warning]**: LLaMA fine-tuning 状态——需确认 Section 4 是否已明确说明\n- **R1-W7 [warning]**: 约束解码对 sampling diversity 影响——需确认 Discussion 是否已讨论\n- **R0-C3 [critical]**: RE 仅 SciERC——需确认措辞是否已降级\n\n### 输出格式\n按 EMNLP 审稿标准输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → 对遗留 Issue 的逐条状态判定（resolved/partially/unresolved）→ Overall Score（1-5）+ Confidence（1-5）",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "2"
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
    "text": "## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper ≤8 页正文，double-blind\n- **匿名规则**: Double-blind，无匿名期要求\n- **附录**: 允许，不计页数，不保证审稿人阅读\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`（sections/ 子目录含全部章节，references.bib 含 40 条引用）\n\n### 你的审查侧重\n**方法严谨性 + 实验设计**。重点关注：\n1. **统计检验规范性**：bootstrap 检验是否完整报告（n, B, paired/unpaired, CI, 统计量）\n2. **Soft Jaccard 形式化**：Eq.(4) 定义是否完备（sim 函数、g_i/g_j 含义、Hungarian 阈值）\n3. **Correlation-selection gap 论证**：instance-level vs per-sample 区分是否清晰，logprob 失败原因分析是否充分\n4. **实验覆盖度**：RE 仅 SciERC 单数据集是否充分 hedge，WNUT-17 boundary claim 措辞是否过强\n5. **训练设置对称性**：Qwen/LLaMA 是否相同训练流程，cross-model 比较是否 fair\n6. **Robustness 分析**：logprob 温度敏感性数据缺失是否充分说明，N-scaling 结论是否 supported\n\n### Round 0-1 遗留 Open Issues（你需要检查是否已修复）\n- **R1-N1 [critical]**: Bootstrap 检验细节不足——需确认 Section 5.3 是否已补完整规范（n=529, B=10,000, paired, 统计量, seed 含义）\n- **R1-N2 [critical]**: Correlation-selection gap 解释力不足——需确认 Discussion 是否已区分 instance-level limitation vs per-sample empirical finding，logprob failure 分析是否充分\n- **R1-N3 [warning]**: Per-sample signal 仅 logprob 1 个——需确认是否已说明 Table 5 SJ = consensus-proximity = LOO-SJ\n- **R1-W1 [warning]**: SJ 形式化有歧义——需确认 Eq.(4) g_i/g_j、sim 公式、Hungarian 阈值是否已补全\n- **R1-W2 [warning]**: Entity voting & SJ 冗余度——需确认是否已报告 Voting-SJ correlation 并论证差异\n- **R0-W4/R1-N1 [critical]**: 统计检验不系统——需确认是否已补充 bootstrap CI\n- **R1-W4 [warning]**: Logprob 温度敏感性数据缺失——需确认 robustness 结论是否已限定\n- **R1-W6 [warning]**: LLaMA fine-tuning 状态——需确认 Section 4 是否已明确说明\n- **R1-W7 [warning]**: 约束解码对 sampling diversity 影响——需确认 Discussion 是否已讨论\n- **R0-C3 [critical]**: RE 仅 SciERC——需确认措辞是否已降级\n\n### 输出格式\n按 EMNLP 审稿标准输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → 对遗留 Issue 的逐条状态判定（resolved/partially/unresolved）→ Overall Score（1-5）+ Confidence（1-5）",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "2"
  }
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-15T02:42:53.854703+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21156
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-15T02:42:54.106108+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 2 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper ≤8 页正文，double-blind\n- **匿名规则**: Double-blind，无匿名期要求\n- **附录**: 允许，不计页数，不保证审稿人阅读\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`（sections/ 子目录含全部章节，references.bib 含 40 条引用）\n\n### 你的审查侧重\n**新颖性 + 完整性 + 格式**。重点关注：\n1. **Novelty 定位**：相对于 Nedellec et al. (2026) 的增量贡献是否充分论证，\"first multi-family comparison\" claim 是否准确\n2. **Related Work 覆盖**：是否遗漏重要相关工作（特别是 self-consistency 变体、difficulty-adaptive 方法、conformal prediction、generative self-aggregation）\n3. **Claim 强度校准**：所有 claim 是否有数据支撑，ρ=0.38 是否有上下文对比，\"establishing capability boundary\" 等措辞是否过强\n4. **写作质量**：论文结构是否清晰，符号一致性，图表可读性，引用格式\n5. **ρ-AUROC dissociation 分析**：EM=1 压缩效应是否在主文充分解释\n6. **Contribution 声明**：三个 contributions 是否准确反映论文实际发现\n7. **引用真实性**：检查 bib 条目是否准确（特别是 nedellec2026consistency 的作者字段）\n\n### Round 0-1 遗留 Open Issues（你需要检查是否已修复）\n- **R1-N4 [critical]**: Nedellec et al. 增量贡献论证不足 + 引用作者错误——需确认 bib 是否已修正（Yao et al. vs Nédellec），增量论证是否加强\n- **R0-C2 [warning]**: 相关工作遗漏——需确认是否已补充 Optimal SC、Difficulty-Adaptive SC、conformal prediction 类引用\n- **R1-W3 [warning]**: ρ=0.38 缺乏 contextualization——需确认是否已补充与 semantic entropy/P(True) 等的对比\n- **R1-W5 [warning]**: \"establishing capability boundary\" 措辞过强——需确认是否已改为 \"consistent with\" 或 \"suggests\"\n- **R1-W8 [warning]**: \"first systematic evaluation\" claim 过强——需确认是否已收窄 scope\n- **R1-W9 [warning]**: 遗漏引用——需确认 Optimal SC (2511.12309)、Difficulty-Adaptive SC (NAACL 2025)、Generative Self-Aggregation 是否已补\n- **R1-W10 [warning]**: ρ-AUROC dissociation 机制分析浅——需确认 EM=1 压缩效应是否已在主文阐述\n- **R1-M1 [info]**: Logistic regression proxy 提及但无结果——需确认是否已删除\n- **R1-M2 [info]**: +18pp on GSM8K 未注明模型——需确认是否已补 (PaLM-540B)\n- **R0-C1 [critical]**: 模型规模单一——需确认是否已消除 model-agnostic 与 Limitations 的内部矛盾\n- **R0-C4 [warning]**: SJ 新颖性有限——需确认增量贡献论证是否加强\n\n### 输出格式\n按 EMNLP 审稿标准输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → 对遗留 Issue 的逐条状态判定（resolved/partially/unresolved）→ Overall Score（1-5）+ Confidence（1-5）",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "2"
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
    "text": "## Round 2 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper ≤8 页正文，double-blind\n- **匿名规则**: Double-blind，无匿名期要求\n- **附录**: 允许，不计页数，不保证审稿人阅读\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`（sections/ 子目录含全部章节，references.bib 含 40 条引用）\n\n### 你的审查侧重\n**新颖性 + 完整性 + 格式**。重点关注：\n1. **Novelty 定位**：相对于 Nedellec et al. (2026) 的增量贡献是否充分论证，\"first multi-family comparison\" claim 是否准确\n2. **Related Work 覆盖**：是否遗漏重要相关工作（特别是 self-consistency 变体、difficulty-adaptive 方法、conformal prediction、generative self-aggregation）\n3. **Claim 强度校准**：所有 claim 是否有数据支撑，ρ=0.38 是否有上下文对比，\"establishing capability boundary\" 等措辞是否过强\n4. **写作质量**：论文结构是否清晰，符号一致性，图表可读性，引用格式\n5. **ρ-AUROC dissociation 分析**：EM=1 压缩效应是否在主文充分解释\n6. **Contribution 声明**：三个 contributions 是否准确反映论文实际发现\n7. **引用真实性**：检查 bib 条目是否准确（特别是 nedellec2026consistency 的作者字段）\n\n### Round 0-1 遗留 Open Issues（你需要检查是否已修复）\n- **R1-N4 [critical]**: Nedellec et al. 增量贡献论证不足 + 引用作者错误——需确认 bib 是否已修正（Yao et al. vs Nédellec），增量论证是否加强\n- **R0-C2 [warning]**: 相关工作遗漏——需确认是否已补充 Optimal SC、Difficulty-Adaptive SC、conformal prediction 类引用\n- **R1-W3 [warning]**: ρ=0.38 缺乏 contextualization——需确认是否已补充与 semantic entropy/P(True) 等的对比\n- **R1-W5 [warning]**: \"establishing capability boundary\" 措辞过强——需确认是否已改为 \"consistent with\" 或 \"suggests\"\n- **R1-W8 [warning]**: \"first systematic evaluation\" claim 过强——需确认是否已收窄 scope\n- **R1-W9 [warning]**: 遗漏引用——需确认 Optimal SC (2511.12309)、Difficulty-Adaptive SC (NAACL 2025)、Generative Self-Aggregation 是否已补\n- **R1-W10 [warning]**: ρ-AUROC dissociation 机制分析浅——需确认 EM=1 压缩效应是否已在主文阐述\n- **R1-M1 [info]**: Logistic regression proxy 提及但无结果——需确认是否已删除\n- **R1-M2 [info]**: +18pp on GSM8K 未注明模型——需确认是否已补 (PaLM-540B)\n- **R0-C1 [critical]**: 模型规模单一——需确认是否已消除 model-agnostic 与 Limitations 的内部矛盾\n- **R0-C4 [warning]**: SJ 新颖性有限——需确认增量贡献论证是否加强\n\n### 输出格式\n按 EMNLP 审稿标准输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → 对遗留 Issue 的逐条状态判定（resolved/partially/unresolved）→ Overall Score（1-5）+ Confidence（1-5）",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "2"
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-15T02:42:55.767360+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1661
}
```

</details>

---


### Assistant

_source line 215 · 2026-05-15T02:43:05.159333+00:00_

Round 2 圆桌审稿已启动。两位 Reviewer 任务已分配：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| Reviewer 1 | 方法严谨性 + 实验设计（bootstrap 规范、SJ 形式化、gap 论证、实验覆盖度） | ✅ 已派发 |
| Reviewer 2 | 新颖性 + 完整性 + 格式（Nedellec 增量贡献、Related Work、claim 校准、写作质量） | ✅ 已派发 |

**本轮重点**：评估 Round 0-1 共 18 个 open/in_progress issue 的修复状态，论文当前版本已可见多项修订（bootstrap 细节补充、LLaMA 训练说明、logprob 失败分析、约束解码讨论、PaLM-540B 注释等）。

等待两位 Reviewer 返回独立初审结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 216 · 2026-05-15T02:48:21.362280+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 2 审稿意见

**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**审查侧重**: 方法严谨性 + 实验设计

---

## Summary

本文系统比较了三个族群（structural/surface/model-internal）的五种 confidence signal 在 generative IE 中的 quality estimation 与 sample selection 效果。核心发现是 "correlation-selection gap"：instance-level 信号能预测 input difficulty（ρ 达 0.38）但无法从 N 个候选中选出最优 output（所有信号均未显著超过 greedy，p>0.39）。此外，信号排名依赖 task difficulty（EM 领先 easy tasks，SJ/Voting 领先 hard tasks）。

---

## 总体评分

**Overall**: 3.5 (Borderline Conference / Strong Findings)
**一句话总结**: Quality estimation 分析全面扎实，但最核心的 selection gap 负结论证据面偏窄（1 dataset × 1 model），削弱了 "fundamental disconnect" 的 framing 强度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | QE 分析严谨、bootstrap 规范完整；但 selection 证据限于 SciERC/Qwen，WNUT-17 boundary claim 缺系统数据 |
| Excitement | 3/5 | QE vs selection 的概念区分有价值；但负结论（selection 失败）在 instance-level signal 框架下可从理论预期，novelty 中等 |
| Reproducibility | 3.5/5 | 训练细节（LoRA rank/α/epochs/framework）完整，bootstrap 规范清晰；但 n=529 vs SciERC 551 的 filtering 未交代 |
| Confidence | 4/5 | 逐节逐表验证了关键 claims，仔细检查了 Round 0-1 遗留问题修复状态 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Selection 结果仅限 SciERC/Qwen，与 framing 不匹配

- **具体位置**: Table 3 (Section 5.3)；Abstract ("no signal reliably surpasses greedy decoding on either task")
- **问题**: 论文最核心的贡献——correlation-selection gap——仅在 SciERC 上用 Qwen 验证。Quality estimation 覆盖 3 datasets × 2 models，但 selection 仅 1 dataset × 1 model。Abstract 和 Conclusion 的 framing 暗示这是跨 task/model 的 "fundamental disconnect"，但 evidence base 不支撑这一泛化。CoNLL selection 未报告（即使 headroom 小，negative result 本身也有价值），LLaMA SciERC selection 未报告。
- **为什么影响接收**: Contribution #2 是论文的 differentiator（与 Nédellec et al. 2026 的关键区别就是 selection 分析），如果 selection 证据过窄，这个 claim 的 generalizability 存疑。
- **建议**: 至少补 LLaMA SciERC selection 结果以验证 cross-model generalization；CoNLL selection 放 appendix（即使结论是 ceiling effect 导致无 headroom，也应明确报告）。

**N2** [critical] WNUT-17 "capability boundary" claim 缺乏系统证据

- **具体位置**: Section 5.1 ("On WNUT-17, SJ achieves only ρ=0.082 (p=0.106), suggesting a capability boundary beyond which all signals break down")；Contribution 3 (Introduction)
- **问题**: 这一 claim 列为 Contribution #3，但全文仅报告 SJ 一个信号的一个 ρ 值。其他四个信号（Voting、EM、FK、Logprob）在 WNUT-17 上的表现未出现在任何 table 或 text 中。更关键的是，SJ ρ=0.082 的 p=0.106 意味着该 correlation 本身不显著——用一个不显著的单信号结果支撑 "all signals break down" 的 claim 在逻辑上不成立。
- **为什么影响接收**: Abstract 和 Contribution list 明确将 WNUT-17 boundary 作为 task-complexity 贡献的一部分，reviewer 会期待至少一个完整的 WNUT-17 结果表。
- **建议**: 在 Table 1 或 Appendix 增加 WNUT-17 column/table，报告全部 5 signal 的 ρ 和 AUROC。如果确实全部 collapse，这反而是更强的证据。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Quality estimation ρ 在 N=8 缺乏不确定性量化

- **具体位置**: Table 1 (Section 5.1)
- **问题**: Table 1 的 N=8 行报告 point estimates（ρ 和 AUROC）without CIs、standard errors 或 significance tests。仅 N=16 3-seed block 有 ±std。主要 claims（如 "entity voting achieves ρ=0.38"）无 associated uncertainty。这与 Section 5.3 selection 结果的 thorough bootstrap（CI、Cohen's d、sign test）形成不一致：QE 是正面结论，selection 是负面结论，但正面结论反而缺乏统计支撑。
- **建议**: 对 N=8 主要 ρ 值报告 bootstrap CIs，或至少在 Appendix 补充 3-seed runs。

**W2** [warning] SJ Hungarian matching 缺 threshold 规范

- **具体位置**: Eq.(4), Section 3.2
- **问题**: Eq.(4) 现在已定义 sim = token-level IoU，g_i/g_j = per-type extraction counts（比 Round 1 改善显著）。但 Hungarian algorithm 是否有 minimum similarity threshold？如果 threshold=0，两个完全不相关的 span 也会被 matched，导致 SJ numerator 非零。如果 threshold>0，threshold 的选择影响所有下游 ρ 值但未报告。
- **建议**: 明确说明是否使用 threshold（以及值），或解释为什么 zero-overlap matches 对 SJ 影响可忽略。

**W3** [warning] RE selection 无统计检验

- **具体位置**: Table 3, Section 5.3
- **问题**: NER selection 报告了完整 bootstrap（p=0.39, CI [-3.0, +4.2]pp, Cohen's d=0.038, sign test）。RE selection 仅报告 "no signal exceeds greedy (0.404) despite 18.1 pp of oracle headroom"，无 p-value、CI 或 effect size。RE 的 selection gap 实际更大（greedy 胜出），理应同样给出统计检验。
- **建议**: 补充 RE selection 的 bootstrap p-value 和 CI。

**W4** [warning] SciERC cross-model 不对称（N=8）

- **具体位置**: Table 1; Appendix A.3
- **问题**: Table 1 SciERC 列仅为 Qwen 结果（表头未标注模型），LLaMA SciERC 仅在 Appendix 文字中零散出现（SJ ρ=0.363, FK ρ=0.327），不完整（5 个信号只报了 2 个），无 AUROC，无 table。SciERC 是驱动核心 claims 的 primary dataset，cross-model validation 的缺失在此处比在 CoNLL 上更关键。
- **建议**: Table 1 增加 SciERC (LLaMA) 列，或在 Appendix 补完整 table。

**W5** [warning] n=529 vs SciERC n=551 的 discrepancy

- **具体位置**: Section 5.3 ("over n=529 NER instances")
- **问题**: SciERC test set 有 551 instances，但 bootstrap 用 n=529。22 instances 被 drop 的原因未交代。如果是 filtering（如 zero-entity instances），应明确说明 filtering criteria。
- **建议**: 一句话说明 n=529 的来源。

---

## 小问题（不影响接收）

- Eq.(4) 分母 $\sum_g \max(|g_i|, |g_j|)$ 是非标准 Jaccard variant，一句解释为何不用 $|A \cup B|$ 会帮助理解。
- FK adaptation (Section 3.2)：N 个来自同一模型的 stochastic samples 不是 Fleiss' κ 假设的 "independent raters"，brief acknowledgment 即可。
- Table 3 的 EM 行显示 "---" 但 caption 未解释原因，caption 可加 "EM produces binary agreement without sample ranking."——实际 caption 已有此句 ✓，但 RE 列也是 "---"，可考虑统一 footnote 说明。
- Section 5.3："three random seeds (42, 123, 456) refer to independent inference runs"——但 Table 1 的 N=8 primary results 未说明用了哪个 seed 或是否 averaged。

---

## Questions for Authors

**Q1.** WNUT-17 上 Voting/EM/FK/Logprob 的 ρ 和 AUROC 分别是多少？如果全部 non-significant，这本身是一个强结论；如果某个信号显著，则 "all signals break down" 需要修正。

**Q2.** CoNLL 的 best-of-N selection 结果（即使 greedy 已 >0.91）？一个可能的 outcome 是 oracle headroom 很小 → selection gap 不存在 → 说明 gap 是 hard-task specific，这也是有价值的 insight。

**Q3.** SciERC bootstrap n=529：22 instances 被 drop 的 criteria 是什么？

**Q4.** SJ Hungarian matching 是否有 minimum similarity threshold？如果无 threshold，matched pairs 中 sim≈0 的比例有多高？

**Q5.** Table 1 的 N=8 主要结果是 single-seed 还是 averaged？如果 single-seed，是否有 variance estimates？

---

## Round 0-1 遗留 Issue 状态判定

| Issue | 状态 | 判定依据 |
|-------|------|----------|
| **R1-N1** [critical]: Bootstrap 检验细节不足 | ✅ **Resolved** | Section 5.3 补齐：n=529, B=10K, paired, percentile 95% CIs [-3.0, +4.2]pp, Cohen's d=0.038, sign test 61W/70L, seeds(42/123/456) 含义明确 |
| **R1-N2** [critical]: Correlation-selection gap 解释力不足 | ✅ **Resolved** | Discussion 清晰区分 instance-level（rank instances）vs per-sample（rank candidates within instance）；logprob 失败归因于 constrained decoding grammar compliance + 75% ties |
| **R1-N3** [warning]: Per-sample signal 仅 logprob | ✅ **Resolved** | Section 3.3 明确 consensus-proximity = LOO-SJ；Appendix 验证 LOO-SJ Δρ=-0.014（negligible circularity） |
| **R1-W1** [warning]: SJ 形式化有歧义 | ⚠️ **Partially resolved** | sim = token-level IoU ✓, g_i/g_j = per-type extraction counts ✓, Hungarian threshold 仍未指定 |
| **R1-W2** [warning]: Voting-SJ 冗余度 | ✅ **Resolved** | 报告 inter-signal ρ=0.659 (NER), 0.605 (RE) + differential behavior across difficulty 论述 |
| **R0-W4/R1-N1** [critical]: 统计检验不系统 | ⚠️ **Partially resolved** | Selection 有完整 bootstrap ✓；QE Table 1 N=8 仍为 point estimates without CIs |
| **R1-W4** [warning]: Logprob 温度敏感性 | ✅ **Resolved** | Section 5.4 + Limitations 均明确 acknowledge T=0.7 logprob data missing |
| **R1-W6** [warning]: LLaMA fine-tuning 状态 | ✅ **Resolved** | Section 4.1: 两模型 identical LoRA (rank=32, α=64), 5 epochs, LLaMA Factory |
| **R1-W7** [warning]: 约束解码影响 | ✅ **Resolved** | Discussion: acknowledged constrained decoding compresses diversity + random baseline gap 3.6pp confirms variance exists + future work identified |
| **R0-C3** [critical]: RE 仅 SciERC | ✅ **Resolved** | Introduction/Discussion/Conclusion/Appendix 四处 hedge |

---

## 主要优势

1. **概念贡献清晰**: QE vs selection 的 distinction 是 generative IE 社区需要的，且 formulation (Section 3.1 per-sample vs instance-level) 精确可操作。
2. **Quality estimation 分析全面**: 5 signals × 4 configurations (Table 1) + conditional filtering + capability stratification + per-relation diagnostic，分析深度超过多数实证论文。
3. **Bootstrap 规范（selection）**: Cohen's d、sign test、percentile CI、seed 解释一应俱全，是 NLP 实证论文的良好标准。
4. **ρ-AUROC dissociation 的发现**: EM 在 ρ 排名低但 AUROC 领先（Section 5.1），揭示 binary vs continuous signal properties 的 metric-dependent 行为，对 practitioners 有直接 actionable 价值。
5. **诚实的 hedging**: RE single-dataset 限制在 4 处 acknowledge，logprob temperature gap 在正文 + Limitations 双重标注——Round 0-1 的 self-awareness 问题已有实质改善。
6. **与 Nédellec et al. (2026) 的定位清晰**: 三点差异化（structural matching / selection analysis / difficulty gradient）具体且有说服力。

---

## 总结

论文从 Round 0 到 Round 2 有显著改善：bootstrap 规范化、SJ 形式化、RE hedging、constrained decoding 讨论等遗留问题大多已 resolved 或 partially resolved。Quality estimation 分析是本文的强项，coverage 和 depth 均达到 long paper 标准。

主要 concern 集中在 evidence breadth vs framing breadth 的 mismatch：correlation-selection gap 作为核心贡献，仅在 1 dataset × 1 model 上验证（N1）；WNUT-17 boundary 作为 listed contribution，仅有 1 个不显著的数据点（N2）。如果这两个问题得到补充，论文有 Conference 实力；当前状态更适合 Findings。

**Overall**: 3.5/5 (Borderline Conference / Strong Findings)
**Confidence**: 4/5

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

_source line 217 · 2026-05-15T02:48:29.100410+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 218 · 2026-05-15T02:48:32.016659+00:00_

[Reviewer 1 审稿结果]:
Round 2 审稿意见已提交给 Review Director。

核心判断：**3.5/5 (Borderline Conference / Strong Findings)**。

相比 Round 0-1 改善显著——bootstrap 规范、SJ 形式化、RE hedging、constrained decoding 讨论等遗留问题大多 resolved。Quality estimation 分析达到 long paper 标准。

两个 Must-Fix 问题阻碍 Conference 推荐：
1. **Selection gap 证据面过窄**：核心贡献仅在 SciERC/Qwen 1 个 setting 验证，但 framing 为 "fundamental disconnect"
2. **WNUT-17 boundary claim 无系统数据**：仅 SJ 一个不显著的 ρ 值支撑 "all signals break down" 的 Contribution #3

补齐这两处后可达 Conference 水平。

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

_source line 219 · 2026-05-15T02:48:37.873502+00:00_

收到 Reviewer 1 的意见。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 17

## Round 17

6 recorded events


### User

_source line 220 · 2026-05-15T02:48:58.700247+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 2 审稿意见（新颖性 + 完整性 + 格式）

### Summary

本文系统比较了五种来自三个family的confidence signals（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在generative IE（NER + RE）中的quality estimation和sample selection表现。核心发现是"correlation-selection gap"：instance-level consistency signals是有效的quality estimators（ρ达0.38, AUROC达0.75），但无法可靠超越greedy decoding进行best-of-N selection（p>0.39），尽管存在13-18pp的oracle headroom。附带发现signal ranking随task difficulty变化。

---

### Strengths

- **S1: 清晰定义的研究问题。** quality estimation与sample selection的解耦（§3.1, per-sample vs. instance-level signal）对该领域有框架性价值。
- **S2: 统计严谨性。** Bootstrap resampling (B=10,000)、95% CI、Cohen's d、sign test、多seed验证等，远超多数同类empirical study。
- **S3: Correlation-selection gap是genuinely useful negative result。** Table 3 + Figure 3 直观展示gap，对test-time scaling后续研究有指导价值。
- **S4: 诚实的Limitations section。** 全文多处hedged表述（"consistent across tested model families"），未过度泛化。
- **S5: Related work覆盖全面。** §2涵盖self-consistency变体、difficulty-adaptive方法、generative self-aggregation、conformal prediction、semantic uncertainty等。

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] ρ=0.38 仍缺乏跨方法数值对比（R1-W3 部分未解决）
- 位置：§4.2 第一段（experiments.tex line 64）；§5 Discussion 第一段
- 问题：论文将ρ=0.38 contextualize为"14% variance explained"和AUROC=0.749，但这是intra-study context。读者无法判断0.38在confidence estimation文献中的位置——semantic entropy (Kuhn 2023)在QA上报告AUROC通常0.75-0.85，P(True) (Kadavath 2022)也有公开ρ值。论文§2引用了这些方法但零数值对比。
- 影响：若ρ=0.38属于typical甚至below-average，则"effective quality estimators"的framing需重新校准。
- 建议：§4.2或§5加footnote，引用已有方法的典型值，明确structured IE与discrete-answer tasks直接比较的困难性。

**N2** [critical] Selection实验仅在SciERC上进行，未解释CoNLL/WNUT-17的缺失
- 位置：Table 3（experiments.tex line 96-115）
- 问题：Best-of-N selection仅报告SciERC，但核心claim是gap在IE中普遍存在。CoNLL headroom可能极小、WNUT-17样本质量太低——但这些reasoning需要stated。
- 影响：三数据集quality estimation → 一数据集selection验证，逻辑链不完整。
- 建议：补充CoNLL/WNUT-17 selection结果（即使headroom为0也有信息量），或明确说明omission原因并给出oracle-greedy gap。

---

### Should-Fix 问题

**W1** [warning] Constrained decoding作为全局confound未充分讨论
- 位置：§5 "Why logprob fails" 段（discussion.tex lines 25-27）
- 问题：constrained decoding压缩per-sample diversity的影响不仅限于logprob，可能影响所有signal的selection表现。论文仅在logprob段落提及，未在Limitations中列为key confound。
- 建议：Limitations section明确列出，或提供per-sample F1 variance数据证明diversity已足够。

**W2** [warning] Abstract "across NER and relation extraction on three datasets" 可能误导
- 位置：Abstract line 3
- 问题：RE实际仅在SciERC上评估。
- 建议：改为"across NER (three datasets) and RE (SciERC)"或类似表述。

**W3** [warning] WNUT-17对"三数据集difficulty gradient"的贡献有限
- 位置：§4.2 line 76；Contribution 3
- 问题：WNUT-17 SJ ρ=0.082 (p=0.106)，信号与F1的相关性不显著，本质上是negative control。
- 建议：明确定位为"capability boundary probe"而非同等地位的evaluation benchmark。

**W4** [warning] EM用于selection的缺失未充分解释
- 位置：Table 3 "---" for EM
- 问题：EM<1时majority output可被识别，picking majority output就是standard self-consistency voting。未解释为何不以此方式使用EM。
- 建议：实现majority-vote selection并报告，或解释为何majority在structured IE中不well-defined。

---

### Minor Issues

- M1: Ethics Statement section缺失（ARR不强制但建议补充）
- M2: `hobelsberger2025systematic`和`lightman2024verify`在OpenAlex中未找到，likely是API覆盖问题而非引用错误
- M3: `feng2025optimal` first-author mismatch为false positive（API surname/firstname混淆）

---

### 遗留 Issue 状态

| Issue | 状态 |
|-------|------|
| R1-N4 bib作者+增量论证 | ✅ Resolved |
| R0-C2 Related work遗漏 | ✅ Resolved |
| R1-W3 ρ=0.38 context | ⚠️ Partially — intra-study OK, cross-method仍缺 |
| R1-W5 "establishing capability boundary" | ✅ Resolved |
| R1-W8 "first systematic evaluation" | ✅ Resolved |
| R1-W9 遗漏引用 | ✅ Resolved |
| R1-W10 ρ-AUROC dissociation | ✅ Resolved |
| R1-M1 Logistic regression proxy | ✅ Resolved |
| R1-M2 +18pp model attribution | ✅ Resolved |
| R0-C1 模型规模单一 | ✅ Resolved（不再overclaim） |
| R0-C4 SJ新颖性 | ⚠️ Partially — 框架转向comparison study |

---

### Overall Assessment

**Overall**: 3.5（Borderline Conference）
**Confidence**: 4/5

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 4/5 | 实验严谨，但selection仅SciERC + constrained decoding confound |
| Excitement | 3/5 | Gap是useful contribution，但整体为empirical study without methodological novelty |
| Reproducibility | 4/5 | 配置明确，缺代码release承诺 |

**核心判断**：方法论扎实、统计严谨的empirical study。Correlation-selection gap有价值，但ρ=0.38缺乏cross-method context、selection仅单数据集验证制约了说服力。大部分Round 0-1 issues已resolved，仅R1-W3和R0-C4 partially open。如果N1和N2得到修复，可以支持conference acceptance。

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

_source line 221 · 2026-05-15T02:49:36.954438+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 2 审稿意见（新颖性 + 完整性 + 格式）\n\n### Summary\n\n本文系统比较了五种来自三个family的confidence signals（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在generative IE（NER + RE）中的quality estimation和sample selection表现。核心发现是\"correlation-selection gap\"：instance-level consistency signals是有效的quality estimators（ρ达0.38, AUROC达0.75），但无法可靠超越greedy decoding进行best-of-N selection（p>0.39），尽管存在13-18pp的oracle headroom。附带发现signal ranking随task difficulty变化。\n\n### Must-Fix 问题\n\n**N1** [critical] ρ=0.38 仍缺乏跨方法数值对比（R1-W3 部分未解决）\n- 位置：§4.2 第一段；§5 Discussion 第一段\n- 问题：论文将ρ=0.38 contextualize为\"14% variance explained\"和AUROC=0.749，但这是intra-study context。读者无法判断0.38在confidence estimation文献中的位置——semantic entropy (Kuhn 2023)在QA上报告AUROC通常0.75-0.85，P(True) (Kadavath 2022)也有公开ρ值。论文§2引用了这些方法但零数值对比。\n- 影响：若ρ=0.38属于typical甚至below-average，则\"effective quality estimators\"的framing需重新校准。\n- 建议：§4.2或§5加footnote，引用已有方法的典型值，明确structured IE与discrete-answer tasks直接比较的困难性。\n\n**N2** [critical] Selection实验仅在SciERC上进行，未解释CoNLL/WNUT-17的缺失\n- 位置：Table 3\n- 问题：Best-of-N selection仅报告SciERC，但核心claim是gap在IE中普遍存在。CoNLL headroom可能极小、WNUT-17样本质量太低——但这些reasoning需要stated。\n- 影响：三数据集quality estimation → 一数据集selection验证，逻辑链不完整。\n- 建议：补充CoNLL/WNUT-17 selection结果（即使headroom为0也有信息量），或明确说明omission原因并给出oracle-greedy gap。\n\n### Should-Fix 问题\n\n**W1** [warning] Constrained decoding作为全局confound未充分讨论\n- 位置：§5 \"Why logprob fails\" 段\n- 问题：constrained decoding压缩per-sample diversity的影响不仅限于logprob，可能影响所有signal的selection表现。论文仅在logprob段落提及，未在Limitations中列为key confound。\n- 建议：Limitations section明确列出，或提供per-sample F1 variance数据证明diversity已足够。\n\n**W2** [warning] Abstract \"across NER and relation extraction on three datasets\" 可能误导\n- 位置：Abstract line 3\n- 问题：RE实际仅在SciERC上评估。\n- 建议：改为\"across NER (three datasets) and RE (SciERC)\"或类似表述。\n\n**W3** [warning] WNUT-17对\"三数据集difficulty gradient\"的贡献有限\n- 位置：§4.2 line 76；Contribution 3\n- 问题：WNUT-17 SJ ρ=0.082 (p=0.106)，信号与F1的相关性不显著，本质上是negative control。\n- 建议：明确定位为\"capability boundary probe\"而非同等地位的evaluation benchmark。\n\n**W4** [warning] EM用于selection的缺失未充分解释\n- 位置：Table 3 \"---\" for EM\n- 问题：EM<1时majority output可被识别，picking majority output就是standard self-consistency voting。未解释为何不以此方式使用EM。\n- 建议：实现majority-vote selection并报告，或解释为何majority在structured IE中不well-defined。\n\n### Minor Issues\n\n- M1: Ethics Statement section缺失\n- M2-M3: bib条目检查（无实质问题）\n\n### Overall: 3.5（Borderline Conference），Confidence: 4/5",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "2"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 2 审稿意见（新颖性 + 完整性 + 格式）\n\n### Summary\n\n本文系统比较了五种来自三个family的confidence signals（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在generative IE（NER + RE）中的quality estimation和sample selection表现。核心发现是\"correlation-selection gap\"：instance-level consistency signals是有效的quality estimators（ρ达0.38, AUROC达0.75），但无法可靠超越greedy decoding进行best-of-N selection（p>0.39），尽管存在13-18pp的oracle headroom。附带发现signal ranking随task difficulty变化。\n\n### Must-Fix 问题\n\n**N1** [critical] ρ=0.38 仍缺乏跨方法数值对比（R1-W3 部分未解决）\n- 位置：§4.2 第一段；§5 Discussion 第一段\n- 问题：论文将ρ=0.38 contextualize为\"14% variance explained\"和AUROC=0.749，但这是intra-study context。读者无法判断0.38在confidence estimation文献中的位置——semantic entropy (Kuhn 2023)在QA上报告AUROC通常0.75-0.85，P(True) (Kadavath 2022)也有公开ρ值。论文§2引用了这些方法但零数值对比。\n- 影响：若ρ=0.38属于typical甚至below-average，则\"effective quality estimators\"的framing需重新校准。\n- 建议：§4.2或§5加footnote，引用已有方法的典型值，明确structured IE与discrete-answer tasks直接比较的困难性。\n\n**N2** [critical] Selection实验仅在SciERC上进行，未解释CoNLL/WNUT-17的缺失\n- 位置：Table 3\n- 问题：Best-of-N selection仅报告SciERC，但核心claim是gap在IE中普遍存在。CoNLL headroom可能极小、WNUT-17样本质量太低——但这些reasoning需要stated。\n- 影响：三数据集quality estimation → 一数据集selection验证，逻辑链不完整。\n- 建议：补充CoNLL/WNUT-17 selection结果（即使headroom为0也有信息量），或明确说明omission原因并给出oracle-greedy gap。\n\n### Should-Fix 问题\n\n**W1** [warning] Constrained decoding作为全局confound未充分讨论\n- 位置：§5 \"Why logprob fails\" 段\n- 问题：constrained decoding压缩per-sample diversity的影响不仅限于logprob，可能影响所有signal的selection表现。论文仅在logprob段落提及，未在Limitations中列为key confound。\n- 建议：Limitations section明确列出，或提供per-sample F1 variance数据证明diversity已足够。\n\n**W2** [warning] Abstract \"across NER and relation extraction on three datasets\" 可能误导\n- 位置：Abstract line 3\n- 问题：RE实际仅在SciERC上评估。\n- 建议：改为\"across NER (three datasets) and RE (SciERC)\"或类似表述。\n\n**W3** [warning] WNUT-17对\"三数据集difficulty gradient\"的贡献有限\n- 位置：§4.2 line 76；Contribution 3\n- 问题：WNUT-17 SJ ρ=0.082 (p=0.106)，信号与F1的相关性不显著，本质上是negative control。\n- 建议：明确定位为\"capability boundary probe\"而非同等地位的evaluation benchmark。\n\n**W4** [warning] EM用于selection的缺失未充分解释\n- 位置：Table 3 \"---\" for EM\n- 问题：EM<1时majority output可被识别，picking majority output就是standard self-consistency voting。未解释为何不以此方式使用EM。\n- 建议：实现majority-vote selection并报告，或解释为何majority在structured IE中不well-defined。\n\n### Minor Issues\n\n- M1: Ethics Statement section缺失\n- M2-M3: bib条目检查（无实质问题）\n\n### Overall: 3.5（Borderline Conference），Confidence: 4/5",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "2"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-15T02:49:55.092324+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18137
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-15T02:49:55.393938+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 2 审稿意见（方法严谨性 + 实验设计）\n\n### Must-Fix 问题\n\n**N1** [critical] Selection 结果仅限 SciERC/Qwen，与 framing 不匹配\n- 具体位置：Table 3 (Section 5.3)；Abstract (\"no signal reliably surpasses greedy decoding on either task\")\n- 问题：论文最核心的贡献——correlation-selection gap——仅在 SciERC 上用 Qwen 验证。Quality estimation 覆盖 3 datasets × 2 models，但 selection 仅 1 dataset × 1 model。Abstract 和 Conclusion 的 framing 暗示这是跨 task/model 的 \"fundamental disconnect\"，但 evidence base 不支撑这一泛化。CoNLL selection 未报告（即使 headroom 小，negative result 本身也有价值），LLaMA SciERC selection 未报告。\n- 建议：至少补 LLaMA SciERC selection 结果以验证 cross-model generalization；CoNLL selection 放 appendix。\n\n**N2** [critical] WNUT-17 \"capability boundary\" claim 缺乏系统证据\n- 具体位置：Section 5.1\n- 问题：全文仅报告 SJ 一个信号的一个 ρ 值（0.082, p=0.106）。其他四个信号未报告。用一个不显著的单信号结果支撑 \"all signals break down\" 在逻辑上不成立。\n- 建议：Appendix 增加 WNUT-17 完整 table（5 signals × ρ + AUROC）。\n\n### Should-Fix 问题\n\n**W1** QE ρ 在 N=8 缺乏 uncertainty quantification（Table 1 point estimates without CIs）\n**W2** SJ Hungarian matching 缺 threshold 规范\n**W3** RE selection 无统计检验\n**W4** SciERC cross-model 不对称（LLaMA SciERC N=8 仅 2/5 signals 有数据）\n**W5** n=529 vs SciERC n=551 discrepancy 未解释\n\n### Minor Issues\n- Eq.(4) 非标准 Jaccard variant 缺一句解释\n- FK \"independent raters\" 假设不成立\n- Table 1 N=8 是 single-seed 还是 averaged 未说明\n\n### Overall: 3.5/5 (Borderline Conference / Strong Findings), Confidence: 4/5",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "2"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 2 审稿意见（方法严谨性 + 实验设计）\n\n### Must-Fix 问题\n\n**N1** [critical] Selection 结果仅限 SciERC/Qwen，与 framing 不匹配\n- 具体位置：Table 3 (Section 5.3)；Abstract (\"no signal reliably surpasses greedy decoding on either task\")\n- 问题：论文最核心的贡献——correlation-selection gap——仅在 SciERC 上用 Qwen 验证。Quality estimation 覆盖 3 datasets × 2 models，但 selection 仅 1 dataset × 1 model。Abstract 和 Conclusion 的 framing 暗示这是跨 task/model 的 \"fundamental disconnect\"，但 evidence base 不支撑这一泛化。CoNLL selection 未报告（即使 headroom 小，negative result 本身也有价值），LLaMA SciERC selection 未报告。\n- 建议：至少补 LLaMA SciERC selection 结果以验证 cross-model generalization；CoNLL selection 放 appendix。\n\n**N2** [critical] WNUT-17 \"capability boundary\" claim 缺乏系统证据\n- 具体位置：Section 5.1\n- 问题：全文仅报告 SJ 一个信号的一个 ρ 值（0.082, p=0.106）。其他四个信号未报告。用一个不显著的单信号结果支撑 \"all signals break down\" 在逻辑上不成立。\n- 建议：Appendix 增加 WNUT-17 完整 table（5 signals × ρ + AUROC）。\n\n### Should-Fix 问题\n\n**W1** QE ρ 在 N=8 缺乏 uncertainty quantification（Table 1 point estimates without CIs）\n**W2** SJ Hungarian matching 缺 threshold 规范\n**W3** RE selection 无统计检验\n**W4** SciERC cross-model 不对称（LLaMA SciERC N=8 仅 2/5 signals 有数据）\n**W5** n=529 vs SciERC n=551 discrepancy 未解释\n\n### Minor Issues\n- Eq.(4) 非标准 Jaccard variant 缺一句解释\n- FK \"independent raters\" 假设不成立\n- Table 1 N=8 是 single-seed 还是 averaged 未说明\n\n### Overall: 3.5/5 (Borderline Conference / Strong Findings), Confidence: 4/5",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "2"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-15T02:49:57.010658+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1616
}
```

</details>

---


### Assistant

_source line 225 · 2026-05-15T02:49:59.963408+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 226 · 2026-05-15T02:50:02.912676+00:00_

[Reviewer 2 审稿结果]:
Round 2 审稿完成，已发送给 Review Director。

核心结论：

- **Overall 3.5**（Borderline Conference），Confidence 4/5
- **2个 Must-Fix**：(1) ρ=0.38仍缺乏与semantic entropy/P(True)等方法的跨方法数值对比；(2) selection实验仅SciERC一个数据集，CoNLL/WNUT-17未报告且未解释原因
- **4个 Should-Fix**：constrained decoding confound、abstract RE措辞误导、WNUT-17贡献有限、EM majority-vote selection缺失
- **遗留Issues**：11项中9项resolved，R1-W3和R0-C4 partially open
- **引用验证**：49条bib entry全部cited，0 orphan/0 missing，45条verified，2条API not_found（hobelsberger2025, lightman2024，为API覆盖问题），2条mismatch为false positive

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

_source line 227 · 2026-05-15T02:50:07.670798+00:00_

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


## Round 19

## Round 19

2 recorded events


### User

_source line 228 · 2026-05-15T02:51:05.223236+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 对 Reviewer 2 Round 2 审稿意见

---

### R2-N1: ρ=0.38 缺乏跨方法数值对比

**[AGREE]** R2-N1: 同意需要 contextualization，但对 "critical" 级别保留意见。

ρ=0.38 的绝对水平确实缺乏 external anchor。论文 §2 (Related Work) 引用了 semantic entropy (Kuhn 2023)、P(True) (Kadavath 2022)、CoCoA (Vashurin 2025) 等方法但未给出任何数值对比，读者无法判断 0.38 在 confidence estimation 领域中的相对位置。R2 的建议（加 footnote contextualize）是合理且 low-cost 的改进。

但我认为这是 **should-fix 而非 must-fix**，原因：(1) structured IE 与 discrete-answer QA 的 output space 根本不同，direct numerical comparison 有误导风险——ρ 在 set-valued output 上的天花板可能远低于 single-token tasks；(2) 论文已从两个维度 contextualize（14% variance explained + AUROC=0.749 的 binary discrimination），不算完全缺失 context。建议作者加一段说明 cross-task comparison 的困难性，同时给出可引用的外部数值（如 semantic entropy QA AUROC 范围）作为 calibration point。

---

### R2-N2: Selection 实验仅在 SciERC 上进行

**[AGREE]** R2-N2: 完全同意，与我的 R1-N1 一致。

这是本轮审稿最重要的 issue。Table 3 (Section 5.3) 的 selection 分析仅覆盖 SciERC/Qwen，但 correlation-selection gap 被 framed 为 generative IE 中的 "fundamental disconnect"（Abstract, Introduction Contribution #2, Conclusion）。Quality estimation 有 3 datasets × 2 models，selection 仅 1 × 1，逻辑链存在明显断裂。

R2 进一步指出 CoNLL headroom 可能极小、WNUT-17 样本质量低——这些 reasoning 即使结论是 "gap 不存在 / headroom 为零"，也是有信息量的 insight（说明 gap 可能是 hard-task specific）。我在自己的 Q2 中也提了同样的问题。两位 reviewer 独立指出同一问题，should strengthen the signal to authors。

---

### R2-W1: Constrained decoding 作为全局 confound

**[AGREE]** R2-W1: 同意 constrained decoding 的影响应扩大讨论范围。

论文 Discussion §5 "Why logprob fails" 段落提到 "Constrained decoding enforces schema compliance at the token level, which may compress per-sample diversity"，但仅在 logprob context 下讨论。R2 正确指出：如果 constrained decoding 压缩 per-sample diversity，这影响的不仅是 logprob，还包括所有 signal 的 selection 表现——因为 consensus-proximity selection（SJ/Voting 的 selection 策略，Section 3.3）也依赖 per-sample 差异来区分候选。

论文 Limitations section 确实未将 constrained decoding 列为 key confound（当前 Limitations 讨论：dataset coverage、model scale、unsupervised-only signals、N range、SJ-FK gap）。建议：(1) Limitations 增加 constrained decoding 条目，或 (2) 报告 per-sample F1 variance（Table 3 已有 random baseline 0.608 vs greedy 0.644，间接说明 variance 存在，但 explicit variance 数据更有力）。

---

### R2-W2: Abstract "across three datasets" 可能误导 RE 覆盖度

**[AGREE]** R2-W2: 同意 Abstract 措辞需修正。

Abstract 第 3 句："across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17)"——自然读法是 NER + RE 均在三个数据集上评估，但实际 RE 仅在 SciERC 上进行（CoNLL 和 WNUT-17 仅有 NER）。虽然 Introduction Contribution #1 和 Discussion 已正确 hedge（"our RE conclusions are based on a single benchmark"），但 Abstract 作为 first impression 应自洽。R2 的建议 "across NER (three datasets) and RE (SciERC)" 或类似表述是简单且准确的 fix。

---

### R2-W3: WNUT-17 贡献定位

**[AGREE]** R2-W3: 同意，且认为问题比 R2 描述的更严重。

R2 建议将 WNUT-17 明确定位为 "capability boundary probe" 而非同等地位的 evaluation benchmark，这是合理的。但我在 R1-N2 中指出了一个更基本的问题：**全文仅报告 SJ 一个信号在 WNUT-17 上的 ρ（0.082, p=0.106），其他四个信号的 WNUT-17 结果完全缺失**。"All signals converge when model capability is insufficient" 这一 claim 用单个不显著的数据点支撑，逻辑上不成立。即使降级为 "probe"，也需要报告全部 5 signals 的数据才能支持 "all signals break down" 的结论。

---

### R2-W4: EM 用于 selection 的缺失

**[REBUT]** R2-W4: 部分反驳——majority-vote selection 在 structured IE 中确实 ill-defined，但论文可以更好地解释。

R2 指出当 EM<1 时，majority output 可被识别，picking majority output 就是 standard self-consistency voting。这在 discrete-answer tasks 中成立（majority vote = 最频繁的答案），但在 structured IE 中有根本性困难：

1. **Exact match 在 entity sets 间极为稀少**。Section 5.1 的 conditional filtering 分析暗示大量 instances 的 EM<1 不是因为有清晰的 majority + minority 分组，而是因为 N 个 outputs 各不相同（partial overlap），此时 "majority" 可能只有 1-2 个完全相同的 sample，其余都是不同的 partial extractions。
2. **论文 Section 3.3 已提供替代方案**：consensus-proximity selection（选择与 consensus 最接近的 sample）本质上是 soft majority vote，已在 Table 3 中报告（SJ selection）。

但 R2 的批评有合理之处：Table 3 caption 说 "EM produces binary agreement without sample ranking" 过于简略——当 EM<1 时，确实有一个 plurality output，论文应解释为什么不使用它。建议：在 Section 3.3 或 Table 3 caption 加 1-2 句说明 exact-match plurality 在 structured output 中的退化问题（plurality 通常仅 1-2 samples，selection 等同于 near-random）。

---

### R2-M1: Ethics Statement 缺失

**[REBUT]** R2-M1: ARR submission 通过 Responsible NLP Checklist 履行 ethics review，不要求单独的 Ethics Statement section。

ACL ARR CFP 要求作者提交 Responsible NLP Research Checklist（作为 submission 的一部分），但不要求在正文中包含单独的 "Ethics Statement" section。部分 *ACL venues（如 NAACL 2024）曾要求 separate section，但 ARR 2025-2026 的 Author Guidelines 明确通过 checklist 完成此功能。除非作者的工作涉及 human subjects、sensitive data 等需要 extended discussion 的伦理问题（本文不涉及——全部使用公开 benchmark、无 human annotation），缺少 separate Ethics Statement section 不构成格式违规。

---

### 总结

| R2 Issue | 我的回应 | 与我自己 issues 的关系 |
|----------|---------|----------------------|
| R2-N1 (ρ=0.38 无 external context) | [AGREE] 但建议降级为 should-fix | 新视角，我未提出 |
| R2-N2 (selection 仅 SciERC) | [AGREE] 完全同意 | = R1-N1 |
| R2-W1 (constrained decoding 全局 confound) | [AGREE] 应扩大讨论范围 | 补充我的 minor 观察 |
| R2-W2 (Abstract RE 措辞) | [AGREE] 简单 fix | 我未明确提出 |
| R2-W3 (WNUT-17 定位) | [AGREE] 但问题更严重 | ⊂ R1-N2（我的更强） |
| R2-W4 (EM majority-vote selection) | [REBUT] structured IE 中 ill-defined | 新视角 |
| R2-M1 (Ethics Statement) | [REBUT] ARR 通过 checklist 完成 | 格式判断 |

**两位 reviewer 的共识 critical issues**: (1) selection 证据面过窄（R1-N1 = R2-N2），(2) WNUT-17 数据不足（R1-N2 ⊃ R2-W3）。这两个问题如果得到补充，论文从 3.5 提升到 4.0 是可期的。

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

_source line 229 · 2026-05-15T02:51:10.744515+00:00_

Reviewer 1 交叉回应已收到，等待 Reviewer 2 交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 230 · 2026-05-15T02:51:13.527040+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：R2 的 7 个 issues 中我 **AGREE 5 个、REBUT 2 个**。

两位 reviewer 独立一致的 critical issues：
1. **Selection 证据面过窄**（R1-N1 = R2-N2）——correlation-selection gap 仅 SciERC/Qwen 验证
2. **WNUT-17 数据不足**（R1-N2 ⊃ R2-W3）——我的版本更强，指出全部 5 signals 结果缺失

反驳了两点：
- **R2-W4**（EM majority-vote selection）：structured IE 中 exact-match plurality 退化严重，consensus-proximity（SJ selection）已是 soft 版本的 majority vote
- **R2-M1**（Ethics Statement）：ARR 通过 Responsible NLP Checklist 完成，不要求 separate section

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

_source line 231 · 2026-05-15T02:51:18.493158+00:00_

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


## Round 21

## Round 21

8 recorded events


### User

_source line 232 · 2026-05-15T02:51:33.913670+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 2 意见的逐条回应

### Must-Fix

**[AGREE] R1-N1: Selection 仅 SciERC/Qwen**
同意，与我的 N2 本质相同。补充：Abstract "either task" 的 evidence base 实际是 1 dataset × 1 model × 2 tasks，比 R1 指出的更窄。

**[AGREE] R1-N2: WNUT-17 "all signals break down" 仅有 SJ 单一数据点**
同意。与我的 W3 互补。R1 的 formulation 更精准（需 5 signals 完整 table），我补充 conditional ρ（non-zero F1 subset）也应报告以排除 floor effect。

### Should-Fix

**[AGREE] R1-W1: N=8 ρ 无 CIs** — signal ordering 中多处 Δ=0.003-0.01，在 N=16 σ≈0.006-0.008 参照下可能 within noise。
**[AGREE] R1-W2: SJ matching 无 threshold** — 同意并提升严重性，Eq.(4) 分母用 max 而非 union 也属非标准，需解释。
**[AGREE] R1-W3: RE selection 无统计检验** — RE oracle headroom 18.1pp 更大，selection failure 更需 p-value。
**[REBUT] R1-W4: LLaMA SciERC N=8 数据不全** — Table 1 CoNLL 有完整 cross-model 覆盖（5 signals, Δρ≤0.005），Appendix N=16 有 LLaMA SciERC 数据。但同意 Table 1 SciERC 列应标注 "Qwen-only"。
**[AGREE] R1-W5: n=529 vs n=551** — 差额 22 instances 未解释，需 stated。

### Minor — 全部同意，其中 Eq.(4) 非标准 Jaccard 应提升为 Should-Fix。

### 两份审稿的共同核心
**Selection claim evidence base 过窄**是两份审稿的共同 #1 问题（R1-N1 = R2-N2）。次要共识：WNUT-17 evidence 不足（R1-N2 ≈ R2-W3）、N=8 缺 uncertainty（R1-W1）。

R1 未覆盖但我认为重要：(1) ρ=0.38 跨方法 contextualization（R2-N1），(2) constrained decoding 全局 confound（R2-W1），(3) EM majority-vote selection 缺失（R2-W4）。

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

_source line 233 · 2026-05-15T02:52:05.800725+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
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
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 234 · 2026-05-15T02:52:05.901683+00:00_



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

_source line 235 · 2026-05-15T02:54:37.458603+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues — updated through Round 2\n  # ============================================================\n\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B），严重限制普适性主张\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性。建议增加 >30B 或 <3B 模型。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 列为 critical (C4)，R2 降为 should-fix。Discussion 仍用 model-agnostic 但 Limitations 承认局限，构成内部矛盾。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"全文已替换为 consistent across tested model families，Limitations 承认局限。R1/R2 均判定 resolved。\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞已修正，不再 overclaim\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Round 0 遗漏部分修复。新遗漏：Optimal SC, Difficulty-Adaptive SC, conformal prediction。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Related Work 已补充 Optimal SC (feng2025optimal)、Difficulty-Adaptive SC (wang2025make)、conformal prediction、Generative Self-Aggregation (li2025llms)、latent SC (oh2025latentsc)、ranked voting (wang2025rankedvoting)、ReASC (kim2026reasc)。R1/R2 均判定 resolved。\"\n    action_items:\n      - round: 1\n        action: \"补充遗漏引用\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Related Work 覆盖全面，49 条 bib 全部 cited\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"SciERC RE 仅 6 relation types, n=397。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 维持 critical，R2 降为 high-warning。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Introduction/Discussion/Conclusion/Appendix 四处 hedge（our RE conclusions rest on SciERC alone and warrant further validation）。R1/R2 均判定 resolved。\"\n    action_items:\n      - round: 1\n        action: \"降级措辞\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞已充分 hedge\"\n    resolution_round: 2\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限——评估指标到 confidence 的自然迁移\"\n    category: method\n    severity: warning\n    status: partially_resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少与 edit distance、embedding similarity 等 kernel 的消融。\"\n      - round: 1\n        reviewers: [2]\n        note: \"演变为 R1-N4: Nedellec 增量贡献论证不足。\"\n      - round: 2\n        reviewers: [2]\n        note: \"R2 判定 partially resolved——框架已转向 comparison study，但 methodological novelty 仍然有限。R1 判定 resolved（定位明确）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams。\"\n    action_items: []\n    resolution: \"论文已包含 5 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析将 8-16× 推理开销描述为 negligible\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"系统性误导。\"\n    action_items: []\n    resolution: \"Round 1 未再被提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"SJ+LP 互补性已证明但未尝试组合。\"\n    action_items: []\n    resolution: \"Round 1 未再被提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"核心比较缺 CI。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"演变为 R1-N1。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Selection bootstrap 完整（n=529, B=10K, paired, CI, Cohen's d, sign test）。QE N=8 仍为 point estimates——新 issue R2-W1 跟踪。\"\n    action_items: []\n    resolution: \"Selection 统计规范已完整；QE uncertainty 由 R2-W1 跟踪\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling 声明与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际 Δ=-0.080。\"\n    action_items: []\n    resolution: \"Round 1 Reviewer 未再发现此矛盾\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues — updated through Round 2\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节严重不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 核心结论统计基础无法验证。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 5.3 补齐：n=529, B=10K, instance-level paired, percentile 95% CIs [-3.0, +4.2]pp, Cohen's d=0.038, sign test 61W/70L, seeds 含义明确。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"Bootstrap 规范完整\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Correlation-selection gap 解释力不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 signals 定义性 + logprob 失败未分析。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Discussion 清晰区分 instance-level vs per-sample limitation；logprob 失败归因于 constrained decoding grammar compliance + 75% ties；LOO-SJ circularity 验证（Δρ=-0.014）。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"解释力充分，instance-level vs per-sample 区分清晰\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 探索严重不足——仅 logprob 1 个\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"per-sample 维度单薄。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 3.3 明确 consensus-proximity = LOO-SJ selection；Appendix 验证 circularity negligible。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"per-sample selection 策略已明确说明\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec et al. (2026) 增量贡献论证不足 + 引用作者错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"bib 第一作者 Yao 全文引用为 Nédellec。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"bib 已修正（author = Yao, Xinzhi...），三点差异化论证（structural matching / selection analysis / difficulty gradient）具体且有说服力。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"引用修正，增量贡献论证充分\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"Soft Jaccard 形式化有歧义\"\n    category: method\n    severity: warning\n    status: partially_resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Eq.(4) g_i/g_j 未定义，sim 公式缺失，Hungarian 阈值未说明。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"sim = token-level IoU ✓, g_i/g_j = per-type extraction counts ✓。但 Hungarian threshold 仍未指定（R1-W2），Eq.(4) 分母非标准 Jaccard variant 未解释（R2 交叉回应提升为 should-fix）。\"\n    action_items:\n      - round: 2\n        action: \"明确 Hungarian matching threshold（或说明无 threshold 的影响）；解释分母 max vs union 的设计选择\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Entity voting & SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"高度相关则削弱两类 structural signal 独立验证论证。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"报告 inter-signal ρ=0.659 (NER), 0.605 (RE) + differential behavior across difficulty。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"冗余度已量化，差异性已论证\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺乏 contextualization\"\n    category: framing\n    severity: warning\n    status: partially_resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"缺乏与 semantic entropy/P(True) 等方法的 ρ 对比。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"intra-study context 已补（14% variance explained + AUROC=0.749）。但 cross-method numerical context 仍缺——semantic entropy QA AUROC 0.75-0.85、P(True) 等无数值对比。R2 列为 critical，R1 同意但建议降为 should-fix（structured IE vs QA output space 不同，direct comparison 有误导风险）。\"\n    action_items:\n      - round: 2\n        action: \"§5 或 §4.2 加 footnote：引用 semantic entropy/P(True) 典型 AUROC 值，明确 structured IE vs discrete-answer tasks 直接对比的困难性\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度敏感性数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"T=0.7 unavailable。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 5.4 + Limitations 明确 acknowledge。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"已充分 acknowledge limitation\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 'establishing capability boundary' 统计措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject null ≠ accept null。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已改为 suggesting a capability boundary。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"措辞已收窄\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA-3.1-8B-Instruct 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA 是否经过 fine-tuning 未说明。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 4.1 明确：两模型 identical LoRA (rank=32, α=64), 5 epochs, LLaMA Factory。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"训练对称性已明确说明\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码对 sampling diversity 的影响未讨论\"\n    category: method\n    severity: warning\n    status: partially_resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"约束解码可能人为压低 per-sample variance。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Discussion 已在 logprob 段落讨论 constrained decoding 压缩 diversity + random baseline gap 3.6pp 说明 variance 存在。但 R2 指出影响不限于 logprob（全局 confound），R1 交叉回应同意。Limitations 未列出。\"\n    action_items:\n      - round: 2\n        action: \"Limitations section 明确列出 constrained decoding 作为 key confound（影响所有 signal 的 selection），或补充 per-sample F1 variance 数据\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W8\"\n    summary: \"'first systematic evaluation' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已收窄为 first multi-family comparison...for both QE and selection in generative IE。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"scope 已限定\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用：Optimal SC、Difficulty-Adaptive SC\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC 和 Difficulty-Adaptive SC 应引用。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Related Work 已补充。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"引用已补充\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 机制分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文阐述。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 5.1 主文 + Discussion 均阐述 EM=1 压缩效应。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"EM=1 效应已在主文和讨论中阐述\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 提及但无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Limitations 提及但无结果。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已删除。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"已删除无数据支撑的提及\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"Introduction +18pp on GSM8K 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"与本文 8B 模型规模差异大。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已补 (PaLM-540B; Wang et al., 2023)。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"已注明模型\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告是否在 CI 内\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Δ=0.005 几乎确定不显著但应报告。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 5.1 已补注 Δ=0.005, within 3-seed σ≈0.007。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"已报告在 CI 内\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 new issues\n  # ============================================================\n\n  - id: \"R2-N1\"\n    summary: \"Selection 证据面过窄——核心贡献仅 1 dataset × 1 model 验证\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-N1 = R2-N2，两位 Reviewer 独立一致。Table 3 selection 分析仅 SciERC/Qwen，但 correlation-selection gap 被 framed 为 fundamental disconnect。QE 有 3 datasets × 2 models，selection 仅 1×1，逻辑链断裂。CoNLL/LLaMA SciERC/WNUT-17 selection 均未报告。\"\n    action_items:\n      - round: 2\n        action: \"至少补 LLaMA SciERC selection 结果验证 cross-model；CoNLL selection 放 Appendix（即使 headroom 小也有信息量）；如 WNUT-17 selection 不可行需说明 oracle-greedy gap\"\n        assigned_to: \"Paper Agent / Experiment Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"WNUT-17 capability boundary claim 缺乏系统数据\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-N2 ⊃ R2-W3。全文仅报告 SJ 一个信号 ρ=0.082 (p=0.106)，其他 4 个信号完全缺失。用单个不显著数据点支撑 all signals break down 逻辑不成立。Contribution #3 列出 WNUT-17 作为 task-complexity boundary conditions 证据。\"\n    action_items:\n      - round: 2\n        action: \"Appendix 增加 WNUT-17 完整 table（5 signals × ρ + AUROC）；如全部 collapse 则为更强证据；补 conditional ρ（non-zero F1 subset）排除 floor effect\"\n        assigned_to: \"Paper Agent / Experiment Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"N=8 QE ρ 缺乏 uncertainty quantification\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W1，R2 交叉回应同意。Table 1 N=8 为 point estimates without CIs，但多处 signal ordering Δ=0.003-0.01 可能 within noise（参照 N=16 σ≈0.006-0.008）。正面 QE 结论反而缺乏统计支撑，与 selection 的 thorough bootstrap 不一致。\"\n    action_items:\n      - round: 2\n        action: \"对 N=8 主要 ρ 值报告 bootstrap CIs，或 Appendix 补 3-seed runs\"\n        assigned_to: \"Paper Agent / Experiment Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"SJ Hungarian matching 无 threshold 规范 + Eq.(4) 非标准分母\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W2 + R2 交叉回应提升。Hungarian 是否有 minimum similarity threshold 未说明；Eq.(4) 分母用 max(|g_i|,|g_j|) 而非标准 |A∪B|，属非标准 Jaccard variant 未解释。\"\n    action_items:\n      - round: 2\n        action: \"明确 threshold（或说明无 threshold 时 sim≈0 matched pairs 比例）；解释 max vs union 设计选择\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W3，R2 交叉回应同意。NER selection 有完整 bootstrap，RE 仅叙述性报告 no signal exceeds greedy 但无 p-value/CI。RE oracle headroom 18.1pp 更大，selection failure 更需统计支撑。\"\n    action_items:\n      - round: 2\n        action: \"补充 RE selection bootstrap p-value 和 CI\"\n        assigned_to: \"Paper Agent / Experiment Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"Abstract 'across NER and RE on three datasets' 措辞误导\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2-W2，R1 交叉回应同意。RE 仅在 SciERC 评估，但 Abstract 暗示 NER+RE 均在三数据集上进行。\"\n    action_items:\n      - round: 2\n        action: \"改为 across NER (three datasets) and RE (SciERC) 或类似准确表述\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"n=529 vs SciERC n=551 discrepancy 未解释\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W5，R2 交叉回应同意。Bootstrap 用 n=529 但 SciERC test set 有 551 instances，22 instances 被 drop 原因未交代。\"\n    action_items:\n      - round: 2\n        action: \"说明 n=529 的 filtering criteria\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-D1\"\n    summary: \"EM majority-vote selection 缺失解释（Reviewer 分歧）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 部分反驳。R2：EM<1 时 majority output 可识别，应报告 majority-vote selection 或解释为何不用。R1：structured IE 中 exact-match plurality 退化严重（通常仅 1-2 samples），consensus-proximity (SJ selection) 已是 soft majority vote。分歧未完全收敛。\"\n    action_items:\n      - round: 2\n        action: \"Section 3.3 或 Table 3 caption 加 1-2 句解释 exact-match plurality 在 structured output 中的退化问题\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues — updated through Round 2\n  # ============================================================\n\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B），严重限制普适性主张\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性。建议增加 >30B 或 <3B 模型。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 列为 critical (C4)，R2 降为 should-fix。Discussion 仍用 model-agnostic 但 Limitations 承认局限，构成内部矛盾。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"全文已替换为 consistent across tested model families，Limitations 承认局限。R1/R2 均判定 resolved。\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞已修正，不再 overclaim\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Round 0 遗漏部分修复。新遗漏：Optimal SC, Difficulty-Adaptive SC, conformal prediction。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Related Work 已补充 Optimal SC (feng2025optimal)、Difficulty-Adaptive SC (wang2025make)、conformal prediction、Generative Self-Aggregation (li2025llms)、latent SC (oh2025latentsc)、ranked voting (wang2025rankedvoting)、ReASC (kim2026reasc)。R1/R2 均判定 resolved。\"\n    action_items:\n      - round: 1\n        action: \"补充遗漏引用\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Related Work 覆盖全面，49 条 bib 全部 cited\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"SciERC RE 仅 6 relation types, n=397。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 维持 critical，R2 降为 high-warning。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Introduction/Discussion/Conclusion/Appendix 四处 hedge（our RE conclusions rest on SciERC alone and warrant further validation）。R1/R2 均判定 resolved。\"\n    action_items:\n      - round: 1\n        action: \"降级措辞\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞已充分 hedge\"\n    resolution_round: 2\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限——评估指标到 confidence 的自然迁移\"\n    category: method\n    severity: warning\n    status: partially_resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少与 edit distance、embedding similarity 等 kernel 的消融。\"\n      - round: 1\n        reviewers: [2]\n        note: \"演变为 R1-N4: Nedellec 增量贡献论证不足。\"\n      - round: 2\n        reviewers: [2]\n        note: \"R2 判定 partially resolved——框架已转向 comparison study，但 methodological novelty 仍然有限。R1 判定 resolved（定位明确）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams。\"\n    action_items: []\n    resolution: \"论文已包含 5 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析将 8-16× 推理开销描述为 negligible\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"系统性误导。\"\n    action_items: []\n    resolution: \"Round 1 未再被提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"SJ+LP 互补性已证明但未尝试组合。\"\n    action_items: []\n    resolution: \"Round 1 未再被提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"核心比较缺 CI。\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"演变为 R1-N1。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Selection bootstrap 完整（n=529, B=10K, paired, CI, Cohen's d, sign test）。QE N=8 仍为 point estimates——新 issue R2-W1 跟踪。\"\n    action_items: []\n    resolution: \"Selection 统计规范已完整；QE uncertainty 由 R2-W1 跟踪\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling 声明与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际 Δ=-0.080。\"\n    action_items: []\n    resolution: \"Round 1 Reviewer 未再发现此矛盾\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues — updated through Round 2\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节严重不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 核心结论统计基础无法验证。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 5.3 补齐：n=529, B=10K, instance-level paired, percentile 95% CIs [-3.0, +4.2]pp, Cohen's d=0.038, sign test 61W/70L, seeds 含义明确。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"Bootstrap 规范完整\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Correlation-selection gap 解释力不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 signals 定义性 + logprob 失败未分析。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Discussion 清晰区分 instance-level vs per-sample limitation；logprob 失败归因于 constrained decoding grammar compliance + 75% ties；LOO-SJ circularity 验证（Δρ=-0.014）。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"解释力充分，instance-level vs per-sample 区分清晰\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 探索严重不足——仅 logprob 1 个\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"per-sample 维度单薄。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 3.3 明确 consensus-proximity = LOO-SJ selection；Appendix 验证 circularity negligible。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"per-sample selection 策略已明确说明\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec et al. (2026) 增量贡献论证不足 + 引用作者错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"bib 第一作者 Yao 全文引用为 Nédellec。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"bib 已修正（author = Yao, Xinzhi...），三点差异化论证（structural matching / selection analysis / difficulty gradient）具体且有说服力。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"引用修正，增量贡献论证充分\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"Soft Jaccard 形式化有歧义\"\n    category: method\n    severity: warning\n    status: partially_resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Eq.(4) g_i/g_j 未定义，sim 公式缺失，Hungarian 阈值未说明。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"sim = token-level IoU ✓, g_i/g_j = per-type extraction counts ✓。但 Hungarian threshold 仍未指定（R1-W2），Eq.(4) 分母非标准 Jaccard variant 未解释（R2 交叉回应提升为 should-fix）。\"\n    action_items:\n      - round: 2\n        action: \"明确 Hungarian matching threshold（或说明无 threshold 的影响）；解释分母 max vs union 的设计选择\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Entity voting & SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"高度相关则削弱两类 structural signal 独立验证论证。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"报告 inter-signal ρ=0.659 (NER), 0.605 (RE) + differential behavior across difficulty。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"冗余度已量化，差异性已论证\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺乏 contextualization\"\n    category: framing\n    severity: warning\n    status: partially_resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"缺乏与 semantic entropy/P(True) 等方法的 ρ 对比。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"intra-study context 已补（14% variance explained + AUROC=0.749）。但 cross-method numerical context 仍缺——semantic entropy QA AUROC 0.75-0.85、P(True) 等无数值对比。R2 列为 critical，R1 同意但建议降为 should-fix（structured IE vs QA output space 不同，direct comparison 有误导风险）。\"\n    action_items:\n      - round: 2\n        action: \"§5 或 §4.2 加 footnote：引用 semantic entropy/P(True) 典型 AUROC 值，明确 structured IE vs discrete-answer tasks 直接对比的困难性\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度敏感性数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"T=0.7 unavailable。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 5.4 + Limitations 明确 acknowledge。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"已充分 acknowledge limitation\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 'establishing capability boundary' 统计措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject null ≠ accept null。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已改为 suggesting a capability boundary。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"措辞已收窄\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA-3.1-8B-Instruct 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA 是否经过 fine-tuning 未说明。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 4.1 明确：两模型 identical LoRA (rank=32, α=64), 5 epochs, LLaMA Factory。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"训练对称性已明确说明\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码对 sampling diversity 的影响未讨论\"\n    category: method\n    severity: warning\n    status: partially_resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"约束解码可能人为压低 per-sample variance。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Discussion 已在 logprob 段落讨论 constrained decoding 压缩 diversity + random baseline gap 3.6pp 说明 variance 存在。但 R2 指出影响不限于 logprob（全局 confound），R1 交叉回应同意。Limitations 未列出。\"\n    action_items:\n      - round: 2\n        action: \"Limitations section 明确列出 constrained decoding 作为 key confound（影响所有 signal 的 selection），或补充 per-sample F1 variance 数据\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W8\"\n    summary: \"'first systematic evaluation' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已收窄为 first multi-family comparison...for both QE and selection in generative IE。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"scope 已限定\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用：Optimal SC、Difficulty-Adaptive SC\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC 和 Difficulty-Adaptive SC 应引用。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Related Work 已补充。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"引用已补充\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 机制分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文阐述。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 5.1 主文 + Discussion 均阐述 EM=1 压缩效应。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"EM=1 效应已在主文和讨论中阐述\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 提及但无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Limitations 提及但无结果。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已删除。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"已删除无数据支撑的提及\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"Introduction +18pp on GSM8K 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"与本文 8B 模型规模差异大。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已补 (PaLM-540B; Wang et al., 2023)。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"已注明模型\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告是否在 CI 内\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Δ=0.005 几乎确定不显著但应报告。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Section 5.1 已补注 Δ=0.005, within 3-seed σ≈0.007。R1/R2 均判定 resolved。\"\n    action_items: []\n    resolution: \"已报告在 CI 内\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 new issues\n  # ============================================================\n\n  - id: \"R2-N1\"\n    summary: \"Selection 证据面过窄——核心贡献仅 1 dataset × 1 model 验证\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-N1 = R2-N2，两位 Reviewer 独立一致。Table 3 selection 分析仅 SciERC/Qwen，但 correlation-selection gap 被 framed 为 fundamental disconnect。QE 有 3 datasets × 2 models，selection 仅 1×1，逻辑链断裂。CoNLL/LLaMA SciERC/WNUT-17 selection 均未报告。\"\n    action_items:\n      - round: 2\n        action: \"至少补 LLaMA SciERC selection 结果验证 cross-model；CoNLL selection 放 Appendix（即使 headroom 小也有信息量）；如 WNUT-17 selection 不可行需说明 oracle-greedy gap\"\n        assigned_to: \"Paper Agent / Experiment Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"WNUT-17 capability boundary claim 缺乏系统数据\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-N2 ⊃ R2-W3。全文仅报告 SJ 一个信号 ρ=0.082 (p=0.106)，其他 4 个信号完全缺失。用单个不显著数据点支撑 all signals break down 逻辑不成立。Contribution #3 列出 WNUT-17 作为 task-complexity boundary conditions 证据。\"\n    action_items:\n      - round: 2\n        action: \"Appendix 增加 WNUT-17 完整 table（5 signals × ρ + AUROC）；如全部 collapse 则为更强证据；补 conditional ρ（non-zero F1 subset）排除 floor effect\"\n        assigned_to: \"Paper Agent / Experiment Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"N=8 QE ρ 缺乏 uncertainty quantification\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W1，R2 交叉回应同意。Table 1 N=8 为 point estimates without CIs，但多处 signal ordering Δ=0.003-0.01 可能 within noise（参照 N=16 σ≈0.006-0.008）。正面 QE 结论反而缺乏统计支撑，与 selection 的 thorough bootstrap 不一致。\"\n    action_items:\n      - round: 2\n        action: \"对 N=8 主要 ρ 值报告 bootstrap CIs，或 Appendix 补 3-seed runs\"\n        assigned_to: \"Paper Agent / Experiment Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"SJ Hungarian matching 无 threshold 规范 + Eq.(4) 非标准分母\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W2 + R2 交叉回应提升。Hungarian 是否有 minimum similarity threshold 未说明；Eq.(4) 分母用 max(|g_i|,|g_j|) 而非标准 |A∪B|，属非标准 Jaccard variant 未解释。\"\n    action_items:\n      - round: 2\n        action: \"明确 threshold（或说明无 threshold 时 sim≈0 matched pairs 比例）；解释 max vs union 设计选择\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W3，R2 交叉回应同意。NER selection 有完整 bootstrap，RE 仅叙述性报告 no signal exceeds greedy 但无 p-value/CI。RE oracle headroom 18.1pp 更大，selection failure 更需统计支撑。\"\n    action_items:\n      - round: 2\n        action: \"补充 RE selection bootstrap p-value 和 CI\"\n        assigned_to: \"Paper Agent / Experiment Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"Abstract 'across NER and RE on three datasets' 措辞误导\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2-W2，R1 交叉回应同意。RE 仅在 SciERC 评估，但 Abstract 暗示 NER+RE 均在三数据集上进行。\"\n    action_items:\n      - round: 2\n        action: \"改为 across NER (three datasets) and RE (SciERC) 或类似准确表述\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"n=529 vs SciERC n=551 discrepancy 未解释\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1-W5，R2 交叉回应同意。Bootstrap 用 n=529 但 SciERC test set 有 551 instances，22 instances 被 drop 原因未交代。\"\n    action_items:\n      - round: 2\n        action: \"说明 n=529 的 filtering criteria\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-D1\"\n    summary: \"EM majority-vote selection 缺失解释（Reviewer 分歧）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 部分反驳。R2：EM<1 时 majority output 可识别，应报告 majority-vote selection 或解释为何不用。R1：structured IE 中 exact-match plurality 退化严重（通常仅 1-2 samples），consensus-proximity (SJ selection) 已是 soft majority vote。分歧未完全收敛。\"\n    action_items:\n      - round: 2\n        action: \"Section 3.3 或 Table 3 caption 加 1-2 句解释 exact-match plurality 在 structured output 中的退化问题\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-15T02:54:37.660994+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 20223}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 237 · 2026-05-15T02:56:52.662696+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 2 审稿报告 — struct_self_consist_ie\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性 + 格式）\n**交叉分享**: 已完成，两位 Reviewer 均提交逐条 [AGREE]/[REBUT] 回应\n\n---\n\n## Summary\n\n本文系统比较了三个族群（structural/surface/model-internal）的五种 confidence signal 在 generative IE（NER + RE）中的 quality estimation 与 sample selection 表现。核心发现是 \"correlation-selection gap\"：instance-level consistency signals 是有效的 quality estimators（entity voting ρ=0.38, exact match AUROC=0.75），但无法可靠超越 greedy decoding 进行 best-of-N selection（p>0.39, bootstrap），尽管存在 13-18pp 的 oracle headroom。附带发现 signal ranking 随 task difficulty 变化（EM 领先 easy tasks，SJ/Voting 领先 hard tasks，WNUT-17 全部 collapse）。\n\n---\n\n## Strengths\n\n1. **概念贡献清晰且有框架性价值**：quality estimation（ranking instances by expected performance）vs sample selection（choosing best output among N candidates）的解耦（§3.1 per-sample vs instance-level signal formulation）对 generative IE 社区有指导意义，是与 Nédellec et al. (2026) 的关键差异化。\n\n2. **Quality estimation 分析深度突出**：5 signals × 4 configurations (Table 1) + conditional filtering + capability stratification + per-relation diagnostic + ρ-AUROC dissociation 分析，超过多数同类 empirical study。\n\n3. **统计规范（selection）达到高标准**：Bootstrap resampling (B=10,000, n=529, instance-level paired), percentile 95% CIs, Cohen's d=0.038, sign test 61W/70L, 3-seed 含义明确——远超多数 NLP empirical papers。\n\n4. **诚实的 hedging**：RE single-dataset 限制在 Introduction/Discussion/Conclusion/Appendix 四处 acknowledge；logprob temperature gap 在正文 + Limitations 双重标注；claim 用 \"consistent across tested model families\" 而非 \"model-agnostic\"——Round 0-1 的 self-awareness 问题已有实质改善。\n\n5. **Related Work 覆盖全面**：§2 涵盖 self-consistency 变体（USC, CISC, ReASC, ranked voting, latent SC）、difficulty-adaptive 方法（Optimal SC, Difficulty-Adaptive SC）、generative self-aggregation、conformal prediction、semantic uncertainty 等。49 条 bib 全部 cited，0 orphan。\n\n6. **ρ-AUROC dissociation 是 actionable finding**：EM 在 ρ 排名低但 AUROC 领先（SciERC NER: ρ=0.295 rank #3, AUROC=0.749 rank #1），揭示 binary vs continuous signal properties 的 metric-dependent 行为，对 practitioners 在 quality-aware routing 中有直接实用价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. Selection 证据面过窄——核心贡献仅 1 dataset × 1 model 验证** [Reviewer 共识: unanimously critical]\n\n- **位置**: Table 3 (§5.3)；Abstract; Introduction Contribution #2; Conclusion\n- **问题**: Correlation-selection gap 是论文的 differentiator（与 Nédellec et al. 的关键区别），但 Table 3 的 selection 分析仅覆盖 SciERC/Qwen。Quality estimation 有 3 datasets × 2 models 的覆盖，selection 仅 1×1，逻辑链断裂。Abstract \"no signal reliably surpasses greedy decoding on either task\" 的 evidence base 实际是 1 dataset × 1 model × 2 tasks。CoNLL selection 未报告（即使 headroom 极小，negative result 本身有价值——说明 gap 可能是 hard-task specific）；LLaMA SciERC selection 未报告（cross-model 验证缺失）。\n- **Action**: (1) 补 LLaMA SciERC selection 结果验证 cross-model generalization；(2) CoNLL selection 放 Appendix（即使结论是 ceiling effect）；(3) 如 WNUT-17 selection 不可行，明确说明 oracle-greedy gap。\n\n**C2. WNUT-17 capability boundary claim 缺乏系统数据** [Reviewer 共识: unanimously critical]\n\n- **位置**: §5.1; Introduction Contribution #3\n- **问题**: Contribution #3 列出 \"task-complexity boundary conditions\"，WNUT-17 是关键证据。但全文仅报告 SJ 一个信号的 ρ=0.082 (p=0.106)——一个不显著的单信号结果。其他四个信号（Voting, EM, FK, Logprob）在 WNUT-17 的结果完全缺失。用单个不显著数据点支撑 \"all signals converge when model capability is insufficient\" 逻辑上不成立。如果 5 个信号全部 collapse，这反而是更强的证据。\n- **Action**: Appendix 增加 WNUT-17 完整 table（5 signals × ρ + AUROC）；补 conditional ρ（non-zero F1 subset）排除 floor effect。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. ρ=0.38 缺乏 cross-method 数值对比** [R2 列为 critical, R1 同意但建议降为 should-fix]\n\n- **位置**: §5.1, §6 Discussion\n- **问题**: 论文以 ρ=0.38 为核心正面结论（\"effective quality estimators\"），intra-study context 已有（14% variance explained + AUROC=0.749），但 cross-method numerical context 完全缺失。§2 引用 semantic entropy (Kuhn 2023)、P(True) (Kadavath 2022)、CoCoA (Vashurin 2025) 但未给出任何数值对比。R1 指出 structured IE 与 discrete-answer QA 的 output space 根本不同，direct comparison 有误导风险，因此降为 should-fix。\n- **Action**: §5 或 §4.2 加 footnote，引用可比方法的典型 AUROC 值，并明确 cross-task comparison 的困难性。\n\n**W2. N=8 QE ρ 缺乏 uncertainty quantification** [Reviewer 共识]\n\n- **位置**: Table 1 (§5.1)\n- **问题**: Table 1 N=8 行为 point estimates without CIs/standard errors。多处 signal ordering Δ=0.003-0.01（如 CoNLL LLaMA SJ-FK Δ=0.003），参照 N=16 σ≈0.006-0.008，可能 within noise。正面 QE 结论反而缺乏统计支撑，与 selection 的 thorough bootstrap 标准不一致。\n- **Action**: 对 N=8 主要 ρ 值报告 bootstrap CIs，或 Appendix 补 3-seed runs。\n\n**W3. SJ Hungarian matching 无 threshold + Eq.(4) 非标准分母** [Reviewer 共识, R2 交叉回应提升严重性]\n\n- **位置**: Eq.(4), §3.2\n- **问题**: sim = token-level IoU ✓, g_i/g_j 定义 ✓。但：(1) Hungarian 是否有 minimum similarity threshold？无 threshold 则完全不相关 span 也会 match，SJ numerator 非零；(2) 分母 max(|g_i|,|g_j|) 是非标准 Jaccard variant（标准为 |A∪B|），未解释设计选择。\n- **Action**: 明确 threshold 及 zero-overlap matched pairs 比例；一句话解释 max vs union 的设计理由。\n\n**W4. RE selection 无统计检验** [Reviewer 共识]\n\n- **位置**: Table 3, §5.3\n- **问题**: NER selection 有完整 bootstrap（p, CI, Cohen's d, sign test），RE 仅叙述性 \"no signal exceeds greedy\" 无任何统计量。RE oracle headroom 18.1pp 更大，selection failure 更需 p-value 支撑。\n- **Action**: 补 RE selection bootstrap p-value 和 CI。\n\n**W5. Constrained decoding 作为全局 confound 讨论不足** [R2 提出, R1 交叉同意]\n\n- **位置**: §6 Discussion; Limitations\n- **问题**: Discussion \"Why logprob fails\" 段提到 constrained decoding 压缩 per-sample diversity，但仅在 logprob context 下讨论。如果 constrained decoding 压缩 diversity，影响的不仅是 logprob，还包括 consensus-proximity selection（SJ/Voting）——因为后者也依赖 per-sample 差异区分候选。Limitations 未列此 confound。\n- **Action**: Limitations 增加 constrained decoding 条目；或补 per-sample F1 variance 数据证明 diversity 已足够。\n\n**W6. Abstract \"across NER and RE on three datasets\" 措辞误导** [Reviewer 共识]\n\n- **位置**: Abstract line 3\n- **问题**: RE 仅在 SciERC 评估，但 Abstract 自然读法暗示 NER+RE 均在三数据集上进行。\n- **Action**: 改为 \"across NER (three datasets) and RE (SciERC)\" 或类似准确表述。\n\n**W7. n=529 vs SciERC n=551 discrepancy** [Reviewer 共识]\n\n- **位置**: §5.3\n- **问题**: Bootstrap 用 n=529 但 SciERC test set 有 551 instances，22 instances 被 drop 原因未交代。\n- **Action**: 一句话说明 filtering criteria。\n\n---\n\n### Minor\n\n- Eq.(4) 分母 max 而非 union 需一句设计理由说明\n- FK adaptation：N 个来自同一模型的 stochastic samples 不是 Fleiss' κ 假设的 independent raters，brief acknowledgment 即可\n- Table 1 N=8 是 single-seed 还是 averaged 未说明\n- EM majority-vote selection 在 Table 3 中标 \"---\"，应加 1-2 句解释 exact-match plurality 在 structured IE 中的退化问题（Reviewer 分歧点，R1 反驳 R2，见下文 Divergence）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上独立达成完全一致：\n\n1. **Selection 证据面过窄是最关键问题**（R1-N1 = R2-N2, unanimously critical）：correlation-selection gap 仅 1 dataset × 1 model 验证，但 framed 为 \"fundamental disconnect\"\n2. **WNUT-17 系统数据缺失**（R1-N2 ⊃ R2-W3, unanimously critical）：5 signals 中仅报告 1 个不显著结果\n3. **N=8 QE 缺 uncertainty**（R1-W1, R2 交叉同意）\n4. **SJ threshold 未规范**（R1-W2, R2 交叉同意并提升严重性）\n5. **RE selection 缺统计检验**（R1-W3, R2 交叉同意）\n6. **Abstract RE 措辞需修正**（R2-W2, R1 交叉同意）\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **EM majority-vote selection (R2-W4)**：R2 认为 EM<1 时应实现 majority-vote selection；R1 反驳指出 structured IE 中 exact-match plurality 退化严重（通常仅 1-2 identical samples），consensus-proximity (SJ selection) 已是 soft majority vote。**Director 判断**：R1 的反驳有技术依据，降为 minor（加解释即可）。\n\n2. **LLaMA SciERC N=8 数据完整性 (R1-W4)**：R1 认为 Table 1 SciERC 列仅 Qwen、LLaMA 数据不全；R2 部分反驳指出 CoNLL 有完整 cross-model 覆盖，但同意 Table 1 应标注 \"Qwen-only\"。**Director 判断**：R2 的反驳合理——CoNLL cross-model 差异极小（Δ=0.005），SciERC 缺失不影响核心 claim。标注即可。\n\n3. **ρ=0.38 contextualization 严重性 (R2-N1 vs R1 交叉回应)**：R2 列为 critical，R1 同意需要但降为 should-fix（structured IE vs QA output space 不同，direct comparison 有误导风险）。**Director 判断**：采纳 R1 的降级——footnote 级修改，不构成 must-fix。\n\n---\n\n## Questions for Authors\n\n1. WNUT-17 上 Voting/EM/FK/Logprob 的 ρ 和 AUROC 分别是多少？\n2. CoNLL 的 best-of-N selection 结果（oracle-greedy gap 有多大）？\n3. SciERC bootstrap n=529 中 22 instances 被 drop 的 criteria？\n4. SJ Hungarian matching 是否有 minimum similarity threshold？无 threshold 时 sim≈0 matched pairs 占多少？\n5. Table 1 N=8 主要结果是 single-seed 还是 averaged？\n\n---\n\n## Missing References\n\n无重大遗漏。Round 1 指出的 Optimal SC、Difficulty-Adaptive SC、Generative Self-Aggregation、conformal prediction 等均已补充。49 条 bib 全部 cited，0 orphan，45 条 verified。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Round 0-1 遗留 Issue 修复状况\n\n**24 个历史 issues 状态汇总**：\n- ✅ **Resolved**: 19 个（R0-C1, R0-C2, R0-C3, R0-C5, R0-C6, R0-W1, R0-W4, R0-RR-D1, R1-N1, R1-N2, R1-N3, R1-N4, R1-W2, R1-W4, R1-W5, R1-W6, R1-W8, R1-W9, R1-W10, R1-M1, R1-M2, R1-M3）\n- ⚠️ **Partially resolved**: 3 个（R0-C4 SJ 新颖性, R1-W1 SJ 形式化, R1-W3 ρ contextualization, R1-W7 constrained decoding）\n- ❌ **Unresolved**: 0 个\n\n论文从 Round 0 到 Round 2 改善显著，绝大多数遗留问题已修复或充分 hedge。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference / Strong Findings**\n\n**Reviewer 1**: 3.5/5, Confidence 4/5\n**Reviewer 2**: 3.5/5, Confidence 4/5\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.75 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 3.5 | 4.0 | 3.75 |\n\n**核心判断**：方法论扎实、统计严谨的 empirical study。Quality estimation 分析是论文的强项，coverage 和 depth 达到 long paper 标准。Correlation-selection gap 是 genuinely useful negative result，概念贡献清晰。\n\n两个 critical 问题制约 Conference 推荐：(1) selection gap 作为核心贡献仅在 1 dataset × 1 model 验证，evidence base 与 \"fundamental disconnect\" framing 不匹配；(2) WNUT-17 capability boundary claim 仅有 1 个不显著数据点支撑。\n\n**如果 C1 和 C2 得到补充**（补 LLaMA SciERC selection + CoNLL selection appendix + WNUT-17 完整 signal table），论文从 3.5 提升到 4.0（Weak Accept）是可期的——evidence breadth 将匹配 framing breadth，核心 claims 将得到充分支撑。\n\n**当前推荐**：Findings（如不补充实验）/ Conference（如补充后 evidence 支撑 claims）。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"across NER and RE on three datasets\" 需修正为 \"NER (three datasets) and RE (SciERC)\"\n- 其余 claims 与正文一致，无 overclaim\n\n### Introduction (§1)\n- Contribution #2 的 framing 应限定 evidence scope\n- Contribution #3 需 WNUT-17 完整数据支撑\n- PaLM-540B attribution ✓, scope 已收窄 ✓\n\n### Related Work (§2)\n- 覆盖全面，无遗漏\n- 与 Nédellec et al. 的三点差异化清晰\n\n### Method (§3)\n- Per-sample vs instance-level formulation 精确\n- SJ: sim 和 g_i/g_j 已定义，Hungarian threshold 和分母 variant 需补充\n- Consensus-proximity = LOO-SJ 已明确\n- FK independent raters 假设可 brief acknowledge\n\n### Experiments (§4-5)\n- QE (Table 1): 需 N=8 uncertainty estimates\n- Selection (Table 3): 需扩展到 LLaMA SciERC + CoNLL appendix\n- RE selection: 需 bootstrap 统计检验\n- WNUT-17: 需完整 signal table\n- n=529 vs 551: 需说明 filtering\n\n### Discussion (§6)\n- QE vs selection 区分清晰 ✓\n- Logprob failure analysis 充分 ✓\n- Constrained decoding 讨论需从 logprob-specific 扩展为全局 confound\n- ρ=0.38 cross-method contextualization 需 footnote\n\n### Conclusion (§7)\n- 三个 findings 准确反映论文内容\n- RE limitation hedge ✓\n\n### Limitations\n- 诚实且全面\n- 需增加 constrained decoding confound 条目",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline"
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
    "report": "# Round 2 审稿报告 — struct_self_consist_ie\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性 + 格式）\n**交叉分享**: 已完成，两位 Reviewer 均提交逐条 [AGREE]/[REBUT] 回应\n\n---\n\n## Summary\n\n本文系统比较了三个族群（structural/surface/model-internal）的五种 confidence signal 在 generative IE（NER + RE）中的 quality estimation 与 sample selection 表现。核心发现是 \"correlation-selection gap\"：instance-level consistency signals 是有效的 quality estimators（entity voting ρ=0.38, exact match AUROC=0.75），但无法可靠超越 greedy decoding 进行 best-of-N selection（p>0.39, bootstrap），尽管存在 13-18pp 的 oracle headroom。附带发现 signal ranking 随 task difficulty 变化（EM 领先 easy tasks，SJ/Voting 领先 hard tasks，WNUT-17 全部 collapse）。\n\n---\n\n## Strengths\n\n1. **概念贡献清晰且有框架性价值**：quality estimation（ranking instances by expected performance）vs sample selection（choosing best output among N candidates）的解耦（§3.1 per-sample vs instance-level signal formulation）对 generative IE 社区有指导意义，是与 Nédellec et al. (2026) 的关键差异化。\n\n2. **Quality estimation 分析深度突出**：5 signals × 4 configurations (Table 1) + conditional filtering + capability stratification + per-relation diagnostic + ρ-AUROC dissociation 分析，超过多数同类 empirical study。\n\n3. **统计规范（selection）达到高标准**：Bootstrap resampling (B=10,000, n=529, instance-level paired), percentile 95% CIs, Cohen's d=0.038, sign test 61W/70L, 3-seed 含义明确——远超多数 NLP empirical papers。\n\n4. **诚实的 hedging**：RE single-dataset 限制在 Introduction/Discussion/Conclusion/Appendix 四处 acknowledge；logprob temperature gap 在正文 + Limitations 双重标注；claim 用 \"consistent across tested model families\" 而非 \"model-agnostic\"——Round 0-1 的 self-awareness 问题已有实质改善。\n\n5. **Related Work 覆盖全面**：§2 涵盖 self-consistency 变体（USC, CISC, ReASC, ranked voting, latent SC）、difficulty-adaptive 方法（Optimal SC, Difficulty-Adaptive SC）、generative self-aggregation、conformal prediction、semantic uncertainty 等。49 条 bib 全部 cited，0 orphan。\n\n6. **ρ-AUROC dissociation 是 actionable finding**：EM 在 ρ 排名低但 AUROC 领先（SciERC NER: ρ=0.295 rank #3, AUROC=0.749 rank #1），揭示 binary vs continuous signal properties 的 metric-dependent 行为，对 practitioners 在 quality-aware routing 中有直接实用价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. Selection 证据面过窄——核心贡献仅 1 dataset × 1 model 验证** [Reviewer 共识: unanimously critical]\n\n- **位置**: Table 3 (§5.3)；Abstract; Introduction Contribution #2; Conclusion\n- **问题**: Correlation-selection gap 是论文的 differentiator（与 Nédellec et al. 的关键区别），但 Table 3 的 selection 分析仅覆盖 SciERC/Qwen。Quality estimation 有 3 datasets × 2 models 的覆盖，selection 仅 1×1，逻辑链断裂。Abstract \"no signal reliably surpasses greedy decoding on either task\" 的 evidence base 实际是 1 dataset × 1 model × 2 tasks。CoNLL selection 未报告（即使 headroom 极小，negative result 本身有价值——说明 gap 可能是 hard-task specific）；LLaMA SciERC selection 未报告（cross-model 验证缺失）。\n- **Action**: (1) 补 LLaMA SciERC selection 结果验证 cross-model generalization；(2) CoNLL selection 放 Appendix（即使结论是 ceiling effect）；(3) 如 WNUT-17 selection 不可行，明确说明 oracle-greedy gap。\n\n**C2. WNUT-17 capability boundary claim 缺乏系统数据** [Reviewer 共识: unanimously critical]\n\n- **位置**: §5.1; Introduction Contribution #3\n- **问题**: Contribution #3 列出 \"task-complexity boundary conditions\"，WNUT-17 是关键证据。但全文仅报告 SJ 一个信号的 ρ=0.082 (p=0.106)——一个不显著的单信号结果。其他四个信号（Voting, EM, FK, Logprob）在 WNUT-17 的结果完全缺失。用单个不显著数据点支撑 \"all signals converge when model capability is insufficient\" 逻辑上不成立。如果 5 个信号全部 collapse，这反而是更强的证据。\n- **Action**: Appendix 增加 WNUT-17 完整 table（5 signals × ρ + AUROC）；补 conditional ρ（non-zero F1 subset）排除 floor effect。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. ρ=0.38 缺乏 cross-method 数值对比** [R2 列为 critical, R1 同意但建议降为 should-fix]\n\n- **位置**: §5.1, §6 Discussion\n- **问题**: 论文以 ρ=0.38 为核心正面结论（\"effective quality estimators\"），intra-study context 已有（14% variance explained + AUROC=0.749），但 cross-method numerical context 完全缺失。§2 引用 semantic entropy (Kuhn 2023)、P(True) (Kadavath 2022)、CoCoA (Vashurin 2025) 但未给出任何数值对比。R1 指出 structured IE 与 discrete-answer QA 的 output space 根本不同，direct comparison 有误导风险，因此降为 should-fix。\n- **Action**: §5 或 §4.2 加 footnote，引用可比方法的典型 AUROC 值，并明确 cross-task comparison 的困难性。\n\n**W2. N=8 QE ρ 缺乏 uncertainty quantification** [Reviewer 共识]\n\n- **位置**: Table 1 (§5.1)\n- **问题**: Table 1 N=8 行为 point estimates without CIs/standard errors。多处 signal ordering Δ=0.003-0.01（如 CoNLL LLaMA SJ-FK Δ=0.003），参照 N=16 σ≈0.006-0.008，可能 within noise。正面 QE 结论反而缺乏统计支撑，与 selection 的 thorough bootstrap 标准不一致。\n- **Action**: 对 N=8 主要 ρ 值报告 bootstrap CIs，或 Appendix 补 3-seed runs。\n\n**W3. SJ Hungarian matching 无 threshold + Eq.(4) 非标准分母** [Reviewer 共识, R2 交叉回应提升严重性]\n\n- **位置**: Eq.(4), §3.2\n- **问题**: sim = token-level IoU ✓, g_i/g_j 定义 ✓。但：(1) Hungarian 是否有 minimum similarity threshold？无 threshold 则完全不相关 span 也会 match，SJ numerator 非零；(2) 分母 max(|g_i|,|g_j|) 是非标准 Jaccard variant（标准为 |A∪B|），未解释设计选择。\n- **Action**: 明确 threshold 及 zero-overlap matched pairs 比例；一句话解释 max vs union 的设计理由。\n\n**W4. RE selection 无统计检验** [Reviewer 共识]\n\n- **位置**: Table 3, §5.3\n- **问题**: NER selection 有完整 bootstrap（p, CI, Cohen's d, sign test），RE 仅叙述性 \"no signal exceeds greedy\" 无任何统计量。RE oracle headroom 18.1pp 更大，selection failure 更需 p-value 支撑。\n- **Action**: 补 RE selection bootstrap p-value 和 CI。\n\n**W5. Constrained decoding 作为全局 confound 讨论不足** [R2 提出, R1 交叉同意]\n\n- **位置**: §6 Discussion; Limitations\n- **问题**: Discussion \"Why logprob fails\" 段提到 constrained decoding 压缩 per-sample diversity，但仅在 logprob context 下讨论。如果 constrained decoding 压缩 diversity，影响的不仅是 logprob，还包括 consensus-proximity selection（SJ/Voting）——因为后者也依赖 per-sample 差异区分候选。Limitations 未列此 confound。\n- **Action**: Limitations 增加 constrained decoding 条目；或补 per-sample F1 variance 数据证明 diversity 已足够。\n\n**W6. Abstract \"across NER and RE on three datasets\" 措辞误导** [Reviewer 共识]\n\n- **位置**: Abstract line 3\n- **问题**: RE 仅在 SciERC 评估，但 Abstract 自然读法暗示 NER+RE 均在三数据集上进行。\n- **Action**: 改为 \"across NER (three datasets) and RE (SciERC)\" 或类似准确表述。\n\n**W7. n=529 vs SciERC n=551 discrepancy** [Reviewer 共识]\n\n- **位置**: §5.3\n- **问题**: Bootstrap 用 n=529 但 SciERC test set 有 551 instances，22 instances 被 drop 原因未交代。\n- **Action**: 一句话说明 filtering criteria。\n\n---\n\n### Minor\n\n- Eq.(4) 分母 max 而非 union 需一句设计理由说明\n- FK adaptation：N 个来自同一模型的 stochastic samples 不是 Fleiss' κ 假设的 independent raters，brief acknowledgment 即可\n- Table 1 N=8 是 single-seed 还是 averaged 未说明\n- EM majority-vote selection 在 Table 3 中标 \"---\"，应加 1-2 句解释 exact-match plurality 在 structured IE 中的退化问题（Reviewer 分歧点，R1 反驳 R2，见下文 Divergence）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上独立达成完全一致：\n\n1. **Selection 证据面过窄是最关键问题**（R1-N1 = R2-N2, unanimously critical）：correlation-selection gap 仅 1 dataset × 1 model 验证，但 framed 为 \"fundamental disconnect\"\n2. **WNUT-17 系统数据缺失**（R1-N2 ⊃ R2-W3, unanimously critical）：5 signals 中仅报告 1 个不显著结果\n3. **N=8 QE 缺 uncertainty**（R1-W1, R2 交叉同意）\n4. **SJ threshold 未规范**（R1-W2, R2 交叉同意并提升严重性）\n5. **RE selection 缺统计检验**（R1-W3, R2 交叉同意）\n6. **Abstract RE 措辞需修正**（R2-W2, R1 交叉同意）\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **EM majority-vote selection (R2-W4)**：R2 认为 EM<1 时应实现 majority-vote selection；R1 反驳指出 structured IE 中 exact-match plurality 退化严重（通常仅 1-2 identical samples），consensus-proximity (SJ selection) 已是 soft majority vote。**Director 判断**：R1 的反驳有技术依据，降为 minor（加解释即可）。\n\n2. **LLaMA SciERC N=8 数据完整性 (R1-W4)**：R1 认为 Table 1 SciERC 列仅 Qwen、LLaMA 数据不全；R2 部分反驳指出 CoNLL 有完整 cross-model 覆盖，但同意 Table 1 应标注 \"Qwen-only\"。**Director 判断**：R2 的反驳合理——CoNLL cross-model 差异极小（Δ=0.005），SciERC 缺失不影响核心 claim。标注即可。\n\n3. **ρ=0.38 contextualization 严重性 (R2-N1 vs R1 交叉回应)**：R2 列为 critical，R1 同意需要但降为 should-fix（structured IE vs QA output space 不同，direct comparison 有误导风险）。**Director 判断**：采纳 R1 的降级——footnote 级修改，不构成 must-fix。\n\n---\n\n## Questions for Authors\n\n1. WNUT-17 上 Voting/EM/FK/Logprob 的 ρ 和 AUROC 分别是多少？\n2. CoNLL 的 best-of-N selection 结果（oracle-greedy gap 有多大）？\n3. SciERC bootstrap n=529 中 22 instances 被 drop 的 criteria？\n4. SJ Hungarian matching 是否有 minimum similarity threshold？无 threshold 时 sim≈0 matched pairs 占多少？\n5. Table 1 N=8 主要结果是 single-seed 还是 averaged？\n\n---\n\n## Missing References\n\n无重大遗漏。Round 1 指出的 Optimal SC、Difficulty-Adaptive SC、Generative Self-Aggregation、conformal prediction 等均已补充。49 条 bib 全部 cited，0 orphan，45 条 verified。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Round 0-1 遗留 Issue 修复状况\n\n**24 个历史 issues 状态汇总**：\n- ✅ **Resolved**: 19 个（R0-C1, R0-C2, R0-C3, R0-C5, R0-C6, R0-W1, R0-W4, R0-RR-D1, R1-N1, R1-N2, R1-N3, R1-N4, R1-W2, R1-W4, R1-W5, R1-W6, R1-W8, R1-W9, R1-W10, R1-M1, R1-M2, R1-M3）\n- ⚠️ **Partially resolved**: 3 个（R0-C4 SJ 新颖性, R1-W1 SJ 形式化, R1-W3 ρ contextualization, R1-W7 constrained decoding）\n- ❌ **Unresolved**: 0 个\n\n论文从 Round 0 到 Round 2 改善显著，绝大多数遗留问题已修复或充分 hedge。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference / Strong Findings**\n\n**Reviewer 1**: 3.5/5, Confidence 4/5\n**Reviewer 2**: 3.5/5, Confidence 4/5\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.75 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 3.5 | 4.0 | 3.75 |\n\n**核心判断**：方法论扎实、统计严谨的 empirical study。Quality estimation 分析是论文的强项，coverage 和 depth 达到 long paper 标准。Correlation-selection gap 是 genuinely useful negative result，概念贡献清晰。\n\n两个 critical 问题制约 Conference 推荐：(1) selection gap 作为核心贡献仅在 1 dataset × 1 model 验证，evidence base 与 \"fundamental disconnect\" framing 不匹配；(2) WNUT-17 capability boundary claim 仅有 1 个不显著数据点支撑。\n\n**如果 C1 和 C2 得到补充**（补 LLaMA SciERC selection + CoNLL selection appendix + WNUT-17 完整 signal table），论文从 3.5 提升到 4.0（Weak Accept）是可期的——evidence breadth 将匹配 framing breadth，核心 claims 将得到充分支撑。\n\n**当前推荐**：Findings（如不补充实验）/ Conference（如补充后 evidence 支撑 claims）。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"across NER and RE on three datasets\" 需修正为 \"NER (three datasets) and RE (SciERC)\"\n- 其余 claims 与正文一致，无 overclaim\n\n### Introduction (§1)\n- Contribution #2 的 framing 应限定 evidence scope\n- Contribution #3 需 WNUT-17 完整数据支撑\n- PaLM-540B attribution ✓, scope 已收窄 ✓\n\n### Related Work (§2)\n- 覆盖全面，无遗漏\n- 与 Nédellec et al. 的三点差异化清晰\n\n### Method (§3)\n- Per-sample vs instance-level formulation 精确\n- SJ: sim 和 g_i/g_j 已定义，Hungarian threshold 和分母 variant 需补充\n- Consensus-proximity = LOO-SJ 已明确\n- FK independent raters 假设可 brief acknowledge\n\n### Experiments (§4-5)\n- QE (Table 1): 需 N=8 uncertainty estimates\n- Selection (Table 3): 需扩展到 LLaMA SciERC + CoNLL appendix\n- RE selection: 需 bootstrap 统计检验\n- WNUT-17: 需完整 signal table\n- n=529 vs 551: 需说明 filtering\n\n### Discussion (§6)\n- QE vs selection 区分清晰 ✓\n- Logprob failure analysis 充分 ✓\n- Constrained decoding 讨论需从 logprob-specific 扩展为全局 confound\n- ρ=0.38 cross-method contextualization 需 footnote\n\n### Conclusion (§7)\n- 三个 findings 准确反映论文内容\n- RE limitation hedge ✓\n\n### Limitations\n- 诚实且全面\n- 需增加 constrained decoding confound 条目",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline"
  }
}
```

</details>

---


### Tool result

_source line 238 · 2026-05-15T02:56:57.030653+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4367
}
```

</details>

---


### Assistant

_source line 239 · 2026-05-15T02:57:09.759103+00:00_

Round 2 审稿完成。

**审稿报告已投递至 Research Director。**

汇总：
- **Overall: 3.5 — Borderline Conference / Strong Findings**（R1: 3.5, R2: 3.5，高度一致）
- **2 个 Must-Fix**（Reviewer 共识 critical）：
  1. Selection gap 核心贡献仅 SciERC/Qwen 1×1 验证——需补 LLaMA SciERC selection + CoNLL selection appendix
  2. WNUT-17 capability boundary 仅 SJ 单个不显著数据点——需补全部 5 signals 完整 table
- **7 个 Should-Fix**：ρ=0.38 cross-method context、N=8 QE 无 CI、SJ threshold、RE selection 无统计检验、constrained decoding 全局 confound、Abstract RE 措辞、n=529 discrepancy
- **Round 0-1 遗留 19/24 issues resolved**，3 partially resolved，0 unresolved
- **推荐**：补齐 C1/C2 后可达 Weak Accept (4.0)；当前状态更适合 Findings

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 22

## Round 22

2 recorded events


### User

_source line 240 · 2026-05-15T02:57:12.597300+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。R1 的 7 个 substantive issues 中同意 6 个、部分反驳 1 个（W4，因 CoNLL 已有完整 cross-model 覆盖且 Appendix N=16 补充了 LLaMA SciERC 数据，但同意 Table 1 标注不清）。两份审稿最大共识是 selection claim 的 evidence base 过窄。

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

_source line 241 · 2026-05-15T02:57:25.281602+00:00_

Round 2 圆桌审稿已完成。

审稿报告已于上一轮提交给 Research Director（在收到 Reviewer 2 交叉回应之前，因 Reviewer 1 的交叉回应先到时已触发了汇总流程）。两位 Reviewer 的交叉回应现已全部收齐，核心共识与已提交报告一致：

**最终结论：3.5 — Borderline Conference / Strong Findings**

**两个 Must-Fix（Reviewer 一致共识）：**
1. Selection gap 仅 SciERC/Qwen 1×1 验证，需补 LLaMA SciERC + CoNLL selection
2. WNUT-17 仅 SJ 一个不显著 ρ 值，需补全部 5 signals 完整 table

**补齐后可达 4.0 (Weak Accept)**。Issue Tracker 已同步更新（19 resolved / 3 partially resolved / 9 new open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 23

## Round 23

62 recorded events


### User

_source line 242 · 2026-05-15T03:55:07.713206+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

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

_source line 243 · 2026-05-15T03:55:13.299652+00:00_

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

_source line 244 · 2026-05-15T03:55:13.350550+00:00_

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
…[truncated 2458 chars]

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

_source line 245 · 2026-05-15T03:55:17.065168+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "8"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-15T03:55:17.065643+00:00_



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

_source line 247 · 2026-05-15T03:55:22.587082+00:00_

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

_source line 248 · 2026-05-15T03:55:23.095546+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (73 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_017_llama_conll_n16_s456_r1024（准备中）\n- exp_017_llama_conll_n16_r1024（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n- exp_007_ner_llama（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp008_re_n16（准备中）\n\n## 近期结论\n- **exp_002_conll_n16_r1024** (killed): —\n- **exp_007_llama_n16_r1024** (killed): —\n- **exp_017_llama_conll_n16_s123_r1024** (killed): —\n\n## 趋势\n成功 37 / 负向 18 / 失败 1 / 共 64\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 508
}
```

</details>

---


### Tool call

_source line 249 · 2026-05-15T03:55:23.146175+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "5000"
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
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-15T03:55:24.554347+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## Registry 清理备注 (2026-05-15)\\n- 9 个 PREPARING+killed 实验因状态机限制无法推进到 DONE，实质已废弃\\n- 包括：exp_017_llama_conll_n16_s456_r1024, exp_017_llama_conll_n16_r1024, exp_001_n16_seed123_full, exp_001_n16_seed456_full, exp001_seed123, exp001_seed456, exp_007_ner_llama, exp_002_merge_conll2003, exp008_re_n16\\n\", \"total_chars\": 1189, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool call

_source line 251 · 2026-05-15T03:55:24.554962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 252 · 2026-05-15T03:55:24.606316+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.

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

_source line 253 · 2026-05-15T03:55:29.284744+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
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
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-15T03:55:29.336376+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
/home/ubuntu/.agent-
…[truncated 1368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 255 · 2026-05-15T03:55:34.659249+00:00_

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

_source line 256 · 2026-05-15T03:55:35.161730+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

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

_source line 257 · 2026-05-15T03:55:35.162064+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "review_issues.yaml",
  "max_chars": "5000"
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
    "file": "review_issues.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 258 · 2026-05-15T03:55:35.463650+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-15T03:55:35.514226+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 260 · 2026-05-15T03:55:35.564971+00:00_



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

_source line 261 · 2026-05-15T03:55:39.682785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
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
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-15T03:55:39.984552+00:00_

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

_source line 263 · 2026-05-15T03:55:40.990033+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-15T03:55:40.990629+00:00_

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

_source line 265 · 2026-05-15T03:55:41.442958+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4012 chars]

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

_source line 266 · 2026-05-15T03:55:41.443514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-15T03:55:41.494148+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 3184 chars]

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

_source line 268 · 2026-05-15T03:55:42.096986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-15T03:55:42.398790+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc c
…[truncated 10971 chars]

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

_source line 270 · 2026-05-15T03:55:42.399168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-15T03:55:42.851854+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-s
…[truncated 2466 chars]

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

_source line 272 · 2026-05-15T03:55:42.852428+00:00_

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

_source line 273 · 2026-05-15T03:55:43.806559+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${\approx}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and when model capability is insufficient (WNUT-17), full-set correlations are inflated by zero/non-zero separation (Voting $\rho{=}0.724$, conditional $\rho{=}0.038$, n.s.) while all signals converge toward weak or non-significant conditional correlations.
8	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
11	
12	\paragraph{Why quality estimators fail as selectors.}
13	The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
14	Quali
…[truncated 3455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-15T03:55:43.957782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-15T03:55:44.259738+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and when model capability is insufficient, inflated full-set correlations (driven by zero/non-zero separation) mask the collapse of all signals on the conditional set.
11	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
12	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
13	
14	Several dire
…[truncated 659 chars]

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

_source line 276 · 2026-05-15T03:55:44.311003+00:00_

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

_source line 277 · 2026-05-15T03:55:47.531814+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2025 – CL deadlines for Qualifying Papers | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/11"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Here are the key details from the EMNLP 2026 Call for Papers:

## Submission Deadline

The ARR submission deadline for long
…[truncated 1533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7849
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-15T03:55:47.532511+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
16	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 3221
}
```

</details>

---


### Tool call

_source line 279 · 2026-05-15T03:55:47.883897+00:00_

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

_source line 280 · 2026-05-15T03:55:47.884524+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 14999 chars]

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

_source line 281 · 2026-05-15T03:55:48.035201+00:00_

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

_source line 282 · 2026-05-15T03:55:48.085810+00:00_



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

_source line 283 · 2026-05-15T03:55:55.068399+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template double blind anonymity ARR",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
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
    "query": "EMNLP 2026 submission format page limit template double blind anonymity ARR",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-15T03:55:56.028034+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__request_study_approval",
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
    "query": "select:mcp__agent-ml-research__request_study_approval",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-15T03:55:56.028508+00:00_



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

_source line 286 · 2026-05-15T03:55:57.438222+00:00_

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

_source line 287 · 2026-05-15T03:55:57.940356+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-15T03:55:58.392364+00:00_

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

_source line 289 · 2026-05-15T03:55:58.443050+00:00_

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


### Tool result

_source line 290 · 2026-05-15T03:56:01.306349+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template double blind anonymity ARR"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Empirical Methods in Natural Language Processing EMNLP 2022 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/empirical-methods-natural-language-processing-emnlp-2022"},{"title":"Empirical Methods in Natural Language Processing | ACL Member Portal","url":"https://www.aclweb.org/portal/content/empirical-methods-natural-language-processing"}]

Based on the web search results, here's information about EMNLP 2026 submission requirements:

## EMNLP 2026 Industry Track Submission Guidelines

The Industry Track accepts full-length papers with a maximum of 6 pages. Submissions must be double-blind, meaning th
…[truncated 1226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6237
}
```

</details>

---


### Tool call

_source line 291 · 2026-05-15T03:56:05.076233+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" main conference papers page limit long short paper requirements site:2026.emnlp.org"
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
    "query": "\"EMNLP 2026\" main conference papers page limit long short paper requirements site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-15T03:56:05.980314+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit long paper short paper template",
  "allowed_domains": "['aclrollingreview.org']"
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
    "query": "ACL Rolling Review 2026 submission guidelines page limit long paper short paper template",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 293 · 2026-05-15T03:56:06.432685+00:00_

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

_source line 294 · 2026-05-15T03:56:06.834904+00:00_

1	issues:
2	  # ============================================================
3	  # Round 0 issues
4	  # ============================================================
5	  - id: "R0-C1"
6	    summary: "模型规模单一（仅 8B）"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 0
11	    last_seen_round: 1
12	    mentions:
13	      - round: 0
14	        reviewers: [1, 2]
15	        note: "8B→8B 仅验证架构鲁棒性非规模鲁棒性"
16	      - round: 1
17	        reviewers: [1, 2]
18	        note: "model-agnostic 与 Limitations 矛盾"
19	    action_items:
20	      - round: 1
21	        action: "全文替换 model-agnostic → consistent across tested model families"
22	        assigned_to: "Paper Agent"
23	        status: resolved
24	    resolution: "Round 2 Reviewer 确认措辞修正到位，无再提"
25	    resolution_round: 2
26	
27	  - id: "R0-C2"
28	    summary: "相关工作显著遗漏"
29	    category: framing
30	    severity: warning
31	    status: resolved
32	    first_raised_round: 0
33	    last_seen_round: 1
34	    mentions:
35	      - round: 0
36	        reviewers: [1, 2]
37	        note: "5 篇核心文献缺失"
38	      - round: 1
39	        reviewers: [1, 2]
40	        note: "新遗漏：Optimal SC, Difficulty-Adaptive SC"
41	    action_items:
42	      - round: 1
43	        action: "补充 6 篇引用到 Related Work"
44	        assigned_to: "Paper Agent"
45	        status: resolved
46	    resolution: "Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏"
47	    resolution_round: 2
48	
49	  - id: "R0-C3"
50	    summary: "RE 结论仅基于 SciERC 单数据集"
51	    category: experiment
52	    severity: critical
53	    status: resolved
54	    first_raised_round: 0
55	    last_seen_round: 2
56	    mentions:
57	      - round: 0
58	        reviewers: [1, 2]
59	        note: "需跨数据集验证或降级措辞"
60	      - round: 2
61	        reviewers: [1, 2]
62	        note: "Abstract RE 措辞需修正"
63	    action_items:
64	      - round: 1
65	        action: "降级措辞 universal → observed in SciERC"
66	        assigned_to: "Paper Agent"
67	        status: resolved
68	      - round: 
…[truncated 18884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 295 · 2026-05-15T03:56:07.840325+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content",
  "glob": "*.{yaml,yml,json,toml}",
  "-i": "True"
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
    "glob": "*.{yaml,yml,json,toml}",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 296 · 2026-05-15T03:56:07.891025+00:00_

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


### Tool result

_source line 297 · 2026-05-15T03:56:08.744634+00:00_

Web search results for query: ""EMNLP 2026" main conference papers page limit long short paper requirements site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"}]

Based on my search of the EMNLP 2026 call for papers, here are the page limit requirements for main conference papers:

**Page Limits for Submissions:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

**After Acceptance:**
Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up
…[truncated 278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 3668
}
```

</details>

---


### Tool result

_source line 298 · 2026-05-15T03:56:11.509259+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit long paper short paper template"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits:

## Page Limit
…[truncated 978 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5528
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-15T03:57:24.500269+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 审稿对象\n- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）\n- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind\n\n## 你的审查侧重\n\n### 1. 方法定义严谨性\n- 5 个 confidence signal（logprob, EM, FK, SJ, voting）的数学定义是否清晰、无歧义\n- Soft Jaccard 的 Hungarian matching + token-level IoU 定义是否完整（threshold? denominator 选择理由？）\n- Per-sample vs instance-level 信号的区分是否准确且一致\n- \"Correlation-selection gap\" 概念是否严格定义，还是仅为经验观察的命名\n\n### 2. 实验设计\n- 数据集选择（SciERC, CoNLL-2003, WNUT-17）是否覆盖足够的 difficulty gradient\n- N=8/16 的采样规模是否足够，是否需要更大 N 的实验\n- 两个模型（Qwen3-8B, LLaMA-3.1-8B）是否足以支撑跨模型结论\n- LoRA fine-tuning 设置是否公平（rank=32, α=64, 5 epochs）\n- 温度设置（T=0.7, T=1.0）是否充分\n\n### 3. 统计检验\n- Bootstrap resampling（B=10,000）的规范是否完整\n- p-value、CI、effect size 报告是否充分\n- 多重比较校正是否需要但缺失\n- \"no signal reliably surpasses greedy\" 的统计论证是否严谨\n\n### 4. 数据一致性\n- 表格数字与正文引用是否一致\n- 不同 section 对同一实验结果的描述是否矛盾\n- Figure 和 Table 的引用是否完整\n\n### 5. RE 单数据集问题\n- RE 结论仅基于 SciERC，论文是否对此做了充分的措辞限定\n- 44% zero-F1 对 RE 信号评估的影响是否充分讨论\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 审稿对象\n- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）\n- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind\n\n## 你的审查侧重\n\n### 1. 方法定义严谨性\n- 5 个 confidence signal（logprob, EM, FK, SJ, voting）的数学定义是否清晰、无歧义\n- Soft Jaccard 的 Hungarian matching + token-level IoU 定义是否完整（threshold? denominator 选择理由？）\n- Per-sample vs instance-level 信号的区分是否准确且一致\n- \"Correlation-selection gap\" 概念是否严格定义，还是仅为经验观察的命名\n\n### 2. 实验设计\n- 数据集选择（SciERC, CoNLL-2003, WNUT-17）是否覆盖足够的 difficulty gradient\n- N=8/16 的采样规模是否足够，是否需要更大 N 的实验\n- 两个模型（Qwen3-8B, LLaMA-3.1-8B）是否足以支撑跨模型结论\n- LoRA fine-tuning 设置是否公平（rank=32, α=64, 5 epochs）\n- 温度设置（T=0.7, T=1.0）是否充分\n\n### 3. 统计检验\n- Bootstrap resampling（B=10,000）的规范是否完整\n- p-value、CI、effect size 报告是否充分\n- 多重比较校正是否需要但缺失\n- \"no signal reliably surpasses greedy\" 的统计论证是否严谨\n\n### 4. 数据一致性\n- 表格数字与正文引用是否一致\n- 不同 section 对同一实验结果的描述是否矛盾\n- Figure 和 Table 的引用是否完整\n\n### 5. RE 单数据集问题\n- RE 结论仅基于 SciERC，论文是否对此做了充分的措辞限定\n- 44% zero-F1 对 RE 信号评估的影响是否充分讨论\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-15T03:57:40.380281+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15880
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-15T03:57:40.531360+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 审稿对象\n- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）\n- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- \"First multi-family comparison of confidence signals for generative IE\" 是否成立？是否有已发表工作做了类似比较？\n- \"Correlation-selection gap\" 作为核心发现——是否真正新颖，还是 self-consistency 文献中已知的现象？\n- Soft Jaccard 相对于 Nedellec (2026) 的增量贡献是否足够\n- 三项 contributions 是否分别有实质性的学术价值\n\n### 2. Related Work 覆盖\n- 自查以下方向是否有重要遗漏：\n  - Self-consistency / test-time scaling（2024-2026）\n  - Confidence / uncertainty estimation for LLMs（2024-2026）\n  - Generative IE 方法（UniNER, GoLLIE 等）\n  - Structured prediction 中的 calibration 工作\n- 对 Nedellec (2026) 的差异化论述是否公平准确\n- 引用是否真实存在（检查是否有可疑的 hallucinated citations）\n\n### 3. 写作质量与逻辑\n- Abstract → Introduction → Contributions 的叙事是否连贯\n- 论文结构是否合理（是否有冗余或缺失的 section）\n- 术语使用是否一致（如 \"quality estimation\" vs \"quality prediction\"）\n- Figure/Table 是否自解释、caption 是否充分\n- Discussion 是否过度推断或保守不足\n\n### 4. 格式合规\n- 页数是否符合 8 页限制（请估算）\n- 参考文献格式是否正确\n- 匿名性是否完整（是否有泄露身份的线索：GitHub URL、acknowledgments、自引模式）\n- Limitations section 是否充分（ARR 要求，desk-reject 项）\n- 是否缺少 Ethics Statement\n\n### 5. 负面结果的呈现\n- \"No signal reliably surpasses greedy\" 是核心负面结果——呈现是否平衡\n- 是否过度包装负面结果为正面贡献\n- 对未来工作的建议是否具体且可行\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 审稿对象\n- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）\n- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- \"First multi-family comparison of confidence signals for generative IE\" 是否成立？是否有已发表工作做了类似比较？\n- \"Correlation-selection gap\" 作为核心发现——是否真正新颖，还是 self-consistency 文献中已知的现象？\n- Soft Jaccard 相对于 Nedellec (2026) 的增量贡献是否足够\n- 三项 contributions 是否分别有实质性的学术价值\n\n### 2. Related Work 覆盖\n- 自查以下方向是否有重要遗漏：\n  - Self-consistency / test-time scaling（2024-2026）\n  - Confidence / uncertainty estimation for LLMs（2024-2026）\n  - Generative IE 方法（UniNER, GoLLIE 等）\n  - Structured prediction 中的 calibration 工作\n- 对 Nedellec (2026) 的差异化论述是否公平准确\n- 引用是否真实存在（检查是否有可疑的 hallucinated citations）\n\n### 3. 写作质量与逻辑\n- Abstract → Introduction → Contributions 的叙事是否连贯\n- 论文结构是否合理（是否有冗余或缺失的 section）\n- 术语使用是否一致（如 \"quality estimation\" vs \"quality prediction\"）\n- Figure/Table 是否自解释、caption 是否充分\n- Discussion 是否过度推断或保守不足\n\n### 4. 格式合规\n- 页数是否符合 8 页限制（请估算）\n- 参考文献格式是否正确\n- 匿名性是否完整（是否有泄露身份的线索：GitHub URL、acknowledgments、自引模式）\n- Limitations section 是否充分（ARR 要求，desk-reject 项）\n- 是否缺少 Ethics Statement\n\n### 5. 负面结果的呈现\n- \"No signal reliably surpasses greedy\" 是核心负面结果——呈现是否平衡\n- 是否过度包装负面结果为正面贡献\n- 对未来工作的建议是否具体且可行\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-15T03:57:42.093584+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1562
}
```

</details>

---


### Assistant

_source line 303 · 2026-05-15T03:57:47.563455+00:00_

Round 1 已启动。两名 Reviewer 已分配并开始独立审稿：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 实验设计 + 统计检验 + 数据一致性 | ⏳ 审稿中 |
| R2 | 新颖性 + 完整性 + 写作质量 + 格式合规 | ⏳ 审稿中 |

等待两位 Reviewer 返回初审意见后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 304 · 2026-05-15T04:03:14.145682+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：Strong Predictors, Weak Selectors

### Summary

本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在 generative IE（NER + RE）上的 quality estimation 和 sample selection 性能。核心发现是 correlation-selection gap：instance-level consistency signal 能预测哪些输入模型处理得好（ρ 最高 0.38, AUROC 最高 0.75），但无法在 best-of-N selection 中可靠超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。

---

### Strengths

- **S1**: Quality estimation 与 sample selection 的问题分解有真正洞察力，将先前工作混淆的两个目标清晰剥离
- **S2**: 实验方法论严谨：paired bootstrap (B=10,000)、多 seed、proper CI、Cohen's d、sign test
- **S3**: WNUT-17 分析揭示 inflated correlation 由 zero/non-zero boundary 驱动（Voting ρ=0.724 → conditional ρ=0.038, n.s.），是重要的 methodological warning
- **S4**: 负面结果处理诚实 balanced，Limitations 坦率承认多项局限
- **S5**: 论文结构和叙事流畅
- **S6**: Robustness 分析覆盖 temperature、N-scaling、cross-model

---

### Must-Fix (Critical)

**N1** [critical] RE 结论建立在单一 benchmark 上且受严重 floor effect 影响
- SciERC RE 44% zero F1，gap 的 RE 证据（-0.9pp, p=0.80）基础薄弱
- 一个 dataset + 严重 floor effect 不足以支撑 generalized conclusion
- 建议增加 RE benchmark 或显著降低 RE claim 强度

**N2** [critical] Logprob 失败缺乏实证解释
- 4 个 instance-level signal 无法 select 在定义上 expected；logprob 作为唯一 per-sample signal 为什么也失败才是关键问题
- Discussion 的 "constrained decoding 压缩 diversity" 解释是猜测性的
- 如果 gap 来自实验设置 artifact 而非结构化 IE 固有属性，核心 claim 需要重新审视
- 建议报告 per-sample logprob variance、unique output fraction、或比较 constrained vs. unconstrained decoding

**N3** [critical] 缺少 Ethics Statement
- ARR review form 明确要求 reviewer 评估 ethical considerations，缺失是格式问题

---

### Should-Fix (Warning)

**W1** "First multi-family comparison" claim 边界需更精确限定，与 CoCoA、CISC 等 existing multi-signal comparison 的差异应更明确
**W2** Soft Jaccard 增量贡献 borderline（vs. Voting Δρ CI 包含零，vs. EM borderline significant CI lower bound +0.003）
**W3** ρ–AUROC dissociation 是 expected statistical behavior，不应作为独立发现过度强调
**W4** 术语不一致："confidence signal" vs "consistency signal"、"VC" vs "Voting Conf."、LLaMA Factory 未引用
**W5** Related Work 遗漏：VerifiNER (ACL 2024)、RASC (NAACL 2025)

---

### Minor Issues

- Abstract 中 "oracle headroom" 此时无定义
- 对 Nedellec (2026) 措辞偏 adversarial
- FK independent raters 假设的 justification 不足
- Table 2 EM omission 需 unique output fraction 数据支持

---

### Missing References

1. Kim et al. (2024) "VerifiNER" — ACL 2024
2. Aggarwal et al. (2025) "Reasoning Aware Self-Consistency" — NAACL 2025
3. He et al. (2024) "Uncertainty Estimation on Sequential Labeling" — NAACL Findings 2024

---

### Scores

| 维度 | 分数 | 理由 |
|------|------|------|
| Overall | 3.0/5 | Findings track |
| Soundness | 3.5/5 | NER 扎实，RE 单 dataset + constrained decoding confound 未 disentangle |
| Excitement | 3.0/5 | 概念贡献有价值但 partially obvious + 无 positive path forward |
| Reproducibility | 4.0/5 | 方法详细、公开 benchmark/model，但代码公开未提及 |
| Confidence | 4/5 | 熟悉相关文献 |

**一句话**：方法论严谨的 empirical study，correlation-selection gap 有概念价值，但 RE 证据薄弱 + logprob 失败解释缺乏实证，适合 Findings 而非 Main。

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

_source line 305 · 2026-05-15T04:03:21.204789+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成独立审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 25

## Round 25

2 recorded events


### User

_source line 306 · 2026-05-15T04:03:23.888254+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0/5（Findings track）**。论文方法论严谨、correlation-selection gap 概念有价值，但三个 critical 问题影响接收——RE 仅一个 benchmark 且 floor effect 严重、logprob 失败的 constrained decoding 解释缺乏实证（可能是 artifact）、缺少 Ethics Statement。

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

_source line 307 · 2026-05-15T04:03:30.650056+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 26

## Round 26

6 recorded events


### User

_source line 308 · 2026-05-15T04:05:20.579630+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

**论文**：Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
**Venue**：EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)

---

## Summary

本文系统比较了生成式信息抽取（IE）中五种置信度信号（三个家族：structural, surface, model-internal）用于质量估计和样本选择两个不同目标的表现。在 SciERC（NER+RE）、CoNLL-2003、WNUT-17 三个数据集和两个 8B 模型（Qwen3-8B, LLaMA-3.1-8B）上实验。核心发现是"correlation-selection gap"：一致性信号在实例级质量估计上有效（ρ 最高 0.38，AUROC 最高 0.75），但用于 best-of-N 选择时没有任何信号能显著超过 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。

---

## Strengths

**S1. 清晰的问题分解与严谨的框架设计。** 将 quality estimation 与 sample selection 明确区分为两个独立目标（§3.1），并用不同指标（Spearman ρ + AUROC vs. best-of-N F1）分别评估，这一分析框架本身是对现有文献的有价值贡献。per-sample vs. instance-level 信号的形式化区分（Eq. 1-7）使得后续分析的逻辑链条清晰可追溯。

**S2. 全面的统计报告。** Bootstrap resampling (B=10,000) 附带 95% CI、Cohen's d、sign test win%（§4.3），pairwise Δρ CI（Appendix D），p-value 和 effect size 齐全。多数实证论文不会做到这个粒度。

**S3. 诚实的 scope limitation 声明。** RE 单数据集问题在 Introduction（第46行）、Discussion（第10行）、Conclusion（第12行）、Limitations 四处明确提及，且 WNUT-17 作为 capability boundary 的诚实报告（full-set ρ=0.724 vs. conditional ρ=0.038，Table 7）都体现了良好的学术诚信。

**S4. Task difficulty 分析有洞察力。** EM 在简单任务领先 vs. SJ/Voting 在复杂任务领先的 crossover 发现（§4.2，CoNLL vs. SciERC），以及 conditional filtering 后信号排序翻转（Figure 2 right panel），为从业者的信号选择提供了实用指导。

**S5. Soft Jaccard 信号设计合理。** 基于 type-aware Hungarian matching + token-level IoU 的 SJ 定义（Eq. 4-5）比简单的 surface matching 更适合结构化输出，对 Nédellec et al. (2026) 的 limitation (i) 有针对性的改进。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Constrained decoding 是 correlation-selection gap 的未控制混淆变量

- 具体位置：§5 Discussion 第25-27行，§Limitations 第15-16行
- 问题：论文的核心发现——"no signal reliably surpasses greedy"——可能部分是 constrained decoding（Outlines/vLLM）压缩 per-sample diversity 的产物，而非置信度信号本身的固有局限。论文在 Discussion 中承认"constrained decoding enforces schema compliance at the token level, which may compress per-sample diversity"，但仅作为 future work 提及，未设计任何对照实验。
- 为什么影响接收：这是论文最核心 claim 的 validity threat。如果 constrained decoding 将 N 个样本压缩到近乎相同的输出空间，任何选择器都无法区分它们——这就不是信号本身的问题，而是实验设置的 artifact。论文用 random baseline gap（3.6pp）论证"variance exists"，但 3.6pp 可能远低于 unconstrained generation 的 variance，使得 gap 的量化可能不具有 generalizability。
- 建议修改方向：（a）增加 unconstrained generation + post-hoc JSON parsing 的对照实验，即使 parse 失败率高，也能 characterize constrained vs. unconstrained 的 diversity 差异；或（b）报告 per-instance 样本间的 pairwise SJ 分布（当前已有此数据），量化 constrained decoding 下的实际 diversity level，并明确论述 gap 结论的 generalizability boundary 为 constrained decoding regime。

**N2** [critical] "No signal reliably surpasses greedy" 的统计论证逻辑不完整——failure to reject ≠ evidence of absence

- 具体位置：§4.3 第128行，p=0.39, 95% CI: [−3.0, +4.2] pp
- 问题：论文用 p>0.39（未能拒绝 H₀）论证"no signal reliably surpasses greedy"，但这只是 absence of evidence，不是 evidence of absence。标准 NHST 无法证明两种方法等价。CI 范围 [−3.0, +4.2] 涵盖了最大 +4.2pp 的可能增益，考虑到 13.2pp oracle headroom，这个区间并不能排除有意义的选择增益存在的可能。
- 为什么影响接收：这是论文三大贡献之一（correlation-selection gap）的统计基础。如果统计检验的逻辑链条有缺陷，核心贡献的可信度受损。
- 建议修改方向：（a）补充等价性检验（TOST, Two One-Sided Tests），设定临床等价边界（如 ±1pp 或 ±2pp），如果 90% CI 落入等价区间则可正式声明等价；（b）或补充 power analysis，说明当前样本量在给定 effect size 下的检测力；（c）至少将措辞从"no signal reliably surpasses"改为"we found no significant evidence that any signal surpasses"，并讨论检测力。

**N3** [critical] N=8 主要结果仅使用单一 seed（seed=42），缺乏可靠性验证

- 具体位置：Table 1 caption "N=8 results use seed=42"，§4.3 第126行
- 问题：论文的核心 quality estimation 结果（Table 1 N=8 部分，覆盖 4 个主要配置）和 selection 结果（Table 2）全部基于单一 random seed。N=16 实验使用了 3 seeds 并报告了 σ（Table 1 下半部分），但这些只覆盖 LLaMA CoNLL 一个配置。SciERC 和 WNUT 的关键结论（如 Voting ρ=0.379、SJ ρ=0.360、EM AUROC=0.749）和 selection gap（p=0.39）都是 single-seed。
- 为什么影响接收：信号排序差异很小（Voting vs. SJ Δρ=0.019，CI 含零），single-seed 结果无法确认这些排序是否稳定。尤其对于 selection 结果，不同 seed 可能产生不同的 p-value。N=16 的 3-seed σ 约 0.003-0.008 暗示 N=8 的方差可能更大（更少样本）。
- 建议修改方向：对 SciERC N=8（核心配置）补充至少 3 seed 的结果并报告 mean ± σ。这在计算上是可行的（inference 成本已产生，只需换 seed 重跑）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 多重比较校正缺失

- 具体位置：Table 8（Appendix D），§4.2 第65-66行 pairwise comparisons
- 问题：论文在 Table 8 报告了 3 个 pairwise Δρ comparison，在正文中隐式进行了更多比较（5 signals × 4+ configurations）。SJ–EM 的"borderline significant"结果（CI lower bound +0.003）在任何 multiple comparison correction 下都不会 survive。
- 建议：明确声明未做多重比较校正；对 borderline 结果的措辞应更谨慎（如"suggestive"而非"Yes†"）。

**W2** [warning] "Correlation-selection gap" 概念的 novelty 部分为 tautological

- 具体位置：§3.1 第10-11行，§5 Discussion 第13-14行
- 问题：5 个信号中 4 个是 instance-level（by design 无法 per-sample 区分），1 个是 per-sample（logprob）。Instance-level 信号无法做 sample selection 是定义层面的必然结果，不是实验发现。真正有经验价值的发现是：（a）logprob 这个唯一的 per-sample 信号也失败了；（b）consensus-proximity 转换策略未能有效弥合这一 gap。论文将 tautological 部分和 non-trivial 部分混在一起作为一个统一的"gap"，降低了概念的锐度。
- 建议：在 Discussion 中明确分离这两层论证：（1）instance-level 信号的结构性局限（by construction）；（2）logprob 的经验性失败（需要解释，论文已提供 constrained decoding 的解释）。这会使 contribution 更清晰。

**W3** [warning] FK 独立性假设未经验证

- 具体位置：§3.2 第37行："While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns."
- 问题：Fleiss' κ 的理论基础要求 raters 独立。温度采样的样本之间共享同一模型参数和 prompt，远非独立。论文仅以一句话 hand-wave 这个问题，未提供任何经验性验证（如 permutation test 检验 inter-sample 相关性）。
- 建议：至少报告 N=8 样本间的 average pairwise correlation 以 characterize 独立性偏离程度，或在 Limitations 中更明确讨论这对 FK 值解释性的影响。

**W4** [warning] SJ 定义中 Hungarian matching 的 cost function 未明确指定

- 具体位置：§3.2 Eq. 4，第42-46行
- 问题：论文说"compute bipartite matching via the Hungarian algorithm with span overlap"，但未明确说明是最大化 IoU（benefit）还是最小化 1-IoU（cost），也未说明 "without minimum similarity threshold" 的具体含义——是否允许 IoU=0 的匹配对？如果允许，一个完全不相关的 entity 被 matched 后贡献 sim=0 到分子但占据分母的一个位置，可能影响 SJ 的行为。
- 建议：补充一到两句明确 Hungarian algorithm 的优化目标（max-weight matching on IoU scores）和 zero-IoU pairs 的处理方式。

**W5** [warning] 两个模型均为 8B 参数，"cross-model" 结论的外推受限

- 具体位置：§Limitations 第4-6行
- 问题：Qwen3-8B 和 LLaMA-3.1-8B 代表的是同一参数量级的两个架构。论文多处使用"cross-model consistency"（如§4.2 第77行），但这更准确地说是"cross-architecture consistency at fixed scale"。论文在 Limitations 中提到 70B+ 模型未测试，但正文的措辞给人的印象是 cross-model 结论比实际更强。
- 建议：在正文中将"cross-model"替换为"cross-architecture"或加限定词（如"cross-model (at 8B scale)"），更准确地反映实际覆盖范围。

**W6** [warning] Consensus-proximity 是唯一的 instance-to-sample 转换策略，未比较替代方案

- 具体位置：§3.3 第67行
- 问题：将 instance-level 信号转为 per-sample 信号的策略（选择最接近 consensus 的样本）与 Minimum Bayes Risk (MBR) decoding 的 utility-maximization formulation 等价（Vashurin et al. 2025 已引用但未建立此联系）。论文未讨论其他可能的转换策略（如 diversity-weighted selection、centroid-based selection with different distance metrics）。如果 consensus-proximity 是次优策略，correlation-selection gap 可能被高估。
- 建议：（a）明确与 MBR decoding 的联系；（b）至少在 Discussion 中说明为何 consensus-proximity 是合理的默认选择，以及替代策略是否可能缩小 gap。

---

## Minor Issues（不影响接收）

**M1.** WNUT-17 "54% zero F1" 数据不一致。§4.1 第11行称"54% zero F1"，但 Table 7（Appendix）显示 n=689（filtering gold-empty 后）中 conditional n=334（non-zero），即 355/689 ≈ 51.5% zero F1，与 54% 有 ~2.5pp 差距。请核实并统一。

**M2.** Table 1 N=16 区域大面积空白。仅报告 LLaMA CoNLL 的 N=16 ρ 值，其余配置在 Appendix Table 5 中。建议至少在 Table 1 caption 中补充交叉引用，或考虑合并呈现。

**M3.** EM 从 selection 实验中排除的理由（Table 2 caption："the probability of two identical structured outputs is negligible"）缺乏经验支持。建议报告 N=8 实验中 exact match pairs 的实际频率以验证此声明。

**M4.** LOO-SJ 验证（Appendix C 第126行）仅报告了 Δρ=−0.014 和 per-instance max Δρ=3.1×10⁻⁴。注意这两个量的量纲不同：前者是整体 Spearman ρ 的变化，后者似乎是 per-instance confidence score 的变化。请澄清 per-instance Δρ 的具体含义。

**M5.** Figure 1 caption 中 "p=0.39 for NER logprob" 直接出现在 figure 描述中，但该 p 值来自 Table 2 的 selection 分析而非 figure 本身可视化的内容（figure 显示的是 correlation vs. selection bars）。Caption 中引入 figure 未直接呈现的统计结果容易造成混淆。

**M6.** §4.2 第64行的脚注比较 semantic entropy AUROC（0.75-0.85 on QA）与本文 AUROC（0.749 on IE），并承认"direct comparison is complicated"。既然承认不可直接比较，建议删除或大幅缩短此脚注，避免给读者留下可比较的印象。

**M7.** 引用格式：feng2025optimal 和 snell2024scaling 的 bib key 使用姓氏但 OpenAlex 返回的 first_author 为名字（Austin/Charlie），这是 bib key 命名惯例问题，不影响引用正确性。hobelsberger2025systematic 和 lightman2024verify 在 OpenAlex 未找到匹配，但两篇均为已知发表论文（后者为 ICLR 2024 paper），应为 API 限制。

---

## Questions to Authors

**Q1.** 是否考虑过在 constrained decoding 之外运行 unconstrained generation 作为对照？即使 parse 成功率低，比较两种 regime 下的 per-sample diversity（如 pairwise SJ 分布）也能 calibrate correlation-selection gap 的 generalizability。

**Q2.** Logprob 在 WNUT conditional set 上达到了所有信号中最高的 ρ=0.350（Table 7），这与主文中"logprob 是最弱信号"的叙述相矛盾。如何 reconcile 这一发现？是否暗示 logprob 在高难度 domain 的 capability boundary 区间反而有独特优势？

**Q3.** LoRA rank=32 的选择是否影响了 sample diversity？更低的 rank 可能导致 fine-tuned 模型更接近 base model 的分布，potentially increasing diversity。是否做过 LoRA rank 的敏感性分析？

**Q4.** Table 6（cross-configuration selection）中 LLaMA/SciERC N=16 configuration 下 SJ 和 FK 并列第一（0.649），但都低于 greedy（0.645→0.649 仅 +0.004pp）。N=16 是否提供了 selection 结果的 multi-seed bootstrap p-value？

---

## Missing References

- **MBR decoding 相关文献**：Eikema & Aziz (2022, "Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation") 和 Freitag et al. (2022, "High Quality Rather Than High Model Probability") 建立了 MBR decoding 的理论框架，本文的 consensus-proximity selection 与之直接相关但未讨论。
- **Structured prediction 的 uncertainty 估计**：Malinin & Gales (2021, "Uncertainty Estimation in Autoregressive Structured Prediction") 讨论了序列级输出的 uncertainty estimation，与本文的 structured output uncertainty 有方法论联系。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法定义基本清晰，统计报告充分；但 constrained decoding 混淆变量未控制（N1）、failure-to-reject 逻辑不完整（N2）、核心结果 single-seed（N3）是三个显著的 soundness gap |
| Excitement | 3/5 | Quality estimation vs. sample selection 的分离框架和 task-difficulty-dependent ordering 有实用价值；但 correlation-selection gap 中 instance-level 信号的部分是 tautological（W2），核心 insight 的 novelty 中等 |
| Reproducibility | 3.5/5 | LoRA 超参、bootstrap B、seed、评估指标均有报告；但缺少代码/数据可用性声明，logprob T=0.7 数据缺失，EM selection 排除缺乏经验验证 |
| Overall | 3/5 | Findings 水平。实验设计 mostly sound、写作质量高，但 N1-N3 三个 critical issues 共同削弱了核心贡献的可信度。若 N1（constrained decoding 对照）和 N3（multi-seed）能在修订中解决，可提升至 3.5 |
| Confidence | 4/5 | 熟悉 self-consistency、uncertainty estimation、IE evaluation 领域，仔细审查了方法定义和统计分析 |

---

## 总体评分

**Overall**: 3/5 (Findings)
**一句话总结**: 框架设计清晰、统计报告充分的经验性研究，但核心发现（correlation-selection gap）受 constrained decoding 混淆变量、single-seed 设计、和 failure-to-reject 论证逻辑三重限制，需要补充实验和统计修订以支撑论文的主要 claim。

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

_source line 309 · 2026-05-15T04:06:08.279000+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个 Must-Fix、Should-Fix 和 Minor Issue：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Summary\n本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在 generative IE（NER + RE）上的 quality estimation 和 sample selection 性能。核心发现是 correlation-selection gap：instance-level consistency signal 能预测哪些输入模型处理得好（ρ 最高 0.38, AUROC 最高 0.75），但无法在 best-of-N selection 中可靠超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。\n\n### Strengths\n- S1: Quality estimation 与 sample selection 的问题分解有真正洞察力\n- S2: 实验方法论严谨：paired bootstrap (B=10,000)、多 seed、proper CI、Cohen's d、sign test\n- S3: WNUT-17 分析揭示 inflated correlation 由 zero/non-zero boundary 驱动\n- S4: 负面结果处理诚实 balanced，Limitations 坦率承认多项局限\n- S5: 论文结构和叙事流畅\n- S6: Robustness 分析覆盖 temperature、N-scaling、cross-model\n\n### Must-Fix (Critical)\n**N1** [critical] RE 结论建立在单一 benchmark 上且受严重 floor effect 影响\n- SciERC RE 44% zero F1，gap 的 RE 证据（-0.9pp, p=0.80）基础薄弱\n- 一个 dataset + 严重 floor effect 不足以支撑 generalized conclusion\n- 建议增加 RE benchmark 或显著降低 RE claim 强度\n\n**N2** [critical] Logprob 失败缺乏实证解释\n- 4 个 instance-level signal 无法 select 在定义上 expected；logprob 作为唯一 per-sample signal 为什么也失败才是关键问题\n- Discussion 的 \"constrained decoding 压缩 diversity\" 解释是猜测性的\n- 如果 gap 来自实验设置 artifact 而非结构化 IE 固有属性，核心 claim 需要重新审视\n- 建议报告 per-sample logprob variance、unique output fraction、或比较 constrained vs. unconstrained decoding\n\n**N3** [critical] 缺少 Ethics Statement\n- ARR review form 明确要求 reviewer 评估 ethical considerations，缺失是格式问题\n\n### Should-Fix (Warning)\n**W1** \"First multi-family comparison\" claim 边界需更精确限定\n**W2** Soft Jaccard 增量贡献 borderline（vs. Voting Δρ CI 包含零，vs. EM borderline significant CI lower bound +0.003）\n**W3** ρ–AUROC dissociation 是 expected statistical behavior，不应作为独立发现过度强调\n**W4** 术语不一致：\"confidence signal\" vs \"consistency signal\"、\"VC\" vs \"Voting Conf.\"、LLaMA Factory 未引用\n**W5** Related Work 遗漏：VerifiNER (ACL 2024)、RASC (NAACL 2025)\n\n### Minor Issues\n- Abstract 中 \"oracle headroom\" 此时无定义\n- 对 Nedellec (2026) 措辞偏 adversarial\n- FK independent raters 假设的 justification 不足\n- Table 2 EM omission 需 unique output fraction 数据支持\n\n### Missing References\n1. Kim et al. (2024) \"VerifiNER\" — ACL 2024\n2. Aggarwal et al. (2025) \"Reasoning Aware Self-Consistency\" — NAACL 2025\n3. He et al. (2024) \"Uncertainty Estimation on Sequential Labeling\" — NAACL Findings 2024"
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
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个 Must-Fix、Should-Fix 和 Minor Issue：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Summary\n本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在 generative IE（NER + RE）上的 quality estimation 和 sample selection 性能。核心发现是 correlation-selection gap：instance-level consistency signal 能预测哪些输入模型处理得好（ρ 最高 0.38, AUROC 最高 0.75），但无法在 best-of-N selection 中可靠超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。\n\n### Strengths\n- S1: Quality estimation 与 sample selection 的问题分解有真正洞察力\n- S2: 实验方法论严谨：paired bootstrap (B=10,000)、多 seed、proper CI、Cohen's d、sign test\n- S3: WNUT-17 分析揭示 inflated correlation 由 zero/non-zero boundary 驱动\n- S4: 负面结果处理诚实 balanced，Limitations 坦率承认多项局限\n- S5: 论文结构和叙事流畅\n- S6: Robustness 分析覆盖 temperature、N-scaling、cross-model\n\n### Must-Fix (Critical)\n**N1** [critical] RE 结论建立在单一 benchmark 上且受严重 floor effect 影响\n- SciERC RE 44% zero F1，gap 的 RE 证据（-0.9pp, p=0.80）基础薄弱\n- 一个 dataset + 严重 floor effect 不足以支撑 generalized conclusion\n- 建议增加 RE benchmark 或显著降低 RE claim 强度\n\n**N2** [critical] Logprob 失败缺乏实证解释\n- 4 个 instance-level signal 无法 select 在定义上 expected；logprob 作为唯一 per-sample signal 为什么也失败才是关键问题\n- Discussion 的 \"constrained decoding 压缩 diversity\" 解释是猜测性的\n- 如果 gap 来自实验设置 artifact 而非结构化 IE 固有属性，核心 claim 需要重新审视\n- 建议报告 per-sample logprob variance、unique output fraction、或比较 constrained vs. unconstrained decoding\n\n**N3** [critical] 缺少 Ethics Statement\n- ARR review form 明确要求 reviewer 评估 ethical considerations，缺失是格式问题\n\n### Should-Fix (Warning)\n**W1** \"First multi-family comparison\" claim 边界需更精确限定\n**W2** Soft Jaccard 增量贡献 borderline（vs. Voting Δρ CI 包含零，vs. EM borderline significant CI lower bound +0.003）\n**W3** ρ–AUROC dissociation 是 expected statistical behavior，不应作为独立发现过度强调\n**W4** 术语不一致：\"confidence signal\" vs \"consistency signal\"、\"VC\" vs \"Voting Conf.\"、LLaMA Factory 未引用\n**W5** Related Work 遗漏：VerifiNER (ACL 2024)、RASC (NAACL 2025)\n\n### Minor Issues\n- Abstract 中 \"oracle headroom\" 此时无定义\n- 对 Nedellec (2026) 措辞偏 adversarial\n- FK independent raters 假设的 justification 不足\n- Table 2 EM omission 需 unique output fraction 数据支持\n\n### Missing References\n1. Kim et al. (2024) \"VerifiNER\" — ACL 2024\n2. Aggarwal et al. (2025) \"Reasoning Aware Self-Consistency\" — NAACL 2025\n3. He et al. (2024) \"Uncertainty Estimation on Sequential Labeling\" — NAACL Findings 2024"
  }
}
```

</details>

---


### Tool result

_source line 310 · 2026-05-15T04:06:31.087237+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22808
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-15T04:06:31.238212+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix、Should-Fix 和 Minor Issue：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n本文系统比较了生成式信息抽取（IE）中五种置信度信号用于质量估计和样本选择两个不同目标的表现。核心发现是\"correlation-selection gap\"：一致性信号在实例级质量估计上有效（ρ 最高 0.38，AUROC 最高 0.75），但用于 best-of-N 选择时没有任何信号能显著超过 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。\n\n### Strengths\n- S1: 清晰的问题分解与严谨的框架设计（per-sample vs. instance-level 形式化）\n- S2: 全面的统计报告（Bootstrap B=10,000 + CI + Cohen's d + sign test）\n- S3: 诚实的 scope limitation 声明（RE 单数据集在 4 处明确提及）\n- S4: Task difficulty 分析有洞察力（EM vs. SJ crossover）\n- S5: Soft Jaccard 信号设计合理（type-aware Hungarian matching + token-level IoU）\n\n### Must-Fix (Critical)\n**N1** [critical] Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n- 论文核心发现\"no signal reliably surpasses greedy\"可能部分是 constrained decoding（Outlines/vLLM）压缩 per-sample diversity 的产物\n- Random baseline gap 仅 3.6pp，可能远低于 unconstrained generation 的 variance\n- 建议增加 unconstrained generation 对照或量化 constrained decoding 下的实际 diversity level\n\n**N2** [critical] \"No signal reliably surpasses greedy\" 的统计论证逻辑不完整——failure to reject ≠ evidence of absence\n- p>0.39 只是 absence of evidence，不是 evidence of absence\n- CI 范围 [−3.0, +4.2] 不能排除有意义的选择增益\n- 建议补充等价性检验（TOST）或 power analysis\n\n**N3** [critical] N=8 主要结果仅使用单一 seed（seed=42），缺乏可靠性验证\n- Table 1 N=8 和 Table 2 全部基于 single random seed\n- N=16 的 3-seed σ 约 0.003-0.008 暗示 N=8 的方差可能更大\n- 信号排序差异很小（Voting vs. SJ Δρ=0.019，CI 含零），single-seed 无法确认稳定性\n\n### Should-Fix (Warning)\n**W1** 多重比较校正缺失（SJ–EM borderline significant 在任何 correction 下不会 survive）\n**W2** \"Correlation-selection gap\" 部分为 tautological（4/5 instance-level 信号 by design 无法 per-sample 区分）\n**W3** FK 独立性假设未经验证（温度采样非独立）\n**W4** SJ 定义中 Hungarian matching 的 cost function 未明确（max IoU? 允许 zero-IoU match?）\n**W5** \"Cross-model\" 实为 cross-architecture at fixed 8B scale\n**W6** Consensus-proximity 是唯一 instance-to-sample 转换策略，未比较替代方案（如 MBR decoding）\n\n### Minor Issues\n**M1** WNUT-17 \"54% zero F1\" vs Table 7 显示 51.5%，数据不一致\n**M2** Table 1 N=16 区域大面积空白\n**M3** EM selection 排除理由缺乏经验支持\n**M4** LOO-SJ Δρ 和 per-instance Δρ 量纲不同\n**M5** Figure 1 caption 引入 figure 未直接呈现的 p=0.39\n**M6** Semantic entropy footnote 比较既然不可比就不应出现\n**M7** 引用格式细节\n\n### Questions to Authors\nQ1: 是否考虑过 unconstrained generation 作为对照？\nQ2: Logprob 在 WNUT conditional set 最高 ρ=0.350，如何 reconcile \"logprob 最弱\"？\nQ3: LoRA rank=32 是否影响 sample diversity？\nQ4: N=16 selection 结果有无 multi-seed bootstrap p-value？\n\n### Missing References\n- MBR decoding: Eikema & Aziz (2022), Freitag et al. (2022)\n- Structured prediction uncertainty: Malinin & Gales (2021)"
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
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix、Should-Fix 和 Minor Issue：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n本文系统比较了生成式信息抽取（IE）中五种置信度信号用于质量估计和样本选择两个不同目标的表现。核心发现是\"correlation-selection gap\"：一致性信号在实例级质量估计上有效（ρ 最高 0.38，AUROC 最高 0.75），但用于 best-of-N 选择时没有任何信号能显著超过 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。\n\n### Strengths\n- S1: 清晰的问题分解与严谨的框架设计（per-sample vs. instance-level 形式化）\n- S2: 全面的统计报告（Bootstrap B=10,000 + CI + Cohen's d + sign test）\n- S3: 诚实的 scope limitation 声明（RE 单数据集在 4 处明确提及）\n- S4: Task difficulty 分析有洞察力（EM vs. SJ crossover）\n- S5: Soft Jaccard 信号设计合理（type-aware Hungarian matching + token-level IoU）\n\n### Must-Fix (Critical)\n**N1** [critical] Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n- 论文核心发现\"no signal reliably surpasses greedy\"可能部分是 constrained decoding（Outlines/vLLM）压缩 per-sample diversity 的产物\n- Random baseline gap 仅 3.6pp，可能远低于 unconstrained generation 的 variance\n- 建议增加 unconstrained generation 对照或量化 constrained decoding 下的实际 diversity level\n\n**N2** [critical] \"No signal reliably surpasses greedy\" 的统计论证逻辑不完整——failure to reject ≠ evidence of absence\n- p>0.39 只是 absence of evidence，不是 evidence of absence\n- CI 范围 [−3.0, +4.2] 不能排除有意义的选择增益\n- 建议补充等价性检验（TOST）或 power analysis\n\n**N3** [critical] N=8 主要结果仅使用单一 seed（seed=42），缺乏可靠性验证\n- Table 1 N=8 和 Table 2 全部基于 single random seed\n- N=16 的 3-seed σ 约 0.003-0.008 暗示 N=8 的方差可能更大\n- 信号排序差异很小（Voting vs. SJ Δρ=0.019，CI 含零），single-seed 无法确认稳定性\n\n### Should-Fix (Warning)\n**W1** 多重比较校正缺失（SJ–EM borderline significant 在任何 correction 下不会 survive）\n**W2** \"Correlation-selection gap\" 部分为 tautological（4/5 instance-level 信号 by design 无法 per-sample 区分）\n**W3** FK 独立性假设未经验证（温度采样非独立）\n**W4** SJ 定义中 Hungarian matching 的 cost function 未明确（max IoU? 允许 zero-IoU match?）\n**W5** \"Cross-model\" 实为 cross-architecture at fixed 8B scale\n**W6** Consensus-proximity 是唯一 instance-to-sample 转换策略，未比较替代方案（如 MBR decoding）\n\n### Minor Issues\n**M1** WNUT-17 \"54% zero F1\" vs Table 7 显示 51.5%，数据不一致\n**M2** Table 1 N=16 区域大面积空白\n**M3** EM selection 排除理由缺乏经验支持\n**M4** LOO-SJ Δρ 和 per-instance Δρ 量纲不同\n**M5** Figure 1 caption 引入 figure 未直接呈现的 p=0.39\n**M6** Semantic entropy footnote 比较既然不可比就不应出现\n**M7** 引用格式细节\n\n### Questions to Authors\nQ1: 是否考虑过 unconstrained generation 作为对照？\nQ2: Logprob 在 WNUT conditional set 最高 ρ=0.350，如何 reconcile \"logprob 最弱\"？\nQ3: LoRA rank=32 是否影响 sample diversity？\nQ4: N=16 selection 结果有无 multi-seed bootstrap p-value？\n\n### Missing References\n- MBR decoding: Eikema & Aziz (2022), Freitag et al. (2022)\n- Structured prediction uncertainty: Malinin & Gales (2021)"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-15T04:06:32.803817+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1565
}
```

</details>

---


### Assistant

_source line 313 · 2026-05-15T04:06:35.460493+00:00_

交叉分享任务已分配。等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 27

## Round 27

2 recorded events


### User

_source line 314 · 2026-05-15T04:06:38.094660+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

审查要点总结：

- **3 个 Must-Fix**：（1）constrained decoding 作为 correlation-selection gap 的未控制混淆变量，需对照实验或 diversity 量化；（2）"no signal surpasses greedy" 基于 failure-to-reject 逻辑，需补充等价性检验或修改措辞；（3）N=8 核心结果仅 single seed，需补充 multi-seed 验证
- **6 个 Should-Fix**：多重比较校正缺失、gap 概念部分 tautological、FK 独立性假设未验证、SJ Hungarian cost function 未明确、cross-model 措辞过度外推、consensus-proximity 未与 MBR decoding 建立联系且未比较替代策略
- **7 个 Minor**：WNUT 54% 数据不一致、Table 1 N=16 空白、EM exclusion 缺经验支持等
- **Overall 3/5 (Findings)**，Soundness 3.5，Excitement 3，Confidence 4

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

_source line 315 · 2026-05-15T04:06:43.348587+00:00_

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


## Round 28

## Round 28

2 recorded events


### User

_source line 316 · 2026-05-15T04:08:37.512760+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应

---

### Must-Fix Issues

**[AGREE] R2-N1: RE 结论建立在单一 benchmark 上且受严重 floor effect 影响**

同意这是一个实质性问题。我在自己的审稿中也将 RE 单数据集问题列为关注点（虽然未列为 Must-Fix，因为论文在 Introduction §1 第46行、Discussion §5 第10行、Conclusion §6 第12行、Limitations 四处均做了明确 hedging）。

R2 的核心论点是正确的：44% zero F1 严重压缩了信号的可区分范围，使得 RE 的 gap 证据（−0.9pp, p=0.80）缺乏统计说服力。补充一个观察：Appendix C（Table 7）的 WNUT conditional 分析表明，当 zero-F1 比例高时，full-set 指标会被 binary success/failure boundary 严重扭曲——SciERC RE 的 44% zero-F1 也存在类似问题，但论文未对 RE 做类似的 conditional 分析（SciERC conditional results in §4.2 and Figure 2 涵盖了 NER 和 RE，但 RE conditional ρ 仅在 Appendix C 简要提及而未深入讨论）。

不过，我认为增加新 RE benchmark 作为修订要求可能过于苛刻——这在 ARR revision cycle 内不太现实。更务实的修改方向是：（a）大幅降低 RE claim 强度（从"IE"泛化改为明确说"NER + preliminary RE evidence"）；（b）对 SciERC RE 补充 conditional filtering 分析（非零 F1 子集），量化 floor effect 对 gap 结论的影响。

**[AGREE] R2-N2: Logprob 失败缺乏实证解释**

完全同意，且这与我的 N1（constrained decoding 混淆变量）高度重叠。R2 精确地指出了问题的核心：4 个 instance-level signal 无法 per-sample select 是定义层面的必然（我在 W2 中也指出了这一 tautological 成分），所以论文真正需要解释的是 logprob 为什么也失败。

R2 建议的具体分析非常到位——per-sample logprob variance 和 unique output fraction 这两个量可以直接 characterize constrained decoding 对 diversity 的压缩程度。如果 unique output fraction 很低（比如 N=8 中平均只有 2-3 个 distinct outputs），那么 correlation-selection gap 在很大程度上就是一个 diversity limitation 而非信号本身的局限。

补充一个来自论文内部的支持证据：§5 Discussion 第22行报告"75% of instance-level logprob comparisons are effectively ties (win%=46.6%)"——这暗示 per-sample logprob 的 variance 确实很小，但论文没有进一步量化。报告每个 instance 的 logprob standard deviation 分布将直接回答这个问题。

此外，WNUT-17 conditional set 上 logprob 达到了所有信号中最高的 ρ=0.350（Table 7），而主文中 logprob 被一致描述为"最弱信号"。这一反转值得在 Discussion 中 reconcile——它可能暗示 logprob 在高 diversity 场景（WNUT 的 noisy domain 使得 constrained decoding 的约束力相对较弱）反而有优势，间接支持了 constrained decoding 压缩 diversity 的假说。

**[REBUT] R2-N3: 缺少 Ethics Statement**

不同意将此列为 Must-Fix/critical。

根据 ACL ARR CFP（2025 年 2 月更新版），Ethics Statement 是"encouraged"而非"required"。原文："We encourage, but do not require, papers to include an Ethics Statement." Limitations section 是 required 的，论文已包含。本文研究的是 confidence signal 评估方法论，使用的是公开 benchmark（SciERC、CoNLL-2003、WNUT-17），不涉及人类数据收集、隐私、dual-use 风险等典型 ethical concern。

当然，添加一个简短的 Ethics Statement（哪怕只说明使用的是公开数据、不涉及人类标注）是 good practice，但将其缺失标为"critical"与 ARR 政策不符。建议降级为 Minor。

---

### Should-Fix Issues

**[AGREE] R2-W1: "First multi-family comparison" claim 边界需更精确限定**

同意。§1 第35行的"First multi-family comparison of confidence signals for generative IE"措辞过宽。Nedellec et al. (2026) 已比较了 surface-level consistency 与 accuracy 的相关性（虽然不是 multi-family）；CoCoA (Vashurin et al., 2025) 融合了 model confidence 与 inter-sample consistency（虽然是 QA/summarization 而非 IE）。更精确的限定应是"first comparison spanning structural, surface, and model-internal signal families for both quality estimation and sample selection in generative structured IE"。

**[REBUT] R2-W2: SJ 增量贡献 borderline**

部分不同意。R2 聚焦于 SJ 在 ρ 上相对于 Voting 和 EM 的微小优势（Δρ CI 含零），但 SJ 的贡献不应仅以 ρ 增量衡量：

1. **Temperature robustness**: Table 5（Appendix B）显示 SJ NER ρ 在 T=0.7→1.0 之间仅变化 0.028（bootstrap CI 含零），而 FK 变化 0.054/0.091。SJ 是唯一在所有 temperature/N-scaling 条件下表现一致稳定的信号（§4.4 第80行）。
2. **Semantic matching 能力**: SJ 设计目的是处理 "partial overlap" 情况——同一实体的不同表面形式（如 span boundary 差异）。EM 和 FK 都依赖 exact string matching，在这些情况下系统性地低估一致性。论文 §1 第16行和 Related Work §2 第14-15行明确说明这解决了 Nedellec et al. 的 limitation (i)。
3. **N-scaling**: SJ 在 N=8→16 时一致性地改善（全部 setting 为正方向），FK 则表现不一致（§Appendix B 第78行：SciERC 上 degradation，CoNLL 上 improvement）。

因此，SJ 的贡献是作为一个 robust 的 structural similarity measure，而非在单个 snapshot（N=8, T=1.0, SciERC）上显著超越其他信号。论文的措辞应更清楚地传达这一点。

**[AGREE with nuance] R2-W3: ρ–AUROC dissociation 是 expected statistical behavior**

部分同意 R2 的诊断：binary classifier 的 AUROC 高于 continuous ranker 的 rank correlation 在统计上确实是 expected 的——EM 的 binary nature 使其天然适合二元分类而弱于连续排序。

但我认为论文的价值不在于发现 dissociation 本身，而在于将其映射到 IE 的实际使用场景：EM 适合 routing/triage（binary discrimination），Voting/SJ 适合 quality ranking。§5 Discussion 第16-17行的实践建议——"these signals are well-suited for routing and triage...but not for fine-grained ranking within a difficulty tier"——是从 dissociation 中提取的 actionable insight，不是对统计现象本身的过度宣传。

建议论文在 §4.2 的表述中承认 dissociation 的统计预期性，然后聚焦于实践含义，而非将其呈现为 surprising finding。

**[AGREE] R2-W4: 术语不一致**

同意。具体问题：
- "confidence signal" vs. "consistency signal"：前者出现在 Abstract、§1、§3；后者出现在 §4、§5。应统一为 "confidence signal"（论文的正式术语），仅在特指 consistency-based 子集时用 "consistency signal"。
- Table 6 用 "VC" 和 "LP"，正文和其他表格用 "Voting Conf." 和 "Log-prob"：应统一缩写。
- LLaMA Factory 未引用：§4.1 第14行提到但确实未提供引用。

**[AGREE with caveat] R2-W5: Related Work 遗漏**

VerifiNER (Kim et al., ACL 2024) 确实高度相关——它使用 LLM 作为 verifier 来检验 NER 输出质量，与本文的 quality estimation 目标直接相关，且提供了 supervised verification 的对照视角（本文是 unsupervised signals）。应在 Related Work §2 第24行附近讨论。

对于 RASC (Aggarwal et al., NAACL 2025)，如果它聚焦于 reasoning task 的 self-consistency 改进（如 Related Work §2 第7行已引用 Kim et al. 2026 的 REASC），需要确认是否为同一方法或不同工作。如果是不同工作且与 IE 相关，应引用；如果主要聚焦 reasoning/QA，可在 Related Work 中简要提及但不必深入讨论。

He et al. (2024, NAACL Findings) 关于 sequential labeling 的 uncertainty estimation 也相关，应在 §2 第24行（NER uncertainty 段落）补充引用。

---

### Minor Issues

**[AGREE] Abstract 中 "oracle headroom" 无定义**：同意。首次出现时应加括号解释，如 "oracle headroom (the gap between the best achievable selection and greedy decoding)"。

**[AGREE with nuance] 对 Nedellec (2026) 措辞偏 adversarial**：Introduction §1 第16行的三点列举 (i)-(iii) 在技术上是准确的，但在学术语气上确实偏向"building a case against"。建议先肯定 Nedellec et al. 的贡献（如 "corroborating the existence of consistency-accuracy correlations"，这在 Related Work §2 第13行已做到），然后在 Introduction 中用更 neutral 的方式指出 gap（如 "leaving open the questions of..."）。Related Work 的表述相比 Introduction 已经 balanced 得多。

**[AGREE] FK independent raters 假设 justification 不足**：与我的 W3 一致。§3.2 第37行的 one-line justification 不够。

**[AGREE] Table 2 EM omission 需 unique output fraction 数据**：与我的 M3 一致。"probability of two identical structured outputs is negligible" 缺乏经验验证。

---

### Missing References 评估

1. **VerifiNER (Kim et al., ACL 2024)**：高度相关，应引用。提供了 supervised NER verification 的参照点。
2. **RASC (Aggarwal et al., NAACL 2025)**：需确认具体内容。如果是 reasoning-focused，相关性中等（已有类似引用）。
3. **He et al. (2024, NAACL Findings)**：序列标注 uncertainty estimation，与 §2 第24行讨论的 NER uncertainty 直接相关，应引用。

---

### 与我（R1）审稿的交叉对比

两份审稿在以下方面**高度一致**：
- Constrained decoding 对 logprob/diversity 的影响是核心 validity threat（R1-N1 ≈ R2-N2）
- FK 独立性假设 justification 不足（R1-W3 ≈ R2-Minor）
- EM omission 需经验数据支持（R1-M3 ≈ R2-Minor）
- 术语一致性需修复

**分歧点**：
- R2 将 RE 单数据集列为 Must-Fix #1，我将其列为 Should-Fix（因论文已多处 hedge）。但 R2 的 floor effect 分析比我更深入，说服力强。**我倾向于上调此问题的严重性到 borderline Must-Fix**。
- R2 将 Ethics Statement 缺失列为 Must-Fix，我认为 ARR 政策仅 "encourage" 而非 "require"，应降为 Minor。
- R2-W3（ρ-AUROC dissociation 是 expected behavior）是一个我未单独提出的有效观点——论文确实可以更明确地承认其统计预期性。
- R2 未提到我的 N2（failure-to-reject 统计逻辑）和 N3（single-seed），这两个是我认为的核心 soundness 问题。

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

_source line 317 · 2026-05-15T04:08:48.143474+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 318 · 2026-05-15T04:08:50.789815+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心判断总结：

- **R2-N1 (RE 单数据集)**：AGREE，floor effect 分析有说服力，我上调此问题严重性
- **R2-N2 (Logprob 解释缺失)**：AGREE，与我的 N1 (constrained decoding confound) 高度重叠
- **R2-N3 (Ethics Statement)**：REBUT，ARR 仅"encourage"非"require"，应降为 Minor
- **R2-W1–W5**：大部分 AGREE，W2 (SJ 贡献) 部分 REBUT——SJ 价值在于 robustness 而非单点 ρ 增量
- 两份审稿在 constrained decoding、FK 独立性、EM omission 上高度一致；R2 未覆盖我的 N2 (failure-to-reject 逻辑) 和 N3 (single-seed) 问题

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

_source line 319 · 2026-05-15T04:08:55.389726+00:00_

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


## Round 30

## Round 30

6 recorded events


### User

_source line 320 · 2026-05-15T04:09:22.723567+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1

### Must-Fix

[AGREE] R1-N1 (constrained decoding confound): 同意，与我的 N2 一致。补充建议：即使不跑 unconstrained 实验，报告 unique output fraction 和 per-sample logprob variance 也能大幅帮助 disentangle。

[REBUT] R1-N2 (failure to reject ≠ evidence of absence): 统计原理正确，但 6/6 configurations 一致未显著（Table 4），cumulative evidence 远强于单一 test。且 CI 正面端仅 +4.2pp vs 13.2pp oracle headroom，practical significance 有限。建议降为 Should-Fix。

[AGREE] R1-N3 (single seed): 合理关切。但 N=16 3-seed 下 signal rankings 完全一致（Table 3），且 N=8→N=16 ranking 也稳定——ordering 稳定性有保障。建议降为 Should-Fix。

### Should-Fix

[AGREE] R1-W1 (多重比较): SJ-EM CI lower bound +0.003，Bonferroni 下几乎必然不 survive。
[AGREE] R1-W2 (tautological gap): 与我观点一致。4/5 instance-level signals 的 selection 失败是 definitional，真正的 empirical contribution 应聚焦 logprob 失败和 consensus-proximity 局限。
[AGREE] R1-W3 (FK independence): 同意。
[AGREE] R1-W4 (SJ cost function): 同意需补充 maximize/minimize 方向和 unmatched entities 处理。
[AGREE] R1-W5 (cross-model at fixed 8B): 同意。
[AGREE] R1-W6 (consensus-proximity 唯一策略): 强烈同意，这是 R1 最有力的 Should-Fix。MBR decoding 是成熟替代方案，仅测试一种转换策略就声称 "signals fail as selectors" 不充分。

### Minor

[AGREE] R1-M1 (54% vs 51.5%): 数据不一致。
[AGREE] R1-M2 (Table 1 空白): 建议移至 Appendix。
[AGREE] R1-M3 (EM exclusion): 同意需 empirical support。
[AGREE] R1-M4 (LOO-SJ 量纲): 同意表述混淆。
[REBUT] R1-M5 (Figure 1 p=0.39): Overview figure caption 引用 supporting statistic 是常见做法，建议保留但加 "(Table 2)" 交叉引用。
[REBUT] R1-M6 (semantic entropy footnote): 该 footnote 提供重要 calibration context 且已显式 caveat，删除反而让读者缺少 reference point。建议强化 caveat placement 但保留。
[AGREE] R1-M7 (引用格式): 同意。

### Missing References
[AGREE] MBR decoding (Eikema & Aziz 2022; Freitag et al. 2022) — 直接相关 W6，significant gap。
[AGREE] Malinin & Gales (2021) — 相关于 uncertainty estimation。

### 综合评价
R1 的审稿意见质量高，技术判断准确。我们的分歧主要在严重程度而非方向上：
- R1-N2 (statistical logic): 我认为 should-fix 而非 critical，因 6/6 配置一致性提供了 cumulative evidence
- R1-N3 (single seed): 我认为 should-fix 因 ranking stability 有保障
- R1-W6 (MBR alternative): 我认为这是 R1 最有价值的贡献点，论文确实只测了一种 instance-to-sample 转换策略就做了 sweeping claim

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

_source line 321 · 2026-05-15T04:12:48.122708+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues (all resolved)\n  # ============================================================\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B）\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"model-agnostic 与 Limitations 矛盾\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 确认措辞修正到位，无再提\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"新遗漏：Optimal SC, Difficulty-Adaptive SC\"\n    action_items:\n      - round: 1\n        action: \"补充 6 篇引用到 Related Work\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 3\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"需跨数据集验证或降级措辞\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Abstract RE 措辞需修正\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围，gap 的 RE 证据 (-0.9pp, p=0.80) 基础薄弱；R1 交叉回应后上调严重性。建议：(a) 降级 RE claim 为 preliminary evidence, (b) 补 SciERC RE conditional filtering 分析\"\n    action_items:\n      - round: 1\n        action: \"降级措辞 universal → observed in SciERC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"Abstract 改为 NER (three datasets) and RE (SciERC)\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Nedellec 增量贡献论证不足 + 引用错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强增量贡献论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认三点差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams\"\n    action_items: []\n    resolution: \"论文已包含 5 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析 negligible 误导\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8-16× 推理开销不应描述为 negligible\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"互补性已证明但未尝试组合\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Bootstrap 细节不足\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling +0.018 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际为 -0.080\"\n    action_items:\n      - round: 0\n        action: \"修正声明\"\n        assigned_to: \"Main Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues (all resolved)\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 支撑核心结论但细节缺失\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价统计规范达到高标准\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Gap 解释力不足 + logprob 失败未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 定义性 + logprob 机制缺失\"\n    action_items:\n      - round: 1\n        action: \"区分 by-design vs empirical + logprob failure 分析段\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 logprob failure analysis 充分\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 单薄\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"consensus-proximity = LOO-SJ 是表述问题\"\n    action_items:\n      - round: 1\n        action: \"显式说明等价关系\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 consensus-proximity = LOO-SJ 已明确\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec 引用错误 + 增量贡献弱\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Yao vs Nédellec 事实错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"SJ 形式化有歧义\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Hungarian threshold + max denominator 需补充\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\"\n    action_items:\n      - round: 1\n        action: \"补全 Eq(4) 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"补 threshold 说明 + max vs union 设计理由\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Voting-SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"instance-level correlation 未报告\"\n    action_items:\n      - round: 1\n        action: \"报告 Voting-SJ ρ=0.659/0.605\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"中等相关数据已报告\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺 contextualization\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 cross-method footnote\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote: semantic entropy AUROC comparison + cross-task caveat\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"robustness 结论需限定\"\n    action_items:\n      - round: 1\n        action: \"限定为 consistency-based signals robust; logprob uncharacterized\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞限定到位\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 establishing 措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject ≠ accept\"\n    action_items:\n      - round: 1\n        action: \"establishing → consistent with/suggests\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA fine-tuning 状态未说明\"\n    action_items:\n      - round: 1\n        action: \"明确两模型 identical LoRA 配置\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 未再提及\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码 diversity 影响\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展为全局 confound + Limitations 条目\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 新增条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已扩展为全局 confound 讨论\"\n    resolution_round: 2\n\n  - id: \"R1-W8\"\n    summary: \"first systematic 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope\"\n    action_items:\n      - round: 1\n        action: \"first multi-family\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 无再提\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC, Difficulty-Adaptive SC 等\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认无遗漏\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文提及\"\n    action_items:\n      - round: 1\n        action: \"Section 5 简述 + 引导 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 dissociation 分析为 actionable finding\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"展示结果或删除\"\n    action_items:\n      - round: 1\n        action: \"删除提及\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已删除\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"GSM8K +18pp 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"补注 PaLM-540B\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告 CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"within 3-seed σ≈0.007\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 issues (all resolved)\n  # ============================================================\n  - id: \"R2-C1\"\n    summary: \"Selection 证据面过窄——仅 1 dataset × 1 model\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需补 LLaMA SciERC + CoNLL selection\"\n    action_items:\n      - round: 2\n        action: \"补 4 配置 selection 分析 + Appendix Table 6\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"6 configurations 全部补齐，无 signal 显著超越 greedy\"\n    resolution_round: 2\n\n  - id: \"R2-C2\"\n    summary: \"WNUT-17 仅报告 1 个信号\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 signals 中仅 SJ 一个数据点\"\n    action_items:\n      - round: 2\n        action: \"补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\"\n    resolution_round: 2\n\n  - id: \"R2-W1\"\n    summary: \"ρ=0.38 缺 cross-method 对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 footnote 引用 semantic entropy AUROC\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R2-W2\"\n    summary: \"N=8 QE ρ 无 uncertainty\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap CIs\"\n    action_items:\n      - round: 2\n        action: \"计算 B=10,000 bootstrap CI + Appendix 表\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\"\n    resolution_round: 2\n\n  - id: \"R2-W3\"\n    summary: \"SJ Hungarian threshold + max denominator\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"无 threshold 声明需验证\"\n    action_items:\n      - round: 2\n        action: \"代码验证 + method.tex 补充\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\"\n    resolution_round: 2\n\n  - id: \"R2-W4\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap p-value\"\n    action_items:\n      - round: 2\n        action: \"RE bootstrap + 补 p=0.80 到论文\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"RE logprob p=0.80, all signals below greedy\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Constrained decoding 全局 confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展到全局 + Limitations\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已处理\"\n    resolution_round: 2\n\n  - id: \"R2-W6\"\n    summary: \"Abstract RE 措辞误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"NER (three datasets) and RE (SciERC)\"\n    action_items:\n      - round: 2\n        action: \"修正 Abstract\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R2-W7\"\n    summary: \"n=529 vs 551 未解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"22 instances filtering criteria\"\n    action_items:\n      - round: 2\n        action: \"补一句说明\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已说明 gold-empty filtering\"\n    resolution_round: 2\n\n  - id: \"R2-DATA\"\n    summary: \"RE selection 数据矛盾 (Table 2 vs L129)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\"\n    action_items:\n      - round: 2\n        action: \"Agent 确认 Table 2 正确 → Paper Agent 修正 L129\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"L129 统一为 logprob=0.395, -0.9pp, p=0.80\"\n    resolution_round: 2\n\n  - id: \"R2-AUROC\"\n    summary: \"L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"corresponding 暗示同一信号\"\n    action_items:\n      - round: 2\n        action: \"分别标注 Voting ρ 和 EM AUROC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已拆分归属\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 new issues\n  # ============================================================\n  - id: \"R3-C1\"\n    summary: \"Constrained decoding 是 correlation-selection gap 的未控制混淆变量\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均独立提出 (R1-N1, R2-N2)。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。Random baseline gap 仅 3.6pp。win%=46.6% 暗示 logprob variance 极小。\"\n    action_items:\n      - round: 3\n        action: \"报告 unique output fraction + per-sample logprob std distribution；或增加 unconstrained generation 对照；或在 Discussion 中明确 gap 结论的 generalizability boundary 为 constrained decoding regime\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 列 critical, R2 交叉回应降为 should-fix (6/6 配置一致性构成 cumulative evidence, CI 正面端仅 +4.2pp vs 13.2pp oracle headroom)。共识：需修改措辞或补充等价性检验。\"\n    action_items:\n      - round: 3\n        action: \"修改措辞为 'we found no significant evidence that any signal surpasses' + 补 power analysis 或 TOST；或保持 6/6 cumulative evidence 论证但更严谨地表述\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C3\"\n    summary: \"N=8 核心结果 single seed (seed=42)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 列 critical, R2 交叉回应降为 should-fix (N=16 3-seed ranking 完全一致)。Table 1 N=8 和 Table 2 selection 全部 single seed。信号排序差异小 (Voting-SJ Δρ=0.019)。\"\n    action_items:\n      - round: 3\n        action: \"SciERC N=8 补至少 3 seed mean±σ，或在 Limitations 中明确 single-seed 风险并引用 N=16 3-seed 作为间接 stability 证据\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"多重比较校正缺失\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive。需声明未做 correction + 修改 borderline 措辞\"\n    action_items:\n      - round: 3\n        action: \"声明未做多重比较校正 + SJ-EM 从 'Yes†' 改为 'suggestive'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"4/5 信号 instance-level by design, selection 失败是 definitional。真正的 empirical contribution 是 logprob 失败 + consensus-proximity 局限。需在 Discussion 中分离两层论证。\"\n    action_items:\n      - round: 3\n        action: \"Discussion 中明确分离 (1) instance-level 信号的结构性局限 (by construction) 和 (2) logprob 的经验性失败\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 提出, R2 强烈同意。仅测一种转换策略就声称 'signals fail as selectors' 不充分。MBR decoding (Eikema & Aziz 2022, Freitag et al. 2022) 是成熟替代方案但未讨论。\"\n    action_items:\n      - round: 3\n        action: \"(a) 明确 consensus-proximity 与 MBR 联系；(b) 讨论为何其为合理默认 + 替代策略是否可能缩小 gap；(c) 引用 MBR 文献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W4\"\n    summary: \"FK 独立性假设 justification 不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"§3.2 L37 一句 hand-wave。温度采样共享模型参数和 prompt，非独立。需报告 inter-sample correlation 或在 Limitations 讨论。\"\n    action_items:\n      - round: 3\n        action: \"报告 N=8 pairwise correlation 量化独立性偏离，或在 Limitations 明确讨论\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"Cross-model 实为 cross-architecture at fixed 8B scale\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两模型均 8B，'cross-model' 措辞过度外推。应改为 'cross-architecture (at 8B scale)'\"\n    action_items:\n      - round: 3\n        action: \"正文将 cross-model 替换为 cross-architecture 或加限定词\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"'First multi-family comparison' claim scope 过宽\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需限定为 'first comparison spanning structural, surface, and model-internal signal families for both QE and selection in generative structured IE'\"\n    action_items:\n      - round: 3\n        action: \"收窄 Contribution 1 措辞\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"confidence signal vs consistency signal 混用；VC vs Voting Conf. 缩写不统一；LLaMA Factory 未引用\"\n    action_items:\n      - round: 3\n        action: \"统一术语 + 补 LLaMA Factory 引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"VerifiNER (Kim+ ACL2024) 高度相关; MBR decoding (Eikema&Aziz 2022, Freitag+ 2022) 与 consensus-proximity 直接相关; Malinin&Gales (2021) 与 structured prediction uncertainty 相关; He+ (NAACL Findings 2024) 序列标注 uncertainty; RASC 需确认是否与已引 REASC 重复\"\n    action_items:\n      - round: 3\n        action: \"补充引用并在 Related Work 中讨论\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M1\"\n    summary: \"WNUT-17 '54% zero F1' 与 Table 7 数据不一致 (51.5%)\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"355/689 ≈ 51.5% vs 正文 54%\"\n    action_items:\n      - round: 3\n        action: \"核实并统一数字\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M2\"\n    summary: \"EM selection exclusion 缺乏经验支持\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 2 EM omission 理由 'probability negligible' 需报告 exact match pairs 实际频率\"\n    action_items:\n      - round: 3\n        action: \"报告 N=8 中 exact match pairs 频率\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M3\"\n    summary: \"Ethics Statement 缺失\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"R2 列 critical, R1 交叉回应 rebut: ARR 仅 'encouraged' 非 'required'。共识降为 minor。使用公开 benchmark，无人类数据收集风险。\"\n    action_items:\n      - round: 3\n        action: \"添加简短 Ethics Statement (使用公开数据，不涉及人类标注)\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M4\"\n    summary: \"ρ-AUROC dissociation 作为独立发现过度强调\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 提出, R1 partially agree。dissociation 本身 expected，价值在于映射到 IE 实际使用场景。建议承认统计预期性后聚焦实践含义。\"\n    action_items:\n      - round: 3\n        action: \"§4.2 承认 dissociation 的统计预期性，聚焦于 routing/triage 的实践含义\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M5\"\n    summary: \"对 Nedellec (2026) 措辞偏 adversarial\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Introduction §1 (i)-(iii) 技术准确但语气偏向 'building a case against'。建议用 'leaving open the questions of...' 替代\"\n    action_items:\n      - round: 3\n        action: \"Introduction 中 Nedellec 描述改为更 neutral 的语气\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M6\"\n    summary: \"LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"Appendix C Δρ=−0.014 (整体 Spearman) vs per-instance max Δρ=3.1×10⁻⁴ (confidence score?) 量纲不同\"\n    action_items:\n      - round: 3\n        action: \"澄清 per-instance Δρ 具体含义\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M7\"\n    summary: \"Figure 1 caption 引入未直接可视化的 p=0.39\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"R2 交叉回应建议保留但加 '(Table 2)' 交叉引用\"\n    action_items:\n      - round: 3\n        action: \"补 '(Table 2)' 交叉引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues (all resolved)\n  # ============================================================\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B）\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"model-agnostic 与 Limitations 矛盾\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 确认措辞修正到位，无再提\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"新遗漏：Optimal SC, Difficulty-Adaptive SC\"\n    action_items:\n      - round: 1\n        action: \"补充 6 篇引用到 Related Work\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 0\n    last_seen_round: 3\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"需跨数据集验证或降级措辞\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Abstract RE 措辞需修正\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围，gap 的 RE 证据 (-0.9pp, p=0.80) 基础薄弱；R1 交叉回应后上调严重性。建议：(a) 降级 RE claim 为 preliminary evidence, (b) 补 SciERC RE conditional filtering 分析\"\n    action_items:\n      - round: 1\n        action: \"降级措辞 universal → observed in SciERC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"Abstract 改为 NER (three datasets) and RE (SciERC)\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Nedellec 增量贡献论证不足 + 引用错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强增量贡献论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认三点差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams\"\n    action_items: []\n    resolution: \"论文已包含 5 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析 negligible 误导\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8-16× 推理开销不应描述为 negligible\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"互补性已证明但未尝试组合\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Bootstrap 细节不足\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling +0.018 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际为 -0.080\"\n    action_items:\n      - round: 0\n        action: \"修正声明\"\n        assigned_to: \"Main Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues (all resolved)\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 支撑核心结论但细节缺失\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价统计规范达到高标准\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Gap 解释力不足 + logprob 失败未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 定义性 + logprob 机制缺失\"\n    action_items:\n      - round: 1\n        action: \"区分 by-design vs empirical + logprob failure 分析段\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 logprob failure analysis 充分\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 单薄\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"consensus-proximity = LOO-SJ 是表述问题\"\n    action_items:\n      - round: 1\n        action: \"显式说明等价关系\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 consensus-proximity = LOO-SJ 已明确\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec 引用错误 + 增量贡献弱\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Yao vs Nédellec 事实错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"SJ 形式化有歧义\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Hungarian threshold + max denominator 需补充\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\"\n    action_items:\n      - round: 1\n        action: \"补全 Eq(4) 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"补 threshold 说明 + max vs union 设计理由\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Voting-SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"instance-level correlation 未报告\"\n    action_items:\n      - round: 1\n        action: \"报告 Voting-SJ ρ=0.659/0.605\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"中等相关数据已报告\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺 contextualization\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 cross-method footnote\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote: semantic entropy AUROC comparison + cross-task caveat\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"robustness 结论需限定\"\n    action_items:\n      - round: 1\n        action: \"限定为 consistency-based signals robust; logprob uncharacterized\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞限定到位\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 establishing 措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject ≠ accept\"\n    action_items:\n      - round: 1\n        action: \"establishing → consistent with/suggests\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA fine-tuning 状态未说明\"\n    action_items:\n      - round: 1\n        action: \"明确两模型 identical LoRA 配置\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 未再提及\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码 diversity 影响\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展为全局 confound + Limitations 条目\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 新增条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已扩展为全局 confound 讨论\"\n    resolution_round: 2\n\n  - id: \"R1-W8\"\n    summary: \"first systematic 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope\"\n    action_items:\n      - round: 1\n        action: \"first multi-family\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 无再提\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC, Difficulty-Adaptive SC 等\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认无遗漏\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文提及\"\n    action_items:\n      - round: 1\n        action: \"Section 5 简述 + 引导 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 dissociation 分析为 actionable finding\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"展示结果或删除\"\n    action_items:\n      - round: 1\n        action: \"删除提及\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已删除\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"GSM8K +18pp 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"补注 PaLM-540B\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告 CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"within 3-seed σ≈0.007\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 issues (all resolved)\n  # ============================================================\n  - id: \"R2-C1\"\n    summary: \"Selection 证据面过窄——仅 1 dataset × 1 model\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需补 LLaMA SciERC + CoNLL selection\"\n    action_items:\n      - round: 2\n        action: \"补 4 配置 selection 分析 + Appendix Table 6\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"6 configurations 全部补齐，无 signal 显著超越 greedy\"\n    resolution_round: 2\n\n  - id: \"R2-C2\"\n    summary: \"WNUT-17 仅报告 1 个信号\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 signals 中仅 SJ 一个数据点\"\n    action_items:\n      - round: 2\n        action: \"补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\"\n    resolution_round: 2\n\n  - id: \"R2-W1\"\n    summary: \"ρ=0.38 缺 cross-method 对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 footnote 引用 semantic entropy AUROC\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R2-W2\"\n    summary: \"N=8 QE ρ 无 uncertainty\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap CIs\"\n    action_items:\n      - round: 2\n        action: \"计算 B=10,000 bootstrap CI + Appendix 表\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\"\n    resolution_round: 2\n\n  - id: \"R2-W3\"\n    summary: \"SJ Hungarian threshold + max denominator\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"无 threshold 声明需验证\"\n    action_items:\n      - round: 2\n        action: \"代码验证 + method.tex 补充\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\"\n    resolution_round: 2\n\n  - id: \"R2-W4\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap p-value\"\n    action_items:\n      - round: 2\n        action: \"RE bootstrap + 补 p=0.80 到论文\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"RE logprob p=0.80, all signals below greedy\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Constrained decoding 全局 confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展到全局 + Limitations\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已处理\"\n    resolution_round: 2\n\n  - id: \"R2-W6\"\n    summary: \"Abstract RE 措辞误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"NER (three datasets) and RE (SciERC)\"\n    action_items:\n      - round: 2\n        action: \"修正 Abstract\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R2-W7\"\n    summary: \"n=529 vs 551 未解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"22 instances filtering criteria\"\n    action_items:\n      - round: 2\n        action: \"补一句说明\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已说明 gold-empty filtering\"\n    resolution_round: 2\n\n  - id: \"R2-DATA\"\n    summary: \"RE selection 数据矛盾 (Table 2 vs L129)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\"\n    action_items:\n      - round: 2\n        action: \"Agent 确认 Table 2 正确 → Paper Agent 修正 L129\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"L129 统一为 logprob=0.395, -0.9pp, p=0.80\"\n    resolution_round: 2\n\n  - id: \"R2-AUROC\"\n    summary: \"L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"corresponding 暗示同一信号\"\n    action_items:\n      - round: 2\n        action: \"分别标注 Voting ρ 和 EM AUROC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已拆分归属\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 new issues\n  # ============================================================\n  - id: \"R3-C1\"\n    summary: \"Constrained decoding 是 correlation-selection gap 的未控制混淆变量\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均独立提出 (R1-N1, R2-N2)。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。Random baseline gap 仅 3.6pp。win%=46.6% 暗示 logprob variance 极小。\"\n    action_items:\n      - round: 3\n        action: \"报告 unique output fraction + per-sample logprob std distribution；或增加 unconstrained generation 对照；或在 Discussion 中明确 gap 结论的 generalizability boundary 为 constrained decoding regime\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 列 critical, R2 交叉回应降为 should-fix (6/6 配置一致性构成 cumulative evidence, CI 正面端仅 +4.2pp vs 13.2pp oracle headroom)。共识：需修改措辞或补充等价性检验。\"\n    action_items:\n      - round: 3\n        action: \"修改措辞为 'we found no significant evidence that any signal surpasses' + 补 power analysis 或 TOST；或保持 6/6 cumulative evidence 论证但更严谨地表述\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C3\"\n    summary: \"N=8 核心结果 single seed (seed=42)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 列 critical, R2 交叉回应降为 should-fix (N=16 3-seed ranking 完全一致)。Table 1 N=8 和 Table 2 selection 全部 single seed。信号排序差异小 (Voting-SJ Δρ=0.019)。\"\n    action_items:\n      - round: 3\n        action: \"SciERC N=8 补至少 3 seed mean±σ，或在 Limitations 中明确 single-seed 风险并引用 N=16 3-seed 作为间接 stability 证据\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"多重比较校正缺失\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive。需声明未做 correction + 修改 borderline 措辞\"\n    action_items:\n      - round: 3\n        action: \"声明未做多重比较校正 + SJ-EM 从 'Yes†' 改为 'suggestive'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"4/5 信号 instance-level by design, selection 失败是 definitional。真正的 empirical contribution 是 logprob 失败 + consensus-proximity 局限。需在 Discussion 中分离两层论证。\"\n    action_items:\n      - round: 3\n        action: \"Discussion 中明确分离 (1) instance-level 信号的结构性局限 (by construction) 和 (2) logprob 的经验性失败\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 提出, R2 强烈同意。仅测一种转换策略就声称 'signals fail as selectors' 不充分。MBR decoding (Eikema & Aziz 2022, Freitag et al. 2022) 是成熟替代方案但未讨论。\"\n    action_items:\n      - round: 3\n        action: \"(a) 明确 consensus-proximity 与 MBR 联系；(b) 讨论为何其为合理默认 + 替代策略是否可能缩小 gap；(c) 引用 MBR 文献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W4\"\n    summary: \"FK 独立性假设 justification 不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"§3.2 L37 一句 hand-wave。温度采样共享模型参数和 prompt，非独立。需报告 inter-sample correlation 或在 Limitations 讨论。\"\n    action_items:\n      - round: 3\n        action: \"报告 N=8 pairwise correlation 量化独立性偏离，或在 Limitations 明确讨论\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"Cross-model 实为 cross-architecture at fixed 8B scale\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两模型均 8B，'cross-model' 措辞过度外推。应改为 'cross-architecture (at 8B scale)'\"\n    action_items:\n      - round: 3\n        action: \"正文将 cross-model 替换为 cross-architecture 或加限定词\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"'First multi-family comparison' claim scope 过宽\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需限定为 'first comparison spanning structural, surface, and model-internal signal families for both QE and selection in generative structured IE'\"\n    action_items:\n      - round: 3\n        action: \"收窄 Contribution 1 措辞\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"confidence signal vs consistency signal 混用；VC vs Voting Conf. 缩写不统一；LLaMA Factory 未引用\"\n    action_items:\n      - round: 3\n        action: \"统一术语 + 补 LLaMA Factory 引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"VerifiNER (Kim+ ACL2024) 高度相关; MBR decoding (Eikema&Aziz 2022, Freitag+ 2022) 与 consensus-proximity 直接相关; Malinin&Gales (2021) 与 structured prediction uncertainty 相关; He+ (NAACL Findings 2024) 序列标注 uncertainty; RASC 需确认是否与已引 REASC 重复\"\n    action_items:\n      - round: 3\n        action: \"补充引用并在 Related Work 中讨论\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M1\"\n    summary: \"WNUT-17 '54% zero F1' 与 Table 7 数据不一致 (51.5%)\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"355/689 ≈ 51.5% vs 正文 54%\"\n    action_items:\n      - round: 3\n        action: \"核实并统一数字\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M2\"\n    summary: \"EM selection exclusion 缺乏经验支持\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 2 EM omission 理由 'probability negligible' 需报告 exact match pairs 实际频率\"\n    action_items:\n      - round: 3\n        action: \"报告 N=8 中 exact match pairs 频率\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M3\"\n    summary: \"Ethics Statement 缺失\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"R2 列 critical, R1 交叉回应 rebut: ARR 仅 'encouraged' 非 'required'。共识降为 minor。使用公开 benchmark，无人类数据收集风险。\"\n    action_items:\n      - round: 3\n        action: \"添加简短 Ethics Statement (使用公开数据，不涉及人类标注)\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M4\"\n    summary: \"ρ-AUROC dissociation 作为独立发现过度强调\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 提出, R1 partially agree。dissociation 本身 expected，价值在于映射到 IE 实际使用场景。建议承认统计预期性后聚焦实践含义。\"\n    action_items:\n      - round: 3\n        action: \"§4.2 承认 dissociation 的统计预期性，聚焦于 routing/triage 的实践含义\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M5\"\n    summary: \"对 Nedellec (2026) 措辞偏 adversarial\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Introduction §1 (i)-(iii) 技术准确但语气偏向 'building a case against'。建议用 'leaving open the questions of...' 替代\"\n    action_items:\n      - round: 3\n        action: \"Introduction 中 Nedellec 描述改为更 neutral 的语气\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M6\"\n    summary: \"LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"Appendix C Δρ=−0.014 (整体 Spearman) vs per-instance max Δρ=3.1×10⁻⁴ (confidence score?) 量纲不同\"\n    action_items:\n      - round: 3\n        action: \"澄清 per-instance Δρ 具体含义\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M7\"\n    summary: \"Figure 1 caption 引入未直接可视化的 p=0.39\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"R2 交叉回应建议保留但加 '(Table 2)' 交叉引用\"\n    action_items:\n      - round: 3\n        action: \"补 '(Table 2)' 交叉引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 322 · 2026-05-15T04:12:48.225510+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 29282}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 323 · 2026-05-15T04:14:58.292418+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告 — Round 3\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT） → 收敛汇总\n\n---\n\n## Summary\n\n本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。在 SciERC、CoNLL-2003、WNUT-17 三个数据集和两个 8B 模型（Qwen3-8B, LLaMA-3.1-8B）上实验。核心发现是 \"correlation-selection gap\"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。\n\n---\n\n## Strengths\n\n**S1. 问题分解有真正洞察力。** 将 quality estimation 与 sample selection 明确区分为两个独立目标，用不同指标分别评估（Spearman ρ + AUROC vs. best-of-N F1）。Per-sample vs. instance-level 信号的形式化区分使分析逻辑链条清晰可追溯。这一分析框架本身是对现有文献的有价值贡献。[R1-S1, R2-S1 一致]\n\n**S2. 统计报告全面严谨。** Paired bootstrap (B=10,000) 附带 95% CI、Cohen's d、sign test win%、pairwise Δρ CI（Appendix D），多数实证论文不会做到这个粒度。[R1-S2, R2-S2 一致]\n\n**S3. WNUT-17 capability boundary 分析揭示重要方法论警示。** Voting ρ=0.724（full-set）→ conditional ρ=0.038 (n.s.) 揭示 inflated correlation 由 zero/non-zero boundary 驱动；logprob 条件反转（full ρ=−0.410 → conditional ρ=0.350）进一步确认此现象。[R1-S4, R2-S3 一致]\n\n**S4. 负面结果处理诚实平衡。** RE 单数据集局限在 Introduction、Discussion、Conclusion、Limitations 四处明确提及。WNUT-17 作为方法边界坦率报告。Limitations section 全面覆盖多项局限。[R1-S3, R2-S4 一致]\n\n**S5. Task difficulty 分析有实用价值。** EM 在简单任务领先 vs. SJ/Voting 在复杂任务领先的 crossover 发现，以及 conditional filtering 后信号排序翻转，为从业者信号选择提供实用指导。[R1-S4]\n\n**S6. Robustness 覆盖面广。** Temperature (T=0.7/1.0)、N-scaling (8→16)、cross-architecture 均有系统分析。[R2-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[Critical] W-C1: Constrained decoding 是 correlation-selection gap 的未控制混淆变量**\n- 两位 Reviewer 独立提出（R1-N1, R2-N2），交叉回应后完全共识\n- 论文核心发现 \"no signal reliably surpasses greedy\" 可能部分是 Outlines/vLLM constrained decoding 压缩 per-sample diversity 的产物，而非置信度信号本身的固有局限\n- Random baseline gap 仅 3.6pp，可能远低于 unconstrained generation 的 variance\n- §5 Discussion 已承认此问题但仅作 future work 提及，未设计任何对照或量化分析\n- 75% of logprob comparisons 为 effective ties (win%=46.6%) 暗示 per-sample variance 极小\n- **建议**：(a) 报告 unique output fraction + per-sample logprob std 分布量化实际 diversity；(b) 增加 unconstrained generation + post-hoc parsing 对照；或 (c) 至少明确 gap 结论的 generalizability boundary 为 constrained decoding regime，在 Abstract/Conclusion 中限定\n\n### Should-Fix（影响评分）\n\n**[Warning] W-S1: RE 结论建立在单一 benchmark 上且受严重 floor effect 影响**\n- R2 独立提出(N1)，R1 交叉回应后上调严重性至 borderline Must-Fix\n- SciERC RE 44% zero F1 严重压缩信号可区分范围，RE gap 证据（−0.9pp, p=0.80）统计说服力弱\n- 论文已在 4 处 hedge（Round 2 修正），但仍在 Abstract 和 Contribution 中以 \"NER and RE\" 并列呈现，给人 RE 证据与 NER 等量齐观的印象\n- **建议**：(a) 进一步降级 RE claim 为 \"preliminary RE evidence on SciERC\"；(b) 补 SciERC RE conditional filtering 分析量化 floor effect 影响\n\n**[Warning] W-S2: Selection gap 统计论证不完整——failure to reject ≠ evidence of absence**\n- R1 列 critical(N2)，R2 交叉回应降为 should-fix（6/6 配置一致性构成 cumulative evidence，CI 正面端 +4.2pp vs 13.2pp oracle headroom 实际意义有限）\n- 共识：措辞需更严谨。p>0.39 只是 absence of evidence\n- **建议**：修改为 \"we found no significant evidence that any signal surpasses greedy\" + 补充 power analysis 或 TOST 等价性检验\n\n**[Warning] W-S3: N=8 核心结果 single seed (seed=42)**\n- R1 列 critical(N3)，R2 交叉回应降为 should-fix（N=16 3-seed ranking 完全一致）\n- Table 1 N=8 和 Table 2 selection 全部基于单一 seed，信号排序差异小（Voting-SJ Δρ=0.019）\n- **建议**：SciERC N=8 补至少 3 seed mean±σ，或在 Limitations 明确 single-seed 风险并引用 N=16 stability\n\n**[Warning] W-S4: Gap 概念部分 tautological**\n- R1(W2) 和 R2 交叉回应均认同：4/5 instance-level 信号 by design 无法 per-sample 区分，selection 失败是定义必然\n- 真正的 empirical contribution 是 (1) logprob（唯一 per-sample 信号）也失败，(2) consensus-proximity 转换策略未能弥合 gap\n- **建议**：Discussion 中明确分离两层论证——结构性局限 (by construction) vs. 经验性失败 (logprob + consensus-proximity)\n\n**[Warning] W-S5: Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系**\n- R1(W6) 提出，R2 强烈同意——\"R1 最有力的 Should-Fix\"\n- 仅测一种转换策略就声称 \"signals fail as selectors\" 不充分\n- MBR decoding (Eikema & Aziz 2022, Freitag et al. 2022) 是成熟替代方案但未讨论\n- **建议**：(a) 明确 consensus-proximity 与 MBR 等价性；(b) 讨论替代策略是否可能缩小 gap；(c) 补引 MBR 文献\n\n**[Warning] W-S6: 多重比较校正缺失**\n- 两位 Reviewer 一致。SJ–EM CI lower bound +0.003，Bonferroni 下几乎必然不 survive\n- **建议**：声明未做校正 + \"Yes†\" 改为 \"suggestive\"\n\n**[Warning] W-S7: FK 独立性假设 justification 不足**\n- 两位 Reviewer 一致。§3.2 一句 hand-wave 不够\n- **建议**：报告 inter-sample correlation 或在 Limitations 明确讨论\n\n**[Warning] W-S8: Cross-model 措辞过度外推**\n- 两位 Reviewer 一致。两模型均 8B，应为 \"cross-architecture at 8B scale\"\n- **建议**：正文加限定词\n\n**[Warning] W-S9: \"First multi-family comparison\" claim scope 过宽**\n- 两位 Reviewer 一致。应限定为 \"for both QE and selection in generative structured IE\"\n\n**[Warning] W-S10: 遗漏引用**\n- VerifiNER (Kim et al., ACL 2024)——supervised NER verification 参照点\n- MBR decoding (Eikema & Aziz 2022; Freitag et al. 2022)——与 consensus-proximity 直接相关\n- Malinin & Gales (2021)——structured prediction uncertainty\n- He et al. (NAACL Findings 2024)——sequential labeling uncertainty\n- RASC (Aggarwal et al., NAACL 2025)——需确认是否与已引 REASC 重复\n\n**[Warning] W-S11: 术语不一致**\n- \"confidence signal\" vs \"consistency signal\" 混用；\"VC\" vs \"Voting Conf.\" 缩写不统一；LLaMA Factory 未引用\n\n### Minor Issues\n\n**[Info] W-M1**: WNUT-17 \"54% zero F1\"（§4.1）vs Table 7 显示 355/689 ≈ 51.5%，数据不一致\n**[Info] W-M2**: EM selection exclusion (Table 2) 理由 \"probability negligible\" 需报告 exact match pairs 实际频率\n**[Info] W-M3**: Ethics Statement 缺失——ARR 仅 \"encouraged\" 非 \"required\"（R1 rebut R2），但添加简短声明为 good practice\n**[Info] W-M4**: ρ–AUROC dissociation 作为独立发现过度强调——dissociation 本身 expected，应承认统计预期性后聚焦实践含义\n**[Info] W-M5**: 对 Nedellec (2026) Introduction 措辞偏 adversarial，建议改为更 neutral 语气\n**[Info] W-M6**: LOO-SJ 验证中 Δρ=−0.014（整体 Spearman）和 per-instance max Δρ=3.1×10⁻⁴ 量纲不同，需澄清\n**[Info] W-M7**: Figure 1 caption 引入 p=0.39（来自 Table 2），建议补 \"(Table 2)\" 交叉引用\n**[Info] W-M8**: SJ Hungarian matching cost function 未明确 maximize/minimize 方向和 zero-IoU pairs 处理\n**[Info] W-M9**: Table 1 N=16 区域大面积空白，建议补交叉引用或考虑合并呈现\n**[Info] W-M10**: Semantic entropy footnote 比较（§4.2）既承认不可比又给出数字，R1 建议删除，R2 建议保留但强化 caveat——共识为保留并强化 caveat placement\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Constrained decoding 是核心 validity threat**：gap 可能部分是实验设置 artifact 而非信号固有局限 [R1-N1 = R2-N2, 完全共识]\n2. **RE 证据薄弱**：44% zero-F1 + 单数据集使 RE claim 基础不稳 [R2-N1, R1 交叉后上调]\n3. **Gap 概念需分层论证**：instance-level 信号的 definitional limitation 与 logprob 的 empirical failure 应分开论述 [R1-W2 = R2 agree]\n4. **Consensus-proximity 需与 MBR 建立联系**：单一转换策略不足以支撑 sweeping claim [R1-W6, R2 强烈同意]\n5. **统计报告整体质量高**但有特定 gaps：单 seed、缺多重比较声明、failure-to-reject 措辞 [双方一致]\n6. **写作质量好**，叙事连贯，负面结果处理诚实 [双方一致]\n\n## Reviewer Divergence [REBUT]\n\n1. **Ethics Statement 严重性**：R2 列 critical → R1 rebut（ARR 仅 encouraged）→ **共识降为 Minor**\n2. **Failure-to-reject 统计逻辑**：R1 列 critical → R2 降为 should-fix（6/6 cumulative evidence）→ **共识降为 Warning**\n3. **Single seed**：R1 列 critical → R2 降为 should-fix（N=16 ranking stability）→ **共识降为 Warning**\n4. **SJ 增量贡献**：R2 认为 borderline → R1 部分 rebut（SJ 价值在 temperature/N-scaling robustness 而非单点 ρ 增量）→ **共识为 SJ 论文措辞应强调 robustness**\n5. **Semantic entropy footnote**：R1 建议删除 → R2 建议保留强化 caveat → **共识为保留但强化**\n\n---\n\n## Questions to Authors\n\n1. 是否考虑过 unconstrained generation 对照？即使 parse 成功率低，比较两种 regime 下 pairwise SJ 分布也能 calibrate gap 的 generalizability。\n2. Logprob 在 WNUT conditional set 达所有信号最高 ρ=0.350（Table 7），如何 reconcile 主文中 \"logprob 最弱\" 叙述？是否暗示 logprob 在高 diversity 场景有独特优势？\n3. LoRA rank=32 是否影响 sample diversity？更低 rank 可能增加 diversity。\n4. N=16 selection 结果有无 multi-seed bootstrap p-value？\n5. SciERC RE conditional filtering 分析（非零 F1 子集）的 gap 结论是否改变？\n\n---\n\n## Missing References\n\n1. Eikema & Aziz (2022) \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for NMT\" — MBR decoding 理论框架，与 consensus-proximity 直接相关\n2. Freitag et al. (2022) \"High Quality Rather Than High Model Probability\" — MBR decoding\n3. Kim et al. (2024) \"VerifiNER\" — ACL 2024, supervised NER verification\n4. Malinin & Gales (2021) \"Uncertainty Estimation in Autoregressive Structured Prediction\"\n5. He et al. (2024) \"Uncertainty Estimation on Sequential Labeling\" — NAACL Findings 2024\n6. Aggarwal et al. (2025) \"Reasoning Aware Self-Consistency\" — NAACL 2025 (需确认与已引 REASC 是否重复)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）\n\n---\n\n## Overall Assessment\n\n**Overall Score: borderline (Findings track)**\n**Confidence: 4/5**\n\n**判断依据**：\n\n论文在 quality estimation vs. sample selection 的问题分解上有真正贡献，correlation-selection gap 作为概念有实用价值，统计报告质量在 empirical NLP 论文中属上乘，WNUT-17 capability boundary 分析提供了重要方法论警示。\n\n但一个 critical 问题（constrained decoding confound）对核心 claim 构成 validity threat——如果 gap 主要由实验设置的 diversity 压缩导致，则核心贡献的 generalizability 受限。7 个 warning 级别问题（RE 单数据集、statistical logic、single seed、gap tautological 成分、MBR 联系缺失、多重比较、FK 独立性）共同表明论文在 soundness 和 framing 上仍有显著改进空间。\n\n两位 Reviewer 独立给出 3/5 (Findings) 评分，交叉回应后评分维持不变。论文方法论严谨的核心质量使其适合 Findings track，但 constrained decoding confound 未解决前不建议 Main Conference。\n\n**修订优先级**（按影响排序）：\n1. **[Must]** Constrained decoding diversity 量化或对照实验（决定核心 claim 是否成立）\n2. **[Should]** RE claim 降级 + conditional analysis（减少过度泛化风险）\n3. **[Should]** Selection gap 措辞修正 + power analysis（统计严谨性）\n4. **[Should]** Gap 论证分层 + MBR 联系（概念清晰度）\n5. **[Should]** Multi-seed 验证或 Limitations 声明（可靠性）\n6. **[Minor]** 术语统一、引用补充、数据一致性修正\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"NER (three datasets of varying difficulty) and RE (SciERC)\" 区分到位（Round 2 修正有效）\n- \"oracle headroom\" 首次出现无定义，建议加括号解释\n- \"no signal reliably surpasses greedy\" 措辞需修改为更严谨的统计表述\n\n### Introduction\n- Quality estimation vs. sample selection 的分离框架论述清晰\n- 对 Nedellec (2026) 的 (i)-(iii) 列举技术准确但语气偏 adversarial\n- \"First multi-family comparison\" 需收窄 scope\n\n### Method (§3)\n- Per-sample vs. instance-level 形式化清晰（Eq. 1-7）\n- SJ Eq. 4: Hungarian matching 优化目标和 zero-IoU pairs 处理需补充\n- FK §3.2: 独立性假设 one-line justification 不充分\n- Consensus-proximity (§3.3): 未与 MBR decoding 建立联系\n\n### Experiments (§4)\n- Quality estimation (§4.2): 数据全面，task difficulty crossover 有洞察力\n- WNUT-17 conditional 分析揭示重要 artifact（Table 7）\n- Selection gap (§4.3): 统计报告详实但 failure-to-reject 逻辑需修正\n- Robustness (§4.4): temperature/N-scaling 分析系统性好，SJ stability 值得突出\n\n### Discussion (§5)\n- Practical recommendations 具体可行\n- \"Why logprob fails\" 段落是关键改进方向——需更多实证支持\n- Constrained decoding 讨论需从 \"future work\" 升级为当前 limitation 的核心分析\n- Gap 论证应分层：definitional (instance-level) vs. empirical (logprob + consensus-proximity)\n\n### Conclusion (§6)\n- 三项 anchoring findings 总结准确\n- RE hedging 到位但仍可进一步降级\n\n### Limitations\n- 覆盖面广且诚实\n- 建议新增：(a) constrained decoding 对 diversity 的影响作为 explicit limitation 条目；(b) single-seed 风险\n\n### Appendix\n- Bootstrap CI 表 (Table 8) 有价值\n- WNUT-17 全信号表 (Table 7) 补充到位\n- Cross-configuration selection (Table 6) 增强了 gap 证据面",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
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
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告 — Round 3\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT） → 收敛汇总\n\n---\n\n## Summary\n\n本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。在 SciERC、CoNLL-2003、WNUT-17 三个数据集和两个 8B 模型（Qwen3-8B, LLaMA-3.1-8B）上实验。核心发现是 \"correlation-selection gap\"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。\n\n---\n\n## Strengths\n\n**S1. 问题分解有真正洞察力。** 将 quality estimation 与 sample selection 明确区分为两个独立目标，用不同指标分别评估（Spearman ρ + AUROC vs. best-of-N F1）。Per-sample vs. instance-level 信号的形式化区分使分析逻辑链条清晰可追溯。这一分析框架本身是对现有文献的有价值贡献。[R1-S1, R2-S1 一致]\n\n**S2. 统计报告全面严谨。** Paired bootstrap (B=10,000) 附带 95% CI、Cohen's d、sign test win%、pairwise Δρ CI（Appendix D），多数实证论文不会做到这个粒度。[R1-S2, R2-S2 一致]\n\n**S3. WNUT-17 capability boundary 分析揭示重要方法论警示。** Voting ρ=0.724（full-set）→ conditional ρ=0.038 (n.s.) 揭示 inflated correlation 由 zero/non-zero boundary 驱动；logprob 条件反转（full ρ=−0.410 → conditional ρ=0.350）进一步确认此现象。[R1-S4, R2-S3 一致]\n\n**S4. 负面结果处理诚实平衡。** RE 单数据集局限在 Introduction、Discussion、Conclusion、Limitations 四处明确提及。WNUT-17 作为方法边界坦率报告。Limitations section 全面覆盖多项局限。[R1-S3, R2-S4 一致]\n\n**S5. Task difficulty 分析有实用价值。** EM 在简单任务领先 vs. SJ/Voting 在复杂任务领先的 crossover 发现，以及 conditional filtering 后信号排序翻转，为从业者信号选择提供实用指导。[R1-S4]\n\n**S6. Robustness 覆盖面广。** Temperature (T=0.7/1.0)、N-scaling (8→16)、cross-architecture 均有系统分析。[R2-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[Critical] W-C1: Constrained decoding 是 correlation-selection gap 的未控制混淆变量**\n- 两位 Reviewer 独立提出（R1-N1, R2-N2），交叉回应后完全共识\n- 论文核心发现 \"no signal reliably surpasses greedy\" 可能部分是 Outlines/vLLM constrained decoding 压缩 per-sample diversity 的产物，而非置信度信号本身的固有局限\n- Random baseline gap 仅 3.6pp，可能远低于 unconstrained generation 的 variance\n- §5 Discussion 已承认此问题但仅作 future work 提及，未设计任何对照或量化分析\n- 75% of logprob comparisons 为 effective ties (win%=46.6%) 暗示 per-sample variance 极小\n- **建议**：(a) 报告 unique output fraction + per-sample logprob std 分布量化实际 diversity；(b) 增加 unconstrained generation + post-hoc parsing 对照；或 (c) 至少明确 gap 结论的 generalizability boundary 为 constrained decoding regime，在 Abstract/Conclusion 中限定\n\n### Should-Fix（影响评分）\n\n**[Warning] W-S1: RE 结论建立在单一 benchmark 上且受严重 floor effect 影响**\n- R2 独立提出(N1)，R1 交叉回应后上调严重性至 borderline Must-Fix\n- SciERC RE 44% zero F1 严重压缩信号可区分范围，RE gap 证据（−0.9pp, p=0.80）统计说服力弱\n- 论文已在 4 处 hedge（Round 2 修正），但仍在 Abstract 和 Contribution 中以 \"NER and RE\" 并列呈现，给人 RE 证据与 NER 等量齐观的印象\n- **建议**：(a) 进一步降级 RE claim 为 \"preliminary RE evidence on SciERC\"；(b) 补 SciERC RE conditional filtering 分析量化 floor effect 影响\n\n**[Warning] W-S2: Selection gap 统计论证不完整——failure to reject ≠ evidence of absence**\n- R1 列 critical(N2)，R2 交叉回应降为 should-fix（6/6 配置一致性构成 cumulative evidence，CI 正面端 +4.2pp vs 13.2pp oracle headroom 实际意义有限）\n- 共识：措辞需更严谨。p>0.39 只是 absence of evidence\n- **建议**：修改为 \"we found no significant evidence that any signal surpasses greedy\" + 补充 power analysis 或 TOST 等价性检验\n\n**[Warning] W-S3: N=8 核心结果 single seed (seed=42)**\n- R1 列 critical(N3)，R2 交叉回应降为 should-fix（N=16 3-seed ranking 完全一致）\n- Table 1 N=8 和 Table 2 selection 全部基于单一 seed，信号排序差异小（Voting-SJ Δρ=0.019）\n- **建议**：SciERC N=8 补至少 3 seed mean±σ，或在 Limitations 明确 single-seed 风险并引用 N=16 stability\n\n**[Warning] W-S4: Gap 概念部分 tautological**\n- R1(W2) 和 R2 交叉回应均认同：4/5 instance-level 信号 by design 无法 per-sample 区分，selection 失败是定义必然\n- 真正的 empirical contribution 是 (1) logprob（唯一 per-sample 信号）也失败，(2) consensus-proximity 转换策略未能弥合 gap\n- **建议**：Discussion 中明确分离两层论证——结构性局限 (by construction) vs. 经验性失败 (logprob + consensus-proximity)\n\n**[Warning] W-S5: Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系**\n- R1(W6) 提出，R2 强烈同意——\"R1 最有力的 Should-Fix\"\n- 仅测一种转换策略就声称 \"signals fail as selectors\" 不充分\n- MBR decoding (Eikema & Aziz 2022, Freitag et al. 2022) 是成熟替代方案但未讨论\n- **建议**：(a) 明确 consensus-proximity 与 MBR 等价性；(b) 讨论替代策略是否可能缩小 gap；(c) 补引 MBR 文献\n\n**[Warning] W-S6: 多重比较校正缺失**\n- 两位 Reviewer 一致。SJ–EM CI lower bound +0.003，Bonferroni 下几乎必然不 survive\n- **建议**：声明未做校正 + \"Yes†\" 改为 \"suggestive\"\n\n**[Warning] W-S7: FK 独立性假设 justification 不足**\n- 两位 Reviewer 一致。§3.2 一句 hand-wave 不够\n- **建议**：报告 inter-sample correlation 或在 Limitations 明确讨论\n\n**[Warning] W-S8: Cross-model 措辞过度外推**\n- 两位 Reviewer 一致。两模型均 8B，应为 \"cross-architecture at 8B scale\"\n- **建议**：正文加限定词\n\n**[Warning] W-S9: \"First multi-family comparison\" claim scope 过宽**\n- 两位 Reviewer 一致。应限定为 \"for both QE and selection in generative structured IE\"\n\n**[Warning] W-S10: 遗漏引用**\n- VerifiNER (Kim et al., ACL 2024)——supervised NER verification 参照点\n- MBR decoding (Eikema & Aziz 2022; Freitag et al. 2022)——与 consensus-proximity 直接相关\n- Malinin & Gales (2021)——structured prediction uncertainty\n- He et al. (NAACL Findings 2024)——sequential labeling uncertainty\n- RASC (Aggarwal et al., NAACL 2025)——需确认是否与已引 REASC 重复\n\n**[Warning] W-S11: 术语不一致**\n- \"confidence signal\" vs \"consistency signal\" 混用；\"VC\" vs \"Voting Conf.\" 缩写不统一；LLaMA Factory 未引用\n\n### Minor Issues\n\n**[Info] W-M1**: WNUT-17 \"54% zero F1\"（§4.1）vs Table 7 显示 355/689 ≈ 51.5%，数据不一致\n**[Info] W-M2**: EM selection exclusion (Table 2) 理由 \"probability negligible\" 需报告 exact match pairs 实际频率\n**[Info] W-M3**: Ethics Statement 缺失——ARR 仅 \"encouraged\" 非 \"required\"（R1 rebut R2），但添加简短声明为 good practice\n**[Info] W-M4**: ρ–AUROC dissociation 作为独立发现过度强调——dissociation 本身 expected，应承认统计预期性后聚焦实践含义\n**[Info] W-M5**: 对 Nedellec (2026) Introduction 措辞偏 adversarial，建议改为更 neutral 语气\n**[Info] W-M6**: LOO-SJ 验证中 Δρ=−0.014（整体 Spearman）和 per-instance max Δρ=3.1×10⁻⁴ 量纲不同，需澄清\n**[Info] W-M7**: Figure 1 caption 引入 p=0.39（来自 Table 2），建议补 \"(Table 2)\" 交叉引用\n**[Info] W-M8**: SJ Hungarian matching cost function 未明确 maximize/minimize 方向和 zero-IoU pairs 处理\n**[Info] W-M9**: Table 1 N=16 区域大面积空白，建议补交叉引用或考虑合并呈现\n**[Info] W-M10**: Semantic entropy footnote 比较（§4.2）既承认不可比又给出数字，R1 建议删除，R2 建议保留但强化 caveat——共识为保留并强化 caveat placement\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Constrained decoding 是核心 validity threat**：gap 可能部分是实验设置 artifact 而非信号固有局限 [R1-N1 = R2-N2, 完全共识]\n2. **RE 证据薄弱**：44% zero-F1 + 单数据集使 RE claim 基础不稳 [R2-N1, R1 交叉后上调]\n3. **Gap 概念需分层论证**：instance-level 信号的 definitional limitation 与 logprob 的 empirical failure 应分开论述 [R1-W2 = R2 agree]\n4. **Consensus-proximity 需与 MBR 建立联系**：单一转换策略不足以支撑 sweeping claim [R1-W6, R2 强烈同意]\n5. **统计报告整体质量高**但有特定 gaps：单 seed、缺多重比较声明、failure-to-reject 措辞 [双方一致]\n6. **写作质量好**，叙事连贯，负面结果处理诚实 [双方一致]\n\n## Reviewer Divergence [REBUT]\n\n1. **Ethics Statement 严重性**：R2 列 critical → R1 rebut（ARR 仅 encouraged）→ **共识降为 Minor**\n2. **Failure-to-reject 统计逻辑**：R1 列 critical → R2 降为 should-fix（6/6 cumulative evidence）→ **共识降为 Warning**\n3. **Single seed**：R1 列 critical → R2 降为 should-fix（N=16 ranking stability）→ **共识降为 Warning**\n4. **SJ 增量贡献**：R2 认为 borderline → R1 部分 rebut（SJ 价值在 temperature/N-scaling robustness 而非单点 ρ 增量）→ **共识为 SJ 论文措辞应强调 robustness**\n5. **Semantic entropy footnote**：R1 建议删除 → R2 建议保留强化 caveat → **共识为保留但强化**\n\n---\n\n## Questions to Authors\n\n1. 是否考虑过 unconstrained generation 对照？即使 parse 成功率低，比较两种 regime 下 pairwise SJ 分布也能 calibrate gap 的 generalizability。\n2. Logprob 在 WNUT conditional set 达所有信号最高 ρ=0.350（Table 7），如何 reconcile 主文中 \"logprob 最弱\" 叙述？是否暗示 logprob 在高 diversity 场景有独特优势？\n3. LoRA rank=32 是否影响 sample diversity？更低 rank 可能增加 diversity。\n4. N=16 selection 结果有无 multi-seed bootstrap p-value？\n5. SciERC RE conditional filtering 分析（非零 F1 子集）的 gap 结论是否改变？\n\n---\n\n## Missing References\n\n1. Eikema & Aziz (2022) \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for NMT\" — MBR decoding 理论框架，与 consensus-proximity 直接相关\n2. Freitag et al. (2022) \"High Quality Rather Than High Model Probability\" — MBR decoding\n3. Kim et al. (2024) \"VerifiNER\" — ACL 2024, supervised NER verification\n4. Malinin & Gales (2021) \"Uncertainty Estimation in Autoregressive Structured Prediction\"\n5. He et al. (2024) \"Uncertainty Estimation on Sequential Labeling\" — NAACL Findings 2024\n6. Aggarwal et al. (2025) \"Reasoning Aware Self-Consistency\" — NAACL 2025 (需确认与已引 REASC 是否重复)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）\n\n---\n\n## Overall Assessment\n\n**Overall Score: borderline (Findings track)**\n**Confidence: 4/5**\n\n**判断依据**：\n\n论文在 quality estimation vs. sample selection 的问题分解上有真正贡献，correlation-selection gap 作为概念有实用价值，统计报告质量在 empirical NLP 论文中属上乘，WNUT-17 capability boundary 分析提供了重要方法论警示。\n\n但一个 critical 问题（constrained decoding confound）对核心 claim 构成 validity threat——如果 gap 主要由实验设置的 diversity 压缩导致，则核心贡献的 generalizability 受限。7 个 warning 级别问题（RE 单数据集、statistical logic、single seed、gap tautological 成分、MBR 联系缺失、多重比较、FK 独立性）共同表明论文在 soundness 和 framing 上仍有显著改进空间。\n\n两位 Reviewer 独立给出 3/5 (Findings) 评分，交叉回应后评分维持不变。论文方法论严谨的核心质量使其适合 Findings track，但 constrained decoding confound 未解决前不建议 Main Conference。\n\n**修订优先级**（按影响排序）：\n1. **[Must]** Constrained decoding diversity 量化或对照实验（决定核心 claim 是否成立）\n2. **[Should]** RE claim 降级 + conditional analysis（减少过度泛化风险）\n3. **[Should]** Selection gap 措辞修正 + power analysis（统计严谨性）\n4. **[Should]** Gap 论证分层 + MBR 联系（概念清晰度）\n5. **[Should]** Multi-seed 验证或 Limitations 声明（可靠性）\n6. **[Minor]** 术语统一、引用补充、数据一致性修正\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"NER (three datasets of varying difficulty) and RE (SciERC)\" 区分到位（Round 2 修正有效）\n- \"oracle headroom\" 首次出现无定义，建议加括号解释\n- \"no signal reliably surpasses greedy\" 措辞需修改为更严谨的统计表述\n\n### Introduction\n- Quality estimation vs. sample selection 的分离框架论述清晰\n- 对 Nedellec (2026) 的 (i)-(iii) 列举技术准确但语气偏 adversarial\n- \"First multi-family comparison\" 需收窄 scope\n\n### Method (§3)\n- Per-sample vs. instance-level 形式化清晰（Eq. 1-7）\n- SJ Eq. 4: Hungarian matching 优化目标和 zero-IoU pairs 处理需补充\n- FK §3.2: 独立性假设 one-line justification 不充分\n- Consensus-proximity (§3.3): 未与 MBR decoding 建立联系\n\n### Experiments (§4)\n- Quality estimation (§4.2): 数据全面，task difficulty crossover 有洞察力\n- WNUT-17 conditional 分析揭示重要 artifact（Table 7）\n- Selection gap (§4.3): 统计报告详实但 failure-to-reject 逻辑需修正\n- Robustness (§4.4): temperature/N-scaling 分析系统性好，SJ stability 值得突出\n\n### Discussion (§5)\n- Practical recommendations 具体可行\n- \"Why logprob fails\" 段落是关键改进方向——需更多实证支持\n- Constrained decoding 讨论需从 \"future work\" 升级为当前 limitation 的核心分析\n- Gap 论证应分层：definitional (instance-level) vs. empirical (logprob + consensus-proximity)\n\n### Conclusion (§6)\n- 三项 anchoring findings 总结准确\n- RE hedging 到位但仍可进一步降级\n\n### Limitations\n- 覆盖面广且诚实\n- 建议新增：(a) constrained decoding 对 diversity 的影响作为 explicit limitation 条目；(b) single-seed 风险\n\n### Appendix\n- Bootstrap CI 表 (Table 8) 有价值\n- WNUT-17 全信号表 (Table 7) 补充到位\n- Cross-configuration selection (Table 6) 增强了 gap 证据面",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 324 · 2026-05-15T04:15:02.462354+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4169
}
```

</details>

---


### Assistant

_source line 325 · 2026-05-15T04:15:12.885175+00:00_

审稿报告已投递至 Research Director。

**Round 3 审稿完成**，汇总如下：

**Overall: borderline（Findings track）**，两位 Reviewer 独立评分一致（3/5），交叉回应后维持。

**核心问题清单**：
- **1 个 Critical**：constrained decoding 是 correlation-selection gap 的未控制混淆变量——gap 可能是 diversity 压缩的 artifact 而非信号固有局限
- **11 个 Warning**：RE 单数据集 + floor effect、failure-to-reject 措辞、single seed、gap tautological 成分、MBR decoding 联系缺失、多重比较校正、FK 独立性、cross-model 措辞、claim scope、遗漏引用、术语不一致
- **10 个 Info**：数据不一致、EM exclusion、Ethics Statement、ρ-AUROC 过度强调等

**修订关键路径**：constrained decoding 的 diversity 量化（unique output fraction + per-sample logprob std）是决定性修订——解决此问题可明确核心 claim 的 generalizability boundary，为提升至 Findings 奠定基础。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 326 · 2026-05-15T04:15:15.553461+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

与 R1 的核心分歧在于严重程度判断：
- R1-N2（统计逻辑）和 R1-N3（单 seed）我认为应降为 Should-Fix，因为 6/6 配置一致性和 ranking 稳定性提供了足够的 cumulative evidence
- R1-W6（consensus-proximity 唯一策略 + 缺少 MBR 对比）是 R1 最有力的贡献点，我的原始审稿未充分关注到这一点

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

_source line 327 · 2026-05-15T04:15:24.919770+00:00_

审稿报告已提交至 Research Director。

**Round 3 审稿完成总结**：

- **Overall**: borderline（Findings track）
- **两位 Reviewer 评分一致**：3/5，交叉回应后维持
- **1 个 Critical**：constrained decoding 混淆变量（两位 Reviewer 独立提出，完全共识）
- **11 个 Warning**：RE 单数据集、statistical logic、single seed、gap tautological 成分、MBR 联系缺失、多重比较校正、FK 独立性、cross-model 措辞、claim scope、遗漏引用、术语不一致
- **10 个 Minor**：数据不一致、EM exclusion、Ethics Statement 等
- **修订优先级第一位**：量化 constrained decoding 对 per-sample diversity 的影响——这决定核心 claim 是否成立

Issue Tracker 已同步更新（`artifacts/review_issues.yaml`），15 个新 open issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 32

## Round 32

96 recorded events


### User

_source line 328 · 2026-05-15T06:38:14.223105+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: findings
- 截止日期: 2026-05-25

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

_source line 329 · 2026-05-15T06:38:26.875806+00:00_

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

_source line 330 · 2026-05-15T06:38:26.926900+00:00_

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
…[truncated 2458 chars]

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

_source line 331 · 2026-05-15T06:38:29.890459+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
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
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 332 · 2026-05-15T06:38:29.941546+00:00_



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

_source line 333 · 2026-05-15T06:38:36.569368+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 334 · 2026-05-15T06:38:36.619975+00:00_

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

_source line 335 · 2026-05-15T06:38:41.491312+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 336 · 2026-05-15T06:38:41.541923+00:00_



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

_source line 337 · 2026-05-15T06:38:44.856187+00:00_

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

_source line 338 · 2026-05-15T06:38:46.274916+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (79 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_017_llama_conll_n16_s456_r1024（准备中）\n- exp_017_llama_conll_n16_r1024（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n- exp_007_ner_llama（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp008_re_n16（准备中）\n\n## 近期结论\n- **exp_018_llama_scierc_seed42_r1024** (success): —\n- **exp_018_llama_scierc_seed456_r1024** (success): —\n- **exp_018_llama_scierc_seed456** (success): —\n\n## 趋势\n成功 43 / 负向 18 / 失败 1 / 共 70\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1418
}
```

</details>

---


### Tool call

_source line 339 · 2026-05-15T06:38:46.275397+00:00_

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

_source line 340 · 2026-05-15T06:38:47.029272+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 341 · 2026-05-15T06:38:47.079890+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 342 · 2026-05-15T06:38:52.051324+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Call for Papers and Shared Task Participation (CASE @ EMNLP 2022): Challenges and Applications of Automated Extraction of Socio-political Events from Text | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-and-shared-task-participation-case-emnlp-2022-challenges-and-applications"}]

Based on the search results, I was unab
…[truncated 994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 4971
}
```

</details>

---
