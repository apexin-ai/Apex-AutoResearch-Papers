# Research conversation: 系统通知：审稿审批已通过。请开始审稿。 [论文提交] - 项目: distill_sparse_swiglu - 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 117
- **Recorded user turns:** 8
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-2/6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a.jsonl`
- **Structured JSON:** [`0d62a20f285d02837993.json`](../../sessions/0d/0d62a20f285d02837993.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-24T04:20:54.897Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T04:20:54.897Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "content": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: distill_sparse_swiglu\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

---

### Runtime record

_source line 2 · 2026-05-24T04:20:54.900Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T04:20:54.900Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

## Round 1

82 recorded events

### User

_source line 3 · 2026-05-24T04:20:54.933Z_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "ef08c6fb-e624-47ee-b4bb-e68a426067ad",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-24T04:20:54.933Z_

```json
{
  "parentUuid": "ef08c6fb-e624-47ee-b4bb-e68a426067ad",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__dispatch_visual_check",
      "mcp__agent-ml-research__get_external_review_status",
      "mcp__agent-ml-research__get_visual_check_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__request_external_review",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__submit_review_report_to_research_director",
      "mcp__agent-ml-research__update_review_issues"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__dispatch_visual_check",
      "mcp__agent-ml-research__get_external_review_status",
      "mcp__agent-ml-research__get_visual_check_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__request_external_review",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__submit_review_report_to_research_director",
      "mcp__agent-ml-research__update_review_issues"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "8d38a364-4052-439d-849a-019277cd9ea6",
  "timestamp": "2026-05-24T04:20:54.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-24T04:20:54.933Z_

```json
{
  "parentUuid": "8d38a364-4052-439d-849a-019277cd9ea6",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "8466cddd-b1b8-4c72-9211-454ac28c7b81",
  "timestamp": "2026-05-24T04:20:54.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-24T04:20:54.933Z_

```json
{
  "parentUuid": "8466cddd-b1b8-4c72-9211-454ac28c7b81",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "af7052c8-8e06-4bb6-9771-6a94c3829839",
  "timestamp": "2026-05-24T04:20:54.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Assistant

_source line 8 · 2026-05-24T04:20:57.564Z_

<details><summary>Logged reasoning block</summary>

```text
The user is asking me to start a review process. Let me first read the review-director-session-start skill to get the full review flow.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af7052c8-8e06-4bb6-9771-6a94c3829839",
  "isSidechain": false,
  "requestId": "req_011CbLkd69dnQMGoPLr3untA",
  "type": "assistant",
  "uuid": "11a94d66-469d-417c-8d46-f5e7c453ebc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNX655niPddzq5UxuHiMFH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16513,
      "cache_read_input_tokens": 11841,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16513
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T04:20:58.088Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ez8hDof2JC5MPJE9k9gFqK`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11a94d66-469d-417c-8d46-f5e7c453ebc4",
  "isSidechain": false,
  "requestId": "req_011CbLkd69dnQMGoPLr3untA",
  "type": "assistant",
  "uuid": "f6236097-1bbc-4d66-a302-2af2e40244ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNX655niPddzq5UxuHiMFH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16513,
      "cache_read_input_tokens": 11841,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16513
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T04:20:58.104Z_

<details><summary>↩ Tool result · `toolu_01Ez8hDof2JC5MPJE9k9gFqK`</summary>

````text
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
68	- 如果到 Step 4 时外部结果仍未返回，调用 `get_external_review_status(project)` 确认状态，在报告中标注
69	
70	### Step 0.7 — 视觉审查派发（与 Step 1 并行）
71	
72	派发独立视觉审查 Agent，与 Reviewer 审稿并行执行：
73	
74	```
75	dispatch_visual_check(project="{project}", review_chat_id="{review_chat_id}")
76	```
77	
78	- 视觉审查 Agent 自动渲染论文 PDF 并逐页检查排版质量（Figure 1 位置、布局节奏、图表质量、空白分布等）
79	- **不参与评分和交叉讨论**，结果仅作为参考信息
80	- 启动和完成通知自动发送到 Group C
81	- 结果在 Step 4 通过 `get_visual_check_status(project)` 读取并拼入报告
82	- **fire-and-forget**：调用立即返回，本步骤永不等待视觉审查完成
83	
84	### Step 1 — Round N：独立审稿
85	
86	携带 Step 0 搜到的 venue 要求，启动所有 Reviewer：
87	
88	```
89	director_post_to_reviewer(reviewer_id="1", round_number=N, text="你负责 {focus}。...")
90	director_post_to_reviewer(reviewer_id="2", round_number=N, text="你负责 {focus}。...")
91	...（按需）
92	```
93	
94	消息中必须包含：
95	- venue 名称和截止日期
96	- 页数限制和模板名称
97	- 匿名规则
98	- 论文文件路径
99	- **该 Reviewer 的审查侧重**（在消息中明确指定）
100	
101	收集所有 Reviewer 的审稿结果。
102	
103	### Step 2 — 交叉分享（原文转发 + 逐条回应）
104	
105	将每位 Reviewer 的**完整审稿原文**转发给其他 Reviewer，要求逐条回应：
106	
107	```
108	director_post_to_reviewer(reviewer_id="2", round_number=N, text="""
109	以下是 Reviewer 1 的完整审稿意见：
110	
111	{Reviewer 1 的原文}
112	
113	请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。
114	""")
115	```
116	
117	对每位 Reviewer 重复此步骤（每人看到其他所有 Reviewer 的原文）。
118	
119	收集所有交叉回应。
120	
121	### Step 3 — 收敛判断
122	
123	分析所有 Reviewer 的意见和交叉回应：
124	
125	- **关键问题已达成共识**（`[AGREE]` 占多数，无未解决的 `[REBUT]` 矛盾）→ 进入 Step 4
126	- **存在重大分歧**（关键 issue 上有 `[REBUT]` 且双方各有道理）→ 回到 Step 1 开始下一轮，附带聚焦问题
127	- **最多 3 轮**：如果第 3 轮仍有分歧，在报告中如实记录各方观点
128	
129	### Step 4 — 汇总报告 & 投递
130	
131	合并所有轮次的发现，形成统一审稿报告：
132	
133	1. 报告结构：
134	   - **Summary**：论文概述（2-3 句）
135	   - **Strengths**：优点（逐条列出）
136	   - **Weaknesses**：缺点（逐条列出，这是重点，必须严格）
137	   - **Reviewer Consensus**：所有 Reviewer 达成共识的关键问题（标注 `[AGREE]`）
138	   - **Reviewer Divergence**：分歧点及各方理由（标注 `[REBUT]`，如有）
139	   - **Questions**：需要作者澄清的问题
140	   - **Missing References**：遗漏的重要相关工作
141	   - **External Review (Stanford Agentic Reviewer)**：如有外部审稿结果，单独列出其 7 维评分、关键发现、以及与内部审稿的差异；如未返回则标注状态
142	   - **Visual Layout Check**（非评分项，不阻塞报告）：调用 `get_visual_check_status(project)` 读一次状态——
143	     - `done` → 直接拼入 findings
144	     - `running` → 写"仍在进行中，本报告不等待，完成后会自动补发到 Group C"
145	     - `timeout` / `error` → 写失败原因 + 提示用户可重新触发
146	     - `not_started` → 写未派发
147	     不要为视觉审查推迟报告投递。视觉 Agent 完成后会自己把结果发到 Group C，与本报告解耦。可直接调用 `format_visual_findings_for_report(project)` 拿到现成的 markdown section
148	   - **Overall Assessment**：总评 + 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度
149	   - **Detailed Comments**：逐节详细意见
150	2. **同步 Issue Tracker**（投递前必做）：
151	   - 用 `read_local_file("projects/{project}/artifacts/review_issues.yaml")` 读当前 tracker（不存在视为空）
152	   - 对本轮所有 Weakness/Must-Fix/Should-Fix:
153	     - 与已有 issue 匹配（同 category + 相似 summary）→ 在 `mentions` 追加本轮记录,更新 `last_seen_round`
154	     - 新问题 → 创建条目（id=`R{reviewer}-W{n}`,status=`open`,first_raised_round=本轮）
155	   - 对上轮 `open`/`in_progress` 但本轮**未被任何 Reviewer 提及**的:
156	     - 在 `mentions` 追加 `note: "本轮未提及,可能已修复,待 Research Director 确认"`
157	   - 调 `update_review_issues(project, issues_yaml=完整 YAML)` 写回
158	3. 调用 `submit_review_report_to_research_director` 投递报告 → Research Director
159	4. 向用户（Group C）汇报审核完成
160	
161	此流程只在 session 启动时执行一次。
162	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "f6236097-1bbc-4d66-a302-2af2e40244ca",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "0dd9e616-91a5-4445-8ba5-6b03a4114cac",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
      "content": "---\nname: review-director-session-start\ndescription: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。\npriority: 9\nscope: global\ntags:\n- workflow\n- review\n- session\nversion: 3\nroles:\n- review_director\n---\n\n# Review Director Session 启动流程（圆桌会议模式）\n\n## 初始化\n\n1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）\n2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在\n3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）\n4. 向用户简要汇报：\n   - **投稿目标**：venue 和 deadline\n   - **论文状态**：当前草稿位置和版本\n   - **资料完整性**：提交的材料是否齐全\n   - **下一步**：即将开始的圆桌审稿流程\n\n## 评审流程（收到论文提交后执行）\n\n### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）\n\n1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全\n2. 确认目标投稿 venue（从提交消息中获取）\n3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：\n   - `\"&lt;venue name> 2026 call for papers\" site:aclweb.org`\n   - `\"&lt;venue name> 2026 submission deadline\"`\n   - `\"&lt;venue name> 2026 author guidelines\"`\n4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续\n5. 提取当前版本的格式要求：\n   - 页数限制（正文 / 附录 / 参考文献）\n   - 模板（ACL / IEEE / NeurIPS / ICML / ...）\n   - 匿名规则（double-blind / single-blind / open）\n   - 附录规则（是否允许、是否参与审稿）\n   - 引用格式（natbib / biblatex / 特定 .bst）\n6. 将以上信息作为上下文，随任务一起传递给 Reviewer\n\n⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。\n\n### Step 0.5 — 决定 Reviewer 编排\n\n根据 venue 类型和论文特点，决定：\n- 需要几个 Reviewer（1-5 人）\n- 每个 Reviewer 的审查侧重\n\n参考：\n- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）\n- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）\n- **Workshop / 短文**：1 人（全面审查）\n\n向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。\n\n### Step 0.6 — 外部审稿线（与 Step 1 并行）\n\n检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：\n- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片\n- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程\n- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告\n- 如果到 Step 4 时外部结果仍未返回，调用 `get_external_review_status(project)` 确认状态，在报告中标注\n\n### Step 0.7 — 视觉审查派发（与 Step 1 并行）\n\n派发独立视觉审查 Agent，与 Reviewer 审稿并行执行：\n\n```\ndispatch_visual_check(project=\"{project}\", review_chat_id=\"{review_chat_id}\")\n```\n\n- 视觉审查 Agent 自动渲染论文 PDF 并逐页检查排版质量（Figure 1 位置、布局节奏、图表质量、空白分布等）\n- **不参与评分和交叉讨论**，结果仅作为参考信息\n- 启动和完成通知自动发送到 Group C\n- 结果在 Step 4 通过 `get_visual_check_status(project)` 读取并拼入报告\n- **fire-and-forget**：调用立即返回，本步骤永不等待视觉审查完成\n\n### Step 1 — Round N：独立审稿\n\n携带 Step 0 搜到的 venue 要求，启动所有 Reviewer：\n\n```\ndirector_post_to_reviewer(reviewer_id=\"1\", round_number=N, text=\"你负责 {focus}。...\")\ndirector_post_to_reviewer(reviewer_id=\"2\", round_number=N, text=\"你负责 {focus}。...\")\n...（按需）\n```\n\n消息中必须包含：\n- venue 名称和截止日期\n- 页数限制和模板名称\n- 匿名规则\n- 论文文件路径\n- **该 Reviewer 的审查侧重**（在消息中明确指定）\n\n收集所有 Reviewer 的审稿结果。\n\n### Step 2 — 交叉分享（原文转发 + 逐条回应）\n\n将每位 Reviewer 的**完整审稿原文**转发给其他 Reviewer，要求逐条回应：\n\n```\ndirector_post_to_reviewer(reviewer_id=\"2\", round_number=N, text=\"\"\"\n以下是 Reviewer 1 的完整审稿意见：\n\n{Reviewer 1 的原文}\n\n请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\"\"\")\n```\n\n对每位 Reviewer 重复此步骤（每人看到其他所有 Reviewer 的原文）。\n\n收集所有交叉回应。\n\n### Step 3 — 收敛判断\n\n分析所有 Reviewer 的意见和交叉回应：\n\n- **关键问题已达成共识**（`[AGREE]` 占多数，无未解决的 `[REBUT]` 矛盾）→ 进入 Step 4\n- **存在重大分歧**（关键 issue 上有 `[REBUT]` 且双方各有道理）→ 回到 Step 1 开始下一轮，附带聚焦问题\n- **最多 3 轮**：如果第 3 轮仍有分歧，在报告中如实记录各方观点\n\n### Step 4 — 汇总报告 & 投递\n\n合并所有轮次的发现，形成统一审稿报告：\n\n1. 报告结构：\n   - **Summary**：论文概述（2-3 句）\n   - **Strengths**：优点（逐条列出）\n   - **Weaknesses**：缺点（逐条列出，这是重点，必须严格）\n   - **Reviewer Consensus**：所有 Reviewer 达成共识的关键问题（标注 `[AGREE]`）\n   - **Reviewer Divergence**：分歧点及各方理由（标注 `[REBUT]`，如有）\n   - **Questions**：需要作者澄清的问题\n   - **Missing References**：遗漏的重要相关工作\n   - **External Review (Stanford Agentic Reviewer)**：如有外部审稿结果，单独列出其 7 维评分、关键发现、以及与内部审稿的差异；如未返回则标注状态\n   - **Visual Layout Check**（非评分项，不阻塞报告）：调用 `get_visual_check_status(project)` 读一次状态——\n     - `done` → 直接拼入 findings\n     - `running` → 写\"仍在进行中，本报告不等待，完成后会自动补发到 Group C\"\n     - `timeout` / `error` → 写失败原因 + 提示用户可重新触发\n     - `not_started` → 写未派发\n     不要为视觉审查推迟报告投递。视觉 Agent 完成后会自己把结果发到 Group C，与本报告解耦。可直接调用 `format_visual_findings_for_report(project)` 拿到现成的 markdown section\n   - **Overall Assessment**：总评 + 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度\n   - **Detailed Comments**：逐节详细意见\n2. **同步 Issue Tracker**（投递前必做）：\n   - 用 `read_local_file(\"projects/{project}/artifacts/review_issues.yaml\")` 读当前 tracker（不存在视为空）\n   - 对本轮所有 Weakness/Must-Fix/Should-Fix:\n     - 与已有 issue 匹配（同 category + 相似 summary）→ 在 `mentions` 追加本轮记录,更新 `last_seen_round`\n     - 新问题 → 创建条目（id=`R{reviewer}-W{n}`,status=`open`,first_raised_round=本轮）\n   - 对上轮 `open`/`in_progress` 但本轮**未被任何 Reviewer 提及**的:\n     - 在 `mentions` 追加 `note: \"本轮未提及,可能已修复,待 Research Director 确认\"`\n   - 调 `update_review_issues(project, issues_yaml=完整 YAML)` 写回\n3. 调用 `submit_review_report_to_research_director` 投递报告 → Research Director\n4. 向用户（Group C）汇报审核完成\n\n此流程只在 session 启动时执行一次。\n",
      "numLines": 162,
      "startLine": 1,
      "totalLines": 162
    }
  },
  "sourceToolAssistantUUID": "f6236097-1bbc-4d66-a302-2af2e40244ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Assistant

_source line 11 · 2026-05-24T04:21:09.768Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to follow the review flow. Let me start with the initialization steps:

1. Get project overview
2. Check paper file status
3. Do venue research (web search for EMNLP 2026 CFP)
4. Check existing review issues

Let me start with Step 0 - initialization and resource checking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dd9e616-91a5-4445-8ba5-6b03a4114cac",
  "isSidechain": false,
  "requestId": "req_011CbLkdKqQ8nHdfmiXLnY1N",
  "type": "assistant",
  "uuid": "b2644b5d-fb95-449a-a08e-08398906235f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AaMn3kzCiUr736iA85v4Qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3452,
      "cache_read_input_tokens": 28354,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 28354,
          "cache_creation_input_tokens": 3452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3452
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-24T04:21:10.280Z_

开始审稿流程。先执行初始化和资料检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2644b5d-fb95-449a-a08e-08398906235f",
  "isSidechain": false,
  "requestId": "req_011CbLkdKqQ8nHdfmiXLnY1N",
  "type": "assistant",
  "uuid": "800506da-7b68-476b-be27-04e2f294ccfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AaMn3kzCiUr736iA85v4Qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3452,
      "cache_read_input_tokens": 28354,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 28354,
          "cache_creation_input_tokens": 3452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3452
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T04:21:12.334Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QbiTBZ8Ud8s8r5K95SNpm4`</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,WebFetch",
  "max_results": 11
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "800506da-7b68-476b-be27-04e2f294ccfc",
  "isSidechain": false,
  "requestId": "req_011CbLkdKqQ8nHdfmiXLnY1N",
  "type": "assistant",
  "uuid": "e551880f-92e5-4d13-a2cb-5fb1b48c3847",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AaMn3kzCiUr736iA85v4Qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3452,
      "cache_read_input_tokens": 28354,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 28354,
          "cache_creation_input_tokens": 3452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3452
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T04:21:12.339Z_

<details><summary>↩ Tool result · `toolu_01QbiTBZ8Ud8s8r5K95SNpm4`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e551880f-92e5-4d13-a2cb-5fb1b48c3847",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "085459d3-cfdc-40bd-b424-f304d7a8a92d",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,WebFetch",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "e551880f-92e5-4d13-a2cb-5fb1b48c3847",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: distill_sparse_swiglu - 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR - 截止日期…",
  "leafUuid": "085459d3-cfdc-40bd-b424-f304d7a8a92d",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Tool call

_source line 17 · 2026-05-24T04:21:29.462Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01BRzMVze7VKv8yuTZdWeiK8`</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "085459d3-cfdc-40bd-b424-f304d7a8a92d",
  "isSidechain": false,
  "requestId": "req_011CbLkeNj4VEnBs6x3z3y2b",
  "type": "assistant",
  "uuid": "fcd66ca1-0fbf-4322-9bde-43e826b19840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEk4Sc6D4ZddTqS41C9Hi3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 31806,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 31806,
          "cache_creation_input_tokens": 1275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1275
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T04:21:30.503Z_

<details><summary>↩ Tool result · `toolu_01BRzMVze7VKv8yuTZdWeiK8`</summary>

```text
{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (408 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- qwen14b_kl30_s123_gsm8k_v4: Rerun s123 GSM8K eval (v3 failed: HF network unreachable). Added source /etc/network_turbo + HF_DATASETS_OFFLINE fallback.（准备中）\n- qwen14b_kl30_s123_gsm8k_v3: Rerun s123 GSM8K eval (v2 failed: python not found, conda not activated). Checkpoint on westd-34887.（准备中）\n- qwen14b_kl30_s123_gsm8k_v2: Rerun s123 GSM8K eval to confirm data completeness — original run (qwen14b_kl30_s123_gsm8k) was killed after ~2.5h on unreachable westd-41718, cannot verify sample_len=1319. Checkpoint available on westd-34887.（准备中）\n\n## 近期结论\n- **perlayer_kl_k4_s42** (success): Per-layer KL distillation with K=4 active layers per step and adaptive lambda scheduling can train the sparsity predictor to achieve avg KL < 0.05 while maintaining ~28% sparsity across all 32 layers.\n- **mse30_s123_downstream** (success): MSE-trained predictor at 30% sparsity (seed 123) preserves downstream task performance comparable to dense baseline because MSE distillation captures sufficient activation magnitude information to maintain task-relevant features in the sparse SwiGLU network.\n\n## 趋势\n成功 258 / 负向 24 / 失败 40 / 共 404\narc_challenge_acc_norm: 0.3737 ↓（近 3 次 success）\ngsm8k_exact_match: 0.0174 ↓（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- mvp_kl_s123: 已被终止 — unknown\n- mvp_kl_s456: 已被终止 — unknown\n- kl_lagrangian_v2: 已被终止 — unknown\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123: 训练失败 — unknown\n- mvp_kl_norm_s456: 已被终止 — unknown\n- kl_norm_v3_quicktest: 已被终止 — unknown\n- spon_kl_s42: 已被终止 — unknown\n- spon_training_seq2048: 已被终止 — unknown\n- spon_2048_s42: 已被终止 — unknown\n- ste_kl_s42: 已被终止 — unknown\n- bce_isocompute_s42: 训练失败 — unknown\n- eval_spon_supp_retry: 训练失败 — unknown\n- bce_isocompute_s42_v2: 已被终止 — unknown\n- spon_supp_eval_retry: 训练失败 — unknown\n- bce_isocompute_v2_s42: 已被终止 — unknown\n- kl_sparsity30_s42: 已被终止 — unknown\n- kl_sparsity70_s42: 已被终止 — unknown\n- kl_sparsity70_s42_v2: 已被终止 — unknown\n- lm_eval_dense_test: 训练失败 — unknown\n- lm_eval_mistral_downstream: 训练失败 — unknown\n- diag_30pct_downstream: 已被终止 — unknown\n- diag_gsm8k_gencomp: 已被终止 — unknown\n- diag_teal_downstream: 已被终止 — unknown\n- bench_mistral_kl50_s42: 已被终止 — unknown\n- longbench_kl30_uniform: 训练失败 — unknown\n- longbench_dense: 训练失败 — unknown\n- longbench_kl30_uniform_v2: 训练失败 — unknown\n- longbench_dense_v2: 训练失败 — unknown\n- longbench_kl30_uniform_v3: 训练失败 — unknown\n- longbench_dense_v3: 训练失败 — unknown\n- longbench_dense_v4: 训练失败 — unknown\n- longbench_dense_v5: 已被终止 — unknown\n- steps_curve_s42: 已被终止 — unknown\n- steps_curve_s42_v2: 已被终止 — unknown\n- mag_preservation_reg: 训练失败 — unknown\n- reverse_kl_50pct_s42: 已被终止 — unknown\n- jsd_50pct_s42: 已被终止 — unknown\n- kl50_s456_train_eval: 已被终止 — unknown\n- c4_download: 已被终止 — unknown\n- qwen14b_kl30_uniform_eval: 训练失败 — unknown\n- qwen14b_teal30_uniform_eval: 训练失败 — unknown\n- qwen14b_kl30_uniform_eval"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcd66ca1-0fbf-4322-9bde-43e826b19840",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "67a427bc-ac7a-485f-b2f8-28b670e242f1",
  "toolUseResult": "{\"result\":\"# 项目 distill_sparse_swiglu 概况\\n\\n## 实验状态 (408 个)\\n\\n- **eval_spon_supp_retry**: DONE (failed) — \\n- **lm_eval_dense_test**: DONE (failed) — \\n- **lm_eval_mistral_downstream**: DONE (failed) — \\n- **mvp_kl_s123**: DONE (killed) — \\n- **mvp_kl_s456**: DONE (killed) — \\n- **kl_sparsity70_s42**: DONE (killed) — \\n- **kl_sparsity30_s42**: DONE (killed) — \\n- **ste_baseline_s42**: DONE (success) — \\n- **spon_supp_eval_retry**: DONE (failed) — \\n- **bce_isocompute_s42**: DONE (failed) — \\n- **ste_kl_s42**: DONE (killed) — \\n- **spon_training_seq2048**: DONE (killed) — \\n- **mvp_kl_norm_s123**: DONE (failed) — \\n- **mvp_kl_norm_s42**: DONE (failed) — \\n- **kl_normalized_quicktest**: DONE (failed) — \\n\\n## 最新报告\\n# Handover — 2026-05-24\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- qwen14b_kl30_s123_gsm8k_v4: Rerun s123 GSM8K eval (v3 failed: HF network unreachable). Added source /etc/network_turbo + HF_DATASETS_OFFLINE fallback.（准备中）\\n- qwen14b_kl30_s123_gsm8k_v3: Rerun s123 GSM8K eval (v2 failed: python not found, conda not activated). Checkpoint on westd-34887.（准备中）\\n- qwen14b_kl30_s123_gsm8k_v2: Rerun s123 GSM8K eval to confirm data completeness — original run (qwen14b_kl30_s123_gsm8k) was killed after ~2.5h on unreachable westd-41718, cannot verify sample_len=1319. Checkpoint available on westd-34887.（准备中）\\n\\n## 近期结论\\n- **perlayer_kl_k4_s42** (success): Per-layer KL distillation with K=4 active layers per step and adaptive lambda scheduling can train the sparsity predictor to achieve avg KL < 0.05 while maintaining ~28% sparsity across all 32 layers.\\n- **mse30_s123_downstream** (success): MSE-trained predictor at 30% sparsity (seed 123) preserves downstream task performance comparable to dense baseline because MSE distillation captures sufficient activation magnitude information to maintain task-relevant features in the sparse SwiGLU network.\\n\\n## 趋势\\n成功 258 / 负向 24 / 失败 40 / 共 404\\narc_challenge_acc_norm: 0.3737 ↓（近 3 次 success）\\ngsm8k_exact_match: 0.0174 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-34887: 无 GPU 信息\\n\\n## 告警\\n- mvp_kl_s123: 已被终止 — unknown\\n- mvp_kl_s456: 已被终止 — unknown\\n- kl_lagrangian_v2: 已被终止 — unknown\\n- kl_normalized_quicktest: 训练失败 — unknown\\n- mvp_kl_norm_s42: 训练失败 — unknown\\n- mvp_kl_norm_s123: 训练失败 — unknown\\n- mvp_kl_norm_s456: 已被终止 — unknown\\n- kl_norm_v3_quicktest: 已被终止 — unknown\\n- spon_kl_s42: 已被终止 — unknown\\n- spon_training_seq2048: 已被终止 — unknown\\n- spon_2048_s42: 已被终止 — unknown\\n- ste_kl_s42: 已被终止 — unknown\\n- bce_isocompute_s42: 训练失败 — unknown\\n- eval_spon_supp_retry: 训练失败 — unknown\\n- bce_isocompute_s42_v2: 已被终止 — unknown\\n- spon_supp_eval_retry: 训练失败 — unknown\\n- bce_isocompute_v2_s42: 已被终止 — unknown\\n- kl_sparsity30_s42: 已被终止 — unknown\\n- kl_sparsity70_s42: 已被终止 — unknown\\n- kl_sparsity70_s42_v2: 已被终止 — unknown\\n- lm_eval_dense_test: 训练失败 — unknown\\n- lm_eval_mistral_downstream: 训练失败 — unknown\\n- diag_30pct_downstream: 已被终止 — unknown\\n- diag_gsm8k_gencomp: 已被终止 — unknown\\n- diag_teal_downstream: 已被终止 — unknown\\n- bench_mistral_kl50_s42: 已被终止 — unknown\\n- longbench_kl30_uniform: 训练失败 — unknown\\n- longbench_dense: 训练失败 — unknown\\n- longbench_kl30_uniform_v2: 训练失败 — unknown\\n- longbench_dense_v2: 训练失败 — unknown\\n- longbench_kl30_uniform_v3: 训练失败 — unknown\\n- longbench_dense_v3: 训练失败 — unknown\\n- longbench_dense_v4: 训练失败 — unknown\\n- longbench_dense_v5: 已被终止 — unknown\\n- steps_curve_s42: 已被终止 — unknown\\n- steps_curve_s42_v2: 已被终止 — unknown\\n- mag_preservation_reg: 训练失败 — unknown\\n- reverse_kl_50pct_s42: 已被终止 — unknown\\n- jsd_50pct_s42: 已被终止 — unknown\\n- kl50_s456_train_eval: 已被终止 — unknown\\n- c4_download: 已被终止 — unknown\\n- qwen14b_kl30_uniform_eval: 训练失败 — unknown\\n- qwen14b_teal30_uniform_eval: 训练失败 — unknown\\n- qwen14b_kl30_uniform_eval\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (408 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- qwen14b_kl30_s123_gsm8k_v4: Rerun s123 GSM8K eval (v3 failed: HF network unreachable). Added source /etc/network_turbo + HF_DATASETS_OFFLINE fallback.（准备中）\n- qwen14b_kl30_s123_gsm8k_v3: Rerun s123 GSM8K eval (v2 failed: python not found, conda not activated). Checkpoint on westd-34887.（准备中）\n- qwen14b_kl30_s123_gsm8k_v2: Rerun s123 GSM8K eval to confirm data completeness — original run (qwen14b_kl30_s123_gsm8k) was killed after ~2.5h on unreachable westd-41718, cannot verify sample_len=1319. Checkpoint available on westd-34887.（准备中）\n\n## 近期结论\n- **perlayer_kl_k4_s42** (success): Per-layer KL distillation with K=4 active layers per step and adaptive lambda scheduling can train the sparsity predictor to achieve avg KL < 0.05 while maintaining ~28% sparsity across all 32 layers.\n- **mse30_s123_downstream** (success): MSE-trained predictor at 30% sparsity (seed 123) preserves downstream task performance comparable to dense baseline because MSE distillation captures sufficient activation magnitude information to maintain task-relevant features in the sparse SwiGLU network.\n\n## 趋势\n成功 258 / 负向 24 / 失败 40 / 共 404\narc_challenge_acc_norm: 0.3737 ↓（近 3 次 success）\ngsm8k_exact_match: 0.0174 ↓（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- mvp_kl_s123: 已被终止 — unknown\n- mvp_kl_s456: 已被终止 — unknown\n- kl_lagrangian_v2: 已被终止 — unknown\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123: 训练失败 — unknown\n- mvp_kl_norm_s456: 已被终止 — unknown\n- kl_norm_v3_quicktest: 已被终止 — unknown\n- spon_kl_s42: 已被终止 — unknown\n- spon_training_seq2048: 已被终止 — unknown\n- spon_2048_s42: 已被终止 — unknown\n- ste_kl_s42: 已被终止 — unknown\n- bce_isocompute_s42: 训练失败 — unknown\n- eval_spon_supp_retry: 训练失败 — unknown\n- bce_isocompute_s42_v2: 已被终止 — unknown\n- spon_supp_eval_retry: 训练失败 — unknown\n- bce_isocompute_v2_s42: 已被终止 — unknown\n- kl_sparsity30_s42: 已被终止 — unknown\n- kl_sparsity70_s42: 已被终止 — unknown\n- kl_sparsity70_s42_v2: 已被终止 — unknown\n- lm_eval_dense_test: 训练失败 — unknown\n- lm_eval_mistral_downstream: 训练失败 — unknown\n- diag_30pct_downstream: 已被终止 — unknown\n- diag_gsm8k_gencomp: 已被终止 — unknown\n- diag_teal_downstream: 已被终止 — unknown\n- bench_mistral_kl50_s42: 已被终止 — unknown\n- longbench_kl30_uniform: 训练失败 — unknown\n- longbench_dense: 训练失败 — unknown\n- longbench_kl30_uniform_v2: 训练失败 — unknown\n- longbench_dense_v2: 训练失败 — unknown\n- longbench_kl30_uniform_v3: 训练失败 — unknown\n- longbench_dense_v3: 训练失败 — unknown\n- longbench_dense_v4: 训练失败 — unknown\n- longbench_dense_v5: 已被终止 — unknown\n- steps_curve_s42: 已被终止 — unknown\n- steps_curve_s42_v2: 已被终止 — unknown\n- mag_preservation_reg: 训练失败 — unknown\n- reverse_kl_50pct_s42: 已被终止 — unknown\n- jsd_50pct_s42: 已被终止 — unknown\n- kl50_s456_train_eval: 已被终止 — unknown\n- c4_download: 已被终止 — unknown\n- qwen14b_kl30_uniform_eval: 训练失败 — unknown\n- qwen14b_teal30_uniform_eval: 训练失败 — unknown\n- qwen14b_kl30_uniform_eval"
    }
  },
  "sourceToolAssistantUUID": "fcd66ca1-0fbf-4322-9bde-43e826b19840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T04:21:30.904Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XCC1HLGyGjpPs8xQLnfCiz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67a427bc-ac7a-485f-b2f8-28b670e242f1",
  "isSidechain": false,
  "requestId": "req_011CbLkeNj4VEnBs6x3z3y2b",
  "type": "assistant",
  "uuid": "4e5756e1-c85a-41fd-a9e9-f91e2c9455c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEk4Sc6D4ZddTqS41C9Hi3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 31806,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 31806,
          "cache_creation_input_tokens": 1275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1275
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T04:21:30.909Z_

<details><summary>↩ Tool result · `toolu_01XCC1HLGyGjpPs8xQLnfCiz`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	% \input{ethics}  % removed per submission guidelines
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e5756e1-c85a-41fd-a9e9-f91e2c9455c0",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "f372a313-6ee5-44cd-b9ad-2ec3282d476c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n% \\usepackage{inconsolata} % not available on this system\n\\usepackage{graphicx}\n\\graphicspath{{../figures/paper/}}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 2pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 2pt}\n\\setlength{\\intextsep}{8pt plus 2pt minus 2pt}\n\n\\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\\input{limitations}\n% \\input{ethics}  % removed per submission guidelines\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  },
  "sourceToolAssistantUUID": "4e5756e1-c85a-41fd-a9e9-f91e2c9455c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T04:21:31.781Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016HL5GFhgCdkcb4bsp3HhHk`</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f372a313-6ee5-44cd-b9ad-2ec3282d476c",
  "isSidechain": false,
  "requestId": "req_011CbLkeNj4VEnBs6x3z3y2b",
  "type": "assistant",
  "uuid": "f8998c73-46c3-47ec-8289-ed89c0c6b442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEk4Sc6D4ZddTqS41C9Hi3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 31806,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 31806,
          "cache_creation_input_tokens": 1275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1275
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T04:21:38.848Z_

<details><summary>↩ Tool result · `toolu_016HL5GFhgCdkcb4bsp3HhHk`</summary>

```text
Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found several results related to EMNLP 2026, though the search didn't return a specific main call for papers page for EMNLP 2026 itself. However, I did find relevant information about submission guidelines through the ACL ecosystem.

Based on the search results, here's what I found about EMNLP 2026 submission guidelines:

## Key Information about EMNLP 2026 ARR Submissions

EMNLP 2025 uses ACL Rolling Review (ARR) as a reviewing system, but final decisions are made by the conference, and EMNLP 2026 is expected to follow a similar process.

Both submissions of articles for review and commitment of reviewed articles to the conference are performed via the Open Review platform. Authors follow a two-step process: they submit articles to ARR where submissions receive reviews and meta-reviews from ARR reviewers and action editors, and then authors commit their reviewed articles to a publication venue like EMNLP.

## Important Details:

- During the ARR submission process, authors are required to specify which co-authors are committing to cover reviewing in that reviewing cycle
- The reviewing process is double-blind, with reviewers not seeing authors, and authors not seeing reviewers and reviews on ARR which are not made publicly visible
- Authors are given the option through ARR to make their anonymized submitted articles publicly visible

For the most comprehensive and up-to-date submission guidelines specific to EMNLP 2026, I recommend checking the official EMNLP 2026 conference website or the ACL Rolling Review system directly at https://aclrollingreview.org/cfp, as the search results primarily showed information about EMNLP 2025 and other 2026 conferences using the ARR system.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8998c73-46c3-47ec-8289-ed89c0c6b442",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "a99c45c6-d35b-49c7-aa08-cf13f494f065",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org",
    "results": [
      {
        "tool_use_id": "srvtoolu_016vmmekXgW2UYypiJ2VpJuC",
        "content": [
          {
            "title": "[EMNLP 2025] First Call for Papers | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"
          },
          {
            "title": "5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"
          },
          {
            "title": "Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"
          },
          {
            "title": "EACL 2026: First Call for Papers | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"
          },
          {
            "title": "Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"
          },
          {
            "title": "EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"
          },
          {
            "title": "First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"
          },
          {
            "title": "Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"
          }
        ]
      },
      "I found several results related to EMNLP 2026, though the search didn't return a specific main call for papers page for EMNLP 2026 itself. However, I did find relevant information about submission guidelines through the ACL ecosystem.\n\nBased on the search results, here's what I found about EMNLP 2026 submission guidelines:\n\n## Key Information about EMNLP 2026 ARR Submissions\n\nEMNLP 2025 uses ACL Rolling Review (ARR) as a reviewing system, but final decisions are made by the conference, and EMNLP 2026 is expected to follow a similar process.\n\nBoth submissions of articles for review and commitment of reviewed articles to the conference are performed via the Open Review platform. Authors follow a two-step process: they submit articles to ARR where submissions receive reviews and meta-reviews from ARR reviewers and action editors, and then authors commit their reviewed articles to a publication venue like EMNLP.\n\n## Important Details:\n\n- During the ARR submission process, authors are required to specify which co-authors are committing to cover reviewing in that reviewing cycle\n- The reviewing process is double-blind, with reviewers not seeing authors, and authors not seeing reviewers and reviews on ARR which are not made publicly visible\n- Authors are given the option through ARR to make their anonymized submitted articles publicly visible\n\nFor the most comprehensive and up-to-date submission guidelines specific to EMNLP 2026, I recommend checking the official EMNLP 2026 conference website or the ACL Rolling Review system directly at https://aclrollingreview.org/cfp, as the search results primarily showed information about EMNLP 2025 and other 2026 conferences using the ARR system."
    ],
    "durationSeconds": 7.063006694000003
  },
  "sourceToolAssistantUUID": "f8998c73-46c3-47ec-8289-ed89c0c6b442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-24T04:21:41.939Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for more specific EMNLP 2026 CFP information and ARR submission guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a99c45c6-d35b-49c7-aa08-cf13f494f065",
  "isSidechain": false,
  "requestId": "req_011CbLkgKtD6kSpeMmDY6r3q",
  "type": "assistant",
  "uuid": "f646ef18-481e-43b2-baf1-3be885658f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018e5qbCtBMYE8AUQd9BXNjp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3777,
      "cache_read_input_tokens": 33081,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 33081,
          "cache_creation_input_tokens": 3777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3777
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T04:21:43.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016yBM8HNX6ofFCyeBi2QWX1`</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f646ef18-481e-43b2-baf1-3be885658f97",
  "isSidechain": false,
  "requestId": "req_011CbLkgKtD6kSpeMmDY6r3q",
  "type": "assistant",
  "uuid": "fed2a2b2-c5ae-4d09-a30d-c211303b9b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018e5qbCtBMYE8AUQd9BXNjp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3777,
      "cache_read_input_tokens": 33081,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 33081,
          "cache_creation_input_tokens": 3777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3777
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T04:21:43.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sf2uaMZCGTBtbqmsnyNpee`</summary>

```json
{
  "query": "EMNLP 2026 call for papers commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fed2a2b2-c5ae-4d09-a30d-c211303b9b13",
  "isSidechain": false,
  "requestId": "req_011CbLkgKtD6kSpeMmDY6r3q",
  "type": "assistant",
  "uuid": "bbb4ec9f-1a4a-4532-a61e-edf4f363516c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018e5qbCtBMYE8AUQd9BXNjp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3777,
      "cache_read_input_tokens": 33081,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 33081,
          "cache_creation_input_tokens": 3777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3777
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T04:21:45.306Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M85W1nBzyiWHUVj9PkMhGu`</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the full submission guidelines for ARR: page limits for long and short papers, formatting requirements, anonymity rules, template requirements, appendix rules, citation format, and any other submission requirements. Also find the upcoming submission deadlines for 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbb4ec9f-1a4a-4532-a61e-edf4f363516c",
  "isSidechain": false,
  "requestId": "req_011CbLkgKtD6kSpeMmDY6r3q",
  "type": "assistant",
  "uuid": "dabbcaae-6859-43ae-b655-8066de89adf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018e5qbCtBMYE8AUQd9BXNjp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3777,
      "cache_read_input_tokens": 33081,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 33081,
          "cache_creation_input_tokens": 3777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3777
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: distill_sparse_swiglu - 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR - 截止日期…",
  "leafUuid": "dabbcaae-6859-43ae-b655-8066de89adf2",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Tool result

_source line 29 · 2026-05-24T04:21:47.695Z_

<details><summary>↩ Tool result · `toolu_01Sf2uaMZCGTBtbqmsnyNpee`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here is the information about the EMNLP 2026 call for papers commitment deadline:

The EMNLP commitment deadline is August 2, 2026. 

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

To provide additional context: Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link. This means that the commitment deadline applies to papers that have already been reviewed through the ACL Rolling Review (ARR) process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbb4ec9f-1a4a-4532-a61e-edf4f363516c",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "43bb7d08-77ed-4057-9294-ef7953ed05b6",
  "toolUseResult": {
    "query": "EMNLP 2026 call for papers commitment deadline",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JRKg2orn5YhLxR1qTDRT4e",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot",
            "url": "https://www.getpaperpilot.com/deadlines/emnlp-2026.html"
          },
          {
            "title": "Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"
          },
          {
            "title": "AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "emnlp 2026 - AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/conference/?id=emnlp26"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "Call for workshops: EMNLP & AACL",
            "url": "https://groups.google.com/g/ml-news/c/W-fucfhVto4"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X",
            "url": "https://x.com/emnlpmeeting/status/2047754845919031450"
          }
        ]
      },
      "Based on the search results, here is the information about the EMNLP 2026 call for papers commitment deadline:\n\nThe EMNLP commitment deadline is August 2, 2026. \n\nAll deadlines are 11:59PM UTC-12:00 (\"anywhere on Earth\").\n\nTo provide additional context: Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link. This means that the commitment deadline applies to papers that have already been reviewed through the ACL Rolling Review (ARR) process."
    ],
    "durationSeconds": 4.222445293000004
  },
  "sourceToolAssistantUUID": "bbb4ec9f-1a4a-4532-a61e-edf4f363516c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T04:21:49.285Z_

<details><summary>↩ Tool result · `toolu_016yBM8HNX6ofFCyeBi2QWX1`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references – so that reviewers' comments can be taken into account. Final versions of short papers may have up to five (5) pages, plus unlimited pages for acknowledgments and references.

## Format Requirements

The paper follows ACL formatting. You are encouraged to use the ACL pubcheck tool to check for common problems. There is an official Overleaf template. Note that this template has a [review] setting that must be on for the submission.

ARR abandons the MS Word Template for conference submissions. The submissions based on the Word template will be desk-rejected starting from March 2026.

## Additional Formatting Notes

For both long and short papers, all figures and tables that are part of the main text must fit within these page limits. ACL currently requires all submissions to have a section titled "Limitations", which discusses the limitations of the work. It does not count towards the page limit.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fed2a2b2-c5ae-4d09-a30d-c211303b9b13",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "a29c1889-d968-457e-ab20-78223c3cd676",
  "toolUseResult": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HNgQAsp5L4sq74nSdZjpa4",
        "content": [
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authorchecklist"
          },
          {
            "title": "Paper formatting guidelines - ACLPUB",
            "url": "https://acl-org.github.io/ACLPUB/formatting.html"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "ACL Rolling Review | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/acl-rolling-review"
          },
          {
            "title": "Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/submissionform"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "Main Conference - ACL 2026",
            "url": "https://2026.aclweb.org/calls/main_conference_papers/"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          }
        ]
      },
      "Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:\n\n## Page Limits\n\nReview versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.\n\nUpon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references – so that reviewers' comments can be taken into account. Final versions of short papers may have up to five (5) pages, plus unlimited pages for acknowledgments and references.\n\n## Format Requirements\n\nThe paper follows ACL formatting. You are encouraged to use the ACL pubcheck tool to check for common problems. There is an official Overleaf template. Note that this template has a [review] setting that must be on for the submission.\n\nARR abandons the MS Word Template for conference submissions. The submissions based on the Word template will be desk-rejected starting from March 2026.\n\n## Additional Formatting Notes\n\nFor both long and short papers, all figures and tables that are part of the main text must fit within these page limits. ACL currently requires all submissions to have a section titled \"Limitations\", which discusses the limitations of the work. It does not count towards the page limit."
    ],
    "durationSeconds": 6.215238474999999
  },
  "sourceToolAssistantUUID": "fed2a2b2-c5ae-4d09-a30d-c211303b9b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T04:21:55.536Z_

<details><summary>↩ Tool result · `toolu_01M85W1nBzyiWHUVj9PkMhGu`</summary>

```text
# ACL Rolling Review (ARR) Submission Guidelines

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations section and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations section and optional ethical considerations
- Unlimited reference pages

Papers exceeding length requirements or lacking a limitations section face desk rejection.

## Formatting Requirements

Submissions must use the official ACL style template available on GitHub. All text should be "addressed exclusively to the human readers and be clearly visible to them." Papers not conforming to required styles—including page size, margins, and font size—are rejected without review.

## Anonymity Rules

Papers must exclude author names and affiliations. Authors should avoid self-references like "We previously showed..." Instead, use third-person citations: "Smith previously showed..." Supplementary materials and repository links must also be anonymized. File-sharing services tracking downloads (Dropbox, Google Drive) are prohibited.

## Appendix Guidelines

Appendices follow the double-column format (with stated exceptions) and appear after references without counting toward page limits. Reviewers are not obligated to review appendices. Critical content for assessing novelty or technical accuracy belongs in the main paper, not appendices.

## Citation Requirements

Authors must cite all relevant refereed publications. Papers appearing fewer than 3 months before submission are considered contemporaneous and don't require detailed comparisons. When preprints have been superseded by refereed versions, cite the refereed publication instead or additionally.

## Upcoming 2026 Deadlines

The document does not specify 2026 submission deadlines. It references cycles with "every two months" frequency but provides no concrete dates for the coming year.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dabbcaae-6859-43ae-b655-8066de89adf2",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "c4ba1851-6dcc-48f8-87b1-bda76c87cb01",
  "toolUseResult": {
    "bytes": 48604,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review (ARR) Submission Guidelines\n\n## Page Limits\n\n**Long Papers:**\n- Up to 8 pages of content\n- Unlimited space for limitations section and optional ethical considerations\n- Unlimited reference pages\n\n**Short Papers:**\n- Up to 4 pages of content\n- Unlimited space for limitations section and optional ethical considerations\n- Unlimited reference pages\n\nPapers exceeding length requirements or lacking a limitations section face desk rejection.\n\n## Formatting Requirements\n\nSubmissions must use the official ACL style template available on GitHub. All text should be \"addressed exclusively to the human readers and be clearly visible to them.\" Papers not conforming to required styles—including page size, margins, and font size—are rejected without review.\n\n## Anonymity Rules\n\nPapers must exclude author names and affiliations. Authors should avoid self-references like \"We previously showed...\" Instead, use third-person citations: \"Smith previously showed...\" Supplementary materials and repository links must also be anonymized. File-sharing services tracking downloads (Dropbox, Google Drive) are prohibited.\n\n## Appendix Guidelines\n\nAppendices follow the double-column format (with stated exceptions) and appear after references without counting toward page limits. Reviewers are not obligated to review appendices. Critical content for assessing novelty or technical accuracy belongs in the main paper, not appendices.\n\n## Citation Requirements\n\nAuthors must cite all relevant refereed publications. Papers appearing fewer than 3 months before submission are considered contemporaneous and don't require detailed comparisons. When preprints have been superseded by refereed versions, cite the refereed publication instead or additionally.\n\n## Upcoming 2026 Deadlines\n\nThe document does not specify 2026 submission deadlines. It references cycles with \"every two months\" frequency but provides no concrete dates for the coming year.",
    "durationMs": 10227,
    "url": "https://aclrollingreview.org/cfp"
  },
  "sourceToolAssistantUUID": "dabbcaae-6859-43ae-b655-8066de89adf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-24T04:21:58.473Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me get the EMNLP 2026 official CFP page for more details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4ba1851-6dcc-48f8-87b1-bda76c87cb01",
  "isSidechain": false,
  "requestId": "req_011CbLkhZCgUv54qKfAB7toD",
  "type": "assistant",
  "uuid": "a3b4dd2d-c7bd-4263-8b05-cbcbe5ab1b3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QG3w694PPCBa8Ec7w6nmeL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2361,
      "cache_read_input_tokens": 36858,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 36858,
          "cache_creation_input_tokens": 2361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2361
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T04:22:01.299Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Bd69fYF3ox8BwBGSizyvaK`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission requirements: page limits, formatting, anonymity rules, deadline dates, commitment deadline, topics, and any special instructions for EMNLP 2026. Include all important dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3b4dd2d-c7bd-4263-8b05-cbcbe5ab1b3a",
  "isSidechain": false,
  "requestId": "req_011CbLkhZCgUv54qKfAB7toD",
  "type": "assistant",
  "uuid": "d8c36757-9402-461f-8c78-cb9353a06025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QG3w694PPCBa8Ec7w6nmeL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2361,
      "cache_read_input_tokens": 36858,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 36858,
          "cache_creation_input_tokens": 2361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2361
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T04:22:01.306Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VsuhPpxrhdEyqJqxUpGHhj`</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8c36757-9402-461f-8c78-cb9353a06025",
  "isSidechain": false,
  "requestId": "req_011CbLkhZCgUv54qKfAB7toD",
  "type": "assistant",
  "uuid": "ec4cd4a7-1434-4f0f-b44b-f7539a15c22a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QG3w694PPCBa8Ec7w6nmeL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2361,
      "cache_read_input_tokens": 36858,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 36858,
          "cache_creation_input_tokens": 2361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2361
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T04:22:01.308Z_

<details><summary>↩ Tool result · `toolu_01VsuhPpxrhdEyqJqxUpGHhj`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec4cd4a7-1434-4f0f-b44b-f7539a15c22a",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "d32b20e7-db6f-467d-b3da-98f840230aa6",
  "toolUseResult": {
    "matches": [],
    "query": "select:read_local_file",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "ec4cd4a7-1434-4f0f-b44b-f7539a15c22a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T04:22:07.274Z_

<details><summary>↩ Tool result · `toolu_01Bd69fYF3ox8BwBGSizyvaK`</summary>

```text
# EMNLP 2026 Submission Requirements Summary

## Page Limits
- **Long Papers:** 8 pages (9 pages in camera-ready version)
- **Short Papers:** 4 pages (5 pages in camera-ready version)

## Important Dates
| Event | Date |
|-------|------|
| ARR Submission Deadline | May 25, 2026 |
| Reviewer Registration Deadline | May 27, 2026 |
| Author Response Period | July 7-13, 2026 |
| Meta Review Released | July 30, 2026 |
| EMNLP Commitment Deadline | August 2, 2026 |
| Acceptance Notification | August 20, 2026 |
| Camera-Ready Due | September 20, 2026 |
| Main Conference | October 24-29, 2026 |

*All deadlines are 11:59PM UTC-12:00*

## Anonymity & Review Process
The conference employs "double-blind" review where "reviewers will not see authors, nor will authors see reviewers." However, there is "no anonymity period requirement" following ACL policies.

## Submission Topics
Accepted areas span traditional NLP research including machine translation, dialogue systems, information extraction, language modeling, and ethics/bias. A special theme addresses "New Missions for NLP Research," emphasizing evaluation methodologies, system-level research, scientific understanding of language, data governance, and LLMs as research instruments.

## Special Requirements
- Authors must declare conference commitment at ARR submission time
- Dual submissions prohibited
- Mandatory reviewing participation expected
- Author lists cannot be modified during commitment phase
- All accepted papers require in-person or virtual conference presentation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8c36757-9402-461f-8c78-cb9353a06025",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "bba3c05b-99b0-4130-9e97-b608ca2a7dec",
  "toolUseResult": {
    "bytes": 26230,
    "code": 200,
    "codeText": "OK",
    "result": "# EMNLP 2026 Submission Requirements Summary\n\n## Page Limits\n- **Long Papers:** 8 pages (9 pages in camera-ready version)\n- **Short Papers:** 4 pages (5 pages in camera-ready version)\n\n## Important Dates\n| Event | Date |\n|-------|------|\n| ARR Submission Deadline | May 25, 2026 |\n| Reviewer Registration Deadline | May 27, 2026 |\n| Author Response Period | July 7-13, 2026 |\n| Meta Review Released | July 30, 2026 |\n| EMNLP Commitment Deadline | August 2, 2026 |\n| Acceptance Notification | August 20, 2026 |\n| Camera-Ready Due | September 20, 2026 |\n| Main Conference | October 24-29, 2026 |\n\n*All deadlines are 11:59PM UTC-12:00*\n\n## Anonymity & Review Process\nThe conference employs \"double-blind\" review where \"reviewers will not see authors, nor will authors see reviewers.\" However, there is \"no anonymity period requirement\" following ACL policies.\n\n## Submission Topics\nAccepted areas span traditional NLP research including machine translation, dialogue systems, information extraction, language modeling, and ethics/bias. A special theme addresses \"New Missions for NLP Research,\" emphasizing evaluation methodologies, system-level research, scientific understanding of language, data governance, and LLMs as research instruments.\n\n## Special Requirements\n- Authors must declare conference commitment at ARR submission time\n- Dual submissions prohibited\n- Mandatory reviewing participation expected\n- Author lists cannot be modified during commitment phase\n- All accepted papers require in-person or virtual conference presentation",
    "durationMs": 5972,
    "url": "https://2026.emnlp.org/calls/main_conference_papers/"
  },
  "sourceToolAssistantUUID": "d8c36757-9402-461f-8c78-cb9353a06025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-24T04:22:07.280Z_

```json
{
  "parentUuid": "bba3c05b-99b0-4130-9e97-b608ca2a7dec",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "62697911-8abd-4e1f-9bda-62f40e7d4532",
  "timestamp": "2026-05-24T04:22:07.280Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 38 · 2026-05-24T04:22:13.140Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of EMNLP 2026 guidelines. Let me also check if there's an existing review_issues.yaml and check the external review config. Let me now read the paper sections to understand the paper content, and check external review configuration.

Let me now:
1. Read the paper abstract and sections
2. Check for existing review_issues.yaml
3. Check external review configuration

But first, let me check the paper files. I've seen main.tex uses \input{} for sections. 

Now I'm examining the key paper sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62697911-8abd-4e1f-9bda-62f40e7d4532",
  "isSidechain": false,
  "requestId": "req_011CbLkiRNAkbCzeidzRwvxo",
  "type": "assistant",
  "uuid": "3ec90ee4-76a1-4e65-aab0-db62fa12bd58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fq7S1LZEnh1coZmmV9jPCd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 39219,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 315,
          "cache_read_input_tokens": 39219,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-24T04:22:14.966Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017JK5n6Hek5abhyGWvKTQ4A`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ec90ee4-76a1-4e65-aab0-db62fa12bd58",
  "isSidechain": false,
  "requestId": "req_011CbLkiRNAkbCzeidzRwvxo",
  "type": "assistant",
  "uuid": "7045e8ea-2e41-49cd-9143-97cd19691d2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fq7S1LZEnh1coZmmV9jPCd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 39219,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 315,
          "cache_read_input_tokens": 39219,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-24T04:22:14.985Z_

<details><summary>↩ Tool result · `toolu_017JK5n6Hek5abhyGWvKTQ4A`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7045e8ea-2e41-49cd-9143-97cd19691d2d",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "9067664b-8c87-4133-807a-4fbbc719740b",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
    ],
    "durationMs": 13,
    "numFiles": 10,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7045e8ea-2e41-49cd-9143-97cd19691d2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-24T04:22:15.239Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Liu9hZ6Lra8BwqRr6ZYTNz`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9067664b-8c87-4133-807a-4fbbc719740b",
  "isSidechain": false,
  "requestId": "req_011CbLkiRNAkbCzeidzRwvxo",
  "type": "assistant",
  "uuid": "0c921a0b-86b3-4f01-b73d-277294a28b00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fq7S1LZEnh1coZmmV9jPCd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 39219,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 315,
          "cache_read_input_tokens": 39219,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-24T04:22:15.250Z_

<details><summary>↩ Tool result · `toolu_01Liu9hZ6Lra8BwqRr6ZYTNz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c921a0b-86b3-4f01-b73d-277294a28b00",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "ad3c10a3-e2a3-4d38-902e-c20706a4e029",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "0c921a0b-86b3-4f01-b73d-277294a28b00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: distill_sparse_swiglu - 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR - 截止日期…",
  "leafUuid": "ad3c10a3-e2a3-4d38-902e-c20706a4e029",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Tool call

_source line 45 · 2026-05-24T04:22:22.474Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S3WM6TPkbrXgE2ByD1U82T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad3c10a3-e2a3-4d38-902e-c20706a4e029",
  "isSidechain": false,
  "requestId": "req_011CbLkj1eggAw8hUfJ9hBHY",
  "type": "assistant",
  "uuid": "229faa0e-3603-4cd4-a839-ba6e8ad45739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP9sqAKds59As6Sv12idsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 39983,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 39983,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-24T04:22:22.479Z_

<details><summary>↩ Tool result · `toolu_01S3WM6TPkbrXgE2ByD1U82T`</summary>

```text
1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with directional commonsense gains ($n{=}3$) but knowledge-intensive regression (8B MMLU $-$5.2pp, CIs overlap; 14B GSM8K $-$19.9pp, $n{=}3$); post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (PPL gap $\leq$0.65pp; 3-seed, 30\%).
5	Per-layer controls show the signal type gap (9.47 PPL) exceeds the coupling breadth range (2.08 PPL) at 30\%, though the decomposition is confounded by train--inference mismatch; a $K{=}4$ control suggests task-dependent coupling effects (\S\ref{sec:perlayer}).
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "229faa0e-3603-4cd4-a839-ba6e8ad45739",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "2cdb0f67-b3d4-422e-8f30-b5207480b96e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex",
      "content": "Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.\nWe train lightweight predictors ($<$1\\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.\nOn LLaMA-3.1-8B at 30\\% sparsity, the KL predictor reduces perplexity by 14.5\\% over TEAL at matched sparsity, with directional commonsense gains ($n{=}3$) but knowledge-intensive regression (8B MMLU $-$5.2pp, CIs overlap; 14B GSM8K $-$19.9pp, $n{=}3$); post-hoc compensation (+67.2M params) becomes redundant.\nOutput-distribution optimization yields masks that diverge 46--68\\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (PPL gap $\\leq$0.65pp; 3-seed, 30\\%).\nPer-layer controls show the signal type gap (9.47 PPL) exceeds the coupling breadth range (2.08 PPL) at 30\\%, though the decomposition is confounded by train--inference mismatch; a $K{=}4$ control suggests task-dependent coupling effects (\\S\\ref{sec:perlayer}).\nCross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.\nThis is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "229faa0e-3603-4cd4-a839-ba6e8ad45739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-24T04:22:22.949Z_

<details open><summary>🔧 Tool call — Read · `toolu_019rmhcvkwMaB9N8Jm7p8axT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cdb0f67-b3d4-422e-8f30-b5207480b96e",
  "isSidechain": false,
  "requestId": "req_011CbLkj1eggAw8hUfJ9hBHY",
  "type": "assistant",
  "uuid": "bee3a29c-1856-42b9-97f4-1d1a0883df3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP9sqAKds59As6Sv12idsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 39983,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 39983,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-24T04:22:22.954Z_

<details><summary>↩ Tool result · `toolu_019rmhcvkwMaB9N8Jm7p8axT`</summary>

```text
1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (mean per-layer Jaccard distance).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Per-layer controls suggest coupling effects are task-dependent, with larger impacts on commonsense than knowledge tasks (\S\ref{sec:perlayer}).
12	
13	We instantiate a lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} on LLaMA-3.1-8B~\cite{grattafiori2024llama3}.
14	At 30\% sparsity under uniform allocation, the predictor reduces TEAL's perplexity by 14.5\% at matched sparsity (8.81 vs.\ 10.30, both at 28.5\%) with downstream (MMLU 40.7$\pm$1.3\% vs.\ 65.3\% dense, 3-seed); global top-$k$ amplifies cross-seed variance ($7.3\times$).
15	At 50\%, the perplexity advantage widens (50\% over TEAL), but downstream reasoning collapses regardless of method.
16	
17	Cross-architecture evaluation on Mistral-7B-v0.3~\cite{jiang2023mistral} (3-seed) confirms the PPL advantage ($-$17.3\%) with directional commonsense gains but tied MMLU; preliminary evaluation on Qwen-2.5-14B~\cite{qwen2024qwen25} shows consistent PPL improvement but reasoning decline (GSM8K $-$19.9pp, $\sigma$=5.3pp; MMLU $-$2.8pp).
18	This paper is primarily an empirical study characterizing how the training objective shapes sparsity prediction quality across allocation strategies, sparsity levels, and model scales. The central finding---that output-distribution alignment consistently and substantially outperforms per-neuron classification for learned sparsity---is the paper's contribution. Without sparse kernel support, the predictor adds 6.4\% latency overhead; wall-clock speedup is not addressed (Appendix~\ref{app:latency}).
19	While individual components (KL divergence, Gumbel-Sigmoid relaxation) are established techniques, their application to contextual activation sparsity prediction has not been explored, and the resulting empirical behaviors are non-obvious.
20	
21	Our contributions are:
22	\begin{itemize}[nosep,leftmargin=*]
23	\item \emph{Empirical:} Output-distribution alignment ranking across five losses, with per-layer decomposition showing the signal type gap (9.47 PPL) exceeds the coupling breadth range (2.08 PPL), though confounded by train--inference mismatch (\S\ref{sec:perlayer});
24	\item \emph{Empirical:} Cross-scale evidence (7--14B) with task-type split: KL outperforms on PPL and commonsense but shows systematic knowledge regression, structural to output-distribution optimization (C4 control; \S\ref{sec:experiments});
25	\item \emph{Analytical:} Target-swap ablation suggests KL-discovered mask targets transfer to BCE; per-layer controls suggest task-dependent coupling effects (\S\ref{sec:perlayer});
26	\item \emph{Analytical:} KL-derived masks render post-hoc compensation (+67.2M params) redundant at both tested sparsity levels (\S\ref{sec:compensation}).
27	\end{itemize}
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\columnwidth]{fig1_overview.pdf}
32	\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}
33	\label{fig:overview}
34	\end{figure}
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bee3a29c-1856-42b9-97f4-1d1a0883df3a",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "5c2b263c-926d-49fd-a0d2-63c05a22c65f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nHow the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.\nLearned sparsity predictors~\\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.\nYet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.\nThis mismatch between per-neuron training and global inference allocation has not been formally analyzed.\nUnlike MaskLLM~\\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.\n\nGradient analysis reveals a structural asymmetry: BCE's gradient $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j = \\sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\\S\\ref{sec:method:gradient}).\nKL's coupled gradients discover neuron importance patterns that diverge 68\\% from magnitude-based masks (mean per-layer Jaccard distance).\nA target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\\pm$0.20. Per-layer controls suggest coupling effects are task-dependent, with larger impacts on commonsense than knowledge tasks (\\S\\ref{sec:perlayer}).\n\nWe instantiate a lightweight predictor (75.9M params, $<$1\\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}.\nAt 30\\% sparsity under uniform allocation, the predictor reduces TEAL's perplexity by 14.5\\% at matched sparsity (8.81 vs.\\ 10.30, both at 28.5\\%) with downstream (MMLU 40.7$\\pm$1.3\\% vs.\\ 65.3\\% dense, 3-seed); global top-$k$ amplifies cross-seed variance ($7.3\\times$).\nAt 50\\%, the perplexity advantage widens (50\\% over TEAL), but downstream reasoning collapses regardless of method.\n\nCross-architecture evaluation on Mistral-7B-v0.3~\\cite{jiang2023mistral} (3-seed) confirms the PPL advantage ($-$17.3\\%) with directional commonsense gains but tied MMLU; preliminary evaluation on Qwen-2.5-14B~\\cite{qwen2024qwen25} shows consistent PPL improvement but reasoning decline (GSM8K $-$19.9pp, $\\sigma$=5.3pp; MMLU $-$2.8pp).\nThis paper is primarily an empirical study characterizing how the training objective shapes sparsity prediction quality across allocation strategies, sparsity levels, and model scales. The central finding---that output-distribution alignment consistently and substantially outperforms per-neuron classification for learned sparsity---is the paper's contribution. Without sparse kernel support, the predictor adds 6.4\\% latency overhead; wall-clock speedup is not addressed (Appendix~\\ref{app:latency}).\nWhile individual components (KL divergence, Gumbel-Sigmoid relaxation) are established techniques, their application to contextual activation sparsity prediction has not been explored, and the resulting empirical behaviors are non-obvious.\n\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\emph{Empirical:} Output-distribution alignment ranking across five losses, with per-layer decomposition showing the signal type gap (9.47 PPL) exceeds the coupling breadth range (2.08 PPL), though confounded by train--inference mismatch (\\S\\ref{sec:perlayer});\n\\item \\emph{Empirical:} Cross-scale evidence (7--14B) with task-type split: KL outperforms on PPL and commonsense but shows systematic knowledge regression, structural to output-distribution optimization (C4 control; \\S\\ref{sec:experiments});\n\\item \\emph{Analytical:} Target-swap ablation suggests KL-discovered mask targets transfer to BCE; per-layer controls suggest task-dependent coupling effects (\\S\\ref{sec:perlayer});\n\\item \\emph{Analytical:} KL-derived masks render post-hoc compensation (+67.2M params) redundant at both tested sparsity levels (\\S\\ref{sec:compensation}).\n\\end{itemize}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_overview.pdf}\n\\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}\n\\label{fig:overview}\n\\end{figure}\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  },
  "sourceToolAssistantUUID": "bee3a29c-1856-42b9-97f4-1d1a0883df3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-24T04:22:23.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DZmncekb7YMe9nodk3P6iD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c2b263c-926d-49fd-a0d2-63c05a22c65f",
  "isSidechain": false,
  "requestId": "req_011CbLkj1eggAw8hUfJ9hBHY",
  "type": "assistant",
  "uuid": "3df293e1-9725-4771-8d26-b261009ab9f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP9sqAKds59As6Sv12idsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 39983,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 39983,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-24T04:22:23.889Z_

<details><summary>↩ Tool result · `toolu_01DZmncekb7YMe9nodk3P6iD`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We present an output-distribution KL framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from $\mathbf{x}^{(\ell)}$.
26	At inference, the scores are fed to a global top-$k$ allocation mechanism~\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\rho) \times L \times d_{\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\rho$.
27	
28	
29	\subsection{Predictor Architecture}
30	\label{sec:method:predictor}
31	
32	Each layer $\ell$ has an independent two-layer MLP predictor:
33	\begin{align}
34	f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) = \text{GELU}(\mathbf{x}^{(\ell)} \mathbf{W}_1^{(\ell)}) \, \mathbf{W}_2^{(\ell)},
35	\label{eq:predictor}
36	\end{align}
37	where $\mathbf{W}_1^{(\ell)} \in \mathbb{R}^{d \times d_b}$ and $\mathbf{W}_2^{(\ell)} \in \mathbb{R}^{d_b \times d_{\text{ff}}}$ with bottleneck dimension $d_b{=}128$.
38	The predictor takes $\mathbf{x}^{(\ell)}$ (the hidden state after attention, before the FFN) and outputs $d_{\text{ff}}$-dimensional logits $\mathbf{s}^{(\ell)}$, from which the mask is derived.
39	
40	Each predictor has $(4096 \times 128) + (128 \times 14336) = 2.37\text{M}$ parameters.
41	With 32 independent predictors (one per layer), the total overhead is 75.9M parameters, less than 1\% of the 8B base model.
42	The predictors operate independently across layers, requiring no cross-layer communication at inference.
43	
44	
45	\subsection{Gumbel-Sigmoid Relaxation}
46	\label{sec:method:gumbel}
47	
48	The hard mask $m_j = \mathbf{1}[s_j > \text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.
49	We apply Gumbel-Sigmoid relaxation~\cite{maddison2017concrete,louizos2018l0,jang2017gumbel} to produce differentiable soft masks:
50	\begin{align}
51	\tilde{m}_j^{(\ell)} = \sigma_\tau\!\left(\log \frac{s_j^{(\ell)}}{1 - s_j^{(\ell)}} + \varepsilon_1 - \varepsilon_2\right), \quad \varepsilon_1, \varepsilon_2 \sim \text{Gumbel}(0,1),
52	\label{eq:gumbel}
53	\end{align}
54	where $\sigma_\tau(x) = \text{sigmoid}(x / \tau)$ and $\tau$ is a temperature parameter.
55	The Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\tau \to 0$, $\tilde{m}_j$ approaches a binary decision.
56	
57	We anneal $\tau$ linearly from 1.0 to 0.1 over training.
58	At high temperature, the soft mask permits gradient flow through all neurons for broad exploration.
59	As temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.
60	
61	\paragraph{Comparison with Straight-Through Estimation.}
62	The straight-through estimator (STE)~\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\partial m / \partial s = 1$).
63	In our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously. The resulting oscillations in the penalty weight prevent convergence to the target sparsity.
64	Gumbel relaxation eliminates this pathology and contributes a 33.8\% improvement (PPL 15.77 $\to$ 11.79 at 50\% sparsity), as we verify empirically in \S\ref{sec:experiments}.
65	
66	
67	\subsection{KL Divergence Training Objective}
68	\label{sec:method:kl}
69	
70	Let $\mathbf{z}_{\text{dense}}$ denote the output logits from a full dense forward pass, and $\mathbf{z}_{\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\{\tilde{\mathbf{m}}^{(\ell)}\}_\ell$ applied at every layer.
71	We minimize the forward KL divergence between the dense and sparse output distributions:
72	\begin{align}
73	\mathcal{L}_{\text{KL}} = D_{\text{KL}}(p_{\text{dense}} \,\|\, p_{\text{sparse}}) = \sum_{v} p_{\text{dense}}^{(v)} \log \frac{p_{\text{dense}}^{(v)}}{p_{\text{sparse}}^{(v)}},
74	\label{eq:kl_loss}
75	\end{align}
76	where $p_{\text{dense}} = \text{softmax}(\mathbf{z}_{\text{dense}})$ and $p_{\text{sparse}} = \text{softmax}(\mathbf{z}_{\text{sparse}})$, summed over the vocabulary $v$ and averaged over all token positions in the sequence.
77	The base model is frozen; only the predictor parameters receive gradients.
78	
79	We use forward KL (mass-covering) rather than reverse KL, as the goal is to preserve the dense model's primary predictions rather than explore alternative modes.
80	In sparsity prediction, mode-covering is critical: false negatives (omitting a rarely but critically active neuron) cascade through downstream layers under global allocation, whereas false positives merely waste capacity; reverse KL's mode-seeking concentrates on high-probability neurons and risks missing compositionally important activations~\cite{wu2025rethinking}.
81	\S\ref{sec:experiments} validates this choice empirically: forward KL outperforms reverse KL by 8.6\% and JSD by 6.4\% (at 50\% sparsity; the gap narrows at 30\%; Table~\ref{tab:ablation}).
82	No temperature scaling ($T{=}1$) is applied~\cite{hinton2015distilling}; we distinguish $T$ from the Gumbel temperature $\tau$ (\S\ref{sec:method:gumbel}), which controls mask sharpness rather than logit scaling.
83	
84	
85	\subsection{Geometric Penalty Schedule}
86	\label{sec:method:lagrangian}
87	
88	We enforce a model-level sparsity target $\rho$ via constrained optimization with $\bar{s} = \frac{1}{L} \sum_\ell \frac{1}{d_{\text{ff}}} \sum_j \tilde{m}_j^{(\ell)}$ denoting the average retained fraction:
89	\begin{align}
90	\min_\theta \; \mathcal{L}_{\text{KL}} \quad \text{s.t.} \quad \bar{s} = 1 - \rho.
91	\label{eq:constrained}
92	\end{align}
93	We relax this via a geometric penalty schedule:
94	\begin{align}
95	\mathcal{L} = \mathcal{L}_{\text{KL}} + \lambda \cdot \text{clamp}(|\bar{s} - (1 - \rho)| - \epsilon, \min{=}0)^2,
96	\label{eq:lagrangian}
97	\end{align}
98	where $\epsilon = 0.02$ is a deadzone margin that suppresses oscillation near the target (sensitivity in Appendix~\ref{app:lagrangian}). The penalty weight $\lambda$ is updated via geometric doubling (doubled when sparsity exceeds target, halved otherwise), clamped to $[\lambda_{\text{floor}}, \lambda_{\max}]$, reaching target sparsity within 40--110 steps across all tested regimes (Appendix~\ref{app:lagrangian}).
99	
100	
101	\subsection{Gradient Analysis: BCE vs.\ KL}
102	\label{sec:method:gradient}
103	
104	We contrast the gradient structure of BCE and KL to build intuition for how KL discovers divergent mask patterns (\S\ref{sec:mask_analysis}). This analysis is suggestive; empirical evidence in \S\ref{sec:mask_analysis} shows KL-discovered mask targets drive inference quality.
105	
106	Under BCE, the predictor trains against oracle masks $m_j^* = \mathbf{1}[|g_j| \geq \text{top-}k\text{ threshold}]$ derived from activation magnitudes.
107	The gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$; each neuron is trained independently with no inter-neuron coupling.
108	Under output-distribution KL, the chain rule introduces a downstream Jacobian $\partial \mathbf{z}_{\text{sparse}} / \partial \tilde{m}_j^{(\ell)}$ that couples neuron $j$'s gradient to all other retained neurons in layers $\ell$ through $L$, because the sparse hidden state propagates through subsequent attention and FFN operations.
109	This coupling allows KL to evaluate each neuron's importance in the context of the full sparse computation, rather than against a fixed magnitude target.
110	
111	Gradient SNR measurements\footnote{$\text{SNR}_\ell = \|\mathbb{E}[\nabla_{\theta_\ell} \mathcal{L}]\|_2^2 / \text{Var}[\nabla_{\theta_\ell} \mathcal{L}]$, expectation over mini-batches.} reveal that BCE maintains consistently higher SNR than KL throughout training ($2.3\times$ at convergence; Figure~\ref{fig:snr_trajectory}), indicating that KL's quality advantage does not arise from cleaner gradient signals.
112	Rather, KL's end-to-end coupled gradient serves as a \emph{search mechanism} that discovers compositionally superior mask patterns, even when the per-step signal is noisier than BCE's decomposed updates.
113	The target-swap ablation in \S\ref{sec:mask_analysis} suggests that the discovered mask targets, not the coupling mechanism itself, drive inference-stage quality.
114	
115	\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}
116	\label{sec:method:taxonomy}
117	
118	We organize prior work along two axes: \emph{correction granularity} (how the mask adapts to input) and \emph{training signal coupling} (whether the objective captures inter-neuron dependencies).
119	
120	\begin{table}[t]
121	\centering
122	\caption{Taxonomy of learned sparsity prediction methods along correction granularity (rows) and training signal coupling (columns). Our method occupies the Per-token $\times$ Coupled cell (organizational framework). Empty cells represent unexplored combinations; their relative merit is an open question.}
123	\label{tab:taxonomy}
124	\resizebox{\columnwidth}{!}{
125	\begin{tabular}{lccc}
126	\toprule
127	 & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\
128	\midrule
129	Static & --- & --- & SPON, MaskLLM \\
130	Per-token & DejaVu, FastForward & ShadowLLM, D2DMoE & \textbf{Ours} \\
131	\bottomrule
132	\end{tabular}}
133	\end{table}
134	
135	Our method combines per-token prediction with coupled KL training (Table~\ref{tab:taxonomy}).
136	KL on output logits directly optimizes next-token prediction loss, which composes across layers; per-layer MSE does not---a mask minimizing FFN output error at layer $\ell$ may amplify errors in layers $\ell{+}1 \ldots L$, explaining its $1.7\times$/$9.6\times$ worse PPL than TEAL at 30\%/50\% (50\%: s42 only; \S\ref{sec:experiments}). % exp_id: mse30_uniform_s42, mse50_uniform_s42
137	Full taxonomy discussion in Appendix~\ref{app:taxonomy}.
138	
139	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3df293e1-9725-4771-8d26-b261009ab9f9",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "b1486914-dd5b-4c24-8a88-a4520d4f1823",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe present an output-distribution KL framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\\ref{fig:overview}).\nThe method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.\n\n\\subsection{Problem Formulation}\n\\label{sec:method:formulation}\n\nConsider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\\cite{shazeer2020glu}.\nFor layer $\\ell$, the FFN computes:\n\\begin{align}\n\\mathbf{y}^{(\\ell)} = \\bigl(\\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)},\n\\label{eq:swiglu}\n\\end{align}\nwhere $\\mathbf{x}^{(\\ell)} \\in \\mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\\sigma$ denotes SiLU, $\\mathbf{W}_g^{(\\ell)}, \\mathbf{W}_u^{(\\ell)} \\in \\mathbb{R}^{d \\times d_{\\text{ff}}}$ and $\\mathbf{W}_d^{(\\ell)} \\in \\mathbb{R}^{d_{\\text{ff}} \\times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\\text{ff}}{=}14{,}336$.\n\nDefine the gate activation $\\mathbf{g}^{(\\ell)} = \\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\in \\mathbb{R}^{d_{\\text{ff}}}$.\nEach element $g_j^{(\\ell)}$ determines the contribution of neuron $j$ to the output.\nWe introduce a binary mask $\\mathbf{m}^{(\\ell)} \\in \\{0,1\\}^{d_{\\text{ff}}}$ that zeros out pruned neurons:\n\\begin{align}\n\\mathbf{y}_{\\text{sparse}}^{(\\ell)} = \\bigl(\\mathbf{m}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)}.\n\\label{eq:sparse_ffn}\n\\end{align}\nOur goal is to learn a mask predictor $f_\\theta^{(\\ell)}(\\mathbf{x}^{(\\ell)}) \\to \\mathbf{s}^{(\\ell)} \\in (0,1)^{d_{\\text{ff}}}$ that produces per-neuron importance scores from $\\mathbf{x}^{(\\ell)}$.\nAt inference, the scores are fed to a global top-$k$ allocation mechanism~\\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\\rho) \\times L \\times d_{\\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\\rho$.\n\n\n\\subsection{Predictor Architecture}\n\\label{sec:method:predictor}\n\nEach layer $\\ell$ has an independent two-layer MLP predictor:\n\\begin{align}\nf_\\theta^{(\\ell)}(\\mathbf{x}^{(\\ell)}) = \\text{GELU}(\\mathbf{x}^{(\\ell)} \\mathbf{W}_1^{(\\ell)}) \\, \\mathbf{W}_2^{(\\ell)},\n\\label{eq:predictor}\n\\end{align}\nwhere $\\mathbf{W}_1^{(\\ell)} \\in \\mathbb{R}^{d \\times d_b}$ and $\\mathbf{W}_2^{(\\ell)} \\in \\mathbb{R}^{d_b \\times d_{\\text{ff}}}$ with bottleneck dimension $d_b{=}128$.\nThe predictor takes $\\mathbf{x}^{(\\ell)}$ (the hidden state after attention, before the FFN) and outputs $d_{\\text{ff}}$-dimensional logits $\\mathbf{s}^{(\\ell)}$, from which the mask is derived.\n\nEach predictor has $(4096 \\times 128) + (128 \\times 14336) = 2.37\\text{M}$ parameters.\nWith 32 independent predictors (one per layer), the total overhead is 75.9M parameters, less than 1\\% of the 8B base model.\nThe predictors operate independently across layers, requiring no cross-layer communication at inference.\n\n\n\\subsection{Gumbel-Sigmoid Relaxation}\n\\label{sec:method:gumbel}\n\nThe hard mask $m_j = \\mathbf{1}[s_j > \\text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.\nWe apply Gumbel-Sigmoid relaxation~\\cite{maddison2017concrete,louizos2018l0,jang2017gumbel} to produce differentiable soft masks:\n\\begin{align}\n\\tilde{m}_j^{(\\ell)} = \\sigma_\\tau\\!\\left(\\log \\frac{s_j^{(\\ell)}}{1 - s_j^{(\\ell)}} + \\varepsilon_1 - \\varepsilon_2\\right), \\quad \\varepsilon_1, \\varepsilon_2 \\sim \\text{Gumbel}(0,1),\n\\label{eq:gumbel}\n\\end{align}\nwhere $\\sigma_\\tau(x) = \\text{sigmoid}(x / \\tau)$ and $\\tau$ is a temperature parameter.\nThe Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\\tau \\to 0$, $\\tilde{m}_j$ approaches a binary decision.\n\nWe anneal $\\tau$ linearly from 1.0 to 0.1 over training.\nAt high temperature, the soft mask permits gradient flow through all neurons for broad exploration.\nAs temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.\n\n\\paragraph{Comparison with Straight-Through Estimation.}\nThe straight-through estimator (STE)~\\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\\partial m / \\partial s = 1$).\nIn our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously. The resulting oscillations in the penalty weight prevent convergence to the target sparsity.\nGumbel relaxation eliminates this pathology and contributes a 33.8\\% improvement (PPL 15.77 $\\to$ 11.79 at 50\\% sparsity), as we verify empirically in \\S\\ref{sec:experiments}.\n\n\n\\subsection{KL Divergence Training Objective}\n\\label{sec:method:kl}\n\nLet $\\mathbf{z}_{\\text{dense}}$ denote the output logits from a full dense forward pass, and $\\mathbf{z}_{\\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\\{\\tilde{\\mathbf{m}}^{(\\ell)}\\}_\\ell$ applied at every layer.\nWe minimize the forward KL divergence between the dense and sparse output distributions:\n\\begin{align}\n\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(p_{\\text{dense}} \\,\\|\\, p_{\\text{sparse}}) = \\sum_{v} p_{\\text{dense}}^{(v)} \\log \\frac{p_{\\text{dense}}^{(v)}}{p_{\\text{sparse}}^{(v)}},\n\\label{eq:kl_loss}\n\\end{align}\nwhere $p_{\\text{dense}} = \\text{softmax}(\\mathbf{z}_{\\text{dense}})$ and $p_{\\text{sparse}} = \\text{softmax}(\\mathbf{z}_{\\text{sparse}})$, summed over the vocabulary $v$ and averaged over all token positions in the sequence.\nThe base model is frozen; only the predictor parameters receive gradients.\n\nWe use forward KL (mass-covering) rather than reverse KL, as the goal is to preserve the dense model's primary predictions rather than explore alternative modes.\nIn sparsity prediction, mode-covering is critical: false negatives (omitting a rarely but critically active neuron) cascade through downstream layers under global allocation, whereas false positives merely waste capacity; reverse KL's mode-seeking concentrates on high-probability neurons and risks missing compositionally important activations~\\cite{wu2025rethinking}.\n\\S\\ref{sec:experiments} validates this choice empirically: forward KL outperforms reverse KL by 8.6\\% and JSD by 6.4\\% (at 50\\% sparsity; the gap narrows at 30\\%; Table~\\ref{tab:ablation}).\nNo temperature scaling ($T{=}1$) is applied~\\cite{hinton2015distilling}; we distinguish $T$ from the Gumbel temperature $\\tau$ (\\S\\ref{sec:method:gumbel}), which controls mask sharpness rather than logit scaling.\n\n\n\\subsection{Geometric Penalty Schedule}\n\\label{sec:method:lagrangian}\n\nWe enforce a model-level sparsity target $\\rho$ via constrained optimization with $\\bar{s} = \\frac{1}{L} \\sum_\\ell \\frac{1}{d_{\\text{ff}}} \\sum_j \\tilde{m}_j^{(\\ell)}$ denoting the average retained fraction:\n\\begin{align}\n\\min_\\theta \\; \\mathcal{L}_{\\text{KL}} \\quad \\text{s.t.} \\quad \\bar{s} = 1 - \\rho.\n\\label{eq:constrained}\n\\end{align}\nWe relax this via a geometric penalty schedule:\n\\begin{align}\n\\mathcal{L} = \\mathcal{L}_{\\text{KL}} + \\lambda \\cdot \\text{clamp}(|\\bar{s} - (1 - \\rho)| - \\epsilon, \\min{=}0)^2,\n\\label{eq:lagrangian}\n\\end{align}\nwhere $\\epsilon = 0.02$ is a deadzone margin that suppresses oscillation near the target (sensitivity in Appendix~\\ref{app:lagrangian}). The penalty weight $\\lambda$ is updated via geometric doubling (doubled when sparsity exceeds target, halved otherwise), clamped to $[\\lambda_{\\text{floor}}, \\lambda_{\\max}]$, reaching target sparsity within 40--110 steps across all tested regimes (Appendix~\\ref{app:lagrangian}).\n\n\n\\subsection{Gradient Analysis: BCE vs.\\ KL}\n\\label{sec:method:gradient}\n\nWe contrast the gradient structure of BCE and KL to build intuition for how KL discovers divergent mask patterns (\\S\\ref{sec:mask_analysis}). This analysis is suggestive; empirical evidence in \\S\\ref{sec:mask_analysis} shows KL-discovered mask targets drive inference quality.\n\nUnder BCE, the predictor trains against oracle masks $m_j^* = \\mathbf{1}[|g_j| \\geq \\text{top-}k\\text{ threshold}]$ derived from activation magnitudes.\nThe gradient $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j = \\sigma(s_j) - m_j^*$ depends only on neuron $j$; each neuron is trained independently with no inter-neuron coupling.\nUnder output-distribution KL, the chain rule introduces a downstream Jacobian $\\partial \\mathbf{z}_{\\text{sparse}} / \\partial \\tilde{m}_j^{(\\ell)}$ that couples neuron $j$'s gradient to all other retained neurons in layers $\\ell$ through $L$, because the sparse hidden state propagates through subsequent attention and FFN operations.\nThis coupling allows KL to evaluate each neuron's importance in the context of the full sparse computation, rather than against a fixed magnitude target.\n\nGradient SNR measurements\\footnote{$\\text{SNR}_\\ell = \\|\\mathbb{E}[\\nabla_{\\theta_\\ell} \\mathcal{L}]\\|_2^2 / \\text{Var}[\\nabla_{\\theta_\\ell} \\mathcal{L}]$, expectation over mini-batches.} reveal that BCE maintains consistently higher SNR than KL throughout training ($2.3\\times$ at convergence; Figure~\\ref{fig:snr_trajectory}), indicating that KL's quality advantage does not arise from cleaner gradient signals.\nRather, KL's end-to-end coupled gradient serves as a \\emph{search mechanism} that discovers compositionally superior mask patterns, even when the per-step signal is noisier than BCE's decomposed updates.\nThe target-swap ablation in \\S\\ref{sec:mask_analysis} suggests that the discovered mask targets, not the coupling mechanism itself, drive inference-stage quality.\n\n\\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}\n\\label{sec:method:taxonomy}\n\nWe organize prior work along two axes: \\emph{correction granularity} (how the mask adapts to input) and \\emph{training signal coupling} (whether the objective captures inter-neuron dependencies).\n\n\\begin{table}[t]\n\\centering\n\\caption{Taxonomy of learned sparsity prediction methods along correction granularity (rows) and training signal coupling (columns). Our method occupies the Per-token $\\times$ Coupled cell (organizational framework). Empty cells represent unexplored combinations; their relative merit is an open question.}\n\\label{tab:taxonomy}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\n & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON, MaskLLM \\\\\nPer-token & DejaVu, FastForward & ShadowLLM, D2DMoE & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nOur method combines per-token prediction with coupled KL training (Table~\\ref{tab:taxonomy}).\nKL on output logits directly optimizes next-token prediction loss, which composes across layers; per-layer MSE does not---a mask minimizing FFN output error at layer $\\ell$ may amplify errors in layers $\\ell{+}1 \\ldots L$, explaining its $1.7\\times$/$9.6\\times$ worse PPL than TEAL at 30\\%/50\\% (50\\%: s42 only; \\S\\ref{sec:experiments}). % exp_id: mse30_uniform_s42, mse50_uniform_s42\nFull taxonomy discussion in Appendix~\\ref{app:taxonomy}.\n\n",
      "numLines": 139,
      "startLine": 1,
      "totalLines": 139
    }
  },
  "sourceToolAssistantUUID": "3df293e1-9725-4771-8d26-b261009ab9f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-24T04:22:24.366Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VuU4mN68mjvBLD2RVq2bd5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1486914-dd5b-4c24-8a88-a4520d4f1823",
  "isSidechain": false,
  "requestId": "req_011CbLkj1eggAw8hUfJ9hBHY",
  "type": "assistant",
  "uuid": "ea327eb2-b676-4ec1-afc7-68333c05e066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP9sqAKds59As6Sv12idsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 39983,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 39983,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-24T04:22:24.371Z_

<details><summary>↩ Tool result · `toolu_01VuU4mN68mjvBLD2RVq2bd5`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; and (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presents the primary comparison. Uniform allocation preserves downstream performance best; global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
28	At 30\% sparsity, output-distribution KL under uniform allocation achieves PPL 8.81$\pm$0.02 (3-seed), a 14.5\% reduction over TEAL at matched actual sparsity (8.81 vs.\ 10.30, both at 28.5\%; Appendix~\ref{app:ood}).
29	Uniform allocation yields stable downstream (MMLU 40.7$\pm$1.3\%, 3-seed; Appendix~\ref{app:stability}), while global top-$k$ exhibits high seed variance (35.7$\pm$9.5\%) from late-layer starvation (L31 retention 28.4\%; \S\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform, kl30_3seed
30	
31	\paragraph{Task-Type Split.}
32	KL shows directional improvements over TEAL on commonsense reasoning (ARC-c, WG, HellaSwag, PIQA: 4/4 wins at 30\% uniform) but underperforms on knowledge-intensive tasks (MMLU, GSM8K: 0/2).
33	With only three seeds, 95\% confidence intervals for individual downstream tasks overlap; we therefore treat PPL ($\sigma{=}0.02$, non-overlapping) as the primary metric and downstream differences as directional evidence.
34	The KL predictor protects L14--L18 (14--18\% sparsity vs.\ 32\% global mean) while aggressively pruning L22--L28 (48--57\%). Constraint interventions (Appendix~\ref{app:constraint}) confirm a task-dependent trade-off: removing the valley improves MMLU +3.4pp but reduces ARC-c by 1.5pp, consistent with localized factual associations~\cite{geva2023dissecting}; task-aware allocation may resolve this. % exp_id: bench_kl30_uniform, teal30_uniform, hellaswag_piqa_kl30_uniform, perlayer_sparsity_analysis, constraint_protect_late, constraint_remove_valley
35	
36	\paragraph{Knowledge-Task Regression: Hypothesis.}
37	Constraint experiments (Appendix~\ref{app:constraint}) confirm allocation contributes: removing the learned valley improves MMLU +3.4pp and GSM8K +1.6pp. A C4-trained control (Appendix~\ref{app:c4_control}) does not alleviate the regression (MMLU 40.0\%, GSM8K 4.1\% vs.\ 40.7\%, 7.5\%), confirming the deficit is structural to forward KL's mode-covering property~\cite{meng2022locating} rather than training data composition. % exp_id: constraint_remove_valley, c4_control_eval
38	
39	At 50\%, the PPL advantage widens (11.92 vs.\ 23.90, 50\% reduction) and generalizes to C4 (Appendix~\ref{app:ood}), but all methods collapse to near-random on MMLU and GSM8K ($\leq$2.7\%); no allocation strategy recovers at this capacity limit. % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval, d030_kl50_uniform, multi_seed_kl50_global
40	
41	\begin{table}[t]
42	\centering
43	\caption{Main results on LLaMA-3.1-8B. $^\ast$$2.71\times$ KL compute (\S\ref{sec:isocompute}). $\pm$: 3-seed; unmarked: s42. $^\ddagger$Actual sparsity: KL 28.5\% vs.\ TEAL 29.3\% at 30\% (Appendix~\ref{app:ood}).}
44	\label{tab:main}
45	\resizebox{\columnwidth}{!}{
46	\begin{tabular}{llccccc}
47	\toprule
48	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
49	\midrule
50	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
51	\midrule
52	\multirow{6}{*}{30\%}
53	& TEAL uniform & 10.82 & 39.33 & 65.04 & \textbf{45.86} & \textbf{8.79} \\ % exp_id: teal30_uniform
54	& BCE global & 11.25 & 41.2 & 66.0 & 36.3 & 6.0 \\ % exp_id: bce30_teal_global
55	& BCE uniform & 15.09$\pm$0.13 & 33.45 & 61.09 & 43.05 & 3.97 \\ % exp_id: bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456
56	& MSE uniform & 18.52$\pm$1.68 & 35.8$\pm$4.1 & 59.8$\pm$2.6 & 30.7$\pm$2.6 & 2.3$\pm$0.7 \\ % exp_id: mse30_3seed
57	& KL global (Ours)$^\ddagger$ & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5 & 8.0$\pm$0.7 \\ % exp_id: kl30_3seed_global
58	& KL uniform$^\ddagger$ & \textbf{8.81$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & 40.7$\pm$1.3 & 7.5$\pm$0.1 \\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform
59	\midrule
60	\multirow{5}{*}{50\%}
61	& TEAL uniform & 23.90 & 27.47 & 54.38 & \textbf{29.26} & 1.74 \\ % exp_id: teal50_uniform
62	& BCE (2700 steps)$^\ast$ & 28.13$\pm$0.20 & 27.6$\pm$0.6 & 51.8$\pm$0.6 & 26.1$\pm$0.5 & 2.1$\pm$0.2 \\ % exp_id: bce50_3seed
63	& MSE uniform & 229.26 & 25.00 & 50.59 & 23.79 & 1.59 \\ % exp_id: mse50_uniform_s42
64	& KL global (Ours) & \textbf{11.84$\pm$0.15} & \textbf{36.3$\pm$3.2} & \textbf{63.8$\pm$0.3} & 28.3$\pm$0.7 & \textbf{2.7$\pm$1.3} \\ % exp_id: bench_kl50_global (s42), kl50_global_s123_reeval (s123 PPL), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456)
65	& KL uniform & 11.92$\pm$0.07 & 33.8$\pm$1.2 & 62.9$\pm$0.1 & 28.0$\pm$0.6 & 2.2$\pm$0.1 \\ % exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456
66	\bottomrule
67	\end{tabular}}
68	\end{table}
69	
70	
71	\subsection{Extended Training Analysis}
72	\label{sec:isocompute}
73	
74	At $2.71\times$ KL compute budget (2700 steps, matched wall-clock), BCE achieves PPL 28.13$\pm$0.20 (3-seed), still $2.39\times$ worse than KL (11.79). % exp_id: bce50_3seed
75	The gap is systematic: BCE reaches higher oracle F1 (0.613 vs.\ 0.540) with 139\% worse PPL, confirming KL optimizes for distributional fidelity rather than magnitude agreement. % exp_id: f1_oracle_analysis, bce_isocompute_s42
76	
77	
78	\subsection{Mask Pattern Analysis}
79	\label{sec:mask_analysis}
80	
81	KL-derived masks diverge from magnitude oracles: per-layer Jaccard distance averages 68\% at 50\% (64 samples, 131K tokens; Figure~\ref{fig:mask_heatmap}), with cross-seed variation (36.3\%) confirming systematic divergence (Appendices~\ref{app:cross_seed_jaccard},~\ref{app:mask_viz}).
82	Despite this, KL achieves PPL 11.79 vs.\ BCE's 28.13$\pm$0.20, confirming that distributional fidelity, not magnitude agreement, produces better masks. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap
83	Divergence follows a U-shaped per-layer pattern, peaking in late layers (0.70--0.75 at 50\%). % exp_id: c1_mask_overlap
84	
85	\paragraph{Target-Swap Ablation: Target Quality vs.\ Gradient Coupling.}
86	To disentangle whether KL's advantage stems from its coupled gradient pathway or from the mask patterns it discovers, we train a standard BCE predictor on KL-derived oracle masks instead of magnitude-based masks (C1 target-swap ablation).
87	Table~\ref{tab:c1} reports results under TEAL uniform allocation at matched sparsity.
88	
89	\begin{table}[t]
90	\centering
91	\caption{Target-swap ablation (C1): BCE on KL-derived masks vs.\ KL predictor (same seed), TEAL uniform. All seeds show max $\Delta$$\leq$1.70pp at 30\%; max $\Delta$$\leq$0.79pp at 50\% (s42). $^\dagger$\textbf{Provenance:} s42 oracle extracted from an earlier training run (not seed-matched); s123/s456 use seed-matched retrained oracles (Appendix~\ref{app:oracle_provenance}).}
92	\label{tab:c1}
93	\resizebox{\columnwidth}{!}{
94	\begin{tabular}{lllccccc}
95	\toprule
96	Sparsity & Seed & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
97	\midrule
98	\multirow{6}{*}{30\%}
99	& s42$^\dagger$ & C1 & 9.45 & 40.27 & 67.40 & \textbf{42.30} & \textbf{7.58} \\ % exp_id: c1_ablation_30pct_s42_eval_v2
100	& & KL & \textbf{8.82} & \textbf{40.78} & \textbf{68.59} & 40.6 & 7.35 \\ % exp_id: bench_kl30_uniform
101	& s123 & C1 & 8.84 & 44.71 & \textbf{69.77} & \textbf{39.92} & 6.82 \\ % exp_id: eval_c1_retrain_30pct_s123
102	& & KL & \textbf{8.83} & \textbf{45.31} & 69.38 & 39.4 & \textbf{7.51} \\ % exp_id: kl30_s123_eval
103	& s456 & C1 & 8.82 & 44.71 & \textbf{69.93} & 41.04 & 6.60 \\ % exp_id: eval_c1_retrain_30pct_s456
104	& & KL & \textbf{8.79} & \textbf{45.05} & 68.75 & \textbf{42.0} & \textbf{7.58} \\ % exp_id: kl30_s456_uniform_eval
105	\midrule
106	\multirow{2}{*}{50\%}
107	& s42 & C1 & 11.96 & 32.17 & \textbf{63.14} & 27.79 & \textbf{2.05} \\ % exp_id: c1_bce_kl_targets_teal50u
108	& & KL & 11.96 & \textbf{32.59} & 62.35 & \textbf{27.92} & 1.97 \\ % exp_id: c1_kl_teal50u
109	\bottomrule
110	\end{tabular}}
111	\end{table}
112	
113	At 50\% (s42, earlier oracle), C1 matches KL within 0.79pp, while magnitude-trained BCE yields $2.4\times$ worse PPL (Table~\ref{tab:main}).
114	At 30\%, retrained seeds show $\leq$1.18pp agreement\footnote{s42 oracle from earlier checkpoint (gap 0.65pp); s123/s456 use seed-matched converged oracles ($\leq$0.03pp gap).}.
115	C1 demonstrates that KL-discovered mask patterns \emph{transfer} to a simpler training mechanism (PPL within 0.79pp; downstream variation up to 4.5pp MMLU); per-layer KL controls (\S\ref{sec:perlayer}) further suggest task-dependent coupling effects.
116	However, C1 also changes mask representation: binarizing oracle soft logits ($>$0) into hard masks discards ranking information, so the near-zero delta reflects transferability of binary mask \emph{patterns} rather than full predictor knowledge. BCE+Gumbel (32.22) underperforms standard BCE (27.97), indicating trajectory-dependent confounds that prevent clean isolation of target quality from gradient coupling (Appendix~\ref{app:oracle_provenance}). % exp_id: bce50_3seed, c1_bce_kl_targets_30u, c1_s123, bce_gumbel_no_penalty_s42, eval_bce_v3_s42
117	
118	\subsection{Ablation Studies}
119	
120	Table~\ref{tab:ablation} isolates the contribution of each design choice at 30\% and 50\% sparsity.
121	
122	\begin{table}[t]
123	\centering
124	\caption{Ablation on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$; uniform at 30\%, global at 50\%). $\pm$: 3-seed; unmarked: s42. $^\ddagger$STE: 20.8\% actual sparsity at 30\% target; loss effect ($\Delta$PPL=20.4) is $5.1\times$ relaxation effect ($\Delta$PPL=3.98). $^\S$MSE 50\%: 2/3 seeds collapsed to ${\sim}$5\% actual sparsity; s42 only (Appendix~\ref{app:mse_config}).}
125	\label{tab:ablation}
126	\resizebox{\columnwidth}{!}{
127	\begin{tabular}{lccc}
128	\toprule
129	Configuration & 30\% PPL$\downarrow$ & 50\% PPL$\downarrow$ & $\Delta_{50}$ \\
130	\midrule
131	\multicolumn{4}{l}{\textit{KL-based variants}} \\
132	Forward KL + Gumbel (Ours) & \textbf{8.81$\pm$0.02} & \textbf{11.79} & --- \\ % exp_id: kl30_ablation_s42, bench_kl50_global
133	JSD (symmetric) + Gumbel & 8.90$\pm$0.02 & 12.54 & +0.75 \\ % exp_id: jsd30_ablation_s42, jsd_ablation_s42
134	Reverse KL + Gumbel & 9.26$\pm$0.07 & 12.80 & +1.01 \\ % exp_id: rkl30_ablation_s42, reverse_kl_ablation_s42
135	Forward KL + STE & ---$^\ddagger$ & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
136	\midrule
137	\multicolumn{4}{l}{\textit{Per-layer training}} \\
138	Per-layer MSE & 18.52$\pm$1.68 & 229.26$^\S$ & +217.47 \\ % exp_id: mse30_uniform_s42, mse50_uniform_s42
139	Per-layer KL ($K{=}1$) & 9.05$\pm$0.02 & 34.85 & +23.06 \\ % exp_id: perlayer_kl_30_3seed, perlayer_kl_50_s42
140	Per-layer KL ($K{=}4$) & 8.89$\pm$0.01 & 44.23 & +32.44 \\ % exp_id: perlayer_kl_k4_3seed, perlayer_kl_k4_50_s42
141	\midrule
142	\multicolumn{4}{l}{\textit{BCE-based variants}} \\
143	BCE (no compensation) & 15.71 & 27.97 & +16.18 \\ % exp_id: bce30_uniform_s42, eval_bce_v3_s42
144	BCE + Gumbel (no penalty) & --- & 32.22 & +20.43 \\ % exp_id: bce_gumbel_no_penalty_s42
145	BCE + Gumbel + Penalty & --- & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
146	BCE + STE & --- & 60.54 & +48.75 \\ % exp_id: bce_ste_s42
147	\bottomrule
148	\end{tabular}}
149	\end{table}
150	
151	\paragraph{Relaxation, Divergence, and SPON.}
152	At 50\%, Gumbel-Sigmoid outperforms STE~\cite{bengio2013ste} by 33.8\% (11.79 vs.\ 15.77); forward KL outperforms JSD (+6.4\%) and reverse KL (+8.6\%), consistent with mode-covering~\cite{gu2024minillm}. % exp_id: ste_baseline_s42, jsd_ablation_s42, reverse_kl_ablation_s42
153	At 30\%, forward KL (8.81) and JSD (8.90) are near-identical, both outperforming reverse KL (9.26) and MSE (18.52$\pm$1.68). % exp_id: kl30_ablation_s42, jsd30_ablation_s42, rkl30_ablation_s42, mse30_uniform_s42, mse30_3seed
154	KL--JSD near-equivalence suggests the divergence measure matters less than optimizing through the output distribution; coupling scope may provide additional downstream benefits (\S\ref{sec:perlayer}). % exp_id: bce30_uniform_s42, rkl30_downstream_3seed
155	\paragraph{Per-Layer KL: Empirical Signal Type vs.\ Coupling Scope.}
156	\label{sec:perlayer}
157	To isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.
158	The $K$-curve (Figure~\ref{fig:k_curve_ppl}) reveals three empirical patterns at 30\%: (1)~PPL is non-monotonic, with $K{=}2$ worst (10.75$\pm$0.15) due to insufficient per-layer updates and $K{=}16$ best (8.67$\pm$0.02), marginally outperforming E2E (8.81$\pm$0.02); (2)~at $K{=}1$ (no coupling), per-layer KL achieves 9.05$\pm$0.02, within 2.7\% of E2E, while per-layer MSE degrades to 18.52$\pm$1.68 ($2.05\times$ worse); (3)~the signal type\footnote{We use ``signal type'' as shorthand for the training objective's optimization target (output distribution vs.\ intermediate activations); this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled.} gap ($K{=}1$ KL 9.05 vs.\ MSE 18.52: 9.47 PPL) exceeds the coupling breadth range ($K{=}16$ 8.67 vs.\ $K{=}2$ 10.75: 2.08 PPL).
159	This suggests output-distribution alignment contributes more than coupling scope to PPL, but the decomposition is confounded by train--inference mismatch ($K{=}1$ masks 1/32 layers during training vs.\ all 32 at inference), per-layer update count disparity, and the 50\% failure where $K{=}1$ (34.85) outperforms $K{=}4$ (44.23) while E2E reaches 11.84.
160	A 3-seed $K{=}4$ control\footnote{Actual sparsity 29.6\%; per-layer sparsity std=0.003 (near-uniform).} partially deconfounds (Appendix~\ref{app:k4_downstream}): PPL and GSM8K gaps largely close while commonsense gaps (ARC-c, WG) persist, suggesting task-dependent coupling effects; detailed per-task attribution is in Appendices~\ref{app:k4_downstream}--\ref{app:perlayer_downstream}. % exp_id: perlayer_kl_30_3seed, perlayer_kl_downstream, mse30_downstream_decomp, perlayer_kl_k4_3seed, perlayer_kl_k4_50_s42, perlayer_kl_50_s42, bench_kl50_global, k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed
161	
162	\begin{figure}[t]
163	\centering
164	\includegraphics[width=\columnwidth]{k_curve_ppl}
165	\vspace{-8pt}
166	\caption{Coupling breadth $K$ vs.\ perplexity (30\%, TEAL uniform, 3-seed mean$\pm$std). $K{=}32$ denotes end-to-end training. $K{=}2$ degradation reflects insufficient per-layer updates (${\sim}62$ vs.\ ${\sim}250$ at $K{=}8$).}
167	\label{fig:k_curve_ppl}
168	\vspace{-8pt}
169	\end{figure}
170	
171	\paragraph{Compensation Redundancy.}
172	\label{sec:compensation}
173	FastForward-style compensation~\cite{gautam2026fastforward} (+67.2M params) provides no benefit (Appendices~\ref{app:comp_convergence}--\ref{app:training_convergence}). % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42, bce_comp_staged_s42, db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep
174	
175	
176	\subsection{Sparsity Scaling and Regime Analysis}
177	\label{sec:scaling}
178	
179	\begin{figure}[t]
180	\centering
181	\includegraphics[width=\columnwidth]{fig2_sparsity_sweep.pdf}
182	\vspace{-8pt}
183	\caption{PPL scaling with sparsity (global allocation). KL's advantage over TEAL grows with sparsity.}
184	\label{fig:sparsity_sweep}
185	\vspace{-8pt}
186	\end{figure}
187	
188	\paragraph{Allocation Behavior.}
189	Table~\ref{tab:phase} (Appendix~\ref{app:alloc_full}) reveals non-monotonic allocation preference: uniform is best at $\leq$30\% ($7.3\times$ smaller MMLU $\sigma$), global at 35--40\%, both collapse at $\geq$45\%. % exp_id: kl30_3seed, regime_kl35_global, regime_kl35_uniform, multi_seed_kl50_global, multi_seed_kl50_uniform
190	
191	\paragraph{Cross-Architecture and Scale.}
192	\label{sec:cross_arch}
193	On Mistral-7B-v0.3~\cite{jiang2023mistral}, PPL generalizes ($-$17.3\%, 3-seed; Table~\ref{tab:mistral_downstream}); on Qwen-2.5-14B~\cite{qwen2024qwen25}, PPL generalizes but MMLU/GSM8K decline (Table~\ref{tab:14b}).
194	Consistent regression across scales (8B MMLU $-$5.2pp, 14B GSM8K 32.2$\pm$5.3 vs.\ 52.1) suggests systematic limitations of output-distribution KL. The pipeline adds 6.4\% latency overhead absent sparse kernels (Appendix~\ref{app:latency}). % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, mistral_teal30_downstream, qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform, latency_profiling
195	
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea327eb2-b676-4ec1-afc7-68333c05e066",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "8dca6d01-6058-45be-8f55-7def5245a581",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + GELU + Linear($128 \\to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB), using AdamW~\\cite{loshchilov2019adamw} with learning rate $1 \\times 10^{-3}$, weight decay $1 \\times 10^{-2}$, and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly\\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \\textbf{BCE predictor} (DejaVu-style~\\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; and (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison. Uniform allocation preserves downstream performance best; global allocation is analyzed to understand allocation-quality tradeoffs (\\S\\ref{sec:scaling}).\nAt 30\\% sparsity, output-distribution KL under uniform allocation achieves PPL 8.81$\\pm$0.02 (3-seed), a 14.5\\% reduction over TEAL at matched actual sparsity (8.81 vs.\\ 10.30, both at 28.5\\%; Appendix~\\ref{app:ood}).\nUniform allocation yields stable downstream (MMLU 40.7$\\pm$1.3\\%, 3-seed; Appendix~\\ref{app:stability}), while global top-$k$ exhibits high seed variance (35.7$\\pm$9.5\\%) from late-layer starvation (L31 retention 28.4\\%; \\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform, kl30_3seed\n\n\\paragraph{Task-Type Split.}\nKL shows directional improvements over TEAL on commonsense reasoning (ARC-c, WG, HellaSwag, PIQA: 4/4 wins at 30\\% uniform) but underperforms on knowledge-intensive tasks (MMLU, GSM8K: 0/2).\nWith only three seeds, 95\\% confidence intervals for individual downstream tasks overlap; we therefore treat PPL ($\\sigma{=}0.02$, non-overlapping) as the primary metric and downstream differences as directional evidence.\nThe KL predictor protects L14--L18 (14--18\\% sparsity vs.\\ 32\\% global mean) while aggressively pruning L22--L28 (48--57\\%). Constraint interventions (Appendix~\\ref{app:constraint}) confirm a task-dependent trade-off: removing the valley improves MMLU +3.4pp but reduces ARC-c by 1.5pp, consistent with localized factual associations~\\cite{geva2023dissecting}; task-aware allocation may resolve this. % exp_id: bench_kl30_uniform, teal30_uniform, hellaswag_piqa_kl30_uniform, perlayer_sparsity_analysis, constraint_protect_late, constraint_remove_valley\n\n\\paragraph{Knowledge-Task Regression: Hypothesis.}\nConstraint experiments (Appendix~\\ref{app:constraint}) confirm allocation contributes: removing the learned valley improves MMLU +3.4pp and GSM8K +1.6pp. A C4-trained control (Appendix~\\ref{app:c4_control}) does not alleviate the regression (MMLU 40.0\\%, GSM8K 4.1\\% vs.\\ 40.7\\%, 7.5\\%), confirming the deficit is structural to forward KL's mode-covering property~\\cite{meng2022locating} rather than training data composition. % exp_id: constraint_remove_valley, c4_control_eval\n\nAt 50\\%, the PPL advantage widens (11.92 vs.\\ 23.90, 50\\% reduction) and generalizes to C4 (Appendix~\\ref{app:ood}), but all methods collapse to near-random on MMLU and GSM8K ($\\leq$2.7\\%); no allocation strategy recovers at this capacity limit. % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval, d030_kl50_uniform, multi_seed_kl50_global\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. $^\\ast$$2.71\\times$ KL compute (\\S\\ref{sec:isocompute}). $\\pm$: 3-seed; unmarked: s42. $^\\ddagger$Actual sparsity: KL 28.5\\% vs.\\ TEAL 29.3\\% at 30\\% (Appendix~\\ref{app:ood}).}\n\\label{tab:main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{6}{*}{30\\%}\n& TEAL uniform & 10.82 & 39.33 & 65.04 & \\textbf{45.86} & \\textbf{8.79} \\\\ % exp_id: teal30_uniform\n& BCE global & 11.25 & 41.2 & 66.0 & 36.3 & 6.0 \\\\ % exp_id: bce30_teal_global\n& BCE uniform & 15.09$\\pm$0.13 & 33.45 & 61.09 & 43.05 & 3.97 \\\\ % exp_id: bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456\n& MSE uniform & 18.52$\\pm$1.68 & 35.8$\\pm$4.1 & 59.8$\\pm$2.6 & 30.7$\\pm$2.6 & 2.3$\\pm$0.7 \\\\ % exp_id: mse30_3seed\n& KL global (Ours)$^\\ddagger$ & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & 8.0$\\pm$0.7 \\\\ % exp_id: kl30_3seed_global\n& KL uniform$^\\ddagger$ & \\textbf{8.81$\\pm$0.02} & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & 40.7$\\pm$1.3 & 7.5$\\pm$0.1 \\\\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform\n\\midrule\n\\multirow{5}{*}{50\\%}\n& TEAL uniform & 23.90 & 27.47 & 54.38 & \\textbf{29.26} & 1.74 \\\\ % exp_id: teal50_uniform\n& BCE (2700 steps)$^\\ast$ & 28.13$\\pm$0.20 & 27.6$\\pm$0.6 & 51.8$\\pm$0.6 & 26.1$\\pm$0.5 & 2.1$\\pm$0.2 \\\\ % exp_id: bce50_3seed\n& MSE uniform & 229.26 & 25.00 & 50.59 & 23.79 & 1.59 \\\\ % exp_id: mse50_uniform_s42\n& KL global (Ours) & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & 28.3$\\pm$0.7 & \\textbf{2.7$\\pm$1.3} \\\\ % exp_id: bench_kl50_global (s42), kl50_global_s123_reeval (s123 PPL), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456)\n& KL uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\ % exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\subsection{Extended Training Analysis}\n\\label{sec:isocompute}\n\nAt $2.71\\times$ KL compute budget (2700 steps, matched wall-clock), BCE achieves PPL 28.13$\\pm$0.20 (3-seed), still $2.39\\times$ worse than KL (11.79). % exp_id: bce50_3seed\nThe gap is systematic: BCE reaches higher oracle F1 (0.613 vs.\\ 0.540) with 139\\% worse PPL, confirming KL optimizes for distributional fidelity rather than magnitude agreement. % exp_id: f1_oracle_analysis, bce_isocompute_s42\n\n\n\\subsection{Mask Pattern Analysis}\n\\label{sec:mask_analysis}\n\nKL-derived masks diverge from magnitude oracles: per-layer Jaccard distance averages 68\\% at 50\\% (64 samples, 131K tokens; Figure~\\ref{fig:mask_heatmap}), with cross-seed variation (36.3\\%) confirming systematic divergence (Appendices~\\ref{app:cross_seed_jaccard},~\\ref{app:mask_viz}).\nDespite this, KL achieves PPL 11.79 vs.\\ BCE's 28.13$\\pm$0.20, confirming that distributional fidelity, not magnitude agreement, produces better masks. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap\nDivergence follows a U-shaped per-layer pattern, peaking in late layers (0.70--0.75 at 50\\%). % exp_id: c1_mask_overlap\n\n\\paragraph{Target-Swap Ablation: Target Quality vs.\\ Gradient Coupling.}\nTo disentangle whether KL's advantage stems from its coupled gradient pathway or from the mask patterns it discovers, we train a standard BCE predictor on KL-derived oracle masks instead of magnitude-based masks (C1 target-swap ablation).\nTable~\\ref{tab:c1} reports results under TEAL uniform allocation at matched sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Target-swap ablation (C1): BCE on KL-derived masks vs.\\ KL predictor (same seed), TEAL uniform. All seeds show max $\\Delta$$\\leq$1.70pp at 30\\%; max $\\Delta$$\\leq$0.79pp at 50\\% (s42). $^\\dagger$\\textbf{Provenance:} s42 oracle extracted from an earlier training run (not seed-matched); s123/s456 use seed-matched retrained oracles (Appendix~\\ref{app:oracle_provenance}).}\n\\label{tab:c1}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lllccccc}\n\\toprule\nSparsity & Seed & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n\\multirow{6}{*}{30\\%}\n& s42$^\\dagger$ & C1 & 9.45 & 40.27 & 67.40 & \\textbf{42.30} & \\textbf{7.58} \\\\ % exp_id: c1_ablation_30pct_s42_eval_v2\n& & KL & \\textbf{8.82} & \\textbf{40.78} & \\textbf{68.59} & 40.6 & 7.35 \\\\ % exp_id: bench_kl30_uniform\n& s123 & C1 & 8.84 & 44.71 & \\textbf{69.77} & \\textbf{39.92} & 6.82 \\\\ % exp_id: eval_c1_retrain_30pct_s123\n& & KL & \\textbf{8.83} & \\textbf{45.31} & 69.38 & 39.4 & \\textbf{7.51} \\\\ % exp_id: kl30_s123_eval\n& s456 & C1 & 8.82 & 44.71 & \\textbf{69.93} & 41.04 & 6.60 \\\\ % exp_id: eval_c1_retrain_30pct_s456\n& & KL & \\textbf{8.79} & \\textbf{45.05} & 68.75 & \\textbf{42.0} & \\textbf{7.58} \\\\ % exp_id: kl30_s456_uniform_eval\n\\midrule\n\\multirow{2}{*}{50\\%}\n& s42 & C1 & 11.96 & 32.17 & \\textbf{63.14} & 27.79 & \\textbf{2.05} \\\\ % exp_id: c1_bce_kl_targets_teal50u\n& & KL & 11.96 & \\textbf{32.59} & 62.35 & \\textbf{27.92} & 1.97 \\\\ % exp_id: c1_kl_teal50u\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt 50\\% (s42, earlier oracle), C1 matches KL within 0.79pp, while magnitude-trained BCE yields $2.4\\times$ worse PPL (Table~\\ref{tab:main}).\nAt 30\\%, retrained seeds show $\\leq$1.18pp agreement\\footnote{s42 oracle from earlier checkpoint (gap 0.65pp); s123/s456 use seed-matched converged oracles ($\\leq$0.03pp gap).}.\nC1 demonstrates that KL-discovered mask patterns \\emph{transfer} to a simpler training mechanism (PPL within 0.79pp; downstream variation up to 4.5pp MMLU); per-layer KL controls (\\S\\ref{sec:perlayer}) further suggest task-dependent coupling effects.\nHowever, C1 also changes mask representation: binarizing oracle soft logits ($>$0) into hard masks discards ranking information, so the near-zero delta reflects transferability of binary mask \\emph{patterns} rather than full predictor knowledge. BCE+Gumbel (32.22) underperforms standard BCE (27.97), indicating trajectory-dependent confounds that prevent clean isolation of target quality from gradient coupling (Appendix~\\ref{app:oracle_provenance}). % exp_id: bce50_3seed, c1_bce_kl_targets_30u, c1_s123, bce_gumbel_no_penalty_s42, eval_bce_v3_s42\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 30\\% and 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$; uniform at 30\\%, global at 50\\%). $\\pm$: 3-seed; unmarked: s42. $^\\ddagger$STE: 20.8\\% actual sparsity at 30\\% target; loss effect ($\\Delta$PPL=20.4) is $5.1\\times$ relaxation effect ($\\Delta$PPL=3.98). $^\\S$MSE 50\\%: 2/3 seeds collapsed to ${\\sim}$5\\% actual sparsity; s42 only (Appendix~\\ref{app:mse_config}).}\n\\label{tab:ablation}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\nConfiguration & 30\\% PPL$\\downarrow$ & 50\\% PPL$\\downarrow$ & $\\Delta_{50}$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{KL-based variants}} \\\\\nForward KL + Gumbel (Ours) & \\textbf{8.81$\\pm$0.02} & \\textbf{11.79} & --- \\\\ % exp_id: kl30_ablation_s42, bench_kl50_global\nJSD (symmetric) + Gumbel & 8.90$\\pm$0.02 & 12.54 & +0.75 \\\\ % exp_id: jsd30_ablation_s42, jsd_ablation_s42\nReverse KL + Gumbel & 9.26$\\pm$0.07 & 12.80 & +1.01 \\\\ % exp_id: rkl30_ablation_s42, reverse_kl_ablation_s42\nForward KL + STE & ---$^\\ddagger$ & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\n\\midrule\n\\multicolumn{4}{l}{\\textit{Per-layer training}} \\\\\nPer-layer MSE & 18.52$\\pm$1.68 & 229.26$^\\S$ & +217.47 \\\\ % exp_id: mse30_uniform_s42, mse50_uniform_s42\nPer-layer KL ($K{=}1$) & 9.05$\\pm$0.02 & 34.85 & +23.06 \\\\ % exp_id: perlayer_kl_30_3seed, perlayer_kl_50_s42\nPer-layer KL ($K{=}4$) & 8.89$\\pm$0.01 & 44.23 & +32.44 \\\\ % exp_id: perlayer_kl_k4_3seed, perlayer_kl_k4_50_s42\n\\midrule\n\\multicolumn{4}{l}{\\textit{BCE-based variants}} \\\\\nBCE (no compensation) & 15.71 & 27.97 & +16.18 \\\\ % exp_id: bce30_uniform_s42, eval_bce_v3_s42\nBCE + Gumbel (no penalty) & --- & 32.22 & +20.43 \\\\ % exp_id: bce_gumbel_no_penalty_s42\nBCE + Gumbel + Penalty & --- & 38.02 & +26.23 \\\\ % exp_id: bce_gumbel_lagrangian_isolation\nBCE + STE & --- & 60.54 & +48.75 \\\\ % exp_id: bce_ste_s42\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Relaxation, Divergence, and SPON.}\nAt 50\\%, Gumbel-Sigmoid outperforms STE~\\cite{bengio2013ste} by 33.8\\% (11.79 vs.\\ 15.77); forward KL outperforms JSD (+6.4\\%) and reverse KL (+8.6\\%), consistent with mode-covering~\\cite{gu2024minillm}. % exp_id: ste_baseline_s42, jsd_ablation_s42, reverse_kl_ablation_s42\nAt 30\\%, forward KL (8.81) and JSD (8.90) are near-identical, both outperforming reverse KL (9.26) and MSE (18.52$\\pm$1.68). % exp_id: kl30_ablation_s42, jsd30_ablation_s42, rkl30_ablation_s42, mse30_uniform_s42, mse30_3seed\nKL--JSD near-equivalence suggests the divergence measure matters less than optimizing through the output distribution; coupling scope may provide additional downstream benefits (\\S\\ref{sec:perlayer}). % exp_id: bce30_uniform_s42, rkl30_downstream_3seed\n\\paragraph{Per-Layer KL: Empirical Signal Type vs.\\ Coupling Scope.}\n\\label{sec:perlayer}\nTo isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.\nThe $K$-curve (Figure~\\ref{fig:k_curve_ppl}) reveals three empirical patterns at 30\\%: (1)~PPL is non-monotonic, with $K{=}2$ worst (10.75$\\pm$0.15) due to insufficient per-layer updates and $K{=}16$ best (8.67$\\pm$0.02), marginally outperforming E2E (8.81$\\pm$0.02); (2)~at $K{=}1$ (no coupling), per-layer KL achieves 9.05$\\pm$0.02, within 2.7\\% of E2E, while per-layer MSE degrades to 18.52$\\pm$1.68 ($2.05\\times$ worse); (3)~the signal type\\footnote{We use ``signal type'' as shorthand for the training objective's optimization target (output distribution vs.\\ intermediate activations); this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled.} gap ($K{=}1$ KL 9.05 vs.\\ MSE 18.52: 9.47 PPL) exceeds the coupling breadth range ($K{=}16$ 8.67 vs.\\ $K{=}2$ 10.75: 2.08 PPL).\nThis suggests output-distribution alignment contributes more than coupling scope to PPL, but the decomposition is confounded by train--inference mismatch ($K{=}1$ masks 1/32 layers during training vs.\\ all 32 at inference), per-layer update count disparity, and the 50\\% failure where $K{=}1$ (34.85) outperforms $K{=}4$ (44.23) while E2E reaches 11.84.\nA 3-seed $K{=}4$ control\\footnote{Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform).} partially deconfounds (Appendix~\\ref{app:k4_downstream}): PPL and GSM8K gaps largely close while commonsense gaps (ARC-c, WG) persist, suggesting task-dependent coupling effects; detailed per-task attribution is in Appendices~\\ref{app:k4_downstream}--\\ref{app:perlayer_downstream}. % exp_id: perlayer_kl_30_3seed, perlayer_kl_downstream, mse30_downstream_decomp, perlayer_kl_k4_3seed, perlayer_kl_k4_50_s42, perlayer_kl_50_s42, bench_kl50_global, k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{k_curve_ppl}\n\\vspace{-8pt}\n\\caption{Coupling breadth $K$ vs.\\ perplexity (30\\%, TEAL uniform, 3-seed mean$\\pm$std). $K{=}32$ denotes end-to-end training. $K{=}2$ degradation reflects insufficient per-layer updates (${\\sim}62$ vs.\\ ${\\sim}250$ at $K{=}8$).}\n\\label{fig:k_curve_ppl}\n\\vspace{-8pt}\n\\end{figure}\n\n\\paragraph{Compensation Redundancy.}\n\\label{sec:compensation}\nFastForward-style compensation~\\cite{gautam2026fastforward} (+67.2M params) provides no benefit (Appendices~\\ref{app:comp_convergence}--\\ref{app:training_convergence}). % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42, bce_comp_staged_s42, db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep\n\n\n\\subsection{Sparsity Scaling and Regime Analysis}\n\\label{sec:scaling}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_sparsity_sweep.pdf}\n\\vspace{-8pt}\n\\caption{PPL scaling with sparsity (global allocation). KL's advantage over TEAL grows with sparsity.}\n\\label{fig:sparsity_sweep}\n\\vspace{-8pt}\n\\end{figure}\n\n\\paragraph{Allocation Behavior.}\nTable~\\ref{tab:phase} (Appendix~\\ref{app:alloc_full}) reveals non-monotonic allocation preference: uniform is best at $\\leq$30\\% ($7.3\\times$ smaller MMLU $\\sigma$), global at 35--40\\%, both collapse at $\\geq$45\\%. % exp_id: kl30_3seed, regime_kl35_global, regime_kl35_uniform, multi_seed_kl50_global, multi_seed_kl50_uniform\n\n\\paragraph{Cross-Architecture and Scale.}\n\\label{sec:cross_arch}\nOn Mistral-7B-v0.3~\\cite{jiang2023mistral}, PPL generalizes ($-$17.3\\%, 3-seed; Table~\\ref{tab:mistral_downstream}); on Qwen-2.5-14B~\\cite{qwen2024qwen25}, PPL generalizes but MMLU/GSM8K decline (Table~\\ref{tab:14b}).\nConsistent regression across scales (8B MMLU $-$5.2pp, 14B GSM8K 32.2$\\pm$5.3 vs.\\ 52.1) suggests systematic limitations of output-distribution KL. The pipeline adds 6.4\\% latency overhead absent sparse kernels (Appendix~\\ref{app:latency}). % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, mistral_teal30_downstream, qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform, latency_profiling\n\n",
      "numLines": 196,
      "startLine": 1,
      "totalLines": 196
    }
  },
  "sourceToolAssistantUUID": "ea327eb2-b676-4ec1-afc7-68333c05e066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-24T04:22:24.856Z_

<details open><summary>🔧 Tool call — Read · `toolu_016JjDtiUSt9wDPqfHBjsa41`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dca6d01-6058-45be-8f55-7def5245a581",
  "isSidechain": false,
  "requestId": "req_011CbLkj1eggAw8hUfJ9hBHY",
  "type": "assistant",
  "uuid": "5f3d30c3-a5d1-4f1a-bd3a-c28c2e6dbdc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP9sqAKds59As6Sv12idsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 39983,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 39983,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-24T04:22:24.865Z_

<details><summary>↩ Tool result · `toolu_016JjDtiUSt9wDPqfHBjsa41`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	ActTail~\cite{zheng2026acttail} applies heavy-tailed self-regularization for global activation sparsity allocation; WiSparse~\cite{yang2026wisparse} proposes weight-aware mixed activation sparsity.
11	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
12	
13	\paragraph{Predictor-Based Contextual Sparsity.}
14	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
15	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
16	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
17	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
18	Dhar et al.~\cite{dhar2025clustering} compress activation patterns via clustering for efficient neuron-level prediction.
19	LazyLLM~\cite{fu2024lazyllm} dynamically prunes tokens across layers for long-context efficiency; COTS~\cite{zhang2025cots} exploits connected activation patterns for structured sparse inference.
20	PowerInfer~\cite{song2024powerinfer} and PowerInfer-2~\cite{xue2024powerinfer2} exploit power-law activation frequencies for GPU--CPU/NPU scheduling.
21	MaskLLM~\cite{fang2024maskllm} shares the recipe-level principle of frozen weights + learnable masks + KL training.
22	The methods differ in three respects: (a) MaskLLM's mask parameters are fixed per input (static N:M weight sparsity via Gumbel-Softmax), while our predictor generates \emph{per-token} masks that must generalize to unseen inputs; (b) static N:M patterns have no cross-layer allocation interaction, whereas our masks coordinate through TEAL's global top-$k$; (c) activation masks must be robust to distribution shift at inference, while weight masks are input-independent.
23	Our contribution beyond the shared recipe is analytical: a systematic decomposition of signal type vs.\ coupling scope for sparsity prediction training, via target-swap ablation and per-layer KL controls (\S\ref{sec:perlayer}).
24	All prior predictor-based methods for activation sparsity use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
25	We empirically observe that an output-distribution-coupled objective propagates gradients through all downstream layers and quantify when this matters for global allocation quality.
26	
27	\paragraph{Static Bias Correction.}
28	SPON (Spontaneous Neurons;~\citealp{xu2025spon}) learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.
29	Our method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers that produces input-dependent masks.
30	SPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are weakly correlated (cosine similarity 0.196, $R^2$=0.038; \S\ref{sec:experiments}).
31	
32	\paragraph{Activation Function Engineering.}
33	ReLU Strikes Back~\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\% natural sparsity; TurboSparse~\cite{song2024turbosparse} and ProSparse~\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.
34	MiniTron~\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.
35	Haziza et al.~\cite{haziza2025accelerating} demonstrate 2:4 semi-structured activation sparsity with hardware-native acceleration, complementing our unstructured approach.
36	MoC~\cite{wu2025moc} selectively activates Top-$K$ FFN channels using SwiGLU's native gating during pretraining.
37	All require retraining or weight modification; our method is a plug-in predictor on \emph{unmodified} SwiGLU models.
38	
39	\paragraph{Weight Pruning, Distillation, and Routing.}
40	Wanda~\cite{sun2024wanda}, SparseGPT~\cite{frantar2023sparsegpt}, and SliceGPT~\cite{ashkboos2024slicegpt} produce static weight masks via one-shot or structured pruning; Polar Sparsity~\cite{shrestha2025polar} scales contextual sparsity to batched inference by shifting focus from MLP to attention head sparsity; Alizadeh et al.~\cite{alizadeh2024llmflash} leverage activation sparsity for memory-efficient inference via selective flash loading.
41	Switch Transformers~\cite{fedus2022switch} and Mixture-of-Depths~\cite{raposo2024mod} achieve conditional computation through learned routing.
42	KL-based distillation~\cite{kim2016sequencekd,sanh2019distilbert,gu2024minillm,agarwal2024gkd,ko2024distillm} trains compact students; SparseLoRA~\cite{khaki2025sparselora} exploits contextual sparsity for fine-tuning.
43	We apply the KL principle to train a sparsity predictor on unmodified dense models, using Gumbel-Sigmoid sampling~\cite{maddison2017concrete,louizos2018l0} for differentiable discrete mask optimization.
44	
45	\paragraph{MoE Routing and Gated Sparsity.}
46	Expert Choice routing~\cite{zhou2022expertchoice} lets each expert select its top-$k$ tokens under a fixed capacity budget, a global allocation perspective that parallels TEAL's neuron-level global top-$k$.
47	D2D-MoE~\cite{szatkowski2024d2dmoe} converts dense SwiGLU layers into dynamic-$k$ MoE by exploiting the same activation sparsity we target, but restructures the network into discrete experts rather than predicting masks on the original architecture.
48	MoNE~\cite{cheng2025mone} applies neuron-granular top-$k$ selection within each MoE expert during pretraining for fine-grained conditional computation without additional routing parameters.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f3d30c3-a5d1-4f1a-bd3a-c28c2e6dbdc2",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "66c8738b-1d87-49db-b441-bc1cfa530e87",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Training-Free Activation Sparsity.}\nTEAL~\\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\\% sparsity with no training cost.\nCATS~\\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\\cite{shin2025sparseinfer} and GRASP~\\cite{shin2025grasp} predict activation sparsity patterns without additional training.\nLaRoSA~\\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.\nWang et al.~\\cite{wang2025dynamicsparse}, AWQ~\\cite{lin2024awq}, and Outlier Suppression+~\\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.\nDhar et al.~\\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.\nOWL~\\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.\nActTail~\\cite{zheng2026acttail} applies heavy-tailed self-regularization for global activation sparsity allocation; WiSparse~\\cite{yang2026wisparse} proposes weight-aware mixed activation sparsity.\nAll training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \\emph{input-dependent} masks trained to minimize output-distribution divergence.\n\n\\paragraph{Predictor-Based Contextual Sparsity.}\nDejaVu~\\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.\nShadowLLM~\\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.\nFastForward~\\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.\nSVD-CSP~\\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.\nDhar et al.~\\cite{dhar2025clustering} compress activation patterns via clustering for efficient neuron-level prediction.\nLazyLLM~\\cite{fu2024lazyllm} dynamically prunes tokens across layers for long-context efficiency; COTS~\\cite{zhang2025cots} exploits connected activation patterns for structured sparse inference.\nPowerInfer~\\cite{song2024powerinfer} and PowerInfer-2~\\cite{xue2024powerinfer2} exploit power-law activation frequencies for GPU--CPU/NPU scheduling.\nMaskLLM~\\cite{fang2024maskllm} shares the recipe-level principle of frozen weights + learnable masks + KL training.\nThe methods differ in three respects: (a) MaskLLM's mask parameters are fixed per input (static N:M weight sparsity via Gumbel-Softmax), while our predictor generates \\emph{per-token} masks that must generalize to unseen inputs; (b) static N:M patterns have no cross-layer allocation interaction, whereas our masks coordinate through TEAL's global top-$k$; (c) activation masks must be robust to distribution shift at inference, while weight masks are input-independent.\nOur contribution beyond the shared recipe is analytical: a systematic decomposition of signal type vs.\\ coupling scope for sparsity prediction training, via target-swap ablation and per-layer KL controls (\\S\\ref{sec:perlayer}).\nAll prior predictor-based methods for activation sparsity use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.\nWe empirically observe that an output-distribution-coupled objective propagates gradients through all downstream layers and quantify when this matters for global allocation quality.\n\n\\paragraph{Static Bias Correction.}\nSPON (Spontaneous Neurons;~\\citealp{xu2025spon}) learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.\nOur method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers that produces input-dependent masks.\nSPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are weakly correlated (cosine similarity 0.196, $R^2$=0.038; \\S\\ref{sec:experiments}).\n\n\\paragraph{Activation Function Engineering.}\nReLU Strikes Back~\\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\\% natural sparsity; TurboSparse~\\cite{song2024turbosparse} and ProSparse~\\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.\nMiniTron~\\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.\nHaziza et al.~\\cite{haziza2025accelerating} demonstrate 2:4 semi-structured activation sparsity with hardware-native acceleration, complementing our unstructured approach.\nMoC~\\cite{wu2025moc} selectively activates Top-$K$ FFN channels using SwiGLU's native gating during pretraining.\nAll require retraining or weight modification; our method is a plug-in predictor on \\emph{unmodified} SwiGLU models.\n\n\\paragraph{Weight Pruning, Distillation, and Routing.}\nWanda~\\cite{sun2024wanda}, SparseGPT~\\cite{frantar2023sparsegpt}, and SliceGPT~\\cite{ashkboos2024slicegpt} produce static weight masks via one-shot or structured pruning; Polar Sparsity~\\cite{shrestha2025polar} scales contextual sparsity to batched inference by shifting focus from MLP to attention head sparsity; Alizadeh et al.~\\cite{alizadeh2024llmflash} leverage activation sparsity for memory-efficient inference via selective flash loading.\nSwitch Transformers~\\cite{fedus2022switch} and Mixture-of-Depths~\\cite{raposo2024mod} achieve conditional computation through learned routing.\nKL-based distillation~\\cite{kim2016sequencekd,sanh2019distilbert,gu2024minillm,agarwal2024gkd,ko2024distillm} trains compact students; SparseLoRA~\\cite{khaki2025sparselora} exploits contextual sparsity for fine-tuning.\nWe apply the KL principle to train a sparsity predictor on unmodified dense models, using Gumbel-Sigmoid sampling~\\cite{maddison2017concrete,louizos2018l0} for differentiable discrete mask optimization.\n\n\\paragraph{MoE Routing and Gated Sparsity.}\nExpert Choice routing~\\cite{zhou2022expertchoice} lets each expert select its top-$k$ tokens under a fixed capacity budget, a global allocation perspective that parallels TEAL's neuron-level global top-$k$.\nD2D-MoE~\\cite{szatkowski2024d2dmoe} converts dense SwiGLU layers into dynamic-$k$ MoE by exploiting the same activation sparsity we target, but restructures the network into discrete experts rather than predicting masks on the original architecture.\nMoNE~\\cite{cheng2025mone} applies neuron-granular top-$k$ selection within each MoE expert during pretraining for fine-grained conditional computation without additional routing parameters.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "5f3d30c3-a5d1-4f1a-bd3a-c28c2e6dbdc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-24T04:22:25.307Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YU3RjZNf3RQBkZEaP9MNqp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66c8738b-1d87-49db-b441-bc1cfa530e87",
  "isSidechain": false,
  "requestId": "req_011CbLkj1eggAw8hUfJ9hBHY",
  "type": "assistant",
  "uuid": "7732c046-e854-4892-80f5-cf91310f2ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP9sqAKds59As6Sv12idsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 39983,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 39983,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-24T04:22:25.312Z_

<details><summary>↩ Tool result · `toolu_01YU3RjZNf3RQBkZEaP9MNqp`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension for learned sparsity prediction, outperforming BCE and MSE across five losses.
5	The KL predictor reduces PPL by 14.5\% over TEAL at 30\%, confirmed on Mistral-7B ($-$17.3\%) and Qwen-2.5-14B.
6	Gains are task-type dependent: KL improves commonsense reasoning but degrades knowledge-intensive tasks (C4 control confirms structural to KL), suggesting KL for commonsense/PPL and TEAL for knowledge tasks.
7	The signal type gap (9.47 PPL) exceeds the coupling breadth range (2.08 PPL), though the decomposition is confounded by train--inference mismatch (\S\ref{sec:perlayer}); disentangling these factors remains an open question.
8	Downstream differences are directional ($n{=}3$, CIs overlap). Code released upon acceptance.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7732c046-e854-4892-80f5-cf91310f2ce5",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "cb321211-bcb6-43be-aded-8afb31524ead",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nOutput-distribution alignment is the primary design dimension for learned sparsity prediction, outperforming BCE and MSE across five losses.\nThe KL predictor reduces PPL by 14.5\\% over TEAL at 30\\%, confirmed on Mistral-7B ($-$17.3\\%) and Qwen-2.5-14B.\nGains are task-type dependent: KL improves commonsense reasoning but degrades knowledge-intensive tasks (C4 control confirms structural to KL), suggesting KL for commonsense/PPL and TEAL for knowledge tasks.\nThe signal type gap (9.47 PPL) exceeds the coupling breadth range (2.08 PPL), though the decomposition is confounded by train--inference mismatch (\\S\\ref{sec:perlayer}); disentangling these factors remains an open question.\nDownstream differences are directional ($n{=}3$, CIs overlap). Code released upon acceptance.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "7732c046-e854-4892-80f5-cf91310f2ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-24T04:22:27.457Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JcDmqDRnRLMqj341FxiiwX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb321211-bcb6-43be-aded-8afb31524ead",
  "isSidechain": false,
  "requestId": "req_011CbLkj1eggAw8hUfJ9hBHY",
  "type": "assistant",
  "uuid": "8a0b7e95-f482-498f-b0ea-1c99a394e190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP9sqAKds59As6Sv12idsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 39983,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 39983,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-24T04:22:27.461Z_

<details><summary>↩ Tool result · `toolu_01JcDmqDRnRLMqj341FxiiwX`</summary>

```text
1	\section*{Limitations}
2	
3	Our findings are bounded by four limitations.
4	\textbf{Sparsity sweet spot.} 30\% is the lowest-degradation level; at 50\%, all methods collapse on reasoning tasks, and a separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$19.9pp GSM8K), suggesting output-distribution objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Evaluation scope.} Open-ended generation (e.g., MT-Bench) and contexts beyond 2048 tokens remain untested.
7	\textbf{Baseline coverage.} The 30\% isocompute comparison lacks a BCE 2700-step baseline; WikiText-2 evaluation shares provenance with the training corpus (WikiText-103), partially mitigated by C4 OOD results (Appendix~\ref{app:ood}).
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a0b7e95-f482-498f-b0ea-1c99a394e190",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "aa491c20-c5d7-43df-95f5-167e7271a479",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\nOur findings are bounded by four limitations.\n\\textbf{Sparsity sweet spot.} 30\\% is the lowest-degradation level; at 50\\%, all methods collapse on reasoning tasks, and a separate predictor must be retrained per target.\n\\textbf{Knowledge-intensive regression.} KL consistently underperforms on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$19.9pp GSM8K), suggesting output-distribution objectives systematically sacrifice reasoning-critical pathways.\n\\textbf{Evaluation scope.} Open-ended generation (e.g., MT-Bench) and contexts beyond 2048 tokens remain untested.\n\\textbf{Baseline coverage.} The 30\\% isocompute comparison lacks a BCE 2700-step baseline; WikiText-2 evaluation shares provenance with the training corpus (WikiText-103), partially mitigated by C4 OOD results (Appendix~\\ref{app:ood}).\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "8a0b7e95-f482-498f-b0ea-1c99a394e190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-24T04:22:27.519Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NLTcye5T8pV4PcvdA5qRRn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa491c20-c5d7-43df-95f5-167e7271a479",
  "isSidechain": false,
  "requestId": "req_011CbLkj1eggAw8hUfJ9hBHY",
  "type": "assistant",
  "uuid": "9208c074-8482-44db-ae8d-4d1e3040d45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP9sqAKds59As6Sv12idsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 39983,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 39983,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-24T04:22:27.784Z_

<details><summary>↩ Tool result · `toolu_01NLTcye5T8pV4PcvdA5qRRn`</summary>

```text
1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.
34	Our contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.
35	
36	
37	\section{Predictor Bottleneck Sensitivity}
38	\label{app:db_sensitivity}
39	
40	Table~\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.
41	
42	\begin{table}[h]
43	\centering
44	\caption{Predictor bottleneck sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}
45	\label{tab:db_sensitivity}
46	\small
47	\begin{tabular}{lcccc}
48	\toprule
49	$d_b$ & Params & TEAL global & $\Delta$ & Per-token \\
50	\midrule
51	64 & 38.2M (0.48\%) & 12.076 & +0.9\% & 10.16 \\ % exp_id: db_sensitivity_sweep
52	128 & 75.9M (0.95\%) & 11.963 & --- & 9.218 \\ % exp_id: db_sensitivity_sweep
53	256 & 151.5M (1.89\%) & 12.105 & +1.2\% & 8.586 \\ % exp_id: db_sensitivity_sweep
54	512 & 302.5M (3.77\%) & 12.315 & +2.9\% & 7.93 \\ % exp_id: db_sensitivity_sweep
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	Under TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\to$7.93).
60	This divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.
61	The $d_b{=}128$ configuration (75.9M params, $<$1\% of base model) is therefore optimal for the TEAL inference protocol.
62	
63	\subsection{Temperature Schedule Sensitivity}
64	\label{app:tau_sensitivity}
65	
66	\begin{table}[h]
67	\centering
68	\caption{Temperature schedule sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
69	\label{tab:tau_sensitivity}
70	\small
71	\begin{tabular}{lc}
72	\toprule
73	$\tau$ Schedule & PPL$\downarrow$ \\
74	\midrule
75	Fixed $\tau{=}0.5$ & \textbf{11.861} \\ % exp_id: tau_schedule_sweep
76	Linear $1.0 \to 0.1$ (default) & 11.963 \\ % exp_id: tau_schedule_sweep
77	Fixed $\tau{=}0.1$ & 12.072 \\ % exp_id: tau_schedule_sweep
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	Temperature schedule has minimal impact ($<$1.8\% PPL variation).
83	The linear annealing default is a conservative choice; even removing annealing entirely (fixed $\tau{=}0.5$) yields comparable performance.
84	
85	\subsection{Training Convergence}
86	\label{app:training_convergence}
87	
88	\begin{table}[h]
89	\centering
90	\caption{Training convergence at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
91	\label{tab:training_convergence}
92	\small
93	\begin{tabular}{cc}
94	\toprule
95	Steps & PPL$\downarrow$ \\
96	\midrule
97	200 & 15.158 \\ % exp_id: training_steps_sweep
98	400 & 12.538 \\ % exp_id: training_steps_sweep
99	600 & 12.046 \\ % exp_id: training_steps_sweep
100	800 & 11.907 \\ % exp_id: training_steps_sweep
101	1000 & \textbf{11.906} \\ % exp_id: training_steps_sweep
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	Training converges rapidly: 95\% of the quality gap closes by step 600, and performance saturates by step 800 ($\Delta < 0.001$ between 800 and 1000 steps).
107	Our default of 1000 steps provides a conservative margin.
108	
109	
110	\section{Geometric Penalty Schedule Dynamics}
111	\label{app:lagrangian}
112	
113	Table~\ref{tab:lagrangian} reports the convergence of the geometric penalty schedule across sparsity targets.
114	The geometric doubling pattern ($1 \to 2 \to 4 \to 8 \to \ldots$) enables $\lambda$ to reach steady state within $\sim$10 steps; the deadzone ($\epsilon = 0.02$) then stabilizes $\lambda$ once actual sparsity is within $\pm$2\% of the target.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Geometric penalty schedule convergence across sparsity targets (margin $\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}
119	\label{tab:lagrangian}
120	\small
121	\begin{tabular}{lccccc}
122	\toprule
123	Target $\rho$ & $\lambda_{\max}$ & Final $\lambda$ & Actual sparsity & Deviation \\
124	\midrule
125	30\% & 5000 & 5000 (cap) & 0.285 & 5.0\% \\ % exp_id: kl_30pct_s42
126	40\% & 5000 & 625 & 0.398 & 0.5\% \\ % exp_id: kl_40pct_s42
127	50\% & 1000 & 8 & 0.504 & 0.8\% \\ % exp_id: kl_50pct_s42
128	70\% & 1000 & 1000 (cap) & 0.688 & 1.7\% \\ % exp_id: kl_70pct_s42
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	At 50\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.
134	At 30\% and 70\%, the gap between the gate prior and target is larger, driving $\lambda$ to its respective caps.
135	The 40\% target converges to $\lambda = 625$ with only 0.5\% deviation; this precision reflects a regime where the target is reachable without $\lambda$ saturation.
136	
137	\begin{figure}[h]
138	\centering
139	\includegraphics[width=\columnwidth]{lagrangian_dynamics.pdf}
140	\caption{Lagrangian controller dynamics for 30\% sparsity target ($\lambda_{\max}=5000$). Left axis (log scale): penalty weight $\lambda$ rises from $0.01$ to its cap once actual sparsity undershoots the target at $\sim$step~150, exhibiting bang-bang oscillations before saturating. Right axis: actual sparsity (solid) converges from the natural density ($\approx$0.41) toward the target (dashed) and stabilizes near 0.28.}
141	\label{fig:lagrangian_dynamics}
142	\end{figure}
143	
144	Temperature $\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.
145	A mild loss increase in the final $\sim$100 steps is expected: as masks become more binary ($\tau \to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.
146	
147	The controller reliably drives actual sparsity to within 5\% of the target across all tested regimes, with $\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.
148	For the 30\% target, actual sparsity is $\approx$28.5\% (5\% deviation). This does not affect conclusions: TEAL at 28.5\% actual sparsity yields PPL 10.30 (vs.\ 10.97 at exact 30\%), a 0.67 PPL difference negligible relative to the KL vs.\ TEAL gap (8.96 vs.\ 10.97).
149	
150	
151	\section{Out-of-Distribution Evaluation}
152	\label{app:ood}
153	
154	To address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\cite{raffel2020c4} validation set under TEAL global allocation.
155	
156	\begin{table}[h]
157	\centering
158	\caption{Out-of-distribution evaluation on C4 validation (PPL$\downarrow$). 30\% KL reports 2-seed mean$\pm$std; other entries use seed 42.}
159	\label{tab:ood}
160	\small
161	\begin{tabular}{llc}
162	\toprule
163	Sparsity & Method & C4 PPL$\downarrow$ \\
164	\midrule
165	0\% & Dense & 9.21 \\
166	\midrule
167	30\% & KL predictor (Ours) & \textbf{16.03$\pm$0.01} \\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123
168	\midrule
169	\multirow{2}{*}{50\%} & KL predictor (Ours) & \textbf{18.40} \\ % exp_id: eval_c4_ood_kl50
170	& TEAL vanilla & 38.75 \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	At the 30\% sparsity level, the KL predictor achieves C4 PPL 16.03$\pm$0.01 (2-seed, global allocation, $1.74\times$ dense), confirming OOD generalization.
176	At 50\%, the KL predictor achieves 52.5\% relative advantage over TEAL (18.40 vs.\ 38.75), comparable to the 50\% advantage on WikiText-2 (11.92 vs.\ 23.90), confirming that KL-trained predictions generalize across distributions.
177	
178	\paragraph{Uniform Allocation.}
179	Under uniform allocation at 30\%, C4 PPL across three seeds is 18.22 (s42), 16.37 (s123), 16.36 (s456), yielding mean 16.98$\pm$1.07 ($1.84\times$ dense). % exp_id: c4_ood_kl30_uniform_3seed
180	The cross-seed variance is substantially higher than in-domain: CV=6.3\% on C4 vs.\ 0.2\% on WikiText-2 (PPL 8.81$\pm$0.02), driven by seed 42's elevated C4 PPL (18.22 vs.\ 16.37 for other seeds).
181	Global allocation's cross-layer budget flexibility partially compensates for domain shift (PPL 16.03 global vs.\ 16.98 uniform), consistent with the Limitations observation that the predictor partially overfits to training-domain activation patterns.
182	
183	\paragraph{Downstream Task Robustness.}
184	Table~\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\ WikiText (in-domain), both at 30\% uniform allocation (seed 42). All six benchmarks show $\Delta$$\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa
185	
186	\begin{table}[h]
187	\centering
188	\caption{Downstream task robustness to calibration domain shift (KL 30\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\_match (GSM8K).}
189	\label{tab:ood_downstream}
190	\small
191	\begin{tabular}{lcccccc}
192	\toprule
193	Calibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\
194	\midrule
195	WikiText & 40.8 & 68.6 & 40.6 & 7.4 & 70.9 & 74.8 \\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa
196	C4 (OOD) & 40.4 & 69.3 & 41.4 & 6.3 & 70.7 & 74.0 \\ % exp_id: c4_ood_downstream_kl30
197	\midrule
198	$\Delta$ & $-$0.4 & +0.7 & +0.8 & $-$1.1 & $-$0.2 & $-$0.8 \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	
204	\section{Per-Layer Retention Analysis}
205	\label{app:retention}
206	
207	\begin{figure}[h]
208	\centering
209	\includegraphics[width=\columnwidth]{per_layer_retention_chart.pdf}
210	\caption{Per-layer neuron retention under global top-$k$ allocation at 30\%, 50\%, and 70\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\% (L31) even at 30\% sparsity. At 70\%, starvation extends to mid-layers (L10--12: 16.7--20.1\%), explaining the transition to the capacity-limited regime.}
211	\label{fig:retention}
212	\end{figure}
213	
214	
215	\section{Training Stability}
216	\label{app:stability}
217	
218	Three-seed evaluation ($s \in \{42, 123, 456\}$) at 50\% sparsity under uniform allocation yields PPL $11.92 \pm 0.07$ (CV=0.6\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform
219	Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
220	
221	Under global allocation at 50\%, MMLU is $28.3 \pm 0.7$\%; the near-random performance is capacity-limited rather than seed-sensitive ($\sigma$=0.7pp vs.\ 9.5pp at 30\% global). % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval
222	The low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.
223	
224	\subsection{Cross-Seed Mask Consistency}
225	\label{app:cross_seed_jaccard}
226	
227	To assess whether KL predictors discover consistent mask patterns across initializations, we compute pairwise Jaccard distances among three independently trained KL predictors (s42/s123/s456) at 30\% uniform allocation (100 sequences, WikiText-2 validation). % exp_id: cross_seed_jaccard_kl30
228	
229	The mean cross-seed Jaccard distance is 0.363 (IoU = 0.637), substantially lower than the KL-vs-magnitude divergence (0.46--0.68), confirming that KL-discovered patterns form a distinct cluster from magnitude-based masks.
230	Per-layer divergence follows a U-shaped pattern: lowest at embedding-adjacent layers (L0: 0.33), peaking at early layers (L1: 0.41), with a mid-network valley (L12--14: 0.33). The random baseline Jaccard distance is 0.462.
231	
232	While specific mask configurations vary moderately across seeds (Jaccard distance 36.3\%), the resulting PPL is highly stable (8.81$\pm$0.02, CV=0.2\%), suggesting multiple near-equivalent optima in the activation mask space.
233	The cross-seed divergence (36.3\%) is substantially lower than the KL-vs-magnitude divergence (46--68\%), confirming that KL discovers effective patterns that cluster distinctly from magnitude-based selection.
234	
235	
236	\section{MSE Baseline Configuration}
237	\label{app:mse_config}
238	
239	The MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\times}10^{-3}$, weight decay $1{\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\tau$: $1.0 \to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.
240	The only difference is the loss target: per-layer $\|\mathbf{W}_d^{(\ell)}(\tilde{\mathbf{m}}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}) - \mathbf{y}_{\text{dense}}^{(\ell)}\|_2^2$, replacing the end-to-end KL divergence.
241	This controlled comparison isolates the effect of output-distribution alignment: all three predictors see identical data in identical order with identical architectures; only the loss function differs. % exp_id: mse30_uniform_s42, mse50_uniform_s42
242	
243	MSE uses $\lambda_{\max}{=}1000$ (vs.\ KL's 5000) because MSE's per-layer gradient magnitude is approximately $5\times$ larger than KL's end-to-end gradient, requiring proportionally less penalty pressure to achieve comparable sparsity control. Both reach their target sparsity within 110 steps.
244	At 50\% target, MSE converges to the target sparsity for seed 42; however, with seed 123, sparsity reaches only 5.1\% under the same $\lambda_{\max}$ cap (eval PPL$=$15{,}789, random-level), indicating high sensitivity to initialization---a failure mode not observed with KL-based losses.
245	At 30\%, MSE achieves 27.7\% actual sparsity for s42 (gap 2.3pp).
246	The 3-seed MSE mean (18.52$\pm$1.68; s42=20.43, s123=17.73, s456=17.39) is still $1.7\times$ worse than TEAL (10.82), confirming that the performance deficit stems from the loss function, not insufficient sparsity pressure.
247	
248	
249	\section{Extended SNR Analysis}
250	\label{app:snr_extended}
251	
252	Figure~\ref{fig:snr_trajectory} plots gradient SNR across the full 1000-step training for both KL and BCE predictors, measured at 14 checkpoints (LLaMA-3.1-8B, C4) with 95\% bootstrap confidence intervals.
253	From step 100 onward, BCE maintains consistently higher SNR than KL (2.3--17$\times$ depending on training phase), with the gap narrowing toward convergence ($2.3\times$ at step 1000: $2.026{\times}10^{-3}$ vs.\ $8.78{\times}10^{-4}$). % exp_id: snr_full_curve_1000steps
254	Despite KL's noisier gradient signal, KL-trained predictors produce substantially better masks (Table~\ref{tab:main}), confirming that \emph{target alignment} matters more than gradient clarity for mask quality.
255	BCE's higher SNR reflects its simpler per-neuron classification objective, which concentrates gradients on individual neuron decisions; KL's coupled gradient distributes signal across all mask decisions jointly, yielding lower SNR but discovering compositionally superior mask patterns (\S\ref{sec:method:gradient}).
256	
257	\begin{figure}[t]
258	\centering
259	\includegraphics[width=\columnwidth]{snr_trajectory.pdf}
260	\caption{Gradient SNR trajectory across 1000 training steps. BCE (orange) maintains consistently higher SNR than KL (blue) from step 100 onward (2.3--17$\times$), yet KL produces superior masks (Table~\ref{tab:main}), suggesting that target alignment matters more than gradient clarity for mask quality.}
261	\label{fig:snr_trajectory}
262	\end{figure}
263	
264	
265	\section{Extended Downstream Evaluation}
266	\label{app:downstream}
267	
268	Table~\ref{tab:downstream} reports HellaSwag and PIQA across sparsity levels and allocation strategies.
269	
270	\begin{table}[h]
271	\centering
272	\caption{Extended downstream benchmarks (LLaMA-3.1-8B). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc. KL 30\% uniform: 3-seed mean$\pm$std; others: seed 42.}
273	\label{tab:downstream}
274	\small
275	\begin{tabular}{llcc}
276	\toprule
277	Sparsity & Method & HellaSwag & PIQA \\
278	\midrule
279	0\% & Dense & \textbf{82.35} & \textbf{80.90} \\
280	\midrule
281	\multirow{3}{*}{30\%}
282	& KL uniform & \textbf{71.07$\pm$0.54} & \textbf{74.95$\pm$0.25} \\ % exp_id: hellaswag_piqa_kl30_uniform (3-seed)
283	& TEAL uniform & 63.31 & 72.80 \\ % exp_id: bench_teal30_uniform_6task
284	& BCE isocompute & 62.81 & 74.21 \\ % exp_id: bce_isocompute_30u_hellaswag_piqa
285	\midrule
286	\multirow{3}{*}{50\%}
287	& KL global & \textbf{58.95} & \textbf{69.48} \\ % exp_id: hellaswag_piqa_kl50_global
288	& KL uniform & 56.66 & 69.10 \\ % exp_id: hellaswag_piqa_kl50_uniform
289	& TEAL uniform & 39.35 & 63.66 \\ % exp_id: bench_teal50_uniform_6task
290	\bottomrule
291	\end{tabular}
292	\end{table}
293	
294	At 30\%, the KL predictor retains 86.3\% of dense HellaSwag accuracy (71.07$\pm$0.54 vs.\ 82.35, 3-seed) and 92.6\% of PIQA (74.95$\pm$0.25 vs.\ 80.90), confirming moderate degradation on non-reasoning tasks.
295	At 50\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\S\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).
296	
297	
298	\section{Compensation Training Convergence}
299	\label{app:comp_convergence}
300	
301	All compensation networks~\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\% s42 (final loss 0.70), 30\% s456 (0.68), 50\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42
302	
303	
304	\section{Qwen-2.5-14B Detailed Results}
305	\label{app:14b}
306	
307	\begin{table}[h]
308	\centering
309	\caption{Qwen-2.5-14B at 30\% nominal sparsity. Actual sparsity differs: KL 29.6\% (3-seed), TEAL 29.3\% (target 30\%). \textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\% native sparsity (\S\ref{sec:method:gradient}), so forced global top-$k$ is used.}
310	\label{tab:14b}
311	\small
312	\resizebox{\columnwidth}{!}{
313	\begin{tabular}{lcccccccc}
314	\toprule
315	Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\
316	\midrule
317	Dense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\
318	\midrule
319	\multicolumn{8}{l}{\emph{Global top-$k$ allocation}} \\
320	KL (Ours) & \textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \textbf{75.01} & \textbf{77.37} \\ % exp_id: qwen14b_kl30_s42
321	TEAL & 8.73 & 56.83 & \textbf{72.69} & \textbf{71.83} & 49.51 & 70.51 & 74.70 \\ % exp_id: qwen14b_teal30_eval
322	BCE & 8.76 & \textbf{57.59} & 72.61 & 71.67 & \textbf{53.07} & 53.43 & 68.28 \\ % exp_id: qwen14b_bce30_s42_eval
323	\midrule
324	\multicolumn{8}{l}{\emph{Uniform allocation}} \\
325	KL (Ours) & \textbf{7.90} & 53.50 & \textbf{72.82} & 63.55 & 32.2$\pm$5.3 & \textbf{72.68$\pm$0.2} & \textbf{76.01$\pm$1.1} \\ % exp_id: qwen14b_kl30_uniform (3-seed s42/s123(v4)/s456)
326	TEAL & 8.01 & \textbf{55.29} & 69.85 & \textbf{66.34} & \textbf{52.1} & 67.72 & 74.70 \\ % exp_id: qwen14b_teal30_uniform
327	\bottomrule
328	\multicolumn{8}{l}{\footnotesize GSM8K: 3-seed (s42/s123(v4)/s456).} \\
329	\end{tabular}}
330	\end{table}
331	
332	Under global allocation, BCE's HellaSwag drops to 53.43\% ($-$17pp vs.\ TEAL), indicating that the magnitude-based predictor's mask quality degrades severely when combined with non-uniform budget distribution at 14B scale. % exp_id: qwen14b_bce30_s42_eval, qwen14b_teal30_eval
333	
334	\section{Full Allocation Analysis}
335	\label{app:alloc_full}
336	
337	\begin{table}[t]
338	\centering
339	\caption{Allocation summary (LLaMA-3.1-8B). $\pm$: 3-seed; $^\ast$high seed variance.}
340	\label{tab:phase}
341	\footnotesize
342	\begin{tabular}{llcc}
343	\toprule
344	Sparsity & Allocation & PPL$\downarrow$ & MMLU \\
345	\midrule
346	\multirow{2}{*}{30\%}
347	& Global & 8.96$\pm$0.02 & 35.7$\pm$9.5$^\ast$ \\ % exp_id: kl30_3seed_global
348	& Uniform & \textbf{8.81$\pm$0.02} & \textbf{40.7$\pm$1.3} \\ % exp_id: bench_kl30_uniform
349	\midrule
350	\multirow{2}{*}{50\%}
351	& Global & \textbf{11.84$\pm$0.15} & \textbf{28.3$\pm$0.7} \\ % exp_id: bench_kl50_global, kl50_global_s123_reeval, kl50_global_s123_downstream_v2, kl50_global_s456_eval
352	& Uniform & 11.92$\pm$0.07 & 28.0$\pm$0.6 \\ % exp_id: multi_seed_kl50_uniform
353	\bottomrule
354	\end{tabular}
355	\end{table}
356	
357	Table~\ref{tab:phase_full} extends Table~\ref{tab:phase} with all downstream metrics.
358	
359	\begin{table*}[t]
360	\centering
361	\caption{Full allocation analysis: global top-$k$ vs.\ uniform across sparsity levels (LLaMA-3.1-8B). Entries with $\pm$: 3-seed mean$\pm$std ($s \in \{42, 123, 456\}$); others: seed 42. $^\ast$High MMLU seed variance (individual seeds span 25.3--43.5\%).}
362	\label{tab:phase_full}
363	\begin{tabular}{llccccc}
364	\toprule
365	Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
366	\midrule
367	\multirow{2}{*}{25\%}
368	& Global & \textbf{8.17} & 45.4 & 70.6 & \textbf{46.6} & \textbf{11.5} \\
369	& Uniform & 8.23 & \textbf{46.5} & \textbf{71.8} & 44.0 & 11.0 \\
370	\midrule
371	\multirow{2}{*}{30\%}
372	& Global & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5$^\ast$ & \textbf{8.0$\pm$0.7} \\
373	& Uniform & \textbf{8.81$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & \textbf{40.7$\pm$1.3} & 7.5$\pm$0.1 \\
374	\midrule
375	\multirow{2}{*}{35\%}
376	& Global & \textbf{9.31} & \textbf{38.9} & \textbf{67.6} & \textbf{40.4} & \textbf{7.7} \\
377	& Uniform & 9.44 & 38.7 & 66.5 & 37.8 & 4.3 \\
378	\midrule
379	\multirow{2}{*}{40\%}
380	& Global & \textbf{10.14} & 39.5 & \textbf{67.5} & \textbf{39.5} & \textbf{6.6} \\
381	& Uniform & 10.76 & \textbf{39.6} & 63.1 & 35.5 & 3.6 \\
382	\midrule
383	\multirow{2}{*}{45\%}
384	& Global & \textbf{10.80} & \textbf{39.2} & \textbf{64.6} & 30.4 & \textbf{3.0} \\
385	& Uniform & 10.95 & 37.6 & 63.6 & \textbf{30.6} & 2.7 \\
386	\midrule
387	\multirow{2}{*}{50\%}
388	& Global & \textbf{11.84$\pm$0.15} & \textbf{36.3$\pm$3.2} & \textbf{63.8$\pm$0.3} & \textbf{28.3$\pm$0.7} & \textbf{2.7$\pm$1.3} \\
389	& Uniform & 11.92$\pm$0.07 & 33.8$\pm$1.2 & 62.9$\pm$0.1 & 28.0$\pm$0.6 & 2.2$\pm$0.1 \\
390	\bottomrule
391	\end{tabular}
392	\end{table*}
393	
394	
395	\section{Mask Pattern Visualization}
396	\label{app:mask_viz}
397	
398	Figure~\ref{fig:mask_heatmap} shows per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\% and 50\% sparsity.
399	Figure~\ref{fig:scatter} shows per-neuron importance scores at layer 16.
400	Figure~\ref{fig:mask_comparison} shows binary mask comparisons at layers 2, 16, and 28.
401	
402	\begin{figure}[t]
403	\centering
404	\includegraphics[width=0.95\columnwidth]{neuron_scatter_layer16.pdf}
405	\caption{KL vs.\ magnitude importance scores for layer 16 neurons at 50\% sparsity. 41\% of neurons fall in disagreement quadrants where one method selects a neuron the other discards.}
406	\label{fig:scatter}
407	\end{figure}
408	
409	\begin{figure*}[t]
410	\centering
411	\includegraphics[width=\textwidth]{mask_divergence_heatmap.pdf}
412	\caption{Per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\% and 50\% sparsity (64 samples, 131K tokens). Divergence peaks in layers 24--28 (Jaccard distance $>$0.73 at 50\%) and increases with sparsity across all layers.}
413	\label{fig:mask_heatmap}
414	\end{figure*}
415	
416	\begin{figure*}[t]
417	\centering
418	\includegraphics[width=\textwidth]{mask_comparison.pdf}
419	\caption{Binary mask comparison between KL-derived and magnitude-based masks at selected layers (L2, L16, L28) for 30\% and 50\% sparsity (64 samples). Black = selected by both, light regions = selected by only one method. Deep layers show the largest divergence (L28 Jaccard distance: 0.60 at 30\%, 0.74 at 50\%).}
420	\label{fig:mask_comparison}
421	\end{figure*}
422	
423	
424	\section{Cross-Architecture Comparison}
425	\label{app:cross_arch}
426	
427	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
428	
429	\begin{table}[h]
430	\centering
431	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. \textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\%: 3-seed mean$\pm$std; other rows: seed 42.}
432	\label{tab:cross_arch}
433	\small
434	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
435	\toprule
436	 & \multicolumn{3}{c}{Mistral-7B} & \multicolumn{3}{c}{LLaMA-8B} \\
437	 & KL & TEAL & Adv & KL & TEAL & Adv \\
438	\midrule
439	30\% & \textbf{6.93$\pm$0.19} & 8.38 & 1.21$\times$ & \textbf{8.96} & 10.97 & 1.22$\times$ \\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, teal_30_mistral, kl30_3seed_global
440	50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
441	70\% & \textbf{13.33} & 61.72 & 4.63$\times$ & \textbf{17.91} & 100.11 & 5.59$\times$ \\ % exp_id: kl_70_mistral, teal_70_mistral
442	\bottomrule
443	\end{tabular}
444	\end{table}
445	
446	The KL PPL advantage ratio is consistent across architectures (within 8\% at $\leq$50\% sparsity).
447	Table~\ref{tab:mistral_downstream} reports downstream task accuracy at 30\% sparsity on Mistral-7B-v0.3 (3-seed). KL improves PPL ($-$17.3\%) and commonsense tasks (WG +6.7pp) but MMLU is tied (43.3\% vs.\ 43.5\%); ARC-c shows high seed variance ($\sigma$=6.4pp); GSM8K reverses.
448	
449	\begin{table}[h]
450	\centering
451	\caption{Mistral-7B-v0.3 downstream evaluation at 30\% sparsity. $\pm$: 3-seed mean$\pm$std ($s \in \{42, 123, 456\}$); TEAL is deterministic (single run). ARC-c exhibits high seed variance ($\sigma$=6.4pp).}
452	\label{tab:mistral_downstream}
453	\small
454	\resizebox{\columnwidth}{!}{
455	\begin{tabular}{lccccccc}
456	\toprule
457	Method & PPL$\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\
458	\midrule
459	Dense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa
460	KL 30\% & \textbf{6.93$\pm$0.19} & \textbf{44.9$\pm$6.4} & \textbf{70.2$\pm$1.2} & \textbf{69.7$\pm$0.8} & \textbf{74.8$\pm$0.4} & 43.3$\pm$1.5 & 8.6$\pm$2.2 \\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456
461	TEAL 30\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & \textbf{43.5} & \textbf{15.9} \\ % exp_id: mistral_teal30_downstream
462	\bottomrule
463	\end{tabular}}
464	\end{table}
465	
466	
467	\section{Taxonomy Discussion}
468	\label{app:taxonomy}
469	
470	\paragraph{Correction granularity.}
471	\emph{Static} methods~\cite{xu2025spon} learn a fixed bias vector per layer that does not depend on the input token.
472	\emph{Per-token} methods~\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.
473	
474	\paragraph{Training signal coupling.}
475	\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.
476	\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.
477	\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass; each mask decision's gradient reflects its joint effect with all other masks on the final distribution.
478	
479	SPON~\cite{xu2025spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\times$ coupled).
480	DejaVu~\cite{liu2023dejavu} and FastForward~\cite{gautam2026fastforward} achieve per-token granularity but use BCE, where each neuron's gradient is independent of other mask states.
481	D2DMoE~\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.
482	We define \emph{output-distribution alignment} as whether the training loss optimizes a quantity that composes across layers.
483	KL on output logits directly optimizes next-token prediction loss, which does not suffer from error composition; per-layer MSE minimizes reconstruction error independently at each layer, but layer-wise optima do not compose---a mask minimizing FFN output error at layer $\ell$ may amplify errors in layers $\ell{+}1 \ldots L$.
484	The SNR analysis (\S\ref{sec:method:gradient}) corroborates this: KL achieves the best masks despite $2.3\times$ lower SNR than BCE, while MSE produces the worst masks.
485	The framework predicts that losses operating on output-level quantities should outperform intermediate-level losses, a hypothesis consistent with our MSE results and testable with alternative output-level objectives.
486	
487	\section{Oracle Mask Provenance}
488	\label{app:oracle_provenance}
489	
490	C1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold (logits $> 0$, equivalent to $\sigma > 0.5$); they reflect one specific training trajectory (optimizer state, data order, Gumbel noise).
491	The s42/s123/s456 consistency ($\leq$1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.
492	
493	\section{SPON Orthogonality}
494	\label{app:spon}
495	
496	SPON~\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\% PPL improvement (12.08$\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
497	The decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.
498	
499	\section{Per-Layer KL Downstream Decomposition}
500	\label{app:perlayer_downstream}
501	
502	Table~\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\ coupling scope decomposition at 30\% sparsity (\S\ref{sec:perlayer}). BoolQ's $\approx$100\% coupling is an upper bound confounded by high cross-seed variance ($\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.
503	
504	\begin{table}[h]
505	\centering
506	\caption{2D decomposition at 30\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \S\ref{sec:perlayer}).}
507	\label{tab:perlayer_downstream}
508	\resizebox{\columnwidth}{!}{
509	\begin{tabular}{lcccccc}
510	\toprule
511	& PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & BoolQ \\
512	\midrule
513	E2E KL & 8.81$\pm$0.02 & 43.7 & 68.9 & 40.7 & 7.5 & 73.7 \\
514	Per-layer KL & 9.05$\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & 64.5 \\
515	MSE & 18.52$\pm$1.68 & 35.8$\pm$4.1 & 59.8$\pm$2.6 & 30.7$\pm$2.6 & 2.3$\pm$0.7 & 64.5$\pm$5.3 \\
516	\midrule
517	Total gap & 9.71 & 7.9 & 9.1 & 10.0 & 5.2 & 9.2 \\
518	Signal type (\%) & 97.5 & 51.9 & 67.0 & 79.0 & 67.3 & $\approx$0 \\
519	Coupling (\%) & 2.5 & 48.1 & 33.0 & 21.0 & 32.7 & $\approx$100 \\
520	\bottomrule
521	\end{tabular}}
522	\end{table}
523	
524	\section{$K{=}4$ Mismatch Control}
525	\label{app:k4_downstream}
526	
527	Table~\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\% sparsity.
528	Training with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\ 1/32 layers masked during training, while inference applies all 32).
529	The gap closure column reports the fraction of the $K{=}1 \to$ E2E KL gap closed by $K{=}4$.
530	
531	\begin{table}[h]
532	\centering
533	\caption{3-seed $K{=}4$ mismatch control at 30\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \in \{42, 123, 456\}$). Actual sparsity 29.6\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\text{E2E} - K{=}1) \times 100$.}
534	\label{tab:k4_downstream}
535	\resizebox{\columnwidth}{!}{
536	\begin{tabular}{lcccc}
537	\toprule
538	& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\%) \\
539	\midrule
540	PPL$\downarrow$ & 8.89$\pm$0.01 & 9.05$\pm$0.02 & 8.81$\pm$0.02 & 66.7 \\
541	ARC-c & 40.0$\pm$1.3 & 39.9 & 43.7$\pm$2.5 & 2.6 \\
542	WG & 66.9$\pm$0.2 & 65.9 & 68.9$\pm$0.4 & 33.3 \\
543	MMLU$^\ast$ & 42.7$\pm$1.4 & 38.6 & 40.7$\pm$1.3 & $>$100 \\
544	GSM8K & 7.0$\pm$1.6 & 5.8 & 7.5$\pm$0.1 & 70.6 \\
545	BoolQ$^\dagger$ & 67.7$\pm$7.5 & 64.5$\pm$11.5 & 73.7 & 34.8 \\
546	\bottomrule
547	\end{tabular}}
548	\vspace{2pt}
549	{\footnotesize $^\ast$MMLU $K{=}4$ systematically exceeds E2E across all 3 seeds; attributable to $K{=}4$'s near-uniform per-layer sparsity (std=0.003) matching uniform eval allocation. Independently confirmed: removing the predictor's middle-layer valley yields MMLU=44.0\% (Appendix~\ref{app:constraint}).
550	$^\dagger$BoolQ exhibits high inter-seed variance for both $K{=}4$ (std=7.5) and $K{=}1$ (std=11.5); gap closure unreliable.}
551	\end{table}
552	
553	\section{Per-Layer Sparsity Constraint Analysis}
554	\label{app:constraint}
555	
556	To test the causal role of the KL predictor's learned per-layer allocation, we evaluate two inference-time interventions at 30\% overall sparsity (seed 42, uniform allocation baseline):
557	
558	\begin{table}[h]
559	\centering
560	\caption{Per-layer sparsity constraint analysis. \emph{Protect late}: cap L22--L28 sparsity $\leq$30\%; \emph{Remove valley}: override L14--L18 sparsity to 30\%. Budget redistributed to maintain 30\% overall.}
561	\label{tab:constraint}
562	\begin{tabular}{lcccc}
563	\toprule
564	Condition & PPL & ARC-c & MMLU & GSM8K \\
565	\midrule
566	KL baseline (s42) & 8.82 & 40.8 & 40.6 & 7.4 \\
567	Protect late layers & 9.26 & 42.4 & 40.7 & 6.5 \\
568	Remove valley & 8.76 & 39.3 & 44.0 & 9.0 \\
569	\bottomrule
570	\end{tabular}
571	\end{table}
572	
573	Protecting late layers (L22--L28) does not improve knowledge-intensive metrics despite reducing their sparsity from 48--57\% to $\leq$30\%, while worsening PPL by 5.2\%.
574	Conversely, removing the protection valley (forcing L14--L18 to 30\% instead of 14--18\%) improves MMLU by +3.4pp and GSM8K by +1.6pp at the cost of ARC-c $-$1.5pp.
575	The KL predictor's learned allocation thus represents a task-dependent trade-off---prioritizing commonsense reasoning via middle-layer protection---rather than a uniformly optimal pattern.
576	This allocation trade-off also explains the $K{=}4$ MMLU anomaly (\S\ref{app:k4_downstream}): $K{=}4$'s near-uniform learned sparsity (std=0.003) inherently removes the valley, producing MMLU=43.5 comparable to the remove-valley condition (44.0).
577	
578	\section{Per-Layer Sparsity Distribution}
579	\label{app:perlayer_sparsity}
580	
581	The KL predictor at 30\% target sparsity learns a non-uniform per-layer allocation that differs markedly from magnitude-based selection.
582	Aggregate sparsity is similar across broad regions (early L0--L7: KL 28.1\% vs.\ magnitude 27.5\%; late L24--L31: 44.9\% vs.\ 47.2\%), but middle layers (L8--L23) exhibit high internal variance despite similar averages (28.2\% vs.\ 27.3\%).
583	Table~\ref{tab:perlayer_sparsity} highlights three sub-ranges.
584	
585	\begin{table}[h]
586	\centering
587	\caption{Per-layer sparsity sub-ranges: KL predictor vs.\ magnitude (LLaMA-3.1-8B, 30\%, uniform allocation). Ranges denote min--max across layers in each group.}
588	\label{tab:perlayer_sparsity}
589	\begin{tabular}{lccc}
590	\toprule
591	Layer Range & KL (\%) & Mag (\%) & $\Delta$ (pp) \\
592	\midrule
593	L8--L12 (high pruning) & 32--36 & 25--26 & $+$7 to $+$10 \\
594	L14--L18 (protection valley) & 14--18 & 28--30 & $-$8 to $-$16 \\
595	L22--L28 (aggressive pruning) & 48--57 & --- & --- \\
596	\bottomrule
597	\end{tabular}
598	\end{table}
599	
600	\section{C4 Training Data Control}
601	\label{app:c4_control}
602	
603	To test whether WikiText-103's narrow domain drives the knowledge-task regression (\S\ref{sec:experiments}), we train the KL predictor on C4~\cite{raffel2020c4} (diverse web text) under identical hyperparameters (1000 steps, 30\% uniform, s42).
604	
605	\begin{table}[h]
606	\centering
607	\caption{C4-trained vs.\ WikiText-trained KL predictor (LLaMA-3.1-8B, 30\% uniform, s42).}
608	\label{tab:c4_control}
609	\resizebox{\columnwidth}{!}{
610	\begin{tabular}{lcccccc}
611	\toprule
612	Training Data & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\
613	\midrule
614	WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa
615	C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\ % exp_id: c4_kl30_s42_eval
616	\bottomrule
617	\end{tabular}}
618	\end{table}
619	
620	The C4-trained predictor achieves comparable MMLU (40.0\% vs.\ 40.6\%) but worse GSM8K (4.1\% vs.\ 7.4\%) and higher PPL (11.55 vs.\ 8.82), despite training on more diverse text.
621	This rules out training data composition as the primary cause of knowledge-task regression and supports the hypothesis that forward KL's mode-covering property structurally under-protects rare reasoning-critical activations. % exp_id: c4_control_eval
622	
623	\section{Per-Layer Coupling Breadth Analysis}
624	\label{app:k_curve}
625	
626	We vary the number of layers coupled per training step ($K$) from 1 (pure per-layer) to 32 (end-to-end), evaluating all predictors under TEAL uniform allocation at 30\% sparsity on LLaMA-3.1-8B.
627	
628	\begin{table}[h]
629	\centering
630	\caption{K-curve: coupling breadth vs.\ predictor quality (30\%, TEAL uniform, LLaMA-3.1-8B). All values are 3-seed mean$\pm$std (s42/s123/s456) except $K{=}1$ downstream (single seed). ``---'' = not evaluated.}
631	\label{tab:k_curve}
632	\resizebox{\columnwidth}{!}{
633	\begin{tabular}{cccccccc}
634	\toprule
635	$K$ & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\
636	\midrule
637	1 & 9.05$\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & --- & --- \\
638	2 & 10.75$\pm$0.15 & 39.7$\pm$1.2 & 63.2$\pm$1.7 & 38.3$\pm$3.2 & 2.8$\pm$0.6 & 66.5$\pm$1.0 & 73.5$\pm$0.7 \\
639	4 & 8.89$\pm$0.01 & 40.0$\pm$1.2 & 66.9$\pm$0.2 & 42.7$\pm$1.4 & 7.0$\pm$1.6 & 67.8$\pm$1.0 & 74.5$\pm$0.5 \\
640	8 & 9.00$\pm$0.06 & 40.7$\pm$1.0 & 68.7$\pm$1.3 & 40.4$\pm$0.6 & 6.8$\pm$1.3 & 69.0$\pm$1.1 & 75.1$\pm$1.1 \\
641	16 & 8.67$\pm$0.02 & 41.9$\pm$1.1 & 68.5$\pm$0.9 & 40.9$\pm$2.9 & 8.5$\pm$1.2 & 70.1$\pm$0.4 & 75.0$\pm$0.8 \\
642	32 (E2E) & 8.81$\pm$0.02 & 43.7$\pm$2.5 & 68.9$\pm$0.4 & 40.7$\pm$1.3 & 7.5$\pm$0.1 & --- & --- \\
643	\bottomrule
644	\end{tabular}}
645	\end{table}
646	
647	PPL exhibits a non-monotonic U-shape (Figure~\ref{fig:k_curve_ppl}): $K{=}2$ is worst (10.75$\pm$0.15), likely due to insufficient per-layer updates (${\sim}$62 updates/layer vs.\ ${\sim}$250 at $K{=}8$). $K{=}16$ achieves the lowest PPL (8.67$\pm$0.02), marginally better than E2E (8.81$\pm$0.02). $K{=}16$ MMLU exhibits high seed variance (std=2.9; s42=44.0, s123=40.0, s456=38.7), with the 3-seed mean (40.9) indistinguishable from E2E (40.7$\pm$1.3).
648	The signal type gap ($K{=}1$ KL 9.05 vs.\ per-layer MSE 18.52$\pm$1.68) of 9.47 PPL exceeds the coupling breadth range within KL (best $K{=}16$ 8.67 vs.\ worst $K{=}2$ 10.75 = 2.08 PPL), reinforcing that output-distribution alignment, not coupling scope, is the primary quality lever for PPL at this sparsity level. % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed, perlayer_kl_30_3seed, perlayer_kl_k4_3seed
649	
650	\section{Licenses}
651	\label{app:licenses}
652	
653	LLaMA-3.1-8B is released under the Llama 3.1 Community License Agreement.
654	Mistral-7B-v0.3 is released under the Apache 2.0 License.
655	Qwen-2.5-14B is released under the Apache 2.0 License.
656	WikiText-103 and WikiText-2~\cite{merity2017pointer} are released under the Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0).
657	All evaluation benchmarks (ARC, WinoGrande, MMLU, GSM8K, HellaSwag, PIQA) are publicly available under their respective licenses.
658	Our code will be released under the MIT License upon acceptance.
659	
660	\section{Use of AI Assistants}
661	\label{app:ai-assistants}
662	
663	We used Claude (Anthropic) as an AI coding and writing assistant
664	throughout this work. Specifically:
665	\begin{itemize}
666	    \item \textbf{Code:} drafting experiment scripts, data-processing
667	    pipelines, and analysis utilities; debugging and refactoring.
668	    \item \textbf{Writing:} drafting and revising paper sections,
669	    polishing prose, and reformatting LaTeX.
670	    \item \textbf{Literature:} summarizing related papers to inform
671	    related-work section.
672	\end{itemize}
673	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9208c074-8482-44db-ae8d-4d1e3040d45b",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "045c8dda-cc00-4e2a-85ff-d4163b02b467",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Inference Efficiency}\n\\label{app:latency}\n\nTable~\\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Sparsity & ms/fwd & tok/s & Overhead \\\\\n\\midrule\nDense & 0\\% & 119.11$\\pm$0.57 & 17{,}195 & --- \\\\\n\\midrule\nKL predictor-only & 30\\% & 126.64$\\pm$0.70 & 16{,}172 & +6.3\\% \\\\ % exp_id: latency_bench\nKL predictor-only & 50\\% & 126.78$\\pm$0.31 & 16{,}154 & +6.4\\% \\\\ % exp_id: latency_bench\n\\midrule\nPredictor + compensation & 30\\% & 129.94$\\pm$0.75 & 15{,}761 & +9.1\\% \\\\ % exp_id: latency_bench\nPredictor + compensation & 50\\% & 129.71$\\pm$0.53 & 15{,}789 & +8.9\\% \\\\ % exp_id: latency_bench\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full KL-sparse pipeline adds 6.4\\% overhead to dense inference (126.78 vs.\\ 119.11\\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\\,ms (2.7\\%); the remainder arises from mask application and sparse FFN indexing.\nEliminating the compensation network saves an additional $\\sim$2.7\\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.\nThe overhead is near-identical at 30\\% and 50\\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.\n\nNote that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.\nThe pipeline adds $\\sim$6.4\\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.\nOur contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.\n\n\n\\section{Predictor Bottleneck Sensitivity}\n\\label{app:db_sensitivity}\n\nTable~\\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Predictor bottleneck sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}\n\\label{tab:db_sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$d_b$ & Params & TEAL global & $\\Delta$ & Per-token \\\\\n\\midrule\n64 & 38.2M (0.48\\%) & 12.076 & +0.9\\% & 10.16 \\\\ % exp_id: db_sensitivity_sweep\n128 & 75.9M (0.95\\%) & 11.963 & --- & 9.218 \\\\ % exp_id: db_sensitivity_sweep\n256 & 151.5M (1.89\\%) & 12.105 & +1.2\\% & 8.586 \\\\ % exp_id: db_sensitivity_sweep\n512 & 302.5M (3.77\\%) & 12.315 & +2.9\\% & 7.93 \\\\ % exp_id: db_sensitivity_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\\to$7.93).\nThis divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.\nThe $d_b{=}128$ configuration (75.9M params, $<$1\\% of base model) is therefore optimal for the TEAL inference protocol.\n\n\\subsection{Temperature Schedule Sensitivity}\n\\label{app:tau_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature schedule sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:tau_sensitivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n$\\tau$ Schedule & PPL$\\downarrow$ \\\\\n\\midrule\nFixed $\\tau{=}0.5$ & \\textbf{11.861} \\\\ % exp_id: tau_schedule_sweep\nLinear $1.0 \\to 0.1$ (default) & 11.963 \\\\ % exp_id: tau_schedule_sweep\nFixed $\\tau{=}0.1$ & 12.072 \\\\ % exp_id: tau_schedule_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature schedule has minimal impact ($<$1.8\\% PPL variation).\nThe linear annealing default is a conservative choice; even removing annealing entirely (fixed $\\tau{=}0.5$) yields comparable performance.\n\n\\subsection{Training Convergence}\n\\label{app:training_convergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training convergence at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:training_convergence}\n\\small\n\\begin{tabular}{cc}\n\\toprule\nSteps & PPL$\\downarrow$ \\\\\n\\midrule\n200 & 15.158 \\\\ % exp_id: training_steps_sweep\n400 & 12.538 \\\\ % exp_id: training_steps_sweep\n600 & 12.046 \\\\ % exp_id: training_steps_sweep\n800 & 11.907 \\\\ % exp_id: training_steps_sweep\n1000 & \\textbf{11.906} \\\\ % exp_id: training_steps_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining converges rapidly: 95\\% of the quality gap closes by step 600, and performance saturates by step 800 ($\\Delta < 0.001$ between 800 and 1000 steps).\nOur default of 1000 steps provides a conservative margin.\n\n\n\\section{Geometric Penalty Schedule Dynamics}\n\\label{app:lagrangian}\n\nTable~\\ref{tab:lagrangian} reports the convergence of the geometric penalty schedule across sparsity targets.\nThe geometric doubling pattern ($1 \\to 2 \\to 4 \\to 8 \\to \\ldots$) enables $\\lambda$ to reach steady state within $\\sim$10 steps; the deadzone ($\\epsilon = 0.02$) then stabilizes $\\lambda$ once actual sparsity is within $\\pm$2\\% of the target.\n\n\\begin{table}[h]\n\\centering\n\\caption{Geometric penalty schedule convergence across sparsity targets (margin $\\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}\n\\label{tab:lagrangian}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTarget $\\rho$ & $\\lambda_{\\max}$ & Final $\\lambda$ & Actual sparsity & Deviation \\\\\n\\midrule\n30\\% & 5000 & 5000 (cap) & 0.285 & 5.0\\% \\\\ % exp_id: kl_30pct_s42\n40\\% & 5000 & 625 & 0.398 & 0.5\\% \\\\ % exp_id: kl_40pct_s42\n50\\% & 1000 & 8 & 0.504 & 0.8\\% \\\\ % exp_id: kl_50pct_s42\n70\\% & 1000 & 1000 (cap) & 0.688 & 1.7\\% \\\\ % exp_id: kl_70pct_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 50\\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.\nAt 30\\% and 70\\%, the gap between the gate prior and target is larger, driving $\\lambda$ to its respective caps.\nThe 40\\% target converges to $\\lambda = 625$ with only 0.5\\% deviation; this precision reflects a regime where the target is reachable without $\\lambda$ saturation.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{lagrangian_dynamics.pdf}\n\\caption{Lagrangian controller dynamics for 30\\% sparsity target ($\\lambda_{\\max}=5000$). Left axis (log scale): penalty weight $\\lambda$ rises from $0.01$ to its cap once actual sparsity undershoots the target at $\\sim$step~150, exhibiting bang-bang oscillations before saturating. Right axis: actual sparsity (solid) converges from the natural density ($\\approx$0.41) toward the target (dashed) and stabilizes near 0.28.}\n\\label{fig:lagrangian_dynamics}\n\\end{figure}\n\nTemperature $\\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.\nA mild loss increase in the final $\\sim$100 steps is expected: as masks become more binary ($\\tau \\to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.\n\nThe controller reliably drives actual sparsity to within 5\\% of the target across all tested regimes, with $\\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.\nFor the 30\\% target, actual sparsity is $\\approx$28.5\\% (5\\% deviation). This does not affect conclusions: TEAL at 28.5\\% actual sparsity yields PPL 10.30 (vs.\\ 10.97 at exact 30\\%), a 0.67 PPL difference negligible relative to the KL vs.\\ TEAL gap (8.96 vs.\\ 10.97).\n\n\n\\section{Out-of-Distribution Evaluation}\n\\label{app:ood}\n\nTo address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\\cite{raffel2020c4} validation set under TEAL global allocation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Out-of-distribution evaluation on C4 validation (PPL$\\downarrow$). 30\\% KL reports 2-seed mean$\\pm$std; other entries use seed 42.}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{llc}\n\\toprule\nSparsity & Method & C4 PPL$\\downarrow$ \\\\\n\\midrule\n0\\% & Dense & 9.21 \\\\\n\\midrule\n30\\% & KL predictor (Ours) & \\textbf{16.03$\\pm$0.01} \\\\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123\n\\midrule\n\\multirow{2}{*}{50\\%} & KL predictor (Ours) & \\textbf{18.40} \\\\ % exp_id: eval_c4_ood_kl50\n& TEAL vanilla & 38.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the 30\\% sparsity level, the KL predictor achieves C4 PPL 16.03$\\pm$0.01 (2-seed, global allocation, $1.74\\times$ dense), confirming OOD generalization.\nAt 50\\%, the KL predictor achieves 52.5\\% relative advantage over TEAL (18.40 vs.\\ 38.75), comparable to the 50\\% advantage on WikiText-2 (11.92 vs.\\ 23.90), confirming that KL-trained predictions generalize across distributions.\n\n\\paragraph{Uniform Allocation.}\nUnder uniform allocation at 30\\%, C4 PPL across three seeds is 18.22 (s42), 16.37 (s123), 16.36 (s456), yielding mean 16.98$\\pm$1.07 ($1.84\\times$ dense). % exp_id: c4_ood_kl30_uniform_3seed\nThe cross-seed variance is substantially higher than in-domain: CV=6.3\\% on C4 vs.\\ 0.2\\% on WikiText-2 (PPL 8.81$\\pm$0.02), driven by seed 42's elevated C4 PPL (18.22 vs.\\ 16.37 for other seeds).\nGlobal allocation's cross-layer budget flexibility partially compensates for domain shift (PPL 16.03 global vs.\\ 16.98 uniform), consistent with the Limitations observation that the predictor partially overfits to training-domain activation patterns.\n\n\\paragraph{Downstream Task Robustness.}\nTable~\\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\\ WikiText (in-domain), both at 30\\% uniform allocation (seed 42). All six benchmarks show $\\Delta$$\\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream task robustness to calibration domain shift (KL 30\\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\\_match (GSM8K).}\n\\label{tab:ood_downstream}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nCalibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nWikiText & 40.8 & 68.6 & 40.6 & 7.4 & 70.9 & 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 (OOD) & 40.4 & 69.3 & 41.4 & 6.3 & 70.7 & 74.0 \\\\ % exp_id: c4_ood_downstream_kl30\n\\midrule\n$\\Delta$ & $-$0.4 & +0.7 & +0.8 & $-$1.1 & $-$0.2 & $-$0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Layer Retention Analysis}\n\\label{app:retention}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{per_layer_retention_chart.pdf}\n\\caption{Per-layer neuron retention under global top-$k$ allocation at 30\\%, 50\\%, and 70\\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\\% (L31) even at 30\\% sparsity. At 70\\%, starvation extends to mid-layers (L10--12: 16.7--20.1\\%), explaining the transition to the capacity-limited regime.}\n\\label{fig:retention}\n\\end{figure}\n\n\n\\section{Training Stability}\n\\label{app:stability}\n\nThree-seed evaluation ($s \\in \\{42, 123, 456\\}$) at 50\\% sparsity under uniform allocation yields PPL $11.92 \\pm 0.07$ (CV=0.6\\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform\nDownstream metrics are similarly stable: ARC-c $33.8 \\pm 1.2$\\%, WinoGrande $62.9 \\pm 0.1$\\%, MMLU $28.0 \\pm 0.6$\\%, GSM8K $2.2 \\pm 0.1$\\%.\n\nUnder global allocation at 50\\%, MMLU is $28.3 \\pm 0.7$\\%; the near-random performance is capacity-limited rather than seed-sensitive ($\\sigma$=0.7pp vs.\\ 9.5pp at 30\\% global). % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\nThe low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.\n\n\\subsection{Cross-Seed Mask Consistency}\n\\label{app:cross_seed_jaccard}\n\nTo assess whether KL predictors discover consistent mask patterns across initializations, we compute pairwise Jaccard distances among three independently trained KL predictors (s42/s123/s456) at 30\\% uniform allocation (100 sequences, WikiText-2 validation). % exp_id: cross_seed_jaccard_kl30\n\nThe mean cross-seed Jaccard distance is 0.363 (IoU = 0.637), substantially lower than the KL-vs-magnitude divergence (0.46--0.68), confirming that KL-discovered patterns form a distinct cluster from magnitude-based masks.\nPer-layer divergence follows a U-shaped pattern: lowest at embedding-adjacent layers (L0: 0.33), peaking at early layers (L1: 0.41), with a mid-network valley (L12--14: 0.33). The random baseline Jaccard distance is 0.462.\n\nWhile specific mask configurations vary moderately across seeds (Jaccard distance 36.3\\%), the resulting PPL is highly stable (8.81$\\pm$0.02, CV=0.2\\%), suggesting multiple near-equivalent optima in the activation mask space.\nThe cross-seed divergence (36.3\\%) is substantially lower than the KL-vs-magnitude divergence (46--68\\%), confirming that KL discovers effective patterns that cluster distinctly from magnitude-based selection.\n\n\n\\section{MSE Baseline Configuration}\n\\label{app:mse_config}\n\nThe MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\\times}10^{-3}$, weight decay $1{\\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\\tau$: $1.0 \\to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.\nThe only difference is the loss target: per-layer $\\|\\mathbf{W}_d^{(\\ell)}(\\tilde{\\mathbf{m}}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}) - \\mathbf{y}_{\\text{dense}}^{(\\ell)}\\|_2^2$, replacing the end-to-end KL divergence.\nThis controlled comparison isolates the effect of output-distribution alignment: all three predictors see identical data in identical order with identical architectures; only the loss function differs. % exp_id: mse30_uniform_s42, mse50_uniform_s42\n\nMSE uses $\\lambda_{\\max}{=}1000$ (vs.\\ KL's 5000) because MSE's per-layer gradient magnitude is approximately $5\\times$ larger than KL's end-to-end gradient, requiring proportionally less penalty pressure to achieve comparable sparsity control. Both reach their target sparsity within 110 steps.\nAt 50\\% target, MSE converges to the target sparsity for seed 42; however, with seed 123, sparsity reaches only 5.1\\% under the same $\\lambda_{\\max}$ cap (eval PPL$=$15{,}789, random-level), indicating high sensitivity to initialization---a failure mode not observed with KL-based losses.\nAt 30\\%, MSE achieves 27.7\\% actual sparsity for s42 (gap 2.3pp).\nThe 3-seed MSE mean (18.52$\\pm$1.68; s42=20.43, s123=17.73, s456=17.39) is still $1.7\\times$ worse than TEAL (10.82), confirming that the performance deficit stems from the loss function, not insufficient sparsity pressure.\n\n\n\\section{Extended SNR Analysis}\n\\label{app:snr_extended}\n\nFigure~\\ref{fig:snr_trajectory} plots gradient SNR across the full 1000-step training for both KL and BCE predictors, measured at 14 checkpoints (LLaMA-3.1-8B, C4) with 95\\% bootstrap confidence intervals.\nFrom step 100 onward, BCE maintains consistently higher SNR than KL (2.3--17$\\times$ depending on training phase), with the gap narrowing toward convergence ($2.3\\times$ at step 1000: $2.026{\\times}10^{-3}$ vs.\\ $8.78{\\times}10^{-4}$). % exp_id: snr_full_curve_1000steps\nDespite KL's noisier gradient signal, KL-trained predictors produce substantially better masks (Table~\\ref{tab:main}), confirming that \\emph{target alignment} matters more than gradient clarity for mask quality.\nBCE's higher SNR reflects its simpler per-neuron classification objective, which concentrates gradients on individual neuron decisions; KL's coupled gradient distributes signal across all mask decisions jointly, yielding lower SNR but discovering compositionally superior mask patterns (\\S\\ref{sec:method:gradient}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{snr_trajectory.pdf}\n\\caption{Gradient SNR trajectory across 1000 training steps. BCE (orange) maintains consistently higher SNR than KL (blue) from step 100 onward (2.3--17$\\times$), yet KL produces superior masks (Table~\\ref{tab:main}), suggesting that target alignment matters more than gradient clarity for mask quality.}\n\\label{fig:snr_trajectory}\n\\end{figure}\n\n\n\\section{Extended Downstream Evaluation}\n\\label{app:downstream}\n\nTable~\\ref{tab:downstream} reports HellaSwag and PIQA across sparsity levels and allocation strategies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended downstream benchmarks (LLaMA-3.1-8B). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc. KL 30\\% uniform: 3-seed mean$\\pm$std; others: seed 42.}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Method & HellaSwag & PIQA \\\\\n\\midrule\n0\\% & Dense & \\textbf{82.35} & \\textbf{80.90} \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& KL uniform & \\textbf{71.07$\\pm$0.54} & \\textbf{74.95$\\pm$0.25} \\\\ % exp_id: hellaswag_piqa_kl30_uniform (3-seed)\n& TEAL uniform & 63.31 & 72.80 \\\\ % exp_id: bench_teal30_uniform_6task\n& BCE isocompute & 62.81 & 74.21 \\\\ % exp_id: bce_isocompute_30u_hellaswag_piqa\n\\midrule\n\\multirow{3}{*}{50\\%}\n& KL global & \\textbf{58.95} & \\textbf{69.48} \\\\ % exp_id: hellaswag_piqa_kl50_global\n& KL uniform & 56.66 & 69.10 \\\\ % exp_id: hellaswag_piqa_kl50_uniform\n& TEAL uniform & 39.35 & 63.66 \\\\ % exp_id: bench_teal50_uniform_6task\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 30\\%, the KL predictor retains 86.3\\% of dense HellaSwag accuracy (71.07$\\pm$0.54 vs.\\ 82.35, 3-seed) and 92.6\\% of PIQA (74.95$\\pm$0.25 vs.\\ 80.90), confirming moderate degradation on non-reasoning tasks.\nAt 50\\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\\S\\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).\n\n\n\\section{Compensation Training Convergence}\n\\label{app:comp_convergence}\n\nAll compensation networks~\\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\\% s42 (final loss 0.70), 30\\% s456 (0.68), 50\\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42\n\n\n\\section{Qwen-2.5-14B Detailed Results}\n\\label{app:14b}\n\n\\begin{table}[h]\n\\centering\n\\caption{Qwen-2.5-14B at 30\\% nominal sparsity. Actual sparsity differs: KL 29.6\\% (3-seed), TEAL 29.3\\% (target 30\\%). \\textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\\% native sparsity (\\S\\ref{sec:method:gradient}), so forced global top-$k$ is used.}\n\\label{tab:14b}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\emph{Global top-$k$ allocation}} \\\\\nKL (Ours) & \\textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \\textbf{75.01} & \\textbf{77.37} \\\\ % exp_id: qwen14b_kl30_s42\nTEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 & 70.51 & 74.70 \\\\ % exp_id: qwen14b_teal30_eval\nBCE & 8.76 & \\textbf{57.59} & 72.61 & 71.67 & \\textbf{53.07} & 53.43 & 68.28 \\\\ % exp_id: qwen14b_bce30_s42_eval\n\\midrule\n\\multicolumn{8}{l}{\\emph{Uniform allocation}} \\\\\nKL (Ours) & \\textbf{7.90} & 53.50 & \\textbf{72.82} & 63.55 & 32.2$\\pm$5.3 & \\textbf{72.68$\\pm$0.2} & \\textbf{76.01$\\pm$1.1} \\\\ % exp_id: qwen14b_kl30_uniform (3-seed s42/s123(v4)/s456)\nTEAL & 8.01 & \\textbf{55.29} & 69.85 & \\textbf{66.34} & \\textbf{52.1} & 67.72 & 74.70 \\\\ % exp_id: qwen14b_teal30_uniform\n\\bottomrule\n\\multicolumn{8}{l}{\\footnotesize GSM8K: 3-seed (s42/s123(v4)/s456).} \\\\\n\\end{tabular}}\n\\end{table}\n\nUnder global allocation, BCE's HellaSwag drops to 53.43\\% ($-$17pp vs.\\ TEAL), indicating that the magnitude-based predictor's mask quality degrades severely when combined with non-uniform budget distribution at 14B scale. % exp_id: qwen14b_bce30_s42_eval, qwen14b_teal30_eval\n\n\\section{Full Allocation Analysis}\n\\label{app:alloc_full}\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation summary (LLaMA-3.1-8B). $\\pm$: 3-seed; $^\\ast$high seed variance.}\n\\label{tab:phase}\n\\footnotesize\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & MMLU \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & 35.7$\\pm$9.5$^\\ast$ \\\\ % exp_id: kl30_3seed_global\n& Uniform & \\textbf{8.81$\\pm$0.02} & \\textbf{40.7$\\pm$1.3} \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_reeval, kl50_global_s123_downstream_v2, kl50_global_s456_eval\n& Uniform & 11.92$\\pm$0.07 & 28.0$\\pm$0.6 \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:phase_full} extends Table~\\ref{tab:phase} with all downstream metrics.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Full allocation analysis: global top-$k$ vs.\\ uniform across sparsity levels (LLaMA-3.1-8B). Entries with $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); others: seed 42. $^\\ast$High MMLU seed variance (individual seeds span 25.3--43.5\\%).}\n\\label{tab:phase_full}\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n\\multirow{2}{*}{25\\%}\n& Global & \\textbf{8.17} & 45.4 & 70.6 & \\textbf{46.6} & \\textbf{11.5} \\\\\n& Uniform & 8.23 & \\textbf{46.5} & \\textbf{71.8} & 44.0 & 11.0 \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5$^\\ast$ & \\textbf{8.0$\\pm$0.7} \\\\\n& Uniform & \\textbf{8.81$\\pm$0.02} & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & \\textbf{40.7$\\pm$1.3} & 7.5$\\pm$0.1 \\\\\n\\midrule\n\\multirow{2}{*}{35\\%}\n& Global & \\textbf{9.31} & \\textbf{38.9} & \\textbf{67.6} & \\textbf{40.4} & \\textbf{7.7} \\\\\n& Uniform & 9.44 & 38.7 & 66.5 & 37.8 & 4.3 \\\\\n\\midrule\n\\multirow{2}{*}{40\\%}\n& Global & \\textbf{10.14} & 39.5 & \\textbf{67.5} & \\textbf{39.5} & \\textbf{6.6} \\\\\n& Uniform & 10.76 & \\textbf{39.6} & 63.1 & 35.5 & 3.6 \\\\\n\\midrule\n\\multirow{2}{*}{45\\%}\n& Global & \\textbf{10.80} & \\textbf{39.2} & \\textbf{64.6} & 30.4 & \\textbf{3.0} \\\\\n& Uniform & 10.95 & 37.6 & 63.6 & \\textbf{30.6} & 2.7 \\\\\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.7$\\pm$1.3} \\\\\n& Uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Mask Pattern Visualization}\n\\label{app:mask_viz}\n\nFigure~\\ref{fig:mask_heatmap} shows per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity.\nFigure~\\ref{fig:scatter} shows per-neuron importance scores at layer 16.\nFigure~\\ref{fig:mask_comparison} shows binary mask comparisons at layers 2, 16, and 28.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{neuron_scatter_layer16.pdf}\n\\caption{KL vs.\\ magnitude importance scores for layer 16 neurons at 50\\% sparsity. 41\\% of neurons fall in disagreement quadrants where one method selects a neuron the other discards.}\n\\label{fig:scatter}\n\\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_divergence_heatmap.pdf}\n\\caption{Per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity (64 samples, 131K tokens). Divergence peaks in layers 24--28 (Jaccard distance $>$0.73 at 50\\%) and increases with sparsity across all layers.}\n\\label{fig:mask_heatmap}\n\\end{figure*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_comparison.pdf}\n\\caption{Binary mask comparison between KL-derived and magnitude-based masks at selected layers (L2, L16, L28) for 30\\% and 50\\% sparsity (64 samples). Black = selected by both, light regions = selected by only one method. Deep layers show the largest divergence (L28 Jaccard distance: 0.60 at 30\\%, 0.74 at 50\\%).}\n\\label{fig:mask_comparison}\n\\end{figure*}\n\n\n\\section{Cross-Architecture Comparison}\n\\label{app:cross_arch}\n\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. \\textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\\%: 3-seed mean$\\pm$std; other rows: seed 42.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.93$\\pm$0.19} & 8.38 & 1.21$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, teal_30_mistral, kl30_3seed_global\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL PPL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity).\nTable~\\ref{tab:mistral_downstream} reports downstream task accuracy at 30\\% sparsity on Mistral-7B-v0.3 (3-seed). KL improves PPL ($-$17.3\\%) and commonsense tasks (WG +6.7pp) but MMLU is tied (43.3\\% vs.\\ 43.5\\%); ARC-c shows high seed variance ($\\sigma$=6.4pp); GSM8K reverses.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B-v0.3 downstream evaluation at 30\\% sparsity. $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); TEAL is deterministic (single run). ARC-c exhibits high seed variance ($\\sigma$=6.4pp).}\n\\label{tab:mistral_downstream}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\\\\n\\midrule\nDense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\\\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa\nKL 30\\% & \\textbf{6.93$\\pm$0.19} & \\textbf{44.9$\\pm$6.4} & \\textbf{70.2$\\pm$1.2} & \\textbf{69.7$\\pm$0.8} & \\textbf{74.8$\\pm$0.4} & 43.3$\\pm$1.5 & 8.6$\\pm$2.2 \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456\nTEAL 30\\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & \\textbf{43.5} & \\textbf{15.9} \\\\ % exp_id: mistral_teal30_downstream\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Taxonomy Discussion}\n\\label{app:taxonomy}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2025spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-token} methods~\\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass; each mask decision's gradient reflects its joint effect with all other masks on the final distribution.\n\nSPON~\\cite{xu2025spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\\times$ coupled).\nDejaVu~\\cite{liu2023dejavu} and FastForward~\\cite{gautam2026fastforward} achieve per-token granularity but use BCE, where each neuron's gradient is independent of other mask states.\nD2DMoE~\\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.\nWe define \\emph{output-distribution alignment} as whether the training loss optimizes a quantity that composes across layers.\nKL on output logits directly optimizes next-token prediction loss, which does not suffer from error composition; per-layer MSE minimizes reconstruction error independently at each layer, but layer-wise optima do not compose---a mask minimizing FFN output error at layer $\\ell$ may amplify errors in layers $\\ell{+}1 \\ldots L$.\nThe SNR analysis (\\S\\ref{sec:method:gradient}) corroborates this: KL achieves the best masks despite $2.3\\times$ lower SNR than BCE, while MSE produces the worst masks.\nThe framework predicts that losses operating on output-level quantities should outperform intermediate-level losses, a hypothesis consistent with our MSE results and testable with alternative output-level objectives.\n\n\\section{Oracle Mask Provenance}\n\\label{app:oracle_provenance}\n\nC1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold (logits $> 0$, equivalent to $\\sigma > 0.5$); they reflect one specific training trajectory (optimizer state, data order, Gumbel noise).\nThe s42/s123/s456 consistency ($\\leq$1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.\n\n\\section{SPON Orthogonality}\n\\label{app:spon}\n\nSPON~\\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\nThe decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.\n\n\\section{Per-Layer KL Downstream Decomposition}\n\\label{app:perlayer_downstream}\n\nTable~\\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\\ coupling scope decomposition at 30\\% sparsity (\\S\\ref{sec:perlayer}). BoolQ's $\\approx$100\\% coupling is an upper bound confounded by high cross-seed variance ($\\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.\n\n\\begin{table}[h]\n\\centering\n\\caption{2D decomposition at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \\S\\ref{sec:perlayer}).}\n\\label{tab:perlayer_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\n& PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & BoolQ \\\\\n\\midrule\nE2E KL & 8.81$\\pm$0.02 & 43.7 & 68.9 & 40.7 & 7.5 & 73.7 \\\\\nPer-layer KL & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & 64.5 \\\\\nMSE & 18.52$\\pm$1.68 & 35.8$\\pm$4.1 & 59.8$\\pm$2.6 & 30.7$\\pm$2.6 & 2.3$\\pm$0.7 & 64.5$\\pm$5.3 \\\\\n\\midrule\nTotal gap & 9.71 & 7.9 & 9.1 & 10.0 & 5.2 & 9.2 \\\\\nSignal type (\\%) & 97.5 & 51.9 & 67.0 & 79.0 & 67.3 & $\\approx$0 \\\\\nCoupling (\\%) & 2.5 & 48.1 & 33.0 & 21.0 & 32.7 & $\\approx$100 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{$K{=}4$ Mismatch Control}\n\\label{app:k4_downstream}\n\nTable~\\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\\% sparsity.\nTraining with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\\ 1/32 layers masked during training, while inference applies all 32).\nThe gap closure column reports the fraction of the $K{=}1 \\to$ E2E KL gap closed by $K{=}4$.\n\n\\begin{table}[h]\n\\centering\n\\caption{3-seed $K{=}4$ mismatch control at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \\in \\{42, 123, 456\\}$). Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\\text{E2E} - K{=}1) \\times 100$.}\n\\label{tab:k4_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\n& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\\%) \\\\\n\\midrule\nPPL$\\downarrow$ & 8.89$\\pm$0.01 & 9.05$\\pm$0.02 & 8.81$\\pm$0.02 & 66.7 \\\\\nARC-c & 40.0$\\pm$1.3 & 39.9 & 43.7$\\pm$2.5 & 2.6 \\\\\nWG & 66.9$\\pm$0.2 & 65.9 & 68.9$\\pm$0.4 & 33.3 \\\\\nMMLU$^\\ast$ & 42.7$\\pm$1.4 & 38.6 & 40.7$\\pm$1.3 & $>$100 \\\\\nGSM8K & 7.0$\\pm$1.6 & 5.8 & 7.5$\\pm$0.1 & 70.6 \\\\\nBoolQ$^\\dagger$ & 67.7$\\pm$7.5 & 64.5$\\pm$11.5 & 73.7 & 34.8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize $^\\ast$MMLU $K{=}4$ systematically exceeds E2E across all 3 seeds; attributable to $K{=}4$'s near-uniform per-layer sparsity (std=0.003) matching uniform eval allocation. Independently confirmed: removing the predictor's middle-layer valley yields MMLU=44.0\\% (Appendix~\\ref{app:constraint}).\n$^\\dagger$BoolQ exhibits high inter-seed variance for both $K{=}4$ (std=7.5) and $K{=}1$ (std=11.5); gap closure unreliable.}\n\\end{table}\n\n\\section{Per-Layer Sparsity Constraint Analysis}\n\\label{app:constraint}\n\nTo test the causal role of the KL predictor's learned per-layer allocation, we evaluate two inference-time interventions at 30\\% overall sparsity (seed 42, uniform allocation baseline):\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity constraint analysis. \\emph{Protect late}: cap L22--L28 sparsity $\\leq$30\\%; \\emph{Remove valley}: override L14--L18 sparsity to 30\\%. Budget redistributed to maintain 30\\% overall.}\n\\label{tab:constraint}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & PPL & ARC-c & MMLU & GSM8K \\\\\n\\midrule\nKL baseline (s42) & 8.82 & 40.8 & 40.6 & 7.4 \\\\\nProtect late layers & 9.26 & 42.4 & 40.7 & 6.5 \\\\\nRemove valley & 8.76 & 39.3 & 44.0 & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nProtecting late layers (L22--L28) does not improve knowledge-intensive metrics despite reducing their sparsity from 48--57\\% to $\\leq$30\\%, while worsening PPL by 5.2\\%.\nConversely, removing the protection valley (forcing L14--L18 to 30\\% instead of 14--18\\%) improves MMLU by +3.4pp and GSM8K by +1.6pp at the cost of ARC-c $-$1.5pp.\nThe KL predictor's learned allocation thus represents a task-dependent trade-off---prioritizing commonsense reasoning via middle-layer protection---rather than a uniformly optimal pattern.\nThis allocation trade-off also explains the $K{=}4$ MMLU anomaly (\\S\\ref{app:k4_downstream}): $K{=}4$'s near-uniform learned sparsity (std=0.003) inherently removes the valley, producing MMLU=43.5 comparable to the remove-valley condition (44.0).\n\n\\section{Per-Layer Sparsity Distribution}\n\\label{app:perlayer_sparsity}\n\nThe KL predictor at 30\\% target sparsity learns a non-uniform per-layer allocation that differs markedly from magnitude-based selection.\nAggregate sparsity is similar across broad regions (early L0--L7: KL 28.1\\% vs.\\ magnitude 27.5\\%; late L24--L31: 44.9\\% vs.\\ 47.2\\%), but middle layers (L8--L23) exhibit high internal variance despite similar averages (28.2\\% vs.\\ 27.3\\%).\nTable~\\ref{tab:perlayer_sparsity} highlights three sub-ranges.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity sub-ranges: KL predictor vs.\\ magnitude (LLaMA-3.1-8B, 30\\%, uniform allocation). Ranges denote min--max across layers in each group.}\n\\label{tab:perlayer_sparsity}\n\\begin{tabular}{lccc}\n\\toprule\nLayer Range & KL (\\%) & Mag (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nL8--L12 (high pruning) & 32--36 & 25--26 & $+$7 to $+$10 \\\\\nL14--L18 (protection valley) & 14--18 & 28--30 & $-$8 to $-$16 \\\\\nL22--L28 (aggressive pruning) & 48--57 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{C4 Training Data Control}\n\\label{app:c4_control}\n\nTo test whether WikiText-103's narrow domain drives the knowledge-task regression (\\S\\ref{sec:experiments}), we train the KL predictor on C4~\\cite{raffel2020c4} (diverse web text) under identical hyperparameters (1000 steps, 30\\% uniform, s42).\n\n\\begin{table}[h]\n\\centering\n\\caption{C4-trained vs.\\ WikiText-trained KL predictor (LLaMA-3.1-8B, 30\\% uniform, s42).}\n\\label{tab:c4_control}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\nTraining Data & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\\\\n\\midrule\nWikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe C4-trained predictor achieves comparable MMLU (40.0\\% vs.\\ 40.6\\%) but worse GSM8K (4.1\\% vs.\\ 7.4\\%) and higher PPL (11.55 vs.\\ 8.82), despite training on more diverse text.\nThis rules out training data composition as the primary cause of knowledge-task regression and supports the hypothesis that forward KL's mode-covering property structurally under-protects rare reasoning-critical activations. % exp_id: c4_control_eval\n\n\\section{Per-Layer Coupling Breadth Analysis}\n\\label{app:k_curve}\n\nWe vary the number of layers coupled per training step ($K$) from 1 (pure per-layer) to 32 (end-to-end), evaluating all predictors under TEAL uniform allocation at 30\\% sparsity on LLaMA-3.1-8B.\n\n\\begin{table}[h]\n\\centering\n\\caption{K-curve: coupling breadth vs.\\ predictor quality (30\\%, TEAL uniform, LLaMA-3.1-8B). All values are 3-seed mean$\\pm$std (s42/s123/s456) except $K{=}1$ downstream (single seed). ``---'' = not evaluated.}\n\\label{tab:k_curve}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{cccccccc}\n\\toprule\n$K$ & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\n1 & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & --- & --- \\\\\n2 & 10.75$\\pm$0.15 & 39.7$\\pm$1.2 & 63.2$\\pm$1.7 & 38.3$\\pm$3.2 & 2.8$\\pm$0.6 & 66.5$\\pm$1.0 & 73.5$\\pm$0.7 \\\\\n4 & 8.89$\\pm$0.01 & 40.0$\\pm$1.2 & 66.9$\\pm$0.2 & 42.7$\\pm$1.4 & 7.0$\\pm$1.6 & 67.8$\\pm$1.0 & 74.5$\\pm$0.5 \\\\\n8 & 9.00$\\pm$0.06 & 40.7$\\pm$1.0 & 68.7$\\pm$1.3 & 40.4$\\pm$0.6 & 6.8$\\pm$1.3 & 69.0$\\pm$1.1 & 75.1$\\pm$1.1 \\\\\n16 & 8.67$\\pm$0.02 & 41.9$\\pm$1.1 & 68.5$\\pm$0.9 & 40.9$\\pm$2.9 & 8.5$\\pm$1.2 & 70.1$\\pm$0.4 & 75.0$\\pm$0.8 \\\\\n32 (E2E) & 8.81$\\pm$0.02 & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & 40.7$\\pm$1.3 & 7.5$\\pm$0.1 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nPPL exhibits a non-monotonic U-shape (Figure~\\ref{fig:k_curve_ppl}): $K{=}2$ is worst (10.75$\\pm$0.15), likely due to insufficient per-layer updates (${\\sim}$62 updates/layer vs.\\ ${\\sim}$250 at $K{=}8$). $K{=}16$ achieves the lowest PPL (8.67$\\pm$0.02), marginally better than E2E (8.81$\\pm$0.02). $K{=}16$ MMLU exhibits high seed variance (std=2.9; s42=44.0, s123=40.0, s456=38.7), with the 3-seed mean (40.9) indistinguishable from E2E (40.7$\\pm$1.3).\nThe signal type gap ($K{=}1$ KL 9.05 vs.\\ per-layer MSE 18.52$\\pm$1.68) of 9.47 PPL exceeds the coupling breadth range within KL (best $K{=}16$ 8.67 vs.\\ worst $K{=}2$ 10.75 = 2.08 PPL), reinforcing that output-distribution alignment, not coupling scope, is the primary quality lever for PPL at this sparsity level. % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed, perlayer_kl_30_3seed, perlayer_kl_k4_3seed\n\n\\section{Licenses}\n\\label{app:licenses}\n\nLLaMA-3.1-8B is released under the Llama 3.1 Community License Agreement.\nMistral-7B-v0.3 is released under the Apache 2.0 License.\nQwen-2.5-14B is released under the Apache 2.0 License.\nWikiText-103 and WikiText-2~\\cite{merity2017pointer} are released under the Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0).\nAll evaluation benchmarks (ARC, WinoGrande, MMLU, GSM8K, HellaSwag, PIQA) are publicly available under their respective licenses.\nOur code will be released under the MIT License upon acceptance.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
      "numLines": 673,
      "startLine": 1,
      "totalLines": 673
    }
  },
  "sourceToolAssistantUUID": "9208c074-8482-44db-ae8d-4d1e3040d45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-24T04:22:33.102Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CZzStD1hu6YpzfJGQGmaYR`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "045c8dda-cc00-4e2a-85ff-d4163b02b467",
  "isSidechain": false,
  "requestId": "req_011CbLkj1eggAw8hUfJ9hBHY",
  "type": "assistant",
  "uuid": "59e0218b-b140-4f62-95b8-80f14f28d628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP9sqAKds59As6Sv12idsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 39983,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 39983,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-24T04:22:33.255Z_

<details><summary>↩ Tool result · `toolu_01CZzStD1hu6YpzfJGQGmaYR`</summary>

```text
issues:
  # ============================================================
  # Round 28 — Active issues
  # ============================================================

  - id: "R20-W1"
    summary: "Per-layer KL decomposition 的 train-inference mismatch confound 未解决"
    category: method
    severity: critical
    status: in_progress
    first_raised_round: 20
    last_seen_round: 28
    mentions:
      - {round: 21, reviewers: [1, 2], note: "R21 Critical。K=4 single-seed。"}
      - {round: 22, reviewers: [1, 2], note: "R22 N2。97.5% 精确数字不可靠。"}
      - {round: 24, reviewers: [1, 2], note: "R24 C1。K=1 有 32× train-inference mismatch。"}
      - {round: 25, reviewers: [1, 2], note: "R25 N1/N2。"}
      - {round: 26, reviewers: [1, 2], note: "R26 R1-N2/R2-N1。建议 stop-gradient 或更多 K 值。"}
      - {round: 27, reviewers: [1, 2], note: "R27 C1。K-curve 6 点中除 K=4 外均 single-seed。K=16 PPL 优势可能 seed-specific。per-layer update count confound 未解决。"}
      - {round: 28, reviewers: [1, 2], note: "R28 双方 AGREE critical。50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）是 decisive evidence。K=4 在 50% 更差（44.23）。论文已有 'upper bound' 和 'exploratory' 标注，但 'may account for a substantial portion' 仍被认为对 exploratory analysis 过强。K=2/8/16 3-seed 数据已补充但 per-layer update count confound 仍未解决。"}
    action_items:
      - {round: 21, action: "K=4 3-seed", assigned_to: "main_agent", status: done}
      - {round: 22, action: "定性 'majority of PPL gap'", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "限定 decomposition 为 moderate sparsity", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "K=2/K=8/K=16 实验扩展 K-curve", assigned_to: "main_agent", status: done}
      - {round: 27, action: "§4.5 降级为 Exploratory Decomposition + may account for a substantial portion", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "experiments L161 'primary design lever' → 'major factor for PPL'", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "appendix L647 加 'for PPL at this sparsity level (preliminary)'", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "K=2/8/16 各补 s123/s456 3-seed", assigned_to: "main_agent", status: done}
      - {round: 28, action: "§4.5 restructured: observation-first narrative, deleted 'may account for a substantial portion', added explicit confound statement, title changed to 'Empirical Signal Type vs. Coupling Scope'", assigned_to: "paper_agent", status: done}
    resolution: ""
    resolution_round: null

  - id: "R20-N2"
    summary: "MMLU/GSM8K 跨架构系统性退步缺乏机制分析"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 18
    last_seen_round: 28
    mentions:
      - {round: 21, reviewers: [1, 2], note: "R21 Critical。"}
      - {round: 24, reviewers: [1, 2], note: "R24 C2。"}
      - {round: 25, reviewers: [1, 2], note: "R25 最高优先级。"}
      - {round: 26, reviewers: [1, 2], note: "R26 R1-N1/R2-N2。"}
      - {round: 27, reviewers: [1, 2], note: "R27 C3。C4 控制 1 seed 不够。KL uniform vs TEAL uniform MMLU 差 5pp（同 allocation）归因未分析。跨 scale 退步暗示根本限制但无缓解路径。"}
      - {round: 28, reviewers: [1, 2], note: "R28 双方 AGREE critical。C4 控制排除训练数据偏差但 mode-covering 假设无直接验证。Constraint analysis（remove valley → MMLU +3.4pp）说明 allocation pattern 影响而非 mode-covering 机制。论文未追问为何退步是 structural。缺 hybrid loss 等缓解方向讨论。"}
    action_items:
      - {round: 21, action: "Constraint 实验", assigned_to: "main_agent", status: done}
      - {round: 25, action: "C4 控制实验", assigned_to: "main_agent", status: done}
      - {round: 26, action: "C4 结果写入 §4.2 + Appendix U", assigned_to: "paper_agent", status: done}
      - {round: 26, action: "Conclusion 'primary design dimension' 限定", assigned_to: "paper_agent", status: done}
      - {round: 26, action: "Abstract 量化知识退步", assigned_to: "paper_agent", status: done}
      - {round: 28, action: "Task-type split elevated to contribution C2; Conclusion expanded with task-type dependent discussion and KL-for-commonsense/TEAL-for-knowledge suggestion", assigned_to: "paper_agent", status: done}
    resolution: ""
    resolution_round: null

  - id: "R24-W2"
    summary: "高方差下游指标统计可靠性不足"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 24
    last_seen_round: 28
    mentions:
      - {round: 24, reviewers: [1, 2], note: "ARC-c 95% CI ≈ ±8.9pp。"}
      - {round: 25, reviewers: [1, 2], note: "Qwen-14B GSM8K std=5.2pp。"}
      - {round: 27, reviewers: [1, 2], note: "R27 W1。30% Global MMLU σ=9.5pp，n=3 CI ≈ ±23.6pp。Abstract/Conclusion 措辞未带 directional 限定。"}
      - {round: 28, reviewers: [1, 2], note: "R28 双方 AGREE critical。Abstract 已改 'directional commonsense gains (n=3)'，但 KL global MMLU 35.7±9.5 的 95% CI ≈ [22.1, 49.3]，任何基于此的比较无统计意义。Qwen-14B GSM8K CV=16.3%。论文在 §4.2 承认 CI overlap 但 abstract/conclusion 仍报告具体 gap 数值。R2 指出 ≥5 seeds 在 14B 有计算限制，应 upfront disclosure。"}
    action_items:
      - {round: 24, action: "正文加 CI overlap caveat", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "Qwen GSM8K 用 mean±std", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "Abstract 'directional commonsense gains (n=3)'", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "Conclusion 'directional downstream gains'", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "Introduction 'robust' → 'directional'", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "experiments 'outperforms' → 'directional improvements'", assigned_to: "paper_agent", status: done}
      - {round: 28, action: "Conclusion expanded with 'Downstream differences are directional (n=3, CIs overlap)' explicit statement", assigned_to: "paper_agent", status: done}
    resolution: ""
    resolution_round: null

  - id: "R27-C2"
    summary: "'Primary design dimension' claim 在知识任务不成立"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 24
    last_seen_round: 28
    mentions:
      - {round: 24, reviewers: [1, 2], note: "建议软化。"}
      - {round: 26, reviewers: [1, 2], note: "限定为 PPL+commonsense。"}
      - {round: 27, reviewers: [1, 2], note: "R27 C2。TEAL MMLU 45.86 vs KL 40.7 同 uniform allocation。claim 仅在 PPL+commonsense 成立。"}
      - {round: 28, reviewers: [], note: "R28 本轮未作为独立 issue 提出。Conclusion 已限定 scope。但 R2 指出 Conclusion 仅 2 句话未充分讨论 scope limitation。"}
    action_items:
      - {round: 27, action: "Conclusion 加 'for perplexity and commonsense at moderate sparsity'", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "experiments L161 限定 scope", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "appendix L647 限定 scope", assigned_to: "paper_agent", status: done}
      - {round: 28, action: "Conclusion expanded to 5 sentences with task-type scope discussion", assigned_to: "paper_agent", status: done}
    resolution: ""
    resolution_round: null

  - id: "R24-W3"
    summary: "C1 ablation soft→hard mask representation 残余 confound"
    category: method
    severity: warning
    status: open
    first_raised_round: 24
    last_seen_round: 28
    mentions:
      - {round: 24, reviewers: [1, 2], note: "Oracle 二值化丢失排序信息。"}
      - {round: 27, reviewers: [1, 2], note: "R27 W2。BCE+Gumbel vs BCE 差 15%。但 R2 指出核心发现仍成立。"}
      - {round: 28, reviewers: [1, 2], note: "R28 双方 AGREE。s42 non-seed-matched + BCE+Gumbel (32.22) 比 BCE (27.97) 更差说明 Gumbel 对 BCE 有害。s123/s456 seed-matched ≤1.18pp 部分缓解。"}
    action_items:
      - {round: 24, action: "讨论 oracle 信息损失", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "正文 binarization confound caveat", assigned_to: "paper_agent", status: done}
    resolution: ""
    resolution_round: null

  - id: "R25-N1"
    summary: "方法新颖性边界需更清晰论证"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 25
    last_seen_round: 28
    mentions:
      - {round: 25, reviewers: [2], note: "核心组件均成熟技术。"}
      - {round: 26, reviewers: [2], note: "MaskLLM 共享核心 recipe。"}
      - {round: 27, reviewers: [1, 2], note: "R27 共识：新颖性为组合级别。"}
      - {round: 28, reviewers: [2], note: "R28 R2 维持 critical（MaskLLM 共享 recipe-level 原则，contextual vs static 区别缺实验验证）。R1 REBUT（不同范式，直接对比不合理）。分歧未解决。"}
    action_items:
      - {round: 25, action: "Intro contribution list 重排", assigned_to: "paper_agent", status: done}
      - {round: 26, action: "Table 1 加入 MaskLLM", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "Contribution items 加 Empirical/Practical 标签", assigned_to: "paper_agent", status: done}
      - {round: 28, action: "Contribution labels changed Practical→Analytical", assigned_to: "paper_agent", status: done}
    resolution: ""
    resolution_round: null

  - id: "R28-W1"
    summary: "Conclusion 仅 2 句话，缺 broader impact 和 future directions"
    category: writing
    severity: warning
    status: in_progress
    first_raised_round: 28
    last_seen_round: 28
    mentions:
      - {round: 28, reviewers: [1, 2], note: "R28 双方 AGREE。2 句话未讨论 knowledge regression implications、future directions（如 hybrid loss）、broader impact。"}
    action_items:
      - {round: 28, action: "Conclusion expanded from 2 to 5 sentences: added task-type split finding, KL-for-commonsense/TEAL-for-knowledge suggestion, per-layer decomposition open question, statistical qualifier", assigned_to: "paper_agent", status: done}
    resolution: ""
    resolution_round: null

  - id: "R28-W2"
    summary: "Contribution C3/C4 标注 'Practical' 在无 wall-clock 加速下有误导性"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 28
    last_seen_round: 28
    mentions:
      - {round: 28, reviewers: [1, 2], note: "R28 R2 列为 critical，R1 AGREE 但认为 should-fix。Predictor +6.4% latency，无 sparse kernel 支持。论文已多处声明无加速，但 contribution 标签 misleading。建议改为 Analytical/Empirical。"}
    action_items:
      - {round: 28, action: "Contribution labels changed Practical→Analytical in introduction.tex", assigned_to: "paper_agent", status: done}
    resolution: ""
    resolution_round: null

  - id: "R26-W1"
    summary: "14.5% PPL improvement 引用基准在 Abstract 与 Table 2 不一致"
    category: writing
    severity: warning
    status: in_progress
    first_raised_round: 26
    last_seen_round: 28
    mentions:
      - {round: 26, reviewers: [1, 2], note: "Abstract 用 matched-sparsity，Table 2 找不到 10.30。"}
      - {round: 27, reviewers: [1, 2], note: "R27 Detailed Comments: 14.5% 引用基准在 Table 2 中找不到。"}
      - {round: 28, reviewers: [], note: "R28 本轮未被任何 Reviewer 提及，可能已通过 Table 2 caption 的 ‡ 标注解决，待 Research Director 确认。"}
    action_items:
      - {round: 26, action: "Table 2 caption 标注 matched-sparsity 来源", assigned_to: "paper_agent", status: done}
    resolution: ""
    resolution_round: null

  # ============================================================
  # Round 28 — New should-fix issues (no action taken yet)
  # ============================================================

  - id: "R28-W3"
    summary: "MSE 50% baseline 仅 s42 有效（s123 catastrophic PPL=15,789），作为 baseline 不可信"
    category: experiment
    severity: warning
    status: open
    first_raised_round: 28
    last_seen_round: 28
    mentions:
      - {round: 28, reviewers: [1, 2], note: "R28 双方 AGREE。2/3 seed 失败说明 MSE 在 50% 下不稳定。Table 4 已有 § 标注但仍在主表中。"}
    action_items: []
    resolution: ""
    resolution_round: null

  - id: "R28-W4"
    summary: "30% 下缺少 BCE isocompute (2700 steps) 对比"
    category: experiment
    severity: warning
    status: open
    first_raised_round: 28
    last_seen_round: 28
    mentions:
      - {round: 28, reviewers: [1, 2], note: "R28 双方 AGREE。BCE isocompute 仅在 50% 下有 3-seed。"}
    action_items: []
    resolution: ""
    resolution_round: null

  - id: "R28-W5"
    summary: "主评估指标单一（WikiText-2 PPL），C4 OOD 不充分"
    category: experiment
    severity: warning
    status: open
    first_raised_round: 28
    last_seen_round: 28
    mentions:
      - {round: 28, reviewers: [1, 2], note: "R28 R1 列为 W5，R2 AGREE。WikiText-2 与 WikiText-103 同源。C4 OOD 30% 仅 2-seed。Uniform 3-seed CV=6.3% vs in-domain 0.2%。"}
    action_items: []
    resolution: ""
    resolution_round: null

  # ============================================================
  # Resolved (older rounds, carried forward)
  # ============================================================

  - id: "R25-W1"
    summary: "BCE 30% uniform 对比已补充"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 25
    last_seen_round: 26
    resolution: "Table 2 已加 BCE 30% uniform (PPL=15.09±0.13, 3-seed)。"
    resolution_round: 27

  - id: "R25-M1"
    summary: "术语不一致"
    category: writing
    severity: minor
    status: resolved
    first_raised_round: 25
    last_seen_round: 27
    resolution: "全文统一为 output-distribution KL。Reviewer 验证 PASS。"
    resolution_round: 27

  - id: "R27-W4"
    summary: "Contribution framing 存在 empirical study vs method 张力"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 27
    last_seen_round: 27
    resolution: "4 个 contribution items 加 Empirical/Practical 标签。Reviewer 验证 PASS。"
    resolution_round: 27

  - id: "R27-W5"
    summary: "Wall-clock speedup 缺失"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 16
    last_seen_round: 28
    mentions:
      - {round: 28, reviewers: [1, 2], note: "R28 R2 将其与 'Practical' 标签合并为新 issue R28-W2。论文已充分 framed 为 empirical study。"}
    resolution: "结构性限制。论文已充分 framed 为 empirical study。多轮维持 resolved。"
    resolution_round: 23

  - id: "R25-W2"
    summary: "MSE 50% baseline 仅 seed 42 有效"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 25
    last_seen_round: 28
    mentions:
      - {round: 28, reviewers: [1, 2], note: "R28 升级为新 issue R28-W3（不可信 baseline）。"}
    resolution: "Table 3 caption 有 § 标注，method.tex 有 '(50%: s42 only)'。但 R28 认为不够，升级为 R28-W3。"
    resolution_round: 27

  - id: "R26-M3"
    summary: "68% divergence 和 32% Jaccard 同句混淆"
    category: writing
    severity: minor
    status: resolved
    first_raised_round: 26
    last_seen_round: 27
    resolution: "Introduction 统一使用 Jaccard distance。Reviewer 验证 PASS。"
    resolution_round: 27

  - id: "R19-N3"
    summary: "无实际 wall-clock 加速"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 16
    last_seen_round: 27
    resolution: "论文已充分 framed 为 empirical study。"
    resolution_round: 23

  - id: "R24-W1"
    summary: "评估覆盖度关键空白"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 24
    last_seen_round: 26
    resolution: "Limitations 已覆盖。Base model 不适用生成评估。"
    resolution_round: 25

  - id: "R24-W4"
    summary: "'Primary design dimension' 需限定"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 24
    last_seen_round: 27
    resolution: "合并入 R27-C2。Conclusion 已限定为 'for perplexity and commonsense at moderate sparsity'。"
    resolution_round: 27

  - id: "R22-W6"
    summary: "Figure 2 仅展示 global allocation"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 21
    last_seen_round: 26
    resolution: "R26/R27 未再提出。"
    resolution_round: 27

  - id: "R19-W1"
    summary: "与 MaskLLM 新颖性区分"
    category: method
    severity: warning
    status: resolved
    first_raised_round: 16
    last_seen_round: 26
    resolution: "合并进 R25-N1。"
    resolution_round: 25

  - id: "R20-W4"
    summary: "WikiText 同分布评估 + C4 OOD"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 20
    last_seen_round: 26
    resolution: "Appendix D OOD 证据充分。"
    resolution_round: 25

  - id: "R22-W3"
    summary: "Table 2 sparsity mismatch 脚注"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 22
    last_seen_round: 26
    resolution: "§4.1 matched 14.5% 独立句。"
    resolution_round: 23

  - id: "R22-W5"
    summary: "规模泛化仅 7-14B"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 22
    last_seen_round: 27
    resolution: "Limitations 已覆盖。"
    resolution_round: 25

  - id: "R25-W3"
    summary: "Introduction 19% 已修正为 14.5%"
    category: writing
    severity: minor
    status: resolved
    first_raised_round: 25
    last_seen_round: 26
    resolution: "数值已修正。"
    resolution_round: 26

  - id: "R25-M2"
    summary: "Eq. 4 s_j 缺层标"
    category: writing
    severity: minor
    status: resolved
    first_raised_round: 25
    last_seen_round: 25
    resolution: "已补充。"
    resolution_round: 25

  - id: "R19-N2"
    summary: "C1 target-swap 因果声明"
    category: method
    severity: warning
    status: resolved
    first_raised_round: 19
    last_seen_round: 24
    resolution: "C1 claim 已降级为 transferability。"
    resolution_round: 23

  - id: "R22-W7"
    summary: "Abstract 信息密度过高"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 22
    last_seen_round: 22
    resolution: "已拆分。"
    resolution_round: 23

  - id: "R22-W8"
    summary: "Conclusion 引用 BoolQ"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 22
    last_seen_round: 22
    resolution: "BoolQ → HellaSwag/PIQA。"
    resolution_round: 23

  - id: "R19-W7"
    summary: "30% sparsity sweet spot"
    category: framing
    severity: info
    status: resolved
    first_raised_round: 19
    last_seen_round: 26
    resolution: "Limitations 已覆盖。"
    resolution_round: 25

  - id: "R15-N3"
    summary: "MaskLLM 新颖性边界"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 9
    last_seen_round: 26
    resolution: "合并进 R25-N1。"
    resolution_round: 23

  - id: "R26-M1"
    summary: "Introduction 中 8.6%/6.4% 未标注 sparsity level"
    category: writing
    severity: minor
    status: resolved
    first_raised_round: 26
    last_seen_round: 26
    resolution: "§4.3 已加 sparsity level 标注。"
    resolution_round: 26

  - id: "R26-M2"
    summary: "'stable downstream' 措辞"
    category: writing
    severity: minor
    status: resolved
    first_raised_round: 26
    last_seen_round: 26
    resolution: "Introduction 已删除 'stable'。"
    resolution_round: 26
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59e0218b-b140-4f62-95b8-80f14f28d628",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "7f8f7bab-73e7-4528-9108-f59b9d0277e8",
  "toolUseResult": {
    "stdout": "issues:\n  # ============================================================\n  # Round 28 — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 28\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 N1/N2。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N2/R2-N1。建议 stop-gradient 或更多 K 值。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 C1。K-curve 6 点中除 K=4 外均 single-seed。K=16 PPL 优势可能 seed-specific。per-layer update count confound 未解决。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE critical。50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）是 decisive evidence。K=4 在 50% 更差（44.23）。论文已有 'upper bound' 和 'exploratory' 标注，但 'may account for a substantial portion' 仍被认为对 exploratory analysis 过强。K=2/8/16 3-seed 数据已补充但 per-layer update count confound 仍未解决。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"定性 'majority of PPL gap'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"限定 decomposition 为 moderate sparsity\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"K=2/K=8/K=16 实验扩展 K-curve\", assigned_to: \"main_agent\", status: done}\n      - {round: 27, action: \"§4.5 降级为 Exploratory Decomposition + may account for a substantial portion\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"experiments L161 'primary design lever' → 'major factor for PPL'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"appendix L647 加 'for PPL at this sparsity level (preliminary)'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"K=2/8/16 各补 s123/s456 3-seed\", assigned_to: \"main_agent\", status: done}\n      - {round: 28, action: \"§4.5 restructured: observation-first narrative, deleted 'may account for a substantial portion', added explicit confound statement, title changed to 'Empirical Signal Type vs. Coupling Scope'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏机制分析\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 28\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 最高优先级。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N1/R2-N2。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 C3。C4 控制 1 seed 不够。KL uniform vs TEAL uniform MMLU 差 5pp（同 allocation）归因未分析。跨 scale 退步暗示根本限制但无缓解路径。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE critical。C4 控制排除训练数据偏差但 mode-covering 假设无直接验证。Constraint analysis（remove valley → MMLU +3.4pp）说明 allocation pattern 影响而非 mode-covering 机制。论文未追问为何退步是 structural。缺 hybrid loss 等缓解方向讨论。\"}\n    action_items:\n      - {round: 21, action: \"Constraint 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 25, action: \"C4 控制实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 26, action: \"C4 结果写入 §4.2 + Appendix U\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Conclusion 'primary design dimension' 限定\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Abstract 量化知识退步\", assigned_to: \"paper_agent\", status: done}\n      - {round: 28, action: \"Task-type split elevated to contribution C2; Conclusion expanded with task-type dependent discussion and KL-for-commonsense/TEAL-for-knowledge suggestion\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标统计可靠性不足\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 28\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 95% CI ≈ ±8.9pp。\"}\n      - {round: 25, reviewers: [1, 2], note: \"Qwen-14B GSM8K std=5.2pp。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 W1。30% Global MMLU σ=9.5pp，n=3 CI ≈ ±23.6pp。Abstract/Conclusion 措辞未带 directional 限定。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE critical。Abstract 已改 'directional commonsense gains (n=3)'，但 KL global MMLU 35.7±9.5 的 95% CI ≈ [22.1, 49.3]，任何基于此的比较无统计意义。Qwen-14B GSM8K CV=16.3%。论文在 §4.2 承认 CI overlap 但 abstract/conclusion 仍报告具体 gap 数值。R2 指出 ≥5 seeds 在 14B 有计算限制，应 upfront disclosure。\"}\n    action_items:\n      - {round: 24, action: \"正文加 CI overlap caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Qwen GSM8K 用 mean±std\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Abstract 'directional commonsense gains (n=3)'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Conclusion 'directional downstream gains'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Introduction 'robust' → 'directional'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"experiments 'outperforms' → 'directional improvements'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 28, action: \"Conclusion expanded with 'Downstream differences are directional (n=3, CIs overlap)' explicit statement\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R27-C2\"\n    summary: \"'Primary design dimension' claim 在知识任务不成立\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 28\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"建议软化。\"}\n      - {round: 26, reviewers: [1, 2], note: \"限定为 PPL+commonsense。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 C2。TEAL MMLU 45.86 vs KL 40.7 同 uniform allocation。claim 仅在 PPL+commonsense 成立。\"}\n      - {round: 28, reviewers: [], note: \"R28 本轮未作为独立 issue 提出。Conclusion 已限定 scope。但 R2 指出 Conclusion 仅 2 句话未充分讨论 scope limitation。\"}\n    action_items:\n      - {round: 27, action: \"Conclusion 加 'for perplexity and commonsense at moderate sparsity'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"experiments L161 限定 scope\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"appendix L647 限定 scope\", assigned_to: \"paper_agent\", status: done}\n      - {round: 28, action: \"Conclusion expanded to 5 sentences with task-type scope discussion\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 28\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化丢失排序信息。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 W2。BCE+Gumbel vs BCE 差 15%。但 R2 指出核心发现仍成立。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。s42 non-seed-matched + BCE+Gumbel (32.22) 比 BCE (27.97) 更差说明 Gumbel 对 BCE 有害。s123/s456 seed-matched ≤1.18pp 部分缓解。\"}\n    action_items:\n      - {round: 24, action: \"讨论 oracle 信息损失\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"正文 binarization confound caveat\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-N1\"\n    summary: \"方法新颖性边界需更清晰论证\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - {round: 25, reviewers: [2], note: \"核心组件均成熟技术。\"}\n      - {round: 26, reviewers: [2], note: \"MaskLLM 共享核心 recipe。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 共识：新颖性为组合级别。\"}\n      - {round: 28, reviewers: [2], note: \"R28 R2 维持 critical（MaskLLM 共享 recipe-level 原则，contextual vs static 区别缺实验验证）。R1 REBUT（不同范式，直接对比不合理）。分歧未解决。\"}\n    action_items:\n      - {round: 25, action: \"Intro contribution list 重排\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Table 1 加入 MaskLLM\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Contribution items 加 Empirical/Practical 标签\", assigned_to: \"paper_agent\", status: done}\n      - {round: 28, action: \"Contribution labels changed Practical→Analytical\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W1\"\n    summary: \"Conclusion 仅 2 句话，缺 broader impact 和 future directions\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。2 句话未讨论 knowledge regression implications、future directions（如 hybrid loss）、broader impact。\"}\n    action_items:\n      - {round: 28, action: \"Conclusion expanded from 2 to 5 sentences: added task-type split finding, KL-for-commonsense/TEAL-for-knowledge suggestion, per-layer decomposition open question, statistical qualifier\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W2\"\n    summary: \"Contribution C3/C4 标注 'Practical' 在无 wall-clock 加速下有误导性\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 R2 列为 critical，R1 AGREE 但认为 should-fix。Predictor +6.4% latency，无 sparse kernel 支持。论文已多处声明无加速，但 contribution 标签 misleading。建议改为 Analytical/Empirical。\"}\n    action_items:\n      - {round: 28, action: \"Contribution labels changed Practical→Analytical in introduction.tex\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-W1\"\n    summary: \"14.5% PPL improvement 引用基准在 Abstract 与 Table 2 不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"Abstract 用 matched-sparsity，Table 2 找不到 10.30。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 Detailed Comments: 14.5% 引用基准在 Table 2 中找不到。\"}\n      - {round: 28, reviewers: [], note: \"R28 本轮未被任何 Reviewer 提及，可能已通过 Table 2 caption 的 ‡ 标注解决，待 Research Director 确认。\"}\n    action_items:\n      - {round: 26, action: \"Table 2 caption 标注 matched-sparsity 来源\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 28 — New should-fix issues (no action taken yet)\n  # ============================================================\n\n  - id: \"R28-W3\"\n    summary: \"MSE 50% baseline 仅 s42 有效（s123 catastrophic PPL=15,789），作为 baseline 不可信\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。2/3 seed 失败说明 MSE 在 50% 下不稳定。Table 4 已有 § 标注但仍在主表中。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W4\"\n    summary: \"30% 下缺少 BCE isocompute (2700 steps) 对比\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。BCE isocompute 仅在 50% 下有 3-seed。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W5\"\n    summary: \"主评估指标单一（WikiText-2 PPL），C4 OOD 不充分\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 R1 列为 W5，R2 AGREE。WikiText-2 与 WikiText-103 同源。C4 OOD 30% 仅 2-seed。Uniform 3-seed CV=6.3% vs in-domain 0.2%。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Resolved (older rounds, carried forward)\n  # ============================================================\n\n  - id: \"R25-W1\"\n    summary: \"BCE 30% uniform 对比已补充\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Table 2 已加 BCE 30% uniform (PPL=15.09±0.13, 3-seed)。\"\n    resolution_round: 27\n\n  - id: \"R25-M1\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 27\n    resolution: \"全文统一为 output-distribution KL。Reviewer 验证 PASS。\"\n    resolution_round: 27\n\n  - id: \"R27-W4\"\n    summary: \"Contribution framing 存在 empirical study vs method 张力\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 27\n    last_seen_round: 27\n    resolution: \"4 个 contribution items 加 Empirical/Practical 标签。Reviewer 验证 PASS。\"\n    resolution_round: 27\n\n  - id: \"R27-W5\"\n    summary: \"Wall-clock speedup 缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 R2 将其与 'Practical' 标签合并为新 issue R28-W2。论文已充分 framed 为 empirical study。\"}\n    resolution: \"结构性限制。论文已充分 framed 为 empirical study。多轮维持 resolved。\"\n    resolution_round: 23\n\n  - id: \"R25-W2\"\n    summary: \"MSE 50% baseline 仅 seed 42 有效\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 升级为新 issue R28-W3（不可信 baseline）。\"}\n    resolution: \"Table 3 caption 有 § 标注，method.tex 有 '(50%: s42 only)'。但 R28 认为不够，升级为 R28-W3。\"\n    resolution_round: 27\n\n  - id: \"R26-M3\"\n    summary: \"68% divergence 和 32% Jaccard 同句混淆\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 27\n    resolution: \"Introduction 统一使用 Jaccard distance。Reviewer 验证 PASS。\"\n    resolution_round: 27\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 27\n    resolution: \"论文已充分 framed 为 empirical study。\"\n    resolution_round: 23\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度关键空白\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。Base model 不适用生成评估。\"\n    resolution_round: 25\n\n  - id: \"R24-W4\"\n    summary: \"'Primary design dimension' 需限定\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 27\n    resolution: \"合并入 R27-C2。Conclusion 已限定为 'for perplexity and commonsense at moderate sparsity'。\"\n    resolution_round: 27\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 26\n    resolution: \"R26/R27 未再提出。\"\n    resolution_round: 27\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 25\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 26\n    resolution: \"Appendix D OOD 证据充分。\"\n    resolution_round: 25\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 sparsity mismatch 脚注\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    resolution: \"§4.1 matched 14.5% 独立句。\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 27\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 25\n\n  - id: \"R25-W3\"\n    summary: \"Introduction 19% 已修正为 14.5%\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"数值已修正。\"\n    resolution_round: 26\n\n  - id: \"R25-M2\"\n    summary: \"Eq. 4 s_j 缺层标\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 25\n    resolution: \"已补充。\"\n    resolution_round: 25\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    resolution: \"C1 claim 已降级为 transferability。\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已拆分。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"BoolQ → HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 25\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 23\n\n  - id: \"R26-M1\"\n    summary: \"Introduction 中 8.6%/6.4% 未标注 sparsity level\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"§4.3 已加 sparsity level 标注。\"\n    resolution_round: 26\n\n  - id: \"R26-M2\"\n    summary: \"'stable downstream' 措辞\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"Introduction 已删除 'stable'。\"\n    resolution_round: 26",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "59e0218b-b140-4f62-95b8-80f14f28d628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 63 · 2026-05-24T04:22:33.260Z_

```json
{
  "parentUuid": "7f8f7bab-73e7-4528-9108-f59b9d0277e8",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "110c7c4d-829f-41e2-9aec-fb8cd9fe85d3",
  "timestamp": "2026-05-24T04:22:33.260Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: distill_sparse_swiglu - 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR - 截止日期…",
  "leafUuid": "110c7c4d-829f-41e2-9aec-fb8cd9fe85d3",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Assistant

_source line 66 · 2026-05-24T04:23:07.250Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also read the references.bib to check the citations, and check the PDF.

Let me now summarize the status and proceed to the review flow:

**Paper**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026 (via ARR)
**Deadline**: May 25, 2026 (tomorrow!)
**Today**: May 24, 2026

**Venue requirements** (from web search):
- Long paper: 8 pages content + unlimited references


- Mandatory limitations section (doesn't count toward page limit)
- Double-blind review
- ACL template with [review] option
- No anonymity period requirement

**Paper structure**:
- main.tex with \usepackage[review]{acl} ✓
- Author: "Anonymous" ✓
- Sections: abstract, introduction, related_work, method, experiments, conclusion, limitations, appendix
- Ethics section commented out

**Review mode**: fresh (no prior memory)

For this EMNLP 2026 submission, I'll assign two reviewers—one focusing on methodological rigor and experimental design, the other on novelty and contribution.

Now I'm checking whether this is truly a fresh review or if I should reference prior feedback. The system message indicates review approval has been granted and submission received, but it doesn't explicitly trigger the fresh review protocol, so I need to be careful about whether to treat previous issues as context or start completely anew.

Looking at the CLAUDE.md guidelines, fresh mode means conducting an independent review without bias from earlier rounds, even though I've already seen the historical issues. I'll do a clean evaluation now and reconcile with the existing tracker later when updating.

I've confirmed the paper is accessible and EMNLP 2026 is the target venue, so I'm ready to begin the actual review. I'm going back and forth on the external review configuration—I should just check the project settings directly rather than speculating. Let me move forward with dispatching the reviewers and generating my report for Group C while I verify the external review status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "110c7c4d-829f-41e2-9aec-fb8cd9fe85d3",
  "isSidechain": false,
  "requestId": "req_011CbLkkLUo5Y4tmJGyUbF3H",
  "type": "assistant",
  "uuid": "ab6d73a7-6eda-4920-9907-481b47d05397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTwm7yPGm1g8vo5XVw6hUR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42950,
      "cache_read_input_tokens": 40936,
      "output_tokens": 1319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1319,
          "cache_read_input_tokens": 40936,
          "cache_creation_input_tokens": 42950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42950
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-24T04:23:07.253Z_

论文已读取完毕。现在检查外部审稿配置并准备派发 Reviewer。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab6d73a7-6eda-4920-9907-481b47d05397",
  "isSidechain": false,
  "requestId": "req_011CbLkkLUo5Y4tmJGyUbF3H",
  "type": "assistant",
  "uuid": "437835e3-c3b8-416a-a742-56c4d5b7b1c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTwm7yPGm1g8vo5XVw6hUR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42950,
      "cache_read_input_tokens": 40936,
      "output_tokens": 1319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1319,
          "cache_read_input_tokens": 40936,
          "cache_creation_input_tokens": 42950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42950
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-24T04:23:09.655Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013KTRceEL3kpCUKt4qwr41m`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_CONFIG_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "437835e3-c3b8-416a-a742-56c4d5b7b1c8",
  "isSidechain": false,
  "requestId": "req_011CbLkkLUo5Y4tmJGyUbF3H",
  "type": "assistant",
  "uuid": "422ba669-7d75-4bad-b419-f1e4c93dadf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTwm7yPGm1g8vo5XVw6hUR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42950,
      "cache_read_input_tokens": 40936,
      "output_tokens": 1319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1319,
          "cache_read_input_tokens": 40936,
          "cache_creation_input_tokens": 42950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42950
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-24T04:23:10.163Z_

<details><summary>↩ Tool result · `toolu_01YMoxcTzSPyWF5YqMnhLkko`</summary>

```text
1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@article{zheng2026acttail,
6	  title={{ActTail}: Heavy-Tailed Self-Regularization for Activation Sparsity in Large Language Models},
7	  author={Zheng, Haocheng and others},
8	  journal={arXiv preprint arXiv:2603.12272},
9	  year={2026}
10	}
11	
12	@article{yang2026wisparse,
13	  title={{WiSparse}: Weight-Aware Mixed Activation Sparsity for Large Language Models},
14	  author={Yang, others},
15	  journal={arXiv preprint arXiv:2602.14452},
16	  year={2026}
17	}
18	
19	@article{huang2025larosa,
20	  title={La{R}o{SA}: Accelerating Large Language Model Inference with Layerwise Rotated Sparse Activation},
21	  author={Huang, Fangcheng and others},
22	  journal={arXiv preprint arXiv:2507.01299},
23	  year={2025}
24	}
25	
26	@inproceedings{geva2023dissecting,
27	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
28	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
29	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
30	  pages = {12216--12235},
31	  year = {2023},
32	}
33	
34	@article{fu2024lazyllm,
35	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
36	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
37	  year = {2024},
38	  journal = {arXiv preprint arXiv:2407.14057},
39	}
40	
41	@article{zhang2025cots,
42	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
43	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
44	  year = {2025},
45	  journal = {arXiv preprint arXiv:2502.14475},
46	}
47	
48	@inproceedings{alizadeh2024llmflash,
49	  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},
50	  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},
51	  year = {2024},
52	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
53	}
54	
55	@article{wei2023outlier,
56	  title = {Outlier Suppression+: Accurate Quantization of Large Language Models by Equivalent and Effective Shifting and Scaling},
57	  author = {Xiuying Wei and Yunchen Zhang and Yuhang Li and Xiangguo Zhang and Ruihao Gong and Jinyang Guo and Xianglong Liu},
58	  year = {2023},
59	  journal = {arXiv preprint arXiv:2304.09145},
60	}
61	
62	% =============================================================================
63	% Direction 1: KL distillation for structured/activation sparsity
64	% =============================================================================
65	
66	@inproceedings{fang2024maskllm,
67	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
68	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
69	  year = {2024},
70	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
71	  url = {https://arxiv.org/abs/2409.17481},
72	}
73	
74	@inproceedings{xu2025spon,
75	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
76	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
77	  year = {2025},
78	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
79	  url = {https://arxiv.org/abs/2512.12744},
80	}
81	
82	@inproceedings{muralidharan2024minitron,
83	  title = {Compact Language Models via Pruning and Knowledge Distillation},
84	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
85	  year = {2024},
86	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
87	  url = {https://arxiv.org/abs/2407.14679},
88	}
89	
90	
91	% =============================================================================
92	% Direction 3: SPON and learnable bias correction for sparsity
93	% =============================================================================
94	
95	@article{gautam2026fastforward,
96	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
97	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},
98	  year = {2026},
99	  journal = {arXiv preprint arXiv:2602.00397},
100	  url = {https://arxiv.org/abs/2602.00397},
101	}
102	
103	
104	% =============================================================================
105	% Direction 4: Predictor-based activation sparsity
106	% =============================================================================
107	
108	@inproceedings{liu2025teal,
109	  title = {Training-Free Activation Sparsity in Large Language Models},
110	  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},
111	  year = {2025},
112	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
113	  url = {https://arxiv.org/abs/2408.14690},
114	}
115	
116	@inproceedings{liu2023dejavu,
117	  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},
118	  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},
119	  year = {2023},
120	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
121	  url = {https://arxiv.org/abs/2310.17157},
122	}
123	
124	@inproceedings{akhauri2024shadowllm,
125	  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},
126	  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},
127	  year = {2024},
128	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
129	  url = {https://arxiv.org/abs/2406.16635},
130	}
131	
132	
133	@article{lee2024cats,
134	  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},
135	  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},
136	  year = {2024},
137	  journal = {arXiv preprint arXiv:2404.08763},
138	  url = {https://arxiv.org/abs/2404.08763},
139	}
140	
141	@inproceedings{zhang2025rsparse,
142	  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},
143	  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},
144	  year = {2025},
145	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
146	  url = {https://arxiv.org/abs/2504.19449},
147	}
148	
149	@inproceedings{federici2025dip,
150	  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},
151	  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},
152	  year = {2024},
153	  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},
154	  url = {https://arxiv.org/abs/2412.01380},
155	}
156	
157	@inproceedings{shin2025sparseinfer,
158	  title = {SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference},
159	  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},
160	  year = {2025},
161	  booktitle = {Proceedings of the Design, Automation \& Test in Europe Conference (DATE)},
162	  url = {https://arxiv.org/abs/2411.12692},
163	}
164	
165	@inproceedings{shin2025grasp,
166	  title = {{GRASP}: Group-Based Prediction of Activation Sparsity for Fast {LLM} Inference},
167	  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},
168	  year = {2025},
169	  booktitle = {Proceedings of the 62nd ACM/IEEE Design Automation Conference (DAC)},
170	  url = {https://dl.acm.org/doi/10.1109/DAC63849.2025.11132899},
171	}
172	
173	@article{serbin2026svdcsp,
174	  title = {SVD Contextual Sparsity Predictors for Fast LLM Inference},
175	  author = {Georgii Serbin and Kirill Koshkin and Zhongao Sun and Anastasiya Bistrigova and C.C. Korikov},
176	  year = {2026},
177	  journal = {arXiv preprint arXiv:2603.14110},
178	  url = {https://arxiv.org/abs/2603.14110},
179	}
180	
181	@inproceedings{dhar2025clustering,
182	  title = {A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering},
183	  author = {Nobel Dhar and Bobin Deng and Md Romyull Islam and Xinyue Zhang and Kazi Fahim Ahmad Nasif and Kun Suo},
184	  year = {2025},
185	  booktitle = {Proceedings of the International Conference on Parallel Processing (Euro-Par)},
186	  url = {https://arxiv.org/abs/2507.14179},
187	}
188	
189	% =============================================================================
190	% Activation function replacement and sparsity enhancement
191	% =============================================================================
192	
193	@inproceedings{mirzadeh2024relu,
194	  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},
195	  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},
196	  year = {2024},
197	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
198	  url = {https://arxiv.org/abs/2310.04564},
199	}
200	
201	@article{song2024turbosparse,
202	  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},
203	  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},
204	  year = {2024},
205	  journal = {arXiv preprint arXiv:2406.05955},
206	  url = {https://arxiv.org/abs/2406.05955},
207	}
208	
209	@inproceedings{song2025prosparse,
210	  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},
211	  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},
212	  year = {2025},
213	  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},
214	  url = {https://arxiv.org/abs/2402.13516},
215	}
216	
217	@article{luo2024sparsinglaw,
218	  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},
219	  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},
220	  year = {2024},
221	  journal = {arXiv preprint arXiv:2411.02335},
222	  url = {https://arxiv.org/abs/2411.02335},
223	}
224	
225	@article{wu2025moc,
226	  title = {Mixture-of-Channels: Exploiting Sparse {FFN}s for Efficient {LLM}s Pre-Training and Inference},
227	  author = {Tong Wu and Yutong He and Bin Wang and Kun Yuan},
228	  year = {2025},
229	  journal = {arXiv preprint arXiv:2511.09323},
230	  url = {https://arxiv.org/abs/2511.09323},
231	}
232	
233	
234	@inproceedings{song2024powerinfer,
235	  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},
236	  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},
237	  year = {2024},
238	  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},
239	  url = {https://arxiv.org/abs/2312.12456},
240	}
241	
242	
243	% =============================================================================
244	% KL distillation and knowledge distillation
245	% =============================================================================
246	
247	@inproceedings{kim2016sequencekd,
248	  title = {Sequence-Level Knowledge Distillation},
249	  author = {Yoon Kim and Alexander M. Rush},
250	  year = {2016},
251	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
252	  url = {https://arxiv.org/abs/1606.07947},
253	}
254	
255	@inproceedings{gu2024minillm,
256	  title = {MiniLLM: Knowledge Distillation of Large Language Models},
257	  author = {Yuxian Gu and Li Dong and Furu Wei and Minlie Huang},
258	  year = {2024},
259	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
260	  url = {https://openreview.net/forum?id=5h0qf7IBZZ},
261	}
262	
263	@inproceedings{agarwal2024gkd,
264	  title = {On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes},
265	  author = {Rishabh Agarwal and Nino Vieillard and Yongchao Zhou and Piotr Stanczyk and Sabela Ramos and Matthieu Geist and Olivier Bachem},
266	  year = {2024},
267	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
268	  url = {https://openreview.net/forum?id=3zKtaqxLhW},
269	}
270	
271	@inproceedings{khaki2025sparselora,
272	  title = {SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity},
273	  author = {Samir Khaki and Xiuyu Li and Junxian Guo and Ligeng Zhu and Konstantinos N. Plataniotis and Amir Yazdanbakhsh and Kurt Keutzer and Song Han and Zhijian Liu},
274	  year = {2025},
275	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
276	  url = {https://proceedings.mlr.press/v267/khaki25a.html},
277	}
278	
279	@article{raposo2024mod,
280	  title = {Mixture-of-Depths: Dynamically allocating compute in transformer-based language models},
281	  author = {David Raposo and Sam Ritter and Blake Richards and Timothy Lillicrap and Peter Conway Humphreys and Adam Santoro},
282	  year = {2024},
283	  journal = {arXiv preprint arXiv:2404.02258},
284	  url = {https://arxiv.org/abs/2404.02258},
285	}
286	
287	@article{sanh2019distilbert,
288	  title = {DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
289	  author = {Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
290	  year = {2019},
291	  journal = {arXiv preprint arXiv:1910.01108},
292	  url = {https://arxiv.org/abs/1910.01108},
293	}
294	
295	% =============================================================================
296	% Weight pruning methods
297	% =============================================================================
298	
299	@inproceedings{sun2024wanda,
300	  title = {A Simple and Effective Pruning Approach for Large Language Models},
301	  author = {Mingjie Sun and Zhuang Liu and Anna Bair and J. Zico Kolter},
302	  year = {2024},
303	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
304	  url = {https://arxiv.org/abs/2306.11695},
305	}
306	
307	@inproceedings{frantar2023sparsegpt,
308	  title = {SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot},
309	  author = {Elias Frantar and Dan Alistarh},
310	  year = {2023},
311	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
312	  url = {https://arxiv.org/abs/2301.00774},
313	}
314	
315	@inproceedings{ashkboos2024slicegpt,
316	  title = {SliceGPT: Compress Large Language Models by Deleting Rows and Columns},
317	  author = {Saleh Ashkboos and Maximilian L. Croci and Marcelo Gennari do Nascimento and Torsten Hoefler and James Hensman},
318	  year = {2024},
319	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
320	  url = {https://arxiv.org/abs/2401.15024},
321	}
322	
323	@inproceedings{shrestha2025polar,
324	  title = {Polar Sparsity: High Throughput Batched {LLM} Inferencing with Scalable Contextual Sparsity},
325	  author = {Susav Shrestha and Brian Settlemyer and Joel Dapello and Peng Chen},
326	  year = {2025},
327	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
328	  url = {https://arxiv.org/abs/2505.14884},
329	}
330	
331	@inproceedings{ko2024distillm,
332	  title = {DistiLLM: Towards Streamlined Distillation for Large Language Models},
333	  author = {Jongwoo Ko and Sungnyun Kim and Tianyi Chen and Se-Young Yun},
334	  year = {2024},
335	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
336	  url = {https://arxiv.org/abs/2402.03898},
337	}
338	
339	@inproceedings{yin2024owl,
340	  title = {Outlier Weighed Layerwise Sparsity ({OWL}): A Missing Secret Sauce for Pruning {LLM}s to High Sparsity},
341	  author = {Lu Yin and You Wu and Zhenyu Zhang and Cheng-Yu Hsieh and Yaqing Wang and Yiling Jia and Gen Li and Ajay Jaiswal and Mykola Pechenizkiy and Yi Liang and Michael Bendersky and Zhangyang Wang and Shiwei Liu},
342	  year = {2024},
343	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
344	  url = {https://arxiv.org/abs/2310.05175},
345	}
346	
347	@article{wang2025dynamicsparse,
348	  title = {Enabling Dynamic Sparsity in Quantized {LLM} Inference},
349	  author = {Rongxiang Wang and Kangyuan Shu and Felix Xiaozhu Lin},
350	  year = {2025},
351	  journal = {arXiv preprint arXiv:2511.04477},
352	  url = {https://arxiv.org/abs/2511.04477},
353	}
354	
355	@article{cheng2025mone,
356	  title = {Mixture of Neuron Experts},
357	  author = {Runxi Cheng and Yuchen Guan and Yucheng Ding and Qingguo Hu and Yongxian Wei and Chun Yuan and Yelong Shen and Weizhu Chen and Yeyun Gong},
358	  year = {2025},
359	  journal = {arXiv preprint arXiv:2510.05781},
360	  url = {https://arxiv.org/abs/2510.05781},
361	}
362	
363	% =============================================================================
364	% Conditional computation and MoE
365	% =============================================================================
366	
367	@inproceedings{szatkowski2024d2dmoe,
368	  title = {Exploiting Activation Sparsity with Dense to Dynamic-$k$ Mixture-of-Experts Conversion},
369	  author = {Filip Szatkowski and Bartosz W{\'o}jcik and Miko{\l}aj Pi{\'o}rczy{\'n}ski and Simone Scardapane},
370	  year = {2024},
371	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
372	  volume = {37},
373	  url = {https://arxiv.org/abs/2310.04361},
374	}
375	
376	@article{fedus2022switch,
377	  title = {Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},
378	  author = {William Fedus and Barret Zoph and Noam Shazeer},
379	  year = {2022},
380	  journal = {Journal of Machine Learning Research},
381	  volume = {23},
382	  number = {120},
383	  pages = {1--40},
384	  url = {https://arxiv.org/abs/2101.03961},
385	}
386	
387	% =============================================================================
388	% MoE routing and gated architectures
389	% =============================================================================
390	
391	@inproceedings{zhou2022expertchoice,
392	  title = {Mixture-of-Experts with Expert Choice Routing},
393	  author = {Yanqi Zhou and Tao Lei and Hanxiao Liu and Nan Du and Yanping Huang and Vincent Zhao and Andrew M. Dai and Zhifeng Chen and Quoc V. Le and James Laudon},
394	  year = {2022},
395	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
396	  volume = {35},
397	  url = {https://arxiv.org/abs/2202.09368},
398	}
399	
400	% =============================================================================
401	% Relaxation methods (Gumbel/Concrete)
402	% =============================================================================
403	
404	@inproceedings{louizos2018l0,
405	  title = {Learning Sparse Neural Networks through $L_0$ Regularization},
406	  author = {Christos Louizos and Max Welling and Diederik P. Kingma},
407	  year = {2018},
408	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
409	  url = {https://arxiv.org/abs/1712.01312},
410	}
411	
412	@inproceedings{maddison2017concrete,
413	  title = {The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables},
414	  author = {Chris J. Maddison and Andriy Mnih and Yee Whye Teh},
415	  year = {2017},
416	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
417	  url = {https://arxiv.org/abs/1611.00712},
418	}
419	
420	% =============================================================================
421	% Foundational references
422	% =============================================================================
423	
424	@article{grattafiori2024llama3,
425	  title = {The Llama 3 Herd of Models},
426	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},
427	  year = {2024},
428	  journal = {arXiv preprint arXiv:2407.21783},
429	  url = {https://arxiv.org/abs/2407.21783},
430	}
431	
432	@article{qwen2024qwen25,
433	  title = {Qwen2.5 Technical Report},
434	  author = {Qwen Team},
435	  year = {2024},
436	  journal = {arXiv preprint arXiv:2412.15115},
437	  url = {https://arxiv.org/abs/2412.15115},
438	}
439	
440	@article{jiang2023mistral,
441	  title = {Mistral 7B},
442	  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},
443	  year = {2023},
444	  journal = {arXiv preprint arXiv:2310.06825},
445	  url = {https://arxiv.org/abs/2310.06825},
446	}
447	
448	@inproceedings{jang2017gumbel,
449	  title = {Categorical Reparameterization with Gumbel-Softmax},
450	  author = {Eric Jang and Shixiang Gu and Ben Poole},
451	  year = {2017},
452	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
453	  url = {https://arxiv.org/abs/1611.01144},
454	}
455	
456	@article{shazeer2020glu,
457	  title = {GLU Variants Improve Transformer},
458	  author = {Noam Shazeer},
459	  year = {2020},
460	  journal = {arXiv preprint arXiv:2002.05202},
461	  url = {https://arxiv.org/abs/2002.05202},
462	}
463	
464	@inproceedings{meng2022locating,
465	  title = {Locating and Editing Factual Associations in {GPT}},
466	  author = {Kevin Meng and David Bau and Alex Andonian and Yonatan Belinkov},
467	  year = {2022},
468	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
469	  url = {https://arxiv.org/abs/2202.05262},
470	}
471	
472	@inproceedings{merity2017pointer,
473	  title = {Pointer Sentinel Mixture Models},
474	  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},
475	  year = {2017},
476	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
477	  url = {https://arxiv.org/abs/1609.07843},
478	}
479	
480	@inproceedings{hinton2015distilling,
481	  title = {Distilling the Knowledge in a Neural Network},
482	  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},
483	  year = {2015},
484	  booktitle = {NeurIPS 2014 Deep Learning Workshop},
485	  url = {https://arxiv.org/abs/1503.02531},
486	}
487	
488	@article{bengio2013ste,
489	  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},
490	  author = {Yoshua Bengio and Nicholas L\'{e}onard and Aaron Courville},
491	  year = {2013},
492	  journal = {arXiv preprint arXiv:1308.3432},
493	  url = {https://arxiv.org/abs/1308.3432},
494	}
495	
496	@inproceedings{loshchilov2019adamw,
497	  title = {Decoupled Weight Decay Regularization},
498	  author = {Ilya Loshchilov and Frank Hutter},
499	  year = {2019},
500	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
501	  url = {https://arxiv.org/abs/1711.05101},
502	}
503	
504	@article{raffel2020c4,
505	  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
506	  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
507	  year = {2020},
508	  journal = {Journal of Machine Learning Research},
509	  volume = {21},
510	  number = {140},
511	  pages = {1--67},
512	  url = {https://arxiv.org/abs/1910.10683},
513	}
514	
515	@inproceedings{wu2025rethinking,
516	  title = {Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models},
517	  author = {Taiqiang Wu and Chaofan Tao and Jiahao Wang and Runming Yang and Zhe Zhao and Ngai Wong},
518	  year = {2025},
519	  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},
520	  url = {https://arxiv.org/abs/2404.02657},
521	}
522	
523	@article{dhar2024activation,
524	  title = {Activation Sparsity Opportunities for Compressing General Large Language Models},
525	  author = {Nobel Dhar and Bobin Deng and Md Romyull Islam and Kazi Fahim Ahmad Nasif and Liang Zhao and Kun Suo},
526	  year = {2024},
527	  journal = {arXiv preprint arXiv:2412.12178},
528	  url = {https://arxiv.org/abs/2412.12178},
529	}
530	
531	@article{xue2024powerinfer2,
532	  title = {PowerInfer-2: Fast Large Language Model Inference on a Smartphone},
533	  author = {Zhiyuan Xue and Yixin Song and Zeyu Mi and Le Chen and Yubin Xia and Haibo Chen},
534	  year = {2024},
535	  journal = {arXiv preprint arXiv:2406.06282},
536	  url = {https://arxiv.org/abs/2406.06282},
537	}
538	
539	@inproceedings{lin2024awq,
540	  title = {{AWQ}: Activation-Aware Weight Quantization for {LLM} Compression and Acceleration},
541	  author = {Ji Lin and Jiaming Tang and Haotian Tang and Shang Yang and Wei-Ming Chen and Wei-Chen Wang and Guangxuan Xiao and Xingyu Dang and Chuang Gan and Song Han},
542	  year = {2024},
543	  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},
544	  url = {https://arxiv.org/abs/2306.00978},
545	}
546	
547	@article{haziza2025accelerating,
548	  title = {Accelerating Transformer Inference and Training with 2:4 Activation Sparsity},
549	  author = {Daniel Haziza and Timothy Chou and Dhruv Choudhary and Luca Wehrstedt and Francisco Massa and Jiecao Yu and Geonhwa Jeong and Supriya Rao and Patrick Labatut and Jesse Cai},
550	  year = {2025},
551	  journal = {arXiv preprint arXiv:2503.16672},
552	  url = {https://arxiv.org/abs/2503.16672},
553	}
554	
555	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04a835a4-35c6-412d-baeb-1cdd62a9208f",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "1eecd899-fa77-472f-b0d0-e2d801a86ad9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
      "content": "% =============================================================================\n% Additional references (R20 review response)\n% =============================================================================\n\n@article{zheng2026acttail,\n  title={{ActTail}: Heavy-Tailed Self-Regularization for Activation Sparsity in Large Language Models},\n  author={Zheng, Haocheng and others},\n  journal={arXiv preprint arXiv:2603.12272},\n  year={2026}\n}\n\n@article{yang2026wisparse,\n  title={{WiSparse}: Weight-Aware Mixed Activation Sparsity for Large Language Models},\n  author={Yang, others},\n  journal={arXiv preprint arXiv:2602.14452},\n  year={2026}\n}\n\n@article{huang2025larosa,\n  title={La{R}o{SA}: Accelerating Large Language Model Inference with Layerwise Rotated Sparse Activation},\n  author={Huang, Fangcheng and others},\n  journal={arXiv preprint arXiv:2507.01299},\n  year={2025}\n}\n\n@inproceedings{geva2023dissecting,\n  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},\n  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {12216--12235},\n  year = {2023},\n}\n\n@article{fu2024lazyllm,\n  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},\n  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2407.14057},\n}\n\n@article{zhang2025cots,\n  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},\n  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2502.14475},\n}\n\n@inproceedings{alizadeh2024llmflash,\n  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},\n  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},\n  year = {2024},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n}\n\n@article{wei2023outlier,\n  title = {Outlier Suppression+: Accurate Quantization of Large Language Models by Equivalent and Effective Shifting and Scaling},\n  author = {Xiuying Wei and Yunchen Zhang and Yuhang Li and Xiangguo Zhang and Ruihao Gong and Jinyang Guo and Xianglong Liu},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2304.09145},\n}\n\n% =============================================================================\n% Direction 1: KL distillation for structured/activation sparsity\n% =============================================================================\n\n@inproceedings{fang2024maskllm,\n  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},\n  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2409.17481},\n}\n\n@inproceedings{xu2025spon,\n  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},\n  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2512.12744},\n}\n\n@inproceedings{muralidharan2024minitron,\n  title = {Compact Language Models via Pruning and Knowledge Distillation},\n  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2407.14679},\n}\n\n\n% =============================================================================\n% Direction 3: SPON and learnable bias correction for sparsity\n% =============================================================================\n\n@article{gautam2026fastforward,\n  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},\n  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2602.00397},\n  url = {https://arxiv.org/abs/2602.00397},\n}\n\n\n% =============================================================================\n% Direction 4: Predictor-based activation sparsity\n% =============================================================================\n\n@inproceedings{liu2025teal,\n  title = {Training-Free Activation Sparsity in Large Language Models},\n  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2408.14690},\n}\n\n@inproceedings{liu2023dejavu,\n  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},\n  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},\n  year = {2023},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2310.17157},\n}\n\n@inproceedings{akhauri2024shadowllm,\n  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},\n  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},\n  year = {2024},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  url = {https://arxiv.org/abs/2406.16635},\n}\n\n\n@article{lee2024cats,\n  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},\n  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2404.08763},\n  url = {https://arxiv.org/abs/2404.08763},\n}\n\n@inproceedings{zhang2025rsparse,\n  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},\n  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2504.19449},\n}\n\n@inproceedings{federici2025dip,\n  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},\n  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},\n  year = {2024},\n  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},\n  url = {https://arxiv.org/abs/2412.01380},\n}\n\n@inproceedings{shin2025sparseinfer,\n  title = {SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference},\n  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},\n  year = {2025},\n  booktitle = {Proceedings of the Design, Automation \\& Test in Europe Conference (DATE)},\n  url = {https://arxiv.org/abs/2411.12692},\n}\n\n@inproceedings{shin2025grasp,\n  title = {{GRASP}: Group-Based Prediction of Activation Sparsity for Fast {LLM} Inference},\n  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},\n  year = {2025},\n  booktitle = {Proceedings of the 62nd ACM/IEEE Design Automation Conference (DAC)},\n  url = {https://dl.acm.org/doi/10.1109/DAC63849.2025.11132899},\n}\n\n@article{serbin2026svdcsp,\n  title = {SVD Contextual Sparsity Predictors for Fast LLM Inference},\n  author = {Georgii Serbin and Kirill Koshkin and Zhongao Sun and Anastasiya Bistrigova and C.C. Korikov},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2603.14110},\n  url = {https://arxiv.org/abs/2603.14110},\n}\n\n@inproceedings{dhar2025clustering,\n  title = {A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering},\n  author = {Nobel Dhar and Bobin Deng and Md Romyull Islam and Xinyue Zhang and Kazi Fahim Ahmad Nasif and Kun Suo},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Parallel Processing (Euro-Par)},\n  url = {https://arxiv.org/abs/2507.14179},\n}\n\n% =============================================================================\n% Activation function replacement and sparsity enhancement\n% =============================================================================\n\n@inproceedings{mirzadeh2024relu,\n  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},\n  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2310.04564},\n}\n\n@article{song2024turbosparse,\n  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},\n  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2406.05955},\n  url = {https://arxiv.org/abs/2406.05955},\n}\n\n@inproceedings{song2025prosparse,\n  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},\n  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2402.13516},\n}\n\n@article{luo2024sparsinglaw,\n  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},\n  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2411.02335},\n  url = {https://arxiv.org/abs/2411.02335},\n}\n\n@article{wu2025moc,\n  title = {Mixture-of-Channels: Exploiting Sparse {FFN}s for Efficient {LLM}s Pre-Training and Inference},\n  author = {Tong Wu and Yutong He and Bin Wang and Kun Yuan},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2511.09323},\n  url = {https://arxiv.org/abs/2511.09323},\n}\n\n\n@inproceedings{song2024powerinfer,\n  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},\n  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},\n  year = {2024},\n  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},\n  url = {https://arxiv.org/abs/2312.12456},\n}\n\n\n% =============================================================================\n% KL distillation and knowledge distillation\n% =============================================================================\n\n@inproceedings{kim2016sequencekd,\n  title = {Sequence-Level Knowledge Distillation},\n  author = {Yoon Kim and Alexander M. Rush},\n  year = {2016},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  url = {https://arxiv.org/abs/1606.07947},\n}\n\n@inproceedings{gu2024minillm,\n  title = {MiniLLM: Knowledge Distillation of Large Language Models},\n  author = {Yuxian Gu and Li Dong and Furu Wei and Minlie Huang},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://openreview.net/forum?id=5h0qf7IBZZ},\n}\n\n@inproceedings{agarwal2024gkd,\n  title = {On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes},\n  author = {Rishabh Agarwal and Nino Vieillard and Yongchao Zhou and Piotr Stanczyk and Sabela Ramos and Matthieu Geist and Olivier Bachem},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://openreview.net/forum?id=3zKtaqxLhW},\n}\n\n@inproceedings{khaki2025sparselora,\n  title = {SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity},\n  author = {Samir Khaki and Xiuyu Li and Junxian Guo and Ligeng Zhu and Konstantinos N. Plataniotis and Amir Yazdanbakhsh and Kurt Keutzer and Song Han and Zhijian Liu},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://proceedings.mlr.press/v267/khaki25a.html},\n}\n\n@article{raposo2024mod,\n  title = {Mixture-of-Depths: Dynamically allocating compute in transformer-based language models},\n  author = {David Raposo and Sam Ritter and Blake Richards and Timothy Lillicrap and Peter Conway Humphreys and Adam Santoro},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2404.02258},\n  url = {https://arxiv.org/abs/2404.02258},\n}\n\n@article{sanh2019distilbert,\n  title = {DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},\n  author = {Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},\n  year = {2019},\n  journal = {arXiv preprint arXiv:1910.01108},\n  url = {https://arxiv.org/abs/1910.01108},\n}\n\n% =============================================================================\n% Weight pruning methods\n% =============================================================================\n\n@inproceedings{sun2024wanda,\n  title = {A Simple and Effective Pruning Approach for Large Language Models},\n  author = {Mingjie Sun and Zhuang Liu and Anna Bair and J. Zico Kolter},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2306.11695},\n}\n\n@inproceedings{frantar2023sparsegpt,\n  title = {SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot},\n  author = {Elias Frantar and Dan Alistarh},\n  year = {2023},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2301.00774},\n}\n\n@inproceedings{ashkboos2024slicegpt,\n  title = {SliceGPT: Compress Large Language Models by Deleting Rows and Columns},\n  author = {Saleh Ashkboos and Maximilian L. Croci and Marcelo Gennari do Nascimento and Torsten Hoefler and James Hensman},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2401.15024},\n}\n\n@inproceedings{shrestha2025polar,\n  title = {Polar Sparsity: High Throughput Batched {LLM} Inferencing with Scalable Contextual Sparsity},\n  author = {Susav Shrestha and Brian Settlemyer and Joel Dapello and Peng Chen},\n  year = {2025},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2505.14884},\n}\n\n@inproceedings{ko2024distillm,\n  title = {DistiLLM: Towards Streamlined Distillation for Large Language Models},\n  author = {Jongwoo Ko and Sungnyun Kim and Tianyi Chen and Se-Young Yun},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2402.03898},\n}\n\n@inproceedings{yin2024owl,\n  title = {Outlier Weighed Layerwise Sparsity ({OWL}): A Missing Secret Sauce for Pruning {LLM}s to High Sparsity},\n  author = {Lu Yin and You Wu and Zhenyu Zhang and Cheng-Yu Hsieh and Yaqing Wang and Yiling Jia and Gen Li and Ajay Jaiswal and Mykola Pechenizkiy and Yi Liang and Michael Bendersky and Zhangyang Wang and Shiwei Liu},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2310.05175},\n}\n\n@article{wang2025dynamicsparse,\n  title = {Enabling Dynamic Sparsity in Quantized {LLM} Inference},\n  author = {Rongxiang Wang and Kangyuan Shu and Felix Xiaozhu Lin},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2511.04477},\n  url = {https://arxiv.org/abs/2511.04477},\n}\n\n@article{cheng2025mone,\n  title = {Mixture of Neuron Experts},\n  author = {Runxi Cheng and Yuchen Guan and Yucheng Ding and Qingguo Hu and Yongxian Wei and Chun Yuan and Yelong Shen and Weizhu Chen and Yeyun Gong},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2510.05781},\n  url = {https://arxiv.org/abs/2510.05781},\n}\n\n% =============================================================================\n% Conditional computation and MoE\n% =============================================================================\n\n@inproceedings{szatkowski2024d2dmoe,\n  title = {Exploiting Activation Sparsity with Dense to Dynamic-$k$ Mixture-of-Experts Conversion},\n  author = {Filip Szatkowski and Bartosz W{\\'o}jcik and Miko{\\l}aj Pi{\\'o}rczy{\\'n}ski and Simone Scardapane},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  volume = {37},\n  url = {https://arxiv.org/abs/2310.04361},\n}\n\n@article{fedus2022switch,\n  title = {Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},\n  author = {William Fedus and Barret Zoph and Noam Shazeer},\n  year = {2022},\n  journal = {Journal of Machine Learning Research},\n  volume = {23},\n  number = {120},\n  pages = {1--40},\n  url = {https://arxiv.org/abs/2101.03961},\n}\n\n% =============================================================================\n% MoE routing and gated architectures\n% =============================================================================\n\n@inproceedings{zhou2022expertchoice,\n  title = {Mixture-of-Experts with Expert Choice Routing},\n  author = {Yanqi Zhou and Tao Lei and Hanxiao Liu and Nan Du and Yanping Huang and Vincent Zhao and Andrew M. Dai and Zhifeng Chen and Quoc V. Le and James Laudon},\n  year = {2022},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  volume = {35},\n  url = {https://arxiv.org/abs/2202.09368},\n}\n\n% =============================================================================\n% Relaxation methods (Gumbel/Concrete)\n% =============================================================================\n\n@inproceedings{louizos2018l0,\n  title = {Learning Sparse Neural Networks through $L_0$ Regularization},\n  author = {Christos Louizos and Max Welling and Diederik P. Kingma},\n  year = {2018},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1712.01312},\n}\n\n@inproceedings{maddison2017concrete,\n  title = {The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables},\n  author = {Chris J. Maddison and Andriy Mnih and Yee Whye Teh},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1611.00712},\n}\n\n% =============================================================================\n% Foundational references\n% =============================================================================\n\n@article{grattafiori2024llama3,\n  title = {The Llama 3 Herd of Models},\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2407.21783},\n  url = {https://arxiv.org/abs/2407.21783},\n}\n\n@article{qwen2024qwen25,\n  title = {Qwen2.5 Technical Report},\n  author = {Qwen Team},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2412.15115},\n  url = {https://arxiv.org/abs/2412.15115},\n}\n\n@article{jiang2023mistral,\n  title = {Mistral 7B},\n  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2310.06825},\n  url = {https://arxiv.org/abs/2310.06825},\n}\n\n@inproceedings{jang2017gumbel,\n  title = {Categorical Reparameterization with Gumbel-Softmax},\n  author = {Eric Jang and Shixiang Gu and Ben Poole},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1611.01144},\n}\n\n@article{shazeer2020glu,\n  title = {GLU Variants Improve Transformer},\n  author = {Noam Shazeer},\n  year = {2020},\n  journal = {arXiv preprint arXiv:2002.05202},\n  url = {https://arxiv.org/abs/2002.05202},\n}\n\n@inproceedings{meng2022locating,\n  title = {Locating and Editing Factual Associations in {GPT}},\n  author = {Kevin Meng and David Bau and Alex Andonian and Yonatan Belinkov},\n  year = {2022},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2202.05262},\n}\n\n@inproceedings{merity2017pointer,\n  title = {Pointer Sentinel Mixture Models},\n  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1609.07843},\n}\n\n@inproceedings{hinton2015distilling,\n  title = {Distilling the Knowledge in a Neural Network},\n  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},\n  year = {2015},\n  booktitle = {NeurIPS 2014 Deep Learning Workshop},\n  url = {https://arxiv.org/abs/1503.02531},\n}\n\n@article{bengio2013ste,\n  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},\n  author = {Yoshua Bengio and Nicholas L\\'{e}onard and Aaron Courville},\n  year = {2013},\n  journal = {arXiv preprint arXiv:1308.3432},\n  url = {https://arxiv.org/abs/1308.3432},\n}\n\n@inproceedings{loshchilov2019adamw,\n  title = {Decoupled Weight Decay Regularization},\n  author = {Ilya Loshchilov and Frank Hutter},\n  year = {2019},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1711.05101},\n}\n\n@article{raffel2020c4,\n  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},\n  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},\n  year = {2020},\n  journal = {Journal of Machine Learning Research},\n  volume = {21},\n  number = {140},\n  pages = {1--67},\n  url = {https://arxiv.org/abs/1910.10683},\n}\n\n@inproceedings{wu2025rethinking,\n  title = {Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models},\n  author = {Taiqiang Wu and Chaofan Tao and Jiahao Wang and Runming Yang and Zhe Zhao and Ngai Wong},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2404.02657},\n}\n\n@article{dhar2024activation,\n  title = {Activation Sparsity Opportunities for Compressing General Large Language Models},\n  author = {Nobel Dhar and Bobin Deng and Md Romyull Islam and Kazi Fahim Ahmad Nasif and Liang Zhao and Kun Suo},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2412.12178},\n  url = {https://arxiv.org/abs/2412.12178},\n}\n\n@article{xue2024powerinfer2,\n  title = {PowerInfer-2: Fast Large Language Model Inference on a Smartphone},\n  author = {Zhiyuan Xue and Yixin Song and Zeyu Mi and Le Chen and Yubin Xia and Haibo Chen},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2406.06282},\n  url = {https://arxiv.org/abs/2406.06282},\n}\n\n@inproceedings{lin2024awq,\n  title = {{AWQ}: Activation-Aware Weight Quantization for {LLM} Compression and Acceleration},\n  author = {Ji Lin and Jiaming Tang and Haotian Tang and Shang Yang and Wei-Ming Chen and Wei-Chen Wang and Guangxuan Xiao and Xingyu Dang and Chuang Gan and Song Han},\n  year = {2024},\n  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},\n  url = {https://arxiv.org/abs/2306.00978},\n}\n\n@article{haziza2025accelerating,\n  title = {Accelerating Transformer Inference and Training with 2:4 Activation Sparsity},\n  author = {Daniel Haziza and Timothy Chou and Dhruv Choudhary and Luca Wehrstedt and Francisco Massa and Jiecao Yu and Geonhwa Jeong and Supriya Rao and Patrick Labatut and Jesse Cai},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2503.16672},\n  url = {https://arxiv.org/abs/2503.16672},\n}\n\n",
      "numLines": 555,
      "startLine": 1,
      "totalLines": 555
    }
  },
  "sourceToolAssistantUUID": "04a835a4-35c6-412d-baeb-1cdd62a9208f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-24T04:23:09.719Z_

<details><summary>↩ Tool result · `toolu_013KTRceEL3kpCUKt4qwr41m`</summary>

```text
NO_CONFIG_FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "422ba669-7d75-4bad-b419-f1e4c93dadf2",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "91b5d8e3-f978-4c5d-beb0-ac25571f5ca6",
  "toolUseResult": {
    "stdout": "NO_CONFIG_FOUND",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "422ba669-7d75-4bad-b419-f1e4c93dadf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-24T04:23:10.149Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YMoxcTzSPyWF5YqMnhLkko`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91b5d8e3-f978-4c5d-beb0-ac25571f5ca6",
  "isSidechain": false,
  "requestId": "req_011CbLkkLUo5Y4tmJGyUbF3H",
  "type": "assistant",
  "uuid": "04a835a4-35c6-412d-baeb-1cdd62a9208f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTwm7yPGm1g8vo5XVw6hUR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42950,
      "cache_read_input_tokens": 40936,
      "output_tokens": 1319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1319,
          "cache_read_input_tokens": 40936,
          "cache_creation_input_tokens": 42950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42950
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 72_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: distill_sparse_swiglu - 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR - 截止日期…",
  "leafUuid": "1eecd899-fa77-472f-b0d0-e2d801a86ad9",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 73_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Assistant

_source line 74 · 2026-05-24T04:23:25.376Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me proceed:

1. External review: config not found, so disabled. I'll skip external review.
2. Visual check: dispatch it
3. Reviewer arrangement: 2 reviewers for EMNLP

Let me now report to Group C and dispatch everything.

Here's the plan:
- Reviewer 1: 方法严谨性 + 实验设计 (method rigor + experimental design)
- Reviewer 2: 新颖性 + 完整性 + 写作质量 (novelty + completeness + writing quality)


I'll dispatch the visual check and both reviewer assignments in parallel, then format everything for Group C. Before I do that, let me verify the venue requirements: EMNLP 2026 through ARR with long papers capped at 8 pages of content plus unlimited references, double-blind review with a mandatory limitations section, using the ACL template with review option, no anonymity period needed, and appendices placed after references without counting toward the page limit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eecd899-fa77-472f-b0d0-e2d801a86ad9",
  "isSidechain": false,
  "requestId": "req_011CbLko4grcEzLsLWVgekQi",
  "type": "assistant",
  "uuid": "cf6937d1-199d-49dd-a826-e1d69f53a121",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pmiAXwrvC2gvob3aMMa9x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11092,
      "cache_read_input_tokens": 83886,
      "output_tokens": 2671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2671,
          "cache_read_input_tokens": 83886,
          "cache_creation_input_tokens": 11092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11092
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-24T04:23:32.260Z_

资料检查完毕。现在派发 Reviewer 和视觉审查。

**审稿概况**：
- **论文**：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
- **Venue**：EMNLP 2026 via ARR，deadline 2026-05-25（明天）
- **格式**：ACL template + `[review]` option，8 页正文 + 无限 references + 必须有 Limitations 节
- **匿名**：Double-blind
- **外部审稿**：未启用
- **审稿模式**：Fresh（重新审稿）

**Reviewer 编排**（EMNLP，2 人）：
- **Reviewer 1**：方法严谨性 + 实验设计（梯度分析可靠性、ablation 设计、统计方法）
- **Reviewer 2**：新颖性 + 完整性 + 写作质量（MaskLLM 边界、claim 与证据匹配、文章结构）

开始 Round 1 独立审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf6937d1-199d-49dd-a826-e1d69f53a121",
  "isSidechain": false,
  "requestId": "req_011CbLko4grcEzLsLWVgekQi",
  "type": "assistant",
  "uuid": "0adc6405-0f8c-462c-a7fa-845a16e1ebdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pmiAXwrvC2gvob3aMMa9x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11092,
      "cache_read_input_tokens": 83886,
      "output_tokens": 2671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2671,
          "cache_read_input_tokens": 83886,
          "cache_creation_input_tokens": 11092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11092
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-24T04:23:34.595Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check · `toolu_01NmoNa89wJS8GqtrQCRfVUX`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0adc6405-0f8c-462c-a7fa-845a16e1ebdb",
  "isSidechain": false,
  "requestId": "req_011CbLko4grcEzLsLWVgekQi",
  "type": "assistant",
  "uuid": "5655df35-07be-46ec-a0d5-9b2c88e50f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pmiAXwrvC2gvob3aMMa9x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11092,
      "cache_read_input_tokens": 83886,
      "output_tokens": 2671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2671,
          "cache_read_input_tokens": 83886,
          "cache_creation_input_tokens": 11092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11092
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-24T04:23:38.207Z_

<details><summary>↩ Tool result · `toolu_01NmoNa89wJS8GqtrQCRfVUX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5655df35-07be-46ec-a0d5-9b2c88e50f73",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "8c93e3a4-a8ba-4e0c-b7be-f24d630821d0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"status\\\": \\\"started\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5655df35-07be-46ec-a0d5-9b2c88e50f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-24T04:23:54.054Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01BR3KZD5wf5fHiETAijsw4k`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + unlimited references + Limitations 不计入页数\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind（不出现作者信息、避免自引）\n- **附录**: 在 references 之后，不计入页数，reviewer 不保证会读\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **方法严谨性**\n   - KL vs BCE 梯度分析（§3.6）的理论推导是否正确，结论是否 over-claimed\n   - Gumbel-Sigmoid relaxation 的数学正确性和与 STE 对比的公平性\n   - Geometric penalty schedule 的收敛保证\n   - Forward KL vs reverse KL 选择的论证是否充分\n\n2. **实验设计**\n   - 统计方法：n=3 seeds 是否足够支撑 claims，CI overlap 下是否有 over-claiming\n   - Ablation 设计：C1 target-swap 是否有残余 confound（soft→hard binarization、oracle provenance）\n   - Per-layer KL decomposition（§4.5）的 train-inference mismatch confound\n   - Baseline 公平性：BCE/MSE 是否在最优配置下对比\n   - WikiText-2 evaluation 与 WikiText-103 training 的同源性问题\n\n3. **Cross-architecture 证据**\n   - Mistral 3-seed vs LLaMA 对比的充分性\n   - Qwen-14B 结果中 GSM8K σ=5.3pp 的可靠性\n\n4. **格式合规**\n   - 8 页限制\n   - Limitations 节完整性\n   - 匿名性\n\n请以 ACL/EMNLP 审稿标准产出结构化审稿意见：Summary, Strengths (S1-Sn), Weaknesses (W1-Wn), Questions (Q1-Qn), Missing References, Minor Issues, Overall Assessment (1-5 scale per EMNLP 2026 ARR rubric)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c93e3a4-a8ba-4e0c-b7be-f24d630821d0",
  "isSidechain": false,
  "requestId": "req_011CbLko4grcEzLsLWVgekQi",
  "type": "assistant",
  "uuid": "c2b18459-6e2a-4bc9-9a29-de50d56023b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pmiAXwrvC2gvob3aMMa9x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11092,
      "cache_read_input_tokens": 83886,
      "output_tokens": 2671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2671,
          "cache_read_input_tokens": 83886,
          "cache_creation_input_tokens": 11092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11092
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-24T04:23:55.511Z_

<details><summary>↩ Tool result · `toolu_01BR3KZD5wf5fHiETAijsw4k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2b18459-6e2a-4bc9-9a29-de50d56023b1",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "7db50303-5e72-430c-9bc3-8c2e79ea223b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "c2b18459-6e2a-4bc9-9a29-de50d56023b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-24T04:24:07.150Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01HC2Yym2wyW4VHTbnu5VNRp`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + unlimited references + Limitations 不计入页数\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind（不出现作者信息、避免自引）\n- **附录**: 在 references 之后，不计入页数，reviewer 不保证会读\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**\n   - 核心 recipe（frozen model + learnable mask + KL + Gumbel relaxation）与 MaskLLM 共享程度——contextual vs static 的区别是否构成足够新颖性\n   - 各组件（KL distillation、Gumbel-Sigmoid、top-k allocation）均为 established techniques，组合新颖性是否达到 EMNLP 标准\n   - Taxonomy（Table 1）的 positioning 是否准确，是否遗漏重要相关工作\n\n2. **Claim 与证据匹配**\n   - Abstract/Introduction 中的 claim 是否被实验充分支撑\n   - \"Primary design dimension\" claim 的 scope 是否合理限定\n   - 知识任务退步（MMLU/GSM8K）的讨论是否充分\n   - Contribution list 中 \"Empirical\" vs \"Analytical\" 标注是否准确\n\n3. **写作质量**\n   - 论文结构和叙事流畅度\n   - 信息密度是否合适（是否过度压缩或冗余）\n   - Conclusion 是否充分讨论 implications 和 future directions\n   - 术语一致性\n   - Figure/Table 质量和信息量\n\n4. **完整性**\n   - Related Work 覆盖度（是否遗漏 2025-2026 重要工作）\n   - Limitations 节是否充分\n   - 评估基准覆盖度\n   - 可复现性信息是否充足\n\n请以 ACL/EMNLP 审稿标准产出结构化审稿意见：Summary, Strengths (S1-Sn), Weaknesses (W1-Wn), Questions (Q1-Qn), Missing References, Minor Issues, Overall Assessment (1-5 scale per EMNLP 2026 ARR rubric)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7db50303-5e72-430c-9bc3-8c2e79ea223b",
  "isSidechain": false,
  "requestId": "req_011CbLko4grcEzLsLWVgekQi",
  "type": "assistant",
  "uuid": "6010627c-3464-4a1a-b707-98c3d48b141c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pmiAXwrvC2gvob3aMMa9x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11092,
      "cache_read_input_tokens": 83886,
      "output_tokens": 2671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2671,
          "cache_read_input_tokens": 83886,
          "cache_creation_input_tokens": 11092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11092
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-24T04:24:08.641Z_

<details><summary>↩ Tool result · `toolu_01HC2Yym2wyW4VHTbnu5VNRp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6010627c-3464-4a1a-b707-98c3d48b141c",
  "isSidechain": false,
  "promptId": "31e60c1e-3a96-4332-aa23-37013689569a",
  "type": "user",
  "uuid": "18649a3d-b055-4f31-8099-1782b74c765e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "6010627c-3464-4a1a-b707-98c3d48b141c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 82_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 83 · 2026-05-24T04:29:37.861Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T04:29:37.861Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "content": "[服务器重启后首条消息 — Director] 项目: distill_sparse_swiglu | 当前日期: 2026-05-24\n服务器刚重启，你的对话记忆已丢失。在处理用户消息前，先执行：\n1. `feishu_read_chat_history(chat_id=\"oc_ddde40053945c09c17d4aaa8ca8e5b93\", limit=30)` 恢复近期对话上下文\n2. `get_project_status(\"distill_sparse_swiglu\")` 检查配置\n3. `director_get_project_overview(\"distill_sparse_swiglu\")` 了解现状\n如果有缺失配置，先向用户确认。\n\n**用户消息：** [Reviewer 1 审稿意见]:\n\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n**论文:** Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue:** EMNLP 2026 via ACL Rolling Review\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: PPL 维度的改进令人信服（14.5% over TEAL, 3-seed, CI 不重叠），但知识类任务系统性退化（MMLU −5.2pp）、缺乏实际加速、以及 §4.5 信号类型 vs. 耦合范围的分解被 train-inference mismatch 严重混淆，共同削弱了贡献的实际影响力。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法（KL+Gumbel-Sigmoid）数学正确；梯度分析（§3.6）定性合理但未形式化；per-layer 分解（§4.5）被承认有 confound 但仍从中下结论；C1 ablation 有残余混淆变量 |\n| Excitement | 3/5 | 研究问题（训练目标如何影响 sparsity predictor 质量）有价值，但实际贡献局限于\"PPL 更好但 MMLU/GSM8K 更差\"的 trade-off，且无实际加速 |\n| Reproducibility | 4/5 | 实验细节充分（超参数、seed、exp_id 注释），承诺开源代码；OOD 验证和多 seed 评估增强了可重复性 |\n| Clarity | 4/5 | 写作清晰坦诚，limitations 主动披露；notation 一致；但 §4.5 的嵌套 confound 讨论较难跟进 |\n| Reviewer Confidence | 4/5 | 熟悉 activation sparsity、KD、Gumbel relaxation 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] §4.5 Per-Layer KL 分解的 claim 超出证据支撑\n- 具体位置：§4.5 (experiments.tex L155-160)、Conclusion (conclusion.tex L7)、Abstract (abstract.tex L5)\n- 问题：论文在 Abstract、§4.5、Conclusion 中反复强调 \"signal type gap (9.47 PPL) exceeds coupling breadth range (2.08 PPL)\"，将此作为核心贡献之一。然而论文自身承认这一分解被 **train-inference mismatch** 严重混淆：K=1 训练时 1/32 层带 mask，推理时 32/32 层带 mask；K=4 控制实验虽部分缓解但自身也有 confound。更严重的是，在 50% sparsity 下 K=1 (34.85) 反而优于 K=4 (44.23)（Table 5 / experiments.tex L159），这一反常结果直接否定了该分解在高 sparsity 下的有效性。\n- 为什么影响接收：这是论文的第一条 contribution（Introduction L23-24），如果分解不可靠，contribution list 需要实质性修改。论文虽然在 §4.5 内有诚实的 caveat，但 Abstract 和 Conclusion 中的表述没有相应降级，给读者留下了过于确定的印象。\n- 建议修改方向：(1) 在 Abstract/Conclusion 中明确标注 \"confounded by train-inference mismatch\" 限定语；(2) 将 9.47 vs 2.08 的对比从 claim 降级为 observation；(3) 考虑设计一个无 mismatch 的控制实验（如 K=1 训练但推理也只 mask 1 层）以真正隔离 signal type 效应。\n\n**N2** [critical] 知识任务系统性退化未充分分析因果机制\n- 具体位置：§4.2 (experiments.tex L32-37)、Conclusion (conclusion.tex L6)、Limitations (limitations.tex L5)\n- 问题：MMLU 退化（30%: 40.7 vs TEAL 45.86, −5.2pp）和 GSM8K 退化（14B: 32.2±5.3 vs 52.1, −19.9pp）是论文最显著的负面结果。论文将其归因于 \"forward KL's mode-covering property\" 结构性地牺牲 rare reasoning-critical activations，并用 C4 control（Appendix V, Table 22）排除了训练数据成分的因素。然而：\n  (a) C4 control 是 **单 seed**（s42），不足以排除 seed-dependent 效应；\n  (b) \"mode-covering sacrifices rare activations\" 的因果论证停留在直觉层面，没有进一步的实证支持（如分析哪些特定 neuron 被错误剪枝、或者在 MMLU 的具体样本上做 case study）；\n  (c) Constraint 实验（Appendix T, Table 20）显示 remove valley → MMLU +3.4pp，说明 allocation 是部分原因，但这与 \"KL structural property\" 的解释存在张力——如果只是 allocation 问题，那用 task-aware allocation 就能修复，不应该是 KL 的固有缺陷。\n- 为什么影响接收：对于声称改进 sparsity prediction 的论文，在核心下游任务上系统性退化而无法解释因果机制，会严重限制方法的可推荐性。\n- 建议修改方向：(1) C4 control 增加到 3-seed；(2) 对 MMLU/GSM8K 退化做 neuron-level 的归因分析（如检查 KL 和 TEAL 在 MMLU 相关 layer 上的具体剪枝差异）；(3) 更清晰地区分 \"allocation-induced regression\"（可修复）和 \"loss-inherent regression\"（结构性）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] C1 Target-Swap Ablation 残余 confound 未充分讨论\n- 具体位置：§4.4 (experiments.tex L86-116)、Table 3\n- 问题：C1 ablation 试图分离 \"mask target quality\" 和 \"gradient coupling\"，但存在至少三个残余 confound：\n  (1) **Soft→hard binarization**：KL oracle 通过 logits>0 硬阈值化，丢弃了 ranking information（论文已承认）；\n  (2) **Oracle provenance 不一致**：s42 oracle 来自 earlier non-seed-matched checkpoint（gap 0.65pp），s123/s456 用 seed-matched oracles（gap ≤0.03pp）。这导致 s42 的 C1 PPL (9.45) 显著劣于 s123 (8.84) 和 s456 (8.82)，而这个差异可能来自 oracle provenance 而非 seed 本身；\n  (3) **BCE+Gumbel 表现反常**：BCE+Gumbel (32.22) 劣于 standard BCE (27.97)（Table 5），论文称之为 \"trajectory-dependent confounds\"，但这意味着 Gumbel relaxation 对 BCE 是有害的，而它对 KL 是核心组件——这一 asymmetry 需要更多讨论。\n- 建议：(1) 将 s42 的 oracle provenance 差异在 Table 3 caption 中更显著标注；(2) 讨论为什么 Gumbel 对 BCE 有害（BCE 的固定 oracle target 不需要 soft exploration？）；(3) 明确承认 C1 无法完全隔离 target quality vs gradient coupling。\n\n**W2** [warning] MSE baseline 可能未在最优配置下评估\n- 具体位置：§4.4 (Table 5)、Appendix G (appendix.tex L236-246)\n- 问题：MSE 在 50% 时 2/3 seeds 崩溃（只达 5.1% sparsity），只有 s42 的 229.26 PPL 可用。这说明 MSE+Gumbel+Lagrangian 的组合在高 sparsity 下不稳定。论文用 \"same hyperparameters\" 作为控制变量，但如果 MSE 需要不同的 λ_max 或 temperature schedule 才能工作，那么 \"identical setup\" 反而 unfairly disadvantages MSE。\n- 建议：(1) 为 MSE 做一轮 λ_max 的小搜索（如 2000, 5000），报告是否能避免崩溃；(2) 如果 MSE 在合理超参下仍然显著劣于 KL，这个 claim 就更强了。目前 MSE 50% 数据点本质上是 anecdotal（单 seed）。\n\n**W3** [warning] n=3 seeds 对部分 claim 支撑不足\n- 具体位置：Table 2 (experiments.tex L41-68)、§4.6 (experiments.tex L193)\n- 问题：\n  (a) MMLU 在 30% global allocation 下 σ=9.5pp（35.7±9.5），3-seed 的 95% CI 约为 [11.9, 59.5]——这个区间跨越了 TEAL (45.86) 的值，因此 \"KL 在 MMLU 上退化\" 在 global allocation 下不能被统计确认；\n  (b) Qwen-14B GSM8K σ=5.3pp (32.2±5.3)，虽然均值差 19.9pp 在统计上显著（~3.7σ），但绝对方差仍然大到令人担忧；\n  (c) Mistral ARC-c σ=6.4pp（Table 16），使该 metric 的比较无意义。\n- 论文在 §4.2 中正确地将 PPL 作为 primary metric（σ=0.02, non-overlapping），但仍然在多处对方差极大的下游指标做了 directional claims。\n- 建议：在 Table 2 和相关讨论中，对 CI 重叠的 downstream 比较加上 \"statistically indeterminate\" 标注；或增加到 5 seeds。\n\n**W4** [warning] WikiText-2 eval / WikiText-103 training 同源性\n- 具体位置：Limitations (limitations.tex L7)、Appendix D (appendix.tex L151-201)\n- 问题：WikiText-2 和 WikiText-103 来自同一 Wikipedia 语料，虽然 split 不重叠，但 domain 和 style 完全一致，PPL 评估可能 inflate KL predictor 的优势（predictor 过拟合 Wikipedia 文体的 activation pattern）。C4 OOD 验证（Appendix D, Table 10）部分缓解了这个问题，但：\n  (a) C4 30% 只有 2-seed（不是 3-seed）；\n  (b) C4 30% uniform 的 cross-seed CV=6.3%，远高于 WikiText-2 的 0.2%，暗示 predictor 对 domain 有敏感性；\n  (c) C4 30% 的 TEAL baseline 未报告，无法在 C4 上确认 KL vs TEAL 的优势。\n- 建议：(1) C4 评估补充 TEAL baseline 和 3-seed 评估；(2) 在主文 Table 2 中加入 C4 PPL 列或交叉引用 Appendix 结果。\n\n---\n\n## 小问题（不影响接收）\n\n- **格式合规**: 正文 8 页 ✓；Limitations 在 references 前 ✓；[review] 选项 ✓；\"Anonymous ACL submission\" ✓；未发现明显 de-anonymization。\n- **Eq. 4 (Gumbel-Sigmoid)**: ε₁ − ε₂ 其中 ε₁, ε₂ ∼ Gumbel(0,1) 等价于 Logistic(0,1) 噪声，数学正确。可考虑加一句说明这一等价性，减少读者困惑。\n- **Table 5 (Ablation)**: STE 行的 30% 列标注 \"---‡\" 并在脚注解释 STE 实际 sparsity 为 20.8% 而非 30%，这个处理合理但容易被忽视。建议在 STE 行直接标注实际 sparsity。\n- **§3.5 Geometric Penalty Schedule**: Eq. 7 中 clamp 的 min=0 参数在 LaTeX 中渲染不太清晰。\n- **Abstract 字数**: 约 173 词，在 200 词限制内 ✓。\n- **Appendix Y (AI Assistants)**: 披露了 Claude 的使用，符合 ARR 要求。\n\n---\n\n## 主要优势\n\n- **S1**: 实验设计总体上很严谨——C1 target-swap ablation、C4 training control、per-layer K-curve 分解、MSE 控制变量实验——形成了一个多角度的分析框架，即使每个控制实验单独来看都有 confound，组合起来仍然提供了有说服力的证据。\n- **S2**: 论文异常坦诚地报告负面结果和 confounds：MMLU/GSM8K 退化在 abstract 中就提到；§4.5 明确承认 train-inference mismatch；Limitations 列出 isocompute 缺失、同源性问题。这种透明度在同行评审中值得肯定。\n- **S3**: PPL 改进在统计上令人信服（8.81±0.02 vs 10.30, non-overlapping CIs, 3-seed），且跨架构泛化（Mistral −17.3%, Qwen-14B −12.6%）。\n- **S4**: 方法简洁——lightweight predictor (<1% params)、无需 compensation network、训练仅需 1000 步——降低了 practical barrier，即使目前没有加速也为后续 sparse kernel work 提供了基础。\n- **S5**: Taxonomy（Table 1, §3.7）提供了一个有用的概念框架（correction granularity × training signal coupling），有助于组织文献并定位贡献。\n\n---\n\n## Missing References\n\n无重大遗漏。Related work 覆盖全面，包括最新的 ActTail (2026)、WiSparse (2026)、SVD-CSP (2026) 等。可考虑补充：\n- Mirzadeh et al., 2024 (\"ReLU Strikes Back\") 已引用 ✓\n- 近期 structured sparsity 加速工作（如 Triton-based sparse kernels）可在 Future Work 中提及。\n\n---\n\n## Questions for Authors\n\n**Q1**: §4.5 中 K=1 在 50% 反而优于 K=4 (34.85 vs 44.23)，作者如何解释这一反常结果？这是否暗示 train-inference mismatch 在高 sparsity 下主导了 performance，使得整个 K-curve 分析在 50% 下失效？\n\n**Q2**: C1 ablation 中 BCE+Gumbel (32.22) 劣于 standard BCE (27.97)——作者认为 Gumbel relaxation 对 BCE 有害的根本原因是什么？如果 Gumbel 对 KL 有益但对 BCE 有害，这是否说明 Gumbel 的作用不仅是 relaxation，还与 KL loss landscape 有特定的协同效应？\n\n**Q3**: 知识任务退化（MMLU −5.2pp）和 commonsense 改进是否可以通过简单的 task-aware allocation（如 constraint experiment 中的 remove-valley）在推理时无额外训练成本地修复？如果可以，是否应该将 \"KL predictor + task-aware allocation\" 作为推荐配置？\n\n**Q4**: Table 5 中 STE 在 30% 的实际 sparsity 只有 20.8%——如果将 STE 的 target 提高到补偿 undershoot（如设置 target 40% 以达到实际 30%），STE 的 PPL 是否仍然显著劣于 Gumbel？\n"
}
```

---

### Runtime record

_source line 84 · 2026-05-24T04:29:37.862Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T04:29:37.862Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

## Round 2

2 recorded events

### User

_source line 85 · 2026-05-24T04:29:37.851Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18649a3d-b055-4f31-8099-1782b74c765e",
  "isSidechain": false,
  "promptId": "558203d7-bd25-41a6-8c4f-122ad15b5660",
  "type": "user",
  "isMeta": true,
  "uuid": "7d6a0966-d1f5-4e5b-a3bc-4be38b543dc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-24T04:29:37.852Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d6a0966-d1f5-4e5b-a3bc-4be38b543dc1",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "7a367749-10ff-42c5-bfd0-bb722b105ba2",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "2b067eb6-cb28-4925-ade8-16414fbff2c3",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

## Round 3

5 recorded events

### User

_source line 87 · 2026-05-24T04:29:37.951Z_

[服务器重启后首条消息 — Director] 项目: distill_sparse_swiglu | 当前日期: 2026-05-24
服务器刚重启，你的对话记忆已丢失。在处理用户消息前，先执行：
1. `feishu_read_chat_history(chat_id="oc_ddde40053945c09c17d4aaa8ca8e5b93", limit=30)` 恢复近期对话上下文
2. `get_project_status("distill_sparse_swiglu")` 检查配置
3. `director_get_project_overview("distill_sparse_swiglu")` 了解现状
如果有缺失配置，先向用户确认。

**用户消息：** [Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计

**论文:** Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue:** EMNLP 2026 via ACL Rolling Review

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: PPL 维度的改进令人信服（14.5% over TEAL, 3-seed, CI 不重叠），但知识类任务系统性退化（MMLU −5.2pp）、缺乏实际加速、以及 §4.5 信号类型 vs. 耦合范围的分解被 train-inference mismatch 严重混淆，共同削弱了贡献的实际影响力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心方法（KL+Gumbel-Sigmoid）数学正确；梯度分析（§3.6）定性合理但未形式化；per-layer 分解（§4.5）被承认有 confound 但仍从中下结论；C1 ablation 有残余混淆变量 |
| Excitement | 3/5 | 研究问题（训练目标如何影响 sparsity predictor 质量）有价值，但实际贡献局限于"PPL 更好但 MMLU/GSM8K 更差"的 trade-off，且无实际加速 |
| Reproducibility | 4/5 | 实验细节充分（超参数、seed、exp_id 注释），承诺开源代码；OOD 验证和多 seed 评估增强了可重复性 |
| Clarity | 4/5 | 写作清晰坦诚，limitations 主动披露；notation 一致；但 §4.5 的嵌套 confound 讨论较难跟进 |
| Reviewer Confidence | 4/5 | 熟悉 activation sparsity、KD、Gumbel relaxation 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] §4.5 Per-Layer KL 分解的 claim 超出证据支撑
- 具体位置：§4.5 (experiments.tex L155-160)、Conclusion (conclusion.tex L7)、Abstract (abstract.tex L5)
- 问题：论文在 Abstract、§4.5、Conclusion 中反复强调 "signal type gap (9.47 PPL) exceeds coupling breadth range (2.08 PPL)"，将此作为核心贡献之一。然而论文自身承认这一分解被 **train-inference mismatch** 严重混淆：K=1 训练时 1/32 层带 mask，推理时 32/32 层带 mask；K=4 控制实验虽部分缓解但自身也有 confound。更严重的是，在 50% sparsity 下 K=1 (34.85) 反而优于 K=4 (44.23)（Table 5 / experiments.tex L159），这一反常结果直接否定了该分解在高 sparsity 下的有效性。
- 为什么影响接收：这是论文的第一条 contribution（Introduction L23-24），如果分解不可靠，contribution list 需要实质性修改。论文虽然在 §4.5 内有诚实的 caveat，但 Abstract 和 Conclusion 中的表述没有相应降级，给读者留下了过于确定的印象。
- 建议修改方向：(1) 在 Abstract/Conclusion 中明确标注 "confounded by train-inference mismatch" 限定语；(2) 将 9.47 vs 2.08 的对比从 claim 降级为 observation；(3) 考虑设计一个无 mismatch 的控制实验（如 K=1 训练但推理也只 mask 1 层）以真正隔离 signal type 效应。

**N2** [critical] 知识任务系统性退化未充分分析因果机制
- 具体位置：§4.2 (experiments.tex L32-37)、Conclusion (conclusion.tex L6)、Limitations (limitations.tex L5)
- 问题：MMLU 退化（30%: 40.7 vs TEAL 45.86, −5.2pp）和 GSM8K 退化（14B: 32.2±5.3 vs 52.1, −19.9pp）是论文最显著的负面结果。论文将其归因于 "forward KL's mode-covering property" 结构性地牺牲 rare reasoning-critical activations，并用 C4 control（Appendix V, Table 22）排除了训练数据成分的因素。然而：
  (a) C4 control 是 **单 seed**（s42），不足以排除 seed-dependent 效应；
  (b) "mode-covering sacrifices rare activations" 的因果论证停留在直觉层面，没有进一步的实证支持（如分析哪些特定 neuron 被错误剪枝、或者在 MMLU 的具体样本上做 case study）；
  (c) Constraint 实验（Appendix T, Table 20）显示 remove valley → MMLU +3.4pp，说明 allocation 是部分原因，但这与 "KL structural property" 的解释存在张力——如果只是 allocation 问题，那用 task-aware allocation 就能修复，不应该是 KL 的固有缺陷。
- 为什么影响接收：对于声称改进 sparsity prediction 的论文，在核心下游任务上系统性退化而无法解释因果机制，会严重限制方法的可推荐性。
- 建议修改方向：(1) C4 control 增加到 3-seed；(2) 对 MMLU/GSM8K 退化做 neuron-level 的归因分析（如检查 KL 和 TEAL 在 MMLU 相关 layer 上的具体剪枝差异）；(3) 更清晰地区分 "allocation-induced regression"（可修复）和 "loss-inherent regression"（结构性）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] C1 Target-Swap Ablation 残余 confound 未充分讨论
- 具体位置：§4.4 (experiments.tex L86-116)、Table 3
- 问题：C1 ablation 试图分离 "mask target quality" 和 "gradient coupling"，但存在至少三个残余 confound：
  (1) **Soft→hard binarization**：KL oracle 通过 logits>0 硬阈值化，丢弃了 ranking information（论文已承认）；
  (2) **Oracle provenance 不一致**：s42 oracle 来自 earlier non-seed-matched checkpoint（gap 0.65pp），s123/s456 用 seed-matched oracles（gap ≤0.03pp）。这导致 s42 的 C1 PPL (9.45) 显著劣于 s123 (8.84) 和 s456 (8.82)，而这个差异可能来自 oracle provenance 而非 seed 本身；
  (3) **BCE+Gumbel 表现反常**：BCE+Gumbel (32.22) 劣于 standard BCE (27.97)（Table 5），论文称之为 "trajectory-dependent confounds"，但这意味着 Gumbel relaxation 对 BCE 是有害的，而它对 KL 是核心组件——这一 asymmetry 需要更多讨论。
- 建议：(1) 将 s42 的 oracle provenance 差异在 Table 3 caption 中更显著标注；(2) 讨论为什么 Gumbel 对 BCE 有害（BCE 的固定 oracle target 不需要 soft exploration？）；(3) 明确承认 C1 无法完全隔离 target quality vs gradient coupling。

**W2** [warning] MSE baseline 可能未在最优配置下评估
- 具体位置：§4.4 (Table 5)、Appendix G (appendix.tex L236-246)
- 问题：MSE 在 50% 时 2/3 seeds 崩溃（只达 5.1% sparsity），只有 s42 的 229.26 PPL 可用。这说明 MSE+Gumbel+Lagrangian 的组合在高 sparsity 下不稳定。论文用 "same hyperparameters" 作为控制变量，但如果 MSE 需要不同的 λ_max 或 temperature schedule 才能工作，那么 "identical setup" 反而 unfairly disadvantages MSE。
- 建议：(1) 为 MSE 做一轮 λ_max 的小搜索（如 2000, 5000），报告是否能避免崩溃；(2) 如果 MSE 在合理超参下仍然显著劣于 KL，这个 claim 就更强了。目前 MSE 50% 数据点本质上是 anecdotal（单 seed）。

**W3** [warning] n=3 seeds 对部分 claim 支撑不足
- 具体位置：Table 2 (experiments.tex L41-68)、§4.6 (experiments.tex L193)
- 问题：
  (a) MMLU 在 30% global allocation 下 σ=9.5pp（35.7±9.5），3-seed 的 95% CI 约为 [11.9, 59.5]——这个区间跨越了 TEAL (45.86) 的值，因此 "KL 在 MMLU 上退化" 在 global allocation 下不能被统计确认；
  (b) Qwen-14B GSM8K σ=5.3pp (32.2±5.3)，虽然均值差 19.9pp 在统计上显著（~3.7σ），但绝对方差仍然大到令人担忧；
  (c) Mistral ARC-c σ=6.4pp（Table 16），使该 metric 的比较无意义。
- 论文在 §4.2 中正确地将 PPL 作为 primary metric（σ=0.02, non-overlapping），但仍然在多处对方差极大的下游指标做了 directional claims。
- 建议：在 Table 2 和相关讨论中，对 CI 重叠的 downstream 比较加上 "statistically indeterminate" 标注；或增加到 5 seeds。

**W4** [warning] WikiText-2 eval / WikiText-103 training 同源性
- 具体位置：Limitations (limitations.tex L7)、Appendix D (appendix.tex L151-201)
- 问题：WikiText-2 和 WikiText-103 来自同一 Wikipedia 语料，虽然 split 不重叠，但 domain 和 style 完全一致，PPL 评估可能 inflate KL predictor 的优势（predictor 过拟合 Wikipedia 文体的 activation pattern）。C4 OOD 验证（Appendix D, Table 10）部分缓解了这个问题，但：
  (a) C4 30% 只有 2-seed（不是 3-seed）；
  (b) C4 30% uniform 的 cross-seed CV=6.3%，远高于 WikiText-2 的 0.2%，暗示 predictor 对 domain 有敏感性；
  (c) C4 30% 的 TEAL baseline 未报告，无法在 C4 上确认 KL vs TEAL 的优势。
- 建议：(1) C4 评估补充 TEAL baseline 和 3-seed 评估；(2) 在主文 Table 2 中加入 C4 PPL 列或交叉引用 Appendix 结果。

---

## 小问题（不影响接收）

- **格式合规**: 正文 8 页 ✓；Limitations 在 references 前 ✓；[review] 选项 ✓；"Anonymous ACL submission" ✓；未发现明显 de-anonymization。
- **Eq. 4 (Gumbel-Sigmoid)**: ε₁ − ε₂ 其中 ε₁, ε₂ ∼ Gumbel(0,1) 等价于 Logistic(0,1) 噪声，数学正确。可考虑加一句说明这一等价性，减少读者困惑。
- **Table 5 (Ablation)**: STE 行的 30% 列标注 "---‡" 并在脚注解释 STE 实际 sparsity 为 20.8% 而非 30%，这个处理合理但容易被忽视。建议在 STE 行直接标注实际 sparsity。
- **§3.5 Geometric Penalty Schedule**: Eq. 7 中 clamp 的 min=0 参数在 LaTeX 中渲染不太清晰。
- **Abstract 字数**: 约 173 词，在 200 词限制内 ✓。
- **Appendix Y (AI Assistants)**: 披露了 Claude 的使用，符合 ARR 要求。

---

## 主要优势

- **S1**: 实验设计总体上很严谨——C1 target-swap ablation、C4 training control、per-layer K-curve 分解、MSE 控制变量实验——形成了一个多角度的分析框架，即使每个控制实验单独来看都有 confound，组合起来仍然提供了有说服力的证据。
- **S2**: 论文异常坦诚地报告负面结果和 confounds：MMLU/GSM8K 退化在 abstract 中就提到；§4.5 明确承认 train-inference mismatch；Limitations 列出 isocompute 缺失、同源性问题。这种透明度在同行评审中值得肯定。
- **S3**: PPL 改进在统计上令人信服（8.81±0.02 vs 10.30, non-overlapping CIs, 3-seed），且跨架构泛化（Mistral −17.3%, Qwen-14B −12.6%）。
- **S4**: 方法简洁——lightweight predictor (<1% params)、无需 compensation network、训练仅需 1000 步——降低了 practical barrier，即使目前没有加速也为后续 sparse kernel work 提供了基础。
- **S5**: Taxonomy（Table 1, §3.7）提供了一个有用的概念框架（correction granularity × training signal coupling），有助于组织文献并定位贡献。

---

## Missing References

无重大遗漏。Related work 覆盖全面，包括最新的 ActTail (2026)、WiSparse (2026)、SVD-CSP (2026) 等。可考虑补充：
- Mirzadeh et al., 2024 ("ReLU Strikes Back") 已引用 ✓
- 近期 structured sparsity 加速工作（如 Triton-based sparse kernels）可在 Future Work 中提及。

---

## Questions for Authors

**Q1**: §4.5 中 K=1 在 50% 反而优于 K=4 (34.85 vs 44.23)，作者如何解释这一反常结果？这是否暗示 train-inference mismatch 在高 sparsity 下主导了 performance，使得整个 K-curve 分析在 50% 下失效？

**Q2**: C1 ablation 中 BCE+Gumbel (32.22) 劣于 standard BCE (27.97)——作者认为 Gumbel relaxation 对 BCE 有害的根本原因是什么？如果 Gumbel 对 KL 有益但对 BCE 有害，这是否说明 Gumbel 的作用不仅是 relaxation，还与 KL loss landscape 有特定的协同效应？

**Q3**: 知识任务退化（MMLU −5.2pp）和 commonsense 改进是否可以通过简单的 task-aware allocation（如 constraint experiment 中的 remove-valley）在推理时无额外训练成本地修复？如果可以，是否应该将 "KL predictor + task-aware allocation" 作为推荐配置？

**Q4**: Table 5 中 STE 在 30% 的实际 sparsity 只有 20.8%——如果将 STE 的 target 提高到补偿 undershoot（如设置 target 40% 以达到实际 30%），STE 的 PPL 是否仍然显著劣于 Gumbel？


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a367749-10ff-42c5-bfd0-bb722b105ba2",
  "isSidechain": false,
  "promptId": "558203d7-bd25-41a6-8c4f-122ad15b5660",
  "type": "user",
  "uuid": "481ef783-d86a-4b49-ad37-48b2aa96a82e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 89 · 2026-05-24T04:30:00.160Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T04:30:00.160Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "content": "[Reviewer 1 审稿结果]:\n审稿意见已提交给 Review Director。\n\n**总结**：Overall 3.5（Borderline Conference）。\n\n核心发现：\n- **PPL 改进令人信服**（14.5%, 3-seed, CI 不重叠），跨架构泛化\n- **两个 critical 问题**：(1) §4.5 signal type vs coupling scope 分解被 train-inference mismatch 混淆，但 Abstract/Conclusion 中的表述未相应降级；(2) MMLU/GSM8K 系统性退化缺乏因果分析\n- **四个 warning 问题**：C1 ablation 残余 confound、MSE baseline 可能未最优配置、n=3 对高方差指标不足、WikiText 同源性\n- **主要优势**：实验框架多角度严谨、论文异常坦诚、方法简洁实用、taxonomy 有概念价值"
}
```

---

### Runtime record

_source line 90 · 2026-05-24T04:30:00.160Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T04:30:00.160Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Assistant

_source line 91 · 2026-05-24T04:30:00.144Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "481ef783-d86a-4b49-ad37-48b2aa96a82e",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "f7ffd26e-9e08-4987-a4f0-0ea0b73b12ea",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "1522b4a5-0e5f-40fd-ac11-b47855e78c41",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

## Round 4

5 recorded events

### User

_source line 92 · 2026-05-24T04:30:00.314Z_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。

核心发现：
- **PPL 改进令人信服**（14.5%, 3-seed, CI 不重叠），跨架构泛化
- **两个 critical 问题**：(1) §4.5 signal type vs coupling scope 分解被 train-inference mismatch 混淆，但 Abstract/Conclusion 中的表述未相应降级；(2) MMLU/GSM8K 系统性退化缺乏因果分析
- **四个 warning 问题**：C1 ablation 残余 confound、MSE baseline 可能未最优配置、n=3 对高方差指标不足、WikiText 同源性
- **主要优势**：实验框架多角度严谨、论文异常坦诚、方法简洁实用、taxonomy 有概念价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7ffd26e-9e08-4987-a4f0-0ea0b73b12ea",
  "isSidechain": false,
  "promptId": "6896a36f-ccda-49c1-966f-ebe8d48bfa09",
  "type": "user",
  "uuid": "4cb03615-16c4-4e99-a5b5-eafd8c4c39e3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 93_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 94 · 2026-05-24T04:31:55.569Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T04:31:55.569Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "content": "[Reviewer 2 审稿意见]:\n\n## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n## Paper Summary\n\n本文提出使用输出分布蒸馏（forward KL divergence）替代传统 per-neuron BCE 来训练 SwiGLU LLM 的上下文稀疏性预测器。核心方法包括：冻结基模型 + 每层独立 2-layer MLP 预测器 + Gumbel-Sigmoid 松弛 + 几何惩罚调度实现目标稀疏度。在 LLaMA-3.1-8B 上，KL 预测器在 30% 稀疏度下相比 TEAL 降低 14.5% PPL。论文还提出了一个二维分类法（correction granularity × training signal coupling），分析 KL 相对 BCE 的梯度耦合机制，并通过大量消融实验研究了设计空间。\n\n---\n\n## Strengths\n\n**S1. 系统性的实验设计与消融分析**\n论文的实验设计非常扎实：3-seed means with standard deviations, target-swap ablation (Table 3), per-layer coupling breadth sweep (Figure 2), compensation冗余性分析 (Table 4), OOD评估 (Appendix D), 以及跨架构验证 (Mistral-7B, Qwen-2.5-14B)。每个 claim 都有对应的 controlled experiment 支撑。附录包含约 20 个补充实验（Appendix A–W），展示了极为彻底的验证工作。\n\n**S2. 有价值的梯度分析（§3.6）**\n§3.6 对比了 BCE 和 KL 的梯度结构：BCE 梯度仅依赖单个 neuron $j$，而 KL 通过下游 Jacobian $\\partial \\hat{p}_v / \\partial g^{(l)}_j$ 将每个 neuron 的 mask 决策与所有其他 neuron 的输出效应耦合。这一分析为\"为什么 KL 能发现更好的 mask\"提供了直觉上的解释，虽然不是严格的理论结果，但对读者理解方法差异很有帮助。\n\n**S3. 实用的二维分类法（Table 1）**\n将已有学习型稀疏方法沿 correction granularity（per-token vs. per-corpus）和 training signal coupling（decomposed/local/coupled）两个维度组织，清晰定位了本文方法的位置，并指出设计空间中未被探索的组合。这对社区有参考价值。\n\n**S4. 诚实的局限性讨论**\n论文坦诚报告了知识任务退化（MMLU -12.7pp, GSM8K 几乎崩塌）、50% 稀疏度下所有方法均失效、以及 wall-clock speedup 未测量等问题。这种透明度值得肯定。\n\n**S5. Target-swap ablation 设计精巧（Table 3）**\n通过让 BCE 预测器使用 KL 发现的 oracle mask 进行训练，巧妙地分离了\"mask 质量\"和\"训练目标\"的贡献。结果表明 KL 发现的 mask targets 可以迁移到 BCE，PPL 从 13.13 降至 11.79，证实了 mask 质量本身是关键因素。\n\n---\n\n## Weaknesses\n\n**W1. [Major] 与 MaskLLM 的新颖性区分不够充分**\n\n核心 recipe（frozen model + learnable mask + forward KL + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文在 §2 中承认了这一点：*\"Unlike MaskLLM...which applies KL to static N:M weight masks, we address contextual activation sparsity.\"* 但\"contextual vs. static\"的区分未被充分论证为足够的独立贡献：\n\n- MaskLLM 的 KL + Gumbel 训练框架是否可以直接扩展到 contextual 设置，只需将 static mask parameters 替换为 input-dependent predictor？如果是，方法学贡献主要是 engineering 而非 research。\n- §3.6 的梯度分析是 contextual 设置特有的（因为 mask 是 hidden state 的函数），但该分析是基于 chain rule 的直接推导，理论深度有限。\n- 论文未讨论从 static 到 contextual 的扩展中遇到了哪些 non-trivial 的技术挑战。\n\n建议：明确列出 contextual setting 引入的 unique challenges（如泛化到 unseen inputs、cross-layer coordination 的动态性、predictor 容量与表达力的 trade-off），并讨论 MaskLLM 框架无法直接处理这些挑战的原因。\n\n**W2. [Major] 知识任务退化严重但分析不足**\n\nTable 2 显示 30% 稀疏度下：\n- MMLU: 40.7 (dense) → 28.0 (KL uniform)，降幅 31%\n- GSM8K: 19.9 → 0.2，几乎完全崩塌\n\n这是非常严重的实际问题。论文给出的解释主要有两个：\n1. 训练数据组成（§4.3, Appendix V）：C4-trained predictor achieves comparable MMLU (40.6%) but worse GSM8K (4.1% vs. 7.4%)——说明训练数据不是唯一原因。\n2. Task-dependent coupling effects（§4.5）：per-layer controls 显示 commonsense 和 knowledge 任务对 coupling 的敏感度不同。\n\n但论文未回答关键问题：**为什么 output-distribution alignment（KL）这个似乎更优的目标反而导致知识任务严重退化？** 如果 KL 发现了更好的 mask（PPL 更低），为什么这些 mask 不能保留知识能力？这暗示 KL 优化的 PPL 与下游 knowledge task 之间存在根本性的 misalignment，但论文未深入分析。\n\n**W3. [Major] \"Primary design dimension\" overclaimed**\n\n论文在 §4.5 和 abstract/contributions 中声称 training signal coupling 是 \"the primary design dimension\"。但证据只比较了 Table 1 taxonomy 中的两个维度（correction granularity × signal coupling）。其他潜在重要的设计维度未被系统比较：\n- Predictor capacity（bottleneck dimension d_b, 目前固定为 128）\n- Training data selection（仅在 Appendix V 中简短探索）\n- Training duration（Appendix B.2 显示 convergence，但未探索 over-training effects）\n- Sparsity allocation strategy（global top-k vs. per-layer budgets）\n\n\"Primary\" 这个断言隐含了对所有设计维度的 exhaustive comparison，但实际上只比较了两个。建议改为 \"a key design dimension\" 或限定 scope 为 \"among the two dimensions in our taxonomy\"。\n\n此外，§4.5 自身也承认了 confounding：per-layer KL 实验中 train-inference mismatch（K=1 masks 1/32 layers during training vs. all 32 at inference）、per-layer update count disparity 都可能混淆结论。在 confounding 未完全解决的情况下做出\"primary\"断言不够审慎。\n\n**W4. [Moderate] 无 wall-clock 推理加速结果**\n\n对于以推理效率为动机的论文，完全缺少 wall-clock 测量是显著缺陷。Appendix A 报告了 throughput overhead（KL-sparse pipeline 增加 6.4% 开销），但这是预测器本身的开销，不是最终的端到端加速。论文明确承认 *\"wall-clock speedup requires sparse kernel support not addressed here\"*（page 8），但这使得读者无法评估方法的实际影响力。\n\n与之对比，TEAL 等 training-free 方法虽然质量更差但可以直接在现有 sparse kernels 上运行。一个自然的问题是：KL 预测器发现的 mask patterns（非结构化 top-k）是否与现有 sparse compute primitives 兼容？\n\n**W5. [Moderate] Contribution labels \"Analytical\" 用法非标准**\n\nC3 和 C4 被标注为 \"Analytical\"，但其内容分别是 target-swap ablation 和 compensation redundancy 实验——这些是实验性发现，不是形式化分析/理论推导。在 ACL/EMNLP 社区，\"Analytical contribution\" 通常指数学推导、理论 bounds 或 formal analysis。建议改为 \"Empirical\" 或 \"Ablation-based\"，避免误导读者期待理论结果。\n\n**W6. [Moderate] 单模型主实验，跨架构泛化不足**\n\n所有主要实验（Tables 2-4, Figures 2-3）仅在 LLaMA-3.1-8B 上完成。跨架构验证仅有：\n- Mistral-7B-v0.3: 简短提及 (§4.2)，PPL advantage 确认但 MMLU 下降\n- Qwen-2.5-14B: \"preliminary evaluation\" (§4.2)，PPL 改善但 reasoning decline (GSM8K -19.9pp)\n\n对于声称 *\"characterizing how the training objective shapes sparsity prediction quality across architectures\"* 的论文，需要更系统的跨架构评估。至少应在主实验表格中包含一个完整的第二模型结果。\n\n---\n\n## Questions\n\n**Q1.** KL predictor 发现的 mask patterns 是否与现有 semi-structured sparsity formats (如 2:4 N:M sparsity) 兼容？如果不兼容，实际部署需要什么样的 kernel 支持？\n\n**Q2.** Gumbel temperature τ 的 annealing schedule (1.0 → 0.1 over 1000 steps, Appendix C) 看起来相对 aggressive。作者是否尝试过更慢的退火方案？Figure 4 显示 final ~100 steps 有 mild loss increase，这是否表明退火过快？\n\n**Q3.** 论文提到 predictor 参数量是基模型的 <1%（75.9M vs. 8B）。但在 30% 稀疏度下，predictor 推理需要一次完整 dense forward pass 加上 predictor inference。这是否意味着首次 token 的延迟实际上会增加？\n\n**Q4.** Table 3 (target-swap ablation) 中 KL predictor trained on KL-derived targets 的 PPL (11.79) 和 BCE predictor trained on KL-derived targets 的 PPL (13.13) 之间的差距如何解释？如果 mask targets 相同，为什么训练目标仍然重要？这似乎暗示 KL 的优势不仅来自发现更好的 masks，还来自训练动态本身。\n\n**Q5.** Abstract 中 \"n=3\" 标注的含义是 3 random seeds。但 3 seeds 对于报告 downstream task variance（尤其是 GSM8K 这种高方差任务）是否足够？Tables 中的 standard deviations 有时相当大。\n\n---\n\n## Missing References\n\n论文的引用覆盖面较广，涵盖了 TEAL, CATS, MaskLLM, SPON, FastForward, DejaVu, ShadowLLM, D2DMoE, ReLU Strikes Back 等主要工作。建议补充考虑：\n\n1. **ProSparse** (Song et al., 2024, EMNLP Findings) — 通过 progressive sparsification 在 SwiGLU 模型上激活稀疏性，与本文方法互补\n2. 若有 2025-2026 年发表的 contextual sparsity + KL distillation 相关工作，应检查是否遗漏\n\n---\n\n## Minor Issues\n\n- **M1.** Table 1 中存在多个 \"empty\" 单元格标注为未探索组合。虽然诚实，但读者可能会质疑 taxonomy 的完整性。建议简要讨论为什么这些组合未被尝试（技术上不可行？或仅是未来工作？）。\n\n- **M2.** Figures 2 和 3 在双栏格式下较小，部分文字标签在打印时可能难以辨认。Figure 3 的 y 轴 \"Wallclock Perplexity Gap\" 标签建议改为更直观的名称。\n\n- **M3.** 脚注使用较多（至少 4 个可见），部分信息（如 TEAL is deterministic, sparsity notation 等）可以整合到正文中，减少阅读碎片化。\n\n- **M4.** §3.5 Geometric Penalty Schedule 中引入了多个超参数（ε, λ, geometric doubling），但主文未提供 sensitivity analysis。虽然 Appendix C 有详细讨论，但主文中应至少提及 robustness。\n\n- **M5.** Conclusion 中 *\"the signal type gap (0.47 PPL)\"*（如果确实是此数值）与 §4.5 中报告的 9.47 PPL gap 不一致。请核实。如果是排版问题，应在camera-ready中修正。[注：此处数字可能是我从 PDF 渲染中误读，但建议作者确认。]\n\n- **M6.** 论文在 §Y 声明使用了 Claude (Anthropic) 进行代码起草和写作辅助。这符合 ARR 2026 政策，但建议确认是否需要在 Responsible NLP Checklist 中额外声明。\n\n---\n\n## 格式合规性检查\n\n- **页数限制**: 主文 8 页 (pp.1-8) ✓；Limitations 在 page 9，不计入页数 ✓；References 和 Appendix 在 page 9 之后 ✓\n- **匿名性**: 标题页显示 \"Anonymous ACL submission\" ✓；未发现明显的自引暴露\n- **Limitations 节**: 存在 ✓，覆盖 4 个要点（sparsity sweet spot, knowledge regression, evaluation scope, baseline coverage）✓\n- **Abstract 长度**: 约 190-200 words，接近 200-word 限制，需确认未超限\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验方法论扎实，3-seed means + controlled ablations；但 \"primary dimension\" overclaimed 且 per-layer KL 分析存在未完全解决的 confounding |\n| **Excitement** | 2.5/5 | 核心 recipe 与 MaskLLM 重叠度高，contextual 扩展属 incremental innovation；梯度分析有价值但理论深度有限；知识任务退化限制了实际影响力 |\n| **Reproducibility** | 4/5 | 详细的超参数、训练设置、模型描述；代码承诺在接收后开源；Appendix 提供充分的实验细节 |\n| **Confidence** | 4/5 | 熟悉稀疏性/剪枝文献及本文使用的具体方法 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**一句话总结**: 扎实的实证研究，系统地证明了 KL 蒸馏在上下文稀疏性预测中优于 BCE，但方法新颖性受限于与 MaskLLM 的高度重叠，且知识任务的严重退化未得到充分解释。\n\n**详细判断依据**:\n\n本文的核心贡献是 empirical 的——通过系统实验证明 output-distribution alignment (KL) 优于 per-neuron classification (BCE) 作为 contextual sparsity predictor 的训练目标。实验设计严谨，消融全面，这些都是 Findings 级别工作的优势。\n\n然而，几个因素阻碍了 main conference 接收：\n1. **方法新颖性有限**: 核心技术栈（KL + Gumbel + frozen model）直接来自 MaskLLM，contextual 扩展虽有意义但属增量创新。\n2. **实际影响力受限**: 无 wall-clock 加速、知识任务严重退化、单模型主实验共同削弱了实际价值论证。\n3. **部分 claims overclaimed**: \"primary design dimension\" 在 confounding 未完全解决的情况下使用过于绝对化的表述。\n\n如果作者能补充 (a) 对知识任务退化的机制分析、(b) 至少一个模型的 wall-clock 结果、(c) 更准确的 contribution scope 限定，本文可能提升至 3.5 (Borderline Conference)。\n\n---\n\nSources (Step 0 搜索):\n- [ARR Review Form](https://aclrollingreview.org/reviewform)\n- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)\n"
}
```

---

### Runtime record

_source line 95 · 2026-05-24T04:31:55.569Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T04:31:55.569Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Assistant

_source line 96 · 2026-05-24T04:31:55.560Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cb03615-16c4-4e99-a5b5-eafd8c4c39e3",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "7cfdb47d-0c09-4025-bfc8-a2d0b4cc9359",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "d124b4a4-c404-4538-91b4-c99752941f78",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

## Round 5

13 recorded events

### User

_source line 97 · 2026-05-24T04:31:55.665Z_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

---

## Paper Summary

本文提出使用输出分布蒸馏（forward KL divergence）替代传统 per-neuron BCE 来训练 SwiGLU LLM 的上下文稀疏性预测器。核心方法包括：冻结基模型 + 每层独立 2-layer MLP 预测器 + Gumbel-Sigmoid 松弛 + 几何惩罚调度实现目标稀疏度。在 LLaMA-3.1-8B 上，KL 预测器在 30% 稀疏度下相比 TEAL 降低 14.5% PPL。论文还提出了一个二维分类法（correction granularity × training signal coupling），分析 KL 相对 BCE 的梯度耦合机制，并通过大量消融实验研究了设计空间。

---

## Strengths

**S1. 系统性的实验设计与消融分析**
论文的实验设计非常扎实：3-seed means with standard deviations, target-swap ablation (Table 3), per-layer coupling breadth sweep (Figure 2), compensation冗余性分析 (Table 4), OOD评估 (Appendix D), 以及跨架构验证 (Mistral-7B, Qwen-2.5-14B)。每个 claim 都有对应的 controlled experiment 支撑。附录包含约 20 个补充实验（Appendix A–W），展示了极为彻底的验证工作。

**S2. 有价值的梯度分析（§3.6）**
§3.6 对比了 BCE 和 KL 的梯度结构：BCE 梯度仅依赖单个 neuron $j$，而 KL 通过下游 Jacobian $\partial \hat{p}_v / \partial g^{(l)}_j$ 将每个 neuron 的 mask 决策与所有其他 neuron 的输出效应耦合。这一分析为"为什么 KL 能发现更好的 mask"提供了直觉上的解释，虽然不是严格的理论结果，但对读者理解方法差异很有帮助。

**S3. 实用的二维分类法（Table 1）**
将已有学习型稀疏方法沿 correction granularity（per-token vs. per-corpus）和 training signal coupling（decomposed/local/coupled）两个维度组织，清晰定位了本文方法的位置，并指出设计空间中未被探索的组合。这对社区有参考价值。

**S4. 诚实的局限性讨论**
论文坦诚报告了知识任务退化（MMLU -12.7pp, GSM8K 几乎崩塌）、50% 稀疏度下所有方法均失效、以及 wall-clock speedup 未测量等问题。这种透明度值得肯定。

**S5. Target-swap ablation 设计精巧（Table 3）**
通过让 BCE 预测器使用 KL 发现的 oracle mask 进行训练，巧妙地分离了"mask 质量"和"训练目标"的贡献。结果表明 KL 发现的 mask targets 可以迁移到 BCE，PPL 从 13.13 降至 11.79，证实了 mask 质量本身是关键因素。

---

## Weaknesses

**W1. [Major] 与 MaskLLM 的新颖性区分不够充分**

核心 recipe（frozen model + learnable mask + forward KL + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文在 §2 中承认了这一点：*"Unlike MaskLLM...which applies KL to static N:M weight masks, we address contextual activation sparsity."* 但"contextual vs. static"的区分未被充分论证为足够的独立贡献：

- MaskLLM 的 KL + Gumbel 训练框架是否可以直接扩展到 contextual 设置，只需将 static mask parameters 替换为 input-dependent predictor？如果是，方法学贡献主要是 engineering 而非 research。
- §3.6 的梯度分析是 contextual 设置特有的（因为 mask 是 hidden state 的函数），但该分析是基于 chain rule 的直接推导，理论深度有限。
- 论文未讨论从 static 到 contextual 的扩展中遇到了哪些 non-trivial 的技术挑战。

建议：明确列出 contextual setting 引入的 unique challenges（如泛化到 unseen inputs、cross-layer coordination 的动态性、predictor 容量与表达力的 trade-off），并讨论 MaskLLM 框架无法直接处理这些挑战的原因。

**W2. [Major] 知识任务退化严重但分析不足**

Table 2 显示 30% 稀疏度下：
- MMLU: 40.7 (dense) → 28.0 (KL uniform)，降幅 31%
- GSM8K: 19.9 → 0.2，几乎完全崩塌

这是非常严重的实际问题。论文给出的解释主要有两个：
1. 训练数据组成（§4.3, Appendix V）：C4-trained predictor achieves comparable MMLU (40.6%) but worse GSM8K (4.1% vs. 7.4%)——说明训练数据不是唯一原因。
2. Task-dependent coupling effects（§4.5）：per-layer controls 显示 commonsense 和 knowledge 任务对 coupling 的敏感度不同。

但论文未回答关键问题：**为什么 output-distribution alignment（KL）这个似乎更优的目标反而导致知识任务严重退化？** 如果 KL 发现了更好的 mask（PPL 更低），为什么这些 mask 不能保留知识能力？这暗示 KL 优化的 PPL 与下游 knowledge task 之间存在根本性的 misalignment，但论文未深入分析。

**W3. [Major] "Primary design dimension" overclaimed**

论文在 §4.5 和 abstract/contributions 中声称 training signal coupling 是 "the primary design dimension"。但证据只比较了 Table 1 taxonomy 中的两个维度（correction granularity × signal coupling）。其他潜在重要的设计维度未被系统比较：
- Predictor capacity（bottleneck dimension d_b, 目前固定为 128）
- Training data selection（仅在 Appendix V 中简短探索）
- Training duration（Appendix B.2 显示 convergence，但未探索 over-training effects）
- Sparsity allocation strategy（global top-k vs. per-layer budgets）

"Primary" 这个断言隐含了对所有设计维度的 exhaustive comparison，但实际上只比较了两个。建议改为 "a key design dimension" 或限定 scope 为 "among the two dimensions in our taxonomy"。

此外，§4.5 自身也承认了 confounding：per-layer KL 实验中 train-inference mismatch（K=1 masks 1/32 layers during training vs. all 32 at inference）、per-layer update count disparity 都可能混淆结论。在 confounding 未完全解决的情况下做出"primary"断言不够审慎。

**W4. [Moderate] 无 wall-clock 推理加速结果**

对于以推理效率为动机的论文，完全缺少 wall-clock 测量是显著缺陷。Appendix A 报告了 throughput overhead（KL-sparse pipeline 增加 6.4% 开销），但这是预测器本身的开销，不是最终的端到端加速。论文明确承认 *"wall-clock speedup requires sparse kernel support not addressed here"*（page 8），但这使得读者无法评估方法的实际影响力。

与之对比，TEAL 等 training-free 方法虽然质量更差但可以直接在现有 sparse kernels 上运行。一个自然的问题是：KL 预测器发现的 mask patterns（非结构化 top-k）是否与现有 sparse compute primitives 兼容？

**W5. [Moderate] Contribution labels "Analytical" 用法非标准**

C3 和 C4 被标注为 "Analytical"，但其内容分别是 target-swap ablation 和 compensation redundancy 实验——这些是实验性发现，不是形式化分析/理论推导。在 ACL/EMNLP 社区，"Analytical contribution" 通常指数学推导、理论 bounds 或 formal analysis。建议改为 "Empirical" 或 "Ablation-based"，避免误导读者期待理论结果。

**W6. [Moderate] 单模型主实验，跨架构泛化不足**

所有主要实验（Tables 2-4, Figures 2-3）仅在 LLaMA-3.1-8B 上完成。跨架构验证仅有：
- Mistral-7B-v0.3: 简短提及 (§4.2)，PPL advantage 确认但 MMLU 下降
- Qwen-2.5-14B: "preliminary evaluation" (§4.2)，PPL 改善但 reasoning decline (GSM8K -19.9pp)

对于声称 *"characterizing how the training objective shapes sparsity prediction quality across architectures"* 的论文，需要更系统的跨架构评估。至少应在主实验表格中包含一个完整的第二模型结果。

---

## Questions

**Q1.** KL predictor 发现的 mask patterns 是否与现有 semi-structured sparsity formats (如 2:4 N:M sparsity) 兼容？如果不兼容，实际部署需要什么样的 kernel 支持？

**Q2.** Gumbel temperature τ 的 annealing schedule (1.0 → 0.1 over 1000 steps, Appendix C) 看起来相对 aggressive。作者是否尝试过更慢的退火方案？Figure 4 显示 final ~100 steps 有 mild loss increase，这是否表明退火过快？

**Q3.** 论文提到 predictor 参数量是基模型的 <1%（75.9M vs. 8B）。但在 30% 稀疏度下，predictor 推理需要一次完整 dense forward pass 加上 predictor inference。这是否意味着首次 token 的延迟实际上会增加？

**Q4.** Table 3 (target-swap ablation) 中 KL predictor trained on KL-derived targets 的 PPL (11.79) 和 BCE predictor trained on KL-derived targets 的 PPL (13.13) 之间的差距如何解释？如果 mask targets 相同，为什么训练目标仍然重要？这似乎暗示 KL 的优势不仅来自发现更好的 masks，还来自训练动态本身。

**Q5.** Abstract 中 "n=3" 标注的含义是 3 random seeds。但 3 seeds 对于报告 downstream task variance（尤其是 GSM8K 这种高方差任务）是否足够？Tables 中的 standard deviations 有时相当大。

---

## Missing References

论文的引用覆盖面较广，涵盖了 TEAL, CATS, MaskLLM, SPON, FastForward, DejaVu, ShadowLLM, D2DMoE, ReLU Strikes Back 等主要工作。建议补充考虑：

1. **ProSparse** (Song et al., 2024, EMNLP Findings) — 通过 progressive sparsification 在 SwiGLU 模型上激活稀疏性，与本文方法互补
2. 若有 2025-2026 年发表的 contextual sparsity + KL distillation 相关工作，应检查是否遗漏

---

## Minor Issues

- **M1.** Table 1 中存在多个 "empty" 单元格标注为未探索组合。虽然诚实，但读者可能会质疑 taxonomy 的完整性。建议简要讨论为什么这些组合未被尝试（技术上不可行？或仅是未来工作？）。

- **M2.** Figures 2 和 3 在双栏格式下较小，部分文字标签在打印时可能难以辨认。Figure 3 的 y 轴 "Wallclock Perplexity Gap" 标签建议改为更直观的名称。

- **M3.** 脚注使用较多（至少 4 个可见），部分信息（如 TEAL is deterministic, sparsity notation 等）可以整合到正文中，减少阅读碎片化。

- **M4.** §3.5 Geometric Penalty Schedule 中引入了多个超参数（ε, λ, geometric doubling），但主文未提供 sensitivity analysis。虽然 Appendix C 有详细讨论，但主文中应至少提及 robustness。

- **M5.** Conclusion 中 *"the signal type gap (0.47 PPL)"*（如果确实是此数值）与 §4.5 中报告的 9.47 PPL gap 不一致。请核实。如果是排版问题，应在camera-ready中修正。[注：此处数字可能是我从 PDF 渲染中误读，但建议作者确认。]

- **M6.** 论文在 §Y 声明使用了 Claude (Anthropic) 进行代码起草和写作辅助。这符合 ARR 2026 政策，但建议确认是否需要在 Responsible NLP Checklist 中额外声明。

---

## 格式合规性检查

- **页数限制**: 主文 8 页 (pp.1-8) ✓；Limitations 在 page 9，不计入页数 ✓；References 和 Appendix 在 page 9 之后 ✓
- **匿名性**: 标题页显示 "Anonymous ACL submission" ✓；未发现明显的自引暴露
- **Limitations 节**: 存在 ✓，覆盖 4 个要点（sparsity sweet spot, knowledge regression, evaluation scope, baseline coverage）✓
- **Abstract 长度**: 约 190-200 words，接近 200-word 限制，需确认未超限

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验方法论扎实，3-seed means + controlled ablations；但 "primary dimension" overclaimed 且 per-layer KL 分析存在未完全解决的 confounding |
| **Excitement** | 2.5/5 | 核心 recipe 与 MaskLLM 重叠度高，contextual 扩展属 incremental innovation；梯度分析有价值但理论深度有限；知识任务退化限制了实际影响力 |
| **Reproducibility** | 4/5 | 详细的超参数、训练设置、模型描述；代码承诺在接收后开源；Appendix 提供充分的实验细节 |
| **Confidence** | 4/5 | 熟悉稀疏性/剪枝文献及本文使用的具体方法 |

---

## Overall Assessment

**Overall: 3.0 — Findings**

**一句话总结**: 扎实的实证研究，系统地证明了 KL 蒸馏在上下文稀疏性预测中优于 BCE，但方法新颖性受限于与 MaskLLM 的高度重叠，且知识任务的严重退化未得到充分解释。

**详细判断依据**:

本文的核心贡献是 empirical 的——通过系统实验证明 output-distribution alignment (KL) 优于 per-neuron classification (BCE) 作为 contextual sparsity predictor 的训练目标。实验设计严谨，消融全面，这些都是 Findings 级别工作的优势。

然而，几个因素阻碍了 main conference 接收：
1. **方法新颖性有限**: 核心技术栈（KL + Gumbel + frozen model）直接来自 MaskLLM，contextual 扩展虽有意义但属增量创新。
2. **实际影响力受限**: 无 wall-clock 加速、知识任务严重退化、单模型主实验共同削弱了实际价值论证。
3. **部分 claims overclaimed**: "primary design dimension" 在 confounding 未完全解决的情况下使用过于绝对化的表述。

如果作者能补充 (a) 对知识任务退化的机制分析、(b) 至少一个模型的 wall-clock 结果、(c) 更准确的 contribution scope 限定，本文可能提升至 3.5 (Borderline Conference)。

---

Sources (Step 0 搜索):
- [ARR Review Form](https://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cfdb47d-0c09-4025-bfc8-a2d0b4cc9359",
  "isSidechain": false,
  "promptId": "83fcad41-b889-4d65-9aad-e48a9949d207",
  "type": "user",
  "uuid": "0a02515a-39b3-46fb-8f12-a7b1793f5037",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 98 · 2026-05-24T04:31:55.665Z_

```json
{
  "parentUuid": "0a02515a-39b3-46fb-8f12-a7b1793f5037",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "58d5b400-f88e-488a-8f36-848510292254",
  "timestamp": "2026-05-24T04:31:55.665Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 99 · 2026-05-24T04:32:08.490Z_

<details><summary>Logged reasoning block</summary>

```text
I now have both Reviewer 1 and Reviewer 2's reviews. Let me proceed to Step 2 — Cross-sharing (交叉分享).

**Reviewer 1 Summary:**
- Overall: 3.5 (Borderline Conference)
- 2 critical (N1: §4.5 decomposition confounded; N2: knowledge regression lacks causal analysis)
- 4 warnings (W1: C1 confound; W2: MSE baseline; W3: n=3 insufficient; W4: WikiText同源)
- Strengths: rigorous experiments, honest reporting, convincing PPL, practical method, useful taxonomy


- **Reviewer 2 Summary:**
- Overall: 3.0 (Findings)
- 3 major (W1: MaskLLM novelty; W2: knowledge regression; W3: "primary dimension" overclaimed)
- 3 moderate (W4: no wall-clock; W5: "Analytical" label; W6: single model main experiment)
- Strengths: systematic experiments, gradient analysis, taxonomy, honest limitations, target-swap design

Now I'm moving to Step 2: Cross-sharing each reviewer's full review with the other, asking them to respond with [AGREE] or [REBUT] for each point.

I'm sending both cross-sharing messages in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58d5b400-f88e-488a-8f36-848510292254",
  "isSidechain": false,
  "requestId": "req_011CbLmToHVAga3kmXTWGiwi",
  "type": "assistant",
  "uuid": "6e3672e7-ee7c-423e-9342-4059d63788c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeTUyUbKjDWPDS6duXGeVq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5128,
      "cache_read_input_tokens": 103273,
      "output_tokens": 2975,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2975,
          "cache_read_input_tokens": 103273,
          "cache_creation_input_tokens": 5128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5128
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 58665
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 100 · 2026-05-24T04:32:11.104Z_

两位 Reviewer 的独立审稿已收到。进入 Step 2 — 交叉分享。

**R1**: 3.5 (Borderline Conference) | **R2**: 3.0 (Findings)

共识方向：PPL 改进令人信服、知识任务退化分析不足、§4.5 分解有 confound。
主要分歧：新颖性评估（R2 认为与 MaskLLM 高度重叠，R1 未将此列为主要问题）、wall-clock 缺失的权重。

现在将双方完整审稿原文互相转发，要求逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e3672e7-ee7c-423e-9342-4059d63788c2",
  "isSidechain": false,
  "requestId": "req_011CbLmToHVAga3kmXTWGiwi",
  "type": "assistant",
  "uuid": "894ce57b-e63f-4049-9d4c-9210009db046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeTUyUbKjDWPDS6duXGeVq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5128,
      "cache_read_input_tokens": 103273,
      "output_tokens": 2975,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2975,
          "cache_read_input_tokens": 103273,
          "cache_creation_input_tokens": 5128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5128
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 58665
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-24T04:32:38.083Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01ECYX8Pz4WGTmDmW2H3Hdpd`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Weaknesses:\n\n**W1. [Major] 与 MaskLLM 的新颖性区分不够充分**\n核心 recipe（frozen model + learnable mask + forward KL + Gumbel relaxation）与 MaskLLM 高度重合。\"contextual vs. static\"的区分未被充分论证为足够的独立贡献。MaskLLM 的 KL + Gumbel 框架是否可以直接扩展到 contextual 设置？§3.6 梯度分析理论深度有限。论文未讨论从 static 到 contextual 的 non-trivial 技术挑战。\n\n**W2. [Major] 知识任务退化严重但分析不足**\nMMLU: 40.7→28.0 (降幅31%), GSM8K 几乎完全崩塌。为什么 output-distribution alignment 这个看似更优的目标反而导致知识任务严重退化？如果 KL 发现了更好的 mask（PPL 更低），为什么不能保留知识能力？暗示 PPL 与 knowledge task 之间存在根本性 misalignment。\n\n**W3. [Major] \"Primary design dimension\" overclaimed**\n证据只比较了 taxonomy 中两个维度，其他设计维度（predictor capacity, training data, duration, allocation strategy）未系统比较。\"Primary\" 隐含 exhaustive comparison。§4.5 自身承认 confounding。\n\n**W4. [Moderate] 无 wall-clock 推理加速结果**\n预测器增加 6.4% 开销，无最终端到端加速。KL mask patterns 是否与现有 sparse compute primitives 兼容？\n\n**W5. [Moderate] Contribution labels \"Analytical\" 用法非标准**\nC3/C4 内容是实验性发现，不是形式化分析。\"Analytical\" 在 ACL/EMNLP 通常指数学推导/理论 bounds。\n\n**W6. [Moderate] 单模型主实验，跨架构泛化不足**\n主要实验仅在 LLaMA-3.1-8B 上完成，Mistral 和 Qwen 验证不够系统。\n\n## Reviewer 2 的 Questions:\n\n**Q1.** KL mask patterns 是否与 2:4 N:M sparsity 兼容？实际部署需要什么 kernel 支持？\n\n**Q2.** Gumbel τ annealing (1.0→0.1) 是否过快？Final ~100 steps 的 mild loss increase 是否表明退火过快？\n\n**Q3.** 30% 稀疏度下首次 token 延迟是否增加（需完整 dense forward + predictor inference）？\n\n**Q4.** Table 3 中 KL predictor (11.79) vs BCE on KL targets (13.13) 的差距如何解释？如果 mask targets 相同，为什么训练目标仍然重要？\n\n**Q5.** n=3 seeds 对高方差下游任务是否足够？\n\n## Reviewer 2 的 Overall Assessment:\n3.0 (Findings)。方法新颖性受限于 MaskLLM 重叠，知识任务退化未充分解释，无 wall-clock 加速。\n\n---\n\n请逐条回应上述 Weaknesses 和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "894ce57b-e63f-4049-9d4c-9210009db046",
  "isSidechain": false,
  "requestId": "req_011CbLmToHVAga3kmXTWGiwi",
  "type": "assistant",
  "uuid": "0dc9bc79-7685-46fc-a471-9c7e4f0eb2f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeTUyUbKjDWPDS6duXGeVq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5128,
      "cache_read_input_tokens": 103273,
      "output_tokens": 2975,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2975,
          "cache_read_input_tokens": 103273,
          "cache_creation_input_tokens": 5128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5128
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 58665
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-24T04:32:42.132Z_

<details><summary>↩ Tool result · `toolu_01ECYX8Pz4WGTmDmW2H3Hdpd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dc9bc79-7685-46fc-a471-9c7e4f0eb2f3",
  "isSidechain": false,
  "promptId": "83fcad41-b889-4d65-9aad-e48a9949d207",
  "type": "user",
  "uuid": "94b9f092-2bcd-47c7-a137-4de07bee9f71",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "0dc9bc79-7685-46fc-a471-9c7e4f0eb2f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-24T04:33:18.274Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01WVHwWrYcSnFSmscncncvHC`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题:\n\n**N1** [critical] §4.5 Per-Layer KL 分解的 claim 超出证据支撑\n- Abstract/§4.5/Conclusion 反复强调 \"signal type gap (9.47 PPL) exceeds coupling breadth range (2.08 PPL)\"。但 train-inference mismatch 严重混淆（K=1 训练 1/32 层 mask vs 推理 32/32 层）。50% 下 K=1 (34.85) 优于 K=4 (44.23) 直接否定了分解在高 sparsity 下的有效性。这是第一条 contribution，但 Abstract/Conclusion 表述未降级。\n- 建议：Abstract/Conclusion 加 \"confounded by train-inference mismatch\" 限定；将 9.47 vs 2.08 从 claim 降级为 observation；设计无 mismatch 控制实验。\n\n**N2** [critical] 知识任务系统性退化未充分分析因果机制\n- MMLU −5.2pp、14B GSM8K −19.9pp。归因于 \"forward KL mode-covering\" 但：\n  (a) C4 control 单 seed；\n  (b) \"mode-covering sacrifices rare activations\" 停留在直觉，无实证；\n  (c) Constraint 实验显示 remove valley → MMLU +3.4pp，说明 allocation 是部分原因，与 \"KL structural property\" 解释有张力。\n- 建议：C4 control 增至 3-seed；neuron-level 归因分析；区分 allocation-induced vs loss-inherent regression。\n\n## Reviewer 1 的 Should-Fix 问题:\n\n**W1** [warning] C1 Target-Swap Ablation 残余 confound\n- Soft→hard binarization 丢失 ranking info；s42 oracle 来自 non-seed-matched checkpoint（gap 0.65pp vs s123/s456 ≤0.03pp）；BCE+Gumbel (32.22) 劣于 BCE (27.97) 暗示 Gumbel 对 BCE 有害但对 KL 有益。\n\n**W2** [warning] MSE baseline 可能未在最优配置下评估\n- MSE 50% 2/3 seeds 崩溃。\"Same hyperparameters\" 可能 unfairly disadvantage MSE。建议为 MSE 做 λ_max 小搜索。\n\n**W3** [warning] n=3 seeds 对部分 claim 支撑不足\n- MMLU 30% global σ=9.5pp, 95% CI ≈ [11.9, 59.5]；Qwen-14B GSM8K σ=5.3pp；Mistral ARC-c σ=6.4pp。\n\n**W4** [warning] WikiText-2 eval / WikiText-103 training 同源性\n- C4 OOD 30% 仅 2-seed；C4 uniform CV=6.3% vs in-domain 0.2%；C4 缺 TEAL baseline。\n\n## Reviewer 1 的 Questions:\n\n**Q1**: K=1 在 50% 优于 K=4 如何解释？K-curve 在 50% 下是否失效？\n**Q2**: BCE+Gumbel (32.22) 劣于 BCE (27.97) 的根本原因？Gumbel 与 KL 有特定协同效应？\n**Q3**: 知识退化是否可通过 task-aware allocation（remove-valley）在推理时修复？\n**Q4**: STE 若补偿 undershoot（target 40% 以达实际 30%），PPL 是否仍劣于 Gumbel？\n\n## Reviewer 1 的 Overall Assessment:\n3.5 (Borderline Conference)。PPL 改进令人信服，但知识退化和 §4.5 confound 削弱贡献。\n\n---\n\n请逐条回应上述 Must-Fix、Should-Fix 问题和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94b9f092-2bcd-47c7-a137-4de07bee9f71",
  "isSidechain": false,
  "requestId": "req_011CbLmToHVAga3kmXTWGiwi",
  "type": "assistant",
  "uuid": "5f1e2755-8dbd-4b73-82c3-40f6aba6f35c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeTUyUbKjDWPDS6duXGeVq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5128,
      "cache_read_input_tokens": 103273,
      "output_tokens": 2975,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2975,
          "cache_read_input_tokens": 103273,
          "cache_creation_input_tokens": 5128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5128
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 58665
      }
    }
  }
}
```

</details>

---

### Runtime record

_source line 104_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Reviewer 2 审稿意见]:  ## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs  ---  ## Paper Summary  本文提出使用输出分布蒸馏（forward KL divergence）替代传统 per-neuron BCE…",
  "leafUuid": "5f1e2755-8dbd-4b73-82c3-40f6aba6f35c",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 105_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Tool result

_source line 106 · 2026-05-24T04:33:19.636Z_

<details><summary>↩ Tool result · `toolu_01WVHwWrYcSnFSmscncncvHC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f1e2755-8dbd-4b73-82c3-40f6aba6f35c",
  "isSidechain": false,
  "promptId": "83fcad41-b889-4d65-9aad-e48a9949d207",
  "type": "user",
  "uuid": "c2348731-a6f0-40cc-9946-7efe496ce664",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "5f1e2755-8dbd-4b73-82c3-40f6aba6f35c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 107_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 108 · 2026-05-24T04:33:28.946Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T04:33:28.946Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "content": "[Reviewer 2 审稿结果]:\n审稿意见已提交给 Review Director。\n\n**审稿结论：Overall 3.0 (Findings)**\n\n核心评价：\n- **Soundness 3.5/5** — 实验设计扎实（3-seed, controlled ablations），但 \"primary design dimension\" overclaimed 且存在未解决的 confounding\n- **Excitement 2.5/5** — 核心 recipe 与 MaskLLM 高度重叠（KL + Gumbel + frozen model），contextual 扩展属增量创新\n- **Overall 3.0/5** — 适合 Findings\n\n**三个 Major Weaknesses**：\n1. 与 MaskLLM 新颖性区分不足（共享 frozen model + KL + Gumbel recipe，contextual vs. static 的技术挑战未充分论证）\n2. 知识任务严重退化（MMLU -31%, GSM8K 几乎崩塌）缺乏机制解释\n3. \"Primary design dimension\" 在 confounding 未解决的前提下 overclaimed\n\n**两个 Moderate Weaknesses**：无 wall-clock 加速结果、单模型主实验限制泛化性论证"
}
```

---

### Runtime record

_source line 109 · 2026-05-24T04:33:28.946Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T04:33:28.946Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

## Round 6

2 recorded events

### User

_source line 110 · 2026-05-24T04:33:28.937Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2348731-a6f0-40cc-9946-7efe496ce664",
  "isSidechain": false,
  "promptId": "1a6637f0-8c90-491b-b0ff-02670dd7dae1",
  "type": "user",
  "isMeta": true,
  "uuid": "81b5ea2f-533b-467d-95b3-9322a294d9c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 111 · 2026-05-24T04:33:28.937Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81b5ea2f-533b-467d-95b3-9322a294d9c5",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "e88fd061-3d04-44dc-a057-5dec7f2555c9",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "203366b9-b51a-4dc7-896d-fc5b97c3bbd0",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

## Round 7

5 recorded events

### User

_source line 112 · 2026-05-24T04:33:29.039Z_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论：Overall 3.0 (Findings)**

核心评价：
- **Soundness 3.5/5** — 实验设计扎实（3-seed, controlled ablations），但 "primary design dimension" overclaimed 且存在未解决的 confounding
- **Excitement 2.5/5** — 核心 recipe 与 MaskLLM 高度重叠（KL + Gumbel + frozen model），contextual 扩展属增量创新
- **Overall 3.0/5** — 适合 Findings

**三个 Major Weaknesses**：
1. 与 MaskLLM 新颖性区分不足（共享 frozen model + KL + Gumbel recipe，contextual vs. static 的技术挑战未充分论证）
2. 知识任务严重退化（MMLU -31%, GSM8K 几乎崩塌）缺乏机制解释
3. "Primary design dimension" 在 confounding 未解决的前提下 overclaimed

**两个 Moderate Weaknesses**：无 wall-clock 加速结果、单模型主实验限制泛化性论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e88fd061-3d04-44dc-a057-5dec7f2555c9",
  "isSidechain": false,
  "promptId": "1a6637f0-8c90-491b-b0ff-02670dd7dae1",
  "type": "user",
  "uuid": "2bbd5c35-8d55-4df4-b1e0-5411382e93e2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 113_

```json
{
  "type": "ai-title",
  "aiTitle": "Review distill_sparse_swiglu paper for EMNLP",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Runtime record

_source line 114 · 2026-05-24T04:34:52.160Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T04:34:52.160Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "content": "[Reviewer 1 审稿意见]:\n\n## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1: 与 MaskLLM 的新颖性区分不够充分**\n部分同意。论文在 §2 (related_work.tex L21-23) 列出了三个区别：(a) per-token vs static masks, (b) cross-layer allocation interaction, (c) distribution shift robustness。但 R2 指出的核心问题是对的——论文没有讨论从 static 到 contextual 的 **技术挑战**。MaskLLM 的 Gumbel-Softmax 在 static 设置中直接优化固定的 mask 参数，而本文需要训练一个 predictor network 来泛化到 unseen inputs，这在优化景观上是不同的（predictor 的泛化误差 vs. 直接优化的 oracle masks）。但论文确实没有形式化这一区别。不过我要补充一点：MaskLLM 处理的是 N:M weight sparsity（结构化、静态），而本文处理的是 contextual activation sparsity（非结构化、动态），这是两个不同的子领域，目标读者群体不完全重叠，因此 \"recipe 重合\" 的严重性应适度评估。论文的真正贡献在于 empirical characterization（5 个 loss 的系统比较 + C1 ablation + K-curve 分解），这一点不依赖于与 MaskLLM 的区分。\n\n**[AGREE] R2-W2: 知识任务退化严重但分析不足**\n完全同意。这与我的 N2 一致。论文的解释（\"forward KL mode-covering sacrifices rare reasoning-critical activations\"）停留在直觉层面。特别值得注意的是：\n- §4.2 Task-Type Split 报告 MMLU 40.7±1.3 (uniform) vs TEAL 45.86 (−5.2pp)\n- 但 Appendix T (Table 20) 的 constraint experiment 显示 remove-valley → MMLU 44.0 (+3.4pp)，几乎恢复到 TEAL 水平\n- 这说明退化可能主要是 **allocation pattern** 的问题而非 KL loss 的固有缺陷\n\nR2 提出的追问很尖锐：\"如果 KL 发现了更好的 mask（PPL 更低），为什么不能保留知识能力？\" 这暗示 PPL 改进和知识任务之间可能存在 Pareto trade-off，而不是 PPL 的绝对改进。论文应该正面讨论这个可能性。\n\n不过我认为 R2 引用的 \"MMLU: 40.7→28.0 (降幅31%)\" 有误导性——40.7 是 30% sparsity, 28.0 是 50% sparsity，这是跨 sparsity level 的比较，不是同一条件下的退化。在同一条件（30% uniform）下，KL MMLU 40.7 vs TEAL 45.86 的退化幅度是 −5.2pp（11.3%），而非 31%。\n\n**[REBUT] R2-W3: \"Primary design dimension\" overclaimed**\n部分反驳。论文的 claim \"Output-distribution alignment is the primary design dimension\" 确实有 overclaim 的嫌疑，这与我的 N1 观点一致。但 R2 说 \"证据只比较了 taxonomy 中两个维度\" 不完全准确：\n- Table 5 (§4.4) 系统比较了 **5 个 loss function**（Forward KL, Reverse KL, JSD, BCE, MSE），不仅是两个维度\n- Appendix B (Table 6) 测试了 predictor capacity（d_b = 64/128/256/512）\n- Appendix B.2 (Table 8) 测试了 training duration（200-1000 steps）\n- §4.2 比较了 allocation strategy（global vs uniform）\n- Appendix B.1 (Table 7) 测试了 temperature schedule 变体\n\n所以论文确实 systematically varied 了多个设计维度，只是 \"primary\" 这个词暗示了穷尽性比较。我建议将 \"primary\" 改为 \"a critical\" 或 \"among the most important\"。但证据基础比 R2 描述的更宽。\n\n**[AGREE] R2-W4: 无 wall-clock 推理加速结果**\n同意这是一个实际局限。但我认为论文已经诚实地处理了这一点：Abstract 末尾（\"wall-clock speedup requires sparse kernel support not addressed here\"）、Introduction (L18)、Appendix A、和 Limitations 都明确说明了。对于一篇定位为 \"empirical study characterizing how the training objective shapes sparsity prediction quality\" 的论文（Introduction L18），不提供加速结果是可以接受的——前提是论文不 claim 加速。论文确实没有。\n\n**[AGREE] R2-W5: \"Analytical\" contribution labels 非标准**\n同意。Introduction L25-27 将 C3（target-swap ablation）和 C4（compensation redundancy）标记为 \"Analytical\"，但这些都是实验发现而非数学分析。在 ACL/EMNLP 语境下，\"Analytical\" 通常指理论推导、complexity bounds 等。建议改为 \"Empirical-analytical\" 或直接用 \"Empirical\"。这是一个 presentation issue，不影响贡献本身的实质。\n\n**[REBUT] R2-W6: 单模型主实验，跨架构泛化不足**\n部分反驳。R2 说 \"Mistral 和 Qwen 验证不够系统\"，但：\n- Mistral-7B-v0.3 有 **3-seed 完整评估**（PPL + 6 个 downstream tasks, Table 16/Appendix N），PPL 泛化 −17.3%，commonsense 改进（WG +6.7pp），知识任务 tied（MMLU 43.3 vs 43.5）\n- Qwen-2.5-14B 有 3-seed GSM8K + 单 seed 其他指标（Table 13/Appendix K）\n- 三个架构覆盖了 GQA (LLaMA), GQA+sliding window (Mistral), 不同 d_ff 维度 (Qwen-14B 5120→18944)\n\n对于一篇 8 页限制的论文，3 个架构（7B-14B 范围）的验证是合理的。Qwen 的评估确实可以更系统（增加更多 seed），但现有证据已经覆盖了主要的架构变体。真正缺失的是 **更大规模**（如 70B）的验证，这一点 R2 没有提到。\n\n---\n\n### Questions 回应\n\n**[REBUT] R2-Q1: KL mask patterns 是否与 2:4 N:M sparsity 兼容？**\nR2 的问题合理但超出了论文的 scope。论文处理的是 unstructured activation sparsity（与 TEAL 相同），而 2:4 N:M 是 structured weight sparsity pattern。这是两个不同的问题设定。MaskLLM 处理 N:M weight masks，本文处理 contextual activation masks——不应期望 activation mask 直接满足 N:M 结构约束。实际部署需要的是 block-sparse kernel（如 Triton block-sparse）而非 2:4 N:M，因为 activation mask 是 input-dependent、layer-varying 的。论文在 Appendix A (appendix.tex L32-33) 提到了这一点。\n\n**[REBUT] R2-Q2: τ annealing 是否过快？**\n论文在 Appendix B.1 (Table 7) 已经回答了这个问题：fixed τ=0.5 (PPL 11.861) 实际上 **略优于** linear 1.0→0.1 (PPL 11.963)，而 fixed τ=0.1 (PPL 12.072) 最差。整体变化范围 <1.8%，说明温度策略对最终结果影响很小。Final ~100 steps 的 mild loss increase（Appendix C, appendix.tex L144-145）被解释为 masks 趋向 binary 时 discrete rounding noise 的正常表现，而非退火过快的症状。如果退火过快，我们预期会看到更大的 loss spike，但实际观察到的只是 mild increase。\n\n**[AGREE] R2-Q3: 首次 token 延迟**\n合理的工程问题。论文的 predictor 在每一层取 x^(ℓ)（attention 后的 hidden state）作为输入，然后预测该层的 mask，因此可以与 base model 的 layer-by-layer forward pass 并行或串行执行。但论文的 latency 测量（Appendix A, Table 5）只报告了 steady-state throughput（100 forward passes 的平均），没有单独报告 first-token latency。对于 autoregressive generation 的 prefill 阶段，predictor 在每个 token 位置独立运行，所以 first-token 不应有额外开销（相对于后续 token）。但这一点论文确实没有明确说明。\n\n**[REBUT] R2-Q4: Table 3 中数字引用有误**\nR2 引用 \"KL predictor (11.79) vs BCE on KL targets (13.13)\"，但这些数字与论文 Table 3 不匹配：\n- 50% s42: C1 PPL = **11.96**, KL PPL = **11.96**（几乎完全匹配，gap ≤0.79pp across all metrics）\n- 30% s42: C1 PPL = 9.45, KL PPL = 8.82（gap 0.63pp，但 s42 oracle 来自 non-seed-matched earlier checkpoint）\n- 30% s123/s456（seed-matched oracles）: C1 PPL 8.84/8.82, KL PPL 8.83/8.79（gap ≤0.03pp）\n\n论文中 **不存在 13.13** 这个数值。11.79 出现在 Table 5 (ablation) 作为 50% 的 forward KL PPL，不在 Table 3 (C1 ablation) 中。R2 可能混淆了不同 table 的数字。实际上 C1 ablation 的结论是 mask patterns **高度可迁移**——在 seed-matched 条件下 gap ≤0.03pp，这恰恰支持了论文的 claim，而非质疑它。\n\n**[AGREE] R2-Q5: n=3 seeds 对高方差 downstream tasks 是否足够**\n完全同意，与我的 W3 一致。PPL 的 σ=0.02 (CV=0.2%) 使 3 seeds 完全足够。但 MMLU 在 30% global 下 σ=9.5pp (CV=26.6%)、Qwen GSM8K σ=5.3pp (CV=16.5%)、Mistral ARC-c σ=6.4pp (CV=14.3%) 意味着 3 seeds 无法产生有意义的置信区间。论文在 §4.2 中正确地将 PPL 作为 primary metric，但在多处对高方差 downstream 指标做了 directional claims，应加上 \"statistically indeterminate\" 限定语。\n\n---\n\n### 综合评价\n\nR2 的整体打分 3.0 (Findings) 在我看来偏低。R2 最有力的论点是 W2（知识任务退化分析不足）和 W5（contribution labeling），但 W1（MaskLLM 重叠）和 W6（跨架构泛化不足）被过度强调：\n\n- W1 忽视了论文真正的贡献是 **empirical characterization**（5 loss 比较 + ablation framework），不是 method novelty\n- W6 低估了 3 个架构、7-14B 范围、含 3-seed Mistral 评估的充分性\n- Q4 引用了论文中不存在的数字 (13.13)，这降低了该 question 的可信度\n\n我维持 3.5 (Borderline Conference) 的评分。论文的 PPL 改进真实可信，实验框架设计有价值，坦诚度高于平均水平。主要扣分在于 §4.5 的 confounded decomposition 被 overclaim（我的 N1）和知识任务退化缺乏深入分析（我的 N2 / R2-W2）。\n"
}
```

---

### Runtime record

_source line 115 · 2026-05-24T04:34:52.160Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T04:34:52.160Z",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a"
}
```

---

### Assistant

_source line 116 · 2026-05-24T04:34:52.150Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bbd5c35-8d55-4df4-b1e0-5411382e93e2",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "c62c8207-24ea-4b63-8a7c-967d430c0c9e",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "21f54028-8ca4-489b-82b6-7760a7d16194",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

## Round 8

1 recorded events

### User

_source line 117 · 2026-05-24T04:34:52.254Z_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R2-W1: 与 MaskLLM 的新颖性区分不够充分**
部分同意。论文在 §2 (related_work.tex L21-23) 列出了三个区别：(a) per-token vs static masks, (b) cross-layer allocation interaction, (c) distribution shift robustness。但 R2 指出的核心问题是对的——论文没有讨论从 static 到 contextual 的 **技术挑战**。MaskLLM 的 Gumbel-Softmax 在 static 设置中直接优化固定的 mask 参数，而本文需要训练一个 predictor network 来泛化到 unseen inputs，这在优化景观上是不同的（predictor 的泛化误差 vs. 直接优化的 oracle masks）。但论文确实没有形式化这一区别。不过我要补充一点：MaskLLM 处理的是 N:M weight sparsity（结构化、静态），而本文处理的是 contextual activation sparsity（非结构化、动态），这是两个不同的子领域，目标读者群体不完全重叠，因此 "recipe 重合" 的严重性应适度评估。论文的真正贡献在于 empirical characterization（5 个 loss 的系统比较 + C1 ablation + K-curve 分解），这一点不依赖于与 MaskLLM 的区分。

**[AGREE] R2-W2: 知识任务退化严重但分析不足**
完全同意。这与我的 N2 一致。论文的解释（"forward KL mode-covering sacrifices rare reasoning-critical activations"）停留在直觉层面。特别值得注意的是：
- §4.2 Task-Type Split 报告 MMLU 40.7±1.3 (uniform) vs TEAL 45.86 (−5.2pp)
- 但 Appendix T (Table 20) 的 constraint experiment 显示 remove-valley → MMLU 44.0 (+3.4pp)，几乎恢复到 TEAL 水平
- 这说明退化可能主要是 **allocation pattern** 的问题而非 KL loss 的固有缺陷

R2 提出的追问很尖锐："如果 KL 发现了更好的 mask（PPL 更低），为什么不能保留知识能力？" 这暗示 PPL 改进和知识任务之间可能存在 Pareto trade-off，而不是 PPL 的绝对改进。论文应该正面讨论这个可能性。

不过我认为 R2 引用的 "MMLU: 40.7→28.0 (降幅31%)" 有误导性——40.7 是 30% sparsity, 28.0 是 50% sparsity，这是跨 sparsity level 的比较，不是同一条件下的退化。在同一条件（30% uniform）下，KL MMLU 40.7 vs TEAL 45.86 的退化幅度是 −5.2pp（11.3%），而非 31%。

**[REBUT] R2-W3: "Primary design dimension" overclaimed**
部分反驳。论文的 claim "Output-distribution alignment is the primary design dimension" 确实有 overclaim 的嫌疑，这与我的 N1 观点一致。但 R2 说 "证据只比较了 taxonomy 中两个维度" 不完全准确：
- Table 5 (§4.4) 系统比较了 **5 个 loss function**（Forward KL, Reverse KL, JSD, BCE, MSE），不仅是两个维度
- Appendix B (Table 6) 测试了 predictor capacity（d_b = 64/128/256/512）
- Appendix B.2 (Table 8) 测试了 training duration（200-1000 steps）
- §4.2 比较了 allocation strategy（global vs uniform）
- Appendix B.1 (Table 7) 测试了 temperature schedule 变体

所以论文确实 systematically varied 了多个设计维度，只是 "primary" 这个词暗示了穷尽性比较。我建议将 "primary" 改为 "a critical" 或 "among the most important"。但证据基础比 R2 描述的更宽。

**[AGREE] R2-W4: 无 wall-clock 推理加速结果**
同意这是一个实际局限。但我认为论文已经诚实地处理了这一点：Abstract 末尾（"wall-clock speedup requires sparse kernel support not addressed here"）、Introduction (L18)、Appendix A、和 Limitations 都明确说明了。对于一篇定位为 "empirical study characterizing how the training objective shapes sparsity prediction quality" 的论文（Introduction L18），不提供加速结果是可以接受的——前提是论文不 claim 加速。论文确实没有。

**[AGREE] R2-W5: "Analytical" contribution labels 非标准**
同意。Introduction L25-27 将 C3（target-swap ablation）和 C4（compensation redundancy）标记为 "Analytical"，但这些都是实验发现而非数学分析。在 ACL/EMNLP 语境下，"Analytical" 通常指理论推导、complexity bounds 等。建议改为 "Empirical-analytical" 或直接用 "Empirical"。这是一个 presentation issue，不影响贡献本身的实质。

**[REBUT] R2-W6: 单模型主实验，跨架构泛化不足**
部分反驳。R2 说 "Mistral 和 Qwen 验证不够系统"，但：
- Mistral-7B-v0.3 有 **3-seed 完整评估**（PPL + 6 个 downstream tasks, Table 16/Appendix N），PPL 泛化 −17.3%，commonsense 改进（WG +6.7pp），知识任务 tied（MMLU 43.3 vs 43.5）
- Qwen-2.5-14B 有 3-seed GSM8K + 单 seed 其他指标（Table 13/Appendix K）
- 三个架构覆盖了 GQA (LLaMA), GQA+sliding window (Mistral), 不同 d_ff 维度 (Qwen-14B 5120→18944)

对于一篇 8 页限制的论文，3 个架构（7B-14B 范围）的验证是合理的。Qwen 的评估确实可以更系统（增加更多 seed），但现有证据已经覆盖了主要的架构变体。真正缺失的是 **更大规模**（如 70B）的验证，这一点 R2 没有提到。

---

### Questions 回应

**[REBUT] R2-Q1: KL mask patterns 是否与 2:4 N:M sparsity 兼容？**
R2 的问题合理但超出了论文的 scope。论文处理的是 unstructured activation sparsity（与 TEAL 相同），而 2:4 N:M 是 structured weight sparsity pattern。这是两个不同的问题设定。MaskLLM 处理 N:M weight masks，本文处理 contextual activation masks——不应期望 activation mask 直接满足 N:M 结构约束。实际部署需要的是 block-sparse kernel（如 Triton block-sparse）而非 2:4 N:M，因为 activation mask 是 input-dependent、layer-varying 的。论文在 Appendix A (appendix.tex L32-33) 提到了这一点。

**[REBUT] R2-Q2: τ annealing 是否过快？**
论文在 Appendix B.1 (Table 7) 已经回答了这个问题：fixed τ=0.5 (PPL 11.861) 实际上 **略优于** linear 1.0→0.1 (PPL 11.963)，而 fixed τ=0.1 (PPL 12.072) 最差。整体变化范围 <1.8%，说明温度策略对最终结果影响很小。Final ~100 steps 的 mild loss increase（Appendix C, appendix.tex L144-145）被解释为 masks 趋向 binary 时 discrete rounding noise 的正常表现，而非退火过快的症状。如果退火过快，我们预期会看到更大的 loss spike，但实际观察到的只是 mild increase。

**[AGREE] R2-Q3: 首次 token 延迟**
合理的工程问题。论文的 predictor 在每一层取 x^(ℓ)（attention 后的 hidden state）作为输入，然后预测该层的 mask，因此可以与 base model 的 layer-by-layer forward pass 并行或串行执行。但论文的 latency 测量（Appendix A, Table 5）只报告了 steady-state throughput（100 forward passes 的平均），没有单独报告 first-token latency。对于 autoregressive generation 的 prefill 阶段，predictor 在每个 token 位置独立运行，所以 first-token 不应有额外开销（相对于后续 token）。但这一点论文确实没有明确说明。

**[REBUT] R2-Q4: Table 3 中数字引用有误**
R2 引用 "KL predictor (11.79) vs BCE on KL targets (13.13)"，但这些数字与论文 Table 3 不匹配：
- 50% s42: C1 PPL = **11.96**, KL PPL = **11.96**（几乎完全匹配，gap ≤0.79pp across all metrics）
- 30% s42: C1 PPL = 9.45, KL PPL = 8.82（gap 0.63pp，但 s42 oracle 来自 non-seed-matched earlier checkpoint）
- 30% s123/s456（seed-matched oracles）: C1 PPL 8.84/8.82, KL PPL 8.83/8.79（gap ≤0.03pp）

论文中 **不存在 13.13** 这个数值。11.79 出现在 Table 5 (ablation) 作为 50% 的 forward KL PPL，不在 Table 3 (C1 ablation) 中。R2 可能混淆了不同 table 的数字。实际上 C1 ablation 的结论是 mask patterns **高度可迁移**——在 seed-matched 条件下 gap ≤0.03pp，这恰恰支持了论文的 claim，而非质疑它。

**[AGREE] R2-Q5: n=3 seeds 对高方差 downstream tasks 是否足够**
完全同意，与我的 W3 一致。PPL 的 σ=0.02 (CV=0.2%) 使 3 seeds 完全足够。但 MMLU 在 30% global 下 σ=9.5pp (CV=26.6%)、Qwen GSM8K σ=5.3pp (CV=16.5%)、Mistral ARC-c σ=6.4pp (CV=14.3%) 意味着 3 seeds 无法产生有意义的置信区间。论文在 §4.2 中正确地将 PPL 作为 primary metric，但在多处对高方差 downstream 指标做了 directional claims，应加上 "statistically indeterminate" 限定语。

---

### 综合评价

R2 的整体打分 3.0 (Findings) 在我看来偏低。R2 最有力的论点是 W2（知识任务退化分析不足）和 W5（contribution labeling），但 W1（MaskLLM 重叠）和 W6（跨架构泛化不足）被过度强调：

- W1 忽视了论文真正的贡献是 **empirical characterization**（5 loss 比较 + ablation framework），不是 method novelty
- W6 低估了 3 个架构、7-14B 范围、含 3-seed Mistral 评估的充分性
- Q4 引用了论文中不存在的数字 (13.13)，这降低了该 question 的可信度

我维持 3.5 (Borderline Conference) 的评分。论文的 PPL 改进真实可信，实验框架设计有价值，坦诚度高于平均水平。主要扣分在于 §4.5 的 confounded decomposition 被 overclaim（我的 N1）和知识任务退化缺乏深入分析（我的 N2 / R2-W2）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c62c8207-24ea-4b63-8a7c-967d430c0c9e",
  "isSidechain": false,
  "promptId": "f8e70eb5-ab02-4ce9-944a-ff43f2da2847",
  "type": "user",
  "uuid": "056585f7-2dff-41f7-b717-4657b72fb6e7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e",
  "sessionId": "6fcc51f2-1ca3-40c0-abb8-7c20f7122b8a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
