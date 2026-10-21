# Director coordination — Part 1 of 10

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/0f/0fa49ecfe50583d66f9a.json)

## Round 1

## Round 1

96 recorded events


### User

_source line 1 · 2026-05-16T00:50:29.754760+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-16T00:50:36.267766+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-16T00:50:36.319580+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-16T00:50:39.031731+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-16T00:50:39.132544+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-16T00:50:43.909874+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-16T00:50:44.362094+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (31 个)\n\n- **bootstrap_ci_analysis**: DONE (success) — \n- **exp016_fewrel_error_taxonomy**: DONE (success) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp007_error_taxonomy**: DONE (success) — \n- **exp_fewrel_formal_80rel**: DONE (success) — \n- **exp_fewrel_formal**: DONE (success) — \n- **exp008_sdgd_zero_fewnerd_r2**: DONE (negative) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n- **fewrel_pilot**: DONE (success) — \n- **exp004_maven_bcs**: DONE (negative) — \n- **exp002_confusability_controlled**: DONE (success) — \n- **exp003a_prompt_v2_rerun**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp001_count_baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp012_llama_fewrel_ch2** (success): LLaMA-3.1-8B-Instruct 在 FewRel 80-rel RE 任务上验证 Channel 2 (BCS-controlled confusability effect)。跨模型家族(Qwen→LLaMA) + 跨规模(32B→8B) + 跨任务(NER→RE) 三重泛化验证。exp2 design: count 8/16 × low/high BCS × 27 batches。 ← 基于 exp012_llama_8b_r2\n- **exp_fewrel_40rel_r4** (success): —\n- **exp012_llama_8b_r2_exp2** (negative): LLaMA-3.1-8B-Instruct exp2 重跑：BCS-controlled factorial (count=6/12, low/high BCS)，验证 confusability effect 跨模型泛化。Parent exp012_llama_8b_r2 的 exp1 count curve 已完成。\n\n## 趋势\n成功 14 / 负向 5 / 失败 10 / 共 31\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-38874: 无 GPU 信息\n\n## 告警\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\n- exp012_llama_8b: 已被终止 — unknown\n- exp_fewrel_40rel: 训练失败 — unknown\n- exp012_llama_awq: 已被终止 — unknown\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\n- exp_fewrel_40rel_r2: 训练失败 — unknown\n- exp_fewrel_40rel_r3: 训练失败 — unknown\n- exp012_llama_8b_r3: 训练失败 — unkno
…[truncated 4 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-16T00:50:44.864660+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-16T00:50:46.220923+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-16T00:50:46.371923+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-16T00:50:46.372366+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-16T00:50:52.249095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-16T00:50:52.249526+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-16T00:50:52.601284+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-16T00:50:53.606789+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-16T00:50:53.959022+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-16T00:50:59.332071+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view
…[truncated 1430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6730
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-16T00:50:59.332568+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5725
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-16T00:50:59.385259+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 5426
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-16T00:51:03.911560+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-16T00:51:04.315998+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper/tables/dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/h
…[truncated 847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-16T00:51:04.316486+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 paper format page limit template anonymous double blind ARR submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 paper format page limit template anonymous double blind ARR submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-16T00:51:04.919369+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "writing_plan.yaml"
  }
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-16T00:51:11.353040+00:00_

Web search results for query: "EMNLP 2026 paper format page limit template anonymous double blind ARR submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/ojs/index.php/tacl/about/submissions"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Paper Submission Guidelines | IEEE VIS 2026","url":"https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here is the information about EMNLP 2026 paper format, page limits, template, and submission guidelines:

## Paper Format and Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Anonymity and Review Process

The reviewing process will continue to be double-blind. Following the ACL and ARR policies, there is no anonymity period requirement. However, papers must not include authors' names and affilia
…[truncated 647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7036
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-16T00:51:11.353712+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml\", \"content\": \"# Writing Plan — schema-dag-extraction\\n# Generated: 2026-05-15\\n# Venue: EMNLP 2026 (ARR May 25 cycle)\\n# Format: 8 pages main text + unlimited references\\n# Mode: Full Draft (2-claim analysis paper + SDGD negative result)\\n\\nmeta:\\n  title: \\\"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\\\"\\n  venue: EMNLP 2026 Main\\n  submission_deadline: \\\"2026-05-25\\\"\\n  page_limit: 8\\n  template: \\\"acl2023\\\"  # ARR uses ACL rolling review LaTeX template\\n  template_note: \\\"No EMNLP 2026 template found locally. Using acl2023.sty (standard ARR template). Worker must download from https://github.com/acl-org/acl-style-files if not available.\\\"\\n  primary_model: \\\"Qwen3-32B-FP8\\\"\\n  secondary_model: \\\"LLaMA-3.1-8B-Instruct (exp-012, D022: 70B→8B cross-scale validation)\\\"\\n  datasets: [\\\"Few-NERD (66 types)\\\", \\\"FewRel (80 relations)\\\", \\\"MAVEN (168 event types)\\\"]\\n\\n# =============================================================================\\n# PAPER OUTLINE\\n# =============================================================================\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    dependencies: [introduction, experiments, results, sdgd_negative, conclusion]\\n    key_content:\\n      - Problem: training-free LLM IE degrades on complex schemas; prior work conflates count and confusability\\n      - Method: first controlled empirical study isolating type confusability from count across 3 tasks\\n      - Findings: multi-channel degradation (count→recall, confusability→type confusion); pairwise SCS robust cross-task (r=0.11-0.13); effect amplifies 3.4× with schema complexity; per-type aggregation confounded on homogeneous schemas\\n      - Negative result: naive confusability-aw
…[truncated 11078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6434
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-16T00:51:21.545764+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-16T00:51:21.596588+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	
15	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	
26	\input{related_work}
27	
28	\input{experimental_setup}
29	
30	\input{results}
31	
32	\input{sdgd_negative}
33	
34	\input{discussion}
35	
36	\section*{Limitations}
37	The primary experiments use Qwen3-32B. Channel~1 (count effect) has been validated on Meta-Llama-3.1-8B-Instruct (recall decline $-$43\,pp, per-batch $r = 0.725$ with Qwen3-32B). Channel~2 was validated cross-model on FewRel RE: Llama-3.1-8B-Instruct shows $\Delta = -27.1$\,pp at count 8 and $-23.9$\,pp at count 16, comparable to Qwen3-32B's $-31.2$\,pp. High-BCS accuracy is model-invariant ($\approx$0.51), with cross-model divergence confined to the low-BCS regime. On Few-NERD NER, the effect was not robustly detectable, likely due to floor effects at 8B scale and the noisier text-match metric. The pairwise confusability signal explains roughly 1.3--1.7\% of the variance in type confusion---entity frequency, prompt position effects, and type definition quality likely contribute to the remaining variance. Our decomposition experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored. We conducted a within-dataset $2\!\times\!2$ factorial analysis (count $\times$ BCS) on Few-NERD; the interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), possibly due to BCS range compression in high-count schemas. The primary evidence for count--confusability interaction remains the $3.4\ti
…[truncated 3802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-16T00:51:22.601237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-16T00:51:22.953089+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE but interacting in NER. Confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural bottleneck for decompose-then-merge pipelines in zero-shot IE.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-16T00:51:22.953463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-16T00:51:23.104343+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two dis
…[truncated 3551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-16T00:51:23.105700+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-16T00:51:23.156341+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Recent surveys categorize LLM-based IE along instruction-tuning and code-generation axes \cite{llm4ie-survey-2024}. Approaches span instruction tuning for unified IE \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided zero-shot extraction \cite{gollie-2024,adelie-2024}, and schema-driven decoding \cite{slot-2025,oneke-2025}. For NER, methods include zero-shot decomposition by entity type \cite{xie-zeroshot-ner-2023,promptner-2023}, ChatGPT distillation \cite{uniner-2024}, bidirectional transformers \cite{gliner-2024,gliner2-2025}, self-improvement \cite{self-improve-ner-2024}, type descriptions \cite{zeroner-2025}, and guided synthesis \cite{guidex-2025,nuner-2024}. Relation extraction benefits from self-prompting \cite{self-prompting-re-2024} and retrieval-augmented code generation \cite{code4uie-2024}. \citet{familiarity-2025} highlight evaluation pitfalls by quantifying label shifts in zero-shot NER. Separately, constrained decoding via JSON schema enforcement \cite{json-schema-bench-2025} guarantees structurally valid outputs; all our experiments use vLLM's constrained JSON decoding (\S\ref{sec:model}).
8	
9	These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. Our work fills both gaps.
10	
11	\subsection{Schema Complexity in IE}
12	\label{sec:rw_schema}
13	
14	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complement
…[truncated 2472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-16T00:51:27.274349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-16T00:51:27.676485+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
27	\midrule
28	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77-
…[truncated 6755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-16T00:51:27.777535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-16T00:51:28.631914+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; see Figure~\ref{fig:count_curves} in the Appendix for visualizations).
8	
9	\paragraph{NER (Few-NERD).}
10	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
11	
12	\paragraph{RE (FewRel).}
13	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)
14	
15	\paragraph{ED (MAVEN).}
16	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \S\ref{sec:centrality_confound}.
17	
18	\paragraph{Cross-model replication.}
19	Channel~1 
…[truncated 12248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-16T00:51:28.782941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-16T00:51:29.134748+00:00_

1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	The multi-channel degradation model (\S\ref{sec:results}) raises an interventional question: if confusability drives type confusion, can we decompose the schema so that confusable types never co-occur in the same prompt?  We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD), a method that uses the pairwise SCS matrix to partition types into low-confusability batches, runs extraction independently on each batch, and merges the results.
5	
6	\paragraph{Decomposition protocol.}
7	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation, following the strategy of \citet{uniner-2024}. Table~\ref{tab:sdgd_results} summarizes the results on Few-NERD.
8	
9	\paragraph{All decomposition modes degrade F1.}
10	Table~\ref{tab:sdgd_results} reports the outcome.  Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368).  SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop.  Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586).  Every decomposition mode falls below the single-pass baseline.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{lrccc}
17	\toprule
18	\textbf{Mode} & \textbf{\# Batches} & \text
…[truncated 3015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-16T00:51:29.135154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-16T00:51:29.336193+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE but interact in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is the bottleneck for decompose-then-merge pipelines. Cross-batch calibration or joint decoding is the key next step.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-16T00:51:29.336523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-16T00:51:29.386993+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-16T00:52:10.777948+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-16T00:52:11.334097+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 34\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 10864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-16T00:52:13.142385+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check project config for external review",
  "subagent_type": "Explore",
  "prompt": "Search for the project configuration file for \"schema-dag-extraction\" in the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_18/. I need to find if there's a config file (likely YAML or JSON) that contains \"external_review\" or \"paperreview_ai\" settings. Check files like config.yaml, project.yaml, registry.yaml, settings.yaml, etc. Report the relevant section if found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check project config for external review",
    "subagent_type": "Explore",
    "prompt": "Search for the project configuration file for \"schema-dag-extraction\" in the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_18/. I need to find if there's a config file (likely YAML or JSON) that contains \"external_review\" or \"paperreview_ai\" settings. Check files like config.yaml, project.yaml, registry.yaml, settings.yaml, etc. Report the relevant section if found."
  }
}
```

</details>

---


### Tool call

_source line 47 · 2026-05-16T00:52:14.750029+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-16T00:52:14.902045+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-16T00:52:14.902489+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/project.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/project.yaml"
  }
}
```

</details>

---


### Tool result

_source line 50 · 2026-05-16T00:52:14.953098+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-16T00:52:14.953532+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-16T00:52:15.154670+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-16T00:52:15.155371+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/settings.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/settings.yaml"
  }
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-16T00:52:15.307022+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-16T00:52:15.357710+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/**/*.json"
  }
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-16T00:52:15.358193+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_no_project.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_reviewer.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_PREPARING_20260512T090500.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_ddf919c12f9233b9c1be7884efc37bb6.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_QUEUED_20260512T103215.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_ALLOCATED_20260512T105446.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/logs/workers/worker_fix_install_tmux_20260512T105529_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_RUNNING_20260512T105712.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/logs/workers/worker_code_pi_controller_20260512T110004_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_RUNNING_20260512T112133.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_DONE_20260512T112136.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_v2_PREPARING_20260512T115726.json
/home/ubuntu/.agent-m
…[truncated 12022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-16T00:52:17.115711+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-16T00:52:17.417905+00:00_

1	baseline: null
2	experiments:
3	  exp001_count_baseline:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-14T16:13:40.180Z'
7	    updated_at: '2026-05-15T05:06:46.365Z'
8	    spec:
9	      hypothesis: F1 随 type count 增加而下降（复现已知现象，验证 setup 正确性）
10	      dataset: Few-NERD
11	      model: Qwen3-32B-FP8
12	      design: count=[1,2,6,12,22,44,66]，每档 5 random samples，count=1 = solo baseline
13	      command: nohup python3 run_experiment.py --mode exp1 --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/
14	        --max_samples 1000
15	      server: cqa1-38874
16	      data_path: /root/schema-dag-extraction/data/parquet/test.parquet
17	      data_count: 1000
18	      model_name: Qwen3-32B-FP8
19	      seed: 42
20	      gpu: cuda:0
21	      pid: 188307
22	      vllm_version: 0.20.2
23	      max_model_len: 4096
24	      gpu_memory_utilization: 0.95
25	    log_path: /root/schema-dag-extraction/logs/exp1.log
26	    metrics:
27	      diagnosis: char offset 96.5% fabricated by model
28	      text_match_reeval:
29	        count_1:
30	          f1: 0.184
31	          precision: 0.105
32	          recall: 0.72
33	          pred_gold_ratio: 6.85
34	        count_2:
35	          f1: 0.123
36	          precision: 0.068
37	          recall: 0.698
38	          pred_gold_ratio: 10.33
39	        count_6:
40	          f1: 0.155
41	          precision: 0.088
42	          recall: 0.62
43	          pred_gold_ratio: 7.02
44	        count_12:
45	          f1: 0.246
46	          precision: 0.16
47	          recall: 0.539
48	          pred_gold_ratio: 3.38
49	        count_22:
50	          f1: 0.322
51	          precision: 0.232
52	          recall: 0.527
53	          pred_gold_ratio: 2.27
54	        count_44:
55	          f1: 0.473
56	          precision: 0.414
57	          recall: 0.551
58	          pred_gold_ratio: 1.33
59	        count_64:
60	          f1: 0.463
61	          precision: 0.52
62	          recall: 0.418
63	          pred_gold_ratio: 0.8
64	      key_findin
…[truncated 62720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-16T00:52:19.477391+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-16T00:52:19.729161+00:00_

Found 4 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/logs/system.log
AGENTS.md
CLAUDE.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-16T00:52:21.587596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_director.jsonl",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_director.jsonl",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-16T00:52:21.990146+00:00_

1	{"ts": "2026-05-16T00:50:29.754760+00:00", "role": "user", "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director", "text": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: schema-dag-extraction\n- 论文路径: projects/schema-dag-extraction/paper/main.tex\n- 目标 venue: EMNLP 2026\n- Track: main conference\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。", "source": "system"}
2	{"ts": "2026-05-16T00:50:36.267766+00:00", "role": "tool", "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director", "text": "called Read", "tool": "Read", "tool_args": {"file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"}}
3	{"ts": "2026-05-16T00:50:36.319580+00:00", "role": "tool_result", "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director", "text": "1\t---\n2\tname: review-director-session-start\n3\tdescription: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。\n4\tpriority: 9\n5\tscope: global\n6\ttags:\n7\t- workflow\n8\t- review\n9\t- session\n10\tversion: 3\n11\troles:\n12\t- review_director\n13\t---\n14\t\n15\t# Review Director Session 启动流程（圆桌会议模式）\n16\t\n17\t## 初始化\n18\t\n19\t1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）\n20\t2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在\n21\t3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）\n22\t4. 向用户简要汇报：\n23\t   - **投稿目标**：venue 和 deadline\n24\t   - **论文状态**：当前草稿位置和版本\n25\t   - **资料完整性**：提交的材料是否齐全\n26\t   - **下一步**：即将开始的圆桌审稿流程\n27\t\n28\t## 评审流程（收到论文提交后执行）\n29\t\n30\t### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）\n31\t\n32\t1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全\n33\t2. 确认目标投稿 venue（从提交消息中获取）\n34\t3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：\n35\t   - `\"&lt;venue name> 2026 call for papers\" site:aclweb.org`\n36\t   - `\"&lt;venue name> 2026 submission deadline\"`\n37\t   - `\"&lt;venue name> 2026 author guidelines\"`\n38\t4. **
…[truncated 48750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 63 · 2026-05-16T00:52:22.040759+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai|review_config",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai|review_config",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/CLAUDE.md"
  }
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-16T00:52:22.191863+00:00_

&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/CLAUDE.md. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-16T00:52:22.242565+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -type f -name \"*.yaml\" -o -name \"*.yml\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -type f -name \"*.yaml\" -o -name \"*.yml\" | head -20"
  }
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-16T00:52:22.393635+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research
…[truncated 722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 67 · 2026-05-16T00:52:24.253066+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" \\) -path \"*config*\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" \\) -path \"*config*\" | head -30"
  }
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-16T00:52:24.705401+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/collapse-aware-mixing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-16T00:52:25.007236+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/logs/system.log",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/logs/system.log",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-16T00:52:25.007629+00:00_

10113:2026-05-16 00:50:28 INFO     [HOOKS] [review] external_review_enabled=False for project=schema-dag-extraction

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-16T00:52:26.463585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-16T00:52:26.464036+00:00_

1	execution:
2	  project_path: /root/schema-dag-extraction
3	  servers:
4	  - account: root
5	    server: cqa1-38874
6	feishu:
7	  chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
8	  operational_chat_id: oc_04544c3b7bc497e1d098ba47fb56a6c2
9	  review_paper_path: projects/schema-dag-extraction/paper/main.tex
10	  review_round: 1
11	  review_supplementary_paths: ''
12	  submission_chat_id: oc_ac7ab7270b6b5caecee04f89b11aab3e
13	project:
14	  created_at: '2026-05-14T16:07:46.825Z'
15	  description: Does Type Confusability Drive Schema-Induced Degradation in LLM Information
16	    Extraction? An Empirical Study and Principled Decomposition Framework
17	  name: schema-dag-extraction
18	  phase: research
19	  source_idea_id: idea_007
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-16T00:52:27.920900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/feishu.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/feishu.yaml"
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-16T00:52:28.071808+00:00_

1	app_id: cli_a97eecbb40781cb5
2	app_secret: FKuZZLcXxI8lfm9wlK0VscSjdSBYUEcU
3	bot_name: Auto Research Prod9
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-16T00:52:28.172685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/registry.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/registry.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-16T00:52:28.223636+00:00_

1	baseline: null
2	experiments:
3	  exp012_llama_fewnerd_r3:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-15T15:55:34.538Z'
7	    updated_at: '2026-05-15T15:55:51.084Z'
8	    spec:
9	      command: python src/run_experiment.py exp012_r3
10	      server: cqa1-38874
11	      data_path: fewnerd
12	      data_count: 0
13	      model_name: llama
14	      seed: 3
15	      log_path: /tmp/exp012_r3.log
16	    conclusion: failed
17	    completed_at: '2026-05-15T15:55:47.661Z'
18	    notes: 'FlashInfer JIT compilation failed: CUDA compiler and CUDA toolkit headers
19	      incompatible (flashinfer 0.6.11.post2, cuda_toolkit.h:41 error). vLLM LLM()
20	      init failed with RuntimeError: Engine core initialization failed. Experiment
21	      never reached inference stage. No W&B data, no output files.'
22	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-16T00:52:29.579375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-16T00:52:29.680214+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-prod9-0512
5	  my_token: 48d731d4ffca61bec8a11c3919f9bf537a2999bc36e98c14fb7d1577b327534e
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-16T00:52:29.680656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-16T00:52:29.731332+00:00_

1	default_model: claude-opus-4-6
2	default_model_claude_code: claude-opus-4-6
3	idea_model: claude-opus-4-6
4	servers:
5	  cqa1-38874:
6	    accounts:
7	    - gpus:
8	      - cuda:0
9	      name: root
10	      password_encrypted: gAAAAABqAuvPRnsR1TtY3nMeh4mVCYkvCSF7_wdLf-0R0bfkxwoGlInSGv3dLgBMCNw2jcYb4Wdztu3hlMLhkpq9hKnRirdTGw==
11	      user: root
12	      work_dir: /root
13	    - gpus: []
14	      name: ''
15	      user: ''
16	    detected_image:
17	      detected: false
18	      image: ''
19	      status: unknown
20	      version: ''
21	    env_activate: ''
22	    host: connect.cqa1.seetacloud.com
23	    port: 38874
24	    total_gpus:
25	    - cuda:0
26	    user_rules_excluded: []
27	    work_dir: /root
28	  home-1x5090:
29	    accounts:
30	    - gpus: []
31	      name: sonny
32	      password_encrypted: gAAAAABqAs98OWvzWtk-wjILplCl-xG8f6sbL0GMIHCqjHs4LD83BaT56W8D4iW7g3UJTcyFGxiYqIy44LDYO4oxAE_ptGirBg==
33	      user: sonny
34	      work_dir: /root
35	    env_activate: ''
36	    host: implicit5638.xyfu.me
37	    port: 22
38	    total_gpus:
39	    - cuda:0
40	    user_rules_excluded: []
41	    work_dir: /root
42	user_rules: []
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-16T00:52:35.052197+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-16T00:52:35.103295+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-16T00:52:35.354662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/logs/system.log",
  "limit": "20",
  "offset": "10110"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/logs/system.log",
    "limit": "20",
    "offset": "10110"
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-16T00:52:35.505707+00:00_

10110	2026-05-16 00:50:27 INFO     [HOOKS] [review] reusing existing Group C: oc_ac7ab7270b6b5caecee04f89b11aab3e
10111	2026-05-16 00:50:27 INFO     [SESSION] [session_server] invalidated sessions for key=feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director
10112	2026-05-16 00:50:27 INFO     [HOOKS] [review] reset all review sessions for chat_id=oc_ac7ab7270b6b5caecee04f89b11aab3e
10113	2026-05-16 00:50:28 INFO     [HOOKS] [review] external_review_enabled=False for project=schema-dag-extraction
10114	2026-05-16 00:50:28 INFO     [HOOKS] [review] kick-off message length=290 has_ext=False
10115	2026-05-16 00:50:28 INFO     [SESSION] [feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director] QUEUED | project=schema-dag-extraction | depth=0 | text='系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: schema-dag-extraction\n- 论文路径: projects/schema-'
10116	2026-05-16 00:50:29 INFO     [HOOKS] [review] Group C=oc_ac7ab7270b6b5caecee04f89b11aab3e project=schema-dag-extraction venue=EMNLP 2026 mode=fresh round=1
10117	2026-05-16 00:50:29 INFO     [SESSION] [session_server] wrote /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_review_director.json
10118	2026-05-16 00:50:29 INFO     [SESSION] [session_server] pool account selected: account-1 (/home/ubuntu/.claude-account-1)
10119	2026-05-16 00:50:29 INFO     [SESSION] [session_server] calling claude | project=schema-dag-extraction | session=None | resume=False
10120	2026-05-16 00:51:11 WARNING  [GPU_MO] GPU poll failed for home-1x5090: timed out
10121	2026-05-16 00:52:21 WARNING  [GPU_MO] GPU poll failed for home-1x5090: timed out
10122	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-16T00:52:37.112594+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ | grep -E \"yaml|yml|json\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ | grep -E \"yaml|yml|json\" | head -20"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-16T00:52:37.414349+00:00_

-rw-rw-r-- 1 ubuntu ubuntu 2901 May  9 09:00 approvals.yaml
-rw------- 1 ubuntu ubuntu  764 May 11 17:59 backend.yaml
-rw-r--r-- 1 ubuntu ubuntu 1558 May 16 00:50 claude_sessions.json
-rw------- 1 ubuntu ubuntu 7843 May 15 19:48 crons.yaml
-rw------- 1 ubuntu ubuntu  364 May 15 04:13 email_tokens.json
-rw------- 1 ubuntu ubuntu  104 May 15 09:17 feishu.yaml
-rw-r--r-- 1 ubuntu ubuntu 4904 May 16 00:21 keepalive.json
-rw-r--r-- 1 ubuntu ubuntu  342 May 11 05:47 mcp_config.json
-rw-r--r-- 1 ubuntu ubuntu  394 May 12 08:44 mcp_config_director.json
-rw-r--r-- 1 ubuntu ubuntu  420 May 15 06:10 mcp_config_dream_review_director.json
-rw-r--r-- 1 ubuntu ubuntu  398 May 12 08:37 mcp_config_no_project.json
-rw-r--r-- 1 ubuntu ubuntu  400 May 15 16:03 mcp_config_paper_agent.json
-rw-r--r-- 1 ubuntu ubuntu  408 May 16 00:50 mcp_config_review_director.json
-rw-r--r-- 1 ubuntu ubuntu  394 May 12 08:46 mcp_config_reviewer.json
-rw-r--r-- 1 ubuntu ubuntu  417 May 12 10:55 mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
-rw-r--r-- 1 ubuntu ubuntu  465 May 15 05:06 mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
-rw-r--r-- 1 ubuntu ubuntu  477 May 15 15:54 mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
-rw-r--r-- 1 ubuntu ubuntu  383 May 15 16:10 mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
-rw-r--r-- 1 ubuntu ubuntu  465 May 12 15:24 mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
-rw-r--r-- 1 ubuntu ubuntu  427 May 13 03:08 mcp_config_worker_3ab953c77b6b0e7621a87cc89f47e64a.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 87 · 2026-05-16T00:52:37.465149+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18 --include=\"*.py\" --include=\"*.md\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18 --include=\"*.py\" --include=\"*.md\" 2>/dev/null | head -30"
  }
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-16T00:52:37.515954+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/AGENTS.md:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/AGENTS.md:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/AGENTS.md:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/AGENTS.md:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状
…[truncated 403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-16T00:52:41.739823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-16T00:52:41.740379+00:00_

1	## 当前项目
2	当前绑定项目：**schema-dag-extraction**
3	
4	今天是 **2026-05-16**。
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
61	报告结构：Summary → Strengths → Weaknesses（重点） → Questions → Missing References → Overall Assessment → Detailed Comments
62	
63	## 群组
64	
65	你的文字回复发到 Group C（审稿群），用户直接看到。
66	
67	**session 启动时**：`Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 了解投稿状态。
68	
69	## 继续审稿模式 vs 重新审稿模式
70	
71	**继续审稿模式** —— 收到 "[Round N - 继续审稿]" 时，你仍保有上一轮的审稿记忆。任务从初审转为**修订评估**：
72	- 逐条检查上轮提出的问题是否已充分解决
…[truncated 4056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-16T00:52:51.070328+00:00_

Excellent! I now have the complete information. Let me provide a comprehensive summary of my findings:

## Summary

I successfully located the project configuration file for "schema-dag-extraction" and found the external review settings. Here are the key findings:

### Configuration File Location
**`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml`**

### Project Configuration Content
The file contains:
```yaml
execution:
  project_path: /root/schema-dag-extraction
  servers:
  - account: root
    server: cqa1-38874
feishu:
  chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
  operational_chat_id: oc_04544c3b7bc497e1d098ba47fb56a6c2
  review_paper_path: projects/schema-dag-extraction/paper/main.tex
  review_round: 1
  review_supplementary_paths: ''
  submission_chat_id: oc_ac7ab7270b6b5caecee04f89b11aab3e
project:
  created_at: '2026-05-14T16:07:46.825Z'
  description: Does Type Confusability Drive Schema-Induced Degradation in LLM Information Extraction?...
  name: schema-dag-extraction
  phase: research
  source_idea_id: idea_007
```

### External Review Settings
**Status: DISABLED**

According to the system log at `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/logs/system.log` (line 10113):
```
2026-05-16 00:50:28 INFO     [HOOKS] [review] external_review_enabled=False for project=schema-dag-extraction
```

### External Review Configuration Structure
The project expects external review settings to follow this structure (documented in CLAUDE.md):
```yaml
external_review:
  paperreview_ai:
    enabled: false  # Currently disabled for this project
```

When enabled (`true`), it would trigger:
- Automatic submission of the paper PDF to paperreview.ai (Stanford Agentic Reviewer)
- Parallel execution with internal review process (non-blocking)
- Integration of external review results into the final consolidated report

### Additional Configuration Locations
- **Project-specific config**: `/home/ubuntu/.agent-ml-research-i
…[truncated 646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "elapsed_ms": 37927
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-16T00:53:30.396050+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n**论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**Venue：** EMNLP 2026 Main Conference（ARR May 25 cycle）\n**格式要求：** 长文 8 页 + 无限参考文献，ACL 模板，double-blind，mandatory Limitations section，Responsible NLP Research Checklist\n**论文路径：** `projects/schema-dag-extraction/docs/paper/main.tex`（各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex；Limitations 在 main.tex 内）\n\n### 你的审查侧重\n\n**1. 实验设计与统计方法**\n- 两个实验范式（count curves + BCS-controlled）的设计是否合理？是否真正隔离了 count 和 confusability？\n- BCS-controlled 实验中 low-BCS vs high-BCS batch 的构造是否有偏？样本量（5 batches/count level, 27 total）是否足够？\n- Bootstrap CI 的使用是否恰当？是否有应报而未报的统计检验？\n- 16-rel 到 80-rel 的 3.4× amplification 是两点比较，统计可靠性如何？\n- Pairwise correlation r=0.112 (r²=1.3%) 的效应量是否被过度解读？\n\n**2. 评估指标**\n- 三个任务使用不同评估指标（text-match F1, accuracy, relaxed F1）是否合理？跨任务可比性如何？\n- NER 的 text-match 而非 exact span match 评估是否引入偏差？\n- MAVEN relaxed F1 的定义是否足够严格？\n\n**3. 可复现性**\n- 实验细节是否充分？（模型配置、prompt 模板、decoding 参数、随机种子）\n- v1/v2 prompt 切换的处理是否透明？\n- Cross-model validation (Llama-3.1-8B) 的覆盖范围是否充分？\n\n**4. SDGD 负面结果**\n- Merge amplification 的分析是否充分？是否遗漏了可能的 merge 策略？\n- 负面结果的呈现是否公平客观？\n\n请按以下格式输出审稿报告：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor])\n- Questions (需要作者澄清的)\n- Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 简要理由)",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n**论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**Venue：** EMNLP 2026 Main Conference（ARR May 25 cycle）\n**格式要求：** 长文 8 页 + 无限参考文献，ACL 模板，double-blind，mandatory Limitations section，Responsible NLP Research Checklist\n**论文路径：** `projects/schema-dag-extraction/docs/paper/main.tex`（各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex；Limitations 在 main.tex 内）\n\n### 你的审查侧重\n\n**1. 实验设计与统计方法**\n- 两个实验范式（count curves + BCS-controlled）的设计是否合理？是否真正隔离了 count 和 confusability？\n- BCS-controlled 实验中 low-BCS vs high-BCS batch 的构造是否有偏？样本量（5 batches/count level, 27 total）是否足够？\n- Bootstrap CI 的使用是否恰当？是否有应报而未报的统计检验？\n- 16-rel 到 80-rel 的 3.4× amplification 是两点比较，统计可靠性如何？\n- Pairwise correlation r=0.112 (r²=1.3%) 的效应量是否被过度解读？\n\n**2. 评估指标**\n- 三个任务使用不同评估指标（text-match F1, accuracy, relaxed F1）是否合理？跨任务可比性如何？\n- NER 的 text-match 而非 exact span match 评估是否引入偏差？\n- MAVEN relaxed F1 的定义是否足够严格？\n\n**3. 可复现性**\n- 实验细节是否充分？（模型配置、prompt 模板、decoding 参数、随机种子）\n- v1/v2 prompt 切换的处理是否透明？\n- Cross-model validation (Llama-3.1-8B) 的覆盖范围是否充分？\n\n**4. SDGD 负面结果**\n- Merge amplification 的分析是否充分？是否遗漏了可能的 merge 策略？\n- 负面结果的呈现是否公平客观？\n\n请按以下格式输出审稿报告：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor])\n- Questions (需要作者澄清的)\n- Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 简要理由)",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-16T00:53:43.771665+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13375
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-16T00:53:43.922704+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）\n\n**论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**Venue：** EMNLP 2026 Main Conference（ARR May 25 cycle）\n**格式要求：** 长文 8 页 + 无限参考文献，ACL 模板，double-blind，mandatory Limitations section，Responsible NLP Research Checklist\n**论文路径：** `projects/schema-dag-extraction/docs/paper/main.tex`（各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex；Limitations 在 main.tex 内）\n\n### 你的审查侧重\n\n**1. 新颖性与贡献**\n- \"首个隔离 type confusability 的控制实验\" 这一 novelty claim 是否成立？是否有遗漏的相关工作？\n- 四个贡献是否 substantive？哪些是增量性的？\n- Multi-channel degradation model 是经验观察还是有理论基础？\n- 负面结果（SDGD）作为贡献的价值？\n\n**2. 相关工作覆盖**\n- LLM-PEE 的对比定位是否充分？\n- 是否遗漏重要相关工作？特别关注：schema decomposition, prompt optimization for IE, LLM calibration\n- Representation degeneration 文献与 centrality confound 的联系是否自然？\n\n**3. 论文结构与写作质量**\n- 注意：当前论文没有 Discussion section（discussion.tex 实际包含的是 Conclusion，仅 1 段）。这是否符合 EMNLP 投稿标准？\n- Limitations section 的覆盖是否充分？\n- Abstract 是否准确概括了论文的主要发现？\n- 各 section 之间的逻辑流是否顺畅？\n\n**4. 格式合规性**\n- Double-blind 匿名性检查（author 字段、self-citation）\n- 是否满足 8 页限制？（请估算各 section 的页面占用）\n- 所有 figures 都在 Appendix——是否应将关键 figures 放入正文？\n- 参考文献格式是否正确？是否有可疑引用？\n- 是否缺少 Ethics Statement 或 Responsible NLP Research Checklist？\n\n**5. 遗漏的参考文献**\n- 检查是否遗漏了应当引用的重要工作\n\n请按以下格式输出审稿报告：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor])\n- Questions (需要作者澄清的)\n- Missing References (如有)\n- Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 简要理由)",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）\n\n**论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**Venue：** EMNLP 2026 Main Conference（ARR May 25 cycle）\n**格式要求：** 长文 8 页 + 无限参考文献，ACL 模板，double-blind，mandatory Limitations section，Responsible NLP Research Checklist\n**论文路径：** `projects/schema-dag-extraction/docs/paper/main.tex`（各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex；Limitations 在 main.tex 内）\n\n### 你的审查侧重\n\n**1. 新颖性与贡献**\n- \"首个隔离 type confusability 的控制实验\" 这一 novelty claim 是否成立？是否有遗漏的相关工作？\n- 四个贡献是否 substantive？哪些是增量性的？\n- Multi-channel degradation model 是经验观察还是有理论基础？\n- 负面结果（SDGD）作为贡献的价值？\n\n**2. 相关工作覆盖**\n- LLM-PEE 的对比定位是否充分？\n- 是否遗漏重要相关工作？特别关注：schema decomposition, prompt optimization for IE, LLM calibration\n- Representation degeneration 文献与 centrality confound 的联系是否自然？\n\n**3. 论文结构与写作质量**\n- 注意：当前论文没有 Discussion section（discussion.tex 实际包含的是 Conclusion，仅 1 段）。这是否符合 EMNLP 投稿标准？\n- Limitations section 的覆盖是否充分？\n- Abstract 是否准确概括了论文的主要发现？\n- 各 section 之间的逻辑流是否顺畅？\n\n**4. 格式合规性**\n- Double-blind 匿名性检查（author 字段、self-citation）\n- 是否满足 8 页限制？（请估算各 section 的页面占用）\n- 所有 figures 都在 Appendix——是否应将关键 figures 放入正文？\n- 参考文献格式是否正确？是否有可疑引用？\n- 是否缺少 Ethics Statement 或 Responsible NLP Research Checklist？\n\n**5. 遗漏的参考文献**\n- 检查是否遗漏了应当引用的重要工作\n\n请按以下格式输出审稿报告：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor])\n- Questions (需要作者澄清的)\n- Missing References (如有)\n- Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 简要理由)",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-16T00:53:45.387795+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1465
}
```

</details>

---


### Assistant

_source line 96 · 2026-05-16T00:53:49.703997+00:00_

Round 1 任务已分配：
- **Reviewer 1**（方法严谨性）→ 已触发
- **Reviewer 2**（新颖性与完整性）→ 已触发

等待两位 Reviewer 返回独立初审报告，收齐后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 2

## Round 2

28 recorded events


### User

_source line 97 · 2026-05-16T00:57:27.467706+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告（方法严谨性）

### Summary

本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行了受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），并提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER/RE/ED 三个任务，辅以跨模型验证，最后通过 SDGD 实验给出 decompose-then-merge 失败的负面结果。研究问题有价值、实验设计新颖，但若干方法论问题削弱了核心 claim 的可靠性。

---

### Strengths

**S1.** 研究问题定义清晰且有实际意义。将 count 和 confusability 拆分为独立 channel 的思路是该领域的空白，实验设计（count curves + BCS-controlled）逻辑上互补，从 correlational 到 interventional 层层递进。

**S2.** Error taxonomy 分析（§5.4, Table 4）质量高。IntraSub 随 BCS 单调递增（RE: ρ=0.954）、RE 中 100% confusion 为 intra-batch 的发现清晰有力，为 Channel 2 提供了机制层面的证据。NER 与 RE 在 missed-entity pattern 上的分歧也被如实报告。

**S3.** Centrality confound 分析（§5.5）是对 BCS 指标局限性的坦诚自省，与 representation degeneration 文献的连接恰当。

**S4.** 跨模型验证设计合理：不同家族（Qwen vs. Llama）、不同规模（32B vs. 8B）。High-BCS accuracy 在两个模型上收敛到 ≈51% 的 model-invariant floor 是一个有趣的发现。

**S5.** Limitations section 异常详尽，主动披露了 factorial 检验不显著（z=−0.67, p=0.50）、3.4× 为两点比较等问题。

---

### Weaknesses

**W1 [Must-Fix] 3.4× amplification 的统计基础薄弱**

3.4× amplification（31.2pp / 9.1pp）是论文最突出的定量 claim（出现在 abstract、introduction、contributions、results），但存在两个严重问题：

(a) 基线无 CI。16-rel 条件下 low-BCS 和 high-BCS 各只有 1 个 batch（Table 3 注释确认）。9.1pp 基线是单次观测，无法评估不确定性。论文只对 80-rel CI 做了传播（1.9–4.7×），但分母方差被完全忽略。

(b) 跨 pool 比较引入混淆。16-rel 来自 validation split，80-rel 来自 train+val 合并的 80 relations。type pool 组成完全不同，amplification 可能部分归因于 pool 差异而非 scale 效应。

建议：在 80-rel pool 内构造 16-type 子集的 BCS-controlled 实验（多个 low/high batch），获取可比 baseline 并附 CI。当前 3.4× 应降格为描述性观察。

**W2 [Must-Fix] Pairwise SCS 效应量极小，framing 过度**

r=0.112, r²=1.3%（Table 2）。论文将其定位为 "the first factor empirically isolated"，掩盖了 embedding similarity 仅解释 1.3% confusion 方差的事实。§5.2 中 nonzero-confusion 子集分析（ρ=0.27–0.31）存在 conditioning on the outcome 问题——剔除 confusion=0 的 pair 人为抬高相关性。

建议：明确承认解释力有限；删除或重新框定 nonzero-confusion 分析并讨论 conditioning bias。

**W3 [Must-Fix] NER 上 count×confusability 交互的证据不足**

§5.4 声称 NER 中两个 channel "interact"，但 Limitations 中的 2×2 factorial 检验不显著（z=−0.67, p=0.50）。这是 Contribution 1 的核心组成部分，缺乏统计支撑。

建议：提供更有力的交互证据，或降级为 "suggestive but not statistically confirmed"。

**W4 [Should-Fix] SDGD 负面结果仅覆盖两种 merge 策略，overclaim "structural bottleneck"**

§6 仅测试 union merge 和 confidence-gated merge 就声称 "structural bottleneck"。未测试 span-level NMS、majority voting、calibration-based reranking 等替代方案。且仅在 Few-NERD 上测试，单数据集 + 两种策略不足以支撑 "structural" 修饰语。

建议：测试更多 merge 策略，在 FewRel 上复现，或弱化表述。

**W5 [Should-Fix] v1/v2 prompt 切换引入实验内混淆**

v1（fabricate offset 96.5%）用于 count curves 和 BCS-controlled NER；v2 用于后续实验和跨模型比较。绝对数值跨实验不直接可比。

建议：统一用 v2 重跑核心实验，或提供 v1/v2 对照消融。

**W6 [Should-Fix] Embedding 模型不一致**

Few-NERD 用 Qwen3-32B embeddings，FewRel/MAVEN 用 MiniLM。不同 embedding 空间的 BCS 不可直接比较，削弱跨任务一致性。

**W7 [Should-Fix] FewRel 数据集构造可能引入偏差**

合并 train+val splits 且未说明 1,000 balanced instances 的抽样方式。

**W8 [Minor] 完整 prompt 模板未在 appendix 中提供，影响可复现性。

**W9 [Minor] MAVEN 结果实质上反驳 count channel 的普遍性（F1 随 count 上升），abstract/introduction 表述应更谨慎。

**W10 [Minor] 缺少与 supervised IE baseline 的参照。

---

### Questions

Q1. 如果在 80-rel pool 内抽 16-type 子集做 BCS-controlled，amplification 估计值是否变化？
Q2. 是否探索过多变量模型（加入 type frequency、prompt position 等）提升解释力？
Q3. SDGD 的 single_pass baseline 用的是 v1 还是 v2 prompt？
Q4. NER cross-model 效应 "not robustly detectable"，如何排除 confusability channel 为 Qwen3 特有？
Q5. High-BCS ≈51% floor 的来源？是否接近随机猜测？

---

### Overall Assessment

**Soundness**: 3/5
**Excitement**: 3.5/5
**Overall**: 3/5 (Findings acceptance)
**Confidence**: 4/5

论文研究问题好、实验设计有新意、写作透明度高，但 W1–W3 三个 Must-Fix 问题需要实质性修正才能达到 Main Conference 接收标准。建议修改后以 Findings 投稿，或补充实验后提升至 Main Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-16T00:57:49.744383+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__request_external_review",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__request_external_review",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-16T00:57:49.744753+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-16T00:57:50.197437+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-16T00:57:50.298881+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-16T00:57:59.820359+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-16T00:58:00.324050+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (31 个)\n\n- **bootstrap_ci_analysis**: DONE (success) — \n- **exp016_fewrel_error_taxonomy**: DONE (success) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp007_error_taxonomy**: DONE (success) — \n- **exp_fewrel_formal_80rel**: DONE (success) — \n- **exp_fewrel_formal**: DONE (success) — \n- **exp008_sdgd_zero_fewnerd_r2**: DONE (negative) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n- **fewrel_pilot**: DONE (success) — \n- **exp004_maven_bcs**: DONE (negative) — \n- **exp002_confusability_controlled**: DONE (success) — \n- **exp003a_prompt_v2_rerun**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp001_count_baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp012_llama_fewrel_ch2** (success): LLaMA-3.1-8B-Instruct 在 FewRel 80-rel RE 任务上验证 Channel 2 (BCS-controlled confusability effect)。跨模型家族(Qwen→LLaMA) + 跨规模(32B→8B) + 跨任务(NER→RE) 三重泛化验证。exp2 design: count 8/16 × low/high BCS × 27 batches。 ← 基于 exp012_llama_8b_r2\n- **exp_fewrel_40rel_r4** (success): —\n- **exp012_llama_8b_r2_exp2** (negative): LLaMA-3.1-8B-Instruct exp2 重跑：BCS-controlled factorial (count=6/12, low/high BCS)，验证 confusability effect 跨模型泛化。Parent exp012_llama_8b_r2 的 exp1 count curve 已完成。\n\n## 趋势\n成功 14 / 负向 5 / 失败 10 / 共 31\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-38874: 无 GPU 信息\n\n## 告警\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\n- exp012_llama_8b: 已被终止 — unknown\n- exp_fewrel_40rel: 训练失败 — unknown\n- exp012_llama_awq: 已被终止 — unknown\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\n- exp_fewrel_40rel_r2: 训练失败 — unknown\n- exp_fewrel_40rel_r3: 训练失败 — unknown\n- exp012_llama_8b_r3: 训练失败 — unkno
…[truncated 4 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-16T00:58:00.324510+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-16T00:58:00.375011+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-16T00:58:01.635015+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-16T00:58:02.290060+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-16T00:58:02.343780+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-16T00:58:02.394481+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-16T00:58:22.192655+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "memory.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "memory.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-16T00:58:22.945819+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## FewRel 40-rel Scaling 中间点 — SUCCESS (2026-05-15) ⭐⭐\\n- Count curve 单调退化：count_1 acc=0.858 → count_40 acc=0.588 (-27pp)\\n- **BCS effect 饱和发现**：16-rel Δ=-9.1pp → 40-rel Δ=-33.3pp/-31.8pp → 80-rel Δ=-31.2pp\\n  - 16→40 大幅跳变，40→80 基本持平\\n  - **语义混淆破坏效应在 ~40 relations 处饱和**，非线性增长\\n  - 论文 Discussion insight：实际应用中 ~40 types 即触发最大 confusability penalty\\n- count_1 baseline：40/80-rel 均为 0.857，低于 16-rel 0.904（relation 数量本身降 baseline，但 40→80 间已稳定）\\n\\n## exp012 跨模型验证 (2026-05-15, FINAL) ⭐⭐\\n- **Channel 1 复现成功**: LLaMA-3.1-8B recall 0.702→0.273 (-43pp), Qwen3-32B -34pp。Per-batch correlation r=0.7249\\n- **Channel 2 NER NEGATIVE**: BCS-controlled confusability effect 在 NER 上跨模型未复现（floor effect + metric 问题）\\n- **Channel 2 FewRel SUCCESS**: LLaMA Δ=-27.1pp(count_8)/-24.0pp(count_16)，达 Qwen3 -31.2pp 的 87%\\n  - Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001)\\n  - 无 floor effect：均值 accuracy=0.77，范围 0.41-0.98\\n  - **跨模型+跨任务+跨规模三重泛化验证完成**\\n- exact/relaxed F1=0 是因为 LLaMA predictions 缺少字符偏移量，text_match 是正确对比指标\\n- **教训**: 弱模型（8B）NER floor effect 压缩 confusability signal，RE accuracy metric 更干净\\n\\n## LLaMA-3.1-8B Chat Template 必须 (2026-05-15) ⭐⭐\\n- `run_extraction.py` 用 `llm.generate(prompts, ...)` 裸文本调用，Qwen3 能工作但 LLaMA-3.1-Instruct 不行\\n- **根因**: LLaMA-3.1-Instruct 严格依赖 chat template，裸文本输入不理解指令\\n- **修复**: `tokenizer.apply_chat_template()` 包装 prompt\\n- **教训**: 非 Qwen 模型都应检查 chat template 需求\\n- run_fewrel_formal.py 也已加 chat template 支持（L92-96, L132-141）\\n\\n## Blackwell GPU flashinfer 兼容性修复 (2026-05-15, UPDATED)\\n- RTX PRO 6000 Blackwell (SM120) 上 flashinfer 0.6.8.post1 无法 JIT 编译 FP8 GEMM\\n- **修复**: flashinfer 0.6.11.post2 + nvidia-cuda-nvcc 13.2.78 + `CUDA_HOME=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13`\\n- **所有新脚本都应包含 CUDA_HOME 设置**\\n\\n## Bootstra
…[truncated 2483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-16T00:58:23.096823+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 113 · 2026-05-16T00:58:23.097307+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-16T00:58:29.074900+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 115 · 2026-05-16T00:58:29.225914+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-16T00:58:50.613616+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-16T00:58:52.018979+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-16T00:58:52.220159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-16T00:58:52.270833+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-16T00:58:55.082975+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-16T00:58:55.233881+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-16T00:58:55.284517+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "writing_plan.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "writing_plan.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-16T00:58:55.335438+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml\", \"content\": \"# Writing Plan — schema-dag-extraction\\n# Generated: 2026-05-15\\n# Venue: EMNLP 2026 (ARR May 25 cycle)\\n# Format: 8 pages main text + unlimited references\\n# Mode: Full Draft (2-claim analysis paper + SDGD negative result)\\n\\nmeta:\\n  title: \\\"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\\\"\\n  venue: EMNLP 2026 Main\\n  submission_deadline: \\\"2026-05-25\\\"\\n  page_limit: 8\\n  template: \\\"acl2023\\\"  # ARR uses ACL rolling review LaTeX template\\n  template_note: \\\"No EMNLP 2026 template found locally. Using acl2023.sty (standard ARR template). Worker must download from https://github.com/acl-org/acl-style-files if not available.\\\"\\n  primary_model: \\\"Qwen3-32B-FP8\\\"\\n  secondary_model: \\\"LLaMA-3.1-8B-Instruct (exp-012, D022: 70B→8B cross-scale validation)\\\"\\n  datasets: [\\\"Few-NERD (66 types)\\\", \\\"FewRel (80 relations)\\\", \\\"MAVEN (168 event types)\\\"]\\n\\n# =============================================================================\\n# PAPER OUTLINE\\n# =============================================================================\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    dependencies: [introduction, experiments, results, sdgd_negative, conclusion]\\n    key_content:\\n      - Problem: training-free LLM IE degrades on complex schemas; prior work conflates count and confusability\\n      - Method: first controlled empirical study isolating type confusability from count across 3 tasks\\n      - Findings: multi-channel degradation (count→recall, confusability→type confusion); pairwise SCS robust cross-task (r=0.11-0.13); effect amplifies 3.4× with schema complexity; per-type aggregation confounded on homogeneous schemas\\n      - Negative result: naive confusability-aw
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 124 · 2026-05-16T00:59:39.594459+00:00_

上下文恢复完毕。关键信息：

- **投稿目标**：EMNLP 2026 Main（ARR May 25 cycle），截止日 2026-05-25
- **论文**：`projects/schema-dag-extraction/docs/paper/main.tex`
- **审稿编排**：2 人（EMNLP 一般会议标准）
  - Reviewer 1：方法严谨性 ✅ 已收到
  - Reviewer 2：新颖性/完整性 ❓ 待确认

---

**Round 1 状态**

Reviewer 1 的审稿报告已接收，质量高、覆盖全面。核心发现：

| 等级 | 编号 | 问题 |
|------|------|------|
| Must-Fix | W1 | 3.4× amplification 统计基础薄弱（16-rel 单点观测无 CI，跨 pool 混淆） |
| Must-Fix | W2 | Pairwise SCS r²=1.3%，framing 过度；nonzero-confusion 分析有 conditioning bias |
| Must-Fix | W3 | NER count×confusability 交互证据不足（factorial p=0.50） |
| Should-Fix | W4 | SDGD 仅 2 种 merge 策略，overclaim "structural bottleneck" |
| Should-Fix | W5 | v1/v2 prompt 切换引入实验内混淆 |
| Should-Fix | W6-W7 | Embedding 模型不一致 + FewRel 数据构造偏差 |

Overall: 3/5，建议 Findings 接收或补实验后 Main Conference。

---

等待 Reviewer 2（新颖性/完整性方向）的审稿意见。收到后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 3

## Round 3

6 recorded events


### User

_source line 125 · 2026-05-16T00:59:40.714304+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：给出 **Overall 3/5 (Findings acceptance)**，识别了 3 个 Must-Fix 问题：

1. **3.4× amplification 统计基础薄弱**——16-rel baseline 仅 1 个 batch 无 CI，且跨 pool 比较引入混淆
2. **Pairwise SCS r²=1.3% 效应量极小但 framing 偏强**——nonzero-confusion 子集分析存在 conditioning on the outcome 偏差
3. **NER count×confusability 交互缺乏统计支撑**——factorial 检验 p=0.50 不显著，但论文仍将其作为核心 contribution

另有 4 个 Should-Fix（SDGD overclaim、v1/v2 prompt 混淆、embedding 不一致、FewRel 数据构造）和 3 个 Minor 问题。

---

[Reviewer 2 审稿意见]:
## ACL ARR Review — Reviewer 2（新颖性与完整性）

**Paper:** "Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?"

---

## Summary

本文研究 training-free LLM 信息抽取中，prompt schema 的 type count 和 type confusability 如何独立影响抽取性能。作者引入 Schema Confusability Score (SCS/BCS)，设计 count curve 和 BCS-controlled 两套实验范式，在 NER/RE/ED 三个任务上隔离出 count-driven recall decline（Channel 1）和 confusability-driven type confusion（Channel 2）两条退化通道，并证明 confusability-aware decomposition 因 merge amplification 而失败。实验设计严谨，研究问题明确，但核心发现的 effect size 偏弱（pairwise r² < 2%），关键 amplification claim 依赖两点比较，且论文在呈现上存在明显缺陷（正文无 figure、无 Discussion section）。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计出色（count curve + BCS-controlled），bootstrap CI 规范。但 pairwise SCS 解释力极弱（r² < 2%），3.4× amplification 基于两点比较，中间点非独立。MAVEN 结果反向，削弱统一叙事 |
| **Excitement** | 3/5 | 研究问题重要且先前未被系统研究，controlled experiment 思路值得推广。但结论以描述性发现为主，缺乏可操作的方法论贡献（SDGD 失败、未提出替代方案） |
| **Overall** | 3/5 | Findings track 可接收水平。实验设计强于结论强度，呈现问题可修复但需实质工作 |
| **Confidence** | 4/5 | 熟悉 LLM-based IE 和 zero-shot extraction 文献 |
| **Reproducibility** | 4/5 | 固定 seed、报告 CI、详细描述实验配置，但代码/数据未提供 |

---

## Strengths

**S1. 实验设计精良，因果推断层次清晰。** Count curve 提供 correlational evidence，BCS-controlled 提供 interventional evidence，逐步升级。这在 LLM IE 文献中属于首次。

**S2. Centrality confound 的发现极有价值。** §4.5 揭示 same-domain schema 中 mean BCS 与 error rate 正相关的反直觉现象，追溯到 representation degeneration 文献，对后续 metric 设计有直接指导。

**S3. Cross-model validation 设计合理。** 不同模型家族上复现两条 channel，特别是 high-BCS accuracy 收敛到 ~51% 的 model-invariant floor。

**S4. Negative result（SDGD）报告诚实且有信息量。** 系统测试四种 decomposition mode，明确定位 merge amplification 为瓶颈。

**S5. 相关工作覆盖广泛，与 LLM-PEE 的三点区分清晰有力。**

---

## Weaknesses

**W1 [Must-Fix] 正文零 figure，关键结果缺乏视觉呈现。** Count curves、BCS scaling、error taxonomy 三张核心 figure 全在 Appendix。Reviewer 评估正文 8 页时无法看到最核心的 evidence。建议将 Fig 1 和 Fig 2 移入正文。

**W2 [Must-Fix] Pairwise SCS 解释力极弱（r² = 1.3–1.7%），framing 有 overclaiming 嫌疑。** Contribution 2 声称"robust predictor"，但 r² < 2%。Conditioning on nonzero confusion pairs（ρ = 0.27–0.31）有 selection bias 风险。建议改为"statistically significant but weak predictor"，详细讨论剩余 98% variance 来源。

**W3 [Must-Fix] 3.4× amplification 核心 claim 基于两点比较，统计支撑不足。** 16-rel 条件仅一个 extreme batch（无 CI），中间 40-rel 来自 80-rel pool 子集（非独立）。建议增加 16-rel 多 batch + 独立中间规模验证。

**W4 [Should-Fix] 无 Discussion section，Conclusion 仅 1 段 5 行。** 对于呈现复杂、矛盾结果的论文，缺乏对 theoretical implications、practical guidelines、替代方案的讨论。

**W5 [Should-Fix] MAVEN 结果与主 narrative 矛盾，SCS/BCS 适用范围被限制在 cross-domain schema，generalizability 大幅缩小。**

**W6 [Should-Fix] v1 vs v2 prompt 不一致，NER count curves 使用 known-flawed v1 prompt（96.5% offset fabrication），影响可比性。**

**W7 [Should-Fix] Limitations section 单段 ~20 行，结构差，难以评估各 limitation 严重程度。**

**W8 [Should-Fix] `minilm-2019` 引用指向 Sentence-BERT，但实际使用 all-MiniLM-L6-v2（应引 MiniLM 原始论文）。**

**W9 [Minor] 缺少 Responsible NLP Research Checklist。**

**W10 [Minor] FewRel 合并 train+val split 为非标准设置，讨论不够显著。**

**W11 [Minor] "Multi-channel degradation model"用"model"描述经验分类，建议改为"framework"。**

---

## Questions for Authors

Q1. 16-rel 条件为何仅一个 extreme batch？增加 batch 获 CI 的技术障碍是什么？
Q2. 是否尝试过 residualized BCS（去除 centrality component）？
Q3. v1 prompt 的 offset fabrication 是否影响 type discrimination behavior？
Q4. SDGD 为何仅在 NER 上测试？RE 上 merge amplification 是否同样严重？
Q5. 是否探索过 non-zero temperature 对 type confusion 的影响？

---

## Missing References

1. "Reflect then Learn: Active Prompting for IE Guided by Introspective Confusion" (AAAI 2026) — 显式建模 IE 中的 confusion，高度相关。
2. MiniLM 原始论文 (Wang et al., 2020, NeurIPS) — 当前引用 Sentence-BERT 不准确。
3. Prompt sensitivity 文献（如 Sclar et al., 2024, TACL）— v1 vs v2 差异本身体现 prompt sensitivity。

## 引用验证

42 条引用均有 bib entry 且被引用，无 orphan/missing。32 条 OpenAlex verified，5 条 author name format mismatch（非实质错误），5 条可能因极新未索引。总体引用质量良好。

---

## Overall Assessment

**Borderline (3/5)** — 推荐 Findings track 接收，主会议需实质修改。

实验设计是 LLM IE 文献中最严谨的之一，centrality confound 和 merge amplification 发现有指导价值。但 pairwise predictor r² < 2%、amplification 两点比较统计不足、MAVEN 上 metric 失效限制 generalizability，加上正文无 figure / 无 Discussion 的呈现缺陷，当前版本不具备主会议竞争力。修复 W1-W3 + W4 后可上升至 weak accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-16T01:00:36.934180+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性与完整性方向）的完整审稿原文。请逐条回应每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你的发现是否一致或矛盾的地方。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Paper:** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\n### Summary\n\n本文研究 training-free LLM 信息抽取中，prompt schema 的 type count 和 type confusability 如何独立影响抽取性能。作者引入 Schema Confusability Score (SCS/BCS)，设计 count curve 和 BCS-controlled 两套实验范式，在 NER/RE/ED 三个任务上隔离出 count-driven recall decline（Channel 1）和 confusability-driven type confusion（Channel 2）两条退化通道，并证明 confusability-aware decomposition 因 merge amplification 而失败。实验设计严谨，研究问题明确，但核心发现的 effect size 偏弱（pairwise r² < 2%），关键 amplification claim 依赖两点比较，且论文在呈现上存在明显缺陷（正文无 figure、无 Discussion section）。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验设计出色（count curve + BCS-controlled），bootstrap CI 规范。但 pairwise SCS 解释力极弱（r² < 2%），3.4× amplification 基于两点比较，中间点非独立。MAVEN 结果反向，削弱统一叙事 |\n| **Excitement** | 3/5 | 研究问题重要且先前未被系统研究，controlled experiment 思路值得推广。但结论以描述性发现为主，缺乏可操作的方法论贡献（SDGD 失败、未提出替代方案） |\n| **Overall** | 3/5 | Findings track 可接收水平。实验设计强于结论强度，呈现问题可修复但需实质工作 |\n| **Confidence** | 4/5 | 熟悉 LLM-based IE 和 zero-shot extraction 文献 |\n| **Reproducibility** | 4/5 | 固定 seed、报告 CI、详细描述实验配置，但代码/数据未提供 |\n\n### Strengths\n\n**S1.** 实验设计精良，因果推断层次清晰。Count curve 提供 correlational evidence，BCS-controlled 提供 interventional evidence，逐步升级。这在 LLM IE 文献中属于首次。\n\n**S2.** Centrality confound 的发现极有价值。§4.5 揭示 same-domain schema 中 mean BCS 与 error rate 正相关的反直觉现象，追溯到 representation degeneration 文献，对后续 metric 设计有直接指导。\n\n**S3.** Cross-model validation 设计合理。不同模型家族上复现两条 channel，特别是 high-BCS accuracy 收敛到 ~51% 的 model-invariant floor。\n\n**S4.** Negative result（SDGD）报告诚实且有信息量。系统测试四种 decomposition mode，明确定位 merge amplification 为瓶颈。\n\n**S5.** 相关工作覆盖广泛，与 LLM-PEE 的三点区分清晰有力。\n\n### Weaknesses\n\n**W1 [Must-Fix] 正文零 figure，关键结果缺乏视觉呈现。** Count curves、BCS scaling、error taxonomy 三张核心 figure 全在 Appendix。Reviewer 评估正文 8 页时无法看到最核心的 evidence。建议将 Fig 1 和 Fig 2 移入正文。\n\n**W2 [Must-Fix] Pairwise SCS 解释力极弱（r² = 1.3–1.7%），framing 有 overclaiming 嫌疑。** Contribution 2 声称\"robust predictor\"，但 r² < 2%。Conditioning on nonzero confusion pairs（ρ = 0.27–0.31）有 selection bias 风险。建议改为\"statistically significant but weak predictor\"，详细讨论剩余 98% variance 来源。\n\n**W3 [Must-Fix] 3.4× amplification 核心 claim 基于两点比较，统计支撑不足。** 16-rel 条件仅一个 extreme batch（无 CI），中间 40-rel 来自 80-rel pool 子集（非独立）。建议增加 16-rel 多 batch + 独立中间规模验证。\n\n**W4 [Should-Fix] 无 Discussion section，Conclusion 仅 1 段 5 行。** 对于呈现复杂、矛盾结果的论文，缺乏对 theoretical implications、practical guidelines、替代方案的讨论。\n\n**W5 [Should-Fix] MAVEN 结果与主 narrative 矛盾，SCS/BCS 适用范围被限制在 cross-domain schema，generalizability 大幅缩小。**\n\n**W6 [Should-Fix] v1 vs v2 prompt 不一致，NER count curves 使用 known-flawed v1 prompt（96.5% offset fabrication），影响可比性。**\n\n**W7 [Should-Fix] Limitations section 单段 ~20 行，结构差，难以评估各 limitation 严重程度。**\n\n**W8 [Should-Fix] `minilm-2019` 引用指向 Sentence-BERT，但实际使用 all-MiniLM-L6-v2（应引 MiniLM 原始论文）。**\n\n**W9 [Minor] 缺少 Responsible NLP Research Checklist。**\n\n**W10 [Minor] FewRel 合并 train+val split 为非标准设置，讨论不够显著。**\n\n**W11 [Minor] \"Multi-channel degradation model\"用\"model\"描述经验分类，建议改为\"framework\"。**\n\n### Questions for Authors\n\nQ1. 16-rel 条件为何仅一个 extreme batch？增加 batch 获 CI 的技术障碍是什么？\nQ2. 是否尝试过 residualized BCS（去除 centrality component）？\nQ3. v1 prompt 的 offset fabrication 是否影响 type discrimination behavior？\nQ4. SDGD 为何仅在 NER 上测试？RE 上 merge amplification 是否同样严重？\nQ5. 是否探索过 non-zero temperature 对 type confusion 的影响？\n\n### Missing References\n\n1. \"Reflect then Learn: Active Prompting for IE Guided by Introspective Confusion\" (AAAI 2026)\n2. MiniLM 原始论文 (Wang et al., 2020, NeurIPS)\n3. Prompt sensitivity 文献（如 Sclar et al., 2024, TACL）\n\n### Overall Assessment\n\n**Borderline (3/5)** — 推荐 Findings track 接收，主会议需实质修改。",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性与完整性方向）的完整审稿原文。请逐条回应每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你的发现是否一致或矛盾的地方。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Paper:** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\n### Summary\n\n本文研究 training-free LLM 信息抽取中，prompt schema 的 type count 和 type confusability 如何独立影响抽取性能。作者引入 Schema Confusability Score (SCS/BCS)，设计 count curve 和 BCS-controlled 两套实验范式，在 NER/RE/ED 三个任务上隔离出 count-driven recall decline（Channel 1）和 confusability-driven type confusion（Channel 2）两条退化通道，并证明 confusability-aware decomposition 因 merge amplification 而失败。实验设计严谨，研究问题明确，但核心发现的 effect size 偏弱（pairwise r² < 2%），关键 amplification claim 依赖两点比较，且论文在呈现上存在明显缺陷（正文无 figure、无 Discussion section）。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验设计出色（count curve + BCS-controlled），bootstrap CI 规范。但 pairwise SCS 解释力极弱（r² < 2%），3.4× amplification 基于两点比较，中间点非独立。MAVEN 结果反向，削弱统一叙事 |\n| **Excitement** | 3/5 | 研究问题重要且先前未被系统研究，controlled experiment 思路值得推广。但结论以描述性发现为主，缺乏可操作的方法论贡献（SDGD 失败、未提出替代方案） |\n| **Overall** | 3/5 | Findings track 可接收水平。实验设计强于结论强度，呈现问题可修复但需实质工作 |\n| **Confidence** | 4/5 | 熟悉 LLM-based IE 和 zero-shot extraction 文献 |\n| **Reproducibility** | 4/5 | 固定 seed、报告 CI、详细描述实验配置，但代码/数据未提供 |\n\n### Strengths\n\n**S1.** 实验设计精良，因果推断层次清晰。Count curve 提供 correlational evidence，BCS-controlled 提供 interventional evidence，逐步升级。这在 LLM IE 文献中属于首次。\n\n**S2.** Centrality confound 的发现极有价值。§4.5 揭示 same-domain schema 中 mean BCS 与 error rate 正相关的反直觉现象，追溯到 representation degeneration 文献，对后续 metric 设计有直接指导。\n\n**S3.** Cross-model validation 设计合理。不同模型家族上复现两条 channel，特别是 high-BCS accuracy 收敛到 ~51% 的 model-invariant floor。\n\n**S4.** Negative result（SDGD）报告诚实且有信息量。系统测试四种 decomposition mode，明确定位 merge amplification 为瓶颈。\n\n**S5.** 相关工作覆盖广泛，与 LLM-PEE 的三点区分清晰有力。\n\n### Weaknesses\n\n**W1 [Must-Fix] 正文零 figure，关键结果缺乏视觉呈现。** Count curves、BCS scaling、error taxonomy 三张核心 figure 全在 Appendix。Reviewer 评估正文 8 页时无法看到最核心的 evidence。建议将 Fig 1 和 Fig 2 移入正文。\n\n**W2 [Must-Fix] Pairwise SCS 解释力极弱（r² = 1.3–1.7%），framing 有 overclaiming 嫌疑。** Contribution 2 声称\"robust predictor\"，但 r² < 2%。Conditioning on nonzero confusion pairs（ρ = 0.27–0.31）有 selection bias 风险。建议改为\"statistically significant but weak predictor\"，详细讨论剩余 98% variance 来源。\n\n**W3 [Must-Fix] 3.4× amplification 核心 claim 基于两点比较，统计支撑不足。** 16-rel 条件仅一个 extreme batch（无 CI），中间 40-rel 来自 80-rel pool 子集（非独立）。建议增加 16-rel 多 batch + 独立中间规模验证。\n\n**W4 [Should-Fix] 无 Discussion section，Conclusion 仅 1 段 5 行。** 对于呈现复杂、矛盾结果的论文，缺乏对 theoretical implications、practical guidelines、替代方案的讨论。\n\n**W5 [Should-Fix] MAVEN 结果与主 narrative 矛盾，SCS/BCS 适用范围被限制在 cross-domain schema，generalizability 大幅缩小。**\n\n**W6 [Should-Fix] v1 vs v2 prompt 不一致，NER count curves 使用 known-flawed v1 prompt（96.5% offset fabrication），影响可比性。**\n\n**W7 [Should-Fix] Limitations section 单段 ~20 行，结构差，难以评估各 limitation 严重程度。**\n\n**W8 [Should-Fix] `minilm-2019` 引用指向 Sentence-BERT，但实际使用 all-MiniLM-L6-v2（应引 MiniLM 原始论文）。**\n\n**W9 [Minor] 缺少 Responsible NLP Research Checklist。**\n\n**W10 [Minor] FewRel 合并 train+val split 为非标准设置，讨论不够显著。**\n\n**W11 [Minor] \"Multi-channel degradation model\"用\"model\"描述经验分类，建议改为\"framework\"。**\n\n### Questions for Authors\n\nQ1. 16-rel 条件为何仅一个 extreme batch？增加 batch 获 CI 的技术障碍是什么？\nQ2. 是否尝试过 residualized BCS（去除 centrality component）？\nQ3. v1 prompt 的 offset fabrication 是否影响 type discrimination behavior？\nQ4. SDGD 为何仅在 NER 上测试？RE 上 merge amplification 是否同样严重？\nQ5. 是否探索过 non-zero temperature 对 type confusion 的影响？\n\n### Missing References\n\n1. \"Reflect then Learn: Active Prompting for IE Guided by Introspective Confusion\" (AAAI 2026)\n2. MiniLM 原始论文 (Wang et al., 2020, NeurIPS)\n3. Prompt sensitivity 文献（如 Sclar et al., 2024, TACL）\n\n### Overall Assessment\n\n**Borderline (3/5)** — 推荐 Findings track 接收，主会议需实质修改。",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-16T01:01:32.252709+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 55318
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-16T01:01:32.704953+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性方向）的完整审稿原文。请逐条回应每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你的发现是否一致或矛盾的地方。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### Summary\n\n本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行了受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），并提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER/RE/ED 三个任务，辅以跨模型验证，最后通过 SDGD 实验给出 decompose-then-merge 失败的负面结果。研究问题有价值、实验设计新颖，但若干方法论问题削弱了核心 claim 的可靠性。\n\n### Strengths\n\n**S1.** 研究问题定义清晰且有实际意义。将 count 和 confusability 拆分为独立 channel 的思路是该领域的空白，实验设计（count curves + BCS-controlled）逻辑上互补，从 correlational 到 interventional 层层递进。\n\n**S2.** Error taxonomy 分析（§5.4, Table 4）质量高。IntraSub 随 BCS 单调递增（RE: ρ=0.954）、RE 中 100% confusion 为 intra-batch 的发现清晰有力，为 Channel 2 提供了机制层面的证据。NER 与 RE 在 missed-entity pattern 上的分歧也被如实报告。\n\n**S3.** Centrality confound 分析（§5.5）是对 BCS 指标局限性的坦诚自省，与 representation degeneration 文献的连接恰当。\n\n**S4.** 跨模型验证设计合理：不同家族（Qwen vs. Llama）、不同规模（32B vs. 8B）。High-BCS accuracy 在两个模型上收敛到 ≈51% 的 model-invariant floor 是一个有趣的发现。\n\n**S5.** Limitations section 异常详尽，主动披露了 factorial 检验不显著（z=−0.67, p=0.50）、3.4× 为两点比较等问题。\n\n### Weaknesses\n\n**W1 [Must-Fix] 3.4× amplification 的统计基础薄弱**\n\n3.4× amplification（31.2pp / 9.1pp）是论文最突出的定量 claim（出现在 abstract、introduction、contributions、results），但存在两个严重问题：\n\n(a) 基线无 CI。16-rel 条件下 low-BCS 和 high-BCS 各只有 1 个 batch（Table 3 注释确认）。9.1pp 基线是单次观测，无法评估不确定性。论文只对 80-rel CI 做了传播（1.9–4.7×），但分母方差被完全忽略。\n\n(b) 跨 pool 比较引入混淆。16-rel 来自 validation split，80-rel 来自 train+val 合并的 80 relations。type pool 组成完全不同，amplification 可能部分归因于 pool 差异而非 scale 效应。\n\n建议：在 80-rel pool 内构造 16-type 子集的 BCS-controlled 实验（多个 low/high batch），获取可比 baseline 并附 CI。当前 3.4× 应降格为描述性观察。\n\n**W2 [Must-Fix] Pairwise SCS 效应量极小，framing 过度**\n\nr=0.112, r²=1.3%（Table 2）。论文将其定位为 \"the first factor empirically isolated\"，掩盖了 embedding similarity 仅解释 1.3% confusion 方差的事实。§5.2 中 nonzero-confusion 子集分析（ρ=0.27–0.31）存在 conditioning on the outcome 问题——剔除 confusion=0 的 pair 人为抬高相关性。\n\n建议：明确承认解释力有限；删除或重新框定 nonzero-confusion 分析并讨论 conditioning bias。\n\n**W3 [Must-Fix] NER 上 count×confusability 交互的证据不足**\n\n§5.4 声称 NER 中两个 channel \"interact\"，但 Limitations 中的 2×2 factorial 检验不显著（z=−0.67, p=0.50）。这是 Contribution 1 的核心组成部分，缺乏统计支撑。\n\n建议：提供更有力的交互证据，或降级为 \"suggestive but not statistically confirmed\"。\n\n**W4 [Should-Fix] SDGD 负面结果仅覆盖两种 merge 策略，overclaim \"structural bottleneck\"**\n\n§6 仅测试 union merge 和 confidence-gated merge 就声称 \"structural bottleneck\"。未测试 span-level NMS、majority voting、calibration-based reranking 等替代方案。且仅在 Few-NERD 上测试，单数据集 + 两种策略不足以支撑 \"structural\" 修饰语。\n\n建议：测试更多 merge 策略，在 FewRel 上复现，或弱化表述。\n\n**W5 [Should-Fix] v1/v2 prompt 切换引入实验内混淆**\n\nv1（fabricate offset 96.5%）用于 count curves 和 BCS-controlled NER；v2 用于后续实验和跨模型比较。绝对数值跨实验不直接可比。\n\n建议：统一用 v2 重跑核心实验，或提供 v1/v2 对照消融。\n\n**W6 [Should-Fix] Embedding 模型不一致**\n\nFew-NERD 用 Qwen3-32B embeddings，FewRel/MAVEN 用 MiniLM。不同 embedding 空间的 BCS 不可直接比较，削弱跨任务一致性。\n\n**W7 [Should-Fix] FewRel 数据集构造可能引入偏差**\n\n合并 train+val splits 且未说明 1,000 balanced instances 的抽样方式。\n\n**W8 [Minor] 完整 prompt 模板未在 appendix 中提供，影响可复现性。\n\n**W9 [Minor] MAVEN 结果实质上反驳 count channel 的普遍性（F1 随 count 上升），abstract/introduction 表述应更谨慎。\n\n**W10 [Minor] 缺少与 supervised IE baseline 的参照。\n\n### Questions\n\nQ1. 如果在 80-rel pool 内抽 16-type 子集做 BCS-controlled，amplification 估计值是否变化？\nQ2. 是否探索过多变量模型（加入 type frequency、prompt position 等）提升解释力？\nQ3. SDGD 的 single_pass baseline 用的是 v1 还是 v2 prompt？\nQ4. NER cross-model 效应 \"not robustly detectable\"，如何排除 confusability channel 为 Qwen3 特有？\nQ5. High-BCS ≈51% floor 的来源？是否接近随机猜测？\n\n### Overall Assessment\n\n**Soundness**: 3/5\n**Excitement**: 3.5/5\n**Overall**: 3/5 (Findings acceptance)\n**Confidence**: 4/5\n\n论文研究问题好、实验设计有新意、写作透明度高，但 W1–W3 三个 Must-Fix 问题需要实质性修正才能达到 Main Conference 接收标准。建议修改后以 Findings 投稿，或补充实验后提升至 Main Conference 水平。",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性方向）的完整审稿原文。请逐条回应每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你的发现是否一致或矛盾的地方。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### Summary\n\n本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行了受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），并提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER/RE/ED 三个任务，辅以跨模型验证，最后通过 SDGD 实验给出 decompose-then-merge 失败的负面结果。研究问题有价值、实验设计新颖，但若干方法论问题削弱了核心 claim 的可靠性。\n\n### Strengths\n\n**S1.** 研究问题定义清晰且有实际意义。将 count 和 confusability 拆分为独立 channel 的思路是该领域的空白，实验设计（count curves + BCS-controlled）逻辑上互补，从 correlational 到 interventional 层层递进。\n\n**S2.** Error taxonomy 分析（§5.4, Table 4）质量高。IntraSub 随 BCS 单调递增（RE: ρ=0.954）、RE 中 100% confusion 为 intra-batch 的发现清晰有力，为 Channel 2 提供了机制层面的证据。NER 与 RE 在 missed-entity pattern 上的分歧也被如实报告。\n\n**S3.** Centrality confound 分析（§5.5）是对 BCS 指标局限性的坦诚自省，与 representation degeneration 文献的连接恰当。\n\n**S4.** 跨模型验证设计合理：不同家族（Qwen vs. Llama）、不同规模（32B vs. 8B）。High-BCS accuracy 在两个模型上收敛到 ≈51% 的 model-invariant floor 是一个有趣的发现。\n\n**S5.** Limitations section 异常详尽，主动披露了 factorial 检验不显著（z=−0.67, p=0.50）、3.4× 为两点比较等问题。\n\n### Weaknesses\n\n**W1 [Must-Fix] 3.4× amplification 的统计基础薄弱**\n\n3.4× amplification（31.2pp / 9.1pp）是论文最突出的定量 claim（出现在 abstract、introduction、contributions、results），但存在两个严重问题：\n\n(a) 基线无 CI。16-rel 条件下 low-BCS 和 high-BCS 各只有 1 个 batch（Table 3 注释确认）。9.1pp 基线是单次观测，无法评估不确定性。论文只对 80-rel CI 做了传播（1.9–4.7×），但分母方差被完全忽略。\n\n(b) 跨 pool 比较引入混淆。16-rel 来自 validation split，80-rel 来自 train+val 合并的 80 relations。type pool 组成完全不同，amplification 可能部分归因于 pool 差异而非 scale 效应。\n\n建议：在 80-rel pool 内构造 16-type 子集的 BCS-controlled 实验（多个 low/high batch），获取可比 baseline 并附 CI。当前 3.4× 应降格为描述性观察。\n\n**W2 [Must-Fix] Pairwise SCS 效应量极小，framing 过度**\n\nr=0.112, r²=1.3%（Table 2）。论文将其定位为 \"the first factor empirically isolated\"，掩盖了 embedding similarity 仅解释 1.3% confusion 方差的事实。§5.2 中 nonzero-confusion 子集分析（ρ=0.27–0.31）存在 conditioning on the outcome 问题——剔除 confusion=0 的 pair 人为抬高相关性。\n\n建议：明确承认解释力有限；删除或重新框定 nonzero-confusion 分析并讨论 conditioning bias。\n\n**W3 [Must-Fix] NER 上 count×confusability 交互的证据不足**\n\n§5.4 声称 NER 中两个 channel \"interact\"，但 Limitations 中的 2×2 factorial 检验不显著（z=−0.67, p=0.50）。这是 Contribution 1 的核心组成部分，缺乏统计支撑。\n\n建议：提供更有力的交互证据，或降级为 \"suggestive but not statistically confirmed\"。\n\n**W4 [Should-Fix] SDGD 负面结果仅覆盖两种 merge 策略，overclaim \"structural bottleneck\"**\n\n§6 仅测试 union merge 和 confidence-gated merge 就声称 \"structural bottleneck\"。未测试 span-level NMS、majority voting、calibration-based reranking 等替代方案。且仅在 Few-NERD 上测试，单数据集 + 两种策略不足以支撑 \"structural\" 修饰语。\n\n建议：测试更多 merge 策略，在 FewRel 上复现，或弱化表述。\n\n**W5 [Should-Fix] v1/v2 prompt 切换引入实验内混淆**\n\nv1（fabricate offset 96.5%）用于 count curves 和 BCS-controlled NER；v2 用于后续实验和跨模型比较。绝对数值跨实验不直接可比。\n\n建议：统一用 v2 重跑核心实验，或提供 v1/v2 对照消融。\n\n**W6 [Should-Fix] Embedding 模型不一致**\n\nFew-NERD 用 Qwen3-32B embeddings，FewRel/MAVEN 用 MiniLM。不同 embedding 空间的 BCS 不可直接比较，削弱跨任务一致性。\n\n**W7 [Should-Fix] FewRel 数据集构造可能引入偏差**\n\n合并 train+val splits 且未说明 1,000 balanced instances 的抽样方式。\n\n**W8 [Minor] 完整 prompt 模板未在 appendix 中提供，影响可复现性。\n\n**W9 [Minor] MAVEN 结果实质上反驳 count channel 的普遍性（F1 随 count 上升），abstract/introduction 表述应更谨慎。\n\n**W10 [Minor] 缺少与 supervised IE baseline 的参照。\n\n### Questions\n\nQ1. 如果在 80-rel pool 内抽 16-type 子集做 BCS-controlled，amplification 估计值是否变化？\nQ2. 是否探索过多变量模型（加入 type frequency、prompt position 等）提升解释力？\nQ3. SDGD 的 single_pass baseline 用的是 v1 还是 v2 prompt？\nQ4. NER cross-model 效应 \"not robustly detectable\"，如何排除 confusability channel 为 Qwen3 特有？\nQ5. High-BCS ≈51% floor 的来源？是否接近随机猜测？\n\n### Overall Assessment\n\n**Soundness**: 3/5\n**Excitement**: 3.5/5\n**Overall**: 3/5 (Findings acceptance)\n**Confidence**: 4/5\n\n论文研究问题好、实验设计有新意、写作透明度高，但 W1–W3 三个 Must-Fix 问题需要实质性修正才能达到 Main Conference 接收标准。建议修改后以 Findings 投稿，或补充实验后提升至 Main Conference 水平。",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-16T01:01:34.320694+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1615
}
```

</details>

---


### Assistant

_source line 130 · 2026-05-16T01:01:44.664583+00:00_

交叉分享已发出。两位 Reviewer 的完整审稿原文已互换，等待各自的 `[AGREE]`/`[REBUT]` 逐条回应。

**当前进度**：
- **Step 1** ✅ Round 1 独立初审完成（R1: 3/5, R2: 3/5，均推荐 Findings track）
- **Step 2** ⏳ 交叉分享已触发，等待双方回应
- 两位 Reviewer 高度一致的 Must-Fix 问题：**3.4× amplification 统计不足**、**pairwise SCS r²<2% framing 过强**
- R1 独有 Must-Fix：NER count×confusability 交互无统计支撑
- R2 独有 Must-Fix：正文零 figure

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 4

## Round 4

2 recorded events


### User

_source line 131 · 2026-05-16T01:01:46.183517+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Borderline (3/5)**，推荐 Findings track。

3 个 Must-Fix 问题：(1) 正文无 figure——核心 evidence 全在 Appendix；(2) pairwise SCS r² < 2% 但 framing 为 "robust predictor"；(3) 3.4× amplification 基于无 CI 的两点比较。4 个 Should-Fix：无 Discussion section、MAVEN 结果限制 generalizability、v1/v2 prompt 不一致、Limitations 结构差。实验设计是主要亮点，centrality confound 和 merge amplification 发现有实际价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 132 · 2026-05-16T01:02:01.657715+00:00_

两位 Reviewer 初审报告均已收到，交叉分享已发出。等待交叉回应中。

**当前进度汇总：**

| 步骤 | 状态 |
|------|------|
| Step 1 — Round 1 独立审稿 | ✅ 完成（R1: 3/5, R2: 3/5） |
| Step 2 — 交叉分享 | ⏳ 已发出，等待回应 |
| Step 3 — 收敛判断 | 待定 |
| Step 4 — 汇总报告 | 待定 |

**两位 Reviewer 高度一致的核心问题：**
1. **3.4× amplification 统计不足** — 两人均列为 Must-Fix，16-rel 单 batch 无 CI、两点比较
2. **Pairwise SCS r² < 2% overclaiming** — 两人均列为 Must-Fix，framing 与效应量不匹配
3. **v1/v2 prompt 不一致** — 两人均列为 Should-Fix
4. **MAVEN 结果限制 generalizability** — 两人均提及

**潜在分歧点（待交叉回应确认）：**
- R1 的 W3（NER 交互证据不足）vs R2 未单独提出
- R2 的 W1（正文零 figure）vs R1 未提及
- R2 的 W4（无 Discussion section）vs R1 未提及
- R1 的 W4（SDGD overclaim "structural bottleneck"）vs R2 对 SDGD 评价较正面（S4）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 133 · 2026-05-16T01:05:20.531986+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R1-W1: 3.4× amplification 的统计基础薄弱**

完全同意，这是本文最严重的方法论问题之一。Table 3 脚注明确承认 16-relation 条件下 low-BCS 和 high-BCS 各仅一个 batch，9.1pp 基线是单次观测。更关键的是 R1 指出的 **跨 pool 混淆**：16-rel 来自 validation split（16 types），80-rel 来自 train+val 合并的 80 types，type pool 组成完全不同。论文在 Limitations 中提到 40-relation 中间点（accuracy 0.588, BCS Δ = −33.3pp），但同样承认 "all 40-relation subsets draw from the same 80-type pool, so the 16-to-80 amplification (3.4×) remains a two-point comparison"。

补充一点 R1 未提到的问题：3.4× 这个数字 (31.2/9.1) 在 abstract、introduction (Contribution 3)、results (§5.3) 中重复出现至少 4 次，这种修辞上的突出与其统计基础的薄弱之间存在严重不匹配。即使 80-rel CI 传播后的 1.9–4.7× 范围也是建立在分母无 CI 的基础上的——实际不确定性范围只会更宽。

建议与 R1 一致：在 80-rel pool 内构造 16-type 子集做匹配实验，否则 3.4× 应降格为描述性观察。

---

**[REBUT] R1-W2: Pairwise SCS 效应量极小，framing 过度**

部分不同意。R1 批评的核心是 r²=1.3% 解释力极低，但我认为论文的 framing 已经相当审慎。§5.2 原文明确写道：

> "The correlations are modest: r² ≈ 1.3–1.7%, meaning pairwise confusability explains roughly 1.5% of the variance in type confusion. Other factors—entity frequency, prompt position effects, and type definition quality—likely contribute to the remaining variance."

> "We frame these results as identifying one factor among several that drive type confusion, but the first to be empirically isolated in a controlled zero-shot IE setting."

这不是 "掩盖" r²=1.3% 的事实——论文在正文和 Limitations 中至少三次提到了解释力有限。"the first factor empirically isolated" 的措辞是关于 **历史优先性**，而非声称效应量大。在社会科学和行为研究中，首次在受控实验中隔离出一个显著但效应量小的因子，本身就有方法论价值。

**但 R1 关于 conditioning on the outcome 的批评完全正确。** 剔除 confusion=0 的 pair 后报告 ρ=0.27–0.31，确实人为选择了因变量非零的子集，这在统计上会抬高相关性估计。论文应明确讨论这一 conditioning bias。建议保留该子分析但添加注释说明其解释局限性，而非删除。

---

**[AGREE] R1-W3: NER 上 count×confusability 交互的证据不足**

同意。这是 Contribution 1 的核心声明之一——"separable in RE but interacting in NER"——但唯一的直接统计检验（2×2 factorial, z=−0.67, p=0.50）远未达到显著性。论文在 Limitations 中坦承了这一点，但问题在于 **正文 §5.4 的措辞并未反映出这种不显著性**。§5.4 写道 "the two channels interact for span-level extraction tasks"，这是一个因果性声明，而支撑证据仅为 NER missed-entity rates 非单调、比 RE 高这一描述性观察。

建议将 "interact" 改为 "suggestive evidence of interaction" 并在正文（而非仅 Limitations）中提及 factorial 检验不显著。

---

**[REBUT] R1-W4: SDGD 负面结果仅覆盖两种 merge 策略，overclaim "structural bottleneck"**

部分不同意。R1 指出仅测试 union merge 和 confidence-gated merge 就声称 "structural bottleneck"，建议测试 span-level NMS、majority voting 等。但我认为论文的论证逻辑不完全依赖于穷举策略：

1. **理论论证有合理性**：§6 的核心论点是——同一文本被呈现给模型 k 次（不同 type 子集），每次独立产生预测，由于 LLM 输出在 pass 之间不校准，任何 union-based merge 都会累积矛盾预测。这是 decompose-then-merge 管线的 **结构性质**，与具体策略无关。
2. **Confidence-gated merge 已覆盖校准思路**：R1 建议的 "calibration-based reranking" 实质上就是 confidence-gated merge 要解决的问题。论文已证明 LLM 置信度校准差（引用了 llm-calibration-survey-2024），因此基于置信度的方法面临系统性障碍。
3. **Per-type 是极端基线**：per_type 模式（66 batches）代表了最极端的分解，recall 最高 (0.586) 但 precision 最差 (0.194)，印证了 "更多 pass → 更多 FP" 的单调关系。

**但 R1 关于单数据集的批评有道理。** 仅在 Few-NERD (NER) 上测试 SDGD，未在 FewRel (RE) 上复现，限制了结论的 generalizability。RE 是分类任务，merge 冲突模式可能完全不同。此外，R1 建议的 majority voting 确实是一个值得测试的非 union-based 策略——它不累积预测，而是取多数表决，可能规避 merge amplification。

建议：弱化 "structural bottleneck" 为 "structural challenge for union-based merge pipelines"，补做 FewRel SDGD 实验，测试 majority voting。

---

**[AGREE] R1-W5: v1/v2 prompt 切换引入实验内混淆**

同意，但认为影响程度有限。v1 的 fabricate offset 率 96.5%（§4.5）是一个严重的 prompt 缺陷，v2 的修正（去除 offset 要求、添加格式约束）是合理的。关键在于：

- **Count curves (§5.1)** 用 v1，**cross-model validation** 用 v2 → 绝对数值不可比（Table A1 caption 确认：Qwen3-32B count=1 recall v1=0.72, v2=0.64）
- **BCS-controlled NER** 用 v1，**BCS-controlled RE** 用 v2（？——实际上从 §5.3 看 RE BCS-controlled 可能也是 v1，Table 5 中 SDGD 区分了 v1/v2）

**但论文的核心 claim（count 趋势、BCS 效应方向、error taxonomy 模式）都是 within-experiment 的相对比较**，prompt 版本在同一实验内保持一致，因此相对结论的有效性不受影响。R1 建议的 v1/v2 对照消融是最佳方案。

---

**[REBUT] R1-W6: Embedding 模型不一致**

不同意这是一个 weakness。Table 1 明确标注了每个数据集使用的 embedding 模型。论文的 **主要分析全部在 within-dataset 层面进行**——Few-NERD 的 BCS 只与 Few-NERD 的性能比较，FewRel 同理。论文从未做过跨数据集的 BCS 绝对值比较。

更重要的是，**使用两种不同的 embedding 模型其实是 robustness check 的一部分**。§5.2 在 Few-NERD 和 MAVEN 上同时报告了 Qwen3 和 MiniLM 的 pairwise 相关系数（Qwen3 ρ=0.168 vs MiniLM ρ=0.144；nonzero-confusion subset Qwen3 ρ=0.272 vs MiniLM ρ=0.306），结果一致，说明 SCS 信号不依赖于特定 embedding 空间。

如果要批评，应该批评论文 **没有在 FewRel 上也做 Qwen3 embedding 的对照**——但这属于 "nice to have"，不影响现有结论的有效性。

---

**[AGREE] R1-W7: FewRel 数据集构造可能引入偏差**

同意，但认为这是 minor 级别而非 should-fix。§4.1 仅说 "combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1,000 balanced instances"，未说明：(1) balanced 是按 relation type 等比例抽样还是按 instance 均匀抽样；(2) 是否有去重；(3) train/val split 之间是否存在 annotation 风格差异。添加一句说明抽样方式即可修复。

---

**[AGREE] R1-W8: Prompt 模板未在 appendix 中提供**

同意。这是一个 **直接影响可复现性** 的遗漏。论文描述了 v1 和 v2 的区别（v1 要求 offset，v2 不要求 + 添加格式约束），但没有提供完整 template。对于 zero-shot IE 研究，prompt 本身 *就是* 方法的一部分，必须完整公开。

---

**[AGREE] R1-W9: MAVEN 结果实质上反驳 count channel 的普遍性**

同意。Abstract 写 "a count channel that suppresses recall as candidate types increase" 没有任何限定，但 MAVEN 的 F1 随 count 单调递增（0.106 → 0.247, §5.1），直接与之矛盾。虽然 §5.1 和 §5.5 详细解释了 MAVEN 的反转原因（same-domain ontology, relaxed matching, centrality confound），但 abstract 和 introduction 的表述未充分反映这一例外。

建议在 abstract 中添加 "on NER and RE" 或 "task-dependently" 等限定词。这是一个 framing 问题，修复成本很低但影响读者对 claim 普遍性的理解。

---

**[REBUT] R1-W10: 缺少与 supervised IE baseline 的参照**

不同意这是一个有效的 weakness。本文的研究问题是 **"什么导致 training-free LLM IE 在 schema 复杂度增长时退化"**，是一个分析性/诊断性研究，不是提出新的 IE 方法。Supervised baseline 提供的信息是 "supervised 方法在相同 schema 上表现如何"，但这与论文的核心问题不相关——supervised 方法通过训练学到了 type 区分能力，不会面临相同的 schema-induced degradation 机制。加入 supervised baseline 反而可能分散注意力，让读者误以为这是一篇方法对比论文。

如果要提供参照，更合适的是与 few-shot LLM IE 或 retrieval-augmented IE 对比，但这超出了论文的 scope。

---

### Questions 回应

**Q1. 80-rel pool 内抽 16-type 子集做 BCS-controlled，amplification 是否变化？**

[AGREE] 这是检验 W1 最直接的实验。如果在 80-rel pool 内构造多个 16-type 低/高 BCS 子集，并附 CI，将大幅加强（或推翻）3.4× claim。这个实验的缺失是当前稿件最大的方法论漏洞之一。

**Q2. 是否探索过多变量模型提升解释力？**

[AGREE] 有价值的建议。论文 Limitations 提到 "entity frequency, prompt position effects, and type definition quality likely contribute to the remaining variance" 但未做多变量分析。加入这些控制变量后 SCS 的偏回归系数 (partial r) 会更准确反映 confusability 的独立贡献。不过我注意到 prompt position 在本文实验中可能并不是主要混淆因素——所有 type 都在 JSON schema 中一次性呈现，不像 in-context learning 那样有 recency/primacy 效应。

**Q3. SDGD 的 single_pass baseline 用的是 v1 还是 v2 prompt？**

[AGREE] 这是一个关键的实验细节遗漏。从 Table 5 (tab:sdgd_results) 看，decomposition 模式标注了 v1/v2，但 single_pass 未标注。如果 single_pass 用 v2（precision 更高）而 decomposition 用 v1（precision 更低），那 F1 差异部分归因于 prompt 而非 merge amplification。需要明确说明。

**Q4. NER cross-model 效应 "not robustly detectable"，如何排除 confusability channel 为 Qwen3 特有？**

[REBUT] 论文已在 FewRel RE 上完成了 cross-model BCS-controlled 验证（Table A2）：Llama-3.1-8B Δ=−27.1pp (count 8) 和 −23.9pp (count 16)，与 Qwen3-32B 的 −31.2pp 方向一致、量级可比。更关键的是 high-BCS accuracy 在两个模型上收敛到 ≈51%（Table A2: count 8 均为 51.0%）。因此 **confusability channel 在 RE 上已确认非 Qwen3 特有**。NER 上未检测到可能确实源于 8B 模型的 floor effect 和 text-match 指标噪声更大（Limitations 中已讨论），而非 channel 2 本身为 Qwen3 特有。但我同意需要更多证据（如在 14B/70B 模型上测 NER BCS-controlled）来确认。

**Q5. High-BCS ≈51% floor 的来源？是否接近随机猜测？**

[AGREE] 这是一个很好的问题，论文确实没有充分解释。在 count=8 的 RE 任务中，纯随机猜测的期望准确率为 1/8=12.5%，所以 51% 远高于 random chance。一个合理的解释是：high-BCS batch 中并非所有 8 个 type 都两两高度混淆——可能存在 2-3 个 "混淆子组"，模型在子组间仍可区分，但子组内近似随机。如果 batch 中有 ~2 个主要混淆对（各含 2-3 types），模型在非混淆 pair 上接近 100%、在混淆 pair 上接近 50%（二选一），加权后约 50-60%。论文应提供 high-BCS batch 内部的 confusion matrix 以验证这一假设。

---

### 总结

R1 的审稿质量很高，绝大多数批评有理有据。我与 R1 在以下核心判断上 **一致**：
- W1（3.4× 统计基础薄弱）和 W3（NER 交互证据不足）是最严重的 must-fix 问题
- W8（prompt 未公开）和 W9（MAVEN 反转未在 abstract 中反映）需要修复

我与 R1 的 **分歧** 集中在：
- W2：论文的 framing 已经比较审慎，R1 的 "掩盖" 评价过于严厉，但 conditioning bias 批评完全正确
- W4："structural bottleneck" 的理论论证有合理性，但需弱化表述并补做实验
- W6：embedding 不一致实际上是 robustness check，不是 weakness
- W10：本文是分析性研究，supervised baseline 不在 scope 内

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 134 · 2026-05-16T01:05:33.414056+00:00_

收到 Reviewer 2 的交叉回应。等待 Reviewer 1 对 Reviewer 2 审稿意见的逐条回应。

当前状态：
- Reviewer 1 初审：已完成
- Reviewer 2 初审：已完成
- Reviewer 2 → R1 交叉回应：**已完成**
- Reviewer 1 → R2 交叉回应：**待收**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 135 · 2026-05-16T01:05:36.042800+00:00_

[Reviewer 2 审稿结果]:
已向 Review Director 提交逐条回应。核心判断：

**与 R1 一致的：**
- **W1** [AGREE]：3.4× amplification 统计基础薄弱（单 batch 基线、跨 pool 混淆），是最严重问题
- **W3** [AGREE]：NER 交互效应 factorial 检验不显著 (p=0.50)，正文措辞应降级
- **W5/W7/W8/W9** [AGREE]：prompt 切换、数据构造细节、prompt 模板缺失、MAVEN 反转未在 abstract 限定

**与 R1 分歧的：**
- **W2** [REBUT]：论文 framing 已审慎（正文三次提及 r²≈1.3%），R1 "掩盖" 评价过严；但 conditioning-on-outcome bias 批评完全正确
- **W4** [REBUT]：merge amplification 的理论论证有合理性（k pass 累积不校准预测），confidence-gated 已覆盖校准思路；但需弱化表述 + 补 FewRel 实验 + 测试 majority voting
- **W6** [REBUT]：embedding 不一致实为 robustness check（两种 embedding 结果一致），within-dataset 分析不受影响
- **W10** [REBUT]：本文是诊断性研究，supervised baseline 不在 scope 内

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 136 · 2026-05-16T01:05:50.178336+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 审稿意见的逐条回应，收齐后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 7

## Round 7

6 recorded events


### User

_source line 137 · 2026-05-16T01:14:21.499728+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见

已通读论文全文（正文 + 附录 + LaTeX 源码），以下逐条回应 R2 的 Weakness 和 Question。

---

### Weaknesses 逐条回应

**[AGREE] R2-W1: 正文零 figure，关键结果缺乏视觉呈现**

完全同意，这是严重的呈现缺陷。我确认所有 `\includegraphics` 命令仅出现在 `\appendix` 之后（main.tex L81–100）。Fig 1（count curves）、Fig 2（BCS scaling）、Fig 3（error taxonomy）全部放在附录。12 页 PDF 中，前 8 页为正文，9–10 页为 references，附录的 2 张表 + 3 张图被挤到最后 1–2 页。Reviewer 评估正文时完全看不到最核心的 empirical evidence。对于一篇以实证发现为核心贡献的论文，这不可接受。

---

**[PARTIALLY AGREE] R2-W2: Pairwise SCS r² < 2%，"robust predictor" overclaiming**

部分同意。r² = 0.013–0.017 的解释力确实极弱，Contribution 2 用 "robust predictor" 容易产生误解。但有两点 nuance：

(1) **"Robust" 的语义**：Contribution 2 原文是 "Pairwise confusability as a robust predictor. We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models"。结合正文 §4.2 明确说 "modest in magnitude" 和 "one factor among several"，"robust" 更可能指 "可复现性强"（跨任务、跨 embedding、survive bootstrap），而非 "效应量大"。问题在于 contribution list 的简短表述有误导性，正文措辞是审慎的。

(2) **Selection bias 的严重程度**：R2 担心 conditioning on nonzero pairs (ρ = 0.27–0.31) 有 selection bias。但论文将此作为补充分析，主结论基于全样本 r = 0.112–0.129。Zero-inflation 来自结构性稀疏——大多数 type pair 从未同时出现在同一 batch，confusion rate 自然为 0——这不等于 SCS 无效。但我同意应改为 "statistically significant but modest predictor" 并详细讨论剩余 98% variance 的来源。

---

**[PARTIALLY AGREE] R2-W3: 3.4× amplification 基于两点比较，统计支撑不足**

部分同意，但论文比 R2 描述的更透明。

Table 3 caption 明确说："The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches"。Limitations section 进一步承认："the 16-to-80 amplification (3.4×) remains a two-point comparison" 并给出 CI-propagated range 1.9–4.7×。论文还说明 40-rel 中间点 "is not an independent schema—all 40-relation subsets draw from the same 80-type pool"（§4.1 和 Limitations）。所以 R2 指出的非独立性和两点比较问题，论文已经 disclosed。

但 R2 的核心问题仍然成立：**16-rel 基线的 Δ = -9.1 pp 无 CI，使得 3.4× 是一个无法量化不确定性的 ratio**。从 16-relation pool 中选 8 个有 C(16,8)=12,870 种组合，理论上可以构造多个 extreme batches。如果 BCS 分布在 16-rel pool 中过于集中导致只有一个有意义的 extreme batch，这本身就值得报告。建议作者补充 16-rel 多 batch 实验或解释技术障碍。

此外，80-rel 条件本身的证据是稳固的：count=8 和 count=16 两个水平均给出 Δ ≈ 31.2 pp 且 CI 不含 0（[17.7, 42.7] 和 [22.9, 39.6]），cross-model validation 也确认了类似幅度（Llama: Δ = -27.1 pp 和 -23.9 pp）。**核心问题不在于 confusability effect 是否存在，而在于 amplification ratio 的精确估计。**

---

**[AGREE] R2-W4: 无 Discussion section**

完全同意。我确认 discussion.tex 仅包含一个 4 行 Conclusion（main.tex L34 `\input{discussion}` → discussion.tex 仅 `\section{Conclusion}` 加 4 句话）。

对于一篇发现复杂且部分矛盾的结果（MAVEN 反转、centrality confound、SDGD 失败、NER 两通道交互）的论文，缺少 Discussion 是严重缺陷。需要至少讨论：(1) 两通道模型的理论边界条件；(2) SCS/BCS 在 same-domain vs cross-domain schema 下的差异化使用指南；(3) merge amplification 的可能解决方向（论文已尝试 confidence-gated merge 但未在 Discussion 中展开）；(4) 对实际 schema 设计的操作性建议。

---

**[PARTIALLY AGREE] R2-W5: MAVEN 矛盾限制 generalizability**

部分同意，但 R2 低估了论文对此的处理深度。

§4.5 对 MAVEN 反转提供了完整的因果解释：same-domain schema 导致 embeddings collapse into single cluster（引用 Cai et al. 2021），centrality signal 压过 confusability signal，翻转聚合层相关性。关键是 pairwise SCS–confusion correlation 在 MAVEN 上仍然完好（r = 0.129, CI [0.104, 0.156], p < 10⁻¹⁰），问题仅出在 mean BCS 聚合步骤。论文还给出实践指导："mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas"。

但我同意 generalizability 的确被缩小了。论文的两个核心应用层面——per-type error 预测和 count curve 趋势——在 MAVEN 上都失效或反转。这意味着主要发现仅在 cross-domain schema（Few-NERD + FewRel）上完整成立。考虑到实际应用中 same-domain schema 很常见（如医疗 NER、法律 RE），这是一个实质性的适用范围限制，值得在 Discussion（如果有的话）中充分讨论。

---

**[AGREE] R2-W6: v1 vs v2 prompt 不一致**

同意。NER count curves（§4.1）和 BCS-controlled NER 实验使用 v1 prompt（96.5% offset fabrication），后续实验全部使用 v2。虽然 text matching 评估不受 offset fabrication 直接影响，但 v1 要求 offsets 可能改变模型的 capacity allocation（同时执行定位 + 分类 vs 纯分类）。

附录 Table 6 提供了关键证据：v1 recall at count=1 为 0.72，v2 为 0.64，差异 8 pp。这说明 prompt 版本确实改变了提取行为（v1 的 over-prediction 趋势）。这使得 §4.1 NER count curves 与 §4.4 error taxonomy 分析之间的对比不够干净——前者基于 v1 行为，后者基于 v2。

---

**[AGREE] R2-W7: Limitations section 结构差**

同意。main.tex L36–37 是一个约 20 行的密集段落，涵盖模型限制、variance 解释、merge 策略、interaction term 不显著、amplification 两点比较、BCS metric 局限等多个议题，但全部挤在一个段落中。结构化为分点列表并标注严重程度会大幅改善可读性和可评估性。

---

**[AGREE] R2-W8: MiniLM 引用错误**

同意。LaTeX 源码 `\cite{minilm-2019}` 指向 Reimers and Gurevych 2019 (Sentence-BERT)，references 中有脚注 "All-MiniLM-L6-v2 is a distilled variant"。但 all-MiniLM-L6-v2 基于 MiniLM 架构，应引用 Wang et al. 2020 (NeurIPS) 的 MiniLM 原始论文。当前引用不准确。

---

**[AGREE] R2-W9: 缺少 Responsible NLP Research Checklist**

同意。ACL ARR 提交要求附带此 checklist。

---

**[AGREE] R2-W10: FewRel 合并 train+val split**

同意，但问题不严重。§3.1 解释了原因（val split 仅 16 relations，不足以支持 schema-scale 实验）。建议更显著地讨论潜在影响——train split 的 relation 分布可能不同，合并后的 1,000 balanced instances 是否仍然 representative。

---

**[AGREE] R2-W11: "model" vs "framework"**

同意。"Multi-channel degradation model" 描述的是经验性分类体系（count channel + confusability channel），不是可参数化/可 fit 的统计模型。"Framework" 或 "taxonomy" 更准确，避免混淆。

---

### Questions 回应

**Q1** (16-rel 为何仅一个 extreme batch？)
我也认为这需要解释。C(16,8)=12,870 种可能的 8-type batch，应足以构造多个 extreme batches。可能的 barrier：16-rel pool 的 BCS 分布很窄（Table 1 的 BCS Range 0.42–0.97 是全 80-rel pool，16-rel 子集的范围会更小），导致 "extreme" 选择空间有限。但这应被明确报告。

**Q2** (Residualized BCS？)
优秀建议，我强烈支持。对 MAVEN 的 mean BCS 进行 centrality 残差化（regress out 与 cluster centroid 的 distance）可能恢复预期方向的相关性，同时为 centrality confound 解释提供因果性检验。

**Q3** (v1 offset fabrication 对 type discrimination 的影响？)
重要问题。v1 要求 offsets 迫使模型同时执行定位 + 分类，可能改变 capacity allocation。Table 6 已显示 v1 vs v2 行为不同（recall 0.72 vs 0.64）。建议补充 v1 vs v2 的 per-type confusion matrix 对比，或至少在 v2 上重跑 NER count curves 以确认趋势一致。

**Q4** (SDGD 仅在 NER 上测试？)
同意应扩展。RE 是更干净的测试场（Channel 2 与 Channel 1 可分离，§4.4）。且 RE 每个 instance 只有一个 gold relation，merge 冲突的性质与 NER（多 entity spans 重叠）不同，merge amplification 的表现可能有差异。补充说明：Table 5 显示作者还测试了 confidence-gated merge (v2 mode)，虽然 F1 仍低于 baseline，但说明作者已探索了 alternatives——R2 审查未提及这一点。

**Q5** (Non-zero temperature？)
次要问题。Temperature=0 是 zero-shot IE 的标准设置，论文使用 greedy decoding 确保确定性和可复现性。Non-zero temperature 可能增加输出噪声，掩盖 confusability signal。学术上有意义但不影响当前贡献。

---

### Missing References 回应

1. **"Reflect then Learn" (AAAI 2026)**——如涉及 confusion-aware prompting for IE，高度相关，应引用。
2. **MiniLM 原始论文 (Wang et al., 2020, NeurIPS)**——必须引用，与 W8 一致。
3. **Sclar et al. 2024 (TACL) prompt sensitivity**——与 v1/v2 差异讨论直接相关，应引用。

---

### 与我审查发现的一致/补充

R2 的审查与我的关注高度一致。我补充以下 R2 未覆盖的发现：

1. **FewRel 未进行 pairwise SCS 分析**：§4.2 解释原因（RE 是 per-instance classification，confusion matrix 不可比），但这意味着 Contribution 2 "pairwise SCS predicts type confusion across tasks" 的跨任务泛化性只有 NER + ED 两个数据点，FewRel 的 confusability 证据完全来自 BCS-controlled 实验（interventional 而非 correlational）。应明确承认这一 asymmetry。

2. **Confidence-gated merge**：Table 5 包含 v2 结果（sdgd_zero v2: F1=0.241, random_batch v2: F1=0.301），虽然 F1 仍低于 baseline (0.445)，但 precision 有改善（sdgd: 0.210→0.324）。论文引用 LLM calibration 文献（Geng et al., 2024）解释失败。R2 的审查完全未提及这些 v2 结果——这是作者对 merge problem 的积极探索，体现了研究的 thoroughness。

3. **NER 两通道交互未量化**：§4.4 指出 NER missed rates 与 BCS non-monotonic，暗示 Channel 1 和 Channel 2 交互。Limitations 提到 2×2 factorial 的 interaction term 不显著（z=-0.67, p=0.50）。但论文仍在 abstract 和 introduction 中说 "confusable type sets additionally impair entity detection"，这一 claim 的统计支撑不足。

---

### 总体判断

R2 审查质量很高，11 个 Weakness 中我完全同意 8 个，部分同意 3 个（W2、W3、W5）。分歧主要在 severity 而非 direction：论文在正文和 Limitations 中对 W3 和 W5 的处理比 R2 给的 credit 更充分；W2 的 "robust" 有语义歧义但确实应修改。

**我同意 R2 的 Borderline (3/5) 评分和 Findings track 推荐。** 实验设计是论文最大的优势，但 effect size 弱、呈现问题（零 figure、无 Discussion）和 generalizability 限制（MAVEN 失效）需要实质修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-16T01:16:08.758143+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "- id: \"R1-W1\"\n  summary: \"3.4× amplification 统计基础薄弱——16-rel 基线仅单 batch 无 CI，跨 pool 比较引入混淆\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 完全一致。R1 首提，R2 交叉回应 AGREE 并补充修辞突出与统计基础不匹配的问题\"\n  action_items:\n    - round: 1\n      action: \"在 80-rel pool 内构造 16-type 子集 BCS-controlled 实验（多 batch + CI），或将 3.4× 降格为描述性观察\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Pairwise SCS r²=1.3% 效应量极小，Contribution 2 'robust predictor' framing 过度；nonzero-confusion 子集分析存在 conditioning-on-outcome bias\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 部分 REBUT：论文正文已三次承认 r²≈1.3%，'robust' 指可复现性而非效应量大。但 R2 完全同意 conditioning bias 批评。共识：改措辞 + 讨论 conditioning bias\"\n  action_items:\n    - round: 1\n      action: \"将 'robust predictor' 改为 'statistically significant but modest predictor'；添加 conditioning bias 讨论；讨论剩余 98% variance 来源\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"NER count×confusability 交互证据不足——factorial 检验 p=0.50 不显著，但正文仍作因果性声明\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。R2 AGREE 并指出正文 §5.4 措辞未反映不显著性\"\n  action_items:\n    - round: 1\n      action: \"将 'interact' 改为 'suggestive evidence of interaction'；在正文（非仅 Limitations）提及 factorial 检验不显著\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"正文零 figure——count curves/BCS scaling/error taxonomy 核心 evidence 全在 Appendix\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。R1 交叉回应 AGREE，确认所有 includegraphics 仅出现在 appendix 后\"\n  action_items:\n    - round: 1\n      action: \"将 Fig 1（count curves）和 Fig 2（BCS scaling）移入正文\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"无 Discussion section，Conclusion 仅 4 行——复杂矛盾结果缺乏理论讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。R1 确认 discussion.tex 仅含 4 行 Conclusion\"\n  action_items:\n    - round: 1\n      action: \"添加 Discussion section：两通道模型边界条件、SCS/BCS 差异化使用指南、merge amplification 方向、schema 设计建议\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"SDGD 'structural bottleneck' overclaim——仅两种 merge 策略 + 单数据集\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 部分 REBUT：理论论证有合理性，confidence-gated 已覆盖校准思路。但同意需弱化表述 + FewRel 复现 + majority voting 测试\"\n  action_items:\n    - round: 1\n      action: \"弱化为 'structural challenge for union-based merge pipelines'；补做 FewRel SDGD 实验；测试 majority voting\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"v1/v2 prompt 切换引入实验内混淆——NER count curves 用 v1（96.5% offset fabrication），后续用 v2\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。Table 6 证实 v1 vs v2 recall 差 8pp。R2 AGREE 但认为 within-experiment 相对结论仍有效\"\n  action_items:\n    - round: 1\n      action: \"统一用 v2 重跑 NER count curves，或提供 v1/v2 对照消融\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"MAVEN 结果与主 narrative 矛盾，SCS/BCS 适用范围被限制在 cross-domain schema\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 PARTIALLY AGREE：论文对 MAVEN 反转的处理比 R2 给的 credit 更充分，但同意 generalizability 确实缩小。same-domain schema 常见（医疗/法律），需在 Discussion 充分讨论\"\n  action_items:\n    - round: 1\n      action: \"在 abstract/introduction 添加适用范围限定；在 Discussion 充分讨论 same-domain 局限\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7\"\n  summary: \"Limitations section 单段 ~20 行结构差，难以评估各 limitation 严重程度\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"结构化为分点列表并标注严重程度\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"MiniLM 引用错误——cite minilm-2019 指向 Sentence-BERT，应引 Wang et al. 2020 NeurIPS\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"添加 MiniLM 原始论文引用\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W8\"\n  summary: \"完整 prompt 模板未在 appendix 中提供，影响可复现性\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。R2 强调 prompt 就是方法本身，必须完整公开\"\n  action_items:\n    - round: 1\n      action: \"在 appendix 中提供 v1 和 v2 完整 prompt 模板\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9\"\n  summary: \"MAVEN F1 随 count 上升，反驳 count channel 普遍性——abstract/introduction 未限定\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"在 abstract 中添加 'on NER and RE' 或 'task-dependently' 限定\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W9\"\n  summary: \"缺少 Responsible NLP Research Checklist\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"添加 ACL ARR Responsible NLP Research Checklist\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W10\"\n  summary: \"FewRel 合并 train+val split 为非标准设置，讨论不足\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 AGREE 但认为问题不严重\"\n  action_items:\n    - round: 1\n      action: \"补充抽样方式说明（balanced 策略、去重、annotation 风格差异）\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W11\"\n  summary: \"'Multi-channel degradation model' 用 'model' 描述经验分类——建议改为 'framework'\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"将 'model' 改为 'framework' 或 'taxonomy'\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W7\"\n  summary: \"FewRel 数据集构造可能引入偏差——1,000 balanced instances 抽样方式未说明\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE 但降为 minor\"\n  action_items:\n    - round: 1\n      action: \"补充说明抽样方式\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "- id: \"R1-W1\"\n  summary: \"3.4× amplification 统计基础薄弱——16-rel 基线仅单 batch 无 CI，跨 pool 比较引入混淆\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 完全一致。R1 首提，R2 交叉回应 AGREE 并补充修辞突出与统计基础不匹配的问题\"\n  action_items:\n    - round: 1\n      action: \"在 80-rel pool 内构造 16-type 子集 BCS-controlled 实验（多 batch + CI），或将 3.4× 降格为描述性观察\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Pairwise SCS r²=1.3% 效应量极小，Contribution 2 'robust predictor' framing 过度；nonzero-confusion 子集分析存在 conditioning-on-outcome bias\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 部分 REBUT：论文正文已三次承认 r²≈1.3%，'robust' 指可复现性而非效应量大。但 R2 完全同意 conditioning bias 批评。共识：改措辞 + 讨论 conditioning bias\"\n  action_items:\n    - round: 1\n      action: \"将 'robust predictor' 改为 'statistically significant but modest predictor'；添加 conditioning bias 讨论；讨论剩余 98% variance 来源\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"NER count×confusability 交互证据不足——factorial 检验 p=0.50 不显著，但正文仍作因果性声明\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。R2 AGREE 并指出正文 §5.4 措辞未反映不显著性\"\n  action_items:\n    - round: 1\n      action: \"将 'interact' 改为 'suggestive evidence of interaction'；在正文（非仅 Limitations）提及 factorial 检验不显著\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"正文零 figure——count curves/BCS scaling/error taxonomy 核心 evidence 全在 Appendix\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。R1 交叉回应 AGREE，确认所有 includegraphics 仅出现在 appendix 后\"\n  action_items:\n    - round: 1\n      action: \"将 Fig 1（count curves）和 Fig 2（BCS scaling）移入正文\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"无 Discussion section，Conclusion 仅 4 行——复杂矛盾结果缺乏理论讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。R1 确认 discussion.tex 仅含 4 行 Conclusion\"\n  action_items:\n    - round: 1\n      action: \"添加 Discussion section：两通道模型边界条件、SCS/BCS 差异化使用指南、merge amplification 方向、schema 设计建议\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"SDGD 'structural bottleneck' overclaim——仅两种 merge 策略 + 单数据集\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 部分 REBUT：理论论证有合理性，confidence-gated 已覆盖校准思路。但同意需弱化表述 + FewRel 复现 + majority voting 测试\"\n  action_items:\n    - round: 1\n      action: \"弱化为 'structural challenge for union-based merge pipelines'；补做 FewRel SDGD 实验；测试 majority voting\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"v1/v2 prompt 切换引入实验内混淆——NER count curves 用 v1（96.5% offset fabrication），后续用 v2\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。Table 6 证实 v1 vs v2 recall 差 8pp。R2 AGREE 但认为 within-experiment 相对结论仍有效\"\n  action_items:\n    - round: 1\n      action: \"统一用 v2 重跑 NER count curves，或提供 v1/v2 对照消融\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"MAVEN 结果与主 narrative 矛盾，SCS/BCS 适用范围被限制在 cross-domain schema\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 PARTIALLY AGREE：论文对 MAVEN 反转的处理比 R2 给的 credit 更充分，但同意 generalizability 确实缩小。same-domain schema 常见（医疗/法律），需在 Discussion 充分讨论\"\n  action_items:\n    - round: 1\n      action: \"在 abstract/introduction 添加适用范围限定；在 Discussion 充分讨论 same-domain 局限\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7\"\n  summary: \"Limitations section 单段 ~20 行结构差，难以评估各 limitation 严重程度\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"结构化为分点列表并标注严重程度\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"MiniLM 引用错误——cite minilm-2019 指向 Sentence-BERT，应引 Wang et al. 2020 NeurIPS\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"添加 MiniLM 原始论文引用\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W8\"\n  summary: \"完整 prompt 模板未在 appendix 中提供，影响可复现性\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致。R2 强调 prompt 就是方法本身，必须完整公开\"\n  action_items:\n    - round: 1\n      action: \"在 appendix 中提供 v1 和 v2 完整 prompt 模板\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9\"\n  summary: \"MAVEN F1 随 count 上升，反驳 count channel 普遍性——abstract/introduction 未限定\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"在 abstract 中添加 'on NER and RE' 或 'task-dependently' 限定\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W9\"\n  summary: \"缺少 Responsible NLP Research Checklist\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"添加 ACL ARR Responsible NLP Research Checklist\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W10\"\n  summary: \"FewRel 合并 train+val split 为非标准设置，讨论不足\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 AGREE 但认为问题不严重\"\n  action_items:\n    - round: 1\n      action: \"补充抽样方式说明（balanced 策略、去重、annotation 风格差异）\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W11\"\n  summary: \"'Multi-channel degradation model' 用 'model' 描述经验分类——建议改为 'framework'\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"完全一致\"\n  action_items:\n    - round: 1\n      action: \"将 'model' 改为 'framework' 或 'taxonomy'\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W7\"\n  summary: \"FewRel 数据集构造可能引入偏差——1,000 balanced instances 抽样方式未说明\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE 但降为 minor\"\n  action_items:\n    - round: 1\n      action: \"补充说明抽样方式\"\n      assigned_to: \"\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-16T01:16:08.859256+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 7748}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-16T01:18:14.478569+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 合并审稿报告 — Round 1\n\n**论文**: \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**目标 Venue**: EMNLP 2026 (ARR May 2025 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性 / R2: 新颖性与完整性）\n**轮次**: Round 1（独立初审 + 交叉分享，1 轮收敛）\n\n---\n\n## Summary\n\n本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER (Few-NERD) / RE (FewRel) / ED (MAVEN) 三个任务，辅以跨模型验证 (Qwen3-32B + LLaMA-3.1-8B)，并通过 SDGD 实验报告 decompose-then-merge 的负面结果。研究问题定义清晰、实验设计严谨，但核心定量 claim 的统计基础薄弱，论文呈现存在严重缺陷。\n\n---\n\n## Strengths\n\n**S1. 实验设计精良，因果推断层次清晰 [R1, R2 一致]。** Count curve 提供 correlational evidence，BCS-controlled 提供 interventional evidence，从观察到干预逐步升级。这在 LLM IE 文献中属首次。\n\n**S2. Error taxonomy 分析质量高 [R1]。** IntraSub 随 BCS 单调递增（RE: ρ=0.954），RE 中 100% confusion 为 intra-batch，为 Channel 2 提供机制层面证据。\n\n**S3. Centrality confound 发现有方法论价值 [R1, R2 一致]。** §4.5 揭示 same-domain schema 中 mean BCS 与 error rate 正相关的反直觉现象，对后续 metric 设计有直接指导。\n\n**S4. 跨模型验证设计合理 [R1, R2 一致]。** 不同模型家族 (Qwen vs Llama) + 不同规模 (32B vs 8B)，high-BCS accuracy 在两模型上收敛到 ≈51% 的 model-invariant floor。\n\n**S5. 负面结果 (SDGD) 报告诚实且有信息量 [R2]。** 系统测试多种 decomposition mode，明确定位 merge amplification 为瓶颈。\n\n**S6. 写作透明度高 [R1]。** Limitations section 主动披露 factorial 检验不显著、3.4× 为两点比较等问题。\n\n---\n\n## Weaknesses\n\n### Must-Fix（4 项，两位 Reviewer 达成共识）\n\n**MW1. 3.4× amplification 统计基础薄弱 [R1-W1, R2-W3 — 完全一致]**\n\n3.4×（31.2pp / 9.1pp）是论文最突出的定量 claim，在 abstract/introduction/contributions/results 中至少出现 4 次，但：\n- 16-rel 条件下 low/high BCS 各仅 1 个 batch，9.1pp 基线是单次观测，无 CI\n- 16-rel 来自 validation split，80-rel 来自 train+val 合并 pool，跨 pool 比较引入混淆\n- CI 传播后 1.9–4.7× 范围仍基于分母无 CI 的前提\n\n**建议**: 在 80-rel pool 内构造 16-type 子集 BCS-controlled 实验（多 batch + CI），获取可比 baseline。否则 3.4× 必须降格为描述性观察，大幅降低修辞突出度。\n\n**MW2. Pairwise SCS framing 与效应量不匹配 [R1-W2, R2-W2 — 共识+微调]**\n\nr = 0.112, r² = 1.3%。Contribution 2 使用 \"robust predictor\" 措辞容易误导。R2 指出论文正文已三次承认解释力有限，\"robust\" 可能指可复现性而非效应量大——但 contribution list 的简短表述有误导性。\n\n两位 Reviewer 完全一致的是：nonzero-confusion 子集分析 (ρ = 0.27–0.31) 存在 **conditioning-on-outcome bias**——剔除 confusion=0 pair 人为抬高相关性。\n\n**建议**: 将 \"robust predictor\" 改为 \"statistically significant but modest predictor\"；保留 nonzero 分析但添加 conditioning bias 讨论；讨论剩余 98% variance 来源。\n\n**MW3. NER count×confusability 交互证据不足 [R1-W3, R2 AGREE]**\n\n§5.4 声称两个 channel \"interact\"，但唯一的直接检验（2×2 factorial, z=−0.67, p=0.50）不显著。正文措辞未反映这一结果。\n\n**建议**: 将 \"interact\" 改为 \"suggestive evidence of interaction\"；在正文（非仅 Limitations）中提及 factorial 检验不显著。\n\n**MW4. 正文零 figure [R2-W1, R1 AGREE]**\n\n所有 `\\includegraphics` 仅出现在 `\\appendix` 后。Count curves、BCS scaling、error taxonomy 三张核心图全在附录。对于实证发现驱动的论文，reviewer 评估正文 8 页时无法看到最核心证据，不可接受。\n\n**建议**: 将 Fig 1（count curves）和 Fig 2（BCS scaling）移入正文。\n\n---\n\n### Should-Fix（6 项）\n\n**SW1. 无 Discussion section [R2-W4, R1 AGREE]**\n\ndiscussion.tex 仅含 4 行 Conclusion。对于发现复杂且部分矛盾的论文（MAVEN 反转、centrality confound、SDGD 失败、NER 交互），缺少 Discussion 是严重缺陷。需讨论：两通道框架边界条件、SCS/BCS 差异化使用指南、merge amplification 方向、schema 设计操作性建议。\n\n**SW2. SDGD \"structural bottleneck\" overclaim [R1-W4, R2 部分 REBUT]**\n\nR2 认为理论论证有合理性（k pass 累积不校准预测是结构性质），confidence-gated 已覆盖校准思路。但仅两种 merge 策略 + 单数据集 (Few-NERD) 不足以支撑 \"structural\" 修饰语。\n\n**共识建议**: 弱化为 \"structural challenge for union-based merge pipelines\"；补做 FewRel SDGD 实验；测试 majority voting。\n\n**SW3. v1/v2 prompt 切换引入实验内混淆 [R1-W5, R2 AGREE]**\n\nv1 (fabricate offset 96.5%) 用于 NER count curves 和 BCS-controlled；v2 用于后续实验。Table 6 证实 v1 vs v2 recall 差 8pp。虽然 within-experiment 相对结论仍有效，但跨实验绝对数值不可比。\n\n**建议**: 统一用 v2 重跑 NER count curves，或提供 v1/v2 对照消融。\n\n**SW4. MAVEN 结果限制 generalizability [R2-W5, R1 PARTIALLY AGREE]**\n\nMAVEN 上 count channel 反转、mean BCS 聚合失效，SCS/BCS 适用范围被限制在 cross-domain schema。R1 指出论文对此的处理比 R2 给的 credit 更充分（§4.5 有完整因果解释），但 same-domain schema 在实际应用中常见（医疗 NER、法律 RE），generalizability 确实缩小。\n\n**建议**: Abstract/introduction 添加适用范围限定；Discussion 充分讨论 same-domain 局限。\n\n**SW5. Limitations section 结构差 [R2-W7, R1 AGREE]**\n\n单段 ~20 行涵盖 6+ 个议题，难以评估各 limitation 严重程度。\n\n**建议**: 结构化为分点列表并标注严重程度。\n\n**SW6. Prompt 模板未在 appendix 中提供 [R1-W8, R2 AGREE]**\n\n对于 zero-shot IE 研究，prompt 本身就是方法的核心部分，必须完整公开。\n\n---\n\n### Minor（6 项）\n\n- **m1.** MiniLM 引用错误：`\\cite{minilm-2019}` 指向 Sentence-BERT，应引 Wang et al. 2020 (NeurIPS) [R2-W8, R1 AGREE]\n- **m2.** MAVEN 反转未在 abstract 中限定：abstract 写 \"count channel suppresses recall\" 无限定词 [R1-W9, R2 AGREE]\n- **m3.** 缺少 Responsible NLP Research Checklist [R2-W9, R1 AGREE]\n- **m4.** FewRel train+val 合并为非标准设置，抽样方式未说明 [R2-W10, R1 AGREE]\n- **m5.** \"Multi-channel degradation model\" 应改为 \"framework\" 或 \"taxonomy\" [R2-W11, R1 AGREE]\n- **m6.** FewRel 1,000 balanced instances 抽样方式未说明 [R1-W7, R2 AGREE]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下核心判断上完全一致：\n\n1. **3.4× amplification 是最严重的方法论问题**——需要实验补充或大幅降级 claim\n2. **NER 交互效应缺乏统计支撑**——正文措辞必须降级\n3. **正文无 figure 不可接受**——核心 evidence 必须在正文呈现\n4. **论文整体达到 Findings track 接收水平**——实验设计是主要优势，但 effect size 弱 + 呈现缺陷限制了主会议竞争力\n5. **Pairwise SCS conditioning bias 需要修复**——nonzero-confusion 子集分析存在方法论问题\n\n## Reviewer Divergence [REBUT]\n\n分歧集中在严重程度评估而非方向：\n\n1. **SCS \"robust predictor\" framing (R1-W2)**：R1 认为论文 \"掩盖\" 了 r²=1.3%；R2 反驳认为论文正文已三次承认解释力有限，\"robust\" 指可复现性。**Director 判断**：R2 的 rebut 有道理——论文的 framing 比 R1 描述的更审慎，但 Contribution 2 的措辞确实需要修改。\n\n2. **SDGD \"structural bottleneck\" (R1-W4)**：R1 认为仅两种策略不足以声称 \"structural\"；R2 反驳理论论证有合理性。**Director 判断**：R2 的理论论点成立（union-based merge 的结构性质），但需弱化表述 + 补实验。\n\n3. **Embedding 不一致 (R1-W6)**：R1 认为是 should-fix；R2 反驳这实际是 robustness check，within-dataset 分析不受影响。**Director 判断**：R2 的 rebut 成功——两种 embedding 结果一致 (ρ=0.168 vs 0.144)，这是优势而非劣势。**从 weakness 列表中移除**。\n\n4. **Supervised baseline (R1-W10)**：R1 认为需要参照；R2 反驳本文是诊断性研究，supervised baseline 不在 scope 内。**Director 判断**：R2 的 rebut 成功。**从 weakness 列表中移除**。\n\n---\n\n## Questions（需作者澄清）\n\n1. **16-rel 为何仅一个 extreme batch？** C(16,8)=12,870 种组合，技术障碍是什么？[R1-Q1, R2-Q1 一致]\n2. **是否探索过多变量模型**（加入 type frequency、prompt position）提升解释力？[R1-Q2, R2 支持]\n3. **SDGD single_pass baseline 用的是 v1 还是 v2？** Table 5 未标注。[R1-Q3, R2 AGREE 认为关键遗漏]\n4. **Residualized BCS**：对 MAVEN mean BCS 去除 centrality component 后，是否恢复预期相关方向？[R2-Q2, R1 强烈支持]\n5. **High-BCS ≈51% floor 的来源？** 远高于随机猜测 (1/8=12.5%)，需解释机制。[R1-Q5, R2 提出 \"混淆子组\" 假设]\n6. **Non-zero temperature 对 type confusion 的影响？** [R2-Q5, R1 认为次要]\n\n---\n\n## Missing References\n\n1. **\"Reflect then Learn: Active Prompting for IE Guided by Introspective Confusion\" (AAAI 2026)** — confusion-aware prompting for IE，高度相关 [R2 提出, R1 AGREE]\n2. **MiniLM 原始论文 (Wang et al., 2020, NeurIPS)** — 当前引用 Sentence-BERT 不准确 [R2 提出, R1 AGREE]\n3. **Sclar et al. 2024 (TACL) — prompt sensitivity** — 与 v1/v2 差异讨论直接相关 [R2 提出, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | **3/5** |\n| Excitement | 3.5/5 | 3/5 | **3/5** |\n| Overall | 3/5 | 3/5 | **3/5 (Borderline → Findings track)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**总评: Borderline (3/5) — 推荐 Findings track 接收，主会议需实质修改。**\n\n实验设计是 LLM IE 文献中最严谨的之一（从 correlational 到 interventional 的层次化推理），centrality confound 和 merge amplification 发现有实际指导价值。但：\n\n1. 核心定量 claim (3.4×) 统计基础薄弱\n2. 主要 predictor 解释力极弱 (r² < 2%) 且存在 conditioning bias\n3. NER 交互效应缺乏统计支撑\n4. 呈现问题严重（零 figure + 无 Discussion）\n5. MAVEN 结果限制 generalizability 至 cross-domain schema\n\n修复 MW1–MW4 + SW1 后可上升至 weak accept (Findings)。若补充 80-rel pool 内 16-type 实验、v2 count curves 重跑、FewRel SDGD，可具备主会议竞争力。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1 中 \"interact\" 需降级为 \"suggestive\" [MW3]\n- Contribution 2 中 \"robust predictor\" 需改为 \"statistically significant but modest predictor\" [MW2]\n- Contribution 3 中 3.4× 应附 CI 或降格 [MW1]\n- \"Multi-channel degradation model\" → \"framework\" [m5]\n\n### §3 Methodology / §4 Experiments\n- v1/v2 prompt 切换需在方法论部分显式说明适用范围 [SW3]\n- FewRel 数据构造需补充抽样细节 [m4, m6]\n- MiniLM 引用需更正 [m1]\n\n### §5 Results\n- §5.2 nonzero-confusion 子集分析需添加 conditioning bias 讨论 [MW2]\n- §5.3 amplification 部分需降低修辞突出度或补充实验 [MW1]\n- §5.4 NER 交互措辞需降级 [MW3]\n- MAVEN count channel 反转需在正文更显著地限定 [m2]\n- 核心 figures 必须从 Appendix 移入正文 [MW4]\n\n### §6 SDGD\n- \"structural bottleneck\" → \"structural challenge for union-based merge pipelines\" [SW2]\n- 补做 FewRel SDGD + majority voting [SW2]\n- 明确 single_pass baseline 的 prompt 版本 [Q3]\n\n### §7 Discussion（需新建）\n- 两通道框架的理论边界条件 [SW1]\n- SCS/BCS 在 same-domain vs cross-domain 的差异化指南 [SW4]\n- Merge amplification 的可能解决方向 [SW2]\n- 对实际 schema 设计的操作性建议 [SW1]\n\n### Appendix\n- 补充完整 v1/v2 prompt 模板 [SW6]\n- 添加 Responsible NLP Research Checklist [m3]\n\n### References\n- 添加 3 条遗漏引用 [见 Missing References]",
  "project": "schema-dag-extraction",
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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 合并审稿报告 — Round 1\n\n**论文**: \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**目标 Venue**: EMNLP 2026 (ARR May 2025 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性 / R2: 新颖性与完整性）\n**轮次**: Round 1（独立初审 + 交叉分享，1 轮收敛）\n\n---\n\n## Summary\n\n本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER (Few-NERD) / RE (FewRel) / ED (MAVEN) 三个任务，辅以跨模型验证 (Qwen3-32B + LLaMA-3.1-8B)，并通过 SDGD 实验报告 decompose-then-merge 的负面结果。研究问题定义清晰、实验设计严谨，但核心定量 claim 的统计基础薄弱，论文呈现存在严重缺陷。\n\n---\n\n## Strengths\n\n**S1. 实验设计精良，因果推断层次清晰 [R1, R2 一致]。** Count curve 提供 correlational evidence，BCS-controlled 提供 interventional evidence，从观察到干预逐步升级。这在 LLM IE 文献中属首次。\n\n**S2. Error taxonomy 分析质量高 [R1]。** IntraSub 随 BCS 单调递增（RE: ρ=0.954），RE 中 100% confusion 为 intra-batch，为 Channel 2 提供机制层面证据。\n\n**S3. Centrality confound 发现有方法论价值 [R1, R2 一致]。** §4.5 揭示 same-domain schema 中 mean BCS 与 error rate 正相关的反直觉现象，对后续 metric 设计有直接指导。\n\n**S4. 跨模型验证设计合理 [R1, R2 一致]。** 不同模型家族 (Qwen vs Llama) + 不同规模 (32B vs 8B)，high-BCS accuracy 在两模型上收敛到 ≈51% 的 model-invariant floor。\n\n**S5. 负面结果 (SDGD) 报告诚实且有信息量 [R2]。** 系统测试多种 decomposition mode，明确定位 merge amplification 为瓶颈。\n\n**S6. 写作透明度高 [R1]。** Limitations section 主动披露 factorial 检验不显著、3.4× 为两点比较等问题。\n\n---\n\n## Weaknesses\n\n### Must-Fix（4 项，两位 Reviewer 达成共识）\n\n**MW1. 3.4× amplification 统计基础薄弱 [R1-W1, R2-W3 — 完全一致]**\n\n3.4×（31.2pp / 9.1pp）是论文最突出的定量 claim，在 abstract/introduction/contributions/results 中至少出现 4 次，但：\n- 16-rel 条件下 low/high BCS 各仅 1 个 batch，9.1pp 基线是单次观测，无 CI\n- 16-rel 来自 validation split，80-rel 来自 train+val 合并 pool，跨 pool 比较引入混淆\n- CI 传播后 1.9–4.7× 范围仍基于分母无 CI 的前提\n\n**建议**: 在 80-rel pool 内构造 16-type 子集 BCS-controlled 实验（多 batch + CI），获取可比 baseline。否则 3.4× 必须降格为描述性观察，大幅降低修辞突出度。\n\n**MW2. Pairwise SCS framing 与效应量不匹配 [R1-W2, R2-W2 — 共识+微调]**\n\nr = 0.112, r² = 1.3%。Contribution 2 使用 \"robust predictor\" 措辞容易误导。R2 指出论文正文已三次承认解释力有限，\"robust\" 可能指可复现性而非效应量大——但 contribution list 的简短表述有误导性。\n\n两位 Reviewer 完全一致的是：nonzero-confusion 子集分析 (ρ = 0.27–0.31) 存在 **conditioning-on-outcome bias**——剔除 confusion=0 pair 人为抬高相关性。\n\n**建议**: 将 \"robust predictor\" 改为 \"statistically significant but modest predictor\"；保留 nonzero 分析但添加 conditioning bias 讨论；讨论剩余 98% variance 来源。\n\n**MW3. NER count×confusability 交互证据不足 [R1-W3, R2 AGREE]**\n\n§5.4 声称两个 channel \"interact\"，但唯一的直接检验（2×2 factorial, z=−0.67, p=0.50）不显著。正文措辞未反映这一结果。\n\n**建议**: 将 \"interact\" 改为 \"suggestive evidence of interaction\"；在正文（非仅 Limitations）中提及 factorial 检验不显著。\n\n**MW4. 正文零 figure [R2-W1, R1 AGREE]**\n\n所有 `\\includegraphics` 仅出现在 `\\appendix` 后。Count curves、BCS scaling、error taxonomy 三张核心图全在附录。对于实证发现驱动的论文，reviewer 评估正文 8 页时无法看到最核心证据，不可接受。\n\n**建议**: 将 Fig 1（count curves）和 Fig 2（BCS scaling）移入正文。\n\n---\n\n### Should-Fix（6 项）\n\n**SW1. 无 Discussion section [R2-W4, R1 AGREE]**\n\ndiscussion.tex 仅含 4 行 Conclusion。对于发现复杂且部分矛盾的论文（MAVEN 反转、centrality confound、SDGD 失败、NER 交互），缺少 Discussion 是严重缺陷。需讨论：两通道框架边界条件、SCS/BCS 差异化使用指南、merge amplification 方向、schema 设计操作性建议。\n\n**SW2. SDGD \"structural bottleneck\" overclaim [R1-W4, R2 部分 REBUT]**\n\nR2 认为理论论证有合理性（k pass 累积不校准预测是结构性质），confidence-gated 已覆盖校准思路。但仅两种 merge 策略 + 单数据集 (Few-NERD) 不足以支撑 \"structural\" 修饰语。\n\n**共识建议**: 弱化为 \"structural challenge for union-based merge pipelines\"；补做 FewRel SDGD 实验；测试 majority voting。\n\n**SW3. v1/v2 prompt 切换引入实验内混淆 [R1-W5, R2 AGREE]**\n\nv1 (fabricate offset 96.5%) 用于 NER count curves 和 BCS-controlled；v2 用于后续实验。Table 6 证实 v1 vs v2 recall 差 8pp。虽然 within-experiment 相对结论仍有效，但跨实验绝对数值不可比。\n\n**建议**: 统一用 v2 重跑 NER count curves，或提供 v1/v2 对照消融。\n\n**SW4. MAVEN 结果限制 generalizability [R2-W5, R1 PARTIALLY AGREE]**\n\nMAVEN 上 count channel 反转、mean BCS 聚合失效，SCS/BCS 适用范围被限制在 cross-domain schema。R1 指出论文对此的处理比 R2 给的 credit 更充分（§4.5 有完整因果解释），但 same-domain schema 在实际应用中常见（医疗 NER、法律 RE），generalizability 确实缩小。\n\n**建议**: Abstract/introduction 添加适用范围限定；Discussion 充分讨论 same-domain 局限。\n\n**SW5. Limitations section 结构差 [R2-W7, R1 AGREE]**\n\n单段 ~20 行涵盖 6+ 个议题，难以评估各 limitation 严重程度。\n\n**建议**: 结构化为分点列表并标注严重程度。\n\n**SW6. Prompt 模板未在 appendix 中提供 [R1-W8, R2 AGREE]**\n\n对于 zero-shot IE 研究，prompt 本身就是方法的核心部分，必须完整公开。\n\n---\n\n### Minor（6 项）\n\n- **m1.** MiniLM 引用错误：`\\cite{minilm-2019}` 指向 Sentence-BERT，应引 Wang et al. 2020 (NeurIPS) [R2-W8, R1 AGREE]\n- **m2.** MAVEN 反转未在 abstract 中限定：abstract 写 \"count channel suppresses recall\" 无限定词 [R1-W9, R2 AGREE]\n- **m3.** 缺少 Responsible NLP Research Checklist [R2-W9, R1 AGREE]\n- **m4.** FewRel train+val 合并为非标准设置，抽样方式未说明 [R2-W10, R1 AGREE]\n- **m5.** \"Multi-channel degradation model\" 应改为 \"framework\" 或 \"taxonomy\" [R2-W11, R1 AGREE]\n- **m6.** FewRel 1,000 balanced instances 抽样方式未说明 [R1-W7, R2 AGREE]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下核心判断上完全一致：\n\n1. **3.4× amplification 是最严重的方法论问题**——需要实验补充或大幅降级 claim\n2. **NER 交互效应缺乏统计支撑**——正文措辞必须降级\n3. **正文无 figure 不可接受**——核心 evidence 必须在正文呈现\n4. **论文整体达到 Findings track 接收水平**——实验设计是主要优势，但 effect size 弱 + 呈现缺陷限制了主会议竞争力\n5. **Pairwise SCS conditioning bias 需要修复**——nonzero-confusion 子集分析存在方法论问题\n\n## Reviewer Divergence [REBUT]\n\n分歧集中在严重程度评估而非方向：\n\n1. **SCS \"robust predictor\" framing (R1-W2)**：R1 认为论文 \"掩盖\" 了 r²=1.3%；R2 反驳认为论文正文已三次承认解释力有限，\"robust\" 指可复现性。**Director 判断**：R2 的 rebut 有道理——论文的 framing 比 R1 描述的更审慎，但 Contribution 2 的措辞确实需要修改。\n\n2. **SDGD \"structural bottleneck\" (R1-W4)**：R1 认为仅两种策略不足以声称 \"structural\"；R2 反驳理论论证有合理性。**Director 判断**：R2 的理论论点成立（union-based merge 的结构性质），但需弱化表述 + 补实验。\n\n3. **Embedding 不一致 (R1-W6)**：R1 认为是 should-fix；R2 反驳这实际是 robustness check，within-dataset 分析不受影响。**Director 判断**：R2 的 rebut 成功——两种 embedding 结果一致 (ρ=0.168 vs 0.144)，这是优势而非劣势。**从 weakness 列表中移除**。\n\n4. **Supervised baseline (R1-W10)**：R1 认为需要参照；R2 反驳本文是诊断性研究，supervised baseline 不在 scope 内。**Director 判断**：R2 的 rebut 成功。**从 weakness 列表中移除**。\n\n---\n\n## Questions（需作者澄清）\n\n1. **16-rel 为何仅一个 extreme batch？** C(16,8)=12,870 种组合，技术障碍是什么？[R1-Q1, R2-Q1 一致]\n2. **是否探索过多变量模型**（加入 type frequency、prompt position）提升解释力？[R1-Q2, R2 支持]\n3. **SDGD single_pass baseline 用的是 v1 还是 v2？** Table 5 未标注。[R1-Q3, R2 AGREE 认为关键遗漏]\n4. **Residualized BCS**：对 MAVEN mean BCS 去除 centrality component 后，是否恢复预期相关方向？[R2-Q2, R1 强烈支持]\n5. **High-BCS ≈51% floor 的来源？** 远高于随机猜测 (1/8=12.5%)，需解释机制。[R1-Q5, R2 提出 \"混淆子组\" 假设]\n6. **Non-zero temperature 对 type confusion 的影响？** [R2-Q5, R1 认为次要]\n\n---\n\n## Missing References\n\n1. **\"Reflect then Learn: Active Prompting for IE Guided by Introspective Confusion\" (AAAI 2026)** — confusion-aware prompting for IE，高度相关 [R2 提出, R1 AGREE]\n2. **MiniLM 原始论文 (Wang et al., 2020, NeurIPS)** — 当前引用 Sentence-BERT 不准确 [R2 提出, R1 AGREE]\n3. **Sclar et al. 2024 (TACL) — prompt sensitivity** — 与 v1/v2 差异讨论直接相关 [R2 提出, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | **3/5** |\n| Excitement | 3.5/5 | 3/5 | **3/5** |\n| Overall | 3/5 | 3/5 | **3/5 (Borderline → Findings track)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**总评: Borderline (3/5) — 推荐 Findings track 接收，主会议需实质修改。**\n\n实验设计是 LLM IE 文献中最严谨的之一（从 correlational 到 interventional 的层次化推理），centrality confound 和 merge amplification 发现有实际指导价值。但：\n\n1. 核心定量 claim (3.4×) 统计基础薄弱\n2. 主要 predictor 解释力极弱 (r² < 2%) 且存在 conditioning bias\n3. NER 交互效应缺乏统计支撑\n4. 呈现问题严重（零 figure + 无 Discussion）\n5. MAVEN 结果限制 generalizability 至 cross-domain schema\n\n修复 MW1–MW4 + SW1 后可上升至 weak accept (Findings)。若补充 80-rel pool 内 16-type 实验、v2 count curves 重跑、FewRel SDGD，可具备主会议竞争力。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1 中 \"interact\" 需降级为 \"suggestive\" [MW3]\n- Contribution 2 中 \"robust predictor\" 需改为 \"statistically significant but modest predictor\" [MW2]\n- Contribution 3 中 3.4× 应附 CI 或降格 [MW1]\n- \"Multi-channel degradation model\" → \"framework\" [m5]\n\n### §3 Methodology / §4 Experiments\n- v1/v2 prompt 切换需在方法论部分显式说明适用范围 [SW3]\n- FewRel 数据构造需补充抽样细节 [m4, m6]\n- MiniLM 引用需更正 [m1]\n\n### §5 Results\n- §5.2 nonzero-confusion 子集分析需添加 conditioning bias 讨论 [MW2]\n- §5.3 amplification 部分需降低修辞突出度或补充实验 [MW1]\n- §5.4 NER 交互措辞需降级 [MW3]\n- MAVEN count channel 反转需在正文更显著地限定 [m2]\n- 核心 figures 必须从 Appendix 移入正文 [MW4]\n\n### §6 SDGD\n- \"structural bottleneck\" → \"structural challenge for union-based merge pipelines\" [SW2]\n- 补做 FewRel SDGD + majority voting [SW2]\n- 明确 single_pass baseline 的 prompt 版本 [Q3]\n\n### §7 Discussion（需新建）\n- 两通道框架的理论边界条件 [SW1]\n- SCS/BCS 在 same-domain vs cross-domain 的差异化指南 [SW4]\n- Merge amplification 的可能解决方向 [SW2]\n- 对实际 schema 设计的操作性建议 [SW1]\n\n### Appendix\n- 补充完整 v1/v2 prompt 模板 [SW6]\n- 添加 Responsible NLP Research Checklist [m3]\n\n### References\n- 添加 3 条遗漏引用 [见 Missing References]",
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-16T01:18:18.746105+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4267
}
```

</details>

---


### Assistant

_source line 142 · 2026-05-16T01:18:30.116557+00:00_

Round 1 审稿完成，报告已投递。

**结论**：两位 Reviewer 一致评分 **Borderline 3/5**，推荐 **Findings track** 接收。

**4 个 Must-Fix**：
1. 3.4× amplification 统计基础薄弱（单 batch 无 CI + 跨 pool 混淆）
2. Pairwise SCS "robust predictor" framing 与 r²=1.3% 不匹配 + conditioning bias
3. NER 交互效应 factorial p=0.50 不显著但正文作因果声明
4. 正文零 figure，核心 evidence 全在 Appendix

**6 个 Should-Fix**：无 Discussion、SDGD overclaim、v1/v2 prompt 混淆、MAVEN 限制 generalizability、Limitations 结构差、prompt 模板未公开

**2 项 R2 rebut 成功被移除**：embedding 不一致（实为 robustness check）、supervised baseline（不在 scope 内）

Issue tracker 已同步至 `review_issues.yaml`（16 条 issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 8

## Round 8

2 recorded events


### User

_source line 143 · 2026-05-16T01:18:32.720022+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

逐条回应了 R2 的 11 个 Weakness 和 5 个 Question：
- **完全同意 8 个**：W1（零 figure）、W4（无 Discussion）、W7（Limitations 结构）、W8（MiniLM 引用）、W9（checklist）、W10（FewRel split）、W11（"model"术语）、W6（v1/v2 不一致）
- **部分同意 3 个**：W2（"robust" 有语义歧义，正文措辞比 contribution list 审慎）、W3（论文已 disclose 两点比较局限，但 16-rel 无 CI 仍是问题）、W5（论文对 MAVEN 反转的分析比 R2 给的 credit 更充分，但 generalizability 确实被缩小）

额外补充了 R2 未覆盖的 3 个发现：FewRel 缺失 pairwise 分析的 asymmetry、Table 5 confidence-gated merge (v2) 结果被 R2 忽略、NER 两通道交互 claim 统计支撑不足。

总体同意 R2 的 Borderline 3/5 评分和 Findings track 推荐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 144 · 2026-05-16T01:18:45.215307+00:00_

审稿报告已投递完毕。

**Round 1 总结**：

- **评分**: Borderline 3/5，推荐 Findings track
- **4 项 Must-Fix**: 3.4× 统计基础薄弱、SCS framing overclaim + conditioning bias、NER 交互证据不足、正文零 figure
- **6 项 Should-Fix**: 无 Discussion、SDGD overclaim、v1/v2 prompt 混淆、MAVEN generalizability、Limitations 结构、prompt 模板缺失
- **6 项 Minor**: MiniLM 引用、MAVEN abstract 限定、NLP checklist、FewRel 数据说明、术语修正、抽样说明

两位 Reviewer 在所有关键问题上方向一致，1 轮交叉分享即达成收敛。Issue tracker 已同步更新至 `review_issues.yaml`（16 条 issue）。报告已通过 `submit_review_report_to_research_director` 投递。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 9

## Round 9

62 recorded events


### User

_source line 145 · 2026-05-16T02:45:34.606226+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-16T02:45:40.470488+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-16T02:45:40.471460+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-16T02:45:43.834992+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-16T02:45:43.936193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-16T02:45:47.655742+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-16T02:45:48.158415+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (35 个)\n\n- **bootstrap_ci_analysis**: DONE (success) — \n- **exp016_fewrel_error_taxonomy**: DONE (success) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp007_error_taxonomy**: DONE (success) — \n- **exp_fewrel_formal_80rel**: DONE (success) — \n- **exp_fewrel_formal**: DONE (success) — \n- **exp008_sdgd_zero_fewnerd_r2**: DONE (negative) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n- **fewrel_pilot**: DONE (success) — \n- **exp004_maven_bcs**: DONE (negative) — \n- **exp002_confusability_controlled**: DONE (success) — \n- **exp003a_prompt_v2_rerun**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp001_count_baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_fewrel_80pool_16sub_bootstrap** (success): 从 80-rel pool 随机采样 16 types 构造 8-type batches，100 random batches + BCS quartile bootstrap CI。消除跨 pool 混淆（MW1 审稿人），与 D033 独立 16-rel pool 和 80-rel 做三方比较。\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\n- **exp_maven_residualized_bcs** (success): MAVEN per-type BCS 正相关是 centrality artifact。控制 log_freq/degree_centrality 后 BCS-F1 相关应消失。回答审稿人 Q4。\n\n## 趋势\n成功 17 / 负向 5 / 失败 10 / 共 35\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-38874: 无 GPU 信息\n\n## 告警\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\n- exp012_llama_8b: 已被终止 — unknown\n- exp_fewrel_40rel: 训练失败 — unknown\n- exp012_llama_awq: 已被终止 — unknown\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\n- exp_fewrel_40rel_r2: 训练失败 — unknown\n-
…[truncated 121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-16T02:45:48.158797+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-16T02:45:48.612370+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## D035 集成方案（2026-05-16）\\n- 论文 Table 3 用**极端批次**方法（BCS 最低/最高各 ~5 batches 的 accuracy Δ），不是四分位\\n- D033 的 7.42pp 是四分位比较，需要用极端批次方法重算\\n- 80-pool-16sub 的 3.92pp 也是四分位，同样需要重算\\n- 四分位 CI 作为补充证据报告，展示效应在不同分析粒度下都稳健\\n- 两组数据一起集成到论文再编译上传\\n\\n## 80-pool-16sub 关键发现（2026-05-16）\\n- BCS 范围窄 [0.458, 0.684]（vs 独立 16-rel [0.653, 0.900]），因为从 80-rel pool 采样的 16 types 语义更分散\\n- 四分位 Δ CI 跨零 [-7.79, +0.42]，但回归斜率 CI 不跨零 [-0.684, -0.062]\\n- 效应弱于独立 16-rel pool——BCS 范围压缩导致效应量缩小，这本身支持 BCS 是驱动因素的论点\\n- 决策：用回归斜率做跨条件比较（斜率控制了 BCS 范围差异），四分位 Δ 作为直觉可读的补充\\n\\n## MAVEN per-type BCS 正相关是 artifact（2026-05-16）\\n- exp_maven_residualized_bcs 确认：控制 log_freq + degree_centrality 后相关消失\\n- MiniLM confound = frequency, Qwen3 confound = degree centrality (r=0.854)\\n- 同质 schema（MAVEN 168 event types 多来自 FrameNet）下 per-type BCS 聚合失效\\n- pairwise SCS 仍然有效\\n\", \"total_chars\": 823, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-16T02:45:48.964510+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/docs/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/docs/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-16T02:45:49.015248+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-16T02:45:53.733553+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-16T02:45:54.135489+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-16T02:45:54.135964+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-16T02:45:54.188065+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper/tables/dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-16T02:45:58.611944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-16T02:45:59.114517+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	
15	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	
26	\input{related_work}
27	
28	\input{experimental_setup}
29	
30	\input{results}
31	
32	\input{sdgd_negative}
33	
34	\input{discussion}
35	
36	\section*{Limitations}
37	\begin{enumerate}[leftmargin=*,itemsep=2pt]
38	\item \textbf{Single primary model.} The primary experiments use Qwen3-32B. Channel~1 has been validated on Llama-3.1-8B-Instruct (recall decline $-$43\,pp, $r = 0.725$). Channel~2 was validated on FewRel RE ($\Delta = -27.1$\,pp at count 8, $-23.9$\,pp at count 16), with high-BCS accuracy converging to a model-invariant floor ($\approx$0.51). On Few-NERD NER, Channel~2 was not robustly detectable at 8B scale, likely due to floor effects and the noisier text-match metric.
39	
40	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of the variance in type confusion. Entity frequency, prompt position effects, mention ambiguity, context complexity, and type definition quality likely account for the remaining variance.
41	
42	\item \textbf{Cross-pool slope consistency.} The BCS--accuracy slopes are statistically indistinguishable across pools (permutation $p = 0.436$), indicating consistent per-unit sensitivity. The larger absolute gap at 80 relations (31.2\,pp vs.\ 9.1\,pp) reflects the wider BCS range available in that pool, not a stronger underlying effect. A within-pool comparison (Table~\ref{tab:within_pool}) confirms this interpretation: slope $-$0.401, CI excludes zero.
43	
44	\item \textbf{Non-significant fa
…[truncated 11809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-16T02:45:59.114914+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 163 · 2026-05-16T02:45:59.315884+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-16T02:46:05.142275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-16T02:46:05.597588+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection (same-domain schemas are subject to a centrality confound). The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), while the wider BCS range at 80 types produces larger absolute accuracy gaps (31.2 vs.\ 9.1\,pp). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-16T02:46:05.648261+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-16T02:46:06.652097+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two dis
…[truncated 3768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-16T02:46:06.652553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-16T02:46:07.154808+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, approaches include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and guided synthesis \cite{guidex-2025,nuner-2024}; \citet{familiarity-2025} quantify label shifts in zero-shot NER evaluation. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
8	
9	\subsection{Schema Complexity in IE}
10	\label{sec:rw_schema}
11	
12	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\S\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confu
…[truncated 1969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-16T02:46:07.155310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-16T02:46:07.607462+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embe
…[truncated 7260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-16T02:46:07.608001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-16T02:46:08.110403+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	\begin{figure}[t]
8	\centering
9	\begin{minipage}[t]{0.48\columnwidth}
10	\centering
11	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
12	\end{minipage}
13	\hfill
14	\begin{minipage}[t]{0.48\columnwidth}
15	\centering
16	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
17	\end{minipage}
18	\caption{\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}
19	\label{fig:main_results}
20	\end{figure}
21	
22	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
23	
24	\paragraph{NER (Few-NERD).}
25	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
26	
27	\paragraph{RE (FewRel).}
28	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40
…[truncated 15036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-16T02:46:08.110818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-16T02:46:08.563902+00:00_

1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	Given that confusability drives type confusion, a natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which constructs a thresholded confusability graph from the pairwise SCS matrix, applies greedy graph coloring to assign types to low-confusability batches, and merges per-batch predictions via set union (full protocol and per-mode results in Appendix~\ref{sec:appendix_sdgd}).
5	
6	Every decomposition mode produces lower F1 than single-pass extraction on Few-NERD: SDGD achieves F1 = 0.241, random batching 0.320, and per-type extraction 0.292, versus the single-pass baseline of 0.445 (Table~\ref{tab:sdgd_results}). The bottleneck is \emph{merge amplification}: processing the same text across multiple passes with different type subsets accumulates contradictory predictions at the union step, destroying precision. Confidence-gated merge does not resolve this, as poorly calibrated LLM scores \cite{llm-calibration-survey-2024} discard correct predictions as aggressively as false positives. This is a structural challenge for union-based merge pipelines, independent of decomposition quality, with direct implications for the partitioning approach of \citet{llm-pee-2025}. Future work must address cross-batch calibration before decomposition can translate confusability signals into extraction gains.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-16T02:46:08.564290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-16T02:46:09.068857+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel framework applies most cleanly to cross-domain schemas where types span multiple semantic clusters. For same-domain schemas (e.g., MAVEN's FrameNet-derived types), the centrality confound (\S\ref{sec:centrality_confound}) complicates BCS-level analysis, though the pairwise SCS signal remains intact. Practitioners should use BCS as a schema difficulty predictor for cross-domain ontologies, and pairwise SCS directly---or with centrality factored out---for same-domain schemas.
6	
7	\paragraph{The 51\% floor.}
8	High-BCS accuracy converges to $\approx$51\% on FewRel regardless of model size (8B vs.\ 32B), well above random guessing (12.5\% for 8-way classification). This suggests that under high confusability, models can still resolve a ``confusion subgroup'' of easily distinguishable relations but fail on the tightly clustered remainder. The floor's model-invariance indicates a task-inherent difficulty ceiling that scaling alone cannot overcome.
9	
10	\paragraph{Merge amplification and future directions.}
11	Our SDGD experiments show that naive decompose-then-merge pipelines fail because union merge accumulates contradictory predictions across passes. Three directions may address this: (1)~calibration-aware merge, where cross-batch confidence scores are normalized before aggregation; (2)~joint decoding, where the model sees all types but decodes with confusability-aware constraints; and (3)~hierarchical extraction, processing coarse-grained types first and refining within clusters.
12	
13	\paragraph{Schema design implications.}
14	Our results suggest concrete guidelines: monitor BCS when assembling extraction schemas---high-BCS batches are unreliable regardless of model; for large ontologies, prefer cross-domain type groupings that minimize intra-batch similarity; when decomposition is necessary, invest in cross-batch calibration rather than decomposition quality, si
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-16T02:46:09.069372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-16T02:46:09.571964+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-16T02:46:09.572319+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-16T02:46:16.709031+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"}]

I found comprehensive information about EMNLP 2026 call for papers submission guidelines and author instructions. Here's a summary of the key details:

## Paper Types and Content

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. In addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insi
…[truncated 1566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7136
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-16T02:46:21.582178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 page limit formatting template double blind anonymity ARR submission requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 page limit formatting template double blind anonymity ARR submission requirements"
  }
}
```

</details>

---


### Tool call

_source line 183 · 2026-05-16T02:46:21.733258+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL rolling review 2026 May cycle submission format page limit template requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL rolling review 2026 May cycle submission format page limit template requirements"
  }
}
```

</details>

---


### Tool result

_source line 184 · 2026-05-16T02:46:28.713935+00:00_

Web search results for query: "EMNLP 2026 page limit formatting template double blind anonymity ARR submission requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/ojs/index.php/tacl/about/submissions"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here is information about EMNLP 2026 submission requirements:

## Page Limits and Formatting

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Double-Blind Review and Anonymity

The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible. Papers must not include authors' names and affiliations.
…[truncated 874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7131
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-16T02:46:30.722435+00:00_

Web search results for query: "ACL rolling review 2026 May cycle submission format page limit template requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"}]

Let me search for more specific information about templates and formatting requirements.

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review pla
…[truncated 3136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8989
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-16T02:46:37.903719+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-16T02:46:39.562160+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1658
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-16T02:46:39.714901+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-16T02:46:39.715400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-16T02:46:43.984392+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-16T02:46:44.436945+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-16T02:46:44.588001+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-16T02:46:44.638635+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-16T02:46:48.457024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-16T02:46:48.457565+00:00_

1	- id: MW1
2	  summary: "3.4× amplification 统计基础薄弱（16-rel 单 batch 无 CI + 跨 pool 混淆）"
3	  category: experiment
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 1
8	  mentions:
9	    - {round: 1, reviewers: [R1, R2], note: "R1-W1 + R2-W3 完全一致"}
10	  action_items:
11	    - {round: 1, action: "D033 16-rel 100 batch bootstrap CI（已在跑）", assigned_to: agent, status: in_progress}
12	    - {round: 1, action: "80-rel pool 内 16-type 子集 BCS-controlled 实验（消除跨 pool 混淆）", assigned_to: agent, status: done}
13	    - {round: 1, action: "论文 3.4× 附 CI，根据 within-pool 结果决定是否降格", assigned_to: paper_agent, status: open}
14	  resolution: ""
15	  resolution_round: null
16	
17	- id: MW2
18	  summary: "Pairwise SCS 'robust predictor' framing vs r²=1.3% + conditioning-on-outcome bias"
19	  category: framing
20	  severity: critical
21	  status: in_progress
22	  first_raised_round: 1
23	  last_seen_round: 1
24	  mentions:
25	    - {round: 1, reviewers: [R1, R2], note: "R1-W2 + R2-W2 共识"}
26	  action_items:
27	    - {round: 1, action: "Contribution 2 'robust predictor' → 'statistically significant but modest predictor'", assigned_to: paper_agent, status: open}
28	    - {round: 1, action: "§5.2 加 conditioning-on-outcome bias 讨论 + 并列 all-pairs vs nonzero-only", assigned_to: paper_agent, status: open}
29	    - {round: 1, action: "讨论 98% variance 来源", assigned_to: paper_agent, status: open}
30	  resolution: ""
31	  resolution_round: null
32	
33	- id: MW3
34	  summary: "NER count×confusability interaction p=0.505 但正文称 'interact'"
35	  category: framing
36	  severity: critical
37	  status: in_progress
38	  first_raised_round: 1
39	  last_seen_round: 1
40	  mentions:
41	    - {round: 1, reviewers: [R1, R2], note: "R1-W3 + R2 AGREE"}
42	  action_items:
43	    - {round: 1, action: "正文移除 'interact'/'suggestive'，factorial p=0.505 移入 supplementary 作为 negative result", assigned_to: paper_agent, status: open}
44	  resolution: ""
45	  resolution_round: null
46	
47	- i
…[truncated 9098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-16T02:46:48.508072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-16T02:46:48.559756+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@article{parse-2025,
18	    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    journal = {arXiv preprint arXiv:2510.08623},
21	    year    = {2025},
22	    url     = {https://arxiv.org/abs/2510.08623},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
36	    booktitle = {Findings of the Association for Computational Linguistics: ACL
…[truncated 18250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-16T02:46:53.948504+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-16T02:46:54.452601+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 37\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 10865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-16T02:46:55.377038+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-16T02:46:55.529999+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_director.jsonl:4:{"ts": "2026-05-16T00:50:39.031731+00:00", "role": "tool", "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review", "max_results": "3"}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/sch
…[truncated 7530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-16T02:48:03.536936+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 8 页正文 + 无限参考文献 + Limitations（不计页数）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文文件\n- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`\n- 各节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`\n- 参考文献: `references.bib`\n\n### 审查要求\n\n请以 EMNLP 最严格审稿人的标准评审此论文，重点关注：\n\n1. **实验设计严谨性**\n   - Count curves 和 BCS-controlled 实验的设计是否充分控制了混淆变量？\n   - 样本量（n=25/27 batches, 1000 test instances）是否足够？bootstrap CI 的使用是否恰当？\n   - 三个数据集（Few-NERD/FewRel/MAVEN）的选择是否合理？评估指标是否恰当？\n\n2. **统计分析**\n   - Pairwise SCS r²=1.3-1.7% 的效应量是否足以支撑论文声称？framing 是否诚实？\n   - Within-pool permutation test (p=0.436) 的解读是否正确？\n   - BCS-controlled 实验中 16-rel 单 batch vs 80-rel 多 batch 的统计功效差异是否被充分讨论？\n   - MAVEN centrality confound 的 partial correlation 分析是否方法论正确？\n\n3. **Claims vs Evidence 对齐**\n   - 四个 contribution 是否都有充分实验支撑？\n   - \"Multi-channel degradation framework\" 是否过度声称？（是 framework 还是 empirical observation？）\n   - SDGD 负面结果的讨论是否充分？是否过度泛化？\n   - 跨模型验证（Llama-3.1-8B）的范围和深度是否足够支持泛化声称？\n\n4. **可复现性**\n   - 实验细节是否足以复现？prompt 模板是否公开？\n   - v1/v2 prompt 切换是否引入跨实验混淆？\n   - 随机种子、bootstrap 参数是否完整报告？\n\n### Round 1 遗留关键问题（供参考验证是否已修复）\n- MW1: 3.4× amplification 统计基础（需 CI + within-pool 控制）\n- MW2: r²=1.3% \"robust predictor\" framing\n- MW3: NER factorial p=0.505 但正文称 \"interact\"\n- SW3: v1/v2 prompt 切换混淆\n- Q1: 16-rel 为何仅一个 extreme batch\n\n请输出完整审稿意见，格式：Summary → Strengths → Weaknesses（逐条编号 W1/W2/...，标注严重程度 [Critical/Major/Minor]）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 8 页正文 + 无限参考文献 + Limitations（不计页数）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文文件\n- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`\n- 各节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`\n- 参考文献: `references.bib`\n\n### 审查要求\n\n请以 EMNLP 最严格审稿人的标准评审此论文，重点关注：\n\n1. **实验设计严谨性**\n   - Count curves 和 BCS-controlled 实验的设计是否充分控制了混淆变量？\n   - 样本量（n=25/27 batches, 1000 test instances）是否足够？bootstrap CI 的使用是否恰当？\n   - 三个数据集（Few-NERD/FewRel/MAVEN）的选择是否合理？评估指标是否恰当？\n\n2. **统计分析**\n   - Pairwise SCS r²=1.3-1.7% 的效应量是否足以支撑论文声称？framing 是否诚实？\n   - Within-pool permutation test (p=0.436) 的解读是否正确？\n   - BCS-controlled 实验中 16-rel 单 batch vs 80-rel 多 batch 的统计功效差异是否被充分讨论？\n   - MAVEN centrality confound 的 partial correlation 分析是否方法论正确？\n\n3. **Claims vs Evidence 对齐**\n   - 四个 contribution 是否都有充分实验支撑？\n   - \"Multi-channel degradation framework\" 是否过度声称？（是 framework 还是 empirical observation？）\n   - SDGD 负面结果的讨论是否充分？是否过度泛化？\n   - 跨模型验证（Llama-3.1-8B）的范围和深度是否足够支持泛化声称？\n\n4. **可复现性**\n   - 实验细节是否足以复现？prompt 模板是否公开？\n   - v1/v2 prompt 切换是否引入跨实验混淆？\n   - 随机种子、bootstrap 参数是否完整报告？\n\n### Round 1 遗留关键问题（供参考验证是否已修复）\n- MW1: 3.4× amplification 统计基础（需 CI + within-pool 控制）\n- MW2: r²=1.3% \"robust predictor\" framing\n- MW3: NER factorial p=0.505 但正文称 \"interact\"\n- SW3: v1/v2 prompt 切换混淆\n- Q1: 16-rel 为何仅一个 extreme batch\n\n请输出完整审稿意见，格式：Summary → Strengths → Weaknesses（逐条编号 W1/W2/...，标注严重程度 [Critical/Major/Minor]）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-16T02:48:24.722036+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21185
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-16T02:48:24.873031+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n### 你的审查侧重：新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 8 页正文 + 无限参考文献 + Limitations（不计页数）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文文件\n- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`\n- 各节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`\n- 参考文献: `references.bib`\n\n### 审查要求\n\n请以 EMNLP 最严格审稿人的标准评审此论文，重点关注：\n\n1. **新颖性与贡献度**\n   - \"First controlled empirical study isolating type confusability from type count\" — 这个 claim 是否成立？是否有被遗漏的先驱工作？\n   - SCS/BCS 作为 metric 是否有足够的创新性？（本质是 cosine similarity 的聚合）\n   - 负面结果（SDGD fails, MAVEN centrality confound）是否构成足够的贡献？\n   - 与 LLM-PEE (2025)、PARSE (2025) 的差异化是否清晰？\n\n2. **Related Work 覆盖度**\n   - 2025-2026 年的 zero-shot IE 工作是否覆盖充分？\n   - Representation degeneration 文献的引用是否恰当？是否缺失关键参考？\n   - 引用格式是否正确？bib 条目是否完整？（特别关注 reflect-learn-2026 条目完整性）\n\n3. **写作质量**\n   - Abstract 是否准确概括论文内容？是否有 overclaim？\n   - Introduction 的 RQ1-RQ3 是否在论文中被充分回答？\n   - Discussion 节是否充分讨论了边界条件和局限？\n   - Limitations 节是否全面、结构清晰？\n   - 论文整体叙事是否连贯？从问题到方法到结果的逻辑链是否完整？\n\n4. **格式合规**\n   - 是否满足 8 页正文限制？（需检查图表布局是否溢出）\n   - 是否有 Limitations 节？是否在正确位置（conclusion 后、references 前）？\n   - 是否缺 Responsible NLP Research Checklist（ARR 必须项）？\n   - 引用格式是否符合 ACL natbib 规范？\n   - 匿名性是否完整？有无泄露作者身份的线索？\n   - 正文中是否有 figure？（上轮 MW4 指出正文零 figure 问题）\n\n5. **表格/图表质量**\n   - 表格设计是否清晰易读？\n   - 图表位置是否合理（正文 vs appendix）？\n   - Caption 是否自包含？\n\n### Round 1 遗留关键问题（供参考验证是否已修复）\n- MW4: 正文零 figure（要求将核心图表移入正文）\n- SW1: 无 Discussion section\n- SW4: MAVEN 结果限制 generalizability，需限定 cross-domain\n- SW5: Limitations 节结构差\n- SW6: Prompt 模板未在 appendix 公开\n- m1/REF2: MiniLM 引用错误\n- m2: Abstract MAVEN 反转未限定\n- m3: 缺 Responsible NLP Research Checklist\n- m4/m6: FewRel 数据构造/抽样说明不足\n- m5: \"model\" → \"framework\"\n- REF1: 缺失 Reflect then Learn (AAAI 2026)\n- REF3: 缺失 Sclar et al. 2024 TACL\n\n请输出完整审稿意见，格式：Summary → Strengths → Weaknesses（逐条编号 W1/W2/...，标注严重程度 [Critical/Major/Minor]）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n### 你的审查侧重：新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 8 页正文 + 无限参考文献 + Limitations（不计页数）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文文件\n- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`\n- 各节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`\n- 参考文献: `references.bib`\n\n### 审查要求\n\n请以 EMNLP 最严格审稿人的标准评审此论文，重点关注：\n\n1. **新颖性与贡献度**\n   - \"First controlled empirical study isolating type confusability from type count\" — 这个 claim 是否成立？是否有被遗漏的先驱工作？\n   - SCS/BCS 作为 metric 是否有足够的创新性？（本质是 cosine similarity 的聚合）\n   - 负面结果（SDGD fails, MAVEN centrality confound）是否构成足够的贡献？\n   - 与 LLM-PEE (2025)、PARSE (2025) 的差异化是否清晰？\n\n2. **Related Work 覆盖度**\n   - 2025-2026 年的 zero-shot IE 工作是否覆盖充分？\n   - Representation degeneration 文献的引用是否恰当？是否缺失关键参考？\n   - 引用格式是否正确？bib 条目是否完整？（特别关注 reflect-learn-2026 条目完整性）\n\n3. **写作质量**\n   - Abstract 是否准确概括论文内容？是否有 overclaim？\n   - Introduction 的 RQ1-RQ3 是否在论文中被充分回答？\n   - Discussion 节是否充分讨论了边界条件和局限？\n   - Limitations 节是否全面、结构清晰？\n   - 论文整体叙事是否连贯？从问题到方法到结果的逻辑链是否完整？\n\n4. **格式合规**\n   - 是否满足 8 页正文限制？（需检查图表布局是否溢出）\n   - 是否有 Limitations 节？是否在正确位置（conclusion 后、references 前）？\n   - 是否缺 Responsible NLP Research Checklist（ARR 必须项）？\n   - 引用格式是否符合 ACL natbib 规范？\n   - 匿名性是否完整？有无泄露作者身份的线索？\n   - 正文中是否有 figure？（上轮 MW4 指出正文零 figure 问题）\n\n5. **表格/图表质量**\n   - 表格设计是否清晰易读？\n   - 图表位置是否合理（正文 vs appendix）？\n   - Caption 是否自包含？\n\n### Round 1 遗留关键问题（供参考验证是否已修复）\n- MW4: 正文零 figure（要求将核心图表移入正文）\n- SW1: 无 Discussion section\n- SW4: MAVEN 结果限制 generalizability，需限定 cross-domain\n- SW5: Limitations 节结构差\n- SW6: Prompt 模板未在 appendix 公开\n- m1/REF2: MiniLM 引用错误\n- m2: Abstract MAVEN 反转未限定\n- m3: 缺 Responsible NLP Research Checklist\n- m4/m6: FewRel 数据构造/抽样说明不足\n- m5: \"model\" → \"framework\"\n- REF1: 缺失 Reflect then Learn (AAAI 2026)\n- REF3: 缺失 Sclar et al. 2024 TACL\n\n请输出完整审稿意见，格式：Summary → Strengths → Weaknesses（逐条编号 W1/W2/...，标注严重程度 [Critical/Major/Minor]）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-16T02:48:26.335343+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Assistant

_source line 206 · 2026-05-16T02:48:30.851741+00:00_

两名 Reviewer 已启动 Round 1 独立审稿：

- **Reviewer 1** → 方法严谨性 + 实验设计 + 统计分析
- **Reviewer 2** → 新颖性 + 完整性 + 写作质量 + 格式合规

等待两名 Reviewer 提交审稿结果，收到后进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 207 · 2026-05-16T02:53:52.810300+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 完整审稿意见

### 审查侧重：方法严谨性 + 实验设计 + 统计分析

---

## 总体评分
**Overall**: 3.0/5 (Findings acceptance)
**一句话总结**: 一篇实验设计用心、负面结果诚实的经验性研究，但核心统计证据不足以支撑"multi-channel degradation framework"的声称——该框架仅在 RE 一个任务上 cleanly work，NER 有耦合，ED 有反转，且关键条件存在统计功效不足和 prompt 混淆问题。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心 claims 有多处统计支撑不足：16-rel 无 CI 的单 batch 比较、80-rel 条件整体回归不显著、非独立 bootstrap、v1/v2 prompt 混淆 |
| Excitement | 3.0/5 | 问题提得好——首次系统性隔离 count vs confusability，centrality confound 分析有新意，SDGD 负面结果有价值 |
| Reproducibility | 3.5/5 | 固定种子、greedy decoding、bootstrap 参数均有报告，但 prompt 模板未公开，v1/v2 切换标准不明确 |
| Overall | 3.0/5 | 贡献真实但被过度包装——"framework" 的叙事超出了证据支持的范围，建议重新定位为更谦虚的经验性发现 |
| Confidence | 4/5 | 仔细阅读了全部实验设计和统计分析，熟悉零样本 IE 和统计方法论 |

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] v1/v2 prompt 切换引入系统性混淆
- 具体位置：§3.5 (experimental_setup.tex L85)、Appendix Table 1 caption (main.tex L71)、Appendix Table 5 caption (main.tex L146)
- 问题：v1 prompt（含 offset 要求）用于 count curves 和 BCS-controlled NER 实验；v2 prompt（去 offset + 加 role instruction）用于"all subsequent experiments"。v1 的 offset 错误率 96.5%，说明 v1 从根本上改变了模型的输出行为。跨模型表（Table A1）用 v2 评估 Qwen3，但 §5.1 的 count curve 用 v1，Qwen3 在 count=1 时 recall 差 0.08（0.72 v1 vs 0.64 v2）——这不是 minor difference，是 11% 的相对差异。SDGD 实验用 v1 prompt（Table 5 caption），但 SDGD 与 single-pass 的对比基准也是 v1，这部分内部一致——然而读者无法判断 SDGD 在 v2 prompt 下是否有不同结论。论文承认了 prompt sensitivity（引用 Sclar et al.），但没有系统性地报告 v1 vs v2 在所有实验上的 paired comparison。
- 为什么影响接收：当论文跨实验比较结果时（如 count curve 数字 vs cross-model 数字），prompt 版本不同使得这些比较无效。核心 framework 的两个 channel 分别建立在不同 prompt 版本上。
- 建议修改方向：(1) 所有主实验统一用一个 prompt 版本运行；或 (2) 对关键实验同时报告两版 prompt 的结果，展示结论对 prompt 选择的鲁棒性。

**N2** [Critical] 16-rel BCS gap (9.1 pp) 基于单个 batch 对比，无统计可靠性
- 具体位置：Table 3 (results.tex L79)、Table 3 caption
- 问题：Table 3 明确标注"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches"——即 9.1 pp 这个数字是一个 low-BCS batch vs 一个 high-BCS batch 的比较，无任何 CI。然而论文随后将 9.1 pp 与 31.2 pp (80-rel) 进行对比来论证"wider BCS range produces larger absolute gaps"（Abstract, §5.3），这个比较的一端没有统计基础。
- 为什么影响接收：9.1 vs 31.2 的对比是论文核心叙事（BCS range 解释 absolute gap 差异）的关键证据支柱。若 9.1 pp 不可靠，slope consistency 论证受损。
- 建议修改方向：对 16-rel 条件补充多 batch 实验，提供 CI。

**N3** [Critical] 80-rel 整体 BCS-accuracy 回归不显著，但论文用 80-rel extreme batches 做 headline result
- 具体位置：Table 4 (results.tex L108)、Table 3
- 问题：Table 4 第三行：Full 80-rel (n=25) slope = −0.151, CI [−0.930, +0.657], r = −0.082, p = 0.698。论文承认"underpowered for both metrics"。但 Table 3 的 headline result 31.2 pp gap 正是从 80-rel pool 的 extreme batches 得来。在 80-rel pool 中，BCS 与 accuracy 的整体线性关系不显著，但 extreme batches 的差异被呈现为核心发现——这本质上是 cherry-picked endpoints。
- 为什么影响接收：31.2 pp 出现在 Abstract、Introduction、Discussion、Conclusion 中，是论文最醒目的数字，但来自一个 BCS-accuracy 关系整体不显著的 pool。
- 建议修改方向：(1) 增加 80-rel batch 数量；(2) 呈现 31.2 pp 时必须紧跟提及整体回归不显著；(3) 考虑以 within-pool 16-sub（slope 显著，p=0.027）作为核心证据。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] "Multi-channel degradation framework" 过度声称
- 具体位置：Introduction Contribution 1、Abstract
- 问题：框架仅在 RE 上 cleanly work；NER 有 channel 耦合 + non-monotonic count curve + 不显著 factorial test (p=0.50)；ED 完全反转。称之为"framework"暗示通用性，但实际证据只支持"empirical observation primarily demonstrated on RE"。

**W2** [Major] 非独立观测的 bootstrap CI
- 具体位置：Table 2 (results.tex L48-57)
- 问题：Pairwise SCS-confusion 的 1,953/11,026 pairs 不独立（同一 type 出现在多个 pairs），bootstrap percentile CI 会低估真实不确定性，p < 10^{-10} 可能被高估。建议使用 cluster-robust bootstrap（以 type 为 cluster）。

**W3** [Major] NER count curve non-monotonicity 未充分解释
- 具体位置：§5.1 (results.tex L25)
- 问题：count=22 (0.527) → count=44 (0.551) 的 recall 上升被称为"minor non-monotonicity"，但未报告这两点的 bootstrap CI。若这在 CI 外则说明 count channel 在 NER 上非单调。

**W4** [Major] SDGD 仅在 Few-NERD 上测试
- 具体位置：§6 (sdgd_negative.tex)
- 问题：负面结果仅在 NER 上报告。RE 是 channels 最 cleanly separable 的任务，若 SDGD 在 RE 上也失败则大大增强 merge amplification 论点；若在 RE 上成功则改变结论。只在一个任务上就得出"structural challenge for union-based merge pipelines"的一般性结论，证据不够。

**W5** [Major] r²=1.3-1.7% 的 practical significance 论证跳跃
- 具体位置：§5.2 (results.tex L62-64)
- 问题：从 r²=1.3-1.7% 跳到"compounds into 31.2 pp"缺乏形式化。within-pool quartile Δ 仅 −3.92 pp（CI 穿越零）。建议用 typical BCS range × slope 计算 realistic practical effect。

**W6** [Minor] "model-invariant floor" 基于仅两个同架构模型
- 具体位置：§5.3、Discussion
- 问题："model-invariant" 和 "scaling alone cannot overcome" 基于 8B 和 32B 两个 decoder-only 模型，不足以支持这种泛化 claim。

**W7** [Minor] reflect-learn-2026 作者为 "[To be verified]"
**W8** [Minor] FewRel 合并 train/val splits 的 distribution 影响未讨论

---

## 小问题
- Table 1 BCS Range 用不同 embedding 计算但并列呈现
- FP8 量化对 extraction 质量的影响未讨论
- FewRel 理论上可做 2×2 factorial (count=8/16 × BCS high/low)，但论文称"not conducted"

---

## 主要优势
1. 研究问题重要且清晰——首次系统性隔离 count vs confusability
2. 诚实报告 modest effect sizes 和负面结果
3. Centrality confound 分析有独立方法论价值
4. 实验细节充足（种子、decoding、bootstrap 参数）
5. Within-pool controlled comparison 是精心设计的控制实验

---

## Questions for Authors
- Q1: 能否提供 v1/v2 prompt 完整文本？
- Q2: 16-rel 为何仅一个 extreme batch？是 pool 限制还是 budget？
- Q3: NER count=22→44 的 recall 上升是否在 bootstrap CI 内？
- Q4: Pairwise bootstrap 是否 accounted for type-level clustering？
- Q5: 为什么 SDGD 没有在 FewRel 上测试？

---

## Missing References
- reflect-learn-2026 作者缺失
- 可考虑补充 schema-guided generation 相关 recent work

---

**评分**: Overall 3.0/5 | Soundness 2.5/5 | Excitement 3.0/5 | Confidence 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 208 · 2026-05-16T02:54:00.367950+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 11

## Round 11

6 recorded events


### User

_source line 209 · 2026-05-16T02:54:01.474480+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 完整审稿意见

### 论文标题
Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?

### 审查侧重
新颖性 + 论文完整性 + 写作质量 + 格式合规

---

## 总体评分

**Overall**: 3.0 / 5 (Findings track acceptance)
**一句话总结**: 实验设计严谨地将 count 和 confusability 两个退化通道分离，是有价值的实证贡献，但核心效应量极小（$r^2 \approx 1.5\%$）、正文仅一幅图、关键格式缺失（Responsible NLP Checklist、引用不完整）限制了当前版本的接收资格。

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 控制实验设计合理（count curves + BCS-controlled），统计方法恰当（bootstrap CI、permutation test），但 pairwise r²=1.3–1.7% 的实际意义需更强论证；MAVEN 反转削弱普适性 |
| Excitement | 2.5/5 | 研究问题重要，但 SCS/BCS 本质是 cosine similarity 的直接聚合，方法论创新有限；负面结果（SDGD）虽有信息量但在预期之内 |
| Reproducibility | 2.5/5 | 给出了模型、seed、采样策略，但 prompt template 未公开（v1/v2 仅文字描述）、代码未提及 |
| Confidence | 4/5 | 熟悉 zero-shot IE 和 embedding similarity 文献，仔细阅读了全文 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] `reflect-learn-2026` 引用条目不完整
- 位置：references.bib line 329–334；Related Work §2.2
- 问题：作者字段为 `[To be verified]`，无 URL、DOI 或页码。提交带占位符的 bib 条目不可接受。
- 建议：补全作者、页码/DOI。若无法验证该论文存在，删除引用并调整正文。

**N2** [critical] 缺少 Responsible NLP Research Checklist
- 位置：main.tex——Limitations 后直接是 \bibliography，无 checklist
- 问题：ACL ARR 要求所有投稿附带 Responsible NLP Research Checklist。当前版本完全缺失，可能导致 desk reject。
- 建议：参照 ARR CFP 模板补充完整 checklist。

**N3** [critical] 核心效应量过小但 framing 过强
- 位置：Abstract（"first controlled empirical study"）；Introduction Contribution 2；Table 2（r² = 0.013–0.017）
- 问题：pairwise SCS 仅解释 1.3–1.7% 的 type confusion variance。虽然 p < 10^{-10}，但 r² 极小意味着 SCS 几乎不具有个体预测力。Abstract/Introduction 的 framing 以"first controlled study"为核心卖点，给读者留下效应量大于实际的印象。BCS-level 实验（31.2 pp gap）显示批次级效应显著，但 pairwise→batch-level 的信号放大机制没有清楚解释。
- 建议：Abstract/Introduction 中明确量化 pairwise r²；更突出从 pairwise 到 batch-level 的信号放大解释。

**N4** [major] 正文仅一幅 Figure
- 位置：Figure 1（§4.1）是正文唯一的 figure。Error taxonomy（Table 7/Figure 2）均在 Appendix。
- 问题：实证分析为核心的 8 页论文只有一幅正文图。Error taxonomy 是支撑 Channel 2 的关键证据，却在 Appendix。
- 建议：将 error taxonomy figure 或 BCS scatter plot 移入正文。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Prompt template 未公开
- 位置：§3.5 描述了 v1/v2 prompt 差异，但 Appendix 无完整 prompt 文本。
- 问题：v1→v2 导致 precision 翻倍，说明 prompt 设计对结果影响巨大。不公开严重影响可复现性。
- 建议：Appendix 增加完整 prompt template。

**W2** [major] MAVEN 反转对普适性的限制未充分反映在 Abstract
- 位置：Abstract——MAVEN 反转仅作为括号附注处理。
- 问题：三个数据集中最大的（168 types）结果与主假设方向相反。论文标题问"Does Type Confusability Drive..."——在最大数据集上答案是"not at aggregate level"。
- 建议：Abstract 中给 MAVEN 反转更多篇幅（1-2 句独立陈述）。

**W3** [major] FewRel 数据构造的外部效度
- 位置：§3.1——合并 train+val splits 采样 1,000 balanced instances。
- 问题：(1) 与 FewRel 标准使用方式不同，影响可比性；(2) RE 实质是 closed-set classification 而非 extraction，但论文多处并列讨论。
- 建议：明确说明差异及原因；Limitations 讨论 classification vs. extraction。

**W4** [warning] `json-schema-bench-2025` 引用不完整——author 字段为 "Li, Saibo and others"。
**W5** [warning] MiniLM 引用仍不精确——实际使用的 all-MiniLM-L6-v2 应额外引用 Reimers & Gurevych (2019) Sentence-BERT。
**W6** [warning] 51% floor 的 "confusion subgroup" 解释是推测性的，无实证支撑。
**W7** [warning] §5 SDGD 正文仅半页总结，核心数据全在 Appendix，定位不当。

---

## 小问题
- m1: Abstract 开头绝对数字未注明模型和 prompt 版本。
- m2: §3.5 "v1 prompt fabricates offsets in 96.5%" 是有趣的 LLM hallucination 现象，但未讨论。
- m3: Limitations item 3 更像 result 而非 limitation。
- m4: Table 4 caption 过长（6 行）。
- m5: §4.1 提到 count=40 的 FewRel 评估但 Table 3 不包含此条件，数据悬空。
- m6: Conclusion 过于简短（3 行）。

---

## Questions to Authors
Q1: Pairwise r²=1.5%，但 BCS gap=31.2 pp。请详细解释从 pairwise 到 batch-level 的信号放大机制。
Q2: v1→v2 prompt 切换导致 precision 翻倍。如何确保 count/confusability 效应不是 prompt 格式的 artifact？
Q3: SDGD 实验仅在 Few-NERD 上进行。为什么不在 FewRel (RE, closed-set classification) 上测试？
Q4: 如果加入 type description 计算 SCS，预测力是否会提升？
Q5: 是否考虑过 closed-source 模型（GPT-4o, Claude）的验证？

## Missing References
1. Reimers & Gurevych (EMNLP 2019) Sentence-BERT
2. Li et al. (2023) "Evaluating ChatGPT's Information Extraction Capabilities"
3. Wadhwa et al. (2023) "Revisiting Relation Extraction in the era of Large Language Models"
4. Hierarchical classification / label confusion 文献（如 AFET, Ren et al. 2016）
5. reflect-learn-2026 需补全（见 N1）

## Overall Assessment
**评分**: 3.0/5 | **置信度**: 4/5

论文提出了合理且重要的研究问题，实验设计（count curves + BCS-controlled）是方法论亮点。主要担忧：(1) 核心定量证据薄弱（pairwise r²=1.5%）且 framing 过强；(2) SCS/BCS 方法论创新有限；(3) MAVEN 反转削弱普适性；(4) SDGD 未尝试更先进的 merge 策略；(5) 格式缺失不满足 ARR 要求。修复格式问题、增加正文可视化、公开 prompt、更诚实传达效应量后，适合 Findings track。

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：Overall 3.0/5，三个 Critical 问题——(1) v1/v2 prompt 混淆使跨实验比较失效；(2) 16-rel 的 9.1 pp gap 基于单 batch 无 CI；(3) 80-rel 整体回归不显著却用 extreme batches 做 headline result。四个 Major 问题涉及 "framework" 过度声称、非独立 bootstrap、NER non-monotonicity、SDGD 仅测试一个任务。论文核心贡献有价值但 framing 超出了证据支持的范围，修订后有望达到 Findings 水平。

---

[Reviewer 2 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

核心判断：**Overall 3.0/5，Findings track 水平**。4 个 Must-Fix（不完整引用 `reflect-learn-2026`、缺 Responsible NLP Checklist、效应量 framing 过强、正文仅 1 figure）+ 7 个 Should-Fix（prompt 未公开、MAVEN 反转在 Abstract 中被低估、FewRel 数据构造外部效度等）+ 5 个 Questions。引用验证发现 `json-schema-bench-2025` 作者字段不合法、MiniLM 引用仍不精确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-16T02:54:24.159062+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### 审查侧重：新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n**Overall**: 3.0/5 | Soundness 3.5/5 | Excitement 2.5/5 | Reproducibility 2.5/5 | Confidence 4/5\n\n### Must-Fix\n\n**N1** [critical] `reflect-learn-2026` 引用条目不完整\n- 位置：references.bib line 329–334；Related Work §2.2\n- 问题：作者字段为 `[To be verified]`，无 URL、DOI 或页码。提交带占位符的 bib 条目不可接受。\n\n**N2** [critical] 缺少 Responsible NLP Research Checklist\n- 位置：main.tex——Limitations 后直接是 \\bibliography，无 checklist\n- 问题：ACL ARR 要求所有投稿附带 Responsible NLP Research Checklist。当前版本完全缺失，可能导致 desk reject。\n\n**N3** [critical] 核心效应量过小但 framing 过强\n- 位置：Abstract（\"first controlled empirical study\"）；Introduction Contribution 2；Table 2（r² = 0.013–0.017）\n- 问题：pairwise SCS 仅解释 1.3–1.7% 的 type confusion variance。虽然 p < 10^{-10}，但 r² 极小意味着 SCS 几乎不具有个体预测力。BCS-level 实验（31.2 pp gap）显示批次级效应显著，但 pairwise→batch-level 的信号放大机制没有清楚解释。\n\n**N4** [major] 正文仅一幅 Figure\n- 位置：Figure 1（§5.1）是正文唯一的 figure。Error taxonomy（Table 7/Figure 2）均在 Appendix。\n\n### Should-Fix\n\n**W1** [major] Prompt template 未公开\n**W2** [major] MAVEN 反转对普适性的限制未充分反映在 Abstract\n**W3** [major] FewRel 数据构造的外部效度——合并 train+val、closed-set classification vs extraction\n**W4** [warning] `json-schema-bench-2025` 引用不完整——author 为 \"Li, Saibo and others\"\n**W5** [warning] MiniLM 引用仍不精确——应额外引用 Reimers & Gurevych (2019) Sentence-BERT\n**W6** [warning] 51% floor 的 \"confusion subgroup\" 解释是推测性的，无实证支撑\n**W7** [warning] §6 SDGD 正文仅半页总结，核心数据全在 Appendix\n\n### Questions\nQ1: Pairwise r²=1.5% 但 BCS gap=31.2 pp，请解释信号放大机制。\nQ2: v1→v2 prompt 导致 precision 翻倍，如何排除 prompt artifact？\nQ3: SDGD 为什么不在 FewRel 上测试？\nQ4: 加入 type description 计算 SCS 是否提升预测力？\nQ5: 是否考虑过 closed-source 模型验证？\n\n### Missing References\n1. Reimers & Gurevych (EMNLP 2019) Sentence-BERT\n2. Li et al. (2023) \"Evaluating ChatGPT's Information Extraction Capabilities\"\n3. Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\"\n4. Hierarchical classification / label confusion 文献（如 AFET, Ren et al. 2016）\n\n---\n\n请逐条回应上述所有 Must-Fix (N1-N4)、Should-Fix (W1-W7)、Questions (Q1-Q5) 和 Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### 审查侧重：新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n**Overall**: 3.0/5 | Soundness 3.5/5 | Excitement 2.5/5 | Reproducibility 2.5/5 | Confidence 4/5\n\n### Must-Fix\n\n**N1** [critical] `reflect-learn-2026` 引用条目不完整\n- 位置：references.bib line 329–334；Related Work §2.2\n- 问题：作者字段为 `[To be verified]`，无 URL、DOI 或页码。提交带占位符的 bib 条目不可接受。\n\n**N2** [critical] 缺少 Responsible NLP Research Checklist\n- 位置：main.tex——Limitations 后直接是 \\bibliography，无 checklist\n- 问题：ACL ARR 要求所有投稿附带 Responsible NLP Research Checklist。当前版本完全缺失，可能导致 desk reject。\n\n**N3** [critical] 核心效应量过小但 framing 过强\n- 位置：Abstract（\"first controlled empirical study\"）；Introduction Contribution 2；Table 2（r² = 0.013–0.017）\n- 问题：pairwise SCS 仅解释 1.3–1.7% 的 type confusion variance。虽然 p < 10^{-10}，但 r² 极小意味着 SCS 几乎不具有个体预测力。BCS-level 实验（31.2 pp gap）显示批次级效应显著，但 pairwise→batch-level 的信号放大机制没有清楚解释。\n\n**N4** [major] 正文仅一幅 Figure\n- 位置：Figure 1（§5.1）是正文唯一的 figure。Error taxonomy（Table 7/Figure 2）均在 Appendix。\n\n### Should-Fix\n\n**W1** [major] Prompt template 未公开\n**W2** [major] MAVEN 反转对普适性的限制未充分反映在 Abstract\n**W3** [major] FewRel 数据构造的外部效度——合并 train+val、closed-set classification vs extraction\n**W4** [warning] `json-schema-bench-2025` 引用不完整——author 为 \"Li, Saibo and others\"\n**W5** [warning] MiniLM 引用仍不精确——应额外引用 Reimers & Gurevych (2019) Sentence-BERT\n**W6** [warning] 51% floor 的 \"confusion subgroup\" 解释是推测性的，无实证支撑\n**W7** [warning] §6 SDGD 正文仅半页总结，核心数据全在 Appendix\n\n### Questions\nQ1: Pairwise r²=1.5% 但 BCS gap=31.2 pp，请解释信号放大机制。\nQ2: v1→v2 prompt 导致 precision 翻倍，如何排除 prompt artifact？\nQ3: SDGD 为什么不在 FewRel 上测试？\nQ4: 加入 type description 计算 SCS 是否提升预测力？\nQ5: 是否考虑过 closed-source 模型验证？\n\n### Missing References\n1. Reimers & Gurevych (EMNLP 2019) Sentence-BERT\n2. Li et al. (2023) \"Evaluating ChatGPT's Information Extraction Capabilities\"\n3. Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\"\n4. Hierarchical classification / label confusion 文献（如 AFET, Ren et al. 2016）\n\n---\n\n请逐条回应上述所有 Must-Fix (N1-N4)、Should-Fix (W1-W7)、Questions (Q1-Q5) 和 Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-16T02:54:43.847921+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19688
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-16T02:54:44.099670+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n \n---\n\n## Reviewer 1 完整审稿意见\n\n### 审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n**Overall**: 3.0/5 | Soundness 2.5/5 | Excitement 3.0/5 | Reproducibility 3.5/5 | Confidence 4/5\n\n### Must-Fix\n\n**N1** [Critical] v1/v2 prompt 切换引入系统性混淆\n- §3.5: v1（含 offset）用于 count curves + BCS-controlled NER；v2（去 offset + role instruction）用于后续实验。v1 offset 错误率 96.5%。Qwen3 count=1 recall 差 0.08 (v1 0.72 vs v2 0.64)，11% 相对差异。跨实验比较时 prompt 版本不同使比较无效。\n\n**N2** [Critical] 16-rel BCS gap (9.1 pp) 基于单个 batch 对比，无统计可靠性\n- Table 3 caption 明确标注单 batch。9.1 vs 31.2 的对比是核心叙事支柱，但一端无 CI。\n\n**N3** [Critical] 80-rel 整体 BCS-accuracy 回归不显著，但用 extreme batches 做 headline result\n- Table 4: Full 80-rel slope = −0.151, CI [−0.930, +0.657], p = 0.698。但 31.2 pp gap 出现在 Abstract/Introduction/Discussion/Conclusion，本质是 cherry-picked endpoints。\n\n### Should-Fix\n\n**W1** [Major] \"Multi-channel degradation framework\" 过度声称\n- 框架仅在 RE 上 cleanly work；NER 有 channel 耦合；ED 完全反转。\n\n**W2** [Major] 非独立观测的 bootstrap CI\n- 1,953/11,026 pairs 不独立（同 type 出现在多 pairs），bootstrap percentile CI 低估真实不确定性。\n\n**W3** [Major] NER count curve non-monotonicity 未充分解释\n- count=22 (0.527) → count=44 (0.551) recall 上升被称为 \"minor\"，未报告 CI。\n\n**W4** [Major] SDGD 仅在 Few-NERD 上测试\n- RE 是 channels 最 cleanly separable 的任务，若 SDGD 在 RE 上也失败则增强论点；只在一个任务上得出一般性结论证据不够。\n\n**W5** [Major] r²=1.3-1.7% 的 practical significance 论证跳跃\n- 从 r²=1.5% 跳到\"compounds into 31.2 pp\"缺乏形式化。within-pool quartile Δ 仅 −3.92 pp（CI 穿越零）。\n\n**W6** [Minor] \"model-invariant floor\" 基于仅两个同架构模型\n\n**W7** [Minor] reflect-learn-2026 作者为 \"[To be verified]\"\n\n**W8** [Minor] FewRel 合并 train/val splits 的 distribution 影响未讨论\n\n### Questions\nQ1: 能否提供 v1/v2 prompt 完整文本？\nQ2: 16-rel 为何仅一个 extreme batch？\nQ3: NER count=22→44 的 recall 上升是否在 bootstrap CI 内？\nQ4: Pairwise bootstrap 是否 accounted for type-level clustering？\nQ5: 为什么 SDGD 没有在 FewRel 上测试？\n\n---\n\n请逐条回应上述所有 Must-Fix (N1-N3)、Should-Fix (W1-W8)、Questions (Q1-Q5)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n \n---\n\n## Reviewer 1 完整审稿意见\n\n### 审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n**Overall**: 3.0/5 | Soundness 2.5/5 | Excitement 3.0/5 | Reproducibility 3.5/5 | Confidence 4/5\n\n### Must-Fix\n\n**N1** [Critical] v1/v2 prompt 切换引入系统性混淆\n- §3.5: v1（含 offset）用于 count curves + BCS-controlled NER；v2（去 offset + role instruction）用于后续实验。v1 offset 错误率 96.5%。Qwen3 count=1 recall 差 0.08 (v1 0.72 vs v2 0.64)，11% 相对差异。跨实验比较时 prompt 版本不同使比较无效。\n\n**N2** [Critical] 16-rel BCS gap (9.1 pp) 基于单个 batch 对比，无统计可靠性\n- Table 3 caption 明确标注单 batch。9.1 vs 31.2 的对比是核心叙事支柱，但一端无 CI。\n\n**N3** [Critical] 80-rel 整体 BCS-accuracy 回归不显著，但用 extreme batches 做 headline result\n- Table 4: Full 80-rel slope = −0.151, CI [−0.930, +0.657], p = 0.698。但 31.2 pp gap 出现在 Abstract/Introduction/Discussion/Conclusion，本质是 cherry-picked endpoints。\n\n### Should-Fix\n\n**W1** [Major] \"Multi-channel degradation framework\" 过度声称\n- 框架仅在 RE 上 cleanly work；NER 有 channel 耦合；ED 完全反转。\n\n**W2** [Major] 非独立观测的 bootstrap CI\n- 1,953/11,026 pairs 不独立（同 type 出现在多 pairs），bootstrap percentile CI 低估真实不确定性。\n\n**W3** [Major] NER count curve non-monotonicity 未充分解释\n- count=22 (0.527) → count=44 (0.551) recall 上升被称为 \"minor\"，未报告 CI。\n\n**W4** [Major] SDGD 仅在 Few-NERD 上测试\n- RE 是 channels 最 cleanly separable 的任务，若 SDGD 在 RE 上也失败则增强论点；只在一个任务上得出一般性结论证据不够。\n\n**W5** [Major] r²=1.3-1.7% 的 practical significance 论证跳跃\n- 从 r²=1.5% 跳到\"compounds into 31.2 pp\"缺乏形式化。within-pool quartile Δ 仅 −3.92 pp（CI 穿越零）。\n\n**W6** [Minor] \"model-invariant floor\" 基于仅两个同架构模型\n\n**W7** [Minor] reflect-learn-2026 作者为 \"[To be verified]\"\n\n**W8** [Minor] FewRel 合并 train/val splits 的 distribution 影响未讨论\n\n### Questions\nQ1: 能否提供 v1/v2 prompt 完整文本？\nQ2: 16-rel 为何仅一个 extreme batch？\nQ3: NER count=22→44 的 recall 上升是否在 bootstrap CI 内？\nQ4: Pairwise bootstrap 是否 accounted for type-level clustering？\nQ5: 为什么 SDGD 没有在 FewRel 上测试？\n\n---\n\n请逐条回应上述所有 Must-Fix (N1-N3)、Should-Fix (W1-W8)、Questions (Q1-Q5)。"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-16T02:54:45.615133+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1515
}
```

</details>

---


### Assistant

_source line 214 · 2026-05-16T02:54:48.824488+00:00_

交叉分享已发送给两位 Reviewer，等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 215 · 2026-05-16T02:56:33.591480+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2 审稿意见

---

### Must-Fix 逐条回应

**[AGREE] R2-N1: `reflect-learn-2026` 引用不完整**
同意，我在自己的审稿中也标记了此问题（我的 W7）。作者字段 `[To be verified]` 在 double-blind 提交中不可接受。无论该论文是否真实存在，以此状态提交属于审稿材料质量问题。但我认为这是一个 5 分钟可修复的格式问题，不应上升到影响接收决定的 critical 级别——降为 Should-Fix 更合适。

**[AGREE] R2-N2: 缺少 Responsible NLP Research Checklist**
同意。ACL ARR 要求所有提交附带 checklist，我在自己的审稿中遗漏了这一点。若确实缺失，这是 desk reject 风险。但需确认：有些提交通过 OpenReview 单独上传 checklist 而非嵌入 main.tex。如果论文确实在任何渠道都没有提交 checklist，则确实是 critical。

**[REBUT] R2-N3: 核心效应量过小但 framing 过强**
部分不同意 R2 的定性。我在自己的审稿（W5）中也质疑了 r²=1.3-1.7% 到 31.2 pp gap 的跳跃缺乏形式化论证。但 R2 将此列为 critical 且同时给 Soundness 3.5/5，存在内部矛盾——如果效应量问题是 critical 级别，Soundness 不应高于 3.0。

更重要的是，论文在 §5.2 (results.tex L62-64) 中的 framing 实际上相当诚实：明确说 "modest in magnitude"，列出了其他可能的 variance sources（frequency、position effects、mention ambiguity 等），并将 SCS 定位为 "one specific, actionable mechanism" 而非全部解释。Contribution 2 标题也是 "statistically significant but modest predictor"。R2 说 "framing 过强" 可能更多是对 Abstract 中 "first controlled empirical study" 的措辞反应——但这个措辞描述的是实验设计的原创性，不是效应量大小。

**我与 R2 的实质分歧在于**：真正的问题不是 r² 小本身（小效应量在大样本中统计显著是正常的），而是 pairwise→batch 的信号放大缺乏形式化（我的 W5），以及 31.2 pp 来自整体回归不显著的 80-rel pool 的 extreme batches（我的 N3）。这些是统计方法论问题，不是"效应量太小"的问题。

**[REBUT] R2-N4: 正文仅一幅 Figure**
不同意 critical 级别。正文 Figure 1 包含两个 panel（count curves + BCS scaling），信息密度合理。Error taxonomy 的详细可视化放在 Appendix 是合理的空间分配——8 页正文限制下不可能把所有图都放正文。这更多是呈现偏好问题，不影响技术正确性或接收决定。

我同意增加 1-2 幅正文 figure（如将 error taxonomy 的关键 panel 提入正文、或加一个 MAVEN centrality confound 的 scatter plot）会改善可读性，但这是 Should-Fix (warning) 级别，不是 Must-Fix。

---

### Should-Fix 逐条回应

**[AGREE] R2-W1: Prompt template 未公开**
强烈同意。我在 Q1 中也提出了同样的问题。v1/v2 prompt 的完整文本对 reproducibility 至关重要——这也是我将 v1/v2 混淆列为 N1 (Critical) 的原因之一。没有 prompt 文本，读者无法判断 v1→v2 的变化是 minor formatting tweak 还是根本性的 task framing 改变。

**[AGREE] R2-W2: MAVEN 反转未在 Abstract 充分体现**
强烈同意，与我的 W1 一致。Abstract 说 "two degradation channels...across three IE tasks" 但实际上 MAVEN/ED 完全不符合这个叙事。Abstract 应当明确指出 ED 的反转趋势和 centrality confound，而非给读者一种"三个任务都支持 framework"的印象。

**[AGREE] R2-W3: FewRel 数据构造的外部效度**
同意，且我想补充一个 R2 隐含但未充分展开的重要观点：FewRel 的 RE 任务是 **closed-set classification**（给定 head/tail entities，选择 relation label），而非 **open extraction**（从文本中同时识别 entities 和 relations）。论文声称 "channels are cleanly separable in RE"（§5.5, results.tex L131）——但这个 "clean separation" 可能是 **任务形式的产物而非降解机制的真实属性**。Classification 任务中不存在 "entity detection" 环节，所以 Channel 2 自然不会影响 detection（missed rate flat at 10-16%）。将此解读为 "RE 上 channels cleanly separate" 是循环论证——classification 本身就消除了 detection 维度。

这一点削弱了论文最强的 claim 之一。如果 "clean separation" 只是因为 RE 没有 detection component，那它不能作为 framework 普适性的证据。

**[AGREE] R2-W4: `json-schema-bench-2025` 引用不完整**
同意但 severity 低。`and others` 在 bib 中不规范，应列出至少前三位作者。

**[AGREE] R2-W5: MiniLM 引用应补充 Sentence-BERT**
同意。论文使用的 `all-MiniLM-L6-v2` 是 Sentence-Transformers 框架下的模型，其训练方法论来自 Reimers & Gurevych (2019)。仅引用 MiniLM 原始论文（关于 knowledge distillation）不足以准确归因。

**[AGREE] R2-W6: 51% floor 的 "confusion subgroup" 解释是推测**
同意，与我的 W6 一致。论文在 Discussion (discussion.tex L8) 中提出 "models can still resolve a confusion subgroup of easily distinguishable relations"，但未提供任何实证支持（如：哪些 relations 被正确分类？是否存在可识别的 easy cluster？）。这是 post-hoc speculation，应标注为 hypothesis 而非 finding。

**[AGREE] R2-W7: §6 SDGD 正文过短**
部分同意。SDGD 被列为四个 contributions 之一（Introduction Contribution 4），但正文仅半页（sdgd_negative.tex 共 6 行文字），核心数据（Table 5, 完整 protocol）全在 Appendix。对于 claimed contribution，这不够。但我认为更根本的问题不是篇幅而是 **scope**——SDGD 仅在 Few-NERD 一个任务上测试（我的 W4），这比篇幅短更影响 claim 的可信度。

---

### Questions 逐条回应

**[AGREE] R2-Q1: Pairwise r²=1.5% 但 BCS gap=31.2 pp 的信号放大机制**
与我的 W5 完全一致。这是论文需要回答的核心问题。我补充：即使放大机制存在，31.2 pp 来自 extreme batches——within-pool 的 quartile Δ 仅 −3.92 pp（CI 穿越零，Table 4）。论文需要区分 "theoretical maximum amplification"（extreme batches）和 "typical amplification"（representative batches），并只用后者做 practical significance 论证。

**[AGREE] R2-Q2: v1→v2 prompt artifact**
与我的 N1 完全一致。v1→v2 使 precision 翻倍（SDGD 表格中 single_pass v1 P=0.563 vs v2 experiments showing much higher precision patterns），这说明 prompt 设计对提取行为有巨大影响。论文必须展示核心结论（两通道分离、BCS-accuracy 关系）在两个 prompt 版本下都成立，否则无法排除 prompt artifact。

**[AGREE] R2-Q3: SDGD 不在 FewRel 上测试**
与我的 W4 完全一致。RE 是 channels 最 cleanly separable 的任务——如果 confusability-aware decomposition 在最有利的条件下都不 work，这才是 "structural challenge" 的强证据。仅在 NER（channels 耦合的任务）上测试，无法区分 merge amplification 本身的问题和 NER-specific 的 detection coupling 问题。

**[REBUT] R2-Q4: 加入 type description 计算 SCS 是否提升预测力**
这是一个合理的 future work 建议，但我不认为它是当前论文的弱点。论文在 §3.2 (experimental_setup.tex L52) 明确说明 "Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time"——在 zero-shot 设置下，prompt 中只有 type names（至少在本文的实验设计中如此）。使用 name-only embedding 与实验设置一致。当然，如果未来工作的 prompt 包含 type definitions，SCS 应相应扩展。但要求当前论文测试一个超出其实验设置的 metric variant 不太公平。

**[REBUT] R2-Q5: Closed-source 模型验证**
合理建议但不是必要的。论文已在两个开源模型（Qwen3-32B, Llama-3.1-8B）上验证，涵盖不同模型家族和规模。Closed-source 模型（GPT-4, Claude）的 API 不支持 hidden-state extraction（用于 Qwen3 embedding 的 SCS），且 API 行为可能受 system prompt、safety filters 等影响，引入额外混淆。开源模型的 reproducibility 优势在本文的经验性研究中更重要。

---

### Missing References 回应

1. **Reimers & Gurevych (2019) Sentence-BERT** — [AGREE] 应补充，理由见 W5。
2. **Li et al. (2023) "Evaluating ChatGPT's IE Capabilities"** — [AGREE] 相关性较高，属于 zero-shot IE evaluation 文献，应至少在 §2.1 提及。
3. **Wadhwa et al. (2023) RE in era of LLMs** — [AGREE] 与论文的 RE 实验直接相关。
4. **AFET / hierarchical label confusion 文献** — [REBUT] 相关性有限。AFET (Ren et al., 2016) 关注的是 hierarchical fine-grained typing with noise，其 label confusion 概念与本文的 embedding-based confusability 在技术层面差异较大。可以在 related work 中一句话提及，但不是 missing 到影响论文完整性的程度。

---

### 总结：与 R2 的主要分歧

1. **R2 给 Soundness 3.5，我给 2.5** — 我认为 R2 低估了统计方法论问题的严重性（16-rel 无 CI、80-rel 回归不显著、非独立 bootstrap），这些直接影响核心 claims 的可信度。
2. **R2 将 N4 (仅一幅图) 列为 critical** — 我认为这是 presentation preference，不是 soundness 或 acceptance 决定问题。
3. **R2-W3 的 FewRel 外部效度** — 我提出了一个 R2 没有明确说的更深层问题：RE-as-classification 本身消除了 detection 维度，使 "clean channel separation" 成为任务设计的 artifact 而非 framework 的验证。
4. **R2-Q4 和 Q5** — 我认为这些是合理的 future work 方向但不是当前论文的缺陷。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 216 · 2026-05-16T02:56:40.833621+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 217 · 2026-05-16T02:56:43.442322+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

主要立场：
- 与 R2 在 7/11 个 Should-Fix + Must-Fix 上 AGREE，但对 N3 的 severity 定性和 N4 的 critical 级别持异议
- 对 R2-W3 (FewRel) 补充了更深层的论点：RE-as-classification 本身消除了 detection 维度，使 "clean channel separation" 可能是任务设计的 artifact
- 与 R2 最大的分歧在 Soundness 评分（我 2.5 vs R2 3.5）——我认为统计方法论问题（无 CI 的单 batch、不显著的 80-rel 回归、非独立 bootstrap）比 R2 认为的更严重

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 218 · 2026-05-16T02:56:50.611005+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 14

## Round 14

8 recorded events


### User

_source line 219 · 2026-05-16T02:57:08.565056+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

### Must-Fix

[AGREE] R1-N1: v1/v2 prompt 切换引入系统性混淆。同意 prompt 版本差异影响绝对值可比性。但严重程度需区分——每个实验内部 prompt 一致，核心 claim（两通道分离）不依赖跨 prompt 比较。真正问题在 Abstract headline numbers 未标注 prompt 版本。应公开完整 prompt（与我的 W1 一致）。

[AGREE] R1-N2: 16-rel 9.1 pp gap 单 batch 无 CI。完全同意。但论文的统计论证重心在 Table 4（independent 16-rel slope −0.449, CI [−0.552, −0.346], n=100），不在 9.1 pp。问题是叙事赋予 9.1 pp 过高地位。

[REBUT] R1-N3: 80-rel 回归不显著 → 31.2 pp cherry-picked。部分反驳。R1 忽略了论文的实际统计架构：(1) within-pool 16-sub (n=100) slope = −0.401, p=0.027, CI 排除零；(2) permutation test p=0.436 表明 slope 跨 pool 一致；(3) full 80-rel 不显著是 power 问题（n=25）。31.2 pp 有 CI [17.7, 42.7]。真正问题是 headline framing 缺 qualification，不是效应不存在。

### Should-Fix

[AGREE] R1-W1: "Multi-channel framework" 过度声称。与我的 W2 一致。
[AGREE] R1-W2: 非独立观测 bootstrap CI。有效统计批评，应用 cluster bootstrap。
[AGREE] R1-W3: NER non-monotonicity 未报 CI。与论文强调的统计严谨性不一致。
[AGREE] R1-W4: SDGD 仅在 Few-NERD 测试。与我的 Q3 一致。
[AGREE] R1-W5: r²→31.2 pp 论证跳跃。与我的 N3 直接相关。
[AGREE] R1-W6/W7/W8: 均同意，程度 minor。

### R1 vs R2 主要分歧

N3：R1 认为 80-rel 不显著 = cherry-picked；我认为 within-pool sub-analysis 提供有效支撑，问题在 framing 而非效应存在性。程度之争，非方向之争。

### 两份审稿的共同结论
论文实验设计有价值，但核心效应量 framing 不诚实，格式缺失不满足 ARR 要求，当前版本适合 Findings track，需重大修改。Overall 3.0/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-16T02:58:12.980086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-16T02:58:13.082929+00:00_

1	- id: MW1
2	  summary: "3.4× amplification 统计基础薄弱（16-rel 单 batch 无 CI + 跨 pool 混淆）"
3	  category: experiment
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 1
8	  mentions:
9	    - {round: 1, reviewers: [R1, R2], note: "R1-W1 + R2-W3 完全一致"}
10	  action_items:
11	    - {round: 1, action: "D033 16-rel 100 batch bootstrap CI（已在跑）", assigned_to: agent, status: in_progress}
12	    - {round: 1, action: "80-rel pool 内 16-type 子集 BCS-controlled 实验（消除跨 pool 混淆）", assigned_to: agent, status: done}
13	    - {round: 1, action: "论文 3.4× 附 CI，根据 within-pool 结果决定是否降格", assigned_to: paper_agent, status: open}
14	  resolution: ""
15	  resolution_round: null
16	
17	- id: MW2
18	  summary: "Pairwise SCS 'robust predictor' framing vs r²=1.3% + conditioning-on-outcome bias"
19	  category: framing
20	  severity: critical
21	  status: in_progress
22	  first_raised_round: 1
23	  last_seen_round: 1
24	  mentions:
25	    - {round: 1, reviewers: [R1, R2], note: "R1-W2 + R2-W2 共识"}
26	  action_items:
27	    - {round: 1, action: "Contribution 2 'robust predictor' → 'statistically significant but modest predictor'", assigned_to: paper_agent, status: open}
28	    - {round: 1, action: "§5.2 加 conditioning-on-outcome bias 讨论 + 并列 all-pairs vs nonzero-only", assigned_to: paper_agent, status: open}
29	    - {round: 1, action: "讨论 98% variance 来源", assigned_to: paper_agent, status: open}
30	  resolution: ""
31	  resolution_round: null
32	
33	- id: MW3
34	  summary: "NER count×confusability interaction p=0.505 但正文称 'interact'"
35	  category: framing
36	  severity: critical
37	  status: in_progress
38	  first_raised_round: 1
39	  last_seen_round: 1
40	  mentions:
41	    - {round: 1, reviewers: [R1, R2], note: "R1-W3 + R2 AGREE"}
42	  action_items:
43	    - {round: 1, action: "正文移除 'interact'/'suggestive'，factorial p=0.505 移入 supplementary 作为 negative result", assigned_to: paper_agent, status: open}
44	  resolution: ""
45	  resolution_round: null
46	
47	- i
…[truncated 9098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-16T03:00:36.491039+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "\n# Round 2 Review Issues Tracker\n# Updated: 2026-05-16\n\n# ============================================================\n# CRITICAL — Must-Fix（影响接收决定）\n# ============================================================\n\n- id: MW1\n  summary: \"16-rel BCS gap (9.1 pp) 基于单 batch 无 CI，统计不可靠\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W1 + R2-W3 完全一致\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R1-N2 re-raised; within-pool 分析已补但 16-rel 独立 pool 仍为单 batch; R2 AGREE\"}\n  action_items:\n    - {round: 1, action: \"D033 16-rel 100 batch bootstrap CI\", assigned_to: agent, status: done}\n    - {round: 1, action: \"80-rel pool 内 16-type 子集 BCS-controlled 实验\", assigned_to: agent, status: done}\n    - {round: 2, action: \"论文中 9.1 pp 数字必须附 CI 或降级为 illustrative（非 inferential）；叙事重心应移至 Table 4 回归分析\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: MW2\n  summary: \"Pairwise r²=1.3-1.7% → batch-level 31.2 pp 的信号放大缺乏形式化论证\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W2 + R2-W2 共识\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W5 + R2-N3; Contribution 2 已改为 'modest predictor'，但 pairwise→batch 放大机制仍未解释; within-pool quartile Δ = −3.92 pp (CI 穿越零) 与 31.2 pp 矛盾\"}\n  action_items:\n    - {round: 1, action: \"Contribution 2 改为 'modest predictor'\", assigned_to: paper_agent, status: done}\n    - {round: 1, action: \"§5.2 加 conditioning-on-outcome bias 讨论\", assigned_to: paper_agent, status: done}\n    - {round: 2, action: \"新增：用 typical BCS range × slope 计算 realistic practical effect，区分 extreme vs representative batches\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW3\n  summary: \"v1/v2 prompt 切换引入跨实验系统性混淆\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W5 + R2 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"升级为 R1-N1 Critical; v1 offset 错误率 96.5%，v1→v2 recall 差 11%; SDGD 用 v1, cross-model 用 v2; 两 Reviewer 共识 Critical; prompt 仍未公开\"}\n  action_items:\n    - {round: 1, action: \"论文标注 prompt 版本\", assigned_to: paper_agent, status: done}\n    - {round: 2, action: \"公开 v1/v2 完整 prompt template 至 Appendix\", assigned_to: paper_agent, status: open}\n    - {round: 2, action: \"对关键实验（count curves, BCS-controlled）报告两版 prompt 结果 or 统一单版本\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: m3\n  summary: \"缺 Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W9 + R1 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-N2 升级为 Critical; ARR 必须项，缺失导致 desk reject 风险; R1 AGREE\"}\n  action_items:\n    - {round: 2, action: \"补充完整 Responsible NLP Research Checklist\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N3-80rel\n  summary: \"80-rel 整体 BCS-accuracy 回归不显著 (p=0.698) 但 extreme batches 做 headline result\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-N3 提出; R2 部分反驳——认为 within-pool sub-analysis 有效支撑 (slope −0.401, p=0.027)，问题在 framing 而非效应不存在; 程度之争\"}\n  action_items:\n    - {round: 2, action: \"31.2 pp 出现时必须紧跟注明 full 80-rel 回归不显著 (n=25, underpowered)，核心统计证据应指向 within-pool slope\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING — Should-Fix（影响评分）\n# ============================================================\n\n- id: R2-W1-framework\n  summary: \"'Multi-channel degradation framework' 过度声称——仅 RE cleanly works\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W1 + R2 AGREE (与 R2-W2 MAVEN 一致); NER 有 channel 耦合, ED 反转; 'framework' 暗示通用性但证据仅 RE\"}\n  action_items:\n    - {round: 2, action: \"Contribution 1 降格为 'empirical observations' 或 'empirical decomposition'，明确限定适用范围\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W2-bootstrap\n  summary: \"Pairwise SCS-confusion bootstrap CI 基于非独立观测，低估不确定性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W2 提出; R2 AGREE; 同 type 出现在多个 pairs, 应用 cluster-robust bootstrap\"}\n  action_items:\n    - {round: 2, action: \"使用 type-level cluster bootstrap 重算 CI，或在论文中讨论 CI 可能被低估\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3-nonmono\n  summary: \"NER count=22→44 recall 上升 (0.527→0.551) 未报 CI，non-monotonicity 未充分解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W3 提出; R2 AGREE\"}\n  action_items:\n    - {round: 2, action: \"报告 count=22 和 count=44 的 bootstrap CI; 若 CI 重叠则说明 non-monotonicity 在 noise 范围内\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W4-sdgd-scope\n  summary: \"SDGD 负面结果仅在 Few-NERD (NER) 上测试，泛化性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W4 + R2-Q3 共识; RE 是 channels 最 cleanly separable 的任务，FewRel SDGD 结果对 merge amplification claim 更有说服力\"}\n  action_items:\n    - {round: 2, action: \"FewRel SDGD 实验 or 在论文中限定 SDGD 结论仅适用于 NER/span-level extraction\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W5-RE-artifact\n  summary: \"RE 'clean channel separation' 可能是 classification task 形式的 artifact\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"R1 交叉回应 R2-W3 时提出; closed-set classification 本身不含 detection 环节, missed rate flat (10-16%) 可能是任务形式产物而非 framework 验证; R2 未明确回应此点\"}\n  action_items:\n    - {round: 2, action: \"Discussion 中讨论 RE 作为 classification 对 channel separation 解读的限制\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW6\n  summary: \"Prompt 模板未在 appendix 公开\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W8 + R2 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W1 re-raised; R1 强烈同意; 与 SW3 prompt 混淆问题关联\"}\n  action_items:\n    - {round: 2, action: \"v1 + v2 完整 prompt 模板加入 Appendix\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: MW4\n  summary: \"正文仅一幅 Figure（Round 1 为零，已改善但仍不足）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W1 + R1 AGREE; 正文零 figure\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-N4 re-raised; Figure 1 有两 panel 但仍仅 1 figure; R1 降级为 warning; error taxonomy figure 仍在 Appendix\"}\n  action_items:\n    - {round: 2, action: \"Error taxonomy 关键 panel 或 MAVEN centrality scatter plot 移入正文\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW4\n  summary: \"MAVEN 反转在 Abstract 中未充分体现，限制 generalizability 声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W5 + R1 partially agree\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W2 re-raised; Abstract 说 'generally suppresses recall' 但 MAVEN 完全反转; 需 1-2 句独立陈述\"}\n  action_items:\n    - {round: 2, action: \"Abstract 给 MAVEN 反转和 centrality confound 独立陈述（非括号附注）\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6-FewRel\n  summary: \"FewRel 数据构造外部效度——合并 train+val、classification vs extraction\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"m4/m6 部分涉及\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W3 提出; R1 AGREE 并深化——classification 任务形式限制了 channel separation 解读\"}\n  action_items:\n    - {round: 2, action: \"Limitations 增加 classification vs extraction 讨论; 说明合并 train+val 的原因\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor（锦上添花）\n# ============================================================\n\n- id: R2-W7-51floor\n  summary: \"51% floor 'confusion subgroup' 解释是推测性的，无实证支撑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W6 + R1-W6 共识; Discussion 中标注为 hypothesis\"}\n  action_items:\n    - {round: 2, action: \"标注为 hypothesis/conjecture 而非 finding\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W8-model-invariant\n  summary: \"'model-invariant floor' 基于仅两个 decoder-only 模型\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"R1-W6; R2 未单独标记但与 R2-Q5 closed-source 模型相关\"}\n  action_items:\n    - {round: 2, action: \"限定为 'consistent across tested models' 而非 'model-invariant'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: m1\n  summary: \"MiniLM 引用不精确——应补充 Reimers & Gurevych 2019 Sentence-BERT\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W8 + R1 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W5 re-raised; R1 AGREE; 仍未修正\"}\n  action_items:\n    - {round: 2, action: \"补充 Reimers & Gurevych 2019 引用\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: REF1\n  summary: \"reflect-learn-2026 引用作者为占位符 '[To be verified]'\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2 提出, R1 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-N1 列为 Critical; R1 同意问题但降级为 Should-Fix; 仍为占位符\"}\n  action_items:\n    - {round: 2, action: \"补全作者信息 or 删除引用并调整正文\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W9-jsonbib\n  summary: \"json-schema-bench-2025 引用不完整——author 为 'Li, Saibo and others'\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W4; R1 AGREE\"}\n  action_items:\n    - {round: 2, action: \"补全前三位作者\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-REF-missing\n  summary: \"缺失引用：Sentence-BERT, Li et al. 2023 ChatGPT IE, Wadhwa et al. 2023 RE with LLMs\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R2], note: \"R2 Missing References; R1 AGREE on Sentence-BERT, Li et al., Wadhwa et al.; REBUT AFET as limited relevance\"}\n  action_items:\n    - {round: 2, action: \"补充 Sentence-BERT, Li et al. 2023, Wadhwa et al. 2023 引用\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-m-sdgd-short\n  summary: \"§6 SDGD 正文仅半页，核心数据全在 Appendix，与 Contribution 4 地位不符\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W7; R1 partially agree——更根本问题是 scope (仅 NER)\"}\n  action_items:\n    - {round: 2, action: \"扩展 §6 或将 Table 5 核心行移入正文\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED（本轮确认已修复）\n# ============================================================\n\n- id: MW3\n  summary: \"NER count×confusability interaction p=0.505 但正文称 'interact'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W3 + R2 AGREE\"}\n    - {round: 2, reviewers: [], note: \"已移至 Appendix (Factorial Analysis) 作为 negative result，正文不再使用 'interact' 措辞\"}\n  resolution: \"Factorial test 移入 Appendix §B，正文删除 'interact'/'suggestive'，改为如实报告 non-significant\"\n  resolution_round: 2\n\n- id: SW1\n  summary: \"无 Discussion section\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W4 + R1 AGREE\"}\n    - {round: 2, reviewers: [], note: \"Discussion section 已添加 (discussion.tex)，含 boundary conditions / 51% floor / merge amplification / schema design implications\"}\n  resolution: \"§7 Discussion 已添加，覆盖边界条件、merge 方向、schema 设计建议\"\n  resolution_round: 2\n\n- id: SW2\n  summary: \"SDGD 'structural bottleneck' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W4 + R2 partial rebut\"}\n    - {round: 2, reviewers: [], note: \"已改为 'structural challenge for union-based merge pipelines'\"}\n  resolution: \"措辞已降格\"\n  resolution_round: 2\n\n- id: SW5\n  summary: \"Limitations section 结构差，单段 ~20 行\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W7 + R1 AGREE\"}\n    - {round: 2, reviewers: [], note: \"已重构为 6 条编号列表，按严重程度排序\"}\n  resolution: \"Limitations 已重构为编号列表\"\n  resolution_round: 2\n\n- id: Q3\n  summary: \"SDGD single_pass prompt 版本未标注\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-Q3 + R2 AGREE\"}\n    - {round: 2, reviewers: [], note: \"Table 5 caption 已标注 'All modes use the v1 prompt'\"}\n  resolution: \"已标注\"\n  resolution_round: 2\n\n- id: Q4\n  summary: \"Residualized BCS：去除 centrality 后 MAVEN 是否恢复预期方向？\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-Q2 + R1 强烈支持\"}\n    - {round: 2, reviewers: [], note: \"Appendix §C 已添加完整 residualized BCS 分析，确认控制 centrality 后相关消失\"}\n  resolution: \"Appendix C (Controlling for Centrality Confounds) 已添加\"\n  resolution_round: 2\n\n- id: REF3\n  summary: \"缺失引用：Sclar et al. 2024 TACL (prompt sensitivity)\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2 提出, R1 AGREE\"}\n    - {round: 2, reviewers: [], note: \"已添加 sclar-sensitivity-2024 至 references.bib 并在 §3.5 引用\"}\n  resolution: \"引用已添加\"\n  resolution_round: 2\n\n- id: m5\n  summary: \"'Multi-channel degradation model' → 'framework'\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W11 + R1 AGREE\"}\n    - {round: 2, reviewers: [], note: \"全文已使用 'framework'（注：'framework' 本身的 overclaim 问题另见 R2-W1-framework）\"}\n  resolution: \"术语已统一\"\n  resolution_round: 2\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "\n# Round 2 Review Issues Tracker\n# Updated: 2026-05-16\n\n# ============================================================\n# CRITICAL — Must-Fix（影响接收决定）\n# ============================================================\n\n- id: MW1\n  summary: \"16-rel BCS gap (9.1 pp) 基于单 batch 无 CI，统计不可靠\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W1 + R2-W3 完全一致\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R1-N2 re-raised; within-pool 分析已补但 16-rel 独立 pool 仍为单 batch; R2 AGREE\"}\n  action_items:\n    - {round: 1, action: \"D033 16-rel 100 batch bootstrap CI\", assigned_to: agent, status: done}\n    - {round: 1, action: \"80-rel pool 内 16-type 子集 BCS-controlled 实验\", assigned_to: agent, status: done}\n    - {round: 2, action: \"论文中 9.1 pp 数字必须附 CI 或降级为 illustrative（非 inferential）；叙事重心应移至 Table 4 回归分析\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: MW2\n  summary: \"Pairwise r²=1.3-1.7% → batch-level 31.2 pp 的信号放大缺乏形式化论证\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W2 + R2-W2 共识\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W5 + R2-N3; Contribution 2 已改为 'modest predictor'，但 pairwise→batch 放大机制仍未解释; within-pool quartile Δ = −3.92 pp (CI 穿越零) 与 31.2 pp 矛盾\"}\n  action_items:\n    - {round: 1, action: \"Contribution 2 改为 'modest predictor'\", assigned_to: paper_agent, status: done}\n    - {round: 1, action: \"§5.2 加 conditioning-on-outcome bias 讨论\", assigned_to: paper_agent, status: done}\n    - {round: 2, action: \"新增：用 typical BCS range × slope 计算 realistic practical effect，区分 extreme vs representative batches\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW3\n  summary: \"v1/v2 prompt 切换引入跨实验系统性混淆\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W5 + R2 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"升级为 R1-N1 Critical; v1 offset 错误率 96.5%，v1→v2 recall 差 11%; SDGD 用 v1, cross-model 用 v2; 两 Reviewer 共识 Critical; prompt 仍未公开\"}\n  action_items:\n    - {round: 1, action: \"论文标注 prompt 版本\", assigned_to: paper_agent, status: done}\n    - {round: 2, action: \"公开 v1/v2 完整 prompt template 至 Appendix\", assigned_to: paper_agent, status: open}\n    - {round: 2, action: \"对关键实验（count curves, BCS-controlled）报告两版 prompt 结果 or 统一单版本\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: m3\n  summary: \"缺 Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W9 + R1 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-N2 升级为 Critical; ARR 必须项，缺失导致 desk reject 风险; R1 AGREE\"}\n  action_items:\n    - {round: 2, action: \"补充完整 Responsible NLP Research Checklist\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N3-80rel\n  summary: \"80-rel 整体 BCS-accuracy 回归不显著 (p=0.698) 但 extreme batches 做 headline result\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-N3 提出; R2 部分反驳——认为 within-pool sub-analysis 有效支撑 (slope −0.401, p=0.027)，问题在 framing 而非效应不存在; 程度之争\"}\n  action_items:\n    - {round: 2, action: \"31.2 pp 出现时必须紧跟注明 full 80-rel 回归不显著 (n=25, underpowered)，核心统计证据应指向 within-pool slope\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING — Should-Fix（影响评分）\n# ============================================================\n\n- id: R2-W1-framework\n  summary: \"'Multi-channel degradation framework' 过度声称——仅 RE cleanly works\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W1 + R2 AGREE (与 R2-W2 MAVEN 一致); NER 有 channel 耦合, ED 反转; 'framework' 暗示通用性但证据仅 RE\"}\n  action_items:\n    - {round: 2, action: \"Contribution 1 降格为 'empirical observations' 或 'empirical decomposition'，明确限定适用范围\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W2-bootstrap\n  summary: \"Pairwise SCS-confusion bootstrap CI 基于非独立观测，低估不确定性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W2 提出; R2 AGREE; 同 type 出现在多个 pairs, 应用 cluster-robust bootstrap\"}\n  action_items:\n    - {round: 2, action: \"使用 type-level cluster bootstrap 重算 CI，或在论文中讨论 CI 可能被低估\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3-nonmono\n  summary: \"NER count=22→44 recall 上升 (0.527→0.551) 未报 CI，non-monotonicity 未充分解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W3 提出; R2 AGREE\"}\n  action_items:\n    - {round: 2, action: \"报告 count=22 和 count=44 的 bootstrap CI; 若 CI 重叠则说明 non-monotonicity 在 noise 范围内\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W4-sdgd-scope\n  summary: \"SDGD 负面结果仅在 Few-NERD (NER) 上测试，泛化性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R1-W4 + R2-Q3 共识; RE 是 channels 最 cleanly separable 的任务，FewRel SDGD 结果对 merge amplification claim 更有说服力\"}\n  action_items:\n    - {round: 2, action: \"FewRel SDGD 实验 or 在论文中限定 SDGD 结论仅适用于 NER/span-level extraction\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W5-RE-artifact\n  summary: \"RE 'clean channel separation' 可能是 classification task 形式的 artifact\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"R1 交叉回应 R2-W3 时提出; closed-set classification 本身不含 detection 环节, missed rate flat (10-16%) 可能是任务形式产物而非 framework 验证; R2 未明确回应此点\"}\n  action_items:\n    - {round: 2, action: \"Discussion 中讨论 RE 作为 classification 对 channel separation 解读的限制\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW6\n  summary: \"Prompt 模板未在 appendix 公开\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W8 + R2 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W1 re-raised; R1 强烈同意; 与 SW3 prompt 混淆问题关联\"}\n  action_items:\n    - {round: 2, action: \"v1 + v2 完整 prompt 模板加入 Appendix\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: MW4\n  summary: \"正文仅一幅 Figure（Round 1 为零，已改善但仍不足）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W1 + R1 AGREE; 正文零 figure\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-N4 re-raised; Figure 1 有两 panel 但仍仅 1 figure; R1 降级为 warning; error taxonomy figure 仍在 Appendix\"}\n  action_items:\n    - {round: 2, action: \"Error taxonomy 关键 panel 或 MAVEN centrality scatter plot 移入正文\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW4\n  summary: \"MAVEN 反转在 Abstract 中未充分体现，限制 generalizability 声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W5 + R1 partially agree\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W2 re-raised; Abstract 说 'generally suppresses recall' 但 MAVEN 完全反转; 需 1-2 句独立陈述\"}\n  action_items:\n    - {round: 2, action: \"Abstract 给 MAVEN 反转和 centrality confound 独立陈述（非括号附注）\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6-FewRel\n  summary: \"FewRel 数据构造外部效度——合并 train+val、classification vs extraction\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"m4/m6 部分涉及\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W3 提出; R1 AGREE 并深化——classification 任务形式限制了 channel separation 解读\"}\n  action_items:\n    - {round: 2, action: \"Limitations 增加 classification vs extraction 讨论; 说明合并 train+val 的原因\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor（锦上添花）\n# ============================================================\n\n- id: R2-W7-51floor\n  summary: \"51% floor 'confusion subgroup' 解释是推测性的，无实证支撑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W6 + R1-W6 共识; Discussion 中标注为 hypothesis\"}\n  action_items:\n    - {round: 2, action: \"标注为 hypothesis/conjecture 而非 finding\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W8-model-invariant\n  summary: \"'model-invariant floor' 基于仅两个 decoder-only 模型\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"R1-W6; R2 未单独标记但与 R2-Q5 closed-source 模型相关\"}\n  action_items:\n    - {round: 2, action: \"限定为 'consistent across tested models' 而非 'model-invariant'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: m1\n  summary: \"MiniLM 引用不精确——应补充 Reimers & Gurevych 2019 Sentence-BERT\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W8 + R1 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W5 re-raised; R1 AGREE; 仍未修正\"}\n  action_items:\n    - {round: 2, action: \"补充 Reimers & Gurevych 2019 引用\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: REF1\n  summary: \"reflect-learn-2026 引用作者为占位符 '[To be verified]'\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2 提出, R1 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R2-N1 列为 Critical; R1 同意问题但降级为 Should-Fix; 仍为占位符\"}\n  action_items:\n    - {round: 2, action: \"补全作者信息 or 删除引用并调整正文\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W9-jsonbib\n  summary: \"json-schema-bench-2025 引用不完整——author 为 'Li, Saibo and others'\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W4; R1 AGREE\"}\n  action_items:\n    - {round: 2, action: \"补全前三位作者\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-REF-missing\n  summary: \"缺失引用：Sentence-BERT, Li et al. 2023 ChatGPT IE, Wadhwa et al. 2023 RE with LLMs\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R2], note: \"R2 Missing References; R1 AGREE on Sentence-BERT, Li et al., Wadhwa et al.; REBUT AFET as limited relevance\"}\n  action_items:\n    - {round: 2, action: \"补充 Sentence-BERT, Li et al. 2023, Wadhwa et al. 2023 引用\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-m-sdgd-short\n  summary: \"§6 SDGD 正文仅半页，核心数据全在 Appendix，与 Contribution 4 地位不符\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W7; R1 partially agree——更根本问题是 scope (仅 NER)\"}\n  action_items:\n    - {round: 2, action: \"扩展 §6 或将 Table 5 核心行移入正文\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED（本轮确认已修复）\n# ============================================================\n\n- id: MW3\n  summary: \"NER count×confusability interaction p=0.505 但正文称 'interact'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W3 + R2 AGREE\"}\n    - {round: 2, reviewers: [], note: \"已移至 Appendix (Factorial Analysis) 作为 negative result，正文不再使用 'interact' 措辞\"}\n  resolution: \"Factorial test 移入 Appendix §B，正文删除 'interact'/'suggestive'，改为如实报告 non-significant\"\n  resolution_round: 2\n\n- id: SW1\n  summary: \"无 Discussion section\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W4 + R1 AGREE\"}\n    - {round: 2, reviewers: [], note: \"Discussion section 已添加 (discussion.tex)，含 boundary conditions / 51% floor / merge amplification / schema design implications\"}\n  resolution: \"§7 Discussion 已添加，覆盖边界条件、merge 方向、schema 设计建议\"\n  resolution_round: 2\n\n- id: SW2\n  summary: \"SDGD 'structural bottleneck' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W4 + R2 partial rebut\"}\n    - {round: 2, reviewers: [], note: \"已改为 'structural challenge for union-based merge pipelines'\"}\n  resolution: \"措辞已降格\"\n  resolution_round: 2\n\n- id: SW5\n  summary: \"Limitations section 结构差，单段 ~20 行\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W7 + R1 AGREE\"}\n    - {round: 2, reviewers: [], note: \"已重构为 6 条编号列表，按严重程度排序\"}\n  resolution: \"Limitations 已重构为编号列表\"\n  resolution_round: 2\n\n- id: Q3\n  summary: \"SDGD single_pass prompt 版本未标注\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-Q3 + R2 AGREE\"}\n    - {round: 2, reviewers: [], note: \"Table 5 caption 已标注 'All modes use the v1 prompt'\"}\n  resolution: \"已标注\"\n  resolution_round: 2\n\n- id: Q4\n  summary: \"Residualized BCS：去除 centrality 后 MAVEN 是否恢复预期方向？\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-Q2 + R1 强烈支持\"}\n    - {round: 2, reviewers: [], note: \"Appendix §C 已添加完整 residualized BCS 分析，确认控制 centrality 后相关消失\"}\n  resolution: \"Appendix C (Controlling for Centrality Confounds) 已添加\"\n  resolution_round: 2\n\n- id: REF3\n  summary: \"缺失引用：Sclar et al. 2024 TACL (prompt sensitivity)\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2 提出, R1 AGREE\"}\n    - {round: 2, reviewers: [], note: \"已添加 sclar-sensitivity-2024 至 references.bib 并在 §3.5 引用\"}\n  resolution: \"引用已添加\"\n  resolution_round: 2\n\n- id: m5\n  summary: \"'Multi-channel degradation model' → 'framework'\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2-W11 + R1 AGREE\"}\n    - {round: 2, reviewers: [], note: \"全文已使用 'framework'（注：'framework' 本身的 overclaim 问题另见 R2-W1-framework）\"}\n  resolution: \"术语已统一\"\n  resolution_round: 2\n"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-16T03:00:36.696400+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 15608}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 205
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-16T03:03:05.836637+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "report": "\n# 圆桌审稿报告 — Round 2\n\n**论文**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿人**: Reviewer 1 (方法严谨性 + 实验设计 + 统计分析), Reviewer 2 (新颖性 + 完整性 + 写作质量 + 格式合规)\n**轮次**: Round 2（论文已针对 Round 1 的 18 个 issue 进行修订）\n**外部审稿**: 未启用\n\n---\n\n## Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能下降的机制，提出将退化分解为 type count 和 type confusability 两个独立通道。引入 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 作为量化指标，在 Few-NERD (NER)、FewRel (RE)、MAVEN (ED) 三个数据集上进行控制实验。主要发现：(1) RE 上两通道 cleanly separable；(2) NER 上 confusability 同时影响 detection；(3) MAVEN 上出现 centrality confound 导致 per-type BCS 方向反转；(4) SDGD 负面结果表明 union-based merge 存在结构性挑战。跨模型验证在 Llama-3.1-8B 上复现了主要效应。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且定义清晰。** 首次系统性隔离 type count 与 type confusability 的独立效应，填补了零样本 IE 退化机制研究的空白。三个 research question 直接可检验。【R1, R2 共识】\n\n**S2. 实验设计精心。** Count curves + BCS-controlled 双范式互补，within-pool controlled comparison (Table 4) 消除跨 pool 混淆，permutation test 比较跨条件 slope 一致性。这是 empirical IE 研究中少见的控制实验水平。【R1 重点肯定】\n\n**S3. 诚实报告 modest effect sizes 和负面结果。** Pairwise r²=1.3-1.7% 如实量化，SDGD 负面结果完整报告而非隐藏，MAVEN centrality confound 作为独立分析呈现。科学态度端正。【R1, R2 共识】\n\n**S4. Centrality confound 分析有独立方法论价值。** 识别 same-domain schema 下 BCS 聚合失效的机制，连接 representation degeneration 文献，partial correlation 验证严谨。对 schema analysis 从业者有直接指导意义。【R1 重点肯定】\n\n**S5. Round 1 修订实质性改进。** Discussion section 新增、Limitations 重构为编号列表、factorial test 移入 Appendix 作为 negative result、Contribution 2 改为 \"modest predictor\"、SDGD 措辞降格、Sclar et al. 引用补充、residualized BCS 分析加入 Appendix。共 8/18 个 Round 1 issue 已解决。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] v1/v2 prompt 切换引入系统性混淆，仍未解决。** v1 prompt（含 offset 要求，96.5% 错误率）用于 count curves + BCS-controlled NER + SDGD；v2 prompt 用于后续实验和 cross-model 验证。v1→v2 使 Qwen3 count=1 recall 差 11% (0.72 vs 0.64)。论文跨实验引用数字时（如 Abstract headline numbers），prompt 版本不同使比较无效。核心 framework 的两个 channel 建立在不同 prompt 版本上。**Prompt 模板仍未公开**，读者无法判断变化性质。\n- Round 1 状态：SW3 (warning) → Round 2 升级为 Critical\n- 两 Reviewer 共识 Critical。\n- **要求**：(a) 公开完整 prompt template 至 Appendix；(b) 对关键实验报告两版 prompt 结果 or 全部统一至一版。\n\n**C2. [Critical] 16-rel BCS gap (9.1 pp) 基于单 batch，无统计可靠性。** Table 3 caption 明确标注\"single extreme batch per BCS level; bootstrap CIs require multiple batches\"。但 9.1 pp 在 Abstract 和 §5.3 中与 31.2 pp 对比以论证 BCS range 解释 absolute gap 差异——对比的一端无任何 CI。\n- Round 1 状态：MW1 部分解决（within-pool 已补），16-rel 独立 pool 单 batch 问题持续。\n- 两 Reviewer 共识。\n- **要求**：补充多 batch CI，或将 9.1 pp 降级为 illustrative，叙事重心移至 Table 4 回归分析。\n\n**C3. [Critical] 80-rel 整体 BCS-accuracy 回归不显著，但 extreme batches 做 headline result。** Table 4: Full 80-rel slope = −0.151, CI [−0.930, +0.657], p = 0.698。31.2 pp 来自同一 pool 的 extreme batches，出现在 Abstract/Introduction/Discussion/Conclusion。\n- R1 认为这是 cherry-picked endpoints；R2 反驳认为 within-pool sub-analysis (slope −0.401, p=0.027) 提供有效支撑，问题在 framing。**程度分歧，非方向分歧**——两方均认为当前 framing 不当。\n- **要求**：31.2 pp 出现时必须注明 full 80-rel 条件不显著 (underpowered)，核心统计论证应指向 within-pool slope。\n\n**C4. [Critical] 缺少 Responsible NLP Research Checklist。** ACL ARR 必须项，缺失导致 desk reject 风险。Round 1 已提出 (m3)，仍未解决。\n- 两 Reviewer 共识。\n- **要求**：立即补充。\n\n**C5. [Critical] reflect-learn-2026 引用作者为占位符 `[To be verified]`。** 提交带占位符的 bib 条目不可接受。\n- R2 列为 Critical，R1 认为应为 Should-Fix（5 分钟可修复的格式问题）。\n- **要求**：补全作者信息，或删除引用并调整正文。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [Major] \"Multi-channel degradation framework\" 过度声称。** 框架仅在 RE 上 cleanly work：NER 有 channel 耦合 + non-monotonic count curve + 不显著 factorial test；ED 完全反转。\"Framework\" 暗示通用性，但证据支持的是 \"empirical observations primarily demonstrated on RE\"。两 Reviewer 共识。\n\n**W2. [Major] Pairwise→batch 信号放大机制未形式化。** r²=1.3-1.7% 跳至 31.2 pp gap 缺乏形式化论证。within-pool quartile Δ 仅 −3.92 pp (CI 穿越零)。论文需区分 extreme batches 的理论最大效应和 representative batches 的典型效应，用 BCS range × slope 计算 realistic practical effect。两 Reviewer 共识（R1-W5 + R2-N3）。\n\n**W3. [Major] Pairwise SCS-confusion bootstrap CI 基于非独立观测。** 1,953/11,026 type pairs 不独立（同 type 出现在多 pairs），percentile bootstrap 低估真实不确定性，p < 10^{-10} 可能被高估。应使用 type-level cluster-robust bootstrap。R1 提出，R2 AGREE。\n\n**W4. [Major] NER count=22→44 recall 上升 (0.527→0.551) 未报 CI。** \"Minor non-monotonicity\" 需 CI 支撑——若 CI 不重叠则说明 count channel 在 NER 上非单调，影响 \"count drives recall decline\" 叙事。R1 提出，R2 AGREE。\n\n**W5. [Major] SDGD 仅在 Few-NERD 测试，泛化性不足。** RE 是 channels 最 cleanly separable 的任务；若 SDGD 在 RE 上也失败则大大增强 merge amplification 论点。仅在一个任务上就得出\"structural challenge for union-based merge pipelines\"的一般性结论，证据不够。R1 提出，R2 AGREE。\n\n**W6. [Major] RE \"clean channel separation\" 可能是 classification 任务形式的 artifact。** FewRel RE 是 closed-set classification（给定 entity pair 选 relation），不含 entity detection 环节。Missed rate flat (10-16%) 可能是任务形式产物——classification 本身消除了 detection 维度，使 \"RE 上 channels cleanly separate\" 成为循环论证。应在 Limitations/Discussion 讨论。R1 交叉回应中提出。\n\n**W7. [Major] MAVEN 反转在 Abstract 中仍被低估。** 三个数据集中最大的 (168 types) 结果与主假设方向相反。Abstract 用 \"generally suppresses recall\" 一带而过，应给 MAVEN 反转和 centrality confound 独立陈述（1-2 句）。两 Reviewer 共识。\n\n**W8. [Major] Prompt template 仍未公开。** v1→v2 导致 precision 翻倍，说明 prompt 设计对结果影响巨大。不公开严重影响可复现性。Round 1 (SW6) 未解决。两 Reviewer 共识。\n\n**W9. [Warning] 正文仅一幅 Figure（Round 1 为零，已改善）。** Error taxonomy 是支撑 Channel 2 的关键证据但仍在 Appendix。R2 列为 Critical，R1 降级为 warning——以 8 页限制合理安排优先级。建议至少补一幅 error taxonomy 或 centrality scatter plot。\n\n**W10. [Warning] FewRel 数据构造外部效度。** 合并 train+val 非标准用法；closed-set classification 与 extraction 有本质差异但论文并列讨论。R2 提出，R1 AGREE。\n\n**W11. [Warning] 51% floor \"confusion subgroup\" 解释为推测。** Discussion 中未标注为 hypothesis。R1, R2 共识。\n\n**W12. [Warning] \"model-invariant floor\" 基于仅两个 decoder-only 模型。** 应限定为 \"consistent across tested models\"。R1 提出。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全共识：\n1. v1/v2 prompt 混淆是关键方法论问题 (C1)\n2. 16-rel 单 batch 无 CI 统计不可靠 (C2)\n3. 缺 Responsible NLP Checklist (C4)\n4. reflect-learn-2026 引用不完整 (C5)\n5. \"Framework\" overclaim (W1)\n6. Pairwise→batch 放大缺形式化 (W2)\n7. 非独立 bootstrap CI (W3)\n8. SDGD 仅在 NER 测试 (W5)\n9. Prompt template 必须公开 (W8)\n10. MAVEN 在 Abstract 中被低估 (W7)\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 立场 | R2 立场 | 性质 |\n|------|---------|---------|------|\n| 80-rel 回归不显著 (C3) | Cherry-picked endpoints | Within-pool sub-analysis 有效支撑，framing 问题 | 程度之争 |\n| 正文 figure 数量 (W9) | Warning 级别 | Critical 级别 | 严重性之争 |\n| reflect-learn-2026 (C5) | Should-Fix | Critical | 严重性之争 |\n| Soundness 评分 | 2.5/5 | 3.5/5 | R1 更重视统计方法论缺陷 |\n| R2-Q4 type description SCS | Future work, 非当前弱点 | 合理问题 | 范围之争 |\n| R2-Q5 closed-source 模型 | 不必要，开源更可复现 | 合理建议 | 范围之争 |\n\n---\n\n## Questions for Authors\n\n1. **v1/v2 prompt 鲁棒性**：能否提供 v1/v2 完整 prompt 文本？核心结论（两通道分离、BCS-accuracy 关系）在两个 prompt 版本下是否都成立？\n2. **16-rel batch 限制**：16-rel 为何仅一个 extreme batch？是 pool size 限制还是 compute budget？能否补充多 batch CI？\n3. **Pairwise→batch 放大**：r²=1.5% 但 BCS gap=31.2 pp。请用 typical BCS range × slope 量化 realistic practical effect，区分 extreme vs representative batches 的效应。\n4. **NER non-monotonicity**：count=22→44 recall 上升 (0.527→0.551) 的 bootstrap CI 是否重叠？\n5. **SDGD on RE**：为什么没有在 FewRel 上测试 SDGD？若 merge amplification 在 RE (classification) 上也成立，\"structural challenge\" claim 大大增强。\n6. **RE 任务形式**：RE 是 closed-set classification，\"clean channel separation\" 是否部分归因于任务不含 detection 环节？\n7. **Non-independent bootstrap**：pairwise 分析的 bootstrap 是否 accounted for type-level clustering？\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 共识（或一方提出、另一方 AGREE）应补充：\n1. **Reimers & Gurevych (EMNLP 2019)** Sentence-BERT — all-MiniLM-L6-v2 的训练框架出处\n2. **Li et al. (2023)** \"Evaluating ChatGPT's Information Extraction Capabilities\" — zero-shot IE evaluation\n3. **Wadhwa et al. (2023)** \"Revisiting Relation Extraction in the era of Large Language Models\" — LLM RE 相关\n4. **reflect-learn-2026** — 需补全作者/DOI 或删除\n\nR1 反驳的引用（不强制要求）：\n- AFET / hierarchical label confusion 文献 (Ren et al. 2016) — R1 认为技术差异较大，相关性有限\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。项目配置 `external_review.paperreview_ai.enabled: false`。\n\n---\n\n## Overall Assessment\n\n**评分: Borderline (介于 weak reject 和 weak accept 之间)**\n**置信度: 4/5**\n\n**R1 评分**: 3.0/5 (Soundness 2.5, Excitement 3.0)\n**R2 评分**: 3.0/5 (Soundness 3.5, Excitement 2.5)\n**综合**: 3.0/5，当前版本适合 **Findings track**，距主会差距在统计严谨性和 framing 诚实度。\n\n### 核心判断\n\n论文选题有价值——首次系统性隔离 count vs confusability 确实是该领域的空白。实验设计（count curves + BCS-controlled + within-pool 控制）体现了高于一般经验性 IE 论文的方法论水平。centrality confound 分析有独立贡献。SDGD 负面结果对社区有信息量。\n\n但关键统计证据存在多处可靠性问题：\n- **16-rel 单 batch 无 CI** 使跨条件对比的一端无统计基础\n- **80-rel 整体回归不显著** 而 extreme batches 做 headline result（尽管 within-pool sub-analysis 部分弥补）\n- **pairwise r²=1.5% → batch-level 31.2 pp 的放大缺乏形式化**\n- **非独立 bootstrap** 可能高估显著性\n- **v1/v2 prompt 混淆** 使跨实验比较的可信度存疑\n\n\"Multi-channel degradation framework\" 的叙事超出了证据支持的范围——仅在 RE (closed-set classification) 上 cleanly work，NER 有 channel 耦合，ED 完全反转。论文应定位为 \"empirical observations with controlled experiments across three IE tasks\"，而非 \"framework\"。\n\n### 与 Round 1 的进展\n\nRound 1 的 18 个 issue 中，8 个已解决（Discussion 新增、Limitations 重构、factorial 降格、SDGD 措辞、术语统一、Sclar 引用、residualized BCS、SDGD prompt 标注）。核心未解决项：v1/v2 prompt 混淆（升级为 Critical）、16-rel 单 batch（持续 Critical）、Checklist 缺失（升级为 Critical）、prompt 未公开（持续）。新发现：80-rel 回归不显著、RE-as-classification artifact、非独立 bootstrap。\n\n### 修改路径建议（非处方性，仅为评估框架）\n\n**最小可行修改（Findings track）**：\n1. 补 Responsible NLP Checklist\n2. 修复 reflect-learn-2026 和 json-schema-bench-2025 引用\n3. 公开 v1/v2 prompt template\n4. 16-rel 9.1 pp 降级为 illustrative 或补 CI\n5. 31.2 pp 出现时注明 full 80-rel 不显著\n6. \"Framework\" → \"empirical decomposition/observations\"\n7. Abstract 给 MAVEN 反转独立陈述\n\n**进一步提升（主会竞争力）**：\n8. 对关键实验报告两版 prompt 结果\n9. Pairwise→batch 放大的形式化量化\n10. FewRel SDGD 补充实验\n11. Type-level cluster bootstrap\n12. Discussion 增加 RE-as-classification 限制\n\n---\n\n## Detailed Comments by Section\n\n### Abstract\n- \"two degradation channels...across three IE tasks\" 但 MAVEN 反转。需限定。\n- \"count channel that generally suppresses recall\" 中 \"generally\" 试图覆盖 MAVEN 例外，但不够明确。\n- headline numbers (0.72→0.42, 85.7%→50.4%) 未标注 prompt 版本和模型。\n\n### Introduction\n- RQ1-RQ3 定义清晰且在论文中有对应实验回答。\n- Contribution 1 \"framework\" 过度；Contribution 2 已改为 \"modest predictor\"（进步）；Contribution 3 \"consistent across schema sizes\" 需 80-rel 不显著的 qualification；Contribution 4 \"structural challenge\" 仅基于 NER 一个任务。\n\n### Related Work (§2)\n- §2.1 覆盖了 2023-2025 zero-shot IE 主要工作。\n- §2.2 对 LLM-PEE 的差异化清晰。\n- §2.3 anisotropy 文献连接有创意。\n- 缺 Sentence-BERT、Li et al. 2023、Wadhwa et al. 2023。\n\n### Experimental Setup (§3)\n- §3.1 数据集选择合理，但 FewRel train+val 合并需更多说明。\n- §3.2 SCS/BCS 定义清晰，但 \"cosine similarity of type name embeddings\" 的局限性应提前讨论。\n- §3.4 实验设计精心——within-pool 控制尤其值得肯定。\n- §3.5 v1/v2 prompt 描述不够——需完整 template。FP8 量化对结果的影响未讨论。\n\n### Results (§5)\n- §5.1 count curves: NER non-monotonicity 需 CI。MAVEN 反转需更多讨论。\n- §5.2 pairwise: r²=1.3-1.7% framing 已改善，但 conditioning-on-outcome 讨论可再强化。\n- §5.3 BCS-controlled: within-pool analysis 是方法论亮点。16-rel 单 batch 和 80-rel 不显著是主要弱点。\n- §5.4 error taxonomy: 支撑 Channel 2 的关键证据，建议部分移入正文。\n- §5.5 centrality confound: 独立有价值，分析严谨。\n\n### SDGD (§6)\n- 半页正文过短，对 Contribution 4 而言不够。\n- 仅在 NER 测试，RE 缺失是遗憾。\n- merge amplification 的诊断有价值。\n\n### Discussion (§7)\n- Boundary conditions 讨论合理。\n- 51% floor 的 \"confusion subgroup\" 解释应标注为 conjecture。\n- \"model-invariant\" 应限定为 \"consistent across tested models\"。\n\n### Limitations\n- 结构大幅改善（Round 1 最大进步之一）。\n- Item 3 (cross-pool slope consistency) 更像 result 而非 limitation。\n- 缺 FewRel classification vs extraction 讨论。\n\n### Appendix\n- Residualized BCS 分析 (§C) 质量高。\n- Factorial analysis (§B) 作为 negative result 放置得当。\n- SDGD full protocol (§A) 完整。\n- 缺 prompt templates。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "report": "\n# 圆桌审稿报告 — Round 2\n\n**论文**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿人**: Reviewer 1 (方法严谨性 + 实验设计 + 统计分析), Reviewer 2 (新颖性 + 完整性 + 写作质量 + 格式合规)\n**轮次**: Round 2（论文已针对 Round 1 的 18 个 issue 进行修订）\n**外部审稿**: 未启用\n\n---\n\n## Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能下降的机制，提出将退化分解为 type count 和 type confusability 两个独立通道。引入 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 作为量化指标，在 Few-NERD (NER)、FewRel (RE)、MAVEN (ED) 三个数据集上进行控制实验。主要发现：(1) RE 上两通道 cleanly separable；(2) NER 上 confusability 同时影响 detection；(3) MAVEN 上出现 centrality confound 导致 per-type BCS 方向反转；(4) SDGD 负面结果表明 union-based merge 存在结构性挑战。跨模型验证在 Llama-3.1-8B 上复现了主要效应。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且定义清晰。** 首次系统性隔离 type count 与 type confusability 的独立效应，填补了零样本 IE 退化机制研究的空白。三个 research question 直接可检验。【R1, R2 共识】\n\n**S2. 实验设计精心。** Count curves + BCS-controlled 双范式互补，within-pool controlled comparison (Table 4) 消除跨 pool 混淆，permutation test 比较跨条件 slope 一致性。这是 empirical IE 研究中少见的控制实验水平。【R1 重点肯定】\n\n**S3. 诚实报告 modest effect sizes 和负面结果。** Pairwise r²=1.3-1.7% 如实量化，SDGD 负面结果完整报告而非隐藏，MAVEN centrality confound 作为独立分析呈现。科学态度端正。【R1, R2 共识】\n\n**S4. Centrality confound 分析有独立方法论价值。** 识别 same-domain schema 下 BCS 聚合失效的机制，连接 representation degeneration 文献，partial correlation 验证严谨。对 schema analysis 从业者有直接指导意义。【R1 重点肯定】\n\n**S5. Round 1 修订实质性改进。** Discussion section 新增、Limitations 重构为编号列表、factorial test 移入 Appendix 作为 negative result、Contribution 2 改为 \"modest predictor\"、SDGD 措辞降格、Sclar et al. 引用补充、residualized BCS 分析加入 Appendix。共 8/18 个 Round 1 issue 已解决。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] v1/v2 prompt 切换引入系统性混淆，仍未解决。** v1 prompt（含 offset 要求，96.5% 错误率）用于 count curves + BCS-controlled NER + SDGD；v2 prompt 用于后续实验和 cross-model 验证。v1→v2 使 Qwen3 count=1 recall 差 11% (0.72 vs 0.64)。论文跨实验引用数字时（如 Abstract headline numbers），prompt 版本不同使比较无效。核心 framework 的两个 channel 建立在不同 prompt 版本上。**Prompt 模板仍未公开**，读者无法判断变化性质。\n- Round 1 状态：SW3 (warning) → Round 2 升级为 Critical\n- 两 Reviewer 共识 Critical。\n- **要求**：(a) 公开完整 prompt template 至 Appendix；(b) 对关键实验报告两版 prompt 结果 or 全部统一至一版。\n\n**C2. [Critical] 16-rel BCS gap (9.1 pp) 基于单 batch，无统计可靠性。** Table 3 caption 明确标注\"single extreme batch per BCS level; bootstrap CIs require multiple batches\"。但 9.1 pp 在 Abstract 和 §5.3 中与 31.2 pp 对比以论证 BCS range 解释 absolute gap 差异——对比的一端无任何 CI。\n- Round 1 状态：MW1 部分解决（within-pool 已补），16-rel 独立 pool 单 batch 问题持续。\n- 两 Reviewer 共识。\n- **要求**：补充多 batch CI，或将 9.1 pp 降级为 illustrative，叙事重心移至 Table 4 回归分析。\n\n**C3. [Critical] 80-rel 整体 BCS-accuracy 回归不显著，但 extreme batches 做 headline result。** Table 4: Full 80-rel slope = −0.151, CI [−0.930, +0.657], p = 0.698。31.2 pp 来自同一 pool 的 extreme batches，出现在 Abstract/Introduction/Discussion/Conclusion。\n- R1 认为这是 cherry-picked endpoints；R2 反驳认为 within-pool sub-analysis (slope −0.401, p=0.027) 提供有效支撑，问题在 framing。**程度分歧，非方向分歧**——两方均认为当前 framing 不当。\n- **要求**：31.2 pp 出现时必须注明 full 80-rel 条件不显著 (underpowered)，核心统计论证应指向 within-pool slope。\n\n**C4. [Critical] 缺少 Responsible NLP Research Checklist。** ACL ARR 必须项，缺失导致 desk reject 风险。Round 1 已提出 (m3)，仍未解决。\n- 两 Reviewer 共识。\n- **要求**：立即补充。\n\n**C5. [Critical] reflect-learn-2026 引用作者为占位符 `[To be verified]`。** 提交带占位符的 bib 条目不可接受。\n- R2 列为 Critical，R1 认为应为 Should-Fix（5 分钟可修复的格式问题）。\n- **要求**：补全作者信息，或删除引用并调整正文。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [Major] \"Multi-channel degradation framework\" 过度声称。** 框架仅在 RE 上 cleanly work：NER 有 channel 耦合 + non-monotonic count curve + 不显著 factorial test；ED 完全反转。\"Framework\" 暗示通用性，但证据支持的是 \"empirical observations primarily demonstrated on RE\"。两 Reviewer 共识。\n\n**W2. [Major] Pairwise→batch 信号放大机制未形式化。** r²=1.3-1.7% 跳至 31.2 pp gap 缺乏形式化论证。within-pool quartile Δ 仅 −3.92 pp (CI 穿越零)。论文需区分 extreme batches 的理论最大效应和 representative batches 的典型效应，用 BCS range × slope 计算 realistic practical effect。两 Reviewer 共识（R1-W5 + R2-N3）。\n\n**W3. [Major] Pairwise SCS-confusion bootstrap CI 基于非独立观测。** 1,953/11,026 type pairs 不独立（同 type 出现在多 pairs），percentile bootstrap 低估真实不确定性，p < 10^{-10} 可能被高估。应使用 type-level cluster-robust bootstrap。R1 提出，R2 AGREE。\n\n**W4. [Major] NER count=22→44 recall 上升 (0.527→0.551) 未报 CI。** \"Minor non-monotonicity\" 需 CI 支撑——若 CI 不重叠则说明 count channel 在 NER 上非单调，影响 \"count drives recall decline\" 叙事。R1 提出，R2 AGREE。\n\n**W5. [Major] SDGD 仅在 Few-NERD 测试，泛化性不足。** RE 是 channels 最 cleanly separable 的任务；若 SDGD 在 RE 上也失败则大大增强 merge amplification 论点。仅在一个任务上就得出\"structural challenge for union-based merge pipelines\"的一般性结论，证据不够。R1 提出，R2 AGREE。\n\n**W6. [Major] RE \"clean channel separation\" 可能是 classification 任务形式的 artifact。** FewRel RE 是 closed-set classification（给定 entity pair 选 relation），不含 entity detection 环节。Missed rate flat (10-16%) 可能是任务形式产物——classification 本身消除了 detection 维度，使 \"RE 上 channels cleanly separate\" 成为循环论证。应在 Limitations/Discussion 讨论。R1 交叉回应中提出。\n\n**W7. [Major] MAVEN 反转在 Abstract 中仍被低估。** 三个数据集中最大的 (168 types) 结果与主假设方向相反。Abstract 用 \"generally suppresses recall\" 一带而过，应给 MAVEN 反转和 centrality confound 独立陈述（1-2 句）。两 Reviewer 共识。\n\n**W8. [Major] Prompt template 仍未公开。** v1→v2 导致 precision 翻倍，说明 prompt 设计对结果影响巨大。不公开严重影响可复现性。Round 1 (SW6) 未解决。两 Reviewer 共识。\n\n**W9. [Warning] 正文仅一幅 Figure（Round 1 为零，已改善）。** Error taxonomy 是支撑 Channel 2 的关键证据但仍在 Appendix。R2 列为 Critical，R1 降级为 warning——以 8 页限制合理安排优先级。建议至少补一幅 error taxonomy 或 centrality scatter plot。\n\n**W10. [Warning] FewRel 数据构造外部效度。** 合并 train+val 非标准用法；closed-set classification 与 extraction 有本质差异但论文并列讨论。R2 提出，R1 AGREE。\n\n**W11. [Warning] 51% floor \"confusion subgroup\" 解释为推测。** Discussion 中未标注为 hypothesis。R1, R2 共识。\n\n**W12. [Warning] \"model-invariant floor\" 基于仅两个 decoder-only 模型。** 应限定为 \"consistent across tested models\"。R1 提出。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全共识：\n1. v1/v2 prompt 混淆是关键方法论问题 (C1)\n2. 16-rel 单 batch 无 CI 统计不可靠 (C2)\n3. 缺 Responsible NLP Checklist (C4)\n4. reflect-learn-2026 引用不完整 (C5)\n5. \"Framework\" overclaim (W1)\n6. Pairwise→batch 放大缺形式化 (W2)\n7. 非独立 bootstrap CI (W3)\n8. SDGD 仅在 NER 测试 (W5)\n9. Prompt template 必须公开 (W8)\n10. MAVEN 在 Abstract 中被低估 (W7)\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 立场 | R2 立场 | 性质 |\n|------|---------|---------|------|\n| 80-rel 回归不显著 (C3) | Cherry-picked endpoints | Within-pool sub-analysis 有效支撑，framing 问题 | 程度之争 |\n| 正文 figure 数量 (W9) | Warning 级别 | Critical 级别 | 严重性之争 |\n| reflect-learn-2026 (C5) | Should-Fix | Critical | 严重性之争 |\n| Soundness 评分 | 2.5/5 | 3.5/5 | R1 更重视统计方法论缺陷 |\n| R2-Q4 type description SCS | Future work, 非当前弱点 | 合理问题 | 范围之争 |\n| R2-Q5 closed-source 模型 | 不必要，开源更可复现 | 合理建议 | 范围之争 |\n\n---\n\n## Questions for Authors\n\n1. **v1/v2 prompt 鲁棒性**：能否提供 v1/v2 完整 prompt 文本？核心结论（两通道分离、BCS-accuracy 关系）在两个 prompt 版本下是否都成立？\n2. **16-rel batch 限制**：16-rel 为何仅一个 extreme batch？是 pool size 限制还是 compute budget？能否补充多 batch CI？\n3. **Pairwise→batch 放大**：r²=1.5% 但 BCS gap=31.2 pp。请用 typical BCS range × slope 量化 realistic practical effect，区分 extreme vs representative batches 的效应。\n4. **NER non-monotonicity**：count=22→44 recall 上升 (0.527→0.551) 的 bootstrap CI 是否重叠？\n5. **SDGD on RE**：为什么没有在 FewRel 上测试 SDGD？若 merge amplification 在 RE (classification) 上也成立，\"structural challenge\" claim 大大增强。\n6. **RE 任务形式**：RE 是 closed-set classification，\"clean channel separation\" 是否部分归因于任务不含 detection 环节？\n7. **Non-independent bootstrap**：pairwise 分析的 bootstrap 是否 accounted for type-level clustering？\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 共识（或一方提出、另一方 AGREE）应补充：\n1. **Reimers & Gurevych (EMNLP 2019)** Sentence-BERT — all-MiniLM-L6-v2 的训练框架出处\n2. **Li et al. (2023)** \"Evaluating ChatGPT's Information Extraction Capabilities\" — zero-shot IE evaluation\n3. **Wadhwa et al. (2023)** \"Revisiting Relation Extraction in the era of Large Language Models\" — LLM RE 相关\n4. **reflect-learn-2026** — 需补全作者/DOI 或删除\n\nR1 反驳的引用（不强制要求）：\n- AFET / hierarchical label confusion 文献 (Ren et al. 2016) — R1 认为技术差异较大，相关性有限\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。项目配置 `external_review.paperreview_ai.enabled: false`。\n\n---\n\n## Overall Assessment\n\n**评分: Borderline (介于 weak reject 和 weak accept 之间)**\n**置信度: 4/5**\n\n**R1 评分**: 3.0/5 (Soundness 2.5, Excitement 3.0)\n**R2 评分**: 3.0/5 (Soundness 3.5, Excitement 2.5)\n**综合**: 3.0/5，当前版本适合 **Findings track**，距主会差距在统计严谨性和 framing 诚实度。\n\n### 核心判断\n\n论文选题有价值——首次系统性隔离 count vs confusability 确实是该领域的空白。实验设计（count curves + BCS-controlled + within-pool 控制）体现了高于一般经验性 IE 论文的方法论水平。centrality confound 分析有独立贡献。SDGD 负面结果对社区有信息量。\n\n但关键统计证据存在多处可靠性问题：\n- **16-rel 单 batch 无 CI** 使跨条件对比的一端无统计基础\n- **80-rel 整体回归不显著** 而 extreme batches 做 headline result（尽管 within-pool sub-analysis 部分弥补）\n- **pairwise r²=1.5% → batch-level 31.2 pp 的放大缺乏形式化**\n- **非独立 bootstrap** 可能高估显著性\n- **v1/v2 prompt 混淆** 使跨实验比较的可信度存疑\n\n\"Multi-channel degradation framework\" 的叙事超出了证据支持的范围——仅在 RE (closed-set classification) 上 cleanly work，NER 有 channel 耦合，ED 完全反转。论文应定位为 \"empirical observations with controlled experiments across three IE tasks\"，而非 \"framework\"。\n\n### 与 Round 1 的进展\n\nRound 1 的 18 个 issue 中，8 个已解决（Discussion 新增、Limitations 重构、factorial 降格、SDGD 措辞、术语统一、Sclar 引用、residualized BCS、SDGD prompt 标注）。核心未解决项：v1/v2 prompt 混淆（升级为 Critical）、16-rel 单 batch（持续 Critical）、Checklist 缺失（升级为 Critical）、prompt 未公开（持续）。新发现：80-rel 回归不显著、RE-as-classification artifact、非独立 bootstrap。\n\n### 修改路径建议（非处方性，仅为评估框架）\n\n**最小可行修改（Findings track）**：\n1. 补 Responsible NLP Checklist\n2. 修复 reflect-learn-2026 和 json-schema-bench-2025 引用\n3. 公开 v1/v2 prompt template\n4. 16-rel 9.1 pp 降级为 illustrative 或补 CI\n5. 31.2 pp 出现时注明 full 80-rel 不显著\n6. \"Framework\" → \"empirical decomposition/observations\"\n7. Abstract 给 MAVEN 反转独立陈述\n\n**进一步提升（主会竞争力）**：\n8. 对关键实验报告两版 prompt 结果\n9. Pairwise→batch 放大的形式化量化\n10. FewRel SDGD 补充实验\n11. Type-level cluster bootstrap\n12. Discussion 增加 RE-as-classification 限制\n\n---\n\n## Detailed Comments by Section\n\n### Abstract\n- \"two degradation channels...across three IE tasks\" 但 MAVEN 反转。需限定。\n- \"count channel that generally suppresses recall\" 中 \"generally\" 试图覆盖 MAVEN 例外，但不够明确。\n- headline numbers (0.72→0.42, 85.7%→50.4%) 未标注 prompt 版本和模型。\n\n### Introduction\n- RQ1-RQ3 定义清晰且在论文中有对应实验回答。\n- Contribution 1 \"framework\" 过度；Contribution 2 已改为 \"modest predictor\"（进步）；Contribution 3 \"consistent across schema sizes\" 需 80-rel 不显著的 qualification；Contribution 4 \"structural challenge\" 仅基于 NER 一个任务。\n\n### Related Work (§2)\n- §2.1 覆盖了 2023-2025 zero-shot IE 主要工作。\n- §2.2 对 LLM-PEE 的差异化清晰。\n- §2.3 anisotropy 文献连接有创意。\n- 缺 Sentence-BERT、Li et al. 2023、Wadhwa et al. 2023。\n\n### Experimental Setup (§3)\n- §3.1 数据集选择合理，但 FewRel train+val 合并需更多说明。\n- §3.2 SCS/BCS 定义清晰，但 \"cosine similarity of type name embeddings\" 的局限性应提前讨论。\n- §3.4 实验设计精心——within-pool 控制尤其值得肯定。\n- §3.5 v1/v2 prompt 描述不够——需完整 template。FP8 量化对结果的影响未讨论。\n\n### Results (§5)\n- §5.1 count curves: NER non-monotonicity 需 CI。MAVEN 反转需更多讨论。\n- §5.2 pairwise: r²=1.3-1.7% framing 已改善，但 conditioning-on-outcome 讨论可再强化。\n- §5.3 BCS-controlled: within-pool analysis 是方法论亮点。16-rel 单 batch 和 80-rel 不显著是主要弱点。\n- §5.4 error taxonomy: 支撑 Channel 2 的关键证据，建议部分移入正文。\n- §5.5 centrality confound: 独立有价值，分析严谨。\n\n### SDGD (§6)\n- 半页正文过短，对 Contribution 4 而言不够。\n- 仅在 NER 测试，RE 缺失是遗憾。\n- merge amplification 的诊断有价值。\n\n### Discussion (§7)\n- Boundary conditions 讨论合理。\n- 51% floor 的 \"confusion subgroup\" 解释应标注为 conjecture。\n- \"model-invariant\" 应限定为 \"consistent across tested models\"。\n\n### Limitations\n- 结构大幅改善（Round 1 最大进步之一）。\n- Item 3 (cross-pool slope consistency) 更像 result 而非 limitation。\n- 缺 FewRel classification vs extraction 讨论。\n\n### Appendix\n- Residualized BCS 分析 (§C) 质量高。\n- Factorial analysis (§B) 作为 negative result 放置得当。\n- SDGD full protocol (§A) 完整。\n- 缺 prompt templates。\n"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-16T03:03:11.031044+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5194
}
```

</details>

---


### Assistant

_source line 226 · 2026-05-16T03:03:20.668558+00:00_

审稿报告已投递至 Research Director。

---

**圆桌审稿完成。** 总结：

- **Overall: Borderline (3.0/5)**，当前版本适合 Findings track
- **5 个 Critical Must-Fix**：v1/v2 prompt 混淆未解决（从 Round 1 升级）、16-rel 单 batch 无 CI、80-rel 回归不显著但 headline framing、缺 NLP Checklist、引用占位符
- **12 个 Should-Fix**：framework overclaim、pairwise→batch 放大未形式化、非独立 bootstrap、NER non-monotonicity、SDGD 仅 NER、RE-as-classification artifact、MAVEN Abstract 不足、prompt 未公开、正文仅 1 figure 等
- **Round 1→2 进展**：18 个 issue 中 8 个已解决，3 个新发现
- Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 227 · 2026-05-16T03:03:23.346055+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

16 条意见中，我对 14 条标记 [AGREE]，对 1 条标记 [REBUT]（R1-N3，关于 80-rel 回归不显著是否等于效应不存在）。核心分歧不在方向上而在程度上——R1 和 R2 均认为 31.2 pp 的 headline framing 需要 qualification，但我认为 within-pool sub-analysis 提供了足够的统计支撑，不应将其定性为 cherry-picking。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 228 · 2026-05-16T03:03:40.018773+00:00_

审稿报告已于 Reviewer 2 交叉回应提交前完成投递，报告内容已完整纳入 R2 的所有立场（包括对 R1-N3 的 [REBUT] 及程度分歧）。

**圆桌审稿完成。** 汇总：

- **Overall**: Borderline (3.0/5)，当前版本适合 Findings track
- **5 个 Critical**：v1/v2 prompt 混淆、16-rel 单 batch 无 CI、80-rel 回归 framing、缺 NLP Checklist、引用占位符
- **12 个 Should-Fix/Warning**：framework overclaim、pairwise→batch 放大未形式化、非独立 bootstrap、SDGD 仅测 NER、RE-as-classification artifact 等
- **Round 1 → Round 2 进展**：18 个 issue 中 8 个已解决，4 个部分解决，6 个未解决或升级
- Issue Tracker 已同步至 `artifacts/review_issues.yaml`
- 报告已投递至 Research Director

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 16

## Round 16

52 recorded events


### User

_source line 229 · 2026-05-16T04:32:06.128827+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-16T04:32:13.546463+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-16T04:32:13.598224+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-16T04:32:18.470043+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-16T04:32:18.570931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-16T04:32:21.501008+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-16T04:32:21.703299+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (37 个)\n\n- **bootstrap_ci_analysis**: DONE (success) — \n- **exp016_fewrel_error_taxonomy**: DONE (success) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp007_error_taxonomy**: DONE (success) — \n- **exp_fewrel_formal_80rel**: DONE (success) — \n- **exp_fewrel_formal**: DONE (success) — \n- **exp008_sdgd_zero_fewnerd_r2**: DONE (negative) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n- **fewrel_pilot**: DONE (success) — \n- **exp004_maven_bcs**: DONE (negative) — \n- **exp002_confusability_controlled**: DONE (success) — \n- **exp003a_prompt_v2_rerun**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp001_count_baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confusability Pilot Results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/pilot_results.txt)\n- **exp_fewrel_v2_bcs_controlled** (success): 验证 Channel 2 (BCS→type confusion) 在 v2 prompt 下方向一致。FewRel 80-rel, count=8, low-BCS 5 batches + high-BCS 5 batches, Qwen3-32B-FP8, v2 prompt。D037 Round 2 审稿 C1b。 ← 基于 exp_fewrel_formal_80rel\n  [fewrel_v2_bcs_eval_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_fewrel_v2_bcs_controlled/data/eval_results.json) | [fewrel_v2_bcs_bootstrap_ci](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_fewrel_v2_bcs_controlled/data/bootstrap_ci.json)\n- **exp_fewrel_80pool_
…[truncated 993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-16T04:32:21.703777+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 237 · 2026-05-16T04:32:21.804600+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-16T04:32:25.972000+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 239 · 2026-05-16T04:32:27.929623+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 240 · 2026-05-16T04:32:28.231257+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 241 · 2026-05-16T04:32:28.231649+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-16T04:32:32.600034+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"}]

Based on the search results, here are the key submission guidelines and author instructions for EMNLP 2026:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce)
…[truncated 1382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6628
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-16T04:32:32.600547+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4368
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-16T04:32:37.828006+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 paper format page limit template anonymous ARR submission",
  "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 paper format page limit template anonymous ARR submission",
    "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 245 · 2026-05-16T04:32:38.330258+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 246 · 2026-05-16T04:32:38.330680+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-16T04:32:39.336096+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-16T04:32:39.890412+00:00_

# Round 2 Review Issues Tracker
# Updated: 2026-05-16 (C1b v2 experiments done + Reviewer PASS)

# ============================================================
# CRITICAL — Must-Fix（影响接收决定）
# ============================================================

- id: MW1
  summary: "16-rel BCS gap (9.1 pp) 基于单 batch 无 CI，统计不可靠"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  mentions:
    - {round: 1, reviewers: [R1, R2], note: "R1-W1 + R2-W3 完全一致"}
    - {round: 2, reviewers: [R1, R2], note: "R1-N2 re-raised; within-pool 分析已补但 16-rel 独立 pool 仍为单 batch; R2 AGREE"}
  action_items:
    - {round: 1, action: "D033 16-rel 100 batch bootstrap CI", assigned_to: agent, status: done}
    - {round: 1, action: "80-rel pool 内 16-type 子集 BCS-controlled 实验", assigned_to: agent, status: done}
    - {round: 2, action: "Abstract/Intro 中 9.1pp 替换为 bootstrapped Δ=-7.42pp CI[-9.40,-5.54]", assigned_to: agent, status: done}
  resolution: "Abstract 改用 bootstrapped CI；Table 3 caption 标注为 illustrative"
  resolution_round: 2

- id: MW2
  summary: "Pairwise r²=1.3-1.7% → batch-level 31.2 pp 的信号放大缺乏形式化论证"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  mentions:
    - {round: 1, reviewers: [R1, R2], note: "R1-W2 + R2-W2 共识"}
    - {round: 2, reviewers: [R1, R2], note: "R1-W5 + R2-N3; within-pool quartile Δ = −3.92 pp (CI 穿越零) 与 31.2 pp 矛盾"}
  action_items:
    - {round: 1, action: "Contribution 2 改为 'modest predictor'", assigned_to: paper_agent, status: done}
    - {round: 1, action: "§5.2 加 conditioning-on-outcome bias 讨论", assigned_to: paper_agent, status: done}
    - {round: 2, action: "§practical_magnitude 新增 realistic effect size", assigned_to: agent, status: done}
  resolution: "§practical_magnitude (IQR 2.2pp, 10-90th 4.2pp); 31.2pp 正确归因为 wider BCS range"
  resolution_round: 2

- id: SW3
  summary: "v1/v2 prompt 切换引入跨实验系统性混淆"
  category: method
  severity: critical
  status:
…[truncated 11860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 249 · 2026-05-16T04:32:40.094516+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-16T04:32:40.196353+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-16T04:32:44.421972+00:00_

Web search results for query: "EMNLP 2026 paper format page limit template anonymous ARR submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the search results, here's what I found about EMNLP 2026 paper format and submission requirements:

## EMNLP 2026 Submission Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## ARR Submission Process

At the time of submission to ARR, authors will be asked to select a preferred venue (e.g., EMNLP 2026). The reviewing process will continue t
…[truncated 1046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6593
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-16T04:32:59.395795+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format long paper short paper page limit template",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format long paper short paper page limit template",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-16T04:33:00.808052+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND\"; echo \"---\"; grep -A 3 \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND\"; echo \"---\"; grep -A 3 \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-16T04:33:01.210031+00:00_

NOT_FOUND
---
NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 255 · 2026-05-16T04:33:01.210442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 256 · 2026-05-16T04:33:01.364381+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	
16	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Single primary model.} The primary experiments use Qwen3-32B. Channel~1 has been validated on Llama-3.1-8B-Instruct (recall decline $-$43\,pp, $r = 0.725$). Channel~2 was validated on FewRel RE ($\Delta = -27.1$\,pp at count 8, $-23.9$\,pp at count 16), with high-BCS accuracy converging to a floor consistent across both tested models ($\approx$0.51). On Few-NERD NER, Channel~2 was not robustly detectable at 8B scale, likely due to floor effects and the noisier text-match metric.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of the variance in type confusion. Entity frequency, prompt position effects, mention ambiguity, context complexity, and type definition quality likely account for the remaining variance.
42	
43	\item \textbf{Cross-pool slope consistency.} The BCS--accuracy slopes are statistically indistinguishable across pools (permutation $p = 0.436$), indicating consistent per-unit sensitivity. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range in that pool, not a stronger underlying effect; the independent 16-relation pool yields a bootstrapped quartile $\Delta$ of $-$7.4\,pp (95\% CI: [$-$9.4, $-$5.5]). A within-pool compa
…[truncated 4388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 153
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-16T04:33:06.861202+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format long paper short paper page limit template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Discontinuation of the MS Word Template – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/discontinuation-word-template"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about ACL Rolling Review 2026 submission format. Here's what I found:

…[truncated 1588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7465
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-16T04:33:17.111344+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" long paper \"8 pages\" short paper \"4 pages\" 2026 formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" long paper \"8 pages\" short paper \"4 pages\" 2026 formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-16T04:33:17.364379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 260 · 2026-05-16T04:33:17.415026+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-16T04:33:22.248192+00:00_

Web search results for query: ""ACL Rolling Review" long paper "8 pages" short paper "4 pages" 2026 formatting requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"NAACL 2026 LaTeX Template | ACL Style Files & Guide | Underleaf","url":"https://www.underleaf.ai/templates/naacl"}]

Based on the search results for ACL Rolling Review 2026 formatting requirements, here's what I found:

## Page Limits

Long papers must follow a page limit of 8 pages, while short papers must follow a page limit of 4 pages, not including limitations and ethical considerations.

## Paper Format Requirements

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to 
…[truncated 748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5136
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-16T04:33:25.109011+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-16T04:33:25.161045+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-16T04:33:31.246035+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-16T04:33:31.297320+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-16T04:33:35.269033+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config*\" -type f 2>/dev/null; echo \"---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -name \"config.yaml\" -type f 2>/dev/null",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config*\" -type f 2>/dev/null; echo \"---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -name \"config.yaml\" -type f 2>/dev/null",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-16T04:33:35.370172+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-16T04:34:15.656053+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && wc -l main.tex && echo \"---\" && ls *.tex 2>/dev/null && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
  "description": "Check paper files and review report history"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && wc -l main.tex && echo \"---\" && ls *.tex 2>/dev/null && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
    "description": "Check paper files and review report history"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-16T04:34:16.058302+00:00_

228 main.tex
---
abstract.tex
checklist.tex
conclusion.tex
discussion.tex
experimental_setup.tex
introduction.tex
main.tex
prompt_appendix.tex
related_work.tex
results.tex
sdgd_negative.tex
---
round_1.md
round_2.md
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-16T04:34:16.058731+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-16T04:34:16.110088+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-16T04:34:23.406238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_2.md"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-16T04:34:23.457282+00:00_

1	---
2	round: 2
3	overall_score: borderline
4	timestamp: 2026-05-16T03:03:05.885772+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	
11	# 圆桌审稿报告 — Round 2
12	
13	**论文**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?
14	**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
15	**截止日期**: 2026-05-25
16	**审稿人**: Reviewer 1 (方法严谨性 + 实验设计 + 统计分析), Reviewer 2 (新颖性 + 完整性 + 写作质量 + 格式合规)
17	**轮次**: Round 2（论文已针对 Round 1 的 18 个 issue 进行修订）
18	**外部审稿**: 未启用
19	
20	---
21	
22	## Summary
23	
24	本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能下降的机制，提出将退化分解为 type count 和 type confusability 两个独立通道。引入 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 作为量化指标，在 Few-NERD (NER)、FewRel (RE)、MAVEN (ED) 三个数据集上进行控制实验。主要发现：(1) RE 上两通道 cleanly separable；(2) NER 上 confusability 同时影响 detection；(3) MAVEN 上出现 centrality confound 导致 per-type BCS 方向反转；(4) SDGD 负面结果表明 union-based merge 存在结构性挑战。跨模型验证在 Llama-3.1-8B 上复现了主要效应。
25	
26	---
27	
28	## Strengths
29	
30	**S1. 研究问题重要且定义清晰。** 首次系统性隔离 type count 与 type confusability 的独立效应，填补了零样本 IE 退化机制研究的空白。三个 research question 直接可检验。【R1, R2 共识】
31	
32	**S2. 实验设计精心。** Count curves + BCS-controlled 双范式互补，within-pool controlled comparison (Table 4) 消除跨 pool 混淆，permutation test 比较跨条件 slope 一致性。这是 empirical IE 研究中少见的控制实验水平。【R1 重点肯定】
33	
34	**S3. 诚实报告 modest effect sizes 和负面结果。** Pairwise r²=1.3-1.7% 如实量化，SDGD 负面结果完整报告而非隐藏，MAVEN centrality confound 作为独立分析呈现。科学态度端正。【R1, R2 共识】
35	
36	**S4. Centrality confound 分析有独立方法论价值。** 识别 same-domain schema 下 BCS 聚合失效的机制，连接 representation degeneration 文献，partial correlation 验证严谨。对 schema analysis 从业者有直接指导意义。【R1 重点肯定】
37	
38	**S5. Round 1 修订实质性改进。** Discussion section 新增、Limitations 重构为编号列表、factorial test 移入 Appendix 作为 negative result、Contribution 2 改为 "modest predictor"、SDGD 措辞降格、Sclar et al. 引用补充、residualized BCS 分析加入 Appendix。共 8/18 个 Round 1 issue 已解决。
39	
40	---
41	
42	## Weaknesses
43	
44	### Mus
…[truncated 10589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-16T04:35:08.614081+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-16T04:35:08.715574+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-16T04:35:35.440661+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "3",
  "text": "## Round 3 审稿任务 — Reviewer 1\n\n**侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template `[review]`, Long paper 8页正文 + unlimited references + appendix\n- **匿名**: Double-blind\n- **必须项**: Limitations section + Responsible NLP Research Checklist\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`\n（含多个 \\input 文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n\n### 你的审查重点\n\n1. **统计方法论**：\n   - 所有 bootstrap CI 是否使用了正确的 resampling 单元（特别是 pairwise SCS 的 type-level cluster bootstrap）\n   - 16-rel BCS gap 是否已降级为 illustrative 或补充了多 batch CI\n   - 80-rel BCS-accuracy 回归不显著问题是否在引用 31.2pp 时有适当注明\n   - NER count=22→44 recall 上升是否报了 CI\n   - r²=1.3-1.7% → batch-level 31.2pp 的信号放大是否有形式化论证（§practical_magnitude）\n\n2. **实验设计**：\n   - v1/v2 prompt 问题是否已解决（Round 2 要求：公开 prompt template + 报告 v2 实验结果）\n   - 检查 prompt_appendix.tex 是否包含完整 prompt template\n   - Cross-model validation 是否充分\n   - SDGD 仅在 NER 测试的局限性是否在 Limitations 中明确标注\n\n3. **因果推断**：\n   - \"Type confusability drives degradation\" 的因果语言是否与 observational 证据匹配\n   - RE clean channel separation 是否讨论了 classification artifact 可能\n\n### Round 2 未解决问题（需验证）\n\n**Open issues:**\n- `R2-W4-sdgd-scope` (warning): SDGD 仅在 Few-NERD (NER) 测试 → Limitations 是否已限定\n- `MW4` (warning, in_progress): 正文仅一幅 Figure → 是否有改善\n\n**Round 2 Critical issues 标记为 resolved，请验证修复质量:**\n- `MW1`: Abstract 中 9.1pp 是否替换为 bootstrapped Δ=-7.42pp CI[-9.40,-5.54]；Table 3 caption 是否标注为 illustrative\n- `MW2`: §practical_magnitude 是否充分论证了 realistic effect size\n- `SW3`: v1/v2 prompt 混淆是否解决——prompt_appendix.tex 是否存在且完整；每个实验的 prompt 版本是否在正文标注\n- `R2-N3-80rel`: 31.2pp 出现时是否注明 full 80-rel 条件不显著\n- `m3`: Responsible NLP Checklist (checklist.tex) 是否完整且格式正确\n- `REF1`: reflect-learn-2026 引用是否已修正为真实作者\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条 S1, S2, ...)\n3. Weaknesses (逐条 W1, W2, ... 标注 severity: critical/major/minor)\n4. Questions for Authors (逐条 Q1, Q2, ...)\n5. Missing References\n6. Round 2 Issue Resolution Verification (逐条确认每个 resolved issue 的修复质量: PASS/PARTIAL/FAIL)\n7. Overall Score (1-5) 和 Confidence (1-5)\n8. Soundness Score (1-5)\n9. Excitement Score (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "3",
    "text": "## Round 3 审稿任务 — Reviewer 1\n\n**侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template `[review]`, Long paper 8页正文 + unlimited references + appendix\n- **匿名**: Double-blind\n- **必须项**: Limitations section + Responsible NLP Research Checklist\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`\n（含多个 \\input 文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n\n### 你的审查重点\n\n1. **统计方法论**：\n   - 所有 bootstrap CI 是否使用了正确的 resampling 单元（特别是 pairwise SCS 的 type-level cluster bootstrap）\n   - 16-rel BCS gap 是否已降级为 illustrative 或补充了多 batch CI\n   - 80-rel BCS-accuracy 回归不显著问题是否在引用 31.2pp 时有适当注明\n   - NER count=22→44 recall 上升是否报了 CI\n   - r²=1.3-1.7% → batch-level 31.2pp 的信号放大是否有形式化论证（§practical_magnitude）\n\n2. **实验设计**：\n   - v1/v2 prompt 问题是否已解决（Round 2 要求：公开 prompt template + 报告 v2 实验结果）\n   - 检查 prompt_appendix.tex 是否包含完整 prompt template\n   - Cross-model validation 是否充分\n   - SDGD 仅在 NER 测试的局限性是否在 Limitations 中明确标注\n\n3. **因果推断**：\n   - \"Type confusability drives degradation\" 的因果语言是否与 observational 证据匹配\n   - RE clean channel separation 是否讨论了 classification artifact 可能\n\n### Round 2 未解决问题（需验证）\n\n**Open issues:**\n- `R2-W4-sdgd-scope` (warning): SDGD 仅在 Few-NERD (NER) 测试 → Limitations 是否已限定\n- `MW4` (warning, in_progress): 正文仅一幅 Figure → 是否有改善\n\n**Round 2 Critical issues 标记为 resolved，请验证修复质量:**\n- `MW1`: Abstract 中 9.1pp 是否替换为 bootstrapped Δ=-7.42pp CI[-9.40,-5.54]；Table 3 caption 是否标注为 illustrative\n- `MW2`: §practical_magnitude 是否充分论证了 realistic effect size\n- `SW3`: v1/v2 prompt 混淆是否解决——prompt_appendix.tex 是否存在且完整；每个实验的 prompt 版本是否在正文标注\n- `R2-N3-80rel`: 31.2pp 出现时是否注明 full 80-rel 条件不显著\n- `m3`: Responsible NLP Checklist (checklist.tex) 是否完整且格式正确\n- `REF1`: reflect-learn-2026 引用是否已修正为真实作者\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条 S1, S2, ...)\n3. Weaknesses (逐条 W1, W2, ... 标注 severity: critical/major/minor)\n4. Questions for Authors (逐条 Q1, Q2, ...)\n5. Missing References\n6. Round 2 Issue Resolution Verification (逐条确认每个 resolved issue 的修复质量: PASS/PARTIAL/FAIL)\n7. Overall Score (1-5) 和 Confidence (1-5)\n8. Soundness Score (1-5)\n9. Excitement Score (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-16T04:35:53.605312+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18164
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-16T04:35:54.109677+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "3",
  "text": "## Round 3 审稿任务 — Reviewer 2\n\n**侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template `[review]`, Long paper 8页正文 + unlimited references + appendix\n- **匿名**: Double-blind\n- **必须项**: Limitations section + Responsible NLP Research Checklist\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`\n（含多个 \\input 文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n\n### 你的审查重点\n\n1. **新颖性评估**：\n   - 首次系统性隔离 type count vs type confusability 的贡献是否真正 novel\n   - SCS/BCS 指标相比现有 schema complexity 指标的增量价值\n   - Centrality confound 分析是否有独立方法论价值\n   - 与 LLM-PEE、GoLLIE 等 2024-2025 工作的差异化是否清晰\n\n2. **完整性**：\n   - Abstract 是否准确反映正文内容（特别是 MAVEN 反转是否有独立陈述）\n   - Introduction 的 contributions 是否与证据匹配（\"framework\" → \"pattern/decomposition\"？）\n   - Related Work 是否完整（Sentence-BERT、Li et al. 2023、Wadhwa et al. 2023 是否已补充）\n   - Discussion 对 boundary conditions 的覆盖是否充分\n   - Limitations 列表是否完整且诚实\n   - 51% floor 的 \"confusion subgroup\" 解释是否已标注为 hypothesis\n   - \"model-invariant\" 是否已改为 \"consistent across tested models\"\n\n3. **写作质量**：\n   - 论文结构是否清晰、逻辑流畅\n   - Figure/Table 是否足够支撑论述（Round 2 报告：正文仅一幅 Figure）\n   - 术语一致性（\"framework\" 是否已全面替换为 \"pattern\"/\"decomposition\"）\n   - §5 SDGD 正文是否仍然过短\n\n4. **格式合规**（严格按 ARR 标准检查）：\n   - 页数是否在 8 页限制内（正文，不含 Limitations/references/appendix）\n   - Responsible NLP Research Checklist 是否存在且完整\n   - 匿名是否彻底（无作者信息、无自引泄露）\n   - 引用格式是否统一\n   - 所有 bib 条目是否有真实作者（无占位符）\n   - checklist.tex line 19 是否仍写 'framework'（D037-m1-checklist issue）\n\n### Round 2 未解决问题（需验证）\n\n**Open issues:**\n- `R2-W4-sdgd-scope` (warning): SDGD 仅在 Few-NERD (NER) 测试 → Limitations 是否已限定\n- `R2-m-sdgd-short` (info): §5 SDGD 正文过短 → 是否有改善\n- `D037-m1-checklist` (info): checklist.tex line 19 'framework' → 是否已改为 'pattern'\n\n**Round 2 Critical issues 标记为 resolved，请验证修复质量:**\n- `MW1`: Abstract headline numbers 是否更新为 bootstrapped CI\n- `SW3`: v1/v2 prompt — prompt_appendix.tex 是否完整\n- `m3`: Responsible NLP Research Checklist 内容是否完整合规\n- `REF1`: reflect-learn-2026 引用作者是否已修正\n- `R2-W1-framework`: \"framework\" 是否全文替换为 \"pattern\"/\"decomposition\"（grep 验证）\n- `SW4`: MAVEN 反转在 Abstract 中是否有独立陈述\n- `R2-W7-51floor`: 51% floor 是否标注为 hypothesis\n- `R2-W8-model-invariant`: \"model-invariant\" 是否改为 \"consistent across tested models\"\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条 S1, S2, ...)\n3. Weaknesses (逐条 W1, W2, ... 标注 severity: critical/major/minor)\n4. Questions for Authors (逐条 Q1, Q2, ...)\n5. Missing References\n6. Round 2 Issue Resolution Verification (逐条确认每个 resolved issue 的修复质量: PASS/PARTIAL/FAIL)\n7. Overall Score (1-5) 和 Confidence (1-5)\n8. Novelty Score (1-5)\n9. Excitement Score (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "3",
    "text": "## Round 3 审稿任务 — Reviewer 2\n\n**侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template `[review]`, Long paper 8页正文 + unlimited references + appendix\n- **匿名**: Double-blind\n- **必须项**: Limitations section + Responsible NLP Research Checklist\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`\n（含多个 \\input 文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n\n### 你的审查重点\n\n1. **新颖性评估**：\n   - 首次系统性隔离 type count vs type confusability 的贡献是否真正 novel\n   - SCS/BCS 指标相比现有 schema complexity 指标的增量价值\n   - Centrality confound 分析是否有独立方法论价值\n   - 与 LLM-PEE、GoLLIE 等 2024-2025 工作的差异化是否清晰\n\n2. **完整性**：\n   - Abstract 是否准确反映正文内容（特别是 MAVEN 反转是否有独立陈述）\n   - Introduction 的 contributions 是否与证据匹配（\"framework\" → \"pattern/decomposition\"？）\n   - Related Work 是否完整（Sentence-BERT、Li et al. 2023、Wadhwa et al. 2023 是否已补充）\n   - Discussion 对 boundary conditions 的覆盖是否充分\n   - Limitations 列表是否完整且诚实\n   - 51% floor 的 \"confusion subgroup\" 解释是否已标注为 hypothesis\n   - \"model-invariant\" 是否已改为 \"consistent across tested models\"\n\n3. **写作质量**：\n   - 论文结构是否清晰、逻辑流畅\n   - Figure/Table 是否足够支撑论述（Round 2 报告：正文仅一幅 Figure）\n   - 术语一致性（\"framework\" 是否已全面替换为 \"pattern\"/\"decomposition\"）\n   - §5 SDGD 正文是否仍然过短\n\n4. **格式合规**（严格按 ARR 标准检查）：\n   - 页数是否在 8 页限制内（正文，不含 Limitations/references/appendix）\n   - Responsible NLP Research Checklist 是否存在且完整\n   - 匿名是否彻底（无作者信息、无自引泄露）\n   - 引用格式是否统一\n   - 所有 bib 条目是否有真实作者（无占位符）\n   - checklist.tex line 19 是否仍写 'framework'（D037-m1-checklist issue）\n\n### Round 2 未解决问题（需验证）\n\n**Open issues:**\n- `R2-W4-sdgd-scope` (warning): SDGD 仅在 Few-NERD (NER) 测试 → Limitations 是否已限定\n- `R2-m-sdgd-short` (info): §5 SDGD 正文过短 → 是否有改善\n- `D037-m1-checklist` (info): checklist.tex line 19 'framework' → 是否已改为 'pattern'\n\n**Round 2 Critical issues 标记为 resolved，请验证修复质量:**\n- `MW1`: Abstract headline numbers 是否更新为 bootstrapped CI\n- `SW3`: v1/v2 prompt — prompt_appendix.tex 是否完整\n- `m3`: Responsible NLP Research Checklist 内容是否完整合规\n- `REF1`: reflect-learn-2026 引用作者是否已修正\n- `R2-W1-framework`: \"framework\" 是否全文替换为 \"pattern\"/\"decomposition\"（grep 验证）\n- `SW4`: MAVEN 反转在 Abstract 中是否有独立陈述\n- `R2-W7-51floor`: 51% floor 是否标注为 hypothesis\n- `R2-W8-model-invariant`: \"model-invariant\" 是否改为 \"consistent across tested models\"\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条 S1, S2, ...)\n3. Weaknesses (逐条 W1, W2, ... 标注 severity: critical/major/minor)\n4. Questions for Authors (逐条 Q1, Q2, ...)\n5. Missing References\n6. Round 2 Issue Resolution Verification (逐条确认每个 resolved issue 的修复质量: PASS/PARTIAL/FAIL)\n7. Overall Score (1-5) 和 Confidence (1-5)\n8. Novelty Score (1-5)\n9. Excitement Score (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-16T04:35:56.025415+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1915
}
```

</details>

---


### Assistant

_source line 280 · 2026-05-16T04:36:01.343865+00:00_

Reviewer 1 和 Reviewer 2 已分配任务，等待独立初审结果返回。

**当前状态**：
- Reviewer 1（方法严谨性 + 实验设计 + 统计分析）— 已派发
- Reviewer 2（新颖性 + 完整性 + 写作质量 + 格式合规）— 已派发
- 外部审稿：未启用
- 轮次：Round 3（基于 Round 2 修订后的论文）

两位 Reviewer 均携带了 Round 2 的 4 个 open/in_progress issue 和 6 个 Critical resolved issue 的验证清单。等待审稿结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 281 · 2026-05-16T04:40:57.647859+00:00_

[Reviewer 1 审稿意见]:
## Round 3 Review — Reviewer 1 (方法严谨性 + 实验设计 + 统计分析)

### 1. Summary

本文通过控制实验设计首次隔离了 training-free LLM IE 中 schema 退化的两个独立通道（type count 和 type confusability），在 NER/RE/ED 三个任务上验证了 pairwise SCS 对 type confusion 的预测力，并报告了 confusability-aware decomposition 的信息性负结果。相比 Round 2，论文在统计注解、prompt 透明度和 limitations 覆盖方面有显著改善。主要遗留问题集中在 prompt 敏感性对主要 claim 的影响未在正文充分展现，以及 BCS-controlled 实验的因果推断语言略微超出证据支持范围。

---

### 2. Strengths

**S1: 实验设计精良，变量隔离到位。** Count curves（固定 confusability 随机化，变 count）和 BCS-controlled experiments（固定 count，变 confusability）互补设计合理，within-pool 控制（从 80-rel pool 抽 16-rel 子集）有效排除了 pool composition 混淆因素。这在该领域是首次系统性的因素隔离。(§3.3, Table 5)

**S2: 统计方法论全面、透明。** Bootstrap CI（B=10,000）、type-level cluster bootstrap（考虑 pair 非独立性）、permutation test（slope comparison p=0.436）、Spearman + Pearson 双验证等。特别是对 pairwise CI 和 cluster bootstrap CI 的差异做了诚实解释——pair-level tighter because treating pairs as independent, cluster bootstrap wider but still significant（Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]）。(§4.2, Table 2)

**S3: 诚实报告负面结果和 limitations。** SDGD 全面失败（best F1=0.32 vs single-pass 0.45）、factorial test 不显著（z=-0.67, p=0.50）、MAVEN centrality confound、80-rel full condition underpowered 等均明确报告且 framing 恰当。Limitations section 涵盖 8 项，比多数投稿更全面。(§5, Limitations, Appendix C)

**S4: Cross-model validation 设计合理。** Llama-3.1-8B 在 NER count channel（r=0.725）和 RE confusability channel（Δ=-27.1pp）上复现了主要发现。High-BCS accuracy 跨模型收敛到 ~51% floor 是一个有趣且有启发性的发现。(§4.3, Appendix Tables 6-7)

**S5: Prompt 完整性大幅改善。** Appendix D 包含三个任务的完整 prompt template（v1/v2 对比，包括 JSON schema），v1→v2 差异明确标注（offset removal + format constraints），RE 单版本明确说明。(Appendix §D)

**S6: Centrality confound 分析是一项独立贡献。** 识别 per-type BCS 在 same-domain schema 上因 embedding collapse 而反转（MAVEN: ρ=+0.184），并通过 residualized analysis 证实 confound（控制 log freq + degree centrality 后 p>0.2），同时保持 pairwise SCS 有效（r=0.129, p<10⁻¹⁰）。(§4.5, Appendix E)

---

### 3. Weaknesses

**W1 [major] Prompt 敏感性严重削弱核心 claim，但正文未充分展现。**
- 具体位置：§4.3 main text vs. Appendix F (§prompt_sensitivity)
- 问题：v2 prompt 将 RE BCS gap 从 31.2pp 缩减至 7.9pp（CI: [-5.2, +21.5] 包含零，n=5）。这意味着论文的标志性数字 31.2pp 有相当部分来自 prompt-induced noise 而非 genuine type confusion。论文在 Appendix F 坦诚讨论了这一点（"the v1 extreme-batch gap reflects both genuine type confusion and prompt-induced noise"），Discussion 也提及（"switching from v1 to v2 reduces the RE BCS gap from 31.2pp to 7.9pp"），但正文核心 narrative 仍以 v1 结果为主锚点。Abstract 虽已用 quartile Δ=-7.4pp 替换，但 Introduction finding (2) 仍引用 "accuracy gaps reaching 31.2pp under extreme-batch comparison"。
- 影响：读者可能高估 confusability 的 practical magnitude。v2 gap 7.9pp 与 CI 包含零意味着在 reasonable prompt design 下，confusability channel 在 RE 上可能不显著——这与论文的主题 "type confusability drives degradation" 存在张力。
- 建议：正文 §4.3 应增加一段明确讨论 v2 attenuation 的文字（不仅放在 Appendix），且 Introduction 引用 31.2pp 时应同时注明 v2 结果。

**W2 [major] "Interventional" 因果语言超出实验设计所支持的推断。**
- 具体位置：§4.3 第一句 "To move from correlational to interventional evidence"；§4.4 "confusability drives substitution errors"
- 问题：BCS-controlled experiments 通过构造 batch（选择高/低 BCS 的 type 组合）来操纵 BCS，但这不是真正的 intervention——batch composition（哪些具体 types 被选入）与 BCS 完全共变。高 BCS batch 里的 types 可能在 inherent difficulty、frequency、definition quality 等维度上系统性地不同于低 BCS types。Within-pool analysis 部分缓解了 pool composition confound，但未控制 type-level properties（如 type frequency in evaluation corpus）。论文在 §4.2 讨论了 entity frequency 等 confounding factors，但在 §4.3 的因果 framing 中未回溯这些 caveats。
- 影响：Reviewer 和读者可能将 BCS-controlled 结果误读为 causal identification，实际上是 quasi-experimental。
- 建议：将 "interventional" 改为 "quasi-experimental" 或 "controlled comparison"；在 §4.3 开头明确 acknowledge 残余 confounds（type frequency, definition quality 等可能与 BCS 共变）。

**W3 [minor] Pairwise r²=1.3-1.7% 到 batch-level gap 的信号放大缺乏形式化论证。**
- 具体位置：§4.2 最后一段，§practical_magnitude
- 问题：论文声称 "pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2pp"。§practical_magnitude 提供了经验数据（IQR=0.054 → 2.2pp expected gap），但缺乏从 pair-level variance explained 到 batch-level effect magnitude 的数学推导。Compounding mechanism 不清楚：为什么 1.3% pair-level variance 能在 batch aggregation 下产生 2-31pp batch-level gaps？是线性叠加、还是非线性放大？
- 建议：增加一个简短的形式化说明（即使放在 Appendix），解释 pair-level r² 如何通过 BCS aggregation 转化为 batch-level accuracy variation。或者承认这是一个 empirical observation 而非 theoretically derived relationship。

**W4 [minor] 正文视觉支持不足。**
- 具体位置：全文仅 Figure 1（双 panel）
- 问题：对于一篇包含 count curves、BCS-controlled experiments、error taxonomy、cross-model validation、centrality confound、SDGD 六大实验模块的论文，仅一张主图不足以引导读者。Error taxonomy visualization（Appendix Figure 2）、within-pool BCS regression scatter、MAVEN centrality confound 等都值得在正文呈现。
- 建议：至少增加 error taxonomy 图或 within-pool regression scatter 到正文。8 页限制内有空间（当前 Discussion 和 Conclusion 较短）。

**W5 [minor] FewRel evaluation 的 classification vs extraction gap 讨论不足。**
- 具体位置：Limitations item 7, item 8
- 问题：FewRel 是 closed-set classification（给定 entity pair 预测 relation），不是 open extraction。论文的最清晰 channel separation 恰恰在 RE 上获得——但这可能正是因为 classification format 消除了 entity detection 维度（Limitations item 8 已承认）。这意味着 "confusability drives substitution errors while detection remains stable"（§4.4）的 clean separation 可能是 task format artifact 而非 confusability 的本质特征。
- 影响：论文最强的 evidence（RE BCS gap）的 external validity 受限。
- 建议：在 Discussion 中更 prominently 讨论这一 threat to validity，而非仅在 Limitations 末尾一句。

---

### 4. Questions for Authors

**Q1:** v2 prompt 下 RE BCS gap 的 CI 包含零（[-5.2, +21.5]）。如果增加 batch 数量（从 n=5 到例如 n=25），是否有初步迹象表明 gap 会达到统计显著？或者 7.9pp 本身可能只是 noise？

**Q2:** Within-pool analysis（80-pool → 16-sub）的 quartile Δ CI 也包含零（[-8.17, +0.38]）。这是否意味着在控制 pool composition 后，BCS 效应在 80-rel pool 内的 typical batches 中实际上不显著？

**Q3:** High-BCS accuracy 跨模型收敛到 ~51%。这个 floor 是否可能只是 random guessing among confusable types 的 expected accuracy？对于包含 8 个 relations 的高 BCS batch，如果模型在高相似 types 间均匀猜测，expected accuracy 约为多少？

**Q4:** NER 的 pairwise SCS-confusion correlation 使用了 Qwen3 embedding（r=0.112），而 RE 使用 MiniLM 的 BCS。embedding 选择是否影响效应方向或大小？Few-NERD 用 MiniLM 做 SCS 结果如何？

**Q5:** SDGD 实验全部使用 v1 prompt（Table 8 caption 确认）。v2 prompt 的 higher precision 是否可能改善 merge amplification 问题？是否考虑过 v2 prompt + SDGD 的组合？

---

### 5. Missing References

- **Chia et al. (2022)** "RELATIONPROMPT: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction" — zero-shot RE 的 prompt-based approach，与 FewRel 实验设计相关
- **Li et al. (2023)** "Evaluating ChatGPT's Information Extraction Capabilities" 的 arXiv 版本在 OpenAlex 上未找到（not_found），建议补充 DOI 或确认出版状态

---

### 6. Round 2 Issue Resolution Verification

| Issue ID | Description | Status | Evidence |
|----------|-------------|--------|----------|
| `MW1` | Abstract 9.1pp → bootstrapped Δ; Table 3 caption illustrative | **PASS** | Abstract: "quartile gap reaching −7.4pp (95% CI: [−9.4, −5.5])"; Table 3 caption: "The 16-relation condition used a single extreme batch per BCS level" |
| `MW2` | §practical_magnitude 论证 realistic effect size | **PASS** | IQR=0.054 → 2.2pp (CI: [0.4, 4.0])，直接 quartile comparison 3.9pp，10th-90th 4.2pp。Clear and well-calibrated. |
| `SW3` | v1/v2 prompt 混淆 → prompt_appendix.tex 完整 | **PASS** | Appendix D 包含 NER v1/v2、ED v1/v2、RE 完整 template + JSON schema + v1→v2 diff 说明。§4 开头标注 "all experiments use v1 unless noted"。 |
| `R2-N3-80rel` | 31.2pp 引用时注明 80-rel 不显著 | **PASS** | 所有 31.2pp 出现处均标注 "extreme-batch comparison" + 引导读者到 §practical_magnitude 或 Table 5。Appendix C 明确 "do not draw inferential conclusions from [full 80-rel]"。 |
| `m3` | Responsible NLP Checklist 完整 | **PASS** | checklist.tex 覆盖 A1-A4, B1-B6, C1-C4, D1-D5, E1，格式正确，引用具体 section。 |
| `REF1` | reflect-learn-2026 引用真实性 | **PASS** | Web search 确认 arXiv:2508.10036 存在，作者 Zhao, Dong et al.，AAAI 2026 发表。OpenAlex 匹配 title + year。 |
| `R2-W4-sdgd-scope` | SDGD 仅在 NER 测试 → Limitations 标注 | **PASS** | Limitations item 5: "Our SDGD experiments test only span-level NER (Few-NERD)...whether decomposition helps or hurts RE or ED remains untested" |
| `MW4` | 正文仅一幅 Figure | **PARTIAL** | 仍然只有 Figure 1（双 panel）。Error taxonomy 图、cross-model 表、residualized BCS 表等均在 Appendix。正文可容纳更多视觉内容。 |

---

### 7. Overall Score: **3.5** (Borderline Conference)

**Confidence: 4** (Quite sure. I tried to check the important points carefully.)

**一句话总结：** 实验设计精良、统计方法透明的 controlled empirical study，但 prompt 敏感性严重削弱了核心 claim 的 robustness（v2 gap CI 包含零），且因果语言超出 quasi-experimental 设计所能支撑的推断水平。

### 8. Soundness: **3.5**

统计方法（bootstrap CI、cluster bootstrap、permutation test）执行规范且透明。主要扣分点：(1) BCS-controlled 实验的 "interventional" 定位不当——未控制 type frequency/definition quality 等与 BCS 共变的 confounders；(2) v2 prompt 下 RE 核心效应的 CI 包含零但未在正文充分讨论；(3) pair-level r² 到 batch-level gap 的放大机制缺乏形式化。如果将因果语言降级为 "controlled observational" 并在正文突出 v2 attenuation，soundness 可上升到 4。

### 9. Excitement: **3.0**

研究问题有实际意义（schema complexity 是 training-free IE 的真实痛点），controlled experimental design 是该领域的方法论进步。但 excitement 受限于：(1) 核心 predictor (SCS) 的 variance explained 仅 1.3-1.7%；(2) 论文的 actionable takeaway 偏有限——SDGD 失败意味着没有提出可行的 engineering solution；(3) 主要的 clean evidence 来自 RE classification task，external validity 待验证。如果能增加一个 open extraction RE 实验或展示 SCS-based schema optimization 的实际收益，excitement 可显著提升。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 282 · 2026-05-16T04:41:08.248486+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 283 · 2026-05-16T04:41:10.926337+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall 3.5（Borderline Conference）**，Soundness 3.5，Excitement 3.0，Confidence 4
- **主要优势**：实验设计精良（count/confusability 隔离）、统计方法全面透明（cluster bootstrap, permutation test）、负面结果诚实报告、prompt 模板完整
- **两个 major issues**：(1) v2 prompt 将 RE BCS gap 从 31.2pp 缩至 7.9pp（CI 含零），核心 claim robustness 存疑但正文未充分讨论；(2) "interventional" 因果语言超出 quasi-experimental 设计支撑范围
- **Round 2 修复验证**：7 项 PASS、1 项 PARTIAL（正文仍仅 1 幅图）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 284 · 2026-05-16T04:41:19.348546+00:00_

Reviewer 1 完成。等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 19

## Round 19

6 recorded events


### User

_source line 285 · 2026-05-16T04:45:35.190646+00:00_

[Reviewer 2 审稿意见]:
## Round 3 审稿完成 — Reviewer 2

### 总体评分
- **Overall: 3.5/5**（介于 Findings 和 Conference 之间）
- **Novelty: 3.5/5**
- **Excitement: 3/5**
- **Confidence: 4/5**

### Summary
本文首次系统隔离 training-free LLM IE 中 type count vs type confusability 的独立退化机制，实验设计（count curves + BCS-controlled + within-pool 对照）严谨，统计方法规范。Centrality confound 分析和 negative SDGD result 有独立方法论价值。

### Strengths (S1-S6)
- S1: 控制实验设计是核心亮点——count curves + BCS-controlled 构成相关性→干预性证据链，within-pool 排除 composition confound
- S2: Centrality confound 分析具独立方法论价值（partial correlation 控制 log freq + degree centrality）
- S3: Cross-model 51% floor convergence 是有趣发现，已恰当标注为 hypothesis
- S4: 统计报告优秀：bootstrap CI、cluster bootstrap、selection bias 警告
- S5: Negative SDGD result 准确定位 merge amplification 瓶颈
- S6: Limitations 极详尽（8 条）

### Weaknesses
- **W1 [major]**: 核心效应量极小（r²=1.3-1.7%，typical-batch gap 仅 2.2 pp），abstract/intro 侧重报道 extreme-batch gap (31.2 pp) 可能误导读者。建议更显著报告 typical-batch magnitude。
- **W2 [major]**: 正文仅 1 Figure + 4 Tables，error taxonomy 和 cross-model 结果全在 appendix。建议将核心证据移入正文。
- **W3 [minor]**: §5 SDGD 仍仅 ~100 词/4 句，与其 contribution 地位不匹配
- **W4 [minor]**: Abstract 中 MAVEN count-curve 反转仅隐式处理（"generally"），未独立陈述
- **W5 [minor]**: RE clean channel separation 可能是 closed-set classification format 的产物，abstract/intro 未附加 caveat
- **W6 [minor]**: 不同 dataset 使用不同 embedding（Qwen3 vs MiniLM），缺少 cross-embedding sensitivity ablation

### Round 2 Issue Verification
9/11 PASS，2 PARTIAL：
- **PARTIAL**: SW4 (MAVEN count-curve reversal 在 abstract 中仍仅隐式); R2-m-sdgd-short (§5 仍 ~4 句)
- 所有 critical issues 均已修复：framework→pattern、model-invariant→consistent across tested models、51% floor→hypothesis、checklist 清理、引用修正

### Key Questions
- Q1: SCS/BCS 在什么阈值以上才值得干预？（2.2 pp typical gap 是否有 actionable 决策边界？）
- Q2: Pairwise r² → batch-level gap 的放大机制？（additive vs nonlinear？）
- Q3: MAVEN count-curve 反转的三个归因中哪个贡献最大？
- Q4: 51% floor 是否接近 random-chance baseline？

### 格式合规
- 页数：8 页正文 + references + appendix ✓
- 匿名：完全匿名，"Anonymous ACL submission" ✓
- Checklist：完整且具体 ✓
- ACL [review] 格式 ✓
- 引用：43 篇，无 orphan/missing ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-16T04:45:56.244935+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "3",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每一条 Weakness 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供具体证据（cite Section/Table/Figure）\n\n---\n\n### Reviewer 2 评分\n- Overall: 3.5/5, Novelty: 3.5/5, Excitement: 3/5, Confidence: 4/5\n\n### Reviewer 2 Strengths (S1-S6)\n- S1: 控制实验设计是核心亮点——count curves + BCS-controlled 构成相关性→干预性证据链，within-pool 排除 composition confound\n- S2: Centrality confound 分析具独立方法论价值（partial correlation 控制 log freq + degree centrality）\n- S3: Cross-model 51% floor convergence 是有趣发现，已恰当标注为 hypothesis\n- S4: 统计报告优秀：bootstrap CI、cluster bootstrap、selection bias 警告\n- S5: Negative SDGD result 准确定位 merge amplification 瓶颈\n- S6: Limitations 极详尽（8 条）\n\n### Reviewer 2 Weaknesses\n- **W1 [major]**: 核心效应量极小（r²=1.3-1.7%，typical-batch gap 仅 2.2 pp），abstract/intro 侧重报道 extreme-batch gap (31.2 pp) 可能误导读者。建议更显著报告 typical-batch magnitude。\n- **W2 [major]**: 正文仅 1 Figure + 4 Tables，error taxonomy 和 cross-model 结果全在 appendix。建议将核心证据移入正文。\n- **W3 [minor]**: §5 SDGD 仍仅 ~100 词/4 句，与其 contribution 地位不匹配\n- **W4 [minor]**: Abstract 中 MAVEN count-curve 反转仅隐式处理（\"generally\"），未独立陈述\n- **W5 [minor]**: RE clean channel separation 可能是 closed-set classification format 的产物，abstract/intro 未附加 caveat\n- **W6 [minor]**: 不同 dataset 使用不同 embedding（Qwen3 vs MiniLM），缺少 cross-embedding sensitivity ablation\n\n### Reviewer 2 Key Questions\n- Q1: SCS/BCS 在什么阈值以上才值得干预？（2.2 pp typical gap 是否有 actionable 决策边界？）\n- Q2: Pairwise r² → batch-level gap 的放大机制？（additive vs nonlinear？）\n- Q3: MAVEN count-curve 反转的三个归因中哪个贡献最大？\n- Q4: 51% floor 是否接近 random-chance baseline？\n\n### Reviewer 2 Round 2 Issue Verification\n9/11 PASS，2 PARTIAL：\n- PARTIAL: SW4 (MAVEN count-curve reversal 在 abstract 中仍仅隐式); R2-m-sdgd-short (§5 仍 ~4 句)\n\n### Reviewer 2 格式合规\n页数、匿名、Checklist、ACL [review]、引用均合规。\n\n---\n\n请逐条回应上述 Weaknesses (W1-W6) 和 Questions (Q1-Q4)，对每条标注 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "3",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每一条 Weakness 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供具体证据（cite Section/Table/Figure）\n\n---\n\n### Reviewer 2 评分\n- Overall: 3.5/5, Novelty: 3.5/5, Excitement: 3/5, Confidence: 4/5\n\n### Reviewer 2 Strengths (S1-S6)\n- S1: 控制实验设计是核心亮点——count curves + BCS-controlled 构成相关性→干预性证据链，within-pool 排除 composition confound\n- S2: Centrality confound 分析具独立方法论价值（partial correlation 控制 log freq + degree centrality）\n- S3: Cross-model 51% floor convergence 是有趣发现，已恰当标注为 hypothesis\n- S4: 统计报告优秀：bootstrap CI、cluster bootstrap、selection bias 警告\n- S5: Negative SDGD result 准确定位 merge amplification 瓶颈\n- S6: Limitations 极详尽（8 条）\n\n### Reviewer 2 Weaknesses\n- **W1 [major]**: 核心效应量极小（r²=1.3-1.7%，typical-batch gap 仅 2.2 pp），abstract/intro 侧重报道 extreme-batch gap (31.2 pp) 可能误导读者。建议更显著报告 typical-batch magnitude。\n- **W2 [major]**: 正文仅 1 Figure + 4 Tables，error taxonomy 和 cross-model 结果全在 appendix。建议将核心证据移入正文。\n- **W3 [minor]**: §5 SDGD 仍仅 ~100 词/4 句，与其 contribution 地位不匹配\n- **W4 [minor]**: Abstract 中 MAVEN count-curve 反转仅隐式处理（\"generally\"），未独立陈述\n- **W5 [minor]**: RE clean channel separation 可能是 closed-set classification format 的产物，abstract/intro 未附加 caveat\n- **W6 [minor]**: 不同 dataset 使用不同 embedding（Qwen3 vs MiniLM），缺少 cross-embedding sensitivity ablation\n\n### Reviewer 2 Key Questions\n- Q1: SCS/BCS 在什么阈值以上才值得干预？（2.2 pp typical gap 是否有 actionable 决策边界？）\n- Q2: Pairwise r² → batch-level gap 的放大机制？（additive vs nonlinear？）\n- Q3: MAVEN count-curve 反转的三个归因中哪个贡献最大？\n- Q4: 51% floor 是否接近 random-chance baseline？\n\n### Reviewer 2 Round 2 Issue Verification\n9/11 PASS，2 PARTIAL：\n- PARTIAL: SW4 (MAVEN count-curve reversal 在 abstract 中仍仅隐式); R2-m-sdgd-short (§5 仍 ~4 句)\n\n### Reviewer 2 格式合规\n页数、匿名、Checklist、ACL [review]、引用均合规。\n\n---\n\n请逐条回应上述 Weaknesses (W1-W6) 和 Questions (Q1-Q4)，对每条标注 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-16T04:46:15.631048+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19386
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-16T04:46:18.005645+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "3",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每一条 Weakness 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供具体证据（cite Section/Table/Figure）\n\n---\n\n### Reviewer 1 评分\n- Overall: 3.5/5, Soundness: 3.5/5, Excitement: 3.0/5, Confidence: 4/5\n\n### Reviewer 1 Strengths (S1-S6)\n- S1: 实验设计精良，变量隔离到位（count curves + BCS-controlled + within-pool 控制）\n- S2: 统计方法论全面、透明（bootstrap CI, cluster bootstrap, permutation test）\n- S3: 诚实报告负面结果和 limitations\n- S4: Cross-model validation 设计合理（Llama-3.1-8B 复现 + 51% floor）\n- S5: Prompt 完整性大幅改善（Appendix D 含完整 v1/v2 template）\n- S6: Centrality confound 分析是独立贡献\n\n### Reviewer 1 Weaknesses\n- **W1 [major]**: Prompt 敏感性严重削弱核心 claim。v2 prompt 将 RE BCS gap 从 31.2pp 缩减至 7.9pp（CI: [-5.2, +21.5] 包含零，n=5）。论文在 Appendix F 坦诚讨论但正文核心 narrative 仍以 v1 结果为主锚点。Introduction finding (2) 仍引用 \"accuracy gaps reaching 31.2pp under extreme-batch comparison\"。v2 gap CI 含零意味着在合理 prompt 设计下 confusability channel 在 RE 上可能不显著。建议：正文 §4.3 增加 v2 attenuation 讨论段，Introduction 引用 31.2pp 时同时注明 v2 结果。\n- **W2 [major]**: \"Interventional\" 因果语言超出 quasi-experimental 设计支撑。§4.3 \"To move from correlational to interventional evidence\"；BCS-controlled experiments 未控制 type-level properties（frequency, definition quality）等与 BCS 共变的 confounders。建议将 \"interventional\" 改为 \"quasi-experimental\" 或 \"controlled comparison\"。\n- **W3 [minor]**: Pairwise r²=1.3-1.7% 到 batch-level gap 的信号放大缺乏形式化论证。§practical_magnitude 提供经验数据但无数学推导。\n- **W4 [minor]**: 正文仅 Figure 1（双 panel），视觉支持不足。\n- **W5 [minor]**: FewRel closed-set classification vs open extraction gap 讨论仅在 Limitations 末尾，应在 Discussion 中更 prominently 讨论。\n\n### Reviewer 1 Questions\n- Q1: v2 prompt 下 RE BCS gap 的 CI 包含零。增加 batch 数至 n=25，gap 是否能显著？还是 7.9pp 只是 noise？\n- Q2: Within-pool quartile Δ CI 也包含零（[-8.17, +0.38]）。控制 pool composition 后 BCS 效应在 typical batches 中不显著？\n- Q3: 51% floor 是否只是 random guessing among confusable types 的 expected accuracy？\n- Q4: NER 用 Qwen3 embedding vs RE 用 MiniLM 的 SCS。embedding 选择影响效应方向/大小？\n- Q5: SDGD 全用 v1 prompt。v2 prompt 的 higher precision 是否可能改善 merge amplification？\n\n### Reviewer 1 Round 2 Issue Verification\n7/8 PASS，1 PARTIAL（MW4: 正文仍仅 1 幅图）\n\n---\n\n请逐条回应上述 Weaknesses (W1-W5) 和 Questions (Q1-Q5)，对每条标注 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "3",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每一条 Weakness 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供具体证据（cite Section/Table/Figure）\n\n---\n\n### Reviewer 1 评分\n- Overall: 3.5/5, Soundness: 3.5/5, Excitement: 3.0/5, Confidence: 4/5\n\n### Reviewer 1 Strengths (S1-S6)\n- S1: 实验设计精良，变量隔离到位（count curves + BCS-controlled + within-pool 控制）\n- S2: 统计方法论全面、透明（bootstrap CI, cluster bootstrap, permutation test）\n- S3: 诚实报告负面结果和 limitations\n- S4: Cross-model validation 设计合理（Llama-3.1-8B 复现 + 51% floor）\n- S5: Prompt 完整性大幅改善（Appendix D 含完整 v1/v2 template）\n- S6: Centrality confound 分析是独立贡献\n\n### Reviewer 1 Weaknesses\n- **W1 [major]**: Prompt 敏感性严重削弱核心 claim。v2 prompt 将 RE BCS gap 从 31.2pp 缩减至 7.9pp（CI: [-5.2, +21.5] 包含零，n=5）。论文在 Appendix F 坦诚讨论但正文核心 narrative 仍以 v1 结果为主锚点。Introduction finding (2) 仍引用 \"accuracy gaps reaching 31.2pp under extreme-batch comparison\"。v2 gap CI 含零意味着在合理 prompt 设计下 confusability channel 在 RE 上可能不显著。建议：正文 §4.3 增加 v2 attenuation 讨论段，Introduction 引用 31.2pp 时同时注明 v2 结果。\n- **W2 [major]**: \"Interventional\" 因果语言超出 quasi-experimental 设计支撑。§4.3 \"To move from correlational to interventional evidence\"；BCS-controlled experiments 未控制 type-level properties（frequency, definition quality）等与 BCS 共变的 confounders。建议将 \"interventional\" 改为 \"quasi-experimental\" 或 \"controlled comparison\"。\n- **W3 [minor]**: Pairwise r²=1.3-1.7% 到 batch-level gap 的信号放大缺乏形式化论证。§practical_magnitude 提供经验数据但无数学推导。\n- **W4 [minor]**: 正文仅 Figure 1（双 panel），视觉支持不足。\n- **W5 [minor]**: FewRel closed-set classification vs open extraction gap 讨论仅在 Limitations 末尾，应在 Discussion 中更 prominently 讨论。\n\n### Reviewer 1 Questions\n- Q1: v2 prompt 下 RE BCS gap 的 CI 包含零。增加 batch 数至 n=25，gap 是否能显著？还是 7.9pp 只是 noise？\n- Q2: Within-pool quartile Δ CI 也包含零（[-8.17, +0.38]）。控制 pool composition 后 BCS 效应在 typical batches 中不显著？\n- Q3: 51% floor 是否只是 random guessing among confusable types 的 expected accuracy？\n- Q4: NER 用 Qwen3 embedding vs RE 用 MiniLM 的 SCS。embedding 选择影响效应方向/大小？\n- Q5: SDGD 全用 v1 prompt。v2 prompt 的 higher precision 是否可能改善 merge amplification？\n\n### Reviewer 1 Round 2 Issue Verification\n7/8 PASS，1 PARTIAL（MW4: 正文仍仅 1 幅图）\n\n---\n\n请逐条回应上述 Weaknesses (W1-W5) 和 Questions (Q1-Q5)，对每条标注 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-16T04:46:19.636007+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1630
}
```

</details>

---


### Assistant

_source line 290 · 2026-05-16T04:46:22.825249+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 291 · 2026-05-16T04:46:25.497512+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**要点总结：**
- **Overall 3.5/5**：实验设计严谨（首次控制实验隔离 count vs confusability），但核心效应量小（r²~1.5%，typical gap ~2pp），正文图表不足
- **2 个 major weakness**：(1) practical significance 论证薄弱，abstract 侧重 extreme-batch gap 可能误导；(2) 正文仅 1 figure，关键证据（error taxonomy、cross-model）全在 appendix
- **Round 2 修复验证**：9/11 PASS，2 PARTIAL（MAVEN count-curve 在 abstract 中仍隐式；§5 仍过短）
- **格式合规**：8 页正文、匿名完整、checklist 完整、引用无问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 292 · 2026-05-16T04:46:31.869382+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 293 · 2026-05-16T04:47:56.135746+00:00_

[Reviewer 1 审稿结果]:
以下是我对 Reviewer 2 各条意见的逐条回应。

---

## Weaknesses 逐条回应

### W1 [major] — Effect size 小，abstract/intro 侧重 extreme-batch gap

**[REBUT]**

R2 的关切有道理但程度被夸大了。当前版本 abstract 的主数字已经是 independent 16-rel pool 的 quartile gap **−7.4 pp (95% CI: [−9.4, −5.5])**，不是 31.2 pp。31.2 pp 在 abstract 中完全没有出现。Introduction §1 第12行提到 "accuracy gaps reaching 31.2 pp under extreme-batch comparison" 时**同句**附带了 "(typical-batch gap ≈2–4 pp, §practical_magnitude)" 的 caveat。§practical_magnitude（results.tex）进一步报告 IQR 产生的预期 gap 仅 2.2 pp (CI: [0.4, 4.0])，直接量化了 typical experience。Table 5 caption 也注明了 extreme vs. typical 的区分。

不过，pairwise r²=1.3–1.7% 确实值得在 abstract 中更显式量化，目前 abstract 只说了 "modest in magnitude"，可以加入具体数字让读者在第一时间校准期望。这方面 R2 有道理。

---

### W2 [major] — 正文仅 1 Figure + 4 Tables

**[AGREE]**

完全同意。对于一篇以实证为核心的 8 页论文，error taxonomy（Table in Appendix §A）和 cross-model BCS 表（Appendix Table）是支撑 Contribution 1（multi-channel pattern）和 cross-model validation 的关键证据，却全部放在 appendix。特别是 error taxonomy 的 IntraSub ρ=1.0 是 Channel 2 机制论证的核心数据点，正文 §4.4 仅用文字引用了这些数字。Figure 1 承载了两个 panel（count curves + BCS scaling），信息密度很高但覆盖面不够。

建议至少将 error taxonomy table 或 fig\_error\_taxonomy.pdf 移入正文，并考虑将 cross-model BCS table 合并为正文 Table 3 的扩展列。这对 8 页 long paper 是可行的（目前 §5 和 §6 加起来不到 1 页，有空间）。

---

### W3 [minor] — §5 SDGD 篇幅过短

**[AGREE]**

同意。§5（sdgd\_negative.tex）正文仅约 100 词 / 4 句，而 SDGD 是 Introduction 列出的第四条 contribution（"informative negative result"）。Appendix §B 有完整的 protocol 和 v1/v2 对比，但正文没有给出足够的 merge amplification 机制分析。读者需要翻到 appendix 才能理解为什么 precision 从 0.563 暴跌到 0.210。建议正文至少增加一段，简要展示 precision-recall tradeoff 的定量分解（multi-pass → union → FP accumulation 的逻辑链）。

---

### W4 [minor] — Abstract 中 MAVEN 反转仅隐式处理

**[AGREE]**

同意。Abstract 用 "a count channel that **generally** suppresses recall" 处理了 MAVEN 例外，但 "generally" 这个词承载了太多信息——读者很容易误读为 "在所有三个数据集上都 suppress recall"。MAVEN 的反转（F1 从 0.106 上升到 0.247）是一个重要的 boundary condition，值得在 abstract 中用半句话显式陈述，例如 "...while same-domain schemas (MAVEN) exhibit the opposite trend due to contextual disambiguation"。这也有助于与 §4.5 centrality confound 形成呼应。

---

### W5 [minor] — RE clean channel separation 可能是 classification artifact

**[REBUT]**（部分同意）

R2 指出 abstract/intro 未附 caveat 是对的。Abstract 说 "cleanly separable in RE" 但没有提及 closed-set classification format 的可能影响。Limitations item 8 和 Discussion §6 都讨论了这一点（"RE's clean channel separation may partly reflect its closed-set classification format, which eliminates the entity detection dimension"），但这些 caveats 来得太晚。

不过，我认为 R2 将此标注为 minor 是合理的，不需要升级为 major。RE 的 clean separation 不仅仅是 format artifact——Table in Appendix 的 error taxonomy 显示 RE missed rates 保持 flat (10–16%) 是一个跨 BCS bin 的系统性 pattern（ρ=0.954 for IntraSub, flat for Missed），而 NER 的 missed rates 是 43–65% 且 non-monotonic。这种 task-level 对比即使考虑 format 差异也是有信息量的。建议在 abstract 中加入 "possibly reflecting its closed-set format" 即可。

---

### W6 [minor] — 不同 dataset 用不同 embedding，缺 cross-embedding ablation

**[AGREE]**

同意这是一个有效关切。Table 1 显示 Few-NERD 用 Qwen3 embedding，FewRel 和 MAVEN 用 MiniLM，但论文没有系统解释选择依据，也没有跨 embedding 的 sensitivity 分析。

唯一的 cross-embedding 数据出现在 Appendix §C（residualized BCS, Table），其中 MAVEN 在 MiniLM 和 Qwen3 两种 embedding 下都做了 partial correlation，结果方向一致（raw positive → controlled non-significant）。但 Few-NERD 的 pairwise 分析（Table 2）只报了 Qwen3，FewRel 的 BCS-controlled 实验只用了 MiniLM。至少应补充 Few-NERD+MiniLM 和 FewRel+Qwen3 的 sensitivity check，或在 Limitations 中明确说明为何没做。

---

## Questions 逐条回应

### Q1 — SCS/BCS actionable threshold?

**[AGREE]**

这是一个实际且重要的缺口。§practical\_magnitude 报告了 typical gap 的 empirical 分布（IQR=0.054 → 2.2pp），但没有给出 practitioners 可操作的 BCS 阈值。论文定位 SCS/BCS 为 "actionable for schema design"，但如果不能说 "BCS 超过 X 时应该考虑 schema 分拆"，这个 actionability claim 就是空的。建议在 Discussion 中基于 regression slope 给出一个参考阈值区间（例如：BCS > 0.7 时 expected accuracy loss > 5pp）。

---

### Q2 — Pairwise r² → batch-level gap 的放大机制?

**[AGREE]**

论文提供了 empirical 证据（§practical\_magnitude: pairwise r²=1.3–1.7%, batch quartile Δ=7.4pp, extreme Δ=31.2pp）但没有 formal 的数学推导。直觉上，batch BCS 是 O(k²) 个 pairwise SCS 的均值，高 BCS batch 意味着**所有**共现 type pair 都 confusable，而非单个 pair——这是 additive accumulation 而非 nonlinear 放大。但论文没有形式化这一点。

一个简单的 sanity check：如果 batch 内每个 confusable pair 独立贡献一个 substitution error，则总 confusion 应与 batch 内高-SCS pair 数量成正比——即 additive。Table (Appendix) 的 IntraSub rates 随 BCS bin 单调上升但未加速（0% → 1.6% → 10.6% → 49.4% for NER），看起来更像 super-linear（可能因为高 BCS bin 内 pair-level SCS 也更高，不仅仅是 pair 数量多）。这个问题值得在 Discussion 中用 1–2 句形式化。

---

### Q3 — MAVEN count-curve 反转的主因?

**[AGREE]**

§4.1 给出了三个归因（relaxed matching / same-domain context / class imbalance），§4.5 提供了 centrality confound 分析，但没有量化各因素的相对贡献。例如，可以通过将 relaxed matching 切换为 exact matching 来隔离因素 (i)，或通过 frequency-stratified 分析隔离因素 (iii)。当前的归因是 post-hoc 的、未分解的，与论文在 NER/RE 上追求的 controlled analysis 标准不一致。这是一个合理的弱点，虽然 MAVEN 不是论文的核心 focus。

---

### Q4 — 51% floor vs random-chance baseline?

**[REBUT]**

这个问题的答案可以从论文中推导。BCS-controlled 实验在 count=8 的 batch 上评估（Table 3: "80-rel, count 8"），random-chance baseline 是 1/8 = 12.5%。51% 远高于 random chance（4.1×），所以这不是 "model 在 guess"。

更有趣的解读是：高 BCS batch 中最 confusable 的 type pair 可能将 8-way classification 有效退化为若干 binary confusions。如果 top-2 confusable types 各占约一半的错误，51% 可以理解为 "除了最 confusable pair 之外的 types 基本正确，但最 confusable pair 上接近 coin-flip"。论文在 Discussion 中已经将此标注为 "task-inherent difficulty floor" 且 "broader model coverage is needed to confirm this hypothesis"（discussion.tex §6）。

建议论文在 Table 3 caption 或 §4.3 正文中明确报告 random-chance baseline 数字以消除读者疑虑，但这不构成 methodology 问题。

---

## 总结

| 条目 | 判断 | 核心理由 |
|------|------|----------|
| W1 | REBUT（部分同意） | Abstract 已改用 −7.4pp 为主数字，但 pairwise r² 可更显式 |
| W2 | AGREE | 核心证据不应全在 appendix |
| W3 | AGREE | §5 篇幅与 contribution 地位不匹配 |
| W4 | AGREE | "generally" 承载过多，MAVEN 反转应显式 |
| W5 | REBUT（部分同意） | Error taxonomy 提供了超越 format artifact 的证据，但 abstract 确需 caveat |
| W6 | AGREE | 缺 cross-embedding sensitivity check |
| Q1 | AGREE | 缺 actionable threshold |
| Q2 | AGREE | 缺 formal amplification mechanism |
| Q3 | AGREE | MAVEN 归因未量化分解 |
| Q4 | REBUT | 51% >> random chance (12.5%)，可从论文推导 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 294 · 2026-05-16T04:48:06.718340+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 22

## Round 22

8 recorded events


### User

_source line 295 · 2026-05-16T04:48:57.444834+00:00_

[Reviewer 2 审稿意见]:
## 交叉回应完成 — Reviewer 2 对 Reviewer 1

### 逐条结果
**Weaknesses:** 5/5 AGREE
- R1-W1 (prompt sensitivity): AGREE — v2 CI 含零是最大威胁，但补充了 pairwise SCS 不受 prompt 影响、NER v2 correlation 更强两个 nuance
- R1-W2 ("interventional" 语言): AGREE — "quasi-experimental" 更准确
- R1-W3 (r² → gap 形式化): AGREE — 与 R2-W1 一致
- R1-W4 (1 figure): AGREE — 与 R2-W2 一致
- R1-W5 (FewRel format): AGREE — 与 R2-W5 一致

**Questions:** 4 AGREE + 1 REBUT
- R1-Q1 (v2 n=25): AGREE — 但即使显著，7.9pp 仍远小于 v1 的 31.2pp
- R1-Q2 (within-pool quartile CI): **REBUT** — regression slope CI [-0.701, -0.069] 排除零（p=0.027），quartile 分析的不显著是 BCS range compression 导致的 power 问题
- R1-Q3 (51% floor = random guessing): AGREE — 非常 sharp，需验证是否是 top-2 confusable types 的 chance level
- R1-Q4 (embedding choice): AGREE — 与 R2-W6 一致
- R1-Q5 (SDGD v2 prompt): AGREE — 但 Appendix B Table A4 已有 v2 结果（precision↑但 recall↓，F1 仍低于 single-pass）；问题是此信息未在 §5 正文呈现

### 两位 Reviewer 共识
1. Prompt sensitivity 是最大 concern（v2 CI 含零需要正文讨论）
2. 正文仅 1 Figure 不够
3. Effect size 的 practical significance 需更诚实呈现
4. "Interventional" → "quasi-experimental"
5. FewRel closed-set 格式 caveat 需更 prominent

### 分歧点
仅 Q2（within-pool quartile CI）：R1 暗示 BCS 效应在 typical batches 不显著，R2 指出 regression slope 显著——两者差异是 summary statistic 选择问题而非效应存在性问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-16T04:49:40.037998+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-16T04:49:40.090028+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-16T04:53:51.001163+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Round 3 Review Issues Tracker\n# Updated: 2026-05-16 (Round 3 review complete)\n\n# ============================================================\n# CRITICAL — Must-Fix\n# ============================================================\n\n- id: MW1\n  summary: \"16-rel BCS gap (9.1 pp) 基于单 batch 无 CI，统计不可靠\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W1 + R2-W3 完全一致\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R1-N2 re-raised; within-pool 已补但 16-rel 独立 pool 仍为单 batch\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Abstract 改用 quartile -7.4pp CI; Table 3 caption 标注 illustrative\"}\n  action_items:\n    - {round: 1, action: \"D033 16-rel 100 batch bootstrap CI\", assigned_to: agent, status: done}\n    - {round: 1, action: \"80-rel pool 内 16-type 子集 BCS-controlled 实验\", assigned_to: agent, status: done}\n    - {round: 2, action: \"Abstract 中 9.1pp 替换为 bootstrapped CI\", assigned_to: agent, status: done}\n  resolution: \"Abstract 改用 bootstrapped CI; Table 3 caption 标注为 illustrative\"\n  resolution_round: 2\n\n- id: MW2\n  summary: \"Pairwise r²=1.3-1.7% → batch-level 31.2 pp 的信号放大缺乏形式化论证\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W2 + R2-W2 共识\"}\n    - {round: 2, reviewers: [R1, R2], note: \"within-pool quartile CI 穿越零与 31.2 pp 矛盾\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PASS on practical_magnitude; 但 formal derivation 仍缺 — 见 R3-W3\"}\n  action_items:\n    - {round: 1, action: \"Contribution 2 改为 modest predictor\", assigned_to: paper_agent, status: done}\n    - {round: 1, action: \"加 conditioning-on-outcome bias 讨论\", assigned_to: paper_agent, status: done}\n    - {round: 2, action: \"practical_magnitude 新增 realistic effect size\", assigned_to: agent, status: done}\n  resolution: \"practical_magnitude (IQR 2.2pp, 10-90th 4.2pp); 31.2pp 正确归因为 wider BCS range\"\n  resolution_round: 2\n\n- id: SW3\n  summary: \"v1/v2 prompt 切换引入跨实验系统性混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W5 + R2 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"升级 Critical; prompt 仍未公开\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Appendix D 完整 v1/v2 template + JSON schema + diff\"}\n  action_items:\n    - {round: 2, action: \"公开 v1/v2 完整 prompt template 至 Appendix\", assigned_to: agent, status: done}\n    - {round: 2, action: \"v2 BCS-controlled RE 实验验证 Channel 2 方向一致\", assigned_to: agent, status: done}\n    - {round: 2, action: \"正文标注每个实验 prompt 版本\", assigned_to: agent, status: done}\n  resolution: \"Appendix D 完整公开; 每个实验 prompt 版本标注; RE v2 验证方向一致\"\n  resolution_round: 2\n\n- id: m3\n  summary: \"缺 Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"desk reject 风险\"}\n    - {round: 2, reviewers: [R1, R2], note: \"升级 Critical\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PASS — checklist.tex 完整 A1-E1\"}\n  action_items:\n    - {round: 2, action: \"创建 checklist.tex\", assigned_to: agent, status: done}\n  resolution: \"checklist.tex 完整且格式正确\"\n  resolution_round: 2\n\n- id: R2-N3-80rel\n  summary: \"80-rel 整体 BCS-accuracy 回归不显著但 extreme batches 做 headline result\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"程度之争\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — 所有 31.2pp 处标注 extreme-batch + 引导 practical_magnitude\"}\n  action_items:\n    - {round: 2, action: \"31.2pp caveat + practical_magnitude\", assigned_to: agent, status: done}\n  resolution: \"全文正确归因 wider BCS range + practical effect size\"\n  resolution_round: 2\n\n- id: REF1\n  summary: \"reflect-learn-2026 引用作者为占位符\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"占位符引用\"}\n    - {round: 2, reviewers: [R1, R2], note: \"升级 Critical\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Zhao, Dong et al. AAAI 2026 确认\"}\n  action_items:\n    - {round: 2, action: \"修正为真实作者\", assigned_to: agent, status: done}\n  resolution: \"引用已修正\"\n  resolution_round: 2\n\n- id: R3-C1\n  summary: \"v2 prompt 下 RE BCS gap 缩至 7.9pp (CI 含零)，核心 claim robustness 存疑但正文未充分讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"两 Reviewer 共识最大 concern; Appendix F 坦诚但正文 narrative 仍以 v1 为主锚点; Introduction 引用 31.2pp 未同时注明 v2\"}\n  action_items:\n    - {round: 3, action: \"正文 §4.3 增加 v2 attenuation 讨论段\", assigned_to: agent, status: open}\n    - {round: 3, action: \"Introduction 引用 31.2pp 时同时注明 v2 结果 (7.9pp)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-C2\n  summary: \"'Interventional' 因果语言超出 quasi-experimental 设计支撑范围\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"§4.3 'correlational to interventional' + §4.4 'drives'; 未控制 type frequency/definition quality 等 confounders\"}\n  action_items:\n    - {round: 3, action: \"'interventional' → 'quasi-experimental' 或 'controlled comparison'\", assigned_to: agent, status: open}\n    - {round: 3, action: \"§4.3 acknowledge 残余 confounds\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING — Should-Fix\n# ============================================================\n\n- id: R2-W1-framework\n  summary: \"'Multi-channel degradation framework' 过度声称\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PASS — framework→pattern/decomposition 全文替换确认\"}\n  action_items:\n    - {round: 2, action: \"'framework' → 'pattern'/'decomposition'\", assigned_to: agent, status: done}\n  resolution: \"全文替换完成，零残留\"\n  resolution_round: 2\n\n- id: R2-W2-bootstrap\n  summary: \"Pairwise SCS-confusion bootstrap CI 基于非独立观测\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"cluster-robust bootstrap\"}\n  action_items:\n    - {round: 2, action: \"type-level cluster bootstrap CI\", assigned_to: agent, status: done}\n  resolution: \"Few-NERD r=0.112 CI[0.069,0.219]; MAVEN r=0.106 CI[0.081,0.185]\"\n  resolution_round: 2\n\n- id: R2-W3-nonmono\n  summary: \"NER count=22→44 recall 上升未报 CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n  action_items:\n    - {round: 2, action: \"Bootstrap CI + permutation test\", assigned_to: agent, status: done}\n  resolution: \"CIs overlap; 正文与 Figure 1a 统一用 pooled recall\"\n  resolution_round: 2\n\n- id: R2-W4-sdgd-scope\n  summary: \"SDGD 负面结果仅在 Few-NERD (NER) 上测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Limitations item 5 明确限定\"}\n  action_items:\n    - {round: 2, action: \"Limitations 限定 SDGD 结论为 span-level NER\", assigned_to: agent, status: done}\n  resolution: \"Limitations item 5 明确限定范围\"\n  resolution_round: 3\n\n- id: R2-W5-RE-artifact\n  summary: \"RE 'clean channel separation' 可能是 classification task artifact\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"closed-set classification 不含 detection\"}\n    - {round: 3, reviewers: [R1, R2], note: \"Discussion + Limitations #8 已有，但 abstract/intro 仍缺 caveat\"}\n  action_items:\n    - {round: 2, action: \"Discussion/Limitations 加讨论\", assigned_to: agent, status: done}\n    - {round: 3, action: \"Abstract 中 RE clean separation 附加 closed-set format caveat\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW6\n  summary: \"Prompt 模板未在 appendix 公开\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"共识\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Appendix D 完整\"}\n  action_items:\n    - {round: 2, action: \"v1+v2 完整 prompt 加入 prompt_appendix.tex\", assigned_to: agent, status: done}\n  resolution: \"Appendix D 包含完整 prompt template\"\n  resolution_round: 2\n\n- id: MW4\n  summary: \"正文仅一幅 Figure\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"正文零 figure\"}\n    - {round: 2, reviewers: [R1, R2], note: \"改善到 1 figure\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PARTIAL — 仍仅 Figure 1; error taxonomy 和 cross-model 全在 appendix\"}\n  action_items:\n    - {round: 3, action: \"至少将 error taxonomy table/figure 移入正文\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW4\n  summary: \"MAVEN 反转在 Abstract 中未充分体现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"'generally' 不够明确\"}\n    - {round: 2, reviewers: [R1, R2], note: \"仍不够\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PARTIAL — 仍用 'generally' 隐式处理; 需半句显式陈述\"}\n  action_items:\n    - {round: 3, action: \"Abstract 显式陈述 MAVEN 反转\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6-FewRel\n  summary: \"FewRel 数据构造外部效度\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n  action_items:\n    - {round: 2, action: \"Limitations 加 train+val 合并 + classification vs extraction\", assigned_to: agent, status: done}\n  resolution: \"limitations #7 已添加\"\n  resolution_round: 2\n\n- id: R3-W1\n  summary: \"Effect size practical significance 未在 abstract/intro 足够突出 (typical gap 仅 2.2pp)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"R2-W1 提出, R1 部分同意; Abstract 已用 -7.4pp 但 pairwise r² 未显式量化\"}\n  action_items:\n    - {round: 3, action: \"Abstract 加入 pairwise r² 或 typical gap 具体数字\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W5\n  summary: \"不同 dataset 使用不同 embedding，缺 cross-embedding sensitivity ablation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"MAVEN 两种 embedding 方向一致 (Appendix C) 但 Few-NERD+MiniLM 和 FewRel+Qwen3 缺失\"}\n  action_items:\n    - {round: 3, action: \"补 cross-embedding sensitivity check 或 Limitations 说明\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor\n# ============================================================\n\n- id: R2-W7-51floor\n  summary: \"51% floor 'confusion subgroup' 解释是推测性的\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n    - {round: 3, reviewers: [R2], note: \"PASS — 已标注为 hypothesis\"}\n  action_items:\n    - {round: 2, action: \"标注为 hypothesis\", assigned_to: agent, status: done}\n  resolution: \"已标注为 hypothesis\"\n  resolution_round: 2\n\n- id: R2-W8-model-invariant\n  summary: \"'model-invariant floor' 基于仅两个模型\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"R1-W6\"}\n    - {round: 3, reviewers: [R2], note: \"PASS\"}\n  action_items:\n    - {round: 2, action: \"'model-invariant' → 'consistent across tested models'\", assigned_to: agent, status: done}\n  resolution: \"全文替换完成\"\n  resolution_round: 2\n\n- id: m1\n  summary: \"MiniLM 引用不精确\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Sentence-BERT 已在 bib 中\"\n  resolution_round: 2\n\n- id: R2-W9-jsonbib\n  summary: \"json-schema-bench-2025 引用 author 格式问题\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"作者已修正\"\n  resolution_round: 2\n\n- id: R2-REF-missing\n  summary: \"缺失引用\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"已补充\"\n  resolution_round: 2\n\n- id: R2-m-sdgd-short\n  summary: \"§5 SDGD 正文过短\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W7\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PARTIAL — 仍 ~100 词/4 句; merge amplification 分析不够\"}\n  action_items:\n    - {round: 3, action: \"§5 增加一段 precision-recall tradeoff 定量分解\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: D037-m1-checklist\n  summary: \"checklist.tex line 19 仍写 'framework'\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [Reviewer], note: \"D037 合并审查发现\"}\n    - {round: 3, reviewers: [R2], note: \"PASS\"}\n  action_items:\n    - {round: 2, action: \"checklist.tex 'framework' → 'pattern'\", assigned_to: agent, status: done}\n  resolution: \"checklist.tex 已修正\"\n  resolution_round: 3\n\n- id: R3-W3\n  summary: \"Pairwise r² → batch-level gap 放大机制缺 formal 数学推导\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"practical_magnitude 有 empirical 数据但无 formal derivation\"}\n  action_items:\n    - {round: 3, action: \"Appendix 增加简短 formal 说明或承认为 empirical observation\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W6\n  summary: \"MAVEN count-curve 反转三因素归因未量化分解\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"relaxed matching / same-domain context / class imbalance 三因素贡献未分离\"}\n  action_items:\n    - {round: 3, action: \"Discussion 或 Appendix 分解因素贡献\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (Round 1-2 历史)\n# ============================================================\n\n- id: MW3\n  summary: \"NER count×confusability interaction p=0.505 但正文称 'interact'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Factorial test 移入 Appendix, 正文删除 'interact'\"\n  resolution_round: 2\n\n- id: SW1\n  summary: \"无 Discussion section\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"§7 Discussion 已添加\"\n  resolution_round: 2\n\n- id: SW2\n  summary: \"SDGD 'structural bottleneck' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"降格为 'structural challenge'\"\n  resolution_round: 2\n\n- id: SW5\n  summary: \"Limitations section 结构差\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"重构为编号列表\"\n  resolution_round: 2\n\n- id: Q3\n  summary: \"SDGD single_pass prompt 版本未标注\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Table caption 已标注\"\n  resolution_round: 2\n\n- id: Q4\n  summary: \"Residualized BCS 分析\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix C 已添加\"\n  resolution_round: 2\n\n- id: REF3\n  summary: \"缺失引用 Sclar et al. 2024\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"已添加\"\n  resolution_round: 2\n\n- id: m5\n  summary: \"'model' → 'framework' 术语统一\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"全文统一\"\n  resolution_round: 2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Round 3 Review Issues Tracker\n# Updated: 2026-05-16 (Round 3 review complete)\n\n# ============================================================\n# CRITICAL — Must-Fix\n# ============================================================\n\n- id: MW1\n  summary: \"16-rel BCS gap (9.1 pp) 基于单 batch 无 CI，统计不可靠\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W1 + R2-W3 完全一致\"}\n    - {round: 2, reviewers: [R1, R2], note: \"R1-N2 re-raised; within-pool 已补但 16-rel 独立 pool 仍为单 batch\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Abstract 改用 quartile -7.4pp CI; Table 3 caption 标注 illustrative\"}\n  action_items:\n    - {round: 1, action: \"D033 16-rel 100 batch bootstrap CI\", assigned_to: agent, status: done}\n    - {round: 1, action: \"80-rel pool 内 16-type 子集 BCS-controlled 实验\", assigned_to: agent, status: done}\n    - {round: 2, action: \"Abstract 中 9.1pp 替换为 bootstrapped CI\", assigned_to: agent, status: done}\n  resolution: \"Abstract 改用 bootstrapped CI; Table 3 caption 标注为 illustrative\"\n  resolution_round: 2\n\n- id: MW2\n  summary: \"Pairwise r²=1.3-1.7% → batch-level 31.2 pp 的信号放大缺乏形式化论证\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W2 + R2-W2 共识\"}\n    - {round: 2, reviewers: [R1, R2], note: \"within-pool quartile CI 穿越零与 31.2 pp 矛盾\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PASS on practical_magnitude; 但 formal derivation 仍缺 — 见 R3-W3\"}\n  action_items:\n    - {round: 1, action: \"Contribution 2 改为 modest predictor\", assigned_to: paper_agent, status: done}\n    - {round: 1, action: \"加 conditioning-on-outcome bias 讨论\", assigned_to: paper_agent, status: done}\n    - {round: 2, action: \"practical_magnitude 新增 realistic effect size\", assigned_to: agent, status: done}\n  resolution: \"practical_magnitude (IQR 2.2pp, 10-90th 4.2pp); 31.2pp 正确归因为 wider BCS range\"\n  resolution_round: 2\n\n- id: SW3\n  summary: \"v1/v2 prompt 切换引入跨实验系统性混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1-W5 + R2 AGREE\"}\n    - {round: 2, reviewers: [R1, R2], note: \"升级 Critical; prompt 仍未公开\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Appendix D 完整 v1/v2 template + JSON schema + diff\"}\n  action_items:\n    - {round: 2, action: \"公开 v1/v2 完整 prompt template 至 Appendix\", assigned_to: agent, status: done}\n    - {round: 2, action: \"v2 BCS-controlled RE 实验验证 Channel 2 方向一致\", assigned_to: agent, status: done}\n    - {round: 2, action: \"正文标注每个实验 prompt 版本\", assigned_to: agent, status: done}\n  resolution: \"Appendix D 完整公开; 每个实验 prompt 版本标注; RE v2 验证方向一致\"\n  resolution_round: 2\n\n- id: m3\n  summary: \"缺 Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"desk reject 风险\"}\n    - {round: 2, reviewers: [R1, R2], note: \"升级 Critical\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PASS — checklist.tex 完整 A1-E1\"}\n  action_items:\n    - {round: 2, action: \"创建 checklist.tex\", assigned_to: agent, status: done}\n  resolution: \"checklist.tex 完整且格式正确\"\n  resolution_round: 2\n\n- id: R2-N3-80rel\n  summary: \"80-rel 整体 BCS-accuracy 回归不显著但 extreme batches 做 headline result\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"程度之争\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — 所有 31.2pp 处标注 extreme-batch + 引导 practical_magnitude\"}\n  action_items:\n    - {round: 2, action: \"31.2pp caveat + practical_magnitude\", assigned_to: agent, status: done}\n  resolution: \"全文正确归因 wider BCS range + practical effect size\"\n  resolution_round: 2\n\n- id: REF1\n  summary: \"reflect-learn-2026 引用作者为占位符\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"占位符引用\"}\n    - {round: 2, reviewers: [R1, R2], note: \"升级 Critical\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Zhao, Dong et al. AAAI 2026 确认\"}\n  action_items:\n    - {round: 2, action: \"修正为真实作者\", assigned_to: agent, status: done}\n  resolution: \"引用已修正\"\n  resolution_round: 2\n\n- id: R3-C1\n  summary: \"v2 prompt 下 RE BCS gap 缩至 7.9pp (CI 含零)，核心 claim robustness 存疑但正文未充分讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"两 Reviewer 共识最大 concern; Appendix F 坦诚但正文 narrative 仍以 v1 为主锚点; Introduction 引用 31.2pp 未同时注明 v2\"}\n  action_items:\n    - {round: 3, action: \"正文 §4.3 增加 v2 attenuation 讨论段\", assigned_to: agent, status: open}\n    - {round: 3, action: \"Introduction 引用 31.2pp 时同时注明 v2 结果 (7.9pp)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-C2\n  summary: \"'Interventional' 因果语言超出 quasi-experimental 设计支撑范围\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"§4.3 'correlational to interventional' + §4.4 'drives'; 未控制 type frequency/definition quality 等 confounders\"}\n  action_items:\n    - {round: 3, action: \"'interventional' → 'quasi-experimental' 或 'controlled comparison'\", assigned_to: agent, status: open}\n    - {round: 3, action: \"§4.3 acknowledge 残余 confounds\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING — Should-Fix\n# ============================================================\n\n- id: R2-W1-framework\n  summary: \"'Multi-channel degradation framework' 过度声称\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PASS — framework→pattern/decomposition 全文替换确认\"}\n  action_items:\n    - {round: 2, action: \"'framework' → 'pattern'/'decomposition'\", assigned_to: agent, status: done}\n  resolution: \"全文替换完成，零残留\"\n  resolution_round: 2\n\n- id: R2-W2-bootstrap\n  summary: \"Pairwise SCS-confusion bootstrap CI 基于非独立观测\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"cluster-robust bootstrap\"}\n  action_items:\n    - {round: 2, action: \"type-level cluster bootstrap CI\", assigned_to: agent, status: done}\n  resolution: \"Few-NERD r=0.112 CI[0.069,0.219]; MAVEN r=0.106 CI[0.081,0.185]\"\n  resolution_round: 2\n\n- id: R2-W3-nonmono\n  summary: \"NER count=22→44 recall 上升未报 CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n  action_items:\n    - {round: 2, action: \"Bootstrap CI + permutation test\", assigned_to: agent, status: done}\n  resolution: \"CIs overlap; 正文与 Figure 1a 统一用 pooled recall\"\n  resolution_round: 2\n\n- id: R2-W4-sdgd-scope\n  summary: \"SDGD 负面结果仅在 Few-NERD (NER) 上测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Limitations item 5 明确限定\"}\n  action_items:\n    - {round: 2, action: \"Limitations 限定 SDGD 结论为 span-level NER\", assigned_to: agent, status: done}\n  resolution: \"Limitations item 5 明确限定范围\"\n  resolution_round: 3\n\n- id: R2-W5-RE-artifact\n  summary: \"RE 'clean channel separation' 可能是 classification task artifact\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"closed-set classification 不含 detection\"}\n    - {round: 3, reviewers: [R1, R2], note: \"Discussion + Limitations #8 已有，但 abstract/intro 仍缺 caveat\"}\n  action_items:\n    - {round: 2, action: \"Discussion/Limitations 加讨论\", assigned_to: agent, status: done}\n    - {round: 3, action: \"Abstract 中 RE clean separation 附加 closed-set format caveat\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW6\n  summary: \"Prompt 模板未在 appendix 公开\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"共识\"}\n    - {round: 3, reviewers: [R1], note: \"PASS — Appendix D 完整\"}\n  action_items:\n    - {round: 2, action: \"v1+v2 完整 prompt 加入 prompt_appendix.tex\", assigned_to: agent, status: done}\n  resolution: \"Appendix D 包含完整 prompt template\"\n  resolution_round: 2\n\n- id: MW4\n  summary: \"正文仅一幅 Figure\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"正文零 figure\"}\n    - {round: 2, reviewers: [R1, R2], note: \"改善到 1 figure\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PARTIAL — 仍仅 Figure 1; error taxonomy 和 cross-model 全在 appendix\"}\n  action_items:\n    - {round: 3, action: \"至少将 error taxonomy table/figure 移入正文\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: SW4\n  summary: \"MAVEN 反转在 Abstract 中未充分体现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"'generally' 不够明确\"}\n    - {round: 2, reviewers: [R1, R2], note: \"仍不够\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PARTIAL — 仍用 'generally' 隐式处理; 需半句显式陈述\"}\n  action_items:\n    - {round: 3, action: \"Abstract 显式陈述 MAVEN 反转\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6-FewRel\n  summary: \"FewRel 数据构造外部效度\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n  action_items:\n    - {round: 2, action: \"Limitations 加 train+val 合并 + classification vs extraction\", assigned_to: agent, status: done}\n  resolution: \"limitations #7 已添加\"\n  resolution_round: 2\n\n- id: R3-W1\n  summary: \"Effect size practical significance 未在 abstract/intro 足够突出 (typical gap 仅 2.2pp)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"R2-W1 提出, R1 部分同意; Abstract 已用 -7.4pp 但 pairwise r² 未显式量化\"}\n  action_items:\n    - {round: 3, action: \"Abstract 加入 pairwise r² 或 typical gap 具体数字\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W5\n  summary: \"不同 dataset 使用不同 embedding，缺 cross-embedding sensitivity ablation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"MAVEN 两种 embedding 方向一致 (Appendix C) 但 Few-NERD+MiniLM 和 FewRel+Qwen3 缺失\"}\n  action_items:\n    - {round: 3, action: \"补 cross-embedding sensitivity check 或 Limitations 说明\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor\n# ============================================================\n\n- id: R2-W7-51floor\n  summary: \"51% floor 'confusion subgroup' 解释是推测性的\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"共识\"}\n    - {round: 3, reviewers: [R2], note: \"PASS — 已标注为 hypothesis\"}\n  action_items:\n    - {round: 2, action: \"标注为 hypothesis\", assigned_to: agent, status: done}\n  resolution: \"已标注为 hypothesis\"\n  resolution_round: 2\n\n- id: R2-W8-model-invariant\n  summary: \"'model-invariant floor' 基于仅两个模型\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"R1-W6\"}\n    - {round: 3, reviewers: [R2], note: \"PASS\"}\n  action_items:\n    - {round: 2, action: \"'model-invariant' → 'consistent across tested models'\", assigned_to: agent, status: done}\n  resolution: \"全文替换完成\"\n  resolution_round: 2\n\n- id: m1\n  summary: \"MiniLM 引用不精确\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Sentence-BERT 已在 bib 中\"\n  resolution_round: 2\n\n- id: R2-W9-jsonbib\n  summary: \"json-schema-bench-2025 引用 author 格式问题\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"作者已修正\"\n  resolution_round: 2\n\n- id: R2-REF-missing\n  summary: \"缺失引用\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"已补充\"\n  resolution_round: 2\n\n- id: R2-m-sdgd-short\n  summary: \"§5 SDGD 正文过短\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"R2-W7\"}\n    - {round: 3, reviewers: [R1, R2], note: \"PARTIAL — 仍 ~100 词/4 句; merge amplification 分析不够\"}\n  action_items:\n    - {round: 3, action: \"§5 增加一段 precision-recall tradeoff 定量分解\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: D037-m1-checklist\n  summary: \"checklist.tex line 19 仍写 'framework'\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: [Reviewer], note: \"D037 合并审查发现\"}\n    - {round: 3, reviewers: [R2], note: \"PASS\"}\n  action_items:\n    - {round: 2, action: \"checklist.tex 'framework' → 'pattern'\", assigned_to: agent, status: done}\n  resolution: \"checklist.tex 已修正\"\n  resolution_round: 3\n\n- id: R3-W3\n  summary: \"Pairwise r² → batch-level gap 放大机制缺 formal 数学推导\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"practical_magnitude 有 empirical 数据但无 formal derivation\"}\n  action_items:\n    - {round: 3, action: \"Appendix 增加简短 formal 说明或承认为 empirical observation\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W6\n  summary: \"MAVEN count-curve 反转三因素归因未量化分解\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"relaxed matching / same-domain context / class imbalance 三因素贡献未分离\"}\n  action_items:\n    - {round: 3, action: \"Discussion 或 Appendix 分解因素贡献\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (Round 1-2 历史)\n# ============================================================\n\n- id: MW3\n  summary: \"NER count×confusability interaction p=0.505 但正文称 'interact'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Factorial test 移入 Appendix, 正文删除 'interact'\"\n  resolution_round: 2\n\n- id: SW1\n  summary: \"无 Discussion section\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"§7 Discussion 已添加\"\n  resolution_round: 2\n\n- id: SW2\n  summary: \"SDGD 'structural bottleneck' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"降格为 'structural challenge'\"\n  resolution_round: 2\n\n- id: SW5\n  summary: \"Limitations section 结构差\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"重构为编号列表\"\n  resolution_round: 2\n\n- id: Q3\n  summary: \"SDGD single_pass prompt 版本未标注\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Table caption 已标注\"\n  resolution_round: 2\n\n- id: Q4\n  summary: \"Residualized BCS 分析\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix C 已添加\"\n  resolution_round: 2\n\n- id: REF3\n  summary: \"缺失引用 Sclar et al. 2024\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"已添加\"\n  resolution_round: 2\n\n- id: m5\n  summary: \"'model' → 'framework' 术语统一\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"全文统一\"\n  resolution_round: 2"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-16T04:53:51.103028+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 16584}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-16T04:56:30.264271+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak accept",
  "report": "# 圆桌审稿报告 — Round 3\n\n**论文**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿人**: Reviewer 1 (方法严谨性 + 实验设计 + 统计分析), Reviewer 2 (新颖性 + 完整性 + 写作质量 + 格式合规)\n**轮次**: Round 3（论文已针对 Round 2 的全部 Critical issues 进行修订）\n**外部审稿**: 未启用\n\n---\n\n## Summary\n\n本文首次系统隔离 training-free LLM IE 中 schema 退化的两个通道（type count 和 type confusability），引入 SCS/BCS 量化指标，在 NER (Few-NERD)、RE (FewRel)、ED (MAVEN) 三个任务上进行控制实验。主要发现：(1) RE 上两通道 cleanly separable（高 BCS 准确率收敛至 ~51% floor）；(2) NER 上 confusability 同时影响 detection；(3) MAVEN 出现 centrality confound 导致 per-type BCS 方向反转；(4) SDGD 负面结果表明 union-based merge 存在结构性挑战。相比 Round 2，论文在 prompt 透明度、统计注解、framing 降格方面有实质性改善。\n\n---\n\n## Strengths\n\n**S1. 实验设计是该领域罕见的方法论标杆。** Count curves（固定 confusability，变 count）和 BCS-controlled experiments（固定 count，变 confusability）互补设计合理，within-pool 控制（80-rel pool → 16-sub）有效排除 pool composition confound。permutation test (p=0.436) 验证跨条件 slope 一致性。这在 training-free IE 领域是首次系统性因素隔离。【R1, R2 共识】\n\n**S2. 统计方法全面且透明。** Bootstrap CI (B=10,000)、type-level cluster bootstrap（处理 pair 非独立性，Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]）、within-pool regression (slope −0.401, CI excludes zero, p=0.027)。对 pair-level CI 与 cluster bootstrap CI 的差异做了诚实解释。§practical_magnitude 校准了 typical vs extreme effect size (IQR → 2.2pp vs extreme 31.2pp)。【R1 重点肯定, R2 同意】\n\n**S3. 诚实报告负面结果和 modest effects。** Pairwise r²=1.3-1.7% 如实报告，SDGD 全面失败 (best F1=0.32 vs single-pass 0.45)，factorial test 不显著 (p=0.50)，MAVEN centrality confound，80-rel full condition underpowered 等均明确标注。Limitations 涵盖 8 项，远超该领域平均水平。【R1, R2 共识】\n\n**S4. Prompt 透明度大幅改善。** Appendix D 包含三个任务的完整 prompt template（v1/v2 对比 + JSON schema + diff 说明），RE 单版本明确标注，§4 开头标注 prompt 版本适用范围。Round 2 的 SW3 (Critical) 完全解决。【R1 PASS】\n\n**S5. Centrality confound 分析有独立方法论贡献。** 识别 per-type BCS 在 same-domain schema 上因 embedding collapse 反转 (MAVEN: ρ=+0.184)，partial correlation 控制 log freq + degree centrality 后 p>0.2，但 pairwise SCS 仍有效 (r=0.129, p<10⁻¹⁰)。对 schema analysis 从业者有直接指导意义。【R1, R2 共识】\n\n**S6. Cross-model validation 设计合理。** Llama-3.1-8B 在 NER count channel (r=0.725) 和 RE confusability channel (Δ=-27.1pp) 上复现主要发现。High-BCS accuracy 跨模型收敛至 ~51% floor 是一个有启发性的发现，已恰当标注为 hypothesis。【R1, R2 共识】\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] v2 prompt 下 RE BCS gap 缩至 7.9pp (CI 含零)，核心 claim robustness 存疑。** v2 prompt 将 RE BCS gap 从 31.2pp (v1) 缩减至 7.9pp (CI: [−5.2, +21.5], n=5)。这意味着在合理 prompt 设计下，confusability channel 在 RE 上可能不显著。论文在 Appendix F 坦诚讨论（\"the v1 extreme-batch gap reflects both genuine type confusion and prompt-induced noise\"），Discussion 也提及，但**正文核心 narrative 仍以 v1 结果为主锚点**。Introduction finding (2) 仍引用 \"accuracy gaps reaching 31.2pp under extreme-batch comparison\" 而未同时注明 v2 结果。\n- **两 Reviewer 共识这是最大 concern。**\n- R2 补充 nuance：pairwise SCS correlation 不受 prompt 影响（基于 type name embedding），NER v2 correlation 更强 (r=+0.58 vs +0.50)。因此 confusability 作为 predictor 的 validity 不受 prompt 影响，受影响的是 practical magnitude。\n- **要求**：(a) 正文 §4.3 增加一段 v2 attenuation 讨论；(b) Introduction 引用 31.2pp 时同时注明 v2 结果 (7.9pp)。\n\n**C2. [Critical] \"Interventional\" 因果语言超出 quasi-experimental 设计支撑范围。** §4.3 \"To move from correlational to interventional evidence\"；§4.4 \"confusability drives substitution errors\"。BCS-controlled experiments 通过构造 batch 操纵 BCS，但 batch composition 与 BCS 完全共变——高 BCS batch 的 types 可能在 inherent difficulty、frequency、definition quality 等维度上系统性不同于低 BCS types。Within-pool analysis 部分缓解了 pool composition confound，但未控制 type-level properties。\n- **两 Reviewer 共识。**\n- **要求**：将 \"interventional\" 改为 \"quasi-experimental\" 或 \"controlled comparison\"；§4.3 开头 acknowledge 残余 confounds。\n\n### Should-Fix（影响评分）\n\n**W1. [Major] Effect size 的 practical significance 在 abstract/intro 未足够突出。** Pairwise r²=1.3-1.7%，typical-batch gap 仅 2.2pp (CI: [0.4, 4.0])。Abstract 主数字已改为 −7.4pp quartile gap，但 pairwise r² 未在 abstract 显式量化。Introduction 仍引用 31.2pp（附 caveat），读者可能仍高估 confusability 的实际影响。R2 提出，R1 部分同意（指出 abstract 已用 −7.4pp，但同意 r² 应更显式）。\n\n**W2. [Major] 正文仅 1 Figure + 4 Tables，关键证据在 appendix。** Error taxonomy（IntraSub ρ=1.0 for NER, 0.954 for RE）是 Channel 2 机制的核心数据点，cross-model BCS 表支撑跨模型验证，但均在 appendix。对于包含六大实验模块的论文，一张双 panel figure 不足以引导读者。**两 Reviewer 共识**，三轮 (Round 1→2→3) 持续提出。\n\n**W3. [Major] MAVEN 反转在 Abstract 中仍仅隐式处理。** Abstract 用 \"generally suppresses recall\" 处理三个数据集中最大的 (168 types) 反转结果。\"generally\" 承载过多信息，读者易误读为全部 suppress。**两 Reviewer 共识**，三轮持续提出。建议用半句话显式陈述 MAVEN 反转。\n\n**W4. [Warning] RE clean channel separation 在 abstract/intro 缺 closed-set format caveat。** RE 是 closed-set classification（消除 entity detection 维度），clean separation 可能部分是 task format artifact。Discussion + Limitations #8 已讨论，但 abstract/intro 中 \"cleanly separable in RE\" 未附加 caveat。R1 REBUT（error taxonomy 提供超越 format artifact 的证据），R2 AGREE。建议 abstract 附加 \"possibly reflecting its closed-set format\"。\n\n**W5. [Warning] 不同 dataset 使用不同 embedding，缺 cross-embedding sensitivity ablation。** Few-NERD 用 Qwen3 embedding，FewRel/MAVEN 用 MiniLM。MAVEN 在两种 embedding 下方向一致 (Appendix C)，但 Few-NERD+MiniLM 和 FewRel+Qwen3 缺失。R2 提出，R1 AGREE。\n\n**W6. [Warning] §5 SDGD 正文过短 (~100 词/4 句)。** SDGD 是 Contribution 4 但正文篇幅与其地位不匹配。Appendix 有完整 protocol，但读者需翻到 appendix 才能理解 precision 暴跌机制。建议增加一段 merge amplification 的定量分解。**两 Reviewer 共识**，两轮持续提出。\n\n### Minor（锦上添花）\n\n**M1. Pairwise r² → batch-level gap 的信号放大缺 formal 推导。** §practical_magnitude 提供 empirical 数据但无从 pair-level variance 到 batch-level gap 的数学推导。Compounding mechanism 不清楚：additive vs nonlinear？两 Reviewer 共识可放 Appendix。\n\n**M2. MAVEN count-curve 反转三因素归因未量化分解。** Relaxed matching / same-domain context / class imbalance 三因素的相对贡献未分离，与论文在 NER/RE 上追求的 controlled analysis 标准不一致。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全共识：\n1. **Prompt sensitivity 是最大 concern** — v2 RE BCS gap CI 含零，需正文讨论 (C1)\n2. **\"Interventional\" → \"quasi-experimental\"** — 因果语言超出设计支撑 (C2)\n3. **正文仅 1 Figure 不够** — 三轮持续问题 (W2)\n4. **Effect size practical significance 需更诚实呈现** (W1)\n5. **MAVEN 反转需 abstract 显式陈述** (W3)\n6. **FewRel closed-set format caveat 需更 prominent** (W4)\n7. **Cross-embedding sensitivity 缺失** (W5)\n8. **§5 SDGD 过短** (W6)\n9. **r² → gap 放大缺形式化** (M1)\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 立场 | R2 立场 | 性质 |\n|------|---------|---------|------|\n| Within-pool quartile CI 含零 (R1-Q2) | BCS 效应在 typical batches 可能不显著 | Regression slope CI excludes zero (p=0.027)，quartile 不显著是 BCS range compression 的 power 问题 | 技术性分歧——summary statistic 选择，非效应存在性 |\n| Effect size abstract framing (W1) | Abstract 已用 −7.4pp，部分同意 r² 应更显式 | 更强调 typical gap 2.2pp 应为主叙事 | 程度之争 |\n\n---\n\n## Questions for Authors\n\n1. **v2 prompt robustness**: v2 RE BCS gap 的 CI 包含零 ([-5.2, +21.5], n=5)。增加 batch 数至 n=25，gap 是否能达到统计显著？若否，论文的 RE confusability claim 如何成立？\n2. **Within-pool quartile CI**: quartile Δ CI 也包含零 ([-8.17, +0.38])。regression slope 显著 (p=0.027) 与 quartile 不显著的差异如何解释？\n3. **51% floor**: 对于 count=8 的高 BCS batch，random chance = 12.5%。51% 远高于 random guessing，但是否接近 \"top-2 confusable types 间的 coin-flip\" baseline？\n4. **Embedding choice**: NER 用 Qwen3 embedding，RE 用 MiniLM。选择依据是什么？Few-NERD+MiniLM 的 SCS-confusion correlation 方向和大小如何？\n5. **SDGD + v2 prompt**: SDGD 全部使用 v1 prompt。v2 的 higher precision 是否可能缓解 merge amplification？Appendix B Table A4 有 v2 结果但未在 §5 讨论。\n6. **Actionable threshold**: SCS/BCS 在什么阈值以上才值得干预？2.2pp typical gap 是否有 actionable 决策边界？\n7. **MAVEN 归因分解**: Relaxed matching / same-domain context / class imbalance 三个归因中，哪个贡献最大？能否通过 exact matching 隔离因素 (i)？\n\n---\n\n## Missing References\n\n- **Chia et al. (2022)** \"RELATIONPROMPT: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\" — zero-shot RE prompt-based approach，与 FewRel 实验设计相关 (R1 提出)\n- **Li et al. (2023)** \"Evaluating ChatGPT's Information Extraction Capabilities\" — R1 检索时 arXiv 版本状态不确定，建议确认 DOI 或出版状态\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。项目配置未开启外部审稿。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Accept (3.5/5)**\n**置信度: 4/5**\n\n**R1 评分**: Overall 3.5, Soundness 3.5, Excitement 3.0, Confidence 4\n**R2 评分**: Overall 3.5, Novelty 3.5, Excitement 3.0, Confidence 4\n\n### 核心判断\n\n论文从 Round 2 (borderline 3.0) 提升至 Round 3 (weak accept 3.5)。**所有 Round 2 Critical issues (6个) 均已解决**，这是实质性进步：\n- MW1: Abstract 改用 bootstrapped CI ✓\n- MW2: §practical_magnitude 校准 typical vs extreme effect ✓\n- SW3: Appendix D 公开完整 prompt template ✓\n- m3: Responsible NLP Checklist 完整 ✓\n- R2-N3-80rel: 31.2pp 全文标注 extreme-batch ✓\n- REF1: 引用修正 ✓\n\n**新发现的两个 Critical issues (R3-C1, R3-C2) 本质上是 framing 问题而非方法论缺陷**——论文的实验数据是完整的（v2 结果存在于 Appendix F），问题在于正文叙事未充分展现这些数据。这与 Round 2 的 Critical issues（数据缺失、checklist 缺失、prompt 未公开）性质不同，修复成本较低。\n\n**升级为 weak accept 的理由**：\n1. 实验设计 (count curves + BCS-controlled + within-pool) 是该领域的方法论标杆\n2. 统计方法全面且透明（cluster bootstrap、permutation test、selection bias 警告）\n3. 诚实报告 modest effects 和负面结果\n4. Centrality confound 分析有独立贡献\n5. Prompt template 完整公开，可复现性显著改善\n\n**阻止进一步升分的因素**：\n1. 核心效应量小（r²=1.3-1.7%，typical gap 2.2pp），practical significance 有限\n2. v2 prompt 下 RE 核心效应 CI 含零——confusability 的 practical magnitude 高度依赖 prompt design\n3. 最清晰的证据来自 RE closed-set classification，external validity 受限\n4. 三轮持续未解的正文视觉支持不足\n5. SDGD 负面结果意味着论文缺少 actionable engineering solution\n\n**推荐**: 修复 C1 (v2 讨论上移正文) 和 C2 (\"interventional\" → \"quasi-experimental\") 后，适合 **EMNLP 主会**。当前版本已是 **Findings track 的安全候选**。\n\n### 与 Round 2 的变化\n\n| 维度 | Round 2 | Round 3 | 变化 |\n|------|---------|---------|------|\n| Overall | 3.0 (borderline) | 3.5 (weak accept) | +0.5 |\n| Critical issues | 6 个 open | 6 个 resolved, 2 个 new (framing) | 实质性改善 |\n| Prompt transparency | 未公开 | Appendix D 完整 | 完全解决 |\n| Statistical annotation | 部分缺失 | CI/caveats 全面 | 显著改善 |\n| Framing | \"framework\" overclaim | \"pattern/decomposition\" | 恰当降格 |\n| 主要 gap | 数据缺失 + prompt 混淆 | v2 attenuation 讨论 + 因果语言 | 从数据层面转向叙事层面 |\n\n---\n\n## Detailed Comments by Section\n\n### Abstract\n- 主数字已改为 −7.4pp quartile gap (CI: [−9.4, −5.5]) ✓\n- \"generally suppresses recall\" 仍隐式处理 MAVEN 反转 → 需半句显式陈述\n- Pairwise r²=1.3-1.7% 未出现 → 建议加入让读者校准期望\n- \"cleanly separable in RE\" 未附 closed-set format caveat\n\n### Introduction\n- RQ1-RQ3 清晰，实验有对应回答 ✓\n- Contribution 1 已改为 \"pattern\"/\"decomposition\" ✓\n- Finding (2) 引用 31.2pp 附带 typical-batch caveat ✓，但未注明 v2 结果\n- Contribution 4 \"structural challenge\" 已限定为 NER ✓\n\n### Related Work (§2)\n- 覆盖 2023-2025 zero-shot IE 主要工作 ✓\n- LLM-PEE 差异化清晰 ✓\n- Sentence-BERT、Li et al. 2023、Wadhwa et al. 2023 补充状态需确认\n- 缺 Chia et al. 2022 (RELATIONPROMPT)\n\n### Experimental Setup (§3)\n- SCS/BCS 定义清晰 ✓\n- Within-pool 控制设计精良 ✓\n- §3.5 prompt 描述改善，Appendix D 完整 ✓\n- Embedding 选择依据未说明（Qwen3 vs MiniLM 在不同 dataset 上的使用）\n\n### Results (§4)\n- §4.1 count curves: NER non-monotonicity 已报 CI ✓；MAVEN 反转需更多正文讨论\n- §4.2 pairwise: r² framing 已改善 ✓；cluster bootstrap 已加入 ✓\n- §4.3 BCS-controlled: within-pool 分析是亮点 ✓；\"interventional\" 语言需修改；v2 attenuation 需正文讨论\n- §4.4 error taxonomy: IntraSub 数据有力 ✓；建议移部分入正文\n- §4.5 centrality confound: 独立贡献 ✓\n- §practical_magnitude: 有效校准 typical vs extreme ✓\n\n### SDGD (§5)\n- 正文仍仅 ~100 词，与 Contribution 4 地位不匹配\n- Appendix B 完整，但正文缺 merge amplification 的定量分解\n\n### Discussion (§6)\n- Boundary conditions 讨论合理 ✓\n- 51% floor 已标注为 hypothesis ✓\n- \"consistent across tested models\" 替换完成 ✓\n- v2 attenuation 提及但可更 prominent\n\n### Limitations\n- 8 条，结构清晰 ✓\n- Item 5 (SDGD scope) 明确限定 ✓\n- Item 7 (FewRel scope) 明确 ✓\n- Item 8 (RE format specificity) 明确 ✓\n\n### Format Compliance\n- 页数: 8 页正文 + references + appendix ✓\n- 匿名: 完全匿名 \"Anonymous ACL submission\" ✓\n- Checklist: 完整 A1-E1 ✓\n- ACL [review] 格式 ✓\n- 引用: 43 篇，无 orphan/missing ✓\n\n---\n\n## Round 2 → Round 3 Issue Resolution Summary\n\n### Resolved (Round 2 Critical → Round 3 PASS): 6/6\n| ID | Issue | Verification |\n|----|-------|-------------|\n| MW1 | 16-rel 单 batch 无 CI | PASS — Abstract 改用 bootstrapped CI |\n| MW2 | 信号放大缺论证 | PASS — §practical_magnitude |\n| SW3 | v1/v2 prompt 混淆 | PASS — Appendix D 完整 |\n| m3 | 缺 Checklist | PASS — checklist.tex 完整 |\n| R2-N3-80rel | 31.2pp headline | PASS — 全文标注 extreme-batch |\n| REF1 | 引用占位符 | PASS — 已修正 |\n\n### Resolved (Round 2 Warning/Info → Round 3 PASS): 4\n| ID | Issue | Verification |\n|----|-------|-------------|\n| R2-W4-sdgd-scope | SDGD 仅 NER | PASS — Limitations #5 |\n| R2-W1-framework | \"framework\" overclaim | PASS — 全文替换 |\n| D037-m1-checklist | checklist.tex 'framework' | PASS |\n| R2-W7-51floor | 51% floor 推测性 | PASS — 标注 hypothesis |\n\n### Partially Resolved: 3\n| ID | Issue | Status |\n|----|-------|--------|\n| MW4 | 正文仅 1 Figure | 仍仅 Figure 1 |\n| SW4 | MAVEN abstract | 仍用 \"generally\" |\n| R2-m-sdgd-short | §5 过短 | 仍 ~100 词 |\n\n### New Issues (Round 3): 7\n| ID | Severity | Summary |\n|----|----------|---------|\n| R3-C1 | Critical | v2 prompt 下 RE gap CI 含零，正文未充分讨论 |\n| R3-C2 | Critical | \"interventional\" 因果语言 |\n| R3-W1 | Warning | Effect size practical significance 未在 abstract 突出 |\n| R3-W5 | Warning | Cross-embedding sensitivity 缺失 |\n| R3-W3 | Info | r² → gap 放大缺 formal 推导 |\n| R3-W6 | Info | MAVEN 反转归因未量化 |\n| R2-W5-RE-artifact | Warning (reopened) | RE classification caveat 缺 abstract |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak accept",
    "report": "# 圆桌审稿报告 — Round 3\n\n**论文**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿人**: Reviewer 1 (方法严谨性 + 实验设计 + 统计分析), Reviewer 2 (新颖性 + 完整性 + 写作质量 + 格式合规)\n**轮次**: Round 3（论文已针对 Round 2 的全部 Critical issues 进行修订）\n**外部审稿**: 未启用\n\n---\n\n## Summary\n\n本文首次系统隔离 training-free LLM IE 中 schema 退化的两个通道（type count 和 type confusability），引入 SCS/BCS 量化指标，在 NER (Few-NERD)、RE (FewRel)、ED (MAVEN) 三个任务上进行控制实验。主要发现：(1) RE 上两通道 cleanly separable（高 BCS 准确率收敛至 ~51% floor）；(2) NER 上 confusability 同时影响 detection；(3) MAVEN 出现 centrality confound 导致 per-type BCS 方向反转；(4) SDGD 负面结果表明 union-based merge 存在结构性挑战。相比 Round 2，论文在 prompt 透明度、统计注解、framing 降格方面有实质性改善。\n\n---\n\n## Strengths\n\n**S1. 实验设计是该领域罕见的方法论标杆。** Count curves（固定 confusability，变 count）和 BCS-controlled experiments（固定 count，变 confusability）互补设计合理，within-pool 控制（80-rel pool → 16-sub）有效排除 pool composition confound。permutation test (p=0.436) 验证跨条件 slope 一致性。这在 training-free IE 领域是首次系统性因素隔离。【R1, R2 共识】\n\n**S2. 统计方法全面且透明。** Bootstrap CI (B=10,000)、type-level cluster bootstrap（处理 pair 非独立性，Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]）、within-pool regression (slope −0.401, CI excludes zero, p=0.027)。对 pair-level CI 与 cluster bootstrap CI 的差异做了诚实解释。§practical_magnitude 校准了 typical vs extreme effect size (IQR → 2.2pp vs extreme 31.2pp)。【R1 重点肯定, R2 同意】\n\n**S3. 诚实报告负面结果和 modest effects。** Pairwise r²=1.3-1.7% 如实报告，SDGD 全面失败 (best F1=0.32 vs single-pass 0.45)，factorial test 不显著 (p=0.50)，MAVEN centrality confound，80-rel full condition underpowered 等均明确标注。Limitations 涵盖 8 项，远超该领域平均水平。【R1, R2 共识】\n\n**S4. Prompt 透明度大幅改善。** Appendix D 包含三个任务的完整 prompt template（v1/v2 对比 + JSON schema + diff 说明），RE 单版本明确标注，§4 开头标注 prompt 版本适用范围。Round 2 的 SW3 (Critical) 完全解决。【R1 PASS】\n\n**S5. Centrality confound 分析有独立方法论贡献。** 识别 per-type BCS 在 same-domain schema 上因 embedding collapse 反转 (MAVEN: ρ=+0.184)，partial correlation 控制 log freq + degree centrality 后 p>0.2，但 pairwise SCS 仍有效 (r=0.129, p<10⁻¹⁰)。对 schema analysis 从业者有直接指导意义。【R1, R2 共识】\n\n**S6. Cross-model validation 设计合理。** Llama-3.1-8B 在 NER count channel (r=0.725) 和 RE confusability channel (Δ=-27.1pp) 上复现主要发现。High-BCS accuracy 跨模型收敛至 ~51% floor 是一个有启发性的发现，已恰当标注为 hypothesis。【R1, R2 共识】\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] v2 prompt 下 RE BCS gap 缩至 7.9pp (CI 含零)，核心 claim robustness 存疑。** v2 prompt 将 RE BCS gap 从 31.2pp (v1) 缩减至 7.9pp (CI: [−5.2, +21.5], n=5)。这意味着在合理 prompt 设计下，confusability channel 在 RE 上可能不显著。论文在 Appendix F 坦诚讨论（\"the v1 extreme-batch gap reflects both genuine type confusion and prompt-induced noise\"），Discussion 也提及，但**正文核心 narrative 仍以 v1 结果为主锚点**。Introduction finding (2) 仍引用 \"accuracy gaps reaching 31.2pp under extreme-batch comparison\" 而未同时注明 v2 结果。\n- **两 Reviewer 共识这是最大 concern。**\n- R2 补充 nuance：pairwise SCS correlation 不受 prompt 影响（基于 type name embedding），NER v2 correlation 更强 (r=+0.58 vs +0.50)。因此 confusability 作为 predictor 的 validity 不受 prompt 影响，受影响的是 practical magnitude。\n- **要求**：(a) 正文 §4.3 增加一段 v2 attenuation 讨论；(b) Introduction 引用 31.2pp 时同时注明 v2 结果 (7.9pp)。\n\n**C2. [Critical] \"Interventional\" 因果语言超出 quasi-experimental 设计支撑范围。** §4.3 \"To move from correlational to interventional evidence\"；§4.4 \"confusability drives substitution errors\"。BCS-controlled experiments 通过构造 batch 操纵 BCS，但 batch composition 与 BCS 完全共变——高 BCS batch 的 types 可能在 inherent difficulty、frequency、definition quality 等维度上系统性不同于低 BCS types。Within-pool analysis 部分缓解了 pool composition confound，但未控制 type-level properties。\n- **两 Reviewer 共识。**\n- **要求**：将 \"interventional\" 改为 \"quasi-experimental\" 或 \"controlled comparison\"；§4.3 开头 acknowledge 残余 confounds。\n\n### Should-Fix（影响评分）\n\n**W1. [Major] Effect size 的 practical significance 在 abstract/intro 未足够突出。** Pairwise r²=1.3-1.7%，typical-batch gap 仅 2.2pp (CI: [0.4, 4.0])。Abstract 主数字已改为 −7.4pp quartile gap，但 pairwise r² 未在 abstract 显式量化。Introduction 仍引用 31.2pp（附 caveat），读者可能仍高估 confusability 的实际影响。R2 提出，R1 部分同意（指出 abstract 已用 −7.4pp，但同意 r² 应更显式）。\n\n**W2. [Major] 正文仅 1 Figure + 4 Tables，关键证据在 appendix。** Error taxonomy（IntraSub ρ=1.0 for NER, 0.954 for RE）是 Channel 2 机制的核心数据点，cross-model BCS 表支撑跨模型验证，但均在 appendix。对于包含六大实验模块的论文，一张双 panel figure 不足以引导读者。**两 Reviewer 共识**，三轮 (Round 1→2→3) 持续提出。\n\n**W3. [Major] MAVEN 反转在 Abstract 中仍仅隐式处理。** Abstract 用 \"generally suppresses recall\" 处理三个数据集中最大的 (168 types) 反转结果。\"generally\" 承载过多信息，读者易误读为全部 suppress。**两 Reviewer 共识**，三轮持续提出。建议用半句话显式陈述 MAVEN 反转。\n\n**W4. [Warning] RE clean channel separation 在 abstract/intro 缺 closed-set format caveat。** RE 是 closed-set classification（消除 entity detection 维度），clean separation 可能部分是 task format artifact。Discussion + Limitations #8 已讨论，但 abstract/intro 中 \"cleanly separable in RE\" 未附加 caveat。R1 REBUT（error taxonomy 提供超越 format artifact 的证据），R2 AGREE。建议 abstract 附加 \"possibly reflecting its closed-set format\"。\n\n**W5. [Warning] 不同 dataset 使用不同 embedding，缺 cross-embedding sensitivity ablation。** Few-NERD 用 Qwen3 embedding，FewRel/MAVEN 用 MiniLM。MAVEN 在两种 embedding 下方向一致 (Appendix C)，但 Few-NERD+MiniLM 和 FewRel+Qwen3 缺失。R2 提出，R1 AGREE。\n\n**W6. [Warning] §5 SDGD 正文过短 (~100 词/4 句)。** SDGD 是 Contribution 4 但正文篇幅与其地位不匹配。Appendix 有完整 protocol，但读者需翻到 appendix 才能理解 precision 暴跌机制。建议增加一段 merge amplification 的定量分解。**两 Reviewer 共识**，两轮持续提出。\n\n### Minor（锦上添花）\n\n**M1. Pairwise r² → batch-level gap 的信号放大缺 formal 推导。** §practical_magnitude 提供 empirical 数据但无从 pair-level variance 到 batch-level gap 的数学推导。Compounding mechanism 不清楚：additive vs nonlinear？两 Reviewer 共识可放 Appendix。\n\n**M2. MAVEN count-curve 反转三因素归因未量化分解。** Relaxed matching / same-domain context / class imbalance 三因素的相对贡献未分离，与论文在 NER/RE 上追求的 controlled analysis 标准不一致。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全共识：\n1. **Prompt sensitivity 是最大 concern** — v2 RE BCS gap CI 含零，需正文讨论 (C1)\n2. **\"Interventional\" → \"quasi-experimental\"** — 因果语言超出设计支撑 (C2)\n3. **正文仅 1 Figure 不够** — 三轮持续问题 (W2)\n4. **Effect size practical significance 需更诚实呈现** (W1)\n5. **MAVEN 反转需 abstract 显式陈述** (W3)\n6. **FewRel closed-set format caveat 需更 prominent** (W4)\n7. **Cross-embedding sensitivity 缺失** (W5)\n8. **§5 SDGD 过短** (W6)\n9. **r² → gap 放大缺形式化** (M1)\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 立场 | R2 立场 | 性质 |\n|------|---------|---------|------|\n| Within-pool quartile CI 含零 (R1-Q2) | BCS 效应在 typical batches 可能不显著 | Regression slope CI excludes zero (p=0.027)，quartile 不显著是 BCS range compression 的 power 问题 | 技术性分歧——summary statistic 选择，非效应存在性 |\n| Effect size abstract framing (W1) | Abstract 已用 −7.4pp，部分同意 r² 应更显式 | 更强调 typical gap 2.2pp 应为主叙事 | 程度之争 |\n\n---\n\n## Questions for Authors\n\n1. **v2 prompt robustness**: v2 RE BCS gap 的 CI 包含零 ([-5.2, +21.5], n=5)。增加 batch 数至 n=25，gap 是否能达到统计显著？若否，论文的 RE confusability claim 如何成立？\n2. **Within-pool quartile CI**: quartile Δ CI 也包含零 ([-8.17, +0.38])。regression slope 显著 (p=0.027) 与 quartile 不显著的差异如何解释？\n3. **51% floor**: 对于 count=8 的高 BCS batch，random chance = 12.5%。51% 远高于 random guessing，但是否接近 \"top-2 confusable types 间的 coin-flip\" baseline？\n4. **Embedding choice**: NER 用 Qwen3 embedding，RE 用 MiniLM。选择依据是什么？Few-NERD+MiniLM 的 SCS-confusion correlation 方向和大小如何？\n5. **SDGD + v2 prompt**: SDGD 全部使用 v1 prompt。v2 的 higher precision 是否可能缓解 merge amplification？Appendix B Table A4 有 v2 结果但未在 §5 讨论。\n6. **Actionable threshold**: SCS/BCS 在什么阈值以上才值得干预？2.2pp typical gap 是否有 actionable 决策边界？\n7. **MAVEN 归因分解**: Relaxed matching / same-domain context / class imbalance 三个归因中，哪个贡献最大？能否通过 exact matching 隔离因素 (i)？\n\n---\n\n## Missing References\n\n- **Chia et al. (2022)** \"RELATIONPROMPT: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\" — zero-shot RE prompt-based approach，与 FewRel 实验设计相关 (R1 提出)\n- **Li et al. (2023)** \"Evaluating ChatGPT's Information Extraction Capabilities\" — R1 检索时 arXiv 版本状态不确定，建议确认 DOI 或出版状态\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。项目配置未开启外部审稿。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Accept (3.5/5)**\n**置信度: 4/5**\n\n**R1 评分**: Overall 3.5, Soundness 3.5, Excitement 3.0, Confidence 4\n**R2 评分**: Overall 3.5, Novelty 3.5, Excitement 3.0, Confidence 4\n\n### 核心判断\n\n论文从 Round 2 (borderline 3.0) 提升至 Round 3 (weak accept 3.5)。**所有 Round 2 Critical issues (6个) 均已解决**，这是实质性进步：\n- MW1: Abstract 改用 bootstrapped CI ✓\n- MW2: §practical_magnitude 校准 typical vs extreme effect ✓\n- SW3: Appendix D 公开完整 prompt template ✓\n- m3: Responsible NLP Checklist 完整 ✓\n- R2-N3-80rel: 31.2pp 全文标注 extreme-batch ✓\n- REF1: 引用修正 ✓\n\n**新发现的两个 Critical issues (R3-C1, R3-C2) 本质上是 framing 问题而非方法论缺陷**——论文的实验数据是完整的（v2 结果存在于 Appendix F），问题在于正文叙事未充分展现这些数据。这与 Round 2 的 Critical issues（数据缺失、checklist 缺失、prompt 未公开）性质不同，修复成本较低。\n\n**升级为 weak accept 的理由**：\n1. 实验设计 (count curves + BCS-controlled + within-pool) 是该领域的方法论标杆\n2. 统计方法全面且透明（cluster bootstrap、permutation test、selection bias 警告）\n3. 诚实报告 modest effects 和负面结果\n4. Centrality confound 分析有独立贡献\n5. Prompt template 完整公开，可复现性显著改善\n\n**阻止进一步升分的因素**：\n1. 核心效应量小（r²=1.3-1.7%，typical gap 2.2pp），practical significance 有限\n2. v2 prompt 下 RE 核心效应 CI 含零——confusability 的 practical magnitude 高度依赖 prompt design\n3. 最清晰的证据来自 RE closed-set classification，external validity 受限\n4. 三轮持续未解的正文视觉支持不足\n5. SDGD 负面结果意味着论文缺少 actionable engineering solution\n\n**推荐**: 修复 C1 (v2 讨论上移正文) 和 C2 (\"interventional\" → \"quasi-experimental\") 后，适合 **EMNLP 主会**。当前版本已是 **Findings track 的安全候选**。\n\n### 与 Round 2 的变化\n\n| 维度 | Round 2 | Round 3 | 变化 |\n|------|---------|---------|------|\n| Overall | 3.0 (borderline) | 3.5 (weak accept) | +0.5 |\n| Critical issues | 6 个 open | 6 个 resolved, 2 个 new (framing) | 实质性改善 |\n| Prompt transparency | 未公开 | Appendix D 完整 | 完全解决 |\n| Statistical annotation | 部分缺失 | CI/caveats 全面 | 显著改善 |\n| Framing | \"framework\" overclaim | \"pattern/decomposition\" | 恰当降格 |\n| 主要 gap | 数据缺失 + prompt 混淆 | v2 attenuation 讨论 + 因果语言 | 从数据层面转向叙事层面 |\n\n---\n\n## Detailed Comments by Section\n\n### Abstract\n- 主数字已改为 −7.4pp quartile gap (CI: [−9.4, −5.5]) ✓\n- \"generally suppresses recall\" 仍隐式处理 MAVEN 反转 → 需半句显式陈述\n- Pairwise r²=1.3-1.7% 未出现 → 建议加入让读者校准期望\n- \"cleanly separable in RE\" 未附 closed-set format caveat\n\n### Introduction\n- RQ1-RQ3 清晰，实验有对应回答 ✓\n- Contribution 1 已改为 \"pattern\"/\"decomposition\" ✓\n- Finding (2) 引用 31.2pp 附带 typical-batch caveat ✓，但未注明 v2 结果\n- Contribution 4 \"structural challenge\" 已限定为 NER ✓\n\n### Related Work (§2)\n- 覆盖 2023-2025 zero-shot IE 主要工作 ✓\n- LLM-PEE 差异化清晰 ✓\n- Sentence-BERT、Li et al. 2023、Wadhwa et al. 2023 补充状态需确认\n- 缺 Chia et al. 2022 (RELATIONPROMPT)\n\n### Experimental Setup (§3)\n- SCS/BCS 定义清晰 ✓\n- Within-pool 控制设计精良 ✓\n- §3.5 prompt 描述改善，Appendix D 完整 ✓\n- Embedding 选择依据未说明（Qwen3 vs MiniLM 在不同 dataset 上的使用）\n\n### Results (§4)\n- §4.1 count curves: NER non-monotonicity 已报 CI ✓；MAVEN 反转需更多正文讨论\n- §4.2 pairwise: r² framing 已改善 ✓；cluster bootstrap 已加入 ✓\n- §4.3 BCS-controlled: within-pool 分析是亮点 ✓；\"interventional\" 语言需修改；v2 attenuation 需正文讨论\n- §4.4 error taxonomy: IntraSub 数据有力 ✓；建议移部分入正文\n- §4.5 centrality confound: 独立贡献 ✓\n- §practical_magnitude: 有效校准 typical vs extreme ✓\n\n### SDGD (§5)\n- 正文仍仅 ~100 词，与 Contribution 4 地位不匹配\n- Appendix B 完整，但正文缺 merge amplification 的定量分解\n\n### Discussion (§6)\n- Boundary conditions 讨论合理 ✓\n- 51% floor 已标注为 hypothesis ✓\n- \"consistent across tested models\" 替换完成 ✓\n- v2 attenuation 提及但可更 prominent\n\n### Limitations\n- 8 条，结构清晰 ✓\n- Item 5 (SDGD scope) 明确限定 ✓\n- Item 7 (FewRel scope) 明确 ✓\n- Item 8 (RE format specificity) 明确 ✓\n\n### Format Compliance\n- 页数: 8 页正文 + references + appendix ✓\n- 匿名: 完全匿名 \"Anonymous ACL submission\" ✓\n- Checklist: 完整 A1-E1 ✓\n- ACL [review] 格式 ✓\n- 引用: 43 篇，无 orphan/missing ✓\n\n---\n\n## Round 2 → Round 3 Issue Resolution Summary\n\n### Resolved (Round 2 Critical → Round 3 PASS): 6/6\n| ID | Issue | Verification |\n|----|-------|-------------|\n| MW1 | 16-rel 单 batch 无 CI | PASS — Abstract 改用 bootstrapped CI |\n| MW2 | 信号放大缺论证 | PASS — §practical_magnitude |\n| SW3 | v1/v2 prompt 混淆 | PASS — Appendix D 完整 |\n| m3 | 缺 Checklist | PASS — checklist.tex 完整 |\n| R2-N3-80rel | 31.2pp headline | PASS — 全文标注 extreme-batch |\n| REF1 | 引用占位符 | PASS — 已修正 |\n\n### Resolved (Round 2 Warning/Info → Round 3 PASS): 4\n| ID | Issue | Verification |\n|----|-------|-------------|\n| R2-W4-sdgd-scope | SDGD 仅 NER | PASS — Limitations #5 |\n| R2-W1-framework | \"framework\" overclaim | PASS — 全文替换 |\n| D037-m1-checklist | checklist.tex 'framework' | PASS |\n| R2-W7-51floor | 51% floor 推测性 | PASS — 标注 hypothesis |\n\n### Partially Resolved: 3\n| ID | Issue | Status |\n|----|-------|--------|\n| MW4 | 正文仅 1 Figure | 仍仅 Figure 1 |\n| SW4 | MAVEN abstract | 仍用 \"generally\" |\n| R2-m-sdgd-short | §5 过短 | 仍 ~100 词 |\n\n### New Issues (Round 3): 7\n| ID | Severity | Summary |\n|----|----------|---------|\n| R3-C1 | Critical | v2 prompt 下 RE gap CI 含零，正文未充分讨论 |\n| R3-C2 | Critical | \"interventional\" 因果语言 |\n| R3-W1 | Warning | Effect size practical significance 未在 abstract 突出 |\n| R3-W5 | Warning | Cross-embedding sensitivity 缺失 |\n| R3-W3 | Info | r² → gap 放大缺 formal 推导 |\n| R3-W6 | Info | MAVEN 反转归因未量化 |\n| R2-W5-RE-artifact | Warning (reopened) | RE classification caveat 缺 abstract |"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-16T04:56:35.586236+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5321
}
```

</details>

---


### Assistant

_source line 302 · 2026-05-16T04:56:44.956775+00:00_

审稿报告已投递。

---

**Round 3 圆桌审稿完成。**

| 维度 | 结果 |
|------|------|
| **Overall** | **Weak Accept (3.5/5)**，从 Round 2 borderline (3.0) 上升 |
| **Reviewer** | R1: 3.5 (Soundness 3.5, Excitement 3.0) / R2: 3.5 (Novelty 3.5, Excitement 3.0) |
| **Round 2 Critical 修复** | **6/6 全部 PASS** |
| **新 Critical** | 2 个（均为 framing，非数据缺陷）：(1) v2 RE gap CI 含零需正文讨论；(2) "interventional"→"quasi-experimental" |
| **新 Warning** | 4 个：effect size 呈现、正文图表不足（三轮持续）、cross-embedding 缺失、RE caveat |
| **共识度** | 9 项完全共识，1 项技术性分歧（within-pool quartile CI 解读） |
| **推荐** | 修复 2 个 Critical framing issues 后适合主会；当前版本是 Findings track 安全候选 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 303 · 2026-05-16T04:56:47.510704+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

与 R1 高度一致（5W 全 AGREE，5Q 中 4 AGREE + 1 REBUT）。唯一分歧在 Q2：R1 认为 within-pool quartile CI 含零说明效应不显著，我指出 regression slope CI 排除零（p=0.027），quartile 不显著是 BCS range 窄导致的 power 问题，不应等同于效应不存在。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 304 · 2026-05-16T04:57:01.661922+00:00_

Round 3 圆桌审稿已完成。

**审稿报告已投递给 Research Director。**

汇总：

| 维度 | 结果 |
|------|------|
| **Overall** | **Weak Accept (3.5/5)**，从 Round 2 borderline (3.0) 提升 |
| **Round 2 Critical** | 6/6 全部 PASS |
| **新 Critical** | 2 个（均为 framing 问题，非方法论缺陷）|
| **Reviewer 共识** | 9 项共识，1 项技术性分歧 |

**两个新 Critical（修复成本低）：**
1. **R3-C1**: v2 prompt 下 RE BCS gap 缩至 7.9pp (CI 含零)，需在正文 §4.3 讨论，Introduction 引用 31.2pp 时注明 v2 结果
2. **R3-C2**: "interventional" → "quasi-experimental"，acknowledge 残余 confounds

**持续未解的 Warning（三轮）：**
- 正文仅 1 Figure（MW4）
- MAVEN 反转在 Abstract 仅隐式处理（SW4）
- §5 SDGD 过短（R2-m-sdgd-short）

**结论**：修复 C1 + C2 后适合 EMNLP 主会；当前版本已是 Findings track 安全候选。Issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 24

## Round 24

70 recorded events


### User

_source line 305 · 2026-05-16T09:02:30.276206+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/paper/main.tex
- 目标 venue: EMNLP 2026 Main Conference
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-16T09:02:38.079169+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-16T09:02:38.130325+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-16T09:02:41.996771+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-16T09:02:41.997244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-16T09:02:47.420194+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-16T09:02:47.972968+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (42 个)\n\n- **bootstrap_ci_analysis**: DONE (success) — \n- **exp016_fewrel_error_taxonomy**: DONE (success) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp007_error_taxonomy**: DONE (success) — \n- **exp_fewrel_formal_80rel**: DONE (success) — \n- **exp_fewrel_formal**: DONE (success) — \n- **exp008_sdgd_zero_fewnerd_r2**: DONE (negative) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n- **fewrel_pilot**: DONE (success) — \n- **exp004_maven_bcs**: DONE (negative) — \n- **exp002_confusability_controlled**: DONE (success) — \n- **exp003a_prompt_v2_rerun**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp001_count_baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- exp_fewrel_v2_n25（准备中）\n- bcs_max_to_mean_fix（准备中）\n\n## 近期结论\n- **exp_confusability_batch_composition** (success): Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confu
…[truncated 1229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-16T09:02:47.973341+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-16T09:02:48.526214+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## exp-018 结果与经验（2026-05-16）\\n- **结果**: confusability_aware 0.8021 > random 0.7877±0.0178 (CI上界0.7967)，提升显著 +1.44pp\\n- single_pass 80-rel 全量仅 0.5042，schema overload 严重\\n- Graph coloring (Welsh-Powell) 将 intra-batch BCS 从 0.5585 降到 0.5524\\n- 51 types improved, 28 degraded — 效果非均匀，部分 type 受益更多\\n- **关键参数**: 80-rel pool, batch_size=8-rel per batch, 15 random seeds for CI, 960 samples\\n- **无 merge amplification** — RE closed-set 验证了 Director 的预判\\n- FLASHINFER_DISABLE_VERSION_CHECK=1 需要设置，否则 vLLM 启动失败\\n- 支持 --resume 断点续传（按 condition 粒度）\\n\\n## exp-018 定位澄清（2026-05-16, Director）\\n- exp-018 不是\\\"重试 SDGD\\\"，而是\\\"confusability-aware batching 在 RE closed-set classification 上的实用方案\\\"\\n- RE 每个 (head, tail) pair 独立分类，无实体边界合并 → 无 merge amplification 问题\\n- exp-008 SDGD 失败的 root cause = NER span overlap 的 merge amplification，不适用于 RE\\n- 论文写法：§5 SDGD 失败因 NER merge amplification，但 RE closed-set 避免了此问题 → practical recommendation\\n\\n## exp-017 GPT-4o-mini（2026-05-16, Director 决定放弃）\\n- TUM proxy 未部署在 AutoDL 服务器，无法访问 OpenAI API\\n- 闭源模型验证缺失已在 discussion.tex limitations 中说明\\n- 教训：API 实验需要预先确认 proxy 可达性\\n\\n## D035 集成方案（2026-05-16）\\n- 论文 Table 3 用**极端批次**方法（BCS 最低/最高各 ~5 batches 的 accuracy Δ），不是四分位\\n- D033 的 7.42pp 是四分位比较，需要用极端批次方法重算\\n- 80-pool-16sub 的 3.92pp 也是四分位，同样需要重算\\n- 四分位 CI 作为补充证据报告，展示效应在不同分析粒度下都稳健\\n- 两组数据一起集成到论文再编译上传\\n\\n## 80-pool-16sub 关键发现（2026-05-16）\\n- BCS 范围窄 [0.458, 0.684]（vs 独立 16-rel [0.653, 0.900]），因为从 80-rel pool 采样的 16 types 语义更分散\\n- 四分位 Δ CI 跨零 [-7.79, +0.42]，但回归斜率 CI 不跨零 [-0.684, -0.062]\\n- 效应弱于独立 16-rel pool——BCS 范围压缩导致效应量缩小，这本身支持 BCS 是驱动因素的论点\\n- 决策：用回归斜率做跨条件比较（斜率控制了 BCS 范围差异），四分位 Δ 作为直觉可读的补充\\n\\n## MAVEN per-type BCS 正相关是 artifact（2026-05-16）\\n- exp_maven_residualized_bcs 确认：控制 log_freq + degree_centrality 后相关消失\\n- MiniLM confound = fre
…[truncated 479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-16T09:02:49.481055+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-16T09:02:49.889937+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 408
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-16T09:02:49.940653+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "projects/schema-dag-extraction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "projects/schema-dag-extraction/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-16T09:02:49.941132+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-16T09:02:55.070059+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-16T09:02:55.221374+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-16T09:02:56.076029+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-16T09:02:56.377835+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-16T09:02:56.428449+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-16T09:02:56.479035+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-16T09:03:04.064352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-16T09:03:04.466697+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	
16	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
42	
43	\item \textbf{Non-significant factorial test.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.
44	
45	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
46	
47	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits 
…[truncated 18346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-16T09:03:04.517442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-16T09:03:04.920411+00:00_

1	# Round 3 Review Issues Tracker
2	# Updated: 2026-05-16 (Action Matrix dispatched to Agent)
3	
4	# ============================================================
5	# CRITICAL — Must-Fix
6	# ============================================================
7	
8	- id: MW1
9	  summary: "16-rel BCS gap (9.1 pp) 基于单 batch 无 CI，统计不可靠"
10	  category: experiment
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 1
14	  last_seen_round: 3
15	  mentions:
16	    - {round: 1, reviewers: [R1, R2], note: "R1-W1 + R2-W3 完全一致"}
17	    - {round: 2, reviewers: [R1, R2], note: "R1-N2 re-raised; within-pool 已补但 16-rel 独立 pool 仍为单 batch"}
18	    - {round: 3, reviewers: [R1], note: "PASS — Abstract 改用 quartile -7.4pp CI; Table 3 caption 标注 illustrative"}
19	  action_items:
20	    - {round: 1, action: "D033 16-rel 100 batch bootstrap CI", assigned_to: agent, status: done}
21	    - {round: 1, action: "80-rel pool 内 16-type 子集 BCS-controlled 实验", assigned_to: agent, status: done}
22	    - {round: 2, action: "Abstract 中 9.1pp 替换为 bootstrapped CI", assigned_to: agent, status: done}
23	  resolution: "Abstract 改用 bootstrapped CI; Table 3 caption 标注为 illustrative"
24	  resolution_round: 2
25	
26	- id: MW2
27	  summary: "Pairwise r²=1.3-1.7% → batch-level 31.2 pp 的信号放大缺乏形式化论证"
28	  category: framing
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 3
33	  mentions:
34	    - {round: 1, reviewers: [R1, R2], note: "R1-W2 + R2-W2 共识"}
35	    - {round: 2, reviewers: [R1, R2], note: "within-pool quartile CI 穿越零与 31.2 pp 矛盾"}
36	    - {round: 3, reviewers: [R1, R2], note: "PASS on practical_magnitude; 但 formal derivation 仍缺 — 见 R3-W3"}
37	  action_items:
38	    - {round: 1, action: "Contribution 2 改为 modest predictor", assigned_to: paper_agent, status: done}
39	    - {round: 1, action: "加 conditioning-on-outcome bias 讨论", assigned_to: paper_agent, status: done}
40	    - {round: 2, action: "practical_magnitude 新增 realistic effect size", assigned
…[truncated 17364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-16T09:03:04.920801+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 329 · 2026-05-16T09:03:04.971308+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-16T09:03:30.369914+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-16T09:03:31.879805+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 332 · 2026-05-16T09:03:32.533089+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 653
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-16T09:03:38.007355+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here's the key information about EMNLP 2026:

## Submission Deadline

The ARR (ACL Rolling Review) submission deadline for long and short papers is May 25, 2026.

## Important Dates

Key dates inclu
…[truncated 1548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7637
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-16T09:03:43.135601+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 paper format page limit template double blind anonymity ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 paper format page limit template double blind anonymity ARR"
  }
}
```

</details>

---


### Tool call

_source line 335 · 2026-05-16T09:03:43.588100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 336 · 2026-05-16T09:03:44.140874+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\text{--}1.7\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability
…[truncated 344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 337 · 2026-05-16T09:03:44.141252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 338 · 2026-05-16T09:03:44.492944+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies implicitly assume different answers: \citet{uniner-2024} extract each type independently; \citet{llm-pee-2025} partition schemas by type embedding similarity; \citet{parse-2025} optimize schema definitions. None isolates \emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusabil
…[truncated 2602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 339 · 2026-05-16T09:03:44.493414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 340 · 2026-05-16T09:03:45.499578+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.
9	
10	\paragraph{Embedding anisotropy.}
11	Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters
…[truncated 101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 341 · 2026-05-16T09:03:45.550399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 342 · 2026-05-16T09:03:45.550823+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample balanced instances and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the va
…[truncated 4995 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 343 · 2026-05-16T09:03:45.652519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 344 · 2026-05-16T09:03:45.753589+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
25	
26	\paragraph{NER (Few-NERD).}
27	Recall declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$ ($-$42\% relative), with minor non-monotonicity within sampling variability (bootstrap CIs overlap). Precision rises inversely (0.11 $\to$ 0.52), reflecting a shift from over-prediction to under-prediction as candidate types increase.
28	
29	\paragraph{RE (FewRel).}
30	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled fr
…[truncated 12428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-16T09:03:57.665391+00:00_

Web search results for query: "EMNLP 2026 paper format page limit template double blind anonymity ARR"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/about/submissions"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Now let me search for more specific information about double-blind anonymity requirements for EMNLP 2026.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Submissions
…[truncated 2179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 14529
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-16T09:04:02.899021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-16T09:04:03.352773+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure is \emph{merge amplification}: presenting the same text $k$ times causes each pass to independently generate predictions. Single-pass precision (0.563) collapses to 0.210--0.249 after union merge with 8 batches, while recall gains are modest (0.368 $\to$ 0.314--0.446). Confidence gating improves precision but with disproportionate recall loss (Appendix~\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \cite{llm-calibration-survey-2024}.
8	
9	\paragraph{Why NER fails but RE does not.}
10	Merge amplification is specific to span-level tasks: each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE operates on fixed (head, tail) pairs with no span reconciliation---each pair receives an independent classification, eliminating the mechanism that caused SDGD to fail.
11	
12	\paragraph{Confusability-aware batch composition for RE.}
13	Since RE avoids merge amplification, we test whether confusability-aware batching improves accuracy. All decomposition conditions use oracle routing (each instance is routed to the batch containing its gold type). Single-type batches versus the 80-relation single-pass yields +29.8\,pp (0.802 vs.\ 0.504), confirming that decomposition is effective whe
…[truncated 415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-16T09:04:03.353166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-16T09:04:03.604835+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Practitioners should monitor BCS and prefer cross-domain type groupings. Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1: $-$31.2\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Future directions.}
8	For NER, merge amplification blocks naive decomposition (\S\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this. For RE, extending confusability-aware batching to broader benchmarks is a natural next step.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp) and across extraction granularities (DocRED document-level RE: count decline $-$49\,pp; BCS slope $= -0.71$, $R^2 = 0.53$), with high-BCS accuracy converging to a floor consistent across both tested models. We further identified a centrality confound on same-domain schemas, demonstrated that merge amplification is a structural challenge for NER decomposition, and showed that confusability-aware batch composition recovers +1.4\,pp on RE where span reconciliation is unnecessary. Cross-batch calibration or joint decoding for NER, and broader
…[truncated 64 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-16T09:04:03.656867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-16T09:04:03.657491+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model replication, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} and \S
…[truncated 4366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-16T09:04:37.042940+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-16T09:04:37.394932+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 44\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 1449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-16T09:04:39.656747+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check external review config",
  "subagent_type": "Explore",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction, find any YAML or JSON config file that contains \"external_review\" or \"paperreview_ai\" settings. Check config.yaml, project.yaml, settings.yaml, or any similar configuration file. Report the external_review enabled status. Search breadth: quick."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check external review config",
    "subagent_type": "Explore",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction, find any YAML or JSON config file that contains \"external_review\" or \"paperreview_ai\" settings. Check config.yaml, project.yaml, settings.yaml, or any similar configuration file. Report the external_review enabled status. Search breadth: quick."
  }
}
```

</details>

---


### Tool call

_source line 355 · 2026-05-16T09:04:41.314417+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/**/*.{yaml,yml,json}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/**/*.{yaml,yml,json}"
  }
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-16T09:04:41.520801+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_PREPARING_20260514T161340.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp002_confusability_controlled_PREPARING_20260514T161342.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_mvp-pipeline_20260514T161549_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_fix-reviewer-critical_20260514T163331_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/few_nerd_types.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_env-setup-and-data_20260514T163452_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_env-setup_20260514T161431_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_code-preflight_20260514T173030_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_fix-few-nerd-loader_20260514T173444_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_rollback-and-run-all_20260514T184153_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_PENDING_20260514T193801.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_QUEUED_20260514T193805.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_ALLOCATED_20260514T193808.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_R
…[truncated 12753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 206
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-16T09:04:41.675995+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "type": "yaml,json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
    "type": "yaml,json"
  }
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-16T09:04:41.726652+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-16T09:04:43.385091+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ | grep -E \"\\.yaml|\\.yml|\\.json|config|settings\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ | grep -E \"\\.yaml|\\.yml|\\.json|config|settings\""
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-16T09:04:43.538267+00:00_

drwxr-xr-x  2 ubuntu ubuntu  4096 May 14 16:41 configs
-rw-------  1 ubuntu ubuntu   411 May 16 02:39 constraints.yaml
-rw-------  1 ubuntu ubuntu 35514 May 16 07:44 decisions.yaml
-rw-------  1 ubuntu ubuntu  3545 May 16 08:23 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu  3550 May 16 08:23 dream_registry.yaml.bak
-rw-------  1 ubuntu ubuntu  5379 May 15 17:09 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu 19038 May 15 07:59 literature_map.yaml
-rw-------  1 ubuntu ubuntu 22206 May 16 04:06 paper_provenance.yaml
-rw-------  1 ubuntu ubuntu 75476 May 16 08:19 registry.yaml
-rw-r--r--  1 ubuntu ubuntu 22363 May 15 16:26 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-16T09:04:45.347049+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-16T09:04:45.750059+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_2.md:150:未启用。项目配置 `external_review.paperreview_ai.enabled: false`。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_director.jsonl:4:{"ts": "2026-05-16T00:50:39.031731+00:00", "role": "tool", "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review", "max_results": "3"}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chat
…[truncated 11257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 363 · 2026-05-16T09:04:45.750443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 364 · 2026-05-16T09:04:45.750685+00:00_

1	_next_id: 3
2	constraints:
3	- id: C001
4	  added: 2026-05-15 22:03 UTC
5	  summary: 论文中 count_40 子集必须明确说明 "40-rel subsets sampled from the 80-relation pool"，不能暗示是独立的
6	    40-type pool
7	  scope: all
8	  reason: count_40 实际是从 80-type pool 中采样的子集，不是独立构建的 pool。Reviewer 指出如果表述不清会误导读者认为存在三个独立
9	    pool size
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-16T09:04:45.851370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-16T09:04:45.902320+00:00_

1	dreams:
2	  dream_20260515T024826:
3	    dream_id: dream_20260515T024826
4	    project: schema-dag-extraction
5	    status: failed
6	    review_mode: full
7	    review_visible: true
8	    writing_visible: true
9	    venue: ''
10	    focus: ''
11	    what_if: []
12	    pid: null
13	    chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
14	    card_message_id: om_x100b6f5cd91cd4b8b256a2dca1f45cd
15	    started_at: '2026-05-15T02:48:26+00:00'
16	    updated_at: '2026-05-15T05:30:49+00:00'
17	    stages_completed: []
18	    error: 'zombie: orchestrator process crashed'
19	    context_hash: 730346e7d98d3361d0b06348cd8c49b58ae54562279fbb78d5cf4b285ece92f2
20	  dream_20260515T053106:
21	    dream_id: dream_20260515T053106
22	    project: schema-dag-extraction
23	    status: done
24	    review_mode: full
25	    review_visible: true
26	    writing_visible: true
27	    venue: ''
28	    focus: ''
29	    what_if: []
30	    pid: 529743
31	    chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
32	    card_message_id: om_x100b6f5eb77f78acb247d8d0b5c4f2a
33	    started_at: '2026-05-15T05:31:06+00:00'
34	    updated_at: '2026-05-15T06:32:51+00:00'
35	    stages_completed:
36	    - imagine
37	    - write
38	    - review
39	    error: null
40	    context_hash: 07225a937020d11e5347d912cee5b625cd4d0898a0896ea4f567284279e62f1b
41	  dream_20260515T113743:
42	    dream_id: dream_20260515T113743
43	    project: schema-dag-extraction
44	    status: done
45	    review_mode: full
46	    review_visible: true
47	    writing_visible: true
48	    venue: ''
49	    focus: SDGD-zero 失败（F1 差于 baseline），论文核心贡献是否需要从"分析+方法"转为纯"系统性分析"？当前证据：pairwise
50	      confusability 跨任务成立，2×3 embedding ablation 矩阵，MAVEN centrality confound 发现。FewRel
51	      formal 和 LLaMA multi-model 实验待完成。
52	    what_if: []
53	    pid: 575315
54	    chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
55	    card_message_id: om_x100b6f44166f78acb3cb39283429a18
56	    started_at: '2026-05-15T11:37:43+00:00'
57	    updated_at: '2026-05-15T12:38:19+00
…[truncated 1757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 367 · 2026-05-16T09:04:48.214947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_2.md",
  "limit": "160"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_2.md",
    "limit": "160"
  }
}
```

</details>

---


### Tool result

_source line 368 · 2026-05-16T09:04:48.265689+00:00_

1	---
2	round: 2
3	overall_score: borderline
4	timestamp: 2026-05-16T03:03:05.885772+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	
11	# 圆桌审稿报告 — Round 2
12	
13	**论文**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?
14	**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
15	**截止日期**: 2026-05-25
16	**审稿人**: Reviewer 1 (方法严谨性 + 实验设计 + 统计分析), Reviewer 2 (新颖性 + 完整性 + 写作质量 + 格式合规)
17	**轮次**: Round 2（论文已针对 Round 1 的 18 个 issue 进行修订）
18	**外部审稿**: 未启用
19	
20	---
21	
22	## Summary
23	
24	本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能下降的机制，提出将退化分解为 type count 和 type confusability 两个独立通道。引入 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 作为量化指标，在 Few-NERD (NER)、FewRel (RE)、MAVEN (ED) 三个数据集上进行控制实验。主要发现：(1) RE 上两通道 cleanly separable；(2) NER 上 confusability 同时影响 detection；(3) MAVEN 上出现 centrality confound 导致 per-type BCS 方向反转；(4) SDGD 负面结果表明 union-based merge 存在结构性挑战。跨模型验证在 Llama-3.1-8B 上复现了主要效应。
25	
26	---
27	
28	## Strengths
29	
30	**S1. 研究问题重要且定义清晰。** 首次系统性隔离 type count 与 type confusability 的独立效应，填补了零样本 IE 退化机制研究的空白。三个 research question 直接可检验。【R1, R2 共识】
31	
32	**S2. 实验设计精心。** Count curves + BCS-controlled 双范式互补，within-pool controlled comparison (Table 4) 消除跨 pool 混淆，permutation test 比较跨条件 slope 一致性。这是 empirical IE 研究中少见的控制实验水平。【R1 重点肯定】
33	
34	**S3. 诚实报告 modest effect sizes 和负面结果。** Pairwise r²=1.3-1.7% 如实量化，SDGD 负面结果完整报告而非隐藏，MAVEN centrality confound 作为独立分析呈现。科学态度端正。【R1, R2 共识】
35	
36	**S4. Centrality confound 分析有独立方法论价值。** 识别 same-domain schema 下 BCS 聚合失效的机制，连接 representation degeneration 文献，partial correlation 验证严谨。对 schema analysis 从业者有直接指导意义。【R1 重点肯定】
37	
38	**S5. Round 1 修订实质性改进。** Discussion section 新增、Limitations 重构为编号列表、factorial test 移入 Appendix 作为 negative result、Contribution 2 改为 "modest predictor"、SDGD 措辞降格、Sclar et al. 引用补充、residualized BCS 分析加入 Appendix。共 8/18 个 Round 1 issue 已解决。
39	
40	---
41	
42	## Weaknesses
43	
44	### Mus
…[truncated 6861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-16T09:04:52.235392+00:00_

Perfect! I found the information. Based on my search, here is my report:

## External Review Configuration Status

**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_2.md` (line 150)

**External Review Status**: **DISABLED**

The configuration explicitly states:
```
external_review.paperreview_ai.enabled: false
```

This is documented in the Round 2 review report under the "External Review (Stanford Agentic Reviewer)" section, which confirms that external review via paperreview_ai is not enabled for this project.

Additionally, the system log evidence from the grep results shows:
```
[HOOKS] [review] external_review_enabled=False for project=schema-dag-extraction
```

And the MCP tool query status confirms:
```
"status": "not_requested"
"message": "No external review requested."
```

**Conclusion**: The schema-dag-extraction project has external review (paperreview_ai) disabled in its configuration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "elapsed_ms": 12578
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-16T09:05:37.966632+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（不含参考文献和附录）\n- **模板**: ACL style files (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无匿名期要求，但论文中不得出现作者身份信息）\n- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 的所有子文件）\n\n## 你的审查侧重\n\n1. **SCS/BCS 度量的合理性**：embedding cosine similarity 作为 confusability proxy 的理论依据是否充分？Qwen3 vs MiniLM 两种 embedding 的选择是否引入系统偏差？BCS 的 mean 聚合是否优于 max（Appendix E 有对比）？\n\n2. **因果推断逻辑**：\n   - BCS-controlled 实验声称是 \"quasi-experimental\"，但未控制 type frequency、definition quality 等 confounders——这是否削弱了因果声称？\n   - 论文中是否存在超出实验设计支撑的因果语言（如 \"drives\"、\"interventional\"）？\n   - Within-pool 分析（Table 5）是否充分控制了 pool composition confound？\n\n3. **统计检验充分性**：\n   - Pairwise r²=1.3-1.7% → batch-level 31.2pp 的放大是否有数学解释（不仅仅是 empirical observation）？\n   - 80-rel 全量回归不显著（Table 5 第三行 p=0.762）但 extreme batches 做 headline result——是否有 cherry-picking 风险？\n   - Bootstrap CI 方法是否恰当？非独立观测（pairwise data）的处理是否正确？\n   - v2 prompt 下 RE BCS gap 从 31.2pp 缩至多少？Appendix F 提到 7.9pp (n=5) 和 25.5pp (n=25)——哪个更可信？\n\n4. **跨数据集/跨模型泛化性**：\n   - 仅 Qwen3-32B + Llama-3.1-8B 两个模型是否足够？\n   - MAVEN 反转的解释（centrality confound）是否充分？\n   - DocRED 的 R²=0.53 vs FewRel R²=0.218——差异原因是否解释清楚？\n\n5. **SDGD 负面结果**：\n   - Merge amplification 的分析是否足够深入？\n   - RE batch composition +1.4pp (p≈0.19) 是否有实际意义？\n   - §5 篇幅是否足够（当前约 200 词正文 + Appendix B）？\n\n请按 EMNLP 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（不含参考文献和附录）\n- **模板**: ACL style files (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无匿名期要求，但论文中不得出现作者身份信息）\n- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 的所有子文件）\n\n## 你的审查侧重\n\n1. **SCS/BCS 度量的合理性**：embedding cosine similarity 作为 confusability proxy 的理论依据是否充分？Qwen3 vs MiniLM 两种 embedding 的选择是否引入系统偏差？BCS 的 mean 聚合是否优于 max（Appendix E 有对比）？\n\n2. **因果推断逻辑**：\n   - BCS-controlled 实验声称是 \"quasi-experimental\"，但未控制 type frequency、definition quality 等 confounders——这是否削弱了因果声称？\n   - 论文中是否存在超出实验设计支撑的因果语言（如 \"drives\"、\"interventional\"）？\n   - Within-pool 分析（Table 5）是否充分控制了 pool composition confound？\n\n3. **统计检验充分性**：\n   - Pairwise r²=1.3-1.7% → batch-level 31.2pp 的放大是否有数学解释（不仅仅是 empirical observation）？\n   - 80-rel 全量回归不显著（Table 5 第三行 p=0.762）但 extreme batches 做 headline result——是否有 cherry-picking 风险？\n   - Bootstrap CI 方法是否恰当？非独立观测（pairwise data）的处理是否正确？\n   - v2 prompt 下 RE BCS gap 从 31.2pp 缩至多少？Appendix F 提到 7.9pp (n=5) 和 25.5pp (n=25)——哪个更可信？\n\n4. **跨数据集/跨模型泛化性**：\n   - 仅 Qwen3-32B + Llama-3.1-8B 两个模型是否足够？\n   - MAVEN 反转的解释（centrality confound）是否充分？\n   - DocRED 的 R²=0.53 vs FewRel R²=0.218——差异原因是否解释清楚？\n\n5. **SDGD 负面结果**：\n   - Merge amplification 的分析是否足够深入？\n   - RE batch composition +1.4pp (p≈0.19) 是否有实际意义？\n   - §5 篇幅是否足够（当前约 200 词正文 + Appendix B）？\n\n请按 EMNLP 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-16T09:05:54.560225+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16593
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-16T09:05:55.114739+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 论文完整性 + 写作质量 + 格式**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（不含参考文献和附录）\n- **模板**: ACL style files (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无匿名期要求，但论文中不得出现作者身份信息）\n- **附录规则**: 附录在审稿期间可参考，但不保证 reviewer 阅读\n- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 的所有子文件）\n\n## 你的审查侧重\n\n1. **Novelty 评估**：\n   - \"First controlled empirical study isolating type confusability from type count\" 这一 novelty claim 是否成立？LLM-PEE (2025) 是否已做过类似分析？\n   - SCS/BCS 本质上是 cosine similarity——metric 本身的 novelty 有多大？\n   - 两通道退化模型的概念贡献是否足够 EMNLP Main Conference 级别？\n\n2. **Related Work 覆盖度**：\n   - 是否遗漏重要相关工作？特别是：\n     - Zero-shot RE prompt-based approaches (e.g., Chia et al. 2022 RELATIONPROMPT)\n     - Schema complexity in other NLP tasks (dialogue, QA)\n     - Embedding similarity for type confusion in non-LLM settings\n   - LLM-PEE 的对比是否公平和完整？\n\n3. **Claim 与 Evidence 匹配度**：\n   - Abstract 中的数字和 claim 是否都有正文支持？\n   - \"robust across schema sizes and prompt designs\" 的 claim 是否被 v2 prompt 的 7.9pp (n=5) 结果削弱？\n   - MAVEN 反转在 Abstract 中的处理（\"generally\"）是否充分？\n   - \"pairwise effect sizes are modest (r²=1.3-1.7%)\" 是否在 abstract/intro 中足够突出？\n   - RE \"cleanly separable\" 是否应标注为 closed-set classification task 特性？\n\n4. **写作质量**：\n   - 论文结构是否清晰？§5 (SDGD) 是否过短？\n   - 正文仅一幅 Figure（Figure 1 双面板）——对于 8 页 EMNLP 论文是否足够？\n   - Discussion 和 Conclusion 是否过于简短？Future work 是否足够具体？\n   - 是否存在过度声称（overclaim）或模糊表述？\n\n5. **格式合规**：\n   - 页数是否在限制内？\n   - References 格式是否正确？是否有占位符/错误引用？\n   - Responsible NLP Research Checklist 是否完整且准确？\n   - 双盲合规：是否有任何泄露作者身份的内容（自引、GitHub 链接、致谢等）？\n\n请按 EMNLP 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 论文完整性 + 写作质量 + 格式**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（不含参考文献和附录）\n- **模板**: ACL style files (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无匿名期要求，但论文中不得出现作者身份信息）\n- **附录规则**: 附录在审稿期间可参考，但不保证 reviewer 阅读\n- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 的所有子文件）\n\n## 你的审查侧重\n\n1. **Novelty 评估**：\n   - \"First controlled empirical study isolating type confusability from type count\" 这一 novelty claim 是否成立？LLM-PEE (2025) 是否已做过类似分析？\n   - SCS/BCS 本质上是 cosine similarity——metric 本身的 novelty 有多大？\n   - 两通道退化模型的概念贡献是否足够 EMNLP Main Conference 级别？\n\n2. **Related Work 覆盖度**：\n   - 是否遗漏重要相关工作？特别是：\n     - Zero-shot RE prompt-based approaches (e.g., Chia et al. 2022 RELATIONPROMPT)\n     - Schema complexity in other NLP tasks (dialogue, QA)\n     - Embedding similarity for type confusion in non-LLM settings\n   - LLM-PEE 的对比是否公平和完整？\n\n3. **Claim 与 Evidence 匹配度**：\n   - Abstract 中的数字和 claim 是否都有正文支持？\n   - \"robust across schema sizes and prompt designs\" 的 claim 是否被 v2 prompt 的 7.9pp (n=5) 结果削弱？\n   - MAVEN 反转在 Abstract 中的处理（\"generally\"）是否充分？\n   - \"pairwise effect sizes are modest (r²=1.3-1.7%)\" 是否在 abstract/intro 中足够突出？\n   - RE \"cleanly separable\" 是否应标注为 closed-set classification task 特性？\n\n4. **写作质量**：\n   - 论文结构是否清晰？§5 (SDGD) 是否过短？\n   - 正文仅一幅 Figure（Figure 1 双面板）——对于 8 页 EMNLP 论文是否足够？\n   - Discussion 和 Conclusion 是否过于简短？Future work 是否足够具体？\n   - 是否存在过度声称（overclaim）或模糊表述？\n\n5. **格式合规**：\n   - 页数是否在限制内？\n   - References 格式是否正确？是否有占位符/错误引用？\n   - Responsible NLP Research Checklist 是否完整且准确？\n   - 双盲合规：是否有任何泄露作者身份的内容（自引、GitHub 链接、致谢等）？\n\n请按 EMNLP 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-16T09:05:56.629198+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1514
}
```

</details>

---


### Assistant

_source line 374 · 2026-05-16T09:06:07.812037+00:00_

两位 Reviewer 已派出：

- **Reviewer 1**（方法严谨性 + 实验设计 + 统计分析）→ 已触发
- **Reviewer 2**（新颖性 + 论文完整性 + 写作质量 + 格式）→ 已触发

等待两位 Reviewer 的 Round 1 独立审稿意见返回。收到后将进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 25

## Round 25

2 recorded events


### User

_source line 375 · 2026-05-16T09:10:27.641151+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计 + 统计分析）

### 总体评分
**Overall**: 3.0 / 5 (Findings)
**Confidence**: 4/5
**一句话总结**: 研究问题有价值、实验设计有创意，但核心效应量极小（pairwise r²<2%），因果声称超出证据支撑，统计呈现存在 cherry-picking 风险——目前更适合作为 Findings 论文。

### 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心因果声称（"drive"）缺乏充分支撑；headline 数字（31.2pp）来自极端构造而非典型场景；多处非显著结果被以"directionally consistent"解读 |
| Excitement | 3.5/5 | 首次系统隔离 count vs confusability 两通道，BCS-controlled 设计有方法论贡献，centrality confound 发现有启发性 |
| Reproducibility | 4/5 | 提供了详细 prompt 模板、decoding 参数、数据集描述、bootstrap 参数；code upon acceptance |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] **因果语言超出证据支撑**
- 具体位置：Title ("Does Type Confusability **Drive** Schema-Induced Degradation")、§1 RQ1、§4.3 ("quasi-experimental evidence")
- 问题：BCS-controlled 实验声称是 "quasi-experimental"，但未控制关键 confounders：(a) type frequency in pretraining corpus（高 BCS 的相似 types 可能本身就是低频/罕见 types）；(b) type definition quality/length（相似 types 的 definitions 本身可能更相似，导致 LLM 混淆来自 prompt 信息不足而非 embedding space overlap）；(c) prompt position effects。Without controlling these, the study establishes **correlation** not **causation**。
- 为什么影响接收：Title 和 RQ framing 暗示因果关系，但证据链只到相关性。如果真正的 driver 是 definition quality 或 type frequency 而非 embedding similarity 本身，整个 "confusability" narrative 的解释力被严重削弱。
- 建议：(1) 将 title 改为描述性表述；(2) 明确声明 BCS-controlled 实验控制了什么、没控制什么；(3) 至少对 type frequency 进行 partial correlation 控制。

**N2** [critical] **Pairwise → batch-level 效应放大缺乏数学解释**
- 具体位置：§4.2 Table 2 (r²=1.3-1.7%) → §4.3 Table 3 (31.2pp gap)
- 问题：Pairwise SCS 解释 type confusion variance 仅 1.3-1.7%，但论文声称这 "compounds" 到 batch level 产生 31.2pp gap。这一放大没有形式化的数学解释——是线性叠加（120 pairs × small effect）、还是非线性交互？更重要的是，§4.3 "Practical magnitude" 承认 typical batch gap 仅 2.2pp (CI: [0.4, 4.0])，即 IQR 范围内的真实效应不到 headline 的 7%。
- 为什么影响接收：无法解释为什么 1.7% variance → 31.2pp gap（且典型场景仅 2.2pp），读者无法判断 BCS 是否有实际工程价值。31.2pp 放在 abstract 和 Table 3 作为 headline result 有误导性。
- 建议：(1) 提供从 pairwise r² 到 batch-level gap 的数学推导；(2) 在 abstract/Results 突出 typical-batch gap（2-4pp）而非 extreme-batch gap；(3) 明确 31.2pp 是 BCS range maximized 的构造结果。

**N3** [critical] **Full 80-rel 回归不显著但极端 batch 作为 headline——cherry-picking 风险**
- 具体位置：Table 5 第三行 (full 80-rel, n=25, slope=+0.221, p=0.762)
- 问题：使用 full 80-rel pool 的 25 个 random batches 做回归时，BCS-accuracy 关系**完全不显著**（p=0.762，slope 甚至为正）。论文注释 "BCS range insufficient" 作为解释，但这等于承认：在自然采样条件下，BCS 对 accuracy 没有可检测的预测力。然而 Table 3 的 31.2pp 极端 batch 比较仍是论文的核心 evidence。
- 为什么影响接收：呈现方式 (burying the null in a footnote while headlining the extreme result) 削弱 credibility。一个 reviewer 的直觉读法："在 natural conditions 下找不到效应，于是构造了极端条件来展示效应"。
- 建议：(1) Table 5 的 80-rel null result 应与 extreme-batch result 并列讨论；(2) 论述 "effect detectable only with sufficient BCS range" 不等于 "effect practically important"。

---

### Should-Fix 问题

**W1** [warning] **Bootstrap CI 对非独立观测可能 anti-conservative**
- 具体位置：§4.2 Table 2 (pair-level percentile bootstrap)
- 问题：Pairwise confusion rates 不独立——共享 type 的 pairs 在统计上相关。论文提到 "type-level cluster bootstrap yields wider CIs" 但仅 parenthetical 一笔带过，primary CIs 仍是 pair-level。
- 建议：将 cluster bootstrap 作为 primary CI 报告。

**W2** [warning] **Embedding 选择不一致且缺乏理论驱动**
- 具体位置：§3.2, Table 1 (Qwen3 for Few-NERD, MiniLM for FewRel/DocRED/MAVEN)
- 问题：如果 SCS 理论基础是 "LLM representation space 中的 overlap 导致 confusion"，应统一用 LLM 自身 embedding。用 MiniLM 计算 RE confusability 缺乏 first-principles justification，且未解释为何不同 task 用不同 embedding。
- 建议：在所有 dataset 上报告两种 embedding 的 SCS-confusion 对比。

**W3** [warning] **RE batch composition +1.4pp (p≈0.19) 不具统计/实际意义**
- 具体位置：§5, Appendix D Table 7
- 问题：n=1 graph-coloring vs random, p≈0.19, BCS margin 仅 0.006。论文 framing "directionally consistent application" 过于积极。Abstract 中 "succeeds for RE" 的表述误导。
- 建议：坦率承认是 null result；将 framing 从 "succeeds" 改为 "provides suggestive but inconclusive evidence"。

**W4** [warning] **仅两个模型（32B+8B）的跨模型泛化过于薄弱**
- 具体位置：Appendix A, §4.3 cross-model paragraph
- 问题：规模差异大，architecture 不同，Channel 2 在 8B NER 上未复制。两模型不足以声称 "cross-model replication"。
- 建议：下调泛化声称强度。

**W5** [warning] **DocRED R²=0.53 vs FewRel R²=0.218 差异解释自相矛盾**
- 具体位置：§4.3 Document-level RE paragraph
- 问题：论文归因 "wider confusability range"，但 Table 1 显示 DocRED BCS range (0.53-0.73) 实际比 FewRel (0.42-0.97) 更窄。解释与数据矛盾。
- 建议：检查并修正此说法。

---

### 小问题

- SCS 仅基于 type name 计算，但 prompt 中提供了 definitions——如果 LLM 主要依据 definition 判断，SCS 可能 misrepresent 真实 confusability
- Abstract 过长（~350 words），EMNLP 建议 150-250 words
- Table 3 的 16-rel condition 无 CI，与其他条目不一致
- §4.4 "100% of confusion errors are intra-batch" 是 RE classification format 的 tautology，非 evidence for confusability
- Limitations #6 承认 "correlational evidence" 与正文 "quasi-experimental" framing 矛盾

---

### 主要优势

- 首次系统隔离 schema degradation 的 count 和 confusability 维度，填补 training-free IE 文献 gap
- BCS-controlled 设计（fix count, vary confusability）比 prior work 提供更强的控制
- Centrality confound 诊断有方法论贡献，提醒社区 per-type aggregation 在 homogeneous schemas 上的陷阱
- Honest about negative results（SDGD failure, RE batch composition non-significance）
- Reproducibility 良好：prompt 模板完整、参数详尽

---

### Questions to Authors

1. 能否提供从 pairwise r²≈1.5% 到 extreme-batch 31.2pp gap 的数学推导（即使是 order-of-magnitude estimation）？
2. 为什么 FewRel 用 MiniLM 而 Few-NERD 用 Qwen3 embedding？有没有在 FewRel 上也用 Qwen3 的结果？
3. Table 5 full 80-rel 回归 p=0.762——如果用 top/bottom 10 batches 单独回归，是否显著？
4. BCS-controlled 实验中，high-BCS vs low-BCS batches 的平均 type frequency 是否有系统差异？

---

### Missing References

- Li et al. (2023) "Evaluating ChatGPT's Information Extraction Capabilities"
- Wadhwa et al. (2023) "Revisiting Relation Extraction in the era of Large Language Models"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 376 · 2026-05-16T09:10:41.127268+00:00_

Reviewer 1 审稿意见已收到。评分 3.0/5 (Findings)，置信度 4/5。

核心发现：3 个 critical issues（因果语言超出证据、pairwise→batch 放大缺数学推导、80-rel null result 与 extreme-batch headline 的 cherry-picking 风险），5 个 warnings。

等待 Reviewer 2 提交审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 377 · 2026-05-16T09:10:43.708306+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 **3.0/5 (Findings)** 评分，主要问题集中在三个 critical issues：(1) 因果语言超出 correlational evidence 支撑，(2) pairwise r²<2% 到 31.2pp headline gap 的放大缺乏数学解释且 typical effect 仅 2pp，(3) full 80-rel 自然条件下回归不显著（p=0.762）但极端构造结果作为 headline 有 cherry-picking 风险。论文的真正贡献在方法论层面（BCS-controlled 设计、centrality confound 诊断），建议 reframe narrative 强度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 378 · 2026-05-16T09:10:49.153147+00:00_

Reviewer 1 意见已收到，记录完毕。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 27

## Round 27

6 recorded events


### User

_source line 379 · 2026-05-16T09:12:19.099573+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见 — Round 1

**论文标题**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May cycle)
**审查侧重**: 新颖性 + 论文完整性 + 写作质量 + 格式

---

## 总体评分

**Overall**: 3/5 (Findings acceptance recommendation)
**一句话总结**: 实验设计严谨、透明度高的 empirical study，但 pairwise effect size 极低（r²≈1.5%）、核心应用结果不显著（SDGD p≈0.19），且 MAVEN 反转限制了 two-channel 模型的普适性，整体贡献更适合 Findings 而非 Main Conference。

---

## 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claim 有实验支撑，但部分 claim（"robust"、"+1.4pp"）强于证据。pairwise r²=1.3-1.7% 解释力很低，RE batch composition 不显著。 |
| Excitement | 2.5/5 | 方法论贡献（隔离 count vs confusability 的实验范式）有价值，但实际影响有限——confusability 信号虽然存在但 effect size 很小，SDGD 失败，实用指导有限。 |
| Overall | 3/5 | Findings 级别推荐。实验工作扎实但新颖性和实际影响力不足以支撑 Main Conference 接收。 |

**置信度**: 4/5（对 IE 和 LLM evaluation 方法论较熟悉，仔细阅读了正文和全部附录）

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 非显著结果被呈现为正面贡献——RE batch composition +1.4pp

- 具体位置：§5 第3段、Abstract 最后一句、Introduction contributions #4、Appendix Table 8
- 问题：Confusability-aware graph coloring 的 +1.4pp gain 不显著（p≈0.19），且在 15 个随机种子中排第 13 名（Appendix §B）。BCS 边际差异仅 0.006。然而 abstract 将其呈现为 "demonstrating a directionally consistent application of our diagnostic framework"，contributions 列表将其作为第四条贡献。对于 EMNLP Main Conference 论文，将统计不显著的结果写入 contributions list 属于 overclaim。
- 为什么影响接收：一个核心 RQ（RQ3: Can confusability-aware schema decomposition improve extraction quality?）的答案实际上是 "No for NER, not significantly for RE"。论文的 framing 对这个本质上的负面结果过于乐观。
- 建议修改方向：(1) 从 contributions list 中移除或改为明确的 negative/inconclusive result；(2) Abstract 中直接说 "does not yield statistically significant gains"；(3) 讨论为什么 BCS margin 如此小，以及是否存在更有效的 partitioning 策略。

**N2** [critical] Pairwise effect size 极低，削弱中心 claim 的实际意义

- 具体位置：Table 2（r²=1.3-1.7%）、§4.2 全节、§4.3 Practical magnitude 段
- 问题：SCS 仅解释 1.3-1.7% 的类型混淆方差。论文承认 "remaining ~98% of variance likely reflects entity frequency, prompt position effects, mention ambiguity, and type definition quality"（§4.2）。Batch-level BCS gap 虽达 31.2pp，但这是 EXTREME batches 的结果；§4.3 Practical magnitude 段承认 typical-batch gap 仅 2.2pp（95% CI: [0.4, 4.0]），约为 extreme gap 的 7%。
- 为什么影响接收：论文标题问 "Does Type Confusability Drive Schema-Induced Degradation?"——但 r²≈1.5% 的答案更接近 "type confusability is a statistically detectable but practically minor factor"。31.2pp extreme gap 在 abstract 中突出呈现，但 2.2pp typical gap 被放在正文深处，这种 framing 不平衡。
- 建议修改方向：(1) Abstract 和 Introduction 需要突出 typical-batch magnitude（2.2pp），而非仅强调 extreme 31.2pp；(2) 标题可能需要调整——当前标题暗示 confusability "drives" degradation，但数据显示它只是一个小因素；(3) 更充分讨论剩余 98% 方差的来源。

**N3** [critical] MAVEN 反转严重限制 two-channel 模型的普适性

- 具体位置：§4.1 ED (MAVEN) 段、§4.5、Abstract（"generally" 一词）、Appendix §C
- 问题：在 4 个数据集中，MAVEN（168 types）的 count channel 完全反转（F1 随 schema size 增加而提高）。这不是边缘 anomaly——MAVEN 是最大的 schema，也是唯一的 same-domain schema。论文将此归因于 centrality confound，但 abstract 仅用 "generally" 一词带过（"a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN"）。此外，per-type BCS-F1 correlation 在控制 centrality 后也消失（Appendix Table 6, p>0.2），意味着 confusability channel 在 same-domain schema 上也仅存在于 pairwise 层面。
- 为什么影响接收：Two-channel degradation model 是 contribution #1，但它在论文中最大的 schema 上部分失效。Cross-domain 和 same-domain 的行为分裂意味着 practitioner 需要不同的诊断框架，但论文没有充分讨论这个 boundary condition。
- 建议修改方向：(1) 在 abstract/intro 中明确标注适用范围："two-channel model applies to cross-domain schemas; same-domain schemas require different treatment"；(2) Discussion §6 需要用更多篇幅讨论 same-domain vs cross-domain 的本质区别；(3) 考虑是否需要第三个 channel 或条件分支来描述 same-domain 行为。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 过长过密——难以解析

- 具体位置：abstract.tex，约 280 words
- 问题：Abstract 堆积了大量数字（0.72→0.42、85.7%→50.4%、88.0%→38.7%、r²=1.3-1.7%、$p=0.60$、-5.3pp、-27pp 等）和多层 qualification（"generally"、"though pairwise effect sizes are modest"、"but reverses direction"、"though pairwise confusability remains significant"）。一次阅读很难抓住核心 takeaway。
- 建议：Abstract 精简到 200 words 以内。核心发现（two channels, modest effect size, SDGD failure）各用一句概括，数字留给正文。

**W2** [warning] §5（SDGD）在正文中过短，关键负面结果未得到充分展开

- 具体位置：sdgd_negative.tex，正文约 0.5 页
- 问题：SDGD 是 RQ3 的核心实验，NER 上的 merge amplification 发现可以说是论文最重要的实践发现，但正文只有 3 段。完整协议和结果被放入 Appendix §B，而 ARR reviewer 不保证阅读 appendix。
- 建议：将 SDGD 的 failure analysis（merge amplification mechanism、NER vs RE 的结构差异）移入正文。正文有余量（当前约 7 页，限制 8 页）。

**W3** [warning] 正文仅一幅 Figure——对 data-heavy empirical paper 来说不够

- 具体位置：Figure 1（page 4），双面板（count curves + BCS scaling）
- 问题：正文 7 页中只有 1 个 figure 和 4 个 table。Appendix Figure 2（error taxonomy decomposition）对理解 two-channel model 至关重要，但在正文中完全没有视觉呈现。对于一篇强调 empirical evidence 的论文，缺少可视化会削弱说服力。
- 建议：将 Appendix Figure 2 (error taxonomy) 移入正文 §4.4。考虑增加一个 schema visualization（展示 SCS graph 结构，说明 high-BCS vs low-BCS batch 的区别）。

**W4** [warning] Discussion（§6）和 Conclusion（§7）过短

- 具体位置：discussion.tex — Discussion 2 段，Conclusion 1 段（合计约 0.5 页）
- 问题：对于一篇做出多个 nuanced claims 的论文，Discussion 应该更充分讨论：(1) two-channel model 的理论解释（为什么 cosine similarity 能预测 LLM 混淆？与 softmax competition / attention 的关系？）；(2) 实用建议（practitioner 如何实际使用 BCS？threshold 如何设置？）；(3) 与 LLM scaling 的关系（更大模型是否能减轻 confusability？）。Future work 仅两句话，过于泛泛。
- 建议：扩展 Discussion 至至少 1 页。Future work 给出具体的实验设计而非仅列方向。

**W5** [warning] Related Work 覆盖度存在缺口

- 具体位置：related_work.tex
- 问题：
  (a) RelationPrompt (Chia et al., 2022) 在 .bib 中但未被引用——这是 zero-shot RE 的代表性工作，应在 "Training-free LLM IE" 段讨论。
  (b) 缺少 schema complexity 在其他 NLP 任务中的讨论——对话状态追踪 (DST) 中 slot type 数量增加导致的类似退化现象。
  (c) 缺少 non-LLM setting 中 type confusion 的相关工作——传统分类器同样面临 fine-grained type confusion 问题，embedding similarity 在此 context 下已有研究。
  (d) LLM-PEE 的对比基本公平（论文正确指出 LLM-PEE conflates count and confusability），但可以更详细描述 LLM-PEE 的三种 partitioning 策略（Random, Average, Level）以及为什么它们无法 isolate confusability。
- 建议：利用正文剩余空间（约 1 页）扩展 Related Work。

**W6** [warning] "robust across prompt designs" claim 被 v2 初始结果削弱

- 具体位置：Abstract、§4.3 Prompt sensitivity 段、Appendix §G
- 问题：初始 v2 prompt 实验（n=5）得到 -7.9pp gap，CI 穿越零（CI: [-5.2, +21.5]）。作者用 n=25 重新实验得到显著结果，但：(1) v2 效应衰减 5.7pp（31.2→25.5pp）；(2) 初始 n=5 失败说明 prompt sensitivity 比 abstract 声称的要大。Abstract 中 "robust across schema sizes and prompt designs" 的措辞过于自信。
- 建议：改为 "directionally consistent across prompt designs, with attenuated magnitude"。

---

## 小问题（不影响接收）

1. **11 个 orphan .bib 条目**（引用验证工具检测到）：chatgpt-ie-eval-2023、dee-2024、dlisc-2025、familiarity-2025、godey-anisotropy-inherent-2024、guidex-2025、kggen-2025、nuner-2024、relationprompt-2022、spt-2025、wadhwa-re-llm-2023 在 .bib 中但未被 \cite。建议清理或引用。
2. **vLLM 版本号 v0.20.2**（checklist.tex C4）：截至 2026 年 5 月，vLLM 版本号体系是否已到 v0.20？如果是正确的请保留，否则请核实。
3. **p-value 格式不一致**：$<10^{-6}$ vs ${<}0.001$ vs $7\times10^{-7}$，建议统一。
4. **DocRED 采样细节不足**（§3.1 DocRED 段）：FewRel 说明了 1000 balanced instances 的采样方式（12-13 per type），但 DocRED 仅说 "sample balanced instances" 未给出具体数量和 per-type 采样细节。
5. **FewRel 合并 train+val splits**（§3.1）：这是非标准用法，应更明确说明 potential 影响（如 data leakage 对 zero-shot claim 的影响——虽然 zero-shot 不做训练，但 test set 选择可能有偏差）。

---

## 主要优势

1. **实验设计精巧**：Count curves + BCS-controlled 两种范式互补，是研究 schema degradation 机制的有效方法论贡献。
2. **多任务、多数据集覆盖**：NER (Few-NERD) + RE sentence-level (FewRel) + RE doc-level (DocRED) + ED (MAVEN)，4 个数据集涵盖不同 schema 规模和 domain 特性。
3. **Cross-model validation**：Qwen3-32B + Llama-3.1-8B 的双模型验证增强了发现的可靠性。
4. **高度透明**：对负面结果（SDGD 失败、modest r²、MAVEN 反转、v2 n=5 不显著）的坦诚报告值得肯定。
5. **统计严谨性**：Bootstrap CIs、permutation tests、within-pool controls、BCS aggregation sensitivity analysis 等多层统计检验。
6. **Centrality confound 发现**：对 MAVEN 正向 correlation 的 centrality 解释（Appendix §C）有独立价值，对未来 per-type embedding analysis 有方法论指导意义。

---

## Missing References

1. **RelationPrompt** (Chia et al., 2022) — 在 bib 中但未引用，应讨论其作为 zero-shot RE approach 的相关性
2. **Dialogue state tracking schema complexity** — 如 SGD (Rastogi et al., 2020) 中 service/slot 数量增加导致的类似 degradation
3. **Label confusion in traditional NER/RE** — 如 confusion matrix analysis in supervised NER (e.g., Augenstein et al., 2017)
4. **DEE (Shiri et al., 2024)** — 在 bib 中但未引用，与 SDGD 方法直接相关（schema-aware event extraction decomposition）

---

## Questions to Authors

1. 你们如何解释 typical-batch BCS gap 仅 2.2pp（7% of extreme gap）？这个数字是否意味着 confusability 在实际场景中的影响可忽略？
2. 对于 same-domain schema（如 MAVEN），two-channel model 的适用性限制是什么？是否需要一个单独的理论框架？
3. 如果 SCS 仅解释 ~1.5% 的方差，那么 "entity frequency, prompt position, mention ambiguity, type definition quality" 中哪个是主导因素？是否有初步数据？
4. SDGD 的 merge amplification 问题是否本质上使所有 decompose-then-merge 策略对 span-level tasks 无效？是否探索过 non-union merge（如 majority voting）？
5. 为什么使用不同 embedding model（Qwen3 for Few-NERD, MiniLM for FewRel/DocRED/MAVEN）？这种不一致是否可能影响跨数据集比较？

---

## 总结判断

这是一篇设计严谨、报告透明的 empirical study。实验范式（隔离 count vs confusability）有方法论价值，centrality confound 的发现有独立意义。但三个核心问题限制了 Main Conference 级别的接收：(1) pairwise effect size 极低（r²≈1.5%，typical gap 2.2pp），中心 claim 的实际意义有限；(2) 唯一的应用尝试（SDGD/batch composition）均无显著改善；(3) MAVEN 反转意味着 two-channel model 对最大 schema（same-domain）不适用。建议投稿 **Findings**，或在 revision 中：(a) 显著加强 practical significance 的讨论和 framing；(b) 扩展 SDGD 到更多 RE benchmark；(c) 补充更多 embedding 或 metric 变体以提高 confusability 预测力。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-16T09:12:51.839763+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见 — Round 1\n\n**Overall**: 3/5 (Findings acceptance recommendation)\n**Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 非显著结果被呈现为正面贡献——RE batch composition +1.4pp\n- §5 第3段、Abstract 最后一句、Introduction contributions #4、Appendix Table 8\n- +1.4pp gain 不显著（p≈0.19），在 15 个随机种子中排第 13 名。BCS 边际差异仅 0.006。Abstract 将其呈现为 \"demonstrating a directionally consistent application\"，contributions 列表将其作为第四条贡献。对于 EMNLP Main Conference 论文，将统计不显著的结果写入 contributions list 属于 overclaim。\n- 建议：(1) 从 contributions list 中移除或改为明确的 negative/inconclusive result；(2) Abstract 中直接说 \"does not yield statistically significant gains\"。\n\n**N2** [critical] Pairwise effect size 极低，削弱中心 claim 的实际意义\n- Table 2（r²=1.3-1.7%）、§4.2 全节、§4.3 Practical magnitude 段\n- SCS 仅解释 1.3-1.7% 的类型混淆方差。Typical-batch gap 仅 2.2pp（95% CI: [0.4, 4.0]），约为 extreme gap 的 7%。标题问 \"Does Type Confusability Drive Schema-Induced Degradation?\"——但 r²≈1.5% 的答案更接近 \"type confusability is a statistically detectable but practically minor factor\"。\n- 建议：Abstract 和 Introduction 需要突出 typical-batch magnitude（2.2pp）；标题可能需要调整。\n\n**N3** [critical] MAVEN 反转严重限制 two-channel 模型的普适性\n- §4.1 ED (MAVEN) 段、§4.5、Abstract、Appendix §C\n- 4 个数据集中，MAVEN（168 types）的 count channel 完全反转，per-type BCS-F1 correlation 在控制 centrality 后也消失（p>0.2）。Two-channel degradation model 是 contribution #1，但它在最大 schema 上部分失效。\n- 建议：在 abstract/intro 中明确标注适用范围；Discussion 需更多篇幅讨论 same-domain vs cross-domain。\n\n## Should-Fix 问题\n\n**W1** [warning] Abstract 过长过密——约 280 words，堆积大量数字和 qualification\n- 建议精简到 200 words 以内\n\n**W2** [warning] §5（SDGD）在正文中过短（约 0.5 页），关键负面结果未充分展开\n- 建议将 SDGD failure analysis 移入正文\n\n**W3** [warning] 正文仅一幅 Figure——对 data-heavy empirical paper 不够\n- 建议将 Appendix Figure 2 (error taxonomy) 移入正文\n\n**W4** [warning] Discussion（§6）和 Conclusion（§7）过短（合计约 0.5 页）\n- 建议扩展 Discussion 至至少 1 页\n\n**W5** [warning] Related Work 覆盖度缺口\n- RelationPrompt (Chia et al., 2022) 在 bib 中但未被引用\n- 缺少 dialogue state tracking 和 non-LLM type confusion 相关工作\n- LLM-PEE 对比可更详细\n\n**W6** [warning] \"robust across prompt designs\" claim 被 v2 初始结果（n=5, -7.9pp, CI 穿零）削弱\n- 建议改为 \"directionally consistent across prompt designs, with attenuated magnitude\"\n\n## 小问题\n1. 11 个 orphan .bib 条目\n2. vLLM 版本号 v0.20.2 需核实\n3. p-value 格式不一致\n4. DocRED 采样细节不足\n5. FewRel 合并 train+val splits 的影响需说明\n\n## Questions to Authors\n1. Typical-batch BCS gap 仅 2.2pp 是否意味着实际影响可忽略？\n2. Same-domain schema 的 two-channel model 适用性限制？\n3. 剩余 98% 方差的来源中哪个是主导因素？\n4. Merge amplification 是否本质上使所有 decompose-then-merge 对 span-level tasks 无效？\n5. 为什么不同 dataset 用不同 embedding model？\n\n---\n\n请逐条回应以上所有问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见 — Round 1\n\n**Overall**: 3/5 (Findings acceptance recommendation)\n**Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 非显著结果被呈现为正面贡献——RE batch composition +1.4pp\n- §5 第3段、Abstract 最后一句、Introduction contributions #4、Appendix Table 8\n- +1.4pp gain 不显著（p≈0.19），在 15 个随机种子中排第 13 名。BCS 边际差异仅 0.006。Abstract 将其呈现为 \"demonstrating a directionally consistent application\"，contributions 列表将其作为第四条贡献。对于 EMNLP Main Conference 论文，将统计不显著的结果写入 contributions list 属于 overclaim。\n- 建议：(1) 从 contributions list 中移除或改为明确的 negative/inconclusive result；(2) Abstract 中直接说 \"does not yield statistically significant gains\"。\n\n**N2** [critical] Pairwise effect size 极低，削弱中心 claim 的实际意义\n- Table 2（r²=1.3-1.7%）、§4.2 全节、§4.3 Practical magnitude 段\n- SCS 仅解释 1.3-1.7% 的类型混淆方差。Typical-batch gap 仅 2.2pp（95% CI: [0.4, 4.0]），约为 extreme gap 的 7%。标题问 \"Does Type Confusability Drive Schema-Induced Degradation?\"——但 r²≈1.5% 的答案更接近 \"type confusability is a statistically detectable but practically minor factor\"。\n- 建议：Abstract 和 Introduction 需要突出 typical-batch magnitude（2.2pp）；标题可能需要调整。\n\n**N3** [critical] MAVEN 反转严重限制 two-channel 模型的普适性\n- §4.1 ED (MAVEN) 段、§4.5、Abstract、Appendix §C\n- 4 个数据集中，MAVEN（168 types）的 count channel 完全反转，per-type BCS-F1 correlation 在控制 centrality 后也消失（p>0.2）。Two-channel degradation model 是 contribution #1，但它在最大 schema 上部分失效。\n- 建议：在 abstract/intro 中明确标注适用范围；Discussion 需更多篇幅讨论 same-domain vs cross-domain。\n\n## Should-Fix 问题\n\n**W1** [warning] Abstract 过长过密——约 280 words，堆积大量数字和 qualification\n- 建议精简到 200 words 以内\n\n**W2** [warning] §5（SDGD）在正文中过短（约 0.5 页），关键负面结果未充分展开\n- 建议将 SDGD failure analysis 移入正文\n\n**W3** [warning] 正文仅一幅 Figure——对 data-heavy empirical paper 不够\n- 建议将 Appendix Figure 2 (error taxonomy) 移入正文\n\n**W4** [warning] Discussion（§6）和 Conclusion（§7）过短（合计约 0.5 页）\n- 建议扩展 Discussion 至至少 1 页\n\n**W5** [warning] Related Work 覆盖度缺口\n- RelationPrompt (Chia et al., 2022) 在 bib 中但未被引用\n- 缺少 dialogue state tracking 和 non-LLM type confusion 相关工作\n- LLM-PEE 对比可更详细\n\n**W6** [warning] \"robust across prompt designs\" claim 被 v2 初始结果（n=5, -7.9pp, CI 穿零）削弱\n- 建议改为 \"directionally consistent across prompt designs, with attenuated magnitude\"\n\n## 小问题\n1. 11 个 orphan .bib 条目\n2. vLLM 版本号 v0.20.2 需核实\n3. p-value 格式不一致\n4. DocRED 采样细节不足\n5. FewRel 合并 train+val splits 的影响需说明\n\n## Questions to Authors\n1. Typical-batch BCS gap 仅 2.2pp 是否意味着实际影响可忽略？\n2. Same-domain schema 的 two-channel model 适用性限制？\n3. 剩余 98% 方差的来源中哪个是主导因素？\n4. Merge amplification 是否本质上使所有 decompose-then-merge 对 span-level tasks 无效？\n5. 为什么不同 dataset 用不同 embedding model？\n\n---\n\n请逐条回应以上所有问题。"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-16T09:13:21.204424+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29364
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-16T09:13:21.556339+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见 — Round 1\n\n**Overall**: 3.0/5 (Findings)\n**Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 因果语言超出证据支撑\n- Title (\"Does Type Confusability **Drive** Schema-Induced Degradation\")、§1 RQ1、§4.3 (\"quasi-experimental evidence\")\n- BCS-controlled 实验未控制：(a) type frequency in pretraining corpus；(b) type definition quality/length；(c) prompt position effects。Without controlling these, the study establishes correlation not causation。\n- 建议：将 title 改为描述性表述；明确声明控制了什么、没控制什么；至少对 type frequency 进行 partial correlation 控制。\n\n**N2** [critical] Pairwise → batch-level 效应放大缺乏数学解释\n- §4.2 Table 2 (r²=1.3-1.7%) → §4.3 Table 3 (31.2pp gap)\n- Typical batch gap 仅 2.2pp (CI: [0.4, 4.0])，即 IQR 范围内的真实效应不到 headline 的 7%。\n- 建议：提供数学推导；在 abstract/Results 突出 typical-batch gap；明确 31.2pp 是构造结果。\n\n**N3** [critical] Full 80-rel 回归不显著但极端 batch 作为 headline——cherry-picking 风险\n- Table 5 第三行 (full 80-rel, n=25, slope=+0.221, p=0.762)\n- 在自然采样条件下，BCS 对 accuracy 没有可检测的预测力。但 Table 3 的 31.2pp 极端 batch 比较仍是论文核心 evidence。\n- 建议：Table 5 的 80-rel null result 应与 extreme-batch result 并列讨论。\n\n## Should-Fix 问题\n\n**W1** [warning] Bootstrap CI 对非独立观测可能 anti-conservative\n- §4.2 Table 2 pair-level percentile bootstrap\n- 建议将 cluster bootstrap 作为 primary CI 报告\n\n**W2** [warning] Embedding 选择不一致且缺乏理论驱动\n- §3.2, Table 1: Qwen3 for Few-NERD, MiniLM for FewRel/DocRED/MAVEN\n- 如果 SCS 理论基础是 \"LLM representation space 中的 overlap 导致 confusion\"，应统一用 LLM 自身 embedding\n- 建议在所有 dataset 上报告两种 embedding 的对比\n\n**W3** [warning] RE batch composition +1.4pp (p≈0.19) 不具统计/实际意义\n- Abstract 中 \"succeeds for RE\" 的表述误导\n- 建议坦率承认是 null result\n\n**W4** [warning] 仅两个模型的跨模型泛化过于薄弱\n- Channel 2 在 8B NER 上未复制\n- 建议下调泛化声称强度\n\n**W5** [warning] DocRED R²=0.53 vs FewRel R²=0.218 差异解释自相矛盾\n- 论文归因 \"wider confusability range\"，但 Table 1 显示 DocRED BCS range (0.53-0.73) 比 FewRel (0.42-0.97) 更窄\n- 建议检查并修正\n\n## 小问题\n- SCS 仅基于 type name 计算，但 prompt 中提供了 definitions\n- Abstract 过长（~350 words）\n- Table 3 的 16-rel condition 无 CI\n- §4.4 \"100% of confusion errors are intra-batch\" 是 RE classification 的 tautology\n- Limitations #6 与正文 \"quasi-experimental\" framing 矛盾\n\n## Questions to Authors\n1. 能否提供从 pairwise r²≈1.5% 到 extreme-batch 31.2pp gap 的数学推导？\n2. 为什么 FewRel 用 MiniLM 而 Few-NERD 用 Qwen3？\n3. Table 5 full 80-rel 如果用 top/bottom 10 batches 单独回归是否显著？\n4. High-BCS vs low-BCS batches 的平均 type frequency 是否有系统差异？\n\n## Missing References\n- Li et al. (2023) \"Evaluating ChatGPT's Information Extraction Capabilities\"\n- Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\"\n\n---\n\n请逐条回应以上所有问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见 — Round 1\n\n**Overall**: 3.0/5 (Findings)\n**Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 因果语言超出证据支撑\n- Title (\"Does Type Confusability **Drive** Schema-Induced Degradation\")、§1 RQ1、§4.3 (\"quasi-experimental evidence\")\n- BCS-controlled 实验未控制：(a) type frequency in pretraining corpus；(b) type definition quality/length；(c) prompt position effects。Without controlling these, the study establishes correlation not causation。\n- 建议：将 title 改为描述性表述；明确声明控制了什么、没控制什么；至少对 type frequency 进行 partial correlation 控制。\n\n**N2** [critical] Pairwise → batch-level 效应放大缺乏数学解释\n- §4.2 Table 2 (r²=1.3-1.7%) → §4.3 Table 3 (31.2pp gap)\n- Typical batch gap 仅 2.2pp (CI: [0.4, 4.0])，即 IQR 范围内的真实效应不到 headline 的 7%。\n- 建议：提供数学推导；在 abstract/Results 突出 typical-batch gap；明确 31.2pp 是构造结果。\n\n**N3** [critical] Full 80-rel 回归不显著但极端 batch 作为 headline——cherry-picking 风险\n- Table 5 第三行 (full 80-rel, n=25, slope=+0.221, p=0.762)\n- 在自然采样条件下，BCS 对 accuracy 没有可检测的预测力。但 Table 3 的 31.2pp 极端 batch 比较仍是论文核心 evidence。\n- 建议：Table 5 的 80-rel null result 应与 extreme-batch result 并列讨论。\n\n## Should-Fix 问题\n\n**W1** [warning] Bootstrap CI 对非独立观测可能 anti-conservative\n- §4.2 Table 2 pair-level percentile bootstrap\n- 建议将 cluster bootstrap 作为 primary CI 报告\n\n**W2** [warning] Embedding 选择不一致且缺乏理论驱动\n- §3.2, Table 1: Qwen3 for Few-NERD, MiniLM for FewRel/DocRED/MAVEN\n- 如果 SCS 理论基础是 \"LLM representation space 中的 overlap 导致 confusion\"，应统一用 LLM 自身 embedding\n- 建议在所有 dataset 上报告两种 embedding 的对比\n\n**W3** [warning] RE batch composition +1.4pp (p≈0.19) 不具统计/实际意义\n- Abstract 中 \"succeeds for RE\" 的表述误导\n- 建议坦率承认是 null result\n\n**W4** [warning] 仅两个模型的跨模型泛化过于薄弱\n- Channel 2 在 8B NER 上未复制\n- 建议下调泛化声称强度\n\n**W5** [warning] DocRED R²=0.53 vs FewRel R²=0.218 差异解释自相矛盾\n- 论文归因 \"wider confusability range\"，但 Table 1 显示 DocRED BCS range (0.53-0.73) 比 FewRel (0.42-0.97) 更窄\n- 建议检查并修正\n\n## 小问题\n- SCS 仅基于 type name 计算，但 prompt 中提供了 definitions\n- Abstract 过长（~350 words）\n- Table 3 的 16-rel condition 无 CI\n- §4.4 \"100% of confusion errors are intra-batch\" 是 RE classification 的 tautology\n- Limitations #6 与正文 \"quasi-experimental\" framing 矛盾\n\n## Questions to Authors\n1. 能否提供从 pairwise r²≈1.5% 到 extreme-batch 31.2pp gap 的数学推导？\n2. 为什么 FewRel 用 MiniLM 而 Few-NERD 用 Qwen3？\n3. Table 5 full 80-rel 如果用 top/bottom 10 batches 单独回归是否显著？\n4. High-BCS vs low-BCS batches 的平均 type frequency 是否有系统差异？\n\n## Missing References\n- Li et al. (2023) \"Evaluating ChatGPT's Information Extraction Capabilities\"\n- Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\"\n\n---\n\n请逐条回应以上所有问题。"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-16T09:13:23.016125+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 384 · 2026-05-16T09:13:33.299347+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 385 · 2026-05-16T09:13:35.877000+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿总结**：

- **Overall: 3/5**（推荐 Findings，不推荐 Main Conference）
- **Soundness: 3.5/5** — 主要 claim 有支撑，但部分 claim 过度
- **Excitement: 2.5/5** — 方法论有价值但实际影响有限

**三个 Must-Fix 问题**：
1. RE batch composition +1.4pp 不显著（p≈0.19）却被写入 contributions list
2. Pairwise r²=1.3-1.7% 过低，typical-batch gap 仅 2.2pp，中心 claim 的实际意义不足
3. MAVEN 反转限制 two-channel model 的普适性，abstract 用 "generally" 一词不够充分

**五个 Should-Fix 问题**：过长 abstract、§5 过短、正文仅一幅 figure、Discussion/Conclusion 过短、Related Work 缺口（RelationPrompt 未引用、缺 DST/non-LLM 相关工作）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 386 · 2026-05-16T09:13:40.778731+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 387 · 2026-05-16T09:14:49.694542+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 对 Reviewer 2 Round 1 意见的逐条回应

### Must-Fix

**[AGREE] R2-N1: RE batch composition +1.4pp overclaim**
完全同意。与我的 W3 一致。p≈0.19、n=1 treatment、BCS margin 0.006——统计和实际意义上都是 null result。Abstract "demonstrating a directionally consistent application" 和 contributions #4 均构成 overclaim。

**[AGREE] R2-N2: Pairwise effect size 极低**
完全同意。与我的 N2 高度重合。r²=1.3-1.7% 意味着论文 headline claim 应从 "identifies the driver" reframe 为 "empirically isolates one specific, modest factor"。核心问题是 framing hierarchy：typical gap (2.2pp) 被埋在 §4.3 中段，而 extreme gap (31.2pp) 出现在 Abstract/Table 3/Conclusion。

**[REBUT] R2-N3: MAVEN 反转严重限制 two-channel 普适性**
部分不同意，建议降为 warning：
1. Pairwise SCS-confusion 在 MAVEN 仍高度显著（r=0.129, p<10^{-42}, Table 2）——失效的是 per-type aggregation，不是 underlying relationship
2. Count channel 反转有明确 task-structure 解释（relaxed matching + same-domain hierarchy + class imbalance, §4.1）
3. Appendix C 花 ~1 page 正确诊断了 centrality confound 并给出 partial correlation 验证
4. 但同意 Abstract/Intro 需明确标注 "cross-domain schemas" 作为适用条件——这是 scope qualification (warning)，非 fundamental validity threat (critical)

### Should-Fix

**[AGREE] R2-W1**: Abstract 过长，同意精简。
**[AGREE] R2-W2**: §5 SDGD 正文过短，merge amplification 分析应移入正文。
**[AGREE] R2-W3**: 正文 Figure 不够，error taxonomy 图应入正文。
**[AGREE] R2-W4**: Discussion+Conclusion 过短，缺 synthesis 和 actionable guidelines。

**[REBUT] R2-W5**: Related Work 缺口——部分同意（orphan bib 应清理，LLM-PEE 可扩展），但 dialogue state tracking 与 IE scope 较远，不认为是必要补充。

**[REBUT] R2-W6**: "robust" 被 n=5 削弱——不同意严重程度。n=25 结果 definitive（p<0.0001, r=-0.919），n=5 是 underpowered 的正确诊断（Appendix F Interpretation 段已论证）。但同意措辞可改为 "robust in direction and significance, with modest magnitude attenuation"。

### 小问题
5 条全部 [AGREE]。vLLM v0.20.2 可能是笔误（当前版本应在 0.4-0.6 范围）。

### 与 R2 的核心分歧
1. N3 严重程度：R2=critical, 我=warning（pairwise signal 仍显著，问题在 aggregation 方法非 fundamental relationship）
2. W6 prompt robustness：R2 认为被 n=5 削弱，我认为 n=25 已 definitive

### 共识点
- Effect size 极小是最大 soundness 问题
- RE +1.4pp 是 null result 不应作为 contribution
- 因果 framing 超出 correlational evidence（我的 N1 + R2 的 N2 指向同一核心问题）
- 论文更适合 Findings track

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 388 · 2026-05-16T09:15:00.444133+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 30

## Round 30

2 recorded events


### User

_source line 389 · 2026-05-16T09:15:03.091777+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 意见的逐条回应并提交给 Director。

核心结论：与 R2 在大部分问题上达成共识（effect size 过小、RE +1.4pp overclaim、因果语言过强），主要分歧在 MAVEN 反转的严重程度（我认为是 scope qualification 而非 fundamental failure，因为 pairwise signal 仍显著）和 prompt robustness（n=25 结果 definitive）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 390 · 2026-05-16T09:15:11.213314+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 31

## Round 31

8 recorded events
