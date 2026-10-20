# Director coordination — Part 1 of 3

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

[Transcript overview](../director-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/6a/6a7b0a19365cff5eceb9.json)

## Round 1

## Round 1

32 recorded events


### User

_source line 1 · 2026-05-14T12:51:22.669182+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: phase-gated-compound-sparse
- 论文路径: projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-14T12:51:29.037737+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-14T12:51:29.089027+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-14T12:51:37.178625+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
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

_source line 5 · 2026-05-14T12:51:37.229466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-14T12:51:42.454149+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-14T12:51:44.868786+00:00_

{"result":"# 项目 phase-gated-compound-sparse 概况\n\n## 实验状态 (76 个)\n\n- **mvp_v4_legacy_s025**: DONE (failed) — \n- **mvp_v4_random_r2**: DONE (success) — \n- **mvp_v4_legacy_s01**: DONE (negative) — \n- **mvp_v4_legacy_s03**: DONE (success) — \n- **mvp_v4_legacy_s02**: DONE (success) — \n- **mvp_v4c_r2**: DONE (failed) — \n- **mvp_v4b_r2**: DONE (failed) — \n- **mvp_v4a_r2**: DONE (failed) — \n- **mvp_ii_profiling_v4-random**: DONE (failed) — \n- **mvp_ii_profiling_v4c**: DONE (failed) — \n- **mvp_ii_profiling_v4b**: DONE (failed) — \n- **mvp_ii_profiling_v4**: DONE (failed) — \n- **mvp_ii_profiling_v3**: DONE (negative) — \n- **mvp_ii_profiling_v2**: DONE (negative) — \n- **mvp_interaction_index_profiling**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **bf16_qw_imp_s035** (success): —\n- **bf16_qw_imp_s010** (success): —\n- **bf16_ds_imp_s035** (success): —\n\n## 趋势\n成功 35 / 负向 9 / 失败 13 / 共 76\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-22162: 无 GPU 信息\n\n## 告警\n- mvp_interaction_index_profiling: 训练失败 — unknown\n- mvp_ii_profiling_v4: 训练失败 — unknown\n- mvp_ii_profiling_v4b: 训练失败 — unknown\n- mvp_ii_profiling_v4c: 训练失败 — unknown\n- mvp_ii_profiling_v4d: 训练失败 — unknown\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\n- mvp_v4a_r2: 训练失败 — unknown\n- mvp_v4b_r2: 训练失败 — unknown\n- mvp_v4c_r2: 训练失败 — unknown\n- mvp_v4_legacy_s025: 训练失败 — unknown\n- mvp_v4_legacy_s035: 训练失败 — unknown\n- mvp_v4_float32_s030: 已被终止 — unknown\n- mvp_v5_fixed_s020: 已被终止 — unknown\n- mvp_v5_fixed_s030: 已被终止 — unknown\n- qwen_importance_s015: 已被终止 — unknown\n- qwen_importance_s020: 已被终止 — unknown\n- qwen_importance_s025: 已被终止 — unknown\n- qwen_importance_s030: 已被终止 — unknown\n- v6_random_s030: 训练失败 — unknown\n- v6_random_s030_r2: 训练失败 — unknown\n- bf16_random_s015: 已被终止 — unknown\n- bf16_random_s020: 已被终止 — unknown\n- bf16_random_s025: 已被终止 — unknown\n- bf16_random_s030: 已被终止 — unknown\n- bf16_qw
…[truncated 315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2414
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-14T12:51:45.322705+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf 2>/dev/null && echo \"FILE_EXISTS\" || echo \"FILE_MISSING\"",
  "description": "Check paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf 2>/dev/null && echo \"FILE_EXISTS\" || echo \"FILE_MISSING\"",
    "description": "Check paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-14T12:51:45.577081+00:00_

-rw-r--r-- 1 ubuntu ubuntu 364984 May 14 12:43 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf
FILE_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 254
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-14T12:51:45.577603+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-14T12:51:45.678879+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md\", \"content\": \"# Project Memory — 2026-05-14 09:21 UTC\\n\\n## 统计方法决策\\n\\n### Mean vs Median（关键教训）\\n- bf16 importance II 数据 skewness 极高（6-17），mean-based gradient 非单调\\n- **决策**：论文统一用 median 报告 II，辅以 winsorized mean（5% trim）\\n- Reviewer 预备答复：skewness > 5，median 是标准做法（Wilcox 2012）\\n\\n### Median Difference 两种定义（2026-05-14 发现）\\n- **定义 A（paired）**: `median(ii_low_i - ii_high_i)` — 论文图表用此\\n- **定义 B（unpaired）**: `median(ii_low) - median(ii_high)` — summary table / registry 用此\\n- 两者略有差异（如 DS s015: paired=0.32 vs unpaired=0.39）\\n- 论文正文需明确说明用了哪种定义\\n\\n### Cohen's d — Director 决策（2026-05-14 确定）\\n**论文用 per-problem paired 方法（B=10000 re-bootstrap）**\\n\\n| Sparsity | DS paired | QW paired | DS segment(旧,supplementary) | QW segment(旧,supplementary) |\\n|----------|-----------|-----------|---------------------------|---------------------------|\\n| s015 | **0.607** | **0.371** (CI含0, marginal) | 0.44 | 0.28 |\\n| s020 | **0.725** | **0.722** | 0.52 | 0.55 |\\n| s025 | **0.953** | **1.233** | 0.68 | 0.89 |\\n| s030 | **1.126** | **1.439** | 0.80 | 1.02 |\\n\\n- 正文用 paired 值，supplementary 附 segment-level 作 robustness check\\n- qw_imp_s015 标注 \\\"marginal at s=0.15, becoming reliable at s≥0.20\\\"\\n- 脚本：`/root/autodl-tmp/pacs/analysis/rebootstrap_importance_b10000.py`\\n\\n### Random: 8/8 FAIL（2026-05-14 确认）\\n- qw_rand_s030 由 B=10000 re-bootstrap 确认 FAIL (p=0.111, gradient CI 含 0)\\n- 论文可简洁报告 \\\"8/8 FAIL\\\"\\n\\n### Permutation Test\\n- Difference statistic 全 4 水平 Bonferroni p < 0.005\\n- 论文主统计检验\\n\\n### Bootstrap B 值\\n- 全部统一为 B=10000（re-bootstrap 已完成）\\n\\n## C4 Entropy Mechanism — Negative for Qwen（2026-05-14）\\n\\n### Qwen importance entropy delta（systematic 非 outlier）\\n- s015: -0.073 (2:28 neg majority) ✓ consistent\\n- s020: -0.076 (4:26 neg majority) ✓ consistent\\n- s025: **+0.045** (22:8 **pos majority**) ⚠️ 
…[truncated 2613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-14T12:51:56.638252+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-14T12:51:56.689059+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-14T12:52:00.367297+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-14T12:52:03.282659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf"
  }
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-14T12:52:04.136797+00:00_

This PDF has 12 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-14T12:52:04.588984+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-14T12:52:05.443063+00:00_

NO_ISSUES_FILE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-14T12:52:05.495687+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 20 · 2026-05-14T12:52:05.546477+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-14T12:52:10.769175+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here are the key submission guidelines and author instructions for EMNLP 2026:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and sh
…[truncated 2335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 10401
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-14T12:52:16.395208+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 formatting guidelines page limits long short paper template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 formatting guidelines page limits long short paper template"
  }
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-14T12:52:18.907888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf",
  "pages": "1-6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf",
    "pages": "1-6"
  }
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-14T12:52:19.363743+00:00_

PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf (356.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-14T12:52:22.892973+00:00_

Web search results for query: "ACL Rolling Review 2026 formatting guidelines page limits long short paper template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"NAACL 2026 LaTeX Template | ACL Style Files & Guide | Underleaf","url":"https://www.underleaf.ai/templates/naacl"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the search results, I found information about ACL Rolling Review 2026 formatting guidelines and page limits:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

## What Doesn't Count Toward Page Limits

Appendices do not count towards the page limit. Additionally, an ethical considerations section does not count towards the page limit,
…[truncated 873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6497
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-14T12:52:29.189270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf",
  "pages": "7-12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf",
    "pages": "7-12"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-14T12:52:29.541758+00:00_

PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf (356.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-14T12:53:39.438317+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计验证**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n- **PDF 路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf`\n- **目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求\n- 长文正文 ≤ 8 页 + 参考文献不限\n- Limitations 节必须有，**不计入页数**，须为无编号独立节置于 Conclusion 之后、References 之前\n- 附录不计入页数\n- 模板：ACL/ARR `[review]` 模式\n- 匿名：double-blind（\"Anonymous ACL submission\"）\n\n### 你的审查重点\n\n请以 EMNLP 最严格审稿人的标准评估以下方面：\n\n1. **方法论严谨性**：\n   - Interaction Index (II) 的定义（Eq. 4）是否合理？additive null 假设是否足够？\n   - Phase segmentation（§3.3 quantile-based）是否有 data leakage 或循环论证风险？\n   - Severity gradient (G = II_low / II_high) 的定义——当 II_high 接近 0 时 G→∞ 的处理是否合理？\n   - 使用 median 而非 mean 的理由是否充分论证？\n\n2. **实验设计**：\n   - 仅 50 个 MATH-500 问题，样本量是否足够支撑结论？\n   - 仅 2 个模型（且共享 Qwen2 架构），泛化性声明是否过度？\n   - 仅 4 个 sparsity levels，是否足以论证\"monotonic\"增长？\n   - 对称 sparsity budget（head pruning 和 KV eviction 使用同一 s）是否限制了结论的普适性？\n\n3. **统计验证**：\n   - Bootstrap B=10,000 + Bonferroni 修正的 permutation test 是否充分？\n   - Qwen s=0.15 的 marginal 结果（d_z=0.28, CI 含零）如何影响 monotonicity 声明？\n   - Cohen's d 从 0.44→0.80 被称为 \"small→large\"，效应量解读是否准确？\n   - Cross-model Spearman ρ=1.0（仅 4 个数据点）的统计功效？\n\n4. **可重复性**：\n   - 是否提供了足够的实验细节（代码、超参、随机种子）？\n   - 50 个问题的选择标准是否清晰？\n\n请输出完整的审稿报告，包含：Summary、Strengths、Weaknesses（必须严格，逐条列出并标注 severity: critical/major/minor）、Questions for Authors、Missing References、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计验证**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n- **PDF 路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf`\n- **目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求\n- 长文正文 ≤ 8 页 + 参考文献不限\n- Limitations 节必须有，**不计入页数**，须为无编号独立节置于 Conclusion 之后、References 之前\n- 附录不计入页数\n- 模板：ACL/ARR `[review]` 模式\n- 匿名：double-blind（\"Anonymous ACL submission\"）\n\n### 你的审查重点\n\n请以 EMNLP 最严格审稿人的标准评估以下方面：\n\n1. **方法论严谨性**：\n   - Interaction Index (II) 的定义（Eq. 4）是否合理？additive null 假设是否足够？\n   - Phase segmentation（§3.3 quantile-based）是否有 data leakage 或循环论证风险？\n   - Severity gradient (G = II_low / II_high) 的定义——当 II_high 接近 0 时 G→∞ 的处理是否合理？\n   - 使用 median 而非 mean 的理由是否充分论证？\n\n2. **实验设计**：\n   - 仅 50 个 MATH-500 问题，样本量是否足够支撑结论？\n   - 仅 2 个模型（且共享 Qwen2 架构），泛化性声明是否过度？\n   - 仅 4 个 sparsity levels，是否足以论证\"monotonic\"增长？\n   - 对称 sparsity budget（head pruning 和 KV eviction 使用同一 s）是否限制了结论的普适性？\n\n3. **统计验证**：\n   - Bootstrap B=10,000 + Bonferroni 修正的 permutation test 是否充分？\n   - Qwen s=0.15 的 marginal 结果（d_z=0.28, CI 含零）如何影响 monotonicity 声明？\n   - Cohen's d 从 0.44→0.80 被称为 \"small→large\"，效应量解读是否准确？\n   - Cross-model Spearman ρ=1.0（仅 4 个数据点）的统计功效？\n\n4. **可重复性**：\n   - 是否提供了足够的实验细节（代码、超参、随机种子）？\n   - 50 个问题的选择标准是否清晰？\n\n请输出完整的审稿报告，包含：Summary、Strengths、Weaknesses（必须严格，逐条列出并标注 severity: critical/major/minor）、Questions for Authors、Missing References、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-14T12:53:55.673266+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16234
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-14T12:53:55.775750+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n- **PDF 路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf`\n- **目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求\n- 长文正文 ≤ 8 页 + 参考文献不限\n- Limitations 节必须有，**不计入页数**，须为无编号独立节置于 Conclusion 之后、References 之前\n- 附录不计入页数\n- 模板：ACL/ARR `[review]` 模式\n- 匿名：double-blind（\"Anonymous ACL submission\"）\n\n### 你的审查重点\n\n请以 EMNLP 最严格审稿人的标准评估以下方面：\n\n1. **新颖性与贡献评估**：\n   - \"compound sparsity severity is phase-dependent\" 这一发现的 novelty 有多高？\n   - Entropy-discrimination collapse 是否是一个真正的新 mechanism，还是已知现象的重新包装？\n   - 论文的贡献是否足以构成 EMNLP main conference 长文？还是更适合 findings/workshop？\n   - Claim 的强度是否与证据匹配？（如 \"phase-strategy interaction\" 的说法）\n\n2. **相关工作完整性**：\n   - 是否遗漏了关键的 compound compression / KV cache eviction / attention sparsity 工作？\n   - 特别关注 2025-2026 年最新工作是否被充分引用\n   - ThinKV (Ramachandran et al., 2026) 被用于 phase segmentation——对该工作的区分是否清晰？\n   - 是否遗漏了 phase-aware inference 或 adaptive compression 的相关工作？\n\n3. **写作质量**：\n   - 论文结构是否清晰？各节之间的逻辑衔接是否流畅？\n   - Abstract 是否准确反映论文内容和贡献？\n   - 术语使用是否一致？（如 \"severity gradient\" 的多重含义）\n   - 图表质量：Figure 1-4 和 Table 1-7 是否清晰、必要、标注规范？\n\n4. **格式合规性**（对照 ARR 要求逐项检查）：\n   - 正文页数是否 ≤ 8 页？精确计算哪些内容在正文范围内\n   - **Limitations 节**：当前作为 §7.1（编号子节）出现在 Discussion 中——这是否符合 ARR 要求？ARR 要求 Limitations 为无编号独立节\n   - 匿名标注是否正确？是否有去匿名化信息泄露？\n   - 引用格式是否符合 ACL 模板规范？\n   - 脚注 2 提到 \"4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB GPUs\"——这是否构成去匿名化风险？\n\n请输出完整的审稿报告，包含：Summary、Strengths、Weaknesses（必须严格，逐条列出并标注 severity: critical/major/minor）、Questions for Authors、Missing References（列出具体论文）、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n- **PDF 路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf`\n- **目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求\n- 长文正文 ≤ 8 页 + 参考文献不限\n- Limitations 节必须有，**不计入页数**，须为无编号独立节置于 Conclusion 之后、References 之前\n- 附录不计入页数\n- 模板：ACL/ARR `[review]` 模式\n- 匿名：double-blind（\"Anonymous ACL submission\"）\n\n### 你的审查重点\n\n请以 EMNLP 最严格审稿人的标准评估以下方面：\n\n1. **新颖性与贡献评估**：\n   - \"compound sparsity severity is phase-dependent\" 这一发现的 novelty 有多高？\n   - Entropy-discrimination collapse 是否是一个真正的新 mechanism，还是已知现象的重新包装？\n   - 论文的贡献是否足以构成 EMNLP main conference 长文？还是更适合 findings/workshop？\n   - Claim 的强度是否与证据匹配？（如 \"phase-strategy interaction\" 的说法）\n\n2. **相关工作完整性**：\n   - 是否遗漏了关键的 compound compression / KV cache eviction / attention sparsity 工作？\n   - 特别关注 2025-2026 年最新工作是否被充分引用\n   - ThinKV (Ramachandran et al., 2026) 被用于 phase segmentation——对该工作的区分是否清晰？\n   - 是否遗漏了 phase-aware inference 或 adaptive compression 的相关工作？\n\n3. **写作质量**：\n   - 论文结构是否清晰？各节之间的逻辑衔接是否流畅？\n   - Abstract 是否准确反映论文内容和贡献？\n   - 术语使用是否一致？（如 \"severity gradient\" 的多重含义）\n   - 图表质量：Figure 1-4 和 Table 1-7 是否清晰、必要、标注规范？\n\n4. **格式合规性**（对照 ARR 要求逐项检查）：\n   - 正文页数是否 ≤ 8 页？精确计算哪些内容在正文范围内\n   - **Limitations 节**：当前作为 §7.1（编号子节）出现在 Discussion 中——这是否符合 ARR 要求？ARR 要求 Limitations 为无编号独立节\n   - 匿名标注是否正确？是否有去匿名化信息泄露？\n   - 引用格式是否符合 ACL 模板规范？\n   - 脚注 2 提到 \"4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB GPUs\"——这是否构成去匿名化风险？\n\n请输出完整的审稿报告，包含：Summary、Strengths、Weaknesses（必须严格，逐条列出并标注 severity: critical/major/minor）、Questions for Authors、Missing References（列出具体论文）、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-14T12:53:57.292321+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1516
}
```

</details>

---


### Assistant

_source line 32 · 2026-05-14T12:54:03.173775+00:00_

Round 1 任务已分配：

- **Reviewer 1**（方法/实验/统计）→ 已派发
- **Reviewer 2**（新颖性/相关工作/写作/格式）→ 已派发

等待两位 Reviewer 返回独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 2

## Round 2

36 recorded events


### User

_source line 33 · 2026-05-14T13:02:35.556393+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: phase-gated-compound-sparse
- 论文路径: artifacts/_project/paper/main.pdf
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-14T13:02:42.608230+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-14T13:02:42.763207+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 154
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-14T13:02:46.178438+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-14T13:02:46.229140+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-14T13:02:51.825874+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-14T13:02:52.859103+00:00_

{"result":"# 项目 phase-gated-compound-sparse 概况\n\n## 实验状态 (76 个)\n\n- **mvp_v4_legacy_s025**: DONE (failed) — \n- **mvp_v4_random_r2**: DONE (success) — \n- **mvp_v4_legacy_s01**: DONE (negative) — \n- **mvp_v4_legacy_s03**: DONE (success) — \n- **mvp_v4_legacy_s02**: DONE (success) — \n- **mvp_v4c_r2**: DONE (failed) — \n- **mvp_v4b_r2**: DONE (failed) — \n- **mvp_v4a_r2**: DONE (failed) — \n- **mvp_ii_profiling_v4-random**: DONE (failed) — \n- **mvp_ii_profiling_v4c**: DONE (failed) — \n- **mvp_ii_profiling_v4b**: DONE (failed) — \n- **mvp_ii_profiling_v4**: DONE (failed) — \n- **mvp_ii_profiling_v3**: DONE (negative) — \n- **mvp_ii_profiling_v2**: DONE (negative) — \n- **mvp_interaction_index_profiling**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **bf16_qw_imp_s035** (success): —\n- **bf16_qw_imp_s010** (success): —\n- **bf16_ds_imp_s035** (success): —\n\n## 趋势\n成功 35 / 负向 9 / 失败 13 / 共 76\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-22162: 无 GPU 信息\n\n## 告警\n- mvp_interaction_index_profiling: 训练失败 — unknown\n- mvp_ii_profiling_v4: 训练失败 — unknown\n- mvp_ii_profiling_v4b: 训练失败 — unknown\n- mvp_ii_profiling_v4c: 训练失败 — unknown\n- mvp_ii_profiling_v4d: 训练失败 — unknown\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\n- mvp_v4a_r2: 训练失败 — unknown\n- mvp_v4b_r2: 训练失败 — unknown\n- mvp_v4c_r2: 训练失败 — unknown\n- mvp_v4_legacy_s025: 训练失败 — unknown\n- mvp_v4_legacy_s035: 训练失败 — unknown\n- mvp_v4_float32_s030: 已被终止 — unknown\n- mvp_v5_fixed_s020: 已被终止 — unknown\n- mvp_v5_fixed_s030: 已被终止 — unknown\n- qwen_importance_s015: 已被终止 — unknown\n- qwen_importance_s020: 已被终止 — unknown\n- qwen_importance_s025: 已被终止 — unknown\n- qwen_importance_s030: 已被终止 — unknown\n- v6_random_s030: 训练失败 — unknown\n- v6_random_s030_r2: 训练失败 — unknown\n- bf16_random_s015: 已被终止 — unknown\n- bf16_random_s020: 已被终止 — unknown\n- bf16_random_s025: 已被终止 — unknown\n- bf16_random_s030: 已被终止 — unknown\n- bf16_qw
…[truncated 315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1033
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-14T13:02:52.910051+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
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

_source line 41 · 2026-05-14T13:02:52.961359+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-14T13:02:54.371320+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/_project/paper/main.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/_project/paper/main.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-14T13:02:54.473680+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-14T13:02:59.342703+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 45 · 2026-05-14T13:03:00.759421+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline page limit template",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline page limit template",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
  }
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-14T13:03:01.323898+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "report.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "report.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-14T13:03:06.968338+00:00_

Web search results for query: "EMNLP 2026 submission deadline page limit template"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"EMNLP 2023: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2023-call-papers"},{"title":"Joint Call for Workshops for NAACL/ACL/EMNLP 2025 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-workshops-naaclaclemnlp-2025"},{"title":"Final Call for Papers - 4th Multilingual Representation Learning (MRL) Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/final-call-papers-4th-multilingual-representation-learning-mrl-workshop"}]

Based on the search results, I found information about EMNLP 2026 main conference papers. Here are the key details:

## EMNLP 2026 Page Limits

Long papers will receive up to 8 pages for content submission, with one additi
…[truncated 1092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6208
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-14T13:03:08.567130+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the web search results, here's a comprehensive overview of the EMNLP 2026 call for papers submission guidelines and author instructions:

## Paper Types and Scope

EMNLP 2026
…[truncated 2152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 9224
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-14T13:03:08.617988+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **bf16_qw_imp_s035** (success): —\\n- **bf16_qw_imp_s010** (success): —\\n- **bf16_ds_imp_s035** (success): —\\n\\n## 趋势\\n成功 35 / 负向 9 / 失败 13 / 共 76\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-22162: 无 GPU 信息\\n\\n## 告警\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\n- mvp_v4a_r2: 训练失败 — unknown\\n- mvp_v4b_r2: 训练失败 — unknown\\n- mvp_v4c_r2: 训练失败 — unknown\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\n- mvp_v4_float32_s030: 已被终止 — unknown\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\n- qwen_importance_s015: 已被终止 — unknown\\n- qwen_importance_s020: 已被终止 — unknown\\n- qwen_importance_s025: 已被终止 — unknown\\n- qwen_importance_s030: 已被终止 — unknown\\n- v6_random_s030: 训练失败 — unknown\\n- v6_random_s030_r2: 训练失败 — unknown\\n- bf16_random_s015: 已被终止 — unknown\\n- bf16_random_s020: 已被终止 — unknown\\n- bf16_random_s025: 已被终止 — unknown\\n- bf16_random_s030: 已被终止 — unknown\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\n- bf16_ds_imp_s015: 已被终止 — unknown\\n- bf16_ds_imp_s020: 已被终止 — unknown\\n- bf16_ds_imp_s025: 已被终止 — unknown\\n- bf16_ds_imp_s030: 已被终止 — unknown\\n\", \"total_chars\": 1511, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7294
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-14T13:03:13.087317+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format template page limit anonymity policy ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format template page limit anonymity policy ARR"
  }
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-14T13:03:13.540332+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-14T13:03:14.243468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf",
  "pages": "1-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf",
    "pages": "1-20"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-14T13:03:20.807509+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format template page limit anonymity policy ARR"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission requirements:

## Submission Format and Page Limits

Papers should follow the style guides and not exceed the page limit (4 pages for short papers, 8 pages for long papers, excluding ethical considerations and limitations). Submissions that exceed the length requirements, or are missing a limitations section, will be desk 
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7720
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-14T13:03:20.808280+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/decisions.yaml\", \"content\": \"_next_id: 52\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:44 UTC\\n  summary: MVP 方案：用 Interaction Index 跨 phase 差异验证核心假设\\n  rationale: 评审建议 novelty 锚定在 \\\"phase-dependent interaction direction reversal\\\"。MVP\\n    聚焦验证这一点：在 MATH-500 子集上 profiling DeepSeek-R1-Distill-Qwen-7B，用 ThinKV 方法切分 phases，计算\\n    attention × KV 的 Interaction Index。比全 grid search 更聚焦，直接验证核心 novelty 锚点。Pass =\\n    II 跨 phase 显著不同；Fail = II 恒定。预计 10-15 H100-hours。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:48 UTC\\n  summary: 向 Manager 申请 4×H100-80GB 租卡，预计 8-10 天，¥3200-5000\\n  rationale: 12 天截稿，4 GPU 并行可将日历时间压到 ~8 天（留 4 天 buffer）。2 GPU 需 11 天，buffer 不足 1 天，风险过高。用户明确授权\\\"几张都可以\\\"。GPU\\n    就绪 hard deadline 5/14 EOD。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 17:54 UTC\\n  summary: Throughput 策略：RTX 6000 Pro 做开发/accuracy，最终 throughput 短租 H100\\n  rationale: IDEA_BRIEF 硬约束要求\\\"Report wall-clock and throughput on H100\\\"，baseline 论文（Polar\\n    Sparsity、SeerAttention-R）均报告 H100 数字。RTX 6000 Pro (sm_89) vs H100 (sm_90) 的 kernel\\n    speedup 可能不同。策略(a)：RTX 6000 Pro 做全部开发+accuracy+ablation（硬件无关），仅 throughput 基准测试短租\\n    H100 ~2-4h（~$6-12）。比策略(b)全在 RTX 6000 Pro 上报告更有说服力，成本极低。H100 在 M5 阶段再申请。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 17:58 UTC\\n  summary: Throughput benchmark 硬件从 H100 改为 H20（Hopper sm_90，用户确认无 H100 可用）\\n  rationale: H20 与 H100 同为 Hopper sm_90，kernel 兼容无需额外适配。96GB HBM3 + 4TB/s 带宽适合 inference\\n    benchmark。在 H20 上重跑所有 baseline 确保公平比较，报告 relative speedup ratio（Hopper 架构内比值稳定）。H100\\n    不可用，H20 是最佳替代。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 18:01 UTC\\n  summary: GPU 从 4× RTX 6000 Pro 换为 4× H20-NVLink 96GB\\n  rationale:
…[truncated 1471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7267
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-14T13:03:21.563900+00:00_

PDF pages extracted: 11 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf (353KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 7320
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-14T13:03:41.173934+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-14T13:03:41.777985+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md\", \"content\": \"# Project Memory — 2026-05-14 09:21 UTC\\n\\n## 统计方法决策\\n\\n### Mean vs Median（关键教训）\\n- bf16 importance II 数据 skewness 极高（6-17），mean-based gradient 非单调\\n- **决策**：论文统一用 median 报告 II，辅以 winsorized mean（5% trim）\\n- Reviewer 预备答复：skewness > 5，median 是标准做法（Wilcox 2012）\\n\\n### Median Difference 两种定义（2026-05-14 发现）\\n- **定义 A（paired）**: `median(ii_low_i - ii_high_i)` — 论文图表用此\\n- **定义 B（unpaired）**: `median(ii_low) - median(ii_high)` — summary table / registry 用此\\n- 两者略有差异（如 DS s015: paired=0.32 vs unpaired=0.39）\\n- 论文正文需明确说明用了哪种定义\\n\\n### Cohen's d — Director 决策（2026-05-14 确定）\\n**论文用 per-problem paired 方法（B=10000 re-bootstrap）**\\n\\n| Sparsity | DS paired | QW paired | DS segment(旧,supplementary) | QW segment(旧,supplementary) |\\n|----------|-----------|-----------|---------------------------|---------------------------|\\n| s015 | **0.607** | **0.371** (CI含0, marginal) | 0.44 | 0.28 |\\n| s020 | **0.725** | **0.722** | 0.52 | 0.55 |\\n| s025 | **0.953** | **1.233** | 0.68 | 0.89 |\\n| s030 | **1.126** | **1.439** | 0.80 | 1.02 |\\n\\n- 正文用 paired 值，supplementary 附 segment-level 作 robustness check\\n- qw_imp_s015 标注 \\\"marginal at s=0.15, becoming reliable at s≥0.20\\\"\\n- 脚本：`/root/autodl-tmp/pacs/analysis/rebootstrap_importance_b10000.py`\\n\\n### Random: 8/8 FAIL（2026-05-14 确认）\\n- qw_rand_s030 由 B=10000 re-bootstrap 确认 FAIL (p=0.111, gradient CI 含 0)\\n- 论文可简洁报告 \\\"8/8 FAIL\\\"\\n\\n### Permutation Test\\n- Difference statistic 全 4 水平 Bonferroni p < 0.005\\n- 论文主统计检验\\n\\n### Bootstrap B 值\\n- 全部统一为 B=10000（re-bootstrap 已完成）\\n\\n## C4 Entropy Mechanism — Negative for Qwen（2026-05-14）\\n\\n### Qwen importance entropy delta（systematic 非 outlier）\\n- s015: -0.073 (2:28 neg majority) ✓ consistent\\n- s020: -0.076 (4:26 neg majority) ✓ consistent\\n- s025: **+0.045** (22:8 **pos majority**) ⚠️ 
…[truncated 1512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-14T13:03:41.829210+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-14T13:03:42.282595+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-14T13:03:42.835597+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-14T13:03:43.791253+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-14T13:03:44.044269+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-14T13:03:44.348221+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-14T13:04:37.249690+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n- **论文路径**: `artifacts/_project/paper/main.pdf`\n- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板, long paper ≤8 页正文（不含参考文献和附录）, double-blind, 需 Limitations section, 附录不参与正式审稿但可参考\n\n### 论文概要\n论文研究 compound sparsity（同时 attention head pruning + KV cache eviction）在 reasoning 模型不同生成阶段的交互效应。核心发现：(1) importance-based eviction 下 compound severity 展现 phase-dependent severity gradient（69×→274× 跨 sparsity levels）；(2) random eviction 无此效应（7/8 条件不显著）；(3) s=0.25 处出现 strategy ranking reversal；(4) 提出 entropy-discrimination collapse 作为机制解释。在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上验证，50 MATH-500 问题。\n\n### 你的审查重点\n\n请严格、不留情面地评估以下方面：\n\n1. **实验设计**：\n   - 50 个 MATH-500 问题的样本量是否足够？统计功效如何？\n   - 仅 2 个模型（且共享 Qwen2 架构）的 cross-model replication 是否令人信服？\n   - 4 个 sparsity levels {0.15, 0.20, 0.25, 0.30} 的覆盖范围是否合理？\n   - Phase segmentation 方法（quantile-based tercile）是否有理论或实验依据？\n\n2. **Interaction Index 指标**：\n   - II = PPL_b - PPL_a - PPL_k + 1 的定义是否严谨？additive null 的选择是否有充分理由？\n   - 用 perplexity ratio 归一化是否引入偏差？\n\n3. **统计分析**：\n   - Nonparametric bootstrap (B=10,000) + Bonferroni correction 的选择是否恰当？\n   - Cohen's d_z 的使用和解读是否正确？\n   - Permutation test 的设计是否有效检验了核心假设？\n   - 多重比较校正是否充分？\n\n4. **因果推断**：\n   - \"Discrimination collapse\" 机制（§5.6）——从 Gini/CV 的相关性到因果机制的跳跃是否有依据？\n   - Entropy redistribution 在 Qwen 上部分不复现（s=0.25 反转）——这是否削弱了整体机制解释？\n\n5. **可复现性**：\n   - 实验细节是否充分到可以独立复现？\n   - 硬件（4× RTX PRO 6000 Blackwell）是否影响结论的普适性？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条）、Questions for Authors、Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n- **论文路径**: `artifacts/_project/paper/main.pdf`\n- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板, long paper ≤8 页正文（不含参考文献和附录）, double-blind, 需 Limitations section, 附录不参与正式审稿但可参考\n\n### 论文概要\n论文研究 compound sparsity（同时 attention head pruning + KV cache eviction）在 reasoning 模型不同生成阶段的交互效应。核心发现：(1) importance-based eviction 下 compound severity 展现 phase-dependent severity gradient（69×→274× 跨 sparsity levels）；(2) random eviction 无此效应（7/8 条件不显著）；(3) s=0.25 处出现 strategy ranking reversal；(4) 提出 entropy-discrimination collapse 作为机制解释。在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上验证，50 MATH-500 问题。\n\n### 你的审查重点\n\n请严格、不留情面地评估以下方面：\n\n1. **实验设计**：\n   - 50 个 MATH-500 问题的样本量是否足够？统计功效如何？\n   - 仅 2 个模型（且共享 Qwen2 架构）的 cross-model replication 是否令人信服？\n   - 4 个 sparsity levels {0.15, 0.20, 0.25, 0.30} 的覆盖范围是否合理？\n   - Phase segmentation 方法（quantile-based tercile）是否有理论或实验依据？\n\n2. **Interaction Index 指标**：\n   - II = PPL_b - PPL_a - PPL_k + 1 的定义是否严谨？additive null 的选择是否有充分理由？\n   - 用 perplexity ratio 归一化是否引入偏差？\n\n3. **统计分析**：\n   - Nonparametric bootstrap (B=10,000) + Bonferroni correction 的选择是否恰当？\n   - Cohen's d_z 的使用和解读是否正确？\n   - Permutation test 的设计是否有效检验了核心假设？\n   - 多重比较校正是否充分？\n\n4. **因果推断**：\n   - \"Discrimination collapse\" 机制（§5.6）——从 Gini/CV 的相关性到因果机制的跳跃是否有依据？\n   - Entropy redistribution 在 Qwen 上部分不复现（s=0.25 反转）——这是否削弱了整体机制解释？\n\n5. **可复现性**：\n   - 实验细节是否充分到可以独立复现？\n   - 硬件（4× RTX PRO 6000 Blackwell）是否影响结论的普适性？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条）、Questions for Authors、Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-14T13:04:52.918035+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15668
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-14T13:04:54.077660+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 实际影响**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n- **论文路径**: `artifacts/_project/paper/main.pdf`\n- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板, long paper ≤8 页正文（不含参考文献和附录）, double-blind, 需 Limitations section, 附录不参与正式审稿但可参考\n\n### 论文概要\n论文研究 compound sparsity（同时 attention head pruning + KV cache eviction）在 reasoning 模型不同生成阶段的交互效应。核心发现：(1) importance-based eviction 下 compound severity 展现 phase-dependent severity gradient（69×→274× 跨 sparsity levels）；(2) random eviction 无此效应（7/8 条件不显著）；(3) s=0.25 处出现 strategy ranking reversal；(4) 提出 entropy-discrimination collapse 作为机制解释。在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上验证，50 MATH-500 问题。\n\n### 你的审查重点\n\n请严格、不留情面地评估以下方面：\n\n1. **新颖性 (Novelty)**：\n   - 核心贡献（phase-dependent compound interaction）相对于现有 compound compression 文献（Liao et al. 2026 SparK; Mozaffari et al. 2025 SLiM; von Rad et al. 2026 UniComp）的增量价值有多大？\n   - \"Severity gradient\" 和 \"phase-strategy crossover\" 是否足够构成一篇 EMNLP 主会论文的贡献？\n   - Interaction Index 是否只是已有 super-additivity 概念的简单形式化？\n   - Discrimination collapse 是否只是一个事后观察而非真正的机制解释？\n\n2. **相关工作 (Related Work)**：\n   - 是否有重要的遗漏？特别关注：\n     - 2025-2026 年的 compound compression / joint pruning 工作\n     - Phase-aware inference 方面的最新进展（ThinKV 之外）\n     - Reasoning model compression 的相关工作\n   - 用 web_search 搜索最新相关工作，验证是否有重要遗漏\n   - 对已引用工作的定位是否准确公正？\n\n3. **写作质量**：\n   - 论文结构是否清晰？正文 ~5 页是否过于紧凑？\n   - Abstract 是否准确反映核心贡献和发现？\n   - 数学符号是否一致？\n   - 图表是否有效传达信息？Figure 1-4 的设计是否合理？\n   - Limitations section 是否诚实全面？\n\n4. **实际影响和 Actionability**：\n   - 论文的发现是否能直接指导实际的 LLM 部署决策？\n   - \"Phase-aware compression budget\" 的提议是否具体到可操作？还是只是概念性的？\n   - 缺少 throughput/latency 测量对论文价值的影响有多大？\n\n5. **格式合规**：\n   - 是否符合 EMNLP 2026 / ARR 格式要求？\n   - 匿名性是否完整（检查自引、致谢、代码链接等）？\n   - 引用格式是否正确？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条）、Questions for Authors、Missing References（用 web_search 验证）、Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 实际影响**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n- **论文路径**: `artifacts/_project/paper/main.pdf`\n- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板, long paper ≤8 页正文（不含参考文献和附录）, double-blind, 需 Limitations section, 附录不参与正式审稿但可参考\n\n### 论文概要\n论文研究 compound sparsity（同时 attention head pruning + KV cache eviction）在 reasoning 模型不同生成阶段的交互效应。核心发现：(1) importance-based eviction 下 compound severity 展现 phase-dependent severity gradient（69×→274× 跨 sparsity levels）；(2) random eviction 无此效应（7/8 条件不显著）；(3) s=0.25 处出现 strategy ranking reversal；(4) 提出 entropy-discrimination collapse 作为机制解释。在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上验证，50 MATH-500 问题。\n\n### 你的审查重点\n\n请严格、不留情面地评估以下方面：\n\n1. **新颖性 (Novelty)**：\n   - 核心贡献（phase-dependent compound interaction）相对于现有 compound compression 文献（Liao et al. 2026 SparK; Mozaffari et al. 2025 SLiM; von Rad et al. 2026 UniComp）的增量价值有多大？\n   - \"Severity gradient\" 和 \"phase-strategy crossover\" 是否足够构成一篇 EMNLP 主会论文的贡献？\n   - Interaction Index 是否只是已有 super-additivity 概念的简单形式化？\n   - Discrimination collapse 是否只是一个事后观察而非真正的机制解释？\n\n2. **相关工作 (Related Work)**：\n   - 是否有重要的遗漏？特别关注：\n     - 2025-2026 年的 compound compression / joint pruning 工作\n     - Phase-aware inference 方面的最新进展（ThinKV 之外）\n     - Reasoning model compression 的相关工作\n   - 用 web_search 搜索最新相关工作，验证是否有重要遗漏\n   - 对已引用工作的定位是否准确公正？\n\n3. **写作质量**：\n   - 论文结构是否清晰？正文 ~5 页是否过于紧凑？\n   - Abstract 是否准确反映核心贡献和发现？\n   - 数学符号是否一致？\n   - 图表是否有效传达信息？Figure 1-4 的设计是否合理？\n   - Limitations section 是否诚实全面？\n\n4. **实际影响和 Actionability**：\n   - 论文的发现是否能直接指导实际的 LLM 部署决策？\n   - \"Phase-aware compression budget\" 的提议是否具体到可操作？还是只是概念性的？\n   - 缺少 throughput/latency 测量对论文价值的影响有多大？\n\n5. **格式合规**：\n   - 是否符合 EMNLP 2026 / ARR 格式要求？\n   - 匿名性是否完整（检查自引、致谢、代码链接等）？\n   - 引用格式是否正确？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条）、Questions for Authors、Missing References（用 web_search 验证）、Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-14T13:04:55.594748+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1517
}
```

</details>

---


### Assistant

_source line 68 · 2026-05-14T13:05:02.457266+00:00_

两名 Reviewer 已分配，Round 1 独立审稿进行中：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 实验设计 + 统计分析 | ⏳ 审稿中 |
| R2 | 新颖性 + 相关工作 + 写作质量 + 实际影响 | ⏳ 审稿中 |

外部审稿：项目未配置 `external_review`，跳过。

等待 Reviewer 返回审稿意见后，进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 3

## Round 3

40 recorded events


### User

_source line 69 · 2026-05-14T13:05:02.480364+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: phase-gated-compound-sparse
- 论文路径: artifacts/_project/paper/main.pdf
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**

---

## 总体评分

**Overall**: 2.5/5（Weak Reject）
**一句话总结**: 本文报告了一个有趣的实证发现（compound sparsity severity 随推理阶段变化），但贡献停留在现象描述层面——没有提出方法、没有解决方案，且实验规模和架构覆盖不足以支撑其 claim 的普遍性；相关工作遗漏严重，格式存在 ARR 合规问题。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 主要 claim 有统计支撑，但方法学局限（2 模型同架构、50 题、仅用 PPL）削弱泛化性；entropy-discrimination collapse 机制仅有相关性证据 |
| Excitement | 2/5 | 发现本身有趣但贡献有限——纯分析无方法/解决方案；作为 main conference 长文偏薄 |
| Overall Assessment | 2.5/5 | 需实质性修订：扩展实验（跨架构、更大规模）、补充缺失引用、修正格式后可能适合 Findings |
| Reproducibility | 3.5/5 | 实验设置详细，统计方法透明，但 50 题 subset 选取细节不够、代码未提及公开 |
| Confidence | 4/5 | 对 KV cache compression 和 attention sparsity 文献较熟悉 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Limitations 节格式不符合 ARR 要求
- 位置：§7.1（第 7 页）
- 当前为 §7 Discussion 的编号子节（§7.1），ARR 要求无编号独立节置于 Conclusion 之后、References 之前。属于 desk reject 检查项。

**N2** [critical] 相关工作遗漏严重
- 位置：§2 Related Work
- 极高优先级遗漏：Lethe（AAAI 2026，phase-aware KV pruning 同期竞争工作）、R-KV（NeurIPS 2025，推理模型 KV 压缩最强 baseline）、"Hold Onto That Thought"（NeurIPS 2025，唯一系统评估推理任务 KV 压缩的工作）
- 高优先级遗漏：Scissorhands（NeurIPS 2023）、FastGen（ICLR 2024）、StreamingLLM（ICLR 2024）、LLM-Pruner（NeurIPS 2023）、Titanus（GLSVLSI 2025）
- 审稿人很可能因缺少 Lethe 和 R-KV 质疑领域了解程度

**N3** [critical] 贡献深度不足
- 纯分析无方法/解决方案。§7 提到 "phase-aware controller" 但停留在 future work。对 EMNLP main conference 长文偏薄，更适合 Findings。

**N4** [critical] 实验规模和多样性不足
- 仅 2 个模型共享 Qwen2 架构，"cross-model replication" 措辞有误导性
- 仅 50 道 MATH-500 题
- 仅 7B 规模
- 仅用 PPL 作为质量指标，缺少 accuracy——PPL 恶化不等于答案错误

---

## Should-Fix 问题

**W1** [major] Entropy-discrimination collapse 因果证据不足（Table 5 仅相关性，缺 intervention 实验）
**W2** [major] Bibliography 管理混乱——7 条 orphan entries（bib 有但正文未引），h2o-neurips2023 title 字段为空
**W3** [major] Abstract 约 600+ 词，远超通常 150-250 词建议
**W4** [major] Footnote 2 泄露 "4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB GPUs"，去匿名化风险
**W5** [minor] "Severity gradient" 术语过载（同时指标和概念）
**W6** [minor] Appendix B 与 Appendix D 文本几乎完全重复，疑为粘贴错误
**W7** [minor] 方程编号可能不连续（Eq. 2 位置不明）

---

## 小问题
- §6.3 PyramidKV 被引用两次且用不同作者信息
- Footnote 1 措辞不清 "float16 eliminated entirely"
- Table 3 caption 公式有多余项 "− Ĥ_dist"
- 部分 bib 年份与 OpenAlex 不一致（adakv-neurips2025 实际 2024、pope-mlsys2023 实际 2022）

---

## Missing References（完整列表）

| 优先级 | 论文 | Venue | 理由 |
|--------|------|-------|------|
| 极高 | Lethe (Zeng et al.) | AAAI 2026 | 与本文 phase-gated 思路直接重叠 |
| 极高 | R-KV (Cai et al.) | NeurIPS 2025 | 推理模型 KV 压缩最强 baseline |
| 极高 | Hold Onto That Thought | NeurIPS 2025 | 唯一系统评估推理任务 KV 压缩 |
| 高 | Scissorhands (Liu et al.) | NeurIPS 2023 | KV eviction 基础方法 |
| 高 | FastGen (Ge et al.) | ICLR 2024 | Per-head adaptive KV cache |
| 高 | StreamingLLM (Xiao et al.) | ICLR 2024 | Attention sink 基础 |
| 高 | LLM-Pruner (Ma et al.) | NeurIPS 2023 | Coupled pruning 开创性工作 |
| 高 | Titanus (Chen et al.) | GLSVLSI 2025 | KV pruning+quantization 复合效果 |
| 中 | SparseGPT | ICML 2023 | 权重稀疏化基础 |
| 中 | Wanda | ICLR 2024 | 轻量 pruning |
| 中 | MInference | NeurIPS 2024 | 注意力稀疏模式分析 |

---

## 主要优势
1. 研究问题有价值——compound sparsity 的 phase-dependent behavior 确实未被充分研究
2. 统计方法论优秀（permutation tests, bootstrap CI, Bonferroni correction, paired effect sizes）
3. Random eviction 作为 falsification control 的实验设计巧妙
4. Crossover 现象（§5.3）是 non-trivial 且有实际意义的发现
5. 写作总体清晰，§5 结果层层递进

---

## Questions for Authors
1. 为什么不报告 MATH-500 accuracy？PPL 下降是否对应答案正确率下降？
2. 与 Lethe（AAAI 2026）的区别和互补？
3. 是否考虑过 LLaMA-3 或 Mistral 上的验证？
4. Entropy-discrimination collapse 能否通过 intervention 实验验证因果性？
5. Appendix B 和 D 文本重复是编辑错误吗？

---

**Overall Score**: Weak Reject (2.5/5)
**Confidence**: 4/5

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：给出 **Weak Reject (2.5/5)** 评分。主要问题：(1) Limitations 节格式违反 ARR 要求（编号子节而非独立节）；(2) 遗漏 Lethe、R-KV、"Hold Onto That Thought" 等直接竞争/基础工作；(3) 贡献停留在现象描述——无方法、无解决方案；(4) 仅 2 个同架构 7B 模型 + 50 题 + 仅 PPL 指标，泛化性 claim 过强。优势方面，统计方法论扎实，random eviction 对照设计巧妙，crossover 现象有实际意义。建议补充跨架构实验 + accuracy 指标 + 缺失引用 + 格式修正后投 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-14T13:05:14.786725+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-14T13:05:17.433169+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 2646
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-14T13:05:17.584791+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
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

_source line 73 · 2026-05-14T13:05:17.585181+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-14T13:05:28.584989+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-14T13:05:29.087050+00:00_

{"result":"# 项目 phase-gated-compound-sparse 概况\n\n## 实验状态 (76 个)\n\n- **mvp_v4_legacy_s025**: DONE (failed) — \n- **mvp_v4_random_r2**: DONE (success) — \n- **mvp_v4_legacy_s01**: DONE (negative) — \n- **mvp_v4_legacy_s03**: DONE (success) — \n- **mvp_v4_legacy_s02**: DONE (success) — \n- **mvp_v4c_r2**: DONE (failed) — \n- **mvp_v4b_r2**: DONE (failed) — \n- **mvp_v4a_r2**: DONE (failed) — \n- **mvp_ii_profiling_v4-random**: DONE (failed) — \n- **mvp_ii_profiling_v4c**: DONE (failed) — \n- **mvp_ii_profiling_v4b**: DONE (failed) — \n- **mvp_ii_profiling_v4**: DONE (failed) — \n- **mvp_ii_profiling_v3**: DONE (negative) — \n- **mvp_ii_profiling_v2**: DONE (negative) — \n- **mvp_interaction_index_profiling**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **bf16_qw_imp_s035** (success): —\n- **bf16_qw_imp_s010** (success): —\n- **bf16_ds_imp_s035** (success): —\n\n## 趋势\n成功 35 / 负向 9 / 失败 13 / 共 76\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-22162: 无 GPU 信息\n\n## 告警\n- mvp_interaction_index_profiling: 训练失败 — unknown\n- mvp_ii_profiling_v4: 训练失败 — unknown\n- mvp_ii_profiling_v4b: 训练失败 — unknown\n- mvp_ii_profiling_v4c: 训练失败 — unknown\n- mvp_ii_profiling_v4d: 训练失败 — unknown\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\n- mvp_v4a_r2: 训练失败 — unknown\n- mvp_v4b_r2: 训练失败 — unknown\n- mvp_v4c_r2: 训练失败 — unknown\n- mvp_v4_legacy_s025: 训练失败 — unknown\n- mvp_v4_legacy_s035: 训练失败 — unknown\n- mvp_v4_float32_s030: 已被终止 — unknown\n- mvp_v5_fixed_s020: 已被终止 — unknown\n- mvp_v5_fixed_s030: 已被终止 — unknown\n- qwen_importance_s015: 已被终止 — unknown\n- qwen_importance_s020: 已被终止 — unknown\n- qwen_importance_s025: 已被终止 — unknown\n- qwen_importance_s030: 已被终止 — unknown\n- v6_random_s030: 训练失败 — unknown\n- v6_random_s030_r2: 训练失败 — unknown\n- bf16_random_s015: 已被终止 — unknown\n- bf16_random_s020: 已被终止 — unknown\n- bf16_random_s025: 已被终止 — unknown\n- bf16_random_s030: 已被终止 — unknown\n- bf16_qw
…[truncated 315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-14T13:05:29.087555+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-14T13:05:29.542013+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-14T13:05:29.542529+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
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

_source line 79 · 2026-05-14T13:05:29.593150+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-14T13:05:39.332235+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
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

_source line 81 · 2026-05-14T13:05:39.386671+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-14T13:05:41.097642+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-14T13:05:42.042943+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 945
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-14T13:05:42.043700+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-14T13:05:43.570637+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 1526
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-14T13:05:43.621370+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-14T13:05:43.874179+00:00_

-rw-r--r-- 1 ubuntu ubuntu 361431 May 14 13:02 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-14T13:06:10.331349+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
  }
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-14T13:06:11.135657+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-14T13:06:20.793057+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers and Shared Task Participation (CASE @ EMNLP 2022): Challenges and Applications of Automated Extraction of Socio-political Events from Text | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-and-shared-task-participation-case-emnlp-2022-challenges-and-applications"},{"title":"Joint Call for Workshops for NAACL/ACL/EMNLP 2025 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-workshops-naaclaclemnlp-2025"}]

Based on the search results, he
…[truncated 2442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 10461
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-14T13:06:20.845652+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9709
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-14T13:06:23.585774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 May submission format requirements page limits template anonymity",
  "allowed_domains": "['aclweb.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 May submission format requirements page limits template anonymity",
    "allowed_domains": "['aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 93 · 2026-05-14T13:06:24.040932+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 important dates deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 important dates deadline commitment"
  }
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-14T13:06:29.247130+00:00_

Web search results for query: "ACL ARR 2026 May submission format requirements page limits template anonymity"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"The 27th Annual Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/27th-annual-meeting-special-interest-group-discourse-and-dialogue"}]

Based on the search results, here's what I found about ACL ARR 2026 May submission format requirements:

## Page Limits

ARR submissions are in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

## A
…[truncated 959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5661
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-14T13:06:30.672135+00:00_

Web search results for query: "EMNLP 2026 important dates deadline commitment"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"}]

Based on the search results, here are the important dates and deadlines for EMNLP 2026:

## Conference Details
The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

## Important Deadlines


- ARR submission deadline (long & short papers): May 25, 2026
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
…[truncated 693 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6631
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-14T13:07:03.517256+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计与评估**\n\n### 论文信息\n- 论文路径：`artifacts/_project/paper/main.pdf`\n- 目标 venue：EMNLP 2026（Main Conference, Long Paper）\n- 提交通道：ACL Rolling Review (ARR) May 2026 cycle\n- Deadline：2026-05-25\n\n### Venue 格式要求（ARR May 2026）\n- 长文正文上限：**8 页**（不含参考文献和附录）\n- 模板：**ACL LaTeX 模板**（MS Word 模板自 2026年3月起会被 desk reject）\n- 匿名规则：**Double-blind**（不能出现作者信息、不能有去匿名化线索）\n- **Limitations 节**：必须存在，且为**独立无编号节**，置于 Conclusion 之后、References 之前。缺失会被 desk reject。\n- 附录：允许，不计入页数限制，但审稿人不保证阅读\n\n### 你的审查重点\n\n请重点评估以下方面：\n\n1. **方法论严谨性**\n   - 实验方法是否合理？统计方法是否正确使用？\n   - 是否存在方法学缺陷（如变量混淆、选择偏差）？\n   - Claim 是否有充分的证据支撑？结论是否过度泛化？\n\n2. **实验设计**\n   - 模型选择是否充分？是否覆盖足够的架构多样性？\n   - 数据集选择和规模是否合理？\n   - Baseline/对照实验是否充分？\n   - 评估指标是否全面？是否遗漏关键指标？\n\n3. **可重复性**\n   - 实验细节是否足以复现？\n   - 超参数、随机种子、硬件信息是否充分报告？\n   - 代码/数据是否承诺公开？\n\n4. **技术正确性**\n   - 数学公式是否正确？\n   - 表格/图表数据是否一致？\n   - 是否有明显的技术错误？\n\n### 输出格式\n\n请按以下结构输出审稿报告：\n1. 总体评分（ACL ARR Review Form 标准维度：Soundness, Excitement, Overall Assessment, Reproducibility, Confidence）\n2. Must-Fix 问题（标注 [critical]）\n3. Should-Fix 问题（标注 [major] 或 [minor]）\n4. 主要优势\n5. Questions for Authors\n6. 小问题列表"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计与评估**\n\n### 论文信息\n- 论文路径：`artifacts/_project/paper/main.pdf`\n- 目标 venue：EMNLP 2026（Main Conference, Long Paper）\n- 提交通道：ACL Rolling Review (ARR) May 2026 cycle\n- Deadline：2026-05-25\n\n### Venue 格式要求（ARR May 2026）\n- 长文正文上限：**8 页**（不含参考文献和附录）\n- 模板：**ACL LaTeX 模板**（MS Word 模板自 2026年3月起会被 desk reject）\n- 匿名规则：**Double-blind**（不能出现作者信息、不能有去匿名化线索）\n- **Limitations 节**：必须存在，且为**独立无编号节**，置于 Conclusion 之后、References 之前。缺失会被 desk reject。\n- 附录：允许，不计入页数限制，但审稿人不保证阅读\n\n### 你的审查重点\n\n请重点评估以下方面：\n\n1. **方法论严谨性**\n   - 实验方法是否合理？统计方法是否正确使用？\n   - 是否存在方法学缺陷（如变量混淆、选择偏差）？\n   - Claim 是否有充分的证据支撑？结论是否过度泛化？\n\n2. **实验设计**\n   - 模型选择是否充分？是否覆盖足够的架构多样性？\n   - 数据集选择和规模是否合理？\n   - Baseline/对照实验是否充分？\n   - 评估指标是否全面？是否遗漏关键指标？\n\n3. **可重复性**\n   - 实验细节是否足以复现？\n   - 超参数、随机种子、硬件信息是否充分报告？\n   - 代码/数据是否承诺公开？\n\n4. **技术正确性**\n   - 数学公式是否正确？\n   - 表格/图表数据是否一致？\n   - 是否有明显的技术错误？\n\n### 输出格式\n\n请按以下结构输出审稿报告：\n1. 总体评分（ACL ARR Review Form 标准维度：Soundness, Excitement, Overall Assessment, Reproducibility, Confidence）\n2. Must-Fix 问题（标注 [critical]）\n3. Should-Fix 问题（标注 [major] 或 [minor]）\n4. 主要优势\n5. Questions for Authors\n6. 小问题列表"
  }
}
```

</details>

---


### Tool call

_source line 97 · 2026-05-14T13:07:03.923866+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-14T13:07:16.941714+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13424
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-14T13:07:16.942295+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/decisions.yaml\", \"content\": \"_next_id: 52\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:44 UTC\\n  summary: MVP 方案：用 Interaction Index 跨 phase 差异验证核心假设\\n  rationale: 评审建议 novelty 锚定在 \\\"phase-dependent interaction direction reversal\\\"。MVP\\n    聚焦验证这一点：在 MATH-500 子集上 profiling DeepSeek-R1-Distill-Qwen-7B，用 ThinKV 方法切分 phases，计算\\n    attention × KV 的 Interaction Index。比全 grid search 更聚焦，直接验证核心 novelty 锚点。Pass =\\n    II 跨 phase 显著不同；Fail = II 恒定。预计 10-15 H100-hours。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:48 UTC\\n  summary: 向 Manager 申请 4×H100-80GB 租卡，预计 8-10 天，¥3200-5000\\n  rationale: 12 天截稿，4 GPU 并行可将日历时间压到 ~8 天（留 4 天 buffer）。2 GPU 需 11 天，buffer 不足 1 天，风险过高。用户明确授权\\\"几张都可以\\\"。GPU\\n    就绪 hard deadline 5/14 EOD。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 17:54 UTC\\n  summary: Throughput 策略：RTX 6000 Pro 做开发/accuracy，最终 throughput 短租 H100\\n  rationale: IDEA_BRIEF 硬约束要求\\\"Report wall-clock and throughput on H100\\\"，baseline 论文（Polar\\n    Sparsity、SeerAttention-R）均报告 H100 数字。RTX 6000 Pro (sm_89) vs H100 (sm_90) 的 kernel\\n    speedup 可能不同。策略(a)：RTX 6000 Pro 做全部开发+accuracy+ablation（硬件无关），仅 throughput 基准测试短租\\n    H100 ~2-4h（~$6-12）。比策略(b)全在 RTX 6000 Pro 上报告更有说服力，成本极低。H100 在 M5 阶段再申请。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 17:58 UTC\\n  summary: Throughput benchmark 硬件从 H100 改为 H20（Hopper sm_90，用户确认无 H100 可用）\\n  rationale: H20 与 H100 同为 Hopper sm_90，kernel 兼容无需额外适配。96GB HBM3 + 4TB/s 带宽适合 inference\\n    benchmark。在 H20 上重跑所有 baseline 确保公平比较，报告 relative speedup ratio（Hopper 架构内比值稳定）。H100\\n    不可用，H20 是最佳替代。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 18:01 UTC\\n  summary: GPU 从 4× RTX 6000 Pro 换为 4× H20-NVLink 96GB\\n  rationale:
…[truncated 1471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 13018
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-14T13:07:27.137590+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse -name \"*.yaml\" -path \"*/agent/*\" | head -5 && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse -name \"*.yaml\" -path \"*/agent/*\" | head -5 && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-14T13:07:27.598045+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 460
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-14T13:07:31.063815+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse -name \"config.yaml\" -o -name \"project.yaml\" | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse -name \"config.yaml\" -o -name \"project.yaml\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-14T13:07:31.214818+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-14T13:07:34.492925+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11 -maxdepth 2 -name \"config.yaml\" -o -name \"settings.yaml\" 2>/dev/null | head -10",
  "description": "Find config files at root level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11 -maxdepth 2 -name \"config.yaml\" -o -name \"settings.yaml\" 2>/dev/null | head -10",
    "description": "Find config files at root level"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-14T13:07:34.593815+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-14T13:07:37.660767+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rl \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rl \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-14T13:07:38.331849+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_director_b570dbd0/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_director_b570dbd0/AGENTS.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 671
}
```

</details>

---


### Assistant

_source line 108 · 2026-05-14T13:07:52.559652+00:00_

外部审稿未配置，跳过。

---

**圆桌审稿 Round 1 状态汇报**

| 项目 | 状态 |
|------|------|
| **投稿目标** | EMNLP 2026 Main Conference (Long Paper) |
| **提交通道** | ARR May 2026 cycle |
| **Deadline** | 2026-05-25 (11天后) |
| **论文 PDF** | `artifacts/_project/paper/main.pdf` ✓ |
| **Reviewer 编排** | 2 人（EMNLP 一般会议标准） |

**Reviewer 分工：**
- **Reviewer 1**：方法严谨性 + 实验设计与评估 — **已派发，等待返回**
- **Reviewer 2**：新颖性 + 相关工作 + 写作质量 + 格式合规 — **已完成（Weak Reject 2.5/5）**

**外部审稿**：项目未配置 paperreview.ai，跳过。

等待 Reviewer 1 完成后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 4

## Round 4

6 recorded events


### User

_source line 109 · 2026-05-14T13:07:52.573380+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**审查侧重：方法严谨性 + 实验设计 + 统计验证**

---

## 总体评分

**Overall**: 3/5 (Findings: Could be accepted to the Findings of the ACL)

**一句话总结**: 论文发现了一个有趣且可验证的现象（compound sparsity 的 phase-strategy 交互），实验设计有亮点（random eviction 作为 falsification control），但实验规模过小（n=50, 2 个同架构模型, 4 个 sparsity levels）、多处数值不一致、以及关键统计论证存在缺陷，不足以支撑论文标题和摘要中隐含的通用性声明。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心发现（phase-strategy interaction）有实验支撑，但多个 main claims 的证据不充分：monotonicity 仅基于 4 个数据点，cross-model ρ=1.0 统计功效极低，Qwen s=0.15 marginal result 被忽略 |
| Excitement | 3/5 | Phase-modulated severity 和 crossover 现象有学术价值，但论文止步于现象描述，未提出或验证 phase-aware controller，实际影响有限 |
| Reproducibility | 3/5 | 提供了模型名称、sparsity levels、统计方法细节，但未提供代码/数据、50 题选择标准不透明、随机种子未完整报告 |
| Confidence | 4/5 | 仔细阅读了全文及附录，逐条核验了统计数据和方程 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 数值不一致：摘要/正文/表格之间存在矛盾数据

- 具体位置：Abstract vs. §5.1 (p.4) vs. Table 1 (p.4)
- 问题：
  - Abstract 和 Table 1 报告 DeepSeek s=0.30 时 Δ=14.59，但 §5.1 第一段（p.4 左栏）写 "Δ increases from 0.39 at s=0.15 to **11.59** at s=0.30"。14.59 与 11.59 不一致。
  - 主文（Table 1 标题、§4.2、§5 全文）均声称 DeepSeek n=50，但 Appendix E（p.11）明确写 "paired permutation test yields **n=49** paired problems for DeepSeek (1 excluded)"。
  - §6.2（p.7）声称 DeepSeek "ΔH ∈ [−0.080, −0.047]"，但 Table 7（p.12）显示 ΔH 范围为 [−0.047, −0.040]。
- 为什么影响接收：多处数值矛盾损害论文可信度，审稿人无法确定哪组数字是正确的。
- 建议修改方向：逐一核对所有数值，确保摘要、正文、表格、附录完全一致。

**N2** [critical] Cross-model Spearman ρ=1.0（n=4）作为 "replication" 证据在统计上无意义

- 具体位置：§5.4 (p.6)
- 问题：4 个数据点的 Spearman ρ=1.0 → p=1/24≈0.042。统计功效极低，无法区分任何单调关系的具体形式；未做 Bonferroni 修正（论文其他检验均做了）；p=0.04 修正后不再显著。论文却据此在 §7 声称 "perfect ordinal agreement" 作为泛化性主要论据。
- 建议修改方向：承认 n=4 rank correlation 功效不足；转而强调 Table 4 中两个模型各自独立的 d_z 递增轨迹；降低泛化性声明力度。

**N3** [critical] 样本量不足以支撑核心声明的稳健性

- 具体位置：§4.2 (p.4)
- 问题：n=50（实际 49/46），右偏分布下 median 估计不稳定。s=0.30 Bootstrap CI=[0.70, 16.29]（Appendix E），跨越一个数量级。问题选择的 random seed 未报告。
- 建议修改方向：做 split-half stability analysis；报告 seed 和 category 分布；理想应扩大到完整 MATH-500。

**N4** [critical] Severity gradient G 定义数值不稳定，69×–274× 数字具有误导性

- 具体位置：Eq. 5 (§3.2), Table 2 (p.6)
- 问题：G = Π̃_low / Π̃_high，分母 Π̃_high = 0.006–0.053 接近零，G 对分母微小变化极度敏感。正文 p.4 称 G "from 0⁺ at s=0.15"，但 Table 2 显示 G=69。ε 阈值未说明取值。
- 建议修改方向：报告 G 的 bootstrap CI；做 sensitivity analysis；弱化 G 的 headline 地位，改用更稳健的 Δ。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Qwen s=0.15 marginal（d_z=0.28, CI含零）与摘要 unqualified monotonicity 声明矛盾
**W2** [major] 仅 2 个同 Qwen2 架构模型，"Transformer-based reasoning" 泛化声明过度
**W3** [major] Phase segmentation 用 attention sparsity 定义 phase，与 attention-dependent outcome 存在概念耦合/confounding
**W4** [major] 仅 4 个 sparsity levels 不足以论证 "monotonic growth" 或分析增长形状
**W5** [major] Cohen's d 解读不准确（0.44≠small, 0.80=threshold of large）；摘要写 0.41 但正文写 0.44
**W6** [major] 缺少 task accuracy 评估（仅 PPL），无法判断 severity gradient 的实际部署影响
**W7** [warning] Limitations 节格式违反 ACL/ARR 要求（应为 Conclusion 后独立无编号节）

---

## 小问题
- h2o-neurips2023 bib 条目缺少 title 字段
- 7 个 orphan bib entries 需清理
- 对称 sparsity budget 限制应更突出讨论
- n=49/46 的 exclusion criteria 应在主文交代

---

## Questions for Authors
1. §5.1 的 "11.59" 与 Table 1 的 "14.59" 哪个正确？
2. n=50 还是 n=49？排除标准？
3. 是否做过 split-half stability analysis？
4. 用 token position 等分或 &lt;think>/<\/think> 标记做 phase segmentation 结果如何？
5. G 的 bootstrap 95% CI？
6. 各条件下 MATH-500 solve rate？
7. Cohen's d 摘要写 0.41 但正文写 0.44，哪个正确？

---

## Missing References
- Cohen (1988) Statistical Power Analysis
- RaaS (Hu et al., 2025) 在 bib 中未被引用
- Per-layer 非对称 sparsity 方法（OWL, Wanda）

---

## 主要优势
- Random eviction 作为 falsification control 是优秀的实验设计（7/8 null results）
- Entropy-discrimination collapse 机制提供了可检验的因果解释
- 论文组织清晰，C1-C6 逐一对应
- Phase-strategy crossover 是有趣的定性发现
- 统计方法论整体合理（median + nonparametric bootstrap + permutation + Bonferroni）

---

**Overall Score**: Borderline (3/5 — Findings-level)
**Confidence**: 4/5

核心发现有价值但实验规模不足、数值不一致问题严重。修正 N1-N4 后可达 Findings 接收水平，当前状态不适合 main conference。

---

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：4 个 critical 问题（数值不一致、ρ=1.0 with n=4 统计无效、样本量不足、G 定义不稳定）+ 7 个 major 问题。Overall 3/5（Findings-level），核心发现有价值但当前证据强度不够支撑 main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-14T13:09:05.123601+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你审查侧重（方法严谨性 + 实验评估）相关的发现是否一致或有分歧。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n**Overall**: 2.5/5（Weak Reject）\n**一句话总结**: 本文报告了一个有趣的实证发现（compound sparsity severity 随推理阶段变化），但贡献停留在现象描述层面——没有提出方法、没有解决方案，且实验规模和架构覆盖不足以支撑其 claim 的普遍性；相关工作遗漏严重，格式存在 ARR 合规问题。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claim 有统计支撑，但方法学局限（2 模型同架构、50 题、仅用 PPL）削弱泛化性；entropy-discrimination collapse 机制仅有相关性证据 |\n| Excitement | 2/5 | 发现本身有趣但贡献有限——纯分析无方法/解决方案；作为 main conference 长文偏薄 |\n| Overall Assessment | 2.5/5 | 需实质性修订：扩展实验（跨架构、更大规模）、补充缺失引用、修正格式后可能适合 Findings |\n| Reproducibility | 3.5/5 | 实验设置详细，统计方法透明，但 50 题 subset 选取细节不够、代码未提及公开 |\n| Confidence | 4/5 | 对 KV cache compression 和 attention sparsity 文献较熟悉 |\n\n### Must-Fix 问题\n\n**N1** [critical] Limitations 节格式不符合 ARR 要求\n- 位置：§7.1（第 7 页）\n- 当前为 §7 Discussion 的编号子节（§7.1），ARR 要求无编号独立节置于 Conclusion 之后、References 之前。属于 desk reject 检查项。\n\n**N2** [critical] 相关工作遗漏严重\n- 位置：§2 Related Work\n- 极高优先级遗漏：Lethe（AAAI 2026，phase-aware KV pruning 同期竞争工作）、R-KV（NeurIPS 2025，推理模型 KV 压缩最强 baseline）、\"Hold Onto That Thought\"（NeurIPS 2025，唯一系统评估推理任务 KV 压缩的工作）\n- 高优先级遗漏：Scissorhands（NeurIPS 2023）、FastGen（ICLR 2024）、StreamingLLM（ICLR 2024）、LLM-Pruner（NeurIPS 2023）、Titanus（GLSVLSI 2025）\n\n**N3** [critical] 贡献深度不足\n- 纯分析无方法/解决方案。§7 提到 \"phase-aware controller\" 但停留在 future work。对 EMNLP main conference 长文偏薄，更适合 Findings。\n\n**N4** [critical] 实验规模和多样性不足\n- 仅 2 个模型共享 Qwen2 架构，\"cross-model replication\" 措辞有误导性\n- 仅 50 道 MATH-500 题\n- 仅 7B 规模\n- 仅用 PPL 作为质量指标，缺少 accuracy——PPL 恶化不等于答案错误\n\n### Should-Fix 问题\n\n**W1** [major] Entropy-discrimination collapse 因果证据不足（Table 5 仅相关性，缺 intervention 实验）\n**W2** [major] Bibliography 管理混乱——7 条 orphan entries（bib 有但正文未引），h2o-neurips2023 title 字段为空\n**W3** [major] Abstract 约 600+ 词，远超通常 150-250 词建议\n**W4** [major] Footnote 2 泄露 \"4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB GPUs\"，去匿名化风险\n**W5** [minor] \"Severity gradient\" 术语过载（同时指标和概念）\n**W6** [minor] Appendix B 与 Appendix D 文本几乎完全重复，疑为粘贴错误\n**W7** [minor] 方程编号可能不连续（Eq. 2 位置不明）\n\n### 小问题\n- §6.3 PyramidKV 被引用两次且用不同作者信息\n- Footnote 1 措辞不清 \"float16 eliminated entirely\"\n- Table 3 caption 公式有多余项 \"− Ĥ_dist\"\n- 部分 bib 年份与 OpenAlex 不一致（adakv-neurips2025 实际 2024、pope-mlsys2023 实际 2022）\n\n### Missing References\n\n| 优先级 | 论文 | Venue | 理由 |\n|--------|------|-------|------|\n| 极高 | Lethe (Zeng et al.) | AAAI 2026 | 与本文 phase-gated 思路直接重叠 |\n| 极高 | R-KV (Cai et al.) | NeurIPS 2025 | 推理模型 KV 压缩最强 baseline |\n| 极高 | Hold Onto That Thought | NeurIPS 2025 | 唯一系统评估推理任务 KV 压缩 |\n| 高 | Scissorhands (Liu et al.) | NeurIPS 2023 | KV eviction 基础方法 |\n| 高 | FastGen (Ge et al.) | ICLR 2024 | Per-head adaptive KV cache |\n| 高 | StreamingLLM (Xiao et al.) | ICLR 2024 | Attention sink 基础 |\n| 高 | LLM-Pruner (Ma et al.) | NeurIPS 2023 | Coupled pruning 开创性工作 |\n| 高 | Titanus (Chen et al.) | GLSVLSI 2025 | KV pruning+quantization 复合效果 |\n| 中 | SparseGPT | ICML 2023 | 权重稀疏化基础 |\n| 中 | Wanda | ICLR 2024 | 轻量 pruning |\n| 中 | MInference | NeurIPS 2024 | 注意力稀疏模式分析 |\n\n### 主要优势\n1. 研究问题有价值——compound sparsity 的 phase-dependent behavior 确实未被充分研究\n2. 统计方法论优秀（permutation tests, bootstrap CI, Bonferroni correction, paired effect sizes）\n3. Random eviction 作为 falsification control 的实验设计巧妙\n4. Crossover 现象（§5.3）是 non-trivial 且有实际意义的发现\n5. 写作总体清晰，§5 结果层层递进\n\n### Questions for Authors\n1. 为什么不报告 MATH-500 accuracy？PPL 下降是否对应答案正确率下降？\n2. 与 Lethe（AAAI 2026）的区别和互补？\n3. 是否考虑过 LLaMA-3 或 Mistral 上的验证？\n4. Entropy-discrimination collapse 能否通过 intervention 实验验证因果性？\n5. Appendix B 和 D 文本重复是编辑错误吗？\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和关键 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你审查侧重（方法严谨性 + 实验评估）相关的发现是否一致或有分歧。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n**Overall**: 2.5/5（Weak Reject）\n**一句话总结**: 本文报告了一个有趣的实证发现（compound sparsity severity 随推理阶段变化），但贡献停留在现象描述层面——没有提出方法、没有解决方案，且实验规模和架构覆盖不足以支撑其 claim 的普遍性；相关工作遗漏严重，格式存在 ARR 合规问题。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claim 有统计支撑，但方法学局限（2 模型同架构、50 题、仅用 PPL）削弱泛化性；entropy-discrimination collapse 机制仅有相关性证据 |\n| Excitement | 2/5 | 发现本身有趣但贡献有限——纯分析无方法/解决方案；作为 main conference 长文偏薄 |\n| Overall Assessment | 2.5/5 | 需实质性修订：扩展实验（跨架构、更大规模）、补充缺失引用、修正格式后可能适合 Findings |\n| Reproducibility | 3.5/5 | 实验设置详细，统计方法透明，但 50 题 subset 选取细节不够、代码未提及公开 |\n| Confidence | 4/5 | 对 KV cache compression 和 attention sparsity 文献较熟悉 |\n\n### Must-Fix 问题\n\n**N1** [critical] Limitations 节格式不符合 ARR 要求\n- 位置：§7.1（第 7 页）\n- 当前为 §7 Discussion 的编号子节（§7.1），ARR 要求无编号独立节置于 Conclusion 之后、References 之前。属于 desk reject 检查项。\n\n**N2** [critical] 相关工作遗漏严重\n- 位置：§2 Related Work\n- 极高优先级遗漏：Lethe（AAAI 2026，phase-aware KV pruning 同期竞争工作）、R-KV（NeurIPS 2025，推理模型 KV 压缩最强 baseline）、\"Hold Onto That Thought\"（NeurIPS 2025，唯一系统评估推理任务 KV 压缩的工作）\n- 高优先级遗漏：Scissorhands（NeurIPS 2023）、FastGen（ICLR 2024）、StreamingLLM（ICLR 2024）、LLM-Pruner（NeurIPS 2023）、Titanus（GLSVLSI 2025）\n\n**N3** [critical] 贡献深度不足\n- 纯分析无方法/解决方案。§7 提到 \"phase-aware controller\" 但停留在 future work。对 EMNLP main conference 长文偏薄，更适合 Findings。\n\n**N4** [critical] 实验规模和多样性不足\n- 仅 2 个模型共享 Qwen2 架构，\"cross-model replication\" 措辞有误导性\n- 仅 50 道 MATH-500 题\n- 仅 7B 规模\n- 仅用 PPL 作为质量指标，缺少 accuracy——PPL 恶化不等于答案错误\n\n### Should-Fix 问题\n\n**W1** [major] Entropy-discrimination collapse 因果证据不足（Table 5 仅相关性，缺 intervention 实验）\n**W2** [major] Bibliography 管理混乱——7 条 orphan entries（bib 有但正文未引），h2o-neurips2023 title 字段为空\n**W3** [major] Abstract 约 600+ 词，远超通常 150-250 词建议\n**W4** [major] Footnote 2 泄露 \"4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB GPUs\"，去匿名化风险\n**W5** [minor] \"Severity gradient\" 术语过载（同时指标和概念）\n**W6** [minor] Appendix B 与 Appendix D 文本几乎完全重复，疑为粘贴错误\n**W7** [minor] 方程编号可能不连续（Eq. 2 位置不明）\n\n### 小问题\n- §6.3 PyramidKV 被引用两次且用不同作者信息\n- Footnote 1 措辞不清 \"float16 eliminated entirely\"\n- Table 3 caption 公式有多余项 \"− Ĥ_dist\"\n- 部分 bib 年份与 OpenAlex 不一致（adakv-neurips2025 实际 2024、pope-mlsys2023 实际 2022）\n\n### Missing References\n\n| 优先级 | 论文 | Venue | 理由 |\n|--------|------|-------|------|\n| 极高 | Lethe (Zeng et al.) | AAAI 2026 | 与本文 phase-gated 思路直接重叠 |\n| 极高 | R-KV (Cai et al.) | NeurIPS 2025 | 推理模型 KV 压缩最强 baseline |\n| 极高 | Hold Onto That Thought | NeurIPS 2025 | 唯一系统评估推理任务 KV 压缩 |\n| 高 | Scissorhands (Liu et al.) | NeurIPS 2023 | KV eviction 基础方法 |\n| 高 | FastGen (Ge et al.) | ICLR 2024 | Per-head adaptive KV cache |\n| 高 | StreamingLLM (Xiao et al.) | ICLR 2024 | Attention sink 基础 |\n| 高 | LLM-Pruner (Ma et al.) | NeurIPS 2023 | Coupled pruning 开创性工作 |\n| 高 | Titanus (Chen et al.) | GLSVLSI 2025 | KV pruning+quantization 复合效果 |\n| 中 | SparseGPT | ICML 2023 | 权重稀疏化基础 |\n| 中 | Wanda | ICLR 2024 | 轻量 pruning |\n| 中 | MInference | NeurIPS 2024 | 注意力稀疏模式分析 |\n\n### 主要优势\n1. 研究问题有价值——compound sparsity 的 phase-dependent behavior 确实未被充分研究\n2. 统计方法论优秀（permutation tests, bootstrap CI, Bonferroni correction, paired effect sizes）\n3. Random eviction 作为 falsification control 的实验设计巧妙\n4. Crossover 现象（§5.3）是 non-trivial 且有实际意义的发现\n5. 写作总体清晰，§5 结果层层递进\n\n### Questions for Authors\n1. 为什么不报告 MATH-500 accuracy？PPL 下降是否对应答案正确率下降？\n2. 与 Lethe（AAAI 2026）的区别和互补？\n3. 是否考虑过 LLaMA-3 或 Mistral 上的验证？\n4. Entropy-discrimination collapse 能否通过 intervention 实验验证因果性？\n5. Appendix B 和 D 文本重复是编辑错误吗？\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和关键 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-14T13:09:43.645576+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 38521
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-14T13:09:44.101522+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你审查侧重（新颖性 + 相关工作 + 写作 + 格式）相关的发现是否一致或有分歧。\n\n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**审查侧重：方法严谨性 + 实验设计 + 统计验证**\n\n**Overall**: 3/5 (Findings-level)\n**一句话总结**: 论文发现了一个有趣且可验证的现象（compound sparsity 的 phase-strategy 交互），实验设计有亮点（random eviction 作为 falsification control），但实验规模过小（n=50, 2 个同架构模型, 4 个 sparsity levels）、多处数值不一致、以及关键统计论证存在缺陷，不足以支撑论文标题和摘要中隐含的通用性声明。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心发现（phase-strategy interaction）有实验支撑，但多个 main claims 的证据不充分：monotonicity 仅基于 4 个数据点，cross-model ρ=1.0 统计功效极低，Qwen s=0.15 marginal result 被忽略 |\n| Excitement | 3/5 | Phase-modulated severity 和 crossover 现象有学术价值，但论文止步于现象描述，未提出或验证 phase-aware controller，实际影响有限 |\n| Reproducibility | 3/5 | 提供了模型名称、sparsity levels、统计方法细节，但未提供代码/数据、50 题选择标准不透明、随机种子未完整报告 |\n| Confidence | 4/5 | 仔细阅读了全文及附录，逐条核验了统计数据和方程 |\n\n### Must-Fix 问题\n\n**N1** [critical] 数值不一致：摘要/正文/表格之间存在矛盾数据\n- Abstract 和 Table 1 报告 DeepSeek s=0.30 时 Δ=14.59，但 §5.1 第一段（p.4 左栏）写 \"Δ increases from 0.39 at s=0.15 to **11.59** at s=0.30\"。14.59 与 11.59 不一致。\n- 主文（Table 1 标题、§4.2、§5 全文）均声称 DeepSeek n=50，但 Appendix E（p.11）明确写 \"paired permutation test yields **n=49** paired problems for DeepSeek (1 excluded)\"。\n- §6.2（p.7）声称 DeepSeek \"ΔH ∈ [−0.080, −0.047]\"，但 Table 7（p.12）显示 ΔH 范围为 [−0.047, −0.040]。\n\n**N2** [critical] Cross-model Spearman ρ=1.0（n=4）作为 \"replication\" 证据在统计上无意义\n- 4 个数据点的 Spearman ρ=1.0 → p=1/24≈0.042。统计功效极低，无法区分任何单调关系的具体形式；未做 Bonferroni 修正（论文其他检验均做了）；p=0.04 修正后不再显著。\n\n**N3** [critical] 样本量不足以支撑核心声明的稳健性\n- n=50（实际 49/46），右偏分布下 median 估计不稳定。s=0.30 Bootstrap CI=[0.70, 16.29]（Appendix E），跨越一个数量级。\n\n**N4** [critical] Severity gradient G 定义数值不稳定，69×–274× 数字具有误导性\n- G = Π̃_low / Π̃_high，分母 Π̃_high = 0.006–0.053 接近零，G 对分母微小变化极度敏感。ε 阈值未说明取值。\n\n### Should-Fix 问题\n\n**W1** [major] Qwen s=0.15 marginal（d_z=0.28, CI含零）与摘要 unqualified monotonicity 声明矛盾\n**W2** [major] 仅 2 个同 Qwen2 架构模型，\"Transformer-based reasoning\" 泛化声明过度\n**W3** [major] Phase segmentation 用 attention sparsity 定义 phase，与 attention-dependent outcome 存在概念耦合/confounding\n**W4** [major] 仅 4 个 sparsity levels 不足以论证 \"monotonic growth\" 或分析增长形状\n**W5** [major] Cohen's d 解读不准确（0.44≠small, 0.80=threshold of large）；摘要写 0.41 但正文写 0.44\n**W6** [major] 缺少 task accuracy 评估（仅 PPL），无法判断 severity gradient 的实际部署影响\n**W7** [warning] Limitations 节格式违反 ACL/ARR 要求（应为 Conclusion 后独立无编号节）\n\n### 小问题\n- h2o-neurips2023 bib 条目缺少 title 字段\n- 7 个 orphan bib entries 需清理\n- 对称 sparsity budget 限制应更突出讨论\n- n=49/46 的 exclusion criteria 应在主文交代\n\n### Questions for Authors\n1. §5.1 的 \"11.59\" 与 Table 1 的 \"14.59\" 哪个正确？\n2. n=50 还是 n=49？排除标准？\n3. 是否做过 split-half stability analysis？\n4. 用 token position 等分或 &lt;think>/<\\/think> 标记做 phase segmentation 结果如何？\n5. G 的 bootstrap 95% CI？\n6. 各条件下 MATH-500 solve rate？\n7. Cohen's d 摘要写 0.41 但正文写 0.44，哪个正确？\n\n### Missing References\n- Cohen (1988) Statistical Power Analysis\n- RaaS (Hu et al., 2025) 在 bib 中未被引用\n- Per-layer 非对称 sparsity 方法（OWL, Wanda）\n\n### 主要优势\n- Random eviction 作为 falsification control 是优秀的实验设计（7/8 null results）\n- Entropy-discrimination collapse 机制提供了可检验的因果解释\n- 论文组织清晰，C1-C6 逐一对应\n- Phase-strategy crossover 是有趣的定性发现\n- 统计方法论整体合理（median + nonparametric bootstrap + permutation + Bonferroni）\n\n**Overall Score**: Borderline (3/5 — Findings-level)\n**Confidence**: 4/5\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和关键 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你审查侧重（新颖性 + 相关工作 + 写作 + 格式）相关的发现是否一致或有分歧。\n\n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**审查侧重：方法严谨性 + 实验设计 + 统计验证**\n\n**Overall**: 3/5 (Findings-level)\n**一句话总结**: 论文发现了一个有趣且可验证的现象（compound sparsity 的 phase-strategy 交互），实验设计有亮点（random eviction 作为 falsification control），但实验规模过小（n=50, 2 个同架构模型, 4 个 sparsity levels）、多处数值不一致、以及关键统计论证存在缺陷，不足以支撑论文标题和摘要中隐含的通用性声明。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心发现（phase-strategy interaction）有实验支撑，但多个 main claims 的证据不充分：monotonicity 仅基于 4 个数据点，cross-model ρ=1.0 统计功效极低，Qwen s=0.15 marginal result 被忽略 |\n| Excitement | 3/5 | Phase-modulated severity 和 crossover 现象有学术价值，但论文止步于现象描述，未提出或验证 phase-aware controller，实际影响有限 |\n| Reproducibility | 3/5 | 提供了模型名称、sparsity levels、统计方法细节，但未提供代码/数据、50 题选择标准不透明、随机种子未完整报告 |\n| Confidence | 4/5 | 仔细阅读了全文及附录，逐条核验了统计数据和方程 |\n\n### Must-Fix 问题\n\n**N1** [critical] 数值不一致：摘要/正文/表格之间存在矛盾数据\n- Abstract 和 Table 1 报告 DeepSeek s=0.30 时 Δ=14.59，但 §5.1 第一段（p.4 左栏）写 \"Δ increases from 0.39 at s=0.15 to **11.59** at s=0.30\"。14.59 与 11.59 不一致。\n- 主文（Table 1 标题、§4.2、§5 全文）均声称 DeepSeek n=50，但 Appendix E（p.11）明确写 \"paired permutation test yields **n=49** paired problems for DeepSeek (1 excluded)\"。\n- §6.2（p.7）声称 DeepSeek \"ΔH ∈ [−0.080, −0.047]\"，但 Table 7（p.12）显示 ΔH 范围为 [−0.047, −0.040]。\n\n**N2** [critical] Cross-model Spearman ρ=1.0（n=4）作为 \"replication\" 证据在统计上无意义\n- 4 个数据点的 Spearman ρ=1.0 → p=1/24≈0.042。统计功效极低，无法区分任何单调关系的具体形式；未做 Bonferroni 修正（论文其他检验均做了）；p=0.04 修正后不再显著。\n\n**N3** [critical] 样本量不足以支撑核心声明的稳健性\n- n=50（实际 49/46），右偏分布下 median 估计不稳定。s=0.30 Bootstrap CI=[0.70, 16.29]（Appendix E），跨越一个数量级。\n\n**N4** [critical] Severity gradient G 定义数值不稳定，69×–274× 数字具有误导性\n- G = Π̃_low / Π̃_high，分母 Π̃_high = 0.006–0.053 接近零，G 对分母微小变化极度敏感。ε 阈值未说明取值。\n\n### Should-Fix 问题\n\n**W1** [major] Qwen s=0.15 marginal（d_z=0.28, CI含零）与摘要 unqualified monotonicity 声明矛盾\n**W2** [major] 仅 2 个同 Qwen2 架构模型，\"Transformer-based reasoning\" 泛化声明过度\n**W3** [major] Phase segmentation 用 attention sparsity 定义 phase，与 attention-dependent outcome 存在概念耦合/confounding\n**W4** [major] 仅 4 个 sparsity levels 不足以论证 \"monotonic growth\" 或分析增长形状\n**W5** [major] Cohen's d 解读不准确（0.44≠small, 0.80=threshold of large）；摘要写 0.41 但正文写 0.44\n**W6** [major] 缺少 task accuracy 评估（仅 PPL），无法判断 severity gradient 的实际部署影响\n**W7** [warning] Limitations 节格式违反 ACL/ARR 要求（应为 Conclusion 后独立无编号节）\n\n### 小问题\n- h2o-neurips2023 bib 条目缺少 title 字段\n- 7 个 orphan bib entries 需清理\n- 对称 sparsity budget 限制应更突出讨论\n- n=49/46 的 exclusion criteria 应在主文交代\n\n### Questions for Authors\n1. §5.1 的 \"11.59\" 与 Table 1 的 \"14.59\" 哪个正确？\n2. n=50 还是 n=49？排除标准？\n3. 是否做过 split-half stability analysis？\n4. 用 token position 等分或 &lt;think>/<\\/think> 标记做 phase segmentation 结果如何？\n5. G 的 bootstrap 95% CI？\n6. 各条件下 MATH-500 solve rate？\n7. Cohen's d 摘要写 0.41 但正文写 0.44，哪个正确？\n\n### Missing References\n- Cohen (1988) Statistical Power Analysis\n- RaaS (Hu et al., 2025) 在 bib 中未被引用\n- Per-layer 非对称 sparsity 方法（OWL, Wanda）\n\n### 主要优势\n- Random eviction 作为 falsification control 是优秀的实验设计（7/8 null results）\n- Entropy-discrimination collapse 机制提供了可检验的因果解释\n- 论文组织清晰，C1-C6 逐一对应\n- Phase-strategy crossover 是有趣的定性发现\n- 统计方法论整体合理（median + nonparametric bootstrap + permutation + Bonferroni）\n\n**Overall Score**: Borderline (3/5 — Findings-level)\n**Confidence**: 4/5\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和关键 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-14T13:09:45.627439+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1525
}
```

</details>

---


### Assistant

_source line 114 · 2026-05-14T13:09:54.625795+00:00_

交叉分享已发出。两位 Reviewer 正在互审对方意见，等待 `[AGREE]`/`[REBUT]` 回应返回后进入收敛判断（Step 3）。

当前进度：
- **Step 0** ✅ Venue 调研完成（EMNLP 2026 / ARR May cycle / 8页长文 / double-blind）
- **Step 0.5** ✅ 编排决定：2 名 Reviewer（R1 方法+实验，R2 新颖性+格式）
- **Step 1** ✅ 两位 Reviewer 独立初审完成
- **Step 2** ⏳ 交叉分享已派发，等待回应
- 外部审稿：未配置，跳过

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 5

## Round 5

6 recorded events


### User

_source line 115 · 2026-05-14T13:13:29.067346+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（Round 1）

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析
**Reviewer Confidence**: 4/5（仔细阅读全文含附录，熟悉 KV cache / attention pruning / 统计方法相关工作）

---

## 总体评分

**Overall**: 2.5/5（介于 "needs substantial revisions" 和 "Findings track" 之间）

**一句话总结**: 研究问题有意义，但 n=50 的样本量、同架构"跨模型"验证、以及核心 severity gradient 指标 G 的近零分母问题，使论文的 claims 远超其证据承载力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心指标 G 受近零分母放大，n=50 统计功效不足，因果机制仅为相关性 |
| Excitement | 3/5 | 研究问题（compound sparsity 的 phase-strategy 交互）有实际价值，但执行不足以支撑强 claims |
| Reproducibility | 3/5 | 实验描述基本充分但缺代码、未指定 MATH-500 子集、部分关键数据仅在 appendix |
| Overall Assessment | 2.5/5 | 需大幅修改后重投 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 样本量严重不足，统计功效存疑

- 具体位置：Section 4（"50 problems from MATH-500"）、Table 1、Section 5.4（Qwen n=46）
- 问题：仅用 MATH-500 的 10%（50 题），每题 1 次 greedy decoding，无重复采样。Bonferroni 校正后（α=0.0125），paired nonparametric test 对 n=50 的最小可检测 Cohen's d_z ≈ 0.48。论文自己报告 Qwen s=0.15 的 d_z=0.28（Table 5），远低于此阈值，bootstrap CI 包含零。论文承认该条件"marginal"，但仍在 abstract 中将 Qwen 复现作为核心 claim（"replicates at s≥0.20"），给读者造成全面复现的印象。
- 更根本的问题：50 题 → 3 phases × 4 sparsity levels → 每个条件的 per-problem II 是一个点估计的 median。当分布右偏至 mean/median ratio 43:1（Section 4），median 的 bootstrap CI 会非常宽，50 个样本是否足以稳定估计值高度可疑。
- 为什么影响接收：样本量不足直接威胁所有定量 claims 的可靠性。
- 建议：(1) 使用全部 500 题；(2) 报告 post-hoc power analysis；(3) 至少对关键条件做 multiple generation seeds 验证稳定性。

**N2** [critical] Severity gradient G 的近零分母问题使 "69×–274×" 数字不可靠

- 具体位置：Eq. 2（G = Π̃_high / Π̃_low）、Section 5.2、Table 2
- 问题：G 是两个 phase 的 median II 之比。Table 2 显示 importance-based eviction 下，high-sparsity phase 的 II 值极小（s=0.15 时 II_high ≈ 0.006）。当分母接近零时，比值对噪声极其敏感——II_high 从 0.006 变为 0.012 就会使 G 减半。论文的核心标题数字 "69×–274×" 本质上是一个近零分母的放大效应，而非反映有意义的 phase 间差异。
- 与此对照：Table 1 的 Δ（中位差）从 0.39 到 14.59，增长 ~37×，这个数字更稳健但远不如 "69×–274×" 震撼。
- 为什么影响接收：论文的核心叙事围绕 "order of magnitude" severity gradient 展开（标题、abstract、conclusion 反复强调），如果这个数字是分母噪声驱动的，整个叙事的基础就不稳固。
- 建议：(1) 报告 G 的 bootstrap CI（当分母含零时 CI 应包含 ∞）；(2) 改用更稳健的效应量指标（如 standardized median difference 或 rank-based measure）；(3) 至少同时报告绝对差异 Δ 和比值 G，不要只依赖 G 做核心叙事。

**N3** [critical] "跨模型复现"使用同一架构，严重高估了泛化性

- 具体位置：Section 5.4、Appendix F（"Both models share the Qwen2ForCausalLM backbone"）
- 问题：DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 共享完全相同的 Qwen2 架构（28 layers, 28 heads, 4-group GQA）。论文用 "cross-model replication"（Section 5.4 标题）来描述这个验证，但实际验证的只是"同一架构不同训练方式下的复现性"。这不排除观察到的现象是 Qwen2 GQA 特定 attention pattern 的 artifact。
- Appendix F 自己承认 per-problem concordance 不显著（mean ρ = −0.11），即两个模型在 problem 层面的 severity pattern 并不一致，削弱了 "robust replication" 的说法。
- Qwen 的效应在 s=0.15 不显著（d_z=0.28, CI 含零），且全部效应量级仅为 DeepSeek 的 ~1/5，更像是 marginal replication 而非 robust replication。
- 为什么影响接收：泛化性声称是论文 contribution 的核心组成部分（Contribution #2），但证据远不足以支撑。
- 建议：(1) 至少增加一个架构不同的模型（如 LLaMA 3.x 或 Mistral）；(2) 将 "cross-model" 改为 "cross-training-regime"；(3) 明确讨论 GQA 架构可能的 confound。

**N4** [critical] Discrimination collapse 机制仅有相关性证据，被呈现为因果解释

- 具体位置：Section 5.6、Table 6（Appendix H）
- 问题：论文的第三个 contribution 是 "entropy-discrimination collapse as a mechanistic explanation"（Section 1）。但证据仅为：(1) head pruning 后 Gini coefficient 下降（Table 6），(2) 这种下降在 low-sparsity phase 更大。从 Gini 下降到 "这就是 severity gradient 的原因" 是一个逻辑跳跃——存在多种混杂因素（head 功能冗余程度的 phase 差异、token-level perplexity 的 baseline 差异等）未被排除。
- 更严重的问题：Appendix K 的 entropy redistribution 分析在 Qwen 上部分不复现（s=0.25 反转），论文承认这是 "model-dependent"。如果机制解释的一半在第二个模型上不成立，这不是 "robust mechanism"。
- 为什么影响接收：论文将 discrimination collapse 提升为 contribution 级别的声明，但证据级别仅为 observational correlation，不足以称为 "mechanism"。
- 建议：(1) 做 causal intervention——人为控制 entropy/Gini 后观察 severity gradient 变化；(2) 或者降低 claim 强度，改为 "a correlational pattern consistent with discrimination collapse" 而非 "mechanistic explanation"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Interaction Index 的 additive null 与论文自身论述存在内在矛盾

- 具体位置：Eq. 1（II = r_b − r_a − r_k + 1）、Section 3（"the two axes operate on disjoint dimensions"）、Section 3 同页（"head pruning affects the importance ranking used for eviction"）
- 问题：论文选择 additive null 的理由是 "两个轴操作在不同维度上"（structural vs. positional）。但论文的核心发现正是这两个轴存在交互——head pruning 改变了 importance ranking 从而影响 KV eviction 的质量。这意味着 additive null 作为基线的假设前提（轴间独立）和论文的核心论点（轴间交互）是矛盾的。
- Appendix B 验证 multiplicative null 给出相似结论，这很好但不够——问题不在于 additive vs multiplicative，而在于 perplexity ratio 空间本身是否是衡量交互效应的正确空间。PPL 是 cross-entropy 的指数函数，在 PPL ratio 空间的 additive interaction 对应概率空间的复杂非线性关系。
- 建议：增加 cross-entropy 空间的 interaction analysis 作为 robustness check。

**W2** [warning] Phase segmentation 缺乏 sensitivity analysis

- 具体位置：Section 3（"quantile-based tercile"）、Appendix A
- 问题：tercile 切分是一个关键设计选择，但论文未报告任何 sensitivity analysis。不同切分方式（quartile、基于阈值而非分位数、不同 min_phase_length）可能产生不同结果。min_phase_length=10 的选择未给出理由。论文引用 ThinKV 作为 tercile segmentation 的先例，但这只是 precedent，不是 justification。
- 建议：增加至少 2-3 种不同 segmentation 方案的 sensitivity analysis。

**W3** [warning] 多重比较校正不充分

- 具体位置：Section 4（"Bonferroni correction for 4 sparsity-level comparisons"）
- 问题：论文对 4 个 sparsity level 做了 Bonferroni 校正，但实际执行的假设检验远超 4 个：per-phase 比较（3 phases × 4 levels）、跨模型比较、crossover 检验、Gini/CV 分析等。如果考虑所有实际执行的检验，family-wise error rate 远高于名义水平。
- Holm correction（论文在 Section 4 提到 p_Holm < 0.005）比 Bonferroni 略好但仍不充分——它只校正了 4 个 level 内的比较，未覆盖跨条件的全部检验。
- 建议：报告所有执行的假设检验总数，并应用 FDR 校正（如 Benjamini-Hochberg）覆盖全部检验。

**W4** [warning] 论文正文仅 ~5 页，关键证据过度依赖 appendix

- 具体位置：全文结构
- 问题：作为 long paper（≤8 页正文），论文仅使用约 5 页正文，将 per-phase breakdown（Table 2）、effect size 细节（Table 5）、discrimination collapse 完整数据（Table 6）等关键支撑证据全部放入 appendix。按 ACL ARR 规则，"appendix 不参与正式审稿但可参考"——这意味着论文的核心 claims 在正文中缺乏充分的直接支撑。
- 建议：将 Table 2（per-phase II breakdown）和 Table 5（effect sizes with CIs）移入正文。论文有 3 页的 budget 可以利用。

**W5** [warning] Sparsity 范围窄且缺乏理论指导

- 具体位置：Section 4（s ∈ {0.15, 0.20, 0.25, 0.30}）
- 问题：4 个 sparsity level 间距均匀为 0.05，覆盖了一个较窄的范围。论文在 Appendix I 提到 s=0.35 时 high-phase II 开始上升（0.105），暗示存在质变点，但未正式探索。对于声称发现了 "monotonic severity gradient" 的论文，4 个点（其中 Qwen 只有 3 个显著）的 monotonic trend 说服力有限——4 个点的 Spearman ρ=1.0 的 p=0.042，仅仅勉强显著。
- 建议：增加至少 2-3 个 sparsity level（特别是 s > 0.30）以确认 monotonicity 和定位 saturation/transition point。

---

## 小问题（不影响接收）

- **引用格式**: h2o-neurips2023 在 .bib 文件中缺少 title 字段。7 条 orphan bib entries 未被引用（compression-ordering-2025, h2o-neurips2023, mustafar-neurips2025, obcache-2025, pagedeviction-eacl2026, pyramidkv-2024, raas-acl2025）。
- **脚注 2 硬件标注**: 论文提到 "4× NVIDIA RTX PRO 4000 Blackwell 96 GB"——请确认型号正确（RTX PRO 4000 vs 6000）。
- **Related Work（Section 2）排版**: 第一段从 "Compound compression" 话题跳到模型描述（"Qwen2.5-7B-Instruct (Yang et al., 2024), with standard inference training"），疑似排版/编辑错误，Related Work 段落混入了 Experimental Setup 的内容。
- **Eq. 2 符号**: G 的定义中 Π̃_high/Π̃_low 的下标含义不够直观——"high" 指 high-sparsity phase 还是 high-II phase？建议明确。
- **Table 2 某些 G 值缺失**: 标注为 "—" 但未解释原因。

---

## 主要优势

1. **研究问题有实际价值**: Compound sparsity 的 phase-dependent 行为对推理模型部署有直接意义——如果 severity 真的跨 phase 变化一个数量级，uniform budget 策略确实有问题。
2. **Random eviction 作为 control 的设计精巧**: 将 random eviction 作为 falsification control 来验证 severity gradient 是 strategy-specific（而非 compound sparsity 的固有属性），这是一个有说服力的实验设计。7/8 random 条件不显著，有效排除了 trivial 解释。
3. **统计方法选择合理（在方法论层面）**: 使用 nonparametric bootstrap + paired design + median-based statistics 来处理重度右偏分布，方法论本身是正确的。问题在于样本量不足以发挥这些方法的优势。
4. **Appendix B 的 multiplicative null 验证**: 主动检验了 additive vs multiplicative null 的 robustness，体现了方法论意识。
5. **Strategy crossover（Section 5.3）**: importance-based eviction 在不同 phase 同时优于和劣于 random 这一发现，如果可靠的话，对实际 compression strategy 选择有直接指导意义。

---

## Questions for Authors

1. 为什么只用 50 题而非全部 MATH-500？如果是计算资源限制，请说明；如果不是，请补全实验。
2. G 的 bootstrap CI 是多少？特别是 s=0.15 时分母 II_high≈0.006 的 CI。如果 CI 包含零或 ∞，如何解释 "69×" 这个数字？
3. 是否尝试过在 Gini coefficient 上做 controlled intervention（如人为保持 Gini 不变但仍做 head pruning）来验证因果关系？
4. Qwen 在 s=0.15 效应不显著（d_z=0.28），为什么 abstract 写 "replicates at s≥0.20" 时不同时指出 s=0.15 失败？
5. 论文声称 "phase-aware compression budgets" 是实际 implication，但未提供任何具体的 phase-aware 算法或 proof-of-concept。是否计划在 camera-ready 中加入？

---

*审查依据：ACL Rolling Review 官方 review form（aclrollingreview.org/reviewform），EMNLP 2026 Main Conference submission guidelines。*

---

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)

---

## 总体评分

**Overall**: 2.5/5 — 介于 Findings 接收和 Resubmit 之间
**一句话总结**: 论文发现了一个有趣的经验现象（compound sparsity severity 的 phase 依赖性），统计方法扎实，但贡献增量性偏强、无方法提出、评估规模过小，作为 EMNLP 主会论文分量不足。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 统计方法（permutation test, bootstrap CI, Bonferroni 校正）规范，但样本量极小（50 problems, 单一架构），discrimination collapse 仅为相关性证据 |
| Excitement | 2.5/5 | 现象本身有趣（phase-strategy crossover），但缺乏方法论贡献，且"severity gradient"的巨大倍数（69×-274×）主要由分母极小驱动 |
| Overall | 2.5/5 | 观察性发现+诊断工具，距离 EMNLP 主会的方法论或系统性贡献门槛尚有差距 |
| Reproducibility | 3/5 | 实验设置描述清晰，但无代码释放，50 个问题的 stratified sampling 种子未明确指定是否公开 |
| Reviewer Confidence | 4/5 | 熟悉 KV cache compression 和 LLM pruning 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 新颖性不足：核心贡献是观察性发现而非方法

- 具体位置：Section 1 贡献列表（3 条贡献均为"identify"/"show"/"propose mechanism"）
- 问题：三条贡献均为经验观察或事后解释，没有提出任何可操作的方法（phase-aware compression controller / dynamic budget allocation）。Discussion (Section 6) 提到"phase-aware compression budget"但仅停留在概念层面（"could mitigate"），未实现、未验证。对于 EMNLP 主会 long paper，纯观察性工作的门槛更高——需要更大规模、更多模型、或更深的理论分析来弥补方法空缺。
- 为什么影响接收：ACL ARR excitement 评分明确要求"novel and useful methodology"或"insightful empirical results"。在仅有 2 个同架构模型、50 道题的规模下，单纯的经验观察难以满足"insightful"标准。
- 建议修改方向：(a) 实现并验证 phase-aware compression budget（哪怕是 oracle/static 版本），展示实际 accuracy 提升；或 (b) 大幅扩大评估规模（多架构、多任务、更大模型），使观察性发现的可信度足以独立成篇。

**N2** [critical] Severity gradient 的 69×-274× 倍数具有误导性

- 具体位置：Abstract ("over an order of magnitude"), Section 5.2, Figure 1
- 问题：G = Ĩ_low / Ĩ_high，其中 Ĩ_high 极小（0.006-0.053，见 Appendix Table D）。当分母接近零时，比值可以任意大——这不反映实际严重程度。实际的绝对差值 Δ = 0.39-14.59（Table 1）更有信息量但远没那么戏剧性。Abstract 用"varies by over an order of magnitude"作为开头论点，过度依赖这个受分母影响的比值指标。
- 为什么影响接收：如果核心叙事建立在一个因分母极小而膨胀的指标上，审稿人和读者会质疑发现的实际意义。
- 建议修改方向：(a) 在正文中主要报告绝对差值 Δ 和 effect size d_z，将 G 降级为辅助指标；(b) 明确讨论 G 的分母敏感性问题；(c) 将 Figure 1 改为展示 Δ 或 d_z 的增长趋势。

**N3** [critical] 评估规模严重不足

- 具体位置：Section 4（50 MATH-500 problems, 2 models, 单一 Qwen2 架构）
- 问题：
  - **50 道题**：MATH-500 有 500 道题，只用 10% 缺乏理由（"stratified sampling" 但未论证 50 为何足够）。Qwen 进一步排除 4 道（n=46）。
  - **单一架构**：两个模型共享 Qwen2ForCausalLM 架构（28 layers, 28 heads, 4-group GQA），这不是跨模型验证——是同一架构不同训练配置的验证。LLaMA 3、Mistral 或非 GQA 架构（如 MHA）未测试。
  - **单一任务**：仅 MATH-500。代码推理、常识推理、多步 QA 等任务的 phase 结构可能完全不同。
- 为什么影响接收：Limitations 诚实承认了这些局限，但 Abstract 和 Introduction 的 claim 表述过于一般化（"reasoning models" 而非 "Qwen2-7B models on 50 math problems"）。
- 建议修改方向：至少覆盖一个非 Qwen 架构（LLaMA 3.3-8B 或 Mistral-7B）和一个非数学任务（如 GPQA 或 LiveCodeBench）。或者显著弱化 claim 的 generality。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Discrimination collapse 是相关性而非因果性证据

- 具体位置：Section 5.6, Appendix H
- 问题：Gini coefficient 下降（−0.030 到 −0.081）与 severity gradient 共现，但论文未排除其他混淆因素。更关键的是，entropy redistribution 组件仅在 DeepSeek 上一致，Qwen 在 s=0.25 出现符号反转（ΔH = +0.045），论文将其归因为"model-specific"但这削弱了机制的普遍性。Section 5.6 称 discrimination collapse 为"mechanistic explanation"，但它更接近于一个 correlational observation。
- 建议：(a) 将"mechanism"改为"hypothesis"或"correlational evidence"；(b) 考虑设计消融实验（如人工控制 Gini 分布的 importance scores 来验证因果关系）。

**W2** [warning] Interaction Index 与已有 super-additivity 概念的区分不清

- 具体位置：Section 3, Eq. 1
- 问题：II = r_b - r_a - r_k + 1 本质上是标准的交互效应（类似 ANOVA 中的 interaction term）。论文引用 SparK (Liao et al., 2026) 的 super-additive degradation 但未清楚区分 II 与 SparK 等工作中已有的 compound interaction 度量。如果 II 只是将 phase 维度加到已有概念上，应明确说明。
- 建议：增加一段明确讨论 II 与 SparK、SLiM、UniComp 中使用的 compound interaction 度量的关系和区别。

**W3** [warning] 正文仅 ~5 页，严重未利用 8 页限制

- 具体位置：全文结构
- 问题：正文约 5 页（Introduction 1.5p + Related Work 0.7p + Background 0.5p + Setup 0.5p + Results 1.2p + Discussion 0.5p + Conclusion 0.3p），远低于 long paper 8 页上限。大量关键信息被放在附录中：
  - 完整的 per-phase breakdown table（Appendix D）应在正文
  - Cross-model comparison table（Appendix F, Table 3）应在正文
  - Effect size table（Appendix G, Table 5）应在正文
  - Discrimination collapse metrics（Appendix H）至少 summary 应在正文
  
  这使正文感觉像是 extended abstract + 附录堆积，而非一篇完整论文。
- 建议：将 Appendix D (Table 2), F (Table 3), G (Table 5) 移入正文，充分利用 8 页空间。将 Discussion 扩展以覆盖更多 deployment implications。

**W4** [warning] Abstract 信息过载，可读性差

- 具体位置：Abstract
- 问题：Abstract 塞入了过多具体数字（69×, 274×, 0.39, 14.59, 0.44, 0.80, 7/8, 0.032, 0.818, 7.106, 1.363, d=-1.00, ρ=1.0, p=0.041...），读者在第一遍阅读时无法消化这些数据。一个好的 abstract 应传达 high-level insight + 关键定量 takeaway（1-2 个数字），而非完整的统计报告。
- 建议：精简 Abstract 至 150-200 words，保留核心发现 + 1-2 个最有 impact 的定量结果。

**W5** [warning] Phase segmentation 方法选择缺乏敏感性分析

- 具体位置：Section 3 ("tercile boundaries of per-position attention entropy")
- 问题：Phase 定义完全依赖 attention entropy 的三分位数划分，且沿用 ThinKV 的方法。但：(a) 为什么是 tercile 而非 quartile/quintile？(b) min_phase_length=10 的选择依据是什么？(c) 换用其他 phase segmentation（如 ThinKV 的 thought-type decomposition: reasoning/execution/transition）结果是否一致？这些选择对 severity gradient 的 magnitude 影响可能很大。
- 建议：至少对 phase 数量和 min_phase_length 做 robustness check。

---

## 小问题（不影响接收）

- **引用问题**：bib 中有 7 个 orphan 条目（在 .bib 中但未被正文引用）：`compression-ordering-2025`, `h2o-neurips2023`, `mustafar-neurips2025`, `obcache-2025`, `pagedeviction-eacl2026`, `pyramidkv-2024`, `raas-acl2025`。其中 H2O、PyramidKV、RaaS 等是高度相关工作，要么引用要么删除。`h2o-neurips2023` 的 title 字段为空。
- **符号不一致**：正文混用 d_s 和 d_z 指代 Cohen's d 的变体，未明确区分。Abstract 用 d（无下标），Section 5.5 用 d_s，Appendix 用 d_z。
- **Table 1 数值与 Appendix Table D 不完全对应**：Table 1 的 Random s=0.25 Δ=0.54，但 Appendix D 显示 Ĩ_low=1.363 - Ĩ_high=0.818 = 0.545，取整差异虽小但应统一精度。
- **脚注 2**：提到"4× NVIDIA RTX PRO 6000 Blackwell 96 GB GPUs"，但实验仅在单个 7B 模型上运行 50 道题，使用 4 块 96GB GPU 似乎 over-provisioned，且未说明是否利用多卡。

---

## 遗漏的重要相关工作（Missing References）

以下通过 web_search 验证的相关工作在论文中未被讨论：

1. **R-KV** (Cai et al., NeurIPS 2025): "Redundancy-aware KV Cache Compression for Reasoning Models"。专门针对 reasoning model 的 KV cache 压缩，识别冗余 token 实现 10% KV cache 保留近乎无损性能。与本文直接相关——R-KV 也识别了 reasoning 生成中不同 token 的重要性差异，但采取了方法导向的路线。**必须讨论。**

2. **RLKV / "Which Heads Matter for Reasoning?"** (Du et al., 2025/2026): 用 RL 识别 reasoning-critical heads 并差异化压缩。直接涉及 head pruning 与 reasoning 质量的交互——论文的核心议题。RLKV 的 "functional heterogeneity" 假设与 discrimination collapse 高度相关。**必须讨论。**

3. **"Hold Onto That Thought"** (Liu et al., NeurIPS 2025): 系统评估 KV cache 压缩对 reasoning 的影响，发现 token-dropping 方法会破坏 reasoning integrity。与本文的 random vs. importance-based eviction 对比直接相关。**应当讨论。**

4. **RAC / "Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction"** (NeurIPS 2025): 50% sparsity 下保留 95% reasoning 能力，关键创新是用 on-policy CoT traces 重建而非仅输入重建。与本文的 pruning + reasoning 主题直接相关。**应当讨论。**

5. **EVICPRESS** (Fang et al., 2025): Joint KV-Cache compression and eviction，优化跨存储层的 eviction 和 compression 决策。属于 compound compression 的方法性工作。**可选讨论。**

6. **LongFlow** (2026, ICLR withdrawn): KV cache compression for reasoning models with throughput measurement (11.8× throughput, 80% compression)。本文缺少 throughput evaluation，LongFlow 展示了这类评估的可行性。**可选讨论。**

7. **"Not All Heads Matter"** (Microsoft, 2024): Head-level KV cache compression with integrated retrieval and reasoning。与 head-level importance heterogeneity 相关。**可选讨论。**

特别指出：论文 bib 中已有 `raas-acl2025` (RaaS) 但正文未引用，这是 reasoning-aware attention sparsity 的直接相关工作，遗漏不可接受。

---

## 主要优势

1. **统计方法严谨**：permutation test + Bonferroni correction + bootstrap CI + effect size reporting 的组合在 ML 论文中罕见，值得肯定（Section 5.5, Appendix C/G）。
2. **Random eviction 作为 falsification control 设计精巧**：用 random eviction 作为 null strategy 来隔离"phase gradient 是 strategy-specific 还是 compound sparsity inherent"的设计简洁有力（Table 1, Section 5.1）。
3. **Multiplicative null 验证**（Appendix B）：检验 additive vs. multiplicative null 不影响结论，增强稳健性。
4. **Limitations section 诚实全面**：对样本量、架构限制、因果性限制等的讨论坦诚，这在很多论文中做不到。

---

## Questions for Authors

1. 如果将评估扩大到全部 500 道 MATH-500 题，severity gradient 的 magnitude 和 statistical significance 是否保持？50 vs. 500 的结果对比是验证当前发现稳健性的最低成本实验。
2. Phase-aware compression budget 的 oracle 版本（已知每个 phase 的最优 sparsity level）相对于 uniform budget 能提升多少 accuracy？如果只需要简单地对 high/low phase 用不同 s，实现成本极低——为什么不做？
3. 为什么选择 Frobenius norm 而非 gradient-based importance 来决定 head pruning？论文在 Extended Discussion 中提到"attention-independent metrics should produce flatter severity gradients"——这是一个 testable prediction，为什么不在本文中验证？
4. Discrimination collapse 的 Gini 下降幅度（0.010-0.081）在绝对值上很小。是否计算了 Gini 下降与 severity gradient 之间的相关系数？如果相关性不强，机制解释的说服力会大打折扣。

---

**总结判断**：论文发现了一个有趣的经验现象，统计分析做得规范，但（1）纯观察性贡献缺乏方法论增量，（2）评估规模过小（2 个同架构模型 × 50 题），（3）核心指标 G 受分母影响存在误导性，（4）遗漏多篇 2025-2026 高度相关工作。建议 **Resubmit next cycle**，补充方法性贡献（至少 oracle phase-aware budget 验证）和扩大评估规模后再投。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-14T13:17:06.156720+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"Severity gradient G 的近零分母使 69×-274× 倍数不可靠\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N2 + R2-N2 共识：G = Π̃_low/Π̃_high 分母极小(0.006-0.053)，比值对噪声极敏感。需报告 bootstrap CI，降低 G 的 headline 地位，改用 Δ 或 d_z 作主要指标。\"\n    action_items:\n      - round: 1\n        action: \"报告 G 的 bootstrap CI；将 G 降为辅助指标，正文主要报告 Δ 和 d_z\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"样本量严重不足（n=50, 实际 49/46），统计功效存疑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N3 共识：50 题仅占 MATH-500 的 10%，bootstrap CI 跨一个数量级（s=0.30 CI=[0.70,16.29]），Qwen s=0.15 不显著。需扩大到全部 500 题或做 split-half stability analysis。\"\n    action_items:\n      - round: 1\n        action: \"使用全部 MATH-500 500 题；报告 post-hoc power analysis；至少做 multiple generation seeds 验证\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"同架构跨模型复现严重高估泛化性\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N3 + R2-N3 共识：DeepSeek 和 Qwen 共享 Qwen2ForCausalLM 架构，per-problem concordance 不显著(ρ=-0.11)。'cross-model replication' 措辞误导，需增加非 Qwen 架构或弱化 claim。\"\n    action_items:\n      - round: 1\n        action: \"增加至少一个非 Qwen 架构（LLaMA 3 或 Mistral）；或将 'cross-model' 改为 'cross-training-regime'\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"Discrimination collapse 仅相关性证据，被呈现为因果机制\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N4 + R2-W1 共识：Gini 下降与 severity gradient 共现但未排除混淆因素，entropy redistribution 在 Qwen s=0.25 反转。需改 'mechanism' 为 'hypothesis' 或做 causal intervention。\"\n    action_items:\n      - round: 1\n        action: \"降低 claim 强度（mechanism → hypothesis/correlational evidence）；或设计 intervention 实验验证因果性\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"贡献深度不足——纯观察无方法提出\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2-N1：三条贡献均为经验观察，phase-aware controller 仅停留概念层面。R1 对此持 moderate concern（Excitement 3/5）。对 EMNLP main conference long paper 偏薄。\"\n    action_items:\n      - round: 1\n        action: \"实现并验证 phase-aware compression budget（至少 oracle 版本）；或大幅扩大评估规模使观察性发现可独立成篇\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N5\"\n    summary: \"数值不一致：Abstract/正文/表格/附录存在多处矛盾\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Initial R1-N1：Δ=14.59 vs 11.59，n=50 vs n=49，ΔH range 不一致，Cohen's d 0.41 vs 0.44。多处数值矛盾损害可信度。\"\n    action_items:\n      - round: 1\n        action: \"逐一核对所有数值，确保 abstract/正文/表格/附录完全一致\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N6\"\n    summary: \"Cross-model Spearman ρ=1.0 (n=4) 统计功效极低\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Initial R1-N2：n=4 的 ρ=1.0 → p≈0.042，未做 Bonferroni 修正后不再显著。不足以支撑 'perfect ordinal agreement' 的泛化声明。\"\n    action_items:\n      - round: 1\n        action: \"承认 n=4 rank correlation 功效不足；强调各模型独立 d_z 递增轨迹；降低泛化声明力度\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"Limitations 节格式违反 ARR 要求（desk reject 风险）\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Initial R2-N1 + R1-W7：当前为 §7.1 编号子节，ARR 要求独立无编号节于 Conclusion 后、References 前。\"\n    action_items:\n      - round: 1\n        action: \"将 Limitations 改为独立无编号节，置于 Conclusion 之后、References 之前\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"相关工作遗漏严重（R-KV, Lethe, RLKV, Hold Onto That Thought 等）\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 两轮均指出极高优先级遗漏：R-KV(NeurIPS 2025), Lethe(AAAI 2026), RLKV, Hold Onto That Thought(NeurIPS 2025), RAC(NeurIPS 2025)。RaaS 已在 bib 但未引用。\"\n    action_items:\n      - round: 1\n        action: \"补充所有极高/高优先级相关工作的讨论，特别是 R-KV、Lethe、RLKV\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation 缺乏 sensitivity analysis\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W2 + R2-W5：tercile 切分未做 robustness check，min_phase_length=10 无理由。需至少 2-3 种 segmentation 方案对比。\"\n    action_items:\n      - round: 1\n        action: \"增加 quartile/quintile 等替代 segmentation 的 sensitivity analysis\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"正文仅 ~5 页，关键表格应移入正文\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W4 + R2-W3：Table 2(per-phase), Table 3(cross-model), Table 5(effect sizes) 等应移入正文，充分利用 8 页空间。\"\n    action_items:\n      - round: 1\n        action: \"将 Appendix D/F/G 的关键表格移入正文\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"缺少 task accuracy 评估（仅 PPL）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W6(initial) + R2 Q1：仅用 PPL 作质量指标，PPL 恶化不等于答案错误。需报告 MATH-500 solve rate。\"\n    action_items:\n      - round: 1\n        action: \"报告各条件下 MATH-500 accuracy（solve rate）\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 过长/信息过载（~600 词，应精简至 150-250 词）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2-W4 + initial R2-W3：Abstract 塞入过多数字，可读性差。\"\n    action_items:\n      - round: 1\n        action: \"精简 Abstract 至 150-200 词，保留 1-2 个关键定量结果\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"多重比较校正不充分（仅 Bonferroni on 4 levels，未覆盖全部检验）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1-W3：实际检验数远超 4 个（per-phase × levels × 跨模型 × Gini 等），应报告总检验数并用 FDR 校正。\"\n    action_items:\n      - round: 1\n        action: \"报告所有假设检验总数，应用 Benjamini-Hochberg FDR 校正\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"Footnote 2 硬件信息可能泄露匿名性\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"RTX PRO 6000 Blackwell Server Edition 96GB 硬件信息过于具体，去匿名化风险。\"\n    action_items:\n      - round: 1\n        action: \"泛化硬件描述或移除具体型号\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Bibliography 管理混乱（7 orphan entries, h2o title 空, 年份不一致）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"7 条 orphan bib entries（含 H2O, PyramidKV, RaaS 等高相关工作），h2o-neurips2023 title 字段为空，部分年份与实际不符。\"\n    action_items:\n      - round: 1\n        action: \"清理 orphan entries（引用或删除），修正 title 和年份\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Sparsity 范围窄（仅 4 levels），monotonicity 证据不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1-W5：4 个 sparsity levels 不足以论证 monotonic growth，Appendix I 暗示 s=0.35 有质变但未正式探索。\"\n    action_items:\n      - round: 1\n        action: \"增加至少 2-3 个 sparsity levels（特别是 s>0.30）\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"II 与已有 super-additivity 概念区分不清\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2-W2：II 本质为标准交互效应，与 SparK 等已有 compound interaction 度量的区别未充分讨论。\"\n    action_items:\n      - round: 1\n        action: \"增加一段讨论 II 与 SparK/SLiM/UniComp 中 compound interaction 度量的区别\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"Appendix B 与 Appendix D 文本疑似重复\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Initial R2-W6：两个 appendix 文本几乎完全重复，疑为粘贴错误。\"\n    action_items:\n      - round: 1\n        action: \"检查并修正 Appendix 重复内容\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"Severity gradient G 的近零分母使 69×-274× 倍数不可靠\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N2 + R2-N2 共识：G = Π̃_low/Π̃_high 分母极小(0.006-0.053)，比值对噪声极敏感。需报告 bootstrap CI，降低 G 的 headline 地位，改用 Δ 或 d_z 作主要指标。\"\n    action_items:\n      - round: 1\n        action: \"报告 G 的 bootstrap CI；将 G 降为辅助指标，正文主要报告 Δ 和 d_z\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"样本量严重不足（n=50, 实际 49/46），统计功效存疑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N3 共识：50 题仅占 MATH-500 的 10%，bootstrap CI 跨一个数量级（s=0.30 CI=[0.70,16.29]），Qwen s=0.15 不显著。需扩大到全部 500 题或做 split-half stability analysis。\"\n    action_items:\n      - round: 1\n        action: \"使用全部 MATH-500 500 题；报告 post-hoc power analysis；至少做 multiple generation seeds 验证\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"同架构跨模型复现严重高估泛化性\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N3 + R2-N3 共识：DeepSeek 和 Qwen 共享 Qwen2ForCausalLM 架构，per-problem concordance 不显著(ρ=-0.11)。'cross-model replication' 措辞误导，需增加非 Qwen 架构或弱化 claim。\"\n    action_items:\n      - round: 1\n        action: \"增加至少一个非 Qwen 架构（LLaMA 3 或 Mistral）；或将 'cross-model' 改为 'cross-training-regime'\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"Discrimination collapse 仅相关性证据，被呈现为因果机制\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N4 + R2-W1 共识：Gini 下降与 severity gradient 共现但未排除混淆因素，entropy redistribution 在 Qwen s=0.25 反转。需改 'mechanism' 为 'hypothesis' 或做 causal intervention。\"\n    action_items:\n      - round: 1\n        action: \"降低 claim 强度（mechanism → hypothesis/correlational evidence）；或设计 intervention 实验验证因果性\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"贡献深度不足——纯观察无方法提出\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2-N1：三条贡献均为经验观察，phase-aware controller 仅停留概念层面。R1 对此持 moderate concern（Excitement 3/5）。对 EMNLP main conference long paper 偏薄。\"\n    action_items:\n      - round: 1\n        action: \"实现并验证 phase-aware compression budget（至少 oracle 版本）；或大幅扩大评估规模使观察性发现可独立成篇\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N5\"\n    summary: \"数值不一致：Abstract/正文/表格/附录存在多处矛盾\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Initial R1-N1：Δ=14.59 vs 11.59，n=50 vs n=49，ΔH range 不一致，Cohen's d 0.41 vs 0.44。多处数值矛盾损害可信度。\"\n    action_items:\n      - round: 1\n        action: \"逐一核对所有数值，确保 abstract/正文/表格/附录完全一致\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N6\"\n    summary: \"Cross-model Spearman ρ=1.0 (n=4) 统计功效极低\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Initial R1-N2：n=4 的 ρ=1.0 → p≈0.042，未做 Bonferroni 修正后不再显著。不足以支撑 'perfect ordinal agreement' 的泛化声明。\"\n    action_items:\n      - round: 1\n        action: \"承认 n=4 rank correlation 功效不足；强调各模型独立 d_z 递增轨迹；降低泛化声明力度\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"Limitations 节格式违反 ARR 要求（desk reject 风险）\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Initial R2-N1 + R1-W7：当前为 §7.1 编号子节，ARR 要求独立无编号节于 Conclusion 后、References 前。\"\n    action_items:\n      - round: 1\n        action: \"将 Limitations 改为独立无编号节，置于 Conclusion 之后、References 之前\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"相关工作遗漏严重（R-KV, Lethe, RLKV, Hold Onto That Thought 等）\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 两轮均指出极高优先级遗漏：R-KV(NeurIPS 2025), Lethe(AAAI 2026), RLKV, Hold Onto That Thought(NeurIPS 2025), RAC(NeurIPS 2025)。RaaS 已在 bib 但未引用。\"\n    action_items:\n      - round: 1\n        action: \"补充所有极高/高优先级相关工作的讨论，特别是 R-KV、Lethe、RLKV\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation 缺乏 sensitivity analysis\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W2 + R2-W5：tercile 切分未做 robustness check，min_phase_length=10 无理由。需至少 2-3 种 segmentation 方案对比。\"\n    action_items:\n      - round: 1\n        action: \"增加 quartile/quintile 等替代 segmentation 的 sensitivity analysis\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"正文仅 ~5 页，关键表格应移入正文\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W4 + R2-W3：Table 2(per-phase), Table 3(cross-model), Table 5(effect sizes) 等应移入正文，充分利用 8 页空间。\"\n    action_items:\n      - round: 1\n        action: \"将 Appendix D/F/G 的关键表格移入正文\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"缺少 task accuracy 评估（仅 PPL）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W6(initial) + R2 Q1：仅用 PPL 作质量指标，PPL 恶化不等于答案错误。需报告 MATH-500 solve rate。\"\n    action_items:\n      - round: 1\n        action: \"报告各条件下 MATH-500 accuracy（solve rate）\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 过长/信息过载（~600 词，应精简至 150-250 词）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2-W4 + initial R2-W3：Abstract 塞入过多数字，可读性差。\"\n    action_items:\n      - round: 1\n        action: \"精简 Abstract 至 150-200 词，保留 1-2 个关键定量结果\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"多重比较校正不充分（仅 Bonferroni on 4 levels，未覆盖全部检验）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1-W3：实际检验数远超 4 个（per-phase × levels × 跨模型 × Gini 等），应报告总检验数并用 FDR 校正。\"\n    action_items:\n      - round: 1\n        action: \"报告所有假设检验总数，应用 Benjamini-Hochberg FDR 校正\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"Footnote 2 硬件信息可能泄露匿名性\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"RTX PRO 6000 Blackwell Server Edition 96GB 硬件信息过于具体，去匿名化风险。\"\n    action_items:\n      - round: 1\n        action: \"泛化硬件描述或移除具体型号\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Bibliography 管理混乱（7 orphan entries, h2o title 空, 年份不一致）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"7 条 orphan bib entries（含 H2O, PyramidKV, RaaS 等高相关工作），h2o-neurips2023 title 字段为空，部分年份与实际不符。\"\n    action_items:\n      - round: 1\n        action: \"清理 orphan entries（引用或删除），修正 title 和年份\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Sparsity 范围窄（仅 4 levels），monotonicity 证据不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"R1-W5：4 个 sparsity levels 不足以论证 monotonic growth，Appendix I 暗示 s=0.35 有质变但未正式探索。\"\n    action_items:\n      - round: 1\n        action: \"增加至少 2-3 个 sparsity levels（特别是 s>0.30）\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"II 与已有 super-additivity 概念区分不清\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2-W2：II 本质为标准交互效应，与 SparK 等已有 compound interaction 度量的区别未充分讨论。\"\n    action_items:\n      - round: 1\n        action: \"增加一段讨论 II 与 SparK/SLiM/UniComp 中 compound interaction 度量的区别\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"Appendix B 与 Appendix D 文本疑似重复\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Initial R2-W6：两个 appendix 文本几乎完全重复，疑为粘贴错误。\"\n    action_items:\n      - round: 1\n        action: \"检查并修正 Appendix 重复内容\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-14T13:17:06.258469+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml\", \"bytes\": 10330}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-14T13:19:11.715776+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Phase-Modulated Compound Sparsity\n**项目**: phase-gated-compound-sparse\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**审稿轮次**: Round 1\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验评估, R2: 新颖性+相关工作+写作+格式）\n**外部审稿**: 未配置\n\n---\n\n## Summary\n\n本文研究 compound sparsity（head pruning + KV cache eviction）在推理模型不同推理阶段的严重程度差异。在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上对 MATH-500 的 50 道题实验，发现 importance-based eviction 的 severity 在 low-sparsity phase 显著高于 high-sparsity phase（作者称 69×-274× severity gradient），而 random eviction 不显示此梯度。提出 entropy-discrimination collapse 作为机制假说。\n\n---\n\n## Strengths\n\n1. **Random eviction 作为 falsification control 设计精巧**：7/8 random 条件不显著，有效排除了 trivial 解释，证明 severity gradient 是 strategy-specific 而非 compound sparsity 固有属性 [R1, R2 共识]\n2. **统计方法严谨**：nonparametric bootstrap + paired permutation test + Bonferroni correction + effect sizes with CI 的组合在 ML 论文中罕见 [R1, R2 共识]\n3. **Phase-strategy crossover 有实际意义**：importance-based eviction 在不同 phase 优劣反转，对实际 compression 策略选择有指导价值 [R1, R2 共识]\n4. **Multiplicative null verification**：主动检验 additive vs multiplicative null 的 robustness [R1]\n5. **Limitations 诚实全面**：对样本量、架构限制、因果性限制等的讨论坦诚 [R2]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Critical Issues（两位 Reviewer 共识）\n\n**C1. Severity gradient G 的 69×-274× 倍数具有误导性** [R1-N2, R2-N2]\n- G = Π̃_low / Π̃_high，分母 Π̃_high 极小（0.006-0.053），比值对噪声极度敏感\n- 论文核心叙事（标题、Abstract、Conclusion）围绕 \"order of magnitude\" 展开，但这个数字本质是近零分母的放大效应\n- 绝对差异 Δ（0.39-14.59）更稳健但远不如 G 震撼\n- **要求**：报告 G 的 bootstrap CI；将 G 降为辅助指标，改用 Δ 和 d_z 作为主要效应量\n\n**C2. 样本量严重不足** [R1-N1, R2-N3]\n- n=50（实际 49/46），仅占 MATH-500 的 10%\n- Bootstrap CI 极宽（s=0.30 时 CI=[0.70, 16.29]，跨一个数量级）\n- Qwen s=0.15 效应不显著（d_z=0.28, CI 含零），但 Abstract 写 \"replicates at s≥0.20\" 给读者全面复现印象\n- 未报告问题选择的 random seed\n- **要求**：使用全部 500 题；报告 post-hoc power analysis；至少做 split-half stability analysis\n\n**C3. 同架构 \"跨模型复现\" 严重高估泛化性** [R1-N3, R2-N3]\n- DeepSeek 和 Qwen 共享 Qwen2ForCausalLM 架构（28 layers, 28 heads, 4-group GQA）\n- \"Cross-model replication\"（§5.4 标题）措辞误导——实际验证同架构不同训练配置\n- Per-problem concordance 不显著（mean ρ = −0.11）\n- Qwen 效应量仅为 DeepSeek 的 ~1/5，更接近 marginal replication\n- **要求**：增加至少一个非 Qwen 架构；或将 \"cross-model\" 改为 \"cross-training-regime\" 并弱化泛化声明\n\n**C4. Discrimination collapse 仅相关性证据** [R1-N4, R2-W1]\n- Gini 下降与 severity gradient 共现，但未排除混淆因素\n- Entropy redistribution 在 Qwen s=0.25 出现符号反转，削弱机制普遍性\n- 论文称 \"mechanistic explanation\" 但证据仅为 correlational\n- **要求**：改 \"mechanism\" 为 \"hypothesis\"/\"correlational evidence\"；或设计 causal intervention\n\n**C5. 贡献深度不足——纯观察无方法** [R2-N1; R1 moderate concern]\n- 三条贡献均为经验观察（identify/show/propose mechanism），无可操作方法\n- Phase-aware controller 仅停留概念层面\n- R2 视为 critical（Excitement 2.5/5），R1 视为 moderate concern（Excitement 3/5）\n- **要求**：实现 phase-aware compression budget（至少 oracle 版本）；或大幅扩大评估规模\n\n**C6. 数值不一致** [R1 initial N1]\n- Abstract/Table 1: Δ=14.59 vs §5.1: Δ=11.59\n- 主文 n=50 vs Appendix E n=49（1 excluded）\n- §6.2 ΔH ∈ [−0.080, −0.047] vs Table 7 ΔH ∈ [−0.047, −0.040]\n- Cohen's d: Abstract 0.41 vs 正文 0.44\n- **要求**：全面核对，确保所有数值一致\n\n**C7. Spearman ρ=1.0 (n=4) 统计无效** [R1 initial N2]\n- p=1/24≈0.042，未做 Bonferroni 修正后不再显著\n- 论文据此在 §7 声称 \"perfect ordinal agreement\" 作为泛化主要论据\n- **要求**：承认功效不足；降低泛化声明力度\n\n**C8. Limitations 节格式违反 ARR 要求** [R2 initial N1, R1 W7]\n- 当前为 §7.1 编号子节\n- ARR 要求独立无编号节于 Conclusion 后、References 前\n- **Desk reject 风险**\n- **要求**：立即修正格式\n\n**C9. 相关工作遗漏严重** [R2 initial N2, R2 updated]\n- 极高优先级：R-KV (NeurIPS 2025), Lethe (AAAI 2026), RLKV, \"Hold Onto That Thought\" (NeurIPS 2025)\n- 高优先级：RAC (NeurIPS 2025), RaaS (已在 bib 未引用), Scissorhands, FastGen, StreamingLLM\n- **要求**：补充所有极高/高优先级工作的讨论\n\n### Should-Fix Issues\n\n**S1.** Phase segmentation 缺乏 sensitivity analysis（tercile 切分未做 robustness check）[R1, R2]\n**S2.** 正文仅 ~5 页，关键表格（Table 2/3/5）应移入正文，充分利用 8 页空间 [R1, R2]\n**S3.** Abstract ~600 词，信息过载，应精简至 150-200 词 [R2]\n**S4.** 多重比较校正不充分（实际检验数远超 4，应用 FDR 校正）[R1]\n**S5.** Sparsity 范围窄（仅 4 levels），monotonicity 证据不足 [R1]\n**S6.** 仅 PPL 无 task accuracy 评估 [R1, R2]\n**S7.** II 与已有 super-additivity 概念区分不清 [R2]\n**S8.** Footnote 2 硬件信息泄露匿名性风险 [R1, R2]\n**S9.** Bibliography 管理问题（7 orphan entries, h2o title 空, 年份不一致）[R1, R2]\n**S10.** Appendix B 与 D 文本疑似重复 [R2]\n**S11.** Interaction Index 的 additive null 假设与核心论点（轴间交互）内在矛盾 [R1]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致 [AGREE]：\n1. G 指标近零分母 → 69×-274× 不可靠，需 CI + 降级\n2. n=50 不足 → 需扩至全部 MATH-500\n3. 同架构 ≠ 跨模型泛化 → 需非 Qwen 架构验证\n4. Discrimination collapse 是相关性非因果 → 降低 claim 或做 intervention\n5. 正文过短，关键表格应移入正文\n6. Phase segmentation 需 sensitivity analysis\n7. 相关工作遗漏严重（R-KV, Lethe, RLKV 等）\n\n## Reviewer Divergence\n\n**D1. 贡献深度 / Excitement**：\n- R2：critical，Excitement 2.5/5——EMNLP main conference 需要方法贡献，纯观察不够\n- R1：moderate concern，Excitement 3/5——观察性发现有价值但需更大规模支撑\n- 两者均认为当前不达 main conference 标准，分歧在严重程度\n\n**D2. Interaction Index 方法论**：\n- R1：additive null 假设（轴间独立）与论文核心论点（轴间交互）矛盾，建议增加 cross-entropy 空间分析\n- R2：关注 II 与已有 super-additivity 概念的区分\n- 视角不同但不冲突\n\n---\n\n## Questions for Authors\n\n1. 为什么不使用全部 500 道 MATH-500 题？如为计算资源限制请说明。\n2. G 的 bootstrap 95% CI？特别是 s=0.15 分母 II_high≈0.006 时。\n3. 各条件下 MATH-500 solve rate（accuracy）？PPL 恶化是否对应答案错误？\n4. 是否尝试过非 Qwen 架构（LLaMA 3, Mistral）？\n5. Phase-aware compression budget 的 oracle 版本相比 uniform budget 能提升多少 accuracy？\n6. Discrimination collapse 的 Gini 下降与 severity gradient 之间的 correlation coefficient？\n7. §5.1 \"11.59\" vs Table 1 \"14.59\" 哪个正确？Cohen's d 0.41 vs 0.44？\n8. 是否做过 split-half stability analysis 或 multiple generation seeds？\n9. 用 token position 等分或 think 标记做 phase segmentation 结果如何？\n10. 为什么选 Frobenius norm 而非 gradient-based importance 做 head pruning？论文提到 \"attention-independent metrics should produce flatter severity gradients\" 为何不验证？\n\n---\n\n## Missing References（合并去重）\n\n| 优先级 | 论文 | Venue | 理由 |\n|--------|------|-------|------|\n| 极高 | R-KV (Cai et al.) | NeurIPS 2025 | Reasoning model KV compression，直接相关 |\n| 极高 | Lethe (Zeng et al.) | AAAI 2026 | Phase-aware KV pruning，直接竞争 |\n| 极高 | RLKV / \"Which Heads Matter\" (Du et al.) | 2025/2026 | Head importance for reasoning，与 discrimination collapse 相关 |\n| 极高 | \"Hold Onto That Thought\" (Liu et al.) | NeurIPS 2025 | 系统评估 KV compression 对 reasoning 影响 |\n| 高 | RAC | NeurIPS 2025 | Reasoning model pruning via CoT reconstruction |\n| 高 | RaaS (Hu et al.) | ACL 2025 | 已在 bib 但未引用，reasoning-aware attention sparsity |\n| 高 | Scissorhands (Liu et al.) | NeurIPS 2023 | KV eviction 基础方法 |\n| 高 | FastGen (Ge et al.) | ICLR 2024 | Per-head adaptive KV cache |\n| 高 | StreamingLLM (Xiao et al.) | ICLR 2024 | Attention sink 基础 |\n| 高 | Titanus (Chen et al.) | GLSVLSI 2025 | KV pruning+quantization 复合效果 |\n| 中 | EVICPRESS (Fang et al.) | 2025 | Joint KV compression + eviction |\n| 中 | SparseGPT | ICML 2023 | 权重稀疏化基础 |\n| 中 | Wanda | ICLR 2024 | 轻量 pruning |\n| 中 | MInference | NeurIPS 2024 | 注意力稀疏模式分析 |\n| 中 | Cohen (1988) | — | Statistical Power Analysis（effect size 解读依据） |\n| 中 | LLM-Pruner (Ma et al.) | NeurIPS 2023 | Coupled pruning 开创性工作 |\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (2.5/5)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立评估后均给出 2.5/5（R1 从初始 3/5 在交叉分享后下调至 2.5/5，R2 维持 2.5/5）。\n\n**核心判断**：论文发现了一个有价值的经验现象（compound sparsity severity 的 phase 依赖性），实验设计有亮点（random eviction control），统计方法论严谨。但存在 9 个 critical 问题：\n1. 核心指标 G 受近零分母膨胀，headline 数字不可靠\n2. 样本量仅 50 题，统计功效不足\n3. 同架构\"跨模型\"验证高估泛化性\n4. 纯观察性贡献无方法提出\n5. Discrimination collapse 仅相关性证据\n6. 多处数值不一致\n7. Spearman ρ=1.0 (n=4) 统计无效\n8. Limitations 节格式违反 ARR 要求（desk reject 风险）\n9. 相关工作遗漏严重\n\n**建议路径**：\n- **立即修复（deadline 前可完成）**：C6(数值一致性), C7(弱化 ρ claim), C8(Limitations 格式), C9(补充引用), S2-S3(正文扩展), S8-S10(格式清理)\n- **需实验补充（可能需延期）**：C1(G 的 CI), C2(扩至 500 题), C3(增加非 Qwen 模型), C5(oracle phase-aware budget), S1(segmentation sensitivity), S5(更多 sparsity levels), S6(accuracy 指标)\n- **需重新定位**：C4(降低因果 claim), C5(如不加方法则转 Findings)\n\n当前状态不适合 EMNLP 2026 main conference。解决 C1-C3、C6-C9 + S1-S6 后可达 **Findings** 接收水平。如额外解决 C4-C5（加方法贡献 + 跨架构验证），可重投 main conference。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过长（~600 词），需精简至 150-200 词\n- 多处数值需核对（Δ=14.59 vs 11.59, d=0.41 vs 0.44）\n- \"over an order of magnitude\" 依赖不可靠的 G 指标\n\n### §1 Introduction\n- 贡献列表三条均为观察性，缺乏方法贡献\n- \"replicates across models\" 措辞需弱化\n\n### §2 Related Work\n- 遗漏 R-KV, Lethe, RLKV, Hold Onto That Thought 等 10+ 篇高相关工作\n- 第一段疑似混入 Experimental Setup 内容\n\n### §3 Background & Methods\n- G 定义的 ε 阈值未说明\n- II 与已有 super-additivity 概念区分不清\n- Additive null 假设与核心论点存在内在矛盾\n\n### §4 Experimental Setup\n- n=50 不足，选题标准不透明\n- 仅 2 模型同架构，4 sparsity levels\n- 仅 PPL 无 accuracy\n\n### §5 Results\n- §5.1: \"11.59\" vs Table 1 \"14.59\" 不一致\n- §5.2: G 的近零分母问题\n- §5.4: ρ=1.0 (n=4) 统计功效不足\n- §5.6: Discrimination collapse 仅相关性\n\n### §6 Discussion\n- Phase-aware controller 仅概念层面\n- ΔH range 与 Table 7 不一致\n\n### §7 Conclusion & Limitations\n- Limitations 格式违反 ARR（§7.1 编号子节 → 应为独立无编号节）\n\n### References & Appendix\n- 7 orphan bib entries\n- h2o-neurips2023 title 空\n- Appendix B 与 D 文本重复\n- Footnote 2 硬件信息泄露匿名性",
  "project": "phase-gated-compound-sparse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Phase-Modulated Compound Sparsity\n**项目**: phase-gated-compound-sparse\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**审稿轮次**: Round 1\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验评估, R2: 新颖性+相关工作+写作+格式）\n**外部审稿**: 未配置\n\n---\n\n## Summary\n\n本文研究 compound sparsity（head pruning + KV cache eviction）在推理模型不同推理阶段的严重程度差异。在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上对 MATH-500 的 50 道题实验，发现 importance-based eviction 的 severity 在 low-sparsity phase 显著高于 high-sparsity phase（作者称 69×-274× severity gradient），而 random eviction 不显示此梯度。提出 entropy-discrimination collapse 作为机制假说。\n\n---\n\n## Strengths\n\n1. **Random eviction 作为 falsification control 设计精巧**：7/8 random 条件不显著，有效排除了 trivial 解释，证明 severity gradient 是 strategy-specific 而非 compound sparsity 固有属性 [R1, R2 共识]\n2. **统计方法严谨**：nonparametric bootstrap + paired permutation test + Bonferroni correction + effect sizes with CI 的组合在 ML 论文中罕见 [R1, R2 共识]\n3. **Phase-strategy crossover 有实际意义**：importance-based eviction 在不同 phase 优劣反转，对实际 compression 策略选择有指导价值 [R1, R2 共识]\n4. **Multiplicative null verification**：主动检验 additive vs multiplicative null 的 robustness [R1]\n5. **Limitations 诚实全面**：对样本量、架构限制、因果性限制等的讨论坦诚 [R2]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Critical Issues（两位 Reviewer 共识）\n\n**C1. Severity gradient G 的 69×-274× 倍数具有误导性** [R1-N2, R2-N2]\n- G = Π̃_low / Π̃_high，分母 Π̃_high 极小（0.006-0.053），比值对噪声极度敏感\n- 论文核心叙事（标题、Abstract、Conclusion）围绕 \"order of magnitude\" 展开，但这个数字本质是近零分母的放大效应\n- 绝对差异 Δ（0.39-14.59）更稳健但远不如 G 震撼\n- **要求**：报告 G 的 bootstrap CI；将 G 降为辅助指标，改用 Δ 和 d_z 作为主要效应量\n\n**C2. 样本量严重不足** [R1-N1, R2-N3]\n- n=50（实际 49/46），仅占 MATH-500 的 10%\n- Bootstrap CI 极宽（s=0.30 时 CI=[0.70, 16.29]，跨一个数量级）\n- Qwen s=0.15 效应不显著（d_z=0.28, CI 含零），但 Abstract 写 \"replicates at s≥0.20\" 给读者全面复现印象\n- 未报告问题选择的 random seed\n- **要求**：使用全部 500 题；报告 post-hoc power analysis；至少做 split-half stability analysis\n\n**C3. 同架构 \"跨模型复现\" 严重高估泛化性** [R1-N3, R2-N3]\n- DeepSeek 和 Qwen 共享 Qwen2ForCausalLM 架构（28 layers, 28 heads, 4-group GQA）\n- \"Cross-model replication\"（§5.4 标题）措辞误导——实际验证同架构不同训练配置\n- Per-problem concordance 不显著（mean ρ = −0.11）\n- Qwen 效应量仅为 DeepSeek 的 ~1/5，更接近 marginal replication\n- **要求**：增加至少一个非 Qwen 架构；或将 \"cross-model\" 改为 \"cross-training-regime\" 并弱化泛化声明\n\n**C4. Discrimination collapse 仅相关性证据** [R1-N4, R2-W1]\n- Gini 下降与 severity gradient 共现，但未排除混淆因素\n- Entropy redistribution 在 Qwen s=0.25 出现符号反转，削弱机制普遍性\n- 论文称 \"mechanistic explanation\" 但证据仅为 correlational\n- **要求**：改 \"mechanism\" 为 \"hypothesis\"/\"correlational evidence\"；或设计 causal intervention\n\n**C5. 贡献深度不足——纯观察无方法** [R2-N1; R1 moderate concern]\n- 三条贡献均为经验观察（identify/show/propose mechanism），无可操作方法\n- Phase-aware controller 仅停留概念层面\n- R2 视为 critical（Excitement 2.5/5），R1 视为 moderate concern（Excitement 3/5）\n- **要求**：实现 phase-aware compression budget（至少 oracle 版本）；或大幅扩大评估规模\n\n**C6. 数值不一致** [R1 initial N1]\n- Abstract/Table 1: Δ=14.59 vs §5.1: Δ=11.59\n- 主文 n=50 vs Appendix E n=49（1 excluded）\n- §6.2 ΔH ∈ [−0.080, −0.047] vs Table 7 ΔH ∈ [−0.047, −0.040]\n- Cohen's d: Abstract 0.41 vs 正文 0.44\n- **要求**：全面核对，确保所有数值一致\n\n**C7. Spearman ρ=1.0 (n=4) 统计无效** [R1 initial N2]\n- p=1/24≈0.042，未做 Bonferroni 修正后不再显著\n- 论文据此在 §7 声称 \"perfect ordinal agreement\" 作为泛化主要论据\n- **要求**：承认功效不足；降低泛化声明力度\n\n**C8. Limitations 节格式违反 ARR 要求** [R2 initial N1, R1 W7]\n- 当前为 §7.1 编号子节\n- ARR 要求独立无编号节于 Conclusion 后、References 前\n- **Desk reject 风险**\n- **要求**：立即修正格式\n\n**C9. 相关工作遗漏严重** [R2 initial N2, R2 updated]\n- 极高优先级：R-KV (NeurIPS 2025), Lethe (AAAI 2026), RLKV, \"Hold Onto That Thought\" (NeurIPS 2025)\n- 高优先级：RAC (NeurIPS 2025), RaaS (已在 bib 未引用), Scissorhands, FastGen, StreamingLLM\n- **要求**：补充所有极高/高优先级工作的讨论\n\n### Should-Fix Issues\n\n**S1.** Phase segmentation 缺乏 sensitivity analysis（tercile 切分未做 robustness check）[R1, R2]\n**S2.** 正文仅 ~5 页，关键表格（Table 2/3/5）应移入正文，充分利用 8 页空间 [R1, R2]\n**S3.** Abstract ~600 词，信息过载，应精简至 150-200 词 [R2]\n**S4.** 多重比较校正不充分（实际检验数远超 4，应用 FDR 校正）[R1]\n**S5.** Sparsity 范围窄（仅 4 levels），monotonicity 证据不足 [R1]\n**S6.** 仅 PPL 无 task accuracy 评估 [R1, R2]\n**S7.** II 与已有 super-additivity 概念区分不清 [R2]\n**S8.** Footnote 2 硬件信息泄露匿名性风险 [R1, R2]\n**S9.** Bibliography 管理问题（7 orphan entries, h2o title 空, 年份不一致）[R1, R2]\n**S10.** Appendix B 与 D 文本疑似重复 [R2]\n**S11.** Interaction Index 的 additive null 假设与核心论点（轴间交互）内在矛盾 [R1]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致 [AGREE]：\n1. G 指标近零分母 → 69×-274× 不可靠，需 CI + 降级\n2. n=50 不足 → 需扩至全部 MATH-500\n3. 同架构 ≠ 跨模型泛化 → 需非 Qwen 架构验证\n4. Discrimination collapse 是相关性非因果 → 降低 claim 或做 intervention\n5. 正文过短，关键表格应移入正文\n6. Phase segmentation 需 sensitivity analysis\n7. 相关工作遗漏严重（R-KV, Lethe, RLKV 等）\n\n## Reviewer Divergence\n\n**D1. 贡献深度 / Excitement**：\n- R2：critical，Excitement 2.5/5——EMNLP main conference 需要方法贡献，纯观察不够\n- R1：moderate concern，Excitement 3/5——观察性发现有价值但需更大规模支撑\n- 两者均认为当前不达 main conference 标准，分歧在严重程度\n\n**D2. Interaction Index 方法论**：\n- R1：additive null 假设（轴间独立）与论文核心论点（轴间交互）矛盾，建议增加 cross-entropy 空间分析\n- R2：关注 II 与已有 super-additivity 概念的区分\n- 视角不同但不冲突\n\n---\n\n## Questions for Authors\n\n1. 为什么不使用全部 500 道 MATH-500 题？如为计算资源限制请说明。\n2. G 的 bootstrap 95% CI？特别是 s=0.15 分母 II_high≈0.006 时。\n3. 各条件下 MATH-500 solve rate（accuracy）？PPL 恶化是否对应答案错误？\n4. 是否尝试过非 Qwen 架构（LLaMA 3, Mistral）？\n5. Phase-aware compression budget 的 oracle 版本相比 uniform budget 能提升多少 accuracy？\n6. Discrimination collapse 的 Gini 下降与 severity gradient 之间的 correlation coefficient？\n7. §5.1 \"11.59\" vs Table 1 \"14.59\" 哪个正确？Cohen's d 0.41 vs 0.44？\n8. 是否做过 split-half stability analysis 或 multiple generation seeds？\n9. 用 token position 等分或 think 标记做 phase segmentation 结果如何？\n10. 为什么选 Frobenius norm 而非 gradient-based importance 做 head pruning？论文提到 \"attention-independent metrics should produce flatter severity gradients\" 为何不验证？\n\n---\n\n## Missing References（合并去重）\n\n| 优先级 | 论文 | Venue | 理由 |\n|--------|------|-------|------|\n| 极高 | R-KV (Cai et al.) | NeurIPS 2025 | Reasoning model KV compression，直接相关 |\n| 极高 | Lethe (Zeng et al.) | AAAI 2026 | Phase-aware KV pruning，直接竞争 |\n| 极高 | RLKV / \"Which Heads Matter\" (Du et al.) | 2025/2026 | Head importance for reasoning，与 discrimination collapse 相关 |\n| 极高 | \"Hold Onto That Thought\" (Liu et al.) | NeurIPS 2025 | 系统评估 KV compression 对 reasoning 影响 |\n| 高 | RAC | NeurIPS 2025 | Reasoning model pruning via CoT reconstruction |\n| 高 | RaaS (Hu et al.) | ACL 2025 | 已在 bib 但未引用，reasoning-aware attention sparsity |\n| 高 | Scissorhands (Liu et al.) | NeurIPS 2023 | KV eviction 基础方法 |\n| 高 | FastGen (Ge et al.) | ICLR 2024 | Per-head adaptive KV cache |\n| 高 | StreamingLLM (Xiao et al.) | ICLR 2024 | Attention sink 基础 |\n| 高 | Titanus (Chen et al.) | GLSVLSI 2025 | KV pruning+quantization 复合效果 |\n| 中 | EVICPRESS (Fang et al.) | 2025 | Joint KV compression + eviction |\n| 中 | SparseGPT | ICML 2023 | 权重稀疏化基础 |\n| 中 | Wanda | ICLR 2024 | 轻量 pruning |\n| 中 | MInference | NeurIPS 2024 | 注意力稀疏模式分析 |\n| 中 | Cohen (1988) | — | Statistical Power Analysis（effect size 解读依据） |\n| 中 | LLM-Pruner (Ma et al.) | NeurIPS 2023 | Coupled pruning 开创性工作 |\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (2.5/5)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立评估后均给出 2.5/5（R1 从初始 3/5 在交叉分享后下调至 2.5/5，R2 维持 2.5/5）。\n\n**核心判断**：论文发现了一个有价值的经验现象（compound sparsity severity 的 phase 依赖性），实验设计有亮点（random eviction control），统计方法论严谨。但存在 9 个 critical 问题：\n1. 核心指标 G 受近零分母膨胀，headline 数字不可靠\n2. 样本量仅 50 题，统计功效不足\n3. 同架构\"跨模型\"验证高估泛化性\n4. 纯观察性贡献无方法提出\n5. Discrimination collapse 仅相关性证据\n6. 多处数值不一致\n7. Spearman ρ=1.0 (n=4) 统计无效\n8. Limitations 节格式违反 ARR 要求（desk reject 风险）\n9. 相关工作遗漏严重\n\n**建议路径**：\n- **立即修复（deadline 前可完成）**：C6(数值一致性), C7(弱化 ρ claim), C8(Limitations 格式), C9(补充引用), S2-S3(正文扩展), S8-S10(格式清理)\n- **需实验补充（可能需延期）**：C1(G 的 CI), C2(扩至 500 题), C3(增加非 Qwen 模型), C5(oracle phase-aware budget), S1(segmentation sensitivity), S5(更多 sparsity levels), S6(accuracy 指标)\n- **需重新定位**：C4(降低因果 claim), C5(如不加方法则转 Findings)\n\n当前状态不适合 EMNLP 2026 main conference。解决 C1-C3、C6-C9 + S1-S6 后可达 **Findings** 接收水平。如额外解决 C4-C5（加方法贡献 + 跨架构验证），可重投 main conference。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过长（~600 词），需精简至 150-200 词\n- 多处数值需核对（Δ=14.59 vs 11.59, d=0.41 vs 0.44）\n- \"over an order of magnitude\" 依赖不可靠的 G 指标\n\n### §1 Introduction\n- 贡献列表三条均为观察性，缺乏方法贡献\n- \"replicates across models\" 措辞需弱化\n\n### §2 Related Work\n- 遗漏 R-KV, Lethe, RLKV, Hold Onto That Thought 等 10+ 篇高相关工作\n- 第一段疑似混入 Experimental Setup 内容\n\n### §3 Background & Methods\n- G 定义的 ε 阈值未说明\n- II 与已有 super-additivity 概念区分不清\n- Additive null 假设与核心论点存在内在矛盾\n\n### §4 Experimental Setup\n- n=50 不足，选题标准不透明\n- 仅 2 模型同架构，4 sparsity levels\n- 仅 PPL 无 accuracy\n\n### §5 Results\n- §5.1: \"11.59\" vs Table 1 \"14.59\" 不一致\n- §5.2: G 的近零分母问题\n- §5.4: ρ=1.0 (n=4) 统计功效不足\n- §5.6: Discrimination collapse 仅相关性\n\n### §6 Discussion\n- Phase-aware controller 仅概念层面\n- ΔH range 与 Table 7 不一致\n\n### §7 Conclusion & Limitations\n- Limitations 格式违反 ARR（§7.1 编号子节 → 应为独立无编号节）\n\n### References & Appendix\n- 7 orphan bib entries\n- h2o-neurips2023 title 空\n- Appendix B 与 D 文本重复\n- Footnote 2 硬件信息泄露匿名性",
    "project": "phase-gated-compound-sparse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-14T13:19:16.947851+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_fdc656be1c7fe17c11ab639cdbce3710:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5232
}
```

</details>

---


### Assistant

_source line 120 · 2026-05-14T13:19:28.522940+00:00_

审稿报告已投递给 Research Director。

---

**Round 1 圆桌审稿完成。** 汇总：

**评分：Weak Reject (2.5/5)**，两位 Reviewer 一致。

**9 个 Critical 问题**：
1. G 指标近零分母 → 69×-274× 不可靠
2. n=50 样本量不足
3. 同架构"跨模型"高估泛化
4. 纯观察无方法贡献
5. Discrimination collapse 仅相关非因果
6. 多处数值不一致（14.59 vs 11.59, n=50 vs 49, d=0.41 vs 0.44）
7. ρ=1.0 (n=4) 统计无效
8. Limitations 格式违反 ARR（desk reject 风险）
9. 相关工作遗漏 10+ 篇

**建议**：当前不适合 EMNLP main conference。修复格式 + 数值 + 引用 + 扩大实验后可达 Findings 水平；加方法贡献 + 跨架构验证可重投 main conference。

Issue Tracker 已同步至 `artifacts/review_issues.yaml`（9 critical + 10 warning/info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 121 · 2026-05-14T13:19:29.738366+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**摘要**：Overall 2.5/5，Soundness 2.5/5，Excitement 3/5。

4 个 critical 问题：
1. **n=50 样本量严重不足** — 仅用 MATH-500 的 10%，Qwen 在 s=0.15 效应不显著（d_z=0.28），统计功效存疑
2. **Severity gradient G 的近零分母** — "69×–274×" 核心数字由 II_high≈0.006 的近零分母放大驱动，对噪声极度敏感
3. **同架构"跨模型"验证** — 两个模型共享 Qwen2 完全相同的架构，不能称为 cross-model replication
4. **Discrimination collapse 仅为相关性证据** — Gini/CV 下降→severity gradient 的因果链缺少 intervention 验证，且 Qwen 上 entropy redistribution 部分不复现

4 个 should-fix：additive null 内在矛盾、phase segmentation 无 sensitivity analysis、多重比较校正不充分、正文仅 ~5 页关键证据过度依赖 appendix。

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论：Overall 2.5/5（建议 Resubmit）。** 核心问题：

1. **新颖性不足**：三条贡献均为经验观察，未提出任何方法。Phase-aware compression budget 仅停留在概念层面。
2. **Severity gradient 指标 G 的 69×-274× 倍数由分母极小（Ĩ_high=0.006-0.053）驱动，具有误导性。**
3. **评估规模严重不足**：仅 2 个同架构（Qwen2）模型、50 道 MATH-500 题，无法支撑论文中"reasoning models"的一般化 claim。
4. **遗漏多篇关键相关工作**：R-KV (NeurIPS 2025)、RLKV (2025)、"Hold Onto That Thought" (NeurIPS 2025) 等直接相关工作未讨论。bib 中已有 RaaS 条目却未在正文引用。
5. **正文仅 ~5 页**，远未利用 8 页限制，大量关键表格被推入附录。

优势：统计方法严谨（permutation test + bootstrap + Bonferroni），random eviction 作为 falsification control 设计精巧，Limitations 诚实。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1

---

### Must-Fix 问题

**[AGREE] R1-N1: 数值不一致**
完全同意。这是严重的质量控制问题。三处不一致均可独立验证：
- 14.59 vs 11.59：Appendix D 的完整 breakdown table 明确显示 s=0.30 importance Δ=14.59（Ĩ_low=14.639 − Ĩ_high=0.053），因此 §5.1 的 "11.59" 几乎确定是笔误。
- n=50 vs n=49：Appendix 明确写 "n=49 paired problems for DeepSeek (1 excluded)"，主文 Table 1 标题却写 n=50。排除标准未在主文交代。
- ΔH 范围：Appendix I 的 Table 显示 DeepSeek ΔH = {−0.040, −0.047, −0.045, −0.044}，范围为 [−0.047, −0.040]，与 §6.2 声称的 [−0.080, −0.047] 明显矛盾。

我自己的审查未逐字核对 §5.1 的具体数值，R1 发现了我遗漏的问题。对于一篇以精确统计分析为核心卖点的论文，这类数值错误尤其致命。

**[AGREE] R1-N2: Cross-model ρ=1.0 (n=4) 无统计意义**
完全同意。4 个数据点的 Spearman ρ=1.0 仅意味着两个序列同为单调递增，p=1/24≈0.042 在 Bonferroni 校正后不再显著。任何两个随 sparsity 递增的量（哪怕机制完全不同）都会产生 ρ=1.0。论文在其他所有检验中均做了 Bonferroni 校正，唯独此处遗漏，构成 cherry-picking 嫌疑。

补充：Abstract 将此作为 cross-model replication 的核心证据（"replicates on Qwen2.5-7B-Instruct"），但 Qwen 的 effect size 仅为 DeepSeek 的 1/5（Table 3: Δ = 0.04→2.94 vs 0.39→14.59），且 s=0.15 处 CI 含零。用 ρ=1.0 来宣称 "replication" 是对这一术语的滥用——magnitude attenuation 这么大，更准确的说法是 "partial, qualitatively consistent but quantitatively much weaker pattern"。

**[AGREE] R1-N3: 样本量不足**
完全同意，与我的 N3 一致。补充两点：
1. R1 指出的 s=0.30 Bootstrap CI=[0.70, 16.29] 跨越一个数量级，这意味着 severity gradient 的 point estimate 不够精确——Δ 的真值可能是 0.70 也可能是 16.29，差 23 倍。
2. 右偏分布下（mean/median ratio 1.6:1, Appendix C），n=49 的 median 估计本身 bias 较小，但 variance 很大。论文选用 median 而非 mean 是正确的，但这不能补救样本量不足的根本问题。

**[AGREE] R1-N4: Severity gradient G 数值不稳定**
与我的 N2 完全一致。G 的分母 Ĩ_high 在 0.006-0.053 范围内，任何微小扰动都会导致 G 剧烈变化。R1 额外指出 ε 阈值（用于避免除零）未说明取值——这是我遗漏的一个好观察。如果 ε=0.001，G 的计算结果会显著不同于 ε=0.01。

---

### Should-Fix 问题

**[AGREE] R1-W1: Qwen s=0.15 marginal result 与 monotonicity 声明**
同意但补充一个 nuance：Abstract 实际上写了 "replicates on Qwen2.5-7B-Instruct at s≥0.20 (d_z≥0.55)"，即 Abstract 自身限定了 Qwen 的有效范围从 s≥0.20 开始。但 R1 的核心论点仍然成立——论文标题用 "Severity Gradients" 暗示一般性结论，而 Qwen s=0.15 的失败（d_z=0.28, CI 含零）说明 gradient 的存在条件比论文暗示的更窄。对于 claim 的表述精度，R1 的批评是合理的。

**[AGREE] R1-W2: 仅 2 个同架构模型的泛化过度**
与我的 N3 完全一致。两个模型共享 Qwen2ForCausalLM（28 layers, 28 heads, 4-group GQA），架构变量为零。DeepSeek vs Qwen 的差异仅来自训练（reasoning distillation vs instruction tuning），这是 training recipe 对比而非 architecture 对比。论文使用 "cross-model replication" 一词时，读者的合理预期是不同架构的验证。

**[REBUT] R1-W3: Phase segmentation 与 outcome 的概念耦合/confounding**
部分反驳。R1 的 concern 有一定道理——phase 由 attention sparsity (Eq. 6) 定义，outcome (II) 也依赖 attention-based metrics——但论文的 random eviction falsification control 实质性地缓解了这一问题。

具体论证：如果 confounding 是 trivial 的（即 phase 定义本身就决定了 severity gradient），那么 random eviction 也应展现 phase gradient，因为 phase assignment 对两种 strategy 完全相同（phase 是在 baseline 无压缩条件下定义的，不依赖 eviction strategy）。但实验结果显示 random eviction 在 7/8 条件下无显著 phase gradient（Table 1），这排除了 "phase 定义本身导致 gradient" 的 trivial 解释。

然而，R1 的 concern 并非完全无效：attention sparsity 定义的 phase 可能与 importance-based eviction 有 mechanistic coupling（高 entropy phase → 更均匀 importance → eviction 更 random-like → 更少 compound interaction），这恰恰是 discrimination collapse 所描述的机制。所以 confounding 和 mechanism 在这里是同一件事——问题是论文是否充分讨论了这一点。建议作者在正文明确承认 phase definition 和 mechanism 的 coupling，并讨论用 non-attention-based phase segmentation（如 token position 等分或 &lt;think> 标记）验证 robustness。

**[AGREE] R1-W4: 仅 4 个 sparsity levels 不足以论证 monotonicity**
同意。4 个数据点只能说 "在测试的 4 个 s 值上观察到递增趋势"，不能称为 "monotonic growth"。特别是：(a) 没有测试 s<0.15 或 s>0.30，不知道边界行为；(b) 4 点的任何排列中有 4!/4!= 1/24 ≈ 4.2% 的概率恰好递增，与 ρ=1.0 的 p-value 一样尴尬。

**[AGREE] R1-W5: Cohen's d 解读不准确 + 数值不一致**
同意。Cohen (1988) 的标准 convention 是 small=0.2, medium=0.5, large=0.8。d_z=0.44 是 small-to-medium，不是 "small"；d_z=0.80 是 large 的起始阈值，不是 firmly large。Abstract 写 d=0.41 但 Appendix Table 5 写 d_z=0.44——又一处数值不一致，支持 R1-N1 的系统性质量问题判断。

**[AGREE with caveat] R1-W6: 缺少 task accuracy 评估**
基本同意。论文使用 MATH-500 problems 但未报告 solve rate（各条件下正确率），仅报告基于 performance ratio 的 interaction index。对于 reasoning 任务，accuracy 是最终 metric——PPL 或 performance ratio 的变化不能直接说明 "这个 sparsity 配置是否仍能正确解题"。

不过我加一个 caveat：如果论文的目标是 characterize interaction patterns 而非 recommend deployment configs，那么 II 作为 relative metric 是合理的。但论文 Section 7 (Conclusion) 和 Discussion 确实提到了 "deployment" 和 "phase-aware sparsity allocation"，这就要求 accuracy 数据来支撑实际影响。

**[AGREE] R1-W7: Limitations 节格式**
同意但认为这是 minor issue。ACL/ARR 确实要求 Limitations 作为正文最后的独立无编号节，不计入页数限制。如果论文将其编号或放在不正确位置，需要修正。但这是纯格式问题，修正成本极低。

---

### Missing References

**[AGREE] R1-MR1: Cohen (1988) Statistical Power Analysis**
同意。论文大量使用 Cohen's d 但未引用原始出处，且解读有误（W5）。加入 Cohen (1988) 并修正解读。

**[AGREE] R1-MR2: RaaS (Hu et al., 2025) 在 bib 中未被引用**
与我自己的发现完全一致。RaaS 已在 bib 中（`raas-acl2025`）但正文从未 \cite，这是一个明显的疏忽。RaaS 发现了 reasoning 中的 "milestone tokens" 现象，与论文的 phase-dependent importance 高度相关。

**[PARTIAL AGREE] R1-MR3: Per-layer 非对称 sparsity 方法（OWL, Wanda）**
部分同意。OWL 和 Wanda 是 weight pruning 方法，与论文研究的 inference-time sparsity (attention head pruning + KV cache eviction) 有本质区别。然而，OWL 的核心思想（per-layer adaptive sparsity budget）与论文提出的 "phase-aware sparsity allocation" 概念有类比价值。建议在 Discussion 中简要提及而非必须在 Related Work 详细讨论。

补充我自己发现的遗漏（R1 未提及）：
- **R-KV** (NeurIPS 2025): Reasoning model 专用 KV cache 压缩，识别冗余 token。直接相关。
- **RLKV** (2025/2026): RL-guided head identification for reasoning，与 head pruning + reasoning 的交互直接相关。
- **"Hold Onto That Thought"** (NeurIPS 2025): KV cache compression 对 reasoning integrity 的系统评估。

---

### 总体评价一致性

R1 给出 3/5（Findings-level），我给出 2.5/5（Findings 和 Resubmit 之间）。我们在核心判断上高度一致：

**共识点：**
1. 评估规模不足（n=50, 2 同架构模型）——我们都列为 critical
2. G 指标的分母敏感性——我们都列为 critical
3. 缺乏方法论贡献——我们都认为 "止步于现象描述" 是核心弱点
4. Random eviction 作为 falsification control 是优秀设计——我们都认可
5. 统计方法整体规范——我们都肯定

**分歧点：**
- R1 给 3/5 (Findings-level)，我给 2.5/5。差异来自我对**新颖性**的更严格要求：我认为在没有方法贡献的前提下，纯观察性发现需要更大规模（多架构、多任务）才能达到 Findings 门槛。R1 似乎认为现象本身的学术价值（phase-strategy crossover）已足够 Findings。
- R1 发现了我遗漏的数值不一致（§5.1 的 11.59 vs 14.59, ΔH 范围矛盾, d=0.41 vs 0.44）——这些进一步降低了我的评分信心。
- 我在 confounding (W3) 上给出了 partial rebut，认为 random eviction control 在相当程度上缓解了这一 concern。

**综合建议：** 维持 Resubmit 建议。R1 发现的多处数值不一致加上我们共同识别的规模不足和 G 指标误导性问题，使论文在当前状态下不适合接收。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

**与 R1 的 12 条意见中，10 条 [AGREE]，1 条 [PARTIAL AGREE]，1 条 [REBUT]：**

- **[AGREE]** N1 数值不一致、N2 ρ=1.0 无意义、N3 样本量不足、N4 G 指标不稳定、W1 Qwen monotonicity 过度声明、W2 泛化过度、W4 仅 4 个 sparsity levels、W5 Cohen's d 误读、W6 缺 accuracy、W7 Limitations 格式
- **[PARTIAL AGREE]** OWL/Wanda 遗漏（weight pruning 与 inference-time sparsity 有本质区别，但 adaptive budget 思想值得类比讨论）
- **[REBUT]** W3 phase segmentation confounding — random eviction 在相同 phase assignment 下无 gradient（7/8 non-significant），排除了 phase 定义本身导致 gradient 的 trivial 解释

核心分歧：R1 给 3/5 (Findings)，我给 2.5/5。我对新颖性要求更严格——没有方法贡献时，纯观察性发现需要更大评估规模支撑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 122 · 2026-05-14T13:20:06.189847+00:00_

审稿报告已于此前提交。现收到 Reviewer 2 的详细交叉回应，确认了报告中的共识判断。

**交叉分享最终结果汇总**：

| R1 意见 | R2 回应 | 状态 |
|---------|---------|------|
| N1 数值不一致 | [AGREE] — 确认 §5.1 "11.59" 为笔误，正确值 14.59 | 共识 |
| N2 ρ=1.0 (n=4) 无意义 | [AGREE] — 补充指出 magnitude attenuation 1/5，"replication" 措辞滥用 | 共识 |
| N3 样本量不足 | [AGREE] — 补充 CI=[0.70,16.29] 差 23 倍 | 共识 |
| N4 G 分母不稳定 | [AGREE] — 补充 ε 阈值缺失 | 共识 |
| W1 Qwen monotonicity | [AGREE] — 含 nuance（Abstract 已限定 s≥0.20） | 共识 |
| W2 泛化过度 | [AGREE] | 共识 |
| **W3 Phase confounding** | **[REBUT]** — random eviction 在相同 phase 下无 gradient (7/8)，排除 trivial 解释 | **分歧** |
| W4 仅 4 levels | [AGREE] | 共识 |
| W5 Cohen's d 误读 | [AGREE] | 共识 |
| W6 缺 accuracy | [AGREE with caveat] — 若目标仅为 characterize patterns 则 II 合理，但论文提了 deployment | 共识 |
| W7 Limitations 格式 | [AGREE] — minor, 修正成本低 | 共识 |
| MR3 OWL/Wanda | [PARTIAL AGREE] — weight pruning ≠ inference-time sparsity，但 adaptive budget 思想可类比 | 部分共识 |

**唯一实质分歧（W3）**：R2 认为 random eviction falsification control 在相当程度上缓解了 phase segmentation confounding。R1 认为 attention sparsity 定义 phase 与 attention-dependent outcome 存在概念耦合。R2 进一步澄清——confounding 和 mechanism (discrimination collapse) 可能是同一件事，建议作者明确讨论这一 coupling 并用 non-attention-based segmentation 验证。

**最终评分**：R1 2.5/5, R2 2.5/5 → 综合 **Weak Reject (2.5/5)**

审稿报告已投递至 Research Director，Issue Tracker 已同步更新（9 critical + 10 warning/info issues）。Round 1 圆桌审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 123 · 2026-05-14T13:20:36.105954+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（Round 1）

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
**审查侧重**: 方法严谨性 + 实验设计与评估
**Reviewer ID**: 1

---

## 1. 总体评分（ACL ARR Review Form）

| 维度 | 分数 | 理由 |
|------|------|------|
| **Soundness** | 2.5/5 | 核心指标 G 受近零分母放大，n=50 统计功效不足，因果机制仅为相关性。主要 claims 的证据支撑不够充分。 |
| **Excitement** | 3/5 | 研究问题（compound sparsity 的 phase-strategy 交互）有实际部署价值，但执行局限性显著削弱了 excitement。如果实验能扩大规模并跨架构验证，会是一篇有价值的论文。 |
| **Overall Assessment** | 2.5/5 | 介于 "Resubmit next cycle"(2) 和 "Findings acceptance"(3) 之间。核心发现有潜力，但需要显著增强实验证据后重投。 |
| **Reproducibility** | 3/5 | 实验描述基本充分（模型、sparsity levels、decoding 策略均已报告），但缺少代码公开承诺、未指定 50 题的具体选取方式、关键参数散落在 appendix 中。 |
| **Confidence** | 4/5 | 仔细阅读全文（含全部 appendix），熟悉 KV cache compression、attention pruning、bootstrap/permutation 统计方法相关工作。 |

---

## 2. Must-Fix 问题

### **N1** [critical] n=50 样本量不足以支撑论文的定量 claims

- **位置**: Section 4 ("50 problems from MATH-500")；Table 1；Section 5.4 (Qwen n=46)；Table 5 (Appendix G)
- **问题**:
  - 仅使用 MATH-500 的 10%（50 题），每题 1 次 greedy decoding，无重复采样。MATH-500 有 500 题且公开可用，选取 50 题未给出理由（计算成本？随机子集？难度分层？）。
  - 在 Bonferroni 校正后（α_eff = 0.0125），paired nonparametric test 对 n=50 的最小可检测 Cohen's d_z ≈ 0.45-0.50。Table 5 显示 Qwen 在 s=0.15 时 d_s=0.25（另一处报告 0.28），远低于此阈值，bootstrap CI 包含零。论文在 Table 5 脚注标注为 "Marginal at s=0.15"，但 abstract 写 "replicates at s ≥ 0.20" 时未同等强调 s=0.15 的失败——给读者造成全面复现的印象。
  - 论文承认 mean/median ratio 高达 43:1 的重度右偏。在如此偏态分布下，50 个样本的 median bootstrap CI 宽度可能覆盖了论文报告的效应量级。
  - Qwen 排除了 4 题（"degenerate phase assignments"），进一步减少至 n=46。排除标准是否事先确定？是否存在 researcher degrees of freedom？
- **为什么影响接收**: 论文的全部定量 claims（severity gradient 倍数、effect sizes、p-values）建立在 n=50 之上。如果增加到 n=500，效应方向不变但 magnitude 改变，核心叙事就需要重写。
- **建议**: (1) 使用全部 500 题，或至少 200+ 题并报告选取策略；(2) 增加 post-hoc power analysis；(3) 对关键条件做 multiple random seeds 验证 median 估计稳定性。

### **N2** [critical] Severity gradient G (Eq. 2) 的 "69×–274×" 数字由近零分母驱动，统计不可靠

- **位置**: Eq. 2（G = Π̃_high / Π̃_low）；Section 5.2；Table 2 (Appendix D)
- **问题**:
  - Table 2 显示 importance-based eviction 在 high-sparsity phase 的 median II 极小：s=0.15 时 Π̃_high ≈ 0.006。G = Π̃_low / Π̃_high = 0.508/0.006 ≈ 85×。当分母为 0.006 时，0.006→0.012 的微小波动就会使 G 减半（85×→42×）；0.006→0.003 则使 G 翻倍（85×→170×）。
  - 论文未报告 G 本身的 bootstrap CI。对于分母含零附近值的比值统计量，bootstrap CI 理论上可以包含 ∞。不报告 CI 而只报告点估计，掩盖了这个不确定性。
  - 对比：Table 1 的 Δ（绝对中位差）从 0.39 到 14.59，增长 37×——这是一个更稳健的指标，但论文选择在标题、abstract、conclusion 中反复使用更不稳定的 G（69×–274×）作为核心叙事。
- **为什么影响接收**: "order of magnitude" severity gradient 是论文的标题级 claim。如果这个数字的不确定性跨越一个数量级本身，论文的核心卖点就不可靠。
- **建议**: (1) 报告 G 的 bootstrap CI；(2) 同时以 Δ（中位差）和 G（比值）双重呈现核心结果；(3) 如果 G 的 CI 过宽，考虑用 log(G) 或 rank-based 指标重构叙事。

### **N3** [critical] "跨模型复现" 使用同一架构（Qwen2ForCausalLM），泛化性声明过强

- **位置**: Section 4（"two 7B parameter models sharing the Qwen2 backbone"）；Section 5.4（"Cross-Model Validation"）；Appendix F；Appendix J
- **问题**:
  - DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 共享完全相同的 Qwen2ForCausalLM 架构（28 layers, 28 heads, 4-group GQA）。Appendix F 自己写道 "This controlled comparison isolates the effect of training methodology"——也即论文清楚这只是 cross-training 而非 cross-architecture 验证。
  - 但 Section 5.4 标题为 "Cross-Model Validation"，abstract 写 "replicates on Qwen2.5-7B-Instruct"，这些措辞给读者造成了跨模型泛化的印象。
  - Appendix F 报告 per-problem concordance mean ρ = −0.11——两个模型在 problem 层面的 severity pattern 不仅不一致，甚至负相关。这意味着 aggregate 方向一致是由不同问题子集驱动的，进一步削弱了 "robust replication" 的说法。
  - Qwen 全部效应量级为 DeepSeek 的 ~1/5，且 s=0.15 不显著。这更像是 partial replication 而非 robust replication。
  - Appendix I 的 "Architecture generality" 讨论承认需要在 LLaMA 3.x、Mistral 等上验证，但论文正文 claims 未做相应降级。
- **为什么影响接收**: 泛化性是 Contribution #2 的核心。观察到的现象可能是 Qwen2 GQA 的 4-group design 和特定 attention redistribution pattern 的 artifact。
- **建议**: (1) 将 "Cross-Model Validation" 改为 "Cross-Training Validation"；(2) 在 abstract/conclusion 明确标注架构限制；(3) 增加至少一个架构不同的模型（LLaMA 3.x / Mistral / Gemma2）。

### **N4** [critical] Discrimination collapse (§5.6) 被呈现为 "mechanistic explanation"，但证据仅为相关性

- **位置**: Section 5.6；Table 6 (Appendix H)；Appendix K
- **问题**:
  - 论文的 Contribution #3 明确声称 "entropy-discrimination collapse as a mechanistic explanation"（Section 1）。但实际证据是：(a) head pruning 后 Gini coefficient 下降（Table 6, 8/8 条件一致）；(b) CV 同步下降。从 "Gini 下降 → 重要性分数区分度降低 → eviction 更像随机" 的逻辑链中，(a)→(b) 是观察性相关，缺乏 intervention 证据。
  - 多种混杂因素未排除：不同 phase 的 baseline perplexity 差异、head 功能冗余度的 phase 差异、token-level 语义复杂度差异等都可能同时导致 Gini 下降和 severity 上升。
  - Appendix K 的 entropy redistribution 分析在 Qwen 上部分不复现（论文 Limitations 承认 "non-contributing eviction replicates on only 2/4 Qwen conditions"）。如果机制解释的子组件在第二个模型上仅部分成立，将其称为 "mechanism" 而非 "correlational pattern" 是过度声称。
  - Appendix I 提出了一个 "testable prediction"（非 attention-mass-based metrics 应产生更平坦 gradient），但论文本身没有检验这个预测。
- **为什么影响接收**: 将相关性证据升格为因果机制是方法论上的重大问题。
- **建议**: (1) 做 controlled intervention——如人为注入噪声维持 Gini 不变后观察 severity gradient 变化；(2) 检验 Appendix I 提出的 testable prediction（用 gradient-based saliency 替代 attention-mass importance）；(3) 或降低 claim 强度为 "a correlational pattern consistent with discrimination collapse"。

---

## 3. Should-Fix 问题

### **W1** [major] Additive null (Eq. 1) 的选择理由与论文核心发现存在逻辑张力

- **位置**: Section 3（"additive null because the two axes operate on disjoint dimensions"）；同 Section（"head pruning alters the importance ranking used for eviction"）
- **问题**: 选择 additive null 的理由是轴间独立性（"disjoint dimensions"），但论文的核心发现正是轴间存在 super-additive 交互。这不是说 additive null 本身错误（它是被检验的假设），但论文对选择理由的表述自相矛盾。Appendix B 验证 multiplicative null 产生类似结论是好的。然而，更深层的问题是：PPL 是 cross-entropy 的指数，在 PPL ratio 空间的 additive interaction 对应概率空间的非线性关系。论文应在 cross-entropy 空间做 robustness check。
- **建议**: (1) 修正 Section 3 对 additive null 选择的论述——不要说"因为独立所以选 additive"，改为"additive null 作为独立性基线被检验"；(2) 增加 cross-entropy 空间的 interaction analysis。

### **W2** [major] Phase segmentation 无 sensitivity analysis，tercile 切分缺乏理论基础

- **位置**: Section 3（"quantile-based tercile"）；Appendix A（"min_phase_length=10"）
- **问题**: 论文的全部结果依赖于 tercile 切分。不同切分方案（quartile、decile、固定阈值、不同 min_phase_length）可能产生不同结果。论文引用 ThinKV 作为先例但未提供选择 tercile 的理论理由。min_phase_length=10 的选择同样缺乏解释。
- **建议**: 至少用 2-3 种切分方案做 sensitivity analysis，报告 G 和 Δ 的稳定性。

### **W3** [major] 多重比较校正范围不足

- **位置**: Section 4（"Bonferroni correction for 4 sparsity-level comparisons"）
- **问题**: Bonferroni/Holm 仅覆盖 4 个 sparsity level 的 paired test。但论文实际执行了远超 4 个假设检验：2 strategies × 4 levels × per-phase 比较、crossover 检验、cross-model 比较、Gini/CV 分析、monotonicity permutation test 等。总检验数目保守估计 >20。当前的 family-wise error correction 只覆盖了检验空间的一小部分。
- **建议**: 列出所有执行的假设检验，应用 FDR 校正（Benjamini-Hochberg）覆盖全部；或至少明确说明哪些检验是 primary（受 FWER 保护），哪些是 exploratory。

### **W4** [major] 正文仅 ~5 页，关键定量证据过度依赖 Appendix

- **位置**: 全文结构
- **问题**: ACL ARR long paper 上限 8 页正文，但论文仅使用约 5 页。Table 2（per-phase II 分解——核心 finding 的直接数据支撑）、Table 5（effect sizes with CIs——统计结论的基础）、Table 6（discrimination collapse 数据——Contribution #3 的证据）均在 appendix。按 ARR 规则，"审稿人不保证阅读附录"——这意味着仅看正文的审稿人无法核实核心 claims。
- **建议**: 将 Table 2 和 Table 5 移入正文。论文有 3 页 budget 可以利用。

### **W5** [minor] Sparsity 覆盖范围偏窄，仅 4 个等间距水平

- **位置**: Section 4（s ∈ {0.15, 0.20, 0.25, 0.30}）；Appendix I（"s=0.35 时 high-phase II 开始上升"）
- **问题**: 4 个 level 支撑 "monotonic" 声称说服力有限——4 点 Spearman ρ=1.0 的 p=0.042，勉强显著。Appendix I 暗示 s>0.30 可能出现质变点但未探索。更宽的范围（如 s ∈ {0.10, 0.15, ..., 0.40}）能大幅增强 monotonicity claim 的可信度。
- **建议**: 增加至少 2-3 个 sparsity level，特别是 s>0.30。

### **W6** [minor] Appendix 中存在疑似段落重复

- **位置**: Appendix I、Appendix J、Appendix K 跨页文本
- **问题**: 多个段落在不同 appendix 中出现了几乎相同的表述（如 "the sub-exponential growth pattern suggests..."、Qwen random s=0.30 的讨论）。这可能是编辑疏忽导致的文本重复，影响论文的专业质感。
- **建议**: 全文去重检查。

---

## 4. 主要优势

1. **研究问题定位精准**: Compound sparsity 的 phase-dependent 行为对推理模型部署有直接实际意义——如果 severity 真的跨 phase 变化一个数量级，当前的 uniform budget 策略确实不够。这个问题在 prior work（SparK, UniComp, ThinKV）中被忽视。

2. **实验设计中 random eviction 作为 falsification control 非常巧妙**: 7/8 random 条件不显著有效排除了 compound sparsity 的 trivial 解释（即"任何两种压缩方法组合都天然产生 phase gradient"）。唯一例外（Qwen s=0.30, p=0.012, d_s=−0.01）被诚实报告并用于论证效应量的重要性——这本身是良好的统计实践。

3. **统计方法论选择合理（方法层面）**: 面对重度右偏分布（mean/median ratio 43:1），选用 median-based statistics + nonparametric bootstrap + paired design，方法选择正确。问题在于样本量不足以发挥这些方法的优势。

4. **Appendix B 主动验证 multiplicative null**: 自发检验了 additive vs multiplicative formulation 的 robustness，体现了方法论自觉。

5. **Strategy crossover 发现（Section 5.3）有实际指导意义**: importance-based eviction 在 high-sparsity phase 优于 random、在 low-sparsity phase 劣于 random——如果可靠，这意味着 phase-aware strategy switching 有实际收益。

6. **Limitations section 诚实且全面**: Appendix J 的 extended limitations 坦诚讨论了模型规模、架构范围、任务覆盖、统计范围的不足，这是好的学术实践。

---

## 5. Questions for Authors

**Q1.** 为什么只用 50 题而非全部 MATH-500？如果是计算资源限制，请量化（需要多少 GPU-hours 扩展到 500 题）。如果是其他原因，请说明选取策略（随机？分层？）。

**Q2.** G 的 bootstrap 95% CI 是多少？特别是 s=0.15 时 Π̃_high ≈ 0.006，该 CI 是否包含零？如果包含零，G 的 CI 理论上为 [某值, +∞)，如何解释 "69×" 这个数字的可靠性？

**Q3.** Appendix F 报告 per-problem concordance mean ρ = −0.11。这意味着两个模型的 severity 在 problem 层面负相关。作者如何调和这与 "cross-model replication" 的说法？

**Q4.** 论文在 Appendix I 提出了可检验预测："非 attention-mass-based 的 importance metric 应产生更平坦的 severity gradient。" 是否尝试过用 gradient-based saliency 或 activation magnitude 做初步验证？

**Q5.** Section 4 的 footnote 1 写道 "An earlier bfloat16 configuration produced sporadic NaN values; bfloat16 eliminated all occurrences"——这里似乎应为 "float16 → bfloat16"？请澄清。此外，NaN 出现在哪些条件下？其根因是否影响 PPL 计算的数值稳定性？

**Q6.** 4 题在 Qwen 上被排除（"degenerate phase assignments, all tokens in a single phase"）。排除标准是否事先确定（pre-registered）？这些被排除的题是否恰好是 high-severity 或 low-severity 的极端案例？

**Q7.** 论文在 Section 6 和 Section 7 多次提到 "phase-aware compression budgets" 作为实际 implication，但未提供任何 proof-of-concept 实现。是否计划在 camera-ready 中加入？

---

## 6. 小问题列表

1. **引用**: .bib 中 `h2o-neurips2023` 条目缺少 title 字段。7 条 orphan bib entries 未被引用（compression-ordering-2025, h2o-neurips2023, mustafar-neurips2025, obcache-2025, pagedeviction-eacl2026, pyramidkv-2024, raas-acl2025）——应清理。
2. **Eq. 2 符号**: G = Π̃_high / Π̃_low——"high" 和 "low" 在此处指 high-sparsity phase 还是 high-II phase？正文说 "G ≫ 1 indicates phase-concentrated severity"，但如果是 Π̃_high_sparsity_phase / Π̃_low_sparsity_phase，且 low-sparsity phase II 更大，则 G < 1。建议明确定义或改用 Π̃_max / Π̃_min。
3. **Section 2 (Related Work)**: "compound compression" 段落末尾突然出现模型描述（"Qwen2.5-7B-Instruct (Yang et al., 2024), with standard inference training, providing a cross-model replication target"），疑似从 Section 4 错误复制到 Related Work。
4. **Table 1 符号**: 表头定义 Δ = Π̃_low − Π̃_high，但正文 Section 5.1 说 "Δ increases from 0.39"（正值），而 Table 2 中部分 Δ 为负值。请统一符号约定并确保正文与表格一致。
5. **Abstract 中 "paired hen's d₁"**: 应为 "paired Cohen's d_z"。
6. **脚注 2 硬件标注**: 请核实 GPU 型号（RTX PRO 4000 / 6000 / 8000 Blackwell？不同处出现不同型号）。
7. **代码与数据**: 论文未提及代码公开计划。ARR 鼓励提交 reproducibility checklist——建议在 camera-ready 中承诺公开代码和 50 题选取列表。

---

*审查依据: ACL Rolling Review 官方 review form (aclrollingreview.org/reviewform)，ARR reviewer guidelines (aclrollingreview.org/reviewerguidelines)。*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 124 · 2026-05-14T13:21:24.504303+00:00_

审稿报告已于此前成功提交给 Research Director（Weak Reject 2.5/5）。

当前收到的是 Reviewer 1 的最终审稿意见和 Reviewer 2 的交叉回应，两者与已提交报告的核心结论完全一致：

**收敛状况**：
- R1: 2.5/5, R2: 2.5/5 — 评分一致
- R2 交叉回应：12 条中 10 条 [AGREE]、1 条 [PARTIAL AGREE]、1 条 [REBUT]
- 唯一 [REBUT]：R2 认为 random eviction control 已实质性缓解 phase segmentation confounding 问题（7/8 null results 排除了 trivial 解释）— 这一论点合理，但不改变整体评估

**报告已涵盖的全部 critical issues**：
1. G 指标近零分母 (C1)
2. n=50 样本量不足 (C2)
3. 同架构伪跨模型验证 (C3)
4. Discrimination collapse 仅相关性 (C4)
5. 纯观察无方法贡献 (C5)
6. 数值不一致 (C6)
7. ρ=1.0(n=4) 统计无效 (C7)
8. Limitations 格式违规 (C8)
9. 相关工作遗漏 (C9)

无需强制重新提交。审稿流程已完成，报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 8

## Round 8

8 recorded events


### User

_source line 125 · 2026-05-14T13:21:27.180147+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**评分摘要**: Soundness 2.5/5, Excitement 3/5, Overall 2.5/5, Reproducibility 3/5, Confidence 4/5。

**4 个 critical 问题**:
1. n=50 样本量不足（MATH-500 的 10%，Qwen s=0.15 效应不显著 d_s=0.25）
2. Severity gradient G 的 "69×–274×" 由 Π̃_high≈0.006 的近零分母放大，未报告 CI
3. 同架构（Qwen2ForCausalLM）"跨模型"验证 + per-problem concordance ρ=−0.11 负相关
4. Discrimination collapse 仅相关性证据，Qwen 上 entropy redistribution 部分不复现

**4 个 major 问题**: additive null 论述自相矛盾、phase segmentation 无 sensitivity analysis、多重比较校正范围不足、正文仅~5 页关键表格全在 appendix。

新增发现：Related Work 段落疑似混入 Section 4 内容、abstract 中 "hen's d₁" 应为 "Cohen's d_z"、脚注 1 bfloat16 描述自相矛盾、GPU 型号在不同位置不一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-14T13:22:06.571879+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml | wc -l",
  "description": "Check review_issues.yaml length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml | wc -l",
    "description": "Check review_issues.yaml length"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-14T13:22:06.927562+00:00_

361

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-14T13:22:14.071217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
  "offset": "340"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
    "offset": "340"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-14T13:22:14.122676+00:00_

340	        status: open
341	    resolution: ""
342	    resolution_round: null
343	
344	  - id: "R1-W6"
345	    summary: "Appendix B 与 Appendix D 文本疑似重复"
346	    category: writing
347	    severity: info
348	    status: open
349	    first_raised_round: 1
350	    last_seen_round: 1
351	    mentions:
352	      - round: 1
353	        reviewers: [2]
354	        note: "Initial R2-W6：两个 appendix 文本几乎完全重复，疑为粘贴错误。"
355	    action_items:
356	      - round: 1
357	        action: "检查并修正 Appendix 重复内容"
358	        assigned_to: "author"
359	        status: open
360	    resolution: ""
361	    resolution_round: null
362	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-14T13:22:30.777031+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
  "old_string": "  - id: \"R1-W6\"\n    summary: \"Appendix B 与 Appendix D 文本疑似重复\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Initial R2-W6：两个 appendix 文本几乎完全重复，疑为粘贴错误。\"\n    action_items:\n      - round: 1\n        action: \"检查并修正 Appendix 重复内容\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null",
  "new_string": "  - id: \"R1-W6\"\n    summary: \"Appendix B 与 Appendix D 文本疑似重复\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Initial R2-W6：两个 appendix 文本几乎完全重复，疑为粘贴错误。R1 最终稿也确认 Appendix I/J/K 存在跨页重复段落。\"\n    action_items:\n      - round: 1\n        action: \"检查并修正 Appendix 重复内容\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W7\"\n    summary: \"Abstract 笔误 'hen's d₁' 应为 'Cohen's d_z'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Abstract 中 'paired hen's d₁' 应为 'paired Cohen's d_z'，明显排版/拼写错误。\"\n    action_items:\n      - round: 1\n        action: \"修正 Abstract 中的 Cohen's d 拼写\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W8\"\n    summary: \"脚注 1 bfloat16 描述自相矛盾 + GPU 型号不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"脚注 1 写 'bfloat16 eliminated all occurrences' 语义不清（应为 float16→bfloat16 消除 NaN）。GPU 型号在不同位置出现 RTX PRO 4000/6000 不一致。\"\n    action_items:\n      - round: 1\n        action: \"修正脚注 1 表述；统一 GPU 型号描述\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W9\"\n    summary: \"Related Work 段落疑似混入 Experimental Setup 内容\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Section 2 末尾出现模型描述 'Qwen2.5-7B-Instruct...providing a cross-model replication target'，应属 Section 4。\"\n    action_items:\n      - round: 1\n        action: \"将模型描述内容移至 Section 4\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
    "old_string": "  - id: \"R1-W6\"\n    summary: \"Appendix B 与 Appendix D 文本疑似重复\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Initial R2-W6：两个 appendix 文本几乎完全重复，疑为粘贴错误。\"\n    action_items:\n      - round: 1\n        action: \"检查并修正 Appendix 重复内容\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null",
    "new_string": "  - id: \"R1-W6\"\n    summary: \"Appendix B 与 Appendix D 文本疑似重复\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Initial R2-W6：两个 appendix 文本几乎完全重复，疑为粘贴错误。R1 最终稿也确认 Appendix I/J/K 存在跨页重复段落。\"\n    action_items:\n      - round: 1\n        action: \"检查并修正 Appendix 重复内容\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W7\"\n    summary: \"Abstract 笔误 'hen's d₁' 应为 'Cohen's d_z'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Abstract 中 'paired hen's d₁' 应为 'paired Cohen's d_z'，明显排版/拼写错误。\"\n    action_items:\n      - round: 1\n        action: \"修正 Abstract 中的 Cohen's d 拼写\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W8\"\n    summary: \"脚注 1 bfloat16 描述自相矛盾 + GPU 型号不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"脚注 1 写 'bfloat16 eliminated all occurrences' 语义不清（应为 float16→bfloat16 消除 NaN）。GPU 型号在不同位置出现 RTX PRO 4000/6000 不一致。\"\n    action_items:\n      - round: 1\n        action: \"修正脚注 1 表述；统一 GPU 型号描述\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W9\"\n    summary: \"Related Work 段落疑似混入 Experimental Setup 内容\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Section 2 末尾出现模型描述 'Qwen2.5-7B-Instruct...providing a cross-model replication target'，应属 Section 4。\"\n    action_items:\n      - round: 1\n        action: \"将模型描述内容移至 Section 4\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-14T13:22:30.828491+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Edit",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 132 · 2026-05-14T13:22:39.680266+00:00_

Issue Tracker 已补录 4 个 info 级问题（R1-W7 ~ R1-W9）。

**审稿状态总结**：Round 1 圆桌审稿已完成并提交。

- **R1**: 2.5/5（方法严谨性+实验评估）
- **R2**: 2.5/5（新颖性+相关工作+格式）
- **交叉分享**：R2 对 R1 的 12 条意见中 10 AGREE / 1 PARTIAL AGREE / 1 REBUT（confounding 问题被 random eviction control 部分缓解）
- **Overall**: **Weak Reject (2.5/5)**
- **Issue Tracker**: 9 critical + 10 warning + 4 info = 23 issues

报告已投递至 Research Director，审稿阶段结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 9

## Round 9

10 recorded events


### User

_source line 133 · 2026-05-14T13:22:41.345747+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 针对 Reviewer 2 审稿意见

---

### Must-Fix 逐条回应

**[AGREE] R2-N1: Limitations 节格式不符 ARR 要求**

同意这是需要修正的格式问题。我在阅读论文时观察到 Limitations 出现在 Section 7 (Conclusion) 之后、References 之前（Page 5），但未仔细核查编号格式。如果确实是编号子节而非独立无编号节，这属于 ARR desk reject 检查项，必须修正。不过，这是纯格式问题，5 分钟可修复，不应成为内容层面的 reject 理由。

**[AGREE with nuance] R2-N2: 相关工作遗漏**

同意论文的相关工作覆盖不完整，但对优先级排序有不同看法：

- **Lethe (AAAI 2026)**：如果确实是 phase-aware KV pruning 的同期工作，遗漏是严重的——需要在 §2 明确讨论与本文的区别。**同意极高优先级。**
- **R-KV (NeurIPS 2025) 和 "Hold Onto That Thought" (NeurIPS 2025)**：推理模型 KV 压缩的直接相关工作，应当引用。**同意极高优先级。**
- **Scissorhands、FastGen、StreamingLLM**：作为 KV eviction 的 foundational works 应被引用，但这些是基础方法论参考，遗漏对论文 claims 的成立不构成直接威胁。**同意高优先级，但不认为构成 critical 问题。**
- **SparseGPT、Wanda、MInference**：相关性更弱。SparseGPT/Wanda 是权重稀疏化（论文研究的是 attention head pruning + KV eviction，不是权重剪枝）。MInference 关注推理加速而非压缩交互。**降级为 nice-to-have。**
- **LLM-Pruner (NeurIPS 2023)**：论文研究的是 structured pruning 在 compound setting 下的交互，LLM-Pruner 作为 coupled pruning 的开创工作确实应该引用。**同意高优先级。**

总结：核心遗漏（Lethe、R-KV、Hold Onto That Thought）确实严重，应在 §2 增加一个专门的 "Reasoning-Aware Compression" 段落讨论。但 R2 列出的 11 篇中，约有 3-4 篇与论文的具体研究问题（compound sparsity 交互）的关联较弱。

**[REBUT] R2-N3: 贡献深度不足，"纯分析无方法"**

不完全同意。我的反驳理由：

1. **实证分析论文在 *CL 顶会有先例**。论文自己引用的 "Are Sixteen Heads Really Better than One?"（Michel et al., NeurIPS 2019）和 "Analyzing Multi-Head Self-Attention"（Voita et al., ACL 2019）都是纯分析论文，均被接收。关键不在于是否提出新方法，而在于分析的深度和影响力。
2. **论文的发现如果可靠，对现有方法有直接指导意义**：Strategy crossover（§5.3）意味着 uniform budget 策略不是最优的；phase-dependent severity 意味着现有的 static compression 方案在 reasoning model 上可能失效。这些不需要论文自己提出新方法也能产生价值。
3. **然而**，我同意 R2 的隐含批评——论文目前的分析深度不足以弥补"无方法"的缺陷。如果 n=50、同架构这些实验局限被修复，纯分析的贡献可以成立；但以当前实验规模，分析的可靠性不够，"纯分析"就显得更薄。

结论：贡献形式（纯分析）本身不是问题，实验规模不足才是。如果扩展到 500 题 + 跨架构验证，Findings 接收是合理的；main conference 取决于 severity gradient 的 magnitude 和 robustness。

**[AGREE] R2-N4: 实验规模和多样性不足**

完全同意。这与我的 N1（n=50）和 N3（同架构）一致。

**R2 提出了一个我遗漏的重要问题：仅用 PPL 作为质量指标，缺少 accuracy。** 这是一个严重的方法论缺陷，我的 Round 1 报告未充分强调：

- MATH-500 的标准评估指标是 accuracy（答案正确/错误），不是 perplexity。
- PPL 恶化不等于答案错误。一个 269× severity gradient in PPL 如果不对应 accuracy 的 phase-dependent 差异，其实际意义就大打折扣。
- 反过来，如果 accuracy 也展现 phase-dependent compound degradation，论文的 claims 会大幅增强。
- 论文完全没有报告 accuracy，也没有讨论 PPL 与 accuracy 的关系。这是一个应被升级为 **[critical]** 的遗漏。

我将此追加为我的审稿补充意见。

---

### Should-Fix 逐条回应

**[AGREE] R2-W1: Entropy-discrimination collapse 因果证据不足**

完全同意。这与我的 N4 一致（Table 6 仅相关性，缺 intervention）。

**[AGREE] R2-W2: Bibliography 管理混乱**

同意。我在小问题中也指出了 7 条 orphan entries 和 h2o-neurips2023 缺 title。

**[AGREE with caveat] R2-W3: Abstract 过长（600+ 词）**

同意 abstract 偏长，但需要核实具体词数。ACL 模板对 abstract 长度没有硬性字数限制（不同于某些 venue 的 150 词限制），ARR CFP 也未明确要求字数上限。600 词确实超出惯例（多数 *CL 论文 abstract 为 150-300 词），但这是 style 问题而非 compliance 问题。建议压缩但不构成 reject 理由。

**[AGREE] R2-W4: Footnote 2 泄露硬件信息的去匿名化风险**

同意存在风险。"4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB" 是 2025-2026 年的新硬件，4 卡配置相对少见。虽然单凭硬件不一定能唯一确定实验室，但这违背了 double-blind 精神。建议改为泛化描述（如 "4× high-end datacenter GPUs with 96 GB memory each"）。

我补充一点：这也是我在小问题列表中提到的——不同位置出现了不同的 GPU 型号（RTX PRO 4000/6000/8000），这可能是编辑过程中的不一致，也加重了去匿名化问题（多个型号暗示作者在多次修改中使用了不同硬件描述）。

**[AGREE] R2-W5: "Severity gradient" 术语过载**

同意。"Severity gradient" 同时指 G 指标（Eq. 2 的比值）和概念（severity 随 phase 变化的现象），增加了理解成本。建议用不同术语区分（如 "severity ratio" for G, "severity gradient" for the phenomenon）。

**[AGREE] R2-W6: Appendix 文本重复**

同意。我在 W6 中也指出了 Appendix I/J/K 的段落重复问题。

**[AGREE] R2-W7: 方程编号可能不连续**

未仔细核查，但如果确实存在，应修正。

---

### Missing References 回应

| R2 优先级 | 论文 | 我的判断 | 理由 |
|-----------|------|----------|------|
| 极高 | Lethe | **[AGREE]** | 如果是 phase-aware KV pruning 同期工作，必须讨论 |
| 极高 | R-KV | **[AGREE]** | 推理模型 KV 压缩最强 baseline，必须对比 |
| 极高 | Hold Onto That Thought | **[AGREE]** | 唯一系统评估推理任务 KV 压缩，高度相关 |
| 高 | Scissorhands | **[AGREE]** | KV eviction 基础方法，应引用 |
| 高 | FastGen | **[AGREE]** | Per-head adaptive KV cache，与 compound 设定相关 |
| 高 | StreamingLLM | **[AGREE]** | Attention sink 是 KV cache 领域基础，应引用 |
| 高 | LLM-Pruner | **[AGREE]** | Structured pruning 开创工作 |
| 高 | Titanus | **[REBUT]** | GLSVLSI 是硬件/系统 venue，与本文的 NLP 分析视角关联较弱 |
| 中 | SparseGPT | **[REBUT]** | 权重稀疏化，非本文研究的 attention/KV 稀疏化 |
| 中 | Wanda | **[REBUT]** | 同上，权重剪枝与 head pruning + KV eviction 是不同的压缩轴 |
| 中 | MInference | **[AGREE weakly]** | 注意力稀疏模式分析有间接相关性，但非必须 |

---

### R2 Questions for Authors 回应

**Q1 (为什么不报告 accuracy)**：**[AGREE — 升级为 critical]**。这是我 Round 1 遗漏的重要问题。MATH-500 的标准评估是 accuracy，PPL 作为 sole metric 无法说明 compound sparsity 对实际任务表现的影响。建议作者补充 accuracy 分析。

**Q2 (与 Lethe 的区别)**：同意需要讨论。

**Q3 (LLaMA-3/Mistral 验证)**：与我的 N3 一致，同意。

**Q4 (Intervention 实验)**：与我的 N4 一致，同意。

**Q5 (Appendix B/D 重复)**：与我和 R2 的 W6 一致，同意。

---

### 与 R2 评分的分歧总结

| 维度 | R1 | R2 | 分歧原因 |
|------|----|----|----------|
| Soundness | 2.5 | 3.0 | 我更重视 G 指标的近零分母问题和 n=50 的功效不足，认为这些直接威胁核心 claims |
| Excitement | 3.0 | 2.0 | 我认为 "纯分析无方法" 不自动降低 excitement——实证发现本身有价值（类似 Michel et al. 2019）。R2 的标准偏向"要有新方法"，我认为这对分析型论文不完全适用 |
| Overall | 2.5 | 2.5 | 一致 |
| Reproducibility | 3.0 | 3.5 | 我对 50 题 subset 选取的不透明和代码未公开更担忧 |

**最重要的新发现（来自 R2）**：缺少 accuracy 指标。这是方法论上的显著缺陷，PPL-only 评估无法支撑论文关于 "实际部署影响" 的 claims。我将此追加为自己审稿的补充 critical issue。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-14T13:23:09.208657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
  "offset": "225",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
    "offset": "225",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-14T13:23:09.259306+00:00_

225	        assigned_to: "author"
226	        status: open
227	    resolution: ""
228	    resolution_round: null
229	
230	  - id: "R2-W1"
231	    summary: "Abstract 过长/信息过载（~600 词，应精简至 150-250 词）"
232	    category: writing
233	    severity: warning
234	    status: open
235	    first_raised_round: 1
236	    last_seen_round: 1
237	    mentions:
238	      - round: 1
239	        reviewers: [2]
240	        note: "R2-W4 + initial R2-W3：Abstract 塞入过多数字，可读性差。"
241	    action_items:
242	      - round: 1
243	        action: "精简 Abstract 至 150-200 词，保留 1-2 个关键定量结果"
244	        assigned_to: "author"
245	        status: open
246	    resolution: ""
247	    resolution_round: null
248	
249	  - id: "R1-W4"
250	    summary: "多重比较校正不充分（仅 Bonferroni on 4 levels，未覆盖全部检验）"
251	    category: method
252	    severity: warning
253	    status: open
254	    first_raised_round: 1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-14T13:23:22.193735+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "缺少 task accuracy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "缺少 task accuracy",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-14T13:23:22.244480+00:00_

212:    summary: "缺少 task accuracy 评估（仅 PPL）"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-14T13:23:25.126818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
  "offset": "210",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
    "offset": "210",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-14T13:23:25.177500+00:00_

210	
211	  - id: "R1-W3"
212	    summary: "缺少 task accuracy 评估（仅 PPL）"
213	    category: experiment
214	    severity: warning
215	    status: open
216	    first_raised_round: 1
217	    last_seen_round: 1
218	    mentions:
219	      - round: 1
220	        reviewers: [1, 2]
221	        note: "R1-W6(initial) + R2 Q1：仅用 PPL 作质量指标，PPL 恶化不等于答案错误。需报告 MATH-500 solve rate。"
222	    action_items:
223	      - round: 1
224	        action: "报告各条件下 MATH-500 accuracy（solve rate）"
225	        assigned_to: "author"
226	        status: open
227	    resolution: ""
228	    resolution_round: null
229	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-14T13:23:34.736587+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
  "old_string": "  - id: \"R1-W3\"\n    summary: \"缺少 task accuracy 评估（仅 PPL）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W6(initial) + R2 Q1：仅用 PPL 作质量指标，PPL 恶化不等于答案错误。需报告 MATH-500 solve rate。\"\n    action_items:\n      - round: 1\n        action: \"报告各条件下 MATH-500 accuracy（solve rate）\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null",
  "new_string": "  - id: \"R1-W3\"\n    summary: \"缺少 task accuracy 评估（仅 PPL）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W6(initial) + R2 Q1：仅用 PPL 作质量指标，PPL 恶化不等于答案错误。需报告 MATH-500 solve rate。\"\n      - round: 1\n        reviewers: [1]\n        note: \"R1 交叉回应中将此升级为 critical：MATH-500 标准评估是 accuracy，PPL-only 评估无法支撑论文关于实际部署影响的 claims。如果 269× severity gradient in PPL 不对应 accuracy 的 phase-dependent 差异，实际意义大打折扣。\"\n    action_items:\n      - round: 1\n        action: \"报告各条件下 MATH-500 accuracy（solve rate）\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
    "old_string": "  - id: \"R1-W3\"\n    summary: \"缺少 task accuracy 评估（仅 PPL）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W6(initial) + R2 Q1：仅用 PPL 作质量指标，PPL 恶化不等于答案错误。需报告 MATH-500 solve rate。\"\n    action_items:\n      - round: 1\n        action: \"报告各条件下 MATH-500 accuracy（solve rate）\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null",
    "new_string": "  - id: \"R1-W3\"\n    summary: \"缺少 task accuracy 评估（仅 PPL）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W6(initial) + R2 Q1：仅用 PPL 作质量指标，PPL 恶化不等于答案错误。需报告 MATH-500 solve rate。\"\n      - round: 1\n        reviewers: [1]\n        note: \"R1 交叉回应中将此升级为 critical：MATH-500 标准评估是 accuracy，PPL-only 评估无法支撑论文关于实际部署影响的 claims。如果 269× severity gradient in PPL 不对应 accuracy 的 phase-dependent 差异，实际意义大打折扣。\"\n    action_items:\n      - round: 1\n        action: \"报告各条件下 MATH-500 accuracy（solve rate）\"\n        assigned_to: \"author\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-14T13:23:34.737481+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 142 · 2026-05-14T13:23:46.022122+00:00_

Issue Tracker 已更新：R1-W3（缺少 accuracy 评估）从 `warning` 升级为 `critical`。

**Round 1 审稿圆桌会议总结**：

- **R1**: 10 AGREE / 1 AGREE with nuance / 1 REBUT（反驳"纯分析不足"——认为实证分析论文有先例，核心问题是实验规模而非贡献形式）
- **R2**: 10 AGREE / 1 PARTIAL AGREE / 1 REBUT（反驳 phase segmentation confounding——random eviction control 有效缓解）
- **共识**：G 指标不可靠、样本量不足、同架构泛化过度、discrimination collapse 非因果、相关工作遗漏、缺少 accuracy
- **分歧**：贡献深度要求（R1 较宽容）、phase confounding（R2 认为 random control 已充分缓解）
- **最终评分**：两位 Reviewer 均 2.5/5，**Weak Reject**

审稿报告已投递 Research Director。圆桌会议完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 143 · 2026-05-14T13:23:48.625773+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：
- **与 R2 一致的**：实验规模不足 (N4)、bibliography 问题 (W2)、discrimination collapse 缺因果证据 (W1)、去匿名化风险 (W4)、文本重复 (W6)、大部分 missing references
- **与 R2 分歧的**：不同意 "纯分析无方法即不足" (N3) — 实证分析论文在 *CL 有先例（Michel 2019, Voita 2019），关键是分析深度而非是否提出新方法；Soundness 我给更低分（2.5 vs 3），因为 G 指标的近零分母问题是核心方法学缺陷
- **来自 R2 的重要新发现**：论文仅用 PPL 评估而缺少 MATH-500 accuracy，这是我 Round 1 遗漏的 critical issue，已追加

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 144 · 2026-05-14T13:24:08.466485+00:00_

审稿流程已全部完成。

**最终状态汇总**：

| 步骤 | 状态 |
|------|------|
| Round 1 独立审稿 | R1 ✓ R2 ✓ |
| 交叉分享 | R1→R2 ✓ R2→R1 ✓ |
| 交叉回应 | R1 ✓（10 AGREE, 1 REBUT on 贡献形式, 升级 accuracy 为 critical） R2 ✓（10 AGREE, 1 PARTIAL AGREE, 1 REBUT on confounding） |
| 收敛判断 | 达成共识，Overall 均 2.5/5 |
| Issue Tracker | 10 critical + 10 warning/info，已更新 |
| 审稿报告 | 已投递 Research Director（Weak Reject 2.5/5） |

**两位 Reviewer 唯一实质分歧**：贡献形式——R2 认为纯观察无方法是 critical 缺陷，R1 认为实证分析论文有先例（Michel 2019, Voita 2019），问题在实验规模而非贡献形式。此分歧已记录在报告 Reviewer Divergence D1 中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 11

## Round 11

82 recorded events


### User

_source line 145 · 2026-05-15T07:34:55.216655+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: phase-gated-compound-sparse
- 论文路径: projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026 ARR
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-15T07:35:01.621115+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-15T07:35:01.725354+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-15T07:35:05.393491+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-15T07:35:05.393958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-15T07:35:10.574302+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-15T07:35:11.228165+00:00_

{"result":"# 项目 phase-gated-compound-sparse 概况\n\n## 实验状态 (83 个)\n\n- **mvp_v4_legacy_s025**: DONE (failed) — \n- **mvp_v4_random_r2**: DONE (success) — \n- **mvp_v4_legacy_s01**: DONE (negative) — \n- **mvp_v4_legacy_s03**: DONE (success) — \n- **mvp_v4_legacy_s02**: DONE (success) — \n- **mvp_v4c_r2**: DONE (failed) — \n- **mvp_v4b_r2**: DONE (failed) — \n- **mvp_v4a_r2**: DONE (failed) — \n- **mvp_ii_profiling_v4-random**: DONE (failed) — \n- **mvp_ii_profiling_v4c**: DONE (failed) — \n- **mvp_ii_profiling_v4b**: DONE (failed) — \n- **mvp_ii_profiling_v4**: DONE (failed) — \n- **mvp_ii_profiling_v3**: DONE (negative) — \n- **mvp_ii_profiling_v2**: DONE (negative) — \n- **mvp_interaction_index_profiling**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-15T05:26:54Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 83 个实验 — ANALYZING 1, DONE 81, RUNNING 1\n**DONE 分布**: failed 14, killed 21, negative 10, success 36\n\n### GPU 占用\n- **分配**: 4 张 — westd-22162:cuda:0, westd-22162:cuda:1, westd-22162:cuda:2, westd-22162:cuda:3\n- **实际运行**: 2 张 — westd-22162:cuda:0(c2_n500_deepseek), westd-22162:cuda:1(c2_n500_deepseek)\n- **空闲（分配了没跑）**: westd-22162:cuda:2, westd-22162:cuda:3\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `c2_n500_deepseek` | westd-22162 | cuda:0,cuda:1 | ? | `—` |\n\n### 📌 最近完成 (top 5)\n- `c2_qw_n500` [failed] — 2026-05-14T19:26:11 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `c5b_pilot` [negative] — 2026-05-14T19:10:56 — oracle recovery 18% < 30% gate; heuristic 32% CI crosses zero. Scientific gate_f\n- `c3_llama` [success] — 2026-05-14T17:58:54\n- `c2_ds_n500` [killed] — 2026-05-14T15:37:18\n- `c3_llama_arch` [killed] — 2026-05-14T15:37:16\n\n### 🔴 最近失败原因 (top 3)\n- `c2_qw_n500`: process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `c2_ds_n500`: _(no failure_reason — pre-2026-04-24 ent
…[truncated 1819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-15T07:35:11.228620+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "report.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-15T07:35:13.239004+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-15T05:26:54Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 83 个实验 — ANALYZING 1, DONE 81, RUNNING 1\\n**DONE 分布**: failed 14, killed 21, negative 10, success 36\\n\\n### GPU 占用\\n- **分配**: 4 张 — westd-22162:cuda:0, westd-22162:cuda:1, westd-22162:cuda:2, westd-22162:cuda:3\\n- **实际运行**: 2 张 — westd-22162:cuda:0(c2_n500_deepseek), westd-22162:cuda:1(c2_n500_deepseek)\\n- **空闲（分配了没跑）**: westd-22162:cuda:2, westd-22162:cuda:3\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `c2_n500_deepseek` | westd-22162 | cuda:0,cuda:1 | ? | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `c2_qw_n500` [failed] — 2026-05-14T19:26:11 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `c5b_pilot` [negative] — 2026-05-14T19:10:56 — oracle recovery 18% < 30% gate; heuristic 32% CI crosses zero. Scientific gate_f\\n- `c3_llama` [success] — 2026-05-14T17:58:54\\n- `c2_ds_n500` [killed] — 2026-05-14T15:37:18\\n- `c3_llama_arch` [killed] — 2026-05-14T15:37:16\\n\\n### 🔴 最近失败原因 (top 3)\\n- `c2_qw_n500`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `c2_ds_n500`: _(no failure_reason — pre-2026-04-24 entry)_\\n- `c3_llama_arch`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| c2_n500_deepseek | C2 statistical power boost: 将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，提升统计功效。预注册：若 QW s015 在 n=500 后 CI 仍跨零，论文叙事改为 \\\"compound effect emerges above a threshold sparsity level (~s020)\\\" | — | — | — |\\n| c2_qw_n500_r3 | C2 Qwen n=500 cont
…[truncated 1444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2010
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-15T07:35:13.239608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-15T07:35:13.691949+00:00_

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\appendix
48	\input{appendix}
49	\input{appendix_moved}
50	\input{appendix_disc_analysis}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-15T07:35:13.792830+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-15T07:35:13.843504+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-15T07:35:21.835243+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
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

_source line 159 · 2026-05-15T07:35:21.885926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-15T07:35:24.788144+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-15T07:35:26.171040+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/artifacts/_project/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/artifacts/_project/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-15T07:35:26.575192+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-15T07:35:26.575651+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 164 · 2026-05-15T07:35:29.244112+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"}]

Based on the search results, I found the EMNLP 2026 ARR submission guidelines and page limits:

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

Additionally, the ARR submission deadline is May 25, 2026, and EMNLP 2026 will use ACL
…[truncated 366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 4455
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-15T07:35:29.244704+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md\", \"content\": \"# 决策记录（非 metrics、非 registry 可查）\\n\\n## D063 Random threshold-based story — 2026-05-15\\n- random s025 在 n=500 下双模型显著（DS p=0.019, QW p<0.001），s015/s020 仍 NS\\n- **论文叙事从 \\\"random 全 FAIL\\\" 改为 threshold-based**：compound effect 在 importance 中显著更强，high sparsity (≥s025) 下 random 也显著但幅度更小\\n- 分析报告中 random 不再标 FAIL/PASS，改报具体数值 + 显著性\\n- s030 random 完成后确认 threshold 在 s020-s025 之间\\n\\n## D064 d_z 降为辅助指标 — 2026-05-15\\n- DS s020→s025 d_z=-0.157 但 median 3.3× 跳跃，根因是单个极端离群值 (ii_low=1524) 膨胀方差\\n- **主指标确认为 Wilcoxon p + median_diff**（对 outlier robust）\\n- d_z 仅作辅助，高 sparsity 条件加注 \\\"受 outlier-driven variance 影响\\\"\\n- 可选增加 rank-biserial correlation 作为 robust alternative\\n- 已派 Worker 修改分析脚本\\n\\n## 统计检验方法选择 — 2026-05-15\\n- **Wilcoxon signed-rank test 保持不变**，不切换 paired permutation test\\n- 理由（Director）：n=500 配对数据下 Wilcoxon 是标准选择\\n\\n## n=500 分析自动触发 — 2026-05-15\\n- 实验完成后（cron 回调）立即跑全量分析，不等 Director 指令\\n- 一键命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 analyze_n500_unified.py --csv --latex`\\n- 分析完成后汇报 Director，由 Director 派 Paper Agent 更新论文\\n\\n## 剂量-反应排列检验 — 2026-05-15\\n- 3 个 sparsity level 只有 6 种排列，理论最小 p≈0.167，无统计效力\\n- 必须等 s030 到齐（4 levels → 24 种排列，最小 p≈0.042）\\n\\n## d_z 报告规则 — 2026-05-14 (D059)\\n- within-importance 对比保留 d_z（如 imp_s015 vs imp_s020）\\n- 涉及 random 的对比只报 Wilcoxon + median_diff，不报 d_z\\n\\n## II 主指标 — 2026-05-14 (D054)\\n- 主指标从 mean 切换为 **median** + median bootstrap CI (B=10000)\\n- 理由：II 分布偏态严重，median 更鲁棒\\n\", \"total_chars\": 1431, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2669
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-15T07:35:33.667935+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines anonymity policy submission format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines anonymity policy submission format requirements"
  }
}
```

</details>

---


### Tool call

_source line 167 · 2026-05-15T07:35:34.070995+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
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

_source line 168 · 2026-05-15T07:35:34.172081+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-15T07:35:39.646902+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines anonymity policy submission format requirements"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the search results, here's a summary of key information about ACL Rolling Review 2026 author guidelines:

## Anonymity Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. However, the new policy incentivizes anonymous
…[truncated 1256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5978
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-15T07:35:44.219800+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the complete submission guidelines for EMNLP 2026 main conference papers: page limits (long/short), formatting requirements, template, anonymity rules, appendix rules, citation format, mandatory sections (e.g. Limitations, Ethics), ARR deadline, and any other submission requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract the complete submission guidelines for EMNLP 2026 main conference papers: page limits (long/short), formatting requirements, template, anonymity rules, appendix rules, citation format, mandatory sections (e.g. Limitations, Ethics), ARR deadline, and any other submission requirements."
  }
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-15T07:35:44.789899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-15T07:35:48.408509+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\widetilde{\Delta} = \placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho 
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 3618
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-15T07:35:48.810630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-15T07:35:48.811072+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 1862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-15T07:35:49.162785+00:00_

# EMNLP 2026 Main Conference Submission Guidelines

## Page Limits
- **Long papers:** 8 pages (final versions may have up to 9 pages)
- **Short papers:** 4 pages (final versions may have up to 5 pages)

## Key Submission Requirements

**Anonymity:** The review process is double-blind. Per ACL policy, "there is no anonymity period requirement."

**Mandatory Sections & Policies:**
- Limitations section required
- Ethics checklist (ARR's responsible NLP research checklist)
- Publication Ethics Policy compliance
- Disclosure Policy adherence
- Writing assistance is permitted; however, entirely AI-generated papers are prohibited

**Formatting & Templates:** Authors must "follow all of the ARR submission requirements" regarding formatting and templates, available through the ACL Rolling Review platform.

**Appendices & Supplementary Materials:** Optional supplementary materials, appendices, software, and data are permitted per ARR guidelines.

**Citations:** Standard academic citation practices apply; hallucinated citations violate integrity policies.

## Critical Deadlines

- **ARR submission:** May 25, 2026
- **Reviewer registration:** May 27, 2026
- **EMNLP commitment:** August 2, 2026

## Additional Requirements

- Double anonymized review instructions must be followed
- Multiple submissions prohibited
- All accepted papers require presentation (in-person or virtual)
- At least one presenting author must register by the early registration deadline

*All deadlines are UTC-12:00 ("anywhere on Earth")*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebFetch",
  "elapsed_ms": 4942
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-15T07:35:49.414564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-15T07:35:49.616070+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All reported confidence intervals and significance t
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-15T07:35:55.947255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-15T07:35:55.948061+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{
…[truncated 8932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-15T07:35:56.048847+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-15T07:35:56.049384+00:00_

1	\section{Analysis: Entropy-Discrimination Collapse}
2	\label{sec:analysis}
3	
4	We propose \emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	Beyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\Delta\mathcal{H} \in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \leq 0.20$ but reverses at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-15T07:35:56.099957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-15T07:35:56.100357+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
11	
12	\paragraph{KV cache eviction.}
13	Most methods rely on importance scoring whose reliability is increasingly questioned.
14	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
15	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
16	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
17	\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.
18	Lethe~\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.
19	These me
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-15T07:35:56.100615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-15T07:35:56.301694+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \placeholder{ORACLE\_PCT}\% (Wilcoxon $p = \placeholder{ORACLE\_P}$), below t
…[truncated 1685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-15T07:35:56.302326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-15T07:35:56.755660+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-15T07:35:56.806594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-15T07:35:57.259520+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
6	
7	\paragraph{Mechanism.}
8	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
9	
10	\paragraph{Sparsity range.}
11	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:lim
…[truncated 14 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-15T07:35:57.260258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-15T07:35:57.311032+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-15T07:36:02.819670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-15T07:36:03.171959+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-15T07:36:03.172398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-15T07:36:04.127772+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in trai
…[truncated 12246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-15T07:36:04.128442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-15T07:36:04.179161+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	
13	\paragraph{Random masking as falsification control.}
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\widetilde{\Delta} = \placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy sh
…[truncated 6847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-15T07:36:04.581705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-15T07:36:04.632664+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{decision-repr-transition-2026,
13	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
14	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
15	    journal = {arXiv preprint arXiv:2605.07271},
16	    year    = {2026},
17	    url     = {https://arxiv.org/abs/2605.07271},
18	}
19	
20	@article{deepseek-r1-2025,
21	    title   = {{DeepSeek-R1} incentivizes reasoning in {LLMs} through reinforcement learning},
22	    author  = {{DeepSeek-AI}},
23	    journal = {Nature},
24	    volume  = {645},
25	    pages   = {633--638},
26	    year    = {2025},
27	    doi     = {10.1038/s41586-025-09422-z},
28	}
29	
30	@inproceedings{defensivekv-iclr2026,
31	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
32	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
33	    booktitle = {International Conference on Learning Representations},
34	    year      = {2026},
35	    url       = {https://arxiv.org/abs/2510.13334},
36	}
37	
38	@article{doing-more-with-less-2026,
39	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
40	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
41	    journal = {arXiv preprint arXiv:2604.25098},
42	    year    = {2026},
43	    url     = {https://arxiv
…[truncated 2955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-15T07:36:14.680142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-15T07:36:14.680802+00:00_

100	
101	@inproceedings{math500-neurips2021,
102	    title     = {Measuring Mathematical Problem Solving With the {MATH} Dataset},
103	    author    = {Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob},
104	    booktitle = {Advances in Neural Information Processing Systems},
105	    year      = {2021},
106	    url       = {https://arxiv.org/abs/2103.03874},
107	}
108	
109	@inproceedings{michel-neurips2019,
110	    title     = {Are Sixteen Heads Really Better than One?},
111	    author    = {Michel, Paul and Levy, Omer and Neubig, Graham},
112	    booktitle = {Advances in Neural Information Processing Systems},
113	    year      = {2019},
114	    url       = {https://arxiv.org/abs/1905.10650},
115	}
116	
117	@inproceedings{nacl-acl2024,
118	    title     = {{NACL}: A General and Effective {KV} Cache Eviction Framework for {LLMs} at Inference Time},
119	    author    = {Chen, Yilong and Wang, Guoxia and Shang, Junyuan and Cui, Shiyao and Zhang, Zhenyu and Liu, Tingwen and Wang, Shuohuan and Sun, Yu and Yu, Dianhai and Wu, Hua},
120	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
121	    year      = {2024},
122	    url       = {https://arxiv.org/abs/2408.03675},
123	}
124	
125	@article{phase-transition-compression-2026,
126	    title   = {Phase transitions in large language model compression},
127	    author  = {Ma, Ziyang and Li, Zuchao and Zhang, Lefei and Xia, Gui-Song and Du, Bo and Zhang, Liangpei and Tao, Dacheng},
128	    journal = {npj Artificial Intelligence},
129	    volume  = {2},
130	    number  = {21},
131	    year    = {2026},
132	    url     = {https://www.nature.com/articles/s44387-026-00072-8},
133	}
134	
135	@article{physics-kvcache-2026,
136	    title   = {Understanding the Physics of Key-Value Cache Compression for {LLMs} through Attention Dynamics},
137	    author  = {Ananthanarayanan, Samhruth and S
…[truncated 5590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-15T07:36:15.737564+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-15T07:36:15.840019+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-15T07:36:18.624219+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-15T07:36:18.675463+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-15T07:36:21.639293+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-15T07:36:21.691907+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-15T07:36:24.354652+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/",
  "description": "List project directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/",
    "description": "List project directory structure"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-15T07:36:24.556236+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.yaml
literature_map.yaml
logs
memory.md
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-15T07:36:27.642653+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/",
  "description": "List docs directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/",
    "description": "List docs directory"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-15T07:36:27.744499+00:00_

IDEA_BRIEF.md
paper
results

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-15T07:36:31.689748+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" | head -20",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" | head -20",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-15T07:36:32.092319+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_paper_trim_results_tex_20260514T114501_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_code_m1v2-analysis-prep_20260513T210243_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_writing_related-work-snapkv-nacl_20260514T055834_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_analysis_qwen-imp-registry-update_20260514T075546_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_research_negative-lit-search_20260513T212407_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_monitor_progress_check_20260514T204145_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_ssh_r2-r3-conflict-check_20260514T054114_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_paper_results-cohens-d_20260514T080529_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_infra_model-final-verify_20260513T191425_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c5b_framing_proposal_20260514T184055_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_infra_importance-vs-random_20260513T222105_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_ops_progress-check
…[truncated 1163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-15T07:36:32.143183+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project_config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-15T07:36:32.194146+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-15T07:36:35.208957+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11 -maxdepth 2 -name \"*.yaml\" -not -path \"*/projects/*\" -not -path \"*/logs/*\" | head -20",
  "description": "Find config files outside projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11 -maxdepth 2 -name \"*.yaml\" -not -path \"*/projects/*\" -not -path \"*/logs/*\" | head -20",
    "description": "Find config files outside projects"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-15T07:36:35.259746+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-15T07:36:37.974556+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/workspace.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/workspace.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-15T07:36:38.075574+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-15T07:36:41.240709+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/ 2>/dev/null | head -10",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/ 2>/dev/null | head -10",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-15T07:36:41.291419+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-15T07:37:24.638015+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 ARR (main conference)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 2-column, 长文 8 页正文 + 不限附录, double-blind\n- **必需 section**: Limitations\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n\n### 你的审查侧重：方法严谨性\n请重点评估以下方面：\n\n1. **实验设计**\n   - 50 个 MATH-500 问题的样本量是否充分？是否存在 selection bias？\n   - 4 个 sparsity levels (0.15–0.30) 是否覆盖了有意义的操作范围？\n   - 仅使用一个 benchmark (MATH-500) 对结论的泛化性有何影响？\n   - compound sparsity 的实现是否合理（同步对称稀疏率）？\n   - Phase segmentation（tercile-based）的选择是否充分论证？\n\n2. **统计分析**\n   - 非参数方法的选择（Wilcoxon, bootstrap, permutation test）是否恰当？\n   - Bonferroni 校正是否充分考虑了多重比较问题？\n   - Cohen's d_z 的报告和解读是否正确？\n   - 置信区间的构造和报告是否规范？\n   - 右偏分布下 median 的选择是否充分论证？\n\n3. **跨模型/跨架构证据强度**\n   - DeepSeek vs Qwen (同架构) 的复现结果差异（~1/5 magnitude）如何解读？\n   - LLaMA 跨架构结果极弱（~1/40 magnitude, 混合统计证据），论文是否过度声称？\n   - 文中 \"partially confirms\" 等表述是否匹配实际数据？\n\n4. **机制分析**\n   - entropy-discrimination collapse 的证据是否充分？correlational vs causal？\n   - Gini coefficient 下降是否真正支持 \"discrimination collapse\"？\n   - 熵重分布在 Qwen s=0.25 的反转如何影响机制的通用性？\n\n5. **数据完整性**\n   - 注意论文中存在多处 `\\placeholder{}` 未填充数据——列出所有位置\n   - 各表格数据是否自洽（cross-check 不同 section 引用的相同数据）\n\n6. **可复现性**\n   - 实验细节是否足够复现？随机种子、硬件、超参数？\n   - 代码/数据是否提及开源计划？\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses → Questions → Minor Issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 ARR (main conference)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 2-column, 长文 8 页正文 + 不限附录, double-blind\n- **必需 section**: Limitations\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n\n### 你的审查侧重：方法严谨性\n请重点评估以下方面：\n\n1. **实验设计**\n   - 50 个 MATH-500 问题的样本量是否充分？是否存在 selection bias？\n   - 4 个 sparsity levels (0.15–0.30) 是否覆盖了有意义的操作范围？\n   - 仅使用一个 benchmark (MATH-500) 对结论的泛化性有何影响？\n   - compound sparsity 的实现是否合理（同步对称稀疏率）？\n   - Phase segmentation（tercile-based）的选择是否充分论证？\n\n2. **统计分析**\n   - 非参数方法的选择（Wilcoxon, bootstrap, permutation test）是否恰当？\n   - Bonferroni 校正是否充分考虑了多重比较问题？\n   - Cohen's d_z 的报告和解读是否正确？\n   - 置信区间的构造和报告是否规范？\n   - 右偏分布下 median 的选择是否充分论证？\n\n3. **跨模型/跨架构证据强度**\n   - DeepSeek vs Qwen (同架构) 的复现结果差异（~1/5 magnitude）如何解读？\n   - LLaMA 跨架构结果极弱（~1/40 magnitude, 混合统计证据），论文是否过度声称？\n   - 文中 \"partially confirms\" 等表述是否匹配实际数据？\n\n4. **机制分析**\n   - entropy-discrimination collapse 的证据是否充分？correlational vs causal？\n   - Gini coefficient 下降是否真正支持 \"discrimination collapse\"？\n   - 熵重分布在 Qwen s=0.25 的反转如何影响机制的通用性？\n\n5. **数据完整性**\n   - 注意论文中存在多处 `\\placeholder{}` 未填充数据——列出所有位置\n   - 各表格数据是否自洽（cross-check 不同 section 引用的相同数据）\n\n6. **可复现性**\n   - 实验细节是否足够复现？随机种子、硬件、超参数？\n   - 代码/数据是否提及开源计划？\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses → Questions → Minor Issues"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-15T07:37:40.629944+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15991
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-15T07:37:41.132251+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 ARR (main conference)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 2-column, 长文 8 页正文 + 不限附录, double-blind\n- **必需 section**: Limitations\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n\n### 你的审查侧重：新颖性/完整性\n请重点评估以下方面：\n\n1. **贡献新颖度**\n   - \"compound sparsity severity is phase-modulated\" 这个 claim 的新颖性如何？\n   - 与已有工作的区分度：ThinKV (phase-aware KV), SparK (compound sparsity), DefensiveKV (fragility) 等是否已经（部分）包含了类似发现？\n   - \"entropy-discrimination collapse\" 作为机制解释的原创性——是否仅是已知现象的重新包装（HIES 2025 已报告 head discrimination collapse under heavy pruning）？\n   - 贡献定位为\"empirical finding\"而非\"method\"——在 EMNLP main conference 中是否有足够影响力？\n\n2. **Related Work 覆盖**\n   - 是否遗漏了重要的相关工作？特别是：\n     - 其他 compound compression 工作（量化+剪枝、蒸馏+剪枝）\n     - phase-aware inference 的更多先驱工作\n     - 其他 KV cache eviction robustness 分析\n   - 引用是否真实？检查所有 2025-2026 年的引用是否存在幻觉引用\n   - 引用格式是否符合 ACL 规范（natbib）？\n\n3. **写作质量**\n   - 论文结构是否清晰？信息流是否流畅？\n   - Abstract 是否准确反映了论文内容和结论的强度？\n   - 是否存在过度声称（overclaim）？特别是关于 cross-architecture generalization 的措辞\n   - Discussion section 是否充分讨论了 limitations 和 implications？\n   - `\\placeholder{}` 未填充问题——列出所有位置并评估影响\n\n4. **格式合规**\n   - 是否符合 ACL double-blind 匿名要求？检查是否有 self-revealing references\n   - 页数是否在 8 页限制内？\n   - Limitations section 是否存在且充分？\n   - 图表是否清晰、标注完整？\n   - 附录中的 \"REVIEWER-ATTACK\" / \"REBUTTAL\" 注释（LaTeX comments）是否应在提交前删除？\n\n5. **整体影响力**\n   - 这篇论文对 NLP/ML 社区的实际价值？\n   - 谁会引用这篇论文？它改变了什么实践？\n   - 对 EMNLP 读者而言，主要 takeaway 是什么？\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses → Questions → Minor Issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 ARR (main conference)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 2-column, 长文 8 页正文 + 不限附录, double-blind\n- **必需 section**: Limitations\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n\n### 你的审查侧重：新颖性/完整性\n请重点评估以下方面：\n\n1. **贡献新颖度**\n   - \"compound sparsity severity is phase-modulated\" 这个 claim 的新颖性如何？\n   - 与已有工作的区分度：ThinKV (phase-aware KV), SparK (compound sparsity), DefensiveKV (fragility) 等是否已经（部分）包含了类似发现？\n   - \"entropy-discrimination collapse\" 作为机制解释的原创性——是否仅是已知现象的重新包装（HIES 2025 已报告 head discrimination collapse under heavy pruning）？\n   - 贡献定位为\"empirical finding\"而非\"method\"——在 EMNLP main conference 中是否有足够影响力？\n\n2. **Related Work 覆盖**\n   - 是否遗漏了重要的相关工作？特别是：\n     - 其他 compound compression 工作（量化+剪枝、蒸馏+剪枝）\n     - phase-aware inference 的更多先驱工作\n     - 其他 KV cache eviction robustness 分析\n   - 引用是否真实？检查所有 2025-2026 年的引用是否存在幻觉引用\n   - 引用格式是否符合 ACL 规范（natbib）？\n\n3. **写作质量**\n   - 论文结构是否清晰？信息流是否流畅？\n   - Abstract 是否准确反映了论文内容和结论的强度？\n   - 是否存在过度声称（overclaim）？特别是关于 cross-architecture generalization 的措辞\n   - Discussion section 是否充分讨论了 limitations 和 implications？\n   - `\\placeholder{}` 未填充问题——列出所有位置并评估影响\n\n4. **格式合规**\n   - 是否符合 ACL double-blind 匿名要求？检查是否有 self-revealing references\n   - 页数是否在 8 页限制内？\n   - Limitations section 是否存在且充分？\n   - 图表是否清晰、标注完整？\n   - 附录中的 \"REVIEWER-ATTACK\" / \"REBUTTAL\" 注释（LaTeX comments）是否应在提交前删除？\n\n5. **整体影响力**\n   - 这篇论文对 NLP/ML 社区的实际价值？\n   - 谁会引用这篇论文？它改变了什么实践？\n   - 对 EMNLP 读者而言，主要 takeaway 是什么？\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses → Questions → Minor Issues"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-15T07:37:43.000780+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1868
}
```

</details>

---


### Assistant

_source line 226 · 2026-05-15T07:37:51.267093+00:00_

Round 1 审稿任务已分配：
- **Reviewer 1**（方法严谨性）：实验设计、统计分析、跨模型证据、机制分析、数据完整性
- **Reviewer 2**（新颖性/完整性）：贡献新颖度、related work 覆盖、写作质量、格式合规、影响力

等待两位 Reviewer 提交独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 227 · 2026-05-15T07:42:15.622736+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见（新颖性/完整性）

---

## 总体评分

**Overall**: 2.5 / 5（Resubmit next cycle ↔ Findings 之间）
**一句话总结**: 论文提出了一个有价值的 empirical finding（compound sparsity severity 的 phase modulation），统计方法扎实，但论文严重未完成（30+ placeholders 未填充，核心 Table 4 完全空白），新颖性相对于已有工作增量有限，且唯一的 cross-architecture 证据很弱。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.0 / 5 | 主实验（DeepSeek Qwen2）统计严谨，但 Table 4（cross-arch）完全由 placeholder 填充，无法验证 LLaMA 结论；30+ placeholders 表明论文远未完成 |
| **Excitement** | 2.5 / 5 | Phase-modulated compound interaction 是有趣的 characterization，但缺乏方法贡献；oracle mitigation 实验未通过自设门槛，实际影响力受限 |
| **Overall** | 2.5 / 5 | 需要大幅修订：填充所有 placeholders、补强 cross-architecture 证据、更清晰地区分于 HIES 等已有工作 |
| **Reproducibility** | 3 / 5 | 报告了模型、数据集、sparsity levels、bootstrap 参数和 GPU 型号；但代码未开源，KV importance 的 position normalization 公式缺乏足够实现细节 |
| **Confidence** | 4 / 5 | 审稿人熟悉 KV cache compression、attention head pruning 和统计方法 |

---

## Summary

本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）在 reasoning model 生成过程中的 phase-dependent severity。核心发现：在 importance-based eviction 下，compound interaction 集中在 low-sparsity reasoning phases，而 random eviction 无此现象。在 DeepSeek-R1-Distill-Qwen-7B 上，severity gradient 从 69× (s=0.15) 增长到 274× (s=0.30)。提出 entropy-discrimination collapse 作为机制解释。在 Qwen2.5-7B-Instruct 上部分复现，在 LlamaForCausalLM 上仅获得微弱的方向性一致证据。

---

## 主要优势

1. **问题定义清晰且有实际意义**：将 compound sparsity 的 phase-invariance assumption 明确地作为攻击目标，对部署 reasoning model 的 practitioners 有直接指导价值。

2. **统计方法论严谨**：使用非参数 bootstrap (B=10,000)、paired permutation tests、Bonferroni correction、Cohen's d_z，并报告中位数而非均值来处理右偏分布（mean/median ratio 高达 43:1）。这在 ML 论文中罕见且值得肯定。

3. **Random eviction 作为 falsification control 设计巧妙**：7/8 conditions 下 random eviction 无显著 phase gradient，有效隔离了 strategy-specific amplification。

4. **Multiplicative null 验证**（Appendix A）增强了 Interaction Index 定义选择的鲁棒性。

5. **Writing 整体结构清晰**：从 Background → Methodology → Results → Analysis → Discussion 的信息流合理，每个 section 内部逻辑连贯。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 论文严重未完成：30+ `\placeholder{}` 未填充
- 具体位置：Abstract (line 8)、Section 5.4 (`NULL_PCT`)、Table 4 全部数据 (Section 5.5, lines 86-98)、Discussion (`ORACLE_PCT`, `ORACLE_P`, `HEUR_PCT`, `HEUR_P`)、Appendix 多处
- 问题：**Table 4（cross-architecture validation）是本文最重要的 generalization 证据，但所有数据格全部为空**。Discussion 中的 oracle phase-aware reallocation 实验——本文唯一尝试从 characterization 走向 actionable mitigation 的部分——四个关键数字全部缺失。Abstract 中也有一个关键统计量未填充。
- 为什么影响接收：Reviewer 无法验证 Section 5.5 和 Discussion 中的任何 claim。论文以当前状态提交将被视为 incomplete submission。
- 建议修改方向：在提交前必须填充所有 placeholder，或如果数据确实不可用则删除相关 claim。

**N2** [critical] Cross-architecture 证据不足以支撑论文标题和 abstract 的 framing
- 具体位置：Section 5.5、Abstract (line 10)、Title ("Reasoning Models" 暗示广泛适用)
- 问题：LLaMA 结果极弱——4 个 sparsity levels 中仅 s=0.30 的 Bonferroni-corrected Wilcoxon 达到显著性 (p=0.029)；绝对 magnitude 仅为 DeepSeek 的 ~1/40；random eviction 在 LLaMA 上也展示了 non-trivial phase gradient（原文 Discussion: "random pruning also exhibits a non-trivial phase gradient"），严重削弱 strategy-specificity claim。然而 Abstract line 10 仍称 "provide mixed but directionally consistent evidence for cross-architecture generalization"，Title 使用复数 "Reasoning Models"。
- 为什么影响接收：Title/abstract 给人的印象是结论在多架构上成立，但实际 LLaMA 证据在统计上大部分不显著，且 strategy contrast 在 LLaMA 上不 clean。这属于 overclaim。
- 建议修改方向：(1) Title 应限定为 Qwen2 架构或明确标注 partial evidence; (2) Abstract 中 LLaMA 部分应更突出 mixed evidence 而非 directional consistency; (3) 考虑将 LLaMA 实验定位为 exploratory supplement 而非 core contribution。

**N3** [critical] 与 HIES (2025) 的区分不充分
- 具体位置：Related Work §2 (line 17)、Analysis §6、Appendix §E
- 问题：HIES (Choi et al., 2025) 已经报告了 "head importance-based discrimination collapses under heavy pruning"。本文的 "entropy-discrimination collapse" 机制与 HIES 的发现高度重叠。论文仅在 Related Work 中一句话提及 HIES ("independently show that importance-based head discrimination collapses under heavy pruning")，未在 Analysis 中讨论两者的区别。HIES 的核心观察——pruning 导致 importance score 区分度下降——与本文 Section 6 的 Gini coefficient 下降分析本质相同。
- 为什么影响接收：这是新颖性的核心问题。如果 discrimination collapse 已被 HIES 发现，本文的 mechanistic contribution 需要更清晰地说明增量在哪里（phase-dependence? compound interaction context? quantitative characterization?）。
- 建议修改方向：在 Analysis 中专门段落对比 HIES 的 single-axis discrimination collapse 与本文的 compound + phase-dependent collapse，明确本文在 mechanism 层面的 delta。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 贡献定位为 empirical finding——对 EMNLP main conference 的影响力疑虑
- 具体位置：全文
- 问题：论文自我定位为 empirical characterization，不提出新方法。唯一的 mitigation 尝试（oracle phase-aware reallocation, Discussion §7）未通过自设的 30% 门槛，95% CI 跨零。论文最终结论是 "motivate phase-aware sparsity allocation"，但未证明这一 motivation 可转化为实际改进。
- 建议：(1) 如果 oracle recovery 实验有数据（placeholder 填充后），即使未过 gate 也应详细报告，展示 ceiling analysis; (2) 更清楚地论证为何 characterization 本身对社区有价值——例如量化现有部署中可能被忽视的性能损失。

**W2** [warning] 样本量偏小且任务单一
- 具体位置：Section 4 (methodology.tex, lines 9-10)
- 问题：仅 50 个 MATH-500 问题，排除后 DeepSeek n=49、Qwen n=46。Mean/median ratio 高达 43:1 表明分布极端右偏，少数 outlier 问题可能主导结果。仅评估数学推理，未涉及 code generation、multi-hop QA 等其他 reasoning task。
- 建议：(1) 报告去除 top-5% outlier 后的 sensitivity analysis; (2) 即使不增加 benchmark，至少讨论为什么 MATH-500 的 phase structure 可能（或不可能）泛化到其他 reasoning task。

**W3** [warning] Related Work 遗漏若干重要工作
- 具体位置：Section 2 (related_work.tex)
- 问题：以下近期高相关工作未被引用：
  - **RLKV** (OpenReview 2026): 使用 RL 优化每个 head 的 cache 使用与 reasoning quality 的关系——直接涉及 head-level reasoning-aware compression
  - **LongFlow** (arXiv 2603.11504): 专门为 reasoning model 的 long-output generation 设计 KV cache compression
  - **PM-KVQ** (OpenReview 2026): Progressive mixed-precision KV cache quantization for long-CoT LLMs——compound compression（量化+eviction）的另一路径
  - 更广泛的 compound compression 文献中，quantization + pruning 的交互（如 NVIDIA Model Optimizer 相关工作）也应提及
- 建议：补充上述引用，特别是 RLKV 和 LongFlow 涉及 reasoning-aware head-level compression，与本文直接相关。

**W4** [warning] Entropy redistribution 分析在 Qwen 上不 replicate
- 具体位置：Section 6 (analysis.tex, line 6)、Appendix §E.2 (Table 8)
- 问题：Entropy redistribution 作为 "secondary amplifier" 在 Qwen 的 s=0.25 出现符号反转（+0.045），s=0.30 接近零。论文称 discrimination collapse 是 "robust, model-independent driver"，但实际上 Gini 下降幅度在 Qwen 上仅为 DeepSeek 的 1/4-1/3。如果两个 model 在同一架构上机制表现就已经差异显著，cross-architecture 的 mechanism claim 更难成立。
- 建议：更审慎地措辞 mechanism 的 generalizability；考虑是否 discrimination collapse 的 magnitude 足够解释 severity gradient 的 magnitude difference（DeepSeek vs Qwen）。

**W5** [warning] Abstract 过长且包含过多具体数字
- 具体位置：Abstract (abstract.tex, 14 行)
- 问题：Abstract 包含 3 个模型名、4 个 sparsity levels、多个 median/d_z/p-value、一个 crossover example、和 cross-architecture 的详细数据。信息密度过高，读者难以提取核心 message。ACL 传统上 abstract 不超过 ~200 words。
- 建议：精简 abstract 到核心 claim + 一两个 headline numbers；将详细统计量移到 Introduction 或 Results。

---

## 小问题（不影响接收）

1. **`h2o-neurips2023` bib entry 缺少 title 字段**（references.bib）——编译后引用可能显示异常。

2. **LaTeX source 中的 REVIEWER-ATTACK / REBUTTAL 注释**（appendix_disc_analysis.tex, lines 27-28, 34-35, 41-42, 56-57, 61-62）：虽然编译后不可见，但 ARR 审稿人如检查 source（OpenReview 可下载源码）会看到针对特定 reviewer attack 的预设 rebuttal，这暴露了非盲审信息（作者预期特定批评并预备回应），应在提交前删除。

3. **引用格式小问题**：`deepseek-r1-2025` 的 author 字段为 "DeepSeek-AI" 而 OpenAlex 记录为 "Guo et al."；`snapkv-neurips2024` 的 first author bib 中为 Li 但 API 记录为 Cai。应核实 canonical author 信息。

4. **Phase segmentation 依赖 quantile-based tercile**：这意味着每个 sequence 都被强制分成三个等大的 phase。如果某个 sequence 的 attention sparsity 分布是 unimodal 的，这种 segmentation 可能产生 artificial phase boundary。论文未讨论 segmentation 的 sensitivity。

5. **Eq. 3 中 G 的定义**（background.tex, line 26-28）：当 $\widetilde{\mathrm{II}}_{\textit{high}} \approx 0$ 时（如 Table 2 中 s=0.15 的 0.006），G 对分母的微小变化极端敏感。报告的 G=69×-274× 可能 inflate 了实际的 phase contrast 程度。建议同时报告 $\Delta$（已报告）和 G，并讨论 G 在分母接近零时的 instability。

6. **Discussion 中 s=0.35 的 supplementary experiment**（appendix_disc_analysis.tex, line 11）提到 "high-phase II rises to 0.105" 但未在任何 table 中报告完整结果。如果要引用应提供更多 context。

---

## Questions to Authors

1. Table 4 的所有 placeholder 何时能填充？如果 LLaMA 实验数据已有但未整理完，建议在 resubmission 时完整报告。如果实验尚未完成，建议删除 Section 5.5 并降低 cross-architecture claim 的强度。

2. 能否提供 HIES (2025) 的 discrimination collapse 与本文 entropy-discrimination collapse 的 explicit comparison？具体而言：HIES 是否也观察到了 phase-dependent 的 discrimination loss？如果没有，这是否是本文的核心 novelty delta？

3. 对于 mean/median ratio 高达 43:1 的分布，是否考虑过 winsorization 或 trimmed mean 作为 robustness check？即使使用非参数方法，极端 outlier 仍可能影响 bootstrap CI 的宽度。

4. 论文提到 "BOS always retained" 但未讨论 sink token phenomenon。在 attention sink 设置下（如 StreamingLLM），compound sparsity 的 phase modulation 是否仍然成立？

5. Oracle phase-aware reallocation 未通过 30% 门槛。这是否说明 phase-aware budget 本身不是一个 promising direction，还是实现细节（如 oracle vs heuristic phase boundary detection）的问题？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 228 · 2026-05-15T07:42:26.080875+00:00_

Reviewer 2 的 Round 1 审稿意见已收到。评分 2.5/5，核心问题：30+ placeholders 未填充、cross-architecture 证据不足支撑 title framing、与 HIES 的区分不充分。

等待 Reviewer 1 的审稿意见，收齐后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 229 · 2026-05-15T07:42:28.898106+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

**审稿结论：Overall 2.5/5**，介于 Resubmit 和 Findings 之间。

核心问题：
1. **30+ placeholders 未填充**（Table 4 完全空白、Discussion oracle 实验数据缺失）——论文处于未完成状态
2. **Cross-architecture 证据不支撑 title/abstract 的 framing**——LLaMA 结果 4/4 中仅 1 个显著，magnitude 仅为 1/40，random eviction 也有 phase gradient
3. **与 HIES (2025) 的 discrimination collapse 区分不足**——机制新颖性存疑

优势：统计方法论严谨（非参数 bootstrap + permutation test + Bonferroni），random eviction 作为 falsification control 设计巧妙，DeepSeek Qwen2 主实验结果有说服力。

引用验证方面：29 篇引用均为真实论文，无幻觉引用；但 `h2o-neurips2023` 缺少 title 字段，3 篇作者信息有小偏差。另外发现 LaTeX source 中有 REVIEWER-ATTACK/REBUTTAL 开发注释需删除。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 230 · 2026-05-15T07:42:37.732892+00:00_

Reviewer 2 初审意见已收到（Overall 2.5/5）。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 14

## Round 14

6 recorded events


### User

_source line 231 · 2026-05-15T07:43:46.876217+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告（方法严谨性）

论文：*Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models*

---

## 总体评分
**Overall**: 2.5 / 5（Borderline Findings）
**一句话总结**: 研究问题新颖且实验设计系统，但论文存在大量未填数据（40+ placeholders 包括 abstract 和主要 results table）、单一 benchmark、cross-architecture 证据薄弱，且机制分析停留在 correlational 层面——当前状态距离可接收还有实质性差距。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5 / 5 | 核心 claim 在 DeepSeek 上有充分支撑，但 LLaMA cross-arch 证据混合且 Table 3 全空；机制分析纯 correlational；大量数据缺失使多处 claim 无法验证 |
| Excitement | 3 / 5 | 发现 compound sparsity 的 phase-strategy interaction 是有价值的，crossover 现象有实际部署意义；但 single benchmark + single scale 限制了 impact |
| Reproducibility | 2 / 5 | 随机种子未报告，代码/数据无开源声明，Table 3 全空，多处关键统计值为 placeholder——当前状态无法复现 cross-arch 和 pilot experiment 结果 |
| Reviewer Confidence | 4 / 5 | 仔细检查了实验设计、统计方法、数据一致性和引用 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 大量 `\placeholder{}` 未填充数据——论文未达投稿状态

- 具体位置：abstract (line 8), §5.4 results.tex (lines 71, 81, 86, 92-95), §7 discussion.tex (lines 10, 15), Appendix B/C/D (appendix_moved.tex lines 30, 35, 41-43, 73, 76; appendix_disc_analysis.tex lines 14, 49)
- 问题：论文中有 **40+ 个** 独立的 `\placeholder{}` 占位符未填，涵盖：
  - **Abstract**: Qwen random s=0.30 的 $\widetilde{\Delta}$ 值
  - **Table 3 (LLaMA cross-arch, §5.5)**: 整个表格 16 个数据单元格全部为空，包括所有 $\widetilde{\Delta}$、CI 和 $p_{\text{Bonf}}$ 值
  - **§5.4 cross-model**: Qwen mid-phase null rate (`NULL_PCT`)、LLaMA 样本量 (`N_LLAMA`)
  - **§7 Discussion**: Oracle pilot experiment 全部 4 个关键指标（`ORACLE_PCT`、`ORACLE_P`、`HEUR_PCT`、`HEUR_P`）
  - **Appendix**: Qwen effective-n 表 (12 cells)、per-problem concordance (ρ, p)、Qwen total n
- 为什么影响接收：文本中做出的 claims（如 "mixed but directionally consistent evidence", "partially confirms"）围绕这些空数据展开，reviewer 无法验证任何 LLaMA cross-arch claim 或 pilot experiment claim。这不是"格式问题"而是**数据完整性问题**。
- 建议修改方向：填充所有 placeholder 数据；如果实验尚未完成，应删除相关 claim 而非保留空表格。

**N2** [critical] 50 题样本量的统计效力论证缺失

- 具体位置：§4 methodology.tex (line 10)
- 问题：从 MATH-500 中抽取 50 题（10% 采样率），论文声称"stratified sampling"但未报告：(a) 分层的具体方案和各层样本量；(b) 事先的 power analysis；(c) 为什么 50 题足以检测报告的效应量。实际有效样本更少——DeepSeek n=49（1 题排除，排除标准未说明）、Qwen n=46（4 题排除为"degenerate phase assignments"）、LLaMA n=49。在 Qwen s=0.15 处 $d_z=0.28$ 且 CI 包含零，这可能是 underpowered 的表现。
- 为什么影响接收：无 power analysis 的情况下，负面结果（如 LLaMA non-significant at s≤0.25）无法区分"效应不存在"和"样本不足"。
- 建议修改方向：(1) 报告 post-hoc power analysis；(2) 解释为什么不用全部 500 题；(3) 明确排除标准。

**N3** [critical] 单一 benchmark (MATH-500) 严重限制泛化性

- 具体位置：§4 methodology.tex (line 10); Limitations (limitations.tex lines 4-6)
- 问题：论文标题和 abstract 使用 "reasoning models" 的一般性表述，但实验仅覆盖数学推理。不同推理任务（代码生成、常识推理、多跳 QA）会产生完全不同的 attention phase structure。Limitations 中承认了这一点，但 title/abstract/conclusion 均未限定范围。
- 为什么影响接收：读者可能错误地将结论泛化到所有推理场景。对于一篇以"characterization"为核心贡献的论文，characterization 的范围直接决定贡献的大小。
- 建议修改方向：至少添加一个非数学推理 benchmark（如 code generation 或 multi-hop QA），或在 title/abstract 中明确限定为 "mathematical reasoning"。

**N4** [critical] Cross-architecture 证据薄弱且内部矛盾，不支持泛化声明

- 具体位置：§5.5 results.tex (lines 77-98); §7 discussion.tex (lines 14-15); Table 3
- 问题：
  - LLaMA 结果的绝对量级仅为 DeepSeek 的 ~1/40、Qwen 的 ~1/7
  - 统计证据混合：s=0.15 时 CI 排除零但 Wilcoxon non-significant；s=0.30 时 CI 跨越零但 Wilcoxon significant——两个统计指标自相矛盾
  - **Random eviction 在 LLaMA 上也展现 non-trivial phase gradient**（§5.5 line 81, discussion.tex line 15），这直接削弱了 "strategy-specific" 的核心 claim
  - Table 3 完全为空——上述所有数字来自文本叙述，读者无法独立验证
- 为什么影响接收：论文的 contribution 2 声称 "replicates across three models spanning two architectures"（Introduction line 23），但 LLaMA 数据：(a) 大部分 condition 非显著；(b) random eviction 也有 phase gradient 从而打破 strategy specificity；(c) Table 全空。"partially confirms" 在文本中的使用是恰当的，但 abstract 和 conclusion 的表述偏强。
- 建议修改方向：(1) 填充 Table 3；(2) 在 abstract/conclusion 中使用更谨慎的措辞（如 "suggestive evidence" 而非列为第二个 contribution）；(3) 解释为什么 random eviction 在 LLaMA 上也有 phase gradient——这对机制解释有什么影响？

**N5** [critical] 机制分析（entropy-discrimination collapse）仅为 correlational，不足以支持 causal claim

- 具体位置：§6 analysis.tex; Appendix D (appendix_moved.tex lines 115-183)
- 问题：
  - 论文标题中 "Phase-Modulated" 暗示因果方向，但证据仅为 correlation：Gini coefficient 在 pruning 后下降（Table 6），与 phase-dependent severity 共现
  - 没有 causal intervention（如固定 entropy 水平观察 II 变化，或 ablate discrimination collapse 路径）
  - Entropy redistribution 在 Qwen s=0.25 出现反转（$\Delta\mathcal{H} = +0.045$，Table 7），即 22/30 problems 熵增而非熵减——论文将此定性为 "secondary, model-dependent amplifier"，但这意味着在特定条件下机制的一半被推翻
  - Limitations 中承认 "causal validation through controlled entropy manipulation is needed"（limitations.tex line 8），但 Analysis section 的叙述仍然偏 causal（"head pruning flattens cumulative importance scores"，"degrading the discriminative power"）
- 为什么影响接收：作为 "characterization + mechanism" 论文，mechanism 部分仅提供 correlational 证据，这是 soundness 的显著缺陷。
- 建议修改方向：(1) 在 §6 开头明确标注 "correlational evidence"；(2) 设计至少一个 causal experiment（如人工 inject entropy 后测量 II）；(3) 更谨慎地讨论 Qwen s=0.25 的 entropy 反转对机制通用性的影响。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Phase segmentation（tercile-based）缺乏充分论证

- 具体位置：§3 background.tex (line 32-33); Appendix A (appendix.tex line 33)
- 问题：论文使用 attention sparsity 的 tercile 划分 3 个 phases，引用 ThinKV 作为先例。但 ThinKV 使用 explicit `&lt;think>` delimiters 划分 thinking/non-thinking phases——与 quantile-based segmentation 是完全不同的方法。为什么用 3 个 phase 而非 4 或 5？为什么用 tercile 而非 data-driven change-point detection？`min_phase_length=10` 的选择依据是什么？
- 建议：(1) 报告 segmentation sensitivity analysis（改变 phase 数量或分割方法对结果的影响）；(2) 不宜将 ThinKV 作为 tercile segmentation 的直接先例。

**W2** [warning] 对称稀疏率 (symmetric $s$) 的实践代表性不足

- 具体位置：§4 methodology.tex (line 13-14)
- 问题：对 head pruning 和 KV cache eviction 使用相同的 $s$，但实际部署中两个轴的最优 budget 通常不同（e.g., 可能 prune 20% heads 但 evict 40% KV cache）。论文未讨论 asymmetric sparsity 对结论的影响。
- 建议：至少讨论 symmetric assumption 的局限性，或提供 1-2 个 asymmetric configuration 的 spot check。

**W3** [warning] Severity gradient $G$ 的数值稳定性问题

- 具体位置：§3 background.tex (Eq. 2); Table 2 results.tex
- 问题：$G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$，当 $\widetilde{\mathrm{II}}_{\textit{high}}$ 接近零时（如 s=0.15 时为 0.006），$G$ 对分母的微小波动极其敏感。0.006 的 bootstrap CI 是多少？如果 CI 为 [0.003, 0.012]，则 $G$ 的不确定范围为 [33, 133]——远大于 point estimate 69。
- 建议：报告 $G$ 的 bootstrap CI，或改用对分母不敏感的指标（如 $\Delta$ 已经报告了，可以用 $\Delta$ 作为主要指标，$G$ 降级为辅助指标）。

**W4** [warning] Bonferroni 校正范围可能不足

- 具体位置：§4 methodology.tex (line 22); §5.6 results.tex (line 104)
- 问题：论文对 4 个 sparsity levels 做 Bonferroni 校正（$k=4$），但实际比较远多于此：2 strategies × 4 sparsity levels × 3 models × low-high paired comparison = 至少 24 个 tests。即使只考虑 DeepSeek 的 importance vs random 对比也有 4 个 test（已校正），但还有 Qwen 的 4 个、LLaMA 的 4 个，以及 within-random 的 8 个。Family-wise error rate 可能被低估。
- 建议：说明 Bonferroni correction 的 family 划分依据；或采用 FDR 控制方法。

**W5** [warning] Cohen's $d_z$ 解读和 Spearman $\rho = 1.0$ 的 4-point 单调性

- 具体位置：§5.4 results.tex (line 71); §5.6 Table 4 results.tex
- 问题：
  - 4 个有序 sparsity levels 上 Spearman $\rho = 1.0$ 说明 $d_z$ 值严格递增，但 4 个点的 $\rho = 1.0$ 概率为 1/24 = 0.042——permutation $p = 0.043$ 仅勉强通过 $\alpha = 0.05$，论文不应将此描述为强证据
  - Table 4 中 DeepSeek $\widetilde{\Delta}$ 值（0.32, 1.15, 3.97, 9.94）与 Table 1 的 $\Delta$ 值（0.39, 1.48, 7.16, 14.59）不同——前者是 per-problem paired median，后者是 segment-level median difference。论文未明确区分这两个统计量，容易混淆读者
- 建议：(1) 不要过度强调 $\rho = 1.0$；(2) 在 Table 4 caption 或 footnote 中解释与 Table 1 的数字差异来源。

**W6** [warning] 数据一致性：n=49 vs n=50 排除标准未说明

- 具体位置：§4 methodology.tex (line 10: "50 problems"); Appendix C appendix_moved.tex (line 82: "n=49 paired problems for DeepSeek")
- 问题：方法说 50 题，但 DeepSeek 实际用 49（排除 1 题），Qwen 用 46（排除 4 题）。排除标准未在 §4 中说明，仅在 Appendix 中提到 Qwen 排除原因为 "degenerate phase assignments"，DeepSeek 的排除原因未提及。
- 建议：在 §4 中明确排除标准和各模型的最终有效 n。

---

## 小问题（不影响接收）

- Abstract 过度密集（14 行连续文本含 10+ 个统计数字），可读性差
- `h2o-neurips2023` bib entry 缺少 title 字段
- 引用验证：`defensivekv-iclr2026`、`hies-2025`、`phase-transition-compression-2026` 在 OpenAlex 中未查到（可能是太新或索引延迟）；`deepseek-r1-2025`、`qwen25-2024`、`snapkv-neurips2024`、`unicomp-2026` 有 first author mismatch（可能是 team 署名 vs 个人署名）
- LaTeX 源码中 `\paragraph` labels（如 `\label{sec:compound-sparsity}`）使用 `sec:` 前缀但实际是 paragraph 级别，可能导致交叉引用混乱
- §4 脚注提到 "4× NVIDIA RTX PRO 6000 Blackwell 96GB GPUs" 但无其他硬件细节（CPU、内存、单次实验时间）
- 论文未提及代码或数据的开源计划

---

## 主要优势

1. **研究问题有价值**：compound sparsity 的 phase-strategy interaction 是一个尚未被系统研究的重要现象，对 efficient inference 部署有直接意义
2. **实验设计系统**：4 个 sparsity levels × 2 strategies × 3 models，配合 random eviction 作为 falsification control，实验矩阵设计合理
3. **统计方法谨慎**：使用 nonparametric methods 处理 right-skewed distribution、paired tests 控制 problem-level variance、Bonferroni correction、报告 effect sizes 和 CIs——统计意识优于多数 ML 论文
4. **Crossover 发现有 insight**：§5.3 的 strategy ranking reversal 是一个 non-trivial 发现——importance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random，这对 deployment 有直接启示
5. **Multiplicative null verification**（Appendix A）增强了 II 定义的 robustness
6. **Limitations 写得坦诚**：多数局限在 limitations section 中有诚实讨论

---

## Questions for Authors

1. 为什么只用 50/500 题？是否有计算预算限制？在全部 500 题上运行 s=0.25 的 DeepSeek 配置大约需要多少 GPU 时间？
2. Phase segmentation 对结果的敏感性如何？如果改用 quartile 或 5-quantile 分割，main findings 是否 robust？
3. LLaMA 上 random eviction 也展现 non-trivial phase gradient——这是否意味着在某些架构上 phase-modulated severity 不是 strategy-specific 的，而是 compound sparsity 的 inherent property？这对论文的核心 narrative 有何影响？
4. Qwen s=0.25 的 entropy 反转（$\Delta\mathcal{H} = +0.045$）是否与该 sparsity level 的 severity gradient 有 quantitative 关联？
5. Oracle pilot experiment（Discussion）结果全部为 placeholder——这个实验是否已执行？如果已执行但 below gate，为什么不填入数据？
6. 是否计划开源代码和实验数据？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-15T07:44:18.039625+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见（新颖性/完整性）\n\n**Overall**: 2.5 / 5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.0 / 5 |\n| Excitement | 2.5 / 5 |\n| Reproducibility | 3 / 5 |\n| Confidence | 4 / 5 |\n\n### Must-Fix 问题\n\n**N1** [critical] 论文严重未完成：30+ `\\placeholder{}` 未填充\n- Abstract (line 8)、Section 5.4 (`NULL_PCT`)、Table 4 全部数据 (Section 5.5, lines 86-98)、Discussion (`ORACLE_PCT`, `ORACLE_P`, `HEUR_PCT`, `HEUR_P`)、Appendix 多处\n- Table 4（cross-architecture validation）是本文最重要的 generalization 证据，但所有数据格全部为空\n- Discussion 中的 oracle phase-aware reallocation 实验——四个关键数字全部缺失\n\n**N2** [critical] Cross-architecture 证据不足以支撑论文标题和 abstract 的 framing\n- LLaMA 结果极弱——4 个 sparsity levels 中仅 s=0.30 显著 (p=0.029)\n- magnitude 仅为 DeepSeek 的 ~1/40\n- random eviction 在 LLaMA 上也展示了 non-trivial phase gradient，削弱 strategy-specificity claim\n- Title 使用复数 \"Reasoning Models\" 属于 overclaim\n\n**N3** [critical] 与 HIES (2025) 的区分不充分\n- HIES 已报告 \"head importance-based discrimination collapses under heavy pruning\"\n- 本文 entropy-discrimination collapse 与 HIES 高度重叠\n- Analysis 中未讨论两者区别\n\n### Should-Fix 问题\n\n**W1** 贡献定位为 empirical finding——对 EMNLP main conference 的影响力疑虑\n**W2** 样本量偏小且任务单一（50 题 MATH-500）\n**W3** Related Work 遗漏：RLKV, LongFlow, PM-KVQ 等\n**W4** Entropy redistribution 在 Qwen s=0.25 反转，mechanism generalizability 存疑\n**W5** Abstract 过长且包含过多具体数字\n\n### 小问题\n1. h2o-neurips2023 bib entry 缺少 title 字段\n2. LaTeX 中 REVIEWER-ATTACK/REBUTTAL 注释应删除\n3. 引用格式小问题（author mismatch）\n4. Phase segmentation sensitivity 未讨论\n5. G 在分母接近零时的 instability\n6. s=0.35 supplementary experiment 未完整报告\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5)、和你认为重要的小问题逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见（新颖性/完整性）\n\n**Overall**: 2.5 / 5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.0 / 5 |\n| Excitement | 2.5 / 5 |\n| Reproducibility | 3 / 5 |\n| Confidence | 4 / 5 |\n\n### Must-Fix 问题\n\n**N1** [critical] 论文严重未完成：30+ `\\placeholder{}` 未填充\n- Abstract (line 8)、Section 5.4 (`NULL_PCT`)、Table 4 全部数据 (Section 5.5, lines 86-98)、Discussion (`ORACLE_PCT`, `ORACLE_P`, `HEUR_PCT`, `HEUR_P`)、Appendix 多处\n- Table 4（cross-architecture validation）是本文最重要的 generalization 证据，但所有数据格全部为空\n- Discussion 中的 oracle phase-aware reallocation 实验——四个关键数字全部缺失\n\n**N2** [critical] Cross-architecture 证据不足以支撑论文标题和 abstract 的 framing\n- LLaMA 结果极弱——4 个 sparsity levels 中仅 s=0.30 显著 (p=0.029)\n- magnitude 仅为 DeepSeek 的 ~1/40\n- random eviction 在 LLaMA 上也展示了 non-trivial phase gradient，削弱 strategy-specificity claim\n- Title 使用复数 \"Reasoning Models\" 属于 overclaim\n\n**N3** [critical] 与 HIES (2025) 的区分不充分\n- HIES 已报告 \"head importance-based discrimination collapses under heavy pruning\"\n- 本文 entropy-discrimination collapse 与 HIES 高度重叠\n- Analysis 中未讨论两者区别\n\n### Should-Fix 问题\n\n**W1** 贡献定位为 empirical finding——对 EMNLP main conference 的影响力疑虑\n**W2** 样本量偏小且任务单一（50 题 MATH-500）\n**W3** Related Work 遗漏：RLKV, LongFlow, PM-KVQ 等\n**W4** Entropy redistribution 在 Qwen s=0.25 反转，mechanism generalizability 存疑\n**W5** Abstract 过长且包含过多具体数字\n\n### 小问题\n1. h2o-neurips2023 bib entry 缺少 title 字段\n2. LaTeX 中 REVIEWER-ATTACK/REBUTTAL 注释应删除\n3. 引用格式小问题（author mismatch）\n4. Phase segmentation sensitivity 未讨论\n5. G 在分母接近零时的 instability\n6. s=0.35 supplementary experiment 未完整报告\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5)、和你认为重要的小问题逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-15T07:44:34.233650+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16194
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-15T07:44:34.434848+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿报告（方法严谨性）\n\n**Overall**: 2.5 / 5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 2.5 / 5 |\n| Excitement | 3 / 5 |\n| Reproducibility | 2 / 5 |\n| Confidence | 4 / 5 |\n\n### Must-Fix 问题\n\n**N1** [critical] 大量 `\\placeholder{}` 未填充数据——40+ placeholders\n- abstract, Table 3 (LLaMA) 16 cells 全空, §5.4 cross-model, §7 Discussion oracle pilot, Appendix 多处\n- 不是\"格式问题\"而是数据完整性问题\n\n**N2** [critical] 50 题样本量的统计效力论证缺失\n- 无 power analysis\n- 10% 采样率，分层方案未报告\n- Qwen s=0.15 $d_z=0.28$ CI 包含零可能是 underpowered\n- 负面结果无法区分\"效应不存在\"和\"样本不足\"\n\n**N3** [critical] 单一 benchmark (MATH-500) 严重限制泛化性\n- Title/abstract 使用 \"reasoning models\" 但仅测数学推理\n- 不同推理任务会产生不同 attention phase structure\n\n**N4** [critical] Cross-architecture 证据薄弱且内部矛盾\n- LLaMA ~1/40 magnitude\n- s=0.15 CI 排除零但 Wilcoxon non-significant vs s=0.30 CI 跨零但 Wilcoxon significant——统计指标自相矛盾\n- Random eviction 在 LLaMA 上也有 non-trivial phase gradient\n- Table 3 完全为空\n- Contribution 2 称 \"replicates across three models spanning two architectures\" 属 overclaim\n\n**N5** [critical] 机制分析仅为 correlational，不足以支持 causal claim\n- 无 causal intervention\n- Entropy redistribution 在 Qwen s=0.25 反转\n- Analysis 叙述偏 causal 但证据仅 correlational\n\n### Should-Fix 问题\n\n**W1** Phase segmentation（tercile-based）缺乏充分论证——ThinKV 用 explicit delimiters 而非 quantile，两者不同\n**W2** 对称稀疏率 (symmetric $s$) 的实践代表性不足\n**W3** G 的数值稳定性问题——分母接近零时 G 极不稳定\n**W4** Bonferroni 校正范围可能不足——实际 test 数远多于 k=4\n**W5** Spearman ρ=1.0 的 4-point 单调性仅 p=0.043，不应描述为强证据；Table 4 vs Table 1 数字差异未解释\n**W6** n=49 vs n=50 排除标准未说明\n\n### 小问题\n- Abstract 过度密集\n- h2o bib entry 缺 title\n- 引用 author mismatch\n- LaTeX label 前缀混乱\n- 硬件细节不足\n- 无代码/数据开源计划\n\n---\n\n请对以上每个 Must-Fix (N1-N5)、Should-Fix (W1-W6)、和你认为重要的小问题逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿报告（方法严谨性）\n\n**Overall**: 2.5 / 5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 2.5 / 5 |\n| Excitement | 3 / 5 |\n| Reproducibility | 2 / 5 |\n| Confidence | 4 / 5 |\n\n### Must-Fix 问题\n\n**N1** [critical] 大量 `\\placeholder{}` 未填充数据——40+ placeholders\n- abstract, Table 3 (LLaMA) 16 cells 全空, §5.4 cross-model, §7 Discussion oracle pilot, Appendix 多处\n- 不是\"格式问题\"而是数据完整性问题\n\n**N2** [critical] 50 题样本量的统计效力论证缺失\n- 无 power analysis\n- 10% 采样率，分层方案未报告\n- Qwen s=0.15 $d_z=0.28$ CI 包含零可能是 underpowered\n- 负面结果无法区分\"效应不存在\"和\"样本不足\"\n\n**N3** [critical] 单一 benchmark (MATH-500) 严重限制泛化性\n- Title/abstract 使用 \"reasoning models\" 但仅测数学推理\n- 不同推理任务会产生不同 attention phase structure\n\n**N4** [critical] Cross-architecture 证据薄弱且内部矛盾\n- LLaMA ~1/40 magnitude\n- s=0.15 CI 排除零但 Wilcoxon non-significant vs s=0.30 CI 跨零但 Wilcoxon significant——统计指标自相矛盾\n- Random eviction 在 LLaMA 上也有 non-trivial phase gradient\n- Table 3 完全为空\n- Contribution 2 称 \"replicates across three models spanning two architectures\" 属 overclaim\n\n**N5** [critical] 机制分析仅为 correlational，不足以支持 causal claim\n- 无 causal intervention\n- Entropy redistribution 在 Qwen s=0.25 反转\n- Analysis 叙述偏 causal 但证据仅 correlational\n\n### Should-Fix 问题\n\n**W1** Phase segmentation（tercile-based）缺乏充分论证——ThinKV 用 explicit delimiters 而非 quantile，两者不同\n**W2** 对称稀疏率 (symmetric $s$) 的实践代表性不足\n**W3** G 的数值稳定性问题——分母接近零时 G 极不稳定\n**W4** Bonferroni 校正范围可能不足——实际 test 数远多于 k=4\n**W5** Spearman ρ=1.0 的 4-point 单调性仅 p=0.043，不应描述为强证据；Table 4 vs Table 1 数字差异未解释\n**W6** n=49 vs n=50 排除标准未说明\n\n### 小问题\n- Abstract 过度密集\n- h2o bib entry 缺 title\n- 引用 author mismatch\n- LaTeX label 前缀混乱\n- 硬件细节不足\n- 无代码/数据开源计划\n\n---\n\n请对以上每个 Must-Fix (N1-N5)、Should-Fix (W1-W6)、和你认为重要的小问题逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-15T07:44:36.095632+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1660
}
```

</details>

---


### Assistant

_source line 236 · 2026-05-15T07:44:38.950738+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 237 · 2026-05-15T07:44:41.768940+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：

- **Overall: 2.5/5 (Borderline Findings)**
- 5 个 Must-Fix 问题：(N1) 40+ placeholders 未填充（含 abstract 和 Table 3 全空）；(N2) 50 题样本量无 power analysis；(N3) 单一 benchmark 限制泛化；(N4) LLaMA cross-arch 证据薄弱且 random eviction 也有 phase gradient；(N5) 机制分析纯 correlational
- 6 个 Should-Fix：tercile segmentation 论证不足、symmetric sparsity 假设、G 值数值稳定性、Bonferroni 范围偏窄、$\rho=1.0$ 在 4 点上的意义有限、n 的排除标准不透明
- 主要优势：研究问题有价值、实验矩阵设计系统、统计方法优于多数 ML 论文、crossover 发现有 insight

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 238 · 2026-05-15T07:44:46.453969+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 239 · 2026-05-15T07:45:59.195102+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 30+ `\placeholder{}` 未填充**

完全同意。这也是我的 N1。我的统计更精确：实际有 **40+** 个独立 placeholder 值（R2 报告 30+）。补充 R2 未列出的位置：
- Appendix B (appendix_moved.tex) 中 Qwen effective-n table 有 12 个空 cell（lines 41-43）
- Per-problem concordance 的 $\rho$ 和 $p$ 值（appendix_moved.tex line 73），尽管 LaTeX 注释中已有数据（`mean_rho=-0.107, per_problem_concordance_p=0.926`），但正文未填入
- Discussion 中 LLaMA random p-value 重复出现两次（results.tex line 81, discussion.tex line 15），均为空

这些 placeholder 的密度说明论文可能是在实验数据尚未完全就绪的情况下提交的。

**[AGREE] R2-N2: Cross-architecture 证据不支撑标题和 abstract 的 framing**

核心判断同意——LLaMA 证据确实太弱以至于不能作为 "cross-architecture generalization" 的有力支撑。我的 N4 提出了相同问题。

补充 R2 未提及的一个自相矛盾细节：§5.5 (results.tex lines 78-79) 中 LLaMA 的统计证据自相矛盾——s=0.15 时 bootstrap CI 排除零但 Wilcoxon non-significant，s=0.30 时 CI 跨越零但 Wilcoxon significant。两个统计方法对同一数据给出相反结论，论文未讨论这一不一致性。

关于 "Reasoning Models"（复数）是否属于 overclaim：R2 的批评合理但可以更精确。标题中的复数在字面上成立（确实测了 3 个模型），但暗示的泛化范围超出了证据支撑——尤其是 LLaMA 的 strategy-specificity 被 random eviction 的 non-trivial phase gradient 削弱。建议标题改为类似 "...in Qwen2-based Reasoning Models with Preliminary Cross-Architecture Evidence" 的表述，或保持当前标题但在 abstract 中更明确限定。

**[REBUT] R2-N3: 与 HIES (2025) 的区分不充分——严重性被高估**

R2 声称本文的 entropy-discrimination collapse 与 HIES "高度重叠"，我认为这一判断**过重**。

关键区别在于：
1. **HIES 是 single-axis finding**：HIES 报告的是 head pruning 单独导致 importance discrimination 下降（单一压缩轴）。本文的贡献不是发现 discrimination collapse 本身，而是证明它在 **compound sparsity**（双轴交互）下产生 **phase-dependent** 的放大效应——这是 HIES 未涉及的。
2. **Phase modulation 是新的**：HIES 没有 phase segmentation 或 phase-strategy interaction 的分析。本文的核心 finding——severity gradient 从 69× 到 274× 且仅在 importance-based eviction 下出现——不能从 HIES 的单轴 discrimination collapse 推导出来。
3. **Crossover 现象**：§5.3 的 strategy ranking reversal（importance 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）是 HIES 框架中不存在的 prediction。

但我同意论文在 Related Work 和 Analysis 中**对 HIES 的讨论确实不充分**。Related Work (related_work.tex line 17) 仅用一句话提及 HIES，§6 Analysis 完全未讨论两者区别。论文应：(1) 在 Related Work 中明确说明 HIES 是 single-axis，本文 extend 到 compound + phase-dependent setting；(2) 在 §6 中讨论本文的 discrimination collapse 如何 build upon HIES 的发现。

判定：问题存在（讨论不充分），但 R2 将其定级为 "critical" 且暗示 novelty 不足（"高度重叠"）我认为不准确——两者的 scope 和 contribution 有清晰区分。建议降级为 Should-Fix。

---

### Should-Fix 问题

**[REBUT] R2-W1: Empirical finding 对 EMNLP main 影响力疑虑**

不同意这构成一个独立的 weakness。ACL/EMNLP 历来接受高质量的 empirical finding 论文——不要求必须提出新方法。Sparse Frontier (2025)、UniComp (2026) 等被本文引用的工作同样是 characterization/finding 类论文且发表在顶会。

关键是 finding 是否有足够的 **novelty + actionability**。本文的 crossover 发现（§5.3）直接意味着 uniform sparsity budget 在 deployment 中是 suboptimal 的——这对实际系统有明确启示。影响力的真正限制不在于"empirical finding"这个类别，而在于 single benchmark + limited scale（这已在 N3/W2 中捕获）。

如果 R2 的意思是论文缺乏 mitigation method 来配合 finding，那 Discussion (discussion.tex lines 9-11) 中的 oracle pilot experiment 本可以填补这一空白——但数据全部为 placeholder，使得这部分贡献无法评估。

**[AGREE] R2-W2: 样本量偏小且任务单一**

完全同意，与我的 N2 和 N3 一致。不再重复。

**[AGREE with caveat] R2-W3: Related Work 遗漏 RLKV, LongFlow, PM-KVQ**

部分同意。Related Work 的覆盖面可以更广。但需要注意：
- 本文的 focus 是 **compound sparsity 的 phase-strategy interaction**，不是综述 KV cache 方法
- 如果所列遗漏论文仅涉及 single-axis KV cache optimization 且未讨论 compound interaction 或 phase-dependent effects，它们与本文的相关性是间接的
- R2 应指明这些遗漏如何**具体影响对本文 contribution 的评价**，而非简单列出 "应该引用"

建议 R2 澄清哪些遗漏论文有与本文直接相关的 finding（如 compound interaction 或 phase-dependent compression）。如果仅是 KV cache 方法的补充引用，降级为 minor issue 更合适。

**[AGREE] R2-W4: Entropy redistribution 在 Qwen s=0.25 反转**

同意。这也是我的 N5 的一部分。22/30 problems 出现 $\Delta\mathcal{H} = +0.045$（Appendix D, appendix_moved.tex lines 159），说明在特定条件下 pruning 导致 surviving heads 的 attention 变得更分散而非更集中——这与 discrimination collapse → entropy compression 的叙事矛盾。

论文将 entropy redistribution 定位为 "secondary, model-dependent amplifier"（analysis.tex line 6）是一种降级处理，但当 2/4 Qwen conditions 不支持时（limitations.tex line 9: "replicates on only 2/4 Qwen conditions"），"amplifier" 这个词本身就不恰当——一个在一半条件下反转的效应不是 amplifier，是一个待解释的独立现象。

**[AGREE] R2-W5: Abstract 过长且包含过多具体数字**

同意。Abstract 14 行文本中嵌入了 10+ 个统计数字（$d_z$, $p$ values, medians, sparsity levels），远超可读性阈值。特别是 LLaMA 结果的细节（"$\widetilde{\Delta}$: $0.020 \to 0.356$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$"）属于 results section 而非 abstract。

---

### 小问题

**[AGREE] R2-Minor-1: h2o-neurips2023 bib entry 缺 title** — 引用验证确认。

**[REBUT] R2-Minor-2: REVIEWER-ATTACK/REBUTTAL 注释应删除** — 这些是 LaTeX `%` 注释（如 appendix_disc_analysis.tex lines 27, 34-35, 41-42），不会出现在编译后的 PDF 中。Blind review 中 reviewer 看到的是 PDF 不是源码。当然，如果提交流程要求上传源码（ARR 某些情况下要求），则确实应删除。建议降级为可选清理项。

**[AGREE] R2-Minor-4: Phase segmentation sensitivity 未讨论** — 这是我的 W1，完全同意。

**[AGREE] R2-Minor-5: G 的分母接近零时 instability** — 这是我的 W3，完全同意。

**[AGREE] R2-Minor-6: s=0.35 supplementary experiment 未完整报告** — Appendix D (appendix_disc_analysis.tex line 11) 中仅用一句话提及 "at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment"，无 table、无 CI、无 statistical test。要么完整报告，要么删除。

---

### 总结

与 R2 的 14 个问题中，我 **AGREE** 10 个、**REBUT** 2 个（N3 严重性过高、W1 非独立 weakness）、**AGREE with caveat** 2 个（N2 标题措辞、W3 遗漏论文的相关性需澄清）。

两位 reviewer 的核心共识：
1. **Placeholder 问题**是 showstopper（R1-N1, R2-N1）
2. **Cross-architecture 证据薄弱**（R1-N4, R2-N2）
3. **单一 benchmark + 小样本**限制 generalizability（R1-N2/N3, R2-W2）
4. **机制分析 correlational only**（R1-N5, R2-W4 partial overlap）

主要分歧：
- HIES 重叠问题：R2 认为 critical，我认为 should-fix（讨论不充分但 contribution 有清晰区分）
- Empirical finding 类型：R2 质疑 venue fit，我认为这不是独立 weakness

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 240 · 2026-05-15T07:46:04.339000+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 241 · 2026-05-15T07:46:07.438308+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。与 R2 的 14 个问题中 AGREE 10 个、REBUT 2 个（N3 HIES 重叠严重性过高、W1 empirical finding 不构成独立 weakness）、带保留意见 AGREE 2 个。两位 reviewer 在 placeholder、cross-arch 证据薄弱、单一 benchmark、mechanism correlational-only 四个核心问题上达成共识。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 242 · 2026-05-15T07:46:14.088166+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 18

## Round 18

8 recorded events


### User

_source line 243 · 2026-05-15T07:46:15.597653+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 1 意见逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 大量 placeholder 未填充**
完全同意。我在自己的审稿中也将此列为 #1 critical issue。需要补充：R1 报告 40+ placeholders，我清点约 30+——差异可能源于计数粒度（Table 4 是按 cell 还是按 row 计）。核心问题一致：Table 4（cross-architecture, Section 5.5）整表空白，Discussion 中 oracle recovery 实验四个关键数字全部缺失。论文以当前状态无法进入实质性审稿。

**[AGREE with nuance] R1-N2: 50 题样本量 / 缺乏 power analysis**
同意 power analysis 缺失是方法论短板，也同意 Qwen s=0.15 ($d_z$=0.28, CI 含零) 可能是 underpowered 而非效应不存在。但需要补充两点 nuance：

1. 论文使用 **paired** 非参数检验（paired permutation test, paired bootstrap），这显著提升了 effective power——每个问题同时在两种 strategy 下评估，消除了 between-problem variance。R1 未提及 paired design 的 power advantage。
2. 在 DeepSeek 上，**所有 4 个 sparsity levels 的 Bonferroni-corrected p < 0.005**（Table 6, Appendix §D），且 CI lower bounds 单调递增 ($0.19 \to 6.70$)。这不是 borderline 结果。Power 不足的疑虑主要限于 Qwen s=0.15 和 LLaMA，而非全局。

因此，我认为 power analysis 缺失是 should-fix 而非 critical——主结论在 DeepSeek 上统计充分，但在 Qwen 低 sparsity 和 LLaMA 全局上确实需要 power 论证或坦承 underpowered。

**[AGREE] R1-N3: 单一 benchmark 限制泛化**
完全同意。我也将此列为 W2。Title 使用 "Reasoning Models" 暗示跨任务适用性，但仅测试 MATH-500。不同 reasoning task（code generation、multi-hop QA）可能产生完全不同的 attention phase structure。Limitations section (limitations.tex, ¶2) 确实承认了 "Different reasoning tasks...may induce different phase structures"，但 title/abstract 的 framing 未充分反映这一局限。

**[AGREE] R1-N4: Cross-architecture 证据薄弱**
强烈同意，这也是我的 N2 critical issue。R1 补充了一个我未充分展开的重要观察：**s=0.15 的 CI 排除零但 Wilcoxon non-significant，而 s=0.30 的 CI 跨零但 Wilcoxon significant**（Section 5.5, results.tex lines 79）——两个统计指标在同一数据上给出矛盾信号，说明 LLaMA 证据极不稳定。这比我原来的分析更精准地暴露了问题。

Contribution 2 (Introduction, line 23) 声称效应 "replicates across three models spanning two architectures"，但 LLaMA 仅 1/4 conditions 在 Bonferroni-corrected Wilcoxon 上显著，且 random eviction 在 LLaMA 上也有 non-trivial phase gradient。这确实是 overclaim。

**[REBUT with partial agreement] R1-N5: 机制分析仅为 correlational**
部分同意，但认为 R1 的 severity 评级偏高。理由：

1. **论文措辞已经是 hedged 的**：Section 6 (analysis.tex) 使用 "We propose... as the primary mechanism"（非 "We demonstrate" 或 "We prove"）；Limitations ¶3 明确承认 "causal validation through controlled entropy manipulation is needed"。
2. **Correlational evidence 跨 16 conditions 一致**：Gini coefficient 在所有 16 conditions (2 models × 4 sparsity × 2 strategies) 下一致为负（Appendix §E.1, Table 7）。虽然是 correlational，但一致性本身增加了可信度。
3. **Random eviction 的 immunity 提供了 partial causal logic**：如果 discrimination collapse 是 mechanism，则 random eviction（不依赖 score quality）应不受影响——这正是观察到的 ($G \approx 1$)。这虽非 intervention，但构成了合理的 counterfactual argument。

然而，我同意 R1 的核心关切：**entropy redistribution 在 Qwen s=0.25 的反转**（$\Delta\mathcal{H} = +0.045$, Appendix Table 8）说明即使 secondary mechanism 也未 replicate。论文将此解释为 "model-specific head specialization patterns"，但这实质上是 ad hoc 解释。

**结论**：将 N5 定级为 should-fix (warning) 而非 critical 更合适——因为论文已使用审慎措辞，且 discrimination collapse（非 entropy redistribution）被定位为主要 driver。但 Analysis section 的标题 "Entropy-Discrimination Collapse" 确实过于 assertive，应改为更 hedged 的表述。

---

### Should-Fix 问题

**[AGREE] R1-W1: Phase segmentation tercile vs ThinKV explicit delimiters**
重要观察。论文 Section 3 (background.tex, line 33) 称 "following ThinKV"，但 ThinKV 使用 `&lt;think>` token 作为 explicit phase boundary，本文使用 attention sparsity 的 quantile tercile——两者在概念上相关但方法论完全不同。Quantile-based tercile **强制将每个 sequence 分为三个等比例的 phase**，即使 attention sparsity 分布是 unimodal 或 heavily skewed 的。这可能产生 artificial phase boundaries。我在自己的小问题 #4 中也提到了这一点，但 R1 正确地将其提升为 should-fix 级别。

建议：(1) 不要称 "following ThinKV"——应说 "inspired by ThinKV's phase distinction but using a quantile-based proxy"; (2) 补充 segmentation sensitivity analysis（如 quartile 或 quintile boundary 是否改变结论）。

**[AGREE] R1-W2: Symmetric sparsity 的实践代表性**
同意。实际部署中 head pruning rate 和 KV eviction rate 通常不同（例如保留 90% heads 但 evict 50% KV cache）。论文使用 $s$ 同时控制两个轴的 sparsity rate，这在 controlled experiment 中合理（减少组合空间），但限制了实际推论。至少应在 Discussion 或 Limitations 中讨论 asymmetric sparsity 下结论是否可能不同。

**[AGREE] R1-W3: G 的数值稳定性**
完全同意。我在自己的小问题 #5 中也提到了这一点。$\widetilde{\mathrm{II}}_{\textit{high}} = 0.006$ 时（Table 2, s=0.15），分母的微小变化会导致 $G$ 剧烈波动。论文应报告 $G$ 的 bootstrap CI，或至少讨论分母接近零时 $G$ 的 interpretability。$\Delta$ 是更稳健的度量，论文实际上两者都报告了，但叙述中过度强调 $G$（"$69\times$ to $274\times$"）。

**[AGREE] R1-W4: Bonferroni 校正范围可能不足**
这是一个精准的统计学观察。论文仅对 4 个 sparsity level 做 Bonferroni correction ($k=4$)，但实际分析中的 hypothesis test 远不止 4 个：2 strategies × 4 sparsity levels × 3 models × (permutation test + Wilcoxon + bootstrap CI)。虽然不同 test 回答不同问题（非简单的 multiple comparison），但至少应论证为何 $k=4$ 是适当的 correction family。

**[AGREE] R1-W5: Spearman ρ=1.0 的 over-interpretation**
同意。4 个数据点的 Spearman ρ=1.0 给出 exact permutation $p = 0.042$ (= 1/24)，这在单次检验中 barely significant。Section 5.4 (results.tex, line 71) 称 "Spearman $\rho = 1.0$" 而未注明这仅基于 4 个点，读者可能误以为这是高 power 的证据。应明确标注 sample size 和 exact p。

R1 提到的 "Table 4 vs Table 1 数字差异" 我需要指出：Table 1 ($\Delta = 0.39$ at s=0.15) 和 Table 3 ($\widetilde{\Delta}$: $0.32$ [0.20, 0.47] at s=0.15) 确实报告了不同数字——前者是 segment-level median，后者是 problem-level paired median。论文未明确解释这一差异，R1 的观察合理。

**[AGREE] R1-W6: 排除标准未说明**
同意。Appendix §C (appendix_moved.tex, line 26) 解释了 Qwen 排除原因（"degenerate phase assignments"），但 DeepSeek 从 50 → 49 的排除原因未在任何位置说明。排除标准应在 Methodology 中完整报告。

---

### 小问题

**[AGREE]** Abstract 过度密集——我也在 W5 中指出。

**[AGREE]** h2o bib entry 缺 title——我也在小问题 #1 中指出。

**[AGREE]** 引用 author mismatch——我也在小问题 #3 中指出（deepseek-r1-2025, snapkv-neurips2024, unicomp-2026）。

**[AGREE]** 无代码/数据开源计划——对 reproducibility 有显著影响。虽然论文报告了实验参数，但 KV importance scoring 的 position normalization（Eq. 4, Appendix §A）和 phase segmentation 的具体实现细节（min_phase_length=10 的 merge 逻辑）仅凭文本描述难以完全复现。

---

### 总结

与 R1 在绝大多数问题上达成共识。主要分歧：

1. **N2 (sample size)**：我认为 paired design 提供了 R1 未充分考虑的 power advantage，主结论（DeepSeek）统计充分。降级为 should-fix。
2. **N5 (mechanism causality)**：论文已使用 hedged language，且 16/16 conditions 一致的 correlational evidence + random eviction counterfactual 构成了合理的 argument。降级为 should-fix，但 section 标题应改得更审慎。

两位 reviewer 共同认为最严重的问题是：**(1) placeholders 未填充，(2) cross-architecture claim overclaim，(3) 单一 benchmark 限制泛化**。这三点必须在 resubmission 前解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-15T07:46:42.864584+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
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

_source line 245 · 2026-05-15T07:46:42.965643+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-15T07:47:46.409881+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"40+ placeholders unfilled — paper not submission-ready (Table 4 entirely empty, Discussion oracle data missing, Abstract incomplete)\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged as #1 critical issue. R1 counted 40+, R2 counted 30+. Cross-response: full consensus.\"\n    action_items:\n      - round: 1\n        action: \"Fill all placeholder values from experimental data; if experiments incomplete, remove corresponding claims\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"Cross-architecture (LLaMA) evidence too weak to support title/abstract framing — 1/4 conditions significant, ~1/40 magnitude, random eviction also shows phase gradient\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N4 = R2-N2. Both agree LLaMA evidence is overclaimed. R1 adds: s=0.15 CI excludes zero but Wilcoxon NS, s=0.30 CI spans zero but Wilcoxon significant — contradictory signals. Contribution 2 'replicates across two architectures' is overclaim.\"\n    action_items:\n      - round: 1\n        action: \"Fill Table 4; downgrade LLaMA to exploratory supplement; use hedged language in abstract/conclusion; consider title change\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"Single benchmark (MATH-500, 50 problems) severely limits generalization — title/abstract say 'reasoning models' but only math reasoning tested\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N3 = R2-W2. Both agree single benchmark is major limitation. R1 rates critical, R2 rates warning. Cross-response: R2 upgrades to agree with R1's assessment.\"\n    action_items:\n      - round: 1\n        action: \"Add at least one non-math benchmark (code gen or multi-hop QA), OR explicitly scope title/abstract to 'mathematical reasoning'\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"50-problem sample size lacks power analysis; stratification scheme unreported; exclusion criteria unclear (DS n=49, QW n=46)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 rates critical, R2 rates should-fix (argues paired design provides power advantage, DeepSeek results statistically sufficient). Divergence on severity but agree power analysis is missing.\"\n    action_items:\n      - round: 1\n        action: \"Report post-hoc power analysis; explain why 50/500 problems; state exclusion criteria in Methodology\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N5\"\n    summary: \"Mechanism analysis (entropy-discrimination collapse) is purely correlational — no causal intervention; entropy redistribution reverses on Qwen s=0.25\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 rates critical, R2 rates should-fix (paper uses hedged language, 16/16 Gini consistent, random eviction counterfactual is partial causal logic). Both agree entropy redistribution reversal at Qwen s=0.25 undermines 'amplifier' framing.\"\n    action_items:\n      - round: 1\n        action: \"Label Analysis as 'correlational evidence'; consider causal intervention experiment; revise section title to be more hedged; address Qwen s=0.25 entropy reversal more substantively\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"Insufficient differentiation from HIES (2025) which already reports discrimination collapse under heavy pruning\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 rates critical, R1 rebuts severity (HIES is single-axis, this paper extends to compound+phase-dependent — clear delta exists). Cross-response consensus: discussion is insufficient but contribution has clear distinction. Consolidated severity: warning.\"\n    action_items:\n      - round: 1\n        action: \"Add explicit comparison paragraph in Related Work and Analysis distinguishing HIES single-axis collapse from compound+phase-dependent collapse\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation (tercile-based) lacks justification — ThinKV uses explicit delimiters not quantiles; no sensitivity analysis for phase count or boundary method\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W1, R2-Minor-4. Both agree. R2 upgrades to should-fix in cross-response.\"\n    action_items:\n      - round: 1\n        action: \"Correct 'following ThinKV' phrasing; add segmentation sensitivity analysis (quartile/quintile); justify min_phase_length=10\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Symmetric sparsity rate assumption (same s for head pruning and KV eviction) lacks practical representativeness\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W2. R2 agrees in cross-response.\"\n    action_items:\n      - round: 1\n        action: \"Discuss symmetric assumption limitation; optionally add 1-2 asymmetric spot checks\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Severity gradient G is numerically unstable when denominator II_high approaches zero — no bootstrap CI reported for G\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W3, R2-Minor-5. Both agree. G=69x-274x may be inflated by near-zero denominator.\"\n    action_items:\n      - round: 1\n        action: \"Report bootstrap CI for G; use Delta as primary metric and G as auxiliary; discuss G instability when II_high near zero\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Bonferroni correction scope (k=4) may be insufficient — actual test count is much higher across models/strategies\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W4. R2 agrees in cross-response.\"\n    action_items:\n      - round: 1\n        action: \"Justify family-wise correction scope (k=4); or adopt FDR control\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Spearman rho=1.0 on 4 points over-interpreted (p=0.042 barely significant); Table 1 vs Table 4 Delta discrepancy unexplained\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W5. R2 agrees. Table 1 segment-level median vs Table 4 problem-level paired median difference not clarified.\"\n    action_items:\n      - round: 1\n        action: \"Annotate Spearman rho with sample size caveat; explain Table 1 vs Table 4 Delta difference in caption/footnote\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"Exclusion criteria not stated in Methodology — DS 50->49 reason unknown, QW 50->46 only in Appendix\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W6. R2 agrees.\"\n    action_items:\n      - round: 1\n        action: \"State exclusion criteria and final effective n per model in Methodology section\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Related Work missing several relevant recent works: RLKV, LongFlow, PM-KVQ\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2-W3. R1 partially agrees but notes relevance depends on whether these works address compound interaction or phase-dependent effects specifically.\"\n    action_items:\n      - round: 1\n        action: \"Assess relevance of RLKV, LongFlow, PM-KVQ; cite those with direct bearing on compound or phase-aware compression\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"Abstract too long and dense — 14 lines with 10+ statistical numbers, poor readability\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged.\"\n    action_items:\n      - round: 1\n        action: \"Condense abstract to core claims + 1-2 headline numbers; move detailed statistics to Introduction/Results\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-2\"\n    summary: \"LaTeX source contains REVIEWER-ATTACK/REBUTTAL comments — visible if source uploaded to OpenReview\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 flags as should-clean. R1 rebuts (not visible in PDF), but agrees should remove if source uploaded.\"\n    action_items:\n      - round: 1\n        action: \"Remove REVIEWER-ATTACK/REBUTTAL comments from LaTeX source before submission\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-1\"\n    summary: \"h2o-neurips2023 bib entry missing title field; several author mismatches in citations\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers flagged. deepseek-r1-2025, snapkv-neurips2024, unicomp-2026 have author field discrepancies.\"\n    action_items:\n      - round: 1\n        action: \"Fix h2o bib entry; verify canonical author info for flagged entries\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-6\"\n    summary: \"s=0.35 supplementary experiment mentioned in Appendix D but not fully reported (no table, CI, or test)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree: either report fully or remove.\"\n    action_items:\n      - round: 1\n        action: \"Provide full s=0.35 results or remove the mention\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-Minor-code\"\n    summary: \"No code or data release plan mentioned — impacts reproducibility\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers noted. KV importance position normalization and phase segmentation merge logic hard to reproduce from text alone.\"\n    action_items:\n      - round: 1\n        action: \"Add code/data availability statement; consider anonymous repo for review\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"40+ placeholders unfilled — paper not submission-ready (Table 4 entirely empty, Discussion oracle data missing, Abstract incomplete)\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged as #1 critical issue. R1 counted 40+, R2 counted 30+. Cross-response: full consensus.\"\n    action_items:\n      - round: 1\n        action: \"Fill all placeholder values from experimental data; if experiments incomplete, remove corresponding claims\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"Cross-architecture (LLaMA) evidence too weak to support title/abstract framing — 1/4 conditions significant, ~1/40 magnitude, random eviction also shows phase gradient\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N4 = R2-N2. Both agree LLaMA evidence is overclaimed. R1 adds: s=0.15 CI excludes zero but Wilcoxon NS, s=0.30 CI spans zero but Wilcoxon significant — contradictory signals. Contribution 2 'replicates across two architectures' is overclaim.\"\n    action_items:\n      - round: 1\n        action: \"Fill Table 4; downgrade LLaMA to exploratory supplement; use hedged language in abstract/conclusion; consider title change\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"Single benchmark (MATH-500, 50 problems) severely limits generalization — title/abstract say 'reasoning models' but only math reasoning tested\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-N3 = R2-W2. Both agree single benchmark is major limitation. R1 rates critical, R2 rates warning. Cross-response: R2 upgrades to agree with R1's assessment.\"\n    action_items:\n      - round: 1\n        action: \"Add at least one non-math benchmark (code gen or multi-hop QA), OR explicitly scope title/abstract to 'mathematical reasoning'\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"50-problem sample size lacks power analysis; stratification scheme unreported; exclusion criteria unclear (DS n=49, QW n=46)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 rates critical, R2 rates should-fix (argues paired design provides power advantage, DeepSeek results statistically sufficient). Divergence on severity but agree power analysis is missing.\"\n    action_items:\n      - round: 1\n        action: \"Report post-hoc power analysis; explain why 50/500 problems; state exclusion criteria in Methodology\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N5\"\n    summary: \"Mechanism analysis (entropy-discrimination collapse) is purely correlational — no causal intervention; entropy redistribution reverses on Qwen s=0.25\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 rates critical, R2 rates should-fix (paper uses hedged language, 16/16 Gini consistent, random eviction counterfactual is partial causal logic). Both agree entropy redistribution reversal at Qwen s=0.25 undermines 'amplifier' framing.\"\n    action_items:\n      - round: 1\n        action: \"Label Analysis as 'correlational evidence'; consider causal intervention experiment; revise section title to be more hedged; address Qwen s=0.25 entropy reversal more substantively\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"Insufficient differentiation from HIES (2025) which already reports discrimination collapse under heavy pruning\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 rates critical, R1 rebuts severity (HIES is single-axis, this paper extends to compound+phase-dependent — clear delta exists). Cross-response consensus: discussion is insufficient but contribution has clear distinction. Consolidated severity: warning.\"\n    action_items:\n      - round: 1\n        action: \"Add explicit comparison paragraph in Related Work and Analysis distinguishing HIES single-axis collapse from compound+phase-dependent collapse\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation (tercile-based) lacks justification — ThinKV uses explicit delimiters not quantiles; no sensitivity analysis for phase count or boundary method\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W1, R2-Minor-4. Both agree. R2 upgrades to should-fix in cross-response.\"\n    action_items:\n      - round: 1\n        action: \"Correct 'following ThinKV' phrasing; add segmentation sensitivity analysis (quartile/quintile); justify min_phase_length=10\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Symmetric sparsity rate assumption (same s for head pruning and KV eviction) lacks practical representativeness\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W2. R2 agrees in cross-response.\"\n    action_items:\n      - round: 1\n        action: \"Discuss symmetric assumption limitation; optionally add 1-2 asymmetric spot checks\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Severity gradient G is numerically unstable when denominator II_high approaches zero — no bootstrap CI reported for G\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W3, R2-Minor-5. Both agree. G=69x-274x may be inflated by near-zero denominator.\"\n    action_items:\n      - round: 1\n        action: \"Report bootstrap CI for G; use Delta as primary metric and G as auxiliary; discuss G instability when II_high near zero\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Bonferroni correction scope (k=4) may be insufficient — actual test count is much higher across models/strategies\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W4. R2 agrees in cross-response.\"\n    action_items:\n      - round: 1\n        action: \"Justify family-wise correction scope (k=4); or adopt FDR control\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Spearman rho=1.0 on 4 points over-interpreted (p=0.042 barely significant); Table 1 vs Table 4 Delta discrepancy unexplained\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W5. R2 agrees. Table 1 segment-level median vs Table 4 problem-level paired median difference not clarified.\"\n    action_items:\n      - round: 1\n        action: \"Annotate Spearman rho with sample size caveat; explain Table 1 vs Table 4 Delta difference in caption/footnote\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"Exclusion criteria not stated in Methodology — DS 50->49 reason unknown, QW 50->46 only in Appendix\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1-W6. R2 agrees.\"\n    action_items:\n      - round: 1\n        action: \"State exclusion criteria and final effective n per model in Methodology section\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Related Work missing several relevant recent works: RLKV, LongFlow, PM-KVQ\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2-W3. R1 partially agrees but notes relevance depends on whether these works address compound interaction or phase-dependent effects specifically.\"\n    action_items:\n      - round: 1\n        action: \"Assess relevance of RLKV, LongFlow, PM-KVQ; cite those with direct bearing on compound or phase-aware compression\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"Abstract too long and dense — 14 lines with 10+ statistical numbers, poor readability\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged.\"\n    action_items:\n      - round: 1\n        action: \"Condense abstract to core claims + 1-2 headline numbers; move detailed statistics to Introduction/Results\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-2\"\n    summary: \"LaTeX source contains REVIEWER-ATTACK/REBUTTAL comments — visible if source uploaded to OpenReview\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 flags as should-clean. R1 rebuts (not visible in PDF), but agrees should remove if source uploaded.\"\n    action_items:\n      - round: 1\n        action: \"Remove REVIEWER-ATTACK/REBUTTAL comments from LaTeX source before submission\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-1\"\n    summary: \"h2o-neurips2023 bib entry missing title field; several author mismatches in citations\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers flagged. deepseek-r1-2025, snapkv-neurips2024, unicomp-2026 have author field discrepancies.\"\n    action_items:\n      - round: 1\n        action: \"Fix h2o bib entry; verify canonical author info for flagged entries\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-6\"\n    summary: \"s=0.35 supplementary experiment mentioned in Appendix D but not fully reported (no table, CI, or test)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree: either report fully or remove.\"\n    action_items:\n      - round: 1\n        action: \"Provide full s=0.35 results or remove the mention\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-Minor-code\"\n    summary: \"No code or data release plan mentioned — impacts reproducibility\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers noted. KV importance position normalization and phase segmentation merge logic hard to reproduce from text alone.\"\n    action_items:\n      - round: 1\n        action: \"Add code/data availability statement; consider anonymous repo for review\"\n        assigned_to: \"\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-15T07:47:46.461632+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml\", \"bytes\": 12563}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-15T07:49:59.751657+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "report": "\n# 圆桌审稿报告 — Round 1\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n**Venue**: EMNLP 2026 ARR (Main Conference)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）\n**轮次**: Round 1（独立审稿 + 交叉分享完成，达成收敛）\n\n---\n\n## Summary\n\n本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）在 reasoning model 生成过程中的 phase-dependent severity。核心发现：在 importance-based eviction 下，compound interaction 的严重程度（以 Interaction Index 衡量）集中在 low-sparsity reasoning phases，severity gradient 从 69× (s=0.15) 增长到 274× (s=0.30)；random eviction 无此现象（7/8 conditions non-significant）。在 Qwen2.5-7B-Instruct 上部分复现（s≥0.20），在 LlamaForCausalLM 上仅获得微弱方向性一致证据。提出 entropy-discrimination collapse 作为机制解释。\n\n---\n\n## Strengths\n\n**S1** [consensus] **研究问题有价值且定义清晰**。将 compound sparsity 的 phase-invariance assumption 作为明确攻击目标，对 efficient inference 部署有直接指导意义。\n\n**S2** [consensus] **统计方法论严谨**。非参数 bootstrap (B=10,000)、paired permutation tests、Bonferroni correction、Cohen's d_z、报告中位数处理右偏分布——统计意识优于绝大多数 ML 论文。\n\n**S3** [consensus] **Random eviction 作为 falsification control 设计巧妙**。7/8 conditions 下 random eviction 无显著 phase gradient，有效隔离了 strategy-specific amplification，构成强 counterfactual。\n\n**S4** [consensus] **Crossover 发现有 non-trivial insight**。§5.3 的 strategy ranking reversal（importance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）对部署有直接启示——uniform budget 必然在某个 phase 是 suboptimal 的。\n\n**S5** [consensus] **Multiplicative null verification** (Appendix A) 增强了 Interaction Index 定义的鲁棒性。\n\n**S6** [consensus] **Limitations 写作坦诚**，多数局限在 limitations section 中有诚实讨论。\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, consensus R1+R2] **论文严重未完成：40+ placeholders 未填充**\n- Abstract 中 Qwen random s=0.30 的 Δ̃ 值缺失\n- Table 4（LLaMA cross-architecture validation, §5.5）整表 16 个数据 cell 全部空白\n- §5.4 cross-model: NULL_PCT、N_LLAMA 未填\n- §7 Discussion: oracle pilot experiment 4 个关键指标（ORACLE_PCT、ORACLE_P、HEUR_PCT、HEUR_P）全部缺失\n- Appendix: Qwen effective-n table 12 cells 空白、per-problem concordance ρ/p 未填（尽管 LaTeX 注释中有数据）、多处 LLaMA random p-value 缺失\n- **影响**：Table 4 是本文最重要的 generalization 证据，Discussion 中的 oracle pilot 是唯一从 characterization 走向 actionable mitigation 的部分——两者的核心数据全部缺失。论文以当前状态提交将被视为 incomplete submission，无法进入实质性审稿。\n\n**MF2** [critical, consensus R1+R2] **Cross-architecture 证据薄弱且 overclaim**\n- LLaMA 绝对 magnitude 仅为 DeepSeek 的 ~1/40、Qwen 的 ~1/7\n- 4 个 sparsity levels 中仅 s=0.30 的 Bonferroni-corrected Wilcoxon 达显著 (p=0.029)\n- 统计指标自相矛盾：s=0.15 时 CI 排除零但 Wilcoxon NS；s=0.30 时 CI 跨零但 Wilcoxon significant\n- Random eviction 在 LLaMA 上也展现 non-trivial phase gradient，严重削弱 strategy-specificity claim\n- Table 4 完全空白，上述数字仅来自文本叙述\n- **Overclaim 位置**：Title \"Reasoning Models\"（复数暗示广泛适用）；Abstract line 10 \"directionally consistent evidence for cross-architecture generalization\"；Contribution 2 \"replicates across three models spanning two architectures\"\n- **建议**：将 LLaMA 降级为 exploratory supplement；Title/Abstract/Contribution 使用 \"suggestive\" 或 \"preliminary\" 等限定词\n\n**MF3** [critical, consensus R1+R2] **单一 benchmark (MATH-500) 严重限制泛化性**\n- 仅测试数学推理，Title/Abstract 使用 \"Reasoning Models\" 的一般性表述\n- 不同推理任务（code generation、multi-hop QA）会产生完全不同的 attention phase structure\n- 作为以 \"characterization\" 为核心贡献的论文，characterization 的范围直接决定贡献大小\n- **建议**：至少添加一个非数学推理 benchmark，或在 Title/Abstract 中明确限定为 \"mathematical reasoning\"\n\n**MF4** [critical R1 / should-fix R2, consolidated: critical] **50 题样本量缺乏 power analysis**\n- 从 MATH-500 中仅抽取 50 题（10% 采样率），无事先 power analysis\n- 分层方案（stratified sampling）未报告各层样本量\n- 有效样本因排除进一步减少：DS n=49、QW n=46、LLaMA n=49\n- Qwen s=0.15 的 d_z=0.28 且 CI 包含零，可能是 underpowered 的表现\n- R2 指出 paired design 提供 power advantage，DeepSeek 主结论统计充分（所有 p_Bonf < 0.005）——power 疑虑主要限于 Qwen 低 sparsity 和 LLaMA 全局\n- **建议**：报告 post-hoc power analysis；解释为何不用全部 500 题；在 Methodology 中完整报告排除标准\n\n**MF5** [critical R1 / should-fix R2, consolidated: should-fix→critical borderline] **机制分析（entropy-discrimination collapse）纯 correlational**\n- 无 causal intervention（如固定 entropy 水平观察 II 变化）\n- Entropy redistribution 在 Qwen s=0.25 出现符号反转（ΔH = +0.045，22/30 problems 熵增），paper 称 \"secondary model-dependent amplifier\" 但这实质是 ad hoc 解释\n- Analysis 叙述偏 causal（\"head pruning flattens...\"、\"degrading the discriminative power...\"）但证据仅 correlational\n- **缓解因素**（R2 指出）：论文已使用 hedged language (\"We propose...as the primary mechanism\")；Gini coefficient 在 16/16 conditions 一致为负；random eviction immunity 构成 partial counterfactual\n- **建议**：§6 标题和叙述改为更 hedged 的表述；至少标注 \"correlational evidence\"；如条件允许设计一个 causal experiment\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, consensus] **Phase segmentation (tercile-based) 缺乏充分论证**\n- ThinKV 使用 explicit `&lt;think>` delimiters，本文使用 attention sparsity quantile tercile——方法论完全不同但论文称 \"following ThinKV\"\n- 强制将每个 sequence 分为三等份，即使 attention sparsity 是 unimodal 的\n- 为什么用 3 phases 而非 4 或 5？min_phase_length=10 依据？无 sensitivity analysis\n- **建议**：修正 ThinKV 引用措辞；添加 segmentation sensitivity analysis\n\n**SF2** [warning, consensus] **G 的数值稳定性问题**\n- 当 II_high ≈ 0.006 (s=0.15) 时，G 对分母微小波动极敏感\n- G 的 bootstrap CI 未报告，可能在 [33, 133] 范围（vs point estimate 69）\n- **建议**：报告 G 的 CI；用 Δ 作主指标，G 降级为辅助\n\n**SF3** [warning, consensus] **Bonferroni 校正范围 (k=4) 可能不足**\n- 实际 test 数远多于 4：2 strategies × 4 sparsity × 3 models × multiple test types\n- Family-wise error rate 可能被低估\n- **建议**：论证 k=4 的 family 划分依据，或采用 FDR\n\n**SF4** [warning, R2 critical → R1 rebuts → consolidated warning] **与 HIES (2025) 区分不充分**\n- HIES 已报告 single-axis head discrimination collapse under heavy pruning\n- Related Work 仅一句话提及，Analysis §6 完全未讨论两者区别\n- R1 指出关键 delta：HIES 是 single-axis，本文 extend 到 compound + phase-dependent setting（crossover 现象是 HIES 框架中不存在的 prediction）——novelty 有清晰区分，但论文未充分展示这一区分\n- **建议**：在 Related Work 和 Analysis 中添加 explicit comparison\n\n**SF5** [warning, consensus] **Symmetric sparsity assumption 的实践代表性**\n- 实际部署中两轴 budget 通常不同\n- **建议**：讨论局限或提供 1-2 个 asymmetric spot check\n\n**SF6** [warning, consensus] **Spearman ρ=1.0 on 4 points 被 over-interpret**\n- 4 个数据点的 exact permutation p = 0.042，barely significant\n- 未注明 sample size，读者可能误以为高 power 证据\n- Table 1 (segment-level Δ) vs Table 4 (problem-level paired Δ̃) 数字差异未解释\n- **建议**：标注 sample size caveat；在 caption 解释两表差异\n\n**SF7** [warning, consensus] **排除标准未在 Methodology 中说明**\n- DS 50→49 排除原因未提及；QW 50→46 仅在 Appendix 解释\n- **建议**：在 §4 中完整报告\n\n**SF8** [warning, partial consensus] **Related Work 可能遗漏 RLKV、LongFlow、PM-KVQ**\n- R2 列出遗漏；R1 同意但指出需确认这些工作是否涉及 compound interaction 或 phase-dependent effects\n- **建议**：评估相关性后补充直接相关引用\n\n**SF9** [warning, consensus] **Abstract 过长过密**\n- 14 行含 10+ 统计数字，可读性差\n- LLaMA 详细统计量（Δ̃、p_Bonf）属于 Results 而非 Abstract\n- **建议**：精简到核心 claim + 1-2 headline numbers\n\n### Info 级别\n\n- **h2o-neurips2023** bib entry 缺 title 字段；deepseek-r1-2025、snapkv-neurips2024、unicomp-2026 author 信息有偏差\n- LaTeX source 中 **REVIEWER-ATTACK/REBUTTAL** 注释应在提交前删除（ARR 某些情况下可下载源码）\n- **s=0.35 supplementary experiment** (Appendix D) 仅一句话提及无完整数据——要么报告完整要么删除\n- 无 **代码/数据开源** 声明，影响 reproducibility\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 **[AGREE]**：\n1. Placeholder 未填充是 showstopper（MF1）\n2. Cross-architecture LLaMA 证据不支撑当前 framing（MF2）\n3. 单一 benchmark 限制泛化（MF3）\n4. Phase segmentation 需 sensitivity analysis（SF1）\n5. G 数值不稳定（SF2）\n6. Bonferroni scope 偏窄（SF3）\n7. Abstract 过密（SF9）\n8. 排除标准未说明（SF7）\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 合并判定 |\n|------|----|----|----------|\n| Sample size power (MF4) | critical | should-fix (paired design power) | critical（缺 power analysis 本身是方法论缺陷） |\n| Mechanism causality (MF5) | critical | should-fix (hedged language, 16/16 consistent) | critical borderline（降级叙述 assertiveness 后可降为 warning） |\n| HIES novelty overlap (SF4) | should-fix | critical | warning（有清晰 delta 但讨论不充分） |\n| Empirical finding venue fit | N/A | W1 warning | dismissed（R1 rebuts: ACL/EMNLP 接受高质量 empirical finding） |\n| REVIEWER-ATTACK comments | optional cleanup | should-clean | info |\n\n---\n\n## Questions for Authors\n\n1. Table 4 的所有 placeholder 何时能填充？如果 LLaMA 实验数据已有但未整理完，建议在 resubmission 时完整报告。如果实验尚未完成，建议删除 Section 5.5 并降低 cross-architecture claim。\n2. 能否提供 HIES (2025) single-axis discrimination collapse 与本文 compound + phase-dependent collapse 的 explicit comparison？HIES 是否观察到 phase-dependent discrimination loss？\n3. 为什么只用 50/500 题？在全部 500 题上运行一个 configuration 的 GPU 时间成本是多少？\n4. Phase segmentation 对结果的敏感性：如果改用 quartile 或 quintile 分割，main findings 是否 robust？\n5. LLaMA 上 random eviction 也展现 non-trivial phase gradient——这是否意味着在某些架构上 phase modulation 不是 strategy-specific 而是 compound sparsity 的 inherent property？\n6. Qwen s=0.25 entropy 反转（ΔH = +0.045）与该 sparsity level 的 severity gradient 有无 quantitative 关联？\n7. Oracle pilot experiment（Discussion）是否已执行？如果已执行且 below gate，为什么不填入数据？\n8. 是否计划开源代码和实验数据？\n\n---\n\n## Missing References\n\nR2 指出以下可能遗漏的近期相关工作（R1 同意需评估相关性）：\n- **RLKV** (OpenReview 2026): RL 优化 per-head cache + reasoning quality\n- **LongFlow** (arXiv 2603.11504): reasoning model long-output KV cache compression\n- **PM-KVQ** (OpenReview 2026): Progressive mixed-precision KV cache quantization for long-CoT\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目无 `external_review.paperreview_ai.enabled` 设置）。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Reject (2.5/5)**\n**置信度: 4/5**（两位 Reviewer 均具备 KV cache compression + 统计方法背景，交叉验证后达成高度共识）\n\n论文提出了一个有价值的 empirical finding——compound sparsity severity 的 phase-strategy interaction——统计方法论优于多数 ML 论文，random eviction 作为 falsification control 设计巧妙。DeepSeek 上的主实验结果可信且有部署启示。\n\n但当前论文有**实质性缺陷**阻碍接收：\n1. **论文未完成**：40+ placeholders 包括核心 Table 和 Abstract，以此状态提交将被 desk reject\n2. **Cross-architecture generalization 被 overclaim**：LLaMA 证据极弱（1/4 significant, ~1/40 magnitude, random eviction 也有 phase gradient），不支撑 Title/Abstract 的 framing\n3. **泛化范围过窄**：50 题 MATH-500，无 power analysis，无其他 reasoning benchmark\n4. **机制分析 correlational only**：entropy-discrimination collapse 在 Qwen 上仅部分 replicate\n\n如果 (1) 填充所有数据并确认 cross-arch 结论、(2) 诚实限定 claim scope、(3) 补充 power analysis 和 segmentation sensitivity——论文有潜力达到 borderline accept / Findings track。当前状态建议 revise and resubmit。\n\n---\n\n## Detailed Comments\n\n### Per-Section Notes\n\n**Abstract**: 过密（14 行 10+ 统计量）；LLaMA 细节应移至 Results；至少一处 placeholder 未填。\n\n**§1 Introduction**: Contribution 2 \"replicates across three models spanning two architectures\" 需降级措辞。整体写作清晰。\n\n**§2 Related Work**: 对 HIES (2025) 讨论严重不足——一句话提及但未在 Analysis 中对比。可能遗漏 RLKV/LongFlow/PM-KVQ。\n\n**§3 Background**: G 定义在 II_high → 0 时数值不稳定，需 CI 或降级为辅助指标。Phase segmentation 引用 ThinKV 但方法不同，需修正措辞。\n\n**§4 Methodology**: 缺 power analysis；排除标准未报告；symmetric sparsity 假设未讨论；sampling 分层方案缺失。\n\n**§5 Results**: Table 1-2 (DeepSeek) 可信；Table 3 (LLaMA) 完全空白；Spearman ρ=1.0 on 4 points 被 over-interpret；Table 1 vs Table 4 数字差异未解释。\n\n**§6 Analysis**: \"Entropy-Discrimination Collapse\" 标题过于 assertive for correlational evidence；Qwen s=0.25 entropy reversal 的 \"model-dependent amplifier\" 解释 ad hoc；需与 HIES 做 explicit comparison。\n\n**§7 Discussion**: Oracle pilot experiment 数据全部为 placeholder——这是论文唯一走向 actionable mitigation 的部分，缺失严重影响 impact。LLaMA architecture-dependent 讨论诚实但与 title/abstract framing 矛盾。\n\n**Limitations**: 坦诚且全面，但 LaTeX 注释中的 REVIEWER-ATTACK/REBUTTAL 预设回应应删除。\n\n**Appendix**: Multiplicative null verification (A) 是加分项；其余 appendix 有大量 placeholder。s=0.35 实验仅一句话提及。\n\n**References**: 29 篇引用均为真实论文，无幻觉引用。h2o-neurips2023 缺 title 字段；3 篇 author mismatch。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "report": "\n# 圆桌审稿报告 — Round 1\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n**Venue**: EMNLP 2026 ARR (Main Conference)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）\n**轮次**: Round 1（独立审稿 + 交叉分享完成，达成收敛）\n\n---\n\n## Summary\n\n本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）在 reasoning model 生成过程中的 phase-dependent severity。核心发现：在 importance-based eviction 下，compound interaction 的严重程度（以 Interaction Index 衡量）集中在 low-sparsity reasoning phases，severity gradient 从 69× (s=0.15) 增长到 274× (s=0.30)；random eviction 无此现象（7/8 conditions non-significant）。在 Qwen2.5-7B-Instruct 上部分复现（s≥0.20），在 LlamaForCausalLM 上仅获得微弱方向性一致证据。提出 entropy-discrimination collapse 作为机制解释。\n\n---\n\n## Strengths\n\n**S1** [consensus] **研究问题有价值且定义清晰**。将 compound sparsity 的 phase-invariance assumption 作为明确攻击目标，对 efficient inference 部署有直接指导意义。\n\n**S2** [consensus] **统计方法论严谨**。非参数 bootstrap (B=10,000)、paired permutation tests、Bonferroni correction、Cohen's d_z、报告中位数处理右偏分布——统计意识优于绝大多数 ML 论文。\n\n**S3** [consensus] **Random eviction 作为 falsification control 设计巧妙**。7/8 conditions 下 random eviction 无显著 phase gradient，有效隔离了 strategy-specific amplification，构成强 counterfactual。\n\n**S4** [consensus] **Crossover 发现有 non-trivial insight**。§5.3 的 strategy ranking reversal（importance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）对部署有直接启示——uniform budget 必然在某个 phase 是 suboptimal 的。\n\n**S5** [consensus] **Multiplicative null verification** (Appendix A) 增强了 Interaction Index 定义的鲁棒性。\n\n**S6** [consensus] **Limitations 写作坦诚**，多数局限在 limitations section 中有诚实讨论。\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, consensus R1+R2] **论文严重未完成：40+ placeholders 未填充**\n- Abstract 中 Qwen random s=0.30 的 Δ̃ 值缺失\n- Table 4（LLaMA cross-architecture validation, §5.5）整表 16 个数据 cell 全部空白\n- §5.4 cross-model: NULL_PCT、N_LLAMA 未填\n- §7 Discussion: oracle pilot experiment 4 个关键指标（ORACLE_PCT、ORACLE_P、HEUR_PCT、HEUR_P）全部缺失\n- Appendix: Qwen effective-n table 12 cells 空白、per-problem concordance ρ/p 未填（尽管 LaTeX 注释中有数据）、多处 LLaMA random p-value 缺失\n- **影响**：Table 4 是本文最重要的 generalization 证据，Discussion 中的 oracle pilot 是唯一从 characterization 走向 actionable mitigation 的部分——两者的核心数据全部缺失。论文以当前状态提交将被视为 incomplete submission，无法进入实质性审稿。\n\n**MF2** [critical, consensus R1+R2] **Cross-architecture 证据薄弱且 overclaim**\n- LLaMA 绝对 magnitude 仅为 DeepSeek 的 ~1/40、Qwen 的 ~1/7\n- 4 个 sparsity levels 中仅 s=0.30 的 Bonferroni-corrected Wilcoxon 达显著 (p=0.029)\n- 统计指标自相矛盾：s=0.15 时 CI 排除零但 Wilcoxon NS；s=0.30 时 CI 跨零但 Wilcoxon significant\n- Random eviction 在 LLaMA 上也展现 non-trivial phase gradient，严重削弱 strategy-specificity claim\n- Table 4 完全空白，上述数字仅来自文本叙述\n- **Overclaim 位置**：Title \"Reasoning Models\"（复数暗示广泛适用）；Abstract line 10 \"directionally consistent evidence for cross-architecture generalization\"；Contribution 2 \"replicates across three models spanning two architectures\"\n- **建议**：将 LLaMA 降级为 exploratory supplement；Title/Abstract/Contribution 使用 \"suggestive\" 或 \"preliminary\" 等限定词\n\n**MF3** [critical, consensus R1+R2] **单一 benchmark (MATH-500) 严重限制泛化性**\n- 仅测试数学推理，Title/Abstract 使用 \"Reasoning Models\" 的一般性表述\n- 不同推理任务（code generation、multi-hop QA）会产生完全不同的 attention phase structure\n- 作为以 \"characterization\" 为核心贡献的论文，characterization 的范围直接决定贡献大小\n- **建议**：至少添加一个非数学推理 benchmark，或在 Title/Abstract 中明确限定为 \"mathematical reasoning\"\n\n**MF4** [critical R1 / should-fix R2, consolidated: critical] **50 题样本量缺乏 power analysis**\n- 从 MATH-500 中仅抽取 50 题（10% 采样率），无事先 power analysis\n- 分层方案（stratified sampling）未报告各层样本量\n- 有效样本因排除进一步减少：DS n=49、QW n=46、LLaMA n=49\n- Qwen s=0.15 的 d_z=0.28 且 CI 包含零，可能是 underpowered 的表现\n- R2 指出 paired design 提供 power advantage，DeepSeek 主结论统计充分（所有 p_Bonf < 0.005）——power 疑虑主要限于 Qwen 低 sparsity 和 LLaMA 全局\n- **建议**：报告 post-hoc power analysis；解释为何不用全部 500 题；在 Methodology 中完整报告排除标准\n\n**MF5** [critical R1 / should-fix R2, consolidated: should-fix→critical borderline] **机制分析（entropy-discrimination collapse）纯 correlational**\n- 无 causal intervention（如固定 entropy 水平观察 II 变化）\n- Entropy redistribution 在 Qwen s=0.25 出现符号反转（ΔH = +0.045，22/30 problems 熵增），paper 称 \"secondary model-dependent amplifier\" 但这实质是 ad hoc 解释\n- Analysis 叙述偏 causal（\"head pruning flattens...\"、\"degrading the discriminative power...\"）但证据仅 correlational\n- **缓解因素**（R2 指出）：论文已使用 hedged language (\"We propose...as the primary mechanism\")；Gini coefficient 在 16/16 conditions 一致为负；random eviction immunity 构成 partial counterfactual\n- **建议**：§6 标题和叙述改为更 hedged 的表述；至少标注 \"correlational evidence\"；如条件允许设计一个 causal experiment\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, consensus] **Phase segmentation (tercile-based) 缺乏充分论证**\n- ThinKV 使用 explicit `&lt;think>` delimiters，本文使用 attention sparsity quantile tercile——方法论完全不同但论文称 \"following ThinKV\"\n- 强制将每个 sequence 分为三等份，即使 attention sparsity 是 unimodal 的\n- 为什么用 3 phases 而非 4 或 5？min_phase_length=10 依据？无 sensitivity analysis\n- **建议**：修正 ThinKV 引用措辞；添加 segmentation sensitivity analysis\n\n**SF2** [warning, consensus] **G 的数值稳定性问题**\n- 当 II_high ≈ 0.006 (s=0.15) 时，G 对分母微小波动极敏感\n- G 的 bootstrap CI 未报告，可能在 [33, 133] 范围（vs point estimate 69）\n- **建议**：报告 G 的 CI；用 Δ 作主指标，G 降级为辅助\n\n**SF3** [warning, consensus] **Bonferroni 校正范围 (k=4) 可能不足**\n- 实际 test 数远多于 4：2 strategies × 4 sparsity × 3 models × multiple test types\n- Family-wise error rate 可能被低估\n- **建议**：论证 k=4 的 family 划分依据，或采用 FDR\n\n**SF4** [warning, R2 critical → R1 rebuts → consolidated warning] **与 HIES (2025) 区分不充分**\n- HIES 已报告 single-axis head discrimination collapse under heavy pruning\n- Related Work 仅一句话提及，Analysis §6 完全未讨论两者区别\n- R1 指出关键 delta：HIES 是 single-axis，本文 extend 到 compound + phase-dependent setting（crossover 现象是 HIES 框架中不存在的 prediction）——novelty 有清晰区分，但论文未充分展示这一区分\n- **建议**：在 Related Work 和 Analysis 中添加 explicit comparison\n\n**SF5** [warning, consensus] **Symmetric sparsity assumption 的实践代表性**\n- 实际部署中两轴 budget 通常不同\n- **建议**：讨论局限或提供 1-2 个 asymmetric spot check\n\n**SF6** [warning, consensus] **Spearman ρ=1.0 on 4 points 被 over-interpret**\n- 4 个数据点的 exact permutation p = 0.042，barely significant\n- 未注明 sample size，读者可能误以为高 power 证据\n- Table 1 (segment-level Δ) vs Table 4 (problem-level paired Δ̃) 数字差异未解释\n- **建议**：标注 sample size caveat；在 caption 解释两表差异\n\n**SF7** [warning, consensus] **排除标准未在 Methodology 中说明**\n- DS 50→49 排除原因未提及；QW 50→46 仅在 Appendix 解释\n- **建议**：在 §4 中完整报告\n\n**SF8** [warning, partial consensus] **Related Work 可能遗漏 RLKV、LongFlow、PM-KVQ**\n- R2 列出遗漏；R1 同意但指出需确认这些工作是否涉及 compound interaction 或 phase-dependent effects\n- **建议**：评估相关性后补充直接相关引用\n\n**SF9** [warning, consensus] **Abstract 过长过密**\n- 14 行含 10+ 统计数字，可读性差\n- LLaMA 详细统计量（Δ̃、p_Bonf）属于 Results 而非 Abstract\n- **建议**：精简到核心 claim + 1-2 headline numbers\n\n### Info 级别\n\n- **h2o-neurips2023** bib entry 缺 title 字段；deepseek-r1-2025、snapkv-neurips2024、unicomp-2026 author 信息有偏差\n- LaTeX source 中 **REVIEWER-ATTACK/REBUTTAL** 注释应在提交前删除（ARR 某些情况下可下载源码）\n- **s=0.35 supplementary experiment** (Appendix D) 仅一句话提及无完整数据——要么报告完整要么删除\n- 无 **代码/数据开源** 声明，影响 reproducibility\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 **[AGREE]**：\n1. Placeholder 未填充是 showstopper（MF1）\n2. Cross-architecture LLaMA 证据不支撑当前 framing（MF2）\n3. 单一 benchmark 限制泛化（MF3）\n4. Phase segmentation 需 sensitivity analysis（SF1）\n5. G 数值不稳定（SF2）\n6. Bonferroni scope 偏窄（SF3）\n7. Abstract 过密（SF9）\n8. 排除标准未说明（SF7）\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 合并判定 |\n|------|----|----|----------|\n| Sample size power (MF4) | critical | should-fix (paired design power) | critical（缺 power analysis 本身是方法论缺陷） |\n| Mechanism causality (MF5) | critical | should-fix (hedged language, 16/16 consistent) | critical borderline（降级叙述 assertiveness 后可降为 warning） |\n| HIES novelty overlap (SF4) | should-fix | critical | warning（有清晰 delta 但讨论不充分） |\n| Empirical finding venue fit | N/A | W1 warning | dismissed（R1 rebuts: ACL/EMNLP 接受高质量 empirical finding） |\n| REVIEWER-ATTACK comments | optional cleanup | should-clean | info |\n\n---\n\n## Questions for Authors\n\n1. Table 4 的所有 placeholder 何时能填充？如果 LLaMA 实验数据已有但未整理完，建议在 resubmission 时完整报告。如果实验尚未完成，建议删除 Section 5.5 并降低 cross-architecture claim。\n2. 能否提供 HIES (2025) single-axis discrimination collapse 与本文 compound + phase-dependent collapse 的 explicit comparison？HIES 是否观察到 phase-dependent discrimination loss？\n3. 为什么只用 50/500 题？在全部 500 题上运行一个 configuration 的 GPU 时间成本是多少？\n4. Phase segmentation 对结果的敏感性：如果改用 quartile 或 quintile 分割，main findings 是否 robust？\n5. LLaMA 上 random eviction 也展现 non-trivial phase gradient——这是否意味着在某些架构上 phase modulation 不是 strategy-specific 而是 compound sparsity 的 inherent property？\n6. Qwen s=0.25 entropy 反转（ΔH = +0.045）与该 sparsity level 的 severity gradient 有无 quantitative 关联？\n7. Oracle pilot experiment（Discussion）是否已执行？如果已执行且 below gate，为什么不填入数据？\n8. 是否计划开源代码和实验数据？\n\n---\n\n## Missing References\n\nR2 指出以下可能遗漏的近期相关工作（R1 同意需评估相关性）：\n- **RLKV** (OpenReview 2026): RL 优化 per-head cache + reasoning quality\n- **LongFlow** (arXiv 2603.11504): reasoning model long-output KV cache compression\n- **PM-KVQ** (OpenReview 2026): Progressive mixed-precision KV cache quantization for long-CoT\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目无 `external_review.paperreview_ai.enabled` 设置）。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Reject (2.5/5)**\n**置信度: 4/5**（两位 Reviewer 均具备 KV cache compression + 统计方法背景，交叉验证后达成高度共识）\n\n论文提出了一个有价值的 empirical finding——compound sparsity severity 的 phase-strategy interaction——统计方法论优于多数 ML 论文，random eviction 作为 falsification control 设计巧妙。DeepSeek 上的主实验结果可信且有部署启示。\n\n但当前论文有**实质性缺陷**阻碍接收：\n1. **论文未完成**：40+ placeholders 包括核心 Table 和 Abstract，以此状态提交将被 desk reject\n2. **Cross-architecture generalization 被 overclaim**：LLaMA 证据极弱（1/4 significant, ~1/40 magnitude, random eviction 也有 phase gradient），不支撑 Title/Abstract 的 framing\n3. **泛化范围过窄**：50 题 MATH-500，无 power analysis，无其他 reasoning benchmark\n4. **机制分析 correlational only**：entropy-discrimination collapse 在 Qwen 上仅部分 replicate\n\n如果 (1) 填充所有数据并确认 cross-arch 结论、(2) 诚实限定 claim scope、(3) 补充 power analysis 和 segmentation sensitivity——论文有潜力达到 borderline accept / Findings track。当前状态建议 revise and resubmit。\n\n---\n\n## Detailed Comments\n\n### Per-Section Notes\n\n**Abstract**: 过密（14 行 10+ 统计量）；LLaMA 细节应移至 Results；至少一处 placeholder 未填。\n\n**§1 Introduction**: Contribution 2 \"replicates across three models spanning two architectures\" 需降级措辞。整体写作清晰。\n\n**§2 Related Work**: 对 HIES (2025) 讨论严重不足——一句话提及但未在 Analysis 中对比。可能遗漏 RLKV/LongFlow/PM-KVQ。\n\n**§3 Background**: G 定义在 II_high → 0 时数值不稳定，需 CI 或降级为辅助指标。Phase segmentation 引用 ThinKV 但方法不同，需修正措辞。\n\n**§4 Methodology**: 缺 power analysis；排除标准未报告；symmetric sparsity 假设未讨论；sampling 分层方案缺失。\n\n**§5 Results**: Table 1-2 (DeepSeek) 可信；Table 3 (LLaMA) 完全空白；Spearman ρ=1.0 on 4 points 被 over-interpret；Table 1 vs Table 4 数字差异未解释。\n\n**§6 Analysis**: \"Entropy-Discrimination Collapse\" 标题过于 assertive for correlational evidence；Qwen s=0.25 entropy reversal 的 \"model-dependent amplifier\" 解释 ad hoc；需与 HIES 做 explicit comparison。\n\n**§7 Discussion**: Oracle pilot experiment 数据全部为 placeholder——这是论文唯一走向 actionable mitigation 的部分，缺失严重影响 impact。LLaMA architecture-dependent 讨论诚实但与 title/abstract framing 矛盾。\n\n**Limitations**: 坦诚且全面，但 LaTeX 注释中的 REVIEWER-ATTACK/REBUTTAL 预设回应应删除。\n\n**Appendix**: Multiplicative null verification (A) 是加分项；其余 appendix 有大量 placeholder。s=0.35 实验仅一句话提及。\n\n**References**: 29 篇引用均为真实论文，无幻觉引用。h2o-neurips2023 缺 title 字段；3 篇 author mismatch。\n"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-15T07:50:04.719988+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_fdc656be1c7fe17c11ab639cdbce3710:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4968
}
```

</details>

---


### Assistant

_source line 250 · 2026-05-15T07:50:13.242840+00:00_

审稿完成。

**圆桌审稿报告已投递至 Research Director。**

汇总结论：

- **评分：Weak Reject (2.5/5)**，置信度 4/5
- **R1 评分 2.5/5，R2 评分 2.5/5**，交叉分享后在核心问题上高度收敛
- **5 项 Must-Fix**：(1) 40+ placeholders 未填充含核心 Table 4 全空；(2) LLaMA cross-arch 证据 overclaim；(3) 单一 benchmark；(4) 缺 power analysis；(5) 机制分析纯 correlational
- **9 项 Should-Fix**：phase segmentation sensitivity、G 数值稳定性、Bonferroni scope、HIES 区分、symmetric sparsity、Spearman over-interpretation、排除标准、Related Work 遗漏、Abstract 过密
- **Issue Tracker** 已同步更新至 `review_issues.yaml`（18 条 issue）

如果填充所有数据、诚实限定 claim scope、补充 power analysis 和 segmentation sensitivity，论文有潜力达到 borderline accept / Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 251 · 2026-05-15T07:50:16.029166+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

与 R1 在大部分问题上达成共识，但在两点上给出了不同 severity 评级：(1) 样本量问题——paired design 提供了额外 power，主结论在 DeepSeek 上统计充分，降级为 should-fix；(2) 机制 causality——论文已用审慎措辞且有 16/16 一致的 correlational evidence，降级为 should-fix。两位 reviewer 一致认为 placeholders 未填充、cross-architecture overclaim、单一 benchmark 是最关键的三个问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 252 · 2026-05-15T07:50:28.516950+00:00_

审稿报告和 Issue Tracker 均已在收到 R1 交叉回应后完成提交（Weak Reject, 2.5/5）。R2 的交叉回应结论与已提交报告中记录的分歧完全一致，无需修订。

**本轮圆桌审稿已完成。**

汇总：
- **评分**：Weak Reject (2.5/5)，置信度 4/5
- **5 项 Must-Fix**：(1) 40+ placeholders 未填充，(2) cross-architecture overclaim，(3) 单一 benchmark，(4) 缺 power analysis，(5) 机制分析 correlational only
- **9 项 Should-Fix**：segmentation sensitivity、G 稳定性、Bonferroni scope、HIES 区分、symmetric sparsity、Spearman over-interpretation、排除标准、Related Work 遗漏、Abstract 过密
- **18 条 issue 已写入 `review_issues.yaml`** 供后续修订轮次追踪
- 报告已投递至 Research Director

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 20

## Round 20

64 recorded events


### User

_source line 253 · 2026-05-15T10:50:33.547580+00:00_

[Round 5 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/phase-gated-compound-sparse/artifacts/review_reports/round_4.md`
跨轮次问题追踪: `projects/phase-gated-compound-sparse/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: phase-gated-compound-sparse
- 论文路径: projects/phase-gated-compound-sparse/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-06-15

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-15T10:50:44.751690+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-15T10:50:44.752226+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-15T10:50:48.573735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_reports/round_4.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_reports/round_4.md"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-15T10:50:49.378329+00:00_

1	---
2	round: 4
3	overall_score: weak reject
4	timestamp: 2026-05-15T07:49:59.758091+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	
11	# 圆桌审稿报告 — Round 1
12	
13	**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
14	**Venue**: EMNLP 2026 ARR (Main Conference)
15	**截止日期**: 2026-05-25
16	**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）
17	**轮次**: Round 1（独立审稿 + 交叉分享完成，达成收敛）
18	
19	---
20	
21	## Summary
22	
23	本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）在 reasoning model 生成过程中的 phase-dependent severity。核心发现：在 importance-based eviction 下，compound interaction 的严重程度（以 Interaction Index 衡量）集中在 low-sparsity reasoning phases，severity gradient 从 69× (s=0.15) 增长到 274× (s=0.30)；random eviction 无此现象（7/8 conditions non-significant）。在 Qwen2.5-7B-Instruct 上部分复现（s≥0.20），在 LlamaForCausalLM 上仅获得微弱方向性一致证据。提出 entropy-discrimination collapse 作为机制解释。
24	
25	---
26	
27	## Strengths
28	
29	**S1** [consensus] **研究问题有价值且定义清晰**。将 compound sparsity 的 phase-invariance assumption 作为明确攻击目标，对 efficient inference 部署有直接指导意义。
30	
31	**S2** [consensus] **统计方法论严谨**。非参数 bootstrap (B=10,000)、paired permutation tests、Bonferroni correction、Cohen's d_z、报告中位数处理右偏分布——统计意识优于绝大多数 ML 论文。
32	
33	**S3** [consensus] **Random eviction 作为 falsification control 设计巧妙**。7/8 conditions 下 random eviction 无显著 phase gradient，有效隔离了 strategy-specific amplification，构成强 counterfactual。
34	
35	**S4** [consensus] **Crossover 发现有 non-trivial insight**。§5.3 的 strategy ranking reversal（importance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）对部署有直接启示——uniform budget 必然在某个 phase 是 suboptimal 的。
36	
37	**S5** [consensus] **Multiplicative null verification** (Appendix A) 增强了 Interaction Index 定义的鲁棒性。
38	
39	**S6** [consensus] **Limitations 写作坦诚**，多数局限在 limitations section 中有诚实讨论。
40	
41	---
42	
43	## Weaknesses（按严重性排序）
44	
45	### Must-Fix（影响接收决定）
46	
47	**MF1** [critical, consensus
…[truncated 10254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-15T10:50:49.629727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-15T10:50:49.680950+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "40+ placeholders unfilled — paper not submission-ready (Table 4 entirely empty, Discussion oracle data missing, Abstract incomplete)"
4	    category: experiment
5	    severity: critical
6	    status: in_progress
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2]
12	        note: "Both reviewers independently flagged as #1 critical issue."
13	    action_items:
14	      - round: 1
15	        action: "n=500 analysis complete → Paper Agent fills all placeholders (Table 4, Abstract, §5.4, §7 oracle, Appendix). CSV export bug (DS s030 missing) must be fixed first."
16	        assigned_to: "main_agent → paper_agent"
17	        status: in_progress
18	    resolution: ""
19	    resolution_round: null
20	
21	  - id: "R1-N4"
22	    summary: "Cross-architecture (LLaMA) evidence too weak to support title/abstract framing — 1/4 conditions significant, ~1/40 magnitude, random eviction also shows phase gradient"
23	    category: framing
24	    severity: critical
25	    status: in_progress
26	    first_raised_round: 1
27	    last_seen_round: 1
28	    mentions:
29	      - round: 1
30	        reviewers: [1, 2]
31	        note: "R1-N4 = R2-N2. Both agree LLaMA evidence is overclaimed."
32	    action_items:
33	      - round: 1
34	        action: "Downgrade LLaMA to 'exploratory cross-architecture analysis'; Title keep 'Reasoning Models' but Abstract/Contribution hedge; §5.5 rename from 'validation' to 'exploratory analysis'"
35	        assigned_to: "paper_agent"
36	        status: in_progress
37	    resolution: ""
38	    resolution_round: null
39	
40	  - id: "R1-N3"
41	    summary: "Single benchmark (MATH-500, 50 problems) severely limits generalization — title/abstract say 'reasoning models' but only math reasoning tested"
42	    category: experiment
43	    severity: critical
44	    status: in_progress
45	    first_raised_round: 1
46	    last_seen_round: 1
47	    mentions:
48	 
…[truncated 15132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-15T10:50:58.235030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-15T10:50:58.285817+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_director_b570dbd0.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-15T10:50:58.336447+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-15T10:50:58.387057+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-15T10:51:01.954436+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-15T10:51:02.005060+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-15T10:51:05.321362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-15T10:51:05.773816+00:00_

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\section*{Reproducibility}
48	Code and data will be released upon acceptance.
49	
50	\appendix
51	\input{appendix}
52	\input{appendix_moved}
53	\input{appendix_disc_analysis}
54	\input{appendix_robustness}
55	
56	\end{document}
57	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-15T10:51:05.824637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-15T10:51:06.277658+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$39{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We observe that discrimination collapse---head pruning flattening cumulative importance scores---correlates with the phase-dependent severity amplification, suggesting a mechanism whereby compound sparsity selectively degrades importance-based eviction in distributed-attention phases.
9	These findings motivate phase-aware compression budgets for mathematical reasoning models.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-15T10:51:06.278212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-15T10:51:06.731637+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 2353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-15T10:51:06.732151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-15T10:51:06.832837+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are
…[truncated 1994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-15T10:51:19.305878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-15T10:51:20.060757+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$39{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger. % exp_id: n500_unified_final; DS imp Δ 0.39→8.48, rand 0.01→0.51; JT z=33.7 (imp), 6.2 (rand)
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\ % exp_id: n500_unified_final; DS imp median_ii_diff
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\ % exp_id: n500_unified_final; DS rand median_ii_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown from an
…[truncated 9653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-15T10:51:20.061330+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-15T10:51:20.613454+00:00_

1	\section{Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	\subsection{Discrimination Collapse}
5	\label{sec:discrimination-collapse-main}
6	
7	We observe that head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient of importance scores decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). This pattern---which we term \emph{discrimination collapse}---is consistent with importance-based eviction degenerating into noise-sensitive selection when score distributions flatten. The effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. This observation is independently corroborated by \cite{hies-2025}, who report importance score collapse under heavy single-axis pruning; our results extend this to the compound setting, where collapse is amplified by the interaction of two compression axes and modulated by reasoning phase. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
8	
9	A partial counterfactual supports this interpretation: random eviction does not rely on importance scores, so it is immune to score-distribution changes caused by head pruning. The flat severity gradient under random eviction ($G \approx 1$) is consistent with this independence, while importance-based eviction---whose decisions depend on the very scores that pruning degrades---exhibits the phase-modulated amplification. We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
10	
11	\subsection{Entropy Redistribu
…[truncated 897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-15T10:51:20.764510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-15T10:51:20.865467+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
12	
13	\paragraph{KV cache eviction.}
14	Most methods rely on importance scoring whose reliability is increasingly questioned.
15	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
16	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
17	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
18	\cite{hies-2025} independently show
…[truncated 2273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-15T10:51:20.916144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-15T10:51:20.966913+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($G{=}30$--$148{\times}$ at $n{=}496$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The near-unity random baseline ($G{=}0.5$--$1.3{\times}$, trivial magnitude) confirms the dominant amplification is strategy-specific. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\% (Wilcoxon $p = 0.002$), below the pre-registe
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-15T10:51:25.440349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-15T10:51:25.842548+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation ($n{=}496$/$475$ problems). Under importance-based eviction, the amplification ratio $G$ ranges from $30{\times}$ to $148{\times}$ across sparsity levels, with paired median differences $\Delta$ from $0.39$ to $8.48$ (DeepSeek) and $0.07$ to $3.16$ (Qwen), all $p < 10^{-13}$. Random eviction develops a detectable phase gradient only above $s \approx 0.20$, but $3$--$39{\times}$ weaker than importance-based. A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at all four sparsity levels; suggestive preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) indicates the phenomenon may extend beyond Qwen2, though at ${\sim}1/40$ the magnitude and with a weaker strategy contrast. Discrimination collapse provides a correlational mechanistic explanation supported by both Qwen2-based models.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment. Extending this analysis to code reasoning (HumanEval, LiveCodeBench) and science reasoning (GPQA), validating the discrimination collapse mechanism through causal intervention, and characterizing asymmetric compound interactions are promising directions for future work.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-15T10:51:26.018549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-15T10:51:26.320468+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. MATH-500 is a suitable first testbed because it elicits structured reasoning with clear phase transitions (exploratory vs.\ structured computation), supports per-problem evaluation enabling paired statistical tests, and spans sufficient difficulty to produce meaningful variation in sequence length and attention dynamics. However, different reasoning tasks---code generation (e.g., HumanEval, LiveCodeBench), science reasoning (e.g., GPQA), multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile. Whether the phase-strategy interaction documented here extends to these domains is an open question.
6	
7	\paragraph{Symmetric sparsity assumption.}
8	Our analysis applies symmetric sparsity rates: the same fraction $s$ is used for both head pruning and KV cache eviction. Practical deployments may use asymmetric budgets (e.g., aggressive head pruning with conservat
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-15T10:51:26.320959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-15T10:51:27.083472+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 762
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-15T10:51:27.184596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-15T10:51:27.235398+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{decision-repr-transition-2026,
13	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
14	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
15	    journal = {arXiv preprint arXiv:2605.07271},
16	    year    = {2026},
17	    url     = {https://arxiv.org/abs/2605.07271},
18	}
19	
20	@article{deepseek-r1-2025,
21	    title   = {{DeepSeek-R1} incentivizes reasoning in {LLMs} through reinforcement learning},
22	    author  = {{DeepSeek-AI}},
23	    journal = {Nature},
24	    volume  = {645},
25	    pages   = {633--638},
26	    year    = {2025},
27	    doi     = {10.1038/s41586-025-09422-z},
28	}
29	
30	@inproceedings{defensivekv-iclr2026,
31	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
32	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
33	    booktitle = {International Conference on Learning Representations},
34	    year      = {2026},
35	    url       = {https://arxiv.org/abs/2510.13334},
36	}
37	
38	@article{doing-more-with-less-2026,
39	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
40	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
41	    journal = {arXiv preprint arXiv:2604.25098},
42	    year    = {2026},
43	    url     = {https://arxiv
…[truncated 238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-15T10:51:31.360009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-15T10:51:31.461238+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$39{\times}$ weaker than importance-based, confirming that the dominant amplification is strategy-specific. % exp_id: n500_unified_final; DS rand s025 0.257 p=0.006, s030 0.510 p=0.006; QW rand s025 0.393, s030 0.913
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy s
…[truncated 4903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-15T10:51:31.662535+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/appendix_robustness.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/appendix_robustness.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-15T10:51:31.713243+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-15T10:51:35.466131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-15T10:51:36.378127+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-model random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-model Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-model random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings. % exp_id: n500_unified_final; source: supplementary_stats.json bh_fdr_correction
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based c
…[truncated 4154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-15T10:51:36.378649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-15T10:51:36.379030+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in trai
…[truncated 12568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-15T10:51:36.831670+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\placeholder",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-15T10:51:36.882370+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex:21:\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-15T10:51:42.010788+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "placeholder",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-15T10:51:42.920018+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex:21:\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/citation_audit_report.md:81:All 31 citations are real, verified papers. No placeholder or hallucinated references detected. The references.bib file is ready for compilation with acl_natbib style.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-15T10:51:43.172054+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "REVIEWER-ATTACK|REBUTTAL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "REVIEWER-ATTACK|REBUTTAL",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-15T10:51:43.222793+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-15T10:51:47.210788+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\placeholder",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-15T10:51:47.663101+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex:21:\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-15T10:51:48.416766+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "h2o.*neurips|h2o-neurips",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
  "output_mode": "content",
  "-A": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "h2o.*neurips|h2o-neurips",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
    "output_mode": "content",
    "-A": "5"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-15T10:51:48.467506+00:00_

69:@inproceedings{h2o-neurips2023,
70-    title     = {{H\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
71-    author    = {Zhang, Zhenyu and Sheng, Ying and Zhou, Tianyi and Chen, Tianlong and Zheng, Lianmin and Cai, Ruisi and Song, Zhao and Tian, Yuandong and R{\'e}, Christopher and Barrett, Clark and Wang, Zhangyang and Chen, Beidi},
72-    booktitle = {Advances in Neural Information Processing Systems},
73-    year      = {2023},
74-    url       = {https://arxiv.org/abs/2306.14048},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-15T10:51:53.490011+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "rlkv|longflow|pmkvq",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
  "output_mode": "content",
  "-i": "True",
  "-A": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "rlkv|longflow|pmkvq",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
    "output_mode": "content",
    "-i": "True",
    "-A": "5"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-15T10:51:53.993218+00:00_

232:@article{longflow-2026,
233:    title   = {{LongFlow}: Efficient {KV} Cache Compression for Reasoning Models},
234-    author  = {Su, Yi and Tian, Zhenxu and Qiao, Dan and Zhou, Yuechi and Li, Juntao and Zhang, Min},
235-    journal = {arXiv preprint arXiv:2603.11504},
236-    year    = {2026},
237-    url     = {https://arxiv.org/abs/2603.11504},
238-    note    = {Withdrawn from ICLR 2026},
--
241:@inproceedings{pmkvq-iclr2026,
242-    title     = {{PM-KVQ}: Progressive Mixed-precision {KV} Cache Quantization for Long-{CoT} {LLMs}},
243-    author    = {Liu, Tengxuan and Li, Shiyao and Yang, Jiayi and Zhao, Tianchen and Zhou, Feng and Song, Xiaohui and Dai, Guohao and Yan, Shengen and Yang, Huazhong and Wang, Yu},
244-    booktitle = {International Conference on Learning Representations},
245-    year      = {2026},
246-    url       = {https://arxiv.org/abs/2505.18610},
--
249:@article{rlkv-2025,
250-    title   = {Which Heads Matter for Reasoning? {RL}-Guided {KV} Cache Compression},
251-    author  = {Du, Wenjie and Jiang, Li and Tao, Keda and Liu, Xue and Wang, Huan},
252-    journal = {arXiv preprint arXiv:2510.08525},
253-    year    = {2025},
254-    url     = {https://arxiv.org/abs/2510.08525},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-15T10:51:54.244899+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "following ThinKV",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "following ThinKV",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-15T10:51:54.295637+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex:33:Each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\ref{app:formulation-details}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-15T10:53:30.856228+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "5",
  "text": "## Round 5 修订评估 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 (main conference)\n- **截止日期**: 2026-06-15\n- **格式**: ACL 2-column, 长文 8 页正文, double-blind\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n\n### 任务\n这是修订评估。论文从 Round 1 (weak reject, 2.5/5) 起经历了多轮修改。请逐条检查以下 open/in_progress issues 是否已在论文中充分解决。对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n### 关键变化摘要（Director 初步扫描）\n- n=50 → n=500（n_eff=496/475）\n- Title: \"Reasoning Models\" → \"Mathematical Reasoning Models\"\n- §5.5 改名 \"Exploratory Cross-Architecture Analysis\"\n- Table 4 (LLaMA) 数据已填充\n- Discussion oracle pilot 数据已填充 (18%/32%)\n- §6 拆分为 §6.1 Discrimination Collapse + §6.2 Entropy Redistribution，标注 correlational\n- HIES 对比扩展\n- 新增 appendix_robustness.tex：BH-FDR、segmentation robustness、mpl sensitivity\n- JT test 替代 Spearman-only；G 降级为辅助指标 + bootstrap CI\n- RLKV/LongFlow/PM-KVQ 已引用\n- Reproducibility 声明已添加\n- REVIEWER-ATTACK 注释已删除\n- placeholder 已全部清除\n\n### 你的 Issue 列表（逐条判定）\n\n**[R1-N1] critical: 40+ placeholders 未填充**\n检查：grep `\\placeholder` 在 .tex 文件中是否仍有使用（不含定义行）。Table 4 数据是否完整。Discussion oracle 数据是否完整。\n\n**[R1-N2] critical: 50 题样本量 / power analysis 缺失**\n检查：现在用 500 题是否消除了 power 疑虑？CI width shrinkage 是否报告？排除标准是否在 §4 说明？\n\n**[R1-N3] critical: 单一 benchmark / Title overclaim**\n检查：Title 是否限定为 mathematical reasoning？Abstract/Conclusion 范围限定是否充分？\n\n**[R1-N4] critical: Cross-arch overclaim**\n检查：§5.5 是否降级为 exploratory？Table 4 数据是否完整？Contribution 2 措辞？LLaMA 叙述是否 hedged？\n\n**[R1-N5] critical: 机制 correlational only**\n检查：§6 标题是否去掉 assertive 措辞？correlational 是否明确标注？§6.1 vs §6.2 拆分是否合理？HIES 对比是否充分？\n\n**[R1-W1] warning: Phase segmentation 论证不足**\n检查：是否有 sensitivity analysis（quartile/quintile）？background.tex 是否仍说 \"following ThinKV\"？min_phase_length 是否论证？\n\n**[R1-W2] warning: Symmetric sparsity**\n检查：Limitations 中是否讨论？\n\n**[R1-W3] warning: G 数值稳定性**\n检查：G 是否有 bootstrap CI？是否降级为辅助指标？Δ 是否为 primary？\n\n**[R1-W4] warning: Bonferroni k=4 scope**\n检查：是否论证 family 划分？BH-FDR 是否补充？\n\n**[R1-W5] warning: Spearman ρ=1.0 / Table 差异**\n检查：是否标注 n=4 caveat + one/two-tail？JT test 是否替代/补充？Table 1 vs Table 3 差异是否解释？\n\n**[R1-W6] warning: 排除标准**\n检查：§4 中是否完整报告排除标准和各模型 effective n？\n\n**[REV-ADD-2] warning: Random masking threshold story**\n检查：Results §5.1 是否报告 random s025+ significance 作为 threshold story？importance vs random effect size ratio？\n\n**[REV-ADD-3] warning: Qwen mid-phase 45.2% null rate**\n检查：是否报告 root cause（temporal autocorrelation）？effective n？对 primary Δ 的影响是否说明？\n\n### 额外检查\n1. n=50 profiling subset 表格（Table 2, permutation test）与 n=500 主表共存是否产生混淆？\n2. 关键数字变化（old Δ_s030=14.59 → new 8.48; old G_s030=274× → new 148×）——n=500 下的新数据是否 internally consistent？\n3. 是否有新引入的方法论问题？\n\n请输出：每个 issue 的判定 + 新发现的问题 + 总体评分更新建议。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "5",
    "text": "## Round 5 修订评估 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 (main conference)\n- **截止日期**: 2026-06-15\n- **格式**: ACL 2-column, 长文 8 页正文, double-blind\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n\n### 任务\n这是修订评估。论文从 Round 1 (weak reject, 2.5/5) 起经历了多轮修改。请逐条检查以下 open/in_progress issues 是否已在论文中充分解决。对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n### 关键变化摘要（Director 初步扫描）\n- n=50 → n=500（n_eff=496/475）\n- Title: \"Reasoning Models\" → \"Mathematical Reasoning Models\"\n- §5.5 改名 \"Exploratory Cross-Architecture Analysis\"\n- Table 4 (LLaMA) 数据已填充\n- Discussion oracle pilot 数据已填充 (18%/32%)\n- §6 拆分为 §6.1 Discrimination Collapse + §6.2 Entropy Redistribution，标注 correlational\n- HIES 对比扩展\n- 新增 appendix_robustness.tex：BH-FDR、segmentation robustness、mpl sensitivity\n- JT test 替代 Spearman-only；G 降级为辅助指标 + bootstrap CI\n- RLKV/LongFlow/PM-KVQ 已引用\n- Reproducibility 声明已添加\n- REVIEWER-ATTACK 注释已删除\n- placeholder 已全部清除\n\n### 你的 Issue 列表（逐条判定）\n\n**[R1-N1] critical: 40+ placeholders 未填充**\n检查：grep `\\placeholder` 在 .tex 文件中是否仍有使用（不含定义行）。Table 4 数据是否完整。Discussion oracle 数据是否完整。\n\n**[R1-N2] critical: 50 题样本量 / power analysis 缺失**\n检查：现在用 500 题是否消除了 power 疑虑？CI width shrinkage 是否报告？排除标准是否在 §4 说明？\n\n**[R1-N3] critical: 单一 benchmark / Title overclaim**\n检查：Title 是否限定为 mathematical reasoning？Abstract/Conclusion 范围限定是否充分？\n\n**[R1-N4] critical: Cross-arch overclaim**\n检查：§5.5 是否降级为 exploratory？Table 4 数据是否完整？Contribution 2 措辞？LLaMA 叙述是否 hedged？\n\n**[R1-N5] critical: 机制 correlational only**\n检查：§6 标题是否去掉 assertive 措辞？correlational 是否明确标注？§6.1 vs §6.2 拆分是否合理？HIES 对比是否充分？\n\n**[R1-W1] warning: Phase segmentation 论证不足**\n检查：是否有 sensitivity analysis（quartile/quintile）？background.tex 是否仍说 \"following ThinKV\"？min_phase_length 是否论证？\n\n**[R1-W2] warning: Symmetric sparsity**\n检查：Limitations 中是否讨论？\n\n**[R1-W3] warning: G 数值稳定性**\n检查：G 是否有 bootstrap CI？是否降级为辅助指标？Δ 是否为 primary？\n\n**[R1-W4] warning: Bonferroni k=4 scope**\n检查：是否论证 family 划分？BH-FDR 是否补充？\n\n**[R1-W5] warning: Spearman ρ=1.0 / Table 差异**\n检查：是否标注 n=4 caveat + one/two-tail？JT test 是否替代/补充？Table 1 vs Table 3 差异是否解释？\n\n**[R1-W6] warning: 排除标准**\n检查：§4 中是否完整报告排除标准和各模型 effective n？\n\n**[REV-ADD-2] warning: Random masking threshold story**\n检查：Results §5.1 是否报告 random s025+ significance 作为 threshold story？importance vs random effect size ratio？\n\n**[REV-ADD-3] warning: Qwen mid-phase 45.2% null rate**\n检查：是否报告 root cause（temporal autocorrelation）？effective n？对 primary Δ 的影响是否说明？\n\n### 额外检查\n1. n=50 profiling subset 表格（Table 2, permutation test）与 n=500 主表共存是否产生混淆？\n2. 关键数字变化（old Δ_s030=14.59 → new 8.48; old G_s030=274× → new 148×）——n=500 下的新数据是否 internally consistent？\n3. 是否有新引入的方法论问题？\n\n请输出：每个 issue 的判定 + 新发现的问题 + 总体评分更新建议。"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-15T10:53:49.723613+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18867
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-15T10:53:50.125781+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "5",
  "text": "## Round 5 修订评估 — Reviewer 2（新颖性/完整性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 (main conference)\n- **截止日期**: 2026-06-15\n- **格式**: ACL 2-column, 长文 8 页正文, double-blind\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n\n### 任务\n这是修订评估。论文从 Round 1 (weak reject, 2.5/5) 起经历了多轮修改。请逐条检查以下 open/in_progress issues 是否已在论文中充分解决。对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n### 关键变化摘要（Director 初步扫描）\n- n=50 → n=500（n_eff=496/475）\n- Title: \"Reasoning Models\" → \"Mathematical Reasoning Models\"\n- §5.5 改名 \"Exploratory Cross-Architecture Analysis\"\n- Table 4 (LLaMA) 数据已填充\n- Discussion oracle pilot 数据已填充 (18%/32%)\n- §6 拆分为 §6.1 + §6.2，correlational 明确标注\n- HIES 对比在 Related Work 和 §6 中扩展\n- 新增 appendix_robustness.tex：BH-FDR 44 tests、segmentation robustness (quartile/quintile)、mpl sensitivity\n- RLKV/LongFlow/PM-KVQ 已引用\n- Abstract 精简重写\n- REVIEWER-ATTACK 注释已删除\n- h2o bib entry 已修复（title 字段已有）\n- Reproducibility 声明已添加\n- \\placeholder 命令无实际使用\n\n### 你的 Issue 列表（逐条判定）\n\n**[R1-N1] critical: Placeholders**\n检查：所有 placeholder 是否清除？Table 4 数据完整性？\n\n**[R2-N3] warning: HIES 区分不足**\n检查：Related Work 和 §6 中是否有 explicit comparison？是否说明 single-axis vs compound+phase delta？crossover 作为 HIES 不能 generate 的 prediction？\n\n**[R2-W3] warning: Missing references RLKV/LongFlow/PM-KVQ**\n检查：是否已引用？引用位置是否恰当？\n\n**[R2-W5] warning: Abstract 过长过密**\n检查：Abstract 是否精简？统计数字是否减少？LLaMA 细节是否移至 Results？\n\n**[R2-Minor-1] info: h2o bib / author mismatch**\n检查：h2o title 字段是否修复？其他 author mismatch？\n\n**[R2-Minor-2] info: REVIEWER-ATTACK/REBUTTAL 注释**\n检查：是否已删除？\n\n**[R2-Minor-6] info: s=0.35 未完整报告**\n检查：是否已删除或完整报告？\n\n**[R1-Minor-code] info: 无代码/数据声明**\n检查：是否有 Reproducibility 声明？\n\n### 额外检查：新颖性和写作质量\n\n1. **Random eviction 叙事变化**：Round 1 中 \"7/8 conditions non-significant\"，现在 n=500 后 random s≥0.25 变显著了。论文是否恰当处理了这一叙事变化？\"dominant driver\" vs \"flat baseline\" 的 framing 是否 honest？\n2. **Abstract 质量**：精简后的 abstract 是否准确、可读、不 overclaim？\n3. **Contribution 措辞**：三个 contributions 是否恰当反映修改后的 evidence strength？\n4. **写作一致性**：n=50 profiling tables 与 n=500 main tables 共存是否 coherent？读者是否会困惑？\n5. **新引用 PM-KVQ 和 RLKV**：引用是否准确？是否有新的幻觉引用？\n6. **\"following ThinKV\" 措辞**（background.tex line 33）：是否仍在，是否应修正？\n7. **整体影响力评估变化**：n=500 极显著结果 (p<10^-69) 是否改变了对论文价值的判断？\n\n请输出：每个 issue 的判定 + 新发现的问题 + 总体评分更新建议。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "5",
    "text": "## Round 5 修订评估 — Reviewer 2（新颖性/完整性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 (main conference)\n- **截止日期**: 2026-06-15\n- **格式**: ACL 2-column, 长文 8 页正文, double-blind\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n\n### 任务\n这是修订评估。论文从 Round 1 (weak reject, 2.5/5) 起经历了多轮修改。请逐条检查以下 open/in_progress issues 是否已在论文中充分解决。对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n### 关键变化摘要（Director 初步扫描）\n- n=50 → n=500（n_eff=496/475）\n- Title: \"Reasoning Models\" → \"Mathematical Reasoning Models\"\n- §5.5 改名 \"Exploratory Cross-Architecture Analysis\"\n- Table 4 (LLaMA) 数据已填充\n- Discussion oracle pilot 数据已填充 (18%/32%)\n- §6 拆分为 §6.1 + §6.2，correlational 明确标注\n- HIES 对比在 Related Work 和 §6 中扩展\n- 新增 appendix_robustness.tex：BH-FDR 44 tests、segmentation robustness (quartile/quintile)、mpl sensitivity\n- RLKV/LongFlow/PM-KVQ 已引用\n- Abstract 精简重写\n- REVIEWER-ATTACK 注释已删除\n- h2o bib entry 已修复（title 字段已有）\n- Reproducibility 声明已添加\n- \\placeholder 命令无实际使用\n\n### 你的 Issue 列表（逐条判定）\n\n**[R1-N1] critical: Placeholders**\n检查：所有 placeholder 是否清除？Table 4 数据完整性？\n\n**[R2-N3] warning: HIES 区分不足**\n检查：Related Work 和 §6 中是否有 explicit comparison？是否说明 single-axis vs compound+phase delta？crossover 作为 HIES 不能 generate 的 prediction？\n\n**[R2-W3] warning: Missing references RLKV/LongFlow/PM-KVQ**\n检查：是否已引用？引用位置是否恰当？\n\n**[R2-W5] warning: Abstract 过长过密**\n检查：Abstract 是否精简？统计数字是否减少？LLaMA 细节是否移至 Results？\n\n**[R2-Minor-1] info: h2o bib / author mismatch**\n检查：h2o title 字段是否修复？其他 author mismatch？\n\n**[R2-Minor-2] info: REVIEWER-ATTACK/REBUTTAL 注释**\n检查：是否已删除？\n\n**[R2-Minor-6] info: s=0.35 未完整报告**\n检查：是否已删除或完整报告？\n\n**[R1-Minor-code] info: 无代码/数据声明**\n检查：是否有 Reproducibility 声明？\n\n### 额外检查：新颖性和写作质量\n\n1. **Random eviction 叙事变化**：Round 1 中 \"7/8 conditions non-significant\"，现在 n=500 后 random s≥0.25 变显著了。论文是否恰当处理了这一叙事变化？\"dominant driver\" vs \"flat baseline\" 的 framing 是否 honest？\n2. **Abstract 质量**：精简后的 abstract 是否准确、可读、不 overclaim？\n3. **Contribution 措辞**：三个 contributions 是否恰当反映修改后的 evidence strength？\n4. **写作一致性**：n=50 profiling tables 与 n=500 main tables 共存是否 coherent？读者是否会困惑？\n5. **新引用 PM-KVQ 和 RLKV**：引用是否准确？是否有新的幻觉引用？\n6. **\"following ThinKV\" 措辞**（background.tex line 33）：是否仍在，是否应修正？\n7. **整体影响力评估变化**：n=500 极显著结果 (p<10^-69) 是否改变了对论文价值的判断？\n\n请输出：每个 issue 的判定 + 新发现的问题 + 总体评分更新建议。"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-15T10:53:51.690364+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1564
}
```

</details>

---


### Assistant

_source line 316 · 2026-05-15T10:53:57.604721+00:00_

Round 5 Reviewer 任务已分配。等待两位 Reviewer 的修订评估返回。

**当前状态**：
- 论文修改幅度很大——20 个 issue 中 Director 初步判断绝大多数已 resolved
- 已知残留：background.tex "following ThinKV" 措辞未修正
- 需 Reviewer 确认的关键点：n=50/n=500 双表共存是否混淆、random eviction 叙事变化是否诚实处理、新数字内部一致性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 317 · 2026-05-15T10:57:46.068628+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 5 修订评估报告（方法严谨性）

论文：*Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models*

---

## 总体评分更新
**Overall**: 2.5 → **3.5 / 5**（Borderline Conference）
**一句话总结**: 论文经过多轮修改后有实质性改善——样本量扩大 10 倍（n=500）、claims 适当限定、统计方法加强、robustness analyses 充分——已达到 borderline conference 水平。残余问题集中在 n=50 profiling 数据与 n=500 主数据共存引起的混淆，以及 crossover analysis 未在 n=500 上验证。

## 官方维度打分更新

| 维度 | Round 1 | Round 5 | 理由 |
|------|---------|---------|------|
| Soundness | 2.5 | **3.5** | n=500 使主要 claims 统计上极显著（p<10^{-69}）；claims 与证据匹配改善；但 n=50 profiling table 共存和 crossover 未验证是残留缺陷 |
| Excitement | 3.0 | **3.0** | 核心发现未变（仍是 single benchmark + 7B scale）；scoping 改善使 claim 更可信但不增加 novelty |
| Reproducibility | 2.0 | **3.5** | 随机种子报告（seed=42）、硬件说明、代码开源承诺、n=500 数据完整——从"无法复现"到"基本可复现" |
| Confidence | 4 | **4** | 不变 |

---

## 逐条 Issue 判定

### **[R1-N1] critical: 40+ placeholders** → [RESOLVED]

- `grep \placeholder` 仅匹配 `\newcommand` 定义行（main.tex:21），无实际使用
- Table 4 (LLaMA cross-arch, §5.5) 数据完整：0.020 [0.002, 0.043] p=0.219 / 0.022 [-0.090, 0.187] p=0.253 / 0.095 [-0.004, 0.303] p=0.083 / 0.356 [-0.069, 0.544] p=0.029
- Discussion oracle pilot: 18% (p=0.002) / 32% (p=0.024)，below 30% gate
- Appendix Qwen effective-n table: 全部填充（High/Low 475, Mid 274）
- Per-problem concordance: mean ρ=−0.107, p=0.926
- Qwen random Δ̃ 值已填
- 残留 cosmetic issue：`\newcommand{\placeholder}` 定义仍存在（main.tex:21）但无功能影响

### **[R1-N2] critical: 50 题样本量** → [RESOLVED]

- n=50 → n=500（全部 MATH-500），n_eff = 496 (DS) / 475 (QW)
- 排除标准在 §4 明确："Problems with degenerate phase assignments (null low or high phase) are excluded"（methodology.tex:10）
- DS 排除 4 题、QW 排除 25 题——数量和原因均报告
- CI width shrinkage：2.5–5.9× across all 16 conditions（methodology.tex:22）
- p-values 从 <0.005（n=50）提升到 <10^{-69}（DS importance, n=496）——power 疑虑完全消除
- Post-hoc power analysis 未显式报告，但在 p<10^{-69} 下已无必要

### **[R1-N3] critical: 单一 benchmark / Title overclaim** → [RESOLVED]

- Title: "Reasoning Models" → "Mathematical Reasoning Models"（main.tex:23）
- Abstract: "mathematical reasoning models"（abstract.tex:3, 9）
- Conclusion: 列出 "code reasoning (HumanEval, LiveCodeBench) and science reasoning (GPQA)" 作为 future work（conclusion.tex:5）
- Limitations: "We evaluate exclusively on MATH-500"（limitations.tex:4-5），明确讨论不同推理任务可能的影响
- Limitations 新增对 MATH-500 选择的正面论证："suitable first testbed because it elicits structured reasoning with clear phase transitions"（limitations.tex:5）

### **[R1-N4] critical: Cross-arch overclaim** → [RESOLVED]

- §5.5 标题改为 "Exploratory Cross-Architecture Analysis"（results.tex:74）
- Contribution 2 改为："with exploratory evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2"（introduction.tex:23）——"exploratory" + "suggesting" + "may"，hedging 充分
- Abstract 使用 "preliminary cross-architecture evidence"（abstract.tex:7）
- Conclusion 使用 "suggestive preliminary evidence"（conclusion.tex:4）
- §5.5 文本："the LLaMA evidence should be interpreted as preliminary given the weak interaction magnitude and partial statistical significance"（results.tex:81）
- LLaMA random 的 non-trivial phase gradient 现在明确讨论："random pruning also exhibits a non-trivial phase gradient on LLaMA (d_z: 0.35→0.44), substantially reducing the strategy contrast"（results.tex:81）

### **[R1-N5] critical: 机制 correlational only** → [RESOLVED]

- §6 标题改为 "Discrimination Collapse under Compound Sparsity"（analysis.tex:1）——去掉了 "Entropy-" 前缀
- 拆分为 §6.1 Discrimination Collapse + §6.2 Entropy Redistribution
- §6.1 明确标注 correlational（analysis.tex:9）："We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work."
- HIES 对比在两处展开：
  - Related Work (related_work.tex:18): "Our work extends this to the compound setting, revealing that collapse is amplified by the interaction of two compression axes and modulated by reasoning phase—phenomena absent in single-axis analysis. The crossover effect is a prediction that single-axis frameworks cannot generate."
  - §6.1 (analysis.tex:7): "independently corroborated by \cite{hies-2025}... our results extend this to the compound setting"
- Abstract 用 "correlates with"（abstract.tex:8）而非因果语言
- Conclusion 用 "correlational mechanistic explanation"（conclusion.tex:4）

### **[R1-W1] warning: Phase segmentation 论证不足** → [PARTIALLY RESOLVED]

**已解决部分：**
- Appendix (app:seg-robust): tercile/quartile/quintile 对比（Table），monotonic Δ 和 significance 保持
- Appendix (app:mpl-sensitivity): mpl ∈ {5, 10, 20} 全 16 conditions 对比（Table），Δ 变化 <5% for DS importance
- §4 (methodology.tex:18): "Robustness to segmentation granularity (quartile, quintile) and minimum phase length (5, 10, 20 tokens) is verified"

**残留问题：**
- Background.tex:33 仍写 "following ThinKV"——ThinKV 使用显式 `&lt;think>` delimiters 定义 phase，与本文的 quantile-based attention sparsity segmentation 是不同方法。引用 ThinKV 作为 phase-aware 方向的先例是合适的，但 "following ThinKV" 暗示使用了 ThinKV 的 segmentation 方法，这是误导。
- Quartile/quintile robustness check 仅用 n=50 spot check（appendix_robustness.tex:76 caption），未在 n=500 上验证。虽然 tercile 在 n=500 上已验证（Table 1），但既然已有 n=500 数据，不对 quartile/quintile 也跑 n=500 有些inconsistent。

### **[R1-W2] warning: Symmetric sparsity** → [RESOLVED]

- Limitations 新增专门段落（limitations.tex:7-8）："Practical deployments may use asymmetric budgets... investigating asymmetric compound interactions is a natural extension."

### **[R1-W3] warning: G 数值稳定性** → [RESOLVED]

- G 有 bootstrap CI：30× [26, 37] → 148× [119, 171]（results.tex:29）
- G 明确标为 "auxiliary metric"（methodology.tex:22; Table 2 caption）
- Δ 为 primary metric："the paired median difference Δ is primary"（methodology.tex:22）

### **[R1-W4] warning: Bonferroni k=4 scope** → [RESOLVED]

- Family 划分论证："per model×strategy combination, 4 sparsity levels testing one dose-response hypothesis"（methodology.tex:22）
- BH-FDR 补充（Appendix app:bh-fdr）：44 个 tests 全覆盖，32 个 Bonferroni-significant 结果在 BH-FDR 下全部 remain significant，5 个 BH-only 结果均在 random eviction（最弱效应）

### **[R1-W5] warning: Spearman ρ=1.0 / Table 差异** → [RESOLVED]

- JT test 补充：z=6.2–33.7, all p<10^{-9}，使用 ~496 per-problem values 而非 4 个 aggregated medians（methodology.tex:22）
- Spearman 现标注 "one-tailed"（results.tex:71）
- Table 1 (n=496) vs Table 3 (n=496/475) 数值一致——DS 在所有 s 下 Δ 值相同（0.39, 1.21, 3.99, 8.48），消除了 Round 1 中 Table 1 (0.39) vs Table 4 (0.32) 的差异

### **[R1-W6] warning: 排除标准** → [RESOLVED]

- §4 methodology.tex:10 完整报告排除标准和各模型 effective n

### **[REV-ADD-2] warning: Random masking threshold story** → [RESOLVED]

- §5.1 (results.tex:8): "Random eviction develops a detectable but weak phase gradient above s≈0.20: at s≤0.20, Δ is non-significant (0.01–0.03; CIs span zero); at s≥0.25, Δ becomes significant (0.26–0.51; p_Bonf<0.006) but 15–39× smaller"
- Cross-model: "2.7–20× weaker than importance-based"（results.tex:71）
- Effect size ratios 一致且充分

### **[REV-ADD-3] warning: Qwen mid-phase 45.2% null rate** → [RESOLVED]

- Root cause 报告："lower temporal autocorrelation in its attention sparsity patterns (lag-1 r=0.718 vs. 0.894, d=−1.68)"（methodology.tex:10）
- Effective n 报告：Appendix Table (qwen-effective-n) 填充完整（High/Low 475, Mid 274）
- 对 primary Δ 的非影响说明："this does not affect the primary gradient metric Δ"（methodology.tex:10）

---

## 额外检查

### 1. n=50 profiling Table 2 与 n=500 主表共存

**[NEW-W1] [warning] n=50 与 n=500 数据混合引起混淆**

Table 2（main body §5.2，full-page table*）使用 n=50 profiling 数据，G 值为 69–274×。Table 1（§5.1，n=496）和 Table 3（§5.6，n=496/475）使用 n=500 数据，text 中 G=30–148×。这导致：
- 同一论文 main body 中出现两套不一致的数字：Table 2 的 Δ_s030=14.59 vs Table 1 的 Δ_s030=8.48（差 72%）
- Table 2 的 G=274× vs text 的 G=148×（差 85%）
- Caption 中有标注（"profiling subset"），但读者对比 Table 1 和 Table 2 仍然困惑
- §5.3 Crossover analysis 引用的数值（0.032 vs 0.818, 7.196 vs 1.363）也来自 n=50，未在 n=500 上确认

**建议**：(a) 将 Table 2 移至 Appendix（作为 "initial profiling results"），main body 仅保留 n=500 数据；或 (b) 在 Table 2 下方/上方添加 n=500 的对应 per-phase breakdown table。

### 2. 关键数字变化的 internal consistency

n=500 下 Δ 值系统性低于 n=50：

| $s$ | Δ (n=50, Table 2) | Δ (n=496, Table 1) | 变化 |
|------|------|------|------|
| 0.15 | 0.39 | 0.39 | 0% |
| 0.20 | 1.48 | 1.21 | −18% |
| 0.25 | 7.16 | 3.99 | −44% |
| 0.30 | 14.59 | 8.48 | −42% |

高 sparsity 处 Δ 缩减约 40%——说明 n=50 subsample 在高 sparsity 下 median 被 outliers 拉高。这是正常的统计行为，但论文未讨论这一点。建议在 §5.2 或 footnote 中用一句话说明 n=50 profiling values 因 small-sample variance 偏高。

### 3. Crossover analysis 未在 n=500 上验证

**[NEW-W2] [warning] §5.3 crossover 数据来自 n=50，未在 n=500 上确认**

§5.3 (results.tex:66) 引用的具体数值（importance high=0.032 vs random high=0.818; importance low=7.196 vs random low=1.363）全部来自 n=50 Table 2。鉴于 n=50→n=500 的 Δ 变化达 40%，crossover magnitude 在 n=500 下是否稳定？crossover 是否仍然存在于所有 4 个 sparsity levels？

论文现在对其他 claims 使用 n=500 数据进行了彻底验证（Table 1, 3, robustness checks），但 crossover 这个 non-trivial claim 仍完全依赖 n=50。这是 methodological inconsistency。

**建议**：在 n=500 上重新计算 per-phase 数据并更新 crossover analysis，至少在 Appendix 中报告。

### 4. 其他新发现

- **Segmentation robustness n=50 only**（appendix_robustness.tex:71, 76）：quartile/quintile 检查仅用 n=50 spot check。既然已有 n=500 数据，至少对 quartile 做 n=500 验证会更有说服力。目前的 argument 是"在 n=50 上 robust"→"因此在 n=500 上也 robust"，逻辑上缺一步。
- **\placeholder command 定义残留**（main.tex:21）：cosmetic，不影响编译，但提交前应删除。
- **LLaMA 仍为 n=49**（results.tex:77, 86）：在 DS/QW 升级到 n=500 的对比下更显 underpowered。论文已标注 "exploratory"，这是诚实的处理，但如果有计算预算，扩展 LLaMA 样本量将显著加强 §5.5。
- **"following ThinKV" 表述**（background.tex:33）：ThinKV 用 explicit `&lt;think>` delimiters，本文用 quantile-based sparsity segmentation——两种方法不同。应改为 "inspired by the phase-aware perspective of ThinKV" 或类似表述。

---

## 总结

**已 RESOLVED (14/16)**：R1-N1, R1-N2, R1-N3, R1-N4, R1-N5, R1-W2, R1-W3, R1-W4, R1-W5, R1-W6, REV-ADD-2, REV-ADD-3 + 原 Round 1 minor issues（h2o bib title 之外的所有 minor）。

**PARTIALLY RESOLVED (1/16)**：R1-W1（sensitivity analysis 充分但 "following ThinKV" 仍误导 + quartile/quintile 仅 n=50）。

**新发现 (2)**：
- NEW-W1: n=50 / n=500 数据混合在 main body（Table 2 + crossover）引起混淆
- NEW-W2: Crossover claim 未在 n=500 上验证

**评分变化理由**：所有 5 个 critical issues 已 resolved；sample size 从 50→500 使核心 findings 在统计上无可争议；claims scoping（title, abstract, contributions, cross-arch framing）显著改善；robustness analyses（segmentation, mpl, BH-FDR）增强说服力。残留 issues 均为 should-fix 或 minor 级别，不影响核心 contribution 的可信度。从 Borderline Findings (2.5) 上调至 Borderline Conference (3.5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 318 · 2026-05-15T10:57:51.893052+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 22

## Round 22

2 recorded events


### User

_source line 319 · 2026-05-15T10:57:54.555376+00:00_

[Reviewer 1 审稿结果]:
报告已提交。

总结：16 个 issues 中 14 个 RESOLVED、1 个 PARTIALLY RESOLVED（R1-W1 segmentation），新发现 2 个 warning 级问题（n=50/n=500 数据混合引起 Table 2 + crossover analysis 的混淆；crossover claim 未在 n=500 上验证）。Overall 评分从 2.5 上调至 3.5/5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 320 · 2026-05-15T10:58:00.148104+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 23

## Round 23

34 recorded events


### User

_source line 321 · 2026-05-15T10:58:21.500802+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 5 修订评估（新颖性/完整性）

---

## 逐条 Issue 判定

### [R1-N1] critical: Placeholders — **[RESOLVED]**

`\placeholder` 命令定义仍保留在 main.tex line 21，但 grep 确认全文无任何实际调用。所有数据已填充：

- **Table 4 (LLaMA cross-arch)**：4 行数据完整（$\widetilde{\Delta}$: 0.020→0.356，CI 和 p 值均有）
- **Discussion oracle pilot**：oracle 18% (p=0.002)、heuristic 32% (p=0.024)
- **Qwen null rate**：45.2%，含 lag-1 autocorrelation 解释 (methodology.tex line 10)
- **Per-problem concordance**：mean ρ=−0.107, p=0.926（appendix_moved.tex line 73）
- **n_LLAMA**：明确 n=49（Table 4 caption）
- **Random eviction Qwen s≥0.25**：Δ=0.39/0.91, p 值完整（appendix_moved.tex line 76）

建议删除 `\newcommand{\placeholder}` 定义以保持 source 整洁，但不影响接收判断。

---

### [R2-N3] warning: HIES 区分不足 — **[RESOLVED]**

修改充分。两处关键增补：

1. **Related Work** (related_work.tex line 18)："HIES independently show that importance-based head discrimination collapses under heavy **single-axis** pruning. Our work extends this to the **compound** setting, revealing that collapse is amplified by the interaction of two compression axes and **modulated by reasoning phase**—phenomena absent in single-axis analysis. **The crossover effect (§5.3) is a prediction that single-axis frameworks cannot generate.**"

2. **Analysis §6.1** (analysis.tex line 7)：同样明确 "extends this to the compound setting, where collapse is amplified by the interaction of two compression axes and modulated by reasoning phase."

关键 novelty delta 现在清晰：(a) single-axis → compound amplification, (b) phase modulation, (c) crossover 作为 HIES 无法生成的 prediction。这三点有效区分了两项工作。

---

### [R2-W3] warning: Missing references RLKV/LongFlow/PM-KVQ — **[RESOLVED]**

三篇均已引用且位置恰当：
- **PM-KVQ** (related_work.tex line 10)：置于 compound compression 段落，关联 "temporal dimension to compression severity"——恰当
- **RLKV + LongFlow** (related_work.tex line 19)：置于 KV cache eviction 段落——恰当
- references.bib 均有完整条目；verify_references 确认 RLKV (verified)、LongFlow (verified)、PM-KVQ (verified)

小问题：LongFlow bib entry 含 `note = {Withdrawn from ICLR 2026}`。引用 withdrawn paper 需要审慎——建议删除 ICLR 2026 note 或在正文中标注仅引用 arXiv 版本。

---

### [R2-W5] warning: Abstract 过长过密 — **[RESOLVED]**

修改显著改善。对比：
- **Round 1**：14 行，含 3 个完整模型名、4 个 sparsity level 的详细 d_z/p/median 数据、cross-architecture 详细数字
- **Round 5**：10 行，结构清晰——(1) 问题 → (2) DeepSeek headline (Δ:0.39→8.48, p<10^-69) → (3) random baseline as contrast → (4) crossover 一句 → (5) Qwen replication → (6) LLaMA "preliminary" → (7) mechanism "correlates with" → (8) implication

LLaMA 现在仅 "preliminary cross-architecture evidence...suggesting the phenomenon may extend beyond Qwen2-family architectures"——远比 Round 1 的详细数字更审慎。Mechanism 使用 "correlates with" 而非 "explains"。

---

### [R2-Minor-1] info: h2o bib / author mismatch — **[RESOLVED]**

h2o-neurips2023 bib entry 现在有 title：`{H\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models`。verify_references 仍报告 "skipped (no title)" 是因为 parser 未处理 LaTeX `\textsubscript` 命令，但实际 bib 内容正确。

Author mismatch 状况与 Round 1 相同（deepseek-r1, snapkv, unicomp, qwen25），均为 API 记录差异，非实质性错误。

---

### [R2-Minor-2] info: REVIEWER-ATTACK/REBUTTAL 注释 — **[RESOLVED]**

Grep 确认全文零匹配。所有 REVIEWER-ATTACK/REBUTTAL LaTeX comments 已完全删除。

---

### [R2-Minor-6] info: s=0.35 未完整报告 — **[RESOLVED]**

原 appendix_disc_analysis.tex 中引用 "s=0.35 high-phase II rises to 0.105" 的那段已被重写，现在仅引用 s≤0.30 数据（line 11: "$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$"），不再引用未完整报告的 supplementary experiment。

---

### [R1-Minor-code] info: 无代码/数据声明 — **[RESOLVED]**

main.tex lines 47-48 新增 `\section*{Reproducibility}` 声明："Code and data will be released upon acceptance." 此外，methodology.tex 现在报告 bootstrap seed=42。

---

## 额外检查

### 1. Random eviction 叙事变化

**诚实且恰当处理。** Round 1 的 "7/8 conditions non-significant" 和 "flat baseline ($G \approx 1$)" 已被替换为更精确的叙事：

- Results §5.1 (line 8)："Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant...at $s \geq 0.25$, $\Delta$ becomes significant...but $15$–$39{\times}$ smaller"
- Discussion §7 (line 5)："The near-unity random baseline ($G{=}0.5$–$1.3{\times}$, trivial magnitude) confirms the **dominant** amplification is strategy-specific"
- Contribution 1 (Introduction line 22)："$3$–$39{\times}$ larger than under random eviction"

从 "flat baseline" → "dominant but not exclusive driver" 是一个 honest 的叙事转变，正确反映了 n=500 的更高统计功效。未试图隐藏 random eviction 在高 sparsity 下也有 detectable gradient。

### 2. Contribution 措辞

三个 contributions 现在恰当反映 evidence strength：

1. ~~"absent under random eviction"~~ → "**$3$–$39{\times}$ larger** than under random eviction" — 更精确
2. ~~"replicates across three models spanning two architectures"~~ → "replicates across **two Qwen2-architecture models**...with **exploratory evidence** from a LlamaForCausalLM model **suggesting** the phenomenon **may** extend beyond Qwen2" — 大幅降低了 overclaim
3. "propose entropy-discrimination collapse as a mechanistic explanation" — 保持 "propose" 措辞，恰当

### 3. n=50 profiling tables 与 n=500 共存

Table 2 (per-phase breakdown, n=50) 和 Table 6 (permutation test, n=49) 显式标注为 "profiling subset"，并 forward-reference 到 n=496 的 Table 1。这是 coherent 的——profiling tables 提供了 per-phase 细粒度数据，n=500 tables 提供了统计功效。

**一个潜在困惑点**：Table 2 的 G 值 (69×–274×) 与正文 n=496 的 G 值 (30×–148×) 差异显著，因为 n=500 包含了更多 "average" 问题稀释了 profiling subset 中的极端值。Discussion (line 5) 使用 "G=30–148×" 但 Table 2 仍显示 69–274×。虽然标注了 subset 来源，但 **建议在 Table 2 caption 或正文中简短解释为何 profiling subset G 高于 full sample G**。

### 4. 新引用验证

- **RLKV** (rlkv-2025): OpenAlex verified, arXiv:2510.08525 ✓
- **LongFlow** (longflow-2026): OpenAlex verified, arXiv:2603.11504 ✓ (但 bib note 标注 "Withdrawn from ICLR 2026")
- **PM-KVQ** (pmkvq-iclr2026): OpenAlex verified, ICLR 2026 ✓

无幻觉引用。

### 5. "following ThinKV" 措辞

background.tex line 33 仍然写 "following ThinKV"。R1-W1 指出 ThinKV 使用 explicit `&lt;think>` delimiters，而本文使用 quantile-based tercile——方法不同。新增的 segmentation robustness 分析 (Appendix §I, §J) 验证了 tercile/quartile/quintile 和 mpl 的鲁棒性，但 **措辞仍具误导性**。

**[STILL OPEN - minor]** 建议改为 "inspired by ThinKV's phase distinction" 或 "analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters."

### 6. 整体影响力评估变化

n=500 将 Bonferroni p-values 推到了 $<10^{-69}$（DeepSeek）和 $<10^{-14}$（Qwen），配合 BH-FDR 44-test correction、segmentation robustness、mpl sensitivity，统计 soundness 不再是问题。这改变了我对论文价值的判断：

- Round 1 时主要疑虑是 **数据不完整**（placeholders）和 **统计证据边缘**（n=50，Qwen s=0.15 CI 含零）
- Round 5 这两个问题均已消除。Qwen s=0.15 的 $\Delta{=}0.07$ [0.05, 0.09] 现在 CI 排除零
- 论文的核心价值——对 compound sparsity 的 phase-dependent severity 的首次系统量化——在统计上得到了坚实支撑

---

## 新发现的问题

### [NEW-1] minor: Table 2 与正文 G 值不一致可能引起困惑

Table 2 (profiling, n=50) 报告 G=69×–274×；正文/Discussion 使用 n=496 的 G=30×–148×。两者均有标注，但落差大（~2×）且无解释。读者可能疑惑为何 G 在更大 sample 上反而更小。

建议在 Table 2 caption 加一句："Full-sample ($n{=}496$) bootstrap $G$ ranges from $30{\times}$ to $148{\times}$, reflecting dilution by lower-severity problems absent in the profiling subset."

### [NEW-2] minor: LongFlow 引用标注 "Withdrawn from ICLR 2026"

references.bib 的 longflow-2026 entry 含 `note = {Withdrawn from ICLR 2026}`。引用 withdrawn paper 虽非禁忌（arXiv 版本仍存在），但可能引起 reviewer 质疑。建议删除 note 或改为仅引用 arXiv preprint。

### [NEW-3] info: `\placeholder` 命令定义仍在 main.tex

虽无实际调用，但保留 `\newcommand{\placeholder}` 在提交源码中不够整洁。建议删除。

---

## 总体评分更新建议

| 维度 | Round 1 | Round 5 | 变化理由 |
|------|---------|---------|----------|
| **Soundness** | 3.0 | **3.5** | n=500 + BH-FDR 44 tests + segmentation/mpl robustness 消除了统计疑虑；correlational mechanism 现在明确标注 |
| **Excitement** | 2.5 | **3.0** | 核心 finding 未变但 evidence strength 大幅提升；crossover 和 quantitative surprise (30–148×) 对 deployment practitioners 有实际价值；仍是 empirical finding 而非 method |
| **Overall** | 2.5 | **3.5** | 从 "resubmit" 提升到 "Findings / borderline Conference"。所有 critical issues resolved，honest framing，thorough robustness。限制因素：单一 benchmark (MATH-500)、无方法贡献、cross-architecture evidence 仍弱 |
| **Reproducibility** | 3.0 | **3.5** | Reproducibility statement + seed=42 + 详细 methodology；但仍 "upon acceptance"，非预发布 |
| **Confidence** | 4 | **4** | 无变化 |

**一句话**：论文从 Round 1 的 incomplete submission 提升为一篇统计严谨、honest framing 的 empirical characterization paper。所有 critical issues 已解决，remaining issues 均为 minor。推荐 **Findings**；如果 AC 重视 compound sparsity 的 deployment-relevant characterization，borderline Conference 也可接受。

---

## Open Issues 总结

| Issue | Status | Severity |
|-------|--------|----------|
| "following ThinKV" 措辞 | STILL OPEN | minor |
| Table 2 vs 正文 G 值落差未解释 | NEW | minor |
| LongFlow "Withdrawn" note | NEW | minor |
| `\placeholder` 命令定义残留 | NEW | trivial |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-15T10:58:49.817498+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "5",
  "text": "## 交叉分享 — Reviewer 2 的 Round 5 修订评估\n\n请逐条回应 [AGREE] 或 [REBUT]。Reviewer 2 评估了全部 issue，结论如下：\n\n### Issue 判定（均 RESOLVED）\n- R1-N1 placeholders: RESOLVED（同你）\n- R2-N3 HIES 区分: RESOLVED\n- R2-W3 missing refs: RESOLVED\n- R2-W5 abstract: RESOLVED\n- R2-Minor-1 h2o bib: RESOLVED\n- R2-Minor-2 REVIEWER-ATTACK: RESOLVED\n- R2-Minor-6 s=0.35: RESOLVED\n- R1-Minor-code: RESOLVED\n\n### \"following ThinKV\" 措辞\nR2 判定 STILL OPEN (minor)，与你的 R1-W1 PARTIALLY RESOLVED 一致。R2 建议改为 \"inspired by ThinKV's phase distinction\" 或 \"analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters.\"\n\n### R2 新发现\n**[NEW-1] minor**: Table 2 (n=50 profiling, G=69-274×) vs 正文 (n=496, G=30-148×) 落差~2× 未解释。建议 Table 2 caption 加一句解释。——与你的 NEW-W1 高度重叠。\n\n**[NEW-2] minor**: LongFlow bib entry 含 \"Withdrawn from ICLR 2026\" note，可能引起 reviewer 质疑。建议删除。\n\n**[NEW-3] trivial**: `\\placeholder` 命令定义残留。\n\n### R2 额外观察\n- Random eviction 叙事变化处理得当（\"dominant but not exclusive driver\"，honest framing）\n- Contribution 措辞恰当（从 overclaim 降为 hedged）\n- n=500 将 p-values 推至 <10^-69，统计 soundness 不再是问题\n\n### R2 评分\nOverall: 2.5 → 3.5/5（与你一致）。推荐 Findings track。\n\n请回应：(1) 对 R2 的 issue 判定是否同意？(2) NEW-2 (LongFlow withdrawn) 你的看法？(3) 你的 NEW-W2 (crossover 未在 n=500 验证) R2 未提及——你是否维持这个 warning？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "5",
    "text": "## 交叉分享 — Reviewer 2 的 Round 5 修订评估\n\n请逐条回应 [AGREE] 或 [REBUT]。Reviewer 2 评估了全部 issue，结论如下：\n\n### Issue 判定（均 RESOLVED）\n- R1-N1 placeholders: RESOLVED（同你）\n- R2-N3 HIES 区分: RESOLVED\n- R2-W3 missing refs: RESOLVED\n- R2-W5 abstract: RESOLVED\n- R2-Minor-1 h2o bib: RESOLVED\n- R2-Minor-2 REVIEWER-ATTACK: RESOLVED\n- R2-Minor-6 s=0.35: RESOLVED\n- R1-Minor-code: RESOLVED\n\n### \"following ThinKV\" 措辞\nR2 判定 STILL OPEN (minor)，与你的 R1-W1 PARTIALLY RESOLVED 一致。R2 建议改为 \"inspired by ThinKV's phase distinction\" 或 \"analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters.\"\n\n### R2 新发现\n**[NEW-1] minor**: Table 2 (n=50 profiling, G=69-274×) vs 正文 (n=496, G=30-148×) 落差~2× 未解释。建议 Table 2 caption 加一句解释。——与你的 NEW-W1 高度重叠。\n\n**[NEW-2] minor**: LongFlow bib entry 含 \"Withdrawn from ICLR 2026\" note，可能引起 reviewer 质疑。建议删除。\n\n**[NEW-3] trivial**: `\\placeholder` 命令定义残留。\n\n### R2 额外观察\n- Random eviction 叙事变化处理得当（\"dominant but not exclusive driver\"，honest framing）\n- Contribution 措辞恰当（从 overclaim 降为 hedged）\n- n=500 将 p-values 推至 <10^-69，统计 soundness 不再是问题\n\n### R2 评分\nOverall: 2.5 → 3.5/5（与你一致）。推荐 Findings track。\n\n请回应：(1) 对 R2 的 issue 判定是否同意？(2) NEW-2 (LongFlow withdrawn) 你的看法？(3) 你的 NEW-W2 (crossover 未在 n=500 验证) R2 未提及——你是否维持这个 warning？"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-15T10:59:04.960614+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15143
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-15T10:59:05.061997+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "5",
  "text": "## 交叉分享 — Reviewer 1 的 Round 5 修订评估\n\n请逐条回应 [AGREE] 或 [REBUT]。Reviewer 1 评估了全部 16 个 issues，结论如下：\n\n### Issue 判定\n- R1-N1 ~ R1-N5: 全部 RESOLVED（与你一致）\n- R1-W1 (phase segmentation): PARTIALLY RESOLVED（sensitivity analysis 充分但 \"following ThinKV\" 仍误导 + quartile/quintile 仅 n=50）——与你一致\n- R1-W2 ~ R1-W6, REV-ADD-2, REV-ADD-3: 全部 RESOLVED\n- Overall: 2.5 → 3.5/5\n\n### R1 新发现\n\n**[NEW-W1] warning: n=50 与 n=500 数据混合引起混淆**\n- Table 2 (n=50, Δ_s030=14.59, G=274×) vs Table 1 (n=496, Δ_s030=8.48, G=148×)——差异 42-85%\n- 建议将 Table 2 移至 Appendix 或在 main body 补充 n=500 per-phase table\n- 与你的 NEW-1 高度重叠，但 R1 将其定为 warning 级别（你定为 minor）\n\n**[NEW-W2] warning: Crossover analysis (§5.3) 未在 n=500 上验证**\n- §5.3 引用的具体数值（imp high=0.032 vs rand high=0.818 等）全部来自 n=50\n- 鉴于 n=50→n=500 的 Δ 变化达 40%，crossover magnitude 可能在 n=500 下不同\n- 建议在 n=500 上重新计算并更新\n\n**额外观察：**\n- Segmentation robustness quartile/quintile 仅 n=50——既然有 n=500 数据应验证\n- LLaMA 仍为 n=49，与 DS/QW n=500 对比更显 underpowered（但 \"exploratory\" 标注诚实）\n\n### R1 评分\nSoundness: 2.5→3.5; Excitement: 3.0→3.0; Reproducibility: 2.0→3.5; Overall: 2.5→3.5\n\n请回应：(1) 对 R1 的 issue 判定是否同意？(2) NEW-W1——你定为 minor，R1 定为 warning，你维持哪个 severity？(3) NEW-W2 (crossover 未在 n=500 验证)——你是否同意这是一个需要关注的问题？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "5",
    "text": "## 交叉分享 — Reviewer 1 的 Round 5 修订评估\n\n请逐条回应 [AGREE] 或 [REBUT]。Reviewer 1 评估了全部 16 个 issues，结论如下：\n\n### Issue 判定\n- R1-N1 ~ R1-N5: 全部 RESOLVED（与你一致）\n- R1-W1 (phase segmentation): PARTIALLY RESOLVED（sensitivity analysis 充分但 \"following ThinKV\" 仍误导 + quartile/quintile 仅 n=50）——与你一致\n- R1-W2 ~ R1-W6, REV-ADD-2, REV-ADD-3: 全部 RESOLVED\n- Overall: 2.5 → 3.5/5\n\n### R1 新发现\n\n**[NEW-W1] warning: n=50 与 n=500 数据混合引起混淆**\n- Table 2 (n=50, Δ_s030=14.59, G=274×) vs Table 1 (n=496, Δ_s030=8.48, G=148×)——差异 42-85%\n- 建议将 Table 2 移至 Appendix 或在 main body 补充 n=500 per-phase table\n- 与你的 NEW-1 高度重叠，但 R1 将其定为 warning 级别（你定为 minor）\n\n**[NEW-W2] warning: Crossover analysis (§5.3) 未在 n=500 上验证**\n- §5.3 引用的具体数值（imp high=0.032 vs rand high=0.818 等）全部来自 n=50\n- 鉴于 n=50→n=500 的 Δ 变化达 40%，crossover magnitude 可能在 n=500 下不同\n- 建议在 n=500 上重新计算并更新\n\n**额外观察：**\n- Segmentation robustness quartile/quintile 仅 n=50——既然有 n=500 数据应验证\n- LLaMA 仍为 n=49，与 DS/QW n=500 对比更显 underpowered（但 \"exploratory\" 标注诚实）\n\n### R1 评分\nSoundness: 2.5→3.5; Excitement: 3.0→3.0; Reproducibility: 2.0→3.5; Overall: 2.5→3.5\n\n请回应：(1) 对 R1 的 issue 判定是否同意？(2) NEW-W1——你定为 minor，R1 定为 warning，你维持哪个 severity？(3) NEW-W2 (crossover 未在 n=500 验证)——你是否同意这是一个需要关注的问题？"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-15T10:59:06.572706+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-15T11:01:30.714242+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-15T11:01:30.787287+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 73
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-15T11:01:33.751609+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-15T11:01:33.802340+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-15T11:01:34.556147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_reports/round_4.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_reports/round_4.md"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-15T11:01:34.607272+00:00_

1	---
2	round: 4
3	overall_score: weak reject
4	timestamp: 2026-05-15T07:49:59.758091+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	
11	# 圆桌审稿报告 — Round 1
12	
13	**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
14	**Venue**: EMNLP 2026 ARR (Main Conference)
15	**截止日期**: 2026-05-25
16	**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）
17	**轮次**: Round 1（独立审稿 + 交叉分享完成，达成收敛）
18	
19	---
20	
21	## Summary
22	
23	本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）在 reasoning model 生成过程中的 phase-dependent severity。核心发现：在 importance-based eviction 下，compound interaction 的严重程度（以 Interaction Index 衡量）集中在 low-sparsity reasoning phases，severity gradient 从 69× (s=0.15) 增长到 274× (s=0.30)；random eviction 无此现象（7/8 conditions non-significant）。在 Qwen2.5-7B-Instruct 上部分复现（s≥0.20），在 LlamaForCausalLM 上仅获得微弱方向性一致证据。提出 entropy-discrimination collapse 作为机制解释。
24	
25	---
26	
27	## Strengths
28	
29	**S1** [consensus] **研究问题有价值且定义清晰**。将 compound sparsity 的 phase-invariance assumption 作为明确攻击目标，对 efficient inference 部署有直接指导意义。
30	
31	**S2** [consensus] **统计方法论严谨**。非参数 bootstrap (B=10,000)、paired permutation tests、Bonferroni correction、Cohen's d_z、报告中位数处理右偏分布——统计意识优于绝大多数 ML 论文。
32	
33	**S3** [consensus] **Random eviction 作为 falsification control 设计巧妙**。7/8 conditions 下 random eviction 无显著 phase gradient，有效隔离了 strategy-specific amplification，构成强 counterfactual。
34	
35	**S4** [consensus] **Crossover 发现有 non-trivial insight**。§5.3 的 strategy ranking reversal（importance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）对部署有直接启示——uniform budget 必然在某个 phase 是 suboptimal 的。
36	
37	**S5** [consensus] **Multiplicative null verification** (Appendix A) 增强了 Interaction Index 定义的鲁棒性。
38	
39	**S6** [consensus] **Limitations 写作坦诚**，多数局限在 limitations section 中有诚实讨论。
40	
41	---
42	
43	## Weaknesses（按严重性排序）
44	
45	### Must-Fix（影响接收决定）
46	
47	**MF1** [critical, consensus
…[truncated 10254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-15T11:01:40.779015+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-15T11:01:40.829955+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "40+ placeholders unfilled — paper not submission-ready (Table 4 entirely empty, Discussion oracle data missing, Abstract incomplete)"
4	    category: experiment
5	    severity: critical
6	    status: in_progress
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2]
12	        note: "Both reviewers independently flagged as #1 critical issue."
13	    action_items:
14	      - round: 1
15	        action: "n=500 analysis complete → Paper Agent fills all placeholders (Table 4, Abstract, §5.4, §7 oracle, Appendix). CSV export bug (DS s030 missing) must be fixed first."
16	        assigned_to: "main_agent → paper_agent"
17	        status: in_progress
18	    resolution: ""
19	    resolution_round: null
20	
21	  - id: "R1-N4"
22	    summary: "Cross-architecture (LLaMA) evidence too weak to support title/abstract framing — 1/4 conditions significant, ~1/40 magnitude, random eviction also shows phase gradient"
23	    category: framing
24	    severity: critical
25	    status: in_progress
26	    first_raised_round: 1
27	    last_seen_round: 1
28	    mentions:
29	      - round: 1
30	        reviewers: [1, 2]
31	        note: "R1-N4 = R2-N2. Both agree LLaMA evidence is overclaimed."
32	    action_items:
33	      - round: 1
34	        action: "Downgrade LLaMA to 'exploratory cross-architecture analysis'; Title keep 'Reasoning Models' but Abstract/Contribution hedge; §5.5 rename from 'validation' to 'exploratory analysis'"
35	        assigned_to: "paper_agent"
36	        status: in_progress
37	    resolution: ""
38	    resolution_round: null
39	
40	  - id: "R1-N3"
41	    summary: "Single benchmark (MATH-500, 50 problems) severely limits generalization — title/abstract say 'reasoning models' but only math reasoning tested"
42	    category: experiment
43	    severity: critical
44	    status: in_progress
45	    first_raised_round: 1
46	    last_seen_round: 1
47	    mentions:
48	 
…[truncated 15132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-15T11:02:15.936254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-15T11:02:16.843040+00:00_

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\section*{Reproducibility}
48	Code and data will be released upon acceptance.
49	
50	\appendix
51	\input{appendix}
52	\input{appendix_moved}
53	\input{appendix_disc_analysis}
54	\input{appendix_robustness}
55	
56	\end{document}
57	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-15T11:02:16.843578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-15T11:02:16.994828+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$39{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger. % exp_id: n500_unified_final; DS imp Δ 0.39→8.48, rand 0.01→0.51; JT z=33.7 (imp), 6.2 (rand)
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\ % exp_id: n500_unified_final; DS imp median_ii_diff
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\ % exp_id: n500_unified_final; DS rand median_ii_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown from an
…[truncated 9653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-15T11:02:16.995235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-15T11:02:17.045943+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are
…[truncated 1994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-15T11:02:22.020646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-15T11:02:22.573677+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$39{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We observe that discrimination collapse---head pruning flattening cumulative importance scores---correlates with the phase-dependent severity amplification, suggesting a mechanism whereby compound sparsity selectively degrades importance-based eviction in distributed-attention phases.
9	These findings motivate phase-aware compression budgets for mathematical reasoning models.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-15T11:02:22.574223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-15T11:02:22.976567+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 2353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-15T11:02:23.027257+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-15T11:02:23.078129+00:00_

1	\section{Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	\subsection{Discrimination Collapse}
5	\label{sec:discrimination-collapse-main}
6	
7	We observe that head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient of importance scores decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). This pattern---which we term \emph{discrimination collapse}---is consistent with importance-based eviction degenerating into noise-sensitive selection when score distributions flatten. The effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. This observation is independently corroborated by \cite{hies-2025}, who report importance score collapse under heavy single-axis pruning; our results extend this to the compound setting, where collapse is amplified by the interaction of two compression axes and modulated by reasoning phase. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
8	
9	A partial counterfactual supports this interpretation: random eviction does not rely on importance scores, so it is immune to score-distribution changes caused by head pruning. The flat severity gradient under random eviction ($G \approx 1$) is consistent with this independence, while importance-based eviction---whose decisions depend on the very scores that pruning degrades---exhibits the phase-modulated amplification. We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
10	
11	\subsection{Entropy Redistribu
…[truncated 897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-15T11:03:10.378192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool call

_source line 347 · 2026-05-15T11:03:10.378628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 348 · 2026-05-15T11:03:10.429138+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
12	
13	\paragraph{KV cache eviction.}
14	Most methods rely on importance scoring whose reliability is increasingly questioned.
15	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
16	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
17	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
18	\cite{hies-2025} independently show
…[truncated 2273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-15T11:03:10.429632+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($G{=}30$--$148{\times}$ at $n{=}496$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The near-unity random baseline ($G{=}0.5$--$1.3{\times}$, trivial magnitude) confirms the dominant amplification is strategy-specific. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\% (Wilcoxon $p = 0.002$), below the pre-registe
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-15T11:05:04.926616+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"40+ placeholders unfilled — paper not submission-ready\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged as #1 critical issue.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All placeholders filled: Table 4 (LLaMA) populated, Abstract complete, Discussion oracle data (18%/32%) filled, Appendix tables complete. Grep confirms zero \\\\placeholder usage.\"\n    action_items:\n      - round: 1\n        action: \"Fill all placeholders with n=500 analysis data\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All 40+ placeholders filled with experimental data from n=500 analysis.\"\n    resolution_round: 5\n\n  - id: \"R1-N4\"\n    summary: \"Cross-architecture (LLaMA) evidence too weak to support title/abstract framing\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree LLaMA evidence is overclaimed.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §5.5 renamed 'Exploratory Cross-Architecture Analysis'; Abstract uses 'preliminary cross-architecture evidence'; Contribution 2 says 'exploratory evidence from LlamaForCausalLM'. Hedging appropriate throughout.\"\n    action_items:\n      - round: 1\n        action: \"Downgrade LLaMA to exploratory; hedge title/abstract/contribution\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"LLaMA downgraded to exploratory with appropriate hedging in title, abstract, and contributions.\"\n    resolution_round: 5\n\n  - id: \"R1-N3\"\n    summary: \"Single benchmark (MATH-500) severely limits generalization — title/abstract say 'reasoning models' but only math reasoning tested\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree single benchmark is major limitation.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Title changed to 'Mathematical Reasoning Models'. Limitations expanded with MATH-500 justification (phase transitions, per-problem evaluation, difficulty variation). Task coverage paragraph lists code/science/multi-hop as future work.\"\n    action_items:\n      - round: 1\n        action: \"Scope title/abstract to mathematical reasoning; expand limitations\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Title scoped to 'Mathematical Reasoning Models'; limitations section provides MATH-500 justification and lists extension domains.\"\n    resolution_round: 5\n\n  - id: \"R1-N2\"\n    summary: \"50-problem sample size lacks power analysis; exclusion criteria unclear\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Reviewer corrects: use CI width shrinkage instead of post-hoc power.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=500 (all MATH-500). Exclusion criteria stated: DS 4, QW 25. CI width shrinkage 2.5-5.9× reported. All p < 10^-69 (DS) and 10^-14 (QW). Power concerns eliminated.\"\n    action_items:\n      - round: 1\n        action: \"Run n=500; report exclusion criteria and CI shrinkage\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Full n=500 dataset used; exclusion criteria, effective n, and CI width shrinkage all reported in Methodology.\"\n    resolution_round: 5\n\n  - id: \"R1-N5\"\n    summary: \"Mechanism analysis (entropy-discrimination collapse) is purely correlational\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Reviewer confirms: can downgrade to warning if §6 properly scoped.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §6 title changed to 'Discrimination Collapse under Compound Sparsity'. Split: §6.1 discrimination collapse (robust, 16/16), §6.2 entropy redistribution (model-dependent). 'correlational' explicitly stated. Causal validation → future work.\"\n    action_items:\n      - round: 1\n        action: \"Split §6; add 'correlational' caveat; causal → future work\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"§6 restructured with honest correlational framing; discrimination collapse separated from model-dependent entropy redistribution.\"\n    resolution_round: 5\n\n  - id: \"R2-N3\"\n    summary: \"Insufficient differentiation from HIES (2025)\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Clear delta exists but paper doesn't articulate it.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §6.1 has explicit HIES comparison: 'independently corroborated by [HIES], who report importance score collapse under heavy single-axis pruning; our results extend this to the compound setting'. Related Work §2 also has dedicated HIES paragraph. Crossover identified as prediction HIES cannot generate.\"\n    action_items:\n      - round: 1\n        action: \"Add explicit HIES comparison in Related Work and §6\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Explicit HIES comparison added in both Related Work and Analysis sections.\"\n    resolution_round: 5\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation lacks justification; 'following ThinKV' wording misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need sensitivity analysis and correct ThinKV reference.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. Sensitivity analysis added: mpl {5,10,20} (Appendix C), quartile/quintile segmentation (Appendix D). min_phase_length justified. BUT 'following ThinKV' wording still in background.tex line 33 — ThinKV uses explicit &lt;think> delimiters, not quantile boundaries.\"\n    action_items:\n      - round: 1\n        action: \"Add sensitivity analysis; correct ThinKV phrasing\"\n        assigned_to: \"paper_agent\"\n        status: in_progress\n      - round: 5\n        action: \"Fix 'following ThinKV' in background.tex:33 — change to 'inspired by' or remove ThinKV from segmentation description\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Symmetric sparsity rate assumption lacks practical representativeness\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree needs discussion.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Dedicated 'Symmetric sparsity assumption' paragraph in Limitations.\"\n    action_items:\n      - round: 1\n        action: \"Add limitations paragraph\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Symmetric sparsity assumption discussed in Limitations with asymmetric extension as future work.\"\n    resolution_round: 5\n\n  - id: \"R1-W3\"\n    summary: \"Severity gradient G numerically unstable when II_high approaches zero\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree. Need bootstrap CI for G.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Δ (paired median diff) is now primary metric. G demoted to auxiliary with bootstrap CIs reported: [26,37] to [119,171]. §4 explicitly states 'G is reported as an auxiliary metric; Δ is primary'.\"\n    action_items:\n      - round: 1\n        action: \"Report G CIs; demote to auxiliary\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"G demoted to auxiliary metric with bootstrap CIs; Δ is primary throughout.\"\n    resolution_round: 5\n\n  - id: \"R1-W4\"\n    summary: \"Bonferroni correction scope (k=4) may be insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Supplement with BH-FDR.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. k=4 per model×strategy family justified in §4. BH-FDR correction across all 44 tests in Appendix B — all 32 Bonferroni-significant results remain significant under BH-FDR; 5 BH-only results are all in random-eviction conditions.\"\n    action_items:\n      - round: 1\n        action: \"Justify k=4; add BH-FDR appendix\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"k=4 family structure justified; BH-FDR appendix confirms no importance-based findings lost.\"\n    resolution_round: 5\n\n  - id: \"R1-W5\"\n    summary: \"Spearman rho=1.0 on 4 points over-interpreted\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need n=4 caveat; use JT test at n=500.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Spearman annotated with n=4 and one-tailed. JT test added (z=6.2-33.7, p<10^-9) using per-problem values (~496 per group). Both tests reported in §4.\"\n    action_items:\n      - round: 1\n        action: \"Annotate Spearman n=4; add JT test\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Spearman properly caveated; JT test provides n=500-level dose-response evidence.\"\n    resolution_round: 5\n\n  - id: \"R1-W6\"\n    summary: \"Exclusion criteria not stated in Methodology\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Merged with R1-N2.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Methodology §4 states: DS 4 excluded (degenerate phase), QW 25 excluded. Qwen mid-phase null rate 45.2% explained with lag-1 autocorrelation.\"\n    action_items:\n      - round: 1\n        action: \"Report exclusion criteria in §4\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Exclusion criteria and effective n fully reported in Methodology.\"\n    resolution_round: 5\n\n  - id: \"R2-W3\"\n    summary: \"Related Work missing RLKV, LongFlow, PM-KVQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2-W3. R1 partially agrees.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All three added: RLKV in KV cache eviction paragraph, LongFlow in same paragraph, PM-KVQ in compound compression paragraph with temporal dimension link.\"\n    action_items:\n      - round: 1\n        action: \"Assess relevance and cite\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"RLKV, LongFlow, PM-KVQ integrated into Related Work with appropriate contextual framing.\"\n    resolution_round: 5\n\n  - id: \"R2-W5\"\n    summary: \"Abstract too long and dense\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both independently flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Rewritten: ~10 lines, structured (problem → finding → replication → mechanism → implication). LLaMA stats moved to Results. Readable.\"\n    action_items:\n      - round: 1\n        action: \"Condense abstract\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Abstract condensed to ~10 lines with clear structure.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-2\"\n    summary: \"LaTeX source contains REVIEWER-ATTACK/REBUTTAL comments\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Should clean before submission.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Deleted from appendix_disc_analysis.tex and other files.\"\n    action_items:\n      - round: 1\n        action: \"Remove all REVIEWER-ATTACK/REBUTTAL comments\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All reviewer-strategy comments removed from LaTeX source.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-1\"\n    summary: \"h2o-neurips2023 bib entry missing title field; citation quality issues\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both flagged.\"\n      - round: 5\n        reviewers: [2]\n        note: \"PARTIALLY RESOLVED. h2o title field added. But LongFlow bib entry contains 'Withdrawn from ICLR 2026' note — citing a withdrawn paper needs careful framing or removal.\"\n    action_items:\n      - round: 1\n        action: \"Fix h2o bib entry\"\n        assigned_to: \"main_agent\"\n        status: done\n      - round: 5\n        action: \"Address LongFlow 'Withdrawn from ICLR 2026' note — either remove citation or add caveat\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-6\"\n    summary: \"s=0.35 supplementary experiment mentioned but not fully reported\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Either report fully or remove.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Removed from Appendix.\"\n    action_items:\n      - round: 1\n        action: \"Remove s=0.35 mention\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"s=0.35 incomplete data removed.\"\n    resolution_round: 5\n\n  - id: \"R1-Minor-code\"\n    summary: \"No code or data release plan\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both noted.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Reproducibility section added in main.tex: 'Code and data will be released upon acceptance.'\"\n    action_items:\n      - round: 1\n        action: \"Add code/data release statement\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Reproducibility statement added.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-1\"\n    summary: \"paper_provenance.yaml C019 outdated\"\n    category: framing\n    severity: warning\n    status: wont_fix\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"Internal process issue, not a paper defect.\"\n      - round: 5\n        reviewers: []\n        note: \"Internal provenance tracking — not visible to venue reviewers. Marking wont_fix for review tracker purposes.\"\n    action_items:\n      - round: 1\n        action: \"Update C019 in paper_provenance.yaml\"\n        assigned_to: \"director\"\n        status: wont_fix\n    resolution: \"Internal process issue, not tracked as paper defect.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-2\"\n    summary: \"Random masking s025+ significant gradient needs explicit paper treatment\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"D063 threshold story needs integration.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §5.1 integrates threshold story: 'Random eviction develops a detectable but weak phase gradient above s≈0.20...15-39× smaller than importance-based'. Cross-model replication (§5.4) mirrors pattern on Qwen. Extended Discussion covers random masking as falsification control.\"\n    action_items:\n      - round: 1\n        action: \"Integrate random threshold story in Results\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Random eviction threshold story fully integrated in Results and Discussion.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-3\"\n    summary: \"Qwen mid-phase 45.2% null rate needs effective n caveat\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"n=500 Qwen mid-phase effective n=274.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Methodology §4 reports null rate (45.2% vs 10.2%) with causal explanation (lag-1 autocorrelation r=0.718 vs 0.894, d=-1.68). Effective n table in Appendix. Explicitly states 'does not affect primary low-high contrast (Δ)'.\"\n    action_items:\n      - round: 1\n        action: \"Investigate root cause; report in §4\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Mid-phase null rate reported with autocorrelation explanation; effective n in Appendix table.\"\n    resolution_round: 5\n\n  - id: \"R5-W1\"\n    summary: \"Table 2 uses n=50 profiling data in main body alongside n=500 tables — potential reader confusion\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1]\n        note: \"Table 2 (main-results) reports per-phase II from n=50 profiling subset. Caption labels provenance and cross-references Table 1 (n=496). However, mixing n=50 and n=500 data in the same Results section risks reader confusion about which results are from which sample.\"\n    action_items:\n      - round: 5\n        action: \"Consider moving Table 2 to Appendix or adding a paragraph explaining the n=50/n=500 data relationship\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Crossover analysis (§5.3 + Appendix A) uses n=50 profiling data — not verified at n=500\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1]\n        note: \"Crossover reversal magnitudes (3.9×-5.4×) and per-phase II values come from bf16_importance/rand exp_ids (n=50 profiling). The crossover may differ at n=500. exp_id comments confirm profiling subset provenance.\"\n    action_items:\n      - round: 5\n        action: \"Verify crossover at n=500 or clearly label as profiling-subset finding with caveat\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-1\"\n    summary: \"'following ThinKV' wording still in background.tex:33 — method is quantile-based, not ThinKV's explicit delimiters\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Continuation of R1-W1. Sensitivity analysis resolved, but the misleading attribution persists.\"\n    action_items:\n      - round: 5\n        action: \"Change 'following ThinKV' to 'inspired by ThinKV' or remove ThinKV from segmentation sentence\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-2\"\n    summary: \"LongFlow bib entry has 'Withdrawn from ICLR 2026' note — citing withdrawn paper\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"Newly added reference per R2-W3 fix. If paper is genuinely withdrawn, citation may signal poor literature curation.\"\n    action_items:\n      - round: 5\n        action: \"Verify LongFlow status; if withdrawn, remove citation or add appropriate caveat\"\n        assigned_to: \"main_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-3\"\n    summary: \"\\\\placeholder command definition residual in main.tex:21\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"Unused but residual. Trivial cleanup.\"\n    action_items:\n      - round: 5\n        action: \"Remove \\\\newcommand{\\\\placeholder} from main.tex\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"40+ placeholders unfilled — paper not submission-ready\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged as #1 critical issue.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All placeholders filled: Table 4 (LLaMA) populated, Abstract complete, Discussion oracle data (18%/32%) filled, Appendix tables complete. Grep confirms zero \\\\placeholder usage.\"\n    action_items:\n      - round: 1\n        action: \"Fill all placeholders with n=500 analysis data\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All 40+ placeholders filled with experimental data from n=500 analysis.\"\n    resolution_round: 5\n\n  - id: \"R1-N4\"\n    summary: \"Cross-architecture (LLaMA) evidence too weak to support title/abstract framing\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree LLaMA evidence is overclaimed.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §5.5 renamed 'Exploratory Cross-Architecture Analysis'; Abstract uses 'preliminary cross-architecture evidence'; Contribution 2 says 'exploratory evidence from LlamaForCausalLM'. Hedging appropriate throughout.\"\n    action_items:\n      - round: 1\n        action: \"Downgrade LLaMA to exploratory; hedge title/abstract/contribution\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"LLaMA downgraded to exploratory with appropriate hedging in title, abstract, and contributions.\"\n    resolution_round: 5\n\n  - id: \"R1-N3\"\n    summary: \"Single benchmark (MATH-500) severely limits generalization — title/abstract say 'reasoning models' but only math reasoning tested\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree single benchmark is major limitation.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Title changed to 'Mathematical Reasoning Models'. Limitations expanded with MATH-500 justification (phase transitions, per-problem evaluation, difficulty variation). Task coverage paragraph lists code/science/multi-hop as future work.\"\n    action_items:\n      - round: 1\n        action: \"Scope title/abstract to mathematical reasoning; expand limitations\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Title scoped to 'Mathematical Reasoning Models'; limitations section provides MATH-500 justification and lists extension domains.\"\n    resolution_round: 5\n\n  - id: \"R1-N2\"\n    summary: \"50-problem sample size lacks power analysis; exclusion criteria unclear\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Reviewer corrects: use CI width shrinkage instead of post-hoc power.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=500 (all MATH-500). Exclusion criteria stated: DS 4, QW 25. CI width shrinkage 2.5-5.9× reported. All p < 10^-69 (DS) and 10^-14 (QW). Power concerns eliminated.\"\n    action_items:\n      - round: 1\n        action: \"Run n=500; report exclusion criteria and CI shrinkage\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Full n=500 dataset used; exclusion criteria, effective n, and CI width shrinkage all reported in Methodology.\"\n    resolution_round: 5\n\n  - id: \"R1-N5\"\n    summary: \"Mechanism analysis (entropy-discrimination collapse) is purely correlational\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Reviewer confirms: can downgrade to warning if §6 properly scoped.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §6 title changed to 'Discrimination Collapse under Compound Sparsity'. Split: §6.1 discrimination collapse (robust, 16/16), §6.2 entropy redistribution (model-dependent). 'correlational' explicitly stated. Causal validation → future work.\"\n    action_items:\n      - round: 1\n        action: \"Split §6; add 'correlational' caveat; causal → future work\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"§6 restructured with honest correlational framing; discrimination collapse separated from model-dependent entropy redistribution.\"\n    resolution_round: 5\n\n  - id: \"R2-N3\"\n    summary: \"Insufficient differentiation from HIES (2025)\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Clear delta exists but paper doesn't articulate it.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §6.1 has explicit HIES comparison: 'independently corroborated by [HIES], who report importance score collapse under heavy single-axis pruning; our results extend this to the compound setting'. Related Work §2 also has dedicated HIES paragraph. Crossover identified as prediction HIES cannot generate.\"\n    action_items:\n      - round: 1\n        action: \"Add explicit HIES comparison in Related Work and §6\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Explicit HIES comparison added in both Related Work and Analysis sections.\"\n    resolution_round: 5\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation lacks justification; 'following ThinKV' wording misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need sensitivity analysis and correct ThinKV reference.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. Sensitivity analysis added: mpl {5,10,20} (Appendix C), quartile/quintile segmentation (Appendix D). min_phase_length justified. BUT 'following ThinKV' wording still in background.tex line 33 — ThinKV uses explicit &lt;think> delimiters, not quantile boundaries.\"\n    action_items:\n      - round: 1\n        action: \"Add sensitivity analysis; correct ThinKV phrasing\"\n        assigned_to: \"paper_agent\"\n        status: in_progress\n      - round: 5\n        action: \"Fix 'following ThinKV' in background.tex:33 — change to 'inspired by' or remove ThinKV from segmentation description\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Symmetric sparsity rate assumption lacks practical representativeness\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree needs discussion.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Dedicated 'Symmetric sparsity assumption' paragraph in Limitations.\"\n    action_items:\n      - round: 1\n        action: \"Add limitations paragraph\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Symmetric sparsity assumption discussed in Limitations with asymmetric extension as future work.\"\n    resolution_round: 5\n\n  - id: \"R1-W3\"\n    summary: \"Severity gradient G numerically unstable when II_high approaches zero\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree. Need bootstrap CI for G.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Δ (paired median diff) is now primary metric. G demoted to auxiliary with bootstrap CIs reported: [26,37] to [119,171]. §4 explicitly states 'G is reported as an auxiliary metric; Δ is primary'.\"\n    action_items:\n      - round: 1\n        action: \"Report G CIs; demote to auxiliary\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"G demoted to auxiliary metric with bootstrap CIs; Δ is primary throughout.\"\n    resolution_round: 5\n\n  - id: \"R1-W4\"\n    summary: \"Bonferroni correction scope (k=4) may be insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Supplement with BH-FDR.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. k=4 per model×strategy family justified in §4. BH-FDR correction across all 44 tests in Appendix B — all 32 Bonferroni-significant results remain significant under BH-FDR; 5 BH-only results are all in random-eviction conditions.\"\n    action_items:\n      - round: 1\n        action: \"Justify k=4; add BH-FDR appendix\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"k=4 family structure justified; BH-FDR appendix confirms no importance-based findings lost.\"\n    resolution_round: 5\n\n  - id: \"R1-W5\"\n    summary: \"Spearman rho=1.0 on 4 points over-interpreted\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need n=4 caveat; use JT test at n=500.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Spearman annotated with n=4 and one-tailed. JT test added (z=6.2-33.7, p<10^-9) using per-problem values (~496 per group). Both tests reported in §4.\"\n    action_items:\n      - round: 1\n        action: \"Annotate Spearman n=4; add JT test\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Spearman properly caveated; JT test provides n=500-level dose-response evidence.\"\n    resolution_round: 5\n\n  - id: \"R1-W6\"\n    summary: \"Exclusion criteria not stated in Methodology\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Merged with R1-N2.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Methodology §4 states: DS 4 excluded (degenerate phase), QW 25 excluded. Qwen mid-phase null rate 45.2% explained with lag-1 autocorrelation.\"\n    action_items:\n      - round: 1\n        action: \"Report exclusion criteria in §4\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Exclusion criteria and effective n fully reported in Methodology.\"\n    resolution_round: 5\n\n  - id: \"R2-W3\"\n    summary: \"Related Work missing RLKV, LongFlow, PM-KVQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2-W3. R1 partially agrees.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All three added: RLKV in KV cache eviction paragraph, LongFlow in same paragraph, PM-KVQ in compound compression paragraph with temporal dimension link.\"\n    action_items:\n      - round: 1\n        action: \"Assess relevance and cite\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"RLKV, LongFlow, PM-KVQ integrated into Related Work with appropriate contextual framing.\"\n    resolution_round: 5\n\n  - id: \"R2-W5\"\n    summary: \"Abstract too long and dense\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both independently flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Rewritten: ~10 lines, structured (problem → finding → replication → mechanism → implication). LLaMA stats moved to Results. Readable.\"\n    action_items:\n      - round: 1\n        action: \"Condense abstract\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Abstract condensed to ~10 lines with clear structure.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-2\"\n    summary: \"LaTeX source contains REVIEWER-ATTACK/REBUTTAL comments\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Should clean before submission.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Deleted from appendix_disc_analysis.tex and other files.\"\n    action_items:\n      - round: 1\n        action: \"Remove all REVIEWER-ATTACK/REBUTTAL comments\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All reviewer-strategy comments removed from LaTeX source.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-1\"\n    summary: \"h2o-neurips2023 bib entry missing title field; citation quality issues\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both flagged.\"\n      - round: 5\n        reviewers: [2]\n        note: \"PARTIALLY RESOLVED. h2o title field added. But LongFlow bib entry contains 'Withdrawn from ICLR 2026' note — citing a withdrawn paper needs careful framing or removal.\"\n    action_items:\n      - round: 1\n        action: \"Fix h2o bib entry\"\n        assigned_to: \"main_agent\"\n        status: done\n      - round: 5\n        action: \"Address LongFlow 'Withdrawn from ICLR 2026' note — either remove citation or add caveat\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-6\"\n    summary: \"s=0.35 supplementary experiment mentioned but not fully reported\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Either report fully or remove.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Removed from Appendix.\"\n    action_items:\n      - round: 1\n        action: \"Remove s=0.35 mention\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"s=0.35 incomplete data removed.\"\n    resolution_round: 5\n\n  - id: \"R1-Minor-code\"\n    summary: \"No code or data release plan\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both noted.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Reproducibility section added in main.tex: 'Code and data will be released upon acceptance.'\"\n    action_items:\n      - round: 1\n        action: \"Add code/data release statement\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Reproducibility statement added.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-1\"\n    summary: \"paper_provenance.yaml C019 outdated\"\n    category: framing\n    severity: warning\n    status: wont_fix\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"Internal process issue, not a paper defect.\"\n      - round: 5\n        reviewers: []\n        note: \"Internal provenance tracking — not visible to venue reviewers. Marking wont_fix for review tracker purposes.\"\n    action_items:\n      - round: 1\n        action: \"Update C019 in paper_provenance.yaml\"\n        assigned_to: \"director\"\n        status: wont_fix\n    resolution: \"Internal process issue, not tracked as paper defect.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-2\"\n    summary: \"Random masking s025+ significant gradient needs explicit paper treatment\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"D063 threshold story needs integration.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §5.1 integrates threshold story: 'Random eviction develops a detectable but weak phase gradient above s≈0.20...15-39× smaller than importance-based'. Cross-model replication (§5.4) mirrors pattern on Qwen. Extended Discussion covers random masking as falsification control.\"\n    action_items:\n      - round: 1\n        action: \"Integrate random threshold story in Results\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Random eviction threshold story fully integrated in Results and Discussion.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-3\"\n    summary: \"Qwen mid-phase 45.2% null rate needs effective n caveat\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"n=500 Qwen mid-phase effective n=274.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Methodology §4 reports null rate (45.2% vs 10.2%) with causal explanation (lag-1 autocorrelation r=0.718 vs 0.894, d=-1.68). Effective n table in Appendix. Explicitly states 'does not affect primary low-high contrast (Δ)'.\"\n    action_items:\n      - round: 1\n        action: \"Investigate root cause; report in §4\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Mid-phase null rate reported with autocorrelation explanation; effective n in Appendix table.\"\n    resolution_round: 5\n\n  - id: \"R5-W1\"\n    summary: \"Table 2 uses n=50 profiling data in main body alongside n=500 tables — potential reader confusion\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1]\n        note: \"Table 2 (main-results) reports per-phase II from n=50 profiling subset. Caption labels provenance and cross-references Table 1 (n=496). However, mixing n=50 and n=500 data in the same Results section risks reader confusion about which results are from which sample.\"\n    action_items:\n      - round: 5\n        action: \"Consider moving Table 2 to Appendix or adding a paragraph explaining the n=50/n=500 data relationship\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Crossover analysis (§5.3 + Appendix A) uses n=50 profiling data — not verified at n=500\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1]\n        note: \"Crossover reversal magnitudes (3.9×-5.4×) and per-phase II values come from bf16_importance/rand exp_ids (n=50 profiling). The crossover may differ at n=500. exp_id comments confirm profiling subset provenance.\"\n    action_items:\n      - round: 5\n        action: \"Verify crossover at n=500 or clearly label as profiling-subset finding with caveat\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-1\"\n    summary: \"'following ThinKV' wording still in background.tex:33 — method is quantile-based, not ThinKV's explicit delimiters\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Continuation of R1-W1. Sensitivity analysis resolved, but the misleading attribution persists.\"\n    action_items:\n      - round: 5\n        action: \"Change 'following ThinKV' to 'inspired by ThinKV' or remove ThinKV from segmentation sentence\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-2\"\n    summary: \"LongFlow bib entry has 'Withdrawn from ICLR 2026' note — citing withdrawn paper\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"Newly added reference per R2-W3 fix. If paper is genuinely withdrawn, citation may signal poor literature curation.\"\n    action_items:\n      - round: 5\n        action: \"Verify LongFlow status; if withdrawn, remove citation or add appropriate caveat\"\n        assigned_to: \"main_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-3\"\n    summary: \"\\\\placeholder command definition residual in main.tex:21\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"Unused but residual. Trivial cleanup.\"\n    action_items:\n      - round: 5\n        action: \"Remove \\\\newcommand{\\\\placeholder} from main.tex\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-15T11:05:05.081903+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml\", \"bytes\": 21179}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 155
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-15T11:06:54.705211+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "report": "# 圆桌审稿报告 — Round 5（继续审稿）\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n**Venue**: EMNLP 2026 ARR (Main Conference)\n**截止日期**: 2026-06-15\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）\n**轮次**: Round 5（修订评估 — 基于 Round 1 审稿意见的修改审查）\n**上轮评分**: 2.5/5 (Weak Reject) → **本轮评分**: 3.5/5 (Borderline Accept)\n\n---\n\n## Summary\n\n论文经过实质性修订：样本量从 n=50 扩展到 n=500（全部 MATH-500），所有 40+ placeholders 已填充，cross-architecture claim 从 \"replicates across three models spanning two architectures\" 降级为 \"exploratory evidence\"，标题限定为 \"Mathematical Reasoning Models\"，机制分析明确标注为 correlational。新增三项 robustness analyses（BH-FDR、min_phase_length sensitivity、segmentation granularity）。统计基础从 borderline adequate 提升到 strong：所有主条件 p < 10^-69 (DS) / 10^-14 (QW)，JT test 补充了 Spearman 的 n=4 局限性。\n\nRound 1 的 5 个 critical issues 全部得到实质性回应。两位 Reviewer 独立将评分从 2.5 上调至 3.5。\n\n---\n\n## Round 1 Issue Resolution Status\n\n### Critical Issues (5/5 Resolved)\n\n| Issue | Round 1 Severity | Round 5 Status | 评估 |\n|-------|-----------------|----------------|------|\n| R1-N1: 40+ placeholders | Critical | **RESOLVED** | 全部填充，grep 确认零残留 |\n| R1-N4: Cross-arch overclaim | Critical | **RESOLVED** | §5.5 \"Exploratory\"，Abstract \"preliminary\"，Contribution \"exploratory evidence\" |\n| R1-N3: Single benchmark | Critical | **RESOLVED** | Title → \"Mathematical Reasoning Models\"；Limitations 有 MATH-500 justification |\n| R1-N2: Sample size / power | Critical | **RESOLVED** | n=500，exclusion criteria (DS 4, QW 25) stated，CI width shrinkage 2.5-5.9× |\n| R1-N5: Mechanism correlational | Critical | **RESOLVED** | §6 split: §6.1 discrimination collapse (robust) + §6.2 entropy (model-dependent)；\"correlational\" explicit |\n\n### Warning Issues (10/11 Resolved or Partially Resolved)\n\n| Issue | Round 5 Status | 评估 |\n|-------|----------------|------|\n| R2-N3: HIES differentiation | **RESOLVED** | §6.1 + Related Work 有 explicit comparison |\n| R1-W1: Phase segmentation | **PARTIAL** | Sensitivity analysis 完备（mpl, quartile, quintile），但 \"following ThinKV\" 措辞仍在 background.tex:33 |\n| R1-W2: Symmetric sparsity | **RESOLVED** | Limitations 有专门段落 |\n| R1-W3: G instability | **RESOLVED** | Δ primary，G auxiliary with bootstrap CIs |\n| R1-W4: Bonferroni scope | **RESOLVED** | k=4 justified，BH-FDR 44-test appendix |\n| R1-W5: Spearman overinterpret | **RESOLVED** | n=4 caveat + one-tailed + JT test (z=6.2-33.7) |\n| R1-W6: Exclusion criteria | **RESOLVED** | §4 complete |\n| R2-W3: Missing refs | **RESOLVED** | RLKV/LongFlow/PM-KVQ all added |\n| R2-W5: Abstract dense | **RESOLVED** | Rewritten, ~10 lines, structured |\n| REV-ADD-2: Random threshold | **RESOLVED** | Integrated in §5.1 + cross-model |\n| REV-ADD-3: Qwen mid-phase | **RESOLVED** | Reported with autocorrelation explanation |\n\n### Info Issues (4/4 Resolved)\n\nR2-Minor-2 (REVIEWER-ATTACK comments), R2-Minor-6 (s=0.35), R1-Minor-code (reproducibility) — all resolved. R2-Minor-1 (bib) partially resolved (h2o fixed, but LongFlow \"Withdrawn\" note introduced).\n\n---\n\n## Strengths（修订后增强）\n\n**S1** [retained, strengthened] **研究问题有价值且定义清晰**。Phase-strategy interaction 的 characterization 对 efficient inference 部署有直接意义。n=500 的统计基础使 claim 可信。\n\n**S2** [retained, strengthened] **统计方法论从 adequate 提升到 exemplary**。新增 BH-FDR (44 tests)、JT dose-response test、mpl sensitivity (3 settings × 16 conditions)、segmentation robustness (tercile/quartile/quintile)。Bootstrap B=10,000, seed=42, Bonferroni k=4 per family — 统计报告质量在 ML 论文中属顶尖。\n\n**S3** [retained] **Random eviction falsification control 设计巧妙**。随机蒸发的阈值故事（s≤0.20 non-significant, s≥0.25 significant but 3-39× weaker）现已完整呈现，强化了 strategy-specificity claim。\n\n**S4** [retained] **Crossover 发现有 deployment insight**。Strategy ranking reversal 对 uniform budget 设计直接有启示。\n\n**S5** [new] **Honest claim scoping**。修订版在 title、abstract、contributions 中系统性地降级了 overclaimed 内容。LLaMA \"exploratory\"、mechanism \"correlational\"、scope \"mathematical reasoning\" — 这是修订中最难做到的部分，作者做到了。\n\n**S6** [new] **Robustness appendix 显著提升可信度**。Table 5 (BH-FDR)、Table 6 (mpl sensitivity, 16 conditions × 3 settings)、Table 7 (segmentation, 4 sparsity × 3 schemes) — 远超多数 EMNLP submission。\n\n**S7** [new] **Qwen mid-phase null rate 分析透彻**。lag-1 autocorrelation explanation (r=0.718 vs 0.894, d=-1.68) 不仅报告问题还解释了 root cause，展示了作者对数据的深度理解。\n\n---\n\n## Weaknesses（修订后残留 + 新发现）\n\n### Should-Fix（影响评分但不阻碍接收）\n\n**SF1** [warning, R1] **n=50 / n=500 数据混合可能误导读者**\n- Table 2（per-phase II breakdown, main body §5.2）使用 n=50 profiling subset 数据\n- Table 1 (§5.1) 和 Table 3 (§5.6) 使用 n=496 / n=475 数据\n- Caption 标注了 \"n=50 profiling subset\" 并引用 Table 1 确认，但同一 Results section 混合两个 sample size 的数据易造成混淆\n- crossover 分析 (§5.3 + Appendix A) 同样使用 n=50 数据（exp_id: bf16_importance_s025, bf16_ds_rand_s025）\n- **建议**：将 Table 2 移至 Appendix 或在 §5.2 添加一段话明确说明 n=50 profiling 与 n=500 confirmation 的关系\n\n**SF2** [warning, R1] **Crossover 未在 n=500 验证**\n- §5.3 的策略排名反转（5.3× reversal at s=0.25）基于 n=50 per-phase II 值\n- 全文 crossover 引用的 II 数值（0.032 vs 0.818, 7.196 vs 1.363）均来自 profiling subset\n- Discussion §7 引用相同 crossover 数值作为 \"quantitative surprise\" 论据\n- 如果 n=500 per-phase II 值不同，crossover magnitude 可能改变\n- **建议**：在 n=500 数据上验证 crossover；或在 §5.3 标注 \"profiling subset\" 并 caveat\n\n**SF3** [warning, R1-W1 residual] **\"following ThinKV\" 措辞仍未修正**\n- background.tex:33: \"following ThinKV [thinkv-iclr2026]\"\n- ThinKV 使用 explicit `&lt;think>` token delimiters 分割 reasoning/non-reasoning 阶段\n- 本文使用 attention sparsity quantile terciles — 方法论完全不同\n- Round 1 已明确提出需修正；Round 5 sensitivity analysis 已添加但措辞未改\n- **建议**：改为 \"inspired by the phase distinction in ThinKV\" 或直接删除 ThinKV 引用\n\n### Minor（不影响接收决定）\n\n**M1** [info, R2] **LongFlow bib \"Withdrawn from ICLR 2026\" 注释**\n- 新增引用 LongFlow 的 bib entry 包含 withdrawn 标注\n- 引用被撤回论文可能被审稿人视为 literature curation 不够严谨\n- **建议**：确认 LongFlow 实际状态；如确实 withdrawn，移除引用或使用 arXiv preprint 形式\n\n**M2** [info, R2] **\\\\placeholder 命令定义残留**\n- main.tex:21 仍有 `\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}`\n- 虽未使用（grep 确认无调用），但提交源码时暗示论文曾有 placeholder 结构\n- **建议**：删除该行\n\n---\n\n## Questions for Authors\n\n1. Table 2 的 n=50 per-phase II 数据在 n=500 上是否有变化？特别是 crossover 的 reversal magnitude（3.9×-5.4×）在 n=500 上是否一致？\n2. \"following ThinKV\" 措辞为何未在本轮修改？是否为 oversight？\n3. LongFlow 是否确实从 ICLR 2026 撤稿？如果是，是否有更合适的替代引用？\n4. Oracle pilot experiment 的 gate failure (18% < 30%) 是否有后续实验计划？\n\n---\n\n## Missing References\n\nRound 1 指出的 RLKV、LongFlow、PM-KVQ 均已补充。本轮未发现新的重要遗漏。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5/5 (Borderline Accept)**\n**置信度: 4/5**\n\n**修订质量评估**: 本轮修订是高质量的实质性回应。5/5 critical issues resolved，10/11 warning issues resolved or partially resolved。n=50→n=500 的扩展消除了 power 疑虑，robustness analyses（BH-FDR、mpl sensitivity、segmentation）远超预期。Claim scoping（title、abstract、contributions）诚实且系统。\n\n**残留问题严重性**: 所有残留问题均为 warning 或 info 级别：\n- SF1-SF2 (n=50/n=500 混合 + crossover 未验证): 最重要的残留问题，但不改变核心 conclusion——n=500 data 已独立确认 monotonic severity gradient\n- SF3 (\"following ThinKV\"): 措辞修正，5 分钟工作量\n- M1-M2: 纯 cosmetic\n\n**接收障碍分析**:\n- **支持接收**: 研究问题有价值；n=500 统计基础强；falsification control 设计优秀；claim scoping 诚实；robustness 超越多数 EMNLP submissions\n- **反对接收**: 仍是 single-benchmark (MATH-500) characterization study；mechanism 为 correlational only；crossover claim 基于 n=50 子集未在 n=500 验证\n- **关键判断**: 对于以 empirical characterization 为核心贡献的论文，当前 evidence quality 达到了 EMNLP main 的门槛，但不具备显著 margin。如果 SF1-SF2 得到解决（crossover 在 n=500 上验证），评分可上调至 4/5。\n\n**建议**:\n- 如果能在投稿前完成 crossover n=500 验证、修正 \"following ThinKV\" 措辞、清理 LongFlow bib 和 \\placeholder 残留：推荐投稿 EMNLP main\n- 如果时间不允许验证 crossover：仍可投稿，但应在 §5.3 添加 \"profiling subset\" caveat，crossover 可能被 reviewer 追问\n\n---\n\n## Detailed Comments\n\n### Per-Section Notes\n\n**Abstract**: 修订后结构清晰，统计数字适量。\"preliminary cross-architecture evidence\" 措辞恰当。唯一微瑕：最后一句 \"motivate phase-aware compression budgets\" 略 overclaim（pilot experiment gate failed at 18%）。\n\n**§1 Introduction**: Contribution scoping 准确。\"3-39× larger\" 比 Round 1 的 \"absent under random\" 更精确，正确反映了 threshold story。Contribution 3 \"propose...as a mechanistic explanation\" 恰当。\n\n**§2 Related Work**: HIES comparison 充分。PM-KVQ temporal dimension link 是好的补充。LongFlow withdrawn status 需确认。整体 coverage 完整。\n\n**§3 Background**: G 的 auxiliary 定位明确。\"following ThinKV\" 需改为 \"inspired by\" 或删除。公式定义清晰。\n\n**§4 Methodology**: n=500 full dataset, exclusion criteria, CI width shrinkage, Bonferroni k=4 family justification, JT test — 统计报告质量优秀。Qwen mid-phase null 的 autocorrelation explanation 是亮点。\n\n**§5 Results**: Table 1 (n=496) 可信且 powerful。Table 2 (n=50) 的 provenance 需更突出标注。§5.3 crossover 需 n=500 验证或 caveat。§5.4 cross-model 完整。§5.5 LLaMA exploratory 措辞恰当。§5.6 statistical validation 强。\n\n**§6 Analysis**: §6.1 discrimination collapse 的 HIES comparison 和 random-eviction counterfactual 构成 reasonable correlational case。§6.2 entropy redistribution 诚实标注 model-dependent。\"correlational; causal validation...important direction for future work\" — 恰当。\n\n**§7 Discussion**: Oracle pilot gate failure (18% < 30%) 诚实报告是加分项。Architecture-dependent magnitude 讨论平衡。Crossover 数值来自 n=50（与 SF2 同一问题）。\n\n**Limitations**: 全面。Symmetric sparsity、mechanism correlational、sparsity range — 覆盖了主要方向。MATH-500 justification 有说服力。\n\n**Appendix**: BH-FDR (44 tests) + mpl sensitivity (48 cells) + segmentation robustness (12 cells) — 三项 robustness 构成强有力的 supplementary evidence。Crossover appendix 和 permutation test 仍使用 n=50 数据（与主文一致但同样是潜在问题）。\n\n**References**: 32 篇引用，新增 RLKV/LongFlow/PM-KVQ。LongFlow withdrawn status 需处理。其余引用无问题。\n\n### Round 1 → Round 5 Score Justification\n\n| 维度 | Round 1 | Round 5 | 变化原因 |\n|------|---------|---------|----------|\n| 数据完整性 | 1/5 (40+ placeholders) | 5/5 | 全部填充 |\n| 统计严谨性 | 3/5 (n=50, no power) | 5/5 | n=500, BH-FDR, JT, mpl, segmentation |\n| Claim scoping | 2/5 (overclaim) | 4/5 | Title/Abstract/Contribution 系统降级 |\n| 机制分析 | 2/5 (causal language) | 4/5 | correlational explicit, split robust/model-dependent |\n| 写作质量 | 3/5 | 4/5 | Abstract 精简, exclusion stated, HIES compared |\n| 整体 | 2.5/5 | 3.5/5 | Substantial improvement |",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline accept",
  "review_chat_id": "oc_57b24a804b56707ec9118a483a8ac65e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "report": "# 圆桌审稿报告 — Round 5（继续审稿）\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n**Venue**: EMNLP 2026 ARR (Main Conference)\n**截止日期**: 2026-06-15\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）\n**轮次**: Round 5（修订评估 — 基于 Round 1 审稿意见的修改审查）\n**上轮评分**: 2.5/5 (Weak Reject) → **本轮评分**: 3.5/5 (Borderline Accept)\n\n---\n\n## Summary\n\n论文经过实质性修订：样本量从 n=50 扩展到 n=500（全部 MATH-500），所有 40+ placeholders 已填充，cross-architecture claim 从 \"replicates across three models spanning two architectures\" 降级为 \"exploratory evidence\"，标题限定为 \"Mathematical Reasoning Models\"，机制分析明确标注为 correlational。新增三项 robustness analyses（BH-FDR、min_phase_length sensitivity、segmentation granularity）。统计基础从 borderline adequate 提升到 strong：所有主条件 p < 10^-69 (DS) / 10^-14 (QW)，JT test 补充了 Spearman 的 n=4 局限性。\n\nRound 1 的 5 个 critical issues 全部得到实质性回应。两位 Reviewer 独立将评分从 2.5 上调至 3.5。\n\n---\n\n## Round 1 Issue Resolution Status\n\n### Critical Issues (5/5 Resolved)\n\n| Issue | Round 1 Severity | Round 5 Status | 评估 |\n|-------|-----------------|----------------|------|\n| R1-N1: 40+ placeholders | Critical | **RESOLVED** | 全部填充，grep 确认零残留 |\n| R1-N4: Cross-arch overclaim | Critical | **RESOLVED** | §5.5 \"Exploratory\"，Abstract \"preliminary\"，Contribution \"exploratory evidence\" |\n| R1-N3: Single benchmark | Critical | **RESOLVED** | Title → \"Mathematical Reasoning Models\"；Limitations 有 MATH-500 justification |\n| R1-N2: Sample size / power | Critical | **RESOLVED** | n=500，exclusion criteria (DS 4, QW 25) stated，CI width shrinkage 2.5-5.9× |\n| R1-N5: Mechanism correlational | Critical | **RESOLVED** | §6 split: §6.1 discrimination collapse (robust) + §6.2 entropy (model-dependent)；\"correlational\" explicit |\n\n### Warning Issues (10/11 Resolved or Partially Resolved)\n\n| Issue | Round 5 Status | 评估 |\n|-------|----------------|------|\n| R2-N3: HIES differentiation | **RESOLVED** | §6.1 + Related Work 有 explicit comparison |\n| R1-W1: Phase segmentation | **PARTIAL** | Sensitivity analysis 完备（mpl, quartile, quintile），但 \"following ThinKV\" 措辞仍在 background.tex:33 |\n| R1-W2: Symmetric sparsity | **RESOLVED** | Limitations 有专门段落 |\n| R1-W3: G instability | **RESOLVED** | Δ primary，G auxiliary with bootstrap CIs |\n| R1-W4: Bonferroni scope | **RESOLVED** | k=4 justified，BH-FDR 44-test appendix |\n| R1-W5: Spearman overinterpret | **RESOLVED** | n=4 caveat + one-tailed + JT test (z=6.2-33.7) |\n| R1-W6: Exclusion criteria | **RESOLVED** | §4 complete |\n| R2-W3: Missing refs | **RESOLVED** | RLKV/LongFlow/PM-KVQ all added |\n| R2-W5: Abstract dense | **RESOLVED** | Rewritten, ~10 lines, structured |\n| REV-ADD-2: Random threshold | **RESOLVED** | Integrated in §5.1 + cross-model |\n| REV-ADD-3: Qwen mid-phase | **RESOLVED** | Reported with autocorrelation explanation |\n\n### Info Issues (4/4 Resolved)\n\nR2-Minor-2 (REVIEWER-ATTACK comments), R2-Minor-6 (s=0.35), R1-Minor-code (reproducibility) — all resolved. R2-Minor-1 (bib) partially resolved (h2o fixed, but LongFlow \"Withdrawn\" note introduced).\n\n---\n\n## Strengths（修订后增强）\n\n**S1** [retained, strengthened] **研究问题有价值且定义清晰**。Phase-strategy interaction 的 characterization 对 efficient inference 部署有直接意义。n=500 的统计基础使 claim 可信。\n\n**S2** [retained, strengthened] **统计方法论从 adequate 提升到 exemplary**。新增 BH-FDR (44 tests)、JT dose-response test、mpl sensitivity (3 settings × 16 conditions)、segmentation robustness (tercile/quartile/quintile)。Bootstrap B=10,000, seed=42, Bonferroni k=4 per family — 统计报告质量在 ML 论文中属顶尖。\n\n**S3** [retained] **Random eviction falsification control 设计巧妙**。随机蒸发的阈值故事（s≤0.20 non-significant, s≥0.25 significant but 3-39× weaker）现已完整呈现，强化了 strategy-specificity claim。\n\n**S4** [retained] **Crossover 发现有 deployment insight**。Strategy ranking reversal 对 uniform budget 设计直接有启示。\n\n**S5** [new] **Honest claim scoping**。修订版在 title、abstract、contributions 中系统性地降级了 overclaimed 内容。LLaMA \"exploratory\"、mechanism \"correlational\"、scope \"mathematical reasoning\" — 这是修订中最难做到的部分，作者做到了。\n\n**S6** [new] **Robustness appendix 显著提升可信度**。Table 5 (BH-FDR)、Table 6 (mpl sensitivity, 16 conditions × 3 settings)、Table 7 (segmentation, 4 sparsity × 3 schemes) — 远超多数 EMNLP submission。\n\n**S7** [new] **Qwen mid-phase null rate 分析透彻**。lag-1 autocorrelation explanation (r=0.718 vs 0.894, d=-1.68) 不仅报告问题还解释了 root cause，展示了作者对数据的深度理解。\n\n---\n\n## Weaknesses（修订后残留 + 新发现）\n\n### Should-Fix（影响评分但不阻碍接收）\n\n**SF1** [warning, R1] **n=50 / n=500 数据混合可能误导读者**\n- Table 2（per-phase II breakdown, main body §5.2）使用 n=50 profiling subset 数据\n- Table 1 (§5.1) 和 Table 3 (§5.6) 使用 n=496 / n=475 数据\n- Caption 标注了 \"n=50 profiling subset\" 并引用 Table 1 确认，但同一 Results section 混合两个 sample size 的数据易造成混淆\n- crossover 分析 (§5.3 + Appendix A) 同样使用 n=50 数据（exp_id: bf16_importance_s025, bf16_ds_rand_s025）\n- **建议**：将 Table 2 移至 Appendix 或在 §5.2 添加一段话明确说明 n=50 profiling 与 n=500 confirmation 的关系\n\n**SF2** [warning, R1] **Crossover 未在 n=500 验证**\n- §5.3 的策略排名反转（5.3× reversal at s=0.25）基于 n=50 per-phase II 值\n- 全文 crossover 引用的 II 数值（0.032 vs 0.818, 7.196 vs 1.363）均来自 profiling subset\n- Discussion §7 引用相同 crossover 数值作为 \"quantitative surprise\" 论据\n- 如果 n=500 per-phase II 值不同，crossover magnitude 可能改变\n- **建议**：在 n=500 数据上验证 crossover；或在 §5.3 标注 \"profiling subset\" 并 caveat\n\n**SF3** [warning, R1-W1 residual] **\"following ThinKV\" 措辞仍未修正**\n- background.tex:33: \"following ThinKV [thinkv-iclr2026]\"\n- ThinKV 使用 explicit `&lt;think>` token delimiters 分割 reasoning/non-reasoning 阶段\n- 本文使用 attention sparsity quantile terciles — 方法论完全不同\n- Round 1 已明确提出需修正；Round 5 sensitivity analysis 已添加但措辞未改\n- **建议**：改为 \"inspired by the phase distinction in ThinKV\" 或直接删除 ThinKV 引用\n\n### Minor（不影响接收决定）\n\n**M1** [info, R2] **LongFlow bib \"Withdrawn from ICLR 2026\" 注释**\n- 新增引用 LongFlow 的 bib entry 包含 withdrawn 标注\n- 引用被撤回论文可能被审稿人视为 literature curation 不够严谨\n- **建议**：确认 LongFlow 实际状态；如确实 withdrawn，移除引用或使用 arXiv preprint 形式\n\n**M2** [info, R2] **\\\\placeholder 命令定义残留**\n- main.tex:21 仍有 `\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}`\n- 虽未使用（grep 确认无调用），但提交源码时暗示论文曾有 placeholder 结构\n- **建议**：删除该行\n\n---\n\n## Questions for Authors\n\n1. Table 2 的 n=50 per-phase II 数据在 n=500 上是否有变化？特别是 crossover 的 reversal magnitude（3.9×-5.4×）在 n=500 上是否一致？\n2. \"following ThinKV\" 措辞为何未在本轮修改？是否为 oversight？\n3. LongFlow 是否确实从 ICLR 2026 撤稿？如果是，是否有更合适的替代引用？\n4. Oracle pilot experiment 的 gate failure (18% < 30%) 是否有后续实验计划？\n\n---\n\n## Missing References\n\nRound 1 指出的 RLKV、LongFlow、PM-KVQ 均已补充。本轮未发现新的重要遗漏。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5/5 (Borderline Accept)**\n**置信度: 4/5**\n\n**修订质量评估**: 本轮修订是高质量的实质性回应。5/5 critical issues resolved，10/11 warning issues resolved or partially resolved。n=50→n=500 的扩展消除了 power 疑虑，robustness analyses（BH-FDR、mpl sensitivity、segmentation）远超预期。Claim scoping（title、abstract、contributions）诚实且系统。\n\n**残留问题严重性**: 所有残留问题均为 warning 或 info 级别：\n- SF1-SF2 (n=50/n=500 混合 + crossover 未验证): 最重要的残留问题，但不改变核心 conclusion——n=500 data 已独立确认 monotonic severity gradient\n- SF3 (\"following ThinKV\"): 措辞修正，5 分钟工作量\n- M1-M2: 纯 cosmetic\n\n**接收障碍分析**:\n- **支持接收**: 研究问题有价值；n=500 统计基础强；falsification control 设计优秀；claim scoping 诚实；robustness 超越多数 EMNLP submissions\n- **反对接收**: 仍是 single-benchmark (MATH-500) characterization study；mechanism 为 correlational only；crossover claim 基于 n=50 子集未在 n=500 验证\n- **关键判断**: 对于以 empirical characterization 为核心贡献的论文，当前 evidence quality 达到了 EMNLP main 的门槛，但不具备显著 margin。如果 SF1-SF2 得到解决（crossover 在 n=500 上验证），评分可上调至 4/5。\n\n**建议**:\n- 如果能在投稿前完成 crossover n=500 验证、修正 \"following ThinKV\" 措辞、清理 LongFlow bib 和 \\placeholder 残留：推荐投稿 EMNLP main\n- 如果时间不允许验证 crossover：仍可投稿，但应在 §5.3 添加 \"profiling subset\" caveat，crossover 可能被 reviewer 追问\n\n---\n\n## Detailed Comments\n\n### Per-Section Notes\n\n**Abstract**: 修订后结构清晰，统计数字适量。\"preliminary cross-architecture evidence\" 措辞恰当。唯一微瑕：最后一句 \"motivate phase-aware compression budgets\" 略 overclaim（pilot experiment gate failed at 18%）。\n\n**§1 Introduction**: Contribution scoping 准确。\"3-39× larger\" 比 Round 1 的 \"absent under random\" 更精确，正确反映了 threshold story。Contribution 3 \"propose...as a mechanistic explanation\" 恰当。\n\n**§2 Related Work**: HIES comparison 充分。PM-KVQ temporal dimension link 是好的补充。LongFlow withdrawn status 需确认。整体 coverage 完整。\n\n**§3 Background**: G 的 auxiliary 定位明确。\"following ThinKV\" 需改为 \"inspired by\" 或删除。公式定义清晰。\n\n**§4 Methodology**: n=500 full dataset, exclusion criteria, CI width shrinkage, Bonferroni k=4 family justification, JT test — 统计报告质量优秀。Qwen mid-phase null 的 autocorrelation explanation 是亮点。\n\n**§5 Results**: Table 1 (n=496) 可信且 powerful。Table 2 (n=50) 的 provenance 需更突出标注。§5.3 crossover 需 n=500 验证或 caveat。§5.4 cross-model 完整。§5.5 LLaMA exploratory 措辞恰当。§5.6 statistical validation 强。\n\n**§6 Analysis**: §6.1 discrimination collapse 的 HIES comparison 和 random-eviction counterfactual 构成 reasonable correlational case。§6.2 entropy redistribution 诚实标注 model-dependent。\"correlational; causal validation...important direction for future work\" — 恰当。\n\n**§7 Discussion**: Oracle pilot gate failure (18% < 30%) 诚实报告是加分项。Architecture-dependent magnitude 讨论平衡。Crossover 数值来自 n=50（与 SF2 同一问题）。\n\n**Limitations**: 全面。Symmetric sparsity、mechanism correlational、sparsity range — 覆盖了主要方向。MATH-500 justification 有说服力。\n\n**Appendix**: BH-FDR (44 tests) + mpl sensitivity (48 cells) + segmentation robustness (12 cells) — 三项 robustness 构成强有力的 supplementary evidence。Crossover appendix 和 permutation test 仍使用 n=50 数据（与主文一致但同样是潜在问题）。\n\n**References**: 32 篇引用，新增 RLKV/LongFlow/PM-KVQ。LongFlow withdrawn status 需处理。其余引用无问题。\n\n### Round 1 → Round 5 Score Justification\n\n| 维度 | Round 1 | Round 5 | 变化原因 |\n|------|---------|---------|----------|\n| 数据完整性 | 1/5 (40+ placeholders) | 5/5 | 全部填充 |\n| 统计严谨性 | 3/5 (n=50, no power) | 5/5 | n=500, BH-FDR, JT, mpl, segmentation |\n| Claim scoping | 2/5 (overclaim) | 4/5 | Title/Abstract/Contribution 系统降级 |\n| 机制分析 | 2/5 (causal language) | 4/5 | correlational explicit, split robust/model-dependent |\n| 写作质量 | 3/5 | 4/5 | Abstract 精简, exclusion stated, HIES compared |\n| 整体 | 2.5/5 | 3.5/5 | Substantial improvement |",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline accept",
    "review_chat_id": "oc_57b24a804b56707ec9118a483a8ac65e"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-15T11:06:56.464065+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_fdc656be1c7fe17c11ab639cdbce3710:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 1758
}
```

</details>

---


### Assistant

_source line 354 · 2026-05-15T11:07:04.177075+00:00_

Round 5 审稿报告已提交，issue tracker 已同步更新。

**本轮结论**：3.5/5（Borderline Accept），从 Round 1 的 2.5/5（Weak Reject）上调一档。

**核心变化**：
- 5/5 critical issues 全部 resolved（placeholders、overclaim、sample size、benchmark scope、mechanism framing）
- 10/11 warning issues resolved
- 新增 3 项 robustness analyses（BH-FDR、mpl sensitivity、segmentation）

**残留问题**（均为 warning/info）：
- SF1-SF2：n=50 per-phase 数据（Table 2、crossover）混在 n=500 主结果中，crossover 未在 n=500 验证 — 最重要的残留项
- SF3：background.tex:33 "following ThinKV" 措辞未修正
- M1-M2：LongFlow withdrawn bib、\placeholder 残留

如果 crossover 在 n=500 上验证通过，评分可上调至 4/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 24

## Round 24

4 recorded events


### User

_source line 355 · 2026-05-15T11:07:05.358958+00:00_

[Reviewer 2 审稿结果]:
Round 5 修订评估已提交给 Review Director。

总结：**所有 Round 1 的 critical/warning issues 均已 resolved**。论文从 n=50 升级到 n=500，填充了全部 placeholder，title 缩窄为 "Mathematical Reasoning Models"，HIES 区分清晰，新引用补全，abstract 精简，REVIEWER-ATTACK 注释删除，mechanism 明确标注为 correlational。评分建议从 2.5 → 3.5（Findings / borderline Conference）。仅余 4 个 minor/trivial 问题（"following ThinKV" 措辞、Table 2 vs 正文 G 值落差、LongFlow withdrawn note、placeholder 命令残留）。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Round 5 评估的交叉回应

---

### (1) R2 Issue 判定——逐条回应

**[AGREE] R2 所有 RESOLVED 判定**：R1-N1, R2-N3, R2-W3, R2-W5, R2-Minor-1/2/6, R1-Minor-code——全部同意。无需逐条展开。

**[AGREE] "following ThinKV" STILL OPEN (minor)**：与我的 R1-W1 PARTIALLY RESOLVED 一致。R2 建议的改写 "analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters" 准确且简洁，我支持这个具体措辞。

**[AGREE] R2-NEW-1: Table 2 vs n=496 落差未解释**：与我的 NEW-W1 高度重叠。R2 建议 Table 2 caption 加一句解释——这是最小侵入式修复，我同意。我的 NEW-W1 额外建议了将 Table 2 移至 Appendix 的选项，但考虑到 Table 2 提供了唯一的 per-phase breakdown（II_high, II_mid, II_low 分别列出），main body 保留它有信息价值。**共识方案**：在 Table 2 caption 末尾加一句，如 "At $n{=}496$, median $\Delta$ values are systematically lower at $s \geq 0.20$ (Table~1) due to reduced outlier influence; the monotonic pattern and strategy contrast are preserved."

**[AGREE] R2-NEW-3: \placeholder 定义残留**：Trivial，同意应删除。

---

### (2) R2-NEW-2: LongFlow bib "Withdrawn from ICLR 2026"

我需要先确认这个事实。Related Work (related_work.tex:19) 引用了 LongFlow：

> "LongFlow~\cite{longflow-2026} targets the long-output setting of reasoning models with an efficient importance metric derived from attention intermediates."

如果 bib entry 确实含有 "Withdrawn" 标注，R2 的顾虑合理——ACL ARR reviewer 可能质疑引用被撤稿工作的做法。

我的判断：**部分同意 R2，但处理方式需要更细致**。

- 引用 withdrawn 论文本身并非不当——arXiv 上的工作无论是否被某个 venue 接收，只要内容是 public 且技术上相关，引用是合规的。ACL ARR 没有禁止引用 withdrawn papers 的规定。
- 但 bib entry 中保留 "Withdrawn from ICLR 2026" 的 note 确实会引起不必要的注意。
- **建议**：(a) 删除 bib 中的 "Withdrawn" note；(b) 将 venue 改为 "arXiv preprint arXiv:XXXX.XXXXX"（如果论文确实仍在 arXiv 上）。这样引用仍然有效，但不会引起 reviewer 的额外质疑。

---

### (3) 我的 NEW-W2 (crossover 未在 n=500 验证)——维持

R2 未提及此问题。我**维持 NEW-W2 为 warning**，理由如下：

§5.3 (results.tex:66) 的 crossover claim 使用的具体数值（importance high-phase II=0.032 vs random 0.818; importance low-phase II=7.196 vs random 1.363; "5.3× reversal"）全部来自 n=50 profiling Table 2。

核心疑虑：
1. **量级不一致风险**：n=50→n=500 后，Δ_s025 从 7.16 降至 3.99（−44%）。如果 per-phase II 值也有类似缩减，crossover 的 magnitude（5.3×）可能不再成立——甚至 crossover 本身是否在 n=500 下仍然存在？
2. **方法论一致性**：论文的其他核心 claims（Δ monotonicity, strategy contrast, dose-response）都在 n=500 上验证。Crossover 是 Contribution 之一（Introduction 未单独列 contribution 但在 Conclusion line 4 中突出），却是唯一一个仅有 n=50 数据支撑的 claim。
3. **修复成本低**：既然已有 n=500 的 per-condition II 数据（否则无法计算 Table 1 的 Δ），只需提取 per-phase medians 即可验证 crossover。这不需要新实验。

**如果 crossover 在 n=500 上稳定**，加一句确认即可。**如果 crossover magnitude 显著变化**，§5.3 的数值和叙述需要更新。无论哪种情况，验证的成本远低于不验证的风险。

严格程度：warning 而非 critical——即使不更新，crossover 的定性方向（importance 在 low-sparsity phase 更差、high-sparsity phase 更好）很可能在 n=500 下仍然成立，但具体数值和 "5.3×" 的精度存疑。

---

### 总结

与 R2 的共识点：
- 所有 RESOLVED 判定一致
- "following ThinKV" 仍需修改（minor）
- Table 2 caption 需补充 n=50 vs n=500 落差说明
- \placeholder 定义应删除
- Overall 3.5/5，两位 reviewer 一致

与 R2 的分歧：
- NEW-W2 (crossover n=500 验证)：R2 未提及，我维持 warning。这是我认为当前论文中最大的残留方法论缺陷——不是因为 crossover 可能不存在，而是因为它是唯一未在 n=500 数据上确认的 main-body claim。
- LongFlow withdrawn 处理：R2 建议删除引用，我建议保留引用但修改 bib entry（删 note、改 venue 为 arXiv）。

**Reviewer 1 最终推荐**：Borderline Conference (3.5/5)。如果 crossover 在 n=500 上验证 + Table 2 caption 修复 + "following ThinKV" 修改，可稳步达到 Conference (4.0) 水平。

---

[Reviewer 1 审稿结果]:
报告已提交。与 R2 在大方向上一致（3.5/5，所有原 critical issues resolved），主要分歧在于我维持 NEW-W2（crossover 未在 n=500 上验证）作为 warning——这是当前 main body 中唯一仅有 n=50 数据支撑的 claim，修复成本低但不验证的风险高。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 5 修订评估

---

### (1) R1 Issue 判定一致性

R1-N1 ~ R1-N5 全部 RESOLVED、R1-W2 ~ R1-W6 及 REV-ADD 系列 RESOLVED——与我的判定完全一致，无分歧。

**[AGREE] R1-W1 (phase segmentation) PARTIALLY RESOLVED**

与我的 "STILL OPEN - minor" 判定一致。我补充一个 R1 的精确观察：quartile/quintile robustness analysis（Appendix §I, Table 12）仅在 n=50 上做了 spot check，而非 n=500。既然 n=50 → n=500 的主指标 $\Delta$ 变化达 40%（Table 2 vs Table 1），segmentation robustness 也应在 full sample 上验证。不过这属于 completeness 问题而非 soundness 问题——tercile 的 n=500 结果已经很扎实，quartile/quintile 作为辅助验证在 n=50 上方向一致已足够支撑结论。

---

### (2) NEW-W1: n=50 与 n=500 数据混合——severity 判定

**我将 severity 从 minor 上调至 warning，同意 R1。** 理由：

重新审视后，Table 2 位于 **main body** 的 §5.2（Phase-Modulated Amplification），是读者首次接触 per-phase 数据的位置。该表的 headline 数字 $G{=}69$–$274\times$ 在视觉上极具冲击力，而正文报告的 n=496 数字 $G{=}30$–$148\times$ 只出现在同段的文字中（results.tex line 29）。对不仔细的读者——包括只扫表格的 reviewer——Table 2 会成为对论文 effect size 的第一印象，且高估 42%–85%。

虽然 Table 2 caption 标注了 "from the $n{=}50$ profiling subset" 和 forward reference，但我认为这不够：

1. **读者习惯问题**：main body 的 table 通常被视为 primary evidence，appendix 的 table 才是 supplementary。将 n=50 profiling table 放在 main body 而将 n=500 primary evidence 仅放在 inline text 中，颠倒了 primary/supplementary 的层级。
2. **具体数字扩散**：Abstract 和 Conclusion 已更新为 n=500 数字，但 §5.2 的 Figure 1 caption 仍然引用 profiling subset（"profiling subset, $n{=}50$"），且 Discussion §7 line 5 用了 "$G{=}30$–$148\times$"。正文在不同位置交替引用两套数字。

**建议（与 R1 一致）**：在 main body 补充 n=500 的 per-phase table（即使作为 condensed 版本只报 $\widetilde{\mathrm{II}}_{\textit{low}}$、$\widetilde{\mathrm{II}}_{\textit{high}}$、$\Delta$、$G$），将当前 Table 2 移至 Appendix 或明确标注为 "Initial Profiling (Superseded)"。

---

### (3) NEW-W2: Crossover 未在 n=500 上验证

**[AGREE] 这是一个需要关注的问题，定级 warning。**

§5.3 (results.tex line 66) 的所有具体数值均来自 n=50 profiling subset：

> "importance-based eviction yields lower II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but higher II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal)"

这些数字直接来自 Table 2（n=50）。而 Table 1（n=500）显示 $\Delta$ 在 s=0.25 从 7.16 变为 3.99、s=0.30 从 14.59 变为 8.48——变化幅度 40%–44%。per-phase 数字的变化可能更大。

关键问题：**crossover 是论文三大 contributions 之一**（Introduction line 22 的 contribution 1 提到 "3–39× larger than under random"），也是区分于 HIES 的核心 novelty argument（Related Work line 18: "The crossover effect is a prediction that single-axis frameworks cannot generate"）。如果这一关键 claim 仅基于 n=50 数据而未在 n=500 上验证，且其他指标在 n=50→n=500 时变化显著，这构成了 **evidence strength 与 claim strength 不匹配**。

Crossover 的 **方向**（importance 在 low-sparsity phase 更差、在 high-sparsity phase 更好）几乎肯定在 n=500 下仍然成立——Table 1 中 importance $\Delta{=}3.99$ vs random $\Delta{=}0.26$ at s=0.25 表明低/高 phase 的差异结构不会消失。但具体的 reversal magnitude（5.3×）可能不同，且 Appendix C 引用的 "3.9×–5.4× across all sparsity levels" 也全部基于 n=50。

**建议**：在 n=500 上计算 per-phase per-strategy median II，更新 §5.3 和 Appendix C 的 crossover 数值。至少应加一句确认 crossover 方向在 n=500 下保持。

---

### 额外同意点

**[AGREE]** R1 观察到 LLaMA 仍为 n=49 vs DS/QW 的 n=500 对比更显 underpowered。我在 Round 1 交叉回应中已经同意 LLaMA 证据弱，但 "Exploratory" 标注是诚实的处理。如果 full MATH-500 的 LLaMA 实验可行，应该补做——但这不是 blocking issue，因为 LLaMA 已被降级为 exploratory。

**[AGREE]** R1 评分 3.5/5 与我的评分一致。两位 reviewer 从 Round 1 的 2.5/5 共同上调至 3.5/5，收敛清晰。

---

### 分歧总结

| Issue | R1 | R2 | 最终建议 |
|-------|----|----|---------|
| NEW-W1 (n=50/n=500 混合) | warning | ~~minor~~ → **warning** (上调) | warning — 需要在 main body 补充 n=500 per-phase table |
| NEW-W2 (crossover 未在 n=500 验证) | warning | **warning** (同意) | warning — crossover 数值应在 n=500 上更新 |
| "following ThinKV" 措辞 | partially resolved | still open (minor) | 一致：minor，改措辞即可 |
| Seg robustness quartile/quintile 仅 n=50 | R1 观察 | 同意但不 blocking | minor — nice-to-have |

**无严重分歧。** 两位 reviewer 在所有 issue 判定上高度一致，severity 分级仅在 NEW-W1 上有 minor→warning 的差异（我已上调）。论文整体评价收敛于 3.5/5 (Findings / borderline Conference)。

---

[Reviewer 2 审稿结果]:
已提交交叉回应。与 R1 在所有 issue 判定上达成一致，将 NEW-W1 (n=50/n=500 混合) 从 minor 上调至 warning。两位 reviewer 评分收敛于 3.5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---
